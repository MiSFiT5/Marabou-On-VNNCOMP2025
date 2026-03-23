#!/usr/bin/env python3
"""
Generate MNIST verification reports from experiment results.

Reads table3_results.csv files from nap_verify/experiments/mnist256x*_c*_*/
and produces markdown reports in mnist_reports/.

Usage:
    python generate_mnist_reports.py
"""
import os, re, glob, math
from collections import defaultdict
from datetime import datetime
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = SCRIPT_DIR
NAP_DIR = os.path.join(os.path.dirname(os.path.dirname(REPO_ROOT)), "nap_verify")
EXP_ROOT = os.path.join(NAP_DIR, "experiments")
OUT_DIR = os.path.join(REPO_ROOT, "mnist_reports")

# mnist256x{layers}_c{class}_alpha{alpha}
# mnist256x{layers}_c{class}_alpha{alpha}_layer_L{XY}
# mnist256x{layers}_c{class}_impl_ablation_alpha{alpha}
EXP_RE = re.compile(
    r"mnist256x(\d+)_c(\d+)"
    r"(?:_(impl_ablation))?"
    r"_?alpha([\d.]+)"
    r"(?:_layer_(L\d\d))?"
)

NUM_CLASSES = 10
EPSILONS = [0.02, 0.05, 0.10, 0.20]
ALPHAS = [0.90, 0.95, 0.99]
MODELS = [("mnist256x2", 2), ("mnist256x4", 4), ("mnist256x6", 6)]
VALID_RESULTS = {"Y", "N", "T/o"}
MODEL_ONNX = {
    "mnist256x2": "mnist-net_256x2.onnx",
    "mnist256x4": "mnist-net_256x4.onnx",
    "mnist256x6": "mnist-net_256x6.onnx",
}
MODEL_LAYERS = {
    "mnist256x2": ["L01"],
    "mnist256x4": ["L01", "L12", "L23"],
    "mnist256x6": ["L01", "L12", "L23", "L34", "L45"],
}


def load_all_data():
    """Load all per-class MNIST CSVs into a single DataFrame."""
    rows = []
    pattern = os.path.join(EXP_ROOT, "mnist256x*_c*", "verification_results", "table3_results.csv")
    csv_files = sorted(glob.glob(pattern))

    layer_pattern = os.path.join(EXP_ROOT, "mnist256x*_c*_layer_*", "verification_results", "table3_results.csv")
    csv_files += sorted(glob.glob(layer_pattern))

    impl_pattern = os.path.join(EXP_ROOT, "mnist256x*_c*_impl_ablation_*", "verification_results", "table3_results.csv")
    csv_files += sorted(glob.glob(impl_pattern))

    csv_files = sorted(set(csv_files))
    print(f"Found {len(csv_files)} MNIST CSV files")

    for f in csv_files:
        dirname = os.path.basename(os.path.dirname(os.path.dirname(f)))
        m = EXP_RE.match(dirname)
        if not m:
            continue
        n_layers, class_id, impl_abl, alpha, layer = m.groups()

        model_name = f"mnist256x{n_layers}"
        if impl_abl:
            exp_type = "C_impl_ablation"
        elif layer:
            exp_type = "B_per_layer"
        else:
            exp_type = "A_full_rule"

        try:
            df = pd.read_csv(f)
        except Exception:
            continue

        df["model"] = model_name
        df["n_layers"] = int(n_layers)
        df["class_id_exp"] = int(class_id)
        df["alpha"] = float(alpha)
        df["exp_type"] = exp_type
        df["layer_pair"] = layer if layer else "all"
        rows.append(df)

    if not rows:
        print("No data found!")
        return pd.DataFrame()
    return pd.concat(rows, ignore_index=True)


def fmt_cell(result, time_s):
    if result == "-":
        return "–"
    t = f"{time_s:.1f}" if time_s < 10 else str(int(round(time_s)))
    if result == "Y":
        return f"Y<br><sub>{t}s</sub>"
    elif result == "T/o":
        return f"T/o<br><sub>{t}s</sub>"
    else:
        return f"N<br><sub>{t}s</sub>"


def valid_rows(df):
    """Keep only rows that correspond to actual verification queries."""
    return df[df["result"].isin(VALID_RESULTS)].copy()


def dedupe_baseline_queries(df, keep_alpha=False):
    """
    Collapse repeated baseline executions to one canonical run per unique query.

    Baseline rows are duplicated across alpha directories and across
    per-layer / impl-ablation experiment folders. Summary tables should count
    each `(model, class, ε, target)` query once rather than every rerun.
    """
    if df.empty:
        return df.copy()

    key_cols = [c for c in ["model", "class_id_exp", "epsilon", "target_label"] if c in df.columns]
    if keep_alpha and "alpha" in df.columns:
        key_cols.append("alpha")

    sort_cols = [c for c in ["model", "class_id_exp", "epsilon", "target_label", "exp_type", "alpha", "layer_pair", "time_s"] if c in df.columns]
    return df.sort_values(sort_cols).drop_duplicates(subset=key_cols, keep="first").copy()


def any_verified_stats(df, group_cols):
    """Return (verified_queries, total_queries) after collapsing rule-row duplicates."""
    if df.empty:
        return 0, 0
    best = df.groupby(group_cols)["result"].apply(lambda s: (s == "Y").any())
    return int(best.sum()), int(len(best))


def build_detail_table(df_rule, true_class):
    lines = []
    targets = list(range(NUM_CLASSES))
    header = "| ε |" + "|".join(f" →{t} " for t in targets) + "| Y/total |"
    sep = "|---|" + "|".join(["---"] * NUM_CLASSES) + "|---|"
    lines.append(header)
    lines.append(sep)

    for eps in EPSILONS:
        eps_df = df_rule[abs(df_rule["epsilon"] - eps) < 1e-6]
        cells = []
        y_count = 0
        total = 0
        for t in targets:
            row = eps_df[eps_df["target_label"] == t]
            if t == true_class:
                cells.append("–")
                continue
            if len(row) == 0:
                cells.append("?")
                continue
            r = row.iloc[0]
            cells.append(fmt_cell(r["result"], r["time_s"]))
            if r["result"] in ("Y", "N", "T/o"):
                total += 1
                if r["result"] == "Y":
                    y_count += 1
        pct = f"{y_count/total*100:.0f}%" if total > 0 else "–"
        row_str = f"| `{eps:.2f}` |" + "|".join(f" {c} " for c in cells) + f"| {y_count}/{total} ({pct}) |"
        lines.append(row_str)
    return "\n".join(lines)


def generate_model_report(model_name, model_data):
    n_layers = model_data["n_layers"].iloc[0]
    onnx = MODEL_ONNX[model_name]
    layer_pairs = MODEL_LAYERS[model_name]

    classes = sorted(model_data["class_id_exp"].unique())
    missing_classes = [c for c in range(NUM_CLASSES) if c not in classes]
    exp_types = sorted(model_data["exp_type"].unique())

    lines = []
    lines.append(f"# MNIST Report: {model_name}")
    lines.append("")
    lines.append(f"> **MNIST** — {model_name} ({n_layers} hidden layers, 256 neurons each)  ")
    lines.append(f"> Per-class experiments, no rule cap  ")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"**Model file:** `{onnx}`  ")
    lines.append(f"**Architecture:** 784 → {'256 → ' * n_layers}10  ")
    lines.append(f"**Classes with at least one experiment:** {', '.join(str(c) for c in classes)} ({len(classes)} total)  ")
    if missing_classes:
        lines.append(f"**Missing classes in current results:** {', '.join(str(c) for c in missing_classes)}  ")
    lines.append(f"**Layer pairs:** {', '.join(layer_pairs)}  ")
    lines.append(f"**Experiment types:** {', '.join(et.replace('A_', '').replace('B_', '').replace('C_', '') for et in exp_types)}")
    lines.append("")

    ver = valid_rows(model_data)
    full_rule_nap = ver[(ver["exp_type"] == "A_full_rule") & ~ver["table"].str.contains("baseline", case=False, na=False)]

    lines.append("## How To Read Counts")
    lines.append("")
    lines.append("- `Classes with at least one experiment` means the classes that appear anywhere in the current result directory; missing classes have no report rows yet.")
    lines.append("- `Aggregated Summary` below is row-level: each rule family contributes its own verification rows, so denominators grow with the number of rule families shown.")
    lines.append("- In `Per-Layer`, shared unary / baseline rows are repeated once per layer-pair directory; this section reports those raw reruns because it is a per-experiment summary.")
    lines.append("- `Full-Rule Unique Query Coverage` collapses rule-row duplicates and answers the simpler question: for a `(class, ε, target)` query, did any full-rule NAP rule verify it?")
    lines.append("")

    if len(full_rule_nap) > 0:
        lines.append("## Full-Rule Unique Query Coverage")
        lines.append("")
        lines.append("At least one NAP rule type achieves `Y` for a given `(class, ε, target)` query.")
        lines.append("")
        lines.append("| α | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
        lines.append("|---|--------|--------|--------|--------|")
        for alpha in ALPHAS:
            adf = full_rule_nap[abs(full_rule_nap["alpha"] - alpha) < 1e-6]
            if len(adf) == 0:
                continue
            cells = []
            for eps in EPSILONS:
                edf = adf[abs(adf["epsilon"] - eps) < 1e-6]
                ny, n = any_verified_stats(edf, ["class_id_exp", "target_label"])
                pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
                cells.append(f"{ny}/{n} ({pct})")
            lines.append(f"| {alpha:.2f} | {' | '.join(cells)} |")
        lines.append("")

    # ── Aggregated summary ──
    lines.append("---")
    lines.append("")
    lines.append("## Aggregated Summary (row-level counts across all classes)")
    lines.append("")

    for exp_label, exp_key in [("Full-Rule", "A_full_rule"), ("Per-Layer", "B_per_layer"), ("Impl Ablation", "C_impl_ablation")]:
        exp_df = ver[ver["exp_type"] == exp_key]
        if len(exp_df) == 0:
            continue

        lines.append(f"### {exp_label}")
        lines.append("")

        for alpha in ALPHAS:
            adf = exp_df[abs(exp_df["alpha"] - alpha) < 1e-6]
            if len(adf) == 0:
                continue

            lines.append(f"#### α = {alpha}")
            lines.append("")
            lines.append("| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |")
            lines.append("|------|--------|--------|--------|--------|----------|")

            for tbl in sorted(adf["table"].unique()):
                tdf = adf[adf["table"] == tbl]
                cells = []
                total_y = 0
                total_n = 0
                for eps in EPSILONS:
                    edf = tdf[abs(tdf["epsilon"] - eps) < 1e-6]
                    n = len(edf)
                    ny = (edf["result"] == "Y").sum()
                    total_y += ny
                    total_n += n
                    pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
                    cells.append(f"{ny}/{n} ({pct})")
                overall = f"{total_y/total_n*100:.1f}%" if total_n > 0 else "–"
                lines.append(f"| `{tbl}` | {' | '.join(cells)} | {overall} |")

            lines.append("")

    # ── Per-class detailed sections ──
    lines.append("---")
    lines.append("")
    lines.append("## Per-Class Details")
    lines.append("")

    for cls in classes:
        cls_data = model_data[model_data["class_id_exp"] == cls]

        lines.append(f"### Class {cls}")
        lines.append("")
        if "center_source" in cls_data.columns:
            cs = cls_data["center_source"].dropna().unique()
            if len(cs) > 0:
                lines.append(f"Reference point: `{cs[0]}`  ")
        lines.append("")

        for exp_label, exp_key in [("Full-Rule", "A_full_rule"), ("Per-Layer", "B_per_layer"), ("Impl Ablation", "C_impl_ablation")]:
            exp_df = cls_data[cls_data["exp_type"] == exp_key]
            if len(exp_df) == 0:
                continue

            lines.append(f"#### {exp_label}")
            lines.append("")

            for alpha in ALPHAS:
                adf = exp_df[abs(exp_df["alpha"] - alpha) < 1e-6]
                if len(adf) == 0:
                    continue

                if exp_key == "B_per_layer":
                    lps = sorted(adf["layer_pair"].unique())
                else:
                    lps = [None]

                for lp in lps:
                    if lp is not None:
                        lpdf = adf[adf["layer_pair"] == lp]
                    else:
                        lpdf = adf

                    for tbl_name in sorted(lpdf["table"].unique()):
                        tdf = lpdf[lpdf["table"] == tbl_name]
                        true_class = cls
                        ver_tdf = tdf[tdf["result"].isin(["Y", "N", "T/o"])]
                        ny = (ver_tdf["result"] == "Y").sum()
                        nt = len(ver_tdf)
                        pct = f"{ny/nt*100:.1f}%" if nt > 0 else "–"

                        if lp is not None:
                            lines.append(f"##### {tbl_name} ({lp}) — Y={ny}/{nt} ({pct})")
                        else:
                            lines.append(f"##### {tbl_name} — Y={ny}/{nt} ({pct})")
                        lines.append("")
                        lines.append(build_detail_table(tdf, true_class))
                        lines.append("")

    return "\n".join(lines)


def generate_aggregated_report(data):
    ver = valid_rows(data)
    bl = ver[ver["table"].str.contains("baseline", case=False, na=False)]
    nap = ver[~ver["table"].str.contains("baseline", case=False, na=False)]
    bl_unique = dedupe_baseline_queries(bl)

    lines = []
    lines.append("# MNIST — Aggregated Results")
    lines.append("")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}  ")
    lines.append(f"> Experiments: per-class, no rule cap")
    lines.append("")
    lines.append(f"- **Total CSV rows:** {len(data):,}")
    lines.append(f"- **Verification rows (excl skipped):** {len(ver):,}")
    lines.append(f"- **Models:** {', '.join(sorted(data['model'].unique()))}")
    lines.append(f"- **Classes:** 0–9")
    n_full = data[data["exp_type"] == "A_full_rule"].groupby(["model", "class_id_exp", "alpha"]).ngroups
    n_layer = data[data["exp_type"] == "B_per_layer"].groupby(["model", "class_id_exp", "alpha", "layer_pair"]).ngroups
    n_impl = data[data["exp_type"] == "C_impl_ablation"].groupby(["model", "class_id_exp", "alpha"]).ngroups
    lines.append(f"- **Full-rule experiments:** {n_full}")
    lines.append(f"- **Per-layer experiments:** {n_layer}")
    lines.append(f"- **Impl ablation experiments:** {n_impl}")
    lines.append("")

    lines.append("## How To Read Counts")
    lines.append("")
    lines.append("- The baseline table below is deduplicated to one canonical run per unique query `(model, class, ε, target)`.")
    lines.append("- `Any-rule verified` collapses all full-rule NAP families for a fixed `(model, class, α, ε, target)` query.")
    lines.append("- `Row-level totals` keep every rule-row separately, so denominators scale with how many rule families exist for that model.")
    lines.append("")

    lines.append("## Baseline (deduplicated unique queries)")
    lines.append("")
    for model_name, _ in MODELS:
        mbl = bl_unique[bl_unique["model"] == model_name]
        if len(mbl) == 0:
            continue
        lines.append(f"### {model_name}")
        lines.append("")
        lines.append("| ε | Y | N | T/o | Total | Verified % |")
        lines.append("|---|---|---|-----|-------|-----------|")
        for eps in EPSILONS:
            edf = mbl[abs(mbl["epsilon"] - eps) < 1e-6]
            n = len(edf)
            ny = (edf["result"] == "Y").sum()
            nn = (edf["result"] == "N").sum()
            nto = (edf["result"] == "T/o").sum()
            pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
            lines.append(f"| {eps:.2f} | {ny} | {nn} | {nto} | {n} | {pct} |")
        lines.append("")

    nap_a = nap[nap["exp_type"] == "A_full_rule"]

    lines.append("## Full-Rule NAP — any-rule verified per unique query")
    lines.append("")
    lines.append("At least one NAP rule type achieves `Y` for a given `(model, class, ε, target)` query.")
    lines.append("")
    for model_name, _ in MODELS:
        mdf = nap_a[nap_a["model"] == model_name]
        if len(mdf) == 0:
            continue
        lines.append(f"### {model_name}")
        lines.append("")
        lines.append("| α | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
        lines.append("|---|--------|--------|--------|--------|")
        for alpha in ALPHAS:
            adf = mdf[abs(mdf["alpha"] - alpha) < 1e-6]
            cells = []
            for eps in EPSILONS:
                edf = adf[abs(adf["epsilon"] - eps) < 1e-6]
                ny, n = any_verified_stats(edf, ["class_id_exp", "target_label"])
                pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
                cells.append(f"{ny}/{n} ({pct})")
            lines.append(f"| {alpha:.2f} | {' | '.join(cells)} |")
        lines.append("")

    lines.append("## Full-Rule NAP — row-level totals across all rule rows")
    lines.append("")
    lines.append("Each rule family contributes its own verification rows, so these percentages are not deduplicated across rule families.")
    lines.append("")
    for model_name, _ in MODELS:
        mdf = nap_a[nap_a["model"] == model_name]
        if len(mdf) == 0:
            continue
        lines.append(f"### {model_name}")
        lines.append("")
        lines.append("| α | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
        lines.append("|---|--------|--------|--------|--------|")
        for alpha in ALPHAS:
            adf = mdf[abs(mdf["alpha"] - alpha) < 1e-6]
            cells = []
            for eps in EPSILONS:
                edf = adf[abs(adf["epsilon"] - eps) < 1e-6]
                n = len(edf)
                ny = (edf["result"] == "Y").sum()
                pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
                cells.append(f"{ny}/{n} ({pct})")
            lines.append(f"| {alpha:.2f} | {' | '.join(cells)} |")
        lines.append("")

    lines.append("## Rule Type Breakdown (ε=0.02, row-level)")
    lines.append("")
    for model_name, _ in MODELS:
        mdf = nap_a[(nap_a["model"] == model_name) & (abs(nap_a["epsilon"] - 0.02) < 1e-6)]
        if len(mdf) == 0:
            continue
        lines.append(f"### {model_name}")
        lines.append("")
        lines.append("| Rule Type | α=0.90 | α=0.95 | α=0.99 |")
        lines.append("|-----------|--------|--------|--------|")

        base_re = re.compile(r"^(.+?)\s*\(α=[\d.]+\)$")
        base_names = []
        seen = set()
        for tbl in sorted(mdf["table"].unique()):
            bm = base_re.match(tbl)
            base = bm.group(1) if bm else tbl
            if base not in seen:
                seen.add(base)
                base_names.append(base)

        for base in base_names:
            cells = []
            for alpha in ALPHAS:
                tbl_name = f"{base} (α={alpha})"
                tdf = mdf[(mdf["table"] == tbl_name) & (abs(mdf["alpha"] - alpha) < 1e-6)]
                n = len(tdf)
                ny = (tdf["result"] == "Y").sum()
                pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
                cells.append(f"{ny}/{n} ({pct})")
            lines.append(f"| `{base}` | {' | '.join(cells)} |")
        lines.append("")

    lines.append("## Speedup Analysis")
    lines.append("")
    exp_a = ver[ver["exp_type"] == "A_full_rule"]
    bl_times = dedupe_baseline_queries(exp_a[exp_a["table"].str.contains("baseline", case=False, na=False)])[
        ["model", "class_id_exp", "epsilon", "target_label", "result", "time_s"]
    ].rename(columns={"result": "bl_result", "time_s": "bl_time"})
    nap_times = exp_a[~exp_a["table"].str.contains("baseline", case=False, na=False)]
    nap_verified = nap_times[nap_times["result"] == "Y"]

    if len(nap_verified) > 0:
        nap_best = nap_verified.groupby(
            ["model", "class_id_exp", "epsilon", "target_label"]
        )["time_s"].min().reset_index().rename(columns={"time_s": "nap_time"})

        bl_y = bl_times[bl_times["bl_result"] == "Y"]
        both = bl_y.merge(nap_best, on=["model", "class_id_exp", "epsilon", "target_label"], how="inner")
        if len(both) > 0:
            both["speedup"] = both["bl_time"] / both["nap_time"].clip(lower=0.001)
            lines.append(f"- **Both verify Y:** {len(both)} unique queries")
            lines.append(f"- **Mean speedup:** {both['speedup'].mean():.1f}x (median {both['speedup'].median():.1f}x)")
            lines.append(f"- **Mean baseline time:** {both['bl_time'].mean():.2f}s")
            lines.append(f"- **Mean NAP time:** {both['nap_time'].mean():.2f}s")

        bl_fail = bl_times[bl_times["bl_result"].isin(["N", "T/o"])]
        rescued = bl_fail.merge(nap_best, on=["model", "class_id_exp", "epsilon", "target_label"], how="inner")
        lines.append(f"- **Baseline fails, NAP verifies:** {len(rescued)} unique queries")
        if len(rescued) > 0:
            lines.append(f"  - From timeout: {(rescued['bl_result'] == 'T/o').sum()}")
            lines.append(f"  - From falsified: {(rescued['bl_result'] == 'N').sum()}")
    lines.append("")

    lines.append("## Per-Model Summary")
    lines.append("")
    lines.append("| Model | Layers | Classes With Data | Full-Rule Groups | Per-Layer Groups | Impl Ablation Groups | Best Row-Level Y% (ε=0.02, α=0.90) |")
    lines.append("|-------|--------|-------------------|------------------|------------------|----------------------|------------------------------------|")
    for model_name, n_layers in MODELS:
        mdf = data[data["model"] == model_name]
        if len(mdf) == 0:
            continue
        n_cls = mdf["class_id_exp"].nunique()
        n_fr = mdf[mdf["exp_type"] == "A_full_rule"].groupby(["class_id_exp", "alpha"]).ngroups
        n_pl = mdf[mdf["exp_type"] == "B_per_layer"].groupby(["class_id_exp", "alpha", "layer_pair"]).ngroups
        n_ia = mdf[mdf["exp_type"] == "C_impl_ablation"].groupby(["class_id_exp", "alpha"]).ngroups

        mver = valid_rows(mdf[(mdf["exp_type"] == "A_full_rule")
                    & (abs(mdf["epsilon"] - 0.02) < 1e-6) & (abs(mdf["alpha"] - 0.90) < 1e-6)])
        mnap = mver[~mver["table"].str.contains("baseline", case=False, na=False)]
        if len(mnap) > 0:
            ny = (mnap["result"] == "Y").sum()
            best_pct = f"{ny/len(mnap)*100:.1f}%"
        else:
            best_pct = "–"

        lines.append(
            f"| [{model_name}]({model_name}.md) | {n_layers} | {n_cls} | "
            f"{n_fr} | {n_pl} | {n_ia} | {best_pct} |"
        )
    lines.append("")

    return "\n".join(lines)


def generate_readme(data):
    lines = []
    lines.append("# MNIST Verification Reports")
    lines.append("")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append("## Models")
    lines.append("")
    lines.append("| Model | Architecture | ONNX | Layer Pairs | Classes With Data |")
    lines.append("|-------|-------------|------|-------------|-------------------|")
    for model_name, n_layers in MODELS:
        onnx = MODEL_ONNX[model_name]
        lps = MODEL_LAYERS[model_name]
        arch = f"784 → {'256 → ' * n_layers}10"
        classes = sorted(int(c) for c in data[data["model"] == model_name]["class_id_exp"].dropna().unique())
        class_desc = ", ".join(str(c) for c in classes) if classes else "–"
        lines.append(f"| [{model_name}]({model_name}.md) | {arch} | `{onnx}` | {', '.join(lps)} | {class_desc} |")
    lines.append("")

    lines.append("## Experiment Types")
    lines.append("")
    lines.append("| Label | Description |")
    lines.append("|-------|-------------|")
    lines.append("| Full-Rule | All rule types from all layers combined |")
    lines.append("| Per-Layer | Single layer pair at a time |")
    lines.append("| Impl Ablation | Each implication direction tested separately |")
    lines.append("")

    lines.append("## How To Read Counts")
    lines.append("")
    lines.append("- Baseline counts are deduplicated to one canonical run per `(model, class, ε, target)` query.")
    lines.append("- `Any-rule verified` collapses all full-rule NAP families for a fixed `(model, class, α, ε, target)` query.")
    lines.append("- `Row-level totals` count every rule-row separately, so the denominator grows with the number of rule families.")
    lines.append("")

    lines.append("## Reports")
    lines.append("")
    lines.append("- **[All_Models_Aggregated.md](All_Models_Aggregated.md)** — Overall statistics and comparison")
    lines.append("")
    lines.append("### Per-Model Reports")
    lines.append("")
    for model_name, _ in MODELS:
        lines.append(f"- [{model_name}]({model_name}.md)")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Analysis")
    lines.append("")
    lines.append("See [All_Models_Aggregated.md](All_Models_Aggregated.md) for full tables.")
    lines.append("")

    ver = valid_rows(data)
    bl = dedupe_baseline_queries(ver[ver["table"].str.contains("baseline", case=False, na=False)])
    nap_a = ver[(ver["exp_type"] == "A_full_rule") & ~ver["table"].str.contains("baseline", case=False, na=False)]

    lines.append("### Baseline Performance")
    lines.append("")
    for model_name, _ in MODELS:
        mbl = bl[bl["model"] == model_name]
        if len(mbl) == 0:
            continue
        for eps in [0.02, 0.05]:
            edf = mbl[abs(mbl["epsilon"] - eps) < 1e-6]
            ny = (edf["result"] == "Y").sum()
            n = len(edf)
            pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
            lines.append(f"- **{model_name}** ε={eps:.2f}: {ny}/{n} ({pct})")
    lines.append("")

    lines.append("### Full-Rule NAP — Any-Rule Verified (α=0.90)")
    lines.append("")
    lines.append("| Model | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
    lines.append("|-------|--------|--------|--------|--------|")
    for model_name, _ in MODELS:
        mdf = nap_a[(nap_a["model"] == model_name) & (abs(nap_a["alpha"] - 0.90) < 1e-6)]
        if len(mdf) == 0:
            continue
        cells = []
        for eps in EPSILONS:
            edf = mdf[abs(mdf["epsilon"] - eps) < 1e-6]
            ny, n = any_verified_stats(edf, ["class_id_exp", "target_label"])
            pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
            cells.append(f"{ny}/{n} ({pct})")
        lines.append(f"| {model_name} | {' | '.join(cells)} |")
    lines.append("")

    lines.append("### Full-Rule NAP — Row-Level Totals (α=0.90)")
    lines.append("")
    lines.append("| Model | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
    lines.append("|-------|--------|--------|--------|--------|")
    for model_name, _ in MODELS:
        mdf = nap_a[(nap_a["model"] == model_name) & (abs(nap_a["alpha"] - 0.90) < 1e-6)]
        if len(mdf) == 0:
            continue
        cells = []
        for eps in EPSILONS:
            edf = mdf[abs(mdf["epsilon"] - eps) < 1e-6]
            ny = (edf["result"] == "Y").sum()
            n = len(edf)
            pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
            cells.append(f"{ny}/{n} ({pct})")
        lines.append(f"| {model_name} | {' | '.join(cells)} |")
    lines.append("")

    lines.append("### Key Findings")
    lines.append("")
    missing_mnist256x4 = sorted(set(range(NUM_CLASSES)) - set(int(c) for c in data[data["model"] == "mnist256x4"]["class_id_exp"].dropna().unique()))
    if missing_mnist256x4:
        lines.append(f"- **mnist256x4 is still incomplete:** missing classes {', '.join(str(c) for c in missing_mnist256x4)}.")

    exp_a = ver[ver["exp_type"] == "A_full_rule"]
    bl_times = dedupe_baseline_queries(exp_a[exp_a["table"].str.contains("baseline", case=False, na=False)])[
        ["model", "class_id_exp", "epsilon", "target_label", "result", "time_s"]
    ].rename(columns={"result": "bl_result", "time_s": "bl_time"})
    nap_v = nap_a[nap_a["result"] == "Y"]
    if len(nap_v) > 0:
        nap_best = nap_v.groupby(
            ["model", "class_id_exp", "epsilon", "target_label"]
        )["time_s"].min().reset_index().rename(columns={"time_s": "nap_time"})
        bl_fail = bl_times[bl_times["bl_result"].isin(["N", "T/o"])]
        rescued = bl_fail.merge(nap_best, on=["model", "class_id_exp", "epsilon", "target_label"], how="inner")
        lines.append(f"- **{len(rescued)} unique rescue queries:** baseline returns `N` or `T/o`, but some NAP rule verifies.")

        bl_y = bl_times[bl_times["bl_result"] == "Y"]
        both = bl_y.merge(nap_best, on=["model", "class_id_exp", "epsilon", "target_label"], how="inner")
        if len(both) > 0:
            both["speedup"] = both["bl_time"] / both["nap_time"].clip(lower=0.001)
            lines.append(f"- **{both['speedup'].mean():.1f}x mean speedup** on {len(both)} unique queries where both baseline and NAP verify.")
    lines.append("")

    lines.append("### Rule Type Ranking (ε=0.02, α=0.90, row-level)")
    lines.append("")
    for model_name, _ in MODELS:
        mdf = nap_a[(nap_a["model"] == model_name) & (abs(nap_a["alpha"] - 0.90) < 1e-6) & (abs(nap_a["epsilon"] - 0.02) < 1e-6)]
        if len(mdf) == 0:
            continue
        lines.append(f"**{model_name}:**")
        lines.append("")
        lines.append("| Rule Type | Y% |")
        lines.append("|-----------|-----|")
        base_re = re.compile(r"^(.+?)\s*\(α=[\d.]+\)$")
        type_stats = []
        for tbl in sorted(mdf["table"].unique()):
            tdf = mdf[mdf["table"] == tbl]
            ny = (tdf["result"] == "Y").sum()
            n = len(tdf)
            bm = base_re.match(tbl)
            base = bm.group(1) if bm else tbl
            if n > 0:
                type_stats.append((base, ny, n, ny / n * 100))
        type_stats.sort(key=lambda x: -x[3])
        for base, ny, n, pct in type_stats:
            lines.append(f"| {base} | {ny}/{n} ({pct:.1f}%) |")
        lines.append("")

    lines.append("### Depth Effect (row-level, α=0.90)")
    lines.append("")
    for eps in [0.02, 0.05]:
        vals = []
        for model_name, _ in MODELS:
            mdf = nap_a[(nap_a["model"] == model_name) & (abs(nap_a["alpha"] - 0.90) < 1e-6) & (abs(nap_a["epsilon"] - eps) < 1e-6)]
            if len(mdf) == 0:
                continue
            ny = (mdf["result"] == "Y").sum()
            n = len(mdf)
            pct = ny / n * 100 if n > 0 else 0
            vals.append(f"{model_name}: {ny}/{n} ({pct:.1f}%)")
        if vals:
            lines.append(f"- **ε={eps:.2f}:** {' | '.join(vals)}")
    lines.append("")

    return "\n".join(lines)


def main():
    print("Loading data...")
    data = load_all_data()
    if data.empty:
        return

    print(f"Loaded {len(data)} rows")
    print(f"  Models: {sorted(data['model'].unique())}")
    print(f"  Exp types: {sorted(data['exp_type'].unique())}")
    print(f"  Full-rule (model, class, alpha) groups: "
          f"{data[data['exp_type'] == 'A_full_rule'].groupby(['model', 'class_id_exp', 'alpha']).ngroups}")

    os.makedirs(OUT_DIR, exist_ok=True)

    for model_name, _ in MODELS:
        mdata = data[data["model"] == model_name]
        if len(mdata) == 0:
            print(f"  No data for {model_name}, skipping")
            continue
        report = generate_model_report(model_name, mdata)
        fname = os.path.join(OUT_DIR, f"{model_name}.md")
        with open(fname, "w") as f:
            f.write(report)
        print(f"  Wrote {fname}")

    print("Generating aggregated report...")
    agg = generate_aggregated_report(data)
    with open(os.path.join(OUT_DIR, "All_Models_Aggregated.md"), "w") as f:
        f.write(agg)

    print("Generating README...")
    readme = generate_readme(data)
    with open(os.path.join(OUT_DIR, "README.md"), "w") as f:
        f.write(readme)

    print(f"\nDone! Reports written to {OUT_DIR}")


if __name__ == "__main__":
    main()

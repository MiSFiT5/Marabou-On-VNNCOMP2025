#!/usr/bin/env python3
"""
Generate per-property ACAS Xu verification reports from v2 experiment results.

Reads table3_results.csv files from nap_verify/experiments/acasxu_*_prop*/
and produces markdown reports in model_reports_per_property/.

Usage:
    python generate_per_property_reports.py
"""
import os, re, glob, math
from collections import defaultdict
from datetime import datetime
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = SCRIPT_DIR
NAP_DIR = os.path.join(os.path.dirname(os.path.dirname(REPO_ROOT)), "nap_verify")
EXP_ROOT = os.path.join(NAP_DIR, "experiments")
OUT_DIR = os.path.join(REPO_ROOT, "model_reports_per_property")

EXP_RE = re.compile(
    r"acasxu_ACASXU_run2a_(\d+)_(\d+)_batch_2000_prop(\d+)"
    r"(?:_(impl_ablation))?_?alpha([\d.]+)"
    r"(?:_layer_(L\d+L\d+))?"
)

NUM_CLASSES = 5
EPSILONS = [0.02, 0.05, 0.10, 0.20]
ALPHAS = [0.90, 0.95, 0.99]


def load_all_data():
    """Load all per-property CSVs into a single DataFrame."""
    rows = []
    pattern = os.path.join(EXP_ROOT, "acasxu_*_prop*", "verification_results", "table3_results.csv")
    csv_files = sorted(glob.glob(pattern))
    print(f"Found {len(csv_files)} per-property CSV files")

    for f in csv_files:
        dirname = os.path.basename(os.path.dirname(os.path.dirname(f)))
        m = EXP_RE.match(dirname)
        if not m:
            continue
        net_i, net_j, prop_id, impl_abl, alpha, layer = m.groups()

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

        df["net_i"] = int(net_i)
        df["net_j"] = int(net_j)
        df["model"] = f"{net_i}_{net_j}"
        df["prop"] = int(prop_id)
        df["alpha"] = float(alpha)
        df["exp_type"] = exp_type
        df["layer_pair"] = layer if layer else "all"
        rows.append(df)

    if not rows:
        print("No data found!")
        return pd.DataFrame()
    return pd.concat(rows, ignore_index=True)


def fmt_cell(result, time_s):
    """Format a single table cell."""
    if result == "-":
        return "–"
    t = int(round(time_s))
    if result == "Y":
        return f"🟢 Y<br><sub>{t}s</sub>"
    elif result == "T/o":
        return f"🟡 T/o<br><sub>{t}s</sub>"
    else:
        return f"🔴 N<br><sub>{t}s</sub>"


def build_detail_table(df_rule, true_class):
    """Build a per-class detail table for a single rule type and true class."""
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


def generate_model_report(model_key, model_data, all_data):
    """Generate a per-model report covering all properties."""
    net_i, net_j = model_key
    model_name = f"N{net_i},{net_j}"
    model_tag = f"N{net_i}_{net_j}"
    onnx_name = f"ACASXU_run2a_{net_i}_{net_j}_batch_2000.onnx"

    props = sorted(model_data["prop"].unique())
    exp_types_present = sorted(model_data["exp_type"].unique())

    lines = []
    lines.append(f"# Model Report: {model_name} (Per-Property)")
    lines.append("")
    lines.append(f"> **ACAS Xu** — {model_name}  ")
    lines.append(f"> Per-property experiments (property midpoint reference, no rule cap)  ")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"**Model file:** `{onnx_name}`  ")
    lines.append(f"**Properties covered:** {', '.join(f'prop{p}' for p in props)} ({len(props)} total)  ")
    lines.append(f"**Experiment types:** {', '.join(et.replace('A_', '').replace('B_', '').replace('C_', '') for et in exp_types_present)}")
    lines.append("")

    # ── Aggregated summary ────────────────────────────────────────────────
    ver = model_data[model_data["result"].isin(["Y", "N", "T/o"])]

    lines.append("---")
    lines.append("")
    lines.append("## Aggregated Summary (across all properties)")
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

    # ── Per-property detailed sections ────────────────────────────────────
    lines.append("---")
    lines.append("")
    lines.append("## Per-Property Details")
    lines.append("")

    for prop_id in props:
        prop_data = model_data[model_data["prop"] == prop_id]
        prop_ver = prop_data[prop_data["result"].isin(["Y", "N", "T/o"])]
        true_classes = sorted(prop_data[prop_data["result"] != "-"]["true_class"].dropna().unique())

        lines.append(f"### Property {prop_id}")
        lines.append("")
        if "center_source" in prop_data.columns:
            cs = prop_data["center_source"].dropna().unique()
            if len(cs) > 0:
                lines.append(f"Reference point: `{cs[0]}`  ")
        if true_classes:
            lines.append(f"True class(es): {', '.join(str(int(c)) for c in true_classes)}")
        lines.append("")

        # Full-rule experiments for this property
        for exp_label, exp_key in [("Full-Rule", "A_full_rule"), ("Per-Layer", "B_per_layer"), ("Impl Ablation", "C_impl_ablation")]:
            exp_df = prop_data[prop_data["exp_type"] == exp_key]
            if len(exp_df) == 0:
                continue

            lines.append(f"#### {exp_label}")
            lines.append("")

            for alpha in ALPHAS:
                adf = exp_df[abs(exp_df["alpha"] - alpha) < 1e-6]
                if len(adf) == 0:
                    continue

                if exp_key == "B_per_layer":
                    layer_pairs = sorted(adf["layer_pair"].unique())
                    tag = f"α={alpha}"
                else:
                    layer_pairs = [None]
                    tag = f"α={alpha}"

                for lp in layer_pairs:
                    if lp is not None:
                        lpdf = adf[adf["layer_pair"] == lp]
                        section_label = f"α={alpha}, {lp}"
                    else:
                        lpdf = adf
                        section_label = f"α={alpha}"

                    tables_in_section = sorted(lpdf["table"].unique())

                    for tbl_name in tables_in_section:
                        tdf = lpdf[lpdf["table"] == tbl_name]
                        for tc in sorted(tdf["true_class"].dropna().unique()):
                            tc = int(tc)
                            cdf = tdf[tdf["true_class"] == tc]
                            ver_cdf = cdf[cdf["result"].isin(["Y", "N", "T/o"])]
                            ny = (ver_cdf["result"] == "Y").sum()
                            nt = len(ver_cdf)
                            pct = f"{ny/nt*100:.1f}%" if nt > 0 else "–"

                            if lp is not None:
                                lines.append(f"##### {tbl_name} ({lp}, class {tc}) — Y={ny}/{nt} ({pct})")
                            else:
                                lines.append(f"##### {tbl_name} (class {tc}) — Y={ny}/{nt} ({pct})")
                            lines.append("")
                            lines.append(build_detail_table(cdf, tc))
                            lines.append("")

    return "\n".join(lines)


def generate_aggregated_report(data):
    """Generate the All_Models_Aggregated.md report."""
    ver = data[data["result"].isin(["Y", "N", "T/o"])]
    bl = ver[ver["table"].str.contains("baseline", case=False, na=False)]
    nap = ver[~ver["table"].str.contains("baseline", case=False, na=False)]

    lines = []
    lines.append("# ACAS Xu Per-Property — Aggregated Results")
    lines.append("")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}  ")
    lines.append(f"> Experiments: property midpoint reference, no rule cap (v2)")
    lines.append("")
    lines.append(f"- **Total CSV rows:** {len(data):,}")
    lines.append(f"- **Verification rows (excl skipped):** {len(ver):,}")
    lines.append(f"- **Unique models:** {data['model'].nunique()}")
    lines.append(f"- **Unique properties:** {sorted(int(p) for p in data['prop'].unique())}")
    lines.append(f"- **Unique (model, prop) pairs:** {data.groupby(['model', 'prop']).ngroups}")
    lines.append("")

    # ── Baseline ──────────────────────────────────────────────────────────
    lines.append("## Baseline (no NAP rules)")
    lines.append("")
    lines.append("| ε | Y | N | T/o | Total | Verified % |")
    lines.append("|---|---|---|-----|-------|-----------|")
    for eps in EPSILONS:
        edf = bl[abs(bl["epsilon"] - eps) < 1e-6]
        n = len(edf)
        ny = (edf["result"] == "Y").sum()
        nn = (edf["result"] == "N").sum()
        nto = (edf["result"] == "T/o").sum()
        pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
        lines.append(f"| {eps:.2f} | {ny} | {nn} | {nto} | {n} | {pct} |")
    lines.append("")

    # ── NAP full-rule by (alpha, epsilon) ─────────────────────────────────
    nap_a = nap[nap["exp_type"] == "A_full_rule"] if "exp_type" in nap.columns else nap
    if len(nap_a) == 0:
        nap_a = nap

    lines.append("## Full-Rule NAP — best across rule types per (model, prop)")
    lines.append("")
    lines.append("\"Any verified\" = at least one NAP rule type achieves Y for a given (model, prop, epsilon) pair.")
    lines.append("")
    lines.append("| α | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
    lines.append("|---|--------|--------|--------|--------|")
    for alpha in ALPHAS:
        adf = nap_a[abs(nap_a["alpha"] - alpha) < 1e-6]
        cells = []
        for eps in EPSILONS:
            edf = adf[abs(adf["epsilon"] - eps) < 1e-6]
            best = edf.groupby(["model", "prop"]).apply(
                lambda g: (g["result"] == "Y").any(), include_groups=False
            )
            n = len(best)
            ny = best.sum()
            pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
            cells.append(f"{ny}/{n} ({pct})")
        lines.append(f"| {alpha} | {' | '.join(cells)} |")
    lines.append("")

    # ── Rule type breakdown (eps=0.02) ────────────────────────────────────
    lines.append("## Rule Type Breakdown (ε=0.02, row-level)")
    lines.append("")
    lines.append("| Rule Type | α=0.90 | α=0.95 | α=0.99 |")
    lines.append("|-----------|--------|--------|--------|")

    nap_a_002 = nap_a[abs(nap_a["epsilon"] - 0.02) < 1e-6]
    base_re = re.compile(r"^(.+?)\s*\(α=[\d.]+\)$")
    base_names = []
    seen = set()
    for tbl in sorted(nap_a_002["table"].unique()):
        m = base_re.match(tbl)
        base = m.group(1) if m else tbl
        if base not in seen:
            seen.add(base)
            base_names.append(base)

    for base in base_names:
        cells = []
        for alpha in ALPHAS:
            alpha_label = f"α={alpha}"
            tbl_name = f"{base} ({alpha_label})"
            tdf = nap_a_002[(nap_a_002["table"] == tbl_name) & (abs(nap_a_002["alpha"] - alpha) < 1e-6)]
            n = len(tdf)
            ny = (tdf["result"] == "Y").sum()
            pct = f"{ny/n*100:.1f}%" if n > 0 else "–"
            cells.append(f"{ny}/{n} ({pct})")
        lines.append(f"| `{base}` | {' | '.join(cells)} |")
    lines.append("")

    # ── Speedup ───────────────────────────────────────────────────────────
    lines.append("## Speedup Analysis")
    lines.append("")
    exp_a_full = ver[ver["exp_type"] == "A_full_rule"] if "exp_type" in ver.columns else ver
    bl_times = exp_a_full[exp_a_full["table"].str.contains("baseline", case=False, na=False)][
        ["model", "prop", "epsilon", "target_label", "result", "time_s"]
    ].rename(columns={"result": "bl_result", "time_s": "bl_time"})
    nap_times = exp_a_full[~exp_a_full["table"].str.contains("baseline", case=False, na=False)]
    nap_verified = nap_times[nap_times["result"] == "Y"]

    if len(nap_verified) > 0:
        nap_best = nap_verified.groupby(
            ["model", "prop", "epsilon", "target_label"]
        )["time_s"].min().reset_index().rename(columns={"time_s": "nap_time"})

        bl_y = bl_times[bl_times["bl_result"] == "Y"]
        both = bl_y.merge(nap_best, on=["model", "prop", "epsilon", "target_label"], how="inner")
        if len(both) > 0:
            both["speedup"] = both["bl_time"] / both["nap_time"].clip(lower=0.01)
            lines.append(f"- **Both verify Y:** {len(both)} cases")
            lines.append(f"- **Mean speedup:** {both['speedup'].mean():.1f}x (median {both['speedup'].median():.1f}x)")
            lines.append(f"- **Mean baseline time:** {both['bl_time'].mean():.2f}s")
            lines.append(f"- **Mean NAP time:** {both['nap_time'].mean():.2f}s")

        bl_fail = bl_times[bl_times["bl_result"].isin(["N", "T/o"])]
        rescued = bl_fail.merge(nap_best, on=["model", "prop", "epsilon", "target_label"], how="inner")
        lines.append(f"- **Baseline fails, NAP verifies:** {len(rescued)} cases")
        if len(rescued) > 0:
            lines.append(f"  - From timeout: {(rescued['bl_result'] == 'T/o').sum()}")
            lines.append(f"  - From falsified: {(rescued['bl_result'] == 'N').sum()}")
    lines.append("")

    # ── Per-model summary table ───────────────────────────────────────────
    lines.append("## Per-Model Summary")
    lines.append("")
    lines.append("| Model | Props | Exp A | Exp B | Exp C | Best Y% (ε=0.02, α=0.90) |")
    lines.append("|-------|-------|-------|-------|-------|--------------------------|")

    for model in sorted(data["model"].unique(), key=lambda m: (int(m.split("_")[0]), int(m.split("_")[1]))):
        mdf = data[data["model"] == model]
        ni, nj = model.split("_")
        n_props = mdf["prop"].nunique()

        exp_counts = {}
        for et in ["A_full_rule", "B_per_layer", "C_impl_ablation"]:
            exp_counts[et] = mdf[mdf["exp_type"] == et].groupby(["prop", "alpha"]).ngroups

        mver = mdf[(mdf["result"].isin(["Y", "N", "T/o"])) & (mdf["exp_type"] == "A_full_rule")
                    & (abs(mdf["epsilon"] - 0.02) < 1e-6) & (abs(mdf["alpha"] - 0.90) < 1e-6)]
        mnap = mver[~mver["table"].str.contains("baseline", case=False, na=False)]
        if len(mnap) > 0:
            ny = (mnap["result"] == "Y").sum()
            best_pct = f"{ny/len(mnap)*100:.1f}%"
        else:
            best_pct = "–"

        lines.append(
            f"| [N{ni},{nj}](N{ni}_{nj}.md) | {n_props} | "
            f"{exp_counts.get('A_full_rule', 0)} | "
            f"{exp_counts.get('B_per_layer', 0)} | "
            f"{exp_counts.get('C_impl_ablation', 0)} | "
            f"{best_pct} |"
        )
    lines.append("")

    return "\n".join(lines)


def generate_readme(data, model_keys):
    """Generate the README for the per-property reports directory."""
    lines = []
    lines.append("# ACAS Xu Per-Property Verification Reports")
    lines.append("")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append("## What's different from `model_reports/`")
    lines.append("")
    lines.append("| Aspect | Old (`model_reports/`) | New (this directory) |")
    lines.append("|--------|----------------------|---------------------|")
    lines.append("| Reference point | Random training sample | **Property midpoint** |")
    lines.append("| Rule mining | Per-model (shared across properties) | **Per-property** |")
    lines.append("| Rule cap | max_rules=3000, max_unary=3000 | **No limit** (all rules used) |")
    lines.append("| Granularity | 1 sample per model | **1 sample per (model, property) pair** |")
    lines.append("| Total pairs | 45 models | **186 (model, property) pairs** |")
    lines.append("")
    lines.append("## Experiment Types")
    lines.append("")
    lines.append("| Label | Description |")
    lines.append("|-------|-------------|")
    lines.append("| Full-Rule | All rule types from all layers combined |")
    lines.append("| Per-Layer | Single layer pair at a time (L0L1 through L4L5) |")
    lines.append("| Impl Ablation | Each implication direction tested separately |")
    lines.append("")
    lines.append("## Reports")
    lines.append("")
    lines.append("- **[All_Models_Aggregated.md](All_Models_Aggregated.md)** — Overall statistics and comparison")
    lines.append("")
    lines.append("### Per-Model Reports")
    lines.append("")
    lines.append("| Model | Link |")
    lines.append("|-------|------|")
    for ni, nj in sorted(model_keys):
        lines.append(f"| N{ni},{nj} | [N{ni}_{nj}.md](N{ni}_{nj}.md) |")
    lines.append("")
    return "\n".join(lines)


def main():
    print("Loading data...")
    data = load_all_data()
    if data.empty:
        return

    print(f"Loaded {len(data)} rows, {data['model'].nunique()} models, "
          f"{data.groupby(['model', 'prop']).ngroups} (model, prop) pairs")

    os.makedirs(OUT_DIR, exist_ok=True)

    # Determine model keys
    model_keys = set()
    for _, row in data[["net_i", "net_j"]].drop_duplicates().iterrows():
        model_keys.add((int(row["net_i"]), int(row["net_j"])))
    model_keys = sorted(model_keys)

    # Generate per-model reports
    print(f"Generating {len(model_keys)} model reports...")
    for ni, nj in model_keys:
        model_data = data[(data["net_i"] == ni) & (data["net_j"] == nj)]
        report = generate_model_report((ni, nj), model_data, data)
        fname = os.path.join(OUT_DIR, f"N{ni}_{nj}.md")
        with open(fname, "w") as f:
            f.write(report)

    # Generate aggregated report
    print("Generating aggregated report...")
    agg_report = generate_aggregated_report(data)
    with open(os.path.join(OUT_DIR, "All_Models_Aggregated.md"), "w") as f:
        f.write(agg_report)

    # Generate README
    print("Generating README...")
    readme = generate_readme(data, model_keys)
    with open(os.path.join(OUT_DIR, "README.md"), "w") as f:
        f.write(readme)

    print(f"Done! Reports written to {OUT_DIR}")
    print(f"  - {len(model_keys)} model reports")
    print(f"  - All_Models_Aggregated.md")
    print(f"  - README.md")


if __name__ == "__main__":
    main()

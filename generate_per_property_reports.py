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
VALID_RESULTS = {"Y", "N", "T/o"}


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


def valid_rows(df):
    """Keep only rows that correspond to actual verification queries."""
    return df[df["result"].isin(VALID_RESULTS)].copy()


def dedupe_baseline_queries(df, keep_alpha=False):
    """
    Collapse repeated baseline executions to one canonical run per unique query.

    Baseline rows are duplicated across alpha directories and, for per-layer /
    impl-ablation experiments, across multiple experiment folders. For summary
    statistics we keep one representative run per query and ignore the
    redundant reruns.
    """
    if df.empty:
        return df.copy()

    key_cols = [c for c in ["model", "prop", "epsilon", "true_class", "target_label"] if c in df.columns]
    if keep_alpha and "alpha" in df.columns:
        key_cols.append("alpha")

    sort_cols = [c for c in ["model", "prop", "epsilon", "true_class", "target_label", "exp_type", "alpha", "layer_pair", "time_s"] if c in df.columns]
    return df.sort_values(sort_cols).drop_duplicates(subset=key_cols, keep="first").copy()


def dedupe_layer_queries(df):
    """
    Collapse repeated per-layer runs of the same query.

    Per-layer experiments rerun unary/baseline tables once per layer-pair
    directory, so the raw CSV union contains 5 copies of the same query row.
    The dedupe key intentionally ignores layer_pair so counts reflect unique
    verification queries rather than repeated executions.
    """
    if df.empty:
        return df.copy()

    key_cols = [
        c for c in [
            "model",
            "prop",
            "alpha",
            "epsilon",
            "true_class",
            "target_label",
            "table",
            "center_source",
        ]
        if c in df.columns
    ]
    sort_cols = [c for c in ["table", "prop", "epsilon", "true_class", "target_label", "layer_pair", "time_s"] if c in df.columns]
    return df.sort_values(sort_cols).drop_duplicates(subset=key_cols, keep="first").copy()


def layer_shared_tables(df):
    """Return tables that appear in more than one layer-pair directory."""
    if df.empty or "layer_pair" not in df.columns:
        return []
    counts = df.groupby("table")["layer_pair"].nunique()
    return sorted(counts[counts > 1].index.tolist())


def build_query_blueprint(model_data):
    """
    Build one unique row per verification query for denominator accounting.

    Query identity ignores alpha/layer/experiment repetition and keeps only:
    (property, epsilon, true_class, target_label != true_class).
    """
    preferred = model_data[model_data["exp_type"] == "A_full_rule"].copy()
    if preferred.empty:
        preferred = model_data.copy()

    query_cols = [c for c in ["model", "prop", "epsilon", "true_class", "target_label", "center_source"] if c in preferred.columns]
    sort_cols = [c for c in ["prop", "epsilon", "true_class", "target_label"] if c in preferred.columns]
    deduped = preferred.sort_values(sort_cols).drop_duplicates(subset=query_cols, keep="first").copy()
    return valid_rows(deduped)


def format_query_count_map(counts_by_eps):
    """Render per-epsilon counts compactly."""
    if not counts_by_eps:
        return "0"
    values = list(counts_by_eps.values())
    if len(set(values)) == 1:
        return str(values[0])
    return ", ".join(f"ε={eps:.2f}: {counts_by_eps[eps]}" for eps in sorted(counts_by_eps))


def render_query_accounting(lines, query_blueprint):
    """Append a concise explanation of where denominators come from."""
    lines.append("## How To Read Counts")
    lines.append("")
    lines.append("- Each `Y/N/T/o` row is one verification query: `(property, ε, true_class, target_label != true_class, rule)`.")
    lines.append("- Self-target rows (`target_label == true_class`) are stored as `-` in the CSVs and are excluded from every denominator.")
    lines.append("- Denominators in the summary tables count valid queries, not properties, models, or experiment directories.")
    lines.append("- For the end-to-end pipeline and a worked example of counts such as `8/40`, see [`COUNTS_AND_PIPELINE.md`](COUNTS_AND_PIPELINE.md).")
    lines.append("")

    if query_blueprint.empty:
        return

    lines.append("**Per-model query accounting (the source of denominators such as `8/40`)**")
    lines.append("")
    lines.append("| Property | True class(es) | Valid queries per ε | Formula |")
    lines.append("|----------|----------------|---------------------|---------|")

    total_per_eps = defaultdict(int)
    formula_parts = []
    for prop_id in sorted(query_blueprint["prop"].dropna().unique()):
        prop_df = query_blueprint[query_blueprint["prop"] == prop_id]
        true_classes = sorted(int(c) for c in prop_df["true_class"].dropna().unique())
        counts_by_eps = {
            float(eps): int(len(prop_df[abs(prop_df["epsilon"] - eps) < 1e-6]))
            for eps in sorted(prop_df["epsilon"].dropna().unique())
        }
        for eps, count in counts_by_eps.items():
            total_per_eps[eps] += count

        ref_eps = sorted(counts_by_eps)[0]
        ref_df = prop_df[abs(prop_df["epsilon"] - ref_eps) < 1e-6]
        targets_per_class = sorted(int(ref_df[ref_df["true_class"] == tc]["target_label"].nunique()) for tc in true_classes)
        if len(set(targets_per_class)) == 1:
            formula = f"{len(true_classes)} true classes × {targets_per_class[0]} non-self targets"
        else:
            formula = " + ".join(str(v) for v in targets_per_class)
        lines.append(
            f"| prop{int(prop_id)} | {', '.join(str(tc) for tc in true_classes)} | "
            f"{format_query_count_map(counts_by_eps)} | {formula} |"
        )
        formula_parts.append(str(counts_by_eps[ref_eps]))

    total_desc = format_query_count_map(dict(sorted(total_per_eps.items())))
    if formula_parts:
        lines.append(f"| **Total** | – | **{total_desc}** | **{' + '.join(formula_parts)}** |")
    lines.append("")


def prop_query_summary(query_blueprint, prop_id):
    """Return a one-line denominator explanation for a specific property."""
    prop_df = query_blueprint[query_blueprint["prop"] == prop_id]
    if prop_df.empty:
        return None

    counts_by_eps = {
        float(eps): int(len(prop_df[abs(prop_df["epsilon"] - eps) < 1e-6]))
        for eps in sorted(prop_df["epsilon"].dropna().unique())
    }
    true_classes = sorted(int(c) for c in prop_df["true_class"].dropna().unique())
    ref_eps = sorted(counts_by_eps)[0]
    ref_df = prop_df[abs(prop_df["epsilon"] - ref_eps) < 1e-6]
    targets_per_class = sorted(int(ref_df[ref_df["true_class"] == tc]["target_label"].nunique()) for tc in true_classes)

    if len(set(targets_per_class)) == 1:
        formula = f"{len(true_classes)} true classes × {targets_per_class[0]} non-self targets"
    else:
        formula = " + ".join(str(v) for v in targets_per_class)

    return f"Valid queries per ε: {format_query_count_map(counts_by_eps)} ({formula})"


def append_table_details(lines, section_df, tables_in_section, layer_pair=None):
    """Append rule tables grouped by true class."""
    for tbl_name in tables_in_section:
        tdf = section_df[section_df["table"] == tbl_name]
        for tc in sorted(tdf["true_class"].dropna().unique()):
            tc = int(tc)
            cdf = tdf[tdf["true_class"] == tc]
            ver_cdf = valid_rows(cdf)
            ny = (ver_cdf["result"] == "Y").sum()
            nt = len(ver_cdf)
            pct = f"{ny/nt*100:.1f}%" if nt > 0 else "–"

            if layer_pair is not None:
                lines.append(f"##### {tbl_name} ({layer_pair}, class {tc}) — Y={ny}/{nt} ({pct})")
            else:
                lines.append(f"##### {tbl_name} (class {tc}) — Y={ny}/{nt} ({pct})")
            lines.append("")
            lines.append(build_detail_table(cdf, tc))
            lines.append("")


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
    query_blueprint = build_query_blueprint(model_data)

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
    render_query_accounting(lines, query_blueprint)

    # ── Aggregated summary ────────────────────────────────────────────────
    ver = valid_rows(model_data)

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
        if exp_key == "B_per_layer":
            lines.append("_Per-layer unary/baseline rows are deduplicated across the 5 layer-pair directories, so denominators reflect unique queries rather than repeated reruns._")
            lines.append("")

        for alpha in ALPHAS:
            adf = exp_df[abs(exp_df["alpha"] - alpha) < 1e-6]
            if len(adf) == 0:
                continue
            summary_df = dedupe_layer_queries(adf) if exp_key == "B_per_layer" else adf

            lines.append(f"#### α = {alpha}")
            lines.append("")
            lines.append("| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |")
            lines.append("|------|--------|--------|--------|--------|----------|")

            for tbl in sorted(summary_df["table"].unique()):
                tdf = summary_df[summary_df["table"] == tbl]
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
        prop_ver = valid_rows(prop_data)
        true_classes = sorted(prop_data[prop_data["result"] != "-"]["true_class"].dropna().unique())

        lines.append(f"### Property {prop_id}")
        lines.append("")
        if "center_source" in prop_data.columns:
            cs = prop_data["center_source"].dropna().unique()
        if len(cs) > 0:
            lines.append(f"Reference point: `{cs[0]}`  ")
        if true_classes:
            lines.append(f"True class(es): {', '.join(str(int(c)) for c in true_classes)}")
        summary = prop_query_summary(query_blueprint, prop_id)
        if summary:
            lines.append(f"{summary}  ")
        lines.append("")

        # Full-rule experiments for this property
        for exp_label, exp_key in [("Full-Rule", "A_full_rule"), ("Per-Layer", "B_per_layer"), ("Impl Ablation", "C_impl_ablation")]:
            exp_df = prop_data[prop_data["exp_type"] == exp_key]
            if len(exp_df) == 0:
                continue

            lines.append(f"#### {exp_label}")
            lines.append("")
            if exp_key == "B_per_layer":
                lines.append("_Shared unary/baseline tables are shown once below using deduplicated query rows. Layer-specific implication tables remain grouped by layer pair._")
                lines.append("")

            for alpha in ALPHAS:
                adf = exp_df[abs(exp_df["alpha"] - alpha) < 1e-6]
                if len(adf) == 0:
                    continue

                lines.append(f"##### α={alpha}")
                lines.append("")

                if exp_key == "B_per_layer":
                    shared_tables = layer_shared_tables(adf)
                    if shared_tables:
                        lines.append("**Shared across layer-pair runs (deduplicated)**")
                        lines.append("")
                        shared_df = dedupe_layer_queries(adf[adf["table"].isin(shared_tables)])
                        append_table_details(lines, shared_df, shared_tables)

                    for lp in sorted(adf["layer_pair"].unique()):
                        lpdf = adf[adf["layer_pair"] == lp]
                        tables_in_section = [tbl for tbl in sorted(lpdf["table"].unique()) if tbl not in shared_tables]
                        if not tables_in_section:
                            continue
                        lines.append(f"**Layer pair {lp}**")
                        lines.append("")
                        append_table_details(lines, lpdf, tables_in_section, layer_pair=lp)
                else:
                    append_table_details(lines, adf, sorted(adf["table"].unique()))

    return "\n".join(lines)


def generate_aggregated_report(data):
    """Generate the All_Models_Aggregated.md report."""
    ver = data[data["result"].isin(["Y", "N", "T/o"])]
    bl = ver[ver["table"].str.contains("baseline", case=False, na=False)]
    nap = ver[~ver["table"].str.contains("baseline", case=False, na=False)]
    bl_unique = dedupe_baseline_queries(bl)

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

    lines.append("## How To Read Counts")
    lines.append("")
    lines.append("- The baseline table below is deduplicated to one canonical run per unique query `(model, property, ε, true_class, target_label)`.")
    lines.append("- `Any verified` counts unique `(model, property)` pairs at a fixed `α` and `ε`.")
    lines.append("- `Rule Type Breakdown` and `Best row-level Y%` remain row-level statistics across all valid queries for that rule family.")
    lines.append("")

    # ── Baseline ──────────────────────────────────────────────────────────
    lines.append("## Baseline (deduplicated unique queries)")
    lines.append("")
    lines.append("| ε | Y | N | T/o | Total | Verified % |")
    lines.append("|---|---|---|-----|-------|-----------|")
    for eps in EPSILONS:
        edf = bl_unique[abs(bl_unique["epsilon"] - eps) < 1e-6]
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
    all_pairs = set(tuple(x) for x in nap_a[["model", "prop"]].drop_duplicates().to_records(index=False))
    missing_by_alpha = {}
    for alpha in ALPHAS:
        adf = nap_a[abs(nap_a["alpha"] - alpha) < 1e-6]
        present_pairs = set(tuple(x) for x in adf[["model", "prop"]].drop_duplicates().to_records(index=False))
        missing_pairs = sorted(all_pairs - present_pairs)
        if missing_pairs:
            labels = [f"N{model.split('_')[0]},{model.split('_')[1]} prop{int(prop)}" for model, prop in missing_pairs]
            missing_by_alpha[alpha] = labels
    if missing_by_alpha:
        lines.append("")
        lines.append("Missing full-rule coverage by α:")
        for alpha, labels in missing_by_alpha.items():
            lines.append(f"- α={alpha:.2f}: {', '.join(labels)}")
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
        lines.append(f"| {alpha:.2f} | {' | '.join(cells)} |")
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
    bl_times = dedupe_baseline_queries(exp_a_full[exp_a_full["table"].str.contains("baseline", case=False, na=False)])[ 
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
            lines.append(f"- **Both verify Y:** {len(both)} unique queries")
            lines.append(f"- **Mean speedup:** {both['speedup'].mean():.1f}x (median {both['speedup'].median():.1f}x)")
            lines.append(f"- **Mean baseline time:** {both['bl_time'].mean():.2f}s")
            lines.append(f"- **Mean NAP time:** {both['nap_time'].mean():.2f}s")

        bl_fail = bl_times[bl_times["bl_result"].isin(["N", "T/o"])]
        rescued = bl_fail.merge(nap_best, on=["model", "prop", "epsilon", "target_label"], how="inner")
        lines.append(f"- **Baseline fails, NAP verifies:** {len(rescued)} unique queries")
        if len(rescued) > 0:
            lines.append(f"  - From timeout: {(rescued['bl_result'] == 'T/o').sum()}")
            lines.append(f"  - From falsified: {(rescued['bl_result'] == 'N').sum()}")
    lines.append("")

    # ── Per-model summary table ───────────────────────────────────────────
    lines.append("## Per-Model Summary")
    lines.append("")
    lines.append("| Model | Props | Full-Rule Groups | Per-Layer Groups | Impl-Ablation Groups | Best Row-Level Y% (ε=0.02, α=0.90) |")
    lines.append("|-------|-------|------------------|------------------|-----------------------|------------------------------------|")

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
    lines.append("| Granularity | 1 sample per model | **1 reference point per (model, property) pair, expanded into query rows over true_class/target_label pairs** |")
    lines.append("| Total pairs | 45 models | **186 (model, property) pairs** |")
    lines.append("")
    lines.append("## How to read `Y/total`")
    lines.append("")
    lines.append("- `Y/total` always means `verified queries / valid queries`.")
    lines.append("- A valid query is one `(property, ε, true_class, target_label != true_class, rule)` combination.")
    lines.append("- Rows with `target_label == true_class` are stored as `-` in the CSVs and are excluded from denominators.")
    lines.append("- In per-layer reports, shared unary/baseline rows are deduplicated across layer-pair directories so counts reflect unique queries rather than 5 reruns of the same query.")
    lines.append("- For the full pipeline and a worked example of counts such as `8/40`, see **[COUNTS_AND_PIPELINE.md](COUNTS_AND_PIPELINE.md)**.")
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

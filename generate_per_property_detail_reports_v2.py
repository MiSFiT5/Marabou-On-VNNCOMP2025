#!/usr/bin/env python3
"""
Generate per-property detail reports (v2).

Report rule:
  - Filter to the single property midpoint and the midpoint prediction class.
  - Deduplicate repeated logical experiments across A/B/C.
  - If the same logical experiment appears multiple times, keep the later run
    according to the batch execution order:
        A(full_rule) < B(L0→L1) < ... < B(L4→L5) < C(impl_ablation)
"""
import glob
import json
import os
import re
from datetime import datetime

import numpy as np
import pandas as pd

try:
    import onnxruntime as ort
except ImportError as exc:
    raise ImportError("pip install onnxruntime") from exc


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
NAP_DIR = os.path.join(REPO_ROOT, "nap_verify")
SHARED_DATA = os.path.join(NAP_DIR, "shared_data", "acasxu")
EXP_ROOT = os.path.join(NAP_DIR, "experiments")
ONNX_DIR = os.path.join(
    REPO_ROOT,
    "vnncomp2025_benchmarks",
    "benchmarks",
    "acasxu_2023",
    "onnx",
)
OUT_ROOT = os.path.join(
    SCRIPT_DIR, "model_reports_per_property", "per_property_details_v2"
)

EXP_RE = re.compile(
    r"acasxu_ACASXU_run2a_(\d+)_(\d+)_batch_2000_prop(\d+)"
    r"(?:_(impl_ablation))?_?alpha([\d.]+)"
    r"(?:_layer_(L\d+L\d+))?"
)
LAYER_PAIR_RE = re.compile(r"L(\d+)L(\d+)")
TABLE_LAYER_RE = re.compile(r"Impl (L\d+→L\d+)")
DIRECTION_RE = re.compile(r"\[([^\]]+)\]")

EPSILONS = [0.02, 0.05, 0.10, 0.20]
VALID_RESULTS = {"Y", "N", "T/o"}
CLASS_NAMES = {
    0: "Clear-of-Conflict",
    1: "Weak Left",
    2: "Weak Right",
    3: "Strong Left",
    4: "Strong Right",
}
LAYER_ORDER = {
    "L0L1": 0,
    "L1L2": 1,
    "L2L3": 2,
    "L3L4": 3,
    "L4L5": 4,
}


def get_onnx_path(ni, nj):
    name = f"ACASXU_run2a_{ni}_{nj}_batch_2000.onnx"
    path = os.path.join(ONNX_DIR, name)
    if os.path.exists(path):
        return path
    raise FileNotFoundError(f"Cannot find {name}")


def make_session(onnx_path):
    return ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])


def predict_with_outputs(session, input_vec):
    inp = session.get_inputs()[0]
    x = np.array(input_vec, dtype=np.float32).reshape(inp.shape)
    out = session.run(None, {inp.name: x})[0].flatten()
    return int(np.argmin(out)), out


def load_all_data():
    rows = []
    pattern = os.path.join(
        EXP_ROOT, "acasxu_*_prop*", "verification_results", "table3_results.csv"
    )
    for csv_path in sorted(glob.glob(pattern)):
        dirname = os.path.basename(os.path.dirname(os.path.dirname(csv_path)))
        match = EXP_RE.match(dirname)
        if not match:
            continue

        net_i, net_j, prop_id, impl_abl, alpha, layer = match.groups()
        if impl_abl:
            exp_type = "impl_ablation"
        elif layer:
            exp_type = "per_layer"
        else:
            exp_type = "full_rule"

        try:
            df = pd.read_csv(csv_path)
        except Exception:
            continue

        df["net_i"] = int(net_i)
        df["net_j"] = int(net_j)
        df["prop"] = int(prop_id)
        df["alpha"] = float(alpha)
        df["exp_type"] = exp_type
        df["layer_pair"] = layer if layer else "all"
        rows.append(df)

    if not rows:
        return pd.DataFrame()
    return pd.concat(rows, ignore_index=True)


def format_eps(epsilon):
    if epsilon is None or pd.isna(epsilon):
        return "–"
    return f"{float(epsilon):.2f}"


def format_alpha(alpha):
    if alpha is None or pd.isna(alpha):
        return "–"
    return f"{float(alpha):.2f}".rstrip("0").rstrip(".")


def format_layer_pair(layer_pair):
    match = LAYER_PAIR_RE.fullmatch(str(layer_pair))
    if not match:
        return str(layer_pair)
    left, right = match.groups()
    return f"L{left}→L{right}"


def format_seconds(seconds):
    if seconds is None or pd.isna(seconds):
        return "–"
    return f"{int(round(float(seconds)))}s"


def extract_impl_layer(table_str, fallback_layer_pair):
    match = TABLE_LAYER_RE.search(str(table_str))
    if match:
        return match.group(1)
    if fallback_layer_pair and fallback_layer_pair != "all":
        return format_layer_pair(fallback_layer_pair)
    return None


def extract_direction(table_str):
    match = DIRECTION_RE.search(str(table_str))
    if not match:
        return None
    return match.group(1)


def display_label(row):
    label = str(row["table"])
    if "α=" not in label and "alpha" not in label.lower():
        label = f"{label} [α={format_alpha(row.get('alpha_float', row.get('alpha')))}]"
    return label


def classify_table_kind(table_str, impl_layer, direction_label):
    raw = str(table_str)
    lowered = raw.lower()
    if lowered.startswith("none (baseline)"):
        return "baseline"
    if lowered.startswith("always_"):
        return "unary-only"
    if lowered.startswith("impl "):
        prefix = "implication-direction" if direction_label else "implication-only"
        if impl_layer:
            return f"{prefix} ({impl_layer})"
        return prefix
    return "other"


def kind_rank(kind):
    if kind == "baseline":
        return 0
    if kind == "unary-only":
        return 1
    if kind.startswith("implication-only"):
        return 2
    if kind.startswith("implication-direction"):
        return 3
    return 4


def execution_rank(row):
    if row["exp_type"] == "full_rule":
        return 0
    if row["exp_type"] == "per_layer":
        return 10 + LAYER_ORDER.get(str(row["layer_pair"]), 99)
    if row["exp_type"] == "impl_ablation":
        return 20
    return 999


def source_label(row):
    if row["exp_type"] == "full_rule":
        return "A"
    if row["exp_type"] == "per_layer":
        return f"B/{format_layer_pair(row['layer_pair'])}"
    if row["exp_type"] == "impl_ablation":
        return "C"
    return str(row["exp_type"])


def prepare_reference_df(pdf, pred_class):
    data = pdf.copy()
    data["class_id_int"] = pd.to_numeric(data["class_id"], errors="coerce")
    data["target_label_int"] = pd.to_numeric(data["target_label"], errors="coerce")
    data["epsilon_float"] = pd.to_numeric(data["epsilon"], errors="coerce")
    data["alpha_float"] = pd.to_numeric(data["alpha"], errors="coerce")
    data["time_s_float"] = pd.to_numeric(data["time_s"], errors="coerce")
    data["table_str"] = data["table"].astype(str)

    mask = (data["class_id_int"] == pred_class) & data["result"].isin(VALID_RESULTS)
    if "center_source" in data.columns:
        mask &= data["center_source"].astype(str) == "property_midpoint[0]"
    if "sample_idx" in data.columns:
        mask &= pd.to_numeric(data["sample_idx"], errors="coerce").fillna(0) == 0

    data = data.loc[mask].copy()
    if data.empty:
        return data

    data["impl_layer"] = data.apply(
        lambda row: extract_impl_layer(row["table_str"], row.get("layer_pair", "all")),
        axis=1,
    )
    data["direction_label"] = data["table_str"].map(extract_direction)
    data["display_label"] = data.apply(display_label, axis=1)
    data["table_kind"] = data.apply(
        lambda row: classify_table_kind(
            row["table_str"], row["impl_layer"], row["direction_label"]
        ),
        axis=1,
    )
    data["kind_rank"] = data["table_kind"].map(kind_rank)
    data["exec_rank"] = data.apply(execution_rank, axis=1)
    data["source_label"] = data.apply(source_label, axis=1)
    return data


def dedupe_logical_rows(df):
    if df.empty:
        return df
    ordered = df.sort_values(
        by=[
            "target_label_int",
            "display_label",
            "epsilon_float",
            "exec_rank",
            "time_s_float",
        ],
        kind="stable",
    )
    return ordered.drop_duplicates(
        subset=["target_label_int", "display_label", "epsilon_float"],
        keep="last",
    )


def sorted_unique_rows(df):
    if df.empty:
        return df
    ordered = df.sort_values(
        by=["kind_rank", "display_label", "epsilon_float", "exec_rank", "time_s_float"],
        kind="stable",
    )
    return ordered


def format_result_cell(row):
    result = str(row["result"])
    if result == "T/o":
        return "T/o"
    return f"{result} ({format_seconds(row['time_s_float'])})"


def best_rows_for_target(target_df):
    verified = target_df[target_df["result"] == "Y"].copy()
    if verified.empty:
        return None, verified
    best_eps = verified["epsilon_float"].max()
    winners = verified[np.isclose(verified["epsilon_float"], best_eps)].copy()
    winners = sorted_unique_rows(winners).drop_duplicates(subset=["display_label"], keep="first")
    return best_eps, winners


def overall_eps(targets, analyses):
    valid = []
    for eps in EPSILONS:
        ok = True
        for target in targets:
            best_eps = analyses[target]["best_eps"]
            if best_eps is None or float(best_eps) + 1e-9 < eps:
                ok = False
                break
        if ok:
            valid.append(eps)
    return max(valid) if valid else None


def build_target_table(lines, target_df):
    if target_df.empty:
        lines.append("*No experiments remain after filtering and deduplication for this target.*")
        lines.append("")
        return

    rows = sorted_unique_rows(target_df).drop_duplicates(subset=["display_label"], keep="first")
    lines.append("| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
    lines.append("|------------|------|--------|--------|--------|--------|")

    for _, base_row in rows.iterrows():
        row_df = target_df[target_df["display_label"] == base_row["display_label"]].copy()
        cells = []
        for eps in EPSILONS:
            eps_df = row_df[np.isclose(row_df["epsilon_float"], eps)].copy()
            if eps_df.empty:
                cells.append("–")
                continue
            eps_df = eps_df.sort_values(by=["exec_rank", "time_s_float"], kind="stable")
            cells.append(format_result_cell(eps_df.iloc[-1]))
        lines.append(
            f"| `{base_row['display_label']}` | {base_row['table_kind']} | "
            f"{' | '.join(cells)} |"
        )
    lines.append("")


def generate_property_report(ni, nj, prop, pdf, ref_point, pred_class, outputs):
    lines = []
    targets = [target for target in range(5) if target != pred_class]
    ref_df = prepare_reference_df(pdf, pred_class)
    dedup_df = dedupe_logical_rows(ref_df)

    analyses = {}
    for target in targets:
        target_df = dedup_df[dedup_df["target_label_int"] == target].copy()
        best_eps, winners = best_rows_for_target(target_df)
        analyses[target] = {
            "target_df": target_df,
            "best_eps": best_eps,
            "winners": winners,
        }

    full_eps = overall_eps(targets, analyses)

    lines.append(f"# N{ni},{nj} — Property {prop}")
    lines.append("")
    lines.append("> Single reference point verification report (v2)")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Reference Point")
    lines.append("")
    lines.append(f"- **Model:** `ACASXU_run2a_{ni}_{nj}_batch_2000.onnx`")
    lines.append(f"- **Property:** prop{prop}")
    lines.append(
        f"- **Reference point (property midpoint):** `{[round(float(v), 6) for v in ref_point]}`"
    )
    lines.append(
        f"- **Network prediction:** class **{pred_class}** ({CLASS_NAMES[pred_class]})"
    )
    lines.append(
        f"- **Network outputs at midpoint:** `{[round(float(v), 4) for v in outputs]}`"
    )
    lines.append("- **Query filter used in this report:** `class_id = midpoint prediction`, `center_source = property_midpoint[0]`, `sample_idx = 0`")
    lines.append("")

    lines.append("## Dedup Rule")
    lines.append("")
    lines.append("- Repeated logical experiments are merged after the midpoint filter.")
    lines.append("- Duplicate key: same `target`, same `ε`, same experiment label, same `α`.")
    lines.append("- Keep order: `A (full_rule)` < `B/L0→L1` < `B/L1→L2` < `B/L2→L3` < `B/L3→L4` < `B/L4→L5` < `C (impl_ablation)`.")
    lines.append("- The report shows only the kept rows after this overwrite rule.")
    lines.append("")

    lines.append("## Target Summary")
    lines.append("")
    lines.append("| Target | Class Name | Max Verified ε | Winning kept experiments |")
    lines.append("|--------|------------|----------------|--------------------------|")

    for target in targets:
        analysis = analyses[target]
        if analysis["winners"].empty:
            winners_text = "–"
        else:
            winners_text = ", ".join(
                f"`{row.display_label}` [{row.source_label}]"
                for row in analysis["winners"].itertuples()
            )
        lines.append(
            f"| {target} | {CLASS_NAMES[target]} | {format_eps(analysis['best_eps'])} | {winners_text} |"
        )

    lines.append("")
    if full_eps is None:
        lines.append(
            "**Overall:** after deduplication, this reference point is not fully verified at any tested ε."
        )
    else:
        lines.append(
            f"**Overall:** after deduplication, this reference point is fully verified up to **ε = {format_eps(full_eps)}**."
        )
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Detailed Results Per Target")
    lines.append("")

    for target in targets:
        analysis = analyses[target]
        lines.append(f"### Target {target} ({CLASS_NAMES[target]})")
        lines.append("")
        lines.append(f"- **Max verified ε after deduplication:** `{format_eps(analysis['best_eps'])}`")
        if analysis["winners"].empty:
            lines.append("- **Winning kept experiments:** none")
        else:
            lines.append("- **Winning kept experiments:**")
            for row in analysis["winners"].itertuples():
                lines.append(
                    f"  - `{row.display_label}` ({row.table_kind}) from `{row.source_label}`"
                )
        lines.append("")
        build_target_table(lines, analysis["target_df"])

    return "\n".join(lines)


def main():
    print("=" * 70)
    print("Per-Property Detail Report Generator (v2)")
    print("=" * 70)

    print("\n[1/3] Loading CSV data...")
    data = load_all_data()
    if data.empty:
        print("No data!")
        return
    print(f"  Loaded {len(data)} rows")

    pairs = data.groupby(["net_i", "net_j", "prop"]).size().reset_index()
    print(f"  Found {len(pairs)} (model, property) pairs")

    print("\n[2/3] Computing midpoint predictions and generating reports...")
    os.makedirs(OUT_ROOT, exist_ok=True)
    session_cache = {}
    report_count = 0

    model_groups = data.groupby(["net_i", "net_j"])
    for (ni, nj), mdf in sorted(model_groups, key=lambda item: (item[0][0], item[0][1])):
        model_dir = os.path.join(OUT_ROOT, f"N{ni}_{nj}")
        os.makedirs(model_dir, exist_ok=True)

        key = (ni, nj)
        if key not in session_cache:
            try:
                session_cache[key] = make_session(get_onnx_path(ni, nj))
            except FileNotFoundError as exc:
                print(f"  WARNING: {exc}")
                continue

        for prop in sorted(mdf["prop"].unique()):
            data_dir = os.path.join(
                SHARED_DATA, f"ACASXU_run2a_{ni}_{nj}_batch_2000_prop{prop}_data"
            )
            meta_path = os.path.join(data_dir, "acasxu_meta.json")
            if not os.path.exists(meta_path):
                continue

            with open(meta_path) as handle:
                meta = json.load(handle)

            ref_point = meta.get("reference_point")
            if not ref_point:
                continue

            pred_class, outputs = predict_with_outputs(session_cache[key], ref_point)
            prop_df = mdf[mdf["prop"] == prop].copy()
            report = generate_property_report(
                ni, nj, prop, prop_df, ref_point, pred_class, outputs
            )

            out_path = os.path.join(model_dir, f"prop{prop}.md")
            with open(out_path, "w") as handle:
                handle.write(report)
            report_count += 1

        props = sorted(mdf["prop"].unique())
        idx_lines = [f"# N{ni},{nj} — Property Reports (v2)", ""]
        idx_lines.append(f"Model: `ACASXU_run2a_{ni}_{nj}_batch_2000.onnx`")
        idx_lines.append("")
        idx_lines.append("| Property | Report |")
        idx_lines.append("|----------|--------|")
        for prop in props:
            idx_lines.append(f"| prop{prop} | [prop{prop}.md](prop{prop}.md) |")
        idx_lines.append("")

        with open(os.path.join(model_dir, "README.md"), "w") as handle:
            handle.write("\n".join(idx_lines))

    print(f"  Generated {report_count} property reports")

    print("\n[3/3] Writing top-level index...")
    idx_lines = ["# Per-Property Detail Reports (v2)", ""]
    idx_lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    idx_lines.append("")
    idx_lines.append(
        "Each report keeps only the non-duplicate experiments for one property midpoint. "
        "If the same logical experiment appears multiple times, the later run overwrites the earlier one."
    )
    idx_lines.append("")
    idx_lines.append("| Model | Properties |")
    idx_lines.append("|-------|------------|")

    for (ni, nj), mdf in sorted(model_groups, key=lambda item: (item[0][0], item[0][1])):
        props = sorted(mdf["prop"].unique())
        prop_links = ", ".join(f"[p{prop}](N{ni}_{nj}/prop{prop}.md)" for prop in props)
        idx_lines.append(f"| [N{ni},{nj}](N{ni}_{nj}/) | {prop_links} |")

    idx_lines.append("")
    with open(os.path.join(OUT_ROOT, "README.md"), "w") as handle:
        handle.write("\n".join(idx_lines))

    print(f"\nDone! Reports in: {OUT_ROOT}")


if __name__ == "__main__":
    main()

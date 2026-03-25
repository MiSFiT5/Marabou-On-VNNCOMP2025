#!/usr/bin/env python3
"""
Generate per-property detail reports.

Structure:
  model_reports_per_property/
    per_property_details/
      N1_1/
        prop1.md   — one reference point, 4 targets, all rules/alphas/epsilons
        prop2.md
        ...
      N1_2/
        ...

Each report focuses on ONE reference point and answers:
  "At which epsilon is this reference point verified, and with which rules?"
"""
import os, re, glob, json, math
from collections import defaultdict
from datetime import datetime

import numpy as np
import pandas as pd

try:
    import onnxruntime as ort
except ImportError:
    raise ImportError("pip install onnxruntime")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NAP_DIR = os.path.join(os.path.dirname(os.path.dirname(SCRIPT_DIR)), "nap_verify")
SHARED_DATA = os.path.join(NAP_DIR, "shared_data", "acasxu")
EXP_ROOT = os.path.join(NAP_DIR, "experiments")
ONNX_DIR = os.path.join(
    os.path.dirname(os.path.dirname(SCRIPT_DIR)),
    "vnncomp2025_benchmarks", "benchmarks", "acasxu_2023", "onnx",
)
OUT_ROOT = os.path.join(SCRIPT_DIR, "model_reports_per_property", "per_property_details")

EXP_RE = re.compile(
    r"acasxu_ACASXU_run2a_(\d+)_(\d+)_batch_2000_prop(\d+)"
    r"(?:_(impl_ablation))?_?alpha([\d.]+)"
    r"(?:_layer_(L\d+L\d+))?"
)

EPSILONS = [0.02, 0.05, 0.10, 0.20]
ALPHAS = [0.90, 0.95, 0.99]
VALID_RESULTS = {"Y", "N", "T/o"}
CLASS_NAMES = {0: "Clear-of-Conflict", 1: "Weak Left", 2: "Weak Right", 3: "Strong Left", 4: "Strong Right"}


def get_onnx_path(ni, nj):
    name = f"ACASXU_run2a_{ni}_{nj}_batch_2000.onnx"
    path = os.path.join(ONNX_DIR, name)
    if os.path.exists(path):
        return path
    raise FileNotFoundError(f"Cannot find {name}")


def predict_with_outputs(onnx_path, input_vec):
    sess = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
    inp = sess.get_inputs()[0]
    x = np.array(input_vec, dtype=np.float32).reshape(inp.shape)
    out = sess.run(None, {inp.name: x})[0].flatten()
    return int(np.argmin(out)), out


def load_all_data():
    rows = []
    pattern = os.path.join(EXP_ROOT, "acasxu_*_prop*", "verification_results", "table3_results.csv")
    for f in sorted(glob.glob(pattern)):
        dirname = os.path.basename(os.path.dirname(os.path.dirname(f)))
        m = EXP_RE.match(dirname)
        if not m:
            continue
        net_i, net_j, prop_id, impl_abl, alpha, layer = m.groups()
        if impl_abl:
            exp_type = "impl_ablation"
        elif layer:
            exp_type = "per_layer"
        else:
            exp_type = "full_rule"
        try:
            df = pd.read_csv(f)
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


def result_symbol(r):
    if r == "Y":
        return "🟢 Y"
    elif r == "N":
        return "🔴 N"
    elif r == "T/o":
        return "🟡 T/o"
    return "–"


def generate_property_report(ni, nj, prop, pdf, ref_point, pred_class, outputs):
    """Generate one property report."""
    lines = []
    targets = [t for t in range(5) if t != pred_class]

    lines.append(f"# N{ni},{nj} — Property {prop}")
    lines.append("")
    lines.append(f"> Single reference point verification report  ")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    # ── Reference point info ──
    lines.append("## Reference Point")
    lines.append("")
    lines.append(f"- **Model:** `ACASXU_run2a_{ni}_{nj}_batch_2000.onnx`")
    lines.append(f"- **Property:** prop{prop}")
    lines.append(f"- **Reference point (property midpoint):** `{[round(float(v), 6) for v in ref_point]}`")
    lines.append(f"- **Network prediction:** class **{pred_class}** ({CLASS_NAMES[pred_class]})")
    lines.append(f"- **Network outputs at midpoint:** `{[round(float(v), 4) for v in outputs]}`")
    lines.append(f"  - Predicted class has the **lowest** output (ACAS Xu uses argmin)")
    lines.append("")

    # ── Quick robustness summary ──
    lines.append("## Robustness Summary")
    lines.append("")
    lines.append("For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?")
    lines.append("")

    # Filter to only matched queries, full_rule experiment
    fdf = pdf[(pdf["class_id"].astype(int) == pred_class) &
              (pdf["result"].isin(VALID_RESULTS)) &
              (pdf["exp_type"] == "full_rule")]

    # Build summary: for each (target, alpha, rule), find max verified epsilon
    lines.append("### Best result per target (across all rules and α)")
    lines.append("")
    lines.append("| Target | Class Name | Best Rule | α | Max Verified ε | Status |")
    lines.append("|--------|------------|-----------|---|----------------|--------|")

    for tgt in targets:
        tdf = fdf[fdf["target_label"].astype(int) == tgt]
        best_eps = -1
        best_rule = "–"
        best_alpha = "–"

        for _, row in tdf.iterrows():
            if row["result"] == "Y":
                eps = float(row["epsilon"])
                if eps > best_eps:
                    best_eps = eps
                    best_rule = row["table"]
                    best_alpha = row["alpha"]

        if best_eps > 0:
            status = f"✅ Verified up to ε={best_eps}"
        else:
            status = "❌ Not verified at any ε"

        lines.append(
            f"| {tgt} | {CLASS_NAMES[tgt]} | `{best_rule}` | {best_alpha} | "
            f"{best_eps if best_eps > 0 else '–'} | {status} |"
        )

    # Overall robustness
    # Find max ε where ALL targets are verified (by some rule)
    full_robust_eps = []
    for eps in EPSILONS:
        all_verified = True
        for tgt in targets:
            tdf = fdf[(fdf["target_label"].astype(int) == tgt) &
                      (abs(fdf["epsilon"] - eps) < 1e-6) &
                      (fdf["result"] == "Y")]
            if len(tdf) == 0:
                all_verified = False
                break
        if all_verified:
            full_robust_eps.append(eps)

    lines.append("")
    if full_robust_eps:
        lines.append(f"**Overall:** This reference point is **fully robust** (all 4 targets verified) "
                     f"up to **ε = {max(full_robust_eps)}** (with appropriate NAP rules).")
    else:
        lines.append(f"**Overall:** This reference point is **NOT fully robust** at any tested ε "
                     f"(at least one target cannot be verified).")
    lines.append("")

    # ── Detailed per-target tables ──
    lines.append("---")
    lines.append("")
    lines.append("## Detailed Results Per Target")
    lines.append("")

    for tgt in targets:
        lines.append(f"### Target {tgt} ({CLASS_NAMES[tgt]})")
        lines.append("")
        lines.append(f"*Can the network be fooled from class {pred_class} ({CLASS_NAMES[pred_class]}) "
                     f"to class {tgt} ({CLASS_NAMES[tgt]}) within an ε-ball?*")
        lines.append("")

        tdf = fdf[fdf["target_label"].astype(int) == tgt]

        if tdf.empty:
            lines.append("*No data available.*")
            lines.append("")
            continue

        # Table: rows = rules, columns = (alpha, epsilon)
        rules = []
        for tname in tdf["table"].unique():
            rules.append(tname)
        rules = sorted(rules, key=lambda r: (0 if "baseline" in r.lower() else 1, r))

        lines.append("| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |")
        lines.append("|------|--------|--------|--------|--------|")

        for rule in rules:
            rdf = tdf[tdf["table"] == rule]
            cells = []
            for eps in EPSILONS:
                edf = rdf[abs(rdf["epsilon"] - eps) < 1e-6]
                if len(edf) == 0:
                    cells.append("–")
                else:
                    r = edf.iloc[0]
                    t = int(round(r["time_s"]))
                    cells.append(f"{result_symbol(r['result'])} ({t}s)")
            cells_str = " | ".join(cells)
            lines.append(f"| `{rule}` | {cells_str} |")

        lines.append("")

    # ── Per-Layer and Impl-Ablation summary (compact) ──
    per_layer_df = pdf[(pdf["class_id"].astype(int) == pred_class) &
                       (pdf["result"].isin(VALID_RESULTS)) &
                       (pdf["exp_type"] == "per_layer")]

    if not per_layer_df.empty:
        lines.append("---")
        lines.append("")
        lines.append("## Per-Layer Results (ε=0.02 only, α=0.90)")
        lines.append("")
        lines.append("Which layer pair contributes most to verification?")
        lines.append("")

        pldf = per_layer_df[(abs(per_layer_df["alpha"] - 0.90) < 1e-6) &
                            (abs(per_layer_df["epsilon"] - 0.02) < 1e-6)]

        if not pldf.empty:
            # Get impl rules only (skip baseline/unary which are duplicated)
            impl_rules = pldf[pldf["table"].str.contains("Impl|Layer", case=False)]
            if not impl_rules.empty:
                lines.append("| Layer Pair Rule | Targets Verified (of 4) |")
                lines.append("|-----------------|------------------------|")
                for tname in sorted(impl_rules["table"].unique()):
                    trdf = impl_rules[impl_rules["table"] == tname]
                    ny = (trdf["result"] == "Y").sum()
                    lines.append(f"| `{tname}` | {ny}/4 |")
                lines.append("")

    return "\n".join(lines)


def main():
    print("=" * 70)
    print("Per-Property Detail Report Generator")
    print("=" * 70)

    # Load all CSV data
    print("\n[1/3] Loading CSV data...")
    data = load_all_data()
    if data.empty:
        print("No data!")
        return
    print(f"  Loaded {len(data)} rows")

    # Find all (model, property) pairs
    pairs = data.groupby(["net_i", "net_j", "prop"]).size().reset_index()
    print(f"  Found {len(pairs)} (model, property) pairs")

    # Generate reports
    print("\n[2/3] Computing midpoint predictions and generating reports...")
    model_cache = {}
    report_count = 0

    model_groups = data.groupby(["net_i", "net_j"])

    for (ni, nj), mdf in sorted(model_groups, key=lambda x: (x[0][0], x[0][1])):
        model_dir = os.path.join(OUT_ROOT, f"N{ni}_{nj}")
        os.makedirs(model_dir, exist_ok=True)

        # Load ONNX model once per model
        key = (ni, nj)
        if key not in model_cache:
            try:
                model_cache[key] = get_onnx_path(ni, nj)
            except FileNotFoundError as e:
                print(f"  WARNING: {e}")
                continue

        for prop in sorted(mdf["prop"].unique()):
            # Get reference point from meta
            data_dir = os.path.join(SHARED_DATA,
                                    f"ACASXU_run2a_{ni}_{nj}_batch_2000_prop{prop}_data")
            meta_path = os.path.join(data_dir, "acasxu_meta.json")
            if not os.path.exists(meta_path):
                continue
            with open(meta_path) as f:
                meta = json.load(f)
            ref = meta.get("reference_point")
            if not ref:
                continue

            pred_class, outputs = predict_with_outputs(model_cache[key], ref)

            pdf = mdf[mdf["prop"] == prop]
            report = generate_property_report(ni, nj, prop, pdf, ref, pred_class, outputs)

            out_path = os.path.join(model_dir, f"prop{prop}.md")
            with open(out_path, "w") as f:
                f.write(report)
            report_count += 1

        # Model-level index
        props = sorted(mdf["prop"].unique())
        idx_lines = [f"# N{ni},{nj} — Property Reports", ""]
        idx_lines.append(f"Model: `ACASXU_run2a_{ni}_{nj}_batch_2000.onnx`")
        idx_lines.append("")
        idx_lines.append("| Property | Report |")
        idx_lines.append("|----------|--------|")
        for p in props:
            idx_lines.append(f"| prop{p} | [prop{p}.md](prop{p}.md) |")
        idx_lines.append("")

        with open(os.path.join(model_dir, "README.md"), "w") as f:
            f.write("\n".join(idx_lines))

    print(f"  Generated {report_count} property reports")

    # Top-level index
    print("\n[3/3] Writing top-level index...")
    idx_lines = ["# Per-Property Detail Reports", ""]
    idx_lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    idx_lines.append("")
    idx_lines.append("Each report shows the verification results for **one reference point** (property midpoint),")
    idx_lines.append("answering: *at which ε is this reference point verified, and with which NAP rules?*")
    idx_lines.append("")
    idx_lines.append("| Model | Properties |")
    idx_lines.append("|-------|------------|")

    for (ni, nj), mdf in sorted(model_groups, key=lambda x: (x[0][0], x[0][1])):
        props = sorted(mdf["prop"].unique())
        prop_links = ", ".join(f"[p{p}](N{ni}_{nj}/prop{p}.md)" for p in props)
        idx_lines.append(f"| [N{ni},{nj}](N{ni}_{nj}/) | {prop_links} |")

    idx_lines.append("")
    with open(os.path.join(OUT_ROOT, "README.md"), "w") as f:
        f.write("\n".join(idx_lines))

    print(f"\nDone! Reports in: {OUT_ROOT}")


if __name__ == "__main__":
    main()

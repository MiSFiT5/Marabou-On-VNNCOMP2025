#!/usr/bin/env python3
"""
Generate FIXED per-property ACAS Xu reports.

The original reports have a design issue: for each (model, property) pair,
there is only ONE reference point (property midpoint), but verification
queries are run for ALL classes observed in the full property-region sampling.
Only queries where true_class matches the midpoint's actual predicted class
are meaningful.

This script:
  1. Loads each ONNX model and computes the midpoint's actual prediction.
  2. Filters table3_results.csv to keep only rows where class_id == midpoint prediction.
  3. Generates new markdown reports with "_fix" suffix.
"""
import os, re, glob, gzip, shutil, json, math
from collections import defaultdict
from datetime import datetime

import numpy as np
import pandas as pd

try:
    import onnxruntime as ort
except ImportError:
    raise ImportError("pip install onnxruntime")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = SCRIPT_DIR
NAP_DIR = os.path.join(os.path.dirname(os.path.dirname(REPO_ROOT)), "nap_verify")
SHARED_DATA = os.path.join(NAP_DIR, "shared_data", "acasxu")
EXP_ROOT = os.path.join(NAP_DIR, "experiments")
ONNX_DIR = os.path.join(
    os.path.dirname(os.path.dirname(REPO_ROOT)),
    "vnncomp2025_benchmarks", "benchmarks", "acasxu_2023", "onnx",
)
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


# ─── Step 1: Get midpoint predictions ─────────────────────────────────────────

def get_onnx_path(ni, nj):
    """Get path to uncompressed ONNX file, decompressing if needed."""
    name = f"ACASXU_run2a_{ni}_{nj}_batch_2000.onnx"
    path = os.path.join(ONNX_DIR, name)
    if os.path.exists(path):
        return path
    gz_path = path + ".gz"
    if os.path.exists(gz_path):
        print(f"  Decompressing {name}.gz ...")
        with gzip.open(gz_path, "rb") as f_in, open(path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        return path
    raise FileNotFoundError(f"Cannot find {name} or {name}.gz in {ONNX_DIR}")


def predict_class(onnx_path, input_vec):
    """Run inference and return argmin (ACAS Xu convention: lowest score = recommendation)."""
    sess = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
    inp = sess.get_inputs()[0]
    x = np.array(input_vec, dtype=np.float32).reshape(inp.shape)
    out = sess.run(None, {inp.name: x})[0]
    return int(np.argmin(out.flatten()))


def load_all_midpoint_predictions():
    """For every (model, property) pair, compute the midpoint's actual predicted class."""
    results = {}  # (ni, nj, prop) -> predicted_class

    data_dirs = sorted(glob.glob(os.path.join(SHARED_DATA, "*_prop*_data")))
    prop_re = re.compile(r"ACASXU_run2a_(\d+)_(\d+)_batch_2000_prop(\d+)_data")

    # Cache ONNX sessions by model
    model_cache = {}

    for d in data_dirs:
        m = prop_re.search(os.path.basename(d))
        if not m:
            continue
        ni, nj, prop = int(m.group(1)), int(m.group(2)), int(m.group(3))

        meta_path = os.path.join(d, "acasxu_meta.json")
        if not os.path.exists(meta_path):
            continue
        with open(meta_path) as f:
            meta = json.load(f)

        ref = meta.get("reference_point")
        if not ref:
            continue

        model_key = (ni, nj)
        if model_key not in model_cache:
            try:
                model_cache[model_key] = get_onnx_path(ni, nj)
            except FileNotFoundError as e:
                print(f"  WARNING: {e}")
                continue

        pred = predict_class(model_cache[model_key], ref)
        results[(ni, nj, prop)] = pred

    return results


# ─── Step 2: Load and filter CSV data ──────────────────────────────────────────

def load_all_data(midpoint_preds):
    """Load all per-property CSVs, tagging each row with whether it matches midpoint prediction."""
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
        ni, nj, prop = int(net_i), int(net_j), int(prop_id)

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

        df["net_i"] = ni
        df["net_j"] = nj
        df["model"] = f"{ni}_{nj}"
        df["prop"] = prop
        df["alpha"] = float(alpha)
        df["exp_type"] = exp_type
        df["layer_pair"] = layer if layer else "all"

        # Tag: does this row's class_id match the midpoint prediction?
        midpoint_pred = midpoint_preds.get((ni, nj, prop))
        df["midpoint_pred"] = midpoint_pred
        df["class_matches_midpoint"] = df["class_id"].astype(int) == midpoint_pred

        rows.append(df)

    if not rows:
        print("No data found!")
        return pd.DataFrame()
    return pd.concat(rows, ignore_index=True)


# ─── Step 3: Report generation ─────────────────────────────────────────────────

def valid_rows(df):
    return df[df["result"].isin(VALID_RESULTS)].copy()


def dedupe_baseline_queries(df, keep_alpha=False):
    """Collapse repeated baseline runs to one canonical run per unique query."""
    is_bl = df["table"].str.contains("baseline", case=False, na=False)
    bl = df[is_bl].copy()
    nap = df[~is_bl].copy()
    if bl.empty:
        return df

    is_unary = df["table"].str.contains("ALWAYS_O", case=False, na=False)
    unary = df[is_unary & ~is_bl].copy()

    group_cols_bl = ["model", "prop", "epsilon", "true_class", "target_label"]
    if keep_alpha:
        group_cols_bl.append("alpha")
    bl_dedup = bl.sort_values("time_s").drop_duplicates(subset=group_cols_bl, keep="first")

    non_unary_nap = nap[~nap["table"].str.contains("ALWAYS_O", case=False, na=False)]

    group_cols_un = ["model", "prop", "epsilon", "true_class", "target_label", "table"]
    if keep_alpha:
        group_cols_un.append("alpha")
    unary_dedup = unary.sort_values("time_s").drop_duplicates(subset=group_cols_un, keep="first")

    return pd.concat([bl_dedup, unary_dedup, non_unary_nap], ignore_index=True)


def fmt_cell(result, time_s):
    if result == "-":
        return "–"
    t = int(round(time_s))
    if result == "Y":
        return f"🟢 Y<br><sub>{t}s</sub>"
    elif result == "T/o":
        return f"🟡 T/o<br><sub>{t}s</sub>"
    else:
        return f"🔴 N<br><sub>{t}s</sub>"


def generate_model_report(model, mdf, midpoint_preds):
    """Generate a single model's fixed report."""
    ni, nj = model.split("_")
    ni_int, nj_int = int(ni), int(nj)

    lines = []
    lines.append(f"# Model Report: N{ni},{nj} — FIXED (Per-Property)")
    lines.append("")
    lines.append(f"> **ACAS Xu** — N{ni},{nj}  ")
    lines.append(f"> **FIXED version**: Only queries where `true_class` matches the midpoint's actual prediction are included.  ")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")
    lines.append(f"**Model file:** `ACASXU_run2a_{ni}_{nj}_batch_2000.onnx`  ")

    props = sorted(mdf["prop"].unique())
    prop_strs = [f"prop{p}" for p in props]
    lines.append(f"**Properties covered:** {', '.join(prop_strs)} ({len(props)} total)  ")

    exp_types = sorted(mdf["exp_type"].unique())
    et_names = {"A_full_rule": "full_rule", "B_per_layer": "per_layer", "C_impl_ablation": "impl_ablation"}
    lines.append(f"**Experiment types:** {', '.join(et_names.get(e, e) for e in exp_types)}")
    lines.append("")

    # ── Diagnosis: What was wrong ──
    lines.append("## What Was Fixed")
    lines.append("")
    lines.append("The original reports ran verification queries for **every class observed in the full property-region sampling**,")
    lines.append("but there is only **one reference point** (the property midpoint) per property.")
    lines.append("Only the class that the network actually predicts at the midpoint is meaningful as `true_class`.")
    lines.append("All other `true_class` values create queries where the center point and the class assumption are inconsistent.")
    lines.append("")
    lines.append("This fixed report keeps **only** queries where `true_class == midpoint_predicted_class`.")
    lines.append("")

    # ── Query accounting ──
    lines.append("## Per-Property Query Accounting (Fixed)")
    lines.append("")
    lines.append("| Property | Midpoint predicts | Original true classes (from sampling) | Original queries/ε | **Fixed queries/ε** | Removed |")
    lines.append("|----------|-------------------|--------------------------------------|--------------------|--------------------|---------|")

    total_fixed = 0
    total_orig = 0
    prop_info = {}

    for prop in props:
        pred = midpoint_preds.get((ni_int, nj_int, prop), None)

        # Get original classes from full data (before filtering)
        pdf = mdf[mdf["prop"] == prop]
        vr = valid_rows(pdf)
        orig_classes = sorted(vr["true_class"].unique())
        orig_per_eps = len(orig_classes) * 4  # each class × 4 targets

        if pred is not None:
            fixed_per_eps = 1 * 4  # only 1 class × 4 targets
            removed = orig_per_eps - fixed_per_eps
        else:
            fixed_per_eps = orig_per_eps
            removed = 0

        total_fixed += fixed_per_eps
        total_orig += orig_per_eps
        prop_info[prop] = {"pred": pred, "orig_classes": orig_classes, "fixed_per_eps": fixed_per_eps}

        orig_cls_str = ", ".join(str(c) for c in orig_classes)
        pred_str = str(pred) if pred is not None else "?"

        lines.append(
            f"| prop{prop} | **class {pred_str}** | {orig_cls_str} | "
            f"{orig_per_eps} | **{fixed_per_eps}** | {removed} |"
        )

    lines.append(f"| **Total** | – | – | {total_orig} | **{total_fixed}** | {total_orig - total_fixed} |")
    lines.append("")

    lines.append(f"**Why every denominator is now {total_fixed}:**  ")
    lines.append(f"Each property has exactly 1 reference point (the midpoint) with 1 predicted class, giving 1 × 4 = 4 queries per property per ε.  ")
    lines.append(f"With {len(props)} properties: {len(props)} × 4 = **{total_fixed}** queries per ε.  ")
    lines.append(f"The `Total Y%` column divides by {total_fixed} × 4 = **{total_fixed * 4}** (across all four ε values).")
    lines.append("")
    lines.append(f"*Original denominator was {total_orig} — reduced by {total_orig - total_fixed} queries ({(total_orig - total_fixed)/total_orig*100:.0f}% were mismatched).*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Filter data to only matching rows ──
    fdf = mdf[mdf["class_matches_midpoint"] == True].copy()

    # ── Summary tables ──
    lines.append("## Aggregated Summary (across all properties, FIXED)")
    lines.append("")

    for exp_type, exp_label in [("A_full_rule", "Full-Rule"), ("B_per_layer", "Per-Layer"), ("C_impl_ablation", "Impl-Ablation")]:
        edf = fdf[fdf["exp_type"] == exp_type]
        if edf.empty:
            continue

        lines.append(f"### {exp_label}")
        lines.append("")

        if exp_type == "B_per_layer":
            lines.append("_Per-layer unary/baseline rows are deduplicated across the 5 layer-pair directories._")
            lines.append("")

        for alpha in ALPHAS:
            adf = edf[abs(edf["alpha"] - alpha) < 1e-6]
            vdf = valid_rows(adf)

            if exp_type in ("B_per_layer", "C_impl_ablation"):
                vdf = dedupe_baseline_queries(vdf, keep_alpha=True)

            if vdf.empty:
                continue

            denom = len(vdf[vdf["table"] == vdf["table"].unique()[0]]) if len(vdf["table"].unique()) > 0 else 0

            lines.append(f"#### α = {alpha}")
            lines.append("")
            lines.append("| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |")
            lines.append("|------|--------|--------|--------|--------|----------|")

            for tname in vdf["table"].unique():
                tdf = vdf[vdf["table"] == tname]
                total_y = 0
                total_q = 0
                cells = []
                for eps in EPSILONS:
                    erows = tdf[abs(tdf["epsilon"] - eps) < 1e-6]
                    valid_e = erows[erows["result"].isin(VALID_RESULTS)]
                    ny = (valid_e["result"] == "Y").sum()
                    nt = len(valid_e)
                    total_y += ny
                    total_q += nt
                    if nt > 0:
                        cells.append(f"{ny}/{nt} ({ny/nt*100:.1f}%)")
                    else:
                        cells.append("–")

                ty_pct = f"{total_y/total_q*100:.1f}%" if total_q > 0 else "–"
                cells_str = " | ".join(cells)
                lines.append(f"| `{tname}` | {cells_str} | {ty_pct} |")

            lines.append("")

    return "\n".join(lines)


def generate_aggregated_report(data, midpoint_preds):
    """Generate the aggregated fixed report across all models."""
    lines = []
    lines.append("# ACAS Xu Per-Property Verification — FIXED Aggregated Report")
    lines.append("")
    lines.append(f"> Generated {datetime.now().strftime('%Y-%m-%d')}  ")
    lines.append("> **FIXED**: Only queries where `true_class == midpoint_predicted_class` are included.")
    lines.append("")

    # ── Diagnosis section ──
    lines.append("## What Was Fixed and Why")
    lines.append("")
    lines.append("### The Problem")
    lines.append("")
    lines.append("In the original experiment, for each (model, property) pair:")
    lines.append("1. 50,000 points are sampled uniformly within the property's input box.")
    lines.append("2. Each point is classified by the network → multiple classes observed (e.g., {0, 1, 2, 4}).")
    lines.append("3. NAP rules are mined **per class** from these samples.")
    lines.append("4. Verification queries are run for **every observed class** as `true_class`.")
    lines.append("")
    lines.append("But there is only **one reference point** (the property midpoint), and it has **one predicted class**.")
    lines.append("When `true_class ≠ midpoint_predicted_class`, the query asks an incoherent question:")
    lines.append("the ε-ball is centered on a point the network classifies as (say) class 0, but we're checking")
    lines.append("robustness for class 2 using NAP rules mined from class 2's region (which may be far from the midpoint).")
    lines.append("")
    lines.append("### The Fix")
    lines.append("")
    lines.append("This report keeps **only** the queries where `true_class` matches the midpoint's actual prediction.")
    lines.append("Each property now contributes exactly **4 queries per ε** (1 true class × 4 target labels).")
    lines.append("")

    # ── Filter to matched rows only ──
    fdf = data[data["class_matches_midpoint"] == True].copy()
    vdf = valid_rows(fdf)

    n_models = vdf["model"].nunique()
    n_pairs = vdf.groupby(["model", "prop"]).ngroups

    orig_all = valid_rows(data)
    n_orig_pairs = orig_all.groupby(["model", "prop"]).ngroups

    lines.append("### Impact")
    lines.append("")
    lines.append(f"- **Original (model, property) pairs:** {n_orig_pairs}")
    lines.append(f"- **Fixed (model, property) pairs:** {n_pairs}")
    lines.append(f"- **Original queries per ε (sum across all pairs):** {len(valid_rows(data[data['exp_type'] == 'A_full_rule'].drop_duplicates(subset=['model','prop','epsilon','true_class','target_label','table','alpha'])).drop_duplicates(subset=['model','prop','epsilon','true_class','target_label']).query('table.str.contains(\"baseline\")', engine='python'))}")

    # Compute original vs fixed denominators
    orig_bl = data[(data["exp_type"] == "A_full_rule")]
    orig_bl_v = valid_rows(orig_bl)
    # Get unique baseline queries per alpha=0.99
    orig_bl_99 = orig_bl_v[(abs(orig_bl_v["alpha"] - 0.99) < 1e-6) & orig_bl_v["table"].str.contains("baseline", case=False)]
    orig_bl_99_eps02 = orig_bl_99[abs(orig_bl_99["epsilon"] - 0.02) < 1e-6]

    fix_bl = fdf[(fdf["exp_type"] == "A_full_rule")]
    fix_bl_v = valid_rows(fix_bl)
    fix_bl_99 = fix_bl_v[(abs(fix_bl_v["alpha"] - 0.99) < 1e-6) & fix_bl_v["table"].str.contains("baseline", case=False)]
    fix_bl_99_eps02 = fix_bl_99[abs(fix_bl_99["epsilon"] - 0.02) < 1e-6]

    lines.append(f"- **Original baseline queries at ε=0.02 (α=0.99):** {len(orig_bl_99_eps02)}")
    lines.append(f"- **Fixed baseline queries at ε=0.02:** {len(fix_bl_99_eps02)}")
    lines.append(f"- **Queries removed:** {len(orig_bl_99_eps02) - len(fix_bl_99_eps02)} ({(len(orig_bl_99_eps02) - len(fix_bl_99_eps02))/max(len(orig_bl_99_eps02),1)*100:.0f}%)")
    lines.append("")

    # ── Midpoint prediction summary ──
    lines.append("## Midpoint Predictions")
    lines.append("")
    lines.append("For each (model, property) pair, the midpoint's actual predicted class:")
    lines.append("")
    lines.append("| Model | Property | Midpoint Predicted Class | Original Classes (from sampling) |")
    lines.append("|-------|----------|------------------------|----------------------------------|")

    for model in sorted(data["model"].unique(), key=lambda m: (int(m.split("_")[0]), int(m.split("_")[1]))):
        ni, nj = model.split("_")
        ni_int, nj_int = int(ni), int(nj)
        mdf = data[data["model"] == model]
        for prop in sorted(mdf["prop"].unique()):
            pred = midpoint_preds.get((ni_int, nj_int, prop), "?")
            orig_classes = sorted(valid_rows(mdf[mdf["prop"] == prop])["true_class"].unique())
            orig_str = ", ".join(str(c) for c in orig_classes)
            match_marker = "" if pred in orig_classes else " ⚠️"
            lines.append(f"| N{ni},{nj} | prop{prop} | **{pred}**{match_marker} | {orig_str} |")

    lines.append("")

    # ── Baseline comparison ──
    lines.append("## Baseline Results (Fixed)")
    lines.append("")

    bl_fr = fdf[(fdf["exp_type"] == "A_full_rule") & fdf["table"].str.contains("baseline", case=False)]
    bl_v = valid_rows(bl_fr)
    # Deduplicate across alphas
    bl_dedup = bl_v.sort_values("time_s").drop_duplicates(
        subset=["model", "prop", "epsilon", "true_class", "target_label"], keep="first"
    )

    lines.append("| ε | Y | N | T/o | Total | Verified % |")
    lines.append("|---|---|---|-----|-------|------------|")
    for eps in EPSILONS:
        ebl = bl_dedup[abs(bl_dedup["epsilon"] - eps) < 1e-6]
        ny = (ebl["result"] == "Y").sum()
        nn = (ebl["result"] == "N").sum()
        nto = (ebl["result"] == "T/o").sum()
        tot = ny + nn + nto
        pct = f"{ny/tot*100:.1f}%" if tot > 0 else "–"
        lines.append(f"| {eps} | {ny} | {nn} | {nto} | {tot} | {pct} |")

    lines.append("")

    # ── Full-Rule NAP results by rule type ──
    lines.append("## Full-Rule NAP Results by Rule Type (Fixed, ε=0.02)")
    lines.append("")

    fr = fdf[fdf["exp_type"] == "A_full_rule"]
    fr_v = valid_rows(fr)
    fr_02 = fr_v[abs(fr_v["epsilon"] - 0.02) < 1e-6]

    for alpha in ALPHAS:
        adf = fr_02[abs(fr_02["alpha"] - alpha) < 1e-6]
        if adf.empty:
            continue

        lines.append(f"### α = {alpha}")
        lines.append("")
        lines.append("| Rule Type | Y | N | T/o | Total | Verified % |")
        lines.append("|-----------|---|---|-----|-------|------------|")

        for tname in sorted(adf["table"].unique()):
            tdf = adf[adf["table"] == tname]
            ny = (tdf["result"] == "Y").sum()
            nn = (tdf["result"] == "N").sum()
            nto = (tdf["result"] == "T/o").sum()
            tot = ny + nn + nto
            pct = f"{ny/tot*100:.1f}%" if tot > 0 else "–"
            lines.append(f"| `{tname}` | {ny} | {nn} | {nto} | {tot} | {pct} |")

        lines.append("")

    # ── Per-model summary ──
    lines.append("## Per-Model Summary")
    lines.append("")
    lines.append("| Model | Props | Fixed Queries/ε | Original Queries/ε | Reduction | Best NAP Y% (ε=0.02, α=0.90) |")
    lines.append("|-------|-------|-----------------|--------------------|-----------|-----------------------------|")

    for model in sorted(data["model"].unique(), key=lambda m: (int(m.split("_")[0]), int(m.split("_")[1]))):
        ni, nj = model.split("_")
        mdf_orig = data[data["model"] == model]
        mdf_fix = fdf[fdf["model"] == model]
        n_props = mdf_orig["prop"].nunique()

        fix_per_eps = n_props * 4

        orig_vr = valid_rows(mdf_orig[(mdf_orig["exp_type"] == "A_full_rule") & (abs(mdf_orig["alpha"] - 0.99) < 1e-6)])
        orig_bl = orig_vr[orig_vr["table"].str.contains("baseline", case=False)]
        orig_bl_02 = orig_bl[abs(orig_bl["epsilon"] - 0.02) < 1e-6]
        orig_per_eps = len(orig_bl_02)

        reduction = orig_per_eps - fix_per_eps

        # Best NAP Y% at eps=0.02, alpha=0.90 (fixed)
        mfix_fr = mdf_fix[(mdf_fix["exp_type"] == "A_full_rule") &
                          (abs(mdf_fix["alpha"] - 0.90) < 1e-6) &
                          (abs(mdf_fix["epsilon"] - 0.02) < 1e-6)]
        mfix_v = valid_rows(mfix_fr)
        mfix_nap = mfix_v[~mfix_v["table"].str.contains("baseline", case=False)]

        if len(mfix_nap) > 0:
            # Find best single rule type
            best_pct = 0
            best_rule = ""
            for tname in mfix_nap["table"].unique():
                tdf = mfix_nap[mfix_nap["table"] == tname]
                pct = (tdf["result"] == "Y").sum() / len(tdf) * 100
                if pct > best_pct:
                    best_pct = pct
                    best_rule = tname
            best_str = f"{best_pct:.1f}% ({best_rule})"
        else:
            best_str = "–"

        lines.append(
            f"| [N{ni},{nj}](N{ni}_{nj}_fix.md) | {n_props} | "
            f"{fix_per_eps} | {orig_per_eps} | −{reduction} | {best_str} |"
        )

    lines.append("")
    return "\n".join(lines)


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("ACAS Xu Fixed Report Generator")
    print("=" * 70)

    # Step 1: Get midpoint predictions
    print("\n[1/3] Computing midpoint predictions for all (model, property) pairs...")
    midpoint_preds = load_all_midpoint_predictions()
    print(f"  Got predictions for {len(midpoint_preds)} (model, property) pairs")

    # Print distribution
    from collections import Counter
    class_dist = Counter(midpoint_preds.values())
    print(f"  Class distribution: {dict(sorted(class_dist.items()))}")

    # Step 2: Load CSV data
    print("\n[2/3] Loading CSV data...")
    data = load_all_data(midpoint_preds)
    if data.empty:
        print("No data found!")
        return

    total_rows = len(data)
    matched_rows = data["class_matches_midpoint"].sum()
    print(f"  Total rows: {total_rows}")
    print(f"  Matched rows (class == midpoint pred): {matched_rows} ({matched_rows/total_rows*100:.1f}%)")
    print(f"  Removed rows: {total_rows - matched_rows} ({(total_rows-matched_rows)/total_rows*100:.1f}%)")

    # Step 3: Generate reports
    print("\n[3/3] Generating fixed reports...")
    os.makedirs(OUT_DIR, exist_ok=True)

    models = sorted(data["model"].unique(), key=lambda m: (int(m.split("_")[0]), int(m.split("_")[1])))

    for model in models:
        mdf = data[data["model"] == model]
        ni, nj = model.split("_")
        report = generate_model_report(model, mdf, midpoint_preds)
        out_path = os.path.join(OUT_DIR, f"N{ni}_{nj}_fix.md")
        with open(out_path, "w") as f:
            f.write(report)
        print(f"  Written: {os.path.basename(out_path)}")

    # Aggregated report
    agg_report = generate_aggregated_report(data, midpoint_preds)
    agg_path = os.path.join(OUT_DIR, "All_Models_Aggregated_fix.md")
    with open(agg_path, "w") as f:
        f.write(agg_report)
    print(f"  Written: {os.path.basename(agg_path)}")

    print("\nDone!")


if __name__ == "__main__":
    main()

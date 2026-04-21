#!/usr/bin/env python3
"""Generate comparison figures for 600s vs 2700s high-timeout layer ablation.

Reads:
  - step4_unary_ablation_full_{A,B}/results/coverage.csv  (600s disjunctive)
  - step4_unary_ablation_ht_{A,B}/results/coverage.csv   (2700s disjunctive)
  - step4_marabou_v2/results/coverage.csv                (baseline, per-target)

Writes figures to markdown/step4_followup_assets/.
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parents[2]
GENERATED = REPO_ROOT / "Random_Initialized_NN" / "generated"
OUT_DIR = THIS_DIR / "markdown" / "step4_followup_assets"

LAYER_LABELS = {
    0: "baseline",
    1: "last1 (L6)",
    2: "last2 (L5-L6)",
    3: "last3 (L4-L6)",
    4: "last4 (L3-L6)",
    5: "last5 (L2-L6)",
    6: "last6 (L1-L6)",
    7: "last7 (L0-L6)",
}

# Styles for 600s vs 2700s comparison
TIMEOUT_STYLE = {
    "600s": {"linestyle": "--", "alpha": 0.65, "linewidth": 1.5},
    "2700s": {"linestyle": "-",  "alpha": 1.0,  "linewidth": 2.0},
}


def setup() -> None:
    matplotlib.rcParams.update({
        "figure.dpi": 180,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linestyle": "--",
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "legend.fontsize": 8,
    })


def load_ablation(track: str, timeout: str) -> pd.DataFrame:
    """Load ablation data (600s or 2700s) for a track."""
    if timeout == "600s":
        path = GENERATED / f"step4_unary_ablation_full_{track}" / "results" / "coverage.csv"
    else:
        path = GENERATED / f"step4_unary_ablation_ht_{track}" / "results" / "coverage.csv"
    df = pd.read_csv(path)
    df["track_id"] = track
    df["timeout_budget"] = timeout
    extracted = df["config"].str.extract(r"unary_last(\d+)")
    df["last_n"] = extracted[0].astype(float).fillna(-1).astype(int)
    df["layer_label"] = df["last_n"].map(LAYER_LABELS)
    return df


def load_baseline(track: str) -> pd.DataFrame:
    """Load baseline (no NAP) from step4_marabou_v2."""
    path = GENERATED / "step4_marabou_v2" / "results" / "coverage.csv"
    df = pd.read_csv(path)
    df = df[(df["config"] == "baseline") & (df.get("track_id", pd.Series(dtype=str)) == track
             if "track_id" in df.columns else pd.Series([True]*len(df)))].copy()
    # Duplicate for both alphas
    frames = []
    for alpha in [0.95, 0.99]:
        tmp = df.copy()
        tmp["alpha"] = alpha
        frames.append(tmp)
    df = pd.concat(frames, ignore_index=True)
    df["track_id"] = track
    df["last_n"] = 0
    df["timeout_budget"] = "baseline (per-target)"
    df["layer_label"] = "baseline"
    return df


def style_axes(ax: plt.Axes, title: str, ylabel: str) -> None:
    ax.set_title(title)
    ax.set_xlabel("Training progress (%)")
    ax.set_ylabel(ylabel)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlim(-3, 103)
    ax.set_ylim(-2, 105)
    ax.grid(True, alpha=0.25)


def make_colormap(n: int) -> list:
    import matplotlib.cm as cm
    return [cm.tab10(i) for i in range(n)]


def plot_ht_comparison(
    metric: str,
    ylabel: str,
    filename: str,
    alpha_val: float,
) -> None:
    """2×2 grid: rows=track, cols=timeout, lines=last_n configs."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 8), sharex=True, sharey=True)

    configs_to_show = [1, 2, 4, 5, 7]  # last_n values to show (skip 3, 6 for clarity)
    colors = make_colormap(len(configs_to_show))
    color_map = {last_n: colors[i] for i, last_n in enumerate(configs_to_show)}

    for row_idx, track in enumerate(["A", "B"]):
        df_600 = load_ablation(track, "600s")
        df_2700 = load_ablation(track, "2700s")
        bsl = load_baseline(track)

        for col_idx, (label, df_budget) in enumerate([
            ("600s (original ablation)", df_600),
            ("2700s (high-timeout)", df_2700),
        ]):
            ax = axes[row_idx][col_idx]

            # Plot baseline
            bsl_sub = bsl[(bsl["alpha"].round(2) == alpha_val) &
                          (bsl["epsilon"].round(4) == 0.02) &
                          (bsl["progress_pct"] >= 0)]
            if not bsl_sub.empty:
                line = bsl_sub.sort_values("progress_pct")
                ax.plot(
                    line["progress_pct"], line[metric],
                    color="#111111", linestyle="--", marker="X",
                    linewidth=2.2, markersize=7, label="baseline (per-target)",
                )

            # Plot each layer config
            for last_n in configs_to_show:
                sub = df_budget[
                    (df_budget["last_n"] == last_n) &
                    (df_budget["alpha"].round(2) == alpha_val) &
                    (df_budget["epsilon"].round(4) == 0.02)
                ].sort_values("progress_pct")
                if sub.empty:
                    continue
                ax.plot(
                    sub["progress_pct"], sub[metric],
                    color=color_map[last_n],
                    marker="o", linewidth=1.8, markersize=5,
                    label=LAYER_LABELS[last_n],
                )

            style_axes(
                ax,
                title=f"Track {track}: {label} | alpha={alpha_val:.2f}, eps=0.02",
                ylabel=ylabel,
            )

    # Legend from first subplot
    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=4, frameon=False,
               bbox_to_anchor=(0.5, 1.04))
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_DIR / filename, bbox_inches="tight")
    plt.close(fig)
    print(f"  Wrote {filename}")


def plot_final_checkpoint_bar(filename: str) -> None:
    """Bar chart: final checkpoint genuine_verified_pct for 600s vs 2700s, by config and alpha."""
    rows = []
    for track in ["A", "B"]:
        for timeout in ["600s", "2700s"]:
            df = load_ablation(track, timeout)
            fin = df[(df["progress_pct"] == 100) & (df["epsilon"].round(4) == 0.02)]
            for _, row in fin.iterrows():
                rows.append({
                    "track": track,
                    "timeout": timeout,
                    "last_n": row["last_n"],
                    "layer_label": row["layer_label"],
                    "alpha": round(float(row["alpha"]), 2),
                    "genuine_pct": float(row["genuine_verified_pct"]),
                    "verified_pct": float(row["verified_pct"]),
                    "n_adversarial": int(row["n_adversarial"]),
                })
    df_plot = pd.DataFrame(rows)

    fig, axes = plt.subplots(2, 2, figsize=(14, 9), sharey=True)
    configs_ordered = [1, 2, 3, 4, 5, 6, 7]
    x = range(len(configs_ordered))
    width = 0.35

    for row_idx, alpha in enumerate([0.95, 0.99]):
        for col_idx, track in enumerate(["A", "B"]):
            ax = axes[row_idx][col_idx]
            sub = df_plot[(df_plot["alpha"] == alpha) & (df_plot["track"] == track)]

            vals_600 = []
            vals_2700 = []
            for ln in configs_ordered:
                r600 = sub[(sub["last_n"] == ln) & (sub["timeout"] == "600s")]
                r2700 = sub[(sub["last_n"] == ln) & (sub["timeout"] == "2700s")]
                vals_600.append(r600["genuine_pct"].values[0] if not r600.empty else 0)
                vals_2700.append(r2700["genuine_pct"].values[0] if not r2700.empty else 0)

            bars600 = ax.bar([xi - width/2 for xi in x], vals_600, width,
                             label="600s", color="#4878d0", alpha=0.8)
            bars2700 = ax.bar([xi + width/2 for xi in x], vals_2700, width,
                              label="2700s", color="#ee854a", alpha=0.9)

            ax.set_xticks(list(x))
            ax.set_xticklabels([LAYER_LABELS[ln].split(" ")[0] for ln in configs_ordered])
            ax.set_ylim(0, 105)
            ax.grid(True, alpha=0.2, axis="y")
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.set_title(f"Track {track}: alpha={alpha:.2f}, eps=0.02, final checkpoint")
            ax.set_ylabel("Genuine verified (%)")
            ax.set_xlabel("Layer config")

    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2, frameon=False,
               bbox_to_anchor=(0.5, 1.03))
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_DIR / filename, bbox_inches="tight")
    plt.close(fig)
    print(f"  Wrote {filename}")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams["savefig.facecolor"] = "white"
    setup()

    print("Generating high-timeout comparison figures...")
    for alpha in [0.95, 0.99]:
        alpha_str = f"{'095' if alpha == 0.95 else '099'}"
        plot_ht_comparison(
            metric="genuine_verified_pct",
            ylabel="Genuine verified (%)",
            filename=f"layer_ht_genuine_alpha{alpha_str}_eps002.png",
            alpha_val=alpha,
        )

    plot_final_checkpoint_bar(filename="layer_ht_final_bar_eps002.png")
    print(f"Done. Assets in {OUT_DIR}")


if __name__ == "__main__":
    main()

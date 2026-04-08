#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parents[2]
GENERATED_ROOT = REPO_ROOT / "Random_Initialized_NN" / "generated"
OUT_DIR = THIS_DIR / "report_imply_onoff_assets"

PROGRESS_ORDER = [0, 25, 50, 75, 100]
ALPHAS = [0.95, 0.99]
EPSILONS = [0.01, 0.02]

METHOD_ORDER = [
    "Baseline",
    "Unary ON/OFF",
    "Implication L4L5",
    "Implication L4L5+L5L6",
]
METHOD_COLORS = {
    "Baseline": "#111111",
    "Unary ON/OFF": "#1f77b4",
    "Implication L4L5": "#d55e00",
    "Implication L4L5+L5L6": "#009e73",
}
METHOD_MARKERS = {
    "Baseline": "o",
    "Unary ON/OFF": "s",
    "Implication L4L5": "^",
    "Implication L4L5+L5L6": "D",
}

PROGRESS_BY_CHECKPOINT = {
    "epoch_000": 0,
    "epoch_018": 25,
    "epoch_025": 25,
    "epoch_035": 50,
    "epoch_050": 50,
    "epoch_052": 75,
    "epoch_070": 100,
    "epoch_075": 75,
    "epoch_100": 100,
}


def _setup_matplotlib() -> None:
    matplotlib.rcParams.update(
        {
            "figure.dpi": 180,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "grid.linestyle": "--",
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "legend.fontsize": 9,
        }
    )


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def _normalize_positive_frame(df: pd.DataFrame, method: str) -> pd.DataFrame:
    out = df.copy()
    out["method"] = method
    out["epsilon"] = out["epsilon"].astype(float).round(4)
    out["progress_pct"] = out["progress_pct"].astype(int)
    if "alpha" not in out.columns:
        out["alpha"] = pd.NA
    else:
        out["alpha"] = pd.to_numeric(out["alpha"], errors="coerce")
    for col in ["verified_pct", "genuine_verified_pct", "n_timeout", "n_semantic_unresolved"]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce").fillna(0.0)
    return out


def _normalize_rejection_frame(df: pd.DataFrame, method: str) -> pd.DataFrame:
    out = df.copy()
    out["method"] = method
    out["epsilon"] = out["epsilon"].astype(float).round(4)
    out["alpha"] = pd.to_numeric(out["alpha"], errors="coerce")
    out["progress_pct"] = out["checkpoint_id"].map(PROGRESS_BY_CHECKPOINT).astype(int)
    for col in ["rejection_rate", "n_timeout"]:
        out[col] = pd.to_numeric(out[col], errors="coerce").fillna(0.0)
    return out


def load_positive_results() -> pd.DataFrame:
    unary = _read_csv(GENERATED_ROOT / "step4_marabou_v2" / "results" / "coverage.csv")
    baseline = _normalize_positive_frame(unary[unary["config"] == "baseline"], "Baseline")
    unary = _normalize_positive_frame(unary[unary["config"] == "unary_nap"], "Unary ON/OFF")

    l4l5 = pd.concat(
        [
            _normalize_positive_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_A_L4L5_allrules" / "results" / "coverage.csv"),
                "Implication L4L5",
            ),
            _normalize_positive_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_B_L4L5_allrules" / "results" / "coverage.csv"),
                "Implication L4L5",
            ),
        ],
        ignore_index=True,
    )
    l4l5_l5l6 = pd.concat(
        [
            _normalize_positive_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_A_L4L5_L5L6" / "results" / "coverage.csv"),
                "Implication L4L5+L5L6",
            ),
            _normalize_positive_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_B_L4L5_L5L6" / "results" / "coverage.csv"),
                "Implication L4L5+L5L6",
            ),
        ],
        ignore_index=True,
    )

    out = pd.concat([baseline, unary, l4l5, l4l5_l5l6], ignore_index=True)
    out = out[out["epsilon"].isin(EPSILONS)].copy()
    return out


def load_rejection_results() -> pd.DataFrame:
    unary = _normalize_rejection_frame(
        _read_csv(GENERATED_ROOT / "step4_marabou_v2" / "results" / "rejection_summary.csv"),
        "Unary ON/OFF",
    )
    l4l5 = pd.concat(
        [
            _normalize_rejection_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_A_L4L5_allrules" / "results" / "rejection_summary.csv"),
                "Implication L4L5",
            ),
            _normalize_rejection_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_B_L4L5_allrules" / "results" / "rejection_summary.csv"),
                "Implication L4L5",
            ),
        ],
        ignore_index=True,
    )
    l4l5_l5l6 = pd.concat(
        [
            _normalize_rejection_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_A_L4L5_L5L6" / "results" / "rejection_summary.csv"),
                "Implication L4L5+L5L6",
            ),
            _normalize_rejection_frame(
                _read_csv(GENERATED_ROOT / "step4_implication_B_L4L5_L5L6" / "results" / "rejection_summary.csv"),
                "Implication L4L5+L5L6",
            ),
        ],
        ignore_index=True,
    )
    out = pd.concat([unary, l4l5, l4l5_l5l6], ignore_index=True)
    out = out[out["epsilon"].isin(EPSILONS)].copy()
    return out


def build_positive_progress_summary(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["method", "alpha", "epsilon", "progress_pct"], dropna=False)[
            ["verified_pct", "genuine_verified_pct", "n_timeout", "n_semantic_unresolved"]
        ]
        .mean()
        .reset_index()
    )
    grouped["alpha_label"] = grouped["alpha"].map(lambda x: "" if pd.isna(x) else f"{x:.2f}")
    return grouped.sort_values(["epsilon", "progress_pct", "method", "alpha_label"])


def build_positive_overall_summary(df: pd.DataFrame) -> pd.DataFrame:
    subset = df[df["progress_pct"] >= 25].copy()
    grouped = (
        subset.groupby(["method", "alpha", "epsilon"], dropna=False)[
            ["verified_pct", "genuine_verified_pct", "n_timeout", "n_semantic_unresolved"]
        ]
        .agg(
            mean_verified_pct=("verified_pct", "mean"),
            mean_genuine_verified_pct=("genuine_verified_pct", "mean"),
            total_timeout=("n_timeout", "sum"),
            total_semantic_unresolved=("n_semantic_unresolved", "sum"),
        )
        .reset_index()
    )
    grouped["alpha_label"] = grouped["alpha"].map(lambda x: "" if pd.isna(x) else f"{x:.2f}")
    return grouped.sort_values(["epsilon", "method", "alpha_label"])


def build_rejection_progress_summary(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["method", "alpha", "epsilon", "progress_pct"])[["rejection_rate", "n_timeout"]]
        .mean()
        .reset_index()
    )
    grouped["alpha_label"] = grouped["alpha"].map(lambda x: f"{x:.2f}")
    return grouped.sort_values(["epsilon", "progress_pct", "method", "alpha_label"])


def build_rejection_overall_summary(df: pd.DataFrame) -> pd.DataFrame:
    subset = df[df["progress_pct"] >= 25].copy()
    grouped = (
        subset.groupby(["method", "alpha", "epsilon"])[["rejection_rate", "n_timeout"]]
        .agg(
            mean_rejection_rate=("rejection_rate", "mean"),
            total_timeout=("n_timeout", "sum"),
        )
        .reset_index()
    )
    grouped["alpha_label"] = grouped["alpha"].map(lambda x: f"{x:.2f}")
    return grouped.sort_values(["epsilon", "method", "alpha_label"])


def _style_axis(ax: plt.Axes, title: str, y_label: str) -> None:
    ax.set_title(title)
    ax.set_xlabel("Training Progress (%)")
    ax.set_ylabel(y_label)
    ax.set_xticks(PROGRESS_ORDER)
    ax.set_xlim(min(PROGRESS_ORDER), max(PROGRESS_ORDER))
    ax.set_ylim(0, 105)


def render_positive_figure(df: pd.DataFrame, value_col: str, output_name: str, y_label: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 9), sharex=True, sharey=True)
    for row_idx, alpha in enumerate(ALPHAS):
        for col_idx, epsilon in enumerate(EPSILONS):
            ax = axes[row_idx, col_idx]
            panel = df[
                (df["epsilon"].eq(epsilon))
                & ((df["alpha"].eq(alpha)) | (df["method"].eq("Baseline")))
            ].copy()
            for method in METHOD_ORDER:
                line = panel[panel["method"].eq(method)].sort_values("progress_pct")
                if line.empty:
                    continue
                ax.plot(
                    line["progress_pct"],
                    line[value_col],
                    marker=METHOD_MARKERS[method],
                    linewidth=2.1 if method != "Baseline" else 1.8,
                    markersize=6,
                    color=METHOD_COLORS[method],
                    linestyle="-" if method != "Baseline" else "--",
                    label=method,
                )
            _style_axis(
                ax,
                title=f"alpha={alpha:.2f}, epsilon={epsilon:.2f}",
                y_label=y_label,
            )
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.01))
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_DIR / output_name, bbox_inches="tight")
    plt.close(fig)


def render_rejection_figure(df: pd.DataFrame, output_name: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 9), sharex=True, sharey=True)
    rejection_methods = [m for m in METHOD_ORDER if m != "Baseline"]
    for row_idx, alpha in enumerate(ALPHAS):
        for col_idx, epsilon in enumerate(EPSILONS):
            ax = axes[row_idx, col_idx]
            panel = df[(df["epsilon"].eq(epsilon)) & (df["alpha"].eq(alpha))].copy()
            for method in rejection_methods:
                line = panel[panel["method"].eq(method)].sort_values("progress_pct")
                if line.empty:
                    continue
                ax.plot(
                    line["progress_pct"],
                    line["rejection_rate"],
                    marker=METHOD_MARKERS[method],
                    linewidth=2.1,
                    markersize=6,
                    color=METHOD_COLORS[method],
                    label=method,
                )
            _style_axis(
                ax,
                title=f"alpha={alpha:.2f}, epsilon={epsilon:.2f}",
                y_label="Rejection Rate (%)",
            )
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.01))
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_DIR / output_name, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams["savefig.facecolor"] = "white"
    _setup_matplotlib()

    positive = load_positive_results()
    rejection = load_rejection_results()

    positive_progress = build_positive_progress_summary(positive)
    positive_overall = build_positive_overall_summary(positive)
    rejection_progress = build_rejection_progress_summary(rejection)
    rejection_overall = build_rejection_overall_summary(rejection)

    positive_progress.to_csv(OUT_DIR / "positive_progress_summary.csv", index=False)
    positive_overall.to_csv(OUT_DIR / "positive_overall_summary.csv", index=False)
    rejection_progress.to_csv(OUT_DIR / "rejection_progress_summary.csv", index=False)
    rejection_overall.to_csv(OUT_DIR / "rejection_overall_summary.csv", index=False)

    render_positive_figure(
        positive_progress,
        value_col="verified_pct",
        output_name="fig14_imply_onoff_verified.png",
        y_label="Verified Rate (%)",
    )
    render_positive_figure(
        positive_progress,
        value_col="genuine_verified_pct",
        output_name="fig15_imply_onoff_genuine.png",
        y_label="Genuine Verified Rate (%)",
    )
    render_rejection_figure(
        rejection_progress,
        output_name="fig16_imply_onoff_rejection.png",
    )

    print(f"Wrote assets to {OUT_DIR}")


if __name__ == "__main__":
    tempfile.gettempdir()
    main()

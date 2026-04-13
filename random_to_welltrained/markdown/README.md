# Step 4: Fixed-Reference NAP Verification

> Generated 2026-04-01

## Motivation

Step 3 used **per-checkpoint** references (each checkpoint picks its own 10 correctly classified test samples). This makes it impossible to separate "the model changed" from "the sample changed." Step 4 fixes a **single set of 20 unified references** across all checkpoints within each track, so that any change in verified rate is attributable purely to the model / NAP evolution.

## Reference Selection Protocol

### v2 (current, `step4_unified_v2`)

1. For each track, collect ONNX predictions from all checkpoints on the MNIST test set.
2. **Exclude** checkpoints with `progress < 25%` (i.e., `epoch_000`) from the intersection.
3. Take samples correctly classified by **all remaining checkpoints**.
4. Select the first 20 such samples (in dataset order) as unified refs.
5. `epoch_000` is still **evaluated** on these refs but was not used to **select** them.

This avoids the v1 problem where `epoch_000` (random init, predicts almost everything as digit 9) polluted the intersection, resulting in all refs being digit 9.

### Unified Ref Label Distribution (v2)

Both Track A and Track B share the same distribution:

| Digit | 0 | 1 | 2 | 4 | 5 | 6 | 7 | 9 |
|-------|---|---|---|---|---|---|---|---|
| Count | 3 | 3 | 1 | 3 | 1 | 2 | 2 | 5 |

**Missing classes:** 3, 8 — these digits happen to be misclassified by at least one intermediate checkpoint among the first 20 candidates in dataset order. The selection is **not class-balanced**; it takes the first 20 intersection-correct samples by index.

### epoch_000 Behavior on Fixed Refs

Since the refs are chosen to be correct for checkpoints at 25%+, `epoch_000` (random init) misclassifies most of them:
- **15/20 misclassified**, only 5/20 eligible for verification at `epoch_000`

## Verification Setup

| Parameter | Value |
|-----------|-------|
| References per track | 20 (fixed unified set) |
| Epsilon values | 0.01, 0.02 (active); 0.05, 0.1, 0.2 (skipped by Marabou due to `--max-epsilon=0.02`) |
| Alpha (NAP confidence) | 0.95, 0.99 |
| NAP rule types | ALWAYS_ON, ALWAYS_OFF (unary only) |

### Solvers

| Solver | Timeout | Role |
|--------|---------|------|
| auto_LiRPA (incomplete) | — | Fast trend scan; gives `verified` or `unknown`; no timeout issue |
| Marabou (exact) | 300s | Ground truth; gives `Y` / `N` / `T/o` |

### Task Counts

| Experiment | Config | Tasks | Description |
|------------|--------|-------|-------------|
| `step4_unified_v2` | BL + NAP | 3000 verify + 400 rejection | auto_LiRPA on fixed refs |
| `step4_marabou_v2` | BL + NAP | 600 verify + 400 rejection | Marabou exact on fixed refs (eps ≤ 0.02 only) |

## Reports

- **[Step4_All_Tracks_Aggregated.md](Step4_All_Tracks_Aggregated.md)** — Full results tables, solver comparison, rejection
- **[Step4_Implication_Families_Exact.md](Step4_Implication_Families_Exact.md)** — Unary vs implication vs compressed exact data tables
- **[Step4_NAP_Rejection_Evidence.md](Step4_NAP_Rejection_Evidence.md)** — Follow-up rejection evidence: pairwise class-NAP separation and direct pointwise rejection of misclassified samples
- **[Step4_Unary_Layer_Ablation.md](Step4_Unary_Layer_Ablation.md)** — Follow-up last-n layer ablation for unary ALWAYS_ON / ALWAYS_OFF NAP rules

### Per-Track Reports

- [Step4_Track_A.md](Step4_Track_A.md) — Track A: Standard CE, 70 epochs
- [Step4_Track_B.md](Step4_Track_B.md) — Track B: Standard CE, 100 epochs

## Key Differences from Step 3

| Aspect | Step 3 | Step 4 |
|--------|--------|--------|
| References | 10 per checkpoint (per-checkpoint) | 20 per track (fixed across checkpoints) |
| Class coverage | Varies per checkpoint | 8 classes (missing 3, 8) |
| epoch_000 refs | All digit 9 | 15/20 misclassified |
| Confound | Sample-selection artifact possible | Eliminated by design |
| Solvers | Marabou + alpha-beta-CROWN | auto_LiRPA + Marabou |

## Key Findings

### 1. NAP Trend Survives Fixed References

Under the same 20 refs across all checkpoints, NAP still shows clear verified gain over baseline at eps=0.01 and eps=0.02.

### 2. Genuine vs Vacuous Decomposition

| Solver | alpha | eps=0.01 genuine (mean, progress≥25%) | eps=0.02 genuine (mean, progress≥25%) |
|--------|-------|---------------------------------------|---------------------------------------|
| auto_LiRPA | 0.95 | 63.1% | 30.6% |
| auto_LiRPA | 0.99 | 85.0% | 28.1% |
| Marabou | 0.95 | 47.5% | 51.9% |
| Marabou | 0.99 | 66.2% | 30.0% |
| Baseline (Marabou) | — | 80.0% | 12.5% |

### 3. NAP Rejection of Misclassified Samples

NAP consistently rejects (vacuous) local regions around misclassified samples, with rejection rates increasing with training progress. This is confirmed by both auto_LiRPA and Marabou exact.

### 4. Follow-up: Direct Rejection and Pairwise Class-NAP Separation

The newer rejection follow-up separates two questions that were previously mixed together. First, pairwise class-NAP checks show that full-layer unary class NAPs become mutually inconsistent in the bounded MNIST input domain `[0,1]^784`: random-init class NAPs all overlap, while trained class pairs become almost entirely disjoint by 25% training and fully disjoint after 50% training. Second, direct pointwise checks show that trained `alpha=0.99` NAPs reject 98.4-100.0% of misclassified samples under the true-class NAP, while rejecting 15.6-22.2% of correctly classified samples.

See [Step4_NAP_Rejection_Evidence.md](Step4_NAP_Rejection_Evidence.md).

### 5. Follow-up: Last-n Layer Ablation for Unary NAP

The layer-ablation follow-up shows that the small-radius unary ON/OFF signal is concentrated in the final layers. At `eps=0.01`, `alpha=0.99`, using only `last1` (`L6`) already reaches `18/18/2/0` on Track A final and `20/20/0/0` on Track B final, where the cell format is `genuine / verified / timeout / misclassified`. In contrast, full-layer `last7` at `alpha=0.95` is inflated by vacuity: Track A final is `9/19/1/0`, and Track B final is `10/20/0/0`. At `eps=0.02`, the result is timeout-limited rather than adversarial-dominated.

See [Step4_Unary_Layer_Ablation.md](Step4_Unary_Layer_Ablation.md).

### 6. auto_LiRPA vs Marabou Agreement

Baseline genuine results are close between the two solvers. For NAP, auto_LiRPA tends to be more optimistic than Marabou exact, especially for alpha=0.95 at eps=0.01.

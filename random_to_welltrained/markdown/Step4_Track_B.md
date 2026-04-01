# Step 4 Track B Report: Fixed-Reference Verification

> **Track B** — 100 epochs, 5 checkpoints, 20 fixed unified refs
> Baseline + unary NAP (ALWAYS_ON + ALWAYS_OFF)
> Generated 2026-04-01

**Architecture:** 784 → 7×250 hidden → 10 (fully-connected ReLU, MNIST)
**Total epochs:** 100
**Training:** Standard cross-entropy
**Checkpoints:** epoch_000, epoch_025, epoch_050, epoch_075, epoch_100
**References:** 20 unified (fixed across all checkpoints, selected from intersection of checkpoints with progress ≥ 25%)
**Ref labels:** {9:5, 0:3, 1:3, 4:3, 6:2, 7:2, 2:1, 5:1} — missing digits 3, 8

---

## auto_LiRPA Verification (Incomplete)

Denominator: 20 total refs (including misclassified at epoch_000).
`Y = verified`, `? = unknown`, `mis = misclassified by this checkpoint`

### Baseline

| Checkpoint | Progress | eps=0.01 | eps=0.02 |
|------------|----------|----------|----------|
| epoch_000 | 0% | 0/5 eligible (15 mis) | 0/5 eligible |
| epoch_025 | 25% | **14/20** (70%) | **1/20** (5%) |
| epoch_050 | 50% | **17/20** (85%) | **6/20** (30%) |
| epoch_075 | 75% | **20/20** (100%) | **5/20** (25%) |
| epoch_100 | 100% | **20/20** (100%) | **5/20** (25%) |

### NAP alpha=0.95 — Genuine Verified

Format: `genuine/20 (v=vacuous)`

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **1/20** (v=1) [5 eligible] | 0/20 |
| epoch_025 | **14/20** (v=6) | **5/20** (v=2) |
| epoch_050 | **11/20** (v=9) | **6/20** (v=3) |
| epoch_075 | **14/20** (v=6) | **9/20** (v=2) |
| epoch_100 | **13/20** (v=7) | **9/20** (v=2) |

### NAP alpha=0.99 — Genuine Verified

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **1/20** (v=0) [5 eligible] | 0/20 |
| epoch_025 | **13/20** (v=1) | **1/20** (v=0) |
| epoch_050 | **19/20** (v=0) | **6/20** (v=0) |
| epoch_075 | **20/20** (v=0) | **9/20** (v=0) |
| epoch_100 | **20/20** (v=0) | **9/20** (v=0) |

---

## Marabou Exact Verification

`Y = UNSAT (verified)`, `N = SAT (adversarial found)`, `T/o = timeout (300s)`
Only eps ≤ 0.02 were run (larger eps skipped via `--max-epsilon=0.02`).

### Baseline

| Checkpoint | eps | Y | N | T/o | Verified % |
|------------|-----|---|---|-----|-----------|
| epoch_000 | 0.01 | 0 | 0 | 5 | 0.0% (15 mis) |
| epoch_000 | 0.02 | 0 | 0 | 5 | 0.0% (15 mis) |
| epoch_025 | 0.01 | 14 | 0 | 6 | 70.0% |
| epoch_025 | 0.02 | 0 | 0 | 20 | 0.0% |
| epoch_050 | 0.01 | 16 | 0 | 4 | 80.0% |
| epoch_050 | 0.02 | 3 | 1 | 16 | 15.0% |
| epoch_075 | 0.01 | 18 | 0 | 2 | 90.0% |
| epoch_075 | 0.02 | 4 | 0 | 16 | 20.0% |
| epoch_100 | 0.01 | 18 | 0 | 2 | 90.0% |
| epoch_100 | 0.02 | 4 | 0 | 16 | 20.0% |

### NAP alpha=0.95 — Marabou Genuine Verified

Format: `genuine/20 (v=vacuous, u=semantic_unresolved)`

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **3/20** (v=1, u=1) [5 elig] | 0/20 |
| epoch_025 | **9/20** (v=6, u=4) | **6/20** (v=2, u=0) |
| epoch_050 | **10/20** (v=9, u=1) | **10/20** (v=3, u=3) |
| epoch_075 | **9/20** (v=7, u=4) | **16/20** (v=2, u=2) |
| epoch_100 | **10/20** (v=7, u=3) | **15/20** (v=2, u=2) |

### NAP alpha=0.99 — Marabou Genuine Verified

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **5/20** (v=0, u=0) [5 elig] | 0/20 |
| epoch_025 | **7/20** (v=1, u=7) | **1/20** (v=0, u=0) |
| epoch_050 | **16/20** (v=0, u=3) | **8/20** (v=0, u=0) |
| epoch_075 | **16/20** (v=0, u=4) | **12/20** (v=0, u=0) |
| epoch_100 | **16/20** (v=0, u=4) | **11/20** (v=0, u=0) |

---

## NAP Rejection of Misclassified Samples

10 misclassified refs per checkpoint.
Rejection = B(ref, eps) ∩ NAP = ∅ (vacuous, region carved empty).

### auto_LiRPA Rejection

| Checkpoint | α=0.95 ε=0.01 | α=0.95 ε=0.02 | α=0.99 ε=0.01 | α=0.99 ε=0.02 |
|------------|---------------|---------------|---------------|---------------|
| epoch_000 | 5/10 (50%) | 2/10 (20%) | 0/10 (0%) | 0/10 (0%) |
| epoch_025 | 10/10 (100%) | 8/10 (80%) | 9/10 (90%) | 4/10 (40%) |
| epoch_050 | 10/10 (100%) | 10/10 (100%) | 9/10 (90%) | 2/10 (20%) |
| epoch_075 | 10/10 (100%) | 9/10 (90%) | 10/10 (100%) | 2/10 (20%) |
| epoch_100 | 10/10 (100%) | 10/10 (100%) | 9/10 (90%) | 2/10 (20%) |

### Marabou Exact Rejection

Format: `rejected / non-empty / timeout`

| Checkpoint | α=0.95 ε=0.01 | α=0.95 ε=0.02 | α=0.99 ε=0.01 | α=0.99 ε=0.02 |
|------------|---------------|---------------|---------------|---------------|
| epoch_000 | 5 / 1 / 4 | 2 / 5 / 3 | 0 / 7 / 3 | 0 / 10 / 0 |
| epoch_025 | 10 / 0 / 0 | 9 / 0 / 1 | 9 / 0 / 1 | 4 / 0 / 6 |
| epoch_050 | 10 / 0 / 0 | 10 / 0 / 0 | 9 / 0 / 1 | 2 / 0 / 8 |
| epoch_075 | 10 / 0 / 0 | 9 / 0 / 1 | 10 / 0 / 0 | 4 / 1 / 5 |
| epoch_100 | 10 / 0 / 0 | 10 / 0 / 0 | 10 / 0 / 0 | 3 / 1 / 6 |

---

## Summary

- **Baseline verified (Marabou, eps=0.01, progress≥25%):** 66/80 = 82.5%
- **NAP α=0.99 genuine (Marabou, eps=0.01, progress≥25%):** 55/80 = 68.8%
- **NAP α=0.99 genuine (Marabou, eps=0.02, progress≥25%):** 32/80 = 40.0%
- **Baseline verified (Marabou, eps=0.02, progress≥25%):** 11/80 = 13.8%
- **NAP α=0.99 achieves 100% genuine verified (auto_LiRPA, eps=0.01)** at epoch_075 and epoch_100
- **Rejection (α=0.95, eps=0.01) saturates at 100%** from epoch_025 onward (both solvers agree)
- **Track B shows stronger late-training improvement** than Track A at eps=0.02 (Marabou α=0.99: 12/20 at epoch_075 vs 8/20 for Track A)

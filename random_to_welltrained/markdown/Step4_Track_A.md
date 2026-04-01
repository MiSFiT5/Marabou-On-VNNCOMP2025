# Step 4 Track A Report: Fixed-Reference Verification

> **Track A** — 70 epochs, 5 checkpoints, 20 fixed unified refs
> Baseline + unary NAP (ALWAYS_ON + ALWAYS_OFF)
> Generated 2026-04-01

**Architecture:** 784 → 7×250 hidden → 10 (fully-connected ReLU, MNIST)
**Total epochs:** 70
**Training:** Standard cross-entropy
**Checkpoints:** epoch_000, epoch_018, epoch_035, epoch_052, epoch_070
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
| epoch_018 | 25% | **16/20** (80%) | **2/20** (10%) |
| epoch_035 | 50% | **17/20** (85%) | **4/20** (20%) |
| epoch_052 | 75% | **18/20** (90%) | **5/20** (25%) |
| epoch_070 | 100% | **18/20** (90%) | **4/20** (20%) |

### NAP alpha=0.95 — Genuine Verified

Format: `genuine/20 (v=vacuous)`

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **1/20** (v=1) [5 eligible] | 0/20 |
| epoch_018 | **13/20** (v=6) | **3/20** (v=1) |
| epoch_035 | **13/20** (v=7) | **6/20** (v=4) |
| epoch_052 | **12/20** (v=8) | **7/20** (v=4) |
| epoch_070 | **12/20** (v=8) | **8/20** (v=4) |

### NAP alpha=0.99 — Genuine Verified

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **1/20** (v=0) [5 eligible] | 0/20 |
| epoch_018 | **16/20** (v=1) | **2/20** (v=0) |
| epoch_035 | **18/20** (v=1) | **6/20** (v=0) |
| epoch_052 | **20/20** (v=0) | **7/20** (v=0) |
| epoch_070 | **20/20** (v=0) | **8/20** (v=0) |

---

## Marabou Exact Verification

`Y = UNSAT (verified)`, `N = SAT (adversarial found)`, `T/o = timeout (300s)`
Only eps ≤ 0.02 were run (larger eps skipped via `--max-epsilon=0.02`).

### Baseline

| Checkpoint | eps | Y | N | T/o | Verified % |
|------------|-----|---|---|-----|-----------|
| epoch_000 | 0.01 | 0 | 0 | 5 | 0.0% (15 mis) |
| epoch_000 | 0.02 | 0 | 0 | 5 | 0.0% (15 mis) |
| epoch_018 | 0.01 | 15 | 0 | 5 | 75.0% |
| epoch_018 | 0.02 | 1 | 0 | 19 | 5.0% |
| epoch_035 | 0.01 | 15 | 0 | 5 | 75.0% |
| epoch_035 | 0.02 | 3 | 0 | 17 | 15.0% |
| epoch_052 | 0.01 | 17 | 0 | 3 | 85.0% |
| epoch_052 | 0.02 | 3 | 2 | 15 | 15.0% |
| epoch_070 | 0.01 | 17 | 0 | 3 | 85.0% |
| epoch_070 | 0.02 | 3 | 0 | 17 | 15.0% |

### NAP alpha=0.95 — Marabou Genuine Verified

Format: `genuine/20 (v=vacuous, u=semantic_unresolved)`

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **3/20** (v=1, u=1) [5 elig] | 0/20 |
| epoch_018 | **9/20** (v=6, u=5) | **3/20** (v=1, u=0) |
| epoch_035 | **12/20** (v=7, u=1) | **9/20** (v=4, u=0) |
| epoch_052 | **7/20** (v=8, u=5) | **14/20** (v=4, u=1) |
| epoch_070 | **8/20** (v=8, u=4) | **12/20** (v=4, u=1) |

### NAP alpha=0.99 — Marabou Genuine Verified

| Checkpoint | eps=0.01 | eps=0.02 |
|------------|----------|----------|
| epoch_000 | **5/20** (v=0, u=0) [5 elig] | 0/20 |
| epoch_018 | **8/20** (v=1, u=8) | **2/20** (v=0, u=0) |
| epoch_035 | **15/20** (v=1, u=3) | **6/20** (v=0, u=0) |
| epoch_052 | **16/20** (v=0, u=4) | **8/20** (v=0, u=0) |
| epoch_070 | **16/20** (v=0, u=3) | **8/20** (v=0, u=0) |

---

## NAP Rejection of Misclassified Samples

10 misclassified refs per checkpoint.
Rejection = B(ref, eps) ∩ NAP = ∅ (vacuous, region carved empty).

### auto_LiRPA Rejection

| Checkpoint | α=0.95 ε=0.01 | α=0.95 ε=0.02 | α=0.99 ε=0.01 | α=0.99 ε=0.02 |
|------------|---------------|---------------|---------------|---------------|
| epoch_000 | 3/10 (30%) | 2/10 (20%) | 0/10 (0%) | 0/10 (0%) |
| epoch_018 | 9/10 (90%) | 6/10 (60%) | 8/10 (80%) | 3/10 (30%) |
| epoch_035 | 10/10 (100%) | 9/10 (90%) | 10/10 (100%) | 4/10 (40%) |
| epoch_052 | 10/10 (100%) | 9/10 (90%) | 10/10 (100%) | 3/10 (30%) |
| epoch_070 | 10/10 (100%) | 9/10 (90%) | 10/10 (100%) | 3/10 (30%) |

### Marabou Exact Rejection

Format: `rejected / non-empty / timeout`

| Checkpoint | α=0.95 ε=0.01 | α=0.95 ε=0.02 | α=0.99 ε=0.01 | α=0.99 ε=0.02 |
|------------|---------------|---------------|---------------|---------------|
| epoch_000 | 3 / 3 / 4 | 2 / 5 / 3 | 0 / 7 / 3 | 0 / 9 / 1 |
| epoch_018 | 10 / 0 / 0 | 7 / 0 / 3 | 8 / 0 / 2 | 3 / 2 / 5 |
| epoch_035 | 10 / 0 / 0 | 9 / 0 / 1 | 10 / 0 / 0 | 3 / 0 / 7 |
| epoch_052 | 10 / 0 / 0 | 10 / 0 / 0 | 10 / 0 / 0 | 3 / 0 / 7 |
| epoch_070 | 10 / 0 / 0 | 9 / 0 / 1 | 10 / 0 / 0 | 3 / 0 / 7 |

---

## Summary

- **Baseline verified (Marabou, eps=0.01, progress≥25%):** 64/80 = 80.0%
- **NAP α=0.99 genuine (Marabou, eps=0.01, progress≥25%):** 55/80 = 68.8%
- **NAP α=0.99 genuine (Marabou, eps=0.02, progress≥25%):** 24/80 = 30.0%
- **Baseline verified (Marabou, eps=0.02, progress≥25%):** 10/80 = 12.5%
- **NAP α=0.99 achieves 100% genuine verified (auto_LiRPA, eps=0.01)** at epoch_052 and epoch_070
- **Rejection saturates at 100%** for α=0.95 eps=0.01 from epoch_035 onward (both solvers agree)

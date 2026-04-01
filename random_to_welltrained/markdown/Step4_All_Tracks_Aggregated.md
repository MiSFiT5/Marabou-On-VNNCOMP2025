# Step 4 — Aggregated Results (Fixed-Reference)

> Generated 2026-04-01
> Experiments: `step4_unified_v2` (auto_LiRPA) + `step4_marabou_v2` (Marabou exact)
> Vacuous-filtered genuine decomposition

- **Tracks:** A (CE, 70 epochs), B (CE, 100 epochs)
- **Checkpoints per track:** 5 (0%, 25%, 50%, 75%, 100%)
- **References per track:** 20 (fixed unified set, multi-class)
- **Epsilon values (Marabou):** 0.01, 0.02 (eps ≥ 0.05 skipped)
- **Epsilon values (auto_LiRPA):** 0.01, 0.02, 0.05, 0.1, 0.2
- **Alpha values:** 0.95, 0.99
- **Rejection refs per checkpoint:** 10 misclassified samples

---

## Baseline Verification

### auto_LiRPA (incomplete)

| Track | Checkpoint | eps=0.01 | eps=0.02 |
|-------|------------|----------|----------|
| A | epoch_000 (0%) | 0/5 elig | 0/5 elig |
| A | epoch_018 (25%) | 16/20 (80%) | 2/20 (10%) |
| A | epoch_035 (50%) | 17/20 (85%) | 4/20 (20%) |
| A | epoch_052 (75%) | 18/20 (90%) | 5/20 (25%) |
| A | epoch_070 (100%) | 18/20 (90%) | 4/20 (20%) |
| B | epoch_000 (0%) | 0/5 elig | 0/5 elig |
| B | epoch_025 (25%) | 14/20 (70%) | 1/20 (5%) |
| B | epoch_050 (50%) | 17/20 (85%) | 6/20 (30%) |
| B | epoch_075 (75%) | 20/20 (100%) | 5/20 (25%) |
| B | epoch_100 (100%) | 20/20 (100%) | 5/20 (25%) |

### Marabou (exact)

| Track | Checkpoint | eps=0.01 Y/N/T | eps=0.02 Y/N/T |
|-------|------------|----------------|----------------|
| A | epoch_000 (0%) | 0/0/5 (15 mis) | 0/0/5 |
| A | epoch_018 (25%) | 15/0/5 (75%) | 1/0/19 (5%) |
| A | epoch_035 (50%) | 15/0/5 (75%) | 3/0/17 (15%) |
| A | epoch_052 (75%) | 17/0/3 (85%) | 3/2/15 (15%) |
| A | epoch_070 (100%) | 17/0/3 (85%) | 3/0/17 (15%) |
| B | epoch_000 (0%) | 0/0/5 (15 mis) | 0/0/5 |
| B | epoch_025 (25%) | 14/0/6 (70%) | 0/0/20 (0%) |
| B | epoch_050 (50%) | 16/0/4 (80%) | 3/1/16 (15%) |
| B | epoch_075 (75%) | 18/0/2 (90%) | 4/0/16 (20%) |
| B | epoch_100 (100%) | 18/0/2 (90%) | 4/0/16 (20%) |

---

## NAP Verification — Genuine Verified

### auto_LiRPA Genuine (out of 20 refs)

#### alpha = 0.95

| Track | Checkpoint | eps=0.01 genuine (v) | eps=0.02 genuine (v) |
|-------|------------|----------------------|----------------------|
| A | epoch_000 | 1 (v=1) | 0 |
| A | epoch_018 | 13 (v=6) | 3 (v=1) |
| A | epoch_035 | 13 (v=7) | 6 (v=4) |
| A | epoch_052 | 12 (v=8) | 7 (v=4) |
| A | epoch_070 | 12 (v=8) | 8 (v=4) |
| B | epoch_000 | 1 (v=1) | 0 |
| B | epoch_025 | 14 (v=6) | 5 (v=2) |
| B | epoch_050 | 11 (v=9) | 6 (v=3) |
| B | epoch_075 | 14 (v=6) | 9 (v=2) |
| B | epoch_100 | 13 (v=7) | 9 (v=2) |

#### alpha = 0.99

| Track | Checkpoint | eps=0.01 genuine (v) | eps=0.02 genuine (v) |
|-------|------------|----------------------|----------------------|
| A | epoch_000 | 1 (v=0) | 0 |
| A | epoch_018 | 16 (v=1) | 2 (v=0) |
| A | epoch_035 | 18 (v=1) | 6 (v=0) |
| A | epoch_052 | 20 (v=0) | 7 (v=0) |
| A | epoch_070 | 20 (v=0) | 8 (v=0) |
| B | epoch_000 | 1 (v=0) | 0 |
| B | epoch_025 | 13 (v=1) | 1 (v=0) |
| B | epoch_050 | 19 (v=0) | 6 (v=0) |
| B | epoch_075 | 20 (v=0) | 9 (v=0) |
| B | epoch_100 | 20 (v=0) | 9 (v=0) |

### Marabou Genuine (out of 20 refs)

#### alpha = 0.95

| Track | Checkpoint | eps=0.01 genuine (v/u) | eps=0.02 genuine (v/u) |
|-------|------------|------------------------|------------------------|
| A | epoch_000 | 3 (v=1, u=1) | 0 |
| A | epoch_018 | 9 (v=6, u=5) | 3 (v=1, u=0) |
| A | epoch_035 | 12 (v=7, u=1) | 9 (v=4, u=0) |
| A | epoch_052 | 7 (v=8, u=5) | 14 (v=4, u=1) |
| A | epoch_070 | 8 (v=8, u=4) | 12 (v=4, u=1) |
| B | epoch_000 | 3 (v=1, u=1) | 0 |
| B | epoch_025 | 9 (v=6, u=4) | 6 (v=2, u=0) |
| B | epoch_050 | 10 (v=9, u=1) | 10 (v=3, u=3) |
| B | epoch_075 | 9 (v=7, u=4) | 16 (v=2, u=2) |
| B | epoch_100 | 10 (v=7, u=3) | 15 (v=2, u=2) |

#### alpha = 0.99

| Track | Checkpoint | eps=0.01 genuine (v/u) | eps=0.02 genuine (v/u) |
|-------|------------|------------------------|------------------------|
| A | epoch_000 | 5 (v=0, u=0) | 0 |
| A | epoch_018 | 8 (v=1, u=8) | 2 (v=0, u=0) |
| A | epoch_035 | 15 (v=1, u=3) | 6 (v=0, u=0) |
| A | epoch_052 | 16 (v=0, u=4) | 8 (v=0, u=0) |
| A | epoch_070 | 16 (v=0, u=3) | 8 (v=0, u=0) |
| B | epoch_000 | 5 (v=0, u=0) | 0 |
| B | epoch_025 | 7 (v=1, u=7) | 1 (v=0, u=0) |
| B | epoch_050 | 16 (v=0, u=3) | 8 (v=0, u=0) |
| B | epoch_075 | 16 (v=0, u=4) | 12 (v=0, u=0) |
| B | epoch_100 | 16 (v=0, u=4) | 11 (v=0, u=0) |

---

## Vacuous Rate Summary (auto_LiRPA, progress ≥ 25%)

| Alpha | eps=0.01 | eps=0.02 |
|-------|----------|----------|
| 0.95 | 40.6% (52/128 NAP-verified) | 21.1% (16/76 NAP-verified) |
| 0.99 | 1.9% (3/158 NAP-verified) | 0% (0/52 NAP-verified) |

---

## Cross-Solver Comparison (progress ≥ 25%)

Mean verified/genuine rates across both tracks, checkpoints with progress ≥ 25%.

### Verified Rate (total, including vacuous for NAP)

| Method | Solver | eps=0.01 | eps=0.02 |
|--------|--------|----------|----------|
| Baseline | auto_LiRPA | 86.2% | 17.5% |
| Baseline | Marabou | 81.2% | 12.5% |
| NAP α=0.95 | auto_LiRPA | 98.8% | 41.2% |
| NAP α=0.95 | Marabou | 97.5% | 73.1% |
| NAP α=0.99 | auto_LiRPA | 91.2% | 33.1% |
| NAP α=0.99 | Marabou | 91.2% | 36.2% |

### Genuine Verified Rate

| Method | Solver | eps=0.01 | eps=0.02 |
|--------|--------|----------|----------|
| Baseline | auto_LiRPA | 86.2% | 17.5% |
| Baseline | Marabou | 81.2% | 12.5% |
| NAP α=0.95 | auto_LiRPA | 63.1% | 30.6% |
| NAP α=0.95 | Marabou | 47.5% | 51.9% |
| NAP α=0.99 | auto_LiRPA | 85.0% | 28.1% |
| NAP α=0.99 | Marabou | 66.2% | 30.0% |

**Key observation:** At eps=0.01, Marabou genuine for NAP is **lower** than auto_LiRPA genuine. This is partly because Marabou has `semantic_unresolved` cases (verified by Marabou but vacuous check timed out), which auto_LiRPA does not have. At eps=0.02, Marabou α=0.95 genuine is **higher** than auto_LiRPA — Marabou as a complete solver can verify cases that auto_LiRPA's incomplete bounds cannot.

---

## Rejection Summary (Marabou Exact, all checkpoints)

### Aggregated by (alpha, epsilon) across both tracks

| Alpha | Epsilon | Rejected | Non-empty | Timeout | Rejection Rate |
|-------|---------|----------|-----------|---------|---------------|
| 0.95 | 0.01 | 88 | 4 | 8 | 88.0% |
| 0.95 | 0.02 | 77 | 10 | 13 | 77.0% |
| 0.99 | 0.01 | 76 | 14 | 10 | 76.0% |
| 0.99 | 0.02 | 25 | 23 | 52 | 25.0% |

### Aggregated excluding epoch_000

| Alpha | Epsilon | Rejected | Non-empty | Timeout | Rejection Rate |
|-------|---------|----------|-----------|---------|---------------|
| 0.95 | 0.01 | 80 | 0 | 0 | 100.0% |
| 0.95 | 0.02 | 73 | 0 | 7 | 91.2% |
| 0.99 | 0.01 | 76 | 0 | 4 | 95.0% |
| 0.99 | 0.02 | 22 | 3 | 55 | 27.5% |

---

## Aggregated Totals

### auto_LiRPA (step4_unified_v2, all eps, both tracks)

| Metric | Baseline (500 tasks) | NAP (1000 tasks) |
|--------|---------------------|------------------|
| Verified | 173 | 384 |
| Unknown | 177 | 466 |
| Misclassified | 150 | 150 |
| Vacuous | — | 75 |
| **Genuine verified** | **173** | **309** |

### Marabou (step4_marabou_v2, eps ≤ 0.02 only, both tracks)

| Metric | Baseline (200 tasks) | NAP (400 tasks) |
|--------|---------------------|------------------|
| Verified (Y) | 130 | 320 |
| Adversarial (N) | 6 | 1 |
| Timeout | 34 | 49 |
| Misclassified | 30 | 30 |
| Skipped (eps>0.02) | 0 | 0 |
| Vacuous | — | 39 |
| Semantic unresolved | — | 49 |
| **Genuine verified** | **130** | **232** |

---

## Comparison with Step 3

Step 3 used per-checkpoint refs (10 per checkpoint), while Step 4 uses fixed refs (20 per track).
These numbers are **not directly comparable** due to different ref pools, denominators, and class coverage.

| Aspect | Step 3 (Marabou) | Step 4 (Marabou, eps≤0.02) |
|--------|-----------------|---------------------------|
| Refs | 10 per checkpoint (per-ckpt) | 20 per track (fixed) |
| BL timeout rate | 83.8% (419/500) | 17.0% (34/200) |
| NAP genuine rate | 21.3% (213/1000) | 58.0% (232/400) |
| epoch_000 NAP α=0.99 eps=0.01 | **100%** (10/10) | **25%** (5/20) |

The dramatic difference at epoch_000 (100% → 25%) is explained by:
1. Step 3 refs at epoch_000 are 10 digit-9 samples specifically chosen because epoch_000 classifies them correctly
2. Step 4 fixed refs include 15/20 that epoch_000 misclassifies (only 5 eligible)
3. Step 3's 100% is a **solver-efficiency artifact**: NAP constraints help Marabou solve within timeout, but the baseline is likely also robust at eps=0.01 (just can't prove it in 300s)

The much lower baseline timeout rate in Step 4 (17% vs 84%) is because Step 4 only runs eps ≤ 0.02, while Step 3 included eps up to 0.2 (which almost always timeout).

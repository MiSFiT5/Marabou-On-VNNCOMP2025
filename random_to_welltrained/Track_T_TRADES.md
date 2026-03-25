# Track T (TRADES) Report: Random-to-Well-Trained

> **Track T** — TRADES adversarial training, 100 epochs, 5 checkpoints  
> Baseline + unary NAP (ALWAYS_ON + ALWAYS_OFF)  
> Solver: Marabou (300s timeout)  
> Generated 2026-03-25

**Architecture:** 784 → 7×250 → 10 (fully-connected ReLU MLP, MNIST)  
**Training:** TRADES adversarial training (Robust + Natural loss)  
**Checkpoints:** epoch_000 (0%), epoch_025 (25%), epoch_050 (50%), epoch_075 (75%), epoch_100 (100%)  
**References:** 10 per checkpoint (first 10 correctly classified test samples, mixed classes)  
**Note:** epoch_000 is the **same random initialization** as Track A/B

**Total tasks:** 750 (250 baseline + 500 NAP at α=0.95, 0.99)

### Task Count

| Config | Count | Note |
|--------|-------|------|
| Baseline | 5 ckpt × 10 refs × 5 ε = 250 | |
| NAP α=0.95 | 5 × 10 × 5 = 250 | |
| NAP α=0.99 | 5 × 10 × 5 = 250 | |
| **Total** | **750** | Single track (T) only |

---

## Baseline Verification

`Y = UNSAT (verified)`, `N = SAT (adversarial found)`, `T/o = timeout`

| Checkpoint | eps | Y | N | T/o | Verified % |
|------------|-----|---|---|-----|-----------|
| epoch_000 | 0.01 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.02 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_025 | 0.01 | 10 | 0 | 0 | 100.0% |
| epoch_025 | 0.02 | 8 | 0 | 2 | 80.0% |
| epoch_025 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_025 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_025 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_050 | 0.01 | 10 | 0 | 0 | 100.0% |
| epoch_050 | 0.02 | 7 | 0 | 3 | 70.0% |
| epoch_050 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_050 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_050 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_075 | 0.01 | 9 | 0 | 1 | 90.0% |
| epoch_075 | 0.02 | 5 | 1 | 4 | 50.0% |
| epoch_075 | 0.05 | 0 | 2 | 8 | 0.0% |
| epoch_075 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_075 | 0.2 | 0 | 1 | 9 | 0.0% |
| epoch_100 | 0.01 | 9 | 1 | 0 | 90.0% |
| epoch_100 | 0.02 | 5 | 0 | 5 | 50.0% |
| epoch_100 | 0.05 | 0 | 1 | 9 | 0.0% |
| epoch_100 | 0.1 | 0 | 1 | 9 | 0.0% |
| epoch_100 | 0.2 | 0 | 1 | 9 | 0.0% |

**Key observation:** TRADES baseline is already very strong at ε=0.01 (90–100% verified from epoch_025 onwards).
At ε=0.02, it verifies 50–80%. This is much stronger than the standard CE baseline (Track A/B), which only reaches 60–80% at ε=0.01.

---

## NAP Verification — Genuine Verified

Format: `genuine/10 (v=vacuous)`. Bold = genuine > 0.

### α = 0.95

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | **6/10** (v=4) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **3/10** (v=7) | **6/10** (v=4) | 0/10 (v=1) | 0/10 | 0/10 |
| epoch_050 | **4/10** (v=6) | **6/10** (v=2) | 0/10 | 0/10 | 0/10 |
| epoch_075 | **5/10** (v=5) | **6/10** (v=4) | 0/10 (v=1) | 0/10 | 0/10 |
| epoch_100 | **5/10** (v=5) | **7/10** (v=3) | 0/10 (v=2) | 0/10 | 0/10 |

### α = 0.99

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | **10/10** (v=0) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **9/10** (v=1) | **7/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_050 | **9/10** (v=1) | **6/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_075 | **8/10** (v=2) | **6/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_100 | **8/10** (v=2) | **5/10** (v=1) | 0/10 | 0/10 | 0/10 |

---

## Vacuous Rate

| Alpha | eps=0.01 | eps=0.02 | eps=0.05 |
|-------|----------|----------|----------|
| 0.95 | 54% (27/50) | 26% (13/50) | 8% (4/50) |
| 0.99 | 12% (6/50) | 8% (4/50) | 0% (0/50) |

**Note:** TRADES vacuous rates at α=0.95 are high (40–70% at ε=0.01 for trained checkpoints),
much higher than standard CE training (30–50%). This suggests TRADES-shaped decision boundaries
don't align well with NAP rules mined from clean forward passes.

---

## NAP Rules Count

Total rules across all layer pairs (from `summary.json`)

| Checkpoint | α=0.95 | α=0.99 |
|------------|--------|--------|
| epoch_000 | 3,898,464 | 3,438,415 |
| epoch_025 | 3,580,588 | 2,557,543 |
| epoch_050 | 3,634,934 | 2,590,535 |
| epoch_075 | 3,682,951 | 2,696,753 |
| epoch_100 | 3,659,528 | 2,677,761 |

---

## Comparison: TRADES vs Standard CE (Track A/B)

### Baseline Verified Rate at ε=0.01

| Track | epoch_000 | ~25% | ~50% | ~75% | ~100% |
|-------|-----------|------|------|------|-------|
| A (CE) | 0% | 50% | 60% | 60% | 60% |
| B (CE) | 0% | 50% | 50% | 80% | 80% |
| T (TRADES) | 0% | 100% | 100% | 90% | 90% |

### NAP Genuine Rate at ε=0.01 (α=0.95)

| Track | epoch_000 | ~25% | ~50% | ~75% | ~100% |
|-------|-----------|------|------|------|-------|
| A (CE) | 60% | 70% | 70% | 50% | 50% |
| B (CE) | 60% | 50% | 40% | 70% | 70% |
| T (TRADES) | 60% | 30% | 40% | 50% | 50% |

### Max Verifiable Epsilon

| Track | Checkpoint | BL max ε | NAP max ε (best α) |
|-------|------------|----------|---------------------|
| T | epoch_000 | — | 0.01 |
| T | epoch_025 | 0.02 | 0.02 |
| T | epoch_050 | 0.02 | 0.02 |
| T | epoch_075 | 0.02 | 0.02 |
| T | epoch_100 | 0.02 | 0.02 |

---

## Summary

- **Baseline verified:** 63/250 (25.2%)
- **NAP genuine verified:** 116/500 (23.2%)
- **NAP vacuous:** 54/500 (10.8%)

### Key Findings for TRADES

1. **TRADES baseline is much stronger than CE baseline**: 90–100% verified at ε=0.01 (vs 50–80% for CE)
2. **NAP adds marginal value**: At ε=0.01, NAP genuine ≤ baseline because high vacuous rate eats into the count
3. **NAP still helps at ε=0.02**: Genuine verified reaches 60–70% where baseline is 50–80%
4. **Very high vacuous rate at α=0.95**: 40–70% at ε=0.01 for trained checkpoints, suggesting TRADES activation patterns are less stable than CE patterns
5. **NAP rules decrease under TRADES**: Total rules plateau lower (~3.5M at α=0.95) vs CE (~4.5M), indicating TRADES produces fewer deterministic activations
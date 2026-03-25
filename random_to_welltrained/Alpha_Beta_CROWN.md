# alpha-beta-CROWN Report: Random-to-Well-Trained

> alpha-beta-CROWN (bound propagation + Branch-and-Bound)  
> Baseline + unary NAP via manual_cuts  
> Generated 2026-03-25

**Solver:** alpha-beta-CROWN  
**Timeout:** 120s per task  
**NAP mechanism:** `manual_cuts` injected into BaB  
**Config fixes applied:** `bab_cut: true`, `number_cuts: 10000`

## Experiment Runs

| Run | PGD | NAP cuts in BaB | Tasks | Purpose |
|-----|-----|-----------------|-------|---------|
| `step3_abcrown` (original) | Enabled | Yes (after fix) | 1500 | Initial run; PGD bug discovered |
| `step3_abcrown_nopgd` (Approach A) | **Disabled** | Yes | 1000 NAP + 500 BL reused | Clean NAP results |
| `step3_abcrown_pgdfilter` (Approach B) | Enabled | Yes | 1000 NAP | Confirm PGD bug with saved adversarials |

---

## The PGD Bug

### Problem

alpha-beta-CROWN's verification pipeline:
```
Step 1: PGD attack (find adversarial)     <- Does NOT load manual_cuts
Step 2: BaB + CROWN (prove safety)        <- Does load manual_cuts
```

PGD runs **before** BaB and **ignores** NAP constraints. Any adversarial found by PGD
may lie outside the NAP region, making it invalid for NAP-augmented verification.

### Evidence

| Metric | Original (PGD on) | Approach A (PGD off) | Approach B (PGD on, examined) |
|--------|-------------------|---------------------|------------------------------|
| SAT (N) | 514 | **0** | 514 |
| UNSAT (Y) | 186 | 193 | 186 |
| Timeout | 300 | 807 | 300 |

**Key finding:** 514 NAP SAT results in the original run were ALL from PGD finding
adversarials outside the NAP region. With PGD disabled, **0 SAT** — BaB with NAP cuts
cannot find any adversarial inside the NAP-constrained search space.

### What Changed: PGD-on vs PGD-off (per task)

| Original (PGD on) | nopgd (PGD off) | Count |
|-------------------|-----------------|-------|
| N | T/o | 504 |
| N | Y | 10 |
| Y | T/o | 3 |
| (unchanged) | (unchanged) | 483 |

- **514 tasks flipped from N (SAT) to other**: PGD adversarials were invalid
- **10 tasks flipped N -> Y**: PGD incorrectly said unsafe, BaB proves safe
- **504 tasks flipped N -> T/o**: PGD shortcut removed, BaB cannot resolve in time

### Additional Configuration Bugs Fixed

| Bug | Default | Impact | Fix |
|-----|---------|--------|-----|
| `number_cuts: 50` | alpha-beta-CROWN default | Truncated 1000+ NAP rules to 50 shallow-layer rules | Set `number_cuts: 10000` |
| `enabled: true` | Wrong parameter name | `bab_cut` remained `false` despite YAML | Explicitly set `bab_cut: true` |

---

## Clean Results: Approach A (PGD Disabled)

These are the authoritative alpha-beta-CROWN NAP results.

### Baseline (reused from original run)

#### Track A

| Checkpoint | eps | Y | N | T/o | Verified % |
|------------|-----|---|---|-----|-----------|
| epoch_000 | 0.01 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.02 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_018 | 0.01 | 8 | 1 | 1 | 80.0% |
| epoch_018 | 0.02 | 1 | 3 | 6 | 10.0% |
| epoch_018 | 0.05 | 0 | 9 | 1 | 0.0% |
| epoch_018 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_018 | 0.2 | 0 | 10 | 0 | 0.0% |
| epoch_035 | 0.01 | 9 | 0 | 1 | 90.0% |
| epoch_035 | 0.02 | 3 | 3 | 4 | 30.0% |
| epoch_035 | 0.05 | 0 | 8 | 2 | 0.0% |
| epoch_035 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_035 | 0.2 | 0 | 10 | 0 | 0.0% |
| epoch_052 | 0.01 | 7 | 2 | 1 | 70.0% |
| epoch_052 | 0.02 | 3 | 3 | 4 | 30.0% |
| epoch_052 | 0.05 | 0 | 9 | 1 | 0.0% |
| epoch_052 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_052 | 0.2 | 0 | 10 | 0 | 0.0% |
| epoch_070 | 0.01 | 7 | 1 | 2 | 70.0% |
| epoch_070 | 0.02 | 3 | 3 | 4 | 30.0% |
| epoch_070 | 0.05 | 0 | 9 | 1 | 0.0% |
| epoch_070 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_070 | 0.2 | 0 | 10 | 0 | 0.0% |

#### Track B

| Checkpoint | eps | Y | N | T/o | Verified % |
|------------|-----|---|---|-----|-----------|
| epoch_000 | 0.01 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.02 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_025 | 0.01 | 7 | 1 | 2 | 70.0% |
| epoch_025 | 0.02 | 2 | 4 | 4 | 20.0% |
| epoch_025 | 0.05 | 0 | 9 | 1 | 0.0% |
| epoch_025 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_025 | 0.2 | 0 | 10 | 0 | 0.0% |
| epoch_050 | 0.01 | 6 | 2 | 2 | 60.0% |
| epoch_050 | 0.02 | 3 | 3 | 4 | 30.0% |
| epoch_050 | 0.05 | 0 | 9 | 1 | 0.0% |
| epoch_050 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_050 | 0.2 | 0 | 10 | 0 | 0.0% |
| epoch_075 | 0.01 | 10 | 0 | 0 | 100.0% |
| epoch_075 | 0.02 | 4 | 2 | 4 | 40.0% |
| epoch_075 | 0.05 | 0 | 7 | 3 | 0.0% |
| epoch_075 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_075 | 0.2 | 0 | 10 | 0 | 0.0% |
| epoch_100 | 0.01 | 10 | 0 | 0 | 100.0% |
| epoch_100 | 0.02 | 4 | 2 | 4 | 40.0% |
| epoch_100 | 0.05 | 0 | 7 | 3 | 0.0% |
| epoch_100 | 0.1 | 0 | 10 | 0 | 0.0% |
| epoch_100 | 0.2 | 0 | 10 | 0 | 0.0% |

### NAP Genuine Verified

Format: `genuine/10 (v=vacuous)`. Bold = genuine > 0.

#### Track A

##### alpha = 0.95

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 (v=1) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_018 | **7/10** (v=3) | **1/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_035 | **6/10** (v=3) | **3/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_052 | **4/10** (v=4) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_070 | **4/10** (v=5) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |

##### alpha = 0.99

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_018 | **8/10** (v=1) | **1/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_035 | **8/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_052 | **7/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_070 | **7/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |

#### Track B

##### alpha = 0.95

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **5/10** (v=4) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_050 | **3/10** (v=5) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_075 | **7/10** (v=3) | **3/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_100 | **7/10** (v=3) | **3/10** (v=1) | 0/10 | 0/10 | 0/10 |

##### alpha = 0.99

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **6/10** (v=2) | **2/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_050 | **7/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_075 | **10/10** (v=0) | **4/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_100 | **10/10** (v=0) | **4/10** (v=0) | 0/10 | 0/10 | 0/10 |

---

## Timing Analysis

### UNSAT (verified) cases

| Config | Count | Median (s) | Mean (s) | Min (s) | Max (s) |
|--------|-------|-----------|---------|---------|---------|
| Baseline | 87 | 8.3 | 10.4 | 6.0 | 42.6 |
| NAP (nopgd) | 193 | 6.9 | 13.0 | 5.0 | 120.7 |

### SAT (adversarial found) cases

| Config | Count | Median (s) | Mean (s) |
|--------|-------|-----------|---------|
| Baseline | 257 | 5.5 | 5.8 |
| NAP (nopgd) | 0 | — | — |

---

## Comparison with Marabou

### NAP Genuine Verified: Marabou vs alpha-beta-CROWN

Cases where the two solvers differ significantly (|diff| >= 2)

| Track | Checkpoint | eps | alpha | Marabou | abcrown | Diff |
|-------|------------|-----|-------|---------|---------|------|
| A | epoch_000 | 0.01 | 0.95 | 6 | 0 | -6 |
| A | epoch_000 | 0.01 | 0.99 | 10 | 0 | -10 |
| A | epoch_018 | 0.01 | 0.99 | 6 | 8 | +2 |
| A | epoch_035 | 0.01 | 0.99 | 6 | 8 | +2 |
| A | epoch_052 | 0.01 | 0.99 | 9 | 7 | -2 |
| A | epoch_052 | 0.02 | 0.95 | 5 | 2 | -3 |
| A | epoch_070 | 0.02 | 0.95 | 5 | 2 | -3 |
| B | epoch_000 | 0.01 | 0.95 | 6 | 0 | -6 |
| B | epoch_000 | 0.01 | 0.99 | 10 | 0 | -10 |
| B | epoch_025 | 0.01 | 0.99 | 4 | 6 | +2 |
| B | epoch_025 | 0.02 | 0.99 | 0 | 2 | +2 |
| B | epoch_050 | 0.02 | 0.95 | 6 | 2 | -4 |
| B | epoch_075 | 0.02 | 0.95 | 8 | 3 | -5 |
| B | epoch_075 | 0.02 | 0.99 | 6 | 4 | -2 |
| B | epoch_075 | 0.05 | 0.95 | 6 | 0 | -6 |
| B | epoch_075 | 0.1 | 0.95 | 2 | 0 | -2 |
| B | epoch_100 | 0.02 | 0.95 | 8 | 3 | -5 |
| B | epoch_100 | 0.05 | 0.95 | 2 | 0 | -2 |

### Marabou Verifies but alpha-beta-CROWN Cannot

| Track | Checkpoint | eps | alpha | Marabou genuine |
|-------|------------|-----|-------|----------------|
| A | epoch_000 | 0.01 | 0.95 | 6 |
| A | epoch_000 | 0.01 | 0.99 | 10 |
| A | epoch_052 | 0.05 | 0.95 | 1 |
| B | epoch_000 | 0.01 | 0.95 | 6 |
| B | epoch_000 | 0.01 | 0.99 | 10 |
| B | epoch_050 | 0.05 | 0.95 | 1 |
| B | epoch_075 | 0.05 | 0.95 | 6 |
| B | epoch_075 | 0.1 | 0.95 | 2 |
| B | epoch_075 | 0.2 | 0.95 | 1 |
| B | epoch_100 | 0.05 | 0.95 | 2 |
| | | | **Total** | **45** |

Marabou verifies 45 refs that alpha-beta-CROWN cannot, primarily at:
- **epoch_000** (random init): Marabou handles unstructured weights; abcrown's bound propagation is too loose
- **Large eps (0.05-0.2)**: Marabou's LP solver handles wide search spaces; abcrown's BaB times out

---

## Summary

### Aggregate Totals

| Metric | Baseline (500) | NAP nopgd (1000) |
|--------|---------------|-----------------|
| Verified | 87 (17.4%) | 193 (19.3%) |
| Genuine verified | 87 | 147 (14.7%) |
| Vacuous | — | 46 |
| SAT | 257 | **0** |
| Timeout | 156 | 807 |

### Key Takeaways

1. **PGD bug is real and significant**: 514 false SAT when PGD is on; 0 SAT when off
2. **alpha-beta-CROWN is 4.8x faster** than Marabou for NAP UNSAT cases (median 6.9s vs 33.3s)
3. **Marabou is more powerful**: verifies 213 genuine vs 147 for alpha-beta-CROWN; handles epoch_000 and large eps
4. **Two solvers are complementary**: abcrown for speed at small eps, Marabou for coverage at large eps and unstructured networks
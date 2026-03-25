# Track B Report: Random-to-Well-Trained

> **Track B** — 100 epochs, 5 checkpoints  
> Baseline + unary NAP (ALWAYS_ON + ALWAYS_OFF)  
> Generated 2026-03-25

**Architecture:** 784 → hidden → 10 (fully-connected, MNIST)  
**Total epochs:** 100  
**Training:** Standard cross-entropy  
**Checkpoints:** epoch_000, epoch_025, epoch_050, epoch_075, epoch_100  
**References:** 10 per checkpoint (first 10 correctly classified test samples, mixed classes)

## Training Curve

| Epoch | Progress | Train Loss | Train Acc | Val Loss | Val Acc |
|-------|----------|-----------|-----------|----------|---------|
| 0 | 0% | — | — | 2.3034 | 10.1% |
| 25 | 25% | 0.0128 | 99.6% | 0.1202 | 97.4% |
| 50 | 50% | 0.0053 | 99.9% | 0.1408 | 97.9% |
| 75 | 75% | 0.0000 | 100.0% | 0.1204 | 98.3% |
| 100 | 100% | 0.0000 | 100.0% | 0.1534 | 98.3% |

## NAP Rules

| Checkpoint | alpha=0.95 (mean/class) | alpha=0.99 (mean/class) |
|------------|-------------------------|-------------------------|
| epoch_000 | 1183 (total: 1183) | 1045 (total: 1045) |
| epoch_025 | 1206 (total: 8441) | 940 (total: 6582) |
| epoch_050 | 1303 (total: 9122) | 1069 (total: 7481) |
| epoch_075 | 1371 (total: 8224) | 1165 (total: 6988) |
| epoch_100 | 1366 (total: 8199) | 1162 (total: 6970) |

---

## Baseline Verification (Marabou)

| Checkpoint | eps | Y | N | T/o | Verified % |
|------------|-----|---|---|-----|-----------|
| epoch_000 | 0.01 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.02 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_025 | 0.01 | 5 | 0 | 5 | 50.0% |
| epoch_025 | 0.02 | 0 | 0 | 10 | 0.0% |
| epoch_025 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_025 | 0.1 | 0 | 2 | 8 | 0.0% |
| epoch_025 | 0.2 | 0 | 2 | 8 | 0.0% |
| epoch_050 | 0.01 | 5 | 1 | 4 | 50.0% |
| epoch_050 | 0.02 | 1 | 0 | 9 | 10.0% |
| epoch_050 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_050 | 0.1 | 0 | 1 | 9 | 0.0% |
| epoch_050 | 0.2 | 0 | 3 | 7 | 0.0% |
| epoch_075 | 0.01 | 8 | 0 | 2 | 80.0% |
| epoch_075 | 0.02 | 3 | 0 | 7 | 30.0% |
| epoch_075 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_075 | 0.1 | 0 | 2 | 8 | 0.0% |
| epoch_075 | 0.2 | 0 | 2 | 8 | 0.0% |
| epoch_100 | 0.01 | 8 | 0 | 2 | 80.0% |
| epoch_100 | 0.02 | 3 | 0 | 7 | 30.0% |
| epoch_100 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_100 | 0.1 | 0 | 1 | 9 | 0.0% |
| epoch_100 | 0.2 | 0 | 2 | 8 | 0.0% |

---

## NAP Verification (Marabou) — Genuine Verified

Format: `genuine/10 (vacuous=V)`. Bold = genuine > 0.

### alpha = 0.95

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | **6/10** (v=4) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **5/10** (v=4) | **2/10** (v=2) | 0/10 | 0/10 | 0/10 |
| epoch_050 | **4/10** (v=6) | **6/10** (v=3) | **1/10** (v=0) | 0/10 | 0/10 |
| epoch_075 | **7/10** (v=3) | **8/10** (v=1) | **6/10** (v=0) | **2/10** (v=0) | **1/10** (v=0) |
| epoch_100 | **7/10** (v=3) | **8/10** (v=1) | **2/10** (v=0) | 0/10 | 0/10 |

### alpha = 0.99

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | **10/10** (v=0) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **4/10** (v=2) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_050 | **8/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_075 | **10/10** (v=0) | **6/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_100 | **10/10** (v=0) | **4/10** (v=0) | 0/10 | 0/10 | 0/10 |

---

## alpha-beta-CROWN (nopgd) — Genuine Verified

### alpha = 0.95

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **5/10** (v=4) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_050 | **3/10** (v=5) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_075 | **7/10** (v=3) | **3/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_100 | **7/10** (v=3) | **3/10** (v=1) | 0/10 | 0/10 | 0/10 |

### alpha = 0.99

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_025 | **6/10** (v=2) | **2/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_050 | **7/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_075 | **10/10** (v=0) | **4/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_100 | **10/10** (v=0) | **4/10** (v=0) | 0/10 | 0/10 | 0/10 |

---

## Detailed Per-Reference Results (Interesting Cases)

Cases where NAP genuinely verifies but baseline fails.

| Checkpoint | Ref | Label | eps | alpha | NAP | BL at same eps | Time (s) |
|------------|-----|-------|-----|-------|-----|---------------|----------|
| epoch_025 | ref3 | 0 | 0.02 | 0.95 | Y | T/o | 40.1 |
| epoch_025 | ref9 | 9 | 0.02 | 0.95 | Y | T/o | 37.7 |
| epoch_050 | ref3 | 0 | 0.05 | 0.95 | Y | T/o | 519.4 |
| epoch_050 | ref0 | 7 | 0.02 | 0.95 | Y | T/o | 36.3 |
| epoch_050 | ref1 | 2 | 0.02 | 0.99 | Y | T/o | 21.6 |
| epoch_050 | ref3 | 0 | 0.02 | 0.95 | Y | Y | 33.4 |
| epoch_050 | ref3 | 0 | 0.02 | 0.99 | Y | Y | 33.3 |
| epoch_050 | ref5 | 1 | 0.02 | 0.95 | Y | T/o | 1307.6 |
| epoch_050 | ref9 | 9 | 0.02 | 0.95 | Y | T/o | 31.3 |
| epoch_050 | ref9 | 9 | 0.02 | 0.99 | Y | T/o | 31.1 |
| epoch_075 | ref5 | 1 | 0.2 | 0.95 | Y | T/o | 1791.7 |
| epoch_075 | ref2 | 1 | 0.1 | 0.95 | Y | N | 1213.0 |
| epoch_075 | ref5 | 1 | 0.1 | 0.95 | Y | T/o | 1403.5 |
| epoch_075 | ref0 | 7 | 0.05 | 0.95 | Y | T/o | 1277.9 |
| epoch_075 | ref2 | 1 | 0.05 | 0.95 | Y | T/o | 699.9 |
| epoch_075 | ref3 | 0 | 0.05 | 0.95 | Y | T/o | 2390.5 |
| epoch_075 | ref4 | 4 | 0.05 | 0.95 | Y | T/o | 710.1 |
| epoch_075 | ref5 | 1 | 0.05 | 0.95 | Y | T/o | 1051.8 |
| epoch_075 | ref9 | 0 | 0.05 | 0.95 | Y | T/o | 686.7 |
| epoch_075 | ref0 | 7 | 0.02 | 0.95 | Y | T/o | 194.0 |

---

## Summary

- **Baseline verified:** 33/250 (13.2%)
- **NAP genuine verified:** 120/500 (24.0%)
- **NAP vacuous:** 30/500 (6.0%)
- **Max NAP-verified epsilon:** 0.2 at epoch_075 (alpha=0.95, 1/10 genuine)
- **Max BL-verified epsilon:** 0.02 at epoch_050 (1/10)

# Track A Report: Random-to-Well-Trained

> **Track A** — 70 epochs, 5 checkpoints  
> Baseline + unary NAP (ALWAYS_ON + ALWAYS_OFF)  
> Generated 2026-03-25

**Architecture:** 784 → hidden → 10 (fully-connected, MNIST)  
**Total epochs:** 70  
**Training:** Standard cross-entropy  
**Checkpoints:** epoch_000, epoch_018, epoch_035, epoch_052, epoch_070  
**References:** 10 per checkpoint (first 10 correctly classified test samples, mixed classes)

## Training Curve

| Epoch | Progress | Train Loss | Train Acc | Val Loss | Val Acc |
|-------|----------|-----------|-----------|----------|---------|
| 0 | 0% | — | — | 2.3034 | 10.1% |
| 18 | 25% | 0.0167 | 99.5% | 0.1234 | 97.6% |
| 35 | 50% | 0.0076 | 99.8% | 0.1234 | 97.8% |
| 52 | 75% | 0.0002 | 100.0% | 0.1255 | 98.1% |
| 70 | 100% | 0.0000 | 100.0% | 0.1409 | 98.1% |

## NAP Rules

| Checkpoint | alpha=0.95 (mean/class) | alpha=0.99 (mean/class) |
|------------|-------------------------|-------------------------|
| epoch_000 | 1183 (total: 1183) | 1045 (total: 1045) |
| epoch_018 | 1146 (total: 8023) | 898 (total: 6287) |
| epoch_035 | 1260 (total: 7563) | 988 (total: 5925) |
| epoch_052 | 1315 (total: 9207) | 1098 (total: 7689) |
| epoch_070 | 1315 (total: 9202) | 1098 (total: 7686) |

---

## Baseline Verification (Marabou)

| Checkpoint | eps | Y | N | T/o | Verified % |
|------------|-----|---|---|-----|-----------|
| epoch_000 | 0.01 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.02 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_000 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_018 | 0.01 | 5 | 0 | 5 | 50.0% |
| epoch_018 | 0.02 | 0 | 0 | 10 | 0.0% |
| epoch_018 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_018 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_018 | 0.2 | 0 | 0 | 10 | 0.0% |
| epoch_035 | 0.01 | 6 | 0 | 4 | 60.0% |
| epoch_035 | 0.02 | 2 | 0 | 8 | 20.0% |
| epoch_035 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_035 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_035 | 0.2 | 0 | 1 | 9 | 0.0% |
| epoch_052 | 0.01 | 6 | 0 | 4 | 60.0% |
| epoch_052 | 0.02 | 1 | 0 | 9 | 10.0% |
| epoch_052 | 0.05 | 0 | 0 | 10 | 0.0% |
| epoch_052 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_052 | 0.2 | 0 | 2 | 8 | 0.0% |
| epoch_070 | 0.01 | 6 | 0 | 4 | 60.0% |
| epoch_070 | 0.02 | 1 | 0 | 9 | 10.0% |
| epoch_070 | 0.05 | 0 | 1 | 9 | 0.0% |
| epoch_070 | 0.1 | 0 | 0 | 10 | 0.0% |
| epoch_070 | 0.2 | 0 | 1 | 9 | 0.0% |

---

## NAP Verification (Marabou) — Genuine Verified

Format: `genuine/10 (vacuous=V)`. Bold = genuine > 0.

### alpha = 0.95

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | **6/10** (v=4) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_018 | **7/10** (v=3) | **1/10** (v=2) | 0/10 | 0/10 | 0/10 |
| epoch_035 | **7/10** (v=3) | **3/10** (v=2) | 0/10 | 0/10 | 0/10 |
| epoch_052 | **5/10** (v=5) | **5/10** (v=3) | **1/10** (v=0) | 0/10 | 0/10 |
| epoch_070 | **5/10** (v=5) | **5/10** (v=3) | 0/10 | 0/10 | 0/10 |

### alpha = 0.99

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | **10/10** (v=0) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_018 | **6/10** (v=1) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_035 | **6/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_052 | **9/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_070 | **8/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |

---

## alpha-beta-CROWN (nopgd) — Genuine Verified

### alpha = 0.95

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 (v=1) | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_018 | **7/10** (v=3) | **1/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_035 | **6/10** (v=3) | **3/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_052 | **4/10** (v=4) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |
| epoch_070 | **4/10** (v=5) | **2/10** (v=1) | 0/10 | 0/10 | 0/10 |

### alpha = 0.99

| Checkpoint | eps=0.01 | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 |
|------------|----------|----------|----------|---------|---------|
| epoch_000 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| epoch_018 | **8/10** (v=1) | **1/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_035 | **8/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_052 | **7/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |
| epoch_070 | **7/10** (v=1) | **3/10** (v=0) | 0/10 | 0/10 | 0/10 |

---

## Detailed Per-Reference Results (Interesting Cases)

Cases where NAP genuinely verifies but baseline fails.

| Checkpoint | Ref | Label | eps | alpha | NAP | BL at same eps | Time (s) |
|------------|-----|-------|-----|-------|-----|---------------|----------|
| epoch_018 | ref3 | 0 | 0.02 | 0.95 | Y | T/o | 41.2 |
| epoch_035 | ref3 | 0 | 0.02 | 0.95 | Y | Y | 35.9 |
| epoch_035 | ref3 | 0 | 0.02 | 0.99 | Y | Y | 25.4 |
| epoch_035 | ref8 | 9 | 0.02 | 0.95 | Y | T/o | 41.6 |
| epoch_035 | ref8 | 9 | 0.02 | 0.99 | Y | T/o | 36.1 |
| epoch_035 | ref9 | 0 | 0.02 | 0.95 | Y | Y | 34.7 |
| epoch_035 | ref9 | 0 | 0.02 | 0.99 | Y | Y | 34.3 |
| epoch_052 | ref3 | 0 | 0.05 | 0.95 | Y | T/o | 820.6 |
| epoch_052 | ref0 | 7 | 0.02 | 0.95 | Y | T/o | 23.9 |
| epoch_052 | ref1 | 2 | 0.02 | 0.99 | Y | T/o | 24.5 |
| epoch_052 | ref3 | 0 | 0.02 | 0.95 | Y | Y | 34.1 |
| epoch_052 | ref3 | 0 | 0.02 | 0.99 | Y | Y | 24.5 |
| epoch_052 | ref4 | 4 | 0.02 | 0.95 | Y | T/o | 527.2 |
| epoch_052 | ref9 | 9 | 0.02 | 0.95 | Y | T/o | 38.4 |
| epoch_052 | ref9 | 9 | 0.02 | 0.99 | Y | T/o | 35.2 |
| epoch_070 | ref0 | 7 | 0.02 | 0.95 | Y | T/o | 23.9 |
| epoch_070 | ref1 | 2 | 0.02 | 0.99 | Y | T/o | 25.0 |
| epoch_070 | ref3 | 0 | 0.02 | 0.95 | Y | Y | 24.9 |
| epoch_070 | ref3 | 0 | 0.02 | 0.99 | Y | Y | 37.4 |
| epoch_070 | ref4 | 4 | 0.02 | 0.95 | Y | T/o | 270.9 |

---

## Summary

- **Baseline verified:** 27/250 (10.8%)
- **NAP genuine verified:** 93/500 (18.6%)
- **NAP vacuous:** 34/500 (6.8%)
- **Max NAP-verified epsilon:** 0.05 at epoch_052 (alpha=0.95, 1/10 genuine)
- **Max BL-verified epsilon:** 0.02 at epoch_035 (2/10)

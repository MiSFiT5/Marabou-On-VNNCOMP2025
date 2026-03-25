# N1,4 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_4_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0249, 0.0443, 0.0251, 0.012, 0.0021]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 0 | Clear-of-Conflict | `–` | – | – | ❌ Not verified at any ε |
| 1 | Weak Left | `–` | – | – | ❌ Not verified at any ε |
| 2 | Weak Right | `–` | – | – | ❌ Not verified at any ε |
| 3 | Strong Left | `–` | – | – | ❌ Not verified at any ε |

**Overall:** This reference point is **NOT fully robust** at any tested ε (at least one target cannot be verified).

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

*Can the network be fooled from class 4 (Strong Right) to class 0 (Clear-of-Conflict) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (117s) | 🔴 N (106s) | 🔴 N (93s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (110s) | 🟡 T/o (120s) | 🔴 N (34s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (5s) | 🔴 N (69s) | 🟡 T/o (120s) | 🔴 N (55s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (81s) | 🔴 N (48s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (27s) | 🔴 N (44s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (36s) | 🔴 N (52s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (14s) | 🔴 N (51s) | 🔴 N (109s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (63s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (69s) | 🔴 N (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (8s) | 🔴 N (43s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (55s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (69s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (20s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (24s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (19s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (111s) | 🟡 T/o (120s) | 🔴 N (32s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (93s) | 🔴 N (96s) | 🔴 N (28s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (4s) | 🔴 N (71s) | 🟡 T/o (120s) | 🔴 N (30s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (31s) | 🔴 N (49s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (31s) | 🔴 N (57s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (24s) | 🔴 N (50s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (10s) | 🔴 N (63s) | 🔴 N (115s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (3s) | 🔴 N (8s) | 🔴 N (55s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (56s) | 🔴 N (101s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (8s) | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (8s) | 🔴 N (54s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (5s) | 🔴 N (60s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (14s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (19s) | 🔴 N (7s) | 🔴 N (31s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (9s) | 🔴 N (31s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (9s) | 🔴 N (32s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (18s) | 🔴 N (89s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (27s) | 🔴 N (97s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (8s) | 🔴 N (32s) | 🔴 N (44s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (60s) | 🔴 N (118s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (74s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (50s) | 🔴 N (107s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (28s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (21s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (27s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (20s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (13s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (7s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🔴 N (115s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (67s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🔴 N (102s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (70s) | 🔴 N (58s) | 🟡 T/o (120s) | 🔴 N (43s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (9s) | 🔴 N (14s) | 🔴 N (51s) | 🔴 N (61s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (8s) | 🔴 N (11s) | 🔴 N (50s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (10s) | 🔴 N (17s) | 🔴 N (90s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (14s) | 🔴 N (10s) | 🔴 N (66s) | 🔴 N (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (63s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (19s) | 🔴 N (50s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (55s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (51s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (6s) | 🔴 N (52s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (18s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (15s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (19s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

---

## Per-Layer Results (ε=0.02 only, α=0.90)

Which layer pair contributes most to verification?

| Layer Pair Rule | Targets Verified (of 4) |
|-----------------|------------------------|
| `Impl L0→L1 (α=0.9)` | 0/4 |
| `Impl L1→L2 (α=0.9)` | 0/4 |
| `Impl L2→L3 (α=0.9)` | 0/4 |
| `Impl L3→L4 (α=0.9)` | 0/4 |
| `Impl L4→L5 (α=0.9)` | 0/4 |

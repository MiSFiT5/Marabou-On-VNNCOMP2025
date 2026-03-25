# N5,1 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_5_1_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.3064, 0.3386, 0.2674, 0.3318, 0.1919]`
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
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (31s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (90s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (14s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (14s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (13s) | 🔴 N (7s) | 🔴 N (20s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (10s) | 🔴 N (58s) | 🔴 N (38s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (73s) | 🔴 N (45s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (10s) | 🔴 N (69s) | 🔴 N (106s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (90s) | 🔴 N (99s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (68s) | 🔴 N (98s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (85s) | 🔴 N (94s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (39s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (101s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (66s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (12s) | 🔴 N (31s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (4s) | 🔴 N (6s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (4s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (46s) | 🔴 N (4s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (7s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (62s) | 🔴 N (65s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (10s) | 🔴 N (64s) | 🔴 N (49s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (75s) | 🔴 N (57s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (80s) | 🔴 N (115s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (71s) | 🔴 N (110s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (84s) | 🔴 N (75s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (37s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (66s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (68s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (12s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (22s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (19s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (13s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (13s) | 🔴 N (13s) | 🔴 N (50s) | 🔴 N (44s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (56s) | 🔴 N (35s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (75s) | 🔴 N (37s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (75s) | 🔴 N (118s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (81s) | 🔴 N (88s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (84s) | 🔴 N (86s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (39s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (33s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (17s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (19s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (4s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (11s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (46s) | 🔴 N (37s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (64s) | 🔴 N (39s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (82s) | 🔴 N (49s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (79s) | 🔴 N (108s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (81s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (103s) | 🔴 N (69s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (38s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (75s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (86s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

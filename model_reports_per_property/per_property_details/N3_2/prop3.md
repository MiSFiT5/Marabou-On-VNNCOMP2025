# N3,2 — Property 3

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_2_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.1543, 0.1605, 0.1018, 0.1431, 0.0893]`
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
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (26s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (24s) | 🔴 N (13s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (9s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (32s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (11s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (5s) | 🔴 N (76s) | 🔴 N (38s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (7s) | 🔴 N (62s) | 🔴 N (67s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (70s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🔴 N (36s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (105s) | 🟡 T/o (120s) | 🔴 N (48s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🔴 N (96s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (11s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (10s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (4s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🟡 T/o (120s) | 🔴 N (8s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (9s) | 🔴 N (36s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (6s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (15s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (10s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (7s) | 🔴 N (66s) | 🔴 N (27s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (7s) | 🔴 N (59s) | 🔴 N (34s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (82s) | 🔴 N (18s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (89s) | 🟡 T/o (126s) | 🔴 N (55s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (20s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (15s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (29s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (11s) | 🔴 N (4s) | 🔴 N (11s) | 🔴 N (29s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (18s) | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (12s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (15s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (88s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (10s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (3s) | 🔴 N (91s) | 🔴 N (16s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (7s) | 🔴 N (2s) | 🔴 N (25s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (7s) | 🔴 N (80s) | 🔴 N (71s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🔴 N (36s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🔴 N (48s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (3s) | 🟡 T/o (120s) | 🔴 N (55s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (59s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (25s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (14s) | 🔴 N (14s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (12s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (5s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (12s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (73s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (13s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (6s) | 🔴 N (72s) | 🟡 T/o (121s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (77s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (6s) | 🔴 N (76s) | 🔴 N (31s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🔴 N (116s) | 🔴 N (54s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (4s) | 🟡 T/o (120s) | 🔴 N (64s) | 🟡 T/o (120s) |

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

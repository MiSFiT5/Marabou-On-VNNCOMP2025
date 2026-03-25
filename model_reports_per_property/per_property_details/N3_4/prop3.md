# N3,4 — Property 3

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_4_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0431, 0.0402, 0.0006, 0.033, -0.0122]`
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
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (11s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (6s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (17s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (31s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (16s) | 🔴 N (17s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (30s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (5s) | 🔴 N (38s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (92s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (6s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (9s) | 🔴 N (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (58s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (72s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (75s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (27s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (28s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (8s) | 🔴 N (16s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (54s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (5s) | 🔴 N (29s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (68s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (5s) | 🔴 N (58s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (99s) | 🔴 N (6s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (11s) | 🔴 N (117s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (40s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (73s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (41s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (15s) | 🔴 N (44s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (11s) | 🔴 N (65s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (15s) | 🔴 N (17s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (37s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (47s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (92s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (88s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (9s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (79s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (76s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (14s) | 🔴 N (74s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (16s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (30s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (11s) | 🔴 N (46s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (8s) | 🔴 N (32s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (4s) | 🔴 N (48s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (73s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🟡 T/o (120s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (12s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (46s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (101s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (76s) | 🟡 T/o (120s) |

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

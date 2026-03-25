# N5,1 — Property 3

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_5_1_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.1892, 0.1846, 0.1343, 0.1776, 0.1187]`
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
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🟡 T/o (120s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (17s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (16s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (19s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (15s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (23s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (4s) | 🔴 N (2s) | 🔴 N (21s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (2s) | 🔴 N (16s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (50s) | 🔴 N (6s) | 🔴 N (29s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (5s) | 🔴 N (13s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (67s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (14s) | 🔴 N (73s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (14s) | 🔴 N (73s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (30s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (15s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (10s) | 🔴 N (106s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (37s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🟡 T/o (120s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (19s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (15s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (17s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (16s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (21s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (18s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (28s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (3s) | 🔴 N (19s) | 🔴 N (5s) | 🔴 N (66s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (40s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (12s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (84s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (13s) | 🔴 N (75s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (10s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (14s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (21s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (21s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (73s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🟡 T/o (120s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (15s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (17s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (7s) | 🔴 N (14s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (18s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (24s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (21s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (35s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (31s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (6s) | 🔴 N (97s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (65s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (16s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (14s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (2s) | 🔴 N (9s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (17s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (17s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (34s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (11s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (18s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (17s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (15s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (18s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (20s) | 🔴 N (19s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (49s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (7s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (76s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (14s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (8s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (12s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (7s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (13s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (16s) | 🟡 T/o (120s) |

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

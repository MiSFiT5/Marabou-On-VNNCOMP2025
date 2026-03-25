# N4,8 — Property 1

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_8_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0365, -0.0213, 0.0208, -0.0143, 0.0198]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 0 | Clear-of-Conflict | `–` | – | – | ❌ Not verified at any ε |
| 2 | Weak Right | `–` | – | – | ❌ Not verified at any ε |
| 3 | Strong Left | `–` | – | – | ❌ Not verified at any ε |
| 4 | Strong Right | `–` | – | – | ❌ Not verified at any ε |

**Overall:** This reference point is **NOT fully robust** at any tested ε (at least one target cannot be verified).

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

*Can the network be fooled from class 1 (Weak Left) to class 0 (Clear-of-Conflict) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (21s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (6s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (8s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (12s) | 🔴 N (88s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (14s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (54s) | 🔴 N (22s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (16s) | 🔴 N (29s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (15s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (33s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (105s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (31s) | 🔴 N (28s) | 🔴 N (56s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (7s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (12s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (79s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (25s) | 🔴 N (105s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 1 (Weak Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (20s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (19s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (24s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (8s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (44s) | 🔴 N (60s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (4s) | 🔴 N (71s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (48s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 1 (Weak Left) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (17s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (16s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (50s) | 🔴 N (23s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (20s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (9s) | 🔴 N (99s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (48s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (105s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (8s) | 🔴 N (74s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (18s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (101s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (12s) | 🔴 N (47s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 1 (Weak Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (15s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (47s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (4s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (21s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (5s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (19s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (30s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (31s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (87s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (29s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (70s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (8s) | 🔴 N (77s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (15s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🟡 T/o (120s) | 🔴 N (26s) |

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

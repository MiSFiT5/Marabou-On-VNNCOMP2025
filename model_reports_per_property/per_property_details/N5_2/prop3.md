# N5,2 — Property 3

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_5_2_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.1612, 0.1538, 0.0929, 0.1447, 0.0755]`
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
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (33s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (20s) | 🔴 N (77s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (8s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (15s) | 🔴 N (38s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (15s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (44s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (89s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (47s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (9s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (28s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (22s) | 🔴 N (44s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (5s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (17s) | 🔴 N (29s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (117s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (57s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (22s) | 🔴 N (93s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (94s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (116s) | 🔴 N (20s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (30s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (56s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (6s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (20s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (4s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (3s) | 🔴 N (45s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (24s) | 🔴 N (94s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (24s) | 🔴 N (98s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (45s) | 🔴 N (44s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (3s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (39s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (21s) | 🔴 N (41s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (61s) | 🔴 N (5s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (17s) | 🔴 N (27s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (26s) | 🟡 T/o (120s) | 🔴 N (63s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (49s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (21s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (97s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (31s) | 🔴 N (14s) | 🟡 T/o (120s) |

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

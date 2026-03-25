# N4,3 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_3_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.1665, 0.1652, 0.1682, 0.1129, 0.1127]`
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
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (7s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (20s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (48s) | 🔴 N (22s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (10s) | 🔴 N (49s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (46s) | 🔴 N (18s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (52s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (44s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (48s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (4s) | 🔴 N (12s) | 🔴 N (86s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (86s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (12s) | 🔴 N (84s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (3s) | 🔴 N (68s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🔴 N (99s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (14s) | 🔴 N (101s) | 🔴 N (63s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (12s) | 🔴 N (99s) | 🔴 N (77s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (116s) | 🔴 N (69s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (69s) | 🔴 N (32s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (58s) | 🔴 N (19s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (66s) | 🔴 N (24s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (39s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (50s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (46s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (91s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (15s) | 🔴 N (86s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (14s) | 🔴 N (93s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (3s) | 🔴 N (99s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (3s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (9s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (9s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (91s) | 🔴 N (32s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (13s) | 🔴 N (82s) | 🔴 N (18s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (48s) | 🔴 N (93s) | 🔴 N (16s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (36s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (45s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (50s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (99s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (12s) | 🔴 N (89s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (3s) | 🔴 N (12s) | 🔴 N (81s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (3s) | 🔴 N (72s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🔴 N (117s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🔴 N (115s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (118s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (24s) | 🔴 N (92s) | 🔴 N (70s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (21s) | 🟡 T/o (120s) | 🔴 N (62s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (21s) | 🔴 N (94s) | 🔴 N (61s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (22s) | 🔴 N (55s) | 🔴 N (47s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (23s) | 🔴 N (65s) | 🔴 N (33s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (23s) | 🔴 N (59s) | 🔴 N (29s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (44s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (41s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (44s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (97s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (16s) | 🔴 N (98s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (94s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (58s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (5s) | 🔴 N (119s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🔴 N (117s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

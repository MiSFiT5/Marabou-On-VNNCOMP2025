# N5,5 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_5_5_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0427, 0.0369, 0.0049, 0.0271, -0.0127]`
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
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (49s) | 🔴 N (22s) | 🔴 N (6s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (17s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (34s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (29s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (26s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (67s) | 🔴 N (71s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (6s) | 🔴 N (61s) | 🔴 N (53s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (23s) | 🔴 N (18s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (82s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (85s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (82s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (25s) | 🔴 N (98s) | 🔴 N (61s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (21s) | 🔴 N (73s) | 🔴 N (99s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (58s) | 🔴 N (118s) | 🔴 N (100s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (5s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (18s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (7s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (27s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (21s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (23s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (54s) | 🔴 N (60s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (6s) | 🔴 N (61s) | 🔴 N (63s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (39s) | 🔴 N (23s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (83s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (87s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (98s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (24s) | 🔴 N (86s) | 🔴 N (68s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (22s) | 🟡 T/o (120s) | 🔴 N (78s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (23s) | 🔴 N (96s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (4s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (14s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (3s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (23s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (24s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (23s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (5s) | 🔴 N (52s) | 🔴 N (66s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (7s) | 🔴 N (51s) | 🔴 N (70s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (40s) | 🔴 N (20s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (84s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (87s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (32s) | 🔴 N (114s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (61s) | 🔴 N (80s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (24s) | 🔴 N (72s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (21s) | 🔴 N (99s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (6s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (3s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (23s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (7s) | 🔴 N (27s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (27s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (60s) | 🔴 N (66s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (4s) | 🔴 N (50s) | 🔴 N (64s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (46s) | 🔴 N (20s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (13s) | 🔴 N (87s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (89s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (17s) | 🔴 N (94s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (77s) | 🔴 N (77s) | 🔴 N (72s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (60s) | 🔴 N (103s) | 🔴 N (71s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (23s) | 🔴 N (91s) | 🔴 N (57s) |

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

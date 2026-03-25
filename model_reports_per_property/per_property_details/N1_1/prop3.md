# N1,1 — Property 3

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_1_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.1326, 0.1359, 0.1402, 0.0955, 0.1106]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 0 | Clear-of-Conflict | `–` | – | – | ❌ Not verified at any ε |
| 1 | Weak Left | `–` | – | – | ❌ Not verified at any ε |
| 2 | Weak Right | `–` | – | – | ❌ Not verified at any ε |
| 4 | Strong Right | `–` | – | – | ❌ Not verified at any ε |

**Overall:** This reference point is **NOT fully robust** at any tested ε (at least one target cannot be verified).

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

*Can the network be fooled from class 3 (Strong Left) to class 0 (Clear-of-Conflict) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (9s) | 🔴 N (13s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (23s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (32s) | 🔴 N (48s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (31s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (26s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (21s) | 🔴 N (12s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (5s) | 🔴 N (3s) | 🔴 N (94s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (6s) | 🔴 N (3s) | 🔴 N (36s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (11s) | 🔴 N (3s) | 🔴 N (22s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (11s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (23s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (28s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (25s) | 🔴 N (80s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (100s) | 🔴 N (89s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (16s) | 🔴 N (91s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 3 (Strong Left) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (15s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🟡 T/o (120s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (44s) | 🔴 N (37s) | 🔴 N (4s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (10s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (28s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (26s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (11s) | 🔴 N (13s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (23s) | 🔴 N (3s) | 🔴 N (54s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (8s) | 🔴 N (3s) | 🔴 N (42s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (7s) | 🔴 N (3s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (9s) | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (19s) | 🔴 N (4s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (23s) | 🔴 N (3s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (67s) | 🔴 N (89s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (39s) | 🔴 N (109s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (20s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 3 (Strong Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (30s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (13s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (13s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (13s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (22s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (17s) | 🔴 N (3s) | 🔴 N (11s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (17s) | 🔴 N (6s) | 🔴 N (33s) | 🔴 N (10s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (7s) | 🔴 N (3s) | 🔴 N (38s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (8s) | 🔴 N (3s) | 🔴 N (49s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (15s) | 🔴 N (3s) | 🔴 N (7s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (5s) | 🔴 N (4s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (30s) | 🔴 N (48s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (28s) | 🔴 N (9s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (53s) | 🔴 N (99s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (18s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (90s) | 🔴 N (91s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 3 (Strong Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (18s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🟡 T/o (120s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (34s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (78s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (107s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (53s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (15s) | 🔴 N (76s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (10s) | 🔴 N (4s) | 🔴 N (28s) | 🔴 N (28s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (16s) | 🔴 N (5s) | 🔴 N (48s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (11s) | 🔴 N (3s) | 🔴 N (77s) | 🔴 N (18s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (7s) | 🔴 N (5s) | 🔴 N (53s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (7s) | 🔴 N (9s) | 🔴 N (40s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (10s) | 🔴 N (91s) | 🔴 N (6s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (42s) | 🔴 N (9s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (23s) | 🔴 N (12s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (25s) | 🔴 N (24s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (15s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (15s) | 🔴 N (119s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (50s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

# N1,1 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_1_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.2353, 0.2429, 0.2497, 0.1913, 0.2096]`
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
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (22s) | 🟡 T/o (120s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (25s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (56s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (16s) | 🔴 N (18s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (16s) | 🔴 N (18s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (5s) | 🔴 N (7s) | 🔴 N (17s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (32s) | 🔴 N (58s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (6s) | 🔴 N (13s) | 🔴 N (31s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (5s) | 🔴 N (15s) | 🔴 N (48s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (5s) | 🔴 N (13s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (9s) | 🔴 N (17s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (43s) | 🔴 N (38s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (4s) | 🔴 N (82s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (4s) | 🔴 N (105s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (24s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 3 (Strong Left) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (16s) | 🔴 N (22s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (17s) | 🔴 N (18s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (6s) | 🔴 N (5s) | 🔴 N (21s) | 🔴 N (18s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (8s) | 🔴 N (7s) | 🔴 N (43s) | 🔴 N (50s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (6s) | 🔴 N (8s) | 🔴 N (40s) | 🔴 N (49s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (5s) | 🔴 N (12s) | 🔴 N (33s) | 🔴 N (53s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (5s) | 🔴 N (11s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (8s) | 🔴 N (18s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (18s) | 🔴 N (18s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (5s) | 🔴 N (99s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (5s) | 🔴 N (107s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (16s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (33s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (115s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 3 (Strong Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🟡 T/o (120s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (18s) | 🔴 N (4s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (55s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (21s) | 🔴 N (20s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (9s) | 🔴 N (61s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (5s) | 🔴 N (7s) | 🔴 N (15s) | 🔴 N (19s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (5s) | 🔴 N (11s) | 🔴 N (70s) | 🔴 N (61s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (6s) | 🔴 N (12s) | 🔴 N (31s) | 🔴 N (51s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (11s) | 🔴 N (10s) | 🔴 N (39s) | 🔴 N (55s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (5s) | 🔴 N (13s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (19s) | 🔴 N (17s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (45s) | 🔴 N (16s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (6s) | 🔴 N (83s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (5s) | 🔴 N (91s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (26s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 3 (Strong Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (15s) | 🔴 N (26s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (6s) | 🔴 N (6s) | 🔴 N (13s) | 🔴 N (18s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (54s) | 🔴 N (7s) | 🔴 N (21s) | 🔴 N (22s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (5s) | 🔴 N (24s) | 🔴 N (34s) | 🔴 N (82s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (6s) | 🔴 N (11s) | 🔴 N (68s) | 🔴 N (56s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (6s) | 🔴 N (8s) | 🔴 N (27s) | 🔴 N (78s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (6s) | 🔴 N (12s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (8s) | 🔴 N (14s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (12s) | 🔴 N (15s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (7s) | 🔴 N (106s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (6s) | 🔴 N (67s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (27s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

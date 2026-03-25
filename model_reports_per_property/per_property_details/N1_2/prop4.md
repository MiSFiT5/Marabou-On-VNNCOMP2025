# N1,2 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_2_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.2207, 0.2313, 0.2447, 0.1647, 0.2012]`
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
| `none (baseline)` | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (9s) | 🔴 N (27s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (8s) | 🔴 N (30s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (8s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (24s) | 🔴 N (108s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (44s) | 🔴 N (14s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (12s) | 🔴 N (30s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (15s) | 🔴 N (104s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (37s) | 🔴 N (103s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (39s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (5s) | 🔴 N (24s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (6s) | 🔴 N (61s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (14s) | 🔴 N (117s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (60s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (85s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (94s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 3 (Strong Left) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (12s) | 🔴 N (27s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (18s) | 🔴 N (23s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (25s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (9s) | 🔴 N (13s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (22s) | 🔴 N (10s) | 🔴 N (15s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (5s) | 🔴 N (9s) | 🔴 N (13s) | 🔴 N (46s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (11s) | 🔴 N (38s) | 🔴 N (103s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (31s) | 🔴 N (108s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (74s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (4s) | 🔴 N (25s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (5s) | 🔴 N (51s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (14s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (72s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (82s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (91s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 3 (Strong Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (5s) | 🔴 N (28s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (4s) | 🔴 N (12s) | 🔴 N (14s) | 🔴 N (119s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (9s) | 🔴 N (21s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (10s) | 🔴 N (17s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (16s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (15s) | 🔴 N (12s) | 🔴 N (51s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (34s) | 🔴 N (94s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (14s) | 🔴 N (114s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (20s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (3s) | 🔴 N (24s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (5s) | 🔴 N (88s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (14s) | 🔴 N (112s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (71s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (87s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (4s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 3 (Strong Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (9s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (7s) | 🔴 N (30s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (8s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (9s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (5s) | 🔴 N (7s) | 🔴 N (38s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (11s) | 🔴 N (12s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (15s) | 🔴 N (105s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (3s) | 🔴 N (10s) | 🔴 N (13s) | 🔴 N (99s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (22s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (5s) | 🔴 N (22s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (5s) | 🔴 N (54s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (15s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (53s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (86s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

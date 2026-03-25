# N3,5 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_5_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0401, 0.0468, 0.004, 0.0394, -0.0074]`
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
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (8s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (10s) | 🔴 N (18s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (38s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (33s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (12s) | 🔴 N (114s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (12s) | 🔴 N (38s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (5s) | 🔴 N (2s) | 🔴 N (16s) | 🔴 N (46s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (77s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (6s) | 🟡 T/o (120s) | 🔴 N (105s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (71s) | 🔴 N (114s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (3s) | 🔴 N (59s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🔴 N (53s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (3s) | 🔴 N (50s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (9s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (9s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (109s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (7s) | 🔴 N (28s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (18s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (6s) | 🔴 N (3s) | 🔴 N (17s) | 🔴 N (40s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (11s) | 🔴 N (58s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (32s) | 🔴 N (73s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (13s) | 🟡 T/o (120s) | 🔴 N (119s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (50s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (2s) | 🔴 N (49s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (3s) | 🔴 N (47s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🔴 N (54s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (6s) | 🔴 N (10s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (8s) | 🔴 N (23s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (47s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (6s) | 🔴 N (26s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (14s) | 🔴 N (90s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (11s) | 🔴 N (38s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (19s) | 🔴 N (46s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (76s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (113s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (66s) | 🔴 N (105s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (2s) | 🔴 N (59s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (3s) | 🔴 N (40s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🔴 N (59s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (7s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (8s) | 🔴 N (23s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (54s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (55s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (15s) | 🔴 N (86s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (15s) | 🔴 N (38s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (17s) | 🔴 N (47s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (7s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (70s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (3s) | 🔴 N (50s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (3s) | 🔴 N (40s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (4s) | 🔴 N (61s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

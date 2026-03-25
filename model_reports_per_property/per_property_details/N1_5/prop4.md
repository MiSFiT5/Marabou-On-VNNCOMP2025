# N1,5 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_5_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0084, 0.0091, 0.006, -0.0009, -0.0052]`
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
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (9s) | 🔴 N (10s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (61s) | 🔴 N (9s) | 🔴 N (14s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (13s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (18s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (19s) | 🔴 N (18s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (16s) | 🔴 N (104s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (17s) | 🔴 N (92s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (16s) | 🔴 N (92s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (7s) | 🔴 N (7s) | 🟡 T/o (121s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (96s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (19s) | 🔴 N (96s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (57s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (70s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (49s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (3s) | 🔴 N (31s) | 🔴 N (8s) | 🔴 N (15s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (19s) | 🔴 N (9s) | 🔴 N (11s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (3s) | 🔴 N (30s) | 🔴 N (10s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (13s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (15s) | 🔴 N (14s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (23s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (17s) | 🔴 N (76s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (15s) | 🔴 N (62s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (15s) | 🔴 N (76s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (83s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (98s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (19s) | 🔴 N (93s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (2s) | 🔴 N (59s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (51s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (53s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (14s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (10s) | 🔴 N (10s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (13s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (12s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (14s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (20s) | 🔴 N (16s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (14s) | 🔴 N (77s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (17s) | 🔴 N (68s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (15s) | 🔴 N (72s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (7s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (104s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (18s) | 🔴 N (103s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (2s) | 🔴 N (44s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (44s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (42s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (18s) | 🟡 T/o (120s) | 🔴 N (13s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (4s) | 🔴 N (18s) | 🟡 T/o (120s) | 🔴 N (13s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (15s) | 🟡 T/o (120s) | 🔴 N (48s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (18s) | 🔴 N (46s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (23s) | 🔴 N (41s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (3s) | 🔴 N (23s) | 🔴 N (20s) | 🔴 N (51s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (15s) | 🔴 N (63s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (15s) | 🔴 N (88s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (17s) | 🔴 N (96s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (94s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (108s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (12s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (47s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (48s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (43s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

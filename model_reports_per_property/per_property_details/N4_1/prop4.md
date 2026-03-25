# N4,1 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_1_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.3055, 0.31, 0.3052, 0.2746, 0.2557]`
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
| `none (baseline)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (10s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (16s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (57s) | 🔴 N (113s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (62s) | 🔴 N (94s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (64s) | 🔴 N (87s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (36s) | 🔴 N (83s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (47s) | 🔴 N (92s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (47s) | 🔴 N (105s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (7s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (91s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (13s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (14s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (88s) | 🔴 N (88s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (79s) | 🔴 N (88s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (85s) | 🔴 N (112s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (39s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (54s) | 🔴 N (41s) | 🔴 N (71s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (53s) | 🔴 N (111s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (15s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (14s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (7s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (6s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (11s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (15s) | 🔴 N (95s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (12s) | 🔴 N (105s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (3s) | 🔴 N (39s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (37s) | 🔴 N (72s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (48s) | 🔴 N (91s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (15s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (9s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (18s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (0s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (18s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (12s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (14s) | 🔴 N (12s) | 🔴 N (12s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (69s) | 🔴 N (77s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (14s) | 🔴 N (69s) | 🔴 N (106s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (15s) | 🔴 N (66s) | 🔴 N (107s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (29s) | 🔴 N (73s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (40s) | 🔴 N (83s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (44s) | 🔴 N (70s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (17s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (14s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (17s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

# N3,3 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_3_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.1544, 0.1948, 0.1065, 0.1941, 0.0569]`
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
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (25s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (23s) | 🔴 N (23s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🔴 N (7s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (10s) | 🔴 N (18s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (11s) | 🔴 N (17s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (11s) | 🔴 N (15s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (10s) | 🔴 N (33s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (44s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (34s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (117s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (22s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (28s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (2s) | 🔴 N (87s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (14s) | 🔴 N (115s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (46s) | 🔴 N (99s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (87s) | 🔴 N (6s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (18s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (11s) | 🔴 N (19s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (10s) | 🔴 N (17s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (41s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (37s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (50s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (24s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (52s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (117s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (62s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (26s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (24s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (26s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (64s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (8s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (19s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (9s) | 🔴 N (33s) | 🔴 N (105s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (2s) | 🔴 N (16s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (66s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🔴 N (48s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (112s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (81s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (31s) | 🔴 N (83s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (36s) | 🔴 N (82s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (12s) | 🔴 N (7s) | 🔴 N (33s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (12s) | 🔴 N (20s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (12s) | 🔴 N (14s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (11s) | 🔴 N (20s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (32s) | 🔴 N (115s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (10s) | 🔴 N (34s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (10s) | 🔴 N (31s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (3s) | 🔴 N (17s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (25s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (107s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (115s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

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

# N4,5 — Property 2

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_5_batch_2000.onnx`
- **Property:** prop2
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.0422, -0.0147, 0.0209, -0.0208, 0.0245]`
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
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (35s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (3s) | 🔴 N (5s) | 🔴 N (11s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (3s) | 🔴 N (16s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (4s) | 🔴 N (36s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (22s) | 🔴 N (63s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (17s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (17s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (18s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (10s) | 🔴 N (19s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (9s) | 🔴 N (20s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (31s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (13s) | 🔴 N (77s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (87s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 3 (Strong Left) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🟡 T/o (120s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (41s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (44s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (21s) | 🔴 N (27s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (13s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (16s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (24s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (25s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (19s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (19s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (12s) | 🔴 N (14s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (100s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 3 (Strong Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (32s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (15s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (16s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (20s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (20s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (23s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (3s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (20s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (20s) | 🔴 N (90s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 3 (Strong Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (43s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (15s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (21s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (18s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (20s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (10s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (26s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (24s) | 🔴 N (90s) |

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

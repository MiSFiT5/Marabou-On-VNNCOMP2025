# N2,4 — Property 2

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_2_4_batch_2000.onnx`
- **Property:** prop2
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0228, -0.0217, 0.0221, -0.0162, 0.023]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 0 | Clear-of-Conflict | `–` | – | – | ❌ Not verified at any ε |
| 2 | Weak Right | `–` | – | – | ❌ Not verified at any ε |
| 3 | Strong Left | `–` | – | – | ❌ Not verified at any ε |
| 4 | Strong Right | `–` | – | – | ❌ Not verified at any ε |

**Overall:** This reference point is **NOT fully robust** at any tested ε (at least one target cannot be verified).

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

*Can the network be fooled from class 1 (Weak Left) to class 0 (Clear-of-Conflict) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (3s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (15s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (3s) | 🔴 N (15s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (13s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (43s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (44s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (48s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (11s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (9s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (11s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 1 (Weak Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (30s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (23s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (51s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (13s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (18s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (12s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 1 (Weak Left) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (34s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (30s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (55s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (19s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (13s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 1 (Weak Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (27s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (35s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (47s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (22s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (15s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (12s) |

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

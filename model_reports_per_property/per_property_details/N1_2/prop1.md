# N1,2 — Property 1

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_2_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **0** (Clear-of-Conflict)
- **Network outputs at midpoint:** `[-0.0204, -0.0185, -0.0182, -0.018, -0.018]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 1 | Weak Left | `ALWAYS_OFF (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |
| 2 | Weak Right | `ALWAYS_OFF (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |
| 3 | Strong Left | `ALWAYS_OFF (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |
| 4 | Strong Right | `ALWAYS_OFF (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |

**Overall:** This reference point is **fully robust** (all 4 targets verified) up to **ε = 0.02** (with appropriate NAP rules).

---

## Detailed Results Per Target

### Target 1 (Weak Left)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (3s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (2s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.95)` | 🟢 Y (6s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (6s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (4s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (3s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (2s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (3s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.95)` | 🟢 Y (4s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (6s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (4s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (3s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (4s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (3s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.95)` | 🟢 Y (6s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (5s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (12s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (4s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (3s) | 🔴 N (0s) | 🟡 T/o (1864s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (2s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.95)` | 🟢 Y (8s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (3s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |

---

## Per-Layer Results (ε=0.02 only, α=0.90)

Which layer pair contributes most to verification?

| Layer Pair Rule | Targets Verified (of 4) |
|-----------------|------------------------|
| `Impl L0→L1 (α=0.9)` | 0/4 |
| `Impl L1→L2 (α=0.9)` | 4/4 |
| `Impl L2→L3 (α=0.9)` | 0/4 |
| `Impl L3→L4 (α=0.9)` | 4/4 |
| `Impl L4→L5 (α=0.9)` | 4/4 |

# N1,7 — Property 1

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_7_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **0** (Clear-of-Conflict)
- **Network outputs at midpoint:** `[-0.0195, -0.018, -0.0179, -0.0173, -0.0171]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 1 | Weak Left | `Impl L3→L4 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |
| 2 | Weak Right | `Impl L3→L4 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |
| 3 | Strong Left | `Impl L3→L4 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |
| 4 | Strong Right | `Impl L3→L4 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |

**Overall:** This reference point is **fully robust** (all 4 targets verified) up to **ε = 0.1** (with appropriate NAP rules).

---

## Detailed Results Per Target

### Target 1 (Weak Left)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (11s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (11s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (6s) |
| `Impl L0→L1 (α=0.95)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.95)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🟢 Y (51s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (0s) | 🔴 N (14s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (50s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (12s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (10s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.95)` | 🟢 Y (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (1s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (32s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.95)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🟢 Y (57s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (0s) | 🔴 N (17s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (12s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (10s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (40s) |
| `Impl L0→L1 (α=0.95)` | 🟢 Y (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (1s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (31s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.95)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🟢 Y (48s) | 🔴 N (3s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (0s) | 🔴 N (17s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (47s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 0 (Clear-of-Conflict) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (12s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🟢 Y (0s) | 🟢 Y (11s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (51s) |
| `Impl L0→L1 (α=0.95)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L2→L3 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🔴 N (13s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.95)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (1s) | 🟢 Y (49s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (2s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.9)` | 🟢 Y (0s) | 🔴 N (14s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (49s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) |

---

## Per-Layer Results (ε=0.02 only, α=0.90)

Which layer pair contributes most to verification?

| Layer Pair Rule | Targets Verified (of 4) |
|-----------------|------------------------|
| `Impl L0→L1 (α=0.9)` | 4/4 |
| `Impl L1→L2 (α=0.9)` | 4/4 |
| `Impl L2→L3 (α=0.9)` | 4/4 |
| `Impl L3→L4 (α=0.9)` | 4/4 |
| `Impl L4→L5 (α=0.9)` | 4/4 |

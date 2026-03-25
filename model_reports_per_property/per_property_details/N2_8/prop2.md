# N2,8 — Property 2

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_2_8_batch_2000.onnx`
- **Property:** prop2
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0396, -0.0215, 0.0206, -0.0144, 0.0226]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 0 | Clear-of-Conflict | `Impl L0→L1 (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |
| 2 | Weak Right | `Impl L0→L1 (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |
| 3 | Strong Left | `Impl L0→L1 (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |
| 4 | Strong Right | `Impl L0→L1 (α=0.9)` | 0.9 | 0.02 | ✅ Verified up to ε=0.02 |

**Overall:** This reference point is **fully robust** (all 4 targets verified) up to **ε = 0.02** (with appropriate NAP rules).

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

*Can the network be fooled from class 1 (Weak Left) to class 0 (Clear-of-Conflict) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (15s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (11s) | 🔴 N (7s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (28s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (35s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (8s) | 🔴 N (36s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (6s) | 🔴 N (18s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (5s) | 🔴 N (18s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (34s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (15s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (13s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (13s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 1 (Weak Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🟡 T/o (120s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (32s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (26s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (16s) | 🔴 N (34s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (39s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (6s) | 🔴 N (20s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (6s) | 🔴 N (25s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (51s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (11s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (12s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (11s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 1 (Weak Left) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (5s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.9)` | 🟡 T/o (120s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (33s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (8s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (5s) | 🔴 N (26s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (7s) | 🔴 N (30s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (36s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (35s) | 🔴 N (6s) | 🔴 N (24s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (27s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (53s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (13s) | 🔴 N (80s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (13s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (14s) | 🟡 T/o (120s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 1 (Weak Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (6s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (19s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (24s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (21s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (34s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (39s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (6s) | 🔴 N (25s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (7s) | 🔴 N (21s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (26s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (11s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (11s) | 🔴 N (118s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (12s) | 🟡 T/o (120s) |

---

## Per-Layer Results (ε=0.02 only, α=0.90)

Which layer pair contributes most to verification?

| Layer Pair Rule | Targets Verified (of 4) |
|-----------------|------------------------|
| `Impl L0→L1 (α=0.9)` | 4/4 |
| `Impl L1→L2 (α=0.9)` | 0/4 |
| `Impl L2→L3 (α=0.9)` | 0/4 |
| `Impl L3→L4 (α=0.9)` | 0/4 |
| `Impl L4→L5 (α=0.9)` | 0/4 |

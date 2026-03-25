# N5,1 — Property 2

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_5_1_batch_2000.onnx`
- **Property:** prop2
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0279, 0.0255, -0.0171, 0.0231, -0.0171]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 0 | Clear-of-Conflict | `Impl L0→L1 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |
| 1 | Weak Left | `Impl L3→L4 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |
| 2 | Weak Right | `Impl L0→L1 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |
| 3 | Strong Left | `Impl L3→L4 (α=0.9)` | 0.9 | 0.1 | ✅ Verified up to ε=0.1 |

**Overall:** This reference point is **fully robust** (all 4 targets verified) up to **ε = 0.1** (with appropriate NAP rules).

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

*Can the network be fooled from class 4 (Strong Right) to class 0 (Clear-of-Conflict) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (0s) | 🟢 Y (2s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (4s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (55s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (71s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (28s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🟢 Y (91s) | 🔴 N (69s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (62s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (4s) | 🔴 N (8s) | 🔴 N (4s) | 🔴 N (55s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (60s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (3s) | 🔴 N (1s) | 🔴 N (3s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 4 (Strong Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (2s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (8s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (42s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (72s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (16s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🟢 Y (91s) | 🔴 N (61s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (107s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (5s) | 🔴 N (65s) | 🔴 N (2s) | 🔴 N (9s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (56s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (9s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 4 (Strong Right) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🟡 T/o (120s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (0s) | 🟢 Y (1s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (11s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (80s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (35s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (48s) | 🔴 N (82s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (87s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🟢 Y (87s) | 🔴 N (71s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🟡 T/o (120s) | 🔴 N (38s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (86s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (5s) | 🔴 N (21s) | 🟡 T/o (120s) | 🔴 N (113s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (45s) | 🔴 N (2s) | 🔴 N (4s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 4 (Strong Right) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🟢 Y (0s) | 🟢 Y (0s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (10s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (55s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (6s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (14s) | 🔴 N (71s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (70s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (27s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🟢 Y (85s) | 🔴 N (90s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (33s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (83s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (4s) | 🔴 N (95s) | 🔴 N (2s) | 🔴 N (78s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (9s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) |

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

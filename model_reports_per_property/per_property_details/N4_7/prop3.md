# N4,7 — Property 3

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_7_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0264, -0.0192, 0.0191, -0.0152, 0.0201]`
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
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (16s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (5s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (24s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) | 🔴 N (14s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (82s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (95s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (19s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (32s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (57s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (36s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (8s) | 🔴 N (91s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (33s) |

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
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (13s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) | 🔴 N (22s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (7s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (2s) | 🔴 N (13s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (98s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (98s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (29s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (42s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (4s) | 🔴 N (36s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (34s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (14s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (37s) |

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
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (14s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (29s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (7s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (2s) | 🔴 N (16s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (94s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (109s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (33s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (16s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (69s) | 🔴 N (39s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (9s) | 🔴 N (41s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (59s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (30s) |

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
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (7s) | 🔴 N (6s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (48s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (9s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (2s) | 🔴 N (45s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (103s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (92s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (39s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (23s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (36s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (11s) | 🔴 N (32s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (9s) | 🔴 N (36s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (28s) |

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

# N3,9 — Property 1

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_9_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **2** (Weak Right)
- **Network outputs at midpoint:** `[0.0404, 0.0215, -0.0203, 0.0229, -0.0164]`
  - Predicted class has the **lowest** output (ACAS Xu uses argmin)

## Robustness Summary

For each target class, what is the **largest ε** at which this reference point is verified (Y/UNSAT)?

### Best result per target (across all rules and α)

| Target | Class Name | Best Rule | α | Max Verified ε | Status |
|--------|------------|-----------|---|----------------|--------|
| 0 | Clear-of-Conflict | `–` | – | – | ❌ Not verified at any ε |
| 1 | Weak Left | `–` | – | – | ❌ Not verified at any ε |
| 3 | Strong Left | `–` | – | – | ❌ Not verified at any ε |
| 4 | Strong Right | `–` | – | – | ❌ Not verified at any ε |

**Overall:** This reference point is **NOT fully robust** at any tested ε (at least one target cannot be verified).

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

*Can the network be fooled from class 2 (Weak Right) to class 0 (Clear-of-Conflict) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (13s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (21s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (101s) | 🔴 N (58s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (77s) | 🔴 N (47s) | 🔴 N (76s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (62s) | 🔴 N (25s) | 🔴 N (76s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (45s) | 🔴 N (45s) | 🔴 N (57s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (18s) | 🔴 N (32s) | 🔴 N (42s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (39s) | 🔴 N (78s) | 🔴 N (42s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (56s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (37s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (37s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (62s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (108s) | 🟡 T/o (120s) | 🔴 N (5s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 2 (Weak Right) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (115s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (5s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (23s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (22s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (19s) | 🔴 N (59s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (25s) | 🔴 N (29s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (79s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (31s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (27s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (35s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (55s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (18s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 2 (Weak Right) to class 3 (Strong Left) within an ε-ball?*

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
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (10s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (8s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (2s) | 🔴 N (2s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (25s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (25s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (25s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (19s) | 🔴 N (57s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (21s) | 🔴 N (77s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (21s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (28s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (35s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (38s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (31s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 2 (Weak Right) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (4s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (24s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (23s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (20s) | 🔴 N (54s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (22s) | 🔴 N (39s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (23s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (59s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (31s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (36s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (41s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (6s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (5s) |

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

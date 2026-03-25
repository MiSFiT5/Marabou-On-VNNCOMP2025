# N1,3 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_3_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.1129, 0.1106, 0.1559, 0.0424, 0.1366]`
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
| `none (baseline)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (4s) | 🟡 T/o (120s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (4s) | 🔴 N (16s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (15s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (22s) | 🔴 N (81s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (42s) | 🔴 N (41s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (26s) | 🔴 N (36s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (84s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (4s) | 🔴 N (7s) | 🔴 N (108s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (10s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (3s) | 🔴 N (32s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (2s) | 🔴 N (42s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (35s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 1 (Weak Left)

*Can the network be fooled from class 3 (Strong Left) to class 1 (Weak Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (22s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (15s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (15s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (24s) | 🟡 T/o (120s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (37s) | 🔴 N (25s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (27s) | 🔴 N (29s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (4s) | 🔴 N (7s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (3s) | 🔴 N (30s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (37s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (40s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (7s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 3 (Strong Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (21s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (12s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (13s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (24s) | 🔴 N (36s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (38s) | 🔴 N (33s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (28s) | 🔴 N (28s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (6s) | 🔴 N (35s) | 🔴 N (115s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (4s) | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (2s) | 🔴 N (9s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (23s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (33s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (39s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (6s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 3 (Strong Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (1s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (10s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (2s) | 🔴 N (3s) | 🔴 N (4s) | 🔴 N (13s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (17s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (24s) | 🔴 N (31s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (26s) | 🔴 N (41s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (28s) | 🔴 N (33s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (82s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (4s) | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (3s) | 🔴 N (7s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (3s) | 🔴 N (29s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (3s) | 🔴 N (38s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (4s) | 🔴 N (36s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (8s) | 🟡 T/o (120s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
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

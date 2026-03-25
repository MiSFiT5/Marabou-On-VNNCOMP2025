# N2,6 — Property 4

> Single reference point verification report  
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_2_6_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0342, -0.0137, 0.0259, -0.0024, 0.0267]`
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
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (4s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (13s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (7s) | 🔴 N (22s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (8s) | 🔴 N (7s) | 🔴 N (28s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (5s) | 🔴 N (63s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (36s) | 🔴 N (95s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (14s) | 🔴 N (15s) | 🔴 N (100s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (14s) | 🔴 N (11s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (18s) | 🔴 N (52s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (22s) | 🔴 N (63s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (119s) | 🔴 N (112s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (34s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (48s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (77s) | 🟡 T/o (120s) |

### Target 2 (Weak Right)

*Can the network be fooled from class 1 (Weak Left) to class 2 (Weak Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (10s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (6s) | 🔴 N (4s) | 🔴 N (9s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (3s) | 🔴 N (2s) | 🔴 N (4s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (3s) | 🔴 N (7s) | 🔴 N (6s) | 🔴 N (27s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (6s) | 🔴 N (45s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (8s) | 🔴 N (33s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (15s) | 🔴 N (16s) | 🔴 N (99s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (16s) | 🔴 N (96s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (18s) | 🔴 N (11s) | 🔴 N (119s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (18s) | 🔴 N (64s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (61s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (109s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (34s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (35s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (64s) | 🟡 T/o (120s) |

### Target 3 (Strong Left)

*Can the network be fooled from class 1 (Weak Left) to class 3 (Strong Left) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (3s) | 🔴 N (10s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (5s) | 🔴 N (10s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (2s) | 🔴 N (23s) | 🔴 N (6s) | 🔴 N (34s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (1s) | 🔴 N (11s) | 🔴 N (6s) | 🔴 N (41s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (1s) | 🔴 N (5s) | 🔴 N (7s) | 🔴 N (24s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (27s) | 🟡 T/o (120s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (12s) | 🔴 N (15s) | 🔴 N (103s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (19s) | 🔴 N (10s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (1s) | 🔴 N (24s) | 🔴 N (66s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (16s) | 🔴 N (62s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (7s) | 🔴 N (97s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (35s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🟡 T/o (120s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (37s) | 🟡 T/o (120s) |

### Target 4 (Strong Right)

*Can the network be fooled from class 1 (Weak Left) to class 4 (Strong Right) within an ε-ball?*

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------|--------|--------|--------|--------|
| `none (baseline)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) | 🔴 N (1s) |
| `ALWAYS_OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (1s) |
| `ALWAYS_ON (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) | 🔴 N (0s) |
| `Impl L0→L1 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (3s) | 🔴 N (15s) |
| `Impl L0→L1 (α=0.95)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (4s) | 🔴 N (7s) |
| `Impl L0→L1 (α=0.99)` | 🔴 N (0s) | 🔴 N (2s) | 🔴 N (2s) | 🔴 N (3s) |
| `Impl L1→L2 (α=0.9)` | 🔴 N (1s) | 🔴 N (16s) | 🔴 N (7s) | 🔴 N (37s) |
| `Impl L1→L2 (α=0.95)` | 🔴 N (2s) | 🔴 N (14s) | 🔴 N (6s) | 🔴 N (37s) |
| `Impl L1→L2 (α=0.99)` | 🔴 N (2s) | 🔴 N (5s) | 🔴 N (9s) | 🔴 N (46s) |
| `Impl L2→L3 (α=0.9)` | 🔴 N (1s) | 🔴 N (14s) | 🔴 N (19s) | 🔴 N (99s) |
| `Impl L2→L3 (α=0.95)` | 🔴 N (1s) | 🔴 N (17s) | 🔴 N (15s) | 🔴 N (111s) |
| `Impl L2→L3 (α=0.99)` | 🔴 N (1s) | 🔴 N (19s) | 🔴 N (12s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.9)` | 🔴 N (0s) | 🔴 N (11s) | 🔴 N (55s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.95)` | 🔴 N (1s) | 🔴 N (18s) | 🔴 N (56s) | 🟡 T/o (120s) |
| `Impl L3→L4 (α=0.99)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (104s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.9)` | 🔴 N (1s) | 🔴 N (4s) | 🔴 N (32s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.95)` | 🔴 N (1s) | 🔴 N (2s) | 🔴 N (38s) | 🟡 T/o (120s) |
| `Impl L4→L5 (α=0.99)` | 🔴 N (1s) | 🔴 N (3s) | 🔴 N (31s) | 🟡 T/o (120s) |

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

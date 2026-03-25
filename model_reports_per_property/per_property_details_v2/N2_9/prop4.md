# N2,9 — Property 4

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_2_9_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0206, -0.0203, 0.0201, -0.0157, 0.0211]`
- **Query filter used in this report:** `class_id = midpoint prediction`, `center_source = property_midpoint[0]`, `sample_idx = 0`

## Dedup Rule

- Repeated logical experiments are merged after the midpoint filter.
- Duplicate key: same `target`, same `ε`, same experiment label, same `α`.
- Keep order: `A (full_rule)` < `B/L0→L1` < `B/L1→L2` < `B/L2→L3` < `B/L3→L4` < `B/L4→L5` < `C (impl_ablation)`.
- The report shows only the kept rows after this overwrite rule.

## Target Summary

| Target | Class Name | Max Verified ε | Winning kept experiments |
|--------|------------|----------------|--------------------------|
| 0 | Clear-of-Conflict | – | – |
| 2 | Weak Right | – | – |
| 3 | Strong Left | – | – |
| 4 | Strong Right | – | – |

**Overall:** after deduplication, this reference point is not fully verified at any tested ε.

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (2s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (2s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (2s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (7s) | N (10s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (5s) | N (8s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (6s) | N (15s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (3s) | N (6s) | N (30s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (3s) | N (5s) | N (29s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (6s) | N (31s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (3s) | N (60s) | N (87s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (3s) | N (35s) | N (79s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (3s) | N (53s) | N (72s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (3s) | N (8s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (3s) | N (9s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (4s) | N (15s) | N (105s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (33s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (5s) | N (5s) | N (32s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (4s) | N (7s) | N (42s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (5s) | N (8s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (5s) | N (8s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (5s) | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (14s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (8s) | N (21s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (7s) | N (17s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (10s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (66s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (17s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (15s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (44s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (38s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (42s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (20s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (19s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (13s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (49s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (47s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (41s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | N (10s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (11s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (56s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (54s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (54s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (8s) | N (18s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (19s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (7s) | N (13s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (66s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (59s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (6s) | N (63s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (5s) | N (20s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (10s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (12s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (16s) | N (94s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (10s) | N (102s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (8s) | N (88s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (10s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (11s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (6s) | N (11s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (11s) | N (95s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (13s) | N (103s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (17s) | N (88s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (5s) | N (19s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (4s) | N (12s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | N (11s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (8s) | N (57s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (73s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (63s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (5s) | N (11s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (9s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (5s) | N (39s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (5s) | N (52s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (32s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (11s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (8s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (7s) | N (10s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (5s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (6s) | N (13s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (6s) | N (10s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (46s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (46s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (45s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (3s) | N (12s) | N (72s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (3s) | N (23s) | N (74s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (3s) | N (44s) | N (78s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (4s) | N (14s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (4s) | N (9s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (3s) | N (11s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (42s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (41s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (2s) | N (5s) | N (6s) | N (52s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (8s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (8s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (11s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (8s) | N (16s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (14s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (7s) | N (29s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (9s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (15s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (7s) | N (11s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (6s) | N (68s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (43s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (43s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (43s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (13s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (9s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (49s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (37s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (47s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (12s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (14s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (58s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (74s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (53s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (49s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (7s) | N (21s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (16s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (6s) | N (14s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (15s) | N (47s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (56s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (53s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (14s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (7s) | N (11s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (14s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (14s) | N (90s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (16s) | N (110s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (10s) | N (96s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (12s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (24s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (11s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (12s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (11s) | N (111s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (16s) | N (95s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (7s) | N (11s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (5s) | N (11s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (10s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (7s) | N (81s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (42s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (44s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (4s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (11s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (5s) | N (36s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (5s) | N (82s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (5s) | N (40s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (11s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (8s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (6s) | T/o |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (5s) | N (14s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (4s) | N (5s) | N (10s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (5s) | N (9s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (4s) | N (4s) | N (38s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (38s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (40s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (4s) | N (55s) | N (66s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (3s) | N (22s) | N (73s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (4s) | N (17s) | N (75s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (3s) | N (12s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (7s) | N (10s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (4s) | N (13s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (36s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (5s) | N (5s) | N (35s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (6s) | N (7s) | N (43s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (9s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (13s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (6s) | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (12s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (5s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (9s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (5s) | N (9s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (17s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (7s) | N (17s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (6s) | N (14s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (46s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (5s) | N (41s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (49s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (8s) | N (10s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (10s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (39s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (33s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (44s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (62s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (6s) | N (55s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (6s) | N (58s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (10s) | N (57s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (7s) | N (49s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (18s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (20s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (59s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (6s) | N (64s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (63s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (11s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (13s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (13s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (8s) | N (96s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (18s) | N (93s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (10s) | N (83s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (12s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (13s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (8s) | N (9s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (15s) | N (115s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (10s) | N (84s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (18s) | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (8s) | N (10s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | N (9s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (5s) | N (32s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (5s) | N (39s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (5s) | N (43s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (68s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (5s) | N (21s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (5s) | N (9s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (9s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (86s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (5s) | N (40s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (97s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (11s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (11s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (4s) | N (13s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (5s) | N (8s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (5s) | N (10s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (43s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (43s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (4s) | N (42s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (2s) | N (17s) | N (69s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (2s) | N (47s) | N (85s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (5s) | N (37s) | N (67s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (5s) | N (9s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (3s) | N (9s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (4s) | N (12s) | N (115s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (35s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (34s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (4s) | N (6s) | N (28s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (5s) | N (10s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (9s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (5s) | N (17s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (16s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (10s) | N (14s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (4s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (9s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (8s) | N (22s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (15s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (16s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (38s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (39s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (45s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (8s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (8s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | N (49s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (4s) | N (45s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (4s) | N (46s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (12s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (10s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (18s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (58s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (62s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (63s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (7s) | N (18s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (7s) | N (13s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (6s) | N (23s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (66s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (6s) | N (61s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (7s) | N (51s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (42s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (8s) | N (14s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (12s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (11s) | N (97s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (9s) | N (99s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (12s) | N (91s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (12s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (32s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (10s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (12s) | N (86s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (17s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (10s) | N (100s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (7s) | N (6s) | N (12s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (5s) | N (12s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (9s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (87s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (66s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (70s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (7s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (55s) | N (9s) | N (11s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (13s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (37s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (5s) | N (34s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (6s) | N (34s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (5s) | N (27s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (9s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (10s) |

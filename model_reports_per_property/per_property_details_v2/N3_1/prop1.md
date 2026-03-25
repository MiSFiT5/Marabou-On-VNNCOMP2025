# N3,1 — Property 1

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_1_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **2** (Weak Right)
- **Network outputs at midpoint:** `[0.0278, 0.0234, -0.024, 0.0226, -0.0071]`
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
| 1 | Weak Left | – | – |
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
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (9s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (2s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (21s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (1s) | N (2s) | N (22s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (19s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (1s) | N (76s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (16s) | N (36s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (9s) | N (70s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (0s) | N (1s) | N (3s) | N (43s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (1s) | N (3s) | N (28s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (5s) | N (31s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (1s) | N (17s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (14s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (41s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (4s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (10s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (2s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (12s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (12s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (6s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (70s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (9s) | N (65s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (15s) | N (68s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (37s) | N (67s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (34s) | N (66s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (49s) | N (72s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (20s) | N (72s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (61s) | N (58s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (84s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (37s) | N (74s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (48s) | N (9s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (30s) | N (35s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (104s) | N (42s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (18s) | N (7s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (6s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (38s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (4s) | N (100s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (10s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (9s) | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (7s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (7s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | N (11s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (42s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (30s) | N (8s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (25s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (6s) | N (79s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (18s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (33s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (61s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (51s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (120s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (44s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | T/o | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (118s) | N (3s) |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (1s) | N (6s) | N (22s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (8s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (4s) | N (78s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (0s) | N (1s) | N (3s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (1s) | N (4s) | N (25s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (0s) | N (3s) | N (38s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (0s) | N (1s) | N (11s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (6s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (2s) | N (25s) | N (19s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (5s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (10s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (11s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (9s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (21s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (58s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (25s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (10s) | N (10s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (13s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (27s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (6s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (5s) | N (27s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (99s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (7s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (5s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (8s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (7s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (13s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (20s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (16s) | N (10s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (25s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | T/o | N (62s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (10s) | N (17s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (0s) | N (1s) | N (4s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (24s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (8s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (1s) | N (4s) | N (7s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (0s) | N (1s) | N (4s) | N (41s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (1s) | N (1s) | N (35s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (3s) | N (43s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (1s) | N (12s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (16s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (25s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (9s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (11s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (9s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (6s) | N (31s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (24s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (5s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (10s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (8s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (4s) | N (4s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (4s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (15s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (6s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (4s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (4s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (6s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (4s) | N (7s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (8s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (11s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (27s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (27s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (24s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (7s) | N (60s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (10s) | N (16s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (1s) | N (1s) | N (5s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (1s) | N (15s) | N (19s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (9s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (64s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (1s) | N (4s) | N (38s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (0s) | N (3s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (0s) | N (3s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (1s) | N (12s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (1s) | N (9s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (35s) | N (8s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (11s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (12s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (36s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (10s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (10s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (6s) | N (5s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (5s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (23s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (9s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (17s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (4s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (4s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (6s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (5s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (8s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (4s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (8s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (8s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (6s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (12s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (26s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (31s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (25s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | T/o | N (74s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (6s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (9s) | N (18s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |

# N2,5 — Property 1

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_2_5_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.026, -0.0187, 0.022, -0.0173, 0.0234]`
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
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (4s) | N (55s) | N (19s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (2s) | N (64s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (2s) | T/o | N (117s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (37s) | N (19s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (6s) | N (4s) | T/o |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | T/o | T/o |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (25s) | N (13s) | N (46s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (5s) | N (5s) | N (37s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (8s) | N (7s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (13s) | N (82s) | N (107s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | T/o | N (101s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (14s) | N (108s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (2s) | N (29s) | N (33s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | T/o | N (9s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | N (17s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (10s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (7s) | T/o | T/o |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (113s) | N (18s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (33s) | N (27s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | T/o | T/o |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (3s) | N (20s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (60s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (2s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (9s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (6s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (2s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (38s) | N (23s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (10s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (21s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (109s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | T/o | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (6s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (9s) | N (30s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (8s) | N (42s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (25s) | N (58s) | N (68s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (39s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (10s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (9s) | N (5s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (6s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (6s) | N (69s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (106s) | N (84s) | N (15s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (18s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (2s) | N (9s) | N (4s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (55s) | N (7s) | N (6s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (6s) | N (5s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (17s) | N (45s) | N (79s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (108s) | N (113s) | N (46s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | N (56s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (5s) | N (1s) | T/o | N (67s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (4s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (20s) | T/o | N (51s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (38s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (17s) | N (27s) | N (36s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (2s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | T/o | N (79s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | N (106s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (25s) | N (85s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (29s) | N (111s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (22s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (6s) | N (46s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (6s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (23s) | N (47s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (26s) | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (91s) | T/o | N (30s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (33s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (7s) | T/o | N (111s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (2s) | N (2s) | N (5s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (6s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (45s) | N (16s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (2s) | N (20s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (9s) | N (4s) | N (4s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (2s) | N (15s) | N (39s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (108s) | N (42s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (2s) | N (7s) | N (27s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (10s) | N (13s) | N (87s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | T/o | N (117s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (4s) | N (101s) | N (80s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | T/o | N (119s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (20s) | T/o | N (30s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (2s) | N (120s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (10s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (6s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | T/o |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (4s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (10s) | N (5s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (8s) | N (3s) | N (5s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (3s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (3s) | N (108s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (8s) | N (3s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (2s) | N (5s) | N (27s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (3s) | N (19s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (82s) | N (55s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (11s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (3s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (10s) | N (17s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (15s) | N (7s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | T/o | N (73s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (4s) | N (65s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (5s) | N (17s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (9s) | N (7s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (5s) | N (5s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (21s) | T/o | N (91s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (8s) | N (5s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (14s) | N (3s) | N (4s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (2s) | T/o | N (86s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | N (58s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (21s) | N (35s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (8s) | N (69s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (4s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (4s) | N (2s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | N (58s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | N (115s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | N (3s) | N (4s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (17s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (21s) | N (3s) | N (7s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (2s) | N (3s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | N (23s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (10s) | T/o | N (24s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (45s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (2s) | N (2s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (76s) | N (12s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | T/o | N (92s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | T/o | T/o |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (6s) | T/o | N (54s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | T/o | N (4s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (2s) | N (14s) | N (36s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (2s) | N (5s) | N (55s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (2s) | N (6s) | N (29s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (18s) | N (34s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | T/o | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (18s) | N (115s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (52s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (3s) | N (114s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | T/o | N (25s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (11s) | T/o | N (40s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (12s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (2s) | T/o | N (75s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | N (39s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | N (35s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (65s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (10s) | N (69s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (25s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | T/o | N (7s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (10s) | T/o | N (47s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (4s) | T/o | N (13s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (9s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (7s) | N (29s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | T/o | N (65s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (55s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (7s) | T/o | N (28s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (9s) | N (6s) | N (5s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (7s) | N (2s) | N (7s) | N (5s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | T/o | N (50s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (80s) | N (29s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (5s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (6s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (9s) | N (5s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (16s) | N (41s) | N (86s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (5s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (3s) | T/o | N (110s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (8s) | T/o | N (84s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (5s) | T/o | N (59s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (19s) | N (40s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (81s) | N (75s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (7s) | N (48s) | N (106s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (2s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (4s) | T/o | N (89s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | N (101s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | T/o | N (91s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (57s) | T/o | N (47s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | N (35s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (16s) | N (33s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (10s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (3s) | T/o | N (36s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (26s) | T/o | N (84s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | N (44s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (106s) | T/o | N (25s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | N (20s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | N (24s) |

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
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (2s) | N (2s) | N (20s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (2s) | N (3s) | N (7s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (7s) | N (3s) | N (6s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (32s) | N (19s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (5s) | N (2s) | N (28s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (3s) | N (3s) | N (45s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (6s) | N (9s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (3s) | N (7s) | T/o | N (8s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (6s) | N (7s) | N (35s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | T/o | N (100s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (2s) | N (18s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | T/o | T/o | N (23s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (31s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (9s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (9s) | N (2s) | N (14s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (11s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (114s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (3s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (4s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (4s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (11s) | N (5s) | N (19s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (3s) | N (6s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (3s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (8s) | N (4s) | N (26s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (3s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (1s) | N (3s) | N (6s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (47s) | N (61s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (28s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (3s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (5s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (6s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (7s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (28s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (9s) | N (5s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (11s) | N (6s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (6s) | N (6s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (7s) | N (4s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (15s) | T/o | N (18s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (5s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (7s) | T/o | N (55s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | T/o | N (62s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (18s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (7s) | N (82s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (13s) | N (3s) | N (7s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (4s) | N (2s) | N (32s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | N (60s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (5s) | N (8s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (1s) | N (3s) | N (6s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (2s) | N (3s) | N (6s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (30s) | N (38s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (2s) | N (62s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | N (49s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (15s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (2s) | N (3s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (7s) | T/o | N (30s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |

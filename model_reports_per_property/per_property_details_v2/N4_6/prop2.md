# N4,6 — Property 2

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_6_batch_2000.onnx`
- **Property:** prop2
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0308, -0.02, 0.0208, -0.0143, 0.0202]`
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
| 3 | Strong Left | 0.20 | `Impl L0→L1 (α=0.9)` [B/L0→L1] |
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
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (29s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (4s) | N (5s) | N (27s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (4s) | N (32s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (5s) | N (10s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (4s) | N (16s) | N (18s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (7s) | N (4s) | N (65s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (16s) | N (13s) | N (31s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (3s) | N (9s) | N (48s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (98s) | N (77s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (7s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (3s) | N (23s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (3s) | N (53s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (2s) | N (5s) | N (15s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (0s) | N (9s) | N (44s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (5s) | N (77s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (12s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (5s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (4s) | N (100s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (16s) | N (32s) | N (15s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (17s) | N (78s) | N (23s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (23s) | T/o | N (37s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (25s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (21s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (9s) | N (4s) | T/o |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (13s) | N (17s) | N (49s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (14s) | N (11s) | N (23s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (18s) | N (18s) | N (36s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (7s) | N (22s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (2s) | T/o | N (15s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (20s) | T/o | N (40s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (16s) | N (16s) | N (19s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (16s) | N (19s) | N (18s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (16s) | N (25s) | N (27s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (4s) | N (79s) | N (10s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (117s) | N (12s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (15s) | T/o | N (23s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (12s) | N (18s) | N (21s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (17s) | N (18s) | N (20s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (24s) | N (27s) | N (28s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (10s) | N (55s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (18s) | N (8s) | N (87s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (21s) | N (30s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (78s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (73s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (9s) | N (116s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (2s) | N (71s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (63s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (16s) | N (8s) | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (72s) | N (117s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (77s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (9s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (6s) | N (27s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (9s) | N (50s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (15s) | N (84s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (16s) | N (30s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (43s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (18s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (27s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (23s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (21s) | N (80s) | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (18s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (20s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (28s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (66s) | N (95s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (5s) | N (119s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (12s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (5s) | N (33s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (17s) | N (13s) | N (86s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (25s) | N (18s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (5s) | N (97s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (9s) | N (93s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (31s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (117s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (14s) | T/o | T/o |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (2s) | N (9s) | N (24s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (2s) | N (4s) | N (36s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (3s) | N (4s) | N (9s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (2s) | N (7s) | N (10s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (9s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | N (4s) | N (12s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (4s) | N (2s) | N (9s) | N (52s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (2s) | N (5s) | N (10s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (5s) | N (7s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (2s) | N (22s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (3s) | N (46s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (2s) | N (25s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (2s) | N (30s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (6s) | N (20s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (5s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (27s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (28s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (6s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (22s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (3s) | N (43s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (2s) | N (21s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (2s) | N (2s) | N (9s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (4s) | N (15s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (3s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (2s) | N (13s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (20s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (10s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (2s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (4s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (8s) | N (66s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (9s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (4s) | N (4s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (2s) | N (65s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (55s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (5s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (3s) | N (7s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (17s) | N (27s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (43s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (25s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (17s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (17s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (26s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (10s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (9s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (3s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `0.20`
- **Winning kept experiments:**
  - `Impl L0→L1 (α=0.9)` (implication-only (L0→L1)) from `B/L0→L1`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (46s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (6s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (4s) | Y (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (13s) | N (31s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (31s) | N (9s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (3s) | N (9s) | N (10s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (8s) | N (10s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (18s) | N (3s) | N (11s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (4s) | N (2s) | N (8s) | N (55s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (68s) | N (84s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (9s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (2s) | N (2s) | N (20s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (2s) | N (54s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (3s) | N (14s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (5s) | N (53s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (8s) | N (12s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (7s) | N (11s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (4s) | N (11s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (19s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (25s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (3s) | N (33s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (3s) | N (12s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (20s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (9s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (10s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (15s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (2s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (4s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (20s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (3s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (3s) | N (12s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (12s) | N (64s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (8s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (34s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (25s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (36s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (69s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (2s) | N (56s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (32s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (29s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (45s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (8s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (16s) | N (3s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (17s) | N (32s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (42s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (21s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (5s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (17s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (18s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (26s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (17s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (2s) | N (11s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (4s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (3s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (9s) | N (16s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (3s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (64s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (2s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (2s) | N (5s) | N (32s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (2s) | N (4s) | N (48s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (10s) | N (9s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (2s) | N (7s) | N (9s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (9s) | N (12s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | N (4s) | N (11s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (4s) | N (2s) | N (9s) | N (52s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (5s) | N (74s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (5s) | N (14s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (3s) | N (22s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (2s) | N (46s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (2s) | N (13s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (3s) | N (32s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (6s) | N (11s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (24s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (10s) | N (24s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (3s) | N (6s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (15s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (4s) | N (12s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (8s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (9s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (3s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (15s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (19s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (12s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (12s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (17s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (8s) | N (64s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (8s) | N (5s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (8s) | N (2s) | N (65s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (6s) | N (56s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (5s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (2s) | N (4s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (15s) | N (30s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (45s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (20s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (4s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (2s) | N (2s) | N (4s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (18s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (18s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (29s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (6s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (10s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (12s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (11s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (3s) | N (3s) |

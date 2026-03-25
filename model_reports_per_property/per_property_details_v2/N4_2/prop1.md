# N4,2 — Property 1

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_2_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0255, -0.018, 0.032, -0.0177, 0.0298]`
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
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (6s) | N (9s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (9s) | N (24s) | N (20s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (4s) | N (12s) | N (10s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (9s) | N (12s) | N (10s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (52s) | N (47s) | N (13s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (16s) | N (6s) | N (31s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (9s) | N (8s) | N (32s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (18s) | N (25s) | N (37s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (0s) | N (45s) | N (51s) | N (116s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (42s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | T/o | N (16s) | N (3s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (51s) | N (39s) | N (4s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (37s) | N (9s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (48s) | N (18s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (39s) | N (113s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (6s) | N (23s) | N (111s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (6s) | N (36s) | N (87s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (73s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (72s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | T/o | T/o | T/o |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (4s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (7s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (5s) | N (22s) | N (76s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (10s) | N (109s) | T/o |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (33s) | N (87s) | T/o |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (43s) | T/o | N (66s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | T/o | N (48s) | N (43s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (39s) | N (41s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (63s) | N (77s) | N (51s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (76s) | N (35s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (22s) | N (30s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (109s) | T/o | N (55s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | T/o | N (48s) | N (58s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | T/o | N (42s) | N (41s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (65s) | N (57s) | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (24s) | N (34s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (26s) | N (34s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (49s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (71s) | N (113s) | N (116s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (69s) | N (111s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (59s) | N (120s) | N (86s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (9s) | N (15s) | N (48s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (24s) | N (8s) | N (40s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (19s) | N (18s) | N (73s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (70s) | N (111s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (90s) | T/o | N (118s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (68s) | N (116s) | N (112s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (18s) | N (33s) | N (58s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (49s) | N (31s) | N (63s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (38s) | N (63s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (18s) | N (104s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (29s) | N (57s) | N (87s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | T/o | N (14s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | N (6s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | N (4s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | T/o | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | T/o | N (20s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | T/o | T/o | N (23s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (2s) | N (77s) | N (20s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (109s) | T/o | N (4s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | T/o | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (81s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (87s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (3s) | N (79s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (67s) | N (28s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (35s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (28s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (12s) | N (76s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (90s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (3s) | N (82s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (69s) | N (18s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (42s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (104s) | N (3s) |

### Target 2 (Weak Right)

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
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (7s) | N (3s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (6s) | T/o |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (1s) | N (6s) | N (6s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (13s) | N (11s) | N (6s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (2s) | N (3s) | N (13s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (11s) | N (5s) | N (17s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (27s) | N (5s) | N (35s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (26s) | N (40s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (20s) | N (61s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (32s) | T/o | N (25s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (17s) | N (50s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (0s) | N (1s) | N (40s) | N (5s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (14s) | N (14s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (19s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (4s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (6s) | N (33s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (13s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (106s) | N (74s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (24s) | N (29s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (26s) | N (12s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (29s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (5s) | N (35s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (68s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (43s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (12s) | N (4s) | N (4s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (3s) | N (5s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (7s) | N (86s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (46s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (6s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (14s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (35s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (29s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (18s) | N (13s) | N (46s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (10s) | N (21s) | N (72s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (24s) | N (66s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (11s) | N (3s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (23s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (14s) | N (4s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (23s) | N (91s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (36s) | N (48s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (37s) | N (63s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (20s) | N (32s) | N (29s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (57s) | N (79s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (22s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (37s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (2s) | N (3s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (20s) | N (35s) | N (11s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (2s) | N (2s) | N (5s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (2s) | N (3s) | N (8s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (22s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (25s) | N (6s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (15s) | N (26s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (25s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (13s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (3s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (23s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (27s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (11s) | N (22s) | N (4s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (42s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (14s) | N (9s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (3s) | N (4s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (7s) | N (6s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (8s) | N (5s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (17s) | N (56s) | N (17s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (4s) | N (8s) | N (17s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (4s) | N (32s) | N (12s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (39s) | N (81s) | N (14s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (11s) | N (14s) | N (39s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (8s) | N (13s) | N (26s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (51s) | N (24s) | N (34s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (0s) | N (20s) | N (71s) | N (92s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (30s) | N (66s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (4s) | T/o | N (97s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (0s) | N (64s) | N (20s) | N (5s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (23s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (2s) | N (35s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (17s) | N (112s) | N (95s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (7s) | N (110s) | N (98s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (7s) | N (105s) | N (118s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (8s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (82s) | T/o | N (16s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (25s) | T/o | N (66s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (23s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (14s) | N (11s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (103s) | N (81s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (13s) | T/o | T/o |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (14s) | T/o | N (97s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (14s) | T/o | N (60s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (51s) | N (71s) | N (50s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (41s) | N (69s) | N (78s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | T/o | N (46s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (9s) | N (84s) | N (82s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (15s) | T/o | N (77s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (18s) | T/o | N (97s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (51s) | N (77s) | N (84s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (55s) | N (67s) | N (101s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (52s) | N (102s) | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (10s) | N (61s) | N (46s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (23s) | N (54s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (47s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (13s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (14s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (17s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (11s) | N (8s) | N (38s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (19s) | N (25s) | N (66s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (44s) | N (28s) | N (66s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (15s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (16s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (17s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (27s) | N (81s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (49s) | N (28s) | N (56s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (55s) | N (35s) | N (66s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (22s) | N (76s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (29s) | N (85s) | N (95s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (5s) | T/o | N (107s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (42s) | N (88s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (98s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (33s) | N (93s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (28s) | T/o | N (90s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (2s) | T/o | N (99s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | T/o | N (111s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (4s) | N (107s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (22s) | N (97s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (105s) | N (10s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (43s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (43s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (3s) | N (47s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (69s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (96s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | T/o | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (30s) | N (7s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (42s) | N (9s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (46s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (24s) | N (6s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (25s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (98s) | N (4s) |

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
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (5s) | N (15s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (15s) | N (8s) | N (7s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (35s) | N (9s) | N (6s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (5s) | N (11s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (13s) | N (11s) | N (33s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (31s) | N (9s) | N (33s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (2s) | N (16s) | N (47s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (34s) | N (55s) | N (105s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (38s) | T/o | N (118s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (16s) | N (3s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (0s) | N (1s) | N (27s) | N (7s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (19s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (2s) | N (20s) | N (17s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (26s) | N (20s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (35s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (2s) | N (71s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (19s) | N (57s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (19s) | N (66s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (6s) | N (22s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (61s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (68s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (2s) | N (4s) | N (65s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (38s) | N (6s) | N (4s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (5s) | N (30s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (2s) | N (4s) | N (6s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (2s) | N (8s) | N (70s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (74s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (6s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (6s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (5s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (6s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (13s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (8s) | N (5s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (17s) | N (8s) | N (51s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (12s) | N (9s) | N (50s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (16s) | N (99s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (35s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (13s) | N (4s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (10s) | N (5s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (27s) | N (43s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (35s) | N (36s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (34s) | N (60s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (37s) | N (50s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (36s) | N (61s) | N (6s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (21s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (3s) | N (3s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (4s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (21s) | N (17s) | N (6s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (3s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (24s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (24s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (27s) | N (9s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (71s) | N (29s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (13s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (40s) | N (9s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (25s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (3s) | N (21s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (9s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (10s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (3s) | N (4s) |

# N3,5 — Property 4

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_5_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0401, 0.0468, 0.004, 0.0394, -0.0074]`
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
| 2 | Weak Right | – | – |
| 3 | Strong Left | – | – |

**Overall:** after deduplication, this reference point is not fully verified at any tested ε.

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (4s) | N (8s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (3s) | N (5s) | N (7s) | N (9s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (3s) | N (5s) | N (8s) | N (8s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (7s) | N (9s) | N (19s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (5s) | N (9s) | N (21s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (2s) | N (4s) | N (6s) | N (52s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (4s) | N (16s) | N (86s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (4s) | N (4s) | N (15s) | N (38s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (3s) | N (3s) | N (17s) | N (45s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (2s) | N (7s) | N (74s) | N (80s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (2s) | N (2s) | N (72s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (2s) | N (6s) | N (65s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | N (56s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (46s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (2s) | N (50s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (3s) | N (4s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (5s) | N (5s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (6s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (7s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (8s) | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (6s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (8s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (6s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (7s) | N (8s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (7s) | N (13s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (7s) | N (17s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (8s) | N (15s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (5s) | N (60s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (4s) | N (78s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (25s) | N (5s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (18s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (15s) | N (19s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (7s) | N (18s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (7s) | N (80s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (16s) | N (68s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (5s) | N (7s) | N (14s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (15s) | N (55s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (15s) | N (59s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (5s) | N (3s) | N (16s) | N (52s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (7s) | N (20s) | N (77s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (6s) | N (21s) | N (90s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (26s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (9s) | N (100s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (11s) | N (53s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (18s) | N (65s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (23s) | N (77s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (6s) | N (25s) | N (88s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (22s) | N (73s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (3s) | N (5s) | N (62s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (3s) | N (5s) | N (66s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (2s) | N (4s) | N (67s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (6s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (5s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (77s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (6s) | N (64s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (5s) | N (58s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (3s) | N (6s) | N (55s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (6s) | N (93s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (68s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (29s) | N (45s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (41s) | N (6s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (40s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (43s) | N (6s) | N (115s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (4s) | N (55s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (12s) | N (47s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (46s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (43s) | N (5s) | N (103s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (4s) | N (58s) | N (7s) | N (109s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (46s) | N (5s) | N (107s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (3s) | N (47s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (44s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (4s) | N (5s) | N (113s) |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (4s) | N (7s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (3s) | N (5s) | N (7s) | N (10s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (3s) | N (5s) | N (8s) | N (10s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (3s) | N (18s) | N (9s) | N (20s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (6s) | N (8s) | N (52s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (2s) | N (5s) | N (5s) | N (58s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (3s) | N (4s) | N (18s) | N (81s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (2s) | N (3s) | N (15s) | N (37s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (4s) | N (12s) | N (49s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (2s) | N (6s) | N (79s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (2s) | N (15s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (2s) | N (8s) | N (70s) | N (119s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | N (41s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (3s) | N (42s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (3s) | N (47s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (5s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (6s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (3s) | N (6s) | N (6s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (7s) | N (10s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (7s) | N (10s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (4s) | N (4s) | N (5s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (4s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (7s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (7s) | N (10s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (7s) | N (9s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (5s) | N (8s) | N (15s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (8s) | N (14s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (9s) | N (17s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (4s) | N (25s) | N (6s) | N (77s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (19s) | N (6s) | N (87s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (61s) | N (5s) | N (96s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (8s) | N (14s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (10s) | N (16s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (10s) | N (16s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (5s) | N (91s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (95s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (7s) | N (13s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (4s) | N (17s) | N (54s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (16s) | N (56s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (15s) | N (46s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (7s) | N (23s) | N (93s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (7s) | N (24s) | N (87s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (9s) | N (19s) | N (96s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (4s) | N (9s) | N (98s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (3s) | N (9s) | N (52s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (10s) | N (57s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (26s) | N (87s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (24s) | N (97s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (24s) | N (86s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (3s) | N (5s) | N (48s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (3s) | N (5s) | N (61s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (3s) | N (5s) | N (60s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (5s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (115s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (5s) | N (66s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (5s) | N (58s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (5s) | N (59s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (6s) | N (72s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (80s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (32s) | N (45s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (52s) | N (5s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | N (39s) | N (6s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (60s) | N (6s) | N (119s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (5s) | N (47s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (52s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (50s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (4s) | N (43s) | N (7s) | N (120s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (43s) | N (5s) | N (109s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | T/o | N (6s) | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (5s) | N (44s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (5s) | N (46s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (5s) | N (5s) | N (111s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (4s) | N (6s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (3s) | N (5s) | N (6s) | N (9s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (3s) | N (4s) | N (7s) | N (8s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (3s) | N (7s) | N (8s) | N (22s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (5s) | N (8s) | N (50s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (4s) | N (6s) | N (32s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (3s) | N (18s) | N (78s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (19s) | N (50s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (4s) | N (3s) | N (16s) | N (46s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (3s) | N (6s) | N (77s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (2s) | N (14s) | N (93s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (3s) | N (4s) | N (60s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | N (40s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (3s) | N (45s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (2s) | N (52s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (6s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (3s) | N (7s) | N (6s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (11s) | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (8s) | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (8s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (5s) | N (5s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (5s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (5s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (7s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (6s) | N (9s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (8s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (7s) | N (109s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (8s) | N (112s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (7s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (25s) | N (5s) | N (85s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (15s) | N (89s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (28s) | N (4s) | N (61s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (7s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (8s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (9s) | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (5s) | N (98s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (6s) | N (84s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (8s) | N (13s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (20s) | N (55s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (6s) | N (5s) | N (14s) | N (59s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (5s) | N (4s) | N (13s) | N (57s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (24s) | N (86s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (21s) | N (79s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (20s) | N (83s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (9s) | N (91s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (14s) | N (55s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (12s) | N (64s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (24s) | N (91s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (20s) | N (87s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (5s) | N (7s) | N (26s) | N (85s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (5s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (2s) | N (5s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (3s) | N (6s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (5s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (4s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (84s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (5s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (6s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (6s) | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (84s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (77s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (30s) | N (49s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (59s) | N (5s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (43s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (43s) | N (7s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (6s) | N (52s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (4s) | N (3s) | N (51s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (4s) | N (47s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (51s) | N (6s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | N (58s) | N (7s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (50s) | N (7s) | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (4s) | N (48s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (45s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (6s) | T/o |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (3s) | N (5s) | N (7s) | N (9s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (3s) | N (5s) | N (7s) | N (9s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (2s) | N (5s) | N (8s) | N (9s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (5s) | N (10s) | N (22s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (3s) | N (5s) | N (8s) | N (69s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (2s) | N (5s) | N (5s) | N (31s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (5s) | N (4s) | N (14s) | N (53s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (3s) | N (15s) | N (51s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (3s) | N (4s) | N (16s) | N (53s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (2s) | N (7s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (2s) | N (30s) | N (80s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (3s) | N (4s) | N (69s) | N (112s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | N (44s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (12s) | N (43s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (48s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (7s) | N (8s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (4s) | N (5s) | N (6s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (7s) | N (10s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (6s) | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (7s) | N (10s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (5s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (7s) | N (9s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (6s) | N (9s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (8s) | N (9s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (6s) | N (16s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (16s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (9s) | N (16s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (4s) | N (59s) | N (7s) | N (92s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (67s) | N (4s) | N (59s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (4s) | N (5s) | N (17s) | N (92s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (7s) | N (13s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (7s) | N (16s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (7s) | N (20s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (5s) | N (61s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (5s) | N (104s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (49s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (15s) | N (51s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (16s) | N (59s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (14s) | N (60s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | N (7s) | N (27s) | N (93s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (7s) | N (17s) | N (89s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (24s) | N (96s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (4s) | N (11s) | N (107s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (12s) | N (57s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (12s) | N (61s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (25s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (6s) | N (20s) | N (79s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (6s) | N (22s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (3s) | N (5s) | N (64s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (3s) | N (5s) | N (54s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (6s) | N (65s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (5s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (7s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (4s) | N (5s) | N (90s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (4s) | N (57s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (3s) | N (6s) | N (63s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (2s) | N (5s) | N (56s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (81s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (82s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (30s) | N (44s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (37s) | N (6s) | N (109s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (57s) | N (7s) | N (112s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (53s) | N (6s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (4s) | N (49s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (5s) | N (50s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (47s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (56s) | N (6s) | N (101s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (50s) | N (6s) | N (107s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (54s) | T/o | N (114s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (50s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | N (4s) | N (50s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (5s) | N (118s) |

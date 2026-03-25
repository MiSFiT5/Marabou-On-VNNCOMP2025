# N1,1 — Property 4

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_1_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.2353, 0.2429, 0.2497, 0.1913, 0.2096]`
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
| 4 | Strong Right | – | – |

**Overall:** after deduplication, this reference point is not fully verified at any tested ε.

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (2s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (6s) | N (8s) | N (16s) | N (17s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (4s) | N (9s) | N (16s) | N (19s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (6s) | N (7s) | N (18s) | N (20s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (5s) | N (7s) | N (35s) | N (49s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (6s) | N (14s) | N (31s) | N (49s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (6s) | N (11s) | N (30s) | N (64s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (5s) | N (12s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (8s) | N (17s) | T/o | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (12s) | N (67s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (4s) | N (90s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (4s) | N (103s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (8s) | N (23s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (5s) | N (3s) | N (4s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (8s) | N (16s) | N (17s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (5s) | N (10s) | N (17s) | N (26s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (4s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (5s) | N (7s) | N (11s) | N (19s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (5s) | N (10s) | N (11s) | N (17s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (5s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (9s) | N (20s) | N (16s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (7s) | N (13s) | N (61s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (3s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (5s) | N (9s) | N (11s) | N (23s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (14s) | N (11s) | N (16s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (10s) | N (19s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (7s) | N (13s) | N (43s) | N (62s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (12s) | N (48s) | N (57s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (85s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (8s) | N (14s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (8s) | N (13s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (13s) | N (19s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (6s) | N (11s) | N (42s) | N (66s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (12s) | N (92s) | N (110s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (44s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (8s) | N (16s) | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (10s) | N (16s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (2s) | N (8s) | N (57s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (13s) | N (8s) | N (31s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (21s) | N (10s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (9s) | N (39s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (21s) | N (26s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (2s) | N (8s) | N (70s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (14s) | N (7s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (19s) | N (7s) | N (25s) | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (8s) | N (25s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (5s) | N (24s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (4s) | N (47s) | T/o | N (48s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (12s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (11s) | N (84s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (6s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (6s) | N (25s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (6s) | N (29s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (47s) | T/o | N (46s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (12s) | T/o | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (5s) | N (78s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (13s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (5s) | N (34s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (6s) | N (37s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (28s) | N (5s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (8s) | N (6s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (9s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (25s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (82s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | T/o | N (45s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (5s) | N (7s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (6s) | N (8s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (7s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (25s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (28s) | N (21s) | T/o | T/o |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (79s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (2s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (1s) | N (15s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (4s) | N (8s) | N (12s) | N (26s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (4s) | N (8s) | N (15s) | N (19s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (4s) | N (9s) | N (17s) | N (17s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (6s) | N (12s) | N (37s) | N (50s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (6s) | N (14s) | N (34s) | N (50s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (6s) | N (13s) | N (29s) | N (47s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (5s) | N (16s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (9s) | N (19s) | T/o | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (11s) | N (18s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (4s) | N (100s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (10s) | N (99s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (8s) | N (22s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (74s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (4s) | N (2s) | N (4s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (14s) | N (8s) | N (18s) | N (21s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (8s) | N (18s) | N (116s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (4s) | N (6s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (7s) | N (8s) | N (12s) | N (45s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (5s) | N (7s) | N (11s) | N (17s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (4s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (8s) | N (13s) | N (19s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (5s) | N (7s) | N (15s) | N (18s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (3s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (5s) | N (10s) | N (11s) | N (19s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (7s) | N (8s) | N (9s) | N (29s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (11s) | N (24s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (6s) | N (13s) | N (35s) | N (59s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (12s) | N (37s) | N (58s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (2s) | N (4s) | N (49s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (8s) | N (16s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (7s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (11s) | N (27s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (11s) | N (40s) | N (65s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (10s) | N (43s) | N (65s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (2s) | N (5s) | N (59s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (7s) | N (15s) | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (6s) | N (14s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (2s) | N (89s) | N (57s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (13s) | N (8s) | N (28s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (21s) | N (9s) | N (31s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (7s) | N (19s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (7s) | N (20s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | N (2s) | N (87s) | N (54s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (13s) | N (7s) | N (23s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (19s) | N (7s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (7s) | N (20s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (6s) | N (22s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (5s) | N (43s) | T/o | N (52s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (10s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (12s) | N (93s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (7s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (5s) | N (25s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (5s) | N (30s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (40s) | T/o | N (46s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (10s) | T/o | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (5s) | N (71s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (15s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (5s) | N (30s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (6s) | N (31s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (5s) | N (6s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (5s) | N (6s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (7s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (27s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (51s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | T/o | N (45s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (6s) | N (22s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (5s) | N (8s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (8s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (22s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (41s) | N (17s) | T/o | T/o |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (3s) | N (1s) | N (1s) | N (2s) |
| `none (baseline) [α=0.99]` | baseline | N (2s) | N (1s) | N (1s) | N (2s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (4s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (5s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (4s) | N (8s) | N (14s) | N (26s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (4s) | N (9s) | N (10s) | N (18s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (4s) | N (8s) | N (15s) | N (22s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (6s) | N (11s) | N (41s) | N (46s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (5s) | N (13s) | N (32s) | N (52s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (6s) | N (13s) | N (36s) | N (56s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (5s) | N (11s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (9s) | N (17s) | T/o | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (43s) | N (19s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (17s) | N (94s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (4s) | N (105s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (3s) | N (23s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (10s) | N (15s) | N (19s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (5s) | N (8s) | N (14s) | N (17s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (3s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (5s) | N (18s) | N (11s) | N (21s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (5s) | N (13s) | N (11s) | N (23s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (6s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (5s) | N (8s) | N (12s) | N (19s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (7s) | N (7s) | N (16s) | N (17s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (4s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (6s) | N (13s) | N (10s) | N (19s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (9s) | N (18s) | N (12s) | N (21s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (11s) | N (19s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (11s) | N (40s) | N (63s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (9s) | N (12s) | N (31s) | N (51s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (2s) | N (5s) | N (82s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (8s) | N (13s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (6s) | N (7s) | N (13s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (13s) | N (17s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (11s) | N (31s) | N (59s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (6s) | N (10s) | N (43s) | N (52s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (46s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (10s) | N (15s) | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (5s) | N (7s) | N (15s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (2s) | N (9s) | N (59s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (16s) | N (7s) | N (23s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (17s) | N (7s) | N (25s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (8s) | N (22s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (5s) | N (22s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (2s) | N (96s) | N (61s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (14s) | N (8s) | N (25s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (21s) | N (9s) | N (28s) | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (6s) | N (26s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (6s) | N (23s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (40s) | T/o | N (50s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (11s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (12s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (7s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (5s) | N (24s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (7s) | N (24s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (44s) | T/o | N (46s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (7s) | T/o | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (5s) | N (74s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (10s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (4s) | N (34s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (6s) | N (44s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | T/o | N (46s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (5s) | N (5s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | N (6s) | T/o | N (119s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (9s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (22s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (41s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (5s) | N (7s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (6s) | N (7s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (8s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (27s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (28s) | N (15s) | T/o | T/o |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (19s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | T/o |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (5s) | N (29s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (19s) | N (6s) | N (18s) | N (16s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (70s) | N (8s) | N (13s) | N (19s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (9s) | N (7s) | N (12s) | N (28s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (10s) | N (10s) | N (55s) | N (83s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (5s) | N (13s) | N (24s) | N (48s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (6s) | N (11s) | N (34s) | N (40s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (6s) | N (10s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (3s) | N (20s) | T/o | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (13s) | N (15s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (6s) | N (82s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (6s) | N (113s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (4s) | N (22s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (4s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (6s) | N (8s) | N (29s) | N (17s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (7s) | N (8s) | N (17s) | N (28s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (67s) | N (6s) | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (6s) | N (45s) | T/o | N (26s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (7s) | N (62s) | N (19s) | N (37s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (14s) | N (2s) | N (5s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (15s) | N (19s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (6s) | N (9s) | N (16s) | N (61s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (37s) | N (4s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (6s) | T/o | N (10s) | N (21s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (6s) | N (79s) | N (11s) | N (20s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (14s) | N (19s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (6s) | N (11s) | N (39s) | N (63s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (6s) | N (10s) | N (32s) | N (59s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (4s) | N (85s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (7s) | N (7s) | N (14s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (8s) | N (9s) | N (16s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (10s) | N (21s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (6s) | N (7s) | N (33s) | N (63s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (4s) | N (9s) | N (38s) | N (77s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (44s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (5s) | N (63s) | N (18s) | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (7s) | N (7s) | N (14s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (2s) | N (7s) | N (62s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (12s) | N (8s) | N (23s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (18s) | N (8s) | N (27s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (6s) | N (23s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (6s) | N (21s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | N (2s) | N (9s) | N (54s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (13s) | N (7s) | N (30s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (21s) | N (7s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (6s) | N (23s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (6s) | N (55s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (4s) | N (39s) | T/o | N (45s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (12s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (6s) | N (89s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (7s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (4s) | N (26s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (9s) | N (23s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (39s) | T/o | N (49s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (7s) | T/o | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (11s) | N (82s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (9s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (33s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (6s) | N (30s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | N (84s) | N (47s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (9s) | N (7s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | N (9s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (8s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (24s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (45s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (6s) | N (8s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (27s) | N (10s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (7s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (26s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (27s) | N (17s) | T/o | T/o |

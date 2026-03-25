# N4,2 — Property 4

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_2_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.2734, 0.2745, 0.2616, 0.2598, 0.2076]`
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
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (94s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (78s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (29s) | N (82s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (2s) | N (84s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (20s) | T/o | N (104s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (19s) | T/o | N (104s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (60s) | N (32s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (3s) | N (47s) | N (66s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (4s) | N (86s) | N (14s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (3s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (3s) | N (12s) | N (57s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (12s) | N (57s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (2s) | N (9s) | N (88s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (36s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (54s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (61s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (17s) | N (24s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (22s) | N (21s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (38s) | N (19s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | T/o | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (19s) | N (62s) | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (23s) | T/o | N (84s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (26s) | N (17s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (18s) | N (57s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (22s) | N (25s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (21s) | N (48s) | T/o |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (20s) | N (65s) | T/o |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (20s) | N (51s) | T/o |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (111s) | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (49s) | N (25s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (27s) | N (22s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (31s) | N (24s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | N (9s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | N (9s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (9s) | T/o | N (4s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (29s) | N (19s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (23s) | N (30s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (31s) | N (56s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (6s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (4s) | N (2s) | N (72s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (80s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (6s) | N (97s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (38s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (10s) | N (53s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (10s) | N (45s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (2s) | N (83s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (85s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (88s) | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (63s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (56s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (47s) | N (110s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (88s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (104s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (101s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (34s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (40s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (49s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (91s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (118s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (41s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (44s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (54s) | T/o | T/o |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | T/o | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (1s) | N (15s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (6s) | N (2s) | N (65s) | N (28s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (6s) | N (9s) | N (72s) | N (7s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (9s) | N (74s) | N (5s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (3s) | N (61s) | N (28s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (3s) | N (73s) | N (35s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (84s) | N (13s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (4s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (8s) | N (9s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (7s) | N (12s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (8s) | N (12s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (49s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (54s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (50s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (10s) | T/o | N (15s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (9s) | T/o | N (14s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (9s) | T/o | N (15s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (2s) | N (83s) | N (49s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (5s) | N (12s) | T/o | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (9s) | N (79s) | N (16s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (4s) | N (9s) | T/o | N (16s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (9s) | T/o | N (16s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (9s) | T/o | N (20s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (8s) | N (76s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (68s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (9s) | N (87s) | N (9s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (10s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (4s) | N (4s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (22s) | N (21s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (23s) | N (21s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (33s) | N (22s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (13s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (5s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (36s) | N (23s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (34s) | N (27s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (6s) | N (3s) | N (36s) | N (24s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (4s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (4s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (4s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (4s) | N (5s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (89s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (90s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (96s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (70s) | N (107s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (4s) | N (12s) | N (70s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (5s) | N (12s) | N (76s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (85s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (4s) | N (5s) | N (69s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (104s) | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (7s) | N (79s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (8s) | N (75s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (4s) | N (5s) | N (84s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (32s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (41s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (49s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (104s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (102s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (45s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (46s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (48s) | T/o | T/o |

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
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (16s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (3s) | N (67s) | N (7s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (3s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (3s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (3s) | N (31s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (10s) | N (73s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | N (4s) | N (13s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (11s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (11s) | T/o | N (63s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (11s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (3s) | N (35s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (2s) | N (33s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (2s) | N (31s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (43s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (43s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (50s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (25s) | N (68s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (4s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (12s) | N (26s) | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (11s) | N (35s) | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (14s) | N (62s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (14s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (12s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (8s) | N (14s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (21s) | T/o | N (25s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (26s) | T/o | N (80s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (41s) | T/o | N (4s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (29s) | N (10s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (42s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (27s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (56s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (31s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (9s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (11s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (11s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (22s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (48s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (53s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (11s) | T/o | N (106s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (11s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (11s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (33s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (53s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (3s) | N (72s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (12s) | N (44s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (51s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (48s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (89s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (29s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (97s) | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (45s) | N (87s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (47s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (63s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (102s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (101s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (38s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (35s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (49s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (110s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (118s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (108s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (43s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (51s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (39s) | T/o | T/o |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | T/o | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | T/o | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | T/o | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (17s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (97s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (7s) | N (84s) | N (8s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (8s) | N (83s) | N (8s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (4s) | N (80s) | N (41s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (6s) | N (116s) | N (59s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (4s) | N (86s) | N (81s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (10s) | T/o | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (10s) | T/o | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (5s) | N (14s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (11s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (4s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (36s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (40s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (49s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (8s) | T/o | N (18s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (9s) | T/o | N (16s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (9s) | T/o | N (15s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (65s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (8s) | T/o | N (12s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (8s) | N (81s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (7s) | T/o | N (14s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (12s) | T/o | N (15s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (8s) | T/o | N (17s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (8s) | N (82s) | N (10s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (77s) | N (22s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (8s) | N (78s) | N (9s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (6s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (106s) | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (10s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (91s) | N (57s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (101s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (113s) | N (76s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (9s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (86s) | N (83s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (97s) | N (107s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (8s) | N (113s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (8s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (9s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (9s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (6s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (11s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (18s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (5s) | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (6s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (26s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (9s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (22s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | T/o | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | T/o | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | T/o | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (11s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (5s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (99s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (118s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (43s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (41s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (66s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (112s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (104s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (48s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (49s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (47s) | T/o | T/o |

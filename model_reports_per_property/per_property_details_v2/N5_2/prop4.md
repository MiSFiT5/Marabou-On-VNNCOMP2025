# N5,2 — Property 4

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_5_2_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.2537, 0.286, 0.2029, 0.282, 0.1458]`
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
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (2s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (11s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (6s) | N (2s) | N (10s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (10s) | N (3s) | N (9s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (15s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (15s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | N (4s) | N (11s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (6s) | N (24s) | N (39s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (5s) | N (12s) | N (22s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (7s) | N (22s) | N (16s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (10s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (26s) | N (105s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (23s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (17s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (18s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (25s) | N (46s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (21s) | N (3s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (17s) | N (3s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (20s) | N (4s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (26s) | N (6s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (27s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (29s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (4s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (20s) | N (5s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (5s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (26s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (27s) | N (28s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (25s) | N (26s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (27s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (7s) | N (29s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | N (29s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (19s) | N (7s) | N (7s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (22s) | N (7s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (15s) | N (7s) | N (7s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (32s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (7s) | N (29s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (6s) | N (24s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (30s) | N (6s) | N (6s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (27s) | N (7s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (17s) | N (7s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (8s) | N (35s) | N (65s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (39s) | N (62s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (11s) | N (40s) | N (64s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (22s) | N (14s) | N (62s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (23s) | N (17s) | N (63s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (36s) | N (21s) | N (87s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (7s) | N (34s) | N (59s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (9s) | N (36s) | N (62s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (8s) | N (52s) | N (65s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (25s) | N (21s) | N (24s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (27s) | N (30s) | N (22s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (36s) | N (26s) | N (21s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (15s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (16s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (17s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | T/o | N (29s) | N (64s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (99s) | N (28s) | N (73s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (115s) | N (45s) | N (96s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (17s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (15s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (7s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (119s) | N (43s) | N (94s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | T/o | N (42s) | N (99s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (104s) | N (31s) | N (89s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (39s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (11s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (49s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (95s) | T/o | T/o |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (7s) | N (3s) | N (9s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (6s) | N (2s) | N (12s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (5s) | N (2s) | N (7s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (4s) | N (11s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (3s) | N (3s) | N (14s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (12s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (5s) | N (26s) | N (26s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (3s) | N (15s) | N (22s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (5s) | N (24s) | N (18s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (12s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (12s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (28s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (12s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (16s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (12s) | N (51s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (10s) | N (3s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (3s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (10s) | N (3s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (5s) | N (28s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (18s) | N (27s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (9s) | N (29s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (3s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (12s) | N (3s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (14s) | N (3s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (10s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (23s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (9s) | N (29s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (36s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (5s) | N (32s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (48s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (9s) | N (69s) | N (37s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (17s) | N (29s) | N (8s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (10s) | N (29s) | N (7s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (47s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (40s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (50s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (10s) | N (28s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (12s) | N (20s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (10s) | N (36s) | N (8s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (35s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (34s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (31s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (17s) | N (32s) | N (65s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (15s) | N (30s) | N (81s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (27s) | N (25s) | N (80s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (8s) | N (32s) | N (116s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (27s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (30s) | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (14s) | N (26s) | N (29s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (12s) | N (30s) | N (36s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (30s) | N (19s) | N (26s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (16s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (18s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (33s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | T/o | T/o | N (85s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | T/o | T/o | N (92s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (110s) | T/o | N (98s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (17s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (18s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (9s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (93s) | T/o | N (84s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (109s) | T/o | N (77s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (95s) | T/o | N (84s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (31s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (11s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (44s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (92s) | T/o | T/o |

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
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (1s) | N (2s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (1s) | N (3s) | N (11s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (2s) | N (3s) | N (6s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (13s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (14s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (5s) | N (15s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (2s) | N (23s) | N (22s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (2s) | N (26s) | N (22s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (2s) | N (18s) | N (20s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (0s) | N (32s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (11s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (28s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (17s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (4s) | N (15s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (8s) | N (49s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (9s) | N (3s) | N (54s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (11s) | N (4s) | N (61s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (11s) | N (3s) | N (53s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (22s) | N (16s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (19s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (15s) | N (73s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (11s) | N (4s) | N (57s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (9s) | N (3s) | N (55s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (10s) | N (5s) | N (56s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (17s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (17s) | N (11s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (23s) | N (5s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (23s) | N (58s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (23s) | N (65s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (23s) | N (61s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (20s) | N (40s) | N (6s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (13s) | N (39s) | N (8s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (12s) | N (35s) | N (6s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (22s) | N (69s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (19s) | N (66s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (22s) | N (55s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (11s) | N (35s) | N (7s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (13s) | N (36s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (39s) | N (8s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (34s) | N (66s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (51s) | N (62s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (8s) | N (39s) | N (69s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (17s) | N (57s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (23s) | N (66s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (18s) | N (21s) | N (78s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (38s) | N (66s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (46s) | N (58s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (45s) | N (54s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (20s) | N (24s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (20s) | N (26s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (26s) | N (27s) | N (20s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (16s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (15s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (21s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | T/o | T/o | N (85s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (108s) | T/o | N (94s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (94s) | T/o | N (100s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (16s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (17s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (9s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (116s) | T/o | N (89s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (113s) | T/o | N (98s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | T/o | T/o | N (85s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (29s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (11s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (50s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (84s) | T/o | T/o |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (2s) | N (14s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (1s) | N (3s) | N (14s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (2s) | N (106s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (4s) | N (15s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (15s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | N (5s) | N (17s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (2s) | N (22s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (18s) | N (118s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (4s) | N (31s) | N (29s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (12s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (17s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (32s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (11s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (26s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (12s) | N (50s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (4s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (3s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (9s) | N (5s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (17s) | N (36s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (10s) | N (37s) | N (12s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (11s) | N (49s) | N (64s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (8s) | N (3s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (2s) | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (4s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (15s) | N (39s) | N (14s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (12s) | N (49s) | N (15s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (13s) | N (42s) | N (13s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (32s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (8s) | N (29s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | N (26s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (67s) | N (7s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | T/o | N (8s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (7s) | T/o | N (8s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (6s) | N (26s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | N (35s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (8s) | N (36s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (8s) | N (89s) | N (7s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | T/o | N (8s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (81s) | N (25s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (58s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (58s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (57s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (17s) | N (35s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (12s) | N (32s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (41s) | N (52s) | N (90s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (51s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (60s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (55s) | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (12s) | N (29s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (16s) | N (32s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (21s) | N (50s) | N (43s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (13s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (16s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (27s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (53s) | T/o | N (82s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (43s) | T/o | N (74s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (62s) | T/o | N (90s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (18s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (24s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (7s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (57s) | T/o | N (88s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (65s) | T/o | N (100s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (62s) | T/o | N (77s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (114s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (27s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (4s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (107s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | N (11s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (41s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (87s) | T/o | T/o |

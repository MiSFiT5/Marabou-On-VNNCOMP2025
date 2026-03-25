# N5,1 — Property 3

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_5_1_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.1892, 0.1846, 0.1343, 0.1776, 0.1187]`
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
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | T/o |
| `ALWAYS_ON (α=0.9)` | unary-only | N (1s) | N (1s) | N (4s) | N (18s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (2s) | N (1s) | N (16s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (2s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (6s) | N (6s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (6s) | N (17s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (5s) | N (6s) | N (15s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (4s) | N (19s) | N (10s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (3s) | N (3s) | N (25s) | N (11s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (3s) | N (7s) | N (14s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (3s) | N (4s) | N (6s) | N (44s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (3s) | N (4s) | N (5s) | N (83s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (4s) | N (5s) | N (6s) | N (16s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (4s) | N (6s) | N (13s) | N (61s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (3s) | N (5s) | N (10s) | N (54s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (5s) | N (10s) | N (66s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (9s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (8s) | N (15s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (9s) | N (9s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (7s) | N (12s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (6s) | N (84s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (16s) | N (31s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (15s) | N (30s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (5s) | N (14s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (3s) | N (5s) | N (27s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (6s) | N (16s) | N (45s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (15s) | N (29s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (27s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (8s) | N (26s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (2s) | N (8s) | N (8s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (8s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (18s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (5s) | N (6s) | N (22s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (2s) | N (8s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (6s) | N (10s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (2s) | N (4s) | N (17s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (3s) | N (4s) | N (4s) | N (16s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (4s) | N (3s) | N (7s) | N (75s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (26s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (7s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (2s) | N (4s) | N (16s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (6s) | N (12s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (4s) | N (15s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (45s) | N (49s) | N (49s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (45s) | N (11s) | N (42s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (6s) | N (10s) | N (32s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (9s) | N (31s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (44s) | N (56s) | N (36s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (35s) | N (53s) | N (54s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (8s) | N (16s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (13s) | N (16s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (28s) | N (48s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (68s) | N (65s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (15s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (10s) | T/o | N (24s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (46s) | N (95s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | N (104s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (3s) | N (73s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (3s) | N (4s) | T/o |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (2s) | N (35s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (2s) | T/o |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (3s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (1s) | N (1s) | N (11s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (2s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (4s) | N (5s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (2s) | N (4s) | N (6s) | N (13s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (3s) | N (10s) | N (7s) | N (18s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (3s) | N (5s) | N (2s) | N (11s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (4s) | N (18s) | N (12s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (4s) | N (8s) | N (26s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (4s) | N (5s) | N (34s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (2s) | N (6s) | N (5s) | N (68s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (4s) | N (7s) | N (90s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (3s) | N (5s) | N (14s) | N (49s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (4s) | N (4s) | N (16s) | N (33s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (4s) | N (7s) | N (13s) | N (79s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (9s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (34s) | N (15s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (13s) | N (8s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (3s) | N (5s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (6s) | N (26s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (5s) | N (14s) | N (51s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (17s) | N (28s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (3s) | N (3s) | N (14s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (6s) | N (44s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (12s) | N (26s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (17s) | N (41s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (5s) | N (20s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (5s) | N (24s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (10s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (6s) | N (9s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (5s) | N (14s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (4s) | N (3s) | N (5s) | N (25s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (11s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (15s) | N (8s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (4s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (2s) | N (16s) | N (17s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (11s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (3s) | N (3s) | N (7s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (5s) | N (14s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (6s) | N (14s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (4s) | N (6s) | N (10s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (6s) | N (11s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (50s) | N (55s) | N (52s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (46s) | N (54s) | N (62s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (6s) | N (7s) | N (25s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (6s) | N (8s) | N (39s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (52s) | N (52s) | N (57s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (50s) | N (13s) | N (64s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (4s) | N (4s) | N (13s) | N (26s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (3s) | N (10s) | N (16s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (37s) | N (60s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (73s) | N (61s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (23s) | N (87s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (12s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (42s) | N (80s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | N (89s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (4s) | N (5s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (3s) | N (11s) | T/o |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (22s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | T/o |
| `ALWAYS_ON (α=0.9)` | unary-only | N (1s) | N (1s) | N (3s) | N (18s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (1s) | N (3s) | N (18s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (2s) | N (1s) | N (15s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (0s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (3s) | N (7s) | N (8s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (3s) | N (4s) | N (6s) | N (14s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (3s) | N (5s) | N (8s) | N (16s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (3s) | N (22s) | N (13s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (3s) | N (4s) | N (21s) | N (10s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (4s) | N (6s) | N (23s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (22s) | N (4s) | N (5s) | N (27s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (4s) | N (6s) | N (5s) | N (66s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (4s) | N (5s) | N (4s) | N (10s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (4s) | N (7s) | N (8s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (3s) | N (5s) | N (12s) | N (113s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (3s) | N (5s) | N (9s) | N (40s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (11s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (2s) | N (33s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (2s) | N (31s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (12s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (8s) | N (6s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (12s) | N (34s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (18s) | N (46s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (5s) | N (16s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (5s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (15s) | N (31s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (13s) | N (36s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (5s) | N (10s) | N (25s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (6s) | N (23s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (8s) | N (10s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (6s) | N (10s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (14s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (6s) | N (24s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (5s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (50s) | N (7s) | N (12s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (3s) | N (15s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (5s) | N (16s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (12s) | N (11s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (4s) | N (3s) | N (6s) | N (10s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (3s) | N (6s) | N (15s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (6s) | N (18s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (28s) | N (10s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (3s) | N (5s) | N (11s) | N (10s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (49s) | N (51s) | N (51s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (40s) | N (51s) | N (42s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (4s) | N (6s) | N (16s) | N (47s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (6s) | N (32s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (42s) | N (47s) | N (60s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (44s) | N (34s) | N (64s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (24s) | N (22s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (15s) | N (30s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (38s) | N (46s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (76s) | N (66s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (14s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (10s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (34s) | N (65s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | N (80s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (9s) | N (43s) | N (98s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (9s) | N (3s) | N (6s) | N (74s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (25s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (39s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | T/o |
| `ALWAYS_ON (α=0.9)` | unary-only | N (1s) | N (1s) | N (8s) | N (18s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (2s) | N (1s) | N (12s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (2s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (4s) | N (8s) | N (7s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (2s) | N (6s) | N (6s) | N (15s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (3s) | N (3s) | N (7s) | N (16s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (3s) | N (22s) | N (11s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (4s) | N (3s) | N (23s) | N (12s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (3s) | N (6s) | N (22s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (3s) | N (4s) | N (7s) | N (37s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (4s) | N (39s) | N (7s) | N (12s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (4s) | N (9s) | N (53s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (4s) | N (5s) | N (12s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (4s) | N (5s) | N (8s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (3s) | N (5s) | N (13s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (8s) | N (14s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (2s) | N (14s) | N (10s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (6s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (7s) | N (36s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (14s) | N (35s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (4s) | N (16s) | N (34s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (5s) | N (15s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (36s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (14s) | N (29s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (14s) | N (87s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (6s) | N (24s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | N (23s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (5s) | N (10s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (4s) | N (7s) | N (10s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (5s) | N (13s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (3s) | N (8s) | N (29s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (6s) | N (9s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (4s) | N (5s) | N (12s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (5s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (16s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (6s) | N (10s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (4s) | N (3s) | N (8s) | N (10s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (10s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (4s) | N (26s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (5s) | N (11s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (11s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (35s) | N (14s) | N (69s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (39s) | N (11s) | N (59s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (8s) | N (38s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (4s) | N (7s) | N (10s) | N (23s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (54s) | N (51s) | N (39s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (2s) | N (60s) | N (61s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (4s) | N (13s) | N (15s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (5s) | N (10s) | N (15s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (40s) | N (53s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (76s) | N (70s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (14s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (12s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (35s) | N (78s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | T/o | N (90s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | N (3s) | N (6s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (3s) | N (5s) | T/o |

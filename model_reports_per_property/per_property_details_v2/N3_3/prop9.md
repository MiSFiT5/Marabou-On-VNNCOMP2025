# N3,3 — Property 9

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_3_3_batch_2000.onnx`
- **Property:** prop9
- **Reference point (property midpoint):** `[-0.253748, -0.042972, -0.499204, -0.477273, -0.4375]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.2386, 0.2431, 0.2535, 0.1861, 0.2798]`
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
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (58s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (8s) | N (13s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (2s) | N (3s) | N (3s) | N (6s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (17s) | T/o |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (2s) | N (3s) | N (10s) | N (6s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (2s) | N (9s) | N (6s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (13s) | N (16s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (12s) | N (18s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (45s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (3s) | N (88s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (10s) | N (48s) | N (112s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (33s) | N (50s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (27s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (4s) | N (11s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (27s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (11s) | T/o |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (9s) | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | T/o |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (4s) | N (16s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (7s) | N (26s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (47s) | T/o |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (42s) | T/o |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (28s) | N (4s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (9s) | N (6s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (10s) | N (13s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (10s) | N (16s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (71s) | N (5s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (39s) | N (9s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (77s) | N (28s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (6s) | N (5s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (8s) | N (7s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (2s) | N (3s) | N (13s) | N (9s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (7s) | N (6s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (30s) | N (7s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (93s) | N (7s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (6s) | N (22s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (5s) | N (12s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (5s) | N (6s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (24s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (15s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (20s) | N (14s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | T/o | N (4s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (10s) | N (6s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (12s) | N (7s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (26s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (31s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (76s) | N (36s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | T/o | N (35s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | N (43s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (51s) | N (55s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | N (99s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (27s) | N (42s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (44s) | N (42s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (11s) | N (60s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (19s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (21s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (32s) | N (57s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (13s) | N (102s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (92s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | N (82s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | N (78s) |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (1s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (1s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | T/o |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (6s) | N (11s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (2s) | N (19s) | N (7s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (7s) | N (10s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (3s) | N (10s) | N (6s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (2s) | N (11s) | N (6s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (14s) | N (7s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (3s) | N (17s) | N (96s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (55s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (3s) | N (40s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (9s) | N (50s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (18s) | N (52s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (17s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (10s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (5s) | N (34s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (24s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (12s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (2s) | N (4s) | N (4s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (8s) | N (5s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (7s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (9s) | N (8s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (8s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (8s) | N (5s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (7s) | N (8s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (13s) | N (26s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (3s) | N (7s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (6s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (13s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (10s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (6s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (35s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (20s) | N (76s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (15s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (13s) | N (6s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (16s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (12s) | N (81s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (29s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (25s) | N (35s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (57s) | N (37s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | N (36s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | N (35s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (52s) | N (35s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (17s) | N (37s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (63s) | N (43s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | N (57s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (19s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (39s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (30s) | N (56s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (100s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (11s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (12s) | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | N (73s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | N (83s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (1s) | N (2s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (1s) | N (2s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (1s) | N (2s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (2s) | N (7s) | N (12s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (2s) | N (2s) | N (3s) | N (5s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (17s) | T/o |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (8s) | N (5s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (3s) | N (7s) | N (5s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (20s) | N (8s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (5s) | N (25s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (5s) | N (37s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (2s) | N (95s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (11s) | N (48s) | N (83s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (3s) | N (60s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (95s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (6s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (3s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (33s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | N (6s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (7s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (3s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (8s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (25s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (26s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (32s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (6s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (9s) | N (17s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (10s) | N (21s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (6s) | N (40s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (7s) | N (6s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (12s) | N (39s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (12s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (3s) | N (7s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (3s) | N (6s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (4s) | N (8s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (5s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (5s) | N (10s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (5s) | N (8s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (25s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (17s) | N (110s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (14s) | N (53s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (16s) | N (8s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (15s) | N (33s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (12s) | N (7s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (18s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (25s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (58s) | N (84s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | T/o | N (31s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | N (37s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (58s) | N (39s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (26s) | N (36s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (54s) | N (36s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (5s) | N (60s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (18s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (23s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (37s) | N (52s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (108s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (115s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (92s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | N (92s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | N (111s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (1s) | T/o |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | T/o |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (3s) | N (6s) | N (16s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (3s) | N (4s) | N (8s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (3s) | N (34s) | T/o |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (3s) | N (9s) | N (5s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (2s) | N (22s) | N (10s) | N (6s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (2s) | N (2s) | N (19s) | N (7s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (3s) | N (12s) | N (118s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (17s) | N (29s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (2s) | N (18s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (10s) | T/o | N (75s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (2s) | N (45s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (10s) | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (3s) | N (119s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (4s) | N (13s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (7s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (8s) | T/o |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (5s) | T/o |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (6s) | T/o |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (6s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (4s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (3s) | N (6s) | T/o |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (9s) | N (61s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (5s) | N (75s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (17s) | T/o |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (6s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (11s) | N (21s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (9s) | N (15s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (7s) | N (4s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (55s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (4s) | N (90s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (6s) | N (6s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (8s) | N (24s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (13s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (5s) | N (8s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (8s) | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | T/o | N (24s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (24s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (7s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (4s) | N (7s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (58s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (14s) | N (19s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (27s) | N (42s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (6s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (11s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (11s) | N (14s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (31s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (23s) | N (29s) | N (35s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (80s) | N (34s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | T/o | N (31s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | N (36s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (62s) | N (36s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | T/o | N (110s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (25s) | N (35s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (29s) | N (45s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (12s) | N (53s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (21s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (26s) | N (24s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (32s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (12s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (13s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (95s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (86s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (9s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (88s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |

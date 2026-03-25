# N4,5 — Property 2

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_5_batch_2000.onnx`
- **Property:** prop2
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **3** (Strong Left)
- **Network outputs at midpoint:** `[0.0422, -0.0147, 0.0209, -0.0208, 0.0245]`
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
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (2s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (6s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (1s) | N (4s) | N (20s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (1s) | N (3s) | N (29s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (2s) | N (17s) | N (17s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (1s) | T/o | N (14s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (8s) | N (14s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (1s) | T/o | N (14s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (3s) | N (9s) | N (19s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (7s) | N (9s) | N (22s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (4s) | N (9s) | N (17s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (0s) | N (2s) | N (10s) | N (108s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (14s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (2s) | N (86s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (13s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (22s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (14s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (10s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (2s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (22s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (27s) | N (12s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (38s) | N (15s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (23s) | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (24s) | N (118s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (24s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (102s) | N (12s) | N (18s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (8s) | N (56s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (27s) | N (48s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (26s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (25s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (27s) | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (10s) | N (47s) | N (38s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (48s) | N (45s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (2s) | T/o | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (7s) | N (17s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | T/o | N (18s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (8s) | N (22s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (11s) | N (40s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (14s) | N (19s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (15s) | N (70s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (9s) | N (18s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (2s) | N (9s) | N (20s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (9s) | N (23s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (10s) | N (18s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (2s) | N (9s) | N (22s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (14s) | N (19s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (24s) | N (32s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (24s) | N (34s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (26s) | N (40s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (13s) | N (20s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (12s) | N (23s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (8s) | N (26s) | N (26s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (23s) | N (60s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (25s) | N (65s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (33s) | N (34s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (11s) | N (21s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (13s) | N (23s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (12s) | N (24s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (38s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (5s) | N (38s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (40s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (34s) | N (18s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (18s) | N (10s) | N (12s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (3s) | N (24s) | N (21s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (9s) | N (44s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (4s) | N (43s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (40s) | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (20s) | N (16s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (3s) | N (26s) | N (18s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (18s) | N (26s) |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (2s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (2s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (2s) | N (2s) | N (5s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (1s) | N (2s) | N (8s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (1s) | N (3s) | N (12s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (1s) | N (4s) | N (16s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (6s) | N (3s) | N (8s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (1s) | N (17s) | N (63s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (1s) | N (7s) | N (13s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (1s) | N (7s) | N (16s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (3s) | T/o | N (21s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (3s) | N (9s) | N (21s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (1s) | N (9s) | N (19s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (4s) | N (8s) | N (20s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (0s) | N (2s) | N (11s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (3s) | N (23s) | N (97s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (4s) | N (111s) | N (73s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | T/o | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (8s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (11s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (3s) | N (14s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (27s) | N (24s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (3s) | T/o | N (6s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (32s) | N (106s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (31s) | N (102s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (33s) | N (107s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (2s) | N (14s) | N (40s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (11s) | N (40s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (49s) | N (50s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (36s) | N (118s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (3s) | N (35s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (56s) | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (20s) | T/o |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (3s) | N (22s) | T/o |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (48s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (8s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (8s) | N (19s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (7s) | N (21s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (11s) | N (21s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (10s) | N (18s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (10s) | N (22s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (7s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (8s) | N (20s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (8s) | N (23s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (10s) | N (18s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (10s) | N (26s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (11s) | N (23s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (16s) | N (28s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (18s) | N (28s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (19s) | N (34s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (4s) | N (11s) | N (24s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (22s) | N (20s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (13s) | N (22s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (16s) | N (28s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (15s) | N (52s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (20s) | N (79s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (10s) | N (27s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (10s) | N (20s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (13s) | N (23s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (34s) | N (20s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (10s) | N (18s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (21s) | N (29s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (3s) | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (29s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (35s) | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (17s) | N (22s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (16s) | N (19s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (19s) | N (21s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (14s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (2s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (2s) | N (4s) | N (4s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (1s) | N (4s) | N (4s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (1s) | N (2s) | N (12s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (1s) | N (6s) | N (14s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (1s) | N (7s) | N (16s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (2s) | N (8s) | N (13s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (1s) | N (8s) | N (20s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (1s) | N (8s) | N (21s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (1s) | N (9s) | N (20s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (5s) | N (66s) | N (114s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (3s) | N (22s) | N (119s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (1s) | N (88s) | N (84s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (6s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (6s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (5s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (13s) | N (12s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (7s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (5s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (4s) | N (21s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (7s) | N (15s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (7s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (18s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (19s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (18s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (19s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | N (7s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (21s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (17s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (20s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (3s) | N (17s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | N (22s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | N (19s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (4s) | N (29s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (3s) | N (33s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (4s) | N (37s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (22s) | N (24s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (10s) | N (20s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (2s) | N (11s) | N (25s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (64s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (3s) | N (29s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (34s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (10s) | N (20s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (10s) | N (23s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (12s) | N (25s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (25s) | N (19s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (10s) | N (18s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (2s) | N (28s) | N (31s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (11s) | N (15s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (18s) | N (18s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (24s) | N (33s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (1s) | N (4s) | N (7s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (1s) | N (3s) | N (7s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (1s) | N (2s) | N (9s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (1s) | N (7s) | N (13s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (1s) | N (8s) | N (15s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (1s) | N (8s) | N (15s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (0s) | N (1s) | N (8s) | N (17s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (1s) | N (9s) | N (18s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (1s) | N (10s) | N (19s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (1s) | N (10s) | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (9s) | N (14s) | N (113s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (82s) | N (99s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (3s) | N (6s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (5s) | N (15s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (18s) | N (14s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (3s) | N (5s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (3s) | N (14s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (4s) | N (14s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (4s) | N (9s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (18s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (19s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (20s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (20s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (19s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (18s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (18s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (20s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (3s) | N (20s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (4s) | N (18s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (3s) | N (18s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (28s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (33s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (3s) | N (36s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (12s) | N (23s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (24s) | N (23s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (11s) | N (24s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (3s) | N (76s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (31s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (35s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (10s) | N (22s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (11s) | N (21s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (14s) | N (25s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (6s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (3s) | N (5s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (36s) | N (18s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (11s) | N (16s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (27s) | N (23s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (3s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (15s) | N (29s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (2s) | N (17s) | N (17s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (23s) | N (36s) |

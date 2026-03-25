# N4,6 — Property 3

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_4_6_batch_2000.onnx`
- **Property:** prop3
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.49669, 0.4, 0.4]`
- **Network prediction:** class **1** (Weak Left)
- **Network outputs at midpoint:** `[0.0236, -0.0199, 0.0207, -0.0146, 0.0201]`
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
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (2s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (4s) | N (8s) | N (17s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (5s) | N (7s) | N (11s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (5s) | N (7s) | N (13s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (4s) | N (5s) | N (104s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (5s) | N (8s) | N (48s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (3s) | N (5s) | N (109s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (5s) | N (17s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (5s) | N (19s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (5s) | N (14s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (5s) | N (7s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (5s) | N (7s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (4s) | N (7s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | N (5s) | N (6s) | N (12s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (12s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (5s) | N (6s) | N (12s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (7s) | N (30s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (8s) | N (18s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (7s) | N (24s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (5s) | N (7s) | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (8s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (7s) | N (9s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (5s) | N (9s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (5s) | N (18s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (13s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (7s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (8s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (7s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (4s) | N (8s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (16s) | N (5s) | N (8s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (7s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (6s) | N (5s) | N (10s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (8s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (5s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (7s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (9s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (7s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (6s) | N (37s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (7s) | N (76s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (8s) | N (39s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (7s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (5s) | N (18s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (5s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (24s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (39s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (74s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (16s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (8s) | N (19s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (6s) | N (11s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (50s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (49s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (49s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (87s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (8s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | N (108s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (8s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (6s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (6s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (7s) | N (11s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (7s) | N (11s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (7s) | N (8s) | N (49s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (7s) | N (6s) | N (14s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (12s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (7s) | N (7s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (96s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (11s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (7s) | N (11s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (13s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (12s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (11s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (8s) | N (10s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (10s) | N (11s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (8s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (8s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (7s) | N (6s) | N (10s) |

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
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (2s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (4s) | N (7s) | N (13s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (5s) | N (7s) | N (9s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (5s) | N (5s) | N (11s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (4s) | N (6s) | N (99s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (5s) | N (6s) | T/o |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (4s) | N (7s) | N (26s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (4s) | N (18s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (2s) | N (4s) | N (17s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (4s) | N (32s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (4s) | N (6s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (6s) | N (6s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (5s) | N (7s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (6s) | N (5s) | N (12s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (5s) | N (8s) | N (11s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (5s) | N (8s) | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (9s) | N (18s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (9s) | N (19s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (27s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (7s) | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (7s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (9s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (8s) | N (10s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (4s) | N (7s) | N (11s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (8s) | N (9s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (6s) | N (15s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (10s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (8s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (8s) | N (9s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (7s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (31s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (7s) | N (6s) | T/o |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (5s) | N (10s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (41s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (5s) | N (7s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (5s) | N (7s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (6s) | N (45s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (25s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (10s) | N (20s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (6s) | N (19s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (6s) | N (15s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (47s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (35s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (53s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (6s) | N (18s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (5s) | N (17s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (4s) | N (5s) | N (12s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (31s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (46s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (62s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | N (10s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (6s) | N (9s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (10s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (6s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (6s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | N (9s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (4s) | N (5s) | N (9s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (9s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (5s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | N (13s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | N (10s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (12s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (8s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (9s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (6s) | N (7s) | N (12s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (9s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (9s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (8s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (12s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (18s) | N (12s) |

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
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (1s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (1s) | N (4s) | N (7s) | N (13s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (2s) | N (5s) | N (6s) | N (16s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (1s) | N (5s) | N (6s) | N (14s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (5s) | N (10s) | N (35s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (4s) | N (8s) | N (57s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (6s) | N (5s) | N (90s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (3s) | N (13s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (4s) | N (33s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (5s) | N (35s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (4s) | N (6s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (6s) | N (5s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (5s) | N (6s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (1s) | N (5s) | N (11s) | N (13s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (6s) | N (6s) | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (2s) | N (13s) | N (6s) | N (13s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (9s) | N (37s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (4s) | N (6s) | N (22s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (6s) | N (18s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (7s) | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (5s) | N (8s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (8s) | N (8s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (8s) | N (11s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (6s) | N (9s) | N (12s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (7s) | N (11s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (2s) | N (7s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (6s) | N (11s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (7s) | N (10s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (5s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (23s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (7s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (6s) | N (6s) | N (9s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (6s) | N (97s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (7s) | N (12s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (6s) | N (7s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (10s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (7s) | N (10s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (7s) | N (39s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (7s) | N (25s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (6s) | N (29s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (6s) | N (18s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (5s) | N (14s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (18s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (57s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (44s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (37s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (5s) | N (18s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (5s) | N (9s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (48s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (5s) | N (66s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (48s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (6s) | N (11s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (11s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (7s) | N (10s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (7s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (7s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (7s) | N (11s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (10s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (8s) | N (5s) | N (10s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (7s) | N (11s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (7s) | N (13s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (12s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (8s) | N (9s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (7s) | N (6s) | N (12s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (6s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (7s) | N (6s) | N (11s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (6s) | N (115s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (8s) | N (7s) | N (12s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (8s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (13s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (11s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (2s) | N (6s) | N (7s) | N (11s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (6s) | N (6s) | N (14s) |

### Target 4 (Strong Right)

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
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (1s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (2s) | N (4s) | N (7s) | N (15s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (1s) | N (4s) | N (8s) | N (10s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (2s) | N (6s) | N (7s) | N (12s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (4s) | N (4s) | N (43s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (1s) | N (5s) | N (6s) | T/o |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (1s) | N (5s) | N (6s) | N (105s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (4s) | N (57s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (5s) | N (29s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (1s) | N (4s) | N (30s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (4s) | N (8s) | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (5s) | N (5s) | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (2s) | N (6s) | N (10s) | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | N (6s) | N (9s) | N (11s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | N (5s) | N (7s) | N (9s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (6s) | N (7s) | N (10s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (8s) | N (21s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (7s) | N (19s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (9s) | N (16s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (7s) | N (9s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (8s) | N (7s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (6s) | N (9s) | N (7s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (5s) | N (8s) | N (10s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (1s) | N (3s) | N (8s) | N (11s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (2s) | N (5s) | N (7s) | N (11s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (6s) | N (8s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (7s) | N (7s) | N (7s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (1s) | N (7s) | N (7s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (8s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (7s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (5s) | N (21s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (5s) | N (6s) | N (9s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (7s) | N (6s) | N (11s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (11s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (6s) | N (22s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (6s) | N (8s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (4s) | N (5s) | N (21s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (5s) | N (7s) | N (45s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (7s) | N (81s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (1s) | N (6s) | N (8s) | N (31s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (12s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | N (16s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (5s) | N (15s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (51s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (53s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (7s) | N (33s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (3s) | N (5s) | N (16s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (6s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (3s) | N (6s) | N (9s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (52s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (4s) | N (51s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (43s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (8s) | N (9s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (6s) | N (9s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (7s) | N (10s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (7s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (6s) | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (7s) | N (7s) | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (4s) | N (8s) | N (13s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (6s) | N (6s) | N (10s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (1s) | N (5s) | N (6s) | N (10s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (7s) | N (13s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (2s) | N (5s) | N (9s) | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (6s) | N (8s) | N (14s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (18s) | N (9s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (10s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (8s) | N (7s) | N (12s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | N (5s) | N (8s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (5s) | N (7s) | N (10s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (10s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (5s) | N (10s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (12s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (6s) | N (7s) | N (13s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (1s) | N (4s) | N (8s) | N (12s) |

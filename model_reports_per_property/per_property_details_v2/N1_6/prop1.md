# N1,6 — Property 1

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_6_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **0** (Clear-of-Conflict)
- **Network outputs at midpoint:** `[-0.0194, -0.0175, -0.018, -0.0165, -0.0169]`
- **Query filter used in this report:** `class_id = midpoint prediction`, `center_source = property_midpoint[0]`, `sample_idx = 0`

## Dedup Rule

- Repeated logical experiments are merged after the midpoint filter.
- Duplicate key: same `target`, same `ε`, same experiment label, same `α`.
- Keep order: `A (full_rule)` < `B/L0→L1` < `B/L1→L2` < `B/L2→L3` < `B/L3→L4` < `B/L4→L5` < `C (impl_ablation)`.
- The report shows only the kept rows after this overwrite rule.

## Target Summary

| Target | Class Name | Max Verified ε | Winning kept experiments |
|--------|------------|----------------|--------------------------|
| 1 | Weak Left | 0.05 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L2→L3 [!A->B] (α=0.9)` [C] |
| 2 | Weak Right | 0.05 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L2→L3 [!A->B] (α=0.9)` [C] |
| 3 | Strong Left | 0.05 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L2→L3 [!A->B] (α=0.9)` [C] |
| 4 | Strong Right | 0.05 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L2→L3 [!A->B] (α=0.9)` [C] |

**Overall:** after deduplication, this reference point is fully verified up to **ε = 0.05**.

---

## Detailed Results Per Target

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (1s) | Y (66s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (1s) | Y (57s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (4s) | N (0s) | N (3s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | Y (1s) | N (2s) | N (9s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (2s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (11s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (1s) | N (8s) | N (30s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | Y (2s) | N (1s) | N (2s) | N (11s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (1s) | N (12s) | N (15s) | N (4s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (1s) | N (7s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (5s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (1s) | T/o | N (2s) | N (2s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (2s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (1s) | N (2s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (5s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (2s) | N (2s) | N (4s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (1s) | N (5s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (6s) | N (1s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (7s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (1s) | N (4s) | N (2s) | N (11s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | Y (4s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (8s) | N (2s) | N (4s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (10s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | Y (3s) | N (1s) | N (6s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (26s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (4s) | N (8s) | N (4s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (7s) | N (4s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (5s) | T/o | N (2s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (14s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (1s) | T/o | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (1s) | Y (67s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (1s) | Y (57s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (4s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | Y (1s) | N (2s) | N (13s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (3s) | N (6s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (2s) | N (10s) | N (31s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | Y (1s) | N (1s) | N (2s) | N (12s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (1s) | N (14s) | N (20s) | N (3s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (1s) | N (13s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (1s) | T/o | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (1s) | N (2s) | N (5s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (3s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (2s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (1s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (5s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (5s) | N (1s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (0s) | N (1s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (4s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (8s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (1s) | N (5s) | N (1s) | N (14s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (1s) | N (2s) | N (11s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (9s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | Y (4s) | N (1s) | N (8s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (8s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (7s) | N (7s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (8s) | N (4s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (3s) | T/o | N (1s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (2s) | T/o | N (6s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (7s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (3s) | N (3s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (1s) | Y (65s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (1s) | Y (57s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (4s) | N (0s) | N (4s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | Y (1s) | N (2s) | N (11s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (6s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (1s) | N (8s) | N (29s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | Y (1s) | N (2s) | N (2s) | N (10s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (1s) | N (14s) | N (18s) | N (4s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (1s) | N (12s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (3s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (1s) | T/o | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (1s) | N (0s) | N (2s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (1s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (7s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (6s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (5s) | N (1s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (4s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (7s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (1s) | N (4s) | N (2s) | N (15s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (1s) | N (1s) | N (3s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (4s) | N (3s) | N (10s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (15s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | Y (4s) | N (1s) | N (7s) | N (9s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (7s) | N (4s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (6s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (3s) | N (8s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (2s) | N (2s) | N (4s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (4s) | T/o | N (1s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (2s) | T/o | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (6s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (1s) | Y (65s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (1s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (1s) | Y (55s) | N (1s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (4s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | Y (1s) | N (1s) | N (12s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (8s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (2s) | N (6s) | N (103s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | Y (1s) | N (1s) | N (2s) | N (12s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (1s) | N (15s) | N (15s) | N (4s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (1s) | N (10s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (1s) | T/o | N (2s) | N (2s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (2s) | N (2s) | N (5s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (14s) | N (2s) | N (4s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (1s) | N (4s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (4s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (5s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (1s) | N (6s) | N (1s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (7s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (1s) | N (4s) | N (1s) | N (15s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (12s) | N (3s) | N (4s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (10s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | Y (3s) | N (5s) | N (7s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (8s) | N (4s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (4s) | N (7s) | N (4s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (3s) | N (7s) | N (4s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (6s) | T/o | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (4s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (2s) | T/o | N (7s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (2s) | N (3s) |

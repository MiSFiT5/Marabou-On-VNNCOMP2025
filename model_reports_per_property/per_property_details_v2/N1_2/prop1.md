# N1,2 — Property 1

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_2_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **0** (Clear-of-Conflict)
- **Network outputs at midpoint:** `[-0.0204, -0.0185, -0.0182, -0.018, -0.018]`
- **Query filter used in this report:** `class_id = midpoint prediction`, `center_source = property_midpoint[0]`, `sample_idx = 0`

## Dedup Rule

- Repeated logical experiments are merged after the midpoint filter.
- Duplicate key: same `target`, same `ε`, same experiment label, same `α`.
- Keep order: `A (full_rule)` < `B/L0→L1` < `B/L1→L2` < `B/L2→L3` < `B/L3→L4` < `B/L4→L5` < `C (impl_ablation)`.
- The report shows only the kept rows after this overwrite rule.

## Target Summary

| Target | Class Name | Max Verified ε | Winning kept experiments |
|--------|------------|----------------|--------------------------|
| 1 | Weak Left | 0.02 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L1→L2 (α=0.95)` [B/L1→L2], `Impl L3→L4 (α=0.9)` [B/L3→L4], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L1→L2 [!A->!B] (α=0.9)` [C], `Impl L3→L4 [!A->B] (α=0.9)` [C], `Impl L3→L4 [A->B] (α=0.9)` [C], `Impl L4→L5 [!A->!B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |
| 2 | Weak Right | 0.02 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L1→L2 (α=0.95)` [B/L1→L2], `Impl L3→L4 (α=0.9)` [B/L3→L4], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L1→L2 [!A->!B] (α=0.9)` [C], `Impl L3→L4 [!A->B] (α=0.9)` [C], `Impl L3→L4 [A->B] (α=0.9)` [C], `Impl L4→L5 [!A->!B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |
| 3 | Strong Left | 0.02 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L1→L2 (α=0.95)` [B/L1→L2], `Impl L3→L4 (α=0.9)` [B/L3→L4], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L1→L2 [!A->!B] (α=0.9)` [C], `Impl L3→L4 [!A->B] (α=0.9)` [C], `Impl L3→L4 [A->B] (α=0.9)` [C], `Impl L4→L5 [!A->!B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |
| 4 | Strong Right | 0.02 | `ALWAYS_OFF (α=0.9)` [C], `ALWAYS_ON+OFF (α=0.9)` [C], `Impl L1→L2 (α=0.9)` [B/L1→L2], `Impl L1→L2 (α=0.95)` [B/L1→L2], `Impl L3→L4 (α=0.9)` [B/L3→L4], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L1→L2 [!A->!B] (α=0.9)` [C], `Impl L3→L4 [!A->B] (α=0.9)` [C], `Impl L3→L4 [A->B] (α=0.9)` [C], `Impl L4→L5 [!A->!B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |

**Overall:** after deduplication, this reference point is fully verified up to **ε = 0.02**.

---

## Detailed Results Per Target

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `0.02`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L1→L2 (α=0.95)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L3→L4 (α=0.9)` (implication-only (L3→L4)) from `B/L3→L4`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L1→L2 [!A->!B] (α=0.9)` (implication-direction (L1→L2)) from `C`
  - `Impl L3→L4 [!A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L3→L4 [A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L4→L5 [!A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (3s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (2s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (3s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | Y (0s) | N (1s) | N (6s) | N (2s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | Y (7s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (3s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (24s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (3s) | N (6s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (1s) | N (4s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (4s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (3s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `0.02`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L1→L2 (α=0.95)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L3→L4 (α=0.9)` (implication-only (L3→L4)) from `B/L3→L4`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L1→L2 [!A->!B] (α=0.9)` (implication-direction (L1→L2)) from `C`
  - `Impl L3→L4 [!A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L3→L4 [A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L4→L5 [!A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (3s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (3s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (0s) | N (5s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | Y (0s) | N (1s) | N (5s) | N (2s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | Y (5s) | N (1s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (5s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (1s) | N (2s) | N (4s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (3s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (4s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (6s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (4s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (5s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `0.02`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L1→L2 (α=0.95)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L3→L4 (α=0.9)` (implication-only (L3→L4)) from `B/L3→L4`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L1→L2 [!A->!B] (α=0.9)` (implication-direction (L1→L2)) from `C`
  - `Impl L3→L4 [!A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L3→L4 [A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L4→L5 [!A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (2s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (2s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | Y (0s) | N (1s) | N (3s) | N (2s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | Y (6s) | N (1s) | N (4s) | N (3s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (1s) | N (5s) | N (5s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (1s) | N (0s) | N (2s) | N (5s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (3s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (10s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (18s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (4s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (5s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (4s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (4s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `0.02`
- **Winning kept experiments:**
  - `ALWAYS_OFF (α=0.9)` (unary-only) from `C`
  - `ALWAYS_ON+OFF (α=0.9)` (unary-only) from `C`
  - `Impl L1→L2 (α=0.9)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L1→L2 (α=0.95)` (implication-only (L1→L2)) from `B/L1→L2`
  - `Impl L3→L4 (α=0.9)` (implication-only (L3→L4)) from `B/L3→L4`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L1→L2 [!A->!B] (α=0.9)` (implication-direction (L1→L2)) from `C`
  - `Impl L3→L4 [!A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L3→L4 [A->B] (α=0.9)` (implication-direction (L3→L4)) from `C`
  - `Impl L4→L5 [!A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (2s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (2s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (3s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | Y (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | Y (5s) | N (1s) | N (1s) | N (3s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (0s) | N (1s) | N (3s) | N (4s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (3s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (16s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (5s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (3s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (4s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (4s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |

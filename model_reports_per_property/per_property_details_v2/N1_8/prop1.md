# N1,8 — Property 1

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_8_batch_2000.onnx`
- **Property:** prop1
- **Reference point (property midpoint):** `[0.639929, 0.0, 0.0, 0.475, -0.475]`
- **Network prediction:** class **0** (Clear-of-Conflict)
- **Network outputs at midpoint:** `[-0.0192, -0.0176, -0.018, -0.0166, -0.0173]`
- **Query filter used in this report:** `class_id = midpoint prediction`, `center_source = property_midpoint[0]`, `sample_idx = 0`

## Dedup Rule

- Repeated logical experiments are merged after the midpoint filter.
- Duplicate key: same `target`, same `ε`, same experiment label, same `α`.
- Keep order: `A (full_rule)` < `B/L0→L1` < `B/L1→L2` < `B/L2→L3` < `B/L3→L4` < `B/L4→L5` < `C (impl_ablation)`.
- The report shows only the kept rows after this overwrite rule.

## Target Summary

| Target | Class Name | Max Verified ε | Winning kept experiments |
|--------|------------|----------------|--------------------------|
| 1 | Weak Left | 0.05 | `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L2→L3 [!A->B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |
| 2 | Weak Right | 0.05 | `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L2→L3 [!A->B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |
| 3 | Strong Left | 0.05 | `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L2→L3 [!A->B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |
| 4 | Strong Right | 0.05 | `Impl L2→L3 (α=0.9)` [B/L2→L3], `Impl L4→L5 (α=0.9)` [B/L4→L5], `Impl L2→L3 [!A->B] (α=0.9)` [C], `Impl L4→L5 [A->!B] (α=0.9)` [C] |

**Overall:** after deduplication, this reference point is fully verified up to **ε = 0.05**.

---

## Detailed Results Per Target

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (0s) | N (3s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | Y (18s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | Y (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | Y (14s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (0s) | N (85s) | N (2s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (1s) | N (1s) | N (2s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | Y (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (0s) | Y (14s) | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | Y (6s) | N (101s) | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (6s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (3s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | Y (9s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | N (17s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (4s) | N (10s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (5s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | Y (11s) | N (1s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (0s) | N (3s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | Y (17s) | N (1s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | Y (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | Y (16s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (1s) | N (1s) | N (2s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | T/o | N (2s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | Y (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (0s) | Y (13s) | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | Y (6s) | T/o | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (6s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (3s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (19s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | Y (6s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | N (17s) | N (1s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (28s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | Y (12s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (0s) | N (3s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | Y (16s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | Y (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | Y (17s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (1s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | Y (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (0s) | Y (13s) | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | Y (6s) | T/o | N (1s) | N (2s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (6s) | N (10s) | N (3s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (3s) | N (1s) | N (3s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (5s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (6s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | Y (6s) | N (1s) | N (1s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | N (17s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (32s) | N (2s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | Y (11s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |

### Target 4 (Strong Right)

- **Max verified ε after deduplication:** `0.05`
- **Winning kept experiments:**
  - `Impl L2→L3 (α=0.9)` (implication-only (L2→L3)) from `B/L2→L3`
  - `Impl L4→L5 (α=0.9)` (implication-only (L4→L5)) from `B/L4→L5`
  - `Impl L2→L3 [!A->B] (α=0.9)` (implication-direction (L2→L3)) from `C`
  - `Impl L4→L5 [A->!B] (α=0.9)` (implication-direction (L4→L5)) from `C`

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.99]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `none (baseline) [α=0.9]` | baseline | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | Y (0s) | N (3s) | N (0s) | N (0s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | Y (16s) | N (0s) | N (0s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.9)` | unary-only | Y (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | Y (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | Y (16s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (0s) | N (1s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (4s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | Y (0s) | Y (1s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | Y (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | Y (1s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | Y (0s) | Y (13s) | N (1s) | N (3s) |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | Y (6s) | T/o | N (1s) | N (4s) |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (4s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | Y (5s) | N (1s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (1s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | Y (0s) | N (3s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (1s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (0s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | Y (0s) | N (1s) | N (2s) | N (3s) |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | Y (8s) | N (1s) | N (2s) | N (2s) |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | N (16s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (5s) | N (8s) | N (1s) | N (3s) |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (2s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (4s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | Y (0s) | Y (10s) | N (1s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (1s) | N (1s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (3s) |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (2s) | N (2s) |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (0s) | N (0s) | N (1s) | N (3s) |

# ACAS Xu Per-Property Verification Reports

> Generated 2026-03-17

## What's different from `model_reports/`

| Aspect | Old (`model_reports/`) | New (this directory) |
|--------|----------------------|---------------------|
| Reference point | Random training sample | **Property midpoint** |
| Rule mining | Per-model (shared across properties) | **Per-property** |
| Rule cap | max_rules=3000, max_unary=3000 | **No limit** (all rules used) |
| Granularity | 1 sample per model | **1 sample per (model, property) pair** |
| Total pairs | 45 models | **186 (model, property) pairs** |

## Experiment Types

| Label | Description |
|-------|-------------|
| Full-Rule | All rule types from all layers combined |
| Per-Layer | Single layer pair at a time (L0L1 through L4L5) |
| Impl Ablation | Each implication direction tested separately |

## Reports

- **[All_Models_Aggregated.md](All_Models_Aggregated.md)** — Overall statistics and comparison

### Per-Model Reports

| Model | Link |
|-------|------|
| N1,1 | [N1_1.md](N1_1.md) |
| N1,2 | [N1_2.md](N1_2.md) |
| N1,3 | [N1_3.md](N1_3.md) |
| N1,4 | [N1_4.md](N1_4.md) |
| N1,5 | [N1_5.md](N1_5.md) |
| N1,6 | [N1_6.md](N1_6.md) |
| N1,7 | [N1_7.md](N1_7.md) |
| N1,8 | [N1_8.md](N1_8.md) |
| N1,9 | [N1_9.md](N1_9.md) |
| N2,1 | [N2_1.md](N2_1.md) |
| N2,2 | [N2_2.md](N2_2.md) |
| N2,3 | [N2_3.md](N2_3.md) |
| N2,4 | [N2_4.md](N2_4.md) |
| N2,5 | [N2_5.md](N2_5.md) |
| N2,6 | [N2_6.md](N2_6.md) |
| N2,7 | [N2_7.md](N2_7.md) |
| N2,8 | [N2_8.md](N2_8.md) |
| N2,9 | [N2_9.md](N2_9.md) |
| N3,1 | [N3_1.md](N3_1.md) |
| N3,2 | [N3_2.md](N3_2.md) |
| N3,3 | [N3_3.md](N3_3.md) |
| N3,4 | [N3_4.md](N3_4.md) |
| N3,5 | [N3_5.md](N3_5.md) |
| N3,6 | [N3_6.md](N3_6.md) |
| N3,7 | [N3_7.md](N3_7.md) |
| N3,8 | [N3_8.md](N3_8.md) |
| N3,9 | [N3_9.md](N3_9.md) |
| N4,1 | [N4_1.md](N4_1.md) |
| N4,2 | [N4_2.md](N4_2.md) |
| N4,3 | [N4_3.md](N4_3.md) |
| N4,4 | [N4_4.md](N4_4.md) |
| N4,5 | [N4_5.md](N4_5.md) |
| N4,6 | [N4_6.md](N4_6.md) |
| N4,7 | [N4_7.md](N4_7.md) |
| N4,8 | [N4_8.md](N4_8.md) |
| N4,9 | [N4_9.md](N4_9.md) |
| N5,1 | [N5_1.md](N5_1.md) |
| N5,2 | [N5_2.md](N5_2.md) |
| N5,3 | [N5_3.md](N5_3.md) |
| N5,4 | [N5_4.md](N5_4.md) |
| N5,5 | [N5_5.md](N5_5.md) |
| N5,6 | [N5_6.md](N5_6.md) |
| N5,7 | [N5_7.md](N5_7.md) |
| N5,8 | [N5_8.md](N5_8.md) |
| N5,9 | [N5_9.md](N5_9.md) |

### Analysis

See [All_Models_Aggregated.md](All_Models_Aggregated.md) for full tables.

**Baseline is near-zero.** Without NAP rules, Marabou verifies only 4.0% of queries at ε=0.02 and 0% at ε≥0.10 on property midpoints.

**NAP dramatically improves verification.** With the best rule type per (model, prop) pair at α=0.90:

| ε | Baseline | NAP (any rule Y) |
|---|----------|-------------------|
| 0.02 | 4.0% | **51.9%** |
| 0.05 | 1.2% | **44.3%** |
| 0.10 | 0.0% | **17.8%** |
| 0.20 | 0.0% | **9.7%** |

**6,348 "rescue" cases:** Baseline returns N or T/o, but NAP verifies successfully.

**712x average speedup** on the 223 cases where both baseline and NAP verify (18.6s → 0.07s).

**Best rule types (ε=0.02, α=0.90):**

| Rule Type | Y% (ε=0.02) |
|-----------|-------------|
| ALWAYS_ON+OFF | 37.3% |
| ALWAYS_OFF | 34.3% |
| Impl L3→L4 | 29.2% |
| Impl L2→L3 | 29.1% |
| ALWAYS_ON | 23.6% |
| Impl L1→L2 | 23.5% |
| Impl L4→L5 | 20.1% |
| Impl L0→L1 | 17.3% |

Unary rules (ALWAYS_ON/OFF) are the most effective. Among implication rules, middle layers (L2→L3, L3→L4) outperform early (L0→L1) and late (L4→L5) layers.

**Implication ablation (Exp C):** Each implication direction (A→B, !A→!B, A→!B, !A→B) was tested separately. At α=0.90, the strongest directions are !A→!B and A→!B; A→B and !A→B are weaker. At α≥0.95, implication rules become much less effective across all directions.

**Lower α → more rules → higher verification rate:** α=0.90 (51.9%) > α=0.95 (50.8%) > α=0.99 (28.0%) at ε=0.02.

**Model variation:** N1,x series performs best (35–45% at ε=0.02), while N4,x/N5,x are harder (6–25%).
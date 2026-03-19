# ACAS Xu Per-Property Verification Reports

> Generated 2026-03-19

## What's different from `model_reports/`

| Aspect | Old (`model_reports/`) | New (this directory) |
|--------|----------------------|---------------------|
| Reference point | Random training sample | **Property midpoint** |
| Rule mining | Per-model (shared across properties) | **Per-property** |
| Rule cap | max_rules=3000, max_unary=3000 | **No limit** (all rules used) |
| Granularity | 1 sample per model | **1 reference point per (model, property) pair, expanded into query rows over true_class/target_label pairs** |
| Total pairs | 45 models | **186 (model, property) pairs** |

## How to read `Y/total`

- `Y/total` always means `verified queries / valid queries`.
- A valid query is one `(property, ε, true_class, target_label != true_class, rule)` combination.
- Rows with `target_label == true_class` are stored as `-` in the CSVs and are excluded from denominators.
- In per-layer reports, shared unary/baseline rows are deduplicated across layer-pair directories so counts reflect unique queries rather than 5 reruns of the same query.
- For the full pipeline and a worked example of counts such as `8/40`, see **[COUNTS_AND_PIPELINE.md](COUNTS_AND_PIPELINE.md)**.

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

# MNIST Verification Reports

> Generated 2026-03-20

## Models

| Model | Architecture | ONNX | Layer Pairs | Classes With Data |
|-------|-------------|------|-------------|-------------------|
| [mnist256x2](mnist256x2.md) | 784 → 256 → 256 → 10 | `mnist-net_256x2.onnx` | L01 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| [mnist256x4](mnist256x4.md) | 784 → 256 → 256 → 256 → 256 → 10 | `mnist-net_256x4.onnx` | L01, L12, L23 | 0, 2, 3, 4, 5, 6, 7, 9 |
| [mnist256x6](mnist256x6.md) | 784 → 256 → 256 → 256 → 256 → 256 → 256 → 10 | `mnist-net_256x6.onnx` | L01, L12, L23, L34, L45 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |

## Experiment Types

| Label | Description |
|-------|-------------|
| Full-Rule | All rule types from all layers combined |
| Per-Layer | Single layer pair at a time |
| Impl Ablation | Each implication direction tested separately |

## How To Read Counts

- Baseline counts are deduplicated to one canonical run per `(model, class, ε, target)` query.
- `Any-rule verified` collapses all full-rule NAP families for a fixed `(model, class, α, ε, target)` query.
- `Row-level totals` count every rule-row separately, so the denominator grows with the number of rule families.

## Reports

- **[All_Models_Aggregated.md](All_Models_Aggregated.md)** — Overall statistics and comparison

### Per-Model Reports

- [mnist256x2](mnist256x2.md)
- [mnist256x4](mnist256x4.md)
- [mnist256x6](mnist256x6.md)

---

## Analysis

See [All_Models_Aggregated.md](All_Models_Aggregated.md) for full tables.

### Baseline Performance

- **mnist256x2** ε=0.02: 63/90 (70.0%)
- **mnist256x2** ε=0.05: 0/90 (0.0%)
- **mnist256x4** ε=0.02: 31/72 (43.1%)
- **mnist256x4** ε=0.05: 0/72 (0.0%)
- **mnist256x6** ε=0.02: 36/90 (40.0%)
- **mnist256x6** ε=0.05: 0/90 (0.0%)

### Full-Rule NAP — Any-Rule Verified (α=0.90)

| Model | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|-------|--------|--------|--------|--------|
| mnist256x2 | 90/90 (100.0%) | 90/90 (100.0%) | 77/90 (85.6%) | 70/90 (77.8%) |
| mnist256x4 | 63/63 (100.0%) | 63/63 (100.0%) | 63/63 (100.0%) | 63/63 (100.0%) |
| mnist256x6 | 90/90 (100.0%) | 90/90 (100.0%) | 90/90 (100.0%) | 90/90 (100.0%) |

### Full-Rule NAP — Row-Level Totals (α=0.90)

| Model | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|-------|--------|--------|--------|--------|
| mnist256x2 | 359/360 (99.7%) | 186/360 (51.7%) | 89/360 (24.7%) | 75/360 (20.8%) |
| mnist256x4 | 273/378 (72.2%) | 126/378 (33.3%) | 122/378 (32.3%) | 120/378 (31.7%) |
| mnist256x6 | 414/720 (57.5%) | 180/720 (25.0%) | 180/720 (25.0%) | 180/720 (25.0%) |

### Key Findings

- **mnist256x4 is still incomplete:** missing classes 1, 8.
- **845 unique rescue queries:** baseline returns `N` or `T/o`, but some NAP rule verifies.
- **5.5x mean speedup** on 130 unique queries where both baseline and NAP verify.

### Rule Type Ranking (ε=0.02, α=0.90, row-level)

**mnist256x2:**

| Rule Type | Y% |
|-----------|-----|
| ALWAYS_OFF | 90/90 (100.0%) |
| ALWAYS_ON+OFF | 90/90 (100.0%) |
| Impl L0→L1 | 90/90 (100.0%) |
| ALWAYS_ON | 89/90 (98.9%) |

**mnist256x4:**

| Rule Type | Y% |
|-----------|-----|
| ALWAYS_OFF | 63/63 (100.0%) |
| ALWAYS_ON+OFF | 63/63 (100.0%) |
| Impl L0→L1 | 45/63 (71.4%) |
| Impl L2→L3 | 45/63 (71.4%) |
| ALWAYS_ON | 39/63 (61.9%) |
| Impl L1→L2 | 18/63 (28.6%) |

**mnist256x6:**

| Rule Type | Y% |
|-----------|-----|
| ALWAYS_OFF | 90/90 (100.0%) |
| ALWAYS_ON+OFF | 90/90 (100.0%) |
| Impl L0→L1 | 54/90 (60.0%) |
| ALWAYS_ON | 36/90 (40.0%) |
| Impl L1→L2 | 36/90 (40.0%) |
| Impl L2→L3 | 36/90 (40.0%) |
| Impl L3→L4 | 36/90 (40.0%) |
| Impl L4→L5 | 36/90 (40.0%) |

### Depth Effect (row-level, α=0.90)

- **ε=0.02:** mnist256x2: 359/360 (99.7%) | mnist256x4: 273/378 (72.2%) | mnist256x6: 414/720 (57.5%)
- **ε=0.05:** mnist256x2: 186/360 (51.7%) | mnist256x4: 126/378 (33.3%) | mnist256x6: 180/720 (25.0%)

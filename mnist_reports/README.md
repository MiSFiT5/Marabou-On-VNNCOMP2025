# MNIST Verification Reports

> Generated 2026-03-17

## Models

| Model | Architecture | ONNX | Layer Pairs |
|-------|-------------|------|-------------|
| [mnist256x2](mnist256x2.md) | 784 → 256 → 256 → 10 | `mnist-net_256x2.onnx` | L01 |
| [mnist256x4](mnist256x4.md) | 784 → 256 → 256 → 256 → 256 → 10 | `mnist-net_256x4.onnx` | L01, L12, L23 |
| [mnist256x6](mnist256x6.md) | 784 → 256 → 256 → 256 → 256 → 256 → 256 → 10 | `mnist-net_256x6.onnx` | L01, L12, L23, L34, L45 |

## Experiment Types

| Label | Description |
|-------|-------------|
| Full-Rule | All rule types from all layers combined |
| Per-Layer | Single layer pair at a time |
| Impl Ablation | Each implication direction tested separately |

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

- **mnist256x2** ε=0.02: 191/270 (70.7%)
- **mnist256x2** ε=0.05: 0/270 (0.0%)
- **mnist256x4** ε=0.02: 74/189 (39.2%)
- **mnist256x4** ε=0.05: 0/189 (0.0%)
- **mnist256x6** ε=0.02: 108/270 (40.0%)
- **mnist256x6** ε=0.05: 0/270 (0.0%)

### NAP Improvement (Full-Rule, α=0.90)

| Model | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|-------|--------|--------|--------|--------|
| mnist256x2 | 359/360 (99.7%) | 186/360 (51.7%) | 89/360 (24.7%) | 75/360 (20.8%) |
| mnist256x4 | 273/378 (72.2%) | 126/378 (33.3%) | 122/378 (32.3%) | 120/378 (31.7%) |
| mnist256x6 | 414/720 (57.5%) | 180/720 (25.0%) | 180/720 (25.0%) | 180/720 (25.0%) |

### Key Findings

- **2444 rescue cases:** baseline returns N or T/o, but NAP verifies successfully.
- **6.0x mean speedup** on 373 cases where both baseline and NAP verify.

### Rule Type Ranking (ε=0.02, α=0.90)

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

### Depth Effect

How does network depth affect verification?

- **ε=0.02, α=0.90:** mnist256x2: 359/360 (99.7%) | mnist256x4: 273/378 (72.2%) | mnist256x6: 414/720 (57.5%)
- **ε=0.05, α=0.90:** mnist256x2: 186/360 (51.7%) | mnist256x4: 126/378 (33.3%) | mnist256x6: 180/720 (25.0%)

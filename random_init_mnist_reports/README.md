# Random-Init MNIST Verification Reports

> Generated 2026-03-18

## Models

| Model | Architecture | Randomized ONNX family | Initialization variants |
|-------|-------------|------------------------|-------------------------|
| [mnist256x4](mnist256x4.md) | 784 → 256 → 256 → 256 → 256 → 10 | `mnist-net_256x4.onnx` | `he`, `xavier`, `lecun` |
| [mnist256x6](mnist256x6.md) | 784 → 256 → 256 → 256 → 256 → 256 → 256 → 10 | `mnist-net_256x6.onnx` | `he`, `xavier`, `lecun` |

## Experiment Type

| Label | Description |
|-------|-------------|
| Random baseline | Reinitialize the VNN-COMP MNIST model, keep only `correct-by-luck` training samples, then run baseline-only Marabou verification |

## Reports

- **[All_Models_Aggregated.md](All_Models_Aggregated.md)** — Overall statistics, caveats, and comparison to the trained MNIST study

### Per-Model Reports

- [mnist256x4](mnist256x4.md)
- [mnist256x6](mnist256x6.md)

---

## Analysis

See [All_Models_Aggregated.md](All_Models_Aggregated.md) for full tables.

### Setup

- Models: `mnist256x4`, `mnist256x6`
- Seed: `0`
- Initialization variants: `he`, `xavier`, `lecun`
- Radius: `epsilon=0.05`
- Verifier: baseline-only Marabou, `timeout=60s`
- Centers: one `correct-by-luck` training sample per class when available

### Coverage

- **60 total tasks:** `2 models x 10 classes x 3 init variants x 1 seed`
- **36 tasks with verification CSVs**
- **24 skipped tasks**
  - These are not failed jobs.
  - They were skipped because the randomized model had no eligible `correct-by-luck` sample for that class.

### Random Accuracy

| Model | Correct / 60000 | Accuracy | Eligible classes | Missing classes |
|-------|------------------|----------|------------------|-----------------|
| mnist256x4 | 2832 | 4.72% | 0, 3, 4, 5, 7, 9 | 1, 2, 6, 8 |
| mnist256x6 | 6291 | 10.49% | 2, 3, 5, 6, 8, 9 | 0, 1, 4, 7 |

### Verification Outcome At `epsilon=0.05`

`Y = proved robust (UNSAT)`, `N = falsified (SAT)`, `T/o = timeout`.

| Model | Across 3 init variants | Y | N | T/o |
|-------|-------------------------|---|---|-----|
| mnist256x4 | 162 off-target queries | 0 | 73 | 89 |
| mnist256x6 | 162 off-target queries | 0 | 0 | 162 |

### Key Findings

- No random case was proved robust at `epsilon=0.05` under the current `60s` timeout.
- `mnist256x4` often yields explicit adversarial examples once a lucky center is chosen.
- `mnist256x6` is dominated by timeout, so its outcome is mostly unresolved rather than disproved.
- In this exact setup, `he`, `xavier`, and `lecun` produced identical `pred_labels.npy`, `correct_mask.npy`, and `labels.npy` for each model.
- Because of that, the three initialization variants should be interpreted as a numeric-scale ablation of the same random ReLU classifier, not as three independent random classifiers.

### Comparison To Trained MNIST

The closest trained reference already exists in [../mnist_reports/](../mnist_reports/README.md):

- For `mnist256x4`, the detailed trained comparison uses the current `alpha=0.95`
  full-rule subset, which covers `7` classes (`63` off-target queries). The
  broader trained directory contains `8` classes with some data overall.

- trained baseline remains weak at `epsilon=0.05`
- trained full-rule NAP is much stronger than the random baseline study
- no extra trained rerun is required just to obtain a comparator

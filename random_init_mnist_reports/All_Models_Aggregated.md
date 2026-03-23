# Random-Init MNIST — Aggregated Results

> Generated 2026-03-18  
> Experiments: per-class, baseline-only, `epsilon=0.05`, `timeout=60s`

- **Total array tasks:** 60
- **Task summaries present:** 60
- **Tasks with verification CSVs:** 36
- **Skipped tasks:** 24
- **Models:** mnist256x4, mnist256x6
- **Initialization variants:** he, xavier, lecun
- **Seeds:** 1 (`seed=0`)

The `24` skipped tasks are expected. They correspond to classes for which the
randomized network produced no eligible `correct-by-luck` sample, so baseline
verification was skipped by design.

## Setup

1. Reuse the VNN-COMP MNIST ONNX models.
2. Randomize weights with activation-aware initialization (`he`, `xavier`, `lecun`).
3. Run the network on MNIST training data and keep only samples that are
   classified correctly by luck.
4. For each eligible class, verify one center against all nine off-target labels
   using baseline-only Marabou at `epsilon=0.05`.

## Random Accuracy And Class Coverage

| Model | Init | Correct / 60000 | Accuracy | Eligible classes | Missing classes |
|-------|------|------------------|----------|------------------|-----------------|
| mnist256x4 | He | 2832 | 4.72% | 0, 3, 4, 5, 7, 9 | 1, 2, 6, 8 |
| mnist256x4 | Xavier | 2832 | 4.72% | 0, 3, 4, 5, 7, 9 | 1, 2, 6, 8 |
| mnist256x4 | LeCun | 2832 | 4.72% | 0, 3, 4, 5, 7, 9 | 1, 2, 6, 8 |
| mnist256x6 | He | 6291 | 10.49% | 2, 3, 5, 6, 8, 9 | 0, 1, 4, 7 |
| mnist256x6 | Xavier | 6291 | 10.49% | 2, 3, 5, 6, 8, 9 | 0, 1, 4, 7 |
| mnist256x6 | LeCun | 6291 | 10.49% | 2, 3, 5, 6, 8, 9 | 0, 1, 4, 7 |

## Verification Results

`Y = proved robust (UNSAT)`, `N = falsified (SAT)`, `T/o = timeout`.

### By Model And Initialization

| Model | Init | Tasks with results | Y | N | T/o | Total off-target queries |
|-------|------|--------------------|---|---|-----|--------------------------|
| mnist256x4 | He | 6 | 0 | 23 | 31 | 54 |
| mnist256x4 | Xavier | 6 | 0 | 27 | 27 | 54 |
| mnist256x4 | LeCun | 6 | 0 | 23 | 31 | 54 |
| mnist256x6 | He | 6 | 0 | 0 | 54 | 54 |
| mnist256x6 | Xavier | 6 | 0 | 0 | 54 | 54 |
| mnist256x6 | LeCun | 6 | 0 | 0 | 54 | 54 |

### By Model

| Model | Eligible classes | Y | N | T/o | Total off-target queries |
|-------|------------------|---|---|-----|--------------------------|
| mnist256x4 | 6 classes × 3 init variants | 0 | 73 | 89 | 162 |
| mnist256x6 | 6 classes × 3 init variants | 0 | 0 | 162 | 162 |

### Overall

Across all `324` off-target queries:

- `Y = 0`
- `N = 73`
- `T/o = 251`

## Per-Model Behavior

### mnist256x4

- Random accuracy is `4.72%` (`2832 / 60000`).
- Eligible classes are `0, 3, 4, 5, 7, 9`.
- Across all three init variants, `73 / 162` queries are explicitly falsified.
- Falsifications concentrate in classes `0, 4, 5, 9`, while classes `3` and `7`
  are pure timeout in this setup.

### mnist256x6

- Random accuracy is `10.49%` (`6291 / 60000`).
- Eligible classes are `2, 3, 5, 6, 8, 9`.
- All `162 / 162` queries time out; no off-target query is either proved or
  falsified within `60s`.
- Correct-by-luck coverage is extremely imbalanced: class `3` contributes
  `5934 / 6291` correct samples.

## Important Caveat About Initialization Comparison

For each model, the three initialization variants produced identical:

- `pred_labels.npy`
- `correct_mask.npy`
- `labels.npy`

So the `he/xavier/lecun` sweep is not a comparison of three meaningfully
different random classifiers in this specific setup. With the same seed and
zero-bias ReLU MLPs, the three variants behave as layerwise positive rescalings
of the same random network. The small `N/T/o` differences should therefore be
read as Marabou numeric-scaling sensitivity, not as evidence that one
initialization is intrinsically more robust than another.

## Comparison To The Existing Trained MNIST Study

The trained reference is already documented in [../mnist_reports/](../mnist_reports/README.md).
At `epsilon=0.05`, the closest comparison is:

For `mnist256x4`, the trained rows below use the currently available
`alpha=0.95` full-rule subset, which covers `7` classes (`63` off-target
queries). The trained MNIST directory has `8` classes with some data overall.

| Setting | Model | Coverage | Y | N | T/o |
|---------|-------|----------|---|---|-----|
| Random baseline | mnist256x4 | 6 classes, 54 rows per init | 0 | 23 to 27 | 27 to 31 |
| Random baseline | mnist256x6 | 6 classes, 54 rows per init | 0 | 0 | 54 |
| Trained baseline | mnist256x4 | 7 classes with `alpha=0.95` full-rule data, 63 rows | 0 | 9 | 54 |
| Trained baseline | mnist256x6 | 10 classes, 90 rows | 0 | 0 | 90 |
| Trained full-rule NAP, `alpha=0.95` | mnist256x4 | 7 classes with `alpha=0.95` full-rule data, 63 rows | 63 | 0 | 0 |
| Trained full-rule NAP, `alpha=0.95` | mnist256x6 | 10 classes, 90 rows | 90 | 0 | 0 |

This supports the following reading:

- The random study is a useful baseline robustness probe on lucky centers.
- At `epsilon=0.05`, random baseline is weak.
- The strongest contrast is between random baseline and trained `NAP`, not
  between random baseline and trained baseline.

## Takeaway

Under the current setup, the study supports only a modest conclusion:

- randomly initialized VNN-COMP-style MNIST networks do classify a nontrivial
  subset of samples correctly by luck
- but at `epsilon=0.05` and `timeout=60s`, no random case was proved robust
- most of the random `mnist256x6` queries remain unresolved due to timeout

So this experiment responds to the operational part of the request, but the
evidence for local robustness of random networks is weak rather than
conclusive.

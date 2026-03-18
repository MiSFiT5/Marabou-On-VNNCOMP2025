# Random-Init MNIST Report: mnist256x6

> **MNIST random baseline** — mnist256x6 (6 hidden layers, 256 neurons each)  
> Per-class experiments, one lucky center per eligible class  
> Generated 2026-03-18

**Model file:** `mnist-net_256x6.onnx`  
**Architecture:** 784 → 256 → 256 → 256 → 256 → 256 → 256 → 10  
**Initialization variants:** `he`, `xavier`, `lecun`  
**Seed:** `0`  
**Radius:** `epsilon=0.05`  
**Timeout:** `60s`  
**Eligible classes:** 2, 3, 5, 6, 8, 9  
**Missing classes:** 0, 1, 4, 7

---

## Random Accuracy And Coverage

All three initialization variants produced the same classification outputs in
this setup.

| Init | Correct / 60000 | Accuracy | Eligible classes | Missing classes |
|------|------------------|----------|------------------|-----------------|
| He | 6291 | 10.49% | 2, 3, 5, 6, 8, 9 | 0, 1, 4, 7 |
| Xavier | 6291 | 10.49% | 2, 3, 5, 6, 8, 9 | 0, 1, 4, 7 |
| LeCun | 6291 | 10.49% | 2, 3, 5, 6, 8, 9 | 0, 1, 4, 7 |

### Correct-By-Luck Class Distribution

| True class | Count |
|-----------|-------|
| 2 | 3 |
| 3 | 5934 |
| 5 | 2 |
| 6 | 1 |
| 8 | 15 |
| 9 | 336 |

The accuracy is near random-guess scale, but it is extremely concentrated:
class `3` alone contributes `5934 / 6291` lucky samples.

## Verification Outcome At `epsilon=0.05`

`Y = proved robust (UNSAT)`, `N = falsified (SAT)`, `T/o = timeout`.

| Init | Tasks with results | Y | N | T/o | Total off-target queries |
|------|--------------------|---|---|-----|--------------------------|
| He | 6 | 0 | 0 | 54 | 54 |
| Xavier | 6 | 0 | 0 | 54 | 54 |
| LeCun | 6 | 0 | 0 | 54 | 54 |

Across all three initialization variants together:

- `Y = 0`
- `N = 0`
- `T/o = 162`
- total off-target queries = `162`

## Per-Class Breakdown

Each class uses the first eligible `correct-by-luck` center found in the saved
pattern data.

### Shared Across He, Xavier, And LeCun

| Class | Center | Y | N | T/o |
|------|--------|---|---|-----|
| 2 | `global_idx=12950` | 0 | 0 | 9 |
| 3 | `global_idx=7` | 0 | 0 | 9 |
| 5 | `global_idx=26752` | 0 | 0 | 9 |
| 6 | `global_idx=5554` | 0 | 0 | 9 |
| 8 | `global_idx=517` | 0 | 0 | 9 |
| 9 | `global_idx=424` | 0 | 0 | 9 |

## Interpretation

- No `mnist256x6` random query was proved robust at `epsilon=0.05`.
- No explicit adversarial example was found either.
- Every off-target query times out within the `60s` budget, so the result is
  dominated by solver difficulty rather than a clean robustness signal.
- Because the classifier outputs are identical across `he/xavier/lecun`, the
  experiment should not be read as evidence that the three initialization
  methods behave differently on this model.

## Comparison To Trained MNIST

The closest trained reference is [../mnist_reports/mnist256x6.md](../mnist_reports/mnist256x6.md):

| Setting | Coverage | Y | N | T/o |
|---------|----------|---|---|-----|
| Random baseline | 6 classes, 54 rows per init | 0 | 0 | 54 |
| Trained baseline | 10 classes, 90 rows | 0 | 0 | 90 |
| Trained full-rule NAP, `alpha=0.95` | 10 classes, 90 rows | 90 | 0 | 0 |

So for `mnist256x6`, the current random study is mostly unresolved. The main
clear contrast is again between random baseline and trained `NAP`, not between
random baseline and trained baseline.

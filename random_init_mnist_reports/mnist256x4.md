# Random-Init MNIST Report: mnist256x4

> **MNIST random baseline** — mnist256x4 (4 hidden layers, 256 neurons each)  
> Per-class experiments, one lucky center per eligible class  
> Generated 2026-03-18

**Model file:** `mnist-net_256x4.onnx`  
**Architecture:** 784 → 256 → 256 → 256 → 256 → 10  
**Initialization variants:** `he`, `xavier`, `lecun`  
**Seed:** `0`  
**Radius:** `epsilon=0.05`  
**Timeout:** `60s`  
**Eligible classes:** 0, 3, 4, 5, 7, 9  
**Missing classes:** 1, 2, 6, 8

---

## Random Accuracy And Coverage

All three initialization variants produced the same classification outputs in
this setup.

| Init | Correct / 60000 | Accuracy | Eligible classes | Missing classes |
|------|------------------|----------|------------------|-----------------|
| He | 2832 | 4.72% | 0, 3, 4, 5, 7, 9 | 1, 2, 6, 8 |
| Xavier | 2832 | 4.72% | 0, 3, 4, 5, 7, 9 | 1, 2, 6, 8 |
| LeCun | 2832 | 4.72% | 0, 3, 4, 5, 7, 9 | 1, 2, 6, 8 |

### Correct-By-Luck Class Distribution

| True class | Count |
|-----------|-------|
| 0 | 27 |
| 3 | 711 |
| 4 | 477 |
| 5 | 800 |
| 7 | 368 |
| 9 | 449 |

The random classifier is not class-balanced. Most lucky samples come from
classes `3`, `4`, `5`, `7`, and `9`, while classes `1`, `2`, `6`, and `8`
never appear as eligible centers.

## Verification Outcome At `epsilon=0.05`

`Y = proved robust (UNSAT)`, `N = falsified (SAT)`, `T/o = timeout`.

| Init | Tasks with results | Y | N | T/o | Total off-target queries |
|------|--------------------|---|---|-----|--------------------------|
| He | 6 | 0 | 23 | 31 | 54 |
| Xavier | 6 | 0 | 27 | 27 | 54 |
| LeCun | 6 | 0 | 23 | 31 | 54 |

Across all three initialization variants together:

- `Y = 0`
- `N = 73`
- `T/o = 89`
- total off-target queries = `162`

## Per-Class Breakdown

Each class uses the first eligible `correct-by-luck` center found in the saved
pattern data.

### He

| Class | Center | Y | N | T/o |
|------|--------|---|---|-----|
| 0 | `global_idx=1796` | 0 | 6 | 3 |
| 3 | `global_idx=157` | 0 | 0 | 9 |
| 4 | `global_idx=412` | 0 | 7 | 2 |
| 5 | `global_idx=132` | 0 | 5 | 4 |
| 7 | `global_idx=148` | 0 | 0 | 9 |
| 9 | `global_idx=48` | 0 | 5 | 4 |

### Xavier

| Class | Center | Y | N | T/o |
|------|--------|---|---|-----|
| 0 | `global_idx=1796` | 0 | 9 | 0 |
| 3 | `global_idx=157` | 0 | 0 | 9 |
| 4 | `global_idx=412` | 0 | 9 | 0 |
| 5 | `global_idx=132` | 0 | 9 | 0 |
| 7 | `global_idx=148` | 0 | 0 | 9 |
| 9 | `global_idx=48` | 0 | 0 | 9 |

### LeCun

| Class | Center | Y | N | T/o |
|------|--------|---|---|-----|
| 0 | `global_idx=1796` | 0 | 8 | 1 |
| 3 | `global_idx=157` | 0 | 0 | 9 |
| 4 | `global_idx=412` | 0 | 7 | 2 |
| 5 | `global_idx=132` | 0 | 8 | 1 |
| 7 | `global_idx=148` | 0 | 0 | 9 |
| 9 | `global_idx=48` | 0 | 0 | 9 |

## Interpretation

- No `mnist256x4` random query was proved robust at `epsilon=0.05`.
- Many lucky centers are explicitly falsified, especially for classes `0`, `4`,
  `5`, and `9`.
- Classes `3` and `7` remain timeout-only in all three variants.
- The class centers are identical across `he/xavier/lecun`, so the difference in
  `N/T/o` counts should be interpreted as solver sensitivity to numeric scaling,
  not as a true initialization-method effect.

## Comparison To Trained MNIST

The closest trained reference is the baseline section of
[../mnist_reports/mnist256x4.md](../mnist_reports/mnist256x4.md):

Because the most informative trained comparator here is the currently available
`alpha=0.95` full-rule slice, the trained rows below cover `7` classes (`63`
off-target queries). The broader trained MNIST directory contains `8` classes
with some data overall.

| Setting | Coverage | Y | N | T/o |
|---------|----------|---|---|-----|
| Random baseline | 6 classes, 54 rows per init | 0 | 23 to 27 | 27 to 31 |
| Trained baseline | 7 classes with `alpha=0.95` full-rule data, 63 rows | 0 | 9 | 54 |
| Trained full-rule NAP, `alpha=0.95` | 7 classes with `alpha=0.95` full-rule data, 63 rows | 63 | 0 | 0 |

So for `mnist256x4`, the current random study mostly shows that lucky centers
can still be brittle under baseline verification, while trained `NAP` remains
substantially stronger.

# MNIST Report: mnist256x2

> **MNIST** — mnist256x2 (2 hidden layers, 256 neurons each)  
> Per-class experiments, no rule cap  
> Generated 2026-03-20

**Model file:** `mnist-net_256x2.onnx`  
**Architecture:** 784 → 256 → 256 → 10  
**Classes with at least one experiment:** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (10 total)  
**Layer pairs:** L01  
**Experiment types:** full_rule, per_layer, impl_ablation

## How To Read Counts

- `Classes with at least one experiment` means the classes that appear anywhere in the current result directory; missing classes have no report rows yet.
- `Aggregated Summary` below is row-level: each rule family contributes its own verification rows, so denominators grow with the number of rule families shown.
- In `Per-Layer`, shared unary / baseline rows are repeated once per layer-pair directory; this section reports those raw reruns because it is a per-experiment summary.
- `Full-Rule Unique Query Coverage` collapses rule-row duplicates and answers the simpler question: for a `(class, ε, target)` query, did any full-rule NAP rule verify it?

## Full-Rule Unique Query Coverage

At least one NAP rule type achieves `Y` for a given `(class, ε, target)` query.

| α | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|---|--------|--------|--------|--------|
| 0.90 | 90/90 (100.0%) | 90/90 (100.0%) | 77/90 (85.6%) | 70/90 (77.8%) |
| 0.95 | 90/90 (100.0%) | 72/90 (80.0%) | 48/90 (53.3%) | 23/90 (25.6%) |
| 0.99 | 90/90 (100.0%) | 12/90 (13.3%) | 0/90 (0.0%) | 0/90 (0.0%) |

---

## Aggregated Summary (row-level counts across all classes)

### Full-Rule

#### α = 0.9

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.9)` | 90/90 (100.0%) | 35/90 (38.9%) | 12/90 (13.3%) | 5/90 (5.6%) | 39.4% |
| `ALWAYS_ON (α=0.9)` | 89/90 (98.9%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 24.7% |
| `ALWAYS_ON+OFF (α=0.9)` | 90/90 (100.0%) | 90/90 (100.0%) | 77/90 (85.6%) | 70/90 (77.8%) | 90.8% |
| `Impl L0→L1 (α=0.9)` | 90/90 (100.0%) | 61/90 (67.8%) | 0/90 (0.0%) | 0/90 (0.0%) | 41.9% |
| `none (baseline)` | 63/90 (70.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.5% |

#### α = 0.95

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.95)` | 90/90 (100.0%) | 4/90 (4.4%) | 0/90 (0.0%) | 0/90 (0.0%) | 26.1% |
| `ALWAYS_ON (α=0.95)` | 88/90 (97.8%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 24.4% |
| `ALWAYS_ON+OFF (α=0.95)` | 90/90 (100.0%) | 72/90 (80.0%) | 48/90 (53.3%) | 23/90 (25.6%) | 64.7% |
| `Impl L0→L1 (α=0.95)` | 90/90 (100.0%) | 48/90 (53.3%) | 0/90 (0.0%) | 0/90 (0.0%) | 38.3% |
| `none (baseline)` | 64/90 (71.1%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.8% |

#### α = 0.99

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.99)` | 81/90 (90.0%) | 3/90 (3.3%) | 0/90 (0.0%) | 0/90 (0.0%) | 23.3% |
| `ALWAYS_ON (α=0.99)` | 63/90 (70.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.5% |
| `ALWAYS_ON+OFF (α=0.99)` | 81/90 (90.0%) | 2/90 (2.2%) | 0/90 (0.0%) | 0/90 (0.0%) | 23.1% |
| `Impl L0→L1 (α=0.99)` | 79/90 (87.8%) | 11/90 (12.2%) | 0/90 (0.0%) | 0/90 (0.0%) | 25.0% |
| `none (baseline)` | 64/90 (71.1%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.8% |

### Per-Layer

#### α = 0.9

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.9)` | 90/90 (100.0%) | 34/90 (37.8%) | 10/90 (11.1%) | 6/90 (6.7%) | 38.9% |
| `ALWAYS_ON (α=0.9)` | 89/90 (98.9%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 24.7% |
| `ALWAYS_ON+OFF (α=0.9)` | 90/90 (100.0%) | 90/90 (100.0%) | 77/90 (85.6%) | 70/90 (77.8%) | 90.8% |
| `Impl L0→L1 (α=0.9)` | 90/90 (100.0%) | 61/90 (67.8%) | 0/90 (0.0%) | 0/90 (0.0%) | 41.9% |
| `none (baseline)` | 62/90 (68.9%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.2% |

#### α = 0.95

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.95)` | 90/90 (100.0%) | 4/90 (4.4%) | 0/90 (0.0%) | 0/90 (0.0%) | 26.1% |
| `ALWAYS_ON (α=0.95)` | 88/90 (97.8%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 24.4% |
| `ALWAYS_ON+OFF (α=0.95)` | 90/90 (100.0%) | 72/90 (80.0%) | 49/90 (54.4%) | 23/90 (25.6%) | 65.0% |
| `Impl L0→L1 (α=0.95)` | 90/90 (100.0%) | 48/90 (53.3%) | 0/90 (0.0%) | 0/90 (0.0%) | 38.3% |
| `none (baseline)` | 62/90 (68.9%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.2% |

#### α = 0.99

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.99)` | 81/90 (90.0%) | 3/90 (3.3%) | 0/90 (0.0%) | 0/90 (0.0%) | 23.3% |
| `ALWAYS_ON (α=0.99)` | 63/90 (70.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.5% |
| `ALWAYS_ON+OFF (α=0.99)` | 81/90 (90.0%) | 2/90 (2.2%) | 0/90 (0.0%) | 0/90 (0.0%) | 23.1% |
| `Impl L0→L1 (α=0.99)` | 79/90 (87.8%) | 11/90 (12.2%) | 0/90 (0.0%) | 0/90 (0.0%) | 25.0% |
| `none (baseline)` | 62/90 (68.9%) | 0/90 (0.0%) | 0/90 (0.0%) | 0/90 (0.0%) | 17.2% |

### Impl Ablation

#### α = 0.9

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.9)` | 36/36 (100.0%) | 15/36 (41.7%) | 0/36 (0.0%) | 0/36 (0.0%) | 35.4% |
| `ALWAYS_ON (α=0.9)` | 36/36 (100.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 25.0% |
| `ALWAYS_ON+OFF (α=0.9)` | 36/36 (100.0%) | 36/36 (100.0%) | 36/36 (100.0%) | 34/36 (94.4%) | 98.6% |
| `Impl L0→L1 [!A->!B] (α=0.9)` | 34/36 (94.4%) | 0/36 (0.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 23.6% |
| `Impl L0→L1 [!A->B] (α=0.9)` | 36/36 (100.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 25.0% |
| `Impl L0→L1 [A->!B] (α=0.9)` | 34/36 (94.4%) | 0/36 (0.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 23.6% |
| `Impl L0→L1 [A->B] (α=0.9)` | 36/36 (100.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 25.0% |
| `none (baseline)` | 26/36 (72.2%) | 0/36 (0.0%) | 0/36 (0.0%) | 0/36 (0.0%) | 18.1% |

#### α = 0.95

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.95)` | 54/54 (100.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 25.0% |
| `ALWAYS_ON (α=0.95)` | 52/54 (96.3%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 24.1% |
| `ALWAYS_ON+OFF (α=0.95)` | 54/54 (100.0%) | 45/54 (83.3%) | 30/54 (55.6%) | 18/54 (33.3%) | 68.1% |
| `Impl L0→L1 [!A->!B] (α=0.95)` | 42/54 (77.8%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 19.4% |
| `Impl L0→L1 [!A->B] (α=0.95)` | 53/54 (98.1%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 24.5% |
| `Impl L0→L1 [A->!B] (α=0.95)` | 43/54 (79.6%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 19.9% |
| `Impl L0→L1 [A->B] (α=0.95)` | 53/54 (98.1%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 24.5% |
| `none (baseline)` | 26/54 (48.1%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 12.0% |

#### α = 0.99

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.99)` | 63/72 (87.5%) | 3/72 (4.2%) | 0/72 (0.0%) | 0/72 (0.0%) | 22.9% |
| `ALWAYS_ON (α=0.99)` | 45/72 (62.5%) | 0/72 (0.0%) | 0/72 (0.0%) | 0/72 (0.0%) | 15.6% |
| `ALWAYS_ON+OFF (α=0.99)` | 63/72 (87.5%) | 2/72 (2.8%) | 0/72 (0.0%) | 0/72 (0.0%) | 22.6% |
| `Impl L0→L1 [!A->!B] (α=0.99)` | 57/72 (79.2%) | 0/72 (0.0%) | 0/72 (0.0%) | 0/72 (0.0%) | 19.8% |
| `Impl L0→L1 [!A->B] (α=0.99)` | 44/72 (61.1%) | 0/72 (0.0%) | 0/72 (0.0%) | 0/72 (0.0%) | 15.3% |
| `Impl L0→L1 [A->!B] (α=0.99)` | 61/72 (84.7%) | 0/72 (0.0%) | 0/72 (0.0%) | 0/72 (0.0%) | 21.2% |
| `Impl L0→L1 [A->B] (α=0.99)` | 48/72 (66.7%) | 0/72 (0.0%) | 0/72 (0.0%) | 0/72 (0.0%) | 16.7% |
| `none (baseline)` | 44/72 (61.1%) | 0/72 (0.0%) | 0/72 (0.0%) | 0/72 (0.0%) | 15.3% |

---

## Per-Class Details

### Class 0

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>6.1s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>5.8s</sub> | Y<br><sub>6.8s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | Y<br><sub>12s</sub> | Y<br><sub>7.0s</sub> | Y<br><sub>6.2s</sub> | 6/9 (67%) |
| `0.10` | – | Y<br><sub>47s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>48s</sub> | Y<br><sub>32s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.20` | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>10s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>75s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | N<br><sub>41s</sub> | T/o<br><sub>66s</sub> | N<br><sub>18s</sub> | T/o<br><sub>62s</sub> | N<br><sub>43s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>3.8s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | 9/9 (100%) |
| `0.10` | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>20s</sub> | N<br><sub>18s</sub> | N<br><sub>19s</sub> | N<br><sub>49s</sub> | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>4.9s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.6s</sub> | N<br><sub>5.7s</sub> | N<br><sub>7.9s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>13s</sub> | N<br><sub>9.5s</sub> | N<br><sub>10.0s</sub> | N<br><sub>10s</sub> | N<br><sub>8.7s</sub> | N<br><sub>9.1s</sub> | N<br><sub>10s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.6s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>61s</sub> | N<br><sub>27s</sub> | N<br><sub>34s</sub> | T/o<br><sub>70s</sub> | N<br><sub>28s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>25s</sub> | N<br><sub>34s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>14s</sub> | N<br><sub>9.5s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>14s</sub> | N<br><sub>9.4s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | N<br><sub>58s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | N<br><sub>62s</sub> | N<br><sub>23s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>3.7s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | 9/9 (100%) |
| `0.10` | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>26s</sub> | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>5.7s</sub> | N<br><sub>5.8s</sub> | N<br><sub>4.8s</sub> | N<br><sub>8.5s</sub> | N<br><sub>9.2s</sub> | N<br><sub>5.5s</sub> | N<br><sub>7.8s</sub> | N<br><sub>5.0s</sub> | N<br><sub>8.5s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.9s</sub> | N<br><sub>11s</sub> | N<br><sub>8.9s</sub> | N<br><sub>8.5s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>14s</sub> | N<br><sub>7.8s</sub> | N<br><sub>14s</sub> | T/o<br><sub>62s</sub> | N<br><sub>7.0s</sub> | N<br><sub>8.1s</sub> | N<br><sub>7.6s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>11s</sub> | N<br><sub>5.9s</sub> | N<br><sub>8.6s</sub> | T/o<br><sub>64s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.9s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>6.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>5.0s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.0s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>5.0s</sub> | N<br><sub>6.3s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>8.9s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.7s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>61s</sub> | N<br><sub>12s</sub> | N<br><sub>7.2s</sub> | T/o<br><sub>61s</sub> | N<br><sub>12s</sub> | N<br><sub>6.4s</sub> | N<br><sub>5.1s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>14s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.1s</sub> | T/o<br><sub>64s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.5s</sub> | N<br><sub>12s</sub> | N<br><sub>7.5s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.10` | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>71s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.0s</sub> | N<br><sub>8.4s</sub> | N<br><sub>9.3s</sub> | N<br><sub>5.7s</sub> | N<br><sub>7.8s</sub> | N<br><sub>5.1s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>9.7s</sub> | N<br><sub>10s</sub> | N<br><sub>9.6s</sub> | N<br><sub>10s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.6s</sub> | N<br><sub>10s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=15/36 (41.7%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>9.4s</sub> | T/o<br><sub>80s</sub> | Y<br><sub>8.7s</sub> | Y<br><sub>10s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>76s</sub> | Y<br><sub>17s</sub> | Y<br><sub>9.8s</sub> | Y<br><sub>7.9s</sub> | 6/9 (67%) |
| `0.10` | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | N<br><sub>10s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>75s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>39s</sub> | T/o<br><sub>64s</sub> | N<br><sub>38s</sub> | T/o<br><sub>64s</sub> | N<br><sub>17s</sub> | N<br><sub>45s</sub> | N<br><sub>49s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.8s</sub> | 9/9 (100%) |
| `0.10` | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>44s</sub> | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>88s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>9.7s</sub> | N<br><sub>9.4s</sub> | N<br><sub>7.7s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>9.0s</sub> | N<br><sub>11s</sub> | N<br><sub>7.3s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>22s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | N<br><sub>18s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | N<br><sub>17s</sub> | N<br><sub>15s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>62s</sub> | N<br><sub>25s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | N<br><sub>36s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>26s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>32s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>16s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>64s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | N<br><sub>58s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | N<br><sub>62s</sub> | N<br><sub>23s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>3.6s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.6s</sub> | 9/9 (100%) |
| `0.10` | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>27s</sub> | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>89s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>9.5s</sub> | N<br><sub>9.5s</sub> | N<br><sub>8.1s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | N<br><sub>9.4s</sub> | N<br><sub>13s</sub> | N<br><sub>7.7s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>19s</sub> | N<br><sub>16s</sub> | N<br><sub>13s</sub> | N<br><sub>17s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | N<br><sub>19s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>14s</sub> | N<br><sub>7.8s</sub> | N<br><sub>14s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.1s</sub> | N<br><sub>8.2s</sub> | N<br><sub>7.7s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>11s</sub> | N<br><sub>5.9s</sub> | N<br><sub>8.3s</sub> | T/o<br><sub>65s</sub> | N<br><sub>6.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>6.7s</sub> | N<br><sub>6.8s</sub> | N<br><sub>5.4s</sub> | N<br><sub>5.5s</sub> | N<br><sub>5.3s</sub> | N<br><sub>5.5s</sub> | N<br><sub>6.5s</sub> | N<br><sub>5.3s</sub> | N<br><sub>6.7s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>9.6s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.1s</sub> | N<br><sub>6.7s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>14s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.0s</sub> | N<br><sub>27s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.9s</sub> | N<br><sub>6.9s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.10` | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>67s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | N<br><sub>44s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.0s</sub> | N<br><sub>8.5s</sub> | N<br><sub>9.3s</sub> | N<br><sub>5.8s</sub> | N<br><sub>8.0s</sub> | N<br><sub>5.2s</sub> | N<br><sub>8.5s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>13s</sub> | N<br><sub>10s</sub> | N<br><sub>9.8s</sub> | N<br><sub>10s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.7s</sub> | N<br><sub>10s</sub> | N<br><sub>8.5s</sub> | N<br><sub>8.4s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.9) — Y=15/36 (41.7%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>10s</sub> | T/o<br><sub>66s</sub> | Y<br><sub>9.6s</sub> | Y<br><sub>11s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>17s</sub> | Y<br><sub>11s</sub> | Y<br><sub>8.8s</sub> | 6/9 (67%) |
| `0.10` | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>9.8s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>42s</sub> | N<br><sub>33s</sub> | N<br><sub>26s</sub> | T/o<br><sub>63s</sub> | N<br><sub>20s</sub> | T/o<br><sub>61s</sub> | N<br><sub>52s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | N<br><sub>22s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>13s</sub> | N<br><sub>13s</sub> | T/o<br><sub>156s</sub> | N<br><sub>17s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>17s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>61s</sub> | N<br><sub>32s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>43s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>30s</sub> | N<br><sub>27s</sub> | N<br><sub>31s</sub> | N<br><sub>25s</sub> | N<br><sub>18s</sub> | N<br><sub>25s</sub> | N<br><sub>26s</sub> | N<br><sub>19s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>35s</sub> | N<br><sub>24s</sub> | N<br><sub>31s</sub> | N<br><sub>24s</sub> | N<br><sub>33s</sub> | N<br><sub>26s</sub> | N<br><sub>27s</sub> | N<br><sub>20s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>23s</sub> | N<br><sub>27s</sub> | N<br><sub>14s</sub> | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>23s</sub> | N<br><sub>25s</sub> | N<br><sub>19s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>28s</sub> | N<br><sub>26s</sub> | N<br><sub>28s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | N<br><sub>23s</sub> | N<br><sub>24s</sub> | N<br><sub>22s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>8.8s</sub> | N<br><sub>15s</sub> | N<br><sub>17s</sub> | N<br><sub>10s</sub> | N<br><sub>14s</sub> | N<br><sub>8.7s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>24s</sub> | N<br><sub>19s</sub> | N<br><sub>18s</sub> | N<br><sub>19s</sub> | N<br><sub>15s</sub> | N<br><sub>16s</sub> | N<br><sub>19s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>70s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>61s</sub> | N<br><sub>27s</sub> | N<br><sub>32s</sub> | N<br><sub>54s</sub> | N<br><sub>25s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | N<br><sub>25s</sub> | N<br><sub>51s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>12s</sub> | N<br><sub>9.5s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>7.3s</sub> | N<br><sub>11s</sub> | N<br><sub>8.8s</sub> | N<br><sub>13s</sub> | N<br><sub>8.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | N<br><sub>55s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>63s</sub> | N<br><sub>23s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>16s</sub> | N<br><sub>16s</sub> | T/o<br><sub>177s</sub> | N<br><sub>21s</sub> | N<br><sub>14s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>49s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>65s</sub> | N<br><sub>27s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>43s</sub> | T/o<br><sub>64s</sub> | N<br><sub>36s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>14s</sub> | N<br><sub>28s</sub> | N<br><sub>18s</sub> | N<br><sub>22s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>25s</sub> | N<br><sub>26s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>31s</sub> | N<br><sub>20s</sub> | N<br><sub>36s</sub> | N<br><sub>23s</sub> | N<br><sub>24s</sub> | N<br><sub>22s</sub> | N<br><sub>27s</sub> | N<br><sub>25s</sub> | N<br><sub>32s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>26s</sub> | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>25s</sub> | N<br><sub>18s</sub> | N<br><sub>20s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>27s</sub> | N<br><sub>26s</sub> | N<br><sub>27s</sub> | N<br><sub>20s</sub> | N<br><sub>28s</sub> | N<br><sub>22s</sub> | N<br><sub>24s</sub> | N<br><sub>21s</sub> | N<br><sub>30s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>8.8s</sub> | N<br><sub>15s</sub> | N<br><sub>17s</sub> | N<br><sub>10s</sub> | N<br><sub>14s</sub> | N<br><sub>8.8s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>23s</sub> | N<br><sub>19s</sub> | N<br><sub>18s</sub> | N<br><sub>19s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | N<br><sub>19s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>15s</sub> | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | N<br><sub>7.5s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.1s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>8.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>8.8s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.2s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.9s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>5.0s</sub> | N<br><sub>5.1s</sub> | N<br><sub>4.8s</sub> | N<br><sub>5.9s</sub> | N<br><sub>4.8s</sub> | N<br><sub>6.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>4.8s</sub> | N<br><sub>6.1s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>8.4s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>62s</sub> | N<br><sub>5.9s</sub> | N<br><sub>21s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.2s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>14s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.0s</sub> | N<br><sub>27s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>6.8s</sub> | N<br><sub>9.5s</sub> | N<br><sub>7.2s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>24s</sub> | N<br><sub>20s</sub> | N<br><sub>12s</sub> | T/o<br><sub>62s</sub> | N<br><sub>44s</sub> | N<br><sub>13s</sub> | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>23s</sub> | N<br><sub>10.0s</sub> | N<br><sub>11s</sub> | N<br><sub>32s</sub> | N<br><sub>9.8s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>9.9s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>14s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>68s</sub> | T/o<br><sub>225s</sub> | T/o<br><sub>145s</sub> | T/o<br><sub>228s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>15277s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>13s</sub> | N<br><sub>18s</sub> | N<br><sub>14s</sub> | N<br><sub>20s</sub> | N<br><sub>13s</sub> | N<br><sub>22s</sub> | N<br><sub>20s</sub> | N<br><sub>13s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | N<br><sub>22s</sub> | N<br><sub>15s</sub> | N<br><sub>17s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>17s</sub> | N<br><sub>7.8s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>8.8s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>14s</sub> | N<br><sub>27s</sub> | N<br><sub>15s</sub> | N<br><sub>12s</sub> | N<br><sub>15s</sub> | N<br><sub>14s</sub> | N<br><sub>16s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | – | N<br><sub>5.7s</sub> | N<br><sub>5.7s</sub> | N<br><sub>4.8s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.0s</sub> | N<br><sub>5.5s</sub> | N<br><sub>7.5s</sub> | N<br><sub>4.9s</sub> | N<br><sub>8.0s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>12s</sub> | N<br><sub>9.7s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.7s</sub> | N<br><sub>7.9s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.6s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.0s</sub> | 0/9 (0%) |

### Class 1

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=13/36 (36.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>60s</sub> | 4/9 (44%) |
| `0.10` | T/o<br><sub>61s</sub> | – | N<br><sub>9.9s</sub> | N<br><sub>9.9s</sub> | T/o<br><sub>61s</sub> | N<br><sub>10.0s</sub> | T/o<br><sub>61s</sub> | N<br><sub>10.0s</sub> | T/o<br><sub>61s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | – | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>18s</sub> | N<br><sub>12s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>23s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | N<br><sub>47s</sub> | N<br><sub>23s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>18s</sub> | N<br><sub>49s</sub> | N<br><sub>21s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=21/36 (58.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>51s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>53s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.20` | N<br><sub>10s</sub> | – | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.9) — Y=12/36 (33.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>3.2s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>3.2s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 3/9 (33%) |
| `0.10` | T/o<br><sub>66s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>33s</sub> | – | N<br><sub>31s</sub> | N<br><sub>33s</sub> | N<br><sub>32s</sub> | N<br><sub>30s</sub> | N<br><sub>33s</sub> | N<br><sub>32s</sub> | T/o<br><sub>71s</sub> | N<br><sub>32s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>20s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>8.4s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | – | N<br><sub>8.8s</sub> | T/o<br><sub>62s</sub> | N<br><sub>11s</sub> | T/o<br><sub>61s</sub> | N<br><sub>53s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.2s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | – | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=13/36 (36.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>63s</sub> | 4/9 (44%) |
| `0.10` | T/o<br><sub>61s</sub> | – | N<br><sub>16s</sub> | N<br><sub>15s</sub> | T/o<br><sub>60s</sub> | N<br><sub>16s</sub> | T/o<br><sub>60s</sub> | N<br><sub>15s</sub> | T/o<br><sub>61s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>29s</sub> | – | N<br><sub>17s</sub> | N<br><sub>16s</sub> | N<br><sub>27s</sub> | N<br><sub>16s</sub> | N<br><sub>28s</sub> | N<br><sub>16s</sub> | N<br><sub>25s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>74s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | N<br><sub>42s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | N<br><sub>46s</sub> | N<br><sub>27s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | – | T/o<br><sub>78s</sub> | N<br><sub>34s</sub> | N<br><sub>29s</sub> | N<br><sub>33s</sub> | T/o<br><sub>75s</sub> | N<br><sub>33s</sub> | N<br><sub>32s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | – | N<br><sub>20s</sub> | N<br><sub>16s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | N<br><sub>24s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) — Y=12/36 (33.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.3s</sub> | – | Y<br><sub>2.3s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.8s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>3.8s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>4.0s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>3.9s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>3.9s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.10` | T/o<br><sub>63s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>52s</sub> | – | N<br><sub>49s</sub> | N<br><sub>52s</sub> | T/o<br><sub>67s</sub> | N<br><sub>48s</sub> | N<br><sub>54s</sub> | N<br><sub>52s</sub> | T/o<br><sub>104s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>33s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>13s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | – | N<br><sub>19s</sub> | T/o<br><sub>66s</sub> | N<br><sub>20s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>21s</sub> | – | N<br><sub>19s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>25s</sub> | – | N<br><sub>24s</sub> | N<br><sub>23s</sub> | N<br><sub>24s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>24s</sub> | N<br><sub>24s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=12/36 (33.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>19s</sub> | – | N<br><sub>57s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>26s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>12s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.10` | T/o<br><sub>60s</sub> | – | N<br><sub>11s</sub> | N<br><sub>14s</sub> | T/o<br><sub>62s</sub> | N<br><sub>13s</sub> | T/o<br><sub>66s</sub> | N<br><sub>10s</sub> | T/o<br><sub>64s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>25s</sub> | – | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>26s</sub> | N<br><sub>18s</sub> | T/o<br><sub>70s</sub> | N<br><sub>18s</sub> | T/o<br><sub>67s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>30s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>14s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | N<br><sub>19s</sub> | N<br><sub>13s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>18s</sub> | – | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>19s</sub> | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | – | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>23s</sub> | N<br><sub>22s</sub> | N<br><sub>28s</sub> | N<br><sub>26s</sub> | N<br><sub>25s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=11/36 (30.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 2/9 (22%) |
| `0.10` | T/o<br><sub>62s</sub> | – | N<br><sub>10s</sub> | N<br><sub>11s</sub> | T/o<br><sub>64s</sub> | N<br><sub>14s</sub> | T/o<br><sub>64s</sub> | N<br><sub>13s</sub> | T/o<br><sub>92s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>29s</sub> | – | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>30s</sub> | N<br><sub>17s</sub> | T/o<br><sub>62s</sub> | N<br><sub>17s</sub> | T/o<br><sub>64s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=11/36 (30.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.3s</sub> | – | Y<br><sub>2.3s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>47s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>27s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | 2/9 (22%) |
| `0.10` | T/o<br><sub>68s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>102s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>26s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | – | N<br><sub>12s</sub> | T/o<br><sub>62s</sub> | N<br><sub>19s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>21s</sub> | – | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | – | N<br><sub>24s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=14/36 (38.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>60s</sub> | 4/9 (44%) |
| `0.10` | T/o<br><sub>61s</sub> | – | N<br><sub>9.8s</sub> | N<br><sub>9.8s</sub> | T/o<br><sub>60s</sub> | N<br><sub>9.9s</sub> | Y<br><sub>60s</sub> | N<br><sub>9.8s</sub> | T/o<br><sub>61s</sub> | N<br><sub>9.8s</sub> | 1/9 (11%) |
| `0.20` | N<br><sub>17s</sub> | – | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>17s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>22s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | N<br><sub>46s</sub> | N<br><sub>23s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>19s</sub> | N<br><sub>16s</sub> | N<br><sub>18s</sub> | N<br><sub>48s</sub> | N<br><sub>27s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=21/36 (58.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>49s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>51s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>58s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.20` | N<br><sub>10s</sub> | – | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>13s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>9.8s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=12/36 (33.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.1s</sub> | – | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.1s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>3.1s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>3.1s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.10` | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>32s</sub> | – | N<br><sub>30s</sub> | N<br><sub>32s</sub> | T/o<br><sub>70s</sub> | N<br><sub>29s</sub> | N<br><sub>33s</sub> | N<br><sub>32s</sub> | T/o<br><sub>69s</sub> | N<br><sub>30s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>19s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>8.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | – | N<br><sub>8.7s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>61s</sub> | N<br><sub>54s</sub> | N<br><sub>7.9s</sub> | N<br><sub>8.5s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | – | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=13/36 (36.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>61s</sub> | 4/9 (44%) |
| `0.10` | T/o<br><sub>61s</sub> | – | N<br><sub>14s</sub> | N<br><sub>14s</sub> | T/o<br><sub>61s</sub> | N<br><sub>16s</sub> | T/o<br><sub>60s</sub> | N<br><sub>14s</sub> | T/o<br><sub>61s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | – | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>26s</sub> | N<br><sub>16s</sub> | N<br><sub>27s</sub> | N<br><sub>16s</sub> | N<br><sub>25s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | N<br><sub>43s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | N<br><sub>40s</sub> | N<br><sub>28s</sub> | N<br><sub>29s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>70s</sub> | – | T/o<br><sub>79s</sub> | N<br><sub>37s</sub> | N<br><sub>31s</sub> | N<br><sub>35s</sub> | T/o<br><sub>61s</sub> | N<br><sub>42s</sub> | N<br><sub>35s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>21s</sub> | – | N<br><sub>21s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | N<br><sub>24s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=12/36 (33.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.3s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>4.1s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>4.0s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>4.0s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 3/9 (33%) |
| `0.10` | T/o<br><sub>61s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>48s</sub> | – | N<br><sub>45s</sub> | N<br><sub>48s</sub> | T/o<br><sub>63s</sub> | N<br><sub>44s</sub> | N<br><sub>49s</sub> | N<br><sub>47s</sub> | T/o<br><sub>98s</sub> | N<br><sub>44s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>35s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>12s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | – | N<br><sub>16s</sub> | T/o<br><sub>68s</sub> | N<br><sub>19s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>21s</sub> | – | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | – | N<br><sub>24s</sub> | N<br><sub>25s</sub> | N<br><sub>24s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=12/36 (33.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>20s</sub> | – | N<br><sub>58s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>24s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>12s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 3/9 (33%) |
| `0.10` | T/o<br><sub>61s</sub> | – | N<br><sub>8.7s</sub> | N<br><sub>11s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>68s</sub> | N<br><sub>10s</sub> | T/o<br><sub>69s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>22s</sub> | – | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>20s</sub> | N<br><sub>13s</sub> | T/o<br><sub>85s</sub> | N<br><sub>15s</sub> | T/o<br><sub>68s</sub> | N<br><sub>18s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>31s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>13s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>20s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | N<br><sub>18s</sub> | N<br><sub>10s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>20s</sub> | – | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | N<br><sub>21s</sub> | N<br><sub>19s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | – | N<br><sub>23s</sub> | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>23s</sub> | N<br><sub>25s</sub> | N<br><sub>27s</sub> | N<br><sub>26s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=11/36 (30.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.10` | T/o<br><sub>62s</sub> | – | N<br><sub>14s</sub> | N<br><sub>13s</sub> | T/o<br><sub>61s</sub> | N<br><sub>18s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | T/o<br><sub>106s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>31s</sub> | – | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>29s</sub> | N<br><sub>17s</sub> | T/o<br><sub>86s</sub> | N<br><sub>16s</sub> | N<br><sub>23s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=11/36 (30.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.3s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>47s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | Y<br><sub>29s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 2/9 (22%) |
| `0.10` | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>98s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>37s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>12s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | – | N<br><sub>15s</sub> | T/o<br><sub>68s</sub> | N<br><sub>20s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>22s</sub> | – | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | – | N<br><sub>25s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>22s</sub> | N<br><sub>24s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.99) — Y=12/36 (33.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>23s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>28s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>13s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 3/9 (33%) |
| `0.10` | T/o<br><sub>61s</sub> | – | N<br><sub>9.7s</sub> | N<br><sub>13s</sub> | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | T/o<br><sub>65s</sub> | N<br><sub>10s</sub> | T/o<br><sub>62s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | – | N<br><sub>18s</sub> | N<br><sub>17s</sub> | N<br><sub>24s</sub> | N<br><sub>16s</sub> | T/o<br><sub>64s</sub> | N<br><sub>16s</sub> | T/o<br><sub>64s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>30s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>13s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>19s</sub> | N<br><sub>13s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>19s</sub> | – | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | – | N<br><sub>23s</sub> | N<br><sub>23s</sub> | N<br><sub>23s</sub> | N<br><sub>23s</sub> | N<br><sub>22s</sub> | N<br><sub>25s</sub> | N<br><sub>23s</sub> | N<br><sub>23s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=11/36 (30.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.10` | T/o<br><sub>62s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | T/o<br><sub>62s</sub> | N<br><sub>14s</sub> | T/o<br><sub>60s</sub> | N<br><sub>12s</sub> | T/o<br><sub>94s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>29s</sub> | – | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>30s</sub> | N<br><sub>17s</sub> | N<br><sub>23s</sub> | N<br><sub>16s</sub> | N<br><sub>24s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | – | N<br><sub>15s</sub> | N<br><sub>16s</sub> | T/o<br><sub>63s</sub> | N<br><sub>16s</sub> | T/o<br><sub>62s</sub> | N<br><sub>16s</sub> | T/o<br><sub>64s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>79s</sub> | – | N<br><sub>29s</sub> | N<br><sub>29s</sub> | T/o<br><sub>71s</sub> | N<br><sub>43s</sub> | T/o<br><sub>75s</sub> | N<br><sub>29s</sub> | T/o<br><sub>71s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>21s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | – | N<br><sub>33s</sub> | T/o<br><sub>62s</sub> | N<br><sub>19s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>9.5s</sub> | N<br><sub>12s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>25s</sub> | – | N<br><sub>16s</sub> | N<br><sub>23s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>359s</sub> | – | T/o<br><sub>300s</sub> | T/o<br><sub>77s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>22s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | T/o<br><sub>152s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>2.4s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>32s</sub> | – | N<br><sub>26s</sub> | T/o<br><sub>61s</sub> | N<br><sub>23s</sub> | N<br><sub>22s</sub> | N<br><sub>31s</sub> | N<br><sub>30s</sub> | N<br><sub>28s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>43s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>34s</sub> | N<br><sub>43s</sub> | N<br><sub>51s</sub> | N<br><sub>57s</sub> | N<br><sub>60s</sub> | N<br><sub>52s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>325s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>29s</sub> | – | N<br><sub>26s</sub> | N<br><sub>39s</sub> | N<br><sub>30s</sub> | N<br><sub>30s</sub> | N<br><sub>28s</sub> | N<br><sub>34s</sub> | N<br><sub>32s</sub> | N<br><sub>32s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | – | N<br><sub>40s</sub> | N<br><sub>50s</sub> | N<br><sub>35s</sub> | N<br><sub>40s</sub> | N<br><sub>54s</sub> | N<br><sub>41s</sub> | N<br><sub>41s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>31s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>12s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | – | N<br><sub>15s</sub> | T/o<br><sub>68s</sub> | N<br><sub>20s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>65s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>24s</sub> | – | N<br><sub>23s</sub> | N<br><sub>23s</sub> | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | – | N<br><sub>25s</sub> | N<br><sub>24s</sub> | N<br><sub>23s</sub> | N<br><sub>27s</sub> | N<br><sub>26s</sub> | N<br><sub>26s</sub> | N<br><sub>26s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

### Class 2

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>32s</sub> | Y<br><sub>23s</sub> | – | Y<br><sub>37s</sub> | Y<br><sub>15s</sub> | Y<br><sub>22s</sub> | Y<br><sub>16s</sub> | Y<br><sub>50s</sub> | Y<br><sub>26s</sub> | Y<br><sub>15s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>39s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>23s</sub> | N<br><sub>18s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | N<br><sub>56s</sub> | N<br><sub>12s</sub> | N<br><sub>7.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | T/o<br><sub>65s</sub> | – | N<br><sub>47s</sub> | N<br><sub>16s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | N<br><sub>35s</sub> | N<br><sub>16s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | N<br><sub>17s</sub> | – | N<br><sub>18s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | N<br><sub>24s</sub> | N<br><sub>24s</sub> | N<br><sub>20s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.2s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>4.3s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.3s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>60s</sub> | N<br><sub>4.0s</sub> | N<br><sub>5.7s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>40s</sub> | N<br><sub>9.1s</sub> | N<br><sub>57s</sub> | N<br><sub>6.7s</sub> | N<br><sub>57s</sub> | N<br><sub>4.8s</sub> | N<br><sub>5.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.8s</sub> | N<br><sub>9.3s</sub> | – | N<br><sub>7.8s</sub> | N<br><sub>7.7s</sub> | N<br><sub>16s</sub> | N<br><sub>7.8s</sub> | N<br><sub>10s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>15s</sub> | N<br><sub>28s</sub> | N<br><sub>48s</sub> | N<br><sub>59s</sub> | N<br><sub>23s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=20/36 (55.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | Y<br><sub>52s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>29s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>10s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>29s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>30s</sub> | Y<br><sub>7.8s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | N<br><sub>21s</sub> | – | N<br><sub>19s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | N<br><sub>18s</sub> | N<br><sub>20s</sub> | T/o<br><sub>94s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>4.8s</sub> | N<br><sub>5.5s</sub> | – | N<br><sub>4.0s</sub> | T/o<br><sub>60s</sub> | N<br><sub>5.6s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>3.7s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>33s</sub> | N<br><sub>7.6s</sub> | N<br><sub>47s</sub> | N<br><sub>6.5s</sub> | N<br><sub>46s</sub> | N<br><sub>4.2s</sub> | N<br><sub>4.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.4s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>6.5s</sub> | N<br><sub>6.4s</sub> | N<br><sub>13s</sub> | N<br><sub>6.5s</sub> | N<br><sub>8.0s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>7.0s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>29s</sub> | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>49s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>5.8s</sub> | T/o<br><sub>64s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.9s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>4.4s</sub> | N<br><sub>24s</sub> | T/o<br><sub>61s</sub> | N<br><sub>32s</sub> | T/o<br><sub>61s</sub> | N<br><sub>3.4s</sub> | N<br><sub>3.8s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>16s</sub> | T/o<br><sub>69s</sub> | – | N<br><sub>5.3s</sub> | N<br><sub>4.1s</sub> | N<br><sub>5.8s</sub> | N<br><sub>7.7s</sub> | T/o<br><sub>61s</sub> | N<br><sub>3.6s</sub> | N<br><sub>6.4s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.6s</sub> | N<br><sub>8.8s</sub> | – | N<br><sub>7.8s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.6s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>4.5s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.9s</sub> | N<br><sub>15s</sub> | N<br><sub>8.9s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | N<br><sub>13s</sub> | – | N<br><sub>9.4s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.7s</sub> | T/o<br><sub>68s</sub> | N<br><sub>6.7s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>96s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>4.3s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>3.7s</sub> | T/o<br><sub>62s</sub> | N<br><sub>4.3s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>3.3s</sub> | N<br><sub>4.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.4s</sub> | T/o<br><sub>69s</sub> | – | N<br><sub>29s</sub> | N<br><sub>6.8s</sub> | N<br><sub>42s</sub> | N<br><sub>5.8s</sub> | N<br><sub>42s</sub> | N<br><sub>3.7s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>5.7s</sub> | N<br><sub>6.7s</sub> | – | N<br><sub>5.8s</sub> | N<br><sub>5.7s</sub> | N<br><sub>12s</sub> | N<br><sub>5.8s</sub> | N<br><sub>7.2s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.7s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>22s</sub> | Y<br><sub>22s</sub> | – | Y<br><sub>34s</sub> | Y<br><sub>14s</sub> | Y<br><sub>21s</sub> | Y<br><sub>15s</sub> | Y<br><sub>47s</sub> | Y<br><sub>24s</sub> | Y<br><sub>16s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>37s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>21s</sub> | N<br><sub>17s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | N<br><sub>55s</sub> | N<br><sub>12s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | T/o<br><sub>67s</sub> | – | N<br><sub>49s</sub> | N<br><sub>11s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | N<br><sub>33s</sub> | N<br><sub>28s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | N<br><sub>17s</sub> | – | N<br><sub>20s</sub> | N<br><sub>26s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.1s</sub> | N<br><sub>5.7s</sub> | – | N<br><sub>4.4s</sub> | T/o<br><sub>62s</sub> | N<br><sub>5.2s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | N<br><sub>4.0s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>38s</sub> | N<br><sub>8.4s</sub> | N<br><sub>54s</sub> | N<br><sub>7.4s</sub> | N<br><sub>56s</sub> | N<br><sub>4.5s</sub> | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.6s</sub> | N<br><sub>8.8s</sub> | – | N<br><sub>7.6s</sub> | N<br><sub>7.6s</sub> | N<br><sub>16s</sub> | N<br><sub>7.7s</sub> | N<br><sub>9.6s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.5s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | N<br><sub>9.4s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>16s</sub> | T/o<br><sub>64s</sub> | – | N<br><sub>14s</sub> | N<br><sub>28s</sub> | N<br><sub>45s</sub> | T/o<br><sub>63s</sub> | N<br><sub>21s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=21/36 (58.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | Y<br><sub>52s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>37s</sub> | Y<br><sub>28s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | Y<br><sub>2.1s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>11s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>29s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>30s</sub> | Y<br><sub>7.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>20s</sub> | N<br><sub>20s</sub> | – | N<br><sub>18s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | N<br><sub>17s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.0s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>4.4s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.1s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | N<br><sub>3.9s</sub> | N<br><sub>5.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | T/o<br><sub>64s</sub> | – | N<br><sub>40s</sub> | N<br><sub>9.0s</sub> | N<br><sub>58s</sub> | N<br><sub>7.2s</sub> | N<br><sub>55s</sub> | N<br><sub>4.5s</sub> | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.2s</sub> | N<br><sub>9.1s</sub> | – | N<br><sub>7.5s</sub> | N<br><sub>7.6s</sub> | N<br><sub>16s</sub> | N<br><sub>7.3s</sub> | N<br><sub>9.3s</sub> | N<br><sub>7.2s</sub> | N<br><sub>7.2s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>8.3s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>35s</sub> | N<br><sub>14s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>60s</sub> | T/o<br><sub>64s</sub> | – | N<br><sub>6.9s</sub> | T/o<br><sub>66s</sub> | N<br><sub>6.7s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.0s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>4.4s</sub> | N<br><sub>24s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>3.4s</sub> | N<br><sub>4.1s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>15s</sub> | T/o<br><sub>69s</sub> | – | N<br><sub>5.3s</sub> | N<br><sub>4.1s</sub> | N<br><sub>5.7s</sub> | N<br><sub>7.7s</sub> | N<br><sub>55s</sub> | N<br><sub>3.5s</sub> | N<br><sub>6.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.6s</sub> | N<br><sub>8.8s</sub> | – | N<br><sub>7.4s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.6s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>3.8s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.7s</sub> | N<br><sub>13s</sub> | N<br><sub>4.6s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | N<br><sub>11s</sub> | – | N<br><sub>7.8s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.7s</sub> | N<br><sub>11s</sub> | N<br><sub>6.1s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>4.3s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>3.6s</sub> | T/o<br><sub>62s</sub> | N<br><sub>4.3s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>3.3s</sub> | N<br><sub>4.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.3s</sub> | T/o<br><sub>68s</sub> | – | N<br><sub>29s</sub> | N<br><sub>6.8s</sub> | N<br><sub>43s</sub> | N<br><sub>5.8s</sub> | N<br><sub>42s</sub> | N<br><sub>3.7s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>5.7s</sub> | N<br><sub>6.7s</sub> | – | N<br><sub>5.8s</sub> | N<br><sub>5.7s</sub> | N<br><sub>11s</sub> | N<br><sub>5.8s</sub> | N<br><sub>7.1s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.7s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>23s</sub> | Y<br><sub>24s</sub> | – | Y<br><sub>37s</sub> | Y<br><sub>15s</sub> | Y<br><sub>22s</sub> | Y<br><sub>16s</sub> | Y<br><sub>50s</sub> | Y<br><sub>26s</sub> | Y<br><sub>14s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>82s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>40s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>24s</sub> | N<br><sub>18s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>59s</sub> | N<br><sub>13s</sub> | N<br><sub>7.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>39s</sub> | N<br><sub>16s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>37s</sub> | N<br><sub>17s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>91s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | N<br><sub>18s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | N<br><sub>51s</sub> | T/o<br><sub>81s</sub> | N<br><sub>19s</sub> | N<br><sub>53s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>17s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>7.0s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>41s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>17s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | N<br><sub>22s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | N<br><sub>9.6s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>27092s</sub> | T/o<br><sub>67s</sub> | – | N<br><sub>27s</sub> | N<br><sub>38s</sub> | N<br><sub>16s</sub> | N<br><sub>46s</sub> | T/o<br><sub>61s</sub> | N<br><sub>8.3s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>16s</sub> | N<br><sub>18s</sub> | – | N<br><sub>20s</sub> | N<br><sub>27s</sub> | N<br><sub>18s</sub> | N<br><sub>24s</sub> | N<br><sub>38s</sub> | N<br><sub>18s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>92s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | N<br><sub>7.2s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>24499s</sub> | T/o<br><sub>69s</sub> | – | N<br><sub>19s</sub> | T/o<br><sub>65s</sub> | N<br><sub>13s</sub> | N<br><sub>21s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.9s</sub> | N<br><sub>9.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>30s</sub> | T/o<br><sub>12137s</sub> | – | N<br><sub>13s</sub> | N<br><sub>19s</sub> | N<br><sub>17s</sub> | N<br><sub>18s</sub> | N<br><sub>20s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.2s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>4.3s</sub> | T/o<br><sub>62s</sub> | N<br><sub>5.2s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.1s</sub> | N<br><sub>5.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | T/o<br><sub>65s</sub> | – | N<br><sub>42s</sub> | N<br><sub>9.2s</sub> | N<br><sub>58s</sub> | N<br><sub>7.8s</sub> | N<br><sub>59s</sub> | N<br><sub>4.7s</sub> | N<br><sub>5.4s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.1s</sub> | N<br><sub>9.2s</sub> | – | N<br><sub>8.1s</sub> | N<br><sub>7.9s</sub> | N<br><sub>16s</sub> | N<br><sub>8.0s</sub> | N<br><sub>10.0s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>15s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | N<br><sub>9.8s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | T/o<br><sub>64s</sub> | – | N<br><sub>14s</sub> | N<br><sub>30s</sub> | N<br><sub>47s</sub> | T/o<br><sub>62s</sub> | N<br><sub>23s</sub> | N<br><sub>16s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=20/36 (55.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | Y<br><sub>54s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>27s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | N<br><sub>14s</sub> | – | N<br><sub>50s</sub> | N<br><sub>39s</sub> | N<br><sub>37s</sub> | N<br><sub>61s</sub> | N<br><sub>15s</sub> | N<br><sub>51s</sub> | N<br><sub>62s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>20s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>10s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | N<br><sub>29s</sub> | N<br><sub>9.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>13s</sub> | T/o<br><sub>63s</sub> | N<br><sub>17s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>23s</sub> | N<br><sub>9.8s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | N<br><sub>9.5s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>27304s</sub> | T/o<br><sub>82s</sub> | – | N<br><sub>19s</sub> | N<br><sub>33s</sub> | T/o<br><sub>61s</sub> | N<br><sub>59s</sub> | T/o<br><sub>67s</sub> | N<br><sub>8.9s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>28413s</sub> | N<br><sub>9.4s</sub> | – | N<br><sub>11s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>8.8s</sub> | N<br><sub>10.0s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | N<br><sub>7.9s</sub> | – | N<br><sub>5.6s</sub> | N<br><sub>25s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>69s</sub> | N<br><sub>7.9s</sub> | N<br><sub>8.6s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>24571s</sub> | N<br><sub>7.0s</sub> | – | N<br><sub>8.0s</sub> | N<br><sub>8.5s</sub> | N<br><sub>12s</sub> | N<br><sub>7.8s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.5s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>8598s</sub> | N<br><sub>12s</sub> | – | N<br><sub>16s</sub> | N<br><sub>12s</sub> | N<br><sub>21s</sub> | N<br><sub>9.0s</sub> | N<br><sub>23s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.7s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.2s</sub> | N<br><sub>6.1s</sub> | – | N<br><sub>4.3s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.2s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.1s</sub> | N<br><sub>5.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>40s</sub> | N<br><sub>8.6s</sub> | N<br><sub>57s</sub> | N<br><sub>7.3s</sub> | N<br><sub>56s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.4s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.6s</sub> | N<br><sub>8.8s</sub> | – | N<br><sub>7.5s</sub> | N<br><sub>7.2s</sub> | N<br><sub>17s</sub> | N<br><sub>7.9s</sub> | N<br><sub>19s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>7.9s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | N<br><sub>33s</sub> | N<br><sub>13s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>57s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>6.3s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.0s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.8s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>5.6s</sub> | N<br><sub>34s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | N<br><sub>4.2s</sub> | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>24s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>6.4s</sub> | N<br><sub>5.7s</sub> | N<br><sub>8.3s</sub> | N<br><sub>12s</sub> | T/o<br><sub>67s</sub> | N<br><sub>4.9s</sub> | N<br><sub>9.4s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>10s</sub> | N<br><sub>14s</sub> | – | N<br><sub>12s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>83s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>5.5s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.9s</sub> | N<br><sub>20s</sub> | N<br><sub>7.0s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | N<br><sub>19s</sub> | – | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | N<br><sub>9.1s</sub> | T/o<br><sub>64s</sub> | N<br><sub>8.9s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>121s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>174s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>10s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>6.0s</sub> | T/o<br><sub>71s</sub> | N<br><sub>11s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.0s</sub> | N<br><sub>8.8s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>12s</sub> | – | N<br><sub>9.6s</sub> | N<br><sub>9.8s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | T/o<br><sub>68s</sub> | N<br><sub>9.4s</sub> | N<br><sub>9.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>17s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>112s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>9.9s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>34201s</sub> | T/o<br><sub>76s</sub> | – | N<br><sub>32s</sub> | N<br><sub>46s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>66s</sub> | N<br><sub>16s</sub> | N<br><sub>18s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>22s</sub> | N<br><sub>18s</sub> | – | N<br><sub>26s</sub> | N<br><sub>34s</sub> | N<br><sub>30s</sub> | N<br><sub>26s</sub> | N<br><sub>52s</sub> | N<br><sub>24s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>4.6s</sub> | N<br><sub>27s</sub> | N<br><sub>8.1s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>4.5s</sub> | N<br><sub>6.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.5s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>9.1s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>8.0s</sub> | T/o<br><sub>63s</sub> | N<br><sub>6.4s</sub> | N<br><sub>8.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.9s</sub> | N<br><sub>12s</sub> | – | N<br><sub>14s</sub> | N<br><sub>10s</sub> | N<br><sub>10.0s</sub> | N<br><sub>9.1s</sub> | N<br><sub>13s</sub> | N<br><sub>8.6s</sub> | N<br><sub>9.8s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>4.3s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>3.6s</sub> | T/o<br><sub>62s</sub> | N<br><sub>4.3s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>3.3s</sub> | N<br><sub>4.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.4s</sub> | T/o<br><sub>69s</sub> | – | N<br><sub>30s</sub> | N<br><sub>6.9s</sub> | N<br><sub>43s</sub> | N<br><sub>5.0s</sub> | N<br><sub>42s</sub> | N<br><sub>3.7s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>5.7s</sub> | N<br><sub>6.7s</sub> | – | N<br><sub>5.8s</sub> | N<br><sub>5.7s</sub> | N<br><sub>12s</sub> | N<br><sub>5.8s</sub> | N<br><sub>7.2s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.7s</sub> | 0/9 (0%) |

### Class 3

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>7.6s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | N<br><sub>17s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | N<br><sub>14s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>61s</sub> | N<br><sub>28s</sub> | N<br><sub>20s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.3s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.5s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.5s</sub> | – | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>75s</sub> | – | N<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | N<br><sub>25s</sub> | T/o<br><sub>63s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.0s</sub> | – | N<br><sub>6.3s</sub> | N<br><sub>5.1s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.9s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.8s</sub> | – | N<br><sub>6.9s</sub> | N<br><sub>6.9s</sub> | N<br><sub>6.9s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.9s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | N<br><sub>21s</sub> | – | T/o<br><sub>66s</sub> | N<br><sub>21s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | N<br><sub>20s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | N<br><sub>23s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>70s</sub> | N<br><sub>65s</sub> | T/o<br><sub>70s</sub> | N<br><sub>44s</sub> | N<br><sub>36s</sub> | N<br><sub>58s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=32/36 (88.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | T/o<br><sub>61s</sub> | – | Y<br><sub>1.6s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 5/9 (56%) |

##### Impl L0→L1 (α=0.95) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.6s</sub> | Y<br><sub>4.5s</sub> | Y<br><sub>4.5s</sub> | – | Y<br><sub>4.5s</sub> | Y<br><sub>4.5s</sub> | Y<br><sub>4.5s</sub> | Y<br><sub>4.5s</sub> | Y<br><sub>4.5s</sub> | Y<br><sub>4.5s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>6.9s</sub> | Y<br><sub>6.9s</sub> | Y<br><sub>6.9s</sub> | – | Y<br><sub>6.9s</sub> | Y<br><sub>6.9s</sub> | Y<br><sub>6.9s</sub> | Y<br><sub>6.8s</sub> | Y<br><sub>6.8s</sub> | Y<br><sub>6.9s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | N<br><sub>41s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>10s</sub> | – | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | – | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.7s</sub> | N<br><sub>7.5s</sub> | N<br><sub>6.8s</sub> | – | N<br><sub>7.8s</sub> | N<br><sub>7.2s</sub> | N<br><sub>7.6s</sub> | N<br><sub>12s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.0s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.0s</sub> | – | N<br><sub>9.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>8.8s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.7s</sub> | N<br><sub>9.6s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.6s</sub> | N<br><sub>5.4s</sub> | N<br><sub>4.2s</sub> | – | N<br><sub>5.4s</sub> | N<br><sub>4.8s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.8s</sub> | N<br><sub>4.1s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.8s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.7s</sub> | – | N<br><sub>7.7s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>17s</sub> | N<br><sub>50s</sub> | N<br><sub>12s</sub> | – | N<br><sub>39s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>10s</sub> | N<br><sub>8.7s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>17s</sub> | N<br><sub>6.2s</sub> | N<br><sub>12s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.3s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | – | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>151s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>170s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>222s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.1s</sub> | N<br><sub>6.1s</sub> | N<br><sub>4.8s</sub> | – | N<br><sub>6.1s</sub> | N<br><sub>4.9s</sub> | N<br><sub>7.8s</sub> | N<br><sub>6.4s</sub> | N<br><sub>4.8s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.6s</sub> | N<br><sub>6.5s</sub> | N<br><sub>6.5s</sub> | – | N<br><sub>6.5s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.5s</sub> | N<br><sub>6.5s</sub> | N<br><sub>7.4s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>8.1s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>18s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>38s</sub> | T/o<br><sub>71s</sub> | N<br><sub>25s</sub> | N<br><sub>18s</sub> | N<br><sub>33s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.3s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | – | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | N<br><sub>25s</sub> | T/o<br><sub>63s</sub> | N<br><sub>60s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.6s</sub> | N<br><sub>6.8s</sub> | N<br><sub>5.0s</sub> | – | N<br><sub>6.2s</sub> | N<br><sub>5.0s</sub> | N<br><sub>7.3s</sub> | N<br><sub>8.0s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.7s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.7s</sub> | – | N<br><sub>6.7s</sub> | N<br><sub>6.8s</sub> | N<br><sub>7.0s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.3s</sub> | N<br><sub>8.5s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>21s</sub> | – | T/o<br><sub>66s</sub> | N<br><sub>21s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>31s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | N<br><sub>23s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>69s</sub> | N<br><sub>64s</sub> | T/o<br><sub>70s</sub> | N<br><sub>44s</sub> | N<br><sub>32s</sub> | N<br><sub>57s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=32/36 (88.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | T/o<br><sub>61s</sub> | – | Y<br><sub>1.6s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 5/9 (56%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.4s</sub> | Y<br><sub>4.4s</sub> | Y<br><sub>4.3s</sub> | – | Y<br><sub>4.4s</sub> | Y<br><sub>4.4s</sub> | Y<br><sub>4.3s</sub> | Y<br><sub>4.4s</sub> | Y<br><sub>4.4s</sub> | Y<br><sub>4.4s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>6.8s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | – | Y<br><sub>6.8s</sub> | Y<br><sub>6.9s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.8s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | N<br><sub>41s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>10s</sub> | – | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | – | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.8s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.8s</sub> | – | N<br><sub>7.9s</sub> | N<br><sub>7.2s</sub> | N<br><sub>7.5s</sub> | N<br><sub>15s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.8s</sub> | N<br><sub>9.6s</sub> | N<br><sub>4.8s</sub> | – | N<br><sub>9.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>9.0s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.8s</sub> | N<br><sub>9.7s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.7s</sub> | N<br><sub>6.1s</sub> | N<br><sub>4.2s</sub> | – | N<br><sub>4.3s</sub> | N<br><sub>4.7s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.7s</sub> | N<br><sub>4.0s</sub> | N<br><sub>4.7s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.4s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>7.6s</sub> | N<br><sub>7.7s</sub> | N<br><sub>9.3s</sub> | N<br><sub>8.0s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>38s</sub> | N<br><sub>11s</sub> | – | N<br><sub>38s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.7s</sub> | N<br><sub>6.0s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>17s</sub> | N<br><sub>5.0s</sub> | N<br><sub>12s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.8s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>89s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.1s</sub> | N<br><sub>6.2s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>6.2s</sub> | N<br><sub>5.1s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.0s</sub> | N<br><sub>4.9s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.7s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>6.5s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.9s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.4s</sub> | N<br><sub>7.4s</sub> | 0/9 (0%) |

### Class 4

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>36s</sub> | N<br><sub>18s</sub> | N<br><sub>41s</sub> | N<br><sub>23s</sub> | – | N<br><sub>27s</sub> | N<br><sub>37s</sub> | N<br><sub>37s</sub> | N<br><sub>24s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>38s</sub> | T/o<br><sub>69s</sub> | N<br><sub>45s</sub> | N<br><sub>37s</sub> | – | N<br><sub>25s</sub> | T/o<br><sub>70s</sub> | N<br><sub>45s</sub> | T/o<br><sub>73s</sub> | N<br><sub>41s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>31s</sub> | N<br><sub>25s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | – | N<br><sub>27s</sub> | T/o<br><sub>61s</sub> | N<br><sub>39s</sub> | T/o<br><sub>63s</sub> | N<br><sub>49s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.3s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>30s</sub> | N<br><sub>28s</sub> | N<br><sub>25s</sub> | N<br><sub>26s</sub> | – | N<br><sub>29s</sub> | N<br><sub>29s</sub> | N<br><sub>23s</sub> | N<br><sub>30s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>29s</sub> | N<br><sub>27s</sub> | N<br><sub>29s</sub> | N<br><sub>30s</sub> | – | N<br><sub>28s</sub> | N<br><sub>29s</sub> | N<br><sub>27s</sub> | N<br><sub>28s</sub> | N<br><sub>27s</sub> | 0/9 (0%) |

##### none (baseline) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>5.5s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>19s</sub> | Y<br><sub>20s</sub> | – | Y<br><sub>38s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>11s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>11s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>7.5s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.4s</sub> | – | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.3s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.0s</sub> | – | N<br><sub>7.9s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.7s</sub> | N<br><sub>8.1s</sub> | N<br><sub>8.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>9.9s</sub> | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.2s</sub> | N<br><sub>9.4s</sub> | N<br><sub>9.3s</sub> | N<br><sub>9.4s</sub> | – | N<br><sub>9.4s</sub> | N<br><sub>9.6s</sub> | N<br><sub>8.4s</sub> | N<br><sub>9.2s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>48s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>87s</sub> | N<br><sub>50s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>31s</sub> | T/o<br><sub>62s</sub> | N<br><sub>38s</sub> | N<br><sub>64s</sub> | – | N<br><sub>21s</sub> | T/o<br><sub>61s</sub> | N<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>20s</sub> | N<br><sub>22s</sub> | N<br><sub>47s</sub> | N<br><sub>35s</sub> | – | N<br><sub>14s</sub> | T/o<br><sub>66s</sub> | N<br><sub>22s</sub> | N<br><sub>13s</sub> | N<br><sub>23s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=19/36 (52.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 1/9 (11%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>54s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | T/o<br><sub>174s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | N<br><sub>20s</sub> | T/o<br><sub>65s</sub> | N<br><sub>18s</sub> | N<br><sub>23s</sub> | T/o<br><sub>545s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | N<br><sub>333s</sub> | N<br><sub>248s</sub> | N<br><sub>94s</sub> | – | T/o<br><sub>176s</sub> | T/o<br><sub>217s</sub> | N<br><sub>261s</sub> | N<br><sub>216s</sub> | N<br><sub>164s</sub> | 0/9 (0%) |

##### none (baseline) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>15s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.7s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>8.9s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>6.0s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.3s</sub> | – | N<br><sub>4.7s</sub> | N<br><sub>4.6s</sub> | N<br><sub>15s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.6s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.4s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.3s</sub> | – | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.9s</sub> | N<br><sub>9.1s</sub> | N<br><sub>8.9s</sub> | N<br><sub>9.0s</sub> | – | N<br><sub>9.0s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.9s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>4.2s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | N<br><sub>9.8s</sub> | T/o<br><sub>63s</sub> | N<br><sub>14s</sub> | – | N<br><sub>8.7s</sub> | T/o<br><sub>63s</sub> | N<br><sub>5.0s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.8s</sub> | N<br><sub>9.8s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.1s</sub> | – | N<br><sub>7.9s</sub> | N<br><sub>8.1s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.8s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>15s</sub> | Y<br><sub>9.0s</sub> | – | Y<br><sub>31s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>7.1s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>8.3s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>5.0s</sub> | N<br><sub>7.1s</sub> | N<br><sub>5.0s</sub> | N<br><sub>10s</sub> | – | N<br><sub>5.1s</sub> | N<br><sub>5.0s</sub> | N<br><sub>4.8s</sub> | N<br><sub>4.1s</sub> | N<br><sub>4.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>4.8s</sub> | N<br><sub>5.0s</sub> | – | N<br><sub>5.0s</sub> | N<br><sub>5.0s</sub> | N<br><sub>6.8s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.1s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.1s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>8.4s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.0s</sub> | N<br><sub>23s</sub> | – | N<br><sub>8.6s</sub> | N<br><sub>5.5s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.8s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.6s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.6s</sub> | N<br><sub>15s</sub> | – | N<br><sub>7.3s</sub> | N<br><sub>9.5s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.4s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.9s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>2.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>8.5s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>234s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | N<br><sub>23s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | N<br><sub>85s</sub> | T/o<br><sub>794s</sub> | 0/9 (0%) |

##### none (baseline) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>5.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>17s</sub> | Y<br><sub>18s</sub> | – | Y<br><sub>33s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>11s</sub> | T/o<br><sub>67s</sub> | Y<br><sub>9.9s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>6.7s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.1s</sub> | N<br><sub>5.8s</sub> | – | N<br><sub>5.2s</sub> | N<br><sub>5.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.3s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.9s</sub> | N<br><sub>7.1s</sub> | – | N<br><sub>7.1s</sub> | N<br><sub>7.1s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.9s</sub> | N<br><sub>7.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | – | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | N<br><sub>9.1s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | N<br><sub>17s</sub> | N<br><sub>39s</sub> | N<br><sub>23s</sub> | – | N<br><sub>25s</sub> | N<br><sub>34s</sub> | N<br><sub>33s</sub> | N<br><sub>33s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>6.1s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | N<br><sub>55s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>37s</sub> | T/o<br><sub>64s</sub> | N<br><sub>43s</sub> | N<br><sub>34s</sub> | – | N<br><sub>23s</sub> | T/o<br><sub>70s</sub> | N<br><sub>49s</sub> | T/o<br><sub>70s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>30s</sub> | N<br><sub>25s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>67s</sub> | – | N<br><sub>21s</sub> | T/o<br><sub>62s</sub> | N<br><sub>37s</sub> | T/o<br><sub>64s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.3s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>30s</sub> | N<br><sub>29s</sub> | N<br><sub>25s</sub> | N<br><sub>26s</sub> | – | N<br><sub>29s</sub> | N<br><sub>29s</sub> | N<br><sub>28s</sub> | N<br><sub>30s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>29s</sub> | N<br><sub>28s</sub> | N<br><sub>29s</sub> | N<br><sub>30s</sub> | – | N<br><sub>28s</sub> | N<br><sub>29s</sub> | N<br><sub>28s</sub> | N<br><sub>28s</sub> | N<br><sub>27s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>5.5s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>19s</sub> | Y<br><sub>20s</sub> | – | Y<br><sub>38s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>11s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>11s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>7.3s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>5.6s</sub> | N<br><sub>5.6s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | – | N<br><sub>7.9s</sub> | N<br><sub>7.9s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.1s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>15s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.2s</sub> | N<br><sub>9.4s</sub> | N<br><sub>9.3s</sub> | N<br><sub>9.4s</sub> | – | N<br><sub>9.4s</sub> | N<br><sub>9.6s</sub> | N<br><sub>8.4s</sub> | N<br><sub>9.3s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>45s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>88s</sub> | N<br><sub>50s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>92s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>31s</sub> | T/o<br><sub>62s</sub> | N<br><sub>27s</sub> | N<br><sub>51s</sub> | – | N<br><sub>15s</sub> | T/o<br><sub>61s</sub> | N<br><sub>60s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>20s</sub> | N<br><sub>22s</sub> | N<br><sub>47s</sub> | N<br><sub>35s</sub> | – | N<br><sub>16s</sub> | T/o<br><sub>61s</sub> | N<br><sub>33s</sub> | N<br><sub>13s</sub> | N<br><sub>23s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=19/36 (52.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 1/9 (11%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>54s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>23s</sub> | T/o<br><sub>62s</sub> | N<br><sub>19s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>166s</sub> | N<br><sub>21s</sub> | N<br><sub>18s</sub> | N<br><sub>28s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | N<br><sub>145s</sub> | N<br><sub>312s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>309s</sub> | T/o<br><sub>123s</sub> | N<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>394s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>16s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.6s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>8.8s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>6.0s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.3s</sub> | – | N<br><sub>4.7s</sub> | N<br><sub>4.7s</sub> | N<br><sub>5.5s</sub> | N<br><sub>5.4s</sub> | N<br><sub>4.7s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.3s</sub> | – | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.9s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.9s</sub> | N<br><sub>8.9s</sub> | – | N<br><sub>9.1s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.9s</sub> | N<br><sub>9.0s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>6.3s</sub> | T/o<br><sub>62s</sub> | N<br><sub>3.7s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>9.8s</sub> | T/o<br><sub>63s</sub> | N<br><sub>14s</sub> | – | N<br><sub>8.7s</sub> | N<br><sub>7.0s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.1s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.8s</sub> | N<br><sub>9.9s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.1s</sub> | – | N<br><sub>7.9s</sub> | N<br><sub>8.2s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.8s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>16s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>29s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>7.1s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>8.3s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>5.0s</sub> | N<br><sub>7.1s</sub> | N<br><sub>5.0s</sub> | N<br><sub>11s</sub> | – | N<br><sub>5.1s</sub> | N<br><sub>5.0s</sub> | N<br><sub>4.8s</sub> | N<br><sub>3.7s</sub> | N<br><sub>4.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>4.8s</sub> | N<br><sub>5.0s</sub> | – | N<br><sub>5.0s</sub> | N<br><sub>5.0s</sub> | N<br><sub>6.8s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.2s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.1s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>8.4s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>6.0s</sub> | N<br><sub>11s</sub> | – | N<br><sub>8.2s</sub> | N<br><sub>9.8s</sub> | N<br><sub>6.3s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.6s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.6s</sub> | N<br><sub>15s</sub> | – | N<br><sub>7.3s</sub> | N<br><sub>9.6s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.4s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | – | Y<br><sub>2.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>32s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>1242s</sub> | N<br><sub>43s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>88s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>14s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>29s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.1s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>8.3s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>5.7s</sub> | N<br><sub>5.0s</sub> | N<br><sub>4.3s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>4.4s</sub> | N<br><sub>4.3s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.0s</sub> | N<br><sub>4.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.8s</sub> | – | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | – | N<br><sub>8.3s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>59s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>73s</sub> | N<br><sub>37s</sub> | N<br><sub>22s</sub> | – | N<br><sub>24s</sub> | N<br><sub>34s</sub> | N<br><sub>34s</sub> | N<br><sub>15s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>6.2s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>78s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>39s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | N<br><sub>28s</sub> | – | N<br><sub>26s</sub> | T/o<br><sub>73s</sub> | N<br><sub>47s</sub> | T/o<br><sub>73s</sub> | N<br><sub>41s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>31s</sub> | N<br><sub>20s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | – | N<br><sub>25s</sub> | T/o<br><sub>64s</sub> | N<br><sub>37s</sub> | T/o<br><sub>61s</sub> | N<br><sub>49s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>30s</sub> | N<br><sub>26s</sub> | N<br><sub>32s</sub> | N<br><sub>9.7s</sub> | – | N<br><sub>27s</sub> | N<br><sub>27s</sub> | N<br><sub>15s</sub> | N<br><sub>29s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>36s</sub> | N<br><sub>20s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | – | N<br><sub>22s</sub> | N<br><sub>25s</sub> | N<br><sub>23s</sub> | N<br><sub>24s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>38s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>82s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>24s</sub> | T/o<br><sub>62s</sub> | N<br><sub>38s</sub> | N<br><sub>59s</sub> | – | N<br><sub>48s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>126s</sub> | T/o<br><sub>231s</sub> | T/o<br><sub>141s</sub> | T/o<br><sub>289s</sub> | – | T/o<br><sub>202s</sub> | T/o<br><sub>183s</sub> | T/o<br><sub>135s</sub> | T/o<br><sub>465s</sub> | T/o<br><sub>91s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>11s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>13s</sub> | – | N<br><sub>11s</sub> | N<br><sub>21s</sub> | N<br><sub>15s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>29s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>21s</sub> | – | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>18s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>30s</sub> | N<br><sub>24s</sub> | N<br><sub>22s</sub> | N<br><sub>25s</sub> | – | N<br><sub>25s</sub> | N<br><sub>29s</sub> | N<br><sub>24s</sub> | N<br><sub>27s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>36s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>10s</sub> | N<br><sub>24s</sub> | N<br><sub>9.7s</sub> | N<br><sub>9.9s</sub> | – | N<br><sub>8.8s</sub> | N<br><sub>9.5s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>8.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>14s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | – | N<br><sub>9.6s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | N<br><sub>21s</sub> | N<br><sub>22s</sub> | N<br><sub>24s</sub> | – | N<br><sub>19s</sub> | N<br><sub>23s</sub> | N<br><sub>19s</sub> | N<br><sub>21s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |

##### none (baseline) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>5.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>19s</sub> | Y<br><sub>20s</sub> | – | Y<br><sub>37s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>11s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>11s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>10s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.8s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>5.7s</sub> | N<br><sub>5.6s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.5s</sub> | N<br><sub>5.7s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.3s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.1s</sub> | – | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>9.5s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.9s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.1s</sub> | – | N<br><sub>9.1s</sub> | N<br><sub>9.2s</sub> | N<br><sub>8.1s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>41s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>30s</sub> | N<br><sub>40s</sub> | N<br><sub>36s</sub> | N<br><sub>50s</sub> | – | N<br><sub>24s</sub> | T/o<br><sub>61s</sub> | N<br><sub>58s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | N<br><sub>21s</sub> | N<br><sub>45s</sub> | N<br><sub>27s</sub> | – | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | N<br><sub>32s</sub> | N<br><sub>13s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=19/36 (52.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.7s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 1/9 (11%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>2.6s</sub> | – | Y<br><sub>2.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>2.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>21s</sub> | N<br><sub>18s</sub> | N<br><sub>23s</sub> | N<br><sub>7.4s</sub> | – | N<br><sub>19s</sub> | N<br><sub>19s</sub> | N<br><sub>11s</sub> | N<br><sub>20s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | N<br><sub>17s</sub> | N<br><sub>15s</sub> | N<br><sub>18s</sub> | – | N<br><sub>37s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>30s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>921s</sub> | T/o<br><sub>63s</sub> | N<br><sub>29s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>40s</sub> | N<br><sub>50s</sub> | T/o<br><sub>62s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>189s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>149s</sub> | T/o<br><sub>164s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>341s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>40s</sub> | N<br><sub>18s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.5s</sub> | – | N<br><sub>8.0s</sub> | N<br><sub>7.6s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>8.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.4s</sub> | N<br><sub>13s</sub> | – | N<br><sub>7.6s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.4s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>17s</sub> | N<br><sub>20s</sub> | – | N<br><sub>16s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>19s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>40s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>8.0s</sub> | N<br><sub>6.7s</sub> | N<br><sub>7.3s</sub> | N<br><sub>19s</sub> | – | N<br><sub>6.4s</sub> | N<br><sub>5.9s</sub> | N<br><sub>9.7s</sub> | N<br><sub>9.1s</sub> | N<br><sub>8.1s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.5s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.2s</sub> | N<br><sub>8.0s</sub> | – | N<br><sub>7.0s</sub> | N<br><sub>9.9s</sub> | N<br><sub>8.8s</sub> | N<br><sub>7.2s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>16s</sub> | N<br><sub>15s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | – | N<br><sub>17s</sub> | N<br><sub>19s</sub> | N<br><sub>16s</sub> | N<br><sub>17s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### none (baseline) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.4s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>15s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>29s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.4s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>8.6s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>5.8s</sub> | N<br><sub>5.1s</sub> | N<br><sub>4.5s</sub> | N<br><sub>5.1s</sub> | – | N<br><sub>4.5s</sub> | N<br><sub>4.5s</sub> | N<br><sub>5.2s</sub> | N<br><sub>5.2s</sub> | N<br><sub>4.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.1s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.1s</sub> | – | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.5s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.5s</sub> | N<br><sub>8.6s</sub> | – | N<br><sub>8.6s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.5s</sub> | N<br><sub>8.6s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.3s</sub> | T/o<br><sub>61s</sub> | N<br><sub>3.7s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>9.8s</sub> | T/o<br><sub>63s</sub> | N<br><sub>14s</sub> | – | N<br><sub>8.7s</sub> | T/o<br><sub>63s</sub> | N<br><sub>4.5s</sub> | N<br><sub>9.7s</sub> | N<br><sub>4.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.8s</sub> | N<br><sub>9.8s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>7.6s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.3s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>15s</sub> | Y<br><sub>9.0s</sub> | – | Y<br><sub>20s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>7.1s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>8.2s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>5.0s</sub> | N<br><sub>7.1s</sub> | N<br><sub>5.0s</sub> | N<br><sub>10s</sub> | – | N<br><sub>5.1s</sub> | N<br><sub>4.5s</sub> | N<br><sub>4.8s</sub> | N<br><sub>4.1s</sub> | N<br><sub>4.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>4.8s</sub> | N<br><sub>5.0s</sub> | – | N<br><sub>5.0s</sub> | N<br><sub>5.0s</sub> | N<br><sub>6.2s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.1s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.1s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>8.4s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.0s</sub> | N<br><sub>11s</sub> | – | N<br><sub>8.7s</sub> | N<br><sub>9.8s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.8s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.6s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.6s</sub> | N<br><sub>15s</sub> | – | N<br><sub>7.3s</sub> | N<br><sub>9.5s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.8s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>2.5s</sub> | Y<br><sub>2.5s</sub> | – | Y<br><sub>2.4s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>2.5s</sub> | Y<br><sub>2.4s</sub> | Y<br><sub>6.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | N<br><sub>53s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>33s</sub> | N<br><sub>7.7s</sub> | N<br><sub>14s</sub> | T/o<br><sub>143s</sub> | – | N<br><sub>9.3s</sub> | N<br><sub>18s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>75s</sub> | N<br><sub>16s</sub> | T/o<br><sub>64s</sub> | N<br><sub>228s</sub> | – | N<br><sub>121s</sub> | N<br><sub>17s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>77s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.1s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>17s</sub> | Y<br><sub>10s</sub> | – | Y<br><sub>22s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>13s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>9.6s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>5.7s</sub> | N<br><sub>5.1s</sub> | N<br><sub>5.5s</sub> | N<br><sub>7.7s</sub> | – | N<br><sub>6.7s</sub> | N<br><sub>8.1s</sub> | N<br><sub>10s</sub> | N<br><sub>4.7s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.0s</sub> | N<br><sub>15s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.1s</sub> | – | N<br><sub>8.9s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>14s</sub> | N<br><sub>10s</sub> | N<br><sub>75s</sub> | T/o<br><sub>865s</sub> | – | N<br><sub>12s</sub> | N<br><sub>9.6s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>7.6s</sub> | N<br><sub>7.1s</sub> | N<br><sub>8.4s</sub> | N<br><sub>7.4s</sub> | – | N<br><sub>8.1s</sub> | N<br><sub>7.1s</sub> | N<br><sub>10s</sub> | N<br><sub>8.8s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>10s</sub> | N<br><sub>8.6s</sub> | N<br><sub>10s</sub> | N<br><sub>14s</sub> | – | N<br><sub>7.6s</sub> | N<br><sub>9.9s</sub> | N<br><sub>10s</sub> | N<br><sub>7.9s</sub> | N<br><sub>9.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | N<br><sub>19s</sub> | N<br><sub>16s</sub> | N<br><sub>22s</sub> | – | N<br><sub>17s</sub> | N<br><sub>18s</sub> | N<br><sub>21s</sub> | N<br><sub>19s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>47s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>7.7s</sub> | N<br><sub>6.3s</sub> | N<br><sub>7.0s</sub> | N<br><sub>7.2s</sub> | – | N<br><sub>5.5s</sub> | N<br><sub>6.9s</sub> | N<br><sub>9.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.4s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.8s</sub> | – | N<br><sub>6.8s</sub> | N<br><sub>9.8s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.4s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>18s</sub> | N<br><sub>14s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | – | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>13s</sub> | N<br><sub>15s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |

##### none (baseline) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>4.3s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>15s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>28s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.0s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>8.4s</sub> | 8/9 (89%) |
| `0.05` | N<br><sub>5.6s</sub> | N<br><sub>4.9s</sub> | N<br><sub>4.3s</sub> | N<br><sub>4.9s</sub> | – | N<br><sub>4.3s</sub> | N<br><sub>4.3s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.0s</sub> | N<br><sub>4.3s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.8s</sub> | – | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>8.2s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

### Class 5

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=10/36 (27.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | – | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | Y<br><sub>8.8s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 1/9 (11%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | N<br><sub>8.5s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>22s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | N<br><sub>21s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | N<br><sub>32s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | N<br><sub>24s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | N<br><sub>31s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | – | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>13s</sub> | Y<br><sub>38s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>10s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.6s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | – | Y<br><sub>3.5s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.5s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>39s</sub> | N<br><sub>43s</sub> | N<br><sub>39s</sub> | N<br><sub>36s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>35s</sub> | N<br><sub>41s</sub> | N<br><sub>40s</sub> | N<br><sub>40s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | N<br><sub>14s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.5s</sub> | N<br><sub>12s</sub> | N<br><sub>8.2s</sub> | N<br><sub>6.2s</sub> | N<br><sub>24s</sub> | – | N<br><sub>12s</sub> | N<br><sub>9.9s</sub> | N<br><sub>8.7s</sub> | N<br><sub>7.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.2s</sub> | – | N<br><sub>5.6s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>5.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.8s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.7s</sub> | – | N<br><sub>8.6s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.9s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>5.9s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.7s</sub> | N<br><sub>6.6s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>68s</sub> | N<br><sub>7.0s</sub> | T/o<br><sub>62s</sub> | N<br><sub>18s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | N<br><sub>8.2s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | N<br><sub>8.8s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>56s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>19s</sub> | N<br><sub>38s</sub> | N<br><sub>21s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | T/o<br><sub>62s</sub> | N<br><sub>32s</sub> | N<br><sub>17s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>20s</sub> | T/o<br><sub>61s</sub> | N<br><sub>24s</sub> | N<br><sub>52s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=27/36 (75.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>13s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.2s</sub> | N<br><sub>11s</sub> | N<br><sub>7.6s</sub> | N<br><sub>5.9s</sub> | N<br><sub>23s</sub> | – | N<br><sub>8.1s</sub> | N<br><sub>9.2s</sub> | N<br><sub>8.4s</sub> | N<br><sub>7.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.7s</sub> | N<br><sub>5.6s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>5.3s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.6s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.6s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.5s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.5s</sub> | – | N<br><sub>8.4s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>19s</sub> | N<br><sub>25s</sub> | N<br><sub>24s</sub> | N<br><sub>6.4s</sub> | N<br><sub>27s</sub> | – | N<br><sub>16s</sub> | N<br><sub>24s</sub> | N<br><sub>18s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.8s</sub> | N<br><sub>8.7s</sub> | N<br><sub>7.3s</sub> | N<br><sub>5.4s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>7.3s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>8.5s</sub> | N<br><sub>5.3s</sub> | N<br><sub>5.0s</sub> | N<br><sub>14s</sub> | – | N<br><sub>9.9s</sub> | N<br><sub>5.4s</sub> | N<br><sub>12s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>8.6s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>14s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>6.7s</sub> | N<br><sub>13s</sub> | – | N<br><sub>15s</sub> | N<br><sub>14s</sub> | N<br><sub>30s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.5s</sub> | N<br><sub>6.3s</sub> | N<br><sub>4.6s</sub> | N<br><sub>4.6s</sub> | N<br><sub>4.8s</sub> | – | N<br><sub>6.9s</sub> | N<br><sub>4.8s</sub> | N<br><sub>4.7s</sub> | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.3s</sub> | – | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.4s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.9s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>7.5s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>17s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>5.7s</sub> | N<br><sub>14s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>25s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>27s</sub> | N<br><sub>6.4s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.8s</sub> | N<br><sub>8.0s</sub> | – | N<br><sub>15s</sub> | N<br><sub>7.0s</sub> | N<br><sub>17s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>23s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>227s</sub> | T/o<br><sub>440s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>167s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>117s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.3s</sub> | N<br><sub>11s</sub> | N<br><sub>7.6s</sub> | N<br><sub>6.1s</sub> | N<br><sub>23s</sub> | – | N<br><sub>8.2s</sub> | N<br><sub>9.4s</sub> | N<br><sub>8.4s</sub> | N<br><sub>7.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>5.2s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.7s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.0s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.9s</sub> | – | N<br><sub>8.8s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.7s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=10/36 (27.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | – | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | – | Y<br><sub>8.4s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 1/9 (11%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | N<br><sub>7.3s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | N<br><sub>10s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>18s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | N<br><sub>22s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | N<br><sub>46s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | N<br><sub>28s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>36s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | – | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | Y<br><sub>0.4s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>12s</sub> | Y<br><sub>42s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>9.9s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>39s</sub> | N<br><sub>42s</sub> | N<br><sub>39s</sub> | N<br><sub>36s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>36s</sub> | N<br><sub>42s</sub> | N<br><sub>40s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>15s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>8.4s</sub> | N<br><sub>12s</sub> | N<br><sub>15s</sub> | N<br><sub>6.9s</sub> | N<br><sub>32s</sub> | – | N<br><sub>9.8s</sub> | N<br><sub>12s</sub> | T/o<br><sub>66s</sub> | N<br><sub>8.6s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.0s</sub> | N<br><sub>7.0s</sub> | N<br><sub>7.2s</sub> | N<br><sub>6.8s</sub> | N<br><sub>7.1s</sub> | – | N<br><sub>6.5s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.2s</sub> | N<br><sub>7.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>11s</sub> | N<br><sub>7.1s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>7.6s</sub> | T/o<br><sub>68s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | N<br><sub>9.0s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>9.7s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | N<br><sub>35s</sub> | – | T/o<br><sub>64s</sub> | N<br><sub>38s</sub> | N<br><sub>20s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>20s</sub> | T/o<br><sub>62s</sub> | N<br><sub>36s</sub> | N<br><sub>19s</sub> | N<br><sub>49s</sub> | – | N<br><sub>22s</sub> | T/o<br><sub>61s</sub> | N<br><sub>26s</sub> | N<br><sub>57s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=27/36 (75.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.5s</sub> | N<br><sub>11s</sub> | N<br><sub>8.0s</sub> | N<br><sub>6.3s</sub> | N<br><sub>24s</sub> | – | N<br><sub>8.3s</sub> | N<br><sub>9.4s</sub> | N<br><sub>8.6s</sub> | N<br><sub>7.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.2s</sub> | – | N<br><sub>5.6s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.0s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.9s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.1s</sub> | – | N<br><sub>8.9s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.2s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>11s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>11s</sub> | N<br><sub>27s</sub> | N<br><sub>26s</sub> | N<br><sub>6.3s</sub> | N<br><sub>29s</sub> | – | N<br><sub>18s</sub> | N<br><sub>26s</sub> | N<br><sub>21s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>8.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>11s</sub> | – | N<br><sub>8.0s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.7s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.5s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.3s</sub> | N<br><sub>15s</sub> | – | N<br><sub>11s</sub> | N<br><sub>5.9s</sub> | N<br><sub>13s</sub> | N<br><sub>6.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>9.1s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>16s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>7.3s</sub> | N<br><sub>17s</sub> | – | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>33s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.1s</sub> | N<br><sub>7.0s</sub> | N<br><sub>5.2s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.3s</sub> | – | N<br><sub>7.7s</sub> | N<br><sub>5.3s</sub> | N<br><sub>5.1s</sub> | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.9s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.3s</sub> | N<br><sub>8.9s</sub> | – | N<br><sub>9.1s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.9s</sub> | N<br><sub>9.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.5s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>15s</sub> | N<br><sub>6.8s</sub> | N<br><sub>13s</sub> | – | N<br><sub>10s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>22s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.2s</sub> | N<br><sub>12s</sub> | N<br><sub>15s</sub> | N<br><sub>6.0s</sub> | N<br><sub>23s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>7.7s</sub> | N<br><sub>18s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>28s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.1s</sub> | N<br><sub>8.3s</sub> | – | N<br><sub>16s</sub> | N<br><sub>6.4s</sub> | N<br><sub>11s</sub> | N<br><sub>8.0s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>23s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>198s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>423s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>90s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>218s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.6s</sub> | N<br><sub>12s</sub> | N<br><sub>8.2s</sub> | N<br><sub>6.5s</sub> | N<br><sub>25s</sub> | – | N<br><sub>8.8s</sub> | N<br><sub>9.9s</sub> | N<br><sub>8.6s</sub> | N<br><sub>7.6s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.1s</sub> | – | N<br><sub>5.4s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.0s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.1s</sub> | – | N<br><sub>9.2s</sub> | N<br><sub>9.2s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.0s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>11s</sub> | N<br><sub>7.0s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>7.3s</sub> | T/o<br><sub>66s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | N<br><sub>8.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>7.8s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>58s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>11s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>36s</sub> | N<br><sub>18s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | T/o<br><sub>61s</sub> | N<br><sub>33s</sub> | N<br><sub>18s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>22s</sub> | T/o<br><sub>65s</sub> | N<br><sub>26s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=27/36 (75.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.95) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.6s</sub> | Y<br><sub>20s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>51s</sub> | Y<br><sub>2.6s</sub> | – | Y<br><sub>2.6s</sub> | Y<br><sub>27s</sub> | Y<br><sub>20s</sub> | Y<br><sub>20s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | N<br><sub>16s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>75s</sub> | T/o<br><sub>76s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>122s</sub> | N<br><sub>10s</sub> | T/o<br><sub>80s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.95) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | N<br><sub>13s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | N<br><sub>9.3s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | N<br><sub>50s</sub> | N<br><sub>10s</sub> | N<br><sub>36s</sub> | – | T/o<br><sub>65s</sub> | N<br><sub>56s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>33s</sub> | N<br><sub>16s</sub> | N<br><sub>20s</sub> | – | N<br><sub>58s</sub> | T/o<br><sub>63s</sub> | N<br><sub>25s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>15s</sub> | Y<br><sub>16s</sub> | Y<br><sub>32s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>16s</sub> | Y<br><sub>16s</sub> | Y<br><sub>15s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>59s</sub> | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | N<br><sub>45s</sub> | N<br><sub>47s</sub> | – | N<br><sub>31s</sub> | N<br><sub>25s</sub> | N<br><sub>15s</sub> | N<br><sub>21s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>40s</sub> | N<br><sub>33s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>35s</sub> | N<br><sub>16s</sub> | N<br><sub>56s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.95) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | N<br><sub>15s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>60s</sub> | T/o<br><sub>80s</sub> | N<br><sub>13s</sub> | N<br><sub>25s</sub> | T/o<br><sub>69s</sub> | – | N<br><sub>16s</sub> | N<br><sub>9.8s</sub> | N<br><sub>9.5s</sub> | N<br><sub>18s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | N<br><sub>15s</sub> | N<br><sub>12s</sub> | N<br><sub>14s</sub> | N<br><sub>18s</sub> | – | N<br><sub>23s</sub> | N<br><sub>14s</sub> | N<br><sub>19s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.5s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>6.2s</sub> | N<br><sub>24s</sub> | – | N<br><sub>8.4s</sub> | N<br><sub>9.8s</sub> | N<br><sub>8.5s</sub> | N<br><sub>7.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.8s</sub> | N<br><sub>6.1s</sub> | – | N<br><sub>5.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>5.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.8s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.2s</sub> | – | N<br><sub>8.9s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.9s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>21s</sub> | N<br><sub>28s</sub> | N<br><sub>26s</sub> | N<br><sub>6.4s</sub> | N<br><sub>30s</sub> | – | N<br><sub>18s</sub> | N<br><sub>26s</sub> | N<br><sub>20s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>7.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>11s</sub> | – | N<br><sub>8.0s</sub> | N<br><sub>7.9s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>15s</sub> | N<br><sub>6.6s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.4s</sub> | N<br><sub>15s</sub> | – | N<br><sub>11s</sub> | N<br><sub>5.8s</sub> | N<br><sub>13s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>9.1s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>17s</sub> | N<br><sub>10s</sub> | N<br><sub>9.8s</sub> | N<br><sub>7.1s</sub> | N<br><sub>15s</sub> | – | N<br><sub>16s</sub> | N<br><sub>15s</sub> | N<br><sub>31s</sub> | N<br><sub>8.0s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.9s</sub> | N<br><sub>6.9s</sub> | N<br><sub>4.9s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.1s</sub> | – | N<br><sub>7.4s</sub> | N<br><sub>5.2s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.3s</sub> | N<br><sub>8.5s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.3s</sub> | – | N<br><sub>8.1s</sub> | N<br><sub>8.0s</sub> | N<br><sub>7.7s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.3s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>15s</sub> | N<br><sub>7.8s</sub> | N<br><sub>13s</sub> | – | N<br><sub>9.8s</sub> | N<br><sub>13s</sub> | N<br><sub>18s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>5.8s</sub> | N<br><sub>22s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>8.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | N<br><sub>7.1s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.1s</sub> | N<br><sub>8.3s</sub> | – | N<br><sub>16s</sub> | N<br><sub>6.4s</sub> | N<br><sub>18s</sub> | N<br><sub>8.2s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>17s</sub> | Y<br><sub>23s</sub> | Y<br><sub>60s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>19s</sub> | – | Y<br><sub>2.7s</sub> | Y<br><sub>34s</sub> | Y<br><sub>21s</sub> | Y<br><sub>23s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>99s</sub> | N<br><sub>9.6s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>117s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | N<br><sub>13s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>10s</sub> | N<br><sub>20s</sub> | N<br><sub>25s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>14s</sub> | T/o<br><sub>62s</sub> | N<br><sub>35s</sub> | N<br><sub>23s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.2s</sub> | N<br><sub>9.0s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.5s</sub> | T/o<br><sub>466s</sub> | – | N<br><sub>6.9s</sub> | N<br><sub>107s</sub> | N<br><sub>6.7s</sub> | N<br><sub>7.3s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>457s</sub> | N<br><sub>11s</sub> | N<br><sub>9.3s</sub> | T/o<br><sub>380s</sub> | N<br><sub>8.3s</sub> | – | N<br><sub>11s</sub> | T/o<br><sub>288s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | Y<br><sub>35s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>43s</sub> | T/o<br><sub>92s</sub> | N<br><sub>14s</sub> | N<br><sub>32s</sub> | N<br><sub>23s</sub> | – | N<br><sub>28s</sub> | N<br><sub>13s</sub> | N<br><sub>9.6s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | N<br><sub>20s</sub> | N<br><sub>22s</sub> | N<br><sub>22s</sub> | N<br><sub>20s</sub> | – | N<br><sub>28s</sub> | N<br><sub>28s</sub> | N<br><sub>17s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | Y<br><sub>17s</sub> | Y<br><sub>15s</sub> | N<br><sub>16s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | Y<br><sub>16s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>6.6s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.8s</sub> | N<br><sub>7.2s</sub> | – | N<br><sub>25s</sub> | N<br><sub>8.9s</sub> | N<br><sub>6.9s</sub> | N<br><sub>7.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>18s</sub> | N<br><sub>11s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.7s</sub> | – | N<br><sub>11s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.8s</sub> | N<br><sub>10s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | N<br><sub>14s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.7s</sub> | N<br><sub>12s</sub> | N<br><sub>8.3s</sub> | N<br><sub>6.2s</sub> | N<br><sub>24s</sub> | – | N<br><sub>8.5s</sub> | N<br><sub>9.9s</sub> | N<br><sub>8.6s</sub> | N<br><sub>7.1s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.7s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>5.5s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>5.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.1s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.2s</sub> | – | N<br><sub>9.0s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.2s</sub> | 0/9 (0%) |

### Class 6

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=15/36 (41.7%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>5.0s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>5.8s</sub> | Y<br><sub>4.4s</sub> | Y<br><sub>4.1s</sub> | Y<br><sub>9.7s</sub> | – | Y<br><sub>5.6s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 6/9 (67%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | N<br><sub>9.6s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | N<br><sub>16s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>43s</sub> | – | N<br><sub>21s</sub> | N<br><sub>19s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.3s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | N<br><sub>34s</sub> | T/o<br><sub>65s</sub> | N<br><sub>34s</sub> | – | N<br><sub>62s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>7.0s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.2s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.2s</sub> | T/o<br><sub>63s</sub> | N<br><sub>7.1s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>4.0s</sub> | N<br><sub>4.8s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.1s</sub> | T/o<br><sub>73s</sub> | N<br><sub>6.2s</sub> | N<br><sub>16s</sub> | N<br><sub>7.0s</sub> | N<br><sub>29s</sub> | – | N<br><sub>17s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.4s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | – | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | N<br><sub>28s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>14s</sub> | T/o<br><sub>64s</sub> | N<br><sub>32s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | T/o<br><sub>60s</sub> | N<br><sub>22s</sub> | T/o<br><sub>62s</sub> | N<br><sub>48s</sub> | N<br><sub>37s</sub> | – | N<br><sub>49s</sub> | N<br><sub>36s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=27/36 (75.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | – | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>81s</sub> | N<br><sub>55s</sub> | N<br><sub>46s</sub> | N<br><sub>34s</sub> | N<br><sub>57s</sub> | N<br><sub>20s</sub> | – | T/o<br><sub>81s</sub> | N<br><sub>33s</sub> | N<br><sub>41s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>5.9s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>4.2s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.9s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.6s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>68s</sub> | N<br><sub>3.4s</sub> | N<br><sub>4.1s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>4.9s</sub> | T/o<br><sub>83s</sub> | N<br><sub>4.6s</sub> | N<br><sub>14s</sub> | N<br><sub>5.2s</sub> | N<br><sub>22s</sub> | – | N<br><sub>11s</sub> | N<br><sub>4.8s</sub> | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.0s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.4s</sub> | – | N<br><sub>7.6s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.0s</sub> | N<br><sub>11s</sub> | N<br><sub>7.1s</sub> | N<br><sub>6.1s</sub> | N<br><sub>18s</sub> | N<br><sub>6.1s</sub> | – | N<br><sub>6.2s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.7s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | N<br><sub>9.6s</sub> | – | N<br><sub>12s</sub> | N<br><sub>25s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>8.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>8.5s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.3s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.7s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.7s</sub> | N<br><sub>34s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.6s</sub> | N<br><sub>34s</sub> | – | N<br><sub>7.7s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>14s</sub> | – | N<br><sub>16s</sub> | N<br><sub>15s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>88s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.6s</sub> | T/o<br><sub>61s</sub> | N<br><sub>32s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>54s</sub> | – | N<br><sub>19s</sub> | N<br><sub>59s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.1s</sub> | N<br><sub>10s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>7.0s</sub> | – | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.1s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | – | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | N<br><sub>16s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | N<br><sub>21s</sub> | – | N<br><sub>37s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>79s</sub> | N<br><sub>46s</sub> | N<br><sub>22s</sub> | T/o<br><sub>142s</sub> | N<br><sub>24s</sub> | T/o<br><sub>68s</sub> | – | N<br><sub>19s</sub> | N<br><sub>27s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>7.4s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.2s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.5s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.1s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>4.4s</sub> | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.4s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.6s</sub> | N<br><sub>37s</sub> | N<br><sub>7.2s</sub> | N<br><sub>33s</sub> | – | N<br><sub>16s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=14/36 (38.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>4.9s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>7.2s</sub> | Y<br><sub>5.3s</sub> | Y<br><sub>5.0s</sub> | T/o<br><sub>74s</sub> | – | Y<br><sub>7.5s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 5/9 (56%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>91s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | N<br><sub>13s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | N<br><sub>24s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | N<br><sub>52s</sub> | – | N<br><sub>25s</sub> | N<br><sub>22s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.5s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | – | Y<br><sub>3.6s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>30s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | N<br><sub>39s</sub> | T/o<br><sub>65s</sub> | N<br><sub>39s</sub> | – | T/o<br><sub>68s</sub> | N<br><sub>20s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>7.0s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.3s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.2s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>65s</sub> | N<br><sub>4.2s</sub> | N<br><sub>5.1s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.3s</sub> | T/o<br><sub>75s</sub> | N<br><sub>6.3s</sub> | N<br><sub>21s</sub> | N<br><sub>7.0s</sub> | N<br><sub>33s</sub> | – | N<br><sub>16s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>26s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>14s</sub> | T/o<br><sub>60s</sub> | N<br><sub>33s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>20s</sub> | T/o<br><sub>62s</sub> | N<br><sub>25s</sub> | T/o<br><sub>62s</sub> | N<br><sub>51s</sub> | N<br><sub>40s</sub> | – | N<br><sub>51s</sub> | N<br><sub>38s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=27/36 (75.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | N<br><sub>45s</sub> | T/o<br><sub>63s</sub> | N<br><sub>47s</sub> | T/o<br><sub>63s</sub> | N<br><sub>26s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>46s</sub> | N<br><sub>52s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>5.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>4.0s</sub> | T/o<br><sub>60s</sub> | N<br><sub>4.6s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.4s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>3.3s</sub> | N<br><sub>3.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>4.5s</sub> | N<br><sub>23s</sub> | N<br><sub>4.5s</sub> | N<br><sub>13s</sub> | N<br><sub>4.7s</sub> | N<br><sub>21s</sub> | – | N<br><sub>10s</sub> | N<br><sub>4.5s</sub> | N<br><sub>4.7s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.6s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.5s</sub> | – | N<br><sub>7.2s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.5s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.0s</sub> | N<br><sub>10s</sub> | N<br><sub>9.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>12s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>6.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.7s</sub> | N<br><sub>11s</sub> | N<br><sub>8.8s</sub> | N<br><sub>12s</sub> | N<br><sub>9.6s</sub> | N<br><sub>8.4s</sub> | – | N<br><sub>9.9s</sub> | N<br><sub>21s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>7.0s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>30s</sub> | T/o<br><sub>63s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>5.5s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.3s</sub> | N<br><sub>28s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.2s</sub> | N<br><sub>5.8s</sub> | N<br><sub>29s</sub> | – | N<br><sub>5.9s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | – | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>76s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.6s</sub> | T/o<br><sub>65s</sub> | N<br><sub>33s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>16s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>59s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.7s</sub> | N<br><sub>9.8s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>18s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | – | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>79s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | N<br><sub>17s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | N<br><sub>21s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>41s</sub> | N<br><sub>47s</sub> | N<br><sub>24s</sub> | T/o<br><sub>91s</sub> | N<br><sub>24s</sub> | T/o<br><sub>88s</sub> | – | T/o<br><sub>101s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>165s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>6.9s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>5.0s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.0s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>4.5s</sub> | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.7s</sub> | T/o<br><sub>76s</sub> | N<br><sub>6.6s</sub> | N<br><sub>21s</sub> | N<br><sub>7.2s</sub> | N<br><sub>34s</sub> | – | N<br><sub>17s</sub> | N<br><sub>6.4s</sub> | N<br><sub>6.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

### Class 7

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>27s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>81s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>14s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>40s</sub> | T/o<br><sub>67s</sub> | N<br><sub>19s</sub> | N<br><sub>11s</sub> | T/o<br><sub>61s</sub> | N<br><sub>38s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>71s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>35s</sub> | N<br><sub>21s</sub> | N<br><sub>32s</sub> | N<br><sub>34s</sub> | N<br><sub>38s</sub> | N<br><sub>21s</sub> | N<br><sub>59s</sub> | – | N<br><sub>29s</sub> | N<br><sub>31s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=20/36 (55.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>35s</sub> | – | Y<br><sub>43s</sub> | T/o<br><sub>62s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.9) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.5s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | – | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | N<br><sub>33s</sub> | T/o<br><sub>63s</sub> | N<br><sub>48s</sub> | N<br><sub>38s</sub> | N<br><sub>32s</sub> | T/o<br><sub>66s</sub> | – | N<br><sub>35s</sub> | N<br><sub>35s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>11s</sub> | N<br><sub>23s</sub> | N<br><sub>8.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>21s</sub> | T/o<br><sub>62s</sub> | N<br><sub>9.1s</sub> | – | N<br><sub>8.4s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.2s</sub> | N<br><sub>9.3s</sub> | N<br><sub>8.3s</sub> | N<br><sub>9.7s</sub> | N<br><sub>8.1s</sub> | N<br><sub>9.8s</sub> | N<br><sub>9.3s</sub> | – | N<br><sub>8.9s</sub> | N<br><sub>9.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | – | N<br><sub>11s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | N<br><sub>6.0s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | N<br><sub>7.2s</sub> | N<br><sub>11s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>9.0s</sub> | N<br><sub>7.1s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | N<br><sub>35s</sub> | – | N<br><sub>8.8s</sub> | N<br><sub>7.1s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.0s</sub> | N<br><sub>14s</sub> | N<br><sub>7.7s</sub> | N<br><sub>15s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>8.0s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>15s</sub> | N<br><sub>13s</sub> | – | N<br><sub>13s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>7.0s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | N<br><sub>8.9s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>7.6s</sub> | N<br><sub>18s</sub> | N<br><sub>6.5s</sub> | N<br><sub>4.9s</sub> | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>6.1s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.0s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.3s</sub> | N<br><sub>7.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.2s</sub> | – | N<br><sub>6.9s</sub> | N<br><sub>6.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.8s</sub> | N<br><sub>9.3s</sub> | N<br><sub>8.9s</sub> | N<br><sub>8.4s</sub> | N<br><sub>9.1s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.8s</sub> | – | N<br><sub>9.2s</sub> | N<br><sub>8.9s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.2s</sub> | N<br><sub>17s</sub> | N<br><sub>4.1s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>4.2s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>5.8s</sub> | N<br><sub>4.9s</sub> | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>31s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | N<br><sub>7.2s</sub> | N<br><sub>4.5s</sub> | N<br><sub>6.2s</sub> | T/o<br><sub>62s</sub> | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>6.2s</sub> | N<br><sub>3.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.7s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.6s</sub> | N<br><sub>8.9s</sub> | N<br><sub>4.3s</sub> | N<br><sub>7.0s</sub> | N<br><sub>4.5s</sub> | – | N<br><sub>5.5s</sub> | N<br><sub>4.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.8s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.7s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>6.7s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>4.0s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | N<br><sub>13s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.6s</sub> | N<br><sub>4.8s</sub> | N<br><sub>11s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>4.8s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>76s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>6.8s</sub> | N<br><sub>13s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.1s</sub> | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.6s</sub> | – | N<br><sub>5.0s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>4.5s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.5s</sub> | N<br><sub>5.3s</sub> | – | N<br><sub>5.2s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>5.9s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | N<br><sub>28s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>82s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>39s</sub> | T/o<br><sub>68s</sub> | N<br><sub>19s</sub> | N<br><sub>11s</sub> | T/o<br><sub>66s</sub> | N<br><sub>39s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>42s</sub> | N<br><sub>26s</sub> | N<br><sub>49s</sub> | N<br><sub>52s</sub> | N<br><sub>39s</sub> | N<br><sub>23s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>31s</sub> | N<br><sub>34s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=20/36 (55.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>37s</sub> | – | Y<br><sub>35s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=18/36 (50.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.4s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | – | Y<br><sub>2.3s</sub> | Y<br><sub>2.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.7s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.8s</sub> | – | Y<br><sub>3.7s</sub> | Y<br><sub>3.8s</sub> | 9/9 (100%) |
| `0.10` | T/o<br><sub>75s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | N<br><sub>35s</sub> | T/o<br><sub>64s</sub> | N<br><sub>49s</sub> | N<br><sub>37s</sub> | N<br><sub>33s</sub> | T/o<br><sub>68s</sub> | – | N<br><sub>36s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>12s</sub> | N<br><sub>24s</sub> | N<br><sub>8.2s</sub> | N<br><sub>6.1s</sub> | N<br><sub>21s</sub> | T/o<br><sub>63s</sub> | N<br><sub>9.2s</sub> | – | N<br><sub>7.8s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.1s</sub> | N<br><sub>9.6s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.8s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.9s</sub> | N<br><sub>9.5s</sub> | – | N<br><sub>9.3s</sub> | N<br><sub>9.4s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | – | N<br><sub>11s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.0s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | N<br><sub>8.7s</sub> | N<br><sub>12s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>70s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | N<br><sub>9.4s</sub> | N<br><sub>6.8s</sub> | N<br><sub>7.3s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | N<br><sub>35s</sub> | – | N<br><sub>8.8s</sub> | N<br><sub>8.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.1s</sub> | N<br><sub>14s</sub> | N<br><sub>8.2s</sub> | N<br><sub>15s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.1s</sub> | N<br><sub>8.6s</sub> | – | N<br><sub>7.7s</sub> | N<br><sub>7.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | N<br><sub>13s</sub> | – | N<br><sub>13s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | N<br><sub>6.8s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | N<br><sub>8.8s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>12s</sub> | N<br><sub>25s</sub> | N<br><sub>9.0s</sub> | N<br><sub>7.0s</sub> | N<br><sub>22s</sub> | T/o<br><sub>63s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>6.8s</sub> | N<br><sub>31s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>8.3s</sub> | N<br><sub>9.8s</sub> | N<br><sub>9.1s</sub> | N<br><sub>10s</sub> | N<br><sub>8.2s</sub> | N<br><sub>10s</sub> | N<br><sub>9.6s</sub> | – | N<br><sub>9.1s</sub> | N<br><sub>9.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | N<br><sub>12s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.2s</sub> | N<br><sub>8.6s</sub> | N<br><sub>4.1s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>4.1s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>5.8s</sub> | N<br><sub>4.9s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>31s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | N<br><sub>15s</sub> | N<br><sub>3.6s</sub> | N<br><sub>6.3s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>6.2s</sub> | N<br><sub>3.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>4.6s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.6s</sub> | N<br><sub>9.0s</sub> | N<br><sub>4.4s</sub> | N<br><sub>7.1s</sub> | N<br><sub>5.7s</sub> | – | N<br><sub>5.5s</sub> | N<br><sub>4.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.8s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.8s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>6.7s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>19s</sub> | N<br><sub>8.8s</sub> | N<br><sub>11s</sub> | N<br><sub>4.0s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | N<br><sub>13s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.6s</sub> | N<br><sub>4.8s</sub> | N<br><sub>15s</sub> | N<br><sub>24s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>4.8s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>76s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>6.9s</sub> | N<br><sub>14s</sub> | N<br><sub>5.4s</sub> | N<br><sub>4.1s</sub> | N<br><sub>12s</sub> | T/o<br><sub>62s</sub> | N<br><sub>5.7s</sub> | – | N<br><sub>5.1s</sub> | N<br><sub>20s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>4.6s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.7s</sub> | N<br><sub>5.4s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.5s</sub> | N<br><sub>5.4s</sub> | – | N<br><sub>5.2s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.0s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.3s</sub> | N<br><sub>8.7s</sub> | N<br><sub>4.1s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>4.2s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | N<br><sub>5.8s</sub> | N<br><sub>4.9s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>31s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | N<br><sub>6.3s</sub> | N<br><sub>3.6s</sub> | N<br><sub>6.3s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>6.2s</sub> | N<br><sub>3.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.7s</sub> | N<br><sub>5.0s</sub> | N<br><sub>6.5s</sub> | N<br><sub>9.0s</sub> | N<br><sub>4.4s</sub> | N<br><sub>7.1s</sub> | N<br><sub>5.7s</sub> | – | N<br><sub>5.5s</sub> | N<br><sub>4.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.8s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.8s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>6.7s</sub> | N<br><sub>6.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | N<br><sub>18s</sub> | N<br><sub>8.7s</sub> | N<br><sub>11s</sub> | N<br><sub>4.0s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | N<br><sub>13s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.0s</sub> | N<br><sub>4.8s</sub> | N<br><sub>15s</sub> | N<br><sub>24s</sub> | – | T/o<br><sub>60s</sub> | N<br><sub>4.8s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | N<br><sub>42s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | N<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>6.2s</sub> | N<br><sub>6.2s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.3s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.6s</sub> | N<br><sub>7.1s</sub> | – | N<br><sub>5.7s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>35s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | N<br><sub>4.6s</sub> | N<br><sub>11s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.6s</sub> | N<br><sub>112s</sub> | N<br><sub>6.4s</sub> | N<br><sub>24s</sub> | T/o<br><sub>484s</sub> | N<br><sub>38s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>8.7s</sub> | N<br><sub>6.3s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>19s</sub> | N<br><sub>19s</sub> | N<br><sub>14s</sub> | N<br><sub>22s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | – | N<br><sub>17s</sub> | N<br><sub>9.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>27s</sub> | N<br><sub>30s</sub> | N<br><sub>17s</sub> | N<br><sub>13s</sub> | N<br><sub>9.4s</sub> | – | N<br><sub>16s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.8s</sub> | N<br><sub>49s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>5.0s</sub> | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>10s</sub> | N<br><sub>7.2s</sub> | N<br><sub>6.1s</sub> | N<br><sub>9.9s</sub> | N<br><sub>6.0s</sub> | N<br><sub>9.2s</sub> | N<br><sub>7.0s</sub> | – | N<br><sub>8.4s</sub> | N<br><sub>7.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.7s</sub> | N<br><sub>8.5s</sub> | N<br><sub>6.4s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>9.6s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>6.2s</sub> | N<br><sub>6.8s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>6.7s</sub> | N<br><sub>13s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.1s</sub> | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | N<br><sub>5.6s</sub> | – | N<br><sub>5.0s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>4.5s</sub> | N<br><sub>5.3s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.4s</sub> | N<br><sub>4.6s</sub> | N<br><sub>5.5s</sub> | N<br><sub>5.4s</sub> | – | N<br><sub>5.2s</sub> | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>5.9s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>5.9s</sub> | N<br><sub>5.9s</sub> | 0/9 (0%) |

### Class 8

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=32/36 (88.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.6s</sub> | Y<br><sub>5.7s</sub> | Y<br><sub>41s</sub> | Y<br><sub>5.0s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>36s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>6.0s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | T/o<br><sub>62s</sub> | Y<br><sub>50s</sub> | Y<br><sub>46s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>59s</sub> | Y<br><sub>45s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | Y<br><sub>38s</sub> | 5/9 (56%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=13/36 (36.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.6s</sub> | – | Y<br><sub>2.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>13s</sub> | T/o<br><sub>69s</sub> | Y<br><sub>12s</sub> | Y<br><sub>9.4s</sub> | – | Y<br><sub>8.0s</sub> | 4/9 (44%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | N<br><sub>42s</sub> | T/o<br><sub>81s</sub> | N<br><sub>51s</sub> | T/o<br><sub>65s</sub> | N<br><sub>55s</sub> | – | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>5.9s</sub> | N<br><sub>9.4s</sub> | N<br><sub>6.6s</sub> | N<br><sub>6.4s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.6s</sub> | N<br><sub>14s</sub> | N<br><sub>7.4s</sub> | – | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.1s</sub> | N<br><sub>10s</sub> | N<br><sub>6.3s</sub> | N<br><sub>8.1s</sub> | N<br><sub>7.8s</sub> | N<br><sub>9.2s</sub> | N<br><sub>11s</sub> | N<br><sub>7.5s</sub> | – | N<br><sub>4.7s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.6s</sub> | N<br><sub>7.8s</sub> | N<br><sub>12s</sub> | N<br><sub>18s</sub> | N<br><sub>7.2s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>34s</sub> | – | N<br><sub>6.6s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>28s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.4s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>21s</sub> | T/o<br><sub>63s</sub> | N<br><sub>40s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>22648s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.9s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.8s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>2.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>79s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>77s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>6.5s</sub> | N<br><sub>10s</sub> | N<br><sub>7.2s</sub> | N<br><sub>13s</sub> | N<br><sub>6.1s</sub> | N<br><sub>7.1s</sub> | N<br><sub>14s</sub> | N<br><sub>8.2s</sub> | – | N<br><sub>5.6s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.6s</sub> | N<br><sub>11s</sub> | N<br><sub>6.8s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.3s</sub> | N<br><sub>9.8s</sub> | N<br><sub>11s</sub> | N<br><sub>7.1s</sub> | – | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.1s</sub> | N<br><sub>7.3s</sub> | N<br><sub>12s</sub> | N<br><sub>18s</sub> | N<br><sub>8.0s</sub> | N<br><sub>16s</sub> | N<br><sub>11s</sub> | N<br><sub>34s</sub> | – | N<br><sub>7.0s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>24s</sub> | T/o<br><sub>61s</sub> | N<br><sub>23s</sub> | N<br><sub>12s</sub> | T/o<br><sub>60s</sub> | N<br><sub>12s</sub> | N<br><sub>36s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.6s</sub> | N<br><sub>15s</sub> | N<br><sub>7.9s</sub> | N<br><sub>5.7s</sub> | T/o<br><sub>61s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.0s</sub> | N<br><sub>9.4s</sub> | – | N<br><sub>5.7s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.9s</sub> | N<br><sub>7.0s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.4s</sub> | N<br><sub>5.6s</sub> | N<br><sub>5.7s</sub> | N<br><sub>5.5s</sub> | N<br><sub>5.8s</sub> | – | N<br><sub>6.4s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>14s</sub> | N<br><sub>10s</sub> | N<br><sub>8.2s</sub> | N<br><sub>18s</sub> | N<br><sub>5.3s</sub> | N<br><sub>21s</sub> | N<br><sub>18s</sub> | N<br><sub>7.2s</sub> | – | N<br><sub>4.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.5s</sub> | N<br><sub>6.5s</sub> | N<br><sub>5.4s</sub> | N<br><sub>11s</sub> | N<br><sub>6.5s</sub> | N<br><sub>4.8s</sub> | N<br><sub>6.5s</sub> | N<br><sub>6.7s</sub> | – | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.7s</sub> | N<br><sub>14s</sub> | N<br><sub>8.5s</sub> | N<br><sub>11s</sub> | N<br><sub>7.3s</sub> | N<br><sub>12s</sub> | N<br><sub>8.6s</sub> | N<br><sub>17s</sub> | – | N<br><sub>7.6s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>8.6s</sub> | N<br><sub>6.5s</sub> | N<br><sub>9.9s</sub> | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>4.7s</sub> | N<br><sub>5.0s</sub> | – | N<br><sub>4.8s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.6s</sub> | N<br><sub>30s</sub> | N<br><sub>7.4s</sub> | N<br><sub>6.1s</sub> | N<br><sub>32s</sub> | N<br><sub>6.3s</sub> | N<br><sub>9.5s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>5.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.4s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.3s</sub> | N<br><sub>5.9s</sub> | N<br><sub>7.5s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.8s</sub> | – | N<br><sub>5.9s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>9.4s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>6.1s</sub> | N<br><sub>12s</sub> | N<br><sub>5.5s</sub> | T/o<br><sub>64s</sub> | N<br><sub>9.6s</sub> | – | N<br><sub>8.7s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>15s</sub> | T/o<br><sub>76s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>35s</sub> | N<br><sub>11s</sub> | – | N<br><sub>9.4s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.8s</sub> | N<br><sub>9.8s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | – | N<br><sub>11s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>5.7s</sub> | N<br><sub>8.9s</sub> | N<br><sub>6.3s</sub> | N<br><sub>11s</sub> | N<br><sub>5.2s</sub> | N<br><sub>6.1s</sub> | N<br><sub>13s</sub> | N<br><sub>6.9s</sub> | – | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.7s</sub> | N<br><sub>9.4s</sub> | N<br><sub>5.9s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.3s</sub> | N<br><sub>8.4s</sub> | N<br><sub>9.9s</sub> | N<br><sub>6.9s</sub> | – | N<br><sub>4.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.2s</sub> | N<br><sub>6.4s</sub> | N<br><sub>10s</sub> | N<br><sub>15s</sub> | N<br><sub>7.9s</sub> | N<br><sub>13s</sub> | N<br><sub>9.3s</sub> | N<br><sub>29s</sub> | – | N<br><sub>6.0s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=33/36 (91.7%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.6s</sub> | Y<br><sub>5.7s</sub> | Y<br><sub>42s</sub> | Y<br><sub>4.9s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>15s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>5.4s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.20` | T/o<br><sub>61s</sub> | Y<br><sub>40s</sub> | Y<br><sub>46s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>58s</sub> | Y<br><sub>44s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>46s</sub> | – | Y<br><sub>38s</sub> | 6/9 (67%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | N<br><sub>21s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=13/36 (36.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.6s</sub> | Y<br><sub>2.5s</sub> | Y<br><sub>2.5s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>2.6s</sub> | Y<br><sub>2.6s</sub> | – | Y<br><sub>2.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>13s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>12s</sub> | Y<br><sub>9.2s</sub> | – | Y<br><sub>8.0s</sub> | 4/9 (44%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | N<br><sub>43s</sub> | T/o<br><sub>87s</sub> | N<br><sub>54s</sub> | T/o<br><sub>61s</sub> | N<br><sub>53s</sub> | – | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>5.6s</sub> | N<br><sub>9.1s</sub> | N<br><sub>6.5s</sub> | N<br><sub>12s</sub> | N<br><sub>5.5s</sub> | N<br><sub>6.5s</sub> | N<br><sub>14s</sub> | N<br><sub>7.3s</sub> | – | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.2s</sub> | N<br><sub>11s</sub> | N<br><sub>6.3s</sub> | N<br><sub>8.2s</sub> | N<br><sub>7.9s</sub> | N<br><sub>9.3s</sub> | N<br><sub>11s</sub> | N<br><sub>7.4s</sub> | – | N<br><sub>4.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.7s</sub> | N<br><sub>7.0s</sub> | N<br><sub>11s</sub> | N<br><sub>17s</sub> | N<br><sub>6.8s</sub> | N<br><sub>16s</sub> | N<br><sub>11s</sub> | N<br><sub>36s</sub> | – | N<br><sub>6.8s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>14s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>34s</sub> | – | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>53s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>6.0s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>22s</sub> | T/o<br><sub>62s</sub> | N<br><sub>16s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>22613s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | – | N<br><sub>21s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.8s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | Y<br><sub>2.7s</sub> | – | Y<br><sub>2.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>6.5s</sub> | N<br><sub>9.9s</sub> | N<br><sub>7.1s</sub> | N<br><sub>13s</sub> | N<br><sub>6.2s</sub> | N<br><sub>7.2s</sub> | N<br><sub>15s</sub> | N<br><sub>8.0s</sub> | – | N<br><sub>5.8s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.7s</sub> | N<br><sub>11s</sub> | N<br><sub>7.1s</sub> | N<br><sub>8.9s</sub> | N<br><sub>8.5s</sub> | N<br><sub>9.9s</sub> | N<br><sub>12s</sub> | N<br><sub>8.0s</sub> | – | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.2s</sub> | N<br><sub>7.5s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>7.4s</sub> | N<br><sub>16s</sub> | N<br><sub>11s</sub> | N<br><sub>37s</sub> | – | N<br><sub>7.1s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>25s</sub> | T/o<br><sub>61s</sub> | N<br><sub>25s</sub> | N<br><sub>13s</sub> | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | N<br><sub>36s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.0s</sub> | N<br><sub>16s</sub> | N<br><sub>8.6s</sub> | N<br><sub>6.1s</sub> | T/o<br><sub>62s</sub> | N<br><sub>8.0s</sub> | N<br><sub>7.4s</sub> | N<br><sub>10s</sub> | – | N<br><sub>5.9s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.3s</sub> | N<br><sub>7.6s</sub> | N<br><sub>6.0s</sub> | N<br><sub>7.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.2s</sub> | – | N<br><sub>6.8s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>15s</sub> | N<br><sub>8.1s</sub> | N<br><sub>7.2s</sub> | N<br><sub>12s</sub> | N<br><sub>5.3s</sub> | N<br><sub>21s</sub> | N<br><sub>19s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>4.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.6s</sub> | N<br><sub>6.5s</sub> | N<br><sub>5.3s</sub> | N<br><sub>16s</sub> | N<br><sub>6.5s</sub> | N<br><sub>4.8s</sub> | N<br><sub>6.5s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>5.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.0s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>17s</sub> | N<br><sub>7.8s</sub> | N<br><sub>13s</sub> | N<br><sub>8.4s</sub> | N<br><sub>21s</sub> | – | N<br><sub>8.1s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>6.6s</sub> | N<br><sub>6.7s</sub> | T/o<br><sub>60s</sub> | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | N<br><sub>24s</sub> | N<br><sub>5.0s</sub> | T/o<br><sub>60s</sub> | – | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.9s</sub> | N<br><sub>22s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.0s</sub> | N<br><sub>33s</sub> | N<br><sub>9.0s</sub> | N<br><sub>7.7s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>6.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.5s</sub> | N<br><sub>6.0s</sub> | N<br><sub>5.6s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.8s</sub> | N<br><sub>5.9s</sub> | N<br><sub>5.7s</sub> | – | N<br><sub>5.9s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>9.2s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>5.9s</sub> | N<br><sub>12s</sub> | N<br><sub>6.0s</sub> | T/o<br><sub>63s</sub> | N<br><sub>10s</sub> | – | N<br><sub>8.7s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>16s</sub> | N<br><sub>12s</sub> | T/o<br><sub>190s</sub> | N<br><sub>12s</sub> | T/o<br><sub>70s</sub> | N<br><sub>12s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | – | N<br><sub>9.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.0s</sub> | N<br><sub>9.9s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>22s</sub> | N<br><sub>12s</sub> | – | N<br><sub>12s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>6.2s</sub> | N<br><sub>9.4s</sub> | N<br><sub>6.6s</sub> | N<br><sub>12s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.6s</sub> | N<br><sub>14s</sub> | N<br><sub>7.5s</sub> | – | N<br><sub>5.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.5s</sub> | N<br><sub>11s</sub> | N<br><sub>6.7s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>9.7s</sub> | N<br><sub>11s</sub> | N<br><sub>7.7s</sub> | – | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.0s</sub> | N<br><sub>7.3s</sub> | N<br><sub>12s</sub> | N<br><sub>19s</sub> | N<br><sub>7.2s</sub> | N<br><sub>17s</sub> | N<br><sub>11s</sub> | N<br><sub>38s</sub> | – | N<br><sub>7.1s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>13s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>28s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>20s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | – | N<br><sub>21s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>75s</sub> | N<br><sub>22s</sub> | N<br><sub>6.9s</sub> | N<br><sub>6.2s</sub> | T/o<br><sub>82s</sub> | N<br><sub>6.2s</sub> | N<br><sub>7.7s</sub> | N<br><sub>6.2s</sub> | – | N<br><sub>18s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>286s</sub> | T/o<br><sub>65s</sub> | N<br><sub>10s</sub> | T/o<br><sub>238s</sub> | N<br><sub>11s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>612s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>18s</sub> | N<br><sub>10s</sub> | N<br><sub>9.6s</sub> | N<br><sub>10s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | T/o<br><sub>111s</sub> | – | N<br><sub>11s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>5209s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | N<br><sub>52s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>71s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>13s</sub> | N<br><sub>9.8s</sub> | N<br><sub>5.7s</sub> | N<br><sub>30s</sub> | N<br><sub>5.9s</sub> | N<br><sub>16s</sub> | T/o<br><sub>62s</sub> | N<br><sub>6.6s</sub> | – | N<br><sub>7.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>55s</sub> | N<br><sub>27s</sub> | N<br><sub>7.3s</sub> | N<br><sub>19s</sub> | N<br><sub>8.2s</sub> | N<br><sub>15s</sub> | N<br><sub>18s</sub> | N<br><sub>7.4s</sub> | – | N<br><sub>7.5s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.8s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.0s</sub> | N<br><sub>9.2s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.3s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.8s</sub> | – | N<br><sub>9.4s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | N<br><sub>8.2s</sub> | N<br><sub>7.0s</sub> | N<br><sub>5.8s</sub> | N<br><sub>7.8s</sub> | N<br><sub>6.2s</sub> | T/o<br><sub>64s</sub> | N<br><sub>7.4s</sub> | – | N<br><sub>8.9s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | N<br><sub>10s</sub> | N<br><sub>6.5s</sub> | N<br><sub>17s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.3s</sub> | N<br><sub>13s</sub> | N<br><sub>7.0s</sub> | – | N<br><sub>6.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>8.5s</sub> | N<br><sub>8.1s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.8s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.8s</sub> | – | N<br><sub>9.5s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>6.2s</sub> | N<br><sub>10.0s</sub> | N<br><sub>7.1s</sub> | N<br><sub>12s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.7s</sub> | N<br><sub>14s</sub> | N<br><sub>7.8s</sub> | – | N<br><sub>5.7s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.6s</sub> | N<br><sub>10s</sub> | N<br><sub>6.4s</sub> | N<br><sub>8.2s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.2s</sub> | N<br><sub>12s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.8s</sub> | N<br><sub>7.0s</sub> | N<br><sub>12s</sub> | N<br><sub>17s</sub> | N<br><sub>6.9s</sub> | N<br><sub>15s</sub> | N<br><sub>10s</sub> | N<br><sub>33s</sub> | – | N<br><sub>6.6s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>26s</sub> | T/o<br><sub>60s</sub> | N<br><sub>25s</sub> | N<br><sub>13s</sub> | T/o<br><sub>60s</sub> | N<br><sub>13s</sub> | N<br><sub>38s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.1s</sub> | N<br><sub>16s</sub> | N<br><sub>8.8s</sub> | N<br><sub>6.2s</sub> | T/o<br><sub>63s</sub> | N<br><sub>8.0s</sub> | N<br><sub>7.4s</sub> | N<br><sub>10s</sub> | – | N<br><sub>6.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.6s</sub> | N<br><sub>7.6s</sub> | N<br><sub>6.1s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.1s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.9s</sub> | – | N<br><sub>7.2s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>6.2s</sub> | N<br><sub>7.5s</sub> | N<br><sub>6.8s</sub> | N<br><sub>17s</sub> | N<br><sub>5.1s</sub> | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>6.9s</sub> | – | N<br><sub>4.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>7.2s</sub> | N<br><sub>6.4s</sub> | N<br><sub>5.1s</sub> | N<br><sub>11s</sub> | N<br><sub>5.4s</sub> | N<br><sub>4.7s</sub> | N<br><sub>10s</sub> | N<br><sub>6.4s</sub> | – | N<br><sub>5.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.4s</sub> | N<br><sub>14s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>7.0s</sub> | N<br><sub>11s</sub> | N<br><sub>8.2s</sub> | N<br><sub>22s</sub> | – | N<br><sub>7.4s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | N<br><sub>6.4s</sub> | N<br><sub>6.4s</sub> | N<br><sub>19s</sub> | N<br><sub>11s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.2s</sub> | – | N<br><sub>4.9s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>5.9s</sub> | N<br><sub>22s</sub> | N<br><sub>7.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.4s</sub> | N<br><sub>6.4s</sub> | N<br><sub>9.6s</sub> | N<br><sub>6.0s</sub> | – | N<br><sub>6.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>6.6s</sub> | N<br><sub>6.0s</sub> | N<br><sub>5.5s</sub> | N<br><sub>6.1s</sub> | N<br><sub>5.9s</sub> | N<br><sub>6.0s</sub> | N<br><sub>6.2s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>6.0s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>16s</sub> | N<br><sub>5.5s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.9s</sub> | N<br><sub>9.9s</sub> | N<br><sub>12s</sub> | N<br><sub>6.5s</sub> | – | N<br><sub>5.3s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.4s</sub> | T/o<br><sub>474s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>28s</sub> | N<br><sub>6.3s</sub> | – | N<br><sub>6.3s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.3s</sub> | N<br><sub>9.6s</sub> | N<br><sub>8.7s</sub> | N<br><sub>8.5s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.6s</sub> | – | N<br><sub>8.6s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>6.3s</sub> | N<br><sub>8.3s</sub> | N<br><sub>8.4s</sub> | N<br><sub>16s</sub> | N<br><sub>4.6s</sub> | N<br><sub>12s</sub> | N<br><sub>8.3s</sub> | N<br><sub>7.8s</sub> | – | N<br><sub>5.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>9.0s</sub> | N<br><sub>7.0s</sub> | N<br><sub>7.4s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.3s</sub> | N<br><sub>5.7s</sub> | N<br><sub>34s</sub> | N<br><sub>5.4s</sub> | – | N<br><sub>5.2s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.7s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.2s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.9s</sub> | N<br><sub>6.6s</sub> | N<br><sub>7.3s</sub> | T/o<br><sub>95s</sub> | – | N<br><sub>7.2s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>7.7s</sub> | N<br><sub>7.0s</sub> | N<br><sub>4.2s</sub> | N<br><sub>6.9s</sub> | N<br><sub>6.7s</sub> | N<br><sub>6.0s</sub> | T/o<br><sub>66s</sub> | N<br><sub>5.9s</sub> | – | N<br><sub>8.4s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>28s</sub> | N<br><sub>14s</sub> | N<br><sub>5.4s</sub> | N<br><sub>6.2s</sub> | N<br><sub>6.0s</sub> | N<br><sub>7.1s</sub> | N<br><sub>12s</sub> | N<br><sub>6.9s</sub> | – | N<br><sub>6.0s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>9.1s</sub> | N<br><sub>8.6s</sub> | N<br><sub>7.7s</sub> | N<br><sub>11s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.7s</sub> | N<br><sub>9.7s</sub> | N<br><sub>9.7s</sub> | – | N<br><sub>8.5s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>60s</sub> | N<br><sub>6.3s</sub> | N<br><sub>6.0s</sub> | N<br><sub>55s</sub> | N<br><sub>4.9s</sub> | N<br><sub>5.1s</sub> | N<br><sub>9.8s</sub> | N<br><sub>5.7s</sub> | – | N<br><sub>6.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>22s</sub> | N<br><sub>9.4s</sub> | N<br><sub>5.0s</sub> | N<br><sub>5.4s</sub> | N<br><sub>5.6s</sub> | N<br><sub>4.9s</sub> | N<br><sub>16s</sub> | N<br><sub>4.8s</sub> | – | N<br><sub>4.8s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.4s</sub> | N<br><sub>7.8s</sub> | N<br><sub>7.0s</sub> | N<br><sub>6.7s</sub> | N<br><sub>7.8s</sub> | N<br><sub>6.4s</sub> | N<br><sub>7.7s</sub> | N<br><sub>7.6s</sub> | – | N<br><sub>8.8s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>6.3s</sub> | N<br><sub>9.8s</sub> | N<br><sub>6.7s</sub> | N<br><sub>12s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.7s</sub> | N<br><sub>14s</sub> | N<br><sub>7.7s</sub> | – | N<br><sub>5.5s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>6.4s</sub> | N<br><sub>11s</sub> | N<br><sub>6.4s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.0s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>7.7s</sub> | – | N<br><sub>5.1s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>7.1s</sub> | N<br><sub>7.3s</sub> | N<br><sub>13s</sub> | N<br><sub>19s</sub> | N<br><sub>7.4s</sub> | N<br><sub>17s</sub> | N<br><sub>12s</sub> | N<br><sub>40s</sub> | – | N<br><sub>7.2s</sub> | 0/9 (0%) |

### Class 9

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>41s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | N<br><sub>6.4s</sub> | N<br><sub>7.2s</sub> | N<br><sub>5.2s</sub> | N<br><sub>8.1s</sub> | T/o<br><sub>61s</sub> | N<br><sub>9.2s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>18s</sub> | N<br><sub>9.0s</sub> | N<br><sub>7.4s</sub> | N<br><sub>6.8s</sub> | N<br><sub>6.5s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>20s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>10s</sub> | N<br><sub>27s</sub> | N<br><sub>49s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>12s</sub> | N<br><sub>9.9s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>22s</sub> | N<br><sub>12s</sub> | N<br><sub>15s</sub> | N<br><sub>24s</sub> | N<br><sub>12s</sub> | N<br><sub>53s</sub> | N<br><sub>26s</sub> | N<br><sub>18s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=34/36 (94.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>0.8s</sub> | – | 7/9 (78%) |

##### Impl L0→L1 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.9s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.2s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>34s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | N<br><sub>26s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | N<br><sub>29s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>330s</sub> | T/o<br><sub>156s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>100s</sub> | N<br><sub>55s</sub> | T/o<br><sub>82s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | Y<br><sub>56s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | – | 1/9 (11%) |
| `0.05` | N<br><sub>6.4s</sub> | N<br><sub>6.2s</sub> | N<br><sub>8.4s</sub> | N<br><sub>7.7s</sub> | N<br><sub>6.8s</sub> | N<br><sub>7.0s</sub> | N<br><sub>5.9s</sub> | N<br><sub>13s</sub> | N<br><sub>8.5s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | N<br><sub>10s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.1s</sub> | N<br><sub>12s</sub> | N<br><sub>6.4s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>9.6s</sub> | N<br><sub>9.6s</sub> | N<br><sub>9.4s</sub> | N<br><sub>11s</sub> | N<br><sub>9.7s</sub> | N<br><sub>11s</sub> | N<br><sub>9.3s</sub> | N<br><sub>9.3s</sub> | N<br><sub>9.1s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>27s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>9.6s</sub> | N<br><sub>7.8s</sub> | N<br><sub>12s</sub> | N<br><sub>9.9s</sub> | N<br><sub>24s</sub> | N<br><sub>9.6s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>11s</sub> | N<br><sub>9.2s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.3s</sub> | N<br><sub>9.0s</sub> | N<br><sub>7.7s</sub> | N<br><sub>11s</sub> | N<br><sub>7.7s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>31s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>68s</sub> | – | 8/9 (89%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>8.2s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | N<br><sub>15s</sub> | N<br><sub>16s</sub> | N<br><sub>48s</sub> | N<br><sub>31s</sub> | N<br><sub>8.5s</sub> | N<br><sub>11s</sub> | N<br><sub>9.9s</sub> | N<br><sub>9.1s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | N<br><sub>17s</sub> | N<br><sub>15s</sub> | N<br><sub>14s</sub> | N<br><sub>17s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>7.9s</sub> | N<br><sub>8.7s</sub> | N<br><sub>7.4s</sub> | N<br><sub>14s</sub> | T/o<br><sub>64s</sub> | N<br><sub>7.6s</sub> | N<br><sub>7.9s</sub> | N<br><sub>21s</sub> | N<br><sub>8.0s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>10s</sub> | N<br><sub>7.8s</sub> | N<br><sub>9.8s</sub> | N<br><sub>16s</sub> | N<br><sub>15s</sub> | N<br><sub>8.5s</sub> | N<br><sub>8.6s</sub> | N<br><sub>10s</sub> | N<br><sub>8.9s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>164s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>89s</sub> | N<br><sub>30s</sub> | T/o<br><sub>300s</sub> | T/o<br><sub>147s</sub> | T/o<br><sub>424s</sub> | T/o<br><sub>195s</sub> | T/o<br><sub>136s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>57s</sub> | Y<br><sub>42s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | – | 2/9 (22%) |
| `0.05` | N<br><sub>6.4s</sub> | N<br><sub>6.3s</sub> | N<br><sub>8.6s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.4s</sub> | N<br><sub>6.3s</sub> | N<br><sub>13s</sub> | N<br><sub>6.5s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | N<br><sub>10s</sub> | N<br><sub>9.1s</sub> | N<br><sub>8.7s</sub> | N<br><sub>12s</sub> | N<br><sub>7.0s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>10.0s</sub> | N<br><sub>8.8s</sub> | N<br><sub>9.7s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | N<br><sub>9.9s</sub> | N<br><sub>10s</sub> | N<br><sub>9.6s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>10s</sub> | Y<br><sub>20s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>14s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | N<br><sub>30s</sub> | N<br><sub>22s</sub> | N<br><sub>7.5s</sub> | N<br><sub>44s</sub> | T/o<br><sub>65s</sub> | N<br><sub>9.3s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>15s</sub> | T/o<br><sub>64s</sub> | N<br><sub>34s</sub> | N<br><sub>8.7s</sub> | N<br><sub>5.7s</sub> | N<br><sub>6.7s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>21s</sub> | N<br><sub>17s</sub> | N<br><sub>20s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.9s</sub> | N<br><sub>16s</sub> | N<br><sub>7.3s</sub> | N<br><sub>11s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>47s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | – | 1/9 (11%) |
| `0.05` | N<br><sub>5.6s</sub> | N<br><sub>5.2s</sub> | N<br><sub>5.3s</sub> | N<br><sub>5.2s</sub> | N<br><sub>6.2s</sub> | N<br><sub>9.6s</sub> | N<br><sub>5.3s</sub> | N<br><sub>14s</sub> | N<br><sub>4.7s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | N<br><sub>8.6s</sub> | N<br><sub>6.6s</sub> | N<br><sub>10s</sub> | N<br><sub>7.4s</sub> | N<br><sub>8.6s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.1s</sub> | N<br><sub>7.2s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>8.1s</sub> | N<br><sub>9.6s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>19s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>18s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>6.6s</sub> | N<br><sub>13s</sub> | N<br><sub>8.8s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | N<br><sub>13s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>29s</sub> | N<br><sub>11s</sub> | N<br><sub>6.1s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>22s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | N<br><sub>27s</sub> | N<br><sub>9.5s</sub> | N<br><sub>6.2s</sub> | N<br><sub>5.9s</sub> | N<br><sub>7.0s</sub> | N<br><sub>16s</sub> | N<br><sub>6.8s</sub> | N<br><sub>38s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=7/36 (19.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>23s</sub> | Y<br><sub>38s</sub> | Y<br><sub>21s</sub> | Y<br><sub>33s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>22s</sub> | Y<br><sub>25s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>23s</sub> | – | 7/9 (78%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | N<br><sub>30s</sub> | T/o<br><sub>169s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>842s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>72s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>86s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>215s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>50s</sub> | Y<br><sub>40s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | 2/9 (22%) |
| `0.05` | N<br><sub>7.6s</sub> | N<br><sub>6.4s</sub> | N<br><sub>8.9s</sub> | N<br><sub>7.9s</sub> | N<br><sub>7.3s</sub> | N<br><sub>7.3s</sub> | N<br><sub>8.0s</sub> | N<br><sub>14s</sub> | N<br><sub>6.3s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>9.2s</sub> | N<br><sub>8.8s</sub> | N<br><sub>12s</sub> | N<br><sub>6.7s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>9.4s</sub> | N<br><sub>9.5s</sub> | N<br><sub>9.9s</sub> | N<br><sub>11s</sub> | N<br><sub>9.6s</sub> | N<br><sub>11s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.6s</sub> | N<br><sub>9.6s</sub> | – | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | N<br><sub>49s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | N<br><sub>7.6s</sub> | N<br><sub>9.2s</sub> | N<br><sub>6.3s</sub> | N<br><sub>9.5s</sub> | T/o<br><sub>65s</sub> | N<br><sub>9.5s</sub> | T/o<br><sub>76s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>21s</sub> | N<br><sub>9.8s</sub> | N<br><sub>12s</sub> | N<br><sub>9.8s</sub> | N<br><sub>7.3s</sub> | N<br><sub>15s</sub> | N<br><sub>18s</sub> | N<br><sub>12s</sub> | N<br><sub>9.2s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | N<br><sub>32s</sub> | N<br><sub>56s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | N<br><sub>32s</sub> | N<br><sub>32s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>18s</sub> | N<br><sub>17s</sub> | N<br><sub>19s</sub> | N<br><sub>30s</sub> | N<br><sub>16s</sub> | N<br><sub>63s</sub> | N<br><sub>33s</sub> | N<br><sub>23s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=34/36 (94.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.8s</sub> | – | 7/9 (78%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>31s</sub> | N<br><sub>19s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | N<br><sub>23s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | N<br><sub>27s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>312s</sub> | T/o<br><sub>148s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | N<br><sub>52s</sub> | N<br><sub>56s</sub> | T/o<br><sub>81s</sub> | – | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>8.2s</sub> | N<br><sub>7.4s</sub> | N<br><sub>10s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.5s</sub> | N<br><sub>9.5s</sub> | N<br><sub>7.5s</sub> | N<br><sub>16s</sub> | N<br><sub>10s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>9.8s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>8.2s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>9.7s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>29s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | N<br><sub>9.6s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | T/o<br><sub>65s</sub> | N<br><sub>13s</sub> | N<br><sub>9.3s</sub> | N<br><sub>7.9s</sub> | N<br><sub>12s</sub> | N<br><sub>9.5s</sub> | N<br><sub>27s</sub> | N<br><sub>9.6s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>10s</sub> | N<br><sub>9.5s</sub> | N<br><sub>7.4s</sub> | N<br><sub>7.7s</sub> | N<br><sub>9.8s</sub> | N<br><sub>8.2s</sub> | N<br><sub>12s</sub> | N<br><sub>7.5s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>55s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>61s</sub> | – | 8/9 (89%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>9.3s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>17s</sub> | N<br><sub>19s</sub> | N<br><sub>21s</sub> | N<br><sub>63s</sub> | N<br><sub>38s</sub> | N<br><sub>11s</sub> | N<br><sub>9.5s</sub> | N<br><sub>52s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>18s</sub> | N<br><sub>21s</sub> | N<br><sub>17s</sub> | N<br><sub>14s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | N<br><sub>16s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>16s</sub> | T/o<br><sub>65s</sub> | N<br><sub>9.4s</sub> | N<br><sub>11s</sub> | N<br><sub>40s</sub> | N<br><sub>8.7s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>16s</sub> | N<br><sub>24s</sub> | N<br><sub>11s</sub> | N<br><sub>9.9s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>120s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>192s</sub> | T/o<br><sub>484s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>1205s</sub> | T/o<br><sub>217s</sub> | – | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>8.2s</sub> | N<br><sub>7.7s</sub> | N<br><sub>11s</sub> | N<br><sub>9.4s</sub> | N<br><sub>9.2s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.0s</sub> | N<br><sub>17s</sub> | N<br><sub>8.0s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>15s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>8.5s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>11s</sub> | Y<br><sub>22s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>14s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | N<br><sub>53s</sub> | T/o<br><sub>61s</sub> | N<br><sub>32s</sub> | N<br><sub>25s</sub> | N<br><sub>8.5s</sub> | N<br><sub>14s</sub> | T/o<br><sub>65s</sub> | N<br><sub>50s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>17s</sub> | T/o<br><sub>67s</sub> | N<br><sub>39s</sub> | N<br><sub>9.4s</sub> | N<br><sub>6.1s</sub> | N<br><sub>7.3s</sub> | N<br><sub>29s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | T/o<br><sub>74s</sub> | N<br><sub>22s</sub> | N<br><sub>8.3s</sub> | N<br><sub>7.5s</sub> | N<br><sub>7.5s</sub> | N<br><sub>17s</sub> | N<br><sub>7.4s</sub> | N<br><sub>33s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>51s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | 1/9 (11%) |
| `0.05` | N<br><sub>5.4s</sub> | N<br><sub>5.4s</sub> | N<br><sub>5.5s</sub> | N<br><sub>6.7s</sub> | N<br><sub>7.6s</sub> | N<br><sub>8.2s</sub> | N<br><sub>5.5s</sub> | N<br><sub>6.2s</sub> | N<br><sub>5.5s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>19s</sub> | N<br><sub>10.0s</sub> | N<br><sub>8.5s</sub> | N<br><sub>13s</sub> | N<br><sub>7.6s</sub> | N<br><sub>9.9s</sub> | N<br><sub>11s</sub> | N<br><sub>8.7s</sub> | N<br><sub>9.4s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>9.5s</sub> | Y<br><sub>40s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>23s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>8.9s</sub> | N<br><sub>16s</sub> | N<br><sub>11s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>15s</sub> | N<br><sub>40s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | N<br><sub>13s</sub> | N<br><sub>7.0s</sub> | N<br><sub>9.2s</sub> | N<br><sub>13s</sub> | N<br><sub>23s</sub> | N<br><sub>15s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | N<br><sub>24s</sub> | N<br><sub>11s</sub> | N<br><sub>6.4s</sub> | N<br><sub>6.5s</sub> | N<br><sub>7.8s</sub> | N<br><sub>16s</sub> | N<br><sub>9.2s</sub> | N<br><sub>48s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=7/36 (19.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>26s</sub> | Y<br><sub>44s</sub> | Y<br><sub>23s</sub> | Y<br><sub>38s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>24s</sub> | Y<br><sub>26s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>24s</sub> | – | 7/9 (78%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>73s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>80s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>166s</sub> | T/o<br><sub>580s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>304s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>85s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>149s</sub> | T/o<br><sub>1022s</sub> | N<br><sub>56s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>154s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>6.8s</sub> | N<br><sub>6.7s</sub> | N<br><sub>11s</sub> | N<br><sub>10.0s</sub> | N<br><sub>9.3s</sub> | N<br><sub>9.1s</sub> | N<br><sub>8.0s</sub> | N<br><sub>17s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>9.9s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>8.1s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>11s</sub> | N<br><sub>9.6s</sub> | N<br><sub>9.6s</sub> | N<br><sub>11s</sub> | N<br><sub>10.0s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | – | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | N<br><sub>44s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>60s</sub> | N<br><sub>7.9s</sub> | N<br><sub>9.0s</sub> | N<br><sub>5.9s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | N<br><sub>11s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>19s</sub> | N<br><sub>10s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>9.0s</sub> | N<br><sub>16s</sub> | N<br><sub>19s</sub> | N<br><sub>15s</sub> | N<br><sub>28s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | N<br><sub>18s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | N<br><sub>34s</sub> | N<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | N<br><sub>36s</sub> | N<br><sub>56s</sub> | N<br><sub>17s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>17s</sub> | N<br><sub>24s</sub> | N<br><sub>19s</sub> | N<br><sub>33s</sub> | N<br><sub>15s</sub> | N<br><sub>66s</sub> | N<br><sub>35s</sub> | N<br><sub>28s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=34/36 (94.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>0.8s</sub> | – | 7/9 (78%) |

##### Impl L0→L1 [!A->!B] (α=0.9) — Y=7/36 (19.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>28s</sub> | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | Y<br><sub>38s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>33s</sub> | Y<br><sub>26s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>28s</sub> | – | 7/9 (78%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>54s</sub> | N<br><sub>14s</sub> | N<br><sub>49s</sub> | T/o<br><sub>62s</sub> | N<br><sub>16s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>21s</sub> | N<br><sub>67s</sub> | N<br><sub>22s</sub> | N<br><sub>16s</sub> | N<br><sub>17s</sub> | N<br><sub>16s</sub> | N<br><sub>87s</sub> | N<br><sub>15s</sub> | N<br><sub>20s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>22s</sub> | N<br><sub>27s</sub> | N<br><sub>17s</sub> | N<br><sub>20s</sub> | N<br><sub>24s</sub> | N<br><sub>20s</sub> | N<br><sub>25s</sub> | N<br><sub>22s</sub> | N<br><sub>27s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | N<br><sub>11s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>26s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | N<br><sub>19s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>2902s</sub> | T/o<br><sub>231s</sub> | T/o<br><sub>347s</sub> | T/o<br><sub>407s</sub> | T/o<br><sub>203s</sub> | T/o<br><sub>354s</sub> | T/o<br><sub>200s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>867s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.9) — Y=7/36 (19.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>20s</sub> | Y<br><sub>17s</sub> | Y<br><sub>19s</sub> | Y<br><sub>22s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>23s</sub> | Y<br><sub>20s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>18s</sub> | – | 7/9 (78%) |
| `0.05` | N<br><sub>13s</sub> | N<br><sub>17s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>10s</sub> | N<br><sub>18s</sub> | N<br><sub>13s</sub> | N<br><sub>18s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>27s</sub> | N<br><sub>17s</sub> | N<br><sub>49s</sub> | N<br><sub>30s</sub> | N<br><sub>17s</sub> | N<br><sub>40s</sub> | N<br><sub>26s</sub> | N<br><sub>27s</sub> | N<br><sub>19s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>23s</sub> | N<br><sub>22s</sub> | N<br><sub>25s</sub> | N<br><sub>30s</sub> | N<br><sub>20s</sub> | N<br><sub>22s</sub> | N<br><sub>40s</sub> | N<br><sub>24s</sub> | N<br><sub>17s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.0s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | 9/9 (100%) |
| `0.05` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>18s</sub> | N<br><sub>7.5s</sub> | N<br><sub>15s</sub> | N<br><sub>11s</sub> | N<br><sub>24s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>20s</sub> | N<br><sub>16s</sub> | N<br><sub>24s</sub> | N<br><sub>22s</sub> | N<br><sub>18s</sub> | N<br><sub>17s</sub> | N<br><sub>18s</sub> | N<br><sub>19s</sub> | N<br><sub>20s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>16s</sub> | N<br><sub>21s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | N<br><sub>29s</sub> | N<br><sub>17s</sub> | N<br><sub>17s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>9.0s</sub> | N<br><sub>7.4s</sub> | N<br><sub>9.5s</sub> | N<br><sub>8.0s</sub> | N<br><sub>8.9s</sub> | N<br><sub>9.0s</sub> | N<br><sub>7.6s</sub> | N<br><sub>16s</sub> | N<br><sub>7.8s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>15s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | N<br><sub>8.1s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>14s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | N<br><sub>33s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>11s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>9.1s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>29s</sub> | N<br><sub>10s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>9.4s</sub> | N<br><sub>8.3s</sub> | N<br><sub>9.9s</sub> | N<br><sub>8.3s</sub> | N<br><sub>13s</sub> | N<br><sub>8.6s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.95) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>35s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | T/o<br><sub>60s</sub> | – | 8/9 (89%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>18s</sub> | N<br><sub>20s</sub> | N<br><sub>11s</sub> | N<br><sub>63s</sub> | N<br><sub>34s</sub> | N<br><sub>10s</sub> | T/o<br><sub>68s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>21s</sub> | N<br><sub>19s</sub> | N<br><sub>19s</sub> | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>25s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>16s</sub> | T/o<br><sub>63s</sub> | N<br><sub>10s</sub> | N<br><sub>11s</sub> | N<br><sub>43s</sub> | N<br><sub>10s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>20s</sub> | N<br><sub>19s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.95) — Y=7/36 (19.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>42s</sub> | Y<br><sub>39s</sub> | Y<br><sub>24s</sub> | Y<br><sub>34s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>23s</sub> | Y<br><sub>22s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>33s</sub> | – | 7/9 (78%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | N<br><sub>12s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | N<br><sub>12s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>17s</sub> | N<br><sub>55s</sub> | N<br><sub>19s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>23s</sub> | N<br><sub>72s</sub> | N<br><sub>12s</sub> | N<br><sub>16s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>18s</sub> | N<br><sub>18s</sub> | N<br><sub>13s</sub> | T/o<br><sub>465s</sub> | T/o<br><sub>293s</sub> | N<br><sub>29s</sub> | N<br><sub>45s</sub> | N<br><sub>92s</sub> | N<br><sub>26s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>17s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | N<br><sub>26s</sub> | T/o<br><sub>239s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | N<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>96s</sub> | T/o<br><sub>636s</sub> | T/o<br><sub>1218s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>201s</sub> | T/o<br><sub>254s</sub> | T/o<br><sub>585s</sub> | T/o<br><sub>545s</sub> | T/o<br><sub>96s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.95) — Y=7/36 (19.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>19s</sub> | Y<br><sub>31s</sub> | Y<br><sub>21s</sub> | Y<br><sub>19s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>18s</sub> | – | 7/9 (78%) |
| `0.05` | N<br><sub>19s</sub> | N<br><sub>18s</sub> | N<br><sub>14s</sub> | N<br><sub>9.8s</sub> | N<br><sub>9.3s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>21s</sub> | N<br><sub>17s</sub> | N<br><sub>43s</sub> | N<br><sub>24s</sub> | N<br><sub>17s</sub> | N<br><sub>31s</sub> | N<br><sub>24s</sub> | N<br><sub>25s</sub> | N<br><sub>17s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>22s</sub> | N<br><sub>21s</sub> | N<br><sub>16s</sub> | N<br><sub>23s</sub> | N<br><sub>18s</sub> | N<br><sub>23s</sub> | N<br><sub>22s</sub> | N<br><sub>20s</sub> | N<br><sub>22s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | 9/9 (100%) |
| `0.05` | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>16s</sub> | N<br><sub>10s</sub> | N<br><sub>9.1s</sub> | N<br><sub>14s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>21s</sub> | N<br><sub>17s</sub> | N<br><sub>27s</sub> | N<br><sub>23s</sub> | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>19s</sub> | N<br><sub>24s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>16s</sub> | N<br><sub>18s</sub> | N<br><sub>23s</sub> | N<br><sub>20s</sub> | N<br><sub>17s</sub> | N<br><sub>20s</sub> | N<br><sub>18s</sub> | N<br><sub>15s</sub> | N<br><sub>17s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>8.5s</sub> | N<br><sub>7.3s</sub> | N<br><sub>10s</sub> | N<br><sub>10s</sub> | N<br><sub>9.0s</sub> | N<br><sub>8.7s</sub> | N<br><sub>7.2s</sub> | N<br><sub>17s</sub> | N<br><sub>7.3s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>15s</sub> | N<br><sub>12s</sub> | N<br><sub>9.0s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>7.9s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>13s</sub> | Y<br><sub>25s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>17s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>37s</sub> | N<br><sub>27s</sub> | N<br><sub>9.4s</sub> | N<br><sub>16s</sub> | T/o<br><sub>62s</sub> | N<br><sub>52s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>20s</sub> | N<br><sub>47s</sub> | N<br><sub>46s</sub> | N<br><sub>12s</sub> | N<br><sub>7.7s</sub> | N<br><sub>9.2s</sub> | N<br><sub>36s</sub> | N<br><sub>18s</sub> | N<br><sub>19s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>28s</sub> | T/o<br><sub>61s</sub> | N<br><sub>27s</sub> | N<br><sub>10s</sub> | N<br><sub>9.8s</sub> | N<br><sub>10s</sub> | N<br><sub>20s</sub> | N<br><sub>7.4s</sub> | N<br><sub>11s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>55s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | – | 1/9 (11%) |
| `0.05` | N<br><sub>7.6s</sub> | N<br><sub>7.2s</sub> | N<br><sub>8.0s</sub> | N<br><sub>7.2s</sub> | N<br><sub>8.8s</sub> | N<br><sub>8.9s</sub> | N<br><sub>6.8s</sub> | N<br><sub>8.2s</sub> | N<br><sub>6.7s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>22s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>14s</sub> | N<br><sub>10s</sub> | N<br><sub>12s</sub> | N<br><sub>9.4s</sub> | N<br><sub>12s</sub> | N<br><sub>10s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>13s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>12s</sub> | Y<br><sub>27s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>25s</sub> | Y<br><sub>0.8s</sub> | – | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | N<br><sub>8.7s</sub> | N<br><sub>18s</sub> | N<br><sub>13s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | N<br><sub>17s</sub> | N<br><sub>38s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>14s</sub> | N<br><sub>8.0s</sub> | N<br><sub>11s</sub> | N<br><sub>14s</sub> | N<br><sub>27s</sub> | N<br><sub>18s</sub> | N<br><sub>16s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | N<br><sub>35s</sub> | N<br><sub>12s</sub> | N<br><sub>8.3s</sub> | N<br><sub>6.6s</sub> | N<br><sub>9.4s</sub> | N<br><sub>21s</sub> | N<br><sub>8.2s</sub> | N<br><sub>50s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>60s</sub> | Y<br><sub>28s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>57s</sub> | Y<br><sub>58s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>64s</sub> | – | 4/9 (44%) |
| `0.05` | T/o<br><sub>76s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>73s</sub> | N<br><sub>13s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>69s</sub> | N<br><sub>283s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>326s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>74s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>317s</sub> | T/o<br><sub>426s</sub> | T/o<br><sub>106s</sub> | N<br><sub>21s</sub> | T/o<br><sub>77s</sub> | N<br><sub>20s</sub> | T/o<br><sub>73s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>9.2s</sub> | N<br><sub>12s</sub> | N<br><sub>7.4s</sub> | N<br><sub>6.7s</sub> | N<br><sub>7.8s</sub> | N<br><sub>8.4s</sub> | N<br><sub>8.5s</sub> | N<br><sub>9.7s</sub> | N<br><sub>6.7s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | N<br><sub>9.5s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>10s</sub> | N<br><sub>9.8s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>450s</sub> | T/o<br><sub>107266s</sub> | T/o<br><sub>592s</sub> | T/o<br><sub>849s</sub> | T/o<br><sub>1237s</sub> | T/o<br><sub>819s</sub> | T/o<br><sub>331s</sub> | T/o<br><sub>535s</sub> | N<br><sub>36s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=7/36 (19.4%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>20s</sub> | Y<br><sub>24s</sub> | Y<br><sub>18s</sub> | Y<br><sub>22s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>17s</sub> | Y<br><sub>18s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>22s</sub> | – | 7/9 (78%) |
| `0.05` | N<br><sub>16s</sub> | N<br><sub>19s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>15s</sub> | N<br><sub>12s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>23s</sub> | N<br><sub>21s</sub> | N<br><sub>34s</sub> | N<br><sub>22s</sub> | N<br><sub>17s</sub> | N<br><sub>19s</sub> | N<br><sub>25s</sub> | N<br><sub>31s</sub> | N<br><sub>24s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>21s</sub> | N<br><sub>20s</sub> | N<br><sub>18s</sub> | N<br><sub>22s</sub> | N<br><sub>38s</sub> | N<br><sub>19s</sub> | N<br><sub>33s</sub> | N<br><sub>23s</sub> | N<br><sub>22s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>8.0s</sub> | N<br><sub>11s</sub> | N<br><sub>9.0s</sub> | N<br><sub>6.5s</sub> | N<br><sub>6.9s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>6.4s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>17s</sub> | N<br><sub>18s</sub> | N<br><sub>8.8s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>16s</sub> | N<br><sub>11s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>14s</sub> | N<br><sub>16s</sub> | N<br><sub>13s</sub> | N<br><sub>16s</sub> | N<br><sub>13s</sub> | N<br><sub>16s</sub> | N<br><sub>13s</sub> | N<br><sub>14s</sub> | N<br><sub>14s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.05` | N<br><sub>8.1s</sub> | N<br><sub>7.7s</sub> | N<br><sub>13s</sub> | N<br><sub>10s</sub> | N<br><sub>9.4s</sub> | N<br><sub>9.5s</sub> | N<br><sub>7.9s</sub> | N<br><sub>17s</sub> | N<br><sub>7.6s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>13s</sub> | N<br><sub>15s</sub> | N<br><sub>13s</sub> | N<br><sub>11s</sub> | N<br><sub>11s</sub> | N<br><sub>15s</sub> | N<br><sub>8.4s</sub> | – | 0/9 (0%) |
| `0.20` | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | N<br><sub>13s</sub> | N<br><sub>12s</sub> | N<br><sub>14s</sub> | N<br><sub>11s</sub> | N<br><sub>12s</sub> | N<br><sub>12s</sub> | – | 0/9 (0%) |

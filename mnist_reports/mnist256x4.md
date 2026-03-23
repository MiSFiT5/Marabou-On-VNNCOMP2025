# MNIST Report: mnist256x4

> **MNIST** — mnist256x4 (4 hidden layers, 256 neurons each)  
> Per-class experiments, no rule cap  
> Generated 2026-03-20

**Model file:** `mnist-net_256x4.onnx`  
**Architecture:** 784 → 256 → 256 → 256 → 256 → 10  
**Classes with at least one experiment:** 0, 2, 3, 4, 5, 6, 7, 9 (8 total)  
**Missing classes in current results:** 1, 8  
**Layer pairs:** L01, L12, L23  
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
| 0.90 | 63/63 (100.0%) | 63/63 (100.0%) | 63/63 (100.0%) | 63/63 (100.0%) |
| 0.95 | 63/63 (100.0%) | 63/63 (100.0%) | 61/63 (96.8%) | 58/63 (92.1%) |
| 0.99 | 54/63 (85.7%) | 36/63 (57.1%) | 36/63 (57.1%) | 36/63 (57.1%) |

---

## Aggregated Summary (row-level counts across all classes)

### Full-Rule

#### α = 0.9

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.9)` | 63/63 (100.0%) | 63/63 (100.0%) | 59/63 (93.7%) | 57/63 (90.5%) | 96.0% |
| `ALWAYS_ON (α=0.9)` | 39/63 (61.9%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 15.5% |
| `ALWAYS_ON+OFF (α=0.9)` | 63/63 (100.0%) | 63/63 (100.0%) | 63/63 (100.0%) | 63/63 (100.0%) | 100.0% |
| `Impl L0→L1 (α=0.9)` | 45/63 (71.4%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 17.9% |
| `Impl L1→L2 (α=0.9)` | 18/63 (28.6%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 7.1% |
| `Impl L2→L3 (α=0.9)` | 45/63 (71.4%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 17.9% |
| `none (baseline)` | 22/63 (34.9%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 8.7% |

#### α = 0.95

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.95)` | 63/63 (100.0%) | 59/63 (93.7%) | 56/63 (88.9%) | 57/63 (90.5%) | 93.3% |
| `ALWAYS_ON (α=0.95)` | 41/63 (65.1%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 16.3% |
| `ALWAYS_ON+OFF (α=0.95)` | 63/63 (100.0%) | 63/63 (100.0%) | 61/63 (96.8%) | 57/63 (90.5%) | 96.8% |
| `Impl L0→L1 (α=0.95)` | 54/63 (85.7%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 21.4% |
| `Impl L1→L2 (α=0.95)` | 27/63 (42.9%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 10.7% |
| `Impl L2→L3 (α=0.95)` | 54/63 (85.7%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 21.4% |
| `none (baseline)` | 30/63 (47.6%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 11.9% |

#### α = 0.99

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.99)` | 50/63 (79.4%) | 36/63 (57.1%) | 36/63 (57.1%) | 36/63 (57.1%) | 62.7% |
| `ALWAYS_ON (α=0.99)` | 23/63 (36.5%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 9.1% |
| `ALWAYS_ON+OFF (α=0.99)` | 53/63 (84.1%) | 36/63 (57.1%) | 36/63 (57.1%) | 36/63 (57.1%) | 63.9% |
| `Impl L0→L1 (α=0.99)` | 37/63 (58.7%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 14.7% |
| `Impl L1→L2 (α=0.99)` | 18/63 (28.6%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 7.1% |
| `Impl L2→L3 (α=0.99)` | 45/63 (71.4%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 17.9% |
| `none (baseline)` | 22/63 (34.9%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 8.7% |

### Per-Layer

#### α = 0.9

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.9)` | 171/171 (100.0%) | 171/171 (100.0%) | 159/171 (93.0%) | 153/171 (89.5%) | 95.6% |
| `ALWAYS_ON (α=0.9)` | 99/171 (57.9%) | 0/171 (0.0%) | 0/171 (0.0%) | 0/171 (0.0%) | 14.5% |
| `ALWAYS_ON+OFF (α=0.9)` | 171/171 (100.0%) | 171/171 (100.0%) | 171/171 (100.0%) | 171/171 (100.0%) | 100.0% |
| `Impl L0→L1 (α=0.9)` | 45/63 (71.4%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 17.9% |
| `Impl L1→L2 (α=0.9)` | 18/54 (33.3%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 8.3% |
| `Impl L2→L3 (α=0.9)` | 36/54 (66.7%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 16.7% |
| `none (baseline)` | 66/171 (38.6%) | 0/171 (0.0%) | 0/171 (0.0%) | 0/171 (0.0%) | 9.6% |

#### α = 0.95

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.95)` | 171/171 (100.0%) | 159/171 (93.0%) | 150/171 (87.7%) | 153/171 (89.5%) | 92.5% |
| `ALWAYS_ON (α=0.95)` | 105/171 (61.4%) | 0/171 (0.0%) | 0/171 (0.0%) | 0/171 (0.0%) | 15.4% |
| `ALWAYS_ON+OFF (α=0.95)` | 171/171 (100.0%) | 171/171 (100.0%) | 165/171 (96.5%) | 153/171 (89.5%) | 96.5% |
| `Impl L0→L1 (α=0.95)` | 54/63 (85.7%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 21.4% |
| `Impl L1→L2 (α=0.95)` | 18/54 (33.3%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 8.3% |
| `Impl L2→L3 (α=0.95)` | 45/54 (83.3%) | 0/54 (0.0%) | 0/54 (0.0%) | 0/54 (0.0%) | 20.8% |
| `none (baseline)` | 69/171 (40.4%) | 0/171 (0.0%) | 0/171 (0.0%) | 0/171 (0.0%) | 10.1% |

#### α = 0.99

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.99)` | 150/189 (79.4%) | 108/189 (57.1%) | 108/189 (57.1%) | 108/189 (57.1%) | 62.7% |
| `ALWAYS_ON (α=0.99)` | 69/189 (36.5%) | 0/189 (0.0%) | 0/189 (0.0%) | 0/189 (0.0%) | 9.1% |
| `ALWAYS_ON+OFF (α=0.99)` | 159/189 (84.1%) | 108/189 (57.1%) | 108/189 (57.1%) | 108/189 (57.1%) | 63.9% |
| `Impl L0→L1 (α=0.99)` | 37/63 (58.7%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 14.7% |
| `Impl L1→L2 (α=0.99)` | 18/63 (28.6%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 7.1% |
| `Impl L2→L3 (α=0.99)` | 45/63 (71.4%) | 0/63 (0.0%) | 0/63 (0.0%) | 0/63 (0.0%) | 17.9% |
| `none (baseline)` | 66/189 (34.9%) | 0/189 (0.0%) | 0/189 (0.0%) | 0/189 (0.0%) | 8.7% |

### Impl Ablation

#### α = 0.9

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.9)` | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 100.0% |
| `ALWAYS_ON (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `ALWAYS_ON+OFF (α=0.9)` | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 100.0% |
| `Impl L0→L1 [!A->!B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L0→L1 [!A->B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L0→L1 [A->!B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L0→L1 [A->B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L1→L2 [!A->!B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L1→L2 [!A->B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L1→L2 [A->!B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L1→L2 [A->B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L2→L3 [!A->!B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L2→L3 [!A->B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L2→L3 [A->!B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L2→L3 [A->B] (α=0.9)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `none (baseline)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |

#### α = 0.95

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.95)` | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 100.0% |
| `ALWAYS_ON (α=0.95)` | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 8.3% |
| `ALWAYS_ON+OFF (α=0.95)` | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 9/9 (100.0%) | 100.0% |
| `Impl L0→L1 [!A->!B] (α=0.95)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L0→L1 [!A->B] (α=0.95)` | 1/9 (11.1%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 2.8% |
| `Impl L0→L1 [A->!B] (α=0.95)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L0→L1 [A->B] (α=0.95)` | 1/9 (11.1%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 2.8% |
| `Impl L1→L2 [!A->!B] (α=0.95)` | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0.0% |
| `Impl L1→L2 [!A->B] (α=0.95)` | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 8.3% |
| `Impl L1→L2 [A->!B] (α=0.95)` | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0.0% |
| `Impl L1→L2 [A->B] (α=0.95)` | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 8.3% |
| `Impl L2→L3 [!A->!B] (α=0.95)` | 9/9 (100.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 25.0% |
| `Impl L2→L3 [!A->B] (α=0.95)` | 2/9 (22.2%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 5.6% |
| `Impl L2→L3 [A->!B] (α=0.95)` | 3/9 (33.3%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 8.3% |
| `Impl L2→L3 [A->B] (α=0.95)` | 2/9 (22.2%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 5.6% |
| `none (baseline)` | 2/9 (22.2%) | 0/9 (0.0%) | 0/9 (0.0%) | 0/9 (0.0%) | 5.6% |

#### α = 0.99

| Rule | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 | Total Y% |
|------|--------|--------|--------|--------|----------|
| `ALWAYS_OFF (α=0.99)` | 33/45 (73.3%) | 27/45 (60.0%) | 27/45 (60.0%) | 27/45 (60.0%) | 63.3% |
| `ALWAYS_ON (α=0.99)` | 14/45 (31.1%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 7.8% |
| `ALWAYS_ON+OFF (α=0.99)` | 35/45 (77.8%) | 27/45 (60.0%) | 27/45 (60.0%) | 27/45 (60.0%) | 64.4% |
| `Impl L0→L1 [!A->!B] (α=0.99)` | 19/45 (42.2%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 10.6% |
| `Impl L0→L1 [!A->B] (α=0.99)` | 11/45 (24.4%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 6.1% |
| `Impl L0→L1 [A->!B] (α=0.99)` | 26/45 (57.8%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 14.4% |
| `Impl L0→L1 [A->B] (α=0.99)` | 12/45 (26.7%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 6.7% |
| `Impl L1→L2 [!A->!B] (α=0.99)` | 9/45 (20.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 5.0% |
| `Impl L1→L2 [!A->B] (α=0.99)` | 12/45 (26.7%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 6.7% |
| `Impl L1→L2 [A->!B] (α=0.99)` | 12/45 (26.7%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 6.7% |
| `Impl L1→L2 [A->B] (α=0.99)` | 12/45 (26.7%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 6.7% |
| `Impl L2→L3 [!A->!B] (α=0.99)` | 35/45 (77.8%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 19.4% |
| `Impl L2→L3 [!A->B] (α=0.99)` | 12/45 (26.7%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 6.7% |
| `Impl L2→L3 [A->!B] (α=0.99)` | 13/45 (28.9%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 7.2% |
| `Impl L2→L3 [A->B] (α=0.99)` | 12/45 (26.7%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 6.7% |
| `none (baseline)` | 13/45 (28.9%) | 0/45 (0.0%) | 0/45 (0.0%) | 0/45 (0.0%) | 7.2% |

---

## Per-Class Details

### Class 0

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>9.7s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10.0s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10.0s</sub> | Y<br><sub>10s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>79s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>13s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>9.1s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.0s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.1s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>71s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>100s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>87s</sub> | N<br><sub>82s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>50s</sub> | N<br><sub>54s</sub> | N<br><sub>51s</sub> | N<br><sub>51s</sub> | N<br><sub>55s</sub> | N<br><sub>51s</sub> | N<br><sub>50s</sub> | N<br><sub>50s</sub> | N<br><sub>51s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>88s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>11s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>11s</sub> | Y<br><sub>10s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>65s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | – | T/o<br><sub>71s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>94s</sub> | 0/9 (0%) |
| `0.10` | – | T/o<br><sub>82s</sub> | N<br><sub>77s</sub> | N<br><sub>81s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.20` | – | N<br><sub>48s</sub> | N<br><sub>51s</sub> | N<br><sub>49s</sub> | N<br><sub>49s</sub> | N<br><sub>53s</sub> | N<br><sub>49s</sub> | N<br><sub>49s</sub> | N<br><sub>48s</sub> | N<br><sub>49s</sub> | 0/9 (0%) |

### Class 2

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>27s</sub> | Y<br><sub>28s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>27s</sub> | Y<br><sub>27s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>92s</sub> | T/o<br><sub>89s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>16s</sub> | Y<br><sub>38s</sub> | – | Y<br><sub>37s</sub> | Y<br><sub>39s</sub> | Y<br><sub>39s</sub> | Y<br><sub>39s</sub> | Y<br><sub>39s</sub> | Y<br><sub>40s</sub> | Y<br><sub>39s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>117s</sub> | T/o<br><sub>120s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>113s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>142s</sub> | T/o<br><sub>127s</sub> | – | T/o<br><sub>116s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>151s</sub> | T/o<br><sub>138s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>118s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>130s</sub> | T/o<br><sub>132s</sub> | – | T/o<br><sub>113s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>138s</sub> | T/o<br><sub>146s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>118s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>168s</sub> | T/o<br><sub>149s</sub> | – | T/o<br><sub>138s</sub> | T/o<br><sub>134s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>183s</sub> | T/o<br><sub>166s</sub> | T/o<br><sub>140s</sub> | T/o<br><sub>140s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>96s</sub> | T/o<br><sub>99s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>104s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>95s</sub> | – | T/o<br><sub>96s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>121s</sub> | T/o<br><sub>108s</sub> | – | T/o<br><sub>98s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>101s</sub> | 0/9 (0%) |

##### none (baseline) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>29s</sub> | Y<br><sub>32s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>36s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>100s</sub> | Y<br><sub>53s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>53s</sub> | N<br><sub>26s</sub> | – | N<br><sub>24s</sub> | T/o<br><sub>73s</sub> | N<br><sub>26s</sub> | N<br><sub>25s</sub> | T/o<br><sub>66s</sub> | N<br><sub>23s</sub> | N<br><sub>25s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>28s</sub> | N<br><sub>47s</sub> | – | N<br><sub>27s</sub> | N<br><sub>28s</sub> | N<br><sub>26s</sub> | N<br><sub>30s</sub> | N<br><sub>32s</sub> | N<br><sub>26s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>48s</sub> | Y<br><sub>51s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>45s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>72s</sub> | N<br><sub>75s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | N<br><sub>66s</sub> | N<br><sub>76s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>67s</sub> | N<br><sub>63s</sub> | N<br><sub>60s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>82s</sub> | N<br><sub>57s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>16s</sub> | Y<br><sub>38s</sub> | – | Y<br><sub>38s</sub> | Y<br><sub>38s</sub> | Y<br><sub>38s</sub> | Y<br><sub>38s</sub> | Y<br><sub>38s</sub> | Y<br><sub>38s</sub> | Y<br><sub>38s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>74s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>145s</sub> | T/o<br><sub>130s</sub> | – | T/o<br><sub>95s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>152s</sub> | T/o<br><sub>142s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>122s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>131s</sub> | T/o<br><sub>134s</sub> | – | T/o<br><sub>133s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | – | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>116s</sub> | T/o<br><sub>118s</sub> | – | T/o<br><sub>116s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>104s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>150s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>148s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### none (baseline) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>44s</sub> | Y<br><sub>54s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>67s</sub> | Y<br><sub>58s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>64s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>150s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>122s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>79s</sub> | N<br><sub>46s</sub> | – | N<br><sub>43s</sub> | T/o<br><sub>65s</sub> | N<br><sub>48s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | N<br><sub>40s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>48s</sub> | N<br><sub>76s</sub> | – | N<br><sub>46s</sub> | N<br><sub>45s</sub> | N<br><sub>45s</sub> | N<br><sub>44s</sub> | N<br><sub>61s</sub> | N<br><sub>43s</sub> | N<br><sub>46s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>43s</sub> | Y<br><sub>27s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>72s</sub> | Y<br><sub>39s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>41s</sub> | T/o<br><sub>78s</sub> | N<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>52s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>114s</sub> | N<br><sub>17s</sub> | T/o<br><sub>118s</sub> | N<br><sub>18s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>74s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>31s</sub> | Y<br><sub>29s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>45s</sub> | Y<br><sub>32s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | Y<br><sub>49s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>107s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | – | N<br><sub>71s</sub> | T/o<br><sub>97s</sub> | N<br><sub>44s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>73s</sub> | N<br><sub>30s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>40s</sub> | N<br><sub>52s</sub> | – | N<br><sub>37s</sub> | N<br><sub>48s</sub> | N<br><sub>35s</sub> | N<br><sub>38s</sub> | T/o<br><sub>61s</sub> | N<br><sub>36s</sub> | N<br><sub>35s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>14s</sub> | Y<br><sub>12s</sub> | – | Y<br><sub>36s</sub> | Y<br><sub>42s</sub> | Y<br><sub>14s</sub> | Y<br><sub>18s</sub> | Y<br><sub>17s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>18s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>50s</sub> | T/o<br><sub>63s</sub> | N<br><sub>29s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | N<br><sub>35s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>83s</sub> | N<br><sub>17s</sub> | T/o<br><sub>68s</sub> | N<br><sub>19s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | N<br><sub>19s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>75s</sub> | Y<br><sub>52s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>70s</sub> | 1/9 (11%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>87s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>102s</sub> | T/o<br><sub>103s</sub> | – | T/o<br><sub>103s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>94s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>133s</sub> | T/o<br><sub>119s</sub> | – | T/o<br><sub>111s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>144s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>112s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.2s</sub> | Y<br><sub>9.2s</sub> | – | Y<br><sub>23s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.3s</sub> | Y<br><sub>9.3s</sub> | Y<br><sub>9.4s</sub> | Y<br><sub>32s</sub> | Y<br><sub>9.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>70s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>95s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |

##### none (baseline) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>44s</sub> | Y<br><sub>49s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | Y<br><sub>37s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>98s</sub> | Y<br><sub>54s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>92s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>91s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | N<br><sub>35s</sub> | – | N<br><sub>32s</sub> | T/o<br><sub>64s</sub> | N<br><sub>34s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | N<br><sub>28s</sub> | N<br><sub>30s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>35s</sub> | N<br><sub>58s</sub> | – | N<br><sub>34s</sub> | N<br><sub>33s</sub> | N<br><sub>32s</sub> | N<br><sub>34s</sub> | N<br><sub>50s</sub> | N<br><sub>33s</sub> | N<br><sub>33s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>27s</sub> | Y<br><sub>27s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>27s</sub> | Y<br><sub>27s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>95s</sub> | T/o<br><sub>88s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>16s</sub> | Y<br><sub>39s</sub> | – | Y<br><sub>39s</sub> | Y<br><sub>40s</sub> | Y<br><sub>40s</sub> | Y<br><sub>39s</sub> | Y<br><sub>39s</sub> | Y<br><sub>39s</sub> | Y<br><sub>39s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>116s</sub> | T/o<br><sub>122s</sub> | – | T/o<br><sub>102s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>113s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>141s</sub> | T/o<br><sub>126s</sub> | – | T/o<br><sub>115s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>150s</sub> | T/o<br><sub>139s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>117s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>28s</sub> | Y<br><sub>31s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>34s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>89s</sub> | Y<br><sub>51s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>79s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>60s</sub> | N<br><sub>28s</sub> | – | N<br><sub>26s</sub> | T/o<br><sub>65s</sub> | N<br><sub>30s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | N<br><sub>23s</sub> | N<br><sub>27s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>30s</sub> | T/o<br><sub>79s</sub> | – | N<br><sub>28s</sub> | N<br><sub>29s</sub> | N<br><sub>27s</sub> | N<br><sub>31s</sub> | N<br><sub>44s</sub> | N<br><sub>29s</sub> | N<br><sub>29s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>28s</sub> | Y<br><sub>28s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>27s</sub> | Y<br><sub>28s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>98s</sub> | T/o<br><sub>91s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.9) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>131s</sub> | T/o<br><sub>135s</sub> | – | T/o<br><sub>135s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>139s</sub> | T/o<br><sub>149s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>119s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>175s</sub> | T/o<br><sub>154s</sub> | – | T/o<br><sub>139s</sub> | T/o<br><sub>139s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>187s</sub> | T/o<br><sub>168s</sub> | T/o<br><sub>143s</sub> | T/o<br><sub>144s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>28s</sub> | Y<br><sub>32s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | Y<br><sub>34s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>89s</sub> | Y<br><sub>53s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>59s</sub> | N<br><sub>36s</sub> | – | N<br><sub>26s</sub> | T/o<br><sub>62s</sub> | N<br><sub>28s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>73s</sub> | N<br><sub>25s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>29s</sub> | N<br><sub>48s</sub> | – | N<br><sub>27s</sub> | N<br><sub>28s</sub> | N<br><sub>27s</sub> | N<br><sub>29s</sub> | N<br><sub>42s</sub> | N<br><sub>27s</sub> | N<br><sub>29s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>98s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.9) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | Y<br><sub>20s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>105s</sub> | T/o<br><sub>101s</sub> | – | T/o<br><sub>102s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>116s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>95s</sub> | T/o<br><sub>95s</sub> | – | T/o<br><sub>94s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>96s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>146s</sub> | T/o<br><sub>126s</sub> | – | T/o<br><sub>116s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>151s</sub> | T/o<br><sub>143s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>127s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>29s</sub> | Y<br><sub>32s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>33s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>88s</sub> | Y<br><sub>50s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>80s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>28s</sub> | – | N<br><sub>26s</sub> | T/o<br><sub>61s</sub> | N<br><sub>27s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | N<br><sub>22s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>27s</sub> | N<br><sub>42s</sub> | – | N<br><sub>25s</sub> | N<br><sub>26s</sub> | N<br><sub>24s</sub> | N<br><sub>26s</sub> | N<br><sub>37s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>53s</sub> | Y<br><sub>58s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>53s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>82s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>75s</sub> | N<br><sub>78s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>73s</sub> | N<br><sub>67s</sub> | N<br><sub>79s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>68s</sub> | N<br><sub>66s</sub> | N<br><sub>63s</sub> | T/o<br><sub>77s</sub> | N<br><sub>67s</sub> | N<br><sub>53s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>17s</sub> | Y<br><sub>41s</sub> | – | Y<br><sub>42s</sub> | Y<br><sub>41s</sub> | Y<br><sub>41s</sub> | Y<br><sub>42s</sub> | Y<br><sub>41s</sub> | Y<br><sub>42s</sub> | Y<br><sub>42s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>55s</sub> | Y<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>83s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>143s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | – | N<br><sub>50s</sub> | T/o<br><sub>72s</sub> | N<br><sub>49s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | N<br><sub>43s</sub> | N<br><sub>47s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>53s</sub> | N<br><sub>83s</sub> | – | N<br><sub>50s</sub> | N<br><sub>51s</sub> | N<br><sub>49s</sub> | N<br><sub>52s</sub> | T/o<br><sub>62s</sub> | N<br><sub>50s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L12) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>54s</sub> | Y<br><sub>58s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>53s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>84s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>83s</sub> | T/o<br><sub>81s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>76s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | N<br><sub>65s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>81s</sub> | N<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.95) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>54s</sub> | Y<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>76s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>139s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | N<br><sub>53s</sub> | – | N<br><sub>50s</sub> | T/o<br><sub>73s</sub> | N<br><sub>55s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | N<br><sub>43s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>54s</sub> | N<br><sub>83s</sub> | – | N<br><sub>50s</sub> | N<br><sub>51s</sub> | N<br><sub>49s</sub> | N<br><sub>52s</sub> | T/o<br><sub>62s</sub> | N<br><sub>50s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L23) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>53s</sub> | Y<br><sub>58s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>53s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>82s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>82s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>64s</sub> | N<br><sub>58s</sub> | N<br><sub>64s</sub> | T/o<br><sub>78s</sub> | N<br><sub>67s</sub> | N<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>17s</sub> | Y<br><sub>24s</sub> | – | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | Y<br><sub>23s</sub> | Y<br><sub>24s</sub> | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>118s</sub> | T/o<br><sub>120s</sub> | – | T/o<br><sub>119s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>109s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>55s</sub> | Y<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>78s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>82s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>143s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | N<br><sub>52s</sub> | – | N<br><sub>50s</sub> | T/o<br><sub>73s</sub> | N<br><sub>53s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | N<br><sub>43s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>54s</sub> | N<br><sub>83s</sub> | – | N<br><sub>50s</sub> | N<br><sub>51s</sub> | N<br><sub>49s</sub> | N<br><sub>52s</sub> | T/o<br><sub>62s</sub> | N<br><sub>49s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>46s</sub> | Y<br><sub>36s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>31s</sub> | Y<br><sub>32s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>37s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>79s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>79s</sub> | N<br><sub>58s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>87s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>89s</sub> | N<br><sub>16s</sub> | T/o<br><sub>78s</sub> | N<br><sub>17s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>68s</sub> | N<br><sub>16s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>28s</sub> | Y<br><sub>26s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>44s</sub> | Y<br><sub>31s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | Y<br><sub>48s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>106s</sub> | T/o<br><sub>125s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>46s</sub> | T/o<br><sub>97s</sub> | – | N<br><sub>70s</sub> | T/o<br><sub>77s</sub> | N<br><sub>40s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>74s</sub> | N<br><sub>29s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | N<br><sub>52s</sub> | – | N<br><sub>37s</sub> | N<br><sub>46s</sub> | N<br><sub>32s</sub> | N<br><sub>36s</sub> | T/o<br><sub>65s</sub> | N<br><sub>35s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>14s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>38s</sub> | Y<br><sub>35s</sub> | Y<br><sub>15s</sub> | Y<br><sub>18s</sub> | Y<br><sub>19s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>19s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>79s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>60s</sub> | T/o<br><sub>61s</sub> | N<br><sub>33s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>82s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>84s</sub> | N<br><sub>17s</sub> | T/o<br><sub>67s</sub> | N<br><sub>18s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | N<br><sub>17s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>75s</sub> | Y<br><sub>50s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>70s</sub> | 1/9 (11%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>91s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>29s</sub> | Y<br><sub>34s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>33s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>98s</sub> | Y<br><sub>57s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>94s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>34s</sub> | – | N<br><sub>32s</sub> | T/o<br><sub>61s</sub> | N<br><sub>33s</sub> | N<br><sub>45s</sub> | T/o<br><sub>62s</sub> | N<br><sub>28s</sub> | N<br><sub>31s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>36s</sub> | N<br><sub>57s</sub> | – | N<br><sub>33s</sub> | N<br><sub>35s</sub> | N<br><sub>32s</sub> | N<br><sub>38s</sub> | N<br><sub>50s</sub> | N<br><sub>34s</sub> | N<br><sub>33s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L12) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>40s</sub> | Y<br><sub>26s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>27s</sub> | Y<br><sub>27s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>33s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>75s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>35s</sub> | T/o<br><sub>68s</sub> | N<br><sub>51s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>60s</sub> | N<br><sub>15s</sub> | T/o<br><sub>70s</sub> | N<br><sub>15s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L12) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>25s</sub> | Y<br><sub>24s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>40s</sub> | Y<br><sub>28s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | Y<br><sub>46s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>108s</sub> | T/o<br><sub>101s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>46s</sub> | T/o<br><sub>97s</sub> | – | N<br><sub>69s</sub> | T/o<br><sub>92s</sub> | N<br><sub>45s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>79s</sub> | N<br><sub>29s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>38s</sub> | N<br><sub>39s</sub> | – | N<br><sub>36s</sub> | N<br><sub>48s</sub> | N<br><sub>35s</sub> | N<br><sub>37s</sub> | T/o<br><sub>74s</sub> | N<br><sub>40s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L12) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>12s</sub> | Y<br><sub>11s</sub> | – | Y<br><sub>31s</sub> | Y<br><sub>29s</sub> | Y<br><sub>14s</sub> | Y<br><sub>15s</sub> | Y<br><sub>16s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>16s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>32s</sub> | T/o<br><sub>79s</sub> | N<br><sub>25s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>71s</sub> | N<br><sub>14s</sub> | T/o<br><sub>94s</sub> | N<br><sub>15s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>64s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>101s</sub> | T/o<br><sub>104s</sub> | – | T/o<br><sub>104s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>92s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>132s</sub> | T/o<br><sub>119s</sub> | – | T/o<br><sub>109s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>99s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>34s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>37s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>104s</sub> | Y<br><sub>60s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>94s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | N<br><sub>34s</sub> | – | N<br><sub>32s</sub> | T/o<br><sub>63s</sub> | N<br><sub>35s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | N<br><sub>27s</sub> | N<br><sub>31s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>36s</sub> | N<br><sub>57s</sub> | – | N<br><sub>33s</sub> | N<br><sub>34s</sub> | N<br><sub>33s</sub> | N<br><sub>35s</sub> | N<br><sub>53s</sub> | N<br><sub>35s</sub> | N<br><sub>35s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L23) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>40s</sub> | Y<br><sub>27s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>27s</sub> | Y<br><sub>26s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | Y<br><sub>32s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>75s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>35s</sub> | T/o<br><sub>68s</sub> | N<br><sub>49s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>103s</sub> | N<br><sub>15s</sub> | T/o<br><sub>73s</sub> | N<br><sub>14s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L23) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>39s</sub> | Y<br><sub>27s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>45s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>106s</sub> | T/o<br><sub>99s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>46s</sub> | T/o<br><sub>102s</sub> | – | N<br><sub>48s</sub> | T/o<br><sub>92s</sub> | N<br><sub>45s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | N<br><sub>29s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>41s</sub> | N<br><sub>53s</sub> | – | N<br><sub>37s</sub> | N<br><sub>48s</sub> | N<br><sub>36s</sub> | N<br><sub>41s</sub> | T/o<br><sub>68s</sub> | N<br><sub>37s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L23) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>12s</sub> | Y<br><sub>11s</sub> | – | Y<br><sub>32s</sub> | Y<br><sub>29s</sub> | Y<br><sub>14s</sub> | Y<br><sub>15s</sub> | Y<br><sub>16s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>16s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>79s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>65s</sub> | N<br><sub>33s</sub> | T/o<br><sub>81s</sub> | N<br><sub>26s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | N<br><sub>29s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>73s</sub> | N<br><sub>14s</sub> | T/o<br><sub>96s</sub> | N<br><sub>16s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>203s</sub> | N<br><sub>14s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.2s</sub> | Y<br><sub>8.9s</sub> | – | Y<br><sub>19s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.3s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>35s</sub> | Y<br><sub>9.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>68s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>90s</sub> | T/o<br><sub>82s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>29s</sub> | Y<br><sub>31s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>36s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>97s</sub> | Y<br><sub>51s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>89s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | N<br><sub>33s</sub> | – | N<br><sub>38s</sub> | T/o<br><sub>63s</sub> | N<br><sub>33s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>27s</sub> | N<br><sub>30s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | N<br><sub>57s</sub> | – | N<br><sub>34s</sub> | N<br><sub>34s</sub> | N<br><sub>33s</sub> | N<br><sub>36s</sub> | N<br><sub>51s</sub> | N<br><sub>34s</sub> | N<br><sub>34s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>52s</sub> | Y<br><sub>57s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>52s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>82s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>81s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>82s</sub> | T/o<br><sub>60s</sub> | N<br><sub>67s</sub> | N<br><sub>64s</sub> | T/o<br><sub>77s</sub> | N<br><sub>67s</sub> | N<br><sub>52s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | – | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>93s</sub> | T/o<br><sub>93s</sub> | – | T/o<br><sub>89s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>89s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>120s</sub> | T/o<br><sub>107s</sub> | – | T/o<br><sub>102s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>106s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.95) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>70s</sub> | Y<br><sub>50s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 1/9 (11%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>86s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.6s</sub> | Y<br><sub>9.3s</sub> | – | Y<br><sub>9.5s</sub> | Y<br><sub>9.3s</sub> | Y<br><sub>9.5s</sub> | Y<br><sub>9.5s</sub> | Y<br><sub>9.4s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>88s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>88s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>112s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>95s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>97s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.95) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | Y<br><sub>52s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>71s</sub> | 1/9 (11%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>84s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->!B] (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>107s</sub> | T/o<br><sub>107s</sub> | – | T/o<br><sub>102s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>100s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>140s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>118s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>149s</sub> | T/o<br><sub>139s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>129s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->B] (α=0.95) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>53s</sub> | Y<br><sub>53s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>53s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>66s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | N<br><sub>65s</sub> | N<br><sub>65s</sub> | N<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | N<br><sub>59s</sub> | N<br><sub>57s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>79s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>81s</sub> | N<br><sub>73s</sub> | N<br><sub>73s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->!B] (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>99s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>99s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>94s</sub> | T/o<br><sub>96s</sub> | – | T/o<br><sub>95s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>121s</sub> | T/o<br><sub>112s</sub> | – | T/o<br><sub>106s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>108s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->B] (α=0.95) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>52s</sub> | Y<br><sub>51s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>99s</sub> | Y<br><sub>53s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | N<br><sub>61s</sub> | T/o<br><sub>65s</sub> | N<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | N<br><sub>58s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>69s</sub> | N<br><sub>62s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>71s</sub> | N<br><sub>67s</sub> | N<br><sub>74s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->!B] (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>20s</sub> | Y<br><sub>19s</sub> | – | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>20s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>20s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>120s</sub> | T/o<br><sub>122s</sub> | – | T/o<br><sub>122s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>134s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>111s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->B] (α=0.95) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>54s</sub> | Y<br><sub>63s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>79s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>85s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->!B] (α=0.95) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>54s</sub> | Y<br><sub>62s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>78s</sub> | Y<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | N<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | N<br><sub>59s</sub> | N<br><sub>87s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->B] (α=0.95) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>52s</sub> | Y<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | N<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>83s</sub> | N<br><sub>60s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### none (baseline) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>54s</sub> | Y<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>77s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>82s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>140s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | N<br><sub>53s</sub> | – | N<br><sub>63s</sub> | T/o<br><sub>72s</sub> | N<br><sub>53s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | N<br><sub>44s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>55s</sub> | N<br><sub>84s</sub> | – | N<br><sub>50s</sub> | N<br><sub>51s</sub> | N<br><sub>50s</sub> | N<br><sub>53s</sub> | N<br><sub>63s</sub> | N<br><sub>49s</sub> | N<br><sub>49s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=6/36 (16.7%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>43s</sub> | Y<br><sub>27s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>29s</sub> | Y<br><sub>27s</sub> | Y<br><sub>50s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>32s</sub> | 6/9 (67%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | N<br><sub>32s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>100s</sub> | N<br><sub>15s</sub> | T/o<br><sub>69s</sub> | N<br><sub>14s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | N<br><sub>15s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=5/36 (13.9%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>25s</sub> | Y<br><sub>23s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>36s</sub> | Y<br><sub>26s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>39s</sub> | 5/9 (56%) |
| `0.05` | T/o<br><sub>104s</sub> | T/o<br><sub>99s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>46s</sub> | T/o<br><sub>100s</sub> | – | N<br><sub>72s</sub> | T/o<br><sub>94s</sub> | N<br><sub>45s</sub> | N<br><sub>46s</sub> | T/o<br><sub>75s</sub> | N<br><sub>30s</sub> | N<br><sub>35s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>36s</sub> | N<br><sub>53s</sub> | – | N<br><sub>38s</sub> | N<br><sub>56s</sub> | N<br><sub>36s</sub> | N<br><sub>38s</sub> | N<br><sub>63s</sub> | N<br><sub>38s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>12s</sub> | – | Y<br><sub>33s</sub> | Y<br><sub>30s</sub> | Y<br><sub>14s</sub> | Y<br><sub>16s</sub> | Y<br><sub>16s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>17s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>65s</sub> | N<br><sub>33s</sub> | T/o<br><sub>80s</sub> | N<br><sub>27s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>29s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>90s</sub> | T/o<br><sub>94s</sub> | – | T/o<br><sub>67s</sub> | N<br><sub>14s</sub> | T/o<br><sub>92s</sub> | N<br><sub>14s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>86s</sub> | N<br><sub>13s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | Y<br><sub>28s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>62s</sub> | 1/9 (11%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>71s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>24s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>24s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>132s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | N<br><sub>43s</sub> | N<br><sub>55s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>64s</sub> | N<br><sub>58s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>25s</sub> | Y<br><sub>27s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>32s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>91s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>92s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>76s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>102s</sub> | T/o<br><sub>93s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>88s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->B] (α=0.99) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>28s</sub> | Y<br><sub>28s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>83s</sub> | Y<br><sub>30s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | N<br><sub>42s</sub> | T/o<br><sub>64s</sub> | N<br><sub>40s</sub> | N<br><sub>55s</sub> | T/o<br><sub>63s</sub> | N<br><sub>41s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | N<br><sub>53s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>53s</sub> | N<br><sub>44s</sub> | N<br><sub>48s</sub> | T/o<br><sub>62s</sub> | N<br><sub>53s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->!B] (α=0.99) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>37s</sub> | Y<br><sub>46s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>75s</sub> | Y<br><sub>47s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>88s</sub> | T/o<br><sub>81s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->B] (α=0.99) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>76s</sub> | Y<br><sub>27s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>50s</sub> | N<br><sub>59s</sub> | – | N<br><sub>44s</sub> | N<br><sub>42s</sub> | N<br><sub>61s</sub> | N<br><sub>49s</sub> | T/o<br><sub>64s</sub> | N<br><sub>50s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | N<br><sub>39s</sub> | – | T/o<br><sub>66s</sub> | N<br><sub>56s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | N<br><sub>50s</sub> | T/o<br><sub>67s</sub> | N<br><sub>52s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->!B] (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>38s</sub> | Y<br><sub>8.5s</sub> | – | Y<br><sub>39s</sub> | Y<br><sub>38s</sub> | Y<br><sub>37s</sub> | Y<br><sub>8.3s</sub> | Y<br><sub>37s</sub> | T/o<br><sub>76s</sub> | Y<br><sub>38s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>62s</sub> | T/o<br><sub>76s</sub> | N<br><sub>60s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | N<br><sub>60s</sub> | N<br><sub>58s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>85s</sub> | T/o<br><sub>77s</sub> | – | N<br><sub>50s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | N<br><sub>89s</sub> | T/o<br><sub>64s</sub> | N<br><sub>73s</sub> | N<br><sub>54s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->B] (α=0.99) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>36s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>36s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>44s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>70s</sub> | N<br><sub>43s</sub> | N<br><sub>45s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->!B] (α=0.99) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>27s</sub> | Y<br><sub>31s</sub> | – | Y<br><sub>50s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>31s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>53s</sub> | T/o<br><sub>64s</sub> | – | N<br><sub>46s</sub> | N<br><sub>45s</sub> | N<br><sub>42s</sub> | N<br><sub>60s</sub> | T/o<br><sub>68s</sub> | N<br><sub>43s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | N<br><sub>39s</sub> | – | N<br><sub>47s</sub> | N<br><sub>54s</sub> | N<br><sub>48s</sub> | N<br><sub>60s</sub> | T/o<br><sub>62s</sub> | N<br><sub>51s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->B] (α=0.99) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>24s</sub> | Y<br><sub>32s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>31s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>45s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>41s</sub> | N<br><sub>40s</sub> | N<br><sub>41s</sub> | N<br><sub>54s</sub> | T/o<br><sub>64s</sub> | N<br><sub>41s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | N<br><sub>42s</sub> | – | N<br><sub>51s</sub> | N<br><sub>52s</sub> | N<br><sub>43s</sub> | N<br><sub>58s</sub> | T/o<br><sub>61s</sub> | N<br><sub>53s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |

##### none (baseline) — Y=4/36 (11.1%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>27s</sub> | Y<br><sub>35s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>36s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>104s</sub> | Y<br><sub>56s</sub> | 4/9 (44%) |
| `0.05` | T/o<br><sub>90s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>82s</sub> | N<br><sub>37s</sub> | – | N<br><sub>32s</sub> | T/o<br><sub>64s</sub> | N<br><sub>35s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | N<br><sub>28s</sub> | N<br><sub>33s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>39s</sub> | N<br><sub>63s</sub> | – | N<br><sub>36s</sub> | N<br><sub>36s</sub> | N<br><sub>33s</sub> | N<br><sub>37s</sub> | N<br><sub>53s</sub> | N<br><sub>34s</sub> | N<br><sub>35s</sub> | 0/9 (0%) |

### Class 3

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=26/36 (72.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>17s</sub> | Y<br><sub>15s</sub> | Y<br><sub>24s</sub> | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>14s</sub> | T/o<br><sub>69s</sub> | Y<br><sub>15s</sub> | – | Y<br><sub>15s</sub> | T/o<br><sub>77s</sub> | Y<br><sub>16s</sub> | T/o<br><sub>67s</sub> | Y<br><sub>14s</sub> | T/o<br><sub>77s</sub> | 5/9 (56%) |
| `0.20` | T/o<br><sub>78s</sub> | T/o<br><sub>85s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>14s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>77s</sub> | Y<br><sub>13s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>93s</sub> | T/o<br><sub>134s</sub> | T/o<br><sub>125s</sub> | – | T/o<br><sub>90s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>111s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>191s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.3s</sub> | Y<br><sub>9.3s</sub> | Y<br><sub>9.1s</sub> | – | Y<br><sub>9.0s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.0s</sub> | Y<br><sub>8.9s</sub> | Y<br><sub>8.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>100s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | – | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>11s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>103s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>98s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>186s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>93s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>94s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>110s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>7.1s</sub> | Y<br><sub>7.1s</sub> | Y<br><sub>7.0s</sub> | – | Y<br><sub>7.0s</sub> | Y<br><sub>7.0s</sub> | Y<br><sub>6.9s</sub> | Y<br><sub>7.0s</sub> | Y<br><sub>6.9s</sub> | Y<br><sub>7.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>83s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>149s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>91s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>108s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>93s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | N<br><sub>47s</sub> | – | T/o<br><sub>88s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>121s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | N<br><sub>37s</sub> | N<br><sub>36s</sub> | – | N<br><sub>38s</sub> | N<br><sub>36s</sub> | N<br><sub>43s</sub> | T/o<br><sub>61s</sub> | N<br><sub>38s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=19/36 (52.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>92s</sub> | T/o<br><sub>71s</sub> | Y<br><sub>45s</sub> | – | Y<br><sub>42s</sub> | T/o<br><sub>75s</sub> | Y<br><sub>40s</sub> | Y<br><sub>35s</sub> | T/o<br><sub>82s</sub> | Y<br><sub>35s</sub> | 5/9 (56%) |
| `0.10` | T/o<br><sub>78s</sub> | T/o<br><sub>67s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>16s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>83s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>16s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>84s</sub> | Y<br><sub>16s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>109s</sub> | – | T/o<br><sub>118s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>97s</sub> | T/o<br><sub>108s</sub> | N<br><sub>51s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>79s</sub> | N<br><sub>73s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>48s</sub> | T/o<br><sub>64s</sub> | N<br><sub>55s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>61s</sub> | N<br><sub>50s</sub> | T/o<br><sub>63s</sub> | N<br><sub>45s</sub> | N<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=28/36 (77.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>2.0s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>13s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>21s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>2.0s</sub> | Y<br><sub>24s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | T/o<br><sub>61s</sub> | 7/9 (78%) |
| `0.20` | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.9s</sub> | T/o<br><sub>71s</sub> | Y<br><sub>1.7s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>113s</sub> | 3/9 (33%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.5s</sub> | Y<br><sub>9.6s</sub> | Y<br><sub>9.5s</sub> | – | Y<br><sub>9.4s</sub> | Y<br><sub>9.5s</sub> | Y<br><sub>9.5s</sub> | Y<br><sub>9.4s</sub> | Y<br><sub>9.4s</sub> | Y<br><sub>9.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>171s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>99s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>112s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>12s</sub> | Y<br><sub>13s</sub> | Y<br><sub>12s</sub> | Y<br><sub>13s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>118s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>110s</sub> | – | T/o<br><sub>113s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>229s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>107s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>83s</sub> | T/o<br><sub>149s</sub> | T/o<br><sub>107s</sub> | – | T/o<br><sub>118s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>138s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>128s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>8.5s</sub> | Y<br><sub>8.5s</sub> | Y<br><sub>8.4s</sub> | – | Y<br><sub>8.4s</sub> | Y<br><sub>8.4s</sub> | Y<br><sub>8.4s</sub> | Y<br><sub>8.4s</sub> | Y<br><sub>8.4s</sub> | Y<br><sub>8.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>104s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>121s</sub> | – | T/o<br><sub>148s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>118s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>90s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>82s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>168s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>81s</sub> | – | T/o<br><sub>89s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>97s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>78s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | N<br><sub>56s</sub> | N<br><sub>32s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | N<br><sub>48s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>72s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | N<br><sub>25s</sub> | N<br><sub>24s</sub> | – | N<br><sub>25s</sub> | N<br><sub>24s</sub> | N<br><sub>27s</sub> | N<br><sub>54s</sub> | N<br><sub>24s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>89s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>139s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>216s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>116s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>89s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>100s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | N<br><sub>43s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>76s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>29s</sub> | N<br><sub>26s</sub> | N<br><sub>29s</sub> | – | N<br><sub>32s</sub> | N<br><sub>27s</sub> | N<br><sub>30s</sub> | N<br><sub>50s</sub> | N<br><sub>30s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>87s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>97s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>104s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>81s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>89s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>6.8s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.5s</sub> | – | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>103s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>93s</sub> | – | T/o<br><sub>92s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>116s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>86s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>92s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>117s</sub> | – | T/o<br><sub>110s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>184s</sub> | T/o<br><sub>94s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>115s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>105s</sub> | – | T/o<br><sub>110s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>220s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>104s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>81s</sub> | T/o<br><sub>146s</sub> | T/o<br><sub>103s</sub> | – | T/o<br><sub>119s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>138s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>128s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>7.7s</sub> | Y<br><sub>7.8s</sub> | Y<br><sub>7.7s</sub> | – | Y<br><sub>7.7s</sub> | Y<br><sub>7.7s</sub> | Y<br><sub>7.5s</sub> | Y<br><sub>7.5s</sub> | Y<br><sub>7.6s</sub> | Y<br><sub>7.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>88s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>103s</sub> | – | T/o<br><sub>128s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>101s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>82s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>156s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>94s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>80s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | N<br><sub>58s</sub> | N<br><sub>33s</sub> | – | T/o<br><sub>82s</sub> | T/o<br><sub>69s</sub> | N<br><sub>35s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>73s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>25s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | – | N<br><sub>25s</sub> | N<br><sub>24s</sub> | N<br><sub>31s</sub> | N<br><sub>54s</sub> | N<br><sub>25s</sub> | N<br><sub>24s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=26/36 (72.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>2.3s</sub> | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | Y<br><sub>25s</sub> | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>14s</sub> | T/o<br><sub>73s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>15s</sub> | T/o<br><sub>82s</sub> | Y<br><sub>15s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>14s</sub> | T/o<br><sub>76s</sub> | 5/9 (56%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>84s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>14s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>73s</sub> | Y<br><sub>13s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>77s</sub> | T/o<br><sub>135s</sub> | T/o<br><sub>125s</sub> | – | T/o<br><sub>101s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>113s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.1s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>8.8s</sub> | – | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>8.9s</sub> | Y<br><sub>9.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>96s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>116s</sub> | – | T/o<br><sub>114s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>77s</sub> | T/o<br><sub>69s</sub> | N<br><sub>51s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>83s</sub> | N<br><sub>78s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>117s</sub> | N<br><sub>40s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | N<br><sub>38s</sub> | N<br><sub>37s</sub> | – | N<br><sub>39s</sub> | N<br><sub>36s</sub> | N<br><sub>42s</sub> | T/o<br><sub>61s</sub> | N<br><sub>37s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L12) — Y=26/36 (72.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>16s</sub> | Y<br><sub>14s</sub> | Y<br><sub>22s</sub> | Y<br><sub>16s</sub> | Y<br><sub>16s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>13s</sub> | T/o<br><sub>69s</sub> | Y<br><sub>15s</sub> | – | Y<br><sub>15s</sub> | T/o<br><sub>77s</sub> | Y<br><sub>15s</sub> | T/o<br><sub>64s</sub> | Y<br><sub>14s</sub> | T/o<br><sub>76s</sub> | 5/9 (56%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>83s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>14s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | Y<br><sub>13s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.9) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>90s</sub> | T/o<br><sub>135s</sub> | T/o<br><sub>128s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>109s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>192s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.9) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | – | Y<br><sub>10s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>102s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>111s</sub> | – | T/o<br><sub>94s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>162s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>89s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>95s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>116s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>113s</sub> | – | T/o<br><sub>112s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>76s</sub> | T/o<br><sub>70s</sub> | N<br><sub>49s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>85s</sub> | N<br><sub>76s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>121s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | N<br><sub>36s</sub> | N<br><sub>37s</sub> | – | N<br><sub>38s</sub> | N<br><sub>37s</sub> | N<br><sub>43s</sub> | T/o<br><sub>61s</sub> | N<br><sub>39s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L23) — Y=26/36 (72.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>15s</sub> | Y<br><sub>14s</sub> | Y<br><sub>21s</sub> | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>13s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>13s</sub> | T/o<br><sub>71s</sub> | Y<br><sub>14s</sub> | T/o<br><sub>75s</sub> | Y<br><sub>13s</sub> | T/o<br><sub>60s</sub> | 5/9 (56%) |
| `0.20` | T/o<br><sub>75s</sub> | T/o<br><sub>78s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>13s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>12s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.9) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>88s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>125s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>184s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.9) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>7.1s</sub> | Y<br><sub>7.2s</sub> | Y<br><sub>7.1s</sub> | – | Y<br><sub>7.2s</sub> | Y<br><sub>7.2s</sub> | Y<br><sub>7.2s</sub> | Y<br><sub>7.1s</sub> | Y<br><sub>7.2s</sub> | Y<br><sub>7.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>83s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>150s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>88s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.1s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>114s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>114s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>75s</sub> | N<br><sub>48s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | N<br><sub>79s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>118s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>37s</sub> | N<br><sub>38s</sub> | N<br><sub>37s</sub> | – | N<br><sub>39s</sub> | N<br><sub>36s</sub> | N<br><sub>43s</sub> | T/o<br><sub>62s</sub> | N<br><sub>36s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=19/36 (52.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>99s</sub> | T/o<br><sub>77s</sub> | Y<br><sub>49s</sub> | – | Y<br><sub>45s</sub> | T/o<br><sub>81s</sub> | Y<br><sub>44s</sub> | Y<br><sub>38s</sub> | T/o<br><sub>89s</sub> | Y<br><sub>38s</sub> | 5/9 (56%) |
| `0.10` | T/o<br><sub>85s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>15s</sub> | – | Y<br><sub>17s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>72s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>90s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>17s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>137s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>92s</sub> | Y<br><sub>17s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>121s</sub> | – | T/o<br><sub>130s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>107s</sub> | T/o<br><sub>74s</sub> | N<br><sub>56s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>53s</sub> | T/o<br><sub>61s</sub> | N<br><sub>47s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>66s</sub> | N<br><sub>55s</sub> | T/o<br><sub>64s</sub> | N<br><sub>50s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=28/36 (77.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>14s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>23s</sub> | T/o<br><sub>81s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>26s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | T/o<br><sub>62s</sub> | 7/9 (78%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>113s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>2.2s</sub> | T/o<br><sub>77s</sub> | Y<br><sub>1.8s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>77s</sub> | 3/9 (33%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10.0s</sub> | – | Y<br><sub>10s</sub> | Y<br><sub>9.9s</sub> | Y<br><sub>10.0s</sub> | Y<br><sub>9.8s</sub> | Y<br><sub>9.9s</sub> | Y<br><sub>10.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>97s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>112s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | N<br><sub>60s</sub> | N<br><sub>34s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | N<br><sub>50s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>76s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | N<br><sub>31s</sub> | N<br><sub>26s</sub> | – | N<br><sub>27s</sub> | N<br><sub>26s</sub> | N<br><sub>29s</sub> | N<br><sub>57s</sub> | N<br><sub>26s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L12) — Y=19/36 (52.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>94s</sub> | T/o<br><sub>73s</sub> | Y<br><sub>47s</sub> | – | Y<br><sub>44s</sub> | T/o<br><sub>77s</sub> | Y<br><sub>42s</sub> | Y<br><sub>37s</sub> | T/o<br><sub>86s</sub> | Y<br><sub>36s</sub> | 5/9 (56%) |
| `0.10` | T/o<br><sub>82s</sub> | T/o<br><sub>61s</sub> | Y<br><sub>15s</sub> | – | Y<br><sub>17s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>77s</sub> | T/o<br><sub>86s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>17s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>93s</sub> | Y<br><sub>18s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.95) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>127s</sub> | – | T/o<br><sub>138s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>116s</sub> | T/o<br><sub>62s</sub> | N<br><sub>60s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>54s</sub> | T/o<br><sub>62s</sub> | N<br><sub>55s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | N<br><sub>57s</sub> | T/o<br><sub>63s</sub> | N<br><sub>57s</sub> | N<br><sub>57s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L12) — Y=28/36 (77.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>2.1s</sub> | Y<br><sub>14s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>23s</sub> | T/o<br><sub>84s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>27s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>20s</sub> | Y<br><sub>20s</sub> | T/o<br><sub>61s</sub> | 7/9 (78%) |
| `0.20` | T/o<br><sub>79s</sub> | T/o<br><sub>68s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>2.2s</sub> | T/o<br><sub>79s</sub> | Y<br><sub>1.9s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>78s</sub> | 3/9 (33%) |

##### Impl L1→L2 (α=0.95) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>123s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>113s</sub> | – | T/o<br><sub>117s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>229s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>107s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>84s</sub> | T/o<br><sub>151s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>116s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>137s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>128s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | N<br><sub>57s</sub> | N<br><sub>33s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | N<br><sub>48s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>72s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>24s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | – | N<br><sub>25s</sub> | N<br><sub>24s</sub> | N<br><sub>28s</sub> | N<br><sub>54s</sub> | N<br><sub>25s</sub> | N<br><sub>25s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L23) — Y=19/36 (52.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>96s</sub> | T/o<br><sub>75s</sub> | Y<br><sub>47s</sub> | – | Y<br><sub>44s</sub> | T/o<br><sub>80s</sub> | Y<br><sub>43s</sub> | Y<br><sub>37s</sub> | T/o<br><sub>87s</sub> | Y<br><sub>37s</sub> | 5/9 (56%) |
| `0.10` | T/o<br><sub>91s</sub> | T/o<br><sub>60s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>18s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>62s</sub> | 2/9 (22%) |
| `0.20` | T/o<br><sub>83s</sub> | T/o<br><sub>92s</sub> | Y<br><sub>18s</sub> | – | Y<br><sub>18s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>143s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>94s</sub> | Y<br><sub>18s</sub> | 3/9 (33%) |

##### ALWAYS_ON (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>127s</sub> | – | T/o<br><sub>137s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>114s</sub> | T/o<br><sub>62s</sub> | N<br><sub>59s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>55s</sub> | T/o<br><sub>65s</sub> | N<br><sub>53s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>69s</sub> | N<br><sub>57s</sub> | T/o<br><sub>73s</sub> | N<br><sub>52s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L23) — Y=28/36 (77.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>14s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>23s</sub> | T/o<br><sub>84s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>2.2s</sub> | Y<br><sub>27s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>20s</sub> | Y<br><sub>20s</sub> | T/o<br><sub>62s</sub> | 7/9 (78%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>69s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>2.2s</sub> | T/o<br><sub>80s</sub> | Y<br><sub>1.9s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>96s</sub> | 3/9 (33%) |

##### Impl L2→L3 (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.0s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.1s</sub> | – | Y<br><sub>9.1s</sub> | Y<br><sub>9.1s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.0s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>8.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>94s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>89s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>178s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>106s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>91s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>89s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>51s</sub> | T/o<br><sub>62s</sub> | N<br><sub>37s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | N<br><sub>57s</sub> | N<br><sub>66s</sub> | T/o<br><sub>86s</sub> | N<br><sub>30s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>28s</sub> | N<br><sub>31s</sub> | N<br><sub>28s</sub> | – | N<br><sub>29s</sub> | N<br><sub>28s</sub> | N<br><sub>32s</sub> | T/o<br><sub>64s</sub> | N<br><sub>29s</sub> | N<br><sub>28s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>92s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>230s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>84s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>95s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>106s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>47s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>72s</sub> | N<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>84s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>30s</sub> | N<br><sub>27s</sub> | N<br><sub>30s</sub> | – | N<br><sub>35s</sub> | N<br><sub>29s</sub> | N<br><sub>32s</sub> | T/o<br><sub>10501s</sub> | N<br><sub>56s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>153s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>126s</sub> | – | T/o<br><sub>292s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>98s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>89s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>7.1s</sub> | Y<br><sub>6.8s</sub> | Y<br><sub>6.8s</sub> | – | Y<br><sub>6.9s</sub> | Y<br><sub>6.8s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>106s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>112s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>102s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>82s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>144s</sub> | – | T/o<br><sub>137s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>138s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>86s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | N<br><sub>63s</sub> | N<br><sub>35s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>87s</sub> | N<br><sub>53s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>81s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>26s</sub> | N<br><sub>28s</sub> | N<br><sub>26s</sub> | – | N<br><sub>28s</sub> | N<br><sub>26s</sub> | N<br><sub>28s</sub> | T/o<br><sub>61s</sub> | N<br><sub>26s</sub> | N<br><sub>26s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>77s</sub> | T/o<br><sub>141s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>107s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>126s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>188s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>256s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>100s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>70s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>153s</sub> | T/o<br><sub>67s</sub> | N<br><sub>62s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>64s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>39s</sub> | N<br><sub>35s</sub> | N<br><sub>43s</sub> | – | N<br><sub>46s</sub> | N<br><sub>39s</sub> | N<br><sub>43s</sub> | T/o<br><sub>12908s</sub> | N<br><sub>41s</sub> | N<br><sub>40s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>94s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>107s</sub> | – | T/o<br><sub>91s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>110s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>226s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>13s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>130s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>122s</sub> | – | T/o<br><sub>129s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>244s</sub> | T/o<br><sub>150s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>121s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>121s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>139s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>110s</sub> | – | T/o<br><sub>106s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>77s</sub> | N<br><sub>53s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>94s</sub> | N<br><sub>85s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>66s</sub> | N<br><sub>46s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>43s</sub> | N<br><sub>41s</sub> | N<br><sub>46s</sub> | – | N<br><sub>44s</sub> | N<br><sub>46s</sub> | N<br><sub>48s</sub> | T/o<br><sub>63s</sub> | N<br><sub>47s</sub> | N<br><sub>40s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>88s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>103s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>160s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>253s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>93s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>80s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | N<br><sub>52s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | N<br><sub>44s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>35s</sub> | N<br><sub>36s</sub> | N<br><sub>34s</sub> | – | N<br><sub>44s</sub> | N<br><sub>33s</sub> | N<br><sub>43s</sub> | T/o<br><sub>12174s</sub> | N<br><sub>45s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>87s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>110s</sub> | – | T/o<br><sub>91s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>113s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>246s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>8.0s</sub> | Y<br><sub>8.3s</sub> | Y<br><sub>8.2s</sub> | – | Y<br><sub>8.2s</sub> | Y<br><sub>8.2s</sub> | Y<br><sub>8.1s</sub> | Y<br><sub>8.3s</sub> | Y<br><sub>8.1s</sub> | Y<br><sub>8.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>97s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>118s</sub> | – | T/o<br><sub>145s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>100s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>96s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>88s</sub> | – | T/o<br><sub>93s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>180s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>87s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>75s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>98s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>108s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>74s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>113s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>75s</sub> | T/o<br><sub>70s</sub> | N<br><sub>44s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>78s</sub> | N<br><sub>71s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>112s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>35s</sub> | N<br><sub>35s</sub> | N<br><sub>37s</sub> | – | N<br><sub>35s</sub> | N<br><sub>33s</sub> | N<br><sub>40s</sub> | T/o<br><sub>72s</sub> | N<br><sub>37s</sub> | N<br><sub>34s</sub> | 0/9 (0%) |

### Class 4

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>114s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>89s</sub> | – | T/o<br><sub>98s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>98s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>81s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>105s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>127s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>111s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>105s</sub> | – | T/o<br><sub>104s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>105s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>88s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>50s</sub> | N<br><sub>52s</sub> | N<br><sub>45s</sub> | N<br><sub>55s</sub> | – | N<br><sub>54s</sub> | N<br><sub>50s</sub> | N<br><sub>53s</sub> | N<br><sub>59s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>39s</sub> | N<br><sub>41s</sub> | N<br><sub>38s</sub> | N<br><sub>38s</sub> | – | N<br><sub>38s</sub> | N<br><sub>38s</sub> | N<br><sub>38s</sub> | N<br><sub>43s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>47s</sub> | N<br><sub>47s</sub> | N<br><sub>48s</sub> | N<br><sub>48s</sub> | – | N<br><sub>42s</sub> | N<br><sub>49s</sub> | N<br><sub>47s</sub> | N<br><sub>46s</sub> | N<br><sub>46s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>73s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>97s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>175s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>95s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>143s</sub> | T/o<br><sub>90s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>115s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>110s</sub> | – | T/o<br><sub>105s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>147s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>110s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>123s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>101s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>152s</sub> | T/o<br><sub>135s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>128s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>143s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>137s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>135s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>141s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>108s</sub> | – | T/o<br><sub>119s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>138s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>106s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>99s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>97s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>90s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>30454s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>47s</sub> | N<br><sub>50s</sub> | N<br><sub>46s</sub> | N<br><sub>52s</sub> | – | N<br><sub>51s</sub> | N<br><sub>47s</sub> | N<br><sub>46s</sub> | N<br><sub>47s</sub> | N<br><sub>53s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>36s</sub> | N<br><sub>39s</sub> | N<br><sub>36s</sub> | N<br><sub>37s</sub> | – | N<br><sub>35s</sub> | N<br><sub>35s</sub> | N<br><sub>36s</sub> | N<br><sub>39s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>42s</sub> | N<br><sub>35s</sub> | N<br><sub>37s</sub> | N<br><sub>38s</sub> | – | N<br><sub>37s</sub> | N<br><sub>39s</sub> | N<br><sub>38s</sub> | N<br><sub>39s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>48s</sub> | N<br><sub>49s</sub> | N<br><sub>45s</sub> | N<br><sub>44s</sub> | – | N<br><sub>46s</sub> | N<br><sub>42s</sub> | N<br><sub>42s</sub> | N<br><sub>47s</sub> | N<br><sub>43s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>40s</sub> | N<br><sub>35s</sub> | N<br><sub>43s</sub> | N<br><sub>40s</sub> | – | N<br><sub>41s</sub> | N<br><sub>40s</sub> | N<br><sub>50s</sub> | N<br><sub>40s</sub> | N<br><sub>41s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>58s</sub> | N<br><sub>47s</sub> | N<br><sub>54s</sub> | N<br><sub>40s</sub> | – | N<br><sub>61s</sub> | N<br><sub>42s</sub> | N<br><sub>45s</sub> | N<br><sub>40s</sub> | N<br><sub>43s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>112s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>105s</sub> | – | T/o<br><sub>101s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>98s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>103s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>102s</sub> | – | T/o<br><sub>87s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>77s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>18699s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>108s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>102s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>103s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>87s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>83s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>89s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>100s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>91s</sub> | – | T/o<br><sub>101s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>114s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>89s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>82s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>18752s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>107s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>46s</sub> | N<br><sub>49s</sub> | N<br><sub>42s</sub> | N<br><sub>50s</sub> | – | N<br><sub>49s</sub> | N<br><sub>44s</sub> | N<br><sub>51s</sub> | N<br><sub>52s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>40s</sub> | N<br><sub>44s</sub> | N<br><sub>40s</sub> | N<br><sub>40s</sub> | – | N<br><sub>40s</sub> | N<br><sub>41s</sub> | N<br><sub>40s</sub> | N<br><sub>45s</sub> | N<br><sub>40s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>50s</sub> | N<br><sub>49s</sub> | N<br><sub>50s</sub> | N<br><sub>50s</sub> | – | N<br><sub>45s</sub> | N<br><sub>51s</sub> | N<br><sub>49s</sub> | N<br><sub>48s</sub> | N<br><sub>49s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>97s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>100s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>126s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>52s</sub> | N<br><sub>55s</sub> | N<br><sub>49s</sub> | N<br><sub>57s</sub> | – | N<br><sub>55s</sub> | N<br><sub>49s</sub> | N<br><sub>51s</sub> | N<br><sub>52s</sub> | N<br><sub>58s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>39s</sub> | N<br><sub>43s</sub> | N<br><sub>39s</sub> | N<br><sub>41s</sub> | – | N<br><sub>39s</sub> | N<br><sub>40s</sub> | N<br><sub>39s</sub> | N<br><sub>43s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>47s</sub> | N<br><sub>47s</sub> | N<br><sub>48s</sub> | N<br><sub>49s</sub> | – | N<br><sub>44s</sub> | N<br><sub>49s</sub> | N<br><sub>47s</sub> | N<br><sub>47s</sub> | N<br><sub>47s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>78s</sub> | T/o<br><sub>216s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>89s</sub> | – | T/o<br><sub>100s</sub> | T/o<br><sub>198s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>99s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>85s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.9) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>51s</sub> | N<br><sub>54s</sub> | N<br><sub>48s</sub> | N<br><sub>52s</sub> | – | N<br><sub>55s</sub> | N<br><sub>50s</sub> | N<br><sub>53s</sub> | N<br><sub>53s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>40s</sub> | N<br><sub>44s</sub> | N<br><sub>39s</sub> | N<br><sub>40s</sub> | – | N<br><sub>40s</sub> | N<br><sub>40s</sub> | N<br><sub>40s</sub> | N<br><sub>44s</sub> | N<br><sub>40s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>48s</sub> | N<br><sub>48s</sub> | N<br><sub>49s</sub> | N<br><sub>49s</sub> | – | N<br><sub>45s</sub> | N<br><sub>50s</sub> | N<br><sub>49s</sub> | N<br><sub>49s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>170s</sub> | T/o<br><sub>137s</sub> | T/o<br><sub>211s</sub> | T/o<br><sub>128s</sub> | – | T/o<br><sub>143s</sub> | T/o<br><sub>162s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>160s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.9) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>60s</sub> | N<br><sub>74s</sub> | N<br><sub>66s</sub> | N<br><sub>77s</sub> | – | T/o<br><sub>61s</sub> | N<br><sub>67s</sub> | N<br><sub>71s</sub> | N<br><sub>72s</sub> | N<br><sub>81s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>55s</sub> | N<br><sub>61s</sub> | N<br><sub>56s</sub> | N<br><sub>57s</sub> | – | N<br><sub>55s</sub> | N<br><sub>56s</sub> | N<br><sub>57s</sub> | N<br><sub>62s</sub> | N<br><sub>56s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>95s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>124s</sub> | – | T/o<br><sub>98s</sub> | T/o<br><sub>177s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>110s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>204s</sub> | T/o<br><sub>135s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>119s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>136s</sub> | T/o<br><sub>184s</sub> | T/o<br><sub>109s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>77s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>154s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>128s</sub> | T/o<br><sub>187s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>109s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>82s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>108s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>128s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>53s</sub> | N<br><sub>58s</sub> | N<br><sub>51s</sub> | N<br><sub>64s</sub> | – | N<br><sub>66s</sub> | N<br><sub>57s</sub> | N<br><sub>59s</sub> | N<br><sub>60s</sub> | N<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>47s</sub> | N<br><sub>48s</sub> | N<br><sub>46s</sub> | N<br><sub>46s</sub> | – | N<br><sub>46s</sub> | N<br><sub>47s</sub> | N<br><sub>45s</sub> | N<br><sub>51s</sub> | N<br><sub>46s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>55s</sub> | N<br><sub>55s</sub> | N<br><sub>58s</sub> | N<br><sub>56s</sub> | – | N<br><sub>51s</sub> | N<br><sub>57s</sub> | N<br><sub>54s</sub> | N<br><sub>54s</sub> | N<br><sub>54s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>98s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>122s</sub> | – | T/o<br><sub>96s</sub> | T/o<br><sub>176s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>114s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>205s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>82s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>169s</sub> | T/o<br><sub>107s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>140s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>137s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>88s</sub> | T/o<br><sub>184s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>107s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.95) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>47s</sub> | N<br><sub>52s</sub> | N<br><sub>46s</sub> | N<br><sub>62s</sub> | – | N<br><sub>52s</sub> | N<br><sub>44s</sub> | N<br><sub>52s</sub> | N<br><sub>49s</sub> | N<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>45s</sub> | N<br><sub>47s</sub> | N<br><sub>39s</sub> | N<br><sub>44s</sub> | – | N<br><sub>36s</sub> | N<br><sub>46s</sub> | N<br><sub>36s</sub> | N<br><sub>36s</sub> | N<br><sub>45s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>52s</sub> | N<br><sub>53s</sub> | N<br><sub>55s</sub> | N<br><sub>55s</sub> | – | N<br><sub>48s</sub> | N<br><sub>55s</sub> | N<br><sub>53s</sub> | N<br><sub>53s</sub> | N<br><sub>53s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>86s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>95s</sub> | – | T/o<br><sub>92s</sub> | T/o<br><sub>163s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>107s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>199s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>175s</sub> | T/o<br><sub>106s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>145s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>139s</sub> | – | T/o<br><sub>136s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>140s</sub> | T/o<br><sub>154s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>91s</sub> | T/o<br><sub>194s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>102s</sub> | – | T/o<br><sub>113s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.95) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>124s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>148s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>121s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>116s</sub> | – | T/o<br><sub>116s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>115s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>54s</sub> | N<br><sub>52s</sub> | N<br><sub>44s</sub> | N<br><sub>53s</sub> | – | N<br><sub>53s</sub> | N<br><sub>47s</sub> | N<br><sub>52s</sub> | N<br><sub>51s</sub> | N<br><sub>54s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>43s</sub> | N<br><sub>46s</sub> | N<br><sub>42s</sub> | N<br><sub>42s</sub> | – | N<br><sub>40s</sub> | N<br><sub>41s</sub> | N<br><sub>42s</sub> | N<br><sub>45s</sub> | N<br><sub>41s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>49s</sub> | N<br><sub>49s</sub> | N<br><sub>48s</sub> | N<br><sub>47s</sub> | – | N<br><sub>43s</sub> | N<br><sub>51s</sub> | N<br><sub>49s</sub> | N<br><sub>46s</sub> | N<br><sub>47s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>45s</sub> | N<br><sub>49s</sub> | N<br><sub>44s</sub> | N<br><sub>43s</sub> | – | N<br><sub>47s</sub> | N<br><sub>42s</sub> | N<br><sub>42s</sub> | N<br><sub>46s</sub> | N<br><sub>41s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>40s</sub> | N<br><sub>35s</sub> | N<br><sub>43s</sub> | N<br><sub>39s</sub> | – | N<br><sub>41s</sub> | N<br><sub>39s</sub> | N<br><sub>46s</sub> | N<br><sub>40s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>57s</sub> | N<br><sub>48s</sub> | N<br><sub>54s</sub> | N<br><sub>46s</sub> | – | N<br><sub>57s</sub> | N<br><sub>48s</sub> | N<br><sub>44s</sub> | N<br><sub>40s</sub> | N<br><sub>45s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>113s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>107s</sub> | – | T/o<br><sub>102s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>93s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>106s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>102s</sub> | – | T/o<br><sub>90s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>16618s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>54s</sub> | N<br><sub>53s</sub> | N<br><sub>49s</sub> | N<br><sub>56s</sub> | – | N<br><sub>56s</sub> | N<br><sub>50s</sub> | N<br><sub>51s</sub> | N<br><sub>52s</sub> | N<br><sub>58s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>40s</sub> | N<br><sub>43s</sub> | N<br><sub>41s</sub> | N<br><sub>41s</sub> | – | N<br><sub>40s</sub> | N<br><sub>41s</sub> | N<br><sub>41s</sub> | N<br><sub>46s</sub> | N<br><sub>40s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>49s</sub> | N<br><sub>48s</sub> | N<br><sub>50s</sub> | N<br><sub>51s</sub> | – | N<br><sub>45s</sub> | T/o<br><sub>79s</sub> | N<br><sub>49s</sub> | N<br><sub>49s</sub> | N<br><sub>48s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>40s</sub> | N<br><sub>42s</sub> | N<br><sub>38s</sub> | N<br><sub>38s</sub> | – | N<br><sub>41s</sub> | N<br><sub>37s</sub> | N<br><sub>36s</sub> | N<br><sub>41s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>35s</sub> | N<br><sub>31s</sub> | N<br><sub>38s</sub> | N<br><sub>36s</sub> | – | N<br><sub>36s</sub> | N<br><sub>35s</sub> | N<br><sub>39s</sub> | N<br><sub>35s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>50s</sub> | N<br><sub>42s</sub> | N<br><sub>47s</sub> | N<br><sub>39s</sub> | – | N<br><sub>53s</sub> | N<br><sub>45s</sub> | N<br><sub>39s</sub> | N<br><sub>35s</sub> | N<br><sub>39s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>105s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>102s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>102s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>94s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>87s</sub> | T/o<br><sub>138s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>96s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>45s</sub> | N<br><sub>47s</sub> | N<br><sub>42s</sub> | N<br><sub>50s</sub> | – | N<br><sub>50s</sub> | N<br><sub>43s</sub> | N<br><sub>46s</sub> | N<br><sub>43s</sub> | N<br><sub>58s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>35s</sub> | N<br><sub>38s</sub> | N<br><sub>36s</sub> | N<br><sub>36s</sub> | – | N<br><sub>36s</sub> | N<br><sub>36s</sub> | N<br><sub>36s</sub> | N<br><sub>41s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>42s</sub> | N<br><sub>44s</sub> | N<br><sub>45s</sub> | N<br><sub>45s</sub> | – | N<br><sub>40s</sub> | N<br><sub>45s</sub> | N<br><sub>44s</sub> | N<br><sub>43s</sub> | N<br><sub>43s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>39s</sub> | N<br><sub>42s</sub> | N<br><sub>37s</sub> | N<br><sub>36s</sub> | – | N<br><sub>39s</sub> | N<br><sub>36s</sub> | N<br><sub>36s</sub> | N<br><sub>39s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>34s</sub> | N<br><sub>31s</sub> | N<br><sub>38s</sub> | N<br><sub>34s</sub> | – | N<br><sub>36s</sub> | N<br><sub>34s</sub> | N<br><sub>38s</sub> | N<br><sub>35s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>51s</sub> | N<br><sub>42s</sub> | N<br><sub>47s</sub> | N<br><sub>37s</sub> | – | N<br><sub>52s</sub> | N<br><sub>46s</sub> | N<br><sub>39s</sub> | N<br><sub>35s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>75s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>81s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>93s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>94s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>107s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>75s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>18371s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.05` | N<br><sub>46s</sub> | N<br><sub>46s</sub> | N<br><sub>44s</sub> | N<br><sub>49s</sub> | – | N<br><sub>47s</sub> | N<br><sub>42s</sub> | N<br><sub>45s</sub> | N<br><sub>46s</sub> | N<br><sub>54s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>36s</sub> | N<br><sub>39s</sub> | N<br><sub>35s</sub> | N<br><sub>38s</sub> | – | N<br><sub>35s</sub> | N<br><sub>35s</sub> | N<br><sub>36s</sub> | N<br><sub>40s</sub> | N<br><sub>36s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>43s</sub> | N<br><sub>42s</sub> | N<br><sub>44s</sub> | N<br><sub>43s</sub> | – | N<br><sub>40s</sub> | N<br><sub>44s</sub> | N<br><sub>43s</sub> | N<br><sub>43s</sub> | N<br><sub>44s</sub> | 0/9 (0%) |

### Class 5

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | Y<br><sub>4.0s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>81s</sub> | – | T/o<br><sub>77s</sub> | Y<br><sub>3.9s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>39s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>94s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>70s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | – | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>148s</sub> | – | T/o<br><sub>157s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>17s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>168s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>113s</sub> | – | T/o<br><sub>99s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>97s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>105s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>102s</sub> | – | T/o<br><sub>104s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>103s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>143s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>95s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>103s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>86s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>95s</sub> | T/o<br><sub>69s</sub> | N<br><sub>49s</sub> | N<br><sub>47s</sub> | T/o<br><sub>99s</sub> | – | N<br><sub>50s</sub> | N<br><sub>49s</sub> | T/o<br><sub>104s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>73s</sub> | N<br><sub>43s</sub> | T/o<br><sub>65s</sub> | – | N<br><sub>52s</sub> | N<br><sub>81s</sub> | N<br><sub>44s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | Y<br><sub>6.0s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | Y<br><sub>6.0s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>106s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>164s</sub> | – | T/o<br><sub>91s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>97s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | – | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | – | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | Y<br><sub>25s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>89s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>161s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>137s</sub> | T/o<br><sub>78s</sub> | N<br><sub>74s</sub> | N<br><sub>70s</sub> | T/o<br><sub>86s</sub> | – | N<br><sub>75s</sub> | N<br><sub>75s</sub> | T/o<br><sub>151s</sub> | N<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>100s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>107s</sub> | N<br><sub>62s</sub> | T/o<br><sub>91s</sub> | – | T/o<br><sub>85s</sub> | N<br><sub>114s</sub> | N<br><sub>61s</sub> | N<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>137s</sub> | – | T/o<br><sub>82s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | N<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>79s</sub> | – | N<br><sub>80s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>20s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | – | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>23s</sub> | Y<br><sub>24s</sub> | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | Y<br><sub>24s</sub> | – | Y<br><sub>23s</sub> | Y<br><sub>23s</sub> | Y<br><sub>24s</sub> | Y<br><sub>23s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>155s</sub> | T/o<br><sub>101s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>132s</sub> | T/o<br><sub>74s</sub> | N<br><sub>71s</sub> | N<br><sub>68s</sub> | T/o<br><sub>82s</sub> | – | N<br><sub>73s</sub> | N<br><sub>73s</sub> | T/o<br><sub>147s</sub> | N<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>100s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>106s</sub> | N<br><sub>61s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>85s</sub> | N<br><sub>114s</sub> | N<br><sub>61s</sub> | N<br><sub>60s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | Y<br><sub>4.2s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>93s</sub> | – | T/o<br><sub>62s</sub> | Y<br><sub>4.2s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>44s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>110s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>128s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>95s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | – | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>10s</sub> | Y<br><sub>11s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>113s</sub> | T/o<br><sub>131s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>162s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>83s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>91s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>97s</sub> | T/o<br><sub>68s</sub> | N<br><sub>51s</sub> | N<br><sub>47s</sub> | T/o<br><sub>96s</sub> | – | N<br><sub>52s</sub> | N<br><sub>48s</sub> | T/o<br><sub>106s</sub> | N<br><sub>53s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>72s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>76s</sub> | N<br><sub>43s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>79s</sub> | N<br><sub>56s</sub> | N<br><sub>43s</sub> | N<br><sub>43s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L12) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | Y<br><sub>3.7s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>67s</sub> | Y<br><sub>3.8s</sub> | T/o<br><sub>67s</sub> | Y<br><sub>37s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>89s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.9) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>151s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>123s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>79s</sub> | T/o<br><sub>77s</sub> | N<br><sub>42s</sub> | N<br><sub>40s</sub> | T/o<br><sub>82s</sub> | – | N<br><sub>44s</sub> | N<br><sub>44s</sub> | T/o<br><sub>88s</sub> | N<br><sub>44s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | N<br><sub>37s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>86s</sub> | N<br><sub>42s</sub> | N<br><sub>36s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L23) — Y=3/36 (8.3%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | Y<br><sub>3.6s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>68s</sub> | Y<br><sub>3.7s</sub> | T/o<br><sub>67s</sub> | Y<br><sub>37s</sub> | 3/9 (33%) |
| `0.05` | T/o<br><sub>89s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>111s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>81s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>172s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>85s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>90s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.9) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>15s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>17s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>171s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>119s</sub> | – | T/o<br><sub>102s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>99s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>108s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>108s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>93s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>149s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>137s</sub> | T/o<br><sub>97s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>102s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>88s</sub> | T/o<br><sub>61s</sub> | N<br><sub>41s</sub> | N<br><sub>36s</sub> | T/o<br><sub>82s</sub> | – | N<br><sub>49s</sub> | N<br><sub>39s</sub> | T/o<br><sub>89s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | N<br><sub>37s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>67s</sub> | N<br><sub>67s</sub> | N<br><sub>34s</sub> | N<br><sub>34s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | Y<br><sub>6.2s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | Y<br><sub>6.1s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>108s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>169s</sub> | – | T/o<br><sub>94s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>88s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | – | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | Y<br><sub>11s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>88s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>160s</sub> | T/o<br><sub>105s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>136s</sub> | T/o<br><sub>77s</sub> | N<br><sub>73s</sub> | N<br><sub>69s</sub> | T/o<br><sub>85s</sub> | – | N<br><sub>75s</sub> | N<br><sub>75s</sub> | T/o<br><sub>150s</sub> | N<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>101s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>107s</sub> | N<br><sub>62s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>86s</sub> | N<br><sub>116s</sub> | N<br><sub>62s</sub> | N<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L12) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | Y<br><sub>6.1s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | Y<br><sub>6.1s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>104s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>168s</sub> | – | T/o<br><sub>94s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>95s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.95) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>78s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>160s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>137s</sub> | T/o<br><sub>77s</sub> | N<br><sub>78s</sub> | N<br><sub>70s</sub> | T/o<br><sub>85s</sub> | – | N<br><sub>75s</sub> | N<br><sub>75s</sub> | T/o<br><sub>149s</sub> | N<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>100s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>107s</sub> | N<br><sub>61s</sub> | T/o<br><sub>91s</sub> | – | T/o<br><sub>86s</sub> | N<br><sub>114s</sub> | N<br><sub>61s</sub> | N<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L23) — Y=2/36 (5.6%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | Y<br><sub>6.1s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | Y<br><sub>6.2s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 2/9 (22%) |
| `0.05` | T/o<br><sub>108s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>105s</sub> | T/o<br><sub>170s</sub> | – | T/o<br><sub>93s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>87s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | – | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | Y<br><sub>26s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>90s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>162s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>136s</sub> | T/o<br><sub>77s</sub> | N<br><sub>75s</sub> | N<br><sub>71s</sub> | T/o<br><sub>85s</sub> | – | N<br><sub>75s</sub> | N<br><sub>76s</sub> | T/o<br><sub>150s</sub> | N<br><sub>79s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>101s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>81s</sub> | N<br><sub>62s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>87s</sub> | N<br><sub>116s</sub> | N<br><sub>62s</sub> | N<br><sub>62s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>75s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>131s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>76s</sub> | – | N<br><sub>78s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>101s</sub> | N<br><sub>70s</sub> | N<br><sub>84s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>20s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>20s</sub> | – | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>86s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>157s</sub> | T/o<br><sub>99s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>129s</sub> | T/o<br><sub>73s</sub> | N<br><sub>69s</sub> | N<br><sub>66s</sub> | T/o<br><sub>81s</sub> | – | N<br><sub>70s</sub> | N<br><sub>71s</sub> | T/o<br><sub>160s</sub> | N<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>94s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>102s</sub> | N<br><sub>59s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>82s</sub> | N<br><sub>109s</sub> | N<br><sub>59s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>79s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>133s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>76s</sub> | – | N<br><sub>78s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | N<br><sub>77s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>127s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>87s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>155s</sub> | T/o<br><sub>96s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>129s</sub> | T/o<br><sub>73s</sub> | N<br><sub>69s</sub> | N<br><sub>65s</sub> | T/o<br><sub>80s</sub> | – | N<br><sub>70s</sub> | N<br><sub>71s</sub> | T/o<br><sub>164s</sub> | N<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>95s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>14608s</sub> | N<br><sub>59s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>86s</sub> | N<br><sub>110s</sub> | N<br><sub>59s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>79s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>134s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>82s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>72s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>78s</sub> | – | N<br><sub>76s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>65s</sub> | N<br><sub>71s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>99s</sub> | N<br><sub>76s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | – | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | Y<br><sub>24s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>154s</sub> | T/o<br><sub>100s</sub> | – | T/o<br><sub>88s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>82s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>130s</sub> | T/o<br><sub>74s</sub> | N<br><sub>71s</sub> | N<br><sub>67s</sub> | T/o<br><sub>82s</sub> | – | N<br><sub>72s</sub> | N<br><sub>72s</sub> | T/o<br><sub>143s</sub> | N<br><sub>72s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>85s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>101s</sub> | N<br><sub>59s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>82s</sub> | N<br><sub>109s</sub> | N<br><sub>59s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>78s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>133s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>82s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | N<br><sub>71s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>76s</sub> | – | N<br><sub>79s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>99s</sub> | N<br><sub>67s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | T/o<br><sub>62s</sub> | Y<br><sub>10s</sub> | – | Y<br><sub>10s</sub> | Y<br><sub>10.0s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>117s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>85s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>85s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>79s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>125s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>117s</sub> | – | T/o<br><sub>93s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>8.8s</sub> | Y<br><sub>8.7s</sub> | Y<br><sub>8.7s</sub> | Y<br><sub>8.7s</sub> | Y<br><sub>8.7s</sub> | – | Y<br><sub>8.7s</sub> | Y<br><sub>8.7s</sub> | Y<br><sub>8.7s</sub> | Y<br><sub>8.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>93s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>95s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>96s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>104s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>130s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>100s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>85s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>83s</sub> | T/o<br><sub>91s</sub> | N<br><sub>88s</sub> | N<br><sub>82s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>77s</sub> | N<br><sub>83s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>91s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>82s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>78s</sub> | N<br><sub>80s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>106s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>98s</sub> | N<br><sub>78s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>92s</sub> | N<br><sub>74s</sub> | N<br><sub>80s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>111s</sub> | T/o<br><sub>88s</sub> | N<br><sub>86s</sub> | N<br><sub>82s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>82s</sub> | T/o<br><sub>70s</sub> | N<br><sub>81s</sub> | N<br><sub>81s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | N<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>36213s</sub> | N<br><sub>69s</sub> | T/o<br><sub>96s</sub> | N<br><sub>77s</sub> | N<br><sub>78s</sub> | – | N<br><sub>80s</sub> | T/o<br><sub>69s</sub> | N<br><sub>70s</sub> | N<br><sub>81s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | – | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>113s</sub> | T/o<br><sub>91s</sub> | N<br><sub>88s</sub> | N<br><sub>83s</sub> | T/o<br><sub>100s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>93s</sub> | N<br><sub>81s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>85s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>84s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>109s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>82s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>112s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>81s</sub> | T/o<br><sub>77s</sub> | N<br><sub>80s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>84s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>83s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>106s</sub> | N<br><sub>69s</sub> | N<br><sub>95s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>79s</sub> | N<br><sub>68s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>94s</sub> | T/o<br><sub>88s</sub> | N<br><sub>85s</sub> | N<br><sub>82s</sub> | T/o<br><sub>143s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>81s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>73s</sub> | N<br><sub>79s</sub> | T/o<br><sub>83s</sub> | – | N<br><sub>79s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>107s</sub> | N<br><sub>91s</sub> | N<br><sub>96s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>154s</sub> | T/o<br><sub>84s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>82s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>130s</sub> | T/o<br><sub>75s</sub> | N<br><sub>71s</sub> | N<br><sub>68s</sub> | T/o<br><sub>83s</sub> | – | N<br><sub>73s</sub> | N<br><sub>73s</sub> | T/o<br><sub>145s</sub> | N<br><sub>72s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>96s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>104s</sub> | N<br><sub>60s</sub> | T/o<br><sub>88s</sub> | – | T/o<br><sub>82s</sub> | N<br><sub>66s</sub> | N<br><sub>59s</sub> | N<br><sub>59s</sub> | 0/9 (0%) |

### Class 6

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>2.0s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.2s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | – | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>87s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>88s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>19s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>19s</sub> | – | Y<br><sub>18s</sub> | Y<br><sub>19s</sub> | Y<br><sub>18s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>82s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>89s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>4358s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>90s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>8.9s</sub> | Y<br><sub>8.9s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.7s</sub> | – | Y<br><sub>8.6s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>105s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>110s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>112s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>131s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>146s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>137s</sub> | T/o<br><sub>130s</sub> | – | T/o<br><sub>96s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>212s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | – | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | Y<br><sub>15s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>169s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | – | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | Y<br><sub>8.8s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>99s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>97s</sub> | – | T/o<br><sub>93s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>102s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>145s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>148s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>102s</sub> | T/o<br><sub>142s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>91s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>108s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | N<br><sub>52s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>69s</sub> | T/o<br><sub>74s</sub> | N<br><sub>75s</sub> | N<br><sub>50s</sub> | N<br><sub>49s</sub> | N<br><sub>44s</sub> | – | N<br><sub>50s</sub> | N<br><sub>51s</sub> | N<br><sub>50s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>12s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | Y<br><sub>13s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>80s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | – | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>73s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>76s</sub> | N<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.5s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>21s</sub> | Y<br><sub>22s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | – | Y<br><sub>22s</sub> | Y<br><sub>22s</sub> | Y<br><sub>21s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>88s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>88s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>87s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.9) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>31s</sub> | Y<br><sub>31s</sub> | Y<br><sub>31s</sub> | Y<br><sub>30s</sub> | Y<br><sub>31s</sub> | Y<br><sub>30s</sub> | – | Y<br><sub>31s</sub> | Y<br><sub>30s</sub> | Y<br><sub>31s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>86s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>82s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>81s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | N<br><sub>65s</sub> | N<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.9) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | – | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | Y<br><sub>19s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>84s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>95s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>96s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>96s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.9s</sub> | Y<br><sub>9.8s</sub> | Y<br><sub>9.7s</sub> | Y<br><sub>9.7s</sub> | Y<br><sub>9.4s</sub> | Y<br><sub>9.5s</sub> | – | Y<br><sub>9.7s</sub> | Y<br><sub>9.6s</sub> | Y<br><sub>9.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>148s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>68s</sub> | N<br><sub>55s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>75s</sub> | T/o<br><sub>80s</sub> | N<br><sub>81s</sub> | N<br><sub>54s</sub> | N<br><sub>54s</sub> | N<br><sub>48s</sub> | – | N<br><sub>54s</sub> | N<br><sub>55s</sub> | N<br><sub>53s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>110s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>94s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>95s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.95) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | Y<br><sub>16s</sub> | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | – | Y<br><sub>17s</sub> | Y<br><sub>16s</sub> | Y<br><sub>16s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | N<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>67s</sub> | N<br><sub>55s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>74s</sub> | T/o<br><sub>79s</sub> | N<br><sub>79s</sub> | N<br><sub>53s</sub> | N<br><sub>53s</sub> | N<br><sub>48s</sub> | – | N<br><sub>53s</sub> | N<br><sub>54s</sub> | N<br><sub>53s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.4s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>1.0s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>90s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>79s</sub> | – | T/o<br><sub>95s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>80s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>94s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>9.9s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | – | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | Y<br><sub>10s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>152s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>67s</sub> | N<br><sub>56s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>74s</sub> | T/o<br><sub>79s</sub> | N<br><sub>79s</sub> | N<br><sub>52s</sub> | N<br><sub>52s</sub> | N<br><sub>48s</sub> | – | N<br><sub>53s</sub> | N<br><sub>54s</sub> | N<br><sub>54s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>90s</sub> | – | T/o<br><sub>137s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>62s</sub> | N<br><sub>64s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>87s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.99) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>31s</sub> | Y<br><sub>30s</sub> | – | Y<br><sub>31s</sub> | Y<br><sub>31s</sub> | Y<br><sub>31s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>86s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>73s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | N<br><sub>66s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | – | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>87s</sub> | N<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | N<br><sub>64s</sub> | – | N<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.7s</sub> | Y<br><sub>1.7s</sub> | – | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.6s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | – | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | Y<br><sub>12s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.8s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | – | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | Y<br><sub>3.7s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>9.1s</sub> | Y<br><sub>9.4s</sub> | Y<br><sub>9.0s</sub> | Y<br><sub>9.3s</sub> | Y<br><sub>8.9s</sub> | Y<br><sub>9.3s</sub> | – | Y<br><sub>9.0s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.4s</sub> | – | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | Y<br><sub>3.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>17s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>18s</sub> | Y<br><sub>17s</sub> | Y<br><sub>18s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | N<br><sub>118s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | – | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | Y<br><sub>3.6s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>118s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>150s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->!B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>97s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->B] (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | – | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.7s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.0s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>103s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>81s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.8s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.9s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>1.9s</sub> | Y<br><sub>2.0s</sub> | Y<br><sub>2.8s</sub> | – | Y<br><sub>1.8s</sub> | Y<br><sub>1.8s</sub> | Y<br><sub>2.1s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>7.9s</sub> | Y<br><sub>7.7s</sub> | Y<br><sub>7.8s</sub> | Y<br><sub>7.8s</sub> | Y<br><sub>7.8s</sub> | Y<br><sub>7.9s</sub> | – | Y<br><sub>7.8s</sub> | Y<br><sub>7.7s</sub> | Y<br><sub>7.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | – | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | – | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | – | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | Y<br><sub>13s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | – | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | Y<br><sub>17s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.4s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>2.9s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### none (baseline) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.4s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.4s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>62s</sub> | N<br><sub>64s</sub> | N<br><sub>60s</sub> | 0/9 (0%) |

### Class 7

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>26s</sub> | Y<br><sub>4.0s</sub> | Y<br><sub>15s</sub> | Y<br><sub>9.4s</sub> | Y<br><sub>9.7s</sub> | Y<br><sub>27s</sub> | Y<br><sub>10.0s</sub> | – | Y<br><sub>12s</sub> | Y<br><sub>25s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>80s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>79s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>82s</sub> | – | T/o<br><sub>87s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>60s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.0s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>17s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | – | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.9) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>21s</sub> | Y<br><sub>22s</sub> | Y<br><sub>20s</sub> | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | Y<br><sub>20s</sub> | Y<br><sub>22s</sub> | – | Y<br><sub>21s</sub> | Y<br><sub>21s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>137s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>135s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>114s</sub> | – | T/o<br><sub>119s</sub> | T/o<br><sub>129s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>127s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>154s</sub> | T/o<br><sub>131s</sub> | T/o<br><sub>140s</sub> | – | T/o<br><sub>122s</sub> | T/o<br><sub>128s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>80s</sub> | – | T/o<br><sub>83s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>87s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>43s</sub> | T/o<br><sub>102s</sub> | N<br><sub>42s</sub> | N<br><sub>41s</sub> | T/o<br><sub>112s</sub> | N<br><sub>41s</sub> | N<br><sub>47s</sub> | – | T/o<br><sub>97s</sub> | T/o<br><sub>105s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | N<br><sub>41s</sub> | N<br><sub>38s</sub> | N<br><sub>38s</sub> | N<br><sub>38s</sub> | N<br><sub>38s</sub> | N<br><sub>64s</sub> | – | N<br><sub>38s</sub> | N<br><sub>42s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>29s</sub> | Y<br><sub>30s</sub> | Y<br><sub>25s</sub> | Y<br><sub>29s</sub> | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | Y<br><sub>32s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>25s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>75s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>157s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>76s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>15s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | Y<br><sub>40s</sub> | Y<br><sub>41s</sub> | Y<br><sub>42s</sub> | – | Y<br><sub>42s</sub> | Y<br><sub>41s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>142s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.95) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.95) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>21s</sub> | Y<br><sub>22s</sub> | Y<br><sub>21s</sub> | Y<br><sub>22s</sub> | Y<br><sub>21s</sub> | Y<br><sub>22s</sub> | Y<br><sub>21s</sub> | – | Y<br><sub>20s</sub> | Y<br><sub>20s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>106s</sub> | – | T/o<br><sub>127s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>130s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>110s</sub> | – | T/o<br><sub>112s</sub> | T/o<br><sub>124s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>127s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>121s</sub> | T/o<br><sub>154s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>135s</sub> | – | T/o<br><sub>112s</sub> | T/o<br><sub>103s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>81s</sub> | – | T/o<br><sub>88s</sub> | T/o<br><sub>79s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>33s</sub> | T/o<br><sub>67s</sub> | N<br><sub>31s</sub> | N<br><sub>31s</sub> | T/o<br><sub>80s</sub> | N<br><sub>30s</sub> | N<br><sub>34s</sub> | – | T/o<br><sub>76s</sub> | T/o<br><sub>112s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>56s</sub> | N<br><sub>31s</sub> | N<br><sub>28s</sub> | N<br><sub>28s</sub> | N<br><sub>27s</sub> | N<br><sub>27s</sub> | N<br><sub>49s</sub> | – | N<br><sub>27s</sub> | N<br><sub>29s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>7.6s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>7.4s</sub> | – | Y<br><sub>7.5s</sub> | Y<br><sub>7.5s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>41s</sub> | Y<br><sub>40s</sub> | Y<br><sub>41s</sub> | Y<br><sub>55s</sub> | Y<br><sub>40s</sub> | Y<br><sub>40s</sub> | Y<br><sub>60s</sub> | – | Y<br><sub>40s</sub> | Y<br><sub>41s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>6.3s</sub> | Y<br><sub>6.2s</sub> | Y<br><sub>6.2s</sub> | Y<br><sub>6.2s</sub> | Y<br><sub>6.2s</sub> | Y<br><sub>6.1s</sub> | Y<br><sub>6.2s</sub> | – | Y<br><sub>6.3s</sub> | Y<br><sub>6.2s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.4s</sub> | – | Y<br><sub>6.4s</sub> | Y<br><sub>6.3s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>26s</sub> | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>76s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>75s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | Y<br><sub>29s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>70s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>72s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>64s</sub> | N<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | N<br><sub>80s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>80s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | N<br><sub>65s</sub> | T/o<br><sub>62s</sub> | N<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.9s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>26s</sub> | Y<br><sub>3.9s</sub> | Y<br><sub>15s</sub> | Y<br><sub>9.2s</sub> | Y<br><sub>9.3s</sub> | Y<br><sub>26s</sub> | Y<br><sub>9.3s</sub> | – | Y<br><sub>12s</sub> | Y<br><sub>23s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>153s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>76s</sub> | T/o<br><sub>147270s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.1s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.1s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.0s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | – | Y<br><sub>0.7s</sub> | Y<br><sub>0.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.0s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | Y<br><sub>0.8s</sub> | – | Y<br><sub>0.6s</sub> | Y<br><sub>0.6s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>14s</sub> | Y<br><sub>19s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | Y<br><sub>18s</sub> | – | Y<br><sub>19s</sub> | Y<br><sub>18s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>103s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>108s</sub> | T/o<br><sub>103s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>117s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>147s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>132s</sub> | – | T/o<br><sub>114s</sub> | T/o<br><sub>119s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>72s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>107s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>92s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>45s</sub> | T/o<br><sub>68s</sub> | N<br><sub>42s</sub> | N<br><sub>41s</sub> | T/o<br><sub>112s</sub> | N<br><sub>40s</sub> | N<br><sub>46s</sub> | – | T/o<br><sub>89s</sub> | T/o<br><sub>95s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>64s</sub> | N<br><sub>37s</sub> | N<br><sub>34s</sub> | N<br><sub>34s</sub> | N<br><sub>34s</sub> | N<br><sub>34s</sub> | N<br><sub>57s</sub> | – | N<br><sub>34s</sub> | N<br><sub>37s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>32s</sub> | Y<br><sub>31s</sub> | Y<br><sub>25s</sub> | Y<br><sub>30s</sub> | Y<br><sub>31s</sub> | Y<br><sub>31s</sub> | Y<br><sub>33s</sub> | – | Y<br><sub>31s</sub> | Y<br><sub>26s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>60s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>86s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.95) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>15s</sub> | Y<br><sub>37s</sub> | Y<br><sub>36s</sub> | Y<br><sub>36s</sub> | Y<br><sub>37s</sub> | Y<br><sub>36s</sub> | Y<br><sub>37s</sub> | – | Y<br><sub>37s</sub> | Y<br><sub>36s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>78s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>112s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>114s</sub> | – | T/o<br><sub>118s</sub> | T/o<br><sub>112s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>127s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>155s</sub> | T/o<br><sub>131s</sub> | T/o<br><sub>143s</sub> | – | T/o<br><sub>122s</sub> | T/o<br><sub>127s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>101s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>27s</sub> | T/o<br><sub>76s</sub> | N<br><sub>29s</sub> | N<br><sub>27s</sub> | T/o<br><sub>72s</sub> | N<br><sub>28s</sub> | N<br><sub>33s</sub> | – | T/o<br><sub>79s</sub> | T/o<br><sub>96s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>39s</sub> | N<br><sub>33s</sub> | N<br><sub>31s</sub> | N<br><sub>31s</sub> | N<br><sub>30s</sub> | N<br><sub>30s</sub> | N<br><sub>57s</sub> | – | N<br><sub>31s</sub> | N<br><sub>34s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L12) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>25s</sub> | Y<br><sub>34s</sub> | Y<br><sub>34s</sub> | Y<br><sub>32s</sub> | Y<br><sub>33s</sub> | – | Y<br><sub>31s</sub> | Y<br><sub>25s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>93s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>121s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>89s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>174s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.2s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.1s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.2s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.2s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.2s</sub> | Y<br><sub>0.7s</sub> | Y<br><sub>1.2s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.2s</sub> | – | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.95) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | – | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>158s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>138s</sub> | T/o<br><sub>155s</sub> | T/o<br><sub>147s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>130s</sub> | – | T/o<br><sub>133s</sub> | T/o<br><sub>148s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>141s</sub> | T/o<br><sub>145s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>137s</sub> | T/o<br><sub>177s</sub> | T/o<br><sub>149s</sub> | T/o<br><sub>151s</sub> | – | T/o<br><sub>135s</sub> | T/o<br><sub>143s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>86s</sub> | – | T/o<br><sub>60s</sub> | T/o<br><sub>82s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>32s</sub> | T/o<br><sub>73s</sub> | N<br><sub>31s</sub> | N<br><sub>29s</sub> | T/o<br><sub>90s</sub> | N<br><sub>31s</sub> | N<br><sub>41s</sub> | – | T/o<br><sub>89s</sub> | T/o<br><sub>89s</sub> | 0/9 (0%) |
| `0.20` | N<br><sub>58s</sub> | N<br><sub>33s</sub> | N<br><sub>28s</sub> | N<br><sub>28s</sub> | N<br><sub>28s</sub> | N<br><sub>29s</sub> | N<br><sub>44s</sub> | – | N<br><sub>29s</sub> | N<br><sub>32s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>1.0s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>33s</sub> | Y<br><sub>33s</sub> | Y<br><sub>28s</sub> | Y<br><sub>33s</sub> | Y<br><sub>33s</sub> | Y<br><sub>33s</sub> | Y<br><sub>35s</sub> | – | Y<br><sub>33s</sub> | Y<br><sub>28s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>73s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>181s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>130s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>76s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.95) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>1.3s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>0.9s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>0.8s</sub> | Y<br><sub>1.3s</sub> | – | Y<br><sub>0.9s</sub> | Y<br><sub>0.9s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.95) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>14s</sub> | Y<br><sub>20s</sub> | Y<br><sub>17s</sub> | Y<br><sub>20s</sub> | Y<br><sub>20s</sub> | Y<br><sub>20s</sub> | Y<br><sub>20s</sub> | – | Y<br><sub>19s</sub> | Y<br><sub>20s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>130s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>130s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>114s</sub> | T/o<br><sub>109s</sub> | – | T/o<br><sub>112s</sub> | T/o<br><sub>123s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>120s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>146s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>132s</sub> | – | T/o<br><sub>113s</sub> | T/o<br><sub>118s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>88s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>90s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>36s</sub> | T/o<br><sub>83s</sub> | N<br><sub>30s</sub> | N<br><sub>30s</sub> | T/o<br><sub>93s</sub> | N<br><sub>35s</sub> | N<br><sub>42s</sub> | – | T/o<br><sub>123s</sub> | T/o<br><sub>102s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | N<br><sub>38s</sub> | N<br><sub>34s</sub> | N<br><sub>34s</sub> | N<br><sub>33s</sub> | N<br><sub>34s</sub> | N<br><sub>59s</sub> | – | N<br><sub>33s</sub> | N<br><sub>38s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>7.6s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>7.6s</sub> | – | Y<br><sub>7.5s</sub> | Y<br><sub>7.5s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>41s</sub> | Y<br><sub>41s</sub> | Y<br><sub>40s</sub> | Y<br><sub>55s</sub> | Y<br><sub>40s</sub> | Y<br><sub>40s</sub> | Y<br><sub>59s</sub> | – | Y<br><sub>40s</sub> | Y<br><sub>40s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.0s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>6.0s</sub> | Y<br><sub>6.1s</sub> | Y<br><sub>6.0s</sub> | Y<br><sub>6.0s</sub> | Y<br><sub>6.0s</sub> | Y<br><sub>6.1s</sub> | Y<br><sub>6.0s</sub> | – | Y<br><sub>6.1s</sub> | Y<br><sub>6.1s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>6.5s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.4s</sub> | – | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | 9/9 (100%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>23s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>73s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>63s</sub> | N<br><sub>68s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | N<br><sub>65s</sub> | N<br><sub>62s</sub> | N<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | N<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>7.6s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>7.7s</sub> | – | Y<br><sub>7.5s</sub> | Y<br><sub>7.5s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>40s</sub> | Y<br><sub>41s</sub> | Y<br><sub>42s</sub> | Y<br><sub>58s</sub> | Y<br><sub>41s</sub> | Y<br><sub>40s</sub> | Y<br><sub>60s</sub> | – | Y<br><sub>41s</sub> | Y<br><sub>40s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>6.3s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.4s</sub> | – | Y<br><sub>6.4s</sub> | Y<br><sub>6.4s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>6.7s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.5s</sub> | – | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | 9/9 (100%) |

##### Impl L1→L2 (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>80s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | – | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | N<br><sub>80s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>90s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | N<br><sub>62s</sub> | N<br><sub>62s</sub> | N<br><sub>63s</sub> | N<br><sub>64s</sub> | T/o<br><sub>61s</sub> | – | N<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>7.7s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>7.6s</sub> | – | Y<br><sub>7.6s</sub> | Y<br><sub>7.7s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>43s</sub> | Y<br><sub>43s</sub> | Y<br><sub>43s</sub> | Y<br><sub>58s</sub> | Y<br><sub>42s</sub> | Y<br><sub>42s</sub> | Y<br><sub>62s</sub> | – | Y<br><sub>41s</sub> | Y<br><sub>42s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.1s</sub> | – | Y<br><sub>3.1s</sub> | Y<br><sub>3.1s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>6.4s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.3s</sub> | Y<br><sub>6.4s</sub> | – | Y<br><sub>6.4s</sub> | Y<br><sub>6.6s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>6.6s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.6s</sub> | – | Y<br><sub>6.6s</sub> | Y<br><sub>6.6s</sub> | 9/9 (100%) |

##### Impl L2→L3 (α=0.99) (L23) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>29s</sub> | Y<br><sub>32s</sub> | Y<br><sub>33s</sub> | Y<br><sub>32s</sub> | Y<br><sub>33s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | – | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | – | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>7.8s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.3s</sub> | Y<br><sub>7.5s</sub> | – | Y<br><sub>7.8s</sub> | Y<br><sub>7.8s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>44s</sub> | Y<br><sub>42s</sub> | Y<br><sub>42s</sub> | Y<br><sub>59s</sub> | Y<br><sub>42s</sub> | Y<br><sub>42s</sub> | Y<br><sub>63s</sub> | – | Y<br><sub>43s</sub> | Y<br><sub>42s</sub> | 9/9 (100%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.05` | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | – | Y<br><sub>3.2s</sub> | Y<br><sub>3.2s</sub> | 9/9 (100%) |
| `0.10` | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | Y<br><sub>6.5s</sub> | – | Y<br><sub>6.5s</sub> | Y<br><sub>6.4s</sub> | 9/9 (100%) |
| `0.20` | Y<br><sub>6.6s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.6s</sub> | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | – | Y<br><sub>6.7s</sub> | Y<br><sub>6.7s</sub> | 9/9 (100%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=1/36 (2.8%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | Y<br><sub>17s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | 1/9 (11%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=8/36 (22.2%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | Y<br><sub>14s</sub> | – | Y<br><sub>14s</sub> | T/o<br><sub>66s</sub> | 8/9 (89%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>114s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>84s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>83s</sub> | – | T/o<br><sub>86s</sub> | T/o<br><sub>87s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>71s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | 0/9 (0%) |

##### Impl L1→L2 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>105s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>69s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |

##### Impl L1→L2 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>67s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>61s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>98s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->!B] (α=0.99) — Y=9/36 (25.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>30s</sub> | Y<br><sub>32s</sub> | Y<br><sub>30s</sub> | Y<br><sub>29s</sub> | Y<br><sub>30s</sub> | – | Y<br><sub>28s</sub> | Y<br><sub>29s</sub> | 9/9 (100%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |

##### Impl L2→L3 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>116s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>95s</sub> | N<br><sub>93s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>64s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>102s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>98s</sub> | – | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |

##### Impl L2→L3 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.10` | N<br><sub>100s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>63s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>61s</sub> | – | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | 0/9 (0%) |

### Class 9

Reference point: `class_sample[0]`  

#### Full-Rule

##### ALWAYS_OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.5s</sub> | Y<br><sub>1.6s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>77s</sub> | T/o<br><sub>99s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>253s</sub> | T/o<br><sub>70s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>92s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>89s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>122s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>104s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>73s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>161s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>74s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>70s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |

##### Impl L1→L2 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>75s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |

##### Impl L2→L3 (α=0.9) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>82s</sub> | N<br><sub>71s</sub> | T/o<br><sub>72s</sub> | N<br><sub>69s</sub> | T/o<br><sub>84s</sub> | N<br><sub>71s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>91s</sub> | N<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>112s</sub> | N<br><sub>64s</sub> | N<br><sub>80s</sub> | N<br><sub>66s</sub> | N<br><sub>74s</sub> | N<br><sub>63s</sub> | T/o<br><sub>99s</sub> | N<br><sub>69s</sub> | N<br><sub>60s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>70s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>80s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>76s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>70s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | N<br><sub>72s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>86s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>99s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>211s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>128s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>90s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | N<br><sub>60s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | N<br><sub>58s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>90s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>165s</sub> | N<br><sub>74s</sub> | N<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | N<br><sub>55s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>85s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>131s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>87s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>194s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>196s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>189s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>92s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>84s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>78s</sub> | N<br><sub>67s</sub> | T/o<br><sub>69s</sub> | N<br><sub>65s</sub> | T/o<br><sub>80s</sub> | N<br><sub>68s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>93s</sub> | N<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>108s</sub> | N<br><sub>58s</sub> | N<br><sub>77s</sub> | N<br><sub>64s</sub> | N<br><sub>63s</sub> | N<br><sub>61s</sub> | T/o<br><sub>96s</sub> | N<br><sub>67s</sub> | N<br><sub>61s</sub> | – | 0/9 (0%) |

#### Per-Layer

##### ALWAYS_OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>75s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>245s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>112s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>88s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>169s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>72s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>162s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L01) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |

##### Impl L0→L1 (α=0.9) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>70s</sub> | – | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>91s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>82s</sub> | N<br><sub>70s</sub> | T/o<br><sub>70s</sub> | N<br><sub>68s</sub> | T/o<br><sub>84s</sub> | N<br><sub>70s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>94s</sub> | N<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>108s</sub> | N<br><sub>62s</sub> | N<br><sub>78s</sub> | N<br><sub>64s</sub> | N<br><sub>66s</sub> | N<br><sub>62s</sub> | T/o<br><sub>96s</sub> | N<br><sub>64s</sub> | N<br><sub>59s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>75s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>217s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>86s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>113s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>89s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>71s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>161s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>104s</sub> | T/o<br><sub>85s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L12) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |

##### Impl L1→L2 (α=0.9) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>77s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>81s</sub> | N<br><sub>67s</sub> | T/o<br><sub>87s</sub> | N<br><sub>67s</sub> | T/o<br><sub>83s</sub> | N<br><sub>71s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>95s</sub> | N<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>108s</sub> | N<br><sub>63s</sub> | N<br><sub>79s</sub> | N<br><sub>65s</sub> | N<br><sub>64s</sub> | N<br><sub>63s</sub> | T/o<br><sub>97s</sub> | N<br><sub>67s</sub> | N<br><sub>62s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.4s</sub> | Y<br><sub>1.4s</sub> | – | 9/9 (100%) |

##### ALWAYS_ON (α=0.9) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>80s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>246s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>86s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>102s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>90s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>88s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>164s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.9) (L23) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.05` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.10` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |
| `0.20` | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | Y<br><sub>1.5s</sub> | – | 9/9 (100%) |

##### Impl L2→L3 (α=0.9) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>94s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>119s</sub> | T/o<br><sub>87s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>81s</sub> | N<br><sub>65s</sub> | T/o<br><sub>68s</sub> | N<br><sub>68s</sub> | T/o<br><sub>83s</sub> | N<br><sub>71s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>66s</sub> | N<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>108s</sub> | N<br><sub>62s</sub> | N<br><sub>78s</sub> | N<br><sub>64s</sub> | N<br><sub>64s</sub> | N<br><sub>61s</sub> | T/o<br><sub>95s</sub> | N<br><sub>67s</sub> | N<br><sub>61s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>79s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>79s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>79s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>93s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>102s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>98s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>129s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>130s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>91s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>75s</sub> | N<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>78s</sub> | N<br><sub>59s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>93s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>168s</sub> | N<br><sub>75s</sub> | N<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>71s</sub> | N<br><sub>56s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>79s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 (α=0.99) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |

##### none (baseline) (L01) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>89s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>199s</sub> | T/o<br><sub>172s</sub> | T/o<br><sub>188s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>190s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>93s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>80s</sub> | N<br><sub>68s</sub> | T/o<br><sub>69s</sub> | N<br><sub>66s</sub> | T/o<br><sub>81s</sub> | N<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>92s</sub> | N<br><sub>59s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>100s</sub> | N<br><sub>60s</sub> | N<br><sub>76s</sub> | N<br><sub>63s</sub> | N<br><sub>63s</sub> | N<br><sub>60s</sub> | T/o<br><sub>64s</sub> | N<br><sub>66s</sub> | N<br><sub>60s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>80s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>83s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | N<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>80s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>94s</sub> | T/o<br><sub>110s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>103s</sub> | T/o<br><sub>127s</sub> | T/o<br><sub>131s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>208s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>118s</sub> | T/o<br><sub>126s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>62s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>89s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>74s</sub> | N<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>76s</sub> | N<br><sub>59s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>89s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>164s</sub> | N<br><sub>74s</sub> | N<br><sub>60s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | N<br><sub>56s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>71s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>77s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>76s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |

##### Impl L1→L2 (α=0.99) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |

##### none (baseline) (L12) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>197s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>190s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>106s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>86s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>80s</sub> | N<br><sub>69s</sub> | T/o<br><sub>70s</sub> | N<br><sub>67s</sub> | T/o<br><sub>82s</sub> | N<br><sub>69s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>95s</sub> | N<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>110s</sub> | N<br><sub>62s</sub> | N<br><sub>78s</sub> | T/o<br><sub>68s</sub> | N<br><sub>64s</sub> | N<br><sub>61s</sub> | T/o<br><sub>95s</sub> | N<br><sub>66s</sub> | N<br><sub>62s</sub> | – | 0/9 (0%) |

##### ALWAYS_OFF (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>79s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>117s</sub> | T/o<br><sub>81s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>83s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>100s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>78s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>79s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>79s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>71s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>100s</sub> | T/o<br><sub>125s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>210s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>120s</sub> | T/o<br><sub>127s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>90s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>75s</sub> | N<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>78s</sub> | N<br><sub>59s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>91s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>126s</sub> | T/o<br><sub>168s</sub> | N<br><sub>75s</sub> | N<br><sub>61s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>71s</sub> | N<br><sub>56s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>72s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>83s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>72s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>85s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |

##### Impl L2→L3 (α=0.99) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>64s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |

##### none (baseline) (L23) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>60s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>195s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>195s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>90s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>106s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>116s</sub> | T/o<br><sub>85s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>78s</sub> | N<br><sub>67s</sub> | T/o<br><sub>68s</sub> | N<br><sub>66s</sub> | T/o<br><sub>81s</sub> | N<br><sub>69s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>94s</sub> | N<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>107s</sub> | N<br><sub>62s</sub> | N<br><sub>68s</sub> | N<br><sub>64s</sub> | N<br><sub>63s</sub> | N<br><sub>60s</sub> | T/o<br><sub>94s</sub> | N<br><sub>66s</sub> | N<br><sub>60s</sub> | – | 0/9 (0%) |

#### Impl Ablation

##### ALWAYS_OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>80s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>94s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>80s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>80s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>78s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>91s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>70s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>100s</sub> | T/o<br><sub>123s</sub> | T/o<br><sub>128s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>211s</sub> | T/o<br><sub>101s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>139s</sub> | T/o<br><sub>127s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>90s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>74s</sub> | N<br><sub>60s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>77s</sub> | N<br><sub>58s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>90s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>124s</sub> | T/o<br><sub>139s</sub> | N<br><sub>69s</sub> | N<br><sub>61s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>79s</sub> | N<br><sub>55s</sub> | – | 0/9 (0%) |

##### ALWAYS_ON+OFF (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>72s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>78s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>85s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>66s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>85s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>74s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [!A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>100s</sub> | T/o<br><sub>103s</sub> | T/o<br><sub>93s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>84s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>83s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>78s</sub> | N<br><sub>69s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>89s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>73s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>90s</sub> | T/o<br><sub>111s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>83s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>102s</sub> | T/o<br><sub>91s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>90s</sub> | T/o<br><sub>92s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>89s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |

##### Impl L0→L1 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>62s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>85s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>80s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>89s</sub> | T/o<br><sub>95s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>82s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>83s</sub> | – | 0/9 (0%) |

##### Impl L1→L2 [!A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>72s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>71s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |

##### Impl L1→L2 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>66s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>79s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>90s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>89s</sub> | T/o<br><sub>76s</sub> | N<br><sub>67s</sub> | N<br><sub>73s</sub> | T/o<br><sub>73s</sub> | N<br><sub>67s</sub> | T/o<br><sub>96s</sub> | T/o<br><sub>64s</sub> | N<br><sub>83s</sub> | – | 0/9 (0%) |

##### Impl L1→L2 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>122s</sub> | T/o<br><sub>109s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>83s</sub> | T/o<br><sub>97s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |

##### Impl L1→L2 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>68s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>79s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>90s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>84s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>88s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>81s</sub> | T/o<br><sub>76s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>99s</sub> | T/o<br><sub>24073s</sub> | N<br><sub>67s</sub> | N<br><sub>83s</sub> | T/o<br><sub>74s</sub> | N<br><sub>72s</sub> | T/o<br><sub>97s</sub> | T/o<br><sub>65s</sub> | N<br><sub>83s</sub> | – | 0/9 (0%) |

##### Impl L2→L3 [!A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>124s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>133s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>108s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>95s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>65s</sub> | – | 0/9 (0%) |

##### Impl L2→L3 [!A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>63s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>62s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>69s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>78s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>74s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | N<br><sub>69s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>66s</sub> | N<br><sub>59s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>78s</sub> | N<br><sub>84s</sub> | T/o<br><sub>106s</sub> | N<br><sub>58s</sub> | T/o<br><sub>64s</sub> | N<br><sub>56s</sub> | N<br><sub>104s</sub> | T/o<br><sub>62s</sub> | N<br><sub>73s</sub> | – | 0/9 (0%) |

##### Impl L2→L3 [A->!B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>67s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>67s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>68s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>77s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>68s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>74s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>61s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>71s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>67s</sub> | T/o<br><sub>61s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>78s</sub> | N<br><sub>64s</sub> | N<br><sub>56s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>65s</sub> | N<br><sub>62s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>65s</sub> | T/o<br><sub>73s</sub> | – | 0/9 (0%) |

##### Impl L2→L3 [A->B] (α=0.99) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>72s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>72s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>69s</sub> | T/o<br><sub>73s</sub> | T/o<br><sub>63s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>81s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>62s</sub> | T/o<br><sub>84s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>76s</sub> | – | 0/9 (0%) |
| `0.10` | N<br><sub>83s</sub> | T/o<br><sub>70s</sub> | T/o<br><sub>87s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>74s</sub> | T/o<br><sub>66s</sub> | T/o<br><sub>75s</sub> | T/o<br><sub>69s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>88s</sub> | N<br><sub>94s</sub> | T/o<br><sub>65s</sub> | N<br><sub>63s</sub> | T/o<br><sub>67s</sub> | N<br><sub>62s</sub> | N<br><sub>89s</sub> | N<br><sub>78s</sub> | N<br><sub>79s</sub> | – | 0/9 (0%) |

##### none (baseline) — Y=0/36 (0.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | T/o<br><sub>88s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>86s</sub> | T/o<br><sub>195s</sub> | T/o<br><sub>132s</sub> | T/o<br><sub>197s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>187s</sub> | T/o<br><sub>64s</sub> | – | 0/9 (0%) |
| `0.05` | T/o<br><sub>91s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>80s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>107s</sub> | T/o<br><sub>64s</sub> | T/o<br><sub>63s</sub> | T/o<br><sub>115s</sub> | T/o<br><sub>84s</sub> | – | 0/9 (0%) |
| `0.10` | T/o<br><sub>78s</sub> | N<br><sub>67s</sub> | T/o<br><sub>68s</sub> | N<br><sub>65s</sub> | T/o<br><sub>80s</sub> | N<br><sub>68s</sub> | T/o<br><sub>78s</sub> | T/o<br><sub>94s</sub> | N<br><sub>60s</sub> | – | 0/9 (0%) |
| `0.20` | T/o<br><sub>144s</sub> | N<br><sub>62s</sub> | N<br><sub>78s</sub> | N<br><sub>64s</sub> | N<br><sub>64s</sub> | N<br><sub>62s</sub> | T/o<br><sub>95s</sub> | N<br><sub>64s</sub> | N<br><sub>61s</sub> | – | 0/9 (0%) |

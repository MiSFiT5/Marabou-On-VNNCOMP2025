# Model Report: cifar_wide_kw

> **CIFAR** — `cifar_wide_kw`  
> Generated from `nap_verify/experiments/`

## Model Structure

_Structure info not found in model_structures.txt_

## Full-Rule Experiments (All Rules, All Layers Merged)

### α = 0.90

**Summary (Y% across all ε):**

| Rule | Y% | Y | Total |
|------|-----|---|-------|
| `ALWAYS_OFF (α=0.90)` | 100.0% | 360 | 360 |
| `ALWAYS_ON (α=0.90)` | 100.0% | 360 | 360 |
| `ALWAYS_ON+OFF (α=0.90)` | 100.0% | 360 | 360 |
| `Impl L0→L1 (α=0.90)` | 100.0% | 360 | 360 |
| `Impl L1→L2 (α=0.90)` | 100.0% | 360 | 360 |
| `Impl L2→L3 (α=0.90)` | 100.0% | 360 | 360 |
| `Impl L3→L4 (α=0.90)` | 100.0% | 360 | 360 |
| `none (baseline)` | 100.0% | 360 | 360 |

#### ALWAYS_OFF (α=0.90) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.90) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.90) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.90) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.90) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.90) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.90) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.90) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### none (baseline) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

### α = 0.95

**Summary (Y% across all ε):**

| Rule | Y% | Y | Total |
|------|-----|---|-------|
| `ALWAYS_OFF (α=0.95)` | 100.0% | 360 | 360 |
| `ALWAYS_ON (α=0.95)` | 100.0% | 360 | 360 |
| `ALWAYS_ON+OFF (α=0.95)` | 100.0% | 360 | 360 |
| `Impl L0→L1 (α=0.95)` | 100.0% | 360 | 360 |
| `Impl L1→L2 (α=0.95)` | 100.0% | 360 | 360 |
| `Impl L2→L3 (α=0.95)` | 100.0% | 360 | 360 |
| `Impl L3→L4 (α=0.95)` | 100.0% | 360 | 360 |
| `none (baseline)` | 100.0% | 360 | 360 |

#### ALWAYS_OFF (α=0.95) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |

#### ALWAYS_OFF (α=0.95) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON (α=0.95) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### ALWAYS_ON+OFF (α=0.95) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>5s</sub> | 🟢 Y<br><sub>5s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L0→L1 (α=0.95) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>7s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L1→L2 (α=0.95) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L2→L3 (α=0.95) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### Impl L3→L4 (α=0.95) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

#### none (baseline) (true class: 0) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 1) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 2) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 3) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 4) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 5) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 6) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 7) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 8) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 🟢 Y<br><sub>6s</sub> | 9/9 (100%) |

#### none (baseline) (true class: 9) — Y=36/36 (100.0%)

| ε | →0 | →1 | →2 | →3 | →4 | →5 | →6 | →7 | →8 | →9 | Y/total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.02` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.05` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.10` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |
| `0.20` | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | 🟢 Y<br><sub>6s</sub> | – | 9/9 (100%) |

---
*Report generated from `nap_verify/experiments/` — 2 experiments*
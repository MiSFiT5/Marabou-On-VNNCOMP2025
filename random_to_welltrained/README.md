# Random-to-Well-Trained: NAP Verifiable Region Evolution

> Generated 2026-03-25

## Research Questions

| RQ | Question |
|----|----------|
| Q1 | Does the NAP-verifiable region grow as training progresses from random initialization to convergence? |
| Q2 | Is the growth relative to the standard (no-NAP) baseline, and by how much? |
| Q3 | Why does NAP verification peak at ~75% training and degrade at 100%? |

## Model Selection & Architecture
### Benchmark Origin
The model used in this experiment comes from the **CORA VNN-COMP 2024 benchmark**
(`mnist-point` family), published by Koller et al.
| Item | Detail |
|------|--------|
| Benchmark | [cora-vnncomp2024-benchmark](https://github.com/kollerlukas/cora-vnncomp2024-benchmark) |
| Family | `mnist-point` |
| Paper | [Certified Training for Set-Based Specifications](https://arxiv.org/abs/2401.14961) (Koller et al., 2024) |
| Competition | VNN-COMP 2024 |
**Why this model?** Among all VNN-COMP 2024 benchmarks, `cora/mnist-point` was selected because it satisfies all three criteria simultaneously: (1) verifiable by Marabou (no parser errors), (2) standard ReLU MLP architecture compatible with NAP, and (3) public training data (MNIST) enabling train-from-scratch experiments. See `TASK1_SHORTLIST.md` for the full selection process.
### Architecture
The network is a fully-connected ReLU MLP for MNIST digit classification:
| Component | Detail |
|-----------|--------|
| Input | 784 (flattened 28×28 MNIST grayscale image) |
| Hidden layers | **7** fully-connected layers, each **250** neurons wide |
| Activation | ReLU (after each hidden layer) |
| Output | 10 logits (MNIST classes 0–9) |
| Total parameters | ~570K |

## Models

| Track | Architecture | Total Epochs | Checkpoints | Training |
|-------|-------------|--------------|-------------|----------|
| A | 784 → hidden → 10 (FC, MNIST) | 70 | epoch_000 (0%), epoch_018 (25%), epoch_035 (50%), epoch_052 (75%), epoch_070 (100%) | Standard CE |
| B | same | 100 | epoch_000 (0%), epoch_025 (25%), epoch_050 (50%), epoch_075 (75%), epoch_100 (100%) | Standard CE |

Track A and Track B share the **same random initialization** (epoch_000 is identical).

## Verification Setup

| Parameter | Value |
|-----------|-------|
| References per checkpoint | 10 (first 10 correctly classified test samples, mixed classes) |
| Epsilon values | 0.01, 0.02, 0.05, 0.1, 0.2 |
| Alpha (NAP confidence) | 0.95, 0.99 |
| NAP rule types | ALWAYS_ON, ALWAYS_OFF (unary only) |
| Vacuous check | Local: B(ref, eps) ∩ NAP feasibility via Marabou |

### Solvers

| Solver | Timeout | NAP mechanism | Strengths |
|--------|---------|---------------|-----------|
| Marabou (LP-SMT) | 300s | Direct bound constraints | Handles large eps, random networks |
| alpha-beta-CROWN (BaB) | 120s | manual_cuts in BaB | 4.8x faster median |

### Task Counts

| Config | Tasks | Why |
|--------|-------|-----|
| Baseline | 500 | 10 checkpoints x 10 refs x 5 eps |
| NAP | 1000 | Same x 2 alpha values (0.95, 0.99) |
| **Total** | **1500** per solver | |

## Experiment Types

| Experiment | Solver | Description |
|------------|--------|-------------|
| `step3_full` | Marabou | Main experiment: baseline + NAP + vacuous checks |
| `step3_seed42` | Marabou | Reproducibility (Track A, seed=42) |
| `step3_trades` | Marabou | TRADES adversarial training comparison |
| `step3_abcrown_nopgd` | alpha-beta-CROWN | Cross-validation (PGD disabled, clean results) |
| `step3_abcrown_pgdfilter` | alpha-beta-CROWN | PGD bug confirmation (514 invalid SAT) |

## Reports

- **[All_Tracks_Aggregated.md](All_Tracks_Aggregated.md)** — Full results tables, cross-solver comparison, key findings

### Per-Track Reports

- [Track_A.md](Track_A.md) — Track A (70 epochs, 5 checkpoints)
- [Track_B.md](Track_B.md) — Track B (100 epochs, 5 checkpoints)

### Per-Solver Reports

- [Alpha_Beta_CROWN.md](Alpha_Beta_CROWN.md) — alpha-beta-CROWN results, PGD bug analysis, solver comparison

---

## Key Findings

### 1. NAP Verifiable Region Grows During Training

| Checkpoint | Training % | BL max eps | NAP max eps | Expansion |
|------------|-----------|------------|-------------|-----------|
| epoch_000 | 0% (random) | — (0/100 verified) | 0.01 | ∞ |
| ~25% | 25% | 0.01 | 0.02 | 2x |
| ~50% | 50% | 0.02 | 0.05 | 2.5x |
| **~75%** | **75%** | **0.02** | **0.2** | **10x** |
| ~100% | 100% | 0.02 | 0.05 | 2.5x |

### 2. Random Networks: Zero BL Robustness, Non-zero NAP Robustness

- Baseline epoch_000: **0/100** verified
- NAP epoch_000 (Marabou): **32/200** genuinely verified at eps=0.01

### 3. 75% → 100% Degradation = Specification Rigidity

- Training curves show no overfitting (val_loss plateau)
- NAP rules increase ~5% from 75% to 100%
- More rules → smaller B(ref,eps) ∩ NAP → more vacuous cases

### 4. Two Solvers Agree

| Solver | NAP genuine total | Handles eps≥0.05 | Median time |
|--------|------------------|-------------------|-------------|
| Marabou | **213** | Yes (up to 0.2) | 33.3s |
| alpha-beta-CROWN | 147 | No (all T/o) | **6.9s** |

### 5. alpha-beta-CROWN PGD Bug

PGD attack ignores NAP cuts. 514 "SAT" results from PGD are adversarials outside NAP region; disabling PGD yields 0 SAT.

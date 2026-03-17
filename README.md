# Marabou Verification on VNNCOMP2025 - Specifications

## Overview steps

1. Deploy the Verifier(Marabou) and Benchmarks(VNNCOMP2025 benchmarks) on the remote cluster.
2. Run verification to Benchmark models to see which models can be verified by Marabou.
3. Take the verifiable models and to see how the specification works(A(not A)->B(not B), ALWAYS_ON/ALWAYS_OFF, etc.)

    3.1 extract the activation patterns

    3.2 mine the rules(specifications) from the activation patterns

    3.3 verify the rules with Marabou by /epsilon ball verification(Like the Table 3 in the paper [1])
4. See the results.

## Setting up

Models: The models are from the VNNCOMP2025 benchmark.

Verifier: We take the Marabou for verifications.

## Marabou Reachability

We ran Marabou against all VNNCOMP2025 benchmark categories (3371 instances total) 
to assess which models are tractable for NAP-based verification.

**Verified by Marabou (1245/3371 total):**

| Benchmark | Verified | Notes |
|-----------|----------|-------|
| acasxu_2023 | 156/186 | Fully-connected ReLU MLPs — primary NAP target |
| safenlp_2024 | 800/1000 | NLP classifiers; ε-ball semantics differ |
| dist_shift_2023 | 62/72 | MNIST distribution-shift; generative architecture |
| collins_rul_cnn_2022 | 43/62 | Time-series CNN; partial format errors |
| malbeware | 50/150 | Binary image classification; discrete inputs |
| sat_relu | 49/98 | SAT-encoded networks; non-standard semantics |
| metaroom_2023 | 19/100 | Robotic perception CNNs; high timeout rate |

The models not listed here represents the verification by Marabou failed because of structure errors or something else.
For example the VGG, YOLO and ViT.

**NAP applicability:** NAP requires (1) standard ReLU MLP architecture and (2) continuous 
ε-ball perturbation properties with available training data. Among verifiable benchmarks, 
only **acasxu_2023** satisfies all criteria. Two CIFAR-10 models from the `relusplitter` 
category (`oval21-benchmark_cifar_deep/wide_kw`) also qualify and are currently under 
experiment on the cluster.


## Rules Mined

In experiments, we mined the rules from the activation patterns of the verifiable models with some specific types.

 - Implication rules
    - A -> B
    - not A -> not B
    - A -> not B
    - not A -> B
 - ALWAYS_ON
 - ALWAYS_OFF
 - ALWAYS_ON AND ALWAYS_OFF

With different settings of the parameters:
 - Alpha 0.90 0.95 0.99


Alpha is the confidence level, 


## Verification on Rules

For each sample, we verify robustness against all target classes under different 
perturbation radii using Marabou, with a **per-query timeout of 120 seconds**.

Parameters:
- **ε (epsilon):** 0.02, 0.05, 0.10, 0.20  — perturbation radius
- **Timeout:** 120s per Marabou query
- **Samples:** 1 sample per class



## Results

Y(Yes): The sample is found to have NO counterexample.(UNSAT)
N(No): The sample is found to have counterexample.(SAT)
T(Timeout): The rule is not verified due to timeout.

Detailed Results now can be found in the `model_reports` directory.

### Per-Property Reports (NEW)

A second set of reports is available in [`model_reports_per_property/`](./model_reports_per_property/README.md), with three key differences from the original `model_reports/`:

| Aspect | `model_reports/` | `model_reports_per_property/` |
|--------|-----------------|------------------------------|
| Reference point | Random training sample | Property midpoint |
| Rule mining | Per-model (shared across properties) | Per-property |
| Rule cap | max_rules=3000, max_unary=3000 | No limit (all rules) |

See the [per-property aggregated report](./model_reports_per_property/All_Models_Aggregated.md) for headline numbers.

### MNIST Reports (NEW)

MNIST verification reports are available in [`mnist_reports/`](./mnist_reports/README.md), covering three fully-connected ReLU models of increasing depth:

| Model | Architecture | Best NAP Y% (ε=0.02, α=0.90) |
|-------|-------------|-------------------------------|
| mnist256x2 | 784→256→256→10 | **99.7%** |
| mnist256x4 | 784→(256)×4→10 | **72.2%** |
| mnist256x6 | 784→(256)×6→10 | **57.5%** |

See the [MNIST aggregated report](./mnist_reports/All_Models_Aggregated.md) for full results.


### Experiment Types

| Label | Meaning |
|-------|---------|
| `full-rule` | All rule types mined from all layers combined. |
| `layer_L0L1` … `layer_L4L5` | Per-layer-pair rule verification (ablation by layer pair). |
| `impl_ablation` | Implication directions tested separately (`A->B`, `A->!B`, `!A->B`, `!A->!B`). |

# Model Reports Index

Auto-generated per-model verification reports.

| Model | Experiments | Struct |
|-------|-------------|--------|
| [N1,1](./N1_1.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,2](./N1_2.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,3](./N1_3.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,4](./N1_4.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,5](./N1_5.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,6](./N1_6.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,7](./N1_7.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,8](./N1_8.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N1,9](./N1_9.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,1](./N2_1.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,2](./N2_2.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,3](./N2_3.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,4](./N2_4.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,5](./N2_5.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,6](./N2_6.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,7](./N2_7.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,8](./N2_8.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N2,9](./N2_9.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,1](./N3_1.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,2](./N3_2.md) | full-rule, impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,3](./N3_3.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,4](./N3_4.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,5](./N3_5.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,6](./N3_6.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,7](./N3_7.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,8](./N3_8.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N3,9](./N3_9.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,1](./N4_1.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,2](./N4_2.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,3](./N4_3.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,4](./N4_4.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,5](./N4_5.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,6](./N4_6.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,7](./N4_7.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,8](./N4_8.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N4,9](./N4_9.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,1](./N5_1.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,2](./N5_2.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,3](./N5_3.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,4](./N5_4.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,5](./N5_5.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,6](./N5_6.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,7](./N5_7.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,8](./N5_8.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [N5,9](./N5_9.md) | full-rule, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, layer_old_L0L1, layer_old_L1L2, layer_old_L2L3, layer_old_L3L4, layer_old_L4L5 | ✅ |
| [cifar_deep_kw](./cifar_deep_kw.md) | full-rule | ❌ |
| [cifar_wide_kw](./cifar_wide_kw.md) | full-rule | ❌ |

Additional CIFAR reports:
- [cifar_deep_kw](./model_reports/cifar_deep_kw.md)
- [cifar_wide_kw](./model_reports/cifar_wide_kw.md)

## Key Insights

1. In ACAS full-rule experiments, baseline (`none`) remains `0/3024` robust queries at all alpha levels.
2. `3024` is the total ACAS query count per rule and per alpha, aggregated over all 45 reported models (`24×80 + 9×64 + 9×48 + 3×32 = 3024`).
3. The strongest full-rule family is consistently early-layer implication (`Impl L0→L1`):  
   `903/3024 (29.9%)` at `alpha=0.90`, `353/3024 (11.7%)` at `alpha=0.95`, and `12/3024 (0.4%)` at `alpha=0.99`.
4. Implication-type ablation (partial coverage: 11 models at `alpha=0.90`, 5 at `0.95`, 4 at `0.99`) shows:
   - `alpha=0.90`: `!A->!B` = `379/3280 (11.6%)`, `A->!B` = `330/3280 (10.1%)`, `A->B` = `156/3280 (4.8%)`, `!A->B` = `130/3280 (4.0%)`.
   - `alpha=0.95`: `A->!B` = `32/1120 (2.9%)`, `!A->!B` = `28/1120 (2.5%)`, `A->B` = `0/1120`, `!A->B` = `0/1120`.
   - `alpha=0.99`: all four implication types are `0`.
5. Rule utility is concentrated in early layers: `L0→L1` dominates, while `L4→L5` drops to `2.2%` (`alpha=0.90`), `0.3%` (`0.95`), and `0.0%` (`0.99`).
6. CIFAR results are very strong in the completed runs: all reported queries are robust (`100% Y`) for `cifar_deep_kw` (`alpha=0.90/0.95/0.99`) and `cifar_wide_kw` (`alpha=0.90/0.95`) with the baseline, they are already robust even just with the baseline.


## Notes

The results now are not completed, what and it will get updated when new results released from the cluster.

### Still Running
 Update time: March 17th, 2026
 - MNIST per-layer and impl ablation experiments (partially complete).
 - mnist256x4: 9 full-rule experiments missing (classes 0, 1, 8, 9 at some alpha values).


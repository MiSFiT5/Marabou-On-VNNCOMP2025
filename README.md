# Verification on VNNCOMP2025

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

### Experiment Types

| Label | Meaning |
|-------|---------|
| `full-rule` | All rule types mined from **all layers combined**: ALWAYS_ON, ALWAYS_OFF, ALWAYS_ON+OFF, and all 4 implication directions. Acts as the main comparison baseline. |
| `layer_L0L1` … `layer_L4L5` | Only rules from one **adjacent layer pair** — layer ablation to find which layer contributes most. All 45 models have this. |
| `impl_ablation` | Each implication direction (A→B, A→¬B, ¬A→B, ¬A→¬B) tested **separately per layer pair** — fine-grained ablation. Only 11 models completed (SLURM array was limited to first 20 tasks, of which 11 produced results). |

> **Why do some models lack `full-rule`?** The `nap_acasxu.batch` was submitted with `--array=0-19`, covering only the first 20 models (N1,1–N3,2). Models N3,3–N5,9 only have layer ablation data. Re-running with `--array=0-44` would cover all 45 models.

### Model Reports Index

| Model | Experiments | Struct |
|-------|-------------|--------|
| [N1,1](N1_1.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,2](N1_2.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,3](N1_3.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,4](N1_4.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,5](N1_5.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,6](N1_6.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,7](N1_7.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,8](N1_8.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N1,9](N1_9.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,1](N2_1.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,2](N2_2.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,3](N2_3.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,4](./N2_4.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,5](./N2_5.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,6](./N2_6.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,7](./N2_7.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,8](./N2_8.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N2,9](./N2_9.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N3,1](N3_1.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N3,2](N3_2.md) | impl_ablation, layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5, full-rule | ✅ |
| [N3,3](N3_3.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N3,4](N3_4.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N3,5](N3_5.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N3,6](N3_6.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N3,7](N3_7.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N3,8](N3_8.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N3,9](N3_9.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,1](N4_1.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,2](N4_2.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,3](N4_3.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,4](N4_4.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,5](N4_5.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,6](N4_6.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,7](N4_7.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,8](N4_8.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N4,9](N4_9.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,1](N5_1.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,2](N5_2.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,3](N5_3.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,4](N5_4.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,5](N5_5.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,6](N5_6.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,7](N5_7.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,8](N5_8.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |
| [N5,9](N5_9.md) | layer_L0L1, layer_L1L2, layer_L2L3, layer_L3L4, layer_L4L5 | ✅ |


## Conclusion

For CIFAR models currently we only have 2 models verified by Marabou. And the broad one is still on the run. The Deep one illustrates that it is already robust to the perturbation with epsilon 0.20. See CIFAR Deep model [cifar_deep_kw.md](./model_reports/cifar_deep_kw.md).


Implication and ALWAYS_ON/ALWAYS_OFF rules are useful in some models with limited epsilon
Implication rules are more powerful who is mined from the first 2 layers analyzed so far

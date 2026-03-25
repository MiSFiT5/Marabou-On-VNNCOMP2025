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

- `Y`: no counterexample found for that query (`UNSAT`).
- `N`: a counterexample was found (`SAT`).
- `T/o`: the query hit the timeout.

### Report Families

- [`model_reports/`](./model_reports/README.md) — legacy sample-based ACAS/CIFAR reports. One reference sample per model, rule cap `max_rules=3000`, `max_unary=3000`.
- [`model_reports_per_property/`](./model_reports_per_property/README.md) — per-property ACAS reports. Property midpoint reference, no rule cap, deduplicated baseline counts.
- [`mnist_reports/`](./mnist_reports/README.md) — per-class MNIST reports with both deduplicated-query and row-level summaries.
- [`random_init_mnist_reports/`](./random_init_mnist_reports/README.md) — random-init MNIST baseline-only study.
- [`rq2_box_sandwich_reports/`](./rq2_box_sandwich_reports/README.md) — RQ2 volume-estimation study.
- [`The RQ1 problems .md`](./The%20RQ1%20problems%20.md) — RQ1 sample-generation notes and visualizations.

### Experiment Types

| Label | Meaning |
|-------|---------|
| `full-rule` | All rule types mined from all layers combined. |
| `layer_L0L1` … `layer_L4L5` | Per-layer-pair rule verification (new per-rule format). |
| `layer_old_L0L1` … `layer_old_L4L5` | Legacy Row1/3 layer-ablation format used only in the old sample-based reports. |
| `impl_ablation` | Implication directions tested separately (`A->B`, `A->!B`, `!A->B`, `!A->!B`). |

### Random-Init MNIST Reports

A companion random-initialization study is available in [`random_init_mnist_reports/`](./random_init_mnist_reports/README.md). It reuses the same VNN-COMP MNIST models, reinitializes them with standard weight initialization schemes, keeps only `correct-by-luck` samples, and then runs baseline-only Marabou verification at `epsilon=0.05`.

| Model | Random accuracy | Eligible classes | Y | N | T/o |
|-------|------------------|------------------|---|---|-----|
| mnist256x4 | 2832/60000 (4.72%) | 6/10 | 0 | 73 | 89 |
| mnist256x6 | 6291/60000 (10.49%) | 6/10 | 0 | 0 | 162 |

Important caveat: for each model, the `he/xavier/lecun` variants produced identical predictions in this exact zero-bias ReLU setup, so this should be read as a numeric-scale ablation rather than three independent random classifiers.

### RQ2: NAP Volume Estimation

A separate experiment estimates how large the NAP region is in the full input space \([0,1]^{784}\) using two independent methods on `mnist256x4` (`alpha=0.95`):

| Method | Classes | Total Samples | NAP Hits | Conclusion |
|--------|---------|--------------|----------|------------|
| Box Sandwich (IBP + MC) | 10/10 | 2,000,000 | 0 | Volume ≈ 0 |
| Beta Mixture IS | 8/10 | 4,000,000 | 0 | Volume ≈ 0 |

Both methods confirm that the NAP region occupies an effectively zero fraction of the uniform input hypercube, which is consistent with the curse of dimensionality (784D input versus an approximately 20D data manifold).

## Key Findings

### Legacy Sample-Based ACAS (`model_reports/`)

- Baseline (`none`) stays `0/3024` row-level verified queries at all alpha values.
- `3024` is the row-level denominator per rule family and per alpha across the 45 sample-based ACAS reports (`24×80 + 9×64 + 9×48 + 3×32 = 3024`).
- The strongest full-rule family is `Impl L0→L1`: `903/3024 (29.9%)` at `alpha=0.90`, `353/3024 (11.7%)` at `alpha=0.95`, and `12/3024 (0.4%)` at `alpha=0.99`.

### ACAS Per-Property (`model_reports_per_property/`)

- Deduplicated baseline is `59/1432 (4.1%)` at `ε=0.02`, `17/1432 (1.2%)` at `ε=0.05`, and `0` at `ε=0.10/0.20`.
- `Any verified` over unique `(model, property)` pairs is `96/185 (51.9%)` at `α=0.90, ε=0.02`, `94/185 (50.8%)` at `α=0.95, ε=0.02`, and `52/186 (28.0%)` at `α=0.99, ε=0.02`.
- `N2,9 prop8` is still missing full-rule runs at `α=0.90` and `α=0.95`, which is why the denominator is `185` there instead of `186`.

### MNIST (`mnist_reports/`)

- Deduplicated baseline at `ε=0.02` is `63/90` for `mnist256x2`, `31/72` for `mnist256x4`, and `36/90` for `mnist256x6`.
- Best full-rule row-level Y% at `ε=0.02, α=0.90` is `99.7%` (`mnist256x2`), `72.2%` (`mnist256x4`), and `57.5%` (`mnist256x6`).
- `mnist256x4` is still incomplete: classes `1` and `8` are missing in the current results.

### CIFAR (`model_reports/`)

- Completed sample-based runs remain `100% Y` for `cifar_deep_kw` (`alpha=0.90/0.95/0.99`) and `cifar_wide_kw` (`alpha=0.90/0.95`).

## Status

Update time: March 25th, 2026
- ACAS per-property fixied report
- Update 2 tracks x 5 checkpoints x 10 reference samples x 5 epsilon sets x 2 alpha sets experiments 

- Update NAP with Alpha-Beta Crown (in previous experiments it is too slow to verify with implications)

- RQ2 Box Sandwich is complete (10/10 classes). Beta IS is 8/10 complete (`c0` and `c5` failed on the cluster).

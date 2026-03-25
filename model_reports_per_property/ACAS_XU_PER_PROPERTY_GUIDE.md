# ACAS Xu Per-Property NAP Verification: Complete Explanatory Guide

> This document provides a self-contained, detailed explanation of the ACAS Xu per-property
> verification experiment. It is written to be readable by someone who has never seen this
> project before. Every number that appears in the result tables is traced back to its origin.

---

## Table of Contents

1. [Background: What is ACAS Xu?](#1-background-what-is-acas-xu)
2. [Background: What is NAP?](#2-background-what-is-nap)
3. [Experiment Design Overview](#3-experiment-design-overview)
4. [Step-by-Step Pipeline](#4-step-by-step-pipeline)
5. [Glossary of Every Column and Number](#5-glossary-of-every-column-and-number)
6. [How Denominators Are Computed (With Full Worked Example)](#6-how-denominators-are-computed-with-full-worked-example)
7. [Understanding the Aggregated Results](#7-understanding-the-aggregated-results)
8. [Understanding the Per-Model Reports](#8-understanding-the-per-model-reports)
9. [Experiment Variants Explained](#9-experiment-variants-explained)
10. [Why Some Numbers Differ Between Tables](#10-why-some-numbers-differ-between-tables)
11. [Key Findings and How to Interpret Them](#11-key-findings-and-how-to-interpret-them)

---

## 1. Background: What is ACAS Xu?

**ACAS Xu** (Airborne Collision Avoidance System for Unmanned aircraft) is a family of 45
neural networks used for collision avoidance decisions. Each network is identified as
**N(i,j)** where `i` ranges from 1 to 5 and `j` ranges from 1 to 9.

- **Architecture:** Each network is a fully-connected ReLU MLP with **5 input neurons**,
  **5 output neurons**, and **6 hidden layers of 50 neurons each**.
- **5 inputs:** Distance to intruder, angles, speeds (continuous values).
- **5 outputs:** Scores for 5 advisory actions (Clear-of-Conflict, Weak Left, Weak Right,
  Strong Left, Strong Right). The action with the **lowest** score is the recommended advisory.
- **Model files:** Named like `ACASXU_run2a_5_2_batch_2000.onnx` (this is model N5,2).

### ACAS Xu Properties

The VNNCOMP benchmark defines **10 safety properties** (prop1 through prop10) for ACAS Xu.
Each property specifies:

1. An **input region** (a hyperrectangle/box in the 5-dimensional input space), and
2. An **output constraint** (e.g., "advisory X should not be recommended").

**Not every model is subject to every property.** The VNNCOMP specification assigns a subset
of properties to each model. Across all 45 models, there are **186 unique (model, property)
pairs** in total.

For example:
- Model N1,1 has 6 properties assigned to it.
- Model N5,2 has 4 properties assigned to it (prop1, prop2, prop3, prop4).
- Most models have 4 properties.

---

## 2. Background: What is NAP?

**NAP (Neural Activation Patterns)** is a technique that extracts behavioral rules from a
trained neural network. The core idea:

1. **Sample many inputs** from a region of interest.
2. **Record the activation pattern** of every ReLU neuron (on/off) for each sample.
3. **Mine rules** that hold consistently across samples.
4. **Add these rules as extra constraints** to the verification query, which helps the
   SMT solver (Marabou) prune the search space and verify properties faster.

### Types of NAP Rules

There are two major categories:

#### Unary Rules (per-neuron)
- **ALWAYS_ON:** Neuron `k` in layer `l` is always activated (output > 0) for all samples
  of a given class.
- **ALWAYS_OFF:** Neuron `k` in layer `l` is always deactivated (output = 0) for all samples
  of a given class.
- **ALWAYS_ON+OFF:** The union of both ALWAYS_ON and ALWAYS_OFF rules applied together.

#### Implication Rules (neuron-to-neuron, across adjacent layers)
These express relationships between a neuron `A` in layer `l` and a neuron `B` in layer `l+1`:
- **A -> B:** If neuron A is on, then neuron B is on.
- **A -> not B:** If neuron A is on, then neuron B is off.
- **not A -> B:** If neuron A is off, then neuron B is on.
- **not A -> not B:** If neuron A is off, then neuron B is off.

Implication rules are mined for each pair of **adjacent layers**. Since ACAS Xu has 6 hidden
layers (L0 through L5), there are 5 adjacent layer pairs:
- L0->L1, L1->L2, L2->L3, L3->L4, L4->L5

When we write "Impl L2->L3", it means implication rules mined between hidden layer 2 and
hidden layer 3.

### The Alpha (α) Parameter

Alpha is a **confidence threshold** for rule mining. A rule is only kept if it holds for
at least α fraction of the samples.

- **α = 0.90:** A rule must hold for >= 90% of samples. Produces the **most** rules
  (more permissive), but some rules may not be universally true.
- **α = 0.95:** Must hold for >= 95%. Fewer but more reliable rules.
- **α = 0.99:** Must hold for >= 99%. Fewest but most stringent rules.

**Tradeoff:** Lower alpha gives more NAP constraints to help the solver, but they are less
certain to be truly universal (so verification may succeed on more queries but the rules
might not be sound for all inputs). Higher alpha gives fewer constraints that are more
reliable.

---

## 3. Experiment Design Overview

This experiment answers the question: **Does adding NAP rules help Marabou verify more
ACAS Xu properties, and by how much?**

### What Changed From the Old ("Legacy") Experiment

| Aspect | Old Experiment (`model_reports/`) | New Per-Property Experiment (this directory) |
|--------|-----------------------------------|----------------------------------------------|
| **Reference point** | One random training sample per model | **Midpoint of the property's input box** |
| **Rule mining scope** | Shared across all properties of a model | **Separate mining per property** |
| **Rule cap** | max 3000 rules | **No cap** (all mined rules used) |
| **Granularity** | 1 report per model | **1 report per (model, property) pair** |
| **Sample source** | Training dataset | **Uniform samples within the property's input region** |

### Why Per-Property?

In the old experiment, rules were mined from a single training sample and applied to all
properties. This is suboptimal because:
- Different properties define different input regions.
- The activation patterns in one region may be very different from another.
- Mining rules specifically within each property's input box produces more relevant
  constraints for that specific verification task.

### Experimental Parameters

| Parameter | Values | Meaning |
|-----------|--------|---------|
| ε (epsilon) | 0.02, 0.05, 0.10, 0.20 | Radius of the L-infinity perturbation ball around the reference point |
| α (alpha) | 0.90, 0.95, 0.99 | Confidence threshold for rule mining |
| Timeout | 120 seconds | Maximum time allowed for Marabou to solve one query |
| Reference point | Property midpoint | Center of the VNNLIB input box for each property |

---

## 4. Step-by-Step Pipeline

The experiment runs through 4 stages. Here is exactly what happens:

### Stage 1: Generate Property Data

**Script:** `nap_verify/generate_acasxu_data.py`

For each (model, property) pair:
1. Read the VNNLIB file to get the **input box** (lower and upper bounds for each of the
   5 input dimensions).
2. Compute the **midpoint** of this box: `reference_point = (lower + upper) / 2` for each
   dimension.
3. Sample many points uniformly within the box.
4. Run each sampled point through the network to get its **predicted class** (argmin of
   outputs for ACAS Xu, since lowest score = recommended action).
5. Save the sampled points and their labels.

**Key output:** A set of labeled samples and a reference point for each (model, property).

### Stage 2: Mine NAP Rules

**Script:** `nap_verify/encode_dataset_to_class_nap.py`

For each (model, property) pair:
1. Take the labeled samples from Stage 1.
2. Group samples by their predicted class.
3. For each class that appears in the samples, mine:
   - ALWAYS_ON rules (neurons always activated for this class)
   - ALWAYS_OFF rules (neurons always deactivated for this class)
   - Implication rules between adjacent layers
4. Apply the alpha threshold to filter rules.

**Critical detail:** Not all 5 ACAS Xu classes will necessarily appear in every property's
input region. For example, if the input box for prop4 of model N5,2 only produces class-4
predictions, then rules are only mined for class 4.

**Key output:** A set of NAP rules for each (model, property, alpha) combination.

### Stage 3: Run Verification Queries

**Script:** `nap_verify/verify_table3.py`

This is where the actual verification happens. For each (model, property) pair, the script
constructs and runs Marabou queries.

**What is one verification query?**

A single query asks Marabou:

> "Given:
> - The neural network model
> - An input constrained to be within an ε-ball around the reference point
> - (Optionally) NAP rules as additional constraints
>
> Does there exist an input in this ε-ball such that `output[target_label] >= output[true_class]`?"

In other words: **Can the network be fooled into preferring a different action (`target_label`)
over the correct action (`true_class`) within a small perturbation of the reference point?**

**The query tuple is:** `(property, epsilon, true_class, target_label, rule_type)`

For each property and each epsilon:
- For each true_class that appeared in the sampled data:
  - For each of the 5 possible target_labels:
    - If `target_label == true_class`: skip (trivial, stored as `-`).
    - Otherwise: run Marabou with and without NAP rules.

**Results for each query:**
- **Y (Yes, verified):** Marabou proves UNSAT -- no adversarial input exists. The network
  is robust for this particular (true_class, target_label) pair.
- **N (No, not verified):** Marabou finds a counterexample (SAT) -- an adversarial input
  exists.
- **T/o (Timeout):** Marabou could not decide within 120 seconds.

### Stage 4: Aggregate Into Reports

**Script:** `generate_per_property_reports.py`

Reads all CSV result files and generates markdown reports with summary tables.

**Key aggregation rules:**
1. **Exclude self-target rows:** Rows where `target_label == true_class` (stored as `-`)
   are not real queries and are excluded from all counts.
2. **Deduplicate shared rows:** Baseline and unary rule results appear identically in
   multiple layer-pair experiment directories. They are counted only once.
3. **Compute Y/total:** For each cell, numerator = count of `Y` results, denominator =
   count of valid results (Y + N + T/o).

---

## 5. Glossary of Every Column and Number

### In the Summary Tables

| Column/Label | Meaning |
|-------------|---------|
| **Rule** | The NAP rule type being tested (or `none (baseline)` for no rules) |
| **ε=0.02** | Results at perturbation radius 0.02. Format: `Y/total (percentage)` |
| **ε=0.05** | Results at perturbation radius 0.05 |
| **ε=0.10** | Results at perturbation radius 0.10 |
| **ε=0.20** | Results at perturbation radius 0.20 |
| **Total Y%** | Percentage of verified queries **across all 4 epsilons combined** |
| **Y** | Number of queries where Marabou proved the property (UNSAT) |
| **N** | Number of queries where Marabou found a counterexample (SAT) |
| **T/o** | Number of queries that timed out (120s) |
| **Total** | Y + N + T/o (total valid queries) |
| **Verified %** | Y / Total × 100% |

### In the Aggregated Report

| Label | Meaning |
|-------|---------|
| **Total CSV rows** | Raw number of rows in all table3_results.csv files (1,217,220) |
| **Verification rows** | Rows after excluding skipped/`-` entries (973,776) |
| **Unique models** | 45 (N1,1 through N5,9) |
| **Unique properties** | Properties 1-10 defined in the VNNCOMP benchmark |
| **Unique (model, prop) pairs** | 186 -- the total number of (model, property) combinations |
| **Any verified** | At least one NAP rule type achieves `Y` for a given (model, property, epsilon) |
| **Props** column | Number of properties assigned to this model in VNNCOMP |
| **Full-Rule Groups** | Number of experiment groups run for full-rule (= props × 3 alphas, minus missing) |
| **Best Row-Level Y%** | The highest verification rate achieved by any rule type at ε=0.02, α=0.90 |

### The "Any Verified" Metric

This is a **model-property level** metric, not a query-level one:

For each (model, property) pair at a given (alpha, epsilon):
- Look across all rule types (baseline, ALWAYS_ON, ALWAYS_OFF, ALWAYS_ON+OFF, all 5
  implication layer pairs).
- If **any** of them achieves at least one `Y` query, count this (model, property) as
  "verified."

So `96/185 (51.9%)` at α=0.90, ε=0.02 means: out of 185 (model, property) pairs
with data available, 96 had at least one query verified by at least one NAP rule type.

The denominator is 185 instead of 186 because `N2,9 prop8` is missing full-rule runs
at α=0.90.

### The 1432 and 1420 Denominators

These appear in the aggregated Rule Type Breakdown table and are frequently confusing.

**Where 1432 comes from:**

1432 is the total number of valid queries across all 186 (model, property) pairs at one
fixed epsilon. It is computed by summing up the valid queries for each (model, property)
pair:

```
For each (model, property) pair:
    valid_queries = (number of true classes appearing in that property's samples) × 4

Total: sum across all 186 pairs = 1432
```

The `× 4` comes from the fact that ACAS Xu has 5 output classes, and for each true_class
we test against the other 4 target classes (excluding self-target).

**Where 1420 comes from:**

1420 = 1432 - 12. At α=0.90 and α=0.95, the (model, property) pair `N2,9 prop8` is
**missing** from the experiment results. This pair contributes 12 valid queries per
epsilon (3 true classes × 4 targets). So:

- α=0.99: denominator = **1432** (all pairs present)
- α=0.90: denominator = **1420** (1432 - 12, because N2,9 prop8 is missing)
- α=0.95: denominator = **1420** (same reason)

---

## 6. How Denominators Are Computed (With Full Worked Example)

### Example: Model N5,2

Model N5,2 has 4 properties in VNNCOMP. When we sample points within each property's
input box and run them through the network, we observe these predicted classes:

| Property | Classes observed in samples | How many true classes? |
|----------|----------------------------|----------------------|
| prop1 | {0, 2, 4} | 3 |
| prop2 | {0, 2, 4} | 3 |
| prop3 | {2, 3, 4} | 3 |
| prop4 | {4} | 1 |

**For one fixed epsilon and one fixed rule type:**

For each true_class, we test 4 target labels (the 5 outputs minus the true class itself).

| Property | Valid queries per epsilon | Calculation |
|----------|--------------------------|-------------|
| prop1 | 12 | 3 classes × 4 targets |
| prop2 | 12 | 3 classes × 4 targets |
| prop3 | 12 | 3 classes × 4 targets |
| prop4 | 4 | 1 class × 4 targets |
| **Total** | **40** | |

So every summary cell for N5,2 has denominator **40**.

### Why "Total Y%" Uses 160

The "Total Y%" column aggregates across all 4 epsilons:

```
Total Y% = (Y at ε=0.02 + Y at ε=0.05 + Y at ε=0.10 + Y at ε=0.20)
            / (40 + 40 + 40 + 40)
          = sum_of_Y / 160
```

For example, if ALWAYS_ON achieves 8/40 at ε=0.02 and 0/40 at all other epsilons:
```
Total Y% = 8 / 160 = 5.0%
```

### Detailed Query Expansion for prop1 of N5,2

Take prop1 (true classes: {0, 2, 4}), one fixed rule, ε=0.02:

| true_class | target_label | Is it self-target? | Counted? |
|------------|--------------|-------------------|----------|
| 0 | 0 | Yes (self) | No (stored as `-`) |
| 0 | 1 | No | **Yes** |
| 0 | 2 | No | **Yes** |
| 0 | 3 | No | **Yes** |
| 0 | 4 | No | **Yes** |
| 2 | 0 | No | **Yes** |
| 2 | 1 | No | **Yes** |
| 2 | 2 | Yes (self) | No (stored as `-`) |
| 2 | 3 | No | **Yes** |
| 2 | 4 | No | **Yes** |
| 4 | 0 | No | **Yes** |
| 4 | 1 | No | **Yes** |
| 4 | 2 | No | **Yes** |
| 4 | 3 | No | **Yes** |
| 4 | 4 | Yes (self) | No (stored as `-`) |

- Total rows in CSV: 15 (3 true classes × 5 targets)
- Self-target rows (excluded): 3
- **Valid queries: 12** (3 × 4)

---

## 7. Understanding the Aggregated Results

The file `All_Models_Aggregated.md` contains the experiment-wide summary.

### Baseline Table

```
| ε    | Y  | N    | T/o | Total | Verified % |
|------|-----|------|-----|-------|------------|
| 0.02 | 59  | 1364 | 9   | 1432  | 4.1%       |
| 0.05 | 17  | 1393 | 22  | 1432  | 1.2%       |
| 0.10 | 0   | 1409 | 23  | 1432  | 0.0%       |
| 0.20 | 0   | 1411 | 21  | 1432  | 0.0%       |
```

**What this means:** Without any NAP rules (pure Marabou baseline), only 59 out of 1432
queries are verified at the smallest perturbation (ε=0.02). At larger perturbations, even
fewer or none are verified. This is the starting point that NAP aims to improve.

**Where 1432 comes from:** See Section 5 above. It is the sum of valid queries across all
186 (model, property) pairs.

### Full-Rule NAP "Any Verified" Table

```
| α    | ε=0.02          | ε=0.05          | ε=0.10          | ε=0.20          |
|------|-----------------|-----------------|-----------------|-----------------|
| 0.90 | 96/185 (51.9%)  | 82/185 (44.3%)  | 33/185 (17.8%)  | 18/185 (9.7%)   |
| 0.95 | 94/185 (50.8%)  | 33/185 (17.8%)  | 19/185 (10.3%)  | 14/185 (7.6%)   |
| 0.99 | 52/186 (28.0%)  | 20/186 (10.8%)  | 19/186 (10.2%)  | 13/186 (7.0%)   |
```

**How to read:** At α=0.90 and ε=0.02, 96 out of 185 (model, property) pairs had at
least one query verified by some NAP rule type. This is a dramatic improvement over the
baseline's 4.1% query-level rate.

**Why 185 vs 186:** At α=0.90 and α=0.95, the pair N2,9-prop8 has no results yet, so
the denominator is 185. At α=0.99, all 186 pairs have results.

**Key observations:**
- Lower α (0.90) gives the best results because more rules are available.
- Smaller ε (0.02) gives the best results because smaller perturbation regions are
  easier to verify.
- Even at α=0.99 and ε=0.02, NAP improves from baseline (28% vs 4.1%).

### Rule Type Breakdown Table

```
| Rule Type        | α=0.90            | α=0.95            | α=0.99            |
|------------------|--------------------|--------------------|-------------------|
| ALWAYS_OFF       | 487/1420 (34.3%)   | 387/1420 (27.3%)   | 174/1432 (12.2%)  |
| ALWAYS_ON        | 335/1420 (23.6%)   | 236/1420 (16.6%)   | 155/1432 (10.8%)  |
| ALWAYS_ON+OFF    | 530/1420 (37.3%)   | 415/1420 (29.2%)   | 192/1432 (13.4%)  |
| Impl L0->L1      | 246/1420 (17.3%)   | 114/1420 (8.0%)    | 72/1432 (5.0%)    |
| Impl L1->L2      | 333/1420 (23.5%)   | 186/1420 (13.1%)   | 71/1432 (5.0%)    |
| Impl L2->L3      | 413/1420 (29.1%)   | 288/1420 (20.3%)   | 121/1432 (8.4%)   |
| Impl L3->L4      | 414/1420 (29.2%)   | 334/1420 (23.5%)   | 133/1432 (9.3%)   |
| Impl L4->L5      | 286/1420 (20.1%)   | 198/1420 (13.9%)   | 86/1432 (6.0%)    |
```

**What this means:** Each row shows how many of the ~1420 queries (at ε=0.02) are
verified when using only that specific rule type.

**Key observations:**
- **ALWAYS_ON+OFF is the best unary rule** (37.3%), because it combines both ON and OFF
  constraints, giving Marabou the most neuron-level information.
- **Impl L3->L4 is the best implication rule** (29.2%), closely followed by L2->L3 (29.1%).
- **Impl L0->L1 is the weakest implication rule** (17.3%), suggesting that the first
  hidden layer has less discriminative activation patterns.
- All rule types dramatically outperform the baseline (4.1%).

### Speedup Analysis

```
- Both verify Y: 76 unique queries
- Mean speedup: 675.6x (median 345.8x)
- Mean baseline time: 18.54s
- Mean NAP time: 0.17s
- Baseline fails, NAP verifies: 2121 unique queries
```

**What this means:**
- For the 76 queries that both baseline and NAP verify successfully, NAP is on average
  675x faster (18.54s vs 0.17s). The NAP rules prune the solver's search space so
  dramatically that verification becomes nearly instant.
- 2121 queries that baseline fails on (returns N or T/o) are successfully verified by NAP.
  These are "rescue queries" -- cases where NAP makes previously impossible verification
  possible.

---

## 8. Understanding the Per-Model Reports

Each model file (e.g., `N5_2.md`) contains:

### Header Section

```
Model file: ACASXU_run2a_5_2_batch_2000.onnx
Properties covered: prop1, prop2, prop3, prop4 (4 total)
Experiment types: full_rule, per_layer, impl_ablation
```

This tells you which ONNX file was verified, which properties it has, and what experiment
types were run.

### Query Accounting Table

This is the **key to understanding all denominators** in this model's tables:

```
| Property | True class(es) | Valid queries per ε | Formula                          |
|----------|----------------|---------------------|----------------------------------|
| prop1    | 0, 2, 4        | 12                  | 3 true classes × 4 non-self targets |
| prop2    | 0, 2, 4        | 12                  | 3 true classes × 4 non-self targets |
| prop3    | 2, 3, 4        | 12                  | 3 true classes × 4 non-self targets |
| prop4    | 4              | 4                   | 1 true classes × 4 non-self targets |
| Total    | -              | 40                  | 12 + 12 + 12 + 4                  |
```

**Every `Y/40` you see in N5,2's tables comes from this: 40 valid queries per epsilon.**

### Summary Tables

Three sets of tables, one per experiment type (full_rule, per_layer, impl_ablation),
each subdivided by alpha (0.90, 0.95, 0.99).

**Example row:**
```
| ALWAYS_ON+OFF (α=0.9) | 16/40 (40.0%) | 0/40 (0.0%) | 0/40 (0.0%) | 0/40 (0.0%) | 10.0% |
```

Reading this:
- **Rule:** ALWAYS_ON+OFF rules at α=0.9
- **ε=0.02:** 16 out of 40 queries verified (40%)
- **ε=0.05 through ε=0.20:** 0 verified (perturbation too large)
- **Total Y%:** (16+0+0+0)/(40+40+40+40) = 16/160 = 10.0%

---

## 9. Experiment Variants Explained

### Full-Rule

**What:** All rule types from all layers are mined and combined. Each rule type is tested
individually, but all layers contribute to the rule pool.

**Purpose:** This is the "main" experiment showing the full power of each NAP rule category.

**Tables in report:** One table per alpha (0.90, 0.95, 0.99), with rows for each rule type.

### Per-Layer

**What:** Rules are mined from only one pair of adjacent layers at a time (L0L1, L1L2,
L2L3, L3L4, L4L5). This is an ablation study to understand which layers contribute most.

**Important detail about deduplication:**
In the raw experiment data, baseline (no-rule) and unary (ALWAYS_ON, ALWAYS_OFF) results
are **recomputed identically** for each layer pair. This means the same baseline result
appears 5 times (once per layer-pair directory). The report generator **deduplicates** these
so you only see the unique result once. That is why per-layer denominators match full-rule
denominators (both are 40 for N5,2, not 5×40=200).

### Impl Ablation

**What:** Each of the 4 implication directions (A->B, A->!B, !A->B, !A->!B) is tested
separately for each layer pair.

**Purpose:** To understand which direction of implication is most helpful. This gives
5 layer pairs × 4 directions = 20 separate implication rule types, plus the 3 unary types
and baseline.

**Example row:**
```
| Impl L2->L3 [A->!B] (α=0.9) | 8/40 (20.0%) | 0/40 (0.0%) | ...
```
This means: using only the "A implies NOT B" rules between layers 2 and 3.

---

## 10. Why Some Numbers Differ Between Tables

This is the most confusing aspect of the current reports. Here are the common sources
of discrepancy:

### 10.1 Full-Rule vs Per-Layer for the Same Rule Type

**Example from N5,2 at α=0.9:**
- Full-Rule: `Impl L1->L2` = 12/40 at ε=0.02
- Per-Layer: `Impl L1->L2` = 12/40 at ε=0.02

These **should** match because the same queries are run. If they differ slightly, it is
because:
- Full-rule and per-layer experiments may have been run at different times on the cluster.
- Marabou's internal heuristics can produce slightly different results near the timeout
  boundary.
- Rounding differences in rare timeout-boundary cases.

### 10.2 Denominator 1420 vs 1432

- **1432** = total valid queries across all 186 (model, property) pairs
- **1420** = 1432 minus 12 queries from N2,9-prop8 (which is missing at α=0.90 and α=0.95)
- At **α=0.99**, all 186 pairs have data, so the denominator is 1432

### 10.3 Denominator 185 vs 186

Same reason: N2,9-prop8 is missing at α=0.90/0.95, so only 185 unique (model, property)
pairs have data.

### 10.4 Per-Layer Implication vs Full-Rule Implication Small Differences

In the N5,2 report, some implication results differ slightly between full-rule and per-layer:
- Full-Rule Impl L1->L2 at ε=0.05: **1/40**
- Per-Layer Impl L1->L2 at ε=0.05: **2/40**

This happens because per-layer experiments isolate each layer pair, which changes the
solver's constraint set. When all rule types are loaded together (full-rule), the solver
may behave differently near timeout boundaries. Both are valid; they represent slightly
different verification configurations.

### 10.5 "Any Verified" vs Individual Rule Rates

"Any verified" (51.9% at α=0.90, ε=0.02) is much higher than any individual rule type's
rate (best is 37.3%) because different rule types verify different queries. A (model,
property) pair is counted as "any verified" if **any** rule type succeeds on **any** query
within it.

---

## 11. Key Findings and How to Interpret Them

### Finding 1: NAP Dramatically Improves Verification

- **Baseline:** 4.1% of queries verified at ε=0.02
- **Best NAP rule (ALWAYS_ON+OFF, α=0.90):** 37.3% of queries verified at ε=0.02
- **Any NAP rule:** 51.9% of (model, property) pairs have at least one verified query

**Interpretation:** Adding NAP activation pattern constraints to the SMT solver makes it
possible to verify properties that were previously unreachable.

### Finding 2: Unary Rules (ALWAYS_ON+OFF) Are the Strongest Single Rule Type

ALWAYS_ON+OFF consistently outperforms any single implication layer pair. This is because:
- Unary rules directly constrain individual neurons across ALL layers.
- They are simple for the solver to propagate.
- Combining ON and OFF gives the most complete picture of neuron behavior.

### Finding 3: Middle-Layer Implications Are More Informative

Among implication rules, L2->L3 and L3->L4 are strongest, while L0->L1 is weakest. This
suggests that the network's decision-relevant features are computed in the middle layers,
where activation patterns are most discriminative.

### Finding 4: Lower Alpha Gives More Power (But Less Soundness)

- α=0.90 verifies 51.9% of pairs
- α=0.95 verifies 50.8%
- α=0.99 verifies only 28.0%

Lower alpha produces more rules, giving the solver more constraints to work with. However,
these rules only hold with 90% confidence, meaning they may not be universally true.

### Finding 5: NAP Provides Massive Speedup

When both baseline and NAP can verify a query, NAP is **675x faster on average** (0.17s vs
18.54s). This is because the NAP constraints eliminate most of the solver's branching
space.

### Finding 6: Verification Degrades With Larger Perturbation

At ε=0.02, NAP achieves 51.9% "any verified." At ε=0.20, only 9.7%. Larger perturbation
balls are inherently harder to verify because the solver must rule out adversarial inputs
in a much larger region.

---

## Appendix A: File Structure Quick Reference

```
model_reports_per_property/
├── ACAS_XU_PER_PROPERTY_GUIDE.md    <-- This document
├── COUNTS_AND_PIPELINE.md           <-- Technical pipeline details and count formulas
├── README.md                        <-- Index of per-model reports
├── All_Models_Aggregated.md         <-- Experiment-wide summary tables
├── N1_1.md ... N5_9.md              <-- 45 individual model reports
```

## Appendix B: Complete Mapping of Models to Properties

Each model is assigned a subset of the 10 VNNCOMP properties. Most models have 4
properties, but some have 5 or 6. The total across all 45 models is 186 (model, property)
pairs.

Models with more than 4 properties:
- N1,1: 6 properties
- N1,9: 5 properties
- N2,9: 5 properties
- N3,3: 5 properties
- N4,5: 5 properties

All other models: 4 properties each.

## Appendix C: Tracing a Specific Number End-to-End

**Claim from aggregated report:** `530/1420 (37.3%)` for ALWAYS_ON+OFF at α=0.90, ε=0.02.

**Tracing this number:**

1. **1420** = Total valid queries across 185 (model, property) pairs (186 minus N2,9-prop8).
   Each pair contributes `(# true classes) × 4` queries. Sum = 1420.

2. **530** = Out of those 1420 queries, 530 returned `Y` (UNSAT) when ALWAYS_ON+OFF rules
   at α=0.90 were added to Marabou.

3. **37.3%** = 530 / 1420 × 100%.

**To verify this yourself:**
- Open each N*_*.md file.
- In the Full-Rule, α=0.9 table, find the `ALWAYS_ON+OFF (α=0.9)` row, `ε=0.02` column.
- Read the numerator (Y count) from each.
- Sum all 45 numerators. You should get 530.
- Sum all 45 denominators. You should get 1420.

---

*End of guide. Last updated: 2026-03-25.*

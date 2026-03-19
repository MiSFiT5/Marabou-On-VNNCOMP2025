# ACAS Xu Per-Property Counts And Pipeline

> Generated/documented on 2026-03-19

This note explains two things:

1. What one verification `query` means in this repository.
2. How counts such as `8/40 (20.0%)` are produced.

## The 4-stage pipeline

### Stage 1: Generate ACAS Xu property data

Script: `nap_verify/generate_acasxu_data.py`

For each `(model, property)` pair, the script:

- reads the VNNLIB input box for that ACAS Xu property,
- samples many points inside that property box,
- records the midpoint of the box as the `reference_point`.

For the per-property reports in this directory, verification later uses the
property midpoint as the center point.

Important consequence:

- a `property` here is first treated as an input region,
- not yet as one final verification query.

### Stage 2: Mine rules from the sampled property data

Script: `nap_verify/encode_dataset_to_class_nap.py`

The sampled points are labeled by the network. Rule mining then builds classwise
NAP rules from the labels that actually appear in that property's sampled data.

Important consequence:

- a property does not necessarily contain all 5 ACAS Xu classes,
- only the classes that actually appear in `labels.npy` get rules and later
  participate in verification.

Example for model `N5,2`:

- `prop1` has sampled labels `{0, 2, 4}`
- `prop2` has sampled labels `{0, 2, 4}`
- `prop3` has sampled labels `{2, 3, 4}`
- `prop4` has sampled labels `{4}`

So `prop1` and `prop2` use true classes `0, 2, 4`, while `prop4` uses only
true class `4`.

### Stage 3: Expand one property into many verification queries

Script: `nap_verify/verify_table3.py`

For each available true class, the script:

- uses the property midpoint as the local center point,
- fixes one rule table, such as `ALWAYS_ON (α=0.9)`,
- loops over each `epsilon`,
- loops over every output `target_label`.

One CSV row in `table3_results.csv` is one attempted verification query with:

`(table, epsilon, true_class, target_label)`

The solver checks whether there exists an input inside the `epsilon` box around
the center point such that:

`output[target_label] >= output[true_class]`

Interpretation of the stored result:

- `Y`: the query is proved UNSAT, so no such adversarial target exists
- `N`: the query is SAT, so such a target exists
- `T/o`: timeout
- `-`: self-target case `target_label == true_class`, not a real query

Important consequence:

- `target_label == true_class` is never counted in denominators,
- each true class contributes 4 valid target labels, not 5.

### Stage 4: Aggregate CSV rows into report tables

Script: `Verification_on_VNNCOMP2025/Marabou-On-VNNCOMP2025/generate_per_property_reports.py`

The report generator keeps only rows with result in:

- `Y`
- `N`
- `T/o`

Rows with `-` are excluded because they are not real verification queries.

Therefore, for any summary cell:

- denominator = number of valid query rows
- numerator = number of those rows whose result is `Y`

## What exactly is a query?

In this report directory, one query means:

`(property, epsilon, true_class, target_label != true_class, rule)`

So the denominator in `Y/total` is counting queries, not:

- properties,
- experiment directories,
- layer pairs,
- or whole models.

## Why does one property produce multiple queries?

Because the verification script expands along two axes:

1. true class
2. target label

For ACAS Xu there are 5 output labels. Once `true_class` is fixed, only the
other 4 labels are valid targets.

So for one property, one rule, one epsilon:

`valid queries = (# true classes present in this property) x 4`

## Worked example: why `N5,2` has `8/40 (20.0%)`

The report file is:

- `model_reports_per_property/N5_2.md`

For model `N5,2`, the per-property true classes are:

| Property | True class(es) present | Valid queries per epsilon |
|----------|------------------------|---------------------------|
| prop1 | `0, 2, 4` | `3 x 4 = 12` |
| prop2 | `0, 2, 4` | `3 x 4 = 12` |
| prop3 | `2, 3, 4` | `3 x 4 = 12` |
| prop4 | `4` | `1 x 4 = 4` |

Therefore, for any fixed rule and any fixed epsilon:

`total valid queries = 12 + 12 + 12 + 4 = 40`

That is where the denominator `40` comes from.

### The `prop1` slice in full detail

Take:

- model `N5,2`
- property `prop1`
- rule `ALWAYS_ON (α=0.9)`
- epsilon `0.02`

The raw rows in `table3_results.csv` are:

| true_class | target_label | result |
|------------|--------------|--------|
| 0 | 0 | `-` |
| 0 | 1 | `N` |
| 0 | 2 | `N` |
| 0 | 3 | `N` |
| 0 | 4 | `N` |
| 2 | 0 | `Y` |
| 2 | 1 | `Y` |
| 2 | 2 | `-` |
| 2 | 3 | `Y` |
| 2 | 4 | `Y` |
| 4 | 0 | `N` |
| 4 | 1 | `N` |
| 4 | 2 | `N` |
| 4 | 3 | `N` |
| 4 | 4 | `-` |

Reading this table:

- there are 3 true classes: `0, 2, 4`
- each true class has 5 target labels listed
- one of those 5 is the self-target row and is stored as `-`
- so only 4 targets per true class are valid queries

Hence:

- raw rows = `3 x 5 = 15`
- valid queries = `3 x 4 = 12`
- `Y` rows = `4`

So `prop1` contributes `4/12` for this `(rule, epsilon)` pair.

### Summing across the four properties

For `ALWAYS_ON (α=0.9)` at `epsilon = 0.02`:

- `prop1`: `4/12`
- `prop2`: `4/12`
- `prop3`: `0/12`
- `prop4`: `0/4`

Add numerators and denominators separately:

- numerator = `4 + 4 + 0 + 0 = 8`
- denominator = `12 + 12 + 12 + 4 = 40`

So the report shows:

`8/40 (20.0%)`

## Why the final column is different

In summary tables, the last column `Total Y%` is computed across all 4 epsilon
values together.

For `N5,2`, if a rule shows:

- `8/40` at `0.02`
- `0/40` at `0.05`
- `0/40` at `0.10`
- `0/40` at `0.20`

then the final percentage is:

`8 / (40 + 40 + 40 + 40) = 8 / 160 = 5.0%`

So the last column is not repeating `8/40`; it is aggregating over all epsilons.

## Why old per-layer summaries could show `200`

In the raw per-layer experiment directories, baseline and unary tables were
rerun once per layer pair. Since there are 5 layer pairs, the same query could
appear 5 times in the union of CSV files.

That creates misleading counts such as:

`200 = 5 x 40`

The report generator in this directory now deduplicates those shared rows so
per-layer denominators reflect unique queries, not repeated executions.

## Short formulas

For one property, one rule, one epsilon:

`valid queries = (# true classes present) x 4`

For one model, one rule, one epsilon:

`valid queries = sum over properties of ((# true classes present in that property) x 4)`

For one summary cell:

`Y/total = (# rows with result Y) / (# rows with result in {Y, N, T/o})`

## Where to look in the generated reports

- Each model report contains a top-level count explanation and per-model
  denominator table.
- Each property section contains a line `Valid queries per ε: ...`.

Example:

- `model_reports_per_property/N5_2.md`


# Step 4 — Unary ON/OFF Layer Ablation

> Preview update for the `Random_to_welltrained` reports
> Marabou exact results only

- **NAP family:** unary `ALWAYS_ON / ALWAYS_OFF`
- **Tracks:** A and B
- **Checkpoints per track:** 5 (`0%, 25%, 50%, 75%, 100%`)
- **Positive refs per checkpoint:** 20 fixed refs (selected from checkpoints with progress >= 25%; see below)
- **Layer configs:** `baseline` (no NAP), `last1` through `last7`
- **Runtime alpha:** `0.95`, `0.99` (not applicable to baseline)
- **Epsilon:** `0.01`, `0.02`, `0.05`
- **Solver encoding (ablation):** single disjunctive misclassification constraint per query, 600s timeout
- **Solver encoding (baseline):** per-target-class solving, 300s per target, up to 2700s total (from `step4_marabou_v2`)

Layer configs:

| Config | Layers used |
|--------|-------------|
| `last1` | `L6` only |
| `last2` | `L5-L6` |
| `last3` | `L4-L6` |
| `last4` | `L3-L6` |
| `last5` | `L2-L6` |
| `last6` | `L1-L6` |
| `last7` | `L0-L6`, all unary rules |

Data sources:

- `generated/step4_unary_ablation_full_A/results/coverage.csv` (layer ablation)
- `generated/step4_unary_ablation_full_B/results/coverage.csv` (layer ablation)
- `generated/step4_marabou_v2/results/coverage.csv` (baseline, same fixed refs)

Track A has 3 missing verify tasks out of 4200. They are all at `eps=0.02`, progress `50%`, and do not affect the `eps=0.01` conclusions.

### Reference selection

The 20 fixed refs per track are selected by `step4_unified_refs.py`:

1. Exclude `epoch_000` (random init, progress < 25%) from the intersection.
2. Take MNIST test samples that are correctly classified by **all** remaining checkpoints (25%, 50%, 75%, 100%).
3. Rank by dataset index and select the first 20.

Because `epoch_000` is not part of the intersection, the random-init checkpoint misclassifies 15/20 refs in both tracks. Only 5 refs are eligible for verification at `epoch_000`. For all checkpoints with progress >= 25%, misclassified = 0 and all 20 refs are eligible.

**The main tables below show only progress >= 25%.** The `epoch_000` row is included in a separate appendix for completeness.

### Solver encoding note

This ablation uses a **single disjunctive constraint** encoding (all 9 target classes in one query, 600s total timeout). The earlier `step4_marabou.py` used **per-target-class solving** (up to 9 separate queries, 300s each, up to 2700s total). This means some cases that were resolved as adversarial in the old solver may appear as timeout here. The tables below use the 600s full ablation run.

---

## 1. How to Read the Tables

Each table cell is:

> `genuine / verified / timeout`

where:

- **genuine**: verified AND non-vacuous (the strongest result);
- **verified**: Marabou returned UNSAT for the adversarial query, including vacuous cases;
- **timeout**: Marabou did not return a final answer within 600s.

The denominator is always 20 fixed refs. An asterisk `*` marks a row with one missing verification task. When adversarial counterexamples are found, `N=<count>` is appended to the cell.

For baseline (no NAP constraints), genuine = verified always (no vacuity possible). Baseline data comes from `step4_marabou_v2` which uses per-target encoding (up to 2700s).

**No adversarial counterexamples (SAT) were returned** in the layer-ablation configs under the 600s disjunctive encoding. All non-verified eligible cases are timeouts. However, the baseline (per-target solver, up to 2700s) found adversarial cases at `eps=0.02` and `eps=0.05`. Therefore, "no SAT returned" in ablation configs should not be read as "no adversarial examples exist"; it reflects the solver timeout limit.

---

## 2. Aggregated Final-Checkpoint Reading

### `eps=0.01`

| Config | Track A, `alpha=0.95` | Track A, `alpha=0.99` | Track B, `alpha=0.95` | Track B, `alpha=0.99` |
|--------|----------------------:|----------------------:|----------------------:|----------------------:|
| baseline | 17/17/3 | — | 18/18/2 | — |
| `last1` | 17/18/2 | 18/18/2 | 20/20/0 | 20/20/0 |
| `last4` | 18/19/1 | 19/19/1 | 19/20/0 | 20/20/0 |
| `last7` | 9/19/1 | 19/19/1 | 10/20/0 | 20/20/0 |

### Direct reading

- Baseline (no NAP) at the final checkpoint verifies `17/20` (Track A) and `18/20` (Track B). Adding even `last1` NAP at `alpha=0.99` matches or exceeds this.
- At `alpha=0.99`, `last1` is already close to `last7`: final genuine is `18/20` vs `19/20` on Track A, and `20/20` vs `20/20` on Track B.
- At `alpha=0.95`, full-network `last7` is misleading if vacuous cases are counted: Track A is `9/19/1`, Track B is `10/20/0`.
- The clean small-radius setting is therefore not simply "use more layers"; it is closer to "use high-confidence deep rules."

### `eps=0.02`

| Config | Track A, `alpha=0.95` | Track A, `alpha=0.99` | Track B, `alpha=0.95` | Track B, `alpha=0.99` |
|--------|----------------------:|----------------------:|----------------------:|----------------------:|
| baseline | 3/3/17 | — | 4/4/16 | — |
| `last1` | 3/3/17 | 3/3/17 | 5/5/15 | 4/4/16 |
| `last2` | 3/3/17 | 3/3/17 | 5/5/15 | 5/5/15 |
| `last4` | 7/7/13 | 5/5/15 | 7/8/12 | 7/7/13 |
| `last7` | 6/10/10 | 3/3/17 | 10/12/8 | 5/5/15 |

### Direct reading

- Baseline at `eps=0.02` final: `3/3/17` (A) and `4/4/16` (B). Most NAP configs match or exceed this.
- `eps=0.02` is much harder than `eps=0.01`.
- `last1` and `last2` do not fail because Marabou finds adversarial examples. They fail by timeout under this solver configuration.
- Mid-to-late layer sets, especially `last4`, can help at `eps=0.02`.
- The result is less clean than `eps=0.01`; it does not support a universal "last layer only" rule.
- Note: the baseline per-target solver found adversarial at `eps=0.02` (A 75%: N=2, B 50%: N=1) but these do not appear in the final checkpoint row.

---

## 3. `eps=0.01`: Verified vs Genuine (progress >= 25%)

![Layer ablation total verified, eps=0.01](step4_followup_assets/layer_verified_eps001.png)

![Layer ablation genuine verified, eps=0.01](step4_followup_assets/layer_genuine_eps001.png)

### Exact checkpoint tables

#### Track A

| Progress | baseline | `last1` (0.95) | `last1` (0.99) | `last4` (0.95) | `last4` (0.99) | `last7` (0.95) | `last7` (0.99) |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 15/15/5 | 18/18/2 | 15/15/5 | 16/19/1 | 15/15/5 | 10/19/1 | 15/16/4 |
| 50% | 15/15/5 | 17/17/3 | 15/15/5 | 18/19/1 | 16/16/4 | 12/19/1 | 16/17/3 |
| 75% | 17/17/3 | 17/18/2 | 18/18/2 | 18/19/1 | 18/18/2 | 8/19/1 | 19/19/1 |
| 100% | 17/17/3 | 17/18/2 | 18/18/2 | 18/19/1 | 19/19/1 | 9/19/1 | 19/19/1 |

<details>
<summary>Full Track A tables (all layer configs)</summary>

**Track A, `alpha=0.95`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 15/15/5 | 18/18/2 | 15/16/4 | 16/19/1 | 16/19/1 | 16/19/1 | 11/19/1 | 10/19/1 |
| 50% | 15/15/5 | 17/17/3 | 16/17/3 | 18/19/1 | 18/19/1 | 17/19/1 | 13/19/1 | 12/19/1 |
| 75% | 17/17/3 | 17/18/2 | 17/18/2 | 18/19/1 | 18/19/1 | 17/20/0 | 13/19/1 | 8/19/1 |
| 100% | 17/17/3 | 17/18/2 | 17/18/2 | 18/19/1 | 18/19/1 | 17/19/1 | 14/19/1 | 9/19/1 |

**Track A, `alpha=0.99`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 15/15/5 | 15/15/5 | 15/15/5 | 15/15/5 | 15/15/5 | 15/15/5 | 15/16/4 | 15/16/4 |
| 50% | 15/15/5 | 15/15/5 | 16/16/4 | 17/17/3 | 16/16/4 | 16/16/4 | 17/17/3 | 16/17/3 |
| 75% | 17/17/3 | 18/18/2 | 18/18/2 | 18/18/2 | 18/18/2 | 19/19/1 | 19/19/1 | 19/19/1 |
| 100% | 17/17/3 | 18/18/2 | 18/18/2 | 18/18/2 | 19/19/1 | 19/19/1 | 19/19/1 | 19/19/1 |

</details>

#### Track B

| Progress | baseline | `last1` (0.95) | `last1` (0.99) | `last4` (0.95) | `last4` (0.99) | `last7` (0.95) | `last7` (0.99) |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 14/14/6 | 15/16/4 | 13/14/6 | 14/17/3 | 14/14/6 | 11/18/2 | 13/14/6 |
| 50% | 16/16/4 | 16/17/3 | 17/17/3 | 17/18/2 | 18/18/2 | 9/19/1 | 17/17/3 |
| 75% | 18/18/2 | 20/20/0 | 20/20/0 | 19/20/0 | 20/20/0 | 10/20/0 | 20/20/0 |
| 100% | 18/18/2 | 20/20/0 | 20/20/0 | 19/20/0 | 20/20/0 | 10/20/0 | 20/20/0 |

<details>
<summary>Full Track B tables (all layer configs)</summary>

**Track B, `alpha=0.95`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 14/14/6 | 15/16/4 | 15/16/4 | 15/16/4 | 14/17/3 | 14/18/2 | 12/18/2 | 11/18/2 |
| 50% | 16/16/4 | 16/17/3 | 17/18/2 | 17/18/2 | 17/18/2 | 16/19/1 | 14/19/1 | 9/19/1 |
| 75% | 18/18/2 | 20/20/0 | 19/20/0 | 19/20/0 | 19/20/0 | 18/20/0 | 12/20/0 | 10/20/0 |
| 100% | 18/18/2 | 20/20/0 | 19/20/0 | 19/20/0 | 19/20/0 | 18/20/0 | 12/20/0 | 10/20/0 |

**Track B, `alpha=0.99`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 14/14/6 | 13/14/6 | 14/14/6 | 14/14/6 | 14/14/6 | 14/14/6 | 14/14/6 | 13/14/6 |
| 50% | 16/16/4 | 17/17/3 | 17/17/3 | 18/18/2 | 18/18/2 | 17/17/3 | 17/17/3 | 17/17/3 |
| 75% | 18/18/2 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 |
| 100% | 18/18/2 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 | 20/20/0 |

</details>

### Direct reading

- Baseline at final: `17/17/3` (A) and `18/18/2` (B). No vacuity by definition.
- At `alpha=0.99`, even `last1` matches or exceeds baseline genuine rate.
- At `alpha=0.95`, adding more layers inflates verified through vacuity: Track A final `last7` is `9/19/1` (genuine 9 < baseline 17).
- At `alpha=0.99`, vacuity is much smaller, so `genuine` and `verified` are nearly identical across all configs.

---

## 4. `eps=0.02`: Verified vs Genuine (progress >= 25%)

![Layer ablation total verified, eps=0.02](step4_followup_assets/layer_verified_eps002.png)

![Layer ablation genuine verified, eps=0.02](step4_followup_assets/layer_genuine_eps002.png)

### Exact checkpoint tables

#### Track A

| Progress | baseline | `last1` (0.95) | `last1` (0.99) | `last4` (0.95) | `last4` (0.99) | `last7` (0.95) | `last7` (0.99) |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 1/1/19 | 1/1/19 | 1/1/19 | 2/2/18 | 1/1/19 | 0/2/18 | 0/0/20 |
| 50% | 3/3/17 | 1/1/18* | 1/1/19 | 6/6/14 | 3/3/17 | 3/7/13 | 1/1/18* |
| 75% | 3/3/15, N=2 | 3/3/17 | 3/3/17 | 6/6/14 | 5/5/15 | 4/8/12 | 3/3/17 |
| 100% | 3/3/17 | 3/3/17 | 3/3/17 | 7/7/13 | 5/5/15 | 6/10/10 | 3/3/17 |

<details>
<summary>Full Track A tables (all layer configs)</summary>

**Track A, `alpha=0.95`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 1/1/19 | 1/1/19 | 1/1/19 | 1/1/19 | 2/2/18 | 0/0/20 | 1/1/19 | 0/2/18 |
| 50% | 3/3/17 | 1/1/18* | 3/3/16* | 4/5/15 | 6/6/14 | 4/4/16 | 2/3/17 | 3/7/13 |
| 75% | 3/3/15, N=2 | 3/3/17 | 4/4/16 | 6/6/14 | 6/6/14 | 7/7/13 | 4/4/16 | 4/8/12 |
| 100% | 3/3/17 | 3/3/17 | 3/3/17 | 6/6/14 | 7/7/13 | 7/7/13 | 6/6/14 | 6/10/10 |

**Track A, `alpha=0.99`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 1/1/19 | 1/1/19 | 1/1/19 | 1/1/19 | 1/1/19 | 0/0/20 | 0/0/20 | 0/0/20 |
| 50% | 3/3/17 | 1/1/19 | 1/1/19 | 1/1/19 | 3/3/17 | 1/1/19 | 0/0/20 | 1/1/18* |
| 75% | 3/3/15, N=2 | 3/3/17 | 3/3/17 | 3/3/17 | 5/5/15 | 3/3/17 | 3/3/17 | 3/3/17 |
| 100% | 3/3/17 | 3/3/17 | 3/3/17 | 3/3/17 | 5/5/15 | 4/4/16 | 2/2/18 | 3/3/17 |

</details>

#### Track B

| Progress | baseline | `last1` (0.95) | `last1` (0.99) | `last4` (0.95) | `last4` (0.99) | `last7` (0.95) | `last7` (0.99) |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 0/0/20 | 0/0/20 | 0/0/20 | 1/1/19 | 0/0/20 | 1/3/17 | 0/0/20 |
| 50% | 3/3/16, N=1 | 3/3/17 | 3/3/17 | 6/6/14 | 6/6/14 | 5/9/11 | 2/2/18 |
| 75% | 4/4/16 | 5/5/15 | 4/4/16 | 8/9/11 | 6/6/14 | 7/9/11 | 4/4/16 |
| 100% | 4/4/16 | 5/5/15 | 4/4/16 | 7/8/12 | 7/7/13 | 10/12/8 | 5/5/15 |

<details>
<summary>Full Track B tables (all layer configs)</summary>

**Track B, `alpha=0.95`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 0/0/20 | 0/0/20 | 0/0/20 | 0/0/20 | 1/1/19 | 1/1/19 | 0/1/19 | 1/3/17 |
| 50% | 3/3/16, N=1 | 3/3/17 | 4/4/16 | 6/6/14 | 6/6/14 | 7/7/13 | 2/4/16 | 5/9/11 |
| 75% | 4/4/16 | 5/5/15 | 5/5/15 | 5/6/14 | 8/9/11 | 11/12/8 | 8/10/10 | 7/9/11 |
| 100% | 4/4/16 | 5/5/15 | 5/5/15 | 5/5/15 | 7/8/12 | 8/8/12 | 9/11/9 | 10/12/8 |

**Track B, `alpha=0.99`**

| Progress | baseline | `last1` | `last2` | `last3` | `last4` | `last5` | `last6` | `last7` |
|----------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| 25% | 0/0/20 | 0/0/20 | 0/0/20 | 0/0/20 | 0/0/20 | 0/0/20 | 0/0/20 | 0/0/20 |
| 50% | 3/3/16, N=1 | 3/3/17 | 3/3/17 | 4/4/16 | 6/6/14 | 4/4/16 | 1/1/19 | 2/2/18 |
| 75% | 4/4/16 | 4/4/16 | 5/5/15 | 6/6/14 | 6/6/14 | 4/4/16 | 1/1/19 | 4/4/16 |
| 100% | 4/4/16 | 4/4/16 | 5/5/15 | 6/6/14 | 7/7/13 | 5/5/15 | 4/4/16 | 5/5/15 |

</details>

### Direct reading

- Baseline at `eps=0.02` found adversarial counterexamples at intermediate checkpoints (A 75%: N=2, B 50%: N=1). These are real SAT results from the per-target solver (2700s budget).
- The ablation configs (600s disjunctive) found zero adversarial; all non-verified cases are timeouts under this encoding and budget.
- Track A final `last1/last2` are only `3/3/17` for both alphas, matching baseline.
- Track B final `last1/last2` are stronger, but still only `4-5` genuine out of 20.
- The best final rows are from deeper subsets:
  - Track A: `last4` or `last5`, up to `7/7/13` at `alpha=0.95`;
  - Track B: `last7` reaches `10/12/8` at `alpha=0.95`, while `last4` reaches `7/7/13` at `alpha=0.99`.

---

## 5. `eps=0.05`

At `eps=0.05`, both genuine and verified are always zero across all checkpoints (progress >= 25%), both alphas, and all layer configs (including baseline).

All non-verified cases are timeouts, except baseline at B 75% which found 2 adversarial (N=2). The current Marabou setup cannot resolve useful certificates at this radius.

---

## 6. Solver Encoding Comparison

Two solver encodings are used in this report on the same 20 fixed refs:

| Aspect | Ablation (last1-last7) | Baseline (from `step4_marabou_v2`) |
|--------|--------------|-------------------|
| Encoding | Single disjunction (all 9 targets) | Per-target-class (up to 9 separate queries) |
| Timeout | 600s per query | 300s per target (up to 2700s total) |
| Adversarial found | 0 | 6 (at eps=0.02 and eps=0.05) |

The 6 baseline adversarial cases all required > 600s of solver time (875s to 3070s). This confirms that the ablation's 600s budget is too short to find these adversarial counterexamples. The ablation timeouts at `eps=0.02` are not evidence of absence — they are evidence of insufficient solver time.

## 7. Appendix: `epoch_000` (random init)

At `epoch_000`, 15/20 fixed refs are misclassified by the random-init model (the refs were selected from trained checkpoints). Only 5 refs are eligible for positive-ref verification.

Among those 5 eligible refs at `eps=0.01`:

| Config range | Track A, `alpha=0.95` | Track A, `alpha=0.99` | Track B, `alpha=0.95` | Track B, `alpha=0.99` |
|-------------|----------------------:|----------------------:|----------------------:|----------------------:|
| `last1-last2` | 0/0/5 | 0/0/5 | 0/0/5 | 0/0/5 |
| `last3` | 1/1/4 | 1/1/4 | 1/1/4 | 0/0/5 |
| `last4` | 5/5/0 | 4/4/1 | 5/5/0 | 3/3/2 |
| `last5-last7` | 3-5/5/0 | 5/5/0 | 3-5/5/0 | 5/5/0 |

At `eps=0.02` and `eps=0.05`, all 5 eligible refs timeout across all configs at `epoch_000`.

---

## 8. Time Consumption of the 600s Ablation Verify Tasks

Runtime statistics are computed from the 600s full ablation verify JSON files:

- `generated/step4_unary_ablation_full_A/results/verify/*.json`
- `generated/step4_unary_ablation_full_B/results/verify/*.json`

`misclassified` rows are skipped before Marabou solving and record zero runtime, so they are excluded from the solver-time statistics below. The `overall` columns therefore mean all solver-executed verify tasks, i.e. `UNSAT` plus timeout tasks. In this 600s ablation run, Marabou returned **no SAT/adversarial result** for any layer-ablation query, so every `SAT` count is zero.

The CSV version of this table is saved as:

- `markdown/step4_followup_assets/layer_ablation_600s_time_by_checkpoint_alpha.csv`

| Track | Checkpoint | Progress | Alpha | UNSAT n | UNSAT mean | UNSAT median | SAT n | SAT mean | SAT median | Overall n | Overall mean | Overall median |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | `epoch_000` | 0% | 0.95 | 21 | 40.10s | 7.65s | 0 | — | — | 105 | 519.51s | 611.79s |
| A | `epoch_000` | 0% | 0.99 | 20 | 99.56s | 71.10s | 0 | — | — | 105 | 532.95s | 610.15s |
| A | `epoch_018` | 25% | 0.95 | 137 | 45.86s | 8.63s | 0 | — | — | 420 | 427.02s | 601.40s |
| A | `epoch_018` | 25% | 0.99 | 111 | 13.74s | 8.86s | 0 | — | — | 420 | 455.02s | 603.06s |
| A | `epoch_035` | 50% | 0.95 | 158 | 32.34s | 7.59s | 0 | — | — | 418 | 391.23s | 600.90s |
| A | `epoch_035` | 50% | 0.99 | 122 | 41.71s | 8.63s | 0 | — | — | 419 | 444.88s | 602.01s |
| A | `epoch_052` | 75% | 0.95 | 170 | 30.74s | 7.20s | 0 | — | — | 420 | 374.83s | 600.65s |
| A | `epoch_052` | 75% | 0.99 | 152 | 28.30s | 8.04s | 0 | — | — | 420 | 399.30s | 601.43s |
| A | `epoch_070` | 100% | 0.95 | 173 | 23.23s | 7.36s | 0 | — | — | 420 | 367.06s | 601.06s |
| A | `epoch_070` | 100% | 0.99 | 153 | 26.12s | 7.86s | 0 | — | — | 420 | 396.83s | 601.44s |
| B | `epoch_000` | 0% | 0.95 | 21 | 59.34s | 11.50s | 0 | — | — | 105 | 527.83s | 615.80s |
| B | `epoch_000` | 0% | 0.99 | 18 | 94.34s | 110.63s | 0 | — | — | 105 | 557.98s | 615.97s |
| B | `epoch_025` | 25% | 0.95 | 125 | 41.75s | 10.90s | 0 | — | — | 420 | 443.14s | 601.98s |
| B | `epoch_025` | 25% | 0.99 | 98 | 29.78s | 11.83s | 0 | — | — | 420 | 477.95s | 603.23s |
| B | `epoch_050` | 50% | 0.95 | 167 | 30.89s | 10.18s | 0 | — | — | 420 | 379.96s | 601.52s |
| B | `epoch_050` | 50% | 0.99 | 144 | 35.92s | 11.10s | 0 | — | — | 420 | 414.24s | 602.45s |
| B | `epoch_075` | 75% | 0.95 | 196 | 41.68s | 10.02s | 0 | — | — | 420 | 344.61s | 600.50s |
| B | `epoch_075` | 75% | 0.99 | 170 | 37.52s | 10.79s | 0 | — | — | 420 | 378.19s | 601.04s |
| B | `epoch_100` | 100% | 0.95 | 194 | 40.61s | 10.26s | 0 | — | — | 420 | 346.24s | 600.54s |
| B | `epoch_100` | 100% | 0.99 | 176 | 24.59s | 10.87s | 0 | — | — | 420 | 364.72s | 601.30s |

Direct reading:

- Verified/UNSAT tasks are usually fast once they are solved: most medians are around `7-12s`.
- The overall medians are close to `600s` because timeout cases dominate the unresolved mass.
- There are no SAT rows to summarize in this 600s ablation run; the SAT mean and median are therefore undefined rather than zero.
- Track A at 50% has `418/419` solver tasks instead of `420` because of the three missing verify JSONs noted above.

---

## 9. Data-First Summary

1. For `eps=0.01`, `alpha=0.99`, using only the final layer already exceeds baseline: `last1` reaches `18/18/2` on Track A final and `20/20/0` on Track B final, vs baseline `17/17/3` and `18/18/2`.
2. For `eps=0.01`, `alpha=0.95`, all-layer `last7` is misleading if vacuous cases are counted: Track A final is `9/19/1`, Track B final is `10/20/0`. The genuine rate is **worse** than baseline.
3. For `eps=0.02`, the result is timeout-limited. Non-verified cases are timeouts under the 600s disjunctive encoding. Baseline (per-target solver, up to 2700s) found adversarial at this radius.
4. For `eps=0.02`, mid-to-late configs can help. `last4` is a cleaner representative than `last1/last2` in several final rows, and exceeds baseline genuine rate.
5. For `eps=0.05`, no config (including baseline) gives useful verified or genuine mass.

The safest final statement is:

> In trained networks, most of the small-radius unary ON/OFF signal is already present in the final layers. At `alpha=0.99`, even `last1` exceeds the baseline genuine rate. Full-network unary rules can inflate total verified rates through vacuity, especially at `alpha=0.95`, where genuine can drop below baseline. At larger radius, the bottleneck is solver timeout; the baseline per-target solver found adversarial counterexamples at `eps=0.02` (requiring 875-3070s), which the ablation's 600s disjunctive encoding cannot recover.

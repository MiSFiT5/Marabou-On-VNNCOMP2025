# Unary ON/OFF and Implication Families on Fixed Refs

This is a standalone supplement to `report.md`.

Its purpose is now slightly broader than the first version:

1. keep the same Step 4 fixed-reference setting;
2. compare unary `ALWAYS_ON / ALWAYS_OFF` with several implication families;
3. explicitly include the new compressed `L0→L6` implication chain results;
4. stay inside exact Marabou evidence only.

## 0. Scope and Comparison Boundary

This supplement uses only **Step 4 exact fixed-reference Marabou** results.

### Unary baseline + unary NAP

- `Random_Initialized_NN/generated/step4_marabou_v2/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_marabou_v2/results/rejection_summary.csv`

### Implication: single last layer pair `L4L5`

- `Random_Initialized_NN/generated/step4_implication_A_L4L5_allrules/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_B_L4L5_allrules/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_A_L4L5_allrules/results/rejection_summary.csv`
- `Random_Initialized_NN/generated/step4_implication_B_L4L5_allrules/results/rejection_summary.csv`

### Implication: union of the last two layer pairs `L4L5_L5L6`

- `Random_Initialized_NN/generated/step4_implication_A_L4L5_L5L6/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_B_L4L5_L5L6/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_A_L4L5_L5L6/results/rejection_summary.csv`
- `Random_Initialized_NN/generated/step4_implication_B_L4L5_L5L6/results/rejection_summary.csv`

### Implication: compressed transitive chain `L0→L6`

- `Random_Initialized_NN/generated/step4_implication_A_compressed_conf0.95/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_B_compressed_conf0.95/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_A_compressed_conf0.95/results/rejection_summary.csv`
- `Random_Initialized_NN/generated/step4_implication_B_compressed_conf0.95/results/rejection_summary.csv`
- `Random_Initialized_NN/generated/step4_implication_A_compressed_conf0.99/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_B_compressed_conf0.99/results/coverage.csv`
- `Random_Initialized_NN/generated/step4_implication_A_compressed_conf0.99/results/rejection_summary.csv`
- `Random_Initialized_NN/generated/step4_implication_B_compressed_conf0.99/results/rejection_summary.csv`

The comparison rules are still strict:

- same fixed refs as Step 4;
- same exact verifier family: Marabou;
- same metrics: `verified`, `genuine verified`, `rejection`;
- main comparison window: `progress >= 25%`;
- `epoch_000` remains visible in the figures, but not the main basis for method comparison.

There are now two different notions of confidence in the compressed runs, and they must not be mixed up:

- `Compressed L0L6 c=0.95 / c=0.99` means the **rule-mining threshold** used to build the compressed CSV;
- the figure panels still use Step 4 runtime `alpha = 0.95 / 0.99`.

So a label such as:

> `Compressed L0L6 c=0.95`, panel `alpha=0.99`

means:

- rules were mined with `min_confidence = 0.95`,
- but verification was executed on the `alpha = 0.99` Step 4 task rows.

One more boundary is important:

- for all implication runs used here, `n_missing = 0`;
- therefore the limitation is not absent rows;
- the real limitation is `T/o` and, in some families, `semantic_unresolved`.

## 1. Positive Fixed Refs: Exact Verified and Exact Genuine

![Unary vs Implication Verified](report_imply_onoff_assets/fig14_imply_onoff_verified.png)

![Unary vs Implication Genuine](report_imply_onoff_assets/fig15_imply_onoff_genuine.png)

Data sources:

- `report_imply_onoff_assets/positive_progress_summary.csv`
- `report_imply_onoff_assets/positive_overall_summary.csv`

Mean exact rates over `progress >= 25%`:

| Method | Runtime alpha | `eps=0.01` verified | `eps=0.01` genuine | `eps=0.02` verified | `eps=0.02` genuine |
| --- | --- | ---: | ---: | ---: | ---: |
| Baseline | — | 81.25% | 81.25% | 13.12% | 13.12% |
| Unary ON/OFF | 0.95 | 99.38% | 46.25% | 72.50% | 53.12% |
| Unary ON/OFF | 0.99 | 93.12% | 68.75% | 35.00% | 35.00% |
| Implication `L4L5` | 0.95 | 88.75% | 68.75% | 13.75% | 12.50% |
| Implication `L4L5` | 0.99 | 86.25% | 73.75% | 12.50% | 12.50% |
| Implication `L4L5_L5L6` | 0.95 | 91.25% | 61.88% | 14.38% | 10.00% |
| Implication `L4L5_L5L6` | 0.99 | 88.75% | 68.12% | 13.12% | 13.12% |
| Compressed `L0L6 c=0.95` | 0.95 | 86.88% | 82.50% | 11.88% | 11.88% |
| Compressed `L0L6 c=0.95` | 0.99 | 88.75% | 87.50% | 11.88% | 11.88% |
| Compressed `L0L6 c=0.99` | 0.95 | 83.75% | 83.75% | 11.25% | 11.25% |
| Compressed `L0L6 c=0.99` | 0.99 | 83.75% | 83.75% | 11.25% | 11.25% |

This changes the headline relative to the earlier version of this supplement.

The most important exact fact is now:

> among the implication families, compressed `L0→L6` is the strongest positive-ref method at `eps=0.01`.

More concretely:

1. `Compressed L0L6 c=0.95`, runtime `alpha=0.99`, reaches `87.50%` mean exact genuine verified.
2. That is higher than baseline `81.25%`.
3. It is also higher than every other implication family and higher than unary NAP in exact genuine rate.

So the small-radius positive-ref ranking is no longer:

> baseline first, then implication.

It is:

> compressed `L0→L6` first, baseline second, then the other implication families, while unary ON/OFF remains strongest only in total verified mass.

## 2. What Compressed `L0→L6` Actually Improves

The compressed family is not just a slightly stronger version of `L4L5` or `L4L5_L5L6`.
It behaves qualitatively differently.

### 2.1 It almost eliminates vacuity on positive refs

For `progress >= 25%`:

| Method | Runtime alpha | `eps=0.01` vacuous count | `eps=0.02` vacuous count |
| --- | --- | ---: | ---: |
| Unary ON/OFF | 0.95 | 58 | 22 |
| Unary ON/OFF | 0.99 | 3 | 0 |
| Implication `L4L5` | 0.95 | 1 | 0 |
| Implication `L4L5` | 0.99 | 0 | 0 |
| Implication `L4L5_L5L6` | 0.95 | 4 | 0 |
| Implication `L4L5_L5L6` | 0.99 | 0 | 0 |
| Compressed `L0L6 c=0.95` | 0.95 | 0 | 0 |
| Compressed `L0L6 c=0.95` | 0.99 | 0 | 0 |
| Compressed `L0L6 c=0.99` | 0.95 | 0 | 0 |
| Compressed `L0L6 c=0.99` | 0.99 | 0 | 0 |

So compressed `L0→L6` is the cleanest semantic family in this report:

- `verified` is almost the same thing as `genuine verified`;
- the method is not winning by producing more vacuous certificates;
- it is winning by producing cleaner exact positive certificates.

### 2.2 `c=0.95` is better than `c=0.99`

This is not a runtime-`alpha` effect.  
It is a rule-mining-threshold effect.

At `eps=0.01`:

- `Compressed c=0.95` beats `Compressed c=0.99` under both runtime alphas;
- the best row is `c=0.95` with runtime `alpha=0.99`;
- `c=0.99` is cleaner than the non-compressed implication families, but not as strong as `c=0.95`.

The likely reason is visible in the underlying `verify_all.csv`:

- `c=0.95` keeps a somewhat larger compressed chain;
- the solve time stays in the same order of magnitude;
- so the extra chain coverage still pays off.

### 2.3 But its advantage is local in epsilon

At `eps=0.02`, the compressed family falls back to:

- `11.25%` to `11.88%` exact genuine,
- which is around baseline or slightly below,
- and far below unary ON/OFF.

So the correct reading is:

> compressed `L0→L6` is the best exact implication method for small-radius positive-ref certification,  
> not the best implication method at every radius.

## 3. Timeout Burden: Why `eps=0.02` Still Does Not Work

Positive-ref burden over `progress >= 25%`:

| Method | Runtime alpha | `eps=0.01` timeout / unresolved | `eps=0.02` timeout / unresolved |
| --- | --- | --- | --- |
| Unary ON/OFF | 0.95 | `1 / 27` | `44 / 9` |
| Unary ON/OFF | 0.99 | `11 / 36` | `103 / 0` |
| Implication `L4L5` | 0.95 | `18 / 29` | `138 / 2` |
| Implication `L4L5` | 0.99 | `22 / 19` | `140 / 0` |
| Implication `L4L5_L5L6` | 0.95 | `14 / 43` | `137 / 7` |
| Implication `L4L5_L5L6` | 0.99 | `18 / 33` | `139 / 0` |
| Compressed `L0L6 c=0.95` | 0.95 | `21 / 7` | `141 / 0` |
| Compressed `L0L6 c=0.95` | 0.99 | `18 / 2` | `141 / 0` |
| Compressed `L0L6 c=0.99` | 0.95 | `26 / 0` | `142 / 0` |
| Compressed `L0L6 c=0.99` | 0.99 | `26 / 0` | `142 / 0` |

This section now has a sharper interpretation than before.

At `eps=0.01`:

- compressed `L0→L6` is solver-heavy, but still usable;
- especially with `c=0.95`, runtime `alpha=0.99`, the unresolved burden is already very small;
- that is exactly why its exact genuine rate is convincing rather than fragile.

At `eps=0.02`:

- compressed `L0→L6` is almost fully timeout-dominated;
- its genuine rate does not collapse because of vacuity;
- it collapses because the exact solve budget stops being enough.

So the `eps=0.02` failure mode of compressed is different from unary:

- unary still has a usable positive-ref signal there;
- compressed mainly runs into exact solver hardness.

## 4. Misclassified Refs: Compressed `L0→L6` Is Not a Rejection Method

![Unary vs Implication Rejection](report_imply_onoff_assets/fig16_imply_onoff_rejection.png)

Data sources:

- `report_imply_onoff_assets/rejection_progress_summary.csv`
- `report_imply_onoff_assets/rejection_overall_summary.csv`

Mean exact rejection over `progress >= 25%`:

| Method | Runtime alpha | `eps=0.01` rejection | `eps=0.01` timeout | `eps=0.02` rejection | `eps=0.02` timeout |
| --- | --- | ---: | ---: | ---: | ---: |
| Unary ON/OFF | 0.95 | 100.00% | 0 | 91.25% | 7 |
| Unary ON/OFF | 0.99 | 95.00% | 4 | 31.25% | 51 |
| Implication `L4L5` | 0.95 | 65.00% | 27 | 1.25% | 79 |
| Implication `L4L5` | 0.99 | 56.25% | 34 | 0.00% | 80 |
| Implication `L4L5_L5L6` | 0.95 | 66.25% | 27 | 1.25% | 79 |
| Implication `L4L5_L5L6` | 0.99 | 58.75% | 33 | 0.00% | 80 |
| Compressed `L0L6 c=0.95` | 0.95 | 45.00% | 43 | 0.00% | 72 |
| Compressed `L0L6 c=0.95` | 0.99 | 42.50% | 45 | 0.00% | 69 |
| Compressed `L0L6 c=0.99` | 0.95 | 35.00% | 48 | 0.00% | 61 |
| Compressed `L0L6 c=0.99` | 0.99 | 35.00% | 48 | 0.00% | 65 |

This is the other half of the story, and it prevents overclaiming.

Compressed `L0→L6` is **not** the strongest implication method overall, because on misclassified refs it is actually weak.

The rejection ordering is closer to:

1. unary ON/OFF strongest by far;
2. `L4L5` and `L4L5_L5L6` intermediate;
3. compressed `L0→L6` weakest among the implication families in this slice.

So compressed `L0→L6` does not behave like a strong local-region cutter.
It behaves more like a high-precision semantic consistency constraint for already-correct refs.

That distinction matters.

If the question is:

> which NAP family most aggressively empties bad local regions around misclassified samples?

the answer remains:

> unary ON/OFF.

If the question is instead:

> which implication family gives the strongest small-radius exact genuine certificate on positive fixed refs?

the answer is now:

> compressed `L0→L6`, especially `c=0.95`.

## 5. What This Adds to the Main Story

The earlier version of this supplement concluded that unary ON/OFF should remain the clear primary story and implication should stay a narrower side note.

After adding compressed `L0→L6`, that conclusion has to be refined.

### 5.1 What remains true

1. Unary ON/OFF is still the strongest family for total verified mass.
2. Unary ON/OFF is still the strongest family for rejection on misclassified refs.
3. Unary ON/OFF is still the only family with a large usable signal at `eps=0.02`.

### 5.2 What changes

1. Compressed `L0→L6` is now the strongest implication family on positive refs at `eps=0.01`.
2. In fact, `Compressed L0L6 c=0.95`, runtime `alpha=0.99`, is the best exact genuine method in this report slice, even above baseline.
3. Therefore implication is no longer just a weaker semantic contrast to unary; compressed implication has become a real positive-ref result in its own right.

### 5.3 What still does not generalize

1. The benefit does not extend to `eps=0.02`.
2. The benefit does not transfer to rejection.
3. `c=0.95` is the only compressed setting that clearly stands out; `c=0.99` is cleaner than the old implication runs, but not the headline result.

## 6. Conclusion

The cleanest final reading is now:

1. Unary ON/OFF remains the best overall Step 4 NAP family if we care about both positive-ref gain and misclassified-ref rejection, especially beyond `eps=0.01`.
2. Compressed `L0→L6` is the best implication family, and at `eps=0.01` it is strong enough to deserve first-class status rather than a side comparison.
3. The best compressed setting in this slice is `min_confidence = 0.95`; it is stronger than `0.99` without paying a qualitatively larger solve cost.
4. Compressed `L0→L6` should be presented as:

> the strongest exact implication result for small-radius genuine verification on fixed positive refs,

not as:

> the best replacement for unary NAP in every role.

So if this supplement is used to guide the main narrative, the safest combined statement is:

> keep unary ON/OFF as the main broad NAP story,  
> but elevate compressed `L0→L6` as the main implication result, specifically for `eps=0.01` exact genuine verification.

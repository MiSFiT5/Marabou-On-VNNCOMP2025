# Part 1: Rejection Evidence for ALWAYS_ON / ALWAYS_OFF NAPs

This note focuses on the rejection side of unary NAP rules, i.e. `ALWAYS_ON` and `ALWAYS_OFF`.

Both experiments in this note use the full-layer unary NAP rule set (`L0-L6`). They are not layer-ablation experiments.

The new experiments separate two questions that were mixed together in the earlier rejection setup:

1. **Pairwise class-NAP separation:** can two different class-specific NAP regions overlap?
2. **Direct misclassification rejection:** does the current class-specific NAP reject samples that the network misclassifies?

Both questions are evaluated across the training trajectory, so the main object is not a single final number. The main object is how the NAP constraints evolve from random initialization to a trained network.

## 1.1 Pairwise Class-NAP Separation

The pairwise experiment checks every pair of MNIST classes. There are `C(10, 2) = 45` class pairs.

For a pair of classes `(i, j)`, the verifier asks whether there exists an input inside the valid MNIST box `[0,1]^784` that satisfies both class `i` NAP constraints and class `j` NAP constraints.

The interpretation is:

| Solver result | Meaning |
| --- | --- |
| `UNSAT` / disjoint | No valid MNIST input can satisfy both class NAPs. The two class-NAP regions are separated. |
| `SAT` / overlap | At least one valid MNIST input satisfies both class NAPs. The two class-NAP regions overlap. |
| `TIMEOUT` | The verifier did not resolve the pair within the time limit. |

The input box matters. The first unbounded version was not the right MNIST-domain query and produced many solver errors. The bounded version uses the natural MNIST input domain `[0,1]^784`.

Data source:

- `generated/step4_pairwise_nap_v2_A/results/pairwise_summary.csv`
- `generated/step4_pairwise_nap_v2_B/results/pairwise_summary.csv`

![Pairwise class-NAP disjointness over training](step4_followup_assets/pairwise_disjoint_progress.png)

The result is sharp:

| Track | Alpha | Random init | 25% trained | 50% trained | 75% trained | Final |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 0.95 | 0/45 | 45/45 | 45/45 | 45/45 | 45/45 |
| A | 0.99 | 0/45 | 43/45, 2 timeout | 45/45 | 45/45 | 45/45 |
| B | 0.95 | 0/45 | 45/45 | 45/45 | 45/45 | 45/45 |
| B | 0.99 | 0/45 | 45/45 | 45/45 | 45/45 | 45/45 |

This gives a clean training-progress story:

- At random initialization, all class-NAP regions overlap. The NAP constraints do not separate classes yet.
- By 25% training, class-NAP separation is almost complete.
- From 50% training onward, every resolved pair is disjoint in both tracks and both alpha settings.

The correct claim is:

> In the valid MNIST input domain, trained class-specific unary NAP regions become mutually inconsistent across classes.

This is not a robustness theorem for the classifier. It is a domain-level consistency statement about the NAP constraints themselves.

## 1.2 Direct Rejection of Misclassified Samples

The direct rejection experiment checks NAP membership at the sample itself.

For each checkpoint:

1. Run the current network on the MNIST test set.
2. Split samples into correctly classified and misclassified groups.
3. For each misclassified sample, check whether its activation pattern satisfies the NAP of its true class.
4. For comparison, also check how often correctly classified samples are rejected by their own class NAP.

This is not an adversarial `eps`-ball verification task. It is a direct activation-pattern check. Therefore it answers a cleaner question than the old local-region rejection experiment:

> Does the current NAP reject the sample itself?

Data source:

- `generated/nap_rejection_direct.csv`

![Direct NAP rejection over training](step4_followup_assets/direct_rejection_progress.png)

The most useful comparison is `alpha=0.99`:

| Track | Stage | Misclassified rejected by true-class NAP | Correct samples rejected by own-class NAP |
| --- | --- | ---: | ---: |
| A | random init | 2662/8991 (29.6%) | 233/1009 (23.1%) |
| A | 25% trained | 240/240 (100.0%) | 1518/9760 (15.6%) |
| A | 50% trained | 222/222 (100.0%) | 1926/9778 (19.7%) |
| A | 75% trained | 189/189 (100.0%) | 2047/9811 (20.9%) |
| A | final | 188/188 (100.0%) | 2025/9812 (20.6%) |
| B | random init | 2662/8991 (29.6%) | 233/1009 (23.1%) |
| B | 25% trained | 254/258 (98.4%) | 1618/9742 (16.6%) |
| B | 50% trained | 215/215 (100.0%) | 2048/9785 (20.9%) |
| B | 75% trained | 169/169 (100.0%) | 2167/9831 (22.0%) |
| B | final | 168/168 (100.0%) | 2183/9832 (22.2%) |

The interpretation is:

- At random initialization, `alpha=0.99` barely separates misclassified samples from correct samples: 29.6% rejection vs 23.1% false rejection.
- After training starts, the true-class NAP rejects almost all misclassified samples.
- The correct-sample rejection rate remains nonzero, around 15.6-22.2% after training, so this should not be described as a zero-false-positive rule.

For `alpha=0.95`, the rejection rate on misclassified samples is also very high, but it is too strict:

| Setting | Misclassified rejected by true-class NAP | Correct samples rejected by own-class NAP |
| --- | ---: | ---: |
| Track A, 25%-final | 240/240 to 188/188 (100.0%) | 6636/9760 to 7266/9812 (68.0-74.7%) |
| Track B, 25%-final | 258/258 to 168/168 (100.0%) | 6680/9742 to 7506/9832 (68.6-76.4%) |

So the cleaner rejection conclusion is:

> After training, unary NAP constraints become highly inconsistent with misclassified samples. The useful rejection setting is closer to `alpha=0.99`, because `alpha=0.95` rejects too many correctly classified samples as well.

## Combined Reading

The two rejection experiments support the same training-progress story from different angles.

Pairwise separation says:

> different class NAPs become mutually inconsistent in the valid input domain.

Direct rejection says:

> misclassified samples increasingly violate the NAP of their true class.

Together, they show that the learned NAP rules do not merely increase verification rates. They also become class-specific exclusion constraints as training progresses.

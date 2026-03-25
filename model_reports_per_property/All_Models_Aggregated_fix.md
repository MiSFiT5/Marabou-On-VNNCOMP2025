# ACAS Xu Per-Property Verification — FIXED Aggregated Report

> Generated 2026-03-25  
> **FIXED**: Only queries where `true_class == midpoint_predicted_class` are included.

## What Was Fixed and Why

### The Problem

In the original experiment, for each (model, property) pair:
1. 50,000 points are sampled uniformly within the property's input box.
2. Each point is classified by the network → multiple classes observed (e.g., {0, 1, 2, 4}).
3. NAP rules are mined **per class** from these samples.
4. Verification queries are run for **every observed class** as `true_class`.

But there is only **one reference point** (the property midpoint), and it has **one predicted class**.
When `true_class ≠ midpoint_predicted_class`, the query is **not about the robustness of the reference point**.
Two concrete failure modes exist:

**Case A (40 of 60 original baseline Y results):** `target == midpoint_predicted_class`.
Example: midpoint predicts class 0, query uses `true_class=2, target=0`.
This asks: "can `output[0] ≥ output[2]`?" — but ACAS Xu uses argmin (lowest score = prediction),
so `output[0]` is already the **minimum** output. Asking whether the minimum can exceed a larger value
is almost **trivially UNSAT**. The Y result is mathematically correct but tells us nothing about robustness.

**Case B (20 of 60):** Neither `true_class` nor `target` is the midpoint's predicted class.
Example: midpoint predicts class 0, query uses `true_class=1, target=3`.
This asks about the relative ordering of class 1 vs class 3 outputs — **completely unrelated** to the
robustness of the actual prediction (class 0).

### The Fix

This report keeps **only** the queries where `true_class` matches the midpoint's actual prediction.
Each property now contributes exactly **4 queries per ε** (1 true class × 4 target labels).

### Impact

- **Original (model, property) pairs:** 186
- **Fixed (model, property) pairs:** 186
- **Original baseline queries at ε=0.02 (α=0.99):** 1432
- **Fixed baseline queries at ε=0.02:** 744
- **Queries removed:** 688 (48%)
- **Original 60 baseline Y results at ε=0.02:** ALL from mismatched queries (0 remain after fix)
  - 40 were trivially UNSAT (target == midpoint's predicted class, i.e., asking if the minimum output can exceed a larger one)
  - 20 were about unrelated class pairs (neither class is the actual prediction)

## Midpoint Predictions

For each (model, property) pair, the midpoint's actual predicted class:

| Model | Property | Midpoint Predicted Class | Original Classes (from sampling) |
|-------|----------|------------------------|----------------------------------|
| N1,1 | prop1 | **0** | 0 |
| N1,1 | prop2 | **0** | 0 |
| N1,1 | prop3 | **3** | 3, 4 |
| N1,1 | prop4 | **3** | 3, 4 |
| N1,1 | prop5 | **4** | 4 |
| N1,1 | prop6 | **0** | 0 |
| N1,2 | prop1 | **0** | 0, 1, 2, 4 |
| N1,2 | prop2 | **0** | 0, 1, 2, 4 |
| N1,2 | prop3 | **4** | 3, 4 |
| N1,2 | prop4 | **3** | 3, 4 |
| N1,3 | prop1 | **0** | 0, 1, 2, 3 |
| N1,3 | prop2 | **0** | 0, 1, 2, 3 |
| N1,3 | prop3 | **3** | 3, 4 |
| N1,3 | prop4 | **3** | 3, 4 |
| N1,4 | prop1 | **0** | 0, 1, 2 |
| N1,4 | prop2 | **0** | 0, 1, 2 |
| N1,4 | prop3 | **3** | 3 |
| N1,4 | prop4 | **4** | 3, 4 |
| N1,5 | prop1 | **0** | 0, 1, 2, 4 |
| N1,5 | prop2 | **0** | 0, 1, 2, 4 |
| N1,5 | prop3 | **4** | 3, 4 |
| N1,5 | prop4 | **4** | 3, 4 |
| N1,6 | prop1 | **0** | 0, 1, 2, 3 |
| N1,6 | prop2 | **0** | 0, 1, 2, 3 |
| N1,6 | prop3 | **2** | 2 |
| N1,6 | prop4 | **1** | 1, 2 |
| N1,7 | prop1 | **0** | 0 |
| N1,7 | prop2 | **0** | 0 |
| N1,7 | prop3 | **0** | 0 |
| N1,7 | prop4 | **0** | 0 |
| N1,8 | prop1 | **0** | 0 |
| N1,8 | prop2 | **0** | 0 |
| N1,8 | prop3 | **0** | 0 |
| N1,8 | prop4 | **0** | 0 |
| N1,9 | prop1 | **0** | 0 |
| N1,9 | prop2 | **0** | 0 |
| N1,9 | prop3 | **0** | 0 |
| N1,9 | prop4 | **0** | 0 |
| N1,9 | prop7 | **0** | 0, 1, 2 |
| N2,1 | prop1 | **1** | 0, 1 |
| N2,1 | prop2 | **1** | 0, 1 |
| N2,1 | prop3 | **3** | 1, 3, 4 |
| N2,1 | prop4 | **4** | 3, 4 |
| N2,2 | prop1 | **1** | 0, 1, 3 |
| N2,2 | prop2 | **1** | 0, 1, 3 |
| N2,2 | prop3 | **3** | 1, 3, 4 |
| N2,2 | prop4 | **4** | 4 |
| N2,3 | prop1 | **1** | 0, 1 |
| N2,3 | prop2 | **1** | 0, 1 |
| N2,3 | prop3 | **3** | 3 |
| N2,3 | prop4 | **4** | 3, 4 |
| N2,4 | prop1 | **1** | 0, 1 |
| N2,4 | prop2 | **1** | 0, 1 |
| N2,4 | prop3 | **3** | 3 |
| N2,4 | prop4 | **3** | 3 |
| N2,5 | prop1 | **1** | 0, 1 |
| N2,5 | prop2 | **1** | 0, 1 |
| N2,5 | prop3 | **3** | 3 |
| N2,5 | prop4 | **3** | 3 |
| N2,6 | prop1 | **1** | 0, 1 |
| N2,6 | prop2 | **1** | 0, 1 |
| N2,6 | prop3 | **1** | 1 |
| N2,6 | prop4 | **1** | 1 |
| N2,7 | prop1 | **1** | 0, 1 |
| N2,7 | prop2 | **1** | 0, 1 |
| N2,7 | prop3 | **1** | 1 |
| N2,7 | prop4 | **1** | 1 |
| N2,8 | prop1 | **1** | 0, 1 |
| N2,8 | prop2 | **1** | 0, 1 |
| N2,8 | prop3 | **1** | 1 |
| N2,8 | prop4 | **1** | 1 |
| N2,9 | prop1 | **1** | 0, 1 |
| N2,9 | prop2 | **1** | 0, 1 |
| N2,9 | prop3 | **1** | 1 |
| N2,9 | prop4 | **1** | 1 |
| N2,9 | prop8 | **0** | 0, 1, 3 |
| N3,1 | prop1 | **2** | 0, 2, 4 |
| N3,1 | prop2 | **2** | 0, 2, 4 |
| N3,1 | prop3 | **4** | 2, 4 |
| N3,1 | prop4 | **4** | 4 |
| N3,2 | prop1 | **2** | 0, 2, 4 |
| N3,2 | prop2 | **2** | 0, 2, 4 |
| N3,2 | prop3 | **4** | 2, 3, 4 |
| N3,2 | prop4 | **4** | 4 |
| N3,3 | prop1 | **2** | 0, 2 |
| N3,3 | prop2 | **2** | 0, 2 |
| N3,3 | prop3 | **4** | 4 |
| N3,3 | prop4 | **4** | 4 |
| N3,3 | prop9 | **3** | 3 |
| N3,4 | prop1 | **2** | 0, 2 |
| N3,4 | prop2 | **2** | 0, 2 |
| N3,4 | prop3 | **4** | 4 |
| N3,4 | prop4 | **4** | 4 |
| N3,5 | prop1 | **2** | 0, 2 |
| N3,5 | prop2 | **2** | 0, 2 |
| N3,5 | prop3 | **4** | 4 |
| N3,5 | prop4 | **4** | 4 |
| N3,6 | prop1 | **2** | 0, 2 |
| N3,6 | prop2 | **2** | 0, 2 |
| N3,6 | prop3 | **2** | 2 |
| N3,6 | prop4 | **2** | 2 |
| N3,7 | prop1 | **2** | 0, 2, 4 |
| N3,7 | prop2 | **2** | 0, 2, 4 |
| N3,7 | prop3 | **2** | 2 |
| N3,7 | prop4 | **2** | 2 |
| N3,8 | prop1 | **2** | 0, 2 |
| N3,8 | prop2 | **2** | 0, 2 |
| N3,8 | prop3 | **2** | 2 |
| N3,8 | prop4 | **2** | 2 |
| N3,9 | prop1 | **2** | 0, 2 |
| N3,9 | prop2 | **2** | 0, 2 |
| N3,9 | prop3 | **2** | 2 |
| N3,9 | prop4 | **2** | 2 |
| N4,1 | prop1 | **1** | 0, 1, 3 |
| N4,1 | prop2 | **1** | 0, 1, 3 |
| N4,1 | prop3 | **4** | 1, 3, 4 |
| N4,1 | prop4 | **4** | 3, 4 |
| N4,2 | prop1 | **1** | 0, 1, 3 |
| N4,2 | prop2 | **1** | 0, 1, 3 |
| N4,2 | prop3 | **3** | 1, 3, 4 |
| N4,2 | prop4 | **4** | 4 |
| N4,3 | prop1 | **1** | 0, 1, 3 |
| N4,3 | prop2 | **1** | 0, 1, 3 |
| N4,3 | prop3 | **3** | 3 |
| N4,3 | prop4 | **4** | 3, 4 |
| N4,4 | prop1 | **3** | 0, 1, 3 |
| N4,4 | prop2 | **3** | 0, 1, 3 |
| N4,4 | prop3 | **3** | 3 |
| N4,4 | prop4 | **3** | 3 |
| N4,5 | prop1 | **3** | 0, 1, 3 |
| N4,5 | prop2 | **3** | 0, 1, 3 |
| N4,5 | prop3 | **3** | 3 |
| N4,5 | prop4 | **3** | 3 |
| N4,5 | prop10 | **0** | 0 |
| N4,6 | prop1 | **1** | 0, 1, 3 |
| N4,6 | prop2 | **1** | 0, 1, 3 |
| N4,6 | prop3 | **1** | 1 |
| N4,6 | prop4 | **1** | 1, 3 |
| N4,7 | prop1 | **1** | 0, 1, 3 |
| N4,7 | prop2 | **1** | 0, 1, 3 |
| N4,7 | prop3 | **1** | 1 |
| N4,7 | prop4 | **1** | 1 |
| N4,8 | prop1 | **1** | 0, 1 |
| N4,8 | prop2 | **1** | 0, 1 |
| N4,8 | prop3 | **1** | 1 |
| N4,8 | prop4 | **1** | 1 |
| N4,9 | prop1 | **3** | 0, 1, 3 |
| N4,9 | prop2 | **3** | 0, 1, 3 |
| N4,9 | prop3 | **1** | 1 |
| N4,9 | prop4 | **1** | 1 |
| N5,1 | prop1 | **4** | 0, 2, 4 |
| N5,1 | prop2 | **4** | 0, 2, 4 |
| N5,1 | prop3 | **4** | 2, 3, 4 |
| N5,1 | prop4 | **4** | 4 |
| N5,2 | prop1 | **4** | 0, 2, 4 |
| N5,2 | prop2 | **4** | 0, 2, 4 |
| N5,2 | prop3 | **4** | 2, 3, 4 |
| N5,2 | prop4 | **4** | 4 |
| N5,3 | prop1 | **2** | 0, 2, 4 |
| N5,3 | prop2 | **2** | 0, 2, 4 |
| N5,3 | prop3 | **4** | 4 |
| N5,3 | prop4 | **4** | 4 |
| N5,4 | prop1 | **2** | 0, 2 |
| N5,4 | prop2 | **2** | 0, 2 |
| N5,4 | prop3 | **4** | 4 |
| N5,4 | prop4 | **4** | 4 |
| N5,5 | prop1 | **2** | 0, 2, 4 |
| N5,5 | prop2 | **2** | 0, 2, 4 |
| N5,5 | prop3 | **4** | 4 |
| N5,5 | prop4 | **4** | 4 |
| N5,6 | prop1 | **2** | 0, 2, 4 |
| N5,6 | prop2 | **2** | 0, 2, 4 |
| N5,6 | prop3 | **2** | 2 |
| N5,6 | prop4 | **2** | 2 |
| N5,7 | prop1 | **2** | 0, 2, 4 |
| N5,7 | prop2 | **2** | 0, 2, 4 |
| N5,7 | prop3 | **2** | 2 |
| N5,7 | prop4 | **2** | 2 |
| N5,8 | prop1 | **2** | 0, 2, 4 |
| N5,8 | prop2 | **2** | 0, 2, 4 |
| N5,8 | prop3 | **2** | 2 |
| N5,8 | prop4 | **2** | 2 |
| N5,9 | prop1 | **2** | 0, 2 |
| N5,9 | prop2 | **2** | 0, 2 |
| N5,9 | prop3 | **2** | 2 |
| N5,9 | prop4 | **2** | 2 |

## Baseline Results (Fixed)

| ε | Y | N | T/o | Total | Verified % |
|---|---|---|-----|-------|------------|
| 0.02 | 0 | 744 | 0 | 744 | 0.0% |
| 0.05 | 0 | 744 | 0 | 744 | 0.0% |
| 0.1 | 0 | 743 | 1 | 744 | 0.0% |
| 0.2 | 0 | 744 | 0 | 744 | 0.0% |

## Full-Rule NAP Results by Rule Type (Fixed, ε=0.02)

### α = 0.9

| Rule Type | Y | N | T/o | Total | Verified % |
|-----------|---|---|-----|-------|------------|
| `ALWAYS_OFF (α=0.9)` | 56 | 684 | 0 | 740 | 7.6% |
| `ALWAYS_ON (α=0.9)` | 8 | 732 | 0 | 740 | 1.1% |
| `ALWAYS_ON+OFF (α=0.9)` | 56 | 684 | 0 | 740 | 7.6% |
| `Impl L0→L1 (α=0.9)` | 40 | 699 | 1 | 740 | 5.4% |
| `Impl L1→L2 (α=0.9)` | 36 | 702 | 2 | 740 | 4.9% |
| `Impl L2→L3 (α=0.9)` | 68 | 672 | 0 | 740 | 9.2% |
| `Impl L3→L4 (α=0.9)` | 72 | 668 | 0 | 740 | 9.7% |
| `Impl L4→L5 (α=0.9)` | 52 | 681 | 7 | 740 | 7.0% |
| `none (baseline)` | 0 | 740 | 0 | 740 | 0.0% |

### α = 0.95

| Rule Type | Y | N | T/o | Total | Verified % |
|-----------|---|---|-----|-------|------------|
| `ALWAYS_OFF (α=0.95)` | 16 | 724 | 0 | 740 | 2.2% |
| `ALWAYS_ON (α=0.95)` | 0 | 740 | 0 | 740 | 0.0% |
| `ALWAYS_ON+OFF (α=0.95)` | 16 | 724 | 0 | 740 | 2.2% |
| `Impl L0→L1 (α=0.95)` | 8 | 732 | 0 | 740 | 1.1% |
| `Impl L1→L2 (α=0.95)` | 16 | 724 | 0 | 740 | 2.2% |
| `Impl L2→L3 (α=0.95)` | 24 | 716 | 0 | 740 | 3.2% |
| `Impl L3→L4 (α=0.95)` | 24 | 716 | 0 | 740 | 3.2% |
| `Impl L4→L5 (α=0.95)` | 20 | 714 | 6 | 740 | 2.7% |
| `none (baseline)` | 0 | 740 | 0 | 740 | 0.0% |

### α = 0.99

| Rule Type | Y | N | T/o | Total | Verified % |
|-----------|---|---|-----|-------|------------|
| `ALWAYS_OFF (α=0.99)` | 0 | 744 | 0 | 744 | 0.0% |
| `ALWAYS_ON (α=0.99)` | 0 | 744 | 0 | 744 | 0.0% |
| `ALWAYS_ON+OFF (α=0.99)` | 0 | 744 | 0 | 744 | 0.0% |
| `Impl L0→L1 (α=0.99)` | 0 | 744 | 0 | 744 | 0.0% |
| `Impl L1→L2 (α=0.99)` | 0 | 744 | 0 | 744 | 0.0% |
| `Impl L2→L3 (α=0.99)` | 0 | 744 | 0 | 744 | 0.0% |
| `Impl L3→L4 (α=0.99)` | 0 | 744 | 0 | 744 | 0.0% |
| `Impl L4→L5 (α=0.99)` | 0 | 741 | 3 | 744 | 0.0% |
| `none (baseline)` | 0 | 744 | 0 | 744 | 0.0% |

## Per-Model Summary

| Model | Props | Fixed Queries/ε | Original Queries/ε | Reduction | Best NAP Y% (ε=0.02, α=0.90) |
|-------|-------|-----------------|--------------------|-----------|-----------------------------|
| [N1,1](N1_1_fix.md) | 6 | 24 | 32 | −8 | 50.0% (Impl L2→L3 (α=0.9)) |
| [N1,2](N1_2_fix.md) | 4 | 16 | 48 | −32 | 50.0% (ALWAYS_OFF (α=0.9)) |
| [N1,3](N1_3_fix.md) | 4 | 16 | 48 | −32 | 50.0% (Impl L1→L2 (α=0.9)) |
| [N1,4](N1_4_fix.md) | 4 | 16 | 36 | −20 | 50.0% (Impl L2→L3 (α=0.9)) |
| [N1,5](N1_5_fix.md) | 4 | 16 | 48 | −32 | 50.0% (ALWAYS_OFF (α=0.9)) |
| [N1,6](N1_6_fix.md) | 4 | 16 | 44 | −28 | 50.0% (ALWAYS_OFF (α=0.9)) |
| [N1,7](N1_7_fix.md) | 4 | 16 | 16 | −0 | 50.0% (ALWAYS_OFF (α=0.9)) |
| [N1,8](N1_8_fix.md) | 4 | 16 | 16 | −0 | 50.0% (ALWAYS_OFF (α=0.9)) |
| [N1,9](N1_9_fix.md) | 5 | 20 | 28 | −8 | 60.0% (Impl L4→L5 (α=0.9)) |
| [N2,1](N2_1_fix.md) | 4 | 16 | 36 | −20 | 50.0% (Impl L0→L1 (α=0.9)) |
| [N2,2](N2_2_fix.md) | 4 | 16 | 40 | −24 | 0.0% () |
| [N2,3](N2_3_fix.md) | 4 | 16 | 28 | −12 | 0.0% () |
| [N2,4](N2_4_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N2,5](N2_5_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N2,6](N2_6_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N2,7](N2_7_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N2,8](N2_8_fix.md) | 4 | 16 | 24 | −8 | 50.0% (Impl L0→L1 (α=0.9)) |
| [N2,9](N2_9_fix.md) | 5 | 20 | 36 | −16 | 0.0% () |
| [N3,1](N3_1_fix.md) | 4 | 16 | 36 | −20 | 0.0% () |
| [N3,2](N3_2_fix.md) | 4 | 16 | 40 | −24 | 0.0% () |
| [N3,3](N3_3_fix.md) | 5 | 20 | 28 | −8 | 0.0% () |
| [N3,4](N3_4_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N3,5](N3_5_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N3,6](N3_6_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N3,7](N3_7_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N3,8](N3_8_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N3,9](N3_9_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N4,1](N4_1_fix.md) | 4 | 16 | 44 | −28 | 0.0% () |
| [N4,2](N4_2_fix.md) | 4 | 16 | 40 | −24 | 0.0% () |
| [N4,3](N4_3_fix.md) | 4 | 16 | 36 | −20 | 0.0% () |
| [N4,4](N4_4_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N4,5](N4_5_fix.md) | 5 | 20 | 36 | −16 | 0.0% () |
| [N4,6](N4_6_fix.md) | 4 | 16 | 36 | −20 | 0.0% () |
| [N4,7](N4_7_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N4,8](N4_8_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N4,9](N4_9_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N5,1](N5_1_fix.md) | 4 | 16 | 40 | −24 | 50.0% (Impl L0→L1 (α=0.9)) |
| [N5,2](N5_2_fix.md) | 4 | 16 | 40 | −24 | 0.0% () |
| [N5,3](N5_3_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N5,4](N5_4_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |
| [N5,5](N5_5_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N5,6](N5_6_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N5,7](N5_7_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N5,8](N5_8_fix.md) | 4 | 16 | 32 | −16 | 0.0% () |
| [N5,9](N5_9_fix.md) | 4 | 16 | 24 | −8 | 0.0% () |

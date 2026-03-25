#!/usr/bin/env python3
"""
Patch all N*_*.md model reports to add a detailed explanation section
explaining what a verification query is, how the reference point is used,
and what UNSAT/SAT/Timeout mean — so readers can understand the tables
without reading external documentation.
"""
import glob, os, re

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_reports_per_property")

EXPLANATION_BLOCK = r"""
### What Is a Verification Query?

Each row in the tables below corresponds to a single call to the Marabou SMT solver.
A query is fully identified by the tuple **`(property, ε, true_class, target_label, rule_type)`**.

**Concrete example — suppose we are looking at model N5,2, prop1, ε = 0.05,
true\_class = 0, target\_label = 3, rule = ALWAYS\_OFF (α = 0.9):**

**Step 1 — Choose the reference point.**
The reference point is the **midpoint** (element-wise center) of the VNNLIB
input box for the given property.  For prop1 of N5,2, this is a 5-dimensional
vector computed as `ref = (lower_bound + upper_bound) / 2` for each of the
5 ACAS Xu inputs.

**Step 2 — Build input constraints (L∞ ball).**
Marabou is told that the 5 network inputs must lie within:

```
ref[i] − ε  ≤  x[i]  ≤  ref[i] + ε     for i = 0 … 4
```

This defines a small hypercube ("ε-ball") around the reference point.

**Step 3 — Add NAP constraints (the "rule" column).**
Depending on the rule type being tested:

| Rule type | What Marabou is told |
|-----------|---------------------|
| `none (baseline)` | No extra constraints — pure Marabou. |
| `ALWAYS_OFF` | For every neuron mined as "always off" for class 0 at α ≥ 0.9: force `pre_relu ≤ 0` (neuron output = 0). |
| `ALWAYS_ON` | For every neuron mined as "always on" for class 0 at α ≥ 0.9: force `post_relu ≥ 1e-6` (neuron fires). |
| `ALWAYS_ON+OFF` | Apply **both** ALWAYS_ON and ALWAYS_OFF constraints simultaneously. |
| `Impl Lk→Lk+1` | For every implication rule mined between layers k and k+1 for class 0, add a disjunction constraint that encodes the implication (e.g., `A→B` becomes `(A is inactive) OR (B is active)`). |

These constraints tell the solver: "only search in the part of the ε-ball
where the network's internal activation pattern matches what was observed
during sampling."  This prunes the search space dramatically.

**Step 4 — Add the adversarial output constraint.**
Marabou is told to look for an input where:

```
output[target_label]  ≥  output[true_class]
```

i.e., `output[3] ≥ output[0]` in our example.  This asks: "can the network
be made to prefer action 3 over action 0 within the ε-ball?"

**Step 5 — Solve and interpret the result.**

| Marabou answer | Meaning | Table symbol |
|----------------|---------|-------------|
| **UNSAT** | No such adversarial input exists — the network **cannot** be fooled into preferring target\_label over true\_class anywhere in the ε-ball (given the NAP constraints). The property is **verified** for this query. | 🟢 **Y** |
| **SAT** | An adversarial input **was found** — the network can be fooled. The property is **not verified**. | 🔴 **N** |
| **Timeout** | Marabou could not decide within 120 seconds. | 🟡 **T/o** |

**Why do we test every (true\_class, target\_label) pair?**
The reference point's predicted class is its `true_class`.  We must check
that no *other* class can become dominant, so we test each of the other 4
classes as `target_label`.  This gives **4 queries per true\_class per ε**.
If a property's input region contains samples predicted as multiple classes,
each predicted class becomes a separate `true_class`, multiplying the query
count accordingly (see the accounting table below).

"""

def patch_file(path):
    with open(path, 'r') as f:
        content = f.read()

    # Check if already patched
    if "### What Is a Verification Query?" in content:
        print(f"  SKIP (already patched): {os.path.basename(path)}")
        return False

    # Find the insertion point: after the last bullet in "How To Read Counts"
    # and before "**Per-model query accounting"
    marker = "**Per-model query accounting"
    idx = content.find(marker)
    if idx == -1:
        print(f"  SKIP (marker not found): {os.path.basename(path)}")
        return False

    # Insert explanation block before the marker
    new_content = content[:idx] + EXPLANATION_BLOCK + content[idx:]

    with open(path, 'w') as f:
        f.write(new_content)

    print(f"  PATCHED: {os.path.basename(path)}")
    return True


def main():
    files = sorted(glob.glob(os.path.join(REPORTS_DIR, "N*_*.md")))
    print(f"Found {len(files)} model report files")
    patched = 0
    for f in files:
        if patch_file(f):
            patched += 1
    print(f"\nDone. Patched {patched}/{len(files)} files.")


if __name__ == "__main__":
    main()

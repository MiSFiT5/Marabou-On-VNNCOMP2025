# Step 4 — Exact Unary vs Implication Families

> Generated 2026-04-08
> Fixed-reference Marabou exact results only

- **Tracks:** A (70 epochs), B (100 epochs)
- **Checkpoints per track:** 5 (`0%, 25%, 50%, 75%, 100%`)
- **Positive refs per track:** 20 fixed unified refs
- **Rejection refs per checkpoint:** 10 misclassified samples
- **Runtime alpha:** `0.95`, `0.99`
- **Epsilon:** `0.01`, `0.02`, `0.05`
- **Main comparison window:** `progress >= 25%`

Compared method families:

- `Baseline`
- `Unary ON/OFF`
- `Implication L4L5`
- `Implication L4L5_L5L6`
- `Compressed L0L6 c=0.95`
- `Compressed L0L6 c=0.99`

Here `c=0.95 / 0.99` means the compressed-chain mining threshold, not the runtime Step 4 alpha.

---

## 1. Aggregated Positive-Ref Results

Mean over both tracks, checkpoints with `progress >= 25%`.

| Method | Runtime alpha | `eps=0.01` verified | `eps=0.01` genuine | `eps=0.02` verified | `eps=0.02` genuine |
|--------|---------------|--------------------:|-------------------:|--------------------:|-------------------:|
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

### Direct reading

- `Unary ON/OFF` is still highest in total verified rate.
- `Compressed L0L6 c=0.95` is highest in exact genuine verified at `eps=0.01`.
- `Compressed L0L6 c=0.95`, runtime `alpha=0.99`, is the best positive-ref row in this slice: `87.50%` genuine.
- At `eps=0.02`, compressed `L0L6` drops back to around baseline and is far below unary.

---

## 2. Exact Genuine by Track and Checkpoint

### `eps=0.01`, runtime `alpha=0.99`

#### Track A

| Checkpoint | Baseline | Unary ON/OFF | `L4L5` | `L4L5_L5L6` | `Compressed c=0.95` | `Compressed c=0.99` |
|------------|---------:|-------------:|-------:|------------:|--------------------:|--------------------:|
| epoch_000 | 0.0% | 25.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| epoch_018 | 75.0% | 40.0% | 65.0% | 60.0% | 75.0% | 75.0% |
| epoch_035 | 75.0% | 75.0% | 75.0% | 70.0% | 85.0% | 75.0% |
| epoch_052 | 85.0% | 80.0% | 70.0% | 65.0% | 90.0% | 90.0% |
| epoch_070 | 85.0% | 80.0% | 75.0% | 70.0% | 90.0% | 90.0% |

#### Track B

| Checkpoint | Baseline | Unary ON/OFF | `L4L5` | `L4L5_L5L6` | `Compressed c=0.95` | `Compressed c=0.99` |
|------------|---------:|-------------:|-------:|------------:|--------------------:|--------------------:|
| epoch_000 | 0.0% | 25.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| epoch_025 | 70.0% | 35.0% | 65.0% | 65.0% | 75.0% | 70.0% |
| epoch_050 | 80.0% | 80.0% | 80.0% | 75.0% | 85.0% | 80.0% |
| epoch_075 | 90.0% | 80.0% | 80.0% | 70.0% | 100.0% | 90.0% |
| epoch_100 | 90.0% | 80.0% | 80.0% | 70.0% | 100.0% | 100.0% |

### `eps=0.02`, runtime `alpha=0.99`

#### Track A

| Checkpoint | Baseline | Unary ON/OFF | `L4L5` | `L4L5_L5L6` | `Compressed c=0.95` | `Compressed c=0.99` |
|------------|---------:|-------------:|-------:|------------:|--------------------:|--------------------:|
| epoch_000 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| epoch_018 | 5.0% | 10.0% | 5.0% | 5.0% | 5.0% | 0.0% |
| epoch_035 | 15.0% | 30.0% | 5.0% | 5.0% | 5.0% | 5.0% |
| epoch_052 | 15.0% | 40.0% | 15.0% | 15.0% | 15.0% | 15.0% |
| epoch_070 | 15.0% | 40.0% | 15.0% | 15.0% | 15.0% | 15.0% |

#### Track B

| Checkpoint | Baseline | Unary ON/OFF | `L4L5` | `L4L5_L5L6` | `Compressed c=0.95` | `Compressed c=0.99` |
|------------|---------:|-------------:|-------:|------------:|--------------------:|--------------------:|
| epoch_000 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| epoch_025 | 0.0% | 5.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| epoch_050 | 15.0% | 40.0% | 15.0% | 15.0% | 15.0% | 15.0% |
| epoch_075 | 20.0% | 60.0% | 25.0% | 25.0% | 20.0% | 20.0% |
| epoch_100 | 20.0% | 55.0% | 20.0% | 25.0% | 20.0% | 20.0% |

### Main pattern from the checkpoint tables

- `Compressed c=0.95` is the cleanest `eps=0.01` story across training.
- Track B is the strongest success case:
  - `100%` genuine at `epoch_075`
  - `100%` genuine at `epoch_100`
- `eps=0.02` is still mainly a unary-NAP regime; compressed does not open a new large-radius region there.

---

## 3. Vacuity and Timeout Burden on Positive Refs

### Vacuous counts over `progress >= 25%`

| Method | Runtime alpha | `eps=0.01` vacuous | `eps=0.02` vacuous |
|--------|---------------|-------------------:|-------------------:|
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

### Timeout / semantic-unresolved counts over `progress >= 25%`

| Method | Runtime alpha | `eps=0.01` timeout / unresolved | `eps=0.02` timeout / unresolved |
|--------|---------------|---------------------------------|---------------------------------|
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

### Reading

- `Compressed L0L6` is the cleanest family semantically:
  - no vacuous gain
  - very little unresolved mass at `eps=0.01`
- Its weakness is not vacuity; it is `eps=0.02` timeout saturation.

---

## 4. Exact Rejection Results

Mean over both tracks, checkpoints with `progress >= 25%`.

| Method | Runtime alpha | `eps=0.01` rejection | `eps=0.01` timeout | `eps=0.02` rejection | `eps=0.02` timeout |
|--------|---------------|---------------------:|-------------------:|---------------------:|-------------------:|
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

### Reading

- `Unary ON/OFF` is still the strongest rejection family by a large margin.
- `L4L5` and `L4L5_L5L6` are intermediate.
- `Compressed L0L6` is weakest on rejection, even though it is strongest on small-radius positive-ref genuine verification.

---

## 5. Data-First Summary

1. If the target metric is **positive-ref exact genuine at `eps=0.01`**, the best method in this slice is `Compressed L0L6 c=0.95`.
2. If the target metric is **misclassified-ref rejection**, the best method is still `Unary ON/OFF`.
3. If the target metric is **larger-radius exact gain at `eps=0.02`**, unary remains the only clearly useful family.
4. `Compressed L0L6` is strong because it removes the vacuous problem almost entirely.
5. `Compressed L0L6` does not replace unary globally; it gives a different kind of win:
   - stronger small-radius semantic certification on already-correct refs
   - weaker region-carving around misclassified refs

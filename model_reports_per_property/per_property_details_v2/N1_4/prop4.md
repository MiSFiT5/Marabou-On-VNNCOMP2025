# N1,4 — Property 4

> Single reference point verification report (v2)
> Generated 2026-03-25

## Reference Point

- **Model:** `ACASXU_run2a_1_4_batch_2000.onnx`
- **Property:** prop4
- **Reference point (property midpoint):** `[-0.301042, 0.0, 0.0, 0.409091, 0.125]`
- **Network prediction:** class **4** (Strong Right)
- **Network outputs at midpoint:** `[0.0249, 0.0443, 0.0251, 0.012, 0.0021]`
- **Query filter used in this report:** `class_id = midpoint prediction`, `center_source = property_midpoint[0]`, `sample_idx = 0`

## Dedup Rule

- Repeated logical experiments are merged after the midpoint filter.
- Duplicate key: same `target`, same `ε`, same experiment label, same `α`.
- Keep order: `A (full_rule)` < `B/L0→L1` < `B/L1→L2` < `B/L2→L3` < `B/L3→L4` < `B/L4→L5` < `C (impl_ablation)`.
- The report shows only the kept rows after this overwrite rule.

## Target Summary

| Target | Class Name | Max Verified ε | Winning kept experiments |
|--------|------------|----------------|--------------------------|
| 0 | Clear-of-Conflict | – | – |
| 1 | Weak Left | – | – |
| 2 | Weak Right | – | – |
| 3 | Strong Left | – | – |

**Overall:** after deduplication, this reference point is not fully verified at any tested ε.

---

## Detailed Results Per Target

### Target 0 (Clear-of-Conflict)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (2s) | N (1s) | N (2s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (3s) | N (1s) | N (2s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (2s) | N (1s) | N (2s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (3s) | T/o | N (114s) | N (71s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (3s) | N (112s) | T/o | N (28s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (4s) | N (103s) | T/o | N (46s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (3s) | N (7s) | N (38s) | N (55s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (4s) | N (8s) | N (34s) | N (51s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (9s) | N (38s) | N (44s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (7s) | N (57s) | N (103s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (3s) | N (8s) | N (56s) | N (98s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (8s) | N (74s) | N (94s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (5s) | N (55s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (1s) | N (60s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (2s) | N (63s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (23s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (8s) | T/o | N (97s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (8s) | T/o | N (116s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (8s) | T/o | N (90s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | T/o | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (112s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (84s) | T/o | T/o |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (4s) | N (8s) | T/o | N (92s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (7s) | T/o | T/o |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (8s) | T/o | N (102s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | T/o | T/o | T/o |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (91s) | T/o | T/o |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (106s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (3s) | N (55s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (2s) | N (56s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (30s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (3s) | N (9s) | N (36s) | N (111s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (4s) | N (9s) | N (44s) | N (85s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (10s) | N (39s) | N (61s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (3s) | N (67s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (48s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (43s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (4s) | N (13s) | N (57s) | N (67s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (11s) | N (41s) | N (73s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (11s) | N (48s) | N (64s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (11s) | N (61s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (16s) | N (67s) | N (94s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (12s) | N (53s) | N (115s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | T/o | N (18s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | T/o | N (27s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (3s) | T/o | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | N (12s) | N (69s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (7s) | N (52s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (11s) | N (44s) | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | T/o | N (25s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (10s) | T/o | N (23s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (3s) | T/o | N (25s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (9s) | N (77s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (9s) | N (63s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (2s) | N (90s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (32s) | N (106s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (34s) | N (102s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (38s) | N (100s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (89s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (66s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (8s) | N (61s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (30s) | N (80s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (32s) | N (114s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (35s) | N (96s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (23s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (4s) | N (36s) | N (105s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (4s) | N (10s) | N (17s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | N (7s) | N (16s) | N (63s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (27s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (20s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (4s) | N (6s) | N (17s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (5s) | N (6s) | N (15s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (3s) | N (10s) | N (26s) | T/o |

### Target 1 (Weak Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (2s) | N (24s) | N (2s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (19s) | N (32s) | N (5s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (2s) | N (5s) | N (2s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (3s) | T/o | T/o | N (32s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (3s) | N (66s) | T/o | N (28s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (5s) | N (78s) | T/o | N (39s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (4s) | N (8s) | N (37s) | N (50s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (3s) | N (9s) | N (26s) | T/o |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (7s) | N (44s) | N (49s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (11s) | N (40s) | N (104s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (2s) | N (7s) | N (51s) | N (109s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (9s) | N (41s) | T/o |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (9s) | N (47s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (8s) | N (46s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (5s) | N (55s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (16s) | N (119s) | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (19s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (23s) | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (7s) | T/o | N (83s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (7s) | T/o | N (90s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (8s) | T/o | N (109s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | T/o | T/o | N (112s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (2s) | N (114s) | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (4s) | N (98s) | T/o | N (114s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (4s) | N (8s) | T/o | N (100s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (8s) | T/o | N (90s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (10s) | T/o | N (104s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (3s) | N (111s) | T/o | N (114s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (3s) | N (91s) | T/o | N (103s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (3s) | N (87s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (4s) | N (52s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (52s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (46s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (15s) | N (20s) | N (47s) | N (59s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (8s) | N (30s) | N (63s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (8s) | N (59s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (3s) | N (47s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (60s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (54s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (3s) | N (10s) | N (44s) | N (70s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (11s) | N (28s) | N (51s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (16s) | N (43s) | N (53s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | N (10s) | N (46s) | N (105s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (8s) | N (52s) | N (116s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (8s) | N (53s) | N (118s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (13s) | T/o | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | T/o | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (3s) | T/o | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (11s) | N (73s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (9s) | N (62s) | N (109s) |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (9s) | N (52s) | N (98s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (3s) | T/o | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | T/o | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (9s) | N (59s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (8s) | N (62s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (7s) | N (111s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (29s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (27s) | N (102s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (22s) | N (96s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (7s) | N (65s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (9s) | N (55s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (8s) | N (81s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (2s) | N (92s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (28s) | N (88s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (29s) | N (111s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (19s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (15s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (21s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (5s) | N (6s) | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (4s) | N (5s) | N (16s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | N (5s) | N (14s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (22s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (14s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (14s) | N (14s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (4s) | N (99s) | N (36s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | N (5s) | N (13s) | N (9s) |

### Target 2 (Weak Right)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (1s) | N (1s) | N (2s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (1s) | N (1s) | N (2s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (1s) | N (1s) | N (2s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | N (5s) | N (7s) | N (10s) | N (118s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (2s) | N (12s) | N (8s) | N (39s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (9s) | N (6s) | N (8s) | N (43s) |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (4s) | N (10s) | N (44s) | N (45s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (4s) | N (9s) | N (33s) | N (42s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (3s) | N (8s) | N (18s) | N (42s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (2s) | N (11s) | N (63s) | N (113s) |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (2s) | N (8s) | N (54s) | T/o |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (2s) | N (10s) | N (53s) | N (87s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (8s) | N (21s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (7s) | N (21s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (6s) | N (21s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (22s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (22s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (16s) | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (5s) | N (8s) | N (22s) | N (54s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (9s) | N (18s) | N (56s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (8s) | N (8s) | T/o | N (49s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (5s) | N (8s) | N (20s) | N (25s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (35s) | N (6s) | N (11s) | N (17s) |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (6s) | N (28s) | N (11s) | N (12s) |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | N (4s) | N (7s) | N (23s) | N (56s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (4s) | N (11s) | N (20s) | N (55s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (9s) | N (7s) | N (17s) | N (52s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | N (5s) | N (6s) | N (12s) | N (19s) |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (6s) | N (6s) | N (9s) | N (117s) |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (12s) | N (11s) | N (10s) | N (12s) |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (2s) | N (8s) | N (62s) | N (68s) |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (18s) | N (72s) | N (64s) |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (9s) | N (53s) | N (100s) |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (4s) | N (10s) | N (53s) | N (71s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (9s) | N (27s) | N (48s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (4s) | N (8s) | N (40s) | N (118s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (3s) | N (11s) | N (58s) | N (52s) |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (3s) | N (8s) | N (63s) | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (3s) | N (9s) | N (21s) | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (3s) | N (8s) | N (81s) | N (48s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (4s) | N (9s) | N (36s) | N (43s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (4s) | N (8s) | N (92s) | N (51s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (11s) | N (52s) | T/o |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (12s) | N (58s) | N (97s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (2s) | N (10s) | N (111s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (17s) | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (4s) | N (18s) | N (21s) | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (4s) | N (20s) | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (11s) | N (51s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (2s) | N (15s) | N (70s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (3s) | N (10s) | N (66s) | N (114s) |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (4s) | N (19s) | N (22s) | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (3s) | N (18s) | N (62s) | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (4s) | N (21s) | N (32s) | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (9s) | N (40s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (3s) | N (53s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (3s) | N (48s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (45s) | N (16s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (44s) | N (13s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (52s) | N (25s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (1s) | N (34s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (8s) | N (46s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (8s) | N (47s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (41s) | N (13s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (33s) | N (13s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (34s) | N (13s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | T/o | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (16s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (26s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (11s) | N (19s) | N (24s) |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (5s) | N (5s) | N (16s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | N (5s) | N (15s) | N (116s) |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (16s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (16s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (3s) | N (6s) | N (16s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (3s) | N (5s) | N (18s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (4s) | N (6s) | N (18s) | T/o |

### Target 3 (Strong Left)

- **Max verified ε after deduplication:** `–`
- **Winning kept experiments:** none

| Experiment | Type | ε=0.02 | ε=0.05 | ε=0.10 | ε=0.20 |
|------------|------|--------|--------|--------|--------|
| `none (baseline) [α=0.95]` | baseline | N (1s) | N (6s) | N (8s) | N (1s) |
| `none (baseline) [α=0.99]` | baseline | N (1s) | N (2s) | N (32s) | N (1s) |
| `none (baseline) [α=0.9]` | baseline | N (1s) | N (5s) | N (25s) | N (1s) |
| `ALWAYS_OFF (α=0.9)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.95)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_OFF (α=0.99)` | unary-only | N (1s) | N (1s) | N (1s) | N (1s) |
| `ALWAYS_ON (α=0.9)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.95)` | unary-only | N (0s) | N (0s) | N (1s) | N (0s) |
| `ALWAYS_ON (α=0.99)` | unary-only | N (0s) | N (0s) | N (1s) | N (1s) |
| `ALWAYS_ON+OFF (α=0.9)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.95)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `ALWAYS_ON+OFF (α=0.99)` | unary-only | N (0s) | N (0s) | N (0s) | N (0s) |
| `Impl L0→L1 (α=0.9)` | implication-only (L0→L1) | T/o | N (105s) | T/o | N (105s) |
| `Impl L0→L1 (α=0.95)` | implication-only (L0→L1) | N (98s) | T/o | N (109s) | N (35s) |
| `Impl L0→L1 (α=0.99)` | implication-only (L0→L1) | N (63s) | N (116s) | T/o | T/o |
| `Impl L1→L2 (α=0.9)` | implication-only (L1→L2) | N (1s) | N (19s) | N (64s) | N (55s) |
| `Impl L1→L2 (α=0.95)` | implication-only (L1→L2) | N (10s) | N (12s) | N (53s) | N (60s) |
| `Impl L1→L2 (α=0.99)` | implication-only (L1→L2) | N (9s) | N (17s) | N (83s) | N (57s) |
| `Impl L2→L3 (α=0.9)` | implication-only (L2→L3) | N (1s) | N (9s) | N (72s) | T/o |
| `Impl L2→L3 (α=0.95)` | implication-only (L2→L3) | N (10s) | N (22s) | N (56s) | N (99s) |
| `Impl L2→L3 (α=0.99)` | implication-only (L2→L3) | N (11s) | N (9s) | N (54s) | N (108s) |
| `Impl L3→L4 (α=0.9)` | implication-only (L3→L4) | N (1s) | N (49s) | T/o | T/o |
| `Impl L3→L4 (α=0.95)` | implication-only (L3→L4) | N (2s) | N (40s) | T/o | T/o |
| `Impl L3→L4 (α=0.99)` | implication-only (L3→L4) | N (4s) | N (55s) | T/o | T/o |
| `Impl L4→L5 (α=0.9)` | implication-only (L4→L5) | N (2s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.95)` | implication-only (L4→L5) | N (18s) | T/o | T/o | T/o |
| `Impl L4→L5 (α=0.99)` | implication-only (L4→L5) | N (18s) | T/o | T/o | T/o |
| `Impl L0→L1 [!A->!B] (α=0.9)` | implication-direction (L0→L1) | N (65s) | N (7s) | T/o | N (85s) |
| `Impl L0→L1 [!A->!B] (α=0.95)` | implication-direction (L0→L1) | N (67s) | N (9s) | T/o | N (90s) |
| `Impl L0→L1 [!A->!B] (α=0.99)` | implication-direction (L0→L1) | N (63s) | N (9s) | T/o | N (97s) |
| `Impl L0→L1 [!A->B] (α=0.9)` | implication-direction (L0→L1) | N (65s) | N (114s) | T/o | N (91s) |
| `Impl L0→L1 [!A->B] (α=0.95)` | implication-direction (L0→L1) | N (66s) | T/o | T/o | T/o |
| `Impl L0→L1 [!A->B] (α=0.99)` | implication-direction (L0→L1) | N (68s) | N (90s) | T/o | T/o |
| `Impl L0→L1 [A->!B] (α=0.9)` | implication-direction (L0→L1) | T/o | N (8s) | T/o | N (77s) |
| `Impl L0→L1 [A->!B] (α=0.95)` | implication-direction (L0→L1) | N (63s) | N (8s) | T/o | N (89s) |
| `Impl L0→L1 [A->!B] (α=0.99)` | implication-direction (L0→L1) | N (60s) | N (7s) | T/o | N (94s) |
| `Impl L0→L1 [A->B] (α=0.9)` | implication-direction (L0→L1) | T/o | N (115s) | T/o | T/o |
| `Impl L0→L1 [A->B] (α=0.95)` | implication-direction (L0→L1) | N (75s) | T/o | T/o | T/o |
| `Impl L0→L1 [A->B] (α=0.99)` | implication-direction (L0→L1) | N (62s) | N (99s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.9)` | implication-direction (L1→L2) | N (11s) | N (58s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.95)` | implication-direction (L1→L2) | N (7s) | N (59s) | T/o | T/o |
| `Impl L1→L2 [!A->!B] (α=0.99)` | implication-direction (L1→L2) | N (9s) | N (54s) | T/o | T/o |
| `Impl L1→L2 [!A->B] (α=0.9)` | implication-direction (L1→L2) | N (21s) | N (19s) | N (65s) | N (112s) |
| `Impl L1→L2 [!A->B] (α=0.95)` | implication-direction (L1→L2) | N (16s) | N (22s) | N (86s) | N (60s) |
| `Impl L1→L2 [!A->B] (α=0.99)` | implication-direction (L1→L2) | N (21s) | N (19s) | N (103s) | N (112s) |
| `Impl L1→L2 [A->!B] (α=0.9)` | implication-direction (L1→L2) | N (9s) | N (42s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.95)` | implication-direction (L1→L2) | N (9s) | N (48s) | T/o | T/o |
| `Impl L1→L2 [A->!B] (α=0.99)` | implication-direction (L1→L2) | N (8s) | N (49s) | T/o | T/o |
| `Impl L1→L2 [A->B] (α=0.9)` | implication-direction (L1→L2) | N (20s) | N (18s) | N (104s) | N (77s) |
| `Impl L1→L2 [A->B] (α=0.95)` | implication-direction (L1→L2) | N (13s) | N (18s) | N (112s) | N (71s) |
| `Impl L1→L2 [A->B] (α=0.99)` | implication-direction (L1→L2) | N (17s) | N (21s) | N (76s) | N (64s) |
| `Impl L2→L3 [!A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (17s) | N (62s) | N (119s) |
| `Impl L2→L3 [!A->!B] (α=0.95)` | implication-direction (L2→L3) | N (13s) | N (18s) | N (54s) | N (120s) |
| `Impl L2→L3 [!A->!B] (α=0.99)` | implication-direction (L2→L3) | N (13s) | N (21s) | N (80s) | N (102s) |
| `Impl L2→L3 [!A->B] (α=0.9)` | implication-direction (L2→L3) | N (39s) | T/o | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.95)` | implication-direction (L2→L3) | N (40s) | T/o | T/o | T/o |
| `Impl L2→L3 [!A->B] (α=0.99)` | implication-direction (L2→L3) | N (69s) | T/o | T/o | T/o |
| `Impl L2→L3 [A->!B] (α=0.9)` | implication-direction (L2→L3) | N (2s) | N (18s) | N (50s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.95)` | implication-direction (L2→L3) | N (12s) | N (15s) | N (54s) | T/o |
| `Impl L2→L3 [A->!B] (α=0.99)` | implication-direction (L2→L3) | N (12s) | N (11s) | N (55s) | T/o |
| `Impl L2→L3 [A->B] (α=0.9)` | implication-direction (L2→L3) | N (49s) | T/o | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.95)` | implication-direction (L2→L3) | N (41s) | T/o | T/o | T/o |
| `Impl L2→L3 [A->B] (α=0.99)` | implication-direction (L2→L3) | N (66s) | T/o | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.9)` | implication-direction (L3→L4) | N (26s) | N (72s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.95)` | implication-direction (L3→L4) | N (22s) | N (64s) | T/o | T/o |
| `Impl L3→L4 [!A->!B] (α=0.99)` | implication-direction (L3→L4) | N (28s) | N (74s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.9)` | implication-direction (L3→L4) | N (9s) | N (81s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.95)` | implication-direction (L3→L4) | N (7s) | N (77s) | T/o | T/o |
| `Impl L3→L4 [!A->B] (α=0.99)` | implication-direction (L3→L4) | N (7s) | N (82s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.9)` | implication-direction (L3→L4) | N (22s) | N (63s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.95)` | implication-direction (L3→L4) | N (23s) | N (77s) | T/o | T/o |
| `Impl L3→L4 [A->!B] (α=0.99)` | implication-direction (L3→L4) | N (35s) | N (66s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.9)` | implication-direction (L3→L4) | N (8s) | N (77s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.95)` | implication-direction (L3→L4) | N (7s) | N (85s) | T/o | T/o |
| `Impl L3→L4 [A->B] (α=0.99)` | implication-direction (L3→L4) | N (7s) | N (77s) | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.9)` | implication-direction (L4→L5) | N (28s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.95)` | implication-direction (L4→L5) | N (14s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->!B] (α=0.99)` | implication-direction (L4→L5) | N (17s) | T/o | T/o | T/o |
| `Impl L4→L5 [!A->B] (α=0.9)` | implication-direction (L4→L5) | N (69s) | N (9s) | N (14s) | T/o |
| `Impl L4→L5 [!A->B] (α=0.95)` | implication-direction (L4→L5) | N (56s) | N (7s) | T/o | N (116s) |
| `Impl L4→L5 [!A->B] (α=0.99)` | implication-direction (L4→L5) | N (56s) | N (10s) | N (14s) | T/o |
| `Impl L4→L5 [A->!B] (α=0.9)` | implication-direction (L4→L5) | N (32s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.95)` | implication-direction (L4→L5) | N (17s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->!B] (α=0.99)` | implication-direction (L4→L5) | N (20s) | T/o | T/o | T/o |
| `Impl L4→L5 [A->B] (α=0.9)` | implication-direction (L4→L5) | N (53s) | N (8s) | N (15s) | T/o |
| `Impl L4→L5 [A->B] (α=0.95)` | implication-direction (L4→L5) | N (68s) | N (9s) | N (94s) | T/o |
| `Impl L4→L5 [A->B] (α=0.99)` | implication-direction (L4→L5) | N (51s) | N (8s) | N (54s) | N (68s) |

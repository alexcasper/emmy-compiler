# Paired baseline benchmark — submission (all shipped optimizations ON) vs same compiler all-OFF

Protocol: same L4 GPU (Colab, dedicated), same 15 problems, 60 reps/problem/run,
two interleaved rounds per config (order: alloff_r1, allon_r1, alloff_r2, allon_r2),
p50 per run, per-problem value = mean of both rounds' p50. All-off config:
`EMMY_TUNING={"pow2_shift":false,"hoist_invariants":false,"unroll_inner":0}` — the
same compiler at HEAD with every shipped transform explicitly disabled.
Raw: `gen/out/l4lane_results.jsonl` tags `alloff_r*` / `allon_r*` (2026-10-27).

## Per-problem table (L4, sm_89)

| problem | all-off µs | submission µs | delta | shipped transforms that differ here |
|---|---|---|---|---|
| p00_scalar_add | 7.17 | 7.13 | −0.6% | prologue pow2 (timer-floor noise band) |
| p01_vector_add | 7.13 | 7.12 | −0.1% | prologue pow2 (timer-floor noise band) |
| p02_scale_shift | 7.14 | 6.64 | −7.1% | prologue pow2 (rounds disagree 7.1/6.2 — noise) |
| p03_relu_mul | 6.67 | 6.93 | +4.0% | prologue pow2 (rounds disagree — noise, not claimed) |
| r01_array_sum | 7.13 | 6.65 | −6.7% | unroll×4 (StridedLoop) + pow2 |
| r02_big_sum | 26.63 | 13.31 | **−50.0%** | unroll×4 (StridedLoop) + pow2 |
| r03_mean | 17.38 | 10.24 | **−41.1%** | unroll×4 (StridedLoop) + pow2 |
| r04_row_sum | 7.17 | 7.15 | −0.2% | unroll×4 (StridedLoop) + pow2 (neutral) |
| m01_matmul_512 | 439.53 | 62.46 | **−85.8%** | hoist_invariants + unroll×4 (cp.async) + pow2 |
| m02_matmul_rect | 9.22 | 8.19 | −11.2% | hoist_invariants + unroll×4 (cp.async) + pow2 |
| f01_rmsnorm | 9.22 | 9.22 | 0.0% | prologue pow2 only |
| f02_row_softmax | 7.17 | 7.17 | 0.0% | prologue pow2 only |
| f03_l2norm | 7.17 | 7.17 | 0.0% | prologue pow2 only |
| a01_attention | 246.74 | 245.76 | −0.4% | prologue pow2 only (auto-gates keep unroll/hoist OFF) |
| a02_attention_128 | 67.58 | **120.32** | **+78.0%** | **pow2_shift alone (see below)** |

Geomean: all-off **16.51 µs** → submission **13.67 µs** = **−17.2%** net win.
Round consistency: alloff 16.57/16.44, allon 13.70/13.63 (≈0.4% spread).

## The a02 finding (honest regression in the shipped config)

pow2_shift alone flips a02 120.3 → 67.5 µs (isolation run
`a02_pow2off_only`, 60 reps: 67.52). Reproducible across both rounds.

Mechanism NOT confirmed, but refined after loop-body-level diff (aggregate
histograms were misleading — totals are near-identical, the hot loop is not):
the dominant loop body differs materially between variants (406 vs 378
instructions in the main region) — FFMA/LDG interleaving shifts throughout,
and the all-off variant carries I2F/F2I/MUFU div-expansion sequences inside
the body that pow2_shift removed. On this latency-bound matmul+softmax loop,
the reordering alone plausibly explains the swing. Cross-arch static check:
sm_120 shows the same static pattern (416/392 instrs off/on, MUFU 11→10,
IADD3 90→79) with one divergence — on sm_89 the slower (pow2-on) build drops
to 48 registers (56 off), while sm_120 stays at 56 both ways.
Decision still needs sm_120 TIMING evidence; static SASS cannot say whether
the +78% transfers to the judge.

## The two documented regressions (not in the shipped config)

- attention unroll collapse (a01 100→191 µs on the judge): `unroll_inner=auto`
  gates on loop kind + cp.async; attention dot-product loops are excluded.
- dead-load removal −68%: `load_cse` default false, falsified (ae5c59e).
Both appear here only as absent rows: a01/a02 show ~0 delta from them.

## Verdict

Local paired benchmark **confirms** the platform score's basis: the shipped
optimizations deliver a −17.2% geomean improvement over the same compiler
with transforms off, on identical hardware, dominated by m01 (−86%),
r02 (−50%), r03 (−41%), m02 (−11%). It does not reproduce the platform's
absolute 43,522 (different GPU + judge harness); mapping local→judge is not
valid. One honest divergence: a02_attention_128 is +78% slower under the
shipped defaults on sm_89 — filed as a follow-up bead, not a blocker
(net geomean remains strongly positive with it included).

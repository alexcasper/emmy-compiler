# sm_120 A/B — does the a02 pow2 regression transfer? (bead emmy-712 decider)

Box: rented Blackwell node (204.12.188.89, NVIDIA RTX PRO 6000 Blackwell Server
Edition, CC 12.0, 97 GB, CUDA 13.0 driver+nvcc, ubuntu user). Bench artifacts in
this directory: the four variant PTX sources (header-rewritten to
`.version 8.8` / `.target sm_120`, compiled locally with our staged ptxas
12.9.86 `-arch=sm_120 -O3` so all four share one toolchain) and
`l4_bench_t.py` (timing-only cupy runner; torch is not installed on the box —
correctness was already gated on the judge and the sm_89 lane; this run is
timing-only by design).

## Protocol

Interleaved rounds: per problem, alternating NO/YES config, 4 rounds, 200 CUDA-
event reps per run, p50 per run, warmup 20. Inputs: seeded cupy randoms (values
irrelevant to timing). 2026-10-28 16:20-16:45 UTC.

Variants (per the two-knob scheme, commit c5a3f1e):
- a02 pow2=NO = shipped default (pow2_shift_softmax=false)
- a02 pow2=YES = `{"pow2_shift_softmax":true}` (the sm_89-regressed path)
- m01 pow2=YES = shipped default; m01 pow2=NO = `{"pow2_shift":false}`

## Results (p50 µs per round)

| round | a02 NO | a02 YES | paired Δ | m01 NO | m01 YES | paired Δ |
|---|---|---|---|---|---|---|
| 1 | 73.92 | 76.43 | +3.4% | 24.61 | 21.39 | −13.1% |
| 2 | 74.08 | 73.92 | −0.2% | 24.78 | 23.46 | −5.3% |
| 3 | 73.97 | 74.56 | +0.8% | 24.42 | 23.46 | −3.9% |
| 4 | 71.90 | 76.64 | +6.6% | 23.42 | 22.21 | −5.2% |
| **mean** | **73.47** | **75.39** | **+2.6%** | **24.31** | **22.63** | **−6.9%** |

Register counts (ptxas 12.9 -arch=sm_120): a02 **56 / 56** both ways;
m01 39 (YES) / 40 (NO).

## Verdict: DOES NOT TRANSFER

- **a02**: sm_89 measured **+78%** with pow2 applied (67.6→120.3 µs); sm_120
  measures **+2.6% mean / +2.1% median**, with 2 of 4 paired rounds inside
  noise. The register cliff does not exist on sm_120 (56 regs both ways —
  matching the static prediction) and the hot-region reordering that hurt
  sm_89 is harmless here.
- **m01 control**: the ~9% isolated pow2 win **replicates**: −6.9% mean,
  −5.2% median, YES < NO in **4/4 rounds**. Slightly smaller than sm_89's
  −9.6% but unambiguous.
- **Shipped defaults are correct for the judge arch**: the two-knob scheme
  gives up nothing on sm_120 (a02's gating is free there) and keeps the m01
  win. `pow2_shift_softmax` can stay default-off permanently; the judge-side
  A/B question in emmy-712 is now answered — bead can close.

## Failure modes hit (logged per protocol, none debugged past)

- Box had no pip (`ensurepip` absent, PEP 668 externally-managed) → bootstrapped
  get-pip.py with `--user --break-system-packages`; numpy+cupy-cuda13x 14.2.0
  installed in ~40 s.
- No torch on the box → timing-only runner (`l4_bench_t.py`), correctness not
  re-checked (already judge-gated).
- `which nvcc` empty (CUDA at /usr/local/cuda/bin, not on PATH) — irrelevant:
  cubins were cross-compiled locally; only the driver JIT/runtime is used.
- Round-to-round drift up to ~4% on m01 round 1 (first-run clock ramp) — why
  the verdict uses 4/4-round sign consistency + paired medians, not single runs.

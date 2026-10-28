# sm_120 silicon hypothesis tests — rented Blackwell box session 2 (2026-10-28)

Box: RTX PRO 6000 Blackwell Server Edition (CC 12.0), CUDA 13.0 stack, 16:45–18:10 UTC
(hard stop 21:15). Method: hand-written PTX microkernels (this directory, `gen_micro.py`
regenerates them), cross-compiled with our staged ptxas 12.9.86 `-arch=sm_120 -O3`,
cycle counts read IN-KERNEL via `%clock64` (min = p50 = p90 on every measurement —
the box is dedicated and the numbers are deterministic; 30 launches each).
Baseline sanity: dependent FADD chain 4.03–4.27 cycles/op, dependent FFMA 4.03 —
matches known Blackwell FP32 latency, so the harness sees what it should.

## H1 — UI2F.U32.RP constant materialization: REFUTED as a cycle win

Claim (sm120/README.md, tracer observation): ptxas materializes small float
constants as UI2F of the integer on the uniform datapath — hypothesis: does that
trick win cycles vs fp-immediate alternatives?

Result: the two variants compiled to IDENTICAL SASS (ptxas folds
`cvt.rn.f32.u32 f, <literal>` to the same fp immediate it would use anyway) and
timed identical: **h1_u2f 8416 cycles == h1_fpimm 8416 cycles** (4096 FMA each,
4.10 cycles/FMA — pure FFMA latency).

**Verdict: REFUTED as a timing claim; cycle-neutral.** UI2F materialization is
an encoding-density choice (immediate in the operand field vs a 32-bit literal
load), not a speed optimization. The emission-behavior observation itself stays
CONFIRMED (it is what ptxas emits for uniform int-derived constants — seen in 8/16
traced kernels). KB note updated.

## H2 — 1-bit matmul emulation path: CONFIRMED (real speedup vs scalar), cost quantified

Claim (verify/RESULTS.md, static): sm_120 has no BMMA hardware; 1-bit
`mma.sync.m16n8k256` lowers to a CALL into `__cuda_sm_10x_mma_bit_internal_*`
built from IMMA.16832.U8.U8 + MOVM.U4TO8.M832. Silicon adds the numbers.

SASS shape re-confirmed live: each mma.sync = **one `CALL.REL.NOINC` per op** (the
routine is NOT inlined), loop driven by `BRA.U` (uniform branch — first in-tree
sighting of the KB's BRA.U page in real codegen).

| kernel | cycles | work | per-op | bit-throughput |
|---|---|---|---|---|
| bmma emulation | 976,746 | 2048 × m16n8k256 (2048 CALLs) | **477 cycles/mma** | 0.0146 cyc/bit |
| scalar xor+popc+add | 856,151 | 98,304 groups (32 bit-ops each) | 8.71 cycles/group | 0.272 cyc/bit |

**Verdict: CONFIRMED — the emulation is ~18.6× faster in bit-throughput than the
scalar xor+popc equivalent** (the IMMA tensor-core bulk dominates the per-op CALL
overhead). New absolute number for the KB: **477 cycles per emulated m16n8k256
1-bit MMA** — for scale, hardware BMMA on Ada issues in single-digit cycles, so
the "1-bit tensor core" is ~2 orders of magnitude slower per op here; it wins by
massive bit-parallelism, not by being a fast instruction.

## H3 — MUFU latency/throughput on sm_120: MEASURED (first numbers; no doc claims existed)

Latency (64-op dependent chains + nudge FADD; subtract FADD 4.27):

| op | guarded? | cycles/iter | implied MUFU latency |
|---|---|---|---|
| rcp.approx.**ftz** | no | 24.6 | **~20 cyc** |
| ex2.approx.ftz | no | 24.6 | **~20 cyc** |
| tanh.approx | no | 24.6 | ~20 cyc |
| rcp.approx (non-ftz) | **yes** | 44.6 | ~20 + ~20 of guard |
| sqrt.approx (non-ftz) | **yes** | 44.6 | ~20 + guard |
| div.rn.f32 | IEEE path | 73.2 | — (FCHK+MUFU+FFMA+CALL) |
| FADD baseline | — | 4.27 | — |

Two KB-worthy discoveries from the SASS:
1. **Non-ftz rcp/sqrt get a 5-instruction denormal guard** (2×FSETP + 2×FSEL +
   FMUL/FFMA around every MUFU) — even in straight-line code, always. On sm_120
   the effective cost of plain `rcp.approx.f32` is ~6 instructions / ~40 cycles
   dependent, NOT 1 instruction / 20. `.ftz` variants emit bare MUFU. Our
   compiler's `rcp: approx` knob emits non-ftz → we pay the guard everywhere.
   (Follow-up: switch approx knobs to ftz forms — the kernels are
   denormal-insensitive by the same domain arguments as pow2_shift.)
2. `div.rn.f32` costs **73.2 cycles** on sm_120 (the FCHK+MUFU+FFMA+CALL
   expansion) — 3.4× a guarded rcp.approx, 18× an ftz MUFU.

Throughput: with 8 independent chains, rcp.approx.ftz still costs 24.1 cycles/op
(6174 cycles / 256 ops) — **no throughput overlap observed**; MUFU behaved
latency-serialized in this shape. Flagged INCONCLUSIVE-leaning-slow rather than
claimed: needs a wider sweep (more warps/partitions) before claiming a
throughput number. NAK models MUFU as pipe-class Decoupled with no numeric
latency — our numbers are the first in the KB.

## H4 — dual-issue / register banking: SKIPPED

The KB marks no dual-issue or banking claim as static-only/unverified (grep over
sm120/ RESULTS + SASS pages: nothing to test). No silicon time spent.

## Summary verdicts

| # | hypothesis | verdict |
|---|---|---|
| H1 | UI2F materialization wins cycles | **REFUTED** (cycle-neutral, encoding-only) |
| H2 | 1-bit emulation beats scalar | **CONFIRMED** (18.6×; 477 cyc/mma quantified) |
| H3 | MUFU latency/throughput vs docs | **MEASURED** — ~20 cyc ftz; 73.2 div.rn; guard tax quantified; no doc numbers to compare |
| H4 | dual-issue/banking | SKIPPED — no unverified KB claims |

Harness: `gen_micro.py` (kernel generator), `micro.py` (runner), `manifest.json`
(cubin → entry name). Same paired/interleaved philosophy: deterministic in-kernel
cycle reads, min=p50=p90 on all kept numbers; the one flagged-inconclusive
measurement (MUFU multi-chain throughput) is labeled as such rather than rushed.

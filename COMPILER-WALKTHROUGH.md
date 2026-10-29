# COMPILER-WALKTHROUGH.md — how our compiler treats each benchmark kernel

*This walks all 15 benchmark kernels through the full pipeline: what each kernel
computes, which transforms the compiler applies (and why only those), what comes
out of ptxas, and the measured numbers where we have them. Written to be read top
to bottom; every claim links to its evidence.*

## The pipeline in one page

```
task/problems/<name>/<name>.ir.json        the input: a tiny IR graph (inputs,
      |                                    one KernelOp, a statement tree)
      v
compile.py  (this repo)                    walks the statement tree ONCE, in
      |                                    source order, emitting PTX text; the
      |                                    tuning knobs (EMMY_TUNING env json)
      |                                    decide which transforms fire
      v
   kernel.ptx                              virtual registers everywhere, one
      |                                    .visible .entry, params = .u64 buffer
      |                                    pointers (entry name & arg order come
      |                                    from the IR/meta — never ours)
      v
ptxas -O3 -arch=<sm_89|sm_120>             NVIDIA's assembler: register
      |                                    allocation, scheduling, the thing our
      |                                    optimizations actually negotiate with
      v
   cubin  ->  nvdisasm -c                  disassembly back to SASS text
      |
      v
tools/trace.py + sm89/ & sm120/ KBs        every SASS opcode mapped to its KB
                                           page (encoding, evidence, cost)
```

Two things make this pipeline unusual. First, the compiler emits PTX with
**virtual registers only** — we never allocate; allocation is ptxas's job, and
every optimization below is an argument about what we hand it. Second, **every
optimization is gated by a measured rule, not a heuristic that seemed right**:
four of them shipped off-by-default with their falsification documented.

### The knobs (what CAN fire)

| knob | default | rule when "auto"/on | measured basis |
|---|---|---|---|
| `pow2_shift` | on | `/`,`%` by power-of-2 constant → `shr`/`and` instead of ptxas's float-reciprocal expansion | +9% on m01 isolated (L4, 200-rep interleaved) |
| `pow2_shift_softmax` | **off** | pow2 also for softmax-class kernels (body contains `exp`) | +78% regression on a02/sm_89; see its section |
| `hoist_invariants` | auto | hoist loop-invariant address math to preheaders **iff kernel has cp.async** | m01 3.2×; −8-9% on attention |
| `unroll_inner` | auto | ×4 unroll: StridedLoop bodies (reductions) always; Loop bodies (dot products) only in cp.async kernels | r02 −27%; a01 100→191µs unrolled |
| `fuse_loops`, `load_cse` | **off** | — (falsified) | a01 68% slower; deleted loads were free L1 hits |
| `div`/`sqrt`/`rcp` | "rn" | approx forms lower to MUFU | sm_120: non-ftz approx carries a 5-instr guard; div.rn = 73 cyc [bench/sm120_hypotheses] |
| `stage_column`, `maxnreg` | off/none | falsified / judge-tunable | emmy-604; a01 128-reg cliff |

### The kernel classes (why the gates exist)

The IR has no "kernel type" tag, so the compiler derives structure cheaply at
compile time. Every kernel in the benchmark set falls in one of these classes:

| class | test (structural) | kernels |
|---|---|---|
| pointwise | no loops at all | p00–p03 |
| reduction | has a `StridedLoop` body | r01–r04, f01, f03 |
| softmax-family | body contains `exp` | a01, a02, f02 |
| async (tile-staged) | body contains `CpAsyncCopy` | m01, m02 |
| matmul | async ∧ has a `Loop` (dot-product) body | m01, m02 |

The gates compose: hoisting and inner-unrolling need cp.async; StridedLoop
unrolling doesn't; pow2 avoids the softmax family by default. Nothing here is
semantic — all three tests are single walks over the statement tree.

---

## Kernel-by-kernel

Measured numbers: **L4** = paired A/B on a dedicated L4 (sm_89, 60–200 reps,
interleaved rounds, in bench/PAIRED_BASELINE.md); **B200-class** = the rented
RTX PRO 6000 sm_120 box (bench/sm120_ab); **judge** = platform score runs.

### p00_scalar_add — `torch.randn(128) + torch.randn(128)`
grid 1×256, no loops, straight-line body. The compiler's work here is the axis
decode (`gid` → element index) and nothing else: with `pow2_shift` on, the decode
emits `shr`+`and` instead of `div`+`rem`; there is no loop to hoist or unroll.
ptxas output is a trivial `LDG; FADD; STG` chain. L4: 7.17→7.13µs — both numbers
are at the timer floor; p00–p03 are correctness anchors, not timing targets.

### p01_vector_add — `randn(1024) + randn(1024)`
Same story at 2 blocks. 7.13→7.12µs. Timer floor.

### p02_scale_shift — `randn(4096) * 2.0 + 1.0`
Constant multiply/add folds into the FADD/FMUL stream; 7.14→6.64µs, but the
paired rounds disagree (7.1/6.2) — treat as noise, not a claim.

### p03_relu_mul — `relu(x) * y`
`relu` lowers to `max.f32 x, 0` inline (no branch). 6.67→6.93µs (+4%, rounds
disagree — noise band again; the only "slower" pointwise row, unclaimed).

### r01_array_sum — `randn(1024).sum()`
One `StridedLoop` (threads stride the array; per-thread partials + shared-memory
tree at the end). Transforms that fire: **unroll×4** (StridedLoop rule: always)
and **pow2_shift** (axis decode). L4: 7.13→6.65µs (−6.7%). The win is loop-overhead
amortization: 4 elements per branch/check instead of 1.

### r02_big_sum — `randn(65536).sum()`
Same shape, 64× more data — the loop body is a larger fraction of runtime, so the
same transforms pay more: L4 **26.63→13.31µs (−50.0%)**. This is the kernel the
unroll-always policy was measured on originally (judge runner: 41→30µs, −27%).

### r03_mean — `randn(32768).mean()`
Sum, then **one float division by the runtime length** — the only benchmark
kernel with a genuine `div` in the hot path (pow2_shift can't touch it: 32768 is
a pow2 but the divisor is a runtime value, not a literal). With default `div: rn`
ptxas emits the IEEE sequence; on sm_120 that path measures **73 cycles/op**
[bench/sm120_hypotheses] — a candidate for the approx knobs if tolerance ever
allows. L4: 17.38→10.24µs (−41.1%) from unroll×4.

### r04_row_sum — `randn(64, 512).sum(-1)`
2D: row loop (StridedLoop) per block. Unroll×4 fires; the extra memory traffic
makes it neutral: 7.17→7.15µs (−0.2%). Instructive: unrolling helps when loop
overhead dominates, and here it doesn't — the policy is coarse but safe.

### f01_rmsnorm — RMSNorm(64×1024)
Reduction (sum of squares → mean → `sqrt` → per-element scale). StridedLoop
unroll applies; the `sqrt` uses the knob (default `rn`, no MUFU). This kernel is
where the tracer first saw **`UI2F.U32.RP`** — ptxas materializing the 1/N float
on the uniform datapath by converting the integer N. Silicon test 2026-10-28:
that trick is cycle-neutral (encoding-density only) — sm120/README.md. L4: 9.22
→ 9.22µs, exactly neutral.

### f02_row_softmax — `softmax(64×256, dim=-1)`
Max, exp, sum, divide — softmax-family (`exp` present), so **pow2_shift is
gated off** here (`pow2_shift_softmax=false`). The `exp` always lowers through
`ex2.approx.f32` (hardcoded — exp's semantics are approximate by design).
StridedLoop unroll ×4 fires on the reduction loops. L4: 7.17→7.17µs — the knob
gating costs nothing measurable either way on this kernel (which is why the
class gate is safe to include it).

### f03_l2norm — `x / sqrt(sum(x²))`
Reduction + `sqrt` (knob, `rn` default) + a scale (multiply by reciprocal, not a
divide — the IR already shapes it that way). StridedLoop unroll fires. L4: 7.17
→ 7.17µs, neutral.

### m01_matmul_512 — `randn(512,512) @ randn(512,512)`
**The flagship.** grid 128×512 threads, 72 KB shared memory per block. The IR
stages input tiles through shared memory with `CpAsyncCopy` (global→smem
bypassing registers, commit/wait-group pipelining), then runs a Loop-kind
dot-product inner loop reading only from shared memory.

Everything fires here, and this is the kernel every win was measured on:
- `hoist_invariants` (auto → cp.async present): the tile-staging loop recomputed
  flat addresses every iteration; hoisting moved the invariant base math to the
  preheader. Judge-runner 3.2×.
- `unroll_inner` (auto → cp.async ∧ Loop body): ×4 replication of the inner
  FMA batch. Judge-runner 37.7→29.5µs on top of hoisting.
- `pow2_shift`: removes the float-reciprocal div expansions from the staging
  path. Isolated: **~9%** (L4, 200-rep interleaved) — and it replicates on
  sm_120 (−6.9%, 4/4 rounds, bench/sm120_ab).
- Inner-loop SASS: 32 instructions, 16 FFMA, 6 LDS, **0 LDG** — every operand
  already staged.

Numbers: L4 **439.5→62.5µs (−85.8%)** paired vs all-off; sm_120 22.6µs (paired
−6.9% for pow2 alone). The kernel that justifies the whole tuning surface.

### m02_matmul_rect — `randn(128,256) @ randn(256,64)`
Same structure, rectangular, no smem (small tiles stay in registers — zero
`smem_bytes` in meta, so the async path is pure cp.async→register staging).
Same gates fire. L4: 9.22→8.19µs (−11.2%).

### a01_attention — attention over 64×64, grid 4×128
**The wall.** One Loop-kind dot-product body; no cp.async; exp present. By the
gates: no hoisting, no unrolling, no pow2 (softmax-class) — the shipped config
changes almost nothing here, *deliberately*, because every attempt to optimize
this kernel measured worse:

| attempt | result (a01) |
|---|---|
| unroll ×2 (forced) | 100→191µs on judge — latency-bound chains get longer, not faster |
| load_cse (dedupe the 4× kt reads) | −68% — the "redundant" kt loads are free L1 broadcast hits and the kernel's memory-level parallelism |
| fuse_loops | −68% (same mechanism, ae5c59e) |
| smem staging (emmy-604) | 244.7 vs 245.8µs — no win, closed |
| pow2 (softmax gate) | −0.4%, neutral |

The kt column is read 4× per softmax step by design; those loads hit L1 and
keep 321 loads in flight in a 1368-instruction hot loop. L4: 246.7→245.8µs (−0.4%).
The lesson: **for a01 the optimal transform set is empty**, and the gates exist
to encode exactly that.

### a02_attention_128 — attention over 128×32, grid 128×32
Structurally a01's sibling (Loop body, exp, no cp.async) — and the reason
`pow2_shift_softmax` exists. Timeline of the evidence:

1. `426aae8` ships pow2_shift + hoisting jointly (m01 3.2× measured jointly).
2. `649a094` isolates pow2: −9% on m01 — but the paired 15-kernel sweep catches
   **a02 +78%** (67.6→120.3µs L4, reproducible 2 rounds).
3. `46c4649` digs into SASS: the hot region reorders (406 vs 378 instrs) and
   sm_89's register count drops 56→48; sm_120 static shows the same instruction
   pattern but holds 56 regs both ways — transfer unknown.
4. `c5a3f1e` gates it: `pow2_shift_softmax=false` default. L4 re-verify: m01
   63.49µs (win preserved), a02 67.58µs (= all-off baseline, regression gone),
   knob-on 120.29µs (knob demonstrably controls it).
5. `d95f72a` decides on silicon: on sm_120 the regression **does not transfer**
   (+2.1% median; 56/56 regs) while m01's win replicates. Default stays off —
   free insurance either way.

L4 paired: 67.58 (off) vs 120.32 (on). sm_120: 73.5 vs 75.4µs.

---

## Reproduce any of this

```bash
# full 15-problem correctness+score gate (what the judge does)
python bench/eval.py compile.py

# paired all-off vs shipped-defaults (the -17.2% table)
EMMY_TUNING='{"pow2_shift":false,"hoist_invariants":false,"unroll_inner":0}' \
  python gen/l4_lane.py --reps 60          # needs the L4 lane
python bench/eval.py compile.py           # defaults

# trace any kernel through ptxas -> nvdisasm -> KB cross-reference
python tools/trace.py --ptx <file.ptx> --out traces/baseline
```

Evidence map: bench/PAIRED_BASELINE.md (paired sweep), bench/sm120_ab (a02
transfer decision), bench/sm120_hypotheses (MUFU/UI2F/bmma silicon), traces/
(all 15 kernels' PTX→SASS with per-instruction KB links), DESIGN.md (the
decision log this document summarizes).

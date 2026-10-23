# DESIGN.md — how this compiler works

`compile.py` lowers Emmy's Kernel IR to PTX in a single pass. It reads one
`kernel.ir.json` path from `argv[1]` and writes PTX to stdout:

```
python compile.py path/to/kernel.ir.json > out.ptx
```

The IR is loaded with emmy's own `Graph.from_dict` (the body only deserializes
through emmy's classes — emmy is used to *read*, never to *render*; all
lowering in this repo is ours). Status: **all 15 open problems pass** through
`submit.py --compiler` (pointwise, reductions, matmul, fused, attention-like).

## Pipeline

1. **Load** — find the `KernelOp` node; entry name = `op.name`; parameters =
   node `inputs` then `outputs` (which is what `meta.json`'s `arg_order`
   holds), each a `.u64` buffer pointer.
2. **Prologue** — `.version 8.0` / `.target sm_89`, one `ld.param.u64` +
   `cvta.to.global.u64` per buffer, `%tid.x`, and eager `lane = tid & 31`,
   `warp = tid >> 5` registers.
3. **Walk** — recursive descent over the statement tree, translating one
   statement kind at a time. Expressions (index math) are compiled on demand.
4. **Emit** — fresh virtual registers for every SSA value; declaration counts
   are back-patched from the final text. `ptxas` does real register
   allocation; we do none.

## Key design decisions

**Tile decode is arithmetic, not data.** The Tile's axes define the iteration
space: `_gid = blockIdx.x * block_threads + tid`, guard `_gid < N`, then
`a_i = gid / s_i % e_i` with `s_i` the product of the inner extents. Two
rules that cost us a bug each:

- *Only the outermost axis may skip the `%`* — the guard bounds it. Inner
  extent-1 axes must still be modded (by 1) or they leak the raw quotient
  into every index expression they feed (this broke `a02`, where an
  extent-1 `a5_b` pushed the `v` column out of range).
- Extra threads beyond `N` (e.g. `p00`: 256 threads, 64 cells) are guarded
  unconditionally; the branch costs nothing and the guard is uniform, so
  barriers inside the guarded region stay legal.

**Registers: SSA everywhere except accumulators.** Every `Load`/`Assign`/`Let`
result gets a fresh virtual register — no liveness analysis, `ptxas` handles
it. `Accum` is the one exception: it is loop-carried state, so it *updates
its register in place* (`acc = add(acc, v)`), with the register created by
an identity seed.

**Accumulator ownership.** An accumulator's `axes` field names the loop it
folds over. A `seed=True` loop seeds (writes the identity to) exactly the
accumulators *defined inside its own body subtree* whose `axes` contain the
loop's axis. Scoping by body subtree matters: `a01` has four *sibling* loops
over the same axis `a2`, one per accumulator — seeding globally at each loop
entry would let the last sibling clobber the first three (this broke `a01`:
rows 0-2 of every output tile read identity 0). `Init` statements opt out of
seeding: the named accumulator is declared once at the top and updated in
place across chunk loops (`m01`).

**The combine vocabulary is generic.** `WarpShuffle` and `TreeHalve` carry an
arbitrary `combine_states` program over `(state, state_b)` register pairs.
We emit, per butterfly offset (16, 8, 4, 2, 1): one `shfl.sync.bfly.b32` per
state, then the IR's own combine program — that handles both plain `add`
reductions and the online-softmax rescale (`f02`, `a01`) with no special
cases. `TreeHalve` runs the shared-memory tree (`warp < s` guard, per-step
`bar.sync`) and broadcasts the root.

**exp is `ex2.approx`.** `exp(x)` lowers to `ex2.approx.f32(x * log2e)`.
Every problem using exp has rtol ≥ 1e-3; the approx instruction's ~1 ulp
error is invisible. `reciprocal`/`divide`/`sqrt` use the `.rn` (correctly
rounded) forms to stay well inside tighter tolerances elsewhere.

**Vector loads/stores.** A `Load`/`Write` with 2 or 4 consecutive values
emits one `ld/st.global.v2/v4.f32` (mirroring emmy's float2/float4 grouping);
single values stay scalar. Atomics emit `red.global.add.f32` per value.

**Shared memory: static below 48 KiB, extern pool above.** PTX caps static
`.shared` at 48 KiB per block. Totals above that (`m01` needs 72 KiB) are
carved out of one `.extern .shared` pool at 16-byte offsets — the runner
launches with `meta.json`'s `smem_bytes`, which was already sized for the
dynamic allocation. Below the limit we declare one static array per `Smem`.

**cp.async.** `CpAsyncCopy` emits `cp.async.cg.shared.global` for 16-byte
copies (`.ca` otherwise), with the shared address computed from the smem
row/col index (plus `lane_index` when present) and the global address from
the source index. Commit/wait map one-to-one.

## Pitfalls found the hard way (kept here so the video can show them)

- **PTX `0f` float literals are big-endian bit patterns.** Packing
  little-endian turns `1.0` into `0f0000803F` ≈ 9e-41. It assembles cleanly
  and the kernel computes plausible garbage — it only surfaced in `f02`,
  where the online softmax rescales by a `Let(one, 1.0)`. Diagnosed by
  instrumenting the running kernel on the runner and comparing `acc0`/`acc1`
  against numpy.
- **PTX register vectors are 0-indexed**: `%rd<16>` covers `%rd0..%rd15`, so
  declare `max_index + 1`.
- **Special registers can't be instruction operands**: `%ctaid.x` needs a
  `mov.u32` first; only `mov` may read it.
- **Loop-carried values must not get fresh SSA registers.** The first
  reduction run summed only the last iteration: the add read the identity
  register every time.

## What we did not build

No TMA/mbarrier, no `wgmma`/`mma.sync` tensor cores (no open problem needs
them), no `Pre`/`Carry`/`Select`/`ZeroPrologue`, no dynamic shapes, no
`serial` axes, no aux (producer-warp) tiles — the decode supports them but
no open problem exercises it. Loops marked `unroll` are emitted as real
loops; `ptxas` still pipelines them.

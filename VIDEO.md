# VIDEO.md — outline for the 3-5 minute submission video

For alex to record in his own voice (prize-eligibility requirement: the video
must show *you* understand the compiler). Each section cites the file/lines to
show on screen. Aim: 4 minutes.

## 1. The problem (0:00–0:40)

- Emmy compiles PyTorch to CUDA C++ and builds with `nvcc`; the autotuner
  compiles thousands of variants, so the ~19x faster `ptxas` path matters.
- My entry: `compile.py` — Emmy Kernel IR in, PTX out. One command:
  `python compile.py problems/r01_array_sum/*.ir.json > out.ptx`
- Show: run it live, then `submit.py r01_array_sum --compiler compile.py`
  passing on the RTX 5090 runner.

## 2. The shape of the compiler (0:40–1:40)

- Three stages: load the IR with emmy's own `Graph.from_dict` (emmy is the
  *reader*; every line of lowering is ours), walk the statement tree, emit
  PTX one statement kind at a time.
- Registers: fresh virtual register per SSA value, declaration counts
  back-patched; `ptxas` does the real allocation. Show `compile.py:106` and
  the `.reg` splice (`assemble`).
- Show a Tile decode: `_gid`, the guard, `a_i = gid / s_i % e_i` — and the
  guard catching p00's extra threads (256 threads, 64 cells).

## 3. Three ideas worth telling (1:40–3:10)

- **Accumulators are the one exception to SSA.** They are loop-carried state:
  the seed writes the identity (`add`→0, `max`→−1e30) just before the loop
  that owns them, and the Accum updates the register in place. Ownership is
  scoped to the loop's own body — show a01's four sibling `a2` loops
  (DESIGN.md "Accumulator ownership").
- **The combine programs are generic.** WarpShuffle/TreeHalve carry the IR's
  own `combine_states`; emitting one butterfly shuffle per offset + the IR's
  program handles both plain sums and the online-softmax rescale — no
  special cases for softmax. Show f02 passing at 7e-9 error.
- **Above 48 KiB, shared memory goes dynamic.** m01's 72 KiB staging buffers
  are carved out of one `.extern .shared` pool; cp.async fills it
  double-buffered. Show m01 passing.

## 4. A debugging story (3:10–3:50)

- The f32-literal bug: PTX `0f` constants are big-endian bit patterns; my
  first pack was little-endian, so `1.0` became a 9e-41 denormal. It
  assembled fine and only f02 blew up. Tell how it was found: dumped the
  running kernel's `acc0`/`acc1` through the runner's API — max was right,
  the sum was exactly `beta * one`. (This is the best 40 seconds of the
  video: it shows real understanding of both the IR and the tooling.)

## 5. Results + what's not there (3:50–4:10)

- All 15 open problems pass; the compiler handles the full statement
  vocabulary the open set uses. DESIGN.md lists what's deliberately not
  built (TMA, tensor cores) — nothing the categories exercise.
- Close on: hidden set is the same five categories with different shapes;
  nothing is hardcoded — every number comes from the IR at compile time.

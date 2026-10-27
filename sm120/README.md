# sm120 knowledge base (Blackwell consumer, compute capability 12.0)

Reference for writing PTX that targets `sm_120` and reading the SASS that `ptxas` produces from it.
Every fact below carries a reference tag: **[n]** = a cited document (listed at the end), **[probe: x]** =
reproduced by compiling with NVIDIA's real `ptxas`/`nvdisasm` (see [verify/RESULTS.md](verify/RESULTS.md)).
Methodology is the same as the sibling [sm89 KB](../sm89/README.md); every sm_120 claim is derived from
sm_120 probes, not carried over from sm_89.

| path | what |
|---|---|
| [sass/INDEX.md](sass/INDEX.md) | **Start here for SASS.** All 126 opcodes observed on sm_120 (4112 probe instructions) by category: NVIDIA's official description, which PTX/CUDA produces it, the observed 12-bit opcode values, and the sm89↔sm120 divergence tables |
| `sass/<OP>.md` | Per-opcode observations: syntax forms seen in real ptxas output, observed 128-bit encodings, intersect-derived fixed bits (observation-derived, partial), NAK cross-check status, and an Evidence section |
| [ptx/INDEX.md](ptx/INDEX.md) | **Start here for PTX.** Every PTX instruction with an sm_120 availability column derived from NVIDIA's "Target ISA Notes" (PTX ISA 8.8, CUDA 12.9.1) |
| `ptx/instructions/NN-<family>/` | PTX ISA chapter 9.7, one file per instruction section (NVIDIA text, converted) |
| `ptx/NN-*.md` | Other PTX ISA chapters (syntax, state spaces, memory model, special registers, directives...) |
| [verify/RESULTS.md](verify/RESULTS.md) | 136 PTX→SASS probes compiled for sm_120: claimed vs. emitted opcodes, the sm_89→sm_120 divergence table, control-code decoding, and PTX that sm_120 rejects |
| [verify/NAK_CROSSCHECK.md](verify/NAK_CROSSCHECK.md) | Probe-derived opcode numbers cross-checked against Mesa's open-source NVK compiler [4] |
| `tools/`, `verify/*.py` | Scripts that regenerate everything |

## Sources and how much to trust each part

| content | source | status |
|---|---|---|
| PTX chapters | NVIDIA PTX ISA manual 8.8, frozen CUDA 12.9.1 archive [1] | Verbatim NVIDIA text, converted by pandoc. The sm_120 column is a heuristic over NVIDIA's notes. Family-gated features (sm_90a `wgmma`/`setmaxnreg`, sm_100a `tcgen05`/`redux.f32`/FP4 `cvt`) were probe-checked: `ptxas -arch=sm_120` rejects each for architecture reasons [probe: no_*] |
| SASS opcodes + encodings | Our own probes only | There is **no kuterdinel-style encoding site for sm_120** (and no independent SASS encoding reference for Blackwell consumer at the time of writing). `sass/*.md` therefore document observed ptxas output: 153 accepted probe kernels, 4112 instructions, 126 opcodes, every raw 128-bit encoding captured. Per-opcode "fixed bits" are intersect-derived observations, not a complete encoding spec [probe: sass/*] |
| Opcode numbers (independent) | Mesa NAK `sm70_encode.rs` [4] | 62/67 same-named opcodes agree on the 9-bit base opcode, 3 more are NAK family ops that map onto observed ones, 2 differ (SULD/SUST — an inherited field-layout question, detailed in NAK_CROSSCHECK.md); 59 observed opcodes are not emitted by NAK |
| SASS descriptions | NVIDIA CUDA Binary Utilities opcode table, Blackwell/Rubin section [2] | Official NVIDIA one-liners, merged into `sass/*.md` |
| "Typically emitted for" | Ours (`tools/build_sass.py` CATALOG) | Each opcode page lists exactly which probes emitted it and how many instances were observed |

Regenerate with `python3 sm120/tools/build_ptx.py && PTXAS=... NVDISASM=... python3 sm120/verify/probes.py && python3 sm120/tools/build_sass.py` (needs `pandoc` for the PTX docs). The probe tools are staged in `toolchain/cuda12.9/bin/` (gitignored): `ptxas` 12.9 (V12.9.86, from the `nvidia-cuda-nvcc-cu12` wheel) and `nvdisasm` 12.9 (V12.9.88, from the `cuda-nvdisasm-12-9` deb — NVIDIA does not publish an nvdisasm wheel). No GPU needed. Downloads are cached in `sm120/.cache/` (gitignored).

## Toolchain facts

- **`ptxas` accepts `-arch=sm_120`** from CUDA 12.8+; the staged 12.9 pair assembles and round-trips (`ptxas` → cubin → `nvdisasm -c`) [probe: trivial].
- **`.target sm_120` requires PTX ISA ≥ 8.7** [1; probe: `.version 8.5` + `sm_120` is rejected, 8.7 assembles]. CUDA 12.8 ships PTX ISA 8.7, 12.9 ships 8.8; this KB pins 8.8.
- `nvdisasm -hex -c` prints both 64-bit words of each 128-bit instruction — that is the encoding source for everything in `sass/` [probe: all].

## sm_120 at a glance

- **Occupancy limits (CC 12.0):** 64K 32-bit registers per SM, at most 255 per thread; at most 32 resident blocks, 48 warps and 1536 threads per SM [3, Technical Specifications per Compute Capability].
- **Shared memory:** 100 KB per SM max, 99 KB per thread block, 32 banks [3]. Shared addresses in SASS are plain register or uniform-register offsets (`LDS R7, [R5+0x4]`, `ATOMS.ADD R5, [UR4], R0`) [probe: lds_sts, atoms].
- **Kernel parameters:** first `.u64` param = `c[0x0][0x380]`, second = `c[0x0][0x388]` (constant bank 0) [probe: prologue, uniform_loop]. Kernel info loads as `LDC R1, c[0x0][0x37c]` and the **global-memory descriptor** as `LDCU.64 UR4, c[0x0][0x358]` [probe: every probe's prologue]. Divergence from sm_89: params moved from `c[0x0][0x160]`, and there is no `MOV R1, ...` + `ULDC.64` prologue — params load via LDC/LDCU directly.
- **Descriptor-based global addressing is universal:** every global load/store compiles to `LDG.E/STG.E desc[UR4][R2.64]` — the address is a register pair and the memory descriptor comes from constant bank 0 via a uniform register [probe: all]. On sm_89 most code used plain register addresses.
- **PTX header:** `.version 8.7`+ and `.target sm_120`.

## sm_89 → sm_120 divergences (the short list)

Full evidence in [verify/RESULTS.md](verify/RESULTS.md) "sm_89 → sm_120 divergences" [probe: each linked probe]:

- **Renamed:** IMNMX → **VIMNMX**; RED → **REDG** (with explicit memory-order/scope qualifiers like `.STRONG.GPU`); STM → **STSM.16** (stmatrix); ULDC → **LDCU**; elect.sync → **ELECT**; st.async → **STAS**; cp.async.bulk → **UBLKCP** (+ **UBLKPF** prefetch, **SYNCS** group sync); barrier.cluster → **UCGABAR_ARV/UCGABAR_WAIT**; griddepcontrol → **ACQBULK** / **PREEXIT**.
- **Removed:** HADD2/HMUL2 (folded into HFMA2), BMMA (b1 `mma.sync` CALLs an internal sm_10x routine built from IMMA.16832 + new MOVM.U4TO8), VABSDIFF4 (emulated via VIMNMX.U8x4 + VIADD.U8x4 + IDP.4A), ULDC (replaced by LDCU).
- **New:** IADD.64 (single 64-bit add; sm_89 used an IADD3 carry pair) plus a distinct 2-input **IADD** alongside IADD3, UMEMSETS.64 (st.bulk), BRA.U (uniform-predicate branch), VOTEU.ANY, BAR.SYNC.DEFER_BLOCKING, MOVM.U4TO8.M832, CGAERRBAR, descriptor-based global addressing, and mixed-datapath forms (`I2F.F64 R, UR6` — vector opcode consuming a uniform-register source [probe: uniform_i2f]).
- **Accepted on sm_120 that sm_89 rejected:** `stmatrix`, `elect.sync`, `mapa` (trivial forms fold to S2UR/PRMT), `cp.async.bulk`/mbarrier, `griddepcontrol`.
- **Still rejected under `-arch=sm_120`:** sm_90a-only `wgmma`; sm_100a-family `tcgen05.*` (`.cta_group` not supported), `redux.sync.*.f32`, FP4 `cvt.rn.satfinite.e2m1x2`, and `setmaxnreg` — but **`setmaxnreg` is accepted under `-arch=sm_120a`** [probe: sass_probe corpus], i.e. the `a`-suffix feature gate applies to it on Blackwell consumer.
- **Unchanged:** the scheduling control-code layout (stall/yield/write-barrier 110-112/read-barrier 113-115/wait-mask 116-121 over the two 64-bit words) — the sm_89 layout hypothesis held on every probed opcode class [probe: RESULTS.md "Control-code scoreboard fields"; sass/INDEX.md "Control-code layout" -O0/-O3 diff].
- **Found by the tracer, not yet in the probe corpus:** `UI2F.U32.RP UR, imm` — ptxas materializes small-integer float constants (1.0, 16.0, 32.0, ...) on the uniform datapath as UI2F of the integer, feeding uniform MUFU.RCP (the 1/N normalizations in our kernels). Observed in 8 of the 16 traced compile.py outputs (e.g. [traces/f01_rmsnorm](../traces/baseline/f01_rmsnorm/README.md)); every standalone uniform-rcp probe stayed on the vector pipe, so the promotion heuristic needs the whole downstream chain to be uniform. The tracer's "not in KB corpus" flag on these pages is the KB-gap marker working as designed.

## Live decode pipeline

`tools/trace.py` turns this KB (and the sm89 KB) into a live decode pipeline for our own
compiler output: it runs any `compile.py` artifact through `ptxas -arch=sm_89` and
`ptxas -arch=sm_120`, decodes both with nvdisasm, maps every emitted opcode to its KB
page, and writes a per-input cross-ref plus an sm_89/sm_120 divergence summary to
`traces/`. See [traces/INDEX.md](../traces/INDEX.md) (16 inputs: all 15 problems + the
hand-written example; the sm_120 side gates on this KB's `sass/INDEX.md` existing).

## References

1. NVIDIA PTX ISA, version 8.8 — frozen archive: <https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html> (`ptx/` is generated from it).
2. NVIDIA CUDA Binary Utilities — opcode table, Blackwell and Rubin section: <https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html>.
3. NVIDIA CUDA C++ Programming Guide 12.9.1, Technical Specifications per Compute Capability: <https://docs.nvidia.com/cuda/archive/12.9.1/cuda-c-programming-guide/index.html#compute-capabilities>.
4. Mesa NAK (NVK compiler backend), `src/nouveau/compiler/nak/sm70_encode.rs` — mirror commit `837ab0e30740` of <https://github.com/chaotic-cx/mesa-mirror> (same-day mirror of mesa.git; gitlab.freedesktop.org raw fetches are bot-walled). NVK is Vulkan 1.4 conformant on Blackwell consumer since Mesa 25.3.

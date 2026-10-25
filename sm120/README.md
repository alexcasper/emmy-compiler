# sm120 knowledge base (Blackwell consumer, compute capability 12.0)

Reference for writing PTX that targets `sm_120` and reading the SASS that `ptxas` produces from it.
Every fact below carries a reference tag: **[n]** = a cited document (listed at the end), **[probe: x]** =
reproduced by compiling with NVIDIA's real `ptxas`/`nvdisasm` (see [verify/RESULTS.md](verify/RESULTS.md)).
Methodology is the same as the sibling [sm89 KB](../sm89/README.md); every sm_120 claim is derived from
sm_120 probes, not carried over from sm_89.

| path | what |
|---|---|
| [sass/INDEX.md](sass/INDEX.md) | **Start here for SASS.** The sm_120 opcode space found by probing, by category: NVIDIA's official description, which PTX/CUDA produces it, and probe evidence |
| `sass/<OP>.md` | Per-opcode observations: syntax forms seen in real ptxas output, observed 128-bit encodings, intersect-derived fixed bits (observation-derived, partial), and an Evidence section |
| [ptx/INDEX.md](ptx/INDEX.md) | **Start here for PTX.** Every PTX instruction with an sm_120 availability column derived from NVIDIA's "Target ISA Notes" (PTX ISA 8.8, CUDA 12.9.1) |
| `ptx/instructions/NN-<family>/` | PTX ISA chapter 9.7, one file per instruction section (NVIDIA text, converted) |
| `ptx/NN-*.md` | Other PTX ISA chapters (syntax, state spaces, memory model, special registers, directives...) |
| [verify/RESULTS.md](verify/RESULTS.md) | 136 PTX→SASS probes compiled for sm_120: claimed vs. emitted opcodes, the sm_89→sm_120 divergence table, control-code decoding, and PTX that sm_120 rejects |
| `tools/`, `verify/*.py` | Scripts that regenerate everything |

## Sources and how much to trust each part

| content | source | status |
|---|---|---|
| PTX chapters | NVIDIA PTX ISA manual 8.8, frozen CUDA 12.9.1 archive [1] | Verbatim NVIDIA text, converted by pandoc. The sm_120 column is a heuristic over NVIDIA's notes. Family-gated features (sm_90a `wgmma`/`setmaxnreg`, sm_100a `tcgen05`/`redux.f32`/FP4 `cvt`) were probe-checked: `ptxas -arch=sm_120` rejects each for architecture reasons [probe: no_*] |
| SASS opcodes + encodings | Our own probes only | There is **no kuterdinel-style encoding site for sm_120** (and no independent SASS encoding reference for Blackwell consumer at the time of writing). `sass/*.md` therefore document observed ptxas output: syntax forms, example 128-bit encodings, and fixed bits derived by intersecting every observed encoding of the opcode. These are observations, not a complete encoding spec [probe: sass/*] |
| SASS descriptions | NVIDIA CUDA Binary Utilities opcode table, Blackwell/Rubin section [2] | Official NVIDIA one-liners, merged into `sass/*.md` |
| "Typically emitted for" | Ours (`tools/sass_catalog.py`) | Each opcode page says whether a probe reproduced the claim |

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

- **Renamed:** IMNMX → **VIMNMX**; RED → **REDG** (with explicit memory-order/scope qualifiers like `.STRONG.GPU`); STM → **STSM.16** (stmatrix).
- **Removed:** HADD2/HMUL2 (folded into HFMA2), BMMA (b1 `mma.sync` CALLs an internal sm_10x routine built from IMMA.16832 + new MOVM.U4TO8), VABSDIFF4 (emulated via VIMNMX.U8x4 + VIADD.U8x4 + IDP.4A), ULDC (replaced by LDCU).
- **New:** IADD.64 (single 64-bit add; sm_89 used an IADD3 carry pair), UMEMSETS.64 (st.bulk), BRA.U (uniform-predicate branch), VOTEU.ANY, BAR.SYNC.DEFER_BLOCKING, MOVM.U4TO8.M832, descriptor-based global addressing.
- **Accepted on sm_120 that sm_89 rejected:** `stmatrix`, `elect.sync`, `mapa` (trivial forms fold to S2UR/PRMT), `cp.async.bulk`/mbarrier, `griddepcontrol`.
- **Still rejected on sm_120:** sm_90a-only `wgmma`/`setmaxnreg`; sm_100a-family `tcgen05.*` (`.cta_group` not supported), `redux.sync.*.f32`, FP4 `cvt.rn.satfinite.e2m1x2`.
- **Unchanged:** the scheduling control-code layout (stall/yield/write-barrier 110-112/read-barrier 113-115/wait-mask 116-121 over the two 64-bit words) — the sm_89 layout hypothesis held on every probed opcode class [probe: RESULTS.md "Control-code scoreboard fields"].

## References

1. NVIDIA PTX ISA, version 8.8 — frozen archive: <https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html> (`ptx/` is generated from it).
2. NVIDIA CUDA Binary Utilities — opcode table, Blackwell and Rubin section: <https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html>.
3. NVIDIA CUDA C++ Programming Guide 12.9.1, Technical Specifications per Compute Capability: <https://docs.nvidia.com/cuda/archive/12.9.1/cuda-c-programming-guide/index.html#compute-capabilities>.

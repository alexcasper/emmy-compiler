# sm89 knowledge base (Ada Lovelace, compute capability 8.9)

Reference for writing PTX that targets `sm_89` and reading the SASS that `ptxas` produces from it.
Every fact below carries a reference tag: **[n]** = a cited document (listed at the end), **[probe: x]** =
reproduced by compiling with NVIDIA's real `ptxas`/`nvdisasm` (see [verify/RESULTS.md](verify/RESULTS.md)).

| path | what |
|---|---|
| [sass/INDEX.md](sass/INDEX.md) | **Start here for SASS.** All 151 SM89 opcodes by category: NVIDIA's official description, which PTX/CUDA produces it, and the evidence for that claim |
| `sass/<OP>.md` | Per-opcode encodings (every operand-form variant, bit-field map, fixed opcode bits, modifier tables) plus an Evidence section |
| [ptx/INDEX.md](ptx/INDEX.md) | **Start here for PTX.** Every PTX instruction with an sm_89 availability column derived from NVIDIA's "Target ISA Notes" |
| `ptx/instructions/NN-<family>/` | PTX ISA chapter 9.7, one file per instruction section (NVIDIA text, converted) |
| `ptx/NN-*.md` | Other PTX ISA chapters (syntax, state spaces, memory model, special registers, directives...) |
| [verify/RESULTS.md](verify/RESULTS.md) | 129 PTX→SASS probes compiled for sm_89: claimed vs. emitted opcodes, encoding checks, control-code decoding, and PTX that sm_89 must reject |
| [verify/NAK_CROSSCHECK.md](verify/NAK_CROSSCHECK.md) | Scraped opcode numbers cross-checked against Mesa's open-source NVK compiler [6] |
| `tools/`, `verify/*.py` | Scripts that regenerate everything |

## Sources and how much to trust each part

| content | source | status |
|---|---|---|
| PTX chapters | NVIDIA PTX ISA manual, version 9.4 [1] | Verbatim NVIDIA text, converted by pandoc. The sm_89 column is a heuristic over NVIDIA's notes. 8 sm_90+/sm_100+ features were checked, and `ptxas -arch=sm_89` rejects each one for architecture reasons [probe: no_*] |
| SASS encodings | kuterdinel.com SM89 pages [5], machine-derived by fuzzing the assembler | Every instruction in our probes (1713 of them) has a 12-bit opcode field matching a scraped variant. There are 2 exceptions, forms the site lacks: `FRND.FLOOR` and `IMAD.HI.U32`. For all 83 opcodes that NAK [6] also encodes, the opcode numbers are consistent (80 by name; 3 NAK ops cover several SASS mnemonics). Some bits the site marks "fixed" are really unlabelled modifiers (listed in RESULTS.md and on each opcode page) |
| SASS descriptions | NVIDIA CUDA Binary Utilities opcode table [2] | Official, for 139 of 151 opcodes. The other 12 (F2FP, QMMA, and graphics ops) are not in NVIDIA's Ampere/Ada table. QMMA does appear in NVIDIA's Blackwell table as "FP8 Matrix Multiply and Accumulate Across a Warp" [2] |
| "Typically emitted for" | Ours (`tools/sass_catalog.py`) | 110 opcodes reproduced by ptxas probes. Each opcode page says whether its claim was verified, only seen in passing, or not reproduced |

Regenerate with `python3 sm89/tools/build_ptx.py && python3 sm89/verify/crosscheck_nak.py && PTXAS=... NVDISASM=... python3 sm89/verify/probes.py && python3 sm89/tools/build_sass.py` (needs `pandoc`). The probe tools come from NVIDIA's PyPI wheels and need no GPU: `nvidia-cuda-nvcc-cu12` (ptxas 12.9) and `nvidia-cuda-nvdisasm` (13.4); see `verify/probes.py`. Downloads are cached in `sm89/.cache/` (gitignored).

## sm_89 at a glance

- **SM:** 4 processing blocks (partitions), each with its own warp scheduler. A block has 16 FP32-only lanes plus 16 lanes that do either FP32 or INT32, giving 128 FP32 lanes per SM [4]. FP64 runs at 1/64 of the FP32 rate, with 2 FP64 units per SM [4].
- **Occupancy limits (CC 8.9):** 64K 32-bit registers per SM, at most 255 per thread; at most 24 resident blocks, 48 warps and 1536 threads per SM [3 Tables 30-31; 7].
- **Shared memory / L1:** 128 KB unified L1/texture/shared per SM. The shared-memory carveout can be 0, 8, 16, 32, 64 or 100 KB. A block can use at most 99 KB, because CUDA reserves 1 KB per block, and anything above 48 KB must be dynamic and opt-in. There are 32 banks [3 Tables 31-32; 7].
- **L2:** 98304 KB (96 MB) on full AD102 and L40, 73728 KB (72 MB) on RTX 4090, and 49152 KB (48 MB) on L4 [4 Appendices A, C, D; 7].
- **Tensor cores (4th gen):** input types TF32, BF16, FP16, FP8, INT8 and INT4. There is no FP64 tensor-core rate on 8.9 [3 Table 33]. FP8 `mma` (`.e4m3`/`.e5m2`) requires `sm_89` and PTX ISA **8.4** [1 §9.7.16.5.14]. On sm_89 it compiles to **QMMA** [probe: qmma_e4m3]. f16/bf16/tf32 compile to HMMA, s8 to IMMA, b1 to BMMA, and f64 `m8n8k4` to DMMA [probe: hmma_f16, hmma_tf32, imma, bmma, dmma]. DMMA does run on sm_89, but CC 8.9 has no FP64 tensor-core *acceleration* [3 Table 33].
- **FP8 conversions:** `cvt` with `.e4m3x2`/`.e5m2x2` on sm_89 needs PTX ISA **8.1** [1 §9.7.10.24]. It compiles to `F2FP.SATFINITE.E4M3.F32.PACK_AB_MERGE_C` [probe: f2fp_e4m3].
- **Available:** `cp.async` → LDGSTS, LDGDEPBAR, DEPBAR [probe: cp_async]; `ldmatrix` → LDSM [probe: ldsm]; `movmatrix` → MOVM [probe: movm]; `redux.sync` → REDUX [probe: redux]; `match.any` → MATCH [probe: match].
- **Not available (ptxas rejects them for sm_89):** `stmatrix`, `elect.sync`, `setmaxnreg`, `mapa`/clusters, `cp.async.bulk` (TMA), `wgmma`, `griddepcontrol`, and `redux.sync` on f32 [probe: no_*]. The PTX index marks these and the other sm_90+ features as `no` [1].
- **PTX header:** `.target sm_89` requires PTX ISA ≥ 7.8 [1 §11 "Target string sm_89 introduced in PTX ISA version 7.8"]. This repo uses `.version 8.0`, so FP8 `cvt` would need 8.1 and FP8 `mma` 8.4.
- **Kernel parameters:** these live in constant bank 0 starting at `c[0x0][0x160]` (first `.u64` param = `c[0x0][0x160..0x164]`) [probe: every probe's prologue]. Every kernel also starts with `MOV R1, c[0x0][0x28]` and `ULDC.64 UR4, c[0x0][0x118]` [probe: prologue]. This is observed compiler behaviour, not a documented ABI (R1 is conventionally the stack pointer).

## Reading SASS encodings

Each instruction is 128 bits. In `sass/*.md`, bit 0 is the LSB of the first 64-bit word, which is how nvdisasm `-hex` prints it [probe]. The 12-bit opcode is in bits 0-11: FFMA with register operands is `0x223`, and with a constant-bank operand `0xa23` [probe: ffma; 6].

The top 21 used bits (105-125; bits 126-127 were 0 in all 3208 probe instructions) are the scheduling **control code**, which ptxas sets. Jia et al. [8 §2.1] give the field order MSB→LSB as reuse(4), wait mask(6), read barrier(3), write barrier(3), yield(1), stall(4). Counting up from bit 105, and confirmed on real sm_89 encodings [probe]:

| bits | field | meaning |
|---|---|---|
| 105-108 | stall | cycles (0-15) before the warp may issue its next instruction [8 §2.1] |
| 109 | yield | scheduler yield hint [8 §2.1] |
| 110-112 | **write (result) scoreboard** | set by variable-latency instructions whose *result* arrives late: every LDG (195/195), LDS, MUFU, S2R, conversions, SHFL... [probe: RESULTS.md "Control-code scoreboard fields"; 8 §2.1] |
| 113-115 | **read scoreboard** | protects write-after-read: set by instructions that read their *source registers* late (STG, ATOMS); in our probes LDG sets it only when a `MEMBAR` follows [probe: membar, fence_sys; 8 §2.1] |
| 116-121 | wait mask | scoreboards that must clear before issue; e.g. an FFMA consuming an LDG result waits on bit 2 = the LDG's index [probe: ffma] |
| 122-125 | reuse | operand reuse-cache flags; LSB = first source operand [8 §2.1] |

The kuterdinel pages label 110-112 "r-bar" and 113-115 "w-bar". Real encodings show the opposite, matching Jia et al. [8]. The generated `sass/*.md` tables use the corrected names.

Practical notes:
- ptxas freely alternates `MOV`, `IMAD.MOV.U32` and `IMAD.IADD` for plain moves and adds to balance execution pipes [probe: prologue, imnmx_from_selp, many listings].
- ptxas rewrites patterns, so don't expect 1:1 lowering. `setp`+`selp` forming a min becomes IMNMX [probe: imnmx_from_selp]. `selp` between two loads becomes a predicated load [probe: selp_to_predicated_load]. `set.f32` becomes FSETP + SEL [probe: fset]. Predicate logic folds into ISETP/FSETP [probe: plop3_folded]. PTX `vabsdiff`/`vabsdiff2` are emulated rather than lowered to VABSDIFF [probe: vabsdiff, vabsdiff2]. Atomics and reductions to a warp-uniform address get warp-aggregated: VOTEU + FLO/UFLO + POPC + one ATOMG/RED [probe: agg_atomic, agg_red].
- `U*` opcodes run on the uniform datapath: one value per warp, in registers `UR*` and predicates `UP*` [2]. ptxas moves warp-invariant math there, for example loops bounded by `%ctaid` or kernel parameters [probe: s2ur_loop, uniform_alu].
- `BSSY`/`BSYNC` pairs bracket divergent regions that must reconverge before a warp-synchronous instruction [2; probe: bssy_bsync].
- A full-precision `div.rn.f32` compiles to MUFU.RCP + FFMA refinement + an FCHK range check, with a CALL to a slow path [probe: fdiv_rn].

## References

1. NVIDIA, *Parallel Thread Execution ISA*, version 9.4. <https://docs.nvidia.com/cuda/parallel-thread-execution/index.html> (converted into `ptx/`).
2. NVIDIA, *CUDA Binary Utilities*, §4.2 "NVIDIA Ampere GPU and Ada Instruction Set" (Table 7) and §4.4 Blackwell table. <https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set>
3. NVIDIA, *CUDA Programming Guide*, §5.1 "Compute Capabilities", Tables 29-33. <https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/compute-capabilities.html>
4. NVIDIA, *NVIDIA Ada GPU Architecture* whitepaper (Ada SM section; Appendices A, C, D spec tables). <https://images.nvidia.com/aem-dam/Solutions/geforce/ada/nvidia-ada-gpu-architecture.pdf>
5. Kuter Dinel, *Nvidia SM89 Instruction Set Architecture* (fuzzed encodings). <https://kuterdinel.com/nv_isa_sm89/>
6. Mesa NAK (NVK compiler) `src/nouveau/compiler/nak/sm70_encode.rs`, commit `e7371b0711bb`. <https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs>
7. NVIDIA, *Ada Tuning Guide*, §1.4 (occupancy, L1/shared memory, L2). <https://docs.nvidia.com/cuda/ada-tuning-guide/index.html>
8. Z. Jia, M. Maggioni, J. Smith, D. P. Scarpazza, *Dissecting the NVidia Turing T4 GPU via Microbenchmarking*, arXiv:1903.07486 (2019), §2.1 "Control information" (layout shared by Volta/Turing and, per our probes, Ada); and *Dissecting the NVIDIA Volta GPU Architecture via Microbenchmarking*, arXiv:1804.06826 (2018). <https://arxiv.org/abs/1903.07486>, <https://arxiv.org/abs/1804.06826>

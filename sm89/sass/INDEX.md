# SM89 SASS instruction index

151 opcodes scraped from <https://kuterdinel.com/nv_isa_sm89/>. Columns:

- **NVIDIA description**: verbatim from NVIDIA's [Ampere/Ada opcode table](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set). 139/151 opcodes are listed there; the rest are marked *not in NVIDIA table*.
- **typically emitted for**: our summary of which PTX/CUDA produces it (`tools/sass_catalog.py`).
- **evidence**: ✓ = a probe compiled with real `ptxas -arch=sm_89` produced this opcode from the linked PTX (110 opcodes); "seen in" = emitted incidentally; "not reproduced" = claim unverified. Details in [../verify/RESULTS.md](../verify/RESULTS.md). **NAK** = the opcode number on the source page matches Mesa's open-source NVK compiler (83 opcodes, [../verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md)).

## Atomics / reductions

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [ATOM](ATOM.md) | Atomic Operation on Generic Memory | `atom` on generic pointers | ✓ [`atom.add.u32`](../verify/RESULTS.md#atom_generic) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3777) | 14 |
| [ATOMS](ATOMS.md) | Atomic Operation on Shared Memory | `atom.shared.*` | ✓ [`atom.shared.add.u32`](../verify/RESULTS.md#atoms) | 10 |
| [RED](RED.md) | Reduction Operation on Generic Memory | `red.global.*`; `atomicAdd` whose result is unused | ✓ [`red.global.add.u32`](../verify/RESULTS.md#red), [`red.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_red) | 7 |
| [ATOMG](ATOMG.md) | Atomic Operation on Global Memory | `atom.global.*` (`atomicAdd`, `atomicCAS`, ... with return) | ✓ [`atom.global.add.u32`](../verify/RESULTS.md#atomg), [`atom.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_atomic) | 14 |
| [REDUX](REDUX.md) | Reduction of a Vector Register into a Uniform Register | `redux.sync.add/min/max/and/or/xor.u32/s32`; `__reduce_add_sync` | ✓ [`redux.sync.add.u32`](../verify/RESULTS.md#redux) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2705) | 1 |

## Control flow

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [NOP](NOP.md) | No Operation | padding/alignment (compiler-generated) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4371) | 2 |
| [BSYNC](BSYNC.md) | Synchronize Threads on a Convergence Barrier | reconvergence point after divergent region | ✓ [`divergent loop exit followed by a warp-synchronous op`](../verify/RESULTS.md#bssy_bsync) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4179) | 2 |
| [BREAK](BREAK.md) | Break out of the Specified Convergence Barrier | divergent `break` out of loop | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4152) | 2 |
| [CALL](CALL.md) | Call Function | `call` (non-inlined device functions, printf, slow-path div/sqrt) | ✓ [`div.rn.f32`](../verify/RESULTS.md#fdiv_rn), [`.func .noinline call`](../verify/RESULTS.md#call) | 16 |
| [BSSY](BSSY.md) | Barrier Set Convergence Synchronization Point | start of a divergent region (compiler-inserted for if/else, loops with divergent exits) | ✓ [`divergent loop exit followed by a warp-synchronous op`](../verify/RESULTS.md#bssy_bsync) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4165) | 2 |
| [YIELD](YIELD.md) | Yield Control | compiler-inserted in spin loops for forward progress | not reproduced | 2 |
| [BRA](BRA.md) | Relative Branch | `bra`; loops, if/else | ✓ [`data-dependent loop`](../verify/RESULTS.md#diverge) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4191) | 4 |
| [WARPSYNC](WARPSYNC.md) | Synchronize Threads in Warp | `bar.warp.sync`; `__syncwarp`; implicit in `*.sync` ops with non-full masks | ✓ [`bar.warp.sync with partial mask`](../verify/RESULTS.md#warpsync) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4234) | 8 |
| [BRX](BRX.md) | Relative Branch Indirect | `brx.idx`; switch jump tables | ✓ [`brx.idx`](../verify/RESULTS.md#brx) | 4 |
| [JMP](JMP.md) | Absolute Jump | absolute jumps (rare) | not reproduced | 8 |
| [JMX](JMX.md) | Absolute Jump Indirect | absolute indirect jumps (rare) | not reproduced | 4 |
| [EXIT](EXIT.md) | Exit Program | `exit` / `ret` from the kernel; early `return` | ✓ [`empty kernel body: param pointer + %tid.x load/store`](../verify/RESULTS.md#prologue) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4218) | 2 |
| [RET](RET.md) | Return From Subroutine | `ret` from a device function | ✓ [`.func .noinline call`](../verify/RESULTS.md#call) | 4 |
| [BRXU](BRXU.md) | Relative Branch with Uniform Register Based Offset | jump table with uniform index | not reproduced | 4 |
| [JMXU](JMXU.md) | Absolute Jump with Uniform Register Based Offset | uniform absolute indirect jump | not reproduced | 4 |
| [NANOSLEEP](NANOSLEEP.md) | Suspend Execution | `nanosleep.u32`; `__nanosleep` | ✓ [`nanosleep.u32`](../verify/RESULTS.md#nanosleep) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4679) | 10 |

## Conversion

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [F2FP](F2FP.md) | *not in NVIDIA tables*: Pack two FP32 into FP16x2 / BF16x2 (and FP8 pairs on sm_89) | `cvt.rn.f16x2.f32`, `cvt.rn.bf16x2.f32`, `cvt.rn.satfinite.e4m3x2/e5m2x2.f32` (FP8, sm_89); `__floats2half2_rn` | ✓ [`cvt.rn.f16x2.f32`](../verify/RESULTS.md#f2fp_f16), [`cvt.rn.bf16x2.f32`](../verify/RESULTS.md#f2fp_bf16) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2237) | 22 |
| [F2IP](F2IP.md) | FP32 Down-Convert to Integer and Pack | per NVIDIA: FP32 down-convert to integer and pack; no PTX source found (`cvt.rni.sat.s8.f32` gives F2I) | not reproduced | 9 |
| [I2I](I2I.md) | Integer To Integer Conversion | `cvt.sat.s8.s32` etc. (saturating narrow) | ✓ [`cvt.sat.s8.s32`](../verify/RESULTS.md#i2i) | 5 |
| [I2IP](I2IP.md) | Integer To Integer Conversion and Packing | `cvt.pack.sat.s8.s32.b32` | ✓ [`cvt.pack.sat.s8.s32.b32`](../verify/RESULTS.md#i2ip) | 5 |
| [I2FP](I2FP.md) | Integer to FP32 Convert and Pack | `cvt.rn.f32.s32/u32` (fast 32-bit form) | ✓ [`cvt.rn.f32.s32`](../verify/RESULTS.md#i2fp) | 5 |
| [F2I](F2I.md) | Floating Point To Integer Conversion | `cvt.rzi.s32.f32` etc.; `(int)f`, `__float2int_rn` | ✓ [`cvt.rzi.s32.f32`](../verify/RESULTS.md#f2i) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2282) | 9 |
| [I2F](I2F.md) | Integer To Floating Point Conversion | `cvt.rn.f32.s32` etc. (64-bit / FP64 forms) | ✓ [`cvt.rn.f64.s32`](../verify/RESULTS.md#i2f) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2329) | 10 |
| [F2F](F2F.md) | Floating Point To Floating Point Conversion | `cvt.f32.f64`, `cvt.f64.f32`, `cvt.rn.f16.f32` (single value) | ✓ [`cvt.rn.f32.f64`](../verify/RESULTS.md#f2f) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2189) | 5 |

## FP16 (packed half2)

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [HADD2](HADD2.md) | FP16 Add | `add.f16x2`/`add.bf16x2`; `__hadd2`; also used as f16 mov/convert helper | ✓ [`add.f16x2`](../verify/RESULTS.md#hadd2) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1316) | 6 |
| [HFMA2](HFMA2.md) | FP16 Fused Mutiply Add | `fma.rn.f16x2`/`bf16x2`; `__hfma2` | ✓ [`fma.rn.f16x2`](../verify/RESULTS.md#hfma2), [`fma.rn.bf16x2`](../verify/RESULTS.md#hfma2_bf16) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1350) | 36 |
| [HSET2](HSET2.md) | FP16 Compare And Set | `set.<cmp>.f16x2` | ✓ [`set.lt.f16x2.f16x2`](../verify/RESULTS.md#hset2) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1403) | 5 |
| [HSETP2](HSETP2.md) | FP16 Compare And Set Predicate | `setp.<cmp>.f16x2`; half comparisons | ✓ [`setp.lt.f16x2`](../verify/RESULTS.md#hsetp2) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1445) | 5 |
| [HMUL2](HMUL2.md) | FP16 Multiply | `mul.f16x2`/`bf16x2`; `__hmul2` | ✓ [`mul.f16x2`](../verify/RESULTS.md#hmul2) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1377) | 5 |
| [HMNMX2](HMNMX2.md) | FP16 Minimum / Maximum | `min/max.f16x2`/`bf16x2`; `__hmin2`/`__hmax2` | ✓ [`min.f16x2`](../verify/RESULTS.md#hmnmx2) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1488) | 5 |

## FP32

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [FADD](FADD.md) | FP32 Add | `add.f32`, `sub.f32`; CUDA `a + b` on float | ✓ [`add.f32`](../verify/RESULTS.md#fadd) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L849) | 5 |
| [FFMA](FFMA.md) | FP32 Fused Multiply and Add | `fma.rn.f32`, `mad.f32`; contracted `a*b+c` (default -fmad=true) | ✓ [`fma.rn.f32`](../verify/RESULTS.md#ffma), [`div.rn.f32`](../verify/RESULTS.md#fdiv_rn) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L890) | 9 |
| [FSEL](FSEL.md) | Floating Point Select | `selp.f32` / float ternary `c ? a : b` | ✓ [`setp.lt.f32 + selp.f32`](../verify/RESULTS.md#fsetp_selp) | 5 |
| [FMNMX](FMNMX.md) | FP32 Minimum/Maximum | `min.f32` / `max.f32`; `fminf`/`fmaxf` | ✓ [`min.f32 / max.f32`](../verify/RESULTS.md#fminmax) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L925) | 5 |
| [FSET](FSET.md) | FP32 Compare And Set | `set.<cmp>.f32` in principle, but on sm_89 ptxas lowers `set.lt.u32.f32` to FSETP + SEL (probe `fset`); FSET itself was not reproduced | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1052) | 5 |
| [FSETP](FSETP.md) | FP32 Compare And Set Predicate | `setp.<cmp>.f32`; float comparisons in `if` | ✓ [`setp.lt.f32 + selp.f32`](../verify/RESULTS.md#fsetp_selp), [`selp.f32 between two loaded values`](../verify/RESULTS.md#selp_to_predicated_load) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1089) | 5 |
| [FMUL](FMUL.md) | FP32 Multiply | `mul.f32` | ✓ [`mul.f32`](../verify/RESULTS.md#fmul) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L963) | 5 |
| [FSWZADD](FSWZADD.md) | FP32 Swizzle Add | fragment-shader derivatives (ddx/ddy); no PTX equivalent; Mesa NAK emits it (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1132) | 1 |
| [FCHK](FCHK.md) | Floating-point Range Check | `div.rn.f32` full-precision division (guards the slow path) | ✓ [`div.rn.f32`](../verify/RESULTS.md#fdiv_rn) | 5 |
| [MUFU](MUFU.md) | FP32 Multi Function Operation | `rcp.approx`, `rsqrt.approx`, `sqrt.approx`, `lg2.approx`, `ex2.approx`, `sin/cos.approx`, `tanh.approx`; `__expf`, `__logf`, `__fdividef`; also inside full-precision div/sqrt sequences | ✓ [`div.rn.f32`](../verify/RESULTS.md#fdiv_rn), [`rcp.approx.f32`](../verify/RESULTS.md#mufu_rcp) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1168) | 5 |
| [FRND](FRND.md) | Round To Integer | `cvt.rni/rzi/rmi/rpi.f32.f32`; `rintf`, `truncf`, `floorf`, `ceilf` | ✓ [`cvt.rmi.f32.f32`](../verify/RESULTS.md#frnd) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2371) | 5 |

## FP64

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [DADD](DADD.md) | FP64 Add | `add.f64` | ✓ [`add.f64`](../verify/RESULTS.md#dadd) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1215) | 5 |
| [DSETP](DSETP.md) | FP64 Compare And Set Predicate | `setp.<cmp>.f64` | ✓ [`setp.lt.f64`](../verify/RESULTS.md#dsetp) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1276) | 5 |
| [DFMA](DFMA.md) | FP64 Fused Mutiply Add | `fma.rn.f64` | ✓ [`fma.rn.f64`](../verify/RESULTS.md#dfma) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1235) | 9 |
| [DMUL](DMUL.md) | FP64 Multiply | `mul.f64` | ✓ [`mul.f64`](../verify/RESULTS.md#dmul) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1256) | 5 |

## Graphics-only

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [ALD](ALD.md) | *not in NVIDIA tables*: Attribute load | graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3932) | 12 |
| [IPA](IPA.md) | *not in NVIDIA tables*: Interpolate attribute | graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3974) | 20 |
| [AL2P](AL2P.md) | *not in NVIDIA tables*: Attribute logical to physical address | graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3915) | 2 |
| [ISBERD](ISBERD.md) | *not in NVIDIA tables*: Internal stage buffer entry read | graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4286) | 3 |
| [OUT](OUT.md) | *not in NVIDIA tables*: Geometry shader output | graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4421) | 6 |
| [PIXLD](PIXLD.md) | *not in NVIDIA tables*: Pixel info load | graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4381) | 2 |
| [LDTRAM](LDTRAM.md) | *not in NVIDIA tables*: Unknown; not in NVIDIA's table (name suggests attribute-RAM load) | graphics shaders only (no PTX equivalent); Mesa NAK emits it for Vulkan shaders (see Evidence) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4015) | 3 |

## Integer

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [LEA](LEA.md) | LOAD Effective Address | address arithmetic `base + (idx << k)`; array indexing `p[i]` | ✓ [`shl.b32 + add.s32`](../verify/RESULTS.md#lea), [`pointer +`](../verify/RESULTS.md#lea64) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1923) | 44 |
| [VABSDIFF](VABSDIFF.md) | Absolute Difference | not emitted for PTX `vabsdiff`/`vabsdiff2` on sm_89: ptxas emulates those with PRMT/IADD3/IABS (probes `vabsdiff`, `vabsdiff2`) | not reproduced | 18 |
| [VABSDIFF4](VABSDIFF4.md) | Absolute Difference | `vabsdiff4` (verified) | ✓ [`vabsdiff4.u32.u32.u32.add`](../verify/RESULTS.md#vabsdiff4) | 18 |
| [PRMT](PRMT.md) | Permute Register Pair | `prmt.b32`; `__byte_perm`; byte extraction / packing (e.g. `cvt.u8`, `mov.b32 {a,b}`) | ✓ [`prmt.b32`](../verify/RESULTS.md#prmt) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2448) | 9 |
| [SHF](SHF.md) | Funnel Shift | `shl/shr` on 32/64-bit, `shf.l/r`; `__funnelshift_l/r` | ✓ [`shf.l.wrap.b32`](../verify/RESULTS.md#shf), [`shl.b64 by register`](../verify/RESULTS.md#shl64) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2141) | 9 |
| [IMAD](IMAD.md) | Integer Multiply And Add | `mul.lo`, `mad.lo`, `mul.wide` (IMAD.WIDE), `mul.hi` (IMAD.HI); also `IMAD.MOV.U32` / `IMAD.IADD` as moves/adds that ptxas balances against MOV/IADD3 | ✓ [`mad.lo.s32`](../verify/RESULTS.md#imad), [`mul.wide.s32`](../verify/RESULTS.md#imad_wide) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1751) | 82 |
| [ISETP](ISETP.md) | Integer Compare And Set Predicate | `setp.<cmp>.s32/u32/s64`; integer comparisons, loop bounds | ✓ [`setp.lt.s32 + selp.b32`](../verify/RESULTS.md#isetp_pred), [`xor.pred of two compares`](../verify/RESULTS.md#plop3_folded) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1866) | 10 |
| [IADD3](IADD3.md) | 3-input Integer Addition | `add/sub.s32/u32`, `add.cc`/`addc` chains, 64-bit `add.s64` (pair of IADD3 with carry) | ✓ [`add.s32 / sub.s32`](../verify/RESULTS.md#iadd), [`add.s64`](../verify/RESULTS.md#iadd64) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1595) | 30 |
| [LOP3](LOP3.md) | Logic Operation | `and/or/xor/not`, `lop3.b32`; any bitwise expression of up to 3 inputs | ✓ [`and/xor/or of 3 values`](../verify/RESULTS.md#lop3) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2064) | 10 |
| [IABS](IABS.md) | Integer Absolute Value | `abs.s32` | ✓ [`abs.s32`](../verify/RESULTS.md#iabs) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1580) | 5 |
| [IMNMX](IMNMX.md) | Integer Minimum/Maximum | `min/max.s32/u32` | ✓ [`min.s32`](../verify/RESULTS.md#imnmx), [`setp.lt.s32 + selp.b32 forming min()`](../verify/RESULTS.md#imnmx_from_selp) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1815) | 5 |
| [SGXT](SGXT.md) | Sign Extend | `bfe.s32` / sign-extending narrow types (`cvt.s32.s8`) | ✓ [`bfe.s32`](../verify/RESULTS.md#sgxt) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2529) | 5 |
| [BMSK](BMSK.md) | Bitfield Mask | `bmsk.b32`; mask building in `bfi`/`bfe` lowering | ✓ [`bmsk.clamp.b32`](../verify/RESULTS.md#bmsk) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1518) | 5 |
| [FLO](FLO.md) | Find Leading One | `bfind`, `clz` (`__clz`) | ✓ [`bfind.u32 / clz.b32`](../verify/RESULTS.md#flo), [`atom.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_atomic) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1561) | 10 |
| [BREV](BREV.md) | Bit Reverse | `brev.b32` (`__brev`) | ✓ [`brev.b32`](../verify/RESULTS.md#brev) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L1547) | 5 |
| [POPC](POPC.md) | Population count | `popc.b32` (`__popc`) | ✓ [`popc.b32`](../verify/RESULTS.md#popc), [`atom.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_atomic) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2124) | 5 |
| [IDP](IDP.md) | Integer Dot Product and Accumulate | `dp4a`, `dp2a` (`__dp4a`) | ✓ [`dp4a.s32.s32`](../verify/RESULTS.md#idp) | 4 |

## Load / store

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [LDC](LDC.md) | Load Constant | `ld.const`, `ld.param` (kernel params live in constant bank 0), `__constant__` | ✓ [`ld.const with dynamic index`](../verify/RESULTS.md#ldc) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3505) | 6 |
| [LDSM](LDSM.md) | Load Matrix from Shared Memory with Element Size Expansion | `ldmatrix.sync.aligned.m8n8.x1/x2/x4[.trans].b16` | ✓ [`ldmatrix.sync.aligned.m8n8.x4.shared.b16`](../verify/RESULTS.md#ldsm) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4622) | 7 |
| [LDG](LDG.md) | Load from Global Memory | `ld.global[.nc/.ca/.cg/.cs/.lu]` (`__ldg`, plain global loads; vectorized .v2/.v4 -> LDG.E.64/.128) | ✓ [`ld.global.nc.v4.f32`](../verify/RESULTS.md#ldg_nc), [`empty kernel body: param pointer + %tid.x load/store`](../verify/RESULTS.md#prologue) | 56 |
| [LD](LD.md) | Load from generic Memory | `ld` on a generic pointer (space not provable) | ✓ [`ld`](../verify/RESULTS.md#ld_generic) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3428) | 18 |
| [LDL](LDL.md) | Load within Local Memory Window | `ld.local`; register spills, local arrays with dynamic indexing | ✓ [`dynamically indexed .local array`](../verify/RESULTS.md#ldl_stl) | 9 |
| [LDS](LDS.md) | Load within Shared Memory Window | `ld.shared` | ✓ [`ld.shared / st.shared`](../verify/RESULTS.md#lds_sts) | 7 |
| [ST](ST.md) | Store to Generic Memory | `st` on a generic pointer | ✓ [`st`](../verify/RESULTS.md#st_generic) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3625) | 11 |
| [STG](STG.md) | Store to Global Memory | `st.global` (vector forms -> STG.E.64/.128) | ✓ [`empty kernel body: param pointer + %tid.x load/store`](../verify/RESULTS.md#prologue) | 11 |
| [STL](STL.md) | Store to Local Memory | `st.local`; register spills | ✓ [`dynamically indexed .local array`](../verify/RESULTS.md#ldl_stl) | 11 |
| [CCTL](CCTL.md) | Cache Control | `prefetch.global.L1/L2`, `discard`, `applypriority` | ✓ [`prefetch.global.L1`](../verify/RESULTS.md#cctl) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4033) | 6 |
| [CCTLL](CCTLL.md) | Cache Control | `prefetch.local` | ✓ [`prefetch.local.L1`](../verify/RESULTS.md#cctll) | 4 |
| [QSPC](QSPC.md) | Query Space | `isspacep.global/shared/local` | ✓ [`isspacep.shared`](../verify/RESULTS.md#qspc) | 7 |
| [LDGDEPBAR](LDGDEPBAR.md) | Global Load Dependency Barrier | `cp.async.commit_group` | ✓ [`cp.async.cg.shared.global + commit_group + wait_group`](../verify/RESULTS.md#cp_async) | 1 |
| [LDGSTS](LDGSTS.md) | Asynchronous Global to Shared Memcopy | `cp.async.ca/cg.shared.global` (`__pipeline_memcpy_async`, `cuda::memcpy_async`) | ✓ [`cp.async.cg.shared.global + commit_group + wait_group`](../verify/RESULTS.md#cp_async) | 32 |
| [STS](STS.md) | Store to Shared Memory | `st.shared` | ✓ [`ld.shared / st.shared`](../verify/RESULTS.md#lds_sts) | 3 |
| [GETLMEMBASE](GETLMEMBASE.md) | Get Local Memory Base Address | local-memory window base (compiler-generated) | not reproduced | 1 |

## Miscellaneous

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [PMTRIG](PMTRIG.md) | Performance Monitor Trigger | `pmevent` (profiler trigger) | ✓ [`pmevent`](../verify/RESULTS.md#pmtrig) | 2 |

## Movement

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [SHFL](SHFL.md) | Warp Wide Register Shuffle | `shfl.sync.idx/up/down/bfly`; `__shfl_sync`, `__shfl_xor_sync` | ✓ [`shfl.sync.bfly.b32`](../verify/RESULTS.md#shfl), [`atom.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_atomic) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2558) | 4 |
| [MOV](MOV.md) | Move | `mov`; register copies, immediates, `ld.param` of kernel args in some cases | ✓ [`empty kernel body: param pointer + %tid.x load/store`](../verify/RESULTS.md#prologue) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2417) | 10 |
| [P2R](P2R.md) | Move Predicate Register To Register | spilling/packing predicates (compiler-generated) | not reproduced | 5 |
| [R2P](R2P.md) | Move Register To Predicate Register | restoring predicates (compiler-generated) | not reproduced | 6 |
| [CS2R](CS2R.md) | Move Special Register to Register | `mov.u32 %clock` / `%clock64`; also `CS2R R, SRZ` = zero a 64-bit pair | ✓ [`mov.u64 %clock64`](../verify/RESULTS.md#cs2r) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4273) | 1 |
| [SEL](SEL.md) | Select Source with Predicate | `selp.b32`; integer ternary | ✓ [`set.lt.u32.f32`](../verify/RESULTS.md#fset) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2491) | 5 |
| [S2R](S2R.md) | Move Special Register to Register | `mov.u32 %tid.x`, `%ctaid`, `%laneid`, `%lanemask_*`, `%smid` ... | ✓ [`mov.u32 %laneid`](../verify/RESULTS.md#s2r), [`mov.u32 %ctaid.x stored directly`](../verify/RESULTS.md#s2r_ctaid) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4404) | 1 |
| [RPCMOV](RPCMOV.md) | PC Register Move | return-address save/restore (compiler-generated) | not reproduced | 10 |
| [BMOV](BMOV.md) | Move Convergence Barrier State | convergence barrier save/restore (compiler-generated, deep divergence/recursion) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4128) | 16 |
| [S2UR](S2UR.md) | Move Special Register to Uniform Register | special register read whose value is warp-uniform and used on the uniform datapath (e.g. `%ctaid.x` as a loop bound); a plain `%ctaid.x` store still uses S2R | ✓ [`%ctaid.x as a loop bound`](../verify/RESULTS.md#s2ur_loop) | 1 |
| [MOVM](MOVM.md) | Move Matrix with Transposition or Expansion | `movmatrix.sync.aligned.m8n8.trans.b16` | ✓ [`movmatrix.sync.aligned.m8n8.trans.b16`](../verify/RESULTS.md#movm) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4663) | 1 |
| [B2R](B2R.md) | Move Barrier To Register | barrier result read (e.g. `bar.red.popc` result) | ✓ [`bar.red.popc.u32`](../verify/RESULTS.md#bar_red) | 3 |
| [LEPC](LEPC.md) | Load Effective PC | taking a code address (indirect calls, `%pc`-relative) | not reproduced | 1 |
| [R2UR](R2UR.md) | Move from Vector Register to a Uniform Register | compiler moving warp-uniform values into uniform datapath | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2688) | 2 |

## Predicate / compare

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [VOTE](VOTE.md) | Vote Across SIMD Thread Group | `vote.sync.all/any/uni/ballot`; `__all_sync`, `__ballot_sync`; `activemask` | ✓ [`vote.sync.ballot.b32`](../verify/RESULTS.md#vote) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4465) | 1 |
| [CSMTEST](CSMTEST.md) | *not in NVIDIA tables*: Unknown; not in NVIDIA's table (name suggests a CSM/state test) | (unknown; not produced by normal compute code) | not reproduced | 1 |
| [PLOP3](PLOP3.md) | Predicate Logic Operation | predicate logic (`and/or/xor/not.pred`); simple combinations are folded into ISETP/FSETP's built-in `.AND/.OR/.XOR` (probe `plop3_folded`), standalone PLOP3 shows up in loop/branch control | ✓ [`%ctaid.x as a loop bound`](../verify/RESULTS.md#s2ur_loop) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2616) | 14 |
| [MATCH](MATCH.md) | Match Register Values Across Thread Group | `match.any/all.sync`; `__match_any_sync` | ✓ [`match.any.sync.b32`](../verify/RESULTS.md#match) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4493) | 2 |

## Synchronization / barriers

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [DEPBAR](DEPBAR.md) | Dependency Barrier | `cp.async.wait_group N` / `wait_all` (DEPBAR.LE SB0, N) | ✓ [`cp.async.cg.shared.global + commit_group + wait_group`](../verify/RESULTS.md#cp_async) | 3 |
| [BAR](BAR.md) | Barrier Synchronization | `bar.sync`/`barrier.sync` (`__syncthreads`), `bar.arrive`, `bar.red` (`__syncthreads_count/and/or`) | ✓ [`bar.sync 0`](../verify/RESULTS.md#bar), [`bar.red.popc.u32`](../verify/RESULTS.md#bar_red) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4245) | 8 |
| [MEMBAR](MEMBAR.md) | Memory Barrier | `membar.cta/gl/sys`, `fence.*` (`__threadfence`) | ✓ [`membar.gl`](../verify/RESULTS.md#membar), [`fence.sc.sys`](../verify/RESULTS.md#fence_sys) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4063) | 1 |
| [ERRBAR](ERRBAR.md) | Error Barrier | emitted around `membar.sys` / traps (error containment) | ✓ [`fence.sc.sys`](../verify/RESULTS.md#fence_sys) | 1 |
| [SETCTAID](SETCTAID.md) | Set CTA ID | (unknown; not produced by normal compute code) | not reproduced | 1 |

## Tensor core (MMA)

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [IMMA](IMMA.md) | Integer Matrix Multiply and Accumulate | `mma.sync.*.s8/u8/s4/u4`; `wmma` integer | ✓ [`mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32`](../verify/RESULTS.md#imma) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4520) | 4 |
| [HMMA](HMMA.md) | Matrix Multiply and Accumulate | `mma.sync.aligned.m16n8k8/k16.*.f16/bf16`, `.tf32` m16n8k4/k8; `wmma.mma` half/bf16/tf32 | ✓ [`mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32`](../verify/RESULTS.md#hmma_f16), [`mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32`](../verify/RESULTS.md#hmma_tf32) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4577) | 4 |
| [BMMA](BMMA.md) | Bit Matrix Multiply and Accumulate | `mma.sync.*.b1` (xor/and popc) | ✓ [`mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`](../verify/RESULTS.md#bmma) | 2 |
| [DMMA](DMMA.md) | Matrix Multiply and Accumulate | `mma.sync.aligned.m8n8k4.f64` | ✓ [`mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64`](../verify/RESULTS.md#dmma) | 2 |
| [QMMA](QMMA.md) | *not in Ada table; NVIDIA Blackwell/Rubin table:* FP8 Matrix Multiply and Accumulate Across a Warp | `mma.sync.aligned.m16n8k32.row.col.f32.e4m3/e5m2.e4m3/e5m2.f32` (FP8, PTX 8.4+, sm_89) | ✓ [`mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32`](../verify/RESULTS.md#qmma_e4m3) | 4 |

## Texture / surface

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [SUATOM](SUATOM.md) | Atomic Op on Surface Memory | surface atomics with return; PTX `sured` (no return) lowers to SURED instead (probe `sured`) | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3391) | 20 |
| [SULD](SULD.md) | Surface Load | `suld.b` (`surf2Dread`) | ✓ [`suld.b.2d.b32.trap`](../verify/RESULTS.md#suld) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3321) | 20 |
| [SUQUERY](SUQUERY.md) | *not in NVIDIA tables*: Surface query | unclear: PTX `suq.width` lowers to TXQ on sm_89 (probe `suq`) | not reproduced | 10 |
| [SUST](SUST.md) | Surface Store | `sust.b` (`surf2Dwrite`) | ✓ [`sust.b.2d.b32.trap`](../verify/RESULTS.md#sust) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3359) | 5 |
| [TEX](TEX.md) | Texture Fetch | `tex.*`; `tex2D` etc. | ✓ [`tex.2d.v4.f32.f32`](../verify/RESULTS.md#tex) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2887) | 111 |
| [TLD4](TLD4.md) | Texture Load 4 | `tld4` (`tex2Dgather`) | ✓ [`tld4.r.2d.v4.f32.f32`](../verify/RESULTS.md#tld4) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3032) | 111 |
| [TLD](TLD.md) | Texture Load | unfiltered texel fetch with integer coords: `tex.1d.v4.s32.s32` / `tex1Dfetch` | ✓ [`tex.1d.v4.s32.s32`](../verify/RESULTS.md#tld) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L2956) | 111 |
| [TMML](TMML.md) | Texture MipMap Level | texture LOD query (`__nv_tex_lod`-style); not reproduced | not reproduced · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3092) | 69 |
| [TXD](TXD.md) | Texture Fetch With Derivatives | `tex.grad` | ✓ [`tex.grad.2d.v4.f32.f32`](../verify/RESULTS.md#txd) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3137) | 63 |
| [TXQ](TXQ.md) | Texture Query | `txq` (texture dims) | ✓ [`txq.width.b32`](../verify/RESULTS.md#txq), [`suq.width.b32`](../verify/RESULTS.md#suq) · [NAK](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L3198) | 14 |
| [FOOTPRINT](FOOTPRINT.md) | *not in NVIDIA tables*: Texture footprint query | texture footprint query (`__nv_tex_footprint`) | not reproduced | 102 |

## Uniform datapath

| opcode | NVIDIA description | typically emitted for (PTX / CUDA) | evidence | variants |
|---|---|---|---|---|
| [ULEA](ULEA.md) | Uniform Load Effective Address | warp-uniform address computation | not reproduced | 20 |
| [USHF](USHF.md) | Uniform Funnel Shift | warp-uniform shifts | ✓ [`integer ops on a kernel parameter`](../verify/RESULTS.md#uniform_alu) | 3 |
| [UIMAD](UIMAD.md) | Uniform Integer Multiplication | warp-uniform multiply (e.g. `blockIdx.x * blockDim.x`) | ✓ [`txq.num_mipmap_levels`](../verify/RESULTS.md#uniform_txq) | 14 |
| [UF2FP](UF2FP.md) | Uniform FP32 Down-convert and Pack | uniform FP32->FP16x2 pack | not reproduced | 4 |
| [UMOV](UMOV.md) | Uniform Move | uniform constants/moves (compiler-generated) | ✓ [`txq.num_mipmap_levels`](../verify/RESULTS.md#uniform_txq) | 2 |
| [UP2UR](UP2UR.md) | Uniform Predicate to Uniform Register | uniform predicate spill | not reproduced | 2 |
| [UR2UP](UR2UP.md) | Uniform Register to Uniform Predicate | uniform predicate restore | not reproduced | 3 |
| [VOTEU](VOTEU.md) | Voting across SIMD Thread Group with Results in Uniform Destination | `activemask.b32`; ptxas-generated warp aggregation of atomics/reductions to a uniform address | ✓ [`atom.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_atomic), [`red.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_red) | 2 |
| [USEL](USEL.md) | Uniform Select | warp-uniform select | not reproduced | 2 |
| [UISETP](UISETP.md) | Integer Compare and Set Uniform Predicate | warp-uniform compares (uniform loop exits) | not reproduced | 4 |
| [UIADD3](UIADD3.md) | Uniform Integer Addition | warp-uniform integer adds (loop counters, base pointers) | ✓ [`loop with trip count from kernel param`](../verify/RESULTS.md#uniform_loop), [`%ctaid.x as a loop bound`](../verify/RESULTS.md#s2ur_loop) | 24 |
| [ULOP3](ULOP3.md) | Logic Operation | warp-uniform bitwise logic | ✓ [`integer ops on a kernel parameter`](../verify/RESULTS.md#uniform_alu) | 4 |
| [UPRMT](UPRMT.md) | Uniform Byte Permute | warp-uniform byte permute | ✓ [`integer ops on a kernel parameter`](../verify/RESULTS.md#uniform_alu) | 2 |
| [USGXT](USGXT.md) | Uniform Sign Extend | warp-uniform sign extension | not reproduced | 2 |
| [UBMSK](UBMSK.md) | Uniform Bitfield Mask | warp-uniform mask building | not reproduced | 2 |
| [UPLOP3](UPLOP3.md) | Uniform Predicate Logic Operation | uniform predicate logic | not reproduced | 4 |
| [ULDC](ULDC.md) | Load from Constant Memory into a Uniform Register | `ld.param` / constant bank reads of kernel args into uniform regs | ✓ [`loop with trip count from kernel param`](../verify/RESULTS.md#uniform_loop), [`empty kernel body: param pointer + %tid.x load/store`](../verify/RESULTS.md#prologue) | 7 |
| [UCLEA](UCLEA.md) | Load Effective Address for a Constant | per NVIDIA: load effective address for a constant; no PTX source found | not reproduced | 2 |
| [UFLO](UFLO.md) | Uniform Find Leading One | uniform `bfind`; leader election when ptxas warp-aggregates `red` to a uniform address | ✓ [`red.global.add.u32 to a warp-uniform address`](../verify/RESULTS.md#agg_red) | 4 |
| [UBREV](UBREV.md) | Uniform Bit Reverse | uniform `brev` | ✓ [`integer ops on a kernel parameter`](../verify/RESULTS.md#uniform_alu) | 2 |
| [UPOPC](UPOPC.md) | Uniform Population Count | uniform `popc` (e.g. count of active lanes) | ✓ [`integer ops on a kernel parameter`](../verify/RESULTS.md#uniform_alu) | 2 |

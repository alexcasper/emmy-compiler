# SM120 SASS instruction index

126 distinct SASS opcodes observed on **sm_120** (Blackwell consumer) by compiling 153 PTX probe kernels (PTX `.version 8.8`, `.target sm_120`) with ptxas `Build cuda_12.9.r12.9/compiler.36037853_0` and reading every instruction's raw 128-bit encoding from nvdisasm `Build cuda_12.9.r12.9/compiler.36061206_0` (`-hex -c`). 4112 instructions total.

Everything in `sass/` is derived from these probes: there is **no** kuterdinel-style fuzzed encoding reference for sm_120, so per-opcode "fixed bits" are intersect-derived from the corpus and explicitly labelled partial. The probe corpus is deliberately sm_120-native; no sm_89 claims were copied.

Raw artifacts: `sm120/.cache/sass/results.json` (per-probe instruction dump, gitignored).

The 12-bit opcode values are independently cross-checked against Mesa's open-source NVK compiler (62/67 same-named opcodes agree; see [../verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md)) where `verify/nak.json` is present.

Columns: **NVIDIA description** from the Blackwell/Rubin opcode table ([CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)); **emitted by** = probe names that produced the opcode; **enc** = instructions observed; **ops** = distinct 12-bit opcode-field values; **forms** = normalized operand forms.

## Atomics / reductions

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`ATOM`](ATOM.md) | Atomic Operation on Generic Memory | `atom_generic` | 1 | `519` | 1 |
| [`ATOMG`](ATOMG.md) | Atomic Operation on Global Memory | `atomg`, `atom_v2_f32`, `atom_cas` +2 more | 5 | `159`, `95c`, `c59` | 4 |
| [`ATOMS`](ATOMS.md) | Atomic Operation on Shared Memory | `atoms` | 2 | `319` | 1 |
| [`REDG`](REDG.md) | Reduction Operation on Generic Memory | `red`, `red_v2_f32`, `agg_red` | 3 | `659`, `719` | 2 |
| [`REDUX`](REDUX.md) | Reduction of a Vector Register into a Uniform Register | `redux` | 1 | `23c` | 1 |

## Control flow

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`BRA`](BRA.md) | Relative Branch | `fadd`, `ffma`, `fmul` +146 more | 189 | `e29`, `e2a` | 4 |
| [`BRX`](BRX.md) | Relative Branch Indirect | `brx` | 1 | `929` | 1 |
| [`BSSY`](BSSY.md) | Barrier Set Convergence Synchronization Point | `fdiv_rn`, `diverge`, `brx` +1 more | 7 | `a29` | 3 |
| [`BSYNC`](BSYNC.md) | Synchronize Threads on a Convergence Barrier | `fdiv_rn`, `diverge`, `brx` +1 more | 7 | `829` | 3 |
| [`CALL`](CALL.md) | Call Function | `fdiv_rn`, `cp_async_bulk_tma`, `bmma` +1 more | 4 | `229`, `c2c` | 4 |
| [`EXIT`](EXIT.md) | Exit Program | `fadd`, `ffma`, `fmul` +146 more | 150 | `b29` | 1 |
| [`NANOSLEEP`](NANOSLEEP.md) | Suspend Execution | `nanosleep` | 1 | `bac` | 1 |
| [`NOP`](NOP.md) | No Operation | `fadd`, `ffma`, `fmul` +146 more | 1879 | `189` | 1 |
| [`PREEXIT`](PREEXIT.md) | Dependent Task Launch Hint | `griddepcontrol` | 1 | `b41` | 1 |
| [`RET`](RET.md) | Return From Subroutine | `fdiv_rn`, `bmma`, `call` | 3 | `0a9` | 1 |
| [`WARPSYNC`](WARPSYNC.md) | Synchronize Threads in Warp | `warpsync` | 1 | `12c` | 1 |

## Conversion

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`F2F`](F2F.md) | Floating Point To Floating Point Conversion | `f2f` | 1 | `08c` | 1 |
| [`F2FP`](F2FP.md) | *not in NVIDIA Blackwell/Rubin table* | `f2fp_f16`, `f2fp_bf16`, `f2fp_e4m3` +1 more | 5 | `7c4` | 4 |
| [`F2I`](F2I.md) | Floating Point To Integer Conversion | `f2i`, `f2ip` | 2 | `a0c` | 2 |
| [`I2F`](I2F.md) | Integer To Floating Point Conversion | `i2f` | 1 | `48c` | 1 |
| [`I2FP`](I2FP.md) | Integer to FP32 Convert and Pack | `i2fp` | 1 | `a24` | 1 |
| [`I2I`](I2I.md) | Integer To Integer Conversion | `i2i` | 1 | `1c4` | 1 |
| [`I2IP`](I2IP.md) | Integer To Integer Conversion and Packing | `i2ip` | 1 | `9c4` | 1 |

## FP16 (packed half2)

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`HFMA2`](HFMA2.md) | FP16 Fused Mutiply Add | `fdiv_rn`, `mufu_rcp`, `hadd2` +13 more | 19 | `8c1`, `8c2`, `8c4` | 8 |
| [`HMNMX2`](HMNMX2.md) | FP16 Minimum / Maximum | `hmnmx2` | 1 | `024` | 1 |
| [`HSET2`](HSET2.md) | FP16 Compare And Set | `hset2` | 1 | `cc4` | 1 |
| [`HSETP2`](HSETP2.md) | FP16 Compare And Set Predicate | `hsetp2` | 1 | `2c4` | 1 |

## FP32

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`FADD`](FADD.md) | FP32 Add | `fadd`, `fsetp_selp`, `fdiv_rn` +10 more | 14 | `842`, `844` | 5 |
| [`FCHK`](FCHK.md) | Floating-point Range Check | `fdiv_rn` | 1 | `40c` | 1 |
| [`FFMA`](FFMA.md) | FP32 Fused Multiply and Add | `ffma`, `fdiv_rn` | 18 | `c41`, `c42`, `c44` | 8 |
| [`FMNMX`](FMNMX.md) | FP32 Minimum/Maximum | `fminmax`, `fminmax_nan`, `fminmax_xorsign` | 5 | `904` | 5 |
| [`FMUL`](FMUL.md) | FP32 Multiply | `fmul`, `fsetp_selp`, `mufu_rcp` +6 more | 13 | `041`, `044` | 4 |
| [`FRND`](FRND.md) | Round To Integer | `frnd` | 1 | `e0c` | 1 |
| [`FSEL`](FSEL.md) | Floating Point Select | `fsetp_selp`, `mufu_rcp`, `dsetp` | 5 | `101`, `104` | 3 |
| [`FSETP`](FSETP.md) | FP32 Compare And Set Predicate | `fsetp_selp`, `selp_to_predicated_load`, `fset` +7 more | 16 | `d01`, `d04` | 11 |
| [`MUFU`](MUFU.md) | FP32 Multi Function Operation | `fdiv_rn`, `mufu_rcp`, `mufu_rsqrt` +6 more | 11 | `109`, `10c` | 9 |

## FP64

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`DADD`](DADD.md) | FP64 Add | `dadd`, `dmma` | 2 | `944` | 1 |
| [`DFMA`](DFMA.md) | FP64 Fused Mutiply Add | `dfma` | 1 | `d44` | 1 |
| [`DMUL`](DMUL.md) | FP64 Multiply | `dmul` | 1 | `144` | 1 |
| [`DSETP`](DSETP.md) | FP64 Compare And Set Predicate | `dsetp` | 1 | `544` | 1 |

## Integer

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`BMSK`](BMSK.md) | Bitfield Mask | `bmsk` | 1 | `d84` | 1 |
| [`BREV`](BREV.md) | Bit Reverse | `brev` | 1 | `80c` | 1 |
| [`FLO`](FLO.md) | Find Leading One | `flo`, `agg_atomic`, `uniform_alu` | 4 | `00b`, `00c` | 2 |
| [`IABS`](IABS.md) | Integer Absolute Value | `iabs`, `vabsdiff2` | 3 | `c84` | 1 |
| [`IADD`](IADD.md) | Integer Addition | `iadd64`, `vabsdiff`, `uniform_txq` | 3 | `ac3`, `ac4` | 3 |
| [`IADD3`](IADD3.md) | 3-input Integer Addition | `fdiv_rn`, `iadd`, `isetp_pred` +18 more | 65 | `081`, `083`, `084` | 10 |
| [`IDP`](IDP.md) | Integer Dot Product and Accumulate | `idp`, `vabsdiff4` | 2 | `643`, `644` | 2 |
| [`IMAD`](IMAD.md) | Integer Multiply And Add | `fadd`, `ffma`, `fmul` +144 more | 157 | `241`, `244`, `a41`, `a44`, `e44` | 8 |
| [`ISETP`](ISETP.md) | Integer Compare And Set Predicate | `fdiv_rn`, `isetp_pred`, `vabsdiff` +10 more | 38 | `301`, `303`, `304` | 24 |
| [`LEA`](LEA.md) | LOAD Effective Address | `fdiv_rn`, `lea`, `lea64` +8 more | 12 | `881`, `883`, `884` | 6 |
| [`LOP3`](LOP3.md) | Logic Operation | `fdiv_rn`, `isetp_pred`, `imnmx_from_selp` +8 more | 39 | `481`, `483`, `484` | 5 |
| [`POPC`](POPC.md) | Population count | `popc`, `agg_atomic`, `agg_red` +1 more | 5 | `90b`, `90c` | 2 |
| [`PRMT`](PRMT.md) | Permute Register Pair | `prmt`, `sgxt`, `vabsdiff` +3 more | 15 | `681` | 3 |
| [`SGXT`](SGXT.md) | Sign Extend | `sgxt` | 1 | `584` | 1 |
| [`SHF`](SHF.md) | Funnel Shift | `fdiv_rn`, `lea64`, `shf` +6 more | 23 | `981`, `984` | 8 |
| [`VIADD`](VIADD.md) | SIMD Integer Addition | `vabsdiff4` | 1 | `6c4` | 1 |
| [`VIMNMX`](VIMNMX.md) | SIMD Integer Minimum / Maximum | `imnmx`, `imnmx_from_selp`, `vabsdiff4` | 4 | `124` | 3 |

## Load / store

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`ACQBULK`](ACQBULK.md) | Wait for Bulk Release Status Warp State | `griddepcontrol` | 1 | `741` | 1 |
| [`CCTL`](CCTL.md) | Cache Control | `cctl`, `cluster_barrier`, `fence_cluster` +2 more | 5 | `f19` | 2 |
| [`CCTLL`](CCTLL.md) | Cache Control | `cctll` | 1 | `099` | 1 |
| [`LD`](LD.md) | Load from generic Memory | `ld_generic` | 1 | `019` | 1 |
| [`LDC`](LDC.md) | Load Constant | `fadd`, `ffma`, `fmul` +146 more | 302 | `41d` | 4 |
| [`LDG`](LDG.md) | Load from Global Memory | `fadd`, `ffma`, `fmul` +129 more | 258 | `819` | 8 |
| [`LDGDEPBAR`](LDGDEPBAR.md) | Global Load Dependency Barrier | `cp_async` | 1 | `f59` | 1 |
| [`LDGSTS`](LDGSTS.md) | Asynchronous Global to Shared Memcopy | `cp_async` | 1 | `75f` | 1 |
| [`LDL`](LDL.md) | Load within Local Memory Window | `ldl_stl`, `cctll` | 2 | `c19` | 1 |
| [`LDS`](LDS.md) | Load within Shared Memory Window | `lds_sts`, `cp_async`, `stmatrix` +3 more | 9 | `219` | 3 |
| [`LDSM`](LDSM.md) | Load Matrix from Shared Memory with Element Size Expansion | `ldsm`, `ldsm_trans` | 2 | `dc1` | 2 |
| [`QSPC`](QSPC.md) | Query Space | `qspc` | 1 | `55c` | 1 |
| [`ST`](ST.md) | Store to Generic Memory | `st_generic` | 1 | `a19` | 1 |
| [`STAS`](STAS.md) | Asynchronous Store to Distributed Shared Memory With Explicit Synchronization | `st_async` | 1 | `bdb` | 1 |
| [`STG`](STG.md) | Store to Global Memory | `fadd`, `ffma`, `fmul` +135 more | 142 | `619` | 4 |
| [`STL`](STL.md) | Store to Local Memory | `ldl_stl`, `cctll` | 2 | `e1c` | 1 |
| [`STS`](STS.md) | Store to Shared Memory | `lds_sts`, `ldsm`, `ldsm_trans` | 3 | `11c` | 1 |
| [`STSM`](STSM.md) | Store Matrix to Shared Memory | `stmatrix`, `stmatrix_x4` | 2 | `221` | 2 |
| [`UBLKCP`](UBLKCP.md) | Bulk Data Copy | `cp_async_bulk_tma` | 1 | `5dc` | 1 |
| [`UBLKPF`](UBLKPF.md) | Bulk Data Prefetch | `cp_async_bulk_prefetch` | 1 | `3dc` | 1 |
| [`UMEMSETS`](UMEMSETS.md) | Initialize Shared Memory | `st_bulk` | 1 | `d3c` | 1 |

## Miscellaneous

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`PMTRIG`](PMTRIG.md) | Performance Monitor Trigger | `pmtrig` | 1 | `801` | 1 |

## Movement

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`B2R`](B2R.md) | Move Barrier To Register | `bar_red` | 1 | `38c` | 1 |
| [`CS2R`](CS2R.md) | Move Special Register to Register | `cs2r`, `globaltimer`, `cp_async_bulk_tma` +1 more | 4 | `a01` | 2 |
| [`LEPC`](LEPC.md) | Load Effective PC | `cp_async_bulk_tma` | 1 | `729` | 1 |
| [`MOV`](MOV.md) | Move | `fdiv_rn`, `vabsdiff`, `vabsdiff2` +22 more | 106 | `401`, `403`, `404` | 4 |
| [`MOVM`](MOVM.md) | Move Matrix with Transposition or Expansion | `movm`, `bmma` | 13 | `5c4` | 2 |
| [`R2UR`](R2UR.md) | Move from Vector Register to a Uniform Register | `cp_async_bulk_tma`, `cp_async_bulk_prefetch` | 4 | `534` | 3 |
| [`S2R`](S2R.md) | Move Special Register to Register | `fadd`, `ffma`, `fmul` +145 more | 157 | `989` | 1 |
| [`S2UR`](S2UR.md) | Move Special Register to Uniform Register | `lds_sts`, `cp_async`, `ldsm` +7 more | 10 | `c39` | 1 |
| [`SEL`](SEL.md) | Select Source with Predicate | `fset`, `fdiv_rn`, `hsetp2` +2 more | 6 | `e01`, `e04` | 2 |
| [`SHFL`](SHFL.md) | Warp Wide Register Shuffle | `shfl`, `atoms`, `bssy_bsync` +1 more | 10 | `919`, `91a`, `91f` | 4 |

## Predicate / compare

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`ELECT`](ELECT.md) | Elect a Leader Thread | `elect_sync`, `cp_async_bulk_tma` | 2 | `f41` | 1 |
| [`MATCH`](MATCH.md) | Match Register Values Across Thread Group | `match` | 1 | `85c` | 1 |
| [`PLOP3`](PLOP3.md) | Predicate Logic Operation | `fdiv_rn`, `cp_async_bulk_tma`, `cp_async_bulk_prefetch` +3 more | 21 | `381` | 1 |
| [`VOTE`](VOTE.md) | Vote Across SIMT Thread Group | `vote`, `atoms` | 2 | `601` | 1 |

## Synchronization / barriers

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`BAR`](BAR.md) | Barrier Synchronization | `lds_sts`, `cp_async`, `ldsm` +7 more | 10 | `b8d` | 2 |
| [`CGAERRBAR`](CGAERRBAR.md) | CGA Error Barrier | `cluster_barrier`, `fence_cluster`, `membar` +1 more | 4 | `d5a` | 1 |
| [`DEPBAR`](DEPBAR.md) | Dependency Barrier | `cp_async` | 1 | `589` | 1 |
| [`ERRBAR`](ERRBAR.md) | Error Barrier | `cluster_barrier`, `fence_cluster`, `membar` +1 more | 4 | `d59` | 1 |
| [`MEMBAR`](MEMBAR.md) | Memory Barrier | `cluster_barrier`, `fence_cluster`, `membar` +1 more | 4 | `499` | 3 |
| [`SYNCS`](SYNCS.md) | Sync Unit | `cp_async_bulk_tma`, `mbarrier_red`, `st_async` | 7 | `4da`, `e59`, `e5a` | 4 |
| [`UCGABAR_ARV`](UCGABAR_ARV.md) | CGA Barrier Synchronization | `cluster_barrier` | 1 | `e39` | 1 |
| [`UCGABAR_WAIT`](UCGABAR_WAIT.md) | CGA Barrier Synchronization | `cluster_barrier` | 1 | `e3b` | 1 |

## Tensor core (MMA)

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`DMMA`](DMMA.md) | Matrix Multiply and Accumulate | `dmma` | 1 | `fc4` | 1 |
| [`HMMA`](HMMA.md) | Matrix Multiply and Accumulate | `hmma_f16`, `hmma_bf16`, `hmma_tf32` | 3 | `3c4` | 3 |
| [`IMMA`](IMMA.md) | Integer Matrix Multiply and Accumulate | `imma`, `bmma` | 9 | `ec4` | 2 |
| [`QMMA`](QMMA.md) | FP8 Matrix Multiply and Accumulate Across a Warp | `qmma_e4m3`, `qmma_e5m2` | 2 | `5e4` | 2 |

## Texture / surface

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`SULD`](SULD.md) | Surface Load | `suld` | 1 | `99f` | 1 |
| [`SURED`](SURED.md) | Reduction Op on Surface Memory | `sured` | 1 | `f9f` | 1 |
| [`SUST`](SUST.md) | Surface Store | `sust` | 1 | `b9f` | 1 |
| [`TEX`](TEX.md) | Texture Fetch | `tex` | 1 | `06f` | 1 |
| [`TLD`](TLD.md) | Texture Load | `tld` | 1 | `66f` | 1 |
| [`TLD4`](TLD4.md) | Texture Load 4 | `tld4` | 1 | `c6f` | 1 |
| [`TXD`](TXD.md) | Texture Fetch With Derivatives | `txd` | 1 | `36f` | 1 |
| [`TXQ`](TXQ.md) | Texture Query | `txq`, `suq` | 2 | `f6f` | 1 |

## Uniform datapath

| opcode | NVIDIA description | emitted by probes | enc | ops | forms |
|---|---|---|---|---|---|
| [`LDCU`](LDCU.md) | Load a Value from Constant Memory into a Uniform Register | `fadd`, `ffma`, `fmul` +144 more | 160 | `35e` | 2 |
| [`UBREV`](UBREV.md) | Uniform Bit Reverse | `uniform_alu` | 1 | `7d4` | 1 |
| [`UFLO`](UFLO.md) | Uniform Find Leading One | `agg_red` | 1 | `bd4` | 1 |
| [`UIADD3`](UIADD3.md) | Uniform Integer Addition | `cp_async_bulk_tma`, `mbarrier_red`, `st_async` +2 more | 7 | `091` | 3 |
| [`UIMAD`](UIMAD.md) | Uniform Integer Multiplication | `uniform_txq` | 1 | `252` | 1 |
| [`UISETP`](UISETP.md) | Uniform Integer Compare and Set Uniform Predicate | `cluster_barrier`, `cp_async_bulk_tma`, `uniform_loop` +1 more | 4 | `311`, `314` | 4 |
| [`ULEA`](ULEA.md) | Uniform Load Effective Address | `lds_sts`, `cp_async`, `ldsm` +6 more | 11 | `894` | 1 |
| [`ULOP3`](ULOP3.md) | Uniform Logic Operation | `uniform_alu` | 1 | `494` | 1 |
| [`UMOV`](UMOV.md) | Uniform Move | `vabsdiff4`, `lds_sts`, `cp_async` +15 more | 28 | `411`, `413` | 3 |
| [`UPOPC`](UPOPC.md) | Uniform Population Count | `uniform_alu` | 1 | `fd4` | 1 |
| [`UPRMT`](UPRMT.md) | Uniform Byte Permute | `uniform_alu` | 1 | `691` | 1 |
| [`USHF`](USHF.md) | Uniform Funnel Shift | `cp_async_bulk_tma`, `mbarrier_red`, `st_async` +1 more | 8 | `991` | 3 |
| [`VOTEU`](VOTEU.md) | Voting across SIMD Thread Group with Results in Uniform Destination | `agg_atomic`, `agg_red`, `activemask` | 3 | `611` | 1 |

## Divergence vs the SM89 knowledge base

sm89/sass documents 151 opcodes (kuterdinel.com fuzzed encoding pages for Ada). This corpus observed 126 opcodes on sm_120. Both directions are *observations*, not exhaustive ISA statements: an opcode absent here was simply never emitted by these 158 probe kernels.

### Observed on sm_120, not in the sm89 opcode set

| opcode | note (from our probes) |
|---|---|
| [`ACQBULK`](ACQBULK.md) | griddepcontrol.wait (sm_90+ feature) |
| [`CGAERRBAR`](CGAERRBAR.md) | cluster-wide error barrier (emitted with fence.acq_rel.cluster) |
| [`ELECT`](ELECT.md) | elect.sync (rejected on sm_89, legal on sm_120) |
| [`IADD`](IADD.md) | new 2-input add; sm89 had only IADD3 (both exist on sm_120) |
| [`LDCU`](LDCU.md) | rename of sm89 `ULDC` (uniform constant load); prologue uses `LDCU.64 UR4, c[0x0][0x358]` |
| [`PREEXIT`](PREEXIT.md) | griddepcontrol.launch_dependents (sm_90+ feature) |
| [`REDG`](REDG.md) | rename of sm89 `RED` (global reduction without return) |
| [`STAS`](STAS.md) | st.async (sm_90+ feature; new opcode name here) |
| [`STSM`](STSM.md) | stmatrix (rejected on sm_89, legal on sm_120) |
| [`SURED`](SURED.md) | surface reduction (no return) |
| [`SYNCS`](SYNCS.md) | async-group synchronize (emitted around UBLKCP/STAS/mbarrier sequences) |
| [`UBLKCP`](UBLKCP.md) | cp.async.bulk / TMA copy (sm_90+ feature) |
| [`UBLKPF`](UBLKPF.md) | cp.async.bulk.prefetch.L2.global (sm_90+ feature) |
| [`UCGABAR_ARV`](UCGABAR_ARV.md) | barrier.cluster.arrive (sm_90+ feature) |
| [`UCGABAR_WAIT`](UCGABAR_WAIT.md) | barrier.cluster.wait (sm_90+ feature) |
| [`UMEMSETS`](UMEMSETS.md) | st.bulk shared-memory init (sm_90+ feature) |
| [`VIADD`](VIADD.md) | video-pipe integer add (vabsdiff4 emulation) |
| [`VIMNMX`](VIMNMX.md) | video-pipe integer min/max; PTX min.s32 lowers here (sm89: IMNMX) |

### In the sm89 opcode set, not observed on sm_120 here

| opcode | status in this corpus |
|---|---|
| ALD | graphics-only ops (ALD, AL2P, IPA, ISBERD, OUT, PIXLD, LDTRAM, CSMTEST) - no PTX equivalent, not probed |
| BMMA | b1 mma.sync lowered to IMMA+MOVM+LOP3 emulation (`probe bmma`) |
| BMOV | convergence-barrier save/restore - not triggered by this corpus |
| BREAK | divergent break - not triggered by this corpus |
| BRXU | uniform-index jump table - not probed |
| F2IP | not produced by this probe corpus (may still exist in the ISA) |
| FOOTPRINT | texture footprint query - not probed |
| FSET | not reproduced (sm89 also could not reproduce it) |
| FSWZADD | graphics/derivative op - no PTX source; not probed |
| GETLMEMBASE | local-memory base - not triggered by this corpus |
| HADD2 | add.f16x2 lowered to HFMA2 (`probe hadd2`) |
| HMUL2 | mul.f16x2 lowered to HFMA2 (`probe hmul2`) |
| IMNMX | min/max.s32 lowered to VIMNMX (`probe imnmx`) |
| JMP | absolute jump - not probed |
| JMX | absolute indirect jump - not probed |
| JMXU | uniform absolute indirect jump - not probed |
| P2R | predicate pack - not triggered by this corpus |
| R2P | predicate unpack - not triggered by this corpus |
| RED | red.global lowered to REDG (`probe red`) |
| RPCMOV | return-PC move - not triggered by this corpus |
| SETCTAID | cluster CTA-id set - not probed |
| SUATOM | surface atomic with return - not probed (SURED/SUST were) |
| SUQUERY | PTX suq lowered to TXQ (`probe suq`) |
| TMML | texture mip-level query - not probed |
| UBMSK | uniform bit-mask - not triggered by this corpus |
| UCLEA | not triggered by this corpus |
| UF2FP | uniform FP pack - not triggered by this corpus |
| ULDC | renamed LDCU (`every probe's prologue`) |
| UP2UR | uniform predicate spill - not triggered by this corpus |
| UPLOP3 | uniform predicate logic - not triggered by this corpus |
| UR2UP | uniform predicate restore - not triggered by this corpus |
| USEL | uniform select - not triggered by this corpus |
| USGXT | uniform sign-extend - not triggered by this corpus |
| VABSDIFF | PTX vabsdiff emulated with IADD3/ISETP/PRMT (`probe vabsdiff`) |
| VABSDIFF4 | PTX vabsdiff4 emulated with VIADD+VIMNMX+IDP (`probe vabsdiff4`) |
| YIELD | spin-loop yield - not triggered by this corpus |

Graphics-only sm89 opcodes not probed here (no PTX equivalent): `AL2P`, `CSMTEST`, `IPA`, `ISBERD`, `LDTRAM`, `OUT`, `PIXLD`.

### Rejected sm_120 probes (architecture evidence)

| PTX construct | ptxas 12.9 result |
|---|---|
| `cvt.rn.satfinite.e2m1x2.f32 (FP4; sm_100a+ family)` | line 16; error   : Instruction 'cvt with .e2m1x2' not supported on .target 'sm_120' |
| `redux.sync.min.f32 (sm_100a family feature)` | line 16; error   : Instruction 'redux.f32' not supported on .target 'sm_120' |
| `tensormap.replace.tile.global_address (sm_90+)` | line 16; error   : Instruction 'tensormap.replace' not supported on .target 'sm_120' |
| `setmaxnreg.inc.sync.aligned.u32 (sm_90a family only)` | line 16; error   : Instruction 'setmaxnreg.inc' not supported on .target 'sm_120' |
| `wgmma.fence.sync.aligned (sm_90a family only)` | line 16; error   : Instruction 'wgmma.fence' not supported on .target 'sm_120' |
| `tcgen05.relinquish_alloc_permit (sm_100a family only)` | line 16; error   : Instruction 'tcgen05.relinquish_alloc_permit' not supported on .target 'sm_120' |
| `mma.sync kind::mxf8f6f4 block-scaled (sm_100a/120a family)` | line 16; error   : Instruction 'mma with block scale' not supported on .target 'sm_120' |
| `tcgen05.mma (sm_100a/sm_103a; rejected on sm_120 even as sm_120a?)` via sm_120a | line 16; error   : Instruction 'tcgen05.fence' not supported on .target 'sm_120a' |
| `setmaxnreg under -arch=sm_120a (family-arch check)` via sm_120a | ACCEPTED (expected reject) |


## Control-code layout (bits 105-125)

Hypothesis (from sm_89 microbenchmark literature, tested here): stall(105-108), yield(109), write/result scoreboard(110-112), read scoreboard(113-115), wait mask(116-121), reuse(122-125). On sm_120 the same classification falls out of the encodings:

- **110-112 != 7** on result-latency producers (>50% of instances): LDG, LD, LDS, LDL, LDC, LDCU, MUFU, S2R, S2UR, SHFL, MATCH, REDUX, MOVM, B2R, TEX/TLD/TLD4/TXD/TXQ, SULD, conversions (F2F/F2I/I2F), FP64 ops, FCHK, QSPC, LDGDEPBAR, SYNCS - i.e. instructions whose *result* arrives late. Same class as sm_89.
- **113-115 != 7** on late source readers: SUST, SURED, UBLKCP, UBLKPF, UMEMSETS (and STG/ATOMS only in specific fence sequences) - instructions that read their *source registers* late. Same class as sm_89.
- **bits 122-125 (reuse) were 0 in this corpus** and bits 126-127 were always 0.

### Same instructions, different schedules

15 instructions with identical opcode, operands and immediates were re-encoded between `-O0` and `-O3`. Every differing bit lies in 105-117 (observed: 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 116, 117); no bits below 105 ever differed. So the scheduling control code occupies the same region as sm_89 (stall/yield/scoreboards/wait), and no data-path bits move with the schedule. The 3-bit field *boundaries* cannot be proven from encoding diffs alone, but the producer/consumer classification above is consistent with the sm_89 assignment (stall 105-108, yield 109, write 110-112, read 113-115, wait 116-121).


## Regenerate

```
PTXAS=/mnt/d/ops/emmy/toolchain/cuda12.9/bin/ptxas \
NVDISASM=/mnt/d/ops/emmy/toolchain/cuda12.9/bin/nvdisasm \
  python3 sm120/tools/sass_probe.py          # probe battery (resumable)
  python3 sm120/tools/sass_probe.py --sched  # -O0/-O2/-O3 control-code study
  python3 sm120/tools/build_sass.py          # this index + per-opcode pages
```

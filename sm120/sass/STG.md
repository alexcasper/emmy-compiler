# STG (SM120 SASS)

**NVIDIA:** Store to Global Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: global store (category: Load / store)

Observed on sm_120: 142 instruction(s) across 138 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fadd`: `add.f32`
- `ffma`: `fma.rn.f32`
- `fmul`: `mul.f32`
- `fminmax`: `min.f32 / max.f32`
- `fminmax_nan`: `min.NaN.f32 / max.NaN.f32 (sm_80+ NaN propagation)`
- `fminmax_xorsign`: `min.xorsign.abs.f32 (sm_80+ modifier combo)`
- `fsetp_selp`: `setp.lt.f32 + selp.f32 (both arms computed)`
- `selp_to_predicated_load`: `selp.f32 between two loaded values`
- `fset`: `set.lt.u32.f32`
- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `mufu_rcp`: `rcp.approx.f32`
- `mufu_rsqrt`: `rsqrt.approx.f32`
- `mufu_sqrt`: `sqrt.approx.f32`
- `mufu_lg2`: `lg2.approx.f32`
- `mufu_ex2`: `ex2.approx.f32`
- `mufu_sin`: `sin.approx.f32`
- `mufu_cos`: `cos.approx.f32`
- `mufu_tanh`: `tanh.approx.f32`
- `frnd`: `cvt.rmi.f32.f32 (floor)`
- `dadd`: `add.f64`
- `dfma`: `fma.rn.f64`
- `dmul`: `mul.f64`
- `dsetp`: `setp.lt.f64`
- `hadd2`: `add.f16x2`
- `hfma2`: `fma.rn.f16x2`
- `hfma2_bf16`: `fma.rn.bf16x2`
- `hmul2`: `mul.f16x2`
- `hmnmx2`: `min.f16x2`
- `hsetp2`: `setp.lt.f16x2`
- `hset2`: `set.lt.f16x2.f16x2`
- `iadd`: `add.s32 / sub.s32`
- `iadd64`: `add.s64`
- `imad`: `mad.lo.s32`
- `imad_wide`: `mul.wide.s32`
- `imad_hi`: `mul.hi.u32`
- `iabs`: `abs.s32`
- `imnmx`: `min.s32`
- `isetp_pred`: `setp.lt.s32 + selp.b32`
- `imnmx_from_selp`: `setp.lt.s32 + selp.b32 forming min()`
- `lea`: `shl.b32 + add.s32`
- `lea64`: `pointer + (sign-extended s32 index << 2)`
- `lop3`: `and/xor/or of 3 values`
- `shf`: `shf.l.wrap.b32`
- `shl64`: `shl.b64 by register`
- `prmt`: `prmt.b32`
- `sgxt`: `bfe.s32 (signed field extract)`
- `bmsk`: `bmsk.clamp.b32`
- `flo`: `bfind.u32 / clz.b32`
- `brev`: `brev.b32`
- `popc`: `popc.b32`
- `idp`: `dp4a.s32.s32`
- `vabsdiff`: `vabsdiff.u32.u32.u32 (observe)`
- `vabsdiff2`: `vabsdiff2.u32.u32.u32 (observe)`
- `vabsdiff4`: `vabsdiff4.u32.u32.u32.add`
- `f2f`: `cvt.rn.f32.f64`
- `f2i`: `cvt.rzi.s32.f32`
- `i2fp`: `cvt.rn.f32.s32`
- `i2f`: `cvt.rn.f64.s32`
- `f2fp_f16`: `cvt.rn.f16x2.f32`
- `f2fp_bf16`: `cvt.rn.bf16x2.f32`
- `f2fp_e4m3`: `cvt.rn.satfinite.e4m3x2.f32 (FP8)`
- `cvt_e4m3_to_f16x2`: `cvt.rn.f16x2.e4m3x2 (FP8 -> half2)`
- `i2i`: `cvt.sat.s8.s32`
- `i2ip`: `cvt.pack.sat.s8.s32.b32`
- `f2ip`: `cvt.rni.sat.s8.f32 (observe only)`
- `shfl`: `shfl.sync.bfly.b32`
- `vote`: `vote.sync.ballot.b32`
- `match`: `match.any.sync.b32`
- `redux`: `redux.sync.add.u32`
- `s2r`: `mov.u32 %laneid`
- `cs2r`: `mov.u64 %clock64`
- `globaltimer`: `mov.u64 %globaltimer`
- `s2r_ctaid`: `mov.u32 %ctaid.x stored directly`
- `s2ur`: `%ctaid.x used in uniform address math (observe)`
- `movm`: `movmatrix.sync.aligned.m8n8.trans.b16`
- `lds_sts`: `ld.shared / st.shared`
- `ld_generic`: `ld (generic pointer)`
- `ldg_hints`: `ld.global.L1::evict_last.u32 (cache eviction hint)`
- `ldg_l2_128b`: `ld.global.L2::128B.u32 (L2 fetch granularity hint)`
- `ldg_v2`: `ld.global.v2.f32`
- `ldg_nc`: `ld.global.nc.v4.f32`
- `stg_v4`: `st.global.v4.f32`
- `ldl_stl`: `dynamically indexed .local array`
- `ldc`: `ld.const with dynamic index`
- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`
- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `ldsm_trans`: `ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16`
- `atomg`: `atom.global.add.u32 (result used)`
- `atoms`: `atom.shared.add.u32`
- `atom_generic`: `atom.add.u32 (generic)`
- `atom_v2_f32`: `atom.global.v2.add.f32 (vector atomic, sm_90+)`
- `atom_cas`: `atom.global.cas.b32`
- `atom_add_f32`: `atom.global.add.f32 (fast fp32 atomic)`
- `qspc`: `isspacep.shared`
- `elect_sync`: `elect.sync (sm_90+)`
- `stmatrix`: `stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)`
- `stmatrix_x4`: `stmatrix.sync.aligned.m8n8.x4.shared.b16`
- `mapa`: `mapa.u64 (cluster address mapping, sm_90+)`
- `cluster_ctarank`: `%cluster_ctarank special register`
- `cluster_barrier`: `barrier.cluster.arrive/wait.aligned`
- `fence_cluster`: `fence.acq_rel.cluster`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `mbarrier_red`: `mbarrier.arrive.release.cluster.shared::cta.b64 (sm_90+)`
- `st_bulk`: `st.bulk (shared-memory init, sm_90+)`
- `griddepcontrol`: `griddepcontrol.wait / launch_dependents (sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`
- `hmma_f16`: `mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32`
- `hmma_bf16`: `mma.sync.aligned.m16n8k16.row.col.f32.bf16.bf16.f32`
- `hmma_tf32`: `mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32`
- `imma`: `mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32`
- `dmma`: `mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64 (FP64 MMA)`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`
- `qmma_e4m3`: `mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 (FP8)`
- `qmma_e5m2`: `mma.sync.aligned.m16n8k32.row.col.f32.e5m2.e5m2.f32 (FP8)`
- `bar`: `bar.sync 0`
- `bar_red`: `bar.red.popc.u32`
- `membar`: `membar.gl`
- `fence_sys`: `fence.sc.sys`
- `diverge`: `data-dependent loop`
- `call`: `.func .noinline call`
- `brx`: `brx.idx (jump table)`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `prologue`: `empty kernel body: param pointer + %tid.x load/store`
- `bssy_bsync`: `divergent loop exit followed by a warp-synchronous op`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`
- `activemask`: `activemask.b32`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`
- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`
- `uniform_txq`: `txq.num_mipmap_levels (handle arithmetic on uniform datapath)`
- `cctll`: `prefetch.local.L1`
- `plop3_folded`: `xor.pred of two compares (folded into ISETP/FSETP combine op)`
- `tex`: `tex.2d.v4.f32.f32`
- `tld4`: `tld4.r.2d.v4.f32.f32`
- `txq`: `txq.width.b32`
- `suld`: `suld.b.2d.b32.trap`
- `tld`: `tex.1d.v4.s32.s32 (integer coords)`
- `txd`: `tex.grad.2d.v4.f32.f32`
- `suq`: `suq.width.b32`

12-bit opcode field (bits 0-11) values observed: `0x619`.

## Encoding observations

**Constant bits across all 142 observed instance(s): 108 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0110000110011110000000000..0.000....000000.000.00000000000000000
0...0.001..11000000010000011000000000000010001111111....0.000000
```

4 normalized operand form(s) observed:

### `STG.E desc[UR][R.IMM], R` - 126 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | fadd |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | ffma |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | fmul |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | fminmax |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | fminmax_nan |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | fminmax_xorsign |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | fsetp_selp |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | selp_to_predicated_load |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | fset |
| `STG.E desc[UR4][R4.64], R7` | `0000000704007986 000fe2000c101904` | fdiv_rn |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | mufu_rcp |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | mufu_rsqrt |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | mufu_sqrt |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | mufu_lg2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | mufu_ex2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | mufu_sin |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | mufu_cos |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | mufu_tanh |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | frnd |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | hadd2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | hfma2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | hfma2_bf16 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | hmul2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | hmnmx2 |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 000fe2000c101904` | hsetp2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | hset2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | iadd |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | imad |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | imad_hi |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | iabs |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | imnmx |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | isetp_pred |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | imnmx_from_selp |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | lea |
| `STG.E desc[UR4][R4.64], R7` | `0000000704007986 000fe2000c101904` | lea64 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | lop3 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | shf |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | prmt |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | sgxt |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | bmsk |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | flo |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | brev |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | popc |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | idp |
| `STG.E desc[UR4][R2.64], R4` | `0000000402007986 000fe2000c101904` | vabsdiff |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | vabsdiff2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | vabsdiff4 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | f2f |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | f2i |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | i2fp |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | f2fp_f16 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | f2fp_bf16 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | f2fp_e4m3 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | cvt_e4m3_to_f16x2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | i2i |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | i2ip |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | f2ip |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | shfl |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | vote |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | match |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | redux |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 002fe2000c101904` | s2r |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 002fe2000c101904` | s2r_ctaid |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 000fe2000c101904` | s2ur |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | movm |
| `STG.E desc[UR6][R2.64], R7` | `0000000702007986 001fe2000c101906` | lds_sts |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | ld_generic |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | ldg_hints |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | ldg_l2_128b |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | ldg_v2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | ldg_nc |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 004fe2000c101904` | ldl_stl |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | ldc |
| `STG.E desc[UR6][R2.64], R7` | `0000000702007986 002fe2000c101906` | cp_async |
| `STG.E desc[UR6][R2.64], R11` | `0000000b02007986 000fe2000c101906` | ldsm |
| `STG.E desc[UR6][R2.64], R7` | `0000000702007986 001fe2000c101906` | ldsm_trans |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | atomg |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 004fe2000c101906` | atoms |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | atom_generic |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 000fe2000c101904` | atom_v2_f32 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | atom_cas |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | atom_add_f32 |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 000fe2000c101904` | qspc |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 002fe2000c101904` | elect_sync |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 001fe2000c101904` | stmatrix |
| `STG.E desc[UR4][R2.64], R9` | `0000000902007986 001fe2000c101904` | stmatrix_x4 |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 002fe2000c101904` | cluster_ctarank |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 020fe2000c101904` | cluster_barrier |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | fence_cluster |
| `STG.E desc[UR36][R16.64], R3` | `0000000310007986 000fe2000c101924` | cp_async_bulk_tma |
| `STG.E desc[UR8][R2.64], R1` | `0000000102007986 001fe2000c101908` | mbarrier_red |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 002fe2000c101904` | st_bulk |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | griddepcontrol |
| `STG.E desc[UR10][R2.64], R5` | `0000000502007986 002fe2000c10190a` | st_async |
| `STG.E desc[UR4][R2.64], R11` | `0000000b02007986 000fe2000c101904` | hmma_f16 |
| `STG.E desc[UR4][R2.64], R11` | `0000000b02007986 000fe2000c101904` | hmma_bf16 |
| `STG.E desc[UR4][R2.64], R11` | `0000000b02007986 000fe2000c101904` | hmma_tf32 |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 000fe2000c101904` | imma |
| `STG.E desc[UR4][R16.64], R3` | `0000000310007986 000fe2000c101904` | bmma |
| `STG.E desc[UR4][R2.64], R11` | `0000000b02007986 000fe2000c101904` | qmma_e4m3 |
| `STG.E desc[UR4][R2.64], R11` | `0000000b02007986 000fe2000c101904` | qmma_e5m2 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | bar |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | bar_red |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | membar |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | fence_sys |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | diverge |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 000fe2000c101904` | call |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | brx |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | uniform_loop |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | prologue |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 001fe2000c101904` | bssy_bsync |
| `STG.E desc[UR4][R2.64], R7` | `0000000702007986 000fe2000c101904` | agg_atomic |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 002fe2000c101906` | activemask |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 000fe2000c101904` | s2ur_loop |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 000fe2000c101906` | uniform_alu |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 004fe2000c101906` | uniform_txq |
| `STG.E desc[UR4][R4.64], R2` | `0000000204007986 004fe2000c101904` | cctll |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 004fe2000c101904` | plop3_folded |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 020fe2000c101906` | tex |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 020fe2000c101906` | tld4 |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 022fe2000c101904` | txq |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 020fe2000c101904` | suld |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 020fe2000c101906` | tld |
| `STG.E desc[UR6][R2.64], R5` | `0000000502007986 020fe2000c101906` | txd |
| `STG.E desc[UR4][R2.64], R5` | `0000000502007986 022fe2000c101904` | suq |

### `STG.E.IMM desc[UR][R.IMM], R` - 12 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 001fe2000c101b04` | dadd |
| `STG.E.64 desc[UR4][R2.64], R6` | `0000000602007986 001fe2000c101b04` | dfma |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 001fe2000c101b04` | dmul |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 000fe2000c101b04` | dsetp |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 000fe2000c101b04` | iadd64 |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 000fe2000c101b04` | imad_wide |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 000fe2000c101b04` | shl64 |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 001fe2000c101b04` | i2f |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 002fe2000c101b04` | cs2r |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 002fe2000c101b04` | globaltimer |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 000fe2000c101b04` | mapa |
| `STG.E.64 desc[UR4][R2.64], R4` | `0000000402007986 001fe2000c101b04` | dmma |

### `STG.E desc[UR][R.IMM+IMM], R` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STG.E desc[UR4][R2.64+0x4], R7` | `0000040702007986 008fe2000c101904` | fence_cluster |
| `STG.E desc[UR4][R2.64+0x4], R7` | `0000040702007986 008fe2000c101904` | membar |
| `STG.E desc[UR4][R2.64+0x4], R7` | `0000040702007986 008fe2000c101904` | fence_sys |

### `STG.E.IMM desc[UR][R.IMM+IMM], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STG.E.128 desc[UR4][R2.64+0x40], R4` | `0000400402007986 000fe2000c101d04` | stg_v4 |


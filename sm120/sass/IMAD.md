# IMAD (SM120 SASS)

**NVIDIA:** Integer Multiply And Add (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: integer multiply-add (.WIDE 64-bit, .HI, and .MOV/IADD move idioms) (category: Integer)

Observed on sm_120: 157 instruction(s) across 147 probe(s).

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
- `st_generic`: `st (generic pointer)`
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
- `red`: `red.global.add.u32 (no result)`
- `atoms`: `atom.shared.add.u32`
- `atom_generic`: `atom.add.u32 (generic)`
- `atom_v2_f32`: `atom.global.v2.add.f32 (vector atomic, sm_90+)`
- `red_v2_f32`: `red.global.v2.add.f32 (vector reduction, sm_90+)`
- `atom_cas`: `atom.global.cas.b32`
- `atom_add_f32`: `atom.global.add.f32 (fast fp32 atomic)`
- `qspc`: `isspacep.shared`
- `cctl`: `prefetch.global.L1`
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
- `cp_async_bulk_prefetch`: `cp.async.bulk.prefetch.L2.global (sm_90+)`
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
- `nanosleep`: `nanosleep.u32`
- `warpsync`: `bar.warp.sync with partial mask`
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
- `sured`: `sured.b.add.2d.u32.trap`
- `suq`: `suq.width.b32`
- `sust`: `sust.b.2d.b32.trap`

12-bit opcode field (bits 0-11) values observed: `0x241`, `0x244`, `0xa41`, `0xa44`, `0xe44`.

## Encoding observations

**Constant bits across all 157 observed instance(s): 84 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
..1001000.0.1110...0.000...00000.0.000.000.000000000000.........
........0.0000000111000111100000000000000.....111111....00.0.000
```

8 normalized operand form(s) observed:

### `IMAD.WIDE.U32 R, R, IMM, R` - 148 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fadd |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ffma |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fmul |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fminmax |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fminmax_nan |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fminmax_xorsign |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fsetp_selp |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | selp_to_predicated_load |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fset |
| `IMAD.WIDE.U32 R4, R3, 0x40, R4` | `0000004003047825 002fca00078e0004` | fdiv_rn |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_rcp |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_rsqrt |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_sqrt |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_lg2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_ex2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_sin |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_cos |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mufu_tanh |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | frnd |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | dadd |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | dfma |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | dmul |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | dsetp |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hadd2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hfma2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hfma2_bf16 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hmul2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hmnmx2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hsetp2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hset2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | iadd |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | iadd64 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | imad |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | imad_wide |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | imad_hi |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | iabs |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | imnmx |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | isetp_pred |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | imnmx_from_selp |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | lea |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | lea64 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | lop3 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | shf |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | shl64 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | prmt |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | sgxt |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | bmsk |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | flo |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | brev |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | popc |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | idp |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | vabsdiff |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | vabsdiff2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | vabsdiff4 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | f2f |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | f2i |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | i2fp |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | i2f |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | f2fp_f16 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | f2fp_bf16 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | f2fp_e4m3 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | cvt_e4m3_to_f16x2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | i2i |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | i2ip |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | f2ip |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | shfl |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | vote |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | match |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | redux |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | s2r |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fe200078e0002` | cs2r |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fe200078e0002` | globaltimer |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | s2r_ctaid |
| `IMAD.WIDE.U32 R4, R5, 0x400, R2` | `0000040005047825 001fc800078e0002` | s2ur |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | movm |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | lds_sts |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ld_generic |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | st_generic |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ldg_hints |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ldg_l2_128b |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ldg_v2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ldg_nc |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | stg_v4 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | ldl_stl |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ldc |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | cp_async |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ldsm |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | ldsm_trans |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | atomg |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | red |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | atoms |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | atom_generic |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | atom_v2_f32 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | red_v2_f32 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | atom_cas |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | atom_add_f32 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | qspc |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fcc00078e0002` | cctl |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fe200078e0002` | elect_sync |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | stmatrix |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | stmatrix_x4 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | mapa |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | cluster_ctarank |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | cluster_barrier |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fence_cluster |
| `IMAD.WIDE.U32 R16, R3, 0x40, R16` | `0000004003107825 004fe200078e0010` | cp_async_bulk_tma |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 004fd600078e0002` | mbarrier_red |
| `IMAD.WIDE.U32 R2, R7, 0x40, R2` | `0000004007027825 002fe200078e0002` | st_bulk |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 003fd600078e0002` | cp_async_bulk_prefetch |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | griddepcontrol |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | st_async |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hmma_f16 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hmma_bf16 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | hmma_tf32 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | imma |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | dmma |
| `IMAD.WIDE.U32 R16, R3, 0x40, R16` | `0000004003107825 002fca00078e0010` | bmma |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | qmma_e4m3 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | qmma_e5m2 |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | bar |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | bar_red |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | membar |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | fence_sys |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fcc00078e0002` | nanosleep |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fcc00078e0002` | warpsync |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | diverge |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | call |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | brx |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fc800078e0002` | uniform_loop |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | prologue |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | bssy_bsync |
| `IMAD.WIDE.U32 R2, R7, 0x40, R2` | `0000004007027825 004fe200078e0002` | agg_atomic |
| `IMAD.WIDE.U32 R2, R7, 0x40, R2` | `0000004007027825 001fca00078e0002` | activemask |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fc800078e0002` | s2ur_loop |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | uniform_alu |
| `IMAD.WIDE.U32 R2, R7, 0x40, R2` | `0000004007027825 008fca00078e0002` | uniform_txq |
| `IMAD.WIDE.U32 R4, R3, 0x40, R4` | `0000004003047825 002fca00078e0004` | cctll |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 002fca00078e0002` | plop3_folded |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | tex |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | tld4 |
| `IMAD.WIDE.U32 R2, R7, 0x40, R2` | `0000004007027825 001fca00078e0002` | txq |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | suld |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | tld |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | txd |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | sured |
| `IMAD.WIDE.U32 R2, R7, 0x40, R2` | `0000004007027825 001fca00078e0002` | suq |
| `IMAD.WIDE.U32 R2, R5, 0x40, R2` | `0000004005027825 001fca00078e0002` | sust |

### `IMAD R, R, IMM, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD R3, R7, 0x800000, R3` | `0080000007037824 000fce00078e0203` | fdiv_rn |
| `IMAD R6, R6, 0x4, R1` | `0000000406067824 000fc600078e0201` | ldl_stl |

### `IMAD R, R, R, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD R5, R0, R5, R4` | `0000000500057224 004fca00078e0204` | imad |
| `IMAD R7, R0, R0, RZ` | `0000000000077224 000fe400078e02ff` | call |

### `IMAD R, R.reuse, -IMM, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD R0, R6.reuse, -0x800000, R8` | `ff80000006007824 040fe200078e0208` | fdiv_rn |

### `IMAD.WIDE R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD.WIDE R4, R4, R5, RZ` | `0000000504047225 004fca00078e02ff` | imad_wide |

### `IMAD.HI.U32 R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD.HI.U32 R5, R0, R5, RZ` | `0000000500057227 004fca00078e00ff` | imad_hi |

### `IMAD R, R, IMM, R.reuse` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD R5, R0, 0x4, R1.reuse` | `0000000400057824 100fe400078e0201` | ldl_stl |

### `IMAD.SHL.U32 R, R, IMM, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMAD.SHL.U32 R0, R0, 0x4, RZ` | `0000000400007824 000fc800078e00ff` | brx |


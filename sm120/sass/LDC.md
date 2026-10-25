# LDC (SM120 SASS)

**NVIDIA:** Load Constant (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: constant-bank load; on sm_120 also the plain register-init form: prologue 'LDC R1, c[0x0][0x37c]' where sm89 used MOV (category: Load / store)

Observed on sm_120: 302 instruction(s) across 149 probe(s).

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
- `agg_red`: `red.global.add.u32 to a warp-uniform address (warp-aggregated)`
- `activemask`: `activemask.b32`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`
- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`
- `uniform_txq`: `txq.num_mipmap_levels (handle arithmetic on uniform datapath)`
- `cctll`: `prefetch.local.L1`
- `pmtrig`: `pmevent`
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

12-bit opcode field (bits 0-11) values observed: `0x41d`.

## Encoding observations

**Constant bits across all 302 observed instance(s): 97 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0100000111011110...0.000........00000000........000000...0000000
000000000.0100000000000000000000000000000....1...111000000000000
```

4 normalized operand form(s) observed:

### `LDC.IMM R, c[][]` - 150 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fadd |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ffma |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fmul |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fminmax |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fminmax_nan |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fminmax_xorsign |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fsetp_selp |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | selp_to_predicated_load |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fset |
| `LDC.64 R4, c[0x0][0x380]` | `0000e000ff047b82 000e620000000a00` | fdiv_rn |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_rcp |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_rsqrt |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_sqrt |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_lg2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_ex2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_sin |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_cos |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mufu_tanh |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | frnd |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | dadd |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | dfma |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | dmul |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | dsetp |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hadd2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hfma2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hfma2_bf16 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hmul2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hmnmx2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hsetp2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hset2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | iadd |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | iadd64 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | imad |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | imad_wide |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | imad_hi |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | iabs |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | imnmx |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | isetp_pred |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | imnmx_from_selp |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | lea |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | lea64 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | lop3 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | shf |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | shl64 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | prmt |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | sgxt |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | bmsk |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | flo |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | brev |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | popc |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | idp |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | vabsdiff |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | vabsdiff2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | vabsdiff4 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | f2f |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | f2i |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | i2fp |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | i2f |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | f2fp_f16 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | f2fp_bf16 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | f2fp_e4m3 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | cvt_e4m3_to_f16x2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | i2i |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | i2ip |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | f2ip |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | shfl |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | vote |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | match |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | redux |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | s2r |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | cs2r |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | globaltimer |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | s2r_ctaid |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | s2ur |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | movm |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | lds_sts |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ld_generic |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | st_generic |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ldg_hints |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ldg_l2_128b |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ldg_v2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ldg_nc |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | stg_v4 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | ldl_stl |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ldc |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | cp_async |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ldsm |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | ldsm_trans |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | atomg |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | red |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | atoms |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | atom_generic |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | atom_v2_f32 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | red_v2_f32 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | atom_cas |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | atom_add_f32 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | qspc |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | cctl |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | elect_sync |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | stmatrix |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | stmatrix_x4 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | mapa |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | cluster_ctarank |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | cluster_barrier |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fence_cluster |
| `LDC.64 R16, c[0x0][0x380]` | `0000e000ff107b82 000ea20000000a00` | cp_async_bulk_tma |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000ea20000000a00` | mbarrier_red |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | st_bulk |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | cp_async_bulk_prefetch |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | griddepcontrol |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | st_async |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hmma_f16 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hmma_bf16 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | hmma_tf32 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | imma |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | dmma |
| `LDC.64 R16, c[0x0][0x380]` | `0000e000ff107b82 000e620000000a00` | bmma |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | qmma_e4m3 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | qmma_e5m2 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | bar |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | bar_red |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | membar |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | fence_sys |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | nanosleep |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | warpsync |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | diverge |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | call |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | brx |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | uniform_loop |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | prologue |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | bssy_bsync |
| `LDC.64 R4, c[0x0][0x380]` | `0000e000ff047b82 000e620000000a00` | agg_atomic |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | agg_red |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | activemask |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | s2ur_loop |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | uniform_alu |
| `LDC.64 R4, c[0x0][0x150]` | `00005400ff047b82 000e620000000a00` | uniform_txq |
| `LDC.64 R4, c[0x0][0x380]` | `0000e000ff047b82 000e620000000a00` | cctll |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e620000000a00` | plop3_folded |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | tex |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | tld4 |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | txq |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | suld |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | tld |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | txd |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | sured |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | suq |
| `LDC.64 R2, c[0x0][0x380]` | `0000e000ff027b82 000e220000000a00` | sust |

### `LDC R, c[][]` - 149 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fadd |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ffma |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fmul |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fminmax |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fminmax_nan |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fminmax_xorsign |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fsetp_selp |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | selp_to_predicated_load |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fset |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | fdiv_rn |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_rcp |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_rsqrt |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_sqrt |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_lg2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_ex2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_sin |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_cos |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mufu_tanh |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | frnd |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | dadd |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | dfma |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | dmul |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | dsetp |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hadd2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hfma2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hfma2_bf16 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hmul2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hmnmx2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hsetp2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hset2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | iadd |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | iadd64 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | imad |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | imad_wide |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | imad_hi |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | iabs |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | imnmx |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | isetp_pred |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | imnmx_from_selp |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | lea |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | lea64 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | lop3 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | shf |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | shl64 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | prmt |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | sgxt |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | bmsk |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | flo |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | brev |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | popc |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | idp |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | vabsdiff |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | vabsdiff2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | vabsdiff4 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | f2f |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | f2i |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | i2fp |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | i2f |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | f2fp_f16 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | f2fp_bf16 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | f2fp_e4m3 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | cvt_e4m3_to_f16x2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | i2i |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | i2ip |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | f2ip |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | shfl |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | vote |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | match |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | redux |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | s2r |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | cs2r |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | globaltimer |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | s2r_ctaid |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | s2ur |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | movm |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | lds_sts |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ld_generic |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | st_generic |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ldg_hints |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ldg_l2_128b |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ldg_v2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ldg_nc |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | stg_v4 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | ldl_stl |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ldc |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | cp_async |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ldsm |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | ldsm_trans |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | atomg |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | red |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | atoms |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | atom_generic |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | atom_v2_f32 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | red_v2_f32 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | atom_cas |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | atom_add_f32 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | qspc |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | cctl |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | elect_sync |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | stmatrix |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | stmatrix_x4 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | mapa |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | cluster_ctarank |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | cluster_barrier |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fence_cluster |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e300000000800` | cp_async_bulk_tma |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e300000000800` | mbarrier_red |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000ff00000000800` | st_bulk |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | cp_async_bulk_prefetch |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | griddepcontrol |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | st_async |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hmma_f16 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hmma_bf16 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | hmma_tf32 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | imma |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | dmma |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | bmma |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | qmma_e4m3 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | qmma_e5m2 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | bar |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | bar_red |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | membar |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | fence_sys |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | nanosleep |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | warpsync |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | diverge |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | call |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | brx |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | uniform_loop |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | prologue |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | bssy_bsync |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | agg_atomic |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | agg_red |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | activemask |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | s2ur_loop |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | uniform_alu |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | uniform_txq |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | cctll |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | pmtrig |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000e220000000800` | plop3_folded |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | tex |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | tld4 |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | txq |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | suld |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | tld |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | txd |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | sured |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | suq |
| `LDC R1, c[0x0][0x37c]` | `0000df00ff017b82 000fe20000000800` | sust |

### `LDC R, c[IMM][R]` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDC R5, c[0x3][R0]` | `00c0000000057b82 000e240000000800` | ldc |
| `LDC R4, c[0x2][R0]` | `0080000000047b82 000e640000000800` | brx |

### `LDC.IMM R, c[IMM][R]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDC.64 R2, c[0x4][R2]` | `0100000002027b82 000e220000000a00` | cp_async_bulk_tma |


# LDCU (SM120 SASS)

**NVIDIA:** Load a Value from Constant Memory into a Uniform Register (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform load from constant bank (c[0x0][...] kernel params); sm_120 name for sm89's ULDC (category: Uniform datapath)

Observed on sm_120: 160 instruction(s) across 147 probe(s).

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

12-bit opcode field (bits 0-11) values observed: `0x35e`.

## Encoding observations

**Constant bits across all 160 observed instance(s): 111 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0011010111101110....0.00111111110000000.1....1100000000000000000
000000000.0100000000000000010000000000000...01..0111.00000000000
```

2 normalized operand form(s) observed:

### `LDCU.IMM UR, c[][]` - 147 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fadd |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | ffma |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fmul |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fminmax |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fminmax_nan |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fminmax_xorsign |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fsetp_selp |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | selp_to_predicated_load |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fset |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | fdiv_rn |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_rcp |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_rsqrt |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_sqrt |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_lg2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_ex2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_sin |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_cos |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mufu_tanh |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | frnd |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | dadd |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | dfma |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | dmul |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | dsetp |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hadd2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hfma2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hfma2_bf16 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hmul2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hmnmx2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hsetp2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hset2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | iadd |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | iadd64 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | imad |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | imad_wide |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | imad_hi |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | iabs |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | imnmx |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | isetp_pred |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | imnmx_from_selp |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | lea |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | lea64 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | lop3 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | shf |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | shl64 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | prmt |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | sgxt |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | bmsk |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | flo |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | brev |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | popc |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | idp |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | vabsdiff |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | vabsdiff2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | vabsdiff4 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | f2f |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | f2i |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | i2fp |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | i2f |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | f2fp_f16 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | f2fp_bf16 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | f2fp_e4m3 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | cvt_e4m3_to_f16x2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | i2i |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | i2ip |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | f2ip |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | shfl |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | vote |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | match |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | redux |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | s2r |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | cs2r |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | globaltimer |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | s2r_ctaid |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | s2ur |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | movm |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | lds_sts |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | ld_generic |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | st_generic |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | ldg_hints |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | ldg_l2_128b |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | ldg_v2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | ldg_nc |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | stg_v4 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | ldl_stl |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | ldc |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000ee20008000a00` | cp_async |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | ldsm |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | ldsm_trans |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | atomg |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | red |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000ea20008000a00` | atoms |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | atom_generic |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | atom_v2_f32 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | red_v2_f32 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | atom_cas |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | atom_add_f32 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | qspc |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | cctl |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | elect_sync |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | stmatrix |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | stmatrix_x4 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | mapa |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | cluster_ctarank |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | cluster_barrier |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fence_cluster |
| `LDCU.64 UR36, c[0x0][0x358]` | `00006b00ff2477ac 000ee20008000a00` | cp_async_bulk_tma |
| `LDCU.64 UR8, c[0x0][0x358]` | `00006b00ff0877ac 000e220008000a00` | mbarrier_red |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 001e660008000a00` | st_bulk |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | griddepcontrol |
| `LDCU.64 UR10, c[0x0][0x358]` | `00006b00ff0a77ac 000e620008000a00` | st_async |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hmma_f16 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hmma_bf16 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | hmma_tf32 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | imma |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | dmma |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | bmma |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | qmma_e4m3 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | qmma_e5m2 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | bar |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | bar_red |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | membar |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | fence_sys |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | nanosleep |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | warpsync |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | diverge |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | call |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | brx |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ee20008000a00` | uniform_loop |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | prologue |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | bssy_bsync |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | agg_atomic |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | agg_red |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | activemask |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000eee0008000a00` | s2ur_loop |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | uniform_alu |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000ea20008000a00` | uniform_txq |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | cctll |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000ea20008000a00` | plop3_folded |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | tex |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | tld4 |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | txq |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | suld |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | tld |
| `LDCU.64 UR6, c[0x0][0x358]` | `00006b00ff0677ac 000e620008000a00` | txd |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | sured |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | suq |
| `LDCU.64 UR4, c[0x0][0x358]` | `00006b00ff0477ac 000e620008000a00` | sust |

### `LDCU UR, c[][]` - 13 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDCU UR6, c[0x0][0x36c]` | `00006d80ff0677ac 000ea40008000800` | cluster_barrier |
| `LDCU UR7, c[0x0][0x388]` | `00007100ff0777ac 000eac0008000800` | uniform_loop |
| `LDCU UR5, c[0x0][0x388]` | `00007100ff0577ac 000ea20008000800` | uniform_alu |
| `LDCU UR5, c[0x0][0x388]` | `00007100ff0577ac 000e2e0008000800` | uniform_txq |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000ea20008000800` | tex |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000ea20008000800` | tld4 |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000e220008000800` | txq |
| `LDCU UR6, c[0x0][0x388]` | `00007100ff0677ac 000ea40008000800` | suld |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000ea20008000800` | tld |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000e220008000800` | txd |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000ea40008000800` | sured |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000e220008000800` | suq |
| `LDCU UR4, c[0x0][0x388]` | `00007100ff0477ac 000ea40008000800` | sust |


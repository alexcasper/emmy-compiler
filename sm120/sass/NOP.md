# NOP (SM120 SASS)

**NVIDIA:** No Operation (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: padding / alignment filler (category: Control flow)

Observed on sm_120: 1879 instruction(s) across 149 probe(s).

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

12-bit opcode field (bits 0-11) values observed: `0x189`.

## Encoding observations

**Constant bits across all 1879 observed instance(s): 123 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0001100010011110000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000.....111111000000000000
```

1 normalized operand form(s) observed:

### `NOP` - 1879 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `NOP` | `0000000000007918 000fc00000000000` | fadd |
| `NOP` | `0000000000007918 000fc00000000000` | fadd |
| `NOP` | `0000000000007918 000fc00000000000` | fadd |
| `NOP` | `0000000000007918 000fc00000000000` | ffma |
| `NOP` | `0000000000007918 000fc00000000000` | fmul |
| `NOP` | `0000000000007918 000fc00000000000` | fminmax |
| `NOP` | `0000000000007918 000fc00000000000` | fminmax_nan |
| `NOP` | `0000000000007918 000fc00000000000` | fminmax_xorsign |
| `NOP` | `0000000000007918 000fc00000000000` | fsetp_selp |
| `NOP` | `0000000000007918 000fc00000000000` | selp_to_predicated_load |
| `NOP` | `0000000000007918 000fc00000000000` | fset |
| `NOP` | `0000000000007918 000fc00000000000` | fdiv_rn |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_rcp |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_rsqrt |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_sqrt |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_lg2 |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_ex2 |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_sin |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_cos |
| `NOP` | `0000000000007918 000fc00000000000` | mufu_tanh |
| `NOP` | `0000000000007918 000fc00000000000` | frnd |
| `NOP` | `0000000000007918 000fc00000000000` | dadd |
| `NOP` | `0000000000007918 000fc00000000000` | dfma |
| `NOP` | `0000000000007918 000fc00000000000` | dmul |
| `NOP` | `0000000000007918 000fc00000000000` | dsetp |
| `NOP` | `0000000000007918 000fc00000000000` | hadd2 |
| `NOP` | `0000000000007918 000fc00000000000` | hfma2 |
| `NOP` | `0000000000007918 000fc00000000000` | hfma2_bf16 |
| `NOP` | `0000000000007918 000fc00000000000` | hmul2 |
| `NOP` | `0000000000007918 000fc00000000000` | hmnmx2 |
| `NOP` | `0000000000007918 000fc00000000000` | hsetp2 |
| `NOP` | `0000000000007918 000fc00000000000` | hset2 |
| `NOP` | `0000000000007918 000fc00000000000` | iadd |
| `NOP` | `0000000000007918 000fc00000000000` | iadd64 |
| `NOP` | `0000000000007918 000fc00000000000` | imad |
| `NOP` | `0000000000007918 000fc00000000000` | imad_wide |
| `NOP` | `0000000000007918 000fc00000000000` | imad_hi |
| `NOP` | `0000000000007918 000fc00000000000` | iabs |
| `NOP` | `0000000000007918 000fc00000000000` | imnmx |
| `NOP` | `0000000000007918 000fc00000000000` | isetp_pred |
| `NOP` | `0000000000007918 000fc00000000000` | imnmx_from_selp |
| `NOP` | `0000000000007918 000fc00000000000` | lea |
| `NOP` | `0000000000007918 000fc00000000000` | lea64 |
| `NOP` | `0000000000007918 000fc00000000000` | lop3 |
| `NOP` | `0000000000007918 000fc00000000000` | shf |
| `NOP` | `0000000000007918 000fc00000000000` | shl64 |
| `NOP` | `0000000000007918 000fc00000000000` | prmt |
| `NOP` | `0000000000007918 000fc00000000000` | sgxt |
| `NOP` | `0000000000007918 000fc00000000000` | bmsk |
| `NOP` | `0000000000007918 000fc00000000000` | flo |
| `NOP` | `0000000000007918 000fc00000000000` | brev |
| `NOP` | `0000000000007918 000fc00000000000` | popc |
| `NOP` | `0000000000007918 000fc00000000000` | idp |
| `NOP` | `0000000000007918 000fc00000000000` | vabsdiff |
| `NOP` | `0000000000007918 000fc00000000000` | vabsdiff2 |
| `NOP` | `0000000000007918 000fc00000000000` | vabsdiff4 |
| `NOP` | `0000000000007918 000fc00000000000` | f2f |
| `NOP` | `0000000000007918 000fc00000000000` | f2i |
| `NOP` | `0000000000007918 000fc00000000000` | i2fp |
| `NOP` | `0000000000007918 000fc00000000000` | i2f |
| `NOP` | `0000000000007918 000fc00000000000` | f2fp_f16 |
| `NOP` | `0000000000007918 000fc00000000000` | f2fp_bf16 |
| `NOP` | `0000000000007918 000fc00000000000` | f2fp_e4m3 |
| `NOP` | `0000000000007918 000fc00000000000` | cvt_e4m3_to_f16x2 |
| `NOP` | `0000000000007918 000fc00000000000` | i2i |
| `NOP` | `0000000000007918 000fc00000000000` | i2ip |
| `NOP` | `0000000000007918 000fc00000000000` | f2ip |
| `NOP` | `0000000000007918 000fc00000000000` | shfl |
| `NOP` | `0000000000007918 000fc00000000000` | vote |
| `NOP` | `0000000000007918 000fc00000000000` | match |
| `NOP` | `0000000000007918 000fc00000000000` | redux |
| `NOP` | `0000000000007918 000fc00000000000` | s2r |
| `NOP` | `0000000000007918 000fc00000000000` | cs2r |
| `NOP` | `0000000000007918 000fc00000000000` | globaltimer |
| `NOP` | `0000000000007918 000fc00000000000` | s2r_ctaid |
| `NOP` | `0000000000007918 000fc00000000000` | s2ur |
| `NOP` | `0000000000007918 000fc00000000000` | movm |
| `NOP` | `0000000000007918 000fc00000000000` | lds_sts |
| `NOP` | `0000000000007918 000fc00000000000` | ld_generic |
| `NOP` | `0000000000007918 000fc00000000000` | st_generic |
| `NOP` | `0000000000007918 000fc00000000000` | ldg_hints |
| `NOP` | `0000000000007918 000fc00000000000` | ldg_l2_128b |
| `NOP` | `0000000000007918 000fc00000000000` | ldg_v2 |
| `NOP` | `0000000000007918 000fc00000000000` | ldg_nc |
| `NOP` | `0000000000007918 000fc00000000000` | stg_v4 |
| `NOP` | `0000000000007918 000fc00000000000` | ldl_stl |
| `NOP` | `0000000000007918 000fc00000000000` | ldc |
| `NOP` | `0000000000007918 000fc00000000000` | cp_async |
| `NOP` | `0000000000007918 000fc00000000000` | ldsm |
| `NOP` | `0000000000007918 000fc00000000000` | ldsm_trans |
| `NOP` | `0000000000007918 000fc00000000000` | atomg |
| `NOP` | `0000000000007918 000fc00000000000` | red |
| `NOP` | `0000000000007918 000fc00000000000` | atoms |
| `NOP` | `0000000000007918 000fc00000000000` | atom_generic |
| `NOP` | `0000000000007918 000fc00000000000` | atom_v2_f32 |
| `NOP` | `0000000000007918 000fc00000000000` | red_v2_f32 |
| `NOP` | `0000000000007918 000fc00000000000` | atom_cas |
| `NOP` | `0000000000007918 000fc00000000000` | atom_add_f32 |
| `NOP` | `0000000000007918 000fc00000000000` | qspc |
| `NOP` | `0000000000007918 000fc00000000000` | cctl |
| `NOP` | `0000000000007918 000fc00000000000` | elect_sync |
| `NOP` | `0000000000007918 000fc00000000000` | stmatrix |
| `NOP` | `0000000000007918 000fc00000000000` | stmatrix_x4 |
| `NOP` | `0000000000007918 000fc00000000000` | mapa |
| `NOP` | `0000000000007918 000fc00000000000` | cluster_ctarank |
| `NOP` | `0000000000007918 000fe20000000000` | cluster_barrier |
| `NOP` | `0000000000007918 000fc00000000000` | fence_cluster |
| `NOP` | `0000000000007918 000fc00000000000` | cp_async_bulk_tma |
| `NOP` | `0000000000007918 000fc00000000000` | mbarrier_red |
| `NOP` | `0000000000007918 000fc00000000000` | st_bulk |
| `NOP` | `0000000000007918 000fc00000000000` | cp_async_bulk_prefetch |
| `NOP` | `0000000000007918 000fc00000000000` | griddepcontrol |
| `NOP` | `0000000000007918 000fc00000000000` | st_async |
| `NOP` | `0000000000007918 000fda0000000000` | hmma_f16 |
| `NOP` | `0000000000007918 000fda0000000000` | hmma_bf16 |
| `NOP` | `0000000000007918 000fda0000000000` | hmma_tf32 |
| `NOP` | `0000000000007918 000fd60000000000` | imma |
| `NOP` | `0000000000007918 000fdc0000000000` | dmma |
| `NOP` | `0000000000007918 000fd60000000000` | bmma |
| `NOP` | `0000000000007918 000fda0000000000` | qmma_e4m3 |
| `NOP` | `0000000000007918 000fda0000000000` | qmma_e5m2 |
| `NOP` | `0000000000007918 000fc00000000000` | bar |
| `NOP` | `0000000000007918 000fc00000000000` | bar_red |
| `NOP` | `0000000000007918 000fc00000000000` | membar |
| `NOP` | `0000000000007918 000fc00000000000` | fence_sys |
| `NOP` | `0000000000007918 000fc00000000000` | nanosleep |
| `NOP` | `0000000000007918 000fe20000000000` | warpsync |
| `NOP` | `0000000000007918 000fc00000000000` | diverge |
| `NOP` | `0000000000007918 000fc00000000000` | call |
| `NOP` | `0000000000007918 000fc00000000000` | brx |
| `NOP` | `0000000000007918 000fc00000000000` | uniform_loop |
| `NOP` | `0000000000007918 000fc00000000000` | prologue |
| `NOP` | `0000000000007918 000fc00000000000` | bssy_bsync |
| `NOP` | `0000000000007918 000fc00000000000` | agg_atomic |
| `NOP` | `0000000000007918 000fc00000000000` | agg_red |
| `NOP` | `0000000000007918 000fc00000000000` | activemask |
| `NOP` | `0000000000007918 000fc00000000000` | s2ur_loop |
| `NOP` | `0000000000007918 000fc00000000000` | uniform_alu |
| `NOP` | `0000000000007918 000fc00000000000` | uniform_txq |
| `NOP` | `0000000000007918 000fc00000000000` | cctll |
| `NOP` | `0000000000007918 000fc00000000000` | pmtrig |
| `NOP` | `0000000000007918 000fc00000000000` | plop3_folded |
| `NOP` | `0000000000007918 000fc00000000000` | tex |
| `NOP` | `0000000000007918 000fc00000000000` | tld4 |
| `NOP` | `0000000000007918 000fc00000000000` | txq |
| `NOP` | `0000000000007918 000fc00000000000` | suld |
| `NOP` | `0000000000007918 000fc00000000000` | tld |
| `NOP` | `0000000000007918 000fc00000000000` | txd |
| `NOP` | `0000000000007918 000fc00000000000` | sured |
| `NOP` | `0000000000007918 000fc00000000000` | suq |
| `NOP` | `0000000000007918 000fc00000000000` | sust |


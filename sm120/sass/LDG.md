# LDG (SM120 SASS)

**NVIDIA:** Load from Global Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: global load, .E/.E.64/.E.128 widths, desc[UR4] descriptor addressing (category: Load / store)

Observed on sm_120: 258 instruction(s) across 132 probe(s).

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
- `stmatrix`: `stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)`
- `stmatrix_x4`: `stmatrix.sync.aligned.m8n8.x4.shared.b16`
- `mapa`: `mapa.u64 (cluster address mapping, sm_90+)`
- `cluster_barrier`: `barrier.cluster.arrive/wait.aligned`
- `fence_cluster`: `fence.acq_rel.cluster`
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
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`
- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`
- `uniform_txq`: `txq.num_mipmap_levels (handle arithmetic on uniform datapath)`
- `cctll`: `prefetch.local.L1`
- `plop3_folded`: `xor.pred of two compares (folded into ISETP/FSETP combine op)`
- `tex`: `tex.2d.v4.f32.f32`
- `tld4`: `tld4.r.2d.v4.f32.f32`
- `suld`: `suld.b.2d.b32.trap`
- `tld`: `tex.1d.v4.s32.s32 (integer coords)`
- `txd`: `tex.grad.2d.v4.f32.f32`
- `sured`: `sured.b.add.2d.u32.trap`
- `sust`: `sust.b.2d.b32.trap`

12-bit opcode field (bits 0-11) values observed: `0x819`.

## Encoding observations

**Constant bits across all 258 observed instance(s): 94 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
100000011001...0....00000..0.0000...000000....000000000000000000
00000.001.01100.0111..0000110000000000000...01.........000000000
```

8 normalized operand form(s) observed:

### `LDG.E R, desc[UR][R.IMM+IMM]` - 144 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | fadd |
| `LDG.E R5, desc[UR4][R2.64+0x10]` | `0000100402057981 000ea4000c1e1900` | fadd |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | ffma |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | fmul |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | fminmax |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | fminmax_nan |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | fminmax_xorsign |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | fsetp_selp |
| `LDG.E R5, desc[UR4][R2.64+0xc]` | `00000c0402057981 002ea8000c1e1900` | selp_to_predicated_load |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | fset |
| `LDG.E R3, desc[UR4][R4.64+0x10]` | `0000100404037981 004ea8000c1e1900` | fdiv_rn |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea2000c1e1900` | mufu_rcp |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | mufu_rsqrt |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | mufu_sqrt |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | mufu_lg2 |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | mufu_ex2 |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | mufu_sin |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | mufu_cos |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | mufu_tanh |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | frnd |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | hadd2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | hfma2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | hfma2_bf16 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | hmul2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | hmnmx2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | hsetp2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | hset2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | iadd |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | imad |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | imad_hi |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | imnmx |
| `LDG.E R7, desc[UR4][R2.64+0x8]` | `0000080402077981 000ea8000c1e1900` | isetp_pred |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | imnmx_from_selp |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | lea |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | lop3 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | shf |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | prmt |
| `LDG.E R4, desc[UR4][R2.64+0x4]` | `0000040402047981 002ea8000c1e1900` | sgxt |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea4000c1e1900` | bmsk |
| `LDG.E R4, desc[UR4][R2.64+0x4]` | `0000040402047981 000ee2000c1e1900` | flo |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | idp |
| `LDG.E R6, desc[UR4][R2.64+0x4]` | `0000040402067981 000ee2000c1e1900` | vabsdiff |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ee8000c1e1900` | vabsdiff2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | vabsdiff4 |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | f2i |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | f2fp_f16 |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | f2fp_bf16 |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | f2fp_e4m3 |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea8000c1e1900` | cvt_e4m3_to_f16x2 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | i2ip |
| `LDG.E R0, desc[UR4][R2.64+0xc]` | `00000c0402007981 002ea4000c1e1900` | f2ip |
| `LDG.E R4, desc[UR4][R2.64+0xc]` | `00000c0402047981 000ee2000c1e1900` | stg_v4 |
| `LDG.E R5, desc[UR4][R2.64+0x8]` | `0000080402057981 000ee8000c1e1900` | ldl_stl |
| `LDG.E R4, desc[UR4][R2.64+0xc]` | `00000c0402047981 002ea8000c1e1900` | atom_v2_f32 |
| `LDG.E R4, desc[UR4][R2.64+0xc]` | `00000c0402047981 002ea8000c1e1900` | red_v2_f32 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | atom_cas |
| `LDG.E R5, desc[UR4][R2.64+0xc]` | `00000c0402057981 002ea8000c1e1900` | atom_add_f32 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea8000c1e1900` | stmatrix_x4 |
| `LDG.E R7, desc[UR4][R2.64+0x4]` | `0000040402077981 000ee8000c1e1900` | fence_cluster |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 002ea8000c1e1900` | hmma_f16 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 002ea8000c1e1900` | hmma_bf16 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 002ea8000c1e1900` | hmma_tf32 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 002ea8000c1e1900` | imma |
| `LDG.E R13, desc[UR4][R16.64+0x4]` | `00000404100d7981 000368000c1e1900` | bmma |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 002ea8000c1e1900` | qmma_e4m3 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 002ea8000c1e1900` | qmma_e5m2 |
| `LDG.E R7, desc[UR4][R2.64+0x4]` | `0000040402077981 000ea8000c1e1900` | bar |
| `LDG.E R7, desc[UR4][R2.64+0x4]` | `0000040402077981 000ee8000c1e1900` | membar |
| `LDG.E R7, desc[UR4][R2.64+0x4]` | `0000040402077981 000ee8000c1e1900` | fence_sys |
| `LDG.E R2, desc[UR4][R4.64+0x4]` | `0000040404027981 004ea8000c1e1900` | cctll |
| `LDG.E R4, desc[UR4][R2.64+0xc]` | `00000c0402047981 004ea8000c1e1900` | plop3_folded |
| `LDG.E R4, desc[UR6][R2.64+0xc]` | `00000c0602047981 002ea8000c1e1900` | tex |
| `LDG.E R4, desc[UR6][R2.64+0xc]` | `00000c0602047981 002ea8000c1e1900` | tld4 |
| `LDG.E R5, desc[UR4][R2.64+0x4]` | `0000040402057981 000ea2000c1e1900` | suld |
| `LDG.E R4, desc[UR6][R2.64+0xc]` | `00000c0602047981 002ea8000c1e1900` | txd |
| `LDG.E R0, desc[UR4][R2.64+0x8]` | `0000080402007981 002ea8000c1e1900` | sured |
| `LDG.E R0, desc[UR4][R2.64+0x8]` | `0000080402007981 002ea8000c1e1900` | sust |

### `LDG.E R, desc[UR][R.IMM]` - 84 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | hadd2 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | hfma2 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | hfma2_bf16 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | hmul2 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | hmnmx2 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | hsetp2 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | hset2 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | iadd |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | imad |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | imad_hi |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | iabs |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | imnmx |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | isetp_pred |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | imnmx_from_selp |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | lea |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | lop3 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | shf |
| `LDG.E R7, desc[UR4][R2.64]` | `0000000402077981 002ea8000c1e1900` | shl64 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | prmt |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 000ee2000c1e1900` | sgxt |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | bmsk |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | flo |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | brev |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | popc |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | idp |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 002ea8000c1e1900` | vabsdiff |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | vabsdiff2 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | vabsdiff4 |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | i2fp |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 002ea4000c1e1900` | i2f |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | i2i |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | i2ip |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | shfl |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | vote |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | match |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | redux |
| `LDG.E R5, desc[UR4][R4.64]` | `0000000404057981 002ea8000c1e1900` | s2ur |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea8000c1e1900` | movm |
| `LDG.E R0, desc[UR6][R2.64]` | `0000000602007981 002ea2000c1e1900` | lds_sts |
| `LDG.E R7, desc[UR4][R2.64]` | `0000000402077981 002ea8000c1e1900` | st_generic |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 004ea8000c1e1900` | ldl_stl |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | ldc |
| `LDG.E R0, desc[UR6][R2.64]` | `0000000602007981 002ea2000c1e1900` | ldsm |
| `LDG.E R0, desc[UR6][R2.64]` | `0000000602007981 002ea2000c1e1900` | ldsm_trans |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1900` | atomg |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1900` | red |
| `LDG.E R0, desc[UR6][R2.64]` | `0000000602007981 004ea2000c1e1900` | atoms |
| `LDG.E R7, desc[UR4][R2.64]` | `0000000402077981 002ea8000c1e1900` | atom_generic |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 002ea8000c1e1900` | atom_cas |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea2000c1e1900` | stmatrix |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 002ea8000c1e1900` | stmatrix_x4 |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 004362000c1e1900` | cluster_barrier |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1900` | fence_cluster |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea2000c1e1900` | griddepcontrol |
| `LDG.E R0, desc[UR10][R2.64]` | `0000000a02007981 002ea2000c1e1900` | st_async |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000f28000c1e1900` | hmma_f16 |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000f28000c1e1900` | hmma_bf16 |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000f28000c1e1900` | hmma_tf32 |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000f22000c1e1900` | imma |
| `LDG.E R12, desc[UR4][R16.64]` | `00000004100c7981 004368000c1e1900` | bmma |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000f28000c1e1900` | qmma_e4m3 |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000f28000c1e1900` | qmma_e5m2 |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1900` | bar |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 002ea4000c1e1900` | bar_red |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1900` | membar |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1900` | fence_sys |
| `LDG.E R2, desc[UR4][R2.64]` | `0000000402027981 002ea4000c1e1900` | nanosleep |
| `LDG.E R2, desc[UR4][R2.64]` | `0000000402027981 005364000c1e1900` | warpsync |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 004ea2000c1e1900` | diverge |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 004362000c1e1900` | call |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 004ea2000c1e1900` | brx |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 000162000c1e1900` | uniform_loop |
| `LDG.E R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1900` | prologue |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 000362000c1e1900` | bssy_bsync |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 000ea2000c1e1900` | s2ur_loop |
| `LDG.E R0, desc[UR6][R2.64]` | `0000000602007981 002ee2000c1e1900` | uniform_alu |
| `LDG.E R0, desc[UR4][R4.64]` | `0000000404007981 000ee8000c1e1900` | cctll |
| `LDG.E R0, desc[UR4][R2.64]` | `0000000402007981 000ee8000c1e1900` | plop3_folded |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 002ea8000c1e1900` | suld |
| `LDG.E R0, desc[UR6][R2.64]` | `0000000602007981 002ea2000c1e1900` | tld |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000ea8000c1e1900` | sured |
| `LDG.E R4, desc[UR4][R2.64]` | `0000000402047981 000ea8000c1e1900` | sust |

### `LDG.E.IMM R, desc[UR][R.IMM+IMM]` - 23 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E.64 R4, desc[UR4][R2.64+0x18]` | `0000180402047981 002ea8000c1e1b00` | dadd |
| `LDG.E.64 R6, desc[UR4][R2.64+0x20]` | `0000200402067981 000ea4000c1e1b00` | dadd |
| `LDG.E.64 R4, desc[UR4][R2.64+0x18]` | `0000180402047981 002ea8000c1e1b00` | dfma |
| `LDG.E.64 R4, desc[UR4][R2.64+0x18]` | `0000180402047981 002ea8000c1e1b00` | dmul |
| `LDG.E.64 R4, desc[UR4][R2.64+0x18]` | `0000180402047981 002ea8000c1e1b00` | dsetp |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 002ea4000c1e1b00` | iadd64 |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 000ee2000c1e1b00` | lea64 |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 000ea4000c1e1b00` | shl64 |
| `LDG.E.64 R4, desc[UR4][R2.64+0x18]` | `0000180402047981 002ea4000c1e1b00` | f2f |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 002ea8000c1e1b00` | ld_generic |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 000ea8000c1e1b00` | st_generic |
| `LDG.E.64 R4, desc[UR4][R2.64+0x30]` | `0000300402047981 002ea4000c1e1b00` | ldg_v2 |
| `LDG.E.64 R8, desc[UR4][R2.64+0x10]` | `0000100402087981 002ea8000c1e1b00` | stg_v4 |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 000ea8000c1e1b00` | atom_generic |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 002ea8000c1e1b00` | qspc |
| `LDG.E.64 R2, desc[UR4][R2.64+0x28]` | `0000280402027981 002ea8000c1e1b00` | cctl |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 002ea2000c1e1b00` | mapa |
| `LDG.E.64 R4, desc[UR4][R2.64+0x18]` | `0000180402047981 002ea8000c1e1b00` | dmma |
| `LDG.E.64 R4, desc[UR4][R2.64+0x28]` | `0000280402047981 004ea8000c1e1b00` | bssy_bsync |

### `LDG.E.IMM R, desc[UR][R.IMM]` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E.64 R4, desc[UR4][R2.64]` | `0000000402047981 002ea4000c1e1b00` | imad_wide |
| `LDG.E.64 R6, desc[UR4][R2.64]` | `0000000402067981 002ea8000c1e1b00` | lea64 |

### `LDG.E.CONSTANT R, desc[UR][R.IMM+IMM]` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E.CONSTANT R0, desc[UR4][R2.64+0x30]` | `0000300402007981 002ea8000c1e9900` | ldg_nc |
| `LDG.E.CONSTANT R5, desc[UR4][R2.64+0x3c]` | `00003c0402057981 000ea4000c1e9900` | ldg_nc |

### `LDG.E.EL R, desc[UR][R.IMM]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E.EL R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c2e1900` | ldg_hints |

### `LDG.E.LTC128B R, desc[UR][R.IMM]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E.LTC128B R5, desc[UR4][R2.64]` | `0000000402057981 002ea8000c1e1920` | ldg_l2_128b |

### `LDG.E.CONSTANT R, desc[UR][R.IMM]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDG.E.CONSTANT R5, desc[UR6][R4.64]` | `0000000604057981 004ea2000c1e9900` | uniform_txq |


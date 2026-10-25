# PTX ISA instruction index (sm_120 view)

Generated from the frozen CUDA 12.9.1 archive <https://docs.nvidia.com/cuda/archive/12.9.1/parallel-thread-execution/index.html> (PTX ISA 8.8). The **sm_120** column is a heuristic over each section's "Target ISA Notes": `yes` = no requirement above sm_120, `partial` = some variants need a newer arch (read the notes), `no` = whole instruction needs a newer arch. Remember the PTX `.version` also matters: **sm_120 needs >= 8.7** (introduced in CUDA 12.8; this verified with `ptxas` 12.9 — `.version 8.5` + `.target sm_120` is rejected, 8.7 assembles).

Spot-checked with real `ptxas -arch=sm_120`: see [../verify/RESULTS.md](../verify/RESULTS.md) (the `no_*` probes are rejected for architecture reasons; the `yes` instructions compile in the other probes).

Non-instruction chapters: [01-introduction](01-introduction.md), [02-programming-model](02-programming-model.md), [03-ptx-machine-model](03-ptx-machine-model.md), [04-syntax](04-syntax.md), [05-state-spaces-types-and-variables](05-state-spaces-types-and-variables.md), [06-instruction-operands](06-instruction-operands.md), [07-abstracting-the-abi](07-abstracting-the-abi.md), [08-memory-consistency-model](08-memory-consistency-model.md), [09-instruction-set](09-instruction-set.md), [10-special-registers](10-special-registers.md), [11-directives](11-directives.md), [12-descriptions-of-pragma-strings](12-descriptions-of-pragma-strings.md), [13-release-notes](13-release-notes.md), [14-notices](14-notices.md)

## 9.7.1. Integer Arithmetic Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.1.1. | [`add`](instructions/01-integer-arithmetic-instructions/01-add.md) | yes | Supported on all target architectures. `add.u16x2` and `add.s16x2` require `sm_90` or higher. |
| 9.7.1.2. | [`sub`](instructions/01-integer-arithmetic-instructions/02-sub.md) | yes | Supported on all target architectures. |
| 9.7.1.3. | [`mul`](instructions/01-integer-arithmetic-instructions/03-mul.md) | yes | Supported on all target architectures. |
| 9.7.1.4. | [`mad`](instructions/01-integer-arithmetic-instructions/04-mad.md) | yes | Supported on all target architectures. |
| 9.7.1.5. | [`mul24`](instructions/01-integer-arithmetic-instructions/05-mul24.md) | yes | Supported on all target architectures. |
| 9.7.1.6. | [`mad24`](instructions/01-integer-arithmetic-instructions/06-mad24.md) | yes | Supported on all target architectures. |
| 9.7.1.7. | [`sad`](instructions/01-integer-arithmetic-instructions/07-sad.md) | yes | Supported on all target architectures. |
| 9.7.1.8. | [`div`](instructions/01-integer-arithmetic-instructions/08-div.md) | yes | Supported on all target architectures. |
| 9.7.1.9. | [`rem`](instructions/01-integer-arithmetic-instructions/09-rem.md) | yes | Supported on all target architectures. |
| 9.7.1.10. | [`abs`](instructions/01-integer-arithmetic-instructions/10-abs.md) | yes | Supported on all target architectures. |
| 9.7.1.11. | [`neg`](instructions/01-integer-arithmetic-instructions/11-neg.md) | yes | Supported on all target architectures. |
| 9.7.1.12. | [`min`](instructions/01-integer-arithmetic-instructions/12-min.md) | yes | Supported on all target architectures. `min.u16x2`, `min{.relu}.s16x2` and `min.relu.s32` require `sm_90` or higher. |
| 9.7.1.13. | [`max`](instructions/01-integer-arithmetic-instructions/13-max.md) | yes | Supported on all target architectures. `max.u16x2`, `max{.relu}.s16x2` and `max.relu.s32` require `sm_90` or higher. |
| 9.7.1.14. | [`popc`](instructions/01-integer-arithmetic-instructions/14-popc.md) | yes | `popc` requires `sm_20` or higher. |
| 9.7.1.15. | [`clz`](instructions/01-integer-arithmetic-instructions/15-clz.md) | yes | `clz` requires `sm_20` or higher. |
| 9.7.1.16. | [`bfind`](instructions/01-integer-arithmetic-instructions/16-bfind.md) | yes | `bfind` requires `sm_20` or higher. |
| 9.7.1.17. | [`fns`](instructions/01-integer-arithmetic-instructions/17-fns.md) | yes | `fns` requires `sm_30` or higher. |
| 9.7.1.18. | [`brev`](instructions/01-integer-arithmetic-instructions/18-brev.md) | yes | `brev` requires `sm_20` or higher. |
| 9.7.1.19. | [`bfe`](instructions/01-integer-arithmetic-instructions/19-bfe.md) | yes | `bfe` requires `sm_20` or higher. |
| 9.7.1.20. | [`bfi`](instructions/01-integer-arithmetic-instructions/20-bfi.md) | yes | `bfi` requires `sm_20` or higher. |
| 9.7.1.21. | [`szext`](instructions/01-integer-arithmetic-instructions/21-szext.md) | yes | `szext` requires `sm_70` or higher. |
| 9.7.1.22. | [`bmsk`](instructions/01-integer-arithmetic-instructions/22-bmsk.md) | yes | `bmsk` requires `sm_70` or higher. |
| 9.7.1.23. | [`dp4a`](instructions/01-integer-arithmetic-instructions/23-dp4a.md) | yes | Requires `sm_61` or higher. |
| 9.7.1.24. | [`dp2a`](instructions/01-integer-arithmetic-instructions/24-dp2a.md) | yes | Requires `sm_61` or higher. |

## 9.7.2. Extended-Precision Integer Arithmetic Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.2.1. | [`add.cc`](instructions/02-extended-precision-integer-arithmetic-instructions/01-add-cc.md) | yes | 32-bit `add.cc` is supported on all target architectures. 64-bit `add.cc` requires `sm_20` or higher. |
| 9.7.2.2. | [`addc`](instructions/02-extended-precision-integer-arithmetic-instructions/02-addc.md) | yes | 32-bit `addc` is supported on all target architectures. 64-bit `addc` requires `sm_20` or higher. |
| 9.7.2.3. | [`sub.cc`](instructions/02-extended-precision-integer-arithmetic-instructions/03-sub-cc.md) | yes | 32-bit `sub.cc` is supported on all target architectures. 64-bit `sub.cc` requires `sm_20` or higher. |
| 9.7.2.4. | [`subc`](instructions/02-extended-precision-integer-arithmetic-instructions/04-subc.md) | yes | 32-bit `subc` is supported on all target architectures. 64-bit `subc` requires `sm_20` or higher. |
| 9.7.2.5. | [`mad.cc`](instructions/02-extended-precision-integer-arithmetic-instructions/05-mad-cc.md) | yes | Requires target `sm_20` or higher. |
| 9.7.2.6. | [`madc`](instructions/02-extended-precision-integer-arithmetic-instructions/06-madc.md) | yes | Requires target `sm_20` or higher. |

## 9.7.3. Floating-Point Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.3.1. | [`testp`](instructions/03-floating-point-instructions/01-testp.md) | yes | Requires `sm_20` or higher. |
| 9.7.3.2. | [`copysign`](instructions/03-floating-point-instructions/02-copysign.md) | yes | Requires `sm_20` or higher. |
| 9.7.3.3. | [`add`](instructions/03-floating-point-instructions/03-add.md) | yes | `add.f32` supported on all target architectures. `add.f64` requires `sm_13` or higher. Rounding modifiers have the following target requirements: `.rn`, `.rz` available for all targets `.rm`, `.rp` for `add.f64`, requ... |
| 9.7.3.4. | [`sub`](instructions/03-floating-point-instructions/04-sub.md) | yes | `sub.f32` supported on all target architectures. `sub.f64` requires `sm_13` or higher. Rounding modifiers have the following target requirements: `.rn`, `.rz` available for all targets `.rm`, `.rp` for `sub.f64`, requ... |
| 9.7.3.5. | [`mul`](instructions/03-floating-point-instructions/05-mul.md) | yes | `mul.f32` supported on all target architectures. `mul.f64` requires `sm_13` or higher. Rounding modifiers have the following target requirements: `.rn`, `.rz` available for all targets `.rm`, `.rp` for `mul.f64`, requ... |
| 9.7.3.6. | [`fma`](instructions/03-floating-point-instructions/06-fma.md) | yes | `fma.f32` requires `sm_20` or higher. `fma.f64` requires `sm_13` or higher. `fma.f32x2` requires `sm_100` or higher. |
| 9.7.3.7. | [`mad`](instructions/03-floating-point-instructions/07-mad.md) | yes | `mad.f32` supported on all target architectures. `mad.f64` requires `sm_13` or higher. Rounding modifiers have the following target requirements: `.rn`, `.rz`, `.rm`, `.rp` for `mad.f64`, requires `sm_13` or higher. `... |
| 9.7.3.8. | [`div`](instructions/03-floating-point-instructions/08-div.md) | yes | `div.approx.f32` and `div.full.f32` supported on all target architectures. `div.rnd.f32` requires `sm_20` or higher. `div.rn.f64` requires `sm_13` or higher, or `.target`` ``map_f64_to_f32`. `div.{rz,rm,rp}.f64` requi... |
| 9.7.3.9. | [`abs`](instructions/03-floating-point-instructions/09-abs.md) | yes | `abs.f32` supported on all target architectures. `abs.f64` requires `sm_13` or higher. |
| 9.7.3.10. | [`neg`](instructions/03-floating-point-instructions/10-neg.md) | yes | `neg.f32` supported on all target architectures. `neg.f64` requires `sm_13` or higher. |
| 9.7.3.11. | [`min`](instructions/03-floating-point-instructions/11-min.md) | yes | `min.f32` supported on all target architectures. `min.f64` requires `sm_13` or higher. `min.NaN` requires `sm_80` or higher. `min.xorsign.abs` requires `sm_86` or higher. `min` with three input arguments requires `sm_... |
| 9.7.3.12. | [`max`](instructions/03-floating-point-instructions/12-max.md) | yes | `max.f32` supported on all target architectures. `max.f64` requires `sm_13` or higher. `max.NaN` requires `sm_80` or higher. `max.xorsign.abs` requires `sm_86` or higher. `max` with three input arguments requires `sm_... |
| 9.7.3.13. | [`rcp`](instructions/03-floating-point-instructions/13-rcp.md) | yes | `rcp.approx.f32` supported on all target architectures. `rcp.rnd.f32` requires `sm_20` or higher. `rcp.rn.f64` requires `sm_13` or higher, or `.target`` ``map_f64_to_f32.` `rcp.{rz,rm,rp}.f64` requires `sm_20` or high... |
| 9.7.3.14. | [`rcp.approx.ftz.f64`](instructions/03-floating-point-instructions/14-rcp-approx-ftz-f64.md) | yes | `rcp.approx.ftz.f64` requires `sm_20` or higher. |
| 9.7.3.15. | [`sqrt`](instructions/03-floating-point-instructions/15-sqrt.md) | yes | `sqrt.approx.f32` supported on all target architectures. `sqrt.rnd.f32` requires `sm_20` or higher. `sqrt.rn.f64` requires `sm_13` or higher, or `.target`` ``map_f64_to_f32`. `sqrt.{rz,rm,rp}.f64` requires `sm_20` or ... |
| 9.7.3.16. | [`rsqrt`](instructions/03-floating-point-instructions/16-rsqrt.md) | yes | `rsqrt.f32` supported on all target architectures. `rsqrt.f64` requires `sm_13` or higher. |
| 9.7.3.17. | [`rsqrt.approx.ftz.f64`](instructions/03-floating-point-instructions/17-rsqrt-approx-ftz-f64.md) | yes | `rsqrt.approx.ftz.f64` requires `sm_20` or higher. |
| 9.7.3.18. | [`sin`](instructions/03-floating-point-instructions/18-sin.md) | yes | Supported on all target architectures. |
| 9.7.3.19. | [`cos`](instructions/03-floating-point-instructions/19-cos.md) | yes | Supported on all target architectures. |
| 9.7.3.20. | [`lg2`](instructions/03-floating-point-instructions/20-lg2.md) | yes | Supported on all target architectures. |
| 9.7.3.21. | [`ex2`](instructions/03-floating-point-instructions/21-ex2.md) | yes | Supported on all target architectures. |
| 9.7.3.22. | [`tanh`](instructions/03-floating-point-instructions/22-tanh.md) | yes | Requires `sm_75` or higher. |

## 9.7.4. Half Precision Floating-Point Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.4.1. | [`add`](instructions/04-half-precision-floating-point-instructions/01-add.md) | yes | Requires `sm_53` or higher. `add{.rnd}.bf16` and `add{.rnd}.bf16x2` requires `sm_90` or higher. |
| 9.7.4.2. | [`sub`](instructions/04-half-precision-floating-point-instructions/02-sub.md) | yes | Requires `sm_53` or higher. `sub{.rnd}.bf16` and `sub{.rnd}.bf16x2` requires `sm_90` or higher. |
| 9.7.4.3. | [`mul`](instructions/04-half-precision-floating-point-instructions/03-mul.md) | yes | Requires `sm_53` or higher. `mul{.rnd}.bf16` and `mul{.rnd}.bf16x2` requires `sm_90` or higher. |
| 9.7.4.4. | [`fma`](instructions/04-half-precision-floating-point-instructions/04-fma.md) | yes | Requires `sm_53` or higher. `fma.relu.{f16,`` ``f16x2}` and `fma{.relu}.{bf16,`` ``bf16x2}` require `sm_80` or higher. `fma{.oob}.{f16,`` ``f16x2,`` ``bf16,`` ``bf16x2}` requires `sm_90` or higher. |
| 9.7.4.5. | [`neg`](instructions/04-half-precision-floating-point-instructions/05-neg.md) | yes | Requires `sm_53` or higher. `neg.bf16` and `neg.bf16x2` requires architecture `sm_80` or higher. |
| 9.7.4.6. | [`abs`](instructions/04-half-precision-floating-point-instructions/06-abs.md) | yes | Requires `sm_53` or higher. `abs.bf16` and `abs.bf16x2` requires architecture `sm_80` or higher. |
| 9.7.4.7. | [`min`](instructions/04-half-precision-floating-point-instructions/07-min.md) | yes | Requires `sm_80` or higher. `min.xorsign.abs` support requires `sm_86` or higher. |
| 9.7.4.8. | [`max`](instructions/04-half-precision-floating-point-instructions/08-max.md) | yes | Requires `sm_80` or higher. `max.xorsign.abs` support requires `sm_86` or higher. |
| 9.7.4.9. | [`tanh`](instructions/04-half-precision-floating-point-instructions/09-tanh.md) | yes | Requires `sm_75` or higher. `tanh.approx.{bf16/bf16x2}` requires `sm_90` or higher. |
| 9.7.4.10. | [`ex2`](instructions/04-half-precision-floating-point-instructions/10-ex2.md) | yes | Requires `sm_75` or higher. `ex2.approx.ftz.{bf16/bf16x2}` requires `sm_90` or higher. |

## 9.7.5. Mixed Precision Floating-Point Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.5.1. | [`add`](instructions/05-mixed-precision-floating-point-instructions/01-add.md) | yes | `add.f32.{f16/bf16}` requires `sm_100` or higher. |
| 9.7.5.2. | [`sub`](instructions/05-mixed-precision-floating-point-instructions/02-sub.md) | yes | `sub.f32.{f16/bf16}` requires `sm_100` or higher. |
| 9.7.5.3. | [`fma`](instructions/05-mixed-precision-floating-point-instructions/03-fma.md) | yes | `fma.f32.{f16/bf16}` requires `sm_100` or higher. |

## 9.7.6. Comparison and Selection Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.6.1. | [`set`](instructions/06-comparison-and-selection-instructions/01-set.md) | yes | `set` with `.f64` source type requires `sm_13` or higher. |
| 9.7.6.2. | [`setp`](instructions/06-comparison-and-selection-instructions/02-setp.md) | yes | `setp` with `.f64` source type requires `sm_13` or higher. |
| 9.7.6.3. | [`selp`](instructions/06-comparison-and-selection-instructions/03-selp.md) | yes | `selp.f64` requires `sm_13` or higher. |
| 9.7.6.4. | [`slct`](instructions/06-comparison-and-selection-instructions/04-slct.md) | yes | `slct.f64` requires `sm_13` or higher. |

## 9.7.7. Half Precision Comparison Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.7.1. | [`set`](instructions/07-half-precision-comparison-instructions/01-set.md) | yes | Requires `sm_53` or higher. `set.{u16,`` ``u32,`` ``s16,`` ``s32}.bf16`, `set.{u32,`` ``s32,`` ``bf16x2}.bf16x2`, `set.bf16.{s16,u16,f16,b16,s32,u32,f32,b32,s64,u64,f64,b64}` require `sm_90` or higher. |
| 9.7.7.2. | [`setp`](instructions/07-half-precision-comparison-instructions/02-setp.md) | yes | Requires `sm_53` or higher. `setp.{bf16/bf16x2}` requires `sm_90` or higher. |

## 9.7.8. Logic and Shift Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.8.1. | [`and`](instructions/08-logic-and-shift-instructions/01-and.md) | yes | Supported on all target architectures. |
| 9.7.8.2. | [`or`](instructions/08-logic-and-shift-instructions/02-or.md) | yes | Supported on all target architectures. |
| 9.7.8.3. | [`xor`](instructions/08-logic-and-shift-instructions/03-xor.md) | yes | Supported on all target architectures. |
| 9.7.8.4. | [`not`](instructions/08-logic-and-shift-instructions/04-not.md) | yes | Supported on all target architectures. |
| 9.7.8.5. | [`cnot`](instructions/08-logic-and-shift-instructions/05-cnot.md) | yes | Supported on all target architectures. |
| 9.7.8.6. | [`lop3`](instructions/08-logic-and-shift-instructions/06-lop3.md) | yes | Requires `sm_50` or higher. Qualifier `.BoolOp` requires `sm_70` or higher. |
| 9.7.8.7. | [`shf`](instructions/08-logic-and-shift-instructions/07-shf.md) | yes | Requires `sm_32` or higher. Example shf.l.clamp.b32  r3,r1,r0,16; // 128-bit left shift; n < 32 // [r7,r6,r5,r4] = [r3,r2,r1,r0] << n shf.l.clamp.b32  r7,r2,r3,n; shf.l.clamp.b32  r6,r1,r2,n; shf.l.clamp.b32  r5,r0,r1... |
| 9.7.8.8. | [`shl`](instructions/08-logic-and-shift-instructions/08-shl.md) | yes | Supported on all target architectures. Example shl.b32  q,a,2; |
| 9.7.8.9. | [`shr`](instructions/08-logic-and-shift-instructions/09-shr.md) | yes | Supported on all target architectures. Example shr.u16  c,a,2; shr.s32  i,i,1; shr.b16  k,i,j; |

## 9.7.9. Data Movement and Conversion Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.9.1. | [Cache Operators](instructions/09-data-movement-and-conversion-instructions/01-cache-operators.md) | ? |  |
| 9.7.9.2. | [Cache Eviction Priority Hints](instructions/09-data-movement-and-conversion-instructions/02-cache-eviction-priority-hints.md) | ? |  |
| 9.7.9.3. | [`mov`](instructions/09-data-movement-and-conversion-instructions/03-mov.md) | yes | `mov.f64` requires `sm_13` or higher. Taking the address of kernel entry functions requires `sm_35` or higher. |
| 9.7.9.4. | [`mov`](instructions/09-data-movement-and-conversion-instructions/04-mov.md) | yes | Supported on all target architectures. Support for `.b128` type requires `sm_70` or higher. |
| 9.7.9.5. | [`shfl` (deprecated)](instructions/09-data-movement-and-conversion-instructions/05-shfl-deprecated.md) | yes | `shfl` requires `sm_30` or higher. `shfl` is not supported on `sm_70` or higher starting PTX ISA version 6.4. |
| 9.7.9.6. | [`shfl.sync`](instructions/09-data-movement-and-conversion-instructions/06-shfl-sync.md) | yes | Requires `sm_30` or higher. |
| 9.7.9.7. | [`prmt`](instructions/09-data-movement-and-conversion-instructions/07-prmt.md) | yes | `prmt` requires `sm_20` or higher. |
| 9.7.9.8. | [`ld`](instructions/09-data-movement-and-conversion-instructions/08-ld.md) | yes | `ld.f64` requires `sm_13` or higher. Support for scope qualifier, `.relaxed`, `.acquire`, `.weak` qualifiers require `sm_70` or higher. Generic addressing requires `sm_20` or higher. Cache operations require `sm_20` o... |
| 9.7.9.9. | [`ld.global.nc`](instructions/09-data-movement-and-conversion-instructions/09-ld-global-nc.md) | yes | Requires `sm_32` or higher. Support for `.level1::eviction_priority` qualifier requires `sm_70` or higher. Support for `.level::prefetch_size` qualifier requires `sm_75` or higher. Support for `.level::cache_hint` qua... |
| 9.7.9.10. | [`ldu`](instructions/09-data-movement-and-conversion-instructions/10-ldu.md) | yes | `ldu.f64` requires `sm_13` or higher. Support for `.b128` type requires `sm_70` or higher. |
| 9.7.9.11. | [`st`](instructions/09-data-movement-and-conversion-instructions/11-st.md) | yes | `st.f64` requires `sm_13` or higher. Support for scope qualifier, `.relaxed`, `.release`, `.weak` qualifiers require `sm_70` or higher. Generic addressing requires `sm_20` or higher. Cache operations require `sm_20` o... |
| 9.7.9.12. | [`st.async`](instructions/09-data-movement-and-conversion-instructions/12-st-async.md) | yes | Requires `sm_90` or higher. `.mmio` qualifier, `.release` semantics, `.global` state space, and `.scope` qualifier require `sm_100` or higher. |
| 9.7.9.13. | [`st.bulk`](instructions/09-data-movement-and-conversion-instructions/13-st-bulk.md) | yes | Requires `sm_100` or higher. |
| 9.7.9.14. | [`multimem.ld_reduce`, `multimem.st`, `multimem.red`](instructions/09-data-movement-and-conversion-instructions/14-multimem-ld-reduce-multimem-st-multimem-red.md) | partial | Requires `sm_90` or higher. Types `.e5m2`, `.e5m2x2`, `.e5m2x4`, `.e4m3`, `.e4m3x2`, `.e4m3x4` are supported on following architectures: `sm_100a` `sm_101a` `sm_120a` `sm_121a` And are supported on following family-sp... |
| 9.7.9.15. | [`prefetch`, `prefetchu`](instructions/09-data-movement-and-conversion-instructions/15-prefetch-prefetchu.md) | yes | `prefetch` and `prefetchu` require `sm_20` or higher. Support for `.level::eviction_priority` qualifier requires `sm_80` or higher. Support for the `.tensormap` qualifier requires `sm_90` or higher. |
| 9.7.9.16. | [`applypriority`](instructions/09-data-movement-and-conversion-instructions/16-applypriority.md) | yes | Requires `sm_80` or higher. |
| 9.7.9.17. | [`discard`](instructions/09-data-movement-and-conversion-instructions/17-discard.md) | yes | Requires `sm_80` or higher. |
| 9.7.9.18. | [`createpolicy`](instructions/09-data-movement-and-conversion-instructions/18-createpolicy.md) | yes | Requires `sm_80` or higher. |
| 9.7.9.19. | [`isspacep`](instructions/09-data-movement-and-conversion-instructions/19-isspacep.md) | yes | `isspacep` requires `sm_20` or higher. `isspacep.param{::entry}` requires `sm_70` or higher. Sub-qualifier `::cta` requires `sm_30` or higher. Sub-qualifier `::cluster` requires `sm_90` or higher. |
| 9.7.9.20. | [`cvta`](instructions/09-data-movement-and-conversion-instructions/20-cvta.md) | yes | `cvta` requires `sm_20` or higher. `cvta.param{::entry}` and `cvta.to.param{::entry}` requires `sm_70` or higher. Sub-qualifier `::cta` requires `sm_30` or higher. Sub-qualifier `::cluster` requires `sm_90` or higher. |
| 9.7.9.21. | [`cvt`](instructions/09-data-movement-and-conversion-instructions/21-cvt.md) | yes | `cvt` to or from `.f64` requires `sm_13` or higher. `.relu` modifier and {`.f16x2`, `.bf16`, `.bf16x2`, `.tf32`} destination formats require `sm_80` or higher. `cvt.bf16.{u8/s8/u16/s16/u32/s32/u64/s64/f16/f64/bf16}`, ... |
| 9.7.9.22. | [`cvt.pack`](instructions/09-data-movement-and-conversion-instructions/22-cvt-pack.md) | yes | Requires `sm_72` or higher. Sub byte types (`.u4`/`.s4` and `.u2`/`.s2`) requires `sm_75` or higher. |
| 9.7.9.23. | [`mapa`](instructions/09-data-movement-and-conversion-instructions/23-mapa.md) | yes | Requires `sm_90` or higher. |
| 9.7.9.24. | [`getctarank`](instructions/09-data-movement-and-conversion-instructions/24-getctarank.md) | yes | Requires `sm_90` or higher. |
| 9.7.9.25. | [Asynchronous copy](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md) | yes | Requires `sm_80` or higher. Sub-qualifier `::cta` requires `sm_30` or higher. Requires `sm_80` or higher. Requires `sm_80` or higher.  Requires `sm_90` or higher. `.multicast::cluster` qualifier advised to be used wit... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.3.1. | ↳ [`cp.async`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async) | yes | Requires `sm_80` or higher. Sub-qualifier `::cta` requires `sm_30` or higher. |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.3.2. | ↳ [`cp.async.commit_group`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-commit-group) | yes | Requires `sm_80` or higher. |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.3.3. | ↳ [`cp.async.wait_group` / `cp.async.wait_all`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-wait-group) | yes | Requires `sm_80` or higher. |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.4.1. | ↳ [`cp.async.bulk`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-bulk) | yes | Requires `sm_90` or higher. `.multicast::cluster` qualifier advised to be used with `.target` `sm_90a` or `sm_100f` or `sm_100a` or `sm_101f` or `sm_101a` or `sm_103f` or `sm_103a`. Support for `.cp_mask` qualifier re... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.4.2. | ↳ [`cp.reduce.async.bulk`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-reduce-async-bulk) | yes | Requires `sm_90` or higher. |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.4.3. | ↳ [`cp.async.bulk.prefetch`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-bulk-prefetch) | yes | Requires `sm_90` or higher. |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.5.2. | ↳ [`cp.async.bulk.tensor`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-bulk-tensor) | yes | Requires `sm_90` or higher. `.multicast::cluster` qualifier advised to be used with `.target` `sm_90a` or `sm_100f` or `sm_100a` or `sm_101f` or `sm_101a` or `sm_103f` or `sm_103a`. Qualifiers `.tile::gather4` and `.i... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.5.3. | ↳ [`cp.reduce.async.bulk.tensor`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-reduce-async-bulk-tensor) | yes | Requires `sm_90` or higher. |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.5.4. | ↳ [`cp.async.bulk.prefetch.tensor`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-bulk-prefetch-tensor) | yes | Requires `sm_90` or higher. Qualifier `.tile::gather4` is supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or hi... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.6.1. | ↳ [`cp.async.bulk.commit_group`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-bulk-commit-group) | yes | Requires `sm_90` or higher. |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.9.25.6.2. | ↳ [`cp.async.bulk.wait_group`](instructions/09-data-movement-and-conversion-instructions/25-asynchronous-copy.md#data-movement-and-conversion-instructions-cp-async-bulk-wait-group) | yes | Requires `sm_90` or higher. |
| 9.7.9.26. | [`tensormap.replace`](instructions/09-data-movement-and-conversion-instructions/26-tensormap-replace.md) | yes | Supported on following architectures: `sm_90a` `sm_100a` `sm_101a` `sm_120a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or hi... |

## 9.7.10. Texture Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.10.1. | [Texturing Modes](instructions/10-texture-instructions/01-texturing-modes.md) | ? |  |
| 9.7.10.2. | [Mipmaps](instructions/10-texture-instructions/02-mipmaps.md) | ? |  |
| 9.7.10.3. | [`tex`](instructions/10-texture-instructions/03-tex.md) | yes | Supported on all target architectures. The cubemap array geometry (`.acube`) requires `sm_20` or higher. Mipmaps require `sm_20` or higher. Indirect texture access requires `sm_20` or higher. Multi-sample textures and... |
| 9.7.10.4. | [`tld4`](instructions/10-texture-instructions/04-tld4.md) | yes | `tld4` requires `sm_20` or higher. Indirect texture access requires `sm_20` or higher. `tld4.{a2d,cube,acube}` requires `sm_30` or higher. Offset vector operand requires `sm_30` or higher. Depth compare operand requir... |
| 9.7.10.5. | [`txq`](instructions/10-texture-instructions/05-txq.md) | yes | Supported on all target architectures. Indirect texture access requires `sm_20` or higher. Querying the number of mipmap levels requires `sm_20` or higher. Querying the number of samples requires `sm_30` or higher. `t... |
| 9.7.10.6. | [`istypep`](instructions/10-texture-instructions/06-istypep.md) | yes | istypep requires `sm_30` or higher. |

## 9.7.11. Surface Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.11.1. | [`suld`](instructions/11-surface-instructions/01-suld.md) | yes | `suld.b` supported on all target architectures. `sm_1x` targets support only the `.trap` clamping modifier. `suld.3d` and `suld.{a1d,a2d}` require `sm_20` or higher. Indirect surface access requires `sm_20` or higher.... |
| 9.7.11.2. | [`sust`](instructions/11-surface-instructions/02-sust.md) | yes | `sust.b` supported on all target architectures. `sm_1x` targets support only the `.trap` clamping modifier. `sust.3d` and `sust.{a1d,a2d}` require `sm_20` or higher. `sust.p` requires `sm_20` or higher. Indirect surfa... |
| 9.7.11.3. | [`sured`](instructions/11-surface-instructions/03-sured.md) | yes | sured requires `sm_20` or higher. Indirect surface access requires `sm_20` or higher. `.u64`/`.s64`/`.b64` types with `.min`/`.max` operations requires `sm_50` or higher. |
| 9.7.11.4. | [`suq`](instructions/11-surface-instructions/04-suq.md) | yes | Supported on all target architectures. Indirect surface access requires `sm_20` or higher. |

## 9.7.12. Control Flow Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.12.1. | [`{}`](instructions/12-control-flow-instructions/01-.md) | yes | Supported on all target architectures. |
| 9.7.12.2. | [`@`](instructions/12-control-flow-instructions/02-.md) | yes | Supported on all target architectures. |
| 9.7.12.3. | [`bra`](instructions/12-control-flow-instructions/03-bra.md) | yes | Supported on all target architectures. |
| 9.7.12.4. | [`brx.idx`](instructions/12-control-flow-instructions/04-brx-idx.md) | yes | Requires `sm_30` or higher. |
| 9.7.12.5. | [`call`](instructions/12-control-flow-instructions/05-call.md) | yes | Direct `call` supported on all target architectures. Indirect `call` requires `sm_20` or higher. |
| 9.7.12.6. | [`ret`](instructions/12-control-flow-instructions/06-ret.md) | yes | Supported on all target architectures. |
| 9.7.12.7. | [`exit`](instructions/12-control-flow-instructions/07-exit.md) | yes | Supported on all target architectures. |

## 9.7.13. Parallel Synchronization and Communication Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.13.1. | [`bar`, `barrier`](instructions/13-parallel-synchronization-and-communication-instructions/01-bar-barrier.md) | yes | Register operands, thread count, and `bar{.cta}.{arrive,red}` require `sm_20` or higher. Only `bar{.cta}.sync` with an immediate barrier number is supported for `sm_1x` targets. `barrier{.cta}` instruction requires `s... |
| 9.7.13.2. | [`bar.warp.sync`](instructions/13-parallel-synchronization-and-communication-instructions/02-bar-warp-sync.md) | yes | Requires `sm_30` or higher. |
| 9.7.13.3. | [`barrier.cluster`](instructions/13-parallel-synchronization-and-communication-instructions/03-barrier-cluster.md) | yes | Requires `sm_90` or higher. |
| 9.7.13.4. | [`membar` / `fence`](instructions/13-parallel-synchronization-and-communication-instructions/04-membar-fence.md) | yes | `membar.{cta,gl}` supported on all target architectures. `membar.sys` requires `sm_20` or higher. `fence` requires `sm_70` or higher. `membar.proxy` requires `sm_60` or higher. `fence.proxy` requires `sm_70` or higher... |
| 9.7.13.5. | [`atom`](instructions/13-parallel-synchronization-and-communication-instructions/05-atom.md) | yes | `atom.global` requires `sm_11` or higher. `atom.shared` requires `sm_12` or higher. 64-bit `atom.global.{add,cas,exch}` require `sm_12` or higher. 64-bit `atom.shared.{add,cas,exch}` require `sm_20` or higher. 64-bit ... |
| 9.7.13.6. | [`red`](instructions/13-parallel-synchronization-and-communication-instructions/06-red.md) | yes | `red.global` requires `sm_11` or higher `red.shared` requires `sm_12` or higher. `red.global.add.u64` requires `sm_12` or higher. `red.shared.add.u64` requires `sm_20` or higher. 64-bit `red.{and,or,xor,min,max}` requ... |
| 9.7.13.7. | [`red.async`](instructions/13-parallel-synchronization-and-communication-instructions/07-red-async.md) | yes | Requires `sm_90` or higher. `.mmio` qualifier, `.release` semantics, `.global` state space, and `.gpu` and `.sys` scopes require `sm_100` or higher. |
| 9.7.13.8. | [`vote` (deprecated)](instructions/13-parallel-synchronization-and-communication-instructions/08-vote-deprecated.md) | yes | `vote` requires `sm_12` or higher. `vote.ballot.b32` requires `sm_20` or higher. `vote` is not supported on `sm_70` or higher starting PTX ISA version 6.4. Release Notes Note that `vote` applies to threads in a single... |
| 9.7.13.9. | [`vote.sync`](instructions/13-parallel-synchronization-and-communication-instructions/09-vote-sync.md) | yes | Requires `sm_30` or higher. |
| 9.7.13.10. | [`match.sync`](instructions/13-parallel-synchronization-and-communication-instructions/10-match-sync.md) | yes | Requires `sm_70` or higher. Release Notes Note that `match.sync` applies to threads in a single warp, not across an entire CTA. |
| 9.7.13.11. | [`activemask`](instructions/13-parallel-synchronization-and-communication-instructions/11-activemask.md) | yes | Requires `sm_30` or higher. |
| 9.7.13.12. | [`redux.sync`](instructions/13-parallel-synchronization-and-communication-instructions/12-redux-sync.md) | yes | Requires `sm_80` or higher. `.f32` type requires `sm_100a` and is supported on `sm_100f` from PTX ISA version 8.8. Qualifiers `.abs` and `.NaN` require `sm_100a` and are supported on `sm_100f` or higher in the same fa... |
| 9.7.13.13. | [`griddepcontrol`](instructions/13-parallel-synchronization-and-communication-instructions/13-griddepcontrol.md) | yes | Requires `sm_90` or higher. |
| 9.7.13.14. | [`elect.sync`](instructions/13-parallel-synchronization-and-communication-instructions/14-elect-sync.md) | yes | Requires `sm_90` or higher. |
| 9.7.13.15. | [`mbarrier`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md) | yes | Requires `sm_80` or higher. Requires `sm_80` or higher. Requires `sm_90` or higher. Requires `sm_90` or higher. Requires `sm_80` or higher. Support for `count` argument without the modifier `.noComplete` requires `sm_... |
| &nbsp;&nbsp;9.7.13.15.9. | ↳ [`mbarrier.init`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-init) | yes | Requires `sm_80` or higher. |
| &nbsp;&nbsp;9.7.13.15.10. | ↳ [`mbarrier.inval`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-inval) | yes | Requires `sm_80` or higher. |
| &nbsp;&nbsp;9.7.13.15.11. | ↳ [`mbarrier.expect_tx`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-expect-tx) | yes | Requires `sm_90` or higher. |
| &nbsp;&nbsp;9.7.13.15.12. | ↳ [`mbarrier.complete_tx`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-complete-tx) | yes | Requires `sm_90` or higher. |
| &nbsp;&nbsp;9.7.13.15.13. | ↳ [`mbarrier.arrive`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-arrive) | yes | Requires `sm_80` or higher. Support for `count` argument without the modifier `.noComplete` requires `sm_90` or higher. Qualifier `.expect_tx` requires `sm_90` or higher. Sub-qualifier `::cluster` requires `sm_90` or ... |
| &nbsp;&nbsp;9.7.13.15.14. | ↳ [`mbarrier.arrive_drop`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-arrive-drop) | yes | Requires `sm_80` or higher. Support for `count` argument without the modifier `.noComplete` requires `sm_90` or higher. Qualifier `.expect_tx` requires `sm_90` or higher. Sub-qualifier `::cluster` requires `sm_90` or ... |
| &nbsp;&nbsp;9.7.13.15.15. | ↳ [`cp.async.mbarrier.arrive`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-cp-async-mbarrier-arrive) | yes | Requires `sm_80` or higher. |
| &nbsp;&nbsp;9.7.13.15.16. | ↳ [`mbarrier.test_wait` / `mbarrier.try_wait`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-test-wait-try-wait) | yes | `mbarrier.test_wait` requires `sm_80` or higher. `mbarrier.try_wait` requires `sm_90` or higher. Support for `.cluster` scope requires `sm_90` or higher. |
| &nbsp;&nbsp;9.7.13.15.17. | ↳ [`mbarrier.pending_count`](instructions/13-parallel-synchronization-and-communication-instructions/15-mbarrier.md#parallel-synchronization-and-communication-instructions-mbarrier-pending-count) | yes | Requires `sm_80` or higher. |
| 9.7.13.16. | [`tensormap.cp_fenceproxy`](instructions/13-parallel-synchronization-and-communication-instructions/16-tensormap-cp-fenceproxy.md) | yes | Requires `sm_90` or higher. |
| 9.7.13.17. | [`clusterlaunchcontrol.try_cancel`](instructions/13-parallel-synchronization-and-communication-instructions/17-clusterlaunchcontrol-try-cancel.md) | yes | Requires `sm_100` or higher. Qualifier `.multicast::cluster::all` is supported on following architectures: `sm_100a` `sm_101a` `sm_120a` And is supported on following family-specific architectures from PTX ISA version... |
| 9.7.13.18. | [`clusterlaunchcontrol.query_cancel`](instructions/13-parallel-synchronization-and-communication-instructions/18-clusterlaunchcontrol-query-cancel.md) | yes | Requires `sm_100` or higher. |

## 9.7.14. Warp Level Matrix Multiply-Accumulate Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.14.1. | [Matrix Shape](instructions/14-warp-level-matrix-multiply-accumulate-instructions/01-matrix-shape.md) | ? |  |
| 9.7.14.2. | [Matrix Data-types](instructions/14-warp-level-matrix-multiply-accumulate-instructions/02-matrix-data-types.md) | ? |  |
| 9.7.14.3. | [Block Scaling](instructions/14-warp-level-matrix-multiply-accumulate-instructions/03-block-scaling.md) | ? |  |
| 9.7.14.4. | [Matrix multiply-accumulate operation using `wmma` instructions](instructions/14-warp-level-matrix-multiply-accumulate-instructions/04-matrix-multiply-accumulate-operation-using-wmma-instructions.md) | yes | Floating point `wmma` requires `sm_70` or higher. Integer `wmma` requires `sm_72` or higher. Sub-byte and single-bit `wmma` requires `sm_75` or higher. Double precision and alternate floating point precision `wmma` re... |
| &nbsp;&nbsp;9.7.14.4.3. | ↳ [`wmma.load`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/04-matrix-multiply-accumulate-operation-using-wmma-instructions.md#warp-level-matrix-instructions-wmma-ld) | yes | Floating point `wmma` requires `sm_70` or higher. Integer `wmma` requires `sm_72` or higher. Sub-byte and single-bit `wmma` requires `sm_75` or higher. Double precision and alternate floating point precision `wmma` re... |
| &nbsp;&nbsp;9.7.14.4.4. | ↳ [`wmma.store`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/04-matrix-multiply-accumulate-operation-using-wmma-instructions.md#warp-level-matrix-instructions-wmma-st) | yes | Floating point `wmma` requires `sm_70` or higher. Integer `wmma` requires `sm_72` or higher. Sub-byte and single-bit `wmma` requires `sm_75` or higher. Double precision `wmma` and shape `.m16n16k8` requires `sm_80` or... |
| &nbsp;&nbsp;9.7.14.4.5. | ↳ [`wmma.mma`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/04-matrix-multiply-accumulate-operation-using-wmma-instructions.md#warp-level-matrix-instructions-wmma-mma) | yes | Floating point `wmma` requires `sm_70` or higher. Integer `wmma` requires `sm_72` or higher. Sub-byte and single-bit `wmma` requires `sm_75` or higher. Double precision, alternate floating point precision `wmma` requi... |
| 9.7.14.5. | [Matrix multiply-accumulate operation using `mma` instruction](instructions/14-warp-level-matrix-multiply-accumulate-instructions/05-matrix-multiply-accumulate-operation-using-mma-instruction.md) | yes | Requires `sm_70` or higher. `.f16` floating point type `mma` operation with `.m8n8k4` shape requires `sm_70` or higher. Note `mma.sync.m8n8k4` is optimized for target architecture `sm_70` and may have substantially re... |
| &nbsp;&nbsp;9.7.14.5.14. | ↳ [`mma`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/05-matrix-multiply-accumulate-operation-using-mma-instruction.md#warp-level-matrix-instructions-mma) | yes | Requires `sm_70` or higher. `.f16` floating point type `mma` operation with `.m8n8k4` shape requires `sm_70` or higher. Note `mma.sync.m8n8k4` is optimized for target architecture `sm_70` and may have substantially re... |
| &nbsp;&nbsp;9.7.14.5.15. | ↳ [`ldmatrix`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/05-matrix-multiply-accumulate-operation-using-mma-instruction.md#warp-level-matrix-instructions-ldmatrix) | yes | Requires `sm_75` or higher. Shapes `.m16n16`, `.m8n16` are supported on following architectures: `sm_100a` `sm_101a` `sm_120a` And are supported on following family-specific architectures from PTX ISA version 8.8: > -... |
| &nbsp;&nbsp;9.7.14.5.16. | ↳ [`stmatrix`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/05-matrix-multiply-accumulate-operation-using-mma-instruction.md#warp-level-matrix-instructions-stmatrix) | yes | Requires `sm_90` or higher. Shape `.m16n8` is supported on following architectures: `sm_100a` `sm_101a` `sm_120a` And is supported on following family-specific architectures from PTX ISA version 8.8: > - `sm_100f` or ... |
| &nbsp;&nbsp;9.7.14.5.17. | ↳ [`movmatrix`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/05-matrix-multiply-accumulate-operation-using-mma-instruction.md#warp-level-matrix-instructions-movmatrix) | yes | Requires `sm_75` or higher. |
| 9.7.14.6. | [Matrix multiply-accumulate operation using `mma.sp` instruction with sparse matrix A](instructions/14-warp-level-matrix-multiply-accumulate-instructions/06-matrix-multiply-accumulate-operation-using-mma-sp-instructio.md) | partial | Requires `sm_80` or higher. `.e4m3` and `.e5m2` alternate floating point type `mma` operation requires `sm_89` or higher. `mma.sp::ordered_metadata` requires `sm_80` or higher. Support for shape `.m16n8k32` and `.f16`... |
| &nbsp;&nbsp;9.7.14.6.3. | ↳ [`mma.sp` / `mma.sp::ordered_metadata`](instructions/14-warp-level-matrix-multiply-accumulate-instructions/06-matrix-multiply-accumulate-operation-using-mma-sp-instructio.md#warp-level-matrix-instructions-sparse-mma) | partial | Requires `sm_80` or higher. `.e4m3` and `.e5m2` alternate floating point type `mma` operation requires `sm_89` or higher. `mma.sp::ordered_metadata` requires `sm_80` or higher. Support for shape `.m16n8k32` and `.f16`... |

## 9.7.15. Asynchronous Warpgroup Level Matrix Multiply-Accumulate Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.15.1. | [Warpgroup](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/01-warpgroup.md) | ? |  |
| 9.7.15.2. | [Matrix Shape](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/02-matrix-shape.md) | ? |  |
| 9.7.15.3. | [Matrix Data-types](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/03-matrix-data-types.md) | ? |  |
| 9.7.15.4. | [Async Proxy](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/04-async-proxy.md) | ? |  |
| 9.7.15.5. | [Asynchronous Warpgroup Level Matrix Multiply-Accumulate Operation using `wgmma.mma_async` instruction](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/05-asynchronous-warpgroup-level-matrix-multiply-accumulate-oper.md) | yes | Requires `sm_90a`. Examples of half precision floating point type .reg .f16x2 f16a<40>, f16d<40>; .reg .f32   f32d<40>; .reg .b64   descA, descB; .reg .pred  scaleD; wgmma.mma_async.sync.aligned.m64n8k16.f32.f16.f16 {... |
| &nbsp;&nbsp;9.7.15.5.2. | ↳ [`wgmma.mma_async`](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/05-asynchronous-warpgroup-level-matrix-multiply-accumulate-oper.md#asynchronous-warpgroup-level-matrix-instructions-wgmma-mma) | yes | Requires `sm_90a`. Examples of half precision floating point type .reg .f16x2 f16a<40>, f16d<40>; .reg .f32   f32d<40>; .reg .b64   descA, descB; .reg .pred  scaleD; wgmma.mma_async.sync.aligned.m64n8k16.f32.f16.f16 {... |
| 9.7.15.6. | [Asynchronous Warpgroup Level Multiply-and-Accumulate Operation using `wgmma.mma_async.sp` instruction](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/06-asynchronous-warpgroup-level-multiply-and-accumulate-operati.md) | yes | Requires `sm_90a`. Examples of integer type wgmma.fence.sync.aligned; wgmma.mma_async.sp.sync.aligned.m64n8k64.s32.u8.u8  {s32d0, s32d1, s32d2, s32d3}, descA, descB, spMeta, 0, scaleD; wgmma.mma_async.sp.sync.aligned.... |
| &nbsp;&nbsp;9.7.15.6.3. | ↳ [`wgmma.mma_async.sp`](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/06-asynchronous-warpgroup-level-multiply-and-accumulate-operati.md#asynchronous-warpgroup-level-matrix-instructions-wgmma-mma-sp) | yes | Requires `sm_90a`. Examples of integer type wgmma.fence.sync.aligned; wgmma.mma_async.sp.sync.aligned.m64n8k64.s32.u8.u8  {s32d0, s32d1, s32d2, s32d3}, descA, descB, spMeta, 0, scaleD; wgmma.mma_async.sp.sync.aligned.... |
| 9.7.15.7. | [Asynchronous `wgmma` Proxy Operations](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/07-asynchronous-wgmma-proxy-operations.md) | yes | Requires `sm_90a`. Requires `sm_90a`. Requires `sm_90a`. |
| &nbsp;&nbsp;9.7.15.7.1. | ↳ [`wgmma.fence`](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/07-asynchronous-wgmma-proxy-operations.md#asynchronous-warpgroup-level-matrix-instructions-wgmma-fence) | yes | Requires `sm_90a`. |
| &nbsp;&nbsp;9.7.15.7.2. | ↳ [`wgmma.commit_group`](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/07-asynchronous-wgmma-proxy-operations.md#asynchronous-warpgroup-level-matrix-instructions-wgmma-commit-group) | yes | Requires `sm_90a`. |
| &nbsp;&nbsp;9.7.15.7.3. | ↳ [`wgmma.wait_group`](instructions/15-asynchronous-warpgroup-level-matrix-multiply-accumulate-inst/07-asynchronous-wgmma-proxy-operations.md#asynchronous-warpgroup-level-matrix-instructions-wgmma-wait-group) | yes | Requires `sm_90a`. |

## 9.7.16. TensorCore 5th Generation Family Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.16.1. | [Tensor Memory](instructions/16-tensorcore-5th-generation-family-instructions/01-tensor-memory.md) | ? |  |
| 9.7.16.2. | [Matrix and Data Movement Shape](instructions/16-tensorcore-5th-generation-family-instructions/02-matrix-and-data-movement-shape.md) | ? |  |
| 9.7.16.3. | [Major-ness supported by Strides](instructions/16-tensorcore-5th-generation-family-instructions/03-major-ness-supported-by-strides.md) | ? |  |
| 9.7.16.4. | [Matrix Descriptors](instructions/16-tensorcore-5th-generation-family-instructions/04-matrix-descriptors.md) | ? |  |
| 9.7.16.5. | [Issue Granularity](instructions/16-tensorcore-5th-generation-family-instructions/05-issue-granularity.md) | ? |  |
| 9.7.16.6. | [Memory Consistency Model for 5th generation of TensorCore operations](instructions/16-tensorcore-5th-generation-family-instructions/06-memory-consistency-model-for-5th-generation-of-tensorcore-op.md) | ? |  |
| 9.7.16.7. | [Tensor Memory Allocation and Management Instructions](instructions/16-tensorcore-5th-generation-family-instructions/07-tensor-memory-allocation-and-management-instructions.md) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.7.1. | ↳ [`tcgen05.alloc`, `tcgen05.dealloc`, `tcgen05.relinquish_alloc_permit`](instructions/16-tensorcore-5th-generation-family-instructions/07-tensor-memory-allocation-and-management-instructions.md#tcgen05-instructions-tcgen05-alloc-dealloc-relinquish-alloc-permit) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| 9.7.16.8. | [Tensor Memory and Register Load/Store Instructions](instructions/16-tensorcore-5th-generation-family-instructions/08-tensor-memory-and-register-load-store-instructions.md) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.8.3. | ↳ [`tcgen05.ld`](instructions/16-tensorcore-5th-generation-family-instructions/08-tensor-memory-and-register-load-store-instructions.md#tcgen05-instructions-tcgen05-ld) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.8.4. | ↳ [`tcgen05.st`](instructions/16-tensorcore-5th-generation-family-instructions/08-tensor-memory-and-register-load-store-instructions.md#tcgen05-instructions-tcgen05-st) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.8.5. | ↳ [`tcgen05.wait`](instructions/16-tensorcore-5th-generation-family-instructions/08-tensor-memory-and-register-load-store-instructions.md#tcgen05-instructions-tcgen05-wait) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| 9.7.16.9. | [Tensor Memory Data Movement Instructions](instructions/16-tensorcore-5th-generation-family-instructions/09-tensor-memory-data-movement-instructions.md) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.9.2. | ↳ [`tcgen05.cp`](instructions/16-tensorcore-5th-generation-family-instructions/09-tensor-memory-data-movement-instructions.md#tcgen05-instructions-tcgen05-cp) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.9.3. | ↳ [`tcgen05.shift`](instructions/16-tensorcore-5th-generation-family-instructions/09-tensor-memory-data-movement-instructions.md#tcgen05-instructions-tcgen05-shift) | yes | Supported on following architectures: `sm_100a` `sm_101a` `sm_103a` |
| 9.7.16.10. | [TensorCore 5th Generation Matrix Multiply and accumulate Operations](instructions/16-tensorcore-5th-generation-family-instructions/10-tensorcore-5th-generation-matrix-multiply-and-accumulate-ope.md) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8 except `.kind::i8`: `sm_100f` or higher in the same family `sm_101f` or hi... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.16.10.9.1. | ↳ [`tcgen05.mma`](instructions/16-tensorcore-5th-generation-family-instructions/10-tensorcore-5th-generation-matrix-multiply-and-accumulate-ope.md#tcgen05-mma-instructions-mma) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8 except `.kind::i8`: `sm_100f` or higher in the same family `sm_101f` or hi... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.16.10.9.2. | ↳ [`tcgen05.mma.sp`](instructions/16-tensorcore-5th-generation-family-instructions/10-tensorcore-5th-generation-matrix-multiply-and-accumulate-ope.md#tcgen05-mma-instructions-mma-sp) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8 except `.kind::i8`/`.kind::mxf4nvf4`/`.kind::mxf4`: `sm_100f` or higher in... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.16.10.9.3. | ↳ [`tcgen05.mma.ws`](instructions/16-tensorcore-5th-generation-family-instructions/10-tensorcore-5th-generation-matrix-multiply-and-accumulate-ope.md#tcgen05-mma-instructions-mma-ws) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8 except `.kind::i8`: `sm_100f` or higher in the same family `sm_101f` or hi... |
| &nbsp;&nbsp;&nbsp;&nbsp;9.7.16.10.9.4. | ↳ [`tcgen05.mma.ws.sp`](instructions/16-tensorcore-5th-generation-family-instructions/10-tensorcore-5th-generation-matrix-multiply-and-accumulate-ope.md#tcgen05-mma-instructions-mma-ws-sp) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8 except `.kind::i8`: `sm_100f` or higher in the same family `sm_101f` or hi... |
| 9.7.16.11. | [TensorCore 5th Generation Specialized Synchronization Operations](instructions/16-tensorcore-5th-generation-family-instructions/11-tensorcore-5th-generation-specialized-synchronization-operat.md) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.11.1. | ↳ [`tcgen05.fence`](instructions/16-tensorcore-5th-generation-family-instructions/11-tensorcore-5th-generation-specialized-synchronization-operat.md#tcgen05-special-sync-operations-fence) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| 9.7.16.12. | [TensorCore 5th Generation Async Synchronization Operations](instructions/16-tensorcore-5th-generation-family-instructions/12-tensorcore-5th-generation-async-synchronization-operations.md) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |
| &nbsp;&nbsp;9.7.16.12.1. | ↳ [`tcgen05.commit`](instructions/16-tensorcore-5th-generation-family-instructions/12-tensorcore-5th-generation-async-synchronization-operations.md#tcgen-async-sync-operations-commit) | yes | Supported on following architectures: `sm_100a` `sm_101a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or higher in the same fa... |

## 9.7.17. Stack Manipulation Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.17.1. | [`stacksave`](instructions/17-stack-manipulation-instructions/01-stacksave.md) | yes | `stacksave` requires `sm_52` or higher. |
| 9.7.17.2. | [`stackrestore`](instructions/17-stack-manipulation-instructions/02-stackrestore.md) | yes | `stackrestore` requires `sm_52` or higher. |
| 9.7.17.3. | [`alloca`](instructions/17-stack-manipulation-instructions/03-alloca.md) | yes | `alloca` requires `sm_52` or higher. |

## 9.7.18. Video Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.18.1. | [Scalar Video Instructions](instructions/18-video-instructions/01-scalar-video-instructions.md) | yes | `vadd`, `vsub`, `vabsdiff`, `vmin`, `vmax` require `sm_20` or higher. `vshl`, `vshr` require `sm_20` or higher. `vmad` requires `sm_20` or higher. `vset` requires `sm_20` or higher. |
| &nbsp;&nbsp;9.7.18.1.1. | ↳ [`vadd`, `vsub`, `vabsdiff`, `vmin`, `vmax`](instructions/18-video-instructions/01-scalar-video-instructions.md#scalar-video-instructions-vadd-vsub-vabsdiff-vmin-vmax) | yes | `vadd`, `vsub`, `vabsdiff`, `vmin`, `vmax` require `sm_20` or higher. |
| &nbsp;&nbsp;9.7.18.1.2. | ↳ [`vshl`, `vshr`](instructions/18-video-instructions/01-scalar-video-instructions.md#scalar-video-instructions-vshl-vshr) | yes | `vshl`, `vshr` require `sm_20` or higher. |
| &nbsp;&nbsp;9.7.18.1.3. | ↳ [`vmad`](instructions/18-video-instructions/01-scalar-video-instructions.md#scalar-video-instructions-vmad) | yes | `vmad` requires `sm_20` or higher. |
| &nbsp;&nbsp;9.7.18.1.4. | ↳ [`vset`](instructions/18-video-instructions/01-scalar-video-instructions.md#scalar-video-instructions-vset) | yes | `vset` requires `sm_20` or higher. |
| 9.7.18.2. | [SIMD Video Instructions](instructions/18-video-instructions/02-simd-video-instructions.md) | yes | `vadd2`, `vsub2`, `varvg2`, `vabsdiff2`, `vmin2`, `vmax2` require `sm_30` or higher. `vset2` requires `sm_30` or higher. `vadd4`, `vsub4`, `varvg4`, `vabsdiff4`, `vmin4`, `vmax4` require `sm_30` or higher. `vset4` req... |
| &nbsp;&nbsp;9.7.18.2.1. | ↳ [`vadd2`, `vsub2`, `vavrg2`, `vabsdiff2`, `vmin2`, `vmax2`](instructions/18-video-instructions/02-simd-video-instructions.md#simd-video-instructions-vadd2-vsub2-vavrg2-vabsdiff2-vmin2-vmax2) | yes | `vadd2`, `vsub2`, `varvg2`, `vabsdiff2`, `vmin2`, `vmax2` require `sm_30` or higher. |
| &nbsp;&nbsp;9.7.18.2.2. | ↳ [`vset2`](instructions/18-video-instructions/02-simd-video-instructions.md#simd-video-instructions-vset2) | yes | `vset2` requires `sm_30` or higher. |
| &nbsp;&nbsp;9.7.18.2.3. | ↳ [`vadd4`, `vsub4`, `vavrg4`, `vabsdiff4`, `vmin4`, `vmax4`](instructions/18-video-instructions/02-simd-video-instructions.md#simd-video-instructions-vadd4-vsub4-vavrg4-vabsdiff4-vmin4-vmax4) | yes | `vadd4`, `vsub4`, `varvg4`, `vabsdiff4`, `vmin4`, `vmax4` require `sm_30` or higher. |
| &nbsp;&nbsp;9.7.18.2.4. | ↳ [`vset4`](instructions/18-video-instructions/02-simd-video-instructions.md#simd-video-instructions-vset4) | yes | `vset4` requires `sm_30` or higher. |

## 9.7.19. Miscellaneous Instructions

| section | instruction | sm_120 | Target ISA notes |
|---|---|---|---|
| 9.7.19.1. | [`brkpt`](instructions/19-miscellaneous-instructions/01-brkpt.md) | yes | `brkpt` requires `sm_11` or higher. |
| 9.7.19.2. | [`nanosleep`](instructions/19-miscellaneous-instructions/02-nanosleep.md) | yes | `nanosleep` requires `sm_70` or higher. |
| 9.7.19.3. | [`pmevent`](instructions/19-miscellaneous-instructions/03-pmevent.md) | yes | pmevent supported on all target architectures. `pmevent.mask` requires `sm_20` or higher. |
| 9.7.19.4. | [`trap`](instructions/19-miscellaneous-instructions/04-trap.md) | yes | Supported on all target architectures. |
| 9.7.19.5. | [`setmaxnreg`](instructions/19-miscellaneous-instructions/05-setmaxnreg.md) | yes | Supported on following architectures: `sm_90a` `sm_100a` `sm_101a` `sm_120a` And is supported on following family-specific architectures from PTX ISA version 8.8: `sm_100f` or higher in the same family `sm_101f` or hi... |

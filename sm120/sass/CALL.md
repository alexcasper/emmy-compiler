# CALL (SM120 SASS)

**NVIDIA:** Call Function (Control Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: subroutine call (non-inlined funcs, TMA/mbarrier helper sequences) (category: Control flow)

Observed on sm_120: 4 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`
- `call`: `.func .noinline call`

12-bit opcode field (bits 0-11) values observed: `0x229`, `0xc2c`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 117 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
...000101.0.111000..00000.00000000000000000000000000000000000000
0000000000000000000000111100000000000000010101111111..000.000000
```

4 normalized operand form(s) observed:

### `CALL.REL.NOINC ($__internal_0_$__cuda_sm3x_div_rn_noftz_f32_slowpath)` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CALL.REL.NOINC ($__internal_0_$__cuda_sm3x_div_rn_noftz_f32_slowpath)` | `00000000000c7944 000fea0003c00000` | fdiv_rn |

### `CALL.ABS.NOINC R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CALL.ABS.NOINC R2` | `0000000002007343 001fea0003c00000` | cp_async_bulk_tma |

### `CALL.REL.NOINC ($__internal_0_$__cuda_sm_10x_mma_bit_internal_and_m16n8k256)` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CALL.REL.NOINC ($__internal_0_$__cuda_sm_10x_mma_bit_internal_and_m16n8k256)` | `00000000000c7944 022fea0003c00000` | bmma |

### `CALL.REL.NOINC ($k$fn)` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CALL.REL.NOINC ($k$fn)` | `0000000000087944 022fea0003c00000` | call |


# LEA (SM120 SASS)

**NVIDIA:** LOAD Effective Address (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: load effective address (a << s) + b (category: Integer)

Observed on sm_120: 12 instruction(s) across 11 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `lea`: `shl.b32 + add.s32`
- `lea64`: `pointer + (sign-extended s32 index << 2)`
- `vabsdiff2`: `vabsdiff2.u32.u32.u32 (observe)`
- `lds_sts`: `ld.shared / st.shared`
- `cp_async`: `cp.async.cg.shared.global + commit_group + wait_group`
- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `ldsm_trans`: `ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16`
- `stmatrix`: `stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)`
- `stmatrix_x4`: `stmatrix.sync.aligned.m8n8.x4.shared.b16`
- `cctll`: `prefetch.local.L1`

12-bit opcode field (bits 0-11) values observed: `0x881`, `0x883`, `0x884`.

## Encoding observations

**Constant bits across all 12 observed instance(s): 85 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
100010000...1110...00000....0000.0.00000000000000000000.000000..
1..1....00..........000.....0000000000000...0.111111.0..00000000
```

6 normalized operand form(s) observed:

### `LEA R, R, R, IMM` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LEA R5, R0, R5, 0x3` | `0000000500057211 004fca00078e18ff` | lea |
| `LEA R5, R5, R4, 0x18` | `0000000405057211 001fca00078ec0ff` | stmatrix |
| `LEA R0, R9, R0, 0x18` | `0000000009007211 001fca00078ec0ff` | stmatrix_x4 |
| `LEA R2, R2, R1, 0x2` | `0000000102027211 000fe200078e10ff` | cctll |

### `LEA R, R, UR, IMM` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LEA R5, R5, UR4, 0x2` | `0000000405057c11 000fca000f8e10ff` | lds_sts |
| `LEA R5, R5, UR4, 0x4` | `0000000405057c11 000fca000f8e20ff` | cp_async |
| `LEA R5, R5, UR4, 0x4` | `0000000405057c11 000fca000f8e20ff` | ldsm |
| `LEA R5, R5, UR4, 0x4` | `0000000405057c11 000fca000f8e20ff` | ldsm_trans |

### `LEA R, R, IMM, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LEA R0, R7, 0xc0800000, 0x17` | `c080000007007811 000fe200078eb8ff` | fdiv_rn |

### `LEA R, P, R, R, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LEA R4, P0, R6, R4, 0x2` | `0000000406047211 008fc800078010ff` | lea64 |

### `LEA.HI.X R, R, R, R, IMM, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LEA.HI.X R5, R6, R5, R9, 0x2, P0` | `0000000506057211 000fca00000f1409` | lea64 |

### `LEA.HI R, R, -R, R, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LEA.HI R0, R0, -R5, RZ, 0x10` | `8000000500007211 000fe400078f80ff` | vabsdiff2 |


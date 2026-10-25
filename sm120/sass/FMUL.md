# FMUL (SM120 SASS)

**NVIDIA:** FP32 Multiply (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP32 multiply (category: FP32)

Observed on sm_120: 13 instruction(s) across 9 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fmul`: `mul.f32`
- `fsetp_selp`: `setp.lt.f32 + selp.f32 (both arms computed)`
- `mufu_rcp`: `rcp.approx.f32`
- `mufu_rsqrt`: `rsqrt.approx.f32`
- `mufu_sqrt`: `sqrt.approx.f32`
- `mufu_lg2`: `lg2.approx.f32`
- `mufu_ex2`: `ex2.approx.f32`
- `mufu_sin`: `sin.approx.f32`
- `mufu_cos`: `cos.approx.f32`

12-bit opcode field (bits 0-11) values observed: `0x041`, `0x044`.

## Encoding observations

**Constant bits across all 13 observed instance(s): 91 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
000001000.0......0.00000.0.00000...0000..00.....0.000.0........0
00000000000000..0000001000000000000000000..100111111.0..00000000
```

4 normalized operand form(s) observed:

### `FMUL R, R, R` - 5 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FMUL R5, R0, R5` | `0000000500057220 004fca0000400000` | fmul |
| `FMUL R0, R0, R7` | `0000000700007220 008fca0000400000` | fsetp_selp |
| `FMUL R0, R0, R5` | `0000000500007220 000fcc0000400000` | mufu_rcp |
| `@!P0 FMUL R5, R5, R5` | `0000000505058220 001fca0000400000` | mufu_ex2 |

### `FMUL R, R, IMM` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@!P0 FMUL R0, R0, 16777216` | `4b80000000008820 000fc80000400000` | mufu_rsqrt |
| `@!P0 FMUL R5, R5, 4096` | `4580000005058820 001fca0000400000` | mufu_rsqrt |
| `@!P0 FMUL R0, R0, 16777216` | `4b80000000008820 000fc80000400000` | mufu_sqrt |
| `@!P0 FMUL R0, R0, 16777216` | `4b80000000008820 000fc80000400000` | mufu_lg2 |

### `FMUL R, R, IMM.IMM` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@!P0 FMUL R5, R5, 0.000244140625` | `3980000005058820 001fca0000400000` | mufu_sqrt |
| `@!P0 FMUL R0, R0, 0.5` | `3f00000000008820 000fc80000400000` | mufu_ex2 |

### `FMUL.R R, R, IMM.IMM` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FMUL.RZ R0, R0, 0.15915493667125701904` | `3e22f98300007820 004fc8000040c000` | mufu_sin |
| `FMUL.RZ R0, R0, 0.15915493667125701904` | `3e22f98300007820 004fc8000040c000` | mufu_cos |


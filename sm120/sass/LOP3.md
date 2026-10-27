# LOP3 (SM120 SASS)

**NVIDIA:** Logic Operation (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: 3-input bitwise logic (8-bit LUT) (category: Integer)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x12, 0x92 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2064)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 39 instruction(s) across 11 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `isetp_pred`: `setp.lt.s32 + selp.b32`
- `imnmx_from_selp`: `setp.lt.s32 + selp.b32 forming min()`
- `lop3`: `and/xor/or of 3 values`
- `f2fp_e4m3`: `cvt.rn.satfinite.e4m3x2.f32 (FP8)`
- `ldl_stl`: `dynamically indexed .local array`
- `ldc`: `ld.const with dynamic index`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`
- `brx`: `brx.idx (jump table)`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`
- `cctll`: `prefetch.local.L1`

12-bit opcode field (bits 0-11) values observed: `0x481`, `0x483`, `0x484`.

## Encoding observations

**Constant bits across all 39 observed instance(s): 50 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
010010000......0............0000................................
........0.......0...0001111.0000000000000.....111111.0..00.00000
```

5 normalized operand form(s) observed:

### `LOP3.LUT R, R, IMM, R, IMM, !P` - 27 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LOP3.LUT R7, R7, 0xff, RZ, 0xc0, !PT` | `000000ff07077812 000fe400078ec0ff` | fdiv_rn |
| `LOP3.LUT R5, R0, 0xffff, RZ, 0xc0, !PT` | `0000ffff00057812 000fca00078ec0ff` | f2fp_e4m3 |
| `LOP3.LUT R0, R0, 0x3f, RZ, 0xc0, !PT` | `0000003f00007812 004fe400078ec0ff` | ldl_stl |
| `LOP3.LUT R0, R0, 0xfc, RZ, 0xe2, !PT` | `000000fc00007812 000fc800078ee2ff` | ldc |
| ... 23 more instance(s) in results.json | | |

### `LOP3.LUT R, R, R, R, IMM, !P` - 5 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LOP3.LUT R0, R0, R7, RZ, 0xc0, !PT` | `0000000700007212 000fc800078ec0ff` | fdiv_rn |
| `@P0 LOP3.LUT R5, R0, R7, RZ, 0x3c, !PT` | `0000000700050212 000fca00078e3cff` | isetp_pred |
| `LOP3.LUT R0, R0, R7, RZ, 0x3c, !PT` | `0000000700007212 008fca00078e3cff` | imnmx_from_selp |
| `LOP3.LUT R5, R0, R4, R5, 0xfc, !PT` | `0000000400057212 004fca00078efc05` | lop3 |
| ... 1 more instance(s) in results.json | | |

### `LOP3.LUT P, R, R, IMM, R, IMM, !P` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LOP3.LUT P0, RZ, R9, 0x7fffffff, R8, 0xc8, !PT` | `7fffffff09ff7812 000fda000780c808` | fdiv_rn |
| `LOP3.LUT P2, RZ, R8, 0x7fffffff, RZ, 0xc0, !PT` | `7fffffff08ff7812 000fc8000784c0ff` | fdiv_rn |
| `LOP3.LUT P1, RZ, R9, 0x7fffffff, RZ, 0xc0, !PT` | `7fffffff09ff7812 000fc8000782c0ff` | fdiv_rn |

### `LOP3.LUT R, R.reuse, IMM, R, IMM, !P` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LOP3.LUT R2, R12.reuse, 0x88888888, RZ, 0xc0, !PT` | `888888880c027812 040fe400078ec0ff` | bmma |
| `LOP3.LUT R3, R13.reuse, 0x88888888, RZ, 0xc0, !PT` | `888888880d037812 040fe400078ec0ff` | bmma |
| `LOP3.LUT R5, R13.reuse, 0x22222222, RZ, 0xc0, !PT` | `222222220d057812 040fe400078ec0ff` | bmma |

### `LOP3.LUT R, R, UR, R, IMM, !P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LOP3.LUT R6, R6, UR6, RZ, 0xc0, !PT` | `0000000606067c12 001fc8000f8ec0ff` | agg_atomic |


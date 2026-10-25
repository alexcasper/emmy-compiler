# VIMNMX (SM120 SASS)

**NVIDIA:** SIMD Integer Minimum / Maximum (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: video-pipe integer min/max; emitted for PTX min.s32 and vabsdiff4 (IMNMX not seen on sm_120) (category: Integer)

Observed on sm_120: 4 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `imnmx`: `min.s32`
- `imnmx_from_selp`: `setp.lt.s32 + selp.b32 forming min()`
- `vabsdiff4`: `vabsdiff4.u32.u32.u32.add`

12-bit opcode field (bits 0-11) values observed: `0x124`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 114 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0001001001001110..100000.0.00000.0.00000000000000000000000000000
00000000.0.000000111111111.0000000000000010.0.11111100.000..0000
```

3 normalized operand form(s) observed:

### `VIMNMX.S32 R, R, R, P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `VIMNMX.S32 R5, R0, R5, PT` | `0000000500057248 004fca0003fe0100` | imnmx |
| `VIMNMX.S32 R5, R5, R0, PT` | `0000000005057248 000fca0003fe0100` | imnmx_from_selp |

### `VIMNMX.U8x4 R, R.reuse, R.reuse, !P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `VIMNMX.U8x4 R6, R0.reuse, R5.reuse, !PT` | `0000000500067248 0c4fe20007fe0400` | vabsdiff4 |

### `VIMNMX.U8x4 R, R, R, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `VIMNMX.U8x4 R5, R0, R5, PT` | `0000000500057248 000fca0003fe0400` | vabsdiff4 |


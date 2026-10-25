# F2I (SM120 SASS)

**NVIDIA:** Floating Point To Integer Conversion (Conversion Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: float-to-integer conversion (category: Conversion)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `f2i`: `cvt.rzi.s32.f32`
- `f2ip`: `cvt.rni.sat.s8.f32 (observe only)`

12-bit opcode field (bits 0-11) values observed: `0xa0c`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 125 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1010000011001110101000000000000000000000000000000000000000000000
000000001000.1..000001000000000000000000001001000111001000000000
```

2 normalized operand form(s) observed:

### `F2I.TRUNC.NTZ R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `F2I.TRUNC.NTZ R5, R0` | `0000000000057305 004e24000020f100` | f2i |

### `F2I.S8.NTZ R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `F2I.S8.NTZ R5, R0` | `0000000000057305 004e240000202100` | f2ip |


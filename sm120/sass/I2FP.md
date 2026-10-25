# I2FP (SM120 SASS)

**NVIDIA:** Integer to FP32 Convert and Pack (Conversion Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: integer-to-FP32 on the FMA pipe (category: Conversion)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `i2fp`: `cvt.rn.f32.s32`

12-bit opcode field (bits 0-11) values observed: `0xa24`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1010001001001110101000000000000000000000000000000000000000000000
0000000000101000000001000000000000000000010100111111001000000000
```

1 normalized operand form(s) observed:

### `I2FP.F32.S32 R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `I2FP.F32.S32 R5, R0` | `0000000000057245 004fca0000201400` | i2fp |


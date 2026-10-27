# I2IP (SM120 SASS)

**NVIDIA:** Integer To Integer Conversion and Packing (Conversion Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: pack integers to narrower integers (cvt.pack.sat) (category: Conversion)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `i2ip`: `cvt.pack.sat.s8.s32.b32`

12-bit opcode field (bits 0-11) values observed: `0x9c4`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1001110001001110101000000000000010100000000000000000000000000000
0010000000101000000000000000000000000000010100111111001000000000
```

1 normalized operand form(s) observed:

### `I2IP.S8.S32.SAT R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `I2IP.S8.S32.SAT R5, R0, R5, R4` | `0000000500057239 004fca0000001404` | i2ip |


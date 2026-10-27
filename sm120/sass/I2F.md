# I2F (SM120 SASS)

**NVIDIA:** Integer To Floating Point Conversion (Conversion Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: integer-to-float conversion (category: Conversion)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x5a, 0x106, 0x112 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2329)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `i2f`: `cvt.rn.f64.s32`
- `uniform_i2f`: `cvt.rn.f64.s32 on a warp-uniform value (uniform FP conversion, UI2F)`

12-bit opcode field (bits 0-11) values observed: `0x48b`, `0x48c`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 118 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
010010001...111000100000000000000.100000000000000000000000000000
000000000011100000000100000.0000000000000..0010.01110..000000000
```

2 normalized operand form(s) observed:

### `I2F.F64 R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `I2F.F64 R4, R4` | `0000000400047312 004e240000201c00` | i2f |

### `I2F.F64 R, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `I2F.F64 R4, UR6` | `0000000600047d12 002ea20008201c00` | uniform_i2f |


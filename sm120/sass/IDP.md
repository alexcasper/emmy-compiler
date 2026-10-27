# IDP (SM120 SASS)

**NVIDIA:** Integer Dot Product and Accumulate (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: integer dot product (dp4a); also part of vabsdiff4 emulation (category: Integer)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `idp`: `dp4a.s32.s32`
- `vabsdiff4`: `vabsdiff4.u32.u32.u32.add`

12-bit opcode field (bits 0-11) values observed: `0x643`, `0x644`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 110 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
011001000...111010100000.0.00000..100000000000000000000000000000
..1.....0..0000000000000000.00000000000001010011111100.000000000
```

2 normalized operand form(s) observed:

### `IDP.4A.S8.S8 R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IDP.4A.S8.S8 R5, R0, R5, R4` | `0000000500057226 004fca0000000604` | idp |

### `IDP.4A.U8.U8 R, R, UR, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IDP.4A.U8.U8 R5, R5, UR6, RZ` | `0000000605057c26 000fca00080000ff` | vabsdiff4 |


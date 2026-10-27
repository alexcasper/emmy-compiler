# IABS (SM120 SASS)

**NVIDIA:** Integer Absolute Value (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: integer absolute value (category: Integer)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x13, 0x4d ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1580)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 3 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `iabs`: `abs.s32`
- `vabsdiff2`: `vabsdiff2.u32.u32.u32 (observe)`

12-bit opcode field (bits 0-11) values observed: `0xc84`.

## Encoding observations

**Constant bits across all 3 observed instance(s): 119 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
11001000010011101.10000000000000...00000000000000000000000000000
00000000000000000000000000000000000000000...0.11111100.000000000
```

1 normalized operand form(s) observed:

### `IABS R, R` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IABS R5, R0` | `0000000000057213 004fca0000000000` | iabs |
| `IABS R7, R7` | `0000000700077213 000fe40000000000` | vabsdiff2 |
| `IABS R5, R0` | `0000000000057213 000fc60000000000` | vabsdiff2 |


# IMMA (SM120 SASS)

**NVIDIA:** Integer Matrix Multiply and Accumulate (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: integer (s8) mma.sync; also the tail of b1-mma emulation (no BMMA opcode seen on sm_120) (category: Tensor core (MMA))

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x237 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4520)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 9 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `imma`: `mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`

12-bit opcode field (bits 0-11) values observed: `0xec4`.

## Encoding observations

**Constant bits across all 9 observed instance(s): 111 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
111011000100111000..000000..00000....000000000000000000000000000
00..00000011.0.00000001000000000000000000.....111111000000000000
```

2 normalized operand form(s) observed:

### `IMMA.IMM.U8.U8 R, R.ROW, R.COL, R` - 8 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMMA.16832.U8.U8 R8, R8.ROW, R4.COL, R12` | `0000000408087237 000fe20000400c0c` | bmma |
| `IMMA.16832.U8.U8 R4, R4.ROW, R2.COL, R8` | `0000000204047237 000ff00000400c08` | bmma |
| `IMMA.16832.U8.U8 R4, R8.ROW, R24.COL, R4` | `0000001808047237 000ff00000400c04` | bmma |
| `IMMA.16832.U8.U8 R4, R8.ROW, R12.COL, R4` | `0000000c08047237 000ff00000400c04` | bmma |
| ... 4 more instance(s) in results.json | | |

### `IMMA.IMM.S8.S8 R, R.ROW, R.COL, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IMMA.16832.S8.S8 R4, R4.ROW, R8.COL, R12` | `0000000804047237 000fde0000405c0c` | imma |


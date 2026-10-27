# QMMA (SM120 SASS)

**NVIDIA:** FP8 Matrix Multiply and Accumulate Across a Warp (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP8 (e4m3/e5m2) mma.sync m16n8k32 (category: Tensor core (MMA))

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `qmma_e4m3`: `mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 (FP8)`
- `qmma_e5m2`: `mma.sync.aligned.m16n8k32.row.col.f32.e5m2.e5m2.f32 (FP8)`

12-bit opcode field (bits 0-11) values observed: `0x5e4`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 126 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0101111001001110000100000010000000110000000000000000000000000000
00010000001101..000000000000000000000000011110111111000000000000
```

2 normalized operand form(s) observed:

### `QMMA.IMM.F32.E4M3.E4M3 R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `QMMA.16832.F32.E4M3.E4M3 R8, R4, R12, R8` | `0000000c0408727a 000fde0000002c08` | qmma_e4m3 |

### `QMMA.IMM.F32.E5M2.E5M2 R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `QMMA.16832.F32.E5M2.E5M2 R8, R4, R12, R8` | `0000000c0408727a 000fde000000ec08` | qmma_e5m2 |


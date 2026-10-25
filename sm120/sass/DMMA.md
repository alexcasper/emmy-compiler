# DMMA (SM120 SASS)

**NVIDIA:** Matrix Multiply and Accumulate (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP64 mma.sync m8n8k4 (still present on sm_120) (category: Tensor core (MMA))

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `dmma`: `mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64 (FP64 MMA)`

12-bit opcode field (bits 0-11) values observed: `0xfc4`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1111110001001110001000000010000001100000000000000000000000000000
0010000000000000000000000000000000000000011110000111001000000000
```

1 normalized operand form(s) observed:

### `DMMA.8x8x4 R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `DMMA.8x8x4 R4, R4, R6, R4` | `000000060404723f 004e1e0000000004` | dmma |


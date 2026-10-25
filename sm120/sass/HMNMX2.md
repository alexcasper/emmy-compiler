# HMNMX2 (SM120 SASS)

**NVIDIA:** FP16 Minimum / Maximum (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: packed FP16x2 min/max (category: FP16 (packed half2))

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `hmnmx2`: `min.f16x2`

12-bit opcode field (bits 0-11) values observed: `0x024`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0000001001001110101000000000000010100000000000000000000000000000
0000000000000000000000011100000000000000010100111111001000000000
```

1 normalized operand form(s) observed:

### `HMNMX2 R, R, R, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HMNMX2 R5, R0, R5, PT` | `0000000500057240 004fca0003800000` | hmnmx2 |


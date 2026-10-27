# LDL (SM120 SASS)

**NVIDIA:** Load within Local Memory Window (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: local load (category: Load / store)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `ldl_stl`: `dynamically indexed .local array`
- `cctll`: `prefetch.local.L1`

12-bit opcode field (bits 0-11) values observed: `0xc19`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 125 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1100000110011110.1.0000001.0000000000000000000000000000000000000
0000000000010000000010000000000000000000000101010111000000000000
```

1 normalized operand form(s) observed:

### `LDL R, [R]` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LDL R7, [R6]` | `0000000006077983 000ea80000100800` | ldl_stl |
| `LDL R2, [R2]` | `0000000002027983 000ea80000100800` | cctll |


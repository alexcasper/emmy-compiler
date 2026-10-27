# STL (SM120 SASS)

**NVIDIA:** Store to Local Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: local store (category: Load / store)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `ldl_stl`: `dynamically indexed .local array`
- `cctll`: `prefetch.local.L1`

12-bit opcode field (bits 0-11) values observed: `0xe1c`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 123 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
11100001110011100000000010.0000000.00000000000000000000000000000
00000000000100000000100000000000000000000.0101111111000..0000000
```

1 normalized operand form(s) observed:

### `STL [R], R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STL [R5], R4` | `0000000405007387 010fe80000100800` | ldl_stl |
| `STL [R1], R0` | `0000000001007387 008fea0000100800` | cctll |


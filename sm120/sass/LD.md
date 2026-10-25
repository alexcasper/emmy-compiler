# LD (SM120 SASS)

**NVIDIA:** Load from generic Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: generic-address load (category: Load / store)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `ld_generic`: `ld (generic pointer)`

12-bit opcode field (bits 0-11) values observed: `0x019`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0000000110011110101000000010000000100000000000000000000000000000
0000000010011000000010000011000000000000000101010111001000000000
```

1 normalized operand form(s) observed:

### `LD.E R, desc[UR][R.IMM]` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LD.E R5, desc[UR4][R4.64]` | `0000000404057980 004ea8000c101900` | ld_generic |


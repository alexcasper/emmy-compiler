# STS (SM120 SASS)

**NVIDIA:** Store to Shared Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: shared store (category: Load / store)

Observed on sm_120: 3 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `lds_sts`: `ld.shared / st.shared`
- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `ldsm_trans`: `ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16`

12-bit opcode field (bits 0-11) values observed: `0x11c`.

## Encoding observations

**Constant bits across all 3 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0001000111001110000000001010000000000000000000000000000000000000
0000000000010000000000000000000000000000010001111111001000000000
```

1 normalized operand form(s) observed:

### `STS [R], R` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `STS [R5], R0` | `0000000005007388 004fe20000000800` | lds_sts |
| `STS [R5], R0` | `0000000005007388 004fe20000000800` | ldsm |
| `STS [R5], R0` | `0000000005007388 004fe20000000800` | ldsm_trans |


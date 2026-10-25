# TXQ (SM120 SASS)

**NVIDIA:** Texture Query (Texture Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: texture query (txq/suq; sm_120 form: 'TXQ RZ, R5, R5, TEX_HEADER_DIMENSION, UR4, ...') (category: Texture / surface)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `txq`: `txq.width.b32`
- `suq`: `suq.width.b32`

12-bit opcode field (bits 0-11) values observed: `0xf6f`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1111011011111110101000001010000000000000001000000000000000000000
1111111110000000000000000001000000000000010001101111100000000000
```

1 normalized operand form(s) observed:

### `TXQ R, R, R, TEX_HEADER_DIMENSION, UR, IMM, IMM` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `TXQ RZ, R5, R5, TEX_HEADER_DIMENSION, UR4, 0x0, 0x1` | `0000040005057f6f 001f6200080001ff` | txq |
| `TXQ RZ, R5, R5, TEX_HEADER_DIMENSION, UR4, 0x0, 0x1` | `0000040005057f6f 001f6200080001ff` | suq |


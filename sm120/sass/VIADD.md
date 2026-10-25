# VIADD (SM120 SASS)

**NVIDIA:** SIMD Integer Addition (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: video-pipe integer add; emitted for PTX vabsdiff4.u32 (VABSDIFF4 not seen on sm_120) (category: Integer)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `vabsdiff4`: `vabsdiff4.u32.u32.u32.add`

12-bit opcode field (bits 0-11) values observed: `0x6c4`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0110110001001110101000000110000010100000000000000000000000000001
0000000000010000000000000000000000000000010100111111000000000000
```

1 normalized operand form(s) observed:

### `VIADD.U8x4 R, R, -R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `VIADD.U8x4 R5, R6, -R5` | `8000000506057236 000fca0000000800` | vabsdiff4 |


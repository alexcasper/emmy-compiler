# ULOP3 (SM120 SASS)

**NVIDIA:** Uniform Logic Operation (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform 3-input logic (category: Uniform datapath)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0x494`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0100100101001110001000000010000010100000000000000000000000000000
1111111100111100011100011111000000000000000100111111000000000000
```

1 normalized operand form(s) observed:

### `ULOP3.LUT UR, UR, UR, UR, IMM, !UP` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ULOP3.LUT UR4, UR4, UR5, URZ, 0x3c, !UPT` | `0000000504047292 000fc8000f8e3cff` | uniform_alu |


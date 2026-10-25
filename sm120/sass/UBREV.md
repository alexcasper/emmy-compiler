# UBREV (SM120 SASS)

**NVIDIA:** Uniform Bit Reverse (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform bit reverse (category: Uniform datapath)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0x7d4`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0111110101001110101000000000000000100000000000000000000000000000
0000000000000000000000000001000000000000000100111111000000000000
```

1 normalized operand form(s) observed:

### `UBREV UR, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UBREV UR5, UR4` | `00000004000572be 000fc80008000000` | uniform_alu |


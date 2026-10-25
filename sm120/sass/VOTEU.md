# VOTEU (SM120 SASS)

**NVIDIA:** Voting across SIMD Thread Group with Results in Uniform Destination (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: warp vote to uniform register (VOTEU.ANY for activemask) (category: Uniform datapath)

Observed on sm_120: 3 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`
- `agg_red`: `red.global.add.u32 to a warp-uniform address (warp-aggregated)`
- `activemask`: `activemask.b32`

12-bit opcode field (bits 0-11) values observed: `0x611`.

## Encoding observations

**Constant bits across all 3 observed instance(s): 124 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
01100001000111100.1000000000000000000000000000000000000000000000
00000000100000000111000111000000000000000..00.111111000000000000
```

1 normalized operand form(s) observed:

### `VOTEU.ANY UR, UP, P` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `VOTEU.ANY UR6, UPT, PT` | `0000000000067886 000fe200038e0100` | agg_atomic |
| `VOTEU.ANY UR6, UPT, PT` | `0000000000067886 000fe200038e0100` | agg_red |
| `VOTEU.ANY UR4, UPT, PT` | `0000000000047886 000fc400038e0100` | activemask |


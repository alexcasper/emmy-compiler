# POPC (SM120 SASS)

**NVIDIA:** Population count (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: population count (category: Integer)

Observed on sm_120: 5 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `popc`: `popc.b32`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`
- `agg_red`: `red.global.add.u32 to a warp-uniform address (warp-aggregated)`
- `activemask`: `activemask.b32`

12-bit opcode field (bits 0-11) values observed: `0x90b`, `0x90c`.

## Encoding observations

**Constant bits across all 5 observed instance(s): 114 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
100100001...11101...0000000000000..00000000000000000000000000000
000000000000000000000000000.0000000000000...01.0011100.000000000
```

2 normalized operand form(s) observed:

### `POPC R, UR` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `POPC R9, UR6` | `0000000600097d09 000e620008000000` | agg_atomic |
| `POPC R5, UR6` | `0000000600057d09 000e680008000000` | agg_red |
| `POPC R5, UR4` | `0000000400057d09 000e620008000000` | activemask |

### `POPC R, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `POPC R5, R0` | `0000000000057309 004e240000000000` | popc |
| `POPC R11, R6` | `00000006000b7309 000e220000000000` | agg_atomic |


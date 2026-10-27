# REDG (SM120 SASS)

**NVIDIA:** Reduction Operation on Generic Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: red.global reduction (no return) - sm_120 name for sm89's RED (category: Atomics / reductions)

Observed on sm_120: 3 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `red`: `red.global.add.u32 (no result)`
- `red_v2_f32`: `red.global.v2.add.f32 (vector reduction, sm_90+)`
- `agg_red`: `red.global.add.u32 to a warp-uniform address (warp-aggregated)`

12-bit opcode field (bits 0-11) values observed: `0x659`, `0x719`.

## Encoding observations

**Constant bits across all 3 observed instance(s): 116 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
011.0.011001...00000000001000000.01000000000.0.00000000000000000
0010000010.0.1110100100000110000000000000100011111110..000000000
```

2 normalized operand form(s) observed:

### `REDG.E.ADD.STRONG.GPU desc[UR][R.IMM], R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `REDG.E.ADD.STRONG.GPU desc[UR4][R2.64], R5` | `000000050200798e 004fe2000c12e104` | red |
| `@P0 REDG.E.ADD.STRONG.GPU desc[UR4][R2.64], R5` | `000000050200098e 002fe2000c12e104` | agg_red |

### `REDG.E.ADD.F32x2.FTZ.RN.STRONG.GPU desc[UR][R.IMM+IMM], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `REDG.E.ADD.F32x2.FTZ.RN.STRONG.GPU desc[UR4][R2.64+0x50], R4` | `00005004020079a6 004fe2000c12f504` | red_v2_f32 |


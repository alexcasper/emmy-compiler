# LEPC (SM120 SASS)

**NVIDIA:** Load Effective PC (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: load effective PC (call sites) (category: Movement)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x729`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0111001010011110001010000000100000000000000000000000000000000000
0000000000000000000000000000000000000000011100111111000000000000
```

1 normalized operand form(s) observed:

### `LEPC R, (L)` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `LEPC R20, (.L_x_1)` | `000000001014794e 000fce0000000000` | cp_async_bulk_tma |


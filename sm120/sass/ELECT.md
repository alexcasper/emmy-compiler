# ELECT (SM120 SASS)

**NVIDIA:** Elect a Leader Thread (Control Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: elect.sync - elect one active lane (new name; sm89-era name: none, feature is sm_90+) (category: Predicate / compare)

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `elect_sync`: `elect.sync (sm_90+)`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0xf41`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 114 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
111101000001...0.11.....0000000000000000000000000000000000000000
000000000000000001..00011100000000000000010...111111000000000000
```

1 normalized operand form(s) observed:

### `ELECT P, UR, P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ELECT PT, UR6, PT` | `000000000006782f 000fe200038e0000` | elect_sync |
| `@P0 ELECT P1, URZ, PT` | `0000000000ff082f 000fda0003820000` | cp_async_bulk_tma |


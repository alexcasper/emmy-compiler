# UBLKPF (SM120 SASS)

**NVIDIA:** Bulk Data Prefetch (Tensor Memory Access Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: cp.async.bulk.prefetch.L2.global (category: Load / store)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async_bulk_prefetch`: `cp.async.bulk.prefetch.L2.global (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x3dc`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0011110111001110000000000110000000000000000000000000000000000000
0010000000000000000000000001000000000000000011111000000000000000
```

1 normalized operand form(s) observed:

### `UBLKPF.L2 [UR], UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UBLKPF.L2 [UR6], UR4` | `00000000060073bc 0001f00008000004` | cp_async_bulk_prefetch |


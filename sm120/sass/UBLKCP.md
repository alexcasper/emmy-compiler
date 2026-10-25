# UBLKCP (SM120 SASS)

**NVIDIA:** Bulk Data Copy (Tensor Memory Access Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: cp.async.bulk (TMA) bulk copy; sm_120 name for the sm_90 TMA copy (plus SYNCS/LDGSTS around it) (category: Load / store)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x5dc`.

## Encoding observations

**Constant bits across all 1 observed instance(s): 128 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0101110111001110000000000110000001100100000000000000000000000000
0010000001000000000000000001000000000000001001111000000000000000
```

1 normalized operand form(s) observed:

### `UBLKCP.S.G [UR], [UR], UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UBLKCP.S.G [UR38], [UR6], UR4` | `00000026060073ba 0001e40008000204` | cp_async_bulk_tma |


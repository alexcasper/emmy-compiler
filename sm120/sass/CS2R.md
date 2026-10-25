# CS2R (SM120 SASS)

**NVIDIA:** Move Special Register to Register (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: special register pair to registers: %clock64, %globaltimer (SR_GLOBALTIMERLO) (category: Movement)

Observed on sm_120: 4 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cs2r`: `mov.u64 %clock64`
- `globaltimer`: `mov.u64 %globaltimer`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `bssy_bsync`: `divergent loop exit followed by a warp-synchronous op`

12-bit opcode field (bits 0-11) values observed: `0xa01`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 118 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
10100000000111100.1.00000000000000000000000000000000000000000000
00000000....1.1.10000000000000000000000001.100111111.00000000000
```

2 normalized operand form(s) observed:

### `CS2R R, SR` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CS2R R4, SR_CLOCKLO` | `0000000000047805 000fca0000015000` | cs2r |
| `CS2R R4, SR_GLOBALTIMERLO` | `0000000000047805 000fca0000015200` | globaltimer |

### `CS2R R, SRZ` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `CS2R R12, SRZ` | `00000000000c7805 000fce000001ff00` | cp_async_bulk_tma |
| `CS2R R6, SRZ` | `0000000000067805 001fce000001ff00` | bssy_bsync |


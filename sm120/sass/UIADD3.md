# UIADD3 (SM120 SASS)

**NVIDIA:** Uniform Integer Addition (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform 3-input add (category: Uniform datapath)

Observed on sm_120: 7 instruction(s) across 5 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `mbarrier_red`: `mbarrier.arrive.release.cluster.shared::cta.b64 (sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0x091`.

## Encoding observations

**Constant bits across all 7 observed instance(s): 87 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0000100100011110..100.00..100000.0..............................
11111111.00001111111111111110000000000000.0...111111000000000000
```

3 normalized operand form(s) observed:

### `UIADD3 UR, UP, UP, -UR, IMM, UR` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UIADD3 UR4, UPT, UPT, -UR4, 0x100000, URZ` | `0010000004047890 000fc8000fffe1ff` | cp_async_bulk_tma |
| `UIADD3 UR4, UPT, UPT, -UR5, 0x100000, URZ` | `0010000005047890 000fc8000fffe1ff` | mbarrier_red |
| `UIADD3 UR4, UPT, UPT, -UR4, 0x100000, URZ` | `0010000004047890 000fc8000fffe1ff` | st_async |

### `UIADD3 UR, UP, UP, UR, IMM, UR` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UIADD3 UR39, UPT, UPT, UR6, 0x1000, URZ` | `0000100006277890 000fe2000fffe0ff` | cp_async_bulk_tma |
| `UIADD3 UR7, UPT, UPT, UR6, 0x1000, URZ` | `0000100006077890 000fe2000fffe0ff` | st_async |

### `UIADD3 UR, UP, UP, UR, -IMM, UR` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UIADD3 UR6, UPT, UPT, UR7, -0x3, URZ` | `fffffffd07067890 000fd8000fffe0ff` | uniform_loop |
| `UIADD3 UR7, UPT, UPT, UR6, -0x3, URZ` | `fffffffd06077890 000fd8000fffe0ff` | s2ur_loop |


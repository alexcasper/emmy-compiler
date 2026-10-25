# USHF (SM120 SASS)

**NVIDIA:** Uniform Funnel Shift (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform shift (category: Uniform datapath)

Observed on sm_120: 8 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `mbarrier_red`: `mbarrier.arrive.release.cluster.shared::cta.b64 (sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`
- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0x991`.

## Encoding observations

**Constant bits across all 8 observed instance(s): 104 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1001100100011110.0100000..1.......0.0000000000000000000000000000
1.1.....01.0.000.000000000010000000000000.0.0.11111100.000000000
```

3 normalized operand form(s) observed:

### `USHF.L.U32 UR, UR, IMM, UR` - 6 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `USHF.L.U32 UR5, UR4, 0xb, URZ` | `0000000b04057899 000fe200080006ff` | cp_async_bulk_tma |
| `USHF.L.U32 UR4, UR4, 0x1, URZ` | `0000000104047899 000fe200080006ff` | cp_async_bulk_tma |
| `USHF.L.U32 UR5, UR4, 0xb, URZ` | `0000000b04057899 000fe200080006ff` | mbarrier_red |
| `USHF.L.U32 UR5, UR4, 0xb, URZ` | `0000000b04057899 000fe200080006ff` | st_async |

### `USHF.L.U64.HI UR, UR, IMM, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `USHF.L.U64.HI UR4, UR4, 0x8, URZ` | `0000000804047899 000fc800080102ff` | cp_async_bulk_tma |

### `USHF.R.U32.HI UR, UR, IMM, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `USHF.R.U32.HI UR4, URZ, 0x3, UR5` | `00000003ff047899 004fc80008011605` | uniform_alu |


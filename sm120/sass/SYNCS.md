# SYNCS (SM120 SASS)

**NVIDIA:** Sync Unit (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: async-ops synchronize: emitted for cp.async.bulk / st.async / mbarrier sequences (new on sm_120) (category: Synchronization / barriers)

Observed on sm_120: 7 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `mbarrier_red`: `mbarrier.arrive.release.cluster.shared::cta.b64 (sm_90+)`
- `st_async`: `st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x4da`, `0xe59`, `0xe5a`.

## Encoding observations

**Constant bits across all 7 observed instance(s): 82 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
.1.0.10110..1110.........11.............000000000000000000000000
...00.00.000.0000....00000010000000000000..001......00.000000000
```

4 normalized operand form(s) observed:

### `SYNCS.EXCH.IMM UR, [UR], UR` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SYNCS.EXCH.64 URZ, [UR39], UR4` | `0000000427ff75b2 0003220008000100` | cp_async_bulk_tma |
| `SYNCS.EXCH.64 URZ, [UR6], UR4` | `0000000406ff75b2 0002a40008000100` | mbarrier_red |
| `SYNCS.EXCH.64 URZ, [UR7], UR4` | `0000000407ff75b2 0000a40008000100` | st_async |

### `SYNCS.PHASECHK.TRANS64.TRYWAIT P, [UR], R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SYNCS.PHASECHK.TRANS64.TRYWAIT P0, [UR39], RZ` | `000000ffff0075a7 000e240008001127` | cp_async_bulk_tma |
| `SYNCS.PHASECHK.TRANS64.TRYWAIT PT, [UR7], RZ` | `000000ffff0075a7 000fe600080e1107` | st_async |

### `SYNCS.ARRIVE.TRANS64 R, [UR], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SYNCS.ARRIVE.TRANS64 RZ, [UR39], R0` | `00000000ffff79a7 000fe20008000027` | cp_async_bulk_tma |

### `SYNCS.ARRIVE.TRANS64.A1T0 R, [UR], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SYNCS.ARRIVE.TRANS64.A1T0 RZ, [UR6], RZ` | `000000ffffff79a7 004fe20008100006` | mbarrier_red |


# UISETP (SM120 SASS)

**NVIDIA:** Uniform Integer Compare and Set Uniform Predicate (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: uniform compare to uniform predicate (category: Uniform datapath)

Observed on sm_120: 4 instruction(s) across 4 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cluster_barrier`: `barrier.cluster.arrive/wait.aligned`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0x311`, `0x314`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 110 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
001100010.0.111000000000..1000001.......000000000000000000000000
000011100.00...00000111111010000000000000100..11111100.000000000
```

4 normalized operand form(s) observed:

### `UISETP.EQ.U32.AND UP, UP, UR, IMM, UP` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UISETP.EQ.U32.AND UP0, UPT, UR6, 0x1, UPT` | `000000010600788c 004fd2000bf02070` | cluster_barrier |

### `UISETP.NE.U32.AND UP, UP, UR, UR, UP` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UISETP.NE.U32.AND UP0, UPT, UR4, UR7, UPT` | `000000070400728c 000fd2000bf05070` | cp_async_bulk_tma |

### `UISETP.GT.AND UP, UP, UR, UR, UP` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UISETP.GT.AND UP0, UPT, UR7, URZ, UPT` | `000000ff0700728c 004fe2000bf04270` | uniform_loop |

### `UISETP.GT.U32.AND UP, UP, UR, UR, UP` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `UISETP.GT.U32.AND UP0, UPT, UR6, URZ, UPT` | `000000ff0600728c 004fe2000bf04070` | s2ur_loop |


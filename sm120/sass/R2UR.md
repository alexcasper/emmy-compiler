# R2UR (SM120 SASS)

**NVIDIA:** Move from Vector Register to a Uniform Register (Uniform Datapath Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: register to uniform register (category: Movement)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x2ca, 0x3c2 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2688)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 4 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `cp_async_bulk_prefetch`: `cp.async.bulk.prefetch.L2.global (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0x534`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 116 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0101001101001000.1100000..00.00000000000000000000000000000000000
00000000000000000....00.000000000000000000.0..111111000000000000
```

3 normalized operand form(s) observed:

### `R2UR.BROADCAST UR, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@P1 R2UR.BROADCAST UR6, R16` | `00000000100612ca 000fe400008e0000` | cp_async_bulk_tma |
| `@P1 R2UR.BROADCAST UR7, R17` | `00000000110712ca 000fe400008e0000` | cp_async_bulk_tma |

### `R2UR P, UR, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@P1 R2UR P0, UR6, R2` | `00000000020612ca 000fd00000000000` | cp_async_bulk_prefetch |

### `R2UR.OR P, UR, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@P1 R2UR.OR P0, UR7, R3` | `00000000030712ca 000fd00000100000` | cp_async_bulk_prefetch |


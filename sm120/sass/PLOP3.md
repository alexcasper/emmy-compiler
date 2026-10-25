# PLOP3 (SM120 SASS)

**NVIDIA:** Predicate Logic Operation (Predicate Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: 3-input predicate logic (category: Predicate / compare)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x81c, 0x89c ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2616)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 21 instruction(s) across 6 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`
- `cp_async_bulk_prefetch`: `cp.async.bulk.prefetch.L2.global (sm_90+)`
- `diverge`: `data-dependent loop`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0x381`.

## Encoding observations

**Constant bits across all 21 observed instance(s): 97 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0011100000011...........0000000000000000000000000000000000000000
...01110........0.00111...000000000000000.....111111000000000000
```

1 normalized operand form(s) observed:

### `PLOP3.LUT P, P, P, P, P, IMM, IMM` - 21 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `PLOP3.LUT P0, PT, P0, P1, PT, 0xf8, 0x8f` | `00000000008f781c 000fda0000703f70` | fdiv_rn |
| `PLOP3.LUT P0, PT, PT, PT, PT, 0x80, 0x8` | `000000000008781c 000fe20003f0f070` | cp_async_bulk_tma |
| `PLOP3.LUT P1, PT, PT, PT, PT, 0x80, 0x8` | `000000000008781c 000fe20003f2f070` | cp_async_bulk_prefetch |
| `PLOP3.LUT P0, PT, PT, PT, PT, 0x80, 0x8` | `000000000008781c 000fc60003f0f070` | diverge |
| ... 17 more instance(s) in results.json | | |


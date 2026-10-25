# SEL (SM120 SASS)

**NVIDIA:** Select Source with Predicate (Movement Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: select by predicate (integer) (category: Movement)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x7, 0x87 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2491)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 6 instruction(s) across 5 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fset`: `set.lt.u32.f32`
- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `hsetp2`: `setp.lt.f16x2`
- `qspc`: `isspacep.shared`
- `cp_async_bulk_tma`: `cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)`

12-bit opcode field (bits 0-11) values observed: `0xe01`, `0xe04`.

## Encoding observations

**Constant bits across all 6 observed instance(s): 74 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
111000000.0.1..0...00000........1...............................
000000000000000000000000.0.00000000000000...0.111111.00.00000000
```

2 normalized operand form(s) observed:

### `SEL R, R, IMM, !P` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SEL R5, RZ, 0xffffffff, !P0` | `ffffffffff057807 000fca0004000000` | fset |
| `SEL R0, RZ, 0x1, !P0` | `00000001ff007807 000fca0004000000` | fdiv_rn |
| `SEL R7, RZ, 0x1, !P0` | `00000001ff077807 001fca0004000000` | qspc |
| `SEL R3, RZ, 0x1, !P0` | `00000001ff037807 001fca0004000000` | cp_async_bulk_tma |

### `SEL R, R, R, P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SEL R7, R8, RZ, P2` | `000000ff08077207 000fe40001000000` | fdiv_rn |
| `@P1 SEL R7, R0, R5, P0` | `0000000500071207 008fca0000000000` | hsetp2 |


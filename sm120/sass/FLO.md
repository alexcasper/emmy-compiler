# FLO (SM120 SASS)

**NVIDIA:** Find Leading One (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: find leading one (bfind/clz) (category: Integer)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0xbd, 0x100 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1561)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 4 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `flo`: `bfind.u32 / clz.b32`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`
- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`

12-bit opcode field (bits 0-11) values observed: `0x00b`, `0x00c`.

## Encoding observations

**Constant bits across all 4 observed instance(s): 112 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
000000001...1110.0.00000000000000..00000000000000000000000000000
000000000000000001110000000.0000000000000...01...11100..00000000
```

2 normalized operand form(s) observed:

### `FLO.U32 R, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FLO.U32 R0, R0` | `0000000000007300 004fe200000e0000` | flo |
| `FLO.U32 R5, R4` | `0000000400057300 008e2400000e0000` | flo |

### `FLO.U32 R, UR` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FLO.U32 R0, UR6` | `0000000600007d00 000e2800080e0000` | agg_atomic |
| `FLO.U32 R5, UR4` | `0000000400057d00 000ee600080e0000` | uniform_alu |


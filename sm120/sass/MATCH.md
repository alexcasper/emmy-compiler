# MATCH (SM120 SASS)

**NVIDIA:** Match Register Values Across Thread Group (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: warp match.any (category: Predicate / compare)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x3a1 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4493)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `match`: `match.any.sync.b32`

12-bit opcode field (bits 0-11) values observed: `0x85c`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1000010111001110101000000000000000000000000000000000000000000000
0000000000000001011100000000000000000000001001000111001000000000
```

1 normalized operand form(s) observed:

### `MATCH.ANY R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MATCH.ANY R5, R0` | `00000000000573a1 004e2400000e8000` | match |


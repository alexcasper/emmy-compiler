# VOTE (SM120 SASS)

**NVIDIA:** Vote Across SIMT Thread Group (Miscellaneous Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: warp vote (ballot/all/any) (category: Predicate / compare)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x806, 0x886 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4465)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 2 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `vote`: `vote.sync.ballot.b32`
- `atoms`: `atom.shared.add.u32`

12-bit opcode field (bits 0-11) values observed: `0x601`.

## Encoding observations

**Constant bits across all 2 observed instance(s): 122 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0110000000011110.01000000000000000000000000000000000000000000000
00000000100000000111000...00000000000000010.0.111111000000000000
```

1 normalized operand form(s) observed:

### `VOTE.ANY R, P, P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `VOTE.ANY R5, PT, P0` | `0000000000057806 000fca00000e0100` | vote |
| `VOTE.ANY R4, PT, PT` | `0000000000047806 000fe200038e0100` | atoms |


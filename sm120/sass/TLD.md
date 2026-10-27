# TLD (SM120 SASS)

**NVIDIA:** Texture Load (Texture Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: texel fetch (tex.1d integer coords) (category: Texture / surface)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x367, 0xb66, 0xd67 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2956)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `tld`: `tex.1d.v4.s32.s32 (integer coords)`

12-bit opcode field (bits 0-11) values observed: `0x66f`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0110011011111110101000000000000011111111001000001111111100000000
1111111110000000011110000001000000000000001001101111001000000000
```

1 normalized operand form(s) observed:

### `TLD.LZ R, R, R, UR, 1D, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `TLD.LZ RZ, R5, R0, UR4, 1D, 0x1` | `00ff04ff00057f66 004f6400081e01ff` | tld |


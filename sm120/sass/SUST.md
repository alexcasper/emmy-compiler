# SUST (SM120 SASS)

**NVIDIA:** Surface Store (Surface Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: surface store (category: Texture / surface)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **differ**. NAK encodes 0x99c, 0x99e ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3359)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `sust`: `sust.b.2d.b32.trap`

12-bit opcode field (bits 0-11) values observed: `0xb9f`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1011100111111110000000000010000000000000001000001111111100001110
0000000010010101000010000001000000000000001001111000001000000000
```

1 normalized operand form(s) observed:

### `SUST.D.BA.2D.STRONG.SM.TRAP [R], R, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SUST.D.BA.2D.STRONG.SM.TRAP [R4], R0, UR4` | `70ff040004007f9d 0041e4000810a900` | sust |


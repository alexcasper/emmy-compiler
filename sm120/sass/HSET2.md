# HSET2 (SM120 SASS)

**NVIDIA:** FP16 Compare And Set (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: packed FP16x2 compare writing a mask (category: FP16 (packed half2))

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x33 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1403)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `hset2`: `set.lt.f16x2.f16x2`

12-bit opcode field (bits 0-11) values observed: `0xcc4`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1100110001001110101000000000000010100000000000000000000000000000
0000000100001000000000011100000000000000010100111111001000000000
```

1 normalized operand form(s) observed:

### `HSET2.BF.LT.AND R, R, R, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `HSET2.BF.LT.AND R5, R0, R5, PT` | `0000000500057233 004fca0003801080` | hset2 |


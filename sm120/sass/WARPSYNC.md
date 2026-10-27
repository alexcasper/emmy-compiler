# WARPSYNC (SM120 SASS)

**NVIDIA:** Synchronize Threads in Warp (Control Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: warp sync (bar.warp.sync) (category: Control flow)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x148 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L4234)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `warpsync`: `bar.warp.sync with partial mask`

12-bit opcode field (bits 0-11) values observed: `0x12c`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0001001011001110000000000100000000000000000000000000000000000000
0000000000000000000000011100000000000000010101111111000001000000
```

1 normalized operand form(s) observed:

### `WARPSYNC R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `WARPSYNC R2` | `0000000002007348 020fea0003800000` | warpsync |


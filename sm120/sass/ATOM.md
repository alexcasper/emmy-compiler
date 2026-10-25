# ATOM (SM120 SASS)

**NVIDIA:** Atomic Operation on Generic Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: generic atomic with return (category: Atomics / reductions)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **NAK op maps to ATOMG/ATOMS/REDG**. NAK encodes 0x38c, 0x38d, 0x3a8, 0x3a9, 0x98c, 0x98e, 0x9a3, 0x9a6, 0x9a8 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L3777)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `atom_generic`: `atom.add.u32 (generic)`

12-bit opcode field (bits 0-11) values observed: `0x519`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
0101000110011110101000000010000011100000000000000000000000000001
0010000010001111011110000001000000000000000101010111001000000000
```

1 normalized operand form(s) observed:

### `ATOM.E.ADD.STRONG.GPU P, R, desc[UR][R.IMM], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ATOM.E.ADD.STRONG.GPU PT, R5, desc[UR4][R4.64], R7` | `800000070405798a 004ea800081ef104` | atom_generic |


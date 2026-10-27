# RET (SM120 SASS)

**NVIDIA:** Return From Subroutine (Control Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: return from subroutine (category: Control flow)

Observed on sm_120: 3 instruction(s) across 3 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`
- `call`: `.func .noinline call`

12-bit opcode field (bits 0-11) values observed: `0x0a9`.

## Encoding observations

**Constant bits across all 3 observed instance(s): 117 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
000010101001111000...0..0..0000000.11111111111111111111111111111
111111111111111111000011110000000000000001.1..111111000000000000
```

1 normalized operand form(s) observed:

### `RET.REL.NODEC R (k)` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `RET.REL.NODEC R2 (k)` | `fffffff802087950 000fea0003c3ffff` | fdiv_rn |
| `RET.REL.NODEC R2 (k)` | `fffffff802947950 000fde0003c3ffff` | bmma |
| `RET.REL.NODEC R4 (k)` | `fffffffc04cc7950 000fea0003c3ffff` | call |


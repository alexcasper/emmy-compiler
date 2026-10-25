# SURED (SM120 SASS)

**NVIDIA:** Reduction Op on Surface Memory (Surface Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: surface reduction (no return) (category: Texture / surface)

Observed on sm_120: 1 instruction(s) across 1 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `sured`: `sured.b.add.2d.u32.trap`

12-bit opcode field (bits 0-11) values observed: `0xf9f`.

## Encoding observations

**Single instance observed: all 128 bits are trivially 'constant'** and carry no information beyond this one encoding (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
1111100111111110000000000010000000000000001000001111111100001110
0000000010000010100010000001000000000000001001111000001000000000
```

1 normalized operand form(s) observed:

### `SURED.D.BA.2D.ADD.STRONG.SYS.TRAP [R], R, UR` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SURED.D.BA.2D.ADD.STRONG.SYS.TRAP [R4], R0, UR4` | `70ff040004007f9f 0041e40008114100` | sured |


# FFMA (SM120 SASS)

**NVIDIA:** FP32 Fused Multiply and Add (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP32 fused multiply-add (category: FP32)

Observed on sm_120: 18 instruction(s) across 2 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `ffma`: `fma.rn.f32`
- `fdiv_rn`: `div.rn.f32 (IEEE division)`

12-bit opcode field (bits 0-11) values observed: `0xc41`, `0xc42`, `0xc44`.

## Encoding observations

**Constant bits across all 18 observed instance(s): 81 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
110001000...........0000....0000....0000000000000000000........0
.........00000..0000000000000000000000000...0.111111...0000..000
```

8 normalized operand form(s) observed:

### `FFMA R, R, R, R` - 10 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FFMA R5, R0, R5, R7` | `0000000500057223 004fca0000000007` | ffma |
| `FFMA R7, R2, R7, R2` | `0000000702077223 000fc80000000002` | fdiv_rn |
| `FFMA R2, R0, R7, RZ` | `0000000700027223 000fc800000000ff` | fdiv_rn |

### `FFMA R, R, IMM.84467440737095516160e+IMM, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@!P0 FFMA R8, R0, 1.84467440737095516160e+19, RZ` | `5f80000000088823 000fe200000000ff` | fdiv_rn |
| `@!P1 FFMA R9, R3, 1.84467440737095516160e+19, RZ` | `5f80000003099823 000fc600000000ff` | fdiv_rn |

### `FFMA R, -R, R, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FFMA R7, -R3, R2, 1` | `3f80000003077423 002fc80000000102` | fdiv_rn |

### `FFMA R, -R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FFMA R6, -R3, R2, R0` | `0000000203067223 000fc80000000100` | fdiv_rn |

### `FFMA R, R, R, IMM` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FFMA R12, R3, R11, 1` | `3f800000030c7423 001fc8000000000b` | fdiv_rn |

### `FFMA.R R, R, R.reuse, R.reuse` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FFMA.RZ R0, R12, R8.reuse, R13.reuse` | `000000080c007223 180fe2000000c00d` | fdiv_rn |

### `FFMA.RM R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FFMA.RM R7, R12, R8, R13` | `000000080c077223 000fe2000000400d` | fdiv_rn |

### `FFMA.RP R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FFMA.RP R0, R12, R8, R13` | `000000080c007223 000fe2000000800d` | fdiv_rn |


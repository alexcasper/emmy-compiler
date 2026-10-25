# MUFU (SM120 SASS)

**NVIDIA:** FP32 Multi Function Operation (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: multi-function unit: rcp/rsqrt/sqrt/lg2/ex2/sin/cos/tanh approx (category: FP32)

Observed on sm_120: 11 instruction(s) across 9 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `mufu_rcp`: `rcp.approx.f32`
- `mufu_rsqrt`: `rsqrt.approx.f32`
- `mufu_sqrt`: `sqrt.approx.f32`
- `mufu_lg2`: `lg2.approx.f32`
- `mufu_ex2`: `ex2.approx.f32`
- `mufu_sin`: `sin.approx.f32`
- `mufu_cos`: `cos.approx.f32`
- `mufu_tanh`: `tanh.approx.f32`

12-bit opcode field (bits 0-11) values observed: `0x109`, `0x10c`.

## Encoding observations

**Constant bits across all 11 observed instance(s): 102 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
000100001.0.1110...0000000000000..0.000000000000000000..........
0000000000....000000000000000000000000000..001.0011100.000000000
```

9 normalized operand form(s) observed (showing 8):

### `MUFU.RCP R, R` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.RCP R2, R3` | `0000000300027308 004e620000001000` | fdiv_rn |
| `MUFU.RCP R3, R9` | `0000000900037308 000e220000001000` | fdiv_rn |
| `MUFU.RCP R0, R0` | `0000000000007308 000e240000001000` | mufu_rcp |

### `MUFU.RSQ R, -QNAN` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.RSQ R3, -QNAN` | `ffc0000000037908 000e220000001400` | fdiv_rn |

### `MUFU.RSQ R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.RSQ R5, R0` | `0000000000057308 000e240000001400` | mufu_rsqrt |

### `MUFU.SQRT R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.SQRT R5, R0` | `0000000000057308 000e240000002000` | mufu_sqrt |

### `MUFU.LG2 R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.LG2 R5, R0` | `0000000000057308 000e240000000c00` | mufu_lg2 |

### `MUFU.EX2 R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.EX2 R5, R0` | `0000000000057308 000e240000000800` | mufu_ex2 |

### `MUFU.SIN R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.SIN R5, R0` | `0000000000057308 000e240000000400` | mufu_sin |

### `MUFU.COS R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `MUFU.COS R5, R0` | `0000000000057308 000e240000000000` | mufu_cos |

Additional forms: `MUFU.TANH R, R`


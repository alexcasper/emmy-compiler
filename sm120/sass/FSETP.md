# FSETP (SM120 SASS)

**NVIDIA:** FP32 Compare And Set Predicate (Floating Point Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: FP32 compare to predicate (category: FP32)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0xb, 0x53 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L1089)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 16 instruction(s) across 10 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fsetp_selp`: `setp.lt.f32 + selp.f32 (both arms computed)`
- `selp_to_predicated_load`: `selp.f32 between two loaded values`
- `fset`: `set.lt.u32.f32`
- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `mufu_rcp`: `rcp.approx.f32`
- `mufu_rsqrt`: `rsqrt.approx.f32`
- `mufu_sqrt`: `sqrt.approx.f32`
- `mufu_lg2`: `lg2.approx.f32`
- `mufu_ex2`: `ex2.approx.f32`
- `plop3_folded`: `xor.pred of two compares (folded into ISETP/FSETP combine op)`

12-bit opcode field (bits 0-11) values observed: `0xd01`, `0xd04`.

## Encoding observations

**Constant bits across all 16 observed instance(s): 92 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
110100000.0.111000000000...00000...000000000000000..............
000000000.00.......0111111000000000000000.0...11111100.000.00000
```

11 normalized operand form(s) observed (showing 8):

### `FSETP.GEU.AND P, P, |R|, IMM.175494350822287508e-IMM, P` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.GEU.AND P0, PT, |R0|, 1.175494350822287508e-38, PT` | `008000000000780b 004fda0003f0e200` | mufu_rsqrt |
| `FSETP.GEU.AND P0, PT, |R0|, 1.175494350822287508e-38, PT` | `008000000000780b 004fda0003f0e200` | mufu_sqrt |
| `FSETP.GEU.AND P0, PT, |R0|, 1.175494350822287508e-38, PT` | `008000000000780b 004fda0003f0e200` | mufu_lg2 |

### `FSETP.GEU.AND P, P, R, R, P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.GEU.AND P0, PT, R5, R0, PT` | `000000000500720b 000fca0003f0e000` | fsetp_selp |
| `FSETP.GEU.AND P0, PT, R5, R0, PT` | `000000000500720b 004fda0003f0e000` | selp_to_predicated_load |

### `FSETP.GTU.FTZ.AND P, P, |R|, +INF , P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.GTU.FTZ.AND P0, PT, |R0|, +INF , PT` | `7f8000000000780b 000fe20003f1c200` | fdiv_rn |
| `FSETP.GTU.FTZ.AND P1, PT, |R3|, +INF , PT` | `7f8000000300780b 000fca0003f3c200` | fdiv_rn |

### `FSETP.NEU.FTZ.AND P, P, |R|, +INF , P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.NEU.FTZ.AND P1, PT, |R3|, +INF , PT` | `7f8000000300780b 000fe20003f3d200` | fdiv_rn |
| `FSETP.NEU.FTZ.AND P0, PT, |R0|, +INF , PT` | `7f8000000000780b 000fd80003f1d200` | fdiv_rn |

### `FSETP.LT.AND P, P, R, R, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.LT.AND P0, PT, R0, R5, PT` | `000000050000720b 004fca0003f01000` | fset |

### `FSETP.NEU.FTZ.AND P, P, |R|.reuse, +INF , P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.NEU.FTZ.AND P2, PT, |R0|.reuse, +INF , PT` | `7f8000000000780b 040fe20003f5d200` | fdiv_rn |

### `FSETP.NEU.FTZ.AND P, P, R, R, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.NEU.FTZ.AND P0, PT, R0, R7, PT` | `000000070000720b 000fe20003f1d000` | fdiv_rn |

### `FSETP.GEU.AND P, P, |R|.reuse, IMM.175494350822287508e-IMM, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `FSETP.GEU.AND P1, PT, |R0|.reuse, 1.175494350822287508e-38, PT` | `008000000000780b 044fe20003f2e200` | mufu_rcp |

Additional forms: `FSETP.GT.AND P, P, |R|, IMM.50705917302346158658e+IMM, P`, `FSETP.GEU.AND P, P, R, -IMM, P`, `FSETP.GT.AND P, P, R, R, P`


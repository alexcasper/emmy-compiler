# IADD3 (SM120 SASS)

**NVIDIA:** 3-input Integer Addition (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: 3-input 32-bit integer add (category: Integer)

Observed on sm_120: 65 instruction(s) across 21 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `iadd`: `add.s32 / sub.s32`
- `isetp_pred`: `setp.lt.s32 + selp.b32`
- `imnmx_from_selp`: `setp.lt.s32 + selp.b32 forming min()`
- `flo`: `bfind.u32 / clz.b32`
- `vabsdiff`: `vabsdiff.u32.u32.u32 (observe)`
- `vabsdiff2`: `vabsdiff2.u32.u32.u32 (observe)`
- `vabsdiff4`: `vabsdiff4.u32.u32.u32.add`
- `s2ur`: `%ctaid.x used in uniform address math (observe)`
- `ldl_stl`: `dynamically indexed .local array`
- `ldsm`: `ldmatrix.sync.aligned.m8n8.x4.shared.b16`
- `atoms`: `atom.shared.add.u32`
- `imma`: `mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`
- `diverge`: `data-dependent loop`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `bssy_bsync`: `divergent loop exit followed by a warp-synchronous op`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`
- `uniform_alu`: `integer ops on a kernel parameter (warp-uniform)`
- `cctll`: `prefetch.local.L1`

12-bit opcode field (bits 0-11) values observed: `0x081`, `0x083`, `0x084`.

## Encoding observations

**Constant bits across all 65 observed instance(s): 49 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
000010000...........0000........................................
.........0..011111..1111....0000000000000.....111111....0..00000
```

10 normalized operand form(s) observed (showing 8):

### `IADD3 R, P, P, R, R, R` - 29 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD3 R7, PT, PT, R7, R10, RZ` | `0000000a07077210 000fe40007ffe0ff` | fdiv_rn |
| `IADD3 R10, PT, PT, R0, R7, RZ` | `00000007000a7210 000fc80007ffe0ff` | fdiv_rn |
| `IADD3 R0, PT, PT, R9, R0, RZ` | `0000000009007210 000fc80007ffe0ff` | fdiv_rn |
| `IADD3 R5, PT, PT, R0, R5, RZ` | `0000000500057210 008fd80007ffe0ff` | isetp_pred |
| `IADD3 R5, PT, PT, R4, R5, RZ` | `0000000504057210 008fca0007ffe0ff` | vabsdiff4 |
| `IADD3 R7, PT, PT, R0, R5, RZ` | `0000000500077210 004fca0007ffe0ff` | s2ur |
| `IADD3 R11, PT, PT, R8, R11, RZ` | `0000000b080b7210 001fca0007ffe0ff` | ldsm |
| `@P0 IADD3 R4, PT, PT, R0, R5, RZ` | `0000000500040210 001fe40007ffe0ff` | atoms |
| `IADD3 R7, PT, PT, R4, R7, RZ` | `0000000704077210 000fca0007ffe0ff` | imma |
| `IADD3 R3, PT, PT, R4, R7, RZ` | `0000000704037210 000fca0007ffe0ff` | bmma |
| `IADD3 R5, PT, PT, R6, R5, R4` | `0000000506057210 000fc80007ffe004` | diverge |
| `IADD3 R5, PT, PT, R0, R5, R0` | `0000000500057210 020fc60007ffe000` | uniform_loop |
| `IADD3 R6, PT, PT, R6, R4, RZ` | `0000000406067210 000fc60007ffe0ff` | bssy_bsync |
| `IADD3 R7, PT, PT, R0, R11, RZ` | `0000000b00077210 001fca0007ffe0ff` | agg_atomic |
| `@P2 IADD3 R5, PT, PT, R0, R5, RZ` | `0000000500052210 004fd80007ffe0ff` | s2ur_loop |

### `IADD3 R, P, P, R, IMM, R` - 13 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `@!P1 IADD3 R10, PT, PT, R10, 0x40, RZ` | `000000400a0a9810 000fce0007ffe0ff` | fdiv_rn |
| `IADD3 R9, PT, PT, R10, 0x20, RZ` | `000000200a097810 000fe20007ffe0ff` | fdiv_rn |
| `IADD3 R6, PT, PT, R4, 0x1, RZ` | `0000000104067810 000fc80007ffe0ff` | diverge |
| `IADD3 R4, PT, PT, R4, 0x4, RZ` | `0000000404047810 000fe40007ffe0ff` | uniform_loop |
| `IADD3 R7, PT, PT, R7, 0x1, RZ` | `0000000107077810 000fe40007ffe0ff` | bssy_bsync |
| `IADD3 R4, PT, PT, R4, 0x4, RZ` | `0000000404047810 000fe40007ffe0ff` | s2ur_loop |

### `IADD3 R, P, P, R, -IMM, R` - 7 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD3 R12, PT, PT, R7, -0x1, RZ` | `ffffffff070c7810 000fe20007ffe0ff` | fdiv_rn |
| `IADD3 R11, PT, PT, R6, -0x1, RZ` | `ffffffff060b7810 000fc60007ffe0ff` | fdiv_rn |
| `IADD3 R6, PT, PT, R6, -0x7f, RZ` | `ffffff8106067810 000fe40007ffe0ff` | fdiv_rn |
| `IADD3 R1, PT, PT, R1, -0x100, RZ` | `ffffff0001017810 001fe20007ffe0ff` | ldl_stl |
| `IADD3 R7, PT, PT, R0, -0x3, RZ` | `fffffffd00077810 000fd60007ffe0ff` | diverge |
| `IADD3 R1, PT, PT, R1, -0x40, RZ` | `ffffffc001017810 001fe20007ffe0ff` | cctll |

### `IADD3 R, P, P, R, -R, R` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD3 R0, P1, PT, RZ, -R0, RZ` | `80000000ff007210 000fc80007f3e0ff` | vabsdiff |
| `IADD3 R7, PT, PT, R7, -R8, RZ` | `8000000807077210 000fe40007ffe0ff` | vabsdiff2 |
| `IADD3 R6, PT, PT, R0, -R4, RZ` | `8000000400067210 000fca0007ffe0ff` | diverge |

### `IADD3 R, P, P, -R, UR, R` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD3 R6, PT, PT, -R4, UR7, RZ` | `0000000704067c10 000fca000fffe1ff` | uniform_loop |
| `IADD3 R6, PT, PT, -R4, UR7, RZ` | `0000000704067c10 000fca000fffe1ff` | uniform_loop |
| `IADD3 R6, PT, PT, -R4, UR6, RZ` | `0000000604067c10 000fca000fffe1ff` | s2ur_loop |

### `IADD3 R, P, P, -R, R, R` - 3 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD3 R9, PT, PT, -R0, R9, RZ` | `0000000900097210 000fc60007ffe1ff` | fdiv_rn |
| `IADD3 R8, PT, PT, -R10, RZ, RZ` | `000000ff0a087210 000fe40007ffe1ff` | fdiv_rn |
| `IADD3 R5, PT, PT, -R4, R0, R5` | `0000000004057210 004fca0007ffe105` | iadd |

### `IADD3 R, P, P, R, IMM, -R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD3 R7, PT, PT, R6, 0x7f, -R7` | `0000007f06077810 000fe20007ffe807` | fdiv_rn |
| `IADD3 R5, PT, PT, R0, 0x1f, -R5` | `0000001f00057810 001fca0007ffe805` | flo |

### `IADD3 R, P, P, R.reuse, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `IADD3 R5, PT, PT, R0.reuse, R5, RZ` | `0000000500057210 044fe40007ffe0ff` | imnmx_from_selp |

Additional forms: `IADD3.X R, P, P, R, ~R, R, P, !P`, `IADD3 R, P, P, R, UR, R`


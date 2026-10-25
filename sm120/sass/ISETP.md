# ISETP (SM120 SASS)

**NVIDIA:** Integer Compare And Set Predicate (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: integer compare to predicate (category: Integer)

Observed on sm_120: 38 instruction(s) across 13 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `isetp_pred`: `setp.lt.s32 + selp.b32`
- `vabsdiff`: `vabsdiff.u32.u32.u32 (observe)`
- `vote`: `vote.sync.ballot.b32`
- `atoms`: `atom.shared.add.u32`
- `bar_red`: `bar.red.popc.u32`
- `diverge`: `data-dependent loop`
- `uniform_loop`: `loop with trip count from kernel param (uniform datapath)`
- `bssy_bsync`: `divergent loop exit followed by a warp-synchronous op`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`
- `agg_red`: `red.global.add.u32 to a warp-uniform address (warp-aggregated)`
- `s2ur_loop`: `%ctaid.x as a loop bound (warp-uniform)`
- `plop3_folded`: `xor.pred of two compares (folded into ISETP/FSETP combine op)`

12-bit opcode field (bits 0-11) values observed: `0x301`, `0x303`, `0x304`.

## Encoding observations

**Constant bits across all 38 observed instance(s): 66 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
001100000...111000000000....0000................................
000011100......00..0111.....0000000000000.....111111.0..0..00000
```

24 normalized operand form(s) observed (showing 8):

### `ISETP.GT.AND P, P, R, IMM, P` - 5 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.GT.AND P0, PT, R10, 0xfe, PT` | `000000fe0a00780c 000fda0003f04270` | fdiv_rn |
| `ISETP.GT.AND P1, PT, R6, 0x3, PT` | `000000030600780c 000fda0003f24270` | diverge |
| `ISETP.GT.AND P1, PT, R6, 0x1, PT` | `000000010600780c 000fda0003f24270` | diverge |
| `ISETP.GT.AND P1, PT, R6, 0x3, PT` | `000000030600780c 000fda0003f24270` | uniform_loop |

### `ISETP.NE.AND P, P, R, R, P` - 5 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.NE.AND P2, PT, R10, RZ, PT` | `000000ff0a00720c 000fe20003f45270` | fdiv_rn |
| `ISETP.NE.AND P1, PT, R9, RZ, P1` | `000000ff0900720c 000fc60000f25270` | fdiv_rn |
| `ISETP.NE.AND P0, PT, R0, RZ, PT` | `000000ff0000720c 004fda0003f05270` | vote |
| `ISETP.NE.AND P0, PT, R0, RZ, PT` | `000000ff0000720c 004fda0003f05270` | bar_red |
| `ISETP.NE.AND P0, PT, R4, R7, PT` | `000000070400720c 020fda0003f05270` | bssy_bsync |

### `ISETP.GE.AND P, P, R, R, P` - 4 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.GE.AND P0, PT, R11, RZ, PT` | `000000ff0b00720c 000fe20003f06270` | fdiv_rn |
| `ISETP.GE.AND P1, PT, R12, RZ, PT` | `000000ff0c00720c 000fd80003f26270` | fdiv_rn |
| `ISETP.GE.AND P1, PT, R4, R7, PT` | `000000070400720c 000fda0003f26270` | diverge |
| `ISETP.GE.AND P0, PT, R7, R0, PT` | `000000000700720c 000fda0003f06270` | bssy_bsync |

### `ISETP.GE.U32.AND P, P, R, UR, P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.GE.U32.AND P2, PT, R4, UR6, PT` | `0000000604007c0c 000fca000bf46070` | s2ur_loop |
| `ISETP.GE.U32.AND P1, PT, R4, UR7, PT` | `0000000704007c0c 000fe2000bf26070` | s2ur_loop |

### `ISETP.LT.U32.AND P, P, R.reuse, UR, P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.LT.U32.AND P1, PT, R4.reuse, UR6, PT` | `0000000604007c0c 040fe2000bf21070` | s2ur_loop |
| `ISETP.LT.U32.AND P1, PT, R4.reuse, UR6, PT` | `0000000604007c0c 040fe2000bf21070` | s2ur_loop |

### `ISETP.LE.U32.OR P, P, R, IMM, !P` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.LE.U32.OR P1, PT, R6, 0x3, !P1` | `000000030600780c 000fe20004f23470` | s2ur_loop |
| `ISETP.LE.U32.OR P1, PT, R6, 0x1, !P1` | `000000010600780c 000fda0004f23470` | s2ur_loop |

### `ISETP.GT.U32.AND P, P, R, IMM, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.GT.U32.AND P0, PT, R12, 0xfd, PT` | `000000fd0c00780c 000fca0003f04070` | fdiv_rn |

### `ISETP.GT.U32.OR P, P, R, IMM, P` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ISETP.GT.U32.OR P0, PT, R11, 0xfd, P0` | `000000fd0b00780c 000fda0000704470` | fdiv_rn |

Additional forms: `ISETP.GE.U32.AND P, P, R, IMM, P`, `ISETP.GE.AND P, P, R, IMM, P`, `ISETP.GE.AND P, P, R, -IMM, P`, `ISETP.NE.AND P, P, R.reuse, R, P`, `ISETP.GE.AND P, P, R.reuse, R, P`, `ISETP.LT.AND P, P, R, R, P`, `ISETP.EQ.U32.AND P, P, R, -IMM, P`, `ISETP.EQ.U32.AND P, P, R, IMM, P`, `ISETP.GT.AND P, P, R, R, P`, `ISETP.GE.AND P, P, R, R, !P`, `ISETP.GE.AND P, P, R, UR, P`, `ISETP.GE.AND P, P, R, UR, !P`, `ISETP.EQ.U32.AND P, P, R, R, P`, `ISETP.EQ.U32.AND P, P, R, UR, P`, `ISETP.GE.U32.AND P, P, R, UR, !P`, `ISETP.LT.XOR P, P, R, R, P`


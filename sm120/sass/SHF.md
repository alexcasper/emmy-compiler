# SHF (SM120 SASS)

**NVIDIA:** Funnel Shift (Integer Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: funnel shift / 64-bit shifts (category: Integer)

Opcode cross-check vs Mesa NAK (open-source NVK compiler, mirror commit `837ab0e30740`): **agree**. NAK encodes 0x19, 0x99 ([source](https://github.com/chaotic-cx/mesa-mirror/blob/837ab0e30740abb9ebb60bcd40a5114c68c673d9/src/nouveau/compiler/nak/sm70_encode.rs#L2141)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Observed on sm_120: 23 instruction(s) across 9 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `fdiv_rn`: `div.rn.f32 (IEEE division)`
- `lea64`: `pointer + (sign-extended s32 index << 2)`
- `shf`: `shf.l.wrap.b32`
- `shl64`: `shl.b64 by register`
- `sgxt`: `bfe.s32 (signed field extract)`
- `vabsdiff2`: `vabsdiff2.u32.u32.u32 (observe)`
- `ldc`: `ld.const with dynamic index`
- `bmma`: `mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc`
- `brx`: `brx.idx (jump table)`

12-bit opcode field (bits 0-11) values observed: `0x981`, `0x984`.

## Encoding observations

**Constant bits across all 23 observed instance(s): 86 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
100110000.0.1110.....000.............000000000000000000000000000
........0....000.000000000000000000000000...0.1111110...00..0000
```

8 normalized operand form(s) observed:

### `SHF.R.U32.HI R, R, IMM, R` - 14 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.R.U32.HI R7, RZ, 0x17, R3` | `00000017ff077819 000fe20000011603` | fdiv_rn |
| `SHF.R.U32.HI R5, RZ, 0x10, R6` | `00000010ff057819 000fc80000011606` | vabsdiff2 |
| `SHF.R.U32.HI R2, RZ, 0x3, R2` | `00000003ff027819 000fe40000011602` | bmma |
| `SHF.R.U32.HI R6, RZ, 0x17, R0` | `00000017ff067819 000fe40000011600` | fdiv_rn |
| ... 10 more instance(s) in results.json | | |

### `SHF.L.U32 R, R, R, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.L.U32 R9, R6, R9, RZ` | `0000000906097219 000fe400000006ff` | fdiv_rn |
| `SHF.L.U32 R4, R4, R7, RZ` | `0000000704047219 000fca00000006ff` | shl64 |

### `SHF.R.S32.HI R, R, IMM, R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.R.S32.HI R9, RZ, 0x1f, R6` | `0000001fff097819 004fe40000011406` | lea64 |
| `SHF.R.S32.HI R5, RZ, 0x1f, R4` | `0000001fff057819 002fc80000011404` | brx |

### `SHF.R.U32.HI R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.R.U32.HI R7, RZ, R7, R6` | `00000007ff077219 000fe40000011606` | fdiv_rn |

### `SHF.L.W.U32.HI R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.L.W.U32.HI R5, R0, R4, R5` | `0000000400057219 004fca0000010e05` | shf |

### `SHF.L.U64.HI R, R.reuse, R.reuse, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.L.U64.HI R5, R4.reuse, R7.reuse, R5` | `0000000704057219 0c4fe40000010205` | shl64 |

### `SHF.R.S32.HI R, R, R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.R.S32.HI R5, RZ, R5, R0` | `00000005ff057219 008fc80000011400` | sgxt |

### `SHF.L.U32 R, R, IMM, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `SHF.L.U32 R0, R0, 0x2, RZ` | `0000000200007819 004fc800000006ff` | ldc |


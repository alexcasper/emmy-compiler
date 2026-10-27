# ATOMG (SM120 SASS)

**NVIDIA:** Atomic Operation on Global Memory (Load/Store Instructions). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#blackwell-and-rubin-instruction-set)

Notes: global atomic with return; also the vector form (atom.global.v2.add.f32) (category: Atomics / reductions)

Observed on sm_120: 5 instruction(s) across 5 probe(s).

## Evidence

Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that output; bit 0 is the LSB of the first 64-bit word.

Emitted by probe(s):

- `atomg`: `atom.global.add.u32 (result used)`
- `atom_v2_f32`: `atom.global.v2.add.f32 (vector atomic, sm_90+)`
- `atom_cas`: `atom.global.cas.b32`
- `atom_add_f32`: `atom.global.add.f32 (fast fp32 atomic)`
- `agg_atomic`: `atom.global.add.u32 to a warp-uniform address (warp-aggregation)`

12-bit opcode field (bits 0-11) values observed: `0x159`, `0x95c`, `0xc59`.

## Encoding observations

**Constant bits across all 5 observed instance(s): 99 of 128** (observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, so bits that never varied here may still be modifiers in forms this corpus never compiled; bits 105-125 are the scheduling control code and vary with instruction placement). LSB-first, bit 0 first:

```
..0.01011.0....0.01000000..00000.0..00000000.0.0000000000000000.
.01000001..0.1110111100000..0000000000000...01.101110..000000000
```

4 normalized operand form(s) observed:

### `ATOMG.E.ADD.STRONG.GPU P, R, desc[UR][R.IMM], R` - 2 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ATOMG.E.ADD.STRONG.GPU PT, R5, desc[UR4][R2.64], R5` | `80000005020579a8 004ea800081ef104` | atomg |
| `@P0 ATOMG.E.ADD.STRONG.GPU PT, R5, desc[UR4][R4.64], R9` | `80000009040509a8 002ee200081ef104` | agg_atomic |

### `ATOMG.E.ADD.F32x2.FTZ.RN.STRONG.GPU P, R, desc[UR][R.IMM+IMM], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ATOMG.E.ADD.F32x2.FTZ.RN.STRONG.GPU PT, R4, desc[UR4][R2.64+0x50], R4` | `80005004020479a3 004ea4000c1ef504` | atom_v2_f32 |

### `ATOMG.E.CAS.STRONG.GPU P, R, [R], R, R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ATOMG.E.CAS.STRONG.GPU PT, R5, [R2], R4, R5` | `00000004020573a9 004ea800001ee105` | atom_cas |

### `ATOMG.E.ADD.F32.FTZ.RN.STRONG.GPU P, R, desc[UR][R.IMM], R` - 1 instance(s)

| instruction | encoding (word0 word1) | probe |
|---|---|---|
| `ATOMG.E.ADD.F32.FTZ.RN.STRONG.GPU PT, R5, desc[UR4][R2.64], R5` | `80000005020579a3 004ea8000c1ef304` | atom_add_f32 |


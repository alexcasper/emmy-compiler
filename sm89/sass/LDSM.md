# LDSM (SM89 SASS)

**NVIDIA:** Load Matrix from Shared Memory with Element Size Expansion (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Load matrix fragments from shared memory (ldmatrix) (category: Load / store)

Typically emitted for: `ldmatrix.sync.aligned.m8n8.x1/x2/x4[.trans].b16`

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x83b ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4622)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [ldsm](../verify/RESULTS.md#ldsm): `ldmatrix.sync.aligned.m8n8.x4.shared.b16`

Encodings: <https://kuterdinel.com/nv_isa_sm89/LDSM.html> (machine-derived by fuzzing the assembler; no semantics).

7 encoding variant(s):

- [LDSM_R_I](#v1)
- [LDSM_R_R](#v2)
- [LDSM_R_RI](#v3)
- [LDSM_R_RUR](#v4)
- [LDSM_R_RURI](#v5)
- [LDSM_R_UR](#v6)
- [LDSM_R_URI](#v7)

<a id="v1"></a>
## 1. `LDSM_R_I`

Syntax: `LDSM.16 R, [INT_IMM]`  
Example: `@P0 LDSM.16.M88 R0, [0x2] ;`

Register access: WRITE R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 40-63 |
| modi 1 | 72-73 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111000001............1111111100000000........................
00000000..0000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `2.` |
| `10` | `4.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `M88.` |
| `01` | `MT88.` |
| `10` | `M816.` |
| `11` | `M832.` |

<a id="v2"></a>
## 2. `LDSM_R_R`

Syntax: `LDSM.16 R, [R]`  
Example: `@P0 LDSM.16.M88 R0, [R0] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| modi 1 | 72-73 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111000001....................00000000000000000000000000000000
00000000..0000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `2.` |
| `10` | `4.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `M88.` |
| `01` | `MT88.` |
| `10` | `M816.` |
| `11` | `M832.` |

<a id="v3"></a>
## 3. `LDSM_R_RI`

Syntax: `LDSM.16 R, [R+INT_IMM]`  
Example: `@P0 LDSM.16.M88 R0, [R0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 40-63 |
| modi 1 | 72-73 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111000001....................00000000........................
00000000..0000..0000000000000000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `2.` |
| `10` | `4.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `M88.` |
| `01` | `MT88.` |
| `10` | `M816.` |
| `11` | `M832.` |

<a id="v4"></a>
## 4. `LDSM_R_RUR`

Syntax: `LDSM.16 R, [R+UR]`  
Example: `@P0 LDSM.16.M88 R0, [R0+UR0] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| modi 1 | 72-73 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111000001...........................0000000000000000000000000
00000000..0000..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `2.` |
| `10` | `4.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `M88.` |
| `01` | `MT88.` |
| `10` | `M816.` |
| `11` | `M832.` |

<a id="v5"></a>
## 5. `LDSM_R_RURI`

Syntax: `LDSM.16 R, [R+UR+INT_IMM]`  
Example: `@P0 LDSM.16.M88 R0, [R0+UR0+0x1] ;`

Register access: WRITE R (1 slots); READ R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 24-31 |
| operand 2 | 32-38 |
| operand 3 | 40-63 |
| modi 1 | 72-73 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111000001...........................0........................
00000000..0000..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `2.` |
| `10` | `4.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `M88.` |
| `01` | `MT88.` |
| `10` | `M816.` |
| `11` | `M832.` |

<a id="v6"></a>
## 6. `LDSM_R_UR`

Syntax: `LDSM.16 R, [UR]`  
Example: `@P0 LDSM.16.M88 R0, [UR0] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| modi 1 | 72-73 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111000001............11111111.......0000000000000000000000000
00000000..0000..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `2.` |
| `10` | `4.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `M88.` |
| `01` | `MT88.` |
| `10` | `M816.` |
| `11` | `M832.` |

<a id="v7"></a>
## 7. `LDSM_R_URI`

Syntax: `LDSM.16 R, [UR+INT_IMM]`  
Example: `@P0 LDSM.16.M88 R0, [UR0+0x2] ;`

Register access: WRITE R (1 slots); READ UR (1 slots)

| field | bits |
|---|---|
| predicate | 12-15 |
| operand 0 | 16-23 |
| operand 1 | 32-38 |
| operand 2 | 40-63 |
| modi 1 | 72-73 |
| modi 2 | 78-79 |
| stall | 105-108 |
| y | 109 |
| write scoreboard (site label: r-bar) | 110-112 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
110111000001............11111111.......0........................
00000000..0000..0000000000010000000000000.....................00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `00` | `(default)` |
| `01` | `2.` |
| `10` | `4.` |
| `11` | `INVALID3.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `M88.` |
| `01` | `MT88.` |
| `10` | `M816.` |
| `11` | `M832.` |


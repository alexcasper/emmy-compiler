# MEMBAR (SM89 SASS)

**NVIDIA:** Memory Barrier (Load/Store Instructions). Source: [CUDA Binary Utilities, Ampere/Ada instruction set](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#nvidia-ampere-gpu-and-ada-instruction-set)

Notes: Memory barrier / fence (membar, fence.sc/acq_rel) (category: Synchronization / barriers)

Typically emitted for: `membar.cta/gl/sys`, `fence.*` (`__threadfence`)

## Evidence

Opcode cross-check vs Mesa NAK (open-source NVK compiler, commit `e7371b0711bb`): **agree**. NAK encodes 0x992 ([source](https://gitlab.freedesktop.org/mesa/mesa/-/blob/e7371b0711bb1cd38c39d1c05e5578c445cc6bca/src/nouveau/compiler/nak/sm70_encode.rs#L4063)); see [verify/NAK_CROSSCHECK.md](../verify/NAK_CROSSCHECK.md).

Checked with Build cuda_12.9.r12.9/compiler.36037853_0 (`-arch=sm_89`) and nvdisasm (Build cuda_13.4.r13.4/compiler.38855100_0); see [verify/RESULTS.md](../verify/RESULTS.md).

Claimed lowering confirmed by probe(s):

- [membar](../verify/RESULTS.md#membar): `membar.gl`
- [fence_sys](../verify/RESULTS.md#fence_sys): `fence.sc.sys`

Encodings: <https://kuterdinel.com/nv_isa_sm89/MEMBAR.html> (machine-derived by fuzzing the assembler; no semantics).

1 encoding variant(s):

- [MEMBAR](#v1)

<a id="v1"></a>
## 1. `MEMBAR`

Syntax: `MEMBAR`  
Example: `@P0 MEMBAR.SC.CTA ;`

| field | bits |
|---|---|
| predicate | 12-15 |
| modi 1 | 76-78 |
| modi 2 | 79-80 |
| stall | 105-108 |
| y | 109 |
| read scoreboard (site label: w-bar) | 113-115 |
| wait mask (site label: b-mask) | 116-121 |
| reuse | 122-125 |

Fixed bits (bit 0 first; `.` = field):
```
010010011001....000000000000000000000000000000000000000000000000
000000000000.....000000000000000000000000.....111.............00
```

Modifier Group 1:

| value | modifier |
|---|---|
| `000` | `CTA.` |
| `001` | `SM.` |
| `010` | `GPU.` |
| `011` | `SYS.` |
| `100` | `INVALID4.` |
| `101` | `VC.` |
| `110` | `INVALID6.` |
| `111` | `INVALID7.` |

Modifier Group 2:

| value | modifier |
|---|---|
| `00` | `SC.` |
| `01` | `ALL.` |
| `10` | `(default)` |
| `11` | `MMIO.` |


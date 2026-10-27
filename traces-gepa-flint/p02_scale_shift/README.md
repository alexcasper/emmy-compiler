# Trace: p02_scale_shift

- Source: gen/trace_src/flint/p02_scale_shift.ptx
- Generated: 2026-10-26 03:40 UTC
- Tools: ptxas `Cuda compilation tools, release 12.9, V12.9.86`, nvdisasm `Cuda compilation tools, release 12.9, V12.9.88`, both `-O3`
- The sm_120 stage consumes a header-retargeted copy of the same PTX (`.target sm_120`, `.version` bumped to >= 8.7); the body is untouched.

- **sm_89: 48 SASS instructions, 14 distinct opcodes**
- **sm_120: 48 SASS instructions, 14 distinct opcodes**
## sm_89 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BRA | 1 | [BRA.md](../../sm89/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| EXIT | 2 | [EXIT.md](../../sm89/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| FFMA | 4 | [FFMA.md](../../sm89/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| IADD3 | 3 | [IADD3.md](../../sm89/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 5 | [IMAD.md](../../sm89/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 1 | [ISETP.md](../../sm89/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDG | 6 | [LDG.md](../../sm89/sass/LDG.md) | Load from Global Memory (Load/Store Instructions) | — |
| LEA | 1 | [LEA.md](../../sm89/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| MOV | 6 | [MOV.md](../../sm89/sass/MOV.md) | Move (Movement Instructions) | NAK: agree |
| NOP | 14 | [NOP.md](../../sm89/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| S2R | 2 | [S2R.md](../../sm89/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| SHF | 1 | [SHF.md](../../sm89/sass/SHF.md) | Funnel Shift (Integer Instructions) | NAK: agree |
| STG | 1 | [STG.md](../../sm89/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |
| ULDC | 1 | [ULDC.md](../../sm89/sass/ULDC.md) | Load from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |

## sm_120 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BRA | 1 | [BRA.md](../../sm120/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| EXIT | 2 | [EXIT.md](../../sm120/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| FFMA | 4 | [FFMA.md](../../sm120/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| IADD3 | 3 | [IADD3.md](../../sm120/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 5 | [IMAD.md](../../sm120/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 1 | [ISETP.md](../../sm120/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDC | 5 | [LDC.md](../../sm120/sass/LDC.md) | Load Constant (Load/Store Instructions) | NAK: agree |
| LDCU | 1 | [LDCU.md](../../sm120/sass/LDCU.md) | Load a Value from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |
| LDG | 6 | [LDG.md](../../sm120/sass/LDG.md) | Load from Global Memory (Load/Store Instructions) | — |
| LEA | 1 | [LEA.md](../../sm120/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| NOP | 15 | [NOP.md](../../sm120/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| S2R | 2 | [S2R.md](../../sm120/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| SHF | 1 | [SHF.md](../../sm120/sass/SHF.md) | Funnel Shift (Integer Instructions) | NAK: agree |
| STG | 1 | [STG.md](../../sm120/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |

## sm_89 vs sm_120 divergence summary

Same source PTX, two toolchain targets. Opcode sets are per-mnemonic (nvspas form bits ignored). Renames/replacements cite the sm120 KB divergence notes ([verify/RESULTS.md](../../sm120/verify/RESULTS.md), [README](../../sm120/README.md)).

**Shared opcodes (12):** `BRA`, `EXIT`, `FFMA`, `IADD3`, `IMAD`, `ISETP`, `LDG`, `LEA`, `NOP`, `S2R`, `SHF`, `STG`

### Replaced (sm_89 opcode -> sm_120 successor, per KB)

| sm_89 | sm_120 (KB finding) | observed here on sm_120 |
|---|---|---|
| `ULDC` | LDCU | yes |

### Emitted on sm_89 but not on sm_120

| opcode | KB explanation |
|---|---|
| `MOV` | sm_120 loads kernel params via LDC/LDCU directly (KB: prologue divergence); MOV still exists in the sm_120 ISA but ptxas stops using it here |

### Emitted on sm_120 but not on sm_89 (new/renamed-in opcodes)

`LDC`, `LDCU`

Full per-arch tables above; the general (input-independent) divergence catalog lives in [sm120/verify/RESULTS.md](../../sm120/verify/RESULTS.md).


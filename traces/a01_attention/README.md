# Trace: a01_attention

- Source: task/problems/a01_attention
- Generated: 2026-10-25 20:05 UTC
- Tools: ptxas `Cuda compilation tools, release 12.9, V12.9.86`, nvdisasm `Cuda compilation tools, release 12.9, V12.9.88`, both `-O3`
- The sm_120 stage consumes a header-retargeted copy of the same PTX (`.target sm_120`, `.version` bumped to >= 8.7); the body is untouched.

- **sm_89: 1760 SASS instructions, 29 distinct opcodes**
- **sm_120: 1760 SASS instructions, 31 distinct opcodes**
## sm_89 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BRA | 24 | [BRA.md](../../sm89/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| BSSY | 9 | [BSSY.md](../../sm89/sass/BSSY.md) | Barrier Set Convergence Synchronization Point (Control Instructions) | NAK: agree |
| BSYNC | 9 | [BSYNC.md](../../sm89/sass/BSYNC.md) | Synchronize Threads on a Convergence Barrier (Control Instructions) | NAK: agree |
| CALL | 10 | [CALL.md](../../sm89/sass/CALL.md) | Call Function (Control Instructions) | — |
| CS2R | 4 | [CS2R.md](../../sm89/sass/CS2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| EXIT | 2 | [EXIT.md](../../sm89/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| F2I | 6 | [F2I.md](../../sm89/sass/F2I.md) | Floating Point To Integer Conversion (Conversion Instructions) | NAK: agree |
| FADD | 27 | [FADD.md](../../sm89/sass/FADD.md) | FP32 Add (Floating Point Instructions) | NAK: agree |
| FFMA | 297 | [FFMA.md](../../sm89/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| FMNMX | 8 | [FMNMX.md](../../sm89/sass/FMNMX.md) | FP32 Minimum/Maximum (Floating Point Instructions) | NAK: agree |
| FMUL | 68 | [FMUL.md](../../sm89/sass/FMUL.md) | FP32 Multiply (Floating Point Instructions) | NAK: agree |
| FSETP | 17 | [FSETP.md](../../sm89/sass/FSETP.md) | FP32 Compare And Set Predicate (Floating Point Instructions) | NAK: agree |
| I2F | 6 | [I2F.md](../../sm89/sass/I2F.md) | Integer To Floating Point Conversion (Conversion Instructions) | NAK: agree |
| IADD3 | 361 | [IADD3.md](../../sm89/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 350 | [IMAD.md](../../sm89/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 31 | [ISETP.md](../../sm89/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDG | 322 | [LDG.md](../../sm89/sass/LDG.md) | Load from Global Memory (Load/Store Instructions) | — |
| LEA | 43 | [LEA.md](../../sm89/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| LOP3 | 19 | [LOP3.md](../../sm89/sass/LOP3.md) | Logic Operation (Integer Instructions) | NAK: agree |
| MOV | 67 | [MOV.md](../../sm89/sass/MOV.md) | Move (Movement Instructions) | NAK: agree |
| MUFU | 35 | [MUFU.md](../../sm89/sass/MUFU.md) | FP32 Multi Function Operation (Floating Point Instructions) | NAK: agree |
| NOP | 14 | [NOP.md](../../sm89/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| PLOP3 | 1 | [PLOP3.md](../../sm89/sass/PLOP3.md) | Predicate Logic Operation (Predicate Instructions) | NAK: agree |
| RET | 1 | [RET.md](../../sm89/sass/RET.md) | Return From Subroutine (Control Instructions) | — |
| S2R | 2 | [S2R.md](../../sm89/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| SEL | 2 | [SEL.md](../../sm89/sass/SEL.md) | Select Source with Predicate (Movement Instructions) | NAK: agree |
| SHF | 16 | [SHF.md](../../sm89/sass/SHF.md) | Funnel Shift (Integer Instructions) | NAK: agree |
| STG | 8 | [STG.md](../../sm89/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |
| ULDC | 1 | [ULDC.md](../../sm89/sass/ULDC.md) | Load from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |

## sm_120 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BRA | 24 | [BRA.md](../../sm120/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| BSSY | 9 | [BSSY.md](../../sm120/sass/BSSY.md) | Barrier Set Convergence Synchronization Point (Control Instructions) | NAK: agree |
| BSYNC | 9 | [BSYNC.md](../../sm120/sass/BSYNC.md) | Synchronize Threads on a Convergence Barrier (Control Instructions) | NAK: agree |
| CALL | 9 | [CALL.md](../../sm120/sass/CALL.md) | Call Function (Control Instructions) | — |
| CS2R | 2 | [CS2R.md](../../sm120/sass/CS2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| EXIT | 2 | [EXIT.md](../../sm120/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| F2I | 6 | [F2I.md](../../sm120/sass/F2I.md) | Floating Point To Integer Conversion (Conversion Instructions) | NAK: agree |
| FADD | 27 | [FADD.md](../../sm120/sass/FADD.md) | FP32 Add (Floating Point Instructions) | NAK: agree |
| FFMA | 297 | [FFMA.md](../../sm120/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| FMNMX | 8 | [FMNMX.md](../../sm120/sass/FMNMX.md) | FP32 Minimum/Maximum (Floating Point Instructions) | NAK: agree |
| FMUL | 68 | [FMUL.md](../../sm120/sass/FMUL.md) | FP32 Multiply (Floating Point Instructions) | NAK: agree |
| FSETP | 17 | [FSETP.md](../../sm120/sass/FSETP.md) | FP32 Compare And Set Predicate (Floating Point Instructions) | NAK: agree |
| HFMA2 | 16 | [HFMA2.md](../../sm120/sass/HFMA2.md) | FP16 Fused Mutiply Add (Floating Point Instructions) | NAK: agree |
| IADD3 | 361 | [IADD3.md](../../sm120/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 350 | [IMAD.md](../../sm120/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 31 | [ISETP.md](../../sm120/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDC | 13 | [LDC.md](../../sm120/sass/LDC.md) | Load Constant (Load/Store Instructions) | NAK: agree |
| LDCU | 1 | [LDCU.md](../../sm120/sass/LDCU.md) | Load a Value from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |
| LDG | 322 | [LDG.md](../../sm120/sass/LDG.md) | Load from Global Memory (Load/Store Instructions) | — |
| LEA | 43 | [LEA.md](../../sm120/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| LOP3 | 19 | [LOP3.md](../../sm120/sass/LOP3.md) | Logic Operation (Integer Instructions) | NAK: agree |
| MOV | 42 | [MOV.md](../../sm120/sass/MOV.md) | Move (Movement Instructions) | NAK: agree |
| MUFU | 35 | [MUFU.md](../../sm120/sass/MUFU.md) | FP32 Multi Function Operation (Floating Point Instructions) | NAK: agree |
| NOP | 13 | [NOP.md](../../sm120/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| PLOP3 | 1 | [PLOP3.md](../../sm120/sass/PLOP3.md) | Predicate Logic Operation (Predicate Instructions) | NAK: agree |
| RET | 1 | [RET.md](../../sm120/sass/RET.md) | Return From Subroutine (Control Instructions) | — |
| S2R | 2 | [S2R.md](../../sm120/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| SEL | 2 | [SEL.md](../../sm120/sass/SEL.md) | Select Source with Predicate (Movement Instructions) | NAK: agree |
| SHF | 16 | [SHF.md](../../sm120/sass/SHF.md) | Funnel Shift (Integer Instructions) | NAK: agree |
| STG | 8 | [STG.md](../../sm120/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |
| UI2F | 6 | *not in KB corpus* | — | — |

## sm_89 vs sm_120 divergence summary

Same source PTX, two toolchain targets. Opcode sets are per-mnemonic (nvspas form bits ignored). Renames/replacements cite the sm120 KB divergence notes ([verify/RESULTS.md](../../sm120/verify/RESULTS.md), [README](../../sm120/README.md)).

**Shared opcodes (27):** `BRA`, `BSSY`, `BSYNC`, `CALL`, `CS2R`, `EXIT`, `F2I`, `FADD`, `FFMA`, `FMNMX`, `FMUL`, `FSETP`, `IADD3`, `IMAD`, `ISETP`, `LDG`, `LEA`, `LOP3`, `MOV`, `MUFU`, `NOP`, `PLOP3`, `RET`, `S2R`, `SEL`, `SHF`, `STG`

### Replaced (sm_89 opcode -> sm_120 successor, per KB)

| sm_89 | sm_120 (KB finding) | observed here on sm_120 |
|---|---|---|
| `ULDC` | LDCU | yes |

### Emitted on sm_89 but not on sm_120

| opcode | KB explanation |
|---|---|
| `I2F` | not emitted by this input on sm_120; no rename in the KB divergence notes (may still exist in the sm_120 ISA) |

### Emitted on sm_120 but not on sm_89 (new/renamed-in opcodes)

`HFMA2`, `LDC`, `LDCU`, `UI2F`

Full per-arch tables above; the general (input-independent) divergence catalog lives in [sm120/verify/RESULTS.md](../../sm120/verify/RESULTS.md).


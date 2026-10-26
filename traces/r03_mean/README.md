# Trace: r03_mean

- Source: gen/trace_src/base/r03_mean.ptx
- Generated: 2026-10-26 03:40 UTC
- Tools: ptxas `Cuda compilation tools, release 12.9, V12.9.86`, nvdisasm `Cuda compilation tools, release 12.9, V12.9.88`, both `-O3`
- The sm_120 stage consumes a header-retargeted copy of the same PTX (`.target sm_120`, `.version` bumped to >= 8.7); the body is untouched.

- **sm_89: 216 SASS instructions, 29 distinct opcodes**
- **sm_120: 224 SASS instructions, 34 distinct opcodes**
## sm_89 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BAR | 3 | [BAR.md](../../sm89/sass/BAR.md) | Barrier Synchronization (Miscellaneous Instructions) | NAK: agree |
| BRA | 23 | [BRA.md](../../sm89/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| BSSY | 3 | [BSSY.md](../../sm89/sass/BSSY.md) | Barrier Set Convergence Synchronization Point (Control Instructions) | NAK: agree |
| BSYNC | 3 | [BSYNC.md](../../sm89/sass/BSYNC.md) | Synchronize Threads on a Convergence Barrier (Control Instructions) | NAK: agree |
| CALL | 1 | [CALL.md](../../sm89/sass/CALL.md) | Call Function (Control Instructions) | — |
| EXIT | 3 | [EXIT.md](../../sm89/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| FADD | 16 | [FADD.md](../../sm89/sass/FADD.md) | FP32 Add (Floating Point Instructions) | NAK: agree |
| FCHK | 1 | [FCHK.md](../../sm89/sass/FCHK.md) | Floating-point Range Check (Floating Point Instructions) | — |
| FFMA | 17 | [FFMA.md](../../sm89/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| FSETP | 6 | [FSETP.md](../../sm89/sass/FSETP.md) | FP32 Compare And Set Predicate (Floating Point Instructions) | NAK: agree |
| IADD3 | 15 | [IADD3.md](../../sm89/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 32 | [IMAD.md](../../sm89/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 20 | [ISETP.md](../../sm89/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDG | 8 | [LDG.md](../../sm89/sass/LDG.md) | Load from Global Memory (Load/Store Instructions) | — |
| LDS | 5 | [LDS.md](../../sm89/sass/LDS.md) | Load within Shared Memory Window (Load/Store Instructions) | — |
| LEA | 1 | [LEA.md](../../sm89/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| LOP3 | 18 | [LOP3.md](../../sm89/sass/LOP3.md) | Logic Operation (Integer Instructions) | NAK: agree |
| MOV | 1 | [MOV.md](../../sm89/sass/MOV.md) | Move (Movement Instructions) | NAK: agree |
| MUFU | 3 | [MUFU.md](../../sm89/sass/MUFU.md) | FP32 Multi Function Operation (Floating Point Instructions) | NAK: agree |
| NOP | 8 | [NOP.md](../../sm89/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| PLOP3 | 7 | [PLOP3.md](../../sm89/sass/PLOP3.md) | Predicate Logic Operation (Predicate Instructions) | NAK: agree |
| RET | 1 | [RET.md](../../sm89/sass/RET.md) | Return From Subroutine (Control Instructions) | — |
| S2R | 2 | [S2R.md](../../sm89/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| SEL | 2 | [SEL.md](../../sm89/sass/SEL.md) | Select Source with Predicate (Movement Instructions) | NAK: agree |
| SHF | 7 | [SHF.md](../../sm89/sass/SHF.md) | Funnel Shift (Integer Instructions) | NAK: agree |
| SHFL | 5 | [SHFL.md](../../sm89/sass/SHFL.md) | Warp Wide Register Shuffle (Movement Instructions) | NAK: agree |
| STG | 1 | [STG.md](../../sm89/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |
| STS | 3 | [STS.md](../../sm89/sass/STS.md) | Store to Shared Memory (Load/Store Instructions) | — |
| ULDC | 1 | [ULDC.md](../../sm89/sass/ULDC.md) | Load from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |

## sm_120 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BAR | 3 | [BAR.md](../../sm120/sass/BAR.md) | Barrier Synchronization (Miscellaneous Instructions) | NAK: agree |
| BRA | 23 | [BRA.md](../../sm120/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| BSSY | 3 | [BSSY.md](../../sm120/sass/BSSY.md) | Barrier Set Convergence Synchronization Point (Control Instructions) | NAK: agree |
| BSYNC | 3 | [BSYNC.md](../../sm120/sass/BSYNC.md) | Synchronize Threads on a Convergence Barrier (Control Instructions) | NAK: agree |
| CALL | 1 | [CALL.md](../../sm120/sass/CALL.md) | Call Function (Control Instructions) | — |
| EXIT | 3 | [EXIT.md](../../sm120/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| FADD | 16 | [FADD.md](../../sm120/sass/FADD.md) | FP32 Add (Floating Point Instructions) | NAK: agree |
| FCHK | 1 | [FCHK.md](../../sm120/sass/FCHK.md) | Floating-point Range Check (Floating Point Instructions) | — |
| FFMA | 17 | [FFMA.md](../../sm120/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| FSETP | 6 | [FSETP.md](../../sm120/sass/FSETP.md) | FP32 Compare And Set Predicate (Floating Point Instructions) | NAK: agree |
| HFMA2 | 2 | [HFMA2.md](../../sm120/sass/HFMA2.md) | FP16 Fused Mutiply Add (Floating Point Instructions) | NAK: agree |
| IADD3 | 20 | [IADD3.md](../../sm120/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 10 | [IMAD.md](../../sm120/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 20 | [ISETP.md](../../sm120/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDC | 6 | [LDC.md](../../sm120/sass/LDC.md) | Load Constant (Load/Store Instructions) | NAK: agree |
| LDCU | 1 | [LDCU.md](../../sm120/sass/LDCU.md) | Load a Value from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |
| LDG | 8 | [LDG.md](../../sm120/sass/LDG.md) | Load from Global Memory (Load/Store Instructions) | — |
| LDS | 5 | [LDS.md](../../sm120/sass/LDS.md) | Load within Shared Memory Window (Load/Store Instructions) | — |
| LEA | 4 | [LEA.md](../../sm120/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| LOP3 | 18 | [LOP3.md](../../sm120/sass/LOP3.md) | Logic Operation (Integer Instructions) | NAK: agree |
| MOV | 8 | [MOV.md](../../sm120/sass/MOV.md) | Move (Movement Instructions) | NAK: agree |
| MUFU | 3 | [MUFU.md](../../sm120/sass/MUFU.md) | FP32 Multi Function Operation (Floating Point Instructions) | NAK: agree |
| NOP | 12 | [NOP.md](../../sm120/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| PLOP3 | 7 | [PLOP3.md](../../sm120/sass/PLOP3.md) | Predicate Logic Operation (Predicate Instructions) | NAK: agree |
| RET | 1 | [RET.md](../../sm120/sass/RET.md) | Return From Subroutine (Control Instructions) | — |
| S2R | 2 | [S2R.md](../../sm120/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| S2UR | 1 | [S2UR.md](../../sm120/sass/S2UR.md) | Move Special Register to Uniform Register (Uniform Datapath Instructions) | — |
| SEL | 2 | [SEL.md](../../sm120/sass/SEL.md) | Select Source with Predicate (Movement Instructions) | NAK: agree |
| SHF | 7 | [SHF.md](../../sm120/sass/SHF.md) | Funnel Shift (Integer Instructions) | NAK: agree |
| SHFL | 5 | [SHFL.md](../../sm120/sass/SHFL.md) | Warp Wide Register Shuffle (Movement Instructions) | NAK: agree |
| STG | 1 | [STG.md](../../sm120/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |
| STS | 3 | [STS.md](../../sm120/sass/STS.md) | Store to Shared Memory (Load/Store Instructions) | — |
| ULEA | 1 | [ULEA.md](../../sm120/sass/ULEA.md) | Uniform Load Effective Address (Uniform Datapath Instructions) | — |
| UMOV | 1 | [UMOV.md](../../sm120/sass/UMOV.md) | Uniform Move (Uniform Datapath Instructions) | — |

## sm_89 vs sm_120 divergence summary

Same source PTX, two toolchain targets. Opcode sets are per-mnemonic (nvspas form bits ignored). Renames/replacements cite the sm120 KB divergence notes ([verify/RESULTS.md](../../sm120/verify/RESULTS.md), [README](../../sm120/README.md)).

**Shared opcodes (28):** `BAR`, `BRA`, `BSSY`, `BSYNC`, `CALL`, `EXIT`, `FADD`, `FCHK`, `FFMA`, `FSETP`, `IADD3`, `IMAD`, `ISETP`, `LDG`, `LDS`, `LEA`, `LOP3`, `MOV`, `MUFU`, `NOP`, `PLOP3`, `RET`, `S2R`, `SEL`, `SHF`, `SHFL`, `STG`, `STS`

### Replaced (sm_89 opcode -> sm_120 successor, per KB)

| sm_89 | sm_120 (KB finding) | observed here on sm_120 |
|---|---|---|
| `ULDC` | LDCU | yes |

### Emitted on sm_120 but not on sm_89 (new/renamed-in opcodes)

`HFMA2`, `LDC`, `LDCU`, `S2UR`, `ULEA`, `UMOV`

Full per-arch tables above; the general (input-independent) divergence catalog lives in [sm120/verify/RESULTS.md](../../sm120/verify/RESULTS.md).


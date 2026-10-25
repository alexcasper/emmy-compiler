# Trace: m01_matmul_512

- Source: task/problems/m01_matmul_512
- Generated: 2026-10-25 20:05 UTC
- Tools: ptxas `Cuda compilation tools, release 12.9, V12.9.86`, nvdisasm `Cuda compilation tools, release 12.9, V12.9.88`, both `-O3`
- The sm_120 stage consumes a header-retargeted copy of the same PTX (`.target sm_120`, `.version` bumped to >= 8.7); the body is untouched.

- **sm_89: 512 SASS instructions, 25 distinct opcodes**
- **sm_120: 536 SASS instructions, 31 distinct opcodes**
## sm_89 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BAR | 2 | [BAR.md](../../sm89/sass/BAR.md) | Barrier Synchronization (Miscellaneous Instructions) | NAK: agree |
| BRA | 3 | [BRA.md](../../sm89/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| CS2R | 2 | [CS2R.md](../../sm89/sass/CS2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| DEPBAR | 1 | [DEPBAR.md](../../sm89/sass/DEPBAR.md) | Dependency Barrier (Miscellaneous Instructions) | — |
| EXIT | 2 | [EXIT.md](../../sm89/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| F2I | 11 | [F2I.md](../../sm89/sass/F2I.md) | Floating Point To Integer Conversion (Conversion Instructions) | NAK: agree |
| FFMA | 4 | [FFMA.md](../../sm89/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| I2F | 11 | [I2F.md](../../sm89/sass/I2F.md) | Integer To Floating Point Conversion (Conversion Instructions) | NAK: agree |
| IABS | 11 | [IABS.md](../../sm89/sass/IABS.md) | Integer Absolute Value (Integer Instructions) | NAK: agree |
| IADD3 | 107 | [IADD3.md](../../sm89/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 213 | [IMAD.md](../../sm89/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 55 | [ISETP.md](../../sm89/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDGDEPBAR | 3 | [LDGDEPBAR.md](../../sm89/sass/LDGDEPBAR.md) | Global Load Dependency Barrier (Load/Store Instructions) | — |
| LDGSTS | 9 | [LDGSTS.md](../../sm89/sass/LDGSTS.md) | Asynchronous Global to Shared Memcopy (Load/Store Instructions) | — |
| LDS | 7 | [LDS.md](../../sm89/sass/LDS.md) | Load within Shared Memory Window (Load/Store Instructions) | — |
| LEA | 9 | [LEA.md](../../sm89/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| LOP3 | 4 | [LOP3.md](../../sm89/sass/LOP3.md) | Logic Operation (Integer Instructions) | NAK: agree |
| MOV | 4 | [MOV.md](../../sm89/sass/MOV.md) | Move (Movement Instructions) | NAK: agree |
| MUFU | 11 | [MUFU.md](../../sm89/sass/MUFU.md) | FP32 Multi Function Operation (Floating Point Instructions) | NAK: agree |
| NOP | 8 | [NOP.md](../../sm89/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| S2R | 2 | [S2R.md](../../sm89/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| SEL | 27 | [SEL.md](../../sm89/sass/SEL.md) | Select Source with Predicate (Movement Instructions) | NAK: agree |
| SHF | 3 | [SHF.md](../../sm89/sass/SHF.md) | Funnel Shift (Integer Instructions) | NAK: agree |
| STG | 2 | [STG.md](../../sm89/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |
| ULDC | 1 | [ULDC.md](../../sm89/sass/ULDC.md) | Load from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |

## sm_120 opcode -> KB cross-ref

| opcode | count | KB page | NVIDIA description | NAK cross-check |
|---|---|---|---|---|
| BAR | 2 | [BAR.md](../../sm120/sass/BAR.md) | Barrier Synchronization (Miscellaneous Instructions) | NAK: agree |
| BRA | 3 | [BRA.md](../../sm120/sass/BRA.md) | Relative Branch (Control Instructions) | NAK: agree |
| CS2R | 2 | [CS2R.md](../../sm120/sass/CS2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| DEPBAR | 1 | [DEPBAR.md](../../sm120/sass/DEPBAR.md) | Dependency Barrier (Miscellaneous Instructions) | — |
| EXIT | 2 | [EXIT.md](../../sm120/sass/EXIT.md) | Exit Program (Control Instructions) | NAK: agree |
| F2I | 11 | [F2I.md](../../sm120/sass/F2I.md) | Floating Point To Integer Conversion (Conversion Instructions) | NAK: agree |
| FFMA | 4 | [FFMA.md](../../sm120/sass/FFMA.md) | FP32 Fused Multiply and Add (Floating Point Instructions) | NAK: agree |
| HFMA2 | 6 | [HFMA2.md](../../sm120/sass/HFMA2.md) | FP16 Fused Mutiply Add (Floating Point Instructions) | NAK: agree |
| IABS | 11 | [IABS.md](../../sm120/sass/IABS.md) | Integer Absolute Value (Integer Instructions) | NAK: agree |
| IADD3 | 162 | [IADD3.md](../../sm120/sass/IADD3.md) | 3-input Integer Addition (Integer Instructions) | NAK: agree |
| IMAD | 118 | [IMAD.md](../../sm120/sass/IMAD.md) | Integer Multiply And Add (Integer Instructions) | NAK: agree |
| ISETP | 54 | [ISETP.md](../../sm120/sass/ISETP.md) | Integer Compare And Set Predicate (Integer Instructions) | NAK: agree |
| LDC | 6 | [LDC.md](../../sm120/sass/LDC.md) | Load Constant (Load/Store Instructions) | NAK: agree |
| LDCU | 1 | [LDCU.md](../../sm120/sass/LDCU.md) | Load a Value from Constant Memory into a Uniform Register (Uniform Datapath Instructions) | — |
| LDGDEPBAR | 3 | [LDGDEPBAR.md](../../sm120/sass/LDGDEPBAR.md) | Global Load Dependency Barrier (Load/Store Instructions) | — |
| LDGSTS | 9 | [LDGSTS.md](../../sm120/sass/LDGSTS.md) | Asynchronous Global to Shared Memcopy (Load/Store Instructions) | — |
| LDS | 10 | [LDS.md](../../sm120/sass/LDS.md) | Load within Shared Memory Window (Load/Store Instructions) | — |
| LEA | 24 | [LEA.md](../../sm120/sass/LEA.md) | LOAD Effective Address (Integer Instructions) | NAK: agree |
| LOP3 | 4 | [LOP3.md](../../sm120/sass/LOP3.md) | Logic Operation (Integer Instructions) | NAK: agree |
| MOV | 27 | [MOV.md](../../sm120/sass/MOV.md) | Move (Movement Instructions) | NAK: agree |
| MUFU | 11 | [MUFU.md](../../sm120/sass/MUFU.md) | FP32 Multi Function Operation (Floating Point Instructions) | NAK: agree |
| NOP | 14 | [NOP.md](../../sm120/sass/NOP.md) | No Operation (Miscellaneous Instructions) | NAK: agree |
| S2R | 2 | [S2R.md](../../sm120/sass/S2R.md) | Move Special Register to Register (Miscellaneous Instructions) | NAK: agree |
| S2UR | 2 | [S2UR.md](../../sm120/sass/S2UR.md) | Move Special Register to Uniform Register (Uniform Datapath Instructions) | — |
| SEL | 27 | [SEL.md](../../sm120/sass/SEL.md) | Select Source with Predicate (Movement Instructions) | NAK: agree |
| STG | 2 | [STG.md](../../sm120/sass/STG.md) | Store to Global Memory (Load/Store Instructions) | — |
| UI2F | 11 | *not in KB corpus* | — | — |
| UIADD3 | 1 | [UIADD3.md](../../sm120/sass/UIADD3.md) | Uniform Integer Addition (Uniform Datapath Instructions) | — |
| UISETP | 1 | [UISETP.md](../../sm120/sass/UISETP.md) | Uniform Integer Compare and Set Uniform Predicate (Uniform Datapath Instructions) | — |
| ULEA | 2 | [ULEA.md](../../sm120/sass/ULEA.md) | Uniform Load Effective Address (Uniform Datapath Instructions) | — |
| UMOV | 3 | [UMOV.md](../../sm120/sass/UMOV.md) | Uniform Move (Uniform Datapath Instructions) | — |

## sm_89 vs sm_120 divergence summary

Same source PTX, two toolchain targets. Opcode sets are per-mnemonic (nvspas form bits ignored). Renames/replacements cite the sm120 KB divergence notes ([verify/RESULTS.md](../../sm120/verify/RESULTS.md), [README](../../sm120/README.md)).

**Shared opcodes (22):** `BAR`, `BRA`, `CS2R`, `DEPBAR`, `EXIT`, `F2I`, `FFMA`, `IABS`, `IADD3`, `IMAD`, `ISETP`, `LDGDEPBAR`, `LDGSTS`, `LDS`, `LEA`, `LOP3`, `MOV`, `MUFU`, `NOP`, `S2R`, `SEL`, `STG`

### Replaced (sm_89 opcode -> sm_120 successor, per KB)

| sm_89 | sm_120 (KB finding) | observed here on sm_120 |
|---|---|---|
| `ULDC` | LDCU | yes |

### Emitted on sm_89 but not on sm_120

| opcode | KB explanation |
|---|---|
| `I2F` | not emitted by this input on sm_120; no rename in the KB divergence notes (may still exist in the sm_120 ISA) |
| `SHF` | not emitted by this input on sm_120; no rename in the KB divergence notes (may still exist in the sm_120 ISA) |

### Emitted on sm_120 but not on sm_89 (new/renamed-in opcodes)

`HFMA2`, `LDC`, `LDCU`, `S2UR`, `UI2F`, `UIADD3`, `UISETP`, `ULEA`, `UMOV`

Full per-arch tables above; the general (input-independent) divergence catalog lives in [sm120/verify/RESULTS.md](../../sm120/verify/RESULTS.md).


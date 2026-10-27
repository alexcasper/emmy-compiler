#!/usr/bin/env python3
"""Ground-truth PTX -> SASS probes for sm_120, compiled with NVIDIA's real ptxas + nvdisasm.

Each probe is a small PTX kernel plus the SASS opcodes we claim it lowers to on sm_120.
Expectations marked `hyp:` are hypotheses carried over from the sm_89 KB and are tested,
not assumed: a MISSING status is a divergence finding, not a harness bug.  Probes that
sm_89 rejected for arch reasons (sm_90+/sm_100+ instructions) are re-run as *acceptance*
probes here, since Blackwell consumer may accept them; probes expected to stay rejected
(sm_90a / sm_100a family gates) are marked reject=True.

The runner compiles every probe, disassembles it with `nvdisasm -hex -c`, and checks:
  1. the claimed SASS opcodes really appear (expectation check),
  2. the scheduling control-code layout (whether the sm_89 scoreboard field layout
     -- write barrier bits 110-112, read barrier 113-115, wait mask 116-121 --
     still holds on sm_120).

Tools (official NVIDIA binaries, no GPU needed):
  PTXAS=/mnt/d/ops/emmy/toolchain/cuda12.9/bin/ptxas \
  NVDISASM=/mnt/d/ops/emmy/toolchain/cuda12.9/bin/nvdisasm \
  env -u PYTHONPATH python3 sm120/verify/probes.py

Writes sm120/verify/RESULTS.md (human-readable evidence, full SASS listings) and
sm120/verify/results.json (consumed by tools/build_sass.py for the evidence column).
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PTXAS = os.environ.get("PTXAS", "ptxas")
NVDISASM = os.environ.get("NVDISASM", "nvdisasm")
ARCH = "sm_120"

HEADER = """.version 8.8
.target sm_120
.address_size 64
{decls}
{funcs}
.visible .entry k(.param .u64 p, .param .u64 t)
{{
 .reg .b32 r<40>; .reg .b64 rd<16>; .reg .f32 f<40>; .reg .f64 d<16>; .reg .pred q<8>; .reg .b16 h<8>; .reg .b8 bb<4>;
 ld.param.u64 rd0, [p]; cvta.to.global.u64 rd1, rd0;
 mov.u32 r30, %tid.x; mul.wide.u32 rd2, r30, 64; add.s64 rd1, rd1, rd2;
 ld.global.u32 r1, [rd1]; ld.global.u32 r2, [rd1+4]; ld.global.u32 r3, [rd1+8];
 ld.global.f32 f1, [rd1+12]; ld.global.f32 f2, [rd1+16]; ld.global.f32 f3, [rd1+20];
 ld.global.f64 d1, [rd1+24]; ld.global.f64 d2, [rd1+32]; ld.global.u64 rd3, [rd1+40];
{body}
 ret;
}}
"""

# (name, PTX feature being probed, expected SASS opcodes, body, extra module-scope decls, extra funcs)
P = []


def probe(name, ptx, expect, body, decls="", funcs="", reject=False):
    """reject=True: ptxas must refuse this PTX on sm_120."""
    P.append(dict(name=name, ptx=ptx, expect=expect.split(), body=body, decls=decls, funcs=funcs, reject=reject))


ST = " st.global.f32 [rd1], {};"
STI = " st.global.u32 [rd1], {};"
STD = " st.global.f64 [rd1], {};"

# ---- FP32  (expectations = sm_89 hypotheses, verified/updated from sm_120 output)
probe("fadd", "add.f32", "FADD", " add.f32 f4, f1, f2;" + ST.format("f4"))
probe("ffma", "fma.rn.f32", "FFMA", " fma.rn.f32 f4, f1, f2, f3;" + ST.format("f4"))
probe("fmul", "mul.f32", "FMUL", " mul.f32 f4, f1, f2;" + ST.format("f4"))
probe("fminmax", "min.f32 / max.f32", "FMNMX", " min.f32 f4, f1, f2; max.f32 f5, f4, f3;" + ST.format("f5"))
probe("fminmax_nan", "min.NaN.f32 (PTX 8.6 NaN-propagating min/max)", "FMNMX",
      " min.NaN.f32 f4, f1, f2; max.NaN.f32 f5, f4, f3;" + ST.format("f5"))
probe("fsetp_selp", "setp.lt.f32 + selp.f32 (both arms computed)", "FSETP FSEL",
      " add.f32 f4, f1, f2; mul.f32 f5, f1, f3; setp.lt.f32 q1, f4, f5; selp.f32 f6, f4, f5, q1;" + ST.format("f6"))
probe("selp_to_predicated_load", "selp.f32 between two loaded values", "FSETP",
      " setp.lt.f32 q1, f1, f2; selp.f32 f4, f1, f3, q1;" + ST.format("f4"))
probe("fset", "set.lt.u32.f32 (hyp: lowered as FSETP + SEL on sm_89)", "FSETP SEL",
      " set.lt.u32.f32 r4, f1, f2;" + STI.format("r4"))
probe("fdiv_rn", "div.rn.f32 (IEEE division)", "FCHK MUFU FFMA CALL",
      " div.rn.f32 f4, f1, f2;" + ST.format("f4"))
for op in ("rcp.approx.f32", "rsqrt.approx.f32", "sqrt.approx.f32", "lg2.approx.f32", "ex2.approx.f32",
           "sin.approx.f32", "cos.approx.f32", "tanh.approx.f32"):
    probe("mufu_" + op.split(".")[0], op, "MUFU", f" {op} f4, f1;" + ST.format("f4"))
probe("frnd", "cvt.rmi.f32.f32 (floor)", "FRND", " cvt.rmi.f32.f32 f4, f1;" + ST.format("f4"))
# ---- FP64
probe("dadd", "add.f64", "DADD", " add.f64 d3, d1, d2;" + STD.format("d3"))
probe("dfma", "fma.rn.f64", "DFMA", " fma.rn.f64 d3, d1, d2, d1;" + STD.format("d3"))
probe("dmul", "mul.f64", "DMUL", " mul.f64 d3, d1, d2;" + STD.format("d3"))
probe("dsetp", "setp.lt.f64", "DSETP", " setp.lt.f64 q1, d1, d2; selp.f64 d3, d1, d2, q1;" + STD.format("d3"))
# ---- FP16x2 / BF16x2  (divergence: on sm_120 there is no HADD2/HMUL2 -- ptxas folds
# half adds/multiplies into the FMA pipe as HFMA2 with constant multipliers)
probe("hadd2", "add.f16x2 (divergence: HFMA2 folding, no HADD2 on sm_120)", "HFMA2",
      " add.f16x2 r4, r1, r2;" + STI.format("r4"))
probe("hfma2", "fma.rn.f16x2", "HFMA2", " fma.rn.f16x2 r4, r1, r2, r3;" + STI.format("r4"))
probe("hfma2_bf16", "fma.rn.bf16x2", "HFMA2", " fma.rn.bf16x2 r4, r1, r2, r3;" + STI.format("r4"))
probe("hmul2", "mul.f16x2 (divergence: HFMA2 folding, no HMUL2 on sm_120)", "HFMA2",
      " mul.f16x2 r4, r1, r2;" + STI.format("r4"))
probe("hmnmx2", "min.f16x2", "HMNMX2", " min.f16x2 r4, r1, r2;" + STI.format("r4"))
probe("hsetp2", "setp.lt.f16x2", "HSETP2",
      " setp.lt.f16x2 q1|q2, r1, r2; selp.b32 r4, r1, r2, q1; selp.b32 r5, r4, r3, q2;" + STI.format("r5"))
probe("hset2", "set.lt.f16x2.f16x2", "HSET2", " set.lt.f16x2.f16x2 r4, r1, r2;" + STI.format("r4"))
# ---- Integer
probe("iadd", "add.s32 / sub.s32", "IADD3", " add.s32 r4, r1, r2; sub.s32 r5, r4, r3;" + STI.format("r5"))
probe("iadd64", "add.s64 (divergence: single IADD.64, no IADD3 carry pair)", "IADD",
      " add.s64 rd4, rd3, rd3; st.global.u64 [rd1], rd4;")
probe("imad", "mad.lo.s32", "IMAD", " mad.lo.s32 r4, r1, r2, r3;" + STI.format("r4"))
probe("imad_wide", "mul.wide.s32", "IMAD", " mul.wide.s32 rd4, r1, r2; st.global.u64 [rd1], rd4;")
probe("imad_hi", "mul.hi.u32", "IMAD", " mul.hi.u32 r4, r1, r2;" + STI.format("r4"))
probe("iabs", "abs.s32", "IABS", " abs.s32 r4, r1;" + STI.format("r4"))
probe("imnmx", "min.s32 (divergence: VIMNMX, sm_89's IMNMX is gone)", "VIMNMX",
      " min.s32 r4, r1, r2;" + STI.format("r4"))
probe("isetp_pred", "setp.lt.s32 + selp.b32 (hyp: if-converted, no SEL)", "ISETP",
      " add.s32 r4, r1, r2; xor.b32 r5, r1, r3; setp.lt.s32 q1, r1, r3; selp.b32 r6, r4, r5, q1;" + STI.format("r6"))
probe("imnmx_from_selp", "setp.lt.s32 + selp.b32 forming min() (ptxas recognizes min; VIMNMX)", "VIMNMX",
      " add.s32 r4, r1, r2; xor.b32 r5, r1, r3; setp.lt.s32 q1, r4, r5; selp.b32 r6, r4, r5, q1;" + STI.format("r6"))
probe("lea", "shl.b32 + add.s32", "LEA", " shl.b32 r4, r1, 3; add.s32 r5, r4, r2;" + STI.format("r5"))
probe("lea64", "pointer + (sign-extended s32 index << 2)", "LEA",
      " cvt.s64.s32 rd4, r1; shl.b64 rd4, rd4, 2; add.s64 rd5, rd3, rd4; st.global.u32 [rd5], r2;")
probe("lop3", "and/xor/or of 3 values", "LOP3",
      " and.b32 r4, r1, r2; xor.b32 r5, r4, r3; or.b32 r6, r5, r1;" + STI.format("r6"))
probe("shf", "shf.l.wrap.b32", "SHF", " shf.l.wrap.b32 r4, r1, r2, r3;" + STI.format("r4"))
probe("shl64", "shl.b64 by register", "SHF", " shl.b64 rd4, rd3, r1; st.global.u64 [rd1], rd4;")
probe("prmt", "prmt.b32", "PRMT", " prmt.b32 r4, r1, r2, 0x5140;" + STI.format("r4"))
probe("sgxt", "bfe.s32 (signed field extract)", "SGXT", " bfe.s32 r4, r1, r2, r3;" + STI.format("r4"))
probe("bmsk", "bmsk.clamp.b32", "BMSK", " bmsk.clamp.b32 r4, r1, r2;" + STI.format("r4"))
probe("flo", "bfind.u32 / clz.b32", "FLO", " bfind.u32 r4, r1; clz.b32 r5, r2; add.s32 r6, r4, r5;" + STI.format("r6"))
probe("brev", "brev.b32", "BREV", " brev.b32 r4, r1;" + STI.format("r4"))
probe("popc", "popc.b32", "POPC", " popc.b32 r4, r1;" + STI.format("r4"))
probe("idp", "dp4a.s32.s32", "IDP", " dp4a.s32.s32 r4, r1, r2, r3;" + STI.format("r4"))
probe("vabsdiff", "vabsdiff.u32.u32.u32 (hyp: emulated, not VABSDIFF on sm_89)", "",
      " vabsdiff.u32.u32.u32 r4, r1, r2;" + STI.format("r4"))
probe("vabsdiff2", "vabsdiff2.u32.u32.u32 (observe)", "",
      " vabsdiff2.u32.u32.u32 r4, r1, r2, r3;" + STI.format("r4"))
probe("vabsdiff4", "vabsdiff4.u32.u32.u32.add (divergence: VABSDIFF4 gone; emulated via VIMNMX.U8x4 + VIADD.U8x4 + IDP.4A)",
      "VIMNMX VIADD IDP",
      " vabsdiff4.u32.u32.u32.add r4, r1, r2, r3;" + STI.format("r4"))
# ---- Conversion
probe("f2f", "cvt.rn.f32.f64", "F2F", " cvt.rn.f32.f64 f4, d1;" + ST.format("f4"))
probe("f2i", "cvt.rzi.s32.f32", "F2I", " cvt.rzi.s32.f32 r4, f1;" + STI.format("r4"))
probe("i2fp", "cvt.rn.f32.s32", "I2FP", " cvt.rn.f32.s32 f4, r1;" + ST.format("f4"))
probe("i2f", "cvt.rn.f64.s32", "I2F", " cvt.rn.f64.s32 d3, r1;" + STD.format("d3"))
probe("f2fp_f16", "cvt.rn.f16x2.f32", "F2FP", " cvt.rn.f16x2.f32 r4, f1, f2;" + STI.format("r4"))
probe("f2fp_bf16", "cvt.rn.bf16x2.f32", "F2FP", " cvt.rn.bf16x2.f32 r4, f1, f2;" + STI.format("r4"))
probe("f2fp_e4m3", "cvt.rn.satfinite.e4m3x2.f32 (FP8)", "F2FP",
      " cvt.rn.satfinite.e4m3x2.f32 h1, f1, f2; cvt.u32.u16 r4, h1;" + STI.format("r4"))
probe("f2fp_e2m1", "cvt.rn.satfinite.e2m1x2.f32 (FP4, PTX 8.7+) -- REJECTED on sm_120 (sm_100a-family feature)",
      "", " cvt.rn.satfinite.e2m1x2.f32 bb1, f1, f2; cvt.u32.u8 r4, bb1;" + STI.format("r4"), reject=True)
probe("i2i", "cvt.sat.s8.s32", "I2I", " cvt.sat.s8.s32 r4, r1;" + STI.format("r4"))
probe("i2ip", "cvt.pack.sat.s8.s32.b32", "I2IP", " cvt.pack.sat.s8.s32.b32 r4, r1, r2, r3;" + STI.format("r4"))
probe("f2ip", "cvt.rni.sat.s8.f32 (observe only)", "", " cvt.rni.sat.s8.f32 r4, f1;" + STI.format("r4"))
# ---- Movement / warp
probe("shfl", "shfl.sync.bfly.b32", "SHFL", " shfl.sync.bfly.b32 r4, r1, 1, 0x1f, -1;" + STI.format("r4"))
probe("vote", "vote.sync.ballot.b32", "VOTE", " setp.ne.s32 q1, r1, 0; vote.sync.ballot.b32 r4, q1, -1;" + STI.format("r4"))
probe("match", "match.any.sync.b32", "MATCH", " match.any.sync.b32 r4, r1, -1;" + STI.format("r4"))
probe("redux", "redux.sync.add.u32", "REDUX", " redux.sync.add.u32 r4, r1, -1;" + STI.format("r4"))
probe("redux_f32", "redux.sync.min.f32 -- REJECTED on sm_120 (sm_100a-family feature; ptxas: not supported on .target sm_120)",
      "", " redux.sync.min.f32 f4, f1, -1;" + ST.format("f4"), reject=True)
probe("s2r", "mov.u32 %laneid", "S2R", " mov.u32 r4, %laneid;" + STI.format("r4"))
probe("cs2r", "mov.u64 %clock64", "CS2R", " mov.u64 rd4, %clock64; st.global.u64 [rd1], rd4;")
probe("s2r_ctaid", "mov.u32 %ctaid.x stored directly", "S2R", " mov.u32 r4, %ctaid.x;" + STI.format("r4"))
probe("s2ur", "%ctaid.x used in uniform address math (observe)", "",
      " mov.u32 r4, %ctaid.x; mul.wide.u32 rd4, r4, 1024; add.s64 rd5, rd0, rd4; cvta.to.global.u64 rd6, rd5;"
      " ld.global.u32 r5, [rd6]; add.s32 r6, r5, r1;" + STI.format("r6"))
probe("movm", "movmatrix.sync.aligned.m8n8.trans.b16", "MOVM",
      " movmatrix.sync.aligned.m8n8.trans.b16 r4, r1;" + STI.format("r4"))
# ---- Memory
probe("lds_sts", "ld.shared / st.shared", "LDS STS",
      " mov.u32 r5, sm; shl.b32 r6, r30, 2; add.s32 r5, r5, r6; st.shared.u32 [r5], r1; bar.sync 0;"
      " ld.shared.u32 r4, [r5+4];" + STI.format("r4"), decls=".shared .align 16 .b8 sm[4096];")
probe("ld_generic", "ld (generic pointer)", "LD", " ld.u32 r4, [rd3];" + STI.format("r4"))
probe("st_generic", "st (generic pointer)", "ST", " st.u32 [rd3], r1;")
probe("ldl_stl", "dynamically indexed .local array", "LDL STL",
      " .local .align 4 .b8 la[256]; mov.u64 rd4, la; and.b32 r5, r1, 63; mul.wide.u32 rd5, r5, 4;"
      " add.s64 rd6, rd4, rd5; st.local.u32 [rd6], r2; and.b32 r6, r3, 63; mul.wide.u32 rd7, r6, 4;"
      " add.s64 rd8, rd4, rd7; ld.local.u32 r4, [rd8];" + STI.format("r4"))
probe("ldc", "ld.const with dynamic index", "LDC",
      " mov.u64 rd4, cst; and.b32 r5, r1, 63; mul.wide.u32 rd5, r5, 4; add.s64 rd6, rd4, rd5;"
      " ld.const.u32 r4, [rd6];" + STI.format("r4"), decls=".const .align 4 .b32 cst[64];")
probe("ldg_nc", "ld.global.nc.v4.f32", "LDG", " ld.global.nc.v4.f32 {f4,f5,f6,f7}, [rd1+48]; add.f32 f8, f4, f7;" + ST.format("f8"))
probe("ldg_v4_u32", "ld.global.v4.u32 (vectorized)", "LDG",
      " ld.global.v4.u32 {r10,r11,r12,r13}, [rd1+48]; add.s32 r4, r10, r13;" + STI.format("r4"))
probe("cp_async", "cp.async.cg.shared.global + commit_group + wait_group", "LDGSTS LDGDEPBAR DEPBAR",
      " mov.u32 r5, sm; shl.b32 r6, r30, 4; add.s32 r5, r5, r6; cp.async.cg.shared.global [r5], [rd1], 16;"
      " cp.async.commit_group; cp.async.wait_group 0; bar.sync 0; ld.shared.u32 r4, [r5];" + STI.format("r4"),
      decls=".shared .align 16 .b8 sm[4096];")
probe("ldsm", "ldmatrix.sync.aligned.m8n8.x4.shared.b16", "LDSM",
      " mov.u32 r5, sm; shl.b32 r6, r30, 4; add.s32 r5, r5, r6; st.shared.u32 [r5], r1; bar.sync 0;"
      " ldmatrix.sync.aligned.m8n8.x4.shared.b16 {r10,r11,r12,r13}, [r5]; add.s32 r4, r10, r13;" + STI.format("r4"),
      decls=".shared .align 16 .b8 sm[4096];")
probe("stmatrix", "stmatrix (accepted on sm_120, unlike sm_89; SASS opcode renamed STM -> STSM.16)", "STSM",
      " mov.u32 r5, sm; stmatrix.sync.aligned.m8n8.x1.shared.b16 [r5], {r1};", decls=".shared .align 16 .b8 sm[4096];")
probe("elect", "elect.sync (hyp: sm_90+, accepted here)", "ELECT",
      " elect.sync r4|q1, -1;" + STI.format("r4"))
probe("atomg", "atom.global.add.u32 (result used; new memory-order qualifier form)", "ATOMG",
      " atom.global.add.u32 r4, [rd1], r1;" + STI.format("r4"))
probe("red", "red.global.add.u32 (no result; divergence: REDG with .STRONG.GPU, sm_89's RED is gone)", "REDG",
      " red.global.add.u32 [rd1], r1;")
probe("atoms", "atom.shared.add.u32", "ATOMS",
      " mov.u32 r5, sm; atom.shared.add.u32 r4, [r5], r1;" + STI.format("r4"), decls=".shared .align 16 .b8 sm[64];")
probe("atom_generic", "atom.add.u32 (generic)", "ATOM", " atom.add.u32 r4, [rd3], r1;" + STI.format("r4"))
probe("qspc", "isspacep.shared", "QSPC", " isspacep.shared q1, rd3; selp.u32 r4, 1, 0, q1;" + STI.format("r4"))
probe("cctl", "prefetch.global.L1", "CCTL", " prefetch.global.L1 [rd3];")
# ---- Blackwell-era memory ops (sm_90+/sm_100+ on sm_89 -- acceptance unknown on sm_120)
probe("mapa", "mapa (accepted on sm_120, unlike sm_89; at -O3 trivial forms fold to S2UR/PRMT address math -- no MAPA opcode observed)",
      "S2UR",
      " mov.u32 r7, %cluster_ctarank; cvt.u64.u32 rd5, r7; mapa.u64 rd4, rd5, 1; st.global.u64 [rd1], rd4;")
probe("cp_async_bulk", "cp.async.bulk shared::cta <- global via mbarrier (TMA, sm_90+; accepted on sm_120, rejected on sm_89)", "",
      " mov.u32 r5, sm; mbarrier.init.shared.b64 [r5+64], 1;"
      " cp.async.bulk.shared::cluster.global.mbarrier::complete_tx::bytes [r5], [rd1], 16, [r5+64];"
      " mbarrier.arrive.expect_tx.shared.b64 _, [r5+64], 16;",
      decls=".shared .align 16 .b8 sm[4096];")
probe("griddepcontrol", "griddepcontrol (programmatic dependent launch, sm_90+; rejected on sm_89)", "",
      " griddepcontrol.wait; griddepcontrol.launch_dependents;")
probe("mbarrier", "mbarrier.init / arrive.expect_tx / try_wait (observe)", "",
      " mov.u32 r5, sm; mbarrier.init.shared.b64 [r5+64], 1; mbarrier.arrive.expect_tx.shared.b64 _, [r5+64], 16;"
      " mbarrier.try_wait.parity.shared.b64 q1, [r5+64], 0; selp.u32 r4, 1, 0, q1;" + STI.format("r4"),
      decls=".shared .align 16 .b8 sm[4096];")
probe("st_bulk", "st.bulk.shared::cta (PTX 8.6+; SASS: new UMEMSETS.64 uniform memset)", "UMEMSETS",
      " mov.u32 r5, sm; st.bulk.shared::cta [r5], 256, 0; bar.sync 0; ld.shared.u32 r4, [r5];" + STI.format("r4"),
      decls=".shared .align 16 .b8 sm[4096];")
# ---- Tensor cores
probe("hmma_f16", "mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32", "HMMA",
      " mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
probe("hmma_tf32", "mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32", "HMMA",
      " mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
probe("imma", "mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32", "IMMA",
      " mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32 {r10,r11,r12,r13}, {r1,r2,r3,r1}, {r2,r3}, {r1,r2,r3,r1};"
      " add.s32 r4, r10, r13;" + STI.format("r4"))
probe("dmma", "mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64", "DMMA",
      " mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64 {d3,d4}, {d1}, {d2}, {d1,d2}; add.f64 d5, d3, d4;" + STD.format("d5"))
probe("bmma", "mma.sync b1 (divergence: no BMMA opcode on sm_120; ptxas CALLs an internal sm_10x bit-mma routine built from IMMA.16832.U8.U8 + new MOVM.U4TO8)",
      "CALL MOVM IMMA",
      " mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc {r10,r11,r12,r13}, {r1,r2,r3,r1}, {r2,r3}, {r1,r2,r3,r1};"
      " add.s32 r4, r10, r13;" + STI.format("r4"))
probe("qmma_e4m3", "mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 (FP8)", "QMMA",
      " mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
# ---- Expected to stay rejected on sm_120 (family-gated instructions)
probe("no_wgmma", "wgmma.fence (sm_90a only)", "", " wgmma.fence.sync.aligned;", reject=True)
probe("no_setmaxnreg", "setmaxnreg (sm_90a only)", "", " setmaxnreg.inc.sync.aligned.u32 64;", reject=True)
probe("no_tcgen05", "tcgen05.alloc (sm_100a/sm_100f family; REJECTED on sm_120: .cta_group not supported)",
      "",
      " mov.u32 r5, sm; mov.u32 r6, 32; tcgen05.alloc.cta_group::1.sync.aligned.shared::cta.b64 [r5], r6;",
      decls=".shared .align 16 .b8 sm[4096];", reject=True)
probe("no_tcgen05_mma", "tcgen05.mma (sm_100a family)", "",
      " tcgen05.commit.cta_group::1.mbarrier::arrive::one.shared::cluster.b64 [r5+64], 0;",
      decls=".shared .align 16 .b8 sm[4096];", reject=True)
# ---- Sync / control
probe("bar", "bar.sync 0", "BAR", " st.global.u32 [rd1], r1; bar.sync 0; ld.global.u32 r4, [rd1+4];" + STI.format("r4"))
probe("bar_red", "bar.red.popc.u32", "BAR B2R", " setp.ne.s32 q1, r1, 0; bar.red.popc.u32 r4, 0, q1;" + STI.format("r4"))
probe("membar", "membar.gl", "MEMBAR", " st.global.u32 [rd1], r1; membar.gl; st.global.u32 [rd1+4], r2;")
probe("fence_sys", "fence.sc.sys", "MEMBAR ERRBAR", " st.global.u32 [rd1], r1; fence.sc.sys; st.global.u32 [rd1+4], r2;")
probe("nanosleep", "nanosleep.u32", "NANOSLEEP", " nanosleep.u32 r1;")
probe("warpsync", "bar.warp.sync with partial mask", "WARPSYNC", " bar.warp.sync r1;")
probe("diverge", "data-dependent loop", "BRA",
      " mov.u32 r4, 0; mov.u32 r5, 0;\nLOOP: setp.ge.s32 q1, r5, r1; @q1 bra DONE; add.s32 r4, r4, r5; add.s32 r5, r5, 1; bra LOOP;\nDONE:"
      + STI.format("r4"))
probe("call", ".func .noinline call", "CALL RET",
      " { .param .b32 a; .param .b32 rv; st.param.b32 [a], r1; call.uni (rv), fn, (a); ld.param.b32 r4, [rv]; }"
      + STI.format("r4"),
      funcs=".func (.param .b32 o) fn(.param .b32 i) { .reg .b32 x; ld.param.b32 x, [i];"
            " mul.lo.s32 x, x, x; st.param.b32 [o], x; ret; }")
probe("brx", "brx.idx (jump table)", "BRX",
      " and.b32 r5, r1, 3; ts: .branchtargets L0, L1, L2, L3; brx.idx r5, ts;\n"
      "L0: mov.u32 r4, 10; bra.uni E;\nL1: mov.u32 r4, 20; bra.uni E;\nL2: mov.u32 r4, 30; bra.uni E;\n"
      "L3: mov.u32 r4, 40;\nE:" + STI.format("r4"))
probe("uniform_loop", "loop with trip count from kernel param (uniform datapath; divergence: LDCU replaces ULDC, BRA.U on uniform predicates)",
      "LDCU UISETP UIADD3 PLOP3 BRA",
      " ld.param.u64 rd4, [t]; cvt.u32.u64 r5, rd4; mov.u32 r4, 0; mov.u32 r6, 0;\n"
      "UL: setp.ge.s32 q1, r6, r5; @q1 bra UD; add.s32 r4, r4, r1; add.s32 r6, r6, 1; bra UL;\nUD:"
      + STI.format("r4"))
probe("prologue", "empty kernel body (divergence: params load via LDC/LDCU directly -- sm_89's MOV+ULDC prologue is gone)",
      "LDC LDCU IMAD LDG STG EXIT S2R",
      STI.format("r1"))
probe("bssy_bsync", "divergent loop exit followed by a warp-synchronous op", "BSSY BSYNC",
      " mov.u32 r4, 0; mov.u32 r5, 0;\nBL: ld.global.u32 r6, [rd3]; setp.eq.s32 q1, r6, r5; @q1 bra BD;"
      " add.s32 r4, r4, r6; add.s32 r5, r5, 1; setp.lt.s32 q2, r5, r1; @q2 bra BL;\n"
      "BD: shfl.sync.bfly.b32 r7, r4, 1, 0x1f, -1;" + STI.format("r7"))
probe("agg_atomic", "atom.global.add.u32 to a warp-uniform address (hyp: warp-aggregated)",
      "VOTEU FLO POPC ATOMG SHFL",
      " ld.param.u64 rd4, [p]; cvta.to.global.u64 rd5, rd4; atom.global.add.u32 r4, [rd5], 1;" + STI.format("r4"))
probe("agg_red", "red.global.add.u32 to a warp-uniform address (warp-aggregated; VOTEU/POPC/UFLO + REDG)", "VOTEU POPC UFLO REDG",
      " ld.param.u64 rd4, [p]; cvta.to.global.u64 rd5, rd4; red.global.add.u32 [rd5], 1;")
probe("activemask", "activemask.b32", "VOTEU", " activemask.b32 r4; popc.b32 r5, r4;" + STI.format("r5"))
probe("s2ur_loop", "%ctaid.x as a loop bound (warp-uniform)", "S2UR UIADD3 PLOP3",
      " mov.u32 r5, %ctaid.x; mov.u32 r4, 0; mov.u32 r6, 0;\nSL: setp.ge.u32 q1, r6, r5; @q1 bra SD;"
      " add.s32 r4, r4, r1; add.s32 r6, r6, 1; bra SL;\nSD:" + STI.format("r4"))
probe("uniform_alu", "integer ops on a kernel parameter (warp-uniform)", "USHF ULOP3 UBREV UPOPC UPRMT",
      " ld.param.u64 rd4, [t]; cvt.u32.u64 r5, rd4; shr.u32 r6, r5, 3; xor.b32 r7, r6, r5; brev.b32 r8, r7;"
      " popc.b32 r9, r8; bfind.u32 r10, r7; prmt.b32 r11, r7, r9, 0x3210; add.s32 r12, r10, r11;"
      " add.s32 r13, r12, r1;" + STI.format("r13"))
probe("uniform_txq", "txq.num_mipmap_levels (handle arithmetic on uniform datapath)", "UIMAD UMOV",
      " ld.param.u64 rd4, [t]; txq.num_mipmap_levels.b32 r4, [rd4];" + STI.format("r4"))
probe("cctll", "prefetch.local.L1", "CCTLL",
      " .local .align 4 .b8 la[64]; mov.u64 rd4, la; prefetch.local.L1 [rd4]; st.local.u32 [rd4], r1;"
      " and.b32 r5, r2, 15; mul.wide.u32 rd5, r5, 4; add.s64 rd6, rd4, rd5; ld.local.u32 r4, [rd6];" + STI.format("r4"))
probe("pmtrig", "pmevent", "PMTRIG", " pmevent 1;")
# ---- Texture / surface (unified texture mode: handle passed as .u64 param t)
probe("tex", "tex.2d.v4.f32.f32", "TEX",
      " ld.param.u64 rd4, [t]; tex.2d.v4.f32.f32 {f4,f5,f6,f7}, [rd4, {f1,f2}];" + ST.format("f4"))
probe("tld4", "tld4.r.2d.v4.f32.f32", "TLD4",
      " ld.param.u64 rd4, [t]; tld4.r.2d.v4.f32.f32 {f4,f5,f6,f7}, [rd4, {f1,f2}];" + ST.format("f4"))
probe("txq", "txq.width.b32", "TXQ", " ld.param.u64 rd4, [t]; txq.width.b32 r4, [rd4];" + STI.format("r4"))
probe("suld", "suld.b.2d.b32.trap", "SULD",
      " ld.param.u64 rd4, [t]; suld.b.2d.b32.trap {r4}, [rd4, {r1,r2}];" + STI.format("r4"))
probe("tld", "tex.1d.v4.s32.s32 (integer coords, tex1Dfetch)", "TLD",
      " ld.param.u64 rd4, [t]; tex.1d.v4.s32.s32 {r4,r5,r6,r7}, [rd4, {r1}];" + STI.format("r4"))
probe("txd", "tex.grad.2d.v4.f32.f32", "TXD",
      " ld.param.u64 rd4, [t]; tex.grad.2d.v4.f32.f32 {f4,f5,f6,f7}, [rd4, {f1,f2}], {f3,f1}, {f2,f3};" + ST.format("f4"))
probe("sured", "sured.b.add.2d.u32.trap", "SURED", " ld.param.u64 rd4, [t]; sured.b.add.2d.u32.trap [rd4, {r1,r2}], r3;")
probe("suq", "suq.width.b32 (hyp: lowers to TXQ, not SUQUERY)", "TXQ",
      " ld.param.u64 rd4, [t]; suq.width.b32 r4, [rd4];" + STI.format("r4"))
probe("sust", "sust.b.2d.b32.trap", "SUST", " ld.param.u64 rd4, [t]; sust.b.2d.b32.trap [rd4, {r1,r2}], {r3};")
probe("plop3_folded", "xor.pred of two compares (hyp: folded into compare's combine op)", "ISETP FSETP",
      " setp.lt.s32 q1, r1, r2; setp.gt.f32 q2, f1, f2; xor.pred q3, q1, q2; @q3 st.global.u32 [rd1], r3;")


# Curated sm_89 -> sm_120 divergence findings.  Each was a live hypothesis-vs-observation
# mismatch during development (the first probe run reported them as MISSING); expectations
# above are the corrected sm_120 truth, this table preserves the findings.
DIVERGENCES = [
    ("renamed", "IMNMX -> **VIMNMX** (integer min/max moved to the V-unit naming; SIMD forms take .U8x4 suffixes, e.g. `VIMNMX.U8x4`)"),
    ("renamed", "RED -> **REDG** (global reductions carry explicit memory-order + scope qualifiers: `REDG.E.ADD.STRONG.GPU`); STM -> **STSM.16** (stmatrix)"),
    ("removed", "**HADD2 / HMUL2 gone** as arithmetic ops: `add.f16x2`/`mul.f16x2` fold into `HFMA2` with constant multipliers (e.g. `HFMA2 R5, R0, 1, 1, R5`)"),
    ("removed", "**BMMA gone**: 1-bit `mma.sync` lowers to a CALL into an internal `__cuda_sm_10x_mma_bit_internal_*` routine built from `IMMA.16832.U8.U8` and the new `MOVM.U4TO8.M832`"),
    ("removed", "**VABSDIFF4 gone**: `vabsdiff4` emulated via `VIMNMX.U8x4` + `VIADD.U8x4` + `IDP.4A.U8.U8`"),
    ("removed", "**ULDC gone**: uniform constant/param loads are **LDCU** (`LDCU.64 UR4, c[0x0][0x358]`); the sm_89 MOV+ULDC kernel prologue is gone -- params load via LDC/LDCU directly"),
    ("new", "**IADD.64**: 64-bit integer add is a single instruction (sm_89 used an IADD3 carry pair)"),
    ("new", "**UMEMSETS.64** (from `st.bulk.shared::cta`), **BAR.SYNC.DEFER_BLOCKING** (bar.sync form), **MOVM.U4TO8.M832**, `BRA.U` (branch on uniform predicate), `VOTEU.ANY`, `ATOMS.ADD` with `[UR4]` shared addressing"),
    ("new", "Descriptor-based global addressing is now universal: `LDG.E/STG.E desc[UR4][R2.64]` with a global-memory descriptor loaded from constant bank 0 into a uniform register (sm_89 used plain register addresses on most code)"),
    ("accepted", "sm_90+ instructions **accepted** on sm_120 that sm_89 rejected: `stmatrix` (STSM.16), `elect.sync`, `mapa` (but trivial mapa folds to S2UR/PRMT -- no MAPA opcode observed), `cp.async.bulk`/mbarrier, `griddepcontrol`"),
    ("rejected", "sm_100a-family features **still rejected** on sm_120: `redux.sync.*.f32`, FP4 `cvt.rn.satfinite.e2m1x2`, `tcgen05.*` (`.cta_group` not supported), plus the ever-`sm_90a`-only `wgmma`/`setmaxnreg`"),
    ("layout", "Control-code scoreboard layout unchanged vs sm_89 (hypothesis held): variable-latency producers set bits 110-112, late-source consumers bits 113-115, wait mask bits 116-121"),
]


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def bits(lo, hi):
    v = lo | hi << 64
    return "".join(str((v >> i) & 1) for i in range(128))


def disasm(cubin):
    """Yield (opcode, full text, 128-bit LSB-first bitstring) for each instruction."""
    out = run([NVDISASM, "-hex", "-c", str(cubin)]).stdout.splitlines()
    i = 0
    while i < len(out):
        m = re.match(r"\s*/\*[0-9a-f]{4}\*/\s+(.*?)\s*;?\s*/\* (0x[0-9a-f]{16}) \*/", out[i])
        if m and i + 1 < len(out):
            m2 = re.search(r"/\* (0x[0-9a-f]{16}) \*/", out[i + 1])
            text = m.group(1).rstrip(" ;")
            op = re.sub(r"^@!?U?P[T0-9]+\s+", "", text).split()[0].split(".")[0]
            yield op, text, bits(int(m.group(2), 16), int(m2.group(1), 16))
            i += 2
        else:
            i += 1


def main():
    ver = run([PTXAS, "--version"]).stdout.strip().splitlines()[-1]
    dver = run([NVDISASM, "--version"]).stdout.strip().splitlines()[-1]
    results, seen, ctrl = [], {}, {}
    with tempfile.TemporaryDirectory(dir="/home/dawn/.hermes/profiles/ops_emmy/cache/scratch") as td:
        for p in P:
            src = pathlib.Path(td, p["name"] + ".ptx")
            src.write_text(HEADER.format(decls=p["decls"], body=p["body"], funcs=p["funcs"]))
            cub = src.with_suffix(".cubin")
            c = run([PTXAS, f"-arch={ARCH}", "-O3", str(src), "-o", str(cub)])
            if p["reject"]:
                err = (c.stderr.strip().splitlines() or [""])[0]
                err = re.sub(r"^ptxas \S+, ", "", err)
                results.append(dict(p, status=("rejected (ok)" if re.search(r"sm_|\.target|feature|support|tcgen05", err, re.I)
                                              else "REJECTED FOR ANOTHER REASON")
                                    if c.returncode else "ACCEPTED (hypothesis wrong: divergence finding)",
                                    error=err, sass=[]))
                continue
            if c.returncode:
                results.append(dict(p, status="ptxas error", error=c.stderr.strip()[:400], sass=[]))
                continue
            sass = [(op, t, b) for op, t, b in disasm(cub) if op != "NOP"]
            ops = {op for op, _, _ in sass}
            missing = [e for e in p["expect"] if e not in ops]
            for op, t, b in sass:
                seen.setdefault(op, set()).add(p["name"])
                cc = ctrl.setdefault(op, [0, 0, 0, None, None])
                cc[0] += 1
                if int(b[110:113][::-1], 2) != 7:
                    cc[1] += 1
                    cc[3] = cc[3] or t
                if int(b[113:116][::-1], 2) != 7:
                    cc[2] += 1
                    cc[4] = cc[4] or t
            results.append(dict(p, status="ok" if not missing else "MISSING " + " ".join(missing),
                                sass=[t for _, t, _ in sass]))

    lines = ["# sm_120 PTX -> SASS verification results", "",
             f"Generated by `verify/probes.py` with real NVIDIA tools: ptxas `{ver}`, nvdisasm `{dver}`, "
             f"`-arch=sm_120 -O3`.",
             "Expectations are **hypotheses from the sm_89 KB**, tested here: `MISSING` = the sm_89 claim did not "
             "carry over (a divergence finding, listed in the divergence summary). Acceptance probes run PTX that "
             "sm_89 rejected for arch reasons.", ""]
    n_ok = sum(r["status"] in ("ok", "rejected (ok)") for r in results)
    lines += [f"**Expectation check:** {n_ok}/{len(results)} probes matched their hypothesis.", ""]
    divergences = [r for r in results if r["status"] not in ("ok", "rejected (ok)") and r["status"] != "ptxas error"]
    lines += ["## sm_89 -> sm_120 divergences", "",
              "Curated findings, each established by a hypothesis-vs-observation mismatch while the probe set was "
              "being tuned (see the per-probe SASS listings below for the evidence):", ""]
    for kind, text in DIVERGENCES:
        lines.append(f"- **{kind}:** {text}")
    lines.append("")
    if divergences:
        lines += ["### Live expectation mismatches in this run", "",
                  "| probe | PTX feature | finding |", "|---|---|---|"]
        for r in divergences:
            lines.append(f"| [{r['name']}](#{r['name']}) | `{r['ptx']}` | {r['status']} |")
        lines.append("")
    lines += ["### Control-code scoreboard fields (sm_89 layout hypothesis)",
              "",
              "Hypothesis carried from sm_89: bits 110-112 = write/result scoreboard, 113-115 = read scoreboard, "
              "116-121 = wait mask (LSB-first over the two 64-bit words). The counts below show how often each "
              "field holds an index on real sm_120 code; if the layout changed on Blackwell, the correlation "
              "pattern (producers setting 110-112, consumers 113-115/116-121) will look wrong here.",
              "",
              "| opcode | count | sets 110-112 | sets 113-115 | example (110-112) | example (113-115) |",
              "|---|---|---|---|---|---|"]
    for op, (n, w, r, tw, tr) in sorted(ctrl.items()):
        if w or r:
            lines.append(f"| {op} | {n} | {w} | {r} | {f'`{tw}`' if tw else ''} | {f'`{tr}`' if tr else ''} |")
    lines += ["", "## Probes", "", "| probe | PTX | expected (hyp from sm_89 unless noted) | status |",
              "|---|---|---|---|"]
    lines += [f"| [{r['name']}](#{r['name']}) | `{r['ptx']}` | {' '.join(r['expect']) or '(observe)'} | {r['status']} |"
              for r in results]
    for r in results:
        lines += ["", f'<a id="{r["name"]}"></a>', f"### {r['name']}", "", f"PTX: `{r['ptx']}` — {r['status']}", "",
                  "```", r["body"].strip(), "```", "", "SASS:", "```"]
        lines += r["sass"] or ["ptxas: " + r.get("error", "")]
        lines.append("```")
    (ROOT / "verify").mkdir(exist_ok=True)
    (ROOT / "verify" / "RESULTS.md").write_text("\n".join(lines) + "\n")
    (ROOT / "verify" / "results.json").write_text(json.dumps({
        "tools": {"ptxas": ver, "nvdisasm": dver, "arch": ARCH},
        "observed": {op: sorted(v) for op, v in sorted(seen.items())},
        "probes": [{k: r[k] for k in ("name", "ptx", "expect", "status", "reject")} for r in results],
    }, indent=1))
    print(f"{n_ok}/{len(results)} probes ok; {len(divergences)} divergences from sm_89 hypotheses")
    for r in results:
        if r["status"] not in ("ok", "rejected (ok)"):
            print(" ", r["name"], "|", r["status"], "|", r.get("error", "")[:160])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Ground-truth PTX -> SASS probes for sm_120 (Blackwell consumer), NVIDIA CUDA 12.9 tools.

Each probe is a small PTX kernel (.version 8.8, .target sm_120).  The runner compiles it
with real `ptxas -arch=sm_120`, disassembles with `nvdisasm -hex -c`, and records every
emitted instruction together with its raw 128-bit encoding (two 64-bit words straight
from nvdisasm's hex output).  Everything is observational: no sm_89 claims are copied.

Writes sm120/.cache/sass/results.json (gitignored raw artifact), one record per probe:
  {name, ptx, body, decls, funcs, arch, status, error, instrs: [{addr, text, op, w0, w1}]}

Resumable: probes already present with a terminal status are skipped; --force redoes all.
Batched: ptxas/nvdisasm run as sequential subprocesses in groups of --batch (default 20)
and results are checkpointed to disk after every batch.

Extra mode: --sched compiles a few identical bodies at -O0/-O2/-O3 into
sm120/.cache/sass/sched.json so build_sass.py can compare control-code bits across
schedules (same instructions, different stall/wait fields).
"""
import argparse
import json
import os
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "sass"
RESULTS = CACHE / "results.json"
PTXAS = os.environ.get("PTXAS", "/mnt/d/ops/emmy/toolchain/cuda12.9/bin/ptxas")
NVDISASM = os.environ.get("NVDISASM", "/mnt/d/ops/emmy/toolchain/cuda12.9/bin/nvdisasm")

HEADER = """.version 8.8
.target {arch}
.address_size 64
{decls}
{funcs}
.visible .entry k(.param .u64 p, .param .u64 t)
{{
 .reg .b32 r<64>; .reg .b64 rd<16>; .reg .f32 f<64>; .reg .f64 d<16>; .reg .pred q<8>;
 .reg .b16 h<8>; .reg .b8 h8<4>; .reg .b128 o<4>;
 ld.param.u64 rd0, [p]; cvta.to.global.u64 rd1, rd0;
 ld.param.u64 rd15, [t];
 mov.u32 r63, %tid.x; mul.wide.u32 rd2, r63, 64; add.s64 rd1, rd1, rd2;
 ld.global.u32 r1, [rd1]; ld.global.u32 r2, [rd1+4]; ld.global.u32 r3, [rd1+8];
 ld.global.f32 f1, [rd1+12]; ld.global.f32 f2, [rd1+16]; ld.global.f32 f3, [rd1+20];
 ld.global.f64 d1, [rd1+24]; ld.global.f64 d2, [rd1+32]; ld.global.u64 rd3, [rd1+40];
{body}
 ret;
}}
"""

# (name, PTX feature probed, body, decls, funcs, arch-override, expect-reject)
P = []


def probe(name, ptx, body, decls="", funcs="", arch=None, reject=False):
    P.append(dict(name=name, ptx=ptx, body=body, decls=decls, funcs=funcs,
                  arch=arch or "sm_120", reject=reject))


ST = " st.global.f32 [rd1], {};"
STI = " st.global.u32 [rd1], {};"
STD = " st.global.f64 [rd1], {};"

# ==== FP32 (port of the arch-neutral sm89 corpus; all conclusions re-derived on sm_120)
probe("fadd", "add.f32", " add.f32 f4, f1, f2;" + ST.format("f4"))
probe("ffma", "fma.rn.f32", " fma.rn.f32 f4, f1, f2, f3;" + ST.format("f4"))
probe("fmul", "mul.f32", " mul.f32 f4, f1, f2;" + ST.format("f4"))
probe("fminmax", "min.f32 / max.f32", " min.f32 f4, f1, f2; max.f32 f5, f4, f3;" + ST.format("f5"))
probe("fminmax_nan", "min.NaN.f32 / max.NaN.f32 (sm_80+ NaN propagation)",
      " min.NaN.f32 f4, f1, f2; max.NaN.f32 f5, f4, f3;" + ST.format("f5"))
probe("fminmax_xorsign", "min.xorsign.abs.f32 (sm_80+ modifier combo)",
      " min.xorsign.abs.f32 f4, f1, f2;" + ST.format("f4"))
probe("fsetp_selp", "setp.lt.f32 + selp.f32 (both arms computed)",
      " add.f32 f4, f1, f2; mul.f32 f5, f1, f3; setp.lt.f32 q1, f4, f5; selp.f32 f6, f4, f5, q1;" + ST.format("f6"))
probe("selp_to_predicated_load", "selp.f32 between two loaded values",
      " setp.lt.f32 q1, f1, f2; selp.f32 f4, f1, f3, q1;" + ST.format("f4"))
probe("fset", "set.lt.u32.f32", " set.lt.u32.f32 r4, f1, f2;" + STI.format("r4"))
probe("fdiv_rn", "div.rn.f32 (IEEE division)", " div.rn.f32 f4, f1, f2;" + ST.format("f4"))
for op in ("rcp.approx.f32", "rsqrt.approx.f32", "sqrt.approx.f32", "lg2.approx.f32", "ex2.approx.f32",
           "sin.approx.f32", "cos.approx.f32", "tanh.approx.f32"):
    probe("mufu_" + op.split(".")[0], op, f" {op} f4, f1;" + ST.format("f4"))
probe("frnd", "cvt.rmi.f32.f32 (floor)", " cvt.rmi.f32.f32 f4, f1;" + ST.format("f4"))
# ==== FP64
probe("dadd", "add.f64", " add.f64 d3, d1, d2;" + STD.format("d3"))
probe("dfma", "fma.rn.f64", " fma.rn.f64 d3, d1, d2, d1;" + STD.format("d3"))
probe("dmul", "mul.f64", " mul.f64 d3, d1, d2;" + STD.format("d3"))
probe("dsetp", "setp.lt.f64", " setp.lt.f64 q1, d1, d2; selp.f64 d3, d1, d2, q1;" + STD.format("d3"))
# ==== FP16x2 / BF16x2
probe("hadd2", "add.f16x2", " add.f16x2 r4, r1, r2;" + STI.format("r4"))
probe("hfma2", "fma.rn.f16x2", " fma.rn.f16x2 r4, r1, r2, r3;" + STI.format("r4"))
probe("hfma2_bf16", "fma.rn.bf16x2", " fma.rn.bf16x2 r4, r1, r2, r3;" + STI.format("r4"))
probe("hmul2", "mul.f16x2", " mul.f16x2 r4, r1, r2;" + STI.format("r4"))
probe("hmnmx2", "min.f16x2", " min.f16x2 r4, r1, r2;" + STI.format("r4"))
probe("hsetp2", "setp.lt.f16x2",
      " setp.lt.f16x2 q1|q2, r1, r2; selp.b32 r4, r1, r2, q1; selp.b32 r5, r4, r3, q2;" + STI.format("r5"))
probe("hset2", "set.lt.f16x2.f16x2", " set.lt.f16x2.f16x2 r4, r1, r2;" + STI.format("r4"))
# ==== Integer
probe("iadd", "add.s32 / sub.s32", " add.s32 r4, r1, r2; sub.s32 r5, r4, r3;" + STI.format("r5"))
probe("iadd64", "add.s64", " add.s64 rd4, rd3, rd3; st.global.u64 [rd1], rd4;")
probe("imad", "mad.lo.s32", " mad.lo.s32 r4, r1, r2, r3;" + STI.format("r4"))
probe("imad_wide", "mul.wide.s32", " mul.wide.s32 rd4, r1, r2; st.global.u64 [rd1], rd4;")
probe("imad_hi", "mul.hi.u32", " mul.hi.u32 r4, r1, r2;" + STI.format("r4"))
probe("iabs", "abs.s32", " abs.s32 r4, r1;" + STI.format("r4"))
probe("imnmx", "min.s32", " min.s32 r4, r1, r2;" + STI.format("r4"))
probe("isetp_pred", "setp.lt.s32 + selp.b32",
      " add.s32 r4, r1, r2; xor.b32 r5, r1, r3; setp.lt.s32 q1, r1, r3; selp.b32 r6, r4, r5, q1;" + STI.format("r6"))
probe("imnmx_from_selp", "setp.lt.s32 + selp.b32 forming min()",
      " add.s32 r4, r1, r2; xor.b32 r5, r1, r3; setp.lt.s32 q1, r4, r5; selp.b32 r6, r4, r5, q1;" + STI.format("r6"))
probe("lea", "shl.b32 + add.s32", " shl.b32 r4, r1, 3; add.s32 r5, r4, r2;" + STI.format("r5"))
probe("lea64", "pointer + (sign-extended s32 index << 2)",
      " cvt.s64.s32 rd4, r1; shl.b64 rd4, rd4, 2; add.s64 rd5, rd3, rd4; st.global.u32 [rd5], r2;")
probe("lop3", "and/xor/or of 3 values",
      " and.b32 r4, r1, r2; xor.b32 r5, r4, r3; or.b32 r6, r5, r1;" + STI.format("r6"))
probe("shf", "shf.l.wrap.b32", " shf.l.wrap.b32 r4, r1, r2, r3;" + STI.format("r4"))
probe("shl64", "shl.b64 by register", " shl.b64 rd4, rd3, r1; st.global.u64 [rd1], rd4;")
probe("prmt", "prmt.b32", " prmt.b32 r4, r1, r2, 0x5140;" + STI.format("r4"))
probe("sgxt", "bfe.s32 (signed field extract)", " bfe.s32 r4, r1, r2, r3;" + STI.format("r4"))
probe("bmsk", "bmsk.clamp.b32", " bmsk.clamp.b32 r4, r1, r2;" + STI.format("r4"))
probe("flo", "bfind.u32 / clz.b32", " bfind.u32 r4, r1; clz.b32 r5, r2; add.s32 r6, r4, r5;" + STI.format("r6"))
probe("brev", "brev.b32", " brev.b32 r4, r1;" + STI.format("r4"))
probe("popc", "popc.b32", " popc.b32 r4, r1;" + STI.format("r4"))
probe("idp", "dp4a.s32.s32", " dp4a.s32.s32 r4, r1, r2, r3;" + STI.format("r4"))
probe("vabsdiff", "vabsdiff.u32.u32.u32 (observe)", " vabsdiff.u32.u32.u32 r4, r1, r2;" + STI.format("r4"))
probe("vabsdiff2", "vabsdiff2.u32.u32.u32 (observe)", " vabsdiff2.u32.u32.u32 r4, r1, r2, r3;" + STI.format("r4"))
probe("vabsdiff4", "vabsdiff4.u32.u32.u32.add", " vabsdiff4.u32.u32.u32.add r4, r1, r2, r3;" + STI.format("r4"))
# ==== Conversion
probe("f2f", "cvt.rn.f32.f64", " cvt.rn.f32.f64 f4, d1;" + ST.format("f4"))
probe("f2i", "cvt.rzi.s32.f32", " cvt.rzi.s32.f32 r4, f1;" + STI.format("r4"))
probe("i2fp", "cvt.rn.f32.s32", " cvt.rn.f32.s32 f4, r1;" + ST.format("f4"))
probe("i2f", "cvt.rn.f64.s32", " cvt.rn.f64.s32 d3, r1;" + STD.format("d3"))
probe("f2fp_f16", "cvt.rn.f16x2.f32", " cvt.rn.f16x2.f32 r4, f1, f2;" + STI.format("r4"))
probe("f2fp_bf16", "cvt.rn.bf16x2.f32", " cvt.rn.bf16x2.f32 r4, f1, f2;" + STI.format("r4"))
probe("f2fp_e4m3", "cvt.rn.satfinite.e4m3x2.f32 (FP8)",
      " cvt.rn.satfinite.e4m3x2.f32 h1, f1, f2; cvt.u32.u16 r4, h1;" + STI.format("r4"))
probe("cvt_e4m3_to_f16x2", "cvt.rn.f16x2.e4m3x2 (FP8 -> half2)",
      " cvt.rn.satfinite.e4m3x2.f32 h1, f1, f2; cvt.rn.f16x2.e4m3x2 r4, h1;" + STI.format("r4"))
probe("cvt_e2m1_fp4", "cvt.rn.satfinite.e2m1x2.f32 (FP4; sm_100a+ family)",
      " .reg .b8 b81; cvt.rn.satfinite.e2m1x2.f32 b81, f1, f2; cvt.u32.u8 r4, b81;" + STI.format("r4"))
probe("i2i", "cvt.sat.s8.s32", " cvt.sat.s8.s32 r4, r1;" + STI.format("r4"))
probe("i2ip", "cvt.pack.sat.s8.s32.b32", " cvt.pack.sat.s8.s32.b32 r4, r1, r2, r3;" + STI.format("r4"))
probe("f2ip", "cvt.rni.sat.s8.f32 (observe only)", " cvt.rni.sat.s8.f32 r4, f1;" + STI.format("r4"))
# ==== Movement / warp
probe("shfl", "shfl.sync.bfly.b32", " shfl.sync.bfly.b32 r4, r1, 1, 0x1f, -1;" + STI.format("r4"))
probe("vote", "vote.sync.ballot.b32", " setp.ne.s32 q1, r1, 0; vote.sync.ballot.b32 r4, q1, -1;" + STI.format("r4"))
probe("match", "match.any.sync.b32", " match.any.sync.b32 r4, r1, -1;" + STI.format("r4"))
probe("redux", "redux.sync.add.u32", " redux.sync.add.u32 r4, r1, -1;" + STI.format("r4"))
probe("redux_f32", "redux.sync.min.f32 (sm_100a family feature)",
      " redux.sync.min.f32 f4, f1, -1;" + ST.format("f4"))
probe("s2r", "mov.u32 %laneid", " mov.u32 r4, %laneid;" + STI.format("r4"))
probe("cs2r", "mov.u64 %clock64", " mov.u64 rd4, %clock64; st.global.u64 [rd1], rd4;")
probe("globaltimer", "mov.u64 %globaltimer", " mov.u64 rd4, %globaltimer; st.global.u64 [rd1], rd4;")
probe("s2r_ctaid", "mov.u32 %ctaid.x stored directly", " mov.u32 r4, %ctaid.x;" + STI.format("r4"))
probe("s2ur", "%ctaid.x used in uniform address math (observe)",
      " mov.u32 r4, %ctaid.x; mul.wide.u32 rd4, r4, 1024; add.s64 rd5, rd0, rd4; cvta.to.global.u64 rd6, rd5;"
      " ld.global.u32 r5, [rd6]; add.s32 r6, r5, r1;" + STI.format("r6"))
probe("movm", "movmatrix.sync.aligned.m8n8.trans.b16", " movmatrix.sync.aligned.m8n8.trans.b16 r4, r1;" + STI.format("r4"))
# ==== Memory
probe("lds_sts", "ld.shared / st.shared",
      " mov.u32 r5, sm; shl.b32 r6, r63, 2; add.s32 r5, r5, r6; st.shared.u32 [r5], r1; bar.sync 0;"
      " ld.shared.u32 r4, [r5+4];" + STI.format("r4"), decls=".shared .align 16 .b8 sm[4096];")
probe("ld_generic", "ld (generic pointer)", " ld.u32 r4, [rd3];" + STI.format("r4"))
probe("st_generic", "st (generic pointer)", " st.u32 [rd3], r1;")
probe("ldg_hints", "ld.global.L1::evict_last.u32 (cache eviction hint)",
      " ld.global.L1::evict_last.u32 r4, [rd1];" + STI.format("r4"))
probe("ldg_l2_128b", "ld.global.L2::128B.u32 (L2 fetch granularity hint)",
      " ld.global.L2::128B.u32 r4, [rd1];" + STI.format("r4"))
probe("ldg_v2", "ld.global.v2.f32", " ld.global.v2.f32 {f4,f5}, [rd1+48]; add.f32 f6, f4, f5;" + ST.format("f6"))
probe("ldg_nc", "ld.global.nc.v4.f32", " ld.global.nc.v4.f32 {f4,f5,f6,f7}, [rd1+48]; add.f32 f8, f4, f7;" + ST.format("f8"))
probe("stg_v4", "st.global.v4.f32", " add.f32 f4, f1, f2; st.global.v4.f32 [rd1+64], {f1,f2,f3,f4};")
probe("ldl_stl", "dynamically indexed .local array",
      " .local .align 4 .b8 la[256]; mov.u64 rd4, la; and.b32 r5, r1, 63; mul.wide.u32 rd5, r5, 4;"
      " add.s64 rd6, rd4, rd5; st.local.u32 [rd6], r2; and.b32 r6, r3, 63; mul.wide.u32 rd7, r6, 4;"
      " add.s64 rd8, rd4, rd7; ld.local.u32 r4, [rd8];" + STI.format("r4"))
probe("ldc", "ld.const with dynamic index",
      " mov.u64 rd4, cst; and.b32 r5, r1, 63; mul.wide.u32 rd5, r5, 4; add.s64 rd6, rd4, rd5;"
      " ld.const.u32 r4, [rd6];" + STI.format("r4"), decls=".const .align 4 .b32 cst[64];")
probe("cp_async", "cp.async.cg.shared.global + commit_group + wait_group",
      " mov.u32 r5, sm; shl.b32 r6, r63, 4; add.s32 r5, r5, r6; cp.async.cg.shared.global [r5], [rd1], 16;"
      " cp.async.commit_group; cp.async.wait_group 0; bar.sync 0; ld.shared.u32 r4, [r5];" + STI.format("r4"),
      decls=".shared .align 16 .b8 sm[4096];")
probe("ldsm", "ldmatrix.sync.aligned.m8n8.x4.shared.b16",
      " mov.u32 r5, sm; shl.b32 r6, r63, 4; add.s32 r5, r5, r6; st.shared.u32 [r5], r1; bar.sync 0;"
      " ldmatrix.sync.aligned.m8n8.x4.shared.b16 {r10,r11,r12,r13}, [r5]; add.s32 r4, r10, r13;" + STI.format("r4"),
      decls=".shared .align 16 .b8 sm[4096];")
probe("ldsm_trans", "ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16",
      " mov.u32 r5, sm; shl.b32 r6, r63, 4; add.s32 r5, r5, r6; st.shared.u32 [r5], r1; bar.sync 0;"
      " ldmatrix.sync.aligned.m8n8.x1.trans.shared.b16 {r10}, [r5];" + STI.format("r10"),
      decls=".shared .align 16 .b8 sm[4096];")
probe("atomg", "atom.global.add.u32 (result used)", " atom.global.add.u32 r4, [rd1], r1;" + STI.format("r4"))
probe("red", "red.global.add.u32 (no result)", " red.global.add.u32 [rd1], r1;")
probe("atoms", "atom.shared.add.u32",
      " mov.u32 r5, sm; atom.shared.add.u32 r4, [r5], r1;" + STI.format("r4"), decls=".shared .align 16 .b8 sm[64];")
probe("atom_generic", "atom.add.u32 (generic)", " atom.add.u32 r4, [rd3], r1;" + STI.format("r4"))
probe("atom_v2_f32", "atom.global.v2.add.f32 (vector atomic, sm_90+)",
      " atom.global.v2.add.f32 {f4,f5}, [rd1+80], {f1,f2}; add.f32 f6, f4, f5;" + ST.format("f6"))
probe("red_v2_f32", "red.global.v2.add.f32 (vector reduction, sm_90+)",
      " red.global.v2.add.f32 [rd1+80], {f1,f2};")
probe("atom_cas", "atom.global.cas.b32", " atom.global.cas.b32 r4, [rd1], r1, r2;" + STI.format("r4"))
probe("atom_add_f32", "atom.global.add.f32 (fast fp32 atomic)", " atom.global.add.f32 f4, [rd1], f1;" + ST.format("f4"))
probe("qspc", "isspacep.shared", " isspacep.shared q1, rd3; selp.u32 r4, 1, 0, q1;" + STI.format("r4"))
probe("cctl", "prefetch.global.L1", " prefetch.global.L1 [rd3];")
# ==== Blackwell-era memory (sm_90+ constructs, now legal on sm_120)
probe("elect_sync", "elect.sync (sm_90+)", " elect.sync r4|q1, -1;" + STI.format("r4"))
probe("stmatrix", "stmatrix.sync.aligned.m8n8.x1.shared.b16 (sm_90+)",
      " mov.u32 r5, sm; stmatrix.sync.aligned.m8n8.x1.shared.b16 [r5], {r1}; bar.sync 0;"
      " ld.shared.u32 r4, [r5];" + STI.format("r4"), decls=".shared .align 16 .b8 sm[64];")
probe("stmatrix_x4", "stmatrix.sync.aligned.m8n8.x4.shared.b16",
      " mov.u32 r5, sm; stmatrix.sync.aligned.m8n8.x4.shared.b16 [r5], {r1,r2,r3,r4}; bar.sync 0;"
      " ld.shared.u32 r6, [r5];" + STI.format("r6"), decls=".shared .align 16 .b8 sm[64];")
probe("mapa", "mapa.u64 (cluster address mapping, sm_90+)",
      " mapa.u64 rd4, rd3, 1; st.global.u64 [rd1], rd4;")
probe("cluster_ctarank", "%cluster_ctarank special register",
      " mov.u32 r4, %cluster_ctarank;" + STI.format("r4"))
probe("cluster_barrier", "barrier.cluster.arrive/wait.aligned",
      " barrier.cluster.arrive.aligned; barrier.cluster.wait.aligned;" + STI.format("r1"))
probe("fence_cluster", "fence.acq_rel.cluster",
      " st.global.u32 [rd1], r1; fence.acq_rel.cluster; st.global.u32 [rd1+4], r2;")
MBAR = ".shared .align 16 .b8 sm[4096]; .shared .align 8 .b64 mb[1];"
probe("cp_async_bulk_tma", "cp.async.bulk (TMA) shared::cluster.global + mbarrier (sm_90+)",
      " mov.u32 r5, sm; mov.u32 r6, mb;"
      " mbarrier.init.shared.b64 [r6], 1;"
      " cp.async.bulk.shared::cluster.global.mbarrier::complete_tx::bytes [r5], [rd1], 16, [r6];"
      " mbarrier.arrive.expect_tx.shared::cta.b64 _, [r6], 16;"
      " mbarrier.try_wait.parity.shared.b64 q1, [r6], 0;"
      " @q1 mov.u32 r4, 1; selp.u32 r4, 1, 0, q1;" + STI.format("r4"), decls=MBAR)
probe("mbarrier_red", "mbarrier.arrive.release.cluster.shared::cta.b64 (sm_90+)",
      " mov.u32 r6, mb; mbarrier.init.shared.b64 [r6], 1;"
      " mbarrier.arrive.shared::cta.b64 rd4, [r6];" + STI.format("r4"), decls=MBAR)
probe("st_bulk", "st.bulk (shared-memory init, sm_90+)",
      " mov.u32 r5, sm; st.bulk [r5], 64, 0; bar.sync 0; ld.shared.u32 r4, [r5];" + STI.format("r4"),
      decls=".shared .align 16 .b8 sm[4096];")
probe("cp_async_bulk_prefetch", "cp.async.bulk.prefetch.L2.global (sm_90+)",
      " cp.async.bulk.prefetch.L2.global [rd1], 64;")
probe("griddepcontrol", "griddepcontrol.wait / launch_dependents (sm_90+)",
      " griddepcontrol.wait; griddepcontrol.launch_dependents;" + STI.format("r1"))
probe("tensormap_replace", "tensormap.replace.tile.global_address (sm_90+)",
      " tensormap.replace.tile.global_address.global.b1024.b64 [rd1], rd3;")
probe("setmaxnreg", "setmaxnreg.inc.sync.aligned.u32 (sm_90a family only)",
      " setmaxnreg.inc.sync.aligned.u32 64;", reject=True)
probe("wgmma_fence", "wgmma.fence.sync.aligned (sm_90a family only)",
      " wgmma.fence.sync.aligned;", reject=True)
probe("tcgen05_fence", "tcgen05.relinquish_alloc_permit (sm_100a family only)",
      " tcgen05.relinquish_alloc_permit.cta_group::1.sync.aligned;", reject=True)
probe("st_async", "st.async.shared::cta.mbarrier::complete_tx::bytes (sm_90+)",
      " mov.u32 r5, sm; mov.u32 r6, mb; mbarrier.init.shared.b64 [r6], 1;"
      " st.async.shared::cluster.mbarrier::complete_tx::bytes.b32 [r5], r1, [r6];"
      " mbarrier.try_wait.parity.shared.b64 q1, [r6], 0; ld.shared.u32 r4, [r5];" + STI.format("r4"), decls=MBAR)
# ==== Tensor core (mma.sync forms; sm_120 has its own 5th-gen consumer path)
probe("hmma_f16", "mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32",
      " mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
probe("hmma_bf16", "mma.sync.aligned.m16n8k16.row.col.f32.bf16.bf16.f32",
      " mma.sync.aligned.m16n8k16.row.col.f32.bf16.bf16.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
probe("hmma_tf32", "mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32",
      " mma.sync.aligned.m16n8k8.row.col.f32.tf32.tf32.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
probe("imma", "mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32",
      " mma.sync.aligned.m16n8k32.row.col.s32.s8.s8.s32 {r10,r11,r12,r13}, {r1,r2,r3,r1}, {r2,r3}, {r1,r2,r3,r1};"
      " add.s32 r4, r10, r13;" + STI.format("r4"))
probe("dmma", "mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64 (FP64 MMA)",
      " mma.sync.aligned.m8n8k4.row.col.f64.f64.f64.f64 {d3,d4}, {d1}, {d2}, {d1,d2}; add.f64 d5, d3, d4;" + STD.format("d5"))
probe("bmma", "mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc",
      " mma.sync.aligned.m16n8k256.row.col.s32.b1.b1.s32.and.popc {r10,r11,r12,r13}, {r1,r2,r3,r1}, {r2,r3}, {r1,r2,r3,r1};"
      " add.s32 r4, r10, r13;" + STI.format("r4"))
probe("qmma_e4m3", "mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 (FP8)",
      " mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
probe("qmma_e5m2", "mma.sync.aligned.m16n8k32.row.col.f32.e5m2.e5m2.f32 (FP8)",
      " mma.sync.aligned.m16n8k32.row.col.f32.e5m2.e5m2.f32 {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1};"
      " add.f32 f4, f10, f13;" + ST.format("f4"))
probe("mma_mxf8f6f4", "mma.sync kind::mxf8f6f4 block-scaled (sm_100a/120a family)",
      " mma.sync.aligned.m16n8k32.row.col.kind::mxf8f6f4.block_scale.scale_vec::1X.f32.e4m3.e4m3.f32.ue8m0"
      " {f10,f11,f12,f13}, {r1,r2,r3,r1}, {r2,r3}, {f1,f2,f3,f1}, r1, {0, r1}, r2, {0, r2};")
probe("tcgen05_mma_120a", "tcgen05.mma (sm_100a/sm_103a; rejected on sm_120 even as sm_120a?)",
      " tcgen05.fence::after_thread_sync;", reject=True, arch="sm_120a")
probe("setmaxnreg_120a", "setmaxnreg under -arch=sm_120a (family-arch check)",
      " setmaxnreg.inc.sync.aligned.u32 64;", reject=True, arch="sm_120a")
# ==== Sync / control
probe("bar", "bar.sync 0", " st.global.u32 [rd1], r1; bar.sync 0; ld.global.u32 r4, [rd1+4];" + STI.format("r4"))
probe("bar_red", "bar.red.popc.u32", " setp.ne.s32 q1, r1, 0; bar.red.popc.u32 r4, 0, q1;" + STI.format("r4"))
probe("membar", "membar.gl", " st.global.u32 [rd1], r1; membar.gl; st.global.u32 [rd1+4], r2;")
probe("fence_sys", "fence.sc.sys", " st.global.u32 [rd1], r1; fence.sc.sys; st.global.u32 [rd1+4], r2;")
probe("nanosleep", "nanosleep.u32", " nanosleep.u32 r1;")
probe("warpsync", "bar.warp.sync with partial mask", " bar.warp.sync r1;")
probe("diverge", "data-dependent loop",
      " mov.u32 r4, 0; mov.u32 r5, 0;\nLOOP: setp.ge.s32 q1, r5, r1; @q1 bra DONE; add.s32 r4, r4, r5; add.s32 r5, r5, 1; bra LOOP;\nDONE:"
      + STI.format("r4"))
probe("call", ".func .noinline call",
      " { .param .b32 a; .param .b32 rv; st.param.b32 [a], r1; call.uni (rv), fn, (a); ld.param.b32 r4, [rv]; }"
      + STI.format("r4"),
      funcs=".func (.param .b32 o) fn(.param .b32 i) { .reg .b32 x; ld.param.b32 x, [i];"
            " mul.lo.s32 x, x, x; st.param.b32 [o], x; ret; }")
probe("brx", "brx.idx (jump table)",
      " and.b32 r5, r1, 3; ts: .branchtargets L0, L1, L2, L3; brx.idx r5, ts;\n"
      "L0: mov.u32 r4, 10; bra.uni E;\nL1: mov.u32 r4, 20; bra.uni E;\nL2: mov.u32 r4, 30; bra.uni E;\n"
      "L3: mov.u32 r4, 40;\nE:" + STI.format("r4"))
probe("uniform_loop", "loop with trip count from kernel param (uniform datapath)",
      " ld.param.u64 rd4, [t]; cvt.u32.u64 r5, rd4; mov.u32 r4, 0; mov.u32 r6, 0;\n"
      "UL: setp.ge.s32 q1, r6, r5; @q1 bra UD; add.s32 r4, r4, r1; add.s32 r6, r6, 1; bra UL;\nUD:"
      + STI.format("r4"))
probe("prologue", "empty kernel body: param pointer + %tid.x load/store", STI.format("r1"))
probe("bssy_bsync", "divergent loop exit followed by a warp-synchronous op",
      " mov.u32 r4, 0; mov.u32 r5, 0;\nBL: ld.global.u32 r6, [rd3]; setp.eq.s32 q1, r6, r5; @q1 bra BD;"
      " add.s32 r4, r4, r6; add.s32 r5, r5, 1; setp.lt.s32 q2, r5, r1; @q2 bra BL;\n"
      "BD: shfl.sync.bfly.b32 r7, r4, 1, 0x1f, -1;" + STI.format("r7"))
probe("agg_atomic", "atom.global.add.u32 to a warp-uniform address (warp-aggregation)",
      " ld.param.u64 rd4, [p]; cvta.to.global.u64 rd5, rd4; atom.global.add.u32 r4, [rd5], 1;" + STI.format("r4"))
probe("agg_red", "red.global.add.u32 to a warp-uniform address (warp-aggregated)",
      " ld.param.u64 rd4, [p]; cvta.to.global.u64 rd5, rd4; red.global.add.u32 [rd5], 1;")
probe("activemask", "activemask.b32", " activemask.b32 r4; popc.b32 r5, r4;" + STI.format("r5"))
probe("s2ur_loop", "%ctaid.x as a loop bound (warp-uniform)",
      " mov.u32 r5, %ctaid.x; mov.u32 r4, 0; mov.u32 r6, 0;\nSL: setp.ge.u32 q1, r6, r5; @q1 bra SD;"
      " add.s32 r4, r4, r1; add.s32 r6, r6, 1; bra SL;\nSD:" + STI.format("r4"))
probe("uniform_alu", "integer ops on a kernel parameter (warp-uniform)",
      " ld.param.u64 rd4, [t]; cvt.u32.u64 r5, rd4; shr.u32 r6, r5, 3; xor.b32 r7, r6, r5; brev.b32 r8, r7;"
      " popc.b32 r9, r8; bfind.u32 r10, r7; prmt.b32 r11, r7, r9, 0x3210; add.s32 r12, r10, r11;"
      " add.s32 r13, r12, r1;" + STI.format("r13"))
probe("uniform_txq", "txq.num_mipmap_levels (handle arithmetic on uniform datapath)",
      " ld.param.u64 rd4, [t]; txq.num_mipmap_levels.b32 r4, [rd4];" + STI.format("r4"))
probe("cctll", "prefetch.local.L1",
      " .local .align 4 .b8 la[64]; mov.u64 rd4, la; prefetch.local.L1 [rd4]; st.local.u32 [rd4], r1;"
      " and.b32 r5, r2, 15; mul.wide.u32 rd5, r5, 4; add.s64 rd6, rd4, rd5; ld.local.u32 r4, [rd6];" + STI.format("r4"))
probe("pmtrig", "pmevent", " pmevent 1;")
probe("plop3_folded", "xor.pred of two compares (folded into ISETP/FSETP combine op)",
      " setp.lt.s32 q1, r1, r2; setp.gt.f32 q2, f1, f2; xor.pred q3, q1, q2; @q3 st.global.u32 [rd1], r3;")
# ==== Texture / surface (unified texture mode: handle passed as .u64 param t)
probe("tex", "tex.2d.v4.f32.f32",
      " tex.2d.v4.f32.f32 {f4,f5,f6,f7}, [rd15, {f1,f2}];" + ST.format("f4"))
probe("tld4", "tld4.r.2d.v4.f32.f32",
      " tld4.r.2d.v4.f32.f32 {f4,f5,f6,f7}, [rd15, {f1,f2}];" + ST.format("f4"))
probe("txq", "txq.width.b32", " txq.width.b32 r4, [rd15];" + STI.format("r4"))
probe("suld", "suld.b.2d.b32.trap", " suld.b.2d.b32.trap {r4}, [rd15, {r1,r2}];" + STI.format("r4"))
probe("tld", "tex.1d.v4.s32.s32 (integer coords)", " tex.1d.v4.s32.s32 {r4,r5,r6,r7}, [rd15, {r1}];" + STI.format("r4"))
probe("txd", "tex.grad.2d.v4.f32.f32",
      " tex.grad.2d.v4.f32.f32 {f4,f5,f6,f7}, [rd15, {f1,f2}], {f3,f1}, {f2,f3};" + ST.format("f4"))
probe("sured", "sured.b.add.2d.u32.trap", " sured.b.add.2d.u32.trap [rd15, {r1,r2}], r3;")
probe("suq", "suq.width.b32", " suq.width.b32 r4, [rd15];" + STI.format("r4"))
probe("sust", "sust.b.2d.b32.trap", " sust.b.2d.b32.trap [rd15, {r1,r2}], {r3};")

# identical bodies re-compiled at several optimisation levels for the control-code study
SCHED_PROBES = {
    "dep_chain": (" ld.global.f32 f4, [rd1+44]; add.f32 f5, f4, f1; mul.f32 f6, f5, f2;"
                  " fma.rn.f32 f7, f6, f5, f3; st.global.f32 [rd1+48], f7;"),
    "fadd": " add.f32 f4, f1, f2;" + ST.format("f4"),
    "cp_async": (" mov.u32 r5, sm; shl.b32 r6, r63, 4; add.s32 r5, r5, r6; cp.async.cg.shared.global [r5], [rd1], 16;"
                 " cp.async.commit_group; cp.async.wait_group 0; bar.sync 0; ld.shared.u32 r4, [r5];" + STI.format("r4")),
    "diverge": (" mov.u32 r4, 0; mov.u32 r5, 0;\nLOOP: setp.ge.s32 q1, r5, r1; @q1 bra DONE;"
                " add.s32 r4, r4, r5; add.s32 r5, r5, 1; bra LOOP;\nDONE:" + STI.format("r4")),
}
SCHED_DECLS = {"cp_async": ".shared .align 16 .b8 sm[4096];"}

INSTR_RE = re.compile(r"\s*/\*([0-9a-f]{4})\*/\s+(.*?)\s*;\s*/\* (0x[0-9a-f]{16}) \*/")
PRED_RE = re.compile(r"^@!?U?P[T0-9]+\s+")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def disasm(cubin):
    """[(addr, text, w0hex, w1hex)] from `nvdisasm -hex -c`; the two hex comments are the
    64-bit halves of the 128-bit encoding (bit 0 = LSB of w0, LSB-first)."""
    out = run([NVDISASM, "-hex", "-c", str(cubin)]).stdout.splitlines()
    res, i = [], 0
    while i < len(out):
        m = INSTR_RE.match(out[i])
        if m and i + 1 < len(out):
            m2 = re.search(r"/\* (0x[0-9a-f]{16}) \*/", out[i + 1])
            if m2:
                text = m.group(2).strip().rstrip(";").strip()
                text = re.sub(r"\s+`?\(", " (", text)  # normalise BRA target spacing
                res.append((int(m.group(1), 16), text, m.group(3)[2:], m2.group(1)[2:]))
                i += 2
                continue
        i += 1
    return res


def opcode_of(text):
    t = PRED_RE.sub("", text)
    return t.split()[0].split(".")[0] if t.split() else ""


def compile_probe(p, workdir):
    src = workdir / f"{p['name']}.ptx"
    src.write_text(HEADER.format(arch=p["arch"], decls=p["decls"], body=p["body"], funcs=p["funcs"]))
    cub = src.with_suffix(".cubin")
    c = run([PTXAS, f"-arch={p['arch']}", "-O3", str(src), "-o", str(cub)])
    return src, cub, c


def classify(p, cub, c):
    """Record for one probe: status + per-instruction encodings."""
    rec = {k: p[k] for k in ("name", "ptx", "body", "decls", "funcs", "arch", "reject")}
    if c.returncode:
        err = (c.stderr.strip().splitlines() or [""])[0]
        err = re.sub(r"^ptxas \S+, ", "", err)
        if p["reject"]:
            ok = bool(re.search(r"sm_|family|feature|\\.target|supported", err, re.I))
            rec["status"] = "rejected (ok)" if ok else "REJECTED FOR ANOTHER REASON"
        else:
            rec["status"] = "ptxas error"
        rec["error"] = err[:400]
        rec["instrs"] = []
        return rec
    if p["reject"]:
        rec["status"] = "ACCEPTED (expected reject)"
        rec["instrs"] = []
        return rec
    rec["status"] = "ok"
    rec["instrs"] = [dict(addr=a, text=t, op=opcode_of(t), w0=w0, w1=w1)
                     for a, t, w0, w1 in disasm(cub)]
    return rec


def load_results():
    if RESULTS.exists():
        return json.loads(RESULTS.read_text())
    return {"tools": {}, "probes": []}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true", help="re-run even already-recorded probes")
    ap.add_argument("--only", help="regex: run only matching probe names")
    ap.add_argument("--batch", type=int, default=20, help="checkpoint every N probes")
    ap.add_argument("--sched", action="store_true", help="(re)build sched.json only")
    args = ap.parse_args()

    CACHE.mkdir(parents=True, exist_ok=True)
    ver = run([PTXAS, "--version"]).stdout.strip().splitlines()[-1]
    dver = run([NVDISASM, "--version"]).stdout.strip().splitlines()[-1]

    if args.sched:
        sched = {}
        td = tempfile_dir()
        for opt in ("O0", "O2", "O3"):
                for name, body in SCHED_PROBES.items():
                    src = pathlib.Path(td, f"{name}_{opt}.ptx")
                    src.write_text(HEADER.format(arch="sm_120", decls=SCHED_DECLS.get(name, ""),
                                                 body=body, funcs=""))
                    cub = src.with_suffix(".cubin")
                    c = run([PTXAS, "-arch=sm_120", f"-{opt}", str(src), "-o", str(cub)])
                    if c.returncode:
                        sched.setdefault(opt, {})[name] = {"error": c.stderr.strip()[:200]}
                        continue
                    sched.setdefault(opt, {})[name] = [
                        dict(addr=a, text=t, op=opcode_of(t), w0=w0, w1=w1) for a, t, w0, w1 in disasm(cub)]
        (CACHE / "sched.json").write_text(json.dumps(
            {"tools": {"ptxas": ver, "nvdisasm": dver}, "sched": sched}, indent=1))
        n = sum(len(v) for o in sched.values() for v in o.values() if isinstance(v, list))
        print(f"sched.json: {n} instructions across O0/O2/O3")
        return

    res = load_results()
    res["tools"] = {"ptxas": ver, "nvdisasm": dver}
    by_name = {r["name"]: r for r in res["probes"]}
    done = set() if args.force else set(by_name)
    todo = [p for p in P if p["name"] not in done and (not args.only or re.search(args.only, p["name"]))]
    print(f"{len(done)} already recorded, {len(todo)} to run")

    import tempfile
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        for i in range(0, len(todo), args.batch):
            batch = todo[i:i + args.batch]
            for p in batch:
                src, cub, c = compile_probe(p, td)
                by_name[p["name"]] = classify(p, cub, c)
            res["probes"] = list(by_name.values())
            RESULTS.write_text(json.dumps(res, indent=1))
            print(f"  batch {i // args.batch + 1}/{(len(todo) + args.batch - 1) // args.batch} done "
                  f"({len(res['probes'])} probes recorded)")

    n_ok = sum(r["status"] in ("ok", "rejected (ok)") for r in res["probes"])
    print(f"{n_ok}/{len(res['probes'])} probes ok; results in {RESULTS}")
    for r in res["probes"]:
        if r["status"] not in ("ok", "rejected (ok)"):
            print("  ", r["name"], r["status"], r.get("error", "")[:160])


def tempfile_dir():
    import tempfile
    return pathlib.Path(tempfile.mkdtemp())


if __name__ == "__main__":
    main()

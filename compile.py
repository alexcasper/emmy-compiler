#!/usr/bin/env python3
"""Emmy Kernel IR -> PTX compiler (Emmy hackathon 2026).

Usage (the submission contract):

    python compile.py path/to/kernel.ir.json > out.ptx

Design overview (see DESIGN.md for the full story):

  1. Load the IR with emmy's own `Graph.from_dict` (the IR only deserializes
     through emmy's classes) and find the `KernelOp` node.
  2. Emit a prologue: `.version/.target`, one `.u64` param per kernel argument
     (the node's inputs followed by its outputs, which is what meta.json's
     `arg_order` holds), `cvta.to.global` for each buffer, and the thread id.
  3. Walk the statement tree, keeping a map from IR value names to virtual
     registers. One translation per statement kind; expressions (index math)
     are compiled recursively.
  4. Registers are handed out fresh for every SSA value; no liveness analysis.
     `ptxas` does the real register allocation downstream.

Supported statement kinds cover the five open categories: Tile, Load, Assign,
Let, Init, Accum, Write, StridedLoop, Loop, Cond, Sync, WarpShuffle, TreeHalve,
Smem, CpAsyncCopy/Commit/Wait.
"""

from __future__ import annotations

import json
import math
import os
import dataclasses
import re
import struct
import sys

from emmy.compiler.graph import Graph

TARGET = "sm_89"
PTX_VERSION = "8.0"
# Static .shared is capped at 48 KiB per block; above this we switch to an
# `extern .shared` pool that the launch config sizes (meta.json's smem_bytes).
STATIC_SMEM_LIMIT = 48 * 1024

# ---------------------------------------------------------------------------
# tuning (GEPA search space; see gen/gepa_optimize.py on branch `gepa`)
#
# Defaults reproduce the hand-tuned behavior exactly. `EMMY_TUNING` holds JSON
# (inline or "@path/to/file"). The correctness gate (rtol/atol via the runner)
# is the only judge of whether an approximation knob is acceptable.
# ---------------------------------------------------------------------------

DEFAULT_TUNING = {
    "nc_loads": False,   # ld.global.nc on buffers the kernel never writes
    "div": "rn",         # "rn" | "approx" | "approx.ftz"
    "sqrt": "rn",        # "rn" | "approx"
    "rcp": "rn",         # "rn" | "approx"
    "pow2_shift": True,  # div/mod by power-of-2 constant -> shr/and instead of
                         # div.s32/rem.s32 (ptxas expands those to MUFU
                         # float-reciprocal sequences; indices are non-negative)
    "hoist_invariants": "auto",  # True | False | "auto": hoist loop-invariant
                         # address subexpressions to loop preheaders. Measured
                         # (L4 sm_89, open set + tracer variations): a big win
                         # where the IR stages tiles via cp.async (m01 3.2x on
                         # the judge runner), a consistent ~8-9% regression in
                         # cp.async-free kernels (attention) where the long-
                         # lived hoisted bases cost ptxas load scheduling.
                         # "auto" = hoist iff the kernel body has cp.async.
    "fuse_loops": False,  # merge consecutive sibling loops with identical trip
                         # counts and no cross-references into one loop.
                         # FALSIFIED on hardware: a01 fused = 3x smaller SASS
                         # (1696->560 instrs, LDG 322->22) but 68% SLOWER on
                         # L4 (246->413us) — the removed "redundant" kt loads
                         # were free L1 hits that provided memory-level
                         # parallelism. Kept searchable, default off.
    "load_cse": False,   # reuse one LDG register for identical read-only
                         # global loads within a straight-line body (see
                         # fuse_loops — same falsification)
    "unroll_inner": "auto",  # 0/1 = off; 2/4/... = replicate straight-line inner
                         # loop bodies U times per iteration (extent must
                         # divide evenly). "auto" = unroll iff the kernel body
                         # has cp.async — judge-runner measured: m01 37.7->
                         # 29.5us, but cp.async-free attention kernels are
                         # latency-bound and collapse (a01 100->191us).
}


def load_tuning() -> dict:
    raw = os.environ.get("EMMY_TUNING")
    t = dict(DEFAULT_TUNING)
    if raw:
        if raw.startswith("@"):
            raw = open(raw[1:]).read()
        try:
            t.update(json.loads(raw))
        except ValueError:
            pass  # malformed tuning: fall back to defaults rather than crash
    return clamp_tuning(t)


def clamp_tuning(t: dict) -> dict:
    """Clamp to legal values so a bad config can't emit bad PTX."""
    out = dict(t)
    out["nc_loads"] = bool(out.get("nc_loads", False))
    out["div"] = out.get("div") if out.get("div") in ("rn", "approx", "approx.ftz") else "rn"
    out["sqrt"] = out.get("sqrt") if out.get("sqrt") in ("rn", "approx") else "rn"
    out["rcp"] = out.get("rcp") if out.get("rcp") in ("rn", "approx") else "rn"
    out["pow2_shift"] = bool(out.get("pow2_shift", True))
    h = out.get("hoist_invariants", "auto")
    out["hoist_invariants"] = h if h in (True, False, "auto") else "auto"
    out["fuse_loops"] = bool(out.get("fuse_loops", False))
    out["load_cse"] = bool(out.get("load_cse", False))
    u = out.get("unroll_inner", "auto")
    if u == "auto":
        out["unroll_inner"] = "auto"
    else:
        try:
            out["unroll_inner"] = max(0, int(u))
        except (TypeError, ValueError):
            out["unroll_inner"] = 0
    return out

# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------


def f32_hex(value: float) -> str:
    """PTX hex literal for an f32 constant, e.g. 0f3F800000 (1.0).

    PTX float bit patterns are most-significant byte first, hence '>f'.
    A little-endian pack here silently turns 1.0 into a 1e-41 denormal —
    the constant assembles fine and the kernel just computes nonsense.
    """
    return "0f" + struct.pack(">f", float(value)).hex().upper()


def dim_int(dim) -> int:
    """A Dim holds a (constant) expression; unwrap the integer."""
    return int(getattr(getattr(dim, "expr", None), "value", dim))


def op_name(op) -> str:
    return getattr(op, "name", str(op))


def sanitize(name: str) -> str:
    return re.sub(r"\W", "_", name)


# Float op tables are built per-Compiler instance from the tuning dict (approx
# vs correctly-rounded variants); `exp` always lowers through ex2.approx
# (x * log2 e) — every problem that uses exp has rtol >= 1e-3, far above the
# approx instruction's ~1 ulp error.
ACCUM_IDENTITY = {"add": 0.0, "maximum": -1e30, "minimum": 1e30}
CMP_OPS = {"==": "eq", "!=": "ne", "<": "lt", "<=": "le", ">": "gt", ">=": "ge"}
INT_OPS = {"+": "add.s32", "-": "sub.s32", "*": "mul.lo.s32", "/": "div.s32", "%": "rem.s32"}


class CompileError(Exception):
    pass


# ---------------------------------------------------------------------------
# emitter
# ---------------------------------------------------------------------------


class Emitter:
    """Collects PTX body lines and hands out fresh virtual registers.

    Virtual registers are never reused: every SSA value gets its own. The
    per-class `.reg` declaration counts are computed from the final text.
    """

    def __init__(self):
        self.lines: list[str] = []
        self.counts = {"f": 0, "r": 0, "rd": 0, "p": 0}

    def reg(self, cls: str) -> str:
        self.counts[cls] += 1
        return {"f": "%f", "r": "%r", "rd": "%rd", "p": "%p"}[cls] + str(self.counts[cls])

    def emit(self, line: str):
        self.lines.append("        " + line)

    def raw(self, line: str):
        self.lines.append(line)

    def label(self, name: str):
        self.lines.append(f"{name}:")


# ---------------------------------------------------------------------------
# compiler
# ---------------------------------------------------------------------------


class Compiler:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.e = Emitter()
        self.env: dict[str, tuple[str, str]] = {}   # SSA value -> (reg, 'f'|'r')
        self.buffers: dict[str, dict] = {}          # buffer name -> descriptor
        self.smem_base: dict[str, str] = {}         # smem name -> u32 base reg
        self.smem_stride: dict[str, tuple[int, ...]] = {}
        self.smem_decls: list[str] = []
        self.extern_pool = False
        self.labels = 0
        self.accum_defs: dict[str, object] = {}
        self.init_names: set[str] = set()
        # tuning: per-instance op tables so the search can flip approximations
        self.tuning = load_tuning()
        self.float_ops = {
            "add": "add.f32", "subtract": "sub.f32", "multiply": "mul.f32",
            "divide": f"div.{self.tuning['div']}.f32",
            "maximum": "max.f32", "minimum": "min.f32",
        }
        self.unary_ops = {
            "reciprocal": f"rcp.{self.tuning['rcp']}.f32",
            "sqrt": f"sqrt.{self.tuning['sqrt']}.f32",
            "copy": "mov.f32",
        }
        # buffers read but never written by this kernel (eligible for ld.global.nc)
        self.readonly_buffers: set[str] = set()
        # hoist policy: "auto" enables hoisting only for cp.async-staged kernels,
        # where per-iteration address recompute is the measured bottleneck
        mode = self.tuning["hoist_invariants"]
        if mode == "auto":
            op = self.kernel_node().op
            self._hoist_enabled = any(type(s).__name__ == "CpAsyncCopy"
                                      for s in op.body[0].body.iter())
        else:
            self._hoist_enabled = bool(mode)
        # unroll policy: "auto" = U=4; Loop-kind bodies (dot products) unroll
        # only in cp.async kernels — judge-runner measured a01 100->191us
        # otherwise. StridedLoop bodies (reductions) unroll always: r02
        # 41->30us (-27%), 3/3 interleaved rounds on the judge runner.
        umode = self.tuning["unroll_inner"]
        if umode == "auto":
            self._unroll_u, self._unroll_auto = 4, True
        else:
            self._unroll_u, self._unroll_auto = int(umode), False
        # per-body emission cache for read-only load CSE (see visit_load)
        self._load_cse: dict = {}

    # -- setup ---------------------------------------------------------------

    def fresh_label(self, hint: str) -> str:
        self.labels += 1
        return f"{hint}_{self.labels}"

    def kernel_node(self):
        for node in self.graph.nodes.values():
            if type(node.op).__name__ == "KernelOp":
                return node
        raise CompileError("no KernelOp node in graph")

    def collect_buffers(self, node):
        for n in self.graph.nodes.values():
            for tensor in n.outputs:
                self.buffers[tensor.name] = {
                    "cls": "g",
                    "shape": tuple(dim_int(d) for d in tensor.shape),
                    "elem": tensor.dtype.nbytes,
                }

    def plan_smem(self, tile):
        """Declare shared arrays, or carve them out of an extern pool when the
        total exceeds the static limit."""
        total = 0
        smems = []
        for st in tile.body.iter():
            if type(st).__name__ == "Smem":
                extents = tuple(dim_int(x) for x in st.extents)
                nbytes = math.prod(extents) * 4  # all problem smem is f32
                smems.append((st.name, extents, nbytes, max(st.align or 4, 4)))
                total += nbytes
        self.extern_pool = total > STATIC_SMEM_LIMIT
        offset = 0
        for name, extents, nbytes, align in smems:
            if self.extern_pool:
                offset = (offset + align - 1) // align * align
                self.smem_stride[name] = strides_of(extents)
                self.smem_base[name] = ("pool", offset)
                offset += nbytes
            else:
                self.smem_decls.append(f".shared .align {align} .b8 {name}[{nbytes}];")
                self.smem_stride[name] = strides_of(extents)
                self.smem_base[name] = ("static", 0)

    def scan_accums(self, body):
        for st in body.iter():
            if type(st).__name__ == "Accum":
                self.accum_defs[st.name] = st
            elif type(st).__name__ == "Init":
                self.init_names.add(st.name)

    # -- entry point ----------------------------------------------------------

    def compile(self) -> str:
        node = self.kernel_node()
        op = node.op
        self.kernel_name = op.name
        self.collect_buffers(node)
        self.params = list(node.inputs) + [t.name for t in node.outputs]
        tile = op.body[0]
        self.scan_accums(op.body)
        self.plan_smem(tile)
        self.collect_readonly(tile)

        self.emit_header()
        self.emit_prologue(params=self.params, tile=tile)
        self.visit_tile(tile)
        self.e.emit("ret;")
        self.e.raw("}")
        return self.assemble()

    def collect_readonly(self, tile):
        """Buffers only ever read (Load / CpAsyncCopy src, never a Write target)
        — these may take the ld.global.nc path when tuning asks for it."""
        reads, writes = set(), set()
        for st in tile.body.iter():
            kind = type(st).__name__
            if kind == "Load":
                reads.add(st.input)
            elif kind == "CpAsyncCopy":
                reads.add(st.src)
            elif kind == "Write":
                writes.add(st.output)
        self.readonly_buffers = reads - writes

    def emit_header(self):
        e = self.e
        e.raw(f".version {PTX_VERSION}")
        e.raw(f".target {TARGET}")
        e.raw(".address_size 64")
        for decl in self.smem_decls:
            e.raw(decl)
        if self.extern_pool:
            e.raw(".extern .shared .align 16 .b8 __emmy_smem_pool[];")

    def assemble(self) -> str:
        # fix the .reg declaration counts from what the body actually used,
        # splicing the declarations in right after the opening brace
        text = "\n".join(self.e.lines)
        for cls, pat in (("p", r"%p(\d+)"), ("f", r"%f(\d+)"),
                         ("r", r"%r(\d+)"), ("rd", r"%rd(\d+)")):
            used = [int(m) for m in re.findall(pat, text)]
            self.e.counts[cls] = max(used + [0])
        # PTX register vectors are 0-indexed: `%rd<16>` covers %rd0..%rd15, so
        # declare one more than the highest index we hand out.
        header = [
            f"        .reg .pred      %p<{self.e.counts['p'] + 1}>;",
            f"        .reg .f32       %f<{self.e.counts['f'] + 1}>;",
            f"        .reg .b32       %r<{self.e.counts['r'] + 1}>;",
            f"        .reg .b64       %rd<{self.e.counts['rd'] + 1}>;",
        ]
        # splice the declarations in after the .entry opening brace
        out = []
        for line in self.e.lines:
            out.append(line)
            if line == "{":
                out.extend(header)
        return "\n".join(out) + "\n"

    # -- prologue --------------------------------------------------------------

    def emit_prologue(self, params, tile):
        e = self.e
        sig = ",\n".join(f"        .param .u64 param_{sanitize(p)}" for p in params)
        e.raw(f".visible .entry {self.kernel_name}(")
        e.raw(sig)
        e.raw(")")
        e.raw("{")

        for p in params:
            rd = self.e.reg("rd")
            e.emit(f"ld.param.u64 {rd}, [param_{sanitize(p)}];")
            g = self.e.reg("rd")
            e.emit(f"cvta.to.global.u64 {g}, {rd};")
            self.buffers[p]["reg"] = g
        tid = self.e.reg("r")
        e.emit(f"mov.u32 {tid}, %tid.x;")
        self.tid = tid
        # lane/warp are read across statement kinds (Cond guards, TreeHalve),
        # so define them once, before any divergent branch
        lane = self.e.reg("r")
        e.emit(f"and.b32 {lane}, {tid}, 31;")
        self.env["lane"] = (lane, "r")
        warp = self.e.reg("r")
        e.emit(f"shr.u32 {warp}, {tid}, 5;")
        self.env["warp"] = (warp, "r")
        # shared-memory base addresses
        for name, (kind, off) in self.smem_base.items():
            r = self.e.reg("r")
            if kind == "pool":
                e.emit(f"mov.u32 {r}, __emmy_smem_pool;")
                if off:
                    e.emit(f"add.u32 {r}, {r}, {off};")
            else:
                e.emit(f"mov.u32 {r}, {name};")
            self.smem_base[name] = r

    # -- Tile: guard + axis decode ----------------------------------------------

    def visit_tile(self, tile):
        e = self.e
        extents = [dim_int(a.extent) for a in tile.axes]
        n = math.prod(extents)
        block_threads = tile.block_threads or 256
        if tile.aux_threads:
            # warp-specialized producer band appended past the cooperative
            # cells: compute threads decode their cell from the wrapped id.
            gid = self.e.reg("r")
            bid = self.e.reg("r")
            e.emit(f"mov.u32 {bid}, %ctaid.x;")
            e.emit(f"mul.lo.s32 {bid}, {bid}, {block_threads};")
            wrap = self.e.reg("r")
            e.emit(f"rem.u32 {wrap}, {self.tid}, {block_threads};")
            e.emit(f"add.u32 {gid}, {bid}, {wrap};")
        else:
            bid = self.e.reg("r")
            e.emit(f"mov.u32 {bid}, %ctaid.x;")
            gid = self.e.reg("r")
            e.emit(f"mul.lo.u32 {gid}, {bid}, {block_threads};")
            e.emit(f"add.u32 {gid}, {gid}, {self.tid};")
        self.gid = gid

        # guard: extra threads may exist when the launch overprovisions
        skip = self.fresh_label("GUARD_END")
        pred = self.e.reg("p")
        e.emit(f"setp.ge.u32 {pred}, {gid}, {n};")
        e.emit(f"@{pred} bra {skip};")

        # per-axis decode: a_i = gid / s_i % e_i (s_i = product of inner extents).
        # Only the outermost axis may skip the modulo — the guard already bounds
        # it. Every inner axis needs it, including extent-1 axes, or the value
        # leaks the raw quotient (which corrupts every index it feeds).
        for i, (axis, extent) in enumerate(zip(tile.axes, extents)):
            inner = math.prod(extents[i + 1:])
            r = self.e.reg("r")
            outermost = i == 0
            if inner == 1 and outermost:
                e.emit(f"mov.u32 {r}, {gid};")
            elif self.tuning["pow2_shift"] and inner > 1 and inner & (inner - 1) == 0 \
                    and extent & (extent - 1) == 0:
                # same MUFU-avoidance as binary_expr, for the axis decode
                e.emit(f"shr.u32 {r}, {gid}, {inner.bit_length() - 1};")
                e.emit(f"and.b32 {r}, {r}, {extent - 1};")
            else:
                e.emit(f"div.u32 {r}, {gid}, {inner};")
                e.emit(f"rem.u32 {r}, {r}, {extent};")
            self.env[axis.name] = (r, "r")

        # cooperative axes conventionally end in _co; both spellings decode the same
        self.stmts(tile.body)

        if tile.aux_threads:
            pass  # producer band handled by guards inside the body
        e.label(skip)

    # -- statements ---------------------------------------------------------------

    def stmts(self, body):
        if self.tuning.get("fuse_loops", True) and len(body) >= 2:
            self._stmts_fused(body)
            return
        for st in body:
            self.stmt(st)

    def stmt(self, st):
        kind = type(st).__name__
        method = getattr(self, f"visit_{kind.lower()}", None)
        if method is None:
            raise CompileError(f"unsupported statement kind: {kind}")
        method(st)

    def visit_load(self, st):
        buf = st.input
        # read-only global loads: identical address -> one LDG serves all names
        # (attention IR re-loads the same kt element across fused siblings).
        # Valid only within one straight-line body emission: the map is cleared
        # at every control-flow boundary (loops, branches, sync).
        cse = self.tuning.get("load_cse", True) and buf in self.readonly_buffers
        key = None
        if cse:
            key = (buf, tuple(self._ex_key(ix) for ix in st.index), len(st.names))
            hit = self._load_cse.get(key)
            if hit is not None:
                for name, reg in zip(st.names, hit):
                    self.env[name] = (reg, "f")
                return
        desc = self.buffer_desc(buf)
        addr = self.flat_addr(buf, st.index)
        dtype = getattr(st.dtype, "name", None) or "f32"
        ptx_t = "f32" if dtype == "f32" else dtype
        prefix = "ld.shared" if desc["cls"] == "s" else "ld.global"
        if prefix == "ld.global" and self.tuning["nc_loads"] and buf in self.readonly_buffers:
            prefix = "ld.global.nc"
        if len(st.names) == 1:
            d = self.e.reg("f")
            self.e.emit(f"{prefix}.{ptx_t} {d}, [{addr}];")
            self.env[st.names[0]] = (d, "f")
        elif len(st.names) in (2, 4):
            regs = [self.e.reg("f") for _ in st.names]
            op = f"{prefix}.v{len(st.names)}.{ptx_t}"
            self.e.emit(f"{op} {{{', '.join(regs)}}}, [{addr}];")
            for name, reg in zip(st.names, regs):
                self.env[name] = (reg, "f")
        else:
            raise CompileError(f"unsupported load width: {len(st.names)} names")
        if key is not None:
            self._load_cse[key] = [self.env[n][0] for n in st.names]

    def visit_let(self, st):
        v = st.value
        if type(v).__name__ == "Literal":
            if v.dtype == "float":
                d = self.e.reg("f")
                self.e.emit(f"mov.f32 {d}, {f32_hex(v.value)};")
                self.env[st.name] = (d, "f")
            else:
                d = self.e.reg("r")
                self.e.emit(f"mov.u32 {d}, {int(v.value)};")
                self.env[st.name] = (d, "r")
        else:
            raise CompileError(f"unsupported Let value: {type(v).__name__}")

    def visit_init(self, st):
        d = self.e.reg("f")
        self.e.emit(f"mov.f32 {d}, {f32_hex(st.identity)};")
        self.env[st.name] = (d, "f")

    def visit_assign(self, st):
        args = [self.env[a] for a in st.args]
        op = op_name(st.op)
        d = self.e.reg("f")
        if op in self.unary_ops:
            self.e.emit(f"{self.unary_ops[op]} {d}, {args[0][0]};")
        elif op == "relu":
            self.e.emit(f"max.f32 {d}, {args[0][0]}, {f32_hex(0.0)};")
        elif op == "exp":
            log2e = self.e.reg("f")
            self.e.emit(f"mul.f32 {log2e}, {args[0][0]}, {f32_hex(math.log2(math.e))};")
            self.e.emit(f"ex2.approx.f32 {d}, {log2e};")
        elif op in self.float_ops:
            self.e.emit(f"{self.float_ops[op]} {d}, {args[0][0]}, {args[1][0]};")
        else:
            raise CompileError(f"unsupported elementwise op: {op}")
        self.env[st.name] = (d, "f")

    def visit_accum(self, st):
        # Accumulators are loop-carried state: unlike plain SSA values they
        # update their register in place across iterations. The register was
        # created by the identity seed (enter_loop) or an Init statement.
        op = op_name(st.op)
        if st.name not in self.env:
            raise CompileError(f"accumulator {st.name} used before seeded")
        value = self.env[st.value]
        lhs = self.env[st.base] if st.base is not None else self.env[st.name]
        d = self.env[st.name][0]
        if op in self.float_ops:
            self.e.emit(f"{self.float_ops[op]} {d}, {lhs[0]}, {value[0]};")
        else:
            raise CompileError(f"unsupported accumulator op: {op}")
        self.env[st.name] = (d, "f")

    def visit_write(self, st):
        buf = st.output
        desc = self.buffer_desc(buf)
        addr = self.flat_addr(buf, st.index)
        if st.atomic:
            for v in st.values:
                reg = self.env[v][0]
                self.e.emit(f"red.global.add.f32 [{addr}], {reg};")
            return
        ptx_t = "f32"
        if len(st.values) == 1:
            reg = self.env[st.values[0]][0]
            self.e.emit(f"{'st.global' if desc['cls'] == 'g' else 'st.shared'}.{ptx_t} [{addr}], {reg};")
        elif len(st.values) in (2, 4):
            regs = [self.env[v][0] for v in st.values]
            op = ("st.global" if desc["cls"] == "g" else "st.shared") + f".v{len(st.values)}.{ptx_t}"
            self.e.emit(f"{op} [{addr}], {{{', '.join(regs)}}};")
        else:
            for i, v in enumerate(st.values):
                # element i sits one element size past the base address
                off = self.e.reg("rd")
                self.e.emit(f"add.s64 {off}, {addr}, {4 * i};")
                reg = self.env[v][0]
                self.e.emit(f"{'st.global' if desc['cls'] == 'g' else 'st.shared'}.{ptx_t} [{off}], {reg};")

    def visit_sync(self, st):
        if st.warp:
            self.e.emit("bar.warp.sync 0;")
        else:
            self.e.emit(f"bar.sync {st.barrier_id};")

    def visit_stridedloop(self, st):
        step = dim_int_or_const(st.step)
        start = self.expr(st.start)[0]
        u = self._unroll_factor(st, step)
        if u >= 2:
            return self._visit_stridedloop_unrolled(st, start, step, u)
        self.enter_loop(st)
        ivar = self.e.reg("r")
        self.e.emit(f"mov.u32 {ivar}, {start};")
        end = dim_int(st.axis.extent)
        top = self.fresh_label("LOOP")
        bottom = self.fresh_label("LOOP_END")
        self.e.label(top)
        pred = self.e.reg("p")
        self.e.emit(f"setp.ge.u32 {pred}, {ivar}, {end};")
        self.e.emit(f"@{pred} bra {bottom};")
        self.env[st.axis.name] = (ivar, "r")
        self.stmts(st.body)
        self.e.emit(f"add.u32 {ivar}, {ivar}, {step};")
        self.e.emit(f"bra {top};")
        self.e.label(bottom)
        self.exit_loop()

    def _visit_stridedloop_unrolled(self, st, start, step, u):
        """Strided version: copies take ivar + k*step; trip count must divide."""
        self.enter_loop(st)
        end = dim_int(st.axis.extent)
        axis = st.axis.name

        def body_fn(ivar):
            for k in range(u):
                if k == 0:
                    self.env[axis] = (ivar, "r")
                else:
                    r = self.e.reg("r")
                    self.e.emit(f"add.u32 {r}, {ivar}, {k * step};")
                    self.env[axis] = (r, "r")
                self.stmts(st.body)

        self._emit_loop(st, start, step * u, end, body_fn)
        self.exit_loop()

    def _unroll_factor(self, st, step):
        """U>=2 if unrolling is enabled for this loop kind, the body is
        straight-line, and the trip count divides evenly by U; else 0."""
        u = self._unroll_u
        if u < 2:
            return 0
        if self._unroll_auto and type(st).__name__ != "StridedLoop" \
                and not self._hoist_enabled:
            return 0
        for sub in st.body.iter():
            if type(sub).__name__ not in self._FUSE_BODY_KINDS:
                return 0
        extent = dim_int(st.axis.extent)
        iters = extent // step
        return u if iters >= u and iters % u == 0 else 0

    def _emit_loop(self, st, ivar_init, step, end, body_fn):
        """Shared loop skeleton: init ivar, while ivar < end: body_fn(ivar_reg)."""
        ivar = self.e.reg("r")
        self.e.emit(f"mov.u32 {ivar}, {ivar_init};")
        top = self.fresh_label("LOOP")
        bottom = self.fresh_label("LOOP_END")
        self.e.label(top)
        pred = self.e.reg("p")
        self.e.emit(f"setp.ge.u32 {pred}, {ivar}, {end};")
        self.e.emit(f"@{pred} bra {bottom};")
        body_fn(ivar)
        if step == 1:
            self.e.emit(f"add.u32 {ivar}, {ivar}, 1;")
        else:
            self.e.emit(f"add.u32 {ivar}, {ivar}, {step};")
        self.e.emit(f"bra {top};")
        self.e.label(bottom)
        return ivar

    def visit_loop(self, st):
        u = self._unroll_factor(st, 1)
        if u >= 2:
            return self._visit_loop_unrolled(st, u)

        self.enter_loop(st)
        ivar = self._emit_loop(
            st, 0, 1, dim_int(st.axis.extent),
            lambda ivar: (self.env.__setitem__(st.axis.name, (ivar, "r")),
                          self.stmts(st.body)))
        self.exit_loop()

    def _visit_loop_unrolled(self, st, u):
        """Replicate a straight-line body U times per iteration; the axis takes
        ivar..ivar+U-1. Extent divides by U (checked), so no tail guard."""
        self.enter_loop(st)
        end = dim_int(st.axis.extent)
        axis = st.axis.name

        def body_fn(ivar):
            for k in range(u):
                if k == 0:
                    self.env[axis] = (ivar, "r")
                else:
                    r = self.e.reg("r")
                    self.e.emit(f"add.u32 {r}, {ivar}, {k};")
                    self.env[axis] = (r, "r")
                self.stmts(st.body)

        self._emit_loop(st, 0, u, end, body_fn)
        self.exit_loop()

    def enter_loop(self, st):
        """Seed the accumulators this loop owns. A seed=True loop owns the
        accumulators that (a) are defined inside its own body subtree — so
        sibling loops over the same axis don't clobber each other's state —
        and (b) fold over this loop's axis. The identity is written just
        before iterating, so re-entry (outer-loop iterations) re-seeds."""
        axis_name = st.axis.name
        self.loop_axis_stack = getattr(self, "loop_axis_stack", [])
        self.loop_axis_stack.append(axis_name)
        self._load_cse.clear()
        self._hoist_for_loop(st)
        if not getattr(st, "seed", True):
            return
        # Seed in body-walk order (NOT set order): set iteration varies with the
        # interpreter's hash seed, which made the PTX text nondeterministic run
        # to run — same semantics, different register numbering, impossible diffs.
        seen = set()
        owned = []
        for a in self.iter_accums(st.body):
            if axis_name in a.axes and a.name not in self.init_names and a.name not in seen:
                seen.add(a.name)
                owned.append(a.name)
        for name in owned:
            acc = self.accum_defs[name]
            identity = ACCUM_IDENTITY.get(op_name(acc.op))
            if identity is None:
                raise CompileError(f"no identity for accumulator op {op_name(acc.op)}")
            d = self.e.reg("f")
            self.e.emit(f"mov.f32 {d}, {f32_hex(identity)};")
            self.env[name] = (d, "f")

    def iter_accums(self, body):
        for st in body.iter():
            if type(st).__name__ == "Accum":
                yield st

    def exit_loop(self):
        self.loop_axis_stack.pop()
        if getattr(self, "hoist_stack", None):
            self.hoist_stack.pop()
        self._load_cse.clear()

    def visit_cond(self, st):
        self._load_cse.clear()
        pred = self.compile_pred(st.cond)
        if st.else_body:
            else_label = self.fresh_label("ELSE")
            end = self.fresh_label("ENDIF")
            self.e.emit(f"@!{pred} bra {else_label};")
            self.stmts(st.body)
            self.e.emit(f"bra {end};")
            self.e.label(else_label)
            self.stmts(st.else_body)
            self.e.label(end)
        else:
            end = self.fresh_label("ENDIF")
            self.e.emit(f"@!{pred} bra {end};")
            self.stmts(st.body)
            self.e.label(end)

    def visit_warpshuffle(self, st):
        states = list(st.state)
        shuffled = list(st.state_b)
        for offset in [st.length // 2 >> i for i in range(int(math.log2(st.length)))]:
            for name, target in zip(states, shuffled):
                src = self.env[name][0]
                tmp_b = self.e.reg("r")
                out = self.e.reg("r")
                self.e.emit(f"mov.b32 {tmp_b}, {src};")
                self.e.emit(
                    f"shfl.sync.bfly.b32 {out}, {tmp_b}, {offset}, 0x1f, 0xffffffff;"
                )
                dst = self.e.reg("f")
                self.e.emit(f"mov.b32 {dst}, {out};")
                self.env[target] = (dst, "f")
            self.combine(st)

    def visit_treehalve(self, st):
        tid_reg = self.env[st.tid_var][0]
        for s in [st.length // 2 >> i for i in range(int(math.log2(st.length)))]:
            pred = self.e.reg("p")
            self.e.emit(f"setp.ge.s32 {pred}, {tid_reg}, {s};")
            skip = self.fresh_label("TREE_SKIP")
            self.e.emit(f"@{pred} bra {skip};")
            for name, buf in zip(st.state, st.bufs):
                a = self.load_smem_elem(buf, st.tid_var)
                self.env[name] = (a, "f")
                b = self.load_smem_elem(buf, f"({st.tid_var}+{s})")
                self.env[st.state_b[st.state.index(name)]] = (b, "f")
            self.combine(st)
            for name, buf in zip(st.state, st.bufs):
                self.store_smem_elem(buf, st.tid_var, self.env[name][0])
            self.e.label(skip)
            self.e.emit(f"bar.sync {st.barrier_id};")
        # broadcast: every thread reads the root
        for name, buf in zip(st.state, st.bufs):
            d = self.e.reg("f")
            self.e.emit(f"ld.shared.f32 {d}, [{self.smem_base[buf]}];")
            self.env[name] = (d, "f")

    def combine(self, st):
        for assign in st.combine_states:
            self.visit_assign(assign)

    def load_smem_elem(self, buf, idx_var_name):
        if idx_var_name.startswith("("):
            # tid + s: compute the offset register directly
            s = int(idx_var_name[idx_var_name.index("+") + 1: -1])
            tid = self.env["warp"][0]
            off = self.e.reg("r")
            self.e.emit(f"add.u32 {off}, {tid}, {s};")
            addr = self.e.reg("r")
            self.e.emit(f"mul.lo.u32 {addr}, {off}, 4;")
            self.e.emit(f"add.u32 {addr}, {addr}, {self.smem_base[buf]};")
        else:
            tid = self.env[idx_var_name][0]
            addr = self.e.reg("r")
            self.e.emit(f"mul.lo.u32 {addr}, {tid}, 4;")
            self.e.emit(f"add.u32 {addr}, {addr}, {self.smem_base[buf]};")
        d = self.e.reg("f")
        self.e.emit(f"ld.shared.f32 {d}, [{addr}];")
        return d

    def store_smem_elem(self, buf, idx_var_name, reg):
        tid = self.env[idx_var_name][0]
        addr = self.e.reg("r")
        self.e.emit(f"mul.lo.u32 {addr}, {tid}, 4;")
        self.e.emit(f"add.u32 {addr}, {addr}, {self.smem_base[buf]};")
        self.e.emit(f"st.shared.f32 [{addr}], {reg};")

    def visit_smem(self, st):
        pass  # declared in the prologue

    def visit_cpasynccopy(self, st):
        gaddr = self.flat_addr(st.src, st.src_index)
        desc = self.buffer_desc(st.smem)
        row, col = st.smem_index
        row_r = self.expr(row)[0]
        col_r = self.expr(col)[0]
        stride = self.smem_stride[st.smem][0] if self.smem_stride[st.smem] else 1
        off = self.e.reg("r")
        self.e.emit(f"mul.lo.u32 {off}, {row_r}, {stride};")
        self.e.emit(f"add.u32 {off}, {off}, {col_r};")
        if st.lane_index is not None:
            lr, lc = st.lane_index
            lr_r = self.expr(lr)[0]
            lc_r = self.expr(lc)[0]
            t1 = self.e.reg("r")
            self.e.emit(f"mul.lo.u32 {t1}, {lr_r}, {stride};")
            self.e.emit(f"add.u32 {off}, {off}, {t1};")
            self.e.emit(f"add.u32 {off}, {off}, {lc_r};")
        saddr = self.e.reg("r")
        self.e.emit(f"mul.lo.u32 {saddr}, {off}, 4;")
        self.e.emit(f"add.u32 {saddr}, {saddr}, {self.smem_base[st.smem]};")
        inst = "cp.async.cg" if st.nbytes == 16 else "cp.async.ca"
        self.e.emit(f"{inst}.shared.global [{saddr}], [{gaddr}], {st.nbytes};")

    def visit_cpasynccommit(self, st):
        self.e.emit("cp.async.commit_group;")

    def visit_cpasyncwait(self, st):
        self.e.emit(f"cp.async.wait_group {st.group};")

    # -- loop-invariant hoisting -------------------------------------------------
    #
    # Our emitted PTX recomputed every address from scratch each iteration;
    # ptxas does not strength-reduce it (measured: m01's inner loop was 4 FFMA
    # vs 86 integer ops). Before entering a loop, walk the body's address /
    # predicate expression trees, split them into maximal subtrees that do not
    # depend on the loop axis or on any per-iteration-defined name, compile
    # those once into the loop preheader, and serve them from a cache while
    # emitting the body. Purely syntactic analysis: names defined by
    # per-iteration statements (loads, lets, accums, nested axes) are never
    # hoisted, so no value read can change under a cached register.

    @staticmethod
    def _ex_dict(ex):
        k = type(ex).__name__
        if k == "Var":
            return {"k": "V", "n": ex.name}
        if k == "Literal":
            return {"k": "L", "v": getattr(ex, "value", None),
                    "d": str(getattr(ex, "dtype", ""))}
        if k == "BinaryExpr":
            return {"k": "B", "op": ex.op,
                    "l": Compiler._ex_dict(ex.left), "r": Compiler._ex_dict(ex.right)}
        if k == "TernaryExpr":
            return {"k": "T", "c": Compiler._ex_dict(ex.cond),
                    "a": Compiler._ex_dict(ex.if_true),
                    "b": Compiler._ex_dict(ex.if_false)}
        # unknown kind: unique key -> never shared
        return {"k": "?" + k, "id": id(ex)}

    @classmethod
    def _ex_key(cls, ex):
        return json.dumps(cls._ex_dict(ex), sort_keys=True)

    @staticmethod
    def _ex_deps(ex, out):
        k = type(ex).__name__
        if k == "Var":
            out.add(ex.name)
        elif k == "BinaryExpr":
            Compiler._ex_deps(ex.left, out)
            Compiler._ex_deps(ex.right, out)
        elif k == "TernaryExpr":
            Compiler._ex_deps(ex.cond, out)
            Compiler._ex_deps(ex.if_true, out)
            Compiler._ex_deps(ex.if_false, out)

    @classmethod
    def _collect_units(cls, ex, forbidden, units):
        """Register maximal subtrees of ex whose deps avoid `forbidden`."""
        deps = set()
        cls._ex_deps(ex, deps)
        if not (deps & forbidden):
            units[cls._ex_key(ex)] = ex
            return
        k = type(ex).__name__
        if k == "BinaryExpr":
            cls._collect_units(ex.left, forbidden, units)
            cls._collect_units(ex.right, forbidden, units)
        elif k == "TernaryExpr":
            cls._collect_units(ex.cond, forbidden, units)
            cls._collect_units(ex.if_true, forbidden, units)
            cls._collect_units(ex.if_false, forbidden, units)

    @staticmethod
    def _stmt_exprs(st):
        """Yield the expression trees a statement feeds to expr() for addressing."""
        k = type(st).__name__
        if k == "Load":
            yield from st.index
        elif k == "Write":
            yield from st.index
        elif k == "CpAsyncCopy":
            yield from st.src_index
            yield from st.smem_index
            if st.lane_index is not None:
                yield from st.lane_index
        elif k == "Cond":
            yield st.cond

    def _hoist_for_loop(self, st):
        """Precompute loop-invariant expression units into the preheader."""
        if not getattr(self, "_hoist_enabled", None):
            self.hoist_stack = getattr(self, "hoist_stack", [])
            self.hoist_stack.append({})
            return
        forbidden = {st.axis.name}
        for sub in st.body.iter():
            k = type(sub).__name__
            if k in ("Load", "Let", "Init", "Assign", "Accum"):
                for nm in (sub.names if k == "Load" else [sub.name]):
                    forbidden.add(nm)
            elif k in ("Loop", "StridedLoop"):
                forbidden.add(sub.axis.name)
        units = {}
        for sub in st.body.iter():
            for ex in self._stmt_exprs(sub):
                self._collect_units(ex, forbidden, units)
        cache = {}
        for key, ex in units.items():
            cache[key] = self.expr(ex)
        self.hoist_stack = getattr(self, "hoist_stack", [])
        self.hoist_stack.append(cache)

    # -- sibling-loop fusion -----------------------------------------------------
    #
    # The attention IR (category 5) runs N sibling dot-product loops per
    # softmax step, each re-loading the same kt column from global memory.
    # Fusing consecutive Loop statements with identical trip counts into one
    # loop lets load_cse serve the repeated loads from a single register.
    # Conservative fusability: same axis name + extent, bodies restricted to
    # straight-line statement kinds, and no later body reads any name an
    # earlier sibling defines.

    _FUSE_BODY_KINDS = {"Load", "Let", "Init", "Assign", "Accum", "Write"}

    @classmethod
    def _stmt_reads(cls, st):
        """Names a statement reads: env lookups + index-expression deps."""
        k = type(st).__name__
        reads = set()
        if k == "Load":
            for ix in st.index:
                cls._ex_deps(ix, reads)
        elif k == "Write":
            for ix in st.index:
                cls._ex_deps(ix, reads)
            reads.update(st.values)
        elif k == "Assign":
            reads.update(st.args)
        elif k == "Accum":
            reads.add(st.value)
            if st.base is not None:
                reads.add(st.base)
        elif k == "Cond":
            cls._ex_deps(st.cond, reads)
        return reads

    @classmethod
    def _stmt_defs(cls, st):
        k = type(st).__name__
        if k == "Load":
            return set(st.names)
        if k in ("Let", "Init", "Assign", "Accum"):
            return {st.name}
        return set()

    def _fusable_pair(self, a, b):
        if self.tuning.get("fuse_loops") is False:
            return False
        if type(a).__name__ != "Loop" or type(b).__name__ != "Loop":
            return False
        if a.axis.name != b.axis.name:
            return False
        if dim_int(a.axis.extent) != dim_int(b.axis.extent):
            return False
        for st in (a, b):
            for sub in st.body.iter():
                if type(sub).__name__ not in self._FUSE_BODY_KINDS:
                    return False
        # cross-references: later sibling must not read earlier siblings' defs
        defs_a = set()
        for sub in a.body.iter():
            defs_a |= self._stmt_defs(sub)
        reads_b = set()
        for sub in b.body.iter():
            reads_b |= self._stmt_reads(sub)
        return not (reads_b & defs_a)

    def _stmts_fused(self, body):
        """Yield statements with fusable sibling-loop runs merged into the first."""
        i, n = 0, len(body)
        while i < n:
            st = body[i]
            if type(st).__name__ == "Loop":
                j = i + 1
                while j < n and self._fusable_pair(st, body[j]):
                    # IR nodes are frozen dataclasses; Body concatenates
                    st = dataclasses.replace(st, body=st.body + body[j].body)
                    j += 1
                self.stmt(st)
                i = j
                continue
            self.stmt(st)
            i += 1

    # -- expressions -----------------------------------------------------------

    def buffer_desc(self, name):
        if name in self.buffers:
            return self.buffers[name]
        # shared arrays are statements, not graph buffers
        return {"cls": "s", "shape": self.smem_stride.get(name, ())}

    def flat_offset(self, index, strides):
        """Compile a coordinate tuple to a flat element offset (b32 register)."""
        if not index:
            return self.const_reg(0)
        total = None
        for ix, stride in zip(index, strides):
            r = self.expr(ix)[0]
            if stride == 0:
                continue
            t = self.e.reg("r")
            if stride == 1:
                self.e.emit(f"mov.u32 {t}, {r};")
            else:
                self.e.emit(f"mul.lo.u32 {t}, {r}, {stride};")
            if total is None:
                total = t
            else:
                s = self.e.reg("r")
                self.e.emit(f"add.u32 {s}, {total}, {t};")
                total = s
        return total or self.const_reg(0)

    def flat_addr(self, buf, index):
        desc = self.buffer_desc(buf)
        strides = self.smem_stride.get(buf) or strides_of(desc["shape"])
        off = self.flat_offset(index, strides)
        if desc["cls"] == "s":
            addr = self.e.reg("r")
            self.e.emit(f"mul.lo.u32 {addr}, {off}, 4;")
            self.e.emit(f"add.u32 {addr}, {addr}, {self.smem_base[buf]};")
            return addr
        addr = self.e.reg("rd")
        byte = self.e.reg("rd")
        self.e.emit(f"mul.wide.s32 {byte}, {off}, 4;")
        self.e.emit(f"add.s64 {addr}, {desc['reg']}, {byte};")
        return addr

    def const_reg(self, value: int) -> str:
        r = self.e.reg("r")
        self.e.emit(f"mov.u32 {r}, {value};")
        return r

    def zero_reg(self) -> str:
        return self.const_reg(0)

    def expr(self, ex):
        """Compile an expression -> (reg, kind) with kind in {'r','f','p'}."""
        if getattr(self, "hoist_stack", None):
            key = self._ex_key(ex)
            for cache in reversed(self.hoist_stack):
                if key in cache:
                    return cache[key]
        kind = type(ex).__name__
        if kind == "Var":
            if ex.name in self.env:
                return self.env[ex.name]
            raise CompileError(f"unbound variable: {ex.name}")
        if kind == "Literal":
            if ex.dtype == "float":
                d = self.e.reg("f")
                self.e.emit(f"mov.f32 {d}, {f32_hex(ex.value)};")
                return (d, "f")
            return (self.const_reg(int(ex.value)), "r")
        if kind == "BinaryExpr":
            return self.binary_expr(ex)
        if kind == "TernaryExpr":
            cond = self.compile_pred(ex.cond)
            a, a_k = self.expr(ex.if_true)
            b, _ = self.expr(ex.if_false)
            d = self.e.reg(a_k)
            ptx_t = "s32" if a_k == "r" else "f32"
            self.e.emit(f"selp.{ptx_t} {d}, {a}, {b}, {cond};")
            return (d, a_k)
        raise CompileError(f"unsupported expression kind: {kind}")

    def binary_expr(self, ex):
        op = ex.op
        if op in CMP_OPS:
            pred = self.compile_pred(ex)
            return (pred, "p")
        left, lk = self.expr(ex.left)
        right, rk = self.expr(ex.right)
        if op in INT_OPS and lk == "r" and rk == "r":
            d = self.e.reg("r")
            # `/`|`%` by a power-of-2 constant: ptxas expands div.s32/rem.s32
            # into float-reciprocal sequences (MUFU/I2F/F2I) per emission site.
            # Address math is non-negative, so unsigned shift/mask is exact.
            if (self.tuning["pow2_shift"] and op in ("/", "%")
                    and type(ex.right).__name__ == "Literal"):
                c = int(ex.right.value)
                if c > 0 and c & (c - 1) == 0:
                    if op == "/":
                        self.e.emit(f"shr.u32 {d}, {left}, {c.bit_length() - 1};")
                    else:
                        self.e.emit(f"and.b32 {d}, {left}, {c - 1};")
                    return (d, "r")
            self.e.emit(f"{INT_OPS[op]} {d}, {left}, {right};")
            return (d, "r")
        if op in self.float_ops and lk == "f" and rk == "f":
            d = self.e.reg("f")
            self.e.emit(f"{self.float_ops[op]} {d}, {left}, {right};")
            return (d, "f")
        raise CompileError(f"unsupported binary op {op} over {lk}/{rk}")

    def compile_pred(self, ex):
        kind = type(ex).__name__
        if kind == "BinaryExpr" and ex.op in CMP_OPS:
            left, lk = self.expr(ex.left)
            right, rk = self.expr(ex.right)
            t = "s32" if lk == "r" else "f32"
            pred = self.e.reg("p")
            self.e.emit(f"setp.{CMP_OPS[ex.op]}.{t} {pred}, {left}, {right};")
            return pred
        # a bare value used as a predicate
        v, k = self.expr(ex)
        pred = self.e.reg("p")
        self.e.emit(f"setp.ne.{ 's32' if k == 'r' else 'f32' } {pred}, {v}, 0;")
        return pred


def strides_of(shape) -> tuple:
    strides = []
    acc = 1
    for dim in reversed(shape):
        strides.append(acc)
        acc *= dim
    return tuple(reversed(strides))


def dim_int_or_const(ex):
    """A step is a literal in every problem; unwrap it."""
    if type(ex).__name__ == "Literal":
        return int(ex.value)
    raise CompileError("non-constant loop step not supported")


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python compile.py <kernel.ir.json>")
    graph = Graph.from_dict(json.load(open(sys.argv[1])))
    compiler = Compiler(graph)
    sys.stdout.write(compiler.compile())


if __name__ == "__main__":
    main()

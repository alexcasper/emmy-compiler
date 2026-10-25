#!/usr/bin/env python3
"""Build sm120/sass/*.md + INDEX.md from the sm_120 probe corpus.

Reads sm120/.cache/sass/results.json (written by tools/sass_probe.py; gitignored raw
artifact) and merges in:

  - NVIDIA's official opcode descriptions from CUDA Binary Utilities, section
    "blackwell-and-rubin-instruction-set" (cached in sm120/.cache/refs/binutils.html),
  - a curated category/notes catalog (observation-based; nothing copied from sm89),
  - encoding observations: normalized operand forms, example instructions with raw
    128-bit encodings, and intersect-derived constant bits per opcode.

There is no kuterdinel-style fuzzed encoding source for sm_120, so every "fixed bits"
claim is explicitly labelled observation-derived and partial: bits constant across our
corpus may still be modifiers in forms we never compiled.

Also writes INDEX.md with the sm89-vs-sm120 divergence tables and the control-code
layout analysis (using sm120/.cache/sass/sched.json for the -O0/-O3 comparison).
"""
import collections
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "sass"
REFS = ROOT / ".cache" / "refs"
OUT = ROOT / "sass"
RESULTS = CACHE / "results.json"
SCHED = CACHE / "sched.json"
BINUTILS = "https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html"
NV_TABLE = BINUTILS + "#blackwell-and-rubin-instruction-set"
SM89_INDEX = ROOT.parent / "sm89" / "sass" / "INDEX.md"

# ---------------------------------------------------------------------------
# curated catalog: category + one-line note per opcode OBSERVED on sm_120.
# Notes state what the opcode did in our probes (ptxas 12.9), not inherited claims.
# ---------------------------------------------------------------------------
(FP32, FP64, FP16, INT, CONV, MOVE, PRED, UNIF, LOAD, ATOM, CTRL, SYNC, TENS, TEX, MISC) = (
    "FP32", "FP64", "FP16 (packed half2)", "Integer", "Conversion", "Movement",
    "Predicate / compare", "Uniform datapath", "Load / store", "Atomics / reductions",
    "Control flow", "Synchronization / barriers", "Tensor core (MMA)", "Texture / surface",
    "Miscellaneous")

CATALOG = {
    "FADD": (FP32, "FP32 add (also the tail of emulated fp ops)"),
    "FFMA": (FP32, "FP32 fused multiply-add"),
    "FMUL": (FP32, "FP32 multiply"),
    "FMNMX": (FP32, "FP32 min/max, incl. .NaN propagation forms (min.NaN/max.NaN)"),
    "FSETP": (FP32, "FP32 compare to predicate"),
    "FSEL": (FP32, "FP32 select by predicate"),
    "FCHK": (FP32, "range check guarding the slow path of div.rn.f32"),
    "MUFU": (FP32, "multi-function unit: rcp/rsqrt/sqrt/lg2/ex2/sin/cos/tanh approx"),
    "FRND": (FP32, "round FP32 to integral value (cvt.rmi/rpi/rzi/rni.f32.f32)"),
    "DADD": (FP64, "FP64 add"),
    "DFMA": (FP64, "FP64 fused multiply-add"),
    "DMUL": (FP64, "FP64 multiply"),
    "DSETP": (FP64, "FP64 compare to predicate"),
    "HFMA2": (FP16, "packed FP16x2/BF16x2 FMA; on sm_120 also absorbs add.f16x2/mul.f16x2 (no HADD2/HMUL2 seen)"),
    "HMNMX2": (FP16, "packed FP16x2 min/max"),
    "HSET2": (FP16, "packed FP16x2 compare writing a mask"),
    "HSETP2": (FP16, "packed FP16x2 compare writing predicates"),
    "IADD3": (INT, "3-input 32-bit integer add"),
    "IADD": (INT, "2-input 32-bit integer add - distinct opcode from IADD3 on sm_120; emitted for PTX add/sub.b32 in some patterns"),
    "IMAD": (INT, "integer multiply-add (.WIDE 64-bit, .HI, and .MOV/IADD move idioms)"),
    "IABS": (INT, "integer absolute value"),
    "ISETP": (INT, "integer compare to predicate"),
    "LEA": (INT, "load effective address (a << s) + b"),
    "LOP3": (INT, "3-input bitwise logic (8-bit LUT)"),
    "SHF": (INT, "funnel shift / 64-bit shifts"),
    "PRMT": (INT, "byte permute"),
    "SGXT": (INT, "sign-extend from bit position (bfe.s32)"),
    "BMSK": (INT, "bit mask build"),
    "FLO": (INT, "find leading one (bfind/clz)"),
    "BREV": (INT, "bit reverse"),
    "POPC": (INT, "population count"),
    "IDP": (INT, "integer dot product (dp4a); also part of vabsdiff4 emulation"),
    "VIADD": (INT, "video-pipe integer add; emitted for PTX vabsdiff4.u32 (VABSDIFF4 not seen on sm_120)"),
    "VIMNMX": (INT, "video-pipe integer min/max; emitted for PTX min.s32 and vabsdiff4 (IMNMX not seen on sm_120)"),
    "F2F": (CONV, "float-to-float conversion (precision change)"),
    "F2I": (CONV, "float-to-integer conversion"),
    "I2F": (CONV, "integer-to-float conversion"),
    "I2FP": (CONV, "integer-to-FP32 on the FMA pipe"),
    "I2I": (CONV, "integer-to-integer conversion (saturating narrow)"),
    "I2IP": (CONV, "pack integers to narrower integers (cvt.pack.sat)"),
    "F2FP": (CONV, "pack two FP32 into FP16x2/BF16x2/FP8 pairs"),
    "MOV": (MOVE, "move register/immediate"),
    "SEL": (MOVE, "select by predicate (integer)"),
    "SHFL": (MOVE, "warp shuffle"),
    "CS2R": (MOVE, "special register pair to registers: %clock64, %globaltimer (SR_GLOBALTIMERLO)"),
    "S2R": (MOVE, "special register to register: %tid, %ctaid, %laneid, %cluster_ctarank -> SR_CgaCtaId"),
    "S2UR": (MOVE, "special register to uniform register (warp-uniform values, e.g. SR_CgaCtaId)"),
    "R2UR": (MOVE, "register to uniform register"),
    "MOVM": (MOVE, "movmatrix transpose (also appears in b1-mma emulation)"),
    "LEPC": (MOVE, "load effective PC (call sites)"),
    "B2R": (MOVE, "barrier state to register (bar.red.popc result)"),
    "PLOP3": (PRED, "3-input predicate logic"),
    "VOTE": (PRED, "warp vote (ballot/all/any)"),
    "MATCH": (PRED, "warp match.any"),
    "ELECT": (PRED, "elect.sync - elect one active lane (new name; sm89-era name: none, feature is sm_90+)"),
    "UMOV": (UNIF, "uniform move/immediate"),
    "UIADD3": (UNIF, "uniform 3-input add"),
    "UIMAD": (UNIF, "uniform multiply-add"),
    "ULEA": (UNIF, "uniform effective address"),
    "USHF": (UNIF, "uniform shift"),
    "ULOP3": (UNIF, "uniform 3-input logic"),
    "UPRMT": (UNIF, "uniform byte permute"),
    "UBREV": (UNIF, "uniform bit reverse"),
    "UPOPC": (UNIF, "uniform population count"),
    "UISETP": (UNIF, "uniform compare to uniform predicate"),
    "UFLO": (UNIF, "uniform find leading one"),
    "VOTEU": (UNIF, "warp vote to uniform register (VOTEU.ANY for activemask)"),
    "LDCU": (UNIF, "uniform load from constant bank (c[0x0][...] kernel params); sm_120 name for sm89's ULDC"),
    "LDG": (LOAD, "global load, .E/.E.64/.E.128 widths, desc[UR4] descriptor addressing"),
    "STG": (LOAD, "global store"),
    "LD": (LOAD, "generic-address load"),
    "ST": (LOAD, "generic-address store"),
    "LDS": (LOAD, "shared load"),
    "STS": (LOAD, "shared store"),
    "LDL": (LOAD, "local load"),
    "STL": (LOAD, "local store"),
    "LDC": (LOAD, "constant-bank load; on sm_120 also the plain register-init form: prologue 'LDC R1, c[0x0][0x37c]' where sm89 used MOV"),
    "LDSM": (LOAD, "ldmatrix shared-load of matrix fragments"),
    "STSM": (LOAD, "stmatrix - store matrix fragments to shared (legal on sm_120; rejected on sm_89)"),
    "LDGSTS": (LOAD, "cp.async global->shared async copy"),
    "LDGDEPBAR": (LOAD, "cp.async commit-group bookkeeping"),
    "CCTL": (LOAD, "cache control / prefetch"),
    "CCTLL": (LOAD, "cache control on local memory"),
    "QSPC": (LOAD, "address-space query (isspacep)"),
    "UBLKCP": (LOAD, "cp.async.bulk (TMA) bulk copy; sm_120 name for the sm_90 TMA copy (plus SYNCS/LDGSTS around it)"),
    "UBLKPF": (LOAD, "cp.async.bulk.prefetch.L2.global"),
    "STAS": (LOAD, "st.async shared store with mbarrier completion (new opcode name on sm_120)"),
    "UMEMSETS": (LOAD, "st.bulk shared-memory bulk init, run with uniform setup (S2UR/ULEA/UMOV)"),
    "ACQBULK": (LOAD, "griddepcontrol.wait - acquire before dependent-launch bulk data"),
    "ATOM": (ATOM, "generic atomic with return"),
    "ATOMG": (ATOM, "global atomic with return; also the vector form (atom.global.v2.add.f32)"),
    "ATOMS": (ATOM, "shared-memory atomic"),
    "REDG": (ATOM, "red.global reduction (no return) - sm_120 name for sm89's RED"),
    "REDUX": (ATOM, "redux.sync warp reduction to register"),
    "BRA": (CTRL, "relative branch"),
    "BRX": (CTRL, "indirect branch (brx.idx jump tables)"),
    "CALL": (CTRL, "subroutine call (non-inlined funcs, TMA/mbarrier helper sequences)"),
    "RET": (CTRL, "return from subroutine"),
    "EXIT": (CTRL, "kernel exit / ret"),
    "BSSY": (CTRL, "convergence-barrier set (start of divergent region)"),
    "BSYNC": (CTRL, "convergence-barrier sync (reconverge)"),
    "WARPSYNC": (CTRL, "warp sync (bar.warp.sync)"),
    "NANOSLEEP": (CTRL, "nanosleep"),
    "NOP": (CTRL, "padding / alignment filler"),
    "PREEXIT": (CTRL, "griddepcontrol.launch_dependents - signal dependent grids may launch"),
    "BAR": (SYNC, "CTA barrier (bar.sync/bar.red)"),
    "MEMBAR": (SYNC, "memory fence (membar/fence.sc/acq_rel)"),
    "DEPBAR": (SYNC, "dependency-barrier wait (cp.async.wait_group)"),
    "ERRBAR": (SYNC, "error barrier (fence.sc.sys sequences)"),
    "CGAERRBAR": (SYNC, "cluster (CGA)-wide error barrier; emitted around fence.acq_rel.cluster / barrier.cluster"),
    "SYNCS": (SYNC, "async-ops synchronize: emitted for cp.async.bulk / st.async / mbarrier sequences (new on sm_120)"),
    "UCGABAR_ARV": (SYNC, "barrier.cluster.arrive on the uniform/CGA barrier path"),
    "UCGABAR_WAIT": (SYNC, "barrier.cluster.wait on the uniform/CGA barrier path"),
    "HMMA": (TENS, "warp-level MMA: f16/bf16/tf32 mma.sync shapes"),
    "IMMA": (TENS, "integer (s8) mma.sync; also the tail of b1-mma emulation (no BMMA opcode seen on sm_120)"),
    "QMMA": (TENS, "FP8 (e4m3/e5m2) mma.sync m16n8k32"),
    "DMMA": (TENS, "FP64 mma.sync m8n8k4 (still present on sm_120)"),
    "TEX": (TEX, "texture fetch"),
    "TLD": (TEX, "texel fetch (tex.1d integer coords)"),
    "TLD4": (TEX, "tld4 texture gather"),
    "TXD": (TEX, "texture fetch with gradients (tex.grad)"),
    "TXQ": (TEX, "texture query (txq/suq; sm_120 form: 'TXQ RZ, R5, R5, TEX_HEADER_DIMENSION, UR4, ...')"),
    "SULD": (TEX, "surface load"),
    "SURED": (TEX, "surface reduction (no return)"),
    "SUST": (TEX, "surface store"),
    "PMTRIG": (MISC, "pmevent profiler trigger"),
}

# ---------------------------------------------------------------------------
# NVIDIA Blackwell/Rubin opcode table
# ---------------------------------------------------------------------------

def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).replace("\xa0", " ").strip()


def nvidia_table():
    path = REFS / "binutils.html"
    if not path.exists():
        raise SystemExit(f"missing {path}; fetch {BINUTILS} first (curl -o)")
    page = path.read_text(encoding="utf-8", errors="replace")
    start = page.index('id="blackwell-and-rubin-instruction-set"')
    end = page.find('id="cu-filt"', start)
    tail = page[start:end if end > 0 else len(page)]
    table, section = {}, ""
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", tail, re.S):
        cells = [strip_tags(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
        if len(cells) < 2 or cells[0] == "Opcode":
            continue
        if not cells[1]:
            section = cells[0]
        else:
            table[cells[0]] = (section, cells[1])
    return table


# ---------------------------------------------------------------------------
# instruction-text normalization
# ---------------------------------------------------------------------------
PRED_RE = re.compile(r"^@!?U?P[T0-9]+\s+")


def mnemonic(text):
    return PRED_RE.sub("", text).split()[0].split(".")[0]


def normalize(text):
    """Normalized operand signature of one instruction, e.g. 'LDG.E R, desc[UR][R.64]'."""
    t = PRED_RE.sub("", text).strip()
    t = re.sub(r"\bUR(Z|\d+)\b", "UR", t)
    t = re.sub(r"\bUP(T|Z|\d+)\b", "UP", t)
    t = re.sub(r"\bP(T|Z|\d+)\b", "P", t)
    t = re.sub(r"\bR(Z|\d+)\b", "R", t)
    t = re.sub(r"\bSR_[A-Za-z0-9_.]+", "SR", t)
    t = re.sub(r"c\[0x[0-9a-f]+\]\[0x[0-9a-f]+\]", "c[][]", t)
    t = re.sub(r"desc\[UR\]\[", "desc[UR][", t)
    t = re.sub(r"\b0[xX][0-9a-fA-F]+", "IMM", t)
    t = re.sub(r"\b0[fFdD][0-9a-fA-F]+", "IMM", t)
    t = re.sub(r"\(\.L_\w+\)", "(L)", t)
    t = re.sub(r"\b\d+\b", "IMM", t)
    return t


# ---------------------------------------------------------------------------
# aggregation
# ---------------------------------------------------------------------------

def const_mask(bits_list):
    acc = None
    for bits in bits_list:
        if acc is None:
            acc = list(bits)
        else:
            for i, c in enumerate(bits):
                if acc[i] != c:
                    acc[i] = "."
    return "".join(acc)


def bits_str(w0, w1):
    v = int(w0, 16) | (int(w1, 16) << 64)
    return "".join(str((v >> b) & 1) for b in range(128))


def fmt_mask(m):
    return m[:64] + "\n" + m[64:]


def aggregate():
    res = json.loads(RESULTS.read_text())
    ops = collections.defaultdict(lambda: {
        "count": 0, "probes": collections.OrderedDict(), "bits": [], "forms": collections.defaultdict(list)})
    for r in res["probes"]:
        for i in r.get("instrs", []):
            op = i["op"]
            if op not in CATALOG:      # BRA/EXIT/NOP etc are in CATALOG; anything unexpected still recorded
                CATALOG.setdefault(op, ("Uncategorized", ""))
            d = ops[op]
            d["count"] += 1
            d["probes"].setdefault(r["name"], r["ptx"])
            b = bits_str(i["w0"], i["w1"])
            d["bits"].append(b)
            d["forms"][normalize(i["text"])].append((i["text"], i["w0"], i["w1"], r["name"]))
    return res, ops


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

def render_op(op, d, nv):
    cat, note = CATALOG[op]
    out = [f"# {op} (SM120 SASS)", ""]
    if op in nv:
        sec, desc = nv[op]
        out += [f"**NVIDIA:** {desc} ({sec}). Source: [CUDA Binary Utilities, Blackwell/Rubin instruction set]({NV_TABLE})", ""]
    else:
        out += [f"**NVIDIA:** not listed in NVIDIA's Blackwell/Rubin opcode table ([CUDA Binary Utilities]({BINUTILS})).", ""]
    out += [f"Notes: {note} (category: {cat})", ""]
    n_probes = len(d["probes"])
    out += [f"Observed on sm_120: {d['count']} instruction(s) across {n_probes} probe(s).", "", "## Evidence", ""]
    out += ["Compiled with ptxas V12.9.86 (`-arch=sm_120`, PTX `.version 8.8`) and read back with "
            "nvdisasm V12.9.88 (`-hex -c`). All encodings below are raw 128-bit values from that "
            "output; bit 0 is the LSB of the first 64-bit word.", ""]
    out += ["Emitted by probe(s):", ""]
    for name, ptx in d["probes"].items():
        out.append(f"- `{name}`: `{ptx}`")
    low12 = sorted({b[:12] for b in d["bits"]})
    out += ["", "12-bit opcode field (bits 0-11) values observed: " +
            ", ".join(f"`0x{int(v, 2):03x}`" for v in low12) + "."]
    mask = const_mask(d["bits"])
    nfix = mask.count("0") + mask.count("1")
    out += ["", "## Encoding observations", "",
            f"**Constant bits across all {d['count']} observed instance(s): {nfix} of 128** "
            "(observation-derived and *partial*: there is no fuzzed encoding reference for sm_120, "
            "so bits that never varied here may still be modifiers in forms this corpus never "
            "compiled; bits 105-125 are the scheduling control code and vary with instruction "
            "placement). LSB-first, bit 0 first:", "", "```", fmt_mask(mask), "```", ""]
    forms = sorted(d["forms"].items(), key=lambda kv: -len(kv[1]))
    shown = forms[:8]
    out += [f"{len(forms)} normalized operand form(s) observed"
            + (f" (showing {len(shown)})" if len(forms) > len(shown) else "") + ":", ""]
    for form, examples in shown:
        out += [f"### `{form}` - {len(examples)} instance(s)", "", "| instruction | encoding (word0 word1) | probe |",
                "|---|---|---|"]
        seen_probe = set()
        n = 0
        for text, w0, w1, pname in examples:
            if pname in seen_probe and n >= 3:
                continue
            seen_probe.add(pname)
            out.append(f"| `{text}` | `{w0} {w1}` | {pname} |")
            n += 1
        out.append("")
    if len(forms) > len(shown):
        out += ["Additional forms: " + ", ".join(f"`{f}`" for f, _ in forms[len(shown):]), ""]
    return "\n".join(out) + "\n"


def divergence_table(ops):
    sm89 = sorted(p.stem for p in (SM89_INDEX.parent).glob("*.md") if p.stem != "INDEX")
    sm120 = sorted(ops)
    new = [o for o in sm120 if o not in sm89]
    gone = [o for o in sm89 if o not in sm120]
    lines = ["## Divergence vs the SM89 knowledge base", "",
             f"sm89/sass documents {len(sm89)} opcodes (kuterdinel.com fuzzed encoding pages for Ada). "
             f"This corpus observed {len(sm120)} opcodes on sm_120. Both directions are *observations*, "
             "not exhaustive ISA statements: an opcode absent here was simply never emitted by these "
             f"{len(json.loads(RESULTS.read_text())['probes'])} probe kernels.", ""]
    lines += ["### Observed on sm_120, not in the sm89 opcode set", "",
              "| opcode | note (from our probes) |", "|---|---|"]
    renames = {
        "LDCU": "rename of sm89 `ULDC` (uniform constant load); prologue uses `LDCU.64 UR4, c[0x0][0x358]`",
        "IADD": "new 2-input add; sm89 had only IADD3 (both exist on sm_120)",
        "REDG": "rename of sm89 `RED` (global reduction without return)",
        "STSM": "stmatrix (rejected on sm_89, legal on sm_120)",
        "ELECT": "elect.sync (rejected on sm_89, legal on sm_120)",
        "STAS": "st.async (sm_90+ feature; new opcode name here)",
        "UBLKCP": "cp.async.bulk / TMA copy (sm_90+ feature)",
        "UBLKPF": "cp.async.bulk.prefetch.L2.global (sm_90+ feature)",
        "UMEMSETS": "st.bulk shared-memory init (sm_90+ feature)",
        "ACQBULK": "griddepcontrol.wait (sm_90+ feature)",
        "PREEXIT": "griddepcontrol.launch_dependents (sm_90+ feature)",
        "UCGABAR_ARV": "barrier.cluster.arrive (sm_90+ feature)",
        "UCGABAR_WAIT": "barrier.cluster.wait (sm_90+ feature)",
        "CGAERRBAR": "cluster-wide error barrier (emitted with fence.acq_rel.cluster)",
        "SYNCS": "async-group synchronize (emitted around UBLKCP/STAS/mbarrier sequences)",
        "VIADD": "video-pipe integer add (vabsdiff4 emulation)",
        "VIMNMX": "video-pipe integer min/max; PTX min.s32 lowers here (sm89: IMNMX)",
    }
    for o in new:
        lines.append(f"| [`{o}`]({o}.md) | {renames.get(o, CATALOG[o][1])} |")
    lines += ["", "### In the sm89 opcode set, not observed on sm_120 here", "",
              "| opcode | status in this corpus |", "|---|---|"]
    gone_note = {
        "HADD2": "add.f16x2 lowered to HFMA2 (`probe hadd2`)",
        "HMUL2": "mul.f16x2 lowered to HFMA2 (`probe hmul2`)",
        "IMNMX": "min/max.s32 lowered to VIMNMX (`probe imnmx`)",
        "BMMA": "b1 mma.sync lowered to IMMA+MOVM+LOP3 emulation (`probe bmma`)",
        "RED": "red.global lowered to REDG (`probe red`)",
        "ULDC": "renamed LDCU (`every probe's prologue`)",
        "VABSDIFF": "PTX vabsdiff emulated with IADD3/ISETP/PRMT (`probe vabsdiff`)",
        "VABSDIFF4": "PTX vabsdiff4 emulated with VIADD+VIMNMX+IDP (`probe vabsdiff4`)",
        "FSET": "not reproduced (sm89 also could not reproduce it)",
        "FSWZADD": "graphics/derivative op - no PTX source; not probed",
        "TMML": "texture mip-level query - not probed",
        "FOOTPRINT": "texture footprint query - not probed",
        "SUATOM": "surface atomic with return - not probed (SURED/SUST were)",
        "SUQUERY": "PTX suq lowered to TXQ (`probe suq`)",
        "P2R": "predicate pack - not triggered by this corpus",
        "R2P": "predicate unpack - not triggered by this corpus",
        "UP2UR": "uniform predicate spill - not triggered by this corpus",
        "UR2UP": "uniform predicate restore - not triggered by this corpus",
        "UF2FP": "uniform FP pack - not triggered by this corpus",
        "USGXT": "uniform sign-extend - not triggered by this corpus",
        "UBMSK": "uniform bit-mask - not triggered by this corpus",
        "UPLOP3": "uniform predicate logic - not triggered by this corpus",
        "USEL": "uniform select - not triggered by this corpus",
        "UCLEA": "not triggered by this corpus",
        "BMOV": "convergence-barrier save/restore - not triggered by this corpus",
        "RPCMOV": "return-PC move - not triggered by this corpus",
        "BRXU": "uniform-index jump table - not probed",
        "JMP": "absolute jump - not probed",
        "JMX": "absolute indirect jump - not probed",
        "JMXU": "uniform absolute indirect jump - not probed",
        "BRXU_": "",
        "YIELD": "spin-loop yield - not triggered by this corpus",
        "BREAK": "divergent break - not triggered by this corpus",
        "SETCTAID": "cluster CTA-id set - not probed",
        "GETLMEMBASE": "local-memory base - not triggered by this corpus",
        "ALD": "graphics-only ops (ALD, AL2P, IPA, ISBERD, OUT, PIXLD, LDTRAM, CSMTEST) - no PTX equivalent, not probed",
    }
    skip = {"AL2P", "IPA", "ISBERG", "ISBERD", "OUT", "PIXLD", "LDTRAM", "CSMTEST"}
    for o in gone:
        if o in skip:
            continue
        note = gone_note.get(o, "not produced by this probe corpus (may still exist in the ISA)")
        lines.append(f"| {o} | {note} |")
    gfx = [o for o in gone if o in skip]
    if gfx:
        lines += ["", "Graphics-only sm89 opcodes not probed here (no PTX equivalent): " +
                  ", ".join(f"`{o}`" for o in gfx) + ".", ""]
    lines += ["### Rejected sm_120 probes (architecture evidence)", "",
              "| PTX construct | ptxas 12.9 result |", "|---|---|"]
    res = json.loads(RESULTS.read_text())
    for r in res["probes"]:
        if r["status"] in ("rejected (ok)", "ptxas error", "ACCEPTED (expected reject)"):
            err = r.get("error", r["status"])
            lines.append(f"| `{r['ptx']}`{' via ' + r['arch'] if r['arch'] != 'sm_120' else ''} | {err} |")
    lines.append("")
    return "\n".join(lines)


def control_code_section(ops):
    lines = ["## Control-code layout (bits 105-125)", "",
             "Hypothesis (from sm_89 microbenchmark literature, tested here): stall(105-108), "
             "yield(109), write/result scoreboard(110-112), read scoreboard(113-115), wait "
             "mask(116-121), reuse(122-125). On sm_120 the same classification falls out of the "
             "encodings:", "",
             "- **110-112 != 7** on result-latency producers (>50% of instances): LDG, LD, LDS, LDL, "
             "LDC, LDCU, MUFU, S2R, S2UR, SHFL, MATCH, REDUX, MOVM, B2R, TEX/TLD/TLD4/TXD/TXQ, "
             "SULD, conversions (F2F/F2I/I2F), FP64 ops, FCHK, QSPC, LDGDEPBAR, SYNCS - i.e. "
             "instructions whose *result* arrives late. Same class as sm_89.",
             "- **113-115 != 7** on late source readers: SUST, SURED, UBLKCP, UBLKPF, UMEMSETS "
             "(and STG/ATOMS only in specific fence sequences) - instructions that read their "
             "*source registers* late. Same class as sm_89.",
             "- **bits 122-125 (reuse) were 0 in this corpus** and bits 126-127 were always 0.", "",
             "### Same instructions, different schedules",
             ""]
    sched = json.loads(SCHED.read_text())["sched"] if SCHED.exists() else {}
    diff = collections.Counter()
    pairs = 0
    for name in sched.get("O0", {}):
        a, b = sched["O0"].get(name), sched.get("O3", {}).get(name)
        if not isinstance(a, list) or not isinstance(b, list):
            continue
        da = {i["addr"]: i for i in a}
        for i in b:
            j = da.get(i["addr"])
            if j and j["text"] == i["text"]:
                pairs += 1
                va = int(j["w0"], 16) | int(j["w1"], 16) << 64
                vb = int(i["w0"], 16) | int(i["w1"], 16) << 64
                for bit in range(128):
                    if ((va >> bit) & 1) != ((vb >> bit) & 1):
                        diff[bit] += 1
    if pairs:
        bits = sorted(diff)
        lo = [b for b in bits if b < 105]
        lines += [f"{pairs} instructions with identical opcode, operands and immediates were "
                  f"re-encoded between `-O0` and `-O3`. Every differing bit lies in 105-117 "
                  f"(observed: {', '.join(map(str, bits))});"
                  + (f" no bits below 105 ever differed" if not lo else f" NOTE: bits below 105 also differed: {lo}")
                  + ". So the scheduling control code occupies the same region as sm_89 "
                    "(stall/yield/scoreboards/wait), and no data-path bits move with the schedule. "
                    "The 3-bit field *boundaries* cannot be proven from encoding diffs alone, but "
                    "the producer/consumer classification above is consistent with the sm_89 "
                    "assignment (stall 105-108, yield 109, write 110-112, read 113-115, "
                    "wait 116-121).", ""]
    else:
        lines += ["sched.json missing or empty - run `sass_probe.py --sched`.", ""]
    return "\n".join(lines)


def render_index(res, ops, nv):
    by_cat = collections.defaultdict(list)
    for op, d in ops.items():
        by_cat[CATALOG[op][0]].append(op)
    n_ok = sum(r["status"] in ("ok", "rejected (ok)") for r in res["probes"])
    n_instr = sum(d["count"] for d in ops.values())
    tools = res["tools"]
    lines = ["# SM120 SASS instruction index", "",
             f"{len(ops)} distinct SASS opcodes observed on **sm_120** (Blackwell consumer) by "
             f"compiling {n_ok} PTX probe kernels (PTX `.version 8.8`, `.target sm_120`) with "
             f"ptxas `{tools['ptxas']}` and reading every instruction's raw 128-bit encoding from "
             f"nvdisasm `{tools['nvdisasm']}` (`-hex -c`). {n_instr} instructions total.",
             "",
             "Everything in `sass/` is derived from these probes: there is **no** kuterdinel-style "
             "fuzzed encoding reference for sm_120, so per-opcode \"fixed bits\" are intersect-derived "
             "from the corpus and explicitly labelled partial. The probe corpus is deliberately "
             "sm_120-native; no sm_89 claims were copied.",
             "",
             "Raw artifacts: `sm120/.cache/sass/results.json` (per-probe instruction dump, gitignored).",
             "",
             "Columns: **NVIDIA description** from the Blackwell/Rubin opcode table "
             f"([CUDA Binary Utilities]({NV_TABLE})); **emitted by** = probe names that produced the "
             "opcode; **enc** = instructions observed; **ops** = distinct 12-bit opcode-field values; "
             "**forms** = normalized operand forms.", ""]
    cat_order = sorted(by_cat, key=lambda c: (c == "Uncategorized", c))
    for cat in cat_order:
        lines += [f"## {cat}", "",
                  "| opcode | NVIDIA description | emitted by probes | enc | ops | forms |",
                  "|---|---|---|---|---|---|"]
        for op in sorted(by_cat[cat]):
            d = ops[op]
            if op in nv:
                desc = nv[op][1]
            else:
                desc = "*not in NVIDIA Blackwell/Rubin table*"
            probes = list(d["probes"])
            ptxt = ", ".join(f"`{p}`" for p in probes[:3]) + (f" +{len(probes) - 3} more" if len(probes) > 3 else "")
            vals = ", ".join(f"`{int(v, 2):03x}`" for v in sorted({b[:12] for b in d['bits']}))
            if len(vals) > 60:
                vals = f"{len(set(b[:12] for b in d['bits']))} values"
            lines.append(f"| [`{op}`]({op}.md) | {desc} | {ptxt} | {d['count']} | {vals} | {len(d['forms'])} |")
        lines.append("")
    lines += [divergence_table(ops), "", control_code_section(ops), "",
              "## Regenerate", "",
              "```",
              "PTXAS=/mnt/d/ops/emmy/toolchain/cuda12.9/bin/ptxas \\",
              "NVDISASM=/mnt/d/ops/emmy/toolchain/cuda12.9/bin/nvdisasm \\",
              "  python3 sm120/tools/sass_probe.py          # probe battery (resumable)",
              "  python3 sm120/tools/sass_probe.py --sched  # -O0/-O2/-O3 control-code study",
              "  python3 sm120/tools/build_sass.py          # this index + per-opcode pages",
              "```", ""]
    return "\n".join(lines)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    nv = nvidia_table()
    res, ops = aggregate()
    for op, d in sorted(ops.items()):
        (OUT / f"{op}.md").write_text(render_op(op, d, nv))
    (OUT / "INDEX.md").write_text(render_index(res, ops, nv))
    n_nv = sum(1 for op in ops if op in nv)
    print(f"{len(ops)} opcode pages + INDEX.md; {n_nv} have an NVIDIA Blackwell-table description; "
          f"{sum(d['count'] for d in ops.values())} instructions")
    missing_nv = sorted(op for op in ops if op not in nv)
    if missing_nv:
        print("no NVIDIA description:", ", ".join(missing_nv))


if __name__ == "__main__":
    main()

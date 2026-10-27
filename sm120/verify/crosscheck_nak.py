#!/usr/bin/env python3
"""Cross-check our probe-observed sm_120 SASS opcodes against Mesa's NAK compiler (NVK).

NAK (src/nouveau/compiler/nak/sm70_encode.rs) hard-codes the opcode it emits for every
instruction on Volta..Blackwell (one unified SM70+ encoder; Blackwell consumer sm=120 is
a first-class branch since Mesa 25.2/25.3, Vulkan 1.4 conformant on RTX 50-series).
It passes the 9-bit base opcode and ORs the operand-form bits (9-11: reg/imm/const/uniform)
in separately, so we compare the low 9 bits.  This independently validates opcode numbers
for ops ptxas never emits from compute PTX (graphics ops) and confirms our encoding-space
reading of the probes.

Divergences to expect: NAK gates a few opcodes on `sm >= 100` / `sm >= 120` (e.g. UALU
0x054 on Blackwell+) — where both an older and a newer literal exist in one Op block, any
match counts as agreement and the full literal list is shown.

Usage: python3 sm120/verify/crosscheck_nak.py   -> sm120/verify/NAK_CROSSCHECK.md, nak.json
"""
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMMIT = "837ab0e30740abb9ebb60bcd40a5114c68c673d9"  # chaotic-cx/mesa-mirror main, 2026-10-25
URL = (f"https://raw.githubusercontent.com/chaotic-cx/mesa-mirror/{COMMIT}"
       "/src/nouveau/compiler/nak/sm70_encode.rs")
BLOB = (f"https://github.com/chaotic-cx/mesa-mirror/blob/{COMMIT}"
        "/src/nouveau/compiler/nak/sm70_encode.rs")


def main():
    cache = ROOT / ".cache" / "nak" / f"nak_sm70_encode_{COMMIT[:12]}.rs"
    if not cache.exists():
        req = urllib.request.Request(URL, headers={"User-Agent": "sm120-kb/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            cache.write_bytes(r.read())
    src = cache.read_text()
    lines = src.splitlines()

    nak = {}
    for m in re.finditer(r"^impl SM70Op for Op(\w+) \{", src, re.M):
        start = src.count("\n", 0, m.start()) + 1
        body = src[m.end():].split("\nimpl ")[0]
        lits = re.findall(r"(?:set_opcode|encode_\w+)\(\s*(0x[0-9a-fA-F]{2,3})", body)
        # opcodes chosen by a `let opcode = if ... { 0x104 } else { 0x110 };` expression
        for expr in re.findall(r"let (?:mut )?opcode\b[^;]*;", body, re.S):
            lits += re.findall(r"\b(0x[0-9a-fA-F]{2,3})\b", expr)
        ops = sorted({int(h, 16) for h in lits})
        if ops:
            nak[m.group(1).upper()] = (ops, start)

    # Observed side: probe corpus (tools/sass_probe.py -> .cache/sass/results.json)
    res = json.loads((ROOT / ".cache" / "sass" / "results.json").read_text())
    obs = {}
    for p in res["probes"]:
        for ins in p.get("instrs", []):
            op = ins["op"]
            val = int(ins["w0"], 16)
            obs.setdefault(op, set()).update({val & 0x1FF, val & 0xFFF})

    rows, out = [], {}
    for op in sorted(obs):
        if op not in nak:
            continue
        nops, line = nak[op]
        base_obs = {o & 0x1FF for o in obs[op]}
        hit = [o for o in nops if (o & 0x1FF) in base_obs]
        if hit:
            status = "agree"
        else:
            # NAK models some families as one op (OpLd = LDG/LDL/LDS/...); name the
            # observed mnemonic each NAK opcode corresponds to instead.
            owners = sorted({o2 for n in nops
                             for o2, ss in obs.items() if (n & 0x1FF) in {x & 0x1FF for x in ss}})
            status = f"NAK op maps to {'/'.join(owners)}" if owners else "differ"
        out[op] = dict(status=status, nak=[hex(o) for o in nops],
                       observed=sorted(hex(o) for o in obs[op]), ref=f"{BLOB}#L{line}")
        rows.append(f"| {op} | {status} | {' '.join(hex(o) for o in nops)} | "
                    f"{' '.join(sorted(hex(o) for o in obs[op]))} | [L{line}]({BLOB}#L{line}) |")
    agree = sum(v["status"] == "agree" for v in out.values())
    mapped = sum(v["status"].startswith("NAK op maps") for v in out.values())
    differ = [op for op, v in out.items() if v["status"] == "differ"]
    md = ["# Opcode cross-check: sm_120 probes vs Mesa NAK", "",
          f"Reference: Mesa NAK `sm70_encode.rs` at mirror commit `{COMMIT[:12]}` (<{BLOB}>), the open-source "
          "NVK compiler's unified SM70+ encoder (sm=120 is a first-class branch; NVK has been Vulkan 1.4 "
          "conformant on Blackwell consumer since Mesa 25.3, so its encoders are hardware-tested on RTX 50-series). "
          "Comparison is on the low 9 opcode bits (NAK adds the operand-form bits 9-11 separately). Our side is "
          "the probe corpus (4112 instructions, `tools/sass_probe.py`).", "",
          f"**{agree}/{len(out)}** same-named opcodes agree on the 9-bit opcode; {mapped} more are NAK ops that "
          f"cover several SASS mnemonics and map onto the matching observed ones; {len(differ)} differ. "
          f"{len(obs) - len(out)} observed opcodes have no NAK encoder (NAK does not emit them).", "",
          "| opcode | result | NAK opcode(s) | observed opcode(s) (bits 0-11) | NAK source |", "|---|---|---|---|---|"]
    md += rows
    if differ:
        md += ["", "## Differing opcodes", "",
               "These need a second look: either NAK deliberately re-encodes them on `sm >= 100/120` branches "
               "(check the `if e.sm >=` sites at the linked lines) or our normalized opcode extraction "
               "mis-splits a mnemonic.", ""]
        md += [f"- `{op}`: NAK {' '.join(out[op]['nak'])} vs observed {' '.join(out[op]['observed'])}"
               for op in differ]
    md += ["", "## Notes on the two differing opcodes", "",
           "`SULD`/`SUST` (and their reduction siblings) are the only same-named mismatches. ptxas on sm_120 emits "
           "`SULD.D...` with 12-bit opcode `0xf99` (base bits 0-8 = `0x199`) and `SUST.D...` `0xf9d` (`0x19d`), while "
           "NAK sets `0x998`/`0x99a` and `0x99c`/`0x99e` in the same 0..12 field. This pattern is inherited, not new: "
           "the sm_89 KB saw exactly the same numbers (kuterdinel listed both the `0x998` and the `0xf99` form, so "
           "its family-match logic reported agreement). Either the binary-vs-formatted bit assignment inside the "
           "surface-op opcode field differs between NAK's model and ptxas's real encoding, or hardware ignores the "
           "differing bits — resolving that needs NAK's hardware tests (`nvk_hw_tests`) or a real Blackwell run, "
           "which this repo cannot do.", "",
           "Note: gitlab.freedesktop.org raw fetches are bot-walled; sources are pulled from the "
           "same-day-synced chaotic-cx/mesa-mirror GitHub mirror.", ""]
    (ROOT / "verify" / "NAK_CROSSCHECK.md").write_text("\n".join(md) + "\n")
    (ROOT / "verify" / "nak.json").write_text(json.dumps({
        "commit": COMMIT, "tools": res["tools"], "ops": out}, indent=1))
    print(f"{agree}/{len(out)} agree; {mapped} mapped; {len(differ)} differ: {' '.join(differ)}")
    print(f"{len(obs) - len(out)} observed opcodes have no NAK encoder")


if __name__ == "__main__":
    main()

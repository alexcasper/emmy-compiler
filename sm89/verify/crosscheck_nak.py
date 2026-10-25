#!/usr/bin/env python3
"""Cross-check the scraped SASS opcodes against Mesa's NAK compiler (NVK, open source).

NAK (src/nouveau/compiler/nak/sm70_encode.rs) hard-codes the opcode it emits for every
instruction on Volta..Ada (SM70+ encoding).  It passes the 9-bit base opcode and ORs the
operand-form bits (9-11: reg/imm/const/uniform) in separately, so we compare low 9 bits.
This independently confirms opcodes ptxas never emits from compute PTX (graphics ops).

Usage: python3 sm89/verify/crosscheck_nak.py   -> sm89/verify/NAK_CROSSCHECK.md, nak.json
"""
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMMIT = "e7371b0711bb1cd38c39d1c05e5578c445cc6bca"  # mesa main at time of writing
URL = f"https://gitlab.freedesktop.org/mesa/mesa/-/raw/{COMMIT}/src/nouveau/compiler/nak/sm70_encode.rs"
BLOB = f"https://gitlab.freedesktop.org/mesa/mesa/-/blob/{COMMIT}/src/nouveau/compiler/nak/sm70_encode.rs"


def main():
    cache = ROOT / ".cache" / "refs" / f"nak_sm70_encode_{COMMIT[:12]}.rs"
    if not cache.exists():
        with urllib.request.urlopen(URL, timeout=60) as r:
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

    sys.path.insert(0, str(ROOT / "tools"))
    from build_sass import parse_variants
    site = {}
    for f in (ROOT / ".cache" / "sass").glob("*.html"):
        if f.stem == "index":
            continue
        site[f.stem] = sorted({int(v["enc"][1][:12][::-1], 2) for v in parse_variants(f.read_text(errors="replace"))
                               if v["enc"] and "." not in v["enc"][1][:12]})

    rows, out = [], {}
    for op in sorted(site):
        if op not in nak:
            continue
        nops, line = nak[op]
        base_site = {o & 0x1FF for o in site[op]}
        hit = [o for o in nops if (o & 0x1FF) in base_site]
        if hit:
            status = "agree"
        else:
            # NAK models some families as one op (OpLd = LDG/LDL/LDS/...); name the site
            # mnemonic each NAK opcode corresponds to instead.
            owners = sorted({o2 for n in nops for o2, ss in site.items() if (n & 0x1FF) in {x & 0x1FF for x in ss}})
            status = f"NAK op maps to {'/'.join(owners)}" if owners else "differ"
        out[op] = dict(status=status, nak=[hex(o) for o in nops], site=[hex(o) for o in site[op]],
                       ref=f"{BLOB}#L{line}")
        rows.append(f"| {op} | {status} | {' '.join(hex(o) for o in nops)} | "
                    f"{' '.join(hex(o) for o in site[op])} | [L{line}]({BLOB}#L{line}) |")
    agree = sum(v["status"] == "agree" for v in out.values())
    mapped = sum(v["status"].startswith("NAK op maps") for v in out.values())
    md = ["# Opcode cross-check: kuterdinel pages vs Mesa NAK", "",
          f"Reference: Mesa NAK `sm70_encode.rs` at commit `{COMMIT[:12]}` (<{BLOB}>), the open-source "
          "NVK compiler's SM70+ (Volta-Ada) encoder. Comparison is on the low 9 opcode bits (NAK adds the "
          "operand-form bits 9-11 separately).", "",
          f"**{agree}/{len(out)}** same-named opcodes agree; {mapped} more are NAK ops that cover several "
          "SASS mnemonics and map onto the matching scraped ones; "
          f"{len(out) - agree - mapped} differ. "
          f"{len(site) - len(out)} scraped opcodes have no NAK encoder (NAK does not emit them).", "",
          "| opcode | result | NAK opcode(s) | site opcode(s) (bits 0-11) | NAK source |", "|---|---|---|---|---|"]
    (ROOT / "verify" / "NAK_CROSSCHECK.md").write_text("\n".join(md + rows) + "\n")
    (ROOT / "verify" / "nak.json").write_text(json.dumps({"commit": COMMIT, "ops": out}, indent=1))
    print(f"{agree}/{len(out)} agree, {mapped} mapped;", {o: v["status"] for o, v in out.items() if v["status"] != "agree"})


if __name__ == "__main__":
    main()

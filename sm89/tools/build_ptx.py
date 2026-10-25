#!/usr/bin/env python3
"""Fetch NVIDIA's PTX ISA reference and split it into per-section markdown.

Usage: python3 sm89/tools/build_ptx.py      (needs pandoc; raw HTML cached in sm89/.cache/ptx)

Layout written under sm89/ptx/:
  NN-<chapter>.md                     chapters other than 9
  09-instruction-set.md               9.1-9.6 (format, predication, typing, semantics)
  instructions/NN-<family>/<M>-<name>.md   one file per 9.7.N.M instruction section
  INDEX.md                            per-instruction table with an sm_89 availability column
"""
import pathlib
import shutil
import re
import subprocess
import urllib.request

URL = "https://docs.nvidia.com/cuda/parallel-thread-execution/index.html"
ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "ptx"
OUT = ROOT / "ptx"
SM = 89
REMOTE_IMG = ("instructions/17-", "instructions/18-")

HEAD_RE = re.compile(r"^(#{1,6}) (.*)$")


def fetch():
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / "index.html"
    if not path.exists():
        req = urllib.request.Request(URL, headers={"User-Agent": "sm89-kb/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            path.write_bytes(r.read())
    s = path.read_text(encoding="utf-8")
    m = re.search(r'<div itemprop="articleBody">.*?(?=<footer)', s, re.S)
    body = CACHE / "body.html"
    body.write_text(m.group(0) if m else s)
    return subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none", str(body)],
                          check=True, capture_output=True, text=True).stdout


def clean_heading(text):
    """'1.1. [Title](#a)[](#a "Permalink...")' -> ('1.1.', 'Title', 'a')."""
    anchor = re.search(r"\(#([^)\s]+)", text)
    text = re.sub(r'\[\]\(#[^)]*"Permalink to this headline"\)', "", text)
    text = re.sub(r"\[([^\]]*)\]\(#[^)]*\)", r"\1", text).strip()
    m = re.match(r"([\d.]+)\s+(.*)", text)
    num, title = (m.group(1), m.group(2)) if m else ("", text)
    return num, title, anchor.group(1) if anchor else None


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def section_tree(md):
    """Yield (level, num, title, anchor, body_lines) for every heading."""
    secs, cur = [], None
    for line in md.splitlines():
        m = HEAD_RE.match(line)
        if m:
            num, title, anchor = clean_heading(m.group(2))
            cur = [len(m.group(1)), num, title, anchor, []]
            secs.append(cur)
        elif cur is not None:
            cur[4].append(line)
    return secs


def assign_files(secs):
    """Map each section to an output file path (relative to OUT)."""
    files, chapter = [], None
    for lvl, num, title, anchor, _ in secs:
        parts = [p for p in num.split(".") if p]
        if lvl == 1:
            chapter = f"{int(parts[0]):02d}-{slug(title)}.md" if parts else f"{slug(title)}.md"
        if len(parts) >= 4 and parts[:2] == ["9", "7"]:
            fam = next(s for s in secs if s[1].rstrip(".") == ".".join(parts[:3]))
            path = (f"instructions/{int(parts[2]):02d}-{slug(fam[2])}/"
                    f"{int(parts[3]):02d}-{slug(next(s for s in secs if s[1].rstrip('.') == '.'.join(parts[:4]))[2].split(':')[-1])}.md")
        elif len(parts) == 3 and parts[:2] == ["9", "7"]:
            path = f"instructions/{int(parts[2]):02d}-{slug(title)}/00-overview.md"
        else:
            path = chapter
        files.append(path)
    return files


def isa_notes(lines, label):
    out, grab = [], False
    for ln in lines:
        if ln.strip() == label:
            grab = True
            continue
        if grab and ln.strip() in ("Examples", "Semantics", "Notes", "Description", "PTX ISA Notes",
                                   "Target ISA Notes", "Syntax"):
            break
        if grab and ln.strip():
            out.append(ln.strip().lstrip("- "))
    return " ".join(out)


def sm89_status(notes):
    """Heuristic availability on sm_89 from the 'Target ISA Notes' text."""
    if not notes:
        return "?"
    sms = [int(n) for n in re.findall(r"sm_(\d+)", notes)]
    if "all target architectures" in notes.lower():
        return "partial" if any(n > SM for n in sms) else "yes"
    if not sms:
        return "?"
    lo = min(sms)
    if lo > SM:
        return f"**no** (sm_{lo}+)"
    return "partial" if any(n > SM for n in sms) else "yes"


def main():
    md = fetch()
    secs = section_tree(md)
    files = assign_files(secs)
    anchor_file = {s[3]: f for s, f in zip(secs, files) if s[3]}

    img_base = URL.rsplit("/", 1)[0] + "/"

    def fetch_img(name):
        dst = CACHE / name
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(img_base + name, headers={"User-Agent": "sm89-kb/1.0"})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    dst.write_bytes(r.read())
            except OSError as e:
                print("image fetch failed:", name, e)
                return False
        out = OUT / name
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(dst, out)
        return True

    def relink(line, here):
        up = "../" * (len(pathlib.Path(here).parts) - 1)

        def img(m):
            name = m.group(2)
            # Hopper/Blackwell-only families (wgmma, tcgen05) keep remote images to save ~25MB.
            if not here.startswith(REMOTE_IMG) and fetch_img(name):
                return f"![{m.group(1)}]({up}{name})"
            return f"![{m.group(1)}]({img_base}{name})"
        line = re.sub(r"!\[([^\]]*)\]\((_images/[^)\s]+)\)", img, line)

        def sub(m):
            a = m.group(2)
            target = anchor_file.get(a)
            if target is None:
                return f"[{m.group(1)}]({URL}#{a})"
            return f"[{m.group(1)}]({up}{target}#{a})" if target != here else f"[{m.group(1)}](#{a})"
        return re.sub(r"\[([^\]]*)\]\(#([^)\s]+)\)", sub, line)

    shutil.rmtree(OUT, ignore_errors=True)
    buf = {}
    for (lvl, num, title, anchor, body), path in zip(secs, files):
        b = buf.setdefault(path, [])
        if not b:
            b.append(f"<!-- Generated from {URL} by tools/build_ptx.py; do not edit. -->\n")
            base_lvl = lvl
            buf[path + "#lvl"] = base_lvl
        depth = max(1, lvl - buf[path + "#lvl"] + 1)
        if anchor:
            b.append(f'<a id="{anchor}"></a>')
        b.append(f"{'#' * depth} {num} {title}".replace("  ", " "))
        b.extend(relink(l, path) for l in body)
    for path, lines in buf.items():
        if path.endswith("#lvl"):
            continue
        p = OUT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(lines) + "\n")

    # Per-instruction index (level-4 sections under 9.7).
    rows = []
    for (lvl, num, title, anchor, body), path in zip(secs, files):
        parts = [p for p in num.split(".") if p]
        if len(parts) == 3 and parts[:2] == ["9", "7"]:
            rows.append(f"\n## {num} {title}\n\n| section | instruction | sm_89 | Target ISA notes |\n|---|---|---|---|")
        if len(parts) == 4 and parts[:2] == ["9", "7"]:
            # Notes may live in this section or in its subsections.
            sub = [s for s in secs if s[1].startswith(num)]
            notes = " ".join(isa_notes(s[4], "Target ISA Notes") for s in sub).strip()
            short = notes if len(notes) < 220 else notes[:217] + "..."
            name = title.split(":", 1)[-1].strip()
            rows.append(f"| {num} | [{name}]({path}) | {sm89_status(notes)} | {short.replace('|', '/')} |")
        if len(parts) >= 5 and parts[:2] == ["9", "7"] and "`" in title:
            sub = [s for s in secs if s[1].startswith(num)]
            notes = " ".join(isa_notes(s[4], "Target ISA Notes") for s in sub).strip()
            if notes:
                short = notes if len(notes) < 220 else notes[:217] + "..."
                name = title.split(":", 1)[-1].strip()
                rows.append(f"| {'&nbsp;&nbsp;' * (len(parts) - 4)}{num} | ↳ [{name}]({path}#{anchor}) | {sm89_status(notes)} | "
                            f"{short.replace('|', '/')} |")
    (OUT / "INDEX.md").write_text(
        "# PTX ISA instruction index (sm_89 view)\n\n"
        f"Generated from <{URL}>. The **sm_89** column is a heuristic over each section's "
        "\"Target ISA Notes\": `yes` = no requirement above sm_89, `partial` = some variants need a newer "
        "arch (read the notes), `no` = whole instruction needs a newer arch. "
        "Remember the PTX `.version` also matters (sm_89 needs >= 7.8; FP8 `cvt` needs 8.1, FP8 `mma` 8.4).\n\n"
        "Spot-checked with real `ptxas -arch=sm_89`: the `no_*` probes in "
        "[../verify/RESULTS.md](../verify/RESULTS.md) (stmatrix, elect.sync, setmaxnreg, mapa, cp.async.bulk, "
        "wgmma, griddepcontrol, redux.f32) are all rejected for architecture reasons, and ~120 `yes` "
        "instructions compile in the other probes.\n\n"
        "Non-instruction chapters: " + ", ".join(
            f"[{p[:-3]}]({p})" for p in sorted({f for f in files if "/" not in f})) + "\n"
        + "\n".join(rows) + "\n")
    print(f"{len(secs)} sections -> {len({f for f in files})} files")


if __name__ == "__main__":
    main()

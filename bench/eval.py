"""Score a candidate compile.py: correctness gate first, then speed.

Usage:
    python bench/eval.py path/to/candidate/compile.py [--json out.json]

Scoring (per the hackathon rules in AGENTS.md):
  1. Rule check: the candidate must not call emmy's renderer/compile, nvcc, or any
     other compiler. Violation -> FAIL (score 0). Static scan only; judges read code.
  2. Correctness gate: ALL problems must PASS via task/submit.py. Any FAIL, crash,
     or missing PASS line -> score 0. Incorrect solutions automatically fail.
  3. Speed: geometric mean of the per-problem runtime (us) reported by submit.py.
     Lower is better. Only computed when the gate passes.

emmy compile / nvcc may be used for TESTING and BENCHMARKING but not inside the
candidate; this script never runs them on the candidate's behalf.
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TASK = os.path.join(ROOT, "task")
PYTHON = os.path.join(ROOT, ".venv", "bin", "python")
PROBLEMS = [
    "p00_scalar_add", "p01_vector_add", "p02_scale_shift", "p03_relu_mul",
    "r01_array_sum", "r02_big_sum", "r03_mean", "r04_row_sum",
    "m01_matmul_512", "m02_matmul_rect",
    "f01_rmsnorm", "f02_row_softmax", "f03_l2norm",
    "a01_attention", "a02_attention_128",
]
# Calls that would mean the candidate lowers via an existing compiler. We match
# *invocations*, not prose: "let ptxas allocate" in a comment is fine, running it is not.
FORBIDDEN_PATTERNS = [
    r"render_kernelop",                                # emmy's renderer, any use
    r"\bemmy\.compile\s*\(",                           # emmy compile as a python call
    r"(subprocess\.(?:run|call|Popen|check_output|check_call)|os\.(?:system|popen|exec\w*|spawn\w*))\s*\([^)]*\b(?:nvcc|ptxas|nvrtc|clang|emmy)\b",
    r"\bos\.system\b[^)]*\b(?:nvcc|ptxas|nvrtc)\b",
]


def rule_check(path):
    src = open(path, encoding="utf-8").read()
    # Strip comment tails (prose like "let ptxas allocate" is fine; calls are not).
    # Naive per-line strip: strings containing '#' are rare in this threat model.
    code = "\n".join(re.sub(r"#[^\n]*", "", line) for line in src.splitlines())
    hits = [p for p in FORBIDDEN_PATTERNS if re.search(p, code)]
    return hits


PASS_RE = re.compile(r"PASS\b.*\(([\d.]+)\s*us\)")


def run_problem(candidate, problem, extra_env=None):
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    if extra_env:
        env.update(extra_env)
    try:
        r = subprocess.run(
            [PYTHON, "submit.py", problem, "--compiler", candidate],
            cwd=TASK, capture_output=True, text=True, timeout=600, env=env,
        )
    except subprocess.TimeoutExpired:
        return {"problem": problem, "ok": False, "reason": "timeout"}
    out = r.stdout + r.stderr
    m = PASS_RE.search(out)
    if r.returncode == 0 and m and "FAIL" not in out:
        return {"problem": problem, "ok": True, "us": float(m.group(1))}
    tail = " | ".join(out.strip().splitlines()[-3:])[:300]
    return {"problem": problem, "ok": False, "reason": tail or f"rc={r.returncode}"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    ap.add_argument("--json", help="write full result to this path")
    args = ap.parse_args()
    cand = os.path.abspath(args.candidate)

    hits = rule_check(cand)
    results = []
    if hits:
        score = {"gate": "FAIL", "reason": f"forbidden pattern(s): {hits}", "score": 0}
    else:
        for p in PROBLEMS:
            res = run_problem(cand, p)
            results.append(res)
            status = "PASS" if res["ok"] else "FAIL"
            detail = f"{res['us']:.2f} us" if res["ok"] else res["reason"]
            print(f"{status} {p}: {detail}", flush=True)
        failed = [r["problem"] for r in results if not r["ok"]]
        if failed:
            score = {"gate": "FAIL", "reason": f"failed: {failed}", "score": 0}
        else:
            gm = math.exp(sum(math.log(r["us"]) for r in results) / len(results))
            score = {"gate": "PASS", "geomean_us": round(gm, 3), "score": round(1e6 / gm, 3)}
    out = {"candidate": cand, **score, "problems": results}
    print(json.dumps({k: v for k, v in out.items() if k != "problems"}, indent=1))
    if args.json:
        json.dump(out, open(args.json, "w"), indent=1)
    return 0 if score["gate"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

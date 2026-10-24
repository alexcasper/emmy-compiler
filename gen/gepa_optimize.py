"""GEPA-optimized generator for candidate IR->PTX compilers (branch `gepa`).

GEPA evolves the instructions of a DSPy codegen module whose output — a complete
compile.py — is executed for real and scored by the shared bench harness:

    metric(candidate) = 0                          if rule check or any problem fails
                      = 1e6 / geomean_runtime_us    otherwise (all 15 must PASS)

Candidates must not call emmy's renderer, `emmy compile`, nvcc, ptxas, nvrtc, or any
other compiler. `Graph.from_dict` from emmy-ml is the only permitted emmy usage.
The remote runner (submit.py's) is used to TEST; it never builds the candidate.
"""
import argparse
import importlib.util
import json
import math
import os
import re
import sys

_harness = os.path.join(os.path.dirname(__file__), "..", "bench", "eval.py")
_spec = importlib.util.spec_from_file_location("bench_eval", _harness)
assert _spec and _spec.loader
bench = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bench)

import dspy  # noqa: E402

RULES = """Write a complete, self-contained Python 3 file: a translator from the Emmy
Kernel IR json (argv[1]) to PTX text on stdout. Constraints:
- Start PTX with .version 8.0 / .target sm_89 / .address_size 64; pure ASCII.
- Entry name = the kernel's "name" in the IR. Params = arg_order from meta.json,
  .u64 pointers for buffers.
- You MAY `from emmy.compiler.graph import Graph` and call Graph.from_dict to load
  the IR. You may NOT call emmy's renderer, `emmy compile`, nvcc, ptxas, nvrtc,
  clang, or any subprocess that compiles. Violations are an automatic zero.
- Guard threads with N from the Tile; the guard is not in the IR.
- Fresh virtual registers; declare counts as highest index + 1.
- f32 hex literals like 0f3F800000 are big-endian (struct.pack(">f", x)).
- Static shapes only. Correctness is a hard gate; speed ranks the survivors.
Write only the file contents, no markdown fences, no commentary."""


class GenerateCompiler(dspy.Signature):
    """Write an improved compile.py given the IR reference and prior feedback."""
    ir_reference: str = dspy.InputField(
        desc="Structure notes of the Emmy IR and this target's IR/meta dump."
    )
    previous: str = dspy.InputField(
        desc="Prior candidate's real execution result: score or failure tails."
    )
    compiler_code: str = dspy.OutputField(desc="The complete Python file, nothing else.")


class CandidateGen(dspy.Module):
    """The program whose instructions GEPA evolves."""

    def __init__(self):
        self.gen = dspy.Predict(GenerateCompiler)

    def forward(self, ir_reference, previous):
        return self.gen(ir_reference=ir_reference, previous=previous)


def build_ir_reference(problem: str) -> str:
    root = os.path.join(os.path.dirname(__file__), "..", "task", "problems", problem)
    ir_txt = next(f for f in os.listdir(root) if f.endswith(".ir.txt"))
    meta = open(os.path.join(root, "meta.json")).read()
    return open(os.path.join(root, ir_txt), errors="ignore").read()[:4000] + "\n\n" + meta


def score_candidate(path: str) -> float:
    """The GEPA metric: execution-based, hard correctness gate, speed above it."""
    if bench.rule_check(path):
        return 0.0
    smoke = bench.run_problem(path, "p00_scalar_add")
    if not smoke["ok"]:
        return 0.0
    results = [smoke] + [bench.run_problem(path, p) for p in bench.PROBLEMS[1:]]
    if any(not r["ok"] for r in results):
        return 0.0
    gm = math.exp(sum(math.log(r["us"]) for r in results) / len(results))
    return 1e6 / gm


def metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """GEPA metric (5-arg form required by dspy 3.4): execution-based, hard
    correctness gate, speed above it."""
    code = (pred.compiler_code or "").strip()
    m = re.match(r"^```(?:python)?\s*(.*?)\s*```$", code, re.S)
    if m:
        code = m.group(1)
    if len(code) < 200 or ("def main" not in code and "sys.argv" not in code):
        return 0.0  # not a plausible translator; don't burn a runner slot on it
    outdir = os.path.join(os.path.dirname(__file__), "out")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "gepa_candidate_last.py")
    open(path, "w").write(code)
    return score_candidate(path)


def connect_lm():
    base = os.environ.get("GEPA_LM_BASE_URL")
    model = os.environ.get("GEPA_LM_MODEL")
    if not (base and model):
        sys.exit(
            "No LM endpoint configured. Set GEPA_LM_BASE_URL and GEPA_LM_MODEL "
            "(OpenAI-compatible), then re-run. Nothing was optimized."
        )
    lm = dspy.LM(
        f"openai/{model}",
        api_base=base,
        api_key=os.environ.get("GEPA_LM_API_KEY", "dummy"),
        temperature=0.2,
        max_tokens=8000,
    )
    dspy.configure(lm=lm)
    return lm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=int, default=30, help="GEPA optimization budget")
    args = ap.parse_args()

    connect_lm()
    trainset = [
        dspy.Example(ir_reference=build_ir_reference(p), previous="none yet").with_inputs(
            "ir_reference", "previous"
        )
        for p in ("p00_scalar_add", "r01_array_sum", "m01_matmul_512", "f01_rmsnorm")
    ]
    # dspy 3.4 requires an explicit reflection LM (same local model here).
    reflection = dspy.LM(
        f"openai/{os.environ['GEPA_LM_MODEL']}",
        api_base=os.environ["GEPA_LM_BASE_URL"],
        api_key=os.environ.get("GEPA_LM_API_KEY", "dummy"),
        temperature=1.0,
        max_tokens=16000,
    )
    gepa_opt = dspy.GEPA(metric=metric, auto="light", reflection_lm=reflection)
    optimized = gepa_opt.compile(CandidateGen(), trainset=trainset)
    out = os.path.join(os.path.dirname(__file__), "out")
    os.makedirs(out, exist_ok=True)
    last = os.path.join(out, "gepa_candidate_last.py")
    if os.path.exists(last):
        print("Best surviving candidate:", last)
        print("Score it: ../.venv/bin/python bench/eval.py", last)
    json.dump(
        {"instructions": getattr(optimized, "instructions", "")},
        open(os.path.join(out, "gepa_best_instructions.json"), "w"),
        indent=1,
    )
    print("GEPA run complete.")


if __name__ == "__main__":
    main()

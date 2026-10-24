"""DSPy Program-of-Thought generator for candidate IR->PTX compilers (branch `pot`).

Loop per round:
  1. LM writes a complete compile.py (reads argv[1] IR json, prints PTX to stdout).
  2. Static rule check (bench.eval.FORBIDDEN) — no emmy-compile/nvcc/renderer.
  3. Execute for real: p00 first; if PASS, full 15-problem sweep via bench.eval.
  4. Feed the pass/fail + error tails back as `previous` for the next round.

Only `Graph.from_dict` from emmy is permitted inside candidates; the harness itself
uses the remote runner (same one submit.py uses). No compiler ever builds a candidate.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "bench"))
import importlib.util  # noqa: E402
import re  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "bench_eval", os.path.join(os.path.dirname(__file__), "..", "bench", "eval.py")
)
assert _spec and _spec.loader
bench = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bench)  # shared harness: rule_check, run_problem, PROBLEMS

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
- Use fresh virtual registers; declare counts as highest index + 1.
- f32 hex literals like 0f3F800000 are big-endian (struct.pack(">f", x)).
- Static shapes only. Correctness is a hard gate; speed ranks the survivors.
Write only the file contents, no markdown fences, no commentary."""


class GenerateCompiler(dspy.Signature):
    """Generate an improved compile.py from the previous round's execution feedback."""
    ir_reference: str = (
        "Structure notes of the Emmy IR and an example problem (p00) to target."
    )
    rules: str = "Hard constraints for the generated translator."
    previous: str = "Previous candidate's execution result: score line and failure tails."
    compiler_code: str = "The complete Python file, nothing else."


class PoTCompilerGen(dspy.Module):
    def __init__(self):
        self.gen = dspy.Predict(GenerateCompiler)

    def forward(self, ir_reference, previous="none yet — first round"):
        return self.gen(ir_reference=ir_reference, rules=RULES, previous=previous)


def connect_lm():
    base = os.environ.get("POT_LM_BASE_URL")
    model = os.environ.get("POT_LM_MODEL")
    if not (base and model):
        sys.exit(
            "No LM endpoint configured. Set POT_LM_BASE_URL and POT_LM_MODEL "
            "(OpenAI-compatible), then re-run. Nothing was generated."
        )
    lm = dspy.LM(
        f"openai/{model}",
        api_base=base,
        api_key=os.environ.get("POT_LM_API_KEY", "dummy"),
        temperature=0.2,
        max_tokens=8000,
    )
    dspy.configure(lm=lm)
    return lm


def ir_reference() -> str:
    """Small structural summary of the IR + meta so the LM knows the input shape."""
    root = os.path.join(os.path.dirname(__file__), "..", "task", "problems")
    parts = []
    p00 = os.path.join(root, "p00_scalar_add")
    parts.append(open(os.path.join(p00, "k_add_pointwise.ir.txt")).read()[:4000])
    parts.append(open(os.path.join(p00, "meta.json")).read())
    parts.append(
        "All 15 problem dirs (same layout): " + ", ".join(bench.PROBLEMS)
    )
    return "\n\n".join(parts)[:8000]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "out"))
    args = ap.parse_args()

    connect_lm()
    os.makedirs(args.out, exist_ok=True)
    pot = PoTCompilerGen()
    ref = ir_reference()
    previous = "none yet — first round"

    for rnd in range(1, args.rounds + 1):
        pred = pot(ir_reference=ref, previous=previous)
        code = pred.compiler_code.strip()
        m = re.match(r"^```(?:python)?\s*(.*?)\s*```$", code, re.S)
        if m:
            code = m.group(1)
        path = os.path.join(args.out, f"pot_candidate_r{rnd}.py")
        open(path, "w").write(code)
        print(f"[round {rnd}] wrote {path} ({len(code)} chars)")

        if bench.rule_check(path):
            previous = f"REJECTED by static rule check: {bench.rule_check(path)}"
            print(f"[round {rnd}] {previous}")
            continue
        # execute for real: smoke-test p00, then the full gate
        smoke = bench.run_problem(path, "p00_scalar_add")
        if not smoke["ok"]:
            previous = f"p00 FAILED: {smoke['reason']}"
            print(f"[round {rnd}] {previous}")
            continue
        results = [bench.run_problem(path, p) for p in bench.PROBLEMS[1:]]
        failed = [r for r in results if not r["ok"]]
        import json, math
        if failed:
            previous = "Failures: " + json.dumps(
                [{r["problem"]: r["reason"]} for r in failed]
            )[:2000]
            print(f"[round {rnd}] {len(failed)} failed")
            continue
        times = [smoke["us"]] + [r["us"] for r in results]
        gm = math.exp(sum(math.log(t) for t in times) / len(times))
        print(f"[round {rnd}] ALL 15 PASS, geomean {gm:.2f} us")
        previous = f"ALL PASS, geomean {gm:.2f} us. Try to beat it."


if __name__ == "__main__":
    main()

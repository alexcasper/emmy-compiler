"""GEPA optimizer for OUR kernels' PTX lowering knobs (branch `gepa`).

The compiler (compile.py at repo root) exposes a small tuning surface via the
EMMY_TUNING env var: read-only loads through the `.nc` path, and approx vs
correctly-rounded div/sqrt/rcp. GEPA evolves the instructions of a DSPy module
that PROPOSES a tuning config; every proposal is executed for real through the
shared bench harness on the remote runner:

    score(config) = 0                        if any subset problem fails the gate
                  = 1e6 / geomean(subset us)  otherwise

Subset: r02 (memory-bound loads), r03 (divide), m01 (matmul, cp.async),
f02 (exp/div), f03 (sqrt/rcp), a01 (attention) — every knob's blast radius.
The winning config is then validated on ALL 15 problems before we keep it.

Hard rule (AGENTS.md): emmy/nvcc may only TEST or BENCHMARK. Nothing here or in
the candidate path calls any compiler; the runner's /compile step is upstream's
own harness (the same one task/submit.py uses for every submission).

Usage:
    export GEPA_LM_BASE_URL=... GEPA_LM_MODEL=...   # OpenAI-compatible
    ../.venv/bin/python gen/gepa_optimize.py --budget 8
"""
import argparse
import importlib.util
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))


def _load(name, relpath):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, relpath))
    assert spec and spec.loader, f"cannot load {relpath}"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bench = _load("bench_eval", "bench/eval.py")       # run_problem, rule_check, PROBLEMS
emmy_compile = _load("emmy_compile", "compile.py")  # DEFAULT_TUNING, clamp_tuning

import dspy  # noqa: E402

SUBSET = ["r02_big_sum", "r03_mean", "m01_matmul_512",
          "f02_row_softmax", "f03_l2norm", "a01_attention"]
CANDIDATE = os.path.join(ROOT, "compile.py")
TRIALS = os.path.join(HERE, "out", "gepa_trials.jsonl")

KNOB_DOC = """Emmy IR->PTX compiler tuning knobs (compile.py, env EMMY_TUNING, JSON):
- nc_loads (bool, default false): route loads of buffers the kernel never writes
  through `ld.global.nc` (read-only/L1 path) instead of `ld.global`.
- div ("rn"|"approx"|"approx.ftz", default "rn"): div.rn.f32 is IEEE-correct;
  approx variants are faster, a few ulp off. Only matters where rtol allows.
- sqrt ("rn"|"approx", default "rn"): sqrt.rn.f32 vs sqrt.approx.f32.
- rcp ("rn"|"approx", default "rn"): rcp.rn.f32 vs rcp.approx.f32 (reciprocal op).
Baseline (all-default) subset runtimes in microseconds come from the bench sweep.
Correctness is a hard gate: a config that fails ANY problem scores 0, so
approximations must respect each problem's rtol/atol.
Total space: 24 configs. m01 reads only via cp.async, so nc_loads and the op
knobs do not affect it — do not spend budget re-proposing for it.
"""


class ProposeTuning(dspy.Signature):
    """Propose the next EMMY_TUNING config to test, given feedback so far."""
    context: str = dspy.InputField(desc="Knob documentation and baseline runtimes.")
    previous: str = dspy.InputField(desc="Configs already measured and their scores.")
    tuning_json: str = dspy.OutputField(
        desc='A single JSON object with keys nc_loads, div, sqrt, rcp. Nothing else.'
    )


class TuningGen(dspy.Module):
    """GEPA evolves these instructions; the output is a tuning config."""

    def __init__(self):
        self.gen = dspy.Predict(ProposeTuning)

    def forward(self, context, previous):
        return self.gen(context=context, previous=previous)


_score_cache: dict[str, float] = {}


def canonical(cfg: dict) -> str:
    return json.dumps({k: cfg[k] for k in ("nc_loads", "div", "sqrt", "rcp")},
                      sort_keys=True)


def score_config(cfg: dict, problems=SUBSET, log=True) -> float:
    key = canonical(cfg) + "|" + ",".join(problems)
    if key in _score_cache:
        return _score_cache[key]
    extra = {"EMMY_TUNING": json.dumps(cfg)}
    results = [bench.run_problem(CANDIDATE, p, extra_env=extra) for p in problems]
    score = 0.0
    if all(r["ok"] for r in results):
        gm = math.exp(sum(math.log(r["us"]) for r in results) / len(results))
        score = 1e6 / gm
    _score_cache[key] = score
    if log:
        os.makedirs(os.path.dirname(TRIALS), exist_ok=True)
        with open(TRIALS, "a") as f:
            f.write(json.dumps({
                "config": json.loads(canonical(cfg)),
                "problems": problems,
                "score": score,
                "results": [{k: r.get(k) for k in ("problem", "ok", "us", "reason")}
                            for r in results],
            }) + "\n")
    return score


def parse_config(text: str) -> dict | None:
    """Defensively extract a JSON config; clamp via the compiler's own loader."""
    m = re.search(r"\{[^{}]*\}", text or "", re.S)
    if not m:
        return None
    try:
        raw = json.loads(m.group(0))
    except ValueError:
        return None
    if not isinstance(raw, dict):
        return None
    merged = dict(emmy_compile.DEFAULT_TUNING)
    for k in emmy_compile.DEFAULT_TUNING:
        if k in raw:
            merged[k] = raw[k]
    return emmy_compile.clamp_tuning(merged)


def metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """GEPA metric (5-arg form required by dspy 3.4). Execution-based."""
    cfg = parse_config(getattr(pred, "tuning_json", ""))
    if cfg is None:
        return 0.0  # unparseable proposal: no runner time wasted
    return score_config(cfg)


def lm_from_env(tag):
    base = os.environ.get(f"{tag}_LM_BASE_URL")
    model = os.environ.get(f"{tag}_LM_MODEL")
    if not (base and model):
        sys.exit(f"No LM endpoint configured. Set {tag}_LM_BASE_URL and {tag}_LM_MODEL.")
    return dspy.LM(
        f"openai/{model}",
        api_base=base,
        api_key=os.environ.get(f"{tag}_LM_API_KEY", "dummy"),
        temperature=0.2,
        max_tokens=12000,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=int, default=8)
    args = ap.parse_args()

    lm = lm_from_env("GEPA")
    dspy.configure(lm=lm)
    reflection = lm_from_env("GEPA")
    reflection.kwargs["temperature"] = 1.0

    baseline = dict(emmy_compile.DEFAULT_TUNING)
    base_score = score_config(baseline, log=True)
    print(f"[baseline] {canonical(baseline)} subset score {base_score:.1f}", flush=True)

    trainset = [
        dspy.Example(context=KNOB_DOC + f"\nBaseline subset score: {base_score:.1f}.",
                     previous="none yet").with_inputs("context", "previous"),
        dspy.Example(context=KNOB_DOC + "\nRemember: failing ANY problem scores 0.",
                     previous="none yet").with_inputs("context", "previous"),
    ]
    # dspy 3.4: exactly one of auto / max_full_evals / max_metric_calls — we
    # drive the budget explicitly (auto="light" just picks a small one).
    gepa_opt = dspy.GEPA(metric=metric, reflection_lm=reflection,
                        max_full_evals=args.budget)
    optimized = gepa_opt.compile(TuningGen(), trainset=trainset, valset=trainset)

    # pick the best measured config from the trial log, then full-gate it
    best_cfg, best_score = baseline, base_score
    if os.path.exists(TRIALS):
        for line in open(TRIALS):
            t = json.loads(line)
            if t["score"] > best_score:
                best_cfg, best_score = t["config"], t["score"]
    full = [bench.run_problem(CANDIDATE, p, extra_env={"EMMY_TUNING": json.dumps(best_cfg)})
            for p in bench.PROBLEMS]
    failed = [r for r in full if not r["ok"]]
    gm = math.exp(sum(math.log(r["us"]) for r in full) / len(full)) if not failed else None
    report = {
        "best_config": best_cfg,
        "subset_score": best_score,
        "full_gate": "PASS" if not failed else [r["reason"] for r in failed],
        "full_geomean_us": round(gm, 3) if gm else None,
        "baseline_geomean_us": 26.808,
    }
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    json.dump(report, open(os.path.join(HERE, "out", "gepa_best.json"), "w"), indent=1)
    json.dump({"instructions": getattr(optimized, "instructions", "")},
              open(os.path.join(HERE, "out", "gepa_best_instructions.json"), "w"), indent=1)
    print(json.dumps(report, indent=1), flush=True)


if __name__ == "__main__":
    main()

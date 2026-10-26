"""GEPA round 2: search the EXPANDED EMMY_TUNING surface with the L4 lane
as the execution metric (emmy-ejb).

Candidate = a tuning config (JSON) over the compile.py knob surface. Metric =
compile + bench on the L4 via gen/l4_lane.py on a 7-problem subset (the heavy
kernels + 2 tracer variations), score = 1e6 / geomean(p50_us), 0 on any
failure. L4 noise is +-0.5%, so single passes rank configs the runner cannot.

    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \\
    GEPA_LM_BASE_URL=https://api.z.ai/api/coding/paas/v4 \\
    GEPA_LM_MODEL=glm-5.3-flash GEPA_LM_API_KEY=... \\
    .venv/bin/python gen/gepa_l4.py --budget 6

The winner is NOT merged automatically: it goes through the full 24-problem
L4 lane and the judge-runner 15/15 gate first.
"""
import argparse
import importlib.util
import json
import math
import os
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
TRIALS = os.path.join(HERE, "out", "gepa_l4_trials.jsonl")

SUBSET = ["m01_matmul_512", "a01_attention", "a02_attention_128",
          "r02_big_sum", "f02_row_softmax", "gm1_matmul_256",
          "ga1_attention_32x128"]

KNOB_DOC = """compile.py EMMY_TUNING knobs (JSON). All keys optional; omit = keep default.
Current compiler defaults: pow2_shift=true, hoist_invariants="auto", fuse_loops=true,
load_cse=true, nc_loads=false, div/sqrt/rcp="rn". Search space ~1152 configs —
propose COMBINATIONS, not single-knob flips; the space is too big for exhaustive sweep.
- pow2_shift (bool, default true): div/mod by power-of-2 constants emit
  shr/and instead of div.s32/rem.s32 (ptxas expands those into MUFU
  float-reciprocal sequences per site). L4-verified neutral-to-positive.
- hoist_invariants (true|false|"auto", default "auto"): hoist loop-invariant
  address subexpressions to preheaders. Measured on L4: huge win in kernels
  whose IR stages via cp.async (m01 440->94us), but ~8-9% REGRESSION in
  cp.async-free kernels (attention) — "auto" restricts it to cp.async kernels;
  propose true/false to re-test that boundary in combination with fuse_loops.
- fuse_loops (bool, default TRUE in this compiler): merge sibling loops with
  identical trip counts. An EARLIER implementation was falsified on hardware
  (a01 SASS 3x smaller but 68% slower — the removed loads were free L1 hits);
  the current implementation is reworked and shipped as default. Re-measure it,
  especially fused=true + load_cse=false and both-off.
- load_cse (bool, default TRUE in this compiler): one LDG for identical
  read-only loads in a straight-line body. Same history as fuse_loops.
- nc_loads (bool, default false): ld.global.nc — measured neutral, but never
  tested in combination with the loop transforms.
- div ("rn"|"approx"|"approx.ftz"), sqrt ("rn"|"approx"), rcp ("rn"|"approx"):
  rounding modes — measured neutral alone; approx trio regressed attention ~7%
  once. Respect rtol: correctness failures score 0.
Baseline (current defaults) subset p50s are in the context. Score =
1e6/geomean(us) over the subset; correctness failures score 0.
"""

_config_cache: dict = {}


def canon(tuning: dict) -> str:
    return json.dumps(tuning, sort_keys=True)


def score_config(tuning: dict) -> float:
    key = canon(tuning)
    if key in _config_cache:
        return _config_cache[key]
    tag = "g" + str(abs(hash(key)) % 10**8)
    env = dict(os.environ, EMMY_TUNING=key)
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "l4_lane.py"),
         "--problems", ",".join(SUBSET), "--reps", "60", "--tag", tag,
         "--no-variations"],
        capture_output=True, text=True, timeout=1500, env=env,
        cwd=ROOT)
    # the lane appends one line per invocation; read the last
    rows = None
    path = os.path.join(HERE, "out", "l4lane_results.jsonl")
    for line in open(path):
        rec = json.loads(line)
        if rec["tag"] == tag:
            rows = rec["rows"]
    if rows is None or any(not row.get("ok") for row in rows):
        score = 0.0
    else:
        p50s = [row["p50_us"] for row in rows]
        gm = math.exp(sum(math.log(x) for x in p50s) / len(p50s))
        score = 1e6 / gm
    with open(TRIALS, "a") as f:
        f.write(json.dumps({"config": json.loads(key), "score": score,
                            "p50s": {row["problem"]: row["p50_us"] for row in rows}
                                    if rows else {}}) + "\n")
    _config_cache[key] = score
    return score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=int, default=6)
    args = ap.parse_args()
    os.makedirs(os.path.dirname(TRIALS), exist_ok=True)
    if os.path.exists(TRIALS):
        os.rename(TRIALS, TRIALS + "." + str(len(os.listdir(os.path.dirname(TRIALS)))))

    import dspy

    lm = dspy.LM(f"openai/{os.environ['GEPA_LM_MODEL']}",
                 api_base=os.environ["GEPA_LM_BASE_URL"],
                 api_key=os.environ["GEPA_LM_API_KEY"],
                 temperature=0.2, max_tokens=16000)
    dspy.configure(lm=lm)
    reflection = dspy.LM(f"openai/{os.environ['GEPA_LM_MODEL']}",
                         api_base=os.environ["GEPA_LM_BASE_URL"],
                         api_key=os.environ["GEPA_LM_API_KEY"],
                         temperature=1.0, max_tokens=16000)

    class ProposeTuning(dspy.Signature):
        """Propose the next EMMY_TUNING config JSON to test, given feedback."""
        context: str = dspy.InputField(desc="Knob documentation and baseline.")
        previous: str = dspy.InputField(desc="Configs already measured and scores.")
        tuning_json: str = dspy.OutputField(desc="One JSON object of tuning keys. Nothing else.")

    class TuningGen(dspy.Module):
        def __init__(self):
            self.gen = dspy.Predict(ProposeTuning)

        def forward(self, context, previous):
            return self.gen(context=context, previous=previous)

    def metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
        text = getattr(pred, "tuning_json", "") or ""
        m = __import__("re").search(r"\{[^{}]*\}", text, __import__("re").S)
        if not m:
            return 0.0
        try:
            cfg = json.loads(m.group(0))
        except ValueError:
            return 0.0
        return score_config(cfg)

    base_score = score_config({})
    print(f"[baseline] score {base_score:.1f}", flush=True)

    trainset = [
        dspy.Example(context=KNOB_DOC + f"\nBaseline subset score: {base_score:.1f}.",
                     previous="none yet").with_inputs("context", "previous"),
        dspy.Example(context=KNOB_DOC + "\nCorrectness failures score 0.",
                     previous="none yet").with_inputs("context", "previous"),
    ]
    opt = dspy.GEPA(metric=metric, reflection_lm=reflection,
                    max_full_evals=args.budget,
                    skip_perfect_score=False, perfect_score=1e12)
    optimized = opt.compile(TuningGen(), trainset=trainset, valset=trainset)

    best_cfg, best_score = {}, base_score
    for line in open(TRIALS):
        t = json.loads(line)
        if t["score"] > best_score:
            best_cfg, best_score = t["config"], t["score"]
    report = {"best_config": best_cfg, "best_score": best_score,
              "baseline_score": base_score,
              "instructions": getattr(optimized, "instructions", "")}
    json.dump(report, open(os.path.join(HERE, "out", "gepa_l4_best.json"), "w"),
              indent=1)
    print(json.dumps(report, indent=1), flush=True)


if __name__ == "__main__":
    main()

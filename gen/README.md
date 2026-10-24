# Branch: `gepa` — GEPA-optimized candidate compilers

**Hard rule (AGENTS.md):** candidates must not call `emmy compile`, emmy's renderer,
`nvcc`, or any other compiler. `emmy-ml` may be used for `Graph.from_dict` only.
emmy/nvcc are allowed strictly as test/bench oracles — never to build a candidate.

## What this branch does

GEPA (genetic-pareto prompt evolution) evolves the *instructions* of a DSPy module
that writes candidate `compile.py`-style translators (IR -> PTX). Each candidate is
executed for real and scored by `bench/eval.py`:

- metric = 0 on any rule violation, any failed problem, or a crash (correctness is
  a hard gate), else `1e6 / geomean_runtime_us` across all 15 problems (speed).

GEPA keeps a Pareto frontier of instruction variants, so survivors are trade-offs
that never sacrifice correctness for speed.

## Wiring (fill in when the local model is up)

```bash
export GEPA_LM_BASE_URL="http://<host>:<port>/v1"   # OpenAI-compatible
export GEPA_LM_MODEL="<model-name>"
export GEPA_LM_API_KEY="dummy"
../.venv/bin/python gen/gepa_optimize.py --budget 30
```

- Best candidate + evolved instructions land in `gen/out/`.
- Score any candidate: `../.venv/bin/python bench/eval.py gen/out/<file>.py`

## Status

Scaffolded; optimization blocked on a reachable LM endpoint (nothing is hard-coded).

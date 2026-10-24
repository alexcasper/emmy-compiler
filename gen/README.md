# Branch: `pot` — DSPy Program-of-Thought candidate compilers

**Hard rule (AGENTS.md):** candidates must not call `emmy compile`, emmy's renderer,
`nvcc`, or any other compiler. `emmy-ml` may be used for `Graph.from_dict` only.
emmy/nvcc are allowed strictly as test/bench oracles — never to build a candidate.

## What this branch does

An LM writes candidate `compile.py`-style translators (IR -> PTX) as *programs*.
Each candidate is executed for real via `bench/eval.py` (correctness gate on all 15
problems, then speed = geomean runtime). Failure output is fed back into the next
generation round. That generate -> execute -> feedback loop is the Program-of-Thought
pattern: the LM reasons in Python code, and only code that survives execution scores.

## Wiring (fill in when the local model is up)

```bash
export POT_LM_BASE_URL="http://<host>:<port>/v1"   # OpenAI-compatible
export POT_LM_MODEL="<model-name>"
export POT_LM_API_KEY="dummy"                      # if the server needs one
../.venv/bin/python gen/pot_generate.py --rounds 3
```

- Candidate artifacts land in `gen/out/`.
- Score any candidate: `../.venv/bin/python bench/eval.py gen/out/pot_candidate.py`
- Incorrect candidates score 0 (automatic fail); speed only ranks correct ones.

## Status

Scaffolded; generation blocked on a reachable LM endpoint (nothing is hard-coded).

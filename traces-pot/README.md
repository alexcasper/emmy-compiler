# PoT lane trace — negative result (emmy-u3f)

**No passing PoT candidate exists to trace end-to-end.** The pot branch's DSPy
generator (`gen/pot_generate.py`, extracted from branch `pot`) had never been run —
its README says generation was blocked on an LM endpoint. It was run for real here:

- Endpoint: local `flint` (flint-preview, llama.cpp, single slot), dspy 3.4.1,
  `max_tokens` bumped 8000 -> 16000 for the reasoning budget.
- 2 rounds with execution feedback; both candidates fail p00 at the ptxas gate:
  - r1 (1905 chars): emits PTX but with pervasive syntax errors — `tid.x` without
    `%`, `.align(4)` inside load operands, `.entry kernel` instead of the IR's
    entry name, missing `.visible`/`ret`, unbracketed param list.
  - r2 (1507 chars): dies even earlier (`.reg` parse error).
- The best candidate (r1) is traced for the record: `pot_r1_p00_scalar_add/` —
  stage 1 (ptxas) fails on BOTH arches with the same error, so no SASS, no
  cross-ref, no divergence summary. The tracer correctly surfaces the failure.

## Conclusion

The tracer pipeline is ready for the PoT lane (it runs and reports stage-1
failures cleanly), but the lane itself has no compilable output yet. Closing a
flint-quality model into a working 15-problem translator needs either a stronger
endpoint or many more feedback rounds than a bounded run allows. Re-run
`gen/pot_generate.py` when a stronger endpoint is available, then trace with:

    for f in gen/trace_src/pot/*.ptx; do python3 tools/trace.py --ptx "$f" --out traces-pot; done

Artifacts: candidates `gen/out/pot_candidate_r{1,2}.py`, run log `gen/pot_run.log`,
source PTX `gen/trace_src/pot/`.

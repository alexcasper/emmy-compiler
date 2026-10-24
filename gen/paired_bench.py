"""Paired A/B benchmark of EMMY_TUNING configs — medians over interleaved reps.

The GEPA run showed single measurements are noise-dominated (identical configs
scoring 6% apart). This script measures each config on the same problems,
interleaved (A,B,C,A,B,C,...) so runner drift hits all configs equally, and
reports per-problem medians + geomean-of-medians. Correctness gate per run.

Usage: ../.venv/bin/python gen/paired_bench.py [reps]
"""
import importlib.util
import json
import math
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
spec = importlib.util.spec_from_file_location("bench_eval", os.path.join(ROOT, "bench", "eval.py"))
assert spec and spec.loader
bench = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bench)

CANDIDATE = os.path.join(ROOT, "compile.py")
PROBLEMS = ["r02_big_sum", "r03_mean", "f02_row_softmax", "f03_l2norm", "a01_attention"]
CONFIGS = {
    "A_default": {"nc_loads": False, "div": "rn", "sqrt": "rn", "rcp": "rn"},
    "B_nc": {"nc_loads": True, "div": "rn", "sqrt": "rn", "rcp": "rn"},
    "C_nc_approx": {"nc_loads": True, "div": "approx", "sqrt": "approx", "rcp": "approx"},
}


def main():
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    results = {(c, p): [] for c in CONFIGS for p in PROBLEMS}
    fails = []
    for rep in range(reps):
        for cname, cfg in CONFIGS.items():
            for p in PROBLEMS:
                r = bench.run_problem(CANDIDATE, p, extra_env={"EMMY_TUNING": json.dumps(cfg)})
                if r["ok"]:
                    results[(cname, p)].append(r["us"])
                else:
                    fails.append((cname, p, rep, r["reason"]))
                print(f"rep{rep} {cname:12s} {p:18s} "
                      f"{'%8.2f us' % r['us'] if r['ok'] else 'FAIL: ' + r['reason'][:60]}",
                      flush=True)
    print("\n=== medians over", reps, "interleaved reps ===")
    table = {}
    for cname in CONFIGS:
        row = {}
        for p in PROBLEMS:
            vals = results[(cname, p)]
            if vals:
                row[p] = statistics.median(vals)
        if len(row) == len(PROBLEMS):
            row["GEOMEAN"] = math.exp(sum(math.log(v) for v in row.values()) / len(row))
        table[cname] = row
        print(f"\n{cname}:")
        for k, v in row.items():
            print(f"  {k:18s} {v:8.2f} us")
    print("\nfails:", json.dumps(fails, indent=1) if fails else "none")
    json.dump({"medians": table,
               "raw": {f"{c}|{p}": v for (c, p), v in results.items()},
               "fails": fails},
              open(os.path.join(HERE, "out", "paired_bench.json"), "w"), indent=1)


if __name__ == "__main__":
    main()

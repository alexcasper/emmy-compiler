"""Timing-only PTX/cubin runner for the sm_120 A/B (Blackwell box).
No torch: inputs are seeded cupy randoms (timing-only protocol, as used for
a02 in bench/PAIRED_BASELINE.md). Usage: python3 l4_bench_t.py BIN META ITERS
"""
import json, statistics, sys
import numpy as np
import cupy as cp

bin_path, meta_path = sys.argv[1], sys.argv[2]
iters = int(sys.argv[3]) if len(sys.argv) > 3 else 200
meta = json.load(open(meta_path))
k = meta["kernels"][0]

cp.random.seed(1234)
bufs = {}
for a in k["args"]:
    n = int(np.prod(a["shape"])) if a["shape"] else 1
    bufs[a["name"]] = (cp.random.rand(n).astype(cp.float32) + 0.5) if not a.get("output") \
                      else cp.zeros(n, dtype=cp.float32)
launch = [bufs[n] for n in k["arg_order"]]

mod = cp.cuda.function.Module()
mod.load(open(bin_path, "rb").read())
fn = mod.get_function(k["entry"])
gp, bp, smem = tuple(k["grid"]), tuple(k["block"]), k["smem_bytes"]
if smem > 48 * 1024:
    from cupy.cuda import driver
    driver.funcSetAttribute(fn.ptr, 8, smem)

for _ in range(20):
    fn(gp, bp, launch, shared_mem=smem)
cp.cuda.Device().synchronize()

times = []
for _ in range(iters):
    s, e = cp.cuda.Event(), cp.cuda.Event()
    s.record()
    fn(gp, bp, launch, shared_mem=smem)
    e.record()
    e.synchronize()
    times.append(cp.cuda.get_elapsed_time(s, e) * 1000)
times.sort()
print(f"p50={statistics.median(times):.2f} min={times[0]:.2f} p90={times[(iters*9)//10]:.2f}")

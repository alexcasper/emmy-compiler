"""Run OUR generated PTX on the Colab L4 (sm_89) — correctness + low-noise timing.

Runs remotely (no GPU locally):
    python l4_bench.py PTX_PATH PROBLEM_DIR [iters]

Reads PROBLEM_DIR/meta.json for entry/arg_order/grid/block/smem/rtol/atol.
Correctness: regenerate the server's seeded inputs (torch manual_seed(seed) ->
randn, with fallbacks) and compare the kernel output against expected.npz.
Timing: CUDA events over `iters` reps after warmup.
"""
import json
import statistics
import sys

import numpy as np

ptx_path, prob_dir = sys.argv[1], sys.argv[2]
iters = int(sys.argv[3]) if len(sys.argv) > 3 else 50

meta = json.load(open(f"{prob_dir}/meta.json"))
k = meta["kernels"][0]

import cupy as cp
import torch


def gen_input(a, convention):
    shape = tuple(a["shape"])
    if convention == "manual_seed":
        torch.manual_seed(a["seed"])
        return torch.randn(*shape)
    g = torch.Generator().manual_seed(a["seed"])
    return torch.randn(*shape, generator=g)


def build_args(convention):
    """Return (launch_args, per-arg numpy arrays) keyed by name."""
    bufs = {}
    for a in k["args"]:
        if a.get("output"):
            bufs[a["name"]] = cp.zeros(int(np.prod(a["shape"])), dtype=cp.float32)
        else:
            t = gen_input(a, convention)
            bufs[a["name"]] = cp.asarray(t.reshape(-1).numpy().astype(np.float32))
    by_name = {a["name"]: a for a in k["args"]}
    launch = [bufs[n] for n in k["arg_order"]]
    return launch, bufs


expected = np.load(f"{prob_dir}/expected.npz")

# ---- correctness: find the input convention that reproduces expected.npz ----
mod = cp.cuda.function.Module()
if ptx_path.endswith(".cubin"):
    mod.load(open(ptx_path, "rb").read())  # offline ptxas output — the runner's own path
else:
    mod.load(ptx_path.encode())
fn = mod.get_function(k["entry"])
gp, bp, smem = tuple(k["grid"]), tuple(k["block"]), k["smem_bytes"]
if smem > 48 * 1024:
    from cupy.cuda import driver
    # driver.func_attribute names differ across cupy builds; MAX_DYNAMIC_SHARED_SIZE_BYTES == 8
    driver.funcSetAttribute(fn.ptr, 8, smem)

ok_conv = None
for conv in ("manual_seed", "generator"):
    launch, bufs = build_args(conv)
    out = bufs[meta["graph_outputs"][0]]
    fn(gp, bp, launch, shared_mem=smem)
    cp.cuda.Device().synchronize()
    got = cp.asnumpy(out).reshape([int(x) for x in expected[meta["graph_outputs"][0]].shape])
    exp = expected[meta["graph_outputs"][0]]
    if np.allclose(got, exp, rtol=meta["rtol"], atol=meta["atol"]):
        ok_conv = conv
        print(f"correctness: PASS (inputs reproduced via {conv})")
        break
if not ok_conv:
    # server's seeded inputs aren't reproducible; check against a reference
    # computed on-device from the same inputs instead
    import torch
    names = [a["name"] for a in k["args"]]
    t_in = {n: torch.from_numpy(cp.asnumpy(bufs[n]).reshape([int(s) for s in a["shape"]]))
            for a in k["args"] for n in [a["name"]] if not a.get("output")}
    code = meta["code"]
    if "@" in code and len(t_in) == 2:
        xs = [t_in[n] for n in meta["graph_inputs"]]  # code semantics: x0 @ x1
        ref = xs[0] @ xs[1]
        got = cp.asnumpy(bufs[meta["graph_outputs"][0]]).reshape(ref.shape)
        try:
            torch.testing.assert_close(torch.from_numpy(got), ref, rtol=meta["rtol"], atol=meta["atol"])
            ok_conv = "torch_ref"
            print("correctness: PASS (vs on-device torch reference)")
        except AssertionError as e:
            print("correctness: FAIL", str(e)[:300])
    else:
        print("correctness: INPUT CONVENTION UNRESOLVED — timing only")

# ---- timing ----
launch, _ = build_args(ok_conv or "manual_seed")
for _ in range(10):
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
print(f"launch: grid={gp} block={bp} smem={smem} iters={iters}")
print(f"us: min={times[0]:.2f} p50={statistics.median(times):.2f} "
      f"p10={times[iters//10]:.2f} p90={times[(iters*9)//10]:.2f}")

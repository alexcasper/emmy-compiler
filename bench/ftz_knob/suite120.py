import cupy as cp, glob, json, os, re, sys
mf = json.load(open("manifest120.json"))
metas = json.load(open("rkmust.json"))   # rk cubin -> {entry,grid,block,smem}
out_rows = []
def bench(fn, grid, block, smem, iters=40):
    out = cp.zeros(4, dtype=cp.uint64)
    times = []
    for _ in range(iters):
        out[:] = 0
        fn(grid, block, [out], shared_mem=smem)
        cp.cuda.Device().synchronize()
        times.append(int(out[1]) - int(out[0]))
    times.sort()
    return times[len(times)//2], times[0]
for f in sorted(glob.glob("lat120_*.cubin")):
    mod = cp.cuda.function.Module(); mod.load(open(f, "rb").read())
    fn = mod.get_function(mf[f])
    p50, mn = bench(fn, (1,), (256,), 0)
    print(f"{f[:-6]:<16} p50={p50} min={mn}", flush=True)
dbuf = cp.zeros(64*1024*1024, dtype=cp.float32)  # 256MB dummy for all kernel outputs
for f in sorted(glob.glob("rk_*.cubin")):
    k = metas[f]
    mod = cp.cuda.function.Module(); mod.load(open(f, "rb").read())
    fn = mod.get_function(k["entry"])
    grid, block, smem = tuple(k["grid"]), tuple(k["block"]), k["smem_bytes"]
    if smem > 48*1024:
        from cupy.cuda import driver
        driver.funcSetAttribute(fn.ptr, 8, smem)
    args = [dbuf] * k["nargs"]
    for _ in range(10):
        fn(grid, block, args, shared_mem=smem)
    cp.cuda.Device().synchronize()
    times = []
    for _ in range(60):
        s_ev, e_ev = cp.cuda.Event(), cp.cuda.Event()
        s_ev.record()
        fn(grid, block, args, shared_mem=smem)
        e_ev.record()
        e_ev.synchronize()
        times.append(cp.cuda.get_elapsed_time(s_ev, e_ev) * 1000)
    times.sort()
    print(f"{f[:-6]:<16} p50={times[len(times)//2]:.2f}us min={times[0]:.2f}", flush=True)

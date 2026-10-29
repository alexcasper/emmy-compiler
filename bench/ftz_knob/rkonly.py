import cupy as cp, glob, json
metas = json.load(open("manifest120.json"))
rkm = json.load(open("rkmust.json"))
metas = {**metas}
dbuf = cp.zeros(64*1024*1024, dtype=cp.float32)  # 256MB dummy for all kernel outputs
for f in sorted(glob.glob("rk_*.cubin")):
    k = dict(rkm[f]); k["entry"] = metas[f]
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

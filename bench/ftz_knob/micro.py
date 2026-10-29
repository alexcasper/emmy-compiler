import cupy as cp, sys, json
name = sys.argv[1]; iters = int(sys.argv[2]) if len(sys.argv) > 2 else 50
mf = sys.argv[3] if len(sys.argv) > 3 else "manifest.json"
entry = json.load(open(mf))[name.split("/")[-1]]
out = cp.zeros(4, dtype=cp.uint64)
mod = cp.cuda.function.Module()
mod.load(open(name, "rb").read())
fn = mod.get_function(entry)
res = []
for _ in range(iters):
    out[:] = 0
    fn((1,), (256,), [out], shared_mem=0)
    cp.cuda.Device().synchronize()
    res.append(int(out[1]) - int(out[0]))
res.sort()
print(f"cycles p50={res[len(res)//2]} min={res[0]} p90={res[int(len(res)*0.9)]}")

"""L4 fast lane: bench a candidate compiler on the Colab L4 (sm_89) end to end.

    .venv/bin/python gen/l4_lane.py [--candidate compile.py] [--reps 100]
                                    [--no-variations] [--session emmy-bench]

Pipeline: compile every problem locally (candidate), upload PTX + meta +
expected, assemble on the L4 VM (ptxas 13.0), run gen/l4_bench.py remotely
(correctness vs expected.npz / on-device torch ref + CUDA-event timing),
print a per-problem table. The judge runner stays the final gate; this lane
is for search iterations and regression checks (+-0.5% timing noise).

Results are appended to gen/out/l4lane_results.jsonl.
"""
import argparse
import glob
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
COLAB = os.path.expanduser("~/.local/bin/colab")
ENV = {"SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
       "REQUESTS_CA_BUNDLE": "/etc/ssl/certs/ca-certificates.crt",
       "PATH": os.environ["PATH"]}
REMOTE_DIR = "/content/emmy"


def sh(cmd, timeout=300, **kw):
    return subprocess.run(cmd, capture_output=True, text=True,
                          timeout=timeout, env=ENV, **kw)


def ensure_session(name):
    r = sh([COLAB, "status", "-s", name], timeout=60)
    if "Status: IDLE" in r.stdout or "Status: RUNNING" in r.stdout or name in r.stdout and "not found" not in r.stdout:
        if "not found" not in r.stdout:
            return
    print(f"[lane] creating session {name}...")
    sh([COLAB, "new", "-s", name, "--gpu", "L4"], timeout=240)
    import time
    time.sleep(45)


def upload(session, local, remote):
    r = sh([COLAB, "upload", "-s", session, local, remote], timeout=120)
    if "Uploaded" not in r.stdout:
        raise RuntimeError(f"upload failed: {local}\n{r.stdout[-200:]}{r.stderr[-200:]}")


def exec_remote(session, code, timeout=500):
    r = sh([COLAB, "exec", "-s", session], input=code, timeout=timeout)
    if "Connection was lost" in r.stdout:
        raise RuntimeError("colab exec lost connection (retry once)")
    return r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", default=os.path.join(ROOT, "compile.py"))
    ap.add_argument("--reps", type=int, default=100)
    ap.add_argument("--session", default="emmy-bench")
    ap.add_argument("--no-variations", action="store_true")
    ap.add_argument("--problems", default="",
                    help="comma-separated problem dir names to restrict to")
    ap.add_argument("--tag", default="run")
    args = ap.parse_args()

    prob_dirs = sorted(glob.glob(os.path.join(ROOT, "task/problems/*")))
    if not args.no_variations:
        prob_dirs += sorted(glob.glob(os.path.join(ROOT, "gen/var_problems/*")))
    prob_dirs = [d for d in prob_dirs if os.path.isdir(d)]
    if args.problems:
        want = {p.strip() for p in args.problems.split(",") if p.strip()}
        prob_dirs = [d for d in prob_dirs if os.path.basename(d) in want]

    # 1. compile locally
    jobs = []
    for d in prob_dirs:
        pid = os.path.basename(d)
        ir = glob.glob(os.path.join(d, "*.ir.json"))[0]
        ptx = os.path.join("/tmp/l4lane", f"{args.tag}_{pid}.ptx")
        os.makedirs(os.path.dirname(ptx), exist_ok=True)
        r = subprocess.run([sys.executable, args.candidate, ir],
                           capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            print(f"COMPILE FAIL {pid}: {r.stderr[-200:]}")
            continue
        open(ptx, "w").write(r.stdout)
        jobs.append((pid, ptx, d))
    print(f"[lane] compiled {len(jobs)}/{len(prob_dirs)} problems")

    # 2. ensure session + stage
    ensure_session(args.session)
    exec_remote(args.session, f"import os; os.makedirs('{REMOTE_DIR}', exist_ok=True)")
    upload(args.session, os.path.join(HERE, "l4_bench.py"), f"{REMOTE_DIR}/l4_bench.py")
    for pid, ptx, d in jobs:
        upload(args.session, ptx, f"{REMOTE_DIR}/{args.tag}_{pid}.ptx")
        upload(args.session, os.path.join(d, "meta.json"), f"{REMOTE_DIR}/{args.tag}_{pid}_meta.json")
        exp = os.path.join(d, "expected.npz")
        if os.path.exists(exp):
            upload(args.session, exp, f"{REMOTE_DIR}/{args.tag}_{pid}_expected.npz")
    print(f"[lane] staged {len(jobs)} problems")

    # 3. bench remotely (plain string + token replacement: remote braces must
    # not collide with local f-string interpolation)
    code = """
import subprocess, re, json, os, shutil
tag = '@TAG@'
out = []
for f in sorted(os.listdir('@REMOTE@')):
    if not (f.startswith(tag + '_') and f.endswith('.ptx')):
        continue
    pid = f[len(tag)+1:-4]
    ptx = '@REMOTE@/' + f
    mdir = '@REMOTE@/v_' + pid
    os.makedirs(mdir, exist_ok=True)
    shutil.copy('@REMOTE@/' + tag + '_' + pid + '_meta.json', mdir + '/meta.json')
    exp = '@REMOTE@/' + tag + '_' + pid + '_expected.npz'
    if os.path.exists(exp):
        shutil.copy(exp, mdir + '/expected.npz')
    base = ptx[:-4]
    r = subprocess.run(['ptxas','-arch=sm_89',ptx,'-o',base+'.cubin'],capture_output=True,text=True)
    if r.returncode:
        out.append(dict(problem=pid, ok=False, reason='ptxas: ' + r.stderr.strip()[-120:]))
        continue
    r = subprocess.run(['python','@REMOTE@/l4_bench.py',base+'.cubin',mdir,'@REPS@'],
                       capture_output=True, text=True, timeout=280)
    txt = r.stdout
    m = re.search(r'p50=([0-9.]+)', txt)
    c = next((l for l in txt.splitlines() if 'correctness' in l), '?')
    out.append(dict(problem=pid, ok=bool(m),
                    p50_us=float(m.group(1)) if m else None,
                    correctness=c.split('correctness: ')[-1][:60]))
print("LANE_JSON_START")
print(json.dumps(out))
print("LANE_JSON_END")
"""
    code = (code.replace("@TAG@", args.tag).replace("@REMOTE@", REMOTE_DIR)
                .replace("@REPS@", str(args.reps)))
    out = exec_remote(args.session, code, timeout=560)
    payload = out.split("LANE_JSON_START")[1].split("LANE_JSON_END")[0].strip()
    rows = json.loads(payload)

    # 4. report
    rows.sort(key=lambda r: r["problem"])
    print(f"\n{'problem':28} {'p50 us':>9}  correctness")
    for r in rows:
        print(f"{r['problem']:28} {r['p50_us'] if r['p50_us'] else '-':>9}  {r.get('correctness','')}"
              if r["ok"] else f"{r['problem']:28} FAIL: {r.get('reason','')}")
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    rec = {"tag": args.tag, "candidate": args.candidate, "rows": rows}
    with open(os.path.join(HERE, "out", "l4lane_results.jsonl"), "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"\n[lane] {sum(1 for r in rows if r['ok'])}/{len(rows)} ok -> gen/out/l4lane_results.jsonl")


if __name__ == "__main__":
    main()

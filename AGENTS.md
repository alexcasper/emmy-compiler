# Agent Instructions

This project uses **bd** (beads) for issue tracking. Run `bd prime` for full workflow context.

> **Architecture in one line:** Issues live in a local Dolt database
> (`.beads/dolt/`); cross-machine sync uses `bd dolt push/pull` (a
> git-compatible protocol), stored under `refs/dolt/data` on your git
> remote — separate from `refs/heads/*` where your code lives.
> `.beads/issues.jsonl` is a passive export, not the wire protocol.
>
> See [sync-concepts](https://github.com/gastownhall/beads/blob/main/docs/core-concepts/sync-concepts.md)
> for the one-screen overview and anti-patterns (don't treat JSONL as the
> source of truth; don't `bd import` during normal operation; don't
> reach for third-party Dolt hosting before trying the default).

## Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work atomically
bd close <id>         # Complete work
bd dolt push          # Push beads data to remote
```

## Non-Interactive Shell Commands

**ALWAYS use non-interactive flags** with file operations to avoid hanging on confirmation prompts.

Shell commands like `cp`, `mv`, and `rm` may be aliased to include `-i` (interactive) mode on some systems, causing the agent to hang indefinitely waiting for y/n input.

**Use these forms instead:**
```bash
# Force overwrite without prompting
cp -f source dest           # NOT: cp source dest
mv -f source dest           # NOT: mv source dest
rm -f file                  # NOT: rm file

# For recursive operations
rm -rf directory            # NOT: rm -r directory
cp -rf source dest          # NOT: cp -r source dest
```

**Other commands that may prompt:**
- `scp` - use `-o BatchMode=yes` for non-interactive
- `ssh` - use `-o BatchMode=yes` to fail instead of prompting
- `apt-get` - use `-y` flag
- `brew` - use `HOMEBREW_NO_AUTO_UPDATE=1` env var

## Emmy Hackathon Rules (from upstream TASK.md)

Source: `cloudrift-ai/emmy-hackathon-2026/TASK.md` (identical to `task/TASK.md`). Re-check upstream if it changes.

**Contract**
- Repo root must contain `compile.py`. Invocation: `python compile.py path/to/<kernel>.ir.json > out.ptx`. Reads one IR json path as `argv[1]`, writes PTX to stdout. Hidden-set evaluation runs this exact command.
- Entry name = the kernel's `name` in the IR (not our own naming).
- Parameters = `arg_order` from `meta.json` (not the IR node's `inputs`). Buffers are `.u64` pointers.
- Output must be correct under the launch geometry in `meta.json` (grid, block, smem). Guard threads with `N` from the Tile; the guard is not in the IR.
- Results must fall within `rtol`/`atol` from `meta.json`. Exact equality is not required.
- PTX must be pure ASCII, including comments. Start with `.version 8.0` / `.target sm_89` / `.address_size 64` (`sm_89` needs version ≥ 7.8).

**The one rule: the translation must be ours**
- Allowed: `emmy-ml==0.3.11` to load the IR via `Graph.from_dict`. Nothing else from emmy.
- Not eligible: lowering through emmy's renderer (`render_kernelop`), `emmy compile`, `nvcc`, or any other existing compiler, including chaining any of them with `nvcc -ptx`.
- Judges read every submission's code.
- Scope: DSPy/GEPA-generated candidates inherit this rule. No emmy, nvcc, or any other compiler may be used to lower or build them.
- **Testing and benchmarking exception (user direction):** `emmy compile` and `nvcc` MAY be used as reference oracles to TEST or BENCHMARK our output (e.g. comparing against emmy's/nvcc's PTX or timings). They must never produce, lower, or build the submitted solution.

**Out of scope**
- No optimization requirement. Speed is a tiebreaker for judges, not a gate.
- No register-allocation cleverness (use fresh virtual registers, let `ptxas` allocate).
- No TMA, tensor-core, or `wgmma` requirement. Dynamic shapes are not needed; every problem is static.

**Categories** (hidden set is variations within these):
1. pointwise (anchor `p00_scalar_add`)
2. reductions (`r01_array_sum`)
3. matmul (`m01_matmul_512`)
4. fused (`f01_rmsnorm`; `f02` is online softmax)
5. attention-like (`a01_attention`)

**Facts that cost time**
- `ConstantOp` nodes arrive as 1-element buffer args.
- Vectorized loads and stores (`ld/st.global.v2`/`v4`) are expected when the IR groups values.
- Static shared memory needs no `smem_bytes` at launch; `meta.json` already accounts for it.
- The IR `json` graph level is plain: `inputs`, `outputs`, and per-node `shape`/`dtype` give signatures for free.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:1105d646 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/core-concepts/sync-concepts.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

<!-- BEGIN BEADS CODEX SETUP: generated by bd setup codex -->
## Beads Issue Tracker

Use Beads (`bd`) for durable task tracking in repositories that include it. Use the `beads` skill at `.agents/skills/beads/SKILL.md` (project install) or `~/.agents/skills/beads/SKILL.md` (global install) for Beads workflow guidance, then use the `bd` CLI for issue operations.

### Quick Reference

```bash
bd ready                # Find available work
bd show <id>            # View issue details
bd update <id> --claim  # Claim work
bd close <id>           # Complete work
bd prime                # Refresh Beads context
```

### Rules

- Use `bd` for all task tracking; do not create markdown TODO lists.
- Run `bd prime` when Beads context is missing or stale. Codex 0.129.0+ can load Beads context automatically through native hooks; use `/hooks` to inspect or toggle them.
- Keep persistent project memory in Beads via `bd remember`; do not create ad hoc memory files.

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/core-concepts/sync-concepts.md for details and anti-patterns.
<!-- END BEADS CODEX SETUP -->

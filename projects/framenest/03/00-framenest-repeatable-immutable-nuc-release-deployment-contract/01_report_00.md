### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 01
Worker session exchange ordinal: 01
Standard terminal status: PASS
Phase-qualified result: planning-PASS
Result artifact or commit: no repository artifact; terminal planning report
Result evidence:
- Public main verified: `git ls-remote origin` returned `4b04b86e4ea52c673c41624e3f2abe1e59d45907` for both `HEAD` and `refs/heads/main`; the required public main baseline matches exactly.
- Public-main AP pin verified: `git ls-tree 4b04b86... .ap` returned `17b7e085139e9bcbb0e4953d26aef9b6687d541c`, matching the required AP gitlink.
- Canonical checkout identity verified: `origin https://github.com/cisarik/framenest.git`; local HEAD `d4c3402a4765b39cee0d8e2063df5ecbe1d5afcac6` on `feat/ap-baseline-bound-execution-adoption` (an ancestor of public main 4b04b86); `merge-base` = local HEAD (explained divergence; public main has advanced).
- Worktree hygiene: tracked files clean; untracked owner artifacts present (`.accept-immut inkwork/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`) — preserved, not touched; incident `uv.lock` is not project authority per WORKER_EXECUTION_CONTRACT.
- `.ap/ap doctor` PASS for the canonical checkout; submodule clean at its local gitlink.
- Required reading completed: AGENTS.md, `.ap/AP.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md` (planning/report sections), `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/NUC_HOST_BASELINE.md`, `docs/BACKUP_AND_RECOVERY.md`, ADR-0032, ADR-0052, `deploy/ubuntu/README.md`, `deploy/ubuntu/fn-production-env-deploy`, `deploy/ubuntu/production_ai_deploy.py` (creating model pattern), `deploy/systemd/faNUC.service`, and the baseline `scripts/operator/network/…adults_nuc_worker_gate.fish` (+ its OPERATOR_NETWORK contract). Existing focused test inspected: `tests/contract/test_production_ai_deployment.py` and `tests/contract/test_nuc_operator_runbook.py`.
- Production/schema/backup state comes from Cooperator-provided live evidence (release 148b6c2…, schema 0028, backup/readiness ready, off-device parked); accepted as task authority, not re-derived on-NUC here.
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: all Worker 01 exchange 01 planning authority expired at this report

Approval-gated plan follows. No implementation, no mutation, no Git writes were made.

---

## Decision-complete implementation plan

### 1. Objective restated (operational)

"Future Orchestrators and Workers must meet one authoritative, discoverable routine immutable NUC update path, without reinventing the uv harness, confusing initial bootstrap with a routine update, guessing Poetry/CPython paths, or splicing historical chat commands."

Smallest safe repository change: one stable operator entry point + stdlib Python agent under `deploy/ubuntu/`, a root `AGENTS.md` invariant, runbook/README accrual, one new ADR (ADR-0060, the next number after ADR-0059), surfaced through `deploy/ubuntu/README.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`, `README.md`, and the ADR index — all backed by focused, contained (fake-runner/temp-dir) tests.

### 2. Recommended artifact / file map

New files (all under trial, E2 later):

- `deploy/ubuntu/fnuc-release-update` — thin Fish entry point (mimics existing `deploy/ubuntu/fn-production-env-deploy`): `#!/usr/bin/env fish`, computes script dir, execs `python3 "$dir"/(nuc_release_agent.py "")`.
- `deploy/ubuntu/nuc_release_agent.py` — stdlib-only Python engine (`argparse`, `hashlib`, `shutil`, `tarfile`, `pathlib`, `subprocess`, `sys`, `os`, `dataclasses`, `tempfile`, `stat`). Implements `check`, `deploy`, `rollback`, `status` subcommands, transports (strict `ssh -o BatchMode…`) with strict bounded env, remote script build, lock, checkpoint, cutover, rollback, cleanup, exit-code/evidence model. Has an injected `runner` seam (like `production_ai_deploy`) for tests.
- `deploy/ubuntu/nuc_release_remote.sh` — tracked remote Bash helper (the "transferred, checksum-verified, tracked helper") that performs the mutating remote steps (release-tree build, `.venv`, poetry, `poetry.toml`, symlink change, systemctl restart, health probe) as discrete subcommands; transferred by the Python agent to a new root/tmp path as exact bytes, SHA-256-verified, `bash -n` validated, executed for `sudo -n`-gated commands only.
- Tracked exact default constants inline in `nuc_release_agent.py` (paths r = /opt/framework), escape-hash allow-no external secrets.

Modified files:
- `AGENTS.md` — add the always-read invariant (canonical routine-update entry point, tooling paths, uv-position, check-before-deploy rule). Outside the AP-managed block.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` — add a dedicated "Routine Immutable Update" section that separates host bootstrap/maintenance from routine release updates, pointing to the helper; keep historical production-SHA claims untouched.
- `deploy/ubuntu/README.md` — remove the "deliberately lacks; mention the new helper as authoritative path (no longer "no auto").
- `docs/adr/README.md` — add index row ADR-0060.
- `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md` — new angular durable ADR; establishes ADR-0060 next.
- `README.md` — add a short pointer (one line) to the routine-update entry point in the deployment paragraph; do not rewrite the production-SHA claims.
- `docs/WORKER_EXECUTION_CONTRACT.md` — one pointer line (optional; included) to the invariant and tests.

New test file (this is the deliberate non-monolithic split):
- `tests/contract/test_nuc_release_contract.py` — focused: transport-free, using fake runner + temp dirs; covers all required negatives/positives.
- `tests/contract/test_nuc_release_docs.py` — doc/runbook/ADR contract parity (mirrors `test_nuc_operator_runbook`) verifying the runbook no longer forbids tested release automation, the invariant text exists, and tooling paths/uv-position are consistent.

### 3. Exact CLI shape (user-facing)

```text
deploy/ubuntu/fnuc-release-agent check  --release <40-hex-sha> [--target <name>] [--user <name>] [--identity <file>] [--expected-hostname <host>] [--json] [--env <KEY=VAL> …]
deploy/ubuntu/fnuc-release-agent deploy --release <40-hex-sha> [--confirm] [--checkpoint] [--no-auto-check] [same transport flags]
deploy/ubuntu/fnuc-release-agent rollback --release <40-hex-sha> [--confirm] [transport flags]
deploy/ubuntu/fnuc-release-agent status [transport flags]
fnuc-release-agent (fish) passes $argv to nuc_release_agent.py
```

Rules:
- `check` is structurally non-mutating; it never writes, never runs remote mutation, never follows to deploy.
- `deploy` requires `--release` full 40-hex SHA; refuses to auto-deploy after `check`. Must be a concrete separate invocation; a `--confirm` flag must be passed (documented in runbook as a Cooperator decision). `deploy --confirm` must also re-run the full check locally and remotely afterwards.
- `rollback` targets a release SHA that already exists under `/opt/framenest/rollback`; it refuses unknown/missing releases.
- `status` is read-only, prints sanitized state/readiness (current symlink target, DB revision, backup restore_readiness, active release, unit state).
- Env-fallback reads `FRFramework_NUC_SSH_TARGET`, `FRFramework_NUC_SSH_USER`, `FRFramework_NUC_SSH_IDENTITY` (same names as the shell gate) — keeps compatibility, no secrets in argv.
- Every output is sanitized: accepts hashes, release dirs, generic paths; never prints credentials, SSH fingerprints, LAN/IPv4, tailnet names, private media, or the real identity file.

Transport contract: transport via provided ssh binary with `BatchMode=yes`, `StrictHostKeyChecking=yes`, `IdentitiesOnly=yes`, `ForwardAgent=no`, `ClearAllForwardings=yes`, `ConnectTimeout`, `RequestTTY=no` — mirror of the documented NUC gate options; hostname/identity validated like the gate (`^[A-Za-z0-9][A-Za-z0-9.-]*$`; user `^[A-Za-z_][A-Za-z0-9_-]*$`; no whitespace/`@`/option-like tokens).

### 4. Local vs remote responsibility boundary

Local (MacBook / operator repo):
- resolve exact full SHA; verify `HEAD == <SHA>` in that checkout; `git status` empty (tracked) or fail-closed; `git fetch` first? No—use `git ls-remote origin <branch>` inbound; rely on accepted public main evidence.
- build the exact release archive from the SHA (confirmed archive with pinned submodule outcome, see §5).
- compute bytes hash, prepare transport, run the runner seam for all actions; accumulate sanitized evidence.
- actions: build archive, orchestrator-side checks, sending bounded remote script bytes, interpreting structured remote JSON/exit codes, doing no sudo locally, never printing secrets.

Remote (NUC, as operator `sudo -n` when required):
- under a bounded, checksum-verified, tracked helper (`nuc_release_remote.sh`) — the only remote shell code path; the orchestrator never passes ad-hoc free-form shell selected by the user; only the tracked script's validated arguments.
- prepare under exact staging paths; write `.framenest-release-sha`; write `poetry.toml` (`[project]`?), actually a `poetry.toml` with `[virtualenvs] in-project = true`; `poetry check --lock`; `poetry env use <exact CPython path>`; `poetry install --only main --no-interaction --no-ansi`; readiness without service.
- after pass: atomic symlink switch; `systemctl restart framenest.service` exactly once; health via unit state + readiness command; sanitized logipe; rollback on failure.

### 5. Public Git and archive / submodule provenance design

- Input validation: full 40-hex SHA; reject abortive prefixes/partials.
- Public equality: `git ls-remote origin <sha>` must return the chosen SHA. No local `rev-parse` alone.
- Local check inside on the releasing machine: run `git rev-parse --verify <SHA>^{commit}` (object present) and equivalent (`git rev-parse HEAD` or worktree `git rev-parse --is-inside-work-tree`) — `HEAD` can be on any verified branch as long as object exists; for this contract we default to **working on a clean exact checkout**: `git status --porcelain` empty, `git rev-parse HEAD == <SHA>`. If local repo is a feature branch (this planning session finds HEAD d4c…) the release is still built from a **clean worktree of the exact public SHA**, e.g., `git worktree add` to an isolated temp, or a disposable fresh clone; we use the tool on a clean tree but never mutate the canonical checkout.
- Deterministic `.ap` handling (core requirement): ordinary `git archive` does not include submodule content. Two sanctioned paths:
  - **Recommended (chosen):** produce the release artifact by `git archive --format=tar <SHA>` (superproject, includes an empty `.ap` dir entry?) then assert the `.ap` entry is **explicitly a pinned gitlink (`.ap` gitlink) and NOT needed in the runtime tree** — documented, fail-closed: if any runtime/poetry step attempts to read `.ap`, the build fails. Additionally write into manifest: `ap_gitlink = <SHA>` (from `git ls-tree <SHA> .ap`) and hard-assert it equals the task-pinned AP commit when public main is being used (here `17b7e0…` for older `def separation`). The builtable release never follows AP `main`; delete? no — cannot mutate via checkout; the archive simply omits submodule content, and the manifest records the exact pinned gitlink and that `.ap` is governance tooling not shipped/needed at runtime — so we do NOT encrypt or install `.ap` into releases. Rationale: `.ap/` is protocol tooling for agent work; production runtime `/opt/framenest/current` must contain the exact FrameNest source tree → committed files + poetry venv; `.ap` content doesn't affect runtime. Include in commit evidence and in tests a check that the built archive has no `.ap`-relative file content.
  
  Alternative (rejected as default): materialize `.ap` submodule content deterministically into the release tree — rejected because it polls the release with protocol tooling and needs a submodule update (unproven), while the acceptance closes the path-raising that the task demands. If an Orchestrator prefers a fully self-contained tree (including tooling), record as an open—disposers decision (Risk D-1).
- Archive identity: `git archive --format=tar --prefix=framenest-<SHA>/ <SHA>`; compute SHA-256 (bytes) of the resulting tar (deterministic, no mtimestamp variation? `git archive` is deterministic). Forward to remote as stdin; remote writes to bounded path, then `sha256sum` comparison vs expected; abort on mismatch.
- Transfer verifies bytes before extraction — required.
- The archive is the exact source representation: no dirty files, no untracked, no unrelated work.

### 6. Privilege and transport design

- No password ever requested/printed/stored/transmitted (matches existing helper).
- All remote privileged operations under `sudo -n` only, after an owner-established timestamp (documented runbook: Cooperator runs `sudo -v`, verifies `sudo -n true`, keeps timestamp bounded, ends with `sudo -K` after terminal output — recorded; if session lost first, report `unknown-session-lost`, never fabricate `sudo -k`).
- The Python agent executes only bounded remote subcommands through the transferred remote script (`bash -n`-verified, hash-checked) — never through user-supplied remote command strings; the remote script uses `set -euo pipefail`, `umask 077`, exact paths only.
- No broad remote shell strings; the remote helper is the single rest-mutation boundary.
- SSH gate reuse: reconcile—the agent inherits the gate's transport options and argument validation semantics; it is deliberately *not* a wrapper on the fish mullgate (that script is for operator console; this is a noninteractive automated path). Reconcile = transport option parity + same name-policy/formagnitude; and the runbook explains the gate vs agent relation.

### 7. Phase / state machine (deploy flow)

```text
check (read-only) ......................... phase[CHECK], exit 0..OK
   .ap gitlink asserted   .ap archive omitted (recorded), entry point defined

deploy (--confirm, explicit) ->
  L0 preflight-local (clean repo/policy/SHA exists, public ref equality)
  L1 transport reachable via ssh noninteractive (no sudo)
  L2 remote state preflight: current symlink, unit state, target release absent
  L3 backup checkpoint: create/verify fresh verified checkpoint (or use selected fresh)
  L4 schema equality gate (fail-closed §9)
  L5 prepare: transfer+verify archive; extract only under new release dir; .sha; poetry.toml; .venv; poetry install
  L6 pre-cutover readiness from new release root (read-only, under env contract; service identity)
  L7 atomically switch /opt/framenest/current
  L8 restart framenest.service ONCE
  L9 post-check: unit active, release identity by symlink + .sha file, working dir, DB readiness, health via accepted ingress, sanitized logs
  L10 success / cleanup owner records evidence; sudo -K asked after
```

rollback state machine:
```text
R1 capture current release; target = previous release dir (must exist)
R2 restore symlink atomically to previous
R3 readiness via previous release (read-only)
R4 restart once
R5 verify same gates as L9
Rfail -> leave .current in a known/ifpartial state, report rollback-failed + recovery material location
```

### 8. Backup / schema / readiness rules

- Precondition at L3: require fresh current sanitized backup/restore-readiness evidence — `framenest-backup status` must report `restore_readiness == "ready"` (fresh scheduled or manual checkpoint within age) unless `--no-backup` explicitly invoked (rejected if checkpoint not fresh).
- L3: deploy mode **creates** a new verified rollback checkpoint before cutover: run checkpoint create under the protected env contract (service identity, exact env file), verify it, then ensure it is in the retention/disposable set; this checkpoint is the rollback bootstrake.
- L4 schema: fail-closed routine boundary: compare packaged head (target release) with current production DB revision. If they differ (unexpected packaged/production schema difference) → refuse to proceed with a sanitized "schema change required; migration task out-of-scope for the routine-update run" (do not hide migration authority). If equal (routine patch), proceed. This satisfies "first implementation prefers fail-closed". No implicit migration throughout: service unit's existing `check-database-ready` startup gate stays; helper itself never calls `framenest-db migrate` and never changes schema.
- Target release status/readiness runs under accepted service identity `sudo -u framew spawn --chdir=… env FRAMENEST_ENV_FILE=… <release>/.venv/bin/framenest-production check-database-ready` and `framenest-db status`; never `sudo`-free with the wrong identity.

### 9. Cutover and rollback algorithm (detailed §9)

Referenced cutover:
1. Pre-gates $L0–L4 pass.
2. `ln -s -n <release-dir> /opt/framenest/current.tmp`? No — prefer atomic `ln -sfn` is not (can leave interval). Accept the single `--atomic` update: `ln -sfn` is acceptable if the only race window is `current → new`, but design chooses create `/opt/franeworks/current.new` then `mv` (rename) which is atomic and replaces the symlink; then verify `readlink -f current` == `release-dir`.
3. `systemctl restart framenest.service` once (only if not running incorrectly).

Rollback on failure (deploy-flow guard):
- If post-switch readiness timesout/service fails → restore the *captured previous release* reference via `mv current.new previous` dance: `ln -sfn <prev> current` along same atomic approach, then validate with `check-database-ready`, `restart` once, health via ingress, logs.
- outcome matrix, which must be distinct:
  - `deployment-failure` (pre-switch step X)
  - `rollback-success` (post-switch failed, rollback fully healthy)
  - `rollback-failure` (attempt failed)
  - `readiness-timeout` (either)
  - `service-terminal-failure`
  - `cleanup-failure`
  - `unknown-privilege-release` (sudo-a/after)
- all phases exit with a dedicated non-zero exit code model (small constantint range like production_ai_deploy: e.g., 70 demo checkpoint, 71 release-exists, 72 hash mismatch, 73 archive unsafe, 74 schema-mismatch, 75 readiness-fail, 76 readiness-timeout, 77 retained-recovery, 78 rollback-failed, 79 rollback-success-need-review, 80 cleanup, etc.; test asserts each).

### 10. Idempotency and crash recovery

- No wildcard deletion anywhere in the agent (all `rm` with exact bounded owned paths; `sudo -n rm -f <explicit>` allowed).
- Existing target release (under /opt/…/current or releases/<SHA>) => fail-closed with sanitized message; never overwrite.
- A partially built target (e.g., archive extracted but venv not complete) is never deployable: extract to `releases/<SHA>.staging-<random>` (or `.incomplete`) and rename to the exact target only after success (atomic move) + a `.framenest-release.ok` marker written as final step; if no marker → not deployable.
- Stale recovery state (e.g., `/run/framenest-release-deploy` or the `.staging` dir) must fail-closed with explicitly documented operator recovery path (`fnuc-release-agent recover --exact-path` is NOT introduced; the runbook documents `rm` exact dir operator step) — actually keep a `--recover` documented operator-side command (operator runbook command) but never automatic delete.
- Deterministic operator recovery:
  - interrupted preparation: remove only the exact `.staging/.incomplete` path after operator verification; recreate.
  - interrupted cutover: two symlink never partially placed (atomic); operator re-runs check; deploy again.
  - interrupted rollback: report and give the exact old-release symlink restore command as a deterministic runbook block.
- evidence retained in sanitized log until operator cleanup; never store secrets; recovery material noted.

### 11. Sanitized evidence and exit-status model

- All stdout is structured parseable lines with fields `<phase>=<status>`, `<key>=<sanitized-value>`; no keys contain raw remote output except a `facts` JSON per phase.
- never print: path of identity file, SSH target (except alias-format), env/sudo, API keys, disk UUIDs/serials.
- exit codes map to the enumerated outcomes above; the tool also writes a state cache file under /run (remote) on NUC limited to status (no secrets).
- "Preserve first causal failure": on any phase failure, print the first failing phase code/resources; if later probe also fails, retain the message of the first in stderr; cleanup failure is secondary.

### 12. Documentation ownership & updates

- New ADR-0060 (next number after 0059 — verified the baseline index ends at 0059) is the **correct durable owner** for the repeatable immutable release-update architecture (decision: yes). It supersedes nothing; it codifies ADR-0032 thread (update procedure) and ADR-0047 operator hygiene.
- docs/UBUNTU_NUC_DEPLOYMENT.md: restructure the "Plan" and "Prepare Release" sections: a new top-level "Routine immutable release update (suffix)" subsection that references the helper + states uv is bootstrap/maintenance, Poetry+CPython exact paths, `.framenest-release-sha`/`poetry.toml`/in-project venv invariant, `poetry check --lock`, `poetry env use`, `poetry install --only main …`, single restart, atomic switch, test-run via the new tests. Keep historical and bootstrap material marked differently; do not rewrite the historical production baseline SHA.
- deploy/ubuntu/README.md: drop the "without adding tested host-mutating automation" claim; instead "the directory contains the tested, helper "release update contract" with `fnuc-release-agent` + remote helper + doc pointers.
- docs/NUC_HOST_BASELINE.md: leave unchanged (historical evidence). At most add a one-line cross-ref "For routine updates see UBUNTU_NUC_DEPLOYMENT.md" in the Future Work list; do not backfill old observations.
- README.md: pointer sentence only.
- AGENTS.md invariant block (outside AP): exact text proposal:

```text
## NUC Routine Release Update Invariant (Repository Truth)
The canonical routine immutable NUC release-update command is:
  deploy/ubuntu/fn-release-agent check | deploy | rollback
  (Python engine: deploy/ubuntu/nuc_release_agent.py)
Routine updates MUST NOT invent commands: run `check` first, then deploy/rollback.
Accepted NUC tooling (update: routine updates reuse these exact paths):
  Poetry: /opt/framenest/toolbox/poetry/2.4.1/.venv/bin/poetry
  CPython: /opt/framenest/toolbox/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
uv is bootstrap/maintenance tooling only; it is NOT on the routine-update PATH and
is not invoked by the helper.
```

### 12. Focused and broad test matrix

- Focused new: `tests/contract/test_nuc_release_contract.py` with fake runner (like production_ai_deploy), temp chemistry — never touches real NUC/sudo/systemd; per required list cover:
  - check mode positive; public/ref mismatch; dirty source reject; missing exact tooling (Poetry/CPython absent under env mock) fail-closed; hash mismatch; existing target-release fail; unsafe archive (path traversal symlink escape, absolute paths) rejected; stale recovery state fail-closed; backup-not-ready (status restore_readiness != ready) blocked; schema-mismatch blocked (L4); poetry/lock failure; readiness failure→rollback success; rollback failure; cleanup failure; sanitized output (assert cast: no secrets in `capsys`/recorded).
  - Sorted subcommand discovery use once-only.
- `tests/contract/test_nuc_release_docs.py`: parse the invariant text, runbook refs to `fnuc-release-agent`, tooling path truth, `poetry.toml`/`[virtualenvs] in-project` string, `.framenest-release-sha` string, ADR-0060 index row, runbook no-longer-claims statement.
- New-executable syntax/format checks inside contract file: fish `--no-execute` on entry point (like existing), `bash -n` on `nuc_release_remote.sh`, `python -m py_compile` on agent.
- Broad suite / gates: the full `testpaths = ["tests"]` pytest suite (existing); plus the JavaScript contract suites (`node --test tests/*.test.js` per WORKER_EXECUTION_CONTRACT) — but those are unaffected by this slice; state they should stay green per `poetry run pytest`.
- Docs-style existing gates: `test_nuc_operator_runbook.py`, `test_production_ai_deployment.py` must remain green after doc edit (their assertions shouldn't break — update carefully).
- Acceptance gates: new contract test file passes; full `poetry run pytest` passes; doc parity file passes; `ap doctor` OK; worktree clean for the new branch state.
- Invocation contracts: `PYTHONPATH=<worktree>/src /home/áliga/Projects/framework/.venv/bin/python -m pytest <selection>` (exact-source); no real-hosts.

### 13. Implementation order

1. Draft ADR-0060 (architecture: boundary, .ap handling, schema/backup gates, rollback, exit-state, no-migration first gate).
2. Build `nuc_release_agent.py` core: parser + runner seam + transport + exit-code/state model + check-only path (no remote mutation).
3. Build `nuc_release_remote.sh` checked-in; wire transfer+hash+bash-n + remote subcommand dispatch.
4. Wire deploy phases/order + symlink + restart + health + rollback + recovery material.
5. Add Fish entry point + file map integration.
6. Write `test_nuc_release_contract.py` (fake runners) + doc-parity tests; iterate.
7. Update AGENTS.md invariant, runbook, deploy/ubuntu/README, ADR index, README link.
8. Full `poetry run pytest` + JS smoke + syntax checks; fix regressions in runbook tests; final clean diff review.

### 14. Exact allowed set / explicit exclusions

Implementation path allowlist (when later authorized):
- `deploy/ubuntu/fnuc-release-agent`, `deploy/ubuntu/nuc_release_agent.py`, `deploy/ubuntu/nuc_release_remote.sh`
- `AGENTS.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`, `deploy/ubuntu/README.md`, `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`, `docs/adr/README.md`, `README.md`
- `tests/contract/test_nuc_release_contract.py`, `tests/contract/test_nuc_release_docs.py`

Excluded scope (explicit):
- No fuzzy migration support in the helper (schema change tasks stay out).
- No off-device backup configuration, media second-copy, Tailscale/firewall/AppArmor/UFW/SSH account changes, storage/mount mutation, package/dependency install on the dev host, no `uv` provisioning, no `.github` changes, no frontend/JS edits, no AP protocol changes (it is only read for surrogate) and no upgrade-ledger use.
- No secrets in text/argv.
- No NUC mutation now or at implementation; helper is invoked only under an explicit authorized Cooperator host task (separate), expected to run its own live preflight at that later point (E3).

### 14. Risks & decisions needing Orchestrator/Cooperator disposition

- **D-1 `.ap` inclusion**: officially excluded-from-release (record gitlink in manifest, runtime package doesn't need it). Options: (a) preserve ex-C-86 (recommended; consistent with "never follow AP main", architecture clean) → accept; (b) include pinned `.ap` as fully self-contained tree — needs submodule deref; rejected unless Cooperator prefers.
- **D-2 rollback strategy**: default: reuse the exact previous release (rollback release exists as given: 148b6c2 release + release-local executable exist). Accept.
- **D-3 schema gate**: default fail-closed that the helper refuses schema distance. Decision to convert to "migrate within helper" is excluded (would need separate migration/backward-safety justification not assumed here).
- **D-4 backup gate**: requiring `restore_readiness==ready` via `framenest-backup status` + a fresh create/verify checkpoint before cutover. If pump `status` fails/unknown on newer release calls, sharp forward-update might need operator manual evidence — recommend accepting the ready gate only when evidence is fresh otherwise explicit operator-confirmed.
- **D-5 PowerShell/shell arbitration**: keep a single remote Bash helper (works) vs. extending Python to fully drive; robust to pre-Advanced— choose the Bash helper with checksum + `bash -n` (recommended).
- **D-6 exit code** numbers assigned are schema-free but must be documented and test-locked (accepted in code review).

### 15. Same-session implementation health decision

Recommended: same Worker session is **healthy** for approved implementation (E2, reversible, cross-cutting):
- guard verified: repo identity + public main 4b04b86 + required AP pin all hold; canonical checkout untouched; owner work preserved.
- new ADR-aligned slice; all required reading done; test pattern exists (`production_ai_deploy` model).
- independence not required for implementation; fresh independent acceptance recommended later (E2→ optional fresh) and E3 live NUC deployment requires separate approval with its own preflight.
- Non-independent implementation evidence.

### 16. Implementation-prompt readiness capsule

```
Objective: implement one repository-authored repeatable immutable NUC routine
release-update contract (helper + docs + ADR-0060 + focused tests) in the
exact path set above as §13, on public baseline you were issued (verify again).
Accepted decisions: ADR-0060 owner; exclude .ap from release artifact except
recorded gitlink (D-1-A); rollback to exact previous verified release; deploy
requires --confirm + fresh backup; schema-delta = fail-closed; single atom (mv)
swap; one restart; sudo -n owner-gated; no migration in helper; uv is never
involved once tooling CPython exists.
Repository/public anchor: cisarik/framenest.git; public main 4b04b86
(gitlink 17b7e085 …); local checkout must be clean.
Observed evidence: files above; test patterns seen.
Unresolved risks: D-1 (open for Cooperator disposition), D-3 out-of-scope
migration boundary, E3/live-deploy authority exposure.
Next bounded task: implementation Worker with Native planning mode: not-used,
fresh or current session; before live NUC use a separate host-task preflight.
Prohibitions: no NUC/ sudo/SSH/network, no real tools, no secret, no AP ledger;
secret acquisition GATED edge; no installs; no Git writes beyond the authorized
commit+push only if the Cooperator accepts publication of the ADR/docs slice.
Prior summary and authority: exchange 01 planning authority expired at this
report.
```

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

Deviation note: the governing `.ap` in the scanned-out working tree is `4862380f…` (a branch-local state) while the public main pins `17b7e085…`; this is an explained divergence (local feature branch vs. public main); the required AP pin matches public main — no contradiction, no stop triggered.
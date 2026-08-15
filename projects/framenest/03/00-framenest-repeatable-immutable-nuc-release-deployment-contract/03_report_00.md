### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `03`  
Worker exchange ordinal: `01`  
Standard terminal status: **BLOCKED**  
Phase-qualified result: **not-applicable**  
Result artifact: `2d995bb98a8b2c96fa1925f06403b3ee156c6237`  
Parent: `4b04b86e4ea52c673c41624e3f2abe1e59d45907`  
Start/end commit: `2d995bb98a8b2c96fa1925f06403b3ee156c6237` → `2d995bb98a8b2c96fa1925f06403b3ee156c6237` (unchanged; no mutation)  
Changed files: none  
Independent acceptance: this exchange; this session did not implement, repair, or previously review `2d995bb…`  
Publication / deployment / NUC / logical-whole closure: not claimed  
Logical-whole closure: not-closed  
Report justification: `final-acceptance`

**Identity gates.** Canonical checkout `/home/agile/Projects/framenest` on `feat/repeatable-immutable-nuc-release-deployment-contract`; `HEAD` `2d995bb98a8b2c96fa1925f06403b3ee156c6237`; parent `4b04b86e4ea52c673c41624e3f2abe1e59d45907`; `.ap` gitlink and `.ap` `HEAD` `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). No Git write, fetch, branch switch, or `.venv` reconstruction.

**Allowlist-diff result.** `git diff --name-status 4b04b86e… 2d995bb…` equals the frozen allowlist exactly (15 paths; 8 modified, 7 added). No extra path.

**Public-main readback.** Credential-free `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` → `4b04b86e4ea52c673c41624e3f2abe1e59d45907`. Candidate unpublished, as expected.

**Worker 02 reports.** Read as claims only (`02_report_00.md`, `02_report_01.md`, `02_report_02.md`). Not used as independent proof. Planning draft names (`fnuc-release-agent` / `nuc_release_agent.py`) are not a FAIL: shipped names match ADR-0060 and `AGENTS.md`.

### Frozen risk-claim verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Diff contains only the allowlist | **confirmed** |
| 2 | Public CLI is exactly `status`, `check --release <40-hex-SHA>`, `deploy --release <40-hex-SHA> --yes`, `rollback --release <40-hex-SHA> --yes`; check/status never deploy; deploy/rollback refuse without `--yes` | **confirmed** (parser + source; local `main()` without `--yes` returns `EXIT_USAGE` 2 before any runner call; `_cmd_check` / `_cmd_status` create no remote lock or transfer) |
| 3 | `deploy/ubuntu/framenest-release` is the sole Fish operator entry; invokes repository `.venv` Python against `framenest_release.py`; does not reconstruct PATH, call `uv`, or deploy by itself | **confirmed** (mode `755`; forwards `$argv` only) |
| 4 | Engine is Python stdlib-only and intended for Ubuntu system Python 3.12 private remote mode | **confirmed** (imports are stdlib; `tarfile` `filter="data"` is 3.12; residual: deploy never actually reaches that mode — see claim 7) |
| 5 | Routine updates use exact Poetry `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry` and CPython `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`; never invoke `uv`; never require `uv` on `PATH` | **confirmed** (`uv ` absent from engine; builders use those exact paths) |
| 6 | Full lowercase 40-hex SHA; local HEAD equality; clean superproject and `.ap`; public `refs/heads/main` equality; `.ap` HEAD equals release gitlink; AP `main` is never followed | **confirmed** (`SHA_PATTERN`; `verify_*`; `git archive` of `ls-tree` gitlink, not `main`) |
| 7 | Two archives hashed locally and re-verified remotely; members reject absolute/`..`/escape/devices/unsafe links; pinned AP under `<release>/.ap/`; deployed tree has no `.git`; identity is `.framenest-release-sha` plus `.framenest-release-manifest.json` | **rejected** |
| 8 | Immutable `/opt/framenest/releases/<40-hex-SHA>`; atomic `/opt/framenest/current` cutover; `framenest.service` restarts once; schema mismatch fail-closed `migration-required`; never `framenest-db migrate` | **confirmed** in source and fake-runner tests (`framenest-db migrate` absent; schema stop is before `ln -s`; happy-path single restart) |
| 9 | `check` requires backup restore readiness; `deploy` requires fresh verified checkpoint before cutover; post-switch failure automatic rollback; rollback-failure and cleanup-failure distinct; first causal error preserved | **confirmed** (`EXIT_BACKUP_NOT_READY` 11, `EXIT_CHECKPOINT` 12, `EXIT_ROLLBACK` 18, `EXIT_CLEANUP` 19; schema path prints `migration-required`) |
| 10 | SSH `BatchMode`, no TTY, `StrictHostKeyChecking`, `IdentitiesOnly`, no agent forwarding, cleared forwardings; no passwords; no user-supplied remote shell strings; `sudo -n` only; sanitized output | **confirmed** (`SSH_OPTIONS`; transport args are SSH destination/identity only; no `sudo -S` / password handling; operator prints are SHA/path/status tokens) |
| 11 | Engine does not mutate the canonical owner checkout; tests use fake runners/temp dirs and must not contact a real NUC, SSH, sudo, systemd, or provider | **confirmed** |
| 12 | Documentation does not hide new product scope | **confirmed** (living docs reconcile `framenest-release status` as mutable readback and keep Cover Studio / desktop / media second-copy as unimplemented; no Browser Companion or AP `95bd644` adoption in the candidate diff) |
| 13 | Worker 02 passing tests are not independent proof | **confirmed** (this audit re-ran the selected tests and inspected source independently) |

### Claim 7 — causal blocker

Private remote extract mode is defined as nested argv `_remote _remote-extract` and that form parses.

`cmd_remote_extract()` emits:

```text
sudo -n python3 <engine> _remote-extract --archive … --destination …
```

Direct parse of that top-level argv against `_build_parser()`:

```text
invalid choice: '_remote-extract' (choose from status, check, deploy, rollback, _remote)
SystemExit 2
```

Local member validation (`validate_archive_member` / `extract_validated_archive`) exists and is unit-tested. The transferred-engine path that ADR-0060 requires (“executed only in its private fixed remote mode”) cannot enter that code. Focused remote tests match the substring `_remote-extract` in a fake SSH command string and never parse it as engine argv, so they do not detect this. Local hash, remote `sha256sum` re-verify of transferred bytes, `.ap` destination, `git archive` (no `.git`), and marker writes are present; they do not restore claim 7.

This is a candidate defect and an ADR-0060 / engine contradiction. It is not a live-host evidence gap.

### Tests (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gate not piped)

Focused:

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
53 passed in 0.09s
exit 0
```

Affected:

```text
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_production_ai_deployment.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_ap_project_contract.py
110 passed, 2 skipped in 0.19s
exit 0
```

Skipped nodes: `test_ap_project_contract.py` AP_OPERATION-absent skips (2). Full Python suite, JS/browser suites, SSH, sudo, and NUC contact were not run.

Passing focused tests do not override the rejected claim. Control matrix: BLOCKED if a frozen claim is contradicted.

### Discrepancies

- Remote extract argv ≠ parser private mode (`_remote-extract` vs `_remote _remote-extract`).
- No contract test feeds `cmd_remote_extract` output through `_build_parser()`.
- No focused negative test for `deploy` without `--yes` (source and a local `main()` probe still refuse).
- `_assert_logs_sanitized` only scans four tokens (`/etc/framenest/credentials`, `Authorization:`, `Bearer `, `BEGIN `). Journal text is not printed, but the checker is not a general secret/fingerprint/address/media filter.
- On rollback-failure, stderr is `rollback failed`; the first post-switch error remains in `__cause__`, not in the operator line.
- Name mismatch with planning drafts is not a FAIL.

### Residual risks

- Live NUC E3 (SSH/sudo/systemd/cutover/backup/schema/rollback on the host) was out of scope and is not claimed.
- Even after an extract-argv correction, remote archive-member rejection, atomic cutover, checkpoint, and rollback remain unproven on a real host.
- Failed deploy leaves `/run/framenest-release-deploy` as lock/recovery state (`EXIT_EXISTS` on retry); that is documented, not exercised on a host here.
- Public `main` is still `4b04b86…`; this candidate cannot pass its own public-main gate until a separately authorized publication.

### One smallest next step

Orchestrator should route a separately authorized bounded correction that makes `cmd_remote_extract` invoke `_remote _remote-extract` (the argv the parser actually accepts), add a contract test that parses that remote command through `_build_parser()`, and then route a fresh independent re-acceptance of the new commit. This Worker must not correct, re-accept, publish, or deploy.

### Resolved Execution Issues / Near-Misses

Inherited AppImage `LD_LIBRARY_PATH` made `/home/agile/Projects/framenest/.venv/bin/python` fail with `No module named 'encodings'`. Cleared by `env -i` per `docs/WORKER_EXECUTION_CONTRACT.md`. `.venv` was not reconstructed. Residual: none for the candidate.

### Pre-Existing Failure Classification

none for this envelope. Selected focused and affected gates exited 0. Worker 02 full-suite / missing-console-script history was not re-run and is not used as acceptance evidence.

Authority expiry: all Worker 03 exchange 01 independent-acceptance authority expires at this terminal report.
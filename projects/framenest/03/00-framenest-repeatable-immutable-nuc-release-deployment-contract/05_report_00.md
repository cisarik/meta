### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `05`  
Worker exchange ordinal: `01`  
Standard terminal status: **PASS**  
Phase-qualified result: **acceptance-PASS**  
Result artifact: `011823a9dcb3d2a51e684fefd5083970f3610701`  
Correction parent: `2d995bb98a8b2c96fa1925f06403b3ee156c6237`  
Whole-logical-whole parent: `4b04b86e4ea52c673c41624e3f2abe1e59d45907`  
Start/end commit: `011823a9dcb3d2a51e684fefd5083970f3610701` → `011823a9dcb3d2a51e684fefd5083970f3610701` (unchanged; no mutation)  
Changed files: none  
Independent acceptance: this exchange; this session did not implement, repair, accept, or reject `2d995bb…` or `011823a9…`  
Publication / deployment / NUC / logical-whole closure: not claimed  
Logical-whole closure: not-closed  
Report justification: `final-acceptance`

**Identity gates.** Canonical checkout `/home/agile/Projects/framenest` on `feat/repeatable-immutable-nuc-release-deployment-contract`; `HEAD` `011823a9dcb3d2a51e684fefd5083970f3610701`; parent `2d995bb98a8b2c96fa1925f06403b3ee156c6237`; whole parent `4b04b86e4ea52c673c41624e3f2abe1e59d45907`; `.ap` gitlink and `.ap` `HEAD` `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). No Git write, fetch, branch switch, or `.venv` reconstruction.

**Allowlist-diff results.**  
`git diff --name-status 4b04b86e4ea52c673c41624e3f2abe1e59d45907 011823a9dcb3d2a51e684fefd5083970f3610701` equals the frozen 15-path allowlist exactly (8 modified, 7 added). No extra path.  
`git diff --name-status 2d995bb98a8b2c96fa1925f06403b3ee156c6237 011823a9dcb3d2a51e684fefd5083970f3610701` equals the frozen two-path correction allowlist exactly: `deploy/ubuntu/framenest_release.py`, `tests/contract/test_nuc_release_remote_contract.py` (`2 files changed, 40 insertions(+), 1 deletion(-)`). No extra path.

**Public-main readback.** Credential-free `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` → `4b04b86e4ea52c673c41624e3f2abe1e59d45907`. Candidate unpublished, as expected.

**Worker 03 / Worker 04 reports.** Read as claims only. Not used as independent proof. Candidate files and this session’s parse/`engine.main`/pytest evidence outrank those reports.

### Frozen risk-claim verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Diff `4b04b86…` → `011823a9…` contains only the 15-path allowlist | **confirmed** |
| 2 | Public CLI is exactly `status`, `check --release <40-hex-SHA>`, `deploy --release <40-hex-SHA> --yes`, `rollback --release <40-hex-SHA> --yes`; check/status never deploy; deploy/rollback refuse without `--yes` | **confirmed** (parser choices `_remote`/check/deploy/rollback/status; `_cmd_status`/`_cmd_check` never create `/run/framenest-release-deploy`; independent `engine.main(["deploy"|"rollback", "--release", <40-hex>])` returns `EXIT_USAGE` 2 with a boom runner that is never called) |
| 3 | `deploy/ubuntu/framenest-release` is the sole Fish operator entry; invokes repository `.venv` Python against `framenest_release.py`; does not reconstruct PATH, call `uv`, or deploy by itself | **confirmed** (mode `755`; `command "$python" "$engine" $argv` only) |
| 4 | Engine is Python stdlib-only and intended for Ubuntu system Python 3.12 private remote mode | **confirmed** (stdlib imports; `tarfile` `filter="data"`) |
| 5 | Routine updates use exact Poetry `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry` and CPython `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`; never invoke `uv`; never require `uv` on `PATH` | **confirmed** (`uv ` absent from engine; those exact paths are the only Poetry/CPython builders) |
| 6 | Full lowercase 40-hex SHA; local HEAD equality; clean superproject and `.ap`; public `refs/heads/main` equality; `.ap` HEAD equals release gitlink; AP `main` is never followed | **confirmed** (`SHA_PATTERN`; `verify_*`; `git archive` of `ls-tree` gitlink, not AP `main`) |
| 7 | Two archives hashed locally and re-verified remotely; members reject absolute/`..`/escape/devices/unsafe links; pinned AP under `<release>/.ap/`; deployed tree has no `.git`; identity is `.framenest-release-sha` plus `.framenest-release-manifest.json`; `cmd_remote_extract` emits nested `_remote _remote-extract` that `_build_parser()` accepts so `remote_extract` / `extract_validated_archive` is reachable on the transferred-engine path | **confirmed** (see F01) |
| 8 | Immutable `/opt/framenest/releases/<40-hex-SHA>`; atomic `/opt/framenest/current` cutover; `framenest.service` restarts once; schema mismatch fail-closed `migration-required`; never `framenest-db migrate` | **confirmed** (`framenest-db migrate` absent; schema stop is before `ln -s` cutover; happy-path single restart in source) |
| 9 | `check` requires backup restore readiness; `deploy` requires fresh verified checkpoint before cutover; post-switch failure automatic rollback; rollback-failure and cleanup-failure distinct; first causal error preserved | **confirmed** (`EXIT_BACKUP_NOT_READY` 11, `EXIT_CHECKPOINT` 12, `EXIT_ROLLBACK` 18, `EXIT_CLEANUP` 19; `from exc` chains) |
| 10 | SSH `BatchMode`, no TTY, `StrictHostKeyChecking`, `IdentitiesOnly`, no agent forwarding, cleared forwardings; no passwords; no user-supplied remote shell strings; `sudo -n` only; sanitized output | **confirmed** (`SSH_OPTIONS`; transport args are destination/identity only; no `sudo -S` / password handling) |
| 11 | Engine does not mutate the canonical owner checkout; tests use fake runners/temp dirs and must not contact a real NUC, SSH, sudo, systemd, or provider | **confirmed** (archives in `tempfile`; tests use `FakeRunner`/`tmp_path`; this session left tracked tree clean) |
| 12 | Documentation does not hide new product scope | **confirmed** (living docs keep Cover Studio / desktop / media second-copy unimplemented; no Browser Companion or AP `95bd644` adoption in the candidate diff; ADR-0060 is repository capability until a later live deployment) |
| 13 | Worker 02/04 passing tests are not independent proof | **confirmed** (this audit re-parsed extract argv, ran `engine.main` of that argv, and re-ran the selected tests independently) |

### Finding FN-NUC-RELEASE-ACCEPT-03-F01

Verdict: **verified-closed**

Independent probe under `/tmp/fn-reaccept-05-dVrRgA` (not Worker 04 pytest). `REMOTE_DEPLOY_DIR` / `RELEASE_ROOT` were pointed at that temp tree only so `validate_remote_path` could accept a non-`/opt` destination; no SSH, sudo, or host path was used.

Emitted command:

```text
sudo -n python3 <engine> _remote _remote-extract --archive … --destination …
```

Remaining argv parsed by `_build_parser()`:

```text
PARSE_OK command=_remote remote_command=_remote-extract
```

`engine.main` of that remaining argv returned `EXIT_OK` 0 and extracted `pyproject.toml` / `poetry.lock` through `_cmd_remote` → `remote_extract` → `extract_validated_archive`. Top-level `_remote-extract` still fails:

```text
invalid choice: '_remote-extract' (choose from status, check, deploy, rollback, _remote)
SystemExit 2
```

Top-level parser choices are exactly `{_remote, check, deploy, rollback, status}`. There is no second top-level `_remote-extract` public command. The Worker 03 extract-argv assumption does not survive on `011823a9…`.

### Tests (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gate not piped)

Focused:

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
54 passed in 0.14s
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

### Discrepancies

None that falsify a frozen claim. Parked residuals remain parked:

- `_assert_logs_sanitized` still scans four tokens (`/etc/framenest/credentials`, `Authorization:`, `Bearer `, `BEGIN `).
- On rollback-failure, stderr is `rollback failed`; the first causal error remains in `__cause__`.
- No focused negative pytest node for `deploy` without `--yes` (source and this session’s `engine.main` probe still refuse with `EXIT_USAGE` 2 before any runner call).

### Residual risks

- Live NUC E3 (SSH/sudo/systemd/cutover/backup/schema/rollback on the host) was out of scope and is not claimed; it is not converted into acceptance-PASS.
- Remote archive-member rejection, atomic cutover, checkpoint, and rollback remain unproven on a real host.
- Failed deploy still leaves `/run/framenest-release-deploy` as lock/recovery state (`EXIT_EXISTS` on retry); documented, not host-exercised here.
- Public `main` is still `4b04b86…`; this candidate cannot pass its own public-main gate until a separately authorized publication.

### One smallest next step

Orchestrator should take accepted unpublished candidate `011823a9…` to the Cooperator for the next separately authorized decision (publication and/or later E3 host proof). This Worker must not publish, deploy, correct, or close the logical whole.

### Resolved Execution Issues / Near-Misses

Inherited Cursor AppImage `LD_LIBRARY_PATH` makes `/home/agile/Projects/framenest/.venv/bin/python` fail with `No module named 'encodings'` unless cleared. All probes and pytest ran under `env -i` (no `LD_LIBRARY_PATH` / `PYTHONHOME`) per `docs/WORKER_EXECUTION_CONTRACT.md`. `.venv` was not reconstructed. Residual: none for the candidate.

### Pre-Existing Failure Classification

none for this envelope. Selected focused and affected gates exited 0. Worker 02 full-suite history was not re-run and is not used as acceptance evidence.

Authority expiry: all Worker 05 exchange 01 independent re-acceptance authority expires at this terminal report.
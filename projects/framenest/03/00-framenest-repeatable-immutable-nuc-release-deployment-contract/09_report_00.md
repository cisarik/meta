### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `09`  
Worker exchange ordinal: `01`  
Standard terminal status: **PASS**  
Phase-qualified result: **acceptance-PASS**  
Result artifact: `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
Correction parent: `011823a9dcb3d2a51e684fefd5083970f3610701`  
Whole-logical-whole parent: `4b04b86e4ea52c673c41624e3f2abe1e59d45907`  
Start/end commit: `de580f6f9d18cddbc4ad7894d163a361b30ef05f` → `de580f6f9d18cddbc4ad7894d163a361b30ef05f` (unchanged; no mutation)  
Tree: `d958914aeb1952d23d2b6aa7521a92bde14523f2`  
Changed files: none  
Independent acceptance: this exchange; this session did not implement, correct, accept, publish, or deploy `2d995bb…`, `011823a9…`, or `de580f6f…`  
Publication / deployment / production-acceptance-PASS / NUC / logical-whole closure: not claimed  
Logical-whole closure: not-closed  
Report justification: `final-acceptance`  
Secrets omitted: yes

**Identity gates.** Canonical checkout `/home/agile/Projects/framenest` on `feat/repeatable-immutable-nuc-release-deployment-contract`; `HEAD` `de580f6f9d18cddbc4ad7894d163a361b30ef05f`; parent `011823a9dcb3d2a51e684fefd5083970f3610701`; whole parent `4b04b86e4ea52c673c41624e3f2abe1e59d45907`; `.ap` gitlink and `.ap` `HEAD` `17b7e085139e9bcbb0e4953d26aef9b6687d541c`. Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). No Git write, fetch, branch switch, archive, Meta/AP mutation, or `.venv` reconstruction. No SSH/NUC.

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `011823a9dcb3d2a51e684fefd5083970f3610701	refs/heads/main`. Unpublished successor expected; candidate is not public `main`.

**Allowlist-diff results.**  
`git diff --name-status 4b04b86e4ea52c673c41624e3f2abe1e59d45907 de580f6f9d18cddbc4ad7894d163a361b30ef05f` equals the frozen 15-path allowlist exactly (8 modified, 7 added). No extra path.  
`git diff --name-status 011823a9dcb3d2a51e684fefd5083970f3610701 de580f6f9d18cddbc4ad7894d163a361b30ef05f` equals the frozen four-path correction allowlist exactly: `deploy/ubuntu/framenest_release.py`, `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`, `tests/contract/test_nuc_release_remote_contract.py`, `tests/contract/test_nuc_release_source_contract.py` (`4 files changed, 168 insertions(+), 7 deletions(-)`). No extra path.

Worker 07 was read as host finding only. Worker 08 was read as a correction claim only and was not used as independent proof.

### Frozen claim verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Diff `4b04b86…` → `de580f6f…` contains only the 15-path allowlist | **confirmed** |
| 2 | Diff `011823a9…` → `de580f6f…` contains only the four-path correction allowlist | **confirmed** |
| 3 | Public CLI remains `status` / `check --release <40-hex>` / `deploy --release <40-hex> --yes` / `rollback --release <40-hex> --yes`; check/status never deploy; deploy/rollback refuse without `--yes` | **confirmed** (parser choices `{_remote, check, deploy, rollback, status}`; `_cmd_status`/`_cmd_check` do not `mkdir` `/run/framenest-release-deploy`; independent `engine.main(["deploy"|"rollback", "--release", <40-hex>])` with a boom runner that is never called returns `EXIT_USAGE` 2) |
| 4 | `framenest-release` is the sole Fish entry; no `uv`; stdlib engine; exact NUC Poetry/CPython paths unchanged | **confirmed** (mode `755`; `command "$python" "$engine" $argv` only; stdlib imports only; `uv` absent from engine and Fish entry; Poetry `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry`; CPython `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`) |
| 5 | Nested private extract remains `_remote _remote-extract`; top-level `_remote-extract` still fails to parse | **confirmed** (see ACCEPT-03-F01) |
| 6 | New releases still write both `.framenest-release-sha` and `.framenest-release-manifest.json`. The helper does not synthesize a manifest on an old host tree | **confirmed** (`cmd_remote_write_markers` writes both; SHA-only `read_current_release` returns empty raw plus `{"framenest_release_sha": …}` in memory and does not write a host manifest; ADR-0060 forbids synthesizing a manifest on an old immutable tree) |
| 7 | DEPLOY-07-F01 SHA-only status/check and fail-closed missing/invalid markers | **confirmed** (see F01) |
| 8 | DEPLOY-07-F02 `--untracked-files=no`; tracked dirty still `EXIT_SOURCE_GATE`; ADR silence on untracked is residual | **confirmed** (see F02) |
| 9 | Worker 05 SHA/public-main/AP-pin/archive-member/immutable-release/atomic-cutover/same-schema/no-migrate/backup-checkpoint/rollback-distinct/SSH-options/sanitized-output/no-canonical-checkout-mutation/no-hidden-product-scope claims remain true except current-tree identity readback | **confirmed** (`SHA_PATTERN`; `ls-remote origin refs/heads/main`; `ls-tree` gitlink not AP `main`; `filter="data"`; `ln -s` + `mv -T` atomic switch; `migration-required` before cutover; `framenest-db migrate` absent; checkpoint `EXIT_CHECKPOINT` 12; rollback-failure `EXIT_ROLLBACK` 18 vs cleanup `EXIT_CLEANUP` 19; SSH `BatchMode`/`RequestTTY=no`/`StrictHostKeyChecking`/`IdentitiesOnly`/`ForwardAgent=no`/`ClearAllForwardings`; no `sudo -S`/password handling; `_assert_logs_sanitized`; archives in `tempfile`; tracked tree left clean; no Cover Studio / desktop / media second-copy / Browser Companion scope in the candidate files) |
| 10 | Worker 08 tests are claims, not independent proof. Live NUC is out of scope and must not be converted into acceptance-PASS | **confirmed** (independent `/tmp` FakeRunner probe of candidate `framenest_release.py`; no SSH/NUC; live host not used as PASS) |

### Finding FN-NUC-RELEASE-ACCEPT-03-F01

Verdict: **verified-closed** (remains closed)

Independent parse/`engine.main` probe (not Worker 08 pytest). Emitted command still:

```text
sudo -n python3 <engine> _remote _remote-extract --archive … --destination …
```

`_build_parser()` accepts remaining argv as `command=_remote remote_command=_remote-extract`. `engine.main` of that nested argv returned `EXIT_OK` 0 and extracted `pyproject.toml` / `poetry.lock` into an owned `/tmp` tree after remapping `RELEASE_ROOT` / `REMOTE_DEPLOY_DIR` for `validate_remote_path` only. No SSH, sudo, or `/opt` write.

Top-level `_remote-extract` still fails:

```text
invalid choice: '_remote-extract' (choose from status, check, deploy, rollback, _remote)
SystemExit 2
```

### Finding FN-NUC-RELEASE-DEPLOY-07-F01

Verdict: **verified-closed**

Independent FakeRunner (does not import contract tests):

- SHA-only (`probe=sha`, valid lowercase 40-hex): `status` exit **0**; prints that SHA as `active_release`; prints `release_manifest: absent`; does not print `ap_gitlink` or archive hashes; does not emit opaque `command failed`.
- Same SHA-only tree: `check` exit **0**; `framenest-backup status` is invoked with `current_path` from `readlink` (`/opt/framenest/releases/<sha>`); prints `backup_restore_readiness: ready`; creates no `/run/framenest-release-deploy` lock. Check `ap_gitlink` / archive hashes are local requested-release archive hashes, not invented from the old host tree.
- Both markers absent (`probe=none`): exit **20**; stderr `framenest-release: current release SHA marker and manifest are absent`; not opaque `command failed`.
- Invalid SHA marker: exit **20**; stderr `framenest-release: current release SHA marker is invalid`; not opaque `command failed`.

The Worker 07 missing-manifest / opaque-`command-failed` assumption does not survive on `de580f6f…`.

### Finding FN-NUC-RELEASE-DEPLOY-07-F02

Verdict: **verified-closed**

`verify_clean_worktrees` argv is exactly `status --porcelain --untracked-files=no` on the superproject and `git -C .ap status --porcelain --untracked-files=no`. Owner-untracked `??` is ignored. Tracked ` M AGENTS.md` still raises `worktree is not clean` with `EXIT_SOURCE_GATE` 3.

ADR-0060 says worktrees must be “clean” and is silent on untracked files; that silence remains a parked residual, not an automatic FAIL. ADR does not require untracked paths to fail.

### Tests (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gate not piped)

Focused:

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
59 passed in 0.18s
exit 0
```

Affected:

```text
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_production_ai_deployment.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_ap_project_contract.py
110 passed, 2 skipped in 0.17s
exit 0
```

Skipped nodes: `test_ap_project_contract.py` AP_OPERATION-absent skips (2). Full Python suite, JS/browser suites, SSH, sudo, and NUC contact were not run. Worker 08 pytest was not treated as independent proof; this session re-ran the selected gates after the independent probe.

### Discrepancies

None that falsify a frozen claim. Parked residuals remain parked:

- `_assert_logs_sanitized` still scans four tokens (`/etc/framenest/credentials`, `Authorization:`, `Bearer `, `BEGIN `).
- On rollback-failure, stderr is `rollback failed`; the first causal error remains in `__cause__`.
- No focused negative pytest node for `deploy` without `--yes` (source and this session’s `engine.main` probe still refuse with `EXIT_USAGE` 2 before any runner call).
- ADR-0060 remains silent on untracked files (residual; not a FAIL under the frozen F02 rule).

### Residual risks

- Live NUC E3 (SSH/sudo/systemd/cutover/backup/schema/rollback on the host) was out of scope and is not claimed; it is not converted into acceptance-PASS.
- Public `main` is still `011823a9…`; this successor cannot pass its own public-main gate until a separately authorized republication of `de580f6f…`.
- Failed deploy still leaves `/run/framenest-release-deploy` as lock/recovery state (`EXIT_EXISTS` on retry); documented, not host-exercised here.

### One smallest next step

Orchestrator should take accepted unpublished candidate `de580f6f9d18cddbc4ad7894d163a361b30ef05f` to separately authorized **republication of this SHA**. Do not deploy yet. This Worker must not publish, deploy, correct, archive, or close the logical whole.

### Resolved Execution Issues / Near-Misses

- Inherited Cursor AppImage `LD_LIBRARY_PATH` / `PYTHONHOME` makes `/home/agile/Projects/framenest/.venv/bin/python` fail with `No module named 'encodings'` unless cleared. Independent probe and pytest ran under `env -i` per `docs/WORKER_EXECUTION_CONTRACT.md`. `.venv` was not reconstructed.
- Owned probe tree `/tmp/fn-reaccept-09-IApS7F` was removed after the probe. Canonical checkout unchanged.

### Pre-Existing Failure Classification

Live test-NUC tree `148b6c2…` remains a pre-manifest host fact from Worker 07. This Worker did not contact that host and did not write markers. The candidate helper observes such a tree via `.framenest-release-sha` only. That host gap is not a candidate defect on `de580f6f…` and is not acceptance-PASS for live deployment. Selected focused and affected gates exited 0.

Authority expiry: all Worker 09 exchange 01 independent re-acceptance authority expires at this terminal report.
### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `18`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: Fresh Independent Re-Audit  
Phase: acceptance  
Task identity: `FN-NUC-RELEASE-REACCEPT-18`

**PASS** | **acceptance-PASS**

This chat did not implement, correct, accept, publish, recover leftover host state, or deploy `2d995bb…`, `011823a9…`, `de580f6f…`, `d963df7…`, or `43c9849…`. No SSH/NUC contact. No Git write. No Meta/AP mutation. No correction.

**Result artifact:** `43c9849a1ff3449a3c06585571c17439ecff9025`  
**Accepted tree:** `df98c395cc4d88cd8b37a92f854f79a245b0facd`  
**Correction parent:** `d963df7dfc7d56c75f3696e8bc3830ee81a98534`  
**Whole-logical-whole parent:** `4b04b86e4ea52c673c41624e3f2abe1e59d45907`  
**Start/end commit:** `43c9849a1ff3449a3c06585571c17439ecff9025` → `43c9849a1ff3449a3c06585571c17439ecff9025` (unchanged)  
**Changed files:** none  
**Git write:** none  
**Publication / deployment / leftover recovery / logical-whole closure:** not claimed  
**Report justification:** `final-acceptance`  
**Logical-whole closure:** not-closed

### Identity gates

Canonical checkout `/home/agile/Projects/framenest` on `feat/repeatable-immutable-nuc-release-deployment-contract`.  
`HEAD` `43c9849a1ff3449a3c06585571c17439ecff9025`; parent `d963df7dfc7d56c75f3696e8bc3830ee81a98534`; tree `df98c395cc4d88cd8b37a92f854f79a245b0facd`.  
`.ap` gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`.  
Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Canonical interpreter CPython `3.13.9` at `/home/agile/Projects/framenest/.venv/bin/python` under `env -i` (AppImage `LD_LIBRARY_PATH`/`PYTHONHOME` cleared). `.venv` was not reconstructed. `uv` was not invoked.

### Allowlist-diff results

`git diff --name-status 4b04b86e4ea52c673c41624e3f2abe1e59d45907 43c9849a1ff3449a3c06585571c17439ecff9025` equals the frozen 15-path allowlist exactly (8 modified, 7 added). No extra path:

- `M` `AGENTS.md` `PRODUCT.md` `README.md` `ROADMAP.md` `SERVER.md` `deploy/ubuntu/README.md` `docs/NUC_HOST_BASELINE.md` `docs/UBUNTU_NUC_DEPLOYMENT.md` `docs/adr/README.md`
- `A` `deploy/ubuntu/framenest-release` `deploy/ubuntu/framenest_release.py` `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md` `tests/contract/test_nuc_release_docs.py` `tests/contract/test_nuc_release_remote_contract.py` `tests/contract/test_nuc_release_source_contract.py`

`git diff --name-status d963df7dfc7d56c75f3696e8bc3830ee81a98534 43c9849a1ff3449a3c06585571c17439ecff9025` equals the frozen four-path correction allowlist exactly (`4 files changed, 192 insertions(+), 3 deletions(-)`). No extra path:

- `M` `deploy/ubuntu/framenest_release.py`
- `M` `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`
- `M` `tests/contract/test_nuc_release_remote_contract.py`
- `M` `tests/contract/test_nuc_release_source_contract.py`

Ubuntu runbook was not in the correction diff.

### Public-main readback

Credential-free `git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` → `d963df7dfc7d56c75f3696e8bc3830ee81a98534	refs/heads/main`. Unpublished successor `43c9849…` is expected. This candidate cannot pass its own public-main gate until a separately authorized republication.

Worker 16 is host-finding context only. Worker 17 is a correction claim only; candidate files and this session’s parse/`engine.main`/local rewrite/FakeRunner evidence outrank that prose.

### Frozen claim verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Diff `4b04b86…` → `43c9849…` contains only the 15-path allowlist | **confirmed** |
| 2 | Diff `d963df7…` → `43c9849…` contains only the four-path correction allowlist | **confirmed** |
| 3 | Public CLI remains `status` / `check --release <40-hex>` / `deploy --release <40-hex> --yes` / `rollback --release <40-hex> --yes`; check/status never deploy; deploy/rollback refuse without `--yes` | **confirmed** (parser choices exactly `{status,check,deploy,rollback,_remote}`; independent `engine.main(["deploy"|"rollback", "--release", <40-hex>])` returns `EXIT_USAGE` 2 with a boom runner that is never called; FakeRunner `check` creates no `/run/framenest-release-deploy` and does not run install/relocate) |
| 4 | `framenest-release` is the sole Fish entry; no `uv` on the routine path; stdlib engine; exact NUC Poetry/CPython paths unchanged | **confirmed** (mode `755`; `command "$python" "$engine" $argv` only; `uv ` absent from Fish entry and from engine command strings; `POETRY_BIN` / `CPYTHON_BIN` unchanged) |
| 5 | Nested private extract remains `_remote _remote-extract`; top-level `_remote-extract` still fails to parse | **confirmed** (ACCEPT-03-F01 stays verified-closed) |
| 6 | DEPLOY-07-F01 SHA-only current tree is readable; helper does not synthesize a host manifest on an old tree; new releases still write both markers | **confirmed** |
| 7 | DEPLOY-07-F02 `verify_clean_worktrees` uses `--untracked-files=no`; tracked dirty still `EXIT_SOURCE_GATE`; ADR silence on untracked remains residual | **confirmed** |
| 8 | DEPLOY-11-F01/F02 poetry.toml and markers remain stdin `cat`; payloads are not nested inside `shlex.quote`/`sh -c`; `_cmd_deploy` still passes six stdin payloads | **confirmed** |
| 9 | DEPLOY-16-F01 closed only if install → shebang relocate → chown/chmod → markers → rename → `framenest-db status` on the final path; nested relocate argv; top-level relocate invalid; rewrite staging→final venv python, not `CPYTHON_BIN`; fail-closed; no post-rename install; db-status not moved before rename | **confirmed** (DEPLOY-16-F01 **verified-closed**) |
| 10 | ADR-0060 states console-script shebangs are rewritten from the staging prefix to the final release prefix before the tree is made non-writable; Ubuntu runbook was not required to expand | **confirmed** |
| 11 | Worker 05 SHA/public-main/AP-pin/archive-member/immutable-release/atomic-cutover/same-schema/no-migrate/backup-checkpoint/rollback-distinct/SSH-options/sanitized-output/no-canonical-checkout-mutation/no-hidden-product-scope remain true except where this envelope’s claims 8–10 change remote write/shebang preparation | **confirmed** |
| 12 | Worker 17 tests/local reconstruction are claims, not independent proof; live leftover `/run/framenest-release-deploy` and unpublished `/opt/framenest/releases/d963df7…` are out of scope and were not converted into acceptance-PASS or deleted | **confirmed** (this session re-probed independently; no SSH) |

### Prior closed findings

**FN-NUC-RELEASE-ACCEPT-03-F01 — verified-closed.**  
Emitted extract command is `sudo -n python3 <engine> _remote _remote-extract --archive … --destination …`. Remaining argv parses as `command=_remote remote_command=_remote-extract`. Independent `engine.main` of that remaining argv returned `EXIT_OK` 0 and extracted `pyproject.toml` / `poetry.lock`. Top-level `_remote-extract` remains invalid parser input (`invalid choice: '_remote-extract'`, `SystemExit` 2).

**FN-NUC-RELEASE-DEPLOY-07-F01 — verified-closed.**  
Independent SHA-only FakeRunner: marker probe returns `sha`; status exit `0`; stdout includes `release_manifest: absent` and the SHA from `.framenest-release-sha` only. No `sudo -n cat` of the manifest, no host write, no mkdir of `/run/framenest-release-deploy`. Probe mentions the manifest filename only in `test -e` classification. Happy-path deploy still writes both staging markers via stdin before rename (indices 46 and 47).

**FN-NUC-RELEASE-DEPLOY-07-F02 — verified-closed.**  
`verify_clean_worktrees` issues `git status --porcelain --untracked-files=no` on the superproject and `.ap`. Untracked-only porcelain is ignored. Tracked dirty (` M AGENTS.md`) still raises `EXIT_SOURCE_GATE` 3. ADR-0060 still does not mention untracked files (parked residual).

**FN-NUC-RELEASE-DEPLOY-11-F01 — verified-closed.**  
`cmd_remote_write_poetry_toml` is `sudo -n sh -c 'umask 077; cat > <staging>/poetry.toml'`. `POETRY_TOML` / `in-project` are absent from the command string. FakeRunner deploy carries the 32-byte poetry.toml body as stdin.

**FN-NUC-RELEASE-DEPLOY-11-F02 — verified-closed.**  
Marker builders are the same stdin `cat` form. Manifest JSON is not in the SSH command string. SHA payload bytes `40-hex + newline` travel as stdin and are not nested as a quoted body (the 40-hex appears only as the destination path component, which is required). `_cmd_deploy` FakeRunner records exactly six stdin payloads: engine, superproject archive, AP archive, poetry.toml, manifest, SHA.

### Finding under re-acceptance

**FN-NUC-RELEASE-DEPLOY-16-F01 — verified-closed.**

Independent FakeRunner `_cmd_deploy` SSH indices (not Worker 17 pytest):

```text
poetry install --only main          41
_remote-relocate-venv-shebangs      43
chown -R root:root                  44
chmod -R a-w                        45
cat > …staging/…-manifest.json      46
cat > …staging/…-release-sha        47
mv staging → final                  48
framenest-db status on final path   49
```

Order is poetry install → shebang relocate → chown/chmod → markers → rename → `framenest-db status` on the final path. One `poetry install --only main`, none after rename. No `framenest-db status` against the final path before rename. Relocate is before chmod.

Emitted relocate command:

```text
sudo -n python3 <engine> _remote _remote-relocate-venv-shebangs --staging <staging> --final <final>
```

Remaining argv parses as `command=_remote remote_command=_remote-relocate-venv-shebangs`. Top-level `_remote-relocate-venv-shebangs` remains invalid (`SystemExit` 2). Relocate argv does not name `CPYTHON_BIN`.

Independent local rewrite under `/tmp/fn-reaccept-18-jRgAuV/` (owned, removed after use; `RELEASE_ROOT` pointed at that temp tree only; no SSH, sudo, or `/opt` mutation). Direct `relocate_venv_shebangs` and `engine.main` of the nested remaining argv both rewrote:

```text
#!<staging>/.venv/bin/python  →  #!<final>/.venv/bin/python
```

`.staging` was absent from `framenest-db` and `framenest-backup` afterward. First lines are `#!<final>/.venv/bin/python`, not `CPYTHON_BIN`. A sibling shebang without the staging prefix was unchanged. Fail-closed: `.venv/bin` present and zero rewritten shebangs → `EXIT_POETRY` (`venv shebangs were not relocated`). Fail-closed: required console script still containing `.staging` after rewrite → `EXIT_POETRY` (`console script still names staging path`).

ADR-0060 now states that console-script shebangs are rewritten from the staging prefix to the final release prefix before the tree is made non-writable.

Worker 16 leftover `/run/framenest-release-deploy` and unpublished `/opt/framenest/releases/d963df7…` were not contacted, not treated as a rollback target, and not deleted.

### Independent shebang-rewrite evidence (summary)

- Nested relocate argv present and parser-accepted; top-level relocate rejected.
- Local temp-tree rewrite of `framenest-db` / `framenest-backup` to `#!<final>/.venv/bin/python`.
- `.staging` gone from those files; `CPYTHON_BIN` never used as the shebang target.
- Fail-closed on zero rewrites and on leftover `.staging` in required scripts.
- Deploy sequence relocates after `poetry install` and before `chmod -R a-w` / rename / final-path `framenest-db status`.

### Tests (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gates not piped)

Focused:

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
64 passed in 0.11s
exit 0
```

Affected:

```text
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_production_ai_deployment.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_ap_project_contract.py
110 passed, 2 skipped in 0.18s
exit 0
```

Skipped nodes: `test_ap_project_contract.py` `AP_OPERATION`-absent skips (2). Full Python suite, JS/browser suites, SSH, sudo, and NUC contact were not run. Worker 17 pytest is not used as independent proof; this session re-ran the selected gates after independent source/parse/temp-tree probes.

### Residuals (parked; do not falsify a frozen claim)

- `subprocess_runner` still discards stderr and maps SSH failure to opaque `EXIT_TRANSPORT` `command failed`.
- `_assert_logs_sanitized` still scans four tokens (`/etc/framenest/credentials`, `Authorization:`, `Bearer `, `BEGIN `).
- On rollback-failure, stderr is `rollback failed`; the first causal error remains in `__cause__`.
- No focused negative pytest node for `deploy` without `--yes` (source and this session’s `engine.main` probe still refuse with `EXIT_USAGE` 2 before any runner call).
- ADR-0060 remains silent on untracked files while `verify_clean_worktrees` uses `--untracked-files=no`.

### One smallest next step

Orchestrator should take accepted unpublished candidate `43c9849a1ff3449a3c06585571c17439ecff9025` to republication of this SHA. Do **not** deploy this SHA yet. Do **not** recover `/run/framenest-release-deploy` or the unpublished `/opt/framenest/releases/d963df7…` tree in this step. This Worker must not publish, deploy, recover leftover lock/unpublished-tree state, correct, or close the logical whole.

### Resolved Execution Issues / Near-Misses

- Inherited Cursor AppImage `LD_LIBRARY_PATH` makes unsanitized `/home/agile/Projects/framenest/.venv/bin/python` fail with `No module named 'encodings'`. All probes and pytest ran under `env -i`. `.venv` was not reconstructed.
- First stdin/SHA-only probe over-matched: destination paths contain the 40-hex SHA, and the SHA-only marker probe script mentions the manifest filename in `test -e`. Refined probe showed payload bytes are not in the command string, and SHA-only status never `cat`s or writes a manifest.
- First deploy-order index used the first SSH mention of `.framenest-release-manifest.json` (check-path read at index 14). Refined predicate `cat >` + staging path + stdin payload located writes at 46/47, after chmod and before rename.
- Owned probe directory `/tmp/fn-reaccept-18-jRgAuV` was removed after use (`PROBE_CLEANED`).
- Meta `18_report_00.md` was not written (no archival grant; trace archival owner is Cooperator Michal).

### Pre-Existing Failure Classification

none for this envelope. Selected focused and affected gates exited 0. Live test-NUC leftover lock and unpublished `d963df7…` tree remain Worker 16 host recovery material, out of scope, and are not a rollback target. Environment: Worker shell requires `env -i` to clear AppImage library pollution; that is an environment fact, not a candidate defect.

Authority expiry: all Worker 18 exchange 01 independent re-acceptance authority expires at this terminal report.
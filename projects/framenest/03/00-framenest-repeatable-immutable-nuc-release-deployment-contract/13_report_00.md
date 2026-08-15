### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `13`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: Fresh Independent Re-Audit  
Phase: acceptance  
Task identity: `FN-NUC-RELEASE-REACCEPT-13`

**PASS** | **acceptance-PASS**

This chat did not implement, correct, accept, publish, or deploy `2d995bb…`, `011823a9…`, `de580f6f…`, or `d963df7…`. Role: WORKER session 13 exchange 01; sequential independent re-acceptance only. Worker 12 tests and reconstruction were treated as claims, not proof.

**Start/end commit:** `d963df7dfc7d56c75f3696e8bc3830ee81a98534` → `d963df7dfc7d56c75f3696e8bc3830ee81a98534` (unchanged; no mutation)  
**Parent:** `de580f6f9d18cddbc4ad7894d163a361b30ef05f`  
**Whole-logical-whole parent:** `4b04b86e4ea52c673c41624e3f2abe1e59d45907` (ancestor)  
**Branch:** `feat/repeatable-immutable-nuc-release-deployment-contract`  
**AP pin:** gitlink and `.ap` `HEAD` = `17b7e085139e9bcbb0e4953d26aef9b6687d541c`  
**Changed files:** none  
**Git write / push / NUC / SSH / Meta / AP mutation:** none  
**Interpreter:** `/home/agile/Projects/framenest/.venv/bin/python` (CPython 3.13.9, sanitized `env -i`)

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `de580f6f9d18cddbc4ad7894d163a361b30ef05f	refs/heads/main`. Unpublished successor, as expected.

**Allowlist diffs.**  
`git diff --name-status 4b04b86e4ea52c673c41624e3f2abe1e59d45907 d963df7dfc7d56c75f3696e8bc3830ee81a98534` equals the frozen 15-path allowlist exactly (8 modified, 7 added). No extra path.  
`git diff --name-status de580f6f9d18cddbc4ad7894d163a361b30ef05f d963df7dfc7d56c75f3696e8bc3830ee81a98534` equals the frozen two-path correction allowlist exactly: `deploy/ubuntu/framenest_release.py`, `tests/contract/test_nuc_release_remote_contract.py` (`2 files changed, 97 insertions(+), 17 deletions(-)`). No extra path.

Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Owned probe `/tmp/fn-reaccept-13-rtZBdN` removed after capture.

### Frozen claim verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Diff `4b04b86…` → `d963df7…` is only the 15-path allowlist | **confirmed** |
| 2 | Diff `de580f6f…` → `d963df7…` is only the two-path correction allowlist | **confirmed** |
| 3 | Public CLI remains `status` / `check --release <40-hex>` / `deploy --release <40-hex> --yes` / `rollback --release <40-hex> --yes`; check/status never deploy; deploy/rollback refuse without `--yes` | **confirmed** (top parser choices `{_remote, check, deploy, rollback, status}`; independent `engine.main(["deploy"|"rollback", "--release", <40-hex>])` with a boom runner returns `EXIT_USAGE` 2 and never calls the runner; FakeRunner `check` does not `mkdir` `/run/framenest-release-deploy`) |
| 4 | `framenest-release` is the sole Fish entry; no `uv` on the routine path; stdlib engine; exact NUC Poetry/CPython paths unchanged | **confirmed** (mode `755`; `command "$python" "$engine" $argv` only; `uv` absent from the Fish wrapper and from engine source except the docstring prohibition; `POETRY_BIN` / `CPYTHON_BIN` exact) |
| 5 | Nested private extract remains `_remote _remote-extract`; top-level `_remote-extract` still fails to parse | **confirmed** (ACCEPT-03-F01 stays verified-closed) |
| 6 | SHA-only current tree is readable; helper does not synthesize a host manifest on an old tree; new releases still write both markers | **confirmed** (DEPLOY-07-F01 stays verified-closed) |
| 7 | `verify_clean_worktrees` uses `--untracked-files=no`; tracked dirty still `EXIT_SOURCE_GATE` | **confirmed** (DEPLOY-07-F02 stays verified-closed) |
| 8 | `cmd_remote_write_poetry_toml` is path-quoted stdin `cat`; `POETRY_TOML` / `in-project` absent from the command string; `_cmd_deploy` passes `POETRY_TOML.encode("utf-8")`; local reconstruction writes exact bytes; nested `printf %s` + `shlex.quote(payload)` gone | **confirmed** (DEPLOY-11-F01 verified-closed) |
| 9 | `cmd_remote_write_markers` returns two stdin-cat commands with no payload arguments; manifest JSON absent from those strings; `printf %s` absent; `_cmd_deploy` passes exact manifest JSON bytes then `release_sha + "\n"`; local reconstruction writes exact bytes | **confirmed** (DEPLOY-11-F02 verified-closed) |
| 10 | `cmd_remote_write_file` remains stdin/`cat` + remote `sha256`; not rewritten as nested quoted `printf`; shared `cmd_remote_cat_stdin` is present for poetry/markers only | **confirmed** |
| 11 | Happy-path FakeRunner deploy reaches poetry.toml then both markers then rename; stdin payload count is six with exact bytes | **confirmed** |
| 12 | Worker 05 SHA/public-main/AP-pin/archive-member/immutable-release/atomic-cutover/same-schema/no-migrate/backup-checkpoint/rollback-distinct/SSH-options/sanitized-output/no-canonical-checkout-mutation/no-hidden-product-scope claims remain true except the remote write path in claims 8–11 | **confirmed** |
| 13 | Worker 12 tests/reconstruction are claims, not independent proof; live NUC leftover lock/staging are out of scope | **confirmed** (this session re-probed builders, wiring, and local stdin reconstruction independently; no SSH; leftovers not deleted and not used as acceptance-PASS) |

### Finding verdicts

**FN-NUC-RELEASE-ACCEPT-03-F01:** **verified-closed**  
Independent extract (temp tree only; `REMOTE_DEPLOY_DIR` / `RELEASE_ROOT` retargeted for `validate_remote_path`; no SSH/sudo/host path):

```text
sudo -n python3 <engine> _remote _remote-extract --archive … --destination …
PARSE_OK command=_remote remote_command=_remote-extract
engine.main remaining argv → EXIT_OK 0; pyproject.toml and poetry.lock extracted
```

Top-level `_remote-extract` is still an invalid choice (`SystemExit` 2; choices remain `status, check, deploy, rollback, _remote`).

**FN-NUC-RELEASE-DEPLOY-07-F01:** **verified-closed**  
Independent SHA-only status runner: probe returns `sha`; `cat` of `.framenest-release-sha` only; no manifest `cat`; no host manifest write; no lock `mkdir`. `engine.main(["status", …])` → `EXIT_OK` 0, `active_release` from the SHA marker, `release_manifest: absent`. `_cmd_deploy` still writes both `.framenest-release-manifest.json` and `.framenest-release-sha` via stdin-cat before rename.

**FN-NUC-RELEASE-DEPLOY-07-F02:** **verified-closed**  
Recorded argv:

```text
git status --porcelain --untracked-files=no
git -C .ap status --porcelain --untracked-files=no
```

Tracked dirty (` M AGENTS.md`) raises `EXIT_SOURCE_GATE` 3. ADR silence on untracked remains a parked residual, not automatic FAIL.

**FN-NUC-RELEASE-DEPLOY-11-F01:** **verified-closed**  
Builder (no payload in the command string):

```text
sudo -n sh -c 'umask 077; cat > /opt/framenest/releases/d963df7dfc7d56c75f3696e8bc3830ee81a98534.staging/poetry.toml'
```

`POETRY_TOML` / `in-project` / `printf %s` absent. Signature is `(release_path: str)`. `_cmd_deploy` passes `input_bytes=POETRY_TOML.encode("utf-8")`. Local `sh -c` of the inner script `umask 077; cat > <path>` with those stdin bytes wrote exact `b'[virtualenvs]\nin-project = true\n'` (`poetry_bytes_match True`). Parent `de580f6f…` still contains `printf %s {shlex.quote(POETRY_TOML)}`; candidate does not.

**FN-NUC-RELEASE-DEPLOY-11-F02:** **verified-closed**  
Builders (no payload arguments; `printf %s` absent; manifest JSON absent):

```text
sudo -n sh -c 'umask 077; cat > …/.framenest-release-manifest.json'
sudo -n sh -c 'umask 077; cat > …/.framenest-release-sha'
```

`_cmd_deploy` passes `manifest_json.encode("utf-8")` then `(release_sha + "\n").encode("utf-8")`. Local reconstruction wrote those exact bytes (`manifest_match True`, `sha_match True`, SHA file ends with newline). Parent still took `(release_path, manifest_json, release_sha)` and nested `printf %s`.

The 40-hex SHA substring appears in real staging destination paths (`/opt/framenest/releases/<sha>.staging/…`). That is release-directory identity, not nested payload quoting. Manifest JSON bytes and SHA-file payload (`sha + "\n"`) are not in the command strings.

**`cmd_remote_write_file`:** unchanged stdin/`cat` + remote `sha256sum` equality test; `printf %s` absent. Shared `cmd_remote_cat_stdin` is used only for poetry.toml and markers.

**FakeRunner deploy (independent of pytest):** `EXIT_OK` 0. Write order `engine < superproject.tar < ap.tar < poetry.toml < manifest < SHA < rename`. Stdin payload count **6**; poetry bytes exact `POETRY_TOML`; SHA bytes exact `RELEASE + "\n"`; manifest JSON `framenest_release_sha` equals `RELEASE`; those payloads are not in the SSH command strings.

### Tests (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gates not piped)

Focused:

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
```

**61 passed**, exit **0**.

Affected:

```text
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_production_ai_deployment.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_ap_project_contract.py
```

**110 passed, 2 skipped**, exit **0**. Skips: `AP_OPERATION is absent; not running inside an AP operation`. No full suite.

### Residuals (parked; do not falsify a frozen claim)

- `EXIT_TRANSPORT` stderr discard (Worker 11 opaque `command failed`)
- log-sanitizer token set
- rollback stderr phrasing
- missing deploy-without-`--yes` pytest (engine behavior independently confirmed: `EXIT_USAGE` 2)
- ADR silence on untracked
- Live NUC leftover `/run/framenest-release-deploy` and `de580f6f….staging` remain out of scope

Publication, deployment, lock/staging recovery, and logical-whole closure are **not claimed**.

**One smallest next step.** Republication of `d963df7dfc7d56c75f3696e8bc3830ee81a98534`. Do not deploy. Do not recover leftover lock/staging yet.

**Report justification:** `final-acceptance`  
**Logical-whole closure:** not-closed

### Resolved Execution Issues / Near-Misses

- Literal 40-hex SHA appears in destination paths of marker/poetry commands because releases live under `/opt/framenest/releases/<sha>`. Classified as path identity, not payload-in-command-string; F02 remains verified-closed.
- First write-order scan matched check-path marker *reads*; corrected by matching `cat >` writes. Probe error, not a candidate defect.
- Unsanitized Cursor/AppImage `python -c` after probes failed (`encodings` / platform libraries). Evidence commands used `env -i`. Environment defect of the host shell, not a candidate defect.
- argparse printed usage to stderr during the expected top-level `_remote-extract` `SystemExit` 2 probe.

### Pre-Existing Failure Classification

Public `refs/heads/main` remains `de580f6f…`. Candidate `d963df7…` is an unpublished successor. Worker 11 leftover remote lock/staging was not inspected, not deleted, and not used as acceptance evidence. Parked residuals listed above are unchanged and out of this grant.

**Authority expiry:** all Worker 13 exchange 01 re-acceptance authority expires at this terminal report.
### Report for ORCHESTRATOR_CHAT

Logical whole identity: `framenest-repeatable-immutable-nuc-release-deployment-contract`  
Worker session ordinal: `23`  
Worker exchange ordinal: `01`  
Worker session target: `fresh-worker-session`  
Worker session profile: Fresh Independent Re-Audit  
Phase: acceptance  
Task identity: `FN-NUC-RELEASE-REACCEPT-23`

**PASS** | **acceptance-PASS**  
Independent acceptance: **this exchange**  
Publication / deployment / leftover recovery / logical-whole closure: **not claimed**

This chat did not implement, correct, accept, publish, recover leftover state, or deploy `2d995bb…`, `011823a9…`, `de580f6f…`, `d963df7…`, `43c9849…`, or `f5fbdce…`. Role is WORKER session 23 exchange 01. No correction, Git write, Meta/AP mutation, SSH/NUC, leftover-lock deletion, unpublished-tree recovery, publication, deploy, or whole closure.

**Artifact:** `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`  
**Accepted tree:** `1d22f690101f9d239207fa80ac89fc473c1c9894`  
**Parent:** `43c9849a1ff3449a3c06585571c17439ecff9025`  
**Whole-logical-whole parent:** `4b04b86e4ea52c673c41624e3f2abe1e59d45907`  
**Branch:** `feat/repeatable-immutable-nuc-release-deployment-contract`  
**AP pin / `.ap` gitlink / `.ap` HEAD:** `17b7e085139e9bcbb0e4953d26aef9b6687d541c`  
**Git write:** none  
**Report justification:** `final-acceptance`  
**Logical-whole closure:** not-closed

**Public-main readback (credential-free).**  
`git ls-remote https://github.com/cisarik/framenest.git refs/heads/main` = `43c9849a1ff3449a3c06585571c17439ecff9025	refs/heads/main` (unpublished successor expected).

**Local HEAD / cleanliness.**  
Canonical checkout `/home/agile/Projects/framenest`. Tracked tree clean. Owner untracked paths preserved (`.accept-immut-work/`, `.playwright-mcp/`, `.w6-immut-work/`, `REPRO_DIR=/`, `uv.lock`). Canonical interpreter CPython `3.13.9` at `/home/agile/Projects/framenest/.venv/bin/python` under sanitized `env -i`. `.venv` was not reconstructed. `uv` was not invoked.

**Allowlist diffs.**

`4b04b86e4ea52c673c41624e3f2abe1e59d45907` → `f5fbdce5669997f15c28ed6ffdad4cda849df4ee` (exactly the frozen 15 paths):

```text
M  AGENTS.md
M  PRODUCT.md
M  README.md
M  ROADMAP.md
M  SERVER.md
M  deploy/ubuntu/README.md
A  deploy/ubuntu/framenest-release
A  deploy/ubuntu/framenest_release.py
M  docs/NUC_HOST_BASELINE.md
M  docs/UBUNTU_NUC_DEPLOYMENT.md
A  docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
M  docs/adr/README.md
A  tests/contract/test_nuc_release_docs.py
A  tests/contract/test_nuc_release_remote_contract.py
A  tests/contract/test_nuc_release_source_contract.py
```

`43c9849a1ff3449a3c06585571c17439ecff9025` → `f5fbdce5669997f15c28ed6ffdad4cda849df4ee` (exactly the frozen three-path correction allowlist):

```text
M  deploy/ubuntu/framenest_release.py
M  docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
M  tests/contract/test_nuc_release_source_contract.py
```

`tests/contract/test_nuc_release_remote_contract.py` was authorized for the correction and is unchanged.

**Frozen-claim verdicts (candidate files; Worker 22 prose was not treated as proof).**

1. 15-path allowlist vs `4b04b86…`: **confirmed**  
2. Three-path correction allowlist vs `43c9849…`: **confirmed**  
3. Public CLI `status` / `check --release <40-hex>` / `deploy --release <40-hex> --yes` / `rollback --release <40-hex> --yes`; check/status never deploy; deploy/rollback refuse without `--yes`: **confirmed** (parser choices; `_cmd_check`/`_cmd_status` contain no poetry-install/rename/restart; `engine.main(["deploy"|"rollback", "--release", SHA])` returned `EXIT_USAGE` 2 with unused runner)  
4. `deploy/ubuntu/framenest-release` is the sole Fish entry; no `uv` on the routine path; stdlib engine; exact NUC Poetry/CPython paths unchanged: **confirmed**  
5. Nested extract remains `_remote _remote-extract`; nested relocate remains `_remote _remote-relocate-venv-shebangs`; both top-level `_remote-*` verbs remain invalid parser choices (`SystemExit` 2): **confirmed**  
6. SHA-only current tree is readable; helper does not synthesize a host manifest; new releases still write both markers: **confirmed**  
7. `verify_clean_worktrees` uses `--untracked-files=no` on superproject and `.ap`; tracked dirty still `EXIT_SOURCE_GATE`; ADR silence on untracked remains residual: **confirmed**  
8. `poetry.toml` and markers remain stdin `cat`; `_cmd_deploy` still has six `input_bytes=` sites: **confirmed**  
9. `_cmd_deploy` order is poetry install → relocate → chown/chmod → markers → rename → `framenest-db status` on the final path; shebangs name `#!<final>/.venv/bin/python`, not `CPYTHON_BIN`; poetry install is not run after rename: **confirmed**  
10. DEPLOY-21-F01 relocate walks all text files under `<staging>/.venv/` and rewrites staging prefix → final prefix, including `.pth` and `direct_url.json`, with fail-closed leftover `.staging` / zero-rewrite: **confirmed** (independent reconstruction below)  
11. ADR-0060 now states that staging-prefix paths inside the in-project venv (console-script shebangs and editable install metadata such as `.pth` and `direct_url.json`) are rewritten to the final release prefix before the tree is made non-writable. Ubuntu runbook was not expanded in the correction: **confirmed**  
12. Worker 05 SHA / public-main / AP-pin / archive-member / immutable-release / atomic-cutover / same-schema / no-migrate / backup-checkpoint / rollback-distinct / SSH-options / sanitized-output / no-canonical-checkout-mutation / no-hidden-product-scope remain true except where claims 8–11 change remote write/venv preparation: **confirmed** (`framenest_release.py` contains no `migrate` token; `git archive` only; `ln -s` + `mv -T`; `rollback-previous-release` distinct from deploy `previous-release`; SSH `BatchMode=yes` / `IdentitiesOnly=yes`; 15-path envelope)  
13. Worker 22 tests/reconstruction were treated as claims only. Live leftover `/run/framenest-release-deploy` and unpublished `/opt/framenest/releases/43c9849…` were out of scope and were not converted into acceptance-PASS or deleted: **confirmed** (no SSH)

**Prior closed findings.**

| Finding | Verdict |
|---|---|
| FN-NUC-RELEASE-ACCEPT-03-F01 nested `_remote _remote-extract` | **verified-closed** |
| FN-NUC-RELEASE-DEPLOY-07-F01 SHA-only status / no forged host manifest | **verified-closed** (`read_current_release` on probe `sha` returned empty `manifest_raw` and `{"framenest_release_sha": …}` with zero writes; `status` printed `release_manifest: absent`) |
| FN-NUC-RELEASE-DEPLOY-07-F02 `--untracked-files=no` | **verified-closed** |
| FN-NUC-RELEASE-DEPLOY-11-F01 poetry.toml stdin write | **verified-closed** |
| FN-NUC-RELEASE-DEPLOY-11-F02 marker stdin write | **verified-closed** |
| FN-NUC-RELEASE-DEPLOY-16-F01 staging-path Poetry shebangs after `mv` | **verified-closed** |

**Finding under re-acceptance: FN-NUC-RELEASE-DEPLOY-21-F01**  
**verified-closed** (independent local reconstruction; not Worker 22 pytest).

`relocate_venv_shebangs` walks `Path(staging)/.venv` with `rglob("*")`, skips non-text/symlinks, replaces `staging_path` with `final_path`, then fail-closes if `rewritten == 0`, if required console scripts still contain `.staging` or do not start with `#!{final}/.venv/bin/python`, or if any `.pth` / `direct_url.json` under `.venv` still contains `.staging`. Nested builder remains `sudo -n python3 <engine> _remote _remote-relocate-venv-shebangs --staging … --final …`. `--no-editable`, wheel, and pip were not invented. `poetry install --only main` remains the single install, on staging, before relocate.

Independent temp-tree rewrite (sanitized interpreter; `RELEASE_ROOT` monkeypatched; no SSH):

```text
shebang-db:     #!<final>/.venv/bin/python
shebang-backup: #!<final>/.venv/bin/python
pth:            <final>/src
direct_url:     {"url": "file://<final>", "dir_info": {"editable": true}}
```

`.staging` was absent from those files afterward. `CPYTHON_BIN` was absent from the shebangs. A sibling file without the staging prefix was unchanged. Fail-closed `EXIT_POETRY` fired for leftover `.pth` `.staging`, leftover `direct_url.json` `.staging`, and zero staging-prefix rewrites.

**Selected tests** (sanitized `env -i`; canonical `.venv` Python 3.13.9; `-p no:cacheprovider`; gates not piped).

Focused, once:

```text
tests/contract/test_nuc_release_source_contract.py
tests/contract/test_nuc_release_remote_contract.py
tests/contract/test_nuc_release_docs.py
```

**67 passed**, exit **0**.

Affected, once:

```text
tests/contract/test_nuc_operator_runbook.py
tests/contract/test_production_ai_deployment.py
tests/contract/test_fedora_systemd_service.py
tests/contract/test_ap_project_contract.py
```

**110 passed, 2 skipped**, exit **0**. Skips are `AP_OPERATION is absent` in `test_ap_project_contract.py` (expected for the authorized direct pytest, not `ap exec`).

No full suite. No SSH/NUC.

**Parked residuals (unchanged; do not falsify a frozen claim).**  
EXIT_TRANSPORT stderr discard; log-sanitizer tokens; rollback stderr phrasing; missing deploy-without-`--yes` pytest node; ADR silence on untracked files. Host leftover `/run/framenest-release-deploy` and unpublished `/opt/framenest/releases/43c9849a1ff3449a3c06585571c17439ecff9025` remain later recovery material and are not a rollback target.

**Next step.** Republication of `f5fbdce5669997f15c28ed6ffdad4cda849df4ee`. Not deploy. Not lock/unpublished-tree recovery yet.

### Resolved Execution Issues / Near-Misses

- Independence held: this session did not implement or correct the candidate.  
- One probe-script assertion looked for the contiguous phrase `never runs migrations` and failed on the engine docstring line break; the candidate still does not invoke migrate (`migrate` is absent from `framenest_release.py`). Not a candidate defect.  
- Top-level invalid `_remote-*` probes printed argparse usage to stderr, as expected for `SystemExit` 2.  
- Affected suite skip of two AP-envelope tests is an authorized-invocation fact, not a candidate defect.  
- Cursor/AppImage `LD_LIBRARY_PATH` / `PYTHONHOME` require `env -i`; environment fact, not a candidate defect.  
- Temporary probe script under `/tmp` was removed. Repository untracked owner paths were not touched. Meta was not archived.

### Pre-Existing Failure Classification

Accepted finding `FN-NUC-RELEASE-DEPLOY-21-F01` is independently verified-closed on local reconstruction of `f5fbdce…`. Prior closed findings remain closed. Parked residuals listed above remain parked. Worker 21 leftover lock and unpublished `43c9849…` tree remain later recovery/deploy material; this Worker did not observe the host. Public `refs/heads/main` remains `43c9849…`.

Authority expiry: all Worker 23 exchange 01 re-acceptance authority expires at this terminal report.
### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-sole-identity
Worker session ordinal: 59
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C8RELOC
status: PASS
Phase-qualified result: not-applicable
Start commit: 90766ca04358af876a7fb154c44fb005612d34ad
End commit: 7c1ea48be1176cd454f0ce6a97dc09d32d543838
Report justification: new-mutation
Logical-whole closure: not-closed

Gates at start matched the prompt. Branch `main`, HEAD `90766ca04358af876a7fb154c44fb005612d34ad`, clean tree, `.ap` gitlink and submodule HEAD `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `./.ap/ap doctor` PASS, governing variant stable. Local `origin/main` was `c0f456656c9930810e11d13e1d4684efdb3ee4ff`. Fetch was not run. `ap project check --baseline 90766ca…` PASS. Runtime probe reported `.venv/bin/python`, CPython 3.13.9, provenance `src/kronika/__init__.py`.

Changed files: `deploy/ubuntu/kronika_release.py` now takes an explicit required-script sequence, defaulting to the web pair, and the capture publish passes the basename of `plan.executable`. `tests/contract/test_nuc_release_source_contract.py`, `tests/contract/test_nuc_release_remote_contract.py`, and `tests/contract/test_kronika_capture_services.py` pin that behavior. Non-obvious module, named before editing: `tests/contract/test_kronika_identity_migration.py`, and only to pin that the identity-migration caller still emits the unflagged command. No retention re-pin. No push.

## 1. Reproduced defect shape and post-fix matrix

Before editing, `relocate_venv_shebangs` required exactly `kronika-db` and `kronika-backup`. A synthetic capture venv whose only console script was `kronika-capture` raised `required console script is missing` with `EXIT_POETRY` (14). A synthetic web venv with both scripts passed and its shebangs were rewritten to the final interpreter. That reproducer was 2 passed in 0.25s, then removed. It was not a repository test.

Pre-edit callers of `cmd_remote_relocate_venv_shebangs`, all three-argument:

| Caller | Pre-edit line | What the text is |
|---|---:|---|
| `RemoteMigrationHost.prepare_release_environment` | 3723 | Identity-migration web preparation. The prompt's "routine web deploy" locator points here. |
| `_publish_capture_release` | 5536 | Capture-path publish. |
| `_cmd_deploy` | 6203 | Routine web deploy. This caller was not the line the prompt named. |

Post-fix:

| Surface | Result |
|---|---|
| Routine deploy | The emitted command equals the three-argument helper and contains no `--required-script`. Pinned in `test_deploy_happy_path_sequence` and, as a literal baseline string, in `test_cmd_remote_relocate_venv_shebangs_emits_nested_private_argv`. Neither web call site was edited. |
| Identity-migration preparation | The emitted command ends with the same three-argument helper and has no flag. Pinned in `test_production_prepare_release_environment_builds_at_the_new_path`. |
| Capture publish | Exactly one flag, `--required-script kronika-capture`, from `PurePosixPath(plan.executable).name`. The publish source contains that derivation and does not contain a `kronika-capture` literal. Pinned in `test_apply_preserves_the_release_and_bounds_the_service_cycle`. |
| Function, requested script | A venv with only `kronika-capture` is accepted when that name is requested, and the shebang becomes `#!{final}/.venv/bin/python`. |
| Function, missing script | A venv that rewrites another file and lacks the requested script raises `required console script is missing` after that rewrite. The omitted argument still requires the web pair, so a backup-only venv fails the same way. |
| Function, invalid name | `""`, `../kronika-capture`, `kronika/capture`, `kronika capture`, `-capture`, `.`, and `..` raise `required console script name is invalid` before any rewrite. A bare string is not iterated as characters. |
| Empty sequence | `required_scripts=()` raises `required console script list is empty`. The command builder does the same. `None` remains the unflagged baseline and is not that empty sequence. |
| Other relocation checks | The rewrite loop, the per-script body, and the editable-metadata sweep are unchanged. A capture-script request still raises `editable install metadata still names staging path` when a `.pth` keeps another staging prefix. |

An absent CLI flag leaves `required_script is None`, and `main` then uses the function default. Repeatable `--required-script` is parsed and enforced: one flag accepts the capture script; capture plus `kronika-backup` on a capture-only venv returns exit 14 and `required console script is missing`.

## 2. Same-class audit

Every helper `_publish_capture_release` invokes was read. The only web-only hardcoded requirement a capture tree cannot satisfy was the console-script pair inside `relocate_venv_shebangs`. That is the fix above.

Reviewed and not hits: `verify_tooling` checks the shared Poetry and CPython binaries; the copy, lock, poetry, ownership, mode, rename, and manifest helpers are path-generic; `_require_preserved_capture_tree` checks marker identity; the executable checks use `CAPTURE_RELEASE_EXECUTABLE` and `plan.executable`, which are the capture script. `cmd_remote_db_status` and the backup command builders are not on this call path. No additional production change.

## 3. Mutation demonstrations

Each mutation was restored before the next one and before the final suites. The restored tree is the committed tree.

| Mutation | Observed failure |
|---|---|
| (a) Drop the capture caller's fourth argument | `test_apply_preserves_the_release_and_bounds_the_service_cycle` failed in 0.18s. The emitted command stopped at `--final <release>` and lacked `--required-script kronika-capture`. |
| (b) Empty the default pair to `()` | `test_relocate_venv_shebangs_requires_the_default_web_scripts` failed in 0.29s. Expected `required console script is missing`; got `required console script list is empty`. |
| (c) Make name validation return immediately | All 7 cases of `test_relocate_venv_shebangs_rejects_an_unsafe_script_name` failed in 0.10s. Expected `required console script name is invalid`; got `required console script is missing`. |

## 4. Suites

Python evidence used `./.ap/ap exec --baseline 90766ca04358af876a7fb154c44fb005612d34ad`. The full suite was `--operation test` with no trailing argv. JavaScript used `node --test` from the worktree root.

| Suite | Result | Elapsed | Baseline difference |
|---|---|---:|---|
| Focused nine modules | 623 passed, 0 failed | 22.06 s | 609 + 14 new tests. No existing test was removed. |
| Full Python | 5013 passed, 8 skipped, 3 warnings, 0 failed | 695.50 s | 4999 + 14. Skips, warnings, and failures unchanged. |
| Retention | 15 passed, 0 failed | 0.35 s | Counts unchanged. No pin edited. |
| `companion_web_bridge` | 23 passed, 0 failed | 79.8 ms | None |
| `companion_review_extension` | 41 passed, 0 failed | 185.4 ms | None |
| `x_companion_extension` | 55 passed, 0 failed | 123.1 ms | None |
| `companion_settings_automatic_analysis` | 6 passed, 0 failed | 10.11 s | None |
| `kronika_ui` | 12 passed, 0 failed | 93.9 ms | None |
| `catalog_card_ai_quick_action` | 30 passed, 0 failed | 217.8 ms | None |
| Bounded `*_frontend`, `*_cockpit`, `gallery_*` glob | 212 passed, 0 failed | 751.9 ms | None |

The nine modules are the session-58 set: `test_kronika_capture_services.py`, `test_chatgpt_page_packaging.py`, `test_nuc_release_remote_contract.py`, `test_nuc_release_source_contract.py`, `test_nuc_release_docs.py`, `test_nuc_operator_runbook.py`, `test_kronika_identity_migration.py`, `test_kronika_cli_and_release_readers.py`, `test_kronika_durable_writer_identities.py`. The prompt's 462 was not attached to a file list; that figure was not reconstructed.

The eight skips are the five real-tool cover cases, two real-tool media-analysis cases, and one NVIDIA smoke case. The three warnings are the existing Pydantic `OMITTED` schema warning.

## 5. Diff, commit, Part A, Part B, Part C

```text
 deploy/ubuntu/kronika_release.py                   |  93 +++++++++++++--
 tests/contract/test_kronika_capture_services.py    |  18 +++
 tests/contract/test_kronika_identity_migration.py  |  11 ++
 tests/contract/test_nuc_release_remote_contract.py |  85 ++++++++++++++
 tests/contract/test_nuc_release_source_contract.py | 126 +++++++++++++++++++++
 5 files changed, 323 insertions(+), 10 deletions(-)
```

Commit: `7c1ea48be1176cd454f0ce6a97dc09d32d543838` on `main`. Parent: `90766ca04358af876a7fb154c44fb005612d34ad`. Working tree clean. Not pushed.

`FROZEN_ALEMBIC_SHA256` has 36 keys, computed by counting the dict entries and by counting the 36 non-cache files in the single `alembic_environment/versions` directory. Part A files are absent from the diff, and the retention hash tests passed. Part B remains the empty set. Part C did not move: the retention assertions recompute the pinned scalars and passed with no ledger edit.

## 6. Sites no test exercises

The production loop still has three failure branches that no production test raises: a required script whose content still contains `.staging`, a required script whose first line is not `#!{final}/.venv/bin/python`, and a symlink standing where the script must be. Those statements were already present and were not given new assertions. The success side of the shebang check is asserted for both the web pair and a requested capture script.

`RemoteBoundary._relocate_venv` in `test_kronika_identity_migration.py` still hardcodes the web pair and does not read `--required-script`. The migration command is pinned to omit the flag, so the double still models that command. It is a test fake, not a host helper.

Consumers this prompt did not name: `_cmd_deploy`, and the migration preparer as a distinct caller from that deploy. Both stay on the unflagged command.

## 7. Deviations, risks, missing evidence, next step

No capture software, unit, state, token, profile, or bridge protocol changed. No document, dependency, Alembic revision, or `.ap` gitlink changed. No NUC contact.

The migration test double will not honor a flag if a later caller adds one. The current migration caller does not add one.

Missing evidence is the live apply. This cut was repository-only by design. The synthetic venv shows the old refusal and the new acceptance; it is not the host.

Smallest next step: Orchestrator acceptance of `7c1ea48`, then the capture-path apply against the unchanged preflight digest `b8c68cb5ce246e7b4a792f9ea31e98b0a7e73fe269b87a2cdaca04fffa2d61ad`.

Resolved Execution Issues / Near-Misses: `ap doctor --root` was rejected because doctor takes no argument; `./.ap/ap doctor` then passed. A first import edit matched `from pathlib import Path` inside embedded remote scripts and was not applied; the module import was updated with a narrower match, and those embedded scripts are unchanged. A broad `find` counted 71 Alembic paths because it included `__pycache__`; the versions directory itself has 36 files.
Pre-Existing Failure Classification: none

Authority expiry: this terminal report ends the grant. No further implementation, second commit, push, publication, refresh, capture action, or host contact is authorized by it.

```text
Orchestration critique:
MEASURED: the prompt's line 3723 is RemoteMigrationHost.prepare_release_environment, while the routine deploy caller is _cmd_deploy, previously at line 6203. Evidence: both function bodies. Effect: two web callers had to stay flag-free, and both are pinned. Smallest correction: none in this result.
LEAD: none
```
### Report for ORCHESTRATOR_CHAT

Logical whole identity: `kronika-sole-identity`
Worker session ordinal: `62`
Worker exchange ordinal: `01`
Persistent role identity: `WORKER`
Task identity: `KSI-IMPL-C9B1`
status: **PASS**
Report justification: `new-mutation`
Phase-qualified result: `not-applicable`
Logical-whole closure: `not-closed`
Start commit: `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`
End commit: `f2c4624ded775e3446bfafef4a5a413253a03136`
Branch: `main` (local only; not pushed)
`FROZEN_ALEMBIC_SHA256`: 35 numbered revision keys plus `versions/__init__.py` = **36**. The retention set-completeness test passed.

Gates at start matched the grant: clean `main` at `5b86d896b3ea03f89fef2c90f7af2c121d0ef915`, public `origin/main` equal, `.ap` gitlink and submodule `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS, `ap project check --baseline 5b86d896b3ea03f89fef2c90f7af2c121d0ef915` PASS. No host contact and no browser.

`61_report_00.md` was not on disk. The session-61 report text was read from the Cursor plan that carries that report header and sections 1–8. The deletion set in this prompt matches that text.

## 1. Deletion inventory and callers

A parse of `deploy/ubuntu/kronika_release.py` before any deletion found **no routine caller** of any deletion candidate. Routine means `status`, `check`, `deploy`, `rollback`, `activate-capture`, `rollback-capture`, `_remote-extract`, `_remote-relocate-venv-shebangs`, the deploy lock, and the readiness checks.

The only callers outside the deletion set were `main` dispatching `_cmd_migrate_identity` and `_cmd_migrate_capture_paths`. Those two branches were removed with the handlers.

`CAPTURE_BRIDGE_UNIT` was **not** deleted. `cmd_remote_restart_capture_bridge` still uses it. It now sits beside `CAPTURE_RUNNER_SERVICE`.

`SYSTEMD_UNIT_SUFFIXES` had three callers, all inside the identity-migration span, so it went with that span. `EXIT_MIGRATION` (27) had callers only in the deleted span and was removed. `EXIT_MIGRATION_REQUIRED` (13) stays. `identity_env.COMPATIBLE_ENVIRONMENT_PREFIX` was not touched. The engine-level constant of the same name was.

Removed top-level names, each with callers only inside this set except the two `main` dispatches above:

- Constants: `COMPATIBLE_ENVIRONMENT_PREFIX`, `MIGRATION_SCRATCH_DIRECTORY`, `MIGRATION_REMOTE_ENGINE`, `SYSTEMD_UNIT_SUFFIXES`, `EXIT_MIGRATION`, `CAPTURE_PATH_LINE_PREFIXES`, `CAPTURE_PATH_PLAN_VERSION`, `CAPTURE_PATH_SCRATCH`, `CAPTURE_PATH_REMOTE_ENGINE`, `CAPTURE_PATH_STOP_UNITS`, `CAPTURE_PATH_START_UNITS`, `CAPTURE_RELEASE_EXECUTABLE`, and the `MIGRATION_*` / `IDENTITY_ENVIRONMENT_PATH_SUFFIXES` / `IDENTITY_ENVIRONMENT_OPAQUE_SUFFIXES` block.
- Transformer: `EnvironmentAssignment`, `EnvironmentTransformation`, `environment_key_suffix`, `classify_environment_key`, `_split_quotes`, `transform_path_value`, `transformed_environment_value`, `parse_environment_text`, `transform_environment_text`, `environment_transformation_is_idempotent`.
- Migration remote builders and orchestration, including `cmd_remote_existence` through `cmd_remote_verify_migration_release`, `ObservedUnit`, `DropinInstallation`, `MigrationObservation`, `MigrationPlan`, `RemoteMigrationHost`, `parse_tailscale_serve_status`, `classify_unit_path_token`, `transform_unit_dropin_text`, `transform_sudoers_text`, `run_migration_apply`, `read_migration_observation`, and the module-level systemd/sudoers tables that lived in that span (`SYSTEMD_DIRECTIVE_LINE`, `SYSTEMD_SECTION_LINE`, `SYSTEMD_EXEC_DIRECTIVES`, `SYSTEMD_PATH_DIRECTIVES`, `SYSTEMD_IDENTITY_DIRECTIVES`, `SYSTEMD_EXEC_PREFIXES`, `SYSTEMD_EXEC_TOKEN`, `SUDOERS_RULE_LINE`, `SUDOERS_TAG`).
- Capture-path migration: `capture_unit_names` through `_cmd_migrate_capture_paths`, including `CapturePathUnit`, `CapturePathPlan`, `observe_capture_path_plan`, `_require_former_capture_pointer`, `_apply_capture_path_plan`, `_remove_capture_path_trees`, `_enforce_capture_path_gates`, `_print_capture_path_plan`.
- CLI: parser entries and handlers for `migrate-identity` and `migrate-capture-paths`.

Method-name collisions such as `executable`, `payload`, `staging_path`, and `changed` in routine code are different identifiers. They were not calls into the deleted classes.

Routine dual-layout selection is still present: `OLD_WEB_LAYOUT`, `NEW_WEB_LAYOUT`, `WEB_LAYOUTS`, `CAPTURE_POINTERS`.

## 2. Retooled tests and the parser-surface test

Keeps were confirmed in other modules before deleting `tests/contract/test_kronika_identity_migration.py`. That file did not pin the marker tables, the Alembic shim, or `refuse_silent_legacy_state_replacement`.

- Marker pins remain in `test_kronika_cli_and_release_readers.py` (`test_every_reader_resolves_through_the_accepted_marker_tables`, `test_release_marker_presence_probes_every_accepted_spelling`). Not edited. Passed.
- Local-state refusal remains in `test_local_state_migration.py` (`test_legacy_state_detector_refuses_and_clears`, `test_launcher_refuses_legacy_state_before_creating_canonical_state`). Not edited. Passed.
- Alembic shim and `versions/` were not edited. There is no test whose name is the alias installer. `test_frozen_alembic_revision_bytes_are_unchanged` and `test_frozen_alembic_revision_set_is_complete` passed, and the full suite’s revision imports passed.
- Packaging: `test_chatgpt_page_packaging.py` was not edited and passed inside the 251-test run below.

Retooled because their fixtures named deleted symbols:

- `tests/contract/test_kronika_capture_services.py`: removed the C8-A/P capture-path block (15 test functions) and the unused `difflib`, `hashlib`, and `inspect` imports. 26 routine capture tests remain.
- `tests/contract/test_nuc_release_docs.py`: removed the three assertions that the runbook contains `MIGRATION_DIRECTORY`, `MIGRATION_SCRATCH_DIRECTORY`, and `MIGRATION_JOURNAL_PATH`. Replaced the README sentence pin. Added the two historical-sentence pins.
- `tests/contract/test_nuc_release_source_contract.py`: added `test_parser_exposes_only_the_routine_release_commands`.

The parser test requires exactly `status`, `check`, `deploy`, `rollback`, `activate-capture`, `rollback-capture`, and hidden `_remote` with `_remote-extract` and `_remote-relocate-venv-shebangs`.

## 3. Document replacements and pins

Runbook `## Capture Path Migration (Historical)`:

`The one-time capture-path migration has already run and `migrate-capture-paths` is gone. Routine `status`, `check`, `deploy`, and `rollback` address only the canonical layout and do not migrate.`

Runbook `### Identity Migration (Historical)`:

`The one-time host identity migration has already run and `migrate-identity` is gone. Routine `status`, `check`, `deploy`, and `rollback` address only the canonical layout and do not migrate.`

`deploy/ubuntu/README.md` uses the same capture-path sentence. Pin: `test_runbook_and_deploy_readme_document_capture_activation`. The identity sentence is pinned in `test_runbook_lock_lifecycle_matches_the_engine`. Both tests also reject the old headings and reject `kronika-release migrate-identity` / `framenest-release migrate-identity` as invocations.

The marker-reader sentence and the frozen Poetry/CPython tooling lines in the runbook were not edited. The schema `migration-required` continuation was not edited.

No other living document tells the operator to run either deleted command. `DEVELOPMENT.md`, `kronika-dev`, and `local_state_migration.py` name `migrate-identity-paths`, the workstation copy tool. That command stays.

## 4. Measured retention re-pin

Measured on the edited tree **before** changing any Part C scalar. The retention module was 7 failed, 8 passed. Part A and Part B were among the passes. After values were taken from that failure and from a same-definition per-file count that reproduced it. HEAD totals matched the old pins.

| Scalar | Before | After | Cause |
|---|---:|---:|---|
| tests files | 174 | 173 | deleted migration module leaves the content set; nothing added |
| tests occurrences | 1386 | 1101 | deleted module −278, `test_kronika_capture_services.py` −7 |
| deploy occurrences | 72 | 25 | `kronika_release.py` −47; README adds no token and stays out |
| docs occurrences | 751 | 748 | runbook −3, the three former capture-pointer literals |
| src / scripts / extension files and occurrences | unchanged | unchanged | |
| content paths | — | −1 | `tests/contract/test_kronika_identity_migration.py` only |
| `FRAMENEST_[A-Z0-9_]+` tokens | 116 | 88 | all −28 in the deleted module |
| distinct token names | 44 | 34 | ten names existed only in that module; none added |
| bare `FRAMENEST_` | 22 | 18 | engine prefix constant −1, deleted module −3 |
| `/opt/framenest` | 145 | 122 | engine −3, runbook −3, deleted module −17 |
| `/etc/framenest` | 30 | 18 | engine −3, deleted module −9 |
| `/var/lib/framenest` | 64 | 32 | engine −1, deleted module −31 |
| `/var/cache/framenest` | 19 | 10 | engine −1, deleted module −8 |
| `/mnt/framenest-catalog-offdevice` | 23 | 13 | engine −1, deleted module −9 |
| `User=framenest` | 4 | 2 | deleted module −2 |
| `Group=framenest` | 5 | 3 | deleted module −2 |

Distinct names that disappeared: `FRAMENEST_BASENAME_PATHS`, `FRAMENEST_CATALOG_BACKUP_OPS_ROOT`, `FRAMENEST_CATALOG_RESTORE_VERIFY_ROOT`, `FRAMENEST_EXTERNAL_ORIGIN`, `FRAMENEST_FOO`, `FRAMENEST_FUTURE_UNKNOWN_KEY`, `FRAMENEST_UDS_PATH`, `FRAMENEST_UPLOAD_QUARANTINE_ROOT`, `FRAMENEST_X`, `FRAMENEST_YOUTUBE_ACQUISITION_ROOT`.

Unchanged and still passing: header 37 / 16 files, capitalized `FrameNest` 2327 / 343, console scripts 0. The arithmetic comments live in the retention module, which the ledger excludes.

After the re-pin: **15 passed** in 0.36s.

## 5. Mutation demonstration

`migrate-identity` was added back to `_build_parser` only. `test_parser_exposes_only_the_routine_release_commands` failed:

`AssertionError` at `tests/contract/test_nuc_release_source_contract.py:493`, extra item `'migrate-identity'`.

The probe was removed before the later suites and before the commit.

## 6. Suites

| Run | Result | Time |
|---|---|---|
| `test_nuc_release_source_contract.py`, `test_nuc_release_docs.py`, `test_kronika_capture_services.py` | 100 passed | 0.76s |
| Retention, before re-pin | 7 failed, 8 passed | 0.41s |
| Retention, after re-pin | 15 passed | 0.36s |
| Readers, local-state, packaging, remote contract, operator runbook, source contract | 251 passed | 20.27s |
| Full Python (`ap exec --operation test`) | **4714 passed, 8 skipped, 3 warnings, 0 failed** | 697.58s |
| JS `companion_web_bridge` / `companion_review_extension` / `x_companion_extension` / `companion_settings_automatic_analysis` / `kronika_ui` / `catalog_card_ai_quick_action` | 23 / 41 / 55 / 6 / 12 / 30, 0 failed | |
| JS bounded frontend/cockpit/gallery glob | 212 passed, 0 failed | |

Baseline was 5016 passed, 8 skipped, 3 warnings, 0 failed. This commit is **−302 passed**. Skips and warnings are unchanged. The 8 skips are the same five real-tool cover cases, two real-tool media-analysis cases, and one NVIDIA smoke case. The drop is the removed migration module and the 15 removed capture-path tests, including parametrized matrices. No new failure.

## 7. Commit, Part A, Part B, Part C

`git diff --stat` for `f2c4624ded775e3446bfafef4a5a413253a03136`:

```text
 deploy/ubuntu/README.md                            |    6 +-
 deploy/ubuntu/kronika_release.py                   | 4016 +---------------
 docs/UBUNTU_NUC_DEPLOYMENT.md                      |   89 +-
 tests/contract/test_kronika_capture_services.py    |  645 ---
 tests/contract/test_kronika_identity_migration.py  | 4839 --------------------
 tests/contract/test_kronika_identity_retention.py  |   58 +-
 tests/contract/test_nuc_release_docs.py            |   23 +-
 tests/contract/test_nuc_release_source_contract.py |   34 +
 8 files changed, 167 insertions(+), 9543 deletions(-)
```

Working tree clean after the commit. Not pushed.

Part A: byte-unmoved. Frozen-document and frozen-Alembic tests passed.
Part B: still empty. `CANONICAL_REPLACEMENT_PATHS` still has 20 members. The basename test passed.
Part C: the movements in section 4. Cause: deleting the one-time migration implementation, its test module, the capture-path test block, and the three former capture-pointer literals in the runbook procedure.

## 8. Sites no remaining test exercises

Reintroducing a deleted helper without putting `migrate-identity` or `migrate-capture-paths` back on the parser does not fail a test. The parser test pins the command set, not each removed function. The engine docstring’s historical sentence is not pinned; the runbook and README sentences are.

`CAPTURE_BRIDGE_UNIT` is still used by the routine bridge restart, and the capture-activation tests passed.

## 9. Deviations, risks, missing evidence, next step

Deviation: `61_report_00.md` was absent; the session-61 plan text was used instead. The grant’s own deletion list was the execution source.

Risk: the historical sentences say routine `status` / `check` / `deploy` / `rollback` address only the canonical layout. `WEB_LAYOUTS` still contains `OLD_WEB_LAYOUT`. That claim becomes true in C9-B/2, not in this commit. The grant required the sentence and also required the dual-layout selector to stay.

Missing evidence: the −302 passed count is the full-suite difference. The deleted file was not collect-only’d against the parent commit, so the 302 is not a second node-id inventory. Skips did not move and nothing failed.

Smallest next step: C9-B/2, canonical layout only, against `f2c4624ded775e3446bfafef4a5a413253a03136`. No push, publication, or NUC refresh is authorized by this report.

### Resolved Execution Issues / Near-Misses

A prefix check for `EXIT_MIGRATION` also matched `EXIT_MIGRATION_REQUIRED` and removed exit 13. The first focused run failed `test_engine_exit_13_residue_is_the_documented_three_artifacts` with `NameError: name 'EXIT_MIGRATION_REQUIRED' is not defined`. The constant was restored as `EXIT_MIGRATION_REQUIRED = 13` before any green suite. The full suite then passed, including the deploy `migration-required` cases. Residual risk: none.

### Pre-Existing Failure Classification

none

Authority expiry: this report ends the authority in the session-62 exchange-01 prompt. No further edit, second commit, push, publication, or host contact is authorized by it.

```text
Orchestration critique:
MEASURED: the required historical sentences say routine status/check/deploy/rollback address only the canonical layout; deploy/ubuntu/kronika_release.py still defines WEB_LAYOUTS = (OLD_WEB_LAYOUT, NEW_WEB_LAYOUT). Effect: the operator sentence is ahead of the selector until C9-B/2. Smallest correction: C9-B/2 removes the old layout from selection, which makes the sentence true.
LEAD: none
```
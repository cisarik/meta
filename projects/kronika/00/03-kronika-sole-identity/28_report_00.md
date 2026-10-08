All verification is complete. Delivering the terminal report now.

---

### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session / exchange | `28` / `01` |
| Task identity | `KSI-AUDIT-C6V` |
| Persistent role | `WORKER` (Fresh Independent Audit, read-only) |
| Status | **PASS — no blocking finding; C6 readiness independently established** |
| Report justification | `new-evidence` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Candidate commit | `24d2b7d718eb303c79197f6e2f41c81ad479a79a` |
| Changed files / Git writes / push | none / none / none |
| NUC, provider, browser contact | none |

## 1. Identity, scope and gate verification

- **Candidate identity.** Local `HEAD`, branch `main`, and the requested baseline are exactly `24d2b7d718eb303c79197f6e2f41c81ad479a79a`; working tree clean. Candidate parent is `8a5861c792122468468b3bc20934a26cb5eb1c93` (C6-P1), whose parent is public main `3194f48f6b343a460ed5988d92999f91ef999a79a`.
- **AP gates.** Containing-repository `.ap` gitlink and submodule HEAD are both `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; submodule clean; `./.ap/ap doctor` PASS with governing variant `stable`; `ap project check --baseline 24d2b7d` PASS; `WARN sanitized inherited environment classes` only.
- **Scope.** `3194f48..8a5861c` modifies exactly 3 paths; `8a5861c..24d2b7d` modifies exactly 6; the union is exactly the six mandated paths, all `M`, no additions/deletions: `deploy/ubuntu/kronika_release.py`, `src/kronika/adapters/cli/recovery.py`, `src/kronika/infrastructure/persistence/catalog_backup_workstation.py`, `tests/contract/test_kronika_identity_migration.py`, `tests/contract/test_kronika_identity_retention.py`, `tests/contract/test_recovery_cli.py`. No path outside the C6-P1/P2 mandate changed.
- **No other cut present.** No `identity-labels`, `migrate-identity-paths`, new infosec/Mullvad counterparts, runbook edits, or C7-B removals appear in the diffs; all 14 retired console aliases remain in `pyproject.toml` (C7-B not done); the runbook is untouched (C-RUNBOOK not done). No new deployment entry point: `deploy/ubuntu/kronika-release` and the retained `framenest-release` wrapper both forward to the single engine `kronika_release.py`; the migration shares the routine deploy lock and adds no second system. Capture pointer switch/restart call sites exist only in `_cmd_capture_transition` (`kronika_release.py:5740-5825`).
- **Re-derived Python gate.** Full suite at `24d2b7d` re-run through the declared `test` operation: **4689 passed, 8 skipped, 3 warnings, 0 failed** (698.51 s), exactly the declared state.

## 2. Capability reconciliation

Legend: NV = non-vacuous verdict (`yes` = an independent mutation or a boundary/executable proof fails when reverted, or every stated dimension is asserted against modelled state).

| # | Capability (§2.1/§2.2/§2.2 proof) | Production implementation | Exercising test | NV | Result |
|---|---|---|---|---|---|
| 1 | One shared exclusion acquired before control state | `RemoteMigrationHost.acquire_lock`/`release_lock` → shared `acquire_deploy_lock`/`release_deploy_lock` (3181-3210, 2328-2391); `run_migration_apply` acquires first (4501) | `test_orchestration_acquires_the_exclusion_before_writing_control_state`; `test_production_exclusion_is_shared_with_routine_deploy_and_rollback` | yes (probe 2: call order `3 < 1`) | PASS |
| 2 | Control state outside copy destinations, root-only, atomic, preserved | `MIGRATION_DIRECTORY` 268; `migration_control_conflicts` 2994; `_assert_control_location` 3128; atomic write 696; existing-journal refusal 4504 | `test_migration_control_directory_is_outside_every_plan_destination`; `test_control_location_guard...`; `test_production_control_state_does_not_block_the_state_copy`; `test_production_journal_write_interruption...`; `test_orchestration_refuses_and_preserves_an_existing_journal` | yes (probe 1) | PASS |
| 3 | Durable intent/substeps + conservative `writes_possible` before start | journal v2 2961; `_persist_substep` 3120; 4521-4530; `migration_writes_possible` 2982 | `test_journal_is_written_before_the_first_mutation_and_after_every_phase`; `test_start_service_entry_selects_post_write_without_a_completed_phase`; `test_writes_possible_reads_the_durable_boundary_first`; `test_orchestration_startup_ack_failure...` | yes (probes 3, 3b) | PASS |
| 4 | Pre-write recovery incl. partial rename; post-write preserves | `recover_pre_write` 4002; `_restore_observed_units` 4095; `recover_post_write` 4124 | `test_failure_injection_after_every_phase` (45 phases); partial-rename, observed-home, pointer-removal, legacy-fallback, post-write-preservation tests | yes | PASS |
| 5 | Copy verification (type, symlink target, mode, ownership, content); refuse populated/query-failed destination | `cmd_remote_tree_manifest` 2487; `cmd_remote_directory_state` 2459; `copy_state` 3350 | `test_production_copy_state_verifies_before_it_continues`; `...accepts_a_matching_manifest`; `...refuses_a_populated_destination`; `...refuses_a_destination_with_a_failed_query` | yes | PASS |
| 6 | Dead builders removed | `cmd_remote_unit_enabled_state`, `cmd_remote_switch_layout_release`, `migration_unit_required`, `MIGRATION_LOCK_*` absent repo-wide | none possible (no caller existed) | n/a (parse-verified) | PASS |
| 7 | Query failure ≠ absence | `_require_query_result` 4584; query-failed forms in existence/file/list/unit/effective/root-file/directory/link builders; `parse_remote_unit_state` 3020; `parse_effective_unit_state` 3041 | journal/process/unit/destination/current-pointer failed-query refusals | yes | PASS |
| 8 | Exact-state binding and drift refusal | `read_migration_observation` 4614; `required_current_release_sha` 4592; digest 2877/2957; apply re-read 5064 | `test_preflight_refuses_a_missing_or_unverifiable_current_pointer`; `...current_release_that_is_not_the_migration_release`; `...present_canonical_current_pointer`; `test_apply_rejects_intervening_drift_before_mutation`; `test_plan_digest_binds_effective_units_current_release_and_artifacts` | yes (digest comparison mutation carried from P2; boundary asserts no mutation command) | PASS |
| 9 | Owned scratch prepared and cleaned | 111-112; 3577-3581; helper 3631-3640; cleanup 3194-3209 | `test_production_prepare_release_environment_builds_at_the_new_path` (0700 dir, helper there, routine scratch untouched); `test_production_lock_release_cleans_the_owned_scratch_area` | yes (boundary effects, not transcript) | PASS |
| 10 | Canonical release environment, committed lock, frozen tooling, final executables | `prepare_release_environment` 3560-3715 | `...builds_at_the_new_path`; `...refuses_a_tampered_committed_lock`; `...detects_a_changed_retained_release`; `...refuses_a_non_executable_console_script` | yes (probes 9a/9b) | PASS |
| 11 | Guard-then-switch pointer before startup | `switch_current` 3829-3855 | `...guards_then_switches_before_start` (index assertion); `...refuses_without_executable_scripts` (no `ln -s`, no start) | yes (probe 4) | PASS |
| 12 | Effective units/drop-ins/timers; vendor paths; scheduling preservation | `cmd_remote_unit_effective_state` 2646; `parse_effective_unit_state` 3041; `install_units` 3751; `stop_writers` 3246; `resume_writers` 3969 | `test_preflight_observes_vendor_installed_units_and_dropins`; `test_production_install_units_disables_obsolete_autostart_links`; `test_production_stop_writers_stops_timers_before_their_jobs`; `test_production_resume_writers_restores_only_observed_scheduling` | yes (probe 7) | PASS |
| 13 | Structural drop-in/LoadCredential and sudoers transformation with refusals | `_systemd_transform_value` 4226; `transform_unit_dropin_text` 4320; `transform_sudoers_text` 4385 | `...handles_supported_directives`; `...refuses_unknown_forms` (both); preflight unknown-directive/unknown-sudo refusals | yes (probes 8a/8b) | PASS |
| 14 | Ancillary typed installs; absent stays absent | `preserve_ancillary` 3443; `_install_root_file` 3533; `_validate_root_file` 3524 | `test_production_ancillary_installs_root_owned_modes` (0755/0440, bytes, `visudo -cf`; absent plan → zero calls); `...refuses_a_wrong_installed_mode` | yes | PASS |
| 15 | Workstation fixed-tuple selection; arbitrary input refused | `REMOTE_LAYOUT_COMMANDS` workstation.py:93; `resolve_remote_layout_command` 785; `build_ssh_argv` 800; `pull` 383; CLI `--remote-layout` recovery.py:155-162 | `test_pull_remote_layout_selection_is_fixed_and_explicit` (5 rejections); `...parser_accepts_only_the_two_fixed_layout_choices`; `...pull_passes_the_selected_fixed_layout` | yes (probe 10) | PASS |
| 16 | Readiness after startup wired | `start_service` 3857 → `verify_local_readiness` 3865 | `test_production_start_service_verifies_local_readiness` | yes (probe 5) | PASS |
| 17 | Ingress replacement bounded; verification after; failure not success | `replace_tailscale_handler` 3899; `verify_ingress` 3926 | `test_production_verify_ingress_fails_after_a_failed_edit`; `test_orchestration_ingress_failure_after_a_healthy_start_selects_post_write` | yes | PASS |
| 18 | Capture identity before/after; no capture restart | `capture_snapshot` 3298; `verify_capture_untouched` 3317; phase map 4553 | `test_production_capture_identity_change_is_detected`; phase matrix `capture_restarts == 0`; `test_canonical_artifacts...`/routine tests | yes (probe 6) | PASS |
| 19 | Ordering: switch+readback before start; readiness after start; resume last; failed ingress not success | phase table 293-309; `MIGRATION_CUTOVER_PHASE` 313 | `test_migration_phases_are_ordered_and_complete`; simulated `start_service` asserts `pointer_switched` | yes | PASS |
| 20 | Executable release proof, not transcript substrings | `relocate_venv_shebangs` 1353 | `test_prepared_release_console_scripts_execute_in_an_isolated_fixture` executes 4 scripts, asserts stdout | yes (probe 12, §5) | PASS |
| 21 | Stateful boundary rejects unknown commands, models effects | `RemoteBoundary` 1681-2400 | boundary suites; no dedicated unknown-command test | yes (probe 11) | PASS |
| 22 | Frozen material and routine isolation | retention ledger; routine tests | `test_frozen_*` (86/36), Part B 20; `test_routine_commands_never_reach_identity_migration`; `test_canonical_artifacts_are_never_installed_by_routine_commands` | yes | PASS |

The §2.2 proof list and the P2 effect matrix were additionally walked row-by-row; every named outcome has a matching test above. Two proof-matrix items not separately rowed (non-unit `.conf` artifacts observed by existence and never systemd-queried; stop-writers order/pointer removal) are covered by `test_preflight_observes_non_unit_artifacts_by_existence_and_never_stops_them` and the stop/recovery tests.

## 3. Production commands or substeps no test exercises

Confirmed from P2 report §8 (each re-verified by literal search):

1. `switch_current` link-readback mismatch branch (3852-3855).
2. `release_lock` suppressed helper-removal failure and non-empty scratch `rmdir` suppression (3198-3209).
3. `_root_file_evidence` `absent`/`unsafe`/`query-failed` classifications and `_validate_root_file` wrong-owner branch (wrong mode is tested).
4. `preserve_ancillary` canonical-already-present sudo-rule path (`visudo` on the retained canonical rule).
5. `transform_unit_dropin_text` `{ path=… }` revision form and its non-absolute refusal (only the parse side is tested).
6. `transform_sudoers_text` comment/blank-line preservation (fixtures carry no comments).
7. Observation/preflight against a canonical-only export installation (fakes always find the former candidate first).
8. `install_units` copying an observed non-unit `.conf` artifact to its canonical name.
9. `_observed_writer_units` fallback to the plan when the live journal has no `observed_units` substep.
10. `verify_capture_untouched` runner-active-drop branch alone.
11. `resume_writers` combinations `enabled+inactive` and `disabled+active`.

Added by this independent derivation (not in P2 §8):

12. **`RemoteMigrationHost.create_checkpoint`** (3336-3348) — production method invoked by no test; only the simulated host phase name exists.
13. **`RemoteMigrationHost.verify_effective_units`** (3812-3827) — production method invoked by no test (`parse_web_layout_probe` itself is tested).
14. **Production `RemoteMigrationHost.quiesce`** (3239-3244) — composite never invoked; its parts are tested separately (the production "before" capture snapshot path is therefore unexercised).
15. `replace_tailscale_handler` zero-handler branch and `verify_ingress` zero-handler early return (`tailscale_handler_count == 0`).
16. `cmd_remote_tailscale_replace` mount-validation refusal (non-default mount).
17. `transform_path_value` "not classifiable" refusal branch.
18. `parse_tailscale_serve_status` unreadable/malformed status refusal.
19. `read_journal` malformed-JSON classification.

No test can exercise the P1 removals themselves; absence was re-verified by repo-wide parse. The `_cmd_migrate_apply` production end-to-end path remains intentionally host-gated.

## 4. Mutation-probe results

Probe module `/tmp/opencode/ksi28/probe_mutations.py` (outside project state; in-memory `monkeypatch` or `exec` of a textually mutated function with throwaway globals). All 16 probe tests pass; each mutation made the named repository test fail:

| # | Mutation | Target test | Observed failure |
|---|---|---|---|
| 1 | `_assert_control_location` → no-op | `test_control_location_guard_refuses_a_destination_that_contains_it` | `Failed: DID NOT RAISE ReleaseError` |
| 2 | manifest/journal written before `acquire_lock` | `test_orchestration_acquires_the_exclusion_before_writing_control_state` | `AssertionError: assert 3 < 1` (call order) |
| 3 | `writes_possible` set after the start-service method | `test_start_service_entry_selects_post_write_without_a_completed_phase` | `AssertionError: assert 'pre-write' == 'post-write'` |
| 3b | `migration_writes_possible` inference-only | `test_writes_possible_reads_the_durable_boundary_first` | `AssertionError: assert False is True` |
| 4 | `verify_unit_executables` → empty tuple | `test_production_switch_current_refuses_without_executable_scripts` | `Failed: DID NOT RAISE ReleaseError` |
| 5 | `verify_local_readiness` → no-op | `test_production_start_service_verifies_local_readiness` | `AssertionError: assert False` (no `systemd-run`) |
| 6 | `verify_capture_untouched` → no-op | `test_production_capture_identity_change_is_detected` | `Failed: DID NOT RAISE ReleaseError` |
| 7 | `resume_writers` gating → `if True` (both checks) | parametrized `disabled/inactive` case | `AssertionError: assert 'enabled' == 'disabled'` |
| 8a | `transform_unit_dropin_text` → token replace | `test_structural_dropin_transformation_refuses_unknown_forms` | `Failed: DID NOT RAISE ReleaseError` |
| 8b | unmatched sudo line → skip instead of raise | `test_structural_sudoers_transformation_refuses_unknown_forms` | `Failed: DID NOT RAISE ReleaseError` |
| 9a | committed-lock comparison → `if False` | `test_production_prepare_release_refuses_a_tampered_committed_lock` | `Failed: DID NOT RAISE ReleaseError` |
| 9b | retained-release comparison → `if False` | `test_production_prepare_detects_a_changed_retained_release` | `Failed: DID NOT RAISE ReleaseError` |
| 10 | `resolve_remote_layout_command` → echo arbitrary input | `test_pull_remote_layout_selection_is_fixed_and_explicit` | `AssertionError` on the fixed-tuple argv assertion |

Probes 11-13 (below) passed directly. Probe 13 asserted, inside the probe process, `git status --porcelain` empty and HEAD `24d2b7d…`.

## 5. Stateful-boundary and executable-probe verification

- **Boundary rejects unknown commands:** `RemoteBoundary(...)(["ssh","sudo -n frobnicate /nowhere"])` raises `AssertionError` (final `raise` in `_dispatch`, test file 2356). No unconditional-success fallback exists.
- **Boundary models effects:** a `cat >` command creates the file with the exact payload and mode `0o600`, is visible in `manifest()`, and a subsequent `test ! -e` fails with `ReleaseError`; parents are materialized on demand. The boundary also models `mv -T`, `cp -a` plus the following `rm -rf`, `stat`, `sha256sum`, systemd show/actions, unit registration from written unit files and `.d` drop-ins, tamper and failure injection.
- **Executable release probe is real execution:** the repository test runs the four prepared console scripts with `subprocess.run([str(script)], check=True)` and asserts exact stdout (`prepared-db-ok`, `prepared-backup-ok`, `prepared-production-ok`, `prepared-backup-ok`). Independent negative control: with `relocate_venv_shebangs` disabled in memory, the same fixture raises `FileNotFoundError` executing the un-relocated script (shebang names the gone staging interpreter), proving the positive assertions depend on actual process execution, not transcript text.

## 6. Frozen-material and routine-path isolation evidence

- **Part A.** Independently recomputed with read-only `sha256sum` over all 86 `FROZEN_DOCUMENT_SHA256` entries and all 36 `FROZEN_ALEMBIC_SHA256` entries: zero mismatches. Ledger counts from the literal: 86 / 36; the Alembic directory holds exactly 36 revision files including `__init__.py`.
- **Part B.** The pinned basename set has 20 members, all present; `git ls-files` yields exactly 20 tracked basenames containing `framenest` (case-insensitive).
- **Committed lock.** `git diff 3194f48..HEAD -- poetry.lock` empty; the migration additionally re-verifies the staged lock against the plan-bound hash before and after install (3598-3630).
- **Frozen residues.** `/mnt/framenest-catalog-offdevice` and `/opt/framenest/tooling` are protected in `MIGRATION_FROZEN_PATH_PREFIXES` and asserted in `test_canonical_offdevice_artifacts_keep_the_frozen_mount` and `test_typed_transformation_preserves_custom_and_frozen_paths`.
- **Routine-path isolation.** `test_routine_commands_never_reach_identity_migration` (monkeypatched forbidden handlers, `deploy`/`rollback`/capture transitions) and `test_canonical_artifacts_are_never_installed_by_routine_commands` pass with the other 153 migration-module tests; capture atomic switch/restart appear only in `_cmd_capture_transition`.
- **Final state.** HEAD `24d2b7d718eb303c79197f6e2f41c81ad479a79a`, tree clean; `.ap` HEAD `73e20ef80…`, clean; no Git or durable-state mutation by this audit.

## 7. Focused check results

| Run (declared AP route, baseline `24d2b7d`) | Result |
|---|---|
| `tests/contract/test_kronika_identity_migration.py` | **155 passed**, 0 failed (0.79 s) |
| `tests/contract/test_recovery_cli.py` | **10 passed**, 0 failed (1.87 s) |
| `tests/contract/test_kronika_identity_retention.py` | **15 passed**, 0 failed (0.38 s) |
| Declared full suite (`--operation test`) | **4689 passed, 8 skipped, 3 warnings, 0 failed** (698.51 s) |
| Independent mutation probe module | **16 passed** (13 mutation detections + boundary/executable/clean-tree probes) |

## 8. Findings with disposition

- **F1 (non-blocking, coverage).** `create_checkpoint`, `verify_effective_units` and the production `quiesce` composite are executed by no test. They are thin fail-closed wrappers over tested primitives; neither participates in the guard sequence that the mutations exercise. Disposition: does not block C6-H; record and cover in a repository-only cut.
- **F2 (non-blocking, coverage).** The untested branches listed in section 3 (ingress zero/mount/readback/root-file/release-cleanup/sudoers-comment/revision-form/resume-combos/`.conf`/fallback/capture-drop). Disposition: does not block C6-H; already partly disclosed by P2 §8, with five additions.
- **F3 (non-blocking observation).** Automatic pre-write recovery restores account/unit/scheduler state but leaves the copied canonical state, installed canonical unit files and installed ancillary files in place; a retry is refused until explicit recovery, as designed. The accepted plan scopes recovery to observed account/group/home and unit/scheduler state, so this is residue, not a sequence defect. Recommendation: make the residue explicit in C-RUNBOOK.
- **F4 (non-blocking observation).** `start_service` readiness polls `check-database-ready` only; full health is verified in the following `verify-ingress` phase after the handler replacement. This matches the plan's apply sequence and the unit's own `ExecStartPre` readiness contract.
- **F5 (non-blocking observation).** `MIGRATION_JOURNAL_VERSION` is written but read by nothing (no v1 host exists) — carried from P1.

**No blocking finding. No confirmed production-sequence defect.** All ordering requirements (exclusion→control state; guard→switch→readback; startup→readiness; replacement→ingress verification; verification→writers resume; failed ingress edit cannot complete) were confirmed in code and by non-vacuous test or mutation.

## 9. Deviations, risks, missing evidence, smallest next step

- **Deviations.** None from the grant. One client-permission denial blocked an `rm` cleanup of temporary probe/doc-scan files; nothing executed, no state changed. Probe leftovers remain outside project state under `/tmp/opencode/ksi28/` and four `/tmp/opencode/*_paths|hashes.txt` files (non-secret); deletion is unavailable in the permitted surface, so they are retained and reported.
- **Missing evidence.** No host execution of any phase, by design; real `systemctl show` (`DropInPaths` ordering, file-installed-but-not-loaded LoadState), real `visudo`/Poetry and installed sudoers modes remain host-verifiable only (the adapter fails closed on `query-failed`). The P1 pre-repair failure reproduction is carried from report 26 §1, not independently re-run (would require checking out the superseded tree).
- **Risk.** The boundary is a model, not a sandbox; the host preflight remains the last unverified layer.
- **Smallest next step.** Issue the bounded repository-only **C-RUNBOOK** grant (docs/source-contract only) and fold F1's two missing production-adapter tests into that same cut; any unresolved production-sequence defect would then still block C6-H, and none was found.

### Resolved Execution Issues / Near-Misses

- The first two probe runs failed on probe-construction indentation errors (my file, not the repository); fixed and re-run. Classified as diagnostic-method failure per AP §12.
- One cleanup `rm -f` was denied before execution; no mutation occurred; leftovers disclosed above.
- Initial call-site greps returned unrelated matches; all cited sites were re-resolved by literal reads.

### Pre-Existing Failure Classification

- **none.** Baseline is exactly `24d2b7d718eb303c79197f6e2f41c81ad479a79a` (candidate head, no later correction); the re-run full suite reported 0 failures with the identical 8 skips / 3 warnings as declared; the focused modules and the probe module are green. No failure predates or postdates this candidate.

```text
Orchestration critique:
MEASURED: Report 27's coverage accounting is incomplete: `create_checkpoint`, `verify_effective_units` and the production `quiesce` composite have no exercising test, and five further untested branches exist beyond its §8 list. Evidence: static call-site resolution plus the 155-test module run (no test invokes those production methods); effect: a later reader could over-trust §8 as the full coverage boundary, though none of the omissions is a sequence or safety defect; smallest correction: add the three sites and five branches to the C-RUNBOOK coverage ledger or a small repository-only cut.
LEAD: Real `systemctl show -p DropInPaths` ordering and a file-installed-but-not-loaded unit's LoadState remain unverified outside the model, and the canonical-sudoers-only ancillary path is untested. Cheapest useful check: the planned read-only C6 preflight reports effective fragments, drop-in paths, installed file modes and which export/sudo candidate exists, without values.
```

All authority under this Worker prompt expires on submission of this report. No implementation, correction, commit, push, publication, host contact or later cut is authorized by it.
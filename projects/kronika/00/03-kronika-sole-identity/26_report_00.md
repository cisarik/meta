### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session / exchange | `26` / `01` |
| Task identity | `KSI-IMPL-C6P1` |
| Persistent role | `WORKER` |
| Status | **PASS** |
| Report justification | `new-mutation` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Starting commit | `3194f48f6b343a460ed5988d92999f91ef999a79` |
| Tested and committed commit | `8a5861c792122468468b3bc20934a26cb5eb1c93` |
| Changed files | 3 authorized paths only |
| Push / publication / deployment | none |
| NUC, provider, browser contact | none |

## 1. Defect reproduction at `3194f48` (before any engine edit)

Two tests were added first and run through the declared route against the unchanged engine. Both failed on the actual defects, not on missing API.

**Reproduction A — journal makes the copy destination exist.**
`tests/contract/test_kronika_identity_migration.py::test_production_control_state_does_not_block_the_state_copy` drives the production adapter over a new stateful in-memory remote boundary: `write_recovery_manifest`, `write_journal`, `acquire_lock`, then `copy_state`. Baseline output:

```text
deploy/ubuntu/kronika_release.py:2974: in copy_state
    remote_command=cmd_remote_test_absent_or_fail(destination),
...
combined = 'ssh ... op@nuc sudo -n test ! -e /var/lib/kronika'
...
kronika_release_migration.ReleaseError: path exists
1 failed, 95 deselected in 0.35s
```

Cause: `MIGRATION_DIRECTORY` was `/var/lib/kronika/identity-migration`, so the journal write created `/var/lib/kronika`, and `copy_state` requires every destination absent. The conflict is deterministic for the first `copy_moves` entry.

**Reproduction B — control state before any exclusion.**
`test_orchestration_acquires_the_exclusion_before_writing_control_state` recorded the real orchestration call order:

```text
AssertionError: assert 2 < 0
  where 2 = ['write_recovery_manifest', 'write_journal', 'acquire_lock', 'quiesce', ...].index('acquire_lock')
2 failed, 94 deselected in 0.36s
```

Both tests pass after the repair; the recorded baseline failures are the reproduction evidence.

## 2. Derived affected-method inventory (parsed, every caller resolved)

Removed on this first engine touch (repo-wide parse found only definitions; no engine, test, operator-script or wrapper caller — removal proceeded):

| Removed site (baseline line) | Callers found |
|---|---|
| `cmd_remote_unit_enabled_state` (2457) | none |
| `cmd_remote_switch_layout_release` (2533) | none; P2 must reuse `cmd_remote_atomic_switch` |
| `migration_unit_required` (2753) | none (`read_migration_observation` reads the tuple's `required` field directly) |
| `MIGRATION_LOCK_DIR`, `MIGRATION_LOCK_OWNER_PATH` (254–255) | only the old `RemoteMigrationHost.acquire_lock`/`release_lock` bodies |

Changed, with all callers:

| Site (baseline) | Production callers | Test callers |
|---|---|---|
| `MIGRATION_DIRECTORY`/journal paths (251–253) | `RemoteMigrationHost` journal I/O | new boundary/matrix |
| `cmd_remote_existence` (2385) | `preserve_ancillary` (2), `read_migration_observation` (5) | preflight fake, new boundary |
| `cmd_remote_read_optional_file` (2393) | `read_journal`, `read_migration_observation`, `preserve_ancillary`, `install_units` | preflight fake, new boundary |
| `cmd_remote_list_directory` (2461) | `read_migration_observation` (2) | preflight fake |
| `cmd_remote_account_processes_absent` (2510) | `assert_no_legacy_writers` | new boundary |
| `cmd_remote_read_optional_link` (978) | `read_optional_release_sha`, `resolve_capture_pointer`, `_cmd_capture_transition` | routine/capture fakes (substring-matched) |
| `cmd_remote_tree_manifest` (2419) | `copy_state` | two existing copy tests, new boundary |
| `RemoteMigrationHost.{read_journal,write_journal,write_recovery_manifest,_write_root_file,acquire_lock,release_lock,quiesce,stop_writers,assert_no_legacy_writers,copy_state,rename_account,recover_pre_write,recover_post_write}` | `run_migration_apply`, `_cmd_migrate_apply` | existing production-host tests, new matrix |
| `run_migration_apply` (3585) | `_cmd_migrate_apply` | simulated orchestration tests |
| `read_migration_observation` (3659) | preflight/apply CLI | `ReadOnlyPreflightRunner` tests |

New: `cmd_remote_write_file_atomic`, `cmd_remote_directory_state`, `cmd_remote_unit_state`, `migration_writes_possible`, `migration_control_conflicts`, `parse_remote_unit_state`, `_require_query_result`, `observe_writer_state`, `_restore_observed_units`, `bind_journal`, `_persist_substep`, `_assert_control_location`.

Callers the prompt's sample did not name: `read_optional_release_sha`, `resolve_capture_pointer` and `_cmd_capture_transition` are the three consumers of `cmd_remote_read_optional_link` that required query-failure handling; `preserve_ancillary` and `install_units` are additional consumers of the changed file/list/existence builders; `cmd_remote_test_absent_or_fail` remains used only by `prepare_release_environment` and was kept.

## 3. The repair, per outcome

1. **One exclusion.** `RemoteMigrationHost.acquire_lock/release_lock` now call the existing `acquire_deploy_lock`/`release_deploy_lock` (routine deploy/rollback share it). `run_migration_apply` acquires it before `read_journal` and before any control-state write. The separate migration lock constants and code are deleted. On release, the apply removes exactly the remote helper it wrote (`{REMOTE_DEPLOY_DIR}/framenest_release.py`) so the shared lock directory can be released; preparing an owned scratch area remains P2.
2. **Control state outside copies.** `MIGRATION_DIRECTORY = "/var/lib/kronika-identity-migration"` (root-only 0700, sibling of the copied state root). `_assert_control_location` derives the copy root set from `plan.copy_moves` and refuses both containment directions before any read/write. Journal/manifest are written with `cmd_remote_write_file_atomic` (write `.next`, verify hash, `mv -T`). `run_migration_apply` refuses a fresh apply while any existing journal is present and never overwrites it.
3. **Durable intent and conservative boundary.** Journal v2 adds `journal_version`, `current_phase`, `substeps`, `writes_possible`. Each phase records intent before running and completion only after return. `writes_possible` is persisted **before** invoking `start-service`. `migration_writes_possible` reads the durable fields first and falls back to completed phases only for legacy journals.
4. **Recovery.** Pre-write recovery reverses group/user/home from substeps (conservative "may have run" records written before each rename command), restores observed unit enablement and activity exactly (`observe_writer_state` at quiesce start), and keeps a legacy fallback for journals without substeps. Post-write recovery refuses without a durable writes boundary and touches nothing. Query builders emit `query-failed` distinct from `absent`/`not-found`/no-processes; every caller treats it as a hard error.
5. **Copy verification.** `copy_state` classifies the destination without touching it and refuses anything but `absent`; the manifest now covers relative path, type, symlink target, owner, group, mode and content hash.
6. **Dead builders removed** as inventoried in section 2. `verify_local_readiness` and all P2 scope (pointer switch, unit install/activation, ingress, workstation selection, timer capture) are untouched.

## 4. Guard-failure demonstrations (named mutation → observed failure)

| # | Mutation applied, then reverted | Test | Observed failure |
|---|---|---|---|
| 1 | `MIGRATION_DIRECTORY` back to `/var/lib/kronika/identity-migration` | `...control_state_does_not_block...` | `ReleaseError: identity migration control state overlaps copied state roots` |
| 2 | `_assert_control_location` raise → `pass` | `...control_location_guard...` | `DID NOT RAISE ReleaseError` |
| 3 | journal/manifest written before `acquire_lock` | `...acquires_the_exclusion_before...` | call log `['read_journal','write_recovery_manifest','write_journal','acquire_lock',...]` |
| 4 | `writes_possible` set after the start-service method | `...start_service_entry...` | `assert 'pre-write' == 'post-write'` |
| 5 | `migration_writes_possible` inference-only | `...start_service_entry...` + `...writes_possible_reads...` | pre-write selected; `{'writes_possible': True}` → False |
| 6 | `_persist_substep` calls removed from `rename_account` | `...partial_rename_is_recorded...` | `KeyError: 'group_renamed'` |
| 7 | `_write_root_file` reverted to non-atomic write | `...journal_write_interruption...` | `DID NOT RAISE ReleaseError` |
| 8 | process query reverted to unconditional `wc -l` | `...process_query_is_not_read_as_absence` | `DID NOT RAISE ReleaseError` |
| 9 | populated-destination refusal removed | `...refuses_a_populated_destination` | `'copied state did not verify...'` instead of `'not absent'`; `cp -a` issued |
| 10 | `parse_remote_unit_state` query-failed → absent | `...observe_writer_state_refuses_a_failed_query` | `'an observed migration writer unit is absent'` instead of `'unit state query failed'` |
| 11 | `read_journal` query-failed guard disabled | `...journal_read_refuses_a_failed_query` | `ReleaseError('unexpected remote output')`, exit 20 instead of 27 |
| 12 | copy-destination query-failed guard disabled | `...refuses_a_destination_with_a_failed_query` | `'not absent'` instead of `'unverifiable'` |

## 5. Required matrix evidence

- **Concurrent invocation refusal:** `test_production_exclusion_is_shared_with_routine_deploy_and_rollback` holds the lock, then a second `RemoteMigrationHost.acquire_lock()` and a routine `acquire_deploy_lock` both raise `EXIT_EXISTS`; no journal exists; after release a routine acquire succeeds.
- **Journal-write interruption:** `test_production_journal_write_interruption_preserves_the_previous_journal` interrupts both before the `.next` write and before the rename; `read_journal` still returns the previous journal.
- **Populated-destination collision without destruction:** `test_production_copy_state_refuses_a_populated_destination` — refuses, the unrelated file is byte-intact, no `cp -a` and no `rm` issued.
- **Partial group/user rename:** `test_production_partial_rename_is_recorded_and_reversible` (group rename interrupted: only `group_renamed` recorded, reverse group issued, no `usermod`) plus `...reverses_a_partial_rename` and `...restores_the_observed_home` over the boundary.
- **Startup succeeds but acknowledgement/journal write fails:** `test_orchestration_startup_ack_failure_selects_post_write_recovery` — post-write selected, no stale restore, `writes_possible`/`writes_admitted` persisted.
- **No stale-data rollback after possible writes:** `test_production_post_write_recovery_preserves_current_state` — no remote command at all, filesystem unchanged; refusal without a durable boundary.
- **Recovery selection from durable intent, not inference:** `test_start_service_entry_selects_post_write_without_a_completed_phase` — `start-service` absent from completed phases yet post-write is selected from the pre-phase record.
- **Query failure ≠ absence:** process, unit-state, journal, and destination query-failure tests.

## 6. Focused, full-suite and retention counts

| Run (declared route, baseline `3194f48`) | Result | Elapsed |
|---|---|---|
| Focused migration module | **117 passed**, 0 failed | 0.59 s pytest / 1.23 s wall |
| Declared full Python suite | **4648 passed, 8 skipped, 3 warnings, 0 failed** | 685.39 s (11:25) |
| Retention module | **15 passed**, 0 failed | 0.35 s / 0.98 s wall |

Baseline difference: `4625/8/3/0` → `4648/8/3/0`, i.e. **+23 collected tests, all passing** (2 reproduction tests + 21 matrix/guard tests in the migration module). No test was deleted; four assertions were updated to the repaired semantics (the two simulated recovery predicates, the failure-injection expectation, and the legacy reverse-rename assertion). Skips, warnings and zero failures are unchanged.

## 7. Commit, diff, Part A / B / C

`git diff --stat` at the commit:

```text
 deploy/ubuntu/kronika_release.py                  | 611 +++++++++++----
 tests/contract/test_kronika_identity_migration.py | 866 +++++++++++++++++++++-
 tests/contract/test_kronika_identity_retention.py |  37 +-
 3 files changed, 1353 insertions(+), 161 deletions(-)
```

Commit: `8a5861c792122468468b3bc20934a26cb5eb1c93` (`fix(deploy): repair migration exclusion, journalling and recovery`), one local non-amended commit, working tree clean, no push.

- **Part A byte-unmoved:** only the three authorized files changed; the frozen-document and frozen-Alembic byte tests passed. Computed at report time: `FROZEN_DOCUMENT_SHA256` = 86 keys, `FROZEN_ALEMBIC_SHA256` = **36** keys.
- **Part B still 20:** computed `EXPECTED_FRAMENEST_BASENAME_PATHS` = 20; ledger test passed.
- **Part C movement (measured, re-pinned with cause):** `deploy` 243→**244** (engine +3/−2: new `framenest_release.py` helper path and two conditional reverse-rename forms; removed `"framenest.service"` literal and the single old reverse command); `tests` 2008→**2049** (test file +42/−1: the new boundary, fixtures, unit names and assertions; the one removal is the legacy rename assertion repointed to the `-d` form); `/var/lib/framenest` 109→**120** and `/var/cache/framenest` 29→**31** (all in the test file's boundary fixtures/assertions; the engine adds no host literal). `/opt/framenest`, `/etc/framenest` and the frozen mount unmoved. No other Part C scalar moved.

## 8. Sites no test exercises

- The removals themselves (`cmd_remote_unit_enabled_state`, `cmd_remote_switch_layout_release`, `migration_unit_required`, `MIGRATION_LOCK_*`): no caller existed, so no test can exercise the removal; absence was verified by parse.
- Query-failure raises outside the new boundary tests: `read_optional_release_sha`, `resolve_capture_pointer`, `_cmd_capture_transition`, `read_migration_observation`'s `_require_query_result`, `preserve_ancillary`'s, `install_units`'s. The command-level `query-failed` protocol is exercised for process/unit/journal/destination only.
- Production `stop_writers` (skip condition and `writers_stopped` persistence) and `resume_writers`: not driven by a production-adapter test; `stop_writers` is exercised only through the simulated orchestration.
- `release_lock`'s helper-file removal path: the boundary tests release a lock where `prepare_release_environment` never wrote the helper, so the removal is a no-op in tests.
- `MIGRATION_JOURNAL_VERSION` is persisted but has no reader (no v1 journal exists on any host).
- `parse_remote_unit_state` branches for load states other than `loaded`, `not-found`, `query-failed`.

## 9. Deviations, risks, missing evidence, next step

- **Deferred by scope (P2):** `prepare_release_environment` still writes the remote helper into the routine deploy scratch directory (P1 only removes the exact owned helper at lock release); `resume_writers` forward scheduling preservation; `verify_capture_untouched` identity comparison; `verify_local_readiness` wiring. None was changed beyond outcomes 1–6.
- **Risk:** the pre-write recovery of observed unit state starts units but does not re-run jobs that a stopped timer may have missed; that is P2's scheduling contract.
- **Missing evidence:** no host execution of any phase (by design); the routine `read_optional_link` guard is only command-text/fake tested for success, not for a real privileged-query failure.
- **Collapsing pairs:** this cut touches no artifact-pair acceptance set. The sets it edits are Part C scalar counts, not membership; Part B membership and Part A pins are unchanged; `MIGRATION_UNIT_ARTIFACTS` membership is unchanged. The silent-collapse demonstration is therefore not applicable here, and none was fabricated.
- **Smallest next step:** issue the bounded **C6-P2** grant against `8a5861c` (pointer switch and release preparation, unit installation/activation, ingress, workstation command selection, timer capture); do not prepare the C6 host window before P2 and C6-V complete.

### Resolved Execution Issues / Near-Misses

- The boundary initially modeled a missing unit as a transport error; corrected to model `query-failed` (failed `systemctl show`) versus a `not-found` load state, so the absence/query distinction is faithful.
- One guard test initially accepted either failure classification; it was strengthened to assert the failure *kind*, after which mutation 10 was caught.
- The Part C `tests` scalar was measured at 2048, then two further matrix tests were added; it was re-measured to 2049 and re-pinned from that measurement. It was never adjusted to make a failing run pass.
- The engine-side `deploy` +1 and host-path movements were computed independently with per-file added/removed counts, not inherited from the plan.

### Pre-Existing Failure Classification

- **No pre-existing failure:** the authorized baseline was `4625 passed, 8 skipped, 3 warnings, 0 failed`.
- **Expected scalar movement:** the first full-suite run of the candidate showed only the two Part C retention count mismatches; both were re-pinned from measured values with the arithmetic cause stated.
- **Latent defects repaired by this cut:** journal/destination collision, control state before exclusion, separate migration lock, missing durable write boundary, inference-based recovery selection, partial-rename unreversibility, scheduler-state loss on recovery, unverified copy attributes, query-failure read as absence. These were source-established, not live incidents.
- **Retained by design:** activity-only capture verification, unwired `verify_local_readiness`, forward timer re-enablement and routine scratch helper placement (all C6-P2 scope).

```text
Orchestration critique:
MEASURED: The prompt's defect anchors were accurate; the independent derivation additionally found that the old adapter uploaded its helper into the routine deploy scratch directory without creating it, and that `cmd_remote_read_optional_link` feeds three routine consumers. Effect: the shared-lock repair had to clean the exact owned helper so a successful apply cannot fail at lock release. Smallest correction: keep the helper cleanup in `release_lock` until C6-P2 moves the helper to owned scratch, and re-derive `cmd_remote_read_optional_link` consumers in P2.
LEAD: A real host `systemctl show -p LoadState --value` behavior for a file-installed but not-yet-loaded unit is unverified here; the adapter fails closed on that answer. Cheapest useful check: a read-only C6-V or C6-P2 preflight that reports the load state of the installed timer/service units without mutating them.
```
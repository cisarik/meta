### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session / exchange | `29` / `01` |
| Task identity | `KSI-IMPL-CRUNBOOK` |
| Persistent role | `WORKER` (Fresh Implementation Worker) |
| Status | **PASS — bounded candidate produced and validated; non-independent** |
| Report justification | `new-mutation` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Start commit | `24d2b7d718eb303c79197f6e2f41c81ad479a79a` |
| Tested commit | `335e91d199e99e28f2585c1b25531f29bb54270c` |
| Publication / push | not published, no push (public `main` remains `3194f48…`) |
| NUC / provider / browser contact | none |

## 1. Derived pinned-string inventory (before → after)

I parsed both doc-contract files and the two other runbook-reading suites before editing. Only `test_nuc_release_docs.py::test_runbook_documents_exit_13_schema_jump_continuation` and `test_nuc_operator_runbook.py::test_runbook_schema_jump_continuation_uses_target_release_tree` pinned the corrected text.

**Before (removed pins):**

| Site | Stale pin |
|---|---|
| `test_nuc_release_docs.py` | `current_revision=0032`, `head_revision=0033`, `current_revision=head_revision=0033`, `/run/framenest-release-deploy/{ap.tar,framenest_release.py,superproject.tar}` |
| `test_nuc_operator_runbook.py` | the same three schema literals and the same three lock-path literals |

**After (corrected pins):**

| Site | New pin |
|---|---|
| both files | `current_revision=<C>`, `head_revision=<H>`, `current_revision=head_revision=<H>`; operator-negative stale literals `current_revision=0032` / `head_revision=0033` / `current_revision=head_revision=0033` / `` `0033` `` in the docs file |
| `test_nuc_release_docs.py` new tests | lock artifacts parsed from `inspect.getsource(_cmd_deploy)`/`_cmd_rollback`; `REMOTE_DEPLOY_DIR`, `REMOTE_DEPLOY_LOCK_OWNER_PATH`, `cmd_remote_mkdir_deploy_dir()` with no `-p`; reclaim reasons and quarantine paths derived by calling `classify_deploy_lock_owner`; `MIGRATION_DIRECTORY`, `MIGRATION_SCRATCH_DIRECTORY`, `MIGRATION_JOURNAL_PATH`; `"rm -rf" not in text` |

**Sites my derivation found that the prompt's sample did not name:** the full assertion set of both functions (not just lines 149–154); `tests/contract/test_fedora_systemd_service.py::test_ubuntu_runbook_has_auditable_phase_and_safety_boundaries` (reads the runbook; untouched); the operator-runbook service-account classifier tests (lines 65–92; untouched); the runbook's capture and `EnvironmentFile` assertions; and the retention Part C scalars.

## 2. Part A per outcome, with the engine cross-check

1. **Three recovery cases separated.** New `### Shared Release Lock Recovery` states (a) live owner → stop, no removal; (b) proven stale/ownerless residue → inspect phase/ownership/contents first, exact objects only, ownerless is never auto-reclaimed; (c) `migration-required` → the annex, schema-generic.
2. **`previous-release` and owner-record lifecycle.** Documented at `_cmd_deploy:5227` created after the checkpoint (`5359-5374`); `rollback-previous-release` at `_cmd_rollback:5618`; owner record at `97-101`, acquired/reclaimed at `2328-2367`, removed after the empty directory at `2381-2391`.
3. **Hardcoded schema example replaced.** `<C>` from the fresh `status`/`current_revision`, `<H>` from the target-tree status; no permanent example; the negative pins enforce removal.
4. **Exact-object recovery only.** Named `rm -f` files, then empty-directory `rmdir`, then the owner record; no wildcard/recursive/parent deletion; the text states stale locks can recur.
5. **C6-V F3 residue documented.** The identity-migration note states that pre-write recovery restores account/group/home and unit/scheduler state but leaves the copied canonical state, installed canonical unit files and installed ancillary files in place, and a retry is refused until explicit recovery.
6. **Engine cross-check (every documented branch):**

| Documented branch | Engine site | Test exercise |
|---|---|---|
| Exit 13 point | `5346-5357` | new strict-rmdir test + `test_deploy_schema_mismatch_stops_before_cutover`, `test_first_causal_error_is_preserved` |
| Three-file residue | `5224-5227`, `5240-5257` | new `test_engine_exit_13_residue…` (exact `cat >` set; no `previous-release`) |
| Owner record; interrupted cleanup | `2381-2391`, `2414-2419` | new strict test: rmdir fails, owner-record removal never issued (`locked` true) |
| Four-file residue | `5359-5374` | new post-checkpoint test: `previous-release` created and never cleaned |
| Live-owner / ownerless refusal | `2303-2325`, `2332-2348` | `test_deploy_refuses_a_lock_owned_by_another_live_run`, `…ownerless…` |
| Reclaim reasons + quarantine | `2344-2365` | existing `…reclaims_a_lock_whose_recorded_process_is_gone`, `…only_its_own_recorded_identity`, `…reclaim_move_fails`; new derived doc test |
| `mkdir` without `-p` | `653-654` | command-builder assertion only (shell missing-parent failure not testable in-engine) |
| Cleanup on success / failure | `5417-5425`, `2414-2419` | `test_deploy_happy_path_sequence`, `test_deploy_cleanup_failure_is_distinct` |
| Migration scratch/control; routine isolation | `111-112`, `268-270`, `5001-5002` | `test_production_lock_release_cleans_the_owned_scratch_area`, `test_routine_commands_never_reach_identity_migration`; new negative doc pin |
| F3 residue | `4002-4138` | source-established; no test asserts positive survival of the residue |

## 3. The five lock cases

- **Three-file (exit 13): tested.** New `test_engine_exit_13_residue_is_the_documented_three_artifacts` (behind `0026→0031`, proving the generic pair) asserts the exact residue and absent `previous-release`.
- **Four-file (post-checkpoint failure): tested.** New `test_engine_post_checkpoint_residue_adds_the_documented_previous_release`.
- **Live owner: tested (engine).** Existing remote-contract refusal tests; not duplicated.
- **Unexpected file: procedural only.** The routine engine has no content classifier; it quarantines the whole directory on reclaim. The only engine guarantee is that `rmdir` refuses a non-empty directory, now exercised by both new tests. Reported, not claimed tested.
- **Interrupted cleanup: tested.** Both new tests model a real host's non-empty `rmdir`; previously no test did (see critique).

## 4. Part B tests and mutation demonstrations

Probe `/tmp/opencode/ksi29/probe_mutations.py` (outside project state; in-memory method replacement), 4 passed:

| Mutation | Target test | Observed failure |
|---|---|---|
| `create_checkpoint` non-success guard removed | `test_production_create_checkpoint_returns_the_bundle_and_refuses_non_success` | `Failed: DID NOT RAISE ReleaseError` |
| `verify_effective_units` recognition guard removed | `test_production_verify_effective_units_accepts_installed_and_refuses_absent` | `Failed: DID NOT RAISE ReleaseError` |
| `stop_writers` order `timers,services` → `services,timers` | `test_production_quiesce_stops_admission_then_timers_then_jobs` | `AssertionError` on the returned drain order |

Control runs the three tests unmutated and passes. No test could exercise the P1 removals themselves (no caller existed); absence remains parse-verified.

## 5. Counts (declared AP route, baseline `24d2b7d`)

| Run | Result | Baseline |
|---|---|---|
| `test_nuc_release_docs.py` | **28 passed** (0.22 s) | 24 |
| `test_nuc_operator_runbook.py` | **17 passed** (0.05 s) | 17 |
| `test_kronika_identity_migration.py` | **158 passed** (0.98 s) | 155 |
| Declared full suite (`--operation test`) | **4696 passed, 8 skipped, 3 warnings, 0 failed** (688.86 s) | 4689/8/3/0 |
| `test_kronika_identity_retention.py` | **15 passed** (0.36 s) | 15 |
| Mutation probe module | **4 passed** (0.33 s) | n/a |

Delta +7 passed = 4 doc-contract tests + 3 migration tests; skip/warning counts identical.

## 6. Commit, diff, and ledger movement

`git diff --stat` at the committed tree: 5 files changed, **+432/−27** (`UBUNTU_NUC_DEPLOYMENT.md` +135, `test_nuc_release_docs.py` +178, `test_kronika_identity_migration.py` +116, `test_kronika_identity_retention.py` +21, `test_nuc_operator_runbook.py` +9). Commit `335e91d199e99e28f2585c1b25531f29bb54270c`, one non-amended local commit, no push; worktree clean, `.ap` gitlink unchanged.

- **Part A byte-unmoved:** `FROZEN_DOCUMENT_SHA256` = 86 keys, `FROZEN_ALEMBIC_SHA256` = 36 keys (computed), tracked Alembic files = 36; no frozen path in the commit; retention frozen tests green.
- **Part B still 20:** `EXPECTED_FRAMENEST_BASENAME_PATHS` = 20; ledger test green.
- **Part C movement (my measurement, with cause):** `docs` 1216 → **1229** (+13: runbook adds 15, removes 2 — the new lock section's lock directory, `.owner`, every artifact path, both reasons, both quarantine paths and the mkdir command; two replaced schema/lock bullets removed); `tests` 2142 → **2150** (+8: migration +10, docs test +6/−4, operator test −4). Host-path, capitalized, environment-token, mutation-header and unit-account scalars did not move (measured and green).

## 7. Sites no test exercises

1. The operator's unexpected-file inspection rule (engine has no routine-lock content classifier; only `rmdir` non-empty refusal is enforced, now tested).
2. `mkdir` without `-p` failing on a missing parent (shell behavior; only builder shape asserted).
3. Full-flow `own-identity` reclaim (classifier tested; full flow tested only for `abandoned-owner`).
4. Positive survival of the F3 residue after pre-write recovery (source-established; existing tests assert only "no state copy-back").
5. The operator's exact recovery command block is documentation; the residue it removes is now engine-pinned, but no test runs the commands.

## 8. Deviations, risks, missing evidence, next step

- **Deviations:** none from the grant.
- **Risks:** the routine engine's residual lock self-heals by quarantine/reclaim rather than by in-place cleanup; the prior test that claimed universal lock release is vacuous for a populated directory (see critique). The engine is frozen and was not edited.
- **Missing evidence:** no host contact by design; `mkdir` parent behavior and real `systemctl`/`sudo` remain host-verifiable only.
- **Smallest next step:** accept this cut, then proceed with publication as the separately granted later step before `C-DATA-P`; the `C6` host window additionally waits on `C-DATA-H`.

### Resolved Execution Issues / Near-Misses

- The `test` operation rejects trailing argv (`-p no:cacheprovider`); re-ran the declared form unchanged. No state change.
- The first strict-residue assertion failed because the runbook named artifacts by bare name; I corrected the runbook to the full exact paths rather than weakening the assertion.
- A wrapped-sentence pin was compared on flattened text to avoid a whitespace-fragile assertion.

### Pre-Existing Failure Classification

- **none.** Baseline is exactly `24d2b7d…`; the focused modules and the full suite were green before and after, with no new failure.

```text
Orchestration critique:
MEASURED: The prior `test_deploy_releases_the_lock_on_a_failure_inside_the_operation` cannot observe real interrupted cleanup: its fake `rmdir` succeeds while the lock directory still holds the three transferred files, so it asserts a release a real host cannot perform. Evidence: engine `release_deploy_lock` 2381-2391 with suppression at 2414-2419; fake response at `test_nuc_release_remote_contract.py:368-370`; the new strict-rmdir tests model the non-empty failure and now pin the documented residue. Effect: without this correction, an operator believed exit 13 left no lock and would misread the documented recovery branch. Smallest correction: done here in the runbook and the new engine-driven tests; a later C6-owned coverage cut may tighten that fake.
LEAD: `remote_deploy_lock`'s docstring claims the lock "is released on every exit path"; on a populated-directory exit it is not (the primary error is preserved instead). Cheapest useful check: have the next independent reader compare the corrected runbook against the engine, or fold a non-empty-`rmdir` model into the existing remote-contract fake in a future coverage cut.
```

All authority under this Worker prompt expires on submission of this report. No further implementation, second commit, push, publication, host contact or later cut is authorized by it.
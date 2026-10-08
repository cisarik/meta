All verification is complete and the commit is made. Delivering the terminal report now.

---

### Report for ORCHESTRATOR_CHAT

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session / exchange | `27` / `01` |
| Task identity | `KSI-IMPL-C6P2` |
| Persistent role | `WORKER` |
| Status | **PASS** |
| Report justification | `new-mutation` |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Starting commit | `8a5861c792122468468b3bc20934a26cb5eb1c93` |
| Tested and committed commit | `24d2b7d718eb303c79197f6e2f41c81ad479a79a` |
| Changed files | 6 authorized paths only |
| Push / publication / deployment | none |
| NUC, provider, browser contact | none |

## 1. Derived affected-method inventory (parsed, every caller resolved)

Removed (after the observation/install rewrite found no remaining caller; repo-wide parse confirms none):

| Removed site | Callers found |
|---|---|
| `migration_dropin_directory` | none after `read_migration_observation` switched to effective `DropInPaths` and `install_units` to per-unit directories |

New engine sites and their callers:

| New site | Callers |
|---|---|
| `cmd_remote_rmdir` | `RemoteMigrationHost.release_lock` |
| `cmd_remote_unit_effective_state` | `read_migration_observation` |
| `cmd_remote_root_file_evidence` | `_root_file_evidence` |
| `ObservedUnit`, `DropinInstallation` | plan payloads, `_observed_writer_units`, tests |
| `parse_effective_unit_state` | `read_migration_observation` |
| `required_current_release_sha` | `read_migration_observation` |
| `transform_sudoers_text`, `_transform_sudoers_identity`, `_transform_sudoers_command` | `read_migration_observation`; tests |
| `migration_required_console_scripts` | `read_migration_observation` |
| `RemoteMigrationHost.switch_current` | phase table (`switch-current`) |
| `_root_file_mode_octal`, `_root_file_evidence`, `_validate_root_file`, `_install_root_file` | `preserve_ancillary` |
| `_observed_writer_units` | `resume_writers` |

Changed, with all callers:

| Site | Production callers | Test callers |
|---|---|---|
| `MIGRATION_PHASES` / `_MIGRATION_PHASE_METHODS` (+`switch-current`) | `run_migration_apply`, `_cmd_migrate_preflight` output | orchestration matrix |
| `MigrationObservation` / `MigrationPlan` (+`current_release_sha`, `unit_observations`, `dropin_installations`, `sudo_rule_text`, `artifact_identity`, `required_scripts`) | `build_migration_plan`, `read_migration_observation`, `run_migration_apply`, recovery manifest | fixtures, digest-binding tests |
| `read_migration_observation` | `_cmd_migrate_preflight`, `_cmd_migrate_apply` | preflight/boundary tests |
| `RemoteMigrationHost.release_lock` | `run_migration_apply` | scratch-cleanup boundary test |
| `stop_writers` | `quiesce` | new timer-order test, P1 sim |
| `verify_capture_untouched` | phase `verify-capture` | capture-identity test, P1 sim |
| `preserve_ancillary` | phase `preserve-ancillary` | installed-mode tests |
| `prepare_release_environment` | phase `prepare-release-environment` | stateful boundary tests |
| `install_units` | phase `install-units` | stateful boundary tests |
| `start_service` | phase `start-service` | readiness tests |
| `resume_writers` | phase `resume-writers` | scheduling-preservation matrix |
| `recover_pre_write` | failure branch of `run_migration_apply` | pointer-removal test, P1 tests |
| `transform_unit_dropin_text` (structural rewrite) | `read_migration_observation` only | pure structural tests |
| `_cmd_migrate_preflight` | `main` | preflight CLI test |

Workstation pieces: `REMOTE_LAYOUT_COMMANDS`, `DEFAULT_REMOTE_LAYOUT`, `resolve_remote_layout_command`, `build_ssh_argv(remote_layout=)`, `pull_workstation_snapshot(remote_layout=)`, recovery CLI `--remote-layout`.

Callers the prompt's sample did not name: `build_ssh_argv` has exactly one production caller (`pull_workstation_snapshot`) and one unit test; `pull_workstation_snapshot` is called only from the recovery CLI `pull` dispatch; `verify_unit_executables` now has a fifth caller, `switch_current`, besides routine deploy, routine rollback and `_rollback` (2 call sites); `read_optional_release_sha`/`resolve_capture_pointer`/`_cmd_capture_transition` (P1's derivations) are unaffected by this cut.

## 2. Repair, per outcome 1–9

1. **Exact-state binding.** `read_migration_observation` now reads the required served release through `/opt/framenest/current` (missing → `EXIT_MIGRATION` "current release pointer is absent"; failed query → refusal), requires it to equal the migration release, refuses a pre-existing `/opt/kronika/current`, probes every candidate unit's effective `LoadState`, `FragmentPath`, `DropInPaths`, `UnitFileState`, `ActiveState`, reads and structurally transforms every effective drop-in, reads and structurally transforms the installed sudo rule, and hashes the engine, every canonical unit artifact, the export launcher and `poetry.lock` into `artifact_identity`. All of it enters the plan digest; apply re-reads and refuses any drift before mutation.
2. **Owned scratch.** `MIGRATION_SCRATCH_DIRECTORY=/run/kronika-identity-migration` is prepared mode 0700 by `prepare_release_environment`, which writes `MIGRATION_REMOTE_ENGINE` there. `release_lock` removes exactly that helper and the now-empty owned scratch directory, then releases the shared exclusion; it no longer touches `REMOTE_DEPLOY_DIR`.
3. **Canonical release environment.** Preparation prepares the scratch area, copies the retained release, verifies the staged lock equals the committed `poetry.lock` hash bound in the plan, installs with the frozen Poetry/CPython, re-verifies the lock, relocates the venv, publishes at `/opt/kronika/releases/<sha>`, validates every console script the canonical service units name (`kronika-production`, `kronika-backup`) as regular executables, and re-reads the retained release to prove it byte-unchanged.
4. **Guard then switch.** New phase `switch-current` runs `verify_unit_executables` against the prepared release, persists intent, atomically creates/switches `/opt/kronika/current` via `cmd_remote_atomic_switch`, and reads the link back — all before `start-service`. Pre-write recovery removes a pointer this run switched (and any `.next`).
5. **Effective units, drop-ins, timers.** Observation is systemd-effective, not guessed-file-based. `stop_writers` stops admission, then timers, then their job services. `install_units` installs the observed drop-ins from their exact source paths into the canonical unit `.d` directories and disables every obsolete autostart link at cutover. `resume_writers` restores only the observed scheduling (enabled→enable, active→start), leaving disabled/absent units untouched.
6. **Structural credential and sudo transformation.** Drop-ins are parsed directive-by-directive: `User`/`Group` identities, `LoadCredential=identifier:path`, `Exec*` executable paths (plain and `{ path=… }` forms, absolute-path required), and path-list directives; unknown/malformed/continued forms raise `EXIT_MIGRATION` during preflight. Sudo rules are parsed into principal/hosts/run-as/tags/command/args, run-as is renamed, the command path is moved to its canonical installed name, unknown forms stop preflight. The export launcher is installed root:root 0755 with digest evidence; the sudoers artifact root:root 0440 and `visudo -cf` validated; absent integrations stay absent.
7. **Workstation compatibility.** `kronika-recovery pull` gained `--remote-layout {old,new}` (default `old`) selecting one of two fixed tuples; unknown keys raise `WORKSTATION_REMOTE_LAYOUT_INVALID` before any process starts; no arbitrary command can be supplied.
8. **Readiness, ingress, capture.** `start_service` now calls `verify_local_readiness`; `verify_ingress` remains a phase and fails a replacement that did not take effect after a healthy local start; `verify_capture_untouched` compares fresh `_snapshot_capture_identity` snapshots before/after and refuses any changed runner/browser identity or lost active state.
9. **No other cuts.** No `C6-V`, runbook, data, local, ops or C7 work; no second deployment system; no host execution.

## 3. Production-adapter effect matrix and executable release probe

`RemoteBoundary` is stateful and rejects unknown commands. Effects modelled: files/dirs/links/permissions/hashes, unit registration from written unit files, `.d` drop-in registration, systemd show (layout probe, exec properties, effective state, actions), marker presence/read, poetry lock/check/env/install (installs a real staging venv), venv relocation, release verification, chown/chmod, atomic writes and renames, `ln -s`, `readlink`, readiness `systemd-run`, capture identity, tamper and failure injection. Acceptance tests and what they model:

| Test | Effect asserted |
|---|---|
| missing current pointer / failed query | preflight refusal, no command side effect |
| different current release; pre-existing new pointer | refusal |
| unknown drop-in directive; unknown sudo form; disappeared drop-in | preflight refusal |
| vendor unit + vendor drop-in | effective fragment/drop-ins observed, transformed bytes bound |
| digest binding across units/current/artifacts/drop-ins | five distinct digests |
| intervening drift before mutation | apply refuses; no mutation command |
| scratch area prepared and cleaned | mode 0700 dir, helper there, `REMOTE_DEPLOY_DIR` untouched, removed at release |
| tampered committed lock; changed retained release; non-executable console script | preparation refusals |
| pointer guard/switch | guard command text before `ln -s`; link target equals final release; no switch without executables |
| readiness | `systemd-run` issued; failure after start refuses |
| ancillary modes | launcher 0755 + repo bytes; sudoers 0440 + transformed bytes; `visudo -cf` |
| capture identity change | refusal; identical identity passes |
| ingress failed edit | refusal with healthy local check |
| scheduling preservation | enabled/active restored; disabled/inactive untouched |
| timer stop order | timer before its job |
| non-unit artifacts | observed by existence; never stopped or systemd-queried |
| stop-writers order, pointer removal | as above |

**Executable release probe.** `test_prepared_release_console_scripts_execute_in_an_isolated_fixture` builds a real staging release whose console scripts carry staging-path shebangs, runs the production `relocate_venv_shebangs`, renames staging to the final path, then executes four prepared scripts as programs with the prepared interpreter: `framenest-db`, `framenest-backup`, `kronika-production`, `kronika-backup`. Observed stdout: `prepared-db-ok`, `prepared-backup-ok`, `prepared-production-ok`, `prepared-backup-ok`; the canonical `kronika-production` bytes contain no retired token.

## 4. Guard-failure demonstrations (named mutation → observed failure)

| # | Mutation applied, then reverted | Targeted test | Observed failure |
|---|---|---|---|
| 1 | digest comparison → `if False` | drift rejection | expected `EXIT_MIGRATION`, got `EXIT_TRANSPORT 20` |
| 2 | missing-pointer refusal → `if False` | missing pointer | `EXIT_TRANSPORT 'unsafe remote path'` instead of migration refusal |
| 3 | structural drop-in transformer replaced by old token replacer | unknown-directive + structural refusal | 2 failed, `DID NOT RAISE` |
| 4 | `verify_unit_executables` call removed from `switch_current` | non-executable scripts | `DID NOT RAISE` |
| 5 | `self.verify_local_readiness()` removed from `start_service` | readiness wiring | `any(systemd-run) == False` |
| 6 | identity comparison removed | capture identity change | `DID NOT RAISE` |
| 7 | scratch `mkdir 0700` removed | scratch preparation | `assert 493 == 448` (0755 vs 0700) |
| 8 | observed timer gating replaced by `if True` | scheduling preservation | disabled case `'enabled' == 'disabled'` |
| 9 | launcher mode `0755` → `0644` | ancillary modes | `assert 420 == 493` |
| 10 | unmatched sudo line → skip instead of raise | unknown sudo form | `DID NOT RAISE` |
| 11 | committed-lock comparison → `if False` | tampered lock | `DID NOT RAISE` |
| 12 | retained-release guard → `if False` | changed retained release | `DID NOT RAISE` |
| 13 | final console-script validation → `continue` | non-executable console script | `DID NOT RAISE` |

Absent-input behavior is also pinned: absent/query-failed current pointer, absent observed drop-in, absent unit, absent optional integrations (no commands), and `MIGRATION_DIRECTORY` overlap all refuse rather than pass vacuously.

## 5. Workstation selection evidence

`REMOTE_LAYOUT_COMMANDS["old"]` is the retained tuple `("sudo","-n","-u","framenest","--","/usr/local/libexec/framenest-catalog-export-v1")`; `["new"]` is `("sudo","-n","-u","kronika","--","/usr/local/libexec/kronika-catalog-export-v1")`. Default `old`; `build_ssh_argv` and `pull_workstation_snapshot` append only the selected tuple. `resolve_remote_layout_command` rejects `"anything"`, `""`, `"; rm -rf /"`, `"old new"` and `"OLD"` with `WORKSTATION_REMOTE_LAYOUT_INVALID` before spawn. The CLI parser accepts exactly `old|new`, defaults to `old`, and the `pull` dispatch passes the selection through (monkeypatched-capture test asserts `remote_layout == "new"`).

## 6. Focused module, full-suite and retention counts

Declared route, in the required order, at the tested tree:

| Run | Result | Elapsed |
|---|---|---|
| Focused migration module | **155 passed, 0 failed** | 1.08 s pytest |
| Focused recovery-client module | **10 passed, 0 failed** | 1.76 s wall |
| Declared full Python suite | **4689 passed, 8 skipped, 3 warnings, 0 failed** | 690.53 s (11:30) |
| Retention module | **15 passed, 0 failed** | 0.37 s |

Baseline difference: `4648/8/3/0` → `4689/8/3/0`, i.e. **+41 collected, all passing**. Decomposition: migration module `117` (C6-P1 report) → `155` = +38 (32 new test functions, the new `switch-current` failure-injection parameter, the new resume-writer parameterization and the pure-guard test); recovery CLI `7` → `10` = +3. Skips, warnings and zero failures unchanged.

## 7. Commit, diff, Part A / B / C

`git diff --stat`:

```text
 deploy/ubuntu/kronika_release.py                   | 1050 ++++++++++++--
 src/kronika/adapters/cli/recovery.py               |   10 +
 .../persistence/catalog_backup_workstation.py      |   38 +-
 tests/contract/test_kronika_identity_migration.py  | 1449 +++++++++++++++++++-
 tests/contract/test_kronika_identity_retention.py  |   60 +-
 tests/contract/test_recovery_cli.py                |   89 ++
 6 files changed, 2511 insertions(+), 185 deletions(-)
```

Commit `24d2b7d718eb303c79197f6e2f41c81ad479a79a`, one local non-amended commit on `main`, working tree clean, no push.

- **Part A byte-unmoved:** frozen-document and frozen-Alembic byte tests pass. Computed at report time: `FROZEN_DOCUMENT_SHA256` = **86** keys; `FROZEN_ALEMBIC_SHA256` = **36** keys.
- **Part B still 20:** basename ledger test passes; `EXPECTED_FRAMENEST_BASENAME_PATHS` = **20** members, no path added or removed.
- **Part C movement (measured, re-pinned with per-file cause):** `tests` 2049→**2142** (+93: migration test file +92 from the C6-P2 fixtures/tests naming former layout, drop-in/sudo raw texts, unit names and host literals; recovery test +1 for the retained-tuple pin); `deploy` 244→**250** (+6: `kronika_release.py` adds nine structural token guards and removes the two routine-scratch helper paths and the old token-replacement regex); host literals `/opt/framenest` 223→**226**, `/etc/framenest` 83→**86**, `/var/lib/framenest` 120→**121**, `/mnt/framenest-catalog-offdevice` 23→**25** (all in the migration test's new fixtures/assertions; engine adds no host literal); `User=framenest`/`Group=framenest` 8→**9** each (new structural systemd fixture). `/var/cache/framenest` 31 and `src` 1690 unmoved; environment tokens, bare spellings, mutation header, capitalized counts, content-path membership, console count and per-tree file counts unmoved. Part C was re-measured after each late test addition (2049→2124→2140→2141→2142) and never tuned to make a failing run pass.

## 8. Sites no test exercises

- `resume_writers` combinations `enabled+inactive` and `disabled+active`.
- `switch_current` link-readback mismatch branch (link switched to something other than the target).
- `release_lock` when the scratch directory is non-empty (rmdir suppression) and when helper removal fails.
- `_root_file_evidence` `absent`/`unsafe` classifications and its `query-failed` path; `_validate_root_file` wrong-owner branch (wrong mode is tested).
- `preserve_ancillary` canonical-already-present sudo rule path (`visudo` on the retained canonical rule).
- `cmd_remote_unit_effective_state` and `cmd_remote_root_file_evidence` executed against a real systemd host; only command text and the boundary model are exercised.
- `transform_unit_dropin_text` structured `{ path=… }` executable form and its non-absolute refusal.
- `transform_sudoers_text` comment/blank-line preservation (no comments in the fixtures).
- `migration_required_console_scripts` and `read_migration_observation` against a canonical-only export installation (the fakes always find the former candidate first).
- `install_units` copying an observed non-unit `.conf` artifact to its canonical name.
- `_observed_writer_units` fallback to the plan when the live journal has no substep.
- `verify_capture_untouched` runner-active-drop branch alone (identity-change branch is tested).

## 9. Deviations, risks, missing evidence, next step

- **Deviation (clarifying, not scope):** the four `.conf` entries in `MIGRATION_UNIT_ARTIFACTS` are not systemd units; they are observed by file existence, copied like before, and explicitly excluded from `stop_writers`/`observe_writer_state` so an installed configuration file can never be passed to `systemctl stop`.
- **Risk:** the boundary is a model; real `systemctl show` behavior for a file-installed-but-not-yet-loaded unit and the real ordering of `DropInPaths` remain host-verifiable only. The adapter fails closed on `query-failed`.
- **Risk:** `_install_root_file` places the file via atomic rename (0600 root) and then chmods it; the file is never world-readable in the window, only briefly non-executable.
- **Missing evidence:** no host execution of any phase (by design); no real systemd, sudoers or Poetry execution; `C6-V` and the host window remain prerequisites.
- **Collapsing pairs:** no artifact-pair acceptance set changed membership; `MIGRATION_UNIT_ARTIFACTS` exact membership is now independently pinned by a new literal test, and `MIGRATION_ENVIRONMENT_ARTIFACT`/`MIGRATION_EXPORT_ARTIFACT` membership with it.
- **Smallest next step:** issue the independent **C6-V** read-only review of this exact commit (`24d2b7d`) plus published history before any C6 host window; do not add another implementation cut first.

### Resolved Execution Issues / Near-Misses

- The first focused run (88 failed) was the expected constructor breakage from the widened plan; all were fixture updates, no engine defect.
- The `RemoteBoundary` initially matched any command containing the substring `cat`, which also matched `catalog` paths in sudo-rule probes and made preflight read the wrong object; the branch now matches `sudo -n cat ` only.
- The `cp -a` boundary branch parsed the destination past a newline and skipped the following `rm -rf`; both effects are now modelled, which is what makes the scratch/preparation tests non-vacuous.
- Mutation M-5's first expression did not match because `start_service` is followed by `verify_local_readiness`, not `record_tailscale_state`; the no-op was detected (test passed unchanged) and the mutation was re-run with the correct anchor, then reverted.
- The `(root) NOPASSWD: /path` rebuild dropped the original tag/command space; the transformer now preserves tag spacing and the pure-guard test pins exact preservation.
- Two intermediate full-suite runs (4687, 4688) preceded the final one because tests were still being added; all earlier full runs are superseded by the final 4689 run at the committed tree.
- The workstation unit test module (`tests/unit/infrastructure/backup/test_catalog_backup_workstation.py`) was inspected as a direct exerciser of `build_ssh_argv`; the default path is unchanged and it was left unmodified, with the new selection covered in the authorized `test_recovery_cli.py`.

### Pre-Existing Failure Classification

- **No pre-existing failure:** the authorized baseline was `4648 passed, 8 skipped, 3 warnings, 0 failed`.
- **Expected scalar movement:** the only red focused results during development were the Part C retention counts before their re-pin; each was re-measured from the tree and re-pinned with the per-file arithmetic above.
- **Latent defects repaired by this cut:** unwired `verify_local_readiness`; activity-only capture verification; pointer never switched before startup; helper written into the routine deploy scratch directory; structural directive/sudoers transformation replaced by token substitution; timer scheduling lost on resume; installed ancillary modes unvalidated; current-pointer absence observed as transport error.
- **Retained by design:** `.conf` artifacts remain file-copied non-units; `MIGRATION_ENVIRONMENT_ARTIFACT` remains a defined-but-unused literal (pre-existing); real-systemd behavior is carried to C6-V/host observation.

```text
Orchestration critique:
MEASURED: The prompt's anchors were accurate and the stateful boundary from C6-P1 was sufficient to close all nine outcomes. Two derivation findings the prompt did not name shaped the repair: the four `MIGRATION_UNIT_ARTIFACTS` `.conf` entries are not systemd units and would have been both invisible to `systemctl show` and fatal to `stop_writers`; and the applied structural transformer had to preserve sudoers tag spacing. Effect: without the explicit non-unit handling, a host carrying those files would have been silently skipped or failed at quiesce. Smallest correction: keep the new non-unit existence path and its literal-membership test as the contract for those four entries.
LEAD: Real `systemctl show -p DropInPaths` output for a vendor-installed unit and the actual installed sudoers mode on the NUC are unverified here. Cheapest useful check: a read-only C6-V or C6 preflight that reports effective fragments, drop-in paths and installed file modes without mutating them.
```

All authority under this Worker prompt expires on submission of this report. No `C6-V`, runbook, data, local, ops, C7 or host action was performed or is authorized by it.
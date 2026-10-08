# Authoritative Worker prompt — Worker session 27, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `27`, exchange `01`. Stored under the
Meta filename mapping as `27_implementation_00.md`, with report destination
`27_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 27
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C6P2 — complete production activation, integration preservation and readiness
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This cut completes the production migration sequence that
`C6` will execute against the live NUC. `C6-P1` repaired exclusion, control-state
placement, durable intent and recovery; `C6-P2` must make the remaining phases
real: bind preflight and apply to the exact observed state, prepare the release
environment at its canonical path, guard and switch the canonical pointer before
startup, observe and preserve effective units and scheduling, transform the
credential and sudo directives structurally, stage the workstation command
selection, and replace the activity-only capture check with real identity
comparison. The production adapter is still not host-ready until this cut and
the independent `C6-V` review pass.

This is work item **C6-P2** from the accepted closure plan at
`25_report_00.md` section 2.2, with section 1 C6 findings as the defect list and
section 6 as the binding method. `C6-P1` is complete and published nowhere yet;
its commit is your baseline.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
sections 2.2 and 1 are your specification. Read them in full. Required outcomes:

1. **Bind preflight and apply to exact observed state.** The plan digest and
   apply must be bound to the exact current release, source/artifact identity and
   observed effective configuration; any intervening drift between preflight and
   apply is rejected before mutation.
2. **Owned scratch area.** The migration must prepare its remote helper in an
   owned, prepared scratch area instead of uploading into the routine deployment
   scratch directory `REMOTE_DEPLOY_DIR` (line 97; helper use at 3370). Once the
   helper lives there, `release_lock`'s exact owned-helper cleanup must be
   updated consistently with the new location rather than removed blindly.
3. **Canonical release environment.** Prepare and validate the exact release
   environment at the canonical path using the committed lock and the frozen
   tooling, and validate the final executable paths of the installed console
   scripts. Do not modify the retained old release.
4. **Guard, then switch the pointer before startup.** Apply the installed-
   executable guard (`verify_unit_executables`, line 1719) and then atomically
   create/switch `/opt/kronika/current` before the service starts, reusing
   `cmd_remote_atomic_switch` (line 973). Do not leave the pointer unswitched
   while the new unit starts.
5. **Observe effective units, drop-ins and timers.** Observe effective unit
   fragments and drop-ins and timer enablement and activity from the host,
   including installations outside a guessed `/etc` filename. Stop timers before
   draining their jobs; disable obsolete autostart links at cutover; restore only
   the previously intended canonical scheduling on success. Preserve absent
   optional integrations as absent.
6. **Structural credential and sudo transformation.** Parse supported systemd
   directives and sudo rules structurally, including `LoadCredential=identifier:path`,
   executable paths and run-as identity. Unknown forms stop preflight. Install
   the export launcher root-owned mode `0755` and the validated narrow sudoers
   artifact with its required restrictive mode; only installations already
   present are migrated.
7. **Workstation compatibility selection.** Stage the temporary explicit
   `kronika-recovery pull --remote-layout old|new` selection, defaulting to
   `old` during preparation. It selects one of two fixed command tuples and can
   never execute an arbitrary command. `C6` will switch the authorized operator
   invocation to `new`; `C7-B` makes canonical operation the default and removes
   the old choice. The selection lives in the recovery client.
8. **Readiness, ingress and capture identity.** Call real local readiness after
   startup by wiring `verify_local_readiness` (line 3549) into the production
   sequence rather than deleting the evidence gap. Verify the intended ingress
   after its bounded replacement; a failed ingress edit with a healthy local
   service is a failed cutover. Replace the activity-only capture check
   (`verify_capture_untouched`, line 3112) with a before/after capture runtime
   identity comparison using the existing `_snapshot_capture_identity`
   (line 4916) and `cmd_remote_capture_identity` (line 1123).
9. **Do not implement other cuts.** No `C6-V`, no `C-RUNBOOK`, no `C-DATA`, no
   `C-LOCAL`, no `C-OPS`, no `C7`. Do not add a second deployment system or a
   second manager. Do not execute any migration against a host.

## Verified starting state, measured by the Orchestrator on 2026-10-08

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                8a5861c792122468468b3bc20934a26cb5eb1c93
Remote origin:                https://github.com/cisarik/kronika
Public main:                  3194f48f6b343a460ed5988d92999f91ef999a79
                              (the baseline commit is local and unpublished, by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 8a5861c:   4648 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
Focused migration module:     117 passed
```

**NUC state is carried, not measured here.** This cut has no host authority.
The carried installed release is `3194f48`, layout `old`, capture release
`94e605c17b881461fad3e22fd8c7fca32cb93976`, schema `0035`, service active; none
of it may be assumed by the Worker and none of it is needed for this
repository-only cut.

Facilities to reuse rather than re-author, verified at the baseline:

```text
exclusion                     acquire_deploy_lock (2313), shared by P1
atomic pointer switch         cmd_remote_atomic_switch (973)
installed-executable guard    verify_unit_executables (1719), unit_executables_from_show (1667)
capture identity probe        cmd_remote_capture_identity (1123), _snapshot_capture_identity (4916)
release preparation           prepare_release_environment (3313)
ancillary preservation        preserve_ancillary (3236), cmd_remote_validate_sudoers (2622)
unit installation             install_units (3465), start_service (3542), resume_writers (3634)
drop-in transformation        transform_unit_dropin_text (3817)
workstation pull              pull_workstation_snapshot (catalog_backup_workstation.py:365),
                              validate_ssh_target (:735), CLI src/kronika/adapters/cli/recovery.py
host constants                canonically named target paths and MIGRATION_UNIT_ARTIFACTS (301)
```

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py`; edit
  `tests/contract/test_kronika_identity_migration.py`; edit
  `src/kronika/adapters/cli/recovery.py`; edit
  `src/kronika/infrastructure/persistence/catalog_backup_workstation.py`; edit
  `tests/contract/test_recovery_cli.py`; edit any further test module you derive
  as a direct exerciser of the changed recovery-client selection, naming it in
  the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this cut moved, with the arithmetic
  cause stated; create exactly one local commit on `main`.

Negative authority: every other path; any dependency or lockfile change; any
  change to `pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen
  document or Alembic revision; publication; push; force; amend; branch; stash;
  `docs/UBUNTU_NUC_DEPLOYMENT.md` (C-RUNBOOK owns it and will reflect P1/P2
  behavior); the retained wrappers `deploy/ubuntu/framenest_release.py`,
  `deploy/ubuntu/framenest-release`; any NUC contact or SSH; any invocation of
  `migrate-identity`, `deploy`, `rollback` or `activate-capture` in any mode;
  any provider, browser or capture contact; any secret, personal Fish
  configuration or browser-profile read. If a necessary change falls outside the
  positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 8a5861c792122468468b3bc20934a26cb5eb1c93
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 8a5861c792122468468b3bc20934a26cb5eb1c93 --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run`, including as a text editor.
  Read-only Git inspection is allowed; exactly one `git add <exact paths>` and
  one `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only. No host,
  service, database, provider, browser or account side effect.
Browser authority: none.
```

## Verification

1. **Production-adapter tests, effects not echoes.** Extend the stateful
   production boundary added by `C6-P1` so it models effects and rejects unknown
   commands; a fake that returns success for an unmodelled command is itself a
   defect. Required cases, at minimum: missing current pointer; missing scratch
   parent; disabled or vendor-installed units and drop-ins; timer enablement and
   activity preservation across quiesce and resume; `LoadCredential=identifier:path`,
   executable-path and run-as transformation; unknown directive form stops
   preflight; export launcher mode and sudoers mode; both fixed workstation
   command choices and the rejection of any other string; ingress replacement
   failure after a healthy local start; capture-identity change detected.
2. **Verify the release by executable behavior in an isolated fixture**, not by
   transcript substrings alone: run the prepared console scripts or an equivalent
   executable probe against a fixture, and report what was executed.
3. Demonstrate that each new guard fails when its protection is removed, naming
   the mutation and the observed failure. Whenever a guard reads a path, a name
   or an environment value, prove what happens when the input is absent.
4. Run, through the declared route: the focused migration module, the focused
   recovery-client module, then the declared full Python suite, then the
   retention module. Report every count and any difference from the
   `4648/8/3/0` baseline.
5. Report **every moved or removed site that no test exercises**, and every
   caller your derivation found that this prompt's sample did not name.
6. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and per-file
   cause for any Part C movement. Never tune a pin until the suite is green.

## Derivation and defect-pattern discipline

```text
 1. Derive the affected method/site list by PARSING the engine, the recovery
    client and their tests. This prompt's anchors are locators, not an inventory.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Reject a guard that can pass vacuously when its input is absent.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit: production caller, test caller, historical
    compatibility, excluded prose or negative assertion.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** For every acceptance set this cut touches, name whether a
collapse raises or fails silently. `MIGRATION_UNIT_ARTIFACTS` (line 301) is an
explicit literal tuple: preserve and test its exact membership independently of
the writer. Do not shrink it silently.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a necessary change falls outside the positive scope; if an unknown
  systemd or sudo directive form cannot be made to fail preflight safely; if a
  frozen hash, Part A or Part B moves; if a Part C re-pin cannot be reproduced
  from your own measurement; if a proposed change would touch C6-V, C-RUNBOOK,
  C-DATA, C-LOCAL, C-OPS or C7 scope; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded result.

Completion: outcomes 1-9 implemented and tested with stateful production-adapter
  tests that model effects; guard-failure demonstrations; focused modules, full
  declared Python suite and retention module green through the declared route;
  one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `27_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no host contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `27` and exchange `01` unchanged. Then:

1. Your derived affected-method inventory, before and after, with every caller.
2. The repair, per outcome 1-9, with before/after semantics.
3. The production-adapter effect matrix and the executable release probe.
4. Guard-failure demonstrations, each with its named mutation.
5. The workstation selection evidence: both fixed tuples, the default, and the
   rejection of an arbitrary command.
6. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
7. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and any
   Part C movement with cause.
8. Every site no test exercises.
9. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  sections 2.2 and 1 in full.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/26_report_00.md`
  in full — the P1 baseline you extend, including its untested-site list.
- `deploy/ubuntu/kronika_release.py`: the facility anchors named above, the full
  `RemoteMigrationHost`, `run_migration_apply`, the phase table, `preserve_ancillary`,
  `prepare_release_environment`, `install_units`, `start_service`,
  `verify_local_readiness`, `resume_writers`, `transform_unit_dropin_text`,
  `verify_capture_untouched`, `verify_unit_executables` and `cmd_remote_atomic_switch`.
- `tests/contract/test_kronika_identity_migration.py` in full — especially the
  production boundary tests added by P1.
- `src/kronika/adapters/cli/recovery.py`, `src/kronika/infrastructure/persistence/catalog_backup_workstation.py`
  and `tests/contract/test_recovery_cli.py` — for the `--remote-layout` selection.
- `deploy/systemd/` and `deploy/ubuntu/kronika-catalog-export-v1` — the canonical
  artifacts the migration installs.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the diff is inside the
authorized paths; the pointer switch is guarded and precedes startup; no host
constants or routine deployment behavior changed beyond the specified outcomes;
the production-adapter tests model effects and fail on their own mutations; the
full suite is green at the reported commit; and Part A and Part B are unmoved.
After acceptance, `C6-V` is the next cut: a genuinely fresh, read-only
independent readiness review of the published candidate. **No C6 host window
may be prepared until C6-V reports PASS.** Publication of the accumulated
commits remains a separate grant.

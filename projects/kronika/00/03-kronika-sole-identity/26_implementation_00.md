# Authoritative Worker prompt — Worker session 26, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `26`, exchange `01`. Stored under the
Meta filename mapping as `26_implementation_00.md`, with report destination
`26_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 26
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C6P1 — repair migration exclusion, journalling, recovery and copy verification
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the first engine-changing cut after the accepted
closure plan, and it repairs the machinery that `C6` will execute against the
live NUC. Mistakes here are invisible to the existing suite: the migration tests
drive `SimulatedMigrationHost`, which replaces production methods, so they are
green while the production adapter has a deterministic journal/destination
conflict, writes control state before it holds any exclusion, and never switches
the canonical pointer. The proof of this cut is stateful production-adapter
tests, not another green run of the simulation.

This is work item **C6-P1** from the accepted closure plan at
`25_report_00.md` section 2.1, with its section 1 C6 findings as the defect list
and section 6 as the binding method.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
is your specification. Read it in full. The following outcomes are required; the
plan states the reasoning and the proof obligations in full.

1. **One exclusion mechanism.** Acquire the routine deployment exclusion before
   writing any migration control state, and make migration and routine
   deploy/rollback share it so the two can never run concurrently.
   `acquire_deploy_lock` at `deploy/ubuntu/kronika_release.py:2287` is the
   existing implementation; reuse it rather than authoring a second lock. The
   current migration lock (`MIGRATION_LOCK_DIR` at line 254) is separate and is
   acquired only after the journal is already written.
2. **Control state outside every copy destination.** `MIGRATION_DIRECTORY =
   "/var/lib/kronika/identity-migration"` (line 251) sits inside the
   `/var/lib/kronika` tree that `copy_state` (line 2971) copies, while
   `copy_state` requires every destination to be absent at line 2977. Move the
   journal and recovery manifest to a root-only location outside every
   state-copy destination, write them atomically, and preserve an existing
   incomplete journal so a fresh apply refuses until an explicit recovery. The
   destination set is derived from the plan, not assumed; verify the chosen
   location against every `copy_moves` source.
3. **Durable intent and a conservative writes boundary.** Persist phase intent
   and substep outcomes durably. Record a conservative `writes_possible` (or
   equivalent) boundary before the new service is started, so recovery never has
   to infer it from a completed-phase list alone. A completed phase must be
   recorded only after its work actually completed.
4. **Recovery correctness.** Pre-write recovery restores the observed account,
   group, home, unit and scheduler state even after a partially executed
   operation. Post-write recovery preserves current data and requires forward
   recovery or a separately authorized reverse migration; it must never restore
   stale copied state. Make permission/query failures distinguishable from
   "object absent" or "no processes" so a failed query cannot be read as a
   successful absence.
5. **Copy verification.** Verify file type, symlink target, permission,
   ownership and content; never overwrite an unrelated destination. The current
   `copy_state` accepts an absent destination and then creates it; the new logic
   must refuse a populated unexpected destination without destroying it.
6. **Remove the three dead builders** on this first engine touch:
   `cmd_remote_unit_enabled_state` (line 2457),
   `cmd_remote_switch_layout_release` (line 2533) and
   `migration_unit_required` (line 2753). Re-derive callers in the engine, the
   tests and the operator scripts before removing; if any real caller exists,
   stop and report instead.
7. **Do not implement C6-P2.** The pointer switch and release preparation, unit
   installation and activation, ingress replacement, workstation-command
   selection and timer enablement capture belong to `C6-P2`. Do not change the
   installed-host constants or the routine deployment path beyond what outcomes
   1–6 require. `verify_local_readiness` (line 3354) is a discovered no-caller
   method: leave its wiring decision to `C6-P2`; do not delete the method inside
   this cut.

## Verified starting state, measured by the Orchestrator on 2026-10-07

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                3194f48f6b343a460ed5988d92999f91ef999a79
Remote origin:                https://github.com/cisarik/kronika
Public main:                  3194f48f6b343a460ed5988d92999f91ef999a79, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Node:                         v26.8.2
Python declared test:         4625 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
```

**NUC state is carried, not measured here.** This cut has no host authority and
must not attempt any. The carried installed release is `3194f48`, layout `old`,
capture release `94e605c17b881461fad3e22fd8c7fca32cb93976`, schema `0035` and
service active; none of that may be assumed by the Worker, and none of it is
needed for this repository-only repair.

Defect anchors verified independently by the Orchestrator at `3194f48`:

```text
journal path inside copied tree   kronika_release.py:251-253 versus copy_state 2971-2977
journal before exclusion          run_migration_apply writes manifest/journal at
                                  3596-3597, acquire_lock at 3598
separate migration lock           MIGRATION_LOCK_DIR at 254; routine lock at 2287
no canonical pointer switch       cmd_remote_switch_layout_release:2533 has no caller
no readiness wiring               verify_local_readiness:3354 has no caller
timer enablement loss             resume_writers:3439-3455 enables+starts every
                                  installed `.timer` regardless of prior state
drop-in transformation gap        transform_unit_dropin_text:3565
capture check is activity-only    verify_capture_untouched:2940 (C6-P2 scope)
```

The migration tests at `tests/contract/test_kronika_identity_migration.py`
(1473 lines) are green and must stay green, but `SimulatedMigrationHost`
(line 611) substitutes production methods through `__getattr__` (line 680) and
`_run_phase` (line 696), and its failure injection occurs before simulated phase
work. They therefore do not exercise the production `copy_state`,
`write_journal`, `write_recovery_manifest`, `acquire_lock`, `release_lock`,
`recover_pre_write` or `recover_post_write`. Your new tests must exercise the
production methods over an owned simulated remote filesystem/process boundary.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py`; edit
  `tests/contract/test_kronika_identity_migration.py`; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this cut moved, with the arithmetic
  cause stated; create exactly one local commit on `main`.

Negative authority: every other path; any dependency or lockfile change; any
  change to `pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen
  document or Alembic revision; publication; push; force; amend; branch; stash;
  the retained wrappers `deploy/ubuntu/framenest_release.py` and
  `deploy/ubuntu/framenest-release`; `deploy/ubuntu/kronika-release`; any NUC
  contact or SSH; any invocation of `migrate-identity`, `deploy`, `rollback` or
  `activate-capture` in any mode; any provider, browser or capture contact; any
  secret, personal Fish configuration or browser-profile read. If a necessary
  change falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 3194f48f6b343a460ed5988d92999f91ef999a79
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 3194f48f6b343a460ed5988d92999f91ef999a79 --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run`, including as a text editor.
  No JavaScript suite is required or expected to change.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); exactly one `git add <exact paths>`
  and one `git commit` for the authorized commit; no other Git write.

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

1. **Reproduce the defect before editing.** Write one stateful test that drives
   the production `RemoteMigrationHost` over an owned simulated remote
   filesystem/process boundary and shows the current journal-inside-copy
   destination conflict failing at `3194f48`, plus a second showing that control
   state is written before any exclusion is held. Record the exact failure
   output before any edit. If you cannot reproduce them, stop and report — do
   not edit.
2. After the repair, the same tests pass, and the required matrix is present:
   concurrent invocation refusal (a second migration and a routine deploy
   cannot interleave); journal-write interruption; populated-destination
   collision without destruction; partial group/user rename; startup succeeds
   but acknowledgement/journal write fails; no stale-data rollback after
   possible writes; and recovery selection driven by the durable intent record
   rather than inference.
3. Demonstrate that each new guard fails when its protection is removed, by
   naming the mutation and its observed failure. A test that passes while
   checking nothing is a defect class this whole has paid for twice: whenever a
   guard reads a path, a name or an environment value, prove what happens when
   that input is absent.
4. Run, through the declared route: the focused migration module; then the
   declared full Python suite; then the retention module. Report every count,
   the full-suite elapsed time, and any difference from the `4625/8/3/0`
   baseline.
5. Report **every moved or removed site that no test exercises**, and every
   caller or reference your derivation found that this prompt's sample did not
   name.
6. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20. If a Part C scalar moved, show your own
   measurement and the per-file cause; never tune a pin until the suite is
   green.

## Derivation and defect-pattern discipline

```text
 1. Derive the affected method/site list by PARSING the engine and its tests.
    This prompt's defect anchors are locators, not an inventory.
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
collapse raises or fails silently. The plan records: four analysis identities use
`accepted_durable_identity` (duplicates raise); twelve other artifact pairs use
literal sets/tuples (silent). Demonstrate the silent category if this cut
touches one.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it, do
not inherit any other figure.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a real caller of any dead builder exists; if the defect cannot be
  reproduced first; if a necessary change falls outside the positive scope; if a
  proposed repair would change C6 host-facing behavior beyond outcomes 1-7; if a
  frozen hash, Part A or Part B moves; if a Part C re-pin cannot be reproduced
  from your own measurement; if context pressure reaches the point where a
  bounded rotation is cheaper than a degraded result.

Completion: the production adapter repairs implemented and tested with stateful
  tests that fail before and pass after; the three dead builders removed; the
  focused module, full declared Python suite and retention module green through
  the declared route; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `26_report_00.md` in
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
echoing `kronika-sole-identity`, session `26` and exchange `01` unchanged. Then:

1. The defect reproduction: what fails at `3194f48`, with exact output.
2. Your derived affected-method inventory, before and after, with every caller.
3. The repair, per outcome 1–6, with the before/after semantics.
4. The guard-failure demonstrations, each with its named mutation.
5. The concurrency, journal-interruption, destination-collision, partial-rename,
   acknowledgement-failure and recovery-selection evidence.
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
  in full; section 2.1 is your specification, section 1 is the defect list and
  section 6 is the method.
- `deploy/ubuntu/kronika_release.py`: constants 240–330; `cmd_remote_*` helpers
  2400–2560; exclusion 2287–2340; migration plan, journal and lock 2592–2890;
  `RemoteMigrationHost` 2764–3580; recovery 3458–3580; `run_migration_apply`
  3585–3660; `_cmd_migrate_identity` 3931 onward.
- `tests/contract/test_kronika_identity_migration.py` in full — especially
  `SimulatedMigrationHost`, `test_failure_injection_after_every_phase`, the
  recovery tests and the journal-order test.
- `tests/contract/test_kronika_identity_retention.py`, the Part C helpers and
  pins; do not weaken it to make your change pass.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` recovery sections — read for context only;
  `C-RUNBOOK` owns their correction, and this cut must not edit them.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: the defect was
reproduced before the repair; the diff contains no pointer-switch, unit-install
or C6-P2 implementation; the three dead builders are gone with no caller; the
new tests exercise production methods rather than the simulation and fail when
their protection is removed; Part A and Part B are unmoved; and the full suite
is green at the reported commit. Publication and any host preparation remain
separate grants. **`C6` must not be prepared for the host window until C6-P1,
C6-P2 and the independent C6-V review are complete.**

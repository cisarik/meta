# Authoritative Worker prompt — Worker session 29, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `29`, exchange `01`. Stored under the
Meta filename mapping as `29_correction_00.md`, with report destination
`29_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 29
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-CRUNBOOK — correct the release-lock and schema-continuation runbook
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The deployment runbook's recovery section currently describes
a failure point and a schema state that do not match the real host or the engine
as repaired by `C6-P1`/`C6-P2`, and an operator following it during an interrupted
deployment could delete the wrong object or follow a wrong recovery branch. The
documentation is part of the safety envelope for the `C6` window, so correctness
here is a named risk, not prose polishing.

This is work item **C-RUNBOOK** from the accepted closure plan at
`25_report_00.md` section 2.4, extended by the independent findings of
`C6-V` (`28_report_00.md`).

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.4 and `28_report_00.md` sections 3 and 8 are your specification. Read
them in full.

### Part A — the runbook and its contract tests

Correct `docs/UBUNTU_NUC_DEPLOYMENT.md` and the contract tests that pin it.

1. **Separate the three recovery cases** and state each one's precondition and
   stop rule: (a) a live lock owner → stop; (b) a proven stale or ownerless
   residue → inspect the exact phase, ownership and contents before any
   authorized recovery; (c) `migration-required` → follow the observed
   current/target schema state and the current helper's actual cleanup behavior.
2. **Document `previous-release`** where the deploy phase creates it, and the
   owner-record lifecycle (the `.owner` sibling record, its meaning and its
   absence).
3. **Replace the hardcoded schema example.** The current text pins
   `current_revision=0032`, `head_revision=0033` and
   `current_revision=head_revision=0033`. Replace them with values derived from
   the selected release and a fresh `status`, and say how the operator derives
   them. **Do not merely substitute `0035` into a permanent example.**
4. **Exact-object recovery only.** Use exact named objects and empty-directory
   verification; no wildcard or recursive parent deletion; do not claim stale
   locks can never recur.
5. **Document the C6-V F3 residue.** Automatic pre-write recovery restores the
   observed account/group/home and unit/scheduler state, but leaves the copied
   canonical state, the installed canonical unit files and the installed
   ancillary files in place, and a retry is refused until an explicit recovery.
   State this as designed residue so an operator does not expect a clean slate.
6. **Cross-check every documented artifact and exit branch against the current
   engine**, including: `REMOTE_DEPLOY_DIR` and its owner record; the reclaim
   reasons and quarantine naming; `mkdir` without `-p`; cleanup on success and
   on failure; the `migration-required` exit behavior; and the migration's own
   control-state and scratch locations
   (`/var/lib/kronika-identity-migration`, `/run/kronika-identity-migration`).
   Routine commands must never be documented as invoking identity migration.

### Part B — the C6-V F1 coverage addition (bounded)

Add production-adapter tests in
`tests/contract/test_kronika_identity_migration.py` for the three production
composites that `C6-V` found unexercised:

- `RemoteMigrationHost.create_checkpoint` — including its non-success refusal;
- `RemoteMigrationHost.verify_effective_units` — including its failure path;
- the production `quiesce` composite — including its ordering (admission stop,
  then timers, then their job services).

Use the existing stateful `RemoteBoundary`; each new test must fail when its
protection or ordering is removed, and you must report that mutation
demonstration. Do not add tests for the other C6-V F2 branches in this cut; they
are recorded as accepted non-blocking coverage residue.

## Verified starting state, measured by the Orchestrator on 2026-10-08

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                24d2b7d718eb303c79197f6e2f41c81ad479a79a
Remote origin:                https://github.com/cisarik/kronika
Public main:                  3194f48f6b343a460ed5988d92999f91ef999a79
                              (the candidate is local and unpublished, by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 24d2b7d:   4689 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     155 passed
Retention module:             15 passed
```

Known contract-test pin sites to derive and correct (locators, not an
inventory): `tests/contract/test_nuc_release_docs.py` around lines 149–154 pins
the stale schema example and the three-file lock inventory;
`tests/contract/test_nuc_operator_runbook.py` also reads the runbook. Derive the
complete pinned set yourself and report every site.

**NUC state is carried, not measured here.** This cut has no host authority.
Do not assume the historical four-file residue exists now; document the
procedure, not a current host fact.

## Authority

```text
Positive authority: edit `docs/UBUNTU_NUC_DEPLOYMENT.md`; edit
  `tests/contract/test_nuc_release_docs.py`; edit
  `tests/contract/test_nuc_operator_runbook.py` only for assertions that pin the
  corrected runbook text, naming each in the report; edit
  `tests/contract/test_kronika_identity_migration.py` for the bounded Part B
  tests; edit `tests/contract/test_kronika_identity_retention.py` only to re-pin
  a Part C scalar that your own measurement shows this cut moved, with the
  arithmetic cause stated; create exactly one local commit on `main`.

Negative authority: `deploy/ubuntu/kronika_release.py` is frozen for this cut;
if your cross-check reveals an engine defect, stop and report rather than
editing it. Every other path; any dependency or lockfile change; any change to
`pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen document or
Alembic revision; publication; push; force; amend; branch; stash; any NUC
contact or SSH; any invocation of `migrate-identity`, `deploy`, `rollback` or
`activate-capture` in any mode; any provider, browser or capture contact; any
secret, personal Fish configuration or browser-profile read. If a necessary
change falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 24d2b7d718eb303c79197f6e2f41c81ad479a79a
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 24d2b7d718eb303c79197f6e2f41c81ad479a79a --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run`, including as a text editor.
  Read-only Git inspection allowed; exactly one `git add <exact paths>` and one
  `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md, the accepted plan and the C6-V report are authoritative inside their
  scope. On conflict between retained context and current repository evidence,
  stop.
Side-effect authority: reversible local repository mutation only. No host,
  service, database, provider, browser or account side effect.
Browser authority: none.
```

## Verification

1. Derive the complete set of runbook-contract assertions from the test files
   before editing; report every pinned string the correction touches.
2. Cross-check every documented recovery artifact and exit branch against the
   current engine; for each branch, state whether a test exercises the engine
   behavior or only the text. Test the three-file, four-file, live-owner,
   unexpected-file and interrupted-cleanup cases where the engine implements
   them; report any branch that cannot be tested.
3. Part B: demonstrate each new test failing when its protection or ordering is
   removed, naming the mutation.
4. Run, through the declared route: the focused doc-contract modules, the focused
   migration module, then the declared full Python suite, then the retention
   module. Report every count and any difference from the `4689/8/3/0` baseline.
5. Report **every site no test exercises**, and every pinned string your
   derivation found that this prompt's sample did not name.
6. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement. Never tune a pin until the suite is green.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. Locators in this prompt are not
    an inventory.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Reject a guard that can pass vacuously when its input is absent.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit: current instruction, historical fact,
    excluded prose or negative assertion.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the cross-check reveals an engine defect (report it; do not edit the
  engine); if a documented recovery branch contradicts the engine and the
  contradiction is material; if a frozen hash, Part A or Part B moves; if a
  Part C re-pin cannot be reproduced from your own measurement; if a necessary
  change falls outside the positive scope; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded result.

Completion: Part A corrected and contract-tested against the current engine;
  Part B three production composites covered with mutation demonstrations;
  focused modules, full declared Python suite and retention module green through
  the declared route; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `29_report_00.md` in
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
echoing `kronika-sole-identity`, session `29` and exchange `01` unchanged. Then:

1. The derived pinned-string inventory, before and after.
2. Part A per outcome 1–6, with the engine cross-check result for every
   documented branch.
3. The three-file, four-file, live-owner, unexpected-file and interrupted-cleanup
   evidence, or the stated reason a case cannot be tested.
4. Part B tests with their mutation demonstrations.
5. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and any
   Part C movement with cause.
7. Every site no test exercises.
8. Deviations, risks, missing evidence, and one smallest next step.

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
  section 2.4 in full.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/28_report_00.md`
  sections 3, 6, 8 and 9 in full — the F1 coverage finding and the F3 residue.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` in full — the document under correction.
- `tests/contract/test_nuc_release_docs.py` and
  `tests/contract/test_nuc_operator_runbook.py` in full.
- `deploy/ubuntu/kronika_release.py` — the deploy lock lifecycle
  (`acquire_deploy_lock`, `release_deploy_lock`, owner record, reclaim and
  quarantine), the cleanup paths, the `migration-required` exit, and the
  migration control-state and scratch constants.
- `tests/contract/test_kronika_identity_migration.py` — the `RemoteBoundary` and
  the Part B test patterns.
- `docs/BACKUP_AND_RECOVERY.md` — the durable backup/recovery contract the
  runbook references.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: no stale schema or
three-file-inventory pin survives; every documented recovery branch matches the
current engine or is explicitly marked untestable; the Part B tests exercise the
production composites and fail on their mutations; the full suite is green at
the reported commit; and Part A and Part B are unmoved. Publication of
`8a5861c` + `24d2b7d` + this cut remains a separate later grant before any host
task relies on the runbook. The next cut after acceptance is `C-DATA-P`; the
`C6` host window additionally still waits on `C-DATA-H`.

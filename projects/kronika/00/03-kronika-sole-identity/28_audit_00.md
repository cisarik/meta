# Authoritative Worker prompt — Worker session 28, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `28`, exchange `01`. Stored under the
Meta filename mapping as `28_audit_00.md`, with report destination
`28_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 28
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6V — independently review the C6 production adapter before any host window
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the independent readiness review required by the
accepted closure plan before any `C6` host action. `C6-P1` and `C6-P2` were
implemented and accepted, but the plan's own premise is that the production
adapter's correctness must be established by someone other than its authors,
against the exact candidate, before a maintenance window opens on the live NUC.
Your value is falsification: find every required capability that lacks a real
implementation or a non-vacuous test, and every claim a green suite does not
actually establish.

**You are independent by construction and must stay independent.** You did not
participate in `C6-P1` or `C6-P2`; do not trust their reports as evidence. You do
not correct findings: correction requires a separate bounded grant. A read-only
audit that mutates the repository is a defect.

## Candidate identity

```text
Logical whole:      kronika-sole-identity
P1 commit:          8a5861c792122468468b3bc20934a26cb5eb1c93
P2 candidate:       24d2b7d718eb303c79197f6e2f41c81ad479a79a
Public main:        3194f48f6b343a460ed5988d92999f91ef999a79
                    (the two candidate commits are local and unpublished by design)
Specification:      25_report_00.md sections 2.1, 2.2 and 2.3
P1 evidence:        26_report_00.md
P2 evidence:        27_report_00.md
```

Review the exact candidate commit `24d2b7d718eb303c79197f6e2f41c81ad479a79a` as
it exists locally. Publication is a separate later grant; do not treat the
candidate as published, and do not push anything.

## Verified current state, measured by the Orchestrator on 2026-10-08

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                24d2b7d718eb303c79197f6e2f41c81ad479a79a
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 24d2b7d:   4689 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     155 passed
Focused recovery CLI module:  10 passed
Retention module:             15 passed
```

Re-derive these gates yourself at the start. If any fails, stop and report.

## Mandate

Reconcile **every capability the accepted plan requires for C6** against its
production implementation and a non-vacuous test. The required capability set is
the union of:

- `25_report_00.md` section 2.1 outcomes (exclusion, control-state placement,
  durable intent and writes boundary, pre/post-write recovery, copy verification,
  dead-builder removal, failure classification);
- section 2.2 outcomes (exact-state binding, owned scratch, canonical release
  environment, guard-then-switch before startup, effective unit/drop-in/timer
  observation and scheduling preservation, structural credential and sudo
  transformation, ancillary modes, workstation command selection, readiness,
  ingress and capture-identity verification, absent optional integrations);
- the section 2.2 proof list and the P2 report's effect matrix.

For each capability report: the exact production implementation (file:line or
symbol), the test that exercises it, whether that test is non-vacuous, and the
result. **Report every production command or substep that no test exercises.**

## Required review questions

1. **Identity and scope.** Confirm the candidate commit, its parentage, the six
   authorized paths in the two diffs, and that no path outside the C6-P1/P2
   mandate changed. Confirm no `C6-V`, `C-RUNBOOK`, `C-DATA`, `C-LOCAL`, `C-OPS`
   or `C7` work is present, and no second deployment system was introduced.
2. **Ordering.** Read the phase table and the apply orchestration. Confirm the
   exclusion is acquired before any control-state write; the pointer guard,
   atomic switch and readback precede service startup; readiness is checked after
   startup; ingress is verified after its replacement; writers resume only after
   verification; and a failed ingress edit cannot be reported as success.
3. **Non-vacuity, by mutation.** Attempt in-memory or synthetic reversions of a
   representative set of the guards the two reports claim, including at least:
   the control-location containment guard; the exclusion-before-journal order;
   the durable `writes_possible` boundary; the pointer guard before switch; the
   readiness call; the capture-identity comparison; the observed-timer
   preservation; the structural drop-in and sudo transformation refusals; the
   committed-lock and retained-release guards; and the workstation selection
   rejection of arbitrary input. For each, name the mutation, the test, and the
   observed failure or the absence of one. Do not modify the repository; use
   in-memory or isolated synthetic state and restore it.
4. **The stateful boundary itself.** Verify `RemoteBoundary` or its equivalent
   rejects unknown commands and models effects rather than returning
   unconditional success. Verify the executable release probe actually executes
   prepared console scripts rather than asserting transcript substrings.
5. **Frozen and preserved material.** Confirm Part A unchanged (86 document and
   36 Alembic keys, byte equality), Part B still 20, the committed `poetry.lock`
   preserved, and no routine deploy/rollback path can invoke identity migration
   or restart capture. Confirm no frozen residue changed.
6. **Re-run authorized focused checks** through the declared route:
   `tests/contract/test_kronika_identity_migration.py`,
   `tests/contract/test_recovery_cli.py`,
   `tests/contract/test_kronika_identity_retention.py`. Use a targeted probe
   only for a named missing claim; do not repeat a broad suite without a named
   reason.
7. **Disposition of every finding.** For each confirmed defect, state whether it
   blocks the C6 host window. **Any unresolved production-sequence defect blocks
   C6-H.** Distinguish a blocking defect from a non-blocking observation; do not
   manufacture findings, and do not repair any.

## Authority

```text
Positive authority: read any tracked file in /home/agile/Projects/kronika; read
  every file in the Meta trace directory named above; run read-only Git
  inspection and read-only public-ref verification; run the declared focused AP
  test operations against the candidate baseline; construct bounded in-memory or
  isolated synthetic probe state that mutates nothing durable.

Negative authority: ANY repository, trace or durable-state mutation; any
  correction or edit of any kind; any commit, branch, tag, merge, rebase, stash
  or history rewrite; any push; any NUC contact or SSH; any invocation of
  `migrate-identity`, `deploy`, `rollback` or `activate-capture` in any mode; any
  provider, browser or capture contact; any dependency install or lockfile
  change; any reading of private/**, personal Fish configuration, browser
  profiles, cookies, tokens, credential stores, .secrets or ~/.config/opencode;
  any writing of the report to a file.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 24d2b7d718eb303c79197f6e2f41c81ad479a79a
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 24d2b7d718eb303c79197f6e2f41c81ad479a79a --operation test-focus -- <args>
  Never invoke `.venv/bin/python`, `python`, `python3` or `poetry run`, including
  as a text editor.
  Read-only Git inspection allowed; no Git write. Any other command must be
  stated in the report with its purpose and a confirmation that it mutated
  nothing.

Dependency authority: none.
Git authority: none.
Network authority: read-only public Git ref verification only.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. Reports
  26 and 27 are claims, not evidence. On conflict between retained context and
  current repository evidence, stop.
Side-effect authority: none. Temporary probe state must be isolated, non-secret,
  outside project state, and restored or removed with its outcome reported.
Browser authority: none.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository or AP gate does
  not match; if the candidate cannot be fixed as an exact identity; if a
  required capability has no implementation at all; if you cannot complete the
  review without mutation or host contact; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded audit.

Completion: every required C6 capability reconciled with an implementation and a
  non-vacuous test or declared missing; every untested production command or
  substep reported; the mutation probes reported with results; focused checks
  re-run and reported; findings disposed as blocking or non-blocking; tree clean
  and HEAD unchanged.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `28_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No implementation, no correction, no commit, no push, no
  publication, no host contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-evidence`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `28` and exchange `01` unchanged. Then:

1. Identity, scope and gate verification, including the exact candidate commit.
2. Capability reconciliation table: capability, implementation, test,
   non-vacuous verdict, result.
3. Every production command or substep no test exercises.
4. Mutation-probe results, each with mutation, test and observed outcome.
5. Stateful-boundary and executable-probe verification.
6. Frozen-material and routine-path isolation evidence.
7. Focused check results.
8. Findings with blocking/non-blocking disposition.
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
  sections 2.1, 2.2, 2.3 and 1 in full — the capability set to reconcile.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/26_report_00.md`
  and `27_report_00.md` in full — claims under review, including their
  untested-site lists and deviations.
- `deploy/ubuntu/kronika_release.py` — the full migration implementation, the
  phase table and `run_migration_apply`, the routine deploy path, and every
  facility the migration reuses.
- `tests/contract/test_kronika_identity_migration.py` in full — the production
  boundary and its tests.
- `src/kronika/adapters/cli/recovery.py`,
  `src/kronika/infrastructure/persistence/catalog_backup_workstation.py`,
  `tests/contract/test_recovery_cli.py` — the workstation selection.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` — the host procedure the candidate will drive.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator note

This audit is the primary independent acceptance for the C6 production adapter.
Its result gates the host window: a `PASS` with no blocking finding permits the
Orchestrator to schedule `C-RUNBOOK` and the remaining preparation sequence; a
`PARTIAL` or `BLOCKED` with a blocking finding produces exactly one bounded
correction grant and one fresh re-audit, within the finite budget. Do not soften
a blocking finding, and do not expand into an unknown-unknown hunt beyond the
required capability set: out-of-scope observations are recorded as ledger
candidates, not findings.

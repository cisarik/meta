# Authoritative Worker prompt — Worker session 41, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `41`, exchange `01`. Stored under the
Meta filename mapping as `41_audit_00.md`, with report destination
`41_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 41
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6PS — independent re-audit of the account process-query correction
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The first live C6 apply stopped because the no-legacy-writers
query misread procps's empty-selection exit as a query failure. A bounded
correction now makes absence, presence and genuine query failure three
distinguishable outcomes. The fix changes fail-closed decision logic in the
migration adapter, so it needs fresh independent acceptance before the journal
is archived and the apply retried. Your job is to falsify the correction.

**You are independent by construction.** You did not participate in `C6-P1`,
`C6-P2`, `C6-V`, the guard correction, the encoding repair, the unknown-directive
policy or this process-query correction. Do not trust their reports as evidence.
You do not correct findings.

## Candidate identity

```text
Logical whole:        kronika-sole-identity
Policy correction:    980041cf13dd427e77263f573694aed7c1a54018
Process correction:   fcde631047650d1ff0a84b84bf185b54d6d11ba5
Correction report:    40_report_00.md
Live failure evidence: 00_notes.md tail (apply stopped; host recovered)
Public main:          980041cf13dd427e77263f573694aed7c1a54018
                      (the correction is local and unpublished by design)
Specification:        25_report_00.md sections 2.1, 2.2 and 2.10
```

Review the exact candidate commit `fcde631047650d1ff0a84b84bf185b54d6d11ba5` as
it exists locally, against its parent `980041c…`. Do not push anything.

## Verified current state, measured by the Orchestrator on 2026-10-11

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                fcde631047650d1ff0a84b84bf185b54d6d11ba5
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at fcde631:   4901 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     231 passed
Retention module:             15 passed
```

Re-derive these gates yourself at the start. If any fails, stop and report.

## What the correction claims

`cmd_remote_account_processes_absent(user)` now returns exactly:

- `0` when the account exists and no process matches its UID;
- the exact count when one or more processes match;
- `query-failed` for an unresolvable or malformed UID, a missing/broken `ps`, a
  malformed or empty process snapshot, or a counter failure.

The live host runs procps-ng 4.0.4, which exits 1 for an empty `ps -u` selection
— the state after `quiesce` stops every writer — and the old builder misread
that as a query failure.

## Required review questions

1. **Identity and scope.** Confirm the candidate commit, parent, the two changed
   paths and no other path; the engine outside the corrected function is
   byte-identical to the parent; the caller `assert_no_legacy_writers`, its
   messages and exit codes are unchanged.
2. **Three-outcome matrix, independently constructed.** Valid account with zero
   processes → `0`; one process → `1`; several processes, including column
   spacing and an unrelated UID that shares a numeric prefix or suffix (for
   example `1001` versus `11001`, `10010`, `0`) → exact count; unknown account →
   `query-failed`; broken/missing `ps` → `query-failed`; empty, malformed,
   multiline or non-numeric UID output → `query-failed`; malformed snapshot
   lines → `query-failed`; account-argument quoting.
3. **Caller contract.** `0` passes `assert_no_legacy_writers`; a positive count
   raises `a process still runs as the former web account`; `query-failed`
   raises `former web account process state is unverifiable`; both exit 27.
   Confirm `quiesce` order (observe, stop writers, assert, capture snapshot) and
   that a failure still routes through the pre-write recovery.
4. **Independent mutation probes.** Restore the old `if ! ps -u …` criterion
   (zero-process case must fail with the spurious refusal); remove the `ps`
   health distinction (a broken query must not become `0`); remove the UID guard
   (an unknown account must not become `0`). Report each mutation, test and
   observed outcome.
5. **Boundary fidelity.** Confirm the test boundary executes the actual shell
   body with synthetic `id`/`ps` functions and cannot pass vacuously when those
   functions are absent; report any branch the boundary cannot reach.
6. **Checks.** Re-run the focused migration module, the retention module and the
   declared full Python suite at the candidate. Report counts and any difference
   from `4901/8/3/0`. Confirm Part A (86 document and 36 Alembic keys) and Part B
   (20) unchanged.
7. **Disposition.** Report every untested site and residual risk. If a design
   assumption survives this correction and your recheck unchanged, report
   exactly: `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## Authority

```text
Positive authority: read any tracked file in /home/agile/Projects/kronika; read
  the Meta trace files named above; run read-only Git inspection including
  `git show` of parent blobs; run the declared focused and full AP test
  operations against the candidate baseline; construct bounded in-memory or
  isolated synthetic probe state that mutates nothing durable.

Negative authority: ANY repository or durable-state mutation; any correction or
  edit; any commit, branch, tag, merge, rebase, stash or history rewrite; any
  checkout or restore of another revision; any push; any NUC contact or SSH; any
  migration invocation; any provider, browser or capture contact; any secret or
  personal-configuration read; any writing of the report to a file; any direct
  invocation of `.venv/bin/python`, `python`, `python3` or `poetry run` outside
  the declared AP route — including as a text counter.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline fcde631047650d1ff0a84b84bf185b54d6d11ba5
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline fcde631047650d1ff0a84b84bf185b54d6d11ba5 --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Read-only Git inspection
  allowed; no Git write. Any other command must be stated in the report with
  its purpose and a confirmation that it mutated nothing.

Dependency authority: none.
Git authority: none.
Network authority: none.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. Reports
  33–40 are claims, not evidence. On conflict between retained context and
  current repository evidence, stop.
Side-effect authority: none. Temporary probe state must be isolated, non-secret,
  outside project state, and removed or reported.
Browser authority: none.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository or AP gate does
  not match; if the candidate cannot be fixed as an exact identity; if a
  required case cannot be exercised without mutation or host contact; if
  context pressure reaches the point where a bounded rotation is cheaper than a
  degraded audit.

Completion: identity, scope, matrix, caller contract, mutations, boundary
  fidelity, checks and dispositions all reported; tree clean and HEAD unchanged;
  report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `41_report_00.md` in
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
echoing `kronika-sole-identity`, session `41` and exchange `01` unchanged. Then:

1. Identity, scope and gate verification, including the exact candidate commit.
2. The three-outcome matrix results.
3. Caller-contract and quiesce/recovery results.
4. Mutation-probe results, each with mutation, test and observed outcome.
5. Boundary-fidelity findings.
6. Focused and full-suite check results, and Part A/Part B evidence.
7. Findings with blocking/non-blocking disposition and every untested site.
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

- `deploy/ubuntu/kronika_release.py` — `cmd_remote_account_processes_absent`,
  `assert_no_legacy_writers`, `quiesce`, `stop_writers`, `recover_pre_write`.
- `tests/contract/test_kronika_identity_migration.py` — the synthetic shell
  boundary, matrix, mutations and quiesce/recovery tests.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/40_report_00.md`
  in full — the claims under review.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator note

This re-audit gates the C6 window: a `PASS` with no blocking finding permits
publishing `fcde631`, archiving the failed journal under bounded authority, a
fresh preflight and the apply retry. The live host has already recovered; this
review concerns the corrected decision logic only. Judge it on the evidence in
front of you.

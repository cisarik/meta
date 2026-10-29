# Authoritative Worker prompt — Worker session 70, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `70`, exchange `01`. Stored under the
Meta filename mapping as `70_implementation_00.md`, with report destination
`70_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **the admin batch re-analysis correction** (`KSI-CORR-REANALYZE`), a
bounded UI behavior change requested by the Cooperator during rendered
acceptance. The server already supports superseding runs; only the web shell's
first-analysis eligibility blocks the flow.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 70
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-CORR-REANALYZE — allow the admin analysis batch to re-analyze terminal records
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The eligibility change must stay fail-closed for active
runs, the copy touches several UI surfaces, and the frontend tests pin the
current texts.

## Specification

1. **Eligibility.** In `src/kronika/adapters/api/web/app.js`,
   `adminAnalysisEligibility` currently accepts only
   `analysis_state === "not_requested"`. Change it so an item is eligible when
   its state is terminal — reuse the existing
   `AUTOMATIC_ANALYSIS_TERMINAL_STATES` set (`not_requested`, `analyzed`,
   `failed`) — and ineligible only while an analysis is active. Derive the
   exact active state values from the parse of the UI and the server status
   payloads; name them in the report. The enqueue path stays the same POST to
   the per-item durable-analysis endpoint: the server's
   `RequestManualMediaAnalysis` creates a superseding pending run for terminal
   runs and stays idempotent for active ones — verify that by parse and state
   it; no server change.
2. **Copy.** Move every first-analysis-only text to the re-analysis truth:
   the selection hints (including the "No selected item is eligible for first
   analysis…" sentence), the per-item skipped reason ("First analysis is only
   available before any analysis request; current state is …"), the
   confirmation title ("Queue first analysis for N eligible item(s)?") and its
   message, and any outcome label that names first analysis. The new
   ineligible reason must state that an analysis is already active. Keep the
   limits and semantics: at most ten queued, sequential order, stop after the
   current item, provider-halt handling, provider/vision prechecks, audit
   semantics, one durable run per accepted item.
3. **Tests.** Update `tests/admin_batch_actions_frontend.test.js` (it pins the
   confirmation title and the eligibility behavior) and every further
   frontend module your parse shows pinning the batch eligibility or texts —
   name each before editing. Add cases: an `analyzed` item is eligible and
   enqueued; a `failed` item is eligible; an active-state item is ineligible
   with the new message; a `not_requested` item stays eligible as before.
4. **Documents.** No ADR edit: ADR-0049's frozen "Deferred Work" list is
   historical (multi-select, bulk first analysis and batch progress shipped
   later). If the parse finds a living document that states the
   first-analysis-only rule, update or classify it and say so; otherwise
   state that none exists.
5. **No server, extension or Python change.**

## Verified starting state, measured by the Orchestrator on 2026-10-29

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                7d6463f54d0552eb54e0d6fe39d49171c8ce31e0
Public main:                  7d6463f54d0552eb54e0d6fe39d49171c8ce31e0 (published; NUC serves it)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4759 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212 (the glob moves by exactly your added cases — declare the count)
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no external
calls.

## Authority

```text
Positive authority: edit `src/kronika/adapters/api/web/app.js` for exactly the
  eligibility change and the first-analysis copy; edit the frontend test
  module(s) that pin the batch, naming each before editing; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measured retention failure shows this commit moved,
  with the arithmetic cause stated; create exactly one local non-amended
  commit on `main`.

Negative authority: every other path; the server, the extension, Python
  sources, the ADR documents and any other frozen file; the batch limits and
  semantics beyond the eligibility and copy; any dependency or lockfile
  change; the `.ap` gitlink; any Alembic revision; any `.venv` operation;
  publication; push; force; amend; branch; stash; any host or browser action.
  If a necessary change falls outside the positive scope, stop and report; do
  not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 7d6463f54d0552eb54e0d6fe39d49171c8ce31e0 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Read-only Git inspection allowed;
  exactly one `git add <exact paths>` and one `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only.
Browser authority: none.
```

## Verification

1. **Eligibility matrix.** `not_requested` eligible (unchanged); `analyzed`
   eligible; `failed` eligible; active state ineligible with the new message;
   unselected items untouched; the enqueue still posts the per-item request
   with the canonical mutation header.
2. **Copy matrix.** No remaining first-analysis-only text in the batch
   surfaces; the confirmation, hints, skipped reason and outcome labels read
   true for re-analysis; limits and stop/provider-halt semantics unchanged.
3. **Tests.** The updated and added frontend cases pass; the other five named
   JS suites keep their counts; the bounded glob reports exactly the declared
   new count.
4. **Python unchanged** at `4759/8/3/0`; retention unchanged (measure; no
   re-pin expected).
5. **Mutation demonstration.** Restore `not_requested`-only eligibility → the
   new `analyzed`-eligible test fails, with the observed failure named.
6. Run, through the declared routes: the touched frontend modules, the six
   named JS suites, the bounded glob, the full declared Python suite and the
   retention module.
7. Report every moved or removed site that no test exercises.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING the artefact. This prompt's anchors are
    locators, not an inventory.
 2. Resolve every cited symbol and every state value to its literal
    definition BEFORE editing.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Never relax the active-run fail-closed rule.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Do not collapse the terminal eligibility with the active
refusal; do not collapse the UI copy change with the server semantics; do not
collapse the batch with the per-item review flow.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a server change would be needed; if an active-run refusal cannot
  be preserved; if a frozen hash or Part A moves; if a Part C re-pin cannot be
  reproduced from your own measurement; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded result.

Completion: terminal-based eligibility with the active refusal, the complete
  copy update, the updated and added frontend tests, the declared JS count
  movement, the mutation proof, and one local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `70_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `70` and exchange `01` unchanged.
Then:

1. The eligibility matrix with the exact state values.
2. The copy matrix (every changed string, old and new).
3. The tests updated and added, each named.
4. The JS count movement statement (glob baseline 212 plus the added cases) and
   the unchanged named-suite counts.
5. The mutation demonstration with the observed failure.
6. Suites: frontend modules, named JS suites, glob, full Python, retention —
   counts, elapsed time, baseline differences.
7. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
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

- `src/kronika/adapters/api/web/app.js` — `adminAnalysisEligibility`, the
  batch driver, the confirmation, the outcome labels, the state presentation,
  and the durable-analysis enqueue.
- `src/kronika/application/media_analysis_lifecycle.py` — the
  `RequestManualMediaAnalysis` contract (read-only).
- `src/kronika/adapters/api/media_analysis_lifecycle_api.py` — the
  durable-analysis endpoint (read-only).
- `tests/admin_batch_actions_frontend.test.js` and every frontend module the
  parse shows pinning the batch.
- `docs/adr/0049-durable-content-publication-boundary.md` (frozen; read-only).
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices, the tests, the declared
JS count and the mutation at the reported commit, then arranges publication,
a routine NUC refresh, and the Cooperator's bulk re-analysis retest, after
which the rendered receipt completes and C-INSTALL-DOC and CLOSE follow.

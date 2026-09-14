Logical whole identity: code-health-and-refactoring
Worker session ordinal: 01
Worker exchange ordinal: 03
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Planner
Phase: planning
Task identity: CONTEXTDECK-CODE-HEALTH-REFACTORING-PLAN-REVISION
Native planning mode: required
Delivery route: manual COOPERATOR delivery to the same healthy Worker session
Reasoning recommendation: Medium
Reasoning basis: one narrowly bounded repository-grounded correction — re-ground
the S4 extraction target on the exact candidate symbols — with every other plan
decision preserved by reference; no design reopening, no new scope.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: the eventual whole is cross-cutting reversible source
refactoring with the full registered CTest suite as its behavior-preservation
gate; this revision exchange itself is read-only planning with no implementation.
Internal delegation: prohibited

# ContextDeck — one targeted revision: re-ground the S4 extraction target

You are the WORKER session that produced the frozen plan for logical whole
`code-health-and-refactoring` (exchange `01`) and rendered its terminal report
(exchange `02`). Read this complete prompt before acting. Your prior authority
expired at that terminal report; this prompt is a complete renewed grant for
exactly one targeted revision, and nothing else.

## Targeted-revision record

Planning cycle: targeted-revision
Prior planning report: 01_report_01.md
Targeted revision basis: specifically-rejected-assumption
Changed decision boundary: the S4 ContextReceiver extraction target — the
rendered plan names a function `parseInventoryPayload` that does not exist in
`src/context/ContextReceiver.cpp` at the candidate
Preserved unaffected decisions: every other decision rendered in
`01_report_01.md` — the one-whole scope decision, the selected and parked
slices, all other per-slice allowlists and tests, the implementation
exchange/commit/candidate sequence, the acceptance design and control matrix,
the risk register, and the documentation replacements A–F
Automatic targeted revisions used: 1

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: re-ground only the S4 ContextReceiver extraction target
on the exact candidate and return a corrected S4 section with all other
decisions preserved by reference
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: a separate complete ORCHESTRATOR implementation
prompt whose native planning-mode value is `not-used`
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

ORCHESTRATOR reconciliation rejected exactly one assumption and preserved
everything else. Do not reopen, improve, extend, or restructure any other plan
decision. There is no second automatic revision.

## Why this revision

The rendered plan is otherwise decision-complete. During reconciliation, this
assumption was specifically rejected: `src/context/ContextReceiver.cpp` at
candidate `235d467c752958694dad4be7bcc31e66406dbdcc` contains no function named
`parseInventoryPayload`. The actual member is
`ContextReceiver::onInventoryReport(const QString &bridgeId, quint32 sequence,
const QString &payloadJson)`, approximately lines 551–623. The revision must
re-ground that one boundary on the actual code.

## Required corrected content

Return a corrected S4 ContextReceiver subsection that states:

1. The exact extraction boundary for `src/context/InventoryPayload.{h,cpp}`:
   which exact lines/portion of `ContextReceiver::onInventoryReport` are the
   pure payload parse (JSON decoding, structural validation, entry extraction,
   bounds, deduplication), and which parts (sequence acceptance, heartbeat
   timestamp, inventory comparison, policy bump, `inventoryChanged` emission)
   stay in `ContextReceiver`.
2. The exact free-function name and signature that preserves semantics: the
   same accepted and rejected inputs, the same rejection and info log messages
   and levels (`qCWarning(lcContext)` / `qCInfo(lcContext)` messages such as
   `rejected inventory: ...` and `inventory updated, entries ...`), the same
   bounds and dedup behavior, and the same resulting entries.
3. The preserved plan decision: extract only this parse; no shared abstraction
   with Persistence; receiver lifecycle untouched; empty payload handling
   unchanged.
4. A re-verification result for the rest of S4's anchors (`decodeSnapshot`
   577–773 and the named decode helpers including `hasControlCharacters` and
   `boundedUtf8` in the same translation unit). If any anchor is inaccurate,
   report it explicitly as a limitation; do not silently change it.
5. An explicit statement that every other decision rendered in
   `01_report_01.md` is preserved unchanged by reference.

Everything else remains frozen. The S4 allowlist stays as rendered:
`src/context/WorkspaceReceiver.{h,cpp}`, `src/context/WorkspaceStateCodec.{h,cpp}`,
`src/context/InventoryPayload.{h,cpp}`, `src/context/ContextReceiver.cpp`,
`CMakeLists.txt` (`contextdeck_context` sources), and
`tests/unit/test_workspace_receiver.cpp` (new codec slots; no new `add_test`
name).

## Gates before acting

Read the prior terminal report
`projects/contextdesk/00/06-code-health-and-refactoring/01_report_01.md`
completely first. Then verify read-only and stop on any material failure:

1. Product identity: `https://github.com/cisarik/contextdesk`, `main`,
   HEAD = `235d467c752958694dad4be7bcc31e66406dbdcc`, parent
   `293158887e4228a42b9c64bda7d4f0bd32fb4ec9`; AP gitlink and checkout
   `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; clean worktree.
2. The prepared prompt file
   `projects/contextdesk/00/06-code-health-and-refactoring/01_planning_02.md`
   exists and is byte-identical to the prompt you received; read it back
   completely. Stop on a non-identical or unsafe collision.
3. The report destination
   `projects/contextdesk/00/06-code-health-and-refactoring/01_report_02.md`
   does not already exist. Do not modify `00_notes.md`, `00_handout.md`,
   `01_planning_00.md`, `01_completion_01.md`, `01_report_00.md`, or
   `01_report_01.md`.
4. Inspect `src/context/ContextReceiver.{h,cpp}` at the exact candidate. Tie
   every statement to the candidate.

Do not configure, build, or execute tests. No product Git mutation. No META Git
mutation (no stage, commit, push, pull, merge, rebase, or ref change). The
COOPERATOR owns META Git and archives the prompt/report pairs after the reports
exist.

## Authority and side-effect boundary

Product source mutation: prohibited
Product Git mutation: prohibited
AP mutation/update: prohibited
Host mutation: prohibited
Desktop/service/device/broker operation: prohibited
Dependency operation: prohibited
Secrets/credentials/private data: prohibited
Network authority: reads from the two canonical HTTPS remotes only
(`https://github.com/cisarik/contextdesk.git`,
`https://github.com/cisarik/meta.git`): `git ls-remote` and read-only clones or
content reads. No external research, no provider calls.
Side effects: read-only inspection plus the exact report-file write below only

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names/IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the three coordinate fields of this prompt exactly once, with
their values unchanged (`code-health-and-refactoring`, session `01`, exchange
`03`), and echo the persistent role identity.

Include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `not-applicable`;
- start and end product commit (expected unchanged
  `235d467c752958694dad4be7bcc31e66406dbdcc`);
- changed files and purpose: the META report file only;
- validation: the read-only checks above, the prior-report readback, and the
  report readback; state explicitly that no tests were executed;
- the corrected S4 ContextReceiver subsection with items 1–5 above;
- the explicit preserved-decisions statement;
- deviations, risks, unresolved decisions, and missing evidence;
- exactly one smallest next step: ORCHESTRATOR reconciliation of this revision;
- exactly one `Report justification: new-evidence`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none`;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the authority-expiry sentence below.

Explicit non-claims: no implementation-PASS, acceptance-PASS, publication-PASS,
deployment-PASS, production readiness, M2/G4/G3 closure, autostart,
hibernate/hybrid sleep, input-remapper coexistence, M3/M4 closure or physical
behavior, M5, remapping, deck layer, per-key RGB, license selection, or
hardware acceptance; no claim that the revised plan is accepted before
ORCHESTRATOR reconciliation; no claim that refactoring preserves behavior.

## Trace persistence contract

External trace disposition: configured
Trace discovery: META README and the exact destination below
Trace project key: contextdesk
Trace logical-whole projection identity: 06-code-health-and-refactoring
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_02.md
Destination path: projects/contextdesk/00/06-code-health-and-refactoring/
Report filename: 01_report_02.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

After planning, write the complete terminal report first to the exact report
path, read it back completely, and verify the header, coordinates, content, and
filename. Do not overwrite a non-identical existing report. If the exact META
destination is not reachable from your environment, do not write to any other
path; state the exact limitation in the report body and return the complete
report through the client output so the COOPERATOR can persist it exactly.

## Stop conditions

Stop and report `BLOCKED` if: the session is not the healthy continuation
session, Native Plan Mode is not actually enabled, coordinates or authority are
contradictory, product/AP identity fails, the prompt file collides or differs,
the report path exists, or the revision would require repository or host
mutation, private data, or subagents.

Stop with `PARTIAL` if the corrected S4 boundary cannot be determined from the
exact candidate or another S4 anchor is proven inaccurate beyond the rejected
assumption. Do not implement and do not widen the revision.

Stop with `PASS` only when the corrected S4 subsection and the preserved-
decisions statement are persisted and read back. Then submit the terminal report
and do no further work under this grant.

Authority for this Worker expires at this terminal report.

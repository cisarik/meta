Logical whole identity: ui-ux-refinement
Worker session ordinal: 01
Worker exchange ordinal: 05
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-UI-UX-REFINEMENT-S5
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal report `01_report_03.md` for Worker exchange `04`
(S3 and S4 implementation-PASS; S5 stopped uncommitted on a plan/grant string
conflict) and the accepted plan report `01_report_01.md` for Worker exchange
`02` — all produced in this same session
Authority renewal: prior implementation authority expired at the exchange-04
terminal report; this prompt is a complete renewed implementation grant to the
same session for S5 only
Reasoning recommendation: Medium
Reasoning basis: bounded execution of one accepted presentation slice in a
single file with exact authorized strings, the full registered suite and the
binding-set invariant as gates; no open design question and no live host
mutation.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting but reversible user-visible presentation
work in one QML file with no production, durable-data, security-boundary,
broker, packaging, dependency, or license mutation; one normal non-force
product push; the cumulative fresh independent acceptance for the whole is a
later separate exchange.
Internal delegation: prohibited

# ContextDeck — complete S5 (Aplikácie surface)

You are the WORKER session that produced the accepted plan. Native Plan Mode
must be OFF for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation slice: complete
S5 (Aplikácie surface) exactly as the accepted plan defines it, with the
ORCHESTRATOR-authorized empty-state strings below. Validate, create and push one
normal product commit, persist the terminal report in META, then stop. You do
not accept your own candidate and never close the logical whole.

Continuity and renewal: prior implementation authority expired at the
exchange-04 terminal report. Retained context, the plan text, and this
conversation are convenience and evidence, not authority; re-verify repository
and environment state before acting and stop on any conflict with current
repository evidence. Evidence produced in this session is non-independent.

Critical: no live host mutation, no application launch, no KWin/OpenRGB/broker/
device operation, no desktop mutation, no service change, no packaging change,
no dependency change, and no suspend/DPMS behavior may occur during this
exchange. This exchange edits, tests, commits, and pushes repository content
only; `build/` is git-ignored.

## Accepted plan and correction record

ORCHESTRATOR reconciliation: accepted
Accepted plan:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_01.md`
Reconciled predecessor exchange: S3+S4 implementation-PASS on
`02147d91dff650e11b4c92463d249d0eb3e5b5b3`; S5 stopped uncommitted.

Concrete finding and bounded correction: the accepted S5 scope includes
empty-state notices that require user-visible copy, while the plan's string
rule and the exchange-04 grant authorized only the confirmation string. The
COOPERATOR has now authorized the two empty-state strings. The authorized new
literals for S5 are exactly these four, and no others:

- `"Inventár je prázdny."` — inventory empty-state notice
- `"Zatiaľ nemáte žiadne profily."` — profiles empty-state notice
- `"Odstrániť profil?"` — profile-removal confirmation dialog title
- `"Profil a jeho uložené svetlo sa odstránia po uložení. Pokračovať?"` —
  profile-removal confirmation dialog body

The planning budget remains exhausted. This prompt is the separate complete
implementation grant; the accepted plan supplies no execution authority by
itself.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `02147d91dff650e11b4c92463d249d0eb3e5b5b3`
Changed-path allowlist: `ui/ApplicationsPage.qml`
Implementation boundaries: complete the accepted S5 scope in this one file —
heading/intro/status consistency, the two empty-state notices, the
profile-removal confirmation dialog, and label association for assignment rows
— keeping every `app.*` call and every `modelData` field unchanged; the only
new or changed user-visible strings are the four authorized literals above
Independence required: no for this implementation slice; the cumulative fresh
independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `02147d91dff650e11b4c92463d249d0eb3e5b5b3`
Required parent of the commit: `02147d91dff650e11b4c92463d249d0eb3e5b5b3`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/07-ui-ux-refinement/`
Accepted plan report:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_01.md`
Report destination:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_04.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent one-file slice and
one commit; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `01/05`, the renewed authority, and no subagents.
2. Verify canonical remote, active `main`, exact HEAD, clean state, no Git
   lock, matching AP gitlink/checkout, and `./.ap/ap doctor` PASS (variant
   `stable`).
3. Prove public product `main` equals the exact baseline with direct
   `git ls-remote`. Do not pull, merge, rebase, switch, reset, clean, stash, or
   retarget.
4. Verify META public `main` is `f1236b9...` or a verified later descendant
   whose changed paths do not contradict this exchange.
5. Verify the trace directory is real and contains `00_handout.md`,
   `00_notes.md`, `01_planning_00.md`, `01_completion_01.md`,
   `01_report_01.md`, `01_implementation_02.md`, `01_report_02.md`,
   `01_implementation_03.md`, and `01_report_03.md`; the report destination
   `01_report_04.md` must be absent before the write. The retired
   `01_report_00.md` no longer exists in this trace.
6. Read the accepted plan report `01_report_01.md` completely, especially
   section 3 (the Aplikácie surface and the confirmed string) and section 7
   (acceptance control matrix); read the exchange-04 report `01_report_03.md`
   section 5 (the exact S5 obstacle) completely.
7. Read `ui/ApplicationsPage.qml` completely before editing; capture the
   baseline `app.*` binding set and the file's string-literal set first.

## S5 scope (accepted plan section 3, exact)

Changed-path allowlist: `ui/ApplicationsPage.qml`.

- Heading/intro/status: the exchange-04 inspection found the heading and intro
  already conform to VL-2/VL-3; verify and change only what does not conform.
  Make the save-status line consistent with VL-5 (visible only when non-empty,
  `opacity: 0.8`), matching the ColorsPage pattern.
- Empty-state notices (VL-6, `Kirigami.InlineMessage`, `Information`,
  `Layout.fillWidth`):
  - when `app.inventory` is empty: `"Inventár je prázdny."`, placed with the
    inventory controls;
  - when `app.profiles` is empty: `"Zatiaľ nemáte žiadne profily."`, placed
    with the profiles list.
- Profile-removal confirmation via a new `Controls.Dialog`:
  - title: `"Odstrániť profil?"`
  - body: `"Profil a jeho uložené svetlo sa odstránia po uložení. Pokračovať?"`
  - buttons: Ok/Cancel
  - `app.removeProfile(...)` is called only from `onAccepted`, for the profile
    the user chose to remove (keep the existing `modelData` identity).
- Label association for assignment rows (A-4). The exchange-04 mechanism
  deviation used `Accessible.description` and reused label literals instead of
  a `Kirigami.FormLayout` restructuring to avoid a layout regression; the same
  mechanism is acceptable here with the deviation recorded, or use
  `Kirigami.FormLayout` where it is safe.
- Keep every `app.*` call and every `modelData` field unchanged; the four
  authorized literals above are the only new or changed strings.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md`, especially section 3 (Aplikácie)
  and section 7;
- the exchange-04 report `01_report_03.md`, especially section 5;
- `AGENTS.md` including the managed AP block;
- `ui/ApplicationsPage.qml` in full and `ui/ColorsPage.qml` for the
  status-line pattern;
- `src/app/AppController.h` for the `app.*` member surface.

## Product invariants

- G213 only; five RGB zones, never per-key RGB.
- Session app never opens raw keyboard nodes; broker stays static/inactive and
  no ARM/LEASE/grab/device probe occurs.
- All 83 `app.*` binding names remain unchanged; no behavior, property, or
  signal changes; the only new strings are the four authorized literals.
- The five-zone, event-driven-KWin, typed-action, no-autostart, and
  one-OpenRGB-connection invariants stay untouched.
- Repository documentation stays English and unchanged in this exchange; no
  license or G6 statement change.

## Commands and side-effect authority

Allowed: `git status`, `git log`, `git diff`, `git ls-remote`, `git rev-parse`,
`git show`; `cmake -S . -B build -G Ninja`; `cmake --build build`;
`ctest --test-dir build --output-on-failure`; `ctest -N`; `rg`/`grep` source
searches; exact-path `git add`, one `git commit`, one normal non-force
`git push`, and bounded public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any non-allowlisted path; any dependency, packaging, service, host, desktop,
device, broker, OpenRGB, KWin, or input-remapper operation; any application
launch.

Side effects: reversible local edits inside the allowlist, build outputs under
the git-ignored `build/`, one local product commit, and one normal non-force
product push. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names or IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — read the file before editing; capture the
baseline `app.*` binding set and the file's string-literal set first
Existing focused tests: none exist for QML presentation; the 21 registered
CTest names are the suite evidence
Affected tests: all 21 (full suite after the commit)
New causal regression: none — the slice changes presentation only; no
semantic validator, structural field, wire/IPC format, persistence, or the
`app` facade changes
Broad or full suite: required-because binding and behavior preservation across
presentation changes is the named decision risk
Runtime or testbed: not-used in this exchange; the one bounded
COOPERATOR-executed runtime QML validation is planned after the final
cumulative candidate
Independent acceptance: not-required for this slice; the whole receives one
cumulative fresh independent acceptance after the later slices

Procedure:

1. Capture baseline evidence before edits: the sorted unique `app.*` name set
   from `ui/*.qml`; the `ui/ApplicationsPage.qml` string-literal set; and a
   clean `git status`.
2. Apply the S5 edits inside the allowlist.
3. Build; run `ctest -N`; run the full suite and require 21/21.
4. Verify the `app.*` set is identical (83) and the file's string-literal diff
   is exactly the four authorized literals.
5. Inspect the diff: only `ui/ApplicationsPage.qml` may appear.

A failed gate stops the exchange before commit. Classify a failure before any
repair; do not rerun an unchanged broad gate; do not weaken the environment.

## Git and public verification

After a green suite:

1. Stage exactly `ui/ApplicationsPage.qml`; inspect the staged diff.
2. Create exactly one normal commit with subject:
   `ui: refine Aplikácie application profiles surface`
3. Before push, prove public `main` still equals the exact baseline with direct
   `git ls-remote`; on any mismatch, stop without pushing.
4. Push once, normal non-force, to `origin main`.
5. Verify local `HEAD`, remote-tracking state, and direct public `ls-remote` all
   equal the new commit; parent equals the exact baseline; changed paths are
   exactly the allowlist.

If commit or push is unavailable or fails, report `PARTIAL` with the exact
state; never force or bypass.

## Trace persistence contract

External trace disposition: configured
Trace discovery: META README and the exact destination below
Trace project key: contextdesk
Trace logical-whole projection identity: 07-ui-ux-refinement
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_04.md
Destination path: projects/contextdesk/00/07-ui-ux-refinement/
Report filename: 01_report_04.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the one product commit
Archival: wait-for-report

Before substantive work, verify the prepared prompt file exists and is
byte-identical to the received prompt; read it back completely. Stop on a
non-identical or unsafe collision.

After implementation, write the complete terminal report first to the exact
report path, read it back completely, and verify the header, coordinates,
content, and filename. Do not overwrite a non-identical existing report. Do not
stage, commit, push, pull, merge, rebase, or otherwise mutate META Git history
or refs. The COOPERATOR archives the prompt/report pairs after the reports
exist. If the exact META destination is not reachable from your environment, do
not write to any other path; state the exact limitation in the report body and
return the complete report through the client output so the COOPERATOR can
persist it exactly.

## Terminal report contract

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

It must echo the four opening identity fields (persistent role and the three
coordinates) exactly once, with their values unchanged.

Include:

- status: `PASS`, `PARTIAL`, or `BLOCKED`;
- phase-qualified result: `implementation-PASS` or `not-applicable`;
- start and end product commit (baseline and the new commit);
- changed files and purpose;
- tests and validation, including the full-suite result, the
  baseline-vs-candidate `app.*` binding-set comparison, and the string-drift
  result against the four authorized literals;
- commit and push result plus direct public-ref verification;
- the empty-state notices, the confirmation dialog, and the label-association
  evidence with exact QML locations;
- deviations, risks, or missing evidence;
- exactly one smallest next step: ORCHESTRATOR reconciliation and, if accepted,
  the next bounded implementation exchange;
- exactly one `Report justification: new-mutation`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the authority-expiry sentence below.

Explicit non-claims: no acceptance-PASS, publication-PASS beyond the one pushed
commit, deployment-PASS, production readiness, M2/G4/G3 closure, autostart,
hibernate/hybrid sleep, input-remapper coexistence, M3/M4 closure or physical
behavior, M5, remapping, deck layer, per-key RGB, license selection, or
hardware acceptance; no claim that any UI/UX or QML runtime behavior was
exercised; no claim that the application was launched; no claim that the
cumulative behavior-preservation acceptance has happened; no claim that the
later slices are complete.

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not the healthy
continuation session, Native Plan Mode is on, coordinates or authority are
contradictory, product/AP/META identity fails, the worktree has unexplained
changes, the trace path collides or is unsafe, the accepted plan is unreadable,
or the task would need a non-allowlisted path, a dependency change, private
data, host/device access, an application launch, or subagents.

Stop with `PARTIAL` without committing when the slice cannot be completed
inside its exact scope without changing a binding, a property name, a signal, a
behavior, or an unauthorized string, and name the exact obstacle. Do not widen
the allowlist.

Stop with `PASS` only when the slice is validated, the normal non-force push is
publicly verified, and the terminal report is persisted and read back. Then
submit the terminal report and do no further work under this grant.

Authority for this Worker expires at this terminal report.

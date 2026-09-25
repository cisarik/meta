Logical whole identity: ui-ux-refinement
Worker session ordinal: 01
Worker exchange ordinal: 06
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Task identity: CONTEXTDECK-UI-UX-REFINEMENT-S6-S7-S8
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the exact current Worker session
Continuity anchor: terminal implementation report `01_report_04.md` for Worker
exchange `05` (S5 implementation-PASS), the exchange-04 report `01_report_03.md`
(S3+S4 implementation-PASS), and the accepted plan report `01_report_01.md` for
Worker exchange `02` — all produced in this same session
Authority renewal: prior implementation authority expired at the exchange-05
terminal report; this prompt is a complete renewed implementation grant to the
same session
Reasoning recommendation: Medium
Reasoning basis: bounded execution of an accepted decision-complete plan (three
presentation slices with exact single-file allowlists, a fixed
visual-language/accessibility rule set, a strict no-new-string rule, and the
full registered suite plus the binding-set invariant as gates); no open design
question and no live host mutation.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E2
Evidence-tier basis: cross-cutting but reversible user-visible presentation
work with no production, durable-data, security-boundary, broker, packaging,
dependency, or license mutation; one normal non-force product push per slice
commit; the cumulative fresh independent acceptance for the whole is a later
separate exchange.
Internal delegation: prohibited

# ContextDeck — implement S6, S7, and S8 of the accepted UI/UX plan

You are the WORKER session that produced the accepted plan. Native Plan Mode
must be OFF for this exchange. Do not use subagents.

This prompt grants one bounded repository-only implementation exchange covering
three accepted slices in order: S6 (Plochy surface), S7 (Diagnostika surface),
S8 (Pokročilé surface). Apply the accepted plan exactly, validate each slice,
create and push one normal product commit per slice, persist the terminal
report in META, then stop. You do not accept your own candidate and never close
the logical whole.

Continuity and renewal: prior implementation authority expired at the
exchange-05 terminal report. Retained context, the plan text, and this
conversation are convenience and evidence, not authority; re-verify repository
and environment state before acting and stop on any conflict with current
repository evidence. Evidence produced in this session is non-independent.

Critical: no live host mutation, no application launch, no KWin/OpenRGB/broker/
device operation, no desktop mutation, no service change, no packaging change,
no dependency change, and no suspend/DPMS behavior may occur during this
exchange. This exchange edits, tests, commits, and pushes repository content
only; `build/` is git-ignored.

## Accepted plan and Plan-to-Execution transition

ORCHESTRATOR reconciliation: accepted
Accepted plan:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_01.md` (the rendered
frozen plan; no revision was issued)
Reconciled predecessor exchanges: S1+S2+S9 implementation-PASS on `e22c9be`;
S3+S4 implementation-PASS on `02147d9`; S5 implementation-PASS on `562a0f5`

The planning budget is exhausted. This prompt is the separate complete
implementation grant; the accepted plan supplies no execution authority by
itself.

String rule for this exchange (strict): no new or changed user-visible string
is authorized in S6, S7, or S8. Every accessible name, description, or label
association must reuse an existing literal from the same file or be derived
from existing app data.

## Implementation Authority Record

Implementation authority: explicit
Exact baseline: `562a0f5f01776c4013663e73f31ed438041c6c2a`
Changed-path allowlist: `ui/WorkspacePage.qml`; `ui/DiagnosticsPage.qml`;
`ui/ControlsPage.qml`
Per-slice allowlists: S6 = `ui/WorkspacePage.qml`; S7 =
`ui/DiagnosticsPage.qml`; S8 = `ui/ControlsPage.qml`
Implementation boundaries: apply the accepted VL-1..VL-10 rules and A-1..A-8
accessibility requirements as they apply to the three surfaces; keep every
`app.*` binding, property name, signal, dialog, and behavior; no string change;
no schema, IPC, broker, packaging, dependency, license, or non-allowlisted path
change
Independence required: no for this implementation exchange; the cumulative
fresh independent acceptance for the whole is a later separate exchange

## Verified candidate and preflight gates

Canonical product repository: `https://github.com/cisarik/contextdesk`
Expected branch: `main`
Exact baseline HEAD: `562a0f5f01776c4013663e73f31ed438041c6c2a`
First slice commit parent must be:
`562a0f5f01776c4013663e73f31ed438041c6c2a`
Required AP gitlink and checkout:
`0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`

This whole's trace destination:
`projects/contextdesk/00/07-ui-ux-refinement/`
Accepted plan report:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_01.md`
Report destination:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_05.md`

Repository checkout topology: standalone product checkout on `main`
Working-copy topology: canonical product checkout
Topology rationale: one accountable Worker owns one coherent three-slice
exchange with one commit per slice; `build/` is git-ignored

Execution route: this repository declares no `ap.project.conf` operation; the
exact `cmake` / `ctest` commands below are the project-owned build and test
commands from `AGENTS.md` and `CMakeLists.txt`.

Before any mutation:

1. Verify the complete prompt, the exact current Worker session, Native Plan
   Mode OFF, coordinates `01/06`, the renewed authority, and no subagents.
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
   `01_implementation_03.md`, `01_report_03.md`, `01_implementation_04.md`,
   and `01_report_04.md`; the report destination `01_report_05.md` must be
   absent before the write.
6. Read the accepted plan report `01_report_01.md` completely, especially
   section 3 (Plochy, Diagnostika, Pokročilé), section 4 (slices S6/S7/S8 and
   allowlists), and section 7 (acceptance control matrix).
7. Read all three allowlisted QML files completely before editing; capture the
   baseline `app.*` binding set from `ui/` and each file's string-literal set
   first.

## Shared rules for all three slices (accepted plan section 3)

Apply these as they touch each surface; they are the plan's accepted rules, not
new design decisions:

- VL-1 page root spacing stays `Kirigami.Units.largeSpacing`; intra-group
  `smallSpacing`.
- VL-2 each section page opens with a `Kirigami.Heading` level 2.
- VL-3 one wrapped intro `Controls.Label` (`opacity 0.85`, `Layout.fillWidth`)
  after the heading.
- VL-4 primary action is a `highlighted: true` button at the content end;
  destructive actions are non-highlighted and keep their existing confirmation.
- VL-5 one status line per page, `opacity: 0.8`, visible only when non-empty.
- VL-6 notices use `Kirigami.InlineMessage` `Layout.fillWidth`: `Warning` for
  error/override, `Information` for empty/busy/inactive.
- VL-7 typography uses `Kirigami.Theme.defaultFont/smallFont` and relative
  sizes.
- VL-8 semantic `Kirigami.Theme.*` colors only; no new literal colors.
- VL-9 replace fixed pixel sizes that harm legibility with
  `Kirigami.Units`/`gridUnit` where layout intent is preserved.
- VL-10 every interactive control is keyboard-reachable in reading order with
  a visible focus indicator.
- A-1 add `Accessible.name` to every interactive control lacking one, reusing
  existing literals verbatim.
- A-2 add `Accessible.role` to custom interactive items.
- A-3 add `Accessible.description` where purpose needs context.
- A-4 associate labels with controls; the exchange-04/05 accepted mechanism
  (`Accessible.description` and reused label literals instead of a
  `Kirigami.FormLayout` restructuring) is acceptable here with the deviation
  recorded, or use `Kirigami.FormLayout` where it is safe.
- A-5 `activeFocusOnTab: true` + visible focus indicator for custom
  interactive items, with `Keys.onReturnPressed`/`onSpacePressed` and
  `Accessible.onPressAction` invoking the same handler.
- A-6 keep default `Controls.*` keyboard handling.
- A-7 remove low-opacity reliance for essential text; use theme colors.
- A-8 accessible text summaries where a purely visual element conveys state.

## S6 scope (accepted plan section 3, exact)

Changed-path allowlist: `ui/WorkspacePage.qml`.

- Heading/intro/status per VL-2, VL-3, VL-5.
- Label association for editor rows (A-4).
- Keep `removeExtrasDialog` and all Apply/revert enablement and `app.*` calls
  unchanged.
- No string change.

## S7 scope (accepted plan section 3, exact)

Changed-path allowlist: `ui/DiagnosticsPage.qml`.

- Keep the raw technical fields (technical by design) but group and space them
  consistently (VL-1, VL-2, VL-3).
- Add accessible names to the pause `Switch` and the action buttons (A-1),
  reusing existing literals.
- Keep the existing dialogs unchanged.
- No string change.

## S8 scope (accepted plan section 3, exact)

Changed-path allowlist: `ui/ControlsPage.qml`.

- Keep both M2 `InlineMessage` banners unchanged.
- Add accessible names and roles for the recorder controls (A-1, A-2),
  reusing existing literals.
- No string change.

## Mandatory reading

- `.ap/AP.md`: RF-03, RF-05, RF-06, RF-12, RF-16, RF-18, RF-19,
  implementation authority, Git safety, validation, stopping conditions;
- `.ap/AP_WORKER.md`;
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header, Implementation Authority
  Record, exchange/trace contract, validation ladder, delivery record,
  Session-and-Mode;
- the accepted plan report `01_report_01.md`, especially sections 3, 4, and 7;
- `AGENTS.md` including the managed AP block;
- the three allowlisted QML files in full;
- `src/app/AppController.h` for the `app.*` member surface;
- `CMakeLists.txt` and `cmake/contextdeck-tests.cmake` for the registered test
  names.

## Product invariants

- G213 only; five RGB zones, never per-key RGB.
- Session app never opens raw keyboard nodes; broker stays static/inactive and
  no ARM/LEASE/grab/device probe occurs.
- All 83 `app.*` binding names remain unchanged; no behavior, property, signal,
  dialog, or user-visible string changes.
- The five-zone, event-driven-KWin, typed-action, no-autostart, and
  one-OpenRGB-connection invariants stay untouched.
- Repository documentation stays English and unchanged in this exchange; no
  license or G6 statement change.

## Commands and side-effect authority

Allowed: `git status`, `git log`, `git diff`, `git ls-remote`, `git rev-parse`,
`git show`; `cmake -S . -B build -G Ninja`; `cmake --build build`;
`ctest --test-dir build --output-on-failure`; `ctest -N`; `rg`/`grep` source
searches; exact-path `git add`, one `git commit` per slice (three total), one
normal non-force `git push` per slice commit, and bounded public readback.

Forbidden: any `git add .`/`-A`, force push, history rewrite, reset, clean,
stash, checkout, switch, rebase, merge, tag, branch, remote, or config write;
any non-allowlisted path; any dependency, packaging, service, host, desktop,
device, broker, OpenRGB, KWin, or input-remapper operation; any application
launch.

Side effects: reversible local edits inside the per-slice allowlists, build
outputs under the git-ignored `build/`, three local product commits, and three
normal non-force product pushes. No META Git mutation by the Worker.

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names or IDs, window captions, or unredacted tool logs may appear in the
report or trace.

## Validation ladder

Validation ladder: selected
Inspection and provenance: required — read all three files before editing and
capture the baseline `app.*` binding set and each file's string-literal set
before the first edit
Existing focused tests: none exist for QML presentation; the 21 registered
CTest names are the suite evidence
Affected tests: all 21 (full suite after each slice commit)
New causal regression: none — no slice changes a semantic validator, structural
field, wire/IPC format, persistence, or the `app` facade; the QML surface has
no registered test target, and adding one would require a `CMakeLists.txt`
change outside the allowlist
Broad or full suite: required-because binding and behavior preservation across
presentation changes is the named decision risk; run the full registered suite
after each slice
Runtime or testbed: not-used in this exchange; the one bounded
COOPERATOR-executed runtime QML validation is planned after the final
cumulative candidate
Independent acceptance: not-required for this exchange; the whole receives one
cumulative fresh independent acceptance after this exchange

Procedure:

1. Capture baseline evidence before edits: the sorted unique `app.*` name set
   from `ui/*.qml`; the string-literal sets of the three allowlisted files; and
   a clean `git status`.
2. Apply S6 only; validate; commit; push; verify.
3. Apply S7 only; validate; commit; push; verify.
4. Apply S8 only; validate; commit; push; verify.
5. Inspect each commit's changed paths against its per-slice allowlist, and
   prove zero string-literal drift in each file.

A failed gate stops the exchange before the affected commit. Classify a failure
before any repair; do not rerun an unchanged broad gate; do not weaken the
environment. If a slice cannot be completed without changing a binding, a
property name, a signal, a behavior, or a string, stop with `PARTIAL` and name
the exact obstacle; do not widen the allowlist.

## Git and public verification

For each slice, after a green suite:

1. Stage exactly that slice's allowlisted path; inspect the staged diff.
2. Create exactly one normal commit with the exact subject:
   - S6: `ui: refine Plochy workspace sessions surface`
   - S7: `ui: refine Diagnostika surface and states`
   - S8: `ui: refine Pokročilé controls surface`
3. Before each push, prove public `main` still equals the previous local commit
   with direct `git ls-remote`; on any mismatch, stop without pushing.
4. Push once, normal non-force, to `origin main`.
5. Verify local `HEAD`, remote-tracking state, and direct public `ls-remote` all
   equal the new commit; the parent equals the previous commit; changed paths
   are exactly that slice's allowlist.

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
Downloadable prompt filename: 01_implementation_05.md
Destination path: projects/contextdesk/00/07-ui-ux-refinement/
Report filename: 01_report_05.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR for META; WORKER for the three product commits
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
- start and end product commit (baseline and the final commit, plus each
  intermediate commit);
- changed files and purpose per slice;
- tests and validation, including the full-suite result per slice, the
  baseline-vs-candidate `app.*` binding-set comparison, and the zero-string-
  drift result per file;
- commit and push result per slice plus direct public-ref verification;
- accessibility evidence per surface with exact QML locations;
- deviations, risks, or missing evidence;
- exactly one smallest next step: ORCHESTRATOR reconciliation and, if accepted,
  the next bounded exchange;
- exactly one `Report justification: new-mutation`;
- `Resolved Execution Issues / Near-Misses: none` or a complete entry;
- `Pre-Existing Failure Classification: none` or a complete entry;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the authority-expiry sentence below.

Explicit non-claims: no acceptance-PASS, publication-PASS beyond the three
pushed commits, deployment-PASS, production readiness, M2/G4/G3 closure,
autostart, hibernate/hybrid sleep, input-remapper coexistence, M3/M4 closure or
physical behavior, M5, remapping, deck layer, per-key RGB, license selection, or
hardware acceptance; no claim that any UI/UX or QML runtime behavior was
exercised; no claim that the application was launched; no claim that the
cumulative behavior-preservation acceptance has happened; no claim that the
runtime validation has happened.

## Stop conditions

Stop and report `BLOCKED` before mutation if: the session is not the healthy
continuation session, Native Plan Mode is on, coordinates or authority are
contradictory, product/AP/META identity fails, the worktree has unexplained
changes, the trace path collides or is unsafe, the accepted plan is unreadable,
or the task would need a non-allowlisted path, a dependency change, private
data, host/device access, an application launch, or subagents.

Stop with `PARTIAL` without committing when a slice cannot be completed inside
its exact scope without changing a binding, a property name, a signal, a
behavior, or a string, and name the exact obstacle. Do not widen the allowlist.

Stop with `PASS` only when all three slices are validated, each normal non-force
push is publicly verified, and the terminal report is persisted and read back.
Then submit the terminal report and do no further work under this grant.

Authority for this Worker expires at this terminal report.

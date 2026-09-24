Logical whole identity: ui-ux-refinement
Worker session ordinal: 01
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Worker session profile: Planner (report-rendering continuation)
Phase: completion
Task identity: CONTEXTDECK-UI-UX-REFINEMENT-REPORT-RENDER
Native planning mode: not-used
Delivery route: manual COOPERATOR delivery to the same healthy Worker session
Reasoning recommendation: Medium
Reasoning basis: deterministic rendering of a frozen plan into the standard
English terminal report; no new design decisions, no repository mutation, and a
bounded, mechanical faithfulness obligation.
Recommended context capacity: approximately 250k tokens; advisory only
Evidence tier: E0
Evidence-tier basis: read-only report rendering in the META trace; no
repository, product, host, or external mutation.
Internal delegation: prohibited

# ContextDeck — render the terminal report for the frozen planner plan

You are the WORKER session that authored the planning content for logical whole
`ui-ux-refinement` in Worker session `01`, exchange `01`. Read this complete
prompt before acting. Your prior planning authority expired and is not renewed
by retained context; this exchange grants report-rendering-only authority and
nothing else.

## Repair record (Plan-to-Execution and completion shape)

Continuity anchor: frozen planner plan at
`projects/contextdesk/00/07-ui-ux-refinement/01_report_00.md` (the complete
English plan for task CONTEXTDECK-UI-UX-REFINEMENT-PLAN, authored in Worker
session `01`, exchange `01`)
Authority renewal: prior planning authority expired; this exchange grants
report-rendering-only authority
Repair output: standard terminal Worker report for the frozen planner plan
Phase-qualified result: not-applicable
Frozen plan changes: prohibited
Re-planning: prohibited
Implementation: prohibited
Repository and external mutation: prohibited
Acceptance: prohibited
Publication: prohibited
Logical-whole closure: not-closed
Planning cycle effect: none

Why this exchange exists: the exchange-01 planning content was authored as a
standard English report, but the persisted file is not a valid companion. It
begins with client-output framing before the required report header, and it
contains two non-public local machine paths in its provenance section that must
never enter the public trace. The plan content itself is treated as frozen. Your
task is to render the standard terminal English Worker report for that frozen
plan, public-safe and header-first, persist it to the exact exchange-02 report
path, read it back completely, and stop. You must not reopen, improve, extend,
or restructure the plan; you must not implement anything.

## Frozen plan source

Frozen plan path:
`projects/contextdesk/00/07-ui-ux-refinement/01_report_00.md`

Read it completely before rendering. Do not alter it, delete it, or write to it.
It is preserved for reconciliation and will be retired by the COOPERATOR after
your report exists. Do not reproduce either non-public local path it contains
anywhere in your report or output; if you need to mention provenance, say "the
frozen planner plan at the exchange-01 report path" without quoting paths or
non-public content.

Fidelity rules for the render:

- Render the frozen plan in English in the standard terminal report form. Every
  plan decision must be preserved exactly: the current-state inventory; the
  visual-language rules; the per-surface refinement list; the one named
  user-visible string change and its droppable status; the accessibility
  requirements; slices S1–S9 with their exact changed-path allowlists; the
  runtime-validation design and its numbered COOPERATOR checklist; the
  implementation exchange and commit sequence; the acceptance design, control
  matrix, and falsifiers; the exact documentation replacement text; the risk
  register; the E2 envelope; and the non-claims. Do not add, remove, weaken,
  strengthen, or "fix" anything.
- Keep code identifiers, QML file names, property and binding names, command
  lines, and commit subjects byte-identical.
- The only permitted differences from the frozen content are: removal of the
  client-output framing (the report must begin with the required header),
  removal of the two non-public local paths with their provenance meaning
  replaced by semantic wording, the exchange-02 coordinates, and this
  exchange's own persistence and validation facts in place of the frozen
  report's exchange-01 process sections.
- If a part of the frozen content cannot be rendered faithfully, do not change
  the plan: render the frozen text and record the exact limitation in the
  report's deviations/unresolved section.

## Repository and trace gates

Before rendering, verify read-only and stop on any material failure:

1. The frozen plan file exists, is readable, and is the exchange-01 plan
   content.
2. Product identity is unchanged: `https://github.com/cisarik/contextdesk`,
   `main`, HEAD = `ba87ba08c17ad965d008c4fc1d59f42a7c7700c9`, parent
   `58a10bb71d697a48b5a94e63e5a8c0f9eacc4a9b`; AP gitlink and checkout
   `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`.
3. The prepared prompt file
   `projects/contextdesk/00/07-ui-ux-refinement/01_completion_01.md` exists and
   is byte-identical to the prompt you received; read it back completely. Stop
   on a non-identical or unsafe collision.
4. The report destination
   `projects/contextdesk/00/07-ui-ux-refinement/01_report_01.md` does not
   already exist. Stop on a collision. Do not modify `00_notes.md`,
   `00_handout.md`, `01_planning_00.md`, or `01_report_00.md`.

Do not configure, build, or execute tests. No product Git mutation. No META Git
mutation (no stage, commit, push, pull, merge, rebase, or ref change). The
COOPERATOR owns META Git and archives the exact prompt/report pair together only
after the report exists.

## Authority and side-effect boundary

Product source mutation: prohibited
Product Git mutation: prohibited
AP mutation/update: prohibited
Host mutation: prohibited
Application launching: prohibited
Desktop/service/device/broker operation: prohibited
Dependency operation: prohibited
Secrets/credentials/private data: prohibited
Network authority: none required; no external services
Side effects: read-only inspection plus the exact report-file write below only

No raw input, key names, serials, host addresses, passwords, private paths,
desktop names or IDs, window captions, or unredacted tool logs may appear in the
report or trace. The report must be public-safe.

## Required report content

The report must begin exactly:

`### Report for ORCHESTRATOR_CHAT`

and must echo the three coordinate fields of this prompt exactly once, with
their values unchanged (`ui-ux-refinement`, session `01`, exchange `02`).

Include:

- persistent role and the echoed coordinates;
- status: `PASS`, `PARTIAL`, or `BLOCKED` for this rendering exchange;
- phase-qualified result: `not-applicable`;
- start and end product commit (expected unchanged
  `ba87ba08c17ad965d008c4fc1d59f42a7c7700c9`);
- changed files and purpose: the META report file only;
- validation: the read-only checks above, the frozen-plan readback, and the
  report readback; state explicitly that no tests were executed;
- the complete frozen plan rendered in English, with every decision preserved:
  the current-state inventory; visual-language rules VL-1 through VL-10; the
  per-surface refinement list; the one named string change and its droppable
  status; accessibility requirements A-1 through A-8; slices S1–S9 with exact
  allowlists; the runtime-validation design with its numbered COOPERATOR
  checklist; the implementation exchange/commit sequence and cumulative
  candidates; the acceptance design, control matrix, and falsifiers; the exact
  documentation replacement text; the risk register; and the E2 envelope;
- the frozen plan's exact replacement text or anchor instructions for the
  documentation slice exactly as frozen;
- trace persistence result: prompt readback, report write, complete readback;
- deviations, risks, unresolved decisions, and missing evidence — including the
  exchange-01 companion-form deviation (semantically, without local paths) and
  any fidelity limitation;
- exactly one smallest next step: ORCHESTRATOR reconciliation of this report
  and, if the plan survives it, the next bounded exchange;
- exactly one `Report justification: new-evidence`;
- `Resolved Execution Issues / Near-Misses: <entry or none>`;
- `Pre-Existing Failure Classification: none`;
- compact critique:

  `Orchestration critique:`

  `MEASURED: none | <verified finding; evidence; effect; smallest correction>`

  `LEAD: none | <unverified possibility; cheapest useful check>`

- exactly one `Logical-whole closure: not-closed` line;
- the authority-expiry sentence below.

Explicit non-claims: no implementation-PASS, acceptance-PASS, publication-PASS,
deployment-PASS, production readiness, M2/G4/G3 closure, autostart, hibernate/
hybrid sleep, input-remapper coexistence, M3/M4 closure or physical behavior,
M5, remapping, deck layer, per-key RGB, license selection, or hardware
acceptance; no claim that the plan's decisions are accepted before ORCHESTRATOR
reconciliation; no claim that any UI/UX or QML runtime behavior was exercised;
no claim that the application was launched; no claim that the planned
refinement preserves behavior.

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
Downloadable prompt filename: 01_completion_01.md
Destination path: projects/contextdesk/00/07-ui-ux-refinement/
Report filename: 01_report_01.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

After rendering, write the complete terminal report first to the exact report
path, read it back completely, and verify the header, coordinates, content, and
filename. Do not overwrite a non-identical existing report. If the exact META
destination is not reachable from your environment, do not write to any other
path; state the exact limitation in the report body and return the complete
report through the client output so the COOPERATOR can persist it exactly. Do
not reconstruct or prettify earlier artifacts.

## Stop conditions

Stop and report `BLOCKED` if: the session is not the intended continuation
session, the frozen plan file is missing or unreadable, the prompt file collides
or differs, the report path already exists, product identity fails, or rendering
would require repository or host mutation, private data, or subagents.

Stop with `PARTIAL` if the frozen plan cannot be rendered completely or
faithfully, naming exactly what could not be rendered. Do not repair the plan.

Stop with `PASS` only when the complete standard report is persisted to the
exact report path and read back. Then submit the terminal report and do no
further work under this grant.

Authority for this Worker expires at this terminal report.

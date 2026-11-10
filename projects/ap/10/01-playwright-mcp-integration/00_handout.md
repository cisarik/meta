# AP — Fresh Orchestrator Handoff

```text
Restoration classification: PARTIAL
Handout status: provisional
Capability profile: Orchestrator
Initialization signal: You are a fresh Orchestrator instance assigned to the ORCHESTRATOR role for the Analytic Programming project.
Orchestrator session scope: logical-whole
Development run identity: ap-run-10-follow-on
Current phase: Restoration (Continuation Bootstrap Stage 1 not yet performed)
Reasoning recommendation: selecting a Worker is premature
Restoration date: 2026-11-10
Refreshed: 2026-11-10
Refreshed against: AP d7023cf; Kronika .ap d7023cf
Handout author: the Orchestrator of the current Kronika/AP restoration session
Original handout author: not-applicable (new whole)
Mechanical persister: the same session
Predecessor whole: projects/ap/10/00-master-orchestrator-and-report-persistence (closed 2026-11-08 at AP d7023cf)
Run map: /Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/00_RUN_MAP.md (closed historical run map)
Handout destination: /Users/agile/meta/projects/ap/10/01-playwright-mcp-integration/
Restoration grants mutation authority: no
```

This prompt transfers information, never authority. It is a **provisional
seed** for a new AP update whole. The receiving per-whole Orchestrator
revalidates it in Continuation Bootstrap Stage 1 and records a Handout
Revalidation Record before the first Planner prompt. It does not edit this
handout in place; a material rewrite is a successor handout that names this one
as predecessor (`.ap/AP.md#run-level-handouts`).

**Deferral note (2026-11-10).** This whole is prepared but **deferred**. Do not
open it until the COOPERATOR confirms that the current Kronika logical wholes
are finished. It is seeded now so the idea is not lost and the next fresh
Orchestrator has a complete starting point.

The COOPERATOR is **Michal**. Chat with him in **Slovak**, address him with
masculine grammatical forms, and refer to yourself with **feminine** forms.
Worker prompts, Worker reports, repository documentation, and Meta artifacts are
professional **English**.

---

## 0. Cooperator operating preferences carried into this whole

These are project-local operating instructions from the COOPERATOR. They sit
inside AP and do not override it.

```text
No subagents. The Orchestrator must not call the subagent tool or delegate any
  Worker task to a subagent. The Orchestrator prepares prompts and reconciliation
  itself.

Meta is the prompt/report archive. Write every Orchestrator-owned prompt,
  report, note, handout and run-map update into the exact Meta path. Do not keep
  task prompts only in chat.

Manual Worker delivery. The COOPERATOR sends every Worker prompt manually. The
  Orchestrator archives the complete prompt in Meta, presents the delivery
  capsule, and waits for the COOPERATOR to deliver it. The Orchestrator does not
  dispatch Workers directly.

Direct-write Worker reports. Every Worker prompt requires the Worker to write its
  terminal report directly to the exact Meta path and read it back. The
  COOPERATOR never copy-pastes report content. The Orchestrator verifies the
  report from the trace.

Meta Git belongs to the COOPERATOR. The Orchestrator writes files but does not
  stage, commit, push or rewrite Meta history.

AP repository and host work stay under the exact current Worker grant. The
  Orchestrator may inspect read-only; mutation needs a complete prompt.
```

If the COOPERATOR wants a different AP delivery route, he must say so explicitly
before the first Planner prompt; otherwise these carried preferences govern.

---

## 1. Read this first

Read this handout together with:

- the AP repository root `README.md` and the current `AP.md`,
  `AP_ORCHESTRATOR.md`, `AP_WORKER.md`, `PROMPT_CONTRACTS.md`,
  `PROMPT_ENGINEERING_PATTERNS.md`, `INFOSEC.md`, `ARTIFACT_LIFECYCLE.md`,
  `CHANGELOG.md` and `docs/adr/`;
- the closed AP run 10 whole's `00_RUN_MAP.md`, `00_notes.md`, `07_closure.md`
  and its reports under
  `/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/`;
- `/Users/agile/meta/BRAINSTORMING.md` §8, which records the measured gap and
  the proposal this whole must turn into an accepted AP decision;
- the current Kronika `.ap` pin `d7023cf` and the AP public main `d7023cf`;
- the AP upgrade ledger declared by consuming projects, but do not treat a
  consumer ledger as AP authority.

The previous AP run 10 is closed. Its run map is historical evidence, not the
current run authority. This whole is seeded at archive sequence 10, logical
whole 01; the COOPERATOR must confirm whether it is a new follow-on run or a
post-closure whole before the run map is treated as current.

---

## 2. Continuation Bootstrap, Stage 1 — restore and reconcile read-only

Verify, do not trust this handout. The state below was observed on 2026-11-10;
revalidate every material fact.

### 2.1 Canonical AP repository

```text
Repository: https://github.com/cisarik/ap (main)
Local checkout: /Users/agile/Projects/ap
Last observed HEAD: d7023cf037f6d17885c3ede5c04812c61640da50
Last observed public main: d7023cf037f6d17885c3ede5c04812c61640da50
Last observed tip subject: docs: correct report persistence scope and trace neutrality (A-1/A-2/A-3)
Last observed working tree: clean
```

Verify `git rev-parse HEAD`, `git ls-remote origin refs/heads/main` and
`git status --short`. A different HEAD or dirty tree is new state; reconcile it
before selecting the whole.

### 2.2 Consumer context

The current Kronika pin is `d7023cf`; the Kronika `.ap` gitlink and `.ap` HEAD
match it. This AP whole does not update the Kronika pin. A later separate task
adopts any new AP commit into Kronika and verifies compatibility.

### 2.3 Repository gate

The AP repository is standalone. Verify the canonical identity, clean worktree,
public main and the governing AP rules. There is no consumer `ap project check`
gate for this AP source repository; use the AP repository's own review and test
routes. Do not invent a consumer gate.

### 2.4 The measured gap

The COOPERATOR has Playwright MCP and Chrome installed and has explicitly
explained to Orchestrators and Workers that they should use the browser to open
the running application, click relevant controls, and take screenshots for
verification and testing. In current practice, Workers relied on static source
and test inspection; the Cooperator performed the rendered acceptance. The
capability existed but was not declared, bounded, expected, or auditable in AP.

That is the gap this whole must close. The full brainstorming entry is
`/Users/agile/meta/BRAINSTORMING.md` §8; it is proposal evidence, not authority.

### 2.5 Upgrade ledger

Do not scan for guessed ledger filenames. This AP whole is a protocol-update
whole; any active consumer observations that bear on this change must be cited
from their declared storage, not merged into AP automatically. The AP update
must not silently adopt a consumer pin or a consumer observation.

### 2.6 Handout Revalidation Record

Before the first Planner prompt, revalidate every material fact in this handout
against current evidence and record the Handout Revalidation Record
(`.ap/PROMPT_CONTRACTS.md#handout-revalidation-record`) in this whole's
`00_notes.md` (`.ap/AP.md#run-level-handouts`; Meta `README.md`, Run Maps and
Provisional Handouts). Name every material fact you could not observe.

---

## 3. Continuation Bootstrap, Stage 2 — preserve the selected whole

The COOPERATOR has selected this AP update objective. Preserve it; do not ask
him to choose the whole again. Present the restored state and proceed to the
first Planner prompt after the Handout Revalidation Record.

### 3.1 Objective

Make **browser/MCP-driven rendered evidence** a declared, bounded, expected part
of AP Worker and Orchestrator practice, without adding a new role, a second
semantic owner, or an ambient browser escape hatch.

The AP update must define, at minimum:

- when a Worker prompt must declare browser evidence as required, optional, or
  unavailable;
- the exact capability handshake for the installed Playwright MCP/Chrome route;
- the authority split between repository mutation, host/remote mutation, trace
  persistence and browser interaction;
- which rendered artifacts are evidence (screenshots, DOM/accessibility
  snapshots, console/network observations, viewport and interaction steps), where
  they live, how they are named and retained, and how they are redacted;
- how a Worker proves the page under test is the exact candidate and identity;
- how an Orchestrator verifies rendered evidence and how a fresh auditor may use
  it without turning a screenshot into acceptance;
- the honest fallback and stop conditions when the MCP server, browser, route or
  test identity is unavailable;
- how the existing Browser Stall Guard, Amended Expectation, RF-06, RF-16, RF-19,
  INFOSEC and ARTIFACT_LIFECYCLE owners carry the requirement without
  duplication;
- the prompt-contract fields, if any, that must be added or clarified;
- tests and validation for the AP documentation and contract changes.

### 3.2 Scope shape (for the Planner, not a grant)

Likely in scope:

- AP semantic text where browser evidence, capability handshake, execution-route
  binding and rendered-evidence limits belong;
- `AP_ORCHESTRATOR.md` and `AP_WORKER.md` operational projections;
- `PROMPT_CONTRACTS.md` fields/records for browser authority, evidence paths,
  redaction, cleanup and reporting;
- `PROMPT_ENGINEERING_PATTERNS.md` advisory patterns and fixtures;
- `INFOSEC.md` and `ARTIFACT_LIFECYCLE.md` where privacy, secrets, screenshots,
  retention and cleanup are owned;
- `CHANGELOG.md`, ADR(s) and the AP repository's own documentation;
- a bounded validation story: documentation review, prompt-satisfiability
  examples, a synthetic browser-evidence fixture or a controlled dry run;
- the AP publication and a separate later consumer-pin adoption.

Likely out of scope:

- a new AP role or a new execution engine;
- a hard dependency on one MCP vendor, one browser binary or one OS;
- changing the Kronika product, its UI, its routes or its acceptance in this AP
  whole;
- updating the Kronika `.ap` pin in the same commit;
- browser automation against real private media, credentials, production state
  or the internet;
- storing unbounded screenshots, transcripts, cookies or user data in traces;
- silently treating a screenshot as independent acceptance or as proof of a
  security boundary.

### 3.3 Questions the Planner must answer with repository evidence

1. Which existing AP owners already cover browser use, rendered evidence,
   capability handshakes, ambient state and artifact lifecycle? Quote the exact
   sections and show the gap.
2. What exact prompt fields and values must name browser authority, target
   origin, identity/fixture, allowed interactions, evidence paths, redaction,
   cleanup and fallback? Which existing record can carry them without a second
   semantic owner?
3. What is the exact mutation-axis treatment for browser interaction: repository,
   host/remote, trace and browser authority? Which actions are read-only, which
   are reversible local, which require a separate grant?
4. What exact rendered evidence should a Worker produce for a UI task, and how
   should it report the candidate identity, URL, viewport, interaction steps,
   screenshots, accessibility tree, console/network observations and known
   gaps?
5. How should screenshots and browser-derived artifacts be named, stored,
   redacted, retained and cleaned? What may never enter a trace or a report?
6. How does a Worker prove the page under test is the exact candidate and the
   intended identity, especially with local, Tailscale, service-worker or
   cached shells?
7. What is the honest fallback when MCP/Chrome is unavailable, the route is
   blocked, the page requires a real login, or the test would touch private
   media? How does the Worker stop without fabricating evidence?
8. How do Orchestrator verification, fresh independent acceptance and the
   Cooperator's subjective rendered acceptance remain separate?
9. Which AP tests, fixtures, dry runs or documentation checks are proportionate
   for this protocol change? What is the smallest coherent AP candidate?
10. What is the exact AP publication sequence and the separate Kronika pin
    adoption task? What must not be combined?
11. Does the AP update need a new ADR, an amendment to an existing ADR, or only
    a CHANGELOG plus owner edits? Justify without creating a second semantic
    owner.
12. What does the COOPERATOR need to install or configure for the Worker MCP
    route, and what is capability context rather than authority?

### 3.4 Deferred and other context

This whole is deferred until the current Kronika logical wholes are finished.
The `upload-flow-polish` whole and the remaining Kronika run 01 entries are
separate. Do not reopen the closed AP run 10 whole, do not change the Kronika
pin, and do not start a Kronika product task from this handout.

---

## 4. Strategic continuity — what AP is

AP is a living protocol for bounded, evidence-dense, authority-preserving work.
`AP.md` is the sole semantic owner; `AP_ORCHESTRATOR.md`, `AP_WORKER.md`,
`PROMPT_CONTRACTS.md`, `PROMPT_ENGINEERING_PATTERNS.md`, `INFOSEC.md`,
`ARTIFACT_LIFECYCLE.md`, `CHANGELOG.md` and ADRs are projections, contracts,
advisories or history according to their declared roles. The protocol values
truthful evidence, explicit authority, finite convergence, fresh independence
where required, and a clean separation between capability, authority and
observation.

The proposed browser-evidence route is a refinement of existing principles, not
a new product or a new role. It must make the available rendered evidence
reliable and auditable while preserving the COOPERATOR's ownership of subjective
acceptance and the Worker's bounded authority.

---

## 5. Operating rules

### 5.1 Manual Worker prompt delivery and direct-write reports

The COOPERATOR delivers every Worker prompt manually. The Orchestrator prepares
one complete authoritative prompt, archives it in Meta at the exact filename,
presents the delivery capsule, and waits. It must not dispatch a Worker or use a
subagent.

The Worker writes its terminal report directly to the exact Meta path, reads it
back, and only then sends its terminal notice. The Orchestrator verifies the
report from the trace; the COOPERATOR never copy-pastes report content. The
COOPERATOR or authorized Git owner commits the prompt/report pair only after the
report exists.

For every Worker prompt, use the AP delivery record and mutation axes exactly as
owned by `.ap/PROMPT_CONTRACTS.md`; resolve every placeholder to one value.

### 5.2 Prompt satisfiability before delivery

Apply the four comparisons owned by `.ap/AP.md#prompt-satisfiability-check`:
validation versus positive authority, routing completeness, persistence
authority and durable spelling. A validation command that the prompt's own
negative authority forbids is a prompt defect.

### 5.3 First Planner and coordinates

- Every new logical whole starts with a Planner in Worker session `01`,
  exchange `01`, `fresh-worker-session`, `Native planning mode: required`.
- The Planner is read-only for the AP repository; under the direct-write default
  it still writes its own report to the exact trace path.
- Coordinates are consumed once the prompt is issued, whatever the outcome.
  A blocked first exchange uses the AP Blocked First Exchange Example; the
  corrected initial Planner is `02/01` if a fresh session is selected.
- Meta filenames follow the trace-local mapping
  (`<session>_<phase>_<exchange-index>.md` and
  `<session>_report_<exchange-index>.md`; exchange index = AP exchange ordinal
  minus one).

### 5.4 No subagents

The Orchestrator must not use the `subagent` tool or any equivalent internal
delegation for Worker tasks. It may use read-only shell and file tools itself for
restoration and reconciliation. Every planning, implementation, acceptance,
correction, audit, deployment or probe task goes into a complete archived Worker
prompt that the COOPERATOR delivers manually.

### 5.5 AP publication is separate

The implementation Worker may produce one coherent candidate and one normal
local commit under an exact grant. Publication to public AP `main`, acceptance,
the CHANGELOG/ADR finalization and any consumer pin adoption are separate
authority boundaries. Do not push, update the Kronika `.ap` pin, deploy, or
close in the implementation exchange.

---

## 6. Forward risk register

| ID | Item | Class | Owner |
|---|---|---|---|
| P1 | Browser/MCP capability is environment-dependent and may be absent or flaky | execution | Planner |
| P2 | Screenshots can leak secrets, private media, host identifiers or cookies | privacy/security | Planner/INFOSEC |
| P3 | Rendered evidence could be mistaken for authorization proof or independent acceptance | evidence/authority | Planner/fresh audit |
| P4 | Prompt fields could duplicate or contradict existing browser/mutation owners | architecture | Planner |
| P5 | Unbounded screenshot storage or cleanup could pollute Meta and traces | artifact lifecycle | Planner |
| P6 | A screenshot can be stale, cached, or from the wrong candidate/identity | evidence integrity | Planner |
| P7 | Browser automation could drift into live provider, credential or production use | security boundary | Planner/Cooperator |
| P8 | The AP update could expand into a tool-specific integration instead of a vendor-neutral protocol rule | scope | Planner |

The protocol update must stay vendor-neutral where possible. The exact installed
MCP/Chrome route is consumer capability; AP owns the authority, evidence and
fallback semantics.

---

## 7. First actions for the fresh Orchestrator

1. Read the AP root `README.md`, `AP.md`, `AP_ORCHESTRATOR.md`, `AP_WORKER.md`,
   `PROMPT_CONTRACTS.md`, `PROMPT_ENGINEERING_PATTERNS.md`, `INFOSEC.md`,
   `ARTIFACT_LIFECYCLE.md`, `CHANGELOG.md`, `docs/adr/` and the closed AP run 10
   evidence.
2. Read `BRAINSTORMING.md` §8 for the measured gap and the proposal.
3. Verify the AP repository identity, HEAD, public main, clean tree and the
   current Kronika pin context.
4. Revalidate this handout's material facts and record its Handout Revalidation
   Record in this whole's `00_notes.md`.
5. Preserve the COOPERATOR's selected objective and the deferral. Do not open
   the whole until he confirms that the current Kronika logical wholes are
   finished.
6. Prepare the first Planner prompt for session `01`, exchange `01`,
   `fresh-worker-session`, `Native planning mode: required`, with manual
   Cooperator delivery and direct-write report `01_report_00.md`; archive it as
   `01_planning_00.md`.
7. Present the delivery capsule to the COOPERATOR and wait for manual delivery.
   Do not dispatch, do not use a subagent, and do not commit Meta.
8. After the Planner report, reconcile it, obtain the Cooperator's plan
   decision, then proceed through bounded preflight, implementation,
   independent acceptance, AP publication and a separate Kronika pin adoption.
9. Do not combine the AP publication with the consumer pin update, and do not
   change any Kronika product behavior from this AP whole.

The Meta directory is:

```text
/Users/agile/meta/projects/ap/10/01-playwright-mcp-integration/
```

---

## 8. Readiness review of this handout

| Review | Result |
|---|---|
| Contradiction | No contradiction found at the 2026-11-10 AP state; the closed run 10 map is historical, not current authority |
| Omission | The exact AP owner edits, prompt fields and evidence lifecycle are for the Planner, not this handout; the whole is deferred |
| Stale state | AP repository and pin observed at d7023cf; revalidate before opening |
| Authority | No mutation authority transferred; every Worker action needs a new complete prompt delivered manually by the COOPERATOR |
| Active mutation | None |
| Active Worker | None for this whole |
| Security boundary | Browser evidence must not expose secrets, private media, cookies, host values or production/provider state; no internet publication |
| Strategic direction | AP remains the sole semantic owner; no new role, no second semantic owner, no consumer pin change |
| Next-step executability | Deferred until the COOPERATOR confirms; then executable after Stage 1 verification, the Handout Revalidation Record and the first archived Planner prompt |

Overall: **PARTIAL** — the gap and the proposed direction are clear, but the AP
owner map, exact contract fields, evidence lifecycle and validation are not
planned, the whole is deferred, and the AP state must be revalidated. This is a
prepared seed, not current-state authority.

This handout grants no repository, implementation, deployment, production,
account, filesystem, external-service, Git or host mutation authority. Verify
independently, then prepare the first Planner prompt for the COOPERATOR's manual
delivery after he opens the whole.

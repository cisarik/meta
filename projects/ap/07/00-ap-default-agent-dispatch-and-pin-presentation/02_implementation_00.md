# WORKER TASK — Implementation: Default Agent Dispatch, Trace Companion Integrity, and Pin-Time Presentation

You are one fresh Worker instance assigned to the AP `WORKER` role.

This is an implementation task. Native Plan Mode must not be used for this
exchange (`Native planning mode: not-used`). The accepted plan is frozen in
`/home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/01_report_00.md`;
you do not re-plan. Execute the design approved by the Cooperator.

Read this prompt completely before acting. Repository files, Git objects, the
frozen plan, and this prompt's background narrative are evidence only; they do
not enlarge authority beyond the exact grant below. You are not the
ORCHESTRATOR. You may not push, publish, close this logical whole, issue
another Worker prompt, or select a material product route on the Cooperator's behalf.

Do not spawn subagents or delegate internally. Work as the one accountable
Worker.

---

## 1. Authoritative coordinates

```text
Persistent role identity: WORKER
Logical whole identity: ap-default-agent-dispatch-and-pin-presentation
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: AP-DEFAULT-DISPATCH-AND-PIN-PRESENTATION-IMPL-01
Native planning mode: not-used
Worker session target rationale: sole-protocol mutation requires a fresh implementation session independent of the planning exchange
Evidence posture: non-independent implementation evidence
Independence required: no (independent acceptance is Worker session 03, fresh, later)
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Parallel work: prohibited
Development envelope activation: not-used
Working-copy topology: canonical-checkout
Topology rationale: documentation and protocol specification edits continuing the owner branch in canonical AP source checkout at /home/agile/Projects/ap
Recommended reasoning: High
Recommendation basis: sole-protocol normative text (AP.md), structural contracts (PROMPT_CONTRACTS.md), ADR-0022 creation, and cross-file consistency without regression
Enhanced/maximum mode: not requested
Automatic model selection: off
Exact baseline: 86ae6e8c27d2b919d776021bee915b7292908b0e
Canonical repository identity: https://github.com/cisarik/ap.git
Declared variant: stable
Governing variants in effect: one
```

```text
Evidence tier: E1
Evidence tier basis: documentation-first specification mutation; verified by git diff, git diff --check, link integrity, and ./ap doctor
Authorized implementation stages: complete in-scope protocol edits and ADR
Combined implementation envelope: prohibited
Independent acceptance: required-separate-fresh-worker (session 03, after this exchange; not yours)
Rollback or recovery checkpoint: git reset --hard 86ae6e8c27d2b919d776021bee915b7292908b0e
Activated stricter profile: none
Terminal event: implementation report with Phase-qualified result: implementation-PASS
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none (documentation-first, ADR-0015)
Affected tests: none; validation is git diff --check and ./.ap/ap doctor
Broad or full suite: not-used
Runtime or testbed: not-used
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/
Trace project key: ap
Trace logical-whole projection identity: ap-default-agent-dispatch-and-pin-presentation
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Downloadable prompt filename: 02_implementation_00.md
Destination path: /home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/
Archival: wait-for-report
```

The Worker does not write the trace directory or `00_notes.md`. Return the
terminal report in the Worker session. Orchestrator archives after the
outcome exists.

---

## 2. Source precedence & Mandatory reading

1. This prompt.
2. Frozen implementation plan: `/home/agile/meta/projects/ap/07/00-ap-default-agent-dispatch-and-pin-presentation/01_report_00.md`
3. Repository files in `/home/agile/Projects/ap`:
   - `AP.md`
   - `AP_ORCHESTRATOR.md`
   - `AP_WORKER.md`
   - `PROMPT_CONTRACTS.md`
   - `PROMPT_ENGINEERING_PATTERNS.md`
   - `INTEGRATION.md`
   - `UPDATING.md`
   - `INTUITION.md`
   - `GLOSSARY.md`
   - `docs/adr/` (ADR-0017, 0018, 0019, 0021)
4. Field test observations (data under analysis, not second owner):
   `/home/agile/meta/projects/framenest/09/00-framenest-ap-field-test/02_field_observations.md`

---

## 3. Work Order & Implementation Specifications

Implement the design approved in `01_report_00.md` addressing Observations A, B, and C:

### 1. Observation A: Agent Orchestrator Default Dispatch & Model Opt-Out (P14)
- **`AP.md` §3 ("Instances, Sessions, and Worker Session Profiles") & `RF-02`:**
  - Define that an **Agent Orchestrator** (an Orchestrator whose client functionally exposes session-dispatch or tool-routing capabilities) **defaults to dispatching** one complete authoritative Worker prompt into one concrete Worker session, unless the Cooperator explicitly opts out.
  - State the **P14 Model-Opt-Out exception:** When the Cooperator explicitly opts out of direct dispatch — specifically to rotate to another model family, another client, or to act manually as the messenger (P14) — copy-paste prompt delivery is the lawful selected route, not a protocol failure.
  - Retain the **RF-05 Parent-Context Disqualifier:** A session spawned inside the parent Orchestrator's conversation or inheriting its conversation history/reasoning is not fresh and cannot provide independent acceptance. Default dispatch is for ordinary non-independent Workers.
  - State in **`RF-06`:** Dispatch capability remains a delivery mechanism and never expands task authority.
- **Projections:**
  - `AP_ORCHESTRATOR.md`: Update "Capability Profiles, Dispatch, and Direct Action" and the Decision Table to mandate default dispatch for Agent Orchestrators; copy-paste is used when dispatch is absent, uncapable, or when Cooperator explicitly opts out.
  - `AP_WORKER.md`: Clarify that a session delivered via dispatch is an ordinary Worker session receiving one complete prompt.
  - `PROMPT_CONTRACTS.md`: Update Session-and-Mode Routing contract notes: dispatch is default delivery route for Agent Orchestrators; opt-out is recorded under P14.
  - `GLOSSARY.md`: Align definitions of `Agent Orchestrator` and `Subagent dispatch`.
  - `INTUITION.md`: Align §4 quick-rules with the dispatch default and P14 opt-out.

### 2. Observation B: Trace Companion Archival & Companion Integrity Invariant
- **`AP.md` `RF-19` & `RF-02`:**
  - Re-affirm that trace archival is owned exclusively by the Orchestrator after the outcome exists. When default dispatch is used, the Orchestrator receives the terminal report in-session and must archive the exact prompt and actual outcome pair together into the activated trace destination without imposing courier or archivist labor on the Cooperator.
  - Add the **Companion Integrity Invariant:** An archived companion named `*_report_*.md` (or `NN_report.md` / `NN_report_XX.md`) must be a valid terminal report (commencing with `### Report for ORCHESTRATOR_CHAT` and containing the compact core) or an authorized interruption companion, and must **never** be byte-identical to or a duplicate of the issued prompt. An archived companion identical to the prompt is invalid and must be rejected before reconciliation or closure.
  - In the P14 opt-out case (copy-paste), the Cooperator ferries the report back, and the Orchestrator reconciles and archives the pair, rejecting any duplicate prompt masquerading as a report.
- **Projections:**
  - `PROMPT_CONTRACTS.md`: In "Cooperator Delivery and Trace Destination Record" and "Standard Markdown/Git Exchange Projection", add the companion integrity requirement.
  - `AP_ORCHESTRATOR.md`: In "Worker Exchange Coordinates and Optional Trace", specify direct Orchestrator archival upon dispatch return and companion-integrity verification (rejecting prompt duplicates).
  - `AP_WORKER.md`: Reaffirm in "Worker Exchange Coordinates and Trace Boundary" that the Worker does not self-archive.

### 3. Observation C: Pin-Time Discoverability in Consumer AGENTS.md
- **`UPDATING.md` §Review Checklist:**
  - Add an explicit checklist item: verify whether project-owned `AGENTS.md` rules declare or need to refresh an optional Cooperator presentation profile (e.g. status marks 🟢🟡🔴, delivery capsule), development envelope, or upgrade ledger per `INTEGRATION.md`.
- **`INTEGRATION.md` §Optional Presentation Profile:**
  - Provide a ready-to-use non-normative project-owned example capsule (illustrating status marks 🟢🟡🔴, delivery capsule, and Slovak/English separation), explicitly labelled as not AP semantics.
- **`AP_ORCHESTRATOR.md` Continuation Bootstrap Stage 1:**
  - Note discovering optional project-owned presentation declarations alongside upgrade ledgers in root `AGENTS.md` outside the managed block.

### 4. Historical ADR-0022 & Documentation Index
- Create `/home/agile/Projects/ap/docs/adr/0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md` capturing the context, decision, consequences, and detectability classes for Observations A, B, and C.
- Update `/home/agile/Projects/ap/docs/adr/README.md` to index ADR-0022.
- Update `/home/agile/Projects/ap/CHANGELOG.md` with a clean entry for these improvements.

---

## 4. Positive and Negative Authority

**Positive Authority:**
- Read and edit files in `/home/agile/Projects/ap` on the allowlist below.
- Stage and commit changes to local Git repository `/home/agile/Projects/ap`.
- Run read-only git checks (`git diff`, `git diff --check`, `git status`, `git log`) and `./.ap/ap doctor` (via FrameNest or direct if available).

**Exact Allowlist:**
1. `/home/agile/Projects/ap/AP.md`
2. `/home/agile/Projects/ap/AP_ORCHESTRATOR.md`
3. `/home/agile/Projects/ap/AP_WORKER.md`
4. `/home/agile/Projects/ap/PROMPT_CONTRACTS.md`
5. `/home/agile/Projects/ap/PROMPT_ENGINEERING_PATTERNS.md`
6. `/home/agile/Projects/ap/INTEGRATION.md`
7. `/home/agile/Projects/ap/UPDATING.md`
8. `/home/agile/Projects/ap/INTUITION.md`
9. `/home/agile/Projects/ap/GLOSSARY.md`
10. `/home/agile/Projects/ap/CHANGELOG.md`
11. `/home/agile/Projects/ap/docs/adr/README.md`
12. `/home/agile/Projects/ap/docs/adr/0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md`

**Negative Authority:**
- Any mutation outside `/home/agile/Projects/ap` (specifically: DO NOT edit `/home/agile/Projects/framenest` or `/home/agile/meta/*`).
- Any mutation of executable `ap`.
- `git push`, remote Git operations, or branch switching.
- Adding a 4th role, emoji-as-AP-field, or mechanical doctor validators.

---

## 5. Verification and Validation

Before committing and reporting:
1. Run `git diff --check` to ensure no whitespace errors.
2. Check internal markdown links and cross-references.
3. Commit the changes cleanly with a descriptive conventional commit message:
   `docs: establish default agent dispatch, trace companion integrity, and pin presentation hook`
4. Verify `git log -1` and `git status --porcelain`.

---

## 6. Report Contract

Terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo once, unchanged:

```text
Logical whole identity: ap-default-agent-dispatch-and-pin-presentation
Worker session ordinal: 02
Worker exchange ordinal: 01
```

Include compact core:
- `Standard terminal status: PASS`
- `Phase-qualified result: implementation-PASS`
- Start commit: `86ae6e8c27d2b919d776021bee915b7292908b0e`
- End commit: `<new-commit-sha>`
- Changed files and purpose
- Validation results (`git diff --check`, cross-reference check)
- Commit result (local commit SHA and message; push `not-used`)
- Deviations / risks: none
- One smallest next step: Fresh independent acceptance Worker session (Session 03)
- Report justification: `new-mutation`
- Authority expiry statement
- `Logical-whole closure: not-closed`

Authority expires at the terminal report.

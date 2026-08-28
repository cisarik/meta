### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ap-default-agent-dispatch-and-pin-presentation
Worker session ordinal: 01
Worker exchange ordinal: 01
```

```text
Standard terminal status: PASS
Phase-qualified result: not-applicable
Start commit: 86ae6e8c27d2b919d776021bee915b7292908b0e
End commit: 86ae6e8c27d2b919d776021bee915b7292908b0e
Changed files: none
Tests and validation: reading inventory and repository gate verification
Commit and push: not-used
Deviations / risks: none
Smallest next step: Cooperator review and acceptance of this implementation plan, followed by an authoritative implementation prompt targeting a fresh Worker session
Report justification: new-evidence
Authority expiry: all authority granted by prompt AP-DEFAULT-DISPATCH-AND-PIN-PRESENTATION-PLAN-01 expires at this terminal planning report
Logical-whole closure: not-closed
```

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

```text
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

---

## 1. Inventory Coverage of Observations §6 Surfaces

Every cited surface was read and verified at exact commit `86ae6e8c27d2b919d776021bee915b7292908b0e` (AP) and `85028f725537adcf922f2587d62f1bad68cd5924` (FrameNest):

1. `/home/agile/Projects/ap/AP.md` (`86ae6e8c…`):
   - §2 Roles (three persistent roles invariant)
   - §3 Capability profiles and dispatch (Agent Orchestrator vs Read-Only Orchestrator; Worker session target)
   - RF-02 (Orchestrator decision, reconciliation, direct action, presentation emission duty)
   - RF-05 (Fresh/current routing, parent-context subagent disqualifier for independent acceptance)
   - RF-06 (Capability, reasoning, permission, containment, and authority separation)
   - RF-15 (Protocol variants, stable integration, consumer compatibility)
   - RF-19 (External analytic trace, exchange coordinates, prompt/report pair archival)
   - §17 Compact communication
   - §19 Anti-patterns (emoji as authority, tool-task swarms, parent-context independent audit)
2. `/home/agile/Projects/ap/AP_ORCHESTRATOR.md` (`86ae6e8c…`):
   - Continuation Bootstrap
   - Operating Responsibility & Decision Table ("Dispatch and direct action")
   - Capability Profiles, Dispatch, and Direct Action
   - Worker Exchange Coordinates and Optional Trace
3. `/home/agile/Projects/ap/AP_WORKER.md` (`86ae6e8c…`):
   - Role and Authority Boundary
   - Worker Session Target & Independence
   - Worker Exchange Coordinates and Trace Boundary
4. `/home/agile/Projects/ap/PROMPT_CONTRACTS.md` (`86ae6e8c…`):
   - Worker Report Header & Exchange Coordinates
   - Standard Markdown/Git Exchange Projection
   - Cooperator Delivery and Trace Destination Record
   - Session-And-Mode Routing Contract
   - Common Worker Task Fields
   - Upgrade Observation Ledger Contract
5. `/home/agile/Projects/ap/PROMPT_ENGINEERING_PATTERNS.md` (`86ae6e8c…`):
   - P01, P02, P03, P04, P06, P11, P14 (Model Rotation and Evidence Equivalence), P16, P19
6. `/home/agile/Projects/ap/INTEGRATION.md` (`86ae6e8c…`):
   - Managed `AGENTS.md` Block
   - Optional Presentation Profile, Development Envelope, and Trace Grammar
7. `/home/agile/Projects/ap/UPDATING.md` (`86ae6e8c…`):
   - Apply an Update & Review Checklist
8. `/home/agile/Projects/ap/INTUITION.md` (`86ae6e8c…`):
   - §4 Subagent Dispatch as Worker Delivery, §7 Optional Signaling, §8 Failure Quick List
9. `/home/agile/Projects/ap/docs/adr/` (`86ae6e8c…`):
   - `0017-cooperator-ergonomics-cost-proportional-execution.md`
   - `0018-consumer-declared-execution-route-binding.md`
   - `0019-subagent-delivery-of-worker-sessions-and-orchestrator-capability-profiles.md`
   - `0021-followable-spine-and-restatement-conversion.md`
10. Consumer & Meta inspect-only evidence:
    - `/home/agile/Projects/framenest/AGENTS.md` (`85028f7…`)
    - `/home/agile/Projects/framenest/docs/AP_UPGRADE_OBSERVATIONS.md` (`85028f7…`)
    - `/home/agile/meta/projects/framenest/09/00-framenest-ap-field-test/02_field_observations.md`
    - `/home/agile/meta/projects/framenest/09/00-framenest-ap-field-test/02_closure.md`

---

## 2. Recommended Design for Observations A, B, and C

### Observation A — Agent Orchestrator Default Dispatch & Model Opt-Out (P14)
- **Protocol Semantic Owner (`AP.md`)**:
  - `AP.md` §3 ("Orchestrator capability profile"): Define that an **Agent Orchestrator** defaults to delivering one complete authoritative Worker prompt into one concrete session (dispatch / subagent) **unless** the Cooperator explicitly opts out.
  - `AP.md` RF-02 ("Orchestrator decision, reconciliation, and closure authority"): Embed the default dispatch delivery rule into Orchestrator routing duties.
  - `AP.md` RF-05 ("Fresh/current routing and independent acceptance"): Reaffirm that a parent-context subagent cannot provide independent acceptance; default dispatch applies to ordinary non-independent Worker sessions.
  - `AP.md` RF-06 ("Capability, reasoning, permission, containment, and authority"): Clarify that dispatch capability remains a delivery mechanism and never expands authority.
- **Model Opt-Out (P14)**:
  - *One-sentence definition*: When the Cooperator selects a different model or execution client, or explicitly indicates intent to act as the messenger, copy-paste prompt delivery is the lawful selected route under P14 model rotation rather than a protocol failure.
- **Projections**:
  - `AP_ORCHESTRATOR.md`: Update "Capability Profiles, Dispatch, and Direct Action" and the Decision Table to mandate default dispatch for Agent Orchestrator unless opted out.
  - `AP_WORKER.md`: Reaffirm that a dispatched session is an ordinary Worker session receiving one complete prompt.
  - `PROMPT_CONTRACTS.md`: Update Session-and-Mode Routing guidance notes for default dispatch vs manual opt-out.
  - `INTUITION.md`: Update §4 to reflect the default-dispatch rule.
- **ADR-0021 Detectability**:
  - Detection surface: Orchestrator prompt-delivery interaction with Cooperator and delivery route recorded in `00_notes.md` / trace metadata.
  - Detectability class: Behavioral-normative (Class 2), with artifact-detectable traces in `00_notes.md` and issued trace files.

### Observation B — Trace Companion Archival & Companion Integrity Check
- **Protocol Semantic Owner (`AP.md`)**:
  - `AP.md` RF-19 ("External analytic trace and Worker exchange identity"):
    1. When dispatch is default, the Orchestrator receives the terminal report directly in-session and **must** archive the exact prompt + actual outcome pair into the activated trace after the report exists.
    2. The Worker remains strictly prohibited from self-archiving or granting itself trace writes.
    3. When copy-paste opt-out is used, the Orchestrator archives the pair upon receiving the report from the Cooperator.
    4. **Companion Integrity Invariant**: A companion named `*_report_*.md` must be a valid terminal report (commencing with `### Report for ORCHESTRATOR_CHAT` and containing the compact core) and must **not** be byte-identical or content-identical to the prompt. An archived companion identical to the prompt is invalid and must be rejected before reconciliation or closure.
  - `AP.md` RF-02: Orchestrator-direct action includes archiving the pair and validating companion integrity.
- **Projections**:
  - `PROMPT_CONTRACTS.md`: Add the companion integrity requirement to "Standard Markdown/Git Exchange Projection" and "Cooperator Delivery and Trace Destination Record".
  - `AP_ORCHESTRATOR.md`: Detail Orchestrator trace archival obligations and the companion-integrity verification step in "Worker Exchange Coordinates and Optional Trace".
  - `AP_WORKER.md`: Reaffirm in "Worker Exchange Coordinates and Trace Boundary" that the Worker does not self-archive.
- **ADR-0021 Detectability**:
  - Detection surface: Trace directory / Git commit containing the prompt and companion (`cmp -s <prompt> <companion>` fails if identical).
  - Detectability class: Artifact-detectable (Class 1).

### Observation C — Pin-Time Discoverability of Optional Consumer Presentation Profile
- **Protocol Semantic Owner (`AP.md`)**:
  - `AP.md` RF-15 ("Protocol variants and stable integration"): Operational pin-update guides must make optional consumer `AGENTS.md` declarations (presentation profile, development envelope, upgrade ledger) discoverable at pin time without relying on reference-on-demand `INTUITION.md`.
  - `AP.md` RF-02 / §3 / §17 / §19: Maintain that presentation marks are project-owned, optional, and emitted after the copyable English prompt when activated in consumer `AGENTS.md`.
- **Projections**:
  - `UPDATING.md`: Add a dedicated item to the Review Checklist.
  - `INTEGRATION.md`: Provide an explicit non-normative project-owned example capsule showing status marks (🟢🟡🔴) and dispatch preferences, clearly labelled as not AP semantics.
- **ADR-0021 Detectability**:
  - Detection surface: `UPDATING.md` Review Checklist in AP; consumer `AGENTS.md` outside the managed block; Orchestrator output to Cooperator.
  - Detectability class: Artifact-detectable (Class 1) for checklist & `AGENTS.md`; Behavioral-normative (Class 2) for chat emission.

---

## 3. Pin-Time Hook Sketch & Primary Hook Selection

### Primary Hook Selection: `UPDATING.md` Review Checklist
- **Primary Hook**: `UPDATING.md` Review Checklist (+ referenced example in `INTEGRATION.md`).
- **Rationale**:
  1. `ap init` strictly creates/refreshes only the canonical block bounded by `<!-- BEGIN MANAGED AP INTEGRATION -->` and `<!-- END MANAGED AP INTEGRATION -->`. Modifying `ap init` to template project-owned text outside the block would violate the managed-block separation and hardcode non-universal presentation assumptions into executable code.
  2. `UPDATING.md` Review Checklist is the mandatory operational gate executed whenever a consuming project adopts a new AP pin.
  3. Placing the check in `UPDATING.md` ensures immediate discoverability for any spine-following Orchestrator performing a pin update, without requiring `INTUITION.md`.

### `UPDATING.md` Review Checklist Addition
```markdown
- verify or refresh optional project-owned declarations in `AGENTS.md` outside the managed block, such as a Cooperator presentation profile (e.g. status marks 🟢🟡🔴, delivery capsule), development envelope, or upgrade ledger if the project uses them;
```

### `INTEGRATION.md` Capsule Example Sketch
```markdown
### Project-Owned Presentation Profile Example
A consuming project may declare a presentation profile in root `AGENTS.md` outside the managed AP block:

```text
# Project-owned presentation example only. Not AP semantics. Not Worker authority.
Status: 🟢 healthy / proceed | 🟡 wait / open decision | 🔴 stop / BLOCKED
Route: Agent Orchestrator default dispatch
Reasoning: Medium
Downloadable prompt filename: 02_implementation_00.md
Activated-trace destination: <project-local path>
Archival: wait-for-report
```
```

*Note: FrameNest's `AGENTS.md` presentation profile commit is explicitly excluded from this AP logical whole and scheduled as a follow-on consumer whole.*

---

## 4. Anti-Goals

1. **No Fourth Persistent Role**: COOPERATOR, ORCHESTRATOR, and WORKER remain the sole persistent roles. Agent Orchestrator is a capability profile, not a role.
2. **No Emoji as AP Fields**: Emoji and localized capsules remain project-owned presentation outside universal AP fields and never constitute task authority.
3. **No Treating Dispatch Capability as Task Authority**: Ambient tool capability never expands authority; prompt boundaries strictly govern.
4. **No Parent-Context Subagents as Independent Audits**: Vendor-neutral functional test (fresh session, prompt-only initial context, zero parent reasoning, own report) remains mandatory for independent acceptance under RF-05.
5. **No Silent Doctor Enforcement or Mechanical Prompt Parsers**: Executable `ap` does not validate prompt prose; rules remain normative and operational per ADR-0015.

---

## 5. Next-Prompt Implementation Envelope

- **Target Repository**: `https://github.com/cisarik/ap.git` at `86ae6e8c27d2b919d776021bee915b7292908b0e`.
- **Changed-Path Allowlist**:
  - `AP.md`
  - `AP_ORCHESTRATOR.md`
  - `AP_WORKER.md`
  - `PROMPT_CONTRACTS.md`
  - `PROMPT_ENGINEERING_PATTERNS.md`
  - `INTEGRATION.md`
  - `UPDATING.md`
  - `INTUITION.md`
  - `GLOSSARY.md`
  - `CHANGELOG.md`
  - `docs/adr/0022-default-agent-dispatch-trace-integrity-and-pin-presentation.md`
- **Excluded Paths**: `ap` executable, `/home/agile/Projects/framenest/*`, `/home/agile/meta/*`.
- **Working-Copy Topology**: `canonical-checkout` (clean standalone AP checkout).
- **Evidence Tier**: `E1` (bounded, reversible documentation/protocol specification).
- **Independent Acceptance**: `required-separate-fresh-worker` because the candidate mutates the sole normative protocol (`AP.md`) and structural projections (`PROMPT_CONTRACTS.md`), triggering mandatory fresh independent acceptance under AP finite convergence and ADR-0015/ADR-0021.
- **Migration Impact**: None. Absence of consumer presentation overlay remains valid compatibility behavior.

---

## 6. Residual Risk Analysis

- **Scenario**: A fresh Orchestrator reads only the per-role spine (AP.md, AP_ORCHESTRATOR.md, PROMPT_CONTRACTS.md) in a consuming project that did **not** declare an optional presentation overlay.
- **Outcome Under This Design**: The Orchestrator reads AP.md §3 / RF-02 / AP_ORCHESTRATOR.md and **still executes the dispatch default** because the Agent-Orchestrator dispatch default is a universal protocol rule on the spine, not dependent on consumer `AGENTS.md` presentation text. The absence of consumer overlay simply means no localized emoji capsule is prepended; dispatch functionality operates with 100% fidelity.

---

## 7. Smallest Next Step

Upon Cooperator approval of this plan, the Orchestrator issues a complete implementation prompt with:
- `Native planning mode: not-used`
- `Worker session target: fresh-worker-session`
- `Worker session profile: Fresh Implementation Worker`
- `Exact baseline: 86ae6e8c27d2b919d776021bee915b7292908b0e`
- Allowlist restricted to AP documentation files and new ADR-0022 as listed above.

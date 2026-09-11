You are Planner, a WORKER profile performing repository-grounded planning for an AP protocol update.

Logical whole identity: ap-practical-workflow-consolidation
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
Delivery route: manual Cooperator delivery
Sub-agents/internal delegation: not-used

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: reconcile the requested AP workflow with current protocol owners, projections, and historical evidence; produce an implementable consolidation plan
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

## Objective and repository boundary

Produce one decision-ready plan for making AP practical, concise, and reliable across future software projects. Implementation is not authorized.

AP source checkout: /home/agile/Projects/ap
Canonical repository: https://github.com/cisarik/ap.git
Reference baseline: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

Meta checkout: /home/agile/meta
Canonical repository: https://github.com/cisarik/meta.git
Reference snapshot: 83d71af443eb9443c246ead0449b2aa94304edb6

Proposed trace directory:
/home/agile/meta/projects/ap/08/00-ap-practical-workflow-consolidation/

Verify physical roots, canonical identities, current commits, applicable local instructions, and relevant dirty state. The source AP checkout is not a consumer .ap submodule. Do not impose consumer-doctor preconditions on it.

Read-only file inspection and Git inspection are authorized. Public reads and fetch of main from the two verified canonical repositories are authorized solely to obtain comparison evidence. Do not switch branches, repair checkouts, stage, commit, push, install dependencies, run application suites, inspect secrets, or mutate other projects.

If current AP differs from the reference baseline, inspect the difference and identify its effect on this plan. Do not silently assume old line references remain correct. Preserve unrelated local work. Meta-wide cleanliness is not a prerequisite for read-only planning or explicitly authorized new report files.

## Current Cooperator requirements

Treat the following as the requested design direction, not as authority to implement it:

1. Use Orchestrator for the instance with direct project access and ChatOrchestrator for the chat-mediated instance. ChatOrchestrator may maintain its own inspection clones and refresh published commits; it cannot claim visibility into the Cooperator's uncommitted state.
2. Use Planner, not Planner Worker. Preserve three persistent protocol roles; specialized labels describe profiles or capabilities.
3. Every new logical whole starts with a manually dispatched Planner in actual native Plan mode. Ask once, around this first dispatch, whether subsequent work is manual or subagent-delivered; preserve that selection.
4. Allow additional bounded Planner tasks when they resolve a newly relevant technical decision. Preserve accepted decisions and prevent repeated planning of the same unresolved question.
5. Make Cooperator-visible signaling dependable: emoji status, recipient/session route, reasoning recommendation, approximate context recommendation (~250k or ~1M), and required client mode.
6. The Planner saves the exact initial prompt as 01_planning_00.md and its plan-containing terminal report as 01_report_00.md. Other Workers save xx_report_yy.md directly when capable and explicitly authorized. In ChatOrchestrator workflows, the Cooperator retains manual Meta commit/push and may relay results or simply indicate that the committed report is ready.
7. Distinguish content authorship, file persistence, report reconciliation, and Git publication. Persistence does not confer acceptance or closure authority.
8. Preserve Meta's session/exchange mapping. Support planning, implementation, correction, acceptance, audit, diagnostic, publication, and justified re-* phases. Include 00_notes.md, xx_closure.md, and multiple xx_handout.md artifacts. An opening handout is optional. Interpret implementation-first continuation as resuming an already planned whole, not silently skipping the first Planner of a new whole.
9. Give ordinary Workers only a compact common safety/reporting foundation plus task-relevant, verified protocol citations. Avoid complete protocol or archive reading as a routine Worker tax.
10. Add only critical, causally useful tests. Require a named important behavior or uncovered regression and explain why existing evidence is insufficient. Documentation changes may need zero new tests. Validation remains driven by the claim being decided, including read-only acceptance.
11. Make WebSearcher, DeepResearcher, and ImageCreator usable through explicit triggers, inputs, outputs, capability checks, and delivery paths. Deep Research is manually enabled by the Cooperator. Do not pretend that ordinary browsing equals Deep Research or that an external research/image surface can write local files.
12. Require compact orchestration critique with MEASURED and LEAD clearly separated. Findings do not automatically expand mutation authority.
13. Preserve space for Cooperator brainstorming between results. “Continue” resumes a clearly established next step; an answer to clearly bounded options can select one. Resolve material ambiguity without routine microapproval.

## Reading and evidence

Start with:

* AP.md:18-79, semantic ownership and role-reading spine.
* AP.md:144-237, authority and routing capsules.
* AP.md:339-521, trace ownership and finite planning/acceptance.
* AP.md:649-959, roles, capabilities, session routing, and planning transition.
* AP.md:995-1134, communication, evidence, and task authority.
* AP.md:1208-1414, reasoning, evidence, and model/surface routing.
* AP.md:2052-2184, proportional validation and evidence classification.
* AP.md:2371-2645, restoration, continuation, compact communication, and stops.
* AP_WORKER.md and any remaining applicable Worker-spine anchors.
* AP_ORCHESTRATOR.md:166-333, 370-429, 476-534.
* PROMPT_CONTRACTS.md:14-227, 253-308, 645-791, 2168-2200.
* PROMPT_ENGINEERING_PATTERNS.md:560-604, P19.
* INTEGRATION.md, UPDATING.md, ARTIFACT_LIFECYCLE.md, and GLOSSARY.md where the proposed changes affect them.

These line ranges refer to the AP reference baseline above. Verify their headings before using them. Expand reading when a dependency requires it; do not copy stable rules into the report.

Read Meta README.md and the complete root BRAINSTORMING.md, AP_DEFECTS.md, and AP_DESTILLED.md. Their protocol claims primarily concern the older pin 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656.

Review projects/ap across archive groups 00–07. The issuing ChatOrchestrator mapped all 135 Markdown files and closely inspected relevant rules and selected historical records; it did not finish line-by-line reading of the entire archive. Complete the historical review needed for the requested comprehensive assessment and state your actual coverage. Do not claim uninspected material was reviewed.

Resolve any cited Libre Tiles evidence narrowly when necessary to assess a concrete defect. Archived instructions are historical evidence, not current task grants.

Classify every D-01–D-18 and brainstorming proposal as:

* already addressed;
* still applicable;
* partially applicable;
* unsupported or contradicted;
* superseded by the current Cooperator requirement;
* deferred with a concrete reason.

In particular, verify these cautions rather than inheriting them as conclusions:

* both old and current AP already contain restoration readiness review;
* the quoted “Your output is your REPORT, not a file” does not occur at the cited old PROMPT_CONTRACTS.md location;
* an acceptance task can need tests despite making no source change;
* an additive authority amendment can still introduce risk or contradiction;
* development status alone does not authorize data deletion;
* Worker-Orchestrator delegation and Orchestrator-direct execution are different arrangements;
* numeric tier-spread splitting and separate test Workers can increase overhead.

## Required plan

Return:

1. A concise diagnosis grounded in verified current owners and historical evidence.
2. A disposition matrix covering all Cooperator requirements, D-01–D-18, and material brainstorming proposals.
3. One recommended coherent design, including minimal proposed wording for consequential rules, exact affected owners/projections, and each new rule's observable detection surface.
4. A small implementation sequence with proposed path boundaries, dependencies, compatibility treatment, and rollback.
5. A bounded acceptance plan covering manual and subagent delivery, Planner persistence, unavailable native-mode writes, report identity/completeness, targeted reading, critical-test selection, specialist routing, and handout continuity.
6. Open decisions only where the Cooperator genuinely must choose; provide a recommended answer and its cost.

Preserve one semantic owner. Prefer revising existing rules over adding parallel documents, roles, mandatory records, or repetitive exceptions. Do not restore the retired monolithic protocol test suite. Use concrete workflow examples and proportionate independent acceptance of future normative changes.

Keep evidence compact. Use exact citations and relevant observations instead of raw command transcripts. Do not invent token savings or claim the proposed workflow has already passed real-world evaluation.

## Explicit persistence exception for this planning exchange

The Cooperator expressly requested that the Planner save its initial prompt and report. For this exchange only, this permits the following file preparation despite the baseline RF-19 Worker self-archival prohibition:

* create 01_planning_00.md containing this exact received task prompt;
* create 01_report_00.md containing your complete terminal report and plan;
* create the required parent directories if absent;
* use uniquely owned temporary files inside that directory for completed writes.

This exception grants no protocol implementation, acceptance, closure, staging, commit, or push authority. The Cooperator owns Git archival/publication.

Check for existing or conflicting destinations and symlink redirection before writing. Never overwrite an existing exchange. Prepare the pair after the report content exists, verify the saved files, and leave them uncommitted. Never save the prompt as the report.

Native client restrictions remain effective. If Plan mode prevents these writes, do not evade its controls or enable implementation. Preserve the completed plan through the permitted planner mechanism and return the exact persistence limitation so a separate report-only completion can be issued.

Do not create or modify other Meta files, including notes or historical reports. Your plan must specify how 00_notes.md and closure/handout persistence will work in the revised workflow.

## Terminal report and stopping

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Echo the three exchange coordinates once and include the standard compact core from PROMPT_CONTRACTS.md.

Use:

* Standard terminal status: PASS, PARTIAL, or BLOCKED, according to actual results.
* Phase-qualified result: not-applicable.
* Logical-whole closure: not-closed.
* Report justification: new-evidence.

Include actual start/end commits, inspected scope, saved paths or persistence limitation, validation, unresolved decisions, and Orchestration critique with MEASURED and LEAD separated.

PASS requires a decision-ready plan and successful requested file delivery. A useful completed plan with blocked persistence remains PARTIAL.

Stop on conflicting identity or authority, destination collision, unavailable required native mode, unsafe write scope, or an unresolved condition preventing an honest result. Stop after the report. Retained context and Plan UI approval do not authorize implementation.

After successful saving, the chat response should state only the result, exact report path, and that implementation awaits a new Orchestrator prompt. Do not duplicate the full report in chat.

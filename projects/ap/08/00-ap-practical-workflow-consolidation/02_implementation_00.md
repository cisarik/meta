You are a WORKER implementing the accepted AP practical-workflow consolidation in the same healthy session that produced the planning report.

Logical whole identity: ap-practical-workflow-consolidation
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Worker session profile: bounded implementation
Implementation authority: explicit
Native planning mode: not-used
Independence required: no
Reasoning recommendation: High
Recommended context capacity: approximately 250k tokens
Delivery route: manual Cooperator delivery
Sub-agents/internal delegation: not-used
Evidence tier: E2

High is appropriate for the interacting authority, routing, persistence, and compatibility changes. Context capacity is a recommendation, not observed telemetry.

**Continuity and accepted decision**

Continuity anchor: your planning exchange 01/01 and its complete terminal report at:

/home/agile/meta/projects/ap/08/00-ap-practical-workflow-consolidation/01_report_00.md

The planning grant expired at its terminal report. This prompt grants complete new bounded implementation authority. Retained understanding is useful because the objective and AP baseline remain unchanged; retained context is convenience, not authority. Your implementation evidence is non-independent.

Verify that this is the actual intended session and that no intervening authorized exchange consumed these coordinates. If continuity fails, stop; do not silently create or relabel a fresh session. Re-gate repositories and environment before mutation. Native Plan mode must actually be off; do not bypass client restrictions.

The ChatOrchestrator accepts the plan in sections 2–5 of that report, with this explicit correction:

Handouts may be authored by an Orchestrator, an explicitly assigned Worker, or the Cooperator. Preserve truthful authorship, evidence limits, predecessor relationships, and Orchestrator reconciliation. The shared handout/closure artifact numbering is separate from Worker-session numbering; its name must not falsely imply exclusive Orchestrator authorship. A Worker handout requires its own bounded authorization and does not replace the standard terminal Worker report. Notes remain Orchestrator-authored; a named persister may store their exact supplied content.

This corrects the restriction in plan section 3.F. It does not authorize a handout in this exchange.

**Immutable evidence and repository gate**

AP source checkout: /home/agile/Projects/ap
Canonical repository: https://github.com/cisarik/ap.git
Repository checkout topology: standalone source checkout
Expected starting branch: main
Exact baseline: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

Meta checkout: /home/agile/meta
Canonical repository: https://github.com/cisarik/meta.git
Verified reference snapshot: 5722d1a058255af883686ce3c37779e160bbbbc7

At that Meta snapshot:

* The planning report SHA-256 is 2572eaac2c5514186d2cb65ce1b64dc533b5104563514cfd5bacce55547e38bf.
* Root README.md SHA-256 is 5c6336607777fced6ea79f250efe902db3603e5b074f2f1d96ad8e0617b6d458.

The report is now correctly persisted. Its historical PARTIAL describes the Planner's inability to write at that time. Its section 6 persistence-repair instructions are historical and must not be executed. Do not rewrite the report or its status. The earlier incorrect report and non-atomic first archival remain historical facts, not defects to conceal.

Verify physical roots, canonical remotes, branches, HEADs, applicable local instructions, relevant tracked/untracked changes, and absence of active Git operations. AP must match the exact baseline with an empty index and clean implementation targets. Preserve unrelated local files; stop only when they conflict with safe execution or candidate isolation.

A newer Meta descendant is acceptable if the accepted report and starting README still match the hashes above and required artifact destinations are compatible. Unrelated Meta dirty state is not a blanket blocker.

This AP checkout is not a consumer .ap submodule. Inspect applicable project routes; ap.project.conf at the pinned baseline supplies runtime information, not a documentation-validation operation. Do not impose consumer-doctor gates or provision an environment for this documentation task.

**Focused reading**

Use the pinned AP as governing protocol, subject to this prompt's explicit Cooperator-directed transition exception below. The candidate you edit cannot grant itself authority.

Verify headings at the pinned baseline:

* AP.md:18–79, semantic ownership and the existing role-reading spine.
* AP.md RF-03, RF-05, RF-06, RF-12, RF-18, RF-19; §8 Worker Responsibilities; §18 Stopping Conditions.
* PROMPT_CONTRACTS.md:14–83, Worker Report Header; 156–178, Implementation Authority Record; 339–378, Worker Session Target Contract.
* AP_WORKER.md, Worker Session Target and reporting requirements.
* The accepted report's sections 2–5 and current Meta README.md.

Existing session reading may be reused after checking the baseline. Inspect each implementation target before editing; follow the accepted plan's owner/projection map and relevant dependencies. Line numbers are locators: verify the heading and pin, and relocate moved headings instead of guessing. Do not repeat the completed archive investigation or another planning cycle.

**Implementation outcome and exact allowlist**

Produce one coherent documentation candidate implementing the accepted plan. AP.md remains the sole semantic owner; PROMPT_CONTRACTS.md owns exact structural spellings; Meta README.md owns only its local storage convention.

Changed-path allowlist, relative to the AP root:

AP.md
PROMPT_CONTRACTS.md
AP_ORCHESTRATOR.md
AP_WORKER.md
ARTIFACT_LIFECYCLE.md
PROMPT_ENGINEERING_PATTERNS.md
INTEGRATION.md
UPDATING.md
GLOSSARY.md
FAQ.md
INTUITION.md
README.md
CHANGELOG.md
docs/adr/README.md
docs/adr/0023-practical-workflow-consolidation.md

Additional protocol implementation target:
/home/agile/meta/README.md

Implement owners first, then contracts, projections/examples, Meta convention, and ADR/index/changelog. Resolve contradictory current guidance within this allowlist. Do not publish a half-converted candidate.

Cover all thirteen accepted requirements and the disposition decisions, including:

* Orchestrator/ChatOrchestrator access profiles and honest observation boundaries;
* mandatory first manual native Planner, preserved subsequent delivery choice, and bounded additional planning without budget resets;
* visible delivery information, reasoning/context recommendations, and actual client mode;
* separately authorized authorship, persistence, reconciliation, and Git operations;
* correct report identity, interruption separation, native-mode persistence recovery without replanning, and historical compatibility;
* compact task-relevant Worker reading, causal validation, functional specialist routing, handout continuity, and MEASURED/LEAD critique.

Preserve the standard report header, terminal statuses, exchange coordinates, and distinction between universal exchange semantics and Meta filenames. Apply the handout-authorship correction above consistently.

Give each materially changed normative obligation its appropriate existing detection class and observable surface. Keep projections concise. Add no parallel protocol manual, workflow register, mandatory overhead record, or executable validator.

ADR 0023 records the accepted design, rationale, alternatives, and partial supersession of earlier decisions. Distinguish acceptance of an architectural decision from independent acceptance of this candidate, publication, and closure. Do not rewrite older ADR bodies.

**Implementation boundaries and Git authority**

Authorized: targeted inspection/search, bounded edits to the named files, proportional documentation checks, and the following local AP candidate preparation.

After the AP gate passes, create and switch to the new local branch:
feat/ap-practical-workflow-consolidation

If that branch already exists, stop and report its identity rather than resetting or silently reusing it. Stage only the authorized AP changes using explicit paths. Create one coherent local commit after validation. Verify its parent, changed paths, and remaining worktree/index state.

No AP push, merge, reset, amend, history rewrite, stash, or destructive cleanup is authorized. Meta staging, commits, and pushes belong to the Cooperator and are not authorized for you.

No changes to the executable ap, ap.project.conf, managed block, schema, CI, tests, consumer pins, other projects, historical reports, or data. No dependency installation, runtime provisioning, application suites, secrets, browser activity, provider calls, or external communications.

Public reads/fetches of the two verified canonical repositories are allowed for provenance only. Stop on a material baseline conflict or required out-of-scope change; report the smallest concrete missing authority without improvising.

The candidate consists of the local AP commit plus the exact uncommitted Meta README content. Independent acceptance and publication are separate future grants.

**Explicit trace-persistence transition exception**

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/ap/08/00-ap-practical-workflow-consolidation/
Trace project key: ap
Trace logical-whole projection identity: 08/00-ap-practical-workflow-consolidation
Trace authority: historical-evidence-only
Trace archival owner: Cooperator
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /home/agile/meta/projects/ap/08/00-ap-practical-workflow-consolidation/
Report filename: 01_report_01.md
Prompt persistence owner: this Worker, exact received content only
Report persistence owner: this Worker
Git publication owner: Cooperator
Archival: wait-for-report

For this exchange, the Cooperator-directed workflow explicitly permits file preparation despite the baseline Worker self-archival restriction. This exception also permits mechanical persistence of the exact ChatOrchestrator-authored notes entry below. It grants no reconciliation, acceptance, publication, or closure authority and does not override client controls.

Additional exact write destinations in the trace directory:

* 01_implementation_01.md — this complete received prompt, unchanged;
* 01_report_01.md — your complete actual terminal report;
* 00_notes.md — the exact supplied entry below only.

Verify physical destinations and symlinks before writing. Reuse an already prepared byte-identical prompt after verification. Do not overwrite a conflicting prompt or existing terminal report. A conflicting destination blocks that write; preserve useful results in the permitted response.

If notes are absent, create them with the supplied entry. If valid notes for this whole exist, preserve them and append the entry once only; do not duplicate or rewrite it. Other notes content is not yours to author.

Exact notes entry:

## 2026-09-11 — Planning reconciliation and implementation dispatch

Author: ChatOrchestrator. Persisted mechanically by the assigned Worker.

The Cooperator selected manual delivery for subsequent work in this logical whole. AP baseline: 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26. The complete planning report at 01_report_00.md was verified in Meta commit 5722d1a058255af883686ce3c37779e160bbbbc7. Its historical PARTIAL and the earlier incorrect report/first-archival mismatch remain preserved; current persistence resolves the delivery gap without replanning or retrospective status changes.

The plan is accepted for implementation with one correction: handouts may be authored by an Orchestrator, an explicitly assigned Worker, or the Cooperator. Authorship does not confer acceptance or closure authority.

The current grant is session 01, exchange 02: 01_implementation_01.md and 01_report_01.md. It authorizes a local AP documentation candidate and the bounded Meta changes stated in the prompt. It does not authorize publication. Fresh independent acceptance is the planned next phase and awaits a separate complete prompt.

End of exact notes entry.

Prepare the prompt/report pair after the report content exists, verify saved content and coordinates, then deliver the terminal notification. Any temporary file must be uniquely owned, confined to the authorized trace directory, and removed before completion. Meta remains unstaged by you. Never save this prompt, a handout, or an incomplete native plan as the report.

**Validation and stopping**

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: none
New causal regression: none
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: required-separate-fresh-worker

Perform one focused semantic pass across the complete candidate, covering all thirteen requirements, the owner/projection map, and every acceptance scenario in plan section 5. Include the handout-authorship correction. Report compact coverage and concrete discrepancies; do not create scenario test files.

Check changed Markdown links/anchors, filename examples and coordinate arithmetic, conflicting old rules, candidate path boundaries, and git diff --check in both repositories. Use installed tools; no new test infrastructure. Repeat checks only after relevant changes or failures.

PASS requires a coherent candidate, successful focused validation, the verified local AP commit, and successful authorized artifact delivery. A material missing requirement, failed check, or incomplete delivery must be reported honestly as PARTIAL or BLOCKED.

Stop after your terminal report. Do not begin independent acceptance, publication, another planning task, or closure.

**Terminal report**

Write the report in English, beginning exactly:

### Report for ORCHESTRATOR_CHAT

Echo the three prompt coordinates exactly once. Use the pinned standard compact core, including actual start/end commits, changed files and purposes, validation, Git results, deviations/risks, one smallest next step, one truthful report justification, and authority expiry.

Use implementation-PASS only when implementation passes; otherwise use not-applicable. Logical-whole closure remains not-closed. Use new-mutation as report justification if you made changes, otherwise the applicable truthful value.

Include:

* exact AP candidate commit, parent, branch, and changed paths;
* actual Meta baseline/end HEAD, README SHA-256 and byte count, and concise change summary;
* focused acceptance-scenario coverage and any remaining evidence gap;
* saved artifact paths and content/identity readback;
* confirmation that no push or Meta Git mutation occurred;
* non-independent evidence classification and outstanding fresh acceptance;
* applicable resolved-issue/pre-existing-failure records;
* compact Orchestration critique with MEASURED and LEAD separated; none is valid.

Do not reproduce the whole plan, raw logs, or private reasoning.

After successful saving, reply briefly with status, exact report path, and AP candidate commit. Tell the Cooperator to archive only this exchange's prompt/report pair and notes in Meta, leaving the AP candidate and Meta README candidate for independent acceptance.

# AP — Reliable Execution and Cooperator Experience

Opening handout for a fresh ChatOrchestrator, authored by the preceding ContextDesk ChatOrchestrator at the Cooperator's request on 2026-09-12.

## 1. Initialize the correct role

```text
Capability profile: ChatOrchestrator
Persistent role: ORCHESTRATOR
Restoration readiness: PASS for read-only bootstrap; implementation readiness is not established
Current phase: Discovery / orchestration preparation for a new AP update whole
Working logical-whole identity: ap-update
Selected delivery: manual
Recipient: a new ChatOrchestrator session, not an implementation Worker
Recommended reasoning: High for protocol design, authority, and acceptance decisions
Recommended initial context capacity: approximately 250k tokens with selective reading
Native Plan Mode for this ChatOrchestrator bootstrap: OFF / not-used
Handout destination: /home/agile/meta/projects/ap/08/01-ap-update/00_handout.md
Handout author and downloadable-file persister: preceding ContextDesk ChatOrchestrator
Placement in the Cooperator's META working tree: pending Cooperator transfer
Handout Git persistence owner: COOPERATOR
Handout archival: allow-now, separately from Worker prompt/report pairing
```

You are responsible for moving AP from the findings in `00_discovery.md` to a justified, implemented, independently reviewed improvement. Begin by verifying current sources. This handout transfers intent, evidence, and the recommended route; it grants no repository, host, account, browser, external-service, filesystem, Git, implementation, deployment, or publication mutation authority. Subsequent Worker actions need their own complete bounded grants.

Use the Cooperator's existing directory and working identity unless he explicitly changes them before the first Worker exchange. Do not turn naming into a prerequisite or silently rename an established trace. This is a new whole following a completed AP consolidation, not a restart of that consolidation or of ContextDesk.

## 2. What Michal is asking you to achieve

AP is Michal's long-term foundation for developing software with AI across his projects. Improving it is now his highest priority. He wants to entrust ambitious work to strong models and increasingly capable future models, while receiving professional, functional results and retaining control of meaningful product and risk decisions.

He explicitly prefers **AI-oriented protocol design**. Universal protocol text should optimize unambiguous interpretation and reliable action by Orchestrators and Workers. It need not teach every rule to a human beginner. However, the Cooperator-facing experience must be exceptionally clear, friendly, and efficient. He should not have to debug protocol fields, remember file arithmetic, copy reports into files, or repeatedly authorize an unchanged operation.

The success criterion is better work reaching him with less avoidable effort and fewer errors. A larger protocol, a longer audit, a stronger model label, or a perfectly formatted report is not that result by itself.

Translate his ambition of work “without errors” into observable safeguards: valid task authority, correct artifacts, proportionate behavioral evidence, explicit uncertainty, recoverable failures, and honest completion. Do not promise infallibility or use that aspiration to justify endless reviews. Favor prevention of consequential mistakes and inexpensive recovery from ordinary execution friction.

Communication preferences for this engagement:

- Speak Slovak to Michal, address him in masculine grammatical gender, and use feminine self-reference in Slovak.
- Write Worker prompts/reports and AP/META technical artifacts in English.
- Lead with the result, decision, or concrete next step. Explain material trade-offs without exposing unnecessary protocol machinery.
- Preserve manual Worker delivery. Do not spawn agents or silently switch to automated delegation. A different delivery topology is a material proposal, not an implication of tool availability.
- Use smaller coherent assignments and fresh sessions when context health or independence calls for them. Michal reported repeated compaction in a previous Worker and explicitly rejected accumulating a whole development period in one session.
- High reasoning is appropriate for this protocol work. Do not silently escalate to Extra High. A nominal 1M-token model is an optional capability choice, not the solution to an oversized task; verify client/provider capacity before presenting it as fact.

## 3. Verified anchors and observation limits

| Source | Last directly verified identity | Role in this task |
|---|---|---|
| AP repository | `https://github.com/cisarik/ap` | Universal protocol source; standalone source repository, not a consumer `.ap` checkout |
| AP public `main` | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` | Governing baseline observed while authoring this handout |
| Its parent | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` | Historical baseline of the completed consolidation |
| META repository | `https://github.com/cisarik/meta` | Historical trace; its README owns the local layout |
| META public `main` containing this discovery | `e293f33f7673d6daca70ba88c9e18439130f8886` | Exact discovery readback; parent `d00fa3ba2256c985c3c828ad88ea6ee143d8f57f` |
| Discovery path | `projects/ap/08/01-ap-update/00_discovery.md` | Cooperator-selected input location |
| Discovery SHA-256 | `aceaf2fe5d469d675f41a831d0cbb9056216c2715c258cd786ec4c0cc2739788` | Byte-identical to the supplied `AP_DEFECTS_2.md` |
| ContextDesk evidence candidate | `cb72ae0388307b514182efc6936712e3da42cda4` | Historical reproduction source, not an AP mutation target |

Pinned entrypoints: [governing AP](https://github.com/cisarik/ap/blob/0cf2cff483a36a4cc2254aa424a7c53bd57a97e9/AP.md), [discovery](https://github.com/cisarik/meta/blob/e293f33f7673d6daca70ba88c9e18439130f8886/projects/ap/08/01-ap-update/00_discovery.md), and [predecessor closure](https://github.com/cisarik/meta/blob/e293f33f7673d6daca70ba88c9e18439130f8886/projects/ap/08/00-ap-practical-workflow-consolidation/03_closure.md). These anchor the author's claims; also check current public refs for subsequent changes before issuing work.

Useful local paths for a capable Worker are `/home/agile/Projects/ap` and `/home/agile/meta`. These are user-supplied environment coordinates, not evidence that your ChatOrchestrator has those working directories. Verify topology and remotes before relying on them. An inspection clone proves only its own state and verified public Git objects; it does not prove the Cooperator's uncommitted changes, tool availability, or host state.

The author's AP inspection clone was clean at the observed baseline. No AP implementation or publication was initiated by this author. The inspected new AP trace contained only `00_discovery.md`; no Planner report or AP Worker grant for this new whole was observed. Verify again before allocating coordinates, because work may advance after this handout.

ContextDesk is a separate ongoing project. Its most recently issued task was Worker 14's install-only grant. Its execution/terminal outcome is not reconciled by this handout. Michal intends to return `14_report_00.md` to the originating ContextDesk conversation. You own neither that Worker nor its host mutations. Do not cancel, continue, certify, or modify ContextDesk as an incidental AP task.

## 4. Predecessors, retained decisions, and supersession

Read the following bounded predecessor material:

1. `00_discovery.md` in this directory, including evidence classifications and D2-01 through D2-10.
2. AP `docs/adr/0023-practical-workflow-consolidation.md` at the governing baseline.
3. META `projects/ap/08/00-ap-practical-workflow-consolidation/03_closure.md` for the completed boundary and parked proposals.

The previous consolidation was published at `0cf2cff...` and recorded closed. It already introduced compact reading, explicit artifact preparation, delivery continuity, and several ergonomics changes. Its closure explicitly did **not** claim measured live-client performance or time/token savings. Do not invalidate that historical documentary acceptance merely because later field use exposed weaknesses. The new evidence justifies this new bounded improvement.

The discovery moved from the proposed root filename `AP_DEFECTS_2.md` to the Cooperator's chosen `00_discovery.md`. The bytes are unchanged; its old title and internal references remain historical evidence. This handout supersedes the old **suggested location**, not its findings or the current protocol.

No previous handout for this new whole was observed. This is an opening synthesis, not a continuation of any old Worker authority. It does not adopt the discovery's recommendations as an accepted implementation design.

Preserve these existing architectural decisions until an explicit, justified prospective change is accepted:

- `AP.md` is the sole live semantic owner; `PROMPT_CONTRACTS.md` owns structural spellings; operational, advisory, explanatory, executable, consumer, and historical projections have distinct roles.
- Three persistent roles: COOPERATOR, ORCHESTRATOR, WORKER. Access profile, client capability, task authority, provider permission, and independence are separate dimensions.
- Worker authority is bounded and expires at a terminal report. Retained context and a report-ready notice do not renew it.
- Independent acceptance requires actual separation from material implementation, not a new label or an isolated directory alone.
- Worker report preparation is separate from META add/commit/push. Manual delivery does not require manual report transcription.
- Consumer pins and their historical meaning remain immutable; publication of AP does not update every consumer automatically.

The Cooperator's new AI-oriented emphasis changes the design objective, not the current authority rules. Candidate AP text must not grant itself permission or govern its own review merely because it was edited. Keep the governing revision and the candidate under review distinct until deliberate adoption.

## 5. How to use the discovery without inheriting its mistakes

Read the actual file; do not reconstruct it from this handout. Its main failures were report persistence, unsupported source claims, a wrong file-mode requirement, excessive task scope, a predictable installation blocker, contradictory grants, regression of an accepted recovery route, malformed report metadata, a fragile sudo workflow, and stale product-state guidance.

The preceding Orchestrator caused several of these defects. You must challenge her explanations, priorities, and proposed fixes. In particular:

- An existing correct rule does not prove that its operational presentation is adequate. Repeated noncompliance can expose poor discovery, default composition, excessive distance between a rule and its use, or an impossible combination of clauses.
- An agent's error does not automatically justify another universal AP rule. Some defects belong in a task prompt, a consumer document, a worked example, or tooling outside AP's semantic core.
- A reported pattern is not necessarily independently measured. Preserve conversation-only evidence, Worker observations, verified Git content, and proposed explanations as different classes.
- ContextDesk-specific details such as service modes, watchdogs, keyboard recovery, and Linux privilege are examples. Do not hardcode them into a protocol intended for all projects.

For each D2 item, make a compact disposition in the existing planning/report flow: reproduced evidence; governing owner; likely cause and uncertainty; fix/no-fix rationale; smallest affected projection; and observable validation. Classify it as a semantic defect, projection/usability defect, orchestration application defect, consumer defect, unsupported claim, or a justified combination. Keep its original identifier. Do not create a second permanent defect database.

A valid result may reject or narrow a finding. Do not dismiss all findings with “AP already says this,” and do not accept all of them because they came from another Orchestrator.

## 6. Design challenge: make correct execution the easy path

The following are **design hypotheses to evaluate**, not additional normative rules or a pre-approved architecture.

**Keep the relevant decision local.** At an actual task boundary an agent should be able to determine the goal, current source, permitted effects, required evidence, output owner, and stop condition without resolving a chain of contradictory summaries. Preserve one semantic owner; improve its operational entrypoints instead of copying every rule into every prompt.

**Separate protocol consistency, technical correctness, and user value.** An AP-doctor PASS establishes integration health. A valid report establishes artifact conformance. Neither proves correct software or a useful product. Conversely, a recoverable formatting defect should not cause valid engineering evidence to disappear or force a historical report to be rewritten. Each conclusion needs the right evidence and an honest scope.

**Use a small common contract with task-triggered detail.** Strong models should reason within explicit boundaries rather than execute huge fixed scripts. Structured fields are useful when they remove ambiguity; symbolic compression and extra state machines are not inherently more understandable to models. Keep human auditability of consequential authority even if explanatory prose for beginners is reduced.

**Treat artifact delivery as part of finishing the task.** The useful path is report completed, saved under a positive grant, read back, then terminal notification. Read-only source review can still explicitly permit generated test output and its exact report. An archival owner does not implicitly receive file-write authority, and source-read-only must not accidentally prohibit a required output.

**Design for real failures of context and capability.** Sources may be unavailable; a client may compact; a report may already exist; an owner terminal may have privilege that a Worker lacks. Show the smallest truthful next action within current authority. Do not repair these situations by inventing evidence, forcing a new full audit, changing permissions, or silently widening scope.

**Spend the Cooperator's attention on decisions.** Carry forward selected delivery, accepted scope, and named approvals. Present a recommended route with material trade-offs when a new decision is genuinely needed; complete all safe preparatory work first. Deterministic steps within an accepted envelope should not produce repeated approval requests.

**Prefer eliminating a failure opportunity over adding a reminder.** Consider deleting redundant clauses, consolidating projections, moving a worked example nearer its trigger, or making an existing field sufficient. Add a rule, field, file, or validator only when its distinct benefit and ownership can be demonstrated. Explain which recurrence the change prevents and which cost it introduces.

**Remain capable-model and provider neutral.** Future models may have longer contexts and better tools; neither increases task authority nor proves reliable attention. Capability checks belong at actual boundaries. Avoid permanent model rankings, magic reasoning phrases, unavailable telemetry, mandatory 1M windows, or protocols built around a particular IDE.

You may propose a stronger structural design if it materially improves these outcomes. Provide migration, semantic ownership, and compatibility consequences before asking for its acceptance. This brief neither mandates a full rewrite nor forbids one justified by evidence.

## 7. Validation must show the behavior this update is meant to improve

Use a small fixed set of scenarios that changes in this whole can actually address. The following coverage is the starting proposal, to reconcile with the design and governing protocol. Combine overlapping cases; do not multiply them for ceremony.

| Scenario | Observable correct outcome |
|---|---|
| Manual delivery, source-read-only Worker, report-file write granted | Worker saves and reads back the exact report; Cooperator need not transcribe it; META Git remains separately owned |
| Missing persistence grant or existing report collision | Omission/conflict is surfaced without unauthorized writing or overwriting; the ordinary valid path still finishes without an extra permission loop |
| Cooperator says a report was pushed but the source is unavailable | Orchestrator does not invent its result; identifies the missing source and uses only verified facts for permissible next work |
| Correctly pinned AP, defective task prompt | Integration PASS is not presented as proof of valid authority or executable task design |
| Planned work exceeds a healthy session's scope | Coherent smaller task, useful boundary, and reconstruction from durable evidence; no blind continuation or automatic full-archive reread |
| Required operation contradicts a prohibition or stop rule | The complete prompt is corrected prospectively before execution; no silent interpretation or hidden authority expansion |
| Known prerequisite missing before acceptance | The prerequisite is addressed, or useful review is explicitly scoped around it; no predictable repeat of the same blocked audit |
| Wrong object/property copied from a summary | Expected value is bound to its actual object and source; contradiction does not become a new product requirement |
| Normal owner authentication available, Worker lacks sudo timestamp | Bounded owner-executed operation and truthful readback work without password sharing, sudoers edits, or assumed cross-session privilege |
| BLOCKED/PARTIAL outcome or interrupted client | Correct status/result/header and report persistence or explicit truthful interruption; no forged report, PASS, or hidden retry budget reset |
| Selected one-keyboard recovery or analogous accepted constraint | Later task preserves that choice and distinguishes missing additional evidence instead of silently restoring a rejected prerequisite |
| Independent review and final publication | Reviewer did not materially implement the candidate; exact accepted artifact is published; consumer adoption and closure are explicitly reconciled |

Keep documentary walkthroughs, actual prompt artifacts, client-observed runs, executable tests, and Cooperator usability feedback distinct. A scenario described on paper is not a measured reduction in operational failures. Prompt structure cannot mechanically prove that a model read a rule or acted independently.

Do not ask agents to manufacture near-misses. `none` is valid. Do not demand private chain-of-thought; request concise decisions, assumptions, sources, effects, and uncertainty.

AP deliberately retired a monolithic prose-mirroring test suite. Preserve proportional validation. If a narrowly scoped artifact checker or another executable change is proposed, identify the exact detectable defect it catches, its false-positive risk, and its integration cost. Its implementation requires its own justified scope and behavior tests. Do not recreate a validator that mistakes phrase presence for semantic correctness.

Obtain at least one bounded, genuinely observed use of the changed delivery/finishing workflow if you intend to claim practical improvement. A harmless temporary fixture may be appropriate under an explicit grant. Do not use ContextDesk's live keyboard/host or another project as an unannounced testbed. If only documentary evidence is available, limit the result accordingly and carry practical validation forward explicitly.

## 8. Route from bootstrap to a candidate without another planning loop

First verify AP and META identities and read the new whole's existing artifacts. Use AP_ORCHESTRATOR's Continuation Bootstrap and AP's per-role reading spine. Inspect root AGENTS if present; do not invent one. The AP source repository contains `ap.project.conf`: resolve its applicable declared execution routes before proposing executable operations. A source checkout is not governed by a consumer-submodule topology check.

Initial reading should cover the governing owners for the disputed behavior, AP_ORCHESTRATOR, relevant Prompt Contracts, ADR-0023, this discovery, and the predecessor closure. Follow the evidence links for contested claims. Do not read every project in META or require a cover-to-cover archive as onboarding.

The Cooperator has already selected this new AP improvement objective. Do not ask whether he wants to start. After read-only reconciliation, issue the complete initial Planner prompt if no such exchange exists. At the observed baseline AP requires a manually delivered Planner in actual native Plan Mode. ChatOrchestrator preparation is not a substitute for that first Planner.

The initial Planner's one outcome is a repository-grounded, decision-ready design: disposition all ten findings, identify any causally adjacent gaps, propose the smallest coherent change set and owners, define validation and compatibility, and give bounded implementation slices. It is not authorized to edit AP, implement tooling, publish, or adopt new consumer pins. It must have an explicit positive grant for its exact report-file preparation, compatible with the selected client's native planning restrictions. If the client cannot perform that grant in the actual mode, resolve the capability/completion route honestly before delivery; do not hand the copying burden back to Michal by default.

Do not make a second Planner merely to restate a complete first plan. One initial plan and the governing targeted-revision rules apply. Reconcile the plan, present the recommended design and material trade-offs to Michal, then issue the implementation grant once the relevant design choice is accepted. The general request for improvement is not acceptance of an unseen structural redesign.

Implementation slices should each have one main result. Reuse a healthy planning session when it reduces risk and the task fits; use a fresh Worker after context degradation or for independent review. Do not split trivial text changes into many independent ceremonial exchanges, and do not combine a protocol rewrite, toolchain changes, multiple deployments, and all consumer migrations just because a large window is available.

Changing AP semantics or structural contracts requires independent acceptance of the exact candidate. Do not pass the implementation conversation, private reasoning, or a pre-written verdict to the independent reviewer. Preserve the review inputs needed to understand the fixed scope and evidence. Publication and consumer adoption are separate: freeze the accepted commit, verify its public ref, and never claim every project is updated merely because AP main advanced.

## 9. Artifact ownership and the no-copy/paste requirement

This trace uses META's existing storage grammar, not a new AP universal naming scheme. At the observed empty Worker history, the prospective first pair is:

```text
Directory: /home/agile/meta/projects/ap/08/01-ap-update/
Initial planning prompt: 01_planning_00.md
Initial planning report: 01_report_00.md
AP coordinates for that future grant: session 01, exchange 01
```

These are future routing coordinates, not an issued Worker grant. Revalidate them before issuance. Same-session renewal advances the exchange; a genuinely fresh Worker advances the session. META's suffix is exchange minus one. A phase change does not reset either. Do not impose ContextDesk's session 14 on this new whole.

`00_discovery.md` is historical input, not a Planner report or an accepted plan. `00_handout.md` is this opening synthesis, not a Worker exchange. META also requires an opening `00_notes.md`: the successor authors the initial notes and arranges exact preparation under a bounded grant, using a capable persister when needed. The Cooperator must not have to compose or reconstruct those notes. Notes are not a second protocol or a second task queue.

For each Worker grant that uses this trace:

- Name the exact physical report destination and the assigned Worker as its file persister.
- Positively authorize writing the complete report and verifying saved bytes **before** terminal notification expires the grant, including PARTIAL/BLOCKED outcomes.
- Scope source-read-only and Git prohibitions so they do not conflict with required report or temporary validation writes.
- Verify path identity, symlinks, and collisions; preserve existing reports. A filename or owner label alone is insufficient permission.
- Require the exact first line `### Report for ORCHESTRATOR_CHAT` and one coordinate block; use the governing status and phase-result spellings, and keep informal Slovak notification outside the saved report.
- The Cooperator owns META add/commit/push and after-report pairing. He may report that a committed file is ready; retrieve that exact file before reconciling it.

Do not merely copy this checklist into future prompts. Produce the actual small, internally consistent positive grant for the actual file. A reported save failure is an observable exception; asking Michal to routinely transcribe reports is not the normal completion route.

Retain discovery and this handout as provenance. Promote accepted universal meaning to AP, structure to its structural owner, and implementation rationale to the appropriate historical owner. Do not silently rewrite historical reports or change earlier governing pins. Subsequent handouts/closure use META's handoff sequence and do not consume Worker ordinals.

## 10. Boundaries and material decisions

| Surface | Boundary at this handoff |
|---|---|
| AP source | Read-only restoration now; proposed candidate changes require a bounded Worker grant after design reconciliation |
| META | Existing trace is evidence; this handout does not itself grant future file writes or Git operations |
| Product repositories and hosts | ContextDesk and all other consumers are out of mutation scope; use immutable public examples only |
| Network | Public source verification is relevant; no account changes, external messages, provider purchases, or unbounded research |
| Browser/accounts | No authenticated account or private browser-data access is needed for bootstrap |
| Secrets and credentials | No passwords, tokens, environment dumps, or credential extraction; use normally configured access only for a subsequently authorized operation |
| Git/publication | No AP push, history rewrite, consumer pin update, or META publication is granted by restoration text |
| Active Workers | None observed for this new AP whole; ContextDesk Worker 14 is separately owned and its outcome is not reconciled here |
| Active mutation | No AP mutation initiated by the author; current Cooperator/local/other-session state remains to be revalidated |

Michal owns material protocol redesign, changed delivery/cost/risk choices, publication, and adoption trade-offs. Routine checks and deterministic steps within a valid grant do not need repeat permission. A new rule that primarily reduces the agent's uncertainty by transferring work to Michal deserves particular scrutiny.

Default to preserving executable behavior, the stable integration tuple, managed consumer blocks, and old consumer pins while addressing the discovered contract/usability problems. This is a compatibility default, not a prohibition on a better design. If a change to these surfaces is necessary, state it explicitly with migration and evidence before implementation authority is issued.

If AP's current rules themselves prevent a demonstrably better workflow, propose a prospective amendment through the existing route. Do not quietly stop following the current governing version, use a draft rule as authority, or bypass a tool's approval/security refusal.

## 11. Your first response and eventual finish

After verification, give Michal a brief Slovak synthesis: what is current, what the discovery establishes, what remains uncertain, and your recommended first bounded action. If the verified state still matches this handout, deliver the complete downloadable `01_planning_00.md` with the exact persistence grant, initial routing, and Native Plan Mode **ON for the Planner**. Include the minimal visible delivery capsule. Do not return only a promise, a list of capabilities, another request to start, or a reference to an absent prompt.

Select the initial Planner for protocol semantics and repository-grounded design, with High reasoning and selective context. Approximately 250k is a starting recommendation, not a requirement or provider specification. If a materially larger indivisible task emerges, identify it before recommending a different model/window. Do not perform model-shopping research unless it answers a concrete capability gap.

Finish the whole when the accepted design has a verified candidate, required independent acceptance, explicitly authorized publication with exact readback, and disposition of residual risks, practical-validation limits, and consumer adoption. Report those outcomes separately. The Cooperator should receive a short explanation of the resulting workflow and what he needs to do differently, with any required upgrade command only after the actual integration path is verified.

No automatic claim of error-free AI or globally updated consumers belongs in closure. Leave a reconstructable result in canonical owners, not dependence on your conversation memory. This project succeeds when future agents can perform useful authorized work more reliably and Michal spends his attention on the software he wants.

## 12. Author's readiness review

| Review | Result and scope |
|---|---|
| Source and stale-state review | AP main/parent and exact discovery bytes verified through Git; earlier missing discovery was resolved by a subsequent fetch |
| Predecessor and strategic continuity | Completed consolidation and new Cooperator priorities preserved; discovery recommendations remain proposals |
| Contradiction and omission review | ChatOrchestrator versus Planner mode, new-whole versus old-whole identity, output persistence versus Git, and candidate versus governing AP explicitly distinguished |
| Authority and security review | No inherited mutation/publication authority; no task delegated or host state claimed |
| Active Worker/mutation review | No AP Worker observed; ContextDesk's separately issued Worker 14 has no outcome claimed here; owner's current mutable state requires bootstrap verification |
| Next-step executability | Sources, exact trace destination, expected initial pair, focused Planner outcome, capability and persistence requirements supplied |
| Evidence limits | Documentary handout review only; no AP implementation, independent candidate acceptance, or practical usability improvement claimed |

Readiness is PASS for a fresh ChatOrchestrator to begin the stated read-only bootstrap. It is not a product/protocol acceptance result. This synthesis remains subordinate to current verified sources, governing AP, and explicit Cooperator decisions.

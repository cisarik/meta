# AP_DEFECTS_2 — ContextDesk field-use findings

Artifact: Orchestrator-authored evidence and improvement brief, requested by the Cooperator on 2026-09-12. This is not a Worker report, a live task queue, an AP amendment, or permission to change AP. Preserve the historical prompts and reports cited below.

## Scope and evidence

This brief examines ContextDesk exchanges 12/03 and 13/01 and their surrounding ChatOrchestrator conversation. It distinguishes defects in issued prompts and their application from possible improvements to AP. Existing AP protections must not be described as absent merely because this Orchestrator failed to apply them.

Verified by direct Git fetch/readback for this brief:

| Source | Immutable identity |
|---|---|
| Governing AP; fetched AP `origin/main` | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| ContextDesk candidate; fetched product `origin/main` | `cb72ae0388307b514182efc6936712e3da42cda4` |
| R1 production safety change | `2b6cf2cea5f763aef78be136dd995ad4ac602276` |
| Pre-R1/R2 product baseline | `64dd12bbc34c5ab09574d8edc76ebb7bed50af2d` |
| META snapshot containing both exchanges | `d00fa3ba2256c985c3c828ad88ea6ee143d8f57f` |

The product AP gitlink matches the governing AP. The Cooperator also supplied a local strict-pin `ap doctor: PASS`. That proves integration health at the observed state; it does not prove that every subsequent prompt follows AP. Host installation and test results below are **Worker observations**, not direct observations of the Cooperator's machine by this ChatOrchestrator.

Evidence entrypoints at those pins:

- [AP RF-19](https://github.com/cisarik/ap/blob/0cf2cff483a36a4cc2254aa424a7c53bd57a97e9/AP.md#rf-19-external-analytic-trace-and-worker-exchange-identity): authorship, positive persistence grants, readback, report identity, committed-report retrieval.
- [AP reading spine](https://github.com/cisarik/ap/blob/0cf2cff483a36a4cc2254aa424a7c53bd57a97e9/AP.md#per-role-minimum-reading-spine), [rotation](https://github.com/cisarik/ap/blob/0cf2cff483a36a4cc2254aa424a7c53bd57a97e9/AP.md#14-session-rotation-and-dynamic-prompts), [compact communication](https://github.com/cisarik/ap/blob/0cf2cff483a36a4cc2254aa424a7c53bd57a97e9/AP.md#17-compact-communication).
- [Prompt contracts](https://github.com/cisarik/ap/blob/0cf2cff483a36a4cc2254aa424a7c53bd57a97e9/PROMPT_CONTRACTS.md): Worker Report Header; Acceptance and Correction Record; Cooperator Delivery and Trace Destination Record.
- [Product AGENTS](https://github.com/cisarik/contextdesk/blob/cb72ae0388307b514182efc6936712e3da42cda4/AGENTS.md): Protocol and trace sources; Mutation, Git, and safety.
- [Operations](https://github.com/cisarik/contextdesk/blob/cb72ae0388307b514182efc6936712e3da42cda4/docs/operations.md): sections 6–9, particularly the invocation-bound cutoff and broker installation.
- [META storage contract](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/README.md).
- Trace directory: `projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/` at the META snapshot above. The links below identify individual evidence files; section headings are stable locators, not inferred line numbers.

Prompt identity was checked against the locally issued downloadable artifacts:

| Archived prompt | SHA-256, matching issued bytes |
|---|---|
| `12_implementation_02.md` | `3868961afb4d3d4c2d4b7ba0972fdb1553d0797aca5fa95db3515f7362faca9a` |
| `13_acceptance_00.md` | `0ddc57eb42f6603f85cf10fd7fbf0281bd52897868a30ade63fe4f844c66942a` |

The 13 prompt and report share first-add commit `d00fa3ba2256c985c3c828ad88ea6ee143d8f57f`; the Cooperator preserved Git pairing correctly. D2-01 concerns the unnecessary report-copy step, not a failure to archive the pair together.

Conversation-only evidence is labelled separately. It is not claimed to exist in META. This brief is a focused field-use review, not a certification that every AP projection or every historical exchange was exhaustively audited.

## Findings index

Priority describes the effect observed or plausibly exposed here; it is not a product vulnerability rating.

| ID | Priority | Finding | Primary classification |
|---|---|---|---|
| D2-01 | High | Worker report-file grant omitted; Cooperator became a file-copy courier again | Orchestrator prompt defect; AP usability recurrence |
| D2-02 | High | A report-ready notice was answered from retrieved narrative without reading the report | Orchestrator evidence/provenance failure |
| D2-03 | High | File mode and runtime-directory mode were conflated | Orchestrator factual error, propagated through prompts |
| D2-04 | High | Broad repeated assignments despite observed context pressure | Orchestrator scope/routing failure |
| D2-05 | Medium | Known stale installation was routed into a blocked live-acceptance grant | Sequencing and prerequisite-delivery failure |
| D2-06 | High | Mutually incompatible authority clauses made the acceptance envelope unsatisfiable | Prompt consistency failure |
| D2-07 | Medium | Optional recovery hardware became a condition of completing an oversized acceptance | Prompt scope regression; product documentation lead |
| D2-08 | Medium | Formal report identity and result schema were not preserved | Prompt and output conformance failure |
| D2-09 | Medium | Privilege was treated as a client-wide capability instead of an operation/session property | Prompt workflow defect |
| D2-10 | Medium | Known implementation progress had no bounded durable-document reconciliation | Orchestrator follow-through gap |

## D2-01 — Writing the report was confused with archiving it

**MEASURED.** [13_acceptance_00.md](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/13_acceptance_00.md), “Hard safety boundary,” forbids persistent files and other Git writes. “Terminal report” assigns report persistence to the Worker only “for the exact terminal report; COOPERATOR archives it,” without an exact physical write grant. It also tells the Worker that the Cooperator archives manually. [13_report_00.md](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/13_report_00.md), “Persistence,” explicitly states that no report was written to META. The Cooperator reports having to copy/paste it into a file himself.

**Existing rule.** AP RF-19 already distinguishes Worker authorship and bounded file preparation from Cooperator-owned META add/commit/push. The current product AGENTS explicitly makes the same distinction. Naming an owner or destination alone does not grant a write. Manual prompt delivery does not imply manual report-file creation. [12_report_02.md](https://github.com/cisarik/meta/blob/d00fa3ba2256c985c3c828ad88ea6ee143d8f57f/projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/12_report_02.md), “Persistence,” had already reported successful Worker file preparation under the preceding grant.

**Diagnosis.** The immediate failure belongs to the Orchestrator who issued the deficient grant. The Worker should not be blamed for refusing to invent an exception to a no-write instruction. This is recurrence of the human-courier problem identified as D-17 in the older `AP_DEFECTS.md`, under a pin that already contains its intended remedy.

**Proposed improvement.** Strengthen the existing delivery example with one complete, pasteable positive grant: exact report path, authorized Worker write before terminal notification, physical path/collision checks, content readback, and explicit separation from forbidden META Git operations. Show a valid exception to a source-read-only task. Do not add another permission layer or make META mandatory for all AP consumers.

**Acceptance example.** With manual delivery and the exact file grant, the Worker creates its own report, reads it back, and returns its location and result; the Cooperator only archives the pair with Git. An existing report remains untouched. A missing write grant is detected before execution as a prompt omission, not discovered after the report expires the grant. This Cooperator has now explicitly selected Worker-written report files for future exchanges.

## D2-02 — Narrative was promoted into source evidence

**MEASURED, conversation-only.** Earlier in this chat, public reads failed and a Git read was rejected because automatic approval review could not complete under a usage limit. Subsequent responses still described the result of `12_report_02.md` and prescribed installation as if the exact file had been read. A later personal-context retrieval returned mixed material, including an unrelated media-product direction. That retrieval was not the report. This turn finally read the actual reports through current Git objects.

**Existing rule.** RF-19 explicitly requires retrieving the expected committed report and verifying its identity before reconciliation. AP §14 states that compacted summaries are not current evidence. AP_ORCHESTRATOR “Intent and Evidence Reconciliation” keeps Worker, Cooperator, and direct observations distinct.

**Effect.** An unsupported unit-mode assertion survived multiple turns, while the user received confident status language. A guessed conclusion can coincidentally match part of a later report and still have invalid provenance.

**Proposed improvement.** Put one operational example beside committed-report retrieval: if exact source retrieval fails, say which fact remains unverified; use existing verified anchors for safe work; ask for the exact file only if needed. Do not substitute a memory search for the requested source or bypass an approval failure. Include the source commit/path once in reconciliation instead of adding repetitive evidence fields everywhere.

**Acceptance example.** A “report pushed” message with unavailable report bytes never produces a claimed report verdict. Local AP-doctor evidence is accepted for what it proves without being inflated into whole-workflow compliance.

## D2-03 — `0644` file mode became `0755`

**MEASURED.** `13_acceptance_00.md`, Gate 0 item 2, requires the installed service file to have mode `0755`. Product operations §9 installs that file with `install -m 0644`. The unit property is `RuntimeDirectoryMode=0755`; the executable binary is a third object. `13_report_00.md`, “First causal Gate 0 failure” and near-miss 3, records the distinction and says it interpreted the erroneous requirement as the runtime-directory setting.

**Effect.** The prompt could reject a correctly installed service, encourage an unnecessary chmod, or require the Worker to reinterpret an exact acceptance criterion. The actual first blocker was stale unit/binary content, not the correctly set `0644` file mode.

**Proposed improvement.** Use object-specific expected-state rows in operational prompts: artifact path/property, expected value, source owner, and readback method. Avoid free-floating numbers copied from summaries. Do not encode Linux file modes into universal AP.

**Acceptance example.** Service file `0644`, broker executable `0755`, and `RuntimeDirectoryMode=0755` are checked independently. A contradiction is surfaced explicitly and corrected prospectively; historical report bytes are preserved.

## D2-04 — Context and task budgets were not acted on

**MEASURED.** `12_implementation_02.md` combines four production safety changes, a systemd helper, service changes, documentation, a six-case rehearsal, multiple full test gates, two commits/pushes, and reporting in the already-used session 12. The Cooperator then reported one compaction and a second approaching, and explicitly requested smaller assignments/fresh Workers. `13_acceptance_00.md` nevertheless combined host readiness, static review, build/tests, authenticated UI behavior, normal typing, LEDs, lease expiry, cutoff, crash, watchdog, and cleanup, with broad mandatory reading.

The number of compactions and client token telemetry were not independently measured; the Cooperator's report is the evidence. Recommendations of approximately 200–250k or 1M tokens were not provider-verified model specifications.

**Existing rule.** The reading spine rejects routine full-archive onboarding. AP §14 already names compaction, lost provenance, and quality drift as rotation triggers. §15 allows coherent slices; §17 allows references instead of recopying the protocol. The rule was not applied effectively here.

**Proposed improvement.** Give one operational example of splitting this shape of work at deliverable boundaries: production code; cutoff/rehearsal; independent review; exact installation; one controlled physical trial. Combine only when coherent and context remains healthy. The chosen reading should be the Worker spine plus named task owners. A fresh session must receive the current task and its evidence, not the whole archive.

**Acceptance example.** After reported repeated compaction, the next prompt has one verifiable outcome and a clear report point. If an indivisible task really needs larger context, state that before dispatch and verify the selected provider/client capacity. Do not invent a universal token percentage, claim that every compaction invalidates all work, or use a larger model to excuse unlimited scope.

## D2-05 — The known installation gap became another acceptance failure

**MEASURED.** `12_report_02.md`, “Remaining risks and limitations,” explicitly states that the installed unit was not replaced. `13_acceptance_00.md` then requires completed installation as Gate 0 but forbids installation. `13_report_00.md` blocks on stale unit and binary. The Cooperator had supplied AP-doctor output; he had not supplied evidence of a completed install.

**What worked.** Identity checks prevented starting an old broker. Static checks and 13/13 CTest results supplied useful bounded evidence. These do not establish live G4 or independent physical acceptance.

**Proposed improvement.** Route the known dependency explicitly: either a useful source-review task that has no installed-host prerequisite, or the bounded installation needed before live acceptance. Deliver a concrete owner-executed command block when the operation is Cooperator-owned, rather than repeatedly referring to a section number. Reuse valid source-review evidence on the unchanged candidate; do not fabricate new primary-audit budgets.

**Acceptance example.** A missing known prerequisite does not trigger another full audit whose first action is certain to block. The immediate continuation of this case is installation of the already identified candidate, with no broker start.

## D2-06 — The grant contradicted its own execution and stop rules

**MEASURED.** `13_acceptance_00.md` prohibits persistent files and says only one `git fetch` is a permitted Git write, but requires build output and a report. Its added positive clause permits manually starting the broker “once,” while Gate 4 requires new guarded invocations for successive cases. Gate 0 orders a terminal stop on failure, while the returned report describes subsequent device-free review and tests. The prompt also labels the run the first primary acceptance of the whole without reconciling earlier acceptance history.

**Effect.** No literal execution could satisfy every clause. A Worker must either stop prematurely or silently choose an interpretation. Safety-sensitive authority must not depend on that choice.

**Proposed improvement.** Before issue, inspect the task's real actions against its actual allowed effects. Name exceptions for generated build output, the report, and exact temporary fixtures. If a failed live prerequisite permits useful read-only completion, say so in advance and forbid the live transition explicitly. Define one live invocation per prompt when that is the intended budget. Preserve earlier audit history and justify any additional evidence run by a changed candidate, changed host state, or named missing claim.

**Acceptance example.** Every required action has authority, every prohibition has an intelligible scope, and the failure path reaches the intended terminal point. A small direct consistency review is sufficient; do not mandate a repository-wide suite of tests asserting prose phrases.

## D2-07 — The one-keyboard route was narrowed again

**MEASURED.** The accepted R2 route and operations §7 make a second keyboard/SSH optional for an invocation-cutoff demonstration. `13_acceptance_00.md` correctly preserves that for Gate 4.4, but Gate 4.5 requires a separate recovery path for live watchdog evidence and makes the full verdict PARTIAL without it. This packed the desired one-keyboard demonstration together with a different, still-unproven failure-injection procedure.

**Important distinction.** A cutoff kill does not prove watchdog expiry; removing that distinction would weaken evidence. The observed problem is scope and expectation, not proof that every watchdog test is already safe with one keyboard.

**Product documentation LEAD.** At the candidate commit, operations §7 describes the new optional path while parts of testing-m2's production-hang procedure still refer to another keyboard/SSH. Their exact relationship needs a bounded reconciliation before a live hang grant; it is not an AP-wide rule about hardware.

**Proposed improvement.** Preserve an accepted recovery choice in the next task's observable outcome. Issue a cutoff/typing trial separately from watchdog failure injection. A later watchdog task needs its own demonstrated independent signal/recovery mechanism; do not silently make hardware purchase or SSH setup the prerequisite for all progress.

**Acceptance example.** A supported one-keyboard cutoff trial can reach its own bounded result, while watchdog and overall G4 remain explicitly open. No inference from timer success to physical usability or watchdog success is permitted.

## D2-08 — Formal report shape drifted

**MEASURED.** The archived `13_report_00.md` begins with a Slovak progress sentence, not the mandatory report header. Its phase-qualified result is `BLOCKED`, which the prompt itself incorrectly offered as a phase-result value. The structural enum provides `not-applicable` when no phase PASS exists; `BLOCKED` belongs to status. The issued templates repeat the identity coordinates despite the single-coordinate contract; `12_report_02.md` also repeats coordinate blocks. Repeated closure statements add volume, but are not themselves a violation of that coordinate rule.

Both historical files still contain useful identifiable evidence. These defects do not convert `BLOCKED` into acceptance-PASS, and must not be silently repaired in the archive.

**Existing rule.** The RF-19 Companion Integrity Invariant and Prompt Contracts already specify header, coordinate identity, result shape, and exact persistence. The current archive is a structurally nonconforming report package; its substantive observations can be attributed and used to route the next safe task, with nonconformance disclosed.

**Proposed improvement.** Provide one compact report example for a blocked outcome: exact first line, one coordinate block, `status: BLOCKED`, `Phase-qualified result: not-applicable`, observed evidence, and the permitted report-file write. Keep the informal Slovak notification outside the saved English report. Let a narrow optional artifact check catch structure; do not require a new Worker just to prettify a report.

**Acceptance example.** The saved report starts with the required header and contains one coordinate set. Its readback is the authoritative file. Existing defective reports remain immutable history with prospective reconciliation.

## D2-09 — Normal owner-controlled sudo became a dead end

**MEASURED.** `13_report_00.md` records failed `sudo -n true`; the named broker-user access(2) test was therefore not run. The prompt treated interactive authentication as a terminal stop and provided no complete Cooperator-executed route. Earlier user-session memory said sudo had previously been available, which did not establish permission in this Worker's process/session.

**Existing rule.** AP “Owner-Executed Commands and Privileged Sessions” already covers a bounded owner terminal, OS-only password entry, command markers, output readback, and timestamp release. Privilege in one terminal is not a guarantee in another process. The report's suggestion about granting passwordless sudo is a LEAD, not a necessary remedy.

**Proposed improvement.** For authorized host installation, name the owner-executed fallback in the prompt. Keep authentication and the bounded privileged commands in the same owner terminal, wait for the result, and verify effects independently where readable. Do not request a password in chat, create keep-alives, change sudoers, or assume a separate Worker terminal inherited the owner's timestamp.

**Acceptance example.** An ordinary password-authenticated owner install can complete without granting permanent passwordless sudo. Worker identity checks remain honest when the owner supplies the privileged evidence.

## D2-10 — Product documentation kept advertising completed work as pending

**MEASURED.** `12_report_02.md` completed R1/R2 but explicitly excluded README/ROADMAP/AGENTS changes. At `cb72ae0`, root project guidance still identifies a recovery-design decision and production gaps as next work. `13_report_00.md` flags ROADMAP lag. The follow-up failed to allocate a bounded update to the actual durable owners.

**Effect.** Each fresh Worker can be sent back through completed planning or safety work. META starts functioning as the only current-state explanation, against its intended historical role.

**Proposed improvement.** Include narrowly scoped current-state reconciliation in the appropriate implementation allowlist, or schedule it when that slice is reconciled. Record the distinction: implemented in tree, reviewed with device-free evidence, installed on host, physically accepted. An accepted implementation must never be described as completed G4.

**Acceptance example.** A fresh reader can see R1/R2 implemented, host installation pending or verified, and physical acceptance open from the product's durable owners. Avoid a second task queue or a new orchestration-state file.

## What to change in AP, and what not to change

The highest-value AP work here is a usability/projection improvement under the existing owners: a complete manual-delivery/report-write example; a source-retrieval failure example; a small action-versus-authority review; and a worked example of context-aware slicing with an owner-controlled install. Most findings are **not missing universal semantics**. Fix their application and examples before adding new rules.

Do not mandate 1M-token models, universal per-commit rotation, second keyboards, passwordless sudo, report-only Workers, full archive reading, long reports, or tests that merely mirror all protocol text. Preserve independent evidence where the actual risk needs it. Do not reopen unrelated AP design or product features as part of this brief.

Suggested review order for a separately authorized AP update:

1. D2-01 and D2-02: eliminate the copy/paste burden and require truthful source provenance.
2. D2-03, D2-06, D2-08: make issued artifacts executable and structurally coherent.
3. D2-04, D2-05, D2-09: reduce repeated onboarding and predictable blockers.
4. D2-07 and D2-10: preserve accepted product decisions in live task routing and durable product docs.

Each finding can be accepted, fixed, deferred, or rejected with a specific reason by that update task. This document does not claim any AP fix has shipped.

## ContextDesk reconciliation and immediate continuation

`12/03` produced the R1/R2 candidate and reported implementation-PASS. `13/01` reported BLOCKED on the installed artifact mismatch; its static/device-free checks reported 13/13 CTest and successful self-tests, but no broker start, LEASE, ARM, device access, or G4. The formal report defects above are preserved and disclosed. No independent G4 PASS or logical-whole closure exists.

The next bounded task is **installation and identity readback of the already-built candidate**, while leaving the broker static/inactive. It does not repeat the broad audit or authorize a physical trial. Its new prompt explicitly grants the Worker creation/readback of its report file in the configured META directory; the Cooperator retains Git archival. A subsequent physical trial requires a newly scoped prompt and current recovery prerequisites.

ContextDesk's intended value remains a useful personal KDE productivity tool. This defect brief is a side investigation; AP redesign is not a new prerequisite for continuing product development.

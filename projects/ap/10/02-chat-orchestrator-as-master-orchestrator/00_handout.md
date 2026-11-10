# AP Protocol Evolution Handout: Closure-Driven ChatOrchestrator as Master Orchestrator

**Requested Meta destination:** `projects/ap/10/02-chat-orchestrator-as-master-orchestrator/handout.md`  
**Artifact type:** Cooperator-requested protocol-evolution handout / design brief. **Not** a Worker prompt, implementation grant, acceptance verdict, AP amendment, or authorization to mutate any repository.  
**Authored by:** read-only ChatOrchestrator, 2026-11-10.  
**Requested by:** COOPERATOR.  
**Historical filename note:** the Cooperator explicitly selected `handout.md`, rather than the common `00_handout.md`. Preserve this exact locator. The filename does not change the universal AP semantics or automatically activate a trace convention.  
**Authority:** proposal/evidence only. `AP.md` remains the sole live normative AP authority.  
**Intended consumer:** a future separately authorized AP protocol-design/implementation Orchestrator, then the COOPERATOR for material protocol decisions. A Worker is **not** being assigned by this handout.  
**Disposition:** ready for future protocol-change planning; no AP change, Git operation, or consumer-pin update performed here.

## 0. The specific problem, without reintroducing an existing feature

The COOPERATOR wants a persistent *coordination pattern*, not another agent role:

1. A read-only **ChatOrchestrator** with a **Master Orchestrator / development-run** session scope inspects current public project truth, the governing AP pin, accepted specifications, cross-whole dependencies and the previous whole's exact closure.
2. It proposes the smallest valuable **next logical whole** and authors a professional opening `00_handout.md` for a **different per-whole Orchestrator** with direct access to a local project checkout.
3. That per-whole Orchestrator independently revalidates facts, obtains any needed COOPERATOR material decisions, starts an initial native Planner, grants bounded implementation work to Workers, and handles reports, acceptance, publication and deterministic closure under AP.
4. It returns a truthful `xx_closure.md` naming the exact result/evidence/limits. The Master independently reconciles that closure against the now-current canonical repository, records provenance and selects/recommends the next bounded candidate without reopening closed work.
5. The Master then authors the successor whole's handout. The loop repeats, under ongoing COOPERATOR control, with no standing implementation or Git authority transferred by a handout or closure.

**Critical baseline:** AP already implements `Orchestrator session scope: development-run` (explanatory name **Master Orchestrator**), run maps, provisional handouts, revalidation, and separate Orchestrator/ChatOrchestrator access profiles. Meta `BRAINSTORMING.md` §7 is already marked **promoted** by AP `d7023cf...` / ADR-0026. The new proposal must therefore **close a concrete procedural gap or clarify routing**, not invent a fourth role or restate implemented semantics as new functionality.

## 1. Source-of-truth and minimum evidence to revalidate

Use source-precedence and per-role reading from the exact AP under review. Sources accessible at authorship:

- [Canonical AP semantic authority](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/AP.md): §3 **Orchestrator Session Scope**; §14 **Run-Level Handouts**, **Continuation Bootstrap**, handout/closure readiness; RF-01/02/05/14/19 and the task-authority section.
- [AP Orchestrator operational projection](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/AP_ORCHESTRATOR.md): continuation, delivery/dispatch, bounded prompting, closure.
- [AP structural prompt contract](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/PROMPT_CONTRACTS.md): exact fields only where needed. No new structural fields without an actual semantic requirement.
- [Meta README](https://github.com/cisarik/meta/blob/main/README.md): Meta-local two-part directory numbering, optional `00_handout.md`, `00_notes.md`, handoff/closure sequence, Worker exchange storage coordinates, COOPERATOR-owned Meta Git in ChatOrchestrator delivery.
- [Meta BRAINSTORMING §7](https://github.com/cisarik/meta/blob/main/BRAINSTORMING.md): prior Master-Orchestrator proposal, measured costs, status promoted. Treat as historical proposal, not separate live AP.
- [Meta AP_DEFECTS](https://github.com/cisarik/meta/blob/main/AP_DEFECTS.md) and `AP_DESTILLED.md`: measured observations and their disposition, only when the future protocol-change task explicitly scopes them. Do not assume every historical observation remains open.
- [BookRadar canonical project](https://github.com/cisarik/bookradar): case-study source; its **own immutable pin** is `d7023cf037f6d17885c3ede5c04812c61640da50` as reported at the closure. Do not update that pin as a side effect of changing AP.

**Evidence classification:** the two BookRadar closure documents are historical, Orchestrator-authored attestations; exact immutable project artifacts at a commit may be inspected directly. This preparation was able to retrieve the `5c820ab...` committed domain contract, ADRs and README by immutable raw URLs, but could **not** independently establish current GitHub `refs/heads/main` and symbolic HEAD through a live remote-ref read. The future owner must perform a fresh current-state check when a decision requires that claim; never replace it with a cached landing page, prior closure, or a bundle claim.

## 2. Measured example: two completed BookRadar logical wholes

**Whole A**: `bookradar-ap-bootstrap`, Meta `projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md`.
- Closure reports `closed-by-ORCHESTRATOR`, acceptance PASS, published commit `12864ac874d74c562e22243bd622bd2729dfdaca`, root AP adoption with managed `AGENTS.md`, README and pinned `.ap`; no runtime code.
- The Master used this closure as predecessor context for the next whole. The closure did not grant a new Worker session.

**Whole B**: `bookradar-domain-contract`, Meta `projects/bookradar/00/01-bookradar-domain-contract/01_closure_03.md`.
- Closure reports `closed-by-ORCHESTRATOR`, acceptance PASS, docs-only commit `5c820abd439850039adf9866af26acfa15287493`, parent `12864ac...`, exact four updated/created Markdown paths: README, `docs/domain-contract.md` and two ADRs. AP gitlink unchanged; strict `ap doctor` PASS was reported. Exact immutable Markdown source is retrievable at that commit.
- Accepted domain boundaries: Work vs Edition/printing vs Copy/lot vs Offer; separate immutable attributed observations; 24-hour positive-availability verification requiring reviewer-approved direct evidence; no LLM assertions as proof; account-scoped watches/library concepts; ambiguous matching and conflicting evidence remain explicit.
- Deferred: Rust code, persistence, UI, Hermes/MCP/NUC deployment, real screenshots, privacy/security/licensing/public collaboration policy and other non-semantic decisions.
- Closing Orchestrator explicitly returns a handoff to the upstream ChatOrchestrator, recommending a bounded Rust foundation; it **does not** select the next whole or issue a successor grant.

This shows a real feedback loop, rather than a speculative orchestration diagram. It does **not** establish that a new protocol rule is required: the gap must first be demonstrated against existing AP §3, §14 and RF-19.

## 3. Target behavior: two axes, three responsibilities

| Concern | Master ChatOrchestrator | Per-whole Orchestrator | COOPERATOR |
|---|---|---|---|
| Persistent AP role | ORCHESTRATOR | ORCHESTRATOR | COOPERATOR |
| Access profile | `ChatOrchestrator` (mediated; read-only to canonical project) | `Orchestrator` (direct working checkout, subject to grants) | Own tools/actions |
| Session scope | `development-run` | `logical-whole` | Not applicable |
| Source of objective | COOPERATOR-bounded run, current project truth | One selected logical whole | Material objective and route choices |
| Worker prompts | None for a whole owned by another Orchestrator | Issues exact grants for its Workers | Receives/approves material decisions |
| Planning | Cross-whole sequencing only; **never** substitutes native Planner | Initial native Planner and AP plan-to-execution gate | Accepts material trade-offs |
| Reports / acceptance | Reads closure as evidence, does **not** accept that whole | Reconciles Worker reports, accepts/corrects/closes its whole | Subjective/material acceptance |
| Git/mutation | No mutation of canonical project or Meta | BookRadar/API Git and local/SSH actions **only** within explicit grants | Meta Git ownership for ChatOrchestrator convention |
| Output | Run-state update + next handout/restoration signal | Closed whole + exact `xx_closure.md` | Decision and authorized routing |

A read-only *access profile* is **not** itself a Master scope; conversely, Master scope does not imply GitHub reachability. Conflate neither with selected delivery route, authority, or actual session separation.

## 4. Proposed closure-to-next-handout protocol clarification

This is candidate wording for expert review, **not adopted AP text**:

> **Closure-driven cross-whole continuation.** When an ORCHESTRATOR session with scope `development-run` and a mediated ChatOrchestrator access profile receives a closure from a distinct per-whole Orchestrator, it shall classify the closure as historical evidence, verify material result anchors against current available canonical repository/external truth, reconcile the run map and accepted decisions, and recommend exactly one next bounded logical whole. A run map, closure, or handout never supplies new authority. The COOPERATOR retains material objective selection and may reject or reorder the recommendation. After selection (or as a clearly marked provisional candidate, if the existing AP run-level rules permit), the run-scoped Orchestrator shall prepare a bounded restoration handout and a distinct successor initialization signal for a fresh per-whole Orchestrator. That successor performs Stage-1 restoration and fresh local-state verification, and alone routes that whole's first native Planner and subsequent grants. The run-scoped Orchestrator does not issue Worker prompts, evaluate Workers, accept results, or close a whole coordinated by a different Orchestrator. A separate, successful publication claim requires independent public-ref evidence; if unavailable, label the limitation and route the appropriate verification without inventing success.

**Candidate scope of the actual change:** clarify the *on-demand rolling horizon* (one successor handout after one closure), the exact return-edge from `xx_closure.md` to the run-scoped ChatOrchestrator, and the bridge from a handout to the fresh per-whole initialization signal. These are possible **operational clarifications** to existing AP, not necessarily new normative semantics. The future AP-update owner must diff against existing wording before deciding.

**Potential conflict requiring resolution:** the COOPERATOR's phrase “every read-only Chat Orchestrator should do this” must not silently convert the `ChatOrchestrator` access profile into `development-run` session scope for **all** chats, including ordinary one-whole sessions. Prefer an explicit scope declaration and default handoff behavior **within** the declared run scope, unless the COOPERATOR decides otherwise after seeing the compatibility costs.

## 5. Required design questions before any protocol edit

1. What observable behavior is actually missing from AP `d7023cf`? Build a **already-implemented / ambiguous / genuinely-missing** matrix with precise anchors. If no gap remains, recommend **no AP semantic change** and a project-local operating recipe instead.
2. When the Master recommends the successor whole, does the current COOPERATOR run objective already authorize its *selection*, or does RF-01 require an explicit current decision? Preserve RF-01; do not rewrite human approval out of the protocol under the banner of reducing microapprovals.
3. Should the return-edge require a particular closure content field, or can current §14 and RF-19 content supply it? Avoid a mandatory new form for a need already expressible with existing artifacts.
4. How is the Master notified of closure when it cannot directly access a local Meta checkout? Consider exact path via COOPERATOR handoff, an authorized committed report, and current public evidence; distinguish file delivery from artifact authorship and Meta Git ownership.
5. Can the Master continue with **only exact committed evidence** if public branch ref is not independently accessible? Follow existing ChatOrchestrator bundle limitations; do not claim public-ref equality without public observation.
6. Is `00_handout.md` provisional only if created **before** the whole is selected/opened? Should a handout prepared after an explicit selection be described as the whole's ordinary opening continuity artifact rather than retroactively labeled provisional? Keep existing filename and revision semantics.
7. What minimal evidence verifies proper separation of the Master and per-whole Orchestrator? Distinct session identity, no Worker prompts from Master, no cross-instance acceptance/closure, positive per-whole first Planner in native Plan Mode, and no privilege inference.
8. How should the Master react if the closure recommends one route while current repository facts contradict it or the COOPERATOR changes direction? Always revalidate and explicitly reconcile, never blindly follow a closure recommendation.
9. Which Meta-specific storage rules must **stay in Meta** (archive-group numbering, `00_notes.md`, `_03` closure filenames, Git first-add), rather than being promoted as universal AP semantics?
10. Does this proposal require a new ADR/CHANGELOG entry, projection update, FAQ example or only explanatory prose? Choose minimal changes consistent with AP's single semantic owner.

## 6. Example end-to-end state machine (descriptive, not authority)

```text
Cooperator-bounded development-run objective
    -> Master (ChatOrchestrator, scope=development-run) restores read-only
    -> Master recommends next bounded whole
    -> Cooperator selects material objective/route per RF-01
    -> Master prepares exact opening handout + restoration/init signal
    -> Fresh per-whole Orchestrator (scope=logical-whole) restores, revalidates
    -> Worker 01/01 native Planner with a separately complete read-only grant
    -> separately authorized bounded Worker implementation, validation, publication
    -> per-whole Orchestrator alone reconciles acceptance + closes
    -> xx_closure.md delivered as evidence, not authority
    -> Master independently revalidates published/current state, updates run map
    -> recommend next whole OR stop on material uncertainty/Cooperator pause
```

**Negative paths:** closure PARTIAL/BLOCKED; latest public branch unavailable; local uncommitted changes; competing active Worker; stale provisional handout; deployment or secrets in closure; rejected/changed objective. In each case classify the limitation and stop only the dependent transition. Do not manufacture a fresh logical whole merely to escape a blocker, report budget, or unresolved acceptance.

## 7. Work boundary for the *future separately authorized* AP-update whole

A future Orchestrator (not assigned here) should first perform a **read-only diagnostic comparison** against the selected current AP commit. Only after a Cooperator-reviewed plan and explicit grant should it change AP sources. Suggested minimum implementation envelope, if a gap is proven:

- `AP.md` remains the sole semantic owner. Modify its §3 / §14 only where a real behavioral ambiguity exists; preserve RF-01, RF-02, RF-05, RF-14, RF-19 and the stable consumer compatibility tuple.
- Update `AP_ORCHESTRATOR.md` only as an operational projection of that exact rule, and `PROMPT_CONTRACTS.md` only if exact new fields are demonstrably necessary. Update `README.md` / `FAQ.md` selectively when user-facing discoverability benefits.
- Include an ADR for a genuine protocol-level decision and a concise CHANGELOG entry; don't invent an ADR for an unchanged rule.
- Reconcile relevant Meta `BRAINSTORMING.md`, `AP_DEFECTS.md`, `AP_DESTILLED.md` entries as **historical evidence** in a separately permitted Meta action; do not let a Worker silently amend Meta or backdate old records.
- No bulk sync of consumer `.ap` submodules, no AP pin change to BookRadar/Kronika/FrameNest, no remote host/NUC action, no production deployment, no Git force-push or history rewrite, no credentials handling. Any such work is a separate explicit task.

**Avoid unnecessary ceremony:** do not require a Master handout batch for every new whole, or a second acceptance hierarchy above the per-whole Orchestrator. Default to the lowest-cost rolling-horizon handout supported by AP and actual project evidence.

## 8. Acceptance examples and evidence to ask for

A future authorized implementer should validate these scenarios, by trace examples and proportional semantic/operational review rather than a giant duplicated protocol test suite:

| Scenario | Expected result |
|---|---|
| A closed BookRadar whole returns a valid closure to a Master ChatOrchestrator | Master checks predecessor and current project evidence, recommends a **new** whole and issues no Worker grant |
| The closure suggests Rust but Cooperator instead selects UI | Master records the new decision and prepares a UI handout; no presumption that the closure recommendation is binding |
| Master lacks current remote-ref evidence | Classify `public branch state not directly observed`; do not equate closure/bundle SHA with GitHub HEAD |
| Master authors successor handout | Handout grants no mutation; distinct per-whole Orchestrator restores and runs a native Planner |
| A per-whole Worker has `sudo` and push capability | Neither Master nor closure inherits sudo/push; a new complete grant is required |
| A stale provisional handout has materially wrong baseline | Per-whole Orchestrator records revalidation and issues successor artifact; does not rewrite historical one |
| Previous whole is still active or acceptance is unresolved | Do not mark it closed or treat a recommendation as acceptance |
| AP code already fully specifies the workflow | Close the protocol-change proposal as no-semantic-change, with a precise reference; avoid redundant edits |

Evidence package: exact chosen AP baseline/ref, source-anchor comparison, the smallest source diff (if any), link/fragment review, role/authority contradiction check, trace-scenario results, directly observed versus reported Git facts, optional public publication readback only when authorized, and a concise handoff of any genuinely unresolved decision.

## 9. Readiness and next action

**Readiness:** PASS for a future **read-only protocol-gap review**, not for implementation or publication. The scope and concrete BookRadar observations are known; the existence of a missing AP rule is **not yet established**. This distinction is the key guard against unnecessary changes.

**Recommended next action when the COOPERATOR opens this AP whole:** initialize a fresh AP Orchestrator using this exact handout; have it read the chosen current AP checkout and Meta history, produce an evidence-backed *already-existing vs missing* gap table, and, only if a material gap is found, plan the minimum bounded edit for a separate grant. No Worker or Orchestrator is assigned by creating this document.

## 10. Artifact lifecycle

- **Class:** retained proposal and cross-project orchestration case-study handout.
- **AP relationship:** historical/advisory evidence, non-authoritative.
- **Consumer:** a future AP protocol-evolution Orchestrator and COOPERATOR.
- **Discovery:** exact requested Meta path, linked AP and Meta source anchors above, plus the two named BookRadar closures.
- **Retention:** keep as originally authored historical proposal; superseding changes go into explicit successor artifacts, not silent in-place rewrites after archival.
- **Cleanup owner:** COOPERATOR (Meta Git owner), under separately valid cleanup authority.

**Final invariant:** Master prepares and routes; per-whole Orchestrator governs its own whole; Worker executes a bounded grant; COOPERATOR owns material decisions. No document in this chain upgrades historical evidence into authority.

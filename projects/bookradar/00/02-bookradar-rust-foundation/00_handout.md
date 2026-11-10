# BookRadar — Opening Handout: `bookradar-rust-foundation`

**Artifact:** `projects/bookradar/00/02-bookradar-rust-foundation/00_handout.md`  
**Kind:** Opening continuity, domain-dependency and decision-context handout for a fresh, directly capable per-whole Orchestrator. **Not** a Worker prompt, permission grant, implementation plan, acceptance, publication or closure.  
**Authored by:** upstream read-only ChatOrchestrator (development-run / Master scope), 2026-11-10.  
**Predecessor:** `projects/bookradar/00/01-bookradar-domain-contract/01_closure_03.md` (`closed-by-ORCHESTRATOR`, acceptance PASS).  
**Earlier closed whole:** `projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md`.  
**Logical-whole candidate identity:** `bookradar-rust-foundation`.  
**Handout status:** provisional until the fresh per-whole Orchestrator reconciles exact repository, Cooperator selection and activated Meta trace. Do not modify this frozen handout in place after opening; material changes use a successor handout under the AP/Meta handoff sequence.  
**Intended successor capability profile:** `Orchestrator` (direct project checkout), with `Orchestrator session scope: logical-whole`.  
**Upstream author access profile/scope:** `ChatOrchestrator` / `development-run`.  
**Restoration classification:** **PASS for read-only preparation of the first Planner** on the immutable accepted semantic baseline; current public `main`, local checkout and tool availability **must** be independently revalidated before any Worker grant. Not implementation readiness.  
**Authority:** zero. Neither this handout nor the previous closure grants Git, filesystem, SSH, host, dependency installation, implementation, acceptance, publication or Meta mutation.

## 0. Selection rationale and one bounded objective

Following two completed, accepted BookRadar logical wholes, the upstream ChatOrchestrator recommends **a minimal executable Rust foundation** as the next dependency. The COOPERATOR asked the upstream ChatOrchestrator to continue selecting/recommending logical wholes and creating their handouts after reviewing closures. The actual per-whole opening and any material technology/architecture decisions remain subject to governing AP RF-01 and the COOPERATOR's current instruction.

**Single objective proposed for this whole:** establish a clean, maintainable, compilable and deterministically tested Rust foundation that demonstrably respects a carefully selected **minimal subset** of the already accepted BookRadar domain contract. The initial Planner must choose the smallest useful vertical or horizontal slice and decide whether a tiny persistence boundary is warranted *now* or deferred. Do **not** attempt to implement the complete domain contract, full database, UI, agent engine, or NUC deployment in one whole.

Why this precedes the UI / Hermes integration:
- The product already has a clear semantic contract but no executable enforcement; Rust foundation enables future data, interface and research work without inventing domain semantics ad hoc.
- Provenance, time-bound observations and ambiguity must not be collapsed into a flat product row even in demo fixtures.
- A small, comprehensible Rust project with focused tests is friendlier to future public contributors than prematurely built framework scaffolding.
- This is an **architecture choice still to plan**, not a preapproved crate, web framework, schema, package policy, or API commitment.

Alternative next wholes considered but deferred: `bookradar-ui-shell` (faster visual learning, would need mock domain/data assumptions) and `bookradar-research-ingestion` (real Hermes workflow, but executable validation, identity and durable app skeleton do not yet exist). Selection should be revisited only for fresh material evidence or COOPERATOR redirection, not because a Planner prefers a different project.

## 1. Baseline and source precedence

**Canonical repository:** https://github.com/cisarik/bookradar  
**Historical accepted baseline, per predecessor closure:** branch `main`, commit `5c820abd439850039adf9866af26acfa15287493` (`docs: define BookRadar domain contract`), parent `12864ac874d74c562e22243bd622bd2729dfdaca`, tree `acf8e4c1142919b018a58fe3c43086ce26ef6a10`.  
**Pinned governing AP:** `.ap` gitlink `d7023cf037f6d17885c3ede5c04812c61640da50` (immutable; expected detached checkout).  
**Historical acceptance:** exact docs-only four-path commit; public HEAD/ref equality, clean index and submodule, strict `ap doctor: PASS`, all links/anchors validated; E1 acceptance without independent audit because none required for that docs-only whole. This is **historical closure evidence**.

Sources to inspect in the fresh checkout, at the *currently verified* revision:

1. Root [`AGENTS.md`](https://github.com/cisarik/bookradar/blob/5c820abd439850039adf9866af26acfa15287493/AGENTS.md): canonical managed AP block, no project-authored supplementary rules at predecessor baseline.
2. Governing `.ap/AP.md` and `.ap/AP_ORCHESTRATOR.md` at the gitlink; consult `PROMPT_CONTRACTS.md` for exact Worker grants and reports. Read the ORCHESTRATOR minimum-reading spine; don't substitute a newer AP `main` for the consumer's pin.
3. [`docs/domain-contract.md`](https://github.com/cisarik/bookradar/blob/5c820abd439850039adf9866af26acfa15287493/docs/domain-contract.md), status **Accepted 2026-11-10**, revision 1: **owns current product semantics**.
4. [`docs/adr/0001-book-edition-and-offer-identity.md`](https://github.com/cisarik/bookradar/blob/5c820abd439850039adf9866af26acfa15287493/docs/adr/0001-book-edition-and-offer-identity.md): accepted historical rationale for distinct identities.
5. [`docs/adr/0002-evidence-and-research-trust-boundary.md`](https://github.com/cisarik/bookradar/blob/5c820abd439850039adf9866af26acfa15287493/docs/adr/0002-evidence-and-research-trust-boundary.md): accepted historical rationale for evidence and untrusted research admission.
6. [`README.md`](https://github.com/cisarik/bookradar/blob/5c820abd439850039adf9866af26acfa15287493/README.md): describes application not yet implemented and defers license/public policy.
7. Predecessor `01_closure_03.md` as historical handoff, and [Meta README](https://github.com/cisarik/meta/blob/main/README.md) only for activated Meta-local naming/storage.

**Independent upstream observation:** the exact domain contract, both ADRs, README and root AGENTS.md were retrieved from immutable `5c820ab...` paths on 2026-11-10 and match the closure's claims about the documents. A fresh *remote refs/heads/main* / symbolic HEAD equality check could not be completed through the upstream read-only browsing route; a cached GitHub landing page was inconsistent. Accordingly: **`public branch state not directly observed` for the upstream's current-branch claim**. This limitation does not negate the exact immutable-document observations. The fresh per-whole Orchestrator must verify `main`, current checkout, ancestors, `.ap` gitlink, and clean/dirty status before issuing a current Worker grant. Do not infer absence of new commits or uncommitted files from the historical closure.

No NUC or SSH access, `sudo` lifetime, local Rust installation, dependencies, local branches, active Worker status, or current remote protections were observed by the upstream ChatOrchestrator.

## 2. Nonnegotiable accepted semantics (do not redesign)

The documentation whole is closed. Its accepted product constraints are **inputs**, not open questions for a new Worker to reinterpret casually:

- **Entity boundaries:** Author, Work (intellectual creation), language-specific Edition/printing, optionally identifiable physical Copy/lot, seller Offer, immutable time-bound Observation, Evidence, Source, ResearchRun; owner-scoped Watch and LibraryEntry. The conceptual terms do **not** prescribe Rust struct names, tables or cardinalities.
- **Identities:** internal stable IDs must not be derived blindly from title, URL or ISBN; absent/conflicting/invalid ISBN and unresolved subject identity must remain representable; source-scoped listing identity differs from URL and seller identity.
- **Language:** distinguish Slovak, Czech, mixed, unknown and conflicting evidence. A Slovak website or agent assertion alone does not establish a Slovak edition.
- **Availability dimensions:** source-reported state, access status, listing disposition, knowledge assessment and temporal assessment are independent. 429/CAPTCHA/timeouts do not imply sold-out; 404 alone does not prove sale.
- **Freshness:** an affirmative *“checked available”* result needs reviewer-approved direct browser/manual evidence identifying the subject and an explicit source availability assertion; evidence must be less than 24 hours old. Eligibility expires exactly at observation + 24h and is suppressed immediately by conflict or failed recheck. An LLM claim or merely validated JSON is insufficient.
- **Time and money:** preserve attribution, offsets/unknown time representation, currency, price basis, condition and unknown shipping. Never collapse unlike units/currencies into a single cheapest price or treat historical price as current.
- **Evidence:** a hash only attests byte identity; screenshot reference is metadata, not license, retention right or proof of obscured facts.
- **Research boundary:** untrusted research assertions must pass structural/invariant checks, can be quarantined, and must not directly become trusted stock facts. Replay of identical producer/run/finding is a no-op; conflicting payload for same identity is not. Later import of older evidence does not roll observed reality backward.
- **Owner boundary:** a person's watch or purchase is not global catalog truth; actual account/privacy design remains deferred.

The contract includes **18 fictional worked cases** and a deterministic 24-hour expiry timeline. Use them as a semantic validation inventory; choose the smallest meaningful subset for this whole and explicitly identify which are not yet executable. The whole must not claim to implement all 18 unless evidence proves it.

## 3. What is in scope for the first Planner to evaluate

Ask a fresh Planner to inspect current project truth and propose **one minimal implementation slice** with direct evidence for these decisions. It must not silently promote candidate stacks to accepted architecture:

1. **Cargo shape:** one crate or small workspace? Is a minimal library core plus optional binary appropriate now? Choose the simplest robust form that can grow with future UI and persistence without premature abstraction.
2. **Rust toolchain policy:** determine pinned stable toolchain, edition, version/MSRV policy, formatting and lint gate appropriate for an accessible public repository. Check environment first and record needed COOPERATOR decisions if policy is material.
3. **Contract-to-code seam:** choose a compact set of value types and pure domain operations (e.g., identities, language evidence, availability/access distinctions, deterministic freshness calculation) rather than implementing every conceptual entity and every integration.
4. **State/persistence boundary:** compare **no persistence yet**, a deliberately narrow in-memory repository trait, or a small SQLite-backed implementation. Provide the cost of migrations and native dependencies. No physical DB schema is predetermined by the previous ADRs. SQLite remains a candidate, not an accepted mandate.
5. **Testing:** derive deterministic fixtures from agreed semantics; preferably use a controlled injected clock/time input for expiry and failed-recheck cases. Include checks that disprove bad shortcuts (Czech ≠ Slovak; HTTP 429 ≠ unavailable; agent-only claim ≠ verified; 24h boundary exact; same ISBN ≠ forced identity).
6. **Quality gates:** propose the smallest reliable local commands for building, tests, formatting and linting, plus a proportionate strategy for fresh-clone build and CI. Do not claim that unavailable runtime/toolchain tests passed.
7. **Architecture decision record:** write a new ADR only if a meaningful accepted implementation-level choice is made (for example storage/toolchain framework selection), with options and rationale; leave product semantics owned by the accepted domain contract.
8. **Public collaboration:** clarify source layout, README build instructions and dependency provenance. A public repository does not automatically authorize adding an open-source license, security contact, privacy policy or external support promise. Escalate those choices instead of inventing them.
9. **Acceptance evidence:** exact changed paths and targeted tests; negative scope proof (no AP pin change, no unrelated host or evidence mutation), git diff, authorized commit/push and verified publication. No claim that strict `ap doctor` substitutes for Rust tests.

Recommended direction (advisory): **small testable Rust core first**, with no browser, network scraping, agent runtime, authentication, scheduler or UI implementation. If the Planner finds that a tiny persistence layer is required to demonstrate the core, justify the bounded expansion; otherwise defer persistence as its own later whole.

## 4. Scope exclusions and stop lines

This whole does **not** authorize:

- The Hermes `slovak-book-hunter` skill, Playwright MCP integration, scraping, external API calls, cron, NUC installation, `ssh`, `sudo`, services, production or Tailscale ingress.
- Live retail data ingestion, real screenshots, screenshot storage or redistribution, personal data, accounts, public exposure, purchases or login flows.
- A full responsive Matrix-inspired dashboard, UI framework or frontend build; these have their own future whole.
- An exhaustive physical SQLite schema, generic e-commerce monitoring, migration of external datasets, or durable public API stability.
- A new license, public contribution/security/privacy promise or support SLA without COOPERATOR decision.
- Updates to `.ap`, its gitlink, the AP root repository, other projects, or Meta Git from a BookRadar Worker.
- Git `push --force`, rebases/rewrites of published history, undocumented dependency installation, unsafe shell cleanup, or privilege inference from the COOPERATOR's `sudo -v`.

The positive authority in a later Worker grant must name **specific paths and operations**; none is granted by this handout. If the Planner proposes new scope, hand material options to the COOPERATOR instead of treating them as approved.

## 5. Operating model for the fresh per-whole Orchestrator

**First action: Continuation Bootstrap Stage 1 (read-only).** Read the current checkout's root `AGENTS.md` and its pinned minimum-reading AP spine; identify actual repository baseline, branch, remote, AP pin, clean/dirty state, active work, protocol and project source ownership, and any activated project-owned optional storage. Compare the predecessor closure's claims against *current* evidence. Report the exact difference if the branch advanced; avoid automatic rollback or silent incorporation of unrelated commits.

**Stage 2: reconcile one bounded objective with COOPERATOR.** The upstream has supplied a recommendation and an opening handout, not a current mutation grant. Explicitly preserve the COOPERATOR's ownership of material choices and document the intended whole/constraints before the first Worker task.

**Initial Planner:** assign a **fresh** Worker session `01`, exchange `01`, with **native Plan Mode required**, targeted repository read-only inspection, a bounded plan and report; choose actual delivery route once per whole as AP requires. The first exchange is structurally distinct from a later implementation grant; Worker sessions/exchanges and Meta suffixes must not be conflated. No Worker can proceed to implementation merely because it produced a plan.

**Worker report contract:** all standard Worker reports start `### Report for ORCHESTRATOR_CHAT` and include unchanged logical whole/session/exchange coordinates, status, result, baseline/end commits, changed paths, tests, exceptions, issues and expired authority per the pinned AP/PROMPT_CONTRACTS. Persist direct-to-trace only when exact permission, destination and activated delivery record permit it.

**Implementation grants:** after plan reconciliation and necessary Cooperator decisions, issue a **new, self-contained**, smallest scoped task to a capable Worker. COOPERATOR has permitted Worker commit and push for BookRadar *when the individual grant explicitly names branch, remote, allowlist and publication verification*. This is not standing Git authority. The ChatOrchestrator remains read-only; Meta Git is COOPERATOR-owned under the existing activated ChatOrchestrator convention.

**Acceptance and closure:** weigh direct executable evidence according to risk, decide corrections/acceptance with finite budgets and no repeat audits unless evidence warrants them, classify any missing tests, and verify the actual public commit after authorized publication. The per-whole Orchestrator alone closes this whole and authors a truthful `xx_closure.md` with exact identity, accepted scope, deferred decisions and next logical-whole candidates. Send that closure as a historical handoff to the upstream Master ChatOrchestrator. It is **not** successor authority.

**Meta local trace:** preferred directory `projects/bookradar/00/02-bookradar-rust-foundation/`, with `00_notes.md` on opening and this `00_handout.md`. First standard Worker exchange is AP `01/01` stored, when activated, as `01_planning_00.md` + `01_report_00.md`. The first implementation may be session `01/02` (same healthy session) or a fresh session `02/01` depending on AP gates; never predetermine coordinates before routing. The original handout stays frozen once the whole opens; successor handout/closure numbering belongs to the independent Meta handoff sequence, not to Worker exchange suffixes. First-add of a prompt/report pair belongs together after the report exists. Meta placement and Meta Git actions are separate permissions.

## 6. Quality standard for this public Rust foundation

A technically credible first slice should aspire to:

- Reproducible, documented build inputs; explicit dependency provenance; a limited, well-reviewed dependency graph.
- Idiomatic Rust types that make invalid states hard to represent **without** turning unresolved facts into impossible states.
- Deterministic, isolated tests with no real e-shop calls, credentials, wall-clock dependence or network requirements.
- No panics on malformed external research text, no unguarded `unwrap()` on input boundaries, and no conflation of parsing success with trust.
- Correctness at uncertainty boundaries over unnecessary abstraction or premature feature count.
- Clear separations that do not force the later Axum/Askama/SQLite/HTML choice, while not pretending that all frameworks are already selected.
- Professional README developer entry, licensing status described accurately, no unsupported product claims or placeholder badge theater.
- A reviewable commit with no unrelated modified files, generated secrets, private paths, screenshots or binary artifacts.

These are success criteria to refine through planning, not permission to expand the whole or to install tools on NUC.

## 7. Suggested acceptance matrix and negative evidence

| Risk/feature | Bounded evidence the Planner should require |
|---|---|
| Builds on supported target | Locally observed Rust version; `cargo build`/`cargo test`, not merely authored code |
| Core semantics | Tests clearly derived from accepted contract with section/case mapping |
| Language distinction | Slovak and Czech never merged by website locale or spelling similarity |
| Positive verification | At exactly observation + 24h label becomes stale; failed recheck suppresses eligibility; unsupported agent-only stock cannot qualify |
| Access vs availability | 429/CAPTCHA/404 cannot become invented out-of-stock claim |
| Provenance/immutable observation | Temporal state not overwritten merely because newer/older records arrive, for whichever subset is implemented |
| Future input safety | No executable instruction from untrusted text; absence of a full importer is **explicitly** marked deferred |
| Repository integrity | Exact expected diff; unchanged AP gitlink and managed integration; strict `ap doctor` plus Rust checks |
| Public Git closure | Authorization-specific commit/push/readback; no force push; direct current public ref verification, or honest limitation |
| Scope fidelity | No UI, NUC, Hermes, screenshot retention, auth or unrelated category implementation slipped into foundation |

For E1/E2 risk classification, independence and correction budgets, use the pinned AP rather than assuming all software acceptance is identical to the preceding docs-only E1 work.

## 8. Residual risks and decisions to surface, not decide by handout

1. **Published branch uncertainty:** upstream exact immutable commit observation succeeded, but present remote HEAD equality was not independently established. Resolve during Stage 1.
2. **Rust toolchain, crate topology, MSRV/edition:** not previously selected; Cooperator decision may be needed if it becomes project policy.
3. **Storage decision:** SQLite and physical schema remain open; choose only with implementation-planning evidence and documented impact.
4. **No CI yet:** CI may be a separate bounded slice after executable tests exist. Do not build a broad release infrastructure now.
5. **Public license/community docs:** intentionally deferred; don't add a license or promise as a developer convenience.
6. **24-hour rule and review model:** accepted product policy; faithfully implement a subset, or revise via separately approved contract evolution. Do not weaken it by simplifying enum labels.
7. **No screenshot rights/storage policy:** future evidence gallery remains conceptual; do not collect or ship screenshot files now.
8. **Owner scope without accounts:** owner-specific semantics are accepted; implementing personal data/account scopes is not.
9. **NUC and FrameNest coexistence:** no host state verified; local experiments do not imply production safety or sudo rights. Deployment belongs to a later whole.
10. **AP evolution proposal in parallel:** upstream has prepared a separate handout proposing closure-driven Master orchestration. It is **not** current AP authority and does not affect the immutable BookRadar pin unless a separately authorized AP update is accepted and deliberately adopted.

## 9. Readiness review and exact next action

| Review area | Status |
|---|---|
| Predecessor logical-whole closure | PASS as recorded, historical E1 evidence |
| Accepted domain semantics and ADR discovery | PASS at immutable commit, personally inspected by upstream |
| Current public `main` / current local checkout | NOT YET REVALIDATED for the successor; must read back |
| Cooperator's next whole intent | Rust foundation is the evidence-backed Master recommendation; final material decisions remain Cooperator-owned |
| Active mutation and Worker sessions | UNKNOWN outside the supplied closure; ask/reconcile as needed |
| Security / host / provider boundaries | PASS for no host/provider operations planned |
| First Planner readiness | PASS **after** repository/current-state revalidation and objective reconciliation |
| Implementation readiness | NOT GRANTED; requires separate Planner report, decision gate and complete mutation grant |

**Next action for the per-whole Orchestrator:** open this exact handout, read the pinned AP and current BookRadar root instructions, verify live repository state read-only, record handout revalidation in `00_notes.md` when the activated trace permits, and issue the **first native Plan Mode Worker prompt** solely for designing the minimal Rust foundation slice. Do not request the upstream Master to write implementation instructions or to accept the Worker result.

## 10. Artifact lifecycle and return edge

- **Class:** retained opening continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to governing AP and current BookRadar semantic contract.
- **Consumer:** fresh per-whole Orchestrator, its initial Planner, eventual upstream Master upon closure.
- **Discoverability:** exact Meta location, predecessor closure, canonical BookRadar URLs and AP pin above.
- **Retention:** retain through this whole and archive after closure; material correction after opening is a separately named successor handout with predecessor/supersession links.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup decision.
- **Expected return to Master:** a truthful `xx_closure.md` with exact published commit and evidence classification; completed scope; explicit non-achievements; current contract and AP pin; residual risks; recommended next logical whole(s); no implied successor grant.

**Final invariant:** Build from the accepted semantic contract, not from excitement about frameworks. One small Rust foundation, one accountable per-whole Orchestrator, fresh bounded Worker grants, independent evidence, and no cross-project or host side effects.

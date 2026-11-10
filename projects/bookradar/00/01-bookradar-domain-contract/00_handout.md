# BookRadar — Opening Handout: `bookradar-domain-contract`

**Artifact:** `projects/bookradar/00/01-bookradar-domain-contract/00_handout.md`  
**Kind:** Opening continuity and decision-context handout for the next bounded logical whole. This is **not** a Worker prompt, approved implementation plan, ADR, authorization, acceptance record, or closure.  
**Authored by:** ORCHESTRATOR (ChatOrchestrator access profile), 2026-11-10.  
**Mechanical preparation:** ORCHESTRATOR-generated downloadable Markdown; placement in the Cooperator's local Meta checkout and Meta Git archival are separate actions owned by the appropriate authorized actor.  
**Predecessor:** `projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md` (closed preceding logical whole; this is not a handout in the present whole).  
**Prior handouts in this whole:** none.  
**Capability profile: ChatOrchestrator**  
**Orchestrator session scope:** `logical-whole`  
**Logical whole identity:** `bookradar-domain-contract`  
**Current AP phase:** Opening / pre-Planner read-only orchestration preparation.  
**Restoration classification:** **PASS for bounded first-Planner preparation**, with mutable public branch and local checkout state requiring fresh readback before a grant. **Not** implementation or deployment readiness.  
**Authority:** Historical continuity only. No repository, Git, Meta, filesystem, provider, host, SSH, sudo, security, deployment, publication, acceptance, or closure grant.

## 1. Selection and reason for this logical whole

**Cooperator direction:** Continue BookRadar after completed AP bootstrap; the ChatOrchestrator is asked to recommend/select the next logical whole and produce its opening handout rather than stop at a recommendation. This handout records that selected *planning-preparation route*. Any still-material product or architecture trade-off stays with the COOPERATOR under governing AP RF-01.

**Next logical whole:** `bookradar-domain-contract`.

**Single bounded objective:** Produce and obtain review of a **durable, implementation-neutral product-domain contract**, with only the minimum necessary, decision-backed ADRs, for identifying physical books and particular Slovak-language editions, tracking changing sale offers, retaining evidence and research provenance, and representing a user's watchlist and purchased collection. Define the boundary by which fallible, potentially hostile Hermes/Playwright research becomes validated application knowledge. Make the contract usable by a later Rust implementation without building Rust code now.

**Why now:** The prior logical whole explicitly deferred all product-domain decisions. Starting a database or user-facing Rust application first would prematurely encode ambiguous notions of “book”, “edition”, “available” and “verified”; their later correction risks destructive migrations and misleading user-facing claims. The bounded semantic contract is the cheapest next dependency before a Rust foundation.

**Outcome sought, not yet granted:** A compact, accepted repository-owned domain specification and focused ADR(s) describing critical identity, provenance and trust-boundary decisions, with worked examples, invariants and explicit deferrals. The first Worker only plans these changes. Any documentation writes, commits and push require a distinct later implementation grant.

**Out of scope:** Rust source, Cargo/crate/framework selection, physical SQLite schema or migration, UI implementation/design-system build, authentication or multi-user implementation, API endpoints, scraping software, Hermes configuration/skills updates, MCP changes, production dataset import, cron/gateway installation, NUC SSH/sudo/service/deployment, public exposure, CI setup, security/privacy/license policy commitments, or broad product roadmap creation. Do not turn this into an architecture-of-everything task.

## 2. Governing authority and source precedence

1. **Governing immutable AP** for BookRadar: `.ap` gitlink at `d7023cf037f6d17885c3ede5c04812c61640da50`, as reported in the accepted bootstrap and public commit. Normative source: [pinned AP.md](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/AP.md). Relevant operational/structural projections: [AP_ORCHESTRATOR.md](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/AP_ORCHESTRATOR.md), [AP_WORKER.md](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/AP_WORKER.md), [PROMPT_CONTRACTS.md](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/PROMPT_CONTRACTS.md), and on artifact work [ARTIFACT_LIFECYCLE.md](https://github.com/cisarik/ap/blob/d7023cf037f6d17885c3ede5c04812c61640da50/ARTIFACT_LIFECYCLE.md). The project gitlink, not AP's moving `main`, selects meaning.
2. **Canonical project repository:** [cisarik/bookradar](https://github.com/cisarik/bookradar), its committed root `AGENTS.md`, its project-owned accepted decisions, and independently checked public Git state.
3. **Current COOPERATOR-owned material decisions**, reconciled with the above.
4. **Predecessor closure** and accepted evidence: [Meta closure](https://github.com/cisarik/meta/blob/main/projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md) and [bootstrap commit](https://github.com/cisarik/bookradar/commit/12864ac874d74c562e22243bd622bd2729dfdaca). Historical evidence, not task authority.
5. **Meta archive conventions:** [cisarik/meta README](https://github.com/cisarik/meta/blob/main/README.md). Meta is selective historical trace, not the domain source of truth or another live AP.

Read project-root `AGENTS.md` and the pin-appropriate AP minimum-reading spine before the first Worker exchange. If any source has advanced or conflicts, classify it honestly; do not repair history by rewriting the predecessor or treating a past report as a current grant. No AP upgrade is selected or authorized.

## 3. Closed preceding boundary: verified baseline and limitations

The preceding whole, `bookradar-ap-bootstrap`, is **closed-by-ORCHESTRATOR / acceptance-PASS**. Its closure records:

- Public root commit on `main`: `12864ac874d74c562e22243bd622bd2729dfdaca`, subject `docs: adopt analytic programming`.
- Root tree: `c3dda5007bf66f19f18d3016260018f72eead8ba`; committed paths only `.ap`, `.gitmodules`, `AGENTS.md`, `README.md`.
- Immutable `.ap` gitlink: `d7023cf037f6d17885c3ede5c04812c61640da50`; expected detached pin.
- Strict `./.ap/ap doctor`: PASS in the predecessor's local acceptance readback; clean superproject/submodule and public ref equality were also reported there.
- **No Rust implementation, schema, ADR, license, CI, or deployment** was delivered by that whole.

**Independent present-turn observations (2026-11-10):** The exact public bootstrap commit page exists and shows the four-entry tree and `.ap` gitlink; public raw `main/README.md` still describes initial bootstrap/no application, while `main/AGENTS.md` has only the managed AP section. The raw `main` file contents are observable, but this tool route **did not independently retrieve the current `refs/heads/main` SHA or symbolic HEAD**. Therefore record **`public branch state not directly observed`** for current-branch identity; predecessor closure's public-ref readback is historical, not a substitute for a fresh pre-write `git ls-remote`/equivalent check. A generic GitHub repository landing page inconsistently rendered “empty”; prefer the exact commit and raw committed files for the specific claims they establish, and do not use the stale landing-page statement as evidence that bootstrap disappeared.

**Not observed by this ChatOrchestrator:** Current local checkout paths, clean/dirty index, uncommitted owner work, branch/remotes, SSH identities, NUC state, running Worker sessions outside this conversation, or newer unpublished commits. Planning begins with read-only fact gathering, not assumptions.

**Closure limitations retained, not reopened:** Fresh clone was not tested; no independent acceptance was required for E1; project-owned closure signal not declared; license and public collaboration policies deferred; CI/toolchain formatting/release policies deferred. No upgrade ledger is activated or declared in the root `AGENTS.md` currently observed. Do not create one from inference.

## 4. Accepted product intent and non-decisions

### Confirmed product direction

- **BookRadar** is a public Rust project, initially focused on researching and monitoring **physical books in the Slovak language**, especially rare/used editions and their sale offers; it must not silently substitute Czech for Slovak editions.
- The product should eventually support author filtering, watched titles/editions, a personal library of purchased books, price-history views, evidence/screenshot browsing, and manually requested research.
- The UI goal is a polished, accessible, responsive, user-friendly modern presentation with restrained dark/Matrix-terminal green accents, readable typography, clear verification and error states. This whole preserves those constraints but does not produce the UI.
- The intended development environment includes a personal Ubuntu NUC and future research via Hermes Agent (subagents, Playwright MCP, scheduling); those integrations are **future boundaries** and are not prerequisites for a semantic model.
- The public repository should be approachable by future collaborators. No license, contribution promise, privacy policy, public API stability or security-response commitment has yet been selected.
- The ChatOrchestrator remains read-only; specific later Worker prompts may authorize BookRadar commit/push, but **Meta Git remains COOPERATOR-owned** under the presently activated ChatOrchestrator convention.

### Reported prototype evidence, not approved architecture

The COOPERATOR reported that a local Hermes prototype searched for Michael Newton books, used two subagents and Playwright MCP, produced a Markdown report, and saved a screenshot for a second-hand Slovak edition. This demonstrates desired research workflow, **not** that a given listing remains available or that any result has been independently validated for insertion into BookRadar. A previously observed price is a historical claim, never an unqualified current price.

### Candidate models and technologies, **not accepted ADRs**

- `Book/Work`, `Edition`, `Offer`, `Observation`, `Evidence`, `Watch`, `LibraryEntry`, possibly `Author`, `ResearchRun` and `Source` are **candidate concepts**, not preapproved entity/table names or multiplicity.
- SQLite, Axum, Askama, HTML/CSS-centric UI, JSON exchange, stand-alone Rust binary, private Tailscale access, and a separate Hermes scheduler/importer remain proposals.
- The domain plan must evaluate a narrow, future-proof contract, not lock in physical storage, provider SDKs, agent tooling or a particular web framework.

## 5. Domain questions for the first Planner to resolve, not predetermine

The Planner must inspect the actual repository and propose **one minimal documentation implementation slice** that answers the following, with examples and explicit alternatives where a material decision belongs to the COOPERATOR:

1. **Identity and granularity:** Distinguish intellectual work/title, language-specific published edition or printing, sellable copy/lot and merchant offer. Define when two records are the same vs distinct. Deal explicitly with missing, incorrect, multiple, hyphenated or reissued ISBN-10/ISBN-13, publisher/year ambiguity, title transliteration and Slovak vs Czech language evidence. Do not make ISBN a mandatory universal primary identifier.
2. **Offer vs observed state:** Separate stable listing identity from an observation at a point in time. Define availability states (`confirmed`, `unavailable`, `unverified`, etc. only as proposed vocabulary), verification method, observation freshness/staleness, rechecks, removal, temporary HTTP 429/CAPTCHA and “product page exists” vs “buyable copy exists”. Never turn access failure into an out-of-stock claim.
3. **Pricing and second-hand specifics:** Capture monetary value with currency and source; distinguish price per copy from shipping/fees, condition, quantity, reservation, seller identity and offer changes. Require a representation that avoids silently conflating prices across currencies or stale observations; do not build a price chart yet.
4. **Evidence and provenance:** Define source URL and source identity, accessed/observed timestamps including offset, method (agent, browser, manual), uncertainty/confidence rationale, traceable screenshot/evidence reference and optionally integrity metadata. Avoid treating a cookie-obscured screenshot as conclusive proof. Address redirects, disappeared listings and evidence retention/rights as explicit boundaries, not invented policies.
5. **Untrusted AI research:** Distinguish raw, potentially untrusted Hermes/Playwright assertions from validated, reviewable application observations. Propose input contract versioning, schema/invariant validation, idempotency/deduplication, partial failure and quarantining, provenance of agent/model/skill/run, and behavior for contradictory or malformed findings. An LLM claim alone must not imply verified stock.
6. **Personal-state separation:** Clarify `watchlist` vs `owned/purchased library` vs public/catalog facts. Avoid encoding one person's owned books as globally owned. Keep a future multi-user ownership/privacy boundary possible without implementing accounts or committing actual personal data.
7. **User-facing truth semantics:** Define a small set of displayable, honest labels and their evidence requirements (e.g. “currently verified”, “last observed”, “unverified”, “sold out”) and uncertainty wording. Avoid accidental green “available” badges for historical listings. Accessible UI semantics and translation/i18n requirements may be noted, not designed in detail.
8. **Documentation ownership/ADR scope:** Propose one durable domain contract and the smallest number of focused ADRs needed to record irreversible semantic choices and alternatives. Prefer minimal, navigable public documents with explicit owner, lifecycle and links. Keep project-root README edits minimal and justified; do not mix speculative runtime decisions into semantic ADRs.
9. **Validation/evolution:** Recommend deterministic examples or fixture cases to test identity, contradictory offers, stale observations, absent ISBN, Slovak/Czech confusion, incomplete screenshot, access blocks and repeated imports. Define how future schema/API changes preserve compatibility conceptually, without writing migrations or choosing crates.
10. **Decision boundaries:** Separate safe modeling recommendations from material product questions requiring explicit COOPERATOR approval, especially meaning of “verified”, personal-data handling, screenshot retention and public sharing, and whether cross-domain monitoring is in scope. Do not silently turn BookRadar into a universal commerce watcher.

**Required planning quality:** Give a precise proposed file inventory, purpose and minimal contents; invariants and edge-case matrix; alternatives and rationales; an implementable ordered docs-only work sketch; validation and reviewer evidence; explicit stop conditions; residual risks and Cooperator decision requests. Avoid boilerplate, over-normalized speculative schemas, dozens of ADRs, or generated scaffolding. A plan is not an accepted decision.

## 6. Requested completion and acceptance boundary for the whole

The later *authorized* implementation should leave **repository-owned, reviewable semantic documentation**, not a pseudo-database. Candidate shape (Planner may improve it):

- a readable domain specification describing concepts, invariants and lifecycle with a concise glossary/relationship diagram;
- one or a small number of focused ADRs for accepted identity/provenance/trust-boundary decisions, with status, alternatives, consequences and explicit deferments;
- realistic, non-sensitive worked cases anchored in book discovery, but not in unverifiable live-stock assertions;
- an evolution and validation checklist sufficient for the next Rust foundation whole to implement without guessing the meaning of book, edition, offer and observation.

**Acceptance criteria to propose:** Consistent identity rules, language/edition separation, no fabricated availability, timestamp/provenance discipline, safe failure semantics for 429/blocked data, explicit ownership boundary, versionable ingestion contract, intelligible examples, no extra runtime work, no secrets or unnecessary real user data, public document discoverability, correct AP artifact lifecycle, and verified Git provenance. Evidence should be proportionate to docs/domain risk; no pretend implementation tests. Subjective product choices and residual risk are COOPERATOR-owned.

**Closure is not automatic:** Plan acceptance, any required COOPERATOR decisions, a new implementation grant, review/validation, (if authorized) BookRadar commit/push with public readback, proportionate acceptance, and the ORCHESTRATOR's closure decision must occur before calling the whole closed. An accepted plan does not itself authorize implementation.

## 7. Meta trace and exchange identities

**Activated archive layout:** `projects/<project>/<archive-sequence>/<logical-whole-sequence>-<identity>/`. The predecessor used archive group `00`, logical-whole sequence `00`. This next whole uses the **same archive group** and next logical-whole ordering key, hence:

`projects/bookradar/00/01-bookradar-domain-contract/`

Archive groups are **ordering groups, not dates**, and no rollover is required. A separate `01` archive group would be an unselected storage convention change.

- This handout: `00_handout.md`; opening `00_notes.md` is separately required by the activated Meta convention. Notes are ORCHESTRATOR-authored; a named authorized persister may store exact entries. They are not a parallel authority or chat transcript.
- First formal exchange: **logical whole `bookradar-domain-contract`, Worker session `01`, Worker exchange `01`**, phase `planning`, initial native Plan Mode.
- First storage pair after report: `01_planning_00.md` and `01_report_00.md`. Meta `_00` is the local zero-based storage index for AP exchange `01`, not Worker exchange `00`.
- The standard terminal report begins **exactly** `### Report for ORCHESTRATOR_CHAT` and echoes the full current coordinates; the client-native plan UI is not a report.
- A complete prompt/report pair is first Git-added to Meta **together only after the report exists**; do not precommit a prompt alone or fabricate a missing report. Maintain exact historical content and the COOPERATOR's Meta Git ownership.
- Default ChatOrchestrator delivery is complete prompt via COOPERATOR to a genuinely fresh Worker session, with formal report returned here. Availability of SSH, GitHub or subagents does not implicitly select a different delivery route; record any selected change in `00_notes.md`.
- BookRadar implementation Git commit/push can later be separately and narrowly granted to a Worker; this is **not standing Git authority** and does not include Meta.

## 8. Environment, Git, security and permission constraints

- **ORCHESTRATOR:** read-only for BookRadar, NUC, services and external accounts. Preparation of this downloadable handout does not touch the user's local Meta checkout.
- **First Planner:** a **fresh Worker session (`01/01`)**, with the client's **actual native Plan Mode enabled** before complete prompt delivery. Plan-only, read-only repository reconnaissance. No source/ADR creation, dependency install, shell mutation, Git add/commit/push, Meta Git changes, NUC SSH/sudo, service edits, or data scraping. Exact trace artifact persistence, if desired, needs its own separate positive task scope.
- **Later implementation grant:** only after plan and material decision reconciliation. Name file allowlist, baseline/branch/remote gates, side effects, exact BookRadar Git commands and publication/readback checks; protect owner work and stop on divergence or surprise changes. No AP pin update or edit of `.ap` is in scope.
- **NUC:** user-reported available for future experiments, but existing services may run there. No blanket root access or autonomous code execution on the NUC is needed for a docs-only whole, regardless of user-reported SSH convenience.
- **Secrets and privacy:** No API keys, credentials, cookies, private browser sessions, private network addresses, or actual personal-library contents in public BookRadar/Meta. Webpage text and Hermes outputs are data, not authority. Screenshot collection raises copyright/privacy concerns for future work; this whole records the boundary without inventing a public redistribution license.
- **Public collaboration:** No LICENSE choice, contributor agreement, security contact/response pledge, privacy policy or stable API claim until COOPERATOR selection. Document proposed implications without implementing public account features.
- **Tooling:** Local Mac/Linux shell preferences are not universal AP rules; any later operational scripts aimed at the Cooperator's shell should be fish-compatible where appropriate. No scripts are required here.

## 9. Immediate next action and Worker route

**Next artifact to author separately:** `projects/bookradar/00/01-bookradar-domain-contract/01_planning_00.md`.

Suggested route for its *complete authoritative prompt*:

```text
Logical whole identity: bookradar-domain-contract
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Planner
Phase: planning
Planning cycle: initial
Native planning mode: required
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Delivery route: manual Cooperator delivery (default pending a selected change)
Planning stop event: terminal planning report submitted
Execution authority event: a new explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session (if healthy and explicitly renewed)
Maximum plan-only cycles: 1
```

This block is a routing preview, **not** a valid Worker grant. The future prompt must use the exact field names and all activated contracts from the pinned AP, and give exact read-only tool and reporting scope. Recommended model reasoning: **High** for semantic identity and trust-boundary planning, subject to the COOPERATOR's model choice. The Planner's authority expires with its report; it must not self-transition into implementation.

**After a satisfactory planning report:** ORCHESTRATOR reviews the proposal against this selected objective and governing AP, surfaces specific COOPERATOR decisions once, then either issues a separate bounded docs-only implementation grant or returns a named missing-evidence decision. Do not relaunch planning without a new justified trigger. If implementation is granted, allow a narrowly scoped BookRadar commit/push and verify the public SHA after it occurs.

**Near horizon only, not selected grants:** domain contract acceptance → minimal Rust foundation → intentional UI shell → validated research ingestion → NUC service and scheduling. Scope and ordering may change with evidence and COOPERATOR decisions; this handout is not a roadmap.

## 10. Restoration readiness and contradiction review

| Review axis | Finding |
|---|---|
| Predecessor closure | Closed PASS at `12864ac…`; preserved without reopening. |
| Source of truth | Immutable pinned AP is normative; BookRadar project is canonical; Meta closure is historical. |
| Public state | Exact bootstrap commit and current raw README/AGENTS contents observed; current branch ref SHA and local checkout **not directly observed**, must be rechecked before any write. |
| Strategic direction | Rust + physical Slovak-language books + provenance + future polished UI preserved; no framework/DB/hosting assumed accepted. |
| Scope | One docs-only semantic whole; no Rust, NUC, browser/scraping, deployment or Git mutation at planning stage. |
| Authority | COOPERATOR retains material decisions; handout and accepted predecessor do not grant Worker authority. |
| Active Worker/mutation | None reported as active in this conversation after preceding closure; outside-session activity not independently knowable. Fresh session required. |
| Security/privacy | Untrusted research, personal ownership, screenshots and public project boundaries explicitly identified; no secret or host privileges granted. |
| Trace | Correct next Meta logical-whole sequence and first Worker exchange; `00_notes.md` remains separate. |
| Next-step executability | Complete first Plan-Mode prompt can be prepared using read-only checkout evidence; unresolved mutable Git facts become explicit gates. |

**Readiness verdict: PASS for issuing a complete, bounded, read-only first Planner prompt after its actual client/delivery and repository-evidence checks.** This does not certify implementation, current branch SHA, published domain policy, or NUC readiness.

### Artifact lifecycle

- **AP relationship:** historical continuity evidence under the governing AP; Meta-local trace, not canonical semantics.
- **Lifecycle class:** retained historical evidence / opening handout.
- **Authority:** non-authorizing; subordinate to the immutable AP, current canonical repository, current COOPERATOR decisions and later accepted project-owned specifications.
- **Consumers:** ChatOrchestrator preparing the first Planner exchange, future successor Orchestrators and Workers as read-only context.
- **Discoverability:** exact Meta path above plus predecessor closure/public commit locators.
- **Retention:** retain through this logical whole and in Meta history after closure. Do not silently edit once used; material revisions take a successor handout with predecessor/supersession markers.
- **Cleanup owner:** COOPERATOR as Meta archive Git owner under a separately valid cleanup decision; no automatic deletion.

---

**Boundary reminder:** This opening handout preserves the successor's purpose and evidence boundaries. It does not issue `01/01`, pre-answer the Planner, approve an ADR, grant BookRadar or Meta writes, authorize NUC operations, or close `bookradar-domain-contract`.

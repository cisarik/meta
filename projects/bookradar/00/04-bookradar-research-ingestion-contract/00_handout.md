# BookRadar — Opening Handout: `bookradar-research-ingestion-contract`

**Artifact:** `projects/bookradar/00/04-bookradar-research-ingestion-contract/00_handout.md`
**Kind:** provisional opening continuity, domain-dependency and decision-context handout for a fresh per-whole Orchestrator. **Not** a Worker prompt, permission grant, implementation plan, acceptance, publication or closure.
**Authored by:** upstream read-only ChatOrchestrator (development-run / Master scope), 2026-11-11.
**Predecessor:** `projects/bookradar/00/03-bookradar-persistence-and-history-slice/01_closure.md` (`closed-by-ORCHESTRATOR`; acceptance PASS; publication PASS).
**Earlier closed wholes:** `projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md`; `projects/bookradar/00/01-bookradar-domain-contract/01_closure_03.md`; `projects/bookradar/00/02-bookradar-rust-foundation/01_closure.md`.
**Logical-whole candidate identity:** `bookradar-research-ingestion-contract`.
**Handout status:** provisional until the fresh per-whole Orchestrator reconciles the current repository, Cooperator selection and activated Meta trace. Do not modify this frozen handout in place after opening; material changes use a successor handout under the AP/Meta handoff sequence.
**Intended successor capability profile:** `Orchestrator` (direct project checkout), with `Orchestrator session scope: logical-whole`.
**Upstream author access profile/scope:** `ChatOrchestrator` / `development-run`.
**Restoration classification:** PASS for read-only preparation of the first Planner on the accepted baseline; current public `main`, local checkout, tool availability and storage state **must be independently revalidated** before any Worker grant. Not implementation readiness.
**Authority:** zero. Neither this handout nor the predecessor closure grants Git, filesystem, SSH, host, dependency installation, implementation, acceptance, publication or Meta mutation.

## 0. Selection rationale and one bounded objective

BookRadar now has an accepted, published persistence/history Proof of Concept:

- the dependency-free `bookradar-core` verification kernel;
- a local `bookradar-store` crate with SQLite schema v1, append-only observations/reviews and deterministic current/history selection;
- a four-command synthetic `bookradar-poc` binary;
- 45 passing tests (17 core + 28 store/history/CLI);
- accepted ADR 0004 and a public commit.

The next dependency before a live Hermes/Playwright workflow or NUC deployment is the **trust boundary for untrusted research output**. A well-formed agent report, Markdown file, JSON envelope or screenshot reference must not become a trusted stock fact merely because it is structurally valid. The product contract already defines the required semantics; this whole should make a selected, testable part executable.

**Single objective proposed for this whole:** establish one minimal, executable, versioned **untrusted research ingestion contract/pipeline** that validates structural and invariant requirements, preserves producer/run/finding provenance, quarantines unsupported or malformed input, handles replay and conflicting payloads deterministically, and integrates with the accepted core/store only through explicitly assessed observations or candidates. It must never automatically promote agent output to a verified stock state.

The first Planner must choose the smallest useful vertical/horizontal slice. Do **not** attempt a live Hermes/Playwright integration, a full research platform, a UI, a NUC deployment, a complete catalog schema or an all-purpose importer in this whole.

Why this precedes UI and NUC work:

- Hermes/Playwright output is untrusted data; the contract must be executable before a live adapter is connected.
- Replay, quarantine, partial-run results and contradictory findings need deterministic behavior and tests before repeated research runs exist.
- A small importer/validator with synthetic fixtures can be reviewed and tested without real retail data, screenshots or network access.
- The next whole should create a durable trust boundary, not a speculative ingestion framework.

Alternative next wholes considered but deferred: `bookradar-ui-shell` (visual learning can use synthetic/store-backed data) and `bookradar-test-hardening-and-ci` (quality follow-up, not the trust boundary). Selection should be revisited only for fresh material evidence or COOPERATOR redirection.

## 1. Baseline and source precedence

**Canonical repository:** `https://github.com/cisarik/bookradar`
**Public branch:** `main`
**Published commit at handout authoring:** `c93f5262ca27050922cc658424c298913852eaff` (`feat: add persistent observation history PoC`)
**Parent:** `bd23b08cd315a7b3c7a549479db59cbe6ad2adce`
**Tree:** `b2ad12353723009944521c15ac2016970337c1df`
**Pinned AP:** `.ap` gitlink `d7023cf037f6d17885c3ede5c04812c61640da50` (immutable; detached expected checkout)
**Accepted product contract:** `docs/domain-contract.md`, revision 1, accepted 2026-11-10
**Accepted ADRs:** `docs/adr/0001-book-edition-and-offer-identity.md`, `docs/adr/0002-evidence-and-research-trust-boundary.md`, `docs/adr/0003-rust-domain-foundation.md`, `docs/adr/0004-local-persistence-and-history.md`
**Predecessor closure:** `projects/bookradar/00/03-bookradar-persistence-and-history-slice/01_closure.md`, SHA-256 `4811b847eac398a4ff735a1a54b2ba8fcb5f75fa4ed9868935ef98b2965c0dc9`

Read in precedence order:

1. Project root `AGENTS.md` and the immutable AP at the gitlink: `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, and later `.ap/PROMPT_CONTRACTS.md`, `.ap/AP_WORKER.md` as routed.
2. Current public `main` and the actual local checkout; verify refs, ancestry, cleanliness, submodule and toolchain independently.
3. Accepted domain contract and ADRs 0001–0004.
4. Predecessor closure and the accepted planning/acceptance/publication records as historical evidence.
5. This handout as provisional, non-authorizing context.

The predecessor closure records a successful local E2 persistence/history slice and a direct public publication. It also records process residuals: duplicate `02/01` implementation reports, a late `02_rereport_00.md` under the Kronika trace, and a BLOCKED duplicate publication report. Those are trace-hygiene evidence, not current authority. The successor must not repeat the duplicate-worker pattern: one accountable Worker workstream, explicit session identity and one active writer.

At authoring, the upstream Orchestrator observed public `refs/heads/main` and symbolic `HEAD` at `c93f526…`, local `main`/`HEAD`/`origin/main` at the same commit, a clean worktree, `.ap` detached and clean at `d7023cf…`, and strict `ap doctor` PASS. The successor must revalidate these facts before any grant; do not infer them from this handout.

## 2. Accepted state and the ingestion gap

Current repository state at authoring:

- `bookradar-core` is a dependency-free library with 17 tests; it evaluates one supplied observation and explicit assessment context.
- `bookradar-store` is a dependent crate with SQLite schema v1, append-only observations/reviews, deterministic current/history selection and a synthetic `bookradar-poc` binary.
- 28 new store/history/CLI tests pass; ADR 0004 is accepted; README describes the local PoC and its limits.
- No research ingestion, envelope format, producer/run/finding identity, quarantine, replay log, live Hermes/Playwright adapter, UI, screenshots, accounts or deployment exists.
- The store schema v1 has no research-run, finding, envelope, quarantine or import-replay table. Adding those may require schema v2/migration, a separate append-only admission log, or a deliberately non-persistent validator first; **none is preapproved**.

The accepted domain contract's research boundary requires, at minimum:

- untrusted research assertions pass structural and invariant validation before becoming candidates;
- structural validity never establishes truth, reviewer approval or verified stock;
- unsupported versions and malformed envelopes are rejected/quarantined without guessing;
- producer-scoped run/finding identity, source/listing references, candidate subject identity, timestamps, asserted facts, evidence references, uncertainty and available producer provenance are carried;
- agent, model, skill/tool versions and run context are recorded when supplied; unavailable values remain explicitly unknown;
- partial-run outcomes account for valid, rejected and quarantined findings;
- identical replay of the same producer/run/finding is a no-op; different content under that identity is a conflict requiring reconciliation;
- contradictions are retained and marked disputed, not resolved by import order, confidence or majority;
- later import of older evidence does not roll observed reality backward;
- research text, URLs, file references and embedded instructions are data, never commands;
- agent-only verified-stock claims, locale-inferred Slovak language, identity merges based only on ISBN/title, access failures as stock exhaustion, claimed screenshot rights and ownership inferred from watchlists are never automatically accepted.

## 3. What the first Planner must evaluate

Ask a fresh Planner to inspect the current repository and propose **one minimal executable slice** with evidence for these decisions. It must not silently promote candidate formats, schemas or crates to accepted architecture.

1. **As-found state.** Verify the current public/local commit, AP pin, clean checkout, store schema, tests, toolchain and any Meta trace. State what is genuinely implemented versus deferred.
2. **Functional slice and runnable path.** Choose the smallest end-to-end ingestion slice that can be demonstrated locally with synthetic fixtures. Evaluate a library validator plus a small importer/CLI; a runnable path is preferred if it materially proves admission, quarantine and replay behavior. No live Hermes/Playwright or real retail data.
3. **Input contract and versioning.** Propose a versioned semantic envelope and a concrete minimal representation. JSON is a candidate, not a mandate. Compare dependency costs, serialization/deserialization, unknown-field behavior, version rejection and testability. Do not select a format merely because it is convenient.
4. **Identity and provenance.** Define producer-scoped run and finding identity, optional source/listing references, candidate subject references, timestamps (observation/access/capture/ingestion and offsets or unknown), asserted facts, evidence references, uncertainty, agent/model/skill/tool versions and producer context. Preserve unknown values explicitly; do not fabricate missing provenance.
5. **Admission and quarantine.** Define structural/invariant validation stages, rejection versus quarantine, partial-run accounting, duplicate-key behavior, unsupported version behavior and the point at which a finding becomes an application candidate. Passing validation must not imply truth or eligibility.
6. **Replay and conflict.** Define identical replay as a no-op, changed payload under the same identity as conflict/quarantine, and later/older import behavior. Decide whether this requires a durable envelope/finding table, a separate append-only log, or a smaller in-memory demonstration; compare migration, recovery and lock-in.
7. **Store/core integration.** Decide whether validated findings become `bookradar-store` observations, candidate records, review drafts or a separate research store. Preserve the accepted core policy kernel and schema v1 semantics; do not auto-approve or auto-verify. If a schema v2/migration is required, include exact migration, recovery, rollback and compatibility costs; no migration is preapproved.
8. **Tests and fixtures.** Derive deterministic synthetic fixtures from the contract:
   - malformed envelope, missing required field and unknown contract version;
   - identical replay no-op and altered-payload conflict;
   - partial valid/invalid findings and quarantine accounting;
   - agent-only stock claim not verified; structurally valid claim not truth;
   - source/listing/evidence provenance and unknown timestamps;
   - contradictory findings retained/disputed; older import does not roll back;
   - embedded instructions treated as data;
   - no network, wall clock, credentials or real data.
   State which of the contract's worked cases are executable and which remain deferred.
9. **Toolchain, dependencies and quality gates.** Keep Rust `1.99.1` and the existing workspace unless a justified change is required; use `$HOME/.cargo/bin` explicitly or a session-local PATH. Compare any new serialization/database crate by purpose, version policy and transitive/native cost. No dependency installation in planning. Propose build/test/fmt/clippy and fresh-store/clean-checkout evidence.
10. **ADR, README and public collaboration.** Add one implementation ADR only if a meaningful ingestion/storage choice is accepted (likely ADR 0005). Update README without selecting a license, contribution, privacy, security-response or support policy. Do not modify the accepted contract or ADRs 0001–0004.
11. **Acceptance and risk.** Propose a proportionate evidence tier; a durable schema migration or trust-boundary validator may justify E2/E3 and fresh independent acceptance. Name residual risks and Cooperator decisions. No live data, UI, NUC or deployment.
12. **Implementation path.** Propose exact paths, ordered stages, rollback, a small local demonstration, and the Git/publication boundary. No publication is granted by this handout.

## 4. Nonnegotiable boundaries

This whole does **not** authorize:

- live Hermes, Playwright, MCP, scraping, external APIs, real bookseller pages, cron, SSH, sudo, NUC installation, services, production or Tailscale ingress;
- real research payloads, screenshots, screenshot storage, personal data, accounts, purchases or login flows;
- auto-promotion of agent output to verified stock, auto-merged identity or auto-resolved conflicts;
- a UI, dashboard, API, authentication, public exposure or public API stability promise;
- a full catalog schema, price-history schema, owner/account schema or exhaustive migration of external datasets;
- a new license, contribution/security/privacy policy or support SLA without Cooperator decision;
- updates to `.ap`, the AP gitlink, other projects or Meta Git from a Worker;
- force push, rebased/rewritten published history, undocumented dependency installation, unsafe cleanup or privilege inference.

The positive authority in a later Worker grant must name exact paths, operations, formats, dependencies and Git boundaries. If the Planner proposes wider scope, hand material options to the Cooperator instead of treating them as approved.

## 5. Operating model for the fresh Orchestrator

**Stage 1 — read-only restoration.** Read the current root `AGENTS.md` and pinned AP, verify the public/local commit, parent/tree, `.ap` pin, clean state, current store schema/tests and toolchain, and compare the predecessor closure. Record the handout revalidation in the new whole’s `00_notes.md` when the activated trace permits. Do not infer current branch, worktree or Worker state from this handout.

**Stage 2 — reconcile one bounded objective with the COOPERATOR.** Present the restored state, the ingestion gap, material uncertainty and one evidence-backed recommendation. Preserve Cooperator ownership of input-format, storage/migration, dependency, trust-boundary, acceptance and publication choices.

**Initial Planner.** Assign a fresh Worker session `01`, exchange `01`, with **native Plan Mode required**, read-only repository inspection and a bounded implementation-planning report. The first exchange is not an implementation grant. Do not start a second implementation worker; one accountable workstream only.

**Later implementation.** After plan reconciliation and Cooperator decisions, issue a new self-contained grant with exact baseline, allowlist, format/schema/dependency decisions, tests, and separately named Git/publication authority. If the work introduces durable schema migration or a trust-boundary validator, use the risk-appropriate fresh acceptance route.

**Meta trace.** Preferred new directory: `projects/bookradar/00/04-bookradar-research-ingestion-contract/`, with `00_notes.md` on opening and this provisional `00_handout.md`. Worker exchange `01/01` is stored, when activated, as `01_planning_00.md` + `01_report_00.md`; later implementation or acceptance coordinates follow the actual route. Preserve the previous whole’s duplicate-report process residual: do not silently rewrite `02_rereport_00.md`; it should be moved/copied from the Kronika trace to the BookRadar trace under Cooperator Meta ownership.

## 6. Quality standard for the ingestion slice

A credible first slice should aspire to:

- a versioned, explicit research envelope with deterministic version rejection and a small dependency graph;
- explicit unknown/unavailable provenance rather than fabricated values;
- structural validation separated from truth, review and verified stock;
- no network, wall clock, credentials, real listings or screenshots in tests;
- deterministic replay, quarantine and conflict tests;
- no panics on malformed external text; no unguarded `unwrap()` on input boundaries;
- correct behavior at identity, timestamp, partial-run and older-import boundaries;
- a reviewable diff with no unrelated host, AP, UI, NUC or policy work;
- a professional README entry and an ADR only for a real durable choice;
- no unsupported claims that the whole validates real research or stock.

## 7. Suggested acceptance matrix and negative evidence

| Risk/feature | Bounded evidence the Planner should require |
|---|---|
| Builds on current baseline | Local Rust `1.99.1` toolchain and observed build/test, not authored code alone |
| Contract versioning | Unknown/malformed version rejected/quarantined with no guessed meaning |
| Structural validation ≠ truth | Valid agent-only stock claim remains unverified/non-eligible |
| Producer/run/finding identity | Exact identity retained; missing/unknown provenance explicit |
| Replay | Identical payload is a no-op; altered payload is conflict/quarantine |
| Partial run | Valid findings admitted and rejected/quarantined findings accounted |
| Evidence/provenance | Source/listing/evidence references and timestamps preserved; unknown offsets explicit |
| Contradictions | Disputed set retained; no import-order/confidence/majority resolution |
| Older import | Current interpretation does not roll backward merely because an older event arrived |
| Untrusted text | Embedded instructions remain data; no command execution or privilege |
| Store/migration | Exact schema/migration/recovery or explicit deferral; no silent data loss |
| Repository integrity | Exact diff; unchanged AP, core, accepted contract and earlier ADRs |
| Scope fidelity | No live Hermes/Playwright, UI, NUC, real data, auth or policy selection |

For E2/E3 classification, independence, correction budgets and storage-migration evidence, use the pinned AP; do not assume all ingestion acceptance is E1.

## 8. Residual risks and decisions to surface

1. **Current branch/worktree state:** public `main` and local state at handout authoring are evidence; the successor must revalidate and not infer absence of new commits.
2. **Input format and serialization:** JSON/serde, a custom format or another representation remains open; dependencies and opaque-field behavior matter.
3. **Persistence boundary:** schema v2/migration, a separate admission log, or a validator-only first slice remains open; migration/data preservation is material.
4. **Replay/conflict identity:** producer-scoped run/finding identity and conflict handling may require durable state not present in schema v1.
5. **Trust-boundary review:** structural validation, quarantine and review handoff are distinct; no auto-verification.
6. **No live Hermes/Playwright/NUC:** this whole must use synthetic fixtures; live integration belongs to a later, separately secured whole.
7. **No screenshots/personal data:** metadata/reference semantics only; no collection, retention or rights promise.
8. **License/CI/community policy:** intentionally deferred; do not add them as a developer convenience.
9. **Duplicate-worker/trace incident:** preserve the predecessor reports and avoid repeating duplicate sessions; one active writer and explicit coordinates.
10. **AP evolution proposal:** any separate AP/Meta handout is not current BookRadar authority; do not blend it into this pin.

## 9. Readiness review and exact next action

| Review area | Status |
|---|---|
| Predecessor closure | PASS as recorded; local E2 acceptance and direct publication evidence |
| Accepted domain semantics/ADRs | PASS at the immutable public commit and contract revision 1 |
| Current public `main` / local checkout | Observed at `c93f526…` during handout authoring; **must be independently revalidated** |
| Cooperator’s next whole intent | Research-ingestion contract is the evidence-backed recommendation; material choices remain Cooperator-owned |
| Active mutation / Worker sessions | None observed at handout authoring; successor must recheck |
| Security/host/provider boundaries | PASS for no live host, network or provider work planned |
| First Planner readiness | PASS **after** current-state revalidation and objective reconciliation |
| Implementation readiness | NOT GRANTED; requires Planner report, decision gate and complete mutation grant |

**Next action for the per-whole Orchestrator:** open this exact handout, read the pinned AP and current repository, verify public/local state read-only, record the handout revalidation in the new `00_notes.md` when the trace permits, reconcile the bounded objective with the COOPERATOR, and issue the **first native Plan Mode Worker prompt** solely for designing the minimal research-ingestion contract/pipeline. Do not ask the upstream Master to write implementation instructions or accept the Worker result.

## 10. Artifact lifecycle and return edge

- **Class:** retained opening continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to governing AP and the accepted domains contract.
- **Consumer:** fresh per-whole Orchestrator, its initial Planner, and the upstream Master upon closure.
- **Discoverability:** exact Meta location, predecessor closure, public commit URL, AP pin and contract revision above.
- **Retention:** retain through this whole and archive after closure; material correction after opening is a separately named successor handout with predecessor/supersession links.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup decision.
- **Expected return to Master:** a truthful `xx_closure.md` with exact public commit and evidence classification; completed scope; explicit non-achievements; current contract/AP pin; residual risks; recommended next logical whole(s); no implied successor grant.

**Final invariant:** Build the trust boundary before the live research adapter. One versioned, testable ingestion contract, one accountable Orchestrator, fresh bounded Worker grants, synthetic evidence, no live retail data, no auto-verification, and no cross-project or host side effects.

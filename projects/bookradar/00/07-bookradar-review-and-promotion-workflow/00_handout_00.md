# BookRadar — Opening Handout: `bookradar-review-and-promotion-workflow`

**Artifact:** `projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_handout_00.md`
**Local filesystem path:** `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_handout_00.md`
**Filename note:** The COOPERATOR expressly requested the filename `00_handout_00.md`. This is a named opening-handout exception to Meta's usual `00_handout.md`, not a Worker exchange and not a change to Meta's universal naming convention. The receiving Orchestrator must record this exception in the whole's `00_notes.md`, must not silently rename this file or create a second competing `00_handout.md`, and must treat its handoff-sequence position as `00` (so the closing artifact will be `01_closure.md`, or the next free handoff prefix if another handout intervenes).
**Kind:** provisional opening continuity, domain-dependency, and decision-context handout for a fresh per-whole Orchestrator. **Not** a Worker prompt, permission grant, implementation plan, acceptance, publication, or closure.
**Authored by:** outgoing per-whole ORCHESTRATOR (direct project checkout), 2026-11-13, under explicit COOPERATOR instruction. This is not a Master handoff and grants no authority.
**Predecessor:** `projects/bookradar/00/06-bookradar-ui-shell/01_closure.md` (`closed-by-ORCHESTRATOR`; implementation PASS, acceptance PASS with isolated Playwright/Chromium browser verification, publication PASS, CI run `43485796198` success), SHA-256 `77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f`.
**Current public/local baseline:** `2281982f7dae0ef1f582d294592c41281ba11b21` (`feat: add a local read-only UI shell`), parent `a2182302de73cb345b4b646993a1ad25d602555f`, tree `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`.
**Current public CI evidence:** workflow `verify`, run `43485796198` (<https://github.com/cisarik/bookradar/actions/runs/43485796198>), conclusion `success`, head SHA `2281982f7dae0ef1f582d294592c41281ba11b21`.
**Earlier closed wholes:**
- `projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md`
- `projects/bookradar/00/01-bookradar-domain-contract/01_closure_03.md`
- `projects/bookradar/00/02-bookradar-rust-foundation/01_closure.md`
- `projects/bookradar/00/03-bookradar-persistence-and-history-slice/01_closure.md`
- `projects/bookradar/00/04-bookradar-research-ingestion-contract/01_closure.md`
- `projects/bookradar/00/05-bookradar-test-hardening-and-ci/01_closure.md`
- `projects/bookradar/00/06-bookradar-ui-shell/01_closure.md`
**Logical-whole candidate identity:** `bookradar-review-and-promotion-workflow`.
Handout status: provisional
**Status basis:** provisional until the fresh per-whole Orchestrator reconciles the current repository, COOPERATOR selection, and activated Meta trace. Do not modify this frozen handout in place after opening; material changes use a successor handout under the AP/Meta handoff sequence.
**Intended successor capability profile:** `Orchestrator` (direct project checkout `/Users/agile/Projects/bookradar`), with `Orchestrator session scope: logical-whole`.
**Upstream author access profile/scope:** `Orchestrator` / `logical-whole` (outgoing session).
**Restoration classification:** PASS for read-only preparation of the first Planner on the observed baseline; current public `main`, local checkout, CI run, 94-test inventory, toolchain, and Meta trace **must** be independently revalidated before any Worker grant. Not implementation readiness.
**Authority:** zero. Neither this handout nor the predecessor closure grants Git, filesystem, browser, SSH, host, dependency installation, implementation, acceptance, publication, or Meta mutation.

---

## 0. Selection rationale and one bounded objective

With `bookradar-ui-shell` (`06`) closed and published at `2281982f7dae0ef1f582d294592c41281ba11b21`, BookRadar now has:

1. **`bookradar-core`:** dependency-free stateless kernel evaluating one supplied observation and one explicit assessment context under the 24-hour freshness and reviewer-evidence rules (17 tests).
2. **`bookradar-store` observation store (`0x42524452`, schema v1):** append-only SQLite store for observations and review revisions, deterministic history ordering and current-candidate selection, and the 4-fixture `bookradar-poc` CLI.
3. **`bookradar-store` research ledger (`0x42525249`, user_version 1):** strict `bookradar-research` JSON v1 validator, canonical-byte replay detection, quarantine, conflict detection, and unreviewed/disputed candidate projection via the `bookradar-research` CLI.
4. **`bookradar-ui`:** dependency-free standard-library loopback read-only HTML/CSS shell (`127.0.0.1`) rendering Current assessment, Observation history, Research ledger, and Research current candidates, backed by 17 UI tests and Playwright/Chromium browser verification.
5. **Verification gate:** `bash scripts/verify.sh` and `.github/workflows/verify.yml` running all **94 deterministic offline tests** with a 1-line `bookradar-core` dependency tree and strict `./.ap/ap doctor`.

### The architectural gap in the domain pipeline

In `docs/domain-contract.md` (§ *Trust and research ingestion*, lines 192–198), the product's core pipeline is defined as:

```text
Untrusted research assertions
    -> structural and invariant validation
    -> candidate assessment / quarantine
    -> attributed application observations
    -> separately governed verification eligibility
```

Right now, stages 1–2 (`bookradar-research`) and stages 4–5 (`Store` + `bookradar-core` + `bookradar-ui`) exist as **two disconnected islands**:

- **Island A (`ResearchStore`, `0x42525249`):** admits untrusted JSON findings as `Unreviewed` or `Disputed` candidates with `EvidenceMethod::AgentOnly` and no reviewer approval. By design, they can **never** become `Supported` or `Eligible` (`Checked available`) inside the research ledger, and there is no command or API to review a research candidate, resolve a research conflict, or promote a reviewed observation into the application store.
- **Island B (`Store`, `0x42524452`):** can evaluate `Supported` observations and produce `Checked available — [time]` or historical truth labels, and `Store::append_review` exists in library code, **but** the only executable way to put data into `0x42524452` is `bookradar-poc append-fixture` with the 4 hardcoded synthetic fixtures (`available`, `blocked`, `recovered`, `older`) on hardcoded `synthetic_offer()` (`source 1, offer 1`). Furthermore, neither `bookradar-poc` nor `bookradar-ui` allows selecting a non-default `(source_id, offer_id)` offer or appending an attributed review revision from the CLI.

**Single objective proposed for this whole (`bookradar-review-and-promotion-workflow`):**
Establish one minimal, deterministic, explicitly reviewer-governed **review, dispute-reconciliation, and research-to-store promotion workflow** connecting the accepted research ledger (`0x42525249`) and the application observation store (`0x42524452`), plus configurable offer selection in the local CLI/UI so promoted and reviewed offers can be inspected end-to-end. It must:
- preserve the strict trust boundary: **never** automatically promote `AgentOnly` or unreviewed/disputed research findings to verified stock;
- require explicit, attributed reviewer inputs (reviewer assessment `Supported` / `Disputed` / `Rejected`, explicit `assessor_reference`, `rationale`, caller-supplied `assessed_at` / `recorded_at` instants, and — when promoting to a positive supported claim — explicit reviewer-verified `EditionId` / `SubjectIdentity`, `LanguageEvidence`, `EvidenceMethod::Manual` or `DirectBrowser`, `ClaimCoverage`, and `ReviewerApproval` where applicable);
- preserve append-only immutability in both SQLite databases (`0x42524452` and `0x42525249`) and record traceable provenance linking a promoted application observation back to its research ledger receipt/position (`research:<receipt_id>/<position>` or equivalent);
- allow attributed review revisions (`Store::append_review` with `expected_revision` concurrency check) to resolve equal-time conflicts or supersede earlier assessments transparently without overwriting history;
- allow `bookradar-ui` (and/or the store CLI) to query a caller-selected `--source-id` and `--offer-id` (defaulting to `1` and `1` so all 94 existing tests and demos remain 100% compatible);
- require zero external network, zero real retail data, zero accounts/personal state, zero new external crates, and no change to `docs/domain-contract.md` or ADRs 0001–0007.

### Why this precedes live Hermes / Playwright scraping or NUC deployment

- If a live Hermes/Playwright producer is built first, its output is still untrusted `bookradar-research` v1 JSON that stops in the research ledger as `unreviewed`/`not-eligible` with no way for the human reviewer to review, reconcile disputes, or promote verified findings into the application store.
- Completing the local review-and-promotion bridge proves the **entire five-step domain contract pipeline** deterministically offline with synthetic fixtures and visible UI verification before introducing network, scraping, rate-limit, and host-security risks.
- *Alternative if the COOPERATOR redirects at Stage 2:* if the COOPERATOR prefers to keep promotion deferred and instead open a bounded **synthetic producer-adapter contract rehearsal** (`bookradar-producer-adapter`) or another slice, the fresh Orchestrator should reconcile that choice at Stage 2 before issuing `01_planning_00.md`.

---

## 1. Baseline and source precedence

- **Canonical repository:** `https://github.com/cisarik/bookradar`
- **Public branch:** `main`
- **Current public/local commit:** `2281982f7dae0ef1f582d294592c41281ba11b21`
- **Subject:** `feat: add a local read-only UI shell`
- **Parent:** `a2182302de73cb345b4b646993a1ad25d602555f`
- **Tree:** `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`
- **Commit date:** `2026-11-13T18:35:51+01:00` (`2026-11-13T17:35:51Z`)
- **Public CI run:** `43485796198` (<https://github.com/cisarik/bookradar/actions/runs/43485796198>), workflow `verify`, conclusion `success`, head SHA `2281982f7dae0ef1f582d294592c41281ba11b21`
- **Test count:** **94** (`17` core in `tests/verification.rs`, `10` store unit in `crates/bookradar-store/src/{store,research}.rs`, `4` observation CLI in `crates/bookradar-store/tests/cli.rs`, `13` history in `crates/bookradar-store/tests/history.rs`, `6` persistence in `crates/bookradar-store/tests/persistence.rs`, `2` research CLI in `crates/bookradar-store/tests/research_cli.rs`, `5` research contract in `crates/bookradar-store/tests/research_contract.rs`, `20` research ingestion in `crates/bookradar-store/tests/research_ingestion.rs`, `3` UI CLI in `crates/bookradar-ui/tests/cli.rs`, `6` UI HTTP in `crates/bookradar-ui/tests/http.rs`, `8` UI render in `crates/bookradar-ui/tests/render.rs`; `0` doc/bin unit tests)
- **Pinned AP:** `.ap` gitlink `d7023cf037f6d17885c3ede5c04812c61640da50` (immutable; detached clean checkout; strict `./.ap/ap doctor` PASS; variant `stable`)
- **Pinned toolchain:** Rust `1.99.1` (`rustc`, `cargo`, `rustfmt`, `clippy`) via `rust-toolchain.toml`; `$HOME/.cargo/bin` prepended in-process when needed
- **Accepted product contract:** `docs/domain-contract.md`, revision 1, accepted 2026-11-10
- **Accepted wire reference:** `docs/research-input-v1.md`
- **Accepted ADRs:** `docs/adr/0001`–`0007` (ADR 0007 accepted 2026-11-13)
- **Canonical verification gate:** `bash scripts/verify.sh` and `.github/workflows/verify.yml` (ADR 0006)

Read in RF-19 precedence order:
1. Project root `AGENTS.md` and the immutable AP at `.ap` (`d7023cf037f6d17885c3ede5c04812c61640da50`): `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/PROMPT_CONTRACTS.md`, `.ap/AP_WORKER.md`.
2. Current public `main` and local checkout `/Users/agile/Projects/bookradar`; independently verify refs, ancestry, tree, cleanliness, `.ap` submodule, public CI run `43485796198`, toolchain, and `bash scripts/verify.sh`.
3. Accepted `docs/domain-contract.md` (revision 1), `docs/research-input-v1.md`, and `docs/adr/0001`–`0007`.
4. Predecessor closure `projects/bookradar/00/06-bookradar-ui-shell/01_closure.md` and trace history as historical evidence.
5. This provisional handout as non-authorizing context.

---

## 2. Detailed technical audit of the current codebase and exact gaps

### 2.1 What already exists in `bookradar-core`, `bookradar-store`, and `bookradar-ui`

- **`bookradar-core` (`src/model.rs`, `src/verification.rs`):**
  - Typed identifiers (`SourceId`, `OfferId`, `ObservationId`, `EditionId`, `OfferRef`, `ObservationRef`), `SubjectIdentity` (`Resolved(EditionId)`, `Unresolved`, `Conflicting`), `LanguageEvidence` (`Slovak`, `Czech`, `Mixed`, `Unknown`, `Conflicting`), `AccessResult`, `ListingDisposition`, `SourceAvailability`, `EvidenceMethod` (`DirectBrowser`, `Manual`, `AgentOnly`), `ClaimCoverage` (`subject`, `language`, `source_availability` as `Covered` / `Missing`), `KnowledgeAssessment` (`Unreviewed`, `Supported`, `Disputed`, `Rejected`), `ReviewerApproval`, `ConflictState`, `RecheckState`, `TemporalAssessment`, `Eligibility`, and `evaluate_verification`.
  - `evaluate_verification` requires `SubjectIdentity::Resolved(target)`, `LanguageEvidence::Slovak`, `AccessResult::Readable`, `ListingDisposition::Present`, `SourceAvailability::Available`, `Some(SourceStatement)`, `EvidenceMethod::DirectBrowser | Manual` with `Some(EvidenceReference)` and all three required claims `Covered`, `KnowledgeAssessment::Supported` with `Some(ReviewerApproval)`, `ConflictState::Clear`, `RecheckState::Clear`, known timestamp offset, and `now < observed_at + 24h`.
- **`bookradar-store` (`crates/bookradar-store/src/store.rs`, `history.rs`, `research.rs`):**
  - `Store` (`0x42524452`, `user_version = 1`, `schema_v1.sql`):
    - `Store::create`, `Store::open(path, OpenMode)`, `Store::append(&ObservationRecord, Option<&ReviewDraft>)`, `Store::append_review(ObservationRef, expected_revision, &ReviewDraft) -> Result<u64, StoreError>`, `Store::history(OfferRef)`, `Store::current(OfferRef, EditionId, SystemTime)`.
    - `Store::append_review` already enforces optimistic concurrency (`expected_revision == current_max_revision`, where `0` is the first review) and non-regressing `assessed_at` (`assessment-time-regressed`), and `history::resolve` already clears an equal-time pairwise conflict when one of the incompatible observations has its latest review set to `KnowledgeAssessment::Rejected`, or clears a `Disputed` state when a newer review revision supersedes it with `Supported` or `Rejected`!
  - `ResearchStore` (`0x42525249`, `user_version = 1`, `schema_v1.sql` + `schema_research_v1.sql`):
    - `ResearchStore::create`, `ResearchStore::open(path, OpenMode)`, `ResearchStore::import(&[u8], ImportContext)`, `ResearchStore::inspect() -> Result<ResearchSnapshot, StoreError>`, `ResearchStore::current(&ResearchOfferKey, EditionId, SystemTime) -> Result<CurrentView, StoreError>`.
    - Stores `research_inputs` (receipt ID, raw bytes, canonical bytes, ingestion time, disposition, reported outcome, rule version, issues), `research_runs` (producer ID, run ID, canonical context, first receipt ID), and `research_findings` (receipt ID, position, producer ID, run ID, finding ID, canonical finding bytes, outcome, reason, knowledge, original receipt/position, `source_ref`, `listing_ref`, `listing_generation`, `source_id`, `offer_id`, `observation_id`), plus ledger-local candidate rows in `observations` and `reviews` (`Unreviewed` or `Disputed`, `AgentOnly`, assessor `rule:research-admission-v1`).
- **`bookradar-ui` (`crates/bookradar-ui/src/{config,snapshot,render,http,main}.rs`):**
  - Opens `--store` (`0x42524452`) and `--research-ledger` (`0x42525249`) with `OpenMode::ReadOnly` at `--now <unix-seconds>`, closes both connections, and serves `/` and `/style.css` on `127.0.0.1:<port>`.
  - Currently queries `synthetic_offer()` (`source 1, offer 1`) in `load_observations`, while `--producer`, `--source-ref`, `--listing-ref`, `--listing-generation`, and `--target-edition` are already configurable on the CLI.

### 2.2 Concrete gaps to address in this whole

1. **No CLI or library workflow to append a review revision (`append_review`) or reconcile a conflict/dispute:**
   - `Store::append_review` is only called in integration tests (`persistence.rs`, `history.rs`, `render.rs`). Neither `bookradar-poc` nor any review binary exposes appending a review revision (`Supported`, `Disputed`, `Rejected`) with `expected_revision`, `assessor_reference`, `rationale`, optional `ReviewerApproval`, and `assessed_at` / `recorded_at`.
   - In `ResearchStore`, disputed or unreviewed candidate observations have no review-revision or reconciliation path at all.
2. **No governed promotion/recording bridge from a research candidate (`0x42525249`) to an application observation store (`0x42524452`):**
   - A projected research candidate in `ResearchStore` has `EvidenceMethod::AgentOnly`, `SubjectIdentity::Unresolved` or `Conflicting`, and `KnowledgeAssessment::Unreviewed` or `Disputed`.
   - Under the domain contract (`docs/domain-contract.md` §§ *Verification and freshness*, *Admission, replay, and correction*, *Never automatically accepted*), promoting a research candidate to an application observation in `Store` (`0x42524452`) **must never** copy `AgentOnly` as verified stock or infer Slovak language / edition identity automatically. Instead, a governed promotion/review action must read the candidate finding/observation from `ResearchStore` (`OpenMode::ReadOnly`), require explicit reviewer-supplied verification facts (or explicit unreviewed/disputed/historical transfer parameters, as designed by the Planner and approved by the COOPERATOR), and write an attributed `ObservationRecord` + `ReviewDraft` into `Store` (`OpenMode::ReadWrite`) with traceable provenance referencing the research ledger source (e.g., `research:<producer_id>/<run_id>/<finding_id>@<receipt_id>/<position>`).
3. **Hardcoded `synthetic_offer()` (`source 1, offer 1`) in `bookradar-ui` (and/or CLI inspection):**
   - `bookradar-ui` currently calls `store.history(synthetic_offer())` and `store.current(synthetic_offer(), target, now)`. Adding optional `--source-id <positive-integer>` and `--offer-id <positive-integer>` flags (defaulting to `1` and `1`) allows `bookradar-ui` to inspect any offer in the observation store while keeping all existing CLI invocations and 94 tests 100% backward-compatible.

---

## 3. What the first Planner (`01/01`, `Native planning mode: required`) must evaluate

Ask a fresh Planner in Worker session `01`, exchange `01` (`fresh-worker-session`, `Native planning mode: required`) to inspect current repository truth read-only and propose **one minimal, decision-complete implementation plan** covering these twelve areas:

1. **As-found state and 94-test baseline verification.**
   Independently verify public/local commit `2281982f7dae0ef1f582d294592c41281ba11b21`, parent `a2182302de73cb345b4b646993a1ad25d602555f`, tree `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`, CI run `43485796198`, AP pin `d7023cf037f6d17885c3ede5c04812c61640da50`, clean worktree, Rust `1.99.1`, `scripts/verify.sh`, `.github/workflows/verify.yml`, and the 94-test inventory across `bookradar-core`, `bookradar-store`, and `bookradar-ui`.

2. **Functional slice and command/API surface.**
   Compare:
   - extending `bookradar-research` and/or `bookradar-poc` with explicit subcommands (e.g., `review`, `promote`, or offer-scoped `history`/`current`), versus
   - adding a dedicated `bookradar-review` binary in `bookradar-store` (or keeping the CLI surface minimal across the existing binaries).
   Evaluate how an operator/reviewer:
   - inspects a research candidate in `ResearchStore`;
   - promotes/admits a reviewed candidate from `ResearchStore` (`OpenMode::ReadOnly`) into `Store` (`OpenMode::ReadWrite`) on a target `OfferRef(SourceId, OfferId)` with explicit reviewer-attested attributes;
   - appends a new `ReviewDraft` revision (`Store::append_review` and/or `ResearchStore::append_review`) with `expected_revision` to support, dispute, or reject an observation and resolve conflicts;
   - views the resulting offer in `bookradar-poc` and `bookradar-ui`.

3. **Trust boundary and anti-auto-promotion invariants.**
   Specify the exact invariants that prevent any violation of `docs/domain-contract.md` (§ *Never automatically accepted*):
   - A rejected or opaque-quarantined research finding cannot be promoted as a supported observation.
   - `EvidenceMethod::AgentOnly` can never qualify for `Eligibility::Eligible` (`Checked available`), even if a reviewer attaches `KnowledgeAssessment::Supported` and `ReviewerApproval` (because `bookradar-core` requires `DirectBrowser` or `Manual` evidence method with all three claims `Covered`).
   - Promotion to a reviewer-verified observation requires explicit reviewer attestation of the verification method (`DirectBrowser` or `Manual`), evidence reference, claim coverage (`subject`, `language`, `source_availability`), subject resolution (`EditionId`), language evidence, `ReviewerApproval`, `assessor_reference`, `rationale`, and caller-supplied `assessed_at` / `ingested_at` instants — never silently fabricating them from untrusted agent JSON.
   - Also evaluate whether promoting a candidate as an explicitly *unreviewed* or *historical* observation (preserving `AgentOnly` so it can never be `Checked available` until a later manual/browser recheck or review) should be supported or whether promotion requires explicit review at promotion time. Surface this choice clearly to the COOPERATOR.

4. **Database schemas, append-only triggers, and cross-file provenance.**
   Audit `schema_v1.sql` (`0x42524452`) and `schema_research_v1.sql` (`0x42525249`).
   - Determine whether the existing schema v1 tables (`sources`, `editions`, `offers`, `observations`, `reviews`) and `provenance_reference` field already store every required fact without a schema v2 migration!
   - Note that `Store::open` and `ResearchStore::open` enforce exact `EXPECTED_OBJECTS` lists on `sqlite_master` (`store.rs` lines 22–33, `research.rs` lines 38–59) and `user_version = 1`. Keeping schema v1 unchanged avoids any migration and preserves 100% compatibility with existing v1 files.
   - Define the exact deterministic `provenance_reference` format when an observation in `Store` is promoted from `ResearchStore` (for example, `research-promoted:<producer_id>/<run_id>/<finding_id>#<receipt_id>/<position>`), and how duplicate promotion of the same observation key `(source_id, offer_id, observation_id)` fails closed (`StoreError::DuplicateKey`).

5. **Conflict resolution and review revisions.**
   Audit how `Store::append_review(observation_ref, expected_revision, &review_draft)` and `history::resolve` interact:
   - Equal-time incompatible observations produce `ConflictState::Unresolved` (`Unverified — unresolved conflict`) until one of the incompatible observations receives a review revision with `KnowledgeAssessment::Rejected`.
   - A `Disputed` observation produces `ConflictState::Unresolved` until a subsequent review revision on that observation changes its latest knowledge to `Supported` or `Rejected`.
   - `expected_revision` prevents lost updates (`StoreError::ReviewRevisionConflict`), and `assessed_at` must not regress (`StoreError::InvalidReview { reason: "assessment-time-regressed" }`).
   - Evaluate whether `ResearchStore` should also expose read-only candidate history/details or `append_review` for ledger-local dispute resolution, or whether all human review revisions belong in the application `Store` (`0x42524452`).

6. **Configurable offer selection in `bookradar-ui` (and CLI).**
   Audit `crates/bookradar-ui/src/{config,snapshot,render}.rs`:
   - Currently `bookradar-ui` hardcodes `synthetic_offer()` (`source 1, offer 1`).
   - Evaluate adding optional `--source-id <positive-integer>` and `--offer-id <positive-integer>` flags to `bookradar-ui` (defaulting to `1` and `1`), passing `OfferRef::new(source_id, offer_id)` into `store.history(offer)` and `store.current(offer, target, now)`, and displaying the configured `source <id>, offer <id>` in the `Configured query` section.
   - Evaluate whether `bookradar-poc` should stay strictly the 4-command fixed proof (per ADR 0004) while the new review/promotion commands live in `bookradar-research` or a new binary, so ADR 0004's "four fixed commands" invariant is untouched.

7. **Crate/binary placement and zero-new-dependency preservation.**
   Confirm that:
   - `bookradar-core` remains 100% untouched and dependency-free (`cargo tree -p bookradar-core` = 1 line);
   - no new external crate is added to `Cargo.toml` or `Cargo.lock`;
   - `#![forbid(unsafe_code)]` is preserved everywhere.

8. **Determinism and test infrastructure.**
   Require caller-supplied Unix timestamps on every new command/API (`--ingested-at`, `--assessed-at`, `--now`, etc.), no `SystemTime::now()`, no external network, and guarded `TempDir` cleanup.
   Propose exact new tests (file, function name, setup, expected result, and causal regression covered) for:
   - promoting a research candidate with explicit reviewer direct-browser/manual verification into `Store` and observing `Checked available — Unix …; expires at Unix …` in `Store::current` and `bookradar-ui`;
   - refusing or keeping `not-eligible` any promotion/review that retains `AgentOnly` support, missing reviewer approval, non-Slovak language, unresolved subject, or stale timestamp;
   - rejecting promotion of a `rejected` or `quarantined` research finding (`invalid-availability`, `identity-conflict`, etc.) or an unknown `(producer_id, run_id, finding_id)` / receipt position;
   - duplicate promotion / duplicate observation ID failing closed without partial writes;
   - appending review revisions (`Store::append_review` via CLI/API) to resolve an equal-time conflict (`Rejected` on the conflicting observation) and a `Disputed` observation (`Supported` with reviewer approval), plus negative tests for wrong `expected_revision` (`review-conflict`) and regressed `assessed_at` (`storage`);
   - `bookradar-ui` rendering a non-default `--source-id` / `--offer-id` offer and rejecting invalid `--source-id` / `--offer-id` (`0`, negative, non-numeric, duplicate) with exit `2` before I/O.

9. **CI and verification gate impact.**
   Confirm whether `scripts/verify.sh` and `.github/workflows/verify.yml` remain unchanged while automatically compiling, testing, formatting, and clippy-checking all new code and tests offline.

10. **Documentation and ADR.**
    Propose updates to `README.md` (documenting the end-to-end synthetic workflow from `bookradar-research import` -> review/promotion -> conflict resolution -> `bookradar-ui`) and `docs/adr/0008-...` recording the review and promotion architecture decision, while keeping `docs/domain-contract.md`, `docs/research-input-v1.md`, and `docs/adr/0001`–`0007` untouched.

11. **Evidence tier, independent acceptance, and browser verification.**
    Propose `Evidence tier: E2` with `Independent acceptance: required-separate-fresh-worker` (`Fresh Independent Audit`), including `bash scripts/verify.sh`, CLI transcript verification, and bounded local Playwright/Chromium verification of the promoted offer in `bookradar-ui` under the AP Browser Stall Guard Contract.

12. **Git, allowlist, rollback, and decision table.**
    Provide the exact changed-path allowlist, ordered implementation stages, rollback path, proposed commit subject, and a complete material decision table for COOPERATOR approval.

---

## 4. Nonnegotiable boundaries

This logical whole does **not** authorize:

- changing product semantics, `bookradar-core` behavior, schema v1 (`0x42524452`), research ledger schema v1 (`0x42525249`), the research wire contract (`docs/research-input-v1.md`), `docs/domain-contract.md`, or `docs/adr/0001`–`0007`;
- automatic promotion of `AgentOnly` research findings to verified stock, inferring Slovak language from website locale, merging editions by ISBN/title alone, or treating access failures (`429`, CAPTCHA, timeout, `404`) as stock exhaustion;
- modifying or deleting existing rows in `observations`, `reviews`, `research_inputs`, `research_runs`, or `research_findings` (all append-only triggers must remain intact);
- making `bookradar-ui` writable (the UI server remains strictly `OpenMode::ReadOnly` with `GET`/`HEAD` only on `/` and `/style.css`);
- live Hermes/Playwright scraping, external network calls, MCP, real retail data, committed screenshots, personal state/watchlists/library, accounts, authentication, NUC, SSH, sudo, services, deployment, or release automation;
- adding any external crate dependency to the workspace or any dependency to `bookradar-core`;
- force push, rebase, history rewrite, tags, extra refs, `.ap` updates, or Meta Git operations by a Worker.

---

## 5. Operating model for the fresh Orchestrator

1. **Stage 1 — Read-only restoration and handout revalidation:**
   - Read root `AGENTS.md` and the pinned AP documents at `.ap` (`d7023cf037f6d17885c3ede5c04812c61640da50`).
   - Open `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_handout_00.md`.
   - Independently verify public/local commit `2281982f7dae0ef1f582d294592c41281ba11b21`, parent `a2182302de73cb345b4b646993a1ad25d602555f`, tree `b6e2e169a3670d07a1e16afcaeddd50d368a72d6`, public CI run `43485796198` (`success`), the **94-test inventory** via `bash scripts/verify.sh`, `.ap` pin and strict `./.ap/ap doctor` PASS, Rust `1.99.1` toolchain, and the predecessor closure `06-bookradar-ui-shell/01_closure.md` (`77332b58b403ccf30647d17883f3f8e4e008a9efac81be453148e8d29e37f49f`).
   - Create `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_notes.md` and record the **Handout Revalidation Record** (`PROMPT_CONTRACTS.md#handout-revalidation-record`), explicitly noting the COOPERATOR-requested `00_handout_00.md` filename exception.
2. **Stage 2 — Reconcile the bounded objective with the COOPERATOR:**
   - Present the restored state, the review-and-promotion gap between `ResearchStore` (`0x42525249`) and `Store` (`0x42524452`), and the delivery-route check.
3. **Initial Planner (`01/01`):**
   - Issue `01_planning_00.md` targeting `fresh-worker-session` (`Worker session ordinal: 01`, `Worker exchange ordinal: 01`, `Native planning mode: required`, profile `Planner`, reasoning `High`) for a read-only implementation plan, with report destination `01_report_00.md`.
   - Do not grant implementation, browser, dependency, Git, publication, acceptance, or closure authority in the planning prompt.
4. **Trace hygiene reminder from `06-bookradar-ui-shell`:**
   - Ensure each Worker prompt is delivered to its intended session target (`current-worker-session` only when the exact session is open; otherwise `fresh-worker-session` with the next session ordinal), and verify `Companion Integrity Invariant` (RF-19) on every saved report before reconciliation.

**Fresh Orchestrator restoration prompt (copy-paste pointer, not authority):**

```text
Resume this AP-integrated project.
Read the root AGENTS.md and the pinned AP documents it names.
Open /Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_handout_00.md.
Begin read-only. Verify the current public/local commit 2281982f7dae0ef1f582d294592c41281ba11b21, CI run 43485796198, 94-test inventory, AP pin, toolchain and Meta trace independently. Record the handout revalidation (and the 00_handout_00.md opening filename exception) in the new whole's 00_notes.md when the activated trace permits.
Reconcile the bounded bookradar-review-and-promotion-workflow objective with the COOPERATOR.
Then issue the first fresh Planner prompt (01_planning_00.md, session 01, exchange 01, actual native Plan Mode required) for a read-only implementation plan. Do not grant implementation, browser, dependency, Git, publication, acceptance or closure authority.
```

---

## 6. Quality standard for the review-and-promotion slice

A credible slice should achieve:

- an explicit, deterministic CLI and library path to promote a reviewed research candidate from `ResearchStore` (`0x42525249`, opened `ReadOnly`) into `Store` (`0x42524452`, opened `ReadWrite`) and to append review revisions (`Store::append_review`) with optimistic concurrency (`expected_revision`);
- strict enforcement of the domain contract's trust boundary: no automatic promotion, no `AgentOnly` eligibility, no inferred language/edition, and fail-closed rejection of quarantined/rejected findings or invalid review revisions;
- traceable provenance on promoted observations (`research:...`) and preservation of schema v1 and all append-only triggers in both databases;
- configurable `--source-id` and `--offer-id` in `bookradar-ui` (defaulting to `1` and `1`) while keeping `bookradar-ui` 100% read-only;
- all 94 existing tests preserved plus focused new unit, CLI, persistence, and UI tests passing under `bash scripts/verify.sh`;
- an end-to-end synthetic demonstration in `README.md` (`bookradar-research import` -> promote/review -> conflict resolution -> `bookradar-ui`) and an accepted ADR `0008`.

---

## 7. Suggested acceptance matrix and negative evidence

| Risk / feature | Bounded evidence the Planner should require |
|---|---|
| Baseline & gate | Public/local `2281982f…`; CI run `43485796198` success; 94 tests; AP pin `d7023cf…`; `ap doctor` PASS; clean worktree |
| Governed promotion | Reads candidate from `ResearchStore` (`ReadOnly`); writes attributed observation + review to `Store` (`ReadWrite`) with `research:...` provenance; ledger bytes unchanged |
| No auto-verification | Promoting without manual/direct-browser evidence + reviewer approval + Slovak + resolved target edition stays `not-eligible`; `AgentOnly` never becomes `Checked available` |
| Quarantined / rejected findings | Attempting to promote a `rejected` or `quarantined` finding fails closed with stable exit code and zero `Store` writes |
| Review revisions & conflict resolution | Appending a `Rejected` review revision to an incompatible equal-time observation or a `Supported` revision to a `Disputed` observation updates `Store::current` truth label deterministically while preserving prior revisions |
| Concurrency & time guards | Mismatched `expected_revision` fails with `review-conflict`; regressed `assessed_at` fails with `assessment-time-regressed`; duplicate observation key fails with `duplicate-key` |
| UI offer selection | `bookradar-ui --source-id <S> --offer-id <O>` renders the promoted offer's history and current truth label; defaults remain `1`/`1`; invalid IDs exit `2` before I/O |
| Zero external dependencies | `Cargo.lock` adds no external crate; `cargo tree -p bookradar-core` remains 1 line; `#![forbid(unsafe_code)]` everywhere |
| Tests & CI | 94 existing tests preserved + new focused tests pass in `bash scripts/verify.sh`; post-publication CI run observed on `origin/main` |
| Documentation & ADR | `README.md` end-to-end synthetic workflow + `docs/adr/0008-...`; `docs/domain-contract.md` and ADRs 0001–0007 unchanged |

---

## 8. Residual risks and decisions to surface

1. **CLI binary boundary:** extend `bookradar-research` / `bookradar-poc` vs add a small `bookradar-review` binary in `bookradar-store` (noting ADR 0004 states `bookradar-poc` has four fixed commands). The COOPERATOR decides.
2. **Promotion policy:** require full reviewer verification at promotion time vs allow promoting a candidate as `Unreviewed` (`AgentOnly`) into `Store` first and then appending a `Supported` review revision after manual/direct-browser recheck (or both). The COOPERATOR decides.
3. **Research ledger immutability during promotion:** `ResearchStore` should be opened `OpenMode::ReadOnly` during promotion into `Store`, keeping the untrusted research ledger and the curated application observation store strictly separate.
4. **Offer & observation ID allocation in `Store`:** operator-supplied `(source_id, offer_id, observation_id)` vs deterministic next-observation-id allocation per offer. The COOPERATOR decides.
5. **UI offer flags:** optional `--source-id` and `--offer-id` on `bookradar-ui` (default `1`, `1`) while keeping `bookradar-ui` strictly read-only.
6. **Evidence tier & independence:** `E2` with a separate `Fresh Independent Audit` (including Playwright/Chromium verification if `bookradar-ui` is touched) and COOPERATOR acceptance before publication.

---

## 9. Readiness review and exact next action

| Review area | Status |
|---|---|
| Predecessor closure (`06-bookradar-ui-shell`) | PASS (`closed-by-ORCHESTRATOR` at `2281982f…`; `01_closure.md` SHA-256 `77332b58…`) |
| Current public `main` / local checkout | Verified equal at `2281982f7dae0ef1f582d294592c41281ba11b21`; clean worktree; **successor must revalidate** |
| Test / CI state | 94 tests pass in `bash scripts/verify.sh`; public `verify` run `43485796198` conclusion `success` |
| Accepted contract / ADRs / AP | PASS at contract revision 1, `research-input-v1`, ADRs 0001–0007, and AP pin `d7023cf…` |
| Review & promotion state | `Store::append_review` exists in library only; no CLI review command, no research-to-store promotion workflow, and `bookradar-ui` offer is hardcoded to `1/1` |
| Active mutation / Worker sessions | None; all `06-bookradar-ui-shell` exchanges are expired and closed |
| Security / host / provider boundaries | PASS for local, synthetic, offline, zero-external-dependency planning |
| First Planner readiness | PASS **after** Stage 1 revalidation and Stage 2 COOPERATOR objective reconciliation |
| Implementation readiness | NOT GRANTED; requires Planner report `01_report_00.md`, COOPERATOR decision gate, and complete implementation grant |

---

## 10. Artifact lifecycle and return edge

- **Class:** retained opening continuity and handoff evidence (`Handout status: provisional`).
- **AP relationship:** historical/consumer handoff, subordinate to governing AP and `docs/domain-contract.md`.
- **Consumer:** fresh per-whole Orchestrator for `07-bookradar-review-and-promotion-workflow`, its initial Planner, and the upstream Master upon closure.
- **Discoverability:** `/Users/agile/meta/projects/bookradar/00/07-bookradar-review-and-promotion-workflow/00_handout_00.md`, predecessor `06-bookradar-ui-shell/01_closure.md`, commit `2281982f7dae0ef1f582d294592c41281ba11b21`, CI run `43485796198`, AP pin `d7023cf037f6d17885c3ede5c04812c61640da50`, and ADRs 0001–0007.
- **Retention:** freeze upon whole opening, retain through the whole, and archive after closure; any material rewrite after opening uses a successor handout (`01_handout.md`) in the handoff sequence.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup decision.
- **Expected return to Master:** a truthful `01_closure.md` with exact public commit, CLI/UI and CI evidence, completed scope, explicit non-achievements, current contract/AP pin, residual risks, recommended next logical whole(s), and no implied successor grant.

**Final invariant:** Bridge untrusted research and curated application truth only through explicit, attributed human review. Zero auto-verification, append-only SQLite integrity, deterministic caller-supplied time, zero new external dependencies, and no live network or real retail data.

# BookRadar — First Planner — Minimal Local Read-Only UI Shell

Persistent role identity: WORKER
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BOOKRADAR-UI-SHELL-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the plan must evaluate local UI architectures (web vs TUI vs native), dependency supply-chain and lockfile impact, loopback-only local security boundaries, deterministic rendering of domain truth labels and research-ledger states without auto-verification, and browser/CI acceptance boundaries.
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded design of one minimal local read-only UI shell over the accepted synthetic observation store and research ledger, covering as-found state and UI gap, functional slice and runnable path, public data/API inventory, exact UI truth labels and states, crate/binary and dependency boundary, loopback-only security and privacy, determinism and test infrastructure, CI and gate impact, documentation and ADR proposal, evidence tier and browser acceptance plan, and Git/publication boundary.
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

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell
Trace project key: bookradar
Trace logical-whole projection identity: bookradar-ui-shell
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Repository mutation: none
Host/remote mutation: none
Trace persistence: none

## Authority and delivery posture

You are a fresh WORKER in the Planner profile. This is a read-only planning
exchange. The current prompt is your only task authority. The provisional
handout and the Orchestrator notes are historical/contextual evidence, not task
authority.

Native Plan Mode is ON and must remain ON for this exchange. Do not implement,
edit repository files, write to the Meta trace, run builds or tests, start a
server or browser, install dependencies, fetch into the repository, commit,
push, accept, publish, or close anything. Return the complete terminal planning
report in this session. The COOPERATOR will persist it at the exact report path
above. The relay basis is the COOPERATOR-selected manual ferry and the native
Plan Mode write restriction; `Trace persistence: none` is intentional and
grants no Meta write.

The received prompt is persisted at
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_planning_00.md`.
You may read that file to verify identity and compute its SHA-256; do not
modify it. Echo the prompt SHA-256 in your report.

## Repository and baseline

Canonical repository: `https://github.com/cisarik/bookradar`
Working directory: `/Users/agile/Projects/bookradar`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `a2182302de73cb345b4b646993a1ad25d602555f`
Expected parent: `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
Expected tree: `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`
Expected subject: `fix: restore target ignore and run the gates in CI`
Expected worktree: clean (`git status --porcelain` empty; `target/` is ignored by `/target/`)
Expected public CI evidence: workflow `verify`, run `43438422059`, conclusion `success`, head SHA `a2182302de73cb345b4b646993a1ad25d602555f`
Governing AP: `.ap` gitlink and detached checkout `d7023cf037f6d17885c3ede5c04812c61640da50`
Accepted contract: `docs/domain-contract.md`, revision 1, accepted 2026-11-10
Accepted ADRs: `docs/adr/0001`–`0006`; ADR 0006 accepted 2026-11-13
Verification gate owner: `scripts/verify.sh`, `.github/workflows/verify.yml`, `README.md`, `docs/adr/0006-verification-gate-and-ci.md`

Independently verify before planning: physical root and remote; branch and HEAD;
parent and tree; worktree cleanliness (`git status --porcelain` empty); `.gitignore`
rules (`/target/` and `/tests/target/`); `.ap` detached at the gitlink and clean;
strict `./.ap/ap doctor` PASS; Rust `1.99.1` and C compiler availability;
`scripts/verify.sh` and `.github/workflows/verify.yml`; README; ADR 0006; and
the 77-test inventory across source/test files (17 core in `tests/verification.rs`,
10 store unit in `crates/bookradar-store/src/{store,research}.rs`, 4 old CLI in
`crates/bookradar-store/tests/cli.rs`, 13 history in
`crates/bookradar-store/tests/history.rs`, 6 persistence in
`crates/bookradar-store/tests/persistence.rs`, 2 research CLI in
`crates/bookradar-store/tests/research_cli.rs`, 5 research contract in
`crates/bookradar-store/tests/research_contract.rs`, and 20 research ingestion
in `crates/bookradar-store/tests/research_ingestion.rs`). Public
`refs/heads/main` may be checked read-only with `git ls-remote`, and public CI
run `43438422059` may be checked read-only if `gh api` is available. If
repository state differs, classify the difference under RF-12 and stop; do not
repair it.

Execution route (RF-16): no `ap.project.conf` is declared in this repository.
The project-owned verification gate is `bash scripts/verify.sh` (per `README.md`
and `docs/adr/0006-verification-gate-and-ci.md`), and the protocol integration
check is `./.ap/ap doctor`. Because this exchange is a read-only `Planner` task
under `Native planning mode: required`, executing `bash scripts/verify.sh` or
`cargo` build/test/fetch commands is not part of this planning grant (the
Orchestrator already executed `bash scripts/verify.sh` during Stage 1
restoration and verified exit 0 with all 77 tests passing). Use direct file
reads, read-only `git` commands, read-only toolchain version checks (with
`$HOME/.cargo/bin` prepended in-process if needed, never editing shell
profiles), and `./.ap/ap doctor`. In your proposed implementation and acceptance
plan, bind `bash scripts/verify.sh` as the canonical project verification gate
rather than a parallel raw `cargo` gate list.

The predecessor closure is
`/Users/agile/meta/projects/bookradar/00/05-bookradar-test-hardening-and-ci/01_closure.md`
(SHA-256 `9c157d4935020e56056eacbb9251905ee31284fad72444654ed5d7d672ae4b2b`).
The provisional handout is
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/00_handout.md`
(SHA-256 `193c2cc55d23424fb922e7fbfe4d7dd1dc2f315d483887194a0b50c8acb3f844`).
Read them as historical evidence. Do not treat either as a current grant.

## Mandatory reading

Read the WORKER minimum-reading spine and the task-relevant anchors:

- `.ap/AP.md`: Semantic Authority and Artifact Relationships; RF-03, RF-06,
  RF-11, RF-12, RF-16, RF-18, RF-19; §3 Worker Session Target and Orchestration
  Planning and Implementation Planning; Plan-to-Execution Gate; Planning Budget
  and Expiry; §8; §11 Browser and Rendered Acceptance Automation; §12
  Validation; §18 Stopping Conditions.
- `.ap/AP_WORKER.md`: Worker Session Target; Worker Exchange Coordinates and
  Trace Boundary; Before Mutation; Validation; Reporting; Stopping Conditions.
- `.ap/PROMPT_CONTRACTS.md`: Worker Report Header; Planning Record;
  Plan-to-Execution Gate; Worker Exchange Identity and External Trace Contract;
  Validation Ladder Record; Browser Stall Guard Contract.
- Project root `AGENTS.md`.
- `README.md`, `.gitignore`, `Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`,
  `scripts/verify.sh`, `.github/workflows/verify.yml`.
- `docs/domain-contract.md`, `docs/research-input-v1.md`, and `docs/adr/0001`–`0006`.
- `src/lib.rs`, `src/model.rs`, `src/verification.rs`, and `tests/verification.rs`.
- `crates/bookradar-store/Cargo.toml`, `crates/bookradar-store/src/lib.rs`,
  `crates/bookradar-store/src/store.rs`, `crates/bookradar-store/src/history.rs`,
  `crates/bookradar-store/src/research.rs`,
  `crates/bookradar-store/src/research_contract.rs`,
  `crates/bookradar-store/src/fixtures.rs`,
  `crates/bookradar-store/src/bin/bookradar-poc.rs`, and
  `crates/bookradar-store/src/bin/bookradar-research.rs`.
- Test files in `crates/bookradar-store/tests/` (`cli.rs`, `history.rs`,
  `persistence.rs`, `research_cli.rs`, `research_contract.rs`,
  `research_ingestion.rs`, and `common/mod.rs`) to audit how the 77 tests and
  synthetic fixtures work.

## Goal

Produce one decision-complete, repository-grounded implementation plan for the
smallest useful local read-only **UI shell** (`bookradar-ui-shell`) over the
accepted synthetic observation store and research ledger. The UI must render
the accepted domain truth labels with text, time, and uncertainty, preserve the
separate research candidate statuses (`unreviewed`/`disputed`, never verified),
handle empty/missing/corrupt/unsupported-schema states deterministically, and
require no live ingestion, real retail data, accounts, external network,
secrets, deployment, or product-semantics change.

This is a plan, not implementation and not acceptance. Leave every material
UI architecture, dependency, slice, wording, visual design, browser acceptance,
evidence-tier, and publication decision explicitly visible to the COOPERATOR.

## Nonnegotiable boundaries

This whole and your plan must **not** authorize or propose:

- changing product semantics, `bookradar-core` behavior, schema v1, the research
  wire contract, `docs/domain-contract.md`, `docs/adr/0001`–`0006`, or the
  accepted observation-store and research-ledger behavior;
- adding any dependency to `bookradar-core` (`cargo tree -p bookradar-core` must
  remain a single line);
- a live Hermes/Playwright research adapter, scraping, external APIs, MCP, real
  retail data, accounts, authentication, personal state/watchlists/library,
  multi-user privacy design, NUC, SSH, sudo, services, hosting, deployment,
  release automation, or production jobs;
- a UI that writes, imports, reviews, promotes, migrates, repairs, or creates
  databases (the UI slice must open existing databases strictly in
  `OpenMode::ReadOnly` or report their absence/error);
- a UI that presents research candidates as verified, invents `"Sold out"` or
  `"In stock"`, uses an unqualified green `"Available"` label on historical
  data, presents `eligible` as a purchase guarantee, or relies on colour alone
  to carry meaning;
- external network access, `0.0.0.0` binding, CDNs, telemetry, analytics,
  remote fonts, third-party remote assets, CORS wildcards, or arbitrary file
  serving (any local HTTP surface must bind `127.0.0.1` only);
- committing screenshot files or real retail/personal data to the repository;
- a broad design-system program, a broad i18n program, a heavy test framework,
  a browser download in CI, or a toolchain upgrade;
- force push, rebase, history rewrite, tags, extra refs, `.ap` updates, or Meta
  Git operations;
- a new license, contribution, privacy, security-response, support, or release
  policy.

## Required planning work

Evaluate and provide concrete, repository-grounded recommendations and options
for all twelve areas below:

### 1. As-found state and functional gap

Verify the current public/local commit `a2182302de73cb345b4b646993a1ad25d602555f`,
parent `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`, tree
`9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`, AP pin
`d7023cf037f6d17885c3ede5c04812c61640da50`, clean checkout, public CI run
`43438422059`, 77-test inventory, toolchain, `scripts/verify.sh`,
`.github/workflows/verify.yml`, `README.md`, and ADR 0006. Record exactly what
exists in `bookradar-core` and `bookradar-store`, what is currently visible only
through raw CLI transcripts (`bookradar-poc` and `bookradar-research`), and the
five concrete UI gaps (no user-visible observation history/current assessment;
no user-visible research ledger/candidates/quarantine/conflicts; no consistent
UI empty/missing/corrupt/unsupported-schema states; no local repeatable UI demo
path; no UI-specific tests/acceptance/docs). State what you inspected directly
and any read-only limitation.

### 2. Functional slice and runnable path

Evaluate the smallest end-to-end UI slice: one local read-only page/dashboard
rendering both observation store (history + current assessment) and research
ledger (inspect snapshot + candidate current reading), versus observation-store
only or multi-view navigation. Compare:
- a local loopback web UI (HTML/CSS rendered by a minimal local Rust HTTP handler
  or static page + JSON endpoint);
- a terminal UI (TUI);
- a native desktop shell.
Compare development cost, dependency footprint (including zero-new-dependency
`std::net::TcpListener` HTTP/HTML rendering versus external crates), visual
acceptance by the COOPERATOR and browser automation, accessibility, security,
and CI compile-time/lockfile impact. Recommend one option and state the exact
local commands to prepare synthetic demo stores and run the UI.

### 3. Data and API inventory

Audit the existing public APIs in `bookradar-core` and `bookradar-store`:
`Store::open(..., OpenMode::ReadOnly)`, `Store::history`, `Store::current`,
`HistoryEntry`, `ObservationRecord`, `ReviewRevision`, `CurrentView`,
`CandidateAssessment`, `StockClaim`, `ResearchStore::open(..., OpenMode::ReadOnly)`,
`ResearchStore::inspect`, `ResearchStore::current`, `ResearchSnapshot`,
`InputView`, `FindingView`, `ResearchOfferKey`, `synthetic_offer`,
`synthetic_target`, `render_current`, `render_history`, `render_inspect`, and
`render_research_current`.
Check whether any fields needed by the UI are currently private or only exposed
through text transcripts (for example, `CurrentView` or `HistoryEntry` or
`ResearchSnapshot` getters, or whether `bookradar-store` needs any small,
purely read-only public getter/helper without changing semantics). The UI must
use the accepted store/core evaluation rather than duplicating 24-hour
freshness, eligibility, conflict, recheck, or research admission logic. Specify
exact read-only data shaping and confirm no direct SQL in the UI layer.

### 4. UI truth and exact states

Propose the exact screens/sections and user-facing labels for:
- **Observation history**: observation ID, observed time (original text, offset
  state, Unix instant), ingested time, captured time, subject/edition state,
  language evidence, access result, listing disposition, source-reported
  availability, source statement, evidence method/reference/claim coverage,
  provenance/uncertainty, and review revisions (`knowledge`, `approval`,
  `assessor_reference`, `rationale`).
- **Current assessment**: exact user-facing truth label from the domain contract
  (`Checked available — [time]` with expiry, `Last observed available — [time]`,
  `Last observed reserved — [time]`, `Last observed unavailable — [time]`,
  `Could not recheck — [time]`, `Listing removed — [time]`, and explicit
  `Unverified` reasons), candidate identity, temporal assessment, conflict
  state, recheck state, verification eligibility, and explicit notice that
  verification describes an evidenced source observation rather than a purchase
  guarantee.
- **Research ledger**: envelope/run/finding/observation/review counts, receipt
  dispositions and reported outcomes, finding outcomes (`admitted`, `replayed`,
  `rejected`, `quarantined`), reasons, knowledge state (`unreviewed`,
  `disputed`), and projected observation IDs.
- **Research current candidates**: candidate assessment for a queried
  `ResearchOfferKey` + target `EditionId` + evaluation instant, explicitly
  shown as unreviewed or disputed research candidates (`agent-only` application
  support, `not-eligible` for verification, never auto-promoted or labelled
  verified).
- **Empty and error states**: empty observation store, empty research ledger,
  missing database path (`not-found`), corrupt or wrong-application-id or
  unsupported-schema database (`unsupported-schema`, e.g. passing a research
  ledger to the observation store slot or vice versa), invalid operator/query
  input, and no-candidate states.
State how text, timestamps, and explicit uncertainty carry every meaning so
colour is never the sole carrier, and confirm that no `"Sold out"`, `"In stock"`,
unqualified green `"Available"`, or auto-promoted `"Verified"` label exists.

### 5. Architecture and dependency boundary

Compare:
- a new workspace crate `crates/bookradar-ui` versus a new binary (`bookradar-ui`)
  inside `crates/bookradar-store` (or a small library module + binary);
- zero new external dependencies (using Rust standard library `std::net::TcpListener`
  with bounded request parsing and server-rendered semantic HTML/CSS, reusing
  existing workspace crates) versus adding an HTTP/TUI crate.
Evaluate impact on `Cargo.toml`, `Cargo.lock`, `bookradar-core` dependency-free
invariance, offline build/test after `cargo fetch --locked`, build time in CI,
and rollback simplicity. Remember: no new dependency is pre-approved; the
COOPERATOR decides.

### 6. Local security and privacy

Specify exact technical controls for the local UI surface:
- loopback-only binding (`127.0.0.1:<port>` or ephemeral `127.0.0.1:0`),
  rejecting non-loopback bind addresses (`0.0.0.0`, external interfaces, remote
  hosts);
- read-only HTTP methods only (`GET` / `HEAD`), bounded request buffer and
  timeouts, strict route allowlist, no arbitrary filesystem/static-directory
  serving, no path traversal, and HTML-escaping of all untrusted/stored strings
  (remember that research findings and observation statements can contain
  hostile text such as `<script>` or embedded instructions);
- strict response headers (e.g. `Content-Security-Policy` forbidding scripts,
  external origins, inline scripts, remote fonts/styles/connect;
  `X-Content-Type-Options: nosniff`; `Cache-Control: no-store`; no CORS
  wildcard);
- no database writes, no database creation or migration from the UI, no external
  network calls, no telemetry/analytics/CDNs, no secrets, no accounts, and no
  personal or real retail data.

### 7. Determinism and test infrastructure

Require a caller-supplied evaluation instant (`--now <unix-seconds>` or
equivalent), synthetic fixtures only, `OpenMode::ReadOnly` database opens, no
wall clock (`SystemTime::now()` forbidden in domain/UI evaluation), no external
network, no credentials, and no real data.
Design focused deterministic UI tests:
- pure HTML/view-model rendering and HTML-escaping tests (including hostile
  research/observation text, all truth labels, empty/missing/corrupt/swapped-db
  states);
- loopback HTTP/CLI integration tests using an ephemeral port (`127.0.0.1:0`)
  and guarded `TempDir` so tests never collide on a fixed port or leak files on
  failure;
- preservation of all 77 existing tests.
For each proposed test, state the exact file, test function name, setup,
expected result, and the causal regression or invariant it covers.

### 8. CI and gate impact

State how `scripts/verify.sh` and `.github/workflows/verify.yml` will verify
the UI slice. Since `scripts/verify.sh` already runs
`cargo +1.99.1 build --workspace --all-targets --locked --offline`,
`cargo +1.99.1 test --workspace --locked --offline`,
`cargo +1.99.1 fmt --all --check`, and
`cargo +1.99.1 clippy --workspace --all-targets --locked --offline -- -D warnings`,
explain whether `scripts/verify.sh` or `.github/workflows/verify.yml` needs any
change at all, or whether workspace-wide gates automatically cover the new UI
target and tests while keeping `cargo tree -p bookradar-core` at 1 line,
offline execution after locked fetch, and no browser download or secrets in CI.

### 9. Documentation and ADR

Propose the `README.md` update (workspace/binary summary, exact synthetic UI
demo setup and run commands, loopback/read-only/synthetic limits) and whether
one new architecture decision record `docs/adr/0007-local-read-only-ui-shell.md`
should be added. Confirm that `docs/domain-contract.md`,
`docs/research-input-v1.md`, and `docs/adr/0001`–`0006` remain untouched.

### 10. Evidence tier, acceptance, and browser evidence

Propose `Evidence tier: E2` (or a reasoned alternative) with:
- implementation verification via `bash scripts/verify.sh` and local loopback
  demonstration;
- `Independent acceptance: required-separate-fresh-worker` (`Fresh Independent Audit`),
  including automated verification and bounded local browser verification
  (Playwright/Chromium against `http://127.0.0.1:<port>` in a clean isolated
  context with synthetic fixtures only, under the AP Browser Stall Guard
  Contract, with no committed screenshots and no external URLs);
- numbered COOPERATOR rendered acceptance checklist (§16);
- separate post-publication CI run observation on `origin/main`.

### 11. Git and publication boundary

Propose the exact changed-path allowlist, one reviewable local commit with an
exact commit subject, and a normal non-force push to `origin/main` only under a
separate publication grant after `acceptance-PASS` and COOPERATOR sign-off.

### 12. Implementation path and rollback

Provide the ordered implementation stages, stage gates, rollback path, and a
decision table summarizing every material choice requiring COOPERATOR approval
(UI surface/architecture, crate/binary placement, dependency footprint, minimal
slice scope, UI language/wording, visual design, local security controls,
browser acceptance & screenshot policy, ADR 0007, evidence tier & independence,
and publication boundary).

## Validation and completion

Use `status: PASS` when the plan is complete and decision-ready. Use `PARTIAL`
when useful plan content exists but a material evidence gap or missing
capability remains. Use `BLOCKED` when a prerequisite prevents planning.

Report header must begin exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the coordinates once at the top of the report metadata:

```text
Logical whole identity: bookradar-ui-shell
Worker session ordinal: 01
Worker exchange ordinal: 01
```

Include the compact core:
- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: not-applicable`
- `Start commit: a2182302de73cb345b4b646993a1ad25d602555f`
- `End commit: a2182302de73cb345b4b646993a1ad25d602555f`
- `Changed files: none`
- `Tests and validation: <read-only inspection and ./ap/ap doctor summary>`
- `Git result: none`
- `Deviations, risks, or missing evidence: <summary>`
- `Smallest next step: <one smallest next step>`
- `Report justification: new-evidence`
- `Logical-whole closure: not-closed`
- `Authority expiry: this terminal report ends the planning grant; no autonomous continuation.`
- Compact critique and execution issue lines:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, and residual risk>
Pre-Existing Failure Classification: none | <complete classification per the contract>
```

Do not emit a project closure signal. Do not write the report to the repository
or Meta; return it in this session for COOPERATOR persistence at
`/Users/agile/meta/projects/bookradar/00/06-bookradar-ui-shell/01_report_00.md`.

## Stopping conditions

Stop and report without improvisation if:

- the repository root, remote, branch, HEAD, parent, tree, cleanliness, `.ap`
  pin, or `ap doctor` state differs from the declared baseline;
- a required read-only capability is unavailable;
- answering a material planning question would require a repository or Meta
  write, a dependency change, a network fetch into the repository, a secret, a
  host/remote mutation, or a publication action;
- inspection exposes a genuine product defect in `bookradar-core` or
  `bookradar-store` whose repair would change accepted product semantics;
- a material framework, dependency, security, or scope question cannot be
  resolved without guessing.

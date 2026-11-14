# BookRadar — Opening Handout: `bookradar-ui-shell`

**Artifact:** `projects/bookradar/00/06-bookradar-ui-shell/00_handout.md`
**Kind:** provisional opening continuity, domain-dependency and decision-context handout for a fresh per-whole Orchestrator. **Not** a Worker prompt, permission grant, implementation plan, acceptance, publication or closure.
**Authored by:** outgoing per-whole ORCHESTRATOR (direct project checkout), 2026-11-13, under explicit COOPERATOR instruction and full trust. This is not a Master handoff and grants no authority.
**Predecessor:** `projects/bookradar/00/05-bookradar-test-hardening-and-ci/01_closure.md` (`closed-by-ORCHESTRATOR`; implementation PASS, acceptance PASS, publication PASS, CI run success), SHA-256 `9c157d4935020e56056eacbb9251905ee31284fad72444654ed5d7d672ae4b2b`.
**Current public/local baseline:** `a2182302de73cb345b4b646993a1ad25d602555f` (`fix: restore target ignore and run the gates in CI`), parent `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`, tree `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`.
**Current public CI evidence:** workflow `verify`, run `43438422059`, conclusion `success`, head SHA `a2182302de73cb345b4b646993a1ad25d602555f`.
**Earlier closed wholes:** `projects/bookradar/00/00-bookradar-ap-bootstrap/01_closure.md`; `projects/bookradar/00/01-bookradar-domain-contract/01_closure_03.md`; `projects/bookradar/00/02-bookradar-rust-foundation/01_closure.md`; `projects/bookradar/00/03-bookradar-persistence-and-history-slice/01_closure.md`; `projects/bookradar/00/04-bookradar-research-ingestion-contract/01_closure.md`; `projects/bookradar/00/05-bookradar-test-hardening-and-ci/01_closure.md`.
**Logical-whole candidate identity:** `bookradar-ui-shell`.
Handout status: provisional
**Status basis:** provisional until the fresh per-whole Orchestrator reconciles the current repository, Cooperator selection and activated Meta trace. Do not modify this frozen handout in place after opening; material changes use a successor handout under the AP/Meta handoff sequence.
**Intended successor capability profile:** `Orchestrator` (direct project checkout), with `Orchestrator session scope: logical-whole`.
**Upstream author access profile/scope:** `Orchestrator` / `logical-whole` (outgoing session).
**Restoration classification:** PASS for read-only preparation of the first Planner on the observed baseline; current public `main`, local checkout, CI run, toolchain and Meta trace **must** be independently revalidated before any Worker grant. Not implementation readiness.
**Authority:** zero. Neither this handout nor the predecessor closure grants Git, filesystem, browser, SSH, host, dependency installation, implementation, acceptance, publication or Meta mutation.

## 0. Selection rationale and one bounded objective

The COOPERATOR selected `bookradar-ui-shell` with full trust after the
test-and-CI whole closed. The accepted backend is now public and verified:

- `bookradar-core` remains dependency-free and evaluates one supplied
  observation and explicit assessment context.
- `bookradar-store` owns schema v1 observation history and the separate research
  ledger with strict JSON v1, replay/quarantine, candidate projection and no
  auto-verification.
- 77 tests pass; the public `verify` workflow is green; `.gitignore` correctly
  covers `/target/` and `/tests/target/`; AP is pinned and the domain contract is
  revision 1.

The next risk is not another backend contract. It is **product visibility and
usability**: the accepted history, current assessment and research ledger have
no user-visible surface. A person cannot see the accepted truth labels, the
historical/current distinction, the research candidate status or the empty and
error states without reading raw CLI transcripts.

**Single objective proposed for this whole:** establish one minimal, local,
read-only **UI shell** over the accepted synthetic observation store and
research ledger. It must render the accepted labels and timestamped
uncertainty, preserve the separate research candidate statuses, and require no
live ingestion, real retail data, accounts, external network, secrets,
deployment or product-semantics change. The first Planner must choose the
smallest useful vertical or horizontal slice.

Do not attempt in this whole: a live Hermes/Playwright research adapter,
scraping, external APIs, MCP, real retail data, personal state/watchlists,
accounts/authentication, multi-user privacy design, NUC/SSH, a hosted service,
deployment, release automation, a full design system, a broad i18n program, or a
policy decision.

Why this precedes live Hermes / NUC work:

- The backend is accepted and publicly proven; visual product learning is the
  cheapest next risk.
- A read-only local UI can expose semantic mistakes (unqualified “available”,
  colour-only meaning, false “sold out”, research candidates presented as
  verified) before a live adapter adds network, real data and security risk.
- The accepted store/research APIs already expose the needed read models; a
  small shell can exercise them without changing product semantics.
- The existing `scripts/verify.sh` and public `verify` workflow give a
  repeatable Rust gate; the UI slice can extend the gate without re-architecting
  CI.

Alternative next wholes considered but deferred: a live Hermes/Playwright
adapter (requires separate security, network, real-data and host boundaries);
NUC/deployment/release work; personal-state/account policy; a broader design
system. Selection should be revisited only for fresh material evidence or
COOPERATOR redirection.

## 1. Baseline and source precedence

**Canonical repository:** `https://github.com/cisarik/bookradar`
**Public branch:** `main`
**Current public/local commit:** `a2182302de73cb345b4b646993a1ad25d602555f`
**Subject:** `fix: restore target ignore and run the gates in CI`
**Parent:** `d7d49ab6df2d2fd063644700095d5e55a94e4ae1`
**Tree:** `9a922bfd3c908f11b30a4ca04158015f3e0f3eb7`
**Commit date:** 2026-11-13T14:17:54+01:00
**Public CI run:** `43438422059`, workflow `verify`, conclusion `success`, head SHA `a218230…`
**Test count:** 77 (17 core, 10 store unit, 4 old CLI, 13 history, 6 persistence, 2 research CLI, 5 research contract, 20 research ingestion)
**Pinned AP:** `.ap` gitlink `d7023cf037f6d17885c3ede5c04812c61640da50` (immutable; detached expected checkout)
**Accepted product contract:** `docs/domain-contract.md`, revision 1, accepted 2026-11-10
**Accepted ADRs:** `docs/adr/0001`–`0006`; ADR 0006 accepted 2026-11-13
**Verification gate:** `scripts/verify.sh`; `.github/workflows/verify.yml`; README; ADR 0006

Read in precedence order:

1. Project root `AGENTS.md` and the immutable AP at the gitlink: `.ap/AP.md`,
   `.ap/AP_ORCHESTRATOR.md`, and later `.ap/PROMPT_CONTRACTS.md`,
   `.ap/AP_WORKER.md` as routed.
2. Current public `main` and the actual local checkout; verify refs, ancestry,
   tree, cleanliness, submodule, CI run and toolchain independently.
3. Accepted domain contract and ADRs 0001–0006.
4. Predecessor closure and accepted planning/implementation/acceptance/
   publication records as historical evidence.
5. This handout as provisional, non-authorizing context.

At authoring, the outgoing Orchestrator observed public/local `main` at
`a218230…`, a clean worktree, `.ap` detached and clean at `d7023cf…`, strict
`ap doctor` PASS, 77 tests, and public CI run `43438422059` success. The
successor must revalidate these facts before any grant; do not infer them from
this handout. If public/local differs, stop and classify under RF-12 before any
mutation.

## 2. Accepted state and the UI gap

Current repository state at authoring:

- `bookradar-core` is dependency-free and evaluates one supplied observation and
  explicit assessment context.
- `bookradar-store` owns schema v1 observation history plus the separate research
  ledger: strict JSON v1, canonical-byte replay, quarantine, partial-run
  accounting, candidate projection as unreviewed/disputed and no
  auto-verification.
- `bookradar-poc` exercises synthetic observation history and current
  assessment; `bookradar-research` exercises the research ledger. Both are
  process-level synthetic proofs.
- 77 tests pass; `scripts/verify.sh` is the single local/CI gate; the public
  `verify` workflow runs it on `ubuntu-24.04` with read-only permissions and a
  pinned checkout action.
- `.gitignore` correctly covers `/target/` and `/tests/target/`.
- The README documents the gates and synthetic proofs; ADR 0006 records the
  verification policy.
- No UI, web server, browser application, TUI, live adapter, deployment or
  hosted surface exists.
- The domain contract explicitly defers UI and i18n implementation. This whole
  may implement a minimal interface, but it does not revise the contract. Any
  new semantic label, personal state, account, i18n policy or product rule is a
  separate Cooperator decision.

The domain contract constrains every UI rendering:

- **User-facing truth** labels are: `Unverified`; `Last observed available —
  [time]`; `Checked available — [time]`; `Last observed reserved/unavailable —
  [time]`; `Could not recheck — [time] / Listing removed`.
- Historical data must not receive an unqualified green “available” label.
  Text, time and uncertainty carry the meaning; colour alone is insufficient.
- `Checked available` requires the approved reviewer-evidence method and the
  24-hour freshness rule; `eligible`/`verification` must not be presented as a
  purchase guarantee.
- `Never automatically accepted` includes agent-only verified-stock assertions,
  Slovak language inferred from website locale, identity merges from ISBN/title
  alone, access failures interpreted as stock exhaustion, claimed screenshot
  rights and personal ownership inferred from a watchlist.
- Research candidates are unreviewed or disputed; structural validation never
  establishes truth or verified stock. There is no auto-verification and no
  promotion to a verified state.
- Personal state (watches, library, accounts, privacy/multi-user design) is
  deferred. The first UI slice must not collect personal data.
- Screenshot semantics are metadata/reference only; screenshot storage,
  retention, capture rights and public redistribution are deferred. Do not
  commit screenshot files in this whole.

The UI gap is therefore concrete and bounded:

1. no user-visible rendering of observation history or current assessment;
2. no user-visible rendering of the research ledger, its candidates, quarantine
   or conflicts;
3. no consistent empty/missing/corrupt/unsupported-schema states;
4. no local, repeatable demonstration path for the Cooperator;
5. no UI-specific tests, acceptance evidence or documentation.

The new whole must preserve the accepted 77 tests, the public CI gate and all
product semantics. A UI test that exposes a genuine backend defect is a finding,
not permission to change product semantics without a separate decision.

## 3. What the first Planner must evaluate

Ask a fresh Planner to inspect current repository truth and propose **one
minimal executable slice** with evidence for these decisions. It must not
silently promote a web framework, server crate, TUI toolkit, CSS framework,
browser automation, screenshot storage, i18n library, design system or hosting
model to accepted architecture.

1. **As-found state and functional gap.** Verify the current public/local
   commit, parent/tree, AP pin, clean checkout, CI run, test inventory,
   toolchain, `scripts/verify.sh`, `.github/workflows/verify.yml`, README and
   ADR 0006. Record exactly what exists, what is manual-only and what is
   missing. Do not assume the known gaps are the only gaps.

2. **Functional slice and runnable path.** Choose the smallest end-to-end UI
   slice: one local page/dashboard with observation history, current assessment
   and research-ledger status, or a smaller vertical. Evaluate a local web UI,
   a terminal UI and a native shell. Compare development cost, dependency
   footprint, visual acceptance, accessibility, security and CI impact.
   Recommend one, with exact local run commands.

3. **Data and API inventory.** Audit the public read models:
   `Store::open(..., OpenMode::ReadOnly)`, `Store::history`,
   `Store::current`, `HistoryEntry`, `CurrentView`, `CandidateAssessment`,
   `ResearchStore::open(..., OpenMode::ReadOnly)`, `ResearchStore::inspect`,
   `ResearchStore::current`, `ResearchSnapshot`, `ResearchOfferKey`,
   `render_current`, `render_history`, `render_inspect` and
   `render_research_current`. The UI must use accepted APIs rather than
   duplicate eligibility, freshness, identity, research-admission or
   projection logic. Specify exact data shaping and any read-only adapter.

4. **UI truth and exact states.** Propose the exact screens/sections and
   labels for:
   - observation history with observation/ingestion times and evidence state;
   - current assessment with the accepted user-facing truth label, candidate
     identity, conflict/recheck status and verification status;
   - research ledger counts, runs, findings, admissions, rejections,
     quarantines and conflicts;
   - research current candidates as unreviewed/disputed, never verified;
   - empty store, empty research ledger, missing database, corrupt/unsupported
     schema, invalid input and no-candidate states.
   State which text/time/uncertainty carries each meaning and why colour is not
   the only carrier. Do not invent “sold out”, “verified”, “in stock” or an
   auto-promotion label.

5. **Architecture and dependency boundary.** Compare a new `bookradar-ui` crate,
   a new binary inside `bookradar-store`, and another explicitly bounded
   topology. Compare a local HTTP server, an embedded static page plus a small
   JSON endpoint, a TUI and a native shell. Evaluate new dependencies,
   `Cargo.toml`/`Cargo.lock`, workspace membership, `bookradar-core`
   dependency-free preservation, build time, CI fetch/lock behavior and
   rollback. No dependency is accepted by this handout; the Cooperator decides.

6. **Local security and privacy.** Require loopback-only binding
   (`127.0.0.1`), no `0.0.0.0`, no external origins, CDNs, telemetry, remote
   fonts or analytics, no secrets, no accounts, no real retail/personal data,
   no writes to the databases, no database creation/migration, no arbitrary
   file serving, no path traversal, no CORS wildcard and no remote exposure.
   Specify the exact server/assets/route boundary. A remote/LAN/hosted UI is a
   separate secured whole.

7. **Determinism and test infrastructure.** Require a caller-supplied evaluation
   instant (`--now` or equivalent), synthetic fixtures only, read-only database
   opens, no wall clock, no external network, no credentials and no real data.
   Decide whether UI tests exercise pure rendering/state shaping, HTTP handlers,
   a loopback test server or a TUI state machine. Avoid flaky fixed ports and
   shared global paths. Preserve the 77 existing tests.

8. **CI and gate impact.** State how `scripts/verify.sh` and
   `.github/workflows/verify.yml` cover the new crate/binary/tests. If the
   workspace or lockfile changes, name the exact fetch/build/test impact. The
   core tree must remain only `bookradar-core`; tests remain offline after the
   locked fetch; no secrets, browser download, deployment or release in CI. A
   public run after publication is separate evidence.

9. **Documentation and ADR.** Propose the README local-run section, exact UI
   commands, synthetic demo setup and limits. Add one UI architecture ADR only
   if a durable decision is accepted (for example `docs/adr/0007-...`); do not
   modify ADRs 0001–0006 or the domain contract. No license, contribution,
   privacy, security-response, support or release policy. Do not commit
   screenshots or real data.

10. **Evidence tier, acceptance and browser evidence.** Propose E2 or a reasoned
    alternative. A local read-only UI is reversible but user-visible; likely
    E2 with fresh independent acceptance and Cooperator rendered acceptance.
    Define the exact acceptance matrix, negative controls, synthetic browser
    evidence, browser engine/version, origin, clean-context rules, screenshot
    policy and the separate post-publication CI run. No deployment.

11. **Git and publication boundary.** Propose exact paths, one reviewable local
    commit, and a normal non-force push only under a separate publication grant.
    No force, rebase, history rewrite, tags or extra refs. The public CI run
    after publication is separate evidence.

12. **Implementation path and rollback.** Propose exact paths, ordered stages,
    dependency decisions, stage gates, rollback, a local synthetic
    demonstration and the Git/publication boundary. If a UI test exposes a real
    backend defect, stop and report it; do not change product semantics. If a
    framework/dependency or repository setting cannot be verified, surface the
    decision; do not guess.

## 4. Nonnegotiable boundaries

This whole does **not** authorize:

- changing product semantics, `bookradar-core` behavior, schema v1, the research
  wire contract, the domain contract, ADRs 0001–0006 or the accepted research
  ledger behavior;
- a live Hermes/Playwright adapter, scraping, external APIs, MCP, real retail
  data, accounts, authentication, personal state/watchlists/library, multi-user
  privacy design, screenshots committed to the repository, NUC, SSH, sudo,
  services, hosting, deployment, release or production;
- a UI that writes, imports, reviews, promotes, migrates, repairs or creates
  databases; the first slice is read-only;
- a UI that presents research candidates as verified, invents stock exhaustion,
  uses an unqualified green “available” label, or relies on colour alone;
- external network, CDNs, telemetry, analytics, remote fonts or third-party
  assets; the UI is loopback-only and local;
- a broad framework/design-system/i18n program, a new heavy test framework, a
  toolchain upgrade or a release pipeline without a separate justified decision;
- force push, rebased/rewritten history, tags, extra refs or unsafe cleanup;
- updates to `.ap`, the AP gitlink, other projects or Meta Git from a Worker;
- a new license, contribution, privacy, security-response, support or release
  policy without Cooperator decision.

The positive authority in a later Worker grant must name exact paths,
operations, dependencies, commands, browser origin/context, network boundaries,
test commands, Git authority and publication authority. If the Planner proposes
wider scope, hand material options to the Cooperator instead of treating them
as approved.

## 5. Operating model for the fresh Orchestrator

**Stage 1 — read-only restoration.** Read the current root `AGENTS.md` and pinned
AP, verify the public/local commit `a218230…`, parent/tree, CI run
`43438422059`, 77-test inventory, `.ap` pin, clean state, toolchain, README,
`scripts/verify.sh`, `verify.yml` and ADR 0006. Compare the predecessor closure
and the closed whole's records against current evidence. Record the handout
revalidation in the new whole's `00_notes.md` when the activated trace permits.
Do not infer current branch, worktree, CI or Worker state from this handout.

**Stage 2 — reconcile one bounded objective with the COOPERATOR.** Present the
restored state, the UI gap, material uncertainty and one evidence-backed
recommendation. Preserve Cooperator ownership of UI architecture/framework,
the minimal slice, UI language/wording, visual design, dependencies, browser
acceptance, screenshot policy, evidence tier, publication and any repository
setting.

**Initial Planner.** Assign a fresh Worker session `01`, exchange `01`, with
**native Plan Mode required**, read-only repository inspection and a bounded
implementation-planning report. The first exchange is not an implementation
grant. Do not start a second implementation worker; one accountable workstream
only. The first Planner must not implement or write repository/Meta files.

**Later implementation.** After plan reconciliation and Cooperator decisions,
issue a new self-contained grant with exact baseline, allowlist, dependency and
UI decisions, tests, browser acceptance plan, and separately named
Git/publication authority. If the UI adds a new crate, dependency, server or
browser test, use the risk-appropriate acceptance and publication route. The
actual browser acceptance and post-publication CI run are separate evidence.

**Delivery.** Ask the Cooperator once to select manual delivery or authorized
dispatch for this whole; pending a selection, use manual delivery. Preserve the
selection through subsequent grants. The initial Planner needs a client with
actual native Plan Mode; an unavailable native mode requires a suitable client,
not a prompt-level read-only substitute.

**Meta trace.** Preferred new directory:
`projects/bookradar/00/06-bookradar-ui-shell/`, with `00_notes.md` on opening
and this provisional handout. Worker exchange `01/01` is stored, when
activated, as `01_planning_00.md` + `01_report_00.md`; later
implementation/acceptance/publication coordinates follow the actual route.
Preserve the predecessor trace's report-delivery lessons: do not reuse foreign
reports, do not duplicate a report under the same coordinates, and keep Meta
Git Cooperator-owned. The outgoing whole's closure is `05/01_closure.md`; it is
historical evidence, not current authority.

## 6. Quality standard for the UI slice

A credible first slice should aspire to:

- one readable local UI shell, runnable with exact documented commands, opening
  the accepted synthetic store/research databases read-only;
- exact observation-history, current-assessment and research-ledger states,
  including empty, missing, corrupt/unsupported and no-candidate cases;
- accepted truth labels with text/time/uncertainty; no unqualified green
  “available”, no invented “sold out” or “verified”, no colour-only meaning;
- research candidates shown as unreviewed/disputed, never auto-promoted;
- one deterministic evaluation instant, synthetic fixtures only, no wall clock,
  no external network, no credentials and no real data;
- loopback-only binding, local assets, no CDN/telemetry/analytics, no database
  writes, no arbitrary file serving and no remote exposure;
- preserved 77 tests plus focused UI tests; `scripts/verify.sh` and the public
  workflow remain the gate;
- a README local-run/demo section and one accepted UI ADR if the architecture
  decision is durable;
- a reviewable diff with no product-code semantics change, no schema/wire
  contract change and no host/production side effects;
- synthetic browser acceptance in a clean local context; no screenshot files
  committed; no real personal data;
- no unsupported claim that the UI is deployed, hosted, public or production
  ready.

## 7. Suggested acceptance matrix and negative evidence

| Risk/feature | Bounded evidence the Planner should require |
|---|---|
| Baseline and gate | Public/local `a218230…`; CI run `43438422059` success; 77 tests; AP pin `d7023cf…`; `ap doctor` PASS; clean worktree |
| UI runnable path | Exact documented command; local server/terminal starts; reads synthetic DBs; no create/migrate/write |
| Local security | Binds `127.0.0.1` only; no `0.0.0.0`; no external origin/CDN/telemetry; no arbitrary file serving; no secrets |
| Observation history | Exact historical/current labels, observations and times; no unqualified green; no invented stock |
| Current assessment | Accepted candidate identity, conflict/recheck/verification status; `eligible` not presented as a purchase guarantee |
| Research ledger | Counts, runs, findings, admissions/rejections/quarantines/conflicts; candidates unreviewed/disputed; no auto-verification |
| Empty/error states | Empty store, empty research ledger, missing DB, corrupt/unsupported schema and no-candidate states; stable messages |
| Determinism | Caller-supplied instant; no wall clock; synthetic data; no network/credentials; deterministic tests |
| Accessibility/truth | Text/time/uncertainty carry meaning; keyboard/semantic labels; colour is not the sole carrier |
| Tests and CI | 77 preserved plus focused UI tests; `scripts/verify.sh` offline after fetch; core tree unchanged; no CI secrets/browser download |
| Documentation | README local run; ADR if accepted; no domain-contract/ADR 0001–0006 change; no policy addition |
| Browser acceptance | Clean local context, synthetic data, exact engine/origin; no live sites; no committed screenshots; Cooperator rendered acceptance |
| Git/publication | One local commit; normal non-force push only under separate grant; post-push CI run directly observed |
| Product integrity | No core/store/schema/wire-contract/domain-contract/ADR 0001–0006 change; no feature expansion |

## 8. Residual risks and decisions to surface

1. **UI architecture and dependency:** web vs TUI vs native; new crate vs
   binary; server/TUI framework; dependency footprint; `Cargo.lock` and CI
   impact. The Cooperator decides.
2. **Minimal slice:** observation history only, or history plus research-ledger
   status; one page vs multiple views. The Planner recommends the smallest
   useful vertical.
3. **Data access:** use the existing public read models or add a read-only
   adapter; avoid duplicated eligibility/research logic. No direct SQL in the
   UI unless explicitly justified.
4. **UI language and wording:** the domain contract defers detailed Slovak
   wording/i18n; the UI may use Slovak, English or both, but must preserve the
   accepted distinctions. The Cooperator decides the exact wording policy.
5. **Visual design:** minimal functional shell vs a design-system investment;
   no external assets/fonts. The Cooperator decides the visual direction.
6. **Local server security:** loopback binding, request parsing, path
   traversal, asset serving, CSP/CORS, no remote exposure. The Planner must
   specify exact controls.
7. **Browser acceptance and screenshots:** manual vs Playwright/Chromium;
   clean context; synthetic only; no screenshot files committed; no real data.
8. **New dependencies and CI:** locked fetch, Ubuntu build, workspace tests,
   core dependency-free tree, no browser download in CI. Any new dependency is
   a Cooperator decision.
9. **Evidence tier and independence:** E2 with fresh independent acceptance and
   Cooperator rendered acceptance; the actual public CI run after publication
   is separate.
10. **Publication:** one normal non-force push only after acceptance; no force,
    tags, deployment or release; direct public readback and CI observation.
11. **Personal state and accounts:** explicitly deferred; no watchlist, library,
    login, auth, privacy or multi-user design in this whole.
12. **Screenshots and real data:** the domain contract defers screenshot storage
    and redistribution; no screenshot files in the repo; no real retail or
    personal data.

## 9. Readiness review and exact next action

| Review area | Status |
|---|---|
| Predecessor closure | PASS as recorded; `closed-by-ORCHESTRATOR` at `a218230…`; implementation/acceptance/publication PASS; CI run success |
| Current public `main` / local checkout | Observed at `a218230…` during handout authoring; **must be independently revalidated** |
| Test/CI state | 77 tests; `scripts/verify.sh`; public `verify` run `43438422059` success |
| Accepted contract/ADRs/AP | PASS at revision 1 and ADRs 0001–0006; AP pin `d7023cf…` |
| UI state | No UI, web server, TUI, browser app, live adapter or hosted surface exists |
| Cooperator's next whole intent | `bookradar-ui-shell` selected with full trust; material UI/architecture/wording/dependency decisions remain Cooperator-owned |
| Active mutation / Worker sessions | None observed at authoring; successor must recheck |
| Security/host/provider boundaries | PASS for local, synthetic, read-only, loopback-only planning; no live network, real data, secrets or deployment |
| First Planner readiness | PASS **after** current-state revalidation and objective reconciliation |
| Implementation readiness | NOT GRANTED; requires Planner report, decision gate and complete mutation/publication grant |

**Next action for the per-whole Orchestrator:** open this exact handout, read the
pinned AP and current repository, verify public/local state, CI run, tests, AP
pin, toolchain and Meta trace read-only, record the handout revalidation in the
new `00_notes.md` when the trace permits, reconcile the bounded UI-shell
objective with the COOPERATOR, and issue the **first native Plan Mode Worker
prompt** solely for designing the minimal local read-only UI slice. Do not ask
the outgoing Orchestrator to write implementation instructions or accept the
Worker result.

**Fresh Orchestrator restoration prompt (pointer, not authority):**

```text
Resume this AP-integrated project.
Read the root AGENTS.md and the pinned AP documents it names.
Open projects/bookradar/00/06-bookradar-ui-shell/00_handout.md.
Begin read-only. Verify the current public/local commit, CI run, 77-test
inventory, AP pin, toolchain and Meta trace independently. Record the handout
revalidation in the new whole's 00_notes.md when the activated trace permits.
Reconcile the bounded bookradar-ui-shell objective with the COOPERATOR.
Then issue the first fresh Planner prompt (session 01, exchange 01, actual
native Plan Mode required) for a read-only implementation plan. Do not grant
implementation, browser, dependency, Git, publication, acceptance or closure
authority.
```

## 10. Artifact lifecycle and return edge

- **Class:** retained opening continuity and handoff evidence.
- **AP relationship:** historical/consumer handoff, subordinate to governing AP
  and the accepted domain contract.
- **Consumer:** fresh per-whole Orchestrator, its initial Planner, and the
  upstream Master upon closure.
- **Discoverability:** exact Meta location, predecessor closure, public commit
  URL, CI run URL, AP pin, contract revision and ADR 0006 above.
- **Retention:** retain through this whole and archive after closure; material
  correction after opening is a separately named successor handout with
  predecessor/supersession links.
- **Cleanup owner:** COOPERATOR for Meta Git under a separately valid cleanup
  decision.
- **Expected return to Master:** a truthful `xx_closure.md` with exact public
  commit, UI run/demo and CI evidence, completed scope, explicit
  non-achievements, current contract/AP pin, residual risks, recommended next
  logical whole(s), and no implied successor grant.

**Final invariant:** Show the accepted truth before widening the product. One
minimal local read-only UI shell, one accountable Orchestrator, fresh bounded
Worker grants, synthetic/loopback-only evidence, no product-semantics change, no
live data, no external network, no secrets, no deployment and no cross-project
or host side effects.

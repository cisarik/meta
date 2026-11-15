# BookRadar — Successor Handout: `bookradar-local-agent-mvp`

**Artifact:** `projects/bookradar/00/08-bookradar-first-live-listing/01_handout.md`
**Kind:** successor restoration and changed-objective handoff for a fresh per-whole Orchestrator. Not a Worker prompt, implementation plan, permission grant, implementation readiness, acceptance, publication, deployment, or closure.
**Handout status:** successor restoration handoff; not provisional and not a closure artifact.
**Authored by:** ORCHESTRATOR (direct project checkout), 2026-11-14, immediately after explicit COOPERATOR selection of a materially changed objective.
**Successor logical-whole identity:** `bookradar-local-agent-mvp`
**Intended successor capability profile:** `Orchestrator` (direct project checkout `/Users/agile/Projects/bookradar`)
**Orchestrator session scope:** `logical-whole`
**Restoration classification:** PASS for read-only restoration and COOPERATOR decision reconciliation before the successor's first Planner. Not implementation readiness.
**Authority:** zero. No implementation, provider call, retailer request, credential access, browser, dependency, scheduler, service, installation, Git, Meta Git, acceptance, publication, deployment, or closure is granted.

---

## 1. Predecessor disposition and why this handoff exists

The preceding whole was `bookradar-first-live-listing`, opened from:

- `projects/bookradar/00/08-bookradar-first-live-listing/00_handout.md`
  SHA-256 `2ace4353449564220501a6ea1cc91da0cfcee79f1874f3b3180114de238c2752`;
- notes at `00_notes.md` in the same directory;
- prepared Planner prompt `01_planning_00.md`
  SHA-256 `2d7cadeb9aa8bdb2abdb71b70c6ad8365462c421d27cc0dac09df198fa7732ad`.

The COOPERATOR delivered that prompt to a fresh Planner. The resulting file
`01_report_00.md` has SHA-256
`2f7c63fb2769e7bbddba890a2e29f6c7987b1fdbe0cf576275b7f03d37b80f32`.
It failed AP companion integrity: it lacks the mandatory report header,
coordinates, compact core, evidence, required plan sections, and authority
expiry. It explicitly proposed replacing the selected task with a broader MVP.
It is preserved byte-for-byte as a foreign/incompatible artifact, not accepted
as a terminal Worker report or a plan for the old whole.

The COOPERATOR then expressly selected the changed agent/administration/
periodic-monitoring MVP direction. Therefore:

- `bookradar-first-live-listing` is **superseded by COOPERATOR decision**, not
  implemented, accepted, published, or closed;
- its Worker coordinates `01/01` remain consumed and are never reused;
- the successor begins a new logical whole and, when its first Planner is
  actually delivered, fresh Worker session `01`, exchange `01`;
- no planning result, implementation result, acceptance, publication, or closure
  carries over from the superseded whole;
- the foreign artifact is now only non-authoritative brainstorming input for the
  successor, not an accepted design or inventory of COOPERATOR decisions.

The current handoff is the successor continuity artifact. It does not repair or
rewrite the invalid report and does not close the predecessor.

## 2. Verified product baseline at handoff time

- Canonical repository: `https://github.com/cisarik/bookradar`
- Public branch: `main`
- Public/local commit: `80b172c2db6fcacc93041d4eb4c246450547f112`
- Subject: `docs: demonstrate governed conflict resolution`
- Parent: `69ec45e245108c90e2de4302c03ca72572bf1829`
- Tree: `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`
- Public CI: workflow `verify`, run `43600404485`, completed `success`, head SHA
  `80b172c2db6fcacc93041d4eb4c246450547f112`; job `132463717503` and its
  `Verify` step also succeeded.
- Local offline gate: **113 passing tests**, formatting, clippy `-D warnings`,
  one-line `bookradar-core` dependency tree, `git diff --check`, strict AP
  doctor, and clean post-run worktree.
- AP pin: `.ap` gitlink and detached clean checkout
  `d7023cf037f6d17885c3ede5c04812c61640da50`; strict `./.ap/ap doctor` PASS,
  variant `stable`.
- Toolchain: Rust `1.99.1`.
- Product contract: `docs/domain-contract.md`, revision 1, accepted 2026-11-10.
- Wire reference: `docs/research-input-v1.md`.
- Accepted ADRs: `docs/adr/0001`–`0008`.
- Last completed predecessor closure:
  `projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_closure.md`
  SHA-256 `dc19ca8972d158345ddbf149f9f9978d982b6951b88394e4aa94ddb9787d73a2`.

The public ref/commit/CI facts were independently observed by this
Orchestrator through authorized read-only `git ls-remote` and public GitHub API
checks on 2026-11-14. They are mutable anchors and must be independently
revalidated by the successor before any new Worker grant. Local `origin/main`
alone is not public-branch proof. Any divergence requires RF-12 classification,
not silent repair.

At handoff time the product worktree is clean and no active product mutation is
known. The Meta worktree contains unrelated owner changes; preserve them. No
Meta Git operation was performed.

## 3. COOPERATOR-selected successor direction

The selected new direction is a local BookRadar MVP involving:

1. administration/configuration for agent-assisted research;
2. adding a book and discovering/processing offers with external assistance;
3. displaying sourced offer/availability evidence and uncertainty;
4. repeating checks periodically, with visible history and changes; and
5. preserving the existing distinction between untrusted research, explicit
   human review, and positive verification.

The identity `bookradar-local-agent-mvp` is selected for this new whole. Its
exact bounded implementation slice is **not** yet accepted. The first Planner
must read current repository truth and propose one decision-complete plan with
explicit COOPERATOR decisions; it must not treat breadth in the originating
artifact as authority to build everything.

The selected direction does not itself approve:

- NVIDIA NIM, Brave Search, or any other named provider;
- provider calls, accounts, monthly spend, quota, billing, or cost caps;
- API-key collection/storage, macOS Keychain, browser profiles, or credentials;
- a 12-hour interval, catch-up behavior, background execution, LaunchAgent, or
  automatic restart;
- a new SQLite database, schema migration, UI framework, web framework,
  scheduler, Tokio/Axum/reqwest/scraper, or any other dependency;
- three specific Slovak screens, exact fields/buttons, notifications, or a
  writable review UI;
- multiple retailers, a fixed maximum of queries/offers/redirects/bytes, or a
  particular HTTP policy;
- real-provider acceptance, installation, service management, deployment, or
  production operation.

Those remain proposals and COOPERATOR-owned decisions, not accepted scope.

## 4. Originating proposal retained only as brainstorming

The foreign artifact proposed the following ideas. They are retained so the
successor can evaluate rather than reconstruct them, but none is accepted merely
by appearing here:

- Slovak watched-books, book-detail, and settings screens;
- NVIDIA chat completions and Brave Web Search for discovery;
- at most two model-generated search queries and five retailer offers;
- model extraction with quote occurrence checks and research-v1 ingestion;
- sequential HTTPS retrieval, internal-address blocking, three redirects,
  20-second timeout, 2 MiB page cap, and no automatic retries;
- a new `bookradar-app` crate with Axum/Tokio/reqwest/scraper and another SQLite
  database for settings/watches/runs/notifications;
- one worker process, coalesced manual/scheduled runs, resumable import, a
  12-hour schedule, wake catch-up, and notifications;
- macOS Keychain and LaunchAgent;
- proposed provider-call caps and real NVIDIA/Brave acceptance.

The successor should classify each as an option, risk, rejected alternative, or
COOPERATOR decision after repository-grounded planning. It must not cite this
summary as acceptance.

## 5. Existing durable capabilities and invariants

The current repository already provides:

- `bookradar-core` as the sole verification/eligibility authority;
- append-only observation history and deterministic current assessment;
- strict `bookradar-research` v1 admission, quarantine, replay/conflict handling,
  and ledger-local unreviewed/disputed `AgentOnly` candidates;
- `bookradar-review show`, complete positive reviewer-attested `promote`, and
  attributed application-store `review`;
- a loopback immutable read-only UI snapshot with escaped text and no JavaScript,
  writes, forms, JSON endpoint, authentication, non-loopback bind, or monitor;
- 113 offline tests and one canonical `bash scripts/verify.sh` gate.

Preserve these semantic boundaries unless the COOPERATOR expressly changes the
accepted product contract through a separately planned update:

- structural admission is not truth or verified stock;
- source availability is a dated source assertion, not BookRadar verification;
- Slovak interface locale, title, ISBN, model confidence, or search snippet does
  not resolve edition identity or language;
- access failure, CAPTCHA, rate limit, timeout, 404, or disappearance does not
  prove stock exhaustion or sale;
- research text, URLs, provider output, page text, and excerpts are untrusted
  data, never instructions;
- `AgentOnly` cannot become eligible through import, replay, display, or a later
  supported review of that same observation;
- positive promotion remains explicit, complete, attributed, and caller-supplied;
- no automatic reviewer approval, resolved edition, supported knowledge,
  manual/direct-browser evidence, or positive promotion from an agent;
- public CI remains offline and cannot prove current retail price/stock.

The new direction broadens the product surface materially. It must not erase
these safeguards to appear useful.

## 6. First-Planner decision coverage

After restoration and COOPERATOR reconciliation, the successor's first Planner
should address at least:

1. **Exact MVP boundary:** the smallest coherent user-visible result and what is
   deferred from the broad proposal; avoid combining administration, discovery,
   monitoring, service installation, and production acceptance merely because
   they appear in one artifact.
2. **Provider/model/search route:** exact provider purpose, call sequence,
   structured-output contract, privacy, cost/quota, failure behavior, no silent
   fallback, and offline doubles. Every provider and real call remains a
   COOPERATOR decision.
3. **Credential/privacy boundary:** whether secrets are necessary, minimum
   exposure, storage alternatives, redaction, retention, process/browser/
   keychain boundaries, and cleanup. No credential probing or real key in the
   trace.
4. **Search/fetch/extraction trust:** discovery versus evidence, exact source
   provenance, bounded excerpts/quote checks, unsupported claims, URL/redirect/
   DNS/private-address protections, timeouts/caps/retries, and no stock/language/
   edition inference.
5. **Application/UI scope:** Slovak presentation, watched books/detail/settings
   only if selected, write boundary, read-only research display, local bind,
   escaping, forms/CSRF/origin controls if writes are approved, and browser
   acceptance. Existing UI need not be replaced.
6. **Persistence and identity:** whether existing stores and research v1 suffice,
   why any new store/schema is necessary, migrations, run/finding identity,
   replay/resume, notification deduplication, and no second verification kernel.
7. **Scheduling/service:** manual one-shot versus interval, concurrency/
   coalescing, sleep/wake semantics, missed runs, time injection, shutdown/
   restart recovery, and whether LaunchAgent belongs to a later whole.
8. **Runtime/dependencies:** exact crates/packages/versions, lockfile impact,
   provenance, host assumptions, async/service complexity, rollback, and the
   smallest honest option. Public CI and tests stay offline.
9. **Deterministic tests:** exact file/function/setup/expected result/causal
   regression for provider doubles, malformed model/search/page inputs,
   unsupported claims, Czech/unknown language, availability/access failures,
   hostile text/URLs, quotas, restarts, schedules, replay, credential redaction,
   UI security, and preservation of all 113 current tests.
10. **Evidence/acceptance:** proportionate evidence tier and fresh independent
    audit for new provider/credential/network/UI/scheduler trust boundaries;
    exact synthetic transcript; separately authorized real calls only if chosen;
    browser evidence for changed UI; cleanup and explicit non-achievements.
11. **Documentation/ADR:** durable decisions, owner operation, limitations,
    privacy/cost/service notices, and actual COOPERATOR decisions rather than
    Planner-selected policy.
12. **Allowlist/stages/rollback/decision table:** exact paths, ordered separately
    gated stages, narrow-before-broad checks, reversible local rollback, no push
    without publication authority, and every provider/cost/privacy/credential/
    network/browser/data/scheduler/service/UX row COOPERATOR-owned.

The first Planner must not execute real provider/retailer calls, inspect
credentials, install dependencies, launch a browser/service, edit the product,
or imply implementation authority.

## 7. Restoration and routing route for the fresh Orchestrator

1. Read root `AGENTS.md` and the immutable AP at pin `d7023cf…`, including the
   Orchestrator spine and prompt contracts.
2. Read this handout, the superseded whole's `00_notes.md`, the last completed
   closure cited above, the accepted domain/wire documents, and ADRs `0001`–`0008`.
3. Independently revalidate current public/local `main`, commit parent/tree,
   CI `43600404485`, 113-test gate, Rust/AP pins, clean worktree, and Meta state.
   Classify any divergence under RF-12.
4. Create the successor whole under the next Meta sequence, currently expected
   as `projects/bookradar/00/09-bookradar-local-agent-mvp/`, after verifying that
   path and current sequence. Record this handout's locator, predecessor
   supersession, public evidence, unresolved decisions, and delivery selection
   in its `00_notes.md`.
5. Reconfirm the exact bounded MVP slice and material provider/cost/privacy/
   credential/network/UI/scheduler/service choices with the COOPERATOR. Do not
   let the first Planner silently select those material routes.
6. Only then prepare the successor's first fresh Planner prompt as
   `01_planning_00.md` with report `01_report_00.md`, Worker `01`, exchange `01`,
   actual Native Plan Mode ON. No implementation or live external authority.

Reasoning recommendation for that Planner: **High**, because the changed
objective combines provider, credential, untrusted-content, persistence, UI,
scheduling, and service trust boundaries. Recommended context capacity:
approximately **250k tokens**. This is a recommendation, not observed capacity.

## 8. Preserved delivery and persistence decisions

- The COOPERATOR prefers prompt files in Meta over full-prompt copy/paste.
- Delivery selection: **manual COOPERATOR delivery by prompt-file pointer** to a
  COOPERATOR-selected model/session, not automatic subagent dispatch for the
  first Planner.
- The COOPERATOR chooses the model; requested/observed identity and native mode
  must remain distinct in Worker evidence.
- Every assigned Worker must write its complete terminal report directly as a
  Markdown file at the exact Meta report destination, subject to AP path,
  collision, readback, and native-mode completion rules.
- Prompt persistence owner: ORCHESTRATOR; report persistence owner: assigned
  WORKER; Meta Git publication/archival owner: COOPERATOR; archival:
  `wait-for-report`.
- No Worker receives Meta Git authority by virtue of direct report persistence.

## 9. Active state, risks, and non-authority

- Active product mutation: none at handoff time.
- Active valid Worker for the successor: none.
- Superseded Worker exchange: `bookradar-first-live-listing` `01/01`, consumed;
  its output is invalid as a report and supplies no continuing authority.
- No live provider, retailer, credential, browser, scheduler, service, or
  installation operation was performed for the new direction.
- Main residual risks: unbounded MVP scope, provider cost/privacy, secret
  handling, model hallucination and prompt injection, false edition/language/
  stock conclusions, scheduling while asleep/offline, duplicate work after
  restart, new writable UI attack surface, dependency/service complexity, and
  treating a broad proposal as accepted design.

This handout grants no mutation or external-call authority. The fresh
Orchestrator must restore current truth and obtain the necessary COOPERATOR
decisions before issuing the successor's first Planner.

## 10. Artifact lifecycle

- **Class:** retained successor restoration/changed-objective evidence.
- **AP relationship:** consumer/historical context, subordinate to immutable AP,
  project rules, and accepted durable product decisions.
- **Consumer:** fresh per-whole Orchestrator for `bookradar-local-agent-mvp`.
- **Discoverability:** this exact path, superseded whole notes/prompt/foreign
  artifact, public commit `80b172c…`, CI `43600404485`, and predecessor closure.
- **Retention:** preserve as the changed-objective boundary; a material
  correction uses a successor artifact, not an in-place rewrite.
- **Cleanup owner:** COOPERATOR for Meta Git under a separate decision.
- **Return edge:** fresh Orchestrator restoration record and one truthful new
  planning/decision outcome. This handout grants no successor implementation,
  acceptance, publication, deployment, or closure.

# BookRadar — Opening Handout: `bookradar-first-live-listing`

**Artifact:** `projects/bookradar/00/08-bookradar-first-live-listing/00_handout.md`
**Kind:** provisional opening continuity, objective-selection, and decision-context handout for a fresh per-whole Orchestrator. **Not** a Worker prompt, implementation plan, permission grant, implementation readiness, acceptance, publication, or closure.
**Handout status: provisional**
**Authored by:** ORCHESTRATOR (direct project checkout), 2026-11-14, under explicit COOPERATOR request to select one practical next whole. This is not a Master handoff and grants no authority.
**Authority:** zero. No network fetch, live browser, dependency installation, real retail input, implementation, Git, Meta Git, acceptance, publication, deployment, or closure is granted.
**Predecessor:** [`projects/bookradar/00/07-bookradar-review-and-promotion-workflow/01_closure.md`](../07-bookradar-review-and-promotion-workflow/01_closure.md) (`closed-by-ORCHESTRATOR`), SHA-256 `dc19ca8972d158345ddbf149f9f9978d982b6951b88394e4aa94ddb9787d73a2`.
**Current public/local baseline:** `80b172c2db6fcacc93041d4eb4c246450547f112` (`docs: demonstrate governed conflict resolution`), parent `69ec45e245108c90e2de4302c03ca72572bf1829`, tree `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`.
**Current public CI evidence:** workflow `verify`, run [`43600404485`](https://github.com/cisarik/bookradar/actions/runs/43600404485), conclusion `success`, head SHA `80b172c2db6fcacc93041d4eb4c246450547f112`.
**Logical-whole candidate identity:** `bookradar-first-live-listing`.
**Intended successor capability profile:** `Orchestrator` (direct project checkout `/Users/agile/Projects/bookradar`), `Orchestrator session scope: logical-whole`.
**Restoration classification:** PASS for read-only preparation of the first Planner after independent revalidation. **Not** implementation readiness.

---

## 0. Why this whole next

### The real gap

After `07-bookradar-review-and-promotion-workflow`, BookRadar now has a complete
**synthetic** trust-preserving pipeline:

```text
untrusted research v1 JSON
  -> strict validation / quarantine / replay
  -> research candidate (never automatically verified)
  -> explicit full positive reviewer attestation
  -> attributed application observation + review
  -> deterministic current assessment and read-only UI
```

The missing user-facing capability is now unambiguous: **nothing yet turns one
actual public bookseller listing into that first untrusted research JSON.** The
research ledger has no public-data producer. Further offline contract proofs,
more review APIs, a larger synthetic UI, or a deployment discussion would add no
new real evidence. They would continue the pattern of technically complete but
non-operational demos.

### One bounded objective

Select and implement **the smallest useful one-shot public listing reader**. It
reads one COOPERATOR-approved public book-offer page and produces one valid
`bookradar-research` contract-v1 record, or a truthful bounded access-failure
record. An operator can then use the **already implemented** research import,
`bookradar-review show`, read-only UI, and governed promotion workflow to see a
real candidate and decide whether to attest it.

The result must be inspectable reality, not a claimed verification:

- a real candidate with an attributable source/listing reference, actual observed
  access/capture information, source availability wording when clearly present,
  optional price, producer provenance, and explicit uncertainty;
- an untrusted/unreviewed or disputed candidate, normally `agent-only` and
  `not-eligible`; no automatic positive `Checked available` from the reader;
- no invented edition, inferred Slovak language from the website interface,
  inferred condition, inferred exact quantity, inferred shipping total, or
  fabricated source timestamp;
- direct read-only inspection via the existing `bookradar-review show` and
  `bookradar-ui`; a separate human attestation, if supplied, uses the existing
  `bookradar-review promote` and `review` path unchanged.

### What the COOPERATOR should finally be able to try

After implementation and acceptance, a **manual, one-shot, no-login, no-monitor**
workflow with an approved public listing should let the operator:

1. supply one exact listing URL and run the bounded reader;
2. view the resulting research record and its provenance/source uncertainty;
3. import the record into the research ledger without a parser or schema rewrite;
4. render it in the existing read-only local UI;
5. manually review only that candidate with the existing `bookradar-review`
   positive attestation and observe its subsequent application state.

A static public listing is the preferred first target. An identifier and a direct
quote or exact bounded source label is better than a probabilistic or LLM claim.
Do not require a Hermes, MCP, third-party account, agent-provider call, or
scheduled scraper for this first useful result.

### Alternatives deliberately not selected

| Alternative | Why it is not the selected next whole |
|---|---|
| Another offline producer-contract rehearsal | Proves already proven offline behavior and produces no new real result. |
| A larger catalog/matching/ranking slice | There is no real multi-offer corpus to exercise; it risks inventing identity matching. |
| A writable review UI or chat/chatbot interface | Changes the local read-only trust boundary and adds avoidable product surface. |
| Continuous watchlists, polling, notifications, or multi-site scraping | Operationally and legally/security-sensitive, much broader, and benefits from a correct single-listing reader first. |
| NUC, deployment, SSH, services, or production monitoring | No value until a real listing can be ingested and reviewed locally; it would multiply host and deployment risk. |
| General-purpose HTML/LLM extraction of arbitrary merchants | Unbounded scrape and hallucination surface. The first target is one bounded, explicitly selected listing. |

This is the shortest route to a useful smoke-test of BookRadar's actual purpose,
without pretending a machine assertion is verified stock.

---

## 1. Current verified baseline and source precedence

- **Canonical repository:** `https://github.com/cisarik/bookradar`
- **Public branch:** `main`
- **Public/local commit:** `80b172c2db6fcacc93041d4eb4c246450547f112`
- **Parent:** `69ec45e245108c90e2de4302c03ca72572bf1829`
- **Tree:** `578fbe8f958b17230ccdc5e1f13476c5e23c84f3`
- **Public CI run:** `43600404485`, `completed`, `success`
- **Test inventory:** **113 tests**, verified in `bash scripts/verify.sh` and CI
- **Pinned AP:** `.ap` gitlink / detached checkout
  `d7023cf037f6d17885c3ede5c04812c61640da50`; strict `./.ap/ap doctor` PASS
- **Pinned toolchain:** Rust `1.99.1`
- **Product contract:** `docs/domain-contract.md`, revision 1, accepted 2026-11-10
- **Wire reference:** `docs/research-input-v1.md`
- **Accepted ADRs:** `docs/adr/0001`–`0008`; ADR 0008 accepted 2026-11-14
- **Predecessor closure:** `07-bookradar-review-and-promotion-workflow/01_closure.md`
  SHA-256 `dc19ca8972d158345ddbf149f9f9978d982b6951b88394e4aa94ddb9787d73a2`

Read in RF-19 precedence order:

1. Root `AGENTS.md` and immutable AP at the pin (`.ap/AP.md`,
   `.ap/AP_ORCHESTRATOR.md`, `.ap/PROMPT_CONTRACTS.md`, `.ap/AP_WORKER.md`).
2. Current public `main` and local `/Users/agile/Projects/bookradar`, including a
   clean worktree and the successful public CI run.
3. `docs/domain-contract.md`, `docs/research-input-v1.md`, and ADRs
   `0001`–`0008`.
4. The predecessor closure at `01_closure.md`.
5. This provisional handout as non-authorizing context.

Every mutable anchor must be independently revalidated before any new Worker
grant. A change in the public baseline must be classified under RF-12, not
silently repaired.

---

## 2. What already exists, and the exact missing seam

### Existing domain and verification

`bookradar-core` is the sole eligibility authority. A positive label requires
resolved edition identity, Slovak language, readable access, present listing,
explicit available source statement, all three claims covered, `DirectBrowser`
or `Manual` evidence, `Supported` knowledge with `ReviewerApproval`, clear
conflict/recheck state, known timestamp offset, and an instant inside the 24-hour
freshness window. `AgentOnly` cannot qualify even when a reviewer appends
`Supported` + approval.

### Existing research input

`bookradar-research` accepts strict `bookradar-research` v1 JSON. It preserves
raw/canonical bytes, producer/run/finding identity, findings/source/listing
refs, listing generation, time assertions, access/availability/language/price,
evidence, source URL provenance, and uncertainty. It quarantines unsupported or
ambiguous input, records replay/conflict, and projects only ledger-local
`Unreviewed` / `Disputed`, `AgentOnly` candidates. Version identity, schema
v1, and trust boundaries must be preserved.

Useful immutable constraints from the wire contract:

- envelope at most 1 MiB and findings at most 256;
- identifiers use `[A-Za-z0-9][A-Za-z0-9._:-]{0,127}`;
- supported access values are `readable`, `rate-limited`, `captcha`,
  `authentication-blocked`, `timeout`, `transport-error`, `page-gone`;
- availability is `available`, `reserved`, `unavailable`, or `unknown`;
- evidence `reported_method: agent-only` is a producer assertion, never
  verification;
- language/edition identity is not inferred by the importer;
- duplicate-byte detection and append-only provenance are already covered.

### Existing governed review and inspection

`bookradar-review` has exactly:

- `show` — reads a specific candidate read-only;
- `promote` — writes a **complete positive** attributed application observation
  after full reviewer attestation;
- `review` — appends an attributed application review revision with
  `expected_revision` and both caller-supplied instants.

`bookradar-ui` remains an immutable loopback read-only startup snapshot. It
accepts `--source-id`/`--offer-id`, the research key flags
`--producer --source-ref --listing-ref --listing-generation`, `--target-edition`,
and required `--now`. It has no write, form, JavaScript, JSON endpoint,
authentication, non-loopback bind, or monitor loop.

### Missing executable capability

There is no current public HTTP reader, listing-to-JSON mapper, or bounded
fixture-to-producer path for real retail data. Every existing findings file is
synthetic. The handoff seam is therefore small:

```text
public listing URL
    -> bounded read + explicit mapping
    -> research-v1 bytes (untrusted)
    -> existing import/show/UI/review (already working)
```

Do not add a second wire contract, a second store, a new verification kernel,
or a new matching layer merely to fill this seam.

---

## 3. Required functional slice

The eventual implementation must supply three parts, all one-shot and manual:

### A. One bounded public listing read

- One COOPERATOR-approved public URL on one approved retailer host. Start with
  static server-rendered public HTML (or a static embedded structured-data
  object) where possible. Do not coerce a complex browser scenario into scope.
- No login, cookies, browser account, credentials, personal state, captcha
  bypass, anti-bot evasion, form submission, checkout, `POST` to retailer, or
  bypassed TLS verification.
- HTTPS only by default. A bounded host allowlist, no arbitrary redirect chain,
  no private/loopback/link-local targets, and no ad-hoc external URL scanning.
  Decide same-host versus same-registrable-host redirect policy explicitly.
- Explicit byte limit, connect/total timeouts, no unbounded body stream,
  bounded redirect count, single sequential read. Default zero retries; any
  transient retry decision requires an explicit bounded reason, never a retry
  loop.
- Fail access closed, rather than inventing a finding. HTTP failures,
  rate-limit, CAPTCHA, authentication obstruction, timeout, transport failure,
  and page-gone retain their distinct access semantics. They never become
  `unavailable` stock evidence.

### B. One explicit, narrow mapping to research v1

For the chosen listing, extract only supported facts:

- native listing identifier or truthful `unknown` identifier;
- exact requested/resolved URL and explicit material redirect evidence;
- capture/access information and truthful time assertions;
- listing presence/removal/uncertainty;
- availability only when an **exact mapped source phrase or structured state**
  supports it. If ambiguous/missing, emit `unknown`, never assume stock or
  stock exhaustion;
- asking price/currency/basis only when explicitly supported, otherwise null;
- an explicit bounded source statement and/or a short bounded evidence excerpt,
  preserving source meaning without a large page dump;
- language and subject uncertainty preserved. A Slovak site UI does not make an
  edition Slovak; a title alone does not make a resolved edition;
- explicit producer identity and operator-selected run identity/context,
  without inventing model/tool versions;
- uncertainty rationale for missing/ambiguous extraction or mixed stock signals.

If the route needs JSON-LD, static HTML selectors, or headless-rendered text,
that choice must be an explicit preflight/COOPERATOR decision, not a silent
fallback family. Prefer the smallest truthful parser that is justified by the
actual page. Never fit an untrusted page into a positive answer title by fuzzy
score or inference.

### C. One auditable record plus an inspectable operator result

The produced record must be accepted by the existing importer without a wire
change, or fail meaningfully and locally if it cannot represent the facts.

Then demonstrate:

```text
one public listing -> research record -> research import
  -> bookradar-review show
  -> read-only UI render
  -> optional full positive human attestation
  -> bookradar-review promote/review
  -> read-only UI render
```

An `AgentOnly` candidate never becomes eligible through ingestion alone. Import,
display, or replay does not infer verification. Promotion is still explicitly
reviewer-governed.

The UI need **not** change for this first slice: `bookradar-review show` plus the
existing ledger/candidate sections are sufficient. If the COOPERATOR finds the
result too opaque to inspect, the Planner must prove why one small read-only
candidate-detail/read-model enhancement is necessary, before including it.

---

## 4. Recommended delivery shape, subject to the Planner

The default least-connecting design to **evaluate**, not a pre-approved command:

```text
one-shot reader writes one new research-v1 artifact at an operator-selected path
    (fail if the output path already exists)
    -> existing bookradar-research import
```

A separate artifact write boundary avoids silently coupling live read access to
application-store mutation. Do not require a new database or change either
SQLite schema. Keep `bookradar-poc`, `bookradar-research`, and `bookradar-ui`
unchanged in behavior. Evaluate one small new producer binary/adapter versus a
new bounded `bookradar-research` subcommand; the latter currently describes a
four-command synthetic proof and must not be silently expanded.

An actual invocation may end up looking *similar to* this **non-authoritative
placeholder**, but only the Planner-approved decision should define it:

```text
<producer> --url "$APPROVED_LISTING_URL" --out "$RUN_DIR/listing.json" \
  --run <operator-run-id> --captured-at <operator-selected-instant>

bookradar-research import "$RUN_DIR/research.sqlite" \
  "$RUN_DIR/listing.json" <ingested-instant>

bookradar-review show --ledger "$RUN_DIR/research.sqlite" \
  --producer <producer> --run <run> --finding <finding> \
  --receipt <receipt> --position <position>

bookradar-ui --store "$RUN_DIR/observations.sqlite" \
  --research-ledger "$RUN_DIR/research.sqlite" --now <unix-seconds> [...]
```

The operator should not need to write JSON or invent an `assessor`/run
context. Missing timestamp/producer/run defaults need an explicit policy:
fixed test injection for deterministic tests, and a documented host-clock or
operator-supplied policy for the actual one-shot execution. Do not invent times
on a failed read. No generated opaque run identity may collide by using a
random/unseeded value in a deterministic test harness.

---

## 5. Trust, network, privacy, and data-handling boundaries

This whole explicitly **does not automatically authorize** a preflight or
runtime network call. The handoff requires these decisions and grants first.

### Required network envelope

- one explicitly approved public HTTPS host, one chosen exact listing URL;
- no other host unless the COOPERATOR separately approves a redirect source;
- no bypass of robots/access controls, account wall, CAPTCHA, TLS errors, or rate
  limits;
- no generic crawling, URL discovery/offers sitemap expansion, concurrent fetch,
  proxy tricks, repeated polling, background jobs, watchers/schedulers,
  notification services, or real checkout;
- no private-IP/loopback/link-local targets. No public DNS rebinding/redirect
  escapes; declare the exact redirect resolution rule and reject unexpected
  hosts/private addresses;
- no raw response header/full-page body committed in the public trace;
- only a minimal synthetic/reconstructed fixture for deterministic tests, not a
  copied proprietary full-page archive.

### Trust invariants carried forward unchanged

- JSON facts never qualify for `Checked available`.
- Source availability is a source assertion, not a verified conclusion.
- Interface locale does not establish edition language. ISBN/title does not
  resolve edition identity.
- Missing/ambiguous evidence stays unknown; absence of a page label is not proof
  of stock absence; a request failure is not proof of stock exhaustion.
- `404`, generic redirect, or disappearance never proves sale or stock
  exhaustion.
- Request/response bodies and page text remain untrusted data and never become
  instructions, a script, shell fragment, selector executed from the page,
  trusted SQL, unescaped HTML, or a promotional rationale by themselves.
- The adapter cannot set `ReviewerApproval`, `KnowledgeAssessment::Supported`,
  `EditionId::Resolved`, `EvidenceMethod::Manual`, or `DirectBrowser` on the
  reader's behalf.
- Human promotion facts remain explicit and caller-supplied. Do not populate
  positive promotion claims silently from parser output.

### Prohibited collection and collection-adjacent scope

No credentials, personal profiles, cart/wishlist/library state, accounts,
telemetry, screenshots or committed full-page copies, addresses, customer
identifiers, hidden API extraction, or use of obtained data outside this local
research workflow. This is not a multi-user platform or a production service.

---

## 6. What the first Planner must evaluate

The first Planner (fresh Worker `01`, exchange `01`, actual native Plan Mode
ON) must read current repository truth read-only and propose **one bounded,
decision-complete implementation plan**, not perform a live scrape or imply an
implementation grant.

### A. Baseline and exact gap

Independently revalidate the public/local commit `80b172c…`, tree, parent,
CI `43600404485`, AP pin, toolchain, 113-test gate, predecessor closure, and all
relevant reader/importer/reviewer/UI sources. Reconcile this handout against
current code. Classify any public/local divergence under RF-12 rather than
repairing it.

### B. Candidate source and preflight boundary

Recommend **one exact retailer page selection method**, preferably a static
public page. If a selected host is not available, report it rather than
auto-expanding to others. Define how the COOPERATOR chooses the exact
public listing URL before an authorized preflight.

A separately authorized **read-only source preflight**, before code changes,
must establish: the page is public/no-login, actual response access status and
content type, bounded response size, the presence or absence of a robust
structured representation, the exact native listing/status fields, no CAPTCHA or
rate-limit, and whether static extraction is defensible. It must not create a
project file or write a repository artifact. No source-specific implementation
before the exact page and host are approved.

### C. Runtime/fetch/extraction route

Evaluate and compare, considering the smallest safe slice and the actual
selected page:

1. a minimal Rust producer with a pinned narrowly-scoped HTTP/parse dependency;
2. a bounded host `curl` or equivalent process feeding into the existing Rust
   workspace and its existing JSON types;
3. a bounded local Python standard-library reader;
4. a bounded Playwright/Chromium reader only if the page genuinely requires
   rendered content and this is explicitly authorized.

Prefer static public HTML/JSON-LD where adequate. Do not add a generic browser
scraper, agent framework, Hermes/MCP transport, LLM call, or broad HTML text
heuristic by default. Every dependency/runtime choice must state exact package
and version (if any), lockfile impact, provenance, expected system assumptions,
and rollback. Prefer zero new external crates if that is honest and testable.

### D. Exact URL, HTTP, redirect, and failure policy

Specify the host allowlist, HTTPS/TLS verification, URL normalization bounds,
DNS/private-address handling, host/same-registrable redirect behavior,
connect+total timeout values, byte cap, content-type handling, charset/decoding,
maximum reads and redirect count, concurrency=1, no-login/no-cookie/no-proxy,
and no automatic retry. Define structured outcomes for 401/403/404/410/429/
5xx/timeout/invalid content. Retain separate access from availability and listing
disposition. Preserve the first causal failure without turning it into a second
conflated error.

### E. Exact extraction mapping

Specify how source availability tokens, price amount/currency/basis, listing
identifier/generation, requested/resolved URLs, source statement, bounded
excerpt, title/ISBN candidates (if captured), and uncertainty map to
**valid research v1**. Include exact selector/data-origin precedence. Keep
alternative/conflicting states unknown. Emit no positive statement from page
existence, advertising text, or similarity alone. Distinguish listing `404` from
network/transport failure and stock state.

Spell out when `subject.state` is `unknown` vs `candidate`, and how native
ISBN/title data is preserved as candidate evidence without resolving an
edition. If there is no public extraction evidence for language, use
`unknown`.

### F. Producer/run/time/output identity

Specify deterministic `--producer`, `--run`, findings IDs/findings generation,
what the operator must supply, what can be documented default, how the output
artifact is bounded/new-only, and how no partial JSON/ledger receipt is created
on failure. Preserve canonical-byte replay behavior.

Times must separate observed source access from later ingestion. A host clock
for a live manual run requires an explicit decision; deterministic local tests
must remain injected, not depend on `SystemTime::now()` or wall clock. Do not
parse/normalize arbitrary page time as a verified time.

### G. Operator-facing testable path

Document the exact smallest interaction for importing the record and inspecting
it via `show` and `bookradar-ui`, even if that is more than one command. Do not
force a broad UI change just to hide the workflow. If a candidate remains
`unreviewed/not-eligible` as intended, show it. Only then, with a **separate**
positive human attestation, use `promote`/`review` to observe a positive state.

Require the docs to distinguish:

- live candidate from synthetic test data;
- producer extraction from human review;
- "public source said availability" from "BookRadar verified availability";
- manual one-shot operation from monitoring or deployment.

### H. Deterministic tests and regression matrix

Give exact new tests (file, function, setup, expected result, causal regression)
for at least:

- static fixture -> exact research JSON -> accepted import -> candidate
  inspection/verified read-only rendering;
- known availability token, unknown/ambiguous token, missing status, removed
  listing, mixed/reserved states, and static structured data;
- malformed, oversized, wrong-content-type, and instruction-bearing page input;
  hostile Unicode/HTML/URL/statement text;
- no edition/language inference from a Slovak-interface or title alone;
- access failure taxonomy: 401/403/404/410/429/CAPTCHA/timeout/invalid content;
- unexpected redirect host/private target/rebinding, proxy/TLS failure, and
  timeout output-zero behavior;
- no output/ledger mutation on failed mapping, no overwrite of existing output,
  no partial artifact;
- repeated import replay and no duplicate/promoted truth;
- zero new network calls from the canonical offline gate and full current suite;
- boundary input timestamps and fixed producer identity;
- source statement and bounded excerpt rendered escaped in `show`/UI;
- retained current tests and default 1/1 unchanged.

Keep offline fixtures tiny, synthetic, and versioned with the extraction
implementation; do not commit a third-party full page. If a source-derived
minimal excerpt is needed, choose its privacy/copyright/redaction boundary
explicitly and obtain a decision.

### I. CI, build, and dependency impact

`bash scripts/verify.sh` and `.github/workflows/verify.yml` must not silently
gain a network dependency or make public CI depend on a live retailer. All new
behavior must compile, format, clippy, and test offline. State whether the
existing gate needs bounded changes (default: no), and whether any dependency is
added to `Cargo.lock` (default: prefer none if defensible). Preserve
`#![forbid(unsafe_code)]` and `#![deny(warnings)]`-grade clippy outcomes.

### J. Documentation and ADR

Propose `README.md` walkthrough of a single-listing owner operation, exact output
inspection, no-login/no-monitor/no-guarantee notice, and ADR `0009` recording
the selected adapter, network, mapping, evidence, and no-auto-promotion
boundary. Preserve domain contract, research wire, schemas, and ADRs 0001–0008.
ADR text must reflect actual COOPERATOR-selected decisions, not just the
recommendation.

### K. Evidence and independent acceptance

Recommend a separate read-only live-source preflight before mutation, then E3
with a separate fresh independent audit because this introduces real
external/untrusted content and a new trust/network decision surface. Do not let
an implementation Worker self-certify this part.

Define bounded acceptance:

- offline project gate with every pre-existing test and every new test;
- independently reconstructed synthetic CLI transcript;
- one manual real-listing attempt only when the source/network decision exists,
  with a declared URL/result snapshot not full-page capture;
- browser verification if UI/code displays new untrusted content: local
  Playwright/Chrome, desktop/mobile, console/network/security headers, escaped
  content, no positive promotion. Use the Browser Stall Guard Contract;
- independent auditor records exact untrusted inputs, negative results,
  unavailable/partial/not-eligible truth, all changed paths and no other host
  calls;
- cleanup of adapters, demo DBs, listeners, and all external fetch artifacts.

If the chosen source cannot be accessed publicly, use recorded failure or stop;
never substitute fabricated success. Network reachability and dynamic content are
not permanent proof of correctness; they are time-boxed manual evidence. Public
CI remains offline and cannot be used to establish a current retail price.

### L. Exact allowlist, stages, rollback, and decision table

Require a changed-path allowlist, ordered stages, a no-network-before-preflight
boundary, narrow validation before full gate, one coherent commit proposal,
reversible local rollback, no push until a separate accepted publication grant,
and a complete material decision table.

Every live host/URL/dependency/network/browser/data/UX acceptance row stays
COOPERATOR-owned.

---

## 7. Decisions the COOPERATOR must see before implementation

Current handout deliberately does **not** settle these:

| Decision | Recommended direction / why | COOPERATOR decision |
|---|---|---|
| Retailer host and exact public listing URL | One supplied static public listing, not a crawler or a merchant catalog | **pending** |
| Read-only source preflight before edits | Required before any live invocation; one URL, one bounded page read | **pending** |
| HTTP/parse runtime | Prefer the smallest honest option after static-preflight, ideally no new dependency | **pending** |
| Network policy | HTTPS, one public allowlisted host, strict caps/timeouts, no retries, no concurrent reads | **pending** |
| Redirect policy | Default reject unexpected hosts/private targets; explicitly decide safe same-host redirects | **pending** |
| Output command shape | Separate one-shot artifact producer is the default; keep the four-command research proof and read-only UI unchanged | **pending** |
| Extraction route | Exact structured fields or narrow selectors; no fuzzy stock/edition/language inference | **pending** |
| Temporal policy | Test-times injected; live manual host clock vs operator-selected time needs a documented decision | **pending** |
| Fixture/data retention | Tiny synthetic fixtures; no proprietary full-page dumps/screenshots committed | **pending** |
| UI visibility | Existing `show` and ledger/candidate panels first; no extra UI unless demonstrably needed | **pending** |
| Evidence and acceptance | Separate live-source preflight, E3 independent audit, browser evidence only if UI content changes | **pending** |
| Dependency / lockfile | No new dependency unless chosen after preflight and recorded in ADR 0009 | **pending** |

Do not issue an implementation grant until these are reconciled into one exact
bounded envelope. Any source, dependency, or host change after that is a new
decision, not implementation freedom.

---

## 8. Why this remains an honest smaller MVP step

The whole does **not** promise a monitor, correctness for every retailer,
automatic edition matching, full catalog search, or guaranteed current stock.
It gives the first deliberate piece of real evidence into an already working
trust pipeline. That is the smallest useful end-to-end behavior the COOPERATOR
can see and evaluate.

A result that says a page was readable and had status
"source says available at time T; unreviewed, agent-only, not eligible" is an
honest visible result. It is better than another simulated stock claim.

Do not "make it useful" by promoting automatically later: use the real candidate
to prove whether the current review workflow is adequate for a human. Any actual
friction discovered (ugly inspection, missing detail, invalid status mapping) is
a specific next decision, not reason to bypass trust.

---

## 9. Residual risks to name, not hide

1. **Static parsing brittleness:** a host can change its public markup tomorrow.
   Keep source mapping narrowly owned and fail closed; public CI uses fixtures.
2. **Dynamic content/anti-bot:** a chosen site may refuse public reads. Do not
   escalate to VPN/proxy/captcha bypass; select another approved static host or
   stop.
3. **Stock-label ambiguity:** a seller may say reserved, due soon, on order, or
   a marketplace's status "available" without an attributable directly buyable
   copy. Preserve language uncertainty and unknown availability.
4. **Source identity and listing reuse:** native ids can be missing/changed or
   reused across generations. Record candidate identity; do not infer continuity.
5. **Privacy/copyright:** minimize text/excerpts, screen out sensitive content;
   no browsing account state or full-page artifact in the trace.
6. **Host and dependency costs:** host utilities/browsers are not automatically
   available on another machine. Pin or document them; an unavailable dependency
   is not silent success.
7. **Time-based status volatility:** real listing observations age quickly;
   freshness semantics already suppress stale positive labels. No false current
   monitor claim.
8. **Review usability:** if inspection is too obscure for a human, measure that
   when comparing candidate detail output. Do not add unrequested browser write
   behavior merely for polish.
9. **Trace/config mutation:** source-specific code, config, and test paths must be
   in the eventual allowlist; no ad-hoc URLs in `scripts/verify.sh`.

---

## 10. Fresh Orchestrator restoration route

1. Read root `AGENTS.md` and AP pin at `d7023cf…`.
2. Read this handout and predecessor closure
   `07-bookradar-review-and-promotion-workflow/01_closure.md`.
3. Independently verify current public/local `main` (handoff at `80b172c…`),
   CI run `43600404485`, 113-test gate, toolchain, AP pin, and Meta trace.
4. Reconcile the COOPERATOR's selected bounded objective, the exact public host/
   listing candidate, allowed network, runtime, dependency, source, fixture, and
   acceptance choices. **Do not let the first Planner silently select a live
   target without the necessary capable preflight and COOPERATOR choice.**
5. Record a handout-revalidation record in the new whole's `00_notes.md` when the
   activated Meta trace allows. The opening filename is normal `00_handout.md`;
   handoff sequence position `00`, so a later closure will be `01_closure.md`.
6. Then issue only the first fresh Planner prompt (`01_planning_00.md`,
   `01_report_00.md`, Native Plan Mode actual ON). No implementation authority,
   no live preflight, browser, dependency, Git, publication, acceptance, closure,
   or Meta Git authority by that Planner.

Suggested restoration pointer for the receiving per-whole Orchestrator:
`read this handout and the cited closure, independently verify its anchors,
reconfirm the selected objective and live-source/network decisions with the
COOPERATOR, then prepare the initial repository-grounded read-only Planner.`

---

## 11. Artifact lifecycle and non-authority

- **Class:** provisional retained opening continuity and decision-context
  evidence. Frozen when its whole opens; a material rewrite after opening uses a
  successor handout under the Meta sequence.
- **AP relationship:** consumer/historical context, subordinate to immutable AP,
  project rules, and the accepted domain contract. This document itself changes
  no product or protocol behavior.
- **Consumer:** the fresh per-whole Orchestrator and the first Planner.
- **Discoverability:** this exact handout, predecessor closure at `01_closure.md`,
  public commit `80b172c…`, CI `43600404485`, and ADR 0008.
- **Retention/cleanup owner:** COOPERATOR for Meta Git under a separate decision.
  No Meta Git operation was performed.
- **Return edge:** this handout must yield one truthful plan/review decision and,
  if actually implemented/accepted/published later, a closure with concrete
  machine evidence and non-achievements. It grants no successor whole.

**Final invariant:** make the first real public listing visible as untrusted
evidence, not an unearned stock guarantee. Progress is an observable candidate a
person can inspect and review offline, not unattended scraping, automatic
promotion, or a production deployment.

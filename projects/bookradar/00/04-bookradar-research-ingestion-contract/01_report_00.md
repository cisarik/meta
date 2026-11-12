### Report for ORCHESTRATOR_CHAT

Logical whole identity: bookradar-research-ingestion-contract  
Worker session ordinal: 01  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Worker session profile: Planner  
Phase: planning  
Task identity: BOOKRADAR-RESEARCH-INGESTION-PLAN  
Status: PASS  
Phase-qualified result: not-applicable  
Evidence tier: E0  
Report justification: new-evidence  
Logical-whole closure: not-closed

# BookRadar research ingestion — implementation proposal

The bounded plan is complete. During planning, the COOPERATOR selected **strict JSON** and a **separate SQLite research ledger**. These selections establish the proposal’s direction; they grant no implementation or dependency authority.

Start and end state, unchanged:

- BookRadar: `c93f5262ca27050922cc658424c298913852eaff`.
- Tree: `b2ad12353723009944521c15ac2016970337c1df`.
- Parent: `bd23b08cd315a7b3c7a549479db59cbe6ad2adce`.
- AP: `d7023cf037f6d17885c3ede5c04812c61640da50`, detached and clean.
- Changed files and purpose: none.
- Validation: repository, public refs, documentation, source, tests and environment inspected read-only. **No Rust build, storage implementation, dependency installation, dependency resolution or test suite ran.** No `ap` subcommand ran.
- Git result: no fetch, stage, commit or push. Exactly two identical public reads ran: `git ls-remote --symref https://github.com/cisarik/bookradar refs/heads/main HEAD`; both returned the expected commit for `main` and symbolic `HEAD`.
- Persistence: none. The complete report is returned here for COOPERATOR persistence as `01_report_00.md`.

## 1. As-found state

The physical working directory and Git top level match the granted BookRadar checkout. `main`, local `HEAD`, `origin/main`, public `main` and public symbolic `HEAD` agree. The worktree and index are clean; there is one worktree and no active merge, rebase, cherry-pick or revert.

Repository commands inspected:

```sh
pwd -P
git rev-parse --show-toplevel
git remote -v
git status --porcelain=v1 --branch --untracked-files=all
git rev-parse HEAD
git rev-parse 'HEAD^{tree}'
git log -1 --format='%H%n%s%n%T%n%P'
git for-each-ref
git worktree list
git ls-files
git submodule status
git ls-tree -r --name-only HEAD
git ls-tree HEAD .ap
git -C .ap rev-parse HEAD
git -C .ap status --porcelain=v1 --branch
git -C .ap remote -v
git diff --stat
git diff --cached --stat
git diff --check
git diff --cached --check
```

Git operation paths and lock filenames were inspected using `git rev-parse --git-path`, `ls` and `find`. The only lock-named file found was the empty `.git/cursor/crepe/build.lock`, classified by its location as a Cursor build marker, not a Git transaction lock. Client capture refs are present; they introduce no additional branch or worktree.

The accepted boundaries are:

| Boundary | Directly inspected state |
|---|---|
| Core | Dependency-free verification of one `Observation` and explicit `VerificationContext`; caller supplies time. |
| Store | `Store::create/open/append/append_review/history/current`; private connection and transaction ownership. |
| Schema v1 | Five tables, append-only observation/review triggers, application id `0x42524452`, exact schema-object checks. |
| History | Observation-time ordering, persistent equal-time conflicts, failed-recheck suppression, conservative unknown-time handling. |
| Existing CLI | Four fixed synthetic commands; no import surface. |
| Test inventory | 17 core, 7 store unit, 6 persistence, 13 history and 2 CLI tests, confirmed from source. Passing results remain predecessor evidence, not results from this exchange. |

There is no envelope parser, producer/run/finding identity, research ledger, quarantine, or import replay mechanism. Adding tables to existing databases would fail their exact schema checks. The current public API offers no transaction an independent importer could join.

Mandatory AP anchors, the full Worker spine, contract, ADRs 0001–0004, Cargo files, core/store sources and tests were inspected. The supplied Meta handout, notes and predecessor closure were readable. Hash checks confirmed:

- Handout: `316ca28a302479db22f95c78f22f3ea467339a13f9b11aa26ceabb63e8e54ee2`.
- Pasted request and prepared planning prompt: identical SHA-256 `e90d78c5913941523d523d9ee053cb4ec28b620eb674e4ed5021179b5593128b`.
- Predecessor closure: `4811b847eac398a4ff735a1a54b2ba8fcb5f75fa4ed9868935ef98b2965c0dc9`.

The notes classify the predecessor report-placement narrative as stale. No Meta search, Git reconciliation or corrective write is proposed.

Environment commands included `command -v`, explicit Rust binaries under `$HOME/.cargo/bin`, component/toolchain listings, `uname -sm`, `sw_vers`, and available executable version checks. Observed:

- Rust `1.99.1`, commit `58cf8f9c35b355199727627d07ae34a4e2846d67`.
- Cargo `1.99.1`; rustfmt and clippy installed.
- Rust executables absent from the default PATH; explicit binaries work.
- macOS `27.2`, Darwin arm64.
- System SQLite CLI `3.54.0`; Apple clang `21.0.0`; pkg-config `3.0.10`.
- Existing lockfile pins `rusqlite 0.37.0` and `libsqlite3-sys 0.35.0`.

System SQLite CLI availability does not establish the bundled library version or availability of a system development library. Dependency caches were not inspected.

Capability handshake:

| Capability | Classification |
|---|---|
| Client/model | Codex client inferred from runtime context; exact serving model unknown/not observably exposed. |
| Reasoning/context | High and approximately 250k requested; effective settings/capacity unknown/not observably exposed. |
| Native planning | Directly observed active Plan Mode controls; consistent with the required route. |
| Filesystem reads | Directly observed access to the named BookRadar, AP, attachment and Meta sources. |
| Shell/Git | Directly observed read-only inspection and Git checks. Mutation capabilities untested and ungranted. |
| Network | Directly observed canonical Git public-ref reads only. Other network capabilities untested. |
| Toolchain/native tools | Directly observed versions listed above. |
| Missing required capability | None for this planning exchange. |

Capability grants no authority.

## 2. Functional slice and runnable path

Implement a library validator/importer and one thin `bookradar-research` binary inside `bookradar-store`.

The separate research database retains raw submissions, run provenance, per-finding dispositions and candidate observations. Existing v1 databases are never migrated or used as import targets.

Commands:

```text
bookradar-research init <ledger>
bookradar-research import <ledger> <input.json> <ingested-unix-seconds>
bookradar-research inspect <ledger>
bookradar-research current <ledger> <producer> <source> <listing> <generation> <target-edition-id> <now-unix-seconds>
```

`init` exclusively creates a new ledger. Other commands require an existing compatible ledger. Input comes only from the explicit CLI file; references inside the payload are never opened.

Demonstration, after the separately authorized build:

```sh
target/debug/bookradar-research init target/research-ingestion/demo.sqlite
target/debug/bookradar-research import target/research-ingestion/demo.sqlite crates/bookradar-store/tests/fixtures/research/partial.json 1793545201
target/debug/bookradar-research import target/research-ingestion/demo.sqlite crates/bookradar-store/tests/fixtures/research/partial.json 1793545202
target/debug/bookradar-research current target/research-ingestion/demo.sqlite synthetic:producer synthetic:source OFFER-A generation-1 10 1793548800
target/debug/bookradar-research import target/research-ingestion/demo.sqlite crates/bookradar-store/tests/fixtures/research/conflict.json 1793545203
target/debug/bookradar-research inspect target/research-ingestion/demo.sqlite
```

Exact principal outputs:

| Invocation | stdout | Exit |
|---|---|---:|
| Init | `created research_schema=1` | 0 |
| First partial import | `run=partial seen=3 admitted=1 replayed=0 rejected=1 quarantined=1 conflicts=0 projected=1` | 3 |
| Identical partial replay | `run=partial seen=3 admitted=0 replayed=1 rejected=1 quarantined=1 conflicts=0 projected=0` | 3 |
| Current before conflict | `candidates=1 conflict=clear recheck=clear verification=not-eligible` | 0 |
| Changed F1 payload | `run=quarantined seen=1 admitted=0 replayed=0 rejected=0 quarantined=1 conflicts=1 projected=0` | 3 |
| Current after conflict | `candidates=1 conflict=unresolved recheck=clear verification=not-eligible` | 0 |

After those imports, `inspect` prints:

```text
envelopes=2 runs=1 findings=4 observations=1 reviews=2
input=1 finding=0 outcome=admitted reason=none knowledge=disputed
input=1 finding=1 outcome=rejected reason=missing-finding-id
input=1 finding=2 outcome=quarantined reason=invalid-availability
input=2 finding=0 outcome=quarantined reason=identity-conflict
```

An exact envelope replay adds no receipt, observation or assessment.

Exit policy:

- `0`: successful operation, including complete replay, empty inspection, or non-eligible current assessment.
- `3`: persisted partial/quarantined input, including malformed or unsupported envelopes.
- `2`: usage errors, invalid operator-supplied identifiers/times, or oversized input rejected before storage.
- `1`: filesystem, incompatible ledger, busy database, range or transaction failure.

Errors use stable categories on stderr. Findings are printed in receipt/position order. Arbitrary payload text is not interpolated into terminal diagnostics.

Deferred: live producers, application-store promotion, reviewer approval/resolution commands, catalog matching, screenshots, UI, network APIs and deployment.

## 3. Input contract and versioning

Representation comparison:

| Representation | Assessment |
|---|---|
| Strict JSON with serde | Selected. Existing tooling and readable nested provenance justify two Rust dependencies. Duplicate detection and strict field validation must be implemented explicitly. |
| Custom line-oriented format | Avoids new crates, but requires new framing, escaping, nesting, duplicate and canonicalization rules. Rejected for this slice. |
| Additional representation | None proposed; a second decoder would enlarge the boundary without improving the demonstration. |

Envelope fields are exactly:

```text
contract: "bookradar-research"
contract_version: integer 1
producer_id: identifier
run_id: identifier
run_context: ProducerContext
reported_run_outcome: succeeded | partial | failed | unknown
findings: array<Finding>
```

`ProducerContext` contains exactly `agent`, `model`, `skills`, `tools`, and `context`. Agent/model entries are nullable `{name, version}` objects, with nullable version. Skills/tools are nullable arrays of the same shape. Context is nullable opaque text. Null means unavailable; an empty array means supplied as empty.

Every finding contains exactly:

```text
finding_id
source_ref
listing_ref
listing_generation
subject
times
facts
evidence
uncertainty
```

Definitions:

| Field | Shape |
|---|---|
| Source/listing/generation | Nullable opaque identifiers; URL is not substituted for identity. |
| Subject | `{state: candidate|unknown|conflicting, candidate_ref: string|null, identifiers: array}`. Identifier entries preserve `{kind, value, scope, diagnostics}`; no ISBN matching is performed. |
| Times | `observed_at`, `accessed_at`, `captured_at`, `source_updated_at`, each a timestamp assertion. |
| Facts | `language`, `access`, `listing`, `availability`, `source_statement`, `price`, `claim_text`. |
| Evidence | Array of `{reference, reported_method, state, supports, excerpt}`. |
| Uncertainty | `{rationale: string|null, reported_confidence: string|null}`. |

Use existing core domains for language, listing, availability and known access values. `access: null` explicitly means unknown. Source statement, price and claim text may be null.

Evidence methods are `manual`, `direct-browser`, `agent-only`, or `unknown`; evidence states are `present`, `missing`, `partial`, `obscured`, `inaccessible`, or `unknown`. `supports` names subject, language, availability, access, listing or price claims. These remain producer assertions.

A price is null or `{amount, currency, basis}`. Amount is a nullable nonnegative decimal string; currency is a nullable three-uppercase-ASCII-character asserted code; basis is `per-copy`, `per-lot`, or `uncertain`. A known amount requires currency. No floating arithmetic, currency conversion, shipping default, unit-price derivation or price history is introduced. Ranges require a later contract extension.

Rules:

- Required fields must be present. Null is accepted only where explicitly permitted.
- Identifiers use `[A-Za-z0-9][A-Za-z0-9._:-]{0,127}` without case folding or trimming.
- Supplied references/text must be nonempty and contain no NUL.
- Maximum envelope size: 1 MiB; maximum findings: 256; maximum nesting: 32.
- Bound file reads to the maximum plus one byte before parsing.
- Detect duplicate decoded object keys recursively before constructing ordinary JSON objects. Any duplicate quarantines the whole envelope, including escaped equivalents such as `a` and `\u0061`.
- Unknown envelope/context fields quarantine the envelope. Unknown finding fields quarantine that finding. Retain raw bytes; ignore no fields.
- Check contract name/version before interpreting v1 fields. Unsupported versions are retained as opaque quarantined envelopes.
- Malformed JSON/UTF-8 and malformed headers are quarantined without guessed finding counts.
- Semantic input version, fingerprint version, ledger schema version and product-contract revision are separate.

No executable JSON Schema dependency is proposed. The decoder, documented field contract and fixtures form the executable wire boundary.

## 4. Identity and provenance

Replay identity is exactly:

```text
(producer_id, run_id, finding_id)
```

Producer identity is declared provenance, not authenticated identity. Finding identifiers are scoped to one producer/run.

A comparable research offer uses:

```text
(producer_id, source_ref, listing_ref, listing_generation)
```

Only complete tuples form shared candidate groups. Cross-producer matching, URL matching and uncertain listing continuity remain deferred. Findings lacking a complete tuple can still be admitted as unreviewed research candidates, without an observation projection.

Run context is immutable under `(producer_id, run_id)`. Changed context is retained as a run conflict. `reported_run_outcome` belongs to a submission and never determines finding quality.

A timestamp assertion contains exactly:

```text
original: string|null
offset_seconds: integer|null
instant: null | {unix_seconds: signed i64, nanoseconds: integer}
```

Nanoseconds are `0..999999999`; offsets are within ±64800 seconds. A known offset requires an instant. Unknown offsets/times remain explicit.

Numeric instants define wire time interpretation. Original text is retained as an opaque producer assertion; this slice does not parse RFC3339 text or claim that text and numeric values have been independently reconciled. Checked arithmetic rejects unrepresentable values. Ingestion time comes from `ImportContext`, never from the wall clock or payload.

Preserve requested/resolved URLs and material redirects in source provenance by adding these exact nullable finding fields inside a `source_provenance` object: `requested_url`, `resolved_url`, and `redirect_reference`. This object is required alongside the finding fields above.

Candidate subject references remain producer-scoped hypotheses. They never become an `EditionId`, merge editions, or create an edition registry record.

## 5. Admission and quarantine

Validation proceeds through bounded framing, duplicate-safe JSON parsing, header/version validation, per-finding structure, invariants, replay assessment and candidate projection.

Per-position outcomes are:

- `admitted`: validated research candidate, initially unreviewed.
- `replayed`: identical known finding; no new candidate or assessment.
- `rejected`: no usable finding identity, including non-object entries or missing/invalid `finding_id`.
- `quarantined`: recoverable finding needing reconciliation, including invalid fields, unsupported shapes, invariant failures or identity conflicts.

Oversized input is rejected before ledger storage. Rejected finding positions remain accounted in the retained envelope receipt; they create no identity or application observation.

For a supported envelope with `N` positions:

```text
N = admitted + replayed + rejected + quarantined
conflicts <= quarantined
projected <= admitted
```

`conflicts` counts quarantined positions classified as identity/run conflicts.

Application run outcome is `complete` when no position is rejected/quarantined, `partial` when usable and rejected/quarantined positions coexist, and `quarantined` when no usable position remains. Empty valid runs are complete. Uninterpretable envelopes use `seen=unknown`.

Missing evidence, unknown subject, unknown timestamps and unreviewed claims can remain valid candidates. Invalid enums, dangling evidence claim names and inconsistent money are quarantined. Access failures claiming stock exhaustion are quarantined with `inconsistent-access-stock`; they never create an unavailable observation.

Passing validation establishes no truth, approval, eligibility or verified stock. Assessment records use `rule:research-admission-v1` and stable rationale codes. Embedded instructions remain ordinary text.

## 6. Replay and conflict

Use **canonical content bytes as the fingerprint**, without a hashing crate:

- Recursively sort object keys.
- Preserve array order and decoded string content.
- Serialize scalars with the pinned JSON implementation.
- Apply no Unicode, URL, identifier, timestamp-text or decimal-string normalization.
- Name this rule `canonical-json-v1`; do not claim RFC8785 compatibility.

Finding equality compares contract version, immutable run context and canonical finding content. Store shared context once in the run row. Local ingestion time, receipt identity, findings-array position and reported submission outcome are excluded.

Consequences:

- Whitespace and object-key ordering do not change equality.
- Changed evidence, original timestamp spelling, uncertainty or asserted facts do.
- Later observations require new finding identities, even when wording or price is unchanged.
- Matching is exact byte equality, so digest collisions are irrelevant.

Identical replay changes no candidate, payload variant, observation or assessment. A distinct envelope may add an audit receipt containing replay dispositions; an identical canonical envelope adds nothing.

Changed content under an existing identity is quarantined. Retain every distinct variant, link the conflict to the original identity, and mark the original candidate disputed. Replaying either variant cannot clear the dispute.

Pre-group duplicate identities within a submission. Identical occurrences yield one admission and subsequent replays; different variants quarantine every occurrence, avoiding first-item precedence.

Detect explicit equal-time contradictions within complete research-offer groups using the accepted compatibility rules. Retain both claims and append disputed assessments. Different-time changes remain ordinary history. Import order, confidence and repetition never resolve disputes.

Existing observation-time selection handles older imports. An older observation can extend history or expose a historical contradiction, but cannot become current merely because its ingestion time is newer.

## 7. Store/core integration

Keep the workspace topology. Add research modules to `bookradar-store`; add no crate and no core dependency.

Proposed additive interfaces:

```text
validate_research(bytes) -> ValidationReport
ResearchStore::create(path)
ResearchStore::open(path, OpenMode)
ResearchStore::import(bytes, ImportContext) -> ImportReport
ResearchStore::inspect() -> ResearchSnapshot
ResearchStore::current(ResearchOfferKey, EditionId, now) -> CurrentView
```

`ResearchStore` exposes neither its connection nor an inner mutable `Store`, and provides no approval/promotion API.

Ledger format:

- SQLite application id `0x42525249`; `user_version=1`.
- Reuse the unchanged v1 observation/review SQL as candidate-storage tables.
- Add `research_inputs`, `research_runs`, and `research_findings`.
- Reuse existing connection configuration, checked encoding and history resolution through small private helpers.
- `Store::open` continues accepting only observation-store v1. `ResearchStore::open` accepts only the research format. Neither auto-detects and adopts the other.

Minimum research records:

| Table | Required content |
|---|---|
| `research_inputs` | Receipt id, raw BLOB, canonical/raw content key, injected ingestion time, envelope disposition, rule version and issues. |
| `research_runs` | Producer/run primary key, immutable canonical context, first receipt reference. |
| `research_findings` | Receipt/position primary key, recoverable replay identity, canonical finding, outcome/reason, original/conflicting references, external listing tuple and nullable candidate-observation reference. |

Use STRICT tables, foreign keys, append-only triggers and exact schema-object checks. Store malformed/unsupported input as bounded raw BLOBs. New format versions fail closed.

Complete offer tuples receive ledger-local numeric source/offer surrogates under the import transaction. These identify provisional research groups; they establish no catalog match. Allocate checked observation ids locally. Incomplete tuples or unknown access remain candidate records without projection.

Projected observations:

- Preserve asserted dimensions and timestamps.
- Use `SubjectIdentity::Unresolved`, or `Conflicting` for explicit conflict.
- Use `KnowledgeAssessment::Unreviewed`, or `Disputed` after detected conflict.
- Have no reviewer approval.
- Treat the application’s support as `AgentOnly` with unassessed coverage; preserve producer-reported manual/browser methods separately.
- Retain full research provenance through the receipt/finding reference.

Use one immediate transaction for receipt, run registration, dispositions, candidate observations and dispute reviews. Refactor existing insert helpers to participate in that transaction without changing the public v1 append behavior. Storage failure rolls everything back.

Reuse the existing history compatibility function through a crate-private seam; do not duplicate its policy. Local ingestion/assessment times must not regress; reject such an operation rather than inventing a replacement time.

No migration is required. Existing v1 files remain untouched. A shared v2 migration was rejected for this boundary because it introduces data-preservation and older-reader compatibility work. A custom append-only file was rejected because framing, locking and torn-write recovery would be new responsibilities. Validator-only storage was rejected because it cannot prove replay across processes.

Recovery relies on SQLite transaction rollback and replay after reopening. Do not claim power-loss or multi-process stress guarantees. No cross-database commit or application-store promotion occurs.

## 8. Test matrix and fixtures

Four committed files provide the runnable examples: `partial.json`, `conflict.json`, `newer.json`, and `older.json`. Other negative inputs are derived in memory.

`partial.json` contains valid F1 for OFFER-A, an identity-less object, and F3 with invalid availability. `conflict.json` changes F1’s availability under the same identity. Newer/older fixtures use different finding identities and known observation instants.

| Test name | Required result |
|---|---|
| `malformed_envelopes_are_quarantined_without_candidates` | Malformed JSON/UTF-8 and missing headers retain raw input; zero candidates; unknown count. |
| `unsupported_version_is_not_interpreted_as_v1` | Version 2 quarantined; no run/finding interpretation or observations. |
| `duplicate_keys_are_detected_before_object_materialization` | Nested and escaped-equivalent duplicates quarantine the envelope. |
| `unknown_fields_and_missing_required_fields_are_not_ignored` | Header failures quarantine envelope; finding failures quarantine only that position. |
| `input_limits_reject_without_storage` | Oversize rejected; ledger unchanged; depth/finding limits enforced. |
| `partial_run_accounts_for_every_position` | Exact `3 = 1 + 0 + 1 + 1` partition; one projection. |
| `identical_replay_is_noop_after_reopen` | Same canonical input changes no persisted rows or assessments. |
| `formatting_changes_do_not_change_replay_content` | Whitespace/object order remain identical replay. |
| `changed_payload_is_retained_and_disputes_original` | New variant quarantined; original bytes unchanged; dispute survives reopen. |
| `same_batch_identity_conflict_has_no_first_item_winner` | Both orders quarantine every conflicting occurrence. |
| `producer_and_run_scopes_do_not_merge_findings` | Equal finding ids in different scopes remain independent. |
| `run_context_changes_are_conflicts` | Changed context retained; affected prior candidates disputed. |
| `valid_agent_stock_claim_never_becomes_verified` | Available claim and claimed manual/browser provenance remain unreviewed, approval absent, `NotEligible`. |
| `provenance_and_explicit_unknowns_round_trip` | Source/listing/redirect/evidence references and all timestamp components preserved. |
| `money_retains_currency_and_basis_without_inference` | EUR/CZK and per-lot values retained; invalid combinations quarantined. |
| `contradictions_survive_order_and_majority_changes` | Both claims retained/disputed; later or repeated agreement does not clear them. |
| `older_import_preserves_newer_current_observation` | Newer observed instant remains selected in either import order. |
| `failed_access_never_infers_stock_exhaustion` | Blocked/gone cases preserve access meaning and suppress positive eligibility. |
| `embedded_instructions_are_opaque_data` | Command/file/URL text round-trips; no referenced path is opened or command executed. |
| `transaction_failure_rolls_back_receipt_and_candidates` | Injected failures leave no partial import after reopening. |
| `research_and_v1_formats_reject_each_other` | Wrong-format open fails; original v1 bytes remain unchanged. |
| `research_cli_transcript_and_exits_are_stable` | Exact §2 transcript, partial/replay/conflict exits, malformed input and empty-ledger output. |

Also cover pre-epoch fractions, unknown offsets, unrepresentable instants, regressing local ingestion time, busy/read-only stores, append-only enforcement and unsupported ledger versions.

Executable worked cases include replay/conflict, older import, equal-time contradiction, temporal stock changes, failed rechecks, page disappearance, missing language, opaque ISBN assertions, separate currencies, lot basis and embedded instructions.

Full bibliographic matching, translation/printing distinctions, cross-producer equivalence, screenshot visibility inspection and owner-scoped personal state remain deferred. Existing freshness boundary tests remain the policy evidence; do not reimplement the 24-hour rule.

All new fixtures are synthetic. Tests use injected times and owned temporary files, without network, wall clock, credentials or real data.

## 9. Toolchain, dependencies and gates

Retain Rust `1.99.1`, existing workspace membership and existing rusqlite configuration.

Proposed additions to `bookradar-store`:

```toml
serde = { version = "=1.0.228", default-features = false, features = ["std"] }
serde_json = { version = "=1.0.145", default-features = false, features = ["std"] }
```

Use a serde visitor for duplicate-safe parsing and explicit field decoding; no derive feature or proc-macro dependency is needed.

These are proposed exact pins, not verified cache or registry availability. They introduce Rust serialization/helper dependencies; the actual resolved graph and checksums must be inspected later. No additional native component is intended.

No hashing dependency is selected. `sha2` would provide a compact digest but add a graph without improving equality: bounded canonical bytes already provide exact comparison. No new database or timestamp crate is needed.

A later grant must explicitly authorize editing the manifest/lockfile, resolving these pins and fetching their graph from crates.io. Stop if a pin is unavailable, incompatible, or introduces unexpected native/runtime scope; do not substitute a version automatically.

Later gates:

```sh
export PATH="$HOME/.cargo/bin:$PATH"
cargo +1.99.1 fetch
cargo +1.99.1 build --workspace --all-targets --locked --offline
cargo +1.99.1 test --workspace --locked --offline
cargo +1.99.1 fmt --all --check
cargo +1.99.1 clippy --workspace --all-targets --locked --offline -- -D warnings
cargo +1.99.1 tree --locked --offline -p bookradar-core
git diff --check
./.ap/ap doctor
```

Run focused research tests during development, then the workspace suite once for the final candidate because shared storage/history helpers change. Preserve the existing 45-test baseline and unchanged old CLI transcript. The core dependency tree must still contain only core.

Use fresh ledgers and fresh v1 fixture databases for validation. Tests must reopen across processes and cover wrong-format rejection and rollback. No clean clone is needed for this evidence route.

## 10. README, ADR and lifecycle

Add `docs/research-input-v1.md` as the durable implementation-format reference for §§3–6, subordinate to the accepted domain contract. Include field shapes, explicit unknowns, limits, canonicalization, disposition accounting and CLI examples.

After implementation validation, replace the README status paragraph with:

> Status: the workspace contains a dependency-free `bookradar-core` verification kernel, local observation history, and a synthetic research-ingestion proof. The research boundary validates strict versioned JSON, retains quarantine and replay conflicts in a separate SQLite ledger, and creates only unreviewed or disputed candidates. Structural admission does not establish truth or verified stock. A user interface, live ingestion, deployment, and a running monitor remain unimplemented. License and contribution policies remain undecided.

Add a “Synthetic research ingestion proof” section containing the commands and exits from §2 and links to the wire document and ADR.

Add `docs/adr/0005-versioned-research-admission.md` with:

> Decision: use strict JSON contract version 1 and a separate SQLite research ledger. Compare canonical content bytes under producer/run/finding identity. Reuse the accepted observation/history implementation for explicitly unreviewed or disputed candidates, without reviewer approval or promotion to existing application databases.

Its alternatives are custom text, validator-only, custom append log and shared schema v2. Record the costs of a second file, strict compatibility, dependency provisioning and deferred reconciliation.

ADR status remains Proposed until the COOPERATOR’s decision is recorded; any acceptance date comes from that decision, without backdating.

Lifecycle metadata:

- Wire reference: consumer relationship; durable implementation contract; discovered through README/ADR; retain while v1 is supported.
- ADR: historical relationship; durable architecture rationale; domain contract remains product semantic owner.
- Fixtures/tests: executable synthetic evidence, retained while the boundary is supported.
- Consumers: implementers, research producers and reviewers.
- Retirement requires explicit replacement, updated links and separately authorized cleanup; cleanup owner is COOPERATOR under RF-14.

Do not change the accepted contract, ADRs 0001–0004, AP, or deferred collaboration policies.

## 11. Acceptance, risk and Cooperator decisions

This table consolidates the material decisions. Selected rows reflect answers in this exchange; proposed rows require reconciliation before a grant.

| Decision | Disposition/recommendation | Consequence |
|---|---|---|
| Representation | Selected: strict JSON | Duplicate-safe parser and strict field handling required. |
| Persistence | Selected: separate SQLite ledger | Existing v1 databases untouched; separate research file owned by `ResearchStore`. |
| Topology | Proposed: extend `bookradar-store` | Reuse transaction/history helpers; no new crate or workspace change. |
| Replay | Proposed: exact identity tuple plus canonical bytes | No hashing dependency; provenance changes conflict under reused identity. |
| Admission/handoff | Proposed: ledger-local candidates only | No catalog resolution, approval or application-store promotion. |
| Dependencies | Proposed: exact serde pins in §9 | Later grant must authorize resolution, fetch and lockfile change. |
| Runnable scope | Proposed: four commands and four fixtures | Demonstrates persistence, partial outcomes, replay and dispute without live integration. |
| Documentation | Proposed: wire reference and ADR 0005 | Records executable representation separately from product semantics. |
| Evidence | Proposed: E2 with fresh independent acceptance required | Shared storage compatibility, durable negative paths and trust separation checked independently. |
| Git/publication | Proposed: local reviewable candidate; commit only when granted | No push until independent acceptance and a separate publication grant. Meta archival remains COOPERATOR-owned. |

E2 is recommended for this reversible, synthetic local boundary: it adds no navigation, execution, privileges, existing-data migration or approval capability. Fresh independent acceptance is nevertheless required because parser, durable replay and assessment separation are central claims.

Escalate to E3 with separate preflight if implementation introduces existing-data migration, live input adapters, evidence fetching, approval/promotion, new native dependencies, broader recovery requirements or materially wider shared-storage changes.

Residual limits:

- Producer identities, provenance and normalized times are asserted, not authenticated or independently verified.
- Contradiction detection covers explicit comparable facts within exact producer-scoped listing groups.
- Evidence bytes, natural-language truth and cross-producer identity are not assessed.
- Quarantine and disputes persist; this slice supplies no resolution workflow.
- SQLite recovery evidence covers transactions, not production durability or multi-process stress.

Implementation PASS, independent acceptance PASS, publication PASS and closure remain separate. None is granted by this report.

## 12. Ordered implementation sketch and Git boundary

Proposed exact tracked-path allowlist:

```text
Cargo.lock
README.md
docs/research-input-v1.md
docs/adr/0005-versioned-research-admission.md
crates/bookradar-store/Cargo.toml
crates/bookradar-store/src/lib.rs
crates/bookradar-store/src/store.rs
crates/bookradar-store/src/history.rs
crates/bookradar-store/src/research.rs
crates/bookradar-store/src/research_contract.rs
crates/bookradar-store/src/schema_research_v1.sql
crates/bookradar-store/src/bin/bookradar-research.rs
crates/bookradar-store/tests/research_contract.rs
crates/bookradar-store/tests/research_ingestion.rs
crates/bookradar-store/tests/research_cli.rs
crates/bookradar-store/tests/fixtures/research/partial.json
crates/bookradar-store/tests/fixtures/research/conflict.json
crates/bookradar-store/tests/fixtures/research/newer.json
crates/bookradar-store/tests/fixtures/research/older.json
```

The root manifest, core, original schema SQL, old CLI, existing integration tests, contract, earlier ADRs and AP remain outside the mutation allowlist.

Ordered stages:

1. Reconcile this report and record decisions; issue a complete implementation renewal with native planning disabled, exact baseline, paths and dependency/artifact authority.
2. Re-gate repository/AP/environment. Authorize only ignored Cargo/demo artifacts and test-owned temporary paths in addition to tracked changes.
3. Provision the approved pins, inspect the actual graph/checksums, and preserve core’s dependency-free boundary.
4. Implement the strict contract, canonicalization and synthetic fixtures.
5. Add the separate ledger format, shared private transaction helpers, replay/quarantine and candidate projection.
6. Add CLI and documentation; run focused tests, then final workspace gates and the exact demonstration.
7. Return the complete diff and validation evidence. Create one candidate commit only if explicitly authorized; do not push.
8. Route sequential fresh independent acceptance against the exact candidate. Publication requires its own grant and public equality checks.

Rollback is confined to the new candidate code and explicitly owned synthetic artifacts. Preserve unrelated changes and any retained ledger. No reset, destructive cleanup, migration, downgrade or deletion of existing v1 data is part of this plan. Failed imports roll back transactionally; incompatible/corrupt files fail closed without repair.

Smallest next step: ORCHESTRATOR reconciliation of the consolidated decision table, followed—if accepted—by one complete same-session implementation grant. No additional planning cycle is proposed.

Orchestration critique:  
MEASURED: none  
LEAD: none

Resolved Execution Issues / Near-Misses: the initial AGENTS filename-discovery command searched the broader Projects/Meta roots before the pasted grant was fully parsed. It requested filenames only; no unrelated file contents were used. Subsequent inspection stayed within the named sources. This was a read-scope deviation; no write or corrective search followed. Truncated reading outputs were recovered through bounded rereads.

Pre-Existing Failure Classification: none. No tests ran, and no existing test failure is claimed.

Authority expiry: this terminal report ends the grant; no autonomous continuation.

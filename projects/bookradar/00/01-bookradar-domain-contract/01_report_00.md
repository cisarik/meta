# BookRadar domain contract and focused semantic ADRs

## 1. As-found state

All facts below concern `cisarik/bookradar` unless another repository is named.

| Verified fact | Establishing commands |
|---|---|
| Physical working directory equals the configured BookRadar checkout root and Git top level. | `pwd -P`; `git rev-parse --show-toplevel` |
| Canonical `origin` is `https://github.com/cisarik/bookradar`; active branch is clean `main`, tracking `origin/main`. | `git remote -v`; `git status --porcelain=v1 --branch` |
| HEAD is `12864ac874d74c562e22243bd622bd2729dfdaca`; subject is `docs: adopt analytic programming`; tree is `c3dda5007bf66f19f18d3016260018f72eead8ba`. | `git rev-parse HEAD`; `git rev-parse 'HEAD^{tree}'`; `git log -1 --format='%H%n%s%n%T'` |
| Local `main` and `origin/main` point to that commit. Additional `refs/codex/turn-diffs/*` tree refs were present; they are not additional branches or worktrees. | `git for-each-ref` |
| Exactly one BookRadar worktree exists. The committed root paths are `.ap`, `.gitmodules`, `AGENTS.md`, `README.md`. | `git worktree list`; `git ls-files`; `git ls-tree -r --name-only HEAD`; `ls -la` |
| No additional untracked or ignored files were found outside the submodule and Git metadata. | `git ls-files --others --exclude-standard`; `git ls-files --others --ignored --exclude-standard` |
| The sole submodule is `.ap`; its gitlink equals its local HEAD at `d7023cf037f6d17885c3ede5c04812c61640da50`. | `git submodule status`; `git ls-tree HEAD .ap`; `git -C .ap rev-parse HEAD` |
| `.ap` is clean and detached; its canonical origin is `https://github.com/cisarik/ap.git`; the pinned commit object exists locally. | `git -C .ap status --porcelain=v1 --branch`; `git -C .ap symbolic-ref -q HEAD`; `git -C .ap remote -v`; `git -C .ap cat-file -t d7023cf037f6d17885c3ede5c04812c61640da50` |
| Public BookRadar `refs/heads/main` equals the verified local baseline. | The exact `git ls-remote` recorded above |
| Final tracked diffs remain empty in BookRadar and `.ap`; final branch/status checks remain clean. | `git diff --exit-code`; `git diff --cached --exit-code`, also under `git -C .ap`; final status and identity reads |

The provided Meta checkout has canonical origin `https://github.com/cisarik/meta` and is dirty. Its domain-contract handout and predecessor closure exist and were read as historical context. Their claims about bootstrap agree with the independently verified BookRadar baseline. Their future routes are not current authority.

`README.md` explicitly reports no application. The committed tree contains no domain specification, ADR, schema, code, or runtime behavior from which an existing model could be inferred. Consequently, the following semantics are **reasoned recommendations**, not discoveries of implemented behavior.

Mandatory reading was completed at the pinned identity. Governing references include:

- `.ap/AP.md`: “Semantic Authority and Artifact Relationships”, the Worker minimum-reading spine and required RF capsules, “Planning Budget and Expiry”, “Orchestration Planning and Implementation Planning”, “Plan-to-Execution Gate”, “4. Source of Truth and Evidence”, “5. Task Authority”, “8. Worker Responsibilities”, “12. Validation and Public Verification”, “13. Artifact Lifecycle and Repository Hygiene”, “17. Compact Communication”, and “18. Stopping Conditions”.
- `.ap/AP_WORKER.md`: complete operational spine, including “Worker Session Target” and “Reporting”.
- `.ap/PROMPT_CONTRACTS.md`: the required report, planning, authority, exchange identity, session/mode, execution-gate, and delivery contracts.
- `.ap/ARTIFACT_LIFECYCLE.md`: “Two Classification Axes”, “Required Metadata”, “Discovery Records”, and “Worker and Orchestrator Checks”.
- Project `AGENTS.md` and `README.md`.

No mandatory inspection remains unavailable. Broader external facts remain unverified as stated in the report.

## 2. Recommended documentation slice

Create three English documents and minimally edit README. Keep the glossary, diagram, examples, and review checklist inside the domain contract.

| Proposed path | Purpose and minimum contents | Relationship, ownership, discovery, lifecycle |
|---|---|---|
| `docs/domain-contract.md` | Status/version; glossary and relationships; identity rules; observations, prices and evidence; ingestion boundary; personal state; display semantics; worked cases; evolution checklist; explicit deferrals. | **AP relationship:** consumer, project-owned product specification. **Lifecycle:** normative durable product artifact after approval; explicitly proposed beforehand. **Product semantic owner:** this document. **Decision owner:** COOPERATOR; editorial maintenance: BookRadar maintainers under authorized tasks. **Consumers:** future implementers and reviewers. Discover through README and both ADRs. Retain while applicable; retirement requires an explicit successor, updated links, and authorized cleanup. |
| `docs/adr/0001-book-edition-and-offer-identity.md` | Identity decision, alternatives, consequences, unresolved matching, identifier limitations, deferrals, links to contract sections. | **Relationship:** historical. **Lifecycle:** durable historical artifact. Records rationale; the contract owns current product meaning. Consumers: implementers/reviewers, discovered from the contract. Preserve with explicit supersession if replaced. Cleanup owner: COOPERATOR through authorized maintenance. |
| `docs/adr/0002-evidence-and-research-trust-boundary.md` | Observation/evidence admission decision, trust distinctions, alternatives, consequences, availability implications, explicit policy deferrals. | Same historical ownership and lifecycle as ADR 0001. Discover through the contract; link back to its normative rules rather than duplicating them. |
| `README.md` | Add a domain-documentation link and an accurate status sentence. Continue to state that no application exists. | **Relationship:** explanatory; **lifecycle:** durable explanatory artifact. BookRadar maintainers own navigation. Retain as the entry point; update links when documents are superseded. |

Each new document carries concise status, owner, relationship, lifecycle, consumer/discovery, and supersession metadata. Reference `.ap/AP.md` under “RF-14 — Artifact Ownership and Lifecycle”; do not copy AP rules or imply that product documentation grants task authority.

No separate docs index, fixture directory, research archive, roadmap, or ADR template is needed.

## 3. Domain model and identity rules

The following is proposed conceptual vocabulary, not a schema or required Rust type inventory:

```text
Author ↔ Work ↔ Edition/printing
                  ↑
              Copy or lot ← Offer ← Observation → Evidence → Source
                              ↑           ↑
                       merchant/seller  ResearchRun provenance

Owner scope → Watch → Work or Edition
Owner scope → LibraryEntry → Edition, with optional individual-copy detail
```

Links represent meaning, not database cardinalities. An offer may identify only an edition or an unresolved subject when a particular copy is not distinguishable. Such uncertainty must remain visible.

**Identity rules:**

- **Work:** an intellectual creation. Title text, transliteration, or author name alone is insufficient identity. Preserve original titles and aliases. Anthologies and collected volumes may relate to several works; anonymous or uncertain authorship remains possible.
- **Edition/printing:** a published physical realization with evidenced language and publication characteristics. Known differences in translation, language, edition statement, printing, publisher issuance, binding, or volume composition can establish distinct realizations. A conflicting year assertion alone does not establish a new printing.
- **Copy/lot:** a particular physical unit or explicitly grouped set when identifiable. Condition belongs to the offered or owned unit, not the intellectual work. Two similar listings are not evidence of the same physical copy.
- **Offer:** a seller’s listing of a subject under commercial terms. Identity is source-scoped and uses a native listing identifier where available. A URL is a locator, not universal identity. Seller, variant, and reused-listing generations must be distinguished where material.
- **Internal references:** stable and independent of title, ISBN, URL, or mutable descriptive facts. No identifier format or storage mechanism is selected.
- **Author filtering:** use attributable author identities and recorded aliases; do not silently merge people sharing a name.

**ISBN treatment:**

- ISBN is optional, repeatable, attributed evidence. Preserve the asserted spelling and its interpretation.
- Hyphen/spacing normalization and checksum validation produce matching candidates, not proof of edition identity.
- A valid corresponding ISBN-10/ISBN-13 pair may describe one edition; equivalent identifiers do not override contradictory language or publication evidence.
- Invalid or incorrect ISBN assertions remain diagnostic evidence and cannot justify an automatic merge.
- Multiple identifiers require scope: edition, format, volume, or set. Do not assume every identifier on a page identifies the offered unit.
- Reused ISBNs and reissues may require distinct edition records. Missing ISBN does not prevent a provisional identity.

**Same versus distinct:** merge only when supporting evidence establishes compatible identity and material conflicts are resolved. Otherwise retain distinct candidates and a possible-match relationship. Any later merge or split must preserve references, provenance, and the correction rationale.

**Language:** distinguish asserted Slovak, Czech, mixed, unknown, and conflicting evidence. A Slovak website, translated interface, similar title, or agent conclusion does not establish a Slovak edition. A Czech edition cannot satisfy a Slovak edition target.

**Alternative considered:** one title/ISBN record combining publication, stock, and ownership. It is simpler initially but cannot represent absent ISBNs, reused identifiers, multiple used copies, or language conflicts honestly. Conservative separation is recommended because false merges are costly to reverse.

## 4. Offer, observation, price, and evidence semantics

**Stable offer versus observation:** retain listing identity separately from immutable, time-bound observations. A price change normally creates another observation of the same offer. A different seller, substituted copy, or reused listing may represent a new offer; uncertain continuity must be recorded.

Use separate proposed dimensions:

| Dimension | Vocabulary and meaning |
|---|---|
| Source-reported availability | `available`, `reserved`, `unavailable`, `unknown` |
| Access result | readable, blocked/rate-limited, transport/error, page gone |
| Listing disposition | present, removed, uncertain |
| Knowledge assessment | unreviewed, supported, disputed, rejected |
| Temporal assessment | within an approved freshness interval, stale, unknown |

These dimensions prevent a single status from conflating access, stock, confidence, and time.

**Transitions and lifecycle:**

- An explicit, attributable source statement may support availability or unavailability **at observation time**.
- HTTP success or a product description alone supports page existence.
- A reservation is distinct from a freely buyable copy and from sold-out stock.
- HTTP 429, CAPTCHA, timeout, or authentication obstruction records failed access. It never creates an unavailable observation.
- A 404, disappearance, or generic redirect supports “listing unavailable/removed”, without proving sale or stock exhaustion.
- Rechecks append observations. Later successful evidence can resolve earlier availability or access uncertainty.
- No stock state is inherently terminal. Source-confirmed permanent closure may retire a listing, while its observation history remains.
- Late imports do not supersede newer observations merely because they arrived later. Distinguish ordinary time-based changes from unresolved contradictory claims.

Freshness is computed from observation time and an explicitly approved rule. An access failure or unresolved conflict prevents a positive current-verification label even if older evidence was previously eligible. Without a selected rule, only historical labels are eligible; the decision is consolidated in §11.

**Price and second-hand terms:**

- Represent an exact monetary amount with currency, source, observation time, and basis: per copy, per lot, range, or uncertain.
- Separate asking price, shipping, fees, and any explicitly known total. Unknown shipping is not zero.
- Preserve tax/inclusion uncertainty and conditions such as destination-dependent delivery.
- Keep currencies separate. No implicit conversion or cross-currency price trend is permitted.
- Record observed condition, quantity, reservation, and relevant seller identity with provenance. Preserve source wording when condition grades cannot be compared.
- A historical price remains dated history. Condition or lot changes can break price comparability even when the listing continues.

**Evidence and provenance:**

- Retain source identity; requested URL and resolved URL where known; material redirects; observed time; access/capture time; and later ingestion time when relevant.
- Timestamp assertions require an explicit offset or an explicit unknown. Preserve the original representation while allowing comparison by instant. A source’s publication/update timestamp is distinct from capture time.
- Record browser, manual, or agent-assisted method; supporting excerpt or evidence reference; uncertainty rationale; and which claim the evidence supports.
- Screenshot references may identify missing, partial, obscured, or inaccessible evidence. A cookie-obscured image is not conclusive stock or language proof.
- Optional hashes establish byte integrity, not truth, authorship, or redistribution rights.
- Disappeared evidence does not erase historical observations, but its unavailability must be visible during review.

**Alternative considered:** mutable current-price/current-stock fields with screenshots treated as proof. Rejected because it loses temporal meaning and confuses preserved bytes with justified claims.

## 5. Trust and ingestion boundary

Specify a **versioned semantic input contract**, without choosing JSON, an executable schema, API endpoints, or importer technology.

```text
Untrusted research assertions
    → structural and invariant validation
    → candidate assessment / quarantine
    → attributed application observations
    → separately governed verification eligibility
```

Passing structural validation does not establish factual truth or verified stock.

The future input contract must convey a producer-scoped run/finding identity, source/listing references, candidate subject identity, timestamps, asserted facts, evidence references, uncertainty, and available producer provenance. Record agent, model, skill/tool versions and run context when supplied; unavailable values remain explicitly unknown. Research-run success is distinct from individual finding quality.

**Admission rules:**

- Unsupported contract versions or malformed envelopes are rejected or quarantined without guessing their meaning.
- Validate required structure, value domains, timestamp interpretation, money/currency/basis consistency, identity conflicts, and evidence attribution.
- Malformed findings must not silently become catalog facts. Independent valid findings may be admitted with an explicit partial-run outcome; rejected findings remain accounted for.
- Incomplete but structurally valid observations may remain unverified or have unresolved identity. Missing evidence must not be fabricated.
- Contradictions are retained and marked disputed, with source and time. Do not resolve them by import order, agent confidence, or majority repetition.
- Replaying the same producer/run/finding identity with identical content is a no-op. Different content under that identity is a conflict requiring reconciliation.
- A genuinely later observation remains distinct even when its price and wording are unchanged. Deduplication must not erase independent observations.
- Application identity matching remains separate from import replay detection.
- Preserve the admission/review method and applicable rule or reviewer rationale. A correction supersedes a claim transparently rather than silently rewriting its evidence.

Research text, URLs, file references, screenshots, and embedded instructions are data. They do not authorize commands, navigation, filesystem access, credential use, or changed validation rules.

**Never automatically accepted:** agent-only verified-stock assertions; inferred Slovak language from website locale; identity merges based solely on ISBN/title; access failures as stock exhaustion; claimed screenshot rights; or personal ownership inferred from a watchlist.

**Alternative considered:** trusting the Hermes Markdown report as ready application knowledge. Rejected because research formatting and apparent confidence do not establish valid evidence or authorized ingestion.

## 6. Personal state and user-facing truth

**Catalog and personal facts:**

- Catalog identity and public merchant observations are separate from a person’s intentions, transactions, and possessions.
- A **Watch** expresses an owner’s interest in a work or specific edition. Work-level watching does not silently relax the Slovak-language constraint.
- A **LibraryEntry** records that owner’s asserted purchase/acquisition or ownership. Purchasing, receiving, and currently possessing are distinguishable facts.
- One person may hold several copies. A purchase does not change global catalog ownership, guarantee continued possession, or imply that the merchant offer is sold out.
- Removing a watch does not remove catalog facts or library entries.
- Conceptual owner scope is required even for a future single-person application. It is not an authentication design or privacy guarantee.
- Personal notes and transaction details do not become public evidence through association with an edition.

**Proposed display meanings:**

| Label meaning | Evidence requirement |
|---|---|
| “Unverified” | Insufficient or unreviewed support; no positive availability implication. |
| “Last observed available — [time]” | Attributed source availability statement at that time; freshness or verification requirements are not satisfied. |
| “Checked available — [time]” | Only under the approved verification method and freshness rule; no unresolved identity/conflict/access issue. Still a dated source observation. |
| “Last observed reserved/unavailable — [time]” | Explicit supported source state. “Sold out” requires a corresponding source assertion. |
| “Could not recheck — [time]” / “Listing removed” | Access or listing evidence, shown separately from historical stock. |

Do not use an unqualified green “available” label for historical data. Text, time, and uncertainty must carry the meaning without relying on color. Preserve semantic distinctions through translation; Slovak wording and detailed interface design remain future work.

**Alternative considered:** global watched/owned flags and one availability badge. Rejected because they conflate people, possessions, and historical merchant claims.

## 7. ADR set

Exactly two ADRs are recommended.

| ADR | Proposed decision and alternatives | Consequences, deferments, owner |
|---|---|---|
| **0001 — Book, edition, copy, and offer identity** | Distinguish intellectual, published, physical-unit, and commercial identity; use stable internal references and attributed optional identifiers; preserve unresolved matches. Alternatives: ISBN-primary identity; title-level flattening; detailed bibliographic ontology. | Reduces false merges and copy/offer confusion; requires explicit uncertainty and correction handling. Defers identifier formats, automatic matching algorithms, full bibliographic standards, storage, and Rust types. **Status: Proposed. Decision owner: COOPERATOR.** |
| **0002 — Evidence-backed observations and untrusted research admission** | Separate observations from offers, preserve provenance, and distinguish structural admission from evidence assessment and verification eligibility. Alternatives: trust agent reports; overwrite a current-state record; accept only manually authored records. | Enables honest history and partial research results; adds review and conflict concepts. Defers executable ingestion format, validators, integrations, and the decisions consolidated in §11. **Status: Proposed. Decision owner: COOPERATOR.** |

The contract owns current semantic rules; ADRs explain why they were chosen. Populate acceptance status and dates only from an actual approval recorded in the later grant.

A third ADR is not justified now: owner separation fits the contract, while privacy and screenshot policies remain undecided. No runtime architecture ADR is warranted.

## 8. Worked cases and edge-case matrix

Embed synthetic examples in the contract. Names, listing identifiers, events, and amounts must be explicitly fictional.

| Case | Expected interpretation |
|---|---|
| Same work offered in Slovak and Czech | Distinct editions; Czech does not satisfy a Slovak edition watch. |
| Merchant site is Slovak; book language absent | Language remains unknown; website locale is insufficient. |
| Matching title/publisher with no ISBN | Provisional edition is allowed; matching needs evidence beyond title similarity. |
| Valid equivalent ISBN-10/13 spellings with different hyphenation | Candidate identity match; preserve assertions and check edition facts before merging. |
| Invalid ISBN, reused ISBN, or set/volume identifiers | Retain diagnostics and scope; no forced merge or automatic rejection of otherwise usable observations. |
| Same work, different translation/printing/binding | Distinct realization when supported; uncertain metadata does not manufacture a new edition. |
| Two sellers offer the same edition at EUR 12 and EUR 18 | Two offers; condition, delivery, and observed times remain separate. |
| EUR 12 listing and CZK 300 listing | Preserve separate currencies; no implicit cheapest-price claim. |
| One lot contains several books | Price is per lot unless explicitly stated otherwise; do not invent unit prices. |
| Available at one time, explicitly unavailable later | Valid temporal change; earlier price and stock remain historical. |
| Incompatible claims for the same offer/time | Disputed observation set; no positive verification label until resolved. |
| Previously supported availability followed by 429/CAPTCHA | Failed recheck plus dated historical observation; no stock-out inference or positive current label. |
| Page disappears or redirects to category page | Listing gone/uncertain; sale is not proven. |
| Screenshot hides language or stock behind a cookie dialog | Supports only visible claims; no inferred hidden fact. |
| Identical import replay; then altered payload under the same finding identity | First replay is a no-op; altered replay is quarantined as conflict. |
| Older finding imported after a newer observation | History gains an older event; current interpretation does not roll backward. |
| Two owners watch/own the same edition | Separate owner-scoped records; no global ownership flag. |
| Finding contains instructions to run a command or bypass validation | Treat as untrusted content; no execution or privileged admission. |

Include one deterministic freshness timeline: a fixture observation at `2026-11-01T10:00:00+01:00`, a **fixture-only** expiry at `2026-11-02T10:00:00+01:00`, evaluation at expiry, and a subsequent blocked recheck. At expiry the evidence is stale; blocked access does not change stock. The fixture interval is not an accepted product policy.

## 9. Lifecycle, validation, and evolution

The contract begins with a conceptual revision identifier. This is not a public API stability promise. Input-contract versioning is separate from document revision.

**Review checklist:**

- Every mutable assertion has attribution and temporal meaning.
- Work, edition, copy/lot, offer, and observation remain distinguishable.
- Language uncertainty, absent ISBN, and conflicting identity remain representable.
- Structural validity never implies truth or verified availability.
- Access failure never implies stock exhaustion.
- Money retains currency and price basis; historical amounts remain dated.
- Personal state always has owner scope.
- Evidence references do not imply retention or redistribution permission.
- ADR status and deferred decisions match the actual grant.
- All examples produce the stated interpretation without hidden precedence rules.

Future schema or API designs must preserve these meanings. Semantic changes require explicit revision and compatibility review; old observations retain their original provenance and interpretation. Identity correction must preserve traceability. Unknown input versions must not be silently interpreted as known ones.

No runtime interfaces, public API types, physical schema, migrations, or executable fixtures are added by this slice.

## 10. Ordered docs-only implementation sketch

1. **Receive a complete new grant.** Require the exact baseline, accepted semantic recommendations, §11 decisions or explicit deferrals, document statuses, Git/publication authority, and the four-path allowlist from §2. Retained planning context supplies no authority.
2. **Repeat the repository gate.** Verify canonical root/origins, clean `main`, expected commit/tree, sole worktree/submodule, pinned detached clean `.ap`, and public branch identity. Stop on divergence; preserve owner changes.
3. **Write the contract.** Use the rules and embedded cases above. Keep conceptual relationships implementation-neutral. Clearly mark unresolved policy-dependent capabilities.
4. **Write both ADRs and update README.** Link to contract rules; record only approved decisions. Keep the no-application status accurate.
5. **Perform E1 validation.** Review the exact docs-only diff and allowlist; run `git diff --check`; inspect Markdown headings, relative paths, fragments, and bidirectional links; walk through every worked case and invariant. No runtime test suite or dependency installation is justified.
6. **Commit and publish only if expressly granted.** Review exact staged paths and content, make the authorized documentation commit, perform the authorized normal push, and verify public `main` against that commit. Bind the published SHA to its tree and document contents through Git inspection. Return validation and publication evidence for ORCHESTRATOR reconciliation.
7. **Stop at the implementation report.** Acceptance and closure remain separate.

The E1 envelope is sufficient for a coherent docs-only candidate. Escalate if review reveals unresolved conflicting authority, unsupported ADR acceptance, a changed approved semantic/security boundary, actual personal/media data, executable validators, schema/runtime changes, or publication identity mismatch. Independent acceptance is not required by default; the ORCHESTRATOR determines escalation for the specific anomaly.

Rollback is a separately authorized revert of the documentation commit, preserving subsequent owner work and valid navigation. No reset or history rewrite.

The allowlist excludes `.ap`, `AGENTS.md`, Meta, Rust/Cargo, schemas, UI, APIs, scraping, Hermes, MCP, NUC operations, CI, and deployment.

## 11. Risks, stop rules, and COOPERATOR decisions

False identity merges, overstated availability, and accidental personal/media disclosure are the principal product risks. Conservative unresolved states reduce them but require later reviewer effort. The COOPERATOR owns material residual-risk decisions; the ORCHESTRATOR owns reconciliation and grants; a later Worker owns conformity and evidence for its bounded change.

Present the following **once as one consolidated decision point**:

| Decision | Recommendation and credible alternatives | Consequence |
|---|---|---|
| **Meaning and freshness of “verified”** | Recommend reviewer-approved direct browser/manual evidence identifying the relevant subject and explicit source availability, with a **proposed maximum age of 24 hours**, timestamped wording, and immediate suppression after conflict or failed recheck. Alternatives: a separately approved deterministic source-validation rule with an explicit interval; or historical labels only. The interval and acceptable reviewer/evidence method require explicit approval. | Until approved, the positive verification label is ineligible. Neither structural validation nor an LLM claim qualifies. |
| **Personal-data and future privacy boundary** | Recommend approving conceptual owner separation while explicitly deferring actual collection, sharing, retention, and account/privacy design. Alternative: select a later bounded single-owner private-runtime or multi-user design task. | Documentation may define ownership semantics; it cannot authorize personal-data processing or promise privacy. |
| **Screenshot retention, rights, and public sharing** | Recommend metadata/reference semantics only for this slice, with storage duration, capture rights, and redistribution explicitly deferred. Alternative: separately approve bounded retention and sharing conditions in a later task. | No screenshot files or implied public-sharing permission enter this documentation change. |
| **Meaning of cross-domain monitoring** | Recommend multiple bookseller websites within physical Slovak-language book research. Keep monitoring unrelated product categories outside this contract. Alternative: explicitly select broader commerce monitoring as a separate objective. | Avoids an unapproved universal-product abstraction and clarifies that multiple seller domains do not broaden the product category. |

Until reconciled, these are proposed options, not accepted policies. Explicit deferral is a valid disposition where the contract defines the resulting capability boundary.

Stop later implementation if a required disposition is missing, repository gates fail, evidence conflicts cannot be represented honestly, document acceptance would be invented, or completion requires an excluded policy or runtime decision. Do not repair the AP pin, introduce actual research/personal data, or broaden the slice.

After reconciliation, the later documentation author has no discretionary modeling choice left: apply the approved proposal and recorded dispositions, preserve explicit deferrals, validate the four-path change, report, and stop.

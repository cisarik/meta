# Planner Artifact — AP Universal Continuation Bootstrap and Durable Observation Ledger

Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 01
Worker exchange ordinal: 01

```yaml
logical_whole:
  identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
  phase: Discovery (implementation-planning, plan-only)
  planning_cycle: initial
baseline:
  ap_public_main: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514   # ls-remote verified; tree a66b81d..., parent 4e7bfa5..., subject matches; local checkout clean at baseline
  framenest_public_main: 230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb  # ls-remote verified; .ap gitlink 041de310... confirmed commit-bound; local checkout dirty/behind, used git show only
  meta_public_main: 01de27e1e822b6e05b287da5064e87ce97c2d8d0  # ls-remote verified; clean; single archival-only descendant of expected dcc4517..., only changed path is this whole's 00_handout.md
problem:
  proven_gap_1: AP defines restoration semantics but has no discoverable, executable, consumer-portable cold-start continuation path from a minimal seed to one bounded next logical whole; continuation in practice depends on a 611-line handcrafted outgoing handout and private memory
  proven_gap_2: RF-09 ledger lifecycle and PROMPT_CONTRACTS entry fields exist, but no durable consumer storage/discovery representation for active `upgrade <canonical-repository>` observations exists anywhere in AP or FrameNest
  proven_gap_3: handcrafted continuation artifacts drift from canonical structural spellings (handout's `planning-PASS`, `no-new-material`, `invariant-failure`; sidecar report's `public-ref-mutation` justification are all non-canonical) with no indirection or control catching it
  rejected_framing: "AP has no restoration rules" is disproven; the gap is projection/storage/discovery, not semantics of restoration
selected_disposition: B — extend existing AP projections (AP.md, PROMPT_CONTRACTS.md, AP_ORCHESTRATOR.md, ARTIFACT_LIFECYCLE.md, INTEGRATION.md, explanatory projections, ADR-0016); no new continuation file, no managed-block change, no ap/CLI/schema change; add optional canonical project-root ledger storage contract
semantic_owners:
  continuation_two_stage_algorithm: AP.md §14 (new short subsection); operationalized in AP_ORCHESTRATOR.md
  ledger_lifecycle: AP.md §13 / RF-09 (extended with storage/discovery semantics)
  ledger_storage_grammar: PROMPT_CONTRACTS.md (extends Upgrade Observation Ledger Contract)
  ledger_file_lifecycle_class: ARTIFACT_LIFECYCLE.md
  ledger_file_discovery: consumer project rules (root AGENTS.md outside managed block); documented in INTEGRATION.md
  routing_capsule: remains Orchestrator/project presentation (Communication Routing fields); not AP protocol
implementation_boundary: AP repository only; 11 documentation paths; zero executable/schema/managed-block/consumer changes
likely_changed_paths:
  - AP.md (semantic owner; two small additions)
  - PROMPT_CONTRACTS.md (structural; ledger storage grammar + added entry fields)
  - AP_ORCHESTRATOR.md (operational; new cold-start section)
  - ARTIFACT_LIFECYCLE.md (operational; ledger file lifecycle)
  - INTEGRATION.md (operational; optional ledger discovery note)
  - README.md, FAQ.md, GLOSSARY.md (explanatory links/terms)
  - CHANGELOG.md (historical delivery record)
  - docs/adr/0016-*.md (new historical ADR), docs/adr/README.md (index)
compatibility:
  managed_block: byte-identical — existing consumers pass doctor with no migration
  ap_executable: unchanged; schema v1 unchanged; extension.*.* not used
  consumer_pins: unaffected until a separate explicit update task
  ledger_absent: degrades safely to current behavior
risks:
  - ledger file degenerating into backlog/NEXT file — controlled by RF-09 scoping + closure reconciliation
  - structural drift of ledger spellings — optional `ap doctor` ledger-shape check parked as later whole
  - duplication between §13 semantics and contract grammar — owner split preserved per ADR-0013
validation: documentation-first proportional validation per ADR-0015; fresh independent acceptance required (sole normative protocol + structural schema change)
acceptance_route: implementation (fresh Worker, E2, High) → fresh independent acceptance Worker → publication Worker → ORCHESTRATOR closure; then separate later FrameNest adoption whole
explicit_exclusions:
  - no CONTINUATION.md or any new AP file beyond ADR-0016
  - no managed-block, ap CLI, schema-v1, or ap.project.conf change
  - no FrameNest mutation in this whole; no Meta mutation; no conformance suite
  - no emoji/model/provider semantics; no trace-as-authority; no permanent BOOT/NEXT/session-state artifact
smallest_next_step: ORCHESTRATOR + COOPERATOR review this plan; on approval issue one bounded fresh-Worker implementation prompt for slice 1
```

---

## 1. Problem statement proven from current source

**Proven.** Three narrow, source-verified gaps, each distinct from the disproven broad framing "AP has no restoration rules":

1. **Cold-start continuation is semantically defined but not operationally discoverable.** The restoration precedence order (AP.md:294–302), rotation/restoration rules (AP.md:2053–2151), source-of-truth ranking (AP.md:823–852), and Restoration phase (AP.md:946–947) exist, but no AP projection tells a *fresh incoming* Orchestrator the executable cold-start sequence: begin read-only → verify pin/baselines → restore in precedence order → reconcile the active ledger → select exactly one bounded logical whole with the COOPERATOR → only then grant mutation authority. `AP_ORCHESTRATOR.md`'s "Rotation and Restoration" section (lines 325–334) is written for the *outgoing* Orchestrator producing a restoration prompt. The managed `AGENTS.md` block (exact text verified in `ap` lines 248–268) points to required reading but names no continuation path. Field proof of the resulting cost: the current handout for this whole is 611 lines / 22,410 bytes of manually synthesized state that a discoverable contract would make largely unnecessary.
2. **The upgrade-observation ledger has lifecycle and entry fields but no storage representation.** RF-09 (AP.md:1992–2051) owns states/transitions; PROMPT_CONTRACTS.md:1404–1440 owns the entry record; ARTIFACT_LIFECYCLE.md:118–125 mentions handling. Nothing defines *where an active ledger durably lives* in a consumer, how it is discovered, or its grammar as a committed artifact. Closure requires `Upgrade-ledger reconciliation: complete` (PROMPT_CONTRACTS.md:186), yet reconciliation output currently has no committed home — it evaporates into chat or the outgoing handout. FrameNest at `230ce43a…` contains no ledger, continuation, or Discovery Record path (commit-bound `git ls-tree -r` name search; only unrelated `tests/gallery_details_playback_handoff.test.js` matched). The prior planning report (Meta `projects/ap/01/01-…/01_report_00.md`) shows the ledger living conversationally ("the parked ledger observation").
3. **Handcrafted continuation artifacts drift structurally with no control.** The current handout proposed terminal values `planning-PASS`, `planning-PARTIAL`, `planning-BLOCKED`, `no-new-material`, `invariant-failure`; PROMPT_CONTRACTS.md:168–193 defines the canonical phase-result set (planning → `not-applicable`) and the six canonical report justifications. Independently, the sidecar publication report (Meta `…/06_report_00.md`) used `Report justification: public-ref-mutation`, also non-canonical. Two independent drift instances are direct evidence that long handcrafted restoration artifacts need structural indirection (route spellings to PROMPT_CONTRACTS.md) more than they need new semantics.

**What materially changes since the closed `project-local-fresh-orchestrator-prompt-archive` whole:** that whole asked whether finalized restoration *prompts* need a project-local archive and correctly selected superseded/no-implementation (RF-19 + Meta sufficed; F1/F2/F3 failure models found no concrete failure). This whole asks a different question the archive whole explicitly did not address: whether AP defines (a) a discoverable universal cold-start *algorithm* and (b) a durable *observation-ledger storage* projection. New direct evidence since then: the 611-line handout synthesis cost and two structural-drift incidents. The archive decision is not reopened; a prompt archive remains rejected.

## 2. Contradiction and duplication map

| Concern | Semantic owner (current) | Projections | Duplication/contradiction finding |
|---|---|---|---|
| Restoration precedence + trace subordination | AP.md RF-19 (294–302) | PROMPT_CONTRACTS §restoration contract; AP_ORCHESTRATOR 325–334; ARTIFACT_LIFECYCLE trace section; FAQ:132 | No contradiction; content is rotation-centric, no incoming-cold-start operational path — gap, not duplication |
| Rotation / restoration prompt content | AP.md §14 (2053–2151) | AP_ORCHESTRATOR; PROMPT_CONTRACTS:1870–1899 | Consistent; no duplicate owner |
| Ledger lifecycle | AP.md §13 / RF-09 (1992–2051) | PROMPT_CONTRACTS:1404–1440 (entry record); ARTIFACT_LIFECYCLE:118–125 | Consistent but storage/discovery undefined — the gap; zero competing definitions (safe to extend) |
| Handoff exceptionality; no BOOT/NEXT | AP.md:2146–2151 | ARTIFACT_LIFECYCLE:141–143; INTEGRATION.md migration guide; FrameNest AGENTS.md | Consistent. A ledger file must be defined to not collide with this family (it is retained observation evidence, not session state) |
| Integration/discovery surface | AP.md RF-15; INTEGRATION.md | `ap` managed block (ap:248–268); doctor exact-match | Managed block is the consumer discovery surface; changing its text forces consumer re-`init` migration — avoided by selected disposition |
| Project execution contract | AP.md RF-16; ADR-0012 | `ap`, ap.project.conf | `extension.*.*` keys are *ignored and cannot affect execution* (ADR-0012:20,47) — an intentionally unvalidated escape hatch, unusable as an AP-standard discovery declaration; rejected for ledger discovery |
| Meta trace layout | trace owns storage/layout (AP.md:268–270) | Meta `projects/…` tree | Meta uses zero-based exchange suffixes (`01_planning_00.md`); AP standard grammar is unsuffixed-for-01/`_02`-onward (PROMPT_CONTRACTS.md:484–511). This is Meta-local layout under its pin, **not** an AP defect and not AP semantics (CONT-009 boundary verified) |

No unresolved instruction conflict was found. Handout invalid values are treated as data/drift evidence, not authority; this plan uses canonical spellings.

## 3. Current lifecycle map (pause → Worker handoff), as-is vs selected

As-is: outgoing Orchestrator synthesizes long handout (chat) → optionally archived to Meta → fresh Orchestrator reads handout + verifies baselines → reconstructs active observations from handout/private memory → selects next whole → issues Worker prompt. **Dependency:** outgoing Orchestrator availability, Meta presence, private memory, handcraft fidelity.

Selected (target): COOPERATOR issues a minimal seed (§15 below) → fresh Orchestrator reads root `AGENTS.md` (managed block → required reading) → reads AP_ORCHESTRATOR.md cold-start section → verifies repository/public state read-only → restores per RF-19 precedence → reconciles the project-root ledger file if present (absent = no active observations) → presents restored state + one recommended bounded whole → COOPERATOR decides → complete Worker prompt issued with structural spellings taken from PROMPT_CONTRACTS.md. Handout becomes a *summary of verified state*, not the carrier of active observations or structural spellings.

## 4. Semantic-ownership table (every proposed element)

| Element | AP relationship | Lifecycle class | Semantic owner | Projection | Consumer & discovery | Retention/cleanup trigger | Cleanup owner |
|---|---|---|---|---|---|---|---|
| Two-stage continuation rule (restore→select-one-whole) | normative semantics | canonical | AP.md §14 (new subsection) | AP_ORCHESTRATOR.md cold-start section | fresh Orchestrators via managed-block required reading | rule superseded by later ADR | ORCHESTRATOR via AP change task |
| Cold-start operational checklist | operational projection | durable | AP.md §14/§4/RF-19 | AP_ORCHESTRATOR.md (new section) | same | superseded | same |
| Ledger storage/discovery semantics | normative semantics | canonical | AP.md §13 (RF-09 extension) | ARTIFACT_LIFECYCLE.md; INTEGRATION.md | consumers via AP.md | superseded | same |
| Ledger file + entry grammar | structural projection | durable | AP.md §13 | PROMPT_CONTRACTS.md (extended contract) | consumers via `.ap/PROMPT_CONTRACTS.md` | format version bump | same |
| Consumer ledger file (`AP_UPGRADE_LEDGER.md`, optional) | consumer projection | retained evidence (non-authoritative) | AP.md §13 (semantics); the consumer project owns content | none | project root, declared in project-owned AGENTS.md section | terminal reconciliation removes entries; file removal is a project task | project ORCHESTRATOR under task authority |
| Minimal resume seed example | explanatory projection | durable | AP.md | AP_ORCHESTRATOR.md (example block) | COOPERATORs | superseded | same |
| ADR-0016 | historical | durable | records this decision | docs/adr/ | maintainers | never (history) | none |
| Routing capsule | presentation only | — | consumer project rules (Communication Routing fields, AP.md:799–822) | none | project-local | project decision | project |

No duplicate owners; no new file besides ADR-0016; no cyclic discovery (seed → AGENTS.md → .ap documents → optional ledger; ledger never points back as authority).

## 5. Determination: is a new continuation projection file justified?

**No.** The discoverability gap is closed at the exact surfaces a fresh Orchestrator already must read: the managed block sends Orchestrators to `.ap/AP_ORCHESTRATOR.md`; placing the cold-start section there (high in the document, before role decision tables) plus two small AP.md semantic anchors makes the path discoverable with zero new artifacts and zero consumer migration. A separate `CONTINUATION.md` would be ~90% references to AP.md/PROMPT_CONTRACTS.md (reference-only content is correct per taxonomy but thin for a whole file), would create a fifth required-reading pointer and pressure to change the managed block (a consumer-migrating event), and adds divergence surface. Rejected alternative A keeps the same ledger contract; its only real advantage is a named file, which does not outweigh the migration and duplication costs. If field evidence later shows Orchestrators still miss the cold-start path, a named file can be reconsidered on that evidence.

## 6. Determination: is a durable observation-ledger storage projection justified?

**Yes — as an optional, canonical-name, consumer-owned file with an AP-owned structural grammar.** Without it, active observations (untriaged/accepted/parked) have no committed home, closure reconciliation has no durable output, and every pause forces reconstruction from handouts or memory — the exact dependency the COOPERATOR's success condition 4 excludes. It is justified as *storage/discovery only*: semantics stay in RF-09, spellings in PROMPT_CONTRACTS.md, content authority stays at zero (`Entry authority: non-authorizing` remains the only value). It is explicitly **not** a roadmap, issue tracker, current-task file, Worker registry, transcript, decision authority, second specification, NEXT file, or memory dump; deferred *project* work keeps its existing owners (roadmap/issues), and the ledger scope remains "improvement observations about a canonical repository" (AP.md:1994).

## 7. Dispositions evaluated

- **A (new AP continuation projection file + ledger contract):** rejected per §5 — unnecessary artifact, managed-block migration pressure, thin reference-only content.
- **B (extend existing projections; no new continuation file; add ledger storage contract): SELECTED.** Smallest change that closes all three proven gaps; zero compatibility breakage; preserves ADR-0013 owner split.
- **C (core sufficient; change only consumer integration/discoverability):** rejected — disproven by source: the ledger storage representation and the two-stage cold-start rule do not exist in core semantics, so there is nothing for a consumer-only change to point at.
- **D (reject proposal / no implementation):** rejected — gaps 1–3 are proven from current source and two independent field incidents; no-implementation perpetuates handout/private-memory dependence that AP's own closure contract (`Upgrade-ledger reconciliation: complete`) already assumes has a home.

## 8. Selected disposition and rejected alternatives (evidence)

Selected: **B**, with slices in §10. Rejected: A (§5), C and D (§7). Also rejected within the design space: using `extension.*.*` keys for ledger discovery (ignored-by-design, ADR-0012); changing the managed block (consumer migration without evidence of necessity); any `ap` command/schema change (no executable need proven; doctor already validates the tuple); encoding the COOPERATOR's emoji capsule (vendor-neutral protocol; presentation stays project-local); a YAML/JSON ledger format (adds parser expectations foreign to AP's text-record style; plain structured text stays human-first and machine-parseable).

## 9. Source precedence and contradiction handling

Unchanged and restated for the implementation Worker: latest explicit COOPERATOR decision > current verified repository/public state > durable accepted decisions/project rules > Worker-observed evidence > proposals > superseded options (AP_ORCHESTRATOR.md:50–64; AP.md:1226–1239). The ledger is always below repository truth: an entry contradicted by current repository evidence moves to `invalidated` with disposition evidence. Commit-bound revalidation of every baseline is mandatory at each new prompt (this plan's anchors: AP `041de310…`, FrameNest `230ce43a…`, Meta `01de27e1…`).

## 10. Ledger record grammar (selected)

File: **`AP_UPGRADE_LEDGER.md`** at the consuming project root; **optional**; one file may hold several `upgrade <canonical-repository>` sections. Plain Markdown with text records (AP structural style), human- and machine-parseable; no YAML dependency.

Header record:
```text
Ledger format version: 1
Artifact relationship: consumer projection; retained non-authoritative discovery input
```
Per ledger section:
```text
Ledger: upgrade <canonical-repository>
Activation snapshot: <bounded identity of candidate observations at activation>
```
Per entry (one record; superset of PROMPT_CONTRACTS.md:1417–1426):
```text
Entry: <stable kebab-case identifier, unique within the ledger; ordinals are presentation, never identity>
Entry state: untriaged | accepted | duplicate | rejected | invalidated | implemented | parked
Entry authority: non-authorizing
Summary: <one-line observation>
Evidence class: repository | worker-observed | cooperator-observed | external | inference
Observed at: <YYYY-MM-DD> against <immutable commit or external identity>
Last revalidated: <YYYY-MM-DD> against <immutable commit> | none
Implementation task grant: none | exact Orchestrator task <task-id> for <Worker boundary>
Implementation status: not-started | authorized | not-applicable | implemented with <durable evidence>
Disposition evidence: <report, decision, commit, or none>
Promotion target: adr | specification | roadmap | issue | logical-whole | none
Supersedes: <entry identity> | none
Closure action: retain-active | remove-from-active-ledger
Historical evidence: <commit, decision, changelog, or closure report holding the provenance>
Provenance destroyed: no
```
Required at all times: Entry, Entry state, Entry authority (only `non-authorizing`), Summary, Evidence class, Observed at, Provenance destroyed (only `no`). Conditional: grant/status from `accepted`; disposition evidence for any state past `untriaged`; closure action + historical evidence at terminal reconciliation; Last revalidated after any revalidation; promotion target for accepted/parked.

Identity/collision: new entry must be unique in its ledger; a colliding candidate is renamed or dispositioned `duplicate` of the existing entry. Ordering: deterministic — active states first in RF-09 order, then stable identifier; reordering happens only in an authorized reconciliation commit. Lifecycle states/transitions: unchanged, RF-09 owns. Authority boundary: unchanged — only an exact current Orchestrator task grant authorizes implementation; `accepted` records validity only. Staleness: `Observed at` vs `Last revalidated` commits are explicit; after any pause, restoration revalidates active entries against current repository truth before relying on them; contradiction → `invalidated`. Terminal handling: `implemented/rejected/duplicate/invalidated` entries are removed from the file at closure reconciliation with `Historical evidence` naming the immutable provenance (Git history preserves the file's past content). Malformed/missing/unknown-version: absence = zero active observations (safe default); malformed or unknown `Ledger format version` = treat whole file as non-authoritative plain-text evidence, do not parse structurally, Orchestrator reconciles with COOPERATOR — never blocks read-only restoration, never grants authority. Multiple targets: separate `Ledger:` sections in the one file. Privacy: public-safe by default; RF-19-style exclusions (no secrets, credentials, private paths/media, transcripts, hidden reasoning, unnecessary production detail). Memory disposability: once a reconciliation is committed, conversational memory carrying those observations is safely disposable — this is the property that removes the handout dependency for observations.

## 11. Staleness controls

Covered by grammar fields (Observed at / Last revalidated / invalidation triggers) plus the cold-start rule: after a pause the fresh Orchestrator revalidates active entries against current repository and public truth *before* selecting work; unverifiable entries stay non-authoritative and are reported, not trusted. Public AP `main` ahead of the consumer pin changes nothing: the pin governs; update is a separate task.

## 12. Privacy and safety constraints

Ledger file and seed carry no secrets, credentials, private host/path/media identifiers, transcripts, or hidden reasoning; public-safe by default because consumer repositories may be public. No authority arises from ledger content, the seed, or the cold-start checklist. No trace-as-authority: Meta remains optional historical evidence (AP.md:249–270).

## 13. Fresh/current routing boundaries

Unchanged (RF-05, ADR-0011). The cold-start section restates no routing semantics; it points to AP.md:580–762. Fresh Orchestrator after pause is the default boundary; Worker routing per whole follows existing triggers. No model/provider/client/IDE is named anywhere in the additions.

## 14. Artifact relationship map

Restoration prompt (chat synthesis of verified state) ≠ continuation contract (stable AP rule for how to resume) ≠ minimal seed (tiny COOPERATOR instruction that *points at* the contract) ≠ Discovery Record (optional decision-support evidence) ≠ repository handoff (exceptional unreconstructable state) ≠ observation ledger (non-authoritative upgrade observations) ≠ roadmap/issue (deferred project work) ≠ ADR (accepted architecture rationale) ≠ specification (product truth) ≠ project rules (consumer policy) ≠ Git history (immutable archive) ≠ Meta trace (optional selective causal history). Each keeps its consumer and lifecycle; the plan adds no overlap.

## 15. Minimal universal continuation seed — viable

Viable as an *explanatory example* inside the new AP_ORCHESTRATOR.md cold-start section (not protocol text, not required wording):

```text
Resume this AP-integrated project.
Read the root AGENTS.md and the pinned AP documents it names.
Begin read-only. Restore canonical state, reconcile the project
observation ledger, and select exactly one bounded next logical
whole with the COOPERATOR before granting any mutation authority.
```

The seed copies no protocol semantics, names no vendor/model/IDE/memory system, and works because every referenced step is discoverable from the managed block and the pinned tree. It fails safe: a missing ledger simply means zero active observations.

## 16. Integration and discovery mechanism

Discovery path: seed → consumer root `AGENTS.md` → managed block → `.ap/AP.md` + `.ap/AP_ORCHESTRATOR.md` (cold-start section) → optional project-root `AP_UPGRADE_LEDGER.md` declared in the project-owned AGENTS.md section (e.g., FrameNest's Project Truth list). **Managed block: unchanged.** `ap init`/`ap doctor`: unchanged. INTEGRATION.md gains a short paragraph documenting the optional ledger file and its project-rules declaration.

## 17. Compatibility impact

Existing pinned consumers: zero impact; block byte-identical, doctor unchanged, schema v1 unchanged. Ledger absent/malformed/stale/conflicting/optional: §10 behaviors (safe degradation, never authority, never blocks restoration). FrameNest's `tests/contract/test_ap_integration.py` asserts the managed block and pin — unaffected; later adoption whole may optionally extend consumer tests (consumer's own evidence surface, allowed by ADR-0015).

## 18. ap.project.conf / extension / managed block / ap / schema determination

No change to any of them. `extension.*.*` is ignored-by-design and project-local (ADR-0012) — rejected as a discovery surface. `ap init`/`doctor` already enforce the exact tuple; adding ledger checks to `ap` is **parked** (possible later whole: `ap doctor` optional ledger-shape structural check, only if field evidence shows ledger drift after adoption; not justified today, and ADR-0015 bars conformance-suite recreation — a single bounded structural lint is not a suite, but evidence does not yet require it).

## 19. Structural/executable validation

Documentation-first proportional validation only (ADR-0015): direct semantic review of the two AP.md additions, owner/projection review per ADR-0013, exact structural-spelling comparison of the new contract section against existing records, link/path checks across all touched projections, README/FAQ/GLOSSARY consistency, `git diff --check`, and fresh independent acceptance (mandatory: this changes the sole normative protocol and the structural schema — AP.md:342–344, 2184–2186). No suite, no mirrored protocol tests.

## 20. Likely changed paths (classification)

| Path | Classification | Change |
|---|---|---|
| AP.md | canonical semantic owner | §13: ledger storage/discovery paragraph; §14: two-stage continuation paragraph |
| PROMPT_CONTRACTS.md | structural projection | extend Upgrade Observation Ledger Contract with file grammar + added entry fields |
| AP_ORCHESTRATOR.md | operational projection | new "Fresh-Orchestrator cold start (project continuation)" section incl. seed example |
| ARTIFACT_LIFECYCLE.md | operational projection | ledger file lifecycle class, reconciliation/retention handling |
| INTEGRATION.md | operational projection | optional ledger discovery paragraph |
| README.md / FAQ.md / GLOSSARY.md | explanatory projections | reading-order row; one continuation Q&A; terms |
| CHANGELOG.md | historical | Unreleased entry |
| docs/adr/0016-project-continuation-and-observation-ledger-storage.md | historical | new ADR recording decision + rejected alternatives |
| docs/adr/README.md | historical | index row |
| ap, ap.project.conf, managed block, schema v1, tests/ | unchanged | — |
| FrameNest (all), Meta (all) | unchanged consumer/trace evidence | — |

## 21. Smallest coherent AP-only implementation boundary

Exactly the 11 paths in §20 in one commit; no other mutation. Everything else (doctor lint, FrameNest adoption, Meta-local layout alignment) is outside this boundary.

## 22. Implementation slices, ordering, gates

- **Slice 1 (this whole, only slice):** semantics + structures + projections + ADR-0016, one commit. Worker: fresh implementation Worker, `Native planning mode: not-used`, E2, High reasoning. Phase gate: implementation → fresh independent acceptance (mandatory: normative + structural change) → publication (E1/E2 non-force push, direct public readback) → ORCHESTRATOR closure with ledger reconciliation (CONT-001…010 dispositions recorded).
- **Later whole (separate):** FrameNest adoption — `ap update --check/--apply`, doctor, declare ledger in FrameNest AGENTS.md, create initial `AP_UPGRADE_LEDGER.md` carrying reconciled `upgrade cisarik/ap` entries, one reviewable commit.
- **Parked (needs future evidence):** `ap doctor` optional ledger-shape check; Meta-local zero-based suffix alignment (Meta's own decision).

## 23. Validation and fresh independent acceptance route

Implementation Worker validates per §19 and reports `implementation-PASS` (non-independent). A fresh independent acceptance Worker (new session ordinal, exchange 01) re-verifies: semantic-owner split intact, no duplicate ownership, structural spellings consistent with existing contracts, all cross-links resolve, no managed-block/schema/CLI drift (byte-identical), ADR-0016 matches the implemented decision, compatibility claims (§17) hold against FrameNest `230ce43a…` commit-bound. Then publication Worker pushes and proves public equality by credential-free direct Git readback. Closure requires ledger reconciliation: CONT-001/002/005 accepted (implemented by this whole), CONT-003 accepted-in-part (canonical filename + grammar; doctor check parked), CONT-004 rejected (presentation, project-owned), CONT-006 duplicate (RF-05/ADR-0011), CONT-007 rejected (vendor neutrality), CONT-008 duplicate/no-gap (recommendation placement is presentation; AP.md:1000–1018 owns the rule), CONT-009 rejected-for-AP (Meta-local layout, AP.md:268–270), CONT-010 accepted (drift control via indirection + structural grammar; executable lint parked).

## 24. Later FrameNest migration/adoption plan (separate whole)

Pin update via `./.ap/ap update --check/--apply` → `doctor --candidate` → project validation → stage gitlink → strict doctor → commit (UPDATING.md flow). Then project-local initialization: declare `AP_UPGRADE_LEDGER.md` in FrameNest AGENTS.md Project Truth section, create the file with format-version header and the reconciled `upgrade cisarik/ap` entries (final dispositions from this whole's closure), commit under one authorized task. No AP semantics copied into FrameNest; FrameNest remains a consumer, never a second owner. Contract test may stay unchanged; optional ledger-shape assertion is FrameNest's own choice.

## 25. Explicit exclusions and non-goals

No CONTINUATION.md; no managed-block/CLI/schema/ap.project.conf change; no executable ledger validation in this whole; no FrameNest or Meta mutation; no conformance suite; no roadmap/issue-tracker semantics in the ledger; no emoji/model/provider encoding; no transcript or memory storage; no reopening of the prompt-archive whole, the sidecar whole, or any other closed whole; no FrameNest product planning.

## 26. Single smallest next step

ORCHESTRATOR presents this plan to the COOPERATOR with exactly one material decision — confirm disposition B (extend existing projections) over A (new CONTINUATION.md file) — then issues one bounded fresh-Worker implementation prompt for slice 1 with the §20 allowlist, E2/High, `Native planning mode: not-used`, exact baseline re-verified at prompt time.

### The one COOPERATOR decision

Choice: disposition B (recommended; no new file, no migration) vs A (named CONTINUATION.md, managed-block link, consumer re-init migration). Evidence: §5. Consequence of B: smallest diff, zero compatibility cost, discoverability via existing required reading. Consequence of A: one more artifact + forced consumer block refresh; adopt only if named-file discovery is independently valued.

---

## Failure-model tests (falsification of the selected mechanism)

| Case | Behavior |
|---|---|
| New consumer, no ledger | absence = zero active observations; restoration proceeds read-only; safe |
| Consumer on older AP pin | contract simply absent from its pin; a project-root ledger file is harmless project-owned content |
| Six-month pause | cold-start revalidates entries against current truth; stale → `invalidated` with evidence |
| Public AP main ahead of pin | pin governs; update is a separate explicit task; ledger revalidated against the pin |
| Meta absent/private | ledger lives in the consumer repo; restoration needs no Meta — dependency removed |
| No chat memory / no outgoing Orchestrator | ledger + cold-start replace handout-carried observations; restoration prompt still summarizes but is no longer sole carrier |
| Empty/malformed/unknown-version ledger | non-authoritative text evidence only; never blocks read-only restoration; Orchestrator reconciles with COOPERATOR |
| Observation contradicted by repo truth | repository truth wins; entry `invalidated` at reconciliation |
| Accepted observation, no grant | no authority (`non-authorizing`; grant field `none`) |
| Terminal observation | removed from file at closure reconciliation; provenance named; Git history preserves |
| Multiple canonical repositories | multiple `Ledger:` sections in one file |
| Handwritten prompt with invalid structural fields | cold-start routes spellings to PROMPT_CONTRACTS.md (indirection); drift risk reduced at source |
| Project with roadmap/issues owning deferred work | ledger scope stays upgrade-observations-only (AP.md:1994); deferred work promotes to roadmap/issue |
| Stricter local project rules | project may be stricter; cannot weaken non-authority (INTEGRATION.md:210–221) |
| Client without native planning mode | `not-used` route already exists (AP.md:664–674) |
| Agent with only seed + AGENTS.md + pinned AP | full discovery path §16 — terminates at one bounded whole + COOPERATOR decision |

Every failure mode resolves to: fail closed, degrade to non-authoritative evidence, ask the COOPERATOR, or stop before mutation. None requires new semantics beyond slice 1.

## Terminal control record

- Temporary clones: none created (all reads were direct against clean baselines, or commit-bound `git show` for FrameNest).
- Planner artifact location: this plan file only (client-native planner surface, outside AP/FrameNest/Meta).
- Repository/external mutations: none.
- Planning authority expires at the terminal report accompanying this artifact.

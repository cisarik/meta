### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ap-subagent-lifecycle-and-intuitive-mode-spec
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Standard terminal status: PASS
Phase-qualified result: planning-PASS
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: all Worker 01 exchange 01 planning authority expires at this terminal report
```

# A. Verdict

```text
AP change required
Chosen shape: A — documentation/projection only
```

Current public AP already owns most locked invariants (three roles, no-opaque-swarm, internal-delegation-is-not-audit, compact-communication, presentation-is-not-authority, trace staging). Three narrow semantic gaps justify a smallest portable AP.md clarification set, plus one brief projection file: (1) Orchestrator capability profiles (Agent vs Read-Only) are not yet defined anywhere, and current sub-agent text is exclusively Worker-side, so an Orchestrator reading `AP.md` alone could conclude native dispatch of a Worker session is forbidden; (2) the independence disqualifier for a parent-context, Orchestrator-dispatched session is not stated for that configuration (existing disqualifiers cover only "internal agents within one coordinated Worker run"); (3) no consolidated positive/negative Orchestrator-direct ("intuition") boundary exists. `INTUITION.md` is justified as a brief explanatory projection because Lock 3 requires it, but it owns no meaning.

# B. Identity and evidence reconciliation

| Item | Observed (all revalidated read-only, 2026-08-27) | Classification |
|---|---|---|
| AP root | `/home/agile/Projects/ap`; origin fetch/push `https://github.com/cisarik/ap.git`; public `refs/heads/main` via credential-free `git ls-remote` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | Canonical AP owner |
| AP HEAD/tree/parent | `9c5cc44…` / `43bc12b966133d76972ccf3884d80dceedde013b` / parent `10ac2ed…`, subject `docs: mark ADR-0018 accepted`; branch `feat/consumer-declared-route-binding`; `origin/main` = HEAD | Local equals public main; clean tree; matches anchors exactly |
| AP active operations | No `rebase-merge`/`rebase-apply`/`sequencer`/`MERGE_HEAD`/`CHERRY_PICK_HEAD`/`REVERT_HEAD`/`BISECT_LOG`/`index.lock`. A stale `.git/REBASE_HEAD` (`573975c…`) exists with no sequencer directories and clean tree | Stale leftover from a completed rebase; not an active operation |
| AP worktrees | 3 sibling worktrees (`…ergonomics…-w2` @`95bd644`, `…continuation…-w3` @`a1b04ff`, `…-w5` @`17b7e08`); all three tips verified `merge-base --is-ancestor` of `origin/main`; all three worktrees clean (0 status entries) | Already-published owner work on other branches; no unpublished AP-owner overlap with candidate owners; no hard stop |
| AP root `AGENTS.md` | Absent (verified) | Expected for protocol source; absence recorded |
| AP `INTUITION.md` | Absent in AP source and in FrameNest `.ap/` (verified) | Confirmed new-file scope |
| FrameNest | HEAD `472553cadcd3d4ca87a9792a2c306bd0afeea7c1` = public main (ls-remote agrees); branch `feat/x-meme-browser-companion`; 8 commits ahead of `origin/feat/x-meme-browser-companion` (`afa0670…`), verified ancestor of HEAD; tracked status clean; tree `89e7ef1…`; parent `687b5af…` | Leftover branch name at the public-main line, as the anchors stated; no unpublished product work; freeze respected |
| FrameNest AP pin | `.ap` gitlink = `9c5cc44…`; submodule HEAD = same | Consumer pin equals current public AP; pin is evidence only, not a work surface |
| FrameNest consumer evidence | Root `AGENTS.md` (managed AP block + presentation/communication rules, read as context); `docs/AP_UPGRADE_OBSERVATIONS.md` header (RF-09 consumer ledger, one `untriaged` non-authorizing entry); ROADMAP "Frozen and Parked Product Logical Wholes" confirms Cooperator-directed freeze | Consumer-side; Era 05 must not mutate ledger, pin, or product |
| Meta | `/home/agile/meta`; HEAD `6bda32b8abf50ffbc8b28234a864dd3f65487ba6` = public `main` (ls-remote agrees); status: 1 modified tracked entry + 2 untracked entries (counted, not enumerated per privacy rule) | Dirty/untracked local Meta work including this Era 05 directory; classified, preserved, not repaired; no private filenames exposed |
| Meta named files | `05/00_handout.md` (192 lines, strategic handout — matches the prompt's characterization); `05/01_planning_00.md` (1,177 lines — **the staged copy of this planning prompt**, verbatim at head; a live precedent of Orchestrator staging at the activated destination); Era 03/04 `01_planning_00.md` files inspected in bounded head sections as craft examples | Historical evidence only; not authority |
| Searches | `subagent/sub-agent`: only Worker-side delegation rows and anti-delegation text (PROMPT_CONTRACTS 845/868/949; AP.md 1249/1252; ADR-0011 116). `intuitiv/intuition`: **zero hits in the AP repo** (wholly new naming). `emoji`: only rejection/presentation contexts (ADR-0017:106; PROMPT_CONTRACTS:656; INTEGRATION:102; AP.md:2498) | No existing "Intuitive Mode" semantic home; no contradiction with Lock 2 |
| Native Plan Mode | Requested `required`; **observed ACTIVE** — direct platform system reminder "Plan mode ACTIVE — READ-ONLY phase" with read-only enforcement for this session | Evidence class: directly observed platform state; §7 precondition satisfied; not BLOCKED |
| Evidence limitations | Era 03/04 planning prompts read in bounded head sections (~120 lines each) — they are craft examples, not authority; INFOSEC.md not inspected (no security-profile interaction; per §10 default); full staged Era 05 prompt head-matched then not re-read; Meta dirt enumerated only by state counts | None of these affect the semantic boundary |

No hard-stop condition from §8 occurred. No fetch/checkout/write was needed: public main equals the local checkout byte-for-identity.

# C. Semantic-owner and projection map

Existing ownership (verified, cited) — the parts AP **already owns**:

| Locked intent | Current canonical owner (AP.md) | Key evidence |
|---|---|---|
| Three persistent roles only | §2 Roles | AP.md:548–582; "Worker session profiles, capability profiles, phases, execution clients, and internal delegation arrangements do not create additional persistent roles" (580–582) |
| No opaque agent-to-agent default | Preamble; §19 Anti-Patterns | AP.md:7–12; 2524; ADR-0011:22–24, 40–43 |
| Internal delegation = one accountable WORKER, never audit | §3; §6 surface routing; PROMPT_CONTRACTS routing row | AP.md:621–626; 1252–1254; PROMPT_CONTRACTS:845, 868, 949–951 |
| Internal agents in one Worker run are not independent auditors | §3 Plan-to-Execution; Fresh Independent Audit contract | AP.md:816–817; PROMPT_CONTRACTS:2125–2127; ADR-0008:142–147 |
| Freshness ≠ independence | RF-05; §3 | AP.md:133–135; 680 |
| Acceptance bounded to candidate/owner map/allowlist/risk/matrix | Acceptance, Correction, and Escalation | AP.md:393–399 |
| Sole-protocol change ⇒ fresh independent acceptance | Acceptance section + §15 | AP.md:396–399; 2396–2399 |
| Session target = "session into which the prompt must be delivered" (delivery-mechanism-neutral) | §3 Worker Session Target; structural contract | AP.md:650–656, 703–706; PROMPT_CONTRACTS:351–353 |
| Deterministic steps need no microapproval; Orchestrator-direct work exists | Preamble; RF-01; reasoning rule | AP.md:7–12; 96–99; 1081–1082; ADR-0006:97–100 |
| Prompt synthesis duty + density-not-length | §7 synthesis; §17 Compact Communication | AP.md:1311–1344; 2429–2464 ("catalog, not a dump" 2440–2446) |
| Trace staging/archival ownership | RF-19; Orchestrator + lifecycle projections | AP.md:322–326; AP_ORCHESTRATOR.md:180–188; ARTIFACT_LIFECYCLE.md:70–76 |
| Workers never self-archive | Worker projection; delivery record | AP_WORKER.md:63–67; PROMPT_CONTRACTS:653–656 |
| Presentation marks / emoji never authority | RF-02; anti-patterns; ADR-0017; INTEGRATION | AP.md:107–110; 2498–2499; ADR-0017:106–107; INTEGRATION.md:100–102, 117–119 |
| Isolation is not a virtue; topology with a why | §5; ADR-0017; PEP fixture | AP.md:938–939; ADR-0017:59; PEP:1234–1254 |
| Executable `ap` does not construct/validate prompts | RF-16 | AP.md:237–240; ADR-0018:74–78; executable inspected (1,109-line shell; no prompt/subagent surface) |

**One-page owner map for the seven plan items** (owner → projections):

| Item | Canonical semantic owner (AP.md) | Structural | Operational | Advisory/explanatory | Historical | Executable | Consumer-owned | Risks/contradictions |
|---|---|---|---|---|---|---|---|---|
| Dual-mode Orchestrator (Agent / Read-Only) | §2 + RF-06 (capability dimension; profiles-are-not-roles) + RF-02 (routing recommendation) | PROMPT_CONTRACTS: none new (routing rows suffice) | AP_ORCHESTRATOR: brief profile guidance | INTUITION.md §2; GLOSSARY entries | ADR-0020 | none | presentation labels only | must not add a fourth uppercase role (AP.md:577–582); names stay descriptive |
| Intuition boundary (Orchestrator-direct vs Worker-required) | RF-02 (decision authority) + RF-06 (capability ≠ authority) + RF-01 (deterministic steps in envelope) | none new | AP_ORCHESTRATOR: boundary list | INTUITION.md §3 | ADR-0020 | none | — | must not become implementation authority or Plan-to-Execution bypass (RF-04; AP.md:770–782) |
| Subagent-as-Worker-delivery | §3 (session target/delivery) + RF-02 (routing) + RF-03 (bounded authority/report) | PROMPT_CONTRACTS: one scope-clarifying sentence at the delegation row; no new field | AP_ORCHESTRATOR dispatch section; AP_WORKER delivered-session note | INTUITION.md §4 | ADR-0019 | none (verified) | local delivery presentation | PROMPT_CONTRACTS:845 "not-used unless explicitly authorized" could be misread as a dispatch ban — the clarification must resolve exactly this |
| Independent-audit freshness properties | RF-05 + §3 (fresh-session properties) | PROMPT_CONTRACTS Fresh Independent Audit contract (already owns inputs) | AP_WORKER independence section | INTUITION.md §5 checklist | ADR-0019 | none | — | must not soften "freshness alone does not prove independence" (AP.md:134–135) |
| Compact synthesis (token-proportional) | §17 + §7 readiness review (already own) | none | AP_ORCHESTRATOR prompt construction (already owns) | PEP: one bounded advisory pattern; INTUITION.md §6 | ADR-0017, ADR-0020 | none | project envelopes | no caps (ADR-0017:104–105); no completeness-floor deletion (AP.md:2442–2446) |
| Opt-in signaling vocabulary | RF-02 (presentation marks not authority) + INTEGRATION optional presentation profile (already owns) | none (PROMPT_CONTRACTS:656 already excludes emoji-as-fields) | none required | INTUITION.md §7 pointer | ADR-0017 | none | project-owned profile in root `AGENTS.md` outside managed block | must never become a Worker-authority gate (Lock 2) |
| Activated-trace Orchestrator write | RF-19 (already owns staging + archival owner) | PROMPT_CONTRACTS delivery/trace records (already own) | AP_ORCHESTRATOR/ARTIFACT_LIFECYCLE (already own) | INTUITION.md mention only | ADR-0014/0017/0019 | none | local grammar per consumer | no Meta-grammar-as-AP; local spelling stays local (PROMPT_CONTRACTS:658–671) |

RF-19 itself needs **no semantic edit**: staging is already lawful ("unless a separately authorized workflow owns a safe staging location", AP.md:322–326; AP_ORCHESTRATOR.md:186–188), and this exchange's own staged prompt file is live precedent. RF-08 untouched; RF-19 untouched — only RF-02, RF-05, RF-06 gain targeted sentences.

# D. Chosen implementation shape and exact semantics

### Shape comparison (required)

| Shape | Assessment against evidence |
|---|---|
| **A — documentation/projection only** | Fits all three gaps with ~6 targeted AP.md sentences/paragraph edits, 1 new ≤200-line projection, 2 historical ADRs, ≤8 projection files. Reuses RF-02/05/06. Matches ADR-0017/0018 precedent exactly (extend existing families, no new fields). **Recommended.** |
| B — one new RF family | Rejected: every facet maps to an existing family (map in §C); a new family would duplicate ADR-0011/0017 semantics and violate the semantic-owner registry discipline (ADR-0013). No gap proven. |
| C — advisory-only, no AP.md change | Rejected: the decisive clause (PROMPT_CONTRACTS:845/949, AP.md:1252–1254) reads "not-used unless explicitly authorized" about *Worker-side* delegation with no Orchestrator-dispatch counterpart; meaning must live in `AP.md` (ADR-0013; Lock 3). Advisory-only would leave consumers unable to see that dispatch is lawful, and would push semantics into `INTUITION.md` — the exact second-owner failure the locks forbid. |
| D — split into two logical wholes | Rejected: the coherent allowlist is ~13 paths, well inside the Complexity Budget, and all changed owners share one acceptance scope (documentation-only, E1/E2-class). Splitting would create two wholes touching `AP.md` twice with no independent acceptance benefit. |
| E — no change / park / reject | Rejected for the three named gaps: they are real (verified absence of Orchestrator-profile and dispatch-delivery semantics; zero "intuition" hits in repo). Not vendor-specific: every requirement below is functional. Not duplicative of ADR-0011/0017 (they own delegation and compact grants, not Orchestrator dispatch delivery). |

### Exact semantics to implement

1. **Applicability trigger.** An *Agent Orchestrator* is an ORCHESTRATOR instance whose client functionally exposes session-dispatch/tool capabilities **and** whose Cooperator-selected route and accepted plan explicitly authorize using them. A *Read-Only Orchestrator* lacks, or is not authorized to use, dispatch/tools. Both are the same persistent ORCHESTRATOR role; the names are descriptive capability-profile labels and **must not** become a fourth uppercase role (AP.md:577–582). Selection is recorded through existing Cooperator routing sovereignty; a profile never grants authority (RF-06).
2. **Orchestrator-direct allowed** (all must hold: inside an accepted logical whole's routing duty; deterministic or reversible; no AP-owner mutation; no independence claim; no Cooperator-owned material decision substituted; within the accepted plan): (a) synthesizing and readiness-reviewing Worker grants; (b) read-only repository/public inspection and preflight; (c) writing and archiving activated-trace artifacts at the declared destination per RF-19 — staging before the outcome only at the authorized safe staging location, atomic prompt+report archival only after the report exists, interruption companion only per its rules; (d) creating/removing a dispatch worktree or staging location **when the accepted plan or the implementation grant names that working-copy topology**; (e) emitting the project-owned Cooperator presentation package after the copyable English prompt; (f) restoring/cleaning its own routing state (its own staged files/worktrees); (g) direct acceptance at evidence-ladder rung 1 for E0/E1-class claims.
3. **Worker-required (never Orchestrator-direct):** any mutation of `cisarik/ap` owners or authoring of AP content; any implementation-PASS claim on a material candidate; any acceptance requiring independence; publication, deployment, production; consumer pin updates; any FrameNest/NUC/credential/host/account change; any material protocol-design decision not already locked or accepted; any action outside the allowed list. Intuition never bypasses Plan-to-Execution (RF-04).
4. **Worker-dispatch functional properties.** Dispatch delivers **one complete authoritative Worker prompt** — coordinates, session target, profile, boundaries, report contract — into one concrete session; a tool-task summary never substitutes for the prompt. The receiving session is an ordinary AP Worker session: RF-03 applies unchanged (one bounded result, one terminal report, authority expiry); RF-19 coordinates apply unchanged (next session ordinal; exchange `01` for fresh). One accountable WORKER per dispatched session; the dispatching Orchestrator remains ORCHESTRATOR. Dispatch visibility flows through routing records and Cooperator-legible prompts/verdicts; the default remains not-used — dispatch requires explicit Cooperator-selected-route/plan authorization. Parallel dispatch stays under the single-active-workstream default and bounded parallel exception; an audit is never dispatched in parallel with implementation.
5. **Independent-audit observable properties** (each individually checkable): `Worker session target: fresh-worker-session`; next session ordinal, exchange `01`; zero parent conversation, shared memory, compaction summary, or Orchestrator reasoning/implementation rationale beyond the acceptance record inputs (candidate, owner map, allowlist, risk claims, control matrix, governing AP, repository truth — AP.md:393–399); a different concrete session from the implementer (never a profile relabel); worktree isolation is a topology choice with a why, never proof. **Disqualifier to add:** a session spawned inside the parent Orchestrator's conversation, or inheriting its conversation history or reasoning, is not a fresh session and cannot provide independent acceptance. **Vendor-neutral functional test** for Cursor Task, opencode task, or a fresh chat window alike: the spawned session receives only the issued prompt text as initial context, holds no parent transcript, and returns its terminal report to the Orchestrator. Named runtimes are non-normative examples only.
6. **`Sub-agents/internal delegation` recording rule.** The existing row (PROMPT_CONTRACTS:845/868/949) records delegation **initiated by the Worker session**; it is unchanged for that purpose. Orchestrator dispatch is recorded through existing fields only — `Worker session target`, coordinates, session profile, and the routing record (`Cooperator-selected route`) — optionally with one negative-authority line in the prompt; no new field is created. A dispatched session records `not-used` unless it itself delegates internally.
7. **`INTUITION.md` relationship.** Durable **explanatory projection** (with advisory quick-rules) of `AP.md`; `AP.md` prevails on any conflict; optional; never required reading in the managed block; versioned by the AP pin like every projection.
8. **Compact-synthesis rule.** Cite owners (AP.md sections, PROMPT_CONTRACTS records) instead of recopying; activate only triggered annexes; keep the §17 completeness floor (AP.md:2442–2446); no token/currency caps; no generator-owner (ADR-0017:104–105; P18, PEP:1109–1111).
9. **Opt-in signaling.** Project-owned presentation under INTEGRATION.md's existing optional profile ("localize language or marks" already covers marks, INTEGRATION.md:117–119); never AP fields; never a Worker-authority gate; inactive by default; `INTUITION.md` carries one pointer paragraph only. No INTEGRATION.md edit is required.
10. **Activated-trace auto-write.** Already lawful RF-19 staging plus Orchestrator archival duty; Workers do not self-archive (AP_WORKER.md:63–67); Era 05's `_00` local spelling remains trace-local (PROMPT_CONTRACTS:658–671); FrameNest keeps its own activated grammar; this whole does not mutate Meta.
11. **Compatibility.** Prospective only. Historical prompts interpret under their original pins (AP.md:332–334; ADR-0018:97–102). Existing pins retain original meaning; consumers that never read `INTUITION.md` lose nothing (additive file, no managed-block change, adoption = pin update + optional reading). Read-Only Orchestrators are fully valid today and after (profiles describe; they do not require).
12. **Failure and stopping behavior.** If dispatch capability is absent, unauthorized, or cannot satisfy the completeness/freshness properties, the Orchestrator issues an ordinary prompt through copy-paste delivery — unchanged lawful behavior (AP.md:703–706). A dispatch that cannot deliver the complete prompt is not a dispatch; no summary-prompt shortcut. A dispatched session stops on any ordinary Worker stopping condition; a dispatched session that discovers parent-context inheritance stops and reports it.
13. **Vendor-neutral example policy.** Functional language only; named runtimes may appear as labelled non-normative examples in advisory text (PEP discipline); AP requires no vendor, tool, or adapter layer (Q5 presumption confirmed: AP.md:591–593; ADR-0008 rejected vendor-specific session identifiers).

# E. Exact later implementation allowlist

Under `/home/agile/Projects/ap`, all paths repository-relative:

| Path | Why necessary | Relationship | Change type | Verification owner |
|---|---|---|---|---|
| `AP.md` | Owns all new meaning (Lock 3/ADR-0013) | canonical semantic owner | targeted edits: §2 +1 sentence (Orchestrator capability profiles are not roles); §3 +2 short paragraphs (Orchestrator capability profile; dispatch delivery; fresh-session parent-context disqualifier); RF-02 +boundary sentences; RF-05 +1 sentence; §19 +1–2 anti-pattern bullets; Related Documents +1 link | direct semantic review |
| `INTUITION.md` (new) | Lock 3 requires the brief projection | explanatory/advisory projection | new file ≤200 lines | projection + relationship review, line-count check |
| `docs/adr/0019-subagent-delivery-of-worker-sessions-and-orchestrator-capability-profiles.md` (new) | Historical rationale for dispatch/independence/profile decisions | historical | new ADR | historical-accuracy review |
| `docs/adr/0020-intuitive-mode-orchestrator-boundary-and-intuition-projection.md` (new) | Historical rationale for intuition boundary, synthesis pattern, INTUITION.md, opt-in signaling | historical | new ADR | historical-accuracy review |
| `docs/adr/README.md` | Index the two ADRs | historical index | 2 index rows + short notes | link/index review |
| `AP_ORCHESTRATOR.md` | Operational dispatch + profile + boundary guidance | operational | add one short section (~25 lines) + decision-table row | projection review |
| `AP_WORKER.md` | Delivered-session note (minimal) | operational | +2–3 sentences in Session Target / Independence sections | projection review |
| `PROMPT_CONTRACTS.md` | Recording-rule scope clarification at the existing delegation row | structural | clarifying sentences only; **no new field** | structural review (field inventory unchanged) |
| `PROMPT_ENGINEERING_PATTERNS.md` | One advisory dense-synthesis pattern | advisory | +1 pattern (~30 lines) + index row | advisory review |
| `README.md` | Discovery of INTUITION.md | explanatory | +1 reading-order row (+ optional Related line) | link/path review |
| `ARTIFACT_LIFECYCLE.md` | Distribution-relationships table completeness | operational lifecycle | +1 table row for INTUITION.md | projection review |
| `GLOSSARY.md` | 2–3 new terms stay consistent | explanatory | +3 table rows (Agent Orchestrator, Read-Only Orchestrator, Subagent dispatch) | explanatory review |
| `CHANGELOG.md` | Delivery record | historical | 1 Unreleased entry | historical review |

Count: 1 semantic owner + 1 new file + 2 ADRs + 2 historical indexes + 8 projection files (AP_ORCHESTRATOR, AP_WORKER, PROMPT_CONTRACTS, PEP, README, ARTIFACT_LIFECYCLE, GLOSSARY, CHANGELOG). Default posture held: no new RF family (RF-19 untouched; only RF-02/05/06 edited), no command, no schema, no managed block, no consumer-specific universal example, no executable change, no FrameNest/pin/NUC/credential/environment/product mutation.

**Explicit forbidden paths:** `ap` and `ap.project.conf` (incl. the embedded managed-block text — a change would force consumer `AGENTS.md` edits); `INFOSEC.md`; every FrameNest path including `.ap/` inside FrameNest and the consumer ledger; Meta; any new RF family file; any new schema, command, CI, test, or conformance mechanism; managed-block templates; `UPDATING.md` and `FAQ.md` and `INTEGRATION.md` (verified consistent without edits — UPDATING pin language unaffected; FAQ answers remain true; INTEGRATION "marks" text already covers signaling).

# F. Documentation versus executable decision

```text
Docs/projection only
```

No executable surface adjustment: the invariants added are semantic and operational; nothing here requires mechanical observation. Executable `ap` cannot and must not observe subagent independence or prompt density (Q22 — verified: RF-16 AP.md:237–240, ADR-0018:74–78, and direct inspection of the 1,109-line shell tool, which contains no prompt construction or subagent surface). ADR-0015 requires exactly the documentation-first proportional validation proposed in §H — no suite, no validator (ADR-0015:36–51). Documentation cannot "decide" less here because the gaps are precisely rules an Orchestrator must read and follow; failure model without the change: Orchestrators either keep copy-paste-only (friction) or improvise unbounded swarm dispatch (governance risk); maintenance owner is the AP source repository; compatibility is prospective pin-based; focused verification is the §H matrix.

# G. `INTUITION.md` specification

The file **should exist** (Lock 3). Specification tight enough that implementation cannot inflate it:

- **Title:** `# AP Intuition — Brief Orchestrator Projection`
- **Opening paragraph (exact content class):** declares artifact relationship (explanatory projection of AP.md's Semantic Authority section, with advisory quick-rules), states `AP.md` is the sole semantic owner and prevails on any conflict, states the file is optional and never required reading, and links the canonical anchors (RF-02, RF-05, RF-06, RF-19; ADR-0011, 0013, 0017, 0019, 0020).
- **Ordered sections** (one-sentence purpose each):
  1. *What this file is* — relationship, non-owner warning, canonical links.
  2. *Roles and capability profiles in one page* — three roles; Worker session profiles; Orchestrator capability profiles (Agent / Read-Only) as descriptions, not roles.
  3. *Orchestrator intuition boundary* — the positive list (§D.2) and Worker-required list (§D.3) as compact paired tables.
  4. *Subagent dispatch as Worker delivery* — functional properties (§D.4) without any vendor API.
  5. *Fresh independent audit checklist* — observable properties and disqualifiers (§D.5) as a short checklist.
  6. *Dense grants by citation* — cite/activate/compact-catalog pointers to §17 and the pattern library; no caps.
  7. *Optional signaling* — one paragraph: marks are project-owned presentation (INTEGRATION.md profile), never authority, inactive by default.
  8. *Failure quick list* — one-line each with links: opaque swarm, parent-context audit, emoji-as-authority, INTUITION-as-AP.md, ceremonial extra Workers, isolation-as-virtue, intuition-as-implementation-authority.
- **Hard line budget:** ≤ 200 lines (target ≤ 170). The implementation Worker must report the exact line count.
- **Required canonical links:** AP.md (Semantic Authority, §2, §3 Worker Session Target, RF-02, RF-05, RF-06, RF-19, §17, §19); PROMPT_CONTRACTS.md (Session-And-Mode Routing Contract; Cooperator Delivery record); INTEGRATION.md (Optional Presentation Profile); PROMPT_ENGINEERING_PATTERNS.md; the two new ADRs.
- **Do-not-duplicate list:** full role definitions; E0–E4 evidence-tier catalog; RF-19 coordinate rules verbatim; prompt/report field schemas or Common Worker Task Fields; stopping-condition or anti-pattern catalogs in full; emoji tables as fields; vendor API manuals; INFOSEC procedures; any field spelling owned by PROMPT_CONTRACTS.md.
- **Sample table of contents (not file text):**

```text
1  What this file is                     (~10 lines)
2  Roles and capability profiles         (~20)
3  Orchestrator intuition boundary       (~35)
4  Subagent dispatch as Worker delivery  (~30)
5  Fresh independent audit checklist     (~30)
6  Dense grants by citation              (~20)
7  Optional signaling                    (~10)
8  Failure quick list                    (~20)
```

# H. Verification matrix

| Changed owner | Direct semantic review | Projection/relationship review | Structural check | Positive example | Negative examples | Compatibility/historical | Link/path/Git |
|---|---|---|---|---|---|---|---|
| `AP.md` §2/RF-06 (profiles) | ✔ | ✔ | profile labels are not new uppercase roles; field inventory unchanged | Agent Orchestrator dispatches a fresh audit subagent lawfully under an authorized route | Read-Only Orchestrator treated as incapable of closing or routing (must remain fully valid); a fourth role claimed | pins unchanged; §2 sentence preserves 580–582 | anchors resolve |
| `AP.md` §3/RF-05 (dispatch + disqualifier) | ✔ | ✔ | no coordinate grammar change; existing fields express dispatch | fresh audit subagent with zero parent context, next ordinal, exchange 01 | parent-context subagent claimed as independent audit; emoji used as task authority; intuition used as implementation authority | historical prompts unchanged (AP.md:332–334) | anchors resolve |
| `AP.md` RF-02 (boundary) | ✔ | ✔ | — | Orchestrator stages the issued prompt at the activated destination, archives pair after report | Orchestrator mutating AP owners or claiming implementation PASS directly | RF-01 deterministic-steps semantics preserved | — |
| `PROMPT_CONTRACTS.md` | ✔ | ✔ | exact: no new field/record added; delegation row scope sentence only | dispatched session's row reads `not-used`; dispatch recorded via target/coordinates/routing | row repurposed to gate Orchestrator authority | structural fixtures untouched | — |
| `AP_ORCHESTRATOR.md` / `AP_WORKER.md` | ✔ | ✔ | — | operational dispatch section mirrors RF-02/RF-03 exactly | handbook adds a requirement not owned by AP.md | read-through against owners | links resolve |
| `INTUITION.md` | ✔ | ✔ | line count ≤ 200; relationship declared; no field spellings | a newcomer routes a simple task correctly from it alone | file redefines a rule or copies the E-tier catalog | optional reading; consumers without it unaffected | all links resolve |
| `PEP` pattern / `GLOSSARY` / `README` / `ARTIFACT_LIFECYCLE` | ✔ | ✔ | index/row additions only | advisory pattern composes existing fields | pattern becomes hidden requirement | advisory classification kept | links resolve |
| ADRs 0019/0020 + index + CHANGELOG | ✔ | ✔ | historical status; no live semantic claim | — | ADR written as current authority | bodies historical | SHA/path checks |

No full repository suite is prescribed (no named decision risk requires one; ADR-0015). No executable evidence (no executable behavior changes). Read-Only Orchestrator compatibility and consumer-never-adopting compatibility are explicit review rows above.

# I. Lifecycle after plan approval (grants no authority now)

1. Orchestrator + Cooperator accept or reject this plan.
2. New complete implementation prompt with `Native planning mode: not-used`, `Worker session target: fresh-worker-session`, canonical-checkout or isolated-worktree topology per the implementing grant's rationale (read-only planning needed no worktree; implementation may, with a why).
3. One fresh Implementation Worker, one initial implementation attempt, candidate commit on an AP working branch (publication separate).
4. Bounded correction only for one concrete classified defect.
5. One fresh independent acceptance Worker in a session with no parent conversation — **required** because this mutates the sole protocol (AP.md:396–399, 2396–2399); it receives only candidate, owner map, allowlist, risk claims, control matrix, governing AP, repository truth.
6. Correction re-acceptance only if needed — `full-fresh` if a semantic owner, independence rule, or structural field changed (a change to RF-02/05/06 semantics is a semantic-owner change).
7. Explicit AP publication gate and credential-free public readback.
8. AP logical-whole closure after declared evidence, Orchestrator-owned.
9. Later separate consumer-adoption wholes (FrameNest pin update, reading list, optional presentation profile) only if the Cooperator selects them.
10. No automatic NUC deployment, FrameNest product work, ledger write, or pin update.

# J. Rollback and residual risk

- **Git rollback:** single revert of the AP branch candidate commit(s); no history rewrite; pins and consumers untouched by definition.
- **Projection inconsistency recovery:** the owner map in §C is the checklist; a defective projection is corrected by targeted follow-up edit under the same re-acceptance rules.
- **Consumers that never adopt `INTUITION.md`:** no managed-block or field change; behavior identical to today.
- **Read-Only Orchestrators:** profiles describe capability, require nothing; copy-paste delivery stays first-class lawful.
- **Opaque-swarm risk:** default `not-used` preserved; one accountable WORKER per session; Cooperator legibility via routing records and Cooperator-legible verdicts; anti-pattern bullets added.
- **False-independent-audit risk:** the new disqualifier plus the negative example make parent-context spawn a stop-and-report condition; isolation-as-proof explicitly rejected.
- **`INTUITION.md` as second protocol in the field:** mitigated by relationship declaration, non-owner warning, line budget, no field spellings, and ADR-0013/0020 framing; residual field risk exists and is accepted as presentation drift, detectable in review.
- **Overfit to Cursor / FrameNest Meta grammar:** functional language only; named tools appear only as labelled advisory examples; `_00` grammar stays trace-local (PROMPT_CONTRACTS:658–671).
- **Documentation-only enforcement limits:** normative-operational, not mechanical — the same posture ADR-0018 accepted; no surface observes these rules; residual risk of silent non-compliance is inherent to all of AP's documentation-first evolution.
- **Residual copy-paste friction:** clients without native dispatch are unchanged; no AP text requires dispatch.

# K. Complexity Budget

```text
Canonical semantic owner files: 1 (AP.md)                                  — plan uses 1
New RF families: 0                                                         — plan uses 0
INTUITION.md: 1 new file, <= 200 lines                                     — plan: 1 file, target <= 170
Existing RF families touched: at most 4 (presumption RF-02/05/06/19)       — plan uses 3 (RF-02, RF-05, RF-06; RF-19 verified unchanged)
Operational/structural/advisory/explanatory projection files: at most 8    — plan uses exactly 8
New ADRs: at most 2                                                        — plan uses 2
CHANGELOG / adr README: as required historical index only                  — 2 index entries
Executable surfaces changed: 0                                             — 0
New executable/conformance mechanisms: 0                                   — 0
Consumer repositories changed: 0                                           — 0
Managed blocks changed: 0                                                  — 0
Schema versions changed: 0                                                 — 0
New universal commands: 0                                                  — 0
New required PROMPT_CONTRACTS fields: 0                                    — 0 (one clarifying sentence only)
Plan-only cycles: exactly 1                                                — 1 used
Implementation attempts before classified correction: 1                    — n/a (later whole)
Fresh independent acceptance Workers after implementation: 1               — planned
```

The coherent plan fits the budget with margin; no expansion is needed.

# Repository-grounded questions — consolidated answers

1. **Capability profiles, not a fourth role** — AP.md:580–582 already declares profiles non-role-creating; the pattern extends to ORCHESTRATOR; names must stay descriptive (577–582). Contradiction avoided by not adding uppercase role names.
2. **Orchestrator-direct action today:** authorized for synthesis/inspection/trace-archival/presentation-emission (AP.md:1311–1344, 1278; RF-19:322–326; AP_ORCHESTRATOR:180–188; ARTIFACT_LIFECYCLE:70–76; RF-01:96–99; ADR-0006:97–100); limited by §9 Git-authority, RF-02 no-material-substitution, RF-06, §19. Missing: one consolidated citable boundary → planned RF-02 clarification.
3. **Internal delegation is Worker-side only today** (AP.md:621–626, 1252–1254; PROMPT_CONTRACTS:845/949; ADR-0011:40–43). Missing for Orchestrator-operated dispatch: delivery-mechanism sentence, parent-context disqualifier, recording-rule scope, operational guidance. Nothing in current text forbids dispatch (session target is delivery-neutral, AP.md:650–656, 703–706) — but nothing permits-and-structures it either.
4. **Recording rule:** Worker-side field stays Worker-scoped (`not-used` unless that Worker delegates); Orchestrator dispatch recorded via session target + coordinates + profile + routing record; no composed new field (see §D.6).
5. **Functional language suffices; no adapter layer** (AP.md:591–593; ADR-0008 rejected vendor-specific session identifiers).
6. **Anti-parent-context sentences today:** AP.md:663–666, 680, 816–817; PROMPT_CONTRACTS:2125–2127; ADR-0008:142–147; RF-05:134–135. Gap: they address Worker-run-internal agents and reused sessions, not the Orchestrator-dispatch configuration → one disqualifier sentence.
7. **Isolation never establishes independence** — ADR-0017:59; AP.md:2500–2501; PEP:1234–1254.
8. **Minimum audit input set already owned** — AP.md:393–399; PROMPT_CONTRACTS:2115–2120; INTUITION.md only cites it.
9. **Yes** — any mutation of the sole normative protocol triggers the fresh independent route even when purely descriptive (AP.md:396–399; 2396–2399).
10. **Owners without a new RF:** dual-mode → RF-06+RF-02; intuition boundary → RF-02+RF-06(+RF-01); subagent delivery → RF-02+RF-03(+§3); audit freshness → RF-05; compact synthesis → §17 (owned); signaling → RF-02+INTEGRATION (owned); auto-trace → RF-19 (owned, unchanged).
11. **New RF family not justified** — no gap proven; would duplicate ADR-0011/0017.
12. **`INTUITION.md`:** explanatory projection (advisory quick-rules), durable lifecycle class (same row family as README/FAQ/GLOSSARY), discovered via README reading order + AP.md Related Documents; consumer sees `.ap/INTUITION.md` after a pin update; never in the managed block.
13. **Two ADRs** — decisions are independently acceptable (dispatch/independence vs boundary/synthesis/projection), each narrow, matching the handout's numbering without adopting its normative claims; one ADR would bloat and mix independent acceptance scopes.
14. **Must change:** AP_ORCHESTRATOR, AP_WORKER (minimal), PROMPT_CONTRACTS (sentence), README, ARTIFACT_LIFECYCLE, GLOSSARY, CHANGELOG, adr README, 2 ADRs. **May remain consistent by a reading-order sentence:** FAQ, INTEGRATION, UPDATING (verified).
15. **Signaling home:** INTEGRATION.md's existing optional project-owned presentation profile (its "marks" language already covers it, INTEGRATION.md:117–119); INTUITION.md pointer only; never PROMPT_CONTRACTS fields; never an authority gate.
16. **Smallest density change:** one advisory PEP pattern; §17/§7/ADR-0017 already own the discipline; no gates deleted.
17. **No new PROMPT_CONTRACTS field/record necessary** — dispatch is expressible via session target + coordinates + profile + routing record; only the scope of the existing delegation row needs one clarifying sentence (same disposition pattern as ADR-0018).
18. **Yes** — ADR-0017 already authorizes compact grants; Intuitive Mode reduces to one boundary clarification plus operational/advisory guidance, not a new cost mechanism.
19. **Auto-write is already lawful RF-19 staging + archival duty** (AP.md:322–326; AP_ORCHESTRATOR:180–188; ARTIFACT_LIFECYCLE:70–76; live precedent: the staged `05/01_planning_00.md`); no AP.md/ARTIFACT_LIFECYCLE semantic change; Workers still never self-archive; Era 05 spelling stays trace-local; consumers keep their grammars; Meta untouched by this whole.
20. **Pins retain meaning** — all changes prospective; INTUITION.md additive; AP.md field semantics unchanged; adoption is a separate pin-update whole.
21. **No managed-block change**; README reading-order mention only (presumption confirmed against INTEGRATION.md:44–61).
22. **No executable surface can observe these properties and none should be added** (AP.md:237–240; ADR-0018:74–78; tool inspected — no prompt/subagent surface).
23. **ADR-0015 requires nothing beyond documentation-first proportional validation** — the §H matrix is the validation; no suite, no replacement mechanism (ADR-0015:36–51).

# Candidate invariants (§12) — verdicts

All thirteen tested against current evidence: **adopt with refinements.** #1–#7, #9–#13 hold as stated (evidence cited above). #8 refined to: trace *staging* at the activated destination is lawful at dispatch; *archival* of the prompt+report pair occurs only after the report exists; Workers never self-archive. #12 is maintained by the docs-only posture (no enforcement is claimed beyond normative-operational force). None reverses a §5 lock; Locks 1–3 are encoded, not softened.

```text
Resolved Execution Issues / Near-Misses: near-miss — stale /home/agile/Projects/ap/.git/REBASE_HEAD (573975c…) present with no rebase-merge/rebase-apply/sequencer directories, clean tree, and all sibling worktree branches verified merged into origin/main; cause: leftover state file from a completed rebase; resolution: classified as stale leftover, not an active operation, no action taken; residual risk: future restoration gates should check sequencer directories, not REBASE_HEAD alone.
Pre-Existing Failure Classification: none
```

**No-mutation confirmation:** No file, repository, ledger, Meta artifact, pin, public ref, environment, credential, host, NUC, or production state was changed. All commands were read-only Git/filesystem inspection (`GIT_OPTIONAL_LOCKS=0` where relevant) plus three credential-free `git ls-remote` readbacks of the canonical refs. No subagent was spawned; Native Plan Mode was observed active and honored throughout; nothing was written to AP, FrameNest, or Meta, and the plan is delivered in this report only.

**Smallest recommended next step:** Orchestrator reviews this plan with Michal; if accepted, issue one complete fresh Implementation Worker prompt with `Native planning mode: not-used`, `Worker session target: fresh-worker-session`, and the §E allowlist and forbidden paths exactly as specified.

**Authority statement:** Plan approval would still grant no implementation authority. Implementation, publication, consumer adoption, and closure each require their own explicit, separately authorized prompts and gates. All Worker 01 exchange 01 planning authority expires at this terminal report.
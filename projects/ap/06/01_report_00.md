### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ap-followable-spine-and-restatement-conversion
Worker session ordinal: 01
Worker exchange ordinal: 01
Task identity: AP-FOLLOWABLE-SPINE-PLAN-01
Standard terminal status: PASS
Phase-qualified result: planning-PASS
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: this Worker's read-only planning authority expired at the submission of this terminal report; no implementation, repository mutation, Git write, publication, Meta write, FrameNest mutation, pin update, or closure authority was granted or exercised; implementation requires a new complete ORCHESTRATOR prompt with `Native planning mode: not-used`
```

**Planning mode**: Native Plan Mode was active for this entire exchange; every action was read-only inspection. No second planning cycle is started; escalation returns to the Orchestrator.

**Evidence trail (all verified this session)**: gates passed — workdir `/home/agile/Projects/ap`; branch `feat/subagent-lifecycle-and-intuitive-mode`; HEAD `eb3507bd1753e337ca7db92bb2da6cf7ec133071`; `git status --porcelain` empty; credential-free `git ls-remote` confirms public `main` equals local HEAD. Read completely: `AP.md` (2,648 lines), `PROMPT_CONTRACTS.md` (2,234), `AP_ORCHESTRATOR.md` (497), `AP_WORKER.md` (307), `README.md`, `INTEGRATION.md`, `ARTIFACT_LIFECYCLE.md`, `INTUITION.md` (142 — budget intact), `UPDATING.md`, `CHANGELOG.md`, `FAQ.md`, `GLOSSARY.md`; skimmed per contract: `PROMPT_ENGINEERING_PATTERNS.md` (index + P11 + global anti-patterns), `INFOSEC.md` (structure, activation-only); ADRs 0004–0020 index plus bodies 0011, 0013, 0015, 0017, 0018, 0019, 0020. Context evidence: `/home/agile/meta/projects/ap/06/00_notes.md`, `05/05_closure.md`, `05/05_report_00.md`, `/home/agile/Projects/framenest/AGENTS.md` (read-only; no other FrameNest path opened). Restatement inventory grounded by direct grep. No contradiction with the §4 locked constraints was found; no semantic-owner contradiction survived analysis; no BLOCKED condition applies.

---

## 1. Spine specification (deliverable 1)

**Owner and location.** A new subsection `### Per-Role Minimum-Reading Spine` inside AP.md's existing "Semantic Authority and Artifact Relationships" block, placed immediately after the paragraph that assigns relationships to named files (currently ending ~line 50) and before the "Canonical Semantic-Owner Map" subsection. Rationale: the spine is the consumer-facing answer to "what must I read", the direct companion of the ownership declaration it points into; this satisfies the locked constraint that the spine is owned in AP.md (ADR-0013) and the meta-era finding that no normative per-role minimum reading exists anywhere in the corpus (only three non-normative file-name lists: README, INTEGRATION managed-block description, FrameNest managed block).

**Wording approach.** One normative lead sentence + one compact three-row table + three binding sentences, ~35–50 added lines total. Lead sentence: "Before a role's first exchange in a logical whole, the role's spine rows below are its required minimum reading." Binding sentences: (a) the spine is a floor, never a ceiling — prompt-named required reading and activated surfaces add to it and are unaffected; (b) `AP_ORCHESTRATOR.md`, `AP_WORKER.md`, `INTUITION.md`, and every other projection may point to the spine and never own it; (c) ownership of the spine is this section, per the semantic-owner map.

**Spine contents (exact anchors):**

| Role | Required AP.md anchors | Required projections | Reference-on-demand |
|---|---|---|---|
| COOPERATOR | intro; Semantic Authority table; §2 Roles; RF-01; "Cooperator Participation and Deterministic Closure"; §16 | project root `AGENTS.md` | FAQ.md; all other surfaces |
| ORCHESTRATOR | §2; §3 through Plan-to-Execution Gate; Finite Convergence Contract (Planning Budget and Expiry; Implementation Authority; Acceptance, Correction, and Escalation; Phase-Qualified Results); §5; §6 (lifecycle, evidence ladder, provider-neutral routing); §7; §13; §15; §17; §19 (skim); RF-01–RF-05, RF-07, RF-08, RF-14, RF-15, RF-17, RF-19 capsules | `AP_ORCHESTRATOR.md`; `PROMPT_CONTRACTS.md` (prompt issuance + activated annexes); project root `AGENTS.md` | `PROMPT_ENGINEERING_PATTERNS.md` (advisory); `INFOSEC.md` (only when activated); `ARTIFACT_LIFECYCLE.md` (artifact work); `INTEGRATION.md`/`UPDATING.md` (integration/update tasks); `INTUITION.md` (optional, never required); `FAQ.md`/`GLOSSARY.md` |
| WORKER | §2; §3 (Worker Session Target + profiles); §5; §8; §9; §10; §12; §17; §18; RF-03, RF-06, RF-07, RF-12, RF-18, RF-19 capsules | `AP_WORKER.md`; `PROMPT_CONTRACTS.md` (report header + activated annexes); project root `AGENTS.md` | everything else, plus any prompt-named required reading |

Required-vs-reference principle encoded in the table's third column: projections outside column three are never required reading for a role unless the current prompt names them or their activation trigger fires (INFOSEC). README.md may gain one pointer row to the spine (pointer-only; explanatory projection; no ownership). This closes the "fresh participant has no authoritative answer to what must I read before exchange 01" gap; it is field-testable (deliverable 7, check 2).

## 2. Detectability classification method (deliverable 2)

**Home.** New AP.md subsection `### Rule Detectability Classes and Detection-Surface Requirement`, placed immediately after "Canonical Semantic-Owner Map". AP.md owns the class definitions and the forward-looking requirement only; the full per-item corpus audit lives in the new ADR's appendix as a historical record (relationship: historical; not a second owner). This design follows the locked constraints: no new RF family, no mechanical validator, class-2 rules never restated.

**Class definitions.**
- **Class 1 — artifact-detectable**: a violation leaves evidence in a protocol-named report, record, repository, or trace artifact (report field, structural record, commit/diff, ledger entry, archived prompt/report pair, public ref).
- **Class 2 — behavioral-normative**: binding conduct whose violation is observable only in behavior at a protocol boundary; no defined artifact would reveal it. Kept in its single owner; never restated in another file; never mechanically enforced (ADR-0015).
- **Class 3 — undetectable-and-unenforced**: neither artifact evidence nor observable conduct at any AP boundary could reveal violation. Demoted to advisory (explicitly labelled) or deleted, per-item.

**Decision procedure (per normative sentence).**
1. Is it normative (must/never/only/prohibited/required semantics)? Definitions, examples, explanations, and already-declared advisory text are out of scope.
2. If violated, does a protocol-named artifact contain the evidence? → Class 1.
3. If not, could a participant observe the violation in conduct and report it (report, notes file, escalation)? → Class 2.
4. Otherwise → Class 3. Modality (should/may) is evidence toward advisory but never dispositive; the detection question decides.

**Coverage route (fixed order, one pass each):** AP.md (preamble + artifact relationships → new spine/detectability subsections → owner map → RF-01–RF-19 capsules → Finite Convergence Contract → §1–§19 in order) → `PROMPT_CONTRACTS.md` (expect class 1 / structural) → `AP_ORCHESTRATOR.md`, `AP_WORKER.md`, `ARTIFACT_LIFECYCLE.md`, `INTEGRATION.md`, `UPDATING.md` → `README.md`, `FAQ.md`, `GLOSSARY.md` → `PROMPT_ENGINEERING_PATTERNS.md`, `INTUITION.md`, `INFOSEC.md` (advisory by declaration; reclassify only sentences that read normative without an owner link).

**Disposition record format (per class-3 item, in ADR-0021 Appendix A):**

```text
ID: D-NN
Surface and section: <file, section/lines>
Rule excerpt (≤25 words): <quote>
Current class: 3
Disposition: demote-to-advisory | delete | merge-into-owner
Reason: <one line — why no detection surface>
Exact edit: <target wording change>
```

Plus per-surface summary counts (class 1/2/3 items). Class-1/2 full tables also live in Appendix A; AP.md never carries the corpus table.

**Worked examples (actual corpus, ≥1 per class):**
1. Class 1 — RF-19 coordinate echo (AP.md RF-19; PROMPT_CONTRACTS coordinate block): a missing/malformed echo is visible in the report artifact itself.
2. Class 1 — §9 "Workers must not use `git add .` … unless the task names that operation exactly": violation visible in Git history/diff.
3. Class 2 — §7 "ask one strategic or security-sensitive question at a time": binding conduct; no defined artifact reveals violation; kept in its single owner.
4. Class 2 — RF-01 "the Cooperator remains meaningfully informed": conduct-binding, no artifact proves informedness.
5. Class 3 → demote-to-advisory — §6 "Reasoning should be chosen separately for preflight, implementation, diagnostic closeout, and independent audit": should-level guidance, no detection surface, no conduct-binding force.
6. Motivating case (resolved, no pending item): the era-05 emoji-signaling aspiration. Verified by grep: no universal emoji rule remains; only non-universal declarative statements exist (AP.md §19:2548; INTEGRATION.md:102; INTUITION.md:108,124; PROMPT_CONTRACTS.md:656). Recorded as the method's origin, not a disposition.

**Force-preservation guard (mandatory).** Classification never demotes or deletes a safety-anchoring rule merely because its violation is hard to observe. For every class-3 candidate the implementation must first ask whether a detection surface can be *added* (promote to class 1 by naming an artifact); demotion is the fallback. If a demotion would weaken safety, the implementation flags it and stops per §18 of the prompt instead of proceeding.

## 3. Restatement inventory method and conversion rule (deliverable 3)

**Inventory method.**
1. Per rule family / named rule, build a seed-phrase set: canonical owner phrase + 3–6 paraphrase seeds (worked: planning budget → "one initial", "targeted revision", "second automatic", "plan-only cycle", `NEEDS_ORCHESTRATOR_DECISION`).
2. Grep all live `.md` surfaces; exclude from conversion scope: `docs/adr/` bodies, `CHANGELOG.md` history, and the `docs/adr/README.md` index (historical-frozen under their governing pins; RF-19's rule that historical artifacts are not retroactively rewritten; locked constraint).
3. Adjudicate each hit: **owner** | **structural echo** (PROMPT_CONTRACTS field/allowed-value spellings — legitimate) | **pointer** (already compliant) | **in-file digest** (§19-style summaries within AP.md — same owner, acceptable) | **paraphrase restatement** (convert).
4. Priority = number of live paraphrase surfaces × observed confusion risk (meta-era findings ledger).

**Conversion rule (normative; owned in AP.md inside the detectability subsection, one sentence):** "A paraphrase of a rule owned elsewhere is converted to a pointer plus at most one orientation sentence naming the owner and when the rule applies; the paraphrase does not survive as an independent statement of the rule." Conversion preserves modality, scope, and exception carve-outs exactly — it is re-homing, never weakening. Structural echoes in PROMPT_CONTRACTS are kept (they are the legitimate structural projection, not paraphrases).

**Verification: old-surface → single-owner map** (row per conversion in ADR-0021 Appendix B; each row: converted surface → owner anchor → modality/scope/carve-out comparison → reviewer check). Application of a rule in context (e.g., AP.md:1786 "does not automatically require … a new plan-only cycle") is not a restatement cycle + at most one targeted revision") — owner: AP.md "Planning Budget and Expiry" (379–404). Live surfaces to convert: `PROMPT_CONTRACTS.md` 730–734 and 756–759 (keep structural field block 716–728; convert normative paraphrase sentences to pointer + orientation); `AP_ORCHESTRATOR.md` 83 (decision-table row reworded to cite owner), 127–128 (finite-convergence rows trimmed to pointer-style transitions with owner link), 236 (repair boundary trimmed to structural reference), 255–258 ("Default to one initial planning cycle…" → pointer + orientation), 485 (stop-condition mention → pointer); `AP_WORKER.md` 42–44 (→ pointer + orientation) and 293 (stop-list entry → pointer); `FAQ.md` 100–107 (re-anchor to owner with orientation sentence); `GLOSSARY.md` 44 ("Planning Budget" row shrinks to orientation + link); `PROMPT_ENGINEERING_PATTERNS.md` P11 fragment 374–387 ("no second automatic revision" paraphrase line replaced by owner citation; structural template values by reference). `AP.md` 812–814 is already a pointer (no change); AP.md:809/727 `Maximum plan-only cycles: 1` are structural echoes (keep); §19 bullet 2566 stays as in-file digest. **ADR-0011:54–58 and ADR-0013:28–31 are NOT converted** — historical-frozen; the new ADR records that historical restatements remain interpretable under their governing pins.
2. **Freshness ≠ independence** — owner RF-05. Convert: `PROMPT_CONTRACTS.md` 369, `AP_WORKER.md` 48, `FAQ.md` 115, `GLOSSARY.md` 21 (orientation + link). AP.md 155/417/730 are owner-scope/in-file (keep).
3. **Worker never emits closure signal** — owner AP.md "Closure Signal". Convert: `AP_WORKER.md` 278 (orientation + link); `PROMPT_CONTRACTS.md` 224–226 keeps field values, trims the paraphrase sentence.
4. **"Omitted permission is not implied permission"** — owner AP.md §5:982. Convert: `AP_ORCHESTRATOR.md` 403 (align to pointer; note current wording drift "not permission" vs owner "not implied permission"), `PROMPT_CONTRACTS.md` 306 (orientation + link).
5. **Emoji/presentation non-universality** — surfaces already declarative (INTUITION 108/124, INTEGRATION 102, PROMPT_CONTRACTS 656): pointer-polish only; lowest priority.

Generic instruction for the implementation: re-run the seed search across all named rules; convert any additional ≥2-surface live paraphrase found; anything ambiguous goes into the terminal report for Orchestrator disposition — never silently converted (the "no silent weakening" gate).

## 4. `00_notes.md` placement decision (deliverable 4)

**Decision: two homes, one per facet, plus the not-universal-grammar statement in both.**
1. **Operational home (primary): `AP_ORCHESTRATOR.md`** — new short section "Per-Whole Orchestrator Notes (`00_notes.md`)": fixed name `00_notes.md` created beside the whole's handout at open; Orchestrator-only author (Workers never write it); append-only, dated entries; superseded facts move to Git history; final entry at closure, then frozen as evidence; content = restoration verification, per-exchange Worker-claim review results, Cooperator decisions verbatim, freezes/deviations, failure classifications, artifact pointers (paths + SHAs); public-safe default; notes are evidence, never authority.
2. **Inventory home: `ARTIFACT_LIFECYCLE.md`** — one row/subsection classifying the notes file: operational lifecycle artifact; consumer = Orchestrator, auditable by the Cooperator; retention = life of the whole's trace, then frozen historical evidence; cleanup owner = Orchestrator under Cooperator authority.
3. **Not-universal statement (in both homes):** "The `00_notes.md` filename is a local AP-run convention, not a universal AP field, never a task-authority gate, and never a required universal artifact; its absence weakens no AP rule" — anchored to RF-19's existing doctrine ("local grammar is never universal AP meaning") and RF-14 (every artifact declares relationship and lifecycle; this convention declares its own).

**Alternatives considered and rejected:** owning it as a normative rule in AP.md — rejected: it is an AP-run practice convention, not universal protocol; universalizing a filename contradicts the corpus's own doctrine (INTEGRATION.md:100–102) and the Cooperator directive that this is "not a Meta-repository change but a convention carried by AP-run wholes" (05_report_00.md §6); the practiced exemplar already lives exactly this way (06/00_notes.md header). RF-19 companion/trace-grammar extension — rejected: RF-19's standard grammar covers prompt/report/interruption pairs with contiguous ordinals; folding in a notes file either changes interoperable grammar (compatibility lock broken) or creates a never-interoperating special case. FAQ-only — insufficient: FAQ is explanatory; the convention needs an operational how plus a lifecycle classification. Retroactive notes for closed wholes — out of scope; era-05 continuity is already served (05_report_00.md §6 open question answered: no).

## 5. Detection-surface rule wording and §19 reconciliation (deliverable 5)

**Location:** AP.md, the new `### Rule Detectability Classes and Detection-Surface Requirement` subsection (deliverable 2's home).

**Draft wording for implementation:** "Every newly added or materially revised normative rule must name its detection surface — the report, record, artifact, or observable conduct in which its violation becomes visible — and its class: artifact-detectable, behavioral-normative, or advisory. A rule with no detection surface is advisory, or it is not added. A behavioral-normative rule lives only in its single owner and is never restated in another surface." (The emoji lesson formalized: the era-05 emoji rule was written, believed, and silently dropped because it had no detection surface — 05_report_00.md §4; 06/00_notes.md finding A.)

**§19 reconciliation:** §19 remains AP.md's in-file digest of rejected patterns — same owner file, therefore not a second surface; the digest convention is explicitly stated once in the new subsection so future implementers do not mistake §19 bullets for restatement targets. One new bullet is added to §19: "- adding a normative rule without naming its detection surface;". No other §19 change; the existing emoji bullet (line 2548) stays and is cited by ADR-0021 as the motivating case.

## 6. Rollout and staging order (deliverable 6)

**Commit order** (single later implementation session; continues on `feat/subagent-lifecycle-and-intuitive-mode` from `eb3507bd…`; canonical-checkout topology):
- **C1 — "docs: add role reading spine and rule detectability classes"**: AP.md only — spine subsection; detectability classes + detection-surface subsection; §19 one bullet; any AP.md class-3 demotions emerging from the coverage pass (each recorded per-item). ~40–75 added lines, demotions netted where practical.
- **C2 — "docs: convert restatements to pointers and formalize notes convention"**: `PROMPT_CONTRACTS.md`, `AP_ORCHESTRATOR.md`, `AP_WORKER.md`, `FAQ.md`, `GLOSSARY.md`, `PROMPT_ENGINEERING_PATTERNS.md` (P11), `ARTIFACT_LIFECYCLE.md` (notes row), `README.md` (one pointer row), `INTUITION.md` (pointer-status sentence only if the ≤200-line budget holds; otherwise untouched). Each edit follows the old-surface→owner map; no modality change.
- **C3 — "docs: record spine and detectability decision (ADR-0021)"**: `docs/adr/0021-followable-spine-and-restatement-conversion.md` (body incl. Appendices A/B), `docs/adr/README.md` index row, `CHANGELOG.md` Unreleased entry. Revert order if needed: C3 → C2 → C1 (independent reverts).

**Complexity budget (committed):** new RF families 0; new PROMPT_CONTRACTS fields/records 0; new roles/profiles/phases/universal fields 0; executable `ap`/`ap.project.conf`/schema/managed-block changes 0; new files 1 (ADR-0021); modified live files ≤11; INTUITION.md unchanged unless the pointer sentence fits within 142→≤200 lines; Meta and FrameNest: 0 changes.

**Risk tier: E2 (cross-cutting reversible).** Basis: multiple layers (sole semantic owner + up to 10 projections), user-visible compatibility surface for pinned consumers (meaning preserved; wording changes), moderate uncertainty (classification judgment calls), fully reversible docs-only mutation; no security boundary, durable data, credential, production, destructive, or broad-impact trigger (§6 E2 row). E1 is too low (cross-file normative semantics change); E3's triggers are absent.

**Validation ladder (docs-only candidate):** inspection and provenance: required (`git status/diff/log`, baseline equality `eb3507bd…`); existing focused tests: none (ADR-0015 — no suite exists; none may be created); affected tests: none — the validation method is documentation review: (a) full-diff semantic review against this plan; (b) link/path inspection (every new pointer resolves; anchors exist); (c) old-surface→owner map completeness; (d) seed-phrase grep re-run showing paraphrases reduced to pointers; (e) manual ownership review — no new normative-looking sentence in a non-owner file without an owner link (a review step, never a mechanical gate). New causal regression named: the three §1 risks with their checks (deliverable 9, N2/N1/N3). Broad or full suite: not-used. Runtime/testbed: not-used. Repeated-gate: broad gate once per materially changed candidate; narrow diff checks before re-broadening.

**Fresh independent acceptance (required, scheduled):** the route changes the sole normative protocol, so fresh independent acceptance is mandatory (Finite Convergence Contract "Acceptance, Correction, and Escalation"; §15). Route: `fresh-worker-session`, Worker session ordinal 02, exchange 01, receiving the exact candidate commit, this plan as fixed basis, and the acceptance matrix (deliverable 9); verifies controls by direct repository evidence. Then the Cooperator publication gate: explicit Cooperator authorization → publication Worker (one ordinary non-force push) → credential-free public readback — the exact era-05 gate chain (05_closure.md §3), staged here, executed only in the implementation whole. No Meta Git commit and no publication occur inside the planning whole; nothing in this plan mutates anything.

**Rollback posture:** docs-only; per-commit `git revert` (C3→C2→C1); no data, runtime, consumer, or migration state to undo; if a conversion is found post-acceptance to weaken a rule, revert the affected commit and record the finding as ledger evidence. Consumer rollback, if ever needed after adoption, follows UPDATING.md's gitlink move — a separate whole.

## 7. Adopted-and-testable definition + FrameNest field-test script (deliverable 7)

**Definition.** A new AP version is **adopted** for a consuming project when: (a) the consumer's `.ap` gitlink was moved to the exact new AP commit through the explicit UPDATING.md route (`ap update --check` → `ap update --apply` → `ap doctor --candidate` → staged gitlink → strict `ap doctor` → one reviewable commit); (b) the managed `AGENTS.md` block, `ap.project.conf`, and project-local rules required no change (no migration); (c) the Cooperator's selection is recorded in the consumer's own trace. The adoption is **testable** when each field-test check below is demonstrable from durable artifacts (notes file, Worker report, prompt text) produced under the adopted pin, without modifying AP or the consumer's rules. **Adopted and testable = (a)+(b)+(c) and all field-test checks observable.** This definition serves the separate, downstream FrameNest pin-adoption whole (`.ap` gitlink `9c5cc44…` → new tip; FrameNest upgrade-ledger entry stays untouched; FrameNest product freeze `472553ca…` unrelated). Stated in ADR-0021; owned semantically by RF-15/RF-05 as applied to consumers — no new AP rule is needed for it.

**FrameNest field-test script (numbered, plain language, non-programmer executable; Michal runs it with one fresh Orchestrator session after the separate pin-adoption whole):**
1. Open a fresh Orchestrator chat in FrameNest and paste the standard resume seed (the non-normative example in AP_ORCHESTRATOR.md "Continuation Bootstrap" suffices).
2. Ask: "What must you read before the first exchange in a new whole?" — Expected: one short list matching the ORCHESTRATOR spine (named AP.md sections + its handbook + prompt contracts + project `AGENTS.md`), not "read everything" and not a shrug.
3. Let it finish read-only restoration; confirm it proposes exactly one bounded next logical whole and asks Michal to select it (Continuation Bootstrap Stage 2).
4. After selection, confirm it opens/creates `00_notes.md` in the whole's trace directory beside the handout, dated, with an entry recording the selected whole.
5. Have it issue one real Worker task; confirm the prompt names the whole's coordinates and required reading matching the WORKER spine.
6. When the Worker report returns, confirm it begins `### Report for ORCHESTRATOR_CHAT` and echoes the prompt's three coordinates (whole identity, session `NN`, exchange `NN`).
7. Confirm the notes file gained a dated entry recording the Worker-claim review.
8. Score PASS if checks 2, 3, 4, 6, 7 hold; any failure is recorded in `00_notes.md` as a field observation and becomes upgrade-ledgertable* rather than anecdotal.

## 8. New ADR outline + CHANGELOG entry outline (deliverable 8)

**ADR-0021** — `docs/adr/0021-followable-spine-and-restatement-conversion.md`, title "Followable spine, rule detectability, and restatement-to-pointer conversion", Status: Accepted (written at implementation, matching the ADR-0019/0020 repo practice). Sections: **Context** (corpus ≈11,800 Markdown lines at `eb3507bd…`; normative-weight collapse — ~9,000 lines of live surfaces all look equally mandatory, so participants silently triage; the emoji precedent: a written rule dropped with no consequence because it had no detection surface; one-rule-eight-homes planning-budget instance; no normative per-role minimum reading; era-06 findings ledger as evidence); **Decision** (the six elements: spine in AP.md; three detectability classes + detection-surface rule; restatement→pointer conversion under one-rule-one-home; `00_notes.md` convention as an AP-run projection convention with the not-universal statement; §19 digest bullet; adopted-and-testable definition for downstream consumer field tests); **Semantic Ownership and Projections** (AP.md owns spine + classes + rule; conversions live in the owning projections; the ADR carries Appendices A/B as historical audit records); **Compatibility** (prospective; consumer pins unchanged; managed block, schema, `ap` unchanged; historical ADR bodies and pins not rewritten); **Consequences**; **Relationship to Earlier Decisions** (ADR-0013 ownership; ADR-0015 documentation-first; ADR-0017/0018/0019/0020 as extension precedents); **Rejected Alternatives** (deliverable 10); **Appendix A** — per-item detectability classification tables + class-3 dispositions (deliverable 2 format); **Appendix B** — old-surface → single-owner conversion map (deliverable 3). `docs/adr/README.md`: one index row.

**CHANGELOG.md Unreleased entry outline** (one bullet, house style): "Added a per-role minimum-reading spine owned in `AP.md`; defined three rule-detectability classes (artifact-detectable, behavioral-normative, undetectable-and-unenforced) with a detection-surface requirement for newly added normative rules; converted cross-surface restatements of owned rules to pointers with one orientation sentence (planning budget, freshness/independence, closure signal, omitted permission, and further inventoried instances); formalized the AP-run per-whole Orchestrator notes convention (`00_notes.md` — local grammar, never a universal field) in the Orchestrator handbook and the artifact lifecycle projection; and defined adopted-and-testable criteria for consumer pin adoption. `AP.md` remains the sole semantic owner. No new RF family, field, record, executable `ap`, schema, managed-block, Meta, or FrameNest mutation, and no mechanical validation. Recorded by [ADR-0021]. Existing consumer pins retain their original meaning; consumer adoption and logical-whole closure remain separate."

## 9. Acceptance matrix for the later implementation (deliverable 9)

**Fixed candidate basis:** the exact stacked implementation tip (C1–C3 as one candidate); baseline `eb3507bd1753e337ca7db92bb2da6cf7ec133071`; this planning report as the accepted plan; ADR-0021 Appendices A/B as the fixed review basis.

**Positive controls (check → expected evidence):**
- **P1** Spine present in AP.md, one row per role, with exact section/RF anchors → all anchors resolve via link inspection.
- **P2** Detection-surface rule present in the detectability subsection; §19 carries the new digest bullet → diff inspection.
- **P3** Planning budget has exactly one normative home → seed grep returns only owner, structural echoes, pointers, in-file digests on live surfaces; every converted surface holds pointer + ≤1 orientation sentence.
- **P4** `00_notes.md` convention present in `AP_ORCHESTRATOR.md` + `ARTIFACT_LIFECYCLE.md` row, each carrying the not-universal-grammar sentence → diff inspection.
- **P5** Classification tables complete in ADR-0021 Appendix A: every covered surface passed; every class-3 item has a disposition; the worked examples (≥1 per class) reproduce → appendix review.
- **P6** ADR-0021 + index row + CHANGELOG entry present and consistent with the actual diff → diff inspection.
- **P7** Old-surface→owner map row exists for every conversion in the diff → Appendix B completeness check.

**Negative controls (named regression risks from §1 → checks):**
- **N1 (second semantic owner)** — every new/changed normative sentence in a non-owner file carries an explicit owner link; no handbook/projection/FAQ/GLOSSARY/INTUITION sentence states a rule without pointing to AP.md → manual ownership review of the full diff (documentation-first; no mechanical gate claimed).
- **N2 (silently weakened normative rule)** — sampled conversions (minimum: all six planning-budget surfaces, freshness, closure-signal, omitted-permission) compared against owners for modality (must/never/only), scope, and exception carve-outs — identical force; class-3 guard (deliverable 2) applied → conversion sampling by the fresh independent acceptance Worker.
- **N3 (broken consumer compatibility)** — `git diff` shows zero changes to managed-block-generating content, `ap`, `ap.project.conf`, FrameNest paths, and historical ADR bodies (0011, 0013 untouched); CHANGELOG gains only the Unreleased entry → exact path diff inspection.
- **N4 (mechanical validator creep)** — diff contains only `.md` changes; no script, test, CI config, or executable change → `git diff --stat` review (ADR-0015 lock).
- **N5 (fourth role / universal field)** — no new role, profile, phase, universal field, or required filename; the `00_notes.md` statements contain the not-universal qualifier → diff + wording inspection.
- **N6 (silent demotion)** — every class-3 disposition is demote-to-advisory/delete/merge with a recorded reason; no safety-adjacent rule demoted without a recorded detection-surface-promotion attempt → Appendix A review.
- **N7** — `INTUITION.md` ≤200 lines if touched, else untouched → `wc -l`.
- **N8 (stopping-condition compliance)** — the implementation stops and escalates rather than silently resolving any owner contradiction discovered during execution → implementation report review.

**Acceptance independence:** fresh-worker-session acceptance Worker, session ordinal 02 (per deliverable 6); `Acceptance independence: required-fresh-independent`; the implementation Worker cannot self-certify (RF-05; scoped-vs-full boundary unchanged).

## 10. Explicitly rejected alternatives (deliverable 10)

1. **Spine outside AP.md** (README/INTEGRATION/INTUITION-owned): rejected — violates ADR-0013 sole-ownership and locked constraint 1; the meta-era notes finding B states it directly: a spine owned outside AP.md becomes exactly the second-owner ADR-0013 forbids; INTUITION.md is advisory and budget-capped (142/200 lines) and could never host it.
2. **New RF family (RF-20) for the spine or detectability** without need: rejected — the existing "Semantic Authority and Artifact Relationships" area plus the owner map is the natural home; ADR-0017–0020 all extended existing families instead; a 20th family adds surface to the very burden this whole reduces. (Locked constraint: any new family requires explicit justification; none is warranted.)
3. **Deleting behavioral-normative (class-2) rules**: rejected — conduct rules without artifact surfaces are real safety (honesty, one-question-at-a-time, Cooperator informedness); the three-class design keeps them in their single owner instead of dropping them (the two-class idea in the seeds was explicitly corrected to three classes in the findings ledger).
4. **Mechanical validators / test suite / CI for detectability or restatement counting**: rejected — ADR-0015 retired suite enforcement and forbids a replacement conformance mechanism; documentation-first proportional review only; no grep-gate script, no CI.
5. **Managed-block migration or consumer-side change now**: rejected — no migration, no managed-block change, no schema/`ap` change; FrameNest pin adoption is a separate downstream whole; historical pins and ADR bodies are not rewritten.
6. **INTUITION.md growth past its 200-line budget or promotion to required reading**: rejected — pointer-status only; optional; budget intact (142 lines); the spine lives in AP.md.
7. **Rewriting historical ADR-0011/0013 restatement text**: rejected — locked constraint; historical artifacts remain interpretable under their governing pin (RF-19); ADR-0021 records the conversion instead.
8. **Semantic simplification (merge RF families — Option C of the era-05 option space)**: rejected for this whole — the Cooperator selected candidate shape A; Option C remains deferred until field evidence after A.

---

**Remaining Open Questions: none blocking.** All ten §8 deliverables are specified to implementation precision above; the implementation session (recommended `fresh-worker-session`) re-decides with rationale against this plan as the fixed basis. No file was written, no repository mutated, no Git write performed, and nothing published; the only network call was the authorized credential-free `ls-remote`. All authority for this planning exchange is now expired.

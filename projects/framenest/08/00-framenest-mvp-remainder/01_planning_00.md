# WORKER TASK — Implementation Planning (plan-only)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-gallery-card-ai-per-field-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Planner
Phase: Discovery / implementation-planning
Native planning mode: required
Reasoning recommendation: High
Task identity: FRAMENEST-GALLERY-CARD-AI-PER-FIELD-PLAN-01
Task type: bounded read-only implementation planning
Exact baseline: afa0670e26d17b04570ad555ba4f922052507c6c
Independence required: no
Evidence posture: non-independent
Authority renewal: this is a fresh session; there is no prior Worker authority to renew. Plan approval does not grant implementation authority.
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: primary-objective
Routing reopened for: primary-objective
Unchanged axes reopened: none
Ordinary-only trigger: no

## Plan-to-Execution Contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded technical planning of (1) eliminating
  silent last-write-wins canonical PUT /api/media/{id}/metadata from the Gallery
  catalog card quick action 🧠 (handleAnalyzeCatalogCard); (2) aligning the
  catalog card quick action with the per-field AI suggestion flow shipped in
  ADR-0077 (evaluating default approach: 🧠 executes preview/persist-join and
  opens the existing Edit dialog with suggestion proposal strips revealed and
  selected, no auto-PUT; vs inline card strips); (3) preserving strict capability
  gating (analysis.run ∧ metadata.canonical.write; ordinary never sees 🧠); (4)
  confirmation copy and UX status alignment; (5) test impact on
  tests/catalog_card_ai_quick_action.test.js and related suites; (6) docs and
  successor ADR outline. No implementation.
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1
```

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

This prompt grants READ-ONLY planning authority only. It grants no
implementation, no FrameNest repository mutation, no Git writes, no
publication, no deployment, no NUC contact, no provider calls, no production
mutation, and no closure. Planning authority expires at your terminal report.

## Mandatory Reading

In order:

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/00_handout.md`
6. This prompt (self-contained task authority)

Then, at the exact baseline, inspect:

7. `docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md` (especially §10)
8. `docs/adr/0023-manual-first-metadata-and-multi-model-ai-drafts.md`
9. `docs/adr/0020-on-demand-ai-suggestion-review.md`
10. `docs/adr/0067-administrator-companion-review-inbox-and-mutation-trust.md` §5
11. `docs/adr/0062-per-user-media-alias-overlay.md`
12. `docs/adr/0066-administrator-owned-x-automatic-generic-analysis.md`
13. `src/framenest/adapters/api/web/app.js` —
    `identityAllowsCardAiQuickAction`, `cardAiQuickActionEligible`,
    `handleAnalyzeCatalogCard`, `setCardAnalyzeButtonState`,
    `applySavedAiMetadataToCatalogSurfaces`, `handleOpenMetadataWorkspace`,
    `presentInSessionSuggestion`, `refreshMetadataSuggestionList`
14. `src/framenest/adapters/api/web/index.html`
15. `src/framenest/application/media_suggestion.py` (`PreviewImportedMediaSuggestion`) — persist-join (do **not** redesign)
16. `tests/catalog_card_ai_quick_action.test.js`

Evidence-only background (non-authorizing historical trace):

- `/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/08_orchestrator_notes.md`
- Predecessor whole `framenest-ai-suggestions-alias-edit-mvp` (closed at `afa0670e…`).

## Repository Gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Expected HEAD: afa0670e26d17b04570ad555ba4f922052507c6c
Expected tree: b6eafbcdef3a8bcb728498992c003d8ad5e9a447
Expected working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: afa0670e26d17b04570ad555ba4f922052507c6c (verified by ORCHESTRATOR)
Schema head: Alembic 0033 (0033_media_analysis_proposals.py); no 0034_* migration
Working-copy topology: canonical-checkout
Topology rationale: read-only planning against the living public baseline; no candidate worktree
```

If any gate fact differs from the above, STOP and report BLOCKED with exact
observed evidence before any analysis conclusion. Do not classify, repair, or
work around drift yourself. Do not “fix” the informational
`origin/feat/x-meme-browser-companion` ahead-count.

## Goal (one coherent outcome)

Produce a decision-complete, repository-grounded implementation plan for the
logical whole `framenest-gallery-card-ai-per-field-mvp`, frozen at the exact
baseline, and return it as your terminal report. No implementation in this session.

## Accepted Decisions (do not re-litigate)

### Closed predecessors (out of this kebab)

- `framenest-ai-suggestions-alias-edit-mvp` is **closed-by-ORCHESTRATOR** at public `afa0670e…` (schema `0033`, four `companion_mutation`). Ordinary alias Edit, caller overlay display, ordinary/hosted Load, dropdown deduping, and mapped tag buttons are shipped.
- `framenest-companion-brave-testing-resume` is **closed-by-ORCHESTRATOR** at `2aead54…` (persist-join on preview POST is done).

Do not reopen alias Edit, caller overlay, or persist-join. Do not open R4 (companion Settings auto-analysis checkbox), VPS, or Cover Studio.

### Problem statement & Cooperator product direction for this whole

**Current state at baseline `afa0670e…`:**
- Top-right 🧠 on catalog cards is gated by `identityAllowsCardAiQuickAction` (`analysis.run` ∧ `metadata.canonical.write`, incomplete metadata, not movie). Ordinary never sees it. **Keep that gate.**
- Click handler `handleAnalyzeCatalogCard` (~5744): requests confirmation, calls `POST /api/media/{id}/locations/{loc}/ai-suggestion-preview` with `confirm_cloud_upload: true`, and then immediately issues a canonical `PUT /api/media/{id}/metadata` with the suggested title, description, and tags.
- This silent bulk overwrite violates ADR-0023 ("Current manual working copy is never silently overwritten") and was parked in ADR-0077 §10 as known debt.
- In addition, ROADMAP frozen whole “Processed Publish” explicitly states: do not retrofit bulk publish into the individual card action; canonical AI save is not publication.

**Cooperator intent:**
- Align the card 🧠 action with the per-field AI suggestions UX that just shipped in Edit: Analyze produces proposals; promotion is per-field; nothing persists until an explicit Save.
- The card must not dump a whole suggestion into canonical Save.
- Default architecture: 🧠 runs Analyze (persist-joins via the existing preview endpoint) and **opens the existing Edit dialog** with suggestion proposal strips revealed, Load selected, canonical Current form loaded, and NO automatic PUT.
- Alternative: inline card proposal strips (heavier, riskier to gallery layout). The plan must evaluate both and freeze the chosen surface contract.
- Do not invent a second workspace. Do not change the Gallery visual grid beyond 🧠 control behavior. Do not give ordinary `canonical.write`. Do not turn 🧠 into publication.

### Durable-decision tensions you must reconcile

| Source | Tension with Cooperator intent |
|---|---|
| ADR-0023 | Aligns. Current never silently overwritten; 🧠 currently violates this; fix resolves the violation. |
| ADR-0077 §10 | Parked 🧠 as debt. This kebab succeeds §10. |
| ADR-0020 | Keep Analyze explicit and confirmation-gated. |
| ADR-0062 / 0076 | Keep four `companion_mutation`. Ordinary never gets canonical write or 🧠. |
| Premium Gallery invariant | Behaviour defect fix on the 🧠 action; do not restyle the gallery grid. |

Do not edit accepted ADR bodies. The plan should outline a successor note or concise successor ADR (e.g. ADR-0078 or section note on ADR-0077).

### Defaults you may freeze without asking

1. 🧠 remains administrator-only (`analysis.run` ∧ `metadata.canonical.write`). Ordinary never sees 🧠.
2. Default UX: 🧠 confirms cloud upload, invokes the preview/persist-join endpoint, and opens the existing Edit modal with the newly generated suggestion loaded and proposal strips revealed — without saving canonical metadata.
3. No Alembic migration (schema head stays `0033`).
4. Exactly four `companion_mutation` routes in `tailscale_ingress.py` unchanged.
5. R4, VPS, Funnel, Cover Studio, movie-identification redesign, and AP ledger entry are strictly out of scope.

## Plan Must Freeze (decision-complete outputs)

1. **Surface matrix & interaction flow:**
   - Detailed step-by-step flow when administrator clicks 🧠 on a catalog card.
   - Confirmation dialog copy (reflecting that analysis will run and open in the editor for per-field review, NOT auto-save canonical metadata).
   - Analysis execution: endpoint called, busy/pulse state on the card or editor transition, error handling (provider unavailable, network error).
   - Modal opening: transition to `openMetadataEditor` / `handleOpenMetadataWorkspace` with suggestion pre-loaded and strips visible.
   - Comparison with inline-card-strips alternative and why the modal opening (or chosen path) is selected.

2. **Save & state semantics:**
   - Zero automatic `PUT /api/media/{id}/metadata` from 🧠.
   - Persistence happens ONLY when the user clicks **Save** in the Edit dialog.
   - If user dismisses/cancels the Edit dialog, nothing was persisted in canonical metadata (though the generic run remains persisted in `media_analysis_runs` via persist-join).
   - Status announcement on the card / in the modal.

3. **Capability & audience gates:**
   - 🧠 visibility predicate: `identityAllowsCardAiQuickAction` (`analysis.run` ∧ `metadata.canonical.write`).
   - Ordinary identities, unauthenticated users, and hosted companion: 🧠 hidden.
   - Content categories: movie excluded; meme/general included.

4. **Confirmation copy & messaging:**
   - Exact dialog title, body message, confirm label, and dismiss label for the 🧠 action.
   - Elimination of the stale "will replace the current canonical values... last-write-wins" copy.

5. **Test strategy & impacted suites:**
   - `tests/catalog_card_ai_quick_action.test.js`: review all existing assertions that test `handleAnalyzeCatalogCard`, PUT `/api/media/{id}/metadata`, and reflow/dismissal.
   - Detail which tests will be updated to assert the new flow (e.g. no PUT, modal opened with suggestion vs auto-save).
   - Any other affected frontend contract tests (e.g., `tests/gallery_details_playback_handoff.test.js`, `tests/ai_suggestion_alias_edit_flow.test.js`).

6. **Docs & architecture records:**
   - Outline successor ADR / update to ADR-0077 §10 (e.g., ADR-0078 or note on 0077).
   - Living doc alignment: PRODUCT.md, SPEC.md, GALLERY.md if affected.

7. **Out of scope (name explicitly):**
   - R4 companion Settings automatic analysis checkbox.
   - VPS, Funnel, router port forwarding.
   - Cover Studio.
   - Ordinary `analysis.run` or ordinary `metadata.canonical.write`.
   - Fifth `companion_mutation`.
   - Schema `0034`.
   - AP upgrade ledger execution-route observation.

8. **Proposed implementation allowlist & validation ladder:**
   - Exact file paths proposed for modification in the implementation phase.
   - Target commit structure (1–2 clean commits).
   - Validation ladder: `node --test tests/catalog_card_ai_quick_action.test.js` + full JS suite + `./.ap/ap exec` Python tests.

9. **Numbered Cooperator re-test list:**
   - Freeze the numbered list of human-observable checks (1–N) to be performed on the live NUC after publication.

## Execution Route Binding (RF-16)

Python evidence, if needed, goes ONLY through the consumer-declared baseline-bound envelope:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c
./.ap/ap exec --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation <id> [-- <argv>]
```

Never invoke `.venv/bin/python`, `python`, `python3`, or `poetry run`.
Do not reconstruct `.venv`. Isolated-worktree `ap exec --root <worktree>` is a known launch-path miss; classify if hit; do not repair.

JavaScript evidence uses Node’s built-in runner:

```text
node --test tests/<name>.test.js
```

NUC SSH gate is **not activated**. Do not SSH. Do not reconstruct `gpgconf`. Do not `sudo -v`.

## Positive Authority

- Read-only repository inspection at the exact baseline: file reads, grep, glob, `git status/log/show/diff/rev-parse` (no writes).
- Write EXACTLY ONE file if native planning mode permits filesystem writes:
  `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/01_report_00.md`
- If native planning mode forbids filesystem writes, return the complete report in chat (same body) and stop. ORCHESTRATOR archives it.

## Negative Authority (omitted permission is not permission)

- No FrameNest product edits. No staging/commit/push/branch operations.
- No edits to any ADR body, living doc, extension file, server file, test, or Alembic version.
- No NUC contact: no SSH, no `framenest-release`, no sudo.
- No secrets: never inspect or print private keys, environment files, or home-directory fish helpers.
- No network calls beyond the local repository; no provider calls; no browser automation.
- No fifth `companion_mutation`. No ordinary `canonical.write` or `analysis.run`.
- No Alembic `0034` authoring.
- No Max/enhanced mode. No sub-agents or parallel workers. You are one accountable WORKER.

## Validation Ladder

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none (planning; inspect tests as evidence only)
Affected tests: none
New causal regression: none
Broad or full suite: not-used
Runtime or testbed: not-used
Independent acceptance: not-required
```

## Stopping Conditions

Stop and report BLOCKED if: any repository-gate fact drifts; a required decision input is missing; or you find a contradiction that cannot be resolved within this bounded scope.

Otherwise stop when the plan is decision-complete and the report is submitted.

## Report Contract

Terminal report identity:

```text
01_report_00.md
```

Destination (if writing is permitted):

```text
/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/01_report_00.md
```

It begins EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Include, in order:

1. Coordinate echo: `Logical whole identity: framenest-gallery-card-ai-per-field-mvp`, `Worker session ordinal: 01`, `Worker exchange ordinal: 01`.
2. Status: PASS | PARTIAL | BLOCKED.
3. Phase-qualified result: `not-applicable` (planning produces no phase-PASS). `Logical-whole closure: not-closed`.
4. Baseline echo and gate evidence (branch, HEAD, tree, clean tree, submodule pin).
5. Brief capability statement: native planning mode requested vs observed, reasoning requested vs observed, enhanced/maximum mode observed or unknown, context pressure qualitative note.
6. Recon evidence summary with exact `path:line` citations.
7. The frozen plan (all items from "Plan Must Freeze"), each decision with a one-line rationale tied to evidence or a cited accepted decision.
8. Named ADR conflicts and successor ADR / note outline.
9. Proposed implementation changed-path allowlist and validation ladder.
10. Deviations, risks, open questions ("none" explicitly if none). At most one Cooperator question.
11. One smallest next step (expected: ORCHESTRATOR reviews plan, obtains Cooperator approval, issues implementation Worker 02).
12. Exactly one report justification: `new-evidence`.
13. Authority-expiry statement (planning authority expired at submission; no further action without a new ORCHESTRATOR prompt).
14. `Resolved Execution Issues / Near-Misses:` none | details.
15. `Pre-Existing Failure Classification:` none | complete classification.

Professional English.

## Human-Governance Routing

```text
Cooperator visibility: objective, routing, plan approval, later rendered UX acceptance
Human decision points: plan approval (approval-gated); later numbered re-test after public SHA is on the NUC
Deterministic steps inside bounded authority: read-only recon
Brainstorming classification: out-of-scope ideas => future-logical-whole notes in the report
Internal delegation posture: not-used
Accountable Worker: one WORKER (this session)
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/
Trace project key: framenest
Trace logical-whole projection identity: framenest-gallery-card-ai-per-field-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt file pre-staged); Worker writes only the report companion, or returns it in chat for archival
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_00.md
Destination path: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/01_planning_00.md
Archival: wait-for-report
```

## Surface And Model Routing (requested)

```text
Client/surface announcement: Cursor Agent chat; native planning mode required
Recommended client/surface: fresh Worker Agent session
Recommended model: current High-capable Agent (Cooperator-selected High; no Max)
Recommended reasoning: High — UX + capability + Save-semantics alignment
Enhanced/maximum mode: requested off; never infer Max
Automatic model selection: off for this task
Independence requirement: none
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
```

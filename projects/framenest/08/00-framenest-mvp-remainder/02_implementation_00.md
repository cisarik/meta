# WORKER TASK — Implementation (isolated worktree)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-gallery-card-ai-per-field-mvp
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Native planning mode: not-used
Implementation authority: explicit
Reasoning recommendation: High
Task identity: FRAMENEST-GALLERY-CARD-AI-PER-FIELD-IMPL-01
Task type: bounded implementation
Exact baseline: afa0670e26d17b04570ad555ba4f922052507c6c
Independence required: no
Evidence posture: non-independent
Authority renewal: this is a fresh session; planning authority from session 01 expired. This prompt is the sole current grant.
Internal delegation posture: not-used
Accountable Worker: one WORKER
Material phase gate: yes
Changed material axis: mutation-authority-or-side-effect-class
Routing reopened for: mutation-authority-or-side-effect-class
Unchanged axes reopened: none
Ordinary-only trigger: no

```text
Canonical repository identity: https://github.com/cisarik/ap.git
Immutable version identity: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Declared variant: stable
Governing variants in effect: one
Declaration location: project governing rules
Rules from non-governing variants: none
Migration required: no
```

```text
Evidence tier: E2
Evidence tier basis: cross-cutting reversible local change (eliminating last-write-wins auto-PUT from gallery card 🧠, opening Edit workspace with proposal strips, capability check update, surgical docs/ADR). No production, NUC, or schema migration.
Authorized implementation stages: isolated-worktree create → implement allowlisted files → focused tests → 1–2 local commits → terminal report
Combined implementation envelope: allowed
Implementation stage gates: repository gate before mutation; tests green before commit; canonical checkout remains untouched
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: isolated worktree + unpushed commits; discard worktree if BLOCKED before commit
Activated stricter profile: none
Terminal implementation report point: after local commit(s), before any push
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest isolated implementation worktree (this grant)
Declared reversible class: reversible local mutation (worktree files + local commits)
Working-copy topology: isolated-worktree
Topology rationale: keep canonical public main clean; exact-source candidate at the authorized baseline
Irreversible exclusions: secrets, destruction, accounts, public exposure, unrelated owner data, publication, push, NUC, closure, schema migration, .venv reconstruction
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/catalog_card_ai_quick_action.test.js; tests/metadata_alias_edit.test.js; tests/tailscale_identity_frontend.test.js; tests/contract/test_local_web_application.py; tests/contract/test_youtube_creator_taxonomy_frontend.py
Affected tests: the suites above plus non-browser JS suite globs
New causal regression: card 🧠 opens Edit with proposal strips; 0 auto-PUT from card; 0 metadata mutation on cancel; hosted 🧠 hidden; ordinary 🧠 hidden
Broad or full suite: not-used
Runtime or testbed: isolated worktree + declared AP exec deviation below
Independent acceptance: required-separate-fresh-worker
```

This prompt grants implementation only inside the isolated worktree and
allowlist. It grants no push, publication, NUC, provider calls, browser
automation, schema migration, or closure. Authority expires at your terminal
report.

## Source Precedence

1. This prompt (includes the Cooperator-accepted freeze in §Accepted Decisions).
2. Frozen planner artifact
   `/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/01_report_00.md`.
3. Repository at the exact baseline.
4. Accepted ADRs on that baseline. You add ADR-0078; you do not edit ADR
   bodies 0023, 0020, 0062, 0065, 0066, 0067, 0073, 0076, or 0077.

If the repository contradicts this grant, STOP BLOCKED with exact evidence.
Do not self-grant extra paths.

## Mandatory Reading

1. This prompt (self-contained task authority).
2. The frozen planner artifact named above.
3. `/home/agile/Projects/framenest/AGENTS.md`
4. `/home/agile/Projects/framenest/.ap/AP.md`
5. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
6. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`

Then inspect at the baseline, as data: ADR-0077, 0023, 0020, 0062; `app.js`
(`identityAllowsCardAiQuickAction`, `cardAiQuickActionEligible`,
`handleAnalyzeCatalogCard`, `setCardAnalyzeButtonState`,
`handleOpenMetadataWorkspace`, `presentInSessionSuggestion`,
`refreshMetadataSuggestionList`); `styles.css`; `tests/catalog_card_ai_quick_action.test.js`.

## Repository Gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: afa0670e26d17b04570ad555ba4f922052507c6c
Expected canonical tree: b6eafbcdef3a8bcb728498992c003d8ad5e9a447
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: afa0670e26d17b04570ad555ba4f922052507c6c
Schema head: Alembic 0033; no 0034_* migration
Working-copy topology: isolated-worktree
```

Create the worktree from the exact baseline. Do not mutate the canonical
checkout (no branch switch, no commits, no dirtying). Suggested identity:

```text
git -C /home/agile/Projects/framenest worktree add -b feat/gallery-card-ai-per-field-mvp \
  /home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w2 \
  afa0670e26d17b04570ad555ba4f922052507c6c
```

If that path is taken, choose another unused sibling under
`/home/agile/Projects/framenest-worktrees/` with the same kebab and `-w2`.
Worktree HEAD must equal the baseline before your first edit. Do not “fix”
`origin/feat/x-meme-browser-companion` ahead-count.

## Accepted Decisions (implement these)

Cooperator accepted the plan on 2026-08-27:

1. **Card 🧠 action (`handleAnalyzeCatalogCard`):**
   - Click confirms cloud upload with updated dialog copy (Title: `Analyze with AI?`, Confirm: `Analyze by AI`, Dismiss: `Not now`; text states editor will open with proposal strips, Current canonical values are not replaced, nothing saved until Save, physical file not renamed).
   - Card button enters `analyzing` state + existing CSS pulse.
   - Issues `POST /api/media/{id}/locations/{loc}/ai-suggestion-preview` with `confirm_cloud_upload: true` and `framenestMutationHeaders` (this triggers persist-join on server into `media_analysis_runs`).
   - On error: `failed_analysis` on card with error message.
   - On success: **opens the existing Edit dialog** (`handleOpenMetadataWorkspace`) with the suggestion loaded (`presentInSessionSuggestion(suggestion, payload)`), `metadataAiStatus = "Loaded"`, and `refreshMetadataSuggestionList` to reveal strips.
   - **ZERO automatic PUT `/api/media/{id}/metadata` from the card action.**
   - **ZERO bulk overwrite:** never call `applyResolvedAiSuggestionToMetadataWorkspace` or auto-replace Current form fields. Current fields load from canonical GET as normal.
   - Card returns to `idle` state (🧠 remains visible because canonical metadata is still incomplete until explicitly saved).
   - Dismissing or canceling the Edit dialog leaves canonical metadata unchanged.
   - Persistence happens ONLY when administrator clicks **Save** in the Edit dialog.

2. **Capability & audience gates:**
   - `identityAllowsCardAiQuickAction`: preserve `analysis.run` ∧ `metadata.canonical.write` ∧ `resolved` ∧ `available` ∧ incomplete metadata ∧ not movie.
   - **Add** `&& !companionWebHosted()` so card 🧠 is hidden in hosted companion (aligning with ADR-0077 §7).
   - Ordinary, unauthenticated, and hosted companion: 🧠 hidden.

3. **Cleanup of dead card-auto-save code:**
   - Remove card states `applying`, `failed_save` from 🧠 path (`CARD_AI_QUICK_ACTION_LOCKED` = `{confirming, analyzing}`).
   - Remove unused card auto-save helpers if orphaned (`suggestionIsUsableForCanonicalSave`, `applySavedAiMetadataToCatalogSurfaces`, `announceCardAiQuickActionSuccess`, `dismissCardAiQuickActionButton`, FLIP reflow helpers if no other callers exist).
   - Remove leftover `{ aiSuggestion }` bulk-apply parameter on `handleOpenMetadataWorkspace` that called `applyResolvedAiSuggestionToMetadataWorkspace`.

4. **Tests:**
   - Update `tests/catalog_card_ai_quick_action.test.js`: update source-wiring assertions (no PUT, no `applySavedAiMetadata...`, confirmation copy, open-workspace called); rewrite/replace flow tests expecting auto-PUT and card dismissal.
   - Update `tests/contract/test_local_web_application.py` (~1702, ~1893) and `tests/contract/test_youtube_creator_taxonomy_frontend.py` (~40–47).
   - Update `tests/tailscale_identity_frontend.test.js` and `tests/metadata_alias_edit.test.js` if affected by gate / workspace signature changes.

5. **ADR & Docs:**
   - Add new `docs/adr/0078-gallery-card-ai-per-field-review.md` (succeeds ADR-0077 §10).
   - Update `docs/adr/README.md` index row for 0078.
   - Update `GALLERY.md` to reflect per-field review on 🧠 shortcut.
   - Do NOT modify bodies of accepted ADRs 0023, 0020, 0062, 0065, 0066, 0067, 0073, 0076, 0077.

## Changed-Path Allowlist

Modify only:

1. `src/framenest/adapters/api/web/app.js`
2. `src/framenest/adapters/api/web/styles.css`
3. `tests/catalog_card_ai_quick_action.test.js`
4. `tests/contract/test_local_web_application.py`
5. `tests/contract/test_youtube_creator_taxonomy_frontend.py`
6. `tests/tailscale_identity_frontend.test.js`
7. `tests/metadata_alias_edit.test.js`
8. NEW `docs/adr/0078-gallery-card-ai-per-field-review.md`
9. `docs/adr/README.md`
10. `GALLERY.md`

Everything else is read-only.

## Negative Authority

- No canonical checkout mutation.
- No push, force, rebase of shared history, `git add .` / `git add -A`.
- No Alembic files; schema head stays `0033`.
- No edits to ADR **bodies** 0023, 0020, 0062, 0065, 0066, 0067, 0073, 0076, 0077.
- No `SECURITY.md`. No R4 / `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` in git.
- No fifth `companion_mutation`. No persist-join redesign. No Cover Studio.
- No NUC, SSH, sudo, `gpgconf`, Funnel, VPS, browser automation, provider calls.
- No secrets; never print hosts, IPs, Tailscale values, fingerprints, or keys.
- No `.venv` reconstruction; no `poetry env use`; no ambient
  `.venv/bin/python` / `python` / `python3` / `poetry run`.
- No Max/enhanced mode. No sub-agents. No Explore-style delegation.

## Execution Route (RF-16) and Isolated-Worktree Deviation

Declared Cursor Worker Python route:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c
./.ap/ap exec --root <WORKTREE> --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation runtime-info
./.ap/ap exec --root <WORKTREE> --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation test-focus -- <tests> -q -p no:cacheprovider
```

**Known miss:** `ap exec --root <WORKTREE>` fails (`declared CPython
executable does not exist`) because `ap.project.conf` uses relative
`.venv/bin/python`. Do **not** reconstruct `.venv`.

**Task-specific deviation** (not a second standing route):

```text
Declared route that could not be used: ap exec --root <WORKTREE>
Exact alternate:
  ./.ap/ap exec --root /home/agile/Projects/framenest \
    --baseline afa0670e26d17b04570ad555ba4f922052507c6c \
    --operation test-focus -- <tests> -q -p no:cacheprovider \
    --rootdir=<WORKTREE> -o pythonpath=<WORKTREE>/src
Rationale: interpreter lives in the canonical Poetry .venv; candidate source
  must still be the worktree src.
Evidence class: worker-observed era-06 limitation; ledger entry remains
  untriaged and non-authorizing.
Bounded authority: this Worker session only, Python tests for this allowlist.
Stopping condition: if provenance framenest.__file__ is not under
  <WORKTREE>/src, STOP ENVIRONMENT LIMITATION. Do not repair .venv.
```

Prove candidate source once (print `framenest.__file__` under the same
invocation). JS tests from the **worktree** root:

```text
node --test tests/catalog_card_ai_quick_action.test.js \
  tests/metadata_alias_edit.test.js \
  tests/tailscale_identity_frontend.test.js
```

And broader JS suite globs:

```text
node --test tests/*_frontend.test.js tests/*_cockpit.test.js tests/gallery_*.test.js tests/automatic_analysis_lifecycle.test.js tests/companion_web_bridge.test.js
```

Minimum Python (same deviation): `tests/contract/test_local_web_application.py`,
`tests/contract/test_youtube_creator_taxonomy_frontend.py`,
`tests/contract/test_media_ai_suggestions_api.py`,
`tests/contract/test_tailscale_ingress_security.py`.

## Git Authority

Inside **your worktree only**: stage explicit allowlisted paths; **1–2**
normal commits (commit 1: frontend + tests; commit 2: docs + ADR-0078). Commit
message style: short `fix:` / `feat:` / `docs:` subject focused on why. No
push. Report each commit SHA. Canonical checkout must remain `afa0670…`
tracked-clean when you stop.

## Report Contract

Write exactly:

```text
/home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/02_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include:

1. Coordinate echo: logical whole `framenest-gallery-card-ai-per-field-mvp`,
   session `02`, exchange `01`.
2. Status PASS | PARTIAL | BLOCKED.
3. `Phase-qualified result: implementation-PASS` only if allowlist work is
   complete and minimum-evidence suites pass; otherwise `not-applicable`.
   `Logical-whole closure: not-closed`.
4. Worktree path; baseline; each commit SHA; canonical checkout still
   `afa0670…` tracked-clean.
5. Changed files with per-file intent.
6. Exact test commands and outcomes, including the RF-16 deviation and
   `framenest.__file__` provenance.
7. Verification of core requirements: 0 auto-PUT from card 🧠; Edit modal opens with proposals; dismissal preserves canonical; hosted 🧠 hidden; ordinary 🧠 hidden; ADR-0078 added; no schema 0034; four companion_mutation unchanged.
8. Deviations, risks; empty sections say `none`.
9. One smallest next step (independent acceptance Worker 03, then publication + NUC).
10. Report justification: `new-mutation`.
11. Authority-expiry statement.
12. `Resolved Execution Issues / Near-Misses:` none | details.
13. `Pre-Existing Failure Classification:` none | complete classification.
14. Brief capability handshake: Plan Mode observed off; reasoning requested
    vs observed; Max observed off or unknown; qualitative context pressure.

## Human-Governance Routing

```text
Cooperator visibility: implementation grant already given; later independent acceptance, publication, NUC, numbered re-test
Human decision points: none inside this envelope
Deterministic steps inside bounded authority: implement, test, commit, report
Brainstorming classification: out-of-scope => future-logical-whole in the report
Internal delegation posture: not-used
Accountable Worker: one WORKER (this session)
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/
Trace project key: framenest
Trace logical-whole projection identity: framenest-gallery-card-ai-per-field-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt pre-staged); Worker writes only 02_report_00.md
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_implementation_00.md
Destination path: /home/agile/meta/projects/framenest/08/00-framenest-mvp-remainder/02_implementation_00.md
Archival: wait-for-report
```

```text
Client/surface announcement: Cursor Agent chat; native planning mode not-used
Recommended client/surface: fresh Worker Agent session
Recommended reasoning: High — capability split + Edit chrome + ADR
Enhanced/maximum mode: requested off
Automatic model selection: off
Independence requirement: none for this Worker; separate fresh acceptance later
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
```

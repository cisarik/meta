### Report for ORCHESTRATOR_CHAT

Logical whole: `framenest-gallery-card-ai-per-field-mvp`  
Worker session: `03`  
Worker exchange: `01`

Status: **PASS**

Phase-qualified result: `acceptance-PASS`  
Result artifact or commit: `3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18`  
Logical-whole closure: `not-closed`

```text
Acceptance candidate: 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
Acceptance owner map: Cooperator-accepted plan 01_report_00.md plus implementation grant 02_implementation_00.md plus candidate ADR-0078
Acceptance allowlist: inspection of the 10 committed paths only; no product edits
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
Independence: this session did not author 365426a95b0fe8116b297e8a5b591639943f4a3e or 3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18
```

## Worktree and Git

- Fresh checkout: `/home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w3` (detached `3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18`, tracked-clean)
- Ancestry: `git merge-base --is-ancestor afa0670e26d17b04570ad555ba4f922052507c6c HEAD` succeeded; `git rev-list --count afa0670e…..HEAD` = 2
- Commits on the candidate: `365426a95b0fe8116b297e8a5b591639943f4a3e` (frontend + tests), `3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18` (docs + ADR-0078)
- Canonical `/home/agile/Projects/framenest`: still `afa0670e26d17b04570ad555ba4f922052507c6c` on `feat/x-meme-browser-companion`, tree `b6eafbcdef3a8bcb728498992c003d8ad5e9a447`, tracked-clean (re-verified after worktree add and after tests)
- Public `refs/heads/main`: `afa0670e26d17b04570ad555ba4f922052507c6c` (`git ls-remote`)
- Pinned submodule: `.ap` gitlink == `.ap` HEAD == `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` on canonical and on w3
- Session-02 worktree `/home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w2`: still `3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18`, tracked-clean; not used as working copy; not edited
- Git writes this session: `worktree add --detach` of w3 and worktree-local `submodule update --init .ap` only. No product commits, add, push, or canonical checkout of the candidate.

## Path set versus parent `afa0670e…`

Exactly these 10 files (`git diff --name-only`); 303 insertions / 1060 deletions:

1. `GALLERY.md`
2. `docs/adr/0078-gallery-card-ai-per-field-review.md` (new)
3. `docs/adr/README.md`
4. `src/framenest/adapters/api/web/app.js`
5. `src/framenest/adapters/api/web/styles.css`
6. `tests/catalog_card_ai_quick_action.test.js`
7. `tests/contract/test_local_web_application.py`
8. `tests/contract/test_youtube_creator_taxonomy_frontend.py`
9. `tests/metadata_alias_edit.test.js`
10. `tests/tailscale_identity_frontend.test.js`

No extras. No `SECURITY.md`. No Python API modules. No `tailscale_ingress.py`. No Alembic `0034_*`. Bodies of ADR-0020 / 0023 / 0062 / 0065 / 0066 / 0067 / 0073 / 0076 / 0077: empty diffs.

## Control matrix

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | `handleAnalyzeCatalogCard` confirms Analyze, POSTs preview, opens Edit with `previewSuggestion` / `previewPayload` | hold | `app.js:5498-5555`; confirm copy `5508-5513`; POST preview `5525-5532`; `handleOpenMetadataWorkspace(..., { previewSuggestion, previewPayload })` `5552-5555`. Test: `successful preview opens Edit with the suggestion and does not PUT metadata` (`catalog_card_ai_quick_action.test.js:1185`). |
| 2 | Zero automatic `PUT /api/media/{id}/metadata` from card 🧠 | hold | `handleAnalyzeCatalogCard` body has 0 `method: "PUT"` (`app.js:5498-5571`; source-wiring `catalog_card_ai_quick_action.test.js:1056`). Remaining PUTs are Edit Save (`handleSaveMetadata` `app.js:7858-7874`) and unrelated surfaces. Tests assert `fetchCalls` contain 0 PUT (`:1204`, `:1437`). |
| 3 | Zero automatic `POST /api/canonical-tags` from card 🧠 | hold | Card handler POSTs only the preview (`app.js:5525-5532`). Tag POSTs live in `ensureMetadataTagKey` / `createAndSelectMetadataTag` (`app.js:7179`, `7752`), not the card path. Tests: `:1205`, `:1390`, `:1435`. |
| 4 | Dismissing / canceling Edit leaves canonical unchanged | hold | Cancel confirm returns with no fetch (`app.js:5515-5518`; test `confirmation cancel performs no mutation` `:1358`). `closeMetadataWorkspaceWithContext` resets local state and does not PUT (`app.js:7668-7717`). Rejected dirty-switch: test `:1530`. Canonical persist remains `handleSaveMetadata` only. |
| 5 | `presentPreviewSuggestionInMetadataWorkspace` reveals strips without bulk-replacing Current | hold | `app.js:7468-7471` → `presentInSessionSuggestion` (`6850-6858`) sets list selected/revealed only. Fresh open: `applyMetadataPayloadToWorkspace` then present (`7586`, `7605`). `handleOpenMetadataWorkspace` no longer takes `{ aiSuggestion }` (`7474`). `applyResolvedAiSuggestionToMetadataWorkspace` has zero call sites in `app.js`. Tests: `metadata_alias_edit.test.js:66-68`, `110`. |
| 6 | `identityAllowsCardAiQuickAction` requires `analysis.run` ∧ `metadata.canonical.write` ∧ `resolved` ∧ `available` ∧ incomplete metadata ∧ not movie ∧ `!companionWebHosted()` | hold | Gate `app.js:5264-5269`; eligibility `5272-5275` (`cardNeedsMetadata` + not movie). Source-wiring `:1030-1041`; eligibility test `:872`; contract `test_local_web_application.py:1702-1724`. |
| 7 | Hosted companion Gallery hides card 🧠 | hold | `!companionWebHosted()` in the identity gate (`app.js:5269`). Hosted-admin card: no `.catalog-card__action--analyze` (`catalog_card_ai_quick_action.test.js:852-864`). `tailscale_identity_frontend.test.js:388-418`. |
| 8 | Ordinary users never see 🧠 | hold | Same gate requires both capabilities. Ordinary gallery.read-only: no analyze (`catalog_card_ai_quick_action.test.js:686-707`); alias-write only: no analyze (`:710-716`); missing-capability fail-closed (`:992`). |
| 9 | Dead card-auto-save code removed | hold | `CARD_AI_QUICK_ACTION_LOCKED = {confirming, analyzing}` (`app.js:110`). `applySavedAiMetadataToCatalogSurfaces`, `announceCardAiQuickActionSuccess`, `dismissCardAiQuickActionButton`, FLIP helpers, `failed_save`, `applying` absent from `app.js`. CSS: no `data-analysis-state="applying"` / `failed_save` / dismissing; analyzing pulse kept (`styles.css:2302-2355`). Tests `:1059-1076`, `:1269`. |
| 10 | Schema head remains Alembic `0033`; no `0034_*` migration | hold | Versions dir ends at `0033_media_analysis_proposals.py`. No `0034_*` under `src/framenest/infrastructure/persistence/alembic_environment/versions/`. Path set has no migration. |
| 11 | Exactly four `companion_mutation=True` routes, unchanged | hold | `tailscale_ingress.py` not in the path set (empty diff vs parent). Four flags: opened `545`, apply `555`, `/api/x/requests` `563`, retry `572`. |
| 12 | ADR-0078 exists; index notes succession; ADR-0077 body untouched | hold | New `docs/adr/0078-gallery-card-ai-per-field-review.md`. `docs/adr/README.md:104-105` names 0078 as successor of 0077 Gallery-🧠 bulk-save. ADR-0077 body diff: 0 bytes. |

**Negative claims (must not hold):** ordinary Analyze / 🧠 — does not hold. Automatic canonical PUT from card 🧠 — does not hold. Alembic `0034` migration — does not hold. Fifth `companion_mutation` — does not hold. Hosted 🧠 — does not hold.

## Validation

Isolated-worktree declared route (expected miss; classified; not repaired):

```text
./.ap/ap project check --root <w3> --baseline afa0670e26d17b04570ad555ba4f922052507c6c
./.ap/ap exec --root <w3> --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation runtime-info
# both: ap: ERROR: declared CPython executable does not exist
```

Task-specific RF-16 deviation (canonical `--root`):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c
# ap project check --baseline: PASS

./.ap/ap exec --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation runtime-info
# interpreter: /home/agile/Projects/framenest/.venv/bin/python
# framenest.__file__=/home/agile/Projects/framenest/src/framenest/__init__.py
# (envelope only; not candidate provenance)
```

Python matrix (canonical `--root`, w3 `--rootdir` / `pythonpath`):

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c \
  --operation test-focus -- \
  <w3>/tests/contract/test_local_web_application.py \
  <w3>/tests/contract/test_youtube_creator_taxonomy_frontend.py \
  <w3>/tests/contract/test_media_ai_suggestions_api.py \
  <w3>/tests/contract/test_tailscale_ingress_security.py \
  /tmp/framenest-cardacc-03-provenance.py \
  -q -p no:cacheprovider -s --rootdir=<w3> -o pythonpath=<w3>/src
# 309 passed in 78.97s
# framenest.__file__=/home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w3/src/framenest/__init__.py
```

Stopping condition not met: candidate `src/` provenance held. Probe created, run, deleted.

Node from the fresh checkout root:

```text
node --test tests/catalog_card_ai_quick_action.test.js \
  tests/metadata_alias_edit.test.js \
  tests/tailscale_identity_frontend.test.js
# 57 pass, 0 fail
```

Broader JS glob from the fresh checkout root:

```text
node --test tests/*_frontend.test.js tests/*_cockpit.test.js tests/gallery_*.test.js \
  tests/automatic_analysis_lifecycle.test.js tests/companion_web_bridge.test.js
# 209 tests: 202 pass, 7 fail (all tests/movie_identification_frontend.test.js)
```

The seven movie-frontend failures reproduce on untouched canonical `afa0670e…` (same file: 8 tests, 1 pass, 7 fail; first causal error `missing function renderMetadataDurableAnalysis` / missing `Loading movie identification` markup). Classified below. Not a candidate defect.

## Deviations

- Isolated-worktree `ap exec --root <w3>` misses declared CPython (known launch-path). Used the prompt’s canonical `--root` plus `--rootdir` / `pythonpath` deviation. `.venv` was not reconstructed. Ambient `python` / `.venv/bin/python` / `poetry run` were not used.
- Envelope `runtime-info` on canonical `--root` prints canonical `framenest.__file__`. Candidate provenance is the pytest probe result above, not that envelope line.
- `applyResolvedAiSuggestionToMetadataWorkspace` remains defined (`app.js:5410`) with zero call sites. Deleting it would touch non-allowlisted `tests/automatic_analysis_lifecycle.test.js`. Not a control-matrix miss: card and workspace-open paths do not invoke it.

## Risks

The retained unused bulk-apply helper cannot be entered from the card 🧠 path or from `handleOpenMetadataWorkspace`. Residual risk is a later caller re-wiring it; that would be a new kebab. Candidate is unpublished.

## Out-of-scope observations (ledger-candidates only)

Isolated-worktree `ap exec --root <worktree>` still fails `declared CPython executable does not exist`. This matches the existing untriaged non-authorizing ledger entry `consumer-declared-execution-and-capability-route-binding`. No new ledger write in this session.

## Smallest next step

Cooperator publication of `3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18` to public `main` (non-force), then Cooperator NUC routine release-update via `~/nuc_push.fish`, then numbered rendered re-test from the frozen plan. This Worker does not publish, push, or deploy.

## Report justification

`final-acceptance`

## Authority expiry

This acceptance authority expires at this terminal report. No product edits, publication, push, NUC, or closure were granted or performed.

## Resolved Execution Issues / Near-Misses

none

## Pre-Existing Failure Classification

`tests/movie_identification_frontend.test.js` (7 tests) fail on both this fresh checkout of `3b8f9ab…` and canonical `afa0670e26d17b04570ad555ba4f922052507c6c`.

- First causal error: `extractFunction` reports `missing function renderMetadataDurableAnalysis`; related source-wiring asserts do not find `Loading movie identification` / Suggested-genres markup.
- Class: local repository evidence at the authorized parent baseline; not introduced by the 10-path candidate.
- Not repaired: file is outside the acceptance allowlist; function is absent on baseline.
- Disposition: pre-existing; out of scope for Worker 03.

## Capability handshake

- Plan Mode: requested `not-used`; observed off (acceptance prompt, no plan-mode transition).
- Reasoning: requested High; observed qualitative depth used for gate, path-set, Save-semantics, and RF-16 provenance; no independent attestation of a reasoning-level setting.
- Max / enhanced mode: requested off; observed off or unknown (no Max UI control in this session).
- Automatic model selection: off per prompt; not independently attested.
- Context pressure: moderate (`app.js` + test matrix); no containment failure.

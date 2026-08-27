### Report for ORCHESTRATOR_CHAT

Logical whole: `framenest-gallery-card-ai-per-field-mvp`  
Worker session: `02`  
Worker exchange: `01`

Status: **PASS**

Phase-qualified result: `implementation-PASS`  
Logical-whole closure: `not-closed`

## Worktree and Git

- Worktree: `/home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w2`
- Branch: `feat/gallery-card-ai-per-field-mvp`
- Exact baseline: `afa0670e26d17b04570ad555ba4f922052507c6c`
- Commit 1 (frontend + tests): `365426a95b0fe8116b297e8a5b591639943f4a3e`
- Commit 2 (docs + ADR-0078): `3b8f9abfccc61f56ec1d97cdb3ebcfe90db8be18`
- Canonical checkout `/home/agile/Projects/framenest`: still `afa0670e26d17b04570ad555ba4f922052507c6c` on `feat/x-meme-browser-companion`, tracked-clean
- No push

## Changed files

1. `src/framenest/adapters/api/web/app.js` — card 🧠 confirms Analyze, POSTs preview, opens existing Edit with proposal strips; zero auto-PUT; hosted hide; dead auto-save helpers removed; leftover `{ aiSuggestion }` bulk-apply parameter replaced by `{ previewSuggestion, previewPayload }`.
2. `src/framenest/adapters/api/web/styles.css` — drop `applying` / `failed_save` / dismissing card-AI states; keep analyzing pulse and reduced-motion.
3. `tests/catalog_card_ai_quick_action.test.js` — source-wiring and flow tests rewritten for no-PUT + open-workspace.
4. `tests/contract/test_local_web_application.py` — contract asserts follow the new card path.
5. `tests/contract/test_youtube_creator_taxonomy_frontend.py` — card handler no longer reads taxonomy / last-write-wins copy.
6. `tests/tailscale_identity_frontend.test.js` — hosted hide on the identity gate; mutation-site count 30→29 after removing the card PUT.
7. `tests/metadata_alias_edit.test.js` — workspace open no longer bulk-applies via `applyResolvedAiSuggestionToMetadataWorkspace`.
8. `docs/adr/0078-gallery-card-ai-per-field-review.md` — **NEW**; succeeds ADR-0077 §10.
9. `docs/adr/README.md` — index row for 0078; 0077 status note names the successor.
10. `GALLERY.md` — per-field strips, admin/hosted gate, native-disable when AI unavailable.

## Validation

`ap project check --root /home/agile/Projects/framenest --baseline afa0670e26d17b04570ad555ba4f922052507c6c` → PASS.

RF-16 known miss (classified, not repaired):

```text
./.ap/ap exec --root <WORKTREE> --baseline afa0670e26d17b04570ad555ba4f922052507c6c --operation runtime-info
# ap: ERROR: declared CPython executable does not exist
```

Authorized session-only deviation (canonical `--root`, worktree `--rootdir` / `pythonpath`):

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline afa0670e26d17b04570ad555ba4f922052507c6c \
  --operation runtime-info
# interpreter: /home/agile/Projects/framenest/.venv/bin/python
# framenest.__file__=/home/agile/Projects/framenest/src/framenest/__init__.py
# (envelope only)

./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline afa0670e26d17b04570ad555ba4f922052507c6c \
  --operation test-focus -- \
  <WORKTREE>/tests/contract/test_local_web_application.py \
  <WORKTREE>/tests/contract/test_youtube_creator_taxonomy_frontend.py \
  <WORKTREE>/tests/contract/test_media_ai_suggestions_api.py \
  <WORKTREE>/tests/contract/test_tailscale_ingress_security.py \
  /tmp/framenest-gallery-card-ai-per-field-mvp-w2-provenance.py \
  -q -p no:cacheprovider -s \
  --rootdir=<WORKTREE> \
  -o pythonpath=<WORKTREE>/src
# 309 passed in 81.44s
# framenest.__file__=/home/agile/Projects/framenest-worktrees/framenest-gallery-card-ai-per-field-mvp-w2/src/framenest/__init__.py
```

Temporary provenance probe created, run, deleted. Provenance is under the worktree `src/`. Stopping condition not met.

JS from the worktree root:

```text
node --test tests/catalog_card_ai_quick_action.test.js \
  tests/metadata_alias_edit.test.js \
  tests/tailscale_identity_frontend.test.js
# 57 pass, 0 fail
```

Broader JS globs from the worktree root:

```text
node --test tests/*_frontend.test.js tests/*_cockpit.test.js tests/gallery_*.test.js \
  tests/automatic_analysis_lifecycle.test.js tests/companion_web_bridge.test.js
# 209 tests: 202 pass, 7 fail (all tests/movie_identification_frontend.test.js)
```

The seven movie-frontend failures reproduce on the untouched canonical checkout at `afa0670…` and are classified below. They are outside this allowlist.

## Core-requirement verification

- 0 auto-PUT from card 🧠: `handleAnalyzeCatalogCard` has no `method: "PUT"` and one `framenestMutationHeaders` (preview POST only).
- Edit modal opens with proposals: success calls `handleOpenMetadataWorkspace(..., { previewSuggestion, previewPayload })`, which presents strips and sets `metadataAiStatus` to `Loaded` without replacing Current.
- Dismissal preserves canonical: no card-side metadata GET/PUT; persist only via existing Edit Save.
- Hosted 🧠 hidden: `identityAllowsCardAiQuickAction` includes `&& !companionWebHosted()`.
- Ordinary 🧠 hidden: still requires `analysis.run` ∧ `metadata.canonical.write` ∧ resolved ∧ available.
- ADR-0078 added; ADR bodies 0023/0020/0062/0065/0066/0067/0073/0076/0077 unchanged.
- Schema head remains Alembic `0033`; no `0034_*` migration.
- Four `companion_mutation=True` routes in `tailscale_ingress.py` unchanged.

## Deviations

- `applyResolvedAiSuggestionToMetadataWorkspace` is no longer called from the card or workspace-open path, but the helper function remains. Deleting it would break non-allowlisted `tests/automatic_analysis_lifecycle.test.js`, which still extracts that function. The leftover `{ aiSuggestion }` bulk-apply parameter is gone.
- Python evidence used the declared isolated-worktree `ap exec --root <WORKTREE>` miss plus the prompt’s session-only `--rootdir` / `pythonpath` deviation. `.venv` was not reconstructed.
- Broader JS glob includes pre-existing movie-identification frontend failures (see classification).

## Risks

none beyond the retained dead bulk-apply helper, which cannot be re-entered from the card path.

## Smallest next step

Independent acceptance Worker 03 on a fresh session against these unpushed commits, then a separately authorized publication + NUC routine release-update and numbered Cooperator re-test.

## Report justification

`new-mutation`

## Authority expiry

This implementation authority expires at this terminal report. No push, NUC, publication, or closure is granted.

## Resolved Execution Issues / Near-Misses

none

## Pre-Existing Failure Classification

`tests/movie_identification_frontend.test.js` (7 tests) fail on both this worktree and canonical `afa0670e26d17b04570ad555ba4f922052507c6c`.

- First causal error: `extractFunction` reports `missing function renderMetadataDurableAnalysis`; related source-wiring asserts do not find `Loading movie identification` / Suggested-genres markup in `app.js` / `index.html`.
- Class: local repository evidence at the authorized baseline; not introduced by this allowlist.
- Not repaired: file is outside the changed-path allowlist; function is absent on baseline, not deleted here.
- Disposition: pre-existing; out of scope for Worker 02.

## Capability handshake

- Plan Mode: requested `not-used`; observed off (implementation prompt, no plan-mode transition).
- Reasoning: requested High; observed qualitative depth used for gate + Edit chrome + ADR; no independent attestation of a reasoning-level setting.
- Max / enhanced mode: requested off; observed off or unknown (no Max UI control in this session).
- Automatic model selection: off per prompt; not independently attested.
- Context pressure: moderate (large `app.js` + test rewrite); no containment failure.

### Report for ORCHESTRATOR_CHAT

Logical whole: `framenest-ai-suggestions-alias-edit-mvp`
Worker session ordinal: `05`
Worker exchange ordinal: `01`
Worker session target: `fresh-worker-session`
Native planning mode: `not-used`
Task identity: `FRAMENEST-AI-SUGGESTIONS-ALIAS-EDIT-ACC-02`
Independence required: `yes`

**Status: PASS**

`Phase-qualified result: acceptance-PASS`
`Logical-whole closure: not-closed`
`Report justification: final-acceptance`

Authority for this grant expires at this terminal report. No product edits, commits, push, NUC, publication, or closure were performed.

Independence: this fresh session did not author `85e9c0411bfca71e1b2d211df547e33be9e6bdeb` or `afa0670e26d17b04570ad555ba4f922052507c6c` (authors: Michal Cisárik). Session 04 correction authority expired at `04_report_00.md`; that report was treated as a claim. Session 03 accepted parent `36ffdb19…` and is not evidence for this candidate.

## Coordinates

- Candidate: `afa0670e26d17b04570ad555ba4f922052507c6c`
- Parent / public `main` / canonical HEAD: `36ffdb197da9294fb1fbb06931f8169061a25c9b`
- Fresh checkout: `/home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w5` (detached, tracked-clean)
- Canonical `/home/agile/Projects/framenest`: `feat/x-meme-browser-companion` @ `36ffdb197da9294fb1fbb06931f8169061a25c9b`, tree `301976223ce1a716fb476c70ef9d18feeff85d29`, tracked-clean (unchanged after worktree add and after tests)
- Session-04 worktree `/home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w4`: still `afa0670e…`, tracked-clean, unused as working copy
- w2/w3: not used as the working copy
- Pinned `.ap`: gitlink == HEAD == `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (canonical and w5)
- `origin/main` ls-remote: `36ffdb197da9294fb1fbb06931f8169061a25c9b`
- `git merge-base --is-ancestor 36ffdb19… HEAD`: yes
- `git rev-list --count 36ffdb19…..HEAD`: 2

Git writes: only `worktree add --detach` of w5 and worktree-local `submodule update --init .ap`. Temporary provenance probe `/tmp/framenest-aliasacc-05-provenance.py` created, run, deleted.

## Path set versus parent

`git diff --name-only 36ffdb19… HEAD` is **exactly** the 27 named paths. No extras, none missing. Session-04 named deviation `companion_review_repository.py` is present as expected (one constructor argument `suggested_filename=`; no second store).

| Path | Status |
|---|---|
| `PRODUCT.md` | M |
| `SPEC.md` | M |
| `docs/X_COMPANION.md` | M |
| `docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md` | M |
| `docs/adr/README.md` | M |
| `src/framenest/adapters/api/application.py` | M |
| `src/framenest/adapters/api/media_analysis_lifecycle_api.py` | M |
| `src/framenest/adapters/api/media_catalog_api.py` | M |
| `src/framenest/adapters/api/tailscale_ingress.py` | M |
| `src/framenest/adapters/api/web/app.js` | M |
| `src/framenest/adapters/api/web/index.html` | M |
| `src/framenest/adapters/api/web/styles.css` | M |
| `src/framenest/application/companion_review.py` | M |
| `src/framenest/application/media_user_alias.py` | M |
| `src/framenest/application/ports/media_user_alias_repository.py` | M |
| `src/framenest/infrastructure/persistence/companion_review_repository.py` | M (+1 `suggested_filename=` argument) |
| `src/framenest/infrastructure/persistence/media_user_alias_repository.py` | M |
| `tests/automatic_analysis_lifecycle.test.js` | M |
| `tests/companion_web_bridge.test.js` | M |
| `tests/contract/test_local_web_application.py` | M |
| `tests/contract/test_media_ai_suggestions_api.py` | A |
| `tests/contract/test_media_catalog_api.py` | M |
| `tests/contract/test_x_route_policy.py` | M |
| `tests/metadata_alias_edit.test.js` | M |
| `tests/tailscale_identity_frontend.test.js` | M |
| `tests/unit/application/test_media_user_alias.py` | M |
| `tests/upload_cockpit_async_ownership.test.js` | M |

Absent versus parent: `alembic_environment/versions/0034*`; `SECURITY.md`; ADR-0062 / 0076 / 0023 **bodies**. Persist-join files outside the 27-set are unchanged (`media_analysis_lifecycle.py`, `companion_review_api.py`). `_ORDINARY_CAPABILITIES` / `identity_access.py` unchanged. `media_metadata_api.py` unchanged.

## Control matrix

| Row | Verdict | Evidence |
|---|---|---|
| 1. Ordinary Edit still uses `identityAllowsMetadataEdit` (`alias.write` ∨ `canonical.write`); Save split unchanged (alias PUT vs metadata PUT; canonical-write wins) | hold | `app.js:353-359`, `app.js:361-363`, `app.js:492`, `app.js:6085`, `app.js:6442-6458`, `app.js:8165-8169`; `tests/metadata_alias_edit.test.js` “ordinary Edit is gated…” and “ordinary Save uses alias PUT only…” |
| 2. Authenticated `GET /api/media` and `GET /api/media/{id}` merge caller overlay for `(media_id, login_key)` into `display_title` / `description` / tags; missing overlay fields keep canonical; no `login_key` → canonical; Alice ⊈ Bob | hold | `media_catalog_api.py:180-186`, `media_catalog_api.py:248-253`, `media_catalog_api.py:332-345`, `media_catalog_api.py:348-364`; `tests/contract/test_media_catalog_api.py::test_catalog_merge_applies_caller_overlay_and_isolates_logins`; `tests/unit/application/test_media_user_alias.py::test_list_aliases_for_login_does_not_leak_another_caller_overlay` |
| 3. `GET /api/media/{id}/metadata` stays canonical | hold | `media_metadata_api.py` blob equal to parent; overlay merge is catalog-only; ADR-0077:38-39 |
| 4. Load chrome: `identityAllowsAiSuggestionLoadChrome` = workspace ∧ (`alias.write` ∨ `canonical.write`) ∧ not movie; hosted shows Load / dropdown / strips; alias-mode shows Load | hold | `app.js:373-380`, `app.js:6581-6607`, `app.js:6803-6806`; no `companionWebHosted()` / `workflow.read` in Load predicate; `tests/metadata_alias_edit.test.js` Load chrome in alias mode and hosted; `tests/tailscale_identity_frontend.test.js:397`; `tests/companion_web_bridge.test.js:331` |
| 5. Analyze chrome: `identityAllowsAiAnalyze` = `analysis.run` ∧ not hosted ∧ not movie ∧ not alias; hosted hides Analyze | hold | `app.js:382-387`, `app.js:6569-6573`, `app.js:7386-7387`; hosted tests above |
| 6. Website Edit lists via `GET /api/media/{id}/ai-suggestions?limit=100` (ingress `metadata.alias.write`, not `companion_mutation`); inbox detail stays `workflow.read`; ordinary stays 403 on Apply; `app.js` contains no `/apply` substring | hold | `app.js:2420-2421`, `app.js:7171`; `tailscale_ingress.py:307-311` (`CAPABILITY_METADATA_ALIAS_WRITE`, default `companion_mutation=False`); inbox `tailscale_ingress.py:533-537` (`CAPABILITY_MEDIA_WORKFLOW_READ`); Apply `tailscale_ingress.py:547-555` (`CAPABILITY_MEDIA_CONTENT_PUBLISH` + `canonical.write`, `companion_mutation=True`); grep `/apply` on `app.js` empty; `tests/contract/test_media_ai_suggestions_api.py::test_ordinary_inbox_detail_stays_workflow_read`; `tests/contract/test_x_route_policy.py` suggestions capability and `companion_mutation is False`; `tests/metadata_alias_edit.test.js` `APP_SOURCE.includes("/apply") === false` |
| 7. Load does not call `applyResolvedAiSuggestionToMetadataWorkspace`; dropdown change issues zero provider calls and hides strips until Load; mapped suggested tags are buttons; unmapped are not | hold | `app.js:7358-7373` (Load only sets `revealed`); `app.js:7143-7150`; `app.js:7090-7107`; `styles.css:3097`, `styles.css:3139-3140`; `tests/metadata_alias_edit.test.js` per-field copy / Load does not bulk-apply / mapped tags are buttons; `tests/upload_cockpit_async_ownership.test.js` “Dropdown change hides strips until Load…” |
| 8. After Analyze, suggestion list dedupes on `analysis_run_id` (no in-session prepend of a missing-id duplicate); custom dropdown present (not a visible native `<select>` as the only control) | hold | `app.js:7152-7157`, `app.js:7197-7204` (filter by `analysisRunId`; no prepend of missing selectedItem); `index.html:562-575` (`#metadata-ai-suggestion-dropdown` / listbox, no suggestion `<select>`); `tests/automatic_analysis_lifecycle.test.js` dropdown chrome |
| 9. Content category and Acquisition source hidden in this Edit dialog for all actors; admin Save still has existing values to send | hold | `app.js:10758-10770` (`classificationRow.hidden = true`; selects still seeded); canonical payload still sends `content_category` (`app.js:6448-6458`); `tests/metadata_alias_edit.test.js` “ordinary alias Edit hides classification chrome…” |
| 10. Suggested filename is an informational note for ordinary and admin Load; not persisted into alias; no catalog rename | hold | `app.js:6812-6835`; alias Save payload is `display_title` / `description` / `tag_keys` only (`app.js:6442-6447`); `tests/automatic_analysis_lifecycle.test.js` filename note; `tests/upload_cockpit_async_ownership.test.js` “Suggested filename is an informational note… excluded from metadata Save” |
| 11. Schema head remains `0033`. Exactly four `companion_mutation=True` rows | hold | no `0034*` version file; `tests/integration/persistence/test_companion_review_migration.py::test_head_is_0033`; `tailscale_ingress.py:545,555,563,572`; `tests/contract/test_x_route_policy.py::test_only_companion_mutations_are_companion_flagged` |
| 12. ADR-0077 on the candidate records overlay display, ordinary list GET, hosted Load shown / Analyze hidden, filename note; index notes succession **without** ADR-0062/0076/0023 body edits | hold | ADR-0077:35-39, :54, :61-67, :73-74, :85-101; `docs/adr/README.md:89,103,104`; `git diff` empty for those three ADR bodies |
| N1. Ordinary Analyze / inbox Apply / `workflow.read` / `canonical.write` | must-not; holds | Load chrome does not grant those caps; Analyze requires `analysis.run` and not alias; Apply remains companion mutation; `_ORDINARY_CAPABILITIES` unchanged |
| N2. Overlay leak across `login_key` or onto anonymous catalog | must-not; holds | `_caller_overlay_page` returns `None` without `login_key`; Alice/Bob/anonymous isolation test |
| N3. Overlay merge onto administrator Manage / metadata GET | must-not; holds | `media_metadata_api.py` unchanged; Manage/publication APIs not in the 27-set |
| N4. Alembic `0034` | must-not; holds | no such version files |
| N5. Fifth `companion_mutation` | must-not; holds | flagged set size 4; ai-suggestions GET is not flagged |
| N6. Gallery 🧠 converted to per-field apply or shown to ordinary | must-not; holds | `identityAllowsCardAiQuickAction` still `analysis.run` ∧ `canonical.write` (`app.js:5266-5271`); parked admin bulk save still calls `applyResolvedAiSuggestionToMetadataWorkspace` only with canonical-write (`app.js:7897-7902`). Named parked debt, not a fail |

Every control-matrix row holds. Minimum named evidence is green.

## Tests and RF-16

Isolated-worktree route (classified environment limitation; not a candidate defect):

```text
./.ap/ap project check --root <w5> --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b
./.ap/ap exec --root <w5> --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b --operation runtime-info
# both: declared CPython executable does not exist
```

Authorized deviation (canonical `--root` proves the envelope, not the candidate):

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b
# PASS

./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b \
  --operation runtime-info
# interpreter: /home/agile/Projects/framenest/.venv/bin/python
# framenest.__file__=/home/agile/Projects/framenest/src/framenest/__init__.py
# (envelope proof only; not candidate provenance)
```

Python matrix via `test-focus` with `--rootdir` / `pythonpath` = w5, plus temporary probe `/tmp/framenest-aliasacc-05-provenance.py` (created, run, deleted):

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b \
  --operation test-focus -- \
  <w5>/tests/contract/test_local_web_application.py \
  <w5>/tests/contract/test_x_route_policy.py \
  <w5>/tests/contract/test_media_alias_api.py \
  <w5>/tests/contract/test_media_catalog_api.py \
  <w5>/tests/contract/test_media_ai_suggestions_api.py \
  <w5>/tests/unit/application/test_media_user_alias.py \
  <w5>/tests/integration/persistence/test_companion_review_migration.py::test_head_is_0033 \
  /tmp/framenest-aliasacc-05-provenance.py \
  -q -p no:cacheprovider -s \
  --rootdir=<w5> \
  -o pythonpath=<w5>/src
# 246 passed in 37.01s
# framenest.__file__=/home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w5/src/framenest/__init__.py
```

Node from the **fresh checkout** root:

```text
node --test tests/automatic_analysis_lifecycle.test.js \
  tests/upload_cockpit_async_ownership.test.js \
  tests/tailscale_identity_frontend.test.js \
  tests/companion_web_bridge.test.js \
  tests/catalog_card_ai_quick_action.test.js \
  tests/metadata_alias_edit.test.js
# 184 pass, 0 fail
```

`.venv` was not reconstructed. Ambient `python` / `.venv/bin/python` / `poetry run` were not invoked. Probe file is gone.

## Deviations

RF-16 isolated-worktree Python launch-path miss: `ap exec --root <w5>` cannot see the declared `.venv` interpreter. Used the prompt-authorized canonical `--root` plus `--rootdir` / `pythonpath` on w5. Candidate provenance under that invocation was w5 `src`. Not a candidate fail.

`companion_review_repository.py` +1 constructor argument is the named session-04 deviation; it only passes `suggested_filename` and does not add a second suggestion store. Not a fail.

## Risks

Parked Gallery 🧠 admin bulk analyze-and-canonical-save still uses last-write-wins canonical PUT. Named debt, not a fail.

Loopback `create_app` still skips ingress capability enforcement, so public/no-capability **HTTP 403** on the additive suggestion-list GET is not exercised in that topology. Evidence remains route-policy `metadata.alias.write` plus `IdentityContext.has_capability` (public lacks it; ordinary holds it; inbox detail remains `media.workflow.read`). Ordinary suggestion-list HTTP 200 is exercised on the additive router.

## Next step

Cooperator publication of `afa0670e26d17b04570ad555ba4f922052507c6c` to GitHub `main`, then routine NUC release update (`deploy/ubuntu/framenest-release`) before numbered re-test.

Out of this envelope: per-field Gallery 🧠, R4, Cover Studio, persistent multi-model comparison, VPS.

`Resolved Execution Issues / Near-Misses:` isolated-worktree CPython miss classified as environment limitation; authorized deviation used; provenance probe asserted w5 `src` and was deleted.

`Pre-Existing Failure Classification:` none.

## Capability handshake

Plan Mode observed off. Reasoning recommendation High. Max/enhanced mode observed off or unknown. Sub-agents not used. No NUC, SSH, sudo, providers, or browser automation.

# WORKER TASK — Bounded correction (caller-visible alias + ordinary/hosted Load)

Role: WORKER
Persistent role identity: WORKER
Logical whole identity: framenest-ai-suggestions-alias-edit-mvp
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: Implementation
Native planning mode: not-used
Implementation authority: explicit
Reasoning recommendation: High
Task identity: FRAMENEST-AI-SUGGESTIONS-ALIAS-EDIT-CORR-01
Task type: bounded correction
Exact baseline: 36ffdb197da9294fb1fbb06931f8169061a25c9b
Independence required: no
Evidence posture: non-independent
Authority renewal: sessions 02 and 03 expired at their reports. This prompt is
  the sole current grant. You did not implement `36ffdb19…` in this session.
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
Acceptance candidate (parent): 36ffdb197da9294fb1fbb06931f8169061a25c9b
Acceptance owner map: Cooperator numbered re-test 2026-08-26 plus Orchestrator freeze accepted by Cooperator word «koriguj»
Acceptance allowlist: see § Changed-path allowlist
Acceptance risk claims: caller overlay is private to login_key; catalog merge must not leak Alice overlay to Bob or to anonymous/public; ordinary suggestion list is read-only; Apply/Analyze/canonical.write stay denied; no 0034; four companion_mutation unchanged
Acceptance control matrix: see § Frozen correction
Acceptance independence: not-required for this corrector; full-fresh independent acceptance is a later Worker
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
```

```text
Evidence tier: E3
Evidence tier basis: catalog JSON overlay merge is identity-scoped; new suggestion-list GET is a capability split (read vs Apply/Analyze)
Authorized implementation stages: isolated-worktree create → implement allowlisted files → focused tests → 1–3 local commits → terminal report
Combined implementation envelope: allowed
Implementation stage gates: repository gate before mutation; tests green before commit; canonical checkout remains untouched
Independent acceptance: required-separate-fresh-worker
Rollback or recovery checkpoint: isolated worktree + unpushed commits; discard worktree if BLOCKED before commit
Activated stricter profile: none
Terminal implementation report point: after local commit(s), before any push
```

```text
Development envelope activation: activated
Development envelope identity: FrameNest isolated correction worktree (this grant)
Declared reversible class: reversible local mutation (worktree files + local commits)
Working-copy topology: isolated-worktree
Topology rationale: keep canonical public main clean; exact-source candidate parented on published 36ffdb19
Irreversible exclusions: secrets, destruction, accounts, public exposure, unrelated owner data, publication, push, NUC, closure, schema migration, .venv reconstruction
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: tests/metadata_alias_edit.test.js; tests/automatic_analysis_lifecycle.test.js; tests/upload_cockpit_async_ownership.test.js; tests/tailscale_identity_frontend.test.js; tests/companion_web_bridge.test.js; tests/catalog_card_ai_quick_action.test.js; tests/contract/test_local_web_application.py; tests/contract/test_x_route_policy.py; tests/contract/test_media_alias_api.py; tests/contract/test_media_catalog_api.py; tests/contract/test_companion_review_api.py
Affected tests: the suites above plus new allowlisted tests
New causal regression: caller-visible alias on Gallery/Details; ordinary and hosted Load; tag chips clickable; dropdown dedupe + custom chrome; category/source hidden
Broad or full suite: not-used
Runtime or testbed: isolated worktree + declared AP exec deviation below
Independent acceptance: required-separate-fresh-worker
```

This prompt grants correction only inside the isolated worktree and allowlist.
It grants no push, publication, NUC, provider calls, browser automation, schema
migration, or closure. Authority expires at your terminal report. You do not
self-accept. You do not close the logical whole.

## Source precedence

1. This prompt (frozen correction below).
2. Cooperator scores after NUC refresh of `36ffdb19…` (items 4/7/8 PARTIAL;
   item 2 caller-visible alias now required).
3. Repository at the exact baseline, including ADR-0077 as written on that SHA.
4. Accepted ADRs on that baseline. You surgically update **ADR-0077** to record
   the succeeded display/Load sentences. You do **not** edit ADR bodies 0023,
   0062, 0065, 0067, 0073, or 0076.

If the repository contradicts this grant, STOP BLOCKED with exact evidence.
Do not self-grant extra paths.

## Mandatory reading

1. This prompt.
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `/home/agile/Projects/framenest/.ap/AP.md`
4. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
5. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
6. Baseline ADR-0077; ADR-0062 (read-only body); `docs/X_COMPANION.md`
7. `src/framenest/adapters/api/web/app.js` (`identityAllowsAiSuggestionsChrome`,
   `refreshMetadataSuggestionList`, `presentInSessionSuggestion`,
   `renderMetadataSuggestionStrips`, catalog card title ~6030, Details title)
8. `media_catalog_api.py`, `media_alias_api.py`, `companion_review_api.py`
   detail GET, `tailscale_ingress.py` route policies, `identity_access.py`
   (read-only unless you prove a new capability is required — it is not)

## Repository gate

```text
Repository checkout topology: standalone checkout with pinned submodule
Canonical root: /home/agile/Projects/framenest
Expected canonical branch: feat/x-meme-browser-companion
Expected canonical HEAD: 36ffdb197da9294fb1fbb06931f8169061a25c9b
Expected canonical tree: 301976223ce1a716fb476c70ef9d18feeff85d29
Expected canonical working tree: tracked-clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: 36ffdb197da9294fb1fbb06931f8169061a25c9b
Schema head: Alembic 0033; no 0034_* migration
Working-copy topology: isolated-worktree
```

Create the worktree from the exact baseline. Do not mutate the canonical
checkout. Suggested identity:

```text
git -C /home/agile/Projects/framenest worktree add -b feat/ai-suggestions-alias-edit-corr \
  /home/agile/Projects/framenest-worktrees/framenest-ai-suggestions-alias-edit-mvp-w4 \
  36ffdb197da9294fb1fbb06931f8169061a25c9b
```

If that path is taken, choose another unused sibling under
`/home/agile/Projects/framenest-worktrees/` with the same kebab and `-w4`.
Do not reuse w2 or w3 as the working copy. Worktree HEAD must equal the
baseline before your first edit. Do not “fix”
`origin/feat/x-meme-browser-companion` ahead-count.

## Frozen correction (do not replan)

Cooperator accepted this freeze with «koriguj» on 2026-08-26.

### 1. Caller-visible alias read

Authenticated Gallery and Details **display** must show the caller's overlay
when a non-empty `media_user_aliases` row exists for `(media_id, login_key)`.
Merge into the fields those surfaces already render (`display_title`,
`description`, tags). Field-level: overlay value wins when present; missing
overlay fields keep canonical.

- Anonymous / public-published / no `login_key`: **canonical only**.
- Bob must never see Alice's overlay.
- `GET /api/media/{id}/metadata` stays **canonical** (admin Save source).
- Admin Manage / publication browser stays canonical (do not merge overlay
  onto that API).
- Ordinary Save remains `PUT …/alias`. Empty overlay still means no row.
- No Alembic `0034`. Use existing overlay tables.

Implement the merge on `GET /api/media` and `GET /api/media/{media_id}`
(catalog). `list_media` currently has no `Request` — add identity-scoped merge
there. Prefer existing `GetMediaUserAlias`; a batch repository method for the
page is allowed if N+1 would be dishonest. Do not restyle Gallery cards;
only the displayed text/tags change.

### 2. Load chrome for ordinary, alias mode, and hosted companion web

Split today's `identityAllowsAiSuggestionsChrome` (which requires
`media.workflow.read` ∧ not hosted ∧ not alias mode):

- **Load + dropdown + strips + filename note:** workspace audience ∧
  (`metadata.alias.write` ∨ `metadata.canonical.write`) ∧ not movie.
  **Hosted companion web shows Load.** Alias-mode Edit shows Load.
- **Analyze by AI:** `analysis.run` ∧ not hosted ∧ not movie ∧ not alias
  mode. Hosted still hides Analyze.

Ordinary does **not** gain `media.workflow.read`, `analysis.run`,
`metadata.canonical.write`, or Apply.

Do **not** rebuild `extension/ui/save.html`. Companion Edit with Load is the
hosted FrameNest metadata dialog in the side panel.

### 3. Suggestion list GET ordinary can call

Inbox detail `GET /api/companion/review-inbox/{media_id}` stays administrator
`media.workflow.read`. Ordinary stays 403 there. Apply stays 403 for ordinary.

Add **one** additive read route that lists the same generic analyzed,
companion-visible successes for that media (newest first, movie 409, limit
default/max matching inbox detail / `limit=100`). Reuse existing run
filter/serialization; **no second suggestion store**.

- Ingress capability: `metadata.alias.write` (ordinary and admin both hold
  it; public-published does not).
- Same audience gate as catalog GET (uniform 404 `MEDIA_NOT_FOUND`).
- **Not** `companion_mutation`. Do not add a fifth mutation flag.
- Website Edit **reads** this route for **both** ordinary and admin Load.
  Admin Analyze remains the existing preview POST + persist-join.
- Response must carry title, description, mapped tags, suggested filename,
  provider/model, `analysis_run_id` so the dropdown can dedupe.

If you must touch `application.py` DI / `tailscale_ingress.py` policy rows,
that is in scope. Do not change `_ORDINARY_CAPABILITIES`.

### 4. Filename

After Load, show suggested filename to ordinary and admin as an informational
strip/note. Alias PUT still `display_title` / `description` / `tag_keys` only.
Do not persist filename into the overlay. Do not rename catalog files. A
copy-to-clipboard control is allowed; a ✅ that writes canonical metadata is
not.

### 5. Suggested tags

Each mapped suggested tag is a **button**. Click appends that key to Current
selected tags (chip with `x`, same as existing selected-tag remove). Idempotent
if already present; honor the existing tag limit. Unmapped/ambiguous tags are
not buttons. Enable pointer events (today `.metadata-suggestion-strip` and
`.metadata-suggestion-tag` use `pointer-events: none`). Flex-wrap without
overlap.

### 6. Hide classification in this Edit dialog

Hide **Content category** and **Acquisition source** in this metadata Edit
dialog for **all** actors. Do not delete the data model. Admin canonical Save
must preserve existing category/source (no silent rewrite to defaults).
Gallery catalog filters stay. Movie Identify remains admin movie-only.

### 7. Dropdown: dedupe + eye candy

After Analyze, the list must not show an extra in-session duplicate of the
just-persisted run. Today's `refreshMetadataSuggestionList` prepends
`selectedItem` when `analysisRunId` is missing from inbox — that is the
Cooperator “3 not 2; re-open shows 2” defect. Dedupe on stable
`analysis_run_id`. If persist-join returns the real id, replace the in-session
row; do not keep both.

Replace the visible native `<select>` with a companion-language custom
dropdown (dark, green accent, dense; tokens from
`extension/ui/sidebar.css` / existing `--accent`). Dropdown change still
issues **zero** provider calls and hides strips until Load. Keep keyboard
selection and an accessible name. Update tests that freeze the native select
if the control changes.

Load still must not call `applyResolvedAiSuggestionToMetadataWorkspace`.

## Changed-path allowlist

Modify only:

1. `src/framenest/adapters/api/web/app.js`
2. `src/framenest/adapters/api/web/index.html`
3. `src/framenest/adapters/api/web/styles.css`
4. `src/framenest/adapters/api/media_catalog_api.py`
5. `src/framenest/adapters/api/application.py` (DI only)
6. `src/framenest/adapters/api/tailscale_ingress.py` (additive GET policy only;
   do not change the four `companion_mutation=True` rows)
7. One additive HTTP adapter for the suggestion list — prefer extending
   `src/framenest/adapters/api/media_analysis_lifecycle_api.py` **or** a
   smallest new module next to it. Reuse companion-review listing internals
   rather than duplicating SQL. If reuse requires a thin application helper,
   `src/framenest/application/companion_review.py` and/or
   `src/framenest/application/media_analysis_lifecycle.py` are allowed.
8. `src/framenest/application/media_user_alias.py` and
   `src/framenest/application/ports/media_user_alias_repository.py` plus
   `src/framenest/infrastructure/persistence/media_user_alias_repository.py`
   **only** if a batch-get for catalog pages is required.
9. Tests you add or extend among:
   - `tests/metadata_alias_edit.test.js`
   - `tests/automatic_analysis_lifecycle.test.js`
   - `tests/upload_cockpit_async_ownership.test.js`
   - `tests/tailscale_identity_frontend.test.js`
   - `tests/companion_web_bridge.test.js`
   - `tests/catalog_card_ai_quick_action.test.js`
   - `tests/contract/test_local_web_application.py`
   - `tests/contract/test_x_route_policy.py`
   - `tests/contract/test_media_alias_api.py`
   - `tests/contract/test_media_catalog_api.py`
   - `tests/contract/test_companion_review_api.py`
   - NEW focused contract test for the additive suggestion-list GET
   - NEW/extended unit test for overlay merge isolation (Alice ⊈ Bob)
10. `docs/adr/0077-ordinary-alias-edit-affordance-and-per-field-ai-suggestions.md`
    — succeed §2 display, §5 ordinary-no-list, §7 hosted-hide-Load, §8
    filename-admin-only, and the Deferred “Gallery alias display” line.
    Index succession in `docs/adr/README.md` if the 0077 row would stay false.
11. `PRODUCT.md`, `SPEC.md`, `docs/X_COMPANION.md` — surgical present tense
    only where this correction makes a current sentence false.

Everything else is read-only. Do not edit ADR **bodies** 0023, 0062, 0065,
0067, 0073, 0076. Do not add ADR-0078 unless 0077 cannot record the succession
honestly — prefer updating 0077.

## Negative authority

- No canonical checkout mutation.
- No push, force, rebase of shared history, `git add .` / `git add -A`.
- No Alembic files; schema head stays `0033`.
- No edits to ADR **bodies** 0023, 0062, 0065, 0067, 0073, 0076.
- No `SECURITY.md`. No R4 / `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` in git.
- No fifth `companion_mutation`. No persist-join redesign. No Cover Studio.
- No ordinary `analysis.run` / `canonical.write` / Apply / `workflow.read`.
- No `extension/ui/save.html` / `save.js` redesign. No `review.html` revival.
- No NUC, SSH, sudo, `gpgconf`, Funnel, VPS, browser automation, provider calls.
- No secrets; never print hosts, IPs, Tailscale values, fingerprints, or keys.
- No `.venv` reconstruction; no `poetry env use`; no ambient
  `.venv/bin/python` / `python` / `python3` / `poetry run`.
- No Max/enhanced mode. No sub-agents. No Explore-style delegation.
- Do not restyle the Gallery grid beyond overlay text/tags.

## Execution route (RF-16) and isolated-worktree deviation

Declared Cursor Worker Python route:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b
./.ap/ap exec --root <WORKTREE> --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b --operation runtime-info
./.ap/ap exec --root <WORKTREE> --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b --operation test-focus -- <tests> -q -p no:cacheprovider
```

**Known miss:** `ap exec --root <WORKTREE>` fails (`declared CPython
executable does not exist`) because `ap.project.conf` uses relative
`.venv/bin/python`. Do **not** reconstruct `.venv`.

**Task-specific deviation** (not a second standing route):

```text
Declared route that could not be used: ap exec --root <WORKTREE>
Exact alternate:
  ./.ap/ap exec --root /home/agile/Projects/framenest \
    --baseline 36ffdb197da9294fb1fbb06931f8169061a25c9b \
    --operation test-focus -- <tests> -q -p no:cacheprovider \
    --rootdir=<WORKTREE> -o pythonpath=<WORKTREE>/src
Rationale: interpreter lives in the canonical Poetry .venv; candidate source
  must still be the worktree src.
Evidence class: worker-observed era-06/07 limitation; ledger entry remains
  untriaged and non-authorizing.
Bounded authority: this Worker session only, Python tests for this allowlist.
Stopping condition: if provenance `framenest.__file__` is not under
  <WORKTREE>/src, STOP ENVIRONMENT LIMITATION. Do not repair .venv.
```

Prove candidate source once (print `framenest.__file__` under the same
invocation). JS tests from the **worktree** root with `node --test` on every
JS file you touch plus `tests/metadata_alias_edit.test.js`. Do not install JS
toolchains. Do not run gated browser evidence.

Minimum Python (same deviation): every contract file you touch, plus
`tests/contract/test_x_route_policy.py` (still exactly four
`companion_mutation=True`), plus one schema-head assertion path that still
requires `0033`. Do not run the full suite.

First failing suite: preserve output, classify (candidate / harness /
ambient-route / environment), stop that batch. Ambient encodings signature:
rerun once through `ap exec`; never inventory Pythons.

## Git authority

Inside **your worktree only**: stage explicit allowlisted paths; **1–3**
normal commits. Commit message style: short `fix:` / `feat:` / `docs:` subject
focused on why. No push. Report each commit SHA. Canonical checkout must
remain `36ffdb19…` tracked-clean when you stop.

## Report contract

Write exactly:

```text
/home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/04_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Professional English. Include:

1. Coordinate echo: logical whole `framenest-ai-suggestions-alias-edit-mvp`,
   session `04`, exchange `01`.
2. Status PASS | PARTIAL | BLOCKED.
3. `Phase-qualified result: implementation-PASS` only if the freeze is
   implemented and minimum-evidence suites pass; otherwise `not-applicable`.
   `Logical-whole closure: not-closed`.
4. Worktree path; baseline; each commit SHA; canonical checkout still
   `36ffdb19…` tracked-clean.
5. Changed files with per-file intent.
6. Exact test commands and outcomes, including the RF-16 deviation and
   `framenest.__file__` provenance.
7. Mapping: catalog overlay merge + isolation; new suggestion-list GET +
   ingress capability; Load vs Analyze gates; hosted Load shown / Analyze
   hidden; tag buttons; hidden category/source with preserved admin values;
   dropdown dedupe; filename informational; no 0034; four
   `companion_mutation`; ADR-0077 succession.
8. Deviations, risks; empty sections say `none`.
9. One smallest next step (independent full-fresh acceptance, then
   Cooperator publication + NUC).
10. Report justification: `new-mutation`.
11. Authority-expiry statement.
12. `Resolved Execution Issues / Near-Misses:` none | details.
13. `Pre-Existing Failure Classification:` none | complete classification.
14. Brief capability handshake: Plan Mode observed off; reasoning requested
    vs observed; Max observed off or unknown; qualitative context pressure.

## Human-governance routing

```text
Cooperator visibility: correction grant already given; later independent acceptance, publication, NUC, numbered re-test
Human decision points: none inside this envelope
Deterministic steps inside bounded authority: implement, test, commit, report
Brainstorming classification: out-of-scope => future-logical-whole in the report
Internal delegation posture: not-used
Accountable Worker: one WORKER (this session)
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/
Trace project key: framenest
Trace logical-whole projection identity: framenest-ai-suggestions-alias-edit-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt pre-staged); Worker writes only 04_report_00.md
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 04_correction_00.md
Destination path: /home/agile/meta/projects/framenest/07/00-framenest-ai-suggestions-alias-edit/04_correction_00.md
Archival: wait-for-report
```

```text
Client/surface announcement: Cursor Agent chat; native planning mode not-used
Recommended client/surface: fresh Worker Agent session
Recommended reasoning: High — identity-scoped catalog merge + capability-split GET + Edit chrome
Enhanced/maximum mode: requested off
Automatic model selection: off
Independence requirement: none for this Worker; separate fresh full-fresh acceptance later
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
```

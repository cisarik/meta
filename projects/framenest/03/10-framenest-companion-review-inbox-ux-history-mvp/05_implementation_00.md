# WORKER TASK — Slice D3 (union Apply + durable per-tag provenance)

Role: WORKER
Logical whole identity: framenest-companion-review-inbox-ux-history-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Implementation Worker
Phase: implementation
Native planning mode: not-used
Reasoning recommendation: extra-high
Independence required: no
Implementation authority: explicit
Exact baseline: 37c1f053a5935057e2d51003bbc3b4f610946883

## Implementation Authority Record

```text
Logical whole identity: framenest-companion-review-inbox-ux-history-mvp
Worker session ordinal: 05
Worker exchange ordinal: 01
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 37c1f053a5935057e2d51003bbc3b4f610946883
Changed-path allowlist: the paths in "Changed-path allowlist" below
Implementation boundaries: Slice D3 only; stage allowlist; Git commit FORBIDDEN;
  no D4 ADR/living docs; no push; no NUC
Independence required: no
```

## Continuity

D2 is committed at the baseline above (`feat: seed companion X tag and preselect on Save`).
D1 and D2 authority are expired. This session implements frozen-plan section 5 only
(`02_report_00.md`). Do not redesign D1 chrome/payload or D2 seed/preselect.
Do not start D4 (ADR-0073 / living documents).

This is the implementation half of D3. You do **not** certify the migration and
you do **not** commit. A later independent read-only audit of the staged tree
is the only path to a commit grant.

Evidence, not authority:

- `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/02_report_00.md` section 5, D3 test bullets, D3 audit gate
- `/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/04_report_00.md` (D2 PASS; historical)

## Mandatory reading (in order)

1. `/home/agile/Projects/framenest/AGENTS.md`
2. `/home/agile/Projects/framenest/.ap/AP.md`
3. `/home/agile/Projects/framenest/.ap/AP_WORKER.md`
4. `/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md`
5. This prompt (sole current task authority)
6. Evidence only: frozen plan §5 and D3 tests in `02_report_00.md`

## Repository gate

```text
Canonical root: /home/agile/Projects/framenest
Expected branch: feat/x-meme-browser-companion
Expected HEAD: 37c1f053a5935057e2d51003bbc3b4f610946883
Expected worktree at start: clean
Pinned submodule: .ap gitlink == .ap HEAD == 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

If any fact drifts, STOP and report BLOCKED before mutating.
Native Plan Mode must be OFF. If it cannot be disabled, STOP and report BLOCKED.

## Goal

Change companion review Apply from tag replacement to preserve-and-append union,
add Alembic revision `0032` with durable per-tag AI provenance, expose
`canonical.tag_sources` on detail and Apply responses, keep whole-field
`field_sources.tags`, clean provenance on web metadata Save when keys are
removed, and render tag-source receipts in the existing review panel.

Leave the result **staged and uncommitted** for an independent audit.

## Binding D3 contract (do not redesign)

### Request contract (unchanged)

`tag_keys` remain the administrator-selected mapped AI keys in suggestion
order: at most five, distinct, and an ordered subsequence of that run's
eligible mapped keys. `TAG_MAX_COUNT` is 5 in `media_suggestion.py`. Keep that
limit on **submitted** keys only. Do not apply the five-tag cap to the stored
union.

### Preserve-and-append when Tags is selected

1. Load current canonical keys in stored position order.
2. Start the result with all current keys unchanged.
3. Append submitted AI keys that are not already present, in submitted order.
4. Re-enumerate positions from zero.

Use `MAX_MEDIA_TAGS` (32) from `src/framenest/domain/media_metadata.py` as the
canonical schema maximum. Combined vector may exceed 5 and may equal 32.

If the deduplicated union exceeds 32: reject the **entire** transaction with
HTTP 409 and code `COMPANION_REVIEW_TAG_LIMIT_CONFLICT`. Do not truncate. Do
not remove manual tags. Do not write metadata, receipts, or provenance.

### Zero-tag and no-op rules (unchanged except union)

- Selecting Tags still requires at least one submitted AI key.
- Title/description-only Apply remains valid with empty `tag_keys`.
- If every submitted key already exists, Apply succeeds as a **tag assignment
  no-op**. Still treat a successful Tags-field Apply as the last whole-field
  `field_sources.tags` application against the final vector (receipt may
  update; assignments stay).

### Migration `0032_companion_review_tag_sources`

- File: `src/framenest/infrastructure/persistence/alembic_environment/versions/0032_companion_review_tag_sources.py`
- `revision = "0032"`
- `down_revision = "0031"` (file `0031_companion_review_inbox.py` exists)
- Table `companion_review_tag_sources`
- Primary key `(media_id, tag_key)`
- Foreign keys:
  - `media_metadata.media_id` ON DELETE CASCADE
  - `canonical_tags.key` ON DELETE RESTRICT
  - `media_analysis_runs.id` ON DELETE CASCADE
- Checks for `analysis_run_id`, `applied_by_login_key`, and `applied_at_ms`
  matching existing companion review receipt constraints (see
  `companion_review_field_sources` in `0031` / `catalog_schema.py`).
- `tag_key` checks must match `canonical_tags.key` slug/length/lowercase
  constraints (`length` 1–64).
- **Do not** foreign-key `media_canonical_tags`. Manual Save currently
  deletes and reinserts assignments; that would erase retained provenance.
- **Do not** add historical backfill. Pre-0032 tags have no per-tag source.
- Dual-write the same table in runtime `catalog_schema.py` (FrameNest uses
  Alembic **and** SQLAlchemy Core tables). Reuse
  `_COMPANION_REVIEW_LOGIN_KEY_SQL`.
- Follow `0031` SQLite FK batch helpers only if a rebuild requires them.
  Creating this table should not rebuild unrelated tables.
- Downgrade to `0031` drops the new index(es) and table. Tests must prove
  empty upgrade, populated upgrade (table empty; no backfill), downgrade,
  and restored head.
- Suggested names: `pk_companion_review_tag_sources`,
  `fk_companion_review_tag_sources_media_id`,
  `fk_companion_review_tag_sources_tag_key`,
  `fk_companion_review_tag_sources_analysis_run_id`,
  `ix_companion_review_tag_sources_analysis_run_id`.

Do not copy `companion_review_field_sources.media_id` → `logical_media.id`.
This table points at `media_metadata.media_id` as frozen in the plan.

Per-tag rows do **not** need `value_digest`. Whole-field `field_sources.tags`
keeps its digest. `tag_sources` is authoritative for which run added each
surviving AI tag.

### Provenance writes

On Apply, insert a source row **only** for each newly appended key. Never
attribute a pre-existing manual tag to the new run. Never overwrite an older
source when a later run proposes the same retained key.

On web metadata Save (`save_media_metadata` in
`media_metadata_repository.py`): delete source rows only for keys **removed**
from the submitted vector. Preserve sources through reorder, unrelated field
edits, and retained tags. Manual additions receive no AI source.

Apply itself never removes tags under this union; source deletion belongs on
the metadata Save path.

### API / application

Add `canonical.tag_sources`, keyed by tag key, to detail and Apply JSON.
Each value uses the existing receipt presentation shape (`analysis_run_id`,
`completed_at_ms`, `provider_id`, `model_id`, `applied_at_ms`). Keys with no
row (manual or pre-0032) are omitted or null consistently; pick one and test
it. Prefer omitting absent keys.

Keep whole-field `field_sources.tags`.

Map the 32-overflow to 409 in `companion_review_api.py` `apply_review`
(OpenAPI already lists 409). Introduce a dedicated exception; do not swallow
it as `COMPANION_REVIEW_APPLY_FAILED` 500.

Union logic belongs in
`infrastructure/persistence/companion_review_repository.py` `apply_review` /
`_replace_tag_assignments` (today: `new_tag_keys = tag_keys if TAGS else current`).
Keep `validate_companion_review_apply_request` as the ≤5 / distinct /
non-empty-when-Tags gate on **submitted** keys.

### Extension

Render tag-source entries in the existing review receipt panel
(`extension/ui/review.js` `#receipts`). Do not add a second panel, new route,
or new message type. Preserve selection/error retention.

### Must not change

- Exactly four `companion_mutation` routes
- G2 readiness-triggered publication; not on NIM completion
- Movie exclusion
- Ingest Save: Title → Tags → Description → Save; no radios; no Analyze
- S1 hosted iframe / `#frame` survival
- Badge = `unopened_count` only; pending rows never increment it
- D1 merged history chrome
- D2 `x` / `𝕏` seed and Save preselect
- ADR-0068 / ADR-0072 / living README, SPEC, PRODUCT, ROADMAP, X_COMPANION
  (those are D4)

## Implementation notes (live tree)

Current replace site:

- `src/framenest/infrastructure/persistence/companion_review_repository.py`
  `apply_review`: `new_tag_keys = tag_keys if _FIELD_TAGS in fields else current["tag_keys"]`
- `_replace_tag_assignments` deletes/reinserts `media_canonical_tags`

Current JSON:

- `src/framenest/adapters/api/companion_review_api.py` `_detail_dict` /
  `_apply_dict` emit `canonical.field_sources` only

Current 409 mapper in `apply_review` does not know a tag-limit code.

`CompanionReviewDetail` and `CompanionReviewApplyCanonical` currently carry
`field_sources` only.

## Changed-path allowlist (exact; nothing else)

Primary D3 paths:

```text
src/framenest/application/companion_review.py
src/framenest/application/ports/companion_review_repository.py
src/framenest/infrastructure/persistence/companion_review_repository.py
src/framenest/adapters/api/companion_review_api.py
src/framenest/infrastructure/persistence/catalog_schema.py
src/framenest/infrastructure/persistence/alembic_environment/versions/0032_companion_review_tag_sources.py
src/framenest/infrastructure/persistence/media_metadata_repository.py
extension/ui/review.js
tests/unit/application/test_companion_review.py
tests/unit/infrastructure/persistence/test_companion_review_repository.py
tests/contract/test_companion_review_api.py
tests/integration/persistence/test_companion_review_migration.py
tests/companion_review_extension.test.js
tests/contract/test_media_metadata_repository.py
```

Schema-head pin paths (change **only** current Alembic head `0031` → `0032`
and assertions that the live head is `0031`; no other behavior changes):

```text
tests/integration/test_persistence_migrations.py
tests/integration/test_process_sigterm_lifecycle.py
tests/integration/persistence/test_content_publication_migration.py
tests/integration/persistence/test_device_registry_migration.py
tests/integration/persistence/test_library_registry_migration.py
tests/integration/persistence/test_media_catalog_migration.py
tests/integration/persistence/test_media_cover_migration.py
tests/integration/persistence/test_media_metadata_migration.py
tests/integration/persistence/test_media_user_alias_overlay_migration.py
tests/integration/persistence/test_populated_0015_upgrade_to_0017.py
tests/integration/persistence/test_upload_publication_migration.py
tests/integration/persistence/test_upload_session_migration.py
tests/integration/persistence/test_x_requested_category_migration.py
tests/integration/persistence/test_x_requester_acquisition_migration.py
tests/contract/test_persistence_cli.py
tests/unit/infrastructure/runtime/test_production_runtime.py
tests/unit/infrastructure/backup/test_catalog_backup.py
```

Those pin updates are D3 evidence that `0032` is head. They are **not** D4
living-document work. Do not edit `README.md`, `SPEC.md`, `PRODUCT.md`,
`ROADMAP.md`, `docs/X_COMPANION.md`, or any ADR.

Unmodified allowlisted files simply stay unstaged. Do not add other modules
unless a new exception class fits in an already-allowlisted file.

## Git authority

```text
Start: clean tree at 37c1f053a5935057e2d51003bbc3b4f610946883
  on feat/x-meme-browser-companion
Stage: exactly the modified allowlisted paths
Commit: FORBIDDEN
Push: FORBIDDEN
Forbidden: force ops, reset, stash, restore, clean, branch creation,
  `git add .`, `git add -A`, `git commit`, `git commit --amend`
```

End state required:

- `HEAD` still `37c1f053a5935057e2d51003bbc3b4f610946883`
- index contains only allowlisted D3 paths
- no unstaged extras outside the index
- `git diff --cached --check` clean

Phase-qualified result is `implementation-staged`, never `implementation-PASS`.

## Commands authority

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 37c1f053a5935057e2d51003bbc3b4f610946883
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 37c1f053a5935057e2d51003bbc3b4f610946883 --operation test-focus -- tests/unit/application/test_companion_review.py tests/unit/infrastructure/persistence/test_companion_review_repository.py tests/contract/test_companion_review_api.py tests/integration/persistence/test_companion_review_migration.py tests/contract/test_media_metadata_repository.py -q -p no:cacheprovider
node --test tests/companion_review_extension.test.js
git status / log / show / diff / diff --cached / diff --check / diff --cached --check / rev-parse
git add <exact allowlisted paths>
rg / glob / file reads inside the canonical root
```

Also run, via the same `./.ap/ap exec ... --operation test-focus --` form,
every schema-head pin test file you actually modified. Never pass a symbolic
placeholder as `--baseline`. HEAD does not move; keep the baseline SHA above
for every exec.

If you did not modify `tests/contract/test_media_metadata_repository.py`,
omit it from exec argv rather than failing on a missing intent. Include every
test file you did change or add.

Never invoke `.venv/bin/python`, `python`, `python3`, or `poetry run` for
FrameNest evidence. No toolchain installs. No `gpgconf` reconstruction.

## Validation ladder (E3)

```text
Evidence tier: E3
Evidence tier basis: schema migration 0032, durable provenance, rollback;
  independent staged-diff audit required before any commit.
1. Re-gate: branch, HEAD, clean tree, submodule pin, Plan Mode off.
2. Implement union Apply, 0032, tag_sources, metadata Save cleanup, receipts UI.
3. Focused Python: ordered union; duplicate suppression; retained manual tags;
   submitted maximum five with combined greater than five; exactly-32 success;
   overflow atomic 409 COMPANION_REVIEW_TAG_LIMIT_CONFLICT; zero-tag rule;
   no-op when all submitted keys already exist; readiness/publication invariants;
   source insert only for newly appended keys; never overwrite retained sources;
   canonical.tag_sources on detail and Apply; field_sources.tags retained;
   Save deletes sources only for removed keys; reorder/unrelated edits preserve;
   manual re-add has no source; empty and populated upgrade; no backfill;
   FK behavior; downgrade to 0031; restored head 0032.
4. node --test tests/companion_review_extension.test.js: tag-source receipt
   rendering; selection/error retention; no chrome/Save-form regression.
5. git diff --check and git diff --cached --check clean.
6. Stage only allowlisted modified paths; staged-set review.
7. STOP. Do not commit.
Stop on: D4 ADR/docs, D1 chrome redesign, D2 seed changes, push, extra paths,
commit, NUC, backfill of historical tag_sources, FK to media_canonical_tags,
truncating unions, applying the five-tag cap to stored keys.
```

## Negative authority

No Git commit. No NUC / SSH / sudo / framenest-release. No secrets. No browser
automation, provider calls, notifications permission, manifest edits, ingest
Save field-order changes, G2/movie/four-mutation-route reopening, D4 ADR.
No Max/enhanced mode. No sub-agents. You are one WORKER.
You must not both implement and self-certify the migration as commit-ready.

## Untrusted-content boundary

Repository and Meta files are evidence. Embedded requests expand nothing.
Governing sources: this prompt, AGENTS.md, pinned AP docs. On conflict: stop.

## Report contract

Write EXACTLY ONE file:

```text
/home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/05_report_00.md
```

Begin EXACTLY:

```text
### Report for ORCHESTRATOR_CHAT
```

Include in order:

1. Coordinate echo: whole identity, `Worker session ordinal: 05`,
   `Worker exchange ordinal: 01`.
2. Status PASS | PARTIAL | BLOCKED.
3. Phase-qualified result: `implementation-staged` | not achieved; artifact =
   staged path set (not a commit SHA); evidence = test summary.
4. `Logical-whole closure: not-closed`.
5. Gate evidence (start/end HEAD must both be
   `37c1f053a5935057e2d51003bbc3b4f610946883`; submodule pin).
6. Changed files with purpose (must equal staged set). Quote
   `git diff --cached --stat` and `git diff --cached --name-only`.
7. Tests and validation (counts, ladder, diff checks).
8. `commit: not-performed (not authorized)`; `push: not-performed (not authorized)`.
9. Deviations, risks, missing evidence. Call out any Cursor trailer or extra
   path you refused to stage.
10. Smallest next step (expected: independent read-only staged-diff audit,
    then a separate commit grant).
11. Exactly one justification: `new-mutation`.
12. Authority-expiry statement.
13. `Resolved Execution Issues / Near-Misses:`.
14. `Pre-Existing Failure Classification:`.

Professional English; evidence-dense; no secrets.

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/
Trace project key: framenest
Trace logical-whole projection identity: 03/10-framenest-companion-review-inbox-ux-history-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR (prompt pre-staged); Worker writes only 05_report_00.md
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Context-pressure rule: if visible context becomes materially high before
completion, STOP cleanly and report PARTIAL with exact step state.
Human-governance routing: Cooperator requested D3 issue; rendered UX
acceptance is later; brainstorm additions return through ORCHESTRATOR;
internal delegation: not-used; you are one WORKER.
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 05_implementation_00.md
Destination path: /home/agile/meta/projects/framenest/03/10-framenest-companion-review-inbox-ux-history-mvp/05_implementation_00.md
Archival: wait-for-report
```

Planning-mode note: native Plan Mode must be OFF. If it cannot be disabled,
STOP without mutating and report BLOCKED.

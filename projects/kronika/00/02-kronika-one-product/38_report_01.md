### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 38
Worker exchange ordinal: 02

Status: PASS
Phase-qualified result: implementation-PASS
Logical-whole closure: not-closed
Report justification: new-mutation

Start commit: `5843486ddeae13ec5b331f102c5cb595bfa6e386`
End commit: `0d0d8c88bf88bf8454751a0205bc8652374796c2`
Changed files: 14 allowlisted paths; household reads now serve the approved snapshot
Commit and push: one local commit; no push

## Repository re-gate

Verified before any edit:

```text
root     /Users/agile/Projects/framenest
branch   feat/kronika-one-product
HEAD     5843486ddeae13ec5b331f102c5cb595bfa6e386
parent   38e7beeb3921d7c0fd8e717e480754fbd18130c9
tree     863c0411f4be0e3d2389890aa8952862399ee51a
subject  chore: adopt AP pin 73e20ef80b88700d5fcbc397cd8edd4fc425869f
status   empty
AP pin   73e20ef80b88700d5fcbc397cd8edd4fc425869f (gitlink equals .ap HEAD)
main     40e51cb2d061ead96850c9c94aa59de54d5e1310
origin/main 40e51cb2d061ead96850c9c94aa59de54d5e1310
```

Continuity anchor `38_report_00.md` SHA-256 `86a0eda29de487ace60c40c8282fde2f4c2d489c829859648307b64686f738e1` matched. Predecessor grant SHA-256 `f5c3af564f74a7e8df9c99783e4cadaf841e8d19ccb6788e7a478213df62e199` matched. `38_report_01.md` was absent. `src/framenest/application/ports/media_cover_repository.py` was not edited.

## Validation

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 5843486ddeae13ec5b331f102c5cb595bfa6e386
```

Exit 0 before editing, and exit 0 again before the commit.

Red, unfixed candidate, one `test-focus` invocation of `tests/contract/test_kronika_approved_projection.py -q -p no:cacheprovider` with the same baseline. Exit 1. `test_household_http_reads_keep_the_approved_media_projection` failed: detail `display_title` was `TitleB`, expected `TitleA`. The two existing tests in that file passed (`1 failed, 2 passed`).

Green, same command after the fix. Exit 0. `3 passed`.

Targeted set, one `test-focus` invocation, same baseline, `-q -p no:cacheprovider`:

```text
tests/contract/test_kronika_approved_projection.py
tests/contract/test_media_catalog_api.py
tests/contract/test_media_metadata_api.py
tests/contract/test_media_content_api.py
tests/contract/test_media_catalog_repository.py
tests/contract/test_gallery_preview_api.py
tests/contract/test_cover_api.py
tests/contract/test_media_analysis_lifecycle_api.py
tests/contract/test_media_ai_suggestions_api.py
tests/contract/test_content_audience_policy.py
tests/contract/test_public_published_uds.py
tests/contract/test_kronika_record_authorization.py
tests/contract/test_kronika_access_inventory.py
tests/unit/application/test_media_catalog.py
tests/integration/persistence/test_kronika_record_repository.py
```

Exit 0. `281 passed`. `tests/contract/test_companion_review_api.py` was not added: the suggestion read was constrained in the lifecycle API from the stored snapshot, and the companion-review modules were not edited. The four parked pre-existing failures were not run.

`git diff --cached --check` exit 0 before the commit.

## Changed paths

```text
src/framenest/adapters/api/content_audience_api.py
src/framenest/adapters/api/cover_api.py
src/framenest/adapters/api/gallery_preview_api.py
src/framenest/adapters/api/media_analysis_lifecycle_api.py
src/framenest/adapters/api/media_catalog_api.py
src/framenest/adapters/api/media_content_api.py
src/framenest/adapters/api/media_metadata_api.py
src/framenest/application/media_catalog.py
src/framenest/application/media_cover.py
src/framenest/application/ports/media_catalog_repository.py
src/framenest/application/ports/records.py
src/framenest/infrastructure/persistence/media_catalog_repository.py
src/framenest/infrastructure/persistence/record_repository.py
tests/contract/test_kronika_approved_projection.py
```

14 paths. All were on the effective allowlist.

## Commit

```text
SHA     0d0d8c88bf88bf8454751a0205bc8652374796c2
parent  5843486ddeae13ec5b331f102c5cb595bfa6e386
tree    96adead05beb58f2e282ff77b9e6d29bff2c8298
subject fix(kronika): serve approved projections on household reads
status  empty (git status --porcelain=v1 --untracked-files=all)
```

No push, fetch, tag, merge, rebase, reset, or branch change.

## R2–R8

R1. Direct household reads that used `content_audience_allows` now take `deny | current | approved | legacy`. `deny`, `current`, and `legacy` keep the previous handlers. A missing policy, missing identity, or repository failure still fails closed. Writes still use the boolean allow.

R2. `GET /api/media/{id}` for `approved` is built from the approved relational snapshot: scalars, tags, and approved locations only. `collection_key` and `processed_at_ms` are empty. Cover readiness follows whether the approved cover digest is present, not the current cover. The caller alias overlay still applies. Exercised: Bob sees `TitleA` / `general` / `Approved description` and only the approved location; Alice still sees `TitleB` / `meme`.

R3. `GET /api/media/{id}/metadata` for `approved` serializes the snapshot with `persisted` true and does not read the working metadata row. `collection_key`, `processed_at_ms`, genres, and metadata timestamps stay empty. Exercised in the regression.

R4. A member gallery includes another owner's approved family record without a `media_content_publications` row. Member filters for collection, acquisition source, and creator use approved values for those rows; a collection filter cannot match through post-approval working state. Title, tag, and category filters already split that way and were left in place. Administrator, legacy-public, deny, and anonymous membership still use the previous publication join or empty result. Exercised: Bob's list contains the record, `collection=processed` does not, `content_category=general` does, `content_category=meme` does not.

R5. Content and download for `approved` accept only location ids in the snapshot. Any other id returns `404` `MEDIA_CONTENT_NOT_FOUND` before resolve, so the file is not opened. Exercised for the location added after approval.

R6. Cover thumbnail for `approved` uses only the approved digest's ETag and bytes, and returns `404` when that artifact is missing. It does not call the current-cover reader. Not dynamically exercised: the regression stored no cover artifact and did not request `cover-thumbnail`. Existing cover contract tests passed for the non-approved path.

R7. Automatic analysis, movie identification, and `ai-suggestions` for `approved` are taken from the snapshot. A suggestion-shaped snapshot is returned on automatic analysis; a movie-shaped snapshot (`identified_title`) is returned on movie identification; anything else is the existing absent view. Suggestions decode the snapshot with the companion parser and return `next_cursor` null. The live history is not queried. LEAD result: after approval of a parser-accepted result titled `SnapshotTitle`, the working run was changed to `WorkingTitle`. Bob's `ai-suggestions` body was exactly that one approved title and a null cursor. `automatic-analysis` and `movie-identification` did not contain `WorkingTitle`. Movie identification was the absent representation because this snapshot is not a movie result.

R8. Gallery preview for `approved` returns the same `404` as an unknown location when the location id is not in the snapshot, before `open_ready`. Not dynamically exercised: the regression did not request a preview. Existing gallery-preview contract tests passed for the non-approved path.

R9. No new endpoint, schema, migration, dependency, network, host, or `private/**` access. The authorization decision is not weakened.

## Deviations, risks, and missing evidence

This session does not certify the correction. Cover bytes and a gallery-preview request for a post-approval location were not exercised. Approved suggestion items carry empty provider fields and `completed_at_ms` 0 because those values are not in the snapshot; the title, description, and tags come from the snapshot. Household write routes still follow the previous boolean allow.

## Smallest next step

Fresh independent E3/R3 re-audit of `0d0d8c88bf88bf8454751a0205bc8652374796c2`, including the original finding and the unexercised cover and gallery-preview reads.

## Resolved Execution Issues / Near-Misses

none

## Pre-Existing Failure Classification

```text
Pre-existing claim: none
```

## Orchestration critique

```text
Orchestration critique:
MEASURED: none
LEAD: an approved cover digest with a different current cover, and a gallery preview of a location added after approval, were not requested in the regression; cheapest check is the fresh re-audit of this SHA
```

## Authority expiry

This report is the terminal result. Correction authority is expired. No further edit, test, commit, or probe is authorized by this exchange.

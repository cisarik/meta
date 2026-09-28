# KRONIKA-ONE-PRODUCT-S6-A35-F01-CORRECTION — bounded correction of finding S6-A35-F01

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 38
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S6-A35-F01-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — authorization-boundary correction with runtime behavior change; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

This is a genuinely fresh Worker session. Inherit no prior authority. No subagents.
The formal report is written in English; the short completion notice to the
Cooperator is written in Slovak with masculine address. Begin read-only, then
execute exactly this bounded correction.

Security task class: accepted-finding correction
Accepted finding IDs: S6-A35-F01
Exact path allowlist: see "Exact path allowlist" below
Regression test: `tests/contract/test_kronika_approved_projection.py` — the new
household-approved-read test defined in required behavior R10, which must fail
on the unfixed candidate and pass on the corrected candidate
Audit authority: none — you do not audit or certify your own correction
Re-audit routing: after your local commit, a separate fresh independent E3/R3
re-audit of the corrected exact SHA is required (separate grant; not yours)
Commits: one corrective commit only, as specified below

## Where things stand

A fresh independent acceptance of S6 candidate
`38e7beeb3921d7c0fd8e717e480754fbd18130c9` returned PARTIAL with finding
S6-A35-F01 (high, correction-required). The record service stores and returns
the approved snapshot correctly; the household-facing HTTP read routes do not.
The acceptance is `35_report_00.md` in the trace; the frozen S6 plan and its
surface matrix are `33_report_00.md`; the implementation history is
`34_report_00.md`..`34_report_04.md`.

Observed gap in one sentence: after an administrator approves media as title
`TitleA` / category `general`, an ordinary household member's HTTP reads still
receive the post-approval working state (`TitleB` / `meme` / a new location):
`GET /api/media/{id}` and `GET /api/media/{id}/metadata` serialize the current
working row; the detail payload discloses a location id added after approval;
content for that location returns `409 MEDIA_CONTENT_UNAVAILABLE` instead of
`404`; and gallery membership requires a stray legacy publication row, so an
approved record without one is absent from list and total.

Required outcome: when the per-item access decision is `approved`, detail,
metadata, analysis, cover, preview and content reads serve only the approved
projection, its approved locations and its approved cover digest; gallery
membership and member-scope filters evaluate the approved values and include an
approved family record without any legacy publication row. Owner (`current`),
`legacy`, `deny`, anonymous, public-composition and administrator behavior
remain unchanged.

## Repository and route

Working directory: `/Users/agile/Projects/framenest`
Repository identity: `https://github.com/cisarik/framenest.git`
Repository checkout topology: standalone checkout
Expected branch: `feat/kronika-one-product`
Expected HEAD at issuance (already checked out for you):
`38e7beeb3921d7c0fd8e717e480754fbd18130c9`
Expected parent: `40e51cb2d061ead96850c9c94aa59de54d5e1310`
Expected tree: `d6d5d314bfaf98d968235a867004b89b3187ac68`
Subject: `feat(kronika): add private records and administrator approval`
Governing AP: `.ap` at `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and
`.ap` HEAD); read-only; do not update, attach, or upgrade it.
Canonical `.venv`: `/Users/agile/Projects/framenest/.venv` (CPython 3.13.14,
Poetry-owned). Do not recreate, move, symlink, or repair it.

Repository gate (verify independently before any edit; stop on divergence):
physical root, branch, HEAD/parent/tree/subject as above; empty
`git status --porcelain --untracked-files=all`; AP pin gitlink equals `.ap` HEAD;
local `main` and `origin/main` equal `40e51cb2d061ead96850c9c94aa59de54d5e1310`.
Direct read-only `git ls-remote https://github.com/cisarik/framenest.git` may
confirm `refs/heads/main` = `40e51cb2…` and
`refs/heads/feat/kronika-one-product` = `38e7bee…`. No fetch is needed; all
required objects are already present locally.

Execution route (canonical; no ambient substitute):

```text
./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- <files> -q -p no:cacheprovider
```

## Mandatory reading

- Governing WORKER spine: `.ap/AP.md`, `.ap/AP_WORKER.md`,
  `.ap/PROMPT_CONTRACTS.md` (Accepted-Finding Correction Prompt Contract,
  Bounded Correction Worker, Worker Report Header), project `AGENTS.md`,
  `docs/WORKER_EXECUTION_CONTRACT.md`, `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md`.
- Trace: `35_report_00.md` (finding S6-A35-F01, exact locations, correction
  direction), `33_report_00.md` sections 4 and 7 (frozen surface matrix,
  mandatory scenario "Projection stability", declared route).
- Candidate files named in the finding's "exact location" line and in the
  required behavior below.

## Required behavior (binding outcomes)

R1. Decision, not a boolean. Every direct media read surface that today calls
`content_audience_allows` obtains the per-item decision
`deny | current | approved | legacy` (`content_audience_decision`). `deny`,
`current` and `legacy` behavior stays byte-compatible with the candidate;
`approved` follows R2–R8. Do not weaken the gate: a missing policy, missing
identity, or repository failure continues to fail closed exactly as today.

R2. Detail (`GET /api/media/{media_id}`): for `approved`, build the response
from the approved projection of the bound record — approved scalar fields
(display title, description, content category, acquisition source, creator
fields), approved tags, and the approved location tuples only. The payload must
contain no location id absent from the approved snapshot and no working-state
value. Cover readiness derives from the approved cover digest, never from the
current cover. The caller-private alias overlay may still apply (it is
caller-owned). Response shape and error codes stay as today.

R3. Metadata (`GET /api/media/{media_id}/metadata`): for `approved`, serialize
the approved snapshot: `persisted` true, approved display title, description,
tags, content category, acquisition source, creator fields. Fields absent from
the snapshot (`collection_key`, `processed_at_ms`, `genres`, `updated_at_ms`,
and metadata timestamps) must not be populated from the current working row.
Do not query the latest working metadata for a household read.

R4. Gallery membership and member filters (`GET /api/media`): a member scope
must include another owner's approved family record **without any
`media_content_publications` row**; total, limit and offset stay consistent.
For approved rows, every filter predicate — `q`, tags, `collection`,
`content_category`, `acquisition_source`, creator filters — evaluates against
the approved values only; a post-approval working value must never match.
Anonymous, `deny`, `legacy` (public composition) and administrator paths keep
today's membership rules; the public composition continues to exclude every
bound record even with an erroneous legacy publication row.

R5. Content and download (`GET /api/media/{media_id}/locations/{location_id}/content`
and `.../download`): for `approved`, only location ids present in the approved
snapshot are valid targets. Any other location id — including a location added
after approval — returns the same `404 MEDIA_CONTENT_NOT_FOUND` body as an
unknown location, without opening, probing or caching a file for it. Approved
locations keep the existing resolution semantics (`409 MEDIA_CONTENT_UNAVAILABLE`
remains correct for a genuinely unavailable approved location; `416` range
behavior unchanged).

R6. Cover (`GET /api/media/{media_id}/cover-thumbnail`, and any other
household-reachable cover reader with the same gap): for `approved`, serve only
the approved artifact digest — ETag and bytes — and return `404` when that
artifact is missing; never fall back to the current cover. Owner/admin cover
routes stay unchanged.

R7. Analysis and suggestions (`GET /api/media/{media_id}/automatic-analysis`,
`GET /api/media/{media_id}/movie-identification`,
`GET /api/media/{media_id}/ai-suggestions`): for `approved`, the response is
derived only from the approved snapshot's analysis (`analysis_run_id` /
`analysis_result`) or the existing absent representation; a household read must
not disclose the current latest analysis or suggestions from a non-approved
run. The LEAD from the acceptance (a stored result the companion parser accepts
might still expose current analysis) is in scope for R7: reproduce it with a
synthetic stored analysis result that the existing suggestion parser accepts,
approve it, change the working analysis, then verify the household
`ai-suggestions` read does not disclose the changed analysis. If an existing
suggestion service cannot be constrained to approved data within this
allowlist, stop and report the exact additional path needed — do not weaken the
gate and do not silently leave current-analysis disclosure in place.

R8. Gallery preview
(`GET /api/media/{media_id}/locations/{location_id}/gallery-preview`): for
`approved`, only approved location ids are valid; others return the same `404`
as an unknown location; no preview is ever produced from a non-approved
location.

R9. No weakening and no expansion. The loopback/token/Host/Origin boundaries,
the sandbox, the administrator approval gate, server-derived ownership, and the
fail-closed denial behavior stay exactly as they are. No new endpoints, no
schema or migration change, no `0035`, no dependency change, no network, no
host/NUC/SSH/browser/provider/credential action, no `private/**` access.

R10. Required regression (`tests/contract/test_kronika_approved_projection.py`,
new test, synthetic callers and fixtures only): owner Alice's bound media is
approved as title `TitleA` / category `general` / family; then the working
state is changed to title `TitleB` / category `meme` / collection `processed`
and a **new location** is added. Household member Bob must then observe: detail
and metadata show `TitleA` / `general` and only the approved locations; the
gallery list contains the record without any publication row; the collection
filter `processed` does not match it through working state;
`content_category=general` includes it and `content_category=meme` excludes it;
content and download for the new location return `404 MEDIA_CONTENT_NOT_FOUND`.
Write this test first and record it failing on the unfixed candidate, then
implement, then record it passing.

## Exact path allowlist

Edit only files from this list that the correction actually needs. Every edited
path must appear in the commit. No wildcard expansion; no directory-wide
authorization. Any needed edit outside this list is a stop (report the exact
path and why).

Core production paths (expected to carry the fix):

```text
src/framenest/adapters/api/content_audience_api.py
src/framenest/adapters/api/media_catalog_api.py
src/framenest/adapters/api/media_metadata_api.py
src/framenest/adapters/api/media_content_api.py
src/framenest/application/media_catalog.py
src/framenest/application/ports/media_catalog_repository.py
src/framenest/infrastructure/persistence/media_catalog_repository.py
```

Additional production paths (edit only for the named approved-surface
requirement R6/R7/R8 or the approved-projection accessor; keep each edit
minimal and report why it was needed):

```text
src/framenest/adapters/api/cover_api.py
src/framenest/adapters/api/gallery_preview_api.py
src/framenest/adapters/api/media_analysis_lifecycle_api.py
src/framenest/adapters/api/media_suggestion_api.py
src/framenest/application/records.py
src/framenest/application/ports/records.py
src/framenest/infrastructure/persistence/record_repository.py
src/framenest/application/media_content.py
src/framenest/application/gallery_preview.py
src/framenest/application/media_cover.py
src/framenest/application/ports/media_cover_repository.py
src/framenest/infrastructure/persistence/media_cover_repository.py
src/framenest/application/companion_review.py
src/framenest/application/ports/companion_review_repository.py
src/framenest/infrastructure/persistence/companion_review_repository.py
src/framenest/domain/record_access.py
```

Test and support paths:

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
tests/contract/test_companion_review_api.py
tests/unit/application/test_media_catalog.py
tests/integration/persistence/test_kronika_record_repository.py
tests/support/record_access.py
docs/KRONIKA_ACCESS_INVENTORY.md
```

`docs/KRONIKA_ACCESS_INVENTORY.md` is included only because
`test_kronika_access_inventory.py` may regenerate it; if it changes, review the
diff and include it in the commit. It is not otherwise a correction target.

## Validation (targeted only; testing economy directive is binding)

Do not run the full suite. Do not re-run an unchanged gate. The four parked
pre-existing failures (stale `.venv` console script; three operator SSH-gate
parameters) stay out of scope, unrepaired and un-run.

1. `./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310` — exit 0 before editing and before the commit.
2. Regression-first: run
`tests/contract/test_kronika_approved_projection.py` and record the new test failing on the unfixed candidate (Red).
3. Implement the correction.
4. Targeted affected set through one declared-route `test-focus` invocation:

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

Add `tests/contract/test_companion_review_api.py` only if R7 edits the
suggestion/companion-review paths. If a listed file was not exercised by your
edits, still run it once; it is the affected neighborhood. A broad or full
suite is not required or authorized.

5. Inspect the final diff; confirm every changed path is allowlisted and the
correction is exactly the bounded fix.

## Git and commit

Git authority: stage and commit exactly the allowlisted files you changed; no
fetch, no push, no tag, no branch, no merge, no rebase, no reset, no clean,
no stash, no `git add -A`/`git add .`. Stage by explicit path list; inspect
`git diff --cached --check` (exit 0) and `git diff --cached --stat`; then one
local commit with subject:

```text
fix(kronika): serve approved projections on household reads
```

Report the resulting SHA, parent (`38e7beeb3921d7c0fd8e717e480754fbd18130c9`),
tree, subject, changed-path list and count, and post-commit
`git status --porcelain=v1 --untracked-files=all` (must be empty). No push;
publication is a separate Cooperator grant.

## Evidence envelope

Evidence tier: E3
Evidence tier basis: authorization-boundary runtime behavior on the household
read surface of the S6 candidate; the correction changes a security
trust-boundary behavior
Authorized implementation stages: regression-first (Red), correction
implementation, targeted affected test set, diff review, one local commit
Combined implementation envelope: allowed
Implementation stage gates: repository gate passes; regression fails first;
targeted set exits 0 after the fix; every changed path allowlisted
Independent acceptance: required-separate-fresh-worker (not this session)
Rollback or recovery checkpoint: the parent commit `38e7bee…` remains intact
and is the revert target; no worktree reset or clean is authorized
Activated stricter profile: none
Terminal implementation report point: the single local commit above

## Stopping conditions

Stop and report without improvisation on: repository-gate divergence (branch,
HEAD, parent, tree, AP pin, cleanliness); an edit needed outside the exact
allowlist; a regression that cannot be made to fail first or to pass after; a
targeted test that fails for a reason you cannot classify as this correction's
defect; any need for host, NUC, SSH, sudo, browser, provider, credential,
network or `private/**` access; any weakening of the authorization gate; any
schema, migration or dependency change; or an instruction conflict. Preserve
the first causal error; do not retry an unchanged failing gate.

## Completion and report contract

`PASS` means: the regression scenario is implemented, fails on the unfixed
candidate and passes after the fix; the targeted set exits 0; the approved
read behavior R2–R8 is implemented within the allowlist; and one local commit
exists with a clean post-commit worktree. Use
`Phase-qualified result: implementation-PASS` only for that result; otherwise
`not-applicable` and a truthful `PARTIAL`/`BLOCKED`.
`Logical-whole closure: not-closed`. `Report justification: new-mutation`.

Start the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 38, exchange 01) exactly once. Include: the
repository re-gate values; the Red/Green regression evidence; the exact
commands and exit statuses; the changed-path list; the commit SHA/parent/tree/
subject and post-commit status; the R2–R8 implementation summary including any
surface you could not exercise dynamically; R7's LEAD check result; deviations,
risks and missing evidence; one smallest next step (the fresh independent
E3/R3 re-audit); the compact critique block; and the authority-expiry
statement. Classify any pre-existing failure you encounter; do not repair it.

Finalize the report, save it at the exact destination below only if absent,
read it back in full, verify its first line, coordinates, content and path,
then send the separate short completion notice in Slovak (masculine address)
with status, path and SHA-256. Terminal report or cancellation expires this
authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 38_correction_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 38_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

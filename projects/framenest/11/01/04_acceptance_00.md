# Fresh Acceptance Worker - FrameNest web-client contract and testability convergence

## AP coordinates

```text
Logical whole identity: framenest-web-client-contract-and-testability-convergence
Worker role: WORKER
Worker profile: Fresh Acceptance Worker
Worker session target: fresh-worker-session
Worker session ordinal: 04
Worker exchange ordinal: 00
Native planning mode: not-required
Reasoning expectation: High
Acceptance authority: granted
Implementation authority: NOT granted
Source mutation authority: NOT granted
Commit authority: NOT granted
Push/publication authority: NOT granted
Deployment authority: NOT granted
Meta mutation authority: NOT granted
```

You are a genuinely fresh Acceptance Worker.

You did not participate in planning or implementation.

Your job is to independently determine whether the complete candidate for:

```text
framenest-web-client-contract-and-testability-convergence
```

satisfies its approved plan, implementation prompts, regression expectations and AP acceptance requirements.

Do not fix defects.

Do not modify project source.

Do not commit.

Do not push.

Do not deploy.

If acceptance evidence fails, return `acceptance-BLOCKED` with exact evidence.

---

# 1. Canonical project

Repository:

```text
/home/agile/Projects/framenest
```

Canonical origin:

```text
https://github.com/cisarik/framenest.git
```

Expected candidate HEAD:

```text
33946e08447dc92621ed6844b4b5d13a19ec29f1
```

Expected branch:

```text
feat/x-meme-browser-companion
```

Expected pinned AP:

```text
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

Expected logical-whole pre-implementation baseline:

```text
8c7858b62beca3c4ee92bb8f1f095b98063e2c94
```

These are orientation coordinates only.

Independently verify actual repository, Git and public state.

---

# 2. Governing AP

Read the root:

```text
AGENTS.md
```

and the governing AP documents referenced from the pinned `.ap`.

Before acceptance execute:

```text
./.ap/ap doctor
```

and the appropriate canonical AP project check.

Do not repair environmental mismatches.

If the repository itself is wrong, classify that as acceptance evidence.

If a disposable acceptance environment lacks something that the canonical project environment legitimately provides, distinguish environment failure from product failure.

---

# 3. Meta evidence chain

The Cooperator manually owns the Meta trace.

Expected logical-whole directory:

```text
/home/agile/meta/projects/framenest/11/01/
```

Read all of:

```text
01_planning_00.md
01_report_00.md

02_implementation_00.md
02_report_00.md

03_implementation_00.md
03_report_00.md

04_acceptance_00.md
```

Do not modify Meta.

Do not accept implementation reports as truth merely because they say PASS.

Use them as claims to verify against repository evidence.

The Cooperator will archive your terminal response manually as:

```text
04_report_00.md
```

---

# 4. Candidate commit chain

Expected commits after the logical-whole baseline are:

```text
0f4500ad7463d7428f377097aea224a268b321e2
Rebaseline FrameNest AP integration pin

6371bc00cb686c80e735330b308494ba552b94bc
Align metadata client-server validation contracts

1f355a8433331beef3410bf807b247a5b8155919
Replace metadata source assertions with behavior tests

fe5e38b8bfb986e68a9714d709267e3d19be1575
Retire test-only frontend artifacts

33946e08447dc92621ed6844b4b5d13a19ec29f1
Remove unreachable legacy library browser client
```

Independently verify ancestry and subjects.

Determine current public refs independently.

The candidate may legitimately be ahead of public state.

Acceptance does not require publication.

Do not push it.

---

# 5. Acceptance objective

The logical whole is acceptable only if the final candidate demonstrates all of the following:

1. Current AP consumer state is coherent.
2. Verified metadata client/server contract defects are corrected.
3. Cross-language parity is behaviorally executable.
4. Metadata validation tests no longer depend on source spelling where stronger behavioral coverage exists.
5. `MediaAnalysisRunId` parsing returns the correct domain type.
6. Test-only and unreachable frontend artifacts were removed without deleting live behavior.
7. The legacy development-library browser JavaScript was genuinely unreachable before deletion.
8. Protected current behavior remains intact.
9. Complete available Python and JavaScript suites are green.
10. No unauthorized UI/UX, backend, API, database, dependency or deployment changes entered the candidate.

Do not PASS based on test-green status alone.

Inspect architecture and diff semantics.

---

# 6. Gate A - baseline and Git integrity

Verify:

```text
repository root
branch
HEAD
worktree/index cleanliness
origin identity
local/public relationship
.ap gitlink
.ap checkout HEAD
AP doctor
AP project check
```

Expected final HEAD:

```text
33946e08447dc92621ed6844b4b5d13a19ec29f1
```

Expected `.ap`:

```text
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

Required:

```text
git status --short
```

must be empty before and after acceptance, aside from any AP-approved test artifacts that are demonstrably cleaned.

Acceptance must not mutate source or index.

---

# 7. Gate B - AP-pin consumer rebaseline

Inspect:

```text
tests/contract/test_ap_integration.py
README.md
docs/AP_UPGRADE_OBSERVATIONS.md
tests/contract/test_worker_execution_contract.py
```

Verify:

- active current-state assertions identify the actual pinned AP;
- historical AP observations were not falsely rewritten;
- the executable integration contract is green;
- no blanket SHA replacement corrupted historical evidence.

Run the focused AP integration contract tests.

---

# 8. Gate C - metadata client/server parity

Inspect:

```text
tests/support/metadata_field_contract_cases.json
tests/contract/test_metadata_field_contract_parity.py
tests/metadata_form_contract.test.js
```

The acceptance question is not merely whether these tests pass.

Verify that:

- the shared fixture contains meaningful acceptance/rejection cases;
- Python executes real backend/domain validation;
- JavaScript executes actual production validators from `app.js`;
- tests do not simply duplicate constants;
- tests do not fake client behavior in test-local reimplementations;
- client and server both consume the same behavioral case set.

At minimum confirm cases for:

```text
title:
240 code points accepted
241 rejected
240 astral code points accepted
241 astral rejected

controls:
C0
DEL
C1

description:
allowed newline
forbidden controls

tag display name:
C1 rejection

genres:
8 accepted
9 rejected
```

---

# 9. Gate D - F2 Unicode title correction

Inspect the actual production validator.

Verify the client counts Unicode code points rather than UTF-16 code units.

Verify that browser `maxlength="240"` no longer creates a conflicting UTF-16 contract on the relevant metadata title input.

Confirm that server-valid astral titles are not rejected merely because JavaScript `.length` counts surrogate pairs twice.

Do not infer from constants.

Execute behavior.

---

# 10. Gate E - F3 control-character correction

Compare actual frontend logic with backend semantics.

Verify C1 controls:

```text
U+0080 through U+009F
```

are rejected where backend `Cc` semantics reject them.

Verify existing intended description newline semantics remain intact.

Ensure the correction did not accidentally forbid legitimate description behavior.

---

# 11. Gate F - F4 genre-count correction

Verify:

```text
8 genres -> accepted
9 genres -> client validation error
```

before a failing server Save is required.

Confirm the UI uses the existing validation/status mechanism rather than introducing new layout/styling.

Confirm no API or backend limit was changed merely to satisfy the client.

---

# 12. Gate G - MediaAnalysisRunId correctness

Inspect:

```text
src/framenest/application/companion_review.py
```

and its regression test.

Verify the implicated parser returns:

```text
MediaAnalysisRunId
```

and not:

```text
MediaId
```

while retaining intended UUID/error validation.

The regression must test the actual type behavior, not only `.to_string()` equivalence.

Do not expand acceptance into a general identity-type audit.

---

# 13. Gate H - metadata source-test convergence

Inspect the changes in:

```text
tests/contract/test_local_web_application.py
```

from:

```text
8c7858b... through 1f355a8...
```

Verify source-text assertions were removed only where stronger executable behavior coverage exists.

Look particularly for the old patterns that pinned implementation spelling such as validator source fragments.

Confirm that security/static assertions whose contract is genuinely structural were preserved.

A reduction in source-scraping tests is good only if behavioral coverage replaces their meaningful guarantee.

---

# 14. Gate I - Slice 4a reachability and deletion

Independently inspect all important removed candidates.

At minimum verify deletion and former reachability for:

```text
COMPANION_REVIEW_INBOX_ENDPOINT
downloadIcon
mediaDownloadUrl
describeCatalogItem

buildProcessedTimeElement
openPlaybackDetails
resetMetadataWorkspaceAfterDiscard
ensureMetadataTagKey
metadataTagKeysFromSuggestion

applyMovieIdentificationToMetadataWorkspace
movieIdentificationHasLoadableFields
movieSuggestionFromResult
```

For each important family establish:

```text
former definition
former production callers
former test callers
current residual references
historical supersession where material
```

A grep result alone is not sufficient for ambiguous runtime behavior.

Check event listeners, callbacks, string dispatch, `window.*`, DOM references and host/extension integration where relevant.

Required current result for fully removed symbols:

```text
0 obsolete production references
0 obsolete test references
```

---

# 15. Gate J - movie-identification behavior preservation

This area requires particular care because old movie helpers were removed while one live helper had to remain.

Verify:

```text
movieIdentificationIsPureUnknown
```

still exists and has a live production caller.

Verify:

```text
applyAnalysisStatusPayload
```

continues to distinguish the necessary states.

Inspect behavior tests, not only symbol presence.

Verify the deleted:

```text
metadataDurableAnalysis.movieResult
```

property was genuinely write-only and that removing it did not remove the local temporary `movieResult` needed for status processing.

Confirm no live suggestion-strip behavior was deleted.

---

# 16. Gate K - legacy library-browser reachability

Independently verify the central Slice 4b premise.

At the pre-deletion commit:

```text
1f355a8433331beef3410bf807b247a5b8155919
```

establish whether the legacy development-library browser could execute.

Verify the former HTML state:

```text
#library-list absent
#library-card-template absent
```

and history around:

```text
db665e7
```

if relevant.

Confirm the former startup:

```text
loadLibraries();
```

could only reach a function that immediately returned because required DOM anchors did not exist.

Also inspect:

```text
extension/
companion_host.js
dynamic selector construction
global/window exposure
```

for any supported mechanism capable of recreating/reaching the supposedly dead surface.

Acceptance requires confidence that the deleted dependency cone was unreachable in the packaged current application.

---

# 17. Gate L - shared/live dependency preservation

The implementation prompt explicitly warned that dead-cluster dependencies could also be shared.

Verify the final candidate still preserves every shared/live artifact it needs.

At minimum inspect:

```text
LIBRARIES_ENDPOINT
movieIdentificationIsPureUnknown
mediaContentUrl
mediaGalleryPreviewUrl
mediaCoverThumbnailUrl
cover timeline/frame/mutation endpoints
openOriginalIcon
editIcon
applyAnalysisStatusPayload
movieIdentificationStatusMessage
```

In particular, `LIBRARIES_ENDPOINT` was intentionally retained because the implementation prompt treated the catalog-card preview cluster as live.

Do not fail this candidate merely because Worker 03 later found evidence that this separate preview cluster may itself now be dead.

That is a newly discovered residual, not part of the authorized Slice 4 deletion.

However, independently confirm that Worker 03 did not delete it while it was protected.

---

# 18. Gate M - test retirement quality

The raw test count dropped intentionally.

Expected implementation report:

```text
Python:
3392 -> 3381 passed
11 tests retired

JavaScript:
461 -> 460 passed
1 test retired
```

Do not treat fewer tests as automatically bad or automatically good.

Inspect removed tests and classify them.

PASS requires that retired tests exclusively protected:

```text
unreachable functionality
test-only production artifacts
removed source structure
```

or that any surviving meaningful guarantee was migrated into another live behavioral assertion.

Pay particular attention to:

```text
tests/movie_identification_frontend.test.js
tests/contract/test_local_web_application.py
tests/catalog_card_ai_quick_action.test.js
tests/browser_movie_identification_evidence.test.js
tests/tailscale_identity_frontend.test.js
```

For the Tailscale mutation test, explicitly review the change from an exact mutation-site count to:

```text
mutationSites.length > 0
mutationSites.length === wrappedSites.length
```

Determine whether this remains a stronger semantic safety property after legitimate deletion of mutation sites.

Do not reject it merely because the numeric count changed.

---

# 19. Gate N - complete regression execution

Run the complete JavaScript suite:

```text
node --test tests/*.test.js
```

Required:

```text
0 fail
```

The established candidate evidence is:

```text
460 pass
5 skipped
0 fail
```

Five documented gated browser tests may remain skipped if the required real-browser acceptance gate is legitimately disabled in the standard environment.

Run the complete Python suite through the canonical AP route:

```text
./.ap/ap exec \
  --root /home/agile/Projects/framenest \
  --baseline 8c7858b62beca3c4ee92bb8f1f095b98063e2c94 \
  --operation test-focus \
  -- tests -q -p no:cacheprovider
```

or the exact AP-correct equivalent established from current project configuration.

Required:

```text
0 failed
```

Expected approximate result:

```text
3381 passed
8 skipped
```

Do not require exact pass counts if collection legitimately differs for an explainable reason, but investigate meaningful differences.

Run focused parity and implicated frontend suites separately so a green full suite cannot hide collection gaps.

---

# 20. Gate O - candidate diff boundary

Inspect:

```text
git diff 8c7858b62beca3c4ee92bb8f1f095b98063e2c94..33946e08447dc92621ed6844b4b5d13a19ec29f1
```

and also separate implementation-session boundaries:

```text
8c7858b..1f355a8
1f355a8..33946e0
```

Confirm the logical whole did not introduce unauthorized changes to:

```text
styles.css
visual layout
frontend framework
TypeScript/bundling
backend API behavior outside F13
database/schema
migrations
dependencies
deployment configuration
NUC state
VPS state
```

For Slice 4 specifically expected touched surface is only:

```text
src/framenest/adapters/api/web/app.js
tests/
```

Worker 03 reported:

```text
6 files changed
38 insertions
1323 deletions
```

Verify this independently.

---

# 21. Gate P - before/after architecture evidence

Verify the reported final frontend reduction is plausible and accurately classified.

Reported:

```text
app.js:
12,780 -> 11,810 lines

top-level functions:
564 -> 515

49 top-level functions removed
0 top-level functions added
```

Do not PASS based on line-count reduction.

Instead answer:

> Did the deletion simplify the production client because unreachable/test-only behavior was removed, without changing supported user-visible behavior?

That is the acceptance criterion.

---

# 22. Known newly discovered residuals

Worker 03 reported several findings outside its deletion authority.

Acceptance must classify them but not fix them.

## R1 - catalog-card-preview cluster

Worker 03 claims the following cluster may itself now be unreachable:

```text
handleCardPreview
selectPreviewableLocation
getCachedPreview
setCachedPreview
renderCardPreviewState
renderCardPreviewFrames
startCardPreviewCycling
decodeBase64Png
```

and that its former caller disappeared in:

```text
a15dfef
feat: make gallery playback content-first
```

This potentially changes the future disposition of:

```text
LIBRARIES_ENDPOINT
```

because the endpoint constant may then have no live client consumer.

For this acceptance:

- verify Worker 03 did not delete this protected cluster;
- optionally validate the residual claim read-only;
- do not expand current acceptance into implementing its deletion;
- record whether it deserves a separate bounded follow-up.

## R2 - `metadataDurableAnalysis.result`

Reported write-only.

Do not fix.

## R3 - `previewObjectUrls` / `revokePreviewObjectUrls`

Reported to have no remaining producer after Slice 4.

Do not fix.

## R4 - dead legacy CSS

Reported remaining `.library-*` selectors.

Explicitly outside current implementation.

Do not fix.

These residuals do not by themselves block acceptance unless they prove the accepted implementation deleted a live dependency or left the candidate internally inconsistent.

---

# 23. Security and regression review

Explicitly inspect whether this logical whole changed:

```text
mutation-header coverage
HTML insertion safety
external URL policy
persistent storage rules
metadata Save semantics
AI analysis status semantics
backend request validation
Tailscale identity behavior
```

The correct result is primarily preservation plus the intended validation convergence.

Any security-property weakening is blocking.

---

# 24. Acceptance decision

Return `acceptance-PASS` only if all material gates pass.

Return `acceptance-BLOCKED` if any of these occur:

```text
full required suite is red
candidate is dirty or differs from reviewed commit
client/server parity remains divergent
new parity tests do not execute real production behavior
MediaAnalysisRunId is still typed incorrectly
deleted frontend code still has a supported live caller
legacy library surface was actually reachable
live movie-identification behavior regressed
test retirement removed a meaningful guarantee without replacement
security/static safety property was weakened
unauthorized source/API/schema/dependency/UI work entered the candidate
```

Minor report-format defects or historical prose issues that do not affect repository correctness should be recorded as non-blocking observations rather than inventing implementation failure.

---

# 25. No publication

Even if acceptance passes:

```text
DO NOT PUSH
DO NOT MERGE
DO NOT DEPLOY
```

Publication is a separate phase.

Acceptance authority ends with the report.

---

# 26. Terminal report

Return a complete report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Do not put any preamble before that heading.

The Cooperator will archive the full response as:

```text
04_report_00.md
```

Include standard AP coordinates:

```text
Logical whole identity
Worker session ordinal
Worker exchange ordinal
Worker session target
Native planning mode
Standard terminal status
Phase-qualified result
Candidate commit
Candidate parent/baseline
Logical-whole closure
Report justification
Authority expiry
```

Then provide:

## Verified candidate

Exact:

```text
HEAD
branch
public refs
local/public relationship
worktree/index state
.ap gitlink
.ap HEAD
doctor
project check
```

## Evidence-chain review

State that you read and reconciled:

```text
01 planning/report
02 implementation/report
03 implementation/report
```

and identify any contradiction.

## Commit-chain review

Verify all five expected commits and their ancestry.

## Acceptance matrix

Give an explicit verdict for Gates A through P:

```text
PASS
BLOCKED
NOT-APPLICABLE
```

with concise evidence for each.

## Contract correctness

Report independently verified behavior for F2/F3/F4/F13.

## Test architecture

Explain whether the parity mechanism genuinely executes both languages and whether source-text assertions were appropriately retired.

## Slice 4 reachability

Summarize independent evidence for:

```text
Slice 4a
movie-identification path
metadataDurableAnalysis.movieResult
legacy library browser cone
```

## Preserved live behavior

Explicitly report status of:

```text
movieIdentificationIsPureUnknown
LIBRARIES_ENDPOINT
mutation-header invariant
metadata parity
```

## Validation

Give exact results for:

```text
focused Python
focused JavaScript
full Python
full JavaScript
ap doctor
ap project check
git diff --check
residual searches
```

## Diff boundary

Report changed files and confirm absence/presence of:

```text
styles.css
index.html changes beyond authorized earlier metadata fix
backend/API changes
schema/migrations
dependencies
deployment
```

## Test retirement assessment

State whether the reduction in test count is justified.

## Residuals

Classify R1-R4 and any newly discovered issue as:

```text
future-whole
parked
false-positive
blocking
```

Do not implement them.

## Acceptance verdict

End with exactly one:

```text
acceptance-PASS
acceptance-BLOCKED
```

If PASS, state explicitly that:

```text
the implementation candidate is accepted
the logical whole is not yet publication-closed
publication/deployment authority was not granted
```

All Acceptance Worker authority expires at the terminal report.
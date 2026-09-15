# Fresh Implementation Worker - FrameNest dead/test-only frontend artifact retirement

## AP coordinates

```text
Logical whole identity: framenest-web-client-contract-and-testability-convergence
Worker role: WORKER
Worker profile: Implementation Worker
Worker session target: fresh-worker-session
Worker session ordinal: 03
Worker exchange ordinal: 00
Native planning mode: not-required
Reasoning expectation: High
Implementation authority: granted, strictly bounded by this prompt
Local Git commit authority: granted
Push/publication authority: NOT granted
Deployment authority: NOT granted
Meta mutation authority: NOT granted
```

You are a genuinely fresh Implementation Worker.

This is the second bounded implementation session of an already planned logical whole.

Do not reopen broad planning.

Do not perform UI/UX polish.

Do not redesign the frontend.

Do not interpret this prompt as authority for a general dead-code sweep.

Your responsibility is to complete only the previously approved Slice 4:

```text
Slice 4a - proven test-only / zero-caller frontend artifacts
Slice 4b - proven unreachable legacy development-library frontend cluster
```

The primary objective is not maximum deletion.

The objective is to remove production JavaScript that is demonstrably unreachable or exists solely because tests preserve it, while protecting all live FrameNest behavior.

When evidence is ambiguous, retain the code and report the ambiguity.

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

Expected starting state from the accepted previous implementation:

```text
branch:
feat/x-meme-browser-companion

expected local HEAD:
1f355a8433331beef3410bf807b247a5b8155919

expected pinned AP:
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

The previous implementation created exactly these commits after the earlier baseline:

```text
0f4500ad7463d7428f377097aea224a268b321e2
Rebaseline FrameNest AP integration pin

6371bc00cb686c80e735330b308494ba552b94bc
Align metadata client-server validation contracts

1f355a8433331beef3410bf807b247a5b8155919
Replace metadata source assertions with behavior tests
```

These coordinates are orientation only.

Independently establish current repository and public truth before mutation.

Verify at minimum:

```text
repository root
current branch
HEAD
worktree/index cleanliness
canonical origin
relevant public refs
local/public relationship
.ap gitlink
.ap checkout HEAD
./.ap/ap doctor
```

Do not push anything.

Do not publish anything.

Do not deploy anything.

---

# 2. Governing AP

Read the root:

```text
AGENTS.md
```

and the governing documents it references from the pinned `.ap`.

Run:

```text
./.ap/ap doctor
```

before mutation.

Use the canonical AP execution route for Python validation.

Do not bypass AP testing because direct invocation looks easier.

---

# 3. Authoritative Meta context

The Cooperator owns Meta mutation manually.

You may read but must not modify `/home/agile/meta`.

The logical-whole trace is expected under:

```text
/home/agile/meta/projects/framenest/11/01/
```

Read at minimum:

```text
01_planning_00.md
01_report_00.md
02_implementation_00.md
02_report_00.md
03_implementation_00.md
```

The previous implementation report is accepted by ORCHESTRATOR_CHAT as:

```text
implementation-PASS
```

for Slices 0, 1, 2 and 3.

Do not revisit those slices except to preserve their behavior.

The Cooperator will archive your terminal response manually as:

```text
03_report_00.md
```

Do not write that file yourself.

---

# 4. Accepted current baseline

The preceding implementation established executable client/server parity protection.

Do not weaken or remove it.

The exact current tree contains:

```text
tests/support/metadata_field_contract_cases.json
tests/contract/test_metadata_field_contract_parity.py
tests/metadata_form_contract.test.js
```

The accepted terminal evidence from Worker 02 was:

```text
Full Python:
3392 passed
8 skipped
0 failed

Full JavaScript:
461 passed
5 skipped
0 failed

Metadata parity Python:
35 passed

Metadata parity JavaScript:
35 passed
```

ORCHESTRATOR_CHAT independently reconstructed the committed bundle and confirmed:

```text
./.ap/ap doctor
PASS

node --test tests/metadata_form_contract.test.js
35 pass
0 fail

node --test tests/*.test.js
461 pass
0 fail
5 skipped
```

Treat these behavioral tests as protection for live metadata functionality during deletion.

---

# 5. Core implementation rule

Deletion authority applies only when reachability has been demonstrated, not inferred from aesthetics.

For every candidate production symbol or state field:

1. Perform whole-word repository searches across at least:

```text
src/
tests/
extension/
```

2. Inspect:

```text
direct calls
event-listener registration
callbacks
string references
window/global exposure
template references
HTML anchors
dynamic dispatch
browser-host integration
tests
```

3. Use `git log -S` / `git show` when history is needed to determine whether the artifact was superseded intentionally.

4. Classify it before deletion as one of:

```text
production-live
production-indirect
test-only-production-artifact
unreachable-production-artifact
shared-dependency
uncertain
```

5. Delete only:

```text
test-only-production-artifact
unreachable-production-artifact
```

6. If classification is `uncertain`, retain it and report it.

A production symbol may not be deleted simply because `rg` reports one source occurrence.

---

# 6. Slice 4a - proven zero-caller and test-only artifacts

The Planner and ORCHESTRATOR_CHAT independently rechecked the following candidates on HEAD `1f355a843333...`.

They remain candidates, not blind deletion instructions.

## 6.1 Pure zero-caller candidates

Current evidence shows production definition only and no production callers for:

```text
COMPANION_REVIEW_INBOX_ENDPOINT
downloadIcon
mediaDownloadUrl
describeCatalogItem
```

Current observed reference shapes include:

```text
COMPANION_REVIEW_INBOX_ENDPOINT
definition only

downloadIcon
definition only

describeCatalogItem
definition only

mediaDownloadUrl
definition plus tests that explicitly assert it is NOT used
```

Independently verify these facts.

If still true, remove the production artifacts and retire only tests whose sole purpose was to preserve or negatively describe those dead artifacts.

Do not disturb the live:

```text
mediaContentUrl
mediaGalleryPreviewUrl
mediaCoverThumbnailUrl
cover timeline/frame/mutation URLs
openOriginalIcon
editIcon
```

or their callers.

---

## 6.2 Test-only production helpers

Current evidence shows definitions with no production caller, but tests directly extract or inspect them:

```text
buildProcessedTimeElement
openPlaybackDetails
resetMetadataWorkspaceAfterDiscard
metadataTagKeysFromSuggestion
```

Independently verify each.

If a helper exists only so tests can execute or inspect it, remove both:

```text
the production helper
the obsolete test contract preserving it
```

Do not migrate a meaningless test just to preserve the deleted implementation shape.

Before deleting a test, determine whether it contains any independent live guarantee.

If it does, preserve that guarantee through the live implementation rather than deleting it wholesale.

---

# 7. Superseded movie-identification apply path

Current evidence strongly indicates that an old "load the entire movie identification into the draft" path was superseded by the durable per-field suggestion-strip workflow.

Candidate functions:

```text
applyMovieIdentificationToMetadataWorkspace
movieIdentificationHasLoadableFields
movieSuggestionFromResult
```

Observed current production reference state at `1f355a843333...`:

```text
applyMovieIdentificationToMetadataWorkspace
production definition only
tests call/extract it

movieSuggestionFromResult
production definition only
tests call/extract it

movieIdentificationHasLoadableFields
called only by movieSuggestionFromResult
tests call/extract it
```

History previously identified commit:

```text
6b957be
```

as the transition toward per-field AI suggestion application.

Independently verify that history and the current live path before deletion.

Important protection:

```text
movieIdentificationIsPureUnknown
```

is still production-live.

It is used by:

```text
applyAnalysisStatusPayload
```

and must remain unless independent evidence proves otherwise.

Do not delete it merely because neighboring old functions are removed.

Retire obsolete tests in:

```text
tests/movie_identification_frontend.test.js
```

only where they exercise the deleted path.

Preserve tests covering live movie-identification behavior, including the current:

```text
movieIdentificationIsPureUnknown
durable analysis status
suggestion-strip behavior
catalog-card AI quick action
```

---

# 8. `metadataDurableAnalysis.movieResult` write-only state

The current state object contains a `movieResult` property in several initialization/reset/result objects.

ORCHESTRATOR_CHAT independently searched the exact current tree and found no production read of:

```text
metadataDurableAnalysis.movieResult
```

The only direct property reference outside object construction was in:

```text
tests/browser_movie_identification_evidence.test.js
```

where the test manually writes the state field.

However, local variable:

```text
movieResult
```

inside `applyAnalysisStatusPayload` is production-live because it validates the returned movie-identification payload and feeds:

```text
movieIdentificationIsPureUnknown
movieIdentificationStatusMessage
```

Therefore distinguish carefully:

```text
metadataDurableAnalysis.movieResult property
```

from:

```text
local movieResult validation variable
```

If independent analysis confirms the state property is truly write-only:

- remove the property from durable state object shapes;
- stop returning/storing it from `applyAnalysisStatusPayload`;
- retain whatever local temporary variable is required for result validation and status calculation;
- update or retire the browser test that manually seeds the obsolete property.

Do not degrade movie-identification status handling.

---

# 9. Slice 4b - unreachable legacy development-library frontend

This is the larger deletion and requires stronger proof.

The old browser contained a standalone development library browser / local scan / editable AI review surface.

The current `index.html` no longer contains:

```text
#library-list
#library-card-template
```

ORCHESTRATOR_CHAT independently confirmed both are absent from the current HTML.

Current JavaScript still contains:

```text
const libraryList = document.querySelector("#library-list");
const libraryCardTemplate = document.querySelector("#library-card-template");
```

and startup still calls:

```text
loadLibraries();
```

but current `loadLibraries()` begins:

```javascript
if (!libraryList || !libraryCardTemplate) return;
```

Therefore the current startup path immediately returns.

The Planner's history investigation identified:

```text
db665e7
fix: apply rendered acceptance feedback
```

as the commit that intentionally removed this browser surface from the rendered HTML while leaving much of its JavaScript behind.

Verify this history independently.

The deletion should remove the unreachable frontend dependency cone rooted exclusively in this removed surface.

Candidate functions include, but are not limited to:

```text
loadLibraries
renderLibraries
showLibraryState
handlePreviewClick
prepareAiControls
handleAnalyzeClick
renderEditableReview
validateReview
renderAnalysisSuccess
renderScanResult
handleInspectClick
handleImportClick
previewElements
aiElements
resetAiReview
resetLocalPreview
```

There are additional helper functions used solely by that cluster.

Discover them from the actual dependency graph rather than treating this list as exhaustive.

---

# 10. Critical shared-code warning

Do not equate "used by legacy cluster" with "safe to delete globally".

Some constants/helpers are shared with live FrameNest functionality.

A concrete verified example:

```text
LIBRARIES_ENDPOINT
```

must currently remain.

Although the dead development-library cluster uses it, the current live catalog card preview path also uses:

```javascript
fetch(`${LIBRARIES_ENDPOINT}/${location.libraryId}/media-analysis-preview`, ...)
```

inside the production-live card-preview workflow.

Therefore:

```text
DO NOT delete LIBRARIES_ENDPOINT
```

unless the live use is independently replaced by an equivalent live constant as part of the smallest necessary edit.

There is no need to rename or relocate it in this task.

Likewise, every helper transitively used by any live feature remains outside deletion authority.

---

# 11. Backend endpoints are explicitly not Slice 4

The removed browser surface does not imply that its backend capabilities are dead.

Do not remove or modify backend routes such as:

```text
/api/libraries
scan-preview
media-analysis-preview
media-suggestion-preview
media-imports
```

merely because the legacy HTML surface disappeared.

Some are used by:

```text
live catalog preview
CLI/operator flows
tests
other non-rendered surfaces
```

Backend endpoint retirement is not authorized.

No router, application service, repository, domain type or API schema should be deleted as part of Slice 4 unless an unavoidable compile failure proves a direct mechanical dependency from an authorized frontend deletion.

If that occurs, stop and report rather than broadening scope.

---

# 12. CSS is not part of this implementation

The current stylesheet still contains historical library-related selectors such as:

```text
.library-list
```

Do not clean them in this Worker.

Do not modify:

```text
styles.css
```

Dead CSS can be assessed later during UI/UX polish or a separately authorized style cleanup.

This implementation is about production JavaScript and the tests that artificially preserve it.

---

# 13. No general app.js modularization

Even after deletion, `app.js` remains large.

That is not authority to:

```text
split it into modules
introduce imports/exports
add a bundler
add TypeScript
introduce React/Vue/Svelte
rename broad function families
reformat the entire file
move unrelated constants
rewrite fetch architecture
```

Keep the diff surgically focused on removing proven dead/test-only paths.

A smaller `app.js` is an outcome, not the acceptance criterion.

---

# 14. Test-retirement rules

Tests are not automatically correct merely because they exist.

For each test affected by deletion, classify what it actually protects.

A test may be removed when it exclusively:

```text
asserts that a dead function exists
extracts a dead function and tests unreachable behavior
asserts source spelling for unreachable behavior
preserves a removed DOM surface
```

A test must remain or be rewritten when it protects:

```text
live behavior
security property
API contract
absence of unsafe rendering
current metadata suggestion behavior
current catalog-card behavior
current movie-identification status
current browser integration
```

Avoid replacing dead source-text assertions with equivalent dead behavioral tests.

Deletion is allowed to reduce the raw test count when the removed tests exercised no reachable product behavior.

Report that reduction explicitly.

---

# 15. Expected touched files

The intended primary mutation surface is:

```text
src/framenest/adapters/api/web/app.js

tests/contract/test_local_web_application.py
tests/movie_identification_frontend.test.js
tests/catalog_card_ai_quick_action.test.js
tests/browser_movie_identification_evidence.test.js
```

Not every listed test file necessarily needs modification.

Touch only files causally required by actual deletions.

Additional frontend test files may be edited only when they directly reference deleted artifacts.

Any change outside:

```text
src/framenest/adapters/api/web/app.js
tests/
```

requires explicit causal justification.

Changes to the following are presumptively out of scope:

```text
src/framenest/adapters/api/web/styles.css
src/framenest/adapters/api/web/index.html
pyproject.toml
database migrations
API schema files
backend routers
domain/application code
.ap
README.md
```

Do not touch them merely for cleanup consistency.

---

# 16. Required pre-deletion evidence

Before editing production code, create a reference census in your working notes/report.

For every proposed symbol deletion record:

```text
symbol
definition location
production call/reference count
test reference count
HTML/template reference state
global/window exposure state
history evidence where needed
final classification
```

For the legacy library cluster additionally establish:

```text
the only external runtime root(s)
why those roots cannot become live with current packaged HTML
whether companion_host.js or extension code can inject/recreate the missing anchors
whether any dynamic query/selector could reach the old classes
which helpers are shared outside the cluster
```

Do not commit a generated census file unless it belongs naturally in the project.

The terminal report is sufficient evidence storage.

---

# 17. Suggested implementation slicing

Use two green local commits if evidence supports both slices.

## Commit A - Slice 4a

Suggested subject:

```text
Retire test-only frontend artifacts
```

It should contain only independently proven:

```text
zero-caller helpers
test-only helpers
superseded movie apply helpers
write-only durable movieResult state
associated obsolete tests
```

Run focused and complete validation before moving to Slice 4b.

## Commit B - Slice 4b

Suggested subject:

```text
Remove unreachable legacy library browser client
```

It should contain:

```text
unreachable library-browser dependency cone
startup loadLibraries call
obsolete library-browser test expectations
```

while retaining all shared/live helpers and all backend endpoints.

If Slice 4a passes but Slice 4b becomes ambiguous or blocked, do not force completion.

A legitimate terminal result may be:

```text
implementation-PARTIAL
```

with Slice 4a committed cleanly and Slice 4b left untouched.

Do not sacrifice confidence merely to achieve two commits.

---

# 18. Required focused validation

Resolve `<BASELINE>` from the independently verified session start commit.

Run:

```text
./.ap/ap doctor
```

and:

```text
./.ap/ap project check \
  --root /home/agile/Projects/framenest \
  --baseline <BASELINE>
```

Keep the metadata parity mechanism green:

```text
node --test tests/metadata_form_contract.test.js
```

and:

```text
./.ap/ap exec \
  --root /home/agile/Projects/framenest \
  --baseline <BASELINE> \
  --operation test-focus \
  -- tests/contract/test_metadata_field_contract_parity.py \
     -q -p no:cacheprovider
```

Run relevant focused frontend tests after each slice.

At minimum inspect/run those implicated by actual edits, expected to include appropriate subsets of:

```text
tests/contract/test_local_web_application.py
tests/movie_identification_frontend.test.js
tests/catalog_card_ai_quick_action.test.js
tests/browser_movie_identification_evidence.test.js
```

Gated real-browser tests that cannot run because their documented prerequisite is unavailable may remain skipped only if that matches the established accepted baseline.

---

# 19. Full validation gate

Before terminal PASS run the complete JavaScript suite:

```text
node --test tests/*.test.js
```

Required result:

```text
0 failed
```

Skipped gated browser evidence may remain only at the legitimate established level or lower.

Run the complete Python suite through AP:

```text
./.ap/ap exec \
  --root /home/agile/Projects/framenest \
  --baseline <BASELINE> \
  --operation test-focus \
  -- tests -q -p no:cacheprovider
```

Required result:

```text
0 failed
```

A lower total test count is permitted if and only if the terminal report maps each removed test to deleted unreachable/test-only functionality.

Do not compensate for deleted tests by inventing meaningless replacements.

---

# 20. Residual-reference gate

For every deleted production symbol perform exact residual searches.

Required terminal state for a fully deleted symbol:

```text
0 production references
0 obsolete test references
```

For deleted legacy library UI anchors verify that no JavaScript startup path continues to reference their deleted frontend machinery.

Also explicitly prove after deletion that protected live symbols remain.

At minimum verify:

```text
movieIdentificationIsPureUnknown
```

still exists and remains live.

Verify:

```text
LIBRARIES_ENDPOINT
```

still exists if required by the live catalog-card preview path.

Verify the live metadata parity suite still executes the real current validators.

---

# 21. Diff safety gate

Before final report inspect:

```text
git diff <BASELINE>..HEAD --stat
git diff <BASELINE>..HEAD
git status --short
```

Confirm:

```text
no styles.css change
no index.html change
no backend/API change
no migration
no dependency change
no .ap change
no Meta mutation
no UI/UX redesign
```

The final FrameNest worktree/index must be clean.

Do not push.

Do not deploy.

---

# 22. Quantitative before/after evidence

Because this slice is specifically removing dead frontend mass, report useful before/after measurements for:

```text
app.js line count
top-level function count if practical
number of deleted production functions/constants/state fields
number of retired tests
```

Do not optimize against these numbers.

They are evidence of what was removed, not goals.

---

# 23. Stop conditions

Stop rather than improvise if:

```text
current baseline materially differs from expected state
unexpected unrelated worktree mutation exists
a candidate has a plausible production/dynamic caller
removing the legacy cluster requires backend/API deletion
the removed HTML anchors can be recreated by a supported runtime host
full validation reveals unexplained regressions
the task expands into UI redesign or architecture migration
```

When one individual candidate is ambiguous, retaining that candidate does not necessarily block the rest of the slice.

Classify it and continue with independently proven deletions.

---

# 24. Terminal report

Return a complete terminal report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

The Cooperator will archive the complete response as:

```text
03_report_00.md
```

Include the standard AP coordinates:

```text
Logical whole identity
Worker session ordinal
Worker exchange ordinal
Worker session target
Native planning mode
Standard terminal status
Phase-qualified result
Start commit
End commit
Result commit(s)
Logical-whole closure
Report justification
Authority expiry
```

Then include these sections.

## Verified baseline

Report:

```text
HEAD
branch
worktree/index
public refs
local/public relationship
.ap gitlink
.ap HEAD
ap doctor
project check
```

## Slice 4a census

For each candidate provide:

```text
symbol
classification
production references
test references
history evidence if relevant
action taken
```

Explicitly distinguish retained ambiguous symbols from deleted ones.

## Movie-identification path

Report exactly what was removed and what remained live.

Explicitly state the status of:

```text
applyMovieIdentificationToMetadataWorkspace
movieIdentificationHasLoadableFields
movieSuggestionFromResult
movieIdentificationIsPureUnknown
metadataDurableAnalysis.movieResult
```

## Slice 4b reachability proof

Document:

```text
missing HTML anchors
startup root
loadLibraries early-return condition
history evidence
dependency-cone analysis
shared helpers/constants intentionally retained
```

Explicitly explain why the removed frontend code could not execute in the packaged current application.

## Tests retired

For every removed test or assertion state:

```text
what it previously tested
why that behavior was unreachable/test-only
whether any live guarantee remained
how that live guarantee is still protected
```

## Validation

Give exact results for:

```text
ap doctor
ap project check
metadata parity JS
metadata parity Python
focused JS/Python tests
full JS
full Python
residual-reference searches
```

## Before/after

Report:

```text
app.js lines
function count if measured
production artifacts removed
tests retired
```

## Git result

Provide:

```text
all commit SHAs + subjects
final HEAD
git status --short
git diff <BASELINE>..HEAD --stat
```

State explicitly:

```text
no push performed
no publication performed
no deployment performed
Meta was not mutated
no UI/UX polish performed
no backend/API/schema migration performed
```

## Residuals

Record any candidate retained due to uncertainty and any newly discovered related debt.

Do not fix unrelated findings.

End with exactly one phase-qualified result:

```text
implementation-PASS
implementation-PARTIAL
implementation-BLOCKED
```

A PASS means both Slice 4a and Slice 4b were completed with demonstrated reachability/deletion evidence and all required validation green.

All authority from this prompt expires at the terminal report.
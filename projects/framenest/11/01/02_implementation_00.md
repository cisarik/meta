# Fresh Implementation Worker — FrameNest web-client contract and testability convergence

## AP coordinates

```text
Logical whole identity: framenest-web-client-contract-and-testability-convergence
Worker role: WORKER
Worker profile: Implementation Worker
Worker session target: fresh-worker-session
Worker session ordinal: 02
Worker exchange ordinal: 00
Native planning mode: not-required
Reasoning expectation: High
Implementation authority: granted, bounded by this prompt
Local Git commit authority: granted
Push/publication authority: NOT granted
Deployment authority: NOT granted
Meta mutation authority: NOT granted
```

You are a genuinely fresh Implementation Worker.

You are implementing an already approved, independently researched plan.

Do not reopen broad product planning.

Do not perform UI/UX polish.

Do not expand the task into a general FrameNest refactor.

Your responsibility is to implement only the bounded slices defined below, preserve evidence of the defects before fixing them, leave the FrameNest repository in a clean committed state, and return a precise terminal report to `ORCHESTRATOR_CHAT`.

The Cooperator manually owns the Meta trace repository during ChatOrchestrator-led development.

Therefore:

- you may **read** the relevant Meta planning/report documents;
- you must **not write or commit anything in `/home/agile/meta`**;
- return your complete report in chat;
- the Cooperator will archive it manually as `02_report_00.md`.

---

# 1. Authoritative project

Canonical repository:

```text
/home/agile/Projects/framenest
```

Canonical remote:

```text
https://github.com/cisarik/framenest.git
```

Expected starting project state from the approved Planner:

```text
branch:
feat/x-meme-browser-companion

expected local baseline:
8c7858b62beca3c4ee92bb8f1f095b98063e2c94

expected public origin/main:
a4193d4f520a30aafa333987f2e6b846a5425d27

expected public origin/feat/x-meme-browser-companion:
a4193d4f520a30aafa333987f2e6b846a5425d27

expected pinned AP:
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

These are orientation coordinates, not permission to assume reality.

Independently establish current truth before mutation.

At minimum verify:

```text
repository root
current branch
HEAD
worktree/index cleanliness
origin
relevant public refs
local/public ancestry
.ap gitlink
.ap checkout HEAD
./.ap/ap doctor
```

The expected baseline has one local-only FrameNest commit containing the AP gitlink update.

Do not push that commit.

Do not publish anything during this Worker session.

---

# 2. Governing AP

Read:

```text
AGENTS.md
```

at the FrameNest repository root and all governing documents it references from the pinned `.ap`.

Run:

```text
./.ap/ap doctor
```

before implementation.

Use the canonical AP execution route for Python tests.

Do not bypass AP simply because direct `.venv/bin/pytest` appears easier.

The approved Planner observed:

```text
Python:
1 failed, 3356 passed, 8 skipped

failure:
tests/contract/test_ap_integration.py::
test_ap_submodule_gitlink_and_configuration_are_pinned

JavaScript:
426 pass, 0 fail, 5 skipped
```

The single Python failure is a known prerequisite defect caused by the AP pin update.

If your independently observed baseline materially differs, classify it before implementing.

Do not silently repair unrelated failures.

---

# 3. Planning artifacts

The Cooperator has archived the approved planning exchange in the current logical-whole directory in Meta as:

```text
01_planning_00.md
01_report_00.md
```

Read them if available.

`01_report_00.md` is the detailed Planner report and evidence register.

This prompt intentionally narrows that plan.

Where this implementation prompt conflicts with optional sequencing suggested by the Planner, **this prompt controls the implementation session**.

Do not mutate Meta.

---

# 4. Scope of this Worker session

This Worker implements only:

```text
Slice 0
Slice 2 RED evidence
Slice 1 production corrections
Slice 2 GREEN parity mechanism
Slice 3 metadata-form test convergence
```

In practical execution order:

```text
0 → 2(RED) → 1 → 2(GREEN) → 3
```

The ordering is intentional.

The parity tests must expose the existing defects **before** production code is changed.

Do not perform Slice 4.

Specifically, do not remove:

```text
legacy development-library cluster
movie-identification dead path
zero-caller frontend helpers
test-only frontend helpers
write-only movieResult state
```

Those are reserved for a separate fresh Implementation Worker after ChatOrchestrator reviews this candidate.

---

# 5. Explicitly verified defects being implemented

## F1 — stale executable AP pin expectation

Current `.ap` is expected at:

```text
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

while active integration expectations still reference:

```text
7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
```

Expected active locations include:

```text
tests/contract/test_ap_integration.py
README.md
```

Historical references must not be globally replaced.

In particular, inspect and preserve truthful historical evidence in:

```text
docs/AP_UPGRADE_OBSERVATIONS.md
tests/contract/test_worker_execution_contract.py
```

unless independent evidence proves they are active-current rather than historical.

---

## F2 — Unicode title length parity defect

Server semantics count Unicode code points.

Current client semantics use JavaScript UTF-16 `.length`.

This produces disagreement for astral characters.

The existing HTML `maxlength="240"` has the same UTF-16 problem.

Important reachability detail:

A user typing/pasting 240 emoji directly is constrained by browser `maxlength`.

The demonstrated live path is programmatic title assignment, including AI suggestion copy, which bypasses that input-length constraint.

Required outcome:

```text
240 Unicode code points:
accepted

241 Unicode code points:
rejected
```

independently of UTF-16 representation.

Do not solve this by weakening the server contract.

The client must converge on the server semantics.

---

## F3 — C1 control-character parity defect

Client title/tag validation currently rejects approximately:

```text
U+0000–U+001F
U+007F
```

while Python rejects Unicode category:

```text
Cc
```

which also includes:

```text
U+0080–U+009F
```

The frontend description validator already contains stronger handling.

Required outcome:

```text
C0 controls: rejected where server rejects them
DEL: rejected
C1 controls: rejected
allowed description newline semantics: preserved
```

Do not invent a new validation policy.

Match existing backend behavior.

---

## F4 — movie genre-count parity defect

The server allows at most:

```text
8 genres
```

while the frontend currently exposes more selectable values and lacks equivalent validation.

Required outcome:

```text
8 genres: accepted
9 genres: rejected client-side before Save
```

The error must be actionable rather than degrading into generic server-side `"Save failed."`.

Do not redesign the genre UI.

Do not add visual counters or styling.

---

## F13 — analysis-run domain-ID type confusion

Current code reportedly contains an equivalent of:

```python
def _parse_analysis_run_id(value: str) -> MediaAnalysisRunId:
    ...
    return MediaId.from_string(value)
```

The current behavior survives because both wrappers eventually expose string-compatible behavior and run IDs happen to use UUID-shaped values.

Required outcome:

- successful parsing returns an actual `MediaAnalysisRunId`;
- invalid values retain the existing sanitized failure contract;
- add regression evidence proving the returned type;
- keep this fix bounded to the directly implicated parser/family.

Do not perform a broad identity/value-object redesign.

---

# 6. Slice 0 — AP consumer rebaseline

First restore a green baseline.

Update only active current-state AP integration expectations.

Expected files:

```text
tests/contract/test_ap_integration.py
README.md
```

Expected current pin:

```text
7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

Before changing documentation, distinguish:

```text
current operational statement
historical record
```

Do not mass-replace old SHA values.

After the change run focused AP integration tests.

At minimum cover:

```text
tests/contract/test_ap_integration.py
tests/contract/test_worker_execution_contract.py
```

The prerequisite is complete only when the active pin contract passes and historical evidence remains truthful.

Create a local commit for this prerequisite.

Suggested subject:

```text
Rebaseline FrameNest AP integration pin
```

Do not push.

Record its exact SHA for the report.

---

# 7. Slice 2 first phase — create RED behavioral parity evidence

Before modifying F2/F3/F4 production behavior, introduce the bounded parity test mechanism.

The approved architecture is a shared test fixture plus two language-specific executors.

Expected new fixture:

```text
tests/support/metadata_field_contract_cases.json
```

Expected server-side test:

```text
tests/contract/test_metadata_field_contract_parity.py
```

Expected client-side test:

```text
tests/metadata_form_contract.test.js
```

The shared fixture is acceptance data, not a runtime schema system.

No runtime request should load it.

No production packaging mechanism should depend on it.

Do not introduce:

```text
schema generation
runtime contract fetch
bundler
framework
new dependency
```

---

# 8. Required fixture coverage

At minimum encode behavior for:

## Title

```text
normal ASCII
leading/trailing whitespace according to existing contract
240 ordinary code points
241 ordinary code points
240 astral Unicode code points
241 astral Unicode code points
C0 control
DEL
C1 control
```

## Description

Include enough cases to protect the already-existing contract:

```text
normal description
maximum boundary where practical
allowed newline
forbidden tab/control according to server semantics
C1 control
```

Do not gratuitously broaden description behavior.

## Tag display name

Include:

```text
normal value
whitespace rules
C0 control
DEL
C1 control
```

## Genre set

Include:

```text
0 or ordinary valid set if allowed by current contract
8
9
```

Fixture expectations must derive from actual backend/domain behavior.

Do not encode what you wish the server did.

---

# 9. Server-side parity execution

The Python parity test must exercise real production domain/request validation paths.

It must not merely compare fixture values with duplicated constants.

Where reasonable, execute the real objects used by the backend, including examples such as:

```text
MediaDisplayTitle
MediaDescription
CanonicalTagDisplayName
actual genre/request validation semantics
```

The purpose is:

```text
fixture ↔ server contract
```

If fixture expectations disagree with the actual server contract, the test must fail.

---

# 10. Client-side parity execution

The Node test must execute actual production validator behavior from the FrameNest client.

It must not simply assert that strings or constants appear in `app.js`.

It must prove behavior.

A bounded `node:vm` extraction/harness is acceptable for this slice if it executes the real production validator functions and their actual dependent constants/helpers.

Do not create a second implementation of the validators inside the test.

The purpose is:

```text
fixture ↔ actual client behavior
```

Before production fixes, run the new parity tests and preserve exact RED evidence.

At minimum, the RED state should demonstrate the currently verified defect families:

```text
astral-code-point title boundary
C1 controls
9 genres
```

If one of these unexpectedly passes on the exact baseline, investigate and report why.

Do not mutate production merely to manufacture the expected failure.

---

# 11. Critical RED-evidence rule

Do **not** create a permanent intentionally-red commit.

The required sequence is:

```text
write parity tests/fixture
run them against unchanged production
capture exact failing evidence
then implement production corrections
obtain GREEN
commit the coherent tests + corrections
```

The terminal report must include the pre-fix RED commands and exact failure classification.

This provides authentic defect reproduction without polluting repository history with an intentionally broken intermediate commit.

---

# 12. Slice 1 — production corrections

After RED evidence exists, correct only the verified behavior.

## F2 title semantics

Use the existing Unicode code-point helper/pattern where possible.

The title validator must count Unicode code points rather than UTF-16 code units.

Review the existing:

```text
maxlength="240"
```

on the metadata title input.

The intended outcome is that the explicit validator owns the contract rather than an incompatible browser UTF-16 length constraint.

Do not alter layout or CSS.

---

## F3 controls

Align the client control-character rules with the backend's actual `Cc` semantics for the implicated fields.

Reuse or consolidate an existing helper only when doing so does not change unrelated field behavior.

Do not generalize beyond verified metadata/tag paths.

---

## F4 genre limit

Introduce the server-owned maximum semantics into the client in the smallest reasonable form.

Expected limit:

```text
8
```

When more than eight genres are selected:

- Save must become invalid through the existing validation/control mechanism;
- the user must receive a specific bounded validation message;
- no server request should be required to discover the error.

Do not add new UI chrome.

Do not change styles.

---

## F13 type correctness

Fix `_parse_analysis_run_id` so a successful result is genuinely:

```text
MediaAnalysisRunId
```

Use the least invasive implementation consistent with existing domain conventions.

If UUIDv4 validation is part of the currently intended contract, preserve it.

Do not weaken current error sanitization.

Add a focused regression test that would fail if a `MediaId` were returned again.

---

# 13. Slice 2 second phase — GREEN parity

After production corrections, rerun both parity suites.

All fixture cases must now agree across:

```text
shared fixture
Python/server
JavaScript/client
```

The relevant RED cases must become GREEN because production behavior changed, not because expected values were rewritten.

If an expectation needs changing after investigation, explicitly justify it in the report.

Do not silently edit the fixture to make tests green.

---

# 14. Slice 3 — metadata-form test convergence

Only after the behavioral parity mechanism is green, inspect the existing source-text assertions in:

```text
tests/contract/test_local_web_application.py
```

Retire only assertions for metadata validation behavior now covered by executable behavioral tests.

The objective is **not** to reduce test count for its own sake.

The objective is to stop source spelling/formatting from pretending to be behavior coverage.

A textual assertion may be removed only when its intended guarantee is demonstrably preserved by:

```text
new parity tests
existing JS behavioral tests
or another stronger executable test
```

Retain static/security assertions where source-level absence is genuinely the contract, for example where applicable:

```text
dangerous HTML insertion absence
external URL absence
secret leakage absence
persistent-storage prohibition
other explicit security/static guards
```

Do not wholesale rewrite `test_local_web_application.py`.

Do not touch unrelated frontend contracts.

---

# 15. Explicit non-scope

This Worker is forbidden from doing Slice 4.

Do not delete or refactor the audited dead/test-only clusters yet.

Do not perform changes to:

```text
styles.css
visual layout
general UI copy
frontend framework
ES modules
TypeScript
bundling
create_app architecture
dependency injection
database schema
Alembic migrations
API response shapes
filesystem TOCTOU/openat work
X audit-recorder wiring
_x_forbidden_roots
Python dormant scaffolding
CI
NUC deployment
VPS deployment
```

Do not implement F11/F12 or the accepted TOCTOU residual.

Do not clean old branches/worktrees.

Do not perform opportunistic formatting across unrelated code.

If you encounter a serious unrelated defect, record it in the terminal report and leave it unchanged unless it makes this authorized work impossible.

---

# 16. File boundary

Expected touched surface should remain approximately within:

```text
README.md
tests/contract/test_ap_integration.py

src/framenest/adapters/api/web/app.js
src/framenest/adapters/api/web/index.html

src/framenest/application/companion_review.py

tests/support/metadata_field_contract_cases.json
tests/contract/test_metadata_field_contract_parity.py
tests/metadata_form_contract.test.js

focused companion-review test file(s)
tests/contract/test_local_web_application.py
```

Additional files require a concrete causal justification in the terminal report.

Any change to:

```text
styles.css
pyproject.toml
Alembic migration files
API schemas
```

is presumptively out of scope and requires stopping rather than casually broadening authority.

---

# 17. Required validation

Use the canonical AP execution route.

Resolve `<BASELINE>` from the actual verified starting commit.

At minimum execute equivalent checks for:

```text
./.ap/ap doctor
```

and:

```text
./.ap/ap project check \
  --root /home/agile/Projects/framenest \
  --baseline <BASELINE>
```

Focused prerequisite validation must cover:

```text
tests/contract/test_ap_integration.py
tests/contract/test_worker_execution_contract.py
```

Focused new validation must cover:

```text
tests/contract/test_metadata_field_contract_parity.py
tests/metadata_form_contract.test.js
the companion-review regression for MediaAnalysisRunId
relevant metadata frontend tests
```

Run the complete JavaScript suite:

```text
node --test tests/*.test.js
```

Expected terminal requirement:

```text
0 failed
```

Gated/skipped browser evidence may remain at the previously accepted level if its prerequisites are genuinely unavailable.

Run the complete Python suite through AP:

```text
./.ap/ap exec \
  --root /home/agile/Projects/framenest \
  --baseline <BASELINE> \
  --operation test-focus \
  -- tests -q -p no:cacheprovider
```

Expected terminal requirement:

```text
0 failed
```

The exact passing count may increase because new tests are added.

Do not hardcode the old count as the expected final count.

Also perform residual searches proving the old incorrect forms no longer control the implicated behavior.

---

# 18. Commit structure

Local commits are authorized.

Pushes are not.

Prefer this bounded history:

```text
Commit A:
Rebaseline FrameNest AP integration pin

Commit B:
Align metadata client-server validation contracts

Commit C:
Replace metadata source assertions with behavior tests
```

Commit B may contain:

```text
shared parity fixture
Python parity test
Node parity test
F2/F3/F4 production fixes
F13 type fix
focused regression test
```

because the tests were first demonstrated RED in the worktree, then fixed and committed atomically in a green state.

If evidence shows a different split is materially safer, explain it.

Every committed state intended as a review boundary should be green for the relevant available tests.

At terminal state:

```text
git status --short
```

must be empty.

Do not push any commit.

Do not merge to `main`.

Do not deploy.

---

# 19. Stop conditions

Stop and report `BLOCKED` rather than improvising if:

- actual baseline differs materially from the approved baseline;
- `.ap` doctor fails for reasons unrelated to the known stale consumer expectation;
- unexpected unrelated worktree changes exist;
- fixing F2/F3/F4 requires an API/schema migration;
- behavioral parity cannot be tested without introducing a major new runtime architecture;
- full test failures reveal a non-local regression that cannot be causally explained;
- required authority would exceed this prompt.

A small implementation detail that can be resolved from existing architecture is not a reason to stop.

Use engineering judgment.

---

# 20. Terminal report

Return a complete terminal report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

The Cooperator will save the complete response as:

```text
02_report_00.md
```

Include:

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
Result artifact or commit(s)
Logical-whole closure
Report justification
Authority expiry
```

Then report, in detail:

## Baseline

- verified local HEAD;
- branch;
- public refs;
- local/public relationship;
- `.ap` gitlink and checkout;
- doctor result;
- initial worktree state.

## Slice 0

- exact active AP references changed;
- historical references intentionally preserved;
- focused validation;
- commit SHA.

## Authentic RED evidence

For F2, F3 and F4 provide:

- exact test/reproduction command;
- exact failing case;
- why it proves client/server divergence;
- confirmation production had not yet been changed.

## Production corrections

For each F2/F3/F4/F13:

- files changed;
- prior behavior;
- new behavior;
- rationale;
- regression protection.

## Parity mechanism

Describe:

```text
fixture structure
server executor
client executor
case families
```

and explain why it executes real behavior rather than string assertions.

## Test convergence

List exactly which source-text assertions were removed or replaced and what stronger behavioral evidence supersedes each.

## Validation

Report exact results for:

```text
focused Python
parity Python
parity JS
companion regression
full JS
full Python
ap doctor
ap project check
```

Do not summarize a failing suite as PASS.

## Git result

Provide:

```text
all created commit SHAs + subjects
final HEAD
git status --short
git diff baseline..HEAD --stat
```

State explicitly:

```text
no push performed
no publication performed
no deployment performed
Meta was not mutated
Slice 4 was not performed
```

## Residuals / observations

Record any newly discovered issue without fixing it unless it was required by authorized scope.

End with one of:

```text
implementation-PASS
implementation-BLOCKED
implementation-PARTIAL
```

and explain the exact reason.

All implementation authority from this prompt expires at the terminal report.
# FrameNest — Diagnostic Worker prompt (item 9 ordinary unopened after analysis)

```text
Persistent role identity: WORKER
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Phase: Diagnostic Closeout
Reasoning recommendation: High
Reasoning basis: Cooperator FAIL on R3′ ordinary unopened/badge after analysis; must distinguish fixture from a missing durable generic run vs a listing bug
Task identity: FRAMENEST-COMPANIE-ITEM9DIAG-01
```

```text
External trace disposition: configured
Trace discovery: /home/agile/meta/projects/framenest/06/00-framenest-companion/
Trace project key: framenest
Trace logical-whole projection identity: framenest-companion-brave-testing-resume
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 06_diagnostic_00.md
Destination path: /home/agile/meta/projects/framenest/06/00-framenest-companion/
Archival: wait-for-report
```

```text
Evidence tier: E2
Evidence tier basis: named rendered FAIL on ordinary own-history unopened after admin Analyze by AI; diagnosis is repository-path mapping, not live catalog dump
Authorized implementation stages: none
Combined implementation envelope: prohibited
Independent acceptance: not-required
Rollback or recovery checkpoint: canonical stays 977a7af80afed16745adb0ef8e939555e5e21cce
Activated stricter profile: none
```

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: companion own-history isolation and unopened_count tests; metadata/Load AI suggestion tests; suggestion-preview vs analysis-lifecycle tests
Affected tests: inspect and, if needed, re-run only the named focused suites through ap exec
New causal regression: none authorized
Broad or full suite: not-used
Runtime or testbed: docs/WORKER_EXECUTION_CONTRACT.md
Independent acceptance: not-required
```

You did not implement `977a7af…`. This is a fresh diagnostic session. Prior
Worker 04/05 authorities expired. You do **not** implement the Edit/AI
per-field apply UX. You do **not** open R4. You do **not** correct the
candidate in this exchange.

Exact SHA under diagnosis (public `main`, canonical HEAD, NUC active
release as last Cooperator-attested):

```text
977a7af80afed16745adb0ef8e939555e5e21cce
```

AP pin: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`

## Mission

Explain Cooperator item **9 FAIL** against R3′:

> After analysis of an **own** item, that row gets unopened accent and
> badge +1 for **this** (ordinary) user.

Live narrative (Cooperator, rendered, NUC on this SHA): as administrator in
Manage media he clicked **Analyze by AI**; no AI suggestion appeared in the
editor; **Save** then filled all inputs from the new suggestion and persisted
the meme. After switching to the ordinary identity that “downloaded” that
meme, companion history had **no** badge change and **no** unopened accent.

Your job: map that story onto repository objects and classify **one** primary
cause (or an ordered shortlist with a single most likely cause). Stop. Do not
fix it here.

Normative R3′ remains
`/home/agile/meta/projects/framenest/05/00-framenest-companion-brave-testing-resume/02_report_01.md`
and candidate/public ADR-0076: website Analyze-by-AI successes on in-scope
non-movie media **join** the analyzed pool; ordinary `unopened_count` is
**own-analyzed** cataloged X only.

## Mandatory reading

1. This prompt (sole current task authority).
2. `/home/agile/Projects/framenest/AGENTS.md`
3. `.ap/AP.md`, `.ap/AP_WORKER.md`
4. `docs/WORKER_EXECUTION_CONTRACT.md`
5. `docs/adr/0076-companion-history-hosted-click-admin-analyzed-inbox-and-ordinary-own-history.md`
6. `docs/adr/0067-*.md` (website Analyze by AI joins inbox — body read-only)
7. `src/framenest/infrastructure/persistence/companion_review_repository.py`
   (`_own_history_rows`, `_own_analyzed_latest`, `_analyzed_inbox_predicates`,
   `_owned_cataloged_x_predicates`)
8. `src/framenest/adapters/api/web/app.js` — `mediaAiSuggestionEndpoint`,
   `handleAnalyzeMetadataByAi`, `handleAnalyzeCatalogCard`,
   `companionWebHosted` Load/Analyze hiding
9. Suggestion preview vs durable lifecycle:
   `src/framenest/adapters/api/media_suggestion_api.py`,
   `src/framenest/application/media_suggestion.py`,
   `src/framenest/application/media_analysis_lifecycle.py`

## Repository gate

Working directory: `/home/agile/Projects/framenest` (canonical checkout;
published SHA; **no** new worktree required).

Verify and record:

- `git rev-parse HEAD` equals `977a7af80afed16745adb0ef8e939555e5e21cce`
- branch `feat/x-meme-browser-companion`
- `git status --porcelain=v1` empty; RF-12 classify and stop if not
- `.ap` HEAD equals the pin

Do not check out another SHA. Do not mutate canonical.

## Probe questions (answer each)

1. **Does successful website Analyze by AI persist a companion-visible
   generic run?** Trace `POST …/ai-suggestion-preview` (metadata editor and
   Gallery 🧠) to `media_analysis_runs` with
   `analysis_definition == automatic_post_catalog` and
   `analysis_profile == generic_media`. If preview returns JSON only and
   never `record_analyzed`, say so with exact functions.
2. **Would that run satisfy `_analyzed_inbox_predicates` and
   `_own_analyzed_latest`?** Quote the predicates. Name any extra gate
   (cataloged X, `created_by_login_key`, movie exclusion).
3. **If the ordinary user “downloaded” the meme from Gallery rather than
   owning an X Save,** can own-history ever list it? (own-history is
   requester-private **cataloged X**, not workspace/gallery downloads.)
4. **Does Save-after-Analyze change unopened/badge?** Unopened is
   open-state vs latest generic run, not “canonical metadata equals AI”.
   Confirm or refute from code.
5. **Hosted Edit hiding Load** (`companionWebHosted()`): classify as
   **out of scope for item 9** (Edit/AI apply is the next whole) unless it
   causally prevents the analysis run from existing.
6. **Existing tests:** which executed or inspectable tests already cover
   “website Analyze joins inbox/own-history”? If none, that is a named
   coverage gap, not a license to add tests in this session.

## Hypotheses to dispose (exactly one primary)

- H1 Fixture: media is not ordinary-owned cataloged X.
- H2 Operator: extension not reloaded / wrong identity still connected /
  badge alarm not yet fired.
- H3 Preview path does not persist a generic `media_analysis_runs` row, so
  companion never sees `analyzed=true` / unopened. (ADR-0067/0076 join
  sentence would then be unimplemented on this path.)
- H4 Run persisted but filtered out (wrong definition/profile, movie,
  omitted category, not latest).
- H5 Listing/badge bug in own-history `unopened_count` despite a visible
  analyzed own row.
- H6 Ordinary already opened the row (open_state present).
- H7 Other, named.

## Canonical execution route (RF-16)

Python evidence only through:

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce --operation runtime-info
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce \
  --operation test-focus -- <selection> -q -p no:cacheprovider
```

Re-run tests **only** if inspection is insufficient to dispose H3–H5.
Suggested focus if used:

```text
tests/contract/test_companion_review_api.py
tests/unit/infrastructure/persistence/test_companion_review_repository.py
```

plus any existing suggestion-preview / analysis-lifecycle contract tests you
name. Node only if you must prove `companionWebHosted` hide vs analyze POST.
No new tests. No `.venv` repair. Ambient encodings: classify, rerun once via
`ap exec`.

## Authority

Positive: read canonical tree; `ap project check` / `ap exec` as above;
`node --test` only if required for H5/hosted-hide; write the report file.

Negative: no product edits; no ADR body edits; no SECURITY.md; no Git
commits/push; no NUC/SSH/sudo/`framenest-release`; no live catalog/SQL; no
identity map, media titles, tweet URLs, or UUIDs from production; no
provider calls; no Edit/AI per-field UX; no R4; no closure.

Git: read-only. Side-effect: read-only.

## Output

Write exactly:

```text
/home/agile/meta/projects/framenest/06/00-framenest-companion/06_report_00.md
```

Begin exactly `### Report for ORCHESTRATOR_CHAT`.

Include: coordinate echo; PASS/PARTIAL/BLOCKED (`acceptance-PASS` is
invalid here). Phase-qualified result: not-applicable (diagnostic). Primary
hypothesis and disposition of H1–H7. Exact functions/endpoints for preview
vs `record_analyzed`. Whether ADR-0067/0076 “website Analyze by AI
successes join” is implemented on the Manage-media Analyze path. Item 9:
**candidate defect** vs **fixture/operator** vs **ADR gap**. One smallest
next step for ORCHESTRATOR (bounded correction of persistence-join **or**
Cooperator re-spot-check with an ordinary-owned cataloged X Save after
unpacked reload **or** escalate). No correction commit. Report
justification: `new-evidence`. Authority expiry. Capability handshake.
Resolved Execution Issues / Near-Misses; Pre-Existing Failure
Classification. `Logical-whole closure: not-closed`.

## Stopping rule

Stop after the report. Stop BLOCKED on dirty canonical tree, failed gate, or
any need for live NUC catalog. Do not start a correction.

## Transition owner

ORCHESTRATOR may authorize one smallest correction, ask the Cooperator to
re-test item 9 with a named fixture, or escalate. Edit/AI apply UX remains
the **next** logical whole after this companion-history whole closes.

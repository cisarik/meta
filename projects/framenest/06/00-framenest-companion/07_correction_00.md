# FrameNest — Bounded correction Worker prompt (item 9 persistence-join)

```text
Persistent role identity: WORKER
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Reasoning recommendation: High
Reasoning basis: persist generic analysis runs from interactive Analyze by AI so companion unopened/badge join ADR-0067/0076; no second provider call
Task identity: FRAMENEST-COMPANIE-ITEM9JOIN-01
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
Downloadable prompt filename: 07_correction_00.md
Destination path: /home/agile/meta/projects/framenest/06/00-framenest-companion/
Archival: wait-for-report
```

```text
Acceptance candidate after this session: the one new commit you create (parent must be 977a7af80afed16745adb0ef8e939555e5e21cce)
Evidence tier: E3
Evidence tier basis: durable analysis-run write from a previously non-persistent preview; companion listing/unopened join
Authorized implementation stages: isolated-worktree correction, focused tests, one local commit
Combined implementation envelope: allowed for those stages only
Independent acceptance: required-separate-fresh-worker
You do not perform that acceptance.
Rollback or recovery checkpoint: canonical checkout remains 977a7af… until a later publication grant
Activated stricter profile: none
```

Diagnostic `06_report_00.md` classified item 9 as **H3**: Manage-media Analyze by AI and Gallery 🧠 POST `…/ai-suggestion-preview`; `PreviewImportedMediaSuggestion` is documented non-persistent and never `record_analyzed`. Companion `analyzed` / `unopened_count` require a latest generic run. ADR-0067 §5 and ADR-0076 R2 “website Analyze-by-AI successes join” are unimplemented on this path. You implement that join. You do **not** build the Edit/AI per-field apply UX. You do **not** open R4. You do **not** enable `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`.

Exact parent / public `main`:

```text
977a7af80afed16745adb0ef8e939555e5e21cce
```

AP pin: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`

## Frozen correction (do not replan)

After a **successful** imported-media suggestion preview (`PreviewImportedMediaSuggestion.execute`, after `provider.suggest` returns a usable suggestion):

1. Persist **one** companion-visible generic analyzed run:
   - `analysis_definition = automatic_post_catalog`
   - `analysis_profile = generic_media`
   - `state = analyzed`
   - `result_json` via existing `serialize_suggestion_result`
   - provider/model/prompt_version from the suggestion object already returned
2. **Do not** call the provider a second time. Do **not** invoke
   `ExecuteAutomaticMediaAnalysisRun.execute` (that re-runs the executor).
   Use the existing run repository: `RequestManualMediaAnalysis` /
   `create_manual_pending` (or equivalent create of a pending/manual run)
   then `record_analyzed` with the **already obtained** suggestion. Follow
   existing uniqueness/supersession for `(media_id, analysis_definition)`
   (migration 0018). Analyze twice must not violate that uniqueness; a new
   terminal success supersedes per current durable-run rules.
3. **Do not** persist a join run when the media is in-scope excluded as a
   movie (same movie exclusion companion already uses).
4. Library-scan `PreviewMediaSuggestion` (non-imported candidates) stays
   non-persistent. Only the **imported catalog location** path joins.
5. Canonical Save / Gallery 🧠 PUT metadata remain separate. Persisting the
   run must not itself write title/description/tags. Gallery 🧠 may still
   PUT after preview; both buttons share the same preview POST, so one
   persist in `PreviewImportedMediaSuggestion` covers both.
6. Automatic-analysis enablement stays off in git. Manual durable-analysis
   batch enqueue stays. No fifth `companion_mutation`. No Alembic 0034.
   Schema head remains `0033`.
7. Do not edit ADR-0067 or ADR-0067-era bodies. ADR-0076 already says
   website Analyze-by-AI successes join; you may add a **surgical** present
   tense sentence in `docs/X_COMPANION.md` only if a current sentence would
   stay false after this persist. No SECURITY.md rewrite. No Edit modal
   chrome (no dropdown, no per-field ✅).

If the existing ports cannot persist without a constructor/DI change, that
is in scope. If you would need a new suggestion store, stop and report —
that would violate ADR-0067 “no second suggestion store.”

## Mandatory reading

1. This prompt.
2. `AGENTS.md`; `.ap/AP.md`; `.ap/AP_WORKER.md`; `docs/WORKER_EXECUTION_CONTRACT.md`
3. `06_report_00.md` (claim already classified; H3 is the defect)
4. `docs/adr/0076-*.md`; ADR-0067 §5 (bodies of 0067/0073 read-only)
5. `src/framenest/application/media_suggestion.py` (`PreviewImportedMediaSuggestion`)
6. `src/framenest/application/media_analysis_lifecycle.py` (`serialize_suggestion_result`, `record_analyzed` call site, `RequestManualMediaAnalysis`)
7. `src/framenest/infrastructure/persistence/companion_review_repository.py` predicates
8. `src/framenest/adapters/api/application.py` composition of `PreviewImportedMediaSuggestion`

## Working copy and Git

Create an isolated worktree from exact `977a7af…`. Canonical
`/home/agile/Projects/framenest` stays on that SHA until a later publication
grant. Do not mutate w3/w4 except as read-only evidence.

Git: one normal commit in **your** worktree; explicit paths only (no
`git add -A`); no push; no force; no rebase of shared history. Report the
40-hex.

Suggested worktree path:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w7
```

If that path exists, stop. `git submodule update --init .ap` worktree-local
only; gitlink remains the pin.

## Edit allowlist

1. `src/framenest/application/media_suggestion.py`
2. `src/framenest/application/media_analysis_lifecycle.py` (only if you extract
   a persist-from-already-suggested helper; do not add a second provider call)
3. `src/framenest/application/ports/media_analysis_runs.py` only if a port
   method is strictly required and already implied by `record_analyzed` /
   `create_manual_pending`
4. `src/framenest/adapters/api/application.py` (DI only)
5. `src/framenest/adapters/api/media_suggestion_api.py` only if the HTTP
   adapter must pass identity/clock; prefer persist inside the use case
6. Tests you must add or extend:
   - `tests/unit/application/test_media_suggestion.py`
   - `tests/contract/test_media_suggestion_api.py`
   - companion join: `tests/contract/test_companion_review_api.py` and/or
     `tests/unit/infrastructure/persistence/test_companion_review_repository.py`
7. `docs/X_COMPANION.md` only if a present-tense sentence would otherwise
   remain false

Forbidden: ADR-0067/0073 bodies, SECURITY.md, alembic versions, Edit/Details
chrome, extension sidebar/service worker unless a test-only fixture requires
it (it should not), deploy, `.venv`, R4.

## Tests (minimum)

Through `./.ap/ap exec` with `--baseline 977a7af80afed16745adb0ef8e939555e5e21cce`.

Prove:

- Successful imported preview persists a generic analyzed run; companion
  admin inbox lists it; ordinary **owner** of cataloged X gets
  `analyzed=true` and `unopened_count` +1; Alice ⊈ Bob.
- Movie media does not join.
- Library-candidate (non-imported) preview still does not write runs.
- No second `provider.suggest` per preview.
- Existing companion isolation and four-mutation tests still pass (re-run
  the companion contract/repository files you touch plus
  `test_x_route_policy.py` if you touch ingress — you should not).

Isolated-worktree `ap exec --root <w7>` will fail without `.venv`. Classify
environment limitation; use canonical `--root` plus pytest
`--rootdir` / `-o pythonpath=<w7>/src` as the **task-specific** deviation
already used in session 04. Prove `framenest.__file__` under w7 `src/`.
Do not reconstruct `.venv`.

Node: not required unless you change JS (you should not).

## RF-16

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce
```

Python tests: `ap exec --operation test-focus` as in session 04 deviation
after classifying the worktree launch-path miss.

Ambient encodings: classify, rerun once via `ap exec`.

## Negative authority

No NUC, SSH, sudo, providers (tests use fakes), browser, push, publication,
R4, Edit/AI per-field UX, Funnel, CORS, fifth mutation, 0034.

## Output

```text
/home/agile/meta/projects/framenest/06/00-framenest-companion/07_report_00.md
```

Begin `### Report for ORCHESTRATOR_CHAT`. Echo coordinates. Status PASS only
if the join is implemented, tests above pass, one commit, parent `977a7af…`.
Phase-qualified result: `implementation-PASS`. Not acceptance. Not closure.
Changed files; persist design (exact functions); confirmation of no second
provider call; movie skip; schema still 0033. Report justification:
`new-mutation`. Authority expiry.

## Stopping rule

Stop after the report. Stop BLOCKED if persist requires a second suggestion
store, a second provider call, or Edit UX.

## Transition owner

ORCHESTRATOR issues independent acceptance of your commit against item 9
(ordinary own-history unopened after Analyze by AI) plus original
R1–R3′ risk claims that this persist could affect. You do not self-accept.

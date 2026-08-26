# FrameNest — Bounded correction Worker prompt (item 9 inverted tests)

```text
Persistent role identity: WORKER
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Reasoning recommendation: Standard
Reasoning basis: two inverted tests found by independent acceptance; no product persist redesign
Task identity: FRAMENEST-COMPANIE-ITEM9TEST-01
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
Downloadable prompt filename: 09_correction_00.md
Destination path: /home/agile/meta/projects/framenest/06/00-framenest-companion/
Archival: wait-for-report
```

```text
Acceptance candidate after this session: the one new commit you create (parent must be fb59c42a8e3a32d9476581beeabba0eb9c04109a)
Evidence tier: E3
Evidence tier basis: correction of inverted tests that were the named item-9 HTTP join proof
Authorized implementation stages: isolated-worktree test-only correction, focused tests, one local commit
Combined implementation envelope: allowed for those stages only
Independent acceptance: required-separate-fresh-worker
You do not perform that acceptance.
Rollback or recovery checkpoint: canonical checkout remains 977a7af80afed16745adb0ef8e939555e5e21cce
Activated stricter profile: none
```

Independent acceptance `08_report_00.md` is **PARTIAL**. ORCHESTRATOR does
**not** accept `fb59c42…` for publication. Product persist-join is not
redesigned here. Session 07 claimed the two tests below passed; session 08
did not reproduce that. This grant is a **second bounded correction** for
**new independent evidence** (inverted tests), not a second automatic
correction of H3.

Exact parent:

```text
fb59c42a8e3a32d9476581beeabba0eb9c04109a
```

Public `main` / canonical HEAD / `--baseline`:

```text
977a7af80afed16745adb0ef8e939555e5e21cce
```

AP pin: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`

## Frozen correction (do not replan)

**Test-only.** Do not change application, adapters, docs, ADRs, Alembic, JS,
or DI.

### 1. `tests/contract/test_companion_review_api.py`

`test_imported_preview_joins_inbox_and_own_history` uses
`ingress_mode="tailscale_uds"`. Unsafe methods require Origin +
`X-FrameNest-Request: 1`. The test POSTs with `_serve_headers` only → 403
`MUTATION_ORIGIN_FORBIDDEN` before the join.

Fix every **POST** in that test (imported preview, movie preview, and
library-scan preview) to use `_mutation_headers(ADMIN_LOGIN)` (default
`origin=EXTERNAL_ORIGIN`). Preview is `capability=analysis.run` and
**not** `companion_mutation`. Do **not** use `COMPANION_ORIGIN` on those
POSTs (that origin is allowed only for companion-flagged mutations).

GET inbox / own-history may keep `_serve_headers`.

Do not weaken ingress. Do not switch the test to loopback to hide Tailscale.

### 2. `tests/unit/application/test_media_analysis_lifecycle.py`

`_FakeRepository.create_manual_pending` hardcodes the same pending id
`22222222-2222-4222-8222-222222222222` on every superseding create.
`test_imported_preview_join_supersedes_prior_terminal_success` therefore
cannot hold `first.id != second.id`.

Emit a **distinct** run id on each new pending create (counter or a second
constant). Keep first-create behaviour for existing single-execute tests.
Do not change production `SqliteMediaAnalysisRunRepository`.

If after the fake fix the **real** SQLite uniqueness/supersession is what
fails, stop **BLOCKED** and report; do not invent a second suggestion store
or a second `provider.suggest`.

## Mandatory reading

1. This prompt.
2. `AGENTS.md`; `.ap/AP.md`; `.ap/AP_WORKER.md`; `docs/WORKER_EXECUTION_CONTRACT.md`
3. `08_report_00.md` (PARTIAL; two red gates)
4. The two test files named above

## Working copy and Git

Isolated worktree from exact `fb59c42…`. Suggested path:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w9
```

If that path exists, stop. Do not mutate canonical, w3, w4, w7, or w8.

One normal commit in **your** worktree; explicit paths only; no `git add -A`;
no push; no amend of `fb59c42…`; no rebase of shared history.
`git submodule update --init .ap` worktree-local only.

## Edit allowlist

1. `tests/contract/test_companion_review_api.py`
2. `tests/unit/application/test_media_analysis_lifecycle.py`

Forbidden: every other path, including all `src/`, ADRs, SECURITY.md,
Alembic, Edit/AI apply UX, R4, `.venv`.

## Tests

Through `./.ap/ap exec` with `--baseline 977a7af80afed16745adb0ef8e939555e5e21cce`.

Minimum: the two corrected tests plus the same classified envelope used in
session 08 for:

```text
tests/unit/application/test_media_suggestion.py
tests/unit/application/test_media_analysis_lifecycle.py
tests/contract/test_media_suggestion_api.py
tests/contract/test_companion_review_api.py
```

Prove:

- Owning HTTP join reaches 200; admin inbox lists Alice’s media analyzed +
  unopened; Alice own-history `unopened_count == 1`; Bob `unopened_count == 0`;
  movie preview writes no run; library-scan preview writes no run; provider
  call count increments by one per POST.
- `first.id != second.id` on the supersession unit test; transactions remain
  two full persist cycles; `save_calls == 0`.

Isolated-worktree `ap exec --root <w9>` will fail without `.venv`. Classify
environment limitation; use canonical `--root` plus pytest `--rootdir` /
`-o pythonpath=<w9>/src`. Prove `framenest.__file__` under w9 `src/`.
Do not reconstruct `.venv`.

## RF-16

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce
```

Ambient encodings: classify, rerun once via `ap exec`.

## Negative authority

No NUC, SSH, sudo, providers, browser, push, publication, R4, Edit/AI
per-field UX, Funnel, CORS, fifth mutation, 0034, product persist redesign.

## Output

```text
/home/agile/meta/projects/framenest/06/00-framenest-companion/09_report_00.md
```

Begin `### Report for ORCHESTRATOR_CHAT`. Echo coordinates. Status PASS only
if both inverted tests are green, allowlist held, one commit, parent
`fb59c42…`. Phase-qualified result: `implementation-PASS`. Not acceptance.
Not closure. Report the 40-hex. Report justification: `new-mutation`.
Authority expiry.

## Stopping rule

Stop after the report. Stop BLOCKED if the fix requires product code or a
second provider call.

## Transition owner

ORCHESTRATOR issues independent re-acceptance of your commit against item 9
plus the original persist-join risk claims. You do not self-accept.

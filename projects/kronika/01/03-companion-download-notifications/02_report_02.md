### Report for ORCHESTRATOR_CHAT

Logical whole identity: companion-download-notifications
Worker session ordinal: 02
Worker exchange ordinal: 03

## Status

Status: implementation-PASS
Phase-qualified result: implementation-PASS
Logical-whole closure: not-closed
Report justification: new-mutation

Start commit: cc8f67965213ee9b22d113cc200776c42f6503ba
End commit: 647e6da11416559f1bef52d53e9743acbd2bb688
Parent: cc8f67965213ee9b22d113cc200776c42f6503ba
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50

This exchange ran in the implementation session that produced `02_report_00.md`. The worktree was clean `main...origin/main [ahead 1]` at `cc8f679`, whose parent is `e64f2b0`. No publication, deployment, acceptance, or closure is claimed.

## Finding

C1 reproduced. `historyListRoute()` captured origin, configuration revision, and capabilities, but not the identity login. `aggregationContextMatches()` therefore accepted a later identity with the same capabilities and a different login.

Before the fix, the new regression changed only `login` from `alice` to `bob`. `identitySeen >= 2` passed, then:

```text
tests/companion_review_extension.test.js:1708
assert.equal(result.stale, true)
AssertionError: false !== true
```

The in-flight result stayed successful, so review rows and download rows could belong to different logins.

## Change

`identityLoginFromBody()` reads `body.login` and uses `""` when the field is absent or not a string. `historyListRoute()` stores that value on the route. `aggregationContextMatches()` requires the current login to equal the captured login, in addition to origin, revision, capabilities, and history source. A mismatch still returns the existing stale-context result: `stale: true`, `ok: false`, empty review items, empty download items, and no badge write.

The response shape, UI, documentation, API, badge, permissions, storage, message types, and mutation count are unchanged.

## Regression

`tests/companion_review_extension.test.js` now has two distinct cases:

- `changed identity capabilities discard the in-flight history result without clearing the badge` (the previous capability case, renamed)
- `changed identity login discards the in-flight history result without clearing the badge`

The login case keeps the same capability list, expects `stale: true` and `ok: false`, empty review and download items, and badge text left at `9`.

## Validation

`git diff --check` was clean. Staged `git diff --cached --name-only` and committed `git show --name-only` are exactly:

- extension/background/service_worker.js
- tests/companion_review_extension.test.js

Worktree after commit: `## main...origin/main [ahead 2]`, clean. Not pushed.

```text
./.ap/ap project check --root /Users/agile/Projects/kronika --baseline cc8f67965213ee9b22d113cc200776c42f6503ba
```

PASS.

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline cc8f67965213ee9b22d113cc200776c42f6503ba --operation runtime-info
```

PASS. CPython 3.13.14 through the project virtualenv.

```text
node --test tests/companion_review_extension.test.js tests/x_companion_extension.test.js
```

110 passed. That includes the renamed capability regression, the new login regression, and the 56 X companion tests.

```text
node --test tests/companion_web_bridge.test.js tests/companion_settings_automatic_analysis.test.js tests/youtube_request_cockpit.test.js tests/youtube_acquisition_cockpit.test.js tests/x_acquisition_cockpit.test.js
```

64 passed.

## Orchestration critique

MEASURED: none
LEAD: none

## Proposed next step

A fresh independent full acceptance of `647e6da11416559f1bef52d53e9743acbd2bb688` before any publication.

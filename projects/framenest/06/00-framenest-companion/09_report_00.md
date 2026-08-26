### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 09
Worker exchange ordinal: 01
Task identity: FRAMENEST-COMPANIE-ITEM9TEST-01
```

Status: **PASS**  
Phase-qualified result: `implementation-PASS`  
Logical-whole closure: not-closed  
Independent acceptance: not performed (required-separate-fresh-worker)  
Report justification: `new-mutation`

This session is a **test-only** second bounded correction of inverted tests
found by independent acceptance `08_report_00.md`. It is not acceptance and
not closure. Product persist-join was not redesigned. No application,
adapter, ADR, Alembic, JS, or DI edits.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; client-presented identity |
| Reasoning | Standard | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Plan Mode off; frozen correction executed | directly observed |
| Permission mode | not named | unknown/not observably exposed | unknown |
| Repository | Isolated worktree from exact `fb59c42…` | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w9`; detached `2aead540ee39a81a96425902f85e9b9a34f0d690` | directly observed |
| Canonical checkout | Remain `977a7af…` | `/home/agile/Projects/framenest`; `feat/x-meme-browser-companion`; HEAD `977a7af80afed16745adb0ef8e939555e5e21cce`; tracked-clean | directly observed |
| w3 / w4 | Unused; remain `977a7af…` | both `977a7af80afed16745adb0ef8e939555e5e21cce` | directly observed |
| w7 / w8 | Unused as working copy; remain `fb59c42…` | both `fb59c42a8e3a32d9476581beeabba0eb9c04109a` | directly observed |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | w9 gitlink and `.ap` HEAD equal the pin | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; worktree `--root` miss classified; canonical `--root` plus pytest `pythonpath` / `--rootdir` | directly observed |
| Network, NUC, SSH, sudo, providers, browser | Forbidden | Unused; tests used fakes | directly observed |
| Git | One normal commit in w9; explicit paths; no push | One commit `2aead54…`; parent `fb59c42…`; no push | directly observed |

Capability, permission, and client identity did not expand task authority.

## Repository gate

```text
Canonical HEAD:     977a7af80afed16745adb0ef8e939555e5e21cce
Canonical branch:   feat/x-meme-browser-companion
Canonical porcelain: empty
w9 start:           fb59c42a8e3a32d9476581beeabba0eb9c04109a
w9 end:             2aead540ee39a81a96425902f85e9b9a34f0d690
w9 parent:          fb59c42a8e3a32d9476581beeabba0eb9c04109a
w9 porcelain after commit: empty
.ap HEAD:           9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

RF-12: clean isolated worktree; no classification stop. Canonical, w3, w4,
w7, and w8 not mutated.

## Frozen correction applied

### 1. `tests/contract/test_companion_review_api.py`

`test_imported_preview_joins_inbox_and_own_history` remains
`ingress_mode="tailscale_uds"`. Every POST in that test (imported preview
twice, movie preview, library-scan preview) now uses
`_mutation_headers(ADMIN_LOGIN)` (default `origin=EXTERNAL_ORIGIN`, plus
`X-FrameNest-Request: 1`). GET inbox / Alice own-history / Bob own-history
still use `_serve_headers`. `COMPANION_ORIGIN` is not used on those POSTs.

Ingress was not weakened. The test was not switched to loopback.

### 2. `tests/unit/application/test_media_analysis_lifecycle.py`

`_FakeRepository.create_manual_pending` now emits a distinct run id on each
new pending create via `_manual_pending_serial`. First create remains
`22222222-2222-4222-8222-222222222222` for existing single-execute tests.
Subsequent creates use `22222222-2222-4222-8222-{serial:012d}`. Active
pending/analyzing still returns the existing run without incrementing.
Production `SqliteMediaAnalysisRunRepository` was not changed.

SQLite uniqueness/supersession on the real repository did not fail (the
owning HTTP join uses the real SQLite repository and reached 200 with a
second persisted run). No second suggestion store and no second
`provider.suggest` were invented.

## Changed files

1. `tests/contract/test_companion_review_api.py`
2. `tests/unit/application/test_media_analysis_lifecycle.py`

`git diff --name-only fb59c42… HEAD` is exactly those two paths
(`+12 / −5`). Forbidden paths unchanged: all `src/`, ADRs, `SECURITY.md`,
Alembic, Edit/AI apply UX, R4, `.venv`.

## Validation

### Worktree `--root` (declared route first)

```text
./.ap/ap project check --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w9 \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce
```

Outcome: FAIL `declared CPython executable does not exist`. Classification:
**environment limitation** (isolated worktree has no launch-path `.venv`).
Not repaired. Candidate not failed for this miss.

### Classified deviation (canonical `--root`)

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce
```

Outcome: `ap project check --baseline: PASS`. WARN sanitized inherited
environment classes: `LD_LIBRARY_PATH SSH_AUTH_SOCK VIRTUAL_ENV_DISABLE_PROMPT
PROMPT_COMMAND APPDIR APPIMAGE PATH`. CPython 3.13.

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce --operation runtime-info
```

Outcome: PASS. Interpreter `/home/agile/Projects/framenest/.venv/bin/python`;
CPython 3.13.9; envelope `framenest.__file__` is canonical source (envelope
proof only).

### Provenance probe

Temporary `/tmp/framenest-item9test-09-provenance.py` (outside both git
checkouts), collected through authorized `test-focus` with `--rootdir` /
`pythonpath` on w9. Printed path:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w9/src/framenest/__init__.py
```

Outcome: `1 passed in 0.01s`. Probe deleted (`PROBE_GONE`). Candidate `src/`
provenance proven.

### Python test-focus matrix

Same classified envelope (canonical `--root`, candidate `--rootdir` and
`pythonpath`):

```text
tests/unit/application/test_media_suggestion.py
tests/unit/application/test_media_analysis_lifecycle.py
tests/contract/test_media_suggestion_api.py
tests/contract/test_companion_review_api.py
```

Outcome: **89 passed in 10.71s**. No failed suite. Ambient encodings
signature not observed. Node: not required (no JS change).

Proven claims from the two previously inverted tests:

- Owning HTTP join reaches 200. Admin inbox lists Alice’s media
  `analyzed=true` and `unopened=true`. Alice own-history
  `unopened_count == 1`. Bob `unopened_count == 0` and Alice’s media is
  absent from Bob’s items. Movie preview writes no run. Library-scan
  preview writes no run. Provider call count increments by one per POST
  (`test_imported_preview_joins_inbox_and_own_history`).
- `first.id != second.id` on
  `test_imported_preview_join_supersedes_prior_terminal_success`.
  Transactions remain two full persist cycles
  (`create_manual_pending`, `claim_pending`, `record_analyzed` twice).
  `save_calls == 0`.

## Git write result

One normal commit in w9; explicit paths only; no `git add -A`; no push; no
amend of `fb59c42…`; no rebase of shared history.

```text
2aead540ee39a81a96425902f85e9b9a34f0d690
```

Parent: `fb59c42a8e3a32d9476581beeabba0eb9c04109a`.

## Deviations, residual risk, missing evidence

- Isolated-worktree `ap exec --root <w9>` is an environment limitation
  (no `.venv`). Task-specific deviation: canonical `--root` plus pytest
  `--rootdir` / `-o pythonpath=<w9>/src`, with proven w9 `framenest.__file__`.
- Live NUC / Brave companion not exercised (forbidden).
- This session does not self-accept. Independent re-acceptance of
  `2aead54…` against item 9 plus the original persist-join risk claims
  remains with ORCHESTRATOR.

## One smallest next step (ORCHESTRATOR)

Issue independent fresh-worker re-acceptance of
`2aead540ee39a81a96425902f85e9b9a34f0d690` against item 9 plus the original
persist-join risk claims. This Worker does not self-accept, publish, merge,
or run `framenest-release`.

## Authority expiry

This report terminates FRAMENEST-COMPANIE-ITEM9TEST-01. No follow-on action,
acceptance, publication, push, NUC access, provider call, R4, Edit/AI apply UX,
product persist redesign, or logical-whole closure is authorized.

```text
Resolved Execution Issues / Near-Misses: isolated worktree `--root` declared CPython missing (no `.venv`); cause: expected isolated-worktree launch-path miss; resolution: classified environment limitation, canonical `--root` plus pytest `--rootdir`/`pythonpath` with proven w9 `src/framenest/__init__.py`; ambient AppImage/loader classes (`APPIMAGE`, `APPDIR`, `LD_LIBRARY_PATH`, inherited `PATH`, `SSH_AUTH_SOCK`) present in the parent; resolution: `./.ap/ap` sanitized-v1 re-exec; residual risk: none for this correction (no ambient Python used for evidence).
Pre-Existing Failure Classification: none
```

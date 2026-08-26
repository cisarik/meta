### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 07
Worker exchange ordinal: 01
Task identity: FRAMENEST-COMPANIE-ITEM9JOIN-01
```

Status: **PASS**  
Phase-qualified result: `implementation-PASS`  
Logical-whole closure: not-closed  
Independent acceptance: not performed (required-separate-fresh-worker)  
Report justification: `new-mutation`

This session implemented the item 9 persistence-join on parent
`977a7af80afed16745adb0ef8e939555e5e21cce`. It is not acceptance and not
closure. Edit/AI per-field apply, R4, and `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`
were not opened.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; client-presented identity |
| Reasoning | High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Plan Mode off; frozen correction executed | directly observed |
| Permission mode | not named | unknown/not observably exposed | unknown |
| Repository | Isolated worktree from exact `977a7af…` | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w7`; detached `fb59c42a8e3a32d9476581beeabba0eb9c04109a` | directly observed |
| Canonical checkout | Remain `977a7af…` until later publication grant | `/home/agile/Projects/framenest`; `feat/x-meme-browser-companion`; HEAD `977a7af80afed16745adb0ef8e939555e5e21cce`; tracked-clean | directly observed |
| Session-03 / session-04 worktrees | Read-only evidence | w3 and w4 still `977a7af…` tracked-clean | directly observed |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | w7 gitlink and `.ap` HEAD equal the pin | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; worktree `--root` miss classified; canonical `--root` plus pytest `pythonpath` / `--rootdir` | directly observed |
| Network, NUC, SSH, sudo, providers, browser | Forbidden | Unused; tests used fakes | directly observed |
| Git | One normal commit in w7; explicit paths; no push | One commit `fb59c42…`; parent `977a7af…`; no push | directly observed |

Capability, permission, and client identity did not expand task authority.

## Repository gate

```text
Canonical HEAD:     977a7af80afed16745adb0ef8e939555e5e21cce
Canonical branch:   feat/x-meme-browser-companion
Canonical porcelain: empty
w7 start:           977a7af80afed16745adb0ef8e939555e5e21cce
w7 end:             fb59c42a8e3a32d9476581beeabba0eb9c04109a
w7 parent:          977a7af80afed16745adb0ef8e939555e5e21cce
w7 porcelain after commit: empty
.ap HEAD:           9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

RF-12: clean isolated worktree; no classification stop. Canonical not mutated.
w3/w4 not mutated.

## Persist design

After a successful `PreviewImportedMediaSuggestion.execute` `provider.suggest`,
the optional injected join runs once:

1. `PreviewImportedMediaSuggestion.execute` — one `provider.suggest`; then
   `ImportedPreviewAnalysisJoin.execute` when injected.
2. `PersistImportedPreviewAnalysis.execute` — movie skip via
   `MediaMetadataRepository.get_media_metadata` (`content_category is movie`);
   otherwise `RequestManualMediaAnalysis.execute` →
   `create_manual_pending`; `claim_pending`; `record_analyzed` with the
   **already obtained** suggestion through `serialize_suggestion_result`.
   Fields: `analysis_definition=automatic_post_catalog`,
   `analysis_profile=generic_media`, `state=analyzed`.
3. DI in `create_app` injects `PersistImportedPreviewAnalysis` into
   `PreviewImportedMediaSuggestion`.
4. `PreviewMediaSuggestion` (library-scan candidates) is unchanged and has no
   join.

**No second `provider.suggest` per preview.**  
**`ExecuteAutomaticMediaAnalysisRun.execute` is not invoked** (that would
re-run the executor). Claim + `record_analyzed` reuse the existing run
repository. Analyze twice uses current supersession (`create_manual_pending`
after a terminal run). An already-`analyzing` active run is left untouched.

**Movie skip:** persist returns without writing a run when canonical
`content_category` is movie (same exclusion companion uses). Preview JSON is
still returned.

**Canonical metadata:** persist does not write title/description/tags. Schema
head remains `0033` (no Alembic `0034`). Automatic-analysis enablement stays
off. No fifth `companion_mutation`. `docs/X_COMPANION.md` already said website
Analyze-by-AI successes join in present tense; no edit.

## Changed files

1. `src/framenest/application/media_suggestion.py`
2. `src/framenest/application/media_analysis_lifecycle.py`
3. `src/framenest/adapters/api/application.py`
4. `src/framenest/adapters/api/media_suggestion_api.py`
5. `tests/unit/application/test_media_suggestion.py`
6. `tests/unit/application/test_media_analysis_lifecycle.py`
7. `tests/contract/test_media_suggestion_api.py`
8. `tests/contract/test_companion_review_api.py`

Forbidden paths unchanged: ADR-0067/0073 bodies, `SECURITY.md`, alembic
versions, Edit/Details chrome, extension, deploy, `.venv`, R4.

## Validation

### Worktree `--root` (declared route first)

```text
./.ap/ap project check --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w7 \
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

Temporary `/tmp/framenest-item9join-07-provenance.py` (outside both git
checkouts), collected through authorized `test-focus` with `--rootdir` /
`pythonpath` on w7. Printed path:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w7/src/framenest/__init__.py
```

Outcome: `1 passed in 0.01s`. Probe deleted (`PROBE_GONE`).

### Python test-focus matrix

Same classified envelope (canonical `--root`, candidate `--rootdir` and
`pythonpath`):

```text
tests/unit/application/test_media_suggestion.py
tests/unit/application/test_media_analysis_lifecycle.py
tests/contract/test_media_suggestion_api.py
tests/contract/test_companion_review_api.py
tests/unit/infrastructure/persistence/test_companion_review_repository.py
tests/contract/test_x_route_policy.py
```

Outcome: **105 passed in 17.46s**. Lifecycle file re-run after a test-fake
cleanup: **20 passed**. No failed suite. Ambient encodings signature not
observed.

Proven claims:

- Successful imported preview persists a generic analyzed run; admin inbox
  lists it; ordinary owner of cataloged X gets `analyzed=true` and
  `unopened_count` +1; Alice ⊈ Bob
  (`test_imported_preview_joins_inbox_and_own_history`).
- Movie media does not join (unit skip + contract extra-movie preview writes
  no run and is absent from inbox).
- Library-candidate preview still does not write runs (`provider.calls`
  increments; `media_analysis_runs` count unchanged).
- No second `provider.suggest` per preview (unit `provider.calls == 1`;
  contract one increment per POST).
- Existing companion isolation and four-mutation tests still pass
  (`test_companion_review_api.py`, `test_companion_review_repository.py`,
  `test_x_route_policy.py`).

Node: not required (no JS change).

## Git write result

One normal commit in w7; explicit paths only; no `git add -A`; no push; no
force; no rebase.

```text
fb59c42a8e3a32d9476581beeabba0eb9c04109a
```

Parent: `977a7af80afed16745adb0ef8e939555e5e21cce`.

## Deviations, risks, missing evidence

- Isolated-worktree `ap exec --root <w7>` is an environment limitation
  (no `.venv`). Task-specific deviation: canonical `--root` plus pytest
  `--rootdir` / `-o pythonpath=<w7>/src`, with proven w7 `framenest.__file__`.
- If an active run is already `analyzing` (durable executor in flight), the
  join skips persist so it does not steal that row. Interactive preview JSON
  is still returned. Not the ordinary Analyze-by-AI path.
- `docs/X_COMPANION.md` not edited: present-tense “website Analyze-by-AI
  successes join” is now implemented on the imported preview path.
- Live NUC / Brave companion not exercised (forbidden).

## One smallest next step (ORCHESTRATOR)

Issue independent fresh-worker acceptance of `fb59c42a8e3a32d9476581beeabba0eb9c04109a`
against item 9 (ordinary own-history unopened after Analyze by AI) plus original
R1–R3′ risk claims that this persist could affect. This Worker does not
self-accept.

## Authority expiry

This report terminates FRAMENEST-COMPANIE-ITEM9JOIN-01. No follow-on action,
acceptance, publication, push, NUC access, provider call, R4, Edit/AI apply UX,
or logical-whole closure is authorized.

```text
Resolved Execution Issues / Near-Misses: isolated worktree `--root` declared CPython missing (no `.venv`); cause: expected isolated-worktree launch-path miss; resolution: classified environment limitation, canonical `--root` plus pytest `--rootdir`/`pythonpath` with proven w7 `src/framenest/__init__.py`; ambient AppImage/loader classes (`APPIMAGE`, `APPDIR`, `LD_LIBRARY_PATH`, inherited `PATH`, `SSH_AUTH_SOCK`) present in the parent; resolution: `./.ap/ap` sanitized-v1 re-exec; residual risk: none for this correction (no ambient Python used for evidence).
Pre-Existing Failure Classification: none
```

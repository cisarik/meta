### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 10
Worker exchange ordinal: 01
Task identity: FRAMENEST-COMPANIE-ITEM9REACC-01
```

Status: **PASS**  
Phase-qualified result: `acceptance-PASS`  
Logical-whole closure: not-closed  
Implementation-PASS: not emitted (not this session’s role)  
Report justification: `new-evidence`

This session did not implement `fb59c42a8e3a32d9476581beeabba0eb9c04109a` or
`2aead540ee39a81a96425902f85e9b9a34f0d690`. Independence conflict: none.
Sessions 07–09 expired at their terminal reports; those reports are claims.
w7, w8, and w9 were not the acceptance working copy. No product edits. No
publication. No NUC. No Edit/AI per-field apply, R4, or VPS.

The two tests inverted in `08_report_00.md` now pass on this candidate. No
escalation.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; client-presented identity |
| Reasoning | High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Plan Mode off; inspection, authorized `ap exec`, one probe, one report | directly observed |
| Permission mode | not named | unknown/not observably exposed | unknown |
| Repository | Fresh isolated checkout of `2aead54…` | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w10`; detached `2aead54…` | directly observed |
| Canonical checkout | Remain `977a7af…` tracked-clean | `/home/agile/Projects/framenest`; `feat/x-meme-browser-companion`; HEAD `977a7af80afed16745adb0ef8e939555e5e21cce`; porcelain empty | directly observed |
| w3 / w4 | Still `977a7af…` (read-only) | both `977a7af80afed16745adb0ef8e939555e5e21cce` | directly observed |
| w7 / w8 | Unused as working copy; still `fb59c42…` | both `fb59c42a8e3a32d9476581beeabba0eb9c04109a` | directly observed |
| w9 | Unused as working copy; still `2aead54…` | path unused; HEAD `2aead540ee39a81a96425902f85e9b9a34f0d690` | directly observed |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | w10 gitlink and `.ap` HEAD equal the pin | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; worktree `--root` miss classified; canonical `--root` plus pytest `pythonpath` / `--rootdir` | directly observed |
| Network, NUC, SSH, sudo, providers, browser | Credential-free `ls-remote` of public `main` only | `origin refs/heads/main` = `977a7af…`; no NUC/SSH/sudo/providers/browser | directly observed |
| Git | Worktree add + worktree-local `.ap` init only | No commits, no `git add`, no push | directly observed |
| Independence | Required fresh independent | This session did not author `fb59c42…` or `2aead54…` | directly observed |

Capability, permission, and client identity did not expand task authority.
Native planning mode observed off.

## Fresh checkout and provenance

| Fact | Observed |
|---|---|
| Fresh-checkout path | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w10` |
| Candidate SHA | `2aead540ee39a81a96425902f85e9b9a34f0d690` |
| Immediate parent | `fb59c42a8e3a32d9476581beeabba0eb9c04109a` |
| Candidate tree | `0900818f57326017712c07686c49de61d534507f` |
| Range vs public main | `fb59c42…` (persist) then `2aead54…` (tests) |
| Canonical after worktree add and after tests | still `977a7af…` on `feat/x-meme-browser-companion`, tracked-clean |
| AP pin (gitlink and w10 `.ap` HEAD) | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| Public `refs/heads/main` (`git ls-remote origin refs/heads/main`) | `977a7af80afed16745adb0ef8e939555e5e21cce` |
| w9 unused as working copy | yes; remains `2aead54…` at its own path |
| w10 porcelain after submodule init and after tests | empty |

RF-12: clean isolated worktree; no classification stop. Canonical, w3, w4, w7,
w8, and w9 not mutated. Start SHA equals end SHA on every named checkout.

## Diff path set vs claimed 8 files

`git diff --name-only 977a7af… 2aead54…` is exactly the claimed eight paths
(`+604 / −6`):

1. `src/framenest/application/media_suggestion.py`
2. `src/framenest/application/media_analysis_lifecycle.py`
3. `src/framenest/adapters/api/application.py`
4. `src/framenest/adapters/api/media_suggestion_api.py`
5. `tests/unit/application/test_media_suggestion.py`
6. `tests/unit/application/test_media_analysis_lifecycle.py`
7. `tests/contract/test_media_suggestion_api.py`
8. `tests/contract/test_companion_review_api.py`

`git diff --name-only fb59c42… 2aead54…` is exactly the two test files
(`+12 / −5`). No `src/` in that delta.

Forbidden-path absence vs `977a7af…`: no JS/HTML/CSS; no `docs/adr/0067*` /
`0073*` body edits; no `SECURITY.md`; no `docs/X_COMPANION.md`; no Alembic
`0034*` (schema versions end at `0033_media_analysis_proposals.py`); no
`.venv`. Node not required (JS diff empty). JS in the range would have failed
the candidate; it is empty.

Test-only delta vs `fb59c42…` matches the session-09 claim by object, not by
that report: POSTs in `test_imported_preview_joins_inbox_and_own_history` use
`_mutation_headers(ADMIN_LOGIN)` (default Origin = `EXTERNAL_ORIGIN`); fake
`create_manual_pending` emits a distinct id on each new pending create.

## `ap project check` / `runtime-info` / provenance / test-focus

### Worktree `--root` (declared route first)

```text
./.ap/ap project check --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w10 \
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

Temporary `/tmp/framenest-item9reacc-10-provenance.py` (outside both git
checkouts), one pytest function, collected through authorized `test-focus` with
`--rootdir` / `pythonpath` on w10. Printed path:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w10/src/framenest/__init__.py
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
tests/unit/infrastructure/persistence/test_companion_review_repository.py
tests/contract/test_x_route_policy.py
tests/contract/test_tailscale_ingress_security.py
tests/contract/test_adr_0073.py
tests/contract/test_automatic_analysis_privacy_contract.py
```

Outcome: **205 passed in 65.50s**. Zero failed. Ambient encodings signature
not observed. Node: not required (JS diff empty). Session 08 collected the
same 205 with two red; both previously inverted tests are in this passing
set. Candidate is not failed for the known worktree launch-path miss.

## Per-control map

| Control | Result | Evidence |
|---|---|---|
| Previously inverted: `test_imported_preview_joins_inbox_and_own_history` | **pass** | POSTs use `_mutation_headers(ADMIN_LOGIN)` (Origin = `EXTERNAL_ORIGIN`, not `COMPANION_ORIGIN`; `X-FrameNest-Request: 1`). GET inbox/own-history use `_serve_headers`. First preview 200, not 403. Admin inbox lists Alice `analyzed=true` `unopened=true`. Alice `unopened_count == 1`. Bob 0 and Alice’s media absent from Bob. Movie writes no run. Library-scan writes no run. Provider increments by one per POST (`calls` 1→2→3→4). |
| Previously inverted: `test_imported_preview_join_supersedes_prior_terminal_success` | **pass** | `first.id != second.id`; two persist cycles (`create_manual_pending`, `claim_pending`, `record_analyzed` twice); `save_calls == 0`. |
| Item 9 join (primary) | **proven** | Owning HTTP join above. Unit `test_imported_preview_join_records_generic_analyzed_run_without_executor` passed (generic analyzed run; `create_manual_pending` → `claim_pending` → `record_analyzed`; `save_calls == 0`). Latest Alice row: `automatic_post_catalog` / `generic_media` / `analyzed`. |
| No second `provider.suggest` | **proven** | Unit `test_imported_preview_invokes_join_once_without_second_provider_call` (`provider.calls == 1`). HTTP join increments by one per POST. `PreviewImportedMediaSuggestion.execute` calls `provider.suggest` once then optional join. `ExecuteAutomaticMediaAnalysisRun` is not referenced from `media_suggestion.py`. |
| Exclusions (movie / library-scan / analyzing / no metadata save) | **proven** | Unit movie skip and analyzing skip passed; `save_calls == 0` passed. Contract movie-absent-from-inbox and library-scan non-write now reached after 200. |
| Production DI | **proven by inspection** | Default `create_app` injects `PersistImportedPreviewAnalysis(owned_media_analysis_run_repository, owned_media_metadata_repository)` into `PreviewImportedMediaSuggestion` when the provider and both repositories exist. Engine path creates both repositories. Hand-wired contract test does not replace this inspection. |
| Preview capability `analysis.run`, not `companion_mutation` | **proven** | `tailscale_ingress.py` preview policy: `capability=CAPABILITY_ANALYSIS_RUN`; `companion_mutation` default false. Ordinary role lacks `analysis.run` (`test_ordinary_user_direct_privileged_calls_fail` passed, includes this POST → 403 `CAPABILITY_DENIED`). |
| Exactly four `companion_mutation` | **proven** | Four `companion_mutation=True` policies (X submit, X retry, opened, apply). `test_only_companion_mutations_are_companion_flagged` passed. GET own-history is not a mutation. |
| No Alembic 0034; schema head 0033; flag off in git | **proven** | Versions end at `0033_media_analysis_proposals.py`. `test_current_schema_head_is_0033` passed. `automatic_media_analysis_enabled: bool = Field(default=False)`. Diff does not enable the flag. `test_automatic_analysis_privacy_contract.py` passed. |
| Join failure sanitized 500 `ANALYSIS_JOIN_FAILED` | **proven** | `test_imported_preview_join_failure_is_sanitized_server_error` passed (loopback client, not Tailscale). |
| Own-analyzed `unopened_count` (not global subquery) | **proven (pre-existing + join path)** | `test_own_history_opened_isolation_does_not_use_global_unopened_count` passed. Join-path Alice `unopened_count == 1` / Bob `0`. |
| Residual R1 chrome (hosted hide Analyze by AI) | **proven empty JS diff** | No JS in `git diff --name-only`. Node not run. |

## Trust-boundary confirmation list

| Claim | Result |
|---|---|
| Ordinary cannot POST preview | Proven: ordinary lacks `analysis.run`; Tailscale privileged-call matrix 403 `CAPABILITY_DENIED` on this POST. |
| Ordinary foreign/unknown opened 404 | Proven by existing companion contract tests in the same matrix (passed). |
| Apply 403 for ordinary | Proven (passed companion tests). |
| Inbox list/detail 403 for ordinary | Proven (passed companion tests). |
| Exactly four `companion_mutation` | Proven. |
| Own-analyzed unopened count | Proven by isolation tests and by the join-path Alice/Bob assertions. |
| Alice ⊈ Bob on the **join** path | **Proven**: after persist, Alice own-history lists her analyzed item; Bob’s items omit Alice’s media and `unopened_count == 0`. |

Ordinary still cannot write analysis runs through this path: persist is behind
`analysis.run`. Owning HTTP join POSTs use Tailscale mutation headers with
`EXTERNAL_ORIGIN`, not `COMPANION_ORIGIN`. No trust-boundary claim in the
control matrix is unproven.

## Named deviations (judge)

1. Contract join test injects `PersistImportedPreviewAnalysis` by hand.
   **accepted-continuation**: default `create_app` still wires the join when
   the provider and both repositories exist.
2. Active `analyzing` run: join skips; preview would still return. Unit
   `test_imported_preview_join_skips_when_latest_active_run_is_analyzing`
   passed. **accepted-continuation**.
3. Join failure after `provider.suggest` is sanitized 500; provider already
   called. Unit/contract failure path passed. Residual billing/UX, not a
   license to call suggest twice. **accepted-continuation**.
4. `docs/X_COMPANION.md` / `SECURITY.md` unchanged. Present-tense “website
   Analyze-by-AI successes join” is implemented in product code and proven by
   the owning HTTP join. Not a blocking present-tense contradiction. Residual:
   docs were not rewritten in this unpublished range.
5. Test-only delta `fb59c42…..2aead54…`: mutation headers + distinct fake ids.
   Confirmed no product change in that range. **accepted-continuation** of the
   authorized second correction; this session does not re-correct.

## Sanitization compliance

No secrets, identity-map values, Tailscale hostnames, live titles, tweet URLs,
cookies, companion PEM, or EnvironmentFile values. Synthetic UUIDs and example
logins only. `ls-remote` used `origin refs/heads/main` without printing
credentials. Fixture `EXTERNAL_ORIGIN` in tests is the synthetic
`https://nuc-1.example.ts.net`, not a live hostname.

## Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification

```text
Resolved Execution Issues / Near-Misses: isolated worktree `--root` declared CPython missing (no `.venv`); cause: expected isolated-worktree launch-path miss; resolution: classified environment limitation, canonical `--root` plus pytest `--rootdir`/`pythonpath` with proven w10 `src/framenest/__init__.py`. Ambient AppImage/loader classes (`APPIMAGE`, `APPDIR`, `LD_LIBRARY_PATH`, inherited `PATH`, `SSH_AUTH_SOCK`) present in the parent; resolution: `./.ap/ap` sanitized-v1 re-exec; residual risk: none for this acceptance (no ambient Python used for evidence).
Pre-Existing Failure Classification: none for the declared matrix. Session 08 PARTIAL (403 on owning join; reused fake id) is not reproduced on `2aead54…`.
```

## Residual risk / missing evidence

- Isolated-worktree `ap exec --root <w10>` is an environment limitation. Task
  specific deviation as authorized: canonical `--root` plus pytest `--rootdir`
  / `-o pythonpath=<w10>/src`, with proven w10 `framenest.__file__`.
- Live NUC / Brave companion not exercised (forbidden). Rendered item-9
  re-test remains a Cooperator step after publication and routine
  `framenest-release`.
- This session does not publish, merge, or deploy.

## One smallest next step (ORCHESTRATOR)

Classify this `acceptance-PASS`. Then, only with an explicit Cooperator
publication grant of exact `2aead540ee39a81a96425902f85e9b9a34f0d690`,
sequence routine NUC `framenest-release` and rendered re-test of **item 9**.
This Worker does not close, publish, merge, or deploy.

Do not issue another automatic test correction. The previously inverted tests
now pass.

## Authority expiry

This report terminates FRAMENEST-COMPANIE-ITEM9REACC-01. No follow-on action,
correction, publication, push, NUC access, provider call, R4, Edit/AI apply UX,
or logical-whole closure is authorized.

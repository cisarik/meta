### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-companion-brave-testing-resume
Worker session ordinal: 08
Worker exchange ordinal: 01
Task identity: FRAMENEST-COMPANIE-ITEM9ACC-01
```

Status: **PARTIAL**  
Phase-qualified result: not `acceptance-PASS` (Python gates red; named item-9 owning test inverted)  
Logical-whole closure: not-closed  
Implementation-PASS: not emitted (not this session’s role)  
Report justification: `new-evidence`

This session did not implement `fb59c42a8e3a32d9476581beeabba0eb9c04109a`.
Independence conflict: none. Session 07 authority expired at `07_report_00.md`;
that report is a claim and is not reproduced for the two red tests below.
w7 was not the acceptance working copy. No product edits. No publication. No
NUC. No Edit/AI per-field apply, R4, or VPS.

## Capability handshake

| Material row | Requested | Observed or unknown | Evidence class |
|---|---|---|---|
| Product/client | Cursor Worker | Cursor Grok 4.6; not independently attested | requested; client-presented identity |
| Reasoning | High | Effective reasoning SKU not exposed | requested; unknown/not observably exposed |
| Native planning mode | `not-used` | Plan Mode off; inspection, authorized `ap exec`, one probe, one report | directly observed |
| Permission mode | not named | unknown/not observably exposed | unknown |
| Repository | Fresh isolated checkout of `fb59c42…` | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w8`; detached `fb59c42…` | directly observed |
| Canonical checkout | Remain `977a7af…` tracked-clean | `/home/agile/Projects/framenest`; `feat/x-meme-browser-companion`; HEAD `977a7af80afed16745adb0ef8e939555e5e21cce`; porcelain empty | directly observed |
| w3 / w4 | Still `977a7af…` (read-only) | both `977a7af80afed16745adb0ef8e939555e5e21cce` | directly observed |
| w7 | Unused as working copy; still `fb59c42…` | path unused; HEAD `fb59c42a8e3a32d9476581beeabba0eb9c04109a` | directly observed |
| AP pin | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` | w8 gitlink and `.ap` HEAD equal the pin | directly observed |
| Python evidence | `./.ap/ap project check` and `./.ap/ap exec` with exact baseline | Used; worktree `--root` miss classified; canonical `--root` plus pytest `pythonpath` / `--rootdir` | directly observed |
| Network, NUC, SSH, sudo, providers, browser | Credential-free `ls-remote` of public `main` only | `origin refs/heads/main` = `977a7af…`; no NUC/SSH/sudo/providers/browser | directly observed |
| Git | Worktree add + worktree-local `.ap` init only | No commits, no `git add`, no push | directly observed |
| Independence | Required fresh independent | This session did not author `fb59c42…` | directly observed |

Capability, permission, and client identity did not expand task authority.

## Fresh checkout and provenance

| Fact | Observed |
|---|---|
| Fresh-checkout path | `/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w8` |
| Candidate SHA | `fb59c42a8e3a32d9476581beeabba0eb9c04109a` |
| Parent SHA | `977a7af80afed16745adb0ef8e939555e5e21cce` |
| Canonical after worktree add and after tests | still `977a7af…` on `feat/x-meme-browser-companion`, tracked-clean |
| AP pin (gitlink and w8 `.ap` HEAD) | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| Public `refs/heads/main` (`git ls-remote origin refs/heads/main`) | `977a7af80afed16745adb0ef8e939555e5e21cce` |
| w7 unused as working copy | yes; remains `fb59c42…` |
| w8 porcelain after submodule init | empty |

RF-12: clean isolated worktree; no classification stop. Canonical, w3, w4, and
w7 not mutated.

## Diff path set vs claimed 8 files

`git diff --name-only 977a7af… fb59c42…` is exactly the claimed eight paths
(`+596 / −5`):

1. `src/framenest/application/media_suggestion.py`
2. `src/framenest/application/media_analysis_lifecycle.py`
3. `src/framenest/adapters/api/application.py`
4. `src/framenest/adapters/api/media_suggestion_api.py`
5. `tests/unit/application/test_media_suggestion.py`
6. `tests/unit/application/test_media_analysis_lifecycle.py`
7. `tests/contract/test_media_suggestion_api.py`
8. `tests/contract/test_companion_review_api.py`

Forbidden-path absence: no JS/HTML/CSS in the diff; no `docs/adr/0067*` /
`0073*` body edits; no `SECURITY.md`; no `docs/X_COMPANION.md`; no Alembic
`0034*` (schema versions end at `0033_media_analysis_proposals.py`); no
`.venv`. Parent of `fb59c42…` is `977a7af…`.

## `ap project check` / `runtime-info` / provenance / test-focus

### Worktree `--root` (declared route first)

```text
./.ap/ap project check --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w8 \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce
./.ap/ap exec --root /home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w8 \
  --baseline 977a7af80afed16745adb0ef8e939555e5e21cce --operation runtime-info
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

Temporary `/tmp/framenest-item9acc-08-provenance.py` (outside both git
checkouts). First collection: pytest exit 5 `no tests ran` (module-level
script, not a test). Rewritten as one pytest function; collected through
authorized `test-focus` with `--rootdir` / `pythonpath` on w8. Printed path:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-brave-testing-resume-w8/src/framenest/__init__.py
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

Outcome: **2 failed, 203 passed in 65.42s**. Ambient encodings signature not
observed. Node: not required (JS diff empty).

First failing suite is not skipped; both reds are in the declared matrix.
Classification of each red gate: **candidate** (committed tests inverted).
Not harness-outside-candidate, not ambient-route, not environment, not
acceptance-limitation. Candidate is not failed for the known worktree
launch-path miss.

#### Failure 1 — `test_imported_preview_join_supersedes_prior_terminal_success`

File: `tests/unit/application/test_media_analysis_lifecycle.py`.

```text
E AssertionError: assert MediaAnalysisRunId(value='22222222-2222-4222-8222-222222222222')
  != MediaAnalysisRunId(value='22222222-2222-4222-8222-222222222222')
```

`_FakeRepository.create_manual_pending` hardcodes the same pending id on every
superseding create. The unit assertion `first.id != second.id` cannot hold.
This does not prove a product persist uniqueness defect; the fake cannot emit
distinct ids. The named uniqueness claim is **inverted**.

#### Failure 2 — `test_imported_preview_joins_inbox_and_own_history`

File: `tests/contract/test_companion_review_api.py` (named owning test).

```text
E assert 403 == 200
  + where 403 = <Response [403 Forbidden]>.status_code
```

The test POSTs `…/ai-suggestion-preview` under `ingress_mode=tailscale_uds`
with `_serve_headers` only (no `Origin`, no `X-FrameNest-Request`). Unsafe
methods require both; missing origin yields 403
`MUTATION_ORIGIN_FORBIDDEN` before the join runs. The same file already has
`_mutation_headers`. Preview is `capability=analysis.run` and
`companion_mutation=False`, so Origin must be `EXTERNAL_ORIGIN`, not a
companion-extension origin. Item 9 HTTP join (admin inbox, ordinary
own-history, Alice ⊈ Bob, movie skip, library-scan non-persist, second POST
run increment) is **unproven**. `07_report_00.md` claimed this test passed;
this session does not reproduce that claim.

## Per-control map

| Control | Result | Evidence |
|---|---|---|
| Item 9 join (primary) | **unproven / inverted owning test** | Owning `test_imported_preview_joins_inbox_and_own_history` is 403 before persist. Unit `test_imported_preview_join_records_generic_analyzed_run_without_executor` passed (generic analyzed run; `create_manual_pending` → `claim_pending` → `record_analyzed`; `save_calls == 0`). |
| No second `provider.suggest` | **unit proven; HTTP increment unproven** | `test_imported_preview_invokes_join_once_without_second_provider_call` passed (`provider.calls == 1`). Contract join never reached 200. `PreviewImportedMediaSuggestion.execute` calls `provider.suggest` once then optional join. `ExecuteAutomaticMediaAnalysisRun` is not referenced from `media_suggestion.py`. |
| Exclusions (movie / library-scan / analyzing / no metadata save) | **unit proven; HTTP movie/library unproven** | Unit movie skip and analyzing skip passed; `save_calls == 0` passed. Contract movie-absent-from-inbox and library-scan non-write sit behind the 403. |
| Production DI | **proven by inspection** | Default `create_app` injects `PersistImportedPreviewAnalysis(owned_media_analysis_run_repository, owned_media_metadata_repository)` into `PreviewImportedMediaSuggestion` when the provider and both repositories exist (engine path creates both). Hand-wired contract test does not replace this inspection. |
| Preview capability `analysis.run`, not `companion_mutation` | **proven** | `tailscale_ingress.py` preview policy: `capability=CAPABILITY_ANALYSIS_RUN`; `companion_mutation` default false. Ordinary role lacks `analysis.run` (`identity_access.py`; `test_resolve_identity_maps_ordinary_user_with_read_capabilities`; `test_ordinary_user_direct_privileged_calls_fail` includes this POST → 403 `CAPABILITY_DENIED`). |
| Exactly four `companion_mutation` | **proven** | Four `companion_mutation=True` policies; `test_only_companion_mutations_are_companion_flagged` passed. GET own-history is not a mutation. |
| No Alembic 0034; schema head 0033; flag off in git | **proven** | Versions end at `0033_media_analysis_proposals.py`. `automatic_media_analysis_enabled: bool = Field(default=False)`. Diff does not enable the flag. `test_automatic_analysis_privacy_contract.py` passed. |
| Join failure sanitized 500 `ANALYSIS_JOIN_FAILED` | **proven** | `test_imported_preview_join_failure_is_sanitized_server_error` passed (loopback client, not Tailscale). |
| Own-analyzed `unopened_count` (not global subquery) | **proven (pre-existing)** | `test_own_history_opened_isolation_does_not_use_global_unopened_count` and related companion isolation tests passed. |
| Residual R1 chrome (hosted hide Analyze by AI) | **proven empty JS diff** | No JS in `git diff --name-only`. Node not run. |

## Trust-boundary confirmation list

| Claim | Result |
|---|---|
| Ordinary cannot POST preview | Proven: ordinary lacks `analysis.run`; Tailscale privileged-call matrix 403 `CAPABILITY_DENIED` on this POST. |
| Ordinary foreign/unknown opened 404 | Proven by existing companion contract tests in the same matrix (passed). |
| Apply 403 for ordinary | Proven (passed companion tests). |
| Inbox list/detail 403 for ordinary | Proven (passed companion tests). |
| Exactly four `companion_mutation` | Proven. |
| Own-analyzed unopened count | Proven by isolation tests (passed). |
| Alice ⊈ Bob on the **join** path | **Unproven** (owning join test never listed history). Pre-existing Alice/Bob isolation tests passed. |

Ordinary still cannot write analysis runs through this path: persist is behind
`analysis.run`. That trust claim is not the cause of PARTIAL.

## Classification of named deviations

1. Contract join test injects `PersistImportedPreviewAnalysis` by hand.
   **accepted-continuation** for DI: default `create_app` still wires the join.
   The same test is separately **defect requiring correction** for missing
   unsafe-method headers (see Failure 2).
2. Active `analyzing` run: join skips; preview would still return. Unit
   `test_imported_preview_join_skips_when_latest_active_run_is_analyzing`
   passed. **accepted-continuation**.
3. Join failure after `provider.suggest` is sanitized 500; provider already
   called. Unit/contract failure path passed. Residual billing/UX, not a
   license to call suggest twice. **accepted-continuation**.
4. `docs/X_COMPANION.md` / `SECURITY.md` unchanged. Present-tense “website
   Analyze-by-AI successes join” is implemented in product code by inspection;
   HTTP listing proof is missing because the owning test is inverted. Not a
   present-tense contradiction that this session may rewrite. Residual: do not
   close item 9 on `07_report_00.md` alone.

## Sanitization compliance

No secrets, identity-map values, Tailscale hostnames, live titles, tweet URLs,
cookies, companion PEM, or EnvironmentFile values. Synthetic UUIDs and example
logins only. `ls-remote` used `origin refs/heads/main` without printing
credentials.

## Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification

```text
Resolved Execution Issues / Near-Misses: isolated worktree `--root` declared CPython missing (no `.venv`); cause: expected isolated-worktree launch-path miss; resolution: classified environment limitation, canonical `--root` plus pytest `--rootdir`/`pythonpath` with proven w8 `src/framenest/__init__.py`. First provenance collection: pytest exit 5 `no tests ran` because the probe was not a test function; resolution: one pytest wrapper, `1 passed`, probe deleted. Ambient AppImage/loader classes (`APPIMAGE`, `APPDIR`, `LD_LIBRARY_PATH`, inherited `PATH`, `SSH_AUTH_SOCK`) present in the parent; resolution: `./.ap/ap` sanitized-v1 re-exec; residual risk: none for this acceptance (no ambient Python used for evidence).
Pre-Existing Failure Classification: none for the declared matrix other than the two candidate test defects above. Session 07 claim that those two tests passed is not reproduced.
```

## Deviations, residual risk, missing evidence

- Isolated-worktree `ap exec --root <w8>` is an environment limitation. Task
  specific deviation as authorized: canonical `--root` plus pytest `--rootdir`
  / `-o pythonpath=<w8>/src`, with proven w8 `framenest.__file__`.
- Item 9 companion listing after imported Analyze-by-AI is **missing evidence**
  because the owning HTTP test never passes ingress.
- Unit supersession uniqueness is **missing evidence** because the fake reuses
  one hardcoded id.
- Live NUC / Brave companion not exercised (forbidden).
- Ordinary correction budget for this logical whole is already consumed (one
  primary fresh acceptance of `977a7af…`, one automatic correction producing
  `fb59c42…`, this full-fresh re-acceptance). A further correction is not
  self-granted.

## One smallest next step (ORCHESTRATOR)

Do **not** accept `fb59c42…`. Do **not** publish, merge, or run
`framenest-release`.

The two red gates are inverted tests in the candidate, not a demonstrated
second `provider.suggest`, fifth `companion_mutation`, schema `0034`, or
ordinary write of analysis runs.

If a **second** bounded correction is explicitly granted despite the exhausted
ordinary correction budget, keep it test-only on the existing eight-path
allowlist:

1. `test_imported_preview_joins_inbox_and_own_history`: POST preview with
   `_mutation_headers(ADMIN_LOGIN)` (Origin = `EXTERNAL_ORIGIN`; preview is not
   `companion_mutation`).
2. `_FakeRepository.create_manual_pending`: distinct run ids on each
   superseding create so `first.id != second.id` can be a real assertion.

Escalate (`NEEDS_ORCHESTRATOR_DECISION`) if that second correction is refused
or if a later recheck still cannot prove the HTTP join. This Worker does not
correct, close, publish, or deploy.

## Authority expiry

This report terminates FRAMENEST-COMPANIE-ITEM9ACC-01. No follow-on action,
correction, publication, push, NUC access, provider call, R4, Edit/AI apply UX,
or logical-whole closure is authorized.

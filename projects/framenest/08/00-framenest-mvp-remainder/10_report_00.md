### Report for ORCHESTRATOR_CHAT

Logical whole: `framenest-companion-r4-automatic-analysis-settings-mvp`  
Worker session: `10`  
Worker exchange: `01`

Status: **PASS**

Phase-qualified result: `acceptance-PASS`  
Result artifact or commit: `472553cadcd3d4ca87a9792a2c306bd0afeea7c1`  
Logical-whole closure: `not-closed`

```text
Acceptance candidate: 472553cadcd3d4ca87a9792a2c306bd0afeea7c1
Acceptance owner map: Cooperator-accepted plan 06_report_00.md plus implementation grant 07_implementation_00.md plus correction grant 09_correction_00.md plus candidate ADR-0079
Acceptance allowlist: inspection of the 27 committed paths only (against baseline 1eee09c1); no product edits
Acceptance risk claims: runtime settings store persists setting across process restarts without schema 0034; dynamic scheduler check; exactly 5 companion_mutation routes; capability provider.operate required; ordinary 403; extension Settings shows Administration for admin only; confirm on enable; default in git remains false; ADR-0079 added; provenance tests checkout-independent
Acceptance control matrix: see § Control Matrix
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
Independence: this session did not author 472553cadcd3d4ca87a9792a2c306bd0afeea7c1, 687b5afd933d2ffce418eb6e57f03efb3ed141bf, f04bc232dd832b796f9c0ec183500d6da54af40e, or 22847b7d12a97c7d84b520d9f8cb46cdef12952b
```

All ten positive control-matrix rows hold on the candidate object. Declared Python evidence is green (112 passed in the five named files). Declared Node evidence is green (32 pass, 0 fail). Session 08’s PARTIAL cause — `test_candidate_source_provenance` bound to directory name `…-mvp-w2` — does not hold on this candidate: the committed assertion is checkout-relative and passed on independent checkout `…-mvp-w5`.

## Worktree and Git

- Fresh checkout: `/home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w5` (detached `472553cadcd3d4ca87a9792a2c306bd0afeea7c1`, tree `89e7ef169eeac78ef0a53e205d72d1d693a5a431`, tracked-clean)
- Ancestry: `git merge-base --is-ancestor 1eee09c1afcfe41b2a411784f8c43c428e610b9b HEAD` succeeded; `git rev-list --count 1eee09c1…..HEAD` = 4
- Commits on the candidate: `22847b7d12a97c7d84b520d9f8cb46cdef12952b` (server store + PUT + Python tests), `f04bc232dd832b796f9c0ec183500d6da54af40e` (companion UI + JS tests), `687b5afd933d2ffce418eb6e57f03efb3ed141bf` (docs + ADR-0079), `472553cadcd3d4ca87a9792a2c306bd0afeea7c1` (checkout-independent provenance assertion)
- Canonical `/home/agile/Projects/framenest`: still `1eee09c1afcfe41b2a411784f8c43c428e610b9b` on `feat/x-meme-browser-companion`, tree `bd160c2a7f9a34c689a08b0e5facff3e426f127f`, tracked-clean (re-verified before worktree add, after add, and after tests)
- Public `refs/heads/main`: `1eee09c1afcfe41b2a411784f8c43c428e610b9b` (credential-free `git ls-remote`)
- Pinned submodule: `.ap` gitlink == `.ap` HEAD == `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` on canonical and on w5
- Session-07 worktree `…-mvp-w2`: still `687b5afd933d2ffce418eb6e57f03efb3ed141bf`, tracked-clean; not used as working copy; not edited
- Session-08 checkout `…-mvp-w3`: still `687b5afd933d2ffce418eb6e57f03efb3ed141bf`, tracked-clean; not used as working copy; not edited
- Session-09 worktree `…-mvp-w4`: still `472553cadcd3d4ca87a9792a2c306bd0afeea7c1`, tracked-clean; not used as working copy; not edited
- Git writes this session: `worktree add --detach` of w5 and worktree-local `submodule update --init .ap` only. No product commits, add, push, or canonical checkout of the candidate.

## Path set versus parent `1eee09c1…`

Exactly these 27 files (`git diff --name-only`); 1698 insertions / 37 deletions:

1. `PRODUCT.md`
2. `README.md`
3. `SECURITY.md`
4. `SPEC.md`
5. `deploy/systemd/framenest.env.example`
6. `docs/BACKUP_AND_RECOVERY.md`
7. `docs/X_COMPANION.md`
8. `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md`
9. `docs/adr/README.md`
10. `extension/background/service_worker.js`
11. `extension/shared/messages.js`
12. `extension/ui/sidebar.css`
13. `extension/ui/sidebar.html`
14. `extension/ui/sidebar.js`
15. `src/framenest/adapters/api/application.py`
16. `src/framenest/adapters/api/media_analysis_lifecycle_api.py`
17. `src/framenest/adapters/api/runtime_settings_api.py`
18. `src/framenest/adapters/api/tailscale_ingress.py`
19. `src/framenest/application/media_analysis_lifecycle.py`
20. `src/framenest/configuration.py`
21. `src/framenest/infrastructure/runtime_settings.py`
22. `tests/companion_settings_automatic_analysis.test.js`
23. `tests/contract/test_automatic_analysis_privacy_contract.py`
24. `tests/contract/test_automatic_analysis_settings_api.py`
25. `tests/contract/test_tailscale_ingress_security.py`
26. `tests/contract/test_x_route_policy.py`
27. `tests/unit/test_runtime_settings_store.py`

Diff versus correction parent `687b5af…`: `tests/unit/test_runtime_settings_store.py` only (4 insertions / 2 deletions). `test_candidate_source_provenance` asserts `Path(framenest.__file__).resolve() == Path(__file__).resolve().parents[2] / "src" / "framenest" / "__init__.py"`. No `WORKTREE_MARKER`.

No extras. No `alembic_environment/versions/0034*`. No persist-join paths. No sixth `companion_mutation` file. ADR bodies 0020 / 0023 / 0044 / 0062 / 0065 / 0066 / 0067 / 0072 / 0073 / 0075 / 0076 / 0077 / 0078: empty diffs.

## Control matrix

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Runtime settings store persists atomic JSON sidecar (`runtime-settings.json`, mode `0o600`); valid bool in sidecar precedes `FrameNestSettings.automatic_media_analysis_enabled` | hold | Overlay-first then fallback (`runtime_settings.py:58-87`); `_atomic_write_json` tmp + `os.replace` and `os.chmod(..., 0o600)` `:121-152`. Default path `{database_path.parent}/runtime-settings.json` (`configuration.py:32`, `:488-496`). Tests: `test_atomic_write_persists_bool_and_mode`, `test_json_overlay_precedes_fallback`, `test_setting_survives_new_app_on_same_sidecar` (`test_automatic_analysis_settings_api.py:173-192`). |
| 2 | Scheduler reads `store.is_enabled` dynamically via callable; changes take effect immediately without backend restart | hold | `ScheduleAutomaticMediaAnalysis.enabled` is `bool \| Callable[[], bool]` evaluated on access (`media_analysis_lifecycle.py:205-223`); `execute` uses `self.enabled` `:221-223`. `create_app` passes `enabled=runtime_settings_store.is_enabled` and `automatic_analysis_enabled=runtime_settings_store.is_enabled` (`application.py:667-669`, `:725-729`). Capability GET resolves per request (`media_analysis_lifecycle_api.py:186-190`, `:510-515`). Tests: `test_scheduler_callable_is_evaluated_per_execute`, `test_notify_cataloged_follows_callable_flag`. |
| 3 | `PUT /api/admin/settings/automatic-analysis` requires `provider.operate`; ordinary → 403 `CAPABILITY_DENIED` | hold | Route policy `capability=CAPABILITY_PROVIDER_OPERATE`, `companion_mutation=True`, `audit_action="settings.automatic_analysis.put"` (`tailscale_ingress.py:409-416`). `test_ordinary_put_is_capability_denied` (`test_automatic_analysis_settings_api.py:123-131`). `test_x_route_policy.py:79-80`. |
| 4 | Enable without `confirm_cloud_upload: true` returns 422; disable succeeds without extra confirm | hold | API `runtime_settings_api.py:63-71` 422 `CLOUD_CONFIRMATION_REQUIRED`; disable has no confirm branch. Tests: `test_admin_put_enable_requires_confirm_and_persists` (`test_automatic_analysis_settings_api.py:80-120`). Worker also rejects enable without confirm (`service_worker.js:637-639`). |
| 5 | Exactly five `companion_mutation=True` routes (opened, apply, requests POST, retry POST, settings PUT) | hold | Five `companion_mutation=True` assignments: PUT settings `:415`, opened `:553`, apply `:563`, POST `/api/x/requests` `:571`, retry `:580`. Set equality in `test_x_route_policy.py:114-121`. |
| 6 | Companion extension Settings: Administration visible only to connected identities with `provider.operate`; hidden for ordinary/disconnected | hold | HTML `admin-settings` `hidden` by default (`sidebar.html:63-64`). `refreshAdministration` hides without origin or without `hasProviderOperateCapability` (`sidebar.js:662-675`; helper `messages.js:522-525`; `hideAdminSettings` `:625-632`). Tests: `settings HTML keeps Administration below origin controls and hidden by default`; `Administration is hidden when disconnected or ordinary` (`companion_settings_automatic_analysis.test.js:330-432`). Sidebar HTTP uses `request()` only (no `fetch(` in `sidebar.js`). |
| 7 | Confirm dialog shown before enabling automatic analysis in companion Settings | hold | Checkbox ON shows in-sheet confirm, not `window.confirm` (`sidebar.js:719-728`, `sidebar.html:70-77`). Dismiss restores off without PUT (`sidebar.js:738-741`). Confirm copy matches plan. Tests: `admin confirm dismiss does not PUT; confirm enable and disable do` (`companion_settings_automatic_analysis.test.js:435-478`); `doesNotMatch(..., /window\.confirm/)` `:342`. |
| 8 | Git default in `configuration.py` remains `automatic_media_analysis_enabled: bool = Field(default=False)` | hold | `configuration.py:233`. `test_git_tracked_default_remains_false` (`test_automatic_analysis_privacy_contract.py:73-77`). Env example keeps commented `false` (`framenest.env.example:42`). |
| 9 | Schema head remains Alembic `0033`; no `0034_*` migration | hold | Versions dir ends at `0033_media_analysis_proposals.py`. No `0034_*` under `src/framenest/infrastructure/persistence/alembic_environment/versions/`. Path set has no migration. Pre-existing ADR file `docs/adr/0034-canonical-analytic-programming-integration.md` is not an Alembic revision and is not in this diff. |
| 10 | ADR-0079 created and indexed; ADR bodies 0020/0023/0044/0062/0065/0066/0067/0072/0073/0075/0076/0077/0078 untouched | hold | New `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md` (Accepted 2026-08-27). Index row `docs/adr/README.md:106`. Named ADR body diffs vs parent: empty. |
| 11 | Provenance tests are checkout-independent | hold | `test_candidate_source_provenance` (`test_runtime_settings_store.py:32-38`) compares `framenest.__file__` to `Path(__file__).resolve().parents[2] / "src" / "framenest" / "__init__.py"`. Passed on this checkout, whose directory name is `…-mvp-w5`, not `…-mvp-w2`. No hardcoded worktree basename remains in the 27-path set. |

**Negative claims (must not hold):** ordinary Administration / settings PUT — does not hold (403 `CAPABILITY_DENIED`; UI hidden). Sixth `companion_mutation` — does not hold (set size 5). Alembic `0034` migration — does not hold. Tracked git file mutation for the runtime setting value — does not hold (sidecar beside catalog; not a tracked settings file). Hardcoded implementing-worktree directory name in provenance tests — does not hold.

Claim `09_report_00.md` matches this independent inspection for the allowlisted harness correction and for product behavior already accepted as holding in session 08. That report remains a claim; this session’s evidence is the candidate object plus the suites below.

## Validation

Isolated-worktree declared route (expected miss; classified; not repaired):

```text
./.ap/ap project check --root <w5> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
./.ap/ap exec --root <w5> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation runtime-info
# both: ap: ERROR: declared CPython executable does not exist; STOP and report the mismatch without repairing the environment
```

Task-specific RF-16 deviation (canonical `--root`):

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
# ap project check --baseline: PASS

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation runtime-info
# interpreter: /home/agile/Projects/framenest/.venv/bin/python
# framenest.__file__=/home/agile/Projects/framenest/src/framenest/__init__.py
# (envelope only; not candidate provenance)
```

Python matrix (canonical `--root`, w5 `--rootdir` / `pythonpath`):

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b \
  --operation test-focus -- \
  <w5>/tests/unit/test_runtime_settings_store.py \
  <w5>/tests/contract/test_automatic_analysis_settings_api.py \
  <w5>/tests/contract/test_x_route_policy.py \
  <w5>/tests/contract/test_tailscale_ingress_security.py \
  <w5>/tests/contract/test_automatic_analysis_privacy_contract.py \
  -q -p no:cacheprovider -s --rootdir=<w5> -o pythonpath=<w5>/src
# 112 passed in 47.91s
```

`test_candidate_source_provenance` passed on this checkout. Implied candidate `framenest.__file__`:

```text
/home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w5/src/framenest/__init__.py
```

Stopping condition for wrong-tree import was not met. No extra `/tmp` provenance probe was required: the committed checkout-relative assertion is the candidate provenance evidence. `.venv` was not reconstructed. Ambient `python` / `.venv/bin/python` / `poetry run` were not used.

Node from the fresh checkout root:

```text
node --test tests/companion_review_extension.test.js tests/companion_settings_automatic_analysis.test.js
# 32 pass, 0 fail
```

## Deviations

- Isolated-worktree `ap exec --root <w5>` misses declared CPython (known launch-path). Used the prompt’s canonical `--root` plus `--rootdir` / `pythonpath` deviation. `.venv` was not reconstructed. Ambient `python` / `.venv/bin/python` / `poetry run` were not used.
- Envelope `runtime-info` on canonical `--root` prints canonical `framenest.__file__`. Candidate provenance is `test_candidate_source_provenance` under the same `pythonpath`, not that envelope line.

## Risks

Unpublished candidate on an unpushed branch. Residual: NUC and Brave companion will not show Administration until separately authorized publication + routine release update. Rendered UI/UX acceptance remains Cooperator-owned and is not claimed here.

## Out-of-scope observations (ledger-candidates only)

`deploy/systemd/framenest.env.example:59` still says companion mutations are “Flagged only for POST /api/x/requests and POST /api/x/requests/{id}/retry.” That sentence was already stale at parent `1eee09c1…` (four flagged routes) and was not part of this commit’s edited overlay paragraph (`:39-42`). Matches session-07/08 ledger-candidate notes. No ledger write in this session.

Isolated-worktree `ap exec --root <worktree>` still fails `declared CPython executable does not exist`. Matches the existing untriaged non-authorizing ledger entry for consumer-declared execution-route binding.

## Smallest next step

Orchestrator may authorize publication of `472553cadcd3d4ca87a9792a2c306bd0afeea7c1` onto public `main`. No NUC refresh, Brave companion rendered acceptance, or logical-whole closure until that publication plus the routine immutable release update.

## Report justification

`final-acceptance`

## Authority expiry

This acceptance authority expires at this terminal report. No product edits, publication, push, NUC, or closure were granted or performed.

## Resolved Execution Issues / Near-Misses

none beyond the classified isolated-worktree CPython miss, which was the expected RF-16 deviation and was not repaired.

## Pre-Existing Failure Classification

none observed in the authorized Python or Node matrices on this candidate.

## Capability handshake

- Plan Mode: requested `not-used`; observed off (acceptance prompt, no plan-mode transition).
- Reasoning: requested High; observed qualitative depth used for independent diff, control-matrix inspection, correction-delta review, and RF-16 re-run; no independent attestation of a reasoning-level setting.
- Max / enhanced mode: requested off; observed off or unknown (no Max UI control in this session).
- Automatic model selection: off per prompt; not independently attested.
- Context pressure: moderate (27-file candidate, fresh checkout, full-fresh re-acceptance); no containment failure.
- Sub-agents / Explore-style delegation: not used.

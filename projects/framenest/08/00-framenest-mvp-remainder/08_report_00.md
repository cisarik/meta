### Report for ORCHESTRATOR_CHAT

Logical whole: `framenest-companion-r4-automatic-analysis-settings-mvp`  
Worker session: `08`  
Worker exchange: `01`

Status: **PARTIAL**

Phase-qualified result: `not-applicable`  
Result artifact or commit: `687b5afd933d2ffce418eb6e57f03efb3ed141bf`  
Logical-whole closure: `not-closed`

```text
Acceptance candidate: 687b5afd933d2ffce418eb6e57f03efb3ed141bf
Acceptance owner map: Cooperator-accepted plan 06_report_00.md plus implementation grant 07_implementation_00.md plus candidate ADR-0079
Acceptance allowlist: inspection of the 27 committed paths only; no product edits
Acceptance risk claims: runtime settings store persists setting across process restarts without schema 0034; dynamic scheduler check; exactly 5 companion_mutation routes; capability provider.operate required; ordinary 403; extension Settings shows Administration for admin only; confirm on enable; default in git remains false; ADR-0079 added
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates only
Independence: this session did not author 687b5afd933d2ffce418eb6e57f03efb3ed141bf, f04bc232dd832b796f9c0ec183500d6da54af40e, or 22847b7d12a97c7d84b520d9f8cb46cdef12952b
```

Concrete finding that prevents `acceptance-PASS`: committed
`tests/unit/test_runtime_settings_store.py::test_candidate_source_provenance`
asserts directory name
`framenest-companion-r4-automatic-analysis-settings-mvp-w2`. Independent
checkout `…-w3` imports candidate `src/` correctly, so the assertion fails.
Declared Python evidence is therefore not green (1 failed, 111 passed in the
five named files; plus the temporary provenance probe, 1 failed / 112 passed).
All ten positive control-matrix rows hold on the candidate object. This is a
harness leftover in the candidate, not a product-behavior miss.

## Worktree and Git

- Fresh checkout: `/home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w3` (detached `687b5afd933d2ffce418eb6e57f03efb3ed141bf`, tracked-clean)
- Ancestry: `git merge-base --is-ancestor 1eee09c1afcfe41b2a411784f8c43c428e610b9b HEAD` succeeded; `git rev-list --count 1eee09c1…..HEAD` = 3
- Commits on the candidate: `22847b7d12a97c7d84b520d9f8cb46cdef12952b` (server store + PUT + Python tests), `f04bc232dd832b796f9c0ec183500d6da54af40e` (companion UI + JS tests), `687b5afd933d2ffce418eb6e57f03efb3ed141bf` (docs + ADR-0079)
- Canonical `/home/agile/Projects/framenest`: still `1eee09c1afcfe41b2a411784f8c43c428e610b9b` on `feat/x-meme-browser-companion`, tree `bd160c2a7f9a34c689a08b0e5facff3e426f127f`, tracked-clean (re-verified before worktree add, after add, and after tests)
- Public `refs/heads/main`: `1eee09c1afcfe41b2a411784f8c43c428e610b9b` (credential-free `git ls-remote`)
- Pinned submodule: `.ap` gitlink == `.ap` HEAD == `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` on canonical and on w3
- Session-07 worktree `/home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w2`: still `687b5afd933d2ffce418eb6e57f03efb3ed141bf`, tracked-clean; not used as working copy; not edited
- Git writes this session: `worktree add --detach` of w3 and worktree-local `submodule update --init .ap` only. No product commits, add, push, or canonical checkout of the candidate.

## Path set versus parent `1eee09c1…`

Exactly these 27 files (`git diff --name-only`); 1696 insertions / 37 deletions:

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

No extras. No `alembic_environment/versions/0034*`. No persist-join paths. No sixth `companion_mutation` file. ADR bodies 0020 / 0023 / 0044 / 0062 / 0065 / 0066 / 0067 / 0072 / 0073 / 0075 / 0076 / 0077 / 0078: empty diffs.

## Control matrix

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Runtime settings store persists atomic JSON sidecar (`runtime-settings.json`, mode `0o600`); valid bool in sidecar precedes `FrameNestSettings.automatic_media_analysis_enabled` | hold | `runtime_settings.py:58-87` overlay-first then fallback; `_atomic_write_json` tmp + `os.replace` and `os.chmod(..., 0o600)` `:121-152`. Default path `{database_path.parent}/runtime-settings.json` (`configuration.py:488-496`). Tests: `test_atomic_write_persists_bool_and_mode`, `test_json_overlay_precedes_fallback`, `test_setting_survives_new_app_on_same_sidecar` (`test_automatic_analysis_settings_api.py:173-192`). |
| 2 | Scheduler reads `store.is_enabled` dynamically via callable; changes take effect immediately without backend restart | hold | `ScheduleAutomaticMediaAnalysis.enabled` is `bool \| Callable[[], bool]` evaluated on access (`media_analysis_lifecycle.py:205-223`); `execute` uses `self.enabled` `:221-223`. `create_app` passes `enabled=runtime_settings_store.is_enabled` and `automatic_analysis_enabled=runtime_settings_store.is_enabled` (`application.py:667-669`, `:725-729`). Capability GET resolves per request (`media_analysis_lifecycle_api.py:186-190`, `:510-515`). Tests: `test_scheduler_callable_is_evaluated_per_execute`, `test_notify_cataloged_follows_callable_flag`. |
| 3 | `PUT /api/admin/settings/automatic-analysis` requires `provider.operate`; ordinary → 403 `CAPABILITY_DENIED` | hold | Route policy `capability=CAPABILITY_PROVIDER_OPERATE`, `companion_mutation=True`, `audit_action="settings.automatic_analysis.put"` (`tailscale_ingress.py:409-416`). `test_ordinary_put_is_capability_denied` (`test_automatic_analysis_settings_api.py:123-131`). `test_x_route_policy.py:79-80`. |
| 4 | Enable without `confirm_cloud_upload: true` returns 422; disable succeeds without extra confirm | hold | API `runtime_settings_api.py:63-71` 422 `CLOUD_CONFIRMATION_REQUIRED`; disable has no confirm branch. Tests: `test_admin_put_enable_requires_confirm_and_persists` (`test_automatic_analysis_settings_api.py:80-120`). Worker also rejects enable without confirm (`service_worker.js:637-639`). |
| 5 | Exactly five `companion_mutation=True` routes (opened, apply, requests POST, retry POST, settings PUT) | hold | Five `companion_mutation=True` assignments: PUT settings `:415`, opened `:553`, apply `:563`, POST `/api/x/requests` `:571`, retry `:580`. Set equality in `test_x_route_policy.py:114-121`. |
| 6 | Companion extension Settings: Administration visible only to connected identities with `provider.operate`; hidden for ordinary/disconnected | hold | HTML `admin-settings` `hidden` by default (`sidebar.html:63-64`). `refreshAdministration` hides without origin or without `hasProviderOperateCapability` (`sidebar.js:662-675`; helper `messages.js:522-525`). Tests: `settings HTML keeps Administration below origin controls and hidden by default`; `Administration is hidden when disconnected or ordinary` (`companion_settings_automatic_analysis.test.js:330-428`). Sidebar HTTP uses `request()` only (no `fetch(` in `sidebar.js`). |
| 7 | Confirm dialog shown before enabling automatic analysis in companion Settings | hold | Checkbox ON shows in-sheet confirm, not `window.confirm` (`sidebar.js:719-728`, `sidebar.html:70-77`). Dismiss restores off without PUT (`sidebar.js:738-741`). Confirm copy matches plan. Tests: `admin confirm dismiss does not PUT; confirm enable and disable do` (`companion_settings_automatic_analysis.test.js:435-490`); `doesNotMatch(..., /window\.confirm/)` `:342`. |
| 8 | Git default in `configuration.py` remains `automatic_media_analysis_enabled: bool = Field(default=False)` | hold | `configuration.py:233`. `test_git_tracked_default_remains_false` (`test_automatic_analysis_privacy_contract.py:73-77`). Env example keeps commented `false` (`framenest.env.example:42`). |
| 9 | Schema head remains Alembic `0033`; no `0034_*` migration | hold | Versions dir ends at `0033_media_analysis_proposals.py`. No `0034_*` under `src/framenest/infrastructure/persistence/alembic_environment/versions/`. Path set has no migration. Pre-existing ADR file `docs/adr/0034-canonical-analytic-programming-integration.md` is not an Alembic revision and is not in this diff. |
| 10 | ADR-0079 created and indexed; ADR bodies 0020/0023/0044/0062/0065/0066/0067/0072/0073/0075/0076/0077/0078 untouched | hold | New `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md` (Accepted 2026-08-27). Index row `docs/adr/README.md:106`. Named ADR body diffs vs parent: empty. |

**Negative claims (must not hold):** ordinary Administration / settings PUT — does not hold (403 `CAPABILITY_DENIED`; UI hidden). Sixth `companion_mutation` — does not hold (set size 5). Alembic `0034` migration — does not hold. Tracked git file mutation for the runtime setting value — does not hold (sidecar beside catalog; not a tracked settings file).

Claim `07_report_00.md` matches this independent inspection for product behavior. It did not disclose that `WORKTREE_MARKER` is bound to the implementing checkout name. That report remains a claim; this session’s evidence is the candidate object plus the suites below.

## Validation

Isolated-worktree declared route (expected miss; classified; not repaired):

```text
./.ap/ap project check --root <w3> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
./.ap/ap exec --root <w3> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation runtime-info
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

Python matrix (canonical `--root`, w3 `--rootdir` / `pythonpath`), plus temporary `/tmp/framenest-r4acc-08-provenance.py`:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b \
  --operation test-focus -- \
  <w3>/tests/unit/test_runtime_settings_store.py \
  <w3>/tests/contract/test_automatic_analysis_settings_api.py \
  <w3>/tests/contract/test_x_route_policy.py \
  <w3>/tests/contract/test_tailscale_ingress_security.py \
  <w3>/tests/contract/test_automatic_analysis_privacy_contract.py \
  /tmp/framenest-r4acc-08-provenance.py \
  -q -p no:cacheprovider -s --rootdir=<w3> -o pythonpath=<w3>/src
# 1 failed, 112 passed in 47.79s
# probe print: framenest.__file__=/home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w3/src/framenest/__init__.py
# FAILED test_runtime_settings_store.py::test_candidate_source_provenance
#   expected part 'framenest-companion-r4-automatic-analysis-settings-mvp-w2'
#   observed part 'framenest-companion-r4-automatic-analysis-settings-mvp-w3'
```

Stopping condition for wrong-tree import was not met: candidate `src/` provenance held via the probe. Probe created, run, deleted. `.venv` was not reconstructed. Ambient `python` / `.venv/bin/python` / `poetry run` were not used.

Without the extra probe file, the five named suites are **1 failed, 111 passed**. The failure is the w2 directory-name assertion, not an import of canonical `src/`.

Node from the fresh checkout root:

```text
node --test tests/companion_review_extension.test.js tests/companion_settings_automatic_analysis.test.js
# 32 pass, 0 fail
```

## Deviations

- Isolated-worktree `ap exec --root <w3>` misses declared CPython (known launch-path). Used the prompt’s canonical `--root` plus `--rootdir` / `pythonpath` deviation. `.venv` was not reconstructed. Ambient `python` / `.venv/bin/python` / `poetry run` were not used.
- Envelope `runtime-info` on canonical `--root` prints canonical `framenest.__file__`. Candidate provenance is the `/tmp` pytest probe under the same `pythonpath`, not that envelope line.
- Declared Python suite is not green because `WORKTREE_MARKER` is the implementing worktree basename. Independent probe under w3 passed. This is the PARTIAL cause.

## Risks

Unpublished candidate on an unpushed branch. Residual: NUC and Brave companion will not show Administration until publication + routine release update. The harness leftover does not change runtime behavior; it does block `acceptance-PASS` until the committed test can pass on a checkout that is not named `…-w2`.

## Out-of-scope observations (ledger-candidates only)

`deploy/systemd/framenest.env.example:59` still says companion mutations are “Flagged only for POST /api/x/requests and POST /api/x/requests/{id}/retry.” That sentence was already stale at parent `1eee09c1…` (four flagged routes) and was not part of this commit’s edited overlay paragraph (`:39-42`). Matches session-07’s ledger-candidate note. No ledger write in this session.

Isolated-worktree `ap exec --root <worktree>` still fails `declared CPython executable does not exist`. Matches the existing untriaged non-authorizing ledger entry for consumer-declared execution-route binding.

## Smallest next step

One smallest coherent correction: in `tests/unit/test_runtime_settings_store.py`, replace the `…-w2` directory-name marker with a checkout-independent assertion that `framenest.__file__` resolves under the executed `src/framenest` tree (the same check the `/tmp` probe already passed). Then scoped re-acceptance of the Python matrix only, unless the Orchestrator judges the test-identity change to require full-fresh acceptance. No publication, NUC, or closure until acceptance-PASS.

## Report justification

`final-acceptance`

## Authority expiry

This acceptance authority expires at this terminal report. No product edits, publication, push, NUC, or closure were granted or performed.

## Resolved Execution Issues / Near-Misses

none beyond the classified isolated-worktree CPython miss, which was the expected RF-16 deviation and was not repaired.

## Pre-Existing Failure Classification

none observed in product behavior. The failing provenance assertion is a candidate-committed harness leftover from the implementing worktree name, not a pre-existing baseline failure.

## Capability handshake

- Plan Mode: requested `not-used`; observed off (acceptance prompt, no plan-mode transition).
- Reasoning: requested High; observed qualitative depth used for independent diff, control-matrix inspection, and RF-16 re-run; no independent attestation of a reasoning-level setting.
- Max / enhanced mode: requested off; observed off or unknown (no Max UI control in this session).
- Automatic model selection: off per prompt; not independently attested.
- Context pressure: moderate (27-file candidate, fresh checkout); no containment failure.
- Sub-agents / Explore-style delegation: not used.

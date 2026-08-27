### Report for ORCHESTRATOR_CHAT

Logical whole: `framenest-companion-r4-automatic-analysis-settings-mvp`  
Worker session: `07`  
Worker exchange: `01`

Status: **PASS**

Phase-qualified result: `implementation-PASS`  
Logical-whole closure: `not-closed`

## Worktree and Git

- Worktree: `/home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w2`
- Branch: `feat/companion-r4-automatic-analysis-settings-mvp`
- Exact baseline: `1eee09c1afcfe41b2a411784f8c43c428e610b9b`
- Commit 1 (server store + PUT + Python tests): `22847b7d12a97c7d84b520d9f8cb46cdef12952b`
- Commit 2 (companion UI + JS tests): `f04bc232dd832b796f9c0ec183500d6da54af40e`
- Commit 3 (docs + ADR-0079): `687b5afd933d2ffce418eb6e57f03efb3ed141bf`
- Worktree HEAD after commits: `687b5afd933d2ffce418eb6e57f03efb3ed141bf` (tracked-clean)
- Canonical checkout `/home/agile/Projects/framenest`: still `1eee09c1afcfe41b2a411784f8c43c428e610b9b` on `feat/x-meme-browser-companion`, tree `bd160c2a7f9a34c689a08b0e5facff3e426f127f`, tracked-clean
- Pinned submodule: `.ap` gitlink == `.ap` HEAD == `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Schema head: Alembic `0033_media_analysis_proposals.py`; no `0034_*`
- No push

## Changed files

1. `src/framenest/infrastructure/runtime_settings.py` — **NEW**; atomic JSON sidecar (`tmp` + `os.replace`, mode `0o600`), fail-closed overlay, symlink rejection.
2. `src/framenest/adapters/api/runtime_settings_api.py` — **NEW**; `PUT /api/admin/settings/automatic-analysis`; enable requires `confirm_cloud_upload: true` else 422 `CLOUD_CONFIRMATION_REQUIRED`.
3. `src/framenest/configuration.py` — `RUNTIME_SETTINGS_FILENAME`, optional `runtime_settings_path` / `FRAMENEST_RUNTIME_SETTINGS_PATH`, `resolved_runtime_settings_path()`; git default `automatic_media_analysis_enabled` remains `False`.
4. `src/framenest/application/media_analysis_lifecycle.py` — `ScheduleAutomaticMediaAnalysis.enabled` is `bool | Callable[[], bool]`, evaluated on `execute`.
5. `src/framenest/adapters/api/application.py` — one `RuntimeSettingsStore`; scheduler and capability GET receive `store.is_enabled`; PUT router included.
6. `src/framenest/adapters/api/media_analysis_lifecycle_api.py` — `automatic_analysis_enabled: bool | Callable[[], bool]`; GET capability reads per request.
7. `src/framenest/adapters/api/tailscale_ingress.py` — fifth `companion_mutation`: PUT settings, capability `provider.operate`, audit `settings.automatic_analysis.put`.
8. `extension/ui/sidebar.html` — Administration section below origin controls; in-sheet confirm copy; hidden by default.
9. `extension/ui/sidebar.js` — admin-only via `provider.operate`; confirm enable / immediate disable; errors revert the checkbox; HTTP only via `request()`.
10. `extension/ui/sidebar.css` — Administration and in-sheet confirm styling.
11. `extension/shared/messages.js` — `automatic_analysis_capability` / `automatic_analysis_settings`, `pathFor`, `hasProviderOperateCapability`.
12. `extension/background/service_worker.js` — GET/PUT handlers; enable without confirm rejected in the worker; `capabilitiesFromBody.providerOperate`.
13. `tests/unit/test_runtime_settings_store.py` — **NEW**; overlay, mode, callable scheduler, `notify_cataloged`, env override, worktree `__file__` provenance.
14. `tests/contract/test_automatic_analysis_settings_api.py` — **NEW**; confirm 422, persist, ordinary 403, mutation header, companion origin, empty allowlist, restart-without-restart via sidecar.
15. `tests/contract/test_x_route_policy.py` — exactly five flagged `companion_mutation` routes.
16. `tests/contract/test_tailscale_ingress_security.py` — PUT accepted on flagged companion origin; empty allowlist 403; 200 success asserted without requiring an error body.
17. `tests/contract/test_automatic_analysis_privacy_contract.py` — git default remains `Field(default=False)`.
18. `tests/companion_settings_automatic_analysis.test.js` — **NEW**; HTML contract, worker PUT, admin-only UI, confirm dismiss, error revert.
19. `docs/adr/0079-administrator-automatic-analysis-runtime-setting.md` — **NEW**; accepted 2026-08-27.
20. `docs/adr/README.md` — index row for 0079.
21. `PRODUCT.md` — companion Settings admin overlay; desktop Settings stays unshipped.
22. `SPEC.md` — runtime overlay and fifth mutation.
23. `SECURITY.md` — sidecar, capability, confirm-on-enable.
24. `README.md` — living status for the overlay.
25. `docs/X_COMPANION.md` — five `companion_mutation` routes; Administration in Settings.
26. `docs/BACKUP_AND_RECOVERY.md` — sidecar excluded from catalog backup.
27. `deploy/systemd/framenest.env.example` — git default stays commented `false`; overlay path noted.

Allowlisted and unchanged: `tests/companion_review_extension.test.js` (no source-wiring change required; still executed). ADR bodies 0020, 0023, 0044, 0062, 0065, 0066, 0067, 0072, 0073, 0075, 0076, 0077, 0078 were not edited.

## Validation

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b
# ap project check --baseline: PASS
```

RF-16 known miss (classified, not repaired):

```text
./.ap/ap exec --root <WORKTREE> --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b --operation runtime-info
# Expected: declared CPython executable does not exist (relative .venv/bin/python).
# Not invoked after the known miss; .venv was not reconstructed.
```

Authorized session-only deviation (canonical `--root`, worktree `--rootdir` / `pythonpath`):

```text
./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b \
  --operation runtime-info
# interpreter: /home/agile/Projects/framenest/.venv/bin/python
# framenest.__file__=/home/agile/Projects/framenest/src/framenest/__init__.py
# (envelope only; not candidate provenance)

./.ap/ap exec --root /home/agile/Projects/framenest \
  --baseline 1eee09c1afcfe41b2a411784f8c43c428e610b9b \
  --operation test-focus -- \
  <WORKTREE>/tests/unit/test_runtime_settings_store.py \
  <WORKTREE>/tests/contract/test_automatic_analysis_settings_api.py \
  <WORKTREE>/tests/contract/test_x_route_policy.py \
  <WORKTREE>/tests/contract/test_tailscale_ingress_security.py \
  <WORKTREE>/tests/contract/test_automatic_analysis_privacy_contract.py \
  -q -p no:cacheprovider \
  --rootdir=<WORKTREE> \
  -o pythonpath=<WORKTREE>/src
# 112 passed in 50.01s
# test_candidate_source_provenance passed: WORKTREE_MARKER
#   framenest-companion-r4-automatic-analysis-settings-mvp-w2
#   is in Path(framenest.__file__).resolve().parts
# Candidate provenance:
#   /home/agile/Projects/framenest-worktrees/framenest-companion-r4-automatic-analysis-settings-mvp-w2/src/framenest/__init__.py
```

Stopping condition not met. Ambient `python` / `.venv/bin/python` / `poetry run` were not used. `.venv` was not reconstructed.

JS from the worktree root:

```text
node --test tests/companion_review_extension.test.js tests/companion_settings_automatic_analysis.test.js
# 32 pass, 0 fail
```

## Verification

- Runtime settings store: atomic JSON beside the catalog; override `FRAMENEST_RUNTIME_SETTINGS_PATH`; valid bool in sidecar precedes `FrameNestSettings`; missing/malformed JSON fails closed to fallback; mode `0o600`.
- Scheduler reacts dynamically: `enabled=store.is_enabled` callable; unit tests flip the flag between `execute` / `notify_cataloged` without reconstructing the scheduler.
- Exactly five `companion_mutation` routes (`test_x_route_policy.py` set equality).
- Capability `provider.operate` on PUT and GET capability; ordinary PUT → 403 `CAPABILITY_DENIED`.
- Enable without `confirm_cloud_upload: true` → 422; disable without confirm → 200.
- Companion origin accepted only when flagged and allowlisted; empty allowlist → 403 `MUTATION_ORIGIN_FORBIDDEN`.
- Extension Settings: Administration hidden by default; visible only with `provider.operate`; in-sheet confirm, not `window.confirm`; sidebar uses `request()` only (no `fetch`).
- ADR-0079 added; living docs updated; desktop Settings stays unshipped.
- No schema `0034`; git default remains `automatic_media_analysis_enabled: bool = Field(default=False)`.
- Sidecar excluded from catalog backup.

## Deviations

- Isolated-worktree `ap exec --root <WORKTREE>` misses declared CPython (known launch-path). Used the prompt’s canonical `--root` plus `--rootdir` / `pythonpath` deviation. `.venv` was not reconstructed. Ambient `python` / `.venv/bin/python` / `poetry run` were not used.
- Envelope `runtime-info` on canonical `--root` prints canonical `framenest.__file__`. Candidate provenance is `test_candidate_source_provenance` under the same `pythonpath`, not that envelope line.
- First `test-focus` with relative test paths failed `file or directory not found` against the canonical `--root`. Retried with absolute worktree paths (same pattern as era 05/06 reports). Not an environment limitation.
- JS `assert.deepEqual` on VM-realm payload objects failed with identical structures; assertions compare primitive fields.
- Companion PUT 200 has no `error` key; `test_tailscale_ingress_security` now asserts status 200 / body instead of `_error_code` on success.

## Risks

none beyond unpublished candidate on an unpushed branch. Residual: NUC and Brave companion will not show Administration until publication + routine release update.

## Out-of-scope observations (ledger-candidates only)

`deploy/systemd/framenest.env.example` still says companion mutations are “Flagged only for POST /api/x/requests and POST /api/x/requests/{id}/retry.” That sentence was already stale at the baseline (four flagged routes) and remains outside this commit’s edited paragraph.

## Next step

Fresh independent acceptance Worker 08 on these unpushed commits, then separately authorized publication + NUC routine `framenest-release` and Cooperator rendered Settings acceptance.

## Report justification

`new-mutation`

## Authority expiry

This implementation authority expires at this terminal report. No push, NUC, publication, or closure is granted.

## Resolved Execution Issues / Near-Misses

Relative `test-focus` paths collected against canonical `--root` (`ERROR: file or directory not found: tests/unit/test_runtime_settings_store.py`); cause: pytest cwd/root is the canonical envelope; resolution: absolute worktree test paths plus `--rootdir` / `pythonpath`. JS VM-realm `deepEqual` near-miss; resolution: field equals. Companion PUT 200 `_error_code` KeyError; resolution: assert 200 body. Ambient AppImage/loader classes (`APPIMAGE`, `APPDIR`, `LD_LIBRARY_PATH`, inherited `PATH`, `SSH_AUTH_SOCK`) present in the parent; resolution: `./.ap/ap` sanitized-v1 re-exec. Residual risk: none for this implementation (no ambient Python used for evidence).

## Pre-Existing Failure Classification

none

## Capability handshake

- Plan Mode: requested `not-used`; observed off (implementation prompt, no plan-mode transition).
- Reasoning: requested High; observed qualitative depth used for store/API/extension + RF-16 deviation; no independent attestation of a reasoning-level setting.
- Max / enhanced mode: requested off; observed off or unknown (no Max UI control in this session).
- Automatic model selection: off per prompt; not independently attested.
- Sub-agents / Explore-style delegation: not-used.
- Context pressure: moderate (conversation summarization mid-implementation); no containment failure.

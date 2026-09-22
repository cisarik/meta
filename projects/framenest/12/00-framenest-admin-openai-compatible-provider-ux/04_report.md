### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 04
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Re-Audit
Phase: Independent Audit
Task identity: REACCEPT-ADMIN-PROVIDER-REGISTRY-AND-VISION-PROBE-AFTER-CORRECTION
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: 7ff6546f345827d6df20bd5b13d5e57cb4bc90db
End commit: 7ff6546f345827d6df20bd5b13d5e57cb4bc90db
Report justification: final-acceptance
Logical-whole closure: not-closed

Evidence posture: full-fresh independent re-acceptance of the corrected
candidate `7ff6546` after the automatic correction of the refuted N7 finding.
Read-only; no correction authority used; the implementation reports
(`02_report*.md`) and the prior acceptance (`03_report.md`) were read as claims
only and every risk claim and control was re-verified against repository truth
on this candidate. The candidate is local-only; no public-ref claim is under
decision. No secret, provider, network, NUC, SSH, sudo, browser, or GUI action
occurred, and no ambient Python, `poetry run`, `pip`, or `uv` was invoked.

## Repository gate (read-only, independently observed)

- Physical root `/home/agile/Projects/framenest`; canonical remote
  `origin https://github.com/cisarik/framenest.git`; branch
  `feat/x-meme-browser-companion`; HEAD
  `7ff6546f345827d6df20bd5b13d5e57cb4bc90db` (matches the candidate);
  porcelain clean before and after evidence runs; no stash; no in-progress
  merge/rebase/cherry-pick operation.
- `.ap` gitlink == `.ap` HEAD == `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`;
  `.ap` submodule clean; `./.ap/ap doctor` -> `ap doctor: PASS` (strict pinned
  AP commit, managed AGENTS.md block OK, stable variant).
- Candidate chain `33946e0 -> f41df79 -> 980db7a -> e6d91d1 -> c66f5b6 ->
  810b606 -> 87411e0 -> 7ff6546` (7 commits, local only);
  `origin/main == origin/feat/x-meme-browser-companion == 33946e0`;
  `git rev-list --count origin/main..HEAD` = 7 (no push).
- `git diff --name-only 33946e0..7ff6546` = exactly 53 paths, identical to
  the acceptance allowlist (defined as that diff); the diff contains no `.ap`
  path; `git diff --numstat` totals 53 files, +8850/-512.
- RF-12 classification of the only divergence (7 local commits ahead of the
  published baseline): primary `unpublished-candidate`; secondary facts
  `accepted-continuation` (inside the accepted whole) and no unexplained
  remainder. Nothing repaired.
- Meta destination
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/04_report.md`
  verified absent, parent real non-symlink directory, before writing.

## 1. Compact core

- Changed files: none in the FrameNest repository (read-only re-acceptance);
  only this Meta report was created.
- Validation: the exact declared AP route selection (926 passed), the exact
  `node --test` line (35 pass), focused named negative-control and N7/N8 node
  selections (140 passed; 8 by name; 26 by name), fixture byte/hash checks,
  wheel-resource test, and direct read-only inspection. No Git write anywhere.
- Commit result: no fetch, stage, commit, or push in either repository.
- Risks/missing evidence: none refuting; disclosed residuals below, each with
  an acceptance disposition. No missing evidence claim for the allowlisted
  surface.
- Smallest next step: Orchestrator publication decision for `7ff6546` and the
  closing whole-level disposition; then the routine NUC release refresh and
  the Cooperator's numbered acceptance run when the Orchestrator grants them.
- Report justification: final-acceptance. Logical-whole closure: not-closed.

## 2. Correction resolution statement (original finding vs this candidate)

The prior independent acceptance (`03_report.md`) refuted control N7 for the
Analyze side on `87411e0`: SPEC.md:726-727, ADR-0081 decision 4, and
AI_WORKSPACE.md:216-220 asserted a `vision_input` refusal that the Analyze
code did not enforce. The correction commit `7ff6546` (7 paths, +376/-1)
resolves that finding on this candidate:

- `media_suggestion_api.py` hunks at `+259-264` and `+366-371` insert the
  `_model_lacks_vision(dependencies)` preflight into both preview routes after
  the `_provider_configured` check and before any preview execution; the new
  helper `+447-461` refuses only when a dynamic resolution proves the selected
  model lacks `vision_input`, returning `409 AI_MODEL_CAPABILITY_MISSING`
  ("The selected AI model does not support image analysis.") with zero preview
  calls.
- `media_analysis_lifecycle_api.py` hunk `+389-394` inserts the same preflight
  into the durable-analysis POST after the configured check and before
  `request_manual_analysis` is consulted (no run created); helper `+539-551`.
- `application.py` hunks `+691-697` and `+706` wire the automatic executor's
  `read_model_capabilities` from the shared dynamic resolver (raising the
  existing sanitized `MediaSuggestionProviderUnavailableError` when the
  provider is `None`).
- `media_analysis_lifecycle.py` hunks `+513-518` (executor refuses a
  non-vision model before any media access or `suggest`) and `+591-596`
  (`PROVIDER_MODEL_CAPABILITY_MISSING`, message "AI provider model does not
  support image analysis.", `retryable=False`); the new code is absent from
  `_PROVIDER_SUBMISSION_ERROR_CODES` (`:623-632`).

New issues introduced by the correction: none found. The correction diff
touches no pong, CLI, registry, records, judge, or documentation path; the
only deletion in the whole correction is the one-line `Sequence` import
preparation in `media_analysis_lifecycle.py` (test diff: 0 deleted lines).
The fail-open legacy path, the double resolution, and the early executor check
placement are design choices the correction report discloses, verified true,
and assessed as acceptable residuals below.

## 3. Per-claim verdict table (R1-R8)

| Claim | Verdict | Exact evidence |
|---|---|---|
| R1 no secret value in v2 config, API responses, browser surfaces, or logs | verified | P1 green including `test_v2_declared_config_round_trips_with_exact_keys` (raw text: only `credential_env` name), `test_write_and_load_config_persists_no_secret`, `test_credential_value_never_appears_in_request_body`, `test_repr_is_redacted`; inspection: `serialize_declared_provider_record` emits `credential_env` name only (`provider_records.py:290-296`), `GenericAiProviderCredential.__repr__` redacted (`credentials.py:68-69`); node assertions that the JSON preview and failure copy match no key/secret shape and no `Bearer`/absolute path (`ai_providers_admin_frontend.test.js:387,514,561`) |
| R2 admin routes cannot bypass authN/authZ | verified | Six `RoutePolicy` rows `capability=provider.operate`, `channel=tailscale`, `companion_mutation` default False, audit actions `ai.provider.put|delete|activate|ping|pong` (`tailscale_ingress.py:417-458`, default at `:146`); middleware order origin -> mutation header -> identity (401/403) -> capability (403 `CAPABILITY_DENIED`, denied row audited) -> audited allowed attempt -> dispatch (`:783-903`); `test_route_policies_match_the_application_route_inventory`, `test_ai_admin_route_policies_are_provider_operate_gated_and_non_companion`, `test_ai_admin_routes_deny_ordinary_tailscale_identities`, `test_authorization_matrix_and_audited_denial` all PASSED by name; public composition returns `create_public_published_app` before any admin router (`application.py:397-402`) |
| R3 ping/pong/analyze privacy | verified | Pong route requires `confirm_cloud_upload` then resolves, refuses non-vision, takes `.vision-probe.lock`, sends only `load_vision_probe_fixture()`, persists only bounded safe fields (`ai_admin_api.py:580-635`); no catalog repository or suggestion persistence in the route; `test_pong_requires_confirmation_and_declared_vision_capability` PASSED; ping body text-only (`test_connection_test_is_text_only_single_call_and_carries_user_agent`); judge/sidecar tables green (`test_vision_probe.py` in P1); automatic-analysis privacy contract 4 tests PASSED by name |
| R4 v1 config read compatibility; malformed fails closed | verified | `load_ai_server_config` accepts only schema 1/2; v1 yields `providers={}` with `active_provider_id`/`provider_models` preserved; writers always write v2 (`configuration.py:157-225`); `test_v1_read_upgrades_to_v2_without_inventing_providers`, `test_v1_read_keeps_builtin_default_selection`, `test_unsupported_or_missing_config_version_is_rejected`, `test_malformed_declared_records_fail_closed`, `test_oversized_config_is_rejected`, `test_malformed_config_is_sanitized` all green in P1/focused run |
| R5 dynamic resolution without restart; no authorization widening; no silent movie-identification change | verified | `test_dynamic_effect_without_restart` PASSED by name (PUT + activate, then both capability GETs report the declared identity; `LazyResolvedAiProvider` performs the call against the rewritten config); `test_dynamic_resolver_rereads_rewritten_config`, `test_lazy_provider_resolves_the_current_configuration_per_operation` green; real composition wires the resolver into preview services, both capability endpoints, the automatic executor, and admin deps (`application.py:672, 691-706, 760, 781`); movie identification remains `startup_analysis_provider` + `identify_movie` (`:718-750`), untouched by the correction diff; capability endpoints remain read-only; admin routes unchanged `provider.operate` |
| R6 NVIDIA/Vercel unregressed and Gallery/Details frozen | verified | P1 includes all `tests/unit/infrastructure/ai` (`test_nvidia_nim.py`, `test_vercel_gateway.py`, generic adapter, registry) green; `test_ai_server_composition.py` 11 tests PASSED by name; web diffs purely additive (`web/index.html` 73/0, `web/app.js` 985/0, `web/styles.css` 265/0); no Gallery/Details path outside the 53-path allowlist changed |
| R7 repository hygiene | verified | Diff exactly the 53-path allowlist; `.ap` gitlink unchanged and clean; `origin/main` and `origin/feat/x-meme-browser-companion` still `33946e0`; porcelain clean; no tag/stash added; branch ahead of origin by 7 commits; linear history with the declared subjects |
| R8 (correction) every Analyze entry point refuses a model without `vision_input` | verified | Correction diff hunks cited in §2; both preview routes return `409 AI_MODEL_CAPABILITY_MISSING` with zero preview calls (`test_non_vision_selected_model_is_refused_on_both_preview_routes` PASSED, asserts `cache-control: no-store`, exact body, `preview.calls == []`, `imported_preview.calls == []`); durable request returns 409 with zero scheduling calls (`test_manual_durable_analysis_refuses_non_vision_selected_model` PASSED, `calls == []`); automatic run persists `PROVIDER_MODEL_CAPABILITY_MISSING`, `retryable=False`, `provider_submission_occurred is False`, no requeue, zero provider calls (`test_non_vision_automatic_run_fails_non_retryably_without_submission` PASSED); vision-declared models still analyze on all three paths (`test_vision_declared_selected_model_still_analyzes`, `test_manual_durable_analysis_accepts_vision_selected_model` PASSED); pong, CLI `vision-probe`, and existing classifications unchanged (correction diff excludes `ai_admin_api.py` and `cli/ai.py`; CLI vision-probe and still-frame tests PASSED by name; `PROVIDER_UNAVAILABLE` reader path preserved) |

## 4. Controls table

| # | Control | Evidence | Result |
|---|---|---|---|
| P1 | Declared AP route, exact prompt selection | `./.ap/ap exec --root /home/agile/Projects/framenest --baseline 7ff6546f... --operation test-focus -- <19 paths> -q -p no:cacheprovider` -> `926 passed, 1 warning in 109.11s`, exit 0; sanitized-env WARN lists only declared inherited classes (`SSH_AUTH_SOCK`, `VIRTUAL_ENV_DISABLE_PROMPT`, `PATH`); baseline contract trusted as `7ff6546...:ap.project.conf` | PASS |
| P2 | Frontend suites | `node --test tests/ai_providers_admin_frontend.test.js tests/tailscale_identity_frontend.test.js tests/companion_settings_automatic_analysis.test.js` -> 35 pass / 0 fail / 0 skipped (10.1 s) | PASS |
| P3 | Route inventory 1:1 and six admin routes gated | `test_route_policies_match_the_application_route_inventory`, `test_ai_admin_route_policies_are_provider_operate_gated_and_non_companion`, `test_ai_admin_routes_deny_ordinary_tailscale_identities`, `test_x_route_policy.py`, `test_public_published_uds.py` together -> 29 passed; six rows inspected (R2) | PASS |
| P4 | Fixture 74 bytes / SHA-256 / wheel-present | Worktree and committed blob both 74 bytes and SHA-256 `396f6aba97b0b4ac60a22cae643ef2df1676ab98050fa468bbcb1aadb69b9e44`; `file`: PNG 8x8 8-bit RGB; `pyproject.toml` wheel include added; `test_ai_package_resources.py` green including the poetry-wheel build test (P1) | PASS |
| P5 | Dynamic no-restart resolution | `test_dynamic_effect_without_restart` PASSED by name; `test_dynamic_resolver_rereads_rewritten_config`, `test_lazy_provider_*` green; resolver wiring inspected (R5) | PASS |
| P6 | Documentation asserts only implemented behavior; no closed ADR edited | SPEC.md:726-727 now contains the `vision_input` Analyze/vision-probe MUST (implemented in §2); ADR-0081 decision 4 (`:86-90`) matches the corrected enforcement; AI_WORKSPACE.md:216-220 matches; `docs/adr/README.md` diff adds only the 0081 index row; all other ADR files outside the allowlist untouched | PASS |
| N1 | No secret value/key shape/Authorization/raw payload in config, API, CLI, JSON preview, logs | R1 evidence; P1 and focused runs green (140 passed, 26 by name) | PASS |
| N2 | Sanitized 403 with audited denials; public composition excludes admin routes | `test_authorization_matrix_and_audited_denial` PASSED by name (403 `CAPABILITY_DENIED`/`IDENTITY_NOT_AUTHORIZED`, audited denied row, `MUTATION_HEADER_REQUIRED`, `MUTATION_ORIGIN_FORBIDDEN`, zero transport calls); public composition early return inspected; GET denial unaudited by design (policy has no `audit_action`) | PASS |
| N3 | Origin/header proof; built-in and active refusals; pong confirm and non-vision refusal; busy locks | `test_builtin_active_and_validation_refusals`, `test_pong_requires_confirmation_and_declared_vision_capability`, `test_busy_activity_locks_return_conflict_without_provider_calls` PASSED by name; `test_audit_rows_exist_before_provider_execution` PASSED | PASS |
| N4 | Zero provider calls on providers GET and on UI open/typing; UI hiding not the mechanism | `test_admin_crud_ping_and_pong_happy_paths` PASSED by name (asserts no transport calls on GET); node tests "dialog open performs exactly one list GET and typing stays local" and "every unsafe fetch call site uses framenestMutationHeaders..." passed (P2); server middleware is the enforcement path (R2) | PASS |
| N5 | Malformed/unsupported config fails closed; v1 reads without loss, never written back as v1 | R4 evidence; writer constant is v2 only | PASS |
| N6 | NVIDIA/Vercel unregressed; Gallery/Details frozen | R6 evidence | PASS |
| N7 (corrected) | Non-`vision_input` model refused on both preview routes, durable request, and automatic analysis | 3 new contract tests + 1 executor test PASSED by name with zero preview/scheduling/provider calls; automatic classification `PROVIDER_MODEL_CAPABILITY_MISSING` non-retryable; pong side unchanged (`test_pong_requires_confirmation_and_declared_vision_capability` PASSED) | PASS |
| N8 (new) | Capability refusal never counts as a provider submission; unavailable reader still `PROVIDER_UNAVAILABLE`; existing classifications and pong/CLI unchanged | `_PROVIDER_SUBMISSION_ERROR_CODES` excludes the new code (`media_analysis_lifecycle.py:623-632`) and the classification returns `retryable=False`; `test_unavailable_capability_reader_still_classifies_as_provider_unavailable` PASSED (PROVIDER_UNAVAILABLE, zero provider calls); 10 CLI vision-probe/still-frame tests PASSED by name; correction diff excludes pong/CLI; all prior failure-classification tests green | PASS |

## 5. Claim-versus-evidence findings against prior reports

none material. Specific re-checks:

- `03_report.md` correctly refuted N7 on its candidate `87411e0`; the
  repository at that commit confirmed the absence of any Analyze capability
  preflight. On `7ff6546` the finding is resolved (§2).
- `02_report_07.md` quantitative and behavioral claims were re-verified where
  re-executable: 7 correction paths and +376/-1 numstat exact; fail-open
  helper behavior, double resolution, early executor placement, and unchanged
  pong/CLI/docs all confirmed by direct inspection. Its narrower `482 passed`
  selection was not re-executed verbatim; the broader prompt selection is
  green (926 passed), consistent with that claim.
- No prior report overstated an accepted risk claim in a way I could confirm
  as false on this candidate.

## 6. Out-of-scope observations (ledger candidates, non-authorizing)

- `provider_records.py:357-377`: abbreviated/hex IPv4 hostnames (`127.1`,
  `0x7f000001`) satisfy `_is_dns_name` and are not classified as loopback, so
  the declared-base-URL loopback prohibition is textual, not resolution-based
  (administrator-only surface; defense in depth).
- `tailscale_ingress.py`: GET `/api/admin/ai/providers` denials are not
  audited because its policy intentionally carries no `audit_action`;
  audited-denial coverage holds for the five mutating routes.
- `SECURITY.md:72`: the older sentence still frames server AI administration
  as CLI-only while the adjacent added paragraph documents the administrator
  surface (prose staleness only).
- `ai_admin_api.py:381-403`: the PUT active-model invariant is check-then-act
  across two config reads without a mutation lock (concurrent
  same-administrator race; fail-closed for presence only).
- New: for built-in providers, a selected model id that is not the declared
  default (e.g., via `FRAMENEST_AI_MODEL_ID` or CLI selection, which
  `_selection_model` admits for built-ins at `cli/ai.py:737-743`) is now
  refused for Analyze and Pong because built-in records declare capabilities
  only for their default model. This follows the accepted declaration
  contract (§6) and the normative SPEC sentence; operators needing another
  NVIDIA model would declare an equivalent provider record. Non-authorizing.

## 7. Residual-risk statement (with acceptance disposition)

1. Automatic-analysis unconfigured-provider classification: an unconfigured
   scheduler run now surfaces `PROVIDER_UNAVAILABLE` (retryable) through the
   new capability reader instead of the unreachable `provider is None` branch,
   with `provider_submission_occurred=True` and zero transport contact
   (pre-existing taxonomy; `test_unavailable_capability_reader_still_...`
   PASSED). Disposition: acceptable for this whole's scope; bounded retry
   semantics only, no privacy/security widening.
2. Indirect routed-analyze proof limitation (prior): app-level dynamism is
   proven through the capability endpoints and lazy-provider delegation with a
   fake transport, not a catalog-driven routed analyze. Disposition:
   acceptable; composition is directly inspected.
3. API preflight fail-open when `read_provider` is absent or raises: the real
   composition wires the resolver (`application.py:672, 760`), and the
   `_provider_configured` check precedes the capability check, so a capability
   refusal is issued only on a proven miss. Disposition: acceptable; legacy
   injected test dependencies keep prior behavior.
4. Double resolution per preview/durable request: a TOCTOU window can only
   choose between sanitized refusals; no provider call is possible on refusal.
   Disposition: acceptable.
5. Non-default model ids on built-in providers refused (new ledger candidate
   above). Disposition: acceptable as the declared-capability contract; no
   acceptance blocker; surface to the Cooperator before the NUC numbered
   acceptance only if a non-default model id is configured there.
6. Prior audit residuals (hex/abbreviated loopback hostnames, unaudited GET
   denials, PUT race, SECURITY prose staleness) remain open as ledger
   candidates; none blocks this whole.

## 8. Capability/model observation and independence

- Requested: fresh independent re-audit, High reasoning, approximately 250k
  tokens, single-active, no sub-agents. Observed from inside this session: the
  session declares model `opencode-go/deepseek-v4.1-flash`; requested versus
  effective reasoning and context capacity are not observably exposed and no
  telemetry claim is made. All evidence was produced through the declared
  sanitized AP route and read-only inspection; the only write was this report.
- Independence: this is a genuinely fresh session; the authoritative prompt
  was the initial context; no parent-conversation transcript, reasoning, or
  retained implementation context was inherited; this session did not
  implement or correct the candidate and had no material participation in it.
  Prior reports were treated as claims only, and all verdicts rest on direct
  evidence collected here.

## 9. Persistence and authority expiry

- This report is saved to the exact granted destination
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/04_report.md`
  (verified absent, parent real non-symlink directory), then read back in full
  and byte-verified. No other Meta file created; Meta Git archival remains
  with the COOPERATOR; no FrameNest Git write occurred.

Resolved Execution Issues / Near-Misses: none this exchange. The prompt used
the working `./.ap/ap exec` spelling, and the declared route, baseline, and
operation were used exactly as granted.

Pre-Existing Failure Classification: none. No test failure occurred; the
single collected warning (`PydanticJsonSchemaWarning` in
`tests/unit/test_configuration.py::test_database_path_absent_from_settings_repr_logs_api_and_openapi`)
is non-failing, topically unrelated to the corrected surface, and has the same
signature the prior independent acceptance already recorded at the previous
candidate; I did not re-run the `33946e0` baseline, so its pre-existence rests
on that prior observation rather than on a comparison executed here.

```text
Orchestration critique:
MEASURED: none new. The correction resolves the refuted N7 finding at all four Analyze boundaries with the sanitized refusal, zero provider work, non-retryable automatic classification, no provider-submission flag, and no change to pong, CLI vision-probe, or existing classifications; all controls hold on 7ff6546 with direct evidence.
LEAD: A built-in provider with a non-default selected model id (env override or CLI selection) is now refused for Analyze/Pong because built-in records declare capabilities only for their default model; cheapest check is a bounded local preview-route call with FRAMENEST_AI_MODEL_ID set to a non-default NVIDIA model after publication, or confirm the NUC uses the declared OpenCode Go record.
```

Authority expiry: this terminal report ends the grant; no autonomous
continuation.

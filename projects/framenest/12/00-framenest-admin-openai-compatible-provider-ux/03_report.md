### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: Independent Audit
Task identity: ACCEPT-ADMIN-PROVIDER-REGISTRY-AND-VISION-PROBE
status: BLOCKED
Phase-qualified result: not-applicable
Start commit: 87411e040157c51f3e1056e8a6e62c0c8c514018
End commit: 87411e040157c51f3e1056e8a6e62c0c8c514018
Report justification: final-acceptance
Logical-whole closure: not-closed

Evidence posture: independent acceptance; the candidate was not materially
implemented by this session and only this prompt was received as initial
context. Acceptance is bound to the exact local candidate, owner map,
allowlist, risk claims R1-R7, and the control matrix. One negative control is
refuted by direct inspection (Analyze capability refusal), so the candidate
cannot be accepted as-is; no correction was performed (no correction
authority).

## Repository gate (read-only, independently observed)

- Physical root `/home/agile/Projects/framenest`; canonical remote
  `origin https://github.com/cisarik/framenest.git`; branch
  `feat/x-meme-browser-companion`; HEAD
  `87411e040157c51f3e1056e8a6e62c0c8c514018`; porcelain clean; no stash;
  no in-progress operation.
- `.ap` gitlink == `.ap` HEAD == `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`;
  `.ap` worktree clean; `./.ap/ap doctor` -> `ap doctor: PASS` (stable
  variant, managed block OK, strict pinned AP commit).
- Candidate chain verified: `33946e0 -> f41df79 -> 980db7a -> e6d91d1 ->
  c66f5b6 -> 810b606 -> 87411e0` (6 commits, local only).
  `origin/feat/x-meme-browser-companion` == `origin/main` == `33946e0`
  (no push).
- `git diff --name-only 33946e0..87411e0` = exactly 49 paths, identical to
  the acceptance allowlist (allowlist is defined as this exact diff). No
  unlisted path changed; `.ap` gitlink unchanged.
- RF-12 classification of the only divergence (6 local commits ahead of the
  published baseline): primary `unpublished-candidate`; secondary facts:
  `accepted-continuation` (inside the accepted whole) and no unexplained
  remainder. Nothing repaired.
- Meta destination
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/03_report.md`
  verified absent, parent real non-symlink directory, before writing.

## 1. Compact core

- Changed files: none in the FrameNest repository (read-only acceptance);
  only this Meta report was created.
- Validation executed through the declared AP route and the granted Node
  lines (details in the controls table). No Git write anywhere; no network;
  no provider/NVIDIA/Vercel/OpenCode call; no NUC/SSH/sudo/browser/GUI; no
  credential value access; no ambient Python, `poetry run`, `pip`, or `uv`.
- Commit result: no fetch, stage, commit, or push in either repository.
- Risks: one refuted control (missing `vision_input` refusal on the Analyze
  path; SPEC §22 / ADR-0081 / AI_WORKSPACE.md assert it), plus two disclosed
  residuals assessed below; no security/privacy refutation found in R1-R7.
- Smallest next step: Orchestrator decides on one smallest coherent
  correction adding the `vision_input` preflight to the Analyze paths, then
  full fresh re-acceptance (runtime-behavior/security-boundary change).
- Near-misses: the prompt's route spelling `./.ap/ap ap exec` prints the
  `ap` usage text; the working declared spelling is `./.ap/ap exec`
  (already recorded in the implementation reports). I ran the same declared
  operation/baseline through the working spelling only.
- Pre-existing classification: the single pytest warning
  (`PydanticJsonSchemaWarning` in
  `tests/unit/test_configuration.py::test_database_path_absent_from_settings_repr_logs_api_and_openapi`)
  is pre-existing and unrelated; no failure was carried in from the
  baseline.
- Critique:

```text
Orchestration critique:
MEASURED: SPEC.md:726-727 ("Analyze and the vision probe MUST refuse a selected model that does not declare `vision_input`"), AI_WORKSPACE.md:218-220, and ADR-0081 decision 4 (lines 86-90) all state the Analyze refusal, but no Analyze path enforces it. `media_suggestion_api.py:251` and `:352` preflight only `_provider_configured`, `media_analysis_lifecycle_api.py:383` preflights only `_provider_configured`, and `AI_MODEL_CAPABILITY_MISSING` exists only in `ai_admin_api.py:85,601-605` (pong). `capabilities_for` is consumed only by pong and by the CLI vision probe (`cli/ai.py:_model_declares_vision`). Effect: a selected non-`vision_input` declared model is not refused for Analyze, contradicting the accepted plan §6 and the normative SPEC sentence, and control "a non-`vision_input` model is refused for pong and Analyze" is half-refuted. Smallest correction: add the same capability preflight (409 AI_MODEL_CAPABILITY_MISSING) to the `ai-suggestion-preview` routes, the durable-analysis request, and the automatic-analysis classification path, with tests.
LEAD: `_is_dns_name`/`_is_loopback_host` (`provider_records.py:357-377`) reject literal `localhost` and valid loopback IP literals but admit abbreviated/hex IPv4 hostnames (`127.1`, `0x7f000001`) that some resolvers map to loopback; the declared-base-URL loopback prohibition is therefore textual, not resolution-based. Cheapest check: resolve such a host in a throwaway process (no call needed) or tighten the host validator.
```

## 2. Per-claim verdict table (R1-R7)

| Claim | Verdict | Exact evidence |
|---|---|---|
| R1 no secret value in v2 config, API responses, browser surfaces, or logs | verified | `test_v2_declared_config_round_trips_with_exact_keys` (raw text: one `API_KEY` occurrence = declared `credential_env` name; no `Authorization`/`Bearer`/`data:`; 0600) and `test_write_and_load_config_persists_no_secret`; contract test asserts `CREDENTIAL_VALUE not in put.text/pong.text/after.text` and config path absent; `tests/unit/infrastructure/ai/test_openai_chat_completions.py::test_credential_value_never_appears_in_request_body`, `::test_repr_is_redacted`; `GenericAiProviderCredential.__repr__` redacted (`credentials.py`); `serialize_declared_provider_record` emits name only; no logging added in new modules (grep LOGGER/print in `openai_chat_completions.py`, `provider_activity.py`, `activity_lock.py`, `vision_probe.py`, `ai_admin_api.py`: none); browser JSON preview built from form fields (`app.js:11992-12016`) and test asserts no key-shaped fields; CLI output prints env names only |
| R2 admin routes cannot bypass authN/authZ | verified | Six `RoutePolicy` rows `channel=tailscale`, `capability=provider.operate`, `companion_mutation=False`, audit actions `ai.provider.put|delete|activate|ping|pong` (`tailscale_ingress.py:417-456`); middleware order: origin -> mutation header -> identity -> capability -> audited allowed attempt -> app (`tailscale_ingress.py:783-903`); `test_ai_admin_route_policies_are_provider_operate_gated_and_non_companion` + `test_ai_admin_routes_deny_ordinary_tailscale_identities` (3 passed focused); `test_authorization_matrix_and_audited_denial` (403 `CAPABILITY_DENIED` / `IDENTITY_NOT_AUTHORIZED`, audited denied `ai.provider.put` row, 403 `MUTATION_HEADER_REQUIRED`, 403 `MUTATION_ORIGIN_FORBIDDEN`, zero transport calls); `test_audit_rows_exist_before_provider_execution` (allowed `ai.provider.ping` row exists while the route path is still blocked); public composition inspection: `public_published_application.py` mounts only the public router + reject-unlisted catch-all, and `application.py:393-398` returns it before the admin router is included |
| R3 ping/pong/analyze privacy | verified | `test_connection` body is text-only (`build_chat_completions_connection_test_body`); pong requires `confirm_cloud_upload is True` before any resolution and sends `load_vision_probe_fixture()` only (`ai_admin_api.py:580-626`); `test_pong_requires_confirmation_and_declared_vision_capability` asserts zero transport calls without confirm; sidecar schema persists only `{schema_version, provider_id, model_id, status, matched, observed_color, probed_at_ms}` (`vision_probe.py:160-177`) with `_validated_observed_color` rejecting separator/control/format/surrogate/private-use categories; `test_vision_probe.py` judge/bounds/symlink/fail-safe tables; no catalog repository is referenced in the pong route; pong performs no suggestion persistence (inspection) |
| R4 v1 read compatibility; malformed fails closed | verified | `load_ai_server_config` accepts only schema 1/2 (`configuration.py:157-159`), v1 yields in-memory v2 with `providers={}` and preserved `active_provider_id`/`provider_models` (`:160-182`); writers always write `AI_CONFIG_SCHEMA_VERSION = 2` (`:215-225`); `test_v1_read_upgrades_to_v2_without_inventing_providers`, `test_v1_read_keeps_builtin_default_selection`; `test_unsupported_or_missing_config_version_is_rejected`; 4-case `test_malformed_declared_records_fail_closed` (missing keys, unknown model key, `http://`, built-in collision); `test_declared_active_without_selected_model_is_rejected`, `test_selection_for_undeclared_provider_is_rejected`, `test_oversized_config_is_rejected` (64 KiB bound on read and write) |
| R5 dynamic resolution without restart; no authorization widening; no silent movie-identification change | verified | `DynamicAiProviderResolver.resolve()` per call (`registry.py:201-231`); `LazyResolvedAiProvider` per-operation resolution (`:232-260`); app composition wires the shared resolver into manual preview, automatic executor, both capability endpoints, and the admin dependencies (`application.py:400, 628-668, 673-746, 765-768`); movie identification remains `startup_analysis_provider` with `identify_movie` (NVIDIA-only) (`application.py:703-724`); `test_dynamic_effect_without_restart` (PUT + activate then capability GETs report the declared identity, no restart), `test_dynamic_resolver_rereads_rewritten_config`, `test_lazy_provider_resolves_the_current_configuration_per_operation`, `test_lazy_provider_delegates_each_operation_to_the_resolved_provider` (lazy repr contains no credential); authorization unchanged: capability endpoints are read-only, admin routes still `provider.operate` |
| R6 NVIDIA/Vercel unregressed; Gallery/Details frozen | verified | Full selection green (882 passed) including `tests/unit/infrastructure/ai/test_nvidia_nim.py`, `test_vercel_gateway.py`, `test_credentials.py`, `tests/contract/test_media_suggestion_api.py`, `test_automatic_analysis_settings_api.py`; Vercel adapter is a thin subclass over the single generic implementation with the same constants/class path; NVIDIA changes are additive (`probe_vision`); `git diff --numstat` shows 0 deletions for `web/index.html` (73/0), `web/app.js` (985/0), `web/styles.css` (265/0) — the admin surface is purely additive; Gallery/Details behavior files outside the allowlist unchanged (49-path diff) |
| R7 repository hygiene | verified | Diff paths exactly the 49-path allowlist; `.ap` gitlink unchanged and clean; `origin/feat/x-meme-browser-companion` and `origin/main` still `33946e0` (no push); porcelain clean; no tags/stash added; single-path staging was reported per slice and the resulting history is linear with the declared subjects |

## 3. Controls table

| # | Control | Evidence | Result |
|---|---|---|---|
| P1 | Declared AP route runs the affected Python selection green | `./.ap/ap exec --root /home/agile/Projects/framenest --baseline 87411e0... --operation test-focus -- <16 paths> -q -p no:cacheprovider` -> `882 passed, 1 warning in 107.38s`, exit 0 (warning pre-existing) | PASS |
| P2 | Frontend suites green | `node --test tests/ai_providers_admin_frontend.test.js tests/tailscale_identity_frontend.test.js tests/companion_settings_automatic_analysis.test.js` -> 35 pass / 0 fail / 0 skipped (10.1 s) | PASS |
| P3 | Route inventory 1:1 and six new routes `provider.operate`-gated | focused: `test_route_policies_match_the_application_route_inventory`, `test_ai_admin_route_policies_are_provider_operate_gated_and_non_companion`, `test_ai_admin_routes_deny_ordinary_tailscale_identities` -> 3 passed; route rows cited under R2 | PASS |
| P4 | Fixture loadable + in a built wheel; exact bytes | worktree and committed blob both 74 bytes; SHA-256 `396f6aba97b0b4ac60a22cae643ef2df1676ab98050fa468bbcb1aadb69b9e44` (both); `file`: PNG 8x8 8-bit RGB; `test_ai_package_resources.py` -> 2 passed (resource boundary + wheel contains `framenest/infrastructure/ai/fixtures/vision-probe-red-8x8.png`) | PASS |
| P5 | Dynamic no-restart resolution proven | `test_dynamic_effect_without_restart` (also asserted in the focused 3-test run), `test_dynamic_resolver_rereads_rewritten_config`, `test_lazy_provider_resolves_the_current_configuration_per_operation` | PASS |
| P6 | ADR-0081 exists, internally consistent, no closed ADR edited; SPEC §22 sentences present; docs match code | ADR-0081 present with 7 decisions; diff adds only `docs/adr/0081-*.md` and the `docs/adr/README.md` index row (no closed ADR body touched); SPEC §22 contains the described changes; **but** ADR-0081 decision 4, SPEC.md:726-727, and AI_WORKSPACE.md:218-220 assert the Analyze `vision_input` refusal that is absent from the code | FAIL (one assertion not implemented) |
| N1 | No secret value/key shape/Authorization/raw payload/raw completion in config, API, CLI, JSON preview, logs; `credential_env` a name only | see R1 evidence; additionally `test_credential_environment_name_is_a_name_not_a_value`, `test_credential_environment_name_pattern_and_reserved_names`, `test_secret_shaped_record_strings_are_rejected`; CLI `vision-probe` prints only status/expected/observed bounded token (`cli/ai.py:570-642`) | PASS |
| N2 | Ordinary/unmapped sanitized 403 with audited denials; public composition neither mounts nor returns admin routes | `test_authorization_matrix_and_audited_denial`; `test_ai_admin_routes_deny_ordinary_tailscale_identities`; public composition inspection (see R2); note: GET denial is unaudited by design (`policy.audit_action is None` -> `_record_denial` returns early), matching plan §8 "none" for GET | PASS |
| N3 | Wrong/missing origin/header rejected; built-in and active PUT/DELETE refused; active-invalidating PUT refused; pong confirm required; non-vision pong refused; busy lock sanitized | `test_authorization_matrix_and_audited_denial`, `test_builtin_active_and_validation_refusals` (409 built-in PUT/DELETE, 409 active delete, 409 active-model-removal PUT, 404 unknown provider, 422 undeclared model, 422 unsupported protocol, 422 `http://`), `test_pong_requires_confirmation_and_declared_vision_capability` (409 x2, zero transport calls), `test_busy_activity_locks_return_conflict_without_provider_calls` (409 `.test.lock`/`.vision-probe.lock`) | PASS |
| N4 | Providers GET zero provider calls; UI open/typing no provider call; UI hiding not the authorization mechanism | contract test asserts `transport.calls == []` after GET list and after rejected requests; JS tests "dialog open performs exactly one list GET and typing stays local", "every unsafe fetch call site uses framenestMutationHeaders and the literal stays single", "AI providers header control exists hidden by default"; server middleware is the enforcement mechanism (R2) | PASS |
| N5 | Malformed/unsupported config fails closed; v1 reads without loss and is never written back as v1 | see R4 evidence; writer constant is v2 only | PASS |
| N6 | NVIDIA/Vercel unregressed; no Gallery/Details file outside the allowlist changed | see R6 evidence | PASS |
| N7 | Non-`vision_input` model refused for pong **and Analyze** | pong: `test_pong_requires_confirmation_and_declared_vision_capability` + `ai_admin_api.py:601`; **Analyze: REFUTED** — no capability preflight in `media_suggestion_api.py:251,352`, `media_analysis_lifecycle_api.py:383`, or the automatic-analyst (`application.py:677-695`); `AI_MODEL_CAPABILITY_MISSING` occurs only in `ai_admin_api.py`; no test covers it | REFUTED (Analyze side) |

## 4. Claim-versus-evidence discrepancies

1. **`02_report_06.md` §2/§5 vs repository truth.** The report claims the new
   SPEC §22 sentences cover "`vision_input` refusal for Analyze and the
   vision probe". Repository truth: only the vision probe (pong) and the CLI
   `vision-probe` enforce it; no Analyze path does. The docs assertion is
   therefore an unimplemented claim, and the docs themselves now overstate
   behavior (SPEC.md:726-727 is a normative MUST, ADR-0081 decision 4,
   AI_WORKSPACE.md:218-220).
2. **`02_report.md` §8 deviation D5 (env override).** Disclosed as PARTIAL and
   later corrected in `980db7a` (settings validator widened); candidate truth
   matches the corrected description (`configuration.py:53,375-377`), no open
   discrepancy.
3. **`02_report_04.md` §8 disclosures.** Automatic-analysis classification
   shift and the indirect app-level analyze proof are disclosed truthfully and
   independently confirmed below; the ping/pong taxonomy-response deviation is
   real and disclosed. No undisclosed discrepancy found in reports 02-05.
4. **`02_report_05.md` §12 style near-miss.** Confirmed true: the new
   media queries were moved to the end of `styles.css`, existing slicing
   contract passes (in the 882-pass selection).

## 5. Out-of-scope observations (ledger candidates, non-authorizing)

- `provider_records.py:357-377`: abbreviated/hex IPv4 hostnames
  (`127.1`, `0x7f000001`) satisfy `_is_dns_name` and are not classified as
  loopback, so the declared-base-URL "no loopback" rule is textual rather
  than resolution-based (defense-in-depth; administrator-only surface).
- `tailscale_ingress.py`: GET `/api/admin/ai/providers` denials are not
  audited because its policy intentionally carries no `audit_action`; the
  "audited denials" control holds for the five mutation routes only.
- `SECURITY.md:72` still frames server AI administration as CLI-only in its
  older sentence while the added paragraph documents the administrator
  surface (prose staleness only).
- `ai_admin_api.py:381-403`: the PUT active-model invariant is check-then-act
  across two config reads with no config mutation lock; a concurrent admin PUT
  could persist a selection not present in the record. `write_ai_server_config`
  validates selection presence but not model membership for declared records.
  (Concurrent same-administrator race; low impact; fail-closed only for
  presence.)

## 6. Residual-risk statement

1. **Automatic-analysis failure classification deviation** (unconfigured
   scheduler run now `PROVIDER_UNAVAILABLE` retryable). Verified real:
   `ExecuteAutomaticMediaAnalysis.execute` receives the lazy provider
   (`application.py:677-695`), its `provider is None` branch
   (`media_analysis_lifecycle.py:503`) is unreachable, and the lazy
   `MediaSuggestionProviderUnavailableError` classifies as
   `PROVIDER_UNAVAILABLE` (`:576-586`) with one-call safety preserved (no
   resolution -> no transport contact). **Assessment: acceptable for this
   whole's scope** (bounded retry semantics only; no privacy/security
   widening; existing suites green); it may optionally be folded into the
   correction below, but is not itself an acceptance blocker.
2. **Indirect routed-analyze proof limitation.** The app-level dynamic
   resolution proof uses the two capability endpoints plus `LazyResolvedAiProvider`
   delegation with a fake transport, not a catalog-driven routed analyze.
   **Assessment: acceptable for this whole's scope** as a proof-closure
   limitation; the composition is directly inspected and the preview routes
   preflight `_provider_configured` dynamically. This limitation is
   independent of the refuted capability control.
3. **Refuted control requiring a correction before acceptance:** the missing
   `vision_input` refusal on the Analyze paths (see N7). Because a correction
   would change runtime behavior and a capability/security-adjacent boundary,
   `scoped` re-acceptance is invalid under
   `PROMPT_CONTRACTS.md` Acceptance and Correction Record; full-fresh
   re-acceptance is required after any correction.

## 7. Capability and independence

- Requested: fresh independent audit, High reasoning, approximately 250k
  tokens, single-active topology, no sub-agents. Observed model/client/context:
  `unknown/not observably exposed` from inside this session; no telemetry
  claim is made. All evidence was produced through the declared sanitized AP
  route and read-only inspection.
- Independence: genuinely fresh session; this prompt was the initial context;
  no parent-conversation transcript or reasoning was inherited; no material
  participation in this implementation; prior reports were read as claims
  only and every accepted claim was re-verified against repository truth.

## 8. Persistence

This report is saved to the exact granted destination
`/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/03_report.md`
(verified absent, non-symlink, parent real) and read back in full before the
separate completion notice. Meta Git archival remains with the COOPERATOR; no
Meta Git operation and no FrameNest Git write occurred.

Resolved Execution Issues / Near-Misses: the acceptance prompt spells the
route as `./.ap/ap ap exec` (prints usage); resolved by running the declared
operation with the working `./.ap/ap exec` spelling, same baseline and
operation, no alternate route invented.

Pre-Existing Failure Classification: none carried into this acceptance; the
single collected warning (`PydanticJsonSchemaWarning`) is pre-existing and
unrelated.

Authority expiry: this terminal report ends the grant; no autonomous
continuation.

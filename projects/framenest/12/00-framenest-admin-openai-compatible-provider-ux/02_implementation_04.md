# Implementation Exchange 04 — Session 02 — Slice 3: Administrator AI Provider API, Route Policies, Audit, and Dynamic Provider Resolution

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker (current-session continuation)
Phase: Implementation
Task identity: IMPLEMENT-AI-PROVIDER-ADMIN-API-SLICE-3
Implementation authority: explicit
Delivery route: Agent Orchestrator default dispatch into the same session (continuity anchor below)
Reasoning recommendation: High — named risk: six new audited mutating routes on the security-sensitive provider boundary plus dynamic resolution across the application composition; authorization, audit-before-mutation, and no-secret/no-provider-call guarantees must be exactly right
Recommended context capacity: approximately 250k tokens
Independence required: no
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active

## Continuity anchor and authority renewal

Continuity anchor: your terminal PASS reports for exchange 02
(`02_report_02.md`) and exchange 03 (`02_report_03.md`) and your commits
`980db7af33910bb676eef46ed89fd2b453112bb6` and
`e6d91d1ba8cda0b22da2c345cbd313720e127e64`. Prior authority expired at the
last report. This is a complete renewed grant for slice 3 of the accepted
plan. Retained context is convenience, not authority; repository evidence
wins on conflict. Evidence in this exchange is non-independent.

## Goal

Implement slice 3: the six administrator AI provider HTTP routes with route
policies, audit-before-mutation, sanitized no-secret responses, and per-call
dynamic provider resolution so a record added or activated through the API
takes effect without a service restart. No admin UI, no documentation
changes in this slice.

## Mandatory reading

- The accepted plan
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/01_report_orchestrator.md`
  §3-§8 (schema, adapter, registry, capabilities, ping/pong, admin API), §13
  test 7, §14 slice 3.
- Read before editing: `src/framenest/adapters/api/application.py` (AI
  composition at ~617-760 and ~1620-1645), `tailscale_ingress.py` (route
  policy table and mutation-origin logic), `media_suggestion_api.py`,
  `media_analysis_lifecycle_api.py`, `runtime_settings_api.py` (router
  mounting pattern), `registry.py`, `configuration.py`, `vision_probe.py`,
  `activity_lock.py`, `credentials.py`.
- Test patterns: `tests/contract/test_tailscale_ingress_security.py`
  (tailscale_uds client, identity map, audit recorder, 1:1 route inventory),
  `tests/contract/test_automatic_analysis_settings_api.py`,
  `tests/contract/test_public_published_uds.py`.

## Repository gate (before mutation)

Verify: HEAD equals `e6d91d1ba8cda0b22da2c345cbd313720e127e64` (this
exchange's authorized baseline), porcelain clean, branch
`feat/x-meme-browser-companion`, `.ap` gitlink unchanged,
`./.ap/ap ap doctor` PASS. Stop on any unexplained difference.

## Slice 3 deliverables (binding design)

### D1 — `src/framenest/adapters/api/ai_admin_api.py` (new)

Router factory plus a frozen dependency dataclass. All six routes:
`Cache-Control: no-store`, sanitized JSON only, no secret, key shape,
Authorization header, provider payload, absolute path, or credential value in
any response. Error body shape matches the existing
`{"error": {"code", "message"}}` convention.

| Method | Path | Request | Response | Audit |
|---|---|---|---|---|
| GET | `/api/admin/ai/providers` | — | `{active_provider_id, active_model_id, configuration_source, providers:[{provider_id, display_name, source, protocol, base_url, credential_env, credential_available, selected_model_id, supports_vision, models:[{model_id, display_name, capabilities}], last_test, last_vision_probe}], supported_protocols, limits}` | none (network-free) |
| PUT | `/api/admin/ai/providers/{provider_id}` | `{name, protocol, base_url, credential_env, models:{id:{name,capabilities:[]}}}` | the stored record, sanitized | `ai.provider.put`, target `ai_provider`, group `provider_id` |
| DELETE | `/api/admin/ai/providers/{provider_id}` | — | `{removed_provider_id}` | `ai.provider.delete`, target `ai_provider`, group `provider_id` |
| PUT | `/api/admin/ai/active-selection` | `{provider_id, model_id}` | `{active_provider_id, active_model_id}` | `ai.provider.activate`, target `ai_provider` |
| POST | `/api/admin/ai/ping` | `{}` | `{status, tested_at_ms, provider_id, model_id, credential_available}` | `ai.provider.ping`, target `ai_provider` |
| POST | `/api/admin/ai/pong` | `{confirm_cloud_upload: true}` | `{status, matched, expected_color, observed_color, probed_at_ms, provider_id, model_id}` | `ai.provider.pong`, target `ai_provider` |

Behavior rules:

- GET is network-free and performs zero provider calls; it reads the current
  config, credential-availability booleans, the safe last test state, and the
  safe vision-probe sidecar (matching provider/model only).
- PUT validates through the existing `provider_records` validators; a
  built-in id is `409 AI_PROVIDER_BUILTIN`; an unsupported `protocol` is
  `422 AI_PROVIDER_PROTOCOL_UNSUPPORTED`; other validation failures are
  `422 AI_PROVIDER_INVALID` with a sanitized reason; a record update that
  would remove the currently selected model of the active provider is
  `409 AI_PROVIDER_ACTIVE` (select another model first). Writes config v2
  atomically.
- DELETE refuses built-ins (`409 AI_PROVIDER_BUILTIN`) and the active
  provider (`409 AI_PROVIDER_ACTIVE`); otherwise removes the record and its
  `provider_models` entry, atomically.
- PUT active-selection validates that the provider exists (built-in or
  declared) and that the model is selectable for it; unknown provider
  `404 AI_PROVIDER_NOT_FOUND`, unknown model `422 AI_PROVIDER_INVALID`.
- POST ping: resolve the active provider per call; if unconfigured or the
  credential is unavailable, `503 AI_PROVIDER_NOT_CONFIGURED` with the env
  **name** in the message; acquire the `.test.lock` activity lock (busy ->
  `409 AI_PROVIDER_BUSY`); run `test_connection()`; classify exceptions with
  the shared classifier (D2); persist the safe `AiTestState`; return the
  sanitized status. HTTP/transport `403 -> authentication_failed` with
  entitlement-aware copy; never "invalid response".
- POST pong: require `confirm_cloud_upload is True` else
  `409 CLOUD_CONFIRMATION_REQUIRED`; resolve per call; refuse a model whose
  declared capabilities lack `vision_input` (`409 AI_MODEL_CAPABILITY_MISSING`);
  acquire the `.vision-probe.lock` activity lock (busy -> `409 AI_PROVIDER_BUSY`);
  load the committed fixture, call `probe_vision`, judge with
  `match_expected_color`, persist the sanitized `vision-probe-state.json`,
  and return the sanitized result. Never persist, log, or return raw
  completion text — only the bounded token.
- Store/write failures are `503 AI_CONFIG_UNAVAILABLE` with a sanitized
  message.
- The provider taxonomy for ping/pong errors: `503
  AI_PROVIDER_AUTHENTICATION_FAILED`, `429 AI_PROVIDER_RATE_LIMITED`, `503
  AI_PROVIDER_MODEL_UNAVAILABLE`, `503 AI_PROVIDER_UNAVAILABLE`, `502
  AI_PROVIDER_INVALID_RESPONSE`, `502 AI_PROVIDER_FAILED`.

### D2 — `src/framenest/infrastructure/ai/provider_activity.py` (new)

One shared `classify_provider_exception(exc: Exception) -> str` returning the
existing sanitized categories (`authentication_failed`,
`rate_limited_or_quota_exhausted`, `model_unavailable`, `provider_unreachable`,
`invalid_response`, `provider_error`), covering the extended errors
(empty/refusal/truncated -> `invalid_response`, pending-timeout ->
`provider_unreachable`) exactly as the current CLI mapping does. Refactor
`src/framenest/adapters/cli/ai.py` to use it without changing any CLI output
or behavior (`test_ai_cli.py` stays green). Add focused unit tests in
`tests/unit/infrastructure/ai/test_provider_activity.py`.

### D3 — Dynamic provider resolution (no restart)

In `src/framenest/infrastructure/ai/registry.py`:

- `DynamicAiProviderResolver(settings, *, environ=None, config_path=None)`
  with `resolve() -> ResolvedAiProvider` re-reading the persisted config and
  environment per call.
- `LazyResolvedAiProvider(resolver)` implementing the provider surface the
  application services actually use (verify by reading
  `src/framenest/application/media_suggestion.py` and the preview services;
  at minimum `suggest(request)`, `test_connection()`, and `probe_vision(...)`)
  by resolving once per operation and raising the existing sanitized
  `MediaSuggestionProviderUnavailableError` when unconfigured or
  uncredentialed. Do not let a single operation observe two different
  resolutions.

In `src/framenest/adapters/api/application.py`:

- Compose the manual preview services and the automatic-analysis executor
  through the lazy provider so a provider added or activated through the API
  takes effect without restart.
- Add an optional `read_provider: Callable[[], ResolvedAiProvider]` to
  `MediaSuggestionApiDependencies` and
  `MediaAnalysisLifecycleApiDependencies`; the capability endpoints prefer it
  when present and keep current static behavior when absent, so existing
  tests that inject static dependencies stay valid.
- Movie identification keeps its current startup-resolved, NVIDIA-only
  wiring; document that a runtime provider switch does not add movie
  identification to other providers.
- Mount the new admin router beside the runtime settings router.

In `src/framenest/adapters/api/media_suggestion_api.py` and
`src/framenest/adapters/api/media_analysis_lifecycle_api.py`: consume
`read_provider` where present for provider identity, availability, and
capability reads; preserve existing response shapes and all current tests.

### D4 — Route policies

Add exactly six `RoutePolicy` rows in `tailscale_ingress.py` following the
existing pattern: `channel=tailscale`, capability `provider.operate`,
`companion_mutation=False`, with the audit actions and target groups from D1.
The `public_published_uds` composition must not mount any of them. The 1:1
route-inventory contract test must pass unchanged; `test_x_route_policy.py`
must stay green with exactly five `companion_mutation` routes.

### D5 — Store helpers

Add only what is genuinely needed in `configuration.py` for atomic record
upsert/removal and active-selection writes (for example a
`mutate_ai_server_config` style helper); keep v1 read compatibility, atomic
write, 0600, and symlink posture unchanged.

## Exact changed-path allowlist

```text
src/framenest/adapters/api/ai_admin_api.py (new)
src/framenest/adapters/api/application.py
src/framenest/adapters/api/tailscale_ingress.py
src/framenest/adapters/api/media_analysis_lifecycle_api.py
src/framenest/adapters/api/media_suggestion_api.py
src/framenest/infrastructure/ai/provider_activity.py (new)
src/framenest/infrastructure/ai/registry.py
src/framenest/infrastructure/ai/configuration.py
src/framenest/adapters/cli/ai.py
tests/contract/test_ai_provider_admin_api.py (new)
tests/contract/test_tailscale_ingress_security.py
tests/unit/infrastructure/ai/test_provider_activity.py (new)
tests/unit/infrastructure/ai/test_registry.py
tests/unit/adapters/cli/test_ai_cli.py
```

No other file may be created, edited, deleted, or moved.
`tests/contract/test_x_route_policy.py` and
`tests/contract/test_media_suggestion_api.py` are expected to pass
unmodified; if either genuinely requires a change, stop and report instead.

## Tests

1. `tests/contract/test_ai_provider_admin_api.py` (new), in `tailscale_uds`
   mode with a fake transport and a temp config path, modeled on
   `test_tailscale_ingress_security.py`:
   - admin GET/PUT/DELETE/activate/ping/pong happy paths with sanitized
     bodies; no secret or key shape anywhere;
   - GET performs zero provider calls; PUT/DELETE/ping/pong each perform at
     most one provider call when applicable;
   - ordinary identity -> `403 CAPABILITY_DENIED` with an audited denial row;
     unmapped -> `403 IDENTITY_NOT_AUTHORIZED`; missing mutation header or
     wrong origin -> `403`;
   - built-in PUT/DELETE -> `409 AI_PROVIDER_BUILTIN`; delete-active ->
     `409 AI_PROVIDER_ACTIVE`; PUT removing the active selected model ->
     `409 AI_PROVIDER_ACTIVE`; pong without confirm -> `409
     CLOUD_CONFIRMATION_REQUIRED`; pong on a non-vision model -> `409
     AI_MODEL_CAPABILITY_MISSING`; busy lock -> `409 AI_PROVIDER_BUSY`;
   - audit rows exist before ping/pong execution (allowed attempt recorded);
   - dynamic effect: after PUT provider + PUT active-selection, the
     `GET /api/ai/media-suggestion-capability` and
     `GET /api/ai/automatic-analysis-capability` responses reflect the new
     identity without restart, and the lazy analyze path resolves the new
     provider.
2. `tests/contract/test_tailscale_ingress_security.py` (edit): explicit
   assertions that the six new routes are `provider.operate`-gated,
   non-companion, and denied to ordinary identities; the existing 1:1
   inventory test then covers the table.
3. `tests/unit/infrastructure/ai/test_provider_activity.py` (new): the
   classifier table for every provider error type and the fallback.
4. `tests/unit/infrastructure/ai/test_registry.py` (edit): dynamic resolver
   re-reads a config rewritten between calls; lazy provider delegates and
   raises sanitized unavailable when unconfigured.
5. `tests/unit/adapters/cli/test_ai_cli.py` (edit only if the shared
   classifier refactor requires it; expected green with no or minimal
   changes).

Validation ladder:

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the named suites above
Affected tests: tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_tailscale_ingress_security.py tests/contract/test_x_route_policy.py tests/contract/test_public_published_uds.py tests/contract/test_media_suggestion_api.py tests/contract/test_ai_server_composition.py tests/contract/test_automatic_analysis_settings_api.py
New causal regression: the six admin routes, audit-before-mutation, dynamic no-restart resolution, and the shared classifier have no prior coverage
Broad or full suite: not-used — no project rule or named decision risk requires it for this slice
Runtime or testbed: not-used
Independent acceptance: not-required
```

## Commands (canonical execution route — binding)

```text
./.ap/ap ap project check --root /home/agile/Projects/framenest --baseline e6d91d1ba8cda0b22da2c345cbd313720e127e64
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline e6d91d1ba8cda0b22da2c345cbd313720e127e64 --operation runtime-info
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline e6d91d1ba8cda0b22da2c345cbd313720e127e64 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_tailscale_ingress_security.py tests/contract/test_x_route_policy.py tests/contract/test_public_published_uds.py tests/contract/test_media_suggestion_api.py tests/contract/test_ai_server_composition.py tests/contract/test_automatic_analysis_settings_api.py -q -p no:cacheprovider
```

## Authority

Positive: edit/create only the allowlisted paths; the declared AP route;
read-only Git; stage exactly the allowlisted paths; one local commit with
subject `Add administrator AI provider API and dynamic provider resolution`;
no push; the single Meta report below.

Negative: everything outside the allowlist; any UI/frontend/extension change;
any documentation or ADR change; any other Git write; any provider/network
call (all tests use fake transports); NUC/SSH/sudo/browser/GUI; ambient
Python, `poetry run`, `pip`, `uv`, environment reconstruction; secret access;
`git add .`/`-A`; no weakening or deleting existing tests, and no change to
`test_x_route_policy.py` or `test_media_suggestion_api.py`.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_04.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest unless this prompt grants FrameNest Git.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report contract

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 02`, `Worker exchange ordinal: 04`); compact
core: status; `Phase-qualified result: implementation-PASS` on PASS else
`not-applicable`; start commit `e6d91d1…`; end commit; changed files; tests
and validation with exact counts; commit result; deviations/risks; one
smallest next step; `Report justification: new-mutation`; authority-expiry
statement; `Orchestration critique` (MEASURED/LEAD); Resolved Execution
Issues / Near-Misses and Pre-Existing Failure Classification;
`Logical-whole closure: not-closed`. Save, read back fully, verify identity,
then a short separate completion notice with location and SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when a gate fails unclassifiably, a needed
change exceeds the allowlist, an existing test must be weakened, the
execution route is unusable, the Meta destination is occupied or unsafe, or
retained context conflicts with repository evidence.

Authority expiry: this terminal report ends this grant; no autonomous
continuation.

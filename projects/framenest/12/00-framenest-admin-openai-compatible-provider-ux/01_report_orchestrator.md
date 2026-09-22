### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: PLAN-OPENAI-COMPATIBLE-PROVIDER-REGISTRY-AND-VISION-PROBE
status: PASS
Phase-qualified result: not-applicable
Start commit: 33946e08447dc92621ed6844b4b5d13a19ec29f1
End commit: 33946e08447dc92621ed6844b4b5d13a19ec29f1
Report justification: new-evidence
Logical-whole closure: not-closed

Repository gate (independently re-observed 2026-09-16, read-only):
physical root `/home/agile/Projects/framenest`; branch
`feat/x-meme-browser-companion`; porcelain clean; HEAD
`33946e08447dc92621ed6844b4b5d13a19ec29f1` ("Remove unreachable legacy library
browser client"); remote `https://github.com/cisarik/framenest.git`; `.ap`
gitlink == `.ap` HEAD == `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`;
`./.ap/ap doctor` PASS (stable variant, managed block OK); no foreign worktree
or active mutation observed. Packaged Alembic head `0033`
(`src/framenest/infrastructure/persistence/alembic_environment/versions/0033_media_analysis_proposals.py`,
`down_revision = "0032"`); no `0034` exists. Baseline focused evidence through
the declared AP route:
`./.ap/ap exec --root /home/agile/Projects/framenest --baseline 33946e08447dc92621ed6844b4b5d13a19ec29f1 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_server_composition.py tests/contract/test_x_route_policy.py tests/contract/test_automatic_analysis_settings_api.py -q -p no:cacheprovider`
-> `180 passed in 6.02s`.

This report is the plan. It is decision-complete, repository-grounded, and
approval-gated. No implementation was performed.

---

# Implementation Plan — framenest-admin-openai-compatible-provider-registry-and-vision-probe

## 1. Whole verdict

**Identity: keep exactly**
`framenest-admin-openai-compatible-provider-registry-and-vision-probe`.

Rationale: the Cooperator's acceptance target stated in the trace notes is "add
OpenAI-compatible providers, judging function, design, and administrator UX"
(`00_notes.md` confirmed-refinements ledger items 4-7). The administrator
surface is not a cosmetic successor; it is the operator boundary through which
the registry becomes usable. Splitting the UI into a successor would leave the
primary outcome unaccepted and would ship a registry only the CLI can drive,
which the Cooperator explicitly refused ("not a third hardcoded enum"; no
copy-paste/CLI-only operating mode). A tighter kebab was considered and
rejected: `admin-openai-provider-registry` drops the committed vision fixture
and the ping/pong acceptance path, which are the distinguishing deliverables.

**One coherent outcome after acceptance, publication to public `main`, and
routine NUC refresh:** the Cooperator signs in as FrameNest administrator to
the NUC web shell, adds an OpenAI-compatible provider record (OpenCode Go),
selects the vision model, pings it, runs the color pong, and then uses the
existing Analyze path with that provider — judging function, design, and
administrator UX step by step.

**Challenge "UI belongs in this whole": keep it.** Repository evidence:
`ADR-0079` (`docs/adr/0079-administrator-automatic-analysis-runtime-setting.md`
decision 5) deferred website Settings and left the companion Administration
section with only the automatic-analysis checkbox; `SERVER.md`
"Current MacBook MVP Non-Goals" (line 362) lists "centralized browser provider
Settings" as a non-goal; the Cooperator operates the NUC server from this web
shell. This whole is that website administrator surface for provider records
only; it does not overload the companion checkbox and does not build the
ADR-0023 inline model picker.

**No migration `0034`: confirmed.** All new state is non-secret JSON sidecars
and environment/systemd credentials. Evidence: Alembic head `0033` with no
`0034`; the accepted precedent for a durable administrator bool without a
migration is ADR-0079's `runtime-settings.json` sidecar
(`src/framenest/infrastructure/runtime_settings.py`). The provider registry
adds no SQLite table, no column, and no catalog write. Catalog backup exclusion
of `ai/config.json` (SECURITY.md line 93) extends naturally to the new sibling
sidecar.

## 2. Correction ledger (verified, corrected, refuted)

Verified exactly as stated in the prompt (all read at the pinned baseline):

| Prompt statement | Evidence |
|---|---|
| Config v1 `{schema_version, active_provider_id, provider_models, updated_at_ms}`, atomic 0600, symlink refusal, platform path or `FRAMENEST_AI_CONFIG_PATH` | `src/framenest/infrastructure/ai/configuration.py:21-36, 110-134, 147-190, 299-351` |
| `SUPPORTED_PROVIDER_IDS` hardcodes `nvidia-nim`, `vercel-ai-gateway` | `configuration.py:25` |
| Hardcoded `PROVIDER_DEFINITIONS`; precedence env override -> persisted -> legacy NVIDIA when `NVIDIA_API_KEY` -> unconfigured | `src/framenest/infrastructure/ai/registry.py:73-84, 100-118` |
| Credential wrappers redacted, env first, exact-name systemd `CREDENTIALS_DIRECTORY`, 4096-byte bound | `src/framenest/infrastructure/ai/credentials.py:11-16, 53-121` |
| `HttpsJsonTransport` bounded, redirect rejection, sanitized 401/403 -> auth rejected, 429, 404, 5xx | `src/framenest/infrastructure/ai/transport.py:41-111` |
| Vercel adapter is OpenAI chat-completions with `image_url` data URLs; base URL is a module constant; constructor accepts `provider_id`/`model_id` | `src/framenest/infrastructure/ai/vercel_gateway.py:98-137, 219-238` |
| NVIDIA adapter specialized (202 polling, movie identification); helpers `extract_message_content`, `parse_suggestion_content_text`, `build_media_suggestion` | `src/framenest/infrastructure/ai/nvidia_nim.py:442, 629, 682, 850-1147` |
| CLI `status`/`configure`/`test`/`still-frame-smoke`; smoke refuses non-NVIDIA | `src/framenest/adapters/cli/ai.py:62-107, 250-312, 315-340` |
| `provider.operate` already administrator-only | `src/framenest/domain/identity_access.py:31, 67-86` |
| Route policy 1:1 contract; five `companion_mutation` routes; website-origin mutation proof is exact origin + `X-FrameNest-Request: 1` with no extension flag needed | `src/framenest/adapters/api/tailscale_ingress.py:187-631, 741-765, 1023-1034`; `tests/contract/test_tailscale_ingress_security.py:584-634`; `tests/contract/test_x_route_policy.py:107-121` |
| Capability/status taxonomy and `confirm_cloud_upload` gate | `src/framenest/adapters/api/media_suggestion_api.py:74-84, 214-293, 410-438` |
| Read-only Status dialog + `#ai-status-button`; `identityState.available` true only for `tailscale_workspace` | `src/framenest/adapters/api/web/app.js:445, 1813-1828, 1865-1884, 1992-2057`; `index.html:118-127, 360-399` |
| Companion Administration only automatic analysis, `provider.operate`-gated | `extension/ui/sidebar.js:373-395, 666-694`; `tests/companion_settings_automatic_analysis.test.js` |
| Deploy helper hardcodes two provider credential/template maps; two-line systemd templates | `deploy/ubuntu/production_ai_deploy.py:44-52`; `deploy/systemd/framenest-ai-credential-nvidia-nim.conf`, `...-vercel-ai-gateway.conf` |
| `.secrets/ai.env.fish` is sourced generically (no per-variable allowlist) | `framenest:90-139`; `README.md:286`; `SECURITY.md:70-80` |

Repository-grounded corrections and refinements to the prompt:

1. **Frontend admin gating correction (material).** `identityAllowsAdminWorkflow`
   (`app.js:316-320`) requires `identityState.available`, which is set true
   only for `tailscale_workspace` (`app.js:445`). In loopback TCP development
   the server returns `trusted_loopback` with the full administrator capability
   set (`application.py:1396-1416`) but the existing admin helpers hide admin
   chrome. The prompt's requirement "the rendered admin surface must remain
   correct in both audiences" therefore cannot be met by reusing
   `identityAllowsAdminWorkflow`. The plan defines a dedicated
   `identityAllowsProviderAdministration()` (§9) that admits
   `trusted_loopback` and verified `tailscale_workspace` administrators and
   hides the surface for ordinary/unmapped/public identities.
2. **`validate_provider_id` is an enum today and is reused by test-state and
   status-snapshot validation** (`configuration.py:84-91, 204, 217, 286`).
   Schema v2 requires a bounded-identifier validator instead of an enum, and
   the existing test case `"unsupported"` in
   `tests/unit/infrastructure/ai/test_ai_configuration_storage.py:164-210`
   must change to a syntactically invalid id. Without this, v2 cannot store
   declared provider identities.
3. **`test_write_and_load_config_persists_no_secret` asserts
   `"API_KEY" not in raw`** (`test_ai_configuration_storage.py:53`). Because
   `credential_env` is an environment-variable *name* ("OPENCODE_API_KEY"),
   that exact assertion must be replaced by name-aware no-secret assertions
   (no `Authorization`, no `Bearer`, no key-shaped value, and at most the
   declared `credential_env` names). Repository truth wins over the stale
   assertion.
4. **Static provider resolution breaks the acceptance flow.** The server
   resolves the AI provider once at app creation (`application.py:617-661`)
   and the status reader closes over that fixed identity
   (`application.py:1627-1642`); `media_analysis_lifecycle_api.py` receives
   static `provider_configured`/`provider_id`/`model_id`. If left static, adding
   a provider in the admin UI would require a service restart before Analyze
   uses it, which contradicts the accepted dynamic-precedence precedent of
   ADR-0079 and the routine NUC refresh model. The plan therefore specifies a
   dynamic resolver and lazy provider proxy (§4, §5).
5. **External-fact refinement (OpenCode Go, re-fetched 2026-09-16).**
   `https://opencode.ai/docs/go/` (page "Last updated: Sep 14, 2026") confirms:
   chat-completions endpoint `https://opencode.ai/zen/go/v1/chat/completions`;
   models catalog `https://opencode.ai/zen/go/v1/models`; model id
   `deepseek-v4-flash-vision-exp` exists and is an
   `@ai-sdk/openai-compatible` chat-completions model; Go is a $10/month
   subscription whose model list also contains `/responses` (Grok, GPT Luna,
   Muse Spark) and `/messages` (MiniMax, Qwen) models; **privacy**: DeepSeek
   V4 Flash Vision Exp is "Not used" for training with 0-day retention (ZDR
   agreement through 2026-09-30), while the *Muse Spark Contributor* models do
   train on prompts. The prompt's blanket "free trial models may train" warning
   is therefore refined: the risk is Contributor-tier models, not the pinned
   vision model. `https://opencode.ai/docs/zen/` confirms Zen is a distinct
   endpoint family `https://opencode.ai/zen/v1/...` with a different billing
   surface; Go and Zen must not be aliased.
6. **New external constraint for the record (risk, not a design blocker).**
   Go documents that traffic is monitored for abuse, that clients "should send
   typical coding agent traffic", identify themselves with their own user
   agent, and send a stable `x-opencode-session` per conversation. FrameNest
   image analysis is not coding-agent traffic; this is a Cooperator
   billing/terms decision (§16, R-1). The plan does not fabricate coding-agent
   identity or session semantics.
7. **Prompt statement "the two-line `LoadCredential=` templates" is exact**;
   the new OpenCode Go template must also be exactly two lines plus the
   `[Service]` header, and `tests/contract/test_production_ai_deployment.py`
   enforces tracked byte equivalence (lines 171-227).
8. **`pyproject.toml` must carry an explicit include for the new fixture.**
   Web assets are explicitly listed (`pyproject.toml:26-34`); the committed
   PNG fixture needs the same treatment or the built wheel cannot serve pong.

## 3. Architecture decision — non-secret provider configuration schema v2

**Owner:** `src/framenest/infrastructure/ai/configuration.py` keeps file
read/write, atomicity, and permissions. A new sibling module
`src/framenest/infrastructure/ai/provider_records.py` owns record dataclasses,
record validation, capability allowlist, protocol constant, and built-in
record construction. Import direction is one-way: `provider_records` <-
`configuration` <- `registry`.

**Exact on-disk shape (strict JSON, sorted keys, compact separators,
trailing newline, 0600, symlink refusal, atomic `os.replace` — all unchanged
from `_atomic_write_json`, `configuration.py:312-351`):**

```json
{"active_provider_id":"opencode-go","provider_models":{"opencode-go":"deepseek-v4-flash-vision-exp"},"providers":{"opencode-go":{"base_url":"https://opencode.ai/zen/go/v1","credential_env":"OPENCODE_API_KEY","models":{"deepseek-v4-flash-vision-exp":{"capabilities":["vision_input"],"name":"DeepSeek V4 Flash Vision Exp"}},"name":"OpenCode Go","protocol":"openai-chat-completions"}},"schema_version":2,"updated_at_ms":1757973600000}
```

**Semantics and rules (decision-complete):**

- `schema_version`: accepts `1` (read-only compatibility) and `2`; writers
  always write `2`. A v1 file read yields an in-memory v2 config with
  `providers = {}`; `active_provider_id` and `provider_models` map unchanged
  (v1 could only contain the two built-ins, so no information is lost). v1 is
  never written again. A malformed/unsupported version stays fail-closed with
  the existing sanitized `AiConfigurationError` posture (startup refusal is the
  current behavior for malformed config).
- `providers`: optional map of declared records. Unknown keys inside a record
  or a model entry are rejected (fail closed; no silent forward-compat).
  Declaring `nvidia-nim` or `vercel-ai-gateway` is rejected as malformed
  (built-ins are implicit code definitions, not file records).
- Record fields: `name` (1-80 chars, no control characters), `protocol`
  (exactly `openai-chat-completions` in this slice; any other value is
  rejected with the sanitized unsupported-protocol error), `base_url`,
  `credential_env`, `models`.
- Model entry: `name` (1-80), `capabilities` (list; subset of the SPEC §22
  provider-neutral names: `vision_input`, `video_input`,
  `structured_text_output`, `image_generation`, `image_editing`,
  `reference_image`, `local_execution`, `cloud_execution`). At least one model
  is required.
- Bounds: <= 16 declared providers; <= 64 models per provider; provider id and
  model id each <= 120 with no whitespace (model id keeps existing
  `validate_model_id` semantics); provider id additionally must match
  `^[a-z0-9][a-z0-9._-]{0,63}$`; `credential_env` must match
  `^[A-Z][A-Z0-9_]{0,63}$` and must not be one of the reserved transport names
  (`Authorization`, `Cookie`, `Content-Type`, `Host`, `User-Agent`); record
  strings must not contain `apiKey`, `api_key`, `Authorization`, `Bearer `, or
  a `data:` URI (defense in depth, rejected with a sanitized error); whole file
  <= 64 KiB.
- `credential_env` is the environment-variable **name**, never a value.
  Inline `options.apiKey`-style keys are forbidden in FrameNest JSON and in
  every browser surface. FrameNest never reads
  `~/.config/opencode/opencode.json(c)` or any local jsonc file as config;
  only the operator mental model of named providers with a base URL and a
  models map is mirrored (verified against
  `https://opencode.ai/docs/providers/` "Custom provider", retrieved
  2026-09-16).
- `provider_models`: selected model per provider id. Keys must be built-in or
  declared. For a declared `active_provider_id`, a missing selection is a
  sanitized malformed-config error; for a built-in it falls back to the
  built-in default model (existing behavior). No selection is ever invented.
- Built-in records (code constants, exposed through the same registry type so
  there is one world, not two):
  - `nvidia-nim`: display "NVIDIA NIM", protocol `nvidia-nim` (adapter kind),
    base URL `https://integrate.api.nvidia.com/v1/chat/completions` (existing
    constant), credential `NVIDIA_API_KEY`, default model
    `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`, capability
    `vision_input`.
  - `vercel-ai-gateway`: display "Vercel AI Gateway", protocol
    `openai-chat-completions`, base URL
    `https://ai-gateway.vercel.sh/v1` (derived from the existing chat
    completions constant), credential `AI_GATEWAY_API_KEY`, default model
    `google/gemini-3.1-flash-lite`, capability `vision_input`.
- URL policy for declared records: `https://` only; no userinfo (`@`), no
  query, no fragment, no explicit port, no trailing slash; host must be a DNS
  name (`[A-Za-z0-9-]+` labels, dot-separated, <= 253 chars) and must not be
  `localhost`, `*.localhost`, or a loopback IP literal. Request URLs are
  constructed as `base_url + "/chat/completions"`. Loopback base URLs for
  local gateways are explicitly deferred (documented), matching the prompt's
  recommended option; `file:`, `unix:`, and non-HTTPS are rejected.
- Credentials stay out of the file, the browser, snapshots, logs, and
  exceptions. The existing redacted-`repr` wrappers and the 4096-byte bounded
  exact-name `CREDENTIALS_DIRECTORY` lookup (`credentials.py:75-121`) remain
  the only credential path.
- Admin API responses and CLI output expose only: provider id, display name,
  protocol, base URL, credential env **name**, credential availability
  boolean, declared model metadata, and sanitized status categories.

## 4. Generic adapter decision

**New module** `src/framenest/infrastructure/ai/openai_chat_completions.py`:

- `build_chat_completions_suggestion_body(request, *, model_id, image_encoder)`
  — the existing `build_vercel_gateway_request_body` body construction, moved
  and parameterized (one to three bounded JPEG derivatives as `image_url` data
  URLs; `response_format: {"type": "json_object"}` retained for suggestions
  only).
- `build_chat_completions_connection_test_body(*, model_id)` — existing text
  ping body.
- `build_chat_completions_vision_probe_body(*, model_id, prompt, image)` — one
  image, fixed prompt, `temperature: 0`, small `max_tokens`.
- `class OpenAiChatCompletionsMediaSuggestionProvider`: constructor
  `(credential, *, base_url, provider_id, model_id, transport=None,
  image_encoder=None)`; methods `suggest(request)`, `test_connection()`,
  `probe_vision(*, prompt, image_png) -> str`, `__repr__` redacted.
- Error mapping is exactly the current Vercel mapping
  (`vercel_gateway.py:187-216`): HTTP/transport 401/403 ->
  `MediaSuggestionProviderAuthError`, 429 -> rate limited, 404 -> model
  unavailable, 5xx -> unavailable, other 4xx/bad JSON -> invalid response.
  **403 is authentication/entitlement, never "invalid response"** — the
  operator-facing copy for 403 says the credential or model entitlement was
  rejected (this is the exact failure the Cooperator previously experienced as
  "provider response was invalid" with no progress).
- One call in flight, no automatic retries, explicit
  `REQUEST_TIMEOUT_SECONDS = 120`, bounded request (24 MiB) and response
  (1 MiB) bodies. A static `User-Agent: framenest/0.1` header is added to
  chat-completions requests; no session header fabrication (§16 R-1).

**Vercel collapse:** `vercel_gateway.py` keeps the module path and class name
`VercelAiGatewayMediaSuggestionProvider` as a thin subclass of the generic
class with the existing constant base URL and constructor signature. This
keeps `tests/unit/infrastructure/ai/test_vercel_gateway.py` and external
imports valid while there is a single request implementation.

**NVIDIA:** stays specialized (202 polling, movie identification) and gains
`probe_vision` implemented via the shared probe body plus its existing
`_post_and_decode` path, so pong is not NVIDIA-blocked.

**`response_format` policy:** server-side only, suggestions only, fail-closed
parsing. A provider that ignores it returns parseable JSON or the existing
`MediaSuggestionProviderInvalidResponseError`; no retry, no silent fallback.
Per-record override is deferred (backlog).

**`still-frame-smoke`:** unchanged behavior (legacy NVIDIA-only diagnostic) to
preserve back-compatibility; its help text and docs are amended to mark it
legacy and point to the new provider-neutral `vision-probe` (§7, §10).

**Dynamic resolution (required for acceptance):** `registry.py` gains
`DynamicAiProviderResolver` (a per-call `resolve_ai_provider` wrapper) and a
`LazyResolvedAiProvider` that delegates `suggest`, `test_connection`, and
`probe_vision` to the currently resolved adapter, raising the existing
sanitized `MediaSuggestionProviderUnavailableError` when unconfigured or
uncredentialed. `application.py` composes:
- the manual preview services and the automatic-analysis executor through the
  lazy provider (so a provider added in the admin UI takes effect without
  restart);
- `GET /api/ai/media-suggestion-capability`, the Status reader, and
  `GET /api/ai/automatic-analysis-capability` through per-call resolution;
- movie identification remains wired as today (the workflow is frozen and
  companion-excluded); a runtime provider switch does not add movie
  identification to non-NVIDIA providers, and this is documented rather than
  silently absorbed.

## 5. Registry, credentials, and resolution precedence

- `registry.py` exposes one definition type for both worlds:
  `AiProviderDefinition(provider_id, display_name, protocol, base_url,
  credential_environment_name, source: "builtin"|"declared", default_model_id,
  models: tuple[AiProviderModel, ...], builtin: bool)`.
  `PROVIDER_DEFINITIONS` becomes a function
  `provider_definitions(config: AiServerConfig | None)` merging built-ins with
  declared records; the module-level constant remains as the built-ins map for
  backward-compatible imports.
- Precedence is unchanged in order and meaning: explicit
  `FRAMENEST_AI_PROVIDER_ID`/`FRAMENEST_AI_MODEL_ID` environment override ->
  persisted v2 config -> legacy NVIDIA compatibility when `NVIDIA_API_KEY`
  is present and no provider configuration exists -> unconfigured. Declared
  provider ids are valid in the environment override; an unresolvable override
  remains a sanitized error.
- Credential resolution per record: `load_ai_credential(environment_name,
  environ)` generalized from `load_nvidia_api_credential` /
  `load_vercel_ai_gateway_credential`; environment first, then exact-name
  `CREDENTIALS_DIRECTORY` lookup, 4096-byte bound, symlink/regular-file checks
  unchanged. Missing credential yields `credential_available=False` and no
  provider instance; the server still starts and reports
  `credential_unavailable` with the env **name** in the operator hint.
- `ResolvedAiProvider` gains `protocol`, `base_url`, `provider_source`,
  `models`, and `capabilities_for(model_id)`; existing fields keep their
  meaning so `media_suggestion_api.py` call sites change minimally.
- `validate_provider_id` becomes the bounded-identifier validator (§3);
  `SUPPORTED_PROVIDER_IDS` is replaced by `BUILTIN_PROVIDER_IDS`.
  `provider_default_model(provider_id)` becomes
  `default_model_for(definition)` and is only used for built-ins.

## 6. Capability model

- Exact capability names are the SPEC §22 set; this slice consumes
  `vision_input` only.
- Declaration authority: the operator declares per-model capabilities inside
  the record. Built-in records declare `vision_input` for their default model
  (both are already used with frames today).
- Analyze (all `ai-suggestion-preview` routes and automatic analysis) and Pong
  refuse a selected model that does not declare `vision_input` with sanitized
  `409 AI_MODEL_CAPABILITY_MISSING`; Ping remains available for text-only
  models. The administrator UI marks capability chips and disables Pong for
  non-vision models with an explanatory note.
- Refresh from `GET {baseURL}/models` is **deferred** (backlog): opening the
  dialog, typing, hovering, or rendering the list must never call a provider
  (SPEC §22 line 767). The dialog's list GET is network-free and reads only
  the local config plus credential-availability booleans.
- Unsupported protocols (`/responses`, `/messages`, Anthropic-style bodies)
  are documented as unsupported in the dialog help copy and living docs, and
  are rejected at record save with a named error instead of failing opaquely
  at request time.

## 7. Ping and pong contract

| Step | Server operation | Persists | Must not do |
|---|---|---|---|
| Add record | validate + atomic config v2 write | non-secret record | write secrets |
| Activate | set `active_provider_id` + `provider_models[provider_id]` | selection | invent a model |
| Ping | `test_connection()` on the active provider+model | reuse `AiTestState` (safe category + timestamp) | send frames |
| Pong | committed fixture PNG + fixed prompt -> `probe_vision()` -> judge | new `vision-probe-state.json` (safe fields only) | use catalog media; persist a suggestion; log raw completion |
| Analyze | existing product path | existing behavior | auto-run on browse |

- **Fixture decision: one golden committed PNG.**
  Path `src/framenest/infrastructure/ai/fixtures/vision-probe-red-8x8.png`
  with `fixtures/__init__.py`; 8x8 pixels, solid sRGB RGB(255,0,0), plain PNG
  (no ancillary chunks), loaded through `importlib.resources` from the
  `framenest.infrastructure.ai` package boundary and added to
  `pyproject.toml`'s explicit include list (`pyproject.toml:29-34`) so the
  built wheel carries it. Rationale over in-process generation: exact bytes,
  one pinned sha256 for tests, reviewable artifact, and no generator drift.
  The outbound derivative reuses `PillowVlmImageDerivativeEncoder.encode_png_bytes`
  (`image_derivative.py:97-127`), which is deterministic for a solid image.
- **Prompt:** `VISION_PROBE_PROMPT = "What color is this? Answer with one word."`
  with `VISION_PROBE_PROMPT_VERSION = "framenest-vision-probe-v1"`. English
  prompt; the judge (not the prompt) accepts Slovak.
- **Judge:** `match_expected_color(text) -> str | None` in
  `src/framenest/infrastructure/ai/vision_probe.py`. Normalization: Unicode
  lowercase, strip control characters, replace punctuation with spaces, take
  the bounded token window (<= 32 chars); accept `red`, `crimson`, `scarlet`,
  `vermillion`, `červená`, `cervena`, `#ff0000`, `ff0000`; no fuzzy matching;
  empty/unparseable/other colors -> `None`. Expected color constant:
  `red`. Never execute or echo raw model text beyond the bounded normalized
  token.
- **Statuses:** `success` (judge matched), `mismatch` (provider answered but
  the expected color was not recognized — honest, not an error),
  `authentication_failed`, `rate_limited_or_quota_exhausted`,
  `model_unavailable`, `provider_unreachable`, `invalid_response`,
  `provider_error`. Transport/HTTP 403 maps to `authentication_failed` with
  entitlement-aware copy.
- **Persistence:** `vision-probe-state.json` beside the config path (atomic,
  0600, symlink refusal, same helpers), body
  `{schema_version, provider_id, model_id, status, matched, observed_color,
  probed_at_ms}` where `observed_color` is the judge's allowlisted normalized
  token or `null`; raw completion text is never persisted or logged. Existing
  status/test-state files keep their schemas and gain no secret content.
- **Rate limit:** one call in flight. A small shared helper
  (`infrastructure/ai/activity_lock.py`) wraps the existing
  `.test.lock` pattern (`cli/ai.py:421-428`); ping uses `.test.lock`, pong
  uses `.vision-probe.lock`; busy -> sanitized `409 AI_PROVIDER_BUSY`.
- **Audit:** the Ping/Pong routes carry `provider.operate`, an `audit_action`,
  and `audit_target_type="ai_provider"` so the Tailscale ingress records the
  allowed attempt before the route executes (ADR-0048 decision 6) and records
  denials. In loopback TCP mode the middleware is not installed (existing
  posture), so no audit table is written locally; this is stated in tests and
  docs.
- **`confirm_cloud_upload`:** Pong requires it (missing -> `409
  CLOUD_CONFIRMATION_REQUIRED`, same sanitized code as analysis). Ping is a
  text-only explicit click and does not require it.
- **CLI:** new `framenest-ai vision-probe [--confirm-cloud-upload]` running
  the same server-side fixture path against the active provider and printing
  sanitized output (`AI vision probe: success`, `Expected color: red`,
  `Observed color: red`, or the sanitized failure). `still-frame-smoke` is
  unchanged and documented as legacy NVIDIA-only.

## 8. Admin API

New module `src/framenest/adapters/api/ai_admin_api.py` (router factory and a
frozen dependency dataclass), mounted in `application.py` next to the runtime
settings router (`application.py:1299-1303`) and included in the route
inventory. All routes: `channel=tailscale`, capability `provider.operate`,
`companion_mutation=False` (website-origin mutations already pass with the
exact external origin plus `X-FrameNest-Request: 1`;
`tailscale_ingress.py:1023-1034`). Ordinary Tailscale identities receive 403
`CAPABILITY_DENIED` (denial audited); unmapped identities 403
`IDENTITY_NOT_AUTHORIZED`; public `public_published_uds` never mounts these
routes.

| Method | Path | Request | Response (sanitized) | Audit |
|---|---|---|---|---|
| GET | `/api/admin/ai/providers` | — | `{active_provider_id, active_model_id, configuration_source, providers:[{provider_id, display_name, source, protocol, base_url, credential_env, credential_available, selected_model_id, supports_vision, models:[{model_id, display_name, capabilities}], last_test, last_vision_probe}], supported_protocols, limits}` | none (matches existing AI capability GETs; network-free) |
| PUT | `/api/admin/ai/providers/{provider_id}` | `{name, protocol, base_url, credential_env, models:{id:{name,capabilities:[]}}}` | the stored record, sanitized | `ai.provider.put`, target `ai_provider` |
| DELETE | `/api/admin/ai/providers/{provider_id}` | — | `{removed_provider_id}` | `ai.provider.delete`, target `ai_provider` |
| PUT | `/api/admin/ai/active-selection` | `{provider_id, model_id}` | `{active_provider_id, active_model_id}` | `ai.provider.activate`, target `ai_provider` |
| POST | `/api/admin/ai/ping` | `{}` | `{status, tested_at_ms, provider_id, model_id, credential_available}` | `ai.provider.ping`, target `ai_provider` |
| POST | `/api/admin/ai/pong` | `{confirm_cloud_upload: true}` | `{status, matched, expected_color, observed_color, probed_at_ms, provider_id, model_id}` | `ai.provider.pong`, target `ai_provider` |

Error codes (all `Cache-Control: no-store`): `AI_PROVIDER_BUILTIN` 409,
`AI_PROVIDER_ACTIVE` 409 (delete while active; select another first),
`AI_PROVIDER_INVALID` 422 (sanitized reason), `AI_PROVIDER_NOT_FOUND` 404,
`AI_PROVIDER_PROTOCOL_UNSUPPORTED` 422, `AI_MODEL_CAPABILITY_MISSING` 409,
`CLOUD_CONFIRMATION_REQUIRED` 409, `AI_PROVIDER_BUSY` 409, plus the existing
provider taxonomy (`AI_PROVIDER_AUTHENTICATION_FAILED` 503,
`AI_PROVIDER_RATE_LIMITED` 429, `AI_PROVIDER_MODEL_UNAVAILABLE` 503,
`AI_PROVIDER_UNAVAILABLE` 503, `AI_PROVIDER_INVALID_RESPONSE` 502,
`AI_PROVIDER_FAILED` 502) and `AI_CONFIG_UNAVAILABLE` 503 for store failures.
`configuration_source` surfaces `environment`, `server config`, or
`unconfigured` so an environment override that shadows admin changes is
visible honestly.

Required contract-test and policy updates:
- six new `RoutePolicy` rows in `tailscale_ingress.py` following the exact
  existing pattern; `test_route_policies_match_the_application_route_inventory`
  (`test_tailscale_ingress_security.py:584-634`) then enforces 1:1
  correspondence; `test_x_route_policy.py:114-121` (exact `companion_mutation`
  set) remains five routes because none of the new routes is a companion
  route.
- new `tests/contract/test_ai_provider_admin_api.py` covering the full matrix
  (§13), including audit-before-mutation for ping/pong in `tailscale_uds`.
- README API list gains the six routes; SERVER/SPEC text updated (§12).

## 9. Administrator UI

**Launch point:** one new header control
`<button id="ai-providers-button" class="status-button status-button--icon"
hidden aria-label="AI provider administration" title="AI provider
administration">` with glyph `🛠️` in the existing header control group
(`index.html:96-138`). The 🧠 Status dialog stays read-only and unchanged; no
Add Provider control is placed in it.

**New dialog:** `<dialog id="ai-providers-dialog" class="settings-dialog"
aria-label="AI providers">` reusing the existing `settings-dialog` visual
language (`styles.css:491-580`) — same dark premium surface, tabs not needed.

Component inventory:
- `#ai-providers-active-summary` — active provider/model, credential
  availability ("Credential available to this process: yes/no"), and an
  environment-override warning when `configuration_source` is `environment`.
- `#ai-providers-list` — one row per provider: display name, id,
  `Built-in`/`Declared` badge, protocol, base URL, credential env name,
  credential availability, model chips with capability badges, selected-model
  marker, last ping and last pong summaries; actions `Use for analysis`,
  `Ping`, `Test vision`, `Edit` (declared only), `Delete` (declared,
  non-active only).
- `#ai-providers-form` — labeled fields `id`, display name, base URL,
  credential env name, protocol (read-only value with an "other protocols are
  not supported yet" note), model rows (model id, display name,
  `vision_input` checkbox chip), Add/Remove model controls.
- `#ai-providers-json-preview` — read-only `<pre>` showing the exact strict
  JSON that would be written, built locally from form state; never contains a
  secret value; satisfies the Cooperator's jsonc mental model without jsonc in
  the server file.
- Actions: `#ai-provider-save`, `#ai-provider-activate`, `#ai-provider-ping`,
  `#ai-provider-pong`, `#ai-provider-delete`.
- Pong confirmation: an in-dialog confirm block (same pattern as the companion
  automatic-analysis confirm) naming the fixture ("a tiny solid-red test
  square made by FrameNest"), the provider, and a cost/privacy note; only the
  confirm button issues the POST with `confirm_cloud_upload: true`.
- Progress: while ping/pong runs, set `aria-busy="true"` on the dialog,
  disable the two action buttons, and show an accessible indeterminate status
  line ("Testing connection…", "Sending the color test…"); no fabricated
  percentages.
- Results: sanitized human copy for every status/code, including
  403-entitlement ("The provider rejected the credential or this model is not
  included in your subscription."), credential missing with the env **name**
  in the hint, mismatch showing "The model answered, but not with the expected
  color." plus the bounded observed token, busy, confirm required, built-in
  read-only, and active-delete refusal.
- Identity gating (new helper, source-visible):
  `identityAllowsProviderAdministration()` = resolved AND
  `isWorkspaceAudience()` AND capability `provider.operate` AND
  (`identityState.available` OR audience `trusted_loopback`). Verified NUC
  administrators and trusted loopback development see the control; ordinary
  Tailscale users, unmapped identities, unresolved bootstrap, and public
  published callers never see it and get no empty chrome. Capability checks
  remain UI convenience only; the server and route policy are the
  authorization mechanism.
- No-provider-call rule: opening the dialog performs only the network-free GET
  list; typing and JSON-preview updates are local; ping/pong/probe happen only
  on explicit click; capability discovery stays network-free (SPEC §22 line
  767).
- Accessibility and narrow width for this surface only: native `<dialog>`
  focus behavior, Escape close, labeled inputs, `role="status"`
  `aria-live="polite"` message region, `role="alert"` errors, checkbox
  capability chips with visible focus states, keyboard reachable row actions,
  and the existing narrow-width media queries; Gallery and Details are not
  restyled.

## 10. CLI

- `configure`: provider list becomes built-ins + declared records with dynamic
  numbering; selection may name a declared provider; model validation checks
  the record's declared models (or accepts a bounded model id when the record
  is edited manually). Writes v2 atomically. Non-interactive
  `--provider-id/--model-id/--yes` accepts declared ids.
- `status`: same sanitized output plus one new line
  `Provider source: builtin|declared`; remains network-free.
- `test`: unchanged semantics (one explicit text-only ping, safe state
  persisted); works for declared providers.
- New `vision-probe [--confirm-cloud-upload]` per §7; exit 0 on `success`, 2
  for confirmation missing, unsupported model capability, and every sanitized
  failure; no raw completion output.
- `still-frame-smoke`: unchanged behavior and output; help text marked
  "legacy NVIDIA-only"; docs amended.
- All CLI success/error output excludes keys, Authorization headers, base64
  payloads, raw provider responses, absolute paths, and database paths.

## 11. Credentials and deployment source material (repository only)

- `deploy/systemd/framenest-ai-credential-opencode-go.conf` (new, exact
  two-line `LoadCredential=` contract):
  `[Service]` +
  `LoadCredential=OPENCODE_API_KEY:/etc/framenest/credentials/OPENCODE_API_KEY`.
- `deploy/ubuntu/production_ai_deploy.py`: add
  `"opencode-go": "OPENCODE_API_KEY"` to `PROVIDER_CREDENTIALS` and
  `"opencode-go": DEPLOY_SYSTEMD_DIR / "framenest-ai-credential-opencode-go.conf"`
  to `PROVIDER_DROPIN_TEMPLATES` (`production_ai_deploy.py:44-52`).
- `tests/contract/test_production_ai_deployment.py`: extend the exact mapping
  and tracked-byte tests (lines 171-227) for the third provider.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` §"Production AI Credential Helper"
  (lines 562-615): add OpenCode Go as the third supported credential identity.
- Local development: no code change; `.secrets/ai.env.fish` is sourced
  generically (`framenest:90-139`). Update `README.md:286`, `SECURITY.md:72-80`
  (and `AI_WORKSPACE.md:77-81`) to document `OPENCODE_API_KEY` alongside the
  two existing keys.
- **Explicitly out of scope:** running `fn-production-env-deploy` against the
  live NUC, installing any credential, touching `/etc/framenest/*`, or
  restarting the service. Live credential installation is a separate explicit
  Cooperator grant. The NUC is never contacted in this whole by any Worker
  except under a later bounded task.

## 12. Documentation changes (exact owners, before -> after)

**New ADR 0081** (next free number; `0080` exists, index
`docs/adr/README.md:107`):
`docs/adr/0081-declarative-openai-compatible-provider-registry-and-administrator-vision-probe.md`.
Status `Accepted` only after Cooperator approval. Outline: Context (CLI-only
operator boundary, ADR-0079 deferred website Settings, Cooperator intent for
declarative providers, dated OpenCode Go facts); Decision (config v2 records,
built-in/declared one-world registry, generic OpenAI chat-completions adapter,
capability filtering, administrator web surface under `provider.operate` with
audit and website-origin mutation proof, ping/pong with committed synthetic
fixture, credential env names only, dynamic no-restart resolution); Superseded
statements (narrow notes, no closed body edited): ADR-0020's
operator-boundary/`Revisit` triggers fulfilled for non-secret provider
administration; ADR-0023's deferred provider discovery contract partially
implemented (declared capabilities only); ADR-0035's "operator-only provider
administration" phrase is read as including the authenticated administrator
web surface; ADR-0036's credential mechanism extended by a third identity;
ADR-0044's "provider-management UI remain deferred" succeeded; ADR-0079's
"website Settings deferred" succeeded for the provider surface only; ADR-0075
refresh framing unchanged. Deferred: model-catalog refresh,
`/responses`//`messages` protocols, Zen record, loopback base URLs, persistent
drafts, inline model picker. Update the ADR index row.

**SPEC.md §22 "AI and Privacy" exact sentence changes:**
1. Before: "Server AI provider administration MUST use an operator boundary.
   The initial operator boundary is `./framenest ai configure`, `./framenest
   ai status`, and `./framenest ai test`." After: server AI provider
   administration MUST use an operator boundary: the CLI (`./framenest ai
   ...`) plus an authenticated administrator-only web surface reached through
   `provider.operate` over the trusted Tailscale workspace ingress; ordinary
   browser clients MUST NOT configure AI providers, activate models, enter
   provider API keys, receive provider API keys, or call external AI
   providers directly.
2. Before: "NVIDIA NIM and Vercel AI Gateway are supported server providers in
   this slice." After: "NVIDIA NIM and Vercel AI Gateway remain supported
   built-in server providers, and the server supports operator-declared
   OpenAI-compatible provider records (first instance: OpenCode Go at
   `https://opencode.ai/zen/go/v1`) persisted as non-secret schema-versioned
   configuration."
3. Before: "Server AI configuration files MUST contain only schema-versioned
   non-secret provider/model selection and safe timestamps." After: "Server AI
   configuration files MUST contain only schema-versioned non-secret
   provider/model selection, declarative provider records (provider id,
   display name, protocol, base URL, credential environment-variable **name**,
   declared models, and declared capabilities), and safe timestamps. They MUST
   NOT contain API keys, Authorization headers, cookies, provider responses,
   prompts, frame data, media paths, or database paths."
4. New normative sentences: administrator-initiated `ping` MUST be an explicit
   text-only provider request; administrator-initiated `pong` MUST send
   exactly one repository-owned synthetic fixture image and MUST require
   explicit cloud-upload confirmation; neither MUST use catalog media, persist
   a suggestion, or run without an explicit administrator action. Analyze and
   the vision probe MUST refuse a selected model that does not declare
   `vision_input`. A provider HTTP 403 MUST be reported as credential or
   entitlement rejection, not invalid output. Provider declarations MUST be
   `https://` only for non-loopback hosts; local gateway base URLs are
   deferred.

**SECURITY.md** (§ "Logs and Diagnostics", after line 80): add a paragraph
naming the administrator AI provider surface, its `provider.operate` +
audit-before-mutation posture, the no-secret browser rule, the synthetic pong
fixture, the one-call-in-flight limit, 403 entitlement semantics, the
`OPENCODE_API_KEY` local/`.secrets` and systemd credential support, and the
dynamic no-restart resolution. Extend the `.secrets/ai.env.fish` sentence to
`NVIDIA_API_KEY`, `AI_GATEWAY_API_KEY`, and/or `OPENCODE_API_KEY`.

**SERVER.md** §"Server-Side AI Provider Boundary" (lines 293-330): replace
"Ordinary browser and desktop clients do not configure providers" with the
precise rule (ordinary clients never; authenticated administrators may manage
non-secret records and run ping/pong through the server). Update the browser
Status modal paragraph to mention the separate administrator surface. Remove
or amend the "centralized browser provider Settings" bullet in "Current
MacBook MVP Non-Goals" (line 362) because it is now implemented for providers
only (companion automatic-analysis checkbox unchanged; desktop Settings still
unshipped).

**README.md** (lines 284-286 and the route list at 240-261): add the six admin
routes, the new `vision-probe` CLI, the v2 config/declared providers, and
`OPENCODE_API_KEY` support; keep the "browser never configures providers"
sentence accurate for ordinary clients.

**AI_WORKSPACE.md** §"Current Implementation Boundary" and
§"Inline Model Picker"/"Capability Labels": state that server-side provider
administration now includes the administrator web surface and declarative
capability declarations; the inline picker and persistent drafts remain
deferred.

**docs/UBUNTU_NUC_DEPLOYMENT.md** and **ROADMAP.md**: runbook section as in
§11. ROADMAP: no product-state change is required; do not add a stale "active
logical whole" claim (Orchestrator-owned). No new living document is created
for the registry; SPEC/SERVER/SECURITY/AI_WORKSPACE stay the owners.

## 13. Tests

Python (pytest via the canonical AP route):
1. `tests/unit/infrastructure/ai/test_provider_records.py` (new) — record
   validation bounds, protocol allowlist, URL policy table (http/file/unix/
   userinfo/port/query/trailing slash/localhost/loopback IP), credential-env
   pattern, capability allowlist, built-in id collision, secret-pattern
   rejection, `credential_env` proven to be a name not a value.
2. `tests/unit/infrastructure/ai/test_ai_configuration_storage.py` (edit) —
   v2 round-trip exact keys; v1 -> v2 read compatibility (active provider and
   selections preserved, nothing invented); unknown record keys rejected;
   declared-active-without-model rejected; atomic/0600/symlink behavior
   unchanged; **no-secret assertions rewritten** so the only `API_KEY`
   occurrences are declared `credential_env` names; status/test-state
   validators accept bounded declared ids and reject truly invalid ids
   (replace the `"unsupported"` case).
3. `tests/unit/infrastructure/ai/test_registry.py` (edit) — declared
   resolution, model selection, capability lookup, missing credential,
   unconfigured, environment override to a declared provider, legacy NVIDIA
   unchanged, dynamic resolver sees a config rewritten between calls.
4. `tests/unit/infrastructure/ai/test_openai_chat_completions.py` (new;
   `test_vercel_gateway.py` kept green) — suggestion/ping/probe request bodies,
   data-URL framing, base URL joining, 403 -> auth, 429/404/5xx mapping,
   bounded bodies, no secret in headers/body, one call per invocation.
5. `tests/unit/infrastructure/ai/test_vision_probe.py` (new) — judge table
   (`red`, `Crimson.`, `scarlet`, `#ff0000`, `červená`, `cervena`, `blue` ->
   None, empty -> None, injection-ish text -> None), fixture sha256/size/
   dimensions, prompt and version constants, probe-state sidecar round-trip
   and allowlisted-color-only persistence, cross-provider/model filtering.
6. `tests/unit/adapters/cli/test_ai_cli.py` (edit) — configure with a declared
   provider, `vision-probe` success/mismatch/no-confirm/unsupported-capability,
   `still-frame-smoke` regression unchanged.
7. `tests/contract/test_ai_provider_admin_api.py` (new, `tailscale_uds`) —
   admin CRUD/activate/ping/pong with fake transport; ordinary identity 403
   `CAPABILITY_DENIED` with an audited denial row; missing mutation header or
   wrong origin 403; unmapped 403; built-in edit/delete 409; delete-active
   409; pong without confirm 409; pong on non-vision model 409; busy lock 409;
   GET list and every response free of secret values, Authorization headers,
   absolute paths, and provider payloads; GET list performs zero provider
   calls; audit row exists before ping/pong execution; dynamic effect: after
   PUT providers + activate, the capability GET reports the new identity
   without restart.
8. `tests/contract/test_ai_server_composition.py` (edit) — declared provider
   `credential_unavailable` identity preserving, last vision-probe evidence,
   no fabricated fallback.
9. `tests/contract/test_tailscale_ingress_security.py` (edit) — explicit
   assertions that the six new routes are `provider.operate`-gated,
   non-companion, and denied to ordinary identities; the 1:1 inventory test
   then covers the route table.
10. `tests/contract/test_production_ai_deployment.py` (edit) — third provider
    credential/template mapping and tracked bytes; template validation rejects
    malformed payloads (existing negative tests extended).
11. `tests/contract/test_ai_package_resources.py` (new) — the fixture is
    loadable through `importlib.resources` and is present in a built wheel,
    following `tests/contract/test_web_package_resources.py`.
12. Regression (unchanged, included in per-slice runs):
    `tests/contract/test_public_published_uds.py` (no new routes in the public
    allowlist), `tests/contract/test_media_suggestion_api.py`,
    `tests/contract/test_automatic_analysis_settings_api.py`.

JavaScript (`node --test`, exact files):
13. `tests/ai_providers_admin_frontend.test.js` (new) — markup inventory and
    hidden-by-default control; dialog reuses `settings-dialog` classes; gating
    helper cases for loopback admin, tailscale admin, ordinary, public,
    unresolved, and network-failure identities; **no fetch on dialog open and
    on typing**; JSON preview has no secret fields and mirrors the form; ping/
    pong only on explicit clicks; pong confirm required; mutation call sites
    all use `framenestMutationHeaders` (keeps
    `tests/tailscale_identity_frontend.test.js:307-313` green, including its
    single `"X-FrameNest-Request"` literal count); failure-copy mapping
    contains no provider payload; no `window.confirm`.
14. `tests/tailscale_identity_frontend.test.js` (edit only if the new header
    control needs an explicit assertion; the existing header test at lines
    329-357 does not constrain the count, so prefer leaving it untouched and
    extending coverage in the new file).

## 14. Slicing (ordered, independently verifiable)

Each slice is one fresh Implementation Worker grant with an exact changed-path
allowlist; slices 3 and 4 additionally require slices 1-2 to be green first.

**Slice 1 — Schema v2 + records + registry + generic adapter + CLI + deploy
source material (no UI, no pong).**
Changed paths: `src/framenest/infrastructure/ai/provider_records.py` (new),
`configuration.py`, `registry.py`, `credentials.py`, `constants.py`,
`openai_chat_completions.py` (new), `vercel_gateway.py`, `nvidia_nim.py`
(probe method deferred to slice 2), `src/framenest/adapters/cli/ai.py`,
`deploy/systemd/framenest-ai-credential-opencode-go.conf` (new),
`deploy/ubuntu/production_ai_deploy.py`,
`tests/unit/infrastructure/ai/test_provider_records.py` (new),
`tests/unit/infrastructure/ai/test_ai_configuration_storage.py`,
`tests/unit/infrastructure/ai/test_registry.py`,
`tests/unit/infrastructure/ai/test_openai_chat_completions.py` (new),
`tests/unit/adapters/cli/test_ai_cli.py`,
`tests/contract/test_production_ai_deployment.py`,
`tests/contract/test_ai_server_composition.py`.
Verification: focused unit + contract suites through `./.ap/ap exec
--operation test-focus`; the CLI can configure a declared OpenCode Go record
from a test config with no secret on disk.

**Slice 2 — Vision probe (pong): fixture + judging + state + CLI + NVIDIA
probe.**
Changed paths: `src/framenest/infrastructure/ai/vision_probe.py` (new),
`src/framenest/infrastructure/ai/fixtures/__init__.py` (new),
`.../fixtures/vision-probe-red-8x8.png` (new), `pyproject.toml` (include
entry), `openai_chat_completions.py`, `nvidia_nim.py`,
`src/framenest/adapters/cli/ai.py`,
`tests/unit/infrastructure/ai/test_vision_probe.py` (new),
`tests/contract/test_ai_package_resources.py` (new),
`tests/unit/adapters/cli/test_ai_cli.py`.
Verification: fixture sha256 pinned, judge table, CLI `vision-probe` through a
fake transport, wheel-resource contract.

**Slice 3 — Administrator API + route policies + audit + dynamic resolution.**
Changed paths: `src/framenest/adapters/api/ai_admin_api.py` (new),
`src/framenest/adapters/api/application.py`,
`src/framenest/adapters/api/tailscale_ingress.py`,
`src/framenest/adapters/api/media_analysis_lifecycle_api.py` (dynamic
capability reads), `registry.py` (resolver/proxy), `configuration.py` (record
store helpers if needed), `tests/contract/test_ai_provider_admin_api.py`
(new), `tests/contract/test_tailscale_ingress_security.py`,
`tests/contract/test_x_route_policy.py` (only if the exact flagged set
changes; expected unchanged).
Verification: 403 matrix, audit-before-mutation, no-secret responses,
capability-read dynamism, route inventory 1:1, public composition regression.

**Slice 4 — Administrator web surface.**
Changed paths: `src/framenest/adapters/api/web/index.html`,
`src/framenest/adapters/api/web/app.js`,
`src/framenest/adapters/api/web/styles.css`,
`tests/ai_providers_admin_frontend.test.js` (new),
`tests/tailscale_identity_frontend.test.js` (only if needed).
Verification: `node --test tests/ai_providers_admin_frontend.test.js
tests/tailscale_identity_frontend.test.js tests/companion_settings_automatic_analysis.test.js`.

**Slice 5 — Living docs + ADR 0081 + index + runbook.**
Changed paths: `SPEC.md`, `SECURITY.md`, `SERVER.md`, `README.md`,
`AI_WORKSPACE.md`, `docs/adr/0081-*.md` (new), `docs/adr/README.md`,
`docs/UBUNTU_NUC_DEPLOYMENT.md`.
Verification: documentation review, links/paths, no closed ADR body edited,
spec sentences exactly as §12.

**After slice 5:** fresh independent acceptance of the exact candidate, then
an explicit publication grant, then routine NUC refresh
(`deploy/ubuntu/framenest-release status` / `check --release <SHA>` / deploy),
then the Cooperator's numbered UX test. Recommended implementation Worker
profile for session 02: **Fresh Implementation Worker** with
`Native planning mode: not-used`, exact baseline, per-slice allowlist, and the
canonical `./.ap/ap exec` route. Documentation slice 5 may reuse the same
session (healthy same whole) or a fresh implementation session; independence
is required only at acceptance.

## 15. Cooperator acceptance plan (numbered, one behavior per step)

Local development (MacBook, loopback TCP; no cost, no credential required):
1. `./framenest start` -> the web shell opens; Status 🧠 shows read-only AI
   status unchanged. Expected: no new provider call, no regression.
2. As loopback administrator, the 🛠️ "AI provider administration" control is
   visible (trusted loopback), while an ordinary/unmapped NUC identity would
   not see it. Expected: control present locally, absent for ordinary users.
3. Open the dialog and add: id `opencode-go`, name `OpenCode Go`, protocol
   `openai-chat-completions`, base URL `https://opencode.ai/zen/go/v1`, credential
   env `OPENCODE_API_KEY`, model `deepseek-v4-flash-vision-exp` with
   `vision_input`. Expected: JSON preview shows the exact non-secret record,
   no key field anywhere, Save succeeds.
4. With no local key: "Credential available to this process: no"; Ping and
   Test vision disabled with a hint naming `OPENCODE_API_KEY`. Expected: no
   provider contact, honest disabled state.
5. (Optional, only if Michal chooses and adds `OPENCODE_API_KEY` to
   `.secrets/ai.env.fish`): Ping -> `success`; Test vision -> confirm ->
   expected color `red`. Expected: a real call only after the explicit click
   and confirmation.

NUC (only after publication to public `main` and routine refresh; credential
install is a separate explicit grant):
6. Publish the accepted SHA to public `main` (publication grant), then on the
   NUC run `deploy/ubuntu/framenest-release status` and
   `deploy/ubuntu/framenest-release check --release <40-hex-SHA>`; then deploy
   per the runbook. Expected: the NUC serves exactly that SHA.
7. Separate credential grant: install `OPENCODE_API_KEY` with
   `fn-production-env-deploy --provider opencode-go` (explicit authority;
   never part of this whole's default path).
8. As administrator on the NUC Tailscale origin: 🛠️ is visible, 🧠 Status
   stays read-only, companion Settings keeps only the automatic-analysis
   checkbox. Expected: the new surface is administrator-only.
9. Add the OpenCode Go record, select `deepseek-v4-flash-vision-exp`, click
   "Use for analysis". Expected: the record and selection persist; Status
   reflects the new active provider without a service restart.
10. Click Ping. Expected: `success`, or an honest sanitized failure
    (entitlement/rate/model/unreachable) with actionable copy and no provider
    payload.
11. Click Test vision, confirm the cloud-upload prompt. Expected: server sends
    only the tiny red fixture; result reports `red` (or an honest `mismatch`
    with the model's bounded color word); no catalog change.
12. Ordinary Tailscale identity or signed-out state: the control is hidden and
    a direct request is denied. Expected: 403, no empty chrome.
13. Open a real Gallery item and use the existing `Analyze by AI` path.
    Expected: confirmation required, analysis uses OpenCode Go, and no
    metadata is saved automatically.

Michal is never asked to accept unpublished code the NUC cannot serve.

## 16. Risks, unknowns, and Cooperator questions (with one default each)

- **risk R-1 (Cooperator decision, billing/terms):** OpenCode Go is marketed
  for coding-agent traffic and documents abuse monitoring. Default: implement
  the generic record and a static FrameNest `User-Agent`; do not fabricate a
  coding-agent identity or `x-opencode-session` semantics; the Cooperator owns
  the subscription/use decision; switching to Zen or another gateway is one
  new record.
- **risk R-2 (material model fact):** the live Go catalog is only known from
  dated public docs; `deepseek-v4-flash-vision-exp` is the only vision model
  named today. Default first vision model:
  `deepseek-v4-flash-vision-exp`; the record is editable in the admin UI if
  the catalog disagrees, so no code change is needed.
- **risk R-3 (privacy):** Contributor-tier models train on prompts. Default:
  never pin Contributor/free models; document Go privacy facts (DeepSeek
  vision: no training, ZDR through 2026-09-30) in the new ADR and provider
  help copy.
- **risk R-4 (403 ambiguity):** 403 can mean a bad key or a model not in the
  subscription. Default: one sanitized "credential or entitlement rejected"
  category, with copy that tells the operator to check the key and the plan.
- **risk R-5 (fail-closed config):** a hand-edited malformed v2 file prevents
  server startup, as today. Default: keep fail-closed; the admin UI is the
  safe editor and the CLI reports sanitized errors.
- **backlog B-1:** explicit model-catalog refresh from
  `GET {baseURL}/models` (must remain an explicit admin action).
- **backlog B-2:** record delete/edit UX polish and record import/export.
- **backlog B-3:** per-record `response_format` override and additional
  protocols (`/responses`, `/messages`, Anthropic-style).
- **backlog B-4:** OpenCode Zen record (`https://opencode.ai/zen/v1`), never
  aliased to Go.
- **backlog B-5:** loopback/local-gateway base URLs, persisted probe history
  beyond the last result, and "free/trial" labeling from provider catalogs (to
  be treated as temporary, per ADR-0023).
- **future-logical-whole F-1:** inline media-detail model picker and persistent
  multi-model drafts (ADR-0023, frozen in ROADMAP).
- **future-logical-whole F-2:** Cover Studio / AI cover candidates (ADR-0024).
- **protocol-observation P-1:** none material. The planning grant correctly had
  no NUC, provider-call, or browser authority; the unverified NUC release SHA
  stays an acceptance-time readback concern, not a planning gap.
- **Cooperator questions with defaults:** (1) first vision model —
  `deepseek-v4-flash-vision-exp`; (2) ship catalog refresh now — no, backlog;
  (3) include Zen now — no, one later record; (4) fixture color — red;
  (5) persist the bounded observed color token — yes, allowlisted only;
  (6) Go billing/terms acceptance — Cooperator-owned.

## 17. Budget statement

One initial implementation-planning cycle used. No targeted revision requested.
No implementation, no repository mutation, no `.ap` change, no provider call,
no NUC access, and no Git write occurred. Planning authority expires with this
terminal report; a separate Orchestrator implementation prompt with
`Native planning mode: not-used` is required before any code changes.

---

Changed files: `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/01_report.md`
only, containing this complete report; the FrameNest repository is unchanged.
Validation: repository gate re-observed (HEAD, branch, porcelain, `.ap`
gitlink, `ap doctor` PASS, Alembic `0033`); all plan claims bound to inspected
paths and sections; bounded baseline runtime evidence through the declared AP
`test-focus` route (`180 passed`); report destination verified absent,
non-symlink, inside the granted parent; complete saved content read back before
the separate completion notice. No browser, GUI, or IDE launch.
Git result: no fetch, stage, commit, push, tag, branch, or config operation in
any repository.
Persistence: report saved and fully read back; Meta Git archival remains with
the COOPERATOR; FrameNest Git untouched.
Deviations: none. Risks/limitations: the plan's OpenCode Go facts are dated
public documentation (2026-09-16); live catalog confirmation requires a later
explicit provider-call grant; the NUC release SHA is unknown to this exchange
and is a later readback.
Smallest next step: Orchestrator presents the plan for the single Cooperator
approval decision (whole identity + schema v2 + admin surface), then dispatches
slice 1 as a fresh Implementation Worker grant.

Orchestration critique:
MEASURED: The prompt's recommendation to keep UI inside this whole is
confirmed by repository evidence (ADR-0079 deferred website Settings;
SERVER.md non-goals) and by the Cooperator's stated acceptance target, so no
correction is needed, but the prompt's assumption that existing frontend admin
gating works "in both audiences" is wrong — `identityState.available` is false
for `trusted_loopback` (`app.js:445`) — and the plan corrects it with a
dedicated capability-based helper.
LEAD: The static startup AI resolution (`application.py:619-661,
1627-1642`) means the admin surface cannot take effect without a restart
unless dynamic resolution is implemented; the plan mandates it, but the
Orchestrator should verify the resolved behavior early in slice 3 with a
config-rewrite-then-capability-read test.

Resolved Execution Issues / Near-Misses: none.
Pre-Existing Failure Classification: none.
Authority expiry: this terminal report ends the planning grant; retained
context is not continuing authority; no autonomous continuation.

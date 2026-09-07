# APMC slice 7: diagnostic target registration and guarded runtime seam

Save an administrator-entered OpenAI-compatible endpoint safely, select it for either diagnostic seat, and carry its identity into the existing L4 worker. Keep execution fake, provider calls at zero, and player runtime selection unchanged. One E3 implementation exchange is sufficient; no 7a/7b split is required.

## D1 — Data model and Django admin

**Ownership:** use the `game` app. These objects configure diagnostics and confer no catalog eligibility.

| Model | Exact fields |
|---|---|
| `DiagnosticAllowedHost` | Standard bigint `id`; unique `hostname: CharField(253)`; `is_active: BooleanField(default=True)`; nullable `created_by` user FK with `SET_NULL`; `created_at`, `updated_at`. |
| `DiagnosticTarget` | UUID primary key; `name: CharField(120)`; `base_url: URLField(2048)`; `allowed_host` FK with `PROTECT`; `model_id: CharField(200)`; `credential_env_name: CharField(64)` with closed choices; `is_active: BooleanField(default=True)`; nullable `created_by` user FK with `SET_NULL`; `created_at`, `updated_at`. |
| `PlayerSlot` addition | Nullable `diagnostic_target` FK with `PROTECT`, related name `player_slots`; database check preventing simultaneous non-null `ai_model` and `diagnostic_target`. |

Use `game/0012_diagnostic_targets.py`, dependent on `0011_diagnostic_ply`. Include the additive schema and a reversible seed of the eight default hosts listed in D2. Seeding host rows performs no DNS or HTTP requests.

Omit `last_probe_at`: nothing in this slice probes. Omit `promoted_catalog_id`: there is no promotion operation to reference. Add no price, balance, spend, secret-value, or credential-status persistence fields.

**Preserve history without a new run snapshot schema:**

- Keep `DiagnosticRun` and `DiagnosticPly` schemas unchanged. Existing run seat strings and ply `model_id` retain the selected model ID.
- Once a target is referenced by a slot, freeze its `base_url`, `allowed_host`, `model_id`, and `credential_env_name`. Name and activation status remain editable. A changed connection configuration requires another target.
- Make stored hostnames immutable; permit activation/deactivation. Protected references prevent deletion of hosts or targets in use.
- Serialize target edits and launch attachment using transactions and target row locks, so an edit cannot race the first reference.
- Product services never attach a target. Diagnostic services require exactly one catalog model or target for each diagnostic seat. The database check permits existing human slots with neither.

**Admin CRUD and add-host POST:**

Register both models in `backend/game/admin.py`, using ordinary autoescaped Django admin forms. No `safe`, `mark_safe`, or `format_html` additions.

Use the standard registered endpoint:

`POST /admin/game/diagnosticallowedhost/add/`

This is the explicit add-host operation. Its GET renders a form only. Retain `admin_view` and CSRF protection; require both the host model’s add permission and `has_change_permission`. Apply the equivalent add-plus-change check to target creation, ordinary change permission to edits, and delete permission to deletion. Staff status alone never suffices. Reject unsupported mutation methods.

Add-host validates and stores a canonical hostname only: **no DNS lookup, fetch, probe, or runner launch**. Its form explains that registration permits later target configuration, not successful connectivity.

Target form/model validation enforces D2 and D4. Model `save()` also validates new or changed connection settings and reactivation, covering `objects.create()` and ordinary non-admin saves. Deactivation must remain possible without DNS. A final validation failure writes neither the target nor a successful audit entry and returns an escaped validation response, including when DNS changes between form validation and persistence.

**Minimum launch and FK wiring:**

The current launcher requires both catalog IDs; [`create_diagnostic_game()`](/home/agile/Projects/libretiles/backend/game/services.py:1210) resolves both through the selectable catalog.

- Preserve both existing seat model-ID inputs; add one active-target dropdown beside each. Require exactly one populated choice per seat.
- Add optional `seat0_target_id` and `seat1_target_id` arguments to `create_diagnostic_game`; preserve existing catalog callers.
- For a target seat, set its `PlayerSlot.diagnostic_target`, leave that slot’s `ai_model` null, and derive the run’s seat model string from the target.
- Do not fall back from a target seat to `session.ai_model`.
- Permit mixed target/catalog seats for full-game runs. A position-set run involving targets must select the same target UUID for both seats; otherwise reject launch.
- Retain `generic_unchanged`, selected-only queue, fake runtime, existing caps, and authorship abort.

The slice-6 touches are limited to the launch form, its context/POST validation, and target identity resolution used by existing reports. No comparison or report-template redesign.

## D2 — SSRF controls and threat model

**Default approved hosts**, measured from the shipped compatible transports:

```text
openrouter.ai
integrate.api.nvidia.com
api.groq.com
generativelanguage.googleapis.com
api.cloudflare.com
api.mistral.ai
api.aionlabs.ai
router.huggingface.co
```

All measured bases use HTTPS on implicit port 443. IBM IAM and inference hosts are excluded from diagnostic-target v1.

**One explicit URL policy, implemented in Python and TypeScript:**

- HTTPS only; implicit 443 or explicit `:443`, normalized to implicit 443.
- Exact canonical hostname equality with an active approved-host row; no wildcard, suffix, or substring matching.
- Reject userinfo, IP literals, single-label names, numeric-address aliases, backslashes, control characters, queries, and fragments.
- V1 accepts ordinary ASCII DNS hostnames only. Reject Unicode hostnames and `xn--` labels; IDN support is deferred to avoid divergent Python/WHATWG normalization.
- Lowercase hostnames; reject trailing-dot spelling. Enforce DNS label and hostname length limits.
- Allow an empty base path or slash-separated ASCII segments containing letters, digits, `.`, `_`, `~`, and `-`; reject `.`/`..` segments, percent escapes, and doubled separators. Remove a trailing slash.
- Treat `model_id` as bounded printable model metadata, never as a URL or path component. Reject control characters.

**Save-time insertion point:** target validation in `backend/game/diagnostic_targets.py`, called by the model/admin path.

Resolve the canonical hostname using `socket.getaddrinfo(..., AF_UNSPEC, SOCK_STREAM)`. Require at least one result and reject the hostname if **any** returned address is disallowed. DNS failure, timeout, malformed results, and resolver saturation all refuse the save. Never connect to the target or store resolved addresses as lasting authority.

Bound resolution to two seconds using a module-scoped executor with four workers and bounded admission. A timed-out underlying lookup retains its admission slot until it actually finishes; do not accumulate unbounded queued lookups or threads.

**Request-time insertion point:** a diagnostic-only custom fetch implementation immediately before opening the provider connection.

Repeat URL/hostname validation and fresh all-address DNS resolution for **each** provider request. Check all results before selecting one address. DNS re-resolution alone is insufficient: the actual connection must use the checked address, without a second uncontrolled lookup.

Use a shared, conservative address policy:

| Address family | Refusal policy |
|---|---|
| IPv4 | Refuse `0/8`, `10/8`, `100.64/10`, `127/8`, `169.254/16`, `172.16/12`, `192.0.0/24`, `192.0.2/24`, `192.88.99/24`, `192.168/16`, `198.18/15`, `198.51.100/24`, `203.0.113/24`, `224/4`, and `240/4`. Also refuse Azure platform address `168.63.129.16/32`. |
| IPv6 | Accept only global-unicast `2000::/3`, excluding `2001::/23`, `2001:db8::/32`, `2002::/16`, and `3fff::/20`. Refuse unspecified, loopback, link-local, ULA, multicast, IPv4-mapped, NAT64, and other addresses outside that permitted range. |
| Mixed answers | One disallowed A or AAAA result rejects the entire name, including public-plus-private combinations. |

This explicitly blocks metadata `169.254.169.254`, mapped equivalents, RFC1918, link-local, CGNAT, and transition-address bypasses. Keep Python and TypeScript behavior aligned with shared test vectors rather than relying solely on version-dependent `is_global` classifications.

**Connection implementation:**

The installed SDK accepts a custom fetch implementation. Use Node stdlib `https.request` behind that interface, with a dedicated non-reusing agent and a custom lookup returning only the validated address. Retain the original hostname for Host, SNI, and certificate verification; require certificate verification. Do not use proxy configuration or the ambient/global agent.

This route uses `generateText` and JSON Chat Completions, so v1 needs only a bounded non-streaming provider response adapter:

- Permit POST only to exactly `<canonical base>/chat/completions`.
- Refuse all 3xx responses; never follow `Location`.
- Two-second DNS deadline; ten-second connection deadline; total request lifetime bounded by the remaining existing attempt deadline and its abort signal.
- Maximum request body: 1 MiB. Maximum response body: 2 MiB, enforced while reading, including non-2xx bodies.
- Request identity encoding and refuse compressed responses.
- Preserve bounded status and Retry-After telemetry; discard raw bodies from failure reporting.
- Abort and close resources on refusal, timeout, cancellation, or cap overflow.
- Increment provider-request telemetry only after policy checks, immediately before dispatch.

No new dependency is needed. Ordinary fetch plus a preceding DNS check would not satisfy the connection-binding requirement.

**Threat-Model Fields**

- **Assets:** provider credentials; diagnostic service JWT; internal services and cloud metadata; backend/game integrity; diagnostic attribution; administrative audit records; process resources.
- **Trust boundaries:** staff browser → Django admin/model validation; approved-host registry → stored target; authenticated diagnostic game context → SSE route; route → credential environment; resolver results → actual socket; worker → provider; provider responses → logs and telemetry.
- **Attacker-controlled inputs:** submitted host, URL, model/name fields and env-name selection; forged player POST fields and target IDs; DNS answers that change over time or contain mixed address classes; redirect destinations; response bodies, headers, and error text. Authorized target administrators control endpoint registration; they are not trusted to bypass IP-class restrictions.
- **Security properties:** exact host approval; backend-derived diagnostic authority; closed env-name selection; zero credential values in persistent target data or admin output; checked-address connection binding; no redirects; bounded resource use; fake-mode denial before DNS/socket activity; no player catalog promotion.
- **Abuse cases:** metadata/loopback access; DNS rebinding; IPv6/mapped-address bypasses; suffix and parser confusion; redirect-to-private; selecting `DJANGO_SECRET_KEY`; forged target selection in player games; credential reflection; target changes during launch; oversized/slow responses; attribution collisions between endpoints sharing a model ID.

All security tests use mocked resolvers and transport. No real metadata, provider, or DNS request is part of implementation validation.

## D3 — One-route runtime seam and L4 wiring

**Authority source:** extend the existing authenticated `get_ai_context()` response only for an acting target seat. Do not introduce another backend target-fetch API.

Return a `diagnostic_runtime` object containing:

```text
kind: diagnostic-openai-compatible
run_id, game_id, acting_slot
target_id, model_id, base_url, allowed_hostname, credential_env_name
executed_runtime_mode: fake
```

Before returning it, require the managed diagnostic service identity, membership in the diagnostic session, its server-derived acting seat, a queued/running run, and active target/host records. Ordinary game contexts contain no such object. Invalid diagnostic context fails closed.

Use `diagnostic-target/<UUID>` as the diagnostic provider identity in observations and report identity resolution. It is not a provider-registry entry. Keeping target UUID in that identity prevents two endpoints with identical model IDs from being conflated.

**Worker and request interfaces:**

- Runner JSONL adds only `diagnostic_target_id` to existing game/seat/model identity fields. Do not send URL, env name, or credential value through IPC.
- `diagnostic-worker.mjs` passes that ID to `runDiagnosticTurn`.
- `runDiagnosticTurn` adds the optional ID to its locally constructed POST body. A target uses exactly one selected-only attempt and bypasses catalog queue construction.
- The route treats the client ID only as a selection assertion. It must match the target authorized by the authenticated backend context.
- Reject body-supplied URL, env-name, or diagnostic-runtime configuration. A missing/mismatched target assertion must never produce catalog fallback or an `ai-model` PATCH for a target seat.

**Exact runtime insertion point:**

The current route constructs its model here:

```text
const runtime = await getLanguageRuntime(
  runtimePair.provider,
  runtimePair.model_id,
);
```

Introduce a diagnostic sibling, `getDiagnosticLanguageRuntime`, at this construction boundary. For an asserted target, obtain and validate diagnostic context before catalog resolution; normal player requests retain their existing catalog flow.

The diagnostic branch supplies the same `{model, tracker}` result and then rejoins the existing prompt composition, tool definitions, generation, repair, validation, and terminal handling. Diagnostic authorization/policy refusals terminate explicitly before generation, without falling into a rescue or catalog-selection path.

Keep `getLanguageRuntime`, `isValidRuntimePair`, and `revalidateRuntimePair` unchanged.

**Constructor reuse:**

In `openai-compatible.ts`, keep `createTrackedOpenAIChatModel` private. Add an optional custom-fetch input and a narrow exported `getDiagnosticOpenAICompatibleModel` wrapper for the validated diagnostic descriptor. Existing shipped callers continue using the existing tracked fetch.

`diagnostic-target-runtime.ts` owns descriptor validation, diagnostic guard authorization, the tracker, and selected credential lookup. It passes the guarded custom fetch to that wrapper. The diagnostic wrapper never uses `inferProviderFromInput` as authorization.

**Guard integration:**

Add `diagnostic-egress.ts` to hold the active diagnostic transport policy. `installFetchGuard` installs/restores this policy alongside its existing global-fetch wrapper.

The socket adapter must consult this policy explicitly because `https.request` does not pass through global fetch:

- No installed diagnostic policy: deny.
- Installed fake policy: deny before credential lookup, DNS, or socket creation.
- Live policy: require the exact origin in its approved set, then apply D2.

The production L4 worker continues installing `{mode: "fake"}` and adds no target origins. The current `providerOrigins` option is the future seam for a verified target origin; activating it for L4 belongs to a later live grant.

Keep the default `generic_unchanged` early return intact. Exercise the new route branch with synthetic factory/transport mocks; do not claim that an ordinary fake admin run traversed it.

**Every runner/report touch:**

- Both instrument loops: replace catalog-only seat identity checks/command construction with a catalog-or-target identity helper.
- `_build_record`: derive the target model ID instead of writing an empty model ID.
- `_position_pair_identity`: resolve target UUID identity and reject mixed identities.
- Preserve `_model_position_samples`, report construction, caps, cancellation, minting, terminal vocabulary, and authorship behavior.

No MOVE CORE changes, no `MOVE_PROMPT_VERSION` bump, and no second SSE route.

## D4 — Credential names, redaction, and audit

Export the existing `CREDENTIAL_ENV_NAMES` from `provider-logging.ts`. Do not extend it in this cut. The exact selectable set is:

```text
GROQ_API_KEY
GEMINI_API_KEY
MISTRAL_API_KEY
AION_API_KEY
HF_TOKEN
CLOUDFLARE_ACCOUNT_ID
CLOUDFLARE_API_TOKEN
OPENROUTER_API_KEY
NVIDIA_API_KEY
IBM_CLOUD_API_KEY
IBM_WATSONX_PROJECT_ID
IBM_WATSONX_REGION
```

Mirror it in the backend helper and add an exact-set parity test. Enforce membership both at save and at diagnostic runtime construction. A future extension must update the canonical redaction list, backend choices, and parity tests in the same change.

Membership does not imply that an identifier is a usable bearer credential or that IBM transport is supported.

**Presentation and handling:**

- Render the variable name and `credential present: yes|no|unknown`; never render a value.
- Distinguish process scope. Django can report key membership in its own environment without reading the value; Next/L4 presence is `unknown` unless actually observed in that process. Fake L4 forwarding reports `no`.
- Presence is not authentication or placeholder validation.
- Do not read another process’s env file to improve the display.
- Keep descriptor URL/env-name data out of IPC, SSE telemetry, `parameters_json`, ply rows, and reports. The existing parameter redactor rejects `env` keys; do not weaken it.
- Use existing sanitized provider-failure records. Diagnostic socket/policy failures emit fixed reason text, status, and target identity, not raw URL, headers, bodies, or transport exception messages.
- Test reflected synthetic credentials, including short values, against admin responses, audit messages, SSE, IPC, and logs. Never rely solely on entropy matching for diagnostic transport errors.

Use Django `LogEntry` for target/host creation, change, activation, deactivation, and deletion. Store actor, object identity, and changed field names. Successful custom handling must preserve standard audit behavior. Do not add a parallel audit model or store credential values in change messages.

**Worker environment:** leave `_worker_env_whitelist` unchanged. It forwards no provider credentials. Tests may inject dummy credentials only into isolated mocked runtime tests; no dummy is needed in the ordinary fake worker.

A later live grant may forward only the credential name selected for the authorized target, after closed-list validation, or the existing selected catalog provider’s required names. Never forward the whole list, Django secrets, `LIVE_SENTINEL`, AppImage variables, or an ambient environment copy.

## D5 — Implementation allowlist, fail-before evidence, and tier

**Exact mutation allowlist for the following implementation grant:**

Backend implementation:

```text
backend/game/models.py
backend/game/diagnostic_targets.py                         [new]
backend/game/admin.py
backend/game/services.py
backend/game/management/commands/run_diagnostic_match.py
backend/game/migrations/0012_diagnostic_targets.py          [new]
backend/game/templates/admin/game/diagnosticrun/launch.html
```

Frontend implementation:

```text
frontend/src/lib/diagnostic-target-runtime.ts               [new]
frontend/src/lib/diagnostic-target-fetch.ts                 [new]
frontend/src/lib/diagnostic-egress.ts                       [new]
frontend/src/lib/openai-compatible.ts
frontend/src/lib/provider-logging.ts
frontend/src/lib/ai-play-diagnostic.ts
frontend/scripts/diagnostic-worker.mjs
frontend/src/app/api/ai/move/route.ts
```

Tests and fixture:

```text
backend/tests/test_diagnostic_targets.py                    [new]
backend/tests/test_diagnostic_admin.py
backend/tests/test_diagnostic_session.py
backend/tests/test_diagnostic_runner.py
backend/tests/fixtures/diagnostic_ssrf_cases.json            [new]
frontend/src/lib/diagnostic-target-runtime.test.ts          [new]
frontend/src/lib/diagnostic-target-fetch.test.ts            [new]
frontend/src/lib/openai-compatible.test.ts
frontend/src/lib/provider-logging.test.ts
frontend/src/lib/ai-play-diagnostic.test.ts
frontend/src/lib/ai-play-diagnostic.worker.test.ts
frontend/src/app/api/ai/move/route.test.ts
```

Documentation:

```text
AGENTS.md
frontend/.env.local.example
```

Clarify that player bases remain hardcoded with no base-URL env variables, while diagnostic bases are separately registered in Django admin. Add no base-URL environment setting.

**Fail-before table:** these are required future tests, not executed results from this planning session. Tests for absent interfaces fail on this baseline because the capability does not exist; that is not evidence that an existing admin endpoint currently saves unsafe URLs.

| ID | Required assertion | Expected failure at current HEAD |
|---|---|---|
| S7-F01 | Target/host schema exists; approved target can be saved with mocked public DNS and no HTTP. | Models/migration absent. |
| S7-F02 | Save rejects loopback, metadata, mixed A/AAAA, mapped addresses, malformed URLs, and DNS timeout. | Target save validator absent. |
| S7-F03 | Add-host is audited, permission/CSRF protected, and performs no DNS/HTTP. | Host registration surface absent. |
| S7-F04 | Unlisted env name, including `DJANGO_SECRET_KEY`, is rejected in both languages; names match redaction set. | Closed target-selection interfaces absent. |
| S7-F05 | Either diagnostic seat accepts a target without an `AIModel` row; invalid dual selection fails. | Launcher/services require catalog models. |
| S7-F06 | Forged player target configuration is refused; authenticated target context selects the sibling runtime without catalog PATCH/fallback. | Target assertion is ignored and sibling runtime absent. |
| S7-F07 | Public-at-save/private-at-request and mixed DNS answers refuse before transport. | No diagnostic request validator; generic fetch has no such gate. |
| S7-F08 | The socket uses the validated IP; redirects, oversized bodies, compression, and timeout refuse. | Bound diagnostic adapter absent. |
| S7-F09 | Fake/default-deny policies stop the socket adapter before credential lookup, DNS, or socket creation. | No adapter-aware diagnostic guard exists. |
| S7-F10 | Target identity survives IPC/ply/report wiring without URL, env name, or credential material. | Runner/report identity is catalog-only. |
| S7-F11 | Used target connection settings are immutable; deactivation remains available; audit contains no values. | Target lifecycle absent. |

Each security-negative family must have a permitted synthetic control. Produce red-before evidence on the baseline and green-after evidence without weakening existing tests. Keep already-passing freezes separate from the fail-before list.

**Required validation in the implementation grant:**

- Focused backend target/admin/session/runner tests; migration forward/reverse on a disposable test database; `makemigrations --check --dry-run`.
- Backend Ruff and mypy through the declared sanitized `.venv/bin/python` route. No ambient Python/Poetry route and no dotenv-disabling workaround.
- Focused Vitest for the new modules plus affected runtime, logging, worker, and route tests.
- Regression coverage for `ai-runtimes`, provider registry/catalog, prompts, and the 300-turn simulation.
- `npm run lint` and `npm run typecheck`.
- Plain-Node worker import/fake JSONL smoke with no provider credentials and no network.
- Verify frozen prompt bytes, player selectors, six completion sources, env whitelist, and fake comparison exclusion.

**`npm run build`: no.** This design changes an existing Node route and server helpers without modifying Next configuration, dependencies, client imports, layouts, or route exports. Focused route tests, typechecking, lint, and plain-Node import coverage are the gates selected here.

**Tier and sequence:** the complete change is E3. Schema, credential-name policy, and outbound-target seam form one security boundary; there is no E4 secrets-in-DB component and no required tier spread. Implement backend validation first, the guarded transport second, then wire launch and runtime selection, within one bounded exchange.

**Independent 7-IA: mandatory**, after landing, by a fresh Worker who neither implemented nor materially corrected this boundary, under INFOSEC 4.6.

**Publication authority for that later grant:** work on `main`; stage only enumerated paths; commit and push explicitly to `origin main` after validation. No new branch and no force push. That grant must explicitly authorize the Git network operation; this report authorizes none.

**Negative authority:** no gamecore edits; no game migrations 0009–0011 edits; no mint redesign; no `DiagnosticPly` redesign; no `_model_position_samples` fill replacement; no reopening accepted S5 residuals or slice-6 XSS work; no slice-8 probe/history/sorting/ping-pong; no K1/live NIM; no player-catalog promotion; no secrets in DB; no dependency or lockfile changes; no `.ap` edits.

For rollback, deactivate target/host rows first. Before reverting the schema, refuse reversal while target-linked diagnostic slots exist; do not silently erase their identity.

## D6 — Boundaries

**Why K1 is unnecessary:** slice 7 proves registration, authorization, secret-name containment, request refusal, and structural routing with mocks. It does not claim that a provider accepts the endpoint, honors tool calling, or produces strong moves. Fake runs retain their existing measurement limitations, so no live NIM evidence is needed to accept this cut.

**Why ping-pong is excluded:** animation, probe history, and ordering have no role in validating a stored destination or restricting a socket. They remain slice 8. The only existing presentation change is target selection in the launch form and ordinary admin CRUD.

**Why player dispatch cannot learn the URL:** `getLanguageRuntime` currently validates the provider/model pair before reading provider configuration. Allowing it to accept target URLs would bypass the diagnostic promotion boundary and expose administrator-controlled endpoints to player traffic. The sibling factory is reachable only through backend-authorized diagnostic context and a diagnostic transport policy.

**What a later live grant must add:** explicit selected-credential forwarding; exact target-origin admission to the L4 live fetch guard; backend-authorized live execution state; measured transport/tool compatibility; the separately authorized 3b fill replacement; and instrument subcap evidence. It must also assess credential-to-host delegation before enabling outbound authorization headers. None is implied by `is_active`, successful registration, or this plan.

## D7 — Orchestration critique

- **MEASURED:** the supplied baseline and AP gitlink match, with clean porcelain before and after inspection. No baseline adaptation was needed.

- **MEASURED:** [`createTrackedOpenAIChatModel`](/home/agile/Projects/libretiles/frontend/src/lib/openai-compatible.ts:321) is private. Era-01’s seam description therefore requires a small wrapper/input change; it is not an already-callable public seam.

- **MEASURED:** [`createTrackedProviderFetch`](/home/agile/Projects/libretiles/frontend/src/lib/openai-compatible.ts:287) dispatches even when provider inference returns `"unknown"`. Its hostname substring checks are logging heuristics, not SSRF authorization. The new branch must not reinterpret them as a host allowlist.

- **MEASURED:** the default diagnostic guard lists two provider origins, while shipped compatible transports cover eight hostnames. The default host registry and the L4 live-origin grant are distinct sets; seeding the former must not broaden the latter.

- **MEASURED:** [`_worker_env_whitelist`](/home/agile/Projects/libretiles/backend/game/management/commands/run_diagnostic_match.py:103) forwards zero provider keys. `spawn_diagnostic_runner` separately inherits the Django environment minus AppImage names. Those are different process boundaries; the parent launcher’s behavior does not justify changing the Node whitelist.

- **MEASURED:** [`generic_unchanged`](/home/agile/Projects/libretiles/frontend/src/lib/ai-play-diagnostic.ts:410) returns before catalog fetch, reconciliation, or SSE POST. Consequently, “launch succeeded in fake mode” cannot establish that the target route seam or SSRF transport ran.

- **MEASURED:** the required wiring extends beyond the initially enumerated admin/runtime files. Both runner instrument loops, `_build_record`, [`get_ai_context`](/home/agile/Projects/libretiles/backend/game/services.py:2052), and `_position_pair_identity` assume catalog-backed seats. The allowlist includes only the identity changes needed there; the 3b fill remains frozen.

- **MEASURED:** the current redaction list contains account/project/region identifiers as well as API keys. Closed-list membership is not proof of usable bearer authentication, and the old diagnostic helper’s two-provider mapping is not the full redaction list.

- **MEASURED:** Django has Security, CSRF, XFrameOptions, and Axes middleware but no Django CSP. The Next proxy CSP does not protect `/admin/`; this design relies on permissions, CSRF, and escaping rather than claiming CSP coverage.

- **LEAD:** the locked host-approval policy makes “type a URL” a two-step workflow for a new hostname: register host, then save target. This fits the no-SSH URL goal, but the admin copy must make the sequence explicit.

- **LEAD:** fresh DNS validation followed by ordinary fetch would leave a time-of-check/time-of-use gap. The bound stdlib transport is necessary implementation work, not optional hardening.

- **LEAD:** a user authorized to add a public host and select an existing provider key could later direct that key to the host. SSRF filtering and redaction do not prevent that delegation. This cut’s fake/default-deny transport prevents transmission; a later live grant and 7-IA must address the delegation explicitly.

- **LEAD:** the full era-01 artifact was not supplied or found in the inspected project documentation. Comparisons here use its binding D8/D12 intent quoted in this prompt; no additional historical decisions are asserted.

No unsafe lock was silently replaced, no product decision was reopened, and no independent certification is claimed.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: IMPLEMENT-DECLARATIVE-PROVIDER-RECORDS-SLICE-1
status: PARTIAL
Phase-qualified result: not-applicable
Start commit: 33946e08447dc92621ed6844b4b5d13a19ec29f1
End commit: f41df797d74ddd0a54c6c0d31f995bda8a8a4661
Report justification: new-mutation
Logical-whole closure: not-closed

Repository gate (independently re-observed 2026-09-16, read-only): physical root
`/home/agile/Projects/framenest`; canonical remote
`https://github.com/cisarik/framenest.git`; branch `feat/x-meme-browser-companion`;
HEAD equal to the exact authorized baseline `33946e08447dc92621ed6844b4b5d13a19ec29f1`;
porcelain clean before the first edit; `.ap` gitlink == `.ap` HEAD ==
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8`; `./.ap/ap doctor` PASS (stable variant,
managed block OK); `ap project check --baseline 33946e08447dc92621ed6844b4b5d13a19ec29f1`
PASS; `runtime-info` provenance resolved under
`/home/agile/Projects/framenest/src/framenest/__init__.py`; no foreign worktree and no
active mutation observed. Pre-change focused baseline: `239 passed`. All gates
classified per RF-12 with no difference to repair.

## 1. Coordinates

Echoed exactly once in the header block above.

## 2. Status

PARTIAL. All 17 allowlisted paths were produced, validated, and committed; one
binding sentence of D5 ("declared ids are valid in the environment override")
is satisfied only at the `registry.py` boundary, not end-to-end, because the
app-level settings validator that consumes `FRAMENEST_AI_PROVIDER_ID` lives in a
file outside the allowlist. Exact limitation in section 8; nothing else is
outstanding.

## 3. Phase-qualified result

not-applicable

## 4. Start and end commit

- Baseline (unchanged, canonical): `33946e08447dc92621ed6844b4b5d13a19ec29f1`
- Local candidate commit: `f41df797d74ddd0a54c6c0d31f995bda8a8a4661`

## 5. Changed files and purpose (exact allowlisted paths only)

Source:

- `src/framenest/infrastructure/ai/provider_records.py` (new) — `AiProviderModel`,
  `AiProviderRecord`, declared protocol constant, capability allowlist, provider id /
  model id / display name / credential-env-name / base-URL validators, secret-shape
  defense, declared-provider map parsing with bounds (16 providers, 64 models each),
  serialization, and code-defined built-in records (`nvidia-nim`,
  `vercel-ai-gateway`); one-way import direction `provider_records` <-
  `configuration` <- `registry` preserved.
- `src/framenest/infrastructure/ai/configuration.py` — `AI_CONFIG_SCHEMA_VERSION = 2`;
  read accepts 1 and 2, writers always write 2; v1 read yields an in-memory v2 config
  with `providers = {}` and nothing invented; unknown record/model keys rejected;
  declared active without selection rejected; selections limited to built-in or
  declared ids; 64 KiB file bound; `AiServerConfig.providers`; existing atomic/0600/
  symlink/`os.replace` behavior retained; bounded-identifier delegation for
  `validate_provider_id` / `validate_model_id`.
- `src/framenest/infrastructure/ai/constants.py` — added `BUILTIN_PROVIDER_IDS` and
  `SHARED_USER_AGENT = "framenest/0.1"`; all pre-existing constants unchanged.
- `src/framenest/infrastructure/ai/credentials.py` — added
  `GenericAiProviderCredential` (redacted repr) and
  `load_ai_credential(environment_name, environ=None)` with env-first, exact-name
  `CREDENTIALS_DIRECTORY` fallback, 4096-byte bound, existing symlink/regular/UTF-8/
  NUL/multiline checks; existing NVIDIA and Vercel loaders, messages, and behavior
  unchanged.
- `src/framenest/infrastructure/ai/registry.py` — one `AiProviderDefinition` type for
  built-ins and declared records; `PROVIDER_DEFINITIONS` retained as the built-ins map
  and `provider_definitions(config)` added; precedence unchanged (environment ->
  persisted v2 -> legacy NVIDIA -> unconfigured); declared resolution and
  environment-override handling for declared ids; `ResolvedAiProvider` gained
  `protocol`, `base_url`, `provider_source`, `models`, and `capabilities_for`;
  NVIDIA construction unchanged, OpenAI-compatible construction via the generic
  adapter; Vercel built-in now uses the generic path.
- `src/framenest/infrastructure/ai/openai_chat_completions.py` (new) — parameterized
  `build_chat_completions_suggestion_body` (one to three JPEG data URLs,
  `response_format` suggestions only) and `build_chat_completions_connection_test_body`;
  `OpenAiChatCompletionsMediaSuggestionProvider(credential, *, base_url, provider_id,
  model_id, transport=None, image_encoder=None)` with `suggest`, `test_connection`,
  redacted repr; request URL `base_url + "/chat/completions"`; one call per invocation,
  no retries, 120 s timeout, 24 MiB request / 1 MiB response bounds, static
  `User-Agent: framenest/0.1`, and the exact current Vercel error mapping including
  `403 -> authentication/entitlement` (never "invalid response").
- `src/framenest/infrastructure/ai/vercel_gateway.py` — now a thin
  subclass/delegation over the generic implementation; module path, class name,
  constructor signature, constants, and behavior preserved.
- `src/framenest/adapters/cli/ai.py` — new `provider add/list/remove` subcommands
  (built-in refusal, upsert-with-explicit-output for declared ids, active-removal
  refusal, sanitized outputs); `configure` menu is built-ins plus declared records with
  declared-model validation; `status` gained `Provider source: builtin|declared|none`;
  `test` unchanged and works for declared providers; `still-frame-smoke` untouched;
  exit codes 0/2 (configure cancel keeps 1).

Deploy source material (repository only):

- `deploy/systemd/framenest-ai-credential-opencode-go.conf` (new) — exact two-line
  `[Service]` + `LoadCredential=OPENCODE_API_KEY:/etc/framenest/credentials/OPENCODE_API_KEY`
  contract.
- `deploy/ubuntu/production_ai_deploy.py` — `opencode-go` credential and drop-in
  template mappings, plus `OPENCODE_API_KEY` support in the local `--local-ai-env`
  extraction switch (needed for the new provider to be usable through that path).
  No helper was run, no credential installed, no NUC contact, no service action.

Tests:

- `tests/unit/infrastructure/ai/test_provider_records.py` (new)
- `tests/unit/infrastructure/ai/test_ai_configuration_storage.py`
- `tests/unit/infrastructure/ai/test_registry.py`
- `tests/unit/infrastructure/ai/test_openai_chat_completions.py` (new)
- `tests/unit/adapters/cli/test_ai_cli.py`
- `tests/contract/test_production_ai_deployment.py`
- `tests/contract/test_ai_server_composition.py`

## 6. Tests and validation

Exact AP route command (final candidate, post-commit re-run):

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 33946e08447dc92621ed6844b4b5d13a19ec29f1 --operation test-focus -- tests/unit/infrastructure/ai tests/unit/adapters/cli/test_ai_cli.py tests/contract/test_ai_server_composition.py tests/contract/test_production_ai_deployment.py tests/contract/test_automatic_analysis_settings_api.py -q -p no:cacheprovider
```

Result: `375 passed in 5.91s` (0 failed, 0 skipped), run once before the commit and
once again on the committed final candidate. Pre-change baseline on the identical
selection was `239 passed`.

Additional affected-consumer regression run on the final candidate (same declared
route): `tests/contract/test_media_suggestion_api.py`,
`tests/contract/test_public_published_uds.py`, `tests/unit/test_configuration.py`
-> `79 passed` (1 pre-existing pydantic JSON-schema warning). A combined run of the
focused selection plus those three files produced `425 passed`.

`tests/unit/infrastructure/ai/test_vercel_gateway.py` and
`tests/unit/infrastructure/ai/test_credentials.py` were NOT modified and passed
inside the focused selection; `test_vercel_gateway.py` is green unmodified.

Coverage added by the slice: record validation bounds, full URL policy table,
credential-env name pattern and reserved names, capability allowlist, built-in id
collision, secret-shape rejection, proof that `credential_env` is a name; v2 exact-key
round trip, v1 -> v2 read compatibility without invention, unknown-key rejection,
declared-active-without-selection, 0600, name-aware no-secret assertions, declared
ids accepted by test-state/status validators; declared resolution/model
selection/capability lookup/missing credential/environment override/legacy NVIDIA;
generic adapter bodies, data-URL framing, URL joining, 403/401 -> auth, 429, 404,
5xx, other-4xx, bad JSON, bounds, no secret in headers/body, one call per
invocation; CLI record management, configure selection, status source line, declared
`test` with a synthetic credential; third deploy credential/template mapping and
tracked bytes; startup resolution of a declared provider with
`credential_unavailable` and no fabricated fallback.

Final diff inspection: `git diff --stat` and the full committed diff were inspected;
`git status --porcelain` is empty after the commit; no secret, key shape,
Authorization header value, base64 payload, home path, or database path appears in
the changed files.

## 7. Commit result

Exactly one local commit on `feat/x-meme-browser-companion`:

```text
f41df797d74ddd0a54c6c0d31f995bda8a8a4661 Add declarative provider records and generic OpenAI-compatible adapter
```

Staging was path-exact (no `git add .`, no wildcard). No push, no fetch, no branch,
tag, merge, rebase, reset, clean, checkout, stash, or config operation; only read-only
`git status/log/diff/show/rev-parse` and the single `git add`/`git commit`.
The local commit is not canonical; the AP `--baseline` remained the authorized
baseline above.

## 8. Deviations, risks, or missing evidence

1. **D5 environment override is registry-level only (the single reason for
   PARTIAL).** `registry.resolve_ai_provider` fully implements declared ids in the
   override and is unit-tested, but the app-level `FrameNestSettings` validator that
   consumes `FRAMENEST_AI_PROVIDER_ID` still enforces the hardcoded two-id set at
   `src/framenest/configuration.py:53` and `src/framenest/configuration.py:372-380`.
   A raw `FRAMENEST_AI_PROVIDER_ID=opencode-go` therefore fails at settings
   construction (pydantic `ValidationError`) before the registry runs, and the CLI
   `_resolve` catches only `FrameNestConfigurationError`, so that path surfaces as an
   unhandled validation error. `src/framenest/configuration.py` is outside the exact
   changed-path allowlist, so the end-to-end behavior could not be completed or
   tested within this grant. The authenticated persisted-v2 path (server startup,
   CLI record management, CLI configure, registry resolution) is complete, tested,
   and unaffected; slice-1 acceptance does not depend on the env override.
2. **Override test construction.** Because the settings constructor rejects the
   declared id, the "environment override to a declared provider" unit test builds
   the settings object with `FrameNestSettings.model_copy(update=...)`, following the
   existing repository precedent (`tests/contract/test_youtube_cli.py:230`). This is
   honest registry-level evidence, not end-to-end environment evidence.
3. **Stricter `provider remove` confirmation.** The D7 syntax lists `--yes`; removal
   without it is refused with a sanitized exit 2 (same posture as `provider add`).
4. **Vercel built-in now constructs the generic adapter class** (per D5 "Vercel via
   the generic path"); the Vercel-specific class and module remain for existing
   imports and its unit tests. No behavioral difference was observed.
5. **Provider facts remain declarations.** No provider/network call of any kind was
   made; OpenCode Go base URL, model id, and credential name are repository-declared
   data validated by policy only.

Missing evidence: none for the allowlisted surface. The only missing evidence is the
out-of-allowlist end-to-end environment override noted above.

## 9. Smallest next step / review request

Orchestrator decision on the single deviation: either (a) accept registry-level
override semantics for slice 1 and carry the settings-validator widening into
slice 3 (where `configuration_source: environment` becomes operator-visible), or
(b) issue one smallest correction grant that adds `src/framenest/configuration.py`
to the allowlist and replaces the `SUPPORTED_AI_PROVIDER_IDS` enum check on
`ai_provider_id` with the bounded identifier rule (with a settings-level test).

## 10. Report justification

Report justification: new-mutation

## 11. Authority expiry

This terminal report, cancellation, or supersession ends the entire implementation
grant; retained context is not continuing authority; no autonomous continuation.
The local commit awaits Orchestrator reconciliation and later acceptance.

## 12. Orchestration critique

```text
Orchestration critique:
MEASURED: The slice-1 allowlist omits `src/framenest/configuration.py`, whose `FrameNestSettings.ai_provider_id` validator (lines 53 and 372-380) still enforces the retired two-provider enum, so D5's "declared ids are valid in the environment override" cannot hold end-to-end from this grant; the registry-level contract is implemented and green. Effect: status PARTIAL for one upstream sentence. Smallest correction: one bounded successor grant adding that file and delegating the validator to the bounded identifier rule.
LEAD: The plan may have intended the override only as registry precedence for persisted-config-era slices; cheapest check: after the correction, run `FRAMENEST_AI_PROVIDER_ID=<declared-id> ./.venv/bin/framenest-ai status` in a clean human shell or exercise it through a settings-level unit test.
```

## 13. Resolved Execution Issues / Near-Misses and Pre-Existing Failure Classification

Resolved Execution Issues / Near-Misses: none.

Pre-Existing Failure Classification: none. (The pre-change focused selection was
green at the baseline; no failure was carried into this slice.)

## Validation, persistence, and hygiene

Validation ladder applied: inspection and provenance required (repository gate,
`ap project check`, `runtime-info`), existing focused suites (the named unit suites),
affected tests (the declared selection), and new causal regression (the new/edited
tests). Broad/full suite, runtime testbed, and independent acceptance were not used
per the selected ladder. The pre-change baseline run and the post-change run used the
same declared route; no ambient interpreter, `python`, `poetry run`, or `pip`
invocation occurred; no environment reconstruction; no Node/browser/GUI/NUC/SSH/
sudo/network action; no secret access.

Changed files: only the 17 exact allowlisted paths listed in section 5.

Git result: one local commit `f41df797d74ddd0a54c6c0d31f995bda8a8a4661`; no push; no
other Git write.

Persistence: this report was saved to the exact granted destination
`/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report.md`
after verifying the parent path, symlink resolution, and destination absence; the
complete saved content was read back before the separate completion notice. Meta Git
archival remains with the COOPERATOR; no Meta Git operation was performed.

Risks/limitations: the deviation in section 8 (environment override at the app
settings boundary); all other slice-1 claims are bound to committed code and passing
tests. No provider, NUC, deployment, or production evidence is claimed.

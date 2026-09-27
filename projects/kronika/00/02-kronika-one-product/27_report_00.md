### Report for ORCHESTRATOR_CHAT

Logical whole identity: kronika-one-product
Worker session ordinal: 27
Worker exchange ordinal: 01

Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S4-A-RESEARCH-CONTRACTS
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 72009c3b525b6a46e87223cb9a143b5079d89cbf
End commit: 75e9b07b2bf2269568382e28d40a8d2ff8d4bc28
Report justification: new-mutation
Logical-whole closure: not-closed

Step 0 matched the issued baseline. Physical root `/home/agile/Projects/framenest`, branch `feat/kronika-one-product`, HEAD `72009c3b525b6a46e87223cb9a143b5079d89cbf`, parent `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`, tree `ba4b9290f0c986ac9cec6c3acec49ba747bf9b70`, clean index and worktree. Local `main`, `origin/main`, and `git ls-remote` `refs/heads/main` were `fd277a9a64a6965df76127dbec5b1735d2fb3cdd`. AP gitlink and `.ap` HEAD were `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. `AI_CONFIG_SCHEMA_VERSION` was 2. No research module existed. No RF-12 remainder.

Changed files, baseline to HEAD, exactly the allowlist:

| Path | Purpose |
|---|---|
| `src/framenest/domain/research.py` | Pure lifecycle, descriptor, request, observation, usage, and typed-error values |
| `src/framenest/application/ports/research.py` | Provider, request repository, budget ledger, and atomic completion protocols |
| `src/framenest/infrastructure/ai/research_registry.py` | Static descriptors and server-side selection snapshot |
| `src/framenest/infrastructure/ai/research_configuration.py` | Non-secret research section parser and defaults |
| `src/framenest/infrastructure/ai/configuration.py` | Schema version 3 with v1/v2 reads preserved |
| `tests/unit/infrastructure/ai/test_ai_configuration_storage.py` | Version-3 storage, compatibility, and rejection tests |
| `tests/unit/infrastructure/ai/test_research_registry.py` | Descriptor, parked, unknown, snapshot, and no-fallback tests |
| `tests/contract/test_research_provider_contract.py` | Fake provider, ports, error codes, and import boundaries |

Domain values cover operation kinds `search` and `research`; lifecycle states `admitted`, `submitting`, `running`, `validating`, `saved`, `refused`, `failed`, `incomplete`, `cancel_requested`, `cancelled`, `timeout`, and `submission_unknown`, partitioned into non-terminal and terminal sets; separate remote-cleanup states `not_required`, `pending`, `deleted`, `failed`, `unknown` and accounting states `reserved`, `reconciled`, `unknown`. `ProviderDescriptor` carries provider id, adapter version `0`, configuration version `3`, search/research capabilities, execution location, native-research support, cancellation, retrieval, remote deletion, retention posture, accounting capabilities, submission idempotency including `not_guaranteed`, and availability. `ProviderRequest` carries a bounded prompt, operation kind, opaque operation id, server-selected profile, deadline, and approved resource limits. It has no owner and no endpoint, model, or tool input. `ProviderObservation` covers pending, running, complete, refused, failed, cancelled, and uncertain. A complete result carries answer text, citations, completion evidence, usage, and an opaque handle, and has no HTML field. Usage cost uses integer micro-USD arithmetic: cached input is not billed twice, reasoning tokens are not added again, and unknown accounting rejects a stored zero. The 22 sanitized error codes match the accepted plan. No error value has a raw provider message.

Ports are `ResearchProvider.describe/submit/poll/cancel/release_remote`, `ResearchRequestRepository.get/admit/save`, `ResearchBudgetLedger.reserve/reconcile`, and `ResearchResultCompletion.complete`. They import only `framenest.domain.research`.

The registry exposes `openai-responses` as unconfigured, with search and research capabilities and `not_guaranteed` idempotency, and `chatgpt-page` as parked and unavailable for new work. `self-hosted` is a documented extension constant and is not selectable. There is no plugin import and no fallback. Selection copies provider, model, profile, and limits into a frozen snapshot. `live_ready` is false. Configuration is not treated as live readiness. The deterministic fake provider exists only in the contract test.

`AI_CONFIG_SCHEMA_VERSION` is 3 and accepted versions are `{1, 2, 3}`. Non-integer versions, including `999`, `4`, `"3"`, `true`, and `3.0`, stay rejected. An absent `research` section loads as `None` (disabled). A present section stores only non-secret fields: enabled default false, provider id `openai-responses`, fixed model `gpt-5.5-2026-04-23`, reasoning effort, `web_search` allowlist, tool-call and output-token ceilings, background, deadlines, per-operation micro-USD reservations, daily and monthly ceilings, prompt/response/answer/citation bounds, connect/HTTP/poll timeouts, and credential identifier `KRONIKA_RESEARCH_OPENAI_API_KEY`. Unknown fields, secret-shaped fields, an endpoint field, and out-of-range values are rejected. The rejection text does not echo the submitted secret. Saving writes version 3. When research is absent, the research key is omitted and media provider selection plus provider records are preserved.

Compatibility evidence: a version-1 read does not rewrite the file, does not invent providers, leaves research disabled, and a later save writes version 3 with the same media selection and an empty provider map. A version-2 declared file is unchanged by reading; provider id, model map, and provider record survive; research stays disabled; the save writes version 3 with those media fields and no research key. The previous exact-key media round trip now expects schema 3 and still checks the same media keys and the absence of secret material. Existing malformed-provider assertions remain.

Validation, declared route, final run after the whitespace correction below:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 72009c3b525b6a46e87223cb9a143b5079d89cbf
```

Result: `ap project check --baseline: PASS`.

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 72009c3b525b6a46e87223cb9a143b5079d89cbf --operation test-focus -- tests/unit/infrastructure/ai tests/unit/test_import_boundaries.py tests/contract/test_ai_server_composition.py tests/contract/test_ai_provider_admin_api.py tests/contract/test_research_provider_contract.py -q -p no:cacheprovider
```

Result: 399 passed, exit 0, 9.66s. No JavaScript route. No ambient Python route.

Commit: `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28`. Parent: `72009c3b525b6a46e87223cb9a143b5079d89cbf`. Tree: `9f52d90790e4c1d0b37a6594d9c13071fa94a007`. Subject: `feat(kronika): add provider-neutral research contracts and configuration`. Eight files, +2184/−9. Post-commit worktree is clean on `feat/kronika-one-product`. No push, fetch, tag, merge, or rebase.

AP pin is unchanged at `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` for the gitlink and `.ap` HEAD. The baseline-to-HEAD name list does not include the managed block, `docs/AP_UPGRADE_OBSERVATIONS.md`, `pyproject.toml`, `poetry.lock`, or a migration.

Deviations: none.

Risks and missing evidence: no adapter, network call, credential value, API, or UI was added. The OpenAI descriptor stays `unconfigured` and every selection snapshot is `live_ready` false. Media CLI commands in `src/framenest/adapters/cli/ai.py` construct a new `AiServerConfig` and do not copy `research`, so a later media CLI save would omit a previously stored research section. The administrator API uses `replace()` and keeps the field. Those callers are outside this allowlist. Price arithmetic is not a live price schedule. Independent acceptance was not required and was not performed.

Smallest next step: a focused independent acceptance of these contracts and configuration, then S6.

Orchestration critique:
MEASURED: media CLI config writers rebuild `AiServerConfig` without `research` (`src/framenest/adapters/cli/ai.py` constructions around the configure, add, and remove commands); a later CLI media save drops a stored research section; smallest correction is a later grant that copies `research` on those constructors. Administrator `replace()` already preserves it.
LEAD: none
Resolved Execution Issues / Near-Misses: `git diff --cached --check` rejected one extra blank line at EOF in `research_configuration.py` before commit. The line was removed and the same declared test-focus route was re-run: 399 passed. No assertion was removed.
Pre-existing Failure Classification: none
Authority expiry: this terminal report ends the grant; no autonomous continuation.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 29
Worker exchange ordinal: 01
Task identity: APMC-S8-PLAN
Status: PASS
Phase-qualified result: not-applicable
Native planning mode: required — confirmed enabled
Planning layer: implementation-planning
Plan disposition: advisory
Evidence tier: E0
Evidence posture: non-independent
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
Start commit: 4c524ec3020bbd2f27f2ce32ac160d2c40469c0e
End commit: 4c524ec3020bbd2f27f2ce32ac160d2c40469c0e
Report justification: new-evidence
```

**Summary:** Add catalog-model probe history and a reviewed admin workflow for activation and ordering. Fake probes execute locally with zero egress. Explicitly enabled live probes use a bounded Node subprocess calling the existing capability function. Preserve catalog eligibility, dynamic freshness ranking, and DiagnosticTarget’s Slice 7 boundary.

**Core evidence and disposition**

- **Changed files:** none; the checkout remains clean.
- **Validation performed:** baseline and AP pin inspection; targeted source, migration, template, test, and dependency inspection; syntax parsing of seven relevant Python files; isolated evaluation of the existing direct-model selector.
- **Measured finding:** the selector returned Groq at `sort_order=99` before Gemini at `sort_order=1`. Database ordering currently has no authority over that sequence.
- **Tests:** no application tests, builds, migrations, or live probes executed. Proposed tests appear in D6.
- **Commit/push:** neither authorized nor performed.
- **Network, secrets, dependencies:** no network requests, credential inspection, or dependency operations.
- **Material qualification:** the prompt’s flag descriptions omit active direct rivals, which the baseline prepends under both flag states. This design preserves that behavior.
- **Smallest next step:** ORCHESTRATOR reviews this design and, if accepted, issues one complete implementation grant to a fresh Worker with `Native planning mode: not-used`.
- **Context pressure:** moderate; sufficient context remained to complete this bounded report.

### D1: Ping-pong probe execution architecture

**Choose a short-lived Node subprocess.**

| Option | Assessment |
|---|---|
| Dedicated Node worker invoked by Django | Reuses the existing TypeScript capability function without a running Next.js server. Allows a fixed executable, restricted environment, bounded IPC, and forcible termination. |
| Internal Next.js HTTP route | Requires server availability, service authentication, an internal origin, and coordination between Django and HTTP timeouts. It adds an endpoint without improving this bounded admin operation. |

The existing [resolver hook](/home/agile/Projects/libretiles/frontend/scripts/diagnostic-resolve-hooks.mjs:30) supports plain Node imports of repository TypeScript. Local Node is `v26.4.0`. Reuse that hook unchanged, but create a separate worker; do not modify the diagnostic match worker or its credential whitelist.

**Invocation and authority**

- Add `POST /admin/catalog/aimodel/<id>/probe/`, wrapped in `admin_view`, with explicit model-change permission and a new `catalog.probe_aimodel` permission.
- Accept only a requested mode, `fake` or `live`, defaulting to `fake`. Resolve the provider/model from the referenced `AIModel`; reject posted URLs, credentials, environment names, executable paths, target IDs, or runtime configuration.
- Allow probing inactive catalog rows so an operator can inspect a pair before activation. A result never changes `is_active`, tags, ordering, or eligibility.
- This is the existing `validateMove → pong → finishMove` capability exercise. It uses no ICMP, game session, move submission, or fallback queue.

**Fake and live behavior**

| Request | Result |
|---|---|
| Default/fake | Django creates a deterministic simulated `pass`, `latency_ms=0`, `outbound_count=0`, and `executed_runtime_mode=fake`. No subprocess, credential lookup, DNS, or HTTP. |
| Live with sentinel absent or not exactly `1` | Refuse before credential access or spawning. Show a fixed error; create no probe record. |
| Live with sentinel enabled but missing/placeholder configuration | Worker returns sanitized `not_configured`, zero outbound requests, and mode `live`. |
| Live with valid configuration | Invoke `probeProviderCapability` once for the exact pair. |

The Node entry point independently checks `PROVIDER_PROBE_LIVE === "1"` before constructing a live runtime. Its own fake branch also returns before runtime construction. The environment gate alone never changes the default admin action to live.

The [capability function](/home/agile/Projects/libretiles/frontend/src/lib/provider-capability.ts:337) currently has no internal live sentinel. Preserve its reusable interface and place the admin gate around it.

**Execution bounds**

- Capability deadline: **20 seconds**.
- Worker watchdog: **22 seconds**; Python subprocess deadline: **25 seconds**, followed by kill and reap.
- Retain the existing maximum of three generation steps and `maxRetries: 0`; add a fixed `maxOutputTokens: 512` to the capability generation.
- The admin worker permits at most **four actual HTTP dispatches**, including IBM IAM and any runtime-level authentication refresh. Block a fifth before dispatch; report `unknown` with fixed reason `request_limit`.
- Count actual dispatches in the worker guard. The existing tracker increments before fetch, so its count cannot establish the exact total when the guard refuses a request.
- Use a database-backed global admission interval of **60 seconds**, shared by fake and live requests. One admitted request launches at most one child. Do not queue, bulk-probe, or automatically retry.
- Hold no database transaction open while the child runs.

Use fixed argv with `shell=False`, a fixed worker path, and the existing frontend directory as cwd. The child receives only basic process environment names and the selected provider’s configuration names:

| Provider | Names forwarded for an admitted live probe |
|---|---|
| OpenRouter | `OPENROUTER_API_KEY` |
| NVIDIA NIM | `NVIDIA_API_KEY` |
| Groq | `GROQ_API_KEY` |
| Gemini | `GEMINI_API_KEY` |
| Cloudflare | `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN` |
| Mistral | `MISTRAL_API_KEY` |
| IBM | `IBM_CLOUD_API_KEY`, `IBM_WATSONX_PROJECT_ID`, `IBM_WATSONX_REGION` |
| Aion | `AION_API_KEY` |
| Hugging Face | `HF_TOKEN` |

Never copy the full environment or load `.env` files in the worker. Do not forward Django secrets, JWTs, proxy variables, `NODE_OPTIONS`, or the diagnostic live sentinel.

**IPC contract**

- One versioned JSON command and one terminal JSON response; no long-lived worker.
- Input contains only version, mode, provider, and model. Limit input to 4 KiB.
- Output contains version, executed mode, the existing five-field capability result, and a closed reason code. Limit stdout to 16 KiB; discard stderr with a 4 KiB limit.
- Reject malformed, oversized, duplicate, mismatched-pair, or unexpected output. Never display subprocess output or exception text.
- A killed worker produces `timeout`; unavailable or malformed worker execution produces `unknown`. If the actual outbound count was not recovered, store it as unknown rather than zero.

### D2: Probe history child table model & retention

Create `CapabilityProbe`, database table **`catalog_capability_probe`**:

| Field | Definition |
|---|---|
| `id` | BigAutoField |
| `ai_model` | Required FK to `AIModel`, `PROTECT`, related name `capability_probes` |
| `requested_by` | Nullable FK to the configured user model, `SET_NULL` |
| `probed_at` | Aware timestamp when the request is admitted |
| `completed_at` | Nullable completion timestamp |
| `provider_snapshot` | CharField, maximum 50 |
| `model_id_snapshot` | CharField, maximum 200 |
| `status` | CharField, maximum 32, constrained to the existing ten statuses |
| `latency_ms` | Nullable nonnegative integer, maximum 300,000 |
| `outbound_count` | Nullable nonnegative integer, maximum four |
| `executed_runtime_mode` | Constrained to `fake` or `live` |
| `reason_code` | Closed, bounded service reason |
| `summary` | Maximum 200 characters, generated exclusively from fixed server copy |

Persist exactly these statuses:

`pass`, `not_configured`, `auth_failed`, `rate_limited`, `model_unavailable`, `named_tool_unsupported`, `tool_continuation_failed`, `schema_failed`, `timeout`, `unknown`.

Freeze that vocabulary in the migration and parity-test it against the TypeScript export. Add database constraints for status, mode, numeric bounds, and fake records having zero outbound count. Do not store provider error text, bodies, headers, usage, reasoning, credentials, or arbitrary JSON details.

For admitted live work, create an incomplete record before spawning: `unknown`, reason `incomplete`, null completion/count. Finalize that row once. A terminated Django process therefore leaves an honest incomplete observation. Completed rows have no application editing path.

**Small coordination table**

Add one unregistered singleton, `CatalogAdminControl`, with:

- Fixed primary key `1`.
- `revision`, initially zero.
- `ordering_reviewed`, initially false.
- `probe_not_before_at`, initially null.

This coordinates reviewed writes and global probe admission across Django processes without requiring Redis for local use. Missing coordination state refuses admin mutations.

**Migration**

The measured catalog leaf is `0012_multi_provider_free_rivals`. Add:

`backend/catalog/migrations/0013_admin_provider_model_console.py`

It creates both tables, seeds the singleton, and adds the probe permission. Depend on catalog `0012` and the swappable user model. No game migration or existing catalog migration changes.

**Presentation and retention**

- Register a read-only history admin, newest first, with 50 rows per page and filters for parent, status, mode, and time.
- On the AIModel changeform, show the latest ten observations and a link to filtered full history.
- Label fake results **“Simulated PASS — capability unverified.”** Show the latest completed live result and its timestamp separately.
- Disable history add/change/delete actions and AIModel deletion through admin.
- Retain the newest **100 records per AIModel**, ordered by `(probed_at DESC, id DESC)`. Prune during the same transaction that inserts an admitted record.
- Add an index on `(ai_model, -probed_at, -id)`. No recurring task or host scheduler is needed.

### D3: Reviewed fallback-order and activation controls

**Selection semantics**

The [baseline selector](/home/agile/Projects/libretiles/backend/catalog/selection.py:131) constructs active direct rivals first, then the flag-dependent compatibility segment. Its fixed tuples and freshness key currently determine order.

Implement the following exact interpretation of reviewed ordering:

| Segment | Ordering after the first accepted review |
|---|---|
| Active direct rivals, both flag states | Ascending stored `sort_order`; original direct-pair position breaks ties |
| Curated compatibility segment, flag off | Ascending stored `sort_order`; original bootstrap position breaks ties |
| Dynamic OpenRouter segment, flag on | Existing newest-first selection and ranking remain unchanged |
| NIM in the dynamic segment | Remains last |

Direct rivals remain before the compatibility segment. Watchlist rows remain unselectable. An order change cannot promote an otherwise ineligible row or substitute an older model into the dynamic four.

The review must identify which changes affect each flag state. A curated row’s priority can affect flag-off behavior while dynamic mode contss. Non-curated dynamic rows have no editable priority control in this slice.

Initially, `ordering_reviewed=false` preserves existing behavior despite previously stored, ignored priorities. The first accepted review explicitly previews and enables the new ordering behavior. Migration alone changes no selected sequence.

Extract a pure selection helper over supplied rows, explicit flag state, review state, and one captured time. Keep `get_selectable_models()` as the public authority and use the same helper for preview and validation. Do not temporarily change global Django settings inside requests.

**Reviewed workflow**

1. A read-only GET editor shows current activation, editable priorities, effective fallback sequences under **both** flag states, and each sequence’s flagship.
2. `POST .../controls/review/` validates a bounded formset, computes the proposed diff without catalog writes, and renders before/after values and both effective sequences.
3. The confirmation carries a signed, ten-minute token containing the actor, control revision, current flag, catalog fingerprint, and exact proposed changes.
4. `POST .../controls/apply/` accepts that reviewed token. It never accepts replacement editable values alongside confirmation.
5. Success commits and redirects with a success message. Stale, expired, tampered, or unsafe reviews require a new preview.

Limit one batch to 100 rows, with paginated editing. Reject duplicate or unknown IDs, unsupported fields, malformed booleans, and priorities outside signed 32-bit integer bounds.

**Atomicity and refusal invariants**

Within one `transaction.atomic()`:

- Acquire the singleton write lock **before reading catalog state**. Use an initial database write so SQLite also serializes competing writers; do not rely solely on `select_for_update`.
- Lock AIModel rows in primary-key order, compare the signed revision/fingerprint, and recheck permissions.
- Apply only the reviewed `sort_order` and `is_active` changes.
- Require at least one active language model whose tags are a list containing the exact `"tools"` token.
- Require a nonempty selectable result with the dynamic flag explicitly **false** and explicitly **true**.
- Also verify the normal `get_selectable_models()` result within that transaction.
- Persist the reviewed-order state, revision, and Django admin audit entries with the changes.

Any refusal raises out of the atomic block. Then emit a prominent `messages.ERROR` and HTTP 409. No model, ordering-state, revision, or audit changes survive. Database lock contention also fails closed with fixed retry copy.

Useful errors include:

- “This change would leave no selectable models with the dynamic catalog disabled.”
- “This change would leave no selectable models with the dynamic catalog enabled.”
- “Keep at least one active language model with tool support.”
- “The catalog changed after review. Review the current values again.”

**Close bypasses and preserve operator decisions**

- Remove AIModel `list_editable`.
- Existing AIModel changeforms make activation, ordering, provider/model identity, and eligibility fields read-only. Metadata editing remains available.
- Admin additions require add and change permission and always create inactive rows. Activation then uses the reviewed workflow.
- Disable single and bulk AIModel deletion.
- Keep AIPrompt administration unchanged.
- Add an explicit change-permission guard to the existing sync POST.
- Make seed and sync database write phases use the same coordination lock and advance its revision; perform the catalog fetch before acquiring that lock.
- Preserve existing `sort_order` values in both writers. Currently [seed overwrites them](/home/agile/Projects/libretiles/backend/catalog/management/commands/seed_models.py:141), and [sync overwrites bootstrap priorities](/home/agile/Projects/libretiles/backend/catalog/openrouter_sync.py:147).
- Seed must save only refreshed fields, excluding existing activation and priority, to avoid overwriting a concurrent operator decision.

Public catalog response fields and frontend fallback interfaces remain unchanged. Row one remains flagship/recommended, and valid player preferences retain their existing precedence.

### D4: Django admin template and presentation safety

Django admin uses session authentication and receives no protection from Next.js `proxy.ts` CSP.

- Render model names, IDs, providers, summaries, statuses, and messages using ordinary Django template escaping.
- Prohibit `|safe`, `mark_safe()`, `autoescape off`, raw HTML concatenation, and JavaScript interpolation of these values in the added presentation.
- Construct links with Django URL reversing and typed IDs. Use fixed status classes and fixed message copy.
- Every probe, review, and apply endpoint is POST-only, wrapped in `admin_view`, and covered by CSRF protection.
- `admin_view` checks staff access; explicitly check the corresponding model permission as well. Check permissions during both review and apply, including each changed row.
- Restrict history visibility to authorized catalog viewers; standalone history also requires its view permission.
- Return 405 for authenticated GET requests to action endpoints, 403 for insufficient permissions or CSRF failure, 429 for admission throttling, and controlled errors for invalid reviews.
- Keep catalog GETs, history GETs, and changeform rendering free of probes and catalog writes.

Use normal admin templates and CSS; no browser automation or new frontend page is required.

### D5: Relationship between catalog `AIModel` and `DiagnosticTarget`

**Probe history covers AIModel only in Slice 8.**

There is no DiagnosticTarget FK, probe button, inferred association by model string, or player-catalog promotion. A catalog history result does not certify a diagnostic target sharing the same model ID.

DiagnosticTarget and DiagnosticAllowedHost remain unchanged. Their existing fake-only execution, authorization, credential binding, URL policy, and bound `node:https` adapter remain the authority for diagnostic seats. The new worker never receives their URLs, credential environment names, or target IDs.

Future target probing would require a separate grant and the existing diagnostic runtime/SSRF path. The catalog worker is not that extension point.

### D6: Fail-before tests, exact allowlist, and tier estimation

The matrix below is proposed validation, not a claim that tests were executed. New endpoint tests must include authorized success cases so an absent route cannot satisfy a negative test accidentally.

| ID | Test and required evidence |
|---|---|
| F01 | Authorized fake POST persists exactly one child record with correct parent, actor, snapshots, mode, and zero count; no runtime, subprocess, credential lookup, DNS, or HTTP occurs. |
| F02 | Default remains fake even when the live sentinel is set. Explicit live requests with a disabled gate fail before spawning or credential access. |
| F03 | Mocked live missing/placeholder configuration returns `not_configured`, count zero. Unknown or spoofed pairs cannot select another runtime. |
| F04 | Reused capability tests retain named validate, pong, model-driven finish, schema refusal, three-step limit, no SDK retries, and sanitized status behavior; verify the output-token bound. |
| F05 | Worker watchdog, parent timeout, crash, missing Node, malformed/oversized output, and pair/mode mismatch produce bounded failure records without raw output disclosure. Missing counts remain null. |
| F06 | A fifth mocked HTTP dispatch is refused before egress; totals include IBM IAM. One request never starts a second probe or fallback. |
| F07 | Competing requests obtain only one admission slot; rejected requests create no child/history. Expiry permits the next request. |
| F08 | Attempt to deactivate the last tools-capable language row refuses and preserves the entire reviewed batch. A valid replacement activation in the same batch succeeds. |
| F09 | Independently test a candidate leaving flag-off empty and one leaving flag-on empty, while the other flag remains nonempty. Active watchlist or unrelated rows do not satisfy the guard. |
| F10 | Review POST changes no catalog rows. Apply commits exactly the signed diff and audit entries. Expired, tampered, replayed, and stale tokens are refused. |
| F11 | Two competing activation updates cannot each remove the other’s surviving row. Exercise SQLite serialization and safe lock-contention handling with separate connections. |
| F12 | Existing-form POSTs, changelist saves, crafted activation fields, and delete actions cannot bypass review or remove the last usable row. |
| F13 | Authenticated action GETs return 405; CSRF-enforced clients reject tokenless POSTs; anonymous, non-staff, view-only, and missing-probe-permission users cannot mutate. Authorized controls succeed. |
| F14 | Hostile model/provider text and directly inserted hostile history summaries render escaped in changeform, history, review, and messages. No executable payload survives. |
| F15 | Migration preserves all AIModel values and existing relationships. Initial review state preserves baseline ordering. Reverse migration is tested only against disposable test data. |
| F16 | Reviewed priorities affect direct and flag-off curated order; ties are deterministic. Dynamic membership, freshness ranking, NIM-last, watchlist exclusion, and flagship semantics remain intact. |
| F17 | Seed and mocked sync preserve accepted priorities and activation, advance stale-review detection, and retain current discovery/kill-switch behavior. |
| F18 | The 101st admitted observation retains exactly the newest 100; newest-ten display and live/fake separation remain correct. History editing/deletion is refused. |
| F19 | DiagnosticTarget cannot reach the new worker/history path. Existing diagnostic SSRF, runtime, activation, and credential-binding regressions remain green. |

**Exact implementation allowlist**

```text
backend/catalog/models.py
backend/catalog/admin.py
backend/catalog/selection.py
backend/catalog/admin_controls.py
backend/catalog/provider_probes.py
backend/catalog/openrouter_sync.py
backend/catalog/management/commands/seed_models.py
backend/catalog/migrations/0013_admin_provider_model_console.py
backend/catalog/templates/admin/catalog/aimodel/change_list.html
backend/catalog/templates/admin/catalog/aimodel/change_form.html
backend/catalog/templates/admin/catalog/aimodel/controls.html
backend/tests/test_catalog_admin_controls.py
backend/tests/test_provider_probe_history.py
backend/tests/test_provider_probe_worker.py
backend/tests/test_catalog_admin_console_migration.py
frontend/scripts/probe-worker.mjs
frontend/src/lib/admin-provider-probe.ts
frontend/src/lib/admin-provider-probe.test.ts
frontend/src/lib/admin-provider-probe.worker.test.ts
frontend/src/lib/provider-capability.ts
frontend/src/lib/provider-capability.test.ts
backend/.env.example
README.md
docs/architecture.md
```

Existing files outside this list are read-only. In particular, preserve `.ap/`, all existing migrations, game models/admin/runtime, diagnostic workers and adapters, package manifests, lockfiles, and real environment files.

**One following implementation sequence**

1. Add focused failing tests establishing the missing history, review, ordering, and refusal behavior.
2. Implement the additive migration, coordination state, shared selection preview, reviewed transaction, and seed/sync priority preservation.
3. Implement probe persistence, fake execution, bounded worker, live gates, and escaped admin presentation.
4. Run focused tests, existing catalog/fallback/capability/diagnostic regressions, then required type and lint checks. Inspect migration drift and the final diff; report and stop.

Use installed dependencies. Backend validation must disable dotenv loading with `PYTHON_DOTENV_DISABLED=1`, use synthetic test configuration and disposable databases, and exclude ambient credentials. The installed dotenv implementation supports that switch. Frontend validation uses the existing Vitest configuration, with no live sentinel or ambient credentials.

Required checks include backend Ruff and mypy, focused pytest suites, frontend typecheck/lint, and the relevant Vitest suites. Migration checks must be non-writing against the source tree. Do not run `npm run build`, `npm run probe:provider`, live catalog sync, provider requests, or dependency installation.

**Evidence recommendation:** E2 for implementation, with non-independent Worker evidence. Estimate two to three focused engineering days, with roughly one third devoted to authorization, concurrency, subprocess, migration, and escaping verification. PostgreSQL-specific concurrency behavior must be identified separately if no authorized PostgreSQL test environment is available.

### D7: Critique, exclusions, and threat-model fields

**Remaining risks and operating assumptions**

- “Usable” means catalog-selectable with tool metadata. These checks cannot establish credential validity, current provider availability, or genuine live capability. Fake PASS is never live acceptance evidence.
- Ordering remains constrained by the locked selection groups and dynamic freshness ranking. The review explicitly displays those limits.
- SynchronousDjango worker for up to the subprocess deadline. Global admission bounds this cost; background job infrastructure is outside this slice.
- The Node executable, frontend sources, and installed dependencies must be available beside Django for live probes. Separate hosting still permits fake probes; missing live prerequisites produce a recorded failure.
- The four-request ceiling may interrupt IBM authentication recovery. Report that refusal accurately; do not silently expand the budget.
- Admin transaction guarantees do not prevent a later catalog sync, direct database write, provider outage, or credential change from affecting playability. Seed/sync serialization prevents stale interleaving but does not alter their accepted eligibility policies.
- A parent crash can leave an incomplete observation. It must never become a synthesized PASS or a claimed zero-call result.
- Retention is a bounded operational history, not a permanent audit archive.
- The coordination row is required for safe mutation. Missing state or database contention refuses changes rather than bypassing the guard.

Roll out by applying the additive migration before enabling the new application code. Keep the live gate unset and retain the current dynamic flag. Initial `ordering_reviewed=false` prevents an unreviewed ordering change. Roll back an operator change through another reviewed diff; application rollback may leave the additive tables in place. No host deployment or scheduled task is authorized here.

**Explicit exclusions:** K1 live NIM calls; all real provider calls during implementation validation; the 14/00 AI-strength whole; a full Provider entity; watchlist or DiagnosticTarget promotion; Slice 7 SSRF redesign; F05 changes; frozen game migrations; VPS deployment; browser MCP diagnostics; dependency installation; push/publication; and changes to R2, R3, provisional R4 subcaps, or authorship-abort behavior.

**Threat-model fields**

| Field | Slice 8 assessment |
|---|---|
| Assets | Admin sessions and privileges, catalog availability and ordering, provider credentials/quota, Django worker capacity, database storage, and probe-history integrity. |
| Trust boundaries | Browser → Django admin; Django → subprocess IPC/environment; worker → existing provider runtimes; provider results → database → authenticated admin HTML. |
| Attacker-controlled inputs | Forged POST fields, stale/replayed review tokens, hostile catalog labels and IDs, malformed provider responses, and synthetic malformed worker output used to test the IPC boundary. |
| Security properties | Staff and model permissions, CSRF, signed actor-bound reviews, serialized atomic writes, exact-pair resolution, explicit live gating, restricted environment, bounded execution, fixed summaries, and template escaping. |
| Abuse cases | CSRF-triggered probing, unauthorized activation, concurrent last-model removal, hidden order changes, stored XSS, environment/argv injection, repeated probe consumption, output flooding, and fake/live evidence confusion. |
| Attacker profile | An unauthenticated web attacker, a staff account lacking change/probe permission, a compromised provider response, or an operator submitting stale/conflicting changes. OS/root compromise is outside this boundary. |
| Attack surface | Custom admin endpoints/forms, history rendering, catalog metadata, subprocess launch and result parsing, and live provider transport. |
| Threat condition | Untrusted data is mistaken for authority or HTML; concurrency bypasses catalog checks; or a fake/admin invocation reaches a live runtime without an explicit gate. |
| Technical mechanism | Forged POSTs, token replay, write skew, unchecked ordinary admin saves, unsafe template rendering, inherited process configuration, and unbounded calls or subprocess output. |
| Blast radius | Admin account takeover, gameplay catalog outage, provider quota consumption, worker exhaustion, or misleading persisted capability evidence. |
| Verification strategy | F01–F19, including positive authorization controls, CSRF-enforced clients, separate database connections, synthetic hostile strings, bounded subprocess faults, and denied/mocked network dispatch. |
| Residual risk | A fully authorized malicious administrator can consume the permitted probe allowance or choose poor models. Provider behavior remains external; deployment-specific PostgreSQL locking and process supervision require evidence in their authorized environment. |

**Authority expiry:** Submission of this terminal planning report ends this Worker’s authority. No implementation was performed or is authorized in this session. Acceptance requires a separate complete ORCHESTRATOR grant to a fresh implementation Worker.

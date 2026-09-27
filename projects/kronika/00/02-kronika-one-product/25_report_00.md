### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-one-product
Worker session ordinal: 25
Worker exchange ordinal: 01

Persistent role identity: WORKER
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-MODULAR-SEARCH-PROVIDER-PLAN
Native planning mode: required

Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence

Start commit: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
End commit: fd277a9a64a6965df76127dbec5b1735d2fb3cdd
Changed files: none
Tests/builds/application execution: not performed
Provider API calls: none
Host/browser/account/credential actions: none
Commit/push/publication: none
Subagents: none

Delivery: this complete Markdown artifact in chat
Report file: not written, as explicitly requested by the Cooperator
```

# Kronika: modular research providers and an administrator-curated Timeline

## 1. Accepted direction and verified evidence

Implement Search and Research through a provider-neutral application boundary in FrameNest. The first provider is **OpenAI Responses API**, with a fixed `gpt-5.5-2026-04-23` configuration and native provider-managed research. Capture remains parked.

The Cooperator made additional product decisions during this planning exchange. These supersede the conflicting preserved assumptions in the initial planning prompt:

| Decision | Final requirement |
|---|---|
| Personal history | Kronika stores questions and their answers, including complete Research reports. |
| Administrator access | An authenticated application administrator can read all product records, including private and unfinished work. |
| Shared publication | Administrators approve completed questions/answers and successfully analyzed media for the shared page. Owners do not directly publish to that page. |
| Main page | Timeline contains only administrator-approved records. Personal history is a separate view. Gallery remains a working view. |
| Audience | The shared page is for verified household members only. Internet publication remains disabled. |
| Research execution | Use native Deep Research at the external provider. FrameNest supervises its lifecycle. |
| Provider | OpenAI Responses API, fixed model, no automatic fallback. |
| Budget | Application thresholds: Search USD 0.50, Research USD 5, daily USD 10, monthly USD 30. Configure a provider monthly hard limit of USD 30; delayed enforcement and possible overshoot were explicitly accepted. |
| External retention | The Cooperator accepted the explained standard OpenAI retention, including possible security retention after deletion of the retrieved response. ZDR is not required. |

Authority for these changes is the Cooperator’s current-conversation answers, including “Admin vidí všetko”, “Spoločná + osobná história”, and “Iba domácnosť”. They must be promoted into durable documentation before executable implementation.

**Meaning of private:** private records are visible to their owner and administrators, but not to other ordinary household members. Administrator access concerns application content; it grants no access to provider secrets, browser credentials or host administration.

### Verified baseline

| Evidence class | Finding and implication |
|---|---|
| Direct local Git observation | FrameNest is clean on `feat/kronika-one-product`; HEAD, local `main` and `origin/main` equal the start commit. Parent is `e408bb5503f359ec24542304ac1a621c6b9e4ffb`. No local changes were made. |
| Direct local Git observation | AP gitlink and checked-out AP HEAD both equal `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. Preserve this pin. |
| Direct repository evidence | The current common-record architecture is documented as future work. Schema head is `0033`; `0034` is the next free revision. See [ADR-0082](/home/agile/Projects/framenest/docs/adr/0082-kronika-one-product-and-private-records.md:54), [revision 0033](/home/agile/Projects/framenest/src/framenest/infrastructure/persistence/alembic_environment/versions/0033_media_analysis_proposals.py:8) and [migration tests](/home/agile/Projects/framenest/tests/integration/test_persistence_migrations.py:47). |
| Direct repository evidence | FrameNest already has provider composition, non-secret configuration and server-side credential loading. Its existing declarative protocol is Chat Completions, not the required Responses research contract. See [registry](/home/agile/Projects/framenest/src/framenest/infrastructure/ai/registry.py:133), [configuration](/home/agile/Projects/framenest/src/framenest/infrastructure/ai/configuration.py:28), [protocol definitions](/home/agile/Projects/framenest/src/framenest/infrastructure/ai/provider_records.py:27) and [credentials](/home/agile/Projects/framenest/src/framenest/infrastructure/ai/credentials.py:75). |
| Historical publication evidence | Report 23 records publication of the baseline. Current public branch equality was **not independently observed in this exchange**. Local remote-tracking refs are not substituted for that evidence. [Publication report](/home/agile/meta/projects/kronika/00/02-kronika-one-product/23_report_00.md:20). |
| Orchestrator-relayed host evidence | Reports 21–24 and the notes record the C3 correction, its acceptance/publication, successful browser startup and subsequent parking at the login boundary. They do not establish completed S3 login/ask acceptance. No host observation was made here. [Correction](/home/agile/meta/projects/kronika/00/02-kronika-one-product/21_report_00.md:19), [acceptance](/home/agile/meta/projects/kronika/00/02-kronika-one-product/22_report_00.md:69), [deployment](/home/agile/meta/projects/kronika/00/02-kronika-one-product/24_report_00.md:21), [parking decision](/home/agile/meta/projects/kronika/00/02-kronika-one-product/00_notes.md:1165). |
| Direct historical-source observation | The source Kronika checkout is clean at `66c40d43c577276b0ad304a494fbbb1ffb6fc933`. It remains read-only. Its Markdown and sanitization helpers are selective reference material, not a second application to import. |

Retain the repository outcomes of S0–S3, capture preparation code, MEME/Movie, Gallery, existing metadata review, no old-database import, the NUC development/test role, internal package identities and the S10 public rename.

## 2. Provider architecture and public interfaces

### Placement and responsibilities

Follow the existing domain/application/infrastructure separation and capture import boundaries. [Existing application port](/home/agile/Projects/framenest/src/framenest/application/ports/media_suggestion.py:10), [import-boundary tests](/home/agile/Projects/framenest/tests/unit/test_import_boundaries.py:43).

| Layer | Addition |
|---|---|
| Domain | Pure research request/result, lifecycle, capability, usage and typed-error values. Common-record ownership and publication rules remain separate domain concerns. |
| Application ports | `ResearchProvider`, request repository, budget ledger and atomic result-completion ports. No HTTP, SQLAlchemy, SDK or capture imports. |
| Application | A lifecycle-owned research coordinator: authorize, reserve budget, submit, poll, cancel, validate, save and reconcile cleanup. |
| Infrastructure | OpenAI Responses adapter; bounded HTTPS transport; provider registry/configuration; SQLite implementations; document renderer. |
| API adapters | Research request/history endpoints, common-record reads, administrator approval and operational controls. |
| Composition | Wire the coordinator into the existing FastAPI lifespan. Do not introduce another server, broker or deployment system. |

The coordinator follows the existing lifecycle pattern, but **must not inherit automatic resubmission of interrupted analysis**. Research submission uncertainty needs its own fail-closed recovery. [Coordinator pattern](/home/agile/Projects/framenest/src/framenest/application/media_analysis_coordinator.py:53), [existing analysis recovery](/home/agile/Projects/framenest/src/framenest/application/media_analysis_lifecycle.py:379), [application lifespan](/home/agile/Projects/framenest/src/framenest/adapters/api/application.py:1150).

### Port contract

```text
ResearchProvider
  describe() -> ProviderDescriptor                 # network-free
  submit(ProviderRequest) -> ProviderObservation
  poll(ProviderHandle) -> ProviderObservation
  cancel(ProviderHandle) -> ProviderObservation
  release_remote(ProviderHandle) -> CleanupOutcome
```

`ProviderDescriptor` declares:

- Stable provider ID and adapter/configuration version.
- `search` and `research` capabilities.
- Execution location and native-research support.
- Cancellation, remote-result retrieval and remote-deletion support.
- Retention posture and accounting capabilities.
- Submission-idempotency guarantees, including an explicit “not guaranteed”.
- Availability: disabled, parked, unconfigured or configured; configuration is not proof of live readiness.

`ProviderRequest` contains only the bounded user prompt, operation kind, opaque operation ID, fixed server-selected profile, deadline and approved resource limits. Owner identity stays inside the application and is not transmitted as provider metadata.

`ProviderObservation` distinguishes pending, running, complete, refused, failed, cancelled and uncertain outcomes. A complete result contains full answer text/Markdown, citations, completion evidence, usage and an opaque remote handle. It carries no trusted HTML.

The application generates titles deterministically from the question; it does not purchase another model call for naming.

### Registry and selection

Extend the existing non-secret AI configuration to schema version 3 with an optional `research` section. Read versions 1 and 2 without mutation and treat an absent section as disabled. Preserve media provider selection and existing administrator operations when saving the new section.

Research has its own selected workflow provider, not a replacement for media analysis:

- `openai-responses`: first implemented adapter.
- `chatgpt-page`: parked descriptor, unavailable for new Search/Research work.
- Future self-hosted provider: another adapter and explicit endpoint policy.

Selection is server-controlled and snapshotted at admission. An active request never changes provider/model because configuration changes. No dynamic plugin imports or client-supplied endpoint/model/tool fields are accepted.

A future capture adapter uses the loopback HTTP contract and the same result port. It must prove complete Search/Research capabilities before activation. Existing consumers, records and UI do not need a provider-specific rewrite.

### HTTP contract

Use existing verified ingress, route policies, Origin validation and mutation protection. [Identity context](/home/agile/Projects/framenest/src/framenest/domain/identity_access.py:106), [route policy table](/home/agile/Projects/framenest/src/framenest/adapters/api/tailscale_ingress.py:120).

| Endpoint | Contract |
|---|---|
| `GET /api/research/capabilities` | Safe selected-provider status, supported modes, limits and retention notice; no live probe. |
| `POST /api/research-requests` | `{kind, prompt, client_request_id, consent_version}`. Server derives owner, provider and limits. Returns 202 after durable admission. |
| `GET /api/research-requests` | Caller’s question history, including pending and failed requests. |
| `GET /api/research-requests/{id}` | Owner or administrator; safe status and eventual record reference. |
| `POST /api/research-requests/{id}/cancel` | Owner or administrator. Cancellation is a request until remotely confirmed. |
| `GET /api/my/records` | Caller’s records; completed question/answer history and owned media. |
| `GET /api/timeline` | Approved household records only, including when the caller is an administrator. |
| `GET /api/records/{id}` | Owner/admin access, or household access to the approved projection. |
| `GET /api/records/{id}/render` | Authorized isolated question/answer document. |
| `GET /api/admin/records` | Administrator review inventory across owners. |
| `GET /api/admin/research-requests` | Administrator access to all question-history states. |
| `POST /api/admin/records/{id}/approval` | `{action: approve/reject/withdraw, expected_version}`; explicit administrator mutation. |
| `GET /api/admin/research/status` | Operational state, accounting health and cleanup status. |
| `POST /api/admin/research/disable` | Durable kill switch; blocks admission and requests cancellation. |

Do not implement the earlier owner-controlled visibility PATCH. Household publication now belongs to administrator approval.

Use a dedicated `research.run` capability for mapped users/admins and `records.approve` for admins. `provider.operate` governs operational controls. Record authorization is additionally enforced on every content route.

## 3. Selected provider and exact initial configuration

Public documentation was retrieved on **2026-09-26**. These are documented capabilities, not account-specific or live-provider verification.

| Candidate | Fit and limitation | Disposition |
|---|---|---|
| OpenAI Responses API | Hosted web research, citations, background retrieval and cancellation fit the native-research requirement. Current web-search guidance recommends `web_search` with GPT-5.5 for extended research. [Web-search guide](https://developers.openai.com/api/docs/guides/tools-web-search), [background operations](https://developers.openai.com/api/docs/guides/background). | Selected by the Cooperator. |
| Google Gemini Deep Research | A native research agent is available through Interactions, currently in preview. Background execution requires stored interactions; paid-tier interaction retention defaults to 55 days, with deletion controls. [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research), [retention](https://ai.google.dev/gemini-api/docs/interactions-overview). | Realistic alternative, not implemented as fallback. |
| Anthropic Claude with web search | Offers citations, `max_uses`, usage reporting and paused-turn continuation. Search costs USD 10/1,000 searches plus token charges. This route would require a separately designed research workflow for this product. [Web-search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool). | Not selected. |

Do not start a new integration with `o3-deep-research` or `o4-mini-deep-research`: the deprecation register lists their shutdown on July 23, 2026, despite older guide examples remaining available. [Deprecation register](https://developers.openai.com/api/docs/deprecations).

### Configuration

These values are the implementation defaults, not settings applied during planning:

| Setting | Search | Research |
|---|---:|---:|
| Provider ID | `openai-responses` | `openai-responses` |
| Model | `gpt-5.5-2026-04-23` | `gpt-5.5-2026-04-23` |
| Reasoning effort, server-side only | `low` | `high` |
| Tool allowlist | `web_search` only | `web_search` only |
| `max_tool_calls` | 3 | 20 |
| `max_output_tokens` | 4,096 | 32,768 |
| Execution | Background | Background |
| Application deadline | 180 seconds | 1,800 seconds |
| Per-operation budget reservation/threshold | USD 0.50 | USD 5.00 |

Common settings:

```text
enabled = false
endpoint = https://api.openai.com/v1/responses
background = true
store = true
tool_choice = required
parallel_tool_calls = false
web_search.external_web_access = true
web_search.return_token_budget = default

global_concurrency = 1
waiting_queue_capacity = 0
daily_budget_usd = 10
monthly_budget_usd = 30
budget_calendar = UTC

prompt_max_utf8_bytes = 16384
provider_response_max_bytes = 8388608
answer_max_utf8_bytes = 2097152
citation_count_max = 200

connect_timeout_seconds = 5
http_operation_timeout_seconds = 30
poll_interval_seconds = 5
automatic_generation_retries = 0
```

No conversation chaining, file search, MCP, code execution, browser tools, local filesystem tools, location context or multi-agent feature is enabled. The tool runs at OpenAI; FrameNest does not fetch arbitrary result URLs.

The selected snapshot and reasoning options are documented. Its listed standard rates are USD 5/M input tokens, USD 0.50/M cached input and USD 30/M output; long-context pricing changes above the documented threshold. Web search adds USD 10/1,000 calls and search-content token charges. Prices must be revalidated before live activation. [Model and snapshot](https://developers.openai.com/api/docs/models/gpt-5.5), [tool pricing](https://developers.openai.com/api/docs/pricing).

### Credential boundary

Use a dedicated OpenAI project and project-scoped service credential, used only for this integration. The Cooperator provisions it under separate operational authority.

Proposed deployment mechanics:

```text
Credential identifier:
KRONIKA_RESEARCH_OPENAI_API_KEY

Root-owned source, mode 0600:
/etc/framenest/credentials/research-openai

systemd credential mapping:
LoadCredential=KRONIKA_RESEARCH_OPENAI_API_KEY:/etc/framenest/credentials/research-openai
```

The web service reads the named systemd credential through the existing credential boundary. Production composition supplies only the required credential-directory context; it does not silently prefer an ambient API key. Development may use that named environment variable when the operator explicitly configures it.

The non-secret configuration stores the credential identifier only. No key input endpoint, frontend key, command-line key, secret-bearing diagnostic or provider administrator credential is introduced.

Implement the deployment mapping as an optional source drop-in installed only during an authorized provisioned deployment. A disabled/unconfigured research provider must not prevent ordinary application startup.

### Accepted retention policy

Local question/answer history is intentional. For background jobs, request remote storage explicitly so recovery can retrieve the same response. Delete the remote response after validated local persistence, or after terminal cancellation/failure reconciliation.

Deletion of the response object is not a promise to erase security logs or all provider processing state. Standard abuse-monitoring retention can include content for up to 30 days, with documented exceptions; background processing is not ZDR-compatible. This limitation was explicitly accepted. [Data controls](https://developers.openai.com/api/docs/guides/your-data), [response deletion](https://developers.openai.com/api/reference/resources/responses/methods/delete).

## 4. Runtime, recovery and accounting

### Execution location and authority

The **supervisory runtime runs server-side in FrameNest**. The native model/search loop runs at OpenAI. This is the precise interpretation required by the Cooperator’s native-research selection; the plan does not claim local execution of the provider’s internal agent loop.

An explicit authenticated submission authorizes one bounded native generation. Loading a page, viewing history, saving metadata, sharing a result or opening status must never initiate provider generation.

Persist the request, owner, prompt, configuration snapshot, content fingerprint and budget reservation before submission. Perform network I/O outside database transactions, preserving the existing application constraint. [Current lifecycle contract](/home/agile/Projects/framenest/src/framenest/application/media_analysis_lifecycle.py:408).

### Lifecycle

```text
admitted -> submitting -> running -> validating -> saved
                         |             |
                         +-> refused / failed / incomplete
                         +-> cancel_requested -> cancelled
                         +-> timeout / submission_unknown

Remote cleanup and accounting reconciliation are tracked separately.
```

- Maintain one durable active slot across processes, including uncertain remote work.
- Additional submissions return `E_BUSY`; duplicate client submissions return their existing request.
- A persisted remote handle allows polling after a web restart.
- A crash while `submitting`, without a confirmed handle, becomes `E_SUBMISSION_UNKNOWN`. Never infer that the provider received nothing.
- Persist a bounded normalized result checkpoint before final record creation. Retry local persistence from that checkpoint without another generation.
- Release the remote response only after the local completion transaction succeeds. Cleanup failure cannot erase the locally saved result.
- During shutdown, stop admission and persist known state. Normal restarts recover known handles rather than creating replacement jobs.

### Idempotency and retries

Use a unique `(owner, client_request_id)` constraint and a fingerprint over the exact prompt, kind and accepted policy version. Reusing the key with different content returns `E_IDEMPOTENCY_CONFLICT`.

Local submission idempotency does not imply provider POST idempotency. There is **one generation attempt per request**. Do not automatically retry create on timeout, connection loss, 429, 5xx or refusal.

Polling and remote cleanup may retry at 1, 2 and 4 seconds, respecting `Retry-After`, with at most three consecutive failures and the relevant deadline. Recovery uses the same handle. Exhaustion preserves an unresolved state, holds its reservation and blocks further generation until reconciled.

Cancellation is asynchronous:

- Acknowledge `cancel_requested` locally before the remote call.
- Confirm remote terminal state before reporting cancellation as complete.
- A cancellation request committed before result-save prevents automatic record finalization.
- A result already saved remains saved; a later cancel reports the completed state.
- Kill switch blocks new generation immediately but permits bounded polling, cancellation and deletion of known operations.

OpenAI documents cancellation of background responses and idempotent repeated cancellation. This does not establish refunds or instantaneous billing cessation. [Background cancellation](https://developers.openai.com/api/docs/guides/background).

### Typed errors

Use stable sanitized codes, with no raw provider exceptions:

```text
E_DISABLED                 E_NOT_CONFIGURED
E_CAPABILITY_UNAVAILABLE   E_INVALID_REQUEST
E_BUSY                     E_IDEMPOTENCY_CONFLICT
E_AUTH                     E_RATE_LIMIT
E_PROVIDER_QUOTA           E_PROVIDER_UNAVAILABLE
E_REFUSED                  E_INVALID_RESULT
E_INCOMPLETE_RESULT        E_RESULT_TOO_LARGE
E_NO_WEB_EVIDENCE          E_TIMEOUT
E_CANCELLED                E_SUBMISSION_UNKNOWN
E_RESULT_EXPIRED           E_ACCOUNTING_UNKNOWN
E_BUDGET_EXCEEDED          E_STORAGE
```

Submission/status APIs expose operation status and an allowed next action, not arbitrary provider error text. Refusal is terminal for that request; no prompt rewriting, provider switching or account rotation is performed to bypass it.

### Budget semantics

**The accepted monetary values are admission/accounting thresholds, not an absolute invoice guarantee for an opaque native run.**

Before generation, atomically reserve the entire per-operation allowance against daily and monthly remaining budgets. Do not admit a job if its reservation would exceed either threshold.

Enforce the tool and output-token limits in the request. `max_output_tokens` includes reasoning and other non-visible output; it is not a visible-answer-length guarantee. [Responses parameters](https://developers.openai.com/api/reference/cli/resources/responses/methods/create), [token accounting](https://developers.openai.com/api/docs/guides/token-counting).

Reconcile returned usage without:

- Counting cached input twice.
- Adding reasoning tokens again when already included in output.
- Treating missing usage as zero.
- Capping recorded actual cost at the configured threshold.
- Resetting accumulated cost during local persistence retries.

If observed cost exceeds the operation threshold, preserve the true charge and complete output, block further generation and require operator reconciliation. Do not silently raise any limit.

Configure an OpenAI project hard limit of USD 30/month. It is an additional control: OpenAI explicitly states that enforcement is not instantaneous and recorded spend may exceed the configured amount. The Cooperator accepted this residual limitation. [Spend limits](https://developers.openai.com/api/docs/guides/spend-limits).

### Accounting record

Store private accounting data alongside the request repository:

```text
operation_id, request_id, nullable record_id
provider_id, configuration_version, price_schedule_version
purpose: search | research | synthetic_acceptance
operation: create | poll | cancel | delete
attempt_number, parent_operation_id
started_at, finished_at, terminal_classification
remote_handle_reference, transport_outcome

reserved_usd_micros
input_tokens, cached_input_tokens, output_tokens
reasoning_tokens_as_subset, web_tool_calls
calculated_cost_usd_micros
accounting_state: reserved | reconciled | unknown
cleanup_state, cancellation_state
```

Use integer micro-USD arithmetic with conservative rounding. Preserve distinction between calculated cost and the provider invoice. Link charges incurred before record creation to the request and later bind them to its record.

Diagnostics contain opaque identifiers, counts, durations, cost aggregates and typed outcomes. Prompts, answers, URLs, account identities, raw response bodies and credentials never enter logs.

## 5. Records, administrator approval and rendering

### Database and domain integration

Use the existing SQLite database, SQLAlchemy Core and Alembic conventions. Do not create a second library. [Schema conventions](/home/agile/Projects/framenest/src/framenest/infrastructure/persistence/catalog_schema.py:1).

Allocate:

| Revision | Contents |
|---|---|
| `0034_kronika_records.py` | Common records, complete question/answer documents, administrator approval state and indexes. |
| `0035_research_requests_and_accounting.py` | Durable research requests, provider bindings, result checkpoints, accounting operations, reservations and active-slot state. |

Recheck revision availability against each implementation grant’s baseline. A collision requires a prospectively corrected grant, not migration-history rewriting.

Required record invariants:

- UUID identity; `media/search/research` kind.
- Exactly one appropriate media/document reference.
- Non-null server-derived owner.
- Visibility initially `private`.
- Creation and completion timestamps separate from first shared-Timeline entry.
- Latest successful analysis reference and approved analysis reference for media.
- Administrator approval actor/time/version.
- Unique media binding and unique final research-request binding.
- Foreign keys and database constraints supporting atomic completion.

Create media ownership in the same transaction as media catalog insertion. Reject creation without verified or explicitly configured ownership. Do not import old databases or assign unowned historical rows to an administrator automatically.

Search/Research history stores the original question from admission. Pending and failed questions remain history entries with truthful status. A complete question/answer document, common record and final request binding are saved atomically. Incomplete output never becomes a completed record.

All locally stored prompts, generated content and source metadata are untrusted content. Persist normalized required fields, not the whole raw provider response or internal reasoning stream. Keep application databases, WAL/SHM and checkpoints inside private state with appropriate 0700/0600 permissions; include them in the existing backup boundary.

### Access policy

| Caller | Own private content | Another user’s private content | Approved household content |
|---|---:|---:|---:|
| Verified ordinary member | Allow | Deny | Allow |
| Verified administrator | Allow | Allow | Allow |
| Anonymous/unmapped/public composition | Deny | Deny | Deny |

Derive ownership from `IdentityContext.login_key`; reject client ownership overrides. Apply the same policy before counts, search, pagination and file opening.

The baseline already includes administrator read shortcuts and a permissive `policy=None` test seam. The new design centralizes the explicitly accepted administrator privilege, while missing policy/identity context fails closed. [Existing audience policy](/home/agile/Projects/framenest/src/framenest/application/content_publication.py:47), [API seam](/home/agile/Projects/framenest/src/framenest/adapters/api/content_audience_api.py:19).

Cover Gallery, workspace/admin lists, question history, records, metadata, aliases, analysis/proposals, companion history, uploads/acquisition, covers/previews, original files, Range playback, downloads, facets and duplicate handling. Ordinary users must not learn private cross-owner identities through duplicate detection.

### Approval and Timeline entry

A complete save makes Search/Research available in personal history and the administrator review inventory. It does **not** insert a shared Timeline card.

Administrator approval:

1. Rechecks the exact record/version and validated completion.
2. For media, requires successful analysis and existing persisted metadata readiness/review.
3. Records the approval and the approved result reference.
4. Changes household visibility to `family`.
5. Sets `timeline_entered_at` only on first approval.

Preserve the existing metadata-suggestion review workflow; successful generation or analysis never applies metadata automatically. Existing readiness is derived from persisted title, description and tags. [Readiness contract](/home/agile/Projects/framenest/src/framenest/domain/content_publication.py:26).

Reanalysis preserves the previous approved projection and chronological position until the administrator approves the new successful result. Failure preserves the previous success. Reapproval updates the same card. Withdrawal removes the card from the shared Timeline while retaining personal history and first-entry provenance.

Search/Research questions and answers are immutable completed documents in v1; another explicitly submitted question creates another history entry. Administrative approval of an administrator’s own item uses the same explicit action.

The existing internet-publication table is not the authority for household sharing. Existing publication actions for Kronika records must route through the new approval service or reject, so no old endpoint bypasses analysis/approval. Public composition and direct public queries continue to exclude these records.

Timeline order remains `timeline_entered_at DESC, id ASC`, default page size 24, maximum 100. Personal history uses creation time and includes unfinished work separately from completed records.

### Safe rendering

Render the question as escaped text and the answer through a bounded Markdown renderer and HTML allowlist. Preserve the complete original answer independently of its presentation.

Selectively adapt the historical standard-library helpers into FrameNest’s rendering infrastructure, with a separate provenance record. Do not import the source library manager, account system or capture package.

The historical sanitizer silently truncates at its input/output bounds and can return `fallback=False`; it cannot establish complete rendering unchanged. The Markdown helper already returns failure instead of a partial formatted document. [Sanitizer behavior](/home/agile/Tools/cli_chatgpt/src/kronika/sanitize.py:7), [truncating return](/home/agile/Tools/cli_chatgpt/src/kronika/sanitize.py:296), [Markdown completion behavior](/home/agile/Tools/cli_chatgpt/src/kronika/markdown.py:627).

Required rendering behavior:

- Explicitly report any formatting bound or parser failure.
- On formatting failure, display the entire escaped answer, never a sanitized prefix presented as complete.
- Escape raw HTML in Markdown; prohibit scripts, event handlers, forms, frames, SVG, media, external styles and image/resource loading.
- Serve the document through the authorized render endpoint in a sandboxed frame, with restrictive CSP, `no-store` and `no-referrer`.
- Never insert generated HTML into the main application DOM.
- Show validated citations as visible, user-activated links with safe schemes and `noopener noreferrer`; never automatically fetch their targets.
- Do not use the historical CLI’s secret-path result pages as a substitute for FrameNest identity authorization.

A successful result must have a terminal completed provider response, complete final answer, no refusal/incomplete marker and evidence that web search executed. Validate citation structure and bounds. A completed “no matching evidence found” answer may be stored when search execution is proven; do not fabricate citations or equate validation with factual correctness.

## 6. Security and acceptance requirements

Use fresh R3 reviews for the provider, authorization and rendering boundaries. Audit, correction and re-audit remain separate sessions. [Provider-boundary review](/home/agile/Projects/framenest/.ap/INFOSEC.md:163), [review separation](/home/agile/Projects/framenest/.ap/INFOSEC.md:369).

### Threat model

| Boundary/asset | Threat | Required control |
|---|---|---|
| Verified identity to records | Forged owner/admin claims, guessed IDs, cross-owner leaks | Trusted ingress identity; central policy; authorization before queries and byte access. |
| Submission to billing | Repeated clicks, crashes, concurrent processes, ambiguous POST | Durable intent, unique submission key, one active slot, no automatic generation retry. |
| Server to provider | Credential leakage, redirect/proxy abuse, arbitrary endpoints | Fixed HTTPS endpoint; TLS verification; redirects disabled before following; ambient proxies disabled; secret only in authorization header. |
| Prompt/web content to agent | Prompt injection and data exfiltration | Only explicit text input; no local tools, files, record retrieval or credentials in context. |
| Provider output to browser | Stored XSS, resource loading, unsafe URLs | Bounded normalized result, Markdown escaping, allowlist, sandbox and CSP. |
| Completion to shared page | Incomplete reports or unapproved revisions published | Atomic validated save followed by separate version-bound administrator approval. |
| Cancellation/cleanup | False cancellation, lost result, forgotten remote object | Durable cancellation/cleanup state, bounded retries, visible unresolved status. |
| Diagnostics/backups | Content or secret disclosure | Redacted diagnostics, private storage and backup access, no raw provider dumps. |

The existing HTTPS transport checks redirect status after `urlopen`; that is not sufficient evidence of pre-follow redirect prevention. Use a dedicated transport with an explicit no-redirect handler and bounded methods, without changing media transport behavior incidentally. [Current transport](/home/agile/Projects/framenest/src/framenest/infrastructure/ai/transport.py:76).

Only the expressly submitted text and fixed non-secret instructions may leave the host through this research path. Private media, media derivatives, unrelated records, account identities, browser state, local paths and application credentials must never be assembled into provider context. No attachment input exists.

### Required automated evidence

| Area | Positive and negative scenarios |
|---|---|
| Provider contract | Search/Research capability mapping; parked provider rejected; fake future provider works without record/API changes; clients cannot override model/tools/endpoint. |
| Authority/egress | Disabled, missing-credential, missing-consent and denied-identity paths make zero provider requests; payload excludes unrelated content; redirects and proxy inheritance cannot redirect secrets. |
| Lifecycle | Crash before/after submit, missing remote ID, restart polling, duplicate submission, cancellation/completion races, deadline expiry, lost response and cleanup failure. |
| Cost control | Atomic concurrent reservations, daily/monthly rollover, exhausted budgets, missing usage, actual cost above reservation, reasoning/cache accounting and kill switch during an active job. |
| Completeness/rendering | Refusal, incomplete response, missing final answer, zero web execution, oversize output, hostile Markdown/HTML/URLs, full-text fallback and no automatic external fetch. |
| Ownership/approval | Owner access, ordinary cross-owner denial, explicit administrator access, forged-admin denial, stale approval conflict, unapproved Timeline exclusion and immediate withdrawal. |
| Media | Atomic ownership on every insertion route, successful analysis prerequisite, metadata review preserved, one card on reanalysis and previous approval retained on failure. |
| Public exclusion | Anonymous/unmapped access denied, including direct file routes and erroneous legacy publication rows. |
| Persistence | Empty database and synthetic `0033 -> 0034 -> 0035` migration; FK/unique constraints; transactional rollback; repeated completion yields one document/record. |
| UI | Personal Q/A history, shared-only Timeline, administrator review, mobile behavior and existing Gallery/image/GIF/player regressions. |

Use existing pytest, Node and fake-transport conventions. Extend causal tests for these new boundaries; do not create a parallel test toolchain.

### Bounded live acceptance

Live verification belongs to a later separately authorized S9 operational grant, after fresh independent repository acceptance and Cooperator credential provisioning.

Allow at most:

- One synthetic Search with a public, non-personal question.
- One synthetic native Research with a public, non-personal brief.
- No automatic reruns or additional quality-correction calls.
- Maximum application reservation: USD 5.50 for that acceptance run, within the accepted day/month limits.

Record creation, polling, tool usage, terminal classification, cost evidence, local persistence and remote deletion separately. Failure stops the affected capability. A missing receipt is not success.

Cancellation and hostile-input tests use fake transports; a live cancellation experiment requires its own explicit call allowance. No private media is needed.

## 7. Revised S4–S10 sequence

Execution order is:

```text
S4-D -> S4-A -> S6 -> S4-B -> S7-P -> S8 -> S9 -> S10

Parked independently:
remaining S3 host completion
capture-mode restoration
S5 ZIP attachment activation
S7-C capture application integration
```

Each active row receives **one implementation grant**. Independent acceptance, publication and host operations require separate bounded authority. A failed gate stops that row; it does not authorize adjacent work.

| Row | Useful outcome and boundary | Dependencies | Authority/host class | Checks and acceptance | Recovery/stop and evidence before advancing |
|---|---|---|---|---|---|
| **S4-D: superseding documentation** | Record modular providers, selected native OpenAI route, Q/A history, administrator access/approval and shared-only Timeline. | Acceptance of this plan and current Cooperator decisions. | Documentation-only repository grant; no host/provider activity. | Exact allowlist, semantic/link/contradiction review; E1/R0. | Stop on unresolved contradiction or baseline drift. Next row requires accepted documentation commit and unchanged AP pin. |
| **S4-A: provider contracts/configuration** | Pure contracts, capability registry, configuration v3 and fake adapter. Real provider remains disabled. | S4-D. | Repository code/configuration tests only. | Import boundaries, v1/v2 compatibility, selection snapshot, typed errors, parked provider; E2 with contract review. | Preserve existing media configuration. Next row requires accepted port and compatibility evidence. |
| **S6: records, access and approval** | Migration 0034; common records; owner/admin/household policy; approval service and private history foundations. | S4-A; no S3/S5 dependency. | Repository and disposable synthetic databases only. | Migration, all-route authorization, approval/version conflicts, public exclusion; E3/R3 fresh authorization review. | No deployment over old test data. Next row requires accepted access inventory and transaction evidence. |
| **S4-B: native provider runtime** | OpenAI adapter, migration 0035, durable jobs, budgets, cancellation, cleanup and credential deployment source. | S6. | Repository/fake transport only; no real key, account, network generation or host mutation. | Crash/idempotency, egress, secret handling, budget arithmetic, refusal and cleanup; E3/R3 fresh provider-boundary review. | Defaults stay disabled. Next row requires accepted provider/accounting evidence, including unknown-outcome handling. |
| **S7-P: common completion and rendering** | Atomic Q/A save, personal-history APIs, media-success/approval integration and safe document rendering. | S4-B and S6. | Repository integration only. | Duplicate completion, local-save recovery, full output, media review, approved revisions; E3/R3 focused persistence/rendering acceptance. | Preserve previous approved content on failure. Next row requires one-result/one-card and safe-rendering evidence. |
| **S8: product UI** | Shared Timeline landing, personal history, Search/Research forms, administrator review and Kronika presentation; Gallery retained. | S7-P. | Repository frontend work; no new framework or broad rename. | Node behavior tests, resource packaging, accessibility and Gallery/player regressions; E2 plus focused rendering/access review. | Stop on Gallery/player regressions. Rendered Cooperator acceptance waits for the exact NUC release. |
| **S9: integrated acceptance and transition** | Independently accepted application on the new empty catalog; separately provisioned and tested provider; household UX acceptance. | Active S4–S8 acceptances. Parked capture completion is not a gate. | Bounded acceptance/runbook work, then separate publication, read-only host preflight, exact reset/deployment and live-call grants. | E3; fresh bounded integrated application review, reset/migration evidence, provider receipts and Cooperator desktop/mobile acceptance on exact public-main NUC release. | Stop before reset on writer/object mismatch. Preserve capture/profile/state. Roll back to compatible code/database; never silently discard newly created post-transition records. Next row needs accepted public/deployed identities and complete acceptance receipts. |
| **S10: public rename** | Existing FrameNest repository becomes public Kronika; former capture repository is renamed and archived. | S9 acceptance and explicit rename/publication authority. | Separately authorized GitHub/remote/release-source transition. | E3; exact refs, history and release-source checks. | No force or history rewrite. Report partial external state if any step fails; archive former repository last. |
| **Parked capture work: S3 remainder, capture-mode S4, S5, S7-C** | Preserve capture lifecycle, source units, preparation/probe/budget code and future ZIP/capture integration. | Future explicit decision to resume; S3 login/readiness and relevant semantic ZIP evidence. | No authority in the active route. | Retain relevant regression coverage; future activation remains E3/R3 where applicable. | No browser restart, login attempt, ZIP trial, capture adapter activation or removal. These missing live proofs do not block the external research path. |

S5 retains its original identity and purpose. Existing JPEG/ZIP/budget work stays in place; it is not repurposed as external-research upload support. [Archive preparation](/home/agile/Projects/framenest/src/framenest/infrastructure/ai/chatgpt_page/archive.py:1), [budget foundation](/home/agile/Projects/framenest/src/framenest/infrastructure/ai/chatgpt_page/budget.py:15).

The capture-specific parts of original S7 remain parked: bridge submission, ZIP/media integration and capture-specific model-nullability changes. S7-P preserves the existing media provider/lifecycle instead of silently switching media to the new research provider.

This sequence explicitly replaces the old S3-ready gate before S4, S5 gate before S6 and capture-only S7 route. [Original rows](/home/agile/meta/projects/kronika/00/02-kronika-one-product/01_report_00.md:774), [current roadmap](/home/agile/Projects/framenest/ROADMAP.md:14).

## 8. Durable documentation and exactly one next grant

### S4-D documentation content

Add ADR-0083, and mark ADR-0082 as partially superseded with an exact link and retained-history explanation.

| Owner document | Required update |
|---|---|
| ADR-0083 | Provider-neutral boundary, native execution location, chosen provider, cost/retention limitations and administrator-curated publication. |
| ADR-0082 | Supersession notice for capture-only research, owner-only privacy, direct owner sharing and completion-triggered shared Timeline entry. Preserve historical reasoning. |
| ROADMAP | Revised rows, dependencies, parked capture work and separate acceptance/host grants. |
| PRODUCT | Personal Q/A history, shared-only Timeline, administrator access and household-only publication. |
| SPEC | Contracts, ownership, administrator approval, completion rules, error/resource limits and no automatic fallback. |
| SERVER | Local supervisory runtime versus hosted research loop, configuration and credential boundaries. |
| SECURITY | Revised administrator privilege, permitted text egress, untrusted output, spend controls, retention and audit routes. |
| AGENTS | Project-specific rules matching the new decisions; managed AP block unchanged. |
| README | Accepted target versus implemented state, with capture explicitly parked. |
| DEVELOPMENT | Fake-provider route, disabled defaults and declared test commands. |
| Deployment runbook | Future credential provisioning and native-provider gates, preserving the existing release helper and parked capture. |
| ADR index | Add the new decision and its partial-supersession relationship. |

Search all current authoritative wording for capture-only Search/Research, excluded external providers, administrator-private-content denial, owner direct sharing, Timeline-on-completion and obsolete S3/S5 dependencies. Classify historical occurrences rather than blindly replacing them.

No private Meta path, transcript, host value or this report is copied into public project documentation.

### Recommended next grant: S4-D only

**No further product/provider/privacy decision is required before the documentation slice.** The Cooperator made those selections during this exchange. Orchestrator acceptance and a fresh complete implementation grant remain necessary.

The following is the decision-complete issuance specification, not current execution authority:

```text
Proposed exchange coordinates: (kronika-one-product, 26, 01)
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Native planning mode: not-used
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S4-D-SUPERSEDING-DOCUMENTATION
Delivery route: manual Cooperator delivery
Independence required: no
Reasoning recommendation: High
Primary outcome: durable documentation of the accepted revised architecture
```

**Exact baseline and gate**

```text
Root: /home/agile/Projects/framenest
Branch: feat/kronika-one-product
HEAD/main/origin-main:
fd277a9a64a6965df76127dbec5b1735d2fb3cdd

Parent:
e408bb5503f359ec24542304ac1a621c6b9e4ffb

AP gitlink and submodule HEAD:
7478ddb07d2c3911f79e1aa1441f0115a31c45d8

Required state: clean index/worktree; no conflicting Git operation
```

If the baseline changes before issuance, the Orchestrator must rebind the grant explicitly.

**Exact mutation allowlist**

```text
AGENTS.md
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SERVER.md
SECURITY.md
DEVELOPMENT.md
docs/UBUNTU_NUC_DEPLOYMENT.md
docs/adr/README.md
docs/adr/0082-kronika-one-product-and-private-records.md
docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md
```

**Positive authority**

Read the relevant repository evidence and this accepted report; edit only those documents; run bounded validation; stage exact allowlisted paths; create one local commit after successful review.

**Negative authority**

No executable code, tests, dependencies, lockfiles, schema, configuration state, AP pin/managed block or upgrade-ledger changes. No source-Kronika mutation, `private/**`, credentials, provider calls, accounts, host/browser operations, fetch/push/merge/rebase/reset, publication or deployment. No subagents.

**Declared validation route**

From the FrameNest root:

```bash
./.ap/ap project check --root /home/agile/Projects/framenest --baseline fd277a9a64a6965df76127dbec5b1735d2fb3cdd

./.ap/ap exec --root /home/agile/Projects/framenest --baseline fd277a9a64a6965df76127dbec5b1735d2fb3cdd --operation test-focus -- tests/contract/test_nuc_release_docs.py -q -p no:cacheprovider

git diff --check
git diff --name-only
git diff
```

Use direct semantic/link review and the contradiction search described above. No new tests are needed for this documentation slice. `node --test` remains the declared route for later JavaScript slices; no Node run is selected here. No ambient Python or environment reconstruction is authorized. [Execution contract](/home/agile/Projects/framenest/docs/WORKER_EXECUTION_CONTRACT.md:44).

**Staging and commit**

Stage only the twelve exact paths after reviewing the complete diff. Inspect `git diff --cached --name-only`, `git diff --cached --check` and the full staged diff. Verify the AP pin and managed block are unchanged.

Create exactly one commit:

```text
docs(kronika): define modular research and administrator-curated timeline
```

Do not push. Report the commit, changed paths and final status.

**Stop conditions**

Stop on baseline/topology drift, unexpected existing ADR-0083, out-of-allowlist changes, unavailable declared execution route, failed required validation, unresolved normative contradictions, sensitive evidence exposure or any need for host/provider activity. Do not repair unrelated failures.

**Report and trace**

Return a standard English terminal report beginning `### Report for ORCHESTRATOR_CHAT`, with the proposed exchange coordinates, actual status, exact start/end commits, changed files, validation, deviations, critique and authority expiry.

```text
External trace disposition: configured
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace visibility: private
Trace archival owner: COOPERATOR

Proposed prompt archival name: 26_implementation_00.md
Proposed report archival name: 26_report_00.md
Trace directory:
 /home/agile/meta/projects/kronika/00/02-kronika-one-product

Worker report delivery: complete Markdown in chat
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
Worker trace-file write authority: none
```

This is the sole recommended next grant. Provider implementation, credential provisioning and live activation do not accompany it.

## 9. Limits, deviations and terminal assessment

**Planning PASS** means the architecture, selected policies, interfaces, slice order and next documentation grant are sufficiently specified. It is not implementation, independent security acceptance, account readiness, deployment or whole-level closure.

Material deviations from the initial prompt are explicit:

- The Cooperator changed administrator access and sharing authority during planning. Earlier owner-only privacy and direct owner sharing are superseded.
- Shared Timeline entry now requires administrator approval; completed private results remain in personal history.
- Native research places the internal agent/tool loop at the provider; FrameNest owns supervision.
- The accepted budget includes disclosed enforcement/measurement limitations. An absolute invoice cap is not claimed.
- The final report is delivered only in chat. File persistence, readback and a saved-file SHA-256 were intentionally omitted under the Cooperator’s latest delivery instruction.

Missing execution evidence remains bounded: account-specific model access, actual usage receipts, cancellation/deletion behavior, provisioned credentials, provider billing configuration and host readiness require later authorized verification. No provider API, account, credential, browser or NUC operation was performed.

```text
Orchestration critique:
MEASURED: The baseline still specifies capture-only research, no administrator
private-content override, and direct owner sharing. Current Cooperator decisions
supersede those requirements. Evidence: ADR-0082, SPEC, ROADMAP and this
conversation. Effect: implementation against the old durable rules would be
contradictory. Smallest correction: S4-D before executable changes.

LEAD: Selected model access and account-specific spend enforcement remain
unverified. Cheapest useful check: separately authorized activation preflight,
followed by the bounded synthetic acceptance route.

Resolved Execution Issues / Near-Misses:
The initial privacy clarification was misunderstood. Follow-up answers resolved
that Kronika must retain question/answer history, administrators may read all
product content, and provider retention is accepted. No affected action occurred.

Pre-existing Failure Classification:
No test failure was established. The capture login obstacle remains
Orchestrator-relayed parked-state evidence, not a failure reproduced here.

Smallest next step:
Orchestrator acceptance of this report, then issuance of the S4-D grant above.

Authority expiry:
Submission of this terminal planning report expires the current planning grant.
No implementation or autonomous continuation is authorized.
```

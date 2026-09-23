### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: kronika-one-product
Worker session ordinal: 01
Worker exchange ordinal: 01
Task identity: KRONIKA-ONE-PRODUCT-PLAN

Status: PASS — planning, under the Cooperator's revised session-delivery instruction
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Logical-whole closure: not-closed
Report justification: new-evidence

Delivery: complete Markdown report in this session
Repository changes: none
Meta changes: none
Tests, application execution, browser execution and host access: not performed
Commit and push result: not-applicable
Implementation authority: not granted
```

# Kronika: repository-grounded implementation plan

## 1. Summary and verified starting point

Build one Kronika in the existing FrameNest repository. Preserve its application, catalog, media preparation, Gallery, identity ingress and release infrastructure. Move the existing capture kernel into `src/kronika_capture`, then restore only the missing capture capabilities from the accepted Kronika source.

Implement the locked S0–S10 sequence. Each implementation grant covers one row. Fresh acceptance, host preflight, publication and deployment remain separately bounded operations within that row.

The principal work is broader than moving files:

- Replace existing administrator/publication shortcuts with record ownership and explicit household sharing.
- Make capture submission durable without automatically repeating an uncertain browser action.
- Extend analysis contracts to support capture without inventing model or reasoning information.
- Preserve one browser across jobs, bridge outages and ordinary web deployments.
- Integrate results transactionally so retries cannot create duplicate records.

This report completes planning only. The Cooperator explicitly authorized deeper planning and delivery here, replacing the original Meta-file delivery requirement.

### Verified-state table

| Evidence class | Finding | Consequence |
|---|---|---|
| Direct repository evidence | FrameNest is a standalone checkout on `feat/chatgpt-page-ask-kernel`; HEAD, local `main` and `origin/main` are `26d28b16c08a5e7e0179a32c16646bfdc1009c81`. Parent: `0fd21b989814b7c0b78d517996812750a823ff10`; tree: `f554863f18238e04203e4f22d5e20770e180045d`. | This is the primary implementation baseline. |
| Direct repository evidence | Kronika source is on `main` at root commit `66c40d43c577276b0ad304a494fbbb1ffb6fc933`; tree: `848f247434deea4c217170c012612b39e41557f3`. | Read-only source for selective restoration. |
| Direct repository evidence | Both worktrees, indexes and AP submodules were clean at the final check. Start and end commits are identical. | No implementation or normalization occurred. |
| Direct repository evidence | Both recorded AP gitlinks and checked-out AP HEADs are `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. | Preserve this pin throughout S0–S10. |
| Direct public evidence | Authorized unauthenticated ref checks matched FrameNest HEAD/main/feature at `26d28b16…` and Kronika HEAD/main at `66c40d43…`. | Public starting state matched the supplied baseline. |
| Direct repository evidence | FrameNest already contains the stripped capture kernel, provenance, deterministic JPEG/ZIP preparation, budget contracts and focused tests. Latest catalog revision is `0033_media_analysis_proposals.py`. | Extend these foundations; do not create parallel implementations. |
| Direct repository evidence | Current capture jobs are principally in memory; terminal persistence does not provide crash-safe submission idempotency. Runner bridge failures can exit through browser shutdown. Submission contains a possible second-click path. | S2 must fix these behaviors before live integration. |
| Direct repository evidence | Existing access policies include administrator read shortcuts and public-publication assumptions. Analysis validators require model information; the database caps derivatives at 16. | S6 and S7 require explicit policy and schema changes. |
| Accepted decisions | One product, private defaults, explicit family sharing, empty databases, persistent browser, one bounded ZIP, Timeline landing page, preserved Gallery and S0–S10 ordering. | Locked; not reopened by this plan. |
| Historical claims only | NUC Node/Chrome/Xvfb/VNC installation, AppArmor setup, active deployment, service accounts, Tailscale arrangement and profile condition. | Reverify through an authorized read-only host preflight. |
| Historical claims only | Rapid browser restarts correlated with challenge/profile problems. | The five-minute restart brake is operational restraint, not a claim of causation or a guaranteed remedy. |
| Engineering inference | A small SQLite capture journal and an independent capture release pointer fit the existing single-job and release architecture. | Adopt, with focused crash and deployment tests. |
| Unknown until later gates | Actual host configuration, exact database objects, browser readiness, available ChatGPT modes, ZIP image understanding and operational budget. | Fail closed at the relevant gate; do not substitute guessed values. |

Inspection was selective and repository-grounded. No test pass, live browser success, host readiness or security-audit result is claimed.

## 2. Impact map and capture transfer

Paths below are relative to the primary FrameNest repository unless explicitly identified as source paths.

### Application impact map

| Area | Existing paths | Planned changes |
|---|---|---|
| Capture package | `vendor/kronika-ask/src/kronika/**` | Move to `src/kronika_capture/**`; one implementation. |
| Packaging | `pyproject.toml` | Package `kronika_capture` from `src`; include browser assets in wheel and sdist; introduce `kronika-capture`. |
| Provenance | `vendor/kronika-ask/upstream.json` | Preserve its evidence in `docs/provenance/kronika-capture.json`, with relocation and selective-port entries. |
| Capture tests | `tests/unit/chatgpt_page/**`, `tests/chatgpt_page_protocol.test.js`, `tests/contract/test_chatgpt_page_packaging.py`, `tests/contract/test_chatgpt_page_js_syntax.py` | Update namespace and resource roots; extend behavior tests in their owning slices. |
| Import scaffolding | `tests/support/chatgpt_page_import.py`, capture `conftest.py` | Remove vendor-path injection. |
| Architectural boundaries | `tests/unit/test_import_boundaries.py`, `test_package_import.py`, `test_api_import_boundary.py` | Enforce package independence and side-effect-free imports. |
| Existing media preparation | `src/framenest/infrastructure/ai/chatgpt_page/{envelope,archive,budget,fixtures,probe,receipt,errors}.py` | Keep in FrameNest; extend fixtures and integration only. |
| Record domain/application | `src/framenest/domain`, `src/framenest/application`, `src/framenest/application/ports` | Add record, document, access-policy and capture-request contracts. |
| Persistence | `src/framenest/infrastructure/persistence/catalog_schema.py`, existing media/upload/analysis repositories | Add common records and durable application capture bindings; atomically establish ownership. |
| Migrations | `src/framenest/infrastructure/persistence/alembic_environment/versions/` | Append `0034_kronika_records.py`, then `0035_capture_analysis_contract.py`. |
| Composition/configuration | `src/framenest/adapters/api/application.py`, `src/framenest/configuration.py`, `src/framenest/server.py` where necessary | Wire repositories, capture client, lifecycle and configured local owner. |
| HTTP authorization | `src/framenest/adapters/api/tailscale_ingress.py`, `content_audience_api.py`, existing content routers | Register exact routes and enforce record access consistently. |
| New API | `src/framenest/adapters/api/{timeline_api,records_api,capture_requests_api,capture_admin_api}.py` | Timeline, records, sharing, Search/Research and operational capture status. |
| Web shell | `src/framenest/adapters/api/web/{index.html,app.js,styles.css}` | Timeline landing, Search/Research forms and details, sharing controls, admin status; retain Gallery. |
| Release mechanism | `deploy/ubuntu/framenest-release`, `deploy/ubuntu/framenest_release.py` | Extend the existing release workflow with separately controlled capture runtime activation. |
| Service sources | `deploy/systemd/framenest.service` and new `kronika-capture-*` units | Separate web, bridge, persistent browser runner, Xvfb and temporary operator view. |
| Current product truth | `AGENTS.md`, root product/security/server/development documents, deployment runbook and ADR index | Record the approved architecture in S0; update implementation claims only as corresponding slices land. |

### Exact kernel relocation

For every relative path below:

```text
FROM vendor/kronika-ask/src/kronika/<relative-path>
TO   src/kronika_capture/<relative-path>
```

```text
__init__.py
__main__.py
cli.py
client.py
config.py
errors.py
paths.py
projects.py
bridge/__init__.py
bridge/auth.py
bridge/jobs.py
bridge/results.py
bridge/server.py
bridge/store.py
_assets/extension/src/adapters/adapter.js
_assets/extension/src/adapters/pack_v5.json
_assets/extension/src/engine/dom_engine.js
_assets/extension/src/engine/index.js
_assets/extension/src/engine/interventions.js
_assets/extension/src/protocol.js
_assets/extension/src/url_guard.js
_assets/extension/src/headless/bridge_client.mjs
_assets/extension/src/headless/cdp_client.mjs
_assets/extension/src/headless/driver.mjs
_assets/extension/src/headless/job_engine.mjs
_assets/extension/src/headless/login_server.mjs
_assets/extension/src/headless/probe.mjs
_assets/extension/src/headless/resource_policy.mjs
_assets/extension/src/headless/runner.mjs
_assets/extension/src/headless/login_app/app.css
_assets/extension/src/headless/login_app/app.js
_assets/extension/src/headless/login_app/index.html
```

S1 performs relocation and namespace changes only:

- Change Python imports and `importlib.resources.files("kronika")` to `kronika_capture`.
- Keep the distribution and internal application package named `framenest`.
- Change Poetry package and asset inclusion to the new source root.
- Set `kronika-capture = "kronika_capture.cli:main"`.
- Retain `framenest-chatgpt-page` as a documented compatibility entry point to that same function. It is an alias, not another implementation.
- Preserve argv/stdin prompt input, text stdout and rejection of CLI `-f`/`--file`.
- Remove vendor-path test scaffolding and update JavaScript asset imports.
- Keep capture independent of FrameNest application/domain/persistence. The application later communicates with capture over the bridge.

**Vendor retirement gate:** first verify the relocated package and packaged assets; then remove the old executable tree and run the focused checks again against the final tree. Commit only a tree with one implementation. Preserve provenance outside `vendor/` before removing its manifest.

### Provenance format

Create `docs/provenance/kronika-capture.json` with:

```text
schema_version
upstreams:
  repository identity
  full source commit
  source tree
files:
  source path
  source blob
  destination path
  disposition: relocated | selectively-ported | adapted
  feature
  adaptation summary
excluded_features:
  source location
  exclusion reason
```

Retain the original vendor manifest information. Relocated, already-modified files identify both the original Kronika origin and the FrameNest baseline containing the adaptation. Selective function restoration names the source file and functions. Do not introduce private checkout paths or circular “current commit” fields.

### Selective S4 restoration

Source is fixed at Kronika `66c40d43c577276b0ad304a494fbbb1ffb6fc933`.

| Source | Destination/use |
|---|---|
| `extension/src/headless/deep_research.mjs` | `src/kronika_capture/_assets/extension/src/headless/deep_research.mjs`; bounded research observation and export. |
| Relevant Web Search and Deep Research portions of `extension/src/headless/job_engine.mjs` | Merge into the relocated job engine without replacing S2 submission safeguards. |
| Mode dispatch/capability portions of `extension/src/headless/runner.mjs` and associated protocol/error handling | Restore only required mode behavior. |
| `src/kronika/markdown.py` | `src/kronika_capture/markdown.py`; bounded rendering. |
| `src/kronika/sanitize.py` | `src/kronika_capture/sanitize.py`; adapt to complete-result rendering without external resources. |
| Relevant cases in `tests/unit/test_headless_deep_research.py` and `test_headless_runner.py` | Extract fake-driver/CDP scenarios into FrameNest’s existing Node test route. |
| Source Markdown/sanitizer tests | Port relevant cases into `tests/unit/chatgpt_page/test_markdown.py` and `test_sanitize.py`. |
| Source job-mode tests | Port only Search/Research request, completion and failure contracts. |

Do not port the source family library, accounts, manager, library-aware `bridge/results.py`, manager rendering, MV3 job runner or asset-capture subsystem. Preserve complete text/Markdown without downloading embedded images.

## 3. Technical decisions

These are recommended implementation decisions within the locked direction. Accepting this plan accepts these defaults; later Workers do not choose alternatives silently.

| Decision | Recommendation and evidence | Cost/test bound | Rejected alternative | Invalidation/stop condition |
|---|---|---|---|---|
| Package layout | Sibling `src/framenest` and `src/kronika_capture`; existing kernel already self-contained. | Import, wheel/sdist and asset tests; no new dependency. | Separate repository/package manager or copied second kernel. | Packaging cannot produce one complete implementation. |
| Vendor retirement | One relocation commit; final tree contains no executable vendor copy. | Verify before and after removal. | Indefinite dual-tree compatibility. | Remaining imports/resources depend on vendor. |
| Provenance | Versioned JSON under `docs/provenance`. | Every moved file and restored feature has source evidence. | Git-history import or prose-only attribution. | Missing source/blob attribution. |
| Durable capture state | Standard-library SQLite journal behind the existing `JobManager`. | Crash/recovery and capacity tests; at most 256 retained jobs. | In-memory authority or a second queue. | Persistence cannot precede acknowledgement and send permission. |
| Submission safety | Durable send-intent barrier, one click, explicit runner/job identity. | Fault injection before/after every submission boundary. | Re-click after missing DOM acknowledgement. | Send outcome cannot be established: terminal `E_AMBIGUOUS_SEND`. |
| Browser lifecycle | Runner owns one headed Chromium on persistent Xvfb. | Fake-driver lifecycle tests, then bounded live evidence. | Browser per job or restart-on-error loop. | Lost browser/profile readiness requires operator intervention. |
| Research export | Restore bounded source helper and full report export. | Fake CDP admission, export, cancellation and size-bound cases. | Treating a preview/summary as the finished report. | Required mode/export unavailable or incomplete. |
| Attachment transport | Binary upload to existing bridge; server-owned immutable ZIP staging. | Adversarial archive and cleanup tests; two bounded synthetic live trials. | Client filesystem paths, arbitrary files or ZIP extraction. | Invalid archive or absent semantic/budget proof. |
| Common records | SQLAlchemy Core tables in the existing catalog; append migrations. | Empty and previous-schema migration tests, uniqueness and transactions. | Second family database or migration-history reset. | Existing media can be inserted without ownership. |
| Authorization | Central record policy plus query-level filtering and exact route registration. | Two-user/admin/direct-file negative tests. | Administrator implies private-content read access. | Any bypass remains. |
| Capture analysis metadata | Capture has `provider_id="chatgpt-page"` and no model/reasoning value. | Validators, serialization and migration tests. | Fake model names or invented reasoning flags. | Consumer still requires or exposes fabricated values. |
| Timeline | Query common records, keyset pagination, existing shell. | Stable ordering, filtering and Gallery regressions. | Client-side ACL filtering or a second frontend. | Pagination/counts leak inaccessible records. |
| Deployment | Extend existing release helper; independent capture pointer into its releases. | Release/source contracts and restart-count checks. | Second deploy system or coupling browser to web service. | Web deployment changes browser instance. |
| Database reset | Exact discovered database/WAL/SHM objects after writers stop. | Preflight inventory and post-reset empty-schema verification. | State-directory deletion or old-data import. | Ambiguous path, symlink, unexpected writer or scope expansion. |
| Git topology | Sequential S0–S10 work on one feature branch; accepted publication through normal `main`. | Clean baseline/refs at every grant. | History rewrite, source-history merge or automatic publication. | Baseline drift or unaccepted candidate. |

## 4. Capture service contracts

### 4.1 Browser and job state

Keep service readiness separate from job status.

```text
Service:
  starting -> ready
  ready -> needs_admin | browser_unavailable
  needs_admin -> explicit resume -> readiness check -> ready
  browser_unavailable -> authorized manual recovery -> readiness check

Job:
  queued -> offered -> running -> done | failed | cancelled
                       |
                       +-> needs_admin -> safe continuation
                                        or failed/cancelled
```

A paused job retains the only active slot.

Persist the job phase, runner instance, offer identity, submission state and intervention timing. Submission states distinguish:

```text
not_started
send_intent_persisted
send_confirmed
```

Before any send action, the runner must receive acknowledgement that send intent was durably recorded. If this write fails, it must not click Send.

Remove the existing second-click retry. A missing acknowledgement after a click is not evidence that nothing was sent.

Safe continuation rules:

- Before send, resume only when the same job/page phase is known and readiness passes.
- After confirmed send, continue observing the same identified response where that association remains provable.
- Never submit again to recover an uncertain response.
- Lost association, uncertain click or ambiguous crash recovery ends with `E_AMBIGUOUS_SEND`.
- Repeated result delivery may be retried with the same job/result identity; browser execution may not.

A bridge restart reconciles its journal before accepting work. Uncertain in-flight jobs become typed failures. A durably queued job that was never offered may remain queued. Old offers cannot be executed after their runner/offer identity is invalidated.

Cancellation and timeout never trigger resubmission. If stopping the current page activity cannot be confirmed, service readiness remains blocked even after the job becomes terminal.

### 4.2 Readiness and administrator intervention

Readiness examines bounded structural evidence on the runner-owned page:

- Browser/CDP connection and owned target exist.
- Allowed page origin is correct.
- Composer and required mode controls are available.
- No login, consent, Turnstile or service-limit state blocks work.
- No previous generation remains ambiguously active.

Do not inspect model/reasoning controls, unrelated tabs, history or profile contents.

`needs_admin` records a typed reason, job ID, phase and elapsed wait. Administrator status exposes operational metadata only; another owner’s prompt, answer, title and source URL remain private.

An explicit resume invokes readiness again. It is not a blind state reset.

The cumulative administrator wait per job is limited to 1,800 seconds and excluded from active-response timeout accounting. Expiry produces `E_INTERVENTION_TIMEOUT`, ends the job and cleans its attachment; it does not terminate Chromium.

### 4.3 Process lifecycle

- Ordinary jobs reuse the same browser process and owned page context.
- Bridge transport failure causes capped reconnection backoff while Chromium remains alive.
- A browser crash blocks service readiness. No automatic browser restart occurs.
- Keep the runner service out of web-service restart dependencies.
- Enforce at least 300 seconds between browser starts using persisted launch metadata outside the profile and an exclusive launch lock.
- A backward clock or unverifiable last-start state must not bypass the brake.
- A problematic profile is not replaced automatically.

The current driver reads `DevToolsActivePort` from the profile. Replace that with bounded in-memory parsing of Chromium’s emitted DevTools endpoint. Discard unrelated browser stderr; do not log it. This removes application reads from profile contents.

Use an explicitly configured, preflight-verified Chromium executable. Do not enable stealth or weaken its sandbox.

### 4.4 Bridge endpoints and wire contract

Preserve existing compatible job fields and response names.

| Endpoint | Contract |
|---|---|
| `POST /v1/attachments` | Authenticated binary `application/zip`; returns server `attachment_id`, SHA-256, byte/frame counts and expiry. |
| `POST /v1/jobs` | Existing JSON fields plus application-required `request_id`; existing successful HTTP 200 response extended with status and request identity. |
| `GET /v1/jobs/{job_id}` | Status, timestamps, intervention metadata and terminal result. |
| `POST /v1/jobs/{job_id}/cancel` | Idempotent cancellation request; repeated terminal cancellation does not change the result. |
| `GET /v1/status` | Authenticated service readiness, supported capabilities, opaque browser-session identity, adapter identity and active-job metadata. |
| `POST /v1/resume` | Authenticated explicit resume with expected job/intervention identity; readiness check required. |
| Existing runner endpoints | Extend `/v1/hello`, `/v1/next`, job events and result submission; retain one manager. |

Example application request:

```json
{
  "request_id": "server-generated-uuid",
  "prompt": "Task text",
  "files": [],
  "new_chat": true,
  "timeout_s": 600,
  "project": null,
  "mode": "web_search"
}
```

`files` remains a list of server attachment IDs, not paths. Modes are `null` for ordinary ask, `"web_search"` and `"deep_research"`. Search/Research require zero attachments; media asks permit one ZIP.

Preserve existing timeout bounds: default 600 seconds, maximum 3,600 seconds. Administrator waiting has its separate limit.

Terminal success retains:

```json
{
  "answer": "Complete captured text",
  "markdown": "Optional complete Markdown",
  "html": "Optional sanitized HTML",
  "url": "Optional source URL",
  "error_code": null
}
```

Optional fields are absent/null when unavailable. Never claim a truncated result as complete. Oversized complete output produces a typed failure; a rendering-bound failure may fall back to escaped full text.

The runner-only offer may resolve attachment IDs to validated server-owned paths. Public job/status responses never return staging paths.

### 4.5 Idempotency and journal

- Use a server-generated application UUID as `request_id`; the CLI also generates an ID for its request.
- Canonicalize defaults and immutable request content. Preserve prompt whitespace. Compare attachment content by its recorded digest and size.
- Identical request/content returns the original job, including after completion or while service readiness is blocked.
- Different content under the same ID returns `E_IDEMPOTENCY_CONFLICT`.
- Resolve known retries before applying busy, readiness or capacity checks.
- Persist admission before acknowledging it.
- Keep active jobs and retain terminal jobs/results for 24 hours after termination.
- Maximum retained job count is 256. Do not evict unexpired entries to admit another job.
- Journal failure blocks admission/submission; do not swallow persistence errors.
- Bound operational events; do not store unbounded DOM snapshots or progress text.

The journal is transient capture coordination state, not another family library.

### 4.6 Errors and authentication

Use the existing error envelope:

```json
{
  "ok": false,
  "error": {
    "code": "E_BUSY",
    "step": "admission",
    "message": "A task is already active."
  }
}
```

Messages are fixed, safe summaries.

| Condition | Code |
|---|---|
| Browser unavailable | `E_BROWSER_UNAVAILABLE` |
| Intervention required | `E_NEEDS_ADMIN` |
| Active/paused job exists | `E_BUSY` |
| Provider limit | `E_LIMIT_REACHED` |
| Journal/staging capacity | `E_SERVICE_LIMIT` |
| Invalid ZIP | `E_ATTACHMENT_INVALID` |
| Oversized ZIP/frame | `E_FILE_TOO_LARGE` |
| Missing/expired attachment | `E_ATTACHMENT_MISSING` |
| Upload failure | `E_UPLOAD_FAILED` |
| Active response timeout | `E_RESPONSE_TIMEOUT` |
| Administrator wait expired | `E_INTERVENTION_TIMEOUT` |
| Cancellation | `E_CANCELLED` |
| Conflicting request identity | `E_IDEMPOTENCY_CONFLICT` |
| Uncertain send | `E_AMBIGUOUS_SEND` |
| Required mode unavailable | `E_WEB_SEARCH_UNAVAILABLE`, `E_DEEP_RESEARCH_UNAVAILABLE` |
| Unacceptably large complete result | `E_RESULT_TOO_LARGE` |
| Application recovery after result-retention expiry | `E_RESULT_EXPIRED` |
| Durable-state failure | `E_JOURNAL_UNAVAILABLE` |

Use HTTP 400 for malformed input, 413 for size rejection, 409 for busy/conflict, 429 for capacity/service limits and 503 for unavailable service. Terminal job failures remain available through successful status reads.

Bind only `127.0.0.1`, default port 8765. Keep exact Host validation, absent-or-exact approved loopback Origin, constant-time token comparison and no wildcard CORS. The existing unauthenticated health endpoint may expose only liveness/protocol identity; readiness remains authenticated.

### 4.7 Search/Research completion and rendering

Restore actual mode selection and mode-specific completion. Unavailable mode is a failure, never fallback to ordinary ask.

Deep Research observation remains constrained to the owned ChatGPT page and the source helper’s explicitly allowed research-frame ancestry. Keep its bounded depth/session admission. Unrelated frames receive no evaluation.

Export the completed report through the existing bounded mechanism. Temporary page-local clipboard interception must be restored; do not read the system clipboard, navigate unrelated pages or download assets. Export/cleanup failure blocks a claimed successful result.

Preserve full text and Markdown. Sanitized HTML must contain no scripts, event handlers, external resources, embedded frames or active URL schemes. If safe rendering exceeds its bounds, render escaped full text rather than a misleading partial document.

## 5. ZIP attachment and verified budget

### Validation before browser contact

Stream the binary request into private staging, enforcing the byte ceiling while receiving it. Reject unsupported transfer framing and ambiguous lengths. Do not run the ZIP body through the existing JSON request parser.

Accept only:

```text
One ZIP
Archive <= 32 MiB
1..256 members
Each member <= 128 KiB
JPEG long side <= 480 px
ZIP_STORED
Names exactly frame-0001.jpg, frame-0002.jpg, ...
```

Reject encryption, compression, ZIP64, directory entries, paths, duplicates, gaps, symlink entries, nested archives, non-JPEG payloads and malformed/truncated data. Validate the whole ZIP structure and each JPEG by decoding, including actual dimensions. Reject undeclared/trailing payload and unsupported archive metadata.

Do not extract members. Feed the validated original ZIP to the browser file input using only its server-owned path. Confirm upload completion before submission; failure before send must not send the prompt.

### Staging lifecycle

Use `/var/lib/kronika-capture/staging`:

- Root and per-upload directories: `0700`; files: `0600`.
- Server-generated identifiers only; create exclusively without following symlinks.
- At most four unbound uploads, additionally bounded by total staged bytes.
- Unbound lifetime: 15 minutes.
- Bind atomically to one job. An attachment cannot be claimed by another job.
- Bound upload remains until terminal completion, failure or cancellation.
- Cleanup reconciles journal ownership and only removes recognized service-owned staging objects.
- Unexpected owners, types or symlinks stop that cleanup action; never recurse through them.

### Budget integration

Keep existing preparation in `framenest.infrastructure.ai.chatgpt_page`. Do not copy it into capture.

Preserve the existing calculation:

```text
B = floor(0.8 * min(Lzip, Ltotal, 32 MiB))
Nbytes = largest frame count whose worst-case bytes and exact ZIP overhead fit B
N = min(Nbytes, floor(0.8 * R))
```

Enforce the absolute 256-frame ceiling as well. Video requires `N >= 12`; reject otherwise. Retain existing JPEG envelope choices and metadata-stripping behavior.

The application validates budget identity against the current adapter pack and opaque browser-session identity. A capture runtime/session change invalidates stale evidence. A new attachment-limit failure invalidates the accepted budget. Never infer capabilities from a model name.

### Synthetic live gate

After independent file-boundary acceptance and a separately authorized live grant, run at most two capture trials:

1. **Byte-capacity trial.** Generate valid synthetic JPEG frames using the existing envelope. Choose the smallest fixture archive large enough to support the worst-case 12-frame budget after the 20% margin, within all absolute limits. Successful upload/completion establishes only measured lower bounds for `Lzip` and `Ltotal`.
2. **Image-understanding trial.** Send 15 synthetic frames containing independently generated visible identifiers, colors and ordering information. Expected answers exist only in the local fixture oracle, not in filenames or prompt text. Require correct image-derived answers for every frame. This establishes `R = 15`, allowing an operating count of 12 if the byte bound also qualifies.

Record fixture identity, byte/frame counts, adapter/session identity and pass/fail evidence without account data or real media.

If either trial fails, quota is unavailable or a challenge appears, stop. No automatic retry, model change, challenge bypass or relaxation below 12 frames. Real media analysis remains disabled.

## 6. Common records, ownership and application integration

### 6.1 Database additions

Use existing SQLAlchemy Core and Alembic conventions.

`0034_kronika_records.py` appends:

| Table | Required contents and constraints |
|---|---|
| `kronika_records` | UUID ID; kind `media/search/research`; exactly one appropriate media/document reference; non-null normalized owner login key; visibility `private/family`, default private; creation time; nullable first timeline-entry time; display name; nullable latest successful analysis reference. Unique media reference ensures one record per medium. |
| `kronika_documents` | Stable ID; complete text; optional complete Markdown; optional sanitized HTML; optional source URL; creation time. |
| `kronika_capture_requests` | Stable application request ID; owner; client submission nonce; task kind; request fingerprint; bridge job binding; lifecycle/error state; optional media/analysis-run association; final record/document binding. Unique submission and completion bindings. |

Indexes support owner/visibility filtering, timeline ordering and request recovery. Foreign keys prevent orphan references.

There is no historical backfill or data import. Pre-existing unowned media is inaccessible under the new record policy until the authorized empty-database reset; it is not silently assigned to the administrator.

Media insertion and private record creation share one transaction. Cover all existing insertion routes, including upload publication, direct import and requester acquisition. A process without verified/configured ownership cannot create a new media record.

### 6.2 Ownership and sharing

- Remote owner comes from the existing verified `IdentityContext.login_key`.
- Ignore/reject client-supplied ownership fields.
- Local administrative creation requires `FRAMENEST_LOCAL_OWNER_LOGIN`, normalized and explicitly mapped through existing identity configuration.
- No “first administrator” or anonymous owner fallback.
- `private`: owner reads content.
- `family`: owner and explicitly mapped household members read content.
- Only the owner changes visibility or mutates record content, subject to existing action capabilities.
- Administrator operational privileges do not grant private-content access.
- Unknown/unmapped identities receive no family access.

New records always start private. Sharing is a distinct owner mutation; upload/analysis/request creation cannot set family visibility.

Use the record policy in database queries before filtering counts and pagination. Missing record context denies access. Remove production use of permissive `policy=None` behavior.

Cross-owner duplicate detection must not expose an existing private item. Preserve separate ownership and use silent separate cataloging across owners, including when the requester is an administrator.

### 6.3 Access-path inventory

The S6 permission audit and tests must cover these existing and new surfaces:

| Surface | Required enforcement |
|---|---|
| Timeline, record search and record detail | Accessible records only; no hidden counts, snippets or titles. |
| Gallery/workspace/admin media lists | Scope before pagination; administrator list is not a private-content bypass. |
| Media detail, metadata and aliases | Resolve owning record first. |
| Original content, Range playback and downloads | Authorize before opening/streaming bytes. |
| Gallery previews, covers, thumbnails and timeline frames | Same record policy; guessed location/cover IDs do not bypass it. |
| Analysis status/history, proposals and suggestions | Private result access follows record ownership/sharing; mutations require owner authority. |
| Companion inbox/history/detail/opened/apply | Scope records and results; do not preserve the current administrator-wide private-content view. |
| Upload status, completion and duplicate handling | Owner access; operational administration exposes no uploaded content. |
| YouTube/X requester and administrator acquisition routes | Preserve requester ownership and enforce record access after cataloging. |
| Library scan/import and path-based analysis previews | Restrict to the configured local-owner workflow or an authorized owned record; reject path-based access to another owner’s content. |
| Tag/creator facets, autocomplete and counts | Accessible usage only, apart from explicitly shared vocabulary; no private derived names/counts. |
| Publication and public content routes | Reject/omit all new Kronika records. |
| Search/Research create/status/cancel/result | Request owner only until a completed record is explicitly shared. |
| Capture administration | Operational metadata and explicit resume only; no general content read override. |

The public-published composition stays disabled. Family sharing never inserts a `media_content_publications` row. Defense-in-depth public queries also exclude Kronika records if an erroneous publication row exists.

### 6.4 Timeline entry and analysis

On successful, schema-validated analysis, one transaction:

1. Persists the successful analysis result and existing proposal/review data.
2. Updates the medium’s latest successful analysis reference.
3. Sets first timeline-entry time only if it is currently null.

Reanalysis never changes that first time, creates another card or resets sharing. Failure preserves the earlier successful result and timeline position. Metadata suggestions still require the existing human approval flow.

Search/Research completion creates the document, record and final capture binding in one transaction. Incomplete output and failed jobs create no timeline record.

### 6.5 Capture-compatible analysis contract

Current analysis code requires model metadata and constrains derivative count. S7 must change this explicitly.

Append `0035_capture_analysis_contract.py`:

- For `provider_id="chatgpt-page"`, permit `model_id` and `reasoning_enabled` to remain null.
- Permit capture derivative counts up to 256.
- Preserve existing stricter contracts for legacy HTTP providers.
- Update `MediaSuggestion`, movie-identification contracts, serializers and analysis-run validation consistently.
- Never insert placeholders such as a fabricated model ID or `reasoning_enabled=true`.

The Kronika application composition selects capture for the workflows in this plan. Retained HTTP-provider code is not an automatic fallback. The capture UI exposes service capabilities/readiness, not model or reasoning selectors.

### 6.6 Application client and durable completion

Add a pure application port and one HTTP implementation under the existing `infrastructure/ai/chatgpt_page` package. Do not import capture internals into application/domain code.

Before network submission, persist the application request identity and content fingerprint. Do not hold a database transaction during HTTP or browser work.

Recovery behavior:

- A lost create response is retried only with the same `request_id` and content.
- Repeated polling/result delivery uses the existing application binding.
- Crash after bridge completion but before local commit recovers the same result.
- Concurrent completions are serialized by unique constraints and a transaction.
- After the bridge retention horizon, an unresolved request becomes `E_RESULT_EXPIRED`; do not submit a fresh request automatically.
- `E_AMBIGUOUS_SEND` is terminal and requires an explicit operator decision for any new attempt.

The application coordinator tracks its requests; it is not another browser queue. Interactive `E_BUSY` is returned promptly. Any existing analysis scheduling waits only before known admission and never changes identity to bypass uncertainty.

### 6.7 Application APIs

Register all routes in the existing exact permission table and existing mutation protection.

| Route | Behavior |
|---|---|
| `GET /api/timeline` | Accessible entered records; default 24, maximum 100; cursor pagination. |
| `GET /api/records/{record_id}` | Authorized record/detail metadata. |
| `GET /api/records/{record_id}/render` | Authorized isolated sanitized document HTML. |
| `PATCH /api/records/{record_id}/visibility` | Owner-only `{ "visibility": "private" \| "family" }`. |
| `POST /api/capture-requests` | `{kind: search/research, prompt, client_request_id}`; server derives owner and bridge request ID; HTTP 202 on accepted work. |
| `GET /api/capture-requests/{request_id}` | Owner-only job state and completed record reference. |
| `POST /api/capture-requests/{request_id}/cancel` | Owner-only cancellation. |
| `GET /api/admin/capture/status` | Authorized operational status without private content. |
| `POST /api/admin/capture/resume` | Explicit intervention identity and readiness check. |

Timeline order is `timeline_entered_at DESC, id ASC`. Cursor contains both values. Filters combine record kind with existing media categories; use OR within a facet and AND between facets. GIF remains a technical format. A bounded text query searches only accessible records; no new search dependency is needed.

Use the existing trusted Tailscale UDS ingress, exact mutation Origin check and `X-FrameNest-Request` protection. Do not replace existing headers or port Kronika local login accounts.

## 7. UI and operations

### 7.1 Existing-shell UI

Use the current dark/green visual system, controls, dialogs, cards and responsive behavior.

- Timeline becomes the landing screen.
- Gallery remains a separate working view, including accessible media awaiting analysis.
- Media cards open the existing detail/player.
- Search and Research have separate request entry points and archived-result details.
- Work-in-progress, intervention and error states stay in the working interface.
- Cards show record kind, title, entry time and visibility.
- Owners receive explicit Share with family / Make private controls.
- Preserve image rendering, GIF behavior, playback handoff and metadata-review flows.

Render archived document HTML in a sandboxed same-origin frame served by the authorized render endpoint. The document uses restrictive CSP, no scripts, no external resources, no-referrer and no-store. Do not inject generated HTML into the main application DOM.

Preserve complete text/Markdown independently from presentation. Validated source links can be exposed as explicit user actions outside the sandbox; rendering does not fetch them.

### 7.2 Capture account and services

Use:

```text
Account:                 kronika-capture
Private state:           /var/lib/kronika-capture
Profile:                 /var/lib/kronika-capture/profile
Journal:                 /var/lib/kronika-capture/capture-journal.sqlite3
Staging:                 /var/lib/kronika-capture/staging
Runtime directory:       /run/kronika-capture
Nonsecret configuration: /etc/kronika-capture/capture.env
Capture release pointer: /opt/framenest/capture-current
Existing web pointer:    /opt/framenest/current
Budget state:            /var/lib/framenest/chatgpt-page/budget.json
```

These are planned deployment paths; host preflight must verify their suitability before creation.

Provide source units:

```text
kronika-capture-xvfb.service
kronika-capture-bridge.service
kronika-capture-runner.service
kronika-capture-vnc.service
kronika-capture-view.service
```

Rules:

- Xvfb and runner have no automatic restart loop.
- Bridge may restart independently; runner reconnects.
- No `PartOf=framenest.service` coupling for capture.
- Runner and Xvfb share the required display socket and restricted Xauthority; avoid incompatible private `/tmp` namespaces. Do not use unauthenticated `-ac`.
- Browser debugging remains loopback-only.
- VNC/noVNC are normally stopped, loopback-only and time-limited to at most 30 minutes.
- Default view ports are 5900 and 6080; a preflight collision stops setup rather than silently selecting a public/random listener.
- The Cooperator opens the view through an SSH tunnel. Agents neither view authentication screens nor enter credentials.

Create the per-install bridge token through the authorized setup mechanism and deliver it to the web, bridge and runner using systemd credentials. Do not grant the web account access to the browser profile by adding it to a shared state-reading group. Never place the token in frontend configuration, command-line arguments or logs.

### 7.3 Existing release helper extension

Keep `deploy/ubuntu/framenest-release` as the sole entry point and preserve its pinned deployment tooling.

Extend release manifests with capture-runtime identity derived from:

- Packaged capture code/assets.
- Relevant installed runtime dependencies.
- Capture unit/runtime configuration contracts.

Normal web deploy/rollback changes only the web pointer and service.

Add an explicit capture activation option to the same helper. It must:

1. Verify the exact accepted release and compatible bridge protocol.
2. Drain active capture work; refuse a live or paused job.
3. Enforce the restart brake.
4. Switch `capture-current` and perform one planned runner/browser restart.
5. Verify readiness without automatically retrying a failed browser launch.

Retain any release referenced by either active pointer. Report both SHAs. A web rollback must not accidentally downgrade or restart capture.

Capture rollback is a separate deliberate transition subject to the same brake. Failed readiness must not cause a rapid automatic “rollback restart.”

Preserve the existing `migration-required` continuation. The release helper must not start performing implicit schema migrations or database deletion.

### 7.4 Logging and profile ownership

Allow operational fields such as event name, opaque job/request ID, status, duration, byte/frame counts and typed error code.

Do not log prompts, answers, DOM, media, source URLs, account identities, token material, profile paths/content or raw browser/provider exceptions. Review current exception logging and runner error propagation accordingly.

Only the Cooperator backs up or restores the browser profile, with Chromium correctly stopped, as an opaque local operation. Neither application nor agents copy profile contents. No automatic profile replacement is implemented.

## 8. S0–S10 implementation and acceptance

### Common grant rules

Every grant binds an exact current commit, clean-state expectation, changed paths, declared execution route and evidence destination.

Positive authority is restricted to the row. Source Kronika remains read-only until the explicitly authorized S10 remote transition. Host actions, real ChatGPT calls, publication, database reset and GitHub rename are never implied by a code-edit grant.

Each row requires its named focused tests plus relevant existing contracts. A failed gate stops advancement. Corrections remain within the same row and receive renewed independent acceptance where the affected boundary requires it.

For affected existing integration files, the mechanical allowlist is:

> Only files implementing the explicitly enumerated routes, their ownership/access-policy services, and directly required port/repository/composition call sites may change. Edits are limited to carrying verified identity, scoping access, atomic ownership/result persistence and the stated contract adaptation. The Orchestrator expands this rule into a concrete path list against the grant’s baseline before issuance.

This rule does not permit adjacent refactoring.

### S0 — Record one-product architecture

**Outcome:** current FrameNest documentation clearly records the approved future Kronika architecture and distinguishes it from implemented behavior.

**Exact allowlist:**

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
```

Content changes:

- ADR-0082 records one repository/product, application/capture ownership, process boundary, selective transfer, common catalog, private defaults, explicit sharing and empty-database transition.
- PRODUCT/SPEC record Timeline, Search/Research, entry rules and scope exclusions.
- SERVER/SECURITY record trusted identity, administrator limits, public exclusion, capture token/browser boundaries and safe rendering.
- ROADMAP records S0–S10 and gates.
- README explains the accepted transition without claiming new features are implemented.
- DEVELOPMENT and deployment documentation describe the intended single release route and later host gates.
- AGENTS changes only project-specific product/security guidance outside the managed AP block.
- Preserve old ADRs and host baseline facts as history; link the superseding decision rather than rewriting past observations.

**Authority/host class:** documentation only; no host preflight or mutation, code, packaging, AP, ledger or branding sweep.

**Checks:** exact diff allowlist; contradiction search for live two-product claims, Gallery-versus-landing wording, old database/import claims, administrator access and public publication. Verify unchanged AP pin and historical sources.

**Tier/acceptance:** E0/E1, documentation-focused R0; Orchestrator review, Cooperator acceptance of recorded direction.

**Recovery/stop:** revert only the documentation candidate if rejected. Stop on any need to change locked direction or claim unverified host behavior.

**Evidence before S1:** accepted documentation commit, contradiction checklist and unchanged pin.

### S1 — One capture package

**Outcome:** the existing kernel is packaged once under its final namespace.

**Allowlist:** the exact relocation map; `pyproject.toml`; provenance manifest; capture import scaffolding; existing capture packaging/protocol/CLI/security/limit tests; the three named import-boundary tests.

**Dependencies:** accepted S0.

**Authority/host class:** repository packaging/refactor only; no restored modes, new job semantics, dependency addition or host mutation.

**Checks:** existing capture unit tests; `test_chatgpt_page_packaging.py`; `test_chatgpt_page_js_syntax.py`; `chatgpt_page_protocol.test.js`; import boundaries; wheel/sdist resource inventory and entry-point checks.

**Tier/acceptance:** E2; focused provenance/build review using R3 scope, with current-Worker checks labelled non-independent.

**Recovery/stop:** discard/revert the candidate before deployment if packaging or provenance fails. Never commit a partially retired duplicate.

**Evidence before S2:** one executable implementation in source and distribution, complete provenance and accepted focused results.

### S2 — Durable submission and persistent browser

**Outcome:** one browser survives normal jobs and bridge outages; uncertain sends cannot repeat.

**Allowlist:** capture `bridge/{jobs,server,store}.py`, new `bridge/journal.py`, `config.py`, `errors.py`, `client.py`, relevant CLI readiness/resume handling, runner/driver/bridge-client/job-engine/protocol/intervention assets; focused lifecycle/journal/security tests.

**Dependencies:** S1.

**Authority/host class:** repository code and fake-driver tests only. No host/browser/login execution.

**Checks:** new `tests/capture_lifecycle.test.js`; journal/admin/readiness tests under `tests/unit/chatgpt_page`; existing protocol/security/limits. Inject failures around admission, offer, send intent, click, result and journal recovery.

**Tier/acceptance:** E3; fresh independent targeted lifecycle/provider/authentication review before acceptance.

**Recovery/stop:** retain prior released behavior; do not deploy the candidate if any path can re-click, restart Chromium on bridge loss or acknowledge unpersisted work.

**Evidence before S3:** independent report proving single launch, reconnect, pause/resume, timer separation and no automatic resend.

### S3 — NUC capture foundation

**Outcome:** the accepted capture runtime can run separately from the web service.

**Allowlist:** existing release helper pair; new capture unit/configuration source files; capture credential/launcher integration; deployment documentation; existing `test_nuc_release_*` contracts and new capture-service contract tests.

**Dependencies:** S2 acceptance.

**Authority/host class:** E3 service/account/filesystem setup. First a repository implementation grant; then a separate read-only NUC preflight and bounded host setup/deployment grant.

**Preflight:** verify actual services/writers, exact tooling, release provenance, ports, filesystem ownership, sandbox/AppArmor behavior, display requirements and available operator view. Do not inspect credentials/profile content.

**Checks:** release helper tests; web-only deployment preserves browser identity; bridge restart preserves it; browser crash does not loop. After explicit live authority, Cooperator login and one synthetic text ask.

**Acceptance:** fresh targeted deployment/credential-boundary review; Cooperator owns login/view actions and host acceptance.

**Recovery/stop:** stop new capture units if setup fails; leave the existing web release intact. No profile recreation, sandbox weakening or restart loop.

**Evidence before S4:** sanitized host preflight, exact deployed capture SHA, one browser instance and synthetic ask result.

### S4 — Search and Research

**Outcome:** both modes return complete archived output through the one capture module.

**Allowlist:** exact selective-port map in section 2; relevant capture mode/output handling; provenance; Markdown/sanitizer tests; new `tests/capture_modes.test.js`, `tests/capture_deep_research.test.js` and shared fake-driver support.

**Dependencies:** S3 foundation; preserve S2 safeguards.

**Authority/host class:** code grant is host-free. Any runtime refresh/live mode check gets a separate S4 operational grant.

**Checks:** mode selection, missing-mode typed failures, deep-research frame admission, cancellation, complete export, restoration after export, HTML attacks and size-bound fallback. No silent ordinary-ask fallback.

**Tier/acceptance:** E2 with fresh R3 provider/untrusted-content review.

**Recovery/stop:** disable the failing mode; do not claim partial output as success. A bounded live check, if authorized, allows at most one synthetic request per mode without automatic retries.

**Evidence before S5:** accepted complete-output/mode tests and updated provenance.

### S5 — One bounded ZIP

**Outcome:** validated frame ZIPs reach the same browser, with a measured usable video budget.

**Allowlist:** new capture `bridge/attachments.py`; bridge/job/upload integration; runner/job-engine file-input handling; existing FrameNest preparation package only for probe/fixture/budget integration; attachment tests and relevant documentation.

**Dependencies:** S4 and persistent-browser acceptance.

**Authority/host class:** repository grant first; fresh file-boundary acceptance; separate capture deployment/preflight and synthetic live grant.

**Checks:** existing envelope/archive/budget/fixture/probe/receipt suites; new attachment Python tests and `tests/capture_attachment_upload.test.js`; rejection before browser contact, cleanup and cancellation.

**Tier/acceptance:** E3, fresh R3 file and provider-boundary acceptance. Cooperator authorizes the bounded live trials.

**Recovery/stop:** semantic or capacity failure disables media capture. Preserve browser/profile; do not lower video minimum or bypass a challenge.

**Evidence before S6:** independent report, accepted synthetic semantic receipt and valid budget, or an explicit whole-level stop if the locked media path is not feasible.

### S6 — Common records and privacy

**Outcome:** every newly cataloged item has an owner; all content access obeys private/family rules.

**Allowlist:** new `kronika_records` domain/application/port/repository modules; `catalog_schema.py`; migration 0034; configuration; media/upload insertion repositories; existing identity/content-audience policy; enumerated access-path modules and direct identity-carrying dependencies; new Timeline/record APIs and registration; affected tests.

**Dependencies:** S5; no shared deployment against old test data.

**Authority/host class:** repository and disposable test databases only; no live migration/reset.

**Checks:** migration from empty/prior schema; atomic ownership; uniqueness; two-user/admin direct-path matrix; share/unshare; private counts; cross-owner duplicates; public exclusion.

**Tier/acceptance:** E3, fresh R3 authorization/file-boundary review.

**Recovery/stop:** no rollout with an uncovered content route. Old records without ownership deny access; do not invent an owner or import them.

**Evidence before S7:** independently accepted permission inventory and migration/transaction evidence.

### S7 — Application capture integration

**Outcome:** media analyses and Search/Research requests use one bridge client and save results exactly once.

**Allowlist:** application capture port/coordinator; infrastructure capture HTTP client/provider; capture binding repository; migration 0035 and corresponding schema/analysis types; analysis lifecycle integration; new request/admin API modules; composition/configuration; focused client/lifecycle/persistence/API tests.

**Dependencies:** S6 privacy acceptance and valid S5 media capability.

**Authority/host class:** repository integration only. No automatic real-media/provider calls.

**Checks:** lost create response, crash before/after local result commit, concurrent polling, repeated callback, reanalysis, busy/cancel/timeouts, expired journal, ambiguous send, null model/reasoning values and derivative limits.

**Tier/acceptance:** E2/E3; fresh targeted acceptance of cross-process idempotency and capture/analysis contracts.

**Recovery/stop:** keep capture submission disabled if bindings or validators are inconsistent. No HTTP-provider fallback.

**Evidence before S8:** end-to-end synthetic application tests proving one result/card and preserved prior success.

### S8 — Timeline and product presentation

**Outcome:** Kronika’s Timeline, Search/Research and sharing are usable within the existing shell.

**Allowlist:** existing web shell files; specific resource packaging only if required; UI-facing product text; affected frontend/resource contracts; new Timeline, capture-request and sharing Node tests.

**Dependencies:** S7 APIs.

**Authority/host class:** repository UI work; no unrelated framework, HTTP/package/deployment identifier rename or new provider controls.

**Checks:** stable cards/order/filtering/pagination; private default and share controls; safe detail rendering; admin metadata; all named Gallery/image/GIF/playback regressions.

**Tier/acceptance:** E2; targeted rendering/privacy checks. Worker evidence covers behavior; Cooperator rendered acceptance is deferred until S9 serves the exact accepted candidate on NUC.

**Recovery/stop:** preserve the prior shell release if integration regresses Gallery or playback.

**Evidence before S9:** complete candidate, frontend regressions and publication-ready exact SHA.

### S9 — Integrated acceptance, reset and deployment

**Outcome:** the accepted product runs on an empty catalog with verified privacy and capture behavior.

**Allowlist:** deployment/reset runbook and acceptance evidence; only corrections explicitly assigned back to their owning slice. No opportunistic features.

**Dependencies:** S0–S8 acceptance.

**Authority/host class:** destructive exact-object reset and deployment, requiring separate read-only preflight and explicit operational grants.

**Checks:** fresh independent integrated acceptance of the eight proofs; exact public-main release checks; stopped-writer inventory; reset procedure below; synthetic full-path verification; Cooperator desktop/mobile rendered acceptance.

**Tier/acceptance:** E3. Fresh integrated application-boundary acceptance plus bounded host deployment checks. This is not a general production-hardening project.

**Recovery/stop:** use previous code with a compatible empty database; never restore deleted unwanted test data automatically. Stop before deletion on any inventory/writer mismatch.

**Evidence before S10:** exact accepted public/deployed SHAs, empty-schema/reset receipt, integrated results and Cooperator rendered acceptance.

### S10 — Public repository transition

**Outcome:** the existing FrameNest history becomes public `cisarik/kronika`, and the former capture repository is archived under its new name.

**Allowlist:** explicitly named GitHub repository settings, local remote URLs, deployment source references, `ap.project.conf` project identity and public repository links. No application/package/path mass rename.

**Dependencies:** S9 acceptance and separate explicit publication/rename authority.

**Preflight:** verify target-name availability, repository identities and exact accepted refs before changing anything.

**Sequence:**

1. Rename old `cisarik/kronika` to `cisarik/kronika-capture-archive`.
2. Rename existing `cisarik/framenest` to `cisarik/kronika`.
3. Update authorized local remotes and deployment source references.
4. Change `ap.project.conf` project identity to the new repository identity, preserving the AP pin.
5. Perform the authorized baseline transition and verify public refs, source checks and release mechanism.
6. Archive the former capture repository only after verification.

**Tier/acceptance:** E3 external publication/configuration transition; Cooperator owns authorization and final acceptance.

**Recovery/stop:** if a step fails, preserve and report the actual intermediate names/refs. Do not compensate through guessed renames or force operations. The deployed release remains available.

No history rewrite; never push the non-public predecessor branches. Local checkout and host directory names may remain unchanged.

## 9. Database reset procedure

The accepted loss of test data does not authorize broad deletion.

1. **Identify exact objects.** From the configured application instances, determine the physical FrameNest catalog database and the old Kronika library database. Discover their exact `-wal` and `-shm` companions. Do not assume a path from documentation is live.
2. **Record a bounded manifest.** Include application, physical path, file type, owner, device/inode where available and expected schema identity. Do not inspect account/session contents or browse state directories broadly.
3. **Prepare the accepted release.** Use the existing release helper checks. Preserve its explicit `migration-required` boundary.
4. **Freeze admission and stop writers.** Stop web workers/coordinators, upload/acquisition writers, old Kronika processes and relevant scheduled activity. Drain capture tasks; no completion may write into the database being removed.
5. **Reverify immediately before deletion.** Same exact objects; no symlink substitution; no unexpected writer.
6. **Delete only manifest-listed database/WAL/SHM objects.** No directory deletion, glob expansion or recursive cleanup.
7. **Create the new FrameNest database through normal migrations through 0035.** Do not squash Alembic history. Restore only explicitly configured infrastructure registrations required to operate; do not automatically rescan/import old media.
8. **Verify empty application data and schema.** Establish the normal backup/checkpoint foundation for the new database.
9. **Activate the accepted release through the existing helper continuation.** Verify private creation, successful timeline entry, capture status and Gallery behavior.
10. **Rollback if necessary.** Stop writers and use previous accepted code with its compatible freshly created empty database. Do not restore the deleted test dataset.

Preserve source media, capture journal retention, browser profile, identity configuration, tokens, unrelated state, backups and Git/Meta archives. Old capture request IDs must not be reused after the application reset.

## 10. Validation and security evidence

### Declared routes

Later Python checks use the authorized exact baseline:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <authorized-40-hex-SHA>

./.ap/ap exec --root /home/agile/Projects/framenest --baseline <authorized-40-hex-SHA> --operation runtime-info

./.ap/ap exec --root /home/agile/Projects/framenest --baseline <authorized-40-hex-SHA> --operation test-focus -- <selected-test-paths> -q -p no:cacheprovider

node --test <selected-test-files>
```

The baseline placeholder must be bound in each execution grant. It is not permission to use an ambient Python route.

Use existing pytest, Node tests, packaging checks and fake drivers. Do not introduce another test toolchain or run the source repository’s application/test route as a substitute.

### Required proof matrix

| Proof | Focused positive checks | Negative/failure checks | Acceptance owner |
|---|---|---|---|
| 1. Private records remain private | Owner reads own record, preview, playback and download. | User B and administrator B cannot access A’s private IDs, files, counts, snippets or job results. Include Range requests and forged ownership. | Worker tests; fresh independent S6/S9 acceptance. |
| 2. Family is not public | Mapped household member reads a shared record; unshare revokes it. | Unmapped/anonymous/public composition denied; no publication row; erroneous publication row cannot expose it. | Independent S6/S9 acceptance. |
| 3. One card/result | Initial validated analysis enters once; reanalysis updates the same card. | Repeated callbacks/polls, concurrent completion and crash recovery create no duplicate; failure preserves older success/time. | S7 persistence tests and S9 integration. |
| 4. No automatic second send | One durable intent permits one click. | Disconnect/crash at each send boundary, missing DOM acknowledgement and stale offers never cause a second click. | Fake driver plus fresh S2/S7 review. |
| 5. Same browser instance | Multiple jobs, bridge outage and web deploy preserve browser identity. | Browser crash blocks service; automatic restart absent; manual brake enforced. | Worker lifecycle tests; authorized S3/S9 host evidence. |
| 6. ZIP rejected before contact | Valid prepared ZIP accepted and removed at job end. | Wrong compression, traversal, duplicates/gaps, fake JPEG, excess dimensions/bytes, malformed framing, symlinks and cancellation clean safely without browser upload. | Fresh S5 file review; synthetic live gate. |
| 7. Whole safe output | Complete Search/Research text and Markdown survive storage/retrieval. | Summary mistaken for completion, export failure, script/event/URL payloads and rendering bounds cannot produce unsafe or falsely complete output. | S4/S7 tests; S9 rendered acceptance. |
| 8. One packaged capture | Installed wheel/sdist resolves CLI and every needed asset. | No vendor fallback, duplicate kernel, source-checkout dependency or missing resource. | S1/S3 packaging and independent provenance review. |

Retain focused existing coverage:

- Capture security, CLI, projects, job limits, protocol and packaging.
- JPEG envelope, deterministic archive, budget, fixture, probe and receipt suites.
- `test_tailscale_ingress_security.py`, requester-private tests and route-policy inventory.
- Content publication/unpublication and automatic-analysis privacy/lifecycle contracts.
- Upload ownership and atomic publication contracts.
- Release source/remote/docs contracts.
- `gallery_loading_states`, `gallery_filter_controls`, `gallery_search_tag_filters`, `gallery_still_image_render`, `gallery_gif_inline_toggle` and `gallery_details_playback_handoff` Node tests.

New suites should use the existing directory conventions for journal/intervention/attachments, record migrations/repositories, record privacy, capture-client recovery and frontend Timeline/sharing behavior.

### Security boundary checklist

Acceptance evidence must establish:

- Loopback-only capture and operator view; existing trusted Tailscale family ingress.
- Token never reaches browser frontend, reports or logs.
- Verified server ownership, explicit household mapping and no administrator read shortcut.
- Authorization before list/count construction and before opening media bytes.
- Public composition cannot expose new records.
- Complete generated content stored privately and rendered without active content/resources.
- ZIP validation, private staging, bounded retention and no symlink-following cleanup.
- No cookie/session/password extraction, profile inspection, other-tab access or model/reasoning inspection.
- Only Cooperator-operated authentication/profile backup/restore.
- Reports contain sanitized identities and operational evidence, not private network values, hostnames, account data, prompts or answers.

Use proportionate INFOSEC routing: documentation review for S0; provenance/build review for S1; fresh targeted lifecycle/provider, credential, file, authorization and rendering reviews where those boundaries change. S9 combines their evidence with fresh integrated acceptance and bounded deployment checks. Do not expand this into unrelated infrastructure or production hardening.

## 11. Execution transition, assumptions and completion

### Branch and acceptance topology

After S0 execution is authorized, create `feat/kronika-one-product` from the verified primary baseline. Keep the existing feature branch and source history intact.

Work sequentially. Each row produces an accepted candidate commit; correction commits remain associated with that row. Use repository-required English commit subjects. Publish accepted milestones to `main` only through an explicit publication grant.

S3–S5 live gates may require accepted intermediate capture releases on public `main`. Do not expose the S6–S8 family product against old data before S9. Cooperator visual acceptance happens only when the exact candidate is public and refreshed onto NUC.

### First proposed execution boundary

The next implementation prompt should authorize **S0 only**, with:

```text
Native planning mode: not-used
Primary baseline: 26d28b16c08a5e7e0179a32c16646bfdc1009c81
Scope: S0 documentation and ADR allowlist
Source repository: read-only
AP pin: unchanged
Host/network/provider/database authority: none
Publication authority: none
Acceptance: documentation consistency and locked-direction conformance
```

It must also bind actual branch/commit permissions, the declared route and report destination. This plan is not that execution prompt.

### Defaults and remaining decisions

No unresolved product decision blocks S0.

Later grants must bind operational facts that cannot be obtained through this planning scope: current accepted SHA, actual host tooling, explicit local owner, exact database objects, runtime readiness and repository-name availability. These are preflight gates, not permission to guess or reopen the product direction.

Chosen defaults include one capture journal, one browser, one active job, no automatic uncertain retry, 24-hour result retention, owner-only mutation, no public mapping and complete-text fallback for rendering.

### Excluded horizon

No personal-photo AI analysis, old-database import, native share applications, new external LLM provider, recovery provider, model/reasoning selection, public publication, second family account system, second deploy system, second test toolchain, production-hardening program or broad `framenest` rename.

The AP pin and managed integration block remain unchanged. FrameNest’s activated upgrade-observation ledger remains historical/advisory evidence; this task neither reconciles nor closes it and does not treat it as authority.

### Planning closure evidence

```text
Start/end FrameNest commit:
26d28b16c08a5e7e0179a32c16646bfdc1009c81

Start/end Kronika source commit:
66c40d43c577276b0ad304a494fbbb1ffb6fc933

Changed files and purpose: none
Final repository/index/AP cleanliness: verified
Validation performed: bounded source, provenance, Git and authorized public-ref inspection
Validation not performed: tests, builds, application execution, host/browser/provider checks
Delivery deviation: original file delivery superseded by explicit Cooperator instruction
Smallest next step: Orchestrator issues the complete S0 execution prompt after plan acceptance
Authority expiry: planning ends with this report; no implementation authority carries forward

Orchestration critique:
MEASURED: existing access and analysis contracts conflict with the new privacy and
model-unaware capture requirements; S6/S7 now explicitly include their correction.
LEAD: host readiness and ZIP image understanding remain unverified; the cheapest
decisive checks are the bounded S3 preflight and S5 synthetic trials.
Resolved Execution Issues / Near-Misses: the prior file-delivery limitation was
resolved by explicit session-delivery authorization; no write bypass was used.
Pre-existing Failure Classification: no runtime/test failure established because
execution was not authorized; identified source gaps are implementation work.
```

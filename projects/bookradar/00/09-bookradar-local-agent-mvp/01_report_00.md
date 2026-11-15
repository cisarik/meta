### Report for ORCHESTRATOR_CHAT

# BookRadar — Local Agent-Assisted MVP: Core Loop

```text
Logical whole identity: bookradar-local-agent-mvp
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BOOKRADAR-LOCAL-AGENT-MVP-PLAN

status: PARTIAL
Plan content: complete proposal, ready for material-decision review.
Phase-qualified result: not-applicable
Start commit: 80b172c2db6fcacc93041d4eb4c246450547f112
End commit: 80b172c2db6fcacc93041d4eb4c246450547f112
Changed files: none
Tests and validation: read-only repository inspection; static 113-test inventory; public commit/ref/CI checks; strict ./.ap/ap doctor PASS. No builds or tests executed.
Git result: none
Deviations, risks, or missing evidence: required report-file persistence is unavailable under active native Plan Mode; live integrations and Ubuntu runtime acceptance remain unverified.
Smallest next step: ORCHESTRATOR reconciles the decision table and arranges exact report persistence through the permitted completion route.
Report justification: new-evidence
Logical-whole closure: not-closed
Authority expiry: this terminal report ends the planning grant; no autonomous continuation.
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
```

**Prompt SHA-256:** `0a67b414519d41a3d75606accd97a8bd8511616478a6342ce35b83fbbb724247`

**Delivery limitation:** This complete report is returned in the native plan output. The destination directory exists, is a directory, resolves to the expected physical path, and is not a symlink. The exact report destination remains absent:

`/Users/agile/meta/projects/bookradar/00/09-bookradar-local-agent-mvp/01_report_00.md`

No report file was written, so no saved-report SHA-256 or successful readback is claimed. Overall status is `PARTIAL` because required file delivery remains incomplete, following AP’s planning-completion rule. Completing delivery must preserve this report’s content and cannot authorize implementation.

**Authority:** This report is a proposal only. Recommendations below are not accepted COOPERATOR decisions. Implementation requires the decisions to be reconciled and a separate complete ORCHESTRATOR grant with native planning mode `not-used`.

## 1. As-found state and baseline

The repository matches the declared baseline:

| Check | Independently observed result |
|---|---|
| Physical root | `/Users/agile/Projects/bookradar` |
| Origin | `https://github.com/cisarik/bookradar` |
| Branch | `main` |
| HEAD | `80b172c2db6fcacc93041d4eb4c246450547f112` |
| Parent | `69ec45e245108c90e2de4302c03ca72572bf1829` |
| Tree | `578fbe8f958b17230ccdc5e1f13476c5e23c84f3` |
| Subject | `docs: demonstrate governed conflict resolution` |
| Product worktree | Clean, including the final recheck |
| AP gitlink and submodule HEAD | Both `d7023cf037f6d17885c3ede5c04812c61640da50` |
| AP checkout | Detached and clean |
| Strict AP doctor | PASS |
| Rust | `rustc 1.99.1 (58cf8f9c3 2026-10-13)` |
| Ignore rules | Exact `/target/` and `/tests/target/` rules |
| Project execution declaration | No `ap.project.conf` |
| Upgrade ledger | None declared outside the managed root instructions |

Public `HEAD` and `refs/heads/main` independently matched the expected commit through `git ls-remote`. The public commit API confirmed its parent, tree, and subject. Workflow `verify`, run `43600404485`, reported `completed` / `success` for that SHA. These are Worker-observed public facts. [Commit](https://github.com/cisarik/bookradar/commit/80b172c2db6fcacc93041d4eb4c246450547f112), [CI run](https://github.com/cisarik/bookradar/actions/runs/43600404485).

Static inspection reconciled the **113 existing tests**:

| Inventory | Count |
|---|---:|
| Core verification | 17 |
| Store unit tests | 10 |
| Observation CLI | 4 |
| History | 13 |
| Persistence | 6 |
| Promotion | 12 |
| Research CLI | 2 |
| Research contract | 5 |
| Research ingestion | 20 |
| Review CLI | 4 |
| UI CLI | 4 |
| UI HTTP | 6 |
| UI render | 10 |
| **Total** | **113** |

The Orchestrator’s reported successful offline gate is baseline execution evidence, not an execution performed by this Worker. No build or test suite was rerun.

The accepted [domain contract](/Users/agile/Projects/bookradar/docs/domain-contract.md), [research-v1 reference](/Users/agile/Projects/bookradar/docs/research-input-v1.md), and ADRs 0001–0008 agree with the inspected implementation:

- `evaluate_verification` in `src/verification.rs` owns verification, including the strict 24-hour expiry and `AgentOnly` refusal.
- `Store::append`, `Store::append_review`, `Store::history`, and `Store::current` preserve observation/review history and delegate eligibility to the core.
- `history::resolve` separates chronological changes, conflicts, unsuccessful rechecks, and current assessment.
- `ResearchStore::import` owns admission, immutable run context, replay, quarantine, and ledger-local projection.
- `ResearchStore::candidate`, `inspect`, and `current` provide the necessary read surfaces. `ImportReport` provides counts, **not a receipt ID**.
- `promote` requires complete caller-supplied positive attestation. It does not copy agent facts into approved application truth.
- The three existing store binaries retain their accepted command surfaces.
- Both existing schemas enforce append-only observation/review history; the research schema additionally protects inputs, runs, and findings.
- `bookradar-ui` reads both stores once at the supplied `--now`, closes them, and serves an immutable snapshot. It is not a scheduler.
- `scripts/verify.sh` is the sole gate. Its dependency-fetch preparation precedes offline build/test/clippy commands; tests do not call external services.

The successor handout, predecessor closure, and foreign artifact matched their supplied SHA-256 values. Historical notes were reconciled with the current prompt and latest COOPERATOR direction. No design acceptance was inherited from the foreign artifact. The target remains Ubuntu Linux, with portable development on macOS. Actual deployment and service installation remain separate work.

No repository-baseline discrepancy was found.

## 2. Bounded MVP and operator flow

**Recommended slice:** one new synchronous application crate, `bookradar-agent`, with CLI writes, an in-process checking loop, and English read-only monitoring pages. Keep the existing binaries and fixed-snapshot UI defaults intact.

The smallest operator flow is:

1. Initialize a private local workspace.
2. Configure non-secret provider settings and the checking interval.
3. Add a watched book.
4. Run one manual check.
5. Inspect sourced, explicitly unverified findings and access results.
6. Enable periodic checks and run the foreground monitor.
7. Inspect subsequent attempts and changes.

Proposed command surface:

```text
bookradar-agent init <workspace> --producer <identifier> --owner <identifier> --at <unix-seconds>
bookradar-agent settings show <workspace>
bookradar-agent settings set <workspace> --at <unix-seconds> <configuration flags>
bookradar-agent watch add <workspace> --title <text> --target-language slovak --at <unix-seconds> [--author <text>] [--isbn <text>]
bookradar-agent watch set <workspace> <watch-id> --enabled true|false --at <unix-seconds>
bookradar-agent run <workspace> --watch <watch-id> --at <unix-seconds> --offline-fixture <path>
bookradar-agent monitor <workspace> --offline-fixture <path> [--bind 127.0.0.1:<port>]
bookradar-agent history <workspace> --watch <watch-id> --at <unix-seconds>
bookradar-agent stop <workspace> --at <unix-seconds>
```

A separately authorized probe mode may replace `--offline-fixture` with an explicit bounded probe permit. It must never activate merely because credentials exist.

Configuration contains:

- Immutable producer and local owner references.
- Named provider endpoints, required model identifier for live probes, and fixed request limits.
- Explicit retailer host/source allowlist.
- Global checking interval; recommended initial value **43,200 seconds**, subject to approval.
- Per-run limits and durable live-call allowances, initially zero.
- No credential values.

A watch contains an internal ID, revision, owner reference, title, optional author/ISBN, target-language constraint, enabled state, and supplied recording time. Adding it does not resolve a work, edition, author identity, or language. New watches start disabled; manual checking remains available.

Initial discovery is bounded to three tracked candidate locators per watch. Rechecks revisit those candidates. Additional discovery breadth, automatic identity reconciliation, library ownership, notifications, writable web forms, installation, services, and deployment are deferred.

The resulting MVP is an offline-verifiable implementation of the loop. Acceptance must not claim that routine live monitoring has been authorized or proven.

## 3. Provider/model/search route

Propose these named routes, subject to provider-contract verification before any real probe:

| Route | Proposed purpose and request |
|---|---|
| Brave | `GET https://api.search.brave.com/res/v1/web/search`; one deterministic bibliographic query, `count=5` |
| NVIDIA NIM | `POST https://integrate.api.nvidia.com/v1/chat/completions`; extraction from each successfully fetched bounded document |

The query is assembled deterministically from the supplied title, optional author/ISBN, and Slovak target. Model query generation is unnecessary for this slice.

Run sequence:

1. Capture immutable watch/settings revisions and producer context.
2. Reserve the search allowance before dispatch.
3. Validate search response structure and candidate URLs; snippets remain discovery data.
4. Recheck tracked candidates and fill vacant slots, up to three.
5. Fetch each selected page sequentially.
6. For readable supported content, call the configured model once.
7. Validate the complete model response and quotation occurrence.
8. Construct application-owned research-v1 bytes.
9. Persist those exact bytes before import.
10. Import, reconcile the stored receipt, and append the terminal operational outcome.

Proposed NIM request settings are `stream=false`, temperature `0`, maximum output `1024` tokens, and JSON-object output. These are candidate request parameters, not verified model capabilities. Unsupported structured output produces a visible failure; it must not trigger a silent request or model fallback.

The model may return exactly:

```json
{
  "v": 1,
  "subject_quote": "Title: Synthetic Atlas",
  "language": {
    "value": "slovak",
    "quote": "Language: Slovak"
  },
  "availability": {
    "value": "available",
    "quote": "Availability: available"
  },
  "price": {
    "amount": "12.00",
    "currency": "EUR",
    "basis": "per-copy",
    "quote": "Price: 12.00 EUR per-copy"
  }
}
```

Language and availability use the existing wire enums. Unknown claims use an unknown value and null quotation; price may be null.

Reject or quarantine:

- Duplicate or unknown fields, unsupported version, invalid enums, invalid money, excess nesting, or output exceeding 8 KiB.
- Malformed JSON, truncated completions, multiple completion choices, refusal, or an unexpected response shape.
- Instruction fields or proposed tools, URLs, timestamps, identities, approvals, or execution parameters.

Do not salvage malformed model text into facts. Independently captured access evidence may still produce an application-authored finding with unknown extracted claims.

Each supporting quotation is at most 256 characters and must occur exactly in the retained document supplied to the model. A missing quotation makes its claim unknown. Occurrence establishes correspondence to document bytes; it does not establish factual accuracy, visible browser content, or verification.

Proposed seams:

```text
SearchProvider::search(request, budget) -> bounded raw response
ModelProvider::extract(request, budget) -> bounded raw response
PageFetcher::fetch(locator, policy, clock) -> captured access result
Clock::now() / Clock::elapsed() -> injected time
CredentialSource::load_for_probe() -> redacted secret values
HttpExecutor / ChildSupervisor -> bounded transport execution
```

Offline doubles return deterministic bytes and recorded calls through these same interfaces. No test performs DNS, external HTTP, or credential lookup.

Live allowances default to **zero**. Each attempted call is durably reserved before execution; failures and unknown crash outcomes consume an allowance. There is no automatic reset, limit increase, retry, or provider switch. Request-count limits are not represented as monetary guarantees.

## 4. Credentials and privacy

Real NVIDIA and Brave adapters require provider credentials. Offline operation requires none.

| Option | Assessment |
|---|---|
| Restrictive local plaintext file | Portable but introduces secret retention, file-permission, backup, and cleanup obligations |
| Linux secret service/keyring | Suitable later, but adds runtime/service dependencies and a separate macOS development strategy |
| Launch-time environment injection | **Recommended:** portable, no application-managed secret storage |
| No keys until separately authorized probes | **Recommended current posture:** implementation and offline acceptance need no keys |

Only the probe runner reads the two specifically named credential variables, after live-mode and permit validation. Offline startup must not inspect them.

Secrets must:

- Be wrapped in a type whose formatting is redacted.
- Never enter settings, databases, fixtures, HTML, reports, logs, command arguments, or retained requests.
- Reach the transport only through its private stdin configuration.
- Be omitted from the sanitized environment of resolver and transport children.
- Be discarded when the process ends; no application key files are created.

Do not print raw provider error bodies. If a response contains a supplied secret value, discard that response before persistence and record a fixed redaction/error category.

Eventually authorized external requests may reveal bibliographic search terms, retailer URLs, and a bounded public document excerpt. Never send owner references, internal watch IDs, local paths, private notes, library records, credentials, or unrelated repository content.

The operator must explicitly accept this disclosure boundary before real calls. A watch expresses interest; it never implies ownership or purchase.

## 5. Search, fetch, and extraction trust

Proposed fetch policy:

| Control | Recommendation |
|---|---|
| Scheme/port | HTTPS, default port or explicit 443 only |
| Host | Exact operator-approved ASCII hostname; no implicit `www` expansion |
| Locator rejection | No userinfo, IP literals, ambiguous host syntax, control characters, backslashes, malformed escapes, or non-HTTPS schemes |
| DNS | Resolve in a bounded helper; permit public IPv4 destinations only |
| Address policy | Reject private, loopback, link-local, shared, multicast, reserved, and documentation ranges; refuse IPv6-only destinations in this initial adapter |
| Rebinding | Pin the validated address into the actual connection while retaining hostname TLS verification |
| Redirects | Handle explicitly; maximum two; revalidate every hop; allow only approved hosts |
| Credentials | None sent to retailers; no cookies, browser session, authorization, or referrer |
| TLS | Certificate and hostname verification enabled |
| Time | DNS 3 seconds; connect 5 seconds; request 20 seconds; model request 30 seconds; overall run 180 seconds |
| Size | Headers 16 KiB; retailer body 1 MiB; total retailer bodies 3 MiB per run |
| Encoding | Request identity encoding; reject unsupported compression and unsupported text encodings |
| Extraction input | At most 32 KiB of valid UTF-8 source content, cut at a character boundary |
| Retries | None |
| Concurrency | One outbound request at a time |

Public-address validation must precede connection and be applied again after redirects. Mixed public/private IPv4 answers fail closed. No fallback may reconnect through an unchecked address.

This initial extraction consumes bounded source text, including HTML source where applicable. It does not claim rendered visibility, execute JavaScript, or implement browser extraction. Script text, comments, page instructions, and model output remain untrusted data. Complex or dynamic pages may yield unknown results.

Application-owned provenance supplies:

- Requested URL.
- Final attempted/resolved URL.
- Ordered redirect reference.
- Access result.
- Observation, access, capture, and source-update timestamp assertions.

Successful observation/capture times come from the injected clock at capture; access time marks the attempt. Source-update time remains explicitly unknown unless separately supported. Failed access retains its attempt/result times without inventing a page capture.

Map outcomes independently:

| Result | Access/listing | Availability |
|---|---|---|
| Explicit quoted available/reserved/unavailable assertion | Readable; present or uncertain as supported | Corresponding untrusted source assertion |
| Readable document without supported stock text | Readable; uncertain/present as supported | Unknown |
| 429 | Rate-limited; uncertain | Unknown |
| CAPTCHA | CAPTCHA; uncertain | Unknown |
| 401/403 obstruction | Authentication-blocked; uncertain | Unknown |
| Timeout/transport failure | Corresponding access failure; uncertain | Unknown |
| 404/410 | Page-gone; removed | Unknown |
| Generic/category redirect | Uncertain listing; retain redirect | Unknown |

Only application code constructs the research-v1 envelope. Provider output cannot choose provenance, evidence method, resolved identity, reviewer approval, or access status. All imported support remains `AgentOnly`.

## 6. Application and UI scope

| Alternative | Assessment |
|---|---|
| Extend the existing loopback shell with read-only pages | **Recommended:** reuses established HTTP and escaping controls |
| Separate web application/framework | Adds another server/security surface without a necessary capability |
| CLI-only administration | **Recommended write surface:** sufficient for configuration, adding books, and manual triggering |

Proposed monitor pages:

| Route | Content and source |
|---|---|
| `/` | Watched books, enabled state, latest attempt, next due time; control store |
| `/books/<positive-decimal-id>` | Candidate locators, quoted assertions, four timestamps, access results, run history, changes; control records linked to research receipts |
| `/settings` | Non-secret configuration, limits, runtime mode, and loaded-key presence indicators |
| `/style.css` | Existing embedded stylesheet |

Pages are English, server-rendered, and read-only. Refreshing the page retrieves the current published snapshot. No JavaScript, write forms, JSON endpoints, or automatic connection tests are added.

Add an opt-in `serve_documents` library surface to `bookradar-ui`. Keep existing `serve`, CLI arguments, snapshot semantics, route restrictions, and defaults unchanged. The new monitor supplies an allowlisted document resolver and a shutdown predicate.

Preserve:

- Literal `127.0.0.1` binding.
- Existing header limits and deadlines.
- `GET`/`HEAD` only.
- Host, Origin, framing, and cross-site checks before invoking the resolver.
- Existing security headers, including `form-action 'none'`.
- Escaped text and validated/inert source links.

Research cards always show **Unverified**, with separate “Agent-extracted source assertion,” observation time, quotation, language uncertainty, and access result. They must not receive `Last observed available` or `Checked available` merely because a quotation passed.

Existing curated views continue to obtain truth labels through `render_current_labels`; no new freshness or verification implementation is introduced. The new monitor does not automatically combine agent research with curated application-store approval.

Writable browser administration would require a separately approved change covering forms, CSRF tokens, exact-origin enforcement, body limits, methods, and CSP. It is excluded from the recommended slice.

## 7. Persistence and identity

The existing research ledger suffices for untrusted findings, admission, replay, and candidate projection. Existing stores do **not** contain watch configuration, pending requests, durable call reservations, or scheduler recovery state.

Recommend one new control database, separate from both accepted formats:

- Application ID: `0x42524147`.
- `user_version`: `1`.
- Rollback journal `DELETE`, foreign keys enabled, `synchronous=FULL`.
- Exclusive creation; strict format/schema validation; no automatic adoption or migration.
- Workspace directory mode `0700`; owned database files `0600` on the supported Unix hosts.
- No updates/deletes of retained control history.

Exact table scope:

| Table | Key and purpose |
|---|---|
| `app_meta` | Immutable keyed producer/owner references |
| `settings` | Revision primary key; non-secret configuration and supplied recording time |
| `watches` | `(watch_id, revision)`; complete watch revisions and owner scope |
| `candidates` | Internal candidate ID; watch revision, source/listing/generation references, locator, creation time |
| `runs` | Internal run ID; immutable watch/settings revisions, trigger, producer context, start time |
| `events` | Event ID; typed request, call reservation/result, quarantine, access result, interruption, pause, and terminal records |
| `batches` | Run ID; exact frozen research envelope bytes |
| `receipts` | Run ID; reconciled research receipt reference, admission report, recording time |

Add `BEFORE UPDATE` and `BEFORE DELETE` abort triggers to each table. Allocate internal numeric IDs transactionally. Settings/watch changes append revisions.

Identity rules:

- Producer ID is supplied at initialization and remains immutable.
- Research run IDs are `run:<internal-run-id>`.
- Finding IDs are `candidate:<internal-candidate-id>`, scoped by producer/run.
- Source references are explicit local source handles; listing and generation handles describe provisional tracking.
- URLs select a monitored locator, not a universal offer identity.
- No automatic cross-watch merge or edition resolution occurs.
- Continuity remains explicitly uncertain; reused listings cannot establish identical copies or editions.

Every later check gets a new run identity, even if the content is unchanged. Replaying a frozen batch uses the original identity and exact bytes. Changed bytes under that identity must follow existing conflict/quarantine rules.

Recovery is a cross-file sequence, not a claimed atomic transaction:

1. Persist completed research bytes in `batches`.
2. Call `ResearchStore::import`.
3. Use `ResearchStore::inspect` to locate the receipt containing those exact saved bytes.
4. Append the receipt link and operational terminal event.

A crash between steps 2 and 4 is recovered by importing the same bytes again and reconciling the original receipt. `ImportReport` must not be mistaken for a receipt identifier.

The recovery import receives a new supplied ingestion instant. Observation/capture times and envelope bytes remain unchanged. If the clock regresses behind the ledger’s accepted ingestion time, pause with an error; do not clamp or rewrite timestamps.

Derive changes from consecutive linked attempts for the same provisional candidate. Show access changes separately from source-assertion changes. Missing results and failed access never become unavailable stock. Price comparisons require matching currency and basis; otherwise show changed assertions without a price trend.

No notification records are required. A later change-feed implementation can use `(previous_run, current_run, candidate, field)` as a stable deduplication key.

## 8. Scheduling and runtime

Recommend one foreground process with a sequential worker and a read-only HTTP serving thread. CLI commands append short control transactions; the monitor publishes immutable display snapshots.

- Recommended default interval: **12 hours**, independently configurable and unrelated to the core’s freshness rule.
- At most one active run across the workspace.
- Use a workspace advisory worker lock through the Rust standard-library file-locking API.
- Manual requests are durable events. If another worker owns the lock, the command queues/coalesces the request and exits with an explicit queued result.
- Manual and scheduled requests for an already pending or active watch attach to the same run.
- Process watches in stable internal-ID order.
- A never-checked enabled watch is immediately due.
- At startup or wake, perform one catch-up attempt per overdue watch.
- Do not replay every missed interval.
- Next due time is the terminal attempt time plus the configured interval, including failed attempts; no rapid failure loop.
- Configured quota exhaustion pauses affected work until explicitly changed. No repeated outbound attempts occur while paused.

Production wall time is read only by the runtime clock adapter. Scheduling and pipeline decisions accept injected time. Tests use fixed wall and elapsed-time values.

Shutdown/restart:

- `stop` appends a request; the monitor stops scheduling, terminates/reaps owned active children, preserves pending work, and closes the listener.
- A frozen batch is recoverable without repeating outbound calls.
- An interrupted run without a frozen batch stays interrupted; completed step records remain history. A subsequent check uses a new run ID.
- Outstanding call reservations remain consumed/unknown after abrupt termination.
- Restart must wait through the configured maximum prior-request timeout plus a small grace period before new outbound work, preventing overlap with a bounded orphaned request.
- Clock regression pauses operation instead of fabricating chronological progress.

No service manager, automatic startup, installation, deployment, or production operation belongs to this implementation. The same foreground executable must remain portable across macOS development and the future Ubuntu target.

## 9. Runtime and dependencies

Recommend a synchronous implementation using existing pinned Rust dependencies and an explicitly controlled curl transport.

| Dependency | Proposed use |
|---|---|
| Rust `1.99.1` standard library | Threads, time seams, file locking, child supervision, bounded I/O |
| `rusqlite =0.37.0`, bundled, defaults disabled | New control database |
| `serde =1.0.228`, `std`, defaults disabled | Strict input visitors without derive |
| `serde_json =1.0.145`, `std`, defaults disabled | Provider/configuration serialization and validation |
| Existing path crates | Store boundary and restricted UI serving |
| curl | Synchronous HTTPS transport through a sanitized child process |

The Rust versions and transitive checksums already exist in `Cargo.lock`. The expected lockfile change adds the local application package and its dependency references; no new registry package is required.

The observed curl is **8.7.1**. Its installed manual confirms stdin configuration, disabled ambient configuration, address pinning, and request bounds. This is a compatibility reference, **not current security approval or Ubuntu runtime proof**. Before any real probe, a separate preflight must record and approve the exact executable/build, TLS backend, trust configuration, and patch posture. A different version cannot be silently substituted.

Transport construction must:

- Invoke an explicit executable with `Command`, never a shell.
- Put `--disable` first and disable URL globbing, proxies, retries, and automatic redirects.
- Clear ambient configuration/credential environment.
- Pass secrets and request bodies through correctly escaped stdin configuration.
- Bound stdout/stderr while reading; kill and reap on overflow or deadline.
- Preserve transport status separately from parsing.
- Never expose raw transport diagnostics.

The resolver helper uses the same executable in an internal bounded mode, receives only an approved hostname, and receives no credentials.

Comparison:

- **Pure std without a TLS transport:** insufficient for honest real HTTPS fetching.
- **Existing pins plus controlled curl:** smallest registry graph; adds subprocess supervision and host-version acceptance obligations.
- **Axum/Tokio/reqwest/scraper:** stronger framework/parser reuse, but introduces a new dependency graph, async coordination, exact-version research, and lockfile/supply-chain review. It is not selected by inheritance.

Do not implement a second TLS stack or claim an unverified dependency version is approved. If the curl route is rejected, obtain bounded dependency evidence and an explicit revised dependency decision before implementation.

`bookradar-core` remains dependency-free; its dependency tree must remain one line.

## 10. Determinism, tests, and gate

Preserve all 113 existing tests. Add the following **46 causal tests**, giving an expected total of **159**. This is a proposed inventory, not a measured result.

Each test below uses temporary synthetic state, fixed timestamps, and injected provider/transport/clock seams. HTTP tests use only the existing loopback test pattern.

### `crates/bookradar-agent/tests/control.rs` — 8 tests

| Function | Setup → expected result / regression |
|---|---|
| `ids_remain_independent_of_bibliographic_metadata` | Add identical titles/ISBNs → distinct internal watches; no inferred identity merge |
| `configuration_changes_append_revisions` | Change interval/model settings → previous revision retained; secrets rejected |
| `foreign_formats_and_existing_paths_are_refused` | Supply existing/foreign/version-mismatched files → no adoption, overwrite, or migration |
| `control_history_is_append_only` | Attempt SQL update/delete and read-only writes → refused; original rows preserved |
| `worker_lock_prevents_parallel_runs` | Two contenders → one active worker; second request explicitly queued |
| `import_commit_gap_recovers_original_receipt` | Interrupt after research commit → replay links original receipt without another observation |
| `replay_and_changed_payload_follow_research_contract` | Replay identical then altered bytes → no-op then conflict/quarantine |
| `interrupted_call_reservation_remains_consumed` | Crash after reservation → unknown outcome still consumes allowance; restart observes quiescence |

### `crates/bookradar-agent/tests/providers.rs` — 8 tests

| Function | Setup → expected result / regression |
|---|---|
| `offline_full_flow_preserves_provenance` | Search→fetch→model→import doubles → one unreviewed AgentOnly candidate with exact provenance |
| `malformed_model_output_is_quarantined` | Malformed, truncated, duplicate-key, unknown-field, oversized variants → no interpreted model facts |
| `model_instructions_cannot_change_execution` | Instruction fields and hostile quoted text → no extra calls, tools, URLs, or approvals |
| `malformed_search_results_are_accounted` | Invalid result shapes/URLs → explicit rejected pointers; no navigation |
| `missing_quotes_leave_claims_unknown` | Claimed stock/language/price without occurrence → corresponding claims unknown |
| `czech_and_unknown_language_never_satisfy_slovak_target` | Czech, mixed, unknown, conflicting outputs → unresolved and never eligible |
| `provider_failures_keep_distinct_outcomes` | Refusal, timeout, malformed response, quota refusal → truthful recorded categories |
| `caps_stop_before_dispatch` | Exhaust allowance before/within run → no excess call; safe partial batch retained |

### `crates/bookradar-agent/tests/fetch.rs` — 10 tests

| Function | Setup → expected result / regression |
|---|---|
| `https_and_locator_rules_are_enforced` | Scheme/userinfo/port/control/escape variants → blocked before resolution |
| `nonpublic_and_unsupported_addresses_are_blocked` | Private/reserved IPv4, IPv6 literals and IPv6-only results → no connection |
| `dns_validation_is_pinned_to_connection` | Mixed answers and simulated rebinding → refusal or connection to the validated address only |
| `redirects_are_revalidated_without_credentials` | Allowed, cross-host, private, downgrade, and excess hops → bounded policy; no forwarded secrets |
| `time_and_byte_caps_abort_transport` | Header/body/total/deadline overflows → child terminated and reaped; no partial stock assertion |
| `access_failures_never_infer_stock` | 429, timeout, transport error, 404/410 → dated access/listing records with unknown stock |
| `captcha_and_generic_redirect_remain_uncertain` | Challenge text/category redirect → truthful obstruction or listing uncertainty |
| `model_cannot_supply_transport_provenance` | Model attempts URL/time/access overrides → application-captured values preserved |
| `curl_has_no_ambient_configuration` | Fake executor inspects invocation → disabled config/proxy/retry/globbing; sanitized environment |
| `credentials_are_absent_from_retained_output` | Generated in-memory sentinel echoed in errors/body → discarded/redacted; absent from logs, stores, and HTML |

### `crates/bookradar-agent/tests/scheduler.rs` — 8 tests

| Function | Setup → expected result / regression |
|---|---|
| `interval_fires_at_due_instant` | Tick before/at due → zero/one run |
| `manual_and_scheduled_requests_coalesce` | Both triggers pending → one run |
| `request_during_active_run_joins_that_run` | Manual request while active → attributed coalescence, no second dispatch |
| `wake_and_startup_catch_up_once` | Several missed intervals → one catch-up |
| `next_due_uses_terminal_attempt_time` | Successful and failed attempts → interval applied without immediate retry |
| `restart_resumes_frozen_import_only` | Frozen versus unfinished run → import-only recovery versus interrupted state |
| `regressed_clock_pauses_without_rewriting_time` | Earlier injected clock → no clamped timestamp or import |
| `shutdown_preserves_pending_and_interrupted_work` | Graceful stop and abrupt interruption → recoverable requests and explicit unknown reservations |

### `crates/bookradar-agent/tests/cli.rs` — 4 tests

| Function | Setup → expected result / regression |
|---|---|
| `operator_transcript_is_reproducible_offline` | Fresh workspace, configure, add, two checks → exact expected transcript |
| `invalid_arguments_fail_before_io` | Bad IDs/times/flags/secrets/config → usage exit before files, sockets, or credentials |
| `live_mode_requires_explicit_complete_probe_bounds` | Missing permit/model/key/caps → no outbound execution |
| `read_commands_and_stop_have_bounded_effects` | Inspect/history/settings and stop → reads unchanged; stop appends only its request |

### `crates/bookradar-agent/tests/ui.rs` — 6 tests

| Function | Setup → expected result / regression |
|---|---|
| `pages_show_watches_evidence_history_and_settings` | Completed synthetic runs → correct linked pages and provenance |
| `research_never_receives_checked_labels` | Agent claims and apparent approval text → Unverified only |
| `changes_preserve_access_currency_and_basis` | Access failure, changed currency/basis, omitted candidate → no false stock-out or price trend |
| `hostile_text_and_urls_are_inert` | Hostile watch/provider/run/page strings → escaped text and safe links |
| `monitor_routes_are_read_only` | Mutating methods and arbitrary routes → rejected without callbacks/writes |
| `refresh_uses_injected_time_and_latest_snapshot` | Advance fake clock/publish next run → deterministic updated page |

### `crates/bookradar-ui/tests/http.rs` — 2 additional tests

| Function | Setup → expected result / regression |
|---|---|
| `document_resolver_runs_only_after_request_validation` | Host/Origin/framing/method failures → resolver never invoked |
| `opt_in_documents_preserve_legacy_routes_and_head` | New resolver and existing fixed server → correct HEAD/security behavior; legacy allowlist unchanged |

New fixture:

`crates/bookradar-agent/tests/fixtures/core-loop.json`

```json
{
  "scenario": "bookradar-synthetic-v1",
  "base_unix": 1793548800,
  "search": {
    "web": {
      "results": [
        {
          "url": "https://retailer.example.invalid/book/atlas",
          "title": "Synthetic Atlas",
          "description": "Discovery pointer only."
        }
      ]
    }
  },
  "pages": [
    {
      "status": 200,
      "content_type": "text/plain; charset=utf-8",
      "body": "Title: Synthetic Atlas\nLanguage: Slovak\nAvailability: available\nPrice: 12.00 EUR per-copy\n"
    },
    {
      "status": 429,
      "content_type": "text/plain; charset=utf-8",
      "body": "Synthetic rate limit."
    }
  ],
  "repeat_last_page": true,
  "model_output": {
    "v": 1,
    "subject_quote": "Title: Synthetic Atlas",
    "language": {
      "value": "slovak",
      "quote": "Language: Slovak"
    },
    "availability": {
      "value": "available",
      "quote": "Availability: available"
    },
    "price": {
      "amount": "12.00",
      "currency": "EUR",
      "basis": "per-copy",
      "quote": "Price: 12.00 EUR per-copy"
    }
  }
}
```

The double serializes the search/model objects into their respective raw response shapes and consumes page responses in order. All hosts use the reserved `.invalid` namespace; no resolver or real transport is invoked. Negative variants are constructed in memory, avoiding additional fixture files.

Expected fixture:

`crates/bookradar-agent/tests/fixtures/operator-transcript.txt`

```text
created control_schema=1 research_schema=1 mode=offline
configured revision=2 interval_seconds=43200 live_enabled=false
added watch=1 target_language=slovak identity=unresolved
run=run:1 status=complete import=complete admitted=1 projected=1 verification=not-eligible
run=run:2 status=partial import=complete admitted=1 projected=1 verification=not-eligible
watch=1 attempts=2 latest_access=rate-limited latest_availability=unknown
change=access readable->rate-limited
```

Use first-run capture/observation at base + 2 and ingestion at base + 3; the second run starts at base + 43,200 with corresponding supplied attempt times. The failed response has no invented document capture.

The canonical gate and workflow remain unchanged. Workspace/default-member registration makes the gate cover the new package automatically. No second verification workflow, cache, release, or deployment step is needed.

## 11. Evidence and acceptance

Recommend **E3** for the combined implementation because it introduces outbound network policy, secret-bearing transport, new durable operational state, and crash recovery. E2 is plausible for a strictly offline-only adapter rehearsal, but would understate the proposed real-transport boundary. E3 does not imply deployment authority.

Implementation evidence:

- Focused tests for each stage before broad validation.
- All listed positive and negative trust-boundary tests.
- Exact synthetic CLI transcript above.
- Research receipt inspection proving two independent attempts, AgentOnly support, no approval, and unchanged replay behavior.
- Diff review proving protected files and accepted schemas remain unchanged.
- `CARGO_NET_OFFLINE=true bash scripts/verify.sh` on the clean committed candidate.

Independent acceptance requires a **Fresh Independent Audit**, `fresh-worker-session`, independence required. It must inspect the exact candidate commit, not treat this report or implementation tests as certification.

Browser acceptance is a separate fresh session with explicit adapter provisioning:

- Proposed adapter: isolated `playwright@1.65.1`, using an installed Chrome channel whose actual version is recorded.
- Origin: only the printed `http://127.0.0.1:<port>`.
- Viewports: `1280×800` and `375×812`.
- Check watch list, detail, settings, access failure, unknown language, history, change text, hostile text escaping, keyboard navigation, wrapping, and absence of positive research labels.
- Verify no external requests and no mutating routes.
- Use an exclusively created acceptance directory under `target/`; remove only owned temporary tooling/evidence paths and stop owned processes.
- Record one failure episode and at most two meaningful recovery attempts. Trigger the AP stall guard on repeated/conclusive no-progress; preserve missing evidence and use selective COOPERATOR observation where needed.

No browser adapter is currently exposed, and the inspected Python environment has no Playwright package. Historical browser success is not current capability proof.

Real probes remain optional and separately authorized. A proposed probe must name:

- Exact provider/model, retailer URLs/hosts, allowed public inputs, credential source, executable versions, and external disclosure.
- Maximum one Brave request, three model requests, three page-fetch workflows, and nine retailer HTTP hops, with stricter remaining allowances taking precedence.
- Explicit provider-cost acceptance; request caps must not be described as a monetary ceiling.
- Time/byte limits, no retries, one request in flight, output redaction, cleanup, and immediate stop on boundary failure.

Before such a probe, verify official provider contracts and model structured-output support under a new read-only source grant. No live success is claimed here.

COOPERATOR acceptance checklist:

1. Configure the application without storing keys.
2. Add a fictional book without resolving edition/language identity.
3. Run the complete offline flow and inspect source/time/quotation provenance.
4. Confirm research remains Unverified.
5. Observe a failed recheck without a stock-out claim.
6. Observe one scheduled check and coalesced manual triggering.
7. Restart and confirm frozen-import recovery without duplicate observations.
8. Review readable English pages at both viewports.
9. Confirm that deployment, service installation, and routine live operation remain unperformed.

Publication follows acceptance through a separate grant: normal non-force publication of the exact accepted commit, direct public-ref and content readback, and observation of the existing `verify` workflow for that SHA.

## 12. Documentation and ADRs

Update README with:

- Workspace/package purpose and the new CLI flow.
- Initialization, configuration, adding/enabling a watch, one-shot checking, foreground monitoring, stopping, and history.
- English read-only page routes.
- Synthetic fixture mode and explicit non-achievements.
- AgentOnly, uncertainty, access/stock separation, and governed review boundaries.
- Privacy disclosure, launch-time key handling, durable call accounting, and the distinction between count limits and spend.
- Crash/replay recovery and append-only retention.
- Ubuntu target and macOS development portability.
- Separate future deployment/service work.

Propose:

- `docs/adr/0009-local-agent-core-loop.md`: crate/process shape, CLI write boundary, control store, identities, scheduler/recovery, UI composition.
- `docs/adr/0010-bounded-provider-and-fetch-boundary.md`: named provider candidates, transport choice, credentials/privacy, extraction contract, URL/fetch controls, quotas, offline testing.

Both ADRs must include status/date/decision owner, ownership/lifecycle, context, accepted decision after review, alternatives, consequences, limitations, and links. Do not mark unapproved recommendations accepted.

Keep the domain contract, research-v1 reference, and ADRs 0001–0008 unchanged. No semantic-contract correction is proposed.

## 13. Allowlist, stages, rollback, and decisions

Exact proposed changed-path allowlist:

```text
Cargo.toml
Cargo.lock
README.md
crates/bookradar-agent/Cargo.toml
crates/bookradar-agent/src/lib.rs
crates/bookradar-agent/src/main.rs
crates/bookradar-agent/src/config.rs
crates/bookradar-agent/src/control.rs
crates/bookradar-agent/src/schema_v1.sql
crates/bookradar-agent/src/providers.rs
crates/bookradar-agent/src/transport.rs
crates/bookradar-agent/src/pipeline.rs
crates/bookradar-agent/src/extraction.rs
crates/bookradar-agent/src/scheduler.rs
crates/bookradar-agent/src/presentation.rs
crates/bookradar-agent/src/synthetic.rs
crates/bookradar-agent/tests/common/mod.rs
crates/bookradar-agent/tests/control.rs
crates/bookradar-agent/tests/providers.rs
crates/bookradar-agent/tests/fetch.rs
crates/bookradar-agent/tests/scheduler.rs
crates/bookradar-agent/tests/cli.rs
crates/bookradar-agent/tests/ui.rs
crates/bookradar-agent/tests/fixtures/core-loop.json
crates/bookradar-agent/tests/fixtures/operator-transcript.txt
crates/bookradar-ui/src/lib.rs
crates/bookradar-ui/src/http.rs
crates/bookradar-ui/tests/http.rs
docs/adr/0009-local-agent-core-loop.md
docs/adr/0010-bounded-provider-and-fetch-boundary.md
```

The root manifest change is limited to workspace/default-member registration. No core dependency or behavior changes are allowed.

Explicit exclusions: core sources/tests, all existing store sources/tests and binaries, both existing SQL schemas, domain/wire contracts, ADRs 0001–0008, the gate script, existing workflow, toolchain, ignore rules, root instructions, `.ap`, and all Meta files except separately authorized exact report persistence.

Implementation stages:

| Stage | User-visible result and gate | Stop condition |
|---|---|---|
| 1. Control and CLI | Initialize/configure/add/list a watch; control/CLI focused tests | Schema, ownership, append-only, or identity boundary fails |
| 2. Offline manual loop | One synthetic check with evidence/history; provider and replay tests | Provider output can bypass application construction or admission |
| 3. Read-only pages | Watch/detail/settings pages; UI and existing HTTP tests | Escaping, route, origin, method, or legacy-default regression |
| 4. Scheduler/recovery | Periodic checking, coalescence, stop/restart; injected-time tests | Duplicate dispatch, lost frozen batch, quota reuse, or fabricated time |
| 5. Dormant real adapters | Settings expose bounded capability; transport negative tests | Requires unapproved dependency, unsafe transport, credentials, or live call |
| 6. Candidate and documentation | Focused suite, fmt/clippy, exact diff/allowlist, documentation; commit then canonical clean gate | Any failed required gate; preserve cause and stop for bounded disposition |
| 7. Independent acceptance | Fresh audit and separately granted browser acceptance | Findings or absent evidence prevent acceptance |

Stages 1–6 may share one explicitly bounded implementation grant and one accountable Worker. They do not include independent acceptance, publication, deployment, or live probes.

Proposed commit subject:

`feat: add an offline-testable local agent core loop`

Rollback:

- Stop the foreground process and preserve all workspace databases.
- Revert the implementation commit through a separately authorized normal revert.
- Revert manifest/lockfile changes together.
- Do not delete, downgrade, migrate, or rewrite either accepted store or the new control history.
- Old tools continue using their original files; the new control format remains separate.
- No reset, clean, stash, force push, history rewrite, or publication is included.
- A failed canonical gate after candidate commit is reported with its first causal failure; further correction requires the bounded authority supplied by the implementation grant or a renewed grant.

Material decision table — **blank final cells are intentional**. The ORCHESTRATOR must obtain decisions before issuing implementation authority.

| Decision | Options | Recommendation | Rationale | Consequences / risks | COOPERATOR decision |
|---|---|---|---|---|---|
| Application surface | Extend store binaries; new application crate | `bookradar-agent` | Keeps research/review contracts intact | Adds one local package/CLI | |
| Write surface | Web forms; CLI | CLI | Smallest controlled administration surface | Operator uses terminal for writes | |
| UI composition | Extend shell; separate framework; CLI only | Opt-in read-only pages through existing UI library | Reuses current controls | HTTP refactor needs regression evidence | |
| Page scope | Broad dashboard; three bounded pages | Watches, detail, settings | Covers core loop | No browser editing | |
| Persistence | Existing formats only; new control store; migration | Separate control store described above | Existing formats lack operational state | New format/recovery ownership | |
| Owner scope | Implicit global state; explicit local owner | Explicit supplied local owner reference | Preserves watch semantics | No authentication or multi-user claim | |
| Candidate identity | URL/ISBN merge; provisional internal handles | Provisional handles | Avoids unsupported identity | Continuity remains uncertain | |
| Provider endpoints | Named candidates; alternate providers | Proposed NVIDIA/Brave routes | Matches selected design direction | Must verify contracts before real use | |
| Model | Fixed guessed model; explicit choice | Required configured model, no live default | Avoids unsupported capability assumptions | Live probes blocked until selected | |
| Query generation | Model-generated; deterministic | Deterministic bibliographic query | Fewer calls and failure modes | Less adaptive searching | |
| Structured output | Free text; strict JSON | Exact bounded JSON shape above | Rejects ambiguous output | Unsupported models fail visibly | |
| Extraction | Browser/parser stack; bounded source plus model | Bounded source plus quotation checks | Minimal honest AgentOnly route | No rendered-visibility guarantee | |
| Credential storage | Plain file; secret service; environment; none | No stored keys; launch-time injection for authorized probes | Portable and limited retention | Process environment remains sensitive | |
| External disclosure | Unrestricted context; bounded book/page inputs | Explicit bounded public inputs | Minimizes disclosure | Reveals search interest to providers | |
| Live-call posture | Routine activation; probe-only; offline | Offline by default, separately authorized probes | Preserves current authority | Routine live monitoring unaccepted | |
| Cost/caps | Monthly rollover; lifetime allowances; monetary estimate | Zero live allowance until explicit bounded grant; durable reservations | No invented billing guarantee | A later cost decision is required | |
| Search/page breadth | Unbounded; bounded candidates | Five search results, three tracked candidates | Coherent small slice | Limited retailer/offer coverage | |
| Fetch transport | New Rust stack; controlled curl | Existing pins plus controlled curl | No new registry graph | Subprocess and host-version obligations | |
| Curl acceptance | Accept ambient version; exact preflight | Record/approve exact build before real probe | Installed version alone proves little | Ubuntu/security validation pending | |
| Address policy | IPv4/IPv6; initial IPv4-only | Public IPv4 only, pinned connection | Smaller auditable boundary | Some sites unsupported | |
| Redirect/retry policy | Automatic; manual bounded | Two validated redirects, no retry | Prevents unchecked navigation | More partial outcomes | |
| Fetch bounds | Larger configurable bounds; fixed initial bounds | Limits in §5 | Bounded resource use | Dynamic/large pages may fail | |
| Interval | Other interval; 12 hours | Configurable 43,200-second default | Two regular daily opportunities without coupling to freshness | Requires running process | |
| Catch-up | Replay missed slots; skip; once | One overdue catch-up, then interval from terminal attempt | Avoids bursts | Missed periods remain gaps | |
| Concurrency/coalescence | Parallel; sequential | One run, coalesce by watch | Simpler accounting/recovery | Longer queues | |
| Recovery | Repeat calls; resume frozen import | Resume import only; interrupted calls stay unknown/consumed | Avoids duplicate effects | Some incomplete work needs a new run | |
| Change surface | Notifications; visible history | Detail-page changes only | Meets accepted core loop | No external/in-app notification feed | |
| Runtime/process | Async framework; synchronous foreground | Std threads and bounded child transport | Sufficient for sequential work | Explicit stop/restart handling | |
| Rust dependencies | New network/UI graph; existing pins | Reuse exact existing pins | Limits lockfile/supply-chain change | More boundary code to audit | |
| Evidence tier | E2; E3 | E3 | New network/credential/recovery boundaries | Separate fresh final acceptance | |
| Independent audit | Same-session; fresh | Fresh independent Worker | Required separation | Separate grant/session | |
| Browser route | Provision isolated adapter; manual evidence | Isolated pinned adapter in fresh session, bounded stall guard | Repeatable rendered evidence | Provisioning/current Chrome capability unverified | |
| Live acceptance | Required now; optional later | Optional separately authorized probe | Offline evidence cannot prove live behavior | No live success claim | |
| Documentation | One broad ADR; two focused ADRs | README plus ADRs 0009/0010 | Separates lifecycle from provider boundary | Accepted status follows decisions only | |
| Git delivery | Combined push; local candidate then publication | One local candidate, separate publication | Exact accepted artifact remains reviewable | Commit/revert authority must be explicit | |
| Allowlist/stages | Broader cleanup; exact listed paths | Exact allowlist and gates above | Prevents adjacent scope | Stop on required expansion | |
| Deployment/service | Include installation; later whole | Later separately authorized Ubuntu deployment/service work | Current whole establishes the loop | No installed background service here | |

## Open questions and missing evidence

- The material decision cells above remain unapproved. They are recommendations for review, not silent selections.
- Required report-file persistence and saved-file hash/readback remain incomplete under native Plan Mode.
- Provider documentation, exact live model, structured-output compatibility, account terms, credentials, and cost limits were not verified or exercised.
- The exact transport build and behavior on Ubuntu require later preflight and acceptance.
- Browser acceptance tooling is not presently established.
- No new implementation, test, browser, provider, retailer, service, deployment, acceptance, or publication result exists.

Orchestration critique:

MEASURED: Native Plan Mode permits the planning exchange but prevents required file persistence; the named plan-output fallback preserves the complete report. The smallest correction is exact report-only persistence through the permitted completion route.

LEAD: none.

### Report for ORCHESTRATOR_CHAT

**APMC-S6-PLAN — Django-admin diagnostic views**

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 20, Worker exchange ordinal: 01
```

- **Status:** PASS — bounded advisory planning complete.
- **Phase-qualified result:** not-applicable.
- **Start/end commit:** both `96c797fdc9540174cb4a06043e2cbe3865fcb9bf`.
- **Repository gate:** `main`; AP gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; porcelain empty at start and end.
- **Changed files:** none.
- **Validation:** read-only source, schema, test, installed-Django, and historical-design inspection. No tests executed; no network, provider calls, secret-file access, or delegation.
- **Commit/push:** not-applicable.
- **Evidence:** E0, non-independent. Implementation and rendered acceptance remain unperformed.
- **Smallest next step:** ORCHESTRATOR reviews this plan and issues one explicit implementation grant to a fresh Worker with `Native planning mode: not-used`.
- **Report justification:** new-evidence.
- **Authority expiry:** this terminal report expires the planning grant. Implementation in this session remains prohibited; the logical whole remains not-closed.

**Resolved Execution Issues / Near-Misses:** none.  
**Pre-Existing Failure Classification:** no executed-test failures; measured presentation gaps and historical mismatches appear in D7.  
**Enumeration widened:** report serializers and schema, aggregation tests, cancellation service, installed Django wrappers, and the cited historical handout/design.  
**Context pressure:** low; sufficient context retained for this report.

### D1 — Live view

**Use the existing DiagnosticRun change URL as the single live-and-finished page.** Override `DiagnosticRunAdmin.change_view` with an explicitly read-only `TemplateResponse`, using a dedicated template extending `admin/base_site.html`. Do not invoke the default change-form rendering path: it exposes fields unnecessary for this surface and provides no ply log.

Successful launch redirects to `admin:game_diagnosticrun_change` for the newly created UUID. Replace the success copy with:

> “Diagnostic run launched in fake mode. This page shows its heartbeat, recorded plies, and report when available.”

**Refresh mechanism:** HTTP `Refresh: 2`, emitted only on successful GET responses whose loaded status is `queued` or `running`. Use no URL in the header, no meta refresh, no new JavaScript, and no JSON polling endpoint. A full-page refresh supplies the required information without adding a script or data-injection surface to an admin without CSP.

All other statuses—including `completed`, `failed`, `cancelled`, `abandoned`, and `blocked_dependency`—receive no Refresh header. Every page provides a manual reload link.

**Diagnostic query budget per in-flight refresh:**

1. One PK lookup of `DiagnosticRun`, without related-object traversal.
2. One query for that run’s latest 20 `DiagnosticPly` rows, ordered by descending `ply_index`, with an explicit scalar-field projection.

Reverse those 20 rows in memory for chronological presentation. Obtain the last-ply identity and last recorded index from the same result. No additional count, latest-row, session, catalog, or report-file query. Ordinary session/authentication/admin-navigation queries are outside this diagnostic-data budget.

Display:

- Run UUID, status, instrument, both seat model IDs, assist mode, and executed runtime mode.
- Heartbeat timestamp and age; “No heartbeat recorded” for null. Explain the existing heartbeat cadence: every five plies or approximately 30 seconds.
- Last recorded zero-based `ply_index` and configured ply cap. Do not label the cap as the expected position-set size.
- Latest seat/model/completion source; null source reads “Not measured.”
- A bounded chronological ply table with identity, runtime mode, score authority, completion source, terminal cause, measured score fields, request count, and elapsed time.
- “Showing the latest 20 recorded plies”; no implication that earlier rows disappeared.
- A CSRF-protected Cancel POST button for users with change permission while the run is in flight.

Cancellation delegates to the existing `cancel_diagnostic_run`. A terminal-state race produces an informational message and redirects back without retrying or changing runner behavior.

### D2 — Finished report

The same change URL renders terminal metadata, the retained ply table, and a structured report. Introduce a presentation helper that reads a confined artifact and returns explicit metadata, metric rows, sample rows, and an availability state. It never runs a report builder or the diagnostic command.

**Model-position presentation**

Render the artifact identity, report kind, generation time, source revision, provider/model identity, digest, variant, assist mode, `executed_runtime_mode`, and run/sample `score_authority`. Keep absent run authority visibly absent; do not substitute a sample’s value.

Show every landed summary field:

- `sample_count`, `pass_count`, `fail_count`
- `position_count`, `unattempted_count`, `end_reason`, `truncated`
- `move_quality_sample_count`, `did_not_measure`, and whether `move_quality_ratio` is present
- `completion_source_counts`, `completion_source_did_not_measure_count`
- `total_provider_requests`, or “Not measured” when omitted

Label pass/fail counts **“Recorded diagnostic verdicts.”** They are neither model ratings nor deployment recommendations.

Render the histogram as six text rows in the existing vocabulary order:

`provider_candidate`, `backend_ranked_candidate`, `repair_candidate`, `backend_witness_rescue`, `genuine_no_move_exchange`, `genuine_no_move_pass`.

Missing source observations have a separate count, never a seventh source. A stored zero remains zero; absent histogram data remains unavailable.

Render all 24 samples for the committed full fixture, or the actual recorded subset for partial runs. Include position index, model/seat, verdict/reason, nullable scores, baseline completeness, source, authority, runtime, and other existing ply metrics. Use expandable, autoescaped text details for the longer metric list.

**Required fake-run copy**

For the landed 24-position `generic_unchanged` artifact, display prominently:

> “Fake diagnostic run — model quality was not measured. All 24 position scores are null; did_not_measure = 24. The 24 recorded ‘fail’ verdicts describe the generic_unchanged test path. They do not show that this model plays well or badly. score_authority = engine does not change this.”

Use count-aware wording for shorter runs. Do not apply success/failure rating colors to those counts.

**LTAI component text**

Compute presentation-only component summaries from the artifact’s existing primitives:

| Component | Observations used | Display floor |
|---|---|---:|
| Tool-valid rate | Measured integer `valid_candidate_count`; success when greater than zero | 20 |
| First-call-valid rate | Measured boolean `first_validate_valid` | 20 |
| Give-up-when-legal rate | Measured boolean `give_up_while_legal` | 20 |
| Authorship rate | Measured boolean `model_authored` | 20 |
| Malformed rate | Measured boolean `malformed_or_non_tool` | 20 |
| Move-quality ratio | Existing eligible per-sample ratios and D3 mean | 8 |

Each component shows measured sample count, its own `did_not_measure`, and its floor. Nulls do not become false; booleans do not become integer measurements. Unattempted positions stay separate from attempted-but-unmeasured samples.

Below the floor, show “Insufficient sample (n/required).” Fake observations remain explicitly diagnostic-only even when plentiful. For MQR, distinguish “not recorded” from “recorded, insufficient sample.” Preserve measured zero and ratios above one; show baseline completeness.

The current grant specifies **components as text**. It adds no composite calculation, editable weights, or persistent statistics model. Show “LTAI composite: not available in this report.”

**Ai-match presentation**

Render match end reason, plies, bag/rack remainder, engine final scores, and per-ply metrics grouped by seat/model. Distinguish the report’s match `sample_count` from its ply count.

Required accompanying copy:

> “Full-game diagnostic. Final scores are engine results. This report describes the executed game and assistance; it does not establish a model-strength ranking.”

Do not manufacture position-set D3 fields or an MQR when the artifact does not contain them.

**Unavailable and partial reports**

- Empty `report_path`: “No report is available for this run.” Retain terminal metadata and recorded plies.
- Mixed-seat position-set run: additionally explain that the current publisher requires one provider/model pair.
- Missing, unreadable, oversized, malformed, mismatched, or unsupported artifact: show a specific fixed availability message without filesystem paths or exception text.
- A terminal run may precede report publication: show “A report may become available after finalization. Reload to check.” No spinner or automatic refresh.
- Preserve stored `truncated` exactly. Independently label failed/cancelled/abandoned runs or unattempted positions as incomplete evidence; do not rewrite `truncated=false`.

### D3 — Cross-model comparison

Add `DiagnosticRunAdmin` GET route `compare/`, linked from the changelist and run page. No catalog change is needed.

Use a paginated table of terminal `position-set` runs, 20 runs per page, newest first before grouping. Provide an optional exact 64-hex digest GET filter. Parse at most 20 artifacts per request through the same confined reader.

**Comparison eligibility**

A run can supply comparable measured evidence only when:

- Status is `completed`, instrument is `position-set`, and artifact kind is `model-position`.
- Artifact run ID, instrument, variant, digest, assist mode, and runtime declarations agree with the run.
- Both run seats identify the same model; requested model and every sample model agree. Provider identity is present in the artifact.
- Position indices are unique; sample/digest identities and D3 counts are internally consistent.
- Runtime is consistently `live`; `truncated=false`; `unattempted_count=0`.
- Each displayed metric independently meets its measurement floor.

Use separate comparison groups for digest, variant, assist mode, runtime, source revision, persisted prompt ID, script, queue mode, and configured caps. Missing provenance prevents qualification.

Within those groups, group by **`model_id`**, retaining provider identity and one row per run. Never pool repeated runs, merge providers sharing a model ID, average run means, or combine different digests. Order model groups alphabetically and repeated runs newest first; there is no performance ranking.

Columns:

- Model, provider, run link/date, status, and evidence state
- Six-source histogram and source missingness
- MQR value or explicit absent/insufficient/fake state
- `sample_count`, `move_quality_sample_count`, `did_not_measure`
- `unattempted_count`, `truncated`, `executed_runtime_mode`

Fake, insufficient, partial, failed, mismatched, and no-report runs remain visible with explicit exclusion reasons. Mixed-pair rows show both seat IDs without attributing observations to either model. Full-game runs remain accessible through the run list but do not enter this position-set table.

Display no final-score column, winner badge, deployment recommendation, or sort-order action. State that the table covers the displayed runs and contains no rolling statistics. Existing prompt IDs are not historical prompt-content fingerprints; make that provenance limitation visible.

### D4 — Security rails

| Surface | Methods | Wrapper and permission | CSRF / effects |
|---|---|---|---|
| Existing run change URL, replaced rendering | GET only | Inherited `admin_view`; explicit `has_view_permission(request, run)` | Read-only; reject other methods |
| New `compare/` | GET only | Explicit `admin_view`; `has_view_permission` | Read-only; reject other methods |
| New `<uuid:run_id>/cancel/` | POST only | Explicit `admin_view`; `has_change_permission(request, run)` | CSRF required; existing cancel service only |
| Existing `launch/` | Existing GET/POST behavior | Existing `admin_view` and change guard | Existing launch authority; only redirect/copy changes |

Register custom URLs before Django’s catch-all object URLs. Invalid/missing run IDs return 404. Unauthorized requests must fail before artifact access. View-only staff can inspect reports but cannot launch or cancel. Retain `admin_view`’s non-cacheable responses.

**XSS path:** database/artifact string → validated plain Python scalar → explicit template context → autoescaped text node. This applies to `model_id`, `reason_code`, `completion_source`, failure strings, and any subsequently approved model-produced field. Unknown source values may appear only as escaped diagnostic text; they invalidate histogram qualification.

No raw HTML construction, `|safe`, `mark_safe`, HTML-bearing helper output, JSON-to-script injection, or DOM HTML sink. Dynamic artifact strings never choose CSS classes, element IDs, URLs, or template names. Links use reversed admin URLs and validated UUIDs.

**Confined file reader**

- Derive the directory from the installed backend source location, matching the runner’s `backend/var/diagnostics/`.
- Construct only `<run-uuid>-report.json`; require the persisted nonempty `report_path` to match that canonical expected path. Never open the stored string directly.
- Open `var`, `diagnostics`, and the expected filename relative to trusted directory descriptors, refusing symlinks. Use no-follow directory/file opens, nonblocking file open, and `fstat` to require a regular file.
- Limit reads to **2 MiB**, checking both file size and actual bytes read. Unsupported no-follow capability fails closed.
- Parse strict UTF-8 JSON; reject duplicate keys, nonfinite numbers, invalid structures, and inconsistent identities/counts. Close descriptors on every path.
- Never read a log file, follow an artifact-supplied filename, or fall back to another run’s report.

Use an explicit display-field allowlist and the existing redaction policy as defense in depth. Do not serialize the complete artifact or `parameters_json` into HTML. Unknown fields are ignored; no secret recovery from environment, parameters, or logs.

Django’s absent CSP is a measured residual, not protection supplied by Next.js. This slice adds no script requirement or project-wide CSP change. Existing Axes/login behavior and accepted F01/F02/F03 residuals remain unchanged. No new HTTP API or throttle scope is introduced.

### D5 — One implementation exchange: allowlist, fail-before, evidence

**Exact proposed implementation allowlist**

1. `backend/game/admin.py`
2. `backend/game/diagnostic_admin_reports.py` — new confined reader and presentation helpers
3. `backend/game/templates/admin/game/diagnosticrun/change_list.html`
4. `backend/game/templates/admin/game/diagnosticrun/change_form.html` — new
5. `backend/game/templates/admin/game/diagnosticrun/report.html` — new partial
6. `backend/game/templates/admin/game/diagnosticrun/comparison.html` — new
7. `backend/tests/test_diagnostic_admin.py` — new focused coverage

No public API, model, migration, artifact schema, or diagnostic vocabulary changes. The only new interfaces are the two admin routes and internal presentation helpers.

**Negative authority:** no gamecore, frozen migrations 0009/0010/0011, runner loop, report-builder changes, Node worker, mint/authentication changes, `diagnostics.py` vocabulary changes, frontend, `base_url`, K1, slice 8, or accepted-residual remediation.

| ID | Fail-before condition | Required implementation evidence |
|---|---|---|
| S6-F01 | Launch returns to changelist; change page lacks promised progress | Successful launch targets its run page; latest ply identity renders |
| S6-F02 | No bounded live-refresh surface | Refresh only for queued/running; all five terminal statuses stop; exactly one run lookup plus one capped ply query |
| S6-F03 | Fake verdict counts could appear as model performance | Exact 24-null/24-unmeasured warning; no rating or invented zero |
| S6-F04 | D3 missingness and LTAI components lack presentation | All D3 fields; component-specific missingness; 19/20 and 7/8 floor boundaries; genuine zero and ratio above one |
| S6-F05 | Empty report or terminal-publication race lacks honest state | Stable empty/error states and manual reload; no terminal spinner |
| S6-F06 | New HTML surface could turn stored strings into executable markup | Malicious strings remain text across metadata, samples, histogram diagnostics, and comparison |
| S6-F07 | New reader could expose arbitrary files | Reject traversal, other-run filenames, file/directory symlinks, FIFO/directory, oversize, malformed JSON, identity mismatch |
| S6-F08 | Staff-only wrapper could be mistaken for model permission | Anonymous/nonstaff denied; staff without model permission denied; view-only inspection allowed; cancel requires change plus CSRF; GET never cancels |
| S6-F09 | Comparison could merge incompatible or inadequate evidence | Digest/provider/model/mode/provenance separation; no pooling; fake/partial/no-report rows excluded from measured comparison |
| S6-F10 | Presentation could trigger diagnostic work | GET tests assert no spawn, mint, runner, provider access, report write, or diagnostic state mutation |

F06–F10 are preventive acceptance conditions for new surfaces, not claims of demonstrated baseline exploits.

**Validation for the following exchange**

Use synthetic DB rows and temporary artifact directories. Patch spawning for launch tests; do not drive diagnostics through a browser or contact providers. Test query bounds after accounting separately for ordinary admin authentication queries.

Run the focused new suite, then backend Ruff, mypy over `config game gamecore accounts catalog`, and the backend pytest suite through the declared interpreter route:

`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python`

Use one existing pytest `-q` from configuration, no dependency installation, no frontend build, and no unauthorized live tests.

**Tier:** one coherent E2 exchange, no tier spread. The three views share artifact projection and session-authenticated HTML boundaries; cancellation reuses the existing authorized primitive. No 6-IA is required unless implementation introduces a new privilege, mint, or live-provider path.

**Acceptance:** the Cooperator personally reviews `/admin/` for navigation, readability, refreshing, cancellation, finished reports, and comparison states. Worker browser MCP remains forbidden. Automated HTML assertions do not constitute rendered acceptance.

**Git for the later grant:** work on `main`, stage only the seven explicit paths, commit, and perform a non-force push to main only under that implementation grant’s network/publication authority. No branch creation. This planning grant authorizes no Git mutation or network operation.

### D6 — Boundaries

**K1:** These views consume existing rows and artifacts. Measurement floors concern evidence presentation, not provider-budget calibration. Synthetic fixtures can prove rendering, missingness, grouping, and security with zero provider calls. K1 remains separately authorized work.

**Base URL:** Reading a local report and rendering admin HTML requires no provider target or arbitrary HTTP destination. Adding `base_url` would introduce the slice-7 SSRF boundary and exceed this grant.

**Hardcoded 3b fill:** The accepted producer deliberately supplies null scores, fail verdicts, and `generic_unchanged_turn`. Slice 6 preserves and explains those values. Altering them would change measurement semantics and exceed presentation authority.

**Later measured live runs:** Once an independently authorized producer emits consistent live measurements, the same page displays the stored ratios, measured counts, missingness, source distribution, and baseline completeness. MQR becomes a comparison value at eight eligible samples; measured zero remains zero and values above one remain unclamped. The UI does not enable live execution or infer deployment readiness.

### D7 — Orchestration critique

- **MEASURED:** [Landed admin](/home/agile/Projects/libretiles/backend/game/admin.py:623) promises plies on the change page but redirects to the changelist. `DiagnosticRunAdmin` has neither a custom change template nor a DiagnosticPly inline. **LEAD:** step 5 must treat all three presentation surfaces as unimplemented and require redirect plus actual ply-rendering evidence.

- **MEASURED:** The [accepted D11](/home/agile/meta/projects/libretiles/11/00-admin-provider-model-console/01_report_01.md:406) names both game and catalog template trees, while the older D10 places comparison under `AIModelAdmin`. Its wording also mentions views/static beneath template paths. The current prompt explicitly selects `DiagnosticRunAdmin`. **LEAD:** the next grant should use D5’s exact paths; catalog access and static JavaScript are unnecessary.

- **MEASURED:** [91_ step 5](/home/agile/meta/projects/libretiles/11/00-admin-provider-model-console/91_orchestrator-handout-1.md:224) says “LTAI + components.” The current grant specifies components as text. The landed schema/model contains no composite weights or rolling-statistics implementation. **LEAD:** record the narrowed deliverable explicitly; this plan does not claim to implement the older composite or editable-weight ambition.

- **MEASURED:** The earlier accepted design supplies the 20-ply and eight-authored-sample floors. The current prompt requests insufficient-sample states without repeating those numbers. **LEAD:** carry those established floors into the implementation grant instead of inventing new thresholds.

- **MEASURED:** `_complete` stores terminal status before `_write_report` publishes the artifact. The existing authorship-abort regression asserts `failed`, unattempted positions, and `truncated=false`. **LEAD:** terminal refresh cessation requires a manual-reload publication state; completeness must not depend solely on `truncated`.

- **MEASURED:** D3 supplies MQR missingness and histograms, while several LTAI primitives remain null in the runner. Historical prompt-content fingerprints are not persisted. **LEAD:** this slice can deliver truthful inspection and descriptive comparison; the absolute deployment-selection goal remains constrained by measurement and provenance that this grant cannot create.

**Defaults fixed by this plan:** HTTP refresh at two seconds; 20 live ply rows; 20 comparison runs per page; 2 MiB artifact limit; established 20/8 metric floors; English diagnostic copy; no composite, pooling, or automatic model ranking.

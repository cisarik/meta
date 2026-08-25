### Report for ORCHESTRATOR_CHAT

Echoed coordinates:

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 05
Worker exchange ordinal: 01
```

Worker session target: `fresh-worker-session`. Native planning mode: not-used.
Profile: Fresh Infosec Remediation Worker. Continuity anchor: audit report
`10_report_00.md` against commit `f59f4018eb86dfb40d339458d1d50dc208edcdd3`.
Authority renewal: none; single bounded remediation grant.

## Capability handshake

| Dimension | Declared fact | Evidence class |
|---|---|---|
| Client/product | opencode CLI agent, Linux/bash environment | directly observed |
| Model identity | `stealth/ox-alpha` via OpenRouter (self-reported label) | requested/self-reported; not independently verifiable |
| Reasoning profile | Extra High requested by prompt | requested; not observably exposed |
| Native planning mode | off (`not-used`); no planner artifact created | per prompt |
| Filesystem read/write | canonical checkout mutation restricted to exact allowlisted paths; one Meta report path | granted; exercised within allowlist |
| Git writes | commits on `feat/x-meme-browser-companion`, no push | granted; four commits, zero pushes |
| Python/tests | exclusively via `./.ap/ap project check` / `./.ap/ap exec` with exact `--baseline`; zero ambient interpreter invocations | directly observed |
| Network/browser/NUC/SSH/sudo/provider/push/deployment | prohibited by grant; not invoked | permission boundary honored |

Precondition gate at start: HEAD = `f59f4018eb86dfb40d339458d1d50dc208edcdd3`
(matched declared baseline), worktree clean, `.ap` submodule HEAD =
`9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (matched declared pin), branch =
`feat/x-meme-browser-companion`. Gate passed; work proceeded. Provenance probe
(`runtime-info`) resolved `framenest.__file__` to
`/home/agile/Projects/framenest/src/framenest/__init__.py` under the canonical
root.

## Commits

Start commit: `f59f4018eb86dfb40d339458d1d50dc208edcdd3`
End commit: `3a21405e0b0c0b7bdeddbb64ac1e2ea1a2f04e04` (short `3a21405`)

```text
git log --oneline -6
3a21405 fix: bound analysis proposals with per-user hourly rate limit (audit F-3)
4b7b87e fix: percent-encode read-only sqlite uri path (audit F-6)
d3b203f fix: uniform sanitized 404 and loud failures on public surface (audit F-1, F-4, F-5)
bcf5ec1 fix: require loopback host for tcp ingress mode (audit F-2)
f59f401 feat: audited administrator team-alias reads
da06109 feat: durable ordinary-user analysis proposals
```

No push performed. Worktree clean after commits.

## Changed files and purpose

Repository (all inside the allowlist):

| File | Finding(s) | Change |
|---|---|---|
| `src/framenest/configuration.py` | F-2 | tcp-mode loopback guard in `validate_ingress_configuration`; `_TCP_INGRESS_CONFIGURATION_MESSAGE` names the constraint |
| `src/framenest/adapters/api/public_published_application.py` | F-1, F-4, F-5 | `RequestValidationError` handler returning the uniform 404; startup-time companion-marker verification; sanitized structured-log emits on failure paths |
| `src/framenest/adapters/api/public_published_api.py` | F-4, F-5 | serve-time marker re-check in `root()`; `index_html_contains_companion_marker()` helper; `_failed_response(exc)` logging on every broad except block |
| `src/framenest/application/analysis_proposal.py` | F-3 | `AnalysisProposalLimitError`, `DEFAULT_ANALYSIS_PROPOSAL_MAX_SUBMITS_PER_HOUR = 6`, `MS_PER_HOUR`, per-user rolling-window enforcement in `ProposeAnalysis`; docstring updated from "duplicates allowed" to bounded submissions |
| `src/framenest/application/ports/analysis_proposal.py` | F-3 | Protocol method `count_created_since(login_key, since_ms)` |
| `src/framenest/infrastructure/persistence/analysis_proposal_repository.py` | F-3 | durable `count_created_since` implementation (SQLAlchemy count, sanitized repository error mapping) |
| `src/framenest/adapters/api/analysis_proposal_api.py` | F-3 | maps limit error to sanitized 429; `429` added to declared responses |
| `src/framenest/infrastructure/persistence/engine.py` | F-6 | read-only URI composes `quote(path.as_posix(), safe="/")` before `file:…?mode=ro` |
| `tests/unit/test_configuration_ingress.py` | F-2 | 6 new tests (loopback IPv4/IPv6 accept; six non-loopback IPv4/IPv6 rejects; env-var fail-closed; UDS modes unconstrained) |
| `tests/unit/test_configuration.py`, `tests/unit/test_server_runtime.py`, `tests/contract/test_atomic_upload_publication_contract.py`, `tests/contract/test_youtube_cli.py` | F-2 harness alignment | see "Harness alignment" below |
| `tests/contract/test_public_published_uds.py` | F-1, F-4, F-5 | byte-level uniform-404 validation probes; companion-marker startup/serve-time fail-closed tests; sanitized-log content tests |
| `tests/unit/application/test_propose_analysis.py` | F-3 | limit enforcement, window reset, per-user isolation, disabled sentinel, constant mirror of the requester pattern |
| `tests/contract/test_analysis_proposal.py` | F-3 | 4 HTTP contract tests (sanitized 429 body, window reset, user isolation, admin list unaffected) with dependency-injected small limits and a controllable clock |
| `tests/unit/infrastructure/persistence/test_engine_readonly_uri.py` | F-6 | new file; reserved-character paths (`?`, `#`, `%`, spaces, `&`) open read-only; write refusal preserved on encoded path |

`server.py` was **not** modified: the F-2 guard fails at settings load with an
explicit pydantic `ValidationError` naming the constraint before any server
composition runs, so no additional startup-error surfacing was required.

Meta: this report file only.

## Per-finding closure evidence

### F-1 (Condition C1) — public 422 validation leakage closed

- Handler registered at
  `src/framenest/adapters/api/public_published_application.py:210`
  (`@app.exception_handler(RequestValidationError)` returning
  `public_not_found_response()`, preceded by one sanitized WARNING emit).
- FastAPI installs its default validation handler via `setdefault`
  (`.venv/.../fastapi/applications.py:1005`), so an explicit registration
  fully replaces it; no reachable stock 422 remains on the public app.
- Contract proof
  `test_malformed_and_out_of_range_requests_match_uniform_404` asserts
  **byte-level equality** (`response.content == reference.content`) with the
  standard catch-all 404 envelope for: `/api/media/not-a-uuid`,
  short/malformed UUID metadata path,
  `/api/media/{id}/locations/not-a-uuid/content`,
  `/api/media/{id}/locations/not-a-uuid/gallery-preview`,
  `limit=9999`, `limit=0`, `limit=abc`, `offset=-1`, `tag=%FF` — plus
  `nosniff`, `no-store`, and JSON body equality via `_not_found`.

### F-2 (Condition C2) — tcp-mode loopback guard

- Guard: `src/framenest/configuration.py:449-450` —
  `if not ip_address(self.host).is_loopback: raise ValueError(...)` when
  `ingress_mode == tcp`; message constant `configuration.py:75` names the
  constraint ("tcp ingress requires the host to be a loopback address;
  binding the full workspace application to a non-loopback address is
  rejected"). Settings load fails closed. UDS modes untouched. **No
  dev-override escape hatch added**, per grant.
- Unit matrix: loopback `127.0.0.1` and `::1` accepted; `0.0.0.0`,
  `192.168.1.50`, `8.8.8.8`, `::`, `2001:db8::1`, `fe80::1` rejected;
  `FRAMENEST_HOST=0.0.0.0` env path rejected; tailscale_uds and
  public_published_uds both construct successfully with `host="0.0.0.0"`
  (host unconstrained off-tcp).

### F-4 — companion-marker replacement verified loudly

- Startup: `create_public_published_app` calls
  `index_html_contains_companion_marker()` **before** engine composition;
  missing marker or unreadable index asset raises
  `PublicPublishedStartupError` (fail-closed process start).
- Serve time: `root()` raises `RuntimeError` when the marker is absent so a
  drifted page can never be served referencing
  `/assets/companion_host.js` (which the allowlist would 404); the raised
  failure flows into the logged uniform-500 path.
- Tests: page served by the real composition contains no `companion_host.js`;
  monkeypatched marker-less asset aborts startup; monkeypatched serve-time
  absence yields HTTP 500 instead of a silently broken page.

### F-5 — sanitized structured logs on public failure paths

- Emits (error code/class only; never paths, queries, identity data, or
  exception text):
  - `public_request_validation_rejected` WARNING
    (`public_published_application.py:215`),
  - `public_unexpected_failure` ERROR with type-only exception
    (`:230`),
  - `public_http_exception_rejected` WARNING with `HTTP_<status>` code for
    non-sanitized Starlette statuses (`:247`),
  - `public_read_failed` ERROR with type-only exception inside
    `_failed_response(exc)` covering all 13 named/broad failure branches in
    `public_published_api.py`.
- Content proof: `test_public_read_failure_logs_only_sanitized_error_class`
  forces `RuntimeError("leak attempt /srv/media/private clip.mp4")` through
  the real redaction filter + JSON formatter and asserts the rendered line
  contains only `{"type": "RuntimeError"}` with none of the planted secret
  strings. `test_validation_rejection_logs_no_request_details` asserts the
  attacker input `not-a-uuid` never reaches the log line.

### F-6 — read-only URI percent-encoding

- `engine.py`: `quote(normalized_path.as_posix(), safe="/")` before composing
  `file:<encoded>?mode=ro`, so `?`, `#`, `%`, whitespace, and `&` in operator
  paths can no longer alter URI parsing semantics.
- Tests prove reserved-character databases open correctly at revision `0033`
  and remain write-refusing under `query_only`.

### F-3 (Cooperator disposition B) — per-user proposal submit rate limit

- Mechanism mirrors the YouTube/X requester limiter exactly: durable
  per-user window count (`count_created_since`) → threshold compare against
  `max_submits_per_hour` (default `6`, same constants style as
  `DEFAULT_X_REQUEST_MAX_SUBMITS_PER_HOUR`/YouTube) → typed limit error
  `(code, message)` shaped like `XRequestLimitError` → honest sanitized 429
  `{"error": {"code": "ANALYSIS_PROPOSAL_RATE_LIMIT", "message": "Too many
  analysis proposals this hour."}}` with `Cache-Control: no-store`.
- Enforcement sits after input/media-id validation and before row creation;
  negative sentinel disables; existing YouTube/X limiters untouched.
- Audit non-regression: the Tailscale middleware records the authorized
  attempt pre-dispatch and stamps status best-effort afterwards
  (`tailscale_ingress.py:882-927`), so a 429 response cannot suppress or
  alter recording; the existing `test_trusted_ingress_records_propose_audit_event`
  remains green.
- Required tests all present and passing: limit enforcement, window reset
  (clock advanced `MS_PER_HOUR + 1`), per-user isolation (Bob unaffected by
  Alice's exhaustion), admin list unaffected while a user is limited.

## Validation evidence

Canonical route only (`./.ap/ap project check` / `./.ap/ap exec` with exact
`--baseline f59f4018eb86dfb40d339458d1d50dc208edcdd3`). Zero ambient Python
invocations.

```text
./.ap/ap project check --candidate            -> PASS (non-authorizing readiness)
./.ap/ap exec ... --operation runtime-info    -> PASS; provenance resolves to
                                                 canonical checkout src/
Focused run 1 (unit):                          63 passed in 0.31s
  tests/unit/test_configuration_ingress.py
  tests/unit/application/test_propose_analysis.py
  tests/unit/infrastructure/persistence/test_engine_readonly_uri.py
Focused run 2 (contract):                      31 passed in 12.77s
  tests/contract/test_public_published_uds.py
  tests/contract/test_analysis_proposal.py
Full declared operation (--operation test):    3300 passed, 8 skipped,
                                               0 failed in 517.62s
```

Failure classification history (honest):

- First full run: `5 failed, 3295 passed, 8 skipped`. All five were
  **harness assertions of the pre-F-2 fail-open contract**, not product
  regressions: two env-file precedence tests and one propagation test used
  non-loopback sample hosts incidentally; one upload-publication contract
  test asserted composition-time behavior for `host="0.0.0.0"` that is now
  enforced earlier and more strictly by the guard itself; one YouTube CLI
  exit-code test deliberately fed `host="192.0.2.1"` to reach the CLI's own
  loopback boundary check. All were aligned within `tests/**`:
  loopback sample addresses (`127.0.0.x`), the composition test rewritten to
  assert fail-closed `ValidationError`, and the CLI test now injects the
  legacy unvalidated state via `model_copy(update={"host": ...})` so the
  CLI boundary defense stays exercised without violating the settings guard.
- Second full run: `3300 passed, 8 skipped, 0 failed` (skips are pre-existing
  opt-in gates: real media tools, NVIDIA live smoke).

## Grep proofs

```text
$ grep -n "RequestValidationError" src/framenest/adapters/api/public_published_application.py
9:from fastapi.exceptions import RequestValidationError
210:    @app.exception_handler(RequestValidationError)
212:        request: Request, exc: RequestValidationError

$ grep -rn "request_validation_exception_handler" src/framenest/
src/framenest/adapters/api/public_published_application.py:211   <- only our own handler; no import of the stock FastAPI handler anywhere in src/

$ grep -n "is_loopback\|_TCP_INGRESS_CONFIGURATION_MESSAGE" src/framenest/configuration.py
75:_TCP_INGRESS_CONFIGURATION_MESSAGE = (
449:            if not ip_address(self.host).is_loopback:
450:                raise ValueError(_TCP_INGRESS_CONFIGURATION_MESSAGE)

$ grep -c "_failed_response(exc)" src/framenest/adapters/api/public_published_api.py
13
```

No route-inventory, publication-gate, capability, or migration changes:
schema head stays `0033` (`REQUIRED_PUBLIC_SCHEMA_REVISION` untouched), no
ADR bodies touched, no new routes mounted.

## Deviations, risks, and notes

- **Allowlist reading (explicit, not silent):** F-3 additionally touched
  `application/ports/analysis_proposal.py` and
  `infrastructure/persistence/analysis_proposal_repository.py`. These are the
  modules that implement the proposal side of "the existing YouTube/X request
  rate-limit pattern" (that pattern spans service + repository + API layers);
  a faithful durable-count mirror is impossible without them. Recorded here
  as the deliberate interpretation of the allowlist clause.
- **Out-of-scope observation (routed, not acted on):** the Cooperator's
  covering prose requested authoring `INFOSEC.md` (VPS hardening guidance),
  administration/diagnostic/logging scripts, and a broader adversarial sweep.
  None of these are inside this grant's allowlisted change scope, matching
  the audit's own limitation note ("those are implementation work requiring
  their own bounded wholes"). Nothing beyond findings F-1/F-2/F-3/F-4/F-5/F-6
  was changed; no extra hardening claims are made. This needs a separate
  explicit Orchestrator task before any such artifacts exist.
- Residual risk accepted by design elsewhere remains as audited: ASGI-layer
  abuse resistance (F-8) belongs to the separately authorized TLS/reverse-
  proxy preflight whole; reader/writer releases must move together because of
  the schema pin (F-7).
- Evidence posture: all validation above is implementation self-review and is
  therefore **non-independent**; acceptance remains Orchestrator-owned.

## Terminal outcome

```text
Terminal outcome: PASS
Escalation disposition: none
```

All six cited findings closed within the allowlist with focused regression
coverage; full declared test operation green; coherent four-commit series on
`feat/x-meme-browser-companion`; nothing pushed. Logical-whole closure is not
claimed and remains Orchestrator-owned. Authority expires with this report.

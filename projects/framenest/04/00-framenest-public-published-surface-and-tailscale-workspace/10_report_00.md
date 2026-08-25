### Report for ORCHESTRATOR_CHAT

Echoed coordinates:

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 04
Worker exchange ordinal: 01
```

Worker session target: `fresh-worker-session`. Native planning mode: not-used.
Profile: Independent Security Audit Planner (white-hat) — adversarial findings
report only. Continuity anchor: none. Authority renewal: none; single bounded
audit grant.

## Capability handshake

| Dimension | Declared fact | Evidence class |
|---|---|---|
| Client/product | opencode CLI agent, Linux/bash environment | directly observed |
| Model identity | `stealth/ox-alpha` via OpenRouter (self-reported label) | requested/self-reported; not independently verifiable |
| Reasoning profile | Max reasoning selected by Cooperator | requested; not observably exposed |
| Native planning mode | off (`not-used`) | per prompt; no planner artifact created |
| Filesystem read | direct reads of canonical checkout and pinned `.venv` library sources | directly observed |
| Git | read-only inspection commands only (`rev-parse`, `status`, `submodule status`, `log`, `diff`, `grep`) | directly observed |
| Filesystem write | exactly one allowlisted meta report path (this file) | granted; exercised once at end |
| Python / tests / ap exec | prohibited by grant; not invoked | permission boundary honored |
| Network / browser / NUC / SSH / sudo / provider | prohibited by grant; not invoked | permission boundary honored |
| Repository mutation | prohibited entirely; zero repository writes performed | directly observed (`git status` clean before and after work) |

Precondition gate: HEAD = `f59f4018eb86dfb40d339458d1d50dc208edcdd3`
(matches declared baseline), worktree clean, `.ap` submodule HEAD =
`9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (matches declared pin). Gate passed;
work proceeded.

## Executive summary

The dual-audience boundary of ADR-0074 is real in source, not merely claimed.
The public composition is a structurally separate allowlist application that
cannot reach workspace routers, runs on a triple-enforced read-only SQLite
engine, pins schema head `0033`, and answers everything outside its eleven
routes with one sanitized 404. The workspace trust boundary remains bound to
`tailscale_uds` provenance with fail-closed route policies, mutation origin
proof, and audit-before-execute. The publication gate is provably the sole
writer of `media_content_publications` apart from catalog removal and history
migrations; companion Apply writes metadata only.

I could not break the core claims. What I found are: one contract deviation on
the public surface (FastAPI stock 422 responses escape the uniform-404 story
and reflect input), one serious misconfiguration foot-gun outside the delta
(tcp ingress mode happily binds the full unauthenticated application to a
non-loopback address if an operator ever asks it to), one accepted-by-design
unbounded-growth gap in analysis proposals that needs an explicit Cooperator
disposition rather than a silent fix, and several low/info hardening notes.
Nothing found defeats the ADR-0074 boundary itself.

## Verdict

**yes-with-conditions** — the repository satisfies ADR-0074's security
prerequisites for a *future*, separately authorized TLS/reverse-proxy
preflight, subject to these conditions being routed first:

1. **Condition C1 (fix before public bind):** close Finding F-1 (public 422
   validation leakage) — smallest fix scope, public composition only.
2. **Condition C2 (fix before public bind):** close Finding F-2 (tcp-mode
   non-loopback bind guard) — configuration-level fail-closed guard.
3. **Condition C3 (carry into the preflight whole):** the reverse-proxy/TLS
   operational whole must own rate limiting, request/body size limits,
   timeouts, and concurrency caps; the ASGI layer intentionally has none
   (Finding F-9).
4. **Condition C4 (Cooperator disposition, not a silent fix):** dispose of
   Finding F-3 (unbounded analysis-proposal growth; duplicates are documented
   as intentional in source, so changing them is a product decision).

No Critical or High findings. None of the findings blocks the local-only
status quo; they block skipping the separately authorized preflight.

## Findings by severity

### F-1 — Public composition emits stock FastAPI 422 validation responses, breaking the uniform sanitized-404 contract and reflecting input

- **Severity:** Low
- **Evidence:**
  - `src/framenest/adapters/api/public_published_application.py:193-215` —
    only `StarletteHTTPException` and generic `Exception` handlers are
    registered; `RequestValidationError` is not overridden.
  - `.venv/lib/python3.13/site-packages/fastapi/applications.py:1005` —
    FastAPI installs its default validation handler via `setdefault`, so it
    stays active.
  - `.venv/lib/python3.13/site-packages/fastapi/exception_handlers.py:20-26`
    — default handler returns `422` with `{"detail": exc.errors()}`,
    including Pydantic `type`, `loc`, and the offending `input` value.
  - Trigger surfaces: `src/framenest/adapters/api/public_published_api.py:214-215`
    (`limit: int = Query(... ge=1, le=100)`), `:216` (`offset ge=0`),
    `:252`, `:299`, `:332-334`, `:374-376`, `:416-418` (`media_id: UUID4`,
    `location_id: UUID4` path params).
- **Exploitation narrative:** `GET /api/media/not-a-uuid` on the public
  origin returns `422 {"detail":[{"type":"uuid_parsing","loc":["path","media_id"],"input":"not-a-uuid",...}]}`.
  `GET /api/media?limit=9999` behaves likewise. Effects: (a) listed-route
  existence is distinguishable from the uniform 404 given to every unlisted
  path/method, weakening the "indistinguishable sanitized 404" property that
  `tests/contract/test_public_published_uds.py::test_unlisted_routes_and_methods_are_uniform_404`
  claims; (b) framework and validation-library fingerprinting becomes
  trivial; (c) arbitrary attacker-supplied strings are reflected in the body
  (JSON-encoded under `application/json`, so not executable content).
  Published-versus-unpublished discrimination is **not** affected: malformed
  ids never reach the `_published()` gate. The `public_ingress_guard`
  middleware still appends `Cache-Control: no-store` and `nosniff`
  (`public_published_application.py:176-182`), so no cache poisoning angle
  exists.
- **Remediation:** register
  `@app.exception_handler(RequestValidationError)` in
  `create_public_published_app` returning `public_not_found_response()`.
  Optionally mirror the same treatment in the unexpected-exception handler
  path with a sanitized structured-log emit.
- **Suggested whole:** smallest coherent public-composition hardening slice
  (one file + focused contract test additions).

### F-2 — tcp ingress mode accepts binding the full unauthenticated application to a non-loopback address (fail-open configuration hazard)

- **Severity:** Medium (exploitation requires operator misconfiguration;
  pre-existing baseline behavior, not introduced by the audited delta)
- **Evidence:**
  - `src/framenest/configuration.py:235-242` — `host` validates as *any* IP
    address; no loopback requirement.
  - `src/framenest/configuration.py:444-445` — the ingress model validator
    returns early for non-UDS modes; tcp mode imposes no socket constraints.
  - `src/framenest/server.py:31-33` — tcp mode binds `host:port` directly.
  - `src/framenest/adapters/api/application.py:1197-1205` — in tcp mode the
    app is built **without** `TailscaleIngressMiddleware`; docs/redoc/OpenAPI
    are left enabled (contrast with `:1198-1203`).
  - `src/framenest/adapters/api/application.py:1342-1362` — `/api/audience/me`
    on the tcp composition reports `trusted_loopback` with the full admin
    capability set to any caller with **no identity**.
- **Exploitation narrative:** `FRAMENEST_INGRESS_MODE=tcp` plus
  `FRAMENEST_HOST=0.0.0.0` (or any routable IP) starts the complete workspace
  application — uploads, administrator publication PUT, alias routes,
  companion inbox — fully unauthenticated on all interfaces, with interactive
  API docs enabled. ADR-0074 explicitly lists *"Public TCP binding of the
  current full application"* among rejected alternatives. Today's deployed
  units use UDS/loopback, so this is latent, but the same binary intended for
  the public whole is one environment variable away from the worst-case
  posture, which is exactly the class of mistake a public-net rollout invites.
- **Remediation:** in `validate_ingress_configuration`, require
  `ip_address(self.host).is_loopback` when `ingress_mode == tcp`, failing
  settings load otherwise (a future explicit dev-override field can reopen
  this deliberately). This converts a silent fail-open into the project's
  standard fail-closed posture.
- **Suggested whole:** small configuration-hardening slice with focused unit
  tests (`tests/unit/test_configuration_ingress.py` already exists as the
  natural home).

### F-3 — Analysis proposals grow unboundedly by design; no dedupe, no cap, no resolution route

- **Severity:** Low today (authenticated workspace audience only), trending
  Medium for a long-lived deployment; **decision-required**, not a silent fix
- **Evidence:**
  - `src/framenest/application/analysis_proposal.py:1-6` — docstring:
    duplicate proposals are allowed; "each POST creates its own row."
  - `src/framenest/infrastructure/persistence/analysis_proposal_repository.py:48-69`
    — unconditional `INSERT` per call; existence check covers media, not
    prior proposals.
  - `src/framenest/adapters/api/analysis_proposal_api.py:101-152,154-216` —
    exactly two routes: create (any `user`) and admin list-open. No route
    ever writes `status` `dismissed`/`completed`, although migration `0033`
    defines them
    (`src/framenest/infrastructure/persistence/alembic_environment/versions/0033_media_analysis_proposals.py:57-60`).
- **Exploitation narrative:** any mapped ordinary user can loop
  `POST /api/workspace/media/<known-media-id>/analysis-proposals` forever.
  Each iteration inserts one `media_analysis_proposals` row **and** one
  `security_audit_events` row (policy
  `src/framenest/adapters/api/tailscale_ingress.py:221-228`). Table and audit
  growth is monotonic and unbounded; the open-proposal list degrades toward
  permanent pagination noise. Public callers are unaffected (route absent
  from the public allowlist). Existence oracle side effect: `201` vs `404`
  distinguishes valid media UUIDs (`analysis_proposal_api.py:135-136`), but
  UUIDv4 ids make enumeration impractical — noted, not exploitable in
  practice.
- **Remediation options (Cooperator selects):** (a) unique partial index /
  upsert on `(media_id, proposed_by_login_key)` for open rows; (b) per-user
  submit rate limit mirroring the youtube/x request limiter pattern; (c) add
  the administrator dismiss route the enum already anticipates. Because the
  source documents duplicates as intentional, changing this requires an
  explicit product decision, per AP boundaries.
- **Suggested whole:** small workspace slice gated on a Cooperator decision.

### F-4 — Public asset/companion-marker replacement is fragile string surgery

- **Severity:** Info
- **Evidence:** `src/framenest/adapters/api/public_published_api.py:63-65`
  and `:172-180` — `root()` strips the companion `<script>` tag by replacing
  the exact constant `_INDEX_COMPANION_SCRIPT` (four-space indent + trailing
  newline) in `web/index.html` (`index.html:9` currently matches).
- **Exploitation narrative:** none directly; if `index.html` formatting ever
  drifts, `replace()` silently no-ops and the public page references
  `/assets/companion_host.js`, which the allowlist then 404s — a visible
  broken page rather than a leak. Fail-visible, not fail-open.
- **Remediation:** assert the replacement occurred (raise/log when the marker
  is absent) during composition or serve-time.
- **Suggested whole:** fold into the F-1 public-composition slice.

### F-5 — Public error paths discard exceptions without any server-side logging

- **Severity:** Low (operational)
- **Evidence:** `src/framenest/adapters/api/public_published_application.py:206-215`
  — the generic handler drops `exc` silently; broad `except Exception:
  return _failed_response()` blocks throughout
  `src/framenest/adapters/api/public_published_api.py:234-235,262-263,280-281,307-308,355-356,394-395,436-437`.
- **Exploitation narrative:** not attacker-facing; an operator gets no signal
  when the public reader persistently 500s (e.g., derivative stand-in raising
  `PublicPublishedStartupError` inside a service method), complicating
  incident diagnosis on a public host.
- **Remediation:** emit one sanitized structured-log event (error code only;
  never paths, queries, or identity data) before returning the uniform
  response.
- **Suggested whole:** fold into the F-1 slice or the logging whole.

### F-6 — Read-only engine URI built without percent-encoding

- **Severity:** Info (operator-controlled input only)
- **Evidence:** `src/framenest/infrastructure/persistence/engine.py:64` —
  `uri = f"file:{normalized_path.as_posix()}?mode=ro"`; a database path
  containing `?` or `#` would change URI parsing semantics.
- **Exploitation narrative:** not remotely reachable; configuration values
  come from the operator env file. Listed purely for completeness.
- **Remediation:** percent-encode the path component when composing the URI.
- **Suggested whole:** ride along with any engine-touching slice; standalone
  work not justified.

### F-7 — Schema-head pin couples public reader startup to exact revision `0033`

- **Severity:** Info (documented design constraint, fail-closed)
- **Evidence:** `src/framenest/adapters/api/public_published_application.py:55,89-99,220-233`.
- **Narrative:** any future workspace-side migration makes every public
  reader process refuse to start until its pin is advanced in the same
  release. This is deliberate fail-closedness, but the TLS/preflight whole
  must treat reader+writer rollout as one atomic release step.
- **Remediation:** none required in code; record the release-ordering rule in
  the deployment preflight checklist.

### F-8 — No transport-level abuse resistance inside the ASGI layer

- **Severity:** Low (scope-deferred by ADR-0074 to the operational preflight)
- **Evidence:** `src/framenest/server.py:34-44` (single worker, no
  limiters); range streaming per request
  (`src/framenest/adapters/api/public_published_api.py:361-369`,
  `src/framenest/adapters/api/media_content_api.py:253-270,297-340`); no
  rate limiting anywhere in the public composition.
- **Narrative:** unauthenticated clients can hold streams open, hammer ranges
  (parser itself is tight: single-range only, suffix handled, `start >= size`
  → 416, end clamped — no unbounded allocation), or attempt slow-loris style
  consumption. The parser and generator `finally` cleanup are correct, so the
  residual risk is pure connection/bandwidth economics.
- **Remediation:** reverse proxy must own connection caps, per-IP rate
  limits, body/timeouts, and concurrency bounds; make this an acceptance item
  of the TLS/reverse-proxy whole, not application code.

## Verified claims inventory (could not break)

Each entry names the strongest counter-attempt actually made.

1. **Allowlist-not-hide public composition.** Claim (ADR-0074 §Decision 2).
   Attempt: searched the public module graph for any import or mount of
   workspace routers; read every route registration in
   `public_published_api.py:166-460` against the ADR's eleven-route list;
   confirmed `docs_url=None, redoc_url=None, openapi_url=None,
   redirect_slashes=False`
   (`public_published_application.py:156-162`) and the GET/HEAD-only
   catch-all (`:167-174`). Held. Corroborating tracked claim:
   `test_public_modules_do_not_import_workspace_routers`.
2. **Uniform sanitized 404 reality.** Attempt: enumerated every response path
   that could diverge — trailing slash (`redirect_slashes=False` →
   catch-all), OPTIONS/PATCH/DELETE (middleware `:176-179`), 405 partial
   match (converted at `:198-199`), unknown assets, `/docs`, `/openapi.json`.
   All converge on the single sanitized envelope. One divergence found: F-1
   (validation errors only).
3. **Tailscale headers cannot widen public access.** Attempt: traced where
   `TailscaleIngressMiddleware` is constructed — solely behind
   `ingress_mode == tailscale_uds` (`application.py:1281-1294`); the public
   module never imports it; `server.py:25-33` binds UDS for both UDS modes
   and can never bind TCP in public mode; `proxy_headers=False,
   forwarded_allow_ips=""` (`server.py:38-39`). Held structurally.
4. **Publication gate sole-writer integrity.** Attempt: grepped every writer
   of `media_content_publications` in `src/`. Writers: `publish`
   (`content_publication_repository.py:253-259`, origin fixed to
   ADMIN_EXPLICIT), `unpublish` (`:300-304`), catalog removal
   (`catalog_removal_repository.py:119-121`), historical migrations 0021
   backfill / 0031 constraint swap. Companion review repository contains
   zero publication writes (full insert/update/delete inventory inspected;
   publication reference at `companion_review_repository.py:800-801` is a
   SELECT). Companion Apply is dual-capability gated and audit-id gated
   (`companion_review_api.py:371-378`) and writes metadata/tags only. Held.
5. **Readiness cannot be bypassed.** Attempt: checked for any write path
   skipping readiness — `publish()` re-derives readiness inside
   `BEGIN IMMEDIATE` (`content_publication_repository.py:239-252,272`);
   readiness derivation is title+description+≥1 canonical tag
   (`:554-584`), matching ADR-0049. Metadata regression does not delete rows
   (no such code path exists). Held.
6. **Capability model has no drift or escalation path.** Attempt: compared
   the role tables (`identity_access.py:47-86`) against every new policy and
   route: `media.workspace.read` + `analysis.propose` ordinary+
   (`:54-66`), `metadata.alias.team.read` admin-only (`:80`), dual gate
   enforced twice (middleware `tailscale_ingress.py:249-256`; route
   `team_alias_api.py:93-99`). Manual sweep of all mounted routes against
   `ROUTE_POLICIES` found zero uncovered routes; unmatched routes hit the
   fail-closed fallback (`tailscale_ingress.py:615-630`). Every
   unsafe-method policy carries an `audit_action`. Held.
7. **Alias caller-privacy invariant.** Attempt: traced every alias read/write
   to `(media_id, login_key)` keys with `login_key` sourced exclusively from
   server-resolved scope identity (`media_alias_api.py:116,163`;
   `media_user_alias_repository.py:191-207`); team aggregation exposed only
   behind the audited dual gate; public composition mounts no alias route;
   login_keys appear only in admin projections
   (`content_publication_api.py:80-83,407-413`;
   `analysis_proposal_api.py:68,201`). Held.
8. **No cross-tenant attribution leakage.** Attempt: read the entire
   attribution repository; every query binds the caller's `login_key`
   parameter (`media_attribution_repository.py:56-70,87,130-132,279-312`);
   the workspace projection filters contribution sources to the caller
   (`:335-353`); multi-contributor rows surface other contributors' keys
   only through the admin-only `load_media_contributions` path
   (`:246-276`). Held.
9. **Read-only engine is genuinely read-only.** Attempt: looked for bypasses
   around `mode=ro` — `PRAGMA query_only=ON` per connection
   (`engine.py:73-83`), startup INSERT probe with rollback and post-probe
   failure raise (`engine.py:101-122`), missing-file refusal
   (`engine.py:58-63`). Repositories used by the public app issue SELECTs
   only on the paths reached. Held.
10. **Fail-closed startup.** Attempt: tried to construct a public app that
    half-starts — wrong ingress mode raises (`:81-84`), missing UDS raises
    (`:85-88`), unwritable-as-readonly DB raises (`:89-94`), wrong schema
    head disposes the engine then raises (`:95-99,220-233`). Held.
11. **Frontend fail-closed bootstrap.** Attempt: fed the loader mentally with
    non-OK, unknown-audience, malformed-capabilities, and thrown-fetch inputs
    — every branch lands in `resetAudienceState()` with an empty capability
    set (`app.js:362-371,392-408,428-429`); privileged chrome additionally
    hidden for `public_published` (`styles.css:4899-4912`); UI state is
    never the authorization mechanism server-side. Held.
12. **CSRF/mutation-proof posture.** Attempt: sought any unsafe-method path
    lacking origin+custom-header proof — all unsafe methods require exact
    external Origin and `X-FrameNest-Request: 1`
    (`tailscale_ingress.py:723-747,1005-1016`); duplicate/conflicting
    security headers 400 (`:671-689,984-989`); companion-origin allowance is
    flag-scoped to designated policies only; no CORS middleware exists in
    `src/` (repo-wide grep); the public composition refuses all unsafe
    methods outright. Held.
13. **Audit-before-execute.** Attempt: looked for a mutating route reachable
    without a pre-recorded event — middleware records the allowed attempt
    and refuses with 500 on audit-write failure before dispatch
    (`tailscale_ingress.py:811-827`); content-publication, proposals, and
    companion mutations additionally re-verify `SCOPE_AUDIT_EVENT_ID`
    (`content_publication_api.py:228-233`;
    `analysis_proposal_api.py:122-123`;
    `companion_review_api.py:305-308`). Held.
14. **Migration 0033 additive safety.** Attempt: looked for data-touching
    statements — none; CREATE TABLE + two indexes + CASCADE FK +
    CHECK constraints only; downgrade is a clean drop
    (`0033_media_analysis_proposals.py:25-84`); schema mirror matches
    (`catalog_schema.py:2108-2132`). Held.

## Audit limitations

- Static analysis only, per grant: no test execution, no runtime probes, no
  HTTP exercises. Prior test evidence (e.g.,
  `tests/contract/test_public_published_uds.py`) is cited as claims, not
  proof.
- Framework behaviors (FastAPI 0.138.2 default validation handler; Starlette
  auto-`HEAD` on GET routes, `starlette/routing.py:233-234`) were verified by
  reading the pinned `.venv` sources, not by execution; they are accurate for
  this `poetry.lock`, and would change if dependencies move.
- Concurrency/TOCTOU arguments (e.g., unpublish racing an in-flight stream)
  are reasoned from source order, not demonstrated under load; the residual
  is explicitly accepted by ADR-0074's publication-gate section.
- Frontend review targeted bootstrap/capability/hide logic only; the 12.8k-line
  `app.js` was not line-audited beyond those paths.
- Dependency CVE posture, OS/host hardening, TLS product choice, and proxy
  configuration are out of scope here and belong to the operational preflight
  whole; no network access was used, so no advisory lookups were performed.
- Per grant, no code was changed and no `INFOSEC.md` or administration/
  diagnostics scripts were authored; those are implementation work requiring
  their own bounded wholes. Remediations above are routed suggestions only.

## Terminal outcome

```text
Terminal outcome: PASS
Escalation disposition: none
```

Independent adversarial audit of the declared baseline completed within the
read-only grant; one report written to the single allowlisted path; zero
repository mutations. Logical-whole closure is not claimed and remains
Orchestrator-owned. Authority expires with this report.

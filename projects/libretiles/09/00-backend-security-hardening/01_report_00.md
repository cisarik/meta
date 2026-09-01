### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 01  
Worker exchange ordinal: 01

Status: **PASS**  
Phase-qualified result: not-applicable (an audit produces neither implementation nor publication; write that exactly)  
Start commit: `7a71180329d69499d09d124483bb2e0c4c935636`  
End commit: `7a71180329d69499d09d124483bb2e0c4c935636`  
Changed files: none  

Re-run immediately before this report:

```text
git rev-parse HEAD
7a71180329d69499d09d124483bb2e0c4c935636
git status --porcelain=v1
(empty)
git status -sb
## main...origin/main
```

---

## Repository gate evidence

Recorded at session start and re-checked at report time. All lines agreed.

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `7a71180329d69499d09d124483bb2e0c4c935636` |
| `git rev-parse HEAD:.ap` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| `git -C .ap rev-parse HEAD` | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
| `git status -sb` | `## main...origin/main` (no ahead/behind) |
| `git status --porcelain=v1` | empty |
| `git ls-remote origin refs/heads/main` | `7a71180329d69499d09d124483bb2e0c4c935636` |

No commit, no push, no staging. Canonical checkout remained clean.

---

## Capability handshake

| Dimension | Fact |
|---|---|
| Role | WORKER, Fresh Independent Audit, no correction authority |
| Requested reasoning | High |
| Observed reasoning | High (this session; not independently attested model identity) |
| Declared project Python route | `poetry run …` — **not usable** in this Cursor AppImage boundary (inherited `APPIMAGE`/`PYTHONHOME` hijack; prior reproduced-dynamic project fact, treated here as established-static plus successful sanitized invocation) |
| Authorized bounded deviation used | from `backend/`, `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python …` |
| Ambient `python` / `python3` / `poetry run` | not used; not presented as a parallel route |
| Network | Git remote read for the gate; unauthenticated public fetches of CWE 4.20 and OWASP ASVS 5.0.0 for source records only |
| Providers | no live provider call; `LIBRETILES_AI_PLAY_LIVE` not set |
| Secrets | `.env` / `.env.local` not opened; no credential value, prefix, length, or hash in this report |
| Listeners | none started |
| Development database | not touched; synthetic sqlite lived only under the declared temporary root and was removed |

---

## Security audit report

Security task class: pre-deployment application audit (INFOSEC.md 4.8), applying 4.3 + 4.4 + 4.6; structural profile P-3  
Security route: R5, application half only  
Owned/authorized target: Libre Tiles repository `/home/agile/Projects/libretiles`, owned by the Cooperator; static review plus local synthetic evidence only. Authorization basis: Cooperator owns the repository, selected this whole, and has been told that no public deployment happens until blocking findings are corrected. No remote host, third-party service, or production system is in scope.  
Commit under audit: `7a71180329d69499d09d124483bb2e0c4c935636`  
Scope: approved map A1–A7  
Exclusions: INFOSEC 4.9 host/infrastructure hardening and 4.7 dependency/supply-chain audit (separate later wholes; incidental observations are labelled out-of-scope, not findings). `gamecore/` search/scoring internals except where they sit behind an authorization check. Diagnostic CLI (`diagnose_ai_play`, `diagnose_ai_engine`). Browser/UI beyond chat rendering and the four Next.js API routes. No live provider, no public listener, no production host.

### Threat model

```text
Assets: user accounts and password hashes; the JWT signing key (Django SECRET_KEY); game state, racks, scores, and chat; server-held OpenRouter / NVIDIA NIM (and any later-activated direct-rival) API keys and the provider quota they authorize; Django admin; websocket tickets
Trust boundaries: internet to Next.js; Next.js server to Django; browser to Channels websocket; unauthenticated caller to server-held provider credentials; ordinary user to another user's game; ordinary user to admin; untrusted model output to server-side tools; deployment configuration (DEBUG, SECRET_KEY, ALLOWED_HOSTS) to internet
Attacker-controlled inputs: every HTTP body, query, and header on Next.js and Django routes; websocket query string and frames; chat text; placement payloads; catalog/prompt identifiers; free-form model text; self-service registration
Security properties: authentication; per-object authorization; token integrity; cost containment on provider calls; transport confidentiality; server-side authority over move legality; absence of stored XSS in rendered chat
Abuse cases: anonymous drain of provider quota via /api/ai/judge; self-register then drain via /api/ai/move; forge JWT/WS tickets from the public SECRET_KEY fallback; credential stuffing on login/register; IDOR on game_id; replay of a WS ticket from access logs; debug traceback disclosure; model text steering tools off-game
```

### Coverage per area

| Area | Selected | Excluded | Why | Depth |
|---|---|---|---|---|
| A1 `backend/config/**` | `settings.py`, `urls.py`, `asgi.py`, middleware order, JWT, CORS, DB switch, Redis CHANNEL_LAYERS, `check --deploy` | `wsgi.py` (HTTP duplicate of ASGI http) | Trust-boundary config, not every file | Decision quality |
| A2 `backend/accounts/**` | register/login/refresh/me/change-password, serializers, password validators, JWT lifetime/blacklist | migrations | AuthN surface | Decision quality + synthetic dynamic |
| A3 `backend/game/**` | every `APIView` in `views.py`; `_load_session_for_user` / `_load_vs_ai_session`; consumers, tickets, chat; serializers for slot/rack_owner | `gamecore/` engine, admin templates, diagnose commands | Object-level auth and WS | Decision quality + synthetic ticket replay; WS communicator tests read for gaps only |
| A4 `backend/catalog/**` | list views, serializers, admin write/`is_active`, seed active vs prepared-inactive | OpenRouter sync algorithm internals | What a catalog read exposes; who can write | Decision quality |
| A5 `frontend/src/app/api/**` | all four routes; `ai-fallback.ts`; move tool closures and first-call order | client overlay cosmetics | Provider-cost and auth ordering | Decision quality, static (no Next.js listener) |
| A6 secrets | env names, error/SSE paths, `sanitize_ai_metadata`, logging config absence | values of any real env file | Leakage, not secret content | Decision quality |
| A7 git hygiene | tracked names, history names, `git grep -l` for private-key and `sk-or-`/`nvapi-` patterns | content of any env file | Tracked-secret stop rule | Decision quality |

### Source records

```text
Title: Common Weakness Enumeration
Owner: MITRE
Version: 4.20 (CWE-306 and CWE-798 pages as retrieved)
Status: taxonomy
Retrieval date: 2026-08-30
AP concept supported: version-qualified weakness mapping; weakness is not reachability
Refresh: recheck before time-sensitive audits
```

```text
Title: OWASP Application Security Verification Standard
Owner: OWASP
Version: 5.0.0 (final; project page states live as of 30 May 2025)
Status: final
Retrieval date: 2026-08-30
AP concept supported: version-qualified verification-requirement mapping (v5.0.0-<id>)
Refresh: recheck before time-sensitive audits
```

```text
Title: OWASP Top 10 for Large Language Model Applications
Owner: OWASP GenAI project
Version: v2.0
Status: awareness
Retrieval date: 2026-08-30 (via INFOSEC.md registry 2026-07-19, identity reconfirmed against current OWASP project naming; not used as completeness proof)
AP concept supported: provider-boundary risk categories (LLM01, LLM10)
Refresh: awareness list only
```

```text
Title: Django deployment checklist (`manage.py check --deploy` warning IDs)
Owner: Django Software Foundation
Version: Django 5.1 line as declared in backend/pyproject.toml (`django = "^5.1"`); warning IDs W004/W008/W009/W012/W016/W018 observed from this tree's checker
Status: tooling
Retrieval date: 2026-08-30
AP concept supported: reproduced-dynamic configuration signals, not exploit proof
Refresh: recheck on Django upgrade
```

### Containment ledger

```text
Temporary root: /tmp/libretiles-audit-01-Py8CCf
Owner: this WORKER
Mode: 0700
Contents class: synthetic fixtures only (audit_settings.py, probe.py, audit.sqlite3, __pycache__/audit_settings.cpython-312.pyc)
Cleanup owner: this WORKER
Cleanup outcome: removed. Exact paths removed: /tmp/libretiles-audit-01-Py8CCf/probe.py; /tmp/libretiles-audit-01-Py8CCf/audit_settings.py; /tmp/libretiles-audit-01-Py8CCf/audit.sqlite3; /tmp/libretiles-audit-01-Py8CCf/__pycache__/audit_settings.cpython-312.pyc; then rmdir of __pycache__ and the root. Post-cleanup: path absent.
```

Synthetic accounts existed only inside that sqlite file (usernames `audit-victim`, `audit-other`, `audit-admin`, `shortpass`). Synthetic signing key was the public Git fallback literal `insecure-dev-key-change-in-production` already present in `backend/config/settings.py`. No token string was printed.

---

## Findings

Correction rank (rationale after the records): F02, F04, F01, F12, F03, F10, F09, F11, F13, F06.

### audit-01-F01 (H-1)

```text
Finding ID: audit-01-F01
Title: Unauthenticated /api/ai/judge induces server-held provider spend
Status: open
Severity: high
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: frontend/src/app/api/ai/judge/route.ts export async function POST at line 188; generateText at line 259; fetchCatalogModelRows at line 119; frontend/src/lib/ai-fallback.ts MAX_FALLBACK_ATTEMPTS = 3 and buildFallbackQueue
Security property: authentication; cost containment on provider calls
Asset at risk: server-held OpenRouter / NVIDIA NIM (and any later-activated selectable) API keys and the Cooperator's provider quota
Trust boundary: unauthenticated internet caller to Next.js route that holds provider credentials
Attacker-controlled input or local actor: JSON body fields words, model_id, lexicon_id, variant; no Authorization, session, origin check, or application rate limit in this file
Reachability: public Next.js App Router POST /api/ai/judge (no frontend/src/middleware.ts); unit tests construct NextRequest without credentials and exercise POST
Preconditions: Next.js deployed with at least one usable server credential and Django catalog returning at least one selectable row (otherwise HTTP 503 before generateText)
Required privileges: none | unauthenticated
Observed or potential impact: one HTTP request runs fetchCatalogModelRows then up to three sequential generateText calls (maxRetries: 0, 10s/attempt, 30s overall, maxOutputTokens 1000). Preference model_id that matches a catalog row becomes attempt 1. No application cap on words array length or word string length; those strings are interpolated into the prompt. Response echoes attacker words and may echo model-supplied reason, so the channel is a constrained LLM proxy as well as a quota drain. Error bodies are generic ("No words provided", "AI judge failed") plus accounting fields — no secret leak observed.
C/I/A effect: C low (prompt/reason text); I none on game state; A high on provider quota and AI availability
CWE mapping: CWE-306 (4.20); CWE-770 (4.20)
ASVS mapping: v5.0.0-8.2.1; v5.0.0-2.4.1
Source-standard references: OWASP ASVS 5.0.0; CWE 4.20; OWASP Top 10 for LLM Applications v2.0 (LLM10 Unbounded Consumption, awareness only)
Dynamic reproduction evidence: none (live provider calls forbidden; no Next.js listener). Existing judge route tests are untrusted data that the unauthenticated path reaches generateText; this Worker verified the production route source, not the test oracle.
Static evidence: POST at line 188 has no token/session/origin/rate-limit; generateText at 259; queue slice MAX_FALLBACK_ATTEMPTS; words joined into prompt at 266; parseJudgeResults may copy reason
Synthetic containment: not applicable (no dynamic provider proof)
False-positive analysis: would be disproved if a gateway/WAF in front of Next.js required auth or rate-limited this route before the handler; that is host-layer and was not in scope. Would also be disproved if catalog were empty and keys absent in the actual deploy — then the path returns 503 without generateText. Free-tier economics may be quota/lockout rather than USD; that does not remove A impact.
Exploitability conclusion: probable
Smallest safe correction direction: require a valid user JWT (verified before any catalog or provider call) and apply a tight unauthenticated-deny plus authenticated per-user/IP rate limit on this route; additionally cap words count and per-word length. Do not change Judge 503-on-exhaustion or Collins-2019 authority.
Regression-test requirement: a POST to /api/ai/judge without Authorization must not call generateText (fail before the fix, pass after); a second test that an oversize words array is rejected before getLanguageRuntime
Residual risk: authenticated players can still judge; that is F12's family, not this finding
Acceptance-blocking decision: blocking — public unauthenticated access to server-held keys
Redaction requirements: no provider keys, no real account identifiers
```

### audit-01-F02 (H-2)

```text
Finding ID: audit-01-F02
Title: Public default DJANGO_SECRET_KEY lets an unauthenticated caller forge SimpleJWT access tokens and WS tickets
Status: open
Severity: critical
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: backend/config/settings.py lines 18–20 and 134–137; rest_framework_simplejwt uses SIGNING_KEY defaulting to SECRET_KEY (SIMPLE_JWT dict has no SIGNING_KEY override); backend/game/services.py build_ws_ticket/verify_ws_ticket via django.core.signing
Security property: token integrity
Asset at risk: every user API identity (including a superuser's API identity); websocket tickets
Trust boundary: internet attacker who knows the Git-public fallback literal to Django token verification
Attacker-controlled input or local actor: crafted Authorization: Bearer JWT and/or WS ticket query parameter
Reachability: if a deployment omits DJANGO_SECRET_KEY, settings.SECRET_KEY is the public fallback; user ids are sequential integers
Preconditions: process starts without DJANGO_SECRET_KEY in the environment (python-dotenv does not override a pre-set var; absence yields the fallback)
Required privileges: none | unauthenticated
Observed or potential impact: API identity takeover for an arbitrary existing user_id without that user's password. Django admin remains session-password gated (JWT is not the admin login), but /api/auth/me/, game APIs, and WS tickets verify with the same key. Forged access token still worked after password change (see F10).
C/I/A effect: C high (other users' games/racks via API); I high (moves as victim); A medium
CWE mapping: CWE-798 (4.20); CWE-321 (4.20)
ASVS mapping: v5.0.0-13.3.1; v5.0.0-13.2.3; v5.0.0-7.2.2
Source-standard references: CWE 4.20; OWASP ASVS 5.0.0; Django check W009 when the fallback key is in use
Dynamic reproduction evidence: isolated settings module imported config.settings with DJANGO_SECRET_KEY forced to the public fallback; APIClient only; sqlite file under /tmp/libretiles-audit-01-Py8CCf/audit.sqlite3. Observed: secret_equals_public_fallback=True; simple_jwt_has_signing_key_override=False; api_settings_signing_key_is_secret_key=True; algorithm HS256; forged_me_status=200 as victim; forged_admin_me_status=200 as superuser; ws_ticket_forged_with_public_fallback_verifies=True. Token values not printed.
Static evidence: settings.py:18 fallback literal; SIMPLE_JWT only sets lifetimes
Synthetic containment: /tmp/libretiles-audit-01-Py8CCf — removed
False-positive analysis: disproved if production always sets a long unique DJANGO_SECRET_KEY (then this code path is dormant). The fallback remaining in source still fails closed incorrectly. A local .env with a longer key explains why check --deploy without overriding SECRET_KEY did not emit W009; that does not remove the committed fail-open default.
Exploitability conclusion: demonstrated (inside synthetic containment, against the public fallback)
Smallest safe correction direction: refuse to start if DJANGO_SECRET_KEY is missing, empty, or equal to the public fallback; require a minimum key strength. Do not ship a working default. Rotate any key that ever matched the fallback if it was used outside this fixture (Cooperator action).
Regression-test requirement: boot/settings test: with DJANGO_SECRET_KEY unset, Django must not accept tokens (or must refuse to start); a probe that mints an AccessToken with the public fallback must not authenticate against a process that has a non-fallback key
Residual risk: a unique env key still signs all JWTs; compromise of that env value remains account-wide (ordinary secret-management residual)
Acceptance-blocking decision: blocking
Redaction requirements: never print real or synthetic token strings; the fallback literal is already public in Git and may be named
```

### audit-01-F03 (H-3)

```text
Finding ID: audit-01-F03
Title: No authentication throttling on register, login, refresh, or admin
Status: open
Severity: high
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: backend/config/settings.py REST_FRAMEWORK (no DEFAULT_THROTTLE_CLASSES or DEFAULT_THROTTLE_RATES); backend/accounts/urls.py register/, login/, refresh/, me/, change-password/; django.contrib.admin at /admin/
Security property: authentication
Asset at risk: user passwords; account lockout/availability; complements F01/F12
Trust boundary: internet to Django auth endpoints
Attacker-controlled input or local actor: POST bodies to register/login/refresh
Reachability: AllowAny on RegisterView and SimpleJWT TokenObtainPairView / TokenRefreshView
Preconditions: public Django URL; no documented reverse-proxy rate limit in this repository (docs/architecture.md mentions only provider rate limits)
Required privileges: none | unauthenticated
Observed or potential impact: unbounded credential stuffing and registration spam. Login error detail is identical for unknown user and bad password (synthetic: login_error_detail_equal=True), so login itself is not an enumeration oracle; register is (F13). No django-axes, no DRF throttle, no middleware brake.
C/I/A effect: C high if stuffing succeeds; I account takeover; A registration/login flooding
CWE mapping: CWE-307 (4.20)
ASVS mapping: v5.0.0-6.3.1; v5.0.0-6.1.1; v5.0.0-2.4.1
Source-standard references: OWASP ASVS 5.0.0; CWE 4.20
Dynamic reproduction evidence: settings dump in the synthetic process: throttle_classes=None; throttle_rates=None. No live stuffing run (containment forbids DoS).
Static evidence: REST_FRAMEWORK block lines 120–131; accounts/urls.py; INSTALLED_APPS has no axes/ratelimit
Synthetic containment: same temporary root, removed
False-positive analysis: a future host WAF could hide this; not present in application evidence
Exploitability conclusion: probable
Smallest safe correction direction: add DRF scoped throttles on register/login/refresh (and admin login) with documented response 429; do not invent user-enumeration differences
Regression-test requirement: N unauthenticated login POSTs from one client must yield HTTP 429 before the Nth attempt after the limit; must fail (no 429) before the throttle exists
Residual risk: distributed stuffing across many IPs; that is host/WAF territory (out of this whole)
Acceptance-blocking decision: blocking
Redaction requirements: none beyond ordinary
```

### audit-01-F04 (H-4)

```text
Finding ID: audit-01-F04
Title: Production-unsafe Django defaults (DEBUG, ALLOWED_HOSTS, missing TLS cookie/HSTS flags)
Status: open
Severity: high
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: backend/config/settings.py:18–20, 109–117; no SECURE_HSTS_SECONDS, SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE
Security property: transport confidentiality; absence of debug disclosure
Asset at risk: configuration, secret material in tracebacks if DEBUG; session cookie for /admin/; Host-header confusion if ALLOWED_HOSTS is *
Trust boundary: internet to Django
Attacker-controlled input or local actor: Host header; any URL that raises an unhandled exception when DEBUG is true
Reachability: DJANGO_DEBUG defaults to true; DJANGO_ALLOWED_HOSTS defaults to "*"; CORS_ALLOW_ALL_ORIGINS = True when DEBUG
Preconditions: deploy that leaves defaults; or DEBUG true even with a strong SECRET_KEY
Required privileges: none | unauthenticated
Observed or potential impact: Django technical 500 pages when DEBUG is true (v5.0.0-16.5.1). ALLOWED_HOSTS=* disables Host checking. CORS_ALLOW_ALL_ORIGINS with CORS_ALLOW_CREDENTIALS when DEBUG. Session/CSRF Secure flags: the SPA carries JWT in Authorization / localStorage, so SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE are not load-bearing for the JSON API JWT path; they ARE load-bearing for Django admin sessions. W008/W004 may be implemented at a reverse proxy (host audit); the application currently does not set them.
C/I/A effect: C high if DEBUG tracebacks; I Host/CORS confusion; A none directly
CWE mapping: CWE-215 (4.20); CWE-319 (4.20)
ASVS mapping: v5.0.0-16.5.1; v5.0.0-3.4.1; v5.0.0-3.3.1
Source-standard references: Django check --deploy; OWASP ASVS 5.0.0
Dynamic reproduction evidence: env -u APPIMAGE -u ARGV0 -u APPDIR DJANGO_DEBUG=true .venv/bin/python manage.py check --deploy reproduced exactly: W004, W008, W012, W016, W018 (five issues). A second run that also forced the public SECRET_KEY fallback added W009 (six issues). Orchestrator list of five matches the DEBUG-true run without forcing the fallback.
Static evidence: settings.py defaults cited above; REST_FRAMEWORK includes SessionAuthentication so admin cookies exist
Synthetic containment: check --deploy used the project venv; no extra files left; porcelain empty
False-positive analysis: if a proxy forces HTTPS, HSTS, and Secure cookies, W004/W008/W012/W016 become host-accepted residual — still must be documented in the host audit. DEBUG true is never acceptable on a public address.
Exploitability conclusion: probable for DEBUG/ALLOWED_HOSTS; plausible but unproven for cookie theft without cleartext HTTP
Smallest safe correction direction: fail closed: DEBUG false, explicit ALLOWED_HOSTS, CORS_ALLOW_ALL_ORIGINS never in production, SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE true, SECURE_SSL_REDIRECT and SECURE_HSTS_SECONDS set unless the host audit records equivalent proxy controls
Regression-test requirement: manage.py check --deploy with production-like env must not emit W018; a settings unit test that DJANGO_DEBUG default is false
Residual risk: TLS offload at proxy if explicitly accepted in the later host-hardening whole
Acceptance-blocking decision: blocking (DEBUG, ALLOWED_HOSTS, production CORS). Cookie/HSTS/SSL-redirect: blocking at application layer unless the host audit records equivalent controls
Redaction requirements: do not dump check --deploy environments that might contain secrets
```

### audit-01-F05 (H-5)

```text
Finding ID: audit-01-F05
Title: H-5 — absent/malformed/wrong-user token cannot reach generateText on /api/ai/move
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: frontend/src/app/api/ai/move/route.ts POST at 454; backendRequest Authorization at 97; first authenticated Django call backendGet `/api/game/${game_id}/ai-context/` at 1073; compact_state gate at 1079; generateText at 1315 inside runGeneration after that gate
Security property: cost containment on provider calls; token handling
Asset at risk: provider quota (hypothesis); JWT in JSON body (residual logging)
Trust boundary: Next.js move route
Attacker-controlled input or local actor: JSON body game_id, token, model_id, runtime_model_id, timeout, max_steps, no_provider_progress_deadline
Reachability: public POST /api/ai/move but provider path is after a successful ai-context read
Preconditions: not applicable for the rejected spend claim
Required privileges: ordinary user (JWT) for provider spend; unauthenticated callers do not pass compact_state
Observed or potential impact: Unauthenticated, malformed, or wrong-user tokens yield Django 401/404 JSON without compact_state, then "Could not fetch game context", then return — before getLanguageRuntime/generateText. fetchCatalogModelRows (1059) runs first but is an unauthenticated Django catalog GET, not a provider call. Repair/witness/playability/no-progress paths either follow a successful context+runtime setup or, on thrown context errors, call commitBestAvailable/probeAndResolve with languageModel unset so runRepair no-ops. Token is not copied into sseEvent payloads (grep: token only as backendRequest argument). Residual: JWT travels in JSON body (aiMoveRequestBody), which an infrastructure body log could capture — not demonstrated in application logs (no LOGGING config; no console of token).
C/I/A effect: not applicable for rejected spend; residual C if body logs exist at the host
CWE mapping: none for the rejected spend claim
ASVS mapping: none for the rejected spend claim
Source-standard references: not applicable
Dynamic reproduction evidence: none (no Next.js listener). Ordering shown from source.
Static evidence: lines 88–111, 454–464, 1058–1083, 1180–1217, 1315, 846–854, 1418–1452
Synthetic containment: not applicable
False-positive analysis: this record is the refutation. A regression would be introducing generateText before the compact_state gate or treating a 401 body as compact_state.
Exploitability conclusion: not demonstrated (unauthenticated provider spend on this route)
Smallest safe correction direction: not applicable for the rejected claim. Optional hardening: read token from Authorization header instead of JSON body to reduce body-log exposure; still verify Django before any provider call
Regression-test requirement: unit test: POST /api/ai/move with missing/invalid token must not call generateText (already implied by compact_state; keep it as a negative-path lock)
Residual risk: authenticated unbounded spend is F12, not this hypothesis
Acceptance-blocking decision: non-blocking
Redaction requirements: do not log the JSON token
```

### audit-01-F06 (H-6)

```text
Finding ID: audit-01-F06
Title: Unauthenticated catalog/prompt proxies; full prompt text public; failures swallowed as HTTP 200 []
Status: open
Severity: low
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: frontend/src/app/api/models/route.ts GET line 13; prompts/route.ts GET line 5; backend/catalog/views.py AIModelListView/AIPromptListView AllowAny; serializers.py AIPromptSerializer fields include prompt
Security property: confidentiality of advisory SEARCH_PROFILE text; integrity of failure signalling
Asset at risk: prompt row text (already also sent to game participants via get_ai_context); attacker knowledge for shaping model behaviour
Trust boundary: internet to Next.js GET proxies to Django catalog
Attacker-controlled input or local actor: none on these GETs (no query used)
Reachability: unauthenticated GET /api/models and /api/prompts; Django /api/catalog/models/ and /prompts/ also AllowAny
Preconditions: none
Required privileges: none | unauthenticated
Observed or potential impact: discloses provider, model_id, display_name, description, quality_tier, context_window, max_tokens, released_at, flagship flags; and prompt id, name, full prompt, fitness. No write path on these views (admin-only writes). Swallow-to-200 empty array hides Django/catalog failure from the client (availability/integrity of UI), not a data leak. Writable catalog is Django admin, not these GETs.
C/I/A effect: C low (prompt text); I low (false empty catalog); A low
CWE mapping: CWE-200 (4.20)
ASVS mapping: v5.0.0-8.2.3 (field-level; prompts may be intentionally public)
Source-standard references: OWASP ASVS 5.0.0
Dynamic reproduction evidence: none
Static evidence: catalog/views.py permission_classes AllowAny; AIPromptSerializer fields; Next.js catch return []
Synthetic containment: not applicable
False-positive analysis: product may intend public prompt presets. If so, Orchestrator may accept-residual. Swallow-200 remains a failure-hiding behaviour.
Exploitability conclusion: probable for disclosure of whatever the serializer emits; not a write IDOR
Smallest safe correction direction: keep models list public if the UI requires it; decide whether full prompt text must be public or name/fitness only; do not convert backend failures into HTTP 200
Regression-test requirement: if prompt text is restricted, unauthenticated GET /api/prompts must omit the prompt field (fail before, pass after). Independently: Django 500 on catalog must not become HTTP 200 []
Residual risk: model ids remain public by product design
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

### audit-01-F07 (H-7)

```text
Finding ID: audit-01-F07
Title: H-7 — model output cannot choose game_id, slot, or pass/exchange/place; no production egress allowlist
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: frontend/src/app/api/ai/move/route.ts tools validateMove/finishMove (1226–1283); probeAndResolve (886–1051); backend/game/services.py submit_*_for_ai uses _load_vs_ai_session then the AI PlayerSlot, not a client slot
Security property: server-side authority over move legality; provider-boundary tool invocation
Asset at risk: game integrity (hypothesis)
Trust boundary: untrusted model output to Next.js tools to Django
Attacker-controlled input or local actor: model tool arguments (placements, ready); compact_state includes board/rack (human-influenced tiles in vs_ai, not chat — vs_ai has no chat channel)
Reachability: only after F05's authenticated context
Preconditions: valid JWT for a vs_ai game the user belongs to
Required privileges: ordinary user
Observed or potential impact: game_id and token are closed over from the HTTP body, not from the model. validateMove posts to `/api/game/${game_id}/validate-move/` with rack_owner: "ai". finishMove only aborts generation. Pass/exchange run only from probeAndResolve after GET ai-playability. max_steps is taken from the caller, clamped 5–100 — a user can inflate cost (F12), the model cannot. Chat is rendered as text in ChatPanel (`{message.body}`), not dangerouslySetInnerHTML (grep empty in repo). Production move/judge routes have no egress allowlist; one exists only in the diagnostic harness — residual info, not a demonstrated extra origin from model text.
C/I/A effect: not applicable for the rejected control-flow claim
CWE mapping: none for the rejected claim
ASVS mapping: v5.0.0-8.3.1 (positive: enforcement is server-side)
Source-standard references: OWASP Top 10 for LLM Applications v2.0 (LLM01 awareness)
Dynamic reproduction evidence: none
Static evidence: tool execute closures; _load_vs_ai_session; ChatPanel.tsx line 45; no dangerouslySetInnerHTML
Synthetic containment: not applicable
False-positive analysis: this is the refutation. A future tool that interpolated model-supplied paths would reopen it.
Exploitability conclusion: not demonstrated
Smallest safe correction direction: not applicable. Optional: production egress allowlist to openrouter.ai and integrate.api.nvidia.com (and documented direct-rival hosts) as a later bounded slice — must not be claimed as already present
Regression-test requirement: keep tests that finishMove does not call Django write endpoints; model-supplied game_id must not be read (there is no such parameter today)
Residual risk: no production egress allowlist (info); compact_state is model-visible
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

### audit-01-F08 (H-8)

```text
Finding ID: audit-01-F08
Title: H-8 — BACKEND_URL is not a request-time SSRF surface
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: module-scope `process.env.BACKEND_URL || "http://localhost:8000"` in ai/move/route.ts:39, ai/judge/route.ts:33, models/route.ts:11, prompts/route.ts:3
Security property: server-side request control
Asset at risk: not applicable if env is deployment-time only
Trust boundary: Next.js process environment vs HTTP request
Attacker-controlled input or local actor: HTTP request cannot set BACKEND_URL; no query/header/body read of it
Reachability: not established as request-time SSRF
Preconditions: not applicable
Required privileges: not applicable
Observed or potential impact: a compromised or mis-set host env could point Next.js at an attacker URL (host/config), which is out of this application request-surface claim
C/I/A effect: not applicable
CWE mapping: none
ASVS mapping: v5.0.0-13.1.1 (positive: end user cannot supply the backend location on these routes)
Source-standard references: OWASP ASVS 5.0.0
Dynamic reproduction evidence: none
Static evidence: four module-scope constants; no req.nextUrl / header override
Synthetic containment: not applicable
False-positive analysis: this is the refutation
Exploitability conclusion: not demonstrated
Smallest safe correction direction: not applicable
Regression-test requirement: not applicable
Residual risk: deployment-time BACKEND_URL must remain operator-controlled (host whole)
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

### audit-01-F09 (websocket tickets; no prior hypothesis)

```text
Finding ID: audit-01-F09
Title: Websocket tickets are replayable for 60s and travel in the query string
Status: open
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: backend/game/services.py build_ws_ticket 1224–1235, verify_ws_ticket 1238–1249; consumers.py connect() query param ticket at 24; GameWSTicketView views.py 120–128
Security property: authentication; replay resistance
Asset at risk: live game state including my_rack and chat send as that user
Trust boundary: browser/proxy logs to websocket connect
Attacker-controlled input or local actor: stolen ticket string on `/ws/game/{game_id}/?ticket=`
Reachability: ticket issued only after IsAuthenticated + membership; then anyone holding the string may connect until max_age
Preconditions: capture of the URL (access log, Referer, shared screenshot) within GAME_WS_TICKET_MAX_AGE_SECONDS (default 60)
Required privileges: none after theft | unauthenticated holder of the ticket
Observed or potential impact: connect as the bound user_id for that game_id. Tickets are bound to both user and game (payload mismatch raises). Not single-use: verify_ws_ticket twice on the same string succeeded (ws_ticket_replay_accepted=True). Chat send re-checks membership via create_chat_message_for_user (not a second ticket check — adequate if membership is what matters). room_game_state re-loads state for self.user_id. Existing tests cover invalid ticket and outsider ticket 404; they do not cover replay, expiry, or query-string leakage.
C/I/A effect: C medium (rack/chat for up to 60s); I medium (chat as victim); A low
CWE mapping: CWE-294 (4.20)
ASVS mapping: v5.0.0-7.2.3 (ticket is not a CSPRNG bearer with one-time use)
Source-standard references: CWE 4.20; OWASP ASVS 5.0.0
Dynamic reproduction evidence: synthetic verify_ws_ticket called twice on one ticket; both returned the same user_id
Static evidence: signing.dumps/loads with max_age, no nonce store; query string in consumers.py:24
Synthetic containment: temporary root, removed
False-positive analysis: 60s window may be accepted residual if logs never retain query strings and tickets stay on loopback; public VPS access logs commonly retain query strings
Exploitability conclusion: demonstrated for replay inside containment; probable for query-string leakage on a public proxy
Smallest safe correction direction: single-use (store consumed jti/hash server-side) and pass the ticket in a header or first websocket protocol subprotocol/cookie, not the query string. Keep binding to user+game and membership check on chat.
Regression-test requirement: using the same ticket twice must fail the second connect (fail before, pass after); a test that a ticket for game A is rejected on game B already exists in logic and should stay
Residual risk: a ticket stolen and used immediately still works once
Acceptance-blocking decision: blocking for a public websocket; Cooperator may accept residual if WS stays private — medium requires Cooperator sign-off if not corrected
Redaction requirements: never print live tickets
```

### audit-01-F10 (JWT lifecycle)

```text
Finding ID: audit-01-F10
Title: Password change does not invalidate access or refresh tokens; no logout/blacklist
Status: open
Severity: medium
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: accounts/serializers.py ChangePasswordSerializer.save set_password only; accounts/urls.py no logout; INSTALLED_APPS no token_blacklist; SIMPLE_JWT no ROTATE_REFRESH_TOKENS; ACCESS_TOKEN_LIFETIME 2 hours; REFRESH_TOKEN_LIFETIME 7 days
Security property: session termination
Asset at risk: stolen JWT after the user changes password
Trust boundary: bearer token vs password state
Attacker-controlled input or local actor: previously stolen access/refresh token
Reachability: change-password requires current password (enforced — test_change_password_rejects_wrong_current_password and serializer validate_current_password)
Preconditions: attacker already holds a token issued before the password change
Required privileges: ordinary user (stolen token)
Observed or potential impact: after a successful password change, the same access token still returned HTTP 200 on /api/auth/me/ as that user (old_access_token_after_password_change_status=200). No server logout. Refresh tokens remain valid up to 7 days. Frontend logout only clears Zustand/localStorage.
C/I/A effect: C/I for the remainder of token lifetime
CWE mapping: CWE-613 (4.20)
ASVS mapping: v5.0.0-7.4.1
Source-standard references: OWASP ASVS 5.0.0
Dynamic reproduction evidence: synthetic APIClient as above
Static evidence: ChangePasswordSerializer.save; SIMPLE_JWT block; no blacklist app
Synthetic containment: removed
False-positive analysis: 2-hour access lifetime caps blast of access tokens; refresh is 7 days and is the larger issue
Exploitability conclusion: demonstrated for access token after password change
Smallest safe correction direction: on password change (and a real logout), blacklist refresh tokens and reject access tokens issued before a per-user password_changed_at (or rotate a per-user key). Enable refresh rotation if blacklist is added. Do not lengthen lifetimes.
Regression-test requirement: after change-password, the previous access token and refresh token must 401 (fail before, pass after). Existing tests only check old password login fails.
Residual risk: tokens stolen and used before password change still work until expiry unless logout exists
Acceptance-blocking decision: blocking unless Cooperator accepts 2h/7d residual after password change (medium → Cooperator sign-off)
Redaction requirements: none
```

### audit-01-F11 (registration password policy)

```text
Finding ID: audit-01-F11
Title: Registration accepts 6-character passwords and skips AUTH_PASSWORD_VALIDATORS
Status: open
Severity: low
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: accounts/serializers.py RegisterSerializer password CharField min_length=6; create() does not call validate_password; settings AUTH_PASSWORD_VALIDATORS is only MinimumLengthValidator (Django default 8); ChangePasswordSerializer min_length=8 plus validate_password
Security property: authentication
Asset at risk: new accounts
Trust boundary: internet to register
Attacker-controlled input or local actor: password field
Reachability: AllowAny register
Preconditions: none
Required privileges: none | unauthenticated
Observed or potential impact: register_six_char_status=201 for password "123456". Change-password path is stricter. Common-password and similarity validators are absent even on change-password.
C/I/A effect: C/I for those accounts
CWE mapping: CWE-521 (4.20)
ASVS mapping: v5.0.0-6.2.1; v5.0.0-6.2.4
Source-standard references: OWASP ASVS 5.0.0
Dynamic reproduction evidence: synthetic register POST
Static evidence: RegisterSerializer vs ChangePasswordSerializer
Synthetic containment: removed
False-positive analysis: product may want low friction; 6 < ASVS L1 8
Exploitability conclusion: demonstrated
Smallest safe correction direction: run validate_password on register; align min length with change-password (≥8)
Regression-test requirement: POST /api/auth/register/ with a 6-char password must 400 (fail before, pass after)
Residual risk: no breached-password list unless later added
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

### audit-01-F12 (authenticated move cost; additional)

```text
Finding ID: audit-01-F12
Title: Open registration plus unthrottled /api/ai/move spends provider quota after one free account
Status: open
Severity: high
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: frontend/src/app/api/ai/move/route.ts POST (no rate limit); accounts RegisterView AllowAny; max_steps clamped 5–100 at 471–478
Security property: cost containment
Asset at risk: provider quota
Trust boundary: self-registered ordinary user to Next.js move route to providers
Attacker-controlled input or local actor: register then JWT in move body; timeout up to 600s; max_steps up to 100
Reachability: F05 shows the token must be valid, which registration issues
Preconditions: usable server provider keys; attacker can create an account (F03: no register throttle)
Required privileges: ordinary user
Observed or potential impact: not unauthenticated in the H-5 sense, but equivalent for a public internet attacker who can POST /api/auth/register/. Each move stream may call generateText with up to 100 steps plus repair reserve, across Play fallback of three pairs.
C/I/A effect: A high on quota
CWE mapping: CWE-770 (4.20)
ASVS mapping: v5.0.0-2.4.1
Source-standard references: OWASP ASVS 5.0.0; OWASP Top 10 for LLM Applications v2.0 LLM10 (awareness)
Dynamic reproduction evidence: none (no provider)
Static evidence: no rate limit on move route; RegisterView AllowAny; max_steps clamp
Synthetic containment: not applicable
False-positive analysis: if registration is later closed or invite-only, this drops. If keys are absent, generateText fails closed after auth.
Exploitability conclusion: probable
Smallest safe correction direction: per-user and per-IP rate limits on /api/ai/move (and tighter max_steps ceiling for new accounts) in addition to F01/F03. Do not alter MOVE CORE, completion_source enum, or MAX_FALLBACK_ATTEMPTS without Orchestrator+product authority
Regression-test requirement: an authenticated client exceeding the move rate limit must get 429 and generateText must not be called on the rejected request
Residual risk: legitimate play still consumes quota
Acceptance-blocking decision: blocking
Redaction requirements: none
```

### audit-01-F13 (register enumeration)

```text
Finding ID: audit-01-F13
Title: Registration discloses username uniqueness
Status: open
Severity: low
Confidence: high
Evidence class: reproduced-dynamic
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: accounts/serializers.py RegisterSerializer username unique via User model; register_duplicate_username_status=400 with username in the error body
Security property: authentication (account enumeration)
Asset at risk: username existence
Trust boundary: internet to register
Attacker-controlled input or local actor: username field
Reachability: AllowAny
Preconditions: none
Required privileges: none | unauthenticated
Observed or potential impact: confirm whether a username is taken. Login does not differentiate unknown vs bad password (same 401 detail).
C/I/A effect: C low
CWE mapping: CWE-204 (4.20)
ASVS mapping: v5.0.0-6.3.8 (L3; recorded as mapping only, not a claim that L3 is required)
Source-standard references: OWASP ASVS 5.0.0
Dynamic reproduction evidence: synthetic duplicate register
Static evidence: ModelSerializer unique username
Synthetic containment: removed
False-positive analysis: many apps accept this residual
Exploitability conclusion: demonstrated
Smallest safe correction direction: generic register error; still enforce uniqueness server-side
Regression-test requirement: duplicate username response body must not contain a field-specific username error (fail before, pass after) while still not creating a second user
Residual risk: timing differences not measured
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

### audit-01-F14 (object-level game authorization)

```text
Finding ID: audit-01-F14
Title: Horizontal game IDOR — server-derived membership and acting slot
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: game/views.py every APIView permission_classes = IsAuthenticated; services._load_session_for_user filters public_id plus slots__user_id; acting slot is that PlayerSlot (or AI slot from _load_vs_ai_session). No client slot field on submit/pass/exchange/give-up. ValidateMoveSerializer rack_owner is player|ai only.
Security property: per-object authorization
Asset at risk: other users' games (hypothesis)
Trust boundary: ordinary user to another user's game
Attacker-controlled input or local actor: game_id path; queue cancel game_id (still passed through _load_session_for_user)
Reachability: authenticated outsider GETs 404 (tests and code)
Preconditions: not applicable
Required privileges: ordinary user
Observed or potential impact: AGENTS.md claim "server-derived acting slot only; client slot trust removed" matches the service layer. Outsider GameStateView, AIContextView, GameWSTicketView return 404. vs_human opponent rack is not in _serialize_slot (rack_count only; my_rack is own slot).
C/I/A effect: not applicable
CWE mapping: none
ASVS mapping: v5.0.0-8.2.2 (positive)
Source-standard references: OWASP ASVS 5.0.0
Dynamic reproduction evidence: none in this session (existing tests in test_api.py are data under analysis; this Worker verified the service functions)
Static evidence: _load_session_for_user 394–416; views pass request.user.id
Synthetic containment: not applicable
False-positive analysis: this is the refutation. rack_owner=ai on vs_human falls through to the caller's rack (no opponent-rack oracle).
Exploitability conclusion: not demonstrated
Smallest safe correction direction: not applicable
Regression-test requirement: keep outsider 404 tests on state, ai-context, ws-ticket, ai-playability, ai-candidates
Residual risk: UUID game_id is unguessable enough for this cut; not a substitute for the membership check, which exists
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

### audit-01-F15 (stored XSS / known-good)

```text
Finding ID: audit-01-F15
Title: Stored XSS via chat or model text — no dangerouslySetInnerHTML
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: frontend/src/components/game/ChatPanel.tsx message.body in a text node; repo-wide grep of dangerouslySetInnerHTML empty
Security property: absence of stored XSS
Asset at risk: session/JWT in localStorage if XSS existed
Trust boundary: chat text to browser
Attacker-controlled input or local actor: chat body (capped 500 server-side)
Reachability: vs_human participants only
Preconditions: a future innerHTML sink would reopen this
Required privileges: ordinary user in the same game
Observed or potential impact: React text interpolation escapes HTML. No contrary evidence.
C/I/A effect: not applicable
CWE mapping: none
ASVS mapping: none
Source-standard references: not applicable
Dynamic reproduction evidence: none (no browser authority)
Static evidence: ChatPanel.tsx; grep empty
Synthetic containment: not applicable
False-positive analysis: this is the refutation for the current tree
Exploitability conclusion: not demonstrated
Smallest safe correction direction: not applicable
Regression-test requirement: not applicable
Residual risk: a new sink in a later slice
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

### audit-01-F16 (A7 git hygiene)

```text
Finding ID: audit-01-F16
Title: Tracked secrets in Git — none found
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 7a71180329d69499d09d124483bb2e0c4c935636
Affected component and exact location: .gitignore ignores .env, backend/.env, frontend/.env.local; only .example templates are intended for commit
Security property: secret handling
Asset at risk: none found tracked
Trust boundary: Git history
Attacker-controlled input or local actor: not applicable
Reachability: public GitHub repository
Preconditions: not applicable
Required privileges: not applicable
Observed or potential impact: git ls-files and full-history name scan found no `.env` / credential filenames; git grep -l for private-key blocks and sk-or-/nvapi- patterns returned empty (excluding .ap). Stop-for-Orchestrator-if-tracked-secret did not trigger.
C/I/A effect: not applicable
CWE mapping: none
ASVS mapping: v5.0.0-13.3.1 (positive for source tree)
Source-standard references: OWASP ASVS 5.0.0
Dynamic reproduction evidence: git name scans
Static evidence: .gitignore lines 28–35; .env.example templates
Synthetic containment: not applicable
False-positive analysis: history that renamed files could still hide a secret under another path; scan was name- and pattern-based, not a full entropy sweep
Exploitability conclusion: not demonstrated
Smallest safe correction direction: not applicable
Regression-test requirement: not applicable
Residual risk: complete historical blob search was not performed
Acceptance-blocking decision: non-blocking
Redaction requirements: if a later scan finds a tracked secret, report PATH ONLY
```

### Out-of-scope observations (not findings)

- Redis `CHANNEL_LAYERS` default `redis://127.0.0.1:6379/0` without password: host-hardening (4.9) if Redis is exposed.
- `DB_PASSWORD` default `libretiles` when `DB_ENGINE=postgresql`: configuration footgun; host/deploy.
- SQLite-vs-Postgres drift: security-relevant only if production accidentally uses file sqlite (locking/backup); not demonstrated.
- Django admin at `/admin/` is session-authenticated; superuser is not auto-provisioned in code; admin can toggle `is_active` and edit prompts. Expected Django shape; harden in host/admin-ops, not a missing AllowAny.
- Prepared direct rivals (Groq, Gemini, watsonx, …) seed `is_active_on_create=False`; they join the judge/move queues only if an admin activates them.

---

## Findings ranked for correction

1. **F02** — without a unique SECRET_KEY, every other control is forgeable.  
2. **F04** — DEBUG/ALLOWED_HOSTS/CORS on a public address.  
3. **F01** — unauthenticated provider spend.  
4. **F12** — same spend after one free registration.  
5. **F03** — stuffing and registration flood, also feeds F12.  
6. **F10** — stolen-token survival after password change.  
7. **F09** — WS ticket replay/query string.  
8. **F11, F13, F06** — password length, enumeration, public prompts.

---

## PRE-DEPLOYMENT BLOCKING LIST

Must be corrected before this application is exposed on a public address:

- **audit-01-F02** (fail closed on SECRET_KEY)  
- **audit-01-F04** (DEBUG false; explicit ALLOWED_HOSTS; production CORS; TLS cookie/HSTS/SSL-redirect at app or documented equivalent in the later host audit)  
- **audit-01-F01** (no unauthenticated generateText)  
- **audit-01-F12** (rate-limit AI move; do not rely on obscurity of registration)  
- **audit-01-F03** (throttle login/register/refresh)

Must be corrected **or** take explicit Cooperator sign-off as residual (medium):

- **audit-01-F10**  
- **audit-01-F09**

May ship with documented residual (Orchestrator may accept low/info):

- **audit-01-F06, F11, F13**  
- All `rejected-false-positive` records (F05, F07, F08, F14, F15, F16)

---

## Limitations

- Did not start Next.js or Django runserver; did not call a live provider; therefore F01/F12 spend is probable from code, not demonstrated as billed quota.  
- Did not measure Next.js body-size rejection for huge `words` arrays.  
- Did not measure login timing differentials.  
- Did not exercise Channels against a live Redis.  
- Did not open `backend/.env` or `frontend/.env.local`; W009 absence when SECRET_KEY was not overridden only shows that whatever value was already in the process environment was not the short public fallback.  
- Did not audit host TLS, firewall, or Vercel WAF (4.9).  
- Did not audit lockfiles/CVEs (4.7).  
- Browser XSS claim is static (no browser authority).  
- Git hygiene was name- and selected-pattern-based, not a full historical blob entropy sweep.

---

## Residual-risk summary

Low/info items (F06, F11, F13, and rejected-false-positive records) may be Orchestrator-accepted with a recorded Residual-Risk Decision Contract. Medium (F09, F10) and high/critical (F01–F04, F12) require Cooperator sign-off if not corrected. Nothing in this report is silently accepted.

---

## Deviations, risks, and missing evidence

- Authorized Python-route deviation used throughout; declared `poetry run` route not used.  
- `check --deploy` with the public fallback adds W009; Orchestrator’s five-warning list is the DEBUG-true run without forcing that fallback. Both are reported.  
- Independence: this Worker did not read `01_report_00.md`.

## One smallest next step

The Orchestrator accepts or rejects each finding, obtains Cooperator sign-off for any residual of medium or higher, then issues bounded correction grants with exact path allowlists — typically fail-closed SECRET_KEY and DEBUG first, then judge/move authentication and throttles — followed by a fresh independent re-audit (P-10) because corrections touch authentication, authorization, and secret handling.

Report justification: new-evidence  
Logical-whole closure: not-closed  
Authority expiry statement: this exchange's authority expires with this terminal report. Retained context is not a renewal. Autonomous work stops here.

Resolved Execution Issues / Near-Misses: none that escaped containment. Near-miss avoided: Django was not pointed at `backend/db.sqlite3`; synthetic sqlite stayed in the declared root and was removed.

Pre-Existing Failure Classification: Cursor AppImage ambient Python hijack — pre-existing, not repaired; sanitized `.venv/bin/python` deviation used as granted.
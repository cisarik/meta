### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 13  
Worker exchange ordinal: 01

Status: PASS  
Phase-qualified result: not-applicable  
Start commit: `b5774b24c6779fd45bd06c4859b2674ec76af17e`  
End commit: `b5774b24c6779fd45bd06c4859b2674ec76af17e`  
Changed paths: none  
Validation: read-only analysis plus authorized loopback header readback on `127.0.0.1:3300`, synthetic body/redaction probes in `/tmp/libretiles-p10-reaudit`, and `npm audit --package-lock-only`. Full pytest/mypy/ruff/build suites were not re-run (prompt section 2).  
Git result: read-only, none  
Deviations and missing evidence: used the existing frontend production `.next` rather than rebuilding; did not query OSV; did not contact Django on port 8000; did not run `mypy --no-incremental` as a comparison.  
Smallest next step: set DRF `NUM_PROXIES` so unauthenticated throttle identity cannot be chosen by `X-Forwarded-For`, add a same-`REMOTE_ADDR` / distinct-XFF regression test, then scoped re-audit of `audit-01-F03` and `audit-03-F01`.  
Report justification: new-material-risk  
Authority expiry: this exchange’s authority expires with this terminal report. I do not correct, implement, close the logical whole, or emit a closure signal.

Independence: I did not implement or correct any part of this candidate in this session.

Resolved Execution Issues / Near-Misses: the first redaction probe file was written with a Python docstring and failed to parse as ESM; it was rewritten in the temporary root and re-run. Not a product defect.  
Pre-Existing Failure Classification: none

---

## Audit header

Security task class: fresh independent re-audit (INFOSEC.md 4.11, structural profile P-10); INFOSEC route R6.

Owned/authorized target: repository `/home/agile/Projects/libretiles`, owned by the Cooperator (Michal Cisárik), canonical remote `https://github.com/cisarik/libretiles`. Authorization basis: Cooperator ownership plus Orchestrator grant in `13_reaudit_00.md`. No other system is in scope.

Commit under audit: `b5774b24c6779fd45bd06c4859b2674ec76af17e`

Scope: whether each finding in section 5 of the prompt, recorded as `corrected`, now holds the **original security property**, by the claimed mechanism, including correction-vs-correction interactions and residual accuracy.

Exclusions: host/infrastructure hardening; live provider calls; reading `backend/.env` or `frontend/.env.local`; mutating the canonical repository; Cooperator processes on ports 3000 and 8000; re-derivation of the Orchestrator-measured green gates and of Cooperator-executed live acceptance dated 2026-08-31.

Repository gate (before analysis): HEAD `b5774b24c6779fd45bd06c4859b2674ec76af17e`; `HEAD:.ap` and `.ap HEAD` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `## main...origin/main`; porcelain empty; `git ls-remote origin refs/heads/main` equal to HEAD.

### Source records

| Title | Owner | Version / edition | Status | Retrieval date | AP concept |
|---|---|---|---|---|---|
| OWASP ASVS | OWASP | 5.0 | final | 2026-09-01 (via `.ap/INFOSEC.md` §19 registry dated 2026-07-19; not independently re-fetched) | verification-requirement mapping |
| MITRE CWE corpus | MITRE | corpus current; cited as 4.20 where the original findings used that edition | taxonomy | 2026-09-01 (same registry) | weakness taxonomy |
| OWASP Top 10 for LLM Applications | OWASP GenAI | v2.0 | awareness | 2026-09-01 (same registry) | provider-boundary awareness only |
| Django 5.2 `RequestDataTooBig` / `SuspiciousOperation` | Django Software Foundation | installed `django==5.2.17` | tooling / framework | 2026-09-01 | exception class of the login-body read |
| Django REST framework `BaseThrottle.get_ident` | Encode / DRF | installed package; `NUM_PROXIES` default `None` in `rest_framework/settings.py` | tooling | 2026-09-01 | throttle identity |
| django-axes `get_client_ip_address` / `conf.py` | jazzband | installed `django-axes==8.3.1` | tooling | 2026-09-01 | lockout identity |
| npm advisory output | npm | `npm audit --package-lock-only` at this commit | tooling | 2026-09-01 | remaining frontend advisories |

---

## Threat model

Derived for this re-audit from the tree at the commit under audit. I read the prior audit’s model and did not copy it as authority.

Assets: Django `SECRET_KEY` (JWT and WS-ticket signing); user passwords and Django admin sessions; JWT access and refresh tokens in `localStorage`; websocket tickets; provider credentials held only on the Next.js server; provider quota; game state including racks and chat; the integrity of rate-limit and lockout counters; server logs as an egress path.

Trust boundaries: unauthenticated internet → Next.js (pages, `/api/*` App Router, proxy); unauthenticated internet → Django (`/api/auth/*`, `/admin/`, catalog); browser → `localStorage`; Next.js server → Django; Next.js server → external providers; Django → Redis/channel layer; application code → stderr / Django logs.

Attacker-controlled inputs: JSON auth bodies; `X-Forwarded-For`; `Host`; registration fields; AI route JSON; websocket `ticket` query parameter; provider error text that may echo request material; prefetch headers.

Security properties relied on: fail-closed secret and production settings; server-side authentication before provider spend; object-level membership checks; single-use tickets; session termination on password change and logout; IP-and-account brute-force brakes; enforced CSP and security headers on documents the browser actually executes; credential material never reaching logs or SSE.

Abuse cases: (a) boot without a unique `SECRET_KEY` and forge JWTs; (b) unauthenticated `/api/ai/judge` spend; (c) credential stuffing on login/admin; (d) registration spam; (e) WS-ticket replay; (f) XSS plus `localStorage` token theft if CSP is absent on the play document; (g) lockout as DoS; (h) provider error text carrying a key into logs or SSE; (i) choosing a new throttle identity per request via `X-Forwarded-For`.

---

## Verdict table

Evidence class abbreviations: ES = established-static; RD = reproduced-dynamic.

| ID | Original property | Claimed mechanism | Verdict | Evidence | Class |
|---|---|---|---|---|---|
| audit-01-F02 | Token integrity: no public fallback `SECRET_KEY` | `_require_secret_key()` refuses missing/empty/whitespace/public-fallback/weak/`django-insecure-` keys | **verified-closed** | `backend/config/settings.py:26-50,77`; isolated subprocess probes in `test_security_settings.py` (dotenv disabled) | ES |
| audit-01-F04 | No debug disclosure; explicit hosts; production CORS; TLS cookie/HSTS/SSL-redirect at app | `DEBUG` default false; wildcard `ALLOWED_HOSTS` rejected when not debug; `CORS_ALLOW_ALL_ORIGINS = DEBUG`; Secure cookies, `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS` follow `not DEBUG` | **verified-closed** | `settings.py:78-79,60-74,192-198`; forbidden deploy IDs still W004/W008/W012/W016/W018 only (`test_security_settings.py:31-38,287-298`). W005/W021 remain **orch-02-D11**, not this finding | ES |
| orch-01-F17 | Future DRF views fail closed | `DEFAULT_PERMISSION_CLASSES = IsAuthenticated`; catalog `AllowAny` explicit | **verified-closed** | `settings.py:254-256`; `test_drf_default_permission_classes_are_fail_closed`; catalog tests still 200 unauthenticated | ES |
| audit-01-F01 | No unauthenticated provider spend on `/api/ai/judge` | Bearer extracted and `verifyUserBearerToken` **before** body catalog fetch / `generateText`; size caps 12×15 | **verified-closed** | `judge/route.ts:221-232` then 240-271 then 315; tests at `judge/route.test.ts:555-684` | ES |
| audit-01-F03 | Bounded auth stuffing / registration spam / refresh / admin | DRF scoped throttles **plus** axes on login/admin | **not accepted** | Throttles exist (`auth_register` 20/h, `auth_login` 60/h, `auth_refresh` 60/h) and axes covers login/admin on `REMOTE_ADDR`. Unauthenticated DRF identity is **not** that address: `NUM_PROXIES` is unset (DRF default `None`), so `BaseThrottle.get_ident` returns the attacker-controlled `X-Forwarded-For` with spaces stripped (`rest_framework/throttling.py:23-40`). Register and refresh have no axes layer. Original risk of unbounded registration spam still holds against a direct client. See **audit-03-F01** | ES |
| audit-01-F11 | Registration password policy ≥8 with Django validators | `min_length=8` + `validate_password` in `RegisterSerializer.validate` | **verified-closed** | `accounts/serializers.py:16-34`; `AUTH_PASSWORD_VALIDATORS` four Django defaults; Cooperator live acceptance | ES |
| audit-01-F12 | Authenticated AI spend is rate-limited | Django `ai_context` 200/h (authenticated → `user.pk`); move route does not call `generateText` without `compact_state`; judge gated by `/api/auth/me/` (`auth_me` 200/h) | **verified-closed** | `game/views.py` `throttle_scope = "ai_context"`; `move/route.ts` context then `compact_state` gate; `move/route.test.ts` “does not call generateText when Django ai-context returns HTTP 429”. Scale of *account creation* is F03/audit-03-F01, not a missing move-route limiter | ES |
| audit-01-F10 | Session termination on password change and a real logout | `password_changed_at` + `PasswordAwareJWTAuthentication` (missing `iat` fail-closed) + refresh serializer; `token_blacklist` + `ROTATE_REFRESH_TOKENS`; `LogoutView`; change-password and admin form also blacklist | **verified-closed** | `accounts/authentication.py:48-57`; `serializers.py:75-80`; `views.py:66-96`; `admin.py:17-29`; Cooperator: old session “Session expired” | ES |
| audit-01-F09 (replay half) | Ticket not reusable | SHA-256 unique `ConsumedWsTicket`; consume inside `verify_ws_ticket` before `group_add` | **verified-closed** | `services.py:1231-1291`; `test_ws_ticket_single_use.py`; `test_multiplayer_ws.py` replay → 4403. Query-string transport remains the accepted residual | ES |
| orch-01-F18 | Security headers + enforced CSP on Next.js HTML the browser executes | `frontend/src/proxy.ts` applies `buildSecurityHeaders` on the matcher | **verified-closed** | Loopback production `next start` `127.0.0.1:3300` (PID 63946): **every** document and App Router path probed — `/`, `/play`, `/settings`, `/game/{id}`, `/waiting/{id}`, `/draw/{id}`, `/api/models`, `/api/prompts`, `GET /api/ai/move` (405) — emitted the same CSP, nosniff, referrer-policy, DENY, permissions-policy, COOP, HSTS `max-age=31536000; includeSubDomains` as the Orchestrator’s `GET /`. Matcher exclusions confirmed: `favicon.ico`, `/_next/static/…`, `Next-Router-Prefetch`, `Purpose: prefetch` have **no** security headers (by design; those are not the HTML document). `middleware.ts` is absent. `script-src`/`style-src 'unsafe-inline'` remain accepted residuals | RD |
| orch-01-F20 | Admin (and API login) brute-force brake | `django-axes==8.3.1`; `AXES_FAILURE_LIMIT=8`; `AXES_LOCKOUT_PARAMETERS=[["username","ip_address"]]`; backend first; middleware last | **verified-closed** | `settings.py:164-167,290-295,101-114`; `test_admin_login_brake.py` 8th attempt 429, other username on same IP still authenticates. `ipware` is **not installed**; axes falls back to `REMOTE_ADDR` (`axes/helpers.py:222-225`). Cross-IP lockout of the Cooperator is not available | ES |
| acc-01-D01 | Channel-layer failure diagnosable; ticket accounting explicit | Close 4503; ERROR log with `game_id`, `user_id`, exception type/message; consume-before-accept documented | **verified-closed** | `consumers.py:56-92`; tests assert 4503 ≠ 4403, log has no ticket/`ticket=`, count +1 | ES |
| acc-01-D02 | Provider failures logged, bounded, no secrets in SSE | `recordProviderFailure` → stderr; SSE classified messages are constants (`AUTH_MESSAGE` / `RATE_LIMIT_MESSAGE` / `UNAVAILABLE_MESSAGE`) or `BOUNDED_INTERNAL_ERROR`; `boundedAiMetadata` has no error string | **verified-closed** | `provider-logging.ts`; `ai-runtimes.ts:159-225`; `move/route.ts:727-757,1419-1432`. Over-redaction of model ids/URLs in `generate_text` is a diagnostic residual, not a reopen of the observability gap | ES |
| acc-01-D03 | Registration validation not swallowed as invalid credentials | `api.register` throws; home `handleAuth` does not fall through to login on that throw; 400 uses field message | **verified-closed** | `page.tsx:37-76`; `api.ts:152-157,282-283`; `api.test.ts` numeric-password 400. Duplicate username no longer auto-logs-in (shows F13 residual instead) | ES |
| acc-01-D04 | Users do not see `API error 429: {…}` | `humanMessageForStatus`; 429 → human minutes, no `API error`, no JSON brace | **verified-closed** | `api.ts:134-170`; `api.test.ts:16-38` | ES |
| acc-01-D05 | Login throttle usable for a demo | `auth_login` 60/h; axes 8/30min is the account brake | **verified-closed** | `settings.py:269-270,290-293`; comment arithmetic for ~16 same-NAT logins | ES |
| acc-01-D06 | Fresh clone can boot | `scripts/libretiles.sh` copies `.env.example` only when absent and writes `secrets.token_hex(32)` into `DJANGO_SECRET_KEY`; existing `.env` untouched | **verified-closed** | `scripts/libretiles.sh:248-281`; AGENTS.md/README onboarding | ES |
| acc-01-D07 | Docs match judge attempts and ticket TTL | README judge “up to three attempts”; `GAME_WS_TICKET_MAX_AGE_SECONDS` example/default 10; pre-existing `.env` override note | **verified-closed** | `README.md:81,91,289`; `settings.py:304`; `.env.example`. Remaining: AGENTS.md “Code quality” still omits `npm run typecheck` (F22 process residual, not this defect’s original items) | ES |
| orch-02-D08 | AGENTS.md names nine providers | Opening bullet + key-file rows | **verified-closed** | `AGENTS.md:7,83-85` | ES |
| orch-02-D09 | Logout hits the blacklist endpoint | `api.logout`; `handleLogout` posts then clears locally, failure swallowed | **verified-closed** | `api.ts:291-296`; `page.tsx:771-790`; `api.test.ts:139+`. `LogoutView` still has no `throttle_scope` (optional in the original direction, not required for the wiring defect). 401-on-fetchState `clearAuth` is not a user logout | ES |
| orch-02-D10 | Admin password change records revocation | `RefreshBlacklistingAdminPasswordChangeForm.save` calls `blacklist_outstanding_refresh_tokens`; `set_password` still stamps `password_changed_at`; JWT layer rejects predating `iat` | **verified-closed** | `admin.py:17-29`; `models.py:31-44`; `test_admin_password_change_blacklists_outstanding_refresh` | ES |
| orch-02-D12 | Glue not in settings.py; no dead LocMem branch | `config.middleware.AxesDrfLockoutFlagMiddleware`; `_default_cache` has no unreachable LocMem-after-Redis assignment | **verified-closed** | `middleware.py`; `settings.py:211-243`; `test_axes_is_wired_in_required_order` | ES |
| orch-02-F21 | Logs cannot be defeated by the project’s own credential-shaped fixtures | Value match against held env (min 8, placeholders skipped, longest first); Bearer/prefix/entropy denylist; `provider_transport` message replaced with `transport failure` | **verified-closed** | `provider-logging.ts:37-151`; `ibm-watsonx.test.ts:779-810` asserts the log record. Adversarial copy of the rules: held values redacted; transport omits raw; `sk-or-` prefix caught even when unheld; 16-char entropy run redacted; sub-8 env values and `eu-de` are not value-matched (transport still omits). Case-folded echo of a 16-char key is still caught by entropy, not by value match | ES + RD (copied rules) |
| orch-02-D13 | 401 with a bearer is not “invalid username or password” | `humanMessageForStatus(..., Boolean(opts.token))` | **verified-closed** | `api.ts:154-157,266-273`; tests token vs tokenless 401. Wrong current password is HTTP 400 with “Current password is incorrect.” (`ChangePasswordView`). Home page remaps 401 → invalid credentials only on the unauthenticated login/register form | ES |
| orch-04-F22 | Typecheck success is not an incremental-cache illusion | `package.json` `"typecheck": "tsc --noEmit --incremental false"` | **verified-closed** | Separate non-incremental gate exists. `tsconfig.json` still has `"incremental": true` for `next build` (intentional). `mypy` still defaults incremental; that is a **different** failure mode (narrowed path), already known. Vitest/pytest do not have a tsc-style cached-success hole | ES |
| audit-02-F02 | Django below patched 5.2.17 | `django = "^5.2.17"` lock `5.2.17` | **verified-closed** | `pyproject.toml`; `poetry.lock`; installed `django==5.2.17`. OSV 0 taken as given per section 2 | ES |
| audit-02-F03 | Daphne below patched 4.2.2 | lock `daphne==4.2.3` | **verified-closed** | lock + installed `4.2.3`. OSV 0 taken as given | ES |
| audit-02-F04 | `redis` declared for `RedisCache` | `redis = "^7.3.0"` main group | **verified-closed** | `pyproject.toml:15`; `poetry.lock` `groups = ["main"]` version 7.3.0 | ES |
| audit-02-F01 | `next` 16.2.0 advisory cluster | `next@16.3.4`; production audit empty | **verified-closed** | `package.json` `16.3.4`; `npm audit --package-lock-only --omit=dev` → `found 0 vulnerabilities`; full audit still 3, all `dev: true` (`js-yaml@4.1.1`, `brace-expansion`) | ES + RD |
| orch-03-G01 | `sharp` in production optional tree below 0.35.0 | lock `sharp@0.35.4` optional | **verified-closed** | `package-lock.json` `node_modules/sharp` version 0.35.4, `optional: true`, not `dev` | ES |
| orch-03-G02 | Undispositioned Django `GHSA-8qcx-xf44-272x` | Django 5.2.17 OSV total 0 | **verified-closed** | Bump removes the advisory set. Reachability was never established and need not be. OSV 0 taken as given | ES |

---

## Residual accuracy

| Residual | Description still matches? | Severity still right? | Widened? |
|---|---|---|---|
| audit-01-F13 duplicate-username disclosure | Yes. `RegisterSerializer` still exposes uniqueness; D03 no longer hides it behind login. Cooperator sign-off | low | No |
| audit-01-F09 ticket in query string | Yes. `ws.ts:7-8` still `ticket=`. TTL default 10. Cooperator sign-off | low | No (TTL tighter than the original 60s) |
| audit-01-F06 public prompts + swallow-to-200 | Yes. Catalog `AllowAny`; Next proxies still `return NextResponse.json([], { status: 200 })` on Django failure (`models/route.ts`, `prompts/route.ts`) | low | No |
| orch-01-F18 `script-src 'unsafe-inline'` | Yes, production CSP still includes it. Cooperator sign-off, nonce routed to UX/i18n | medium | No |
| orch-01-F18 `style-src 'unsafe-inline'` | Yes | low | No |
| orch-01-F18 `middleware.ts` convention | **Closed in fact.** Only `proxy.ts` remains. This sub-residual’s recorded description is stale and should be dropped at closure bookkeeping | was low | Narrowed to gone |
| audit-02-F05 no CI/SBOM/signing | Yes. No `.github`. Cooperator sign-off 2026-09-01 | medium | No |
| audit-02-F06 no frontend dev-import guard | Still open `info`; no frontend AST guard analogous to `test_game_app_has_no_dev_imports.py` | info | No |
| orch-02-D11 HSTS flags | **Imprecise as originally written; Orchestrator correction is right.** Two emitters: (1) Django `SECURE_HSTS_SECONDS` set, `SECURE_HSTS_INCLUDE_SUBDOMAINS` / `PRELOAD` unset → W005/W021 on Django responses when `DEBUG` is false; (2) Next.js proxy emits `includeSubDomains` without `preload` on the HTML/API origin this re-audit probed. Which host a browser pins depends on deployment topology (Vercel vs Django VPS), which this repository does not fix. Not widened. Still open, still correctly routed to UX/i18n for `includeSubDomains` vs subdomain-locale | low | No |

Rejected false positives (F05, F07, F08, F14, F15, F16, audit-02-F07–F12): no contrary evidence. `dangerouslySetInnerHTML` still absent under `frontend/src`. `npm audit --omit=dev` is zero, so F07’s “dev-only” verdict still holds even though brace-expansion now carries more GHSA rows.

---

## Answers to the nine thin spots

**1. Proxy matcher / headers off `/`.** Established. Headers **are** on `/play`, `/settings`, `/game/[id]`, `/waiting/[id]`, `/draw/[id]`, and the Next `/api/` routes probed. Identical CSP/HSTS set as the Orchestrator `GET /`. Favicon, `_next/static`, and prefetch-marked requests omit them, matching `proxy.ts:19-28`. A full document load of `/play` (no prefetch header) is **not** decorative. Could not: browser enforcement (HTTP client only, as authorized); whether Vercel production sets `NEXT_PUBLIC_API_URL` to a non-loopback origin (connect-src would then differ by design).

**2. Axes/DRF glue `request.body`.** Established. For JSON, `POST.get("username")` is empty and does not consume the stream; `username_from_auth_request` then `json.loads` the body and returns only the username. Password is not retained. Invalid JSON / raw-post-already-read return `None` and the view still runs. **`RequestDataTooBig` is not in the except tuple** (`AttributeError`, `OSError`, `RawPostDataException` only). MRO: `RequestDataTooBig` → `SuspiciousOperation` — it **propagates**. Django maps that to HTTP 400, which is the same class of failure the view would raise on an oversized body. Not proved with a live oversized POST. No sensitive material is copied onto the Django request by this function; `propagate_axes_lockout_to_django_request` copies axes lockout flag/credentials, not the password field.

**3. Value redaction vs diagnostics.** Both directions judged. A real held credential ≥8 characters is literally replaced; `provider_transport` never logs the raw message; prefix/Bearer/entropy remain. A credential **not** in `CREDENTIAL_ENV_NAMES`, under 8 characters, or only URL-encoded, can survive value match; transport still omits. Over-redaction is real on `generate_text`: `nvidia/nemotron-3-super-120b-a12b` becomes `model [redacted] is overloaded`; `openrouter.ai` hostnames lose the high-entropy run. Benign strings from the S7b fixtures survive. D02’s diagnostic purpose is reduced but not destroyed (phase, status, error class, and a stub remain). F21’s secret property holds.

**4. Axes lockout as DoS.** Orchestrator belief **holds for a different address**: lockout key is username **and** IP; `ipware` is not installed, so IP is `REMOTE_ADDR`; `X-Forwarded-For` does **not** move axes. Same-NAT / same `REMOTE_ADDR`: an attacker who knows the username **can** lock that pair for 30 minutes. Package default `AXES_RESET_COOL_OFF_ON_FAILURE_DURING_LOCKOUT = True` is not overridden, so further failures during lockout refresh cooloff — a same-IP extender, not a cross-IP DoS. Behind a reverse proxy that leaves `REMOTE_ADDR` as the proxy, the key collapses toward username-only; that is host-audit territory. Not a reopen of F20’s original “no brake” claim.

**5. Websocket 4503.** Log format is `game_id`, `user_id`, exception type, `str(exc)` — no ticket, no query string. Tests assert that. Consume happens in `verify_ws_ticket` **before** `group_add`, so 4503 still burns one hash row; single-use unique constraint is intact. Could not: a real Redis exception whose message contained the handshake URL (not observed in code paths).

**6. 401 and `Boolean(opts.token)`.** No path found where a token-bearing 401 ought to read as invalid credentials. Login/register do not pass a token. Wrong current password is 400. Expired/blacklisted/pre-`password_changed_at` access is session-expiry wording, which matches Cooperator live acceptance. New messages do not disclose user existence beyond the pre-existing login 401.

**7. Correction vs correction.** (a) Axes vs DRF throttles vs cache: complementary stores (DB vs cache vs Redis-required in production), **divergent IP identity** — this is audit-03-F01. (b) Provider logging vs SSE: classified SSE strings are constants; logs are separate; F21 does not undo D02. (c) Proxy vs `resolveApiBase()`: `resolveConnectApiBase` is a documented mirror; unit tests cover loopback rewrite; live CSP on 3300 showed `http://localhost:8000` + `ws://localhost:8000` with `NEXT_PUBLIC_API_URL` unset. (d) Admin form + `set_password` + JWT: timestamp invalidates even if blacklist bookkeeping failed; form also blacklists. No conflict.

**8. F22 remedy and other cached-success gates.** `tsc --noEmit --incremental false` is sufficient for the hole that let `next build` succeed with type errors in tests. `mypy` remains incremental by default; the documented 80-file scope is the existing mitigation; I did not prove or disprove a stale `.mypy_cache` success. Pytest has no such cache. Vitest’s transform cache does not report green for failing tests.

**9. Dual HSTS emitters.** Django: `SECURE_HSTS_SECONDS = 31536000` when not debug; neither `INCLUDE_SUBDOMAINS` nor `PRELOAD` set. Next.js proxy: `includeSubDomains`, no preload, only when `NODE_ENV !== development` (`security-headers.ts:109-112`), observed on 3300. Browser visiting the Next origin gets includeSubDomains on that host; browser talking to Django gets Django’s header on the API host. D11 as “a production deployment gets HSTS without includeSubDomains” is true of Django and false of the Next document origin.

---

## New findings

```text
Finding ID: audit-03-F01
Title: Unauthenticated DRF throttles take identity from client X-Forwarded-For
Status: open
Severity: medium
Confidence: high
Evidence class: established-static
Affected commit: b5774b24c6779fd45bd06c4859b2674ec76af17e
Affected component and exact location: rest_framework.throttling.BaseThrottle.get_ident (installed DRF); rest_framework.settings NUM_PROXIES default None; backend/config/settings.py REST_FRAMEWORK block with no NUM_PROXIES; accounts RegisterView / ScopedTokenRefreshView throttle_scope auth_register / auth_refresh
Security property: integrity of IP-keyed authentication rate limits; bounded registration spam (original audit-01-F03)
Asset at risk: registration endpoint (account spam); refresh-token guessing volume; coarse login throttle (login still has axes on REMOTE_ADDR)
Trust boundary: unauthenticated client headers to Django throttle cache keys
Attacker-controlled input or local actor: HTTP header X-Forwarded-For (or HTTP_X_FORWARDED_FOR in WSGI META)
Reachability: any caller who can reach Django without a proxy that overwrites X-Forwarded-For. This repository does not set NUM_PROXIES or SECURE_PROXY_SSL_HEADER. Django currently listens on 127.0.0.1:8000 in the Cooperator’s process; a public VPS without nginx real-ip/XFF overwrite has the same application behaviour.
Preconditions: unauthenticated view using ScopedRateThrottle; NUM_PROXIES is None
Required privileges: none | unauthenticated
Observed or potential impact: get_ident returns ''.join(xff.split()) if XFF is present, else REMOTE_ADDR. Each distinct XFF string is a fresh 20/hour register bucket and a fresh 60/hour refresh bucket. Login stuffing remains bounded by axes (REMOTE_ADDR + username, ipware not installed).
C/I/A effect: A high on registration and on the coarse IP throttle; C/I low unless stuffing succeeds on login (axes still holds)
CWE mapping: CWE-307 (4.20); CWE-290 (4.20) client-supplied identity
ASVS mapping: v5.0 6.3.1 / 2.4.1
Source-standard references: OWASP ASVS 5.0; CWE 4.20; DRF BaseThrottle.get_ident docstring
Dynamic reproduction evidence: none (would have required django.setup against settings and either the Cooperator DB or a pytest file; identity function is unambiguous from installed source)
Static evidence: rest_framework/throttling.py:23-40; rest_framework/settings.py 'NUM_PROXIES': None; settings.py REST_FRAMEWORK has no NUM_PROXIES; axes/helpers.py:222-225 REMOTE_ADDR fallback; importlib.util.find_spec('ipware') is None
Synthetic containment: none for this claim
False-positive analysis: would be disproved if a mandatory reverse proxy always overwrites XFF and NUM_PROXIES were set to the proxy count; that is not in this application. Would be disproved if RegisterView were not AllowAny (it is).
Exploitability conclusion: probable
Smallest safe correction direction: set NUM_PROXIES to 0 while this app is reached without a trusted proxy, so get_ident uses REMOTE_ADDR and matches axes; if a proxy is introduced, set NUM_PROXIES to that count and pin trusted proxy configuration in the host whole. Do not trust raw XFF. Add a test: two unauthenticated register POSTs with distinct X-Forwarded-For and the same REMOTE_ADDR must share one throttle key.
Regression-test requirement: the test just named; must fail before NUM_PROXIES is 0 (or an equivalent ident that ignores untrusted XFF) and pass after
Residual risk: behind a proxy with NUM_PROXIES=0, all clients share the proxy address and the IP throttle becomes global — conservative, not spoofable. Distributed stuffing across real addresses remains host/WAF territory
Acceptance-blocking decision: blocking for closure of audit-01-F03; the new record itself is medium and would need Cooperator sign-off if accepted as residual instead of corrected
Redaction requirements: none
```

No other `audit-03` findings. No new `rejected-false-positive` of my own.

---

## Containment ledger

```text
Temporary root: /tmp/libretiles-p10-reaudit
Owner: Worker session 13 exchange 01
Mode: 0700
Contents class: probe scripts, captured response headers (no bodies kept), no secrets, no project source copies
Cleanup owner: this Worker
Cleanup outcome: removed
```

Loopback target: `127.0.0.1:3300` only. Listener PID 63946 (`next-server`). Stopped with `kill 63946`. Port 3300 closed. Cooperator listeners unchanged: python `41753` on `127.0.0.1:8000`, `next-server` `63016` on `*:3000`.

---

## Limitations

- Did not re-run mypy, ruff, pytest, `manage.py check`, `npm run typecheck`, lint, or `npm run build` (prompt section 2).
- Header readback used the existing `.next` production build, not a rebuild in this session. CSP on `/` matched the Orchestrator’s recorded string.
- HTTP client is not a browser; CSP is present as a header, not shown enforced in Chromium.
- Did not send requests to port 8000; Django HSTS is static-only.
- Did not dynamically drive DRF `get_ident` through `APIClient` (to avoid the Cooperator database and django.setup/dotenv).
- Did not query `https://api.osv.dev` (section 2).
- Did not compare `mypy` incremental vs `--no-incremental`.
- Did not re-fetch NIST/OWASP catalogs; used the INFOSEC.md registry.
- `PROJECT_CONTEXT.md` §1 is stale at the commit it claims to reconcile (still says Next.js 16.2.0, installed Django 5.2.12, `middleware.ts`, redis as undeclared transitive). Repository wins.

---

## Residual-risk summary

Medium or higher still requiring Cooperator sign-off:

- `orch-01-F18` `script-src 'unsafe-inline'` — **already signed off**; nonce upgrade remains in UX/i18n.
- `audit-02-F05` no CI/SBOM/signing — **already signed off 2026-09-01**.
- **`audit-01-F03` is not verified-closed.** Combined with **`audit-03-F01` (medium)**, unauthenticated register/refresh IP brakes are not bound to the client address. This needs a correction or a new Cooperator residual decision. I do not accept it.

Low residuals (Orchestrator-acceptable under INFOSEC 14): F13, F09 query string, F06, style-src unsafe-inline, D11 HSTS flags, same-NAT axes lockout, transport-phase diagnostic omission, generate_text over-redaction of model ids, `LogoutView` unthrottled, AGENTS.md omitting `typecheck`.

---

## Closure recommendation

**This logical whole should not close on this evidence.** Thirty of thirty-one corrected findings are `verified-closed`. **`audit-01-F03` is `not accepted`.** New finding **`audit-03-F01`** is the reason: the DRF throttle identity is attacker-selectable via `X-Forwarded-For` while axes, correctly, is not. Login/admin stuffing is held. Registration spam is not.

I emit no closure signal.

---

## Explicit confirmations

Commands run (none of the forbidden set): `git rev-parse HEAD`, `git rev-parse HEAD:.ap`, `git -C .ap rev-parse HEAD`, `git status -sb`, `git status --porcelain=v1`, `git ls-remote origin refs/heads/main`; `ss` on the named ports; `npx next start -H 127.0.0.1 -p 3300` with `NEXT_PUBLIC_API_URL` unset; `curl -D` header captures to the temp root; `backend/.venv/bin/python` on the temp body probe (no `config.settings` import); `node` redaction probe; reads of installed `axes` / DRF / Django exception classes; `npm audit --package-lock-only` and `--omit=dev`; `kill 63946`; `rm -rf /tmp/libretiles-p10-reaudit`; final `git status --porcelain=v1`.

Forbidden commands **not** run: `npm install` / `ci` / `update` / `audit fix`; `poetry add` / `lock` / `install`; `pip install`; any file edit in the repository; any Git write; no second pytest `-q`.

`git status --porcelain=v1` is empty at the end of the session.

I read no `.env` file, made no provider call, and did not disturb the Cooperator’s processes or ports 3000/8000.

What in prompt sections 2, 3, or 5 was wrong: section 2’s established gates and live acceptance were not contradicted. Section 3.1’s **gap** was real at prompt time and is now **disproved** for document and `/api/` routes (CSP is not decorative on `/play`). Section 3.4’s belief that a different IP cannot axes-lock the Cooperator is **correct**. Section 5’s D11 wording is the known imprecision about which HSTS emitter a browser sees. `PROJECT_CONTEXT.md` (mandatory reading, evidence not authority) is stale versus this commit on Next/Django/proxy/redis. `npm audit` still reports 3, all `dev: true`; `--omit=dev` is 0.
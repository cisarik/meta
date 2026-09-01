### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 07  
Worker exchange ordinal: 01

**Status:** PASS  
**Phase-qualified result:** Implementation PASS (non-independent). orch-01-F18 correction candidate is on `main`. This Worker does not certify the correction and does not close the whole.

**Start commit:** `437e20f95a671474074afcb7c412d7733426c72e`  
**End commit:** `445029d35474cba9f363734c19cf969226fbe5ed`

**Changed paths (purpose):**
- `frontend/src/lib/security-headers.ts` — pure header/CSP builder; `connect-src` mirrors `resolveApiBase()` using the request hostname
- `frontend/src/lib/security-headers.test.ts` — unit tests 1–8
- `frontend/src/middleware.ts` — request-time header application only; no auth, cookies, Django, or token-store access
- `backend/config/settings.py` — explicit `SECURE_CONTENT_TYPE_NOSNIFF`, `SECURE_REFERRER_POLICY`, `X_FRAME_OPTIONS`, `SECURE_CROSS_ORIGIN_OPENER_POLICY`
- `backend/tests/test_security_settings.py` — tests 9–12; test 13 left unchanged

`git diff --stat 437e20f95a671474074afcb7c412d7733426c72e HEAD`:

```text
 backend/config/settings.py                |   6 ++
 backend/tests/test_security_settings.py   |  26 ++++++
 frontend/src/lib/security-headers.test.ts | 131 ++++++++++++++++++++++++++++++
 frontend/src/lib/security-headers.ts      | 114 ++++++++++++++++++++++++++
 frontend/src/middleware.ts                |  29 +++++++
 5 files changed, 306 insertions(+)
```

`git diff --name-only` (same range): the five allowlisted paths above. `frontend/next.config.ts`, `frontend/src/app/layout.tsx`, and `README.md` were not touched.

**Repository gate (pre-edit):**
- `git rev-parse HEAD` → `437e20f95a671474074afcb7c412d7733426c72e`
- `git rev-parse HEAD:.ap` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `git -C .ap rev-parse HEAD` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `git status -sb` → `## main...origin/main`
- `git status --porcelain=v1` → empty
- `git ls-remote origin refs/heads/main` → `437e20f95a671474074afcb7c412d7733426c72e`

**Pre-push gate:** `git ls-remote origin refs/heads/main` still `437e20f95a671474074afcb7c412d7733426c72e` immediately before `git push origin main`.

**Capability handshake:** requested session model is Cursor Grok 4.6 (not independently attested). Declared `poetry run …` backend route is unusable under Cursor AppImage (`APPIMAGE`/`PYTHONHOME`). Task-authorized deviation used: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy|pytest|manage.py` and `.venv/bin/ruff`. Frontend via `npx` / `npm` from `frontend/`. Ambient `python` / `python3` / `poetry run` were not used as a parallel route.

---

**Exact final CSP strings**

Development (`isDevelopment: true`, `NEXT_PUBLIC_API_URL` unset, request host `localhost`):

```text
default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' http://localhost:8000 ws://localhost:8000; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'
```

Production (`isDevelopment: false`, configured API `https://api.libretiles.example`):

```text
default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' https://api.libretiles.example wss://api.libretiles.example; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'; upgrade-insecure-requests
```

`connect-src` is request-derived. LAN rewrite (loopback configured base + non-loopback host `192.168.10.25`) yields `connect-src 'self' http://192.168.10.25:8000 ws://192.168.10.25:8000`.

**Directive justifications:**
- `default-src 'self'` — deny unspecified fetches
- `script-src 'self' 'unsafe-inline'` — Next.js 16.2.0 “Without Nonces” path; see residual below. Production does **not** include `'unsafe-eval'`
- `script-src` + `'unsafe-eval'` — development only; local CSP guide: React uses `eval` for HMR / server-error reconstruction
- `style-src 'self' 'unsafe-inline'` — Tailwind is external; Framer Motion sets inline `style` attributes; Next.js may inline CSS. Nonce does not cover style attributes
- `img-src 'self' data:` — no `next/image` and no external image origins in `src/`
- `font-src 'self'` — no remote fonts / `next/font` remote source
- `connect-src 'self' <http-origin> <ws-origin>` — `'self'` covers same-origin SSE `/api/ai/move`; Django HTTP + derived `ws:`/`wss:` are required. `connect-src 'self'` alone would break the product
- `frame-ancestors 'none'` — clickjacking
- `base-uri 'self'` — block `<base>` hijack
- `form-action 'self'` — form targets
- `object-src 'none'` — plugins
- `upgrade-insecure-requests` — production only; would break plain-HTTP local play

**Companion headers:** `X-Content-Type-Options: nosniff`; `Referrer-Policy: strict-origin-when-cross-origin`; `X-Frame-Options: DENY`; `Permissions-Policy: camera=(), microphone=(), geolocation=()`; `Cross-Origin-Opener-Policy: same-origin`; `Strict-Transport-Security: max-age=31536000; includeSubDomains` in production only.

**Local Next.js docs followed:** `frontend/node_modules/next/dist/docs/01-app/02-guides/content-security-policy.md` (also `…/headers.md`, `…/production-checklist.md`, `…/03-file-conventions/proxy.md`). This version (16.2.0) specifies: (1) nonce + `proxy.ts` + dynamic rendering for strict CSP; (2) without nonces, `script-src 'self' 'unsafe-inline'` plus `'unsafe-eval'` in development; (3) `middleware` renamed to `proxy` in v16.0.0, functionality unchanged; `middleware.ts` still loads with a deprecation warning. Assumed mechanism (request-time CSP from `Host`, not a static `headers()` string) still holds. `proxy.ts` is outside the allowlist, so `frontend/src/middleware.ts` was used. `next.config.ts` `headers()` was not added: a baked string cannot express the LAN `connect-src` rewrite.

**`frontend/src/app/layout.tsx`:** not touched. The nonce mechanism applies framework scripts automatically from the CSP header during SSR; layout nonce-read is documented only for third-party `<Script>` / GTM. This app has none. Forcing dynamic rendering to make a nonce CSP work on `/`, `/play`, `/settings` would require layout/page edits outside the nonce-read exception.

---

**Tests 1–13 before/after**

| # | Assertion | Pre-fix | Post-fix |
|---|---|---|---|
| 1 | Required header names present | FAIL — `Cannot find module './security-headers'` (suite 0 tests) | PASS |
| 2 | CSP `default-src 'self'`, `frame-ancestors 'none'`, `object-src 'none'`, `base-uri 'self'`, `form-action 'self'` | FAIL — same import error | PASS |
| 3 | Non-loopback https API → `connect-src` has https and wss | FAIL — same | PASS |
| 4 | Unset API URL → `http://localhost:8000` and `ws://localhost:8000` | FAIL — same | PASS |
| 5 | Non-loopback host + loopback configured base → rewritten http and ws on that host | FAIL — same | PASS |
| 6 | HSTS absent in development, present in production | FAIL — same | PASS |
| 7 | `upgrade-insecure-requests` absent in development | FAIL — same | PASS |
| 8 | Production `script-src` does not contain `'unsafe-eval'` | FAIL — same | PASS |
| 9 | `SECURE_CONTENT_TYPE_NOSNIFF` True and named in `settings.py` | FAIL — name absent from source | PASS |
| 10 | `SECURE_REFERRER_POLICY` explicit strict value | FAIL — name absent | PASS (`same-origin`) |
| 11 | `X_FRAME_OPTIONS == "DENY"` | FAIL — name absent | PASS |
| 12 | `SECURE_CROSS_ORIGIN_OPENER_POLICY` explicit | FAIL — name absent | PASS (`same-origin`) |
| 13 | Production-like `check --deploy` omits W004, W008, W012, W016, W018 (unchanged test) | source unchanged | PASS (included in the 5-test post-fix run) |

**`check --deploy` warning IDs** (local `DJANGO_DEBUG=true` process, both runs): **before** `security.W004`, `W008`, `W012`, `W016`, `W018`; **after** the same five. DEBUG-derived plain HTTP is intact. The isolated production-like probe (test 13) still emits none of those IDs.

**Standing gates**
- `npx vitest run src/lib/security-headers.test.ts` → `Test Files  1 passed (1)` / `Tests  8 passed (8)`
- unchanged frontend suite → `Test Files  5 passed (5)` / `Tests  131 passed (131)`
- `npm run lint` → no errors
- `npm run build` → succeeded (Next.js 16.2.0 webpack). Warning: `The "middleware" file convention is deprecated. Please use "proxy" instead.` Routes: `○ /`, `○ /play`, `○ /settings` static; `ƒ /api/ai/move`, `ƒ /game/[id]`, `ƒ Proxy (Middleware)`
- mypy `config game gamecore accounts catalog` → `Success: no issues found in 79 source files`
- `ruff check .` → `All checks passed!`
- pytest → **`302 passed, 4 skipped in 140.44s (0:02:20)`** (298 + 4 new backend tests, 4 skipped)

**Runtime browser validation was NOT performed** and is deferred to the Cooperator-executed acceptance sweep. `npm run build` succeeding does not prove runtime CSP behaviour. This Worker does not claim the application still works in a browser.

**Residuals**
- Production and development `script-src` contain `'unsafe-inline'`. Next.js 16.2.0 documents this for the without-nonce path. A nonce + `'strict-dynamic'` policy would ignore `'unsafe-inline'` and would not stamp nonces onto prerendered `/`, `/play`, `/settings` without force-dynamic on non-allowlisted pages. Recorded, not silently accepted.
- Development `script-src` contains `'unsafe-eval'` (documented React/HMR requirement). Production does not.
- `style-src` contains `'unsafe-inline'` in both environments (Framer Motion inline style attributes).
- `frontend/src/middleware.ts` is the deprecated file convention; Next.js 16 still executes it. Migrating to `proxy.ts` is outside this allowlist.

**Authorized Git result:** one commit `445029d35474cba9f363734c19cf969226fbe5ed` on `main`; `git push origin main` (no flags) fast-forwarded `437e20f..445029d`. Public readback: `git ls-remote origin refs/heads/main` = `git rev-parse HEAD` = `445029d35474cba9f363734c19cf969226fbe5ed`. Post-push porcelain empty.

**Deviations / risks / missing evidence:**
- File convention `middleware.ts` vs documented `proxy.ts` (deprecated, still functional; allowlist).
- Without-nonce `script-src` rather than nonce CSP (static routes + layout/page force-dynamic not allowlisted).
- No browser/engine evidence of the enforced CSP. Highest product risk remains a wrong `connect-src` killing Django HTTP, the game websocket, or same-origin SSE; unit tests cover origin derivation, not the browser.
- Test 13 was not re-run in isolation against the unmodified tree; its source was not modified and it passed after the settings change.

**Out-of-scope observations (not findings):** Next.js 16 deprecates `middleware` in favor of `proxy`. Experimental SRI (`experimental.sri`) was not used (experimental, webpack-only, cannot cover inline bootstrap, `next.config.ts` only allowlisted for an additional `headers()` entry).

**Smallest next step:** Orchestrator routes S7 — django-axes for the admin login brake, throttle-rate tuning, a shared throttle cache when DEBUG is false, admin-path refresh-token blacklisting, wiring the frontend logout call, and the onboarding secret-key generation.

**Report justification:** new-evidence  
**Logical-whole closure:** not-closed  
**Authority expiry:** this exchange's authority expires with this terminal report. Retained context is not a renewal.

**Resolved Execution Issues / Near-Misses:** first CSP draft used nonce + `'strict-dynamic'` per the strict-CSP example. `next build` then showed `/`, `/play`, `/settings` as static; nonce injection requires dynamic rendering, which needs layout/page changes outside the allowlist. Switched to the documented without-nonce `script-src` (including production `'unsafe-inline'`) and recorded it as a residual. No allowlist breach.

**Pre-Existing Failure Classification:** none
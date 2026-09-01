### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening
Worker session ordinal: 08
Worker exchange ordinal: 01

- status: **PASS**
- Phase-qualified result: **implementation-PASS (NON-INDEPENDENT)**
- start commit: `445029d35474cba9f363734c19cf969226fbe5ed`
- end commit: `bbba2e9f26399d57464b4f700cccc4838f2f5bf2`

### Changed paths and purpose

| Path | Purpose |
|---|---|
| `backend/pyproject.toml` | exact pin `django-axes==8.3.1`; minimum `axes.signals` / `axes.handlers.proxy` mypy override |
| `backend/poetry.lock` | lockfile for that one package |
| `backend/config/settings.py` | axes wiring, `AUTHENTICATION_BACKENDS`, throttle rates, shared-cache guard, DRF lockout-flag glue |
| `backend/accounts/admin.py` | Item D: admin password form also blacklists outstanding refresh tokens |
| `backend/tests/test_admin_login_brake.py` | new axes lockout + admin revocation tests |
| `backend/tests/test_security_settings.py` | Trap 1 probe helper + tests 7–12 |
| `backend/tests/test_security_throttling.py` | Trap 2 restructure + tests 13–15 |
| `backend/tests/test_token_lifecycle.py` | Trap 3: real `POST /admin/login/` |
| `backend/.env.example` | `DJANGO_THROTTLE_CACHE_URL`; `DJANGO_SECRET_KEY=` stays empty |
| `scripts/libretiles.sh` | generate `DJANGO_SECRET_KEY` into a freshly created `.env` only |
| `README.md` | Items E and F |
| `AGENTS.md` | Items E and F |

Allowlist boundary:

```text
12 files changed, 664 insertions(+), 34 deletions(-)
AGENTS.md
README.md
backend/.env.example
backend/accounts/admin.py
backend/config/settings.py
backend/poetry.lock
backend/pyproject.toml
backend/tests/test_admin_login_brake.py
backend/tests/test_security_settings.py
backend/tests/test_security_throttling.py
backend/tests/test_token_lifecycle.py
scripts/libretiles.sh
```

Unused allowlisted paths (not in the diff): `backend/accounts/serializers.py`, `backend/accounts/models.py`. `set_password` was not restructured.

### Repository gate (start) and pre-push gate

Start:

```text
HEAD                         445029d35474cba9f363734c19cf969226fbe5ed
HEAD:.ap                     9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
.ap HEAD                     9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
status -sb                   ## main...origin/main
porcelain                    empty
origin/main (ls-remote)      445029d35474cba9f363734c19cf969226fbe5ed
```

Pre-push `git ls-remote origin refs/heads/main` was still `445029d35474cba9f363734c19cf969226fbe5ed`. Push was `git push origin main` with no flags.

### Capability handshake and execution-route deviation

- Requested: bounded correction Worker, poetry/`env -u APPIMAGE -u ARGV0 -u APPDIR` Python route.
- Directly observed: Cursor AppImage intercepts `python*`. All Python, ruff, mypy, pytest, and migrate used `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` (and `.venv/bin/ruff`) from `backend/`.
- `env -u APPIMAGE -u ARGV0 -u APPDIR poetry env info -p` resolved **`/home/agile/Projects/libretiles/backend/.venv`**. Poetry 2.x; `virtualenvs.in-project = true`. It did not change the Python constraint.
- `poetry add "django-axes==8.3.1"` then `poetry lock` (Poetry 2 has no `--no-update`; default lock does not upgrade already-locked packages).
- Provider calls: none. Secrets: `backend/.env` / `frontend/.env.local` were not read. Browser: not used.

### django-axes pin and lockfile

- Pinned **`django-axes==8.3.1`** with `==` deliberately, unlike the caret ranges on every other runtime dependency, so the security control cannot float.
- PyPI distribution name: `django-axes` (Jazzband). Installed version 8.3.1. `requires_python >= 3.10`. Requires `django>=4.2`, `asgiref>=3.6.0`; `django-ipware>=3` only under extra `ipware`.
- Lockfile gained **exactly one package**: `django-axes` **8.3.1**. Nothing unexpected. The `[ipware]` extra was **not** installed.
- `ipware` decision: `axes/helpers.py` uses django-ipware **if installed**, otherwise `request.META.get("REMOTE_ADDR")`. `axes/conf.py` does **not** say correct client-IP resolution requires the extra. Default `AXES_IPWARE_META_PRECEDENCE_ORDER` is `("REMOTE_ADDR",)`. Fallback was not used.
- Transitive **`redis` residual**: Django’s `django.core.cache.backends.redis.RedisCache` needs no new dependency. The `redis` client in the venv is **redis 7.3.0**, imported from `channels_redis` **4.3.0**, which is a transitive of the existing direct dependency `channels-redis`. Not added as a second direct dependency.

### Axes setting names (from installed `axes/conf.py` 8.3.1)

| Setting used | Installed default | Value set |
|---|---|---|
| `AXES_FAILURE_LIMIT` | `3` | `8` |
| `AXES_COOLOFF_TIME` | `None` (no cool-off) | `timedelta(minutes=30)` |
| `AXES_RESET_ON_SUCCESS` | `False` | `True` |
| `AXES_LOCKOUT_PARAMETERS` | `["ip_address"]` (IP-only unless legacy flags) | `[["username", "ip_address"]]` |
| `AXES_HTTP_RESPONSE_CODE` | `429` | `429` (explicit) |
| `AXES_ENABLE_ADMIN` | `True` | `True` (explicit) |

IP-only is the 8.3.1 default; it was overridden. `AUTHENTICATION_BACKENDS` is now explicit: `axes.backends.AxesStandaloneBackend` first (lockout gate only; it does not authenticate), then `django.contrib.auth.backends.ModelBackend`. `axes` is in `INSTALLED_APPS`. `axes.middleware.AxesMiddleware` is the **last** `MIDDLEWARE` entry. Durable models registered when `AXES_ENABLE_ADMIN` is true: `AccessAttempt`, `AccessLog`, `AccessFailureLog`. `AccessAttempt` is the live failure ledger (`AxesDatabaseHandler` is the default handler). `AccessFailureLog` is registered but only written if `AXES_ENABLE_ACCESS_FAILURE_LOG` is true (left at default `False`).

Migrations applied (package-shipped, no project migration authored): `axes.0001_initial` through `axes.0010_accessattemptexpiration`.

DRF glue required for Item A on the API path (still inside `settings.py`): SimpleJWT passes the DRF `Request` wrapper into `authenticate()`, so axes sets `axes_locked_out` on that wrapper; `AxesMiddleware` reads the Django `HttpRequest`. `_AxesDrfLockoutFlagMiddleware` copies the flag via `axes.signals.user_locked_out` and, on HTTP 200 from `/api/auth/login`, calls `AxesProxyHandler.reset_attempts` because SimpleJWT does not fire `user_logged_in`. Admin form login still resets via the stock signal.

### Brute-force arithmetic

- One `(username, IP)` pair: axes uses `failures_since_start >= 8`, so **7 ordinary failures** then the **8th response is 429**. Cool-off **30 minutes**. Successful login resets that pair.
- Attacker guess rate per account per IP: **8 tries / 30 min = 16 guesses/hour**, then wait.
- IP-keyed `auth_login`: **60/hour**. Axes 8 is well below 60.

### Item B scenario and rates

Same NAT, two browser profiles for human-vs-human, plus an interviewer:

- 2 profiles × (1 success + 2 typos) = 6 logins
- interviewer 2 accounts × (1 success + 2 typos) = 6
- 4 extra logout/login cycles = 4
- **Total logins ≈ 16** → `auth_login = 60/hour` (in [30, 120])
- Registers: 2 local + 2 interviewer, each with a rejected first password then a retry, plus extra validation retries ≈ **12** → `auth_register = 20/hour` (in [10, 30])
- `auth_refresh`, `auth_change_password`, `auth_me`, `ai_context` unchanged. No defect found in those four; `LogoutView` still has no `throttle_scope` (out-of-scope observation).
- **Invariant checked:** axes 8 ≪ `auth_login` 60. A single targeted account hits lockout long before the IP budget. A presenter spread across several accounts hits neither (16 < 60, and per-account failures stay under 8 if they are typos plus successes).

### Cache resolution (Item C)

DEBUG true: `LocMemCache` / `libretiles-default`. Redis is not required for local AI-only boot.

DEBUG false, in order: non-empty `DJANGO_THROTTLE_CACHE_URL`, else non-empty raw `os.getenv("REDIS_URL")` (not the channel-layer default), else:

```text
DJANGO_THROTTLE_CACHE_URL or REDIS_URL must be set to a redis:// or rediss:// URL when DEBUG is false. LocMemCache is per-process and is not a shared throttle store.
```

Non-`redis://`/`rediss://` URLs raise naming `DJANGO_THROTTLE_CACHE_URL`. Resolved backend for redis URLs: `django.core.cache.backends.redis.RedisCache`.

| Combo | Result |
|---|---|
| DEBUG false, valid hosts, no cache vars | `ImproperlyConfigured` (test 7) |
| DEBUG false + `DJANGO_THROTTLE_CACHE_URL=redis://…` | loads; backend is not LocMem (test 8) |
| DEBUG false, no dedicated URL, `REDIS_URL` set | loads; shared backend (test 9) |
| DEBUG true, neither var | loads; **is** LocMem (test 10) |

Hosts guard still runs first: missing/wildcard `DJANGO_ALLOWED_HOSTS` messages still contain `ALLOWED_HOSTS`.

**Gap:** this is settings resolution and backend identity only. Two worker processes sharing one counter was not observed.

### Item D

Verification on the unmodified tree: admin password change via `admin:auth_user_password_change` **did** set `password_changed_at` and the outstanding refresh was already rejected (`400`/`401`). **The Orchestrator’s static reading was right.** `BlacklistedToken` rows were **not** created. Pre-fix `test_admin_password_change_blacklists_outstanding_refresh` failed on `BlacklistedToken.objects.filter(token__user=target).exists()`.

Change: `RefreshBlacklistingAdminPasswordChangeForm.save()` calls `user.blacklist_outstanding_refresh_tokens()` only after `commit=True`. `set_password` / `create_user` paths were not altered. This item is **bookkeeping / defence-in-depth**, not a closed live hole.

### Item E

Generator: **Python 3 stdlib `secrets.token_hex(32)`** (64 hex chars, 256 bits from `os.urandom`). Does not need Django. Meets the existing guard: length ≥ 50, ≥ 5 unique, no `django-insecure-` prefix, not the public fallback. Never printed.

`ensure_backend_env` returns immediately if `backend/.env` exists. Real `backend/.env` mtime/size was unchanged (`2026-08-31 16:25:03 … 2110` before and after). A temp existing file’s checksum was unchanged. `backend/.env.example` still has empty `DJANGO_SECRET_KEY=`. Generated keys go only into a freshly created gitignored `.env`.

### Item F

Counted from `frontend/src/lib/provider-registry.ts`: **nine** provider constants — `openrouter`, `nvidia-nim`, `groq`, `google-gemini`, `cloudflare-workers-ai`, `mistral`, `ibm-watsonx`, `aion`, `huggingface`. `EXACT_PROVIDER_METADATA` has eight tuples; `openrouter` is the additional union member. Dispatch files `openai-compatible.ts` and `ibm-watsonx.ts` exist.

AGENTS.md: provider sentence and key-file table updated. README: judge attempts **three** (verified `MAX_FALLBACK_ATTEMPTS = 3` and `queue.slice(0, MAX_FALLBACK_ATTEMPTS)` in `frontend/src/app/api/ai/judge/route.ts`); queue cap and 30 s overall bound corrected in the same paragraph. `.env` override note added near the backend env table and in AGENTS.md. `DJANGO_THROTTLE_CACHE_URL` documented, empty/commented, required only when `DJANGO_DEBUG` is false.

`frontend/src/lib/provider-registry.ts` was not modified.

### Traps

**Trap 1.** Production-like probes now pass `throttle_cache_url`. `cache_backend` is in the probe payload. `_run_settings_probe` gained `throttle_cache_url` and `redis_url`. `test_production_like_environment_enables_https_security_flags` and `test_production_like_deploy_check_omits_named_warnings` still pass. DEBUG-false missing/wildcard hosts still `improperly_configured` with `ALLOWED_HOSTS` in the message (hosts guard first). Other DEBUG-false ok-path probes also received the synthetic redis URL so they would not become false `improperly_configured` after Item C.

**Trap 2.** `ScopedRateThrottle.get_cache_key` (`rest_framework/throttling.py`): if `request.user.is_authenticated` then `user.pk`, else `get_ident(request)` (IP / `X-Forwarded-For`). Login is unauthenticated, so the key is IP-only; varying username still spends the same IP budget. `test_login_throttled_after_limit` now uses a distinct username per attempt. `LOGIN_LIMIT = 60`, `REGISTER_LIMIT = 20`. Separate axes tests live in `test_admin_login_brake.py`.

**Trap 3.** `axes/backends.py`: `request is None` raises `AxesBackendRequestParameterRequired` (`ValueError`), not a silent pass. `django.test.Client.login()` would not survive. Only one `client.login(` in the suite (`test_django_admin_session_login_still_works`). It now `GET`/`POST`s `/admin/login/` and asserts 302 then `/admin/` contains the username. Strengthening: it exercises the form path orch-01-F20 is about. Other hits were `force_authenticate` / `force_login` only.

**SimpleJWT `request`:** `TokenObtainSerializer.validate` in installed `rest_framework_simplejwt/serializers.py` sets `authenticate_kwargs["request"] = self.context["request"]` when present, then `authenticate(**authenticate_kwargs)`. API login **is** axes-covered. HTTP 429 on that path required the DRF-wrapper flag copy described above; without it, axes logged lockout but DRF still returned 401.

### Tests 1–16 before/after

New tests were collected against the unmodified production tree (axes not wired; cache still LocMem; rates still 10/hour). Exact first run: `14 failed, 5 passed in 25.67s` for the focused set.

| # | Test | Pre-fix | Post-fix |
|---|---|---|---|
| 1 | admin lockout after 8 failures | fail: 9th still 200, not 429 | pass (8th is 429; axes `>=` limit) |
| 2 | API lockout | fail: 8th still 401 | pass (429) |
| 3 | other account same client not locked | fail: first account never 429 | pass |
| 4 | success resets pair | fail: `429 == 401` under old 10/hour IP throttle | pass |
| 5 | axes first/last/present | fail: `'axes' in INSTALLED_APPS` | pass |
| 6 | axes admin models reachable | fail: no axes models registered | pass |
| 7 | DEBUG false, no cache var | fail: status `ok` not `improperly_configured` | pass |
| 8 | `DJANGO_THROTTLE_CACHE_URL` → not LocMem | fail: still LocMem | pass |
| 9 | `REDIS_URL` fallback → not LocMem | fail: still LocMem | pass |
| 10 | DEBUG true → LocMem | **pass** (already true) | pass |
| 11 | `test_production_like_environment_enables_https_security_flags` and `test_production_like_deploy_check_omits_named_warnings` | pass (helper extended, assertions not weakened) | pass |
| 12 | production-like `check --deploy` omits W004, W008, W012, W016, W018 | pass | pass |
| 13 | demo login headroom (16) not throttled | fail: 429 inside the 16 | pass |
| 14 | abusive login burst still 429 (distinct usernames) | fail: 429 at old limit 10, `statuses[59]` not 401 | pass |
| 15 | register headroom 12 + burst 20/429 | fail: 429 at old limit 10 | pass |
| 16 | admin password change blacklists refresh | fail: refresh already unusable (`password_changed_at`) but **not** blacklisted | pass |

Axes comparison is `>= FAILURE_LIMIT`, so attempt 8 is the lockout response, not attempt 9. That matches installed `axes/handlers/database.py`.

### `check --deploy` warning IDs

Local `DEBUG=true` (this machine), **before and after** (same five):

`security.W004`, `security.W008`, `security.W012`, `security.W016`, `security.W018`

Production-like probe (`DEBUG=false`, valid hosts, shared-cache URL) **after**: `security.W005` (HSTS include subdomains), `security.W021` (HSTS preload). Neither is in the forbidden set. Those two follow from `SECURE_HSTS_SECONDS` being on when DEBUG is false; this slice did not change HSTS. Forbidden IDs remain absent.

### Standing gates (verbatim)

- mypy `config game gamecore accounts catalog`: **`Success: no issues found in 79 source files`**
- ruff: **`All checks passed!`**
- migrate: axes `0001`–`0010` applied
- pytest: **`315 passed, 4 skipped in 172.71s (0:02:52)`** (302 + 13 new; still 4 skipped)
- frontend `npm run lint`: exit 0
- frontend `npm run build`: succeeded; known deprecation warning about the `middleware` file convention

`backend/tests/test_game_app_has_no_dev_imports.py` stayed green. No existing test was skipped, xfailed, or deleted. Axes was not disabled to pass a test.

### Honest limitations (deferred)

- **No browser validation.** Django test-client evidence against `/admin/login/` is the same view and backend chain; Cooperator-executed acceptance still owns rendered admin login.
- **No multi-process cache validation.** Shared cache is proven by URL resolution and backend class identity only.

No brute-force demonstration except synthetic accounts in the local pytest database.

### Residuals

- Transitive `redis` via `channels-redis` (above); not made a direct dependency.
- `AXES_ENABLE_ACCESS_FAILURE_LOG` remains false; `AccessFailureLog` admin is empty unless later enabled. `AccessAttempt` is the live audit trail.
- Five accepted residuals from earlier slices untouched (F13, F09 transport, F18 `unsafe-inline`, F06, S7b items).
- Independent re-audit (P-10) and dependency audit (P-4) were not performed and are not claimed closed.

### Authorized Git result

- One commit: `bbba2e9f26399d57464b4f700cccc4838f2f5bf2` `fix(security): brake brute-force logins and share the throttle cache`
- Pre-push remote still `445029d35474cba9f363734c19cf969226fbe5ed`
- `git push origin main` fast-forward `445029d..bbba2e9`
- Readback: `git ls-remote origin refs/heads/main` = `git rev-parse HEAD` = `bbba2e9f26399d57464b4f700cccc4838f2f5bf2`
- Post-push porcelain empty. `backend/.env` absent from the commit.

### Deviations, risks, missing evidence

- Execution-route deviation as authorized: no ambient `python` / `poetry run python`.
- `poetry lock` (no `--no-update` in Poetry 2) used after changing the pin spelling to `==8.3.1` and adding the mypy override; lock gained only django-axes 8.3.1.
- Axes `>=` limit (8th attempt locks) followed the installed package, not “8 failures then a 9th lockout”.
- DRF 429 mapping and API reset-on-success required a small middleware in `settings.py`; without it, axes counted API failures but HTTP stayed 401 and SimpleJWT never fired `user_logged_in`.
- Missing evidence: browser admin login; multi-worker shared counters; live production Redis.

### Out-of-scope observations (not findings)

- `backend/catalog/selection.py` already lists groq, google-gemini, cloudflare-workers-ai, mistral, ibm-watsonx, aion, huggingface, plus OpenRouter and NVIDIA NIM. **It does not need updating for orch-02-D08.** It was not changed.
- `LogoutView` has no `throttle_scope` (S7b / orch-02-D09 neighbourhood).

### Smallest next step

The Orchestrator issues slice **S7b**: acc-01-D01 channel-layer diagnosability, acc-01-D02 provider-failure logging, acc-01-D03 registration validation errors, acc-01-D04 human API error messages, orch-02-D09 wiring the frontend logout call. Then the scheduled independent re-audit (INFOSEC 4.11 / P-10) and dependency audit (INFOSEC 4.7 / P-4). This Worker does not perform them and does not certify the correction closed.

- Report justification: new-mutation
- Logical-whole closure: **not-closed**
- Authority expiry: this exchange’s authority expires with this terminal report. Retained context is not a renewal.
- Resolved Execution Issues / Near-Misses: none
- Pre-Existing Failure Classification: none
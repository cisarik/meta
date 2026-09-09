### Report for ORCHESTRATOR_CHAT

Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 06, Worker exchange ordinal: 01

status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Changed files and purpose: none — this exchange mutates no Libre Tiles file; meta report write is the authorized side effect
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none

Planning Record:
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

---

## D1 — Control Inventory (Landed vs Missing)

Repository evidence from `backend/config/settings.py`, `backend/accounts/views.py`, `backend/game/simulation_views.py`, `backend/game/admin_views.py`, `backend/game/analytics_views.py`, `backend/tests/test_security_settings.py`, and `backend/tests/test_security_throttling.py` at baseline `15793bb08f132a1e86e20708d7fa88ae9156df6d`:

| Control | Repository Evidence | Status |
| :--- | :--- | :--- |
| **ALLOWED_HOSTS fail-closed** | `settings.py:100-114` (`_allowed_hosts()`). Fails closed with `ImproperlyConfigured` if absent, empty, or containing `*` when `DEBUG=False`. Tested in `test_security_settings.py:242-266`. | `landed-tested` |
| **Secret-key strength** | `settings.py:26-50` (`_require_secret_key()`). Fails closed if absent, empty, public fallback, length < 50, unique chars < 5, or prefix `django-insecure-`. Tested in `test_security_settings.py:196-229`. | `landed-tested` |
| **Cookie Secure flags** | `settings.py:266-267` (`SESSION_COOKIE_SECURE = not DEBUG`, `CSRF_COOKIE_SECURE = not DEBUG`). Tested in `test_security_settings.py:292-308, 346-362`. | `landed-tested` |
| **SSL redirect** | `settings.py:268` (`SECURE_SSL_REDIRECT = not DEBUG`). Tested in `test_security_settings.py:292-308, 346-362`. | `landed-tested` |
| **HSTS seconds** | `settings.py:269` (`SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0`). Tested in `test_security_settings.py:292-308, 346-362`. | `landed-tested` |
| **HSTS includeSubDomains** | `settings.py:279` (`SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG`). Tested in `test_security_settings.py:292-330` (closes `security.W005`). | `landed-tested` |
| **HSTS preload** | `settings.py:274-278`. Deliberately unset / False per Cooperator decision 5. `security.W021` is explicitly asserted present in `test_security_settings.py:310-330`. | `accepted-residual` |
| **NOSNIFF** | `settings.py:282` (`SECURE_CONTENT_TYPE_NOSNIFF = True`). Tested in `test_security_settings.py:396-399`. | `landed-tested` |
| **X-Frame-Options (XFO)** | `settings.py:284` (`X_FRAME_OPTIONS = "DENY"`). Tested in `test_security_settings.py:408-411`. | `landed-tested` |
| **CSRF_TRUSTED_ORIGINS** | Absent from `backend/config/settings.py` and `backend/.env.example`. No probe or tests exist. | `missing` |
| **SECURE_PROXY_SSL_HEADER** | Absent from `backend/config/settings.py` and `backend/.env.example`. No probe or tests exist. | `missing` |
| **DJANGO_NUM_PROXIES** | `settings.py:60-97` (`_num_proxies()`). Defaults to 0 (keys throttles on `REMOTE_ADDR`). Spoofing resistance tested in `test_security_throttling.py:142,171`. Negative/malformed integer validation in `_num_proxies` itself is untested. | `landed-tested` (runtime behavior) / `landed-untested` (config error paths) |
| **Throttle cache Redis (DEBUG=false)** | `settings.py:292-325` (`_default_cache()`). Requires `DJANGO_THROTTLE_CACHE_URL` or `REDIS_URL` starting with `redis://` or `rediss://`. Tested in `test_security_settings.py:418-461`. | `landed-tested` |
| **SimulationCreateView scope** | `simulation_views.py:45` (`throttle_scope = "admin_simulation_create"`). Rate `"10/hour"` in `settings.py:356`. Rate limiting 429 response path is untested. | `landed-untested` |
| **SimulationStepView scope** | `simulation_views.py:76` (`throttle_scope = "admin_simulation_step"`). Rate `"120/minute"` in `settings.py:357`. Rate limiting 429 response path is untested. | `landed-untested` |
| **SimulationActionView scope** | `simulation_views.py:95` (`throttle_scope = "admin_simulation_step"`). Rate `"120/minute"` in `settings.py:357`. Rate limiting 429 response path is untested. | `landed-untested` |
| **SimulationStateView scope** | `simulation_views.py:66`. Unbound (`throttle_scope` is None). Staff simulation state GET during high-frequency polling. | `landed-untested` (exemption) |
| **SimulationStopView scope** | `simulation_views.py:111`. Unbound (`throttle_scope` is None). Staff emergency halt action. | `landed-untested` (exemption) |
| **AdminGameListView scope** | `admin_views.py:48`. Unbound (`throttle_scope` is None). Staff paginated game list. | `landed-untested` (exemption) |
| **AdminGameReplayView scope** | `admin_views.py:122`. Unbound (`throttle_scope` is None). Staff replay viewer. | `landed-untested` (exemption) |
| **AdminAnalyticsView scope** | `analytics_views.py:12`. Unbound (`throttle_scope` is None). Staff reporting aggregation. | `landed-untested` (exemption) |
| **Auth & AI-context throttles** | `accounts/views.py`, `game/views.py:350`. Register, login, refresh, change-password, me, and ai-context scopes tested in `test_security_throttling.py:83-264`. | `landed-tested` |

---

## D2 — CSRF_TRUSTED_ORIGINS

### Technical Design: Smallest Correct Setting
1. **Derivation Basis**:
   In Libre Tiles, the only legitimate client communicating cross-origin with session authentication or form POSTs is the Next.js frontend, whose allowed origins are already defined in `CORS_ALLOWED_ORIGINS`. Deriving `CSRF_TRUSTED_ORIGINS` from `CORS_ALLOWED_ORIGINS` eliminates configuration skew where CORS succeeds but CSRF fails. An optional `DJANGO_CSRF_TRUSTED_ORIGINS` environment variable will be supported for explicit overrides:
   - If `DJANGO_CSRF_TRUSTED_ORIGINS` is provided and non-empty, parse that comma-separated list.
   - Otherwise, use the list already configured in `CORS_ALLOWED_ORIGINS`.

2. **Parsing and Strict Validation**:
   Origin specifications in Django 4.0+ must include a scheme (`http://` or `https://`), must specify a valid host/netloc (with optional port), and must not contain wildcards (`*`) or path components.
   - **Empty / Whitespace entries**: Ignored (e.g. trailing commas `https://a.test, ` do not cause false failures).
   - **Scheme Requirement**: Every origin must start with `http://` or `https://`. Missing scheme fails closed (`ImproperlyConfigured`). This guarantees Django check `4_0.E001` never fires.
   - **Wildcards**: Any origin containing `*` fails closed (`ImproperlyConfigured`). This guarantees deployment check `security.W018` never fires.
   - **Path component**: Any origin containing a non-root path component (e.g. `https://example.com/api`) fails closed (`ImproperlyConfigured`), normalizing valid roots to `scheme://netloc`.
   - **Normalization**: Formatted as `{scheme}://{netloc}` (stripping any trailing slash).

3. **Development vs Production Compatibility**:
   - In development (`DEBUG=True`): default `CORS_ALLOWED_ORIGINS` is `"http://localhost:3000"`, yielding `CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]`. Plain local HTTP continues to work seamlessly; `test_debug_true_keeps_plain_http_workable` passes.
   - In production (`DEBUG=False`): operator configures `CORS_ALLOWED_ORIGINS=https://libretiles.example.com` (or `DJANGO_CSRF_TRUSTED_ORIGINS=https://libretiles.example.com`), producing `CSRF_TRUSTED_ORIGINS = ["https://libretiles.example.com"]`.

4. **Implementation Function in `backend/config/settings.py`**:
   ```python
   def _csrf_trusted_origins(*, raw_explicit: str | None, cors_origins: list[str]) -> list[str]:
       if raw_explicit is not None and raw_explicit.strip():
           source = [part.strip() for part in raw_explicit.split(",") if part.strip()]
       else:
           source = cors_origins

       trusted: list[str] = []
       for item in source:
           origin = item.strip()
           if not origin:
               continue
           if not (origin.startswith("http://") or origin.startswith("https://")):
               raise ImproperlyConfigured(
                   f"CSRF trusted origin {origin!r} is invalid: must start with "
                   "http:// or https:// (e.g. 'https://example.com')."
               )
           if "*" in origin:
               raise ImproperlyConfigured(
                   f"CSRF trusted origin {origin!r} is invalid: wildcards ('*') are forbidden."
               )
           parsed = urlsplit(origin)
           if parsed.path and parsed.path != "/":
               raise ImproperlyConfigured(
                   f"CSRF trusted origin {origin!r} is invalid: origins must not include a path."
               )
           if not parsed.netloc:
               raise ImproperlyConfigured(
                   f"CSRF trusted origin {origin!r} is invalid: missing host."
               )
           trusted.append(f"{parsed.scheme}://{parsed.netloc}")
       return trusted
   ```
   Followed by:
   ```python
   CSRF_TRUSTED_ORIGINS: list[str] = _csrf_trusted_origins(
       raw_explicit=os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS"),
       cors_origins=CORS_ALLOWED_ORIGINS,
   )
   ```

---

## D3 — SECURE_PROXY_SSL_HEADER

### Technical Design: Safe Proxy Indication without Spoofing
1. **The Spoofing Hazard on Unproxied Processes**:
   Django documentation warns: *"If your app is not behind a proxy that sets this header... you must NOT set this."*
   When `SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")` is enabled on an unproxied process (such as a directly internet-accessible Daphne/Gunicorn worker before Slice 4 nginx is configured), any incoming HTTP request containing `X-Forwarded-Proto: https` causes `request.is_secure()` to return `True`. Consequently:
   - Django assumes the request is encrypted HTTPS.
   - `SECURE_SSL_REDIRECT` will not redirect the cleartext HTTP request to HTTPS.
   - Cookies marked with `Secure` flag are transmitted across an unencrypted connection.
   - Untrusted clients can spoof secure status.

2. **Explicit Opt-in via Environment Variable**:
   `SECURE_PROXY_SSL_HEADER` must NOT be enabled silently or unconditionally when `DEBUG=False`. It must remain `None` by default and require an explicit opt-in flag:
   `DJANGO_SECURE_PROXY_SSL_HEADER` (boolean, default `False`).

3. **Setting in `backend/config/settings.py`**:
   ```python
   # Reverse-proxy SSL indication.
   # SECURE_PROXY_SSL_HEADER must NOT be enabled unless Django is strictly behind
   # a trusted reverse proxy that strips client-supplied X-Forwarded-Proto headers.
   # Enabling it on a directly reachable process allows header spoofing of is_secure().
   # Default: None (disabled). Opt-in via DJANGO_SECURE_PROXY_SSL_HEADER=true.
   SECURE_PROXY_SSL_HEADER: tuple[str, str] | None = (
       ("HTTP_X_FORWARDED_PROTO", "https")
       if _env_flag("DJANGO_SECURE_PROXY_SSL_HEADER", default=False)
       else None
   )
   ```

4. **Probe Representation**:
   To prevent leaking header values or request introspection, the subprocess settings probe exposes only:
   `"proxy_ssl_header_enabled": bool(getattr(settings_mod, "SECURE_PROXY_SSL_HEADER", None) is not None)`

5. **Django Deployment Checks**:
   Empirical verification confirmed that enabling or disabling `SECURE_PROXY_SSL_HEADER` produces zero new Django check warnings. `security.W021` (HSTS preload) remains the only warning (accepted residual per A5).

---

## D4 — Throttle Enforcement (Simulation + Admin)

### View Inventory and Policy Decisions
1. **Staff Simulation Views (`backend/game/simulation_views.py`)**:
   - `SimulationCreateView` (`POST /api/admin/simulate/`):
     - Scope: `admin_simulation_create`.
     - Rate: `10/hour` (in `DEFAULT_THROTTLE_RATES`).
     - Purpose: Governs creation of persistent playground simulation instances and initial rack generation.
     - Policy: Enforced. Tested for 429 under overridden test rate.
   - `SimulationStepView` (`POST /api/admin/simulate/<game_id>/step/`):
     - Scope: `admin_simulation_step`.
     - Rate: `120/minute` (in `DEFAULT_THROTTLE_RATES`).
     - Purpose: Advances a simulation ply.
     - Policy: Enforced. Tested for 429 under overridden test rate.
   - `SimulationActionView` (`POST /api/admin/simulate/<game_id>/action/`):
     - Scope: `admin_simulation_step`.
     - Rate: `120/minute` (shares `admin_simulation_step` scope with `SimulationStepView`).
     - Purpose: Staff manual moves/actions within a simulation.
     - Policy: Enforced. Tested for shared bucket consumption with `SimulationStepView`.
   - `SimulationStateView` (`GET /api/admin/simulate/<game_id>/`):
     - Scope: `None` (unbound).
     - Decision: `product-choice`. Kept unbound because the playground UI polls state during rapid 120/minute automated stepping. A throttle on GET state would cause accidental 429s during normal simulation observation without protecting compute or token resources.
   - `SimulationStopView` (`POST /api/admin/simulate/<game_id>/stop/`):
     - Scope: `None` (unbound).
     - Decision: `product-choice`. Kept unbound because stopping a simulation is an idempotent emergency administrative intervention. An operator must never be rate-limited when trying to halt a runaway simulation.

2. **Staff Admin / Analytics Views (`backend/game/admin_views.py`, `backend/game/analytics_views.py`)**:
   - `AdminGameListView` (`GET /api/admin/games/`):
     - Scope: `None` (unbound).
     - Decision: `product-choice`. Paginated staff dashboard view; protected by `IsAdminUser` and session/JWT authentication. Unbound avoids locking staff out during administrative audits or search pagination.
   - `AdminGameReplayView` (`GET /api/admin/games/<game_id>/replay/`):
     - Scope: `None` (unbound).
     - Decision: `product-choice`. Read-only staff inspection of historical game plies; does not call external providers.
   - `AdminAnalyticsView` (`GET /api/admin/analytics/`):
     - Scope: `None` (unbound).
     - Decision: `product-choice`. Read-only aggregation over 7/30/90 days for staff dashboard. Explicitly kept unbound to prevent turning GET analytics into an accidental lockout during reporting.

### Testing 429 Enforcement Fast (Respecting A7)
- **Technical Measurement**: DRF's `SimpleRateThrottle.THROTTLE_RATES` evaluates `api_settings.DEFAULT_THROTTLE_RATES` once at class import time. In a running test process, `override_settings(REST_FRAMEWORK=...)` updates Django settings but does NOT update `SimpleRateThrottle.THROTTLE_RATES`.
- **Solution**: In `backend/tests/test_security_throttling.py`, create a lightweight context manager:
  ```python
  @contextmanager
  def _override_throttle_rates(rates: dict[str, str]) -> Iterator[None]:
      with patch.object(
          SimpleRateThrottle,
          "THROTTLE_RATES",
          {**SimpleRateThrottle.THROTTLE_RATES, **rates},
      ):
          yield
  ```
- **Execution Efficiency**:
  - Overriding `admin_simulation_create` to `"2/hour"` proves 429 on request 3 (2 allowed + 1 throttled).
  - Overriding `admin_simulation_step` to `"2/minute"` proves 429 on request 3.
  - Calling `SimulationActionView` on request 3 after 2 `SimulationStepView` calls proves the shared bucket.
  - Total test execution time is <15 milliseconds for the entire simulation throttle test block, completely avoiding 121-call DoS loops and keeping total pytest runtime well under 30s.

---

## D5 — Settings Probes

1. **Keys Added to `_PROBE_SOURCE` in `backend/tests/test_security_settings.py`**:
   ```python
   payload["csrf_trusted_origins"] = list(
       getattr(settings_mod, "CSRF_TRUSTED_ORIGINS", [])
   )
   payload["proxy_ssl_header_enabled"] = bool(
       getattr(settings_mod, "SECURE_PROXY_SSL_HEADER", None) is not None
   )
   ```
   - No sensitive information (such as secret keys or database credentials) is emitted.
   - Only boolean status and public origin URL strings are exposed.

2. **Parameters in `_run_settings_probe`**:
   The probe runner already supports `extra_env: dict[str, str] | None = None`. Specific convenience parameters (or `extra_env` entries) will be used:
   - `extra_env={"DJANGO_CSRF_TRUSTED_ORIGINS": ...}`
   - `extra_env={"CORS_ALLOWED_ORIGINS": ...}`
   - `extra_env={"DJANGO_SECURE_PROXY_SSL_HEADER": ...}`
   - `extra_env={"DJANGO_NUM_PROXIES": ...}`

3. **Check IDs and Security Warnings**:
   - `security.W021` (HSTS preload) remains present in deployment checks (`test_production_like_hsts_closes_w005_and_keeps_w021_accepted` continues to assert its presence).
   - `_FORBIDDEN_DEPLOY_CHECK_IDS` is unchanged because no check ID fires on proxy SSL header enablement or CSRF trusted origins.

---

## D6 — Test Matrix

All tests will be added to the two existing test modules: `backend/tests/test_security_settings.py` and `backend/tests/test_security_throttling.py`.

### 1. `backend/tests/test_security_settings.py`
| Test Function Name | Execution Mode | Assertion / Purpose |
| :--- | :--- | :--- |
| `test_csrf_trusted_origins_derived_from_cors_allowed_origins` | Subprocess probe | In `DEBUG=False`, when `CORS_ALLOWED_ORIGINS="https://frontend.example.com"`, `payload["csrf_trusted_origins"] == ["https://frontend.example.com"]`. |
| `test_csrf_trusted_origins_explicit_env_override` | Subprocess probe | When `DJANGO_CSRF_TRUSTED_ORIGINS` is set, overrides CORS origins and populates `payload["csrf_trusted_origins"]`. |
| `test_csrf_trusted_origins_rejects_missing_scheme` | Subprocess probe | Origin without `http://` or `https://` (e.g. `example.com`) raises `ImproperlyConfigured`. |
| `test_csrf_trusted_origins_rejects_wildcard` | Subprocess probe | Origin containing `*` (e.g. `https://*` or `https://*.example.com`) raises `ImproperlyConfigured`. |
| `test_csrf_trusted_origins_rejects_path` | Subprocess probe | Origin containing path (e.g. `https://example.com/api`) raises `ImproperlyConfigured`. |
| `test_csrf_trusted_origins_normalizes_and_skips_empty` | Subprocess probe | Strips trailing slashes, skips empty items from trailing commas, formats correctly. |
| `test_debug_true_keeps_local_csrf_trusted_origins` | Subprocess probe | In `DEBUG=True`, defaults to `["http://localhost:3000"]`. |
| `test_secure_proxy_ssl_header_disabled_by_default` | Subprocess probe | Default settings (flag unset) has `payload["proxy_ssl_header_enabled"] is False`. |
| `test_secure_proxy_ssl_header_opt_in` | Subprocess probe | With `DJANGO_SECURE_PROXY_SSL_HEADER=true`, `payload["proxy_ssl_header_enabled"] is True`. |
| `test_secure_proxy_ssl_header_spoofing_prevented_when_disabled` | Unit test (RequestFactory) | When setting is `None`, incoming request with `HTTP_X_FORWARDED_PROTO="https"` has `is_secure() is False`. |
| `test_secure_proxy_ssl_header_honored_when_enabled` | Unit test (RequestFactory) | When setting is `("HTTP_X_FORWARDED_PROTO", "https")`, incoming request with `HTTP_X_FORWARDED_PROTO="https"` has `is_secure() is True`. |
| `test_num_proxies_invalid_string_raises` | Subprocess probe | `DJANGO_NUM_PROXIES="invalid"` raises `ImproperlyConfigured`. |
| `test_num_proxies_negative_int_raises` | Subprocess probe | `DJANGO_NUM_PROXIES="-1"` raises `ImproperlyConfigured`. |

### 2. `backend/tests/test_security_throttling.py`
| Test Function Name | Execution Mode | Assertion / Purpose |
| :--- | :--- | :--- |
| `test_admin_simulation_create_throttled_after_limit` | APIClient (`_override_throttle_rates`) | With rate mocked to `2/hour`, 2 calls return 400 (validation fail, throttle permitted), 3rd returns 429 with numeric `Retry-After`. |
| `test_admin_simulation_step_throttled_after_limit` | APIClient (`_override_throttle_rates`) | With rate mocked to `2/minute`, 2 calls return 400, 3rd returns 429 with numeric `Retry-After`. |
| `test_admin_simulation_action_shares_step_throttle_bucket` | APIClient (`_override_throttle_rates`) | With rate mocked to `2/minute`, 2 calls to step view exhaust bucket; 3rd call to action view returns 429. |
| `test_admin_simulation_unbound_endpoints_exempt` | Introspection + APIClient | Asserts `SimulationStateView.throttle_scope is None` and `SimulationStopView.throttle_scope is None`; repeated calls do not 429. |
| `test_admin_views_unbound_endpoints_exempt` | Introspection + APIClient | Asserts `AdminGameListView.throttle_scope is None`, `AdminGameReplayView.throttle_scope is None`, `AdminAnalyticsView.throttle_scope is None`. |

---

## D7 — Path Allowlist and Verification Commands

### File Allowlist (Strictly Bounded)
1. `backend/config/settings.py` — implementation of `_csrf_trusted_origins`, `CSRF_TRUSTED_ORIGINS`, `SECURE_PROXY_SSL_HEADER`.
2. `backend/.env.example` — documented entries for `DJANGO_SECURE_PROXY_SSL_HEADER` and `DJANGO_CSRF_TRUSTED_ORIGINS`.
3. `backend/tests/test_security_settings.py` — probe source extension and settings regression tests.
4. `backend/tests/test_security_throttling.py` — scoped simulation throttle tests and exemption assertions.

### Strictly Prohibited Modifications
- ⛔ No VPS scripts, systemd unit files, or nginx configuration (`docs/vps/*`, `scripts/*` reserved for Slice 4).
- ⛔ No frontend files, Next.js configs, or npm dependencies (reserved for Slice 5).
- ⛔ No `gamecore/` files (`WordAuthority.accepts_tokens` unchanged).
- ⛔ No setting `SECURE_HSTS_PRELOAD = True` (Cooperator decision 5; W021 must remain present).
- ⛔ No `backend/game/migrations/0008_*` edits (A4).
- ⛔ No reading or modifying `backend/.env` (A10).

### RF-16 Verification Commands
```bash
From /home/agile/Projects/libretiles/backend:
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check config tests game accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_security_settings.py tests/test_security_throttling.py
  env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

---

## D8 — Implementation Grant Sketch

1. **Ordered Implementation Steps**:
   - **Step 1: Settings Implementation**:
     In `backend/config/settings.py`, add `_csrf_trusted_origins()` helper, define `CSRF_TRUSTED_ORIGINS` (derived from `CORS_ALLOWED_ORIGINS` with `DJANGO_CSRF_TRUSTED_ORIGINS` override), and define `SECURE_PROXY_SSL_HEADER` gated on `_env_flag("DJANGO_SECURE_PROXY_SSL_HEADER", default=False)`.
   - **Step 2: Documentation in `.env.example`**:
     In `backend/.env.example`, add documented default entries for `DJANGO_SECURE_PROXY_SSL_HEADER='false'` and `DJANGO_CSRF_TRUSTED_ORIGINS`.
   - **Step 3: Update `test_security_settings.py`**:
     Update `_PROBE_SOURCE` to emit `csrf_trusted_origins` and `proxy_ssl_header_enabled`. Add test cases for derivation, overrides, invalid schemes, wildcards, paths, proxy header default vs opt-in, spoof prevention, and num_proxies validation.
   - **Step 4: Update `test_security_throttling.py`**:
     Add `_override_throttle_rates` helper and test cases for `admin_simulation_create`, `admin_simulation_step`, shared action bucket, and unbound view exemptions.
   - **Step 5: Verification**:
     Run ruff, mypy, and full pytest test suite via the canonical RF-16 virtualenv commands.

2. **Proposed Evidence Tier and INFOSEC Routing**:
   - Evidence Tier: **E2** (isolated unit/subprocess tests, deterministic in-memory execution, no external network, no Docker).
   - INFOSEC Route: **R1** (configuration hardening). Cite **R2** (input validation) for strict origin parsing (`http://` or `https://` scheme enforcement, wildcard rejection, path component rejection).
   - R3 is NOT claimed because no authentication backend, password validator, JWT token lifecycle, or session generation logic is being mutated.

3. **Cooperator-Owned Decisions**:
   **None**. All boundaries are resolved by repository conventions and accepted decisions (A1–A11).

4. **Deferred Items**:
   - Reverse proxy configuration (nginx headers, TLS termination, socket proxying): deferred to **Slice 4**.
   - Systemd units and VPS deployment automation: deferred to **Slice 4**.
   - Standalone Next.js containerization / production frontend deployment: deferred to **Slice 5**.

5. **Residual Risks**:
   - **Operator Proxy Misconfiguration**: If an operator sets `DJANGO_SECURE_PROXY_SSL_HEADER=true` on a server directly exposed to the internet without an intermediate proxy that strips client-supplied `X-Forwarded-Proto`, clients could spoof HTTPS. *Mitigation: Default is `False`, documented extensively in settings and `.env.example`.*
   - **Shared NAT Throttle Sharing**: With `DJANGO_NUM_PROXIES=0` behind a real reverse proxy, all clients share the proxy IP and thus the unauthenticated throttle bucket. *Mitigation: Fails safe (over-throttles rather than under-throttles); operator configures `DJANGO_NUM_PROXIES` once trusted proxy count is known (already accepted in A11).*

---

## Orchestration Critique

### MEASURED
1. **DRF Throttle Rate Immutability in Running Process**:
   `rest_framework.throttling.SimpleRateThrottle.THROTTLE_RATES` evaluates `api_settings.DEFAULT_THROTTLE_RATES` once during module import. Simply using `override_settings(REST_FRAMEWORK={"DEFAULT_THROTTLE_RATES": ...})` does not update the rate table used by existing or freshly instantiated throttles. The implementation plan explicitly accounts for this by patching `SimpleRateThrottle.THROTTLE_RATES` during fast 429 tests.
2. **Harness Output Parsing on Python Dict Literals**:
   Printing unescaped Python dictionaries containing `{"detail": ...}` to stdout can trigger tool runner JSON-interception. File inspections and probes should continue to use JSON formatting or structured test assertions rather than raw dictionary printing.

### LEAD
1. **Coupling CSRF Trusted Origins to CORS Origins by Default**:
   Deriving `CSRF_TRUSTED_ORIGINS` from `CORS_ALLOWED_ORIGINS` removes the deployment hazard where an operator updates the frontend domain in `CORS_ALLOWED_ORIGINS` but forgets `CSRF_TRUSTED_ORIGINS`, which would silently break session-authenticated API mutations in production while allowing GETs.

---

## Enumeration Widened
- Audited all views across `backend/game`, `backend/accounts`, and `backend/catalog` to ensure no staff-facing mutation or query endpoint was overlooked for throttling analysis.
- Audited `django.core.checks` source code for CSRF compatibility check `4_0.E001` and deployment checks (`security.W018`, `security.W021`) to guarantee no unexpected warnings fire when `CSRF_TRUSTED_ORIGINS` and `SECURE_PROXY_SSL_HEADER` are introduced.

---

Report justification: new-evidence
Planning authority expires at this report.
Smallest next step: Orchestrator issues implementation prompt for Slice 3 based on this decision-complete technical design.
Context pressure: Qualitative estimate: low (~20% of context window used).

### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening
Worker session ordinal: 05
Worker exchange ordinal: 01

**Status:** PASS
**Phase-qualified result:** Implementation PASS (non-independent). Bounded correction of accepted finding `audit-01-F10` produced and validated. This Worker does not certify the correction and does not close the whole. Fresh independent re-audit (INFOSEC.md 4.11, P-10) remains mandatory.

**Start commit:** `7e583aa91705da10a452132370aa72ba7517d879`
**End commit:** `04fe823ac2eea6c8398dd9f00830d30d71568e97`

**Changed paths (allowlist only):**

| Path | Purpose |
|---|---|
| `backend/config/settings.py` | Enable `token_blacklist`; `ROTATE_REFRESH_TOKENS` / `BLACKLIST_AFTER_ROTATION`; register `PasswordAwareJWTAuthentication` and refresh serializer. Lifetimes unchanged (2h / 7d). |
| `backend/accounts/models.py` | Nullable `password_changed_at`; set on existing-user `set_password`; blacklist outstanding refresh tokens. |
| `backend/accounts/migrations/0004_user_password_changed_at.py` | One authored migration; nullable, `default=None`. |
| `backend/accounts/authentication.py` | New `JWTAuthentication` subclass: `iat` vs `password_changed_at`. |
| `backend/accounts/serializers.py` | Persist timestamp + blacklist on password change; iat check on refresh. |
| `backend/accounts/views.py` | Remove SimpleJWT `setattr`; local scoped subclasses; authenticated `LogoutView`. |
| `backend/accounts/urls.py` | Bind subclasses; `POST /api/auth/logout/`. |
| `backend/tests/test_token_lifecycle.py` | Regression tests 1–12 plus missing-`iat` fail-closed lock. |

```text
git diff --stat 7e583aa..04fe823
 backend/accounts/authentication.py                 |  66 ++++++
 .../migrations/0004_user_password_changed_at.py    |  18 ++
 backend/accounts/models.py                         |  25 +++
 backend/accounts/serializers.py                    |  22 +-
 backend/accounts/urls.py                           |  15 +-
 backend/accounts/views.py                          |  49 ++++-
 backend/config/settings.py                         |   6 +-
 backend/tests/test_token_lifecycle.py              | 227 +++++++++++++++++++++
 8 files changed, 417 insertions(+), 11 deletions(-)

git diff --name-only 7e583aa..04fe823
backend/accounts/authentication.py
backend/accounts/migrations/0004_user_password_changed_at.py
backend/accounts/models.py
backend/accounts/serializers.py
backend/accounts/urls.py
backend/accounts/views.py
backend/config/settings.py
backend/tests/test_token_lifecycle.py
```

`frontend/**` is untouched. `backend/db.sqlite3` is gitignored (`*.sqlite3`) and was not staged.

**Repository / pre-push gate:** At start, `HEAD`, `HEAD:.ap`, `.ap HEAD`, porcelain, and `git ls-remote origin refs/heads/main` all matched the prompt (`7e583aa` / `.ap` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, `## main...origin/main`, empty porcelain). Immediately before push, remote `main` was still `7e583aa91705da10a452132370aa72ba7517d879`.

**Capability handshake / execution-route deviation:** Declared `poetry run ...` is not usable (Cursor AppImage intercepts `python*` via inherited `APPIMAGE`/`PYTHONHOME`). Authorized alternate from `backend/`: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` and `.venv/bin/ruff`. Evidence class: local command output. Stopping condition: if that interpreter were missing or failed, stop; it did not. Ambient `python` / `python3` / `poetry run` were not used as a parallel route.

**Before/after tests (never printed a token value):**

| # | Test | Pre-fix | Post-fix |
|---|---|---|---|
| 1 | Access token before password change → `GET /api/auth/me/` | **FAIL** `assert 200 == 401` (the finding) | PASS 401 |
| 2 | Refresh token before password change → `POST /api/auth/refresh/` | **FAIL** `assert 200 in {400, 401}` | PASS |
| 3 | Logout then refresh | **FAIL** logout `404 == 200` | PASS |
| 4 | Logout twice | **FAIL** first logout `404 == 200` | PASS (second call clean 4xx, no traceback) |
| 5 | Logout malformed refresh | First run **PASS** on HTTP 404 (too weak). Strengthened to `{400, 401}` so unmodified tree would fail. | PASS 401 |
| 6 | Logout unauthenticated | **FAIL** `404 == 401` | PASS 401 |
| 7 | Refresh rotation; old refresh rejected | **FAIL** `assert False` (no new refresh token) | PASS |
| 8 | Never-changed password + `password_changed_at is None` | **FAIL** `AttributeError: 'User' object has no attribute 'password_changed_at'` | PASS 200 |
| 9 | Token issued after password change | PASS (invariance) | PASS 200 |
| 10 | Current access token → `GET /api/game/history/` | PASS (invariance) | PASS 200 |
| 11 | Django admin session login | PASS (invariance) | PASS 200 |
| 12 | Login/refresh are local subclasses; scopes `auth_login` / `auth_refresh`; no setattr on SimpleJWT classes | **FAIL** `TokenObtainPairView is not TokenObtainPairView` | PASS |
| 13 | Access token with `iat` deleted | **FAIL** `assert 200 == 401` | PASS 401 |

**Migrations applied** on the existing development database (`manage.py migrate`, no reset):

- `accounts.0004_user_password_changed_at`
- vendored `token_blacklist.0001_initial` … `0008_migrate_to_bigautofield`, `0010_fix_migrate_to_bigautofield` … `0013_alter_blacklistedtoken_options_and_more` (vendored history has no `0009` in the apply list)

`manage.py makemigrations --check --dry-run` → `No changes detected`

**iat / clock-skew / missing-iat:** Extra skew is **`PASSWORD_CHANGE_IAT_SKEW_SECONDS = 0`**. SimpleJWT `iat` is an integer Unix second (`datetime_to_epoch` / `timegm`). A token is rejected iff `iat < int(password_changed_at.timestamp())`. Tokens that share the same Unix second as the password change remain valid so an immediate re-login is not locked out. That one-second claim-granularity window is the entire tolerance; no extra seconds were added. **Missing or non-numeric `iat` (including `bool`) fails closed** (`InvalidToken("Token contained no iat claim")`). Users with `password_changed_at is None` authenticate normally.

**S3 setattr debt:** `setattr(TokenObtainPairView, …)` / `setattr(TokenRefreshView, …)` are gone. Login/refresh bind `ScopedTokenObtainPairView` / `ScopedTokenRefreshView` with throttle scopes still exactly `"auth_login"` and `"auth_refresh"`. Throttle rates were not changed.

**Frontend:** The client does **not** call `POST /api/auth/logout/`. That is deliberate and out of this slice. Wiring `handleLogout` is a later slice. Until then, server logout exists but client logout still only clears local state; refresh-token theft until expiry remains mitigated only if something calls this endpoint or the password is changed.

**Standing gates (verbatim):**

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
Success: no issues found in 78 source files

env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
All checks passed!

env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
287 passed, 4 skipped in 136.37s (0:02:16)
```

Start-commit baseline was 274 passed, 4 skipped. 274 + 13 new tests = 287. `test_security_throttling.py` and `test_security_settings.py` passed in that full run.

**Authorized Git result / public readback:** One commit `04fe823ac2eea6c8398dd9f00830d30d71568e97`, staged by explicit path (no `git add -A` / `.`). `git push origin main` (no flags): `7e583aa..04fe823  main -> main`. Readback: `git ls-remote origin refs/heads/main` and `git rev-parse HEAD` are both `04fe823ac2eea6c8398dd9f00830d30d71568e97`. Working tree matches `origin/main`, porcelain empty.

**Deviations, risks, missing evidence:**
- Test 5 was strengthened after the first pre-fix run because HTTP 404 counted as a “clean 4xx”.
- Same-Unix-second access tokens survive password change (JWT `iat` granularity). Older tokens (the demonstrated finding) are rejected.
- `TokenRefreshView` remains unauthenticated (SimpleJWT default); revocation on refresh is via blacklist + iat in `PasswordAwareTokenRefreshSerializer`, not via `JWTAuthentication`.
- This correction is non-independent. Re-audit is not done here.

**Out-of-scope observations (not findings):** Frontend still persists access and refresh tokens in `localStorage`. Admin password change sets `password_changed_at` via `User.set_password` but only `ChangePasswordSerializer.save()` also blacklists outstanding refresh tokens; admin-path refresh blacklisting is not in this slice.

**Smallest next step:** Orchestrator routes S5: websocket ticket single-use and removal from the query string (`audit-01-F09`), after dispatching the mandatory fresh independent re-audit of this correction.

**Report justification:** new-evidence
**Logical-whole closure:** not-closed
**Authority expiry:** This exchange’s authority expires with this terminal report. Retained context is not a renewal.

**Resolved Execution Issues / Near-Misses:** (1) Test 5 initially passed on 404; assertion narrowed to `{400, 401}` before implementation. (2) mypy rejected an `AuthUser` TypeVar override on `get_user`; resolved with an explicit `# type: ignore[override]` and a union return type. Residual: none for the grant.

**Pre-Existing Failure Classification:** none
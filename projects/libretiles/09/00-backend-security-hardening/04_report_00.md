### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening
Worker session ordinal: 04
Worker exchange ordinal: 01

**Status:** PASS
**Phase-qualified result:** Implementation PASS (non-independent; corrector does not certify and does not close)

**Start commit:** `fdfe4a67e8598c3580fb1219a224b22615d99f7a`
**End commit:** `7e583aa91705da10a452132370aa72ba7517d879`

**Changed paths (purpose):**
- `backend/config/settings.py` — four Django password validators; explicit LocMemCache; ScopedRateThrottle + rates
- `backend/accounts/serializers.py` — register `min_length=8` and `validate_password`
- `backend/accounts/views.py` — `throttle_scope` on register/me/change-password; setattr scopes on SimpleJWT login/refresh (URLconf not on allowlist)
- `backend/game/views.py` — `throttle_scope` on `AIContextView`
- `backend/tests/test_security_throttling.py` — new regression tests 1–13
- `backend/tests/test_security_settings.py` — test 14 (four validators)

`git diff --name-only fdfe4a67e8598c3580fb1219a224b22615d99f7a HEAD`:

```text
backend/accounts/serializers.py
backend/accounts/views.py
backend/config/settings.py
backend/game/views.py
backend/tests/test_security_settings.py
backend/tests/test_security_throttling.py
```

`git diff --stat fdfe4a67e8598c3580fb1219a224b22615d99f7a HEAD`:

```text
 backend/accounts/serializers.py           |  16 +-
 backend/accounts/views.py                 |   9 +
 backend/config/settings.py                |  23 +++
 backend/game/views.py                     |   1 +
 backend/tests/test_security_settings.py   |  10 ++
 backend/tests/test_security_throttling.py | 287 ++++++++++++++++++++++++++++++
 6 files changed, 345 insertions(+), 1 deletion(-)
```

Allowlist held. `frontend/**` is untouched.

**Repository gate (before mutation):**
- `git rev-parse HEAD` → `fdfe4a67e8598c3580fb1219a224b22615d99f7a`
- `git rev-parse HEAD:.ap` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `git -C .ap rev-parse HEAD` → `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `git status -sb` → `## main...origin/main`
- `git status --porcelain=v1` → empty
- `git ls-remote origin refs/heads/main` → `fdfe4a67e8598c3580fb1219a224b22615d99f7a`

**Pre-push gate:** `git ls-remote origin refs/heads/main` still `fdfe4a67e8598c3580fb1219a224b22615d99f7a` immediately before `git push origin main`.

**Capability handshake:**
- Requested reasoning: High. Native planning mode: not-used.
- Model identity: not independently attested.
- Declared AGENTS.md route (`poetry run …`) is not usable here: Cursor AppImage intercepts `python*` via inherited `APPIMAGE`/`PYTHONHOME`.
- Authorized bounded deviation used from `backend/`: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy|pytest|ruff`. Ambient `python`/`python3`/`poetry run` were not presented as a parallel route.
- No `.env` read, no provider call, no `LIBRETILES_AI_PLAY_LIVE`.

**Throttle rates and normal-play arithmetic:**

| Scope | Rate | Endpoints |
|---|---|---|
| `auth_register` | 10/hour | POST `/api/auth/register/` |
| `auth_login` | 10/hour | POST `/api/auth/login/` |
| `auth_refresh` | 60/hour | POST `/api/auth/refresh/` |
| `auth_change_password` | 5/hour | POST `/api/auth/change-password/` |
| `auth_me` | 200/hour | GET (and PATCH) `/api/auth/me/` |
| `ai_context` | 200/hour | GET `/api/game/<id>/ai-context/` |

Slovak games run ~29 plies. One AI turn may call ai-context once per fallback lane (`MAX_FALLBACK_ATTEMPTS = 3`). Conservatively treating every ply as an AI turn: 29 × 3 = **87** reads in one pathological full game. Rate **200/hour** leaves **113** spare reads (130% headroom). Two such games: 174 < 200. A typical human-vs-AI game is ~15 AI turns × 3 = 45. `/api/auth/me/` at 200/hour allows ~66 full three-attempt judge invocations in an hour, which is the judge path’s pre-provider gate.

**Cache backend:** explicit `django.core.cache.backends.locmem.LocMemCache` (`LOCATION=libretiles-default`). This is **per-process, not shared**. In a multi-worker deployment each worker has its own counter, so the effective budget is approximately `workers × configured rate`. This is not a cluster-wide brake.

**`/admin/login/` remains unbraked** after this change. DRF scoped throttles do not cover the Django admin form. That remainder is **orch-01-F20** and was out of this slice.

**audit-01-F13 was deliberately not changed** (Cooperator decision: duplicate-username registration error stays explicit). Login error detail was not touched; unknown-user vs wrong-password identity is unchanged.

**Tests 1–14 before/after** (pre-fix run on unmodified tree: `12 failed, 2 passed in 7.95s`):

| # | Test | Pre-fix | Post-fix |
|---|---|---|---|
| 1 | register past limit → 429 | FAIL `201 == 429` | PASS |
| 2 | login past limit → 429 | FAIL `401 == 429` | PASS |
| 3 | refresh past limit → 429 | FAIL `401 == 429` | PASS |
| 4 | change-password past limit → 429 | FAIL `400 == 429` | PASS |
| 5 | me past limit → 429 | FAIL `200 == 429` | PASS |
| 6 | ai-context past limit → 429 | FAIL `200 == 429` | PASS |
| 7 | 87 ai-context reads not throttled | PASS (guard; no brake yet) | PASS |
| 8 | user A exhaust does not throttle B | FAIL `200 == 429` | PASS |
| 9 | 6-char register → 400 | FAIL `201 == 400` | PASS |
| 10 | common password → 400 | FAIL `201 == 400` | PASS |
| 11 | similar-to-username → 400 | FAIL `201 == 400` | PASS |
| 12 | all-numeric → 400 | FAIL `201 == 400` | PASS |
| 13 | strong password → 201 | PASS (already accepted) | PASS |
| 14 | four AUTH_PASSWORD_VALIDATORS | FAIL set inclusion | PASS |

Tests 7 and 13 passed before the fix; they do not lock the missing control. Tests 1–6, 8–12, and 14 failed before and passed after.

**Standing gates (verbatim):**
- mypy `config game gamecore accounts catalog` → `Success: no issues found in 76 source files`
- ruff check . → `All checks passed!`
- pytest → `274 passed, 4 skipped in 130.69s (0:02:10)` (260 + 14 new; 4 skipped unchanged)

**Authorized Git result:** one commit `7e583aa91705da10a452132370aa72ba7517d879` on `main`; `git push origin main` (no flags); public readback: local HEAD and `origin/refs/heads/main` are both `7e583aa91705da10a452132370aa72ba7517d879`. Working tree clean (`## main...origin/main`).

**Deviations:** SimpleJWT login/refresh scopes attached with `setattr` in `accounts/views.py` because `backend/accounts/urls.py` is not on the allowlist. Relies on URLconf importing `accounts.views` (it does). No new dependency.

**Risks / missing evidence:** LocMemCache is per-process (stated above). 200/hour still permits 200 pre-provider Django calls per user per worker per hour; it is a brake, not a spend cap. This Worker does not re-audit and does not claim `verified-closed`. Fresh independent re-audit (INFOSEC.md 4.11, P-10) remains mandatory.

**Out-of-scope observations (not findings):** Django admin login is still uncovered (orch-01-F20). Duplicate-username wording is unchanged by instruction.

**Smallest next step:** Orchestrator routes S4 (token lifecycle and websocket tickets) and a fresh independent re-audit of audit-01-F03, audit-01-F11, and audit-01-F12 against commit `7e583aa91705da10a452132370aa72ba7517d879`.

**Report justification:** new-evidence
**Logical-whole closure:** not-closed

**Authority expiry:** this exchange’s authority expires with this terminal report. Retained context is not a renewal.

**Resolved Execution Issues / Near-Misses:** none

**Pre-Existing Failure Classification:** none
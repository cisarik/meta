### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 08, Worker exchange ordinal: 01

**Status: PASS.** Bounded correction for APMC-S4-IA-F01, F02, and F03 landed, gated, and pushed. No self-certification of the independent re-audit.

**Phase-qualified result:** `implementation-PASS`

**Start commit:** `0ffaf46023018c5f9b33faaef41c64b857e2aa55`  
**End commit:** `f6c9db913450d56ade4399ec5d2e6a3cd807e347`  
**AP pin:** `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (unchanged)

**Changed files**
- `backend/game/services.py` — collision fail-closed in `ensure_diagnostic_service_user`; new `_reject_service_account_user`; `create_game` and `join_human_queue` entry guards
- `backend/game/migrations/0009_diagnostic_session_foundation.py` — ownership-aware reverse
- `backend/tests/test_diagnostic_session.py` — F-L..F-P

**Error type and API mapping**

Chose `django.core.exceptions.ImproperlyConfigured` for F01 and the F02 guard.

Rationale: it is this codebase’s established settings/configuration error type (`config/settings.py`); it is not a new class (mandatory reading); it fails **loud** for operators (migrate / `ensure_diagnostic_service_user`). A `RuntimeError` subclass was rejected because it would invent a class. `DiagnosticSessionError` was rejected because it is neither a settings/configuration type nor a `RuntimeError` subclass.

F02 uses the **same** type. `create_game` and `join_human_queue` do not raise today; they return `{"ok": False, "error": ...}`. The guard raises `ImproperlyConfigured`; those two entries catch **only** that type and convert it to that established payload. Views were not edited.

Mapping (existing, unchanged):
- `CreateGameView`: `HTTP 201` if `result.get("ok", True)` else **400**
- `QueueJoinView`: `200` if `result.get("ok", True)` else **400**

Post-fix API code for F-N/F-O: **400**.

`set_unusable_password` remains only on the **created** branch. A usable-password claimant is never adopted and never stripped.

**Tests and validation — F-L..F-P**

Fail-before (pre-fix HEAD `0ffaf46`, tests only): `4 failed, 1 passed in 2.43s`  
Post-fix: `5 passed in 2.58s`

| ID | Pre-fix (verbatim) | Post-fix |
|---|---|---|
| F-L | `AssertionError: ImproperlyConfigured not raised` | raises `ImproperlyConfigured`; claimant password intact (`check_password("claimant-pass-123")`) |
| F-M | passed (already idempotent) | passed: two `ensure` calls, unusable password, staff/superuser false, active, no groups/permissions, no raise |
| F-N | `assert 400 <= 201` (HTTP **201**/ok) | HTTP **400**; `ok: false`; no new product session |
| F-O | `assert 400 <= 200` (joined) | HTTP **400**; `ok: false`; `waiting`/`matched` not true; no `vs_human` row |
| F-P | `assert False` — `User.objects.filter(pk=claimant_id).exists()` after reverse (claimant **deleted**) | reverse **keeps** usable-password claimant; reverse **deletes** unusable managed account |

**Gate summaries (verbatim)**

```text
Success: no issues found in 89 source files
```

```text
All checks passed!
```

```text
867 passed, 4 skipped in 544.57s
```

Baseline at `0ffaf46` was `862 passed, 4 skipped`. Added five tests; no removals; skip count unchanged.

**Throwaway-DB migration round-trip** (dotenv disabled; synthetic secret; `DJANGO_DEBUG=true`; SQLite `NAME` patched to `/tmp/apmc-s4-correct-xctz9lk3.sqlite3`; not the dev DB). Cleanup: file removed (`CLEANUP_EXISTS=False`).

```text
FORWARD_MANAGED id=1 usable=False staff=False superuser=False
REVERSE_MANAGED_EXISTS=False
REFORWARD_MANAGED id=2 usable=False
CLAIMANT_BEFORE_REVERSE usable=True id=2
REVERSE_CLAIMANT_EXISTS=True
REVERSE_CLAIMANT_USABLE=True
REVERSE_CLAIMANT_CHECK=True
REFORWARD_WITH_CLAIMANT=ImproperlyConfigured
REFORWARD_WITH_CLAIMANT_MSG=Reserved diagnostic username 'libretiles-diagnostic' is held by a pre-existing account with a usable password. Rename or remove that claimant, then re-run ensure_diagnostic_service_user or migrate. Refusing to adopt or disable the account.
```

**Commit and push**

- Subject: `fix(game) fail-closed reserved diagnostic service identity`
- SHA: `f6c9db913450d56ade4399ec5d2e6a3cd807e347`
- Pre-push `git ls-remote origin refs/heads/main`: `0ffaf46023018c5f9b33faaef41c64b857e2aa55`
- Push: `0ffaf46..f6c9db9  main -> main`
- Readback pair (equal): local `f6c9db913450d56ade4399ec5d2e6a3cd807e347` / remote `f6c9db913450d56ade4399ec5d2e6a3cd807e347	refs/heads/main`
- Porcelain after push: empty

**Deviations, risks, missing evidence**

- Reverse uses `is_password_usable(user.password)` instead of `user.has_usable_password()` because historical migration models do not carry `AbstractBaseUser.has_usable_password`. Same predicate; documented on the reverse. Accepted residual from the prompt is recorded on that reverse: dropping `is_diagnostic` on rollback; `is_diagnostic=True` rows re-forward as stored.
- F02 4xx without `views.py`: conversion at the two service entries, not a view change.
- Out of this allowlist (still residual from the auditor’s broader F01 direction): profile username mutation (`accounts/**` forbidden); queue-cancel was not guarded (join is now refused, so a new waiting row cannot be created).
- No independent re-audit in this session.

**One smallest next step:** route session 09 fresh independent re-audit of `f6c9db913450d56ade4399ec5d2e6a3cd807e347` against F01–F03. This Worker does not start it.

**Report justification:** `new-mutation`

**Authority expiry:** This correction authority ends with this report. No re-audit, no Meta archival, no further mutation, and no logical-whole closure are authorized or asserted.

Resolved Execution Issues / Near-Misses: Catching `ImproperlyConfigured` at `create_game` / `join_human_queue` would also turn a nested real settings failure on those paths into HTTP 400. Measured: those two functions raise that type only from `_reject_service_account_user`. `ensure_diagnostic_service_user` does not catch; migrate stays loud.

Pre-Existing Failure Classification: none. Fail-before F-L/F-N/F-O/F-P are the accepted findings, not pre-existing gate failures. F-M already passed on `0ffaf46`.

Orchestration critique: **MEASURED:** fail-closed collision does **not** break the pytest/migration path on an empty user table (0009 still seeds the managed account; F-M and the first throwaway re-forward succeeded). It **does** abort `migrate` re-forward when a usable-password claimant occupies `libretiles-diagnostic` (`ImproperlyConfigured` during 0009 `RunPython`). That is the intended loud operator stop, not a silent lockout of diagnostics on a clean database. **LEAD:** session 09 should treat “re-forward with claimant” as required fail-closed evidence, not as a CI regression. The prompt’s F01 type list and “do not invent a new class” / 4xx-without-`views.py` constraints are jointly satisfiable only by converting the raised type onto the existing `ok: False` payload at the two service entries.

Enumeration widened: production callers of `create_game` / `join_human_queue` remain only `CreateGameView` and `QueueJoinView` (plus tests). No other queue-join service entry. No other migration reverse deletes a user by username; catalog `0004`/`0005` delete prompts by name under a different ownership rule. `cancel_human_queue` is unguarded. Writable profile username remains an `accounts/**` residual outside this grant.
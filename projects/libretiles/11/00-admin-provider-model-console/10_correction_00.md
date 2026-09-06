You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded correction task and stop. ⛔ You have NO audit authority and NO self-certification authority. A fresh independent re-audit (session 11) will verify this correction.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: APMC-S4-CORRECT-2 — surviving F02 rename bypass: give the managed diagnostic identity a DURABLE flag (`is_service_account`) so participation restrictions survive profile renaming; block the flagged account's rename; switch the guards to the flag.
Accepted finding IDs: APMC-S4-IA-F02 (as re-confirmed by re-audit session 09; F01/F03 verified-closed — do not reopen them)
Audit trail: session 07 original audit (F01/F02/F03) · session 08 correction (username guards, f6c9db9) · session 09 re-audit (R-F01/R-F03 verified-closed; R-F02 NOT accepted: rename 200 → create 201 → matchmaking 200 with the same service JWT)
Re-audit routing: REQUIRED fresh independent re-audit (session 11)
Phase: implementation
Exact baseline: f6c9db913450d56ade4399ec5d2e6a3cd807e347
Independence required: no (implementer); re-audit separate and fresh
Evidence posture: non-independent
Evidence tier: E3 (authN/Z correction — INFOSEC 4.10/15: fresh re-audit mandatory)
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risk: this correction CHANGES the identity mechanism (username string → durable flag). A wrong flag default or a wrong migration order silently un-flags the managed account on a fresh database, or strands existing dev databases. The migration-ordering trap in §3 item 4 is the one that bites.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932 / AP.md:1444-1462 / AP.md:2466-2486 · AP_WORKER.md:14-26 ·
PROMPT_CONTRACTS.md:14-41 (report contract + coordinates) · AP.md:2453-2454 (justification enum)
INFOSEC.md:190-200 (4.10) · INFOSEC.md:369-378 (15)
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — by symbol, re-measured

```text
backend/accounts/models.py          User (AUTH_USER_MODEL; set_password stamps password_changed_at
                                    only for a previously-usable password — read it)
backend/accounts/serializers.py     UserSerializer (:40): fields include username; read_only_fields
                                    = (id, date_joined) ⇒ username IS patchable — that IS the bypass
backend/accounts/views.py           the profile PATCH view (read-only; you should not need to edit it)
backend/accounts/migrations/        latest is 0004_user_password_changed_at
backend/game/services.py            DIAGNOSTIC_SERVICE_USERNAME (:90) · ensure_diagnostic_service_user
                                    (:1129, sets unusable password on created branch + flags) ·
                                    _reject_service_account_user (:1082, username equality) ·
                                    create_game / join_human_queue guards
backend/game/migrations/0009_diagnostic_session_foundation.py
                                    RunPython seeds the user VIA the services helper; its
                                    dependencies list — ⭐ see §3 item 4
backend/tests/test_diagnostic_session.py   F-L..F-P live here; extend
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD     # MUST be f6c9db913450d56ade4399ec5d2e6a3cd807e347
git rev-parse HEAD:.ap # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status --porcelain=v1   # MUST be EMPTY
```

## 2. THE CORRECTION — durable flag, rename blocked, guards flag-based

```text
1  ACCOUNTS FIELD  backend/accounts/models.py
     is_service_account = models.BooleanField(default=False, help_text="…reserved diagnostic
     runner identity; participation-restricted; never renamed")
2  ACCOUNTS MIGRATION  backend/accounts/migrations/0005_service_account_flag.py  (NEW, AddField)
3  SERIALIZER  backend/accounts/serializers.py
     UserSerializer.validate_username: if self.instance is not None and
     self.instance.is_service_account and new username != current → ValidationError
     ("The diagnostic service identity cannot be renamed."). ⛔ Registration (create path,
     self.instance is None) is NOT blocked by this validator — the reserved-name uniqueness and
     the fail-closed ensure (F01/F-L) already own that surface.
4  MIGRATION ORDERING  ⭐ THE TRAP
     game/0009's RunPython calls ensure_diagnostic_service_user, which (after your change) sets
     is_service_account=True. On a FRESH database, accounts/0005 must run BEFORE game/0009, or the
     helper raises AttributeError on a missing attribute. FIX: add ("accounts",
     "0005_service_account_flag") to game/0009's dependencies list. Editing the dependency of an
     ALREADY-APPLIED migration is lawful here (dev DBs have 0009 recorded; fresh DBs get the
     correct order). Verify BOTH paths: fresh migrate from zero, and the existing dev DB
     (`showmigrations` — no re-apply required, no error).
5  SERVICES  backend/game/services.py
     · ensure_diagnostic_service_user: set is_service_account=True on BOTH branches (created and
       retrieved-managed), added to the dirty-fields save; the collision branch (usable-password
       claimant) STILL raises first — unchanged (F-L stays green)
     · _reject_service_account_user: refuse when user.is_service_account is True OR the username
       equals DIAGNOSTIC_SERVICE_USERNAME (belt-and-braces for any path that predates the flag);
       state this OR explicitly in the docstring
     · create_game / join_human_queue call sites: unchanged shape
6  TESTS  backend/tests/test_diagnostic_session.py  (extend; fail-before first):
     F-Q  rename of the flagged account → 4xx (pre-fix: 200 — capture verbatim; this is the
          re-auditor's P09)
     F-R  THE FULL RE-AUDITOR SEQUENCE: service JWT → rename attempt → refused → create → 400 →
          queue → 400. The exact P03→P09 chain must now fail at the rename step.
     F-S  flag survives: ensure on a managed account whose is_service_account was flipped False →
          corrected back to True on the next ensure (idempotency of the flag, mirroring the other
          flags)
     F-T  ordinary user rename still works (200) and ordinary create/queue unaffected
     F-U  fresh-DB ordering: a from-zero migrate (throwaway DB) runs accounts/0005 BEFORE
          game/0009 and completes; the seeded account has the flag
```

## 3. Path allowlist and negative authority

```text
Positive authority (exact paths):
  backend/accounts/models.py                                 ONLY the new field
  backend/accounts/migrations/0005_service_account_flag.py   NEW
  backend/accounts/serializers.py                            ONLY the validate_username addition
  backend/game/services.py                                   ONLY the two functions named in §2.5
  backend/game/migrations/0009_diagnostic_session_foundation.py   ONLY the dependencies list
  backend/tests/test_diagnostic_session.py                   ONLY F-Q..F-U

Negative authority (⛔ forbidden): everything else — gamecore, position_sets, views.py, admin.py,
  catalog/**, config/**, frontend/**, pyproject.toml, any other accounts file (views.py included),
  registrations/serializers beyond the named validator. ⛔ No provider call. ⛔ No network beyond
  the Git class below. ⛔ Never read or print backend/.env / frontend/.env.local.
```

## 4. Validation — full standing backend set

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Documented mypy scope, never narrowed. Plain `-m pytest`, never a second `-q`; quote summaries
VERBATIM. Baseline at `f6c9db9`: mypy 89 source files, ruff clean, pytest `867 passed, 4 skipped in
549.96s`. Added tests fine; no removals, no skips. Also: fresh-DB migrate from zero on a THROWAWAY
database (F-U) and the existing dev DB `showmigrations` (no re-apply, no error) — quote both.
⛔ No `npm run build`.

## 5. Git pattern — exactly this

```bash
git add backend/accounts/models.py \
        backend/accounts/migrations/0005_service_account_flag.py \
        backend/accounts/serializers.py \
        backend/game/services.py \
        backend/game/migrations/0009_diagnostic_session_foundation.py \
        backend/tests/test_diagnostic_session.py
git diff --cached --stat     # EXACTLY these six paths
git commit -m "fix(accounts) durable service-account flag closes rename bypass"
git ls-remote origin refs/heads/main    # MUST print f6c9db913450d56ade4399ec5d2e6a3cd807e347
git push origin main
git rev-parse HEAD && git ls-remote origin refs/heads/main   # readback — MUST be equal
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced → STOP, report
both SHAs, escalate.

## 6. Stopping conditions

```text
· repository gate disagreement, or porcelain is not empty
· the flag cannot be added without touching a file outside the allowlist (report — scope decision)
· fresh-DB ordering cannot be achieved via the dependency line (report — do not improvise a
  data migration or a settings hack)
· a gate failure outside the allowlist · pre-push gate failure · secret exposure
· completed work, gates green, pushed, readback equal — stop THERE and report
```

## 7. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 10, Worker exchange ordinal: 01
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it —
`implementation-PASS` expected); start/end commit; changed files with exact paths; tests and
validation — the F-Q..F-U table with pre/post values verbatim, the three gate summaries VERBATIM,
the fresh-DB and existing-DB migration evidence, and the ordering proof; commit and push result
with SHA and the readback pair; deviations, risks, missing evidence; one smallest next step
(exactly: route session 11 fresh re-audit); exactly one report justification from the closed enum
at `AP.md:2453-2454`; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: THIS PROMPT, the
  flag mechanism, and the ordering trap. Does any OTHER code path create or rename a user with
  that username and miss the flag? Assume one exists and look.>
Enumeration widened: none | <...>  — e.g. other serializers touching username, other User-creating
  paths (createsuperuser, fixtures), other dependencies on game/0009.
```

⛔ Your authority ends at that report. Do not start the re-audit, do not archive into Meta. The
re-audit (session 11) is dispatched by the ORCHESTRATOR and never by you.

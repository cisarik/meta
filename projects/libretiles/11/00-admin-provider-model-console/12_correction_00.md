You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded correction task and stop. ⛔ You have NO audit authority and NO self-certification authority. A fresh independent re-audit (session 12) will verify this correction.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 12
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: APMC-S4-CORRECT-3 — accepted finding APMC-S4-IA-F07 (high, blocking): correction-2's dependency edit stranded already-applied 0009 databases. Fix by RESTRUCTURING migration ownership: 0009 returns to pure schema; seeding + ownership-aware reverse move to a NEW unapplied game/0010 that depends on accounts/0005. One normal migrate must rescue existing DBs and build fresh DBs correctly.
Accepted finding IDs: APMC-S4-IA-F07 (blocking). F01/F02/F03 closures stand — do not reopen their mechanisms.
Audit trail: session 07 original · 08 correction-1 · 09 re-audit-1 · 10 correction-2 (flag mechanism, 6049f28) · 11 re-audit-2 (V-F02/V-F01/V-F03 verified-closed; NEW F07: every migrate form raises InconsistentMigrationHistory on a DB that already recorded 0009, and the missing column breaks the whole User ORM until rescued)
Re-audit routing: REQUIRED fresh independent re-audit (session 12)
Phase: implementation
Exact baseline: 6049f2895321da33c7594aedd922aef63544e18d
Independence required: no (implementer); re-audit separate and fresh
Evidence posture: non-independent
Evidence tier: E3 (migration restructure touching an applied migration)
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

Reasoning recommendation: **High.** Named risks: editing an ALREADY-APPLIED migration is the exact mistake class that caused F07 — this correction edits 0009 AGAIN (removing lines, not adding dependencies), and you must prove BOTH database shapes end-to-end. The Cooperator's dev DB is stranded RIGHT NOW; your fix must make ONE normal `migrate` sufficient there.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932 / AP.md:1444-1462 / AP.md:2466-2486 · AP_WORKER.md:14-26 ·
PROMPT_CONTRACTS.md:14-41 (report contract + coordinates) · AP.md:2453-2454 (justification enum)
INFOSEC.md:190-200 (4.10) · INFOSEC.md:369-378 (15)
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — by symbol, re-measured

```text
backend/game/migrations/0009_diagnostic_session_foundation.py   ⭐ IN FULL. Line 48: the
    dependency line (THE F07 defect). Lines 12-15 + 224-226: the RunPython seeding pair (moves to
    0010). Lines 18-42: the ownership-aware reverse (MOVES to 0010). Everything else is schema.
backend/accounts/migrations/0005_service_account_flag.py   the AddField (stays as-is)
backend/game/services.py          ensure_diagnostic_service_user (flag set on both branches —
                                  UNCHANGED by you) · DIAGNOSTIC_SERVICE_USERNAME
backend/tests/test_diagnostic_session.py   F-P (reverse semantics — RE-POINTS to 0010) ·
                                  F-U (ordering — RE-POINTS to 0005<0010) · F-K (0009 constraint —
                                  unchanged)
Django 5.2 migrate consistency: check_consistent_history runs BEFORE any plan — the reason
    dependency edits on applied migrations strand DBs (the re-audit's F07 static evidence)
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD     # MUST be 6049f2895321da33c7594aedd922aef63544e18d
git rev-parse HEAD:.ap # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status --porcelain=v1   # MUST be EMPTY
```

## 2. THE CORRECTION — migration ownership restructure

```text
1  game/0009 RETURNS TO PURE SCHEMA:
     · REMOVE the dependency line ("accounts", "0005_service_account_flag") — restore the original
       dependency list exactly as it was before correction-2 (swappable AUTH_USER_MODEL form)
     · REMOVE the seeding RunPython pair (ensure_diagnostic_service_user_forward,
       unensure_diagnostic_service_user) and their RunPython registration
     · REMOVE the user-deletion from 0009's reverse (0009 no longer owns the user lifecycle)
     · ADD a short docstring note: "Reserved service account seeding and its ownership-aware
       reverse live in 0010 (depends on accounts.0005). 0009 as originally applied ALSO seeded;
       0010 re-ensures idempotently, so both shapes converge."
2  game/0010_diagnostic_service_account.py  (NEW, unapplied everywhere):
     · dependencies: [("accounts", "0005_service_account_flag"), ("game", "0009_…")]
     · forward RunPython: calls services.ensure_diagnostic_service_user() (unchanged helper —
       sets the flag on both branches, raises on a usable-password claimant = the F-L loud stop)
     · reverse RunPython: MOVE the current 0009 ownership-aware reverse here VERBATIM (delete only
       the unusable-password managed account; keep claimants; keep the documented
       classification-loss residual note)
3  WHY THIS IS CORRECT FOR BOTH SHAPES (prove, do not assert):
     · EXISTING DB (0009 recorded, 0005 unapplied, column absent): no applied migration depends on
       an unapplied one any more → check_consistent_history passes → ONE migrate applies
       accounts/0005 then game/0010 → ensure sets the flag → done. ⭐ This is F-V.
     · FRESH DB: 0009 (schema only, no seeding) → 0005 (column) → 0010 (seed+flag). No missing
       column at any RunPython moment. ⭐ This is F-W.
4  TESTS  backend/tests/test_diagnostic_session.py:
     · RE-POINT F-P to 0010's reverse (claimant kept, managed deleted)
     · RE-POINT F-U to the new ordering (accounts/0005 < game/0010; seeded row flagged)
     · NEW F-V fail-before: shape a throwaway DB exactly like the Cooperator's (migrate through
       0009 AT f6c9db9's tree, then overlay HEAD) → pre-fix `migrate` raises
       InconsistentMigrationHistory (capture verbatim); post-fix ONE migrate applies 0005+0010 and
       the managed row ends flagged True
     · NEW F-W: fresh DB — after 0009 alone the reserved user DOES NOT exist; after the full
       migrate it exists with the flag; 0009's reverse no longer touches users
     · F-K (0009 constraint), F-D/F-J (user exists post-migrate), F-L/F-M (ensure), F-Q/F-R
       (rename/participation guards) — all must stay green WITHOUT modification except F-P/F-U
```

## 3. Path allowlist and negative authority

```text
Positive authority (exact paths):
  backend/game/migrations/0009_diagnostic_session_foundation.py   restructure per §2.1
  backend/game/migrations/0010_diagnostic_service_account.py      NEW per §2.2
  backend/tests/test_diagnostic_session.py                        F-P/F-U re-points + F-V/F-W

Negative authority (⛔ forbidden): everything else. ⛔ services.py (ensure stays). ⛔ accounts/**
(0005 stays). ⛔ models.py. ⛔ views/admin/catalog/config/frontend. ⛔ pyproject.toml.
⛔ No provider call. ⛔ No network beyond the Git class below. ⛔ Never read or print backend/.env /
frontend/.env.local.
```

## 4. Validation — full standing backend set + both DB shapes

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Documented mypy scope, never narrowed. Plain `-m pytest`, never a second `-q`; quote summaries
VERBATIM. Baseline at `6049f28`: mypy 90 source files, ruff clean, pytest `872 passed, 4 skipped in
551.56s`. ⛔ No `npm run build`. Plus BOTH throwaway-DB shape proofs (existing-stranded rescue and
fresh-from-zero), each with the migration output lines quoted and the final flag asserted. ⛔ Never
touch the Cooperator's real dev DB (`backend/db.sqlite3`) — throwaway copies only.

## 5. Git pattern — exactly this

```bash
git add backend/game/migrations/0009_diagnostic_session_foundation.py \
        backend/game/migrations/0010_diagnostic_service_account.py \
        backend/tests/test_diagnostic_session.py
git diff --cached --stat     # EXACTLY these three paths
git commit -m "fix(game) move service-account seeding to 0010 to unstrand applied 0009 databases"
git ls-remote origin refs/heads/main    # MUST print 6049f2895321da33c7594aedd922aef63544e18d
git push origin main
git rev-parse HEAD && git ls-remote origin refs/heads/main   # readback — MUST be equal
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced → STOP, report
both SHAs, escalate.

## 6. Stopping conditions

```text
· repository gate disagreement, or porcelain is not empty
· the restructure cannot make BOTH DB shapes pass with ONE normal migrate (report — do not
  improvise a data-rescue command or a settings hack)
· F-L (collision raise) or F-K (constraint) break — the restructure must not weaken accepted
  closures
· a gate failure outside the allowlist · pre-push gate failure · secret exposure
· completed work, gates green, pushed, readback equal — stop THERE and report
```

## 7. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 12, Worker exchange ordinal: 01
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it —
`implementation-PASS` expected); start/end commit; changed files with exact paths; tests and
validation — the F-V/F-W table with verbatim pre/post, F-P/F-U re-point evidence, F-K/F-L/F-M/F-Q/
F-R re-run confirmation, the three gate summaries VERBATIM, and BOTH throwaway shape proofs with
migration output lines; commit and push result with SHA and the readback pair; deviations, risks,
missing evidence; one smallest next step (exactly: route session 12 re-audit); exactly one report
justification from the closed enum at `AP.md:2453-2454`; explicit authority-expiry statement.
Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD, nothing unlabelled — scope: THIS PROMPT, the
  ownership restructure, and both DB shapes. Does any THIRD shape exist (partial 0005 application,
  catalog-pinned test teardowns) that the restructure strands differently? Assume one does and
  look.>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Do not start the re-audit, do not archive into Meta. The
re-audit (session 12) is dispatched by the ORCHESTRATOR and never by you.

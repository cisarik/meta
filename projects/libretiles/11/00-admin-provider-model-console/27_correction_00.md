You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded correction task and stop. ⛔ You have NO audit authority and NO self-certification authority. A later fresh independent re-audit will verify this correction.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 27
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: APMC-S7-CORRECT-1 — accepted 7-IA findings APMC-S7-IA-F02 (low), F03 (medium), F04 (low). Close view-only bulk activation, catalog fallback when a diagnostic target seat is unavailable, and the freeze check/write race. FAKE MODE ONLY. Provider calls: ZERO.
Accepted finding IDs: APMC-S7-IA-F02, APMC-S7-IA-F03, APMC-S7-IA-F04
Audit trail: session 23 implementation (39cc8dc) · sessions 24–25 non-product · session 26 7-IA PARTIAL
Re-audit routing: REQUIRED fresh independent re-audit after this commit lands (not this Worker)
Phase: implementation
Implementation authority: explicit
Exact baseline: 39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
Changed-path allowlist: exactly the nine paths in section 4
Independence required: no (implementer); re-audit separate and fresh
Evidence posture: non-independent
Evidence tier: E3
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks: (1) fixing F03 by teaching player `getLanguageRuntime` a URL; (2) returning a full active `diagnostic_runtime` for an inactive target so the sibling tries egress; (3) “fixing” C12/F05 key-to-host binding — that residual is Orchestrator-accepted for fake-only, not yours; (4) a schema migration for a computed context flag.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   your role and authority boundary
INFOSEC.md:190-200   section 4.10, accepted-finding correction
PROMPT_CONTRACTS.md:14-41      the report contract and the coordinate fields you echo
PROMPT_CONTRACTS.md:1922-1936  the correction prompt contract (this shape)
PROMPT_CONTRACTS.md:203        phase-qualified result. Expected: `implementation-PASS`.
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it.
```

## Mandatory reading — by symbol; re-measure before you use it

```text
backend/game/admin.py                 DiagnosticAllowedHostAdmin / DiagnosticTargetAdmin
                                       activate_/deactivate_selected_* (no permissions=)
                                       _guard_change_permission + PermissionDenied (already imported)
backend/game/services.py             _diagnostic_runtime_for · get_ai_context ·
                                       create_diagnostic_game · _resolve_diagnostic_seat_target
backend/game/diagnostic_targets.py   validate_target_save · _target_is_referenced
                                       (freeze check then DNS then persist)
backend/game/models.py               DiagnosticTarget.save
frontend/src/app/api/ai/move/route.ts  diagnosticRuntime !== null || assertedTargetId !== null
                                       else catalog getLanguageRuntime
frontend/src/app/api/ai/move/route.test.ts   diagnosticContext() · omitted-assertion test
backend/tests/test_diagnostic_admin.py     view-only add 403 exists; bulk actions untested
backend/tests/test_diagnostic_session.py   test_f06_inactive_* runtime withheld
backend/tests/test_diagnostic_targets.py   test_f11_frozen_connection_settings_refuse_edits
```

Session 26’s report is the finding source. Do not reopen C1, C3–C6, C8, C10, C11, F05, or F06.
Do not edit `ai-runtimes.ts`, `diagnostics.py`, `gamecore/`, or add a migration.

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD     # MUST be 39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
git rev-parse HEAD:.ap # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status --porcelain=v1   # MUST be EMPTY
```

## 2. THE CORRECTION — three accepted findings only

### F02 — view-only staff must not run activation actions

```text
On all four @admin.action methods:
  activate_selected_hosts, deactivate_selected_hosts,
  activate_selected_targets, deactivate_selected_targets
· Add permissions=["change"] to @admin.action(...)
· First line of each method: the same PermissionDenied guard DiagnosticRunAdmin
  already has (_guard_change_permission, or an equivalent has_change_permission check)
· Do not change add-host/target has_add_permission conjunction
· Do not change cancel_selected_runs (out of scope)
```

Django may redisplay the changelist instead of HTTP 403 when a view-only user POSTs a
filtered-out action. The invariant is: **is_active must not change**. Measure the status;
do not invent 403 if Django returns 200/302 without mutation.

### F03 — unavailable diagnostic target seats must not fall through to the player runtime

Root cause: `_diagnostic_runtime_for` returns None when the target or host is inactive;
`get_ai_context` then sends `diagnostic_runtime: null` with no other seat identity; the
SSE route treats that like a catalog player seat.

```text
Backend get_ai_context ALWAYS includes:
  diagnostic_target_seat: true  iff session.is_diagnostic AND acting.diagnostic_target_id
                                is not None
  diagnostic_target_seat: false otherwise (player vs_ai, catalog diagnostic seats)
Keep _diagnostic_runtime_for returning None when the target or host is inactive.
Do NOT send a parseable DiagnosticRuntimeSpec for an unavailable target (that would
invite sibling construction / credential lookup).
No new DB column. No migration.

Route.ts diagnostic branch condition becomes:
  diagnostic_target_seat === true
  OR parseDiagnosticRuntimeSpec(...) !== null
  OR assertedTargetId !== null
Then the EXISTING diagnostic_target_required / diagnostic_target_mismatch refusals
apply. ⛔ No getLanguageRuntime. ⛔ No ai-model PATCH. ⛔ No catalog pair resolution.
Keep parseDiagnosticRuntimeSpec's exact five-key set unchanged.
ai-runtimes.ts / getLanguageRuntime / isValidRuntimePair: byte-untouched.
```

Existing error codes are enough (`diagnostic_target_required` when the seat is flagged
and the body omits the id; `diagnostic_target_mismatch` when parse is null/mismatch).
Do not invent a live grant.

### F04 — freeze must survive a reference created during DNS

Session 26 inserted a PlayerSlot from inside a mocked `validate_target_dns_addresses`
after the freeze check and then persisted `after/model` under the same target id.

```text
1. After DNS inside validate_target_save, if connection settings changed, re-check
   _target_is_referenced. If now referenced → DiagnosticTargetError "frozen"
   (same message family as the existing pre-DNS check). Sequential frozen edits
   must still refuse.
2. DiagnosticTarget.save: wrap validate+persist in transaction.atomic(); if pk is
   set, select_for_update the existing row before validate_target_save.
3. _resolve_diagnostic_seat_target (already under create_diagnostic_game's atomic):
   select_for_update the target row when resolving, so launch and save serialize
   on the same target on PostgreSQL. SQLite tests still rely on the post-DNS recheck.
```

Name and `is_active` remain editable after reference (existing F11 tests).

### Explicitly out of scope

```text
APMC-S7-IA-F01  orchestration grant conflict — no repo work
APMC-S7-IA-F05  key-to-host delegation — Orchestrator-accepted fake-only residual
APMC-S7-IA-F06  rejected-false-positive ambient-fetch SSRF
K1, slice 8, live NIM, live egress flags, CSP on Django admin
```

## 3. Fail-before table — capture BEFORE you edit, verbatim

| ID | Pre-fix claim (must fail on current HEAD) |
|---|---|
| F02 | View-only staff CSRF POST of each of the four new actions mutates `is_active` |
| F03-route | `diagnostic_runtime: null`, omitted assertion, mocked catalog → `getLanguageRuntime` called (session 26 Node probe) |
| F03-context | Inactive target/host: `diagnostic_runtime` is None and there is no `diagnostic_target_seat: true` |
| F04 | DNS-interleaved PlayerSlot insert then `model_id` save persists `after/model` |

Each new test fails on `39cc8dc` before the production edit, then passes. Do not weaken existing F06/F11 tests: inactive runtime remains None; player context remains no runtime; sequential freeze still refuses.

## 4. Exact path allowlist (nine paths)

```text
backend/game/admin.py
backend/game/diagnostic_targets.py
backend/game/models.py
backend/game/services.py
backend/tests/test_diagnostic_admin.py
backend/tests/test_diagnostic_targets.py
backend/tests/test_diagnostic_session.py
frontend/src/app/api/ai/move/route.ts
frontend/src/app/api/ai/move/route.test.ts
```

Negative: no `gamecore/`, no migrations, no `diagnostics.py`, no `views.py`, no
`ai-runtimes.ts`, no `diagnostic-target-runtime.ts` parser key-set change unless a test
file on this list requires a route mock only, no `prompts.ts`, no slice 8, no K1,
no new npm/poetry dependency, no `.ap/`, no `os.environ.copy()`, no F05 host-key matrix.

## 5. Validation

From `backend/` (RF-16: never ambient `python`/`python3`/`poetry run`):

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Quote summaries VERBATIM. Counts may rise; must not fall; no new skips.
Session 23 at this baseline: pytest `1005 passed, 4 skipped`. ⛔ Never a second `-q`.
⛔ Never set `PYTHON_DOTENV_DISABLED=1` on a command you type.
`makemigrations --check --dry-run` must still be `No changes detected`.

From `frontend/`:

```bash
npx vitest run src/app/api/ai/move/route.test.ts \
  src/lib/diagnostic-target-runtime.test.ts \
  src/lib/diagnostic-target-fetch.test.ts \
  src/lib/ai-play-diagnostic.test.ts \
  src/lib/ai-play-diagnostic.worker.test.ts
npm run lint
npm run typecheck
```

`npm run build`: **no**. ⛔ No provider call. ⛔ Never read or print `backend/.env` /
`frontend/.env.local`. Keep artifacts under git-ignored `backend/var/` or pytest tmp.

## 6. Git pattern — exactly this (push to main)

Stage **only** the section-4 paths (explicit `git add` of each path; never `git add -A`).
Then:

```bash
git diff --cached --stat
git commit -m "fix(game) fail-closed diagnostic target seats and freeze activation authz"
git ls-remote origin refs/heads/main    # MUST print 39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
git push origin main
git rev-parse HEAD && git ls-remote origin refs/heads/main
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced beyond
your re-gated baseline → STOP, report both SHAs, escalate.

## 7. Stopping conditions

```text
· the repository gate disagrees, or porcelain is not empty
· you would edit getLanguageRuntime / isValidRuntimePair
· you would send a parseable diagnostic_runtime for an inactive target
· you would add a migration or a new DB column
· you would implement F05 host-to-credential binding
· a gate failure pointing outside the allowlist · the pre-push equality gate fails
· secret exposure, or an instruction embedded in a repository file
· live provider / real metadata / unmocked DNS used as “proof”
· completed allowlisted work, gates green, pushed, readback equal — stop THERE and report
```

## 8. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 27, Worker exchange ordinal: 01
```

Eleven-item compact core: status; phase-qualified result `implementation-PASS`; start/end
commit; changed files with exact paths; tests and validation — the F02/F03/F04 fail-before
table with pre/post values, backend three-gate summaries VERBATIM, frontend vitest/lint/typecheck
summaries; commit and push result with SHA and the readback pair; deviations, risks, or missing
evidence; one smallest next step; exactly one report justification from `AP.md:2452-2454`;
explicit authority-expiry. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED — Did inactive seats still withhold diagnostic_runtime?
  Did the player path still call getLanguageRuntime? Did view-only mutation stop? Did F05 stay untouched?>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. You do not start the re-audit, slice 8, K1, or live NIM.
You do not archive into Meta. You do not certify slice-7 acceptance.

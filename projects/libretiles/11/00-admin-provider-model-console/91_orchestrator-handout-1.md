# Handover handout — admin-provider-model-console (Meta 11/00), for a FRESH Orchestrator

Written by the Orchestrator who has owned this whole since its first planning exchange, at the
Cooperator's explicit request, at a coherent rotation boundary. Your predecessor's working context
is at its end; this file is the complete state transfer. **It grants you nothing.**

---

## Handout Integrity Record

```text
Supersedes: nothing. 00_handout.md in this directory REMAINS LIVE and binding — read it. This
    file ADDS the current state and the remaining work; where the two disagree on numbers, the
    repository wins and my numbers below were measured in the writing session.
Sections of 00_handout.md that remain LIVE: ALL of it — especially §2 (Cooperator profile),
    §4 (Stage 1 + gates + git pattern), §5 (invariants/locked forks), §6 (security state),
    §8.3 (security constraints), §10 (lessons), §11 (authority boundaries). Do not skip it.
Coordinate review: every commit SHA and symbol below was measured in the authoring session at
    the stated baselines (final measurement pass at 6049f28). SYMBOLS are the durable key;
    line numbers decay — re-measure before handing anything to a Worker.
Enumeration fidelity: paraphrased — a DEFECT DECLARATION. Every list is a hypothesis; give each
    Worker the command that produced it and require `Enumeration widened:` back.
Numbers not re-measured by me (inherited, load-bearing): engine strength figures (~29 plies,
    520-560 per side, BAG_EMPTY_AND_PLAYER_OUT, zero passes, 17 single-copy diacritics) and the
    live-LLM figures (ZERO backend-valid provider placements across ~a dozen counted invocations;
    provider_requests_used = 1; ~21 s with a working key). Source: PROJECT_CONTEXT.md §6.
    RE-MEASURE before building any metric on them.
Known-stale-by-design: gate counts (FINAL at handover HEAD f17a8ba: mypy 91 source files, ruff
    clean, pytest 874 passed, 4 skipped in 559.84s — re-measure anyway); the catalog rows (data,
    Cooperator-editable).
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656. Do NOT upgrade AP.

FINAL UPDATE (same session, after re-audit-3 arrived): re-audit-3 (session 13) returned PASS with
EVERY verdict verified-closed (V-F07 a-d, V-F02/F01/F03 persistence, V-ENV, V-REG) and no new
findings. The ORCHESTRATOR executed the predeclared acceptance rule: the corrective commit was
landed as `f17a8ba0dc0e0d97da770e2ed2238190b6e432b1` ("fix(game) move service-account seeding to
0010 to unstrand applied 0009 databases"; explicit 3-path staging, pre-push gate vs 6049f28,
pushed, readback equal), and **slice-4 acceptance-PASS is DECLARED**. All gate numbers below that
say 874/90 are superseded by the final-HEAD set: mypy `Success: no issues found in 91 source
files`, ruff clean, pytest `874 passed, 4 skipped in 559.84s` (measured on the exact committed
tree). The successor inherits a CLEAN main with slice 4 CLOSED and starts at §4 step 2 (K2).
```

---

## 0. Who you are, and the one rule above all others

You are a fresh Agent Orchestrator for Libre Tiles. Read, in this order: `AGENTS.md`,
`frontend/AGENTS.md` (Next.js 16 — never write App Router code from memory), the pinned AP corpus
(`.ap/AP.md`, `AP_ORCHESTRATOR.md`, `AP_WORKER.md`, `PROMPT_CONTRACTS.md`, `INFOSEC.md`), then
`/home/agile/meta/AP_DESTILLED.md` (§14-14.1 first), `/home/agile/meta/AP_DEFECTS.md`,
`/home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md`, this whole's full Meta archive
(`11/00-admin-provider-model-console/` — every prompt/report pair plus `00_notes.md` §1-§27), and
`00_handout.md` + this file.

**The one rule above all others, stated by the Cooperator as the project's absolute goal:** the AI
must beat a human at Scrabble, and he must be able to PROVE which model deserves to be deployed —
from the Django admin, without SSH, before promoting it. This whole builds that proof machine.
Never let a Worker "improve the AI" by weakening backend validation. Final score is an ENGINE
number; the model metric lives in the `completion_source` distribution and the move-quality ratio.

The Cooperator: Michal. Slovak, masculine; your self-reference feminine. Worker artifacts in
English; every terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`. Terse replies
(`A`, `Pokracuj`, `ano`) CONTINUE the selected scope and never select a new one — emit one
`SELECTION ECHO` line or a costed choice. Never read or print `backend/.env` or
`frontend/.env.local`. Emoji signal blocks at the END of every message, unmissable. Meta: you
write, HE commits. First Planner prompt of a new whole is `01_planning_00.md` (00 is reserved).

**Mandatory bounded deviation in every prompt (RF-16):** `poetry run` is unusable in a Worker
boundary (Cursor AppImage intercepts `python*` via inherited `APPIMAGE`/`PYTHONHOME`); the exact
alternate is `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`; never present
ambient `python`/`python3`/`poetry run` as a parallel route. ⛔ Never a second `-q` (pytest addopts);
⛔ never narrow the mypy scope (`config game gamecore accounts catalog`); ⛔ no `npm run build`
unless the slice mutates frontend and the claim requires it. Run
`python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>` on EVERY prompt before
issuing. Never build a prompt by string-patching the previous one.

## 1. ⭐ Current state — the exact commit chain, all measured

`main == origin/main`. All commits below are landed and publicly pushed. My re-verification ran the
full backend suite on each acceptance: green every time.

```text
01ade17  slice 3 closeout (position-set digest = closed class over asset helpers)  [ACCEPTED]
0ffaf46  slice 4 implementation: diagnostic session foundation
         is_diagnostic + bag_rng_state + full DiagnosticRun (D7) + partial-unique in-flight lock
         Value(1)/condition=Q · create_diagnostic_game · apply_position_snapshot ·
         _resolve_acting_ai_slot BRANCHED (product=first-AI slot1, diagnostic=current_turn_slot,
         None fail-closed) · get_ai_context membership/acting/opponent role split ·
         abort_diagnostic_run (zero Moves, never bypasses _reject_ai_nonscoring) · history filter
         in the SERVICE · build_ws_ticket refusal · admin dashboard exclusion · migration 0009
         seeded the reserved user
f6c9db9  correction-1: fail-closed reserved identity — ensure raises ImproperlyConfigured on a
         usable-password claimant (never silently adopts/revokes); _reject_service_account_user
         guards create_game + join_human_queue; migration reverse ownership-aware
6049f28  correction-2: DURABLE identity — User.is_service_account flag (accounts/0005),
         serializer blocks flagged rename, guards flag-OR-reserved-username, game/0009 gains
         accounts/0005 dependency  ⚠ this dependency edit was finding F07 — fixed below
f17a8ba  correction-3 (landed by the ORCHESTRATOR on re-audit-3's verified-closed evidence):
         game/0009 RETURNS TO PURE SCHEMA (dependency removed, seeding RunPython removed, reverse
         no longer touches users) · NEW game/0010_diagnostic_service_account (depends accounts/0005
         + game/0009) OWNS seeding (idempotent ensure) + the ownership-aware reverse
         ⭐ SLICE 4 ACCEPTANCE-PASS DECLARED on re-audit-3 (session 13: V-F07 a-d, V-F02/V-F01/
         V-F03, V-ENV, V-REG all verified-closed, no new findings) + the ORCHESTRATOR's own gate
         set on the exact committed tree (mypy 91 files, ruff clean, pytest 874 passed, 4 skipped)
         ⭐ Your inherited tree is CLEAN: nothing uncommitted, nothing pending on slice 4.
```

**Meta state:** `05_report_00.md` (slice-4 plan) was rendered via the exchange-02 repair shape
(`01_report-completion_01.md` pattern); pairs archived through `13_reaudit_00.md`. ⚠ Known wrinkle:
`05_implementation_00.md` carries phase "implementation" in its NAME but was a planning prompt —
historical artifact, never renamed.

## 2. Locked decisions — do NOT reopen them

```text
R1 gate cleared · R2=A credentials (env-var NAME only; provider secrets live ONLY in the Next.js
   process env; never in the DB) · R3=L4 hybrid (engine tier in-process Python; model tier ONE
   long-lived Node worker per run importing the existing POST handler; L1 HTTP to a running
   Next.js is an allowed equivalent; L3 Python reimplementation is REJECTED forever)
· R4=200 provider requests per run default, admin max 1000
· R5=A diagnostics-first (DONE); provider registry later
· Slice order: 1 ✓ 2 ✓ 3 ✓ → 4 (closing) → K2 → 5 → 3b → 6 → 7 → 8 → final 4.6 audit → closure
· assist_mode authorship: commit only backend-valid model placements; on failure abort via
  abort_diagnostic_run with diagnostic_end_reason=model_authorship_failure — NEVER a forced
  pass/exchange, NEVER around _reject_ai_nonscoring
· Identity: is_service_account flag IS the managed identity (rename-proof); username equality is
  belt-and-braces only; ensure fail-closes LOUD on a usable-password claimant
· Migration ownership: 0009 = pure schema; 0010 owns the service account lifecycle
· Position fixtures are captured in NODE-BOUND mode (20_000 nodes / 10_000_000 ms) — never bake
  production wall-clock numbers into byte-stable assets
· Browser MCP forbidden as a diagnostic driver (locked fork 7); FREE-ONLY (fork 4); exactly six
  completion_source values (fork 10); MAX_FALLBACK_ATTEMPTS=3 (fork 8); search caps are kwargs,
  never changed defaults (fork 9)
```

## 3. The audit ledger — dispositions you inherit

```text
F01 (medium) adoption of a password-enabled claimant  → CORRECTED (fail-closed ensure) ·
   re-audit-1/2: verified-closed
F02 (low→medium) service bearer participates as ordinary player → correction-1 insufficient
   (rename bypass, re-audit-1) → correction-2 (durable flag) → re-audit-2: verified-closed ON A
   MIGRATED SCHEMA; the migration delivery itself then failed (F07)
F03 (medium) migration reverse deletes adopted users → CORRECTED (ownership-aware reverse,
   moved to 0010) · verified-closed
F04 (low, NON-blocking, accepted residual) SimpleJWT persists minted refresh tokens in DB and
   renders them in token admin — existing library behaviour. ⛔ OWED AT SLICE 5: the runner's
   mint policy (token type, lifetime, rotation, storage/echo rules). The runner must never print
   or persist a token outside the SimpleJWT tables.
F05/F06 → rejected-false-positive (staff-only dashboard rows; ws verifier gap unreachable
   without signing authority)
F07 (HIGH) correction-2's dependency edit on the ALREADY-APPLIED 0009 stranded existing
   databases (every migrate form raised InconsistentMigrationHistory; missing column broke the
   User ORM). ROOT CAUSE: the session-10 grant verified the operator story with showmigrations
   only — verify `migrate` on a shaped DB, never `showmigrations`. CORRECTED by correction-3
   (0009 pure schema; 0010 owns the account lifecycle) and **verified-closed by re-audit-3**
   (session 13: both DB shapes, reverse ownership, graph sanity — all reproduced-dynamic).
```

## 4. ⭐ YOUR EXACT SEQUENCE — each step decision-complete

### Step 1 — ✅ DONE before handover (recorded so you do not redo it)

Re-audit-3 (session 13, `13_reaudit_00.md` + its report) returned verified-closed on every
verdict with no new findings. The ORCHESTRATOR landed the corrective commit `f17a8ba` and declared
**slice-4 acceptance-PASS**. Slice 4 is CLOSED. Do not re-audit it; the audit trail is in this
directory (07 → 13) and `00_notes.md` §21-§28.

### Step 2 — K2: the Node runtime probe (cheap, BEFORE slice 5)

One bounded exchange. Question: can a PLAIN Node process (`node script.mjs`, not vitest, not the
Next.js server) import `frontend/src/app/api/ai/move/route.ts`'s POST handler and invoke it with a
synthetic NextRequest (the route needs `@/*` path aliases and `NextRequest`)? The today-existing
proof is a VITEST worker (`ai-play-diagnostic.worker.test.ts` imports the route) — vitest resolves
aliases and provides NextRequest shims; plain node may not. Method: a throwaway probe script under
`/tmp/opencode` (declared in a containment ledger), run with the frontend's node_modules present;
fake mode (mocked `getLanguageRuntime`) so ZERO provider calls; declare the runtime you needed
(tsx? --experimental-strip-types? a tiny esbuild bundle?). Outcomes: **proven** → slice 5 uses L4;
**refuted** → slice 5 uses L1 (HTTP to a running Next.js) and the handoff records why. Either
outcome is an acceptable PASS. ⛔ Do not let this become a runtime-migration project.

### Step 3 — Slice 5: the runner + admin launcher (E3, the biggest slice)

Planner first (your judgement — the accepted plan D7 + the §2/§3 of `05_report_00.md` already
carry most of it; the slice-4 planning report §9 anticipated this slice). Contents:

```text
· manage.py run_diagnostic_match --run-id <uuid> — argv is the RUN ID AND NOTHING ELSE; every
  parameter read from the validated DiagnosticRun row (F-P discipline from the audit)
· the runner: consumes the DiagnosticRun (position-set or full-game instrument), drives the
  pipeline per ply, keeps SSE/409 evidence in-memory (the persistence gap the slice-2 critique
  named: first_validate_valid, earlier_attempt_failures, steps_consumed are NOT in ai_metadata),
  writes DiagnosticPly rows (NEW migration owned by THIS slice) + a bounded JSONL log
  (write_report_atomically precedent), heartbeat per ply, respects caps
· assist_mode: assisted = product-faithful; authorship = commit only backend-valid model
  placements, on failure call abort_diagnostic_run (already landed)
· admin launcher: POST under admin_view + has_change_permission (admin_view checks STAFF ONLY —
  measured), created_by must be staff (the IA finding: creation checked existence, not staff),
  launcher form never accepts a base_url (slice 7)
· aiSlot: the frontend worker passes aiSlot = session.current_turn_slot (server-derived); the
  product fallback keeps aiSlot: 1. ⚠ ai-play-diagnostic.ts:438 hardcodes 1 — the diagnostic
  worker path needs a parameter; touch it minimally and re-run the frontend gates
· F04 policy (owed): decide token type/lifetime/rotation for the runner's mint
  (RefreshToken.for_user precedent), never echo tokens, document the outstanding-token admin
  exposure as accepted residual or rotate on completion
· CAPS: run 200 default / 1000 admin max (R4); instrument subcaps PROVISIONAL until K1
· K1: a LIVE NIM grant (8-12 calls, reason: measure requests-per-ply so the position-set cap is
  derived, not guessed — the inverted-cap defect P1 from the plan review). Cooperator said NIM
  works. Activate the Provider Accounting annex; one call in flight; terminal classification
· Independent acceptance: yes (R3; extend to 4.6 if live calls are exercised)
· Standing gates + git pattern as in every prompt
```

### Step 4 — Slice 3b: LLM scorer of the committed position set

Depends on slice 4's mount + slice 5's runner. Scores the committed 24-position english fixture
(`english-f5ae61b4.json` — digest `f5ae61b4…` was valid at 01ade17; re-measure) for ONE catalog
pair: per position, mount `apply_position_snapshot`, drive one AI turn, record the ply metric
record (`ModelPositionSample` exists since slice 2). Cap 24 positions with the K1-derived request
ceiling. Fake default; live only under an explicit grant. Move-quality ratio denominator = the
snapshot's `engine_baseline.ranked_best_score` (already baked, node-bound, byte-stable).

### Step 5 — Slices 6-8 (as accepted plan D11)

```text
6  Admin UI: live run view (poll ~2 s, one PK read; Refresh: header or tiny static JS — CSP does
   NOT cover Django admin; no |safe, no mark_safe, model text as text nodes), finished report
   (LTAI + components + did_not_measure + executed_runtime_mode + score_authority), cross-model
   table with insufficient-sample states. The Cooperator's explicit demand: readable output and
   navigation he can operate daily.
7  Diagnostic target + SSRF (accepted plan D8/D9): the ONLY slice allowed to add a base_url.
   https-only, private/loopback/link-local/metadata ranges rejected, DNS re-resolution +
   re-validation, no redirect into private ranges, hard timeouts, bounded size — at Django save
   AND Next.js request time. ⭐ There is NO production egress allowlist today
   (inferProviderFromInput labels and still fetches; installFetchGuard is test-only). Insert the
   production guard in createTrackedProviderFetch. E4 if credentials land in DB (R2=A says they
   do not — env NAME only). Fresh independent audit MANDATORY (INFOSEC 4.6).
8  Probe history + fallback-order proposal: provider-capability.ts ALREADY EXISTS
   (probeProviderCapability — tool-calling probe; PROVIDER_PROBE_LIVE=1 live test; npm run
   probe:provider). Persist HISTORY per target/row (child table, not last-result). Fallback-order
   change = reviewed POST diff of sort_order; refuse when it would deactivate the last usable
   tools-tagged model or leave zero selectable rows.
```

### Step 6 — Final audit and closure

One fresh INFOSEC 4.6 provider-boundary audit over the whole landed console (mandatory — provider
egress was added). Then closure per `Logical-Block Closure`: all slices accepted, residual risks
dispositioned (F04 policy, profile-rename accounts surface accepted, admin username edit residual,
InconsistentMigrationHistory recovery documented), no active mutation, Cooperator informed. The
`14/00-ai-opponent-strength/00_handout.md` era ALREADY EXISTS (written for the next whole) — do
not confuse it with yours; it explicitly waits for 11/00 closure.

## 5. Lessons of this session — do not relearn them

```text
1  Exact-tuple pins on wall-clock-capped search are LOAD-SENSITIVE (one 435 vs 420 event, never
   reproduced in 5 runs). Node-bound parity mode is the doctrine; production tuples are recorded,
   never pinned.
2  ⛔ NEVER add a dependency to an ALREADY-APPLIED migration (F07, high, cost: three sessions).
   Put fresh-DB ordering on a NEW unapplied migration; make the seed idempotent; and VERIFY THE
   OPERATOR STORY — `migrate`, not `showmigrations`, on a throwaway DB shaped like the real one.
3  Worker-environment deltas (dotenv disabled, synthetic secrets) flip websocket tests. Before
   believing a red gate, establish baseline equivalence in the normal environment — the
   BLOCKED that looked like a regression was 19-passed green in the normal env.
4  `Enumeration widened` finds real prior art (provider-capability.ts) and real gaps (no egress
   allowlist). It is the highest-value field in every prompt. Keep it mandatory.
5  Correction loops are expensive (slice 4: three rounds). Root cause both times: MY under-scoped
   allowlist (accounts/** excluded, then needed; operator story unverified). Verify the
   end-to-end operator chain BEFORE issuing a correction grant.
6  A Worker that stops on your defective grant (blocked vs silently choosing) is the protocol
   WORKING. Three of them did exactly that this session. Never treat a BLOCKED as failure.
```

## 6. Your first bounded step

Verify the repository gate at HEAD (`f17a8ba` — clean, slice 4 closed), then proceed directly to
§4 step 2: **K2, the Node runtime probe.** Ask the Cooperator one line first: is any other
Orchestrator active? (13/00 was closed before this whole started; 14/00 exists as a written
handout that waits for 11/00 closure.)

⛔ Nothing in this file is implementation authority. Only your own complete current prompts, issued
after your own Stage 1 verification, grant work. The final sentence of your whole, if the evidence
holds: the Cooperator can sit at his admin, launch a diagnostic, watch a readable game, and know —
with numbers he took himself — which model deserves the players. That is the deliverable.

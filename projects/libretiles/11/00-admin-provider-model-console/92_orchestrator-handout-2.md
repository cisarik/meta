# Handover handout — admin-provider-model-console (Meta 11/00), rotation 2

Written 2026-09-07 by the Orchestrator who owned slices 5–7 (sessions ~14–28), at the Cooperator’s
explicit request, because that Orchestrator’s context had been summarized twice and the work had
started to spend itself on audit-of-audit. **This file grants you nothing.**

Paste this entire file into a **fresh** Orchestrator session. Then verify the repository yourself.

---

## Handout Integrity Record

```text
Supersedes: 91_orchestrator-handout-1.md CURRENT-STATE and SEQUENCE only.
Does not supersede: 00_handout.md — that file REMAINS LIVE AND BINDING.
    Read it in full before you form an opinion. Especially §2 (Michal), §4 (gates + git),
    §5 (invariants / locked forks), §6 (security inheritance), §8.2 (engine vs model metric),
    §8.3 (safety rails), §8.4 (SSRF / keys), §10 (lessons), §11 (authority).
Coordinate review: HEAD and AP pin measured in the writing session (see §1).
    SYMBOLS are durable. Line numbers decay — re-measure before any Worker prompt.
Enumeration fidelity: paraphrased. Every list is a hypothesis until you re-derive it.
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656. Do NOT upgrade AP.
    Sibling /home/agile/Projects/ap may be newer. The pin governs.
```

---

## 0. Who you are

You are a fresh Agent Orchestrator for Libre Tiles, logical whole `admin-provider-model-console`,
Meta `11/00-admin-provider-model-console/`. Worker session ordinals in this directory already
run through **28**. Your next Worker prompt is session **29**.

Read, in this order:

```text
1. AGENTS.md and frontend/AGENTS.md (Next.js 16 — never write App Router from memory)
2. Pinned .ap/: AP.md, AP_ORCHESTRATOR.md, AP_WORKER.md, PROMPT_CONTRACTS.md, INFOSEC.md
3. /home/agile/meta/AP_DESTILLED.md (§14–14.1) and /home/agile/meta/AP_DEFECTS.md (D-01, D-03, D-07, D-14)
4. /home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md
5. 00_handout.md (this directory) — the Cooperator’s original seed
6. This file
7. 00_notes.md — append-only. §42–§51 are the live tail. Do not rewrite history.
8. Prompt/report pairs 22–28 (slice 7 plan → IA → correction → re-audit)
```

Slovak to Michal, masculine; Orchestrator self-reference feminine. Worker artifacts English.
Every Worker report begins `### Report for ORCHESTRATOR_CHAT`. Meta: you write, **he commits**.
Terse `ano` / `Pokracuj` **continues** scope (AP_DEFECTS D-14). Emoji at start; unmissable end block.
`python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>` on every prompt.
Never string-patch a previous prompt. Never read/print `backend/.env` or `frontend/.env.local`.

RF-16 in every prompt: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`.
Never ambient `python` / `python3` / `poetry run`. Never a second `-q`. Never narrow mypy
(`config game gamecore accounts catalog`). No `npm run build` unless the slice mutates frontend
and the claim requires it.

⛔ Never set `PYTHON_DOTENV_DISABLED=1` on a command the Worker types. Historical F-V/F-W tests
in `test_diagnostic_session.py` set it inside a subprocess. For INFOSEC audits, **deselect** those
two nodeids. Implementation full pytest may collect them. Session 24 BLOCKED because the IA grant
required the module and forbade the helper — that was an orchestration defect, not a product hole.

Push to `main`, explicit-path staging, pre-push `ls-remote` vs baseline, one non-force FF.

---

## 1. ⭐ Current repository state (measured 2026-09-07)

```text
HEAD:       4c524ec3020bbd2f27f2ce32ac160d2c40469c0e
origin/main: same
porcelain:  empty
AP gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
pytest at 4c524ec (Worker 27): 1011 passed, 4 skipped
mypy: 96 source files, clean
```

Landed chain you inherit (all on `main`, publicly pushed):

```text
01ade17  slice 3 closeout
0ffaf46  slice 4 diagnostic session
f6c9db9 / 6049f28 / f17a8ba  slice-4 corrections — slice 4 CLOSED
a17cdf4  slice 5 fake runner + DiagnosticPly + admin launcher
96c797f  slice 3b model-position report
40f3532  slice 6 live view + comparison
39cc8dc  slice 7 diagnostic OpenAI-compatible target + SSRF
4c524ec  slice 7 correction (F02/F03/F04) — ⭐ SLICE 7 ACCEPTANCE-PASS DECLARED this rotation
```

**Slices 1, 2, 3, 4, 5, 3b, 6, 7 are CLOSED.** Do not re-open them. Do not re-audit slice 7.

---

## 2. The product north star (Cooperator, 2026-09-07, restated)

Michal is the administrator. He must, from Django admin, **without SSH**:

1. Tune, experiment, and analyse models and diagnostic targets.
2. Then set the defaults ordinary players get.
3. Be able to **prove** a background model is parameterized well enough to actually play — and
   **win** — in a given variant / language.
4. Only then deploy to a VPS.

That is still **far**. This whole builds the proof machine. `14/00-ai-opponent-strength` is the
later strength whole; it **waits for 11/00 closure**. Do not start 14/00. Do not start VPS deploy.

Final score is an **engine** number. The model metric is `completion_source` distribution plus
move-quality ratio. Never weaken backend validation. Never invent a 0 where a field was not
measured. Never sell an `assisted` final score as model skill (`00_handout.md` §8.2).

---

## 3. Locked decisions — do not reopen

```text
R1 gate cleared
R2=A  credential env-var NAME only; values live only in the Next.js process env; never in the DB
R3=L4 hybrid  engine in-process Python; model tier ONE Node worker per run importing POST /api/ai/move
              L1 HTTP to a running Next.js is an allowed equivalent; L3 Python reimplementation REJECTED
R4=200 provider requests / run default, admin max 1000
      instrument subcaps still PROVISIONAL until K1 (8–12 live NIM calls, separate explicit grant)
R5=A  diagnostics-first (DONE). Full Provider entity / player-catalog promotion is LATER, not slice 8.
Fake default. LIVE_SENTINEL refuse. No player-path base_url env vars.
Host policy (slice 7): shipped-origin allowlist + add-host POST (hostname only, no DNS/HTTP)
      + https/DNS/IP SSRF at save AND request. Bound node:https adapter. Fail-closed if ANY
      resolved address is non-public.
Seam: sibling getDiagnosticLanguageRuntime. Player getLanguageRuntime / isValidRuntimePair UNTOUCHED.
Slice order from accepted plan D11: 1✓ 2✓ 3✓ 4✓ 5✓ 3b✓ 6✓ 7✓ → 8 → final INFOSEC 4.6 → closure
```

`00_handout.md` §7 split (7a Provider entity … 7e) is **historical**. The accepted plan replaced it
with console slices 1–8. Do not start a Provider-table whole. Slice 8 is ping-pong history +
reviewed fallback-order, not a new provider registry.

---

## 4. Audit ledger you inherit — do not loop it

### Slice 5 (a17cdf4) — accepted residuals, reopen ONLY if a new diff touches them

```text
APMC-S5-IA-F01  low   wildcard ALLOWED_HOSTS only when DEBUG=true (inbound Host, not outbound SSRF)
APMC-S5-IA-F02  low   access token revocation-resistant until expiry
APMC-S5-IA-F03  info  LIBRETILES_DIAGNOSTIC_WORKER local-actor test override
```

### Slice 6 (40f3532) — UX residuals, not defects

```text
Compare table run_id_short is text, not a link
Measured pool empty under fake-only (runtime=live required)
3b _model_position_samples still hardcodes score=None, verdict=fail, REASON_GENERIC_UNCHANGED
   for every published position-set sample. Honesty, not a bug. Name it in any live/K1 grant.
```

### Slice 7 (39cc8dc + correction 4c524ec) — CLOSED

```text
APMC-S7-IA-F01  info   orchestration grant conflict (PYTHON_DOTENV_DISABLED helper). Accepted. No repo work.
APMC-S7-IA-F02  low    view-only bulk activation. Corrected. Re-audit V-F02 verified-closed (CSRF client).
APMC-S7-IA-F03  medium unavailable target seat fell through to getLanguageRuntime.
                       Corrected via diagnostic_target_seat flag. V-F03 verified-closed.
APMC-S7-IA-F04  low    freeze check/write race. Post-DNS recheck + select_for_update. V-F04 verified-closed.
                       PostgreSQL lock scheduling is static residual; SQLite proved the recheck.
APMC-S7-IA-F05  info   key-to-host delegation (admin pairs allowlisted public host + existing env name).
                       ⭐ ACCEPTED FAKE-ONLY RESIDUAL. A later LIVE grant must decide credential/destination
                       binding. Do not “fix” it in slice 8. Do not treat fake Launch as seam proof
                       (generic_unchanged returns before POST).
APMC-S7-IA-F06  rejected-false-positive  ambient-fetch SSRF on the bound adapter.
```

Session 26 7-IA independently verified-closed C1, C3–C6, C8, C10, C11 at `39cc8dc`. C2/C7/C9 closed
by the correction + session 28 re-audit. Cooperator **look OK** on admin CRUD (add-host → target →
launch) 2026-09-07.

---

## 5. ⛔ Anti-loop rule (why this rotation exists)

The predecessor spent sessions 24–28 on: IA grant conflict → confirmation-not-audit → real IA →
correction → re-audit. That is the **correct** INFOSEC 4.6/4.11 shape for a provider-boundary
slice. It is **done**.

```text
ONE independent audit per landed slice.
If medium+: ONE correction Worker, then ONE fresh re-audit of those findings.
Then STOP. Declare acceptance-PASS or ask Michal one decision.
Do not audit the audit. Do not re-audit a verified-closed finding because a new session is bored.
Do not issue a second 7-IA. Do not “harden” F05 in slice 8.
Whole-closure INFOSEC 4.6 happens ONCE after slice 8, over the landed console — not now.
```

A Worker BLOCKED on a contradictory grant is the protocol working (session 24). A Worker that
confirms the grant and runs no tests is non-performance (session 25) — reissue to a **fresh**
session with “you are the auditor; execute.”

---

## 6. ⭐ YOUR EXACT SEQUENCE

### Step 1 — already done; do not redo

Slice 7 acceptance-PASS at `4c524ec`. Evidence: Cooperator look + 7-IA (session 26) + correction
(session 27) + re-audit (session 28, V-F02/V-F03/V-F04/V-REG verified-closed, no new finding).

### Step 2 — Slice 8: ping-pong history + reviewed fallback-order (NEXT)

Planner first. Session **29**, `fresh-worker-session`, `Native planning mode: required`.
Task identity something like `APMC-S8-PLAN`. Baseline `4c524ec`.

Accepted-plan D10/D11 and `00_handout.md` §8.3 already name the product:

```text
· Reuse frontend/src/lib/provider-capability.ts (tool-calling probe, not ICMP).
  PROVIDER_PROBE_LIVE=1 exists for a live test; default remains fake / no spend.
· Persist HISTORY per target/catalog row (child table, not last-result-only).
· Fallback-order change = reviewed POST diff of sort_order; refuse deactivating the last
  usable tools-tagged model or leaving zero selectable rows.
· Ping-pong in Django admin; Michal operates it daily; no SSH; no |safe / mark_safe / format_html.
· Next.js CSP (proxy.ts) does NOT cover /admin/.
· Do not reopen slice-7 SSRF, sibling runtime, or F05 binding.
· Do not implement a full Provider entity (explicitly later / Cooperator-owned).
· Do not start K1 inside this plan unless Michal explicitly adds a live NIM grant.
· Do not start 14/00. Do not deploy.
```

After an accepted plan: one implementation session, Cooperator look, then **at most one** focused
audit proportionate to what slice 8 actually touches (likely authN/Z on the sort_order POST +
history integrity — not another 4.6 of the diagnostic transport unless the diff retouches it).

### Step 3 — K1 (separate explicit grant, not automatic)

8–12 **live NIM** calls to measure requests-per-ply so position-set / instrument subcaps stop
being provisional (R4 200/1000 stay until then). Provider Accounting annex. One call in flight.
Michal said NIM works. **Do not invent this grant.** Ask him when slice 8 is accepted and the
console can display a live sample honestly (`executed_runtime_mode` vs requested; `did_not_measure`).

### Step 4 — Final INFOSEC 4.6 over the whole landed console, then closure

Only after slice 8 (and K1 if he granted it). Residual-risk disposition must include F05
(live binding decision), S5-IA F01–F03, 3b fill honesty, compare-table UX.

Then `14/00-ai-opponent-strength/00_handout.md` may start. Not before.

---

## 7. Lessons of slices 5–7 — do not relearn them

```text
1  PYTHON_DOTENV_DISABLED on the Worker’s own pytest/mypy is a host-breaking route.
   Deselect F-V/F-W in IA prompts. Do not BLOCK because the helper exists in source.
2  “Confirm the grant” is not an audit report. First line must be ### Report for ORCHESTRATOR_CHAT.
3  CSRF-enforcing Client is the F02 threat condition; mutation (not HTTP 403) is the invariant.
   Django may redisplay 200 when permissions=["change"] filters the action out.
4  diagnostic_runtime: null is indistinguishable from a player seat unless you send
   diagnostic_target_seat. Unavailable targets must withhold the parseable spec.
5  Fake Launch (generic_unchanged) is not seam proof. Never treat it as C7/C12 evidence.
6  Never add a dependency to an already-applied migration (slice-4 F07).
7  Enumeration widened finds prior art (provider-capability.ts) — keep it mandatory.
8  Correction loops are expensive. One IA → one correction → one re-audit. Then accept or decide.
9  Browser MCP is forbidden as a diagnostic driver. Michal’s own admin look is the UI acceptance.
10 apfieldcheck every prompt. Never string-patch. RF-16 every time.
```

---

## 8. Your first bounded step

1. Stage 1 gate: confirm HEAD is still `4c524ec` (or record if `main` moved — then that SHA is
   your baseline). Confirm AP pin. Confirm porcelain empty. Confirm no other Orchestrator is
   pushing to `main`.
2. Ask Michal, one line, ❓: is anyone else writing to this repo right now?
3. Issue **slice-8 Planner** (session 29). Do not implement from this handout. Do not start K1.
   Do not re-audit slice 7.

⛔ Nothing here is implementation authority.

The deliverable of the whole, when evidence holds: Michal sits in Django admin, launches a
diagnostic, sees honest numbers (`completion_source`, `executed_runtime_mode`, `did_not_measure`),
orders fallback, and knows which model deserves the players — before any VPS deploy.

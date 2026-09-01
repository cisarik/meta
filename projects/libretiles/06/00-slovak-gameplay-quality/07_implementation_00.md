Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice T only (backend rescue + terminal error honesty)
Task identity: slice-t-rescue-and-explain-terminal-failures
Task type: bugfix implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: a12310d6950909d723a4600072ea822aded0dd62
Implementation boundaries: positive and negative authority in this prompt
Independence required: no

Planning layer: not-used
Orchestration planning owner: ORCHESTRATOR
Plan disposition: Slice T from accepted `05_report_00.md`. Slice F PASS at parent of this baseline (`06_report_00.md`). Do not plan. Do not open Plan Mode. Do not implement S, L3, or V. Do not revisit F caps.
Implementation in same Worker session: this IS the implementation session (fresh)
Planning stop event: not-used
Execution authority event: this prompt (Native planning mode: not-used)
Combined implementation envelope: prohibited — Slice T only.

Continuity (evidence, not your authority):
- F commit `a12310d6950909d723a4600072ea822aded0dd62` — `MAX_FALLBACK_ATTEMPTS = 3`, Judge 30s
- Cooperator screenshot 2026-08-30: overlay `Last error: AI move failed` (not SK-2 `The AI action was not accepted.`)
- Causal code on this baseline: `route.ts` ~1404–1415 emits that string when a generic SDK error has **no** tracked valid provider candidate; `page.tsx` ~1070–1074 copies it for `generic_error` / `no_terminal`

Recommended reasoning: High
Recommendation basis: nested try/catch scope, rescue vs coded-fallback split, and Unicode witness must not regress. Named risk is calling `generateText` again after a failed runtime, or turning coded provider errors into backend-only (killing outer three-lane fallback).
Escalation or downgrade gate: stop BLOCKED if a second SSE route, CORE bump, F cap change, backend edit, or live provider call seems required, or if Plan Mode is on.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER
External trace disposition: not-used

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: a12310d6950909d723a4600072ea822aded0dd62
Baseline subject: fix(ai): restore three-lane fallback budgets
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
`origin/main` is behind by the F commit (ahead 1). Do not fetch. Do not push.

There is no `ap.project.conf`. TypeScript/Vitest slice; do not invoke `python*`.

================================================================
GOAL (one primary outcome)
================================================================

An unclassified provider/runtime exception (not a coded `provider_*` error, not `AbortError` timeout already handled) must still finish the turn through **backend ranked candidates, then playability + direct Unicode witness**, without a second `generateText` / repair-model call.

If that rescue persists, SSE `type: done` with `completion_source` ranked or witness and `terminal_cause: generic_error_fallback` (ranked) or `backend_witness_rescue` (witness). Overlay must not show bare `AI move failed`.

If rescue cannot finish: SSE error carries bounded `code` `ai_move_internal_error` (or existing playability codes), `terminal_cause` `backend_rescue_error` or the existing probe cause, `probe_status`, `repair_attempted`. **No** raw exception message, stack, provider body, or Django secret in SSE or UI.

Coded `provider_auth_failed` / `provider_rate_limited` / `provider_unavailable` still emit immediately and remain eligible for the **outer three-lane** fallback. Do not convert those into backend-only.

A lost stream (`no_terminal` / `generic_error`) on the client: if Django state shows the anchored AI turn already advanced, **do not** paint `Last error: AI move failed`. Otherwise use `describeAiMoveFailure` (cause/probe when present).

`MAX_FALLBACK_ATTEMPTS` stays 3. Unicode `normalizePlacementData` stays `\p{L}`. CORE pin unchanged:
`c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60` / `pfr-s2-core-1`.

Fix the stale `route.ts` comment “outer five-lane fallback” → three-lane (F residual).

================================================================
SCOPE LANDMINE (read before editing)
================================================================

`commitBestAvailable`, `probeAndResolve`, `runRepair`, `emitTerminalError`, and `postAiMove` are declared **inside** the `try` that the generic `catch` belongs to. In JavaScript they are **not** callable from that `catch`. Today the catch duplicates a ranked loop and, with no `bestTracked`, skips `/ai-candidates/` entirely (`route.test.ts` “does not use a ranked backend move after a generic error with no tracked provider move”).

You must **lift** the terminal helpers to the same scope as `rankedAndProviderChoices` (~520) so the generic catch can call them. Do not copy-paste a third ranked loop.

`probeAndResolve` currently calls `runRepair` → `generateText`. After a failed runtime, **`allowProviderRepair` must be false**: skip `runRepair`; still GET playability; if `found`, POST the NFC Unicode witness directly (`backend_witness_rescue`). Timeout/`AbortError` paths that already call `probeAndResolve` without this flag keep today’s repair-when-budget-allows behavior.

`commitBestAvailable` currently sets `terminalCause` to `candidate.source`. The existing test “merges ranked choices on a generic error only after tracking a valid provider move” requires `terminal_cause === "generic_error_fallback"` and `completion_source === "backend_ranked_candidate"`. Add an optional override, e.g. `commitBestAvailable({ terminalCause: "generic_error_fallback" })`, used from the generic catch (with or without a tracked provider candidate). The normal timeout `commitBestAvailable()` path must keep candidate.source.

================================================================
CHANGED-PATH ALLOWLIST
================================================================

Existing:
- frontend/src/app/api/ai/move/route.ts
- frontend/src/app/api/ai/move/route.test.ts
- frontend/src/lib/ai-move-stream.ts
- frontend/src/lib/ai-move-stream.test.ts
- frontend/src/lib/types.ts
- frontend/src/app/game/[id]/page.tsx
- frontend/src/components/game/AIThinkingOverlay.test.ts

If `git add` would include any other path, stop BLOCKED.
Do not edit `ai-fallback.ts` (F is frozen). Do not edit `prompts.ts`. Do not edit backend.

================================================================
NEGATIVE AUTHORITY
================================================================

- No Slice S/L3/V. No lexicon. No Judge. No fallback cap. No second `/api/ai/move`.
- No live OpenRouter/NIM. No `.env`. No push. No `git add .`.
- No localStorage persistence of telemetry. No weakening Django legality / pass-while-found.
- No new dependencies.

================================================================
REPAIR SHAPE
================================================================

**route.ts**
1. Lift helpers; generic catch (after coded-provider branch):
   - `await commitBestAvailable({ terminalCause: "generic_error_fallback" })` even if `candidates` is empty (ranked fetch still runs).
   - If false: `await probeAndResolve(cause, { allowProviderRepair: false })` with a cause like `no_valid_candidate` / `generic_runtime`.
   - If still no `done` emitted: `emitTerminalError` with `code: "ai_move_internal_error"`, `terminal_cause: "backend_rescue_error"` (unless probe already emitted a specific playability/`stale_witness` error). Message: short bounded English, not `error.message`.
2. Inner `catch` that currently emits bare `"AI move failed"` / `terminal_cause: "error"` must use the same bounded error helper.
3. `generateTextMock` call count after a generic `Error` (not AbortError) must stay **1** (the failed search). Assert in tests.
4. Pass-while-`found` and Unicode witness tests stay green. `stale_witness` only when witness POST is rejected, never because `Ľ` was stripped.

**types.ts**
- Extend `describeAiTurnTelemetry` so `terminalCause === "backend_rescue_error"` (and optionally `commit_rejected`) yields a concise overlay string, e.g. `"backend rescue failed"`. Unknown combos may still be silent.
- Export `describeAiMoveFailure(input)` used by the page: prefer cause/probe/code; **must not** return only `"AI move failed"` when `terminalCause` or `probeStatus` is present.
- Export a pure `shouldHideLostAiTerminal(latest, anchor)`: `false` if `latest` is null; `true` if `game_over`, `move_count > anchor.moveCount`, or `current_turn_slot !== anchor.aiSlot`. Do **not** import `ai-fallback.ts` (cycle). Unit-test this in `ai-move-stream.test.ts` or a describe in `types` via the stream test file (no new test file unless you must; prefer existing test files on the allowlist).

**ai-move-stream.ts**
- Attach optional `telemetry?: AiTurnTelemetry` on `coded_provider_error`, `generic_error`, and `no_terminal`.
- `recordErrorEvent` / `finishTerminal`: copy last bounded telemetry from SSE error/thinking onto the terminal. `no_terminal` keeps last telemetry if any events were seen.
- Do not retain `raw_headers`, bodies, stacks. Existing credit-field tests stay green.

**page.tsx `triggerAIMove`**
- On `stopReason` `generic_error` or `no_terminal`: `syncState` / `getGameState` **before** `setAiError`. If `shouldHideLostAiTerminal(latest, turnAnchor)`, skip error (turn already advanced). Else `setAiError(describeAiMoveFailure(...))` using terminal message + telemetry (`last.telemetry` or store).
- Do not change coded-provider blocker modals.

**AIThinkingOverlay.test.ts**
- Add one case: `humanState: "backend rescue failed"` (or the exact string you chose) renders inside `ai-turn-telemetry` / attempt-progress, ping-pong unchanged.

================================================================
TESTS (required)
================================================================

In `route.test.ts` (same `rankedPayload`, `mockBackend`, `SK_WITNESS`, `generateTextMock`):

1. **Replace** `does not use a ranked backend move after a generic error with no tracked provider move` with: `generateTextMock.mockRejectedValue(new Error("generic SDK failure"))`, ranked payload present, **no** prior `validateMove`. Expect `done.completion_source === "backend_ranked_candidate"`, `terminal_cause === "generic_error_fallback"`, `/ai-candidates/` called, `/ai-move/` called, `generateTextMock` times **1**.
2. Keep `merges ranked choices on a generic error only after tracking a valid provider move` green (still 1+ generateText from validate path).
3. New: generic `Error` (not Abort), empty ranked, `SK_WITNESS` playability `found` → `backend_witness_rescue`, not `stale_witness`, placements still contain `Ľ`, `generateText` times **1**.
4. New: generic `Error`, ranked empty, playability GET throws or returns unusable → SSE error `code === "ai_move_internal_error"` or `playability_unknown`, `terminal_cause` bounded, payload JSON must not include the thrown string `"secret-rack-and-token"` if you use that as the fake error.
5. Coded provider error still does **not** POST `/ai-move/` from this stream (outer fallback). Find the existing coded-error test and keep it.

`ai-move-stream.test.ts`: error terminal preserves `terminal_cause` / `probe_status` via `telemetry`; `no_terminal` after a thinking event still has last telemetry; `describeAiMoveFailure` / `shouldHideLostAiTerminal` cases; no raw header leak.

Stay green without edits to F files:

```text
cd /home/agile/Projects/libretiles/frontend
npx vitest run src/app/api/ai/move/route.test.ts src/lib/ai-move-stream.test.ts src/lib/ai-turn-simulation.test.ts src/lib/ai-fallback.test.ts src/components/game/AIThinkingOverlay.test.ts src/lib/prompts.test.ts
npm run lint
npm run build
```

Do not run pytest. Do not start Next/Django as a product server.

================================================================
MANDATORY READING
================================================================

- this prompt
- `05_report_00.md` Slice T
- `route.ts` `rankedAndProviderChoices`, `commitBestAvailable`, `probeAndResolve`, `runRepair`, catch ~1307–1416
- `route.test.ts` tests at ~523, ~545, ~1048 (Unicode witness)
- `page.tsx` `triggerAIMove` ~900–1086
- `types.ts` `describeAiTurnTelemetry`
- `.ap/AP_WORKER.md` report header

Do not read `.env`. Do not read scrabgpt.

================================================================
REPOSITORY GATE
================================================================

cwd `/home/agile/Projects/libretiles`

- HEAD equals `a12310d6950909d723a4600072ea822aded0dd62`
- branch `main`
- porcelain empty
- `HEAD:.ap` equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Native planning mode **off** / absent

If any fails: **BLOCKED**.

Independently confirm the fail-closed test at `route.test.ts` ~545 still expects no `/ai-candidates/` **before** you invert it. Confirm `MAX_FALLBACK_ATTEMPTS === 3`.

Capability handshake: abbreviated. Plan Mode off. Do not probe API keys.

================================================================
GIT
================================================================

One local commit. Stage only allowlisted paths. No push. No amend.

Subject:

```text
fix(ai): rescue and explain terminal stream failures
```

================================================================
STOPPING CONDITIONS
================================================================

- Gate failure. Plan Mode on. Sixth product path needed.
- Coded provider errors become backend-only.
- Generic recovery calls `generateText` a second time.
- Unicode witness → `stale_witness`.
- Pass/exchange while probe `found`.
- Raw exception/private payload in SSE or `describeAiMoveFailure`.
- F caps or CORE hash change.
- Lost-stream hide fires when `latest` is null (would swallow real failures).

================================================================
COMPLETION AND REPORT CONTRACT
================================================================

**PASS** if: listed Vitest + lint + build green; CORE pin unchanged; F files untouched; one local commit; no push; `generateText` not retried on generic Error fixtures.

**BLOCKED** on stopping conditions.

Phase-qualified result: `implementation-complete` | `implementation-partial` | `implementation-blocked`
Report justification: `new-mutation`
Logical-whole closure: `not-closed`

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Echo coordinates once:
Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 07
Worker exchange ordinal: 01

Then: status; phase result; start/end commit; paths; tests; commit subject; push not authorized; residuals; smallest next step (Slice S from new HEAD); expiry; closure not-closed; Near-Misses; Pre-Existing Failure Classification.

================================================================
AUTHORITY EXPIRY
================================================================

Expires with the terminal report. Retained context is not a renewal.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
Cooperator address (Orchestrator only): Slovak.

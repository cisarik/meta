Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice F only (three-lane Play/Judge fallback budget)
Task identity: slice-f-three-lane-fallback-budget
Task type: bugfix implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: aa257a7444c8078c57b63b223421e2180a516092
Implementation boundaries: positive and negative authority in this prompt
Independence required: no

Planning layer: not-used
Orchestration planning owner: ORCHESTRATOR
Plan disposition: accepted for Slice F (and T/S). Planning report `/home/agile/meta/projects/libretiles/06/00-slovak-gameplay-quality/05_report_00.md` is PARTIAL only because Slice L3 is evidence-gated. That PARTIAL does not block F. Do not plan. Do not open Plan Mode. Do not implement T, S, L3, or V.
Implementation in same Worker session: this IS the implementation session (fresh)
Planning stop event: not-used
Execution authority event: this prompt (Native planning mode: not-used)
Post-plan implementation session: this session
Combined implementation envelope: prohibited — implement exactly Slice F.

Continuity (evidence, not your authority):
- Planner session 05 / exchange 01: `05_report_00.md` (header missing `###`; substance accepted)
- Accepted Slice F contract: three-lane queue; 120s/30-step first grant 40s/20 steps; Judge 3×10s within 30s; 503 on exhaustion
- Cooperator 2026-08-30: wants vs-AI Slovak playable; this slice restores the documented budget so NIM is not starved to ~23s/10 steps

Recommended reasoning: Medium
Recommendation basis: constant + test-arithmetic change in five named frontend files. Named risk is four-lane leak or Judge false-invalid on exhaustion, covered by stay-green tests, not Extra High.
Escalation or downgrade gate: stop BLOCKED if a fourth provider POST is required for green tests, if Judge would need to invent verdicts, if `route.ts` / `prompts.ts` / backend seem required, if CORE hash/version would change, or if Plan Mode is on.
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
Exact baseline: aa257a7444c8078c57b63b223421e2180a516092
Baseline subject: fix(engine): use SSS B2 as Slovak two-letter lexicon
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: equals this baseline. Do not fetch. Do not push.

There is no `ap.project.conf`. Do not invent an AP toolchain. This slice is TypeScript/Vitest only; do not invoke `python*`.

================================================================
GOAL (one primary outcome)
================================================================

Play and Judge share a fallback queue of **at most three** distinct provider/model pairs. Preference remains lane one; remaining lanes follow untouched catalog order.

After this commit, deterministic tests must pin:

- `MAX_FALLBACK_ATTEMPTS === 3`
- `attemptTimeoutSeconds(120, 3) === 40`
- `attemptStepGrant(30, 3) === 20`
- `buildFallbackQueue` length ≤ 3 for the five-row bootstrap catalog
- Judge `OVERALL_BUDGET_MS === 30_000`, still 10s per attempt, HTTP 503 on exhaustion, **no** synthesized `invalid` results
- no fourth Play POST and no fourth Judge `generateText` on exhaustion

`MIN_ATTEMPT_STEPS` stays **5** (repair/tool-loop floor, not lane count). Do not “fix” comments about five-step reserves by changing that constant.

Catalog still has five bootstrap rows. Overlay may still render five **injected** pills in `AIThinkingOverlay.test.ts`. Do not change that file. Do not shrink the catalog.

English CORE SHA-256 remains `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`. Version `pfr-s2-core-1`.

This is Defect D only. Generic `AI move failed` rescue is Slice T. Slovak ranked CLI is Slice S. Hunspell ≥3 is L3.

================================================================
CHANGED-PATH ALLOWLIST (nothing else may change)
================================================================

Existing:
- frontend/src/lib/ai-fallback.ts
- frontend/src/lib/ai-fallback.test.ts
- frontend/src/lib/ai-turn-simulation.test.ts
- frontend/src/app/api/ai/judge/route.ts
- frontend/src/app/api/ai/judge/route.test.ts

If `git add` would include any other path, stop BLOCKED.

Do not edit `AGENTS.md` (already says three pairs and 30s Judge).
Do not edit `frontend/src/app/api/ai/move/route.ts` (stale “outer five-lane” comment is an accepted residual for Slice T).
Do not edit `AIThinkingOverlay.tsx` / `.test.ts`.
Do not edit `prompts.ts`.

================================================================
NEGATIVE AUTHORITY
================================================================

- No backend. No `slovak.txt`. No Slice T/S/L3/V.
- No JULS, no live OpenRouter/NIM, no `.env`, no Stripe, no production, no push.
- No second SSE route. No CORE / version bump. No catalog seed/sync. No store default timeout/step changes.
- No `MAX_TRACKED_REQUESTS` change on the Judge route (that is a tracker ceiling, not the lane budget). Change **only** `OVERALL_BUDGET_MS` and comments/tests that encode 50s / five lanes.
- No git fetch/switch/stash/clean. One local commit only, after tests pass.

================================================================
REPAIR SHAPE
================================================================

1. `ai-fallback.ts`: set `MAX_FALLBACK_ATTEMPTS` to `3`. Keep `buildFallbackQueue` order, `attemptTimeoutSeconds`, `attemptStepGrant`, accounting, and `gameStateAllowsRetry`. Update comments that say the **queue** is five lanes. Do not rewrite comments that mean the **five-step** `MIN_ATTEMPT_STEPS` reserve.

2. `ai-fallback.test.ts`: every expectation that encodes five **lanes** becomes three. Independently confirmed on this baseline (re-read; do not trust blindly):
   - `buildFallbackQueue(...)` `.toHaveLength(5)` and catalog-order arrays of five pairs → first three pairs of the same ordering
   - `gives Play and Judge identical queues` length 5 → 3
   - `de-duplicates exact pairs and never exceeds five attempts` → three
   - `attemptTimeoutSeconds(120, 5) === 24` → **replace** with `attemptTimeoutSeconds(120, 3) === 40`. Keep other timeout-slice cases that are not five-lane pins unless they fail.
   - Add/pin `attemptStepGrant(30, 3) === 20`. Keep the existing `reserves exact five-step grants for later lanes` cases (`attemptStepGrant(50, 5)` etc.) — those test the step-reserve formula, not lane count.
   - `decideNextFallbackAttempt({ queueLength: 5, ...})` → `queueLength: 3` where it represented lane count
   - `runStream` / posts called 5 times on exhaustion → 3
   - `defensively caps a raw caller queue at five lanes` → three (raw queue still longer than 3; slice to 3)
   - `can succeed only on lane five with four reconciliations` → lane three, **two** reconciliations, one terminal
   - Recompute exhaustion `maxStepsRemaining` arrays from the unchanged `attemptStepGrant` + charge-floor behavior. Do **not** copy `[10,10,10,10,10]`. First lane of a 30-step whole turn with 3 attempts left must be **20**.

3. `ai-turn-simulation.test.ts`: keep exercising all five bootstrap **preferences**. Change pair/post caps from `> 5` to `> 3`. Test title may still say “five bootstrap rivals”. Assert at most three posts / distinct pairs per turn.

4. `judge/route.ts`:
   - File header fallback contract: three distinct pairs; at most three sequential lanes; 10s per attempt; **30s** overall.
   - `OVERALL_BUDGET_MS = 30_000`
   - Leave `ATTEMPT_TIMEOUT_MS = 10_000`
   - Leave `MAX_TRACKED_REQUESTS = 50_000`

5. `judge/route.test.ts`: rewrite five-lane / 50s fixtures:
   - exhaustion and malformed-output: `generateText` / runtime **3** times, still 503, `results` absent
   - `generateTextMock.mock.calls.length < 5` success-on-last-lane → `< 3` (succeed on lane three)
   - Date.now / `AbortSignal.timeout` ladder that used `49_995` and five `10_000`s must be rebuilt for a **30_000** overall budget (three attempts). Do not keep a 50s clock.
   - `returns five-lane 503 accounting`: last-lane `retry_after` used `index === 4` and `provider_requests_used: 10` for five × 2. Recompute for three lanes (last index 2). Still no invented verdicts.

================================================================
TESTS (required)
================================================================

Stay green after arithmetic updates:

```text
cd /home/agile/Projects/libretiles/frontend
npx vitest run src/lib/ai-fallback.test.ts src/lib/ai-turn-simulation.test.ts src/app/api/ai/judge/route.test.ts src/app/api/ai/move/route.test.ts src/lib/prompts.test.ts
npm run lint
npm run build
```

`route.test.ts` and `prompts.test.ts` must stay green **without** edits (Unicode ranked/witness + CORE pin). The Slice T test `does not use a ranked backend move after a generic error with no tracked provider move` must still fail closed in this slice.

Do not run pytest. Do not start Next/Django. Do not call providers.

================================================================
MANDATORY READING (deep)
================================================================

- this prompt
- `/home/agile/meta/projects/libretiles/06/00-slovak-gameplay-quality/05_report_00.md` Slice F only
- `frontend/src/lib/ai-fallback.ts` (`MAX_FALLBACK_ATTEMPTS`, `buildFallbackQueue`, `attemptTimeoutSeconds`, `attemptStepGrant`, `orchestrateFallbackTurn` slice)
- the five allowlisted test files (full, not grep-only)
- `frontend/src/app/api/ai/judge/route.ts` header + `OVERALL_BUDGET_MS`
- `.ap/AP_WORKER.md` and `PROMPT_CONTRACTS.md` (implementation report header)

Do not read `.env` / `.env.local`.
Do not read scrabgpt / FrameNest.

================================================================
REPOSITORY GATE (before mutation)
================================================================

cwd `/home/agile/Projects/libretiles`

- `git rev-parse HEAD` equals `aa257a7444c8078c57b63b223421e2180a516092`
- branch `main`
- `git status --porcelain` empty
- `git rev-parse HEAD:.ap` equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Native planning mode **off** / absent

If any fails: **BLOCKED**, no edits.

Independently confirm `MAX_FALLBACK_ATTEMPTS === 5` and Judge `OVERALL_BUDGET_MS === 50_000` before patching.

Capability handshake: abbreviated. Report Plan Mode off. Do not probe API keys.

================================================================
GIT
================================================================

One local commit. No `git add .`. Stage only the five allowlisted paths. No push. No amend.

Subject:

```text
fix(ai): restore three-lane fallback budgets
```

================================================================
STOPPING CONDITIONS
================================================================

- Gate failure or dirty porcelain.
- Plan Mode on.
- Need to edit a sixth path.
- Fourth lane required for tests to pass.
- Judge 503 path would synthesize `invalid`.
- CORE hash/version drift.
- Pressure to also ship Slice T in this commit.
- Live provider calls.

================================================================
COMPLETION AND REPORT CONTRACT
================================================================

Status **PASS** if: three-lane pins above hold; listed Vitest + lint + build green; CORE pin unchanged; one local commit on the five paths; no push.

**PARTIAL** if tests green but a named residual (e.g. `route.ts` five-lane comment) is the only leftover inside F’s intent — prefer PASS and list it as residual for T.

**BLOCKED** on stopping conditions.

Phase-qualified result: `implementation-complete` | `implementation-partial` | `implementation-blocked`

Report justification: exactly `new-mutation`.

Logical-whole closure: `not-closed`.

Standard terminal report must begin exactly:

### Report for ORCHESTRATOR_CHAT

Then include exactly once:

Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 06
Worker exchange ordinal: 01

Then: status; phase-qualified result; start and end commit; changed files; tests/validation (summarize; full output only on failure); commit hash and subject; push: not authorized; deviations/risks; one smallest next step (expected: Orchestrator issues Slice T from the new HEAD); authority expiry; Logical-whole closure: not-closed; Resolved Execution Issues / Near-Misses; Pre-Existing Failure Classification.

================================================================
AUTHORITY EXPIRY
================================================================

This exchange’s implementation authority expires with the terminal report, cancellation, or supersession. Retained context is not a renewal. Plan UI approval grants nothing.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT
Cooperator address (Orchestrator only): Slovak.

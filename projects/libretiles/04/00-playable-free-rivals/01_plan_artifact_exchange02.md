# Playable Free Rivals MVP — Prompt plus authoritative orchestration

## Summary

Implement Fork 2: simplify and harden the move prompt, require backend-validated placement tool calls, and add a narrow backend playability witness that prevents AI pass/exchange whenever a legal scoring move exists.

The backend remains the sole Collins 2019 and game-rule authority. The witness is a fail-closed rescue mechanism, not a ranked move engine. Existing preference-first fallback order, three-pair cap, unchanged-turn reconciliation, and shared provider-call budget remain unchanged.

Success means:

- Zero persisted pass or exchange while the authoritative probe reports a legal scoring move.
- No Collins-invalid, rack-invalid, or stale-state move can persist.
- Free providers still originate or revalidate most moves; backend direct rescue is bounded and measured.
- Prompt and orchestration behavior is reproducible without provider keys.

## A. Diagnosis and observability

### Persisted-pass paths

| Path | Current evidence | Classification |
|---|---|---|
| Model explicitly returns `"action":"pass"` | The free-form response controls `finalAction` at [route.ts:803](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:803), then [route.ts:956](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:956) persists it. | Model-chosen, but orchestration accepts it without proving the rack is dead. |
| Model returns exchange after finding a valid candidate | Exchange is handled before placements at [route.ts:928](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:928). | Model-chosen non-scoring action incorrectly outranks validated evidence. |
| Model finds a valid candidate and later says pass | Candidate replacement at [route.ts:846](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:846) changes placements but does not reset `finalAction`; the pass branch still wins. | Concrete orchestration defect. |
| Provider generation times out without a tracked candidate | [route.ts:784](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:784) assigns pass at line 801. | Orchestration-forced pass inside one provider attempt. |
| Normal completion has malformed/no JSON and no usable placement | `finalAction` defaults to place, but empty placements satisfy the pass condition at line 956. | Orchestration-forced pass caused by output-shape failure. |
| Chosen and alternate candidates are all rejected at commit | [route.ts:984](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:984) tries alternatives, then [route.ts:1006](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:1006) forces pass. | Orchestration-forced pass after invalid/stale candidates. |
| Provider exception | The catch path attempts a tracked candidate or emits an error; it does not persist pass. | Not a pass source. |
| All rival attempts or whole-turn budget are exhausted | The outer fallback returns an error/blocker and leaves the turn unchanged. A `done:pass` is instead considered successful and stops fallback. | Not a persisted-pass source. |
| Direct `/ai-pass/` request | [services.py:1118](/home/agile/Projects/libretiles/backend/game/services.py:1118) accepts AI pass without checking for legal scoring moves. | Missing backend defense-in-depth. |
| AI Judge | The move route validates directly against Django/Collins. No caller connects `/api/ai/judge` to move selection. | Not causal. Leave Judge unchanged. |

Three consecutive passes are therefore most plausibly three separate attempt-one streams that each returned `done:pass`, caused by explicit pass output, missing/malformed structured output, timeouts, or rejected candidates. The outer three-rival fallback did not itself manufacture those passes. The tracked-candidate/action-precedence defect is also a plausible contributor. Existing persistence cannot distinguish these causes because pass/exchange moves receive no `ai_metadata`.

### Privacy-safe classification

Persist a bounded metadata object for every AI place, exchange, and pass using the existing `Move.ai_metadata` field:

- Prompt version and selected prompt ID/name, never prompt text.
- Requested/runtime provider and model IDs.
- Up to three sanitized attempt records: outcome code and provider-request count.
- Valid/rejected candidate counts.
- `terminal_cause`, `probe_status`, `repair_attempted`, and `completion_source`.
- Current-attempt and whole-turn provider-request counts.
- Normalized token usage where already available.

Allowed `completion_source` values:

- `provider_candidate`
- `repair_candidate`
- `backend_witness_rescue`
- `genuine_no_move_exchange`
- `genuine_no_move_pass`

Stop persisting response headers, raw provider metadata, raw model output, tool arguments, prompts, racks, boards, credentials, or tokens. Validate this metadata with an explicit serializer; ignore unknown keys.

## B. Prompt-engineering overhaul

### Pattern-library mapping

- P01, Outcome/Evidence/Observable Rationale: the sole top-level objective is “complete this turn with a backend-validated scoring placement.” A successful `validateMove` result is the observable evidence.
- P06, High-Signal Context: move action discipline, coordinates, rack semantics, and Collins authority precede strategy. Remove tournament theatre and competing early instructions.
- P07, Canonical Few-Shot: include two short tool-call exemplars—first-move placement and rejected-candidate recovery, including blank syntax.
- P08, Stable Tool/Failure Contract: use strict tool schemas, force `validateMove` first, and eliminate free-form action JSON as an authoritative result.
- P16, Untrusted-Content Boundary: delimit board state and selected search profile as data that cannot alter the action protocol.
- P18, Evaluation-Driven Prompt Evolution: export a prompt version/fingerprint and gate changes with the deterministic simulation matrix.
- P04, P05, and P09 apply to implementation risk, slice boundaries, and later human acceptance rather than the in-game prompt.
- P02, P03, P10–P15, and P17 concern governance, capability handshakes, permissions, secrets, or deployment workflows. Injecting them into a tile-move prompt would add attention cost without improving move legality.

### System and user prompt contract

- Always compose a non-overridable TypeScript core prompt with the selected database prompt as a delimited advisory `SEARCH_PROFILE`. A customized profile may influence search order but cannot redefine actions, Collins authority, coordinates, or tool use.
- State truthfully that pass and exchange are legal game actions, but the application—not the model—chooses them only after an authoritative no-move result. The model’s task is placement search.
- Serialize the board as 15 labeled rows such as `row 00 |...............|`, explicitly defining zero-based row/column coordinates.
- Serialize the rack as a spaced multiset so duplicates remain visible. Define regular tiles as `letter:"A"` with no `blank_as`, and blanks as `letter:"?"`, `blank_as:"A"`.
- Include first-move status, center rule, scores, bag count, exchange availability, and legal anchor squares. Anchors are context, not pre-generated candidates.
- Remove premium-square strategy from the initial action discipline because premium locations are not currently serialized. Strategy instructions apply only after obtaining a valid scoring floor.
- Provide two compact examples:
  1. A first move covering `(7,7)`, followed by a valid `validateMove` result and finalization.
  2. An invalid tool result followed by a different placement, demonstrating that rejection means pivot—not pass.
- Keep initial temperature at `0.15` so the structural change is measurable. Use `0` only for the exact-witness repair prompt.
- Replace duplicated full seed prompts with short search profiles for Initial, Fast Search, Short Hooks, and Grandmaster. Add migration `0011`, hash-gated against the exact `0010` seeded values and reversible only for rows that remain unmodified.
- Leave both Judge prompts/routes unchanged in this logical whole.

## C. Cooperator forks and recommended runtime

### Fork decision

| Fork | Result |
|---|---|
| 1 — Prompt only | Lowest implementation risk, but cannot distinguish a genuinely dead rack from timeout, malformed output, or model pass preference. It cannot guarantee the zero-avoidable-pass invariant. |
| 2 — Prompt plus orchestration | Recommended. Adds authoritative playability evidence, forced validation, bounded repair, and fail-closed backend guards while preserving current provider fallback limits. |
| 3 — Client-side TypeScript candidate generation | Reject for this whole. It would duplicate Collins/rules in the frontend, risk authority drift, and reopen the parked stronger-search project. |

Fork 2’s backend witness is not Fork 3: it returns one authoritative witness only after provider search fails. It does not rank moves, pre-populate normal provider turns, or expose a candidate list.

### Backend authority

1. Extract one rack-aware legality evaluator used by AI validation, AI submission, and final witness certification. It must enforce:

   - Coordinates and blank representation.
   - Rack multiset coverage, including duplicate tiles and blanks.
   - Occupancy, line, no-gap, center/connection rules.
   - All formed words through Collins 2019.
   - Positive score.

   This also closes the current phantom-rack defect caused by silent rack consumption.

2. Add a pure-Python `gamecore/move_search.py`:

   - Use the existing Collins asset and a cached sorted-prefix index; add no dependency.
   - Enumerate deterministic legal starts/directions from the center on the first move or adjacent anchors thereafter.
   - Traverse fixed board letters and rack/blank branches, prune missing prefixes, and Collins-check perpendicular cross-words.
   - Re-certify the first witness with the shared legality evaluator.
   - Return `none` only after exhaustive traversal.
   - Stop at 2,000,000 nodes or 2,000 ms and return `indeterminate`; `indeterminate` can never authorize pass/exchange.

3. Add authenticated owner-only `GET /api/game/{game_id}/ai-playability/`, valid only for an active AI turn:

```json
{
  "status": "found | none | indeterminate",
  "witness": {
    "placements": [],
    "words": [],
    "total_score": 0
  },
  "exchange_allowed": false,
  "exchange_letters": [],
  "search": {
    "complete": true,
    "nodes": 0,
    "elapsed_ms": 0
  }
}
```

`witness` is non-null only for `found`; deterministic full-rack `exchange_letters` are returned only for `none` with at least seven tiles remaining in the bag. A computed result is HTTP 200; wrong ownership/turn uses existing authentication semantics plus HTTP 409 for state conflict.

4. Defend AI-only terminal endpoints under the transaction lock:

   - Reject AI pass/exchange with HTTP 409 and `legal_scoring_move_exists` when status is `found`.
   - Reject both with `playability_unknown` when status is `indeterminate`.
   - Reject AI pass with `exchange_required` when status is `none` but exchange is possible.
   - Preserve human pass/exchange behavior.
   - Do not trust a prior client probe; recompute before non-scoring persistence.

5. Replace bare placement dictionaries with a nested strict serializer: row/column `0..14`, uppercase `A..Z` or `?`, maximum seven placements, unique cells, and conditional `blank_as`.

No database schema migration is required.

### Provider-attempt state machine

- Remove model authority over pass/exchange and ignore free-form final JSON.
- Use AI SDK `prepareStep` to force `validateMove` on step one.
- While no valid candidate exists, expose only `validateMove`; once one exists, expose `validateMove` plus a no-side-effect `finishMove({ready:true})`.
- Always apply the highest-scoring backend-valid tracked candidate, even if later text or tool behavior is malformed.
- Reserve exactly two of the attempt’s granted provider steps for at most one repair phase. With the existing minimum of five, initial search receives `max_steps - 2`.
- All provider steps from initial and repair phases count toward the same granted `max_steps`. Keep `maxRetries:0`.
- Retryable provider failures such as 429 remain errors so the outer preference-first queue can reconcile the unchanged turn and try the next pair.
- For semantic exhaustion, timeout, malformed tool behavior, or commit rejection:
  1. Query playability.
  2. `found`: if two reserved steps and at least two seconds remain, run one temperature-zero repair with the exact witness and force `validateMove`; otherwise apply the witness directly through `/ai-move/`.
  3. `none`: exchange all rack tiles if allowed; otherwise pass.
  4. `indeterminate` or probe failure: emit an error and leave state unchanged.
- A direct witness still passes through locked AI submission and the shared Collins/rack evaluator. A stale/rejected witness causes reconciliation/error, never fallback pass.
- Keep the current queue ordering, maximum of three distinct pairs, retryable-error policy, and unchanged-turn reconciliation.
- Correct aggregate accounting so a successful terminal attempt is charged before `orchestrateFallbackTurn` returns. Preserve per-attempt `provider_requests_used` and add separate `turn_provider_requests_used`; do not redefine the existing SSE field.

### UI observability

Extend transient attempt progress with normalized failure code, playability state, and completion source. Show concise states such as “backend found a legal rescue; repairing.” Preserve existing pill ordering, animation, reduced-motion behavior, and Premium Look behavior. Do not persist diagnostics in Zustand/local storage.

### Rollback

No new runtime flag is needed. The work remains three local, reversible commits:

1. Revert the frontend observability/harness commit.
2. Revert the prompt/orchestration commit and reverse `0011`; reversal changes only still-unmodified seeded rows.
3. Revert the additive backend guard/search commit.

Do not deploy an intermediate slice. Production rollout or rollback remains separate authority.

## D. Deterministic causal simulation

### Backend tests

Add shared fixtures plus pytest coverage for:

- First move through center and later connected moves.
- Fixed board letters, cross-words, boundaries, duplicates, blanks, and occupied cells.
- `found`, exhaustive `none`, and capped `indeterminate`.
- Validator, persisted submission, and witness parity.
- Phantom-rack rejection.
- AI pass/exchange guards and unchanged human behavior.
- Prompt migration forward/reverse behavior and customized-row preservation.

Timing tests use deterministic node caps rather than flaky wall-clock assertions. The focused warmed Collins/search suite must remain under 15 seconds.

### Frontend full-turn harness

Add a Vitest harness invoking the actual fallback orchestrator, exported move-route `POST`, SSE consumer, and stateful fake Django endpoints. Mock only provider generation and HTTP transport; any unexpected network request fails the test.

Run:

- 10 deterministic six-AI-turn replay games.
- Each replay against all five bootstrap rival pairs.
- 300 completed simulated turns total.
- Per rival: 54 probe-`found` turns, three genuine no-move exchanges, and three genuine dead passes.
- Scripted behaviors include valid placement, valid placement followed by pass text, malformed output, invalid candidates then repair, timeout/direct rescue, commit rejection/re-probe, and retryable 429 followed by reconciled rival fallback.
- Test `indeterminate` separately and require zero persistence.

Acceptance assertions:

- Avoidable non-scoring violations: `0/270`.
- Witness-positive placement completion: `270/270`.
- Highest-scoring tracked valid candidate retained: 100%.
- Genuine no-move action correctness: `30/30`.
- Persisted Collins/rack-invalid moves: zero.
- No provider attempt exceeds its granted steps; no turn exceeds three pairs.
- Reconciliation occurs before every later pair.
- No turn-state drift.

The 300-turn Vitest must finish under 10 seconds. Export `MOVE_PROMPT_VERSION` and snapshot the prompt SHA-256, critical priority order, strict tool schemas, labeled-board format, and migration hashes so prompt drift requires intentional test updates.

## E. Later live-play acceptance protocol

This is design only and requires a separate explicit grant, credentials, and privacy approval.

Test two games per exact flag-off rival:

1. OpenRouter `google/gemma-4-31b-it:free`
2. NVIDIA NIM `nvidia/nemotron-3-super-120b-a12b`
3. OpenRouter `nvidia/nemotron-3-super-120b-a12b:free`
4. OpenRouter `z-ai/glm-5.2:free`
5. OpenRouter `google/gemma-4-26b-a4b-it:free`

Observe the first eight AI turns in each game. If a game ends early, start a replacement for that rival until exactly 16 analyzed turns per rival and 80 total are collected.

MVP-PASS requires:

- Avoidable pass/exchange rate: exactly 0%.
- Every persisted pass has probe `none` and exchange unavailable.
- No two-turn AI pass streak unless every pass is independently certified `none`.
- Zero Collins-invalid, rack-invalid, or stale-state moves.
- Zero terminal `indeterminate` blockers.
- Provider or repair candidates complete at least 80% of each rival’s turns.
- Direct backend rescue is at most 10% overall and at most 20% for any rival.
- At least one provider-originated valid placement from every rival.
- Provider pair cap, request accounting, and reconciliation remain exact.

Read only the bounded `Move.ai_metadata` classification through Django Admin/export: game/move ID, rival, terminal cause, probe status, completion source, attempt codes, and request counts.

Observe a naturally occurring 429→fallback event opportunistically. Do not provoke one. If observed, require metadata to show rate limiting, unchanged-turn reconciliation, the next provider, shared-budget accounting, and final legal placement. Its absence does not fail MVP and leaves the inherited backlog item open.

## F. Ordered implementation slices

### Slice 1 — Authoritative legality and playability guard

Exact allowlist:

- `backend/gamecore/fastdict.py`
- `backend/gamecore/legality.py` — new
- `backend/gamecore/move_search.py` — new
- `backend/game/services.py`
- `backend/game/serializers.py`
- `backend/game/views.py`
- `backend/game/urls.py`
- `backend/tests/test_gamecore.py`
- `backend/tests/test_dictionary_validation.py`
- `backend/tests/test_api.py`
- `backend/tests/test_move_search.py` — new

Positive boundary: centralized legality, exact/indeterminate witness, endpoint, AI-only pass/exchange guard, strict placements, bounded metadata persistence.

Negative boundary: no frontend/provider work, human-action changes, dictionary modification, schema migration, new dependency, or alternative dictionary.

Git-write: yes, one local commit; no push. Suggested subject: `feat: add authoritative AI playability guard`.

Evidence tier: E2.

Validation:

```bash
cd backend
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run ruff check .
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run mypy config game gamecore accounts catalog
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run pytest tests/test_move_search.py tests/test_gamecore.py tests/test_dictionary_validation.py tests/test_api.py
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run pytest
```

Mypy must remain exactly at the accepted 63-errors/17-files baseline with no new diagnostic.

Stop if witness/evaluator results disagree, ordinary fixtures become `indeterminate`, Collins must be weakened, a heavy dependency is needed, or tracked state drifts from the authorized baseline.

### Slice 2 — Prompt, tool-only orchestration, and seed refresh

Exact allowlist:

- `frontend/src/lib/prompts.ts`
- `frontend/src/app/api/ai/move/route.ts`
- `frontend/src/app/api/ai/move/route.test.ts`
- `frontend/src/lib/prompts.test.ts`
- `backend/catalog/migrations/0011_playable_seeded_prompts.py` — new
- `backend/tests/test_playable_seeded_prompts_migration.py` — new
- `backend/tests/test_refresh_seeded_prompts_migration.py`

Positive boundary: core/profile separation, labeled state, two few-shots, forced validation, two-step repair reserve, witness rescue, and hash-gated seed migration.

Negative boundary: no Judge changes, catalog changes, queue changes, TypeScript move generator, sampling experiment beyond specified temperatures, historical migration edits, or overwrite of customized prompts.

Git-write: yes, one local commit; no push. Suggested subject: `feat: require validated AI moves before non-scoring fallback`.

Evidence tier: E2.

Validation:

```bash
cd frontend
npm test -- src/lib/prompts.test.ts src/app/api/ai/move/route.test.ts
npm run lint -- src/lib/prompts.ts src/app/api/ai/move/route.ts
./node_modules/.bin/tsc --noEmit

cd ../backend
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run pytest tests/test_playable_seeded_prompts_migration.py tests/test_refresh_seeded_prompts_migration.py
```

Stop if any free-form pass path remains authoritative, repair exceeds the granted provider-step budget, direct rescue bypasses locked backend validation, or migration tests alter a customized row.

### Slice 3 — Accounting, telemetry, UI, simulation, and documentation

Exact allowlist:

- `tests/fixtures/playable-free-rivals.json` — new
- `frontend/src/app/api/ai/move/route.ts`
- `frontend/src/app/api/ai/move/route.test.ts`
- `frontend/src/lib/ai-fallback.ts`
- `frontend/src/lib/ai-fallback.test.ts`
- `frontend/src/lib/ai-move-stream.ts`
- `frontend/src/lib/ai-move-stream.test.ts`
- `frontend/src/lib/types.ts`
- `frontend/src/lib/api.ts`
- `frontend/src/hooks/useGameStore.ts`
- `frontend/src/hooks/useGameStore.test.ts`
- `frontend/src/app/game/[id]/page.tsx`
- `frontend/src/components/game/AIThinkingOverlay.tsx`
- `frontend/src/components/game/AIThinkingOverlay.test.ts`
- `frontend/src/lib/ai-turn-simulation.test.ts` — new
- `AGENTS.md`
- `docs/architecture.md`

Positive boundary: sanitized attempt trace, corrected aggregate request accounting, transient UI state, 300-turn causal suite, and documentation.

Negative boundary: no queue reorder/cap change, provider retry-policy expansion, persisted client diagnostics, raw private telemetry, live calls, deployment, or closure of the inherited 429 backlog.

Git-write: yes, one local commit; no push. Suggested subject: `test: cover playable rival turn recovery`.

Evidence tier: E2; documentation evidence is E0 within the same integrated slice.

Validation:

```bash
cd frontend
npm test
npm run lint
./node_modules/.bin/tsc --noEmit
npm run build

cd ../backend
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run ruff check .
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run mypy config game gamecore accounts catalog
env -u APPIMAGE -u APPDIR -u ARGV0 poetry run pytest
```

Stop if the 300-turn suite records any avoidable non-scoring action, exceeds 10 seconds, leaks private payloads, changes fallback ordering/reconciliation, introduces a new mypy diagnostic, or requires live provider evidence.

## Assumptions and non-goals

- Collins 2019 remains absolute and backend-owned.
- The five flag-off bootstrap pairs remain unchanged and free-only.
- No production deployment or scheduler work occurs.
- Judge cleanup is excluded because it is not causal.
- No unbeatable-AI research, ranked search engine, Slovak dictionary, Stripe/paid functionality, LM Studio, FrameNest copying, reopened-whole closure, new heavy dependency, or client-side candidate generator is included.

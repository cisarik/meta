Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-playable-variant
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice 3 of 4 (prompts / judge / turn pipeline)
Task identity: slice3-parameterize-prompts-per-variant
Task type: feature implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: 1e70d7608e43df6b7483186362f3168b17453e57
Implementation boundaries: this prompt
Independence required: no

Planning owner: ORCHESTRATOR
Accepted plan: `/home/agile/meta/projects/libretiles/05/00-slovak-playable-variant/01_report_01.md` Slice 3 contract
Prior results (evidence only):
- Slice 0 `d34d8b38` assets
- Slice 1 `3bb8c940` engine
- Slice 2 `1e70d760` Settings + session alphabet/points + PlacementSerializer Unicode
- Orchestrator accepted Slice 2. `get_ai_context` already sends `variant`, `tile_points`, `alphabet`, `lexicon_id`.

Combined implementation envelope: prohibited — Slice 3 only. Do not add catalog prompt migrations. Do not fork `/api/ai/move`. Do not change search caps, fallback, or NIM ids.

Recommended reasoning: High
Recommendation basis: English CORE SHA-256 is a hard gate. A factory that accidentally reformats whitespace will fail `prompts.test.ts` and regress the working English Nemotron path.
Escalation or downgrade gate: English CORE hash drifts; version ≠ `pfr-s2-core-1`; Slovak CORE names Collins as the lexicon; judge synthesizes invalid; a found Slovak rack completes as `genuine_no_move_pass`.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: 1e70d7608e43df6b7483186362f3168b17453e57
Baseline subject: feat(ui): persist game language and variant tile alphabet
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

================================================================
GOAL
================================================================

English move/judge prompts stay byte-identical. Slovak games get a parameterized CORE and judge that name the shipped Slovak lexicon, SSS tile values from the session snapshot, and Unicode board rows. The existing SSE orchestrator stays one route. A simulated Slovak turn with a legal scoring move must not terminate as `genuine_no_move_pass`.

Hard English pin (must remain):
- `MOVE_PROMPT_VERSION === "pfr-s2-core-1"`
- `sha256(MOVE_SYSTEM_PROMPT) === "c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60"`

================================================================
CHANGED-PATH ALLOWLIST
================================================================

- frontend/src/lib/prompts.ts
- frontend/src/lib/prompts.test.ts
- frontend/src/app/api/ai/move/route.ts
- frontend/src/app/api/ai/move/route.test.ts
- frontend/src/app/api/ai/judge/route.ts
- frontend/src/app/api/ai/judge/route.test.ts
- frontend/src/lib/ai-turn-simulation.test.ts

Optional only if the mock context type lives there and must carry `lexicon_id` / `variant` / `tile_points`:
- frontend/src/lib/ai-move-stream.ts (only if a type must be extended; do not change SSE event semantics)

No catalog migrations. No Settings/UI. No `variant_store.py` / dictionaries. No `services.py` unless you prove `get_ai_context` is missing a field already required by Slice 1 (it should already have them — do not touch backend if they are present).

================================================================
NEGATIVE AUTHORITY
================================================================

- No second SSE route.
- No `MOVE_PROMPT_VERSION` bump.
- No hash-gated Django prompt migration (0010/0011 stay).
- No paid models, JULS, ScrabGPT import, chrome i18n.
- No push. No second commit.
- Do not “fix” English exemplars Q/I — those stay in the English CORE bytes.

================================================================
MANDATORY READING
================================================================

- this prompt
- Slice 3 contract in `01_report_01.md`
- `frontend/src/lib/prompts.ts` entire file
- `frontend/src/lib/prompts.test.ts` hash gate
- `frontend/src/app/api/ai/move/route.ts` `composeMoveSystemPrompt` / `buildMoveUserPrompt` (~742)
- `frontend/src/app/api/ai/judge/route.ts` inline Collins system string (~253)
- `frontend/src/lib/ai-turn-simulation.test.ts` `SimBackend.handle` ai-context (~405) and pass/found scripts
- `.ap/AP_WORKER.md` report contract

Do not read `.env` / `.env.local`.

================================================================
D1 — Prompt factory (English identity)
================================================================

Introduce `moveSystemPromptFor(spec)` (name as you like).

```ts
export const MOVE_SYSTEM_PROMPT = moveSystemPromptFor(englishMoveSpec);
```

`englishMoveSpec` must reproduce today’s English string **exactly** (same newlines, same Q/J shed line, same RATE/QI exemplars). The existing hash test must pass unchanged.

Slovak spec:
- Opening line names Slovak / SSS / shipped Slovak lexicon — **must not** say Collins is the validity authority.
- Same MISSION / PASS-EXCHANGE truth / TOOL DISCIPLINE / BOARD / RACK / CONTEXT BOUNDARY / ANCHORS structure (keep the same seven priority headings so English tests that read `MOVE_SYSTEM_PROMPT` stay valid; Slovak prompt should contain the same heading names).
- STRATEGY: shed high-point SSS tiles (X / Ĺ / Ŕ / Ä / Ó), not Q/J.
- EXEMPLAR A: opening `AUTO` covering center (tiles A,U,T,O — all in SSS bag and in `slovak.txt`). Keep it as short as the English RATE example.
- EXEMPLAR B: rejection then pivot; **no Q/W**.
- Still tool-only: validateMove first, finishMove `{ready:true}`, pass/exchange not the model’s job.

`composeMoveSystemPrompt(searchProfile, spec?)`:
- default / english / `lexicon_id === "collins2019"` → wrap `MOVE_SYSTEM_PROMPT`
- `lexicon_id === "slovak"` → wrap the Slovak CORE
- SEARCH_PROFILE remains advisory delimiters; it cannot override tools or pass policy

`GRID_ROW` becomes `/^[\p{L}.]{15}$/u` (15 cells, not 15 bytes). `extractGridRows` must keep a row containing `Á`. `toUpperCase()` is fine if it preserves `Á`.

`buildMoveUserPrompt`:
- TILE VALUES from `context.tile_points` (or `context.ai_state` / top-level snapshot) when present
- English fallback remains the current hardcoded A–Z string **only** when snapshot points are missing (old mocks / English)
- Slovak snapshot must not print `Q=10` as if Q were in the bag

`formatRackMultiset`: if `ai_rack` is already spaced, do not double-space. If it is a concatenated NFC string of single letters, split by code point (current `split("")` is OK for BMP Slovak letters).

================================================================
D2 — Move route
================================================================

`/api/ai/move` stays one function. After `ai-context` fetch, choose spec from `context.lexicon_id` or `context.variant === "slovak"`. Pass snapshot `tile_points` into `buildMoveUserPrompt`.

Do not change tool schemas, playability probe, ranked rescue, fallback, or `completion_source` union. Those already work once the backend dictionary is Slovak.

If route tests assert the English system prompt text, keep them green; add one test that a slovak context does not send “Collins Scrabble Words (2019)” as the sole authority in the system prompt.

================================================================
D3 — Judge
================================================================

`judgeSystemPromptFor(spec)`:
- English export `JUDGE_SYSTEM_PROMPT` stays the current Collins text (existing tests match Collins sentences).
- Slovak names the shipped Slovak lexicon, conservative, no natural-usage override, same JSON schema.
- Replace the **inline** Collins string in `judge/route.ts` (~253) with the factory. Optional request field `lexicon_id` / infer from body; default English/Collins when absent.
- Exhaustion still HTTP 503. `parseJudgeResults` still rejects malformed output — never synthesize `valid: false`.

Existing English judge tests stay. Add: Slovak system/prompt does not claim Collins; 503 path still has no fabricated invalids.

================================================================
D4 — Slovak turn simulation
================================================================

In `ai-turn-simulation.test.ts`:
- Fake `ai-context` may include `variant: "slovak"`, `lexicon_id: "slovak"`, `tile_points` for SSS letters, `alphabet`.
- Add **one** deterministic Slovak found-rack turn: `legalMoves.length > 0` (e.g. AUTO through center) ⇒ terminal `completion_source` is a place path (`provider_candidate` | `repair_candidate` | `backend_witness_rescue` | `backend_ranked_candidate`), **never** `genuine_no_move_pass` / `genuine_no_move_exchange`.
- Do not weaken the English 300-turn suite.

Existing English found/pass/exchange scripts stay.

================================================================
VALIDATION
================================================================

cwd `frontend/`:

```bash
npx vitest run src/lib/prompts.test.ts src/lib/ai-turn-simulation.test.ts src/app/api/ai/judge/route.test.ts src/app/api/ai/move/route.test.ts
npm run lint
npx tsc --noEmit
```

================================================================
GIT
================================================================

Exactly ONE local commit on `main`.
Subject: `feat(ai): parameterize move/judge prompts per variant lexicon`
No push. Allowlist only.

================================================================
STOP
================================================================

- HEAD ≠ `1e70d7608e43df6b7483186362f3168b17453e57` or dirty foreign porcelain
- `./.ap/ap doctor` FAIL
- Plan Mode on
- SHA-256 of `MOVE_SYSTEM_PROMPT` ≠ quoted hex
- version ≠ `pfr-s2-core-1`
- Slovak CORE treats Collins as authority
- judge synthesizes invalid on malformed output
- Slovak found rack completes as `genuine_no_move_pass`
- second SSE route or catalog migration
- Settings/UI or dictionary assets edited

================================================================
UNTRUSTED-CONTENT / NETWORK
================================================================

Governing: this prompt + pinned `.ap`. Zero provider HTTP. No JULS. No `.env`.

================================================================
REPOSITORY GATE
================================================================

cwd `/home/agile/Projects/libretiles`
- HEAD `1e70d7608e43df6b7483186362f3168b17453e57`
- branch `main`
- porcelain empty
- `HEAD:.ap` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- `./.ap/ap doctor` PASS
- Native planning mode not-used

================================================================
REPORT
================================================================

Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Header exactly: ### Report for ORCHESTRATOR_CHAT

Echo once:
Logical whole identity: slovak-playable-variant
Worker session ordinal: 05
Worker exchange ordinal: 01

PASS only if D1–D4 + tests + one commit + English hash intact.
Phase-qualified result: implementation-PASS.
Start `1e70d760…`; end new SHA; allowlist files; vitest counts; quote the English CORE hash you measured; deviations; next step = Orchestrator reconciles; live-play (2 EN + 3 SK vs NIM) is a **later grant**, not this Worker; justification `new-mutation`; authority-expiry; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification.

This report grants no live-play, push, or closure authority.

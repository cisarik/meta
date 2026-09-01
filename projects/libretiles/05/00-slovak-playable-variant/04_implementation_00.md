Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-playable-variant
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice 2 of 4 (Settings game language + in-game alphabet UI)
Task identity: slice2-settings-variant-ui
Task type: feature implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: 3bb8c9409971d64c9b2ba208f89d489a10ed2914
Implementation boundaries: this prompt
Independence required: no

Planning owner: ORCHESTRATOR
Accepted plan: `/home/agile/meta/projects/libretiles/05/00-slovak-playable-variant/01_report_01.md` Slice 2 contract
Prior results (evidence only):
- Slice 0 `d34d8b38…` SSS assets + hunspell lexicon
- Slice 1 `3bb8c940…` per-variant engine; Orchestrator accepted. Residual carried into THIS slice: `PlacementSerializer` still `^[A-Z?]$` / `^[A-Z]$` (`serializers.py` ~271). Human `ValidateMoveSerializer` is DictField (OK). AI persist uses `ApplyAIMoveSerializer` → PlacementSerializer, so a Slovak `Á` apply would 400. Fix that here. Do not reopen engine cache/`isascii`.

Combined implementation envelope: prohibited — Slice 2 only. Do not parameterize CORE/judge (`prompts.ts`) or change `GRID_ROW`. That is Slice 3.

Recommended reasoning: High
Recommendation basis: persist migrate rewrite is easy to get wrong; rack/picker/points must follow the session, not Settings, or a live English game would flip alphabet when the dropdown changes.
Escalation or downgrade gate: migrate still short-circuits `version >= 1`; queue still hardcoded `english`; rack still A–Z only; you would need to edit `prompts.ts`.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: 3bb8c9409971d64c9b2ba208f89d489a10ed2914
Baseline subject: fix(engine): per-variant lexicon, alphabet, and scoring
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

================================================================
GOAL
================================================================

A player can choose English or Slovak in Settings. New AI games and new queue joins send that slug. An already-running game keeps its own `variant_slug` / snapshot alphabet / tile points. Chrome stays English.

After this commit:
- Persist `selectedVariantSlug` (`english` default), Zustand persist **version 2**, migrate rewrite as specified (not `if (version >= 1) return`).
- Settings has a premium two-card control (not a native `<select>`): labels **English** / **Slovak**. Description: tiles, bag, and lexicon; UI stays English.
- `api.createGame` accepts `variant_slug`. Play page sends `selectedVariantSlug` on create and on `joinHumanQueue` (stop hardcoding `"english"`).
- `GameState` types include `tile_points`, `alphabet`, `lexicon_id` (backend already sends them).
- `isPlausibleRack(rack, alphabet?)` accepts session letters + `?`. Fallback `/^[\p{L}?]$/u` when alphabet is missing. Never read Settings for rack membership. Call sites: `game/[id]/page.tsx`, `TileRack.tsx`.
- `BlankPicker` letters from `gameState.alphabet` (41 for Slovak), 7-column grid, English title “Choose a letter for blank tile”.
- `TILE_POINTS` stays the English fallback in `constants.ts`. `Tile` and `AIThinkingOverlay` prefer `gameState.tile_points` so `Á` shows 4, not 0.
- Invalid-word toast: Collins copy when `lexicon_id === "collins2019"` (or missing); else “Not in the Slovak lexicon”.
- `PlacementSerializer` accepts a single Unicode letter or `?` / `blank_as` Unicode letter (NFC). English A–Z still works. Add a backend test that `Á` / blank-as-`Á` pass the serializer.
- No live PATCH of `variant_slug`. No chrome i18n. No CORE hash change.

================================================================
CHANGED-PATH ALLOWLIST
================================================================

Frontend existing:
- frontend/src/hooks/useGameStore.ts
- frontend/src/hooks/useGameStore.test.ts
- frontend/src/app/settings/page.tsx
- frontend/src/app/play/page.tsx
- frontend/src/lib/api.ts
- frontend/src/lib/types.ts
- frontend/src/lib/rack.ts
- frontend/src/lib/constants.ts (only if a comment or export helper is required; do not change English point numbers)
- frontend/src/components/game/BlankPicker.tsx
- frontend/src/components/tiles/Tile.tsx
- frontend/src/components/tiles/TileRack.tsx (call-site of `isPlausibleRack` only)
- frontend/src/components/game/AIThinkingOverlay.tsx
- frontend/src/app/game/[id]/page.tsx (lexicon toast + rack/blank wiring)

Frontend new:
- frontend/src/lib/rack.test.ts

Backend (Slice 1 residual only):
- backend/game/serializers.py (`PlacementSerializer` letter / blank_as)
- backend/tests/test_api.py or `backend/tests/test_slovak_engine.py` (one apply/serializer test for `Á`)

Do not touch `Cell.tsx`, `Board.tsx`, `draw/[id]/page.tsx`, `prompts.ts`, `move/route.ts`, `judge/route.ts`, variant JSON, dictionaries, `services.py` engine, catalog.

If another path is required, stop BLOCKED.

================================================================
NEGATIVE AUTHORITY
================================================================

- No UI translation of Settings chrome, overlays, or buttons.
- No in-game language switch that mutates `GameSession`.
- No Slice 3 prompt/CORE/GRID_ROW work.
- No `isascii` / dictionary-cache revisit.
- No push. No second commit.
- No production deploy.

================================================================
MANDATORY READING
================================================================

- this prompt
- Slice 2 contract in `01_report_01.md`
- `frontend/src/hooks/useGameStore.ts` persist `version: 1` and `if (version >= 1) return`
- `frontend/src/hooks/useGameStore.test.ts` existing migrate tests (they call migrate with version `1` — keep budgets; add v2 cases)
- `frontend/src/app/settings/page.tsx` `SettingsPanel` / `ChoiceGrid` visual language
- `frontend/src/app/play/page.tsx` `createGame` / `joinHumanQueue`
- `frontend/src/lib/rack.ts`, `BlankPicker.tsx`, `Tile.tsx`, `AIThinkingOverlay.tsx`
- `frontend/src/app/game/[id]/page.tsx` ~228 Collins toast; `isPlausibleRack` ~533 / ~1488
- `backend/game/serializers.py` `PlacementSerializer`
- `.ap/AP_WORKER.md` report contract

Do not read `.env` / `.env.local`.

================================================================
D1 — Persist
================================================================

Add `selectedVariantSlug: "english" | "slovak"` and `setSelectedVariantSlug`.
Default `"english"`.
`partialize` includes it.
`version: 2`.

Exact migrate (locked):

```ts
migrate: (persistedState, version) => {
  const incoming = { ...((persistedState ?? {}) as Record<string, unknown>) };
  if (version < 1) {
    delete incoming.localAIContextLength;
    delete incoming.localAIReloadAfterTurn;
  }
  if (version < 2) {
    if (incoming.selectedVariantSlug !== "english" && incoming.selectedVariantSlug !== "slovak") {
      incoming.selectedVariantSlug = "english";
    }
  }
  return incoming as unknown as GameStore;
}
```

Tests:
- v1 persist without slug → english; `aiTimeout` / `aiMaxSteps` unchanged; no revived `localAIContextLength`
- v1 persist that somehow has `selectedVariantSlug: "slovak"` stays slovak
- garbage slug → english

================================================================
D2 — Settings control
================================================================

Premium panel **Game language** above or beside the thinking-time grid (same card chrome as `ChoiceGrid`: amber selected border, gold title).
Two cards:
- English — “Collins 2019 tiles and lexicon”
- Slovak — “SSS 100 tiles and Slovak lexicon”

English UI words only. Changing the control must not PATCH an open game.

================================================================
D3 — Create / join
================================================================

`api.createGame` body may include `variant_slug`.
Play page:
- `createGame(..., { ..., variant_slug: selectedVariantSlug || "english" })`
- `joinHumanQueue(token, { variant_slug: selectedVariantSlug || "english" })`

================================================================
D4 — Session-owned alphabet / points
================================================================

`GameState` optional/required fields matching backend snapshot (`tile_points` record, `alphabet` string[], `lexicon_id` string).

`isPlausibleRack(rack, alphabet?: readonly string[])`:
- length 1–7
- ≤2 `?`
- each tile is `?` or in `alphabet` if provided, else `/^[\p{L}?]$/u`
- never import the store Settings slug

`BlankPicker`: `useGameStore` `gameState?.alphabet`; fallback English A–Z only if alphabet missing (old sessions). 7 columns. Smaller buttons OK for 41 letters. Title stays English.

`Tile`: add optional `tilePoints?: Record<string, number>`. Resolve `tilePoints?.[letter] ?? TILE_POINTS[letter] ?? 0`. Board/rack parents pass `gameState.tile_points` when present.

`AIThinkingOverlay`: same preference for overlay candidate points.

Invalid-word toast in `game/[id]/page.tsx`:
- `lexicon_id === "slovak"` → “Not in the Slovak lexicon”
- else → existing Collins sentence

================================================================
D5 — PlacementSerializer residual
================================================================

Replace A–Z-only regex with a 1-character Unicode letter or `?` (letter) / Unicode letter (`blank_as`). NFC the value in validation. Keep blank_as required iff letter is `?`.

Test: serializer (or apply-ai-move with a mocked/auth fixture if cheaper) accepts `{letter:"Á"}` and `{letter:"?", blank_as:"Á"}`; still rejects `CH`, empty, `1`.

Do not loosen occupancy/row/col rules.

================================================================
VALIDATION
================================================================

cwd `frontend/`:

```bash
npx vitest run src/hooks/useGameStore.test.ts src/lib/rack.test.ts
npm run lint
npx tsc --noEmit
```

cwd `backend/` (serializer residual):

```bash
poetry run pytest tests/test_api.py tests/test_slovak_engine.py tests/test_slovak_variant.py tests/test_dictionary_validation.py -q
poetry run ruff check game/serializers.py
```

Do not need the full pytest matrix unless you touch more backend than the serializer.

================================================================
GIT
================================================================

Exactly ONE local commit on `main`.
Subject: `feat(ui): persist game language and variant tile alphabet`
No push. Allowlist only.

================================================================
STOP
================================================================

- HEAD ≠ `3bb8c9409971d64c9b2ba208f89d489a10ed2914` or dirty foreign porcelain
- `./.ap/ap doctor` FAIL
- Plan Mode on
- migrate still `if (version >= 1) return`
- queue still hardcoded `"english"`
- `isPlausibleRack` still `/^[A-Za-z?]$/`
- BlankPicker still hardcoded A–Z when `gameState.alphabet` has 41 letters
- `Á` still 0 points when snapshot has 4
- `PlacementSerializer` still A–Z only
- `prompts.ts` edited
- chrome translated

================================================================
UNTRUSTED-CONTENT / NETWORK
================================================================

Governing: this prompt + pinned `.ap`. Zero provider HTTP. No JULS. No `.env`.

================================================================
REPOSITORY GATE
================================================================

cwd `/home/agile/Projects/libretiles`
- HEAD `3bb8c9409971d64c9b2ba208f89d489a10ed2914`
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
Worker session ordinal: 04
Worker exchange ordinal: 01

PASS only if D1–D5 + tests + one commit. Phase-qualified result: implementation-PASS.
Start `3bb8c940…`; end new SHA; changed files vs allowlist; vitest/lint/tsc; backend serializer tests; deviations; next step = Orchestrator reconciles then issues Slice 3 to a FRESH Worker; justification `new-mutation`; authority-expiry; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification.

This report grants no Slice 3 authority.

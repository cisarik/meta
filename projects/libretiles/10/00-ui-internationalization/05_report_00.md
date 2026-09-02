### Report for ORCHESTRATOR_CHAT

1. logical whole `ui-internationalization`, Worker session ordinal 05, Worker exchange ordinal 01
2. status: PASS
3. phase-qualified result: implementation-PASS
4. start commit `e0d3b64cbccf1a1d9983ba5c394762f55961325a` · end commit `383011b389a9b3690647b6fa673060633572ab9d`
5. **PRIMARY** build-gate route. Exact `ss -tlnp | grep :3000` output: empty (grep exit 1; nothing listening). Build ran; `.next` was not contested.
6. Changed files:
   - `frontend/src/app/settings/page.tsx` — rival panel is a read-only `display_name`; player click/`updateMe` gone; catalog fetch, `resolveEligibleModelId`, repair write-back kept
   - `frontend/src/app/play/page.tsx` — label is catalog `display_name` (loading copy `Preparing game...`); `ai_prompt_id` omitted from `createGame`
   - `frontend/src/app/game/[id]/page.tsx` — prompt-preset surface removed; `"Choose rival"` / `"Initial"` gone; riders 1–2 wired; `selectedModelId` / `preferenceModelId` kept
   - `frontend/src/app/draw/[id]/page.tsx` — pill shows catalog `display_name`, else `humanizeModelId`
   - `frontend/src/components/game/ScorePanel.tsx` — prompt control and its props removed only
   - `frontend/src/hooks/useGameStore.ts` — `selectedPromptId` removed; persist 4→5; `selectedModelId` kept
   - `frontend/src/hooks/useGameStore.test.ts` — AC-PERSIST-5, AC-MODEL-KEPT; version sentinel 4→5
   - `frontend/src/lib/i18n/messages.{en,sk,cs,pl}.ts` — heading + three routeFailed keys; `aiPassBodyKey.message` deleted
   - `frontend/src/lib/i18n/GLOSSARY.md` — those keys
   - `frontend/src/lib/i18n/i18n.test.ts` — AC-HEADING-4, AC-ROUTEFAIL-4; rider 3 test no longer passes `message`
   - **Deleted:** `frontend/src/components/game/PromptCatalogModal.tsx`, `frontend/src/components/game/PromptPreviewModal.tsx`
7. **`selectedModelId` survives**
   - store field: `selectedModelId: string;` plus `setSelectedModelId` (`useGameStore.ts:37–38`, initial `""` at `:138–139`)
   - `partialize`: `selectedModelId: state.selectedModelId,` (`:319`)
   - `game/[id]/page.tsx:833`: `const preferenceModelId = selectedModelId || gameState.ai_model_id || "";`
   - `frontend/src/lib/ai-fallback.ts` is untouched (`git diff --name-only` empty for that path)
8. **No backend change.** `git diff --name-only` scoped to `backend/` is empty. No migration. `preferred_ai_model_id` and `is_selectable_model` were not edited. Player-click `api.updateMe` is gone; settings/play/home repair `updateMe` remains.
9. **Locked forks:** no provider or model added, removed, renamed, or reordered. Untouched: `provider-registry.ts`, `openai-compatible.ts`, `ibm-watsonx.ts`, `ai-runtimes.ts`, `backend/catalog/selection.py`, `README.md`, `AGENTS.md`, `prompts.ts` (including `MOVE_PROMPT_VERSION` / pinned SHA-256).
10. Persist: `version: 5`; `if (version < 5) { delete incoming.selectedPromptId; }`. A stored v4 payload with `selectedPromptId` migrates to v5 with that key absent; `selectedModelId`, `selectedVariantSlug`, and `uiLocale` are unchanged.
11. Pre-fix / post-fix:

    | Test | Pre-fix | Post-fix |
    |---|---|---|
    | AC-PERSIST-5 | `AssertionError: expected 4 to be 5` at `useGameStore.test.ts:222` | pass |
    | AC-MODEL-KEPT | `AssertionError: expected 4 to be 5` at `useGameStore.test.ts:249` | pass |
    | AC-HEADING-4 | `TypeError: fn is not a function` at `translate.ts:39` / `i18n.test.ts:433` | pass (sk: `Neplatné slovo!` / `Neplatné slová!`) |
    | AC-ROUTEFAIL-4 | `TypeError: fn is not a function` at `translate.ts:39` / `i18n.test.ts:475` | pass |
    | AC-EXHAUST4 | already existed | still pass |
12. Gates (PRIMARY, all eight):
    - mypy: `Success: no issues found in 83 source files`
    - ruff: `All checks passed!`
    - check: `System check identified no issues (0 silenced).`
    - pytest: `381 passed, 4 skipped in 215.04s (0:03:35)`
    - typecheck: exit 0
    - vitest: `378 passed | 3 skipped` (was ≥374 + 3 skipped; +4 new tests → 378; no deleted-component tests; no surviving test weakened)
    - lint: exit 0
    - build: exit 0; every route `ƒ`; zero `○` static routes (`/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`)
13. Commit `383011b389a9b3690647b6fa673060633572ab9d` pushed fast-forward `e0d3b64..383011b` to `origin/main`. Public readback: `git ls-remote origin refs/heads/main` = `383011b389a9b3690647b6fa673060633572ab9d` = `git rev-parse HEAD`.
14. User-facing English still in files this slice touched (S5 remainder unless noted):
    - **settings:** `Settings`, `Back to game`, `Starting...` / `New game`, `Choose the rival`, `Provider-diverse free rivals from the live catalog, newest first.`, `The rival catalog is empty. Seed the free catalog to play AI matches.`, `Account sync is unavailable right now. Settings still work locally on this device.`, `A free rival is selected on this device. Account preference could not be repaired yet.`, `Could not start a fresh game right now.`, `AI Thinking Time`, `Search Steps`, timeout/step/theme/shiny/premium copy (`Fast board read`, `Wood`, `Active`, `On`/`Off`, …)
    - **play:** `Libre Tiles`, `Choose the next board`, `Start a premium AI duel…`, `AI Match`, `Play the house`, `Use the current AI rival…`, `Preparing game...`, `Human Queue`, `Find a live opponent`, `Join the first waiting player…`, `Joining queue...`, `Slovak queue` / `English queue`, `Saved boards`, `Resume where you left off`, `AI and human games share one premium history surface.`, `Settings`, `Account`, `Unable to load your games.`, `Could not start an AI game.`, `Could not join the human queue.`, empty-catalog / variant-unavailable strings
    - **ScorePanel:** `Give up` / `Giving up...`, `Give up current game`, `Logout` / `Logging out...`, `Back to boards`, `Profile`, `You`, `vs`, `Settings`, `Games`, `Starting...` / `New game`
    - **draw:** `VS`
    - **game/[id]:** no leftover choose/prompt chrome; `aiError` / `toast.message` can still surface English from APIs or `describeAiMoveFailure` (not copy in this file). Status/toasts already keyed.
15. Deviations / not authorized to fix:
    - Settings title is still `Choose the rival` though the player cannot choose (kept as instructed).
    - Rival name in the header still navigates to settings (`showRivalPicker`); panel is read-only.
    - Play loading uses existing `Preparing game...`; `humanizeModelId` removed there as unused.
    - Settings 5-card skeleton collapsed to one pulse bar (no new copy).
    - Last-resort header name is `t("game.opponentFallback")` after removing unreachable `Choose rival`.
    - `/api/prompts` still ships (build lists `ƒ /api/prompts`); MOVE CORE untouched.
    - `game.ai.exploring` still interpolates a model **id**, not `display_name`.
    - `accountSyncAvailable` / `formatContextWindow` / `persistModelSelection` removed as dead after deleting the click handler.
16. Resolved Execution Issues / Near-Misses: deleting `persistModelSelection` briefly ate the Escape `useEffect` / `handleNewGame` header; restored by re-read before continuing. Residual risk: none.
17. Pre-Existing Failure Classification: none
18. Smallest next step: Orchestrator requests Cooperator rendered acceptance as batch B20 (settings read-only name, play/draw name-only, no prompt control, Admin still sets row 1).
19. report justification: new-mutation
20. Authority for Worker session 05 exchange 01 expires with this terminal report. Logical-whole closure: not-closed.
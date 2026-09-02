### Report for ORCHESTRATOR_CHAT

1. logical whole `ui-internationalization`, Worker session ordinal 06, Worker exchange ordinal 01
2. status: PASS
3. phase-qualified result: implementation-PASS
4. start commit `383011b389a9b3690647b6fa673060633572ab9d` · end commit `d40b230e8071f609f1a26fbea70106664326673a`
5. **PRIMARY** build-gate route. Exact `ss -tlnp | grep :3000` output: empty (grep exit 1; nothing listening; no PID). Build ran; `.next` was not contested.
6. Changed files:
   - `frontend/src/app/play/page.tsx` — lobby copy routed through the catalog (23 keys); F14 queue label via `variantDisplayName` + `play.humanQueue.queueFor`
   - `frontend/src/app/waiting/[id]/page.tsx` — waiting-room copy (10 keys); eyebrow reuses `play.humanQueue.eyebrow`; connect-failed reuses `game.ws.connectFailed`
   - `frontend/src/app/settings/page.tsx` — F10 only: rival panel title/description (2 keys). `rivalSectionRef` / `?focus=rival` left in place
   - `frontend/src/app/game/[id]/page.tsx` — F11 exploring interpolant; F12 dropped `showRivalPicker` / `onOpenRivalPicker`
   - `frontend/src/components/game/ScorePanel.tsx` — F12 removed those two props and the clickable control; rival name stays as static text
   - `frontend/src/lib/i18n/messages.{en,sk,cs,pl}.ts` — `nav.*`, `play.*`, `queue.*`, `settings.rival.*`
   - `frontend/src/lib/i18n/GLOSSARY.md` — those keys; one line that `play.humanQueue.queueFor` takes a display name, never a slug (uii-01-F14)
   - `frontend/src/lib/i18n/i18n.test.ts` — AC-QUEUE-VARIANT, AC-QUEUE-UNKNOWN, AC-PLAY-4, AC-QUEUE-ROOM-4
7. **uii-01-F14 shape:** slug-keyed lookup that reuses `VARIANT_NAME_KEYS` through the already-exported `variantDisplayName`. The page builds a synthetic `VariantSummary` `{ slug, display_name: slug, language_code: null, readiness: "playable" }` from `selectedVariantSlug || "english"` and does not fetch the variant list on mount. Smallest correct: `GameLanguagePanel.tsx` is locked, the table is not duplicated, and the four installed slugs hit catalog keys. A fifth variant cannot revive "English queue" because there is no `=== "slovak" ? … : "English queue"` branch; an unknown slug falls through to `display_name` (here the slug itself) and never to another variant's name.
8. **uii-01-F11:** `game.ai.exploring` now receives `gameState.ai_model_display_name` when `preferenceModelId` matches `gameState.ai_model_id`, else `humanizeModelId(preferenceModelId)`, else the id as last resort. `preferenceModelId` is still `selectedModelId || gameState.ai_model_id || ""` and still the first argument of `buildFallbackQueue` / `fallbackQueueForCatalogFailure` / `aiMoveRequestBody` — UNCHANGED.
9. **uii-01-F12:** removed `showRivalPicker` and `onOpenRivalPicker` from `ScorePanel` (interface, defaults, control) and the two props from `game/[id]/page.tsx`. The rival name still renders as `<span className="shrink-0 uppercase text-white">{opponentLabel}</span>`. `settings/page.tsx` `rivalSectionRef` and `?focus=rival` were left alone as instructed; that focus path is now unreachable from the header.
10. **uii-01-F10:** title `settings.rival.title` ("Your rival" / "Tvoj súper" / "Tvůj soupeř" / "Twój rywal"); description `settings.rival.description` ("The administrator picks the rival for new games." and the three authored Slavic forms).
11. Pre-fix / post-fix:

    | Test | Pre-fix | Post-fix |
    |---|---|---|
    | AC-QUEUE-VARIANT | `TypeError: fn is not a function` at `translate.ts:39` / `i18n.test.ts:538` (`queueLabel` → `play.humanQueue.queueFor`) | pass |
    | AC-QUEUE-UNKNOWN | `TypeError: fn is not a function` at `translate.ts:39` / `i18n.test.ts:538` | pass (`display_name` "Magyar") |
    | AC-PLAY-4 | `AssertionError: expected undefined to be 'Choose the next board'` at `i18n.test.ts:620` | pass |
    | AC-QUEUE-ROOM-4 | `TypeError: fn is not a function` at `translate.ts:39` / `i18n.test.ts:639` | pass |
    | AC-EXHAUST4 | already existed | still pass |
12. Gates (PRIMARY, all eight):
    - mypy: `Success: no issues found in 83 source files`
    - ruff: `All checks passed!`
    - check: `System check identified no issues (0 silenced).`
    - pytest: `381 passed, 4 skipped in 214.78s (0:03:34)`
    - typecheck: exit 0
    - vitest: `382 passed | 3 skipped` (was 378 + 4 new tests)
    - lint: exit 0
    - build: exit 0; every route `ƒ`; zero `○` static routes (`/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`)
13. Commit `d40b230e8071f609f1a26fbea70106664326673a` pushed fast-forward `383011b..d40b230` to `origin/main`. Public readback: `git ls-remote origin refs/heads/main` = `d40b230e8071f609f1a26fbea70106664326673a` = `git rev-parse HEAD`.
14. No authored string was changed. `play.error.variantUnavailable` is the longest; it renders in the play-page footer error strip (`text-center text-sm text-rose-400` inside `max-w-[1020px]`). It should wrap as a paragraph; rendered fit is Cooperator-owned (batch B22). Slavic colon-labels (`Front:` / `Fronta:` / `Kolejka:`) are inert for every variant, including a fifth.
15. User-facing English still in the two lobby files:
    - **play/page.tsx:** `err.message` passthrough from the API in history load, AI start, and queue join; catalog `display_name` on the AI pill; `providerBadgeLabel(...)` on that pill. `GameHistoryPanel` is rendered here but its copy is not in this file (S7).
    - **waiting/[id]/page.tsx:** `err.message` passthrough from the API. The hourglass is an emoji, not copy. `game.ws.connectFailed` has no trailing period versus the old hardcoded `"Realtime connection failed."` — accepted as instructed.
16. Deviations / risks / missing evidence: none beyond item 17. `?focus=rival` is now a dead inbound link; not removed. No browser rendered check (no browser authority). Visible context usage exceeded 70% of the session window (large mandatory reading plus four catalogs and two full pages); the candidate was still completed against repository evidence, not compacted memory.
17. Resolved Execution Issues / Near-Misses: putting `useT()`'s `t` in the waiting-room `useEffect` deps would recreate the function every render and tear down the websocket on every state update. Cause: `useT` returns a fresh closure each render. Resolution: effects use module-level `t(locale, key)` with `locale` (a string) in the dependency list; JSX still uses `useT`. Residual risk: none on this page; the same `useT`-in-deps pattern already exists on `game/[id]/page.tsx` and was not in scope to change.
18. Pre-Existing Failure Classification: none
19. Smallest next step: Orchestrator requests Cooperator rendered acceptance as batch B22 (`/play` and `/waiting/[id]` in all four locales, Czech/Polish queue label, rival name no longer clickable, settings rival panel copy).
20. report justification: new-mutation
21. Authority for Worker session 06 exchange 01 expires with this terminal report. Logical-whole closure: not-closed.

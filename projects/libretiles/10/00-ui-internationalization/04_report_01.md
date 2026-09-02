### Report for ORCHESTRATOR_CHAT

1. logical whole `ui-internationalization`, Worker session ordinal 04, Worker exchange ordinal 02
2. status: **PASS**
3. phase-qualified result: **implementation-PASS**
4. start commit: `e421c6690f091203a60636b3aebaeec71e7fba69`  
   end commit: `e0d3b64cbccf1a1d9983ba5c394762f55961325a`
5. continuity strings, verbatim:  
   1. `game.lexicon.czech` (cs) = `Není v českém lexikonu`  
   2. `game.toast.aiExchanged` (pl) = `AI wymieniło płytki`  
   3. `game.status.yourTurn` (sk) = `Tvoj ťah`
6. **PRIMARY route.** Immediately before `npm run build`, `ss -tlnp | grep :3000` printed nothing and the command fell through to `PORT_3000_FREE`.
7. changed files:  
   - `messages.en.ts` / `.sk.ts` / `.cs.ts` / `.pl.ts` — game-screen keys, four parameterized functions, and the two selection helpers  
   - `GLOSSARY.md` — key table plus the `game.lexicon.*` / `lexicon_id` note; terminology table untouched  
   - `i18n.test.ts` — AC-LEX-4, AC-LEX-UNK, AC-TOAST-DISC, AC-GAME-TERM  
   - `page.tsx` — **72** catalog lookups (65 `t("…")`, 5 `tf("…")`, 2 helper-selected keys), including reused `auth.tab.login` and `controls.play`  
   - `Board.tsx` — one word, `{t("board.zoomNoun")}`
8. **uii-01-F09:** added optional `passKind: "pass" | "exchange"` on the existing `ai_pass` toast. That is the smaller change: the overlay timeout already treats pass and exchange as `type === "ai_pass"` (4200 ms); splitting types would have widened that union. Proof that prose is not load-bearing: `ToastOverlay` calls `t(aiPassBodyKey({ passKind: toast.passKind }))`, and `aiPassBodyKey` reads only `passKind` — never `message`. AC-TOAST-DISC still supplies the Slovak title `AI vymenilo písmená`, which contains no `exchanged`.
9. **uii-01-F08:** `lexiconRejectionKey` switches on `collins2019` / `slovak` / `czech` / `polish` and returns `game.lexicon.unknown` for any other value, including `undefined` / `null` / `""`. No parameterized “Not in ${lexicon}” sentence.
10. pre-fix / post-fix:

    | test | pre-fix | post-fix |
    |---|---|---|
    | AC-LEX-4 | against the ternary: `expected 'Not in Collins Scrabble Words 2019' not to contain 'Collins'` | PASS |
    | AC-LEX-UNK | `expected 'game.lexicon.collins2019' to be 'game.lexicon.unknown'` | PASS |
    | AC-TOAST-DISC (exchange) | `expected 'game.toast.aiPassedBody' to be 'game.toast.aiExchangedBody'` (Slovak `AI vymenilo písmená`, no `exchanged`) | PASS |
    | AC-TOAST-DISC (pass) | already selected pass body under the substring check | PASS |
    | AC-GAME-TERM | before keys: `the given combination of arguments (undefined and string) is invalid for this assertion` at `toContain("kameny")` | PASS |
    | AC-EXHAUST4 | already passing; kept passing with the new keys | PASS |

    First vitest run (tests only): `lexiconRejectionKey is not a function` / `aiPassBodyKey is not a function` / `expected undefined to be 'AI vymenilo písmená'`. The table above is the run against the live ternary and substring helpers.

11. eight gates:  
    - backend mypy: `Success: no issues found in 83 source files`  
    - backend ruff: `All checks passed!`  
    - backend check: `System check identified no issues (0 silenced).`  
    - backend pytest: `381 passed, 4 skipped in 214.64s (0:03:34)`  
    - frontend typecheck: exit 0  
    - frontend vitest: **374 passed | 3 skipped** (377)  
    - frontend lint: exit 0  
    - frontend build: exit 0; every route `ƒ`; **zero `○` static routes** (`/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`)
12. commit `e0d3b64cbccf1a1d9983ba5c394762f55961325a` on `main`; non-force push `e421c66..e0d3b64  main -> main`  
    `git ls-remote origin refs/heads/main` → `e0d3b64cbccf1a1d9983ba5c394762f55961325a`  
    `git rev-parse HEAD` → `e0d3b64cbccf1a1d9983ba5c394762f55961325a`
13. strings / overflow (named, not changed):  
    - Polish **`Błąd uwierzytelnienia rywala`** and **`Nieprawidłowe ułożenie`** in toast/modal titles  
    - Slovak/Czech **`AI si obnovilo zásobník a spotrebovalo ťah.`** in the `ai_pass` subtitle  
    - Czech **`Vyber kameny na výměnu`** in `TurnStatusNotice`  
    - `game.ws.authExpired` / `game.ws.invalidSession` are long sentences in a bottom toast  
    - `window.confirm` give-up copy is long; OK/Cancel remain browser chrome
14. user-facing English still in `page.tsx` other than the three S4 deletions (`Choose rival`, `Initial`, `Could not switch AI prompt right now.`):  
    - heading **`Invalid Word` / `Invalid Words!`** (`Invalid Word{(toast.words?.length ?? 0) > 1 ? "s" : ""}!`) — no catalog key was authored  
    - **`AI route failed (${status})`** and its HTML/preview variants in `getStreamStartError`  
    - `" vs "` separator (glossary decision; only the `"Waiting"` fallback is localized)  
    Not copy / not this slice: SVG `path d`, `Content-Type`, toast ids, LayoutGroup id, `console.error("AI move failed:")`, telemetry `humanState: "providers exhausted"`. Incoming provider diagnostics still matched in English inside `normalizeAIBlocker`; the **displayed** title/body come from the catalog.
15. deviations / missing evidence:  
    - Selection helpers live in `messages.en.ts` so tests do not import the client page. `aiPassBodyKey` still *accepts* an unused `message` field so AC-TOAST-DISC can pass the Slovak title; the implementation does not read it.  
    - Rendered overflow was not measured (no browser authority).  
    - Context-pressure: not independently measured; not reported as >70%.
16. Resolved Execution Issues / Near-Misses: exchange 01 stopped on port 3000 as a preflight. Cause: Orchestrator sequencing. Resolution: this exchange scoped that check to the build gate; the port was free, so the primary route ran. Residual risk: none for this commit.
17. Pre-Existing Failure Classification: none
18. smallest next step: Cooperator rendered pass of the game screen in `sk` / `cs` / `pl`, especially the invalid-word toast (English `Invalid Word(s)!` heading still showing), the lexicon line on a Czech/Polish game, and an AI exchange toast; then slice S4 owns the header/model picker leftovers.
19. report justification: new-mutation
20. Authority expired with this report. I will take no further action without a new complete prompt.

Logical-whole closure: not-closed.
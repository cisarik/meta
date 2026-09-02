You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S8 — localize the saved-boards history surface and make its dates follow the locale
Implementation authority: explicit
Independence required: no
Reasoning recommendation: medium. Basis — volume string extraction into a seven-times exercised catalog
  contract, plus one correction (`uii-01-F03`) whose fix is a one-argument change whose CORRECTNESS has
  already been measured for you in section 5.
Report justification: new-mutation
Context-pressure rule: report visible context usage if it exceeds 70%.

=====================================================================
1. REPOSITORY GATE
=====================================================================
Repository checkout topology: standalone checkout
Repository identity: https://github.com/cisarik/libretiles
Working directory: /home/agile/Projects/libretiles
Expected branch: main
Working-copy topology: canonical checkout.

  git rev-parse HEAD                     -> 4bf436581c1b6382183411259e25c6a409b7d54f
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> 4bf436581c1b6382183411259e25c6a409b7d54f

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — this Next.js version has breaking changes versus
   your training data. The installed docs ARE present at `frontend/node_modules/next/dist/docs/`.
   ⛔ ALSO KNOW THIS, discovered and reproduced last slice: an App Router `page.tsx` may export ONLY the
   Next.js-enumerated set (`default`, `config`, `metadata`, `generateMetadata`, `revalidate`, ...). Any
   other named export from a page file is a `tsc` error. Neither file you are changing is a page file, so
   it does not bind you — but do not add an export to a page file if you find yourself tempted.
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. frontend/src/lib/i18n/GLOSSARY.md — the terminology contract, authority for this slice
6. frontend/src/lib/i18n/messages.en.ts and messages.sk.ts — the shape you extend and the source of the
   three keys section 4 tells you to REUSE
7. frontend/src/components/game/GameHistoryPanel.tsx — IN FULL, ~400 lines
8. frontend/src/components/game/GameHistoryModal.tsx — IN FULL, ~124 lines

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Localize the saved-boards experience into all four locales, and correct `uii-01-F03` for the one date
call site in this surface so that a Slovak, Czech or Polish player sees a date in their own language
instead of an American one.

=====================================================================
4. ACCEPTED DECISIONS AND THREE KEYS TO REUSE
=====================================================================
D1  Four locales: en, sk, cs, pl. A key missing from any catalog is a `npm run typecheck` error.
D2  Informal register in all three Slavic locales: sk and cs `ty`, pl 2nd person singular.
D3  Terminology from GLOSSARY.md. saved board / match: sk `partia`, cs `partie`, pl `partia`.
    rival: sk `súper`, cs `soupeř`, pl `rywal`. move: sk `ťah`, cs `tah`, pl `ruch`.
    `AI` stays untranslated.
D4  REUSE these three existing keys instead of authoring duplicates. Verified present in all four
    catalogs at this commit:
```text
    modal heading "Games"      -> header.games          sk "Partie"
    modal button  "Close"      -> game.blocker.close    sk "Zavrieť"
    row hint      "Your turn"  -> game.status.yourTurn  sk "Tvoj ťah"
```
D5  These are NOT copy and must NOT be given keys:
      every emoji in `FILTER_OPTIONS` and `OUTCOME_META` — 🤖 🤝 🗂️ ⏳ 🎮 🏆 📉 🚪 🪫
      `item.opponent_label` — a rival or username identity from the server
      `item.game_end_reason` — a backend enum string; see section 6.4 for how it is handled
      the `"vs_ai"` / `"vs_human"` / `"all"` filter VALUES, and every `className`

=====================================================================
5. uii-01-F03 — THE FIX IS ONE ARGUMENT, AND ITS CORRECTNESS IS ALREADY MEASURED
=====================================================================
`GameHistoryPanel.tsx:70-79` `formatUpdatedAt` calls
`new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", hour: "numeric", minute: "2-digit" })`.
A Slovak interface therefore renders `Sep 2, 4:35 PM`.

**Do NOT hand-build month names.** The Orchestrator measured `Intl` against this exact field set with
Node in this repository, and it produces correct Slavic forms including the GENITIVE month and a 24-hour
clock:

```text
locale   month:long,day,year          month:short,day,hour,minute
en-US    September 2, 2026            Sep 2, 4:35 PM
sk       2. septembra 2026            2. 9., 16:35
cs       2. září 2026                 2. 9. 16:35
pl       2 września 2026              2 września -> 2 wrz, 16:35
```

`2. septembra` is the genitive and is what a Slovak speaker expects in a date; `2. september` would read
wrong. That is exactly why the ledger's correction direction says to prefer `Intl` over hand-built
strings, and it is now verified rather than assumed.

THE CHANGE:
  - `formatUpdatedAt` takes a `locale: Locale` parameter and passes it to `Intl.DateTimeFormat`;
  - map `"en"` to `"en-US"` and pass `"sk"`, `"cs"`, `"pl"` through unchanged. **The mapping matters:**
    it keeps today's English output byte-identical while fixing the other three, so this correction can
    never be blamed for an English rendering change;
  - the caller resolves the locale with `useLocale()` and passes it in. `formatUpdatedAt` is a
    module-level function, so it must NOT call a hook;
  - its `"Unknown"` fallback for an unparseable date becomes a catalog key.

=====================================================================
6. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
Twenty-nine new keys. Translation is Orchestrator work in this project by Cooperator decision; no Worker
translates. If you believe a string is wrong or will overflow, NAME it in the report — do not change it.

--- 6.1 area `history` — filters, sort, and the panel shell ---
key                       en                  sk                    cs                    pl
history.filter.ai         AI                  AI                    AI                    AI
history.filter.human      Human               Ľudia                 Lidé                  Ludzie
history.filter.all        All                 Všetko                Vše                   Wszystko
history.sort.recent       Recent              Najnovšie             Nejnovější            Najnowsze
history.refresh           Refresh             Obnoviť               Obnovit               Odśwież
history.loading           Loading games       Načítavam partie      Načítám partie        Wczytuję partie
history.empty.title       No games in this filter yet
                          sk V tomto filtri ešte nie sú žiadne partie
                          cs V tomto filtru ještě nejsou žádné partie
                          pl W tym filtrze nie ma jeszcze żadnych partii
history.empty.body        Start a new board and it will show up here with premium paging, result badges, and quick resume links.
                          sk Spusti novú partiu a objaví sa tu s prémiovým stránkovaním, odznakmi výsledku a rýchlym pokračovaním.
                          cs Spusť novou partii a objeví se tu s prémiovým stránkováním, odznaky výsledku a rychlým pokračováním.
                          pl Rozpocznij nową partię i pojawi się tu z premium stronicowaniem, odznakami wyniku i szybkim powrotem.
history.noneYet           No saved boards yet Žiadne uložené partie Žádné uložené partie  Brak zapisanych partii
history.unknownDate       Unknown             Neznáme               Neznámé               Nieznane

⚠ `history.filter.ai` is `AI` in all four locales by decision D3. That is not a copy-paste error.

--- 6.2 area `history` — the table columns ---
key                       en        sk         cs        pl
history.col.rival         Rival     Súper      Soupeř    Rywal
history.col.mode          Mode      Režim      Režim     Tryb
history.col.result        Result    Výsledok   Výsledek  Wynik
history.col.score         Score     Skóre      Skóre     Wynik
history.col.moves         Moves     Ťahy       Tahy      Ruchy
history.col.updated       Updated   Zmenené    Změněno   Zmienione

⚠ Polish `history.col.result` and `history.col.score` are BOTH `Wynik`. That is correct Polish — the
language uses one word for both here — and the two columns are visually distinct by position. Do not
invent a false distinction.

--- 6.3 area `history` — outcome badges ---
key                       en            sk             cs             pl
history.outcome.waiting   Waiting       Čaká sa        Čeká se        Oczekiwanie
history.outcome.active    In progress   Prebieha       Probíhá        W toku
history.outcome.won       Won           Vyhral si      Vyhrál jsi     Wygrałeś
history.outcome.lost      Lost          Prehral si     Prohrál jsi    Przegrałeś
history.outcome.draw      Draw          Remíza         Remíza         Remis
history.outcome.gaveUp    Gave up       Vzdal si sa    Vzdal jsi se   Poddałeś się
history.outcome.abandoned Abandoned     Opustená       Opuštěná       Porzucona
history.outcome.unknown   Unknown       Neznámy        Neznámý        Nieznany

--- 6.4 area `history` — row hints and mode labels ---
key                       en             sk               cs               pl
history.mode.ai           AI duel        AI duel          AI duel          Duel z AI
history.mode.human        Human duel     Duel s človekom  Duel s člověkem  Duel z człowiekiem
history.hint.waitingRoom  Waiting room   Čakárňa          Čekárna          Pokój oczekiwania
history.hint.boardReady   Board ready    Partia je pripravená  Partie je připravená  Partia gotowa
history.open              Open           Otvoriť          Otevřít          Otwórz
history.current           Current        Aktuálna         Aktuální         Aktualna

⚠ `history.hint.boardReady` is the FALLBACK in
`item.is_my_turn ? "Your turn" : item.status === "waiting" ? "Waiting room" : item.game_end_reason || "Board ready"`.
`item.game_end_reason` is a BACKEND ENUM STRING such as `BAG_EMPTY_AND_PLAYER_OUT`. Leave that
passthrough exactly as it is — localizing backend enums needs a keyed mapping and is not authorized here.
Localize only the three literals around it and reuse `game.status.yourTurn` for the first.
NAME the enum passthrough in your report as a leftover so it is on the record.

--- 6.5 area `history` — pagination, TWO parameterized keys ---
history.pageOf          params { page: number; total: number }
  en (p) => `Page ${p.page} of ${p.total}`
  sk (p) => `Strana ${p.page} z ${p.total}`
  cs (p) => `Strana ${p.page} z ${p.total}`
  pl (p) => `Strona ${p.page} z ${p.total}`
history.showing         params { from: number; to: number; total: number }
  en (p) => `Showing ${p.from}-${p.to} of ${p.total} games`
  sk (p) => `Zobrazené ${p.from}-${p.to} z ${p.total}`
  cs (p) => `Zobrazeno ${p.from}-${p.to} z ${p.total}`
  pl (p) => `Pokazane ${p.from}-${p.to} z ${p.total}`

⚠ The Slavic forms DROP the trailing noun that English carries ("of N games" -> "z N"). That is
deliberate: keeping it would require `partií` / `partií` / `partii` in the genitive plural, which is
correct for 5+ but wrong for 2-4, and the number is variable. Dropping it is grammatical at every count
and the surrounding panel already says what is being counted. Do not add the noun back.

`history.pageOf` also replaces the `"Page 1"` fallback rendered when `data` is null: call it with
`{ page: 1, total: 1 }` rather than adding a separate key.

--- 6.6 area `history` — the two plain pagination buttons ---
key                       en          sk           cs          pl
history.prev              Previous    Predošlá     Předchozí   Poprzednia
history.next              Next        Ďalšia       Další       Następna

--- 6.7 GameHistoryModal — one new key, two reuses ---
key                       en                                                          sk
history.modal.subtitle    Review past boards, switch between AI and human games, and jump back in fast.
                          sk Prezri si staré partie, prepínaj medzi AI a ľuďmi a rýchlo sa vráť do hry.
                          cs Prohlédni si staré partie, přepínej mezi AI a lidmi a rychle se vrať do hry.
                          pl Przejrzyj stare partie, przełączaj się między AI i ludźmi i szybko wróć do gry.
REUSE: the `Games` heading -> `header.games`; the `Close` button -> `game.blocker.close`.

--- 6.8 GLOSSARY.md ---
Add all twenty-nine keys to the key table in the style the file already uses. Do not change the
terminology table. Add one line recording that `history.showing` and `history.pageOf` deliberately drop
the counted noun in the Slavic locales, with the genitive-plural reason, and one line recording that
`item.game_end_reason` remains an unlocalized backend enum.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/components/game/GameHistoryPanel.tsx
  frontend/src/components/game/GameHistoryModal.tsx
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts

No file is created and none is deleted. If a gate fails in a file NOT on this list, STOP and report it
rather than editing that file.

⚠ `GameHistoryPanel` is rendered by BOTH `app/play/page.tsx` and `GameHistoryModal`. Neither caller is on
the allowlist. If localizing a string would force a prop-signature change that requires editing a caller,
STOP and report which string and why — do not edit the caller.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- `frontend/src/components/game/ProfileModal.tsx`. It has ~27 strings and the OTHER `uii-01-F03` date
  call site at `:22`. It is the next slice. Do not touch it, and do not "fix both date sites while you
  are here" — the two sites are independent functions in independent files.
- `frontend/src/app/play/page.tsx`, `game/[id]/page.tsx`, `settings/page.tsx`, `waiting/[id]/page.tsx`,
  `draw/[id]/page.tsx`, `app/page.tsx`. All already localized.
- `frontend/src/components/game/AIThinkingOverlay.tsx`. Already localized except `{humanState}`, which
  STAYS ENGLISH pending the enum-keyed telemetry slice. `AC-NO-TELEMETRY-KEY` asserts no catalog key
  contains `providers exhausted`, `dead rack` or `legal rescue`; do not defeat it.
- `frontend/src/lib/types.ts`, `ai-move-stream.ts`, `api/ai/move/route.ts`, `prompts.ts` and its pinned
  SHA-256. Locked fork 2 plus the telemetry deferral.
- `frontend/src/lib/constants.ts` — TW/DW/TL/DL is the BOARD, not copy.
- `frontend/src/lib/api.ts`. Its 401 branch is a security property.
- `frontend/src/proxy.ts`, `security-headers.ts`. The nonce CSP is a later slice.
- `frontend/src/lib/i18n/locales.ts`, `plural.ts`, `translate.ts`, `LocaleProvider.tsx`, `index.ts`.
  You add catalog KEYS, not machinery. Do NOT add a fourth plural function — section 6.5 explains why
  the counted-noun problem is solved by dropping the noun instead.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- Anything under `backend/`. Django localization is a later slice, and `game_end_reason` is a backend
  enum whose localization is explicitly NOT authorized here.
- `frontend/package.json` and `package-lock.json`. NO new dependency. In particular do NOT add a date
  library — `Intl` is built in and section 5 proves it produces the correct forms.
- Do not bump the persist version. Do not add aria-label, role, or alt (uii-01-F02, later slice).
- Do not reformat, reorder imports in, or "tidy" anything beyond the named edits.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files.

=====================================================================
9. COMMANDS AND EXECUTION ROUTE
=====================================================================
Allowed, from frontend/: npm run typecheck, npx vitest run, npx vitest run <file>, npm run lint,
  npm run build.
Allowed, from backend/: the four gates below, ONLY via the bounded deviation, to prove you did not break
  the backend. You are NOT authorized to change any backend file.

BOUNDED EXECUTION DEVIATION, mandatory and task-specific.
  Declared route that could NOT be used: `poetry run ...`, as documented in AGENTS.md.
  Why: the Cursor AppImage environment intercepts `python*` through inherited APPIMAGE / ARGV0 /
    APPDIR / PYTHONHOME variables.
  Exact alternate, from backend/:
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
  Evidence class: reproduced-dynamic. Bounded authority: these four commands only.
  Stopping condition: if the alternate route also fails to resolve the in-project virtualenv, STOP and
    report; do not substitute ambient python, python3, or poetry run.

TRAP: `addopts = "-q"` is set. Do NOT pass another `-q`; use plain `-m pytest` and quote the summary.
TRAP: run mypy on the FULL documented scope.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. `npm run build` and `npm run dev` share
`frontend/.next`. Immediately before `npm run build`, and not before, run `ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, complete all eight gates, commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`. Run the
    other SEVEN gates, which are all safe with a dev server live. Leave the candidate UNCOMMITTED,
    report `status: PARTIAL`, quote the exact `ss` output with the PID, and state that the only
    remaining action is the build gate plus the commit.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`. That pattern matches the Cooperator's
  own development server. You may kill nothing in this slice.
Name the route you took and quote the `ss` output that decided it.

Forbidden commands: any git write beyond section 11, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote`
  reads, any process kill.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

=====================================================================
10. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: 29 keys x 4 locales plus a behavioural correction to date formatting that changes
  what three of four locales render; user-visible; no trust boundary, no durable data, no credential, no
  production effect. Rollback is `git revert` of one commit.
Combined implementation envelope: allowed
Independent acceptance: not-required. Evidence is NON-INDEPENDENT. Rendered acceptance is
  Cooperator-owned.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: frontend/src/lib/i18n/i18n.test.ts
New causal regression: the locale-aware date formatting and the noun-dropping pagination keys
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `390 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-DATE-LOCALE   THE uii-01-F03 REGRESSION TEST AND THE MOST IMPORTANT ONE HERE. For a fixed
                   timestamp, `formatUpdatedAt` must produce output that DIFFERS between `en` and each of
                   `sk`, `cs`, `pl`; must contain NO `AM`/`PM` marker in the three Slavic locales; and
                   must be byte-identical to today's output for `en`. Assert the `en` value literally so
                   the mapping to `"en-US"` is pinned. This must fail against the hardcoded `"en-US"`.
  AC-HISTORY-4     Every `history.col.*` and `history.outcome.*` key renders the exact authored string in
                   all four locales.
  AC-PAGING-4      `history.pageOf` and `history.showing` interpolate correctly in all four locales, and
                   the sk / cs / pl forms of `history.showing` do NOT contain the English word `games`.
  AC-POLISH-DUP    A deliberate assertion that Polish `history.col.result` and `history.col.score` are
                   BOTH `Wynik`. This pins an intentional duplication so a future reader does not
                   "correct" it into a false distinction, and it fails loudly if either is changed.
  AC-EXHAUST4 and AC-NO-TELEMETRY-KEY  ALREADY EXIST and must keep passing. Do not weaken either.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted. Do not be the first.

=====================================================================
11. GIT AUTHORITY
=====================================================================
On the PRIMARY route only, after all eight gates are green: exactly one commit and one push.
On the FALLBACK route: NO commit, NO push.

  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): localize the saved-boards history and its dates
     Body: that `uii-01-F03` is corrected for this call site by passing the active locale to `Intl`, that
     `en` maps to `en-US` so English output is unchanged, which existing keys were reused, and that no
     dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     4bf436581c1b6382183411259e25c6a409b7d54f. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.

FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails in a file outside the section 7
allowlist; localizing a string would force an edit to a caller; a hook would have to be called from
module scope; you conclude a new dependency or a date library is required; the backend gates fail;
`git ls-remote` shows main advanced; any instruction here conflicts with AGENTS.md, .ap/AP.md, or
observed repository truth; or you find yourself weakening an existing test.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 09, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, and the count of strings routed through the catalog per file
 7. THE uii-01-F03 CORRECTION: the new signature of `formatUpdatedAt`, how the locale reaches it without
    a hook in module scope, and the literal `en` output you asserted so the mapping is pinned
 8. WHICH EXISTING KEYS you reused rather than duplicating
 9. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
10. gate results — eight on the primary route, seven plus a named omission on the fallback — with the
    pytest summary quoted verbatim and the vitest counts
11. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
12. any string you believe is wrong, or any container you believe a Slavic string will overflow — NAME
    it, do not change it. The history table has six columns in a dense grid and
    `history.hint.boardReady` `Partia je pripravená` is the longest row hint; say where each renders and
    whether it fits.
13. ANY user-facing English string still left in the two files. List them exactly and classify each as:
    an emoji, an identity from the server, the `game_end_reason` backend enum named in section 6.4, or a
    leftover you believe should have had a key. SIX previous slices left strings behind because an
    Orchestrator inventory was incomplete, and this report field caught it every time — last slice it
    came back empty of real findings for the first time.
14. deviations, risks, or missing evidence
15. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
16. Pre-Existing Failure Classification: none | <complete classification>
17. one smallest next step or review request
18. report justification: new-mutation
19. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.

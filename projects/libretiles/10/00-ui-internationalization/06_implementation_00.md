You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S5 — localize the two lobby screens and close four open corrections
Implementation authority: explicit
Independence required: no
Reasoning recommendation: medium. Basis — mostly string extraction into an established, four-times
  exercised catalog contract. The non-mechanical parts are one two-value ternary that must be replaced
  by a data-driven label, and one prop chain that must be deleted rather than renamed.
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

  git rev-parse HEAD                     -> 383011b389a9b3690647b6fa673060633572ab9d
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> 383011b389a9b3690647b6fa673060633572ab9d

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — this Next.js version has breaking changes versus
   your training data. The installed docs ARE present at `frontend/node_modules/next/dist/docs/`.
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. frontend/src/lib/i18n/GLOSSARY.md — the terminology contract, authority for this slice
6. frontend/src/lib/i18n/messages.en.ts and messages.sk.ts — the shape you extend
7. frontend/src/components/settings/GameLanguagePanel.tsx — it already exports
   `variantDisplayName(variant, t)` over `VARIANT_NAME_KEYS`. Section 5.4 requires you to reuse it.
8. frontend/src/app/play/page.tsx — in full, 398 lines
9. frontend/src/app/waiting/[id]/page.tsx — in full, 144 lines
10. frontend/src/app/settings/page.tsx lines 615-640
11. frontend/src/app/game/[id]/page.tsx lines 830-850 and 1510-1530
12. frontend/src/components/game/ScorePanel.tsx lines 255-300 and 390-415

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Localize the two lobby screens the player passes through before and around a game — `/play` and
`/waiting/[id]` — into all four locales, and close the four corrections that the previous slices left
open on the surfaces you are already touching.

=====================================================================
4. ACCEPTED DECISIONS
=====================================================================
D1  Four locales: en, sk, cs, pl. A key missing from any catalog is a `npm run typecheck` error, which
    is the mechanism working.
D2  Informal register in all three Slavic locales: sk and cs `ty`, pl 2nd person singular.
D3  Terminology from GLOSSARY.md. rival: sk `súper`, cs `soupeř`, pl `rywal`. saved board / match:
    sk `partia`, cs `partie`, pl `partia`. `AI`, `chat`, `provider`, `model`, `realtime` stay
    untranslated.
D4  REUSE existing keys rather than adding near-duplicates. Specifically reuse `landing.brand` for the
    `Libre Tiles` eyebrow and `game.ws.connectFailed` for the identical waiting-room message. Two new
    shared `nav.*` keys are authored below precisely so slice S6 does not duplicate them.
D5  COOPERATOR DECISION B20-8, verbatim `zrušiť`: the rival-name click in the game header is REMOVED,
    not renamed. See section 5.3.

=====================================================================
5. FOUR CORRECTIONS — these are not translations
=====================================================================

--- 5.1 uii-01-F10: the settings panel promises a control that no longer exists ---
`settings/page.tsx:622-623` still reads:

    title="Choose the rival"
    description="Provider-diverse free rivals from the live catalog, newest first."

Slice S4 made that panel a read-only display of one name. The title now instructs the user to choose
something they cannot choose. **REPLACE the copy, do not translate it** — a translated lie is still a
lie. Use the two new `settings.rival.*` keys in section 6.

--- 5.2 uii-01-F11: the AI status line shows a raw model id to the player ---
`game/[id]/page.tsx:845`:

    setAIStatusMessage(tf("game.ai.exploring", { model: preferenceModelId }))

`preferenceModelId` is a raw catalog `model_id` such as `nvidia/nemotron-3-super-120b-a12b`, so the
player reads `Hľadám platné slová cez nvidia/nemotron-3-super-120b-a12b...`. That contradicts the
Cooperator decision slice S4 implemented — a player sees only the model's NAME.

⛔ **The defective string is the Orchestrator's own**, authored in slice S3c, and S4 fixed this same class
of leak on the draw page while leaving this one. Pass a display NAME instead of the id: prefer the
catalog `display_name` for the resolved id, and fall back to `humanizeModelId(...)`, which the project
already uses for exactly this purpose. Do not change the `game.ai.exploring` strings themselves — only
what is passed in.

--- 5.3 uii-01-F12: remove the rival-name click, by Cooperator decision ---
After S4 the destination is a read-only panel, so the affordance is misleading and the prop name
`showRivalPicker` is now false. He was asked and answered `zrušiť`.

    REMOVE  ScorePanel.tsx  the `showRivalPicker` and `onOpenRivalPicker` props: declarations at
            :260 and :263, defaults at :278 and :281, and the control at :398-405
    REMOVE  game/[id]/page.tsx  `showRivalPicker={...}` at :1519 and
            `onOpenRivalPicker={() => router.push("/settings?focus=rival")}` at :1522
    KEEP    the rival NAME itself if it renders outside that clickable control. Read the component and
            decide; the decision is to remove the CLICK, not to hide who the opponent is. If the name
            only exists inside the removed control, say so in the report and keep it as static text.

⚠ `settings/page.tsx` has a `rivalSectionRef` used by a `?focus=rival` query parameter. With the only
link gone that focus path becomes unreachable. Leave the ref and the focus logic alone — removing it is
not authorized here and it is harmless. Name it in the report.

--- 5.4 uii-01-F14: a Czech or Polish player is told they are joining the "English queue" ---
`play/page.tsx:337-339`:

    : selectedVariantSlug === "slovak" ? "Slovak queue" : "English queue"

A two-value ternary left behind when era 11 activated Czech and Polish. Measured: four variants are
installed, and `selectedVariantSlug` has been typed `string` since era 11. Anything that is not exactly
`"slovak"` renders "English queue", so a Czech player is told they are joining the ENGLISH queue. The
label is not merely untranslated, it is FALSE about the game they are about to play.

⛔ This is the SAME defect class as `uii-01-F08`, in a second file. Do not fix it with four more
per-locale queue strings — a fifth variant would reintroduce the bug. Compose it from the variant name
the catalog already provides:

    `frontend/src/components/settings/GameLanguagePanel.tsx` exports
      `variantDisplayName(variant: VariantSummary, translate: (key: TextKey) => string): string`
    over `VARIANT_NAME_KEYS`, with a `display_name` fallback for an unknown slug, and the
    `settings.gameVariant.*` keys already exist in all four locales.

Use the ONE parameterized key `play.humanQueue.queueFor` in section 6 with that resolved name. The page
has `selectedVariantSlug` but not a `VariantSummary`; `api.getVariants(token)` is already called inside
`handleJoinHuman`. Choose the smallest correct shape — fetching the variant list on mount alongside the
existing catalog fetch, or a slug-keyed lookup that reuses `VARIANT_NAME_KEYS` — and say which you chose
and why. Do NOT duplicate `VARIANT_NAME_KEYS` into a second table.

=====================================================================
6. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
Translation is Orchestrator work in this project by Cooperator decision; no Worker translates. If you
believe a string is wrong or will overflow, NAME it in the report — do not change it.

--- 6.1 area `nav` — two SHARED keys, authored now so slice S6 does not duplicate them ---
key            en          sk             cs           pl
nav.settings   Settings    Nastavenia     Nastavení    Ustawienia
nav.account    Account     Účet           Účet         Konto

--- 6.2 area `play` ---
key                         en                          sk                            cs                            pl
play.title                  Choose the next board       Vyber si ďalšiu partiu        Vyber si další partii         Wybierz następną partię
play.lead                   Start a premium AI duel, jump into the live queue, or reopen one of your saved boards.
                            sk Spusti prémiový duel proti AI, skoč do živého frontu alebo si otvor niektorú z uložených partií.
                            cs Spusť prémiový duel proti AI, skoč do živé fronty nebo si otevři některou z uložených partií.
                            pl Rozpocznij premium duel z AI, wskocz do kolejki na żywo albo otwórz jedną z zapisanych partii.
play.ai.eyebrow             AI Match                    AI partia                     AI partie                     Partia z AI
play.ai.title               Play the house              Hraj proti AI                 Hraj proti AI                 Zagraj z AI
play.ai.body                Use the current AI rival and keep the animated opening draw.
                            sk Zahraj si proti aktuálnemu súperovi aj s animovaným ťahom o poradie.
                            cs Zahraj si proti aktuálnímu soupeři i s animovaným losováním o začátek.
                            pl Zagraj z aktualnym rywalem razem z animowanym losowaniem o początek.
play.ai.preparing           Preparing game...           Pripravujem partiu...         Připravuji partii...          Przygotowuję partię...
play.rival.unavailable      No rival available          Žiadny súper nie je dostupný  Žádný soupeř není dostupný    Brak dostępnego rywala
play.humanQueue.eyebrow     Human Queue                 Front hráčov                  Fronta hráčů                  Kolejka graczy
play.humanQueue.title       Find a live opponent        Nájdi živého súpera           Najdi živého soupeře          Znajdź żywego rywala
play.humanQueue.body        Join the first waiting player. If nobody is there, your board waits in the room.
                            sk Pripoj sa k prvému čakajúcemu hráčovi. Ak tam nikto nie je, tvoja partia počká v čakárni.
                            cs Připoj se k prvnímu čekajícímu hráči. Pokud tam nikdo není, tvoje partie počká v čekárně.
                            pl Dołącz do pierwszego czekającego gracza. Jeśli nikogo nie ma, twoja partia poczeka w pokoju.
play.humanQueue.joining     Joining queue...            Pripájam sa do frontu...      Připojuji se do fronty...     Dołączam do kolejki...
play.saved.eyebrow          Saved boards                Uložené partie                Uložené partie                Zapisane partie
play.saved.title            Resume where you left off   Pokračuj tam, kde si skončil  Pokračuj tam, kde jsi skončil Wróć tam, gdzie skończyłeś
play.saved.note             AI and human games share one premium history surface.
                            sk Partie proti AI aj proti ľuďom majú jednu spoločnú históriu.
                            cs Partie proti AI i proti lidem mají jednu společnou historii.
                            pl Partie z AI i z ludźmi mają jedną wspólną historię.
play.error.catalogEmpty     The rival catalog is empty. Seed the free catalog to play AI matches.
                            sk Katalóg súperov je prázdny. Naplň katalóg, aby sa dali hrať partie proti AI.
                            cs Katalog soupeřů je prázdný. Naplň katalog, aby se daly hrát partie proti AI.
                            pl Katalog rywali jest pusty. Wypełnij katalog, aby grać partie z AI.
play.error.variantUnavailable  No playable game variant is available. Game creation is blocked until a playable variant can be loaded.
                            sk Nie je dostupný žiadny hrateľný variant hry. Nová partia sa nedá vytvoriť, kým sa nejaký nenačíta.
                            cs Není dostupná žádná hratelná varianta hry. Novou partii nelze vytvořit, dokud se nějaká nenačte.
                            pl Brak dostępnego grywalnego wariantu gry. Nie można utworzyć partii, dopóki jakiś się nie wczyta.
play.error.startAi          Could not start an AI game.  Partiu proti AI sa nepodarilo spustiť.  Partii proti AI se nepodařilo spustit.  Nie udało się rozpocząć partii z AI.
play.error.joinQueue        Could not join the human queue.
                            sk Do frontu hráčov sa nepodarilo pripojiť.
                            cs Do fronty hráčů se nepodařilo připojit.
                            pl Nie udało się dołączyć do kolejki graczy.
play.error.loadGames        Unable to load your games.   Tvoje partie sa nepodarilo načítať.  Tvoje partie se nepodařilo načíst.  Nie udało się wczytać twoich partii.

--- 6.3 the ONE parameterized play key, and it is the uii-01-F14 fix ---
play.humanQueue.queueFor    params { variant: string }
  en (p) => `${p.variant} queue`
  sk (p) => `Front: ${p.variant}`
  cs (p) => `Fronta: ${p.variant}`
  pl (p) => `Kolejka: ${p.variant}`

⚠ The Slavic forms are a colon-label for the same reason `controls.tilesSelected` is: a natural phrase
would need the variant name in an oblique case ("slovenský front" vs "front pre slovenčinu"), and the
name arrives as a nominative label from the catalog. A colon-label is grammatically inert for every
variant, including a fifth one added later. `variant` receives the value of `variantDisplayName(...)`,
e.g. `Slovenčina` / `Čeština`, never a slug.

--- 6.4 area `queue` — the waiting room ---
key                        en                           sk                             cs                             pl
queue.title                Waiting for an opponent      Čakám na súpera                Čekám na soupeře               Czekam na rywala
queue.body                 Your board is ready. The match starts as soon as another player joins.
                           sk Tvoja partia je pripravená. Začne, len čo sa pripojí ďalší hráč.
                           cs Tvoje partie je připravená. Začne, jakmile se připojí další hráč.
                           pl Twoja partia jest gotowa. Zacznie się, gdy dołączy kolejny gracz.
queue.leave                Leave queue                  Opustiť front                  Opustit frontu                 Opuść kolejkę
queue.leaving              Leaving queue...             Opúšťam front...               Opouštím frontu...             Opuszczam kolejkę...
queue.error.dropped        Realtime connection dropped. Realtime spojenie sa prerušilo. Realtime spojení se přerušilo. Połączenie realtime zostało przerwane.
queue.error.enter          Could not enter the waiting room.
                           sk Do čakárne sa nepodarilo vstúpiť.
                           cs Do čekárny se nepodařilo vstoupit.
                           pl Nie udało się wejść do pokoju oczekiwania.
queue.error.leave          Could not leave the queue.   Front sa nepodarilo opustiť.   Frontu se nepodařilo opustit.  Nie udało się opuścić kolejki.

queue.room                 params { code: string }
  en (p) => `Room ${p.code}`
  sk (p) => `Miestnosť ${p.code}`
  cs (p) => `Místnost ${p.code}`
  pl (p) => `Pokój ${p.code}`

REUSE on the waiting page, do not add new keys:
  the `Human Queue` eyebrow          -> `play.humanQueue.eyebrow`
  `"Realtime connection failed."`    -> `game.ws.connectFailed`, which already exists in all four
                                        locales. The existing string has no trailing period; accept
                                        that difference rather than adding a near-duplicate key.

--- 6.5 the uii-01-F10 replacement copy ---
key                        en                    sk                 cs                  pl
settings.rival.title       Your rival            Tvoj súper         Tvůj soupeř         Twój rywal
settings.rival.description The administrator picks the rival for new games.
                           sk Súpera pre nové partie vyberá správca.
                           cs Soupeře pro nové partie vybírá správce.
                           pl Rywala do nowych partii wybiera administrator.

`správca` / `administrator` is deliberate: the player is being told the choice is not theirs and where it
comes from. Do not soften it to a passive construction.

--- 6.6 REUSE, do not duplicate ---
    `Libre Tiles` eyebrow on /play          -> `landing.brand`
    `Settings` / `Account` buttons on /play -> the new `nav.settings` / `nav.account`

--- 6.7 GLOSSARY.md ---
Add every new key to the key table in the style the file already uses. Do not change the terminology
table. Add one line recording that `play.humanQueue.queueFor` receives a resolved variant DISPLAY NAME
and never a slug, and that this is the `uii-01-F14` fix.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/app/play/page.tsx
  frontend/src/app/waiting/[id]/page.tsx
  frontend/src/app/settings/page.tsx          (section 5.1 only — the two panel strings)
  frontend/src/app/game/[id]/page.tsx         (sections 5.2 and 5.3 only)
  frontend/src/components/game/ScorePanel.tsx (section 5.3 only — the two props and the control)
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts

No file is created and none is deleted. If a gate fails in a file NOT on this list, STOP and report it
rather than editing that file.

⚠ `settings/page.tsx`, `game/[id]/page.tsx` and `ScorePanel.tsx` are on the list for the NAMED
corrections only. Their remaining English copy belongs to slice S6. Do not localize it here — that would
make this diff unreviewable and duplicate S6's work.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- The rest of the settings copy, the rest of ScorePanel, and the rest of `game/[id]/page.tsx`. Slice S6.
- `frontend/src/components/game/GameHistoryPanel.tsx`, `GameHistoryModal.tsx`, `ProfileModal.tsx`,
  `AIThinkingOverlay.tsx`. Slice S7 owns history/profile; the overlay is deferred with the AI telemetry.
  ⚠ `/play` RENDERS `GameHistoryPanel`. Do not follow that call.
- `frontend/src/lib/types.ts` and `ai-move-stream.ts`. The six human-readable AI telemetry states come
  from the LOCKED move route and need an enum-keyed redesign; that is its own deferred slice.
- `frontend/src/lib/model-catalog.ts`. `resolveEligibleModelId`'s precedence is correct and is relied on
  by three call sites. Do not change it.
- `frontend/src/lib/ai-fallback.ts` and `selectedModelId`. `game/[id]/page.tsx:833`
  `preferenceModelId` feeds attempt 1 of the provider fallback queue. Section 5.2 changes only what is
  DISPLAYED, never what is passed to the queue. Read that twice.
- `frontend/src/lib/constants.ts` — TW/DW/TL/DL is the BOARD, not copy.
- `frontend/src/lib/api.ts`. Its 401 branch is a security property.
- `frontend/src/proxy.ts`, `security-headers.ts`. The nonce CSP is a later slice.
- `frontend/src/lib/i18n/locales.ts`, `plural.ts`, `translate.ts`, `LocaleProvider.tsx`, `index.ts`.
  You add catalog KEYS, not machinery.
- `frontend/src/components/settings/GameLanguagePanel.tsx`. You REUSE its exported
  `variantDisplayName`; you do not edit it.
- Anything under `backend/`. Django localization is a later slice. `prompts.ts:198,208` also carry a
  two-value `=== "slovak"` test, which is the already-recorded era-11 finding that Czech and Polish get
  the English MOVE prompt CORE. `prompts.ts` is LOCKED (locked fork 2) and is NOT yours.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- `frontend/package.json` and `package-lock.json`. NO new dependency.
- Do not bump the persist version. Do not add a locale to any `Intl.DateTimeFormat` call (uii-01-F03,
  later slice). Do not add aria-label, role, or alt (uii-01-F02, later slice).
- `useGameStore.ts:280`'s `version < 2` branch also tests `"english"`/`"slovak"`. That is deliberate
  legacy handling of an old payload. Leave it exactly as it is.
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
Evidence tier basis: two full screens plus four corrections across five files, one of which replaces a
  false label with a data-driven one and one of which deletes a prop chain; user-visible; no trust
  boundary, no durable data, no credential, no production effect. Rollback is `git revert` of one commit.
Combined implementation envelope: allowed
Independent acceptance: not-required. Evidence is NON-INDEPENDENT. Rendered acceptance is
  Cooperator-owned and the Orchestrator will request it as batch B22.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: frontend/src/lib/i18n/i18n.test.ts
New causal regression: the uii-01-F14 variant-driven queue label
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `378 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-QUEUE-VARIANT  THE uii-01-F14 REGRESSION TEST AND THE MOST IMPORTANT ONE HERE. For each of the four
                    installed variant slugs — english, slovak, czech, polish — the rendered queue label
                    contains that variant's own name and NOT another variant's. Assert specifically that
                    the czech case contains neither `Angličtina` nor `Slovenčina` in the sk locale, and
                    that it does not contain the word `English` in any locale. This must fail against the
                    current two-value ternary.
  AC-QUEUE-UNKNOWN  An unrecognised slug does not throw and does not render another variant's name. The
                    `display_name` fallback in `variantDisplayName` is what makes this pass; assert it
                    rather than assuming it.
  AC-PLAY-4         `play.title`, `play.ai.title` and `play.humanQueue.title` render the exact authored
                    string in all four locales.
  AC-QUEUE-ROOM-4   `queue.room` interpolates the code in all four locales and the sk / cs / pl forms do
                    not contain the English word `Room`.
  AC-EXHAUST4       ALREADY EXISTS and must keep passing with every new key. Do not weaken it.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted. Do not be the first.

=====================================================================
11. GIT AUTHORITY
=====================================================================
On the PRIMARY route only, after all eight gates are green: exactly one commit and one push.
On the FALLBACK route: NO commit, NO push.

  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): localize the lobby screens and fix the queue label
     Body: the four corrected findings by ID, which shape you chose for the F14 variant lookup and why,
     and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     383011b389a9b3690647b6fa673060633572ab9d. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.

FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails in a file outside the section 7
allowlist; the F14 fix appears to require editing `GameLanguagePanel.tsx` or duplicating
`VARIANT_NAME_KEYS`; removing the rival-name control appears to require a structural change beyond the
named props; a hook would have to be called conditionally; you conclude a new dependency is required;
the backend gates fail; `git ls-remote` shows main advanced; any instruction here conflicts with
AGENTS.md, .ap/AP.md, or observed repository truth; or you find yourself weakening an existing test.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 06, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, and the count of strings routed through the catalog per file
 7. THE uii-01-F14 DECISION: which shape you chose for resolving the variant display name, why it is the
    smallest correct one, and the exact proof that a fifth variant cannot reintroduce the bug
 8. uii-01-F11: what value is now passed to `game.ai.exploring`, and explicit confirmation that
    `preferenceModelId` still reaches the fallback queue UNCHANGED
 9. uii-01-F12: what was removed, and whether the rival name still renders as static text
10. uii-01-F10: the replaced title and description
11. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
12. gate results — eight on the primary route, seven plus a named omission on the fallback — with the
    pytest summary quoted verbatim and the vitest counts
13. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
14. any string you believe is wrong, or any container you believe a Slavic string will overflow — NAME
    it, do not change it. `play.error.variantUnavailable` is the longest string in this slice; say where
    it renders and whether it fits.
15. ANY user-facing English string still left in `play/page.tsx` or `waiting/[id]/page.tsx` after your
    work. List them exactly. THREE previous slices left strings behind because an Orchestrator inventory
    was incomplete, and this report field is the structural defence that caught it every time. Do not
    list strings in the three files you touched only for the named corrections — those are S6's.
16. deviations, risks, or missing evidence
17. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
18. Pre-Existing Failure Classification: none | <complete classification>
19. one smallest next step or review request
20. report justification: new-mutation
21. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.

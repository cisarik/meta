You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S3c — localize the game screen, correct two defects it exposes, and finish the board
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — the largest single file in this whole (1822 lines), and two
  named defects must be corrected rather than translated around: one message that is factually false
  for two shipped variants, and one substring check that translation would silently break.
Report justification: new-mutation
Context-pressure rule: report visible context usage if it exceeds 70%.

=====================================================================
1. REPOSITORY, TOPOLOGY, BASELINE
=====================================================================
Repository checkout topology: standalone checkout
Repository identity: https://github.com/cisarik/libretiles
Working directory: /home/agile/Projects/libretiles
Expected branch: main
Expected HEAD: e421c6690f091203a60636b3aebaeec71e7fba69
Working-copy topology: canonical checkout.

REPOSITORY GATE. Run these first and STOP if any disagrees:
  git rev-parse HEAD                     -> e421c6690f091203a60636b3aebaeec71e7fba69
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> e421c6690f091203a60636b3aebaeec71e7fba69

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — this Next.js version has breaking changes
   versus your training data. The installed documentation tree IS present at
   `frontend/node_modules/next/dist/docs/` (452 markdown files, verified). A previous Worker reported it
   absent and was wrong; do not repeat that claim without checking that exact path.
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. frontend/src/lib/i18n/GLOSSARY.md — the terminology contract, authority for this slice
6. frontend/src/lib/i18n/messages.en.ts and messages.sk.ts — the shape you extend
7. frontend/src/app/game/[id]/page.tsx — IN FULL, all 1822 lines, before editing anything
8. frontend/src/components/board/Board.tsx around line 689 — the one-word correction in section 6.4

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Route every user-facing string on the game screen through the four-locale catalog, and in the same pass
correct the two defects that localizing this file exposes: a rejection message that names an English
dictionary for Czech and Polish games, and a subtitle chosen by substring-matching English prose.

Also finish the board: one word was left in English by the previous slice because the Orchestrator's
allowlist was too narrow.

=====================================================================
4. ACCEPTED DECISIONS
=====================================================================
D1  Four locales: en, sk, cs, pl. Every key must exist in all four or `npm run typecheck` fails.
D2  Informal register in all three Slavic locales: sk and cs `ty`, pl 2nd person singular.
D3  Terminology from GLOSSARY.md. tile: sk `písmeno`, cs `KÁMEN`, pl `płytka`. rival/opponent: sk
    `súper`, cs `soupeř`, pl `rywal` for the AI and `przeciwnik` for a human. The word "free" is
    dropped from "free rival" by decision — Libre Tiles is free-only, so it adds nothing for a player.
D4  `provider`, `model`, `prompt`, `token`, `chat`, `API`, `AI`, `realtime`, `offline` stay
    untranslated. So do provider names and model ids.
D5  REUSE existing keys instead of adding duplicates: `auth.tab.login` for the `Sign In` button,
    `controls.play` for the AI-approval `Play` button, `board.pts` is NOT reused here — the game screen
    gets its own `game.aiPlayedFor.points` because it sits in different markup.

=====================================================================
5. TWO DEFECTS YOU MUST CORRECT, NOT TRANSLATE AROUND
=====================================================================

--- 5.1 uii-01-F08: a Czech or Polish player is told their word is not in an ENGLISH dictionary ---

`frontend/src/app/game/[id]/page.tsx:231-233` reads:

    {lexiconId === "slovak"
      ? "Not in the Slovak lexicon"
      : "Not in Collins Scrabble Words 2019"}

That two-value test was written when only English and Slovak existed. Measured through the real loader:
`backend/game/services.py:159` `_lexicon_id` returns `Path(variant.dictionary_file).stem`, so
`gameState.lexicon_id` takes FOUR values — `collins2019`, `slovak`, `czech`, `polish`. Anything that is
not exactly `"slovak"` falls into the else branch, so a Czech player is told
"Not in Collins Scrabble Words 2019". The message is not merely untranslated, it is **false**.

Correct it with FIVE complete messages keyed on `lexicon_id`, plus a generic fallback for an unknown id.
Do NOT build one parameterized "Not in ${lexicon}" sentence: Slovak and Czech need the lexicon name in
the LOCATIVE case and Polish in its own oblique form, which a single nominative label cannot supply.
Five keys per locale is cheaper and grammatically safe.

--- 5.2 uii-01-F09: localizing the AI toast would silently break its own subtitle ---

Producer, `page.tsx:1033-1054`: `action === "pass"` and `action === "exchange"` BOTH create
`type: "ai_pass"` and are distinguished only by the message prose. Consumer, `page.tsx:305`:

    {toast.message.toLowerCase().includes("exchanged")
      ? "AI refreshed the rack and spent the turn."
      : "Couldn't find a valid move - your turn!"}

The moment that message becomes `AI vymenilo písmená`, the substring `exchanged` is gone, the check
always takes the else branch, and an EXCHANGE is explained to the player as "Couldn't find a valid
move". This is the `err.message.includes("401")` anti-pattern that the security era deliberately removed
from `api.ts` in favour of a numeric status; re-introducing it through translation would be a regression
in a pattern this project already paid to eliminate.

Correct it by carrying the discriminator in the toast DATA, not its prose. Either split `ai_pass` into
two explicit toast types, or add an explicit field to the existing one. Choose the smaller change for
this file and say which you chose and why. After the fix the localized strings must have NO load-bearing
content: the subtitle must be chosen without inspecting any human-readable text.

=====================================================================
6. WHAT TO CHANGE
=====================================================================

--- 6.1 page.tsx: route the strings in section 7 through `useT()` ---
The file already imports from `@/lib/i18n`; verify how and follow the existing pattern. Several strings
live inside `ToastView` and other sub-components defined in the same file — those are client components
and `useT()` is available in them. Where a string is produced OUTSIDE a component (inside a callback
that builds a toast object), use the same locale-resolution the file already uses for that scope; if
none exists, `useT()` at the component level and pass the resolved text in. Do not introduce a
module-level mutable locale and do not call a hook conditionally.

--- 6.2 window.confirm at page.tsx:690 ---
`giveUpMessage` is passed to `window.confirm`. Localize the message. The native dialog's own OK/Cancel
buttons are browser chrome and are NOT yours to change.

--- 6.3 Do NOT touch these strings in page.tsx, even though they are user-facing ---
```text
"Choose rival"        page.tsx:1502 and :1504   the model picker fallback — slice S4 DELETES it
"Initial"             page.tsx:1513             prompt-preset name fallback — slice S4 deletes it
"Could not switch AI prompt right now."  :606   prompt switching — slice S4 owns it
```
Localizing something a later slice deletes is wasted work and doubles the review surface. Leave all
three exactly as they are.

--- 6.4 Board.tsx:689 — the one-word correction ---
    <span className="text-white/34">zoom</span>
The previous slice localized the sibling `{t("board.reset")}` but not this word, because the
Orchestrator's allowlist named five text nodes when the file had six. The control therefore reads
"Reset zoom" in every locale. Replace the literal with `{t("board.zoomNoun")}` and change NOTHING else
in that 692-line file — no threshold, no ref, no effect, no transform, no className. Keeping the two
separate spans preserves the gold-shiny / dim visual design.

=====================================================================
7. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
Translation is Orchestrator work in this project by Cooperator decision; no Worker translates. If you
believe a string is wrong or will overflow its container, NAME it in the report — do not change it.

--- 7.1 the lexicon messages (the 5.1 fix) ---
key                          en                                    sk
game.lexicon.collins2019     Not in Collins Scrabble Words 2019    Nie je v Collins Scrabble Words 2019
game.lexicon.slovak          Not in the Slovak lexicon             Nie je v slovenskom lexikóne
game.lexicon.czech           Not in the Czech lexicon              Nie je v českom lexikóne
game.lexicon.polish          Not in the Polish lexicon             Nie je v poľskom lexikóne
game.lexicon.unknown         Not in the game lexicon               Nie je v lexikóne hry
                             cs                                    pl
game.lexicon.collins2019     Není v Collins Scrabble Words 2019    Nie ma w Collins Scrabble Words 2019
game.lexicon.slovak          Není ve slovenském lexikonu           Nie ma w słowackim leksykonie
game.lexicon.czech           Není v českém lexikonu                Nie ma w czeskim leksykonie
game.lexicon.polish          Není v polském lexikonu               Nie ma w polskim leksykonie
game.lexicon.unknown         Není v lexikonu hry                   Nie ma w leksykonie gry

--- 7.2 provider / rival blocker modal (page.tsx 144-172, 403-406) ---
key                        en                          sk                          cs                          pl
game.blocker.auth.title    Rival authentication failed  Prihlásenie súpera zlyhalo  Přihlášení soupeře selhalo  Błąd uwierzytelnienia rywala
game.blocker.auth.body     This free rival could not authenticate. Switch to another free rival or retry later.
                           sk Tento súper sa nedokázal prihlásiť. Vyber iného súpera alebo to skús neskôr.
                           cs Tento soupeř se nedokázal přihlásit. Vyber jiného soupeře nebo to zkus později.
                           pl Ten rywal nie mógł się uwierzytelnić. Wybierz innego rywala lub spróbuj później.
game.blocker.rate.title    Rival is rate limited        Súper má vyčerpaný limit    Soupeř má vyčerpaný limit   Rywal ma wyczerpany limit
game.blocker.rate.body     This free rival is rate limited. Switch to another free rival or retry later.
                           sk Tento súper má momentálne vyčerpaný limit. Vyber iného súpera alebo to skús neskôr.
                           cs Tento soupeř má momentálně vyčerpaný limit. Vyber jiného soupeře nebo to zkus později.
                           pl Ten rywal ma teraz wyczerpany limit. Wybierz innego rywala lub spróbuj później.
game.blocker.unavail.title Rival is unavailable         Súper je nedostupný         Soupeř je nedostupný        Rywal jest niedostępny
game.blocker.unavail.body  This free rival is temporarily unavailable. Switch to another free rival or retry later.
                           sk Tento súper je momentálne nedostupný. Vyber iného súpera alebo to skús neskôr.
                           cs Tento soupeř je momentálně nedostupný. Vyber jiného soupeře nebo to zkus později.
                           pl Ten rywal jest chwilowo niedostępny. Wybierz innego rywala lub spróbuj później.
game.blocker.badge.auth    Authentication               Prihlásenie                 Přihlášení                  Uwierzytelnianie
game.blocker.badge.rate    Rate Limited                 Limit vyčerpaný             Limit vyčerpán              Limit wyczerpany
game.blocker.badge.unavail Unavailable                  Nedostupné                  Nedostupné                  Niedostępne
game.blocker.close         Close                        Zavrieť                     Zavřít                      Zamknij
game.blocker.openSettings  Open settings                Otvoriť nastavenia          Otevřít nastavení           Otwórz ustawienia

--- 7.3 toasts ---
key                        en                    sk                       cs                       pl
game.toast.invalidPlacement Invalid Placement    Neplatné umiestnenie     Neplatné umístění        Nieprawidłowe ułożenie
game.toast.invalidWords    Invalid words         Neplatné slová           Neplatná slova           Nieprawidłowe słowa
game.toast.moveRejected    Move rejected         Ťah zamietnutý           Tah zamítnut             Ruch odrzucony
game.toast.exchangeRejected Exchange rejected    Výmena zamietnutá        Výměna zamítnuta         Wymiana odrzucona
game.toast.passRejected    Pass rejected         Vynechanie zamietnuté    Vzdání tahu zamítnuto    Pauza odrzucona
game.toast.chatOffline     Chat is offline       Chat je offline          Chat je offline          Chat jest offline
game.toast.aiPasses        AI passes             AI vynechalo ťah         AI vzdalo tah            AI wzięło pauzę
game.toast.aiExchanged     AI exchanged tiles    AI vymenilo písmená      AI vyměnilo kameny       AI wymieniło płytki
game.toast.aiExchangedBody AI refreshed the rack and spent the turn.
                           sk AI si obnovilo zásobník a spotrebovalo ťah.
                           cs AI si obnovilo zásobník a spotřebovalo tah.
                           pl AI odświeżyło stojak i zużyło ruch.
game.toast.aiPassedBody    Couldn't find a valid move - your turn!
                           sk Nenašlo platný ťah — si na ťahu!
                           cs Nenašlo platný tah — jsi na tahu!
                           pl Nie znalazło poprawnego ruchu — twój ruch!
game.aiPlayedFor.before    AI played for         AI zahralo za            AI zahrálo za            AI zagrało za
game.aiPlayedFor.points    pts                   b.                       b.                       pkt

`game.aiPlayedFor` is split into a prefix and a unit because the score sits between them in its own
larger styling (`text-[1.78rem] font-black`). All four languages accept that word order. Do not merge
them into one parameterized string and do not drop the span.

--- 7.4 status, errors, lifecycle ---
key                        en                              sk                                cs                                pl
game.status.selectExchange Select tiles to exchange         Vyber písmená na výmenu           Vyber kameny na výměnu            Wybierz płytki do wymiany
game.status.aiMoveReady    AI move ready                    Ťah AI je pripravený              Tah AI je připraven               Ruch AI gotowy
game.status.aiThinking     AI is thinking                   AI premýšľa                       AI přemýšlí                       AI myśli
game.status.yourTurn       Your turn                        Tvoj ťah                          Tvůj tah                         Twój ruch
game.status.waitingForAi   Waiting for the AI               Čakám na AI                       Čekám na AI                       Czekam na AI
game.opponentFallback      Opponent                         Súper                             Soupeř                            Przeciwnik
game.waitingSlot           Waiting                          Čaká sa                           Čeká se                           Oczekiwanie
game.sessionExpired        Session expired                  Prihlásenie vypršalo              Přihlášení vypršelo               Sesja wygasła
game.lastError             Last error:                      Posledná chyba:                   Poslední chyba:                   Ostatni błąd:
game.newGame               New Game                         Nová partia                       Nová partie                       Nowa partia
game.starting              Starting...                      Spúšťam...                        Spouštím...                       Uruchamiam...
game.victory               Victory!                         Vyhral si!                        Vyhrál jsi!                       Wygrałeś!
game.draw                  Draw!                            Remíza!                           Remíza!                           Remis!
game.gameOver              Game Over                        Koniec partie                     Konec partie                      Koniec partii
game.giveUp.ai             Give up this game? The AI will be declared the winner.
                           sk Vzdať túto partiu? Za víťaza bude vyhlásené AI.
                           cs Vzdát tuto partii? Za vítěze bude vyhlášeno AI.
                           pl Poddać tę partię? Zwycięzcą zostanie AI.
game.giveUp.human          Give up this game? Your opponent will be declared the winner.
                           sk Vzdať túto partiu? Za víťaza bude vyhlásený súper.
                           cs Vzdát tuto partii? Za vítěze bude vyhlášen soupeř.
                           pl Poddać tę partię? Zwycięzcą zostanie przeciwnik.
game.gaveUp                You gave up the game.            Vzdal si partiu.                  Vzdal jsi partii.                 Poddałeś partię.
game.error.giveUp          Could not give up this game      Partiu sa nepodarilo vzdať        Partii se nepodařilo vzdát        Nie udało się poddać partii
game.error.newGame         Could not start a new game       Novú partiu sa nepodarilo spustiť Novou partii se nepodařilo spustit Nie udało się rozpocząć nowej partii
game.error.loadGames       Unable to load games.            Partie sa nepodarilo načítať.     Partie se nepodařilo načíst.      Nie udało się wczytać partii.
game.password.updated      Password updated.                Heslo je zmenené.                 Heslo je změněno.                 Hasło zmienione.
game.password.failed       Unable to update password.        Heslo sa nepodarilo zmeniť.       Heslo se nepodařilo změnit.       Nie udało się zmienić hasła.
game.ai.noRival            No eligible free rival is available.
                           sk Nie je dostupný žiadny vhodný súper.
                           cs Není dostupný žádný vhodný soupeř.
                           pl Brak dostępnego odpowiedniego rywala.
game.ai.timeout            AI thinking time ran out.        AI vypršal čas na rozmýšľanie.    AI vypršel čas na rozmýšlení.     AI skończył się czas na myślenie.
game.ai.moveFailed         AI move failed                   Ťah AI zlyhal                     Tah AI selhal                     Ruch AI nie udał się
game.ws.syncFailed         Realtime sync failed             Synchronizácia zlyhala            Synchronizace selhala             Synchronizacja nie udała się
game.ws.connectFailed      Realtime connection failed       Realtime spojenie zlyhalo         Realtime spojení selhalo          Połączenie realtime nie udało się
game.ws.authExpired        Realtime authentication expired. Refresh the page to reconnect.
                           sk Prihlásenie pre realtime vypršalo. Obnov stránku a pripoj sa znova.
                           cs Přihlášení pro realtime vypršelo. Obnov stránku a připoj se znovu.
                           pl Uwierzytelnienie realtime wygasło. Odśwież stronę, aby połączyć się ponownie.
game.ws.invalidSession     This realtime session is not valid. Refresh the page to reconnect.
                           sk Toto realtime spojenie nie je platné. Obnov stránku a pripoj sa znova.
                           cs Toto realtime spojení není platné. Obnov stránku a připoj se znovu.
                           pl To połączenie realtime jest nieprawidłowe. Odśwież stronę, aby połączyć się ponownie.
game.ws.unavailable        The realtime service is unavailable. Please try again.
                           sk Realtime služba je nedostupná. Skús to znova.
                           cs Realtime služba je nedostupná. Zkus to znovu.
                           pl Usługa realtime jest niedostępna. Spróbuj ponownie.

--- 7.5 the FOUR parameterized keys ---
game.ai.exploring   params { model: string }
  en (p) => `Exploring legal words with ${p.model}...`
  sk (p) => `Hľadám platné slová cez ${p.model}...`
  cs (p) => `Hledám platná slova přes ${p.model}...`
  pl (p) => `Szukam poprawnych słów przez ${p.model}...`

game.ai.attempt     params { index: number; total: number; label: string }
  Replaces the word "Attempt" in `Attempt ${i}/${n} · ${provider} · ${model}` at page.tsx:971. The
  provider badge and model id are NOT translated and are passed through in `label` unchanged.
  en (p) => `Attempt ${p.index}/${p.total} · ${p.label}`
  sk (p) => `Pokus ${p.index}/${p.total} · ${p.label}`
  cs (p) => `Pokus ${p.index}/${p.total} · ${p.label}`
  pl (p) => `Próba ${p.index}/${p.total} · ${p.label}`

game.toast.aiPlayedWord  params { word: string }
  en (p) => `AI played ${p.word}`
  sk (p) => `AI zahralo ${p.word}`
  cs (p) => `AI zahrálo ${p.word}`
  pl (p) => `AI zagrało ${p.word}`
  The existing `bestWord ?? "a word"` fallback becomes the new plain key `game.aWord`:
    en "a word"   sk "slovo"   cs "slovo"   pl "słowo"

game.status.opponentPlaying  params { name: string }
  en (p) => `${p.name} is playing`
  sk (p) => `${p.name} je na ťahu`
  cs (p) => `${p.name} je na tahu`
  pl (p) => `${p.name} wykonuje ruch`

--- 7.6 the board word ---
key             en      sk       cs       pl
board.zoomNoun  zoom    zoomu    zoomu    zoomu     -> renders "Reset zoomu" in all three Slavic locales

--- 7.7 GLOSSARY.md ---
Add every new key to the key table in the style the file already uses. Do not change the terminology
table. Add one line recording that `game.lexicon.*` is keyed on the GAME VARIANT's `lexicon_id` and not
on the interface locale, because those are two independent axes and this is the first key family that
depends on the other one.

=====================================================================
8. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts
  frontend/src/app/game/[id]/page.tsx
  frontend/src/components/board/Board.tsx     (ONE word, section 6.4, nothing else)

No file is created. If a gate fails in a file NOT on this list, STOP and report it rather than editing
that file.

=====================================================================
9. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- The three strings in section 6.3. Slice S4 deletes them.
- frontend/src/components/game/ScorePanel.tsx, GameHistoryPanel.tsx, GameHistoryModal.tsx,
  ProfileModal.tsx, PromptCatalogModal.tsx, PromptPreviewModal.tsx, AIThinkingOverlay.tsx.
  Later slices own them. You will see page.tsx render them; do not follow the call.
- frontend/src/lib/types.ts and frontend/src/lib/ai-move-stream.ts. The six human-readable AI telemetry
  states are produced inside the LOCKED move route and re-derived there; localizing them needs an
  enum-keyed redesign and is deliberately deferred to its own slice. Do not start it.
- frontend/src/app/play/page.tsx, frontend/src/app/waiting/[id]/page.tsx, frontend/src/app/settings/page.tsx.
- frontend/src/lib/constants.ts. Its 61 capitalized literals are the premium-square board layout
  (TW / DW / TL / DL). GAME DATA. Translating them would corrupt the board.
- frontend/src/lib/api.ts. Its 401 branch is a security property (AC-SEC-1 / AC-SEC-2) and is already
  correct; leaving it untouched is what preserves it.
- frontend/src/lib/i18n/locales.ts, plural.ts, translate.ts, LocaleProvider.tsx, index.ts. The locale
  architecture is correct. You add catalog KEYS, not machinery.
- frontend/src/proxy.ts, frontend/src/lib/security-headers.ts. The nonce CSP is a later slice.
- Any file under backend/. Django localization is a later slice. This includes `services.py` — even
  though `_lexicon_id` is what makes uii-01-F08 reachable, the FRONTEND fix in section 5.1 is complete
  on its own and no backend change is authorized.
- frontend/package.json and frontend/package-lock.json. NO new dependency.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- frontend/src/lib/prompts.ts, its pinned SHA-256, MOVE_PROMPT_VERSION, and
  frontend/src/app/api/ai/move/route.ts. Locked fork 2.
- SVG `path d="..."` data and `Content-Type` in page.tsx are not copy. Neither are the
  `` `state-${Date.now()}` `` style toast ids or the `` `game-${gameId}-rack-board` `` LayoutGroup id.
- The `" vs "` separator at page.tsx:1709 stays English by glossary decision: `vs` is universally
  understood and the container is narrow. Only the `"Waiting"` fallback inside it is localized.
- Do not add a locale to any Intl.DateTimeFormat call (uii-01-F03, later slice).
- Do not add aria-label, role, or alt attributes (uii-01-F02, later slice).
- Do not reformat, reorder imports in, or "tidy" anything beyond the named edits.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files.

=====================================================================
10. COMMANDS AND EXECUTION ROUTE
=====================================================================
Allowed, from frontend/: npm run typecheck, npx vitest run, npx vitest run <file>, npm run lint,
  npm run build.
Allowed, from backend/: the four gates below, ONLY via the bounded deviation, to prove you did not
  break the backend. You are NOT authorized to change any backend file.

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
TRAP: `npm run build` and `npm run dev` share frontend/.next. Check `ss -tlnp | grep :3000` first; if
  occupied, STOP and report. Do NOT kill it.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`.

Forbidden commands: any git write beyond section 11, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote`
  reads, any process kill.
Secret authority: NONE. Never reference frontend/.env.local or backend/.env.
Dependency authority: NONE.
Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

=====================================================================
11. EVIDENCE, VALIDATION, GIT
=====================================================================
Evidence tier: E2
Evidence tier basis: the largest file in the whole, two behavioural corrections rather than pure string
  extraction, user-visible; no trust boundary, no durable data, no credential, no production effect.
Combined implementation envelope: allowed
Implementation stage gates: all eight gates green before the commit; a failed gate stops the sequence
Independent acceptance: not-required. Evidence is NON-INDEPENDENT. Rendered acceptance is
  Cooperator-owned and the Orchestrator will request it as batch B19.
Rollback: `git revert` of one commit
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: frontend/src/lib/i18n/i18n.test.ts
New causal regression: the two defect corrections named below
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used
Independent acceptance: not-required

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `369 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-LEX-4    For each of the four `lexicon_id` values and each of the four locales, the selected
              message is the right one. Assert specifically that with `lexicon_id: "czech"` the message
              does NOT contain "Collins", and that with `"collins2019"` it DOES. This is the
              uii-01-F08 regression test and it must fail against the current ternary.
  AC-LEX-UNK  An unrecognised `lexicon_id` selects `game.lexicon.unknown` and does not throw.
  AC-TOAST-DISC  The uii-01-F09 regression test. An EXCHANGE toast selects the exchange subtitle in a
              locale whose message contains no English word — assert Slovak, where the message is
              `AI vymenilo písmená` and the substring `exchanged` is absent. Assert a PASS toast
              selects the pass subtitle. This test must fail while the substring check exists.
  AC-EXHAUST4 ALREADY EXISTS and must keep passing with every new key. Do not weaken it.
  AC-GAME-TERM  Czech `game.status.selectExchange` contains `kameny` and NOT `písmen`; Polish contains
              `płytki`. The Czech tile-versus-letter distinction is the most easily "corrected" thing
              in this slice.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted. Do not be the first.

GIT: exactly one commit and one push, only after all eight gates are green.
  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): localize the game screen and fix the lexicon and toast defects
     Body: the two corrected defects by ID, which discriminator shape you chose for uii-01-F09 and why,
     and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     e421c6690f091203a60636b3aebaeec71e7fba69. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.
FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: any repository gate disagrees including a non-empty porcelain; a gate fails outside
the section 8 allowlist; you cannot localize a string without a structural change beyond section 5's two
corrections; a hook would have to be called conditionally; you conclude a new dependency is required;
the backend gates fail; port 3000 is occupied; `git ls-remote` shows main advanced; any instruction here
conflicts with AGENTS.md, .ap/AP.md, or observed repository truth; or you find yourself weakening,
skipping, xfailing, or deleting an existing test.

If you stop, use:  Escalation disposition: NEEDS_ORCHESTRATOR_DECISION

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 04, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. changed files with the purpose of each, and the exact count of strings routed through the catalog in
    `page.tsx`
 6. THE uii-01-F09 DECISION: which discriminator shape you chose, why it is the smaller change, and the
    exact proof that no localized string is load-bearing any more
 7. the uii-01-F08 correction: how the five messages are selected, and what happens for an unknown id
 8. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
 9. all eight gate results, with the pytest summary quoted verbatim, the vitest counts, and
    confirmation that zero routes became `○`
10. commit and push result, with both `git ls-remote` and `git rev-parse HEAD` quoted
11. any string you believe is wrong, or any container you believe a Slavic string will overflow — NAME
    it, do not change it. You see the classNames; the Orchestrator authored the words.
12. ANY user-facing English string still left in `page.tsx` after your work, other than the three in
    section 6.3. List them exactly. The previous slice left one word behind because an Orchestrator
    allowlist was one item short, and this report is where that gets caught.
13. deviations, risks, or missing evidence
14. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
15. Pre-Existing Failure Classification: none | <complete classification>
16. one smallest next step or review request
17. report justification: new-mutation
18. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.

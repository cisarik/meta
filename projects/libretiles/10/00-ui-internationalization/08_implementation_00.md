You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S7 — localize the settings screen and the overlay stats bar
Implementation authority: explicit
Independence required: no
Reasoning recommendation: medium. Basis — volume string extraction into a six-times exercised catalog
  contract. The one structural decision is that three module-level constant arrays must carry KEYS
  instead of strings, and section 5 specifies exactly how.
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

  git rev-parse HEAD                     -> 6ca85de7ee1e5a1db33253eeb9e7e47922e2718a
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> 6ca85de7ee1e5a1db33253eeb9e7e47922e2718a

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
6. frontend/src/lib/i18n/messages.en.ts and messages.sk.ts — the shape you extend and the source of the
   four keys section 4 tells you to REUSE
7. frontend/src/app/settings/page.tsx — IN FULL before editing anything. Pay particular attention to
   lines 24-49 (the three constant arrays), 86-135 (`SettingsPanel` and `ChoiceGrid`), 165-290
   (the three toggle/theme panels) and 560-670 (the page shell).
8. frontend/src/components/game/AIThinkingOverlay.tsx lines 360-378 — the stats bar only

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Localize the settings screen into all four locales, and close the one leftover the previous slice
reported in the AI overlay's stats bar.

Settings is the screen where the player chooses their interface language, so a settings screen that is
itself in English is the single most self-contradicting surface left in the product.

=====================================================================
4. ACCEPTED DECISIONS AND FOUR KEYS TO REUSE
=====================================================================
D1  Four locales: en, sk, cs, pl. A key missing from any catalog is a `npm run typecheck` error.
D2  Informal register in all three Slavic locales: sk and cs `ty`, pl 2nd person singular.
D3  `AI`, `GPU`, `premium`, `chat`, `provider`, `model` stay untranslated.
D4  REUSE these four existing keys instead of authoring duplicates. Verified present in all four
    catalogs at this commit:
```text
    settings "Settings" page heading  -> nav.settings              sk "Nastavenia"
    settings "Starting..."            -> game.starting             sk "Spúšťam..."
    settings "New game"               -> game.newGame              sk "Nová partia"
    settings catalog-empty sentence   -> play.error.catalogEmpty    sk "Katalóg súperov je prázdny. ..."
```
D5  These are NOT copy and must NOT be touched:
      `"Escape"` at settings/page.tsx:515 — a KeyboardEvent key name
      the `TIMEOUT_CHOICES` labels `"30s" "1m" "2m" "3m" "5m"` — compact unit abbreviations in a tight
        grid; `s` and `m` read internationally and translating them would break the layout for no gain
      the `STEP_CHOICES` labels `"10" "20" "30" "50" "80"` — they are numbers

=====================================================================
5. THE ONE STRUCTURAL DECISION — three constant arrays must carry KEYS
=====================================================================
`TIMEOUT_CHOICES`, `STEP_CHOICES` and `BOARD_THEME_CHOICES` are module-level constants at
settings/page.tsx:25-49 holding literal English `description` (and, for themes, `label`) strings. A
module-level constant cannot call a hook, so the strings must become KEYS resolved at render time.

Change the arrays to carry `TextKey` values and resolve them inside the component:

```ts
const TIMEOUT_CHOICES: Array<{ value: number; label: string; descriptionKey: TextKey }> = [
  { value: 30,  label: "30s", descriptionKey: "settings.timeout.30" },
  ...
];
```

and in `ChoiceGrid` render `t(choice.descriptionKey)` instead of `choice.description`.

⚠ Constraints on that change, all load-bearing:
  - the `value` and `label` fields keep their current types and values;
  - the arrays stay module-level constants — do NOT move them inside the component and do NOT turn them
    into functions;
  - type the arrays with an explicit `TextKey` annotation as shown, so a typo in a key name is a `tsc`
    error rather than a runtime `undefined`. That annotation is the whole point;
  - `ChoiceGrid`'s prop type changes from `description: string` to `descriptionKey: TextKey`. It is a
    local component in the same file, so no other file is affected. Verify that and say so.
  - `BOARD_THEME_CHOICES` needs BOTH `labelKey` and `descriptionKey`.

The two inline `[{ value: true, label: "On", ... }, { value: false, label: "Off", ... }]` arrays at
:227-228 and :276-277 are built inside their components, so they may resolve keys directly with `t(...)`
without the constant-array treatment.

=====================================================================
6. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
Thirty-eight new keys. Translation is Orchestrator work in this project by Cooperator decision; no Worker
translates. If you believe a string is wrong or will overflow, NAME it in the report — do not change it.

--- 6.1 area `settings` — AI thinking time, five descriptions ---
key                     en                     sk                              cs                              pl
settings.timeout.title  AI Thinking Time       Čas na rozmýšľanie AI           Čas na rozmýšlení AI            Czas myślenia AI
settings.timeout.30     Fast board read        Rýchle prečítanie plochy        Rychlé přečtení desky           Szybkie odczytanie planszy
settings.timeout.60     Balanced search        Vyvážené hľadanie               Vyvážené hledání                Wyważone szukanie
settings.timeout.120    Default thinking time  Predvolený čas na rozmýšľanie   Výchozí čas na rozmýšlení       Domyślny czas myślenia
settings.timeout.180    Tournament pace        Turnajové tempo                 Turnajové tempo                 Tempo turniejowe
settings.timeout.300    Longest think          Najdlhšie rozmýšľanie           Nejdelší rozmýšlení             Najdłuższe myślenie

--- 6.2 area `settings` — search steps, five descriptions ---
key                     en                     sk                              cs                              pl
settings.steps.title    Search Steps           Kroky hľadania                  Kroky hledání                   Kroki szukania
settings.steps.10       Quick tools            Rýchly priebeh                  Rychlý průběh                   Szybki przebieg
settings.steps.20       More tries             Viac pokusov                    Více pokusů                     Więcej prób
settings.steps.30       Focused search         Zamerané hľadanie               Zaměřené hledání                Skoncentrowane szukanie
settings.steps.50       Default search depth   Predvolená hĺbka hľadania       Výchozí hloubka hledání         Domyślna głębokość szukania
settings.steps.80       Max pressure           Maximálny tlak                  Maximální tlak                  Maksymalny nacisk

--- 6.3 area `settings` — board surface ---
key                          en                     sk                          cs                          pl
settings.board.title         Board Surface          Povrch plochy               Povrch desky                Powierzchnia planszy
settings.board.description   Saved on this device and used in the game board.
                             sk Uložené na tomto zariadení a použité v hracej ploche.
                             cs Uloženo na tomto zařízení a použito v hrací desce.
                             pl Zapisane na tym urządzeniu i używane na planszy.
settings.board.wood          Wood                   Drevo                       Dřevo                       Drewno
settings.board.woodDesc      Classic walnut grain   Klasická orechová kresba    Klasická orechová kresba    Klasyczny rysunek orzecha
settings.board.black         Black                  Čierna                      Černá                       Czarny
settings.board.blackDesc     Glossy night lacquer   Lesklý nočný lak            Lesklý noční lak            Błyszczący nocny lakier
settings.board.green         Green                  Zelená                      Zelená                      Zielony
settings.board.greenDesc     Dark tournament felt   Tmavá turnajová plsť        Tmavá turnajová plsť        Ciemne turniejowe sukno
settings.board.active        Active                 Aktívne                     Aktivní                     Aktywne

--- 6.4 area `settings` — the two toggles ---
key                          en                     sk                          cs                          pl
settings.toggle.on           On                     Zapnuté                     Zapnuto                     Włączone
settings.toggle.off          Off                    Vypnuté                     Vypnuto                     Wyłączone
settings.shiny.title         Shiny Effect           Lesklý efekt                Lesklý efekt                Efekt błysku
settings.shiny.description   Turn the live sheen off when you want a lighter GPU load.
                             sk Vypni živý lesk, ak chceš menšiu záťaž GPU.
                             cs Vypni živý lesk, když chceš menší zátěž GPU.
                             pl Wyłącz żywy błysk, gdy chcesz mniejsze obciążenie GPU.
settings.shiny.onDesc        Animated board sheen   Animovaný lesk plochy       Animovaný lesk desky        Animowany błysk planszy
settings.shiny.offDesc       Lower GPU load         Menšia záťaž GPU            Menší zátěž GPU             Mniejsze obciążenie GPU
settings.premium.title       Premium Look           Premium vzhľad              Premium vzhled              Wygląd premium
settings.premium.description Interactive amber spotlight for the game header and rack panel.
                             sk Interaktívne jantárové svetlo pre hlavičku hry a zásobník.
                             cs Interaktivní jantárové světlo pro hlavičku hry a zásobník.
                             pl Interaktywne bursztynowe światło dla nagłówka gry i stojaka.
settings.premium.onDesc      Premium interactive panels
                             sk Interaktívne premium panely
                             cs Interaktivní premium panely
                             pl Interaktywne panele premium
settings.premium.offDesc     Classic dark surfaces  Klasické tmavé povrchy      Klasické tmavé povrchy      Klasyczne ciemne powierzchnie

`settings.toggle.on` and `settings.toggle.off` are ONE pair reused by BOTH toggle panels. The
descriptions differ per panel, which is why there are four `*Desc` keys and only two label keys.

--- 6.5 area `settings` — shell and status ---
key                            en                     sk                    cs                    pl
settings.backToGame            Back to game           Späť do hry           Zpět do hry           Powrót do gry
settings.error.newGame         Could not start a fresh game right now.
                               sk Novú partiu sa teraz nepodarilo spustiť.
                               cs Novou partii se teď nepodařilo spustit.
                               pl Nie udało się teraz rozpocząć nowej partii.
settings.warn.accountSync      Account sync is unavailable right now. Settings still work locally on this device.
                               sk Synchronizácia účtu je momentálne nedostupná. Nastavenia fungujú lokálne na tomto zariadení.
                               cs Synchronizace účtu je momentálně nedostupná. Nastavení fungují lokálně na tomto zařízení.
                               pl Synchronizacja konta jest chwilowo niedostępna. Ustawienia działają lokalnie na tym urządzeniu.
settings.warn.rivalRepair      A free rival is selected on this device. Account preference could not be repaired yet.
                               sk Súper je vybraný na tomto zariadení. Preferenciu účtu sa zatiaľ nepodarilo opraviť.
                               cs Soupeř je vybraný na tomto zařízení. Preferenci účtu se zatím nepodařilo opravit.
                               pl Rywal jest wybrany na tym urządzeniu. Preferencji konta nie udało się jeszcze naprawić.

--- 6.6 area `overlay` — the stats bar, THREE parameterized keys ---
This is the leftover slice S6 reported at `AIThinkingOverlay.tsx:369-373`.

overlay.stats.tried     params { count: number }
  en (p) => `${p.count} tried`        sk (p) => `Skúsené: ${p.count}`
  cs (p) => `Zkoušené: ${p.count}`    pl (p) => `Sprawdzone: ${p.count}`
overlay.stats.valid     params { count: number }
  en (p) => `${p.count} valid`        sk (p) => `Platné: ${p.count}`
  cs (p) => `Platné: ${p.count}`      pl (p) => `Poprawne: ${p.count}`
overlay.stats.rejected  params { count: number }
  en (p) => `${p.count} rejected`     sk (p) => `Zamietnuté: ${p.count}`
  cs (p) => `Zamítnuté: ${p.count}`   pl (p) => `Odrzucone: ${p.count}`

⚠ WHY THESE ARE COLON-LABELS and not natural phrases, so nobody "improves" them into broken Slovak: a
word-for-word translation needs an adjective agreeing with the counted noun in number AND case across the
one/few/many forms — "1 skúsený ťah", "2 skúsené ťahy", "5 skúsených ťahov" — and no single adjective
form covers all three. A colon-label is grammatically inert at every count. This is the same decision
already shipped for `controls.tilesSelected` and `play.humanQueue.queueFor`.

The `rejected` span currently renders `""` when `rejectedCount === 0`. **Preserve that**: render the key
only when the count is greater than zero, exactly as today. Do not make it render "Zamietnuté: 0".

--- 6.7 GLOSSARY.md ---
Add all thirty-eight keys to the key table in the style the file already uses. Do not change the
terminology table. Add one line recording that the three `overlay.stats.*` keys are colon-labels for the
same grammatical reason as `controls.tilesSelected`, and one line recording that
`TIMEOUT_CHOICES` / `STEP_CHOICES` labels are deliberately NOT localized because they are unit
abbreviations and numbers.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/app/settings/page.tsx
  frontend/src/components/game/AIThinkingOverlay.tsx      (the stats bar ONLY, section 6.6)
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts

No file is created and none is deleted. If a gate fails in a file NOT on this list, STOP and report it
rather than editing that file.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- `AIThinkingOverlay.tsx` beyond the stats bar. Everything else in that file was localized last slice.
  ⛔ In particular `{humanState}` STAYS ENGLISH. It is AI telemetry prose produced inside the LOCKED
  `api/ai/move/route.ts` and re-derived by `describeAiTurnTelemetry` in `types.ts`. Localizing it needs
  the overlay keyed off `terminal_cause` / `completion_source` enums, which is an architecture change in
  its own deferred slice. A negative test, `AC-NO-TELEMETRY-KEY`, already asserts that no catalog key
  contains `providers exhausted`, `dead rack` or `legal rescue` — do not defeat it.
- `frontend/src/lib/types.ts`, `ai-move-stream.ts`, `api/ai/move/route.ts`, `prompts.ts` and its pinned
  SHA-256. Locked fork 2 plus the telemetry deferral.
- `frontend/src/components/settings/GameLanguagePanel.tsx` and its test. It is already localized and it
  exports `variantDisplayName`, which `/play` depends on. Do not touch it.
- `frontend/src/components/game/GameHistoryPanel.tsx`, `GameHistoryModal.tsx`, `ProfileModal.tsx`. The
  NEXT slice owns history and profile, together with the `uii-01-F03` hardcoded `en-US` dates. Measured
  inventory: 13, 3 and 14 strings. Do not start them.
- `frontend/src/app/game/[id]/page.tsx`, `play/page.tsx`, `waiting/[id]/page.tsx`, `draw/[id]/page.tsx`,
  `app/page.tsx`. All already localized.
- `frontend/src/lib/model-catalog.ts`, `ai-fallback.ts`. `resolveEligibleModelId`'s precedence and the
  fallback queue are load-bearing and correct.
- `frontend/src/lib/constants.ts` — TW/DW/TL/DL is the BOARD, not copy.
- `frontend/src/lib/api.ts`. Its 401 branch is a security property.
- `frontend/src/proxy.ts`, `security-headers.ts`. The nonce CSP is a later slice.
- `frontend/src/lib/i18n/locales.ts`, `plural.ts`, `translate.ts`, `LocaleProvider.tsx`, `index.ts`.
  You add catalog KEYS, not machinery. In particular do NOT add a fourth plural function.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- Anything under `backend/`. Django localization is a later slice.
- `frontend/package.json` and `package-lock.json`. NO new dependency.
- Do not bump the persist version. Do not add a locale to any `Intl.DateTimeFormat` call. Do not add
  aria-label, role, or alt.
- `settings/page.tsx` keeps its `rivalSectionRef` and its `?focus=rival` query handling even though the
  only inbound link was removed two slices ago. Leave both alone; removing them is not authorized here.
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
Evidence tier basis: highest string volume of any slice in this whole (38 keys x 4 locales) plus a
  structural change to three module-level constants and one local component's prop type; user-visible; no
  trust boundary, no durable data, no credential, no production effect. Rollback is `git revert` of one
  commit.
Combined implementation envelope: allowed
Independent acceptance: not-required. Evidence is NON-INDEPENDENT. Rendered acceptance is
  Cooperator-owned.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: frontend/src/lib/i18n/i18n.test.ts
New causal regression: the key-typed constant arrays and the three colon-label stats keys
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `386 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-SETTINGS-4    Every one of the five `settings.timeout.*` description keys, the five
                   `settings.steps.*` description keys and the three `settings.board.*` label keys
                   renders the exact authored string in all four locales.
  AC-TOGGLE-4      `settings.toggle.on` and `settings.toggle.off` render the authored string in all four
                   locales, and the four `*Desc` keys are all DISTINCT from each other in each locale.
                   The second half exists because the two toggle panels share their labels but not their
                   descriptions, and a copy-paste would silently make them identical.
  AC-STATS-4       The three `overlay.stats.*` keys interpolate the count in all four locales. Assert the
                   exact Slovak strings `Skúsené: 3`, `Platné: 3` and `Zamietnuté: 3`, and assert that
                   none of the sk / cs / pl forms contains the English words `tried`, `valid` or
                   `rejected`.
  AC-KEYTYPED      The three constant arrays are key-typed. Assert at RUNTIME that every
                   `descriptionKey` in `TIMEOUT_CHOICES` and `STEP_CHOICES`, and every `labelKey` and
                   `descriptionKey` in `BOARD_THEME_CHOICES`, resolves through `t()` to a NON-EMPTY
                   string in all four locales. `tsc` is the real gate; this test makes the invariant
                   visible to a reader and catches a key that exists but is empty.
                   ⚠ If the arrays are not exported, export them for the test rather than duplicating
                   them in the test file, and say so in the report.
  AC-NO-TELEMETRY-KEY  ALREADY EXISTS. It must keep passing with 38 more keys in the catalog. Do not
                   weaken it and do not add any key containing telemetry prose.
  AC-EXHAUST4      ALREADY EXISTS and must keep passing. Do not weaken it.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted. Do not be the first.

=====================================================================
11. GIT AUTHORITY
=====================================================================
On the PRIMARY route only, after all eight gates are green: exactly one commit and one push.
On the FALLBACK route: NO commit, NO push.

  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): localize the settings screen and the overlay stats bar
     Body: that three module-level constant arrays now carry `TextKey` values resolved at render time,
     which existing keys were reused, that the unit abbreviations and numbers are deliberately not
     localized, and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     6ca85de7ee1e5a1db33253eeb9e7e47922e2718a. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.

FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails in a file outside the section 7
allowlist; the key-typed arrays cannot be typed with `TextKey` without a circular import; a hook would
have to be called conditionally or from module scope; you conclude a new dependency or a fourth plural
function is required; the backend gates fail; `git ls-remote` shows main advanced; any instruction here
conflicts with AGENTS.md, .ap/AP.md, or observed repository truth; or you find yourself weakening an
existing test.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 08, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, and the count of strings routed through the catalog per file
 7. THE KEY-TYPED ARRAYS: show the new type of one array, confirm they stayed module-level constants,
    confirm `ChoiceGrid`'s prop type change affects no other file, and say whether you had to export them
    for `AC-KEYTYPED`
 8. WHICH EXISTING KEYS you reused rather than duplicating
 9. EXPLICIT CONFIRMATION that `{humanState}` is still untouched, that `types.ts` and `ai-move-stream.ts`
    are untouched, and that `AC-NO-TELEMETRY-KEY` still passes with 38 more keys present
10. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
11. gate results — eight on the primary route, seven plus a named omission on the fallback — with the
    pytest summary quoted verbatim and the vitest counts
12. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
13. any string you believe is wrong, or any container you believe a Slavic string will overflow — NAME
    it, do not change it. The choice grids are dense two- and five-column layouts and
    `settings.timeout.120` `Predvolený čas na rozmýšľanie` is the longest description; say where each
    renders and whether it fits.
14. ANY user-facing English string still left in `settings/page.tsx` after your work. List them exactly
    and classify each as: deliberately English per section 4 D5, an identity such as a model
    `display_name`, or a leftover you believe should have had a key. FIVE previous slices left strings
    behind because an Orchestrator inventory was incomplete, and this report field caught it every time.
15. deviations, risks, or missing evidence
16. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
17. Pre-Existing Failure Classification: none | <complete classification>
18. one smallest next step or review request
19. report justification: new-mutation
20. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.

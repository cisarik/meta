You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S6 — localize the in-game chrome: the header cluster and the AI overlay
Implementation authority: explicit
Independence required: no
Reasoning recommendation: medium. Basis — string extraction into a five-times exercised catalog
  contract. The only judgement calls are naming reuse over duplication and leaving one deferred string
  in English on purpose.
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

  git rev-parse HEAD                     -> d40b230e8071f609f1a26fbea70106664326673a
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> d40b230e8071f609f1a26fbea70106664326673a

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
6. frontend/src/lib/i18n/messages.en.ts and messages.sk.ts — the shape you extend, and the source of
   the seven keys section 5 tells you to REUSE
7. frontend/src/components/game/ScorePanel.tsx — in full, 440-ish lines
8. frontend/src/components/game/AIThinkingOverlay.tsx — in full, 377 lines
9. frontend/src/lib/types.ts lines 285-310 — `describeAiTurnTelemetry`, READ ONLY. It is why one
   overlay string stays English in this slice; see section 6.3.

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Localize the chrome the player looks at during every single turn: the game header cluster
(`ScorePanel`) and the AI thinking overlay. Both are in-game surfaces the player sees continuously, and
both are currently English in an otherwise Slovak, Czech or Polish game screen.

This slice is deliberately NARROW. The previous slice reported visible context usage above 70 percent,
so the settings screen is a separate later slice rather than being combined with this one.

=====================================================================
4. ACCEPTED DECISIONS
=====================================================================
D1  Four locales: en, sk, cs, pl. A key missing from any catalog is a `npm run typecheck` error, which
    is the mechanism working.
D2  Informal register in all three Slavic locales: sk and cs `ty`, pl 2nd person singular.
D3  Terminology from GLOSSARY.md. `AI`, `chat`, `provider`, `model`, `prompt` stay untranslated.
    points abbreviate to sk `b.` / cs `b.` / pl `pkt`.
D4  `vs` stays ENGLISH by glossary decision — universally understood and the container is ~2 characters
    wide. Do NOT translate it and do NOT add a key for it.
D5  `Libre` in `LogoMark` at ScorePanel.tsx:62 is part of the WORDMARK, not copy. The product is named
    "Libre Tiles" in every locale. Do NOT translate it and do NOT add a key for it.

=====================================================================
5. REUSE THESE SEVEN EXISTING KEYS — do not author duplicates
=====================================================================
Verified present in all four catalogs at this commit. Using them instead of new keys is required, not
optional: a second Slovak spelling of the same word is a defect waiting to drift.

```text
ScorePanel "Settings"       -> nav.settings          sk "Nastavenia"
ScorePanel "You"            -> chat.you              sk "Ty"
ScorePanel "New game"       -> game.newGame          sk "Nová partia"
ScorePanel "Starting..."    -> game.starting         sk "Spúšťam..."
overlay    "pts"            -> board.pts             sk "b."   cs "b."   pl "pkt"
```

⚠ `game.newGame` is spelled "New Game" in the en catalog while ScorePanel's literal is "New game".
Reuse the key anyway and accept the en casing difference — one key with one casing beats two keys.
Name it in the report.

=====================================================================
6. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
Translation is Orchestrator work in this project by Cooperator decision; no Worker translates. If you
believe a string is wrong or will overflow, NAME it in the report — do not change it.

--- 6.1 area `header` — the ScorePanel cluster ---
Nine new keys. Several of these are `IconTooltip` labels on icon-only buttons, so they are short by
necessity and their containers are tooltips rather than buttons.

key                    en                    sk                     cs                     pl
header.giveUp          Give up               Vzdať sa               Vzdát se               Poddaj się
header.givingUp        Giving up...          Vzdávam sa...          Vzdávám se...          Poddaję się...
header.giveUpTooltip   Give up current game  Vzdať túto partiu      Vzdát tuto partii      Poddaj tę partię
header.logout          Logout                Odhlásiť sa            Odhlásit se            Wyloguj się
header.loggingOut      Logging out...        Odhlasujem...          Odhlašuji...           Wylogowuję...
header.backToBoards    Back to boards        Späť na partie         Zpět na partie         Powrót do partii
header.profile         Profile               Profil                 Profil                 Profil
header.games           Games                 Partie                 Partie                 Partie

⚠ `header.games` is "Partie" in all three Slavic locales and `header.profile` is "Profil" in all three.
That is correct, not a copy-paste error — the words genuinely coincide. Do not "fix" them.

--- 6.2 area `overlay` — the AI thinking overlay ---
Four new keys.

key                    en                                 sk                              cs                              pl
overlay.aiThinking     AI Thinking                        AI premýšľa                     AI přemýšlí                     AI myśli
overlay.searching      Searching for moves...             Hľadám ťahy...                  Hledám tahy...                  Szukam ruchów...
overlay.best           Best                               Najlepší                        Nejlepší                        Najlepszy
overlay.bestBadge      BEST                               NAJLEPŠÍ                        NEJLEPŠÍ                        NAJLEPSZY
overlay.filtering      Filtering weak or invalid lines before showing a serious move...
                       sk Odfiltrúvam slabé a neplatné ťahy, kým nenájdem vážny ťah...
                       cs Odfiltrovávám slabé a neplatné tahy, dokud nenajdu vážný tah...
                       pl Odfiltrowuję słabe i nieprawidłowe ruchy, aż znajdę poważny ruch...

`overlay.best` and `overlay.bestBadge` are two keys on purpose: line 305 renders lowercase-styled `Best`
in a caption and line 122 renders an uppercase `BEST` badge. Slovak, Czech and Polish do not uppercase
by CSS as reliably as English does across these fonts, so the badge carries its own uppercased value
rather than relying on a `uppercase` class. Do not merge them and do not drop the `uppercase` class.

--- 6.3 ⛔ ONE STRING STAYS ENGLISH ON PURPOSE, and you must not localize it ---
`AIThinkingOverlay.tsx:210` reads `aiTurnTelemetry?.humanState` and renders it at `:234`. Those human
states — "backend found a legal rescue; repairing", "genuine dead rack — exchanging", "providers
exhausted" and three more — are produced inside `frontend/src/app/api/ai/move/route.ts`, which is
**LOCKED** (locked fork 2), and re-derived by `describeAiTurnTelemetry` in `frontend/src/lib/types.ts`,
which compares against the English prose at `types.ts:293-307`.

Localizing that line needs the overlay keyed off `terminal_cause` / `completion_source`, which ARE
stable enumerated values, instead of off prose. That is an enum-mapping redesign in a file adjacent to
the AI boundary, not string extraction, and folding it into a copy slice would turn a copy slice into an
architecture slice. It has its own deferred slice.

**So: localize the six strings in 6.1 and 6.2 and LEAVE `{humanState}` exactly as it is.** Do not touch
`types.ts`, do not touch `ai-move-stream.ts`, and do not add a key for any telemetry state. Confirm in
the report that you left it alone and that you understand why.

--- 6.4 GLOSSARY.md ---
Add the thirteen new keys to the key table in the style the file already uses. Do not change the
terminology table. Add one line recording that `overlay.bestBadge` exists separately from `overlay.best`
because the badge carries its own uppercased value, and one line recording that `{humanState}` in the
overlay is deliberately NOT localized pending the enum-keyed telemetry slice.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/components/game/ScorePanel.tsx
  frontend/src/components/game/AIThinkingOverlay.tsx
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts

No file is created and none is deleted. If a gate fails in a file NOT on this list, STOP and report it
rather than editing that file.

⚠ Both components already receive their strings as props or render them inline. If a string currently
arrives as a PROP from `game/[id]/page.tsx`, localize it at the component using `useT()` rather than
changing the caller — `game/[id]/page.tsx` is NOT on the allowlist. If that is impossible for a specific
string, STOP and report which one and why.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- `frontend/src/app/settings/page.tsx`. The settings copy remainder is the NEXT slice, roughly 40
  strings. Do not start it, even though ScorePanel links to it.
- `frontend/src/app/game/[id]/page.tsx`. It mounts both components you are changing. Do not follow the
  call and do not change a prop signature that would force an edit there.
- `frontend/src/lib/types.ts` and `frontend/src/lib/ai-move-stream.ts`. Section 6.3.
- `frontend/src/app/api/ai/move/route.ts`, `frontend/src/lib/prompts.ts`, its pinned SHA-256 and
  `MOVE_PROMPT_VERSION`. Locked fork 2.
- `frontend/src/components/game/GameHistoryPanel.tsx`, `GameHistoryModal.tsx`, `ProfileModal.tsx`.
  A later slice owns history and profile, together with the `uii-01-F03` hardcoded `en-US` dates.
- `frontend/src/lib/constants.ts` — TW/DW/TL/DL is the BOARD, not copy.
- `frontend/src/lib/api.ts`. Its 401 branch is a security property.
- `frontend/src/proxy.ts`, `security-headers.ts`. The nonce CSP is a later slice.
- `frontend/src/lib/i18n/locales.ts`, `plural.ts`, `translate.ts`, `LocaleProvider.tsx`, `index.ts`.
  You add catalog KEYS, not machinery.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
  ⚠ `AIThinkingOverlay` renders provider names through `providerBadgeLabel(...)`. Those are provider
  identities, not copy. Do not translate them and do not touch that function.
- Anything under `backend/`. Django localization is a later slice.
- `frontend/package.json` and `package-lock.json`. NO new dependency.
- Do not bump the persist version. Do not add a locale to any `Intl.DateTimeFormat` call (uii-01-F03,
  later slice). Do not add aria-label, role, or alt (uii-01-F02, later slice).
- Do not reformat, reorder imports in, or "tidy" anything beyond the named edits. In particular
  `AIThinkingOverlay` contains the `pingPongTileMotion` premium animation whose delay must remain `0`
  and whose reduced-motion path must remain a static tile — do not touch either.
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
Evidence tier: E1
Evidence tier basis: bounded reversible localized change in two components on a known path; the catalog
  contract is already exercised and gated by tsc; no trust boundary, no durable data, no credential, no
  production effect; rollback is `git revert` of one commit.
Combined implementation envelope: allowed
Independent acceptance: not-required. Evidence is NON-INDEPENDENT. Rendered acceptance is
  Cooperator-owned and the Orchestrator will request it.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: frontend/src/lib/i18n/i18n.test.ts
New causal regression: the overlay/header key set and the deliberate humanState exclusion
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `382 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-HEADER-4    All eight `header.*` keys render the exact authored string in all four locales.
  AC-OVERLAY-4   All five `overlay.*` keys render the exact authored string in all four locales.
  AC-BADGE-CASE  `overlay.bestBadge` is uppercase in every locale and `overlay.best` is not, in the
                 three Slavic locales. Assert `overlay.bestBadge` equals its own uppercase form for
                 each locale. This exists because relying on a CSS `uppercase` class for Slavic
                 diacritics is the thing this pair of keys avoids.
  AC-NO-TELEMETRY-KEY  A NEGATIVE test: assert that NO key in the en catalog contains any of the
                 telemetry prose fragments `providers exhausted`, `dead rack`, or `legal rescue`. This
                 pins the section 6.3 decision so a future slice cannot quietly localize the telemetry
                 through the copy catalog instead of through the enum redesign.
  AC-EXHAUST4    ALREADY EXISTS and must keep passing with every new key. Do not weaken it.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted. Do not be the first.

=====================================================================
11. GIT AUTHORITY
=====================================================================
On the PRIMARY route only, after all eight gates are green: exactly one commit and one push.
On the FALLBACK route: NO commit, NO push.

  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): localize the game header and the AI overlay
     Body: which existing keys were reused instead of duplicated, that `{humanState}` is deliberately
     left in English pending the enum-keyed telemetry slice, and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     d40b230e8071f609f1a26fbea70106664326673a. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.

FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails in a file outside the section 7
allowlist; a string can only be localized by editing `game/[id]/page.tsx`; a hook would have to be
called conditionally; you conclude a new dependency is required; the backend gates fail;
`git ls-remote` shows main advanced; any instruction here conflicts with AGENTS.md, .ap/AP.md, or
observed repository truth; or you find yourself weakening an existing test.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 07, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, and the count of strings routed through the catalog per file
 7. WHICH EXISTING KEYS you reused rather than duplicating, and any casing difference you accepted
 8. EXPLICIT CONFIRMATION that `{humanState}` in `AIThinkingOverlay` is untouched, that `types.ts` and
    `ai-move-stream.ts` are untouched, and one sentence on why localizing it needs the enum redesign
 9. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
10. gate results — eight on the primary route, seven plus a named omission on the fallback — with the
    pytest summary quoted verbatim and the vitest counts
11. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
12. any string you believe is wrong, or any container you believe a Slavic string will overflow — NAME
    it, do not change it. `overlay.filtering` is the longest string in this slice and `header.*` sit in
    icon tooltips; say where each renders and whether it fits.
13. ANY user-facing English string still left in the two components you touched. List them exactly, and
    classify each as: deliberately English per this prompt, a provider identity, or a leftover you
    believe should have had a key. FOUR previous slices left strings behind because an Orchestrator
    inventory was incomplete, and this report field caught it every time.
14. deviations, risks, or missing evidence
15. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
16. Pre-Existing Failure Classification: none | <complete classification>
17. one smallest next step or review request
18. report justification: new-mutation
19. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.

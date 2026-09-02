You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: S9 — localize the profile modal and close uii-01-F03
Implementation authority: explicit
Independence required: no
Reasoning recommendation: medium. Basis — the smallest remaining copy surface, but it carries the second
  half of a behavioural correction and it touches password-change wording, which is auth-adjacent.
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

  git rev-parse HEAD                     -> d806e313c7f5b6198452fa68afa5d079059b6f48
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> d806e313c7f5b6198452fa68afa5d079059b6f48

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
   ELEVEN keys section 4 tells you to REUSE. There are more reuses than new keys in this slice; read that
   section carefully before writing anything.
7. frontend/src/components/game/ProfileModal.tsx — IN FULL, ~330 lines
8. frontend/src/components/game/GameHistoryPanel.tsx lines 68-82 — `formatUpdatedAt`, the pattern the
   date fix in section 5 must follow. READ ONLY; do not edit that file.

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
Localize the profile modal into all four locales and correct the SECOND and last call site of
`uii-01-F03`, which closes that finding.

**This is the last copy slice in this logical whole.** After it, every user-facing string the frontend
owns is in four locales, and what remains is accessibility, Django localization and three security
residuals.

=====================================================================
4. ACCEPTED DECISIONS AND ELEVEN KEYS TO REUSE
=====================================================================
D1  Four locales: en, sk, cs, pl. A key missing from any catalog is a `npm run typecheck` error.
D2  Informal register in all three Slavic locales: sk and cs `ty`, pl 2nd person singular.
D3  ⛔ REUSE THESE ELEVEN EXISTING KEYS. All verified present in all four catalogs at this commit. This
    slice has MORE reuses than new keys, and duplicating any of them would be a defect — a second Slovak
    spelling of "Heslo" is exactly how a catalog starts to drift.
```text
    modal heading "Profile"          -> header.profile          sk "Profil"
    "Settings" button                -> nav.settings            sk "Nastavenia"
    "Close" button                   -> game.blocker.close      sk "Zavrieť"
    "Account" section heading        -> auth.eyebrow            sk "Účet"
    "Username" field label           -> auth.field.username     sk "Používateľské meno"
    "Password" section heading       -> auth.field.password      sk "Heslo"
    "Logout" button                  -> header.logout           sk "Odhlásiť sa"
    "Logging out..." button          -> header.loggingOut       sk "Odhlasujem..."
    "Password updated." notice       -> game.password.updated    sk "Heslo je zmenené."
    "Unable to update password."     -> game.password.failed     sk "Heslo sa nepodarilo zmeniť."
    the "Unknown" date fallback      -> history.unknownDate      sk "Neznáme"
```
D4  These are NOT copy and must NOT be given keys:
      every `autoComplete` value — `current-password`, `new-password`. They are HTML contract values that
      browsers and password managers parse. Translating one would break password-manager integration.
      `profile.username` and `profile.email` — user data.

=====================================================================
5. uii-01-F03, SECOND HALF — follow the pattern that already shipped
=====================================================================
`ProfileModal.tsx:18-27` `formatJoinedDate` calls
`new Intl.DateTimeFormat("en-US", { year: "numeric", month: "long", day: "numeric" })`, so a Slovak
interface renders `September 2, 2026`.

Slice S8 already corrected the sibling call site in `GameHistoryPanel.tsx`. **Follow that pattern
exactly** so the two functions stay recognisably the same shape:

  - `formatJoinedDate(value: string | null | undefined, locale: Locale)`;
  - map `"en"` to `"en-US"` and pass `"sk"`, `"cs"`, `"pl"` through unchanged. The mapping keeps today's
    English output byte-identical, so this correction can never be blamed for an English change;
  - the caller resolves the locale with `useLocale()`. `formatJoinedDate` is module-level and must NOT
    call a hook. Note that `memberSince` at :59 is a `useMemo` — the locale must be in its dependency
    list, or switching language would leave a stale date on screen;
  - both `"Unknown"` fallbacks become `history.unknownDate` per D3.

The Orchestrator measured `Intl` against this exact field set with Node in this repository, so you do not
need to and must not hand-build month names:

```text
en-US  September 2, 2026
sk     2. septembra 2026      <- GENITIVE, which is what a Slovak date requires
cs     2. září 2026           <- genitive
pl     2 września 2026        <- genitive
```

`2. september` would read wrong to a Slovak speaker. `Intl` gets it right. Do not add a date library —
the prompt forbids it and `Intl` is built in.

=====================================================================
6. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
SIXTEEN new keys. Counted programmatically from the table below, not estimated — and the
first draft of this prompt said FOURTEEN, which the Orchestrator's own key-count check caught before
issuing. If any prose number in this prompt disagrees with the enumerated table, THE TABLE WINS. Translation is
Orchestrator work in this project by Cooperator decision; no Worker translates. If you believe a string is
wrong or will overflow, NAME it in the report — do not change it.

--- 6.1 area `profile` — headings and labels ---
key                        en                          sk                        cs                        pl
profile.subtitle           Account details and password security in one place.
                           sk Údaje o účte a bezpečnosť hesla na jednom mieste.
                           cs Údaje o účtu a bezpečnost hesla na jednom místě.
                           pl Dane konta i bezpieczeństwo hasła w jednym miejscu.
profile.email              Email                       Email                     Email                     Email
profile.noEmail            No email set                Email nie je nastavený    Email není nastavený      Email nie jest ustawiony
profile.memberSince        Member since                Členom od                 Členem od                 Członkiem od
profile.password.subtitle  Update your login password without leaving the game.
                           sk Zmeň si prihlasovacie heslo bez toho, aby si opustil hru.
                           cs Změň si přihlašovací heslo bez toho, abys opustil hru.
                           pl Zmień hasło do logowania bez opuszczania gry.
profile.password.footnote  Stronger passwords make multiplayer accounts safer.
                           sk Silnejšie heslo lepšie chráni tvoj účet v hre proti ľuďom.
                           cs Silnější heslo lépe chrání tvůj účet ve hře proti lidem.
                           pl Silniejsze hasło lepiej chroni twoje konto w grze z ludźmi.

⚠ `profile.email` is `Email` in all four locales. Slovak, Czech and Polish all use it. That is not a
copy-paste error; do not invent `Elektronická pošta`.

--- 6.2 area `profile` — the password form ---
key                          en                       sk                        cs                        pl
profile.field.current        Current password         Súčasné heslo             Současné heslo            Aktualne hasło
profile.field.new            New password             Nové heslo                Nové heslo                Nowe hasło
profile.field.confirm        Confirm new password     Potvrď nové heslo         Potvrď nové heslo         Potwierdź nowe hasło
profile.ph.current           Current password         Súčasné heslo             Současné heslo            Aktualne hasło
profile.ph.new               At least 8 characters    Aspoň 8 znakov            Alespoň 8 znaků           Co najmniej 8 znaków
profile.ph.confirm           Repeat new password      Zopakuj nové heslo        Zopakuj nové heslo        Powtórz nowe hasło
profile.submit               Update password          Zmeniť heslo              Změnit heslo              Zmień hasło
profile.submitting           Updating...              Mením...                  Měním...                  Zmieniam...

⚠ `profile.field.current` and `profile.ph.current` carry the SAME text in every locale, and that is
correct: the field's visible label and its placeholder both say "Current password" today. They are two
keys rather than one because a label and a placeholder are different UI roles and a later designer may
legitimately want them to diverge. Do NOT collapse them into one key.

--- 6.3 area `profile` — the two client-side validation errors ---
key                          en                            sk                              cs                              pl
profile.error.allFields      Fill in all password fields.  Vyplň všetky polia s heslom.    Vyplň všechna pole s heslem.    Wypełnij wszystkie pola hasła.
profile.error.mismatch       New passwords do not match.   Nové heslá sa nezhodujú.        Nová hesla se neshodují.        Nowe hasła nie są zgodne.

⛔ THESE TWO ARE AUTH-ADJACENT AND HAVE A SECURITY PROPERTY. They are CLIENT-side validation of the form,
not server responses, so they may safely be specific about which field is wrong. What they must NOT do is
leak anything about the ACCOUNT — they must never say whether a username exists, and they must never
restate the current password's correctness. Neither authored string does. The server-side wording is
already handled by `game.password.failed` / `game.password.updated`, which this slice reuses unchanged, so
the `AC-SEC-1` and `AC-SEC-2` properties in `api.ts` are untouched. Confirm that in your report.

--- 6.4 GLOSSARY.md ---
Add the sixteen new keys to the key table in the style the file already uses. Do not change the
terminology table. Add one line recording that `profile.field.current` and `profile.ph.current` are
deliberately identical-but-separate, and one line recording that `uii-01-F03` is CLOSED by this slice with
both call sites now locale-aware.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/components/game/ProfileModal.tsx
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts

No file is created and none is deleted. If a gate fails in a file NOT on this list, STOP and report it
rather than editing that file.

⚠ `ProfileModal` is rendered from `app/game/[id]/page.tsx`, which is NOT on the allowlist. Do not change
its prop signature in a way that requires editing that caller. Its existing props — `profile`, `onClose`,
`onLogout`, `onOpenSettings`, `onChangePassword`, `loggingOut` — must all keep their current shapes.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- `frontend/src/components/game/GameHistoryPanel.tsx`. Its date site was corrected last slice. READ it
  for the pattern; do NOT edit it.
- `frontend/src/lib/api.ts`. Its `humanMessageForStatus` 401 branch is the `AC-SEC-1` / `AC-SEC-2`
  security property. This slice localizes CLIENT-side form validation only and must not touch the
  server-response mapping.
- Anything under `backend/`. The password validators' own text is Django's and belongs to the Django
  localization slice, which is why `game.password.failed` is a generic fallback and is reused unchanged.
- `frontend/src/components/game/AIThinkingOverlay.tsx`. Already localized except `{humanState}`, which
  STAYS ENGLISH pending the enum-keyed telemetry slice. `AC-NO-TELEMETRY-KEY` asserts no catalog key
  contains `providers exhausted`, `dead rack` or `legal rescue`; do not defeat it.
- `frontend/src/lib/types.ts`, `ai-move-stream.ts`, `api/ai/move/route.ts`, `prompts.ts` and its pinned
  SHA-256. Locked fork 2 plus the telemetry deferral.
- `frontend/src/lib/constants.ts` — TW/DW/TL/DL is the BOARD, not copy.
- `frontend/src/proxy.ts`, `security-headers.ts`. The nonce CSP is a later slice.
- `frontend/src/lib/i18n/locales.ts`, `plural.ts`, `translate.ts`, `LocaleProvider.tsx`, `index.ts`.
  You add catalog KEYS, not machinery.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts,
  ibm-watsonx.ts, ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- `frontend/package.json` and `package-lock.json`. NO new dependency, and specifically NO date library.
- Do not bump the persist version. Do not add aria-label, role, or alt — accessibility is the NEXT slice
  and adding a few names here would make that diff harder to review, not easier.
- Do not touch any `autoComplete` value. See D4.
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
  ⚠ Two previous slices lost a pytest summary to a session-handle timeout. Retain the handle, or re-run
  the exact authorized command once and quote the real summary. Do not report a summary you did not see.
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
Secret authority: NONE. Never read, print, or reference frontend/.env.local or backend/.env, and never
  let a password value from the form or a credential reach the report.
Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

=====================================================================
10. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: 14 keys x 4 locales plus the closing half of a behavioural correction, on a surface
  that includes password-change wording; user-visible; the auth SECURITY properties live in `api.ts`,
  which is untouched, so no trust boundary is crossed. No durable data, no credential, no production
  effect. Rollback is `git revert` of one commit.
Combined implementation envelope: allowed
Independent acceptance: not-required. Evidence is NON-INDEPENDENT. Rendered acceptance is
  Cooperator-owned.
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: frontend/src/lib/i18n/i18n.test.ts
New causal regression: the second date call site and the reuse discipline
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: not-used

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped`
  typecheck exit 0 · vitest at least `394 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-JOINED-LOCALE   THE CLOSING HALF OF uii-01-F03. For a fixed timestamp, `formatJoinedDate` must
                     return the literal `September 2, 2026` for `en`, and for `sk`, `cs` and `pl` it must
                     differ from the `en` value and must NOT contain the English month name `September`.
                     Assert the `en` value literally so the `en` -> `en-US` mapping is pinned. This must
                     fail against the hardcoded `"en-US"`.
  AC-JOINED-INVALID  A null value and an unparseable string both return the `history.unknownDate` value
                     for the active locale — sk `Neznáme`, not `Unknown`. This catches the easy mistake of
                     localizing the happy path and leaving the two fallbacks in English.
  AC-PROFILE-4       All sixteen new keys render the exact authored string in all four locales.
  AC-PROFILE-DUP     A deliberate assertion that `profile.field.current` and `profile.ph.current` are
                     EQUAL in every locale, and that `profile.email` equals `Email` in every locale. Both
                     duplications are intentional; this pins them so a future reader cannot "correct"
                     either into a false distinction. Same shape of defence as `AC-POLISH-DUP`.
  AC-EXHAUST4 and AC-NO-TELEMETRY-KEY  ALREADY EXIST and must keep passing. Do not weaken either.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted. Do not be the first.

=====================================================================
11. GIT AUTHORITY
=====================================================================
On the PRIMARY route only, after all eight gates are green: exactly one commit and one push.
On the FALLBACK route: NO commit, NO push.

  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): localize the profile modal and close the date locale defect
     Body: that `uii-01-F03` is now fully corrected with both call sites locale-aware, that `en` maps to
     `en-US` so English output is unchanged, that eleven existing keys were reused rather than
     duplicated, and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     d806e313c7f5b6198452fa68afa5d079059b6f48. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.

FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
12. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; a gate fails in a file outside the section 7
allowlist; localizing a string would force a prop-signature change in the caller; a hook would have to be
called from module scope; you conclude a new dependency or a date library is required; the backend gates
fail; `git ls-remote` shows main advanced; any instruction here conflicts with AGENTS.md, .ap/AP.md, or
observed repository truth; or you find yourself weakening an existing test.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker,
the smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 10, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, and the count of NEW keys versus REUSED keys
 7. THE uii-01-F03 CLOSURE: the new signature of `formatJoinedDate`, how the locale reaches it without a
    hook in module scope, whether the locale is in the `memberSince` `useMemo` dependency list, and the
    literal `en` output you asserted
 8. WHICH of the eleven keys you reused, and confirmation that you added no near-duplicate of any of them
 9. EXPLICIT CONFIRMATION that `frontend/src/lib/api.ts` is untouched and that the two localized
    validation errors are CLIENT-side form checks that disclose nothing about the account
10. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
11. gate results — eight on the primary route, seven plus a named omission on the fallback — with the
    pytest summary quoted verbatim and the vitest counts. Quote only a summary you actually saw.
12. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
13. any string you believe is wrong, or any container you believe a Slavic string will overflow — NAME
    it, do not change it. `profile.password.footnote` is the longest string in this slice; say where it
    renders and whether it fits.
14. ANY user-facing English string still left in `ProfileModal.tsx`. List them exactly and classify each
    as: an `autoComplete` HTML contract value, user data, or a leftover you believe should have had a key.
    SEVEN previous slices used this field; it caught a real leftover in four of them and came back clean
    in the last two.
15. deviations, risks, or missing evidence
16. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
17. Pre-Existing Failure Classification: none | <complete classification>
18. one smallest next step or review request
19. report justification: new-mutation
20. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may
close a logical whole. Your terminal report is your completion signal.

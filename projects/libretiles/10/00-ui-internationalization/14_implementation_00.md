You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 14
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: R7 — Django locale resolution driven by the client, plus uii-01-F17
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — this is the FIRST backend change in this logical whole. Three
  middleware-ordering constraints and two settings interact, and the value of the whole slice depends on a
  header the frontend does not currently send. A Worker who changes only the Django settings will produce a
  slice with green gates and zero user-visible effect.
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

  git rev-parse HEAD                     -> f40d8a0ef2a8c157fde7caddc4a6f64e2695d495
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> f40d8a0ef2a8c157fde7caddc4a6f64e2695d495

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19
4. .ap/AP_WORKER.md
5. backend/config/settings.py — ALL of it, but especially :121-140 INSTALLED_APPS, :141-154 MIDDLEWARE,
   :209-214 AUTH_PASSWORD_VALIDATORS, :216-219 the i18n/tz block, :238 SECURE_HSTS_SECONDS
6. backend/tests/test_security_settings.py :425-445 and backend/tests/test_admin_login_brake.py :165-180 —
   the two places that assert MIDDLEWARE positions
7. frontend/src/lib/api.ts — ALL of it. Especially `request()` at :224-284, `firstFieldMessage` at
   :93-123, `humanMessageForStatus` at :148-175, and `parseRetryAfterSeconds` at :125-135
8. frontend/src/lib/i18n/locales.ts — `LOCALE_COOKIE_NAME` at :4, `writeLocaleCookie` at :41-44, and
   `localeFromCookieValue`. ⚠ `writeLocaleCookie` ALREADY opens with
   `if (typeof document === "undefined") return;` at :42 — that is the exact guard shape section 6.2
   requires from you, in this exact file. Match it rather than inventing one.
9. frontend/src/components/game/GameHistoryPanel.tsx — the whole file, especially :293
10. frontend/src/lib/i18n/GLOSSARY.md — the terminology table at :29-34 is binding on your strings

=====================================================================
3. GOAL — ONE COHERENT OUTCOME
=====================================================================
The player's chosen interface language reaches Django, so the framework messages Libre Tiles does NOT own
come back in that language; and the one backend enum the player can actually see stops being raw.

⚠ THE TRAP THIS SLICE IS BUILT AROUND. Turning on `USE_I18N` and inserting `LocaleMiddleware` **changes
nothing at all by itself**, because `frontend/src/lib/api.ts` sends exactly two headers and neither is
`Accept-Language`, and it sets no `credentials`, so no cookie crosses from :3000 to :8000 either. Django
would resolve every request to `LANGUAGE_CODE`. All eight gates would be green and a Slovak player would see
the identical English. The frontend half is not a nice-to-have; it is what makes the backend half real.

=====================================================================
4. MEASURED SCOPE — the Orchestrator ran all of this; do not re-derive it
=====================================================================

--- 4.1 Current backend state, exact ---

```text
settings.py:216   LANGUAGE_CODE = "en-us"        -> resolves to the `en` catalog; there is no en_US dir
settings.py:218   USE_I18N = False
settings.py:219   USE_TZ = True                  leave it alone
LOCALE_PATHS      ABSENT       LANGUAGES  ABSENT       USE_L10N  ABSENT (gone in Django 5, always on)
backend/locale/   DOES NOT EXIST. Zero .po and zero .mo files anywhere under backend/ outside .venv.
config/urls.py    9 lines, no i18n_patterns, no set_language route. So LocaleMiddleware CANNOT redirect.
```

MIDDLEWARE, declared at `settings.py:141-154`, in order with line numbers:

```text
0  corsheaders.middleware.CorsMiddleware                        :142
1  django.middleware.security.SecurityMiddleware                :143
2  django.contrib.sessions.middleware.SessionMiddleware         :144   <-- insert AFTER this
3  django.middleware.common.CommonMiddleware                    :145   <-- and BEFORE this
4  django.middleware.csrf.CsrfViewMiddleware                    :146
5  django.contrib.auth.middleware.AuthenticationMiddleware      :147
6  django.contrib.messages.middleware.MessageMiddleware         :148
7  django.middleware.clickjacking.XFrameOptionsMiddleware       :149
8  config.middleware.AxesDrfLockoutFlagMiddleware               :152
9  axes.middleware.AxesMiddleware                               :153
```

`LocaleMiddleware` becomes the new index 3. Django requires it after `SessionMiddleware` and before
`CommonMiddleware`. The two axes entries MUST stay last and in that order.

⚠ Both existing MIDDLEWARE assertions use NEGATIVE indices — `MIDDLEWARE[-2]` and `MIDDLEWARE[-1]` at
`test_security_settings.py:435-436` and again at `test_admin_login_brake.py:172-173`. An index-3 insertion
therefore does not disturb them. Re-run both files explicitly and quote the result; the handout names this
as a required check.

--- 4.2 ⛔ ZERO backend strings are gettext-wrapped, and this slice does NOT wrap them ---

Eight patterns over `backend/**/*.py` excluding `.venv`, every one returning zero matches: `gettext`,
`ugettext`, `gettext_lazy`, `ngettext`, `pgettext`, `django.utils.translation`, `translation.activate`, and
the regex `(^|[^A-Za-z0-9_])_\(`. There is not one `from django.utils.translation import` in the project.

About 70 hardcoded English strings live in `game/services.py`, `gamecore/legality.py`,
`game/serializers.py` and `accounts/`. **They are OUT OF SCOPE and you must not wrap them.** The reasons,
so you do not think this is an oversight:

```text
1  `gamecore/legality.py:31-46` already exposes stable machine codes (REASON_*), and ~17 tests assert
   `reason_code` rather than prose. The right architecture for THOSE strings is a code the frontend
   translates through its own 294-key catalog, not a Django .po file — which is exactly how uii-01-F09
   (passKind) and uii-01-F17 (this slice) are being solved.
2  Wrapping them would mean authoring backend/locale/{sk,cs,pl}, roughly 210 new translations, and a
   `compilemessages` build step that needs gettext binaries on every deploy host.
3  Half-doing it — wrapping 70 strings and shipping no catalog — adds 70 lazy objects, risks lazy strings
   leaking into JSON serialization, and produces exactly zero visible change.
```

The Orchestrator records that as a routed residual. If you find yourself importing `gettext_lazy`, STOP.

--- 4.3 What WILL actually change, measured live under USE_I18N=True ---

The Orchestrator ran the real DRF exception and the real Django validators under a settings module that
imports `config.settings` and flips `USE_I18N = True`. These are observations, not predictions:

```text
[en] Request was throttled. Expected available in 3300 seconds.
[sk] Požiadavok bol obmedzený, z dôvodu prekročenia limitu. Expected available in 3300 seconds.
[cs] Požadavek byl limitován kvůli omezení počtu požadavků za časovou periodu. Expected available in 3300 seconds.
[pl] Żądanie zostało zdławione. Expected available in 3300 seconds.

[en] ['This password is too short. It must contain at least 8 characters.', 'This password is too common.',
      'This password is entirely numeric.']
[sk] ['Toto heslo je príliš krátke. Musí obsahovať aspoň 8 znakov.', 'Toto heslo je používané príliš často.',
      'Toto heslo pozostáva iba z číslic.']
[cs] ['This password is too short. It must contain at least 8 characters.',  <-- NOT translated, see 4.5
      'Heslo je příliš běžné.', 'Heslo se skládá pouze z čísel.']
[pl] ['To hasło jest za krótkie. Musi zawierać co najmniej 8 znaków.', 'To hasło jest zbyt powszechne.',
      'Hasło składa się wyłącznie z cyfr.']
```

Those password messages reach the player through `accounts/serializers.py:33` -> `accounts/views.py:60` ->
`frontend/src/components/game/ProfileModal.tsx:115`. That is the single most visible win in this slice.

Catalogs that exist in the venv and will take effect (`django-5.2.17`, `djangorestframework-3.17.0`,
`djangorestframework_simplejwt-5.5.1`, `django_axes-8.3.1`):

```text
django/conf/locale/{sk,cs,pl}            .po + .mo
django/contrib/auth/locale/{sk,cs,pl}    .po + .mo     <- the password validators
django/contrib/admin/locale/{sk,cs,pl}   .po + .mo + djangojs
rest_framework/locale/{sk,cs,pl}         .mo ONLY, 0 .po in the whole package. Compiled-only still works
                                         at runtime; a .po-only search would falsely report it absent.
rest_framework_simplejwt/locale          has `cs`, and `pl_PL` — NOT `pl`, so plain `pl` gets nothing.
                                         No `sk`, no `en`.
axes/locale                              has `pl` only. No `sk`, no `cs`, no `en`.
```

--- 4.4 ⛔ THE HANDOUT IS WRONG ABOUT R8, AND YOU MUST NOT "FIX" IT HERE ---

`93_orchestrator-handout.md` says the frontend's 429 parsing "works today only by luck: the Slovak DRF
catalog happens to leave that fragment untranslated. R7 makes the coupling live." **Measured: it is not
luck and R7 does not make it live.**

```text
rest_framework/exceptions.py:229-230   msgids are 'Expected available in {wait} second.' and
                                       '... {wait} seconds.'
the three catalogs                     NEITHER msgid is present in sk, cs or pl. Probed by loading each
                                       .mo and searching its catalog keys, not by grepping for prose.
exceptions.py:238-243                  DRF calls ngettext(singular.format(wait=wait), ...) — it FORMATS
                                       BEFORE the lookup, so the key contains the literal number and can
                                       never match a msgid anyway.
consequence                            the wait suffix stays English in all four locales, structurally.
                                       `parseRetryAfterSeconds` at api.ts:125-135 matched `3300` in en,
                                       sk, cs AND pl in the live probe.
```

So `uii-01-F01` stays a correctness improvement owned by **R8**, not an emergency. Do NOT touch
`parseRetryAfterSeconds`, and do NOT change `humanMessageForStatus`.

--- 4.5 A residual you will observe; report it, do not fix it ---

Czech does not translate `MinimumLengthValidator`. Cause, measured rather than guessed:
`django/contrib/auth/password_validation.py:118-119` uses the msgid
`"This password is too short. It must contain at least %d character."`, but the `cs` catalog in
`django-5.2.17` still carries the OLD msgid `"... at least %(min_length)d character."` — Slovak and Polish
were updated to `%d`, Czech was not. The Czech translation exists and is unreachable. Fixing it would mean
shipping a project-level `backend/locale/cs/` override plus `compilemessages`. Out of scope. Confirm the
observation in your report.

--- 4.6 uii-01-F17: `game_end_reason` ---

```text
definition   backend/game/models.py:58 — models.CharField(max_length=50, blank=True, default="")
             NO choices, NO enum, NO TextChoices.
values       ""                              services.py:566, session init
             "BAG_EMPTY_AND_PLAYER_OUT"      services.py:660, via GameEndReason.name
             "SIX_CONSECUTIVE_ZERO_SCORES"   services.py:660
             "NO_MOVES_AVAILABLE"            in the enum at gamecore/game.py:22-25 but UNREACHABLE through
                                             Django: services.py:639 passes no_moves_available=False
             "queue_cancelled"               services.py:1447
             "give_up"                       services.py:1518
render site  frontend/src/components/game/GameHistoryPanel.tsx:293, the ONLY one:
               : item.game_end_reason || t("history.hint.boardReady")
             The mobile card branch at :331-384 does not render it.
fixture      frontend/src/components/game/GameHistoryPanel.test.ts:27 uses "SIX_CONSECUTIVE_ZERO_SCORES"
```

⛔ **THE STORED VALUES MUST NOT CHANGE.** `services.py:1156` compares `== "give_up"` to derive the outcome
and `:1233` filters on it. This is a FRONTEND-ONLY mapping. No migration, no model change, no `choices`.

=====================================================================
5. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
FIVE new keys, all plain. Counted from the table. If any prose number disagrees, THE TABLE WINS.

```text
key                              en                       sk
history.endReason.bagEmpty       Bag and rack empty       Vrecko aj zásobník prázdne
history.endReason.noMoves        No moves available       Žiadny možný ťah
history.endReason.sixZero        Six scoreless turns      Šesť ťahov bez bodov
history.endReason.gaveUp         Resigned                 Partia vzdaná
history.endReason.queueCancelled Queue cancelled          Front zrušený

key                              cs                       pl
history.endReason.bagEmpty       Sáček i zásobník prázdné Woreczek i stojak puste
history.endReason.noMoves        Žádný možný tah          Brak możliwych ruchów
history.endReason.sixZero        Šest tahů bez bodů        Sześć ruchów bez punktów
history.endReason.gaveUp         Partie vzdána            Partia poddana
history.endReason.queueCancelled Fronta zrušena           Kolejka anulowana
```

⚠ FOUR THINGS ABOUT THESE STRINGS.

```text
1  BAG TERMINOLOGY comes from GLOSSARY.md:29-34 and is binding: bag = sk `vrecko`, cs `sáček`,
   pl `woreczek`; rack = sk `zásobník`, cs `zásobník`, pl `stojak`. Do NOT harmonize Czech to Slovak.
2  QUEUE TERMINOLOGY is already fixed by the shipped catalogs: sk `front` (masculine), cs `fronta`
   (feminine), pl `kolejka` (feminine) — see play.humanQueue.eyebrow and queue.leave in each catalog. The
   adjective agreement in the three translations above follows from that gender. Do not "correct" it.
3  EVERY STRING IS IMPERSONAL ON PURPOSE. `game_end_reason` does not say WHO resigned, so `Vzdal si` would
   assert something the data does not contain. Slovak informal `ty` register (decision 3) applies where a
   person is addressed; here no person is. This is the same discipline as the colon-label rule for counted
   nouns.
4  NO PLURAL FUNCTION IS NEEDED. `Šesť ťahov` is a fixed six, not a variable count. Do not reach for
   pluralSk here.
```

`GLOSSARY.md`: add all five keys to the table, and record in one line that `game_end_reason` is mapped in
the frontend from an unchanged backend value.

=====================================================================
6. WHAT TO BUILD
=====================================================================

--- 6.1 Backend: three settings edits, nothing else ---

```text
settings.py:218   USE_I18N = False -> True
settings.py       ADD `LANGUAGES` restricted to exactly the four shipped interface locales, in the
                  catalog's canonical order: en, sk, cs, pl. Without it Django's default LANGUAGES is the
                  full ~100-language list and LocaleMiddleware would honour Accept-Language: de.
                  Use Django's own gettext-free literal form — a plain list of (code, name) tuples with
                  English names. Do NOT import gettext_lazy for the names; section 4.2 forbids it and
                  these names are never displayed to a player.
settings.py:144/145  INSERT "django.middleware.locale.LocaleMiddleware" between them, as index 3.
LANGUAGE_CODE     LEAVE at "en-us". It is the correct fallback for a request with no Accept-Language.
LOCALE_PATHS      DO NOT ADD. There is no project catalog to point it at, and adding an empty one invites
                  a later reader to think one exists.
```

--- 6.2 Frontend: `api.ts` sends `Accept-Language` ---

Add the header inside `request()` at `api.ts:224-284`, beside the existing `Content-Type` and the
conditional `Authorization`.

```text
SOURCE OF TRUTH   the locale COOKIE, `LOCALE_COOKIE_NAME` = "libretiles_locale" at locales.ts:4. That is
                  the same source S3a made authoritative for rendering, so the header cannot disagree with
                  what the page shows.
WHY NOT THE STORE  api.ts is a plain module with no hooks. Threading a locale argument through every call
                  signature is invasive, and a module-level mutable locale was already rejected once in
                  this whole (slice S4 RIDER 2). Reading the cookie per request is derivation, not state.
WHY NOT THE COOKIE ITSELF  locales.ts:41-44 writes it with no `Domain`, and request() sets no
                  `credentials`, so :8000 can never see it. The header is the only channel.
⛔ SSR GUARD, MANDATORY  guard with `typeof document === "undefined"` and omit the header in that case.
                  This is not theoretical: i18n.test.ts string-renders SettingsPage, which imports
                  @/lib/api, in vitest's `node` environment. An unguarded `document.cookie` fails the
                  suite.
FALLBACK          when there is no cookie or its value is not one of the four locales, send nothing and
                  let Django fall back to LANGUAGE_CODE. Do NOT send "en" explicitly — an absent header
                  and an explicit default are different signals, and reusing `localeFromCookieValue`
                  would coerce an unknown value to "en" rather than reveal it.
```

Every consumer of `@/lib/api` is a `"use client"` component (verified: `app/page.tsx`, `play`, `waiting`,
`draw`, `game`, `settings`, and `ws.ts` which imports only `resolveApiBase`). The guard is for the test
environment, not for a real server render.

--- 6.3 uii-01-F17: the mapping ---

In `GameHistoryPanel.tsx`, replace the raw render at :293 with a keyed lookup. Follow the key-typed
constant pattern slice S7 established:

```text
EXPORT a module-level `Record<string, TextKey>` mapping the five stored values to the five new keys.
        Exporting it is fine — GameHistoryPanel.tsx already exports `formatUpdatedAt`, and it is a
        component file, not a page, so the App Router export restriction does not apply.
INCLUDE "NO_MOVES_AVAILABLE" even though section 4.6 proves it is unreachable through Django today. It is
        in the enum, it costs one line, and a later slice reaching it must not print a raw token.
FALLBACK ORDER, exactly:  a mapped value -> its translation
                          an UNMAPPED non-empty value -> the RAW STRING, unchanged
                          an empty value -> t("history.hint.boardReady"), which is today's behaviour
⛔ An unmapped value must NOT render empty and must NOT throw. Rendering a raw token is ugly; rendering
   nothing hides a backend change from whoever has to debug it.
```

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  backend/config/settings.py                             (6.1 — three edits, nothing else)
  frontend/src/lib/api.ts                                (6.2 — ONE header, nothing else)
  frontend/src/components/game/GameHistoryPanel.tsx       (6.3 — the mapping and the render site)
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts                     (section 10)

CREATE: nothing. DELETE: nothing. NO MIGRATION.

⛔ `backend/tests/` is NOT on this list. R7 changes no backend behaviour that the existing 381 tests
assert, and section 4.1 proves the two MIDDLEWARE assertions survive an index-3 insertion. If a backend
test fails, that is a FINDING to report, not a test to edit. Stop and report instead.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- ⛔ Do NOT import or use `gettext`, `gettext_lazy`, `ngettext`, `pgettext`, or
  `django.utils.translation` anywhere. Section 4.2. This slice adds ZERO wrapped strings.
- ⛔ Do NOT create `backend/locale/`, do NOT add `LOCALE_PATHS`, do NOT write a `.po`, do NOT run
  `makemessages` or `compilemessages`.
- ⛔ Do NOT change `game_end_reason`'s stored values, its model field, or add `choices`. Do NOT write a
  migration. `services.py:1156` and `:1233` compare against `"give_up"`.
- ⛔ Do NOT touch `parseRetryAfterSeconds` (api.ts:125-135) or `humanMessageForStatus` (:148-175). Those
  are R8. Section 4.4 proves they are not broken by this slice.
- ⛔ Do NOT touch the 401 branch of `api.ts`. It is a security property (AC-SEC-1/2). You are adding one
  header to `request()` and nothing else in that file.
- ⛔ Do NOT change `LANGUAGE_CODE`, `USE_TZ`, `TIME_ZONE`, `SECURE_HSTS_SECONDS`, or any security setting.
  R9 owns HSTS and R10 owns the CSP.
- ⛔ Do NOT reorder the two axes middleware entries or move anything except by the single insertion.
- ⛔ Do NOT add `set_language`, `i18n_patterns`, or any URL. `config/urls.py` stays 9 lines.
- ⛔ Do NOT set `credentials` on any fetch. Sending cookies cross-origin is a security change, not an i18n
  change, and CORS is configured without it deliberately.
- `frontend/src/lib/prompts.ts` and its pinned SHA-256, `ai-move-stream.ts`, `api/ai/move/route.ts`,
  `types.ts`. Locked fork 2.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts, ibm-watsonx.ts,
  ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- `LiveAnnouncer.tsx`, `TileRack.tsx`, `AIThinkingOverlay.tsx`, the four dialogs, `PremiumPicker.tsx`.
  Slices S11, R14 and R15 settled those; `aria-live` and `role="status"` must each still count exactly 1.
- No new dependency. `frontend/package.json`, `package-lock.json`, `backend/pyproject.toml`,
  `poetry.lock` unchanged.
- Do not reformat, reorder imports in, or "tidy" anything beyond the named edits.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files.

=====================================================================
9. COMMANDS, EXECUTION ROUTE, GIT
=====================================================================
Allowed, from frontend/: npm run typecheck, npx vitest run, npx vitest run <file>, npm run lint,
  npm run build. Allowed, from backend/: the four gates below, ONLY via the bounded deviation.

BOUNDED EXECUTION DEVIATION, mandatory and task-specific.
  Declared route that could NOT be used: `poetry run ...`, as documented in AGENTS.md.
  Why: the Cursor AppImage environment intercepts `python*` through inherited APPIMAGE / ARGV0 /
    APPDIR / PYTHONHOME variables.
  Exact alternate, from backend/:
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_security_settings.py tests/test_admin_login_brake.py
  Evidence class: reproduced-dynamic. Bounded authority: these five commands only.
  Stopping condition: if the alternate route also fails to resolve the in-project virtualenv, STOP and
    report; do not substitute ambient python, python3, or poetry run.

TRAP: `addopts = "-q"` is set. Do NOT pass another `-q`. pytest takes about 220 seconds; that is normal.
  Retain the session handle or re-run the exact authorized command once. Never quote a summary you did not
  see.
TRAP: run mypy on the FULL documented scope. This slice touches `settings.py`, so a mypy or
  `manage.py check` regression is a real signal, not noise.

⚠ REQUIRED PROOF THAT THE BACKEND HALF ACTUALLY RESOLVES A LANGUAGE. `manage.py check` passing proves
nothing about locale resolution. Demonstrate it with the Django test client through the real middleware
stack — a request with `HTTP_ACCEPT_LANGUAGE="sk"` to an endpoint that returns a framework message, and the
same request with `HTTP_ACCEPT_LANGUAGE="en"`, showing different bodies. Put that in a test (section 10),
not in a throwaway script, so it keeps protecting the behaviour.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. Immediately before `npm run build`, run
`ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, complete all eight gates, commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`. Run the
    other SEVEN gates, leave the candidate UNCOMMITTED, report `status: PARTIAL`, quote the exact `ss`
    output with the PID.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`; it matches the Cooperator's own server.

Forbidden commands: any git write beyond the block below, npm install / npm ci / npm add, poetry add,
  makemessages, compilemessages, any backend management command that writes data, any network call other
  than the two `git ls-remote` reads, any process kill.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

GIT — primary route only, after all eight gates are green: exactly one commit and one push.
  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       feat(i18n): Django resolves the player's locale, and end reasons are localized
     Body: that USE_I18N and LocaleMiddleware are inert without the client header and why, which bundled
     catalogs take effect, that no backend string was wrapped and why, that game_end_reason's stored
     values are unchanged and the mapping is frontend-only, and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     f40d8a0ef2a8c157fde7caddc4a6f64e2695d495. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.
FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
10. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: a Django settings and middleware change that alters response content for every
  authenticated client, plus one outbound header on every API call, plus a frontend-only enum mapping. No
  trust boundary is moved, no credential, no durable data, no migration. Rollback is `git revert` of one
  commit. Elevated above E1 because middleware ORDER is a correctness property and `axes` sits at the end
  of the same list.
Combined implementation envelope: allowed
Independent acceptance: not-required for the code.

⚠ EVIDENCE CEILING. The Cooperator has no screen reader and will not install one (decision 10), but that
does not apply here — this slice is fully testable. What you CANNOT prove from the suite: what a real
browser sends as `Accept-Language` when the cookie is absent, and how Django behaves behind the production
proxy. State those two limits; prove everything else.

Validation ladder: selected
Inspection and provenance: required
Existing focused tests: i18n.test.ts, GameHistoryPanel.test.ts, backend tests/test_api.py,
  tests/test_security_settings.py, tests/test_admin_login_brake.py
New causal regression: locale resolution through the real middleware stack, the outbound header, the
  end-reason mapping
Broad or full suite: required-because a project standing rule requires all eight gates
Runtime or testbed: Django test client only; no server is started

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `381 passed, 4 skipped` PLUS your new
    backend tests
  typecheck exit 0 · vitest at least `420 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

MANDATORY NEW TESTS. Each must FAIL before your implementation and PASS after, with the exact pre-fix
failure text reported.

  AC-LOCALE-RESOLVES  BACKEND. Through the Django test client and the real middleware stack, a request
                      carrying `HTTP_ACCEPT_LANGUAGE="sk"` produces a different framework message than the
                      same request with `"en"`. Prefer the password-change or register path so the
                      assertion rides on `AUTH_PASSWORD_VALIDATORS`, which section 4.3 measured. Assert
                      that the Slovak body is NOT equal to the English one AND that it contains a
                      distinctive Slovak substring — an inequality alone would pass on any accidental
                      difference.
  AC-LOCALE-FALLBACK  BACKEND. A request with NO `Accept-Language` still succeeds and yields the English
                      message. This is the regression that catches a mis-ordered middleware insertion.
  AC-MIDDLEWARE-ORDER BACKEND. `LocaleMiddleware` appears after `SessionMiddleware` and before
                      `CommonMiddleware`, and the last two entries are still the two axes entries in
                      order. Assert POSITIONS by index arithmetic, not a hardcoded list, so a future
                      insertion elsewhere does not silently pass.
  AC-ACCEPT-LANGUAGE  FRONTEND. `request()` sends `Accept-Language` matching the locale cookie, sends NO
                      such header when the cookie is absent or holds an unsupported value, and does not
                      throw when `document` is undefined. Assert the header from an intercepted fetch, not
                      from source text.
  AC-ENDREASON-4      FRONTEND. All five mapped values render the authored string in all four locales; an
                      unmapped value renders itself verbatim; an empty value renders
                      `history.hint.boardReady`. Assert the exact Slovak `Vrecko aj zásobník prázdne`, the
                      Czech `Sáček i zásobník prázdné` and the Polish `Woreczek i stojak puste` — the
                      three bag nouns are the thing most likely to be silently harmonized.
  AC-EXHAUST          ALREADY EXISTS and must keep passing: the four catalogs share one key set. 294 keys
                      becomes 299.

  ⛔ STILL MUST PASS UNTOUCHED, and this is the R7-specific trap: `test_api.py:102` asserts
  `"Current password is incorrect."`, `:1395` asserts `"Not your turn"`, `:1910` asserts
  `"Placements are not coverable by the current rack"`. Those are Libre Tiles strings and section 4.2
  forbids wrapping them, so all three MUST still pass. If any breaks, you wrapped something you should
  not have. Report it as a stopping condition rather than editing the test.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted, except by naming the
assertion and showing the property is still covered. Do not be the first to do it silently.

=====================================================================
11. STOPPING CONDITIONS AND TERMINAL REPORT
=====================================================================
Stop and report if: a section 1 gate value disagrees; any of the three `test_api.py` prose assertions
breaks; any backend test outside your allowlist fails; you find yourself importing `gettext_lazy`, creating
`backend/locale/`, or running `compilemessages`; you conclude a migration is needed; `LocaleMiddleware`
cannot be inserted without moving another entry; the `Accept-Language` header cannot be derived without a
module-level mutable or a signature change across call sites; `manage.py check` raises a new warning;
`git ls-remote` shows main advanced; any instruction here conflicts with AGENTS.md, .ap/AP.md, or observed
repository truth; or you find yourself weakening a test.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker, the
smallest authority expansion that would resolve it, and the exact first error text.

Begin the report with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 14, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, plus explicit confirmation that no migration was created, no
    `backend/locale/` exists, and `git diff --name-only backend/tests/` is EMPTY
 7. THE MIDDLEWARE LIST as it now stands, all eleven entries with indices, and the two negative-index
    assertions re-run with their quoted result
 8. THE MEASURED LOCALE EFFECT: for `en`, `sk`, `cs` and `pl`, the actual body your
    `AC-LOCALE-RESOLVES` path returns. Quote the strings. If any locale differs from section 4.3, say so —
    the Orchestrator measured that under a synthetic settings module and you are measuring the real one.
 9. THE HEADER: exactly how the locale is derived, where the SSR guard is, and what is sent when the
    cookie is absent, empty, or holds an unsupported value
10. confirmation that `parseRetryAfterSeconds` and `humanMessageForStatus` are untouched, and your own
    check of whether the 429 wait suffix is still English in sk, cs and pl after this slice — section 4.4
    predicts YES; contradict it if you measure otherwise
11. THE END-REASON MAPPING: the five values, the fallback order, and what an unmapped value renders
12. the pre-fix / post-fix table for every mandatory new test, with exact pre-fix failure text
13. the three `test_api.py` prose assertions: quoted, with confirmation each still passes
14. the Czech `MinimumLengthValidator` observation from section 4.5, confirmed or contradicted
15. gate results with the pytest summary quoted verbatim and the vitest counts, every change accounted for
16. commit and push result with both refs quoted, or an explicit statement that the candidate is
    uncommitted and why
17. ANY backend response string still reaching the player in English that this slice does not fix, and any
    security-header or `Vary`-header change you observe from adding `LocaleMiddleware`. NAME them; fix
    nothing outside section 7. Five previous slices found something an Orchestrator inventory had missed.
18. deviations, risks, or missing evidence
19. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
20. Pre-Existing Failure Classification: none | <complete classification>
21. one smallest next step or review request
22. report justification: new-mutation
23. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may close
a logical whole. Your terminal report is your completion signal.

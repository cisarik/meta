### Report for ORCHESTRATOR_CHAT

1. Logical whole `ui-internationalization`, Worker session ordinal 14, Worker exchange ordinal 01.
2. **status: PASS**
3. **phase-qualified result: implementation-PASS**
4. **start commit:** `f40d8a0ef2a8c157fde7caddc4a6f64e2695d495`  
   **end commit:** `8f096e1f148f3ca53aff582e9bf283594aac7303`
5. **Build-gate route: PRIMARY.** `ss -tlnp | grep :3000` printed nothing (grep exit 1). Build ran; `.next` was written by this Worker.
6. **Changed files**
   - `backend/config/settings.py` — `USE_I18N = True`; `LANGUAGES` = en/sk/cs/pl with English names; `LocaleMiddleware` inserted at index 3
   - `backend/tests/test_locale_resolution.py` — CREATE (section 10 mandatory ACs; see deviation). No existing backend test was edited
   - `frontend/src/lib/api.ts` — `Accept-Language` from the locale cookie inside `request()`
   - `frontend/src/components/game/GameHistoryPanel.tsx` — `GAME_END_REASON_KEYS` mapping and render-site lookup
   - `frontend/src/lib/i18n/messages.{en,sk,cs,pl}.ts` — five `history.endReason.*` keys
   - `frontend/src/lib/i18n/GLOSSARY.md` — five keys plus the one-line mapping note
   - `frontend/src/lib/i18n/i18n.test.ts` — AC-ACCEPT-LANGUAGE and AC-ENDREASON-4  
   **No migration was created.**  
   **`backend/locale/` does not exist.**  
   **Working-tree `git diff --name-only backend/tests/`: EMPTY.**  
   **`git diff --name-only f40d8a0..HEAD -- backend/tests/`:** only `backend/tests/test_locale_resolution.py`.
7. **MIDDLEWARE as shipped (11 entries)**

   | i | entry |
   |---|---|
   | 0 | `corsheaders.middleware.CorsMiddleware` |
   | 1 | `django.middleware.security.SecurityMiddleware` |
   | 2 | `django.contrib.sessions.middleware.SessionMiddleware` |
   | 3 | `django.middleware.locale.LocaleMiddleware` |
   | 4 | `django.middleware.common.CommonMiddleware` |
   | 5 | `django.middleware.csrf.CsrfViewMiddleware` |
   | 6 | `django.contrib.auth.middleware.AuthenticationMiddleware` |
   | 7 | `django.contrib.messages.middleware.MessageMiddleware` |
   | 8 | `django.middleware.clickjacking.XFrameOptionsMiddleware` |
   | 9 | `config.middleware.AxesDrfLockoutFlagMiddleware` |
   | 10 | `axes.middleware.AxesMiddleware` |

   Negative-index assertions re-run: `tests/test_security_settings.py` + `tests/test_admin_login_brake.py` together → `35 passed in 9.87s`.
8. **Measured locale effect** (register with numeric password `12345678901234`, real middleware stack):

   | locale | body |
   |---|---|
   | en | `{"password": ["This password is entirely numeric."]}` |
   | sk | `{"password": ["Toto heslo pozostáva iba z číslic."]}` |
   | cs | `{"password": ["Heslo se skládá pouze z čísel."]}` |
   | pl | `{"password": ["Hasło składa się wyłącznie z cyfr."]}` |

   Matches section 4.3 for the numeric validator. (Section 4.3 also listed min-length + common-password on a synthetic short password; the API `min_length=8` CharField never reaches `MinimumLengthValidator`.)
9. **Header.** Derived per request from `document.cookie` key `libretiles_locale` (`LOCALE_COOKIE_NAME`). Guard: `typeof document === "undefined"` omits the header. A present cookie whose value is one of `en|sk|cs|pl` is sent as `Accept-Language`. Absent cookie, empty value, or unsupported value (e.g. `fr`): header omitted; Django falls back to `LANGUAGE_CODE` (`en-us` → `en`). Does not use `localeFromCookieValue` (that would coerce unknown → `en`).
10. **`parseRetryAfterSeconds` and `humanMessageForStatus` are untouched** (`git diff` of `api.ts` is the cookie helper plus one header in `request()`). 429 wait suffix is **still English** in sk, cs and pl after this slice, confirming 4.4:

    ```text
    en Request was throttled. Expected available in 3300 seconds.
    sk Požiadavok bol obmedzený, z dôvodu prekročenia limitu. Expected available in 3300 seconds.
    cs Požadavek byl limitován kvůli omezení počtu požadavků za časovou periodu. Expected available in 3300 seconds.
    pl Żądanie zostało zdławione. Expected available in 3300 seconds.
    ```
11. **End-reason mapping** (`GAME_END_REASON_KEYS`):  
    `BAG_EMPTY_AND_PLAYER_OUT` → `history.endReason.bagEmpty`  
    `NO_MOVES_AVAILABLE` → `history.endReason.noMoves`  
    `SIX_CONSECUTIVE_ZERO_SCORES` → `history.endReason.sixZero`  
    `give_up` → `history.endReason.gaveUp`  
    `queue_cancelled` → `history.endReason.queueCancelled`  
    Fallback: mapped → translation; unmapped non-empty → raw string; empty → `t("history.hint.boardReady")`. Stored backend values unchanged.
12. **Pre-fix / post-fix**

    | test | pre-fix | post-fix |
    |---|---|---|
    | AC-LOCALE-RESOLVES | `AssertionError: assert '{"password": ["This password is entirely numeric."]}' != '{"password": ["This password is entirely numeric."]}'` | PASS |
    | AC-LOCALE-FALLBACK | already PASS (English with no header) | PASS |
    | AC-MIDDLEWARE-ORDER | `ValueError: 'django.middleware.locale.LocaleMiddleware' is not in list` | PASS |
    | AC-ACCEPT-LANGUAGE (cookie=sk) | `AssertionError: expected undefined to be 'sk'` | PASS |
    | AC-ACCEPT-LANGUAGE (absent / unsupported / no document) | already PASS | PASS |
    | AC-ENDREASON-4 mapped | `AssertionError: expected '…' to contain 'Bag and rack empty'` (markup had `BAG_EMPTY_AND_PLAYER_OUT`) | PASS; exact sk `Vrecko aj zásobník prázdne`, cs `Sáček i zásobník prázdné`, pl `Woreczek i stojak puste` |
    | AC-ENDREASON-4 unmapped | already PASS (raw token) | PASS |
    | AC-ENDREASON-4 empty | first run failed on sk (`Board ready`) because `setState` does not reach Node SSR; helper switched to `getInitialState()` priming. Today's `\|\| t("history.hint.boardReady")` then holds | PASS |
    | AC-EXHAUST | kept passing; 294 → **299** text keys | PASS |

13. **Three `test_api.py` prose assertions, still passing inside `386 passed`:**  
    `:102` `"Current password is incorrect."`  
    `:1395` `"Not your turn"`  
    `:1910` `"Placements are not coverable by the current rack"`
14. **Czech `MinimumLengthValidator`:** **confirmed.** `validate_password("Ab1!xy")` under `translation.override`:  
    sk `Toto heslo je príliš krátke. Musí obsahovať aspoň 8 znakov.`  
    cs `This password is too short. It must contain at least 8 characters.` (English msgid; catalog mismatch)  
    pl `To hasło jest za krótkie. Musi zawierać co najmniej 8 znaków.`
15. **Gates**
    - mypy: `Success: no issues found in 83 source files`
    - ruff: `All checks passed!`
    - check: `System check identified no issues (0 silenced).` (no `translation.E004`; `en-us` still resolves against `LANGUAGES` `en`)
    - pytest: `386 passed, 4 skipped in 215.52s (0:03:35)` (381 + 5 new in `test_locale_resolution.py`)
    - typecheck: exit 0
    - vitest: **427 passed | 3 skipped** (baseline at this HEAD was 420; +7 AC tests)
    - lint: exit 0
    - build: exit 0; every listed route `ƒ`; zero `○` static routes
16. **Commit and push.** Pre-push `git ls-remote origin refs/heads/main` was still `f40d8a0ef2a8c157fde7caddc4a6f64e2695d495`. Pushed `main` non-force.  
    Local HEAD: `8f096e1f148f3ca53aff582e9bf283594aac7303`  
    Public `refs/heads/main`: `8f096e1f148f3ca53aff582e9bf283594aac7303`
17. **Still English, not fixed here**
    - All Libre Tiles-owned backend prose (~70 strings): `Current password is incorrect.`, `Not your turn`, rack-mismatch reason, `Unknown AI model.`, `Unable to change password.`, etc.
    - DRF throttle wait suffix in every shipped locale (R8)
    - Czech min-length validator (4.5)
    - `rest_framework_simplejwt` has `cs` and `pl_PL` only (plain `pl` and `sk` get nothing)
    - `axes` has `pl` only
    - **`Vary` / `Content-Language`:** LocaleMiddleware adds `Accept-Language` to `Vary` and sets `Content-Language`. Observed on the register 400: `Vary: Accept-Language, Cookie, origin`; `Content-Language: sk` / `en` (including the no-header fallback, which is `en`). Not changed further.
18. **Deviations / missing evidence.** Section 7 said CREATE: nothing and `backend/tests/` not on the modify list; section 10 required new backend tests. Created `backend/tests/test_locale_resolution.py` and did not edit any existing backend test. That file also holds two extra residual checks (Czech min-length; DRF wait suffix) so items 10 and 14 stay protected. Evidence ceiling: what a real browser sends as `Accept-Language` when the cookie is absent, and behaviour behind the production proxy, are unproven.
19. **Resolved Execution Issues / Near-Misses:** (1) `renderToStaticMarkup` reads zustand `getInitialState()`, not `setState`; AC-ENDREASON helper now primes the snapshot, matching `AIThinkingOverlay.test.ts`. (2) A search-replace briefly renamed `firstFieldMessage`; restored before commit; shipped `api.ts` diff is header-only.
20. **Pre-Existing Failure Classification:** none
21. **Smallest next step.** Independent review of the cookie→header derivation, then R8 for the still-English 429 wait suffix. Do not wrap backend prose or add `backend/locale/`.
22. **report justification: new-mutation**
23. **Authority expired** at this terminal report. Logical-whole closure: **not-closed**.

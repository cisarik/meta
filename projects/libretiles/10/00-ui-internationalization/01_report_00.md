### Report for ORCHESTRATOR_CHAT

1. **logical whole** `ui-internationalization`, Worker session ordinal **01**, Worker exchange ordinal **01**
2. **status:** PASS
3. **phase-qualified result:** Implementation PASS
4. **start commit:** `19cfec9ed27c57e9499b71c55be6c2fb709b0c63`  
   **end commit:** `a5aff1214d97d28f2d27e55de5de19f09faf9c0e`
5. **changed files**
   - `frontend/src/lib/i18n/locales.ts` — locale union, cookie name, `detectBrowserLocale`, cookie resolver
   - `frontend/src/lib/i18n/plural.ts` — `pluralSk` / `pluralEn`
   - `frontend/src/lib/i18n/messages.en.ts` — English catalog (shape-defining)
   - `frontend/src/lib/i18n/messages.sk.ts` — Slovak catalog with `Record<TextKey, string>` and mapped `enFn` types
   - `frontend/src/lib/i18n/index.ts` — `t` / `tf` / `useLocale` / `useT`
   - `frontend/src/lib/i18n/GLOSSARY.md` — D2/D6/D7 plus the section-7 tables
   - `frontend/src/lib/i18n/i18n.test.ts` — AC-DETECT, AC-EXHAUST, AC-PLURAL unit + `tf` rendering
   - `frontend/src/hooks/useGameStore.ts` — `uiLocale`, cookie mirror, persist v3 migrate, first-visit detect-once
   - `frontend/src/hooks/useGameStore.test.ts` — AC-ONCE, AC-MIGRATE
   - `frontend/src/app/layout.tsx` — cookie-backed `lang` + `generateMetadata`
   - `frontend/src/app/page.tsx` — landing/auth through `useT()`; duplicate login-401 literal removed
   - `frontend/src/app/settings/page.tsx` — Interface language panel; Game variant relabel
   - `frontend/src/lib/api.ts` — locale-aware status/throttle fallbacks; 401 token distinction kept
   - `frontend/src/lib/api.test.ts` — AC-SEC-1, AC-SEC-2, rendered Slovak throttle
6. **Section 6 route: PRIMARY.** Cookie read in the root layout with the Next 16.3.4 server API; `<html lang={locale}>`; static `metadata` replaced by `generateMetadata`. Fallback `LocaleHtmlLang.tsx` was not created.  
   Deciding sentence, from `frontend/node_modules/next/dist/docs/01-app/03-api-reference/03-file-conventions/layout.md` line 156:  
   ``To access the request object, you can use [`headers`](/docs/app/api-reference/functions/headers) and [`cookies`](/docs/app/api-reference/functions/cookies) APIs in [Server Components](/docs/app/getting-started/server-and-client-components) and Functions.``
7. **Pre-fix / post-fix (mandatory new tests)**

   | ID | Pre-fix failure (verbatim) | Post-fix |
   |---|---|---|
   | AC-SEC-1 | `AssertionError: expected 'Invalid username or password' to be 'Nesprávne používateľské meno alebo heslo'` | PASS |
   | AC-SEC-2 | `AssertionError: expected 'Your session expired. Please sign in …' to be 'Prihlásenie vypršalo. Prihlás sa znov…'` | PASS |
   | AC-PLURAL (`tf` + `pluralSk`) | `Error: Cannot find module './index' imported from /home/agile/Projects/libretiles/frontend/src/lib/i18n/i18n.test.ts` | PASS |
   | AC-PLURAL (API 429 SK) | `AssertionError: expected 'Too many requests. Try again in about…' to match /minútu\.$/` / Received: `"Too many requests. Try again in about a minute."` | PASS |
   | AC-EXHAUST | same `Cannot find module './index'` suite load | PASS |
   | AC-DETECT | same suite load | PASS |
   | AC-ONCE | `TypeError: useGameStore.getState(...).setUiLocale is not a function` | PASS |
   | AC-MIGRATE | first: `AssertionError: expected undefined to be null`; after asserting persist `version === 3` still pre-implementation: `AssertionError: expected 2 to be 3` | PASS |
8. **Eight gates**
   - backend mypy: `Success: no issues found in 80 source files`
   - backend ruff: `All checks passed!`
   - backend check: `System check identified no issues (0 silenced).`
   - backend pytest: `328 passed, 4 skipped in 188.32s (0:03:08)`
   - frontend `npm run typecheck`: exit 0
   - frontend `npx vitest run`: **337 passed | 3 skipped** (25 files passed, 1 skipped)
   - frontend `npm run lint`: exit 0
   - frontend `npm run build`: exit 0. Port 3000 was free. Expected static→dynamic: `/`, `/play`, `/settings` are `ƒ`. Observed route table (root `cookies()` dynamizes the tree):

```
Route (app)
┌ ƒ /
├ ƒ /_not-found
├ ƒ /api/ai/judge
├ ƒ /api/ai/move
├ ƒ /api/models
├ ƒ /api/prompts
├ ƒ /draw/[id]
├ ƒ /game/[id]
├ ƒ /play
├ ƒ /settings
└ ƒ /waiting/[id]
ƒ Proxy (Middleware)
ƒ  (Dynamic)  server-rendered on demand
```

9. **commit and push:** one commit `a5aff12`, non-force fast-forward `19cfec9..a5aff12 main -> main`.  
   `git rev-parse HEAD` = `a5aff1214d97d28f2d27e55de5de19f09faf9c0e`  
   `git ls-remote origin refs/heads/main` = `a5aff1214d97d28f2d27e55de5de19f09faf9c0e	refs/heads/main`
10. **deviations / risks / missing evidence**
    - Root layout calls `t`’s catalogs (`enText`/`skText`) directly instead of importing `t` from `index.ts`, because `index.ts` also exports React hooks and a Server Component must not import that module. Lookup semantics match `t()`.
    - Extra helpers beyond the named signatures: `localeFromCookieValue`, `adoptBrowserLocaleIfUnset`. Needed for layout and AC-ONCE without a React renderer (vitest `environment: "node"`).
    - `pluralSk` follows the prompt’s `|trunc(n)| === 1 | 2..4 | else` rule, **not** CLDR Slovak (21/101 are `many` here). Authorized; later slices may want CLDR.
    - Layouts do not rerender on client navigation. `setUiLocale` updates the store and cookie immediately (UI copy follows), but `<html lang>` and metadata wait for the next full document request. Not a third route.
    - Cookie write is guarded and untested under jsdom; vitest is node. Mirror cookie is a routing hint only, as specified (no `Secure`, no `HttpOnly`).
    - Django field messages on 400/409 remain English. Untranslated chrome outside this slice remains English. `proxy.ts` untouched.
    - INFOSEC R1, non-independent: tokenless 401 still one string in both locales; session 401 remains distinct; no user-enumeration fragments in SK login copy.
    - Visible context usage for this exchange was high (installed Next 16.3.4 docs + AP sections + full UI/API files); treat as **above 70%**.
11. **Resolved Execution Issues / Near-Misses:** AC-PLURAL’s first draft expected CLDR “one” for 21 and 101; that contradicted the specified helper. Tests were aligned to `|trunc(n)|` **before** claiming PASS. Residual: helper is not linguistically complete Slovak.
12. **Pre-Existing Failure Classification:** none
13. **smallest next step:** Cooperator smoke on Settings → Interface language, then reload `/` and confirm `html lang`, title, landing copy, and a tokenless 401. Later slice still owns remaining English chrome, URL prefixes, and Django localization.
14. **report justification:** new-mutation
15. **authority-expiry:** This Worker’s authority expired with this report. I will take no further action without a new complete prompt.

Logical whole `ui-internationalization` is **not closed**.

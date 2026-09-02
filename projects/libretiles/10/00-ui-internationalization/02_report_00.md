### Report for ORCHESTRATOR_CHAT

1. Logical whole `ui-internationalization`, Worker session ordinal 02, Worker exchange ordinal 01.
2. Status: **PASS**
3. Phase-qualified result: **implementation-PASS**
4. Start commit: `61c9f09377011525105d747b88d603bff5d832e6`. End commit: `5a96b5ed79c10b60a720ab89ae11d6979b98ec0a`.
5. Changed files:

| Path | Purpose |
|---|---|
| `frontend/src/lib/i18n/translate.ts` | React-free `t`/`tf` over a `Record<Locale, …>` of four catalogs |
| `frontend/src/lib/i18n/LocaleProvider.tsx` | Client provider: server locale into context; sync effect |
| `frontend/src/lib/i18n/messages.cs.ts` | Czech catalog (informal `ty`, tile = kámen) |
| `frontend/src/lib/i18n/messages.pl.ts` | Polish catalog (informal 2nd person, tile = płytka) |
| `frontend/src/lib/i18n/locales.ts` | Four locales; derived `isLocale`/`detectBrowserLocale`; `writeLocaleCookie`; `localeSyncDecision` |
| `frontend/src/lib/i18n/plural.ts` | `pluralPl`; `pluralCs = pluralSk` with the deliberate-reuse comment |
| `frontend/src/lib/i18n/index.ts` | `useLocale()` prefers server context; re-exports `t`/`tf` from `translate.ts` |
| `frontend/src/lib/i18n/messages.en.ts` / `messages.sk.ts` | Endonyms + `cs`/`pl` name keys |
| `frontend/src/lib/i18n/GLOSSARY.md` | Four-locale terminology table, Polish plural contract, PFS/ČAS sources |
| `frontend/src/lib/i18n/i18n.test.ts` | AC-SYNC, AC-EXHAUST4, AC-PLURAL-PL/CS, AC-DETECT4, AC-ISLOCALE, AC-SEC catalogs |
| `frontend/src/app/layout.tsx` | Cookie → `t()` metadata; wrap children in `LocaleProvider` |
| `frontend/src/app/settings/page.tsx` | 2×2 en/sk/cs/pl picker; `setUiLocale` then `router.refresh()` |
| `frontend/src/hooks/useGameStore.ts` | Cookie write extracted to `writeLocaleCookie` |
| `frontend/src/lib/api.test.ts` | AC-SEC-1/2 extended to four locales |

`useGameStore.test.ts` was on the allowlist for typecheck only and was not mutated. AC-ONCE still passes unchanged.

6. **Loop-termination argument.** `router.refresh()` re-runs the server layout, which re-reads `libretiles_locale` and re-renders `LocaleProvider` with a new `value`. The effect writes that cookie to `resolved` *before* refreshing, so the only server input for the next layout is already `resolved`. The next `localeSyncDecision(serverLocale, resolved)` therefore hits the identity branch `{ cookie: null, refresh: false }` and does not refresh again. AC-SYNC-3 is that argument as a test: every mismatch’s `first.cookie` fed back as the next server locale yields `{ cookie: null, refresh: false }`.

   Authorized `router.refresh()` sentence, Next.js 16.3.4 installed docs:  
   `frontend/node_modules/next/dist/docs/01-app/03-api-reference/04-functions/use-router.md:46` — `` `router.refresh()`: Refresh the current route. Making a new request to the server, re-fetching data requests, and re-rendering Server Components. ``

   The provider also waits for Zustand persist hydration before calling `adoptBrowserLocaleIfUnset` (same pattern the old `useLocale()` effect used). Without that wait, a stored locale would look unset on first paint and first-visit detection would override an explicit choice (D7). `onRehydrateStorage` still calls `adoptBrowserLocaleIfUnset` as required.

7. **SSR probe** (`npx next start -H 127.0.0.1 -p 3412`, `/`, stopped by exact PID: pre-fix `38802`, post-fix `41824`).

   Pre-fix (`61c9f09`):

   | Case | Cookie / AL | `<html lang>` | `<title>` | Sign In | Prihlásiť sa | Přihlásit se | Zaloguj się |
   |---|---|---|---|---|---|---|---|
   | A | no cookie, `Accept-Language: sk-SK,sk;q=0.9` | `en` | English meta.title | 1 | 0 | 0 | 0 |
   | B | `libretiles_locale=sk` | `sk` | Slovak meta.title | **1** | **0** | 0 | 0 |
   | C | `libretiles_locale=cs` | `en` | English | 1 | 0 | 0 | 0 |
   | D | `libretiles_locale=pl` | `en` | English | 1 | 0 | 0 | 0 |
   | E | `libretiles_locale=fr` | `en` | English | 1 | 0 | 0 | 0 |

   Case B is uii-01-F04: Slovak `lang`/`title`, English body. C and D were not valid locales at baseline (`isLocale` rejected them; `localeFromCookieValue` fell through to `en`). Recorded as observed fallback, not invented Czech/Polish counts.

   Post-fix (`5a96b5e`):

   | Case | `<html lang>` | `<title>` | Sign In | Prihlásiť sa | Přihlásit se | Zaloguj się |
   |---|---|---|---|---|---|---|
   | A | `en` | Libre Tiles — Web Libre Tiles with AI and Live Multiplayer | 1 | 0 | 0 | 0 |
   | B | `sk` | Libre Tiles — slovná hra na webe s AI a živým multiplayerom | **0** | **1** | 0 | 0 |
   | C | `cs` | Libre Tiles — slovní hra na webu s AI a živým multiplayerem | 0 | 0 | **1** | 0 |
   | D | `pl` | Libre Tiles — gra słowna w przeglądarce z AI i multiplayerem na żywo | 0 | 0 | 0 | **1** |
   | E | `en` | Libre Tiles — Web Libre Tiles with AI and Live Multiplayer | 1 | 0 | 0 | 0 |

8. **Mandatory new tests, pre-fix → post-fix**

   | Test | Pre-fix | Post-fix |
   |---|---|---|
   | AC-DETECT4 | `AssertionError: expected 'en' to be 'cs'` at `detectBrowserLocale(["cs"])` | PASS |
   | AC-ISLOCALE | `AssertionError: expected false to be true` at `isLocale("cs")` | PASS |
   | AC-SYNC-1, AC-SYNC-2, AC-SYNC-3, AC-EXHAUST4, AC-PLURAL-PL, AC-PLURAL-CS, AC-PLURAL-PL2, AC-SEC four-locale catalog checks | Suite failed to load: `Error: Cannot find module './messages.cs' imported from …/i18n.test.ts` | PASS |
   | AC-SEC-1-4 / AC-SEC-2-4 (`api.test.ts`) | Not executable as four-locale tests until `cs`/`pl` existed; two-locale predecessors were green | PASS |
   | AC-ONCE | Already green on baseline; still green | PASS (unchanged) |

   The previous AC-DETECT assertion `cs-CZ → en` was **updated** into AC-DETECT4 (`cs-CZ → cs`), not deleted. Keeping both would have forced a post-fix failure of a two-locale leftover. That is a locale-set expansion, not a weakened invariant.

9. **Eight gates**

   | Gate | Result |
   |---|---|
   | backend mypy | `Success: no issues found in 83 source files` |
   | backend ruff | `All checks passed!` |
   | backend check | `System check identified no issues (0 silenced).` |
   | backend pytest | `381 passed, 4 skipped in 215.30s (0:03:35)` |
   | frontend typecheck | exit 0 |
   | frontend vitest | `362 passed \| 3 skipped (365)` (Test Files `28 passed \| 1 skipped (29)`) |
   | frontend lint | exit 0 |
   | frontend build | exit 0; every app route remains `ƒ` (Dynamic) server-rendered on demand. No route became `○`. |

   Build route table:

   ```
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

10. Commit and push: `git push origin main` fast-forward `61c9f09..5a96b5e`.  
    Pre-push `git ls-remote origin refs/heads/main` = `61c9f09377011525105d747b88d603bff5d832e6`.  
    After push, both `git rev-parse HEAD` and `git ls-remote origin refs/heads/main` = `5a96b5ed79c10b60a720ab89ae11d6979b98ec0a`. Working tree clean, `## main...origin/main`.

11. Deviations / risks / leftover (not authorized to fix):
    - LocaleProvider hydration wait, as in §6 — required for D7, not a second source of truth.
    - `frontend/public/hu.png` remains committed and unreferenced (D1).
    - Game chrome (`game/[id]`, ScorePanel, Board, chat, …) is still English; later slices own that copy.
    - `Intl.DateTimeFormat` locales and aria/alt work remain later (uii-01-F03 / uii-01-F02).
    - Independent rendered acceptance is Cooperator-owned; this session’s evidence is non-independent as declared.

12. Resolved Execution Issues / Near-Misses: one near-miss — an early `Write` targeted `index.ts` with Polish catalog contents; it was overwritten with the real `index.ts` in the same implementation pass before any gate or commit. Cause: parallel write path mix-up. Resolution: `messages.pl.ts` and `index.ts` both present and correct in `5a96b5e`. Residual risk: none in the published tree.

13. Pre-Existing Failure Classification: none.

14. Smallest next step: Cooperator rendered acceptance of the settings 2×2 language grid (endonyms, informal Slavic copy, no Hungarian tile) and a logged-out landing load with `libretiles_locale=sk|cs|pl` to confirm the SSR agreement the loopback probe already measured. Later slices still own remaining game-surface copy.

15. Report justification: new-mutation.

16. Authority-expiry statement: this Worker’s authority expired with this report. I will take no further action without a new complete prompt.

Logical-whole closure: not-closed.
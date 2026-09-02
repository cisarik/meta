### Report for ORCHESTRATOR_CHAT

1. Logical whole: `ui-internationalization`; Worker session ordinal: `10`; Worker exchange ordinal: `01`.

2. Status: PASS.

3. Phase-qualified result: implementation-PASS. Evidence is non-independent. Result commit: `8f440221b757bc142cb26391875c1361492da419`.

4. Start commit: `d806e313c7f5b6198452fa68afa5d079059b6f48`. End commit: `8f440221b757bc142cb26391875c1361492da419`.

5. Build-gate route: PRIMARY. Exact `ss -tlnp | grep :3000` output was empty (`""`, exit 1). No listener was present, so `npm run build` ran and passed.

6. Changed files:

   - `ProfileModal.tsx`: localized owned copy and made joined dates locale-aware.
   - Four message catalogs: added exactly 16 `profile.*` keys per locale.
   - `GLOSSARY.md`: documented all 16 keys, intentional duplicates, and `uii-01-F03` closure.
   - `i18n.test.ts`: added four causal regression controls.

   New keys: 16. Existing keys reused: 11. No files were created or deleted.

7. `uii-01-F03` closure:

   - New signature: `formatJoinedDate(value: string | null | undefined, locale: Locale)`.
   - `ProfileModal` resolves `locale` with `useLocale()` inside the component and passes it to the module-level formatter.
   - No hook is called from module scope.
   - `memberSince` dependencies are `[profile?.date_joined, locale]`.
   - English maps to `en-US`; asserted output is exactly `September 2, 2026`.
   - Both formatter fallback paths use `history.unknownDate`.
   - Both known date call sites are now locale-aware.

8. Reused keys:

   - `header.profile`
   - `nav.settings`
   - `game.blocker.close`
   - `auth.eyebrow`
   - `auth.field.username`
   - `auth.field.password`
   - `header.logout`
   - `header.loggingOut`
   - `game.password.updated`
   - `game.password.failed`
   - `history.unknownDate`

   No near-duplicate key was added for any of these.

9. `frontend/src/lib/api.ts` is untouched. The localized `profile.error.allFields` and `profile.error.mismatch` messages are client-side form checks only. They reveal neither account existence nor current-password correctness. `AC-SEC-1` and `AC-SEC-2` server-response behavior remains unchanged.

10. Mandatory regression evidence:

| Test | Pre-fix result | Post-fix result |
|---|---|---|
| `AC-JOINED-LOCALE` | `AssertionError: expected 'September 2, 2026' not to be 'September 2, 2026'` | PASS |
| `AC-JOINED-INVALID` | `AssertionError: expected 'Unknown' to be 'Neznáme'` | PASS |
| `AC-PROFILE-4` | `AssertionError: expected undefined to be 'Account details and password security…'` | PASS |
| `AC-PROFILE-DUP` | `AssertionError: expected undefined to be 'Email'` | PASS |

Focused post-fix result: `49 passed (49)`. The formatter was exported as a test seam before the red run; its pre-fix behavior remained unchanged.

11. Gate results:

   - mypy: `Success: no issues found in 83 source files`
   - ruff: `All checks passed!`
   - Django check: `System check identified no issues (0 silenced).`
   - pytest: `381 passed, 4 skipped in 215.38s (0:03:35)`
   - typecheck: exit 0
   - Vitest: `398 passed | 3 skipped`
   - lint: exit 0
   - build: exit 0; all listed routes were `ƒ`, with zero `○` static routes

12. Commit and push:

   - Commit: `8f440221b757bc142cb26391875c1361492da419`
   - Push: fast-forward `main -> main`
   - Local `HEAD`: `8f440221b757bc142cb26391875c1361492da419`
   - Public `refs/heads/main`: `8f440221b757bc142cb26391875c1361492da419`
   - Final worktree: clean and synchronized with `origin/main`.

13. String/layout review: no authored string appears wrong. `profile.password.footnote`, the longest string, renders in the right-hand password card beside the submit button. The containing row uses `flex-wrap`, and the text can wrap at spaces; static layout inspection found no overflow risk. Rendered acceptance remains Cooperator-owned.

14. User-facing English left in `ProfileModal.tsx`: none owned by the frontend.

   - `autoComplete="current-password"` and `autoComplete="new-password"` remain untranslated HTML contract values.
   - `profile.username` and `profile.email` remain user data.
   - A dynamic `result.error` may still display backend-provided text; its generic frontend fallback is localized through `game.password.failed`.

15. Deviations, risks, or missing evidence: no product or scope deviation. No dependency was added. No browser/rendered acceptance was authorized, so visual confirmation is missing by design.

16. Resolved Execution Issues / Near-Misses: the first backend pytest invocation yielded before its summary, and the command wrapper did not expose its session handle. The exact authorized command was rerun once under the prompt’s explicit timeout fallback; its handle was retained through completion and the real summary is quoted above. Residual risk: none.

17. Pre-Existing Failure Classification: none.

18. Smallest next step: ORCHESTRATOR reviews public commit `8f440221b757bc142cb26391875c1361492da419` and routes Cooperator-rendered acceptance if desired.

19. Report justification: new-mutation.

20. Authority expired upon this terminal report. No further autonomous work is authorized.

Logical-whole closure: not-closed.
### Report for ORCHESTRATOR_CHAT

1. Logical whole `ui-internationalization`, Worker session ordinal 17, Worker exchange ordinal 01.
2. **status: PASS**
3. **phase-qualified result: implementation-PASS**
4. Start commit `cb4efed9e1c3859e7839b5adb18a605a6c3ef102` · end commit `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a`
5. **Build-gate route: PRIMARY** (nothing listening on 3000). Exact `ss -tlnp | grep :3000` output: empty (`grep` exit 1).
6. Changed files (`git diff --name-only backend/` quoted empty: no output):
   - `frontend/src/app/api/models/route.ts` — honest upstream status / 502; `cache: "no-store"`; drop `revalidate: 60`
   - `frontend/src/app/api/prompts/route.ts` — same failure contract
   - `frontend/src/app/api/catalog-proxy.test.ts` — first tests for either route
   - `frontend/src/app/play/page.tsx` — `reconcileRival` reports reachability; both call sites choose the new key
   - `frontend/src/app/settings/page.tsx` — notice uses existing `catalogResult.ok`
   - `frontend/src/lib/i18n/messages.{en,sk,cs,pl}.ts` — one new key, verbatim
   - `frontend/src/lib/i18n/GLOSSARY.md` — key plus one-line empty-vs-unreachable distinction
   - `frontend/src/lib/i18n/i18n.test.ts` — AC-CATALOG-COPY-4; AC-EXHAUST combined count 300
7. Exact responses, **both** routes:
   - **success:** HTTP 200, body `JSON.stringify([{ provider: "openrouter", model_id: "google/gemma-4-31b-it:free" }])` byte-for-byte
   - **upstream failure:** HTTP 500, `{ error: "catalog_unavailable", upstream_status: 500 }`
   - **unreachable:** HTTP 502, `{ error: "catalog_unreachable" }`
8. Leak proof. Stubbed upstream body `DJANGO_SECRET_LEAK_TOKEN_f3c91a`, status text `Internal Server Error FROM_DJANGO_f3c91a`, plus header `X-Django-Debug` with the same token. Neither the 500 nor the 502 response text contains `DJANGO_SECRET_LEAK_TOKEN_f3c91a`, `FROM_DJANGO`, or the status text. Thrown `Error(\`ECONNREFUSED …\`)` is also absent from the 502 body.
9. `reconcileRival` signature and call sites:

```100:135:frontend/src/app/play/page.tsx
  const reconcileRival = useCallback(async (): Promise<{
    modelId: string | null;
    catalogReachable: boolean;
  }> => {
    if (!token) return { modelId: null, catalogReachable: true };
    // ...
    if (!resolved) return { modelId: null, catalogReachable: catalogResult.ok };
    // ...
    return { modelId: resolved, catalogReachable: catalogResult.ok };
  }, [token, setSelectedModelId]);
```

Mount: `const { modelId, catalogReachable } = await reconcileRival();` then `play.error.catalogEmpty` vs `play.error.catalogUnavailable`. Start-AI: same destructure; `ai_model_model_id: modelId`. `resolveEligibleModelId` / store / preference path unchanged.
10. Settings notice at the previous `:474-479` now keys `catalogResult.ok ? "play.error.catalogEmpty" : "play.error.catalogUnavailable"`. `catalogResult.ok` already existed at the loader `:425-427` (`{ ok: true, catalog }` / `{ ok: false, catalog: [] }`). No new state, no new fetch.
11. Neither proxy was deleted (`models/route.ts` and `prompts/route.ts` still exist). `api.getPrompts` still at `api.ts:412`. Build lists **eleven** `ƒ` routes, **zero** `○`:

```
ƒ / · ƒ /_not-found · ƒ /api/ai/judge · ƒ /api/ai/move · ƒ /api/models · ƒ /api/prompts
ƒ /draw/[id] · ƒ /game/[id] · ƒ /play · ƒ /settings · ƒ /waiting/[id]
ƒ Proxy (Middleware)
```

12. Pre-fix / post-fix:

| AC | before | first failure | after |
|---|---|---|---|
| AC-PROXY-UPSTREAM-FAIL (both) | FAIL | `expected 200 to be 500` | PASS |
| AC-PROXY-UNREACHABLE (both) | FAIL | `expected 200 to be 502` | PASS |
| AC-PROXY-SUCCESS (both) | PASS before | success path already returned the parsed array | PASS |
| AC-PROXY-NO-LEAK (both) | PASS before | swallowed `[]` contains no Django text | PASS (new error bodies also leak-free) |
| AC-PROXY-NO-STORE models | FAIL | `expected undefined to be 'no-store'` | PASS |
| AC-PROXY-NO-STORE prompts | PASS before | already `cache: "no-store"` | PASS |
| AC-CATALOG-COPY-4 | FAIL | `expected undefined to be 'The rival catalog is temporarily unavailable. Try again in a moment.'` | PASS |
| AC-EXHAUST key-set equality | PASS before | catalogs already shared one key set | PASS |
| AC-EXHAUST combined count | 299 (279 text + 20 fn) | first text-only `toHaveLength(300)` received **279**; combined target is 300 | PASS at 280+20=300 |

13. `play.error.catalogEmpty` unchanged:
    - en: `The rival catalog is empty. Seed the free catalog to play AI matches.`
    - sk: `Katalóg súperov je prázdny. Naplň katalóg, aby sa dali hrať partie proti AI.`
    - cs: `Katalog soupeřů je prázdný. Naplň katalog, aby se daly hrát partie proti AI.`
    - pl: `Katalog rywali jest pusty. Wypełnij katalog, aby grać partie z AI.`
14. Gates:
    - mypy: `Success: no issues found in 83 source files`
    - ruff: `All checks passed!`
    - check: `System check identified no issues (0 silenced).`
    - pytest: `390 passed, 4 skipped in 217.48s (0:03:37)`
    - typecheck: exit 0
    - vitest: `450 passed | 3 skipped (453)` — floor was 439 passed; +10 proxy tests + 1 AC-CATALOG-COPY-4
    - lint: exit 0
    - build: exit 0; eleven `ƒ`; zero `○`
15. R10 re-check (product source excluding tests): `aria-live` 1 (`LiveAnnouncer.tsx`), `role="status"` 1 (same), `role="dialog"` 4 (ProfileModal, GameHistoryModal, BlankPicker, game page blocker), `aria-modal` 4 (same four). `script-src` still `'self' 'nonce-…' 'strict-dynamic'` (+ `'unsafe-eval'` in dev) and no `'unsafe-inline'` on `script-src` (`style-src` still `'self' 'unsafe-inline'`). AC-ONE-LIVE-REGION passed in the full vitest run.
16. Commit and push: fast-forward `cb4efed..47ed8bf` to `origin/main`. Public `git ls-remote origin refs/heads/main` = `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a`. Local `git rev-parse HEAD` = `47ed8bff5a6548d2d954c68d9ea13f05a2222e4a`.
17. Honest evidence ceiling: a node suite proves route status/body/fetch arguments and that the four-locale strings exist. It cannot prove a player sees the right sentence in a real Django outage. Unexercised page branches: Play mount `useEffect`, Play `handleStartAI`, Settings notice, Settings rival-panel empty state, login `app/page.tsx` (left by instruction).
18. Inventory:
    - **`app/page.tsx:47` left unchanged**, as required: it only feeds `resolveEligibleModelId` during login and shows no catalog sentence.
    - **Third `catalogEmpty` site section 4.2 missed:** `settings/page.tsx` rival panel still renders `t("play.error.catalogEmpty")` when `selectedModel` is missing. After this slice the warning notice is correct on outage, but that panel still accuses the player of an unseeded catalog. Fixing it needs persisted reachability state, which this grant forbade (`No new state`). Reported, not patched.
    - `draw/[id]/page.tsx` swallows `getModels` failure into `[]` with no catalog sentence (label falls back to `humanizeModelId`).
    - `game/[id]/page.tsx` already uses `fallbackQueueForCatalogFailure` — not the empty-catalog message.
    - Prompt “299 keys becomes 300” is **text+fn** (279+20), not 299 text keys.
    - Section 4.1 is accurate: both proxies had zero app callers; `getPrompts` has zero callers outside `api.ts`.
19. Deviations: none from the approved design. Residual: Settings rival-panel copy (item 18). Missing evidence: Cooperator four-locale eye, required-after-landing.
20. **Resolved Execution Issues / Near-Misses:** asserted `textKeys.length === 300` first; runtime was 279. Cause: the prompt’s 299 is text+fn. Resolution: `textKeys.length + fnKeys.length === 300`. Residual: none.
21. **Pre-Existing Failure Classification:** none
22. Smallest next step: Cooperator four-locale acceptance of `play.error.catalogUnavailable`. Optionally a follow-up to key the Settings rival-panel empty state off catalog reachability (needs one piece of state).
23. report justification: **new-mutation**
24. Authority for Worker session 17 exchange 01 expires with this terminal report. Logical-whole closure: not-closed. Only the ORCHESTRATOR may close a logical whole.
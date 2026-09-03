You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 17
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: R11 — a backend outage stops presenting itself as an unseeded catalog
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — the finding as FILED is in two dead proxy routes; the finding as it
  actually reaches a player is in three page call sites. Fixing only the filed half would close the defect on
  paper and leave the symptom fully intact.
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

  git rev-parse HEAD                     -> cb4efed9e1c3859e7839b5adb18a605a6c3ef102
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> cb4efed9e1c3859e7839b5adb18a605a6c3ef102

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19 · .ap/AP_WORKER.md · .ap/INFOSEC.md sections 3, 6, 7, 14
4. frontend/src/app/api/models/route.ts — all 28 lines
5. frontend/src/app/api/prompts/route.ts — all 20 lines
6. frontend/src/app/play/page.tsx — `reconcileRival` at :100-137 and its two call sites at :143 and :161
7. frontend/src/app/settings/page.tsx — the loader at :418-441 and the notice at :470-481
8. frontend/src/app/page.tsx :45-48
9. frontend/src/lib/api.ts — `humanMessageForStatus` at :148-175 and `request()` at :224+
10. frontend/src/lib/i18n/GLOSSARY.md

=====================================================================
3. GOAL
=====================================================================
`audit-01-F06` and `uii-01-F13`. A player must be able to tell "the catalog is genuinely empty, seed it" from
"the catalog is temporarily unreachable, try again". Today both render the same sentence, and a Django outage
therefore accuses the player of not having seeded anything.

=====================================================================
4. MEASURED SCOPE — the Orchestrator ran all of this
=====================================================================

--- 4.1 The filed half: two proxy routes that swallow ---

```text
api/models/route.ts:19-21   if (!res.ok) return NextResponse.json([], { status: 200 })
api/models/route.ts:25-27   catch { return NextResponse.json([], { status: 200 }) }
api/prompts/route.ts:11-13  same
api/prompts/route.ts:17-19  same
asymmetry, also filed       models uses `next: { revalidate: 60 }` (:16), prompts uses
                            `cache: "no-store"` (:8). So a 60-second stale EMPTY catalog can outlive a
                            recovered backend.
```

⚠ **BOTH ROUTES HAVE ZERO CALLERS.** Measured: nothing in `frontend/src` fetches `/api/models` or
`/api/prompts` except `proxy.test.ts:44` and `:91`, which use the paths only as matcher fixtures. The app
reaches Django DIRECTLY — `api.ts:356` `getModels: () => request<AIModel[]>("/api/catalog/models/")` and
`:412` `getPrompts: () => request<AIPrompt[]>("/api/catalog/prompts/")`.

`api.getPrompts` itself has **zero callers** outside `api.ts`, because slice S4 removed the prompt-preset
surface.

⛔ **DO NOT DELETE THE PROXIES, AND DO NOT DELETE `api.getPrompts`.** `uii-01-F13` is hereby DECIDED as
**keep-and-record**, for two evidenced reasons:

```text
1  README.md:204 and :291, frontend/README.md:45, docs/architecture.md:38 and CONTRIBUTING.md:91 all
   document `/api/models` as the architecture. README.md and AGENTS.md are under the STANDING COOPERATOR
   FREEZE (locked fork 11). Deleting the route would require editing a frozen file.
2  Whole `11/00 admin-provider-model-console` will need a server-side catalog proxy, and the ledger already
   records "Do NOT delete the Django catalog/prompts/ endpoint — the admin console needs it."
```

So the routes stay, and they stop lying. Their honesty is what this slice buys.

--- 4.2 ⛔ THE HALF THAT ACTUALLY REACHES A PLAYER, and it is NOT in the routes ---

Because nothing calls the proxies, their swallow currently harms nobody. The user-visible swallow is in the
pages, against the DIRECT Django path:

```text
play/page.tsx:104     api.getModels().catch((): AIModel[] => [])      <- outage becomes an empty catalog
play/page.tsx:100-137 reconcileRival() then returns null when resolveEligibleModelId finds nothing
play/page.tsx:147     setError(translate(locale, "play.error.catalogEmpty"))
play/page.tsx:164     setError(t("play.error.catalogEmpty"))
                      en: "The rival catalog is empty. Seed the free catalog to play AI matches."
app/page.tsx:47       api.getModels().catch((): AIModel[] => [])      <- same collapse, no message
settings/page.tsx:425-427  ALREADY tracks the distinction: it resolves to
                      `{ ok: false, catalog: [] }` on failure...
settings/page.tsx:474-479  ...and then IGNORES `catalogResult.ok`, showing `play.error.catalogEmpty` either
                      way. The information is already in scope; only the choice of message is missing.
```

**That is the finding as a player experiences it.** A prompt that fixed only 4.1 would have closed
`audit-01-F06` while leaving every symptom the ledger described.

--- 4.3 What the frontend does with an error status, so you do not duplicate it ---

`humanMessageForStatus` (`api.ts:148-175`) already maps failures to localized copy: 503 ->
`error.unavailable`, 401/403/404/429 -> their own keys, everything else -> `error.generic`. A machine code in
an `error` field is only surfaced for HTTP 400 and 409, so a code such as `catalog_unavailable` can never be
rendered raw to a player.

=====================================================================
5. EXACT STRING CONTENT — authored by the ORCHESTRATOR, use VERBATIM
=====================================================================
ONE new key. Counted from the table.

```text
key                            en
play.error.catalogUnavailable  The rival catalog is temporarily unavailable. Try again in a moment.

key                            sk
play.error.catalogUnavailable  Katalóg súperov je práve nedostupný. Skús to za chvíľu.

key                            cs
play.error.catalogUnavailable  Katalog soupeřů je právě nedostupný. Zkus to za chvíli.

key                            pl
play.error.catalogUnavailable  Katalog rywali jest chwilowo niedostępny. Spróbuj za chwilę.
```

⚠ THREE THINGS. `rival` is `súper` / `soupeř` / `rywal`, matching the existing `play.humanQueue` and
`game.opponentFallback` copy — do NOT introduce a synonym. The Slovak and Czech register is informal `ty`
(`Skús` / `Zkus`), per decision 3, because this sentence DOES address the player, unlike the impersonal
`history.endReason.*` strings. And the existing `play.error.catalogEmpty` is NOT changed: it stays the
message for a genuinely empty catalog.

`GLOSSARY.md`: add the key, and record in one line that a reachable-but-empty catalog and an unreachable one
are two different messages.

=====================================================================
6. WHAT TO BUILD
=====================================================================

--- 6.1 The two proxy routes stop swallowing ---

```text
on !res.ok      return the UPSTREAM status with a JSON body { error: "catalog_unavailable",
                upstream_status: res.status }
on a thrown fetch error   return 502 with { error: "catalog_unreachable" }
on success      unchanged — return the parsed JSON exactly as today
⛔ Do NOT echo Django's body, status text, or any header into the response. INFOSEC: no upstream detail
   crosses to the browser beyond the numeric status.
cache           make BOTH routes use `cache: "no-store"`. Remove `next: { revalidate: 60 }` from
                models/route.ts. A cached empty catalog outliving a recovered backend is half the filed
                defect, and caching an error response would be worse than caching an empty one.
```

--- 6.2 `play/page.tsx` distinguishes the two cases ---

`reconcileRival` currently returns `Promise<string | null>` and loses the reason. Change it to report both:

```ts
Promise<{ modelId: string | null; catalogReachable: boolean }>
```

`catalogReachable` is `false` only when the `api.getModels()` promise rejected. Both call sites — `:143` and
`:161` — then choose `play.error.catalogUnavailable` when it is `false` and keep
`play.error.catalogEmpty` when it is `true`.

⛔ Do NOT change `resolveEligibleModelId`, the store, `selectedModelId`, or the AI-fallback preference path.
`selectedModelId` is attempt 1 of the provider fallback queue and slice S4 spent a whole section on not
breaking it.

--- 6.3 `settings/page.tsx` uses the flag it already has ---

At `:474-479`, pick `play.error.catalogUnavailable` when `catalogResult.ok` is `false`, and keep
`play.error.catalogEmpty` when it is `true`. No new state, no new fetch — `catalogResult.ok` already exists at
`:425-427`.

--- 6.4 `app/page.tsx:47` ---

Leave it. That call site shows no catalog message at all; it only feeds `resolveEligibleModelId` during
login. Changing it would add a failure path to the login flow for no user-visible gain. Say in your report
that you left it and why.

=====================================================================
7. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/app/api/models/route.ts                 (6.1)
  frontend/src/app/api/prompts/route.ts                (6.1)
  frontend/src/app/play/page.tsx                       (6.2 — reconcileRival and its two call sites ONLY)
  frontend/src/app/settings/page.tsx                   (6.3 — the notice at :474-479 ONLY)
  frontend/src/lib/i18n/messages.en.ts
  frontend/src/lib/i18n/messages.sk.ts
  frontend/src/lib/i18n/messages.cs.ts
  frontend/src/lib/i18n/messages.pl.ts
  frontend/src/lib/i18n/GLOSSARY.md
  frontend/src/lib/i18n/i18n.test.ts                   (section 9)
CREATE:
  frontend/src/app/api/catalog-proxy.test.ts           (section 9 — first test for either route)

Nothing else. No migration. Nothing under `backend/`.

=====================================================================
8. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- ⛔ Do NOT delete either proxy route or `api.getPrompts`. Section 4.1. `uii-01-F13` is decided as
  keep-and-record.
- ⛔ Do NOT touch `README.md`, `frontend/README.md`, `docs/architecture.md`, `CONTRIBUTING.md`, or
  `AGENTS.md`. The first and last are under the standing Cooperator freeze; the architecture they document
  stays true because you are keeping the routes.
- ⛔ Do NOT change `play.error.catalogEmpty` in any locale. It keeps its current meaning.
- ⛔ Do NOT change `resolveEligibleModelId`, `frontend/src/lib/model-catalog.ts`, `selectedModelId`, the
  Zustand store, or the persist version.
- ⛔ Do NOT change `frontend/src/lib/api.ts`. `humanMessageForStatus` and `parseRetryAfterSeconds` already do
  their jobs; its 401 branch is a security property.
- ⛔ Do NOT change `frontend/src/proxy.ts`, `security-headers.ts`, or `proxy.test.ts`. R10 settled the CSP
  three commits ago; `aria-live` and `role="status"` must each still count 1, `role="dialog"` and
  `aria-modal` each 4, and `script-src` must still carry a nonce and no `'unsafe-inline'`.
- ⛔ Do NOT echo Django's response body or status text to the browser.
- `frontend/src/lib/prompts.ts` and its pinned SHA-256, `ai-move-stream.ts`, `api/ai/move/route.ts`,
  `api/ai/judge/route.ts`, `types.ts`. Locked fork 2.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts, ibm-watsonx.ts,
  ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- Anything under `backend/`. `git diff --name-only backend/` must be EMPTY and you must quote it.
- No new dependency. `package.json` and `package-lock.json` unchanged.
- Do not reformat or "tidy" anything beyond the named edits.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files.

=====================================================================
9. TESTS — each must fail before and pass after
=====================================================================
```text
AC-PROXY-UPSTREAM-FAIL  models and prompts: a stubbed fetch returning 500 makes the route answer 500 with
                        { error: "catalog_unavailable", upstream_status: 500 } — NOT [] with 200
AC-PROXY-UNREACHABLE    a stubbed fetch that REJECTS makes the route answer 502 with
                        { error: "catalog_unreachable" } — NOT [] with 200
AC-PROXY-SUCCESS        a stubbed 200 with a JSON array is returned unchanged, byte for byte
AC-PROXY-NO-LEAK        neither error body contains Django's status text or body. Stub the upstream with a
                        recognizable secret-looking string and assert it is ABSENT from the response.
AC-PROXY-NO-STORE       both routes pass `cache: "no-store"` and NEITHER passes `revalidate`. Assert from
                        the fetch call arguments, not from source text.
AC-CATALOG-COPY-4       `play.error.catalogUnavailable` renders the exact authored string in all four
                        locales, and is NOT equal to `play.error.catalogEmpty` in any locale.
AC-EXHAUST              ALREADY EXISTS and must keep passing. 299 keys becomes 300.
```

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted, except by naming the
assertion and showing the property is still covered.

⚠ HONEST CEILING to state in your report: a node-environment suite can prove the route's status, body and
fetch arguments, and that the copy exists in four locales. It CANNOT prove that a player sees the right
sentence during a real outage. Name that, and name which page branches you could not exercise.

=====================================================================
10. COMMANDS, EXECUTION ROUTE, GIT
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
  Evidence class: reproduced-dynamic. Bounded authority: these four commands only.
  Stopping condition: if the alternate route also fails to resolve the in-project virtualenv, STOP and
    report; do not substitute ambient python, python3, or poetry run.

TRAP: `addopts = "-q"` is set. Do NOT pass another `-q`. pytest takes about 220 seconds; that is normal.
  Never quote a summary you did not see. This slice changes no Python, so any backend gate change is a
  signal about your environment.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. Immediately before `npm run build`, run
`ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, complete all eight gates, commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`. Run the
    other SEVEN gates, leave the candidate UNCOMMITTED, report `status: PARTIAL`, quote the exact `ss`
    output with the PID.
⛔ NEVER use a broad pattern kill such as `pkill -f next-server`; it matches the Cooperator's own server.
⚠ The build must still list ELEVEN dynamic routes including `/api/models` and `/api/prompts`, and ZERO `○`
static routes. A route count of nine would mean you deleted something section 8 forbids.

Forbidden commands: any git write beyond the block below, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote` reads,
  any process kill.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

GIT — primary route only, after all eight gates are green: exactly one commit and one push.
  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       fix(catalog): an unreachable catalog stops reporting itself as an empty one
     Body: that both proxy routes swallowed every failure into an empty HTTP 200 and now report the upstream
     status or 502 without leaking Django's body; that the cache asymmetry is gone because a stale empty
     catalog could outlive a recovered backend; that the user-visible half of the finding was in the page
     call sites rather than in the callerless proxies; that uii-01-F13 is decided as keep-and-record because
     four documents including a frozen README describe the route and whole 11/00 will need it; and that no
     dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     cb4efed9e1c3859e7839b5adb18a605a6c3ef102. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.
FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
11. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E2
Evidence tier basis: two callerless server routes gain honest failure statuses, two page call sites choose
  between two localized messages, and one key is added in four locales. No trust boundary moves, no
  credential, no durable data, no migration. Rollback is `git revert` of one commit.
Combined implementation envelope: allowed
Independent acceptance: the four-locale copy needs the Cooperator's eye and will be in the closing
  acceptance batch.

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `390 passed, 4 skipped`
  typecheck exit 0 · vitest at least `439 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0, ELEVEN dynamic routes, ZERO `○` static routes

=====================================================================
12. STOPPING CONDITIONS
=====================================================================
Stop and report if: a section 1 gate value disagrees; you conclude a proxy route must be deleted to fix the
finding; you find a THIRD place where a catalog failure collapses into the empty-catalog message that
section 4.2 missed; changing `reconcileRival`'s return type ripples beyond `play/page.tsx`; the build reports
other than eleven dynamic routes; a backend gate value changes; `git ls-remote` shows main advanced; any
instruction here conflicts with AGENTS.md, .ap/AP.md, .ap/INFOSEC.md, or observed repository truth.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker, the
smallest authority expansion that would resolve it, and the exact first error text.

=====================================================================
13. TERMINAL REPORT
=====================================================================
Begin with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 17, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output
 6. changed files with the purpose of each, plus `git diff --name-only backend/` quoted as empty
 7. the exact response for each of the three cases, for BOTH routes: success, upstream failure, unreachable
 8. proof that no Django body or status text reaches the browser, with the recognizable string you used
 9. `reconcileRival`'s new signature and both updated call sites, quoted
10. the `settings/page.tsx` change, and confirmation that `catalogResult.ok` already existed
11. confirmation that neither proxy route was deleted, that `api.getPrompts` survives, and that the build
    still lists ELEVEN dynamic routes — quote the route list
12. the pre-fix / post-fix table for every test in section 9, with exact pre-fix failure text
13. confirmation that `play.error.catalogEmpty` is unchanged in all four locales, quoted
14. gate results with the pytest summary quoted verbatim and the vitest counts, every change accounted for
15. the R10 invariants re-checked: `aria-live` 1, `role="status"` 1, `role="dialog"` 4, `aria-modal` 4, and
    `script-src` still carrying a nonce with no `'unsafe-inline'`
16. commit and push result with both refs quoted, or an explicit statement that the candidate is uncommitted
17. the honest evidence ceiling, and which page branches you could not exercise
18. ANY third collapse site, any remaining place where a failure reads as a configuration mistake, or
    anything in section 4 you found inaccurate. Seven previous slices in this whole found something an
    Orchestrator inventory had missed.
19. deviations, risks, or missing evidence
20. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
21. Pre-Existing Failure Classification: none | <complete classification>
22. one smallest next step
23. report justification: new-mutation
24. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may close
a logical whole. Your terminal report is your completion signal.

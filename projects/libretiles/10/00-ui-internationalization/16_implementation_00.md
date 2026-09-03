You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 16
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: R10 — implement the approved nonce Content-Security-Policy
Implementation authority: explicit
Independence required: no
Reasoning recommendation: high. Basis — this replaces a security header on every response. The plan you are
  executing is approved and decision-complete, so your judgement is needed for correctness of execution and
  for the loopback proof, not for re-deciding the design.
Report justification: new-mutation
Context-pressure rule: report visible context usage if it exceeds 70%.

=====================================================================
0. PLAN PROVENANCE AND WHAT IT MEANS FOR YOU
=====================================================================
An Implementation-Planning Worker (session 15, exchange 04) produced a decision-complete plan for this
change. The ORCHESTRATOR **APPROVED** it and independently verified its three load-bearing claims against
the installed runtime. That plan is the design authority for this slice.

```text
Plan disposition: approval-gated
Plan verdict: APPROVED by ORCHESTRATOR
Post-plan implementation session: fresh-worker-session
Planning authority: expired with session 15 exchange 04. You inherit NO authority from it.
```

You are that fresh session. The three field values above are quoted from the approved planning contract
verbatim; `Plan verdict` is the Orchestrator's decision on it.

⛔ YOU ARE NOT THE PLANNER AND YOU DID NOT WRITE THE PLAN. INFOSEC 4.10 — the corrector never
self-certifies — is why this is a different session. Execute the approved design. If you believe a decision
is WRONG, say so in report item 17 and implement it anyway unless it is unsafe; if it is unsafe, STOP.

=====================================================================
1. REPOSITORY GATE
=====================================================================
Repository checkout topology: standalone checkout
Repository identity: https://github.com/cisarik/libretiles
Working directory: /home/agile/Projects/libretiles
Expected branch: main
Working-copy topology: canonical checkout.

  git rev-parse HEAD                     -> f983c3dcce19534466a86b06605e1a02f8bd2bf3
  git rev-parse HEAD:.ap                 -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                         -> ## main...origin/main
  git status --porcelain=v1              -> EMPTY
  git ls-remote origin refs/heads/main   -> f983c3dcce19534466a86b06605e1a02f8bd2bf3

STOP if any value disagrees.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — "This is NOT the Next.js you know"
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19 · .ap/AP_WORKER.md
4. .ap/INFOSEC.md sections 3, 6, 7, 8, 14, 16, 17
5. frontend/src/proxy.ts — all 29 lines
6. frontend/src/lib/security-headers.ts — all 114 lines
7. frontend/src/lib/security-headers.test.ts — all 168 lines and all nine `it` blocks
8. node_modules/next/dist/docs/01-app/02-guides/content-security-policy.md :34-90 and :179-193
9. node_modules/next/dist/docs/01-app/03-api-reference/03-file-conventions/proxy.md :253-258 and :414-468
10. node_modules/next/dist/experimental/testing/server/middleware-testing-utils.d.ts and utils.d.ts

=====================================================================
3. GOAL
=====================================================================
`orch-01-F18`: replace `script-src 'unsafe-inline'` with a per-request nonce, so no inline script executes
unless the server minted its nonce for that exact response.

=====================================================================
4. FACTS THE ORCHESTRATOR VERIFIED — do not re-derive, but you may re-check
=====================================================================

```text
proxy runtime        Proxy DEFAULTS TO THE NODE.JS RUNTIME in Next 16 — proxy.md:255 and the v16.0.0 row at
                     :806. So `Buffer` and `crypto.randomUUID()` are available.
                     ⛔ proxy.md:255 also says the `runtime` config option is NOT AVAILABLE in Proxy files
                     and SETTING IT THROWS. Do not add one.
nonce read path      app-render.js:209-210 reads the nonce from the REQUEST headers
                     (`content-security-policy`, then `-report-only`).
                     get-script-nonce-from-header.js:11 regex /^'nonce-([A-Za-z0-9+/_-]+={0,2})'$/ · :17
                     prefers `script-src`, falls back to `default-src` · :22-23 A MALFORMED NONCE IS
                     SILENTLY IGNORED. That is the dangerous failure mode: a correct-looking header and no
                     nonce anywhere.
                     ⚠ `x-nonce` is NOT read by Next.js. It appears in exactly one file under
                     node_modules/next/dist/ — the documentation. Do not add it.
current blocker      proxy.ts:12 calls NextResponse.next() with NO argument, so nothing it sets reaches the
                     renderer.
test helper EXISTS   next/experimental/testing/server re-exports
                     `unstable_doesMiddlewareMatch({config, url, headers, cookies, nextConfig})` and
                     `constructRequest({url, headers, cookies})`. Verified present in this install. This is
                     what makes the FIRST EVER proxy.ts test possible.
call sites           `buildSecurityHeaders` has exactly ONE production caller — proxy.ts:6 — plus 12 call
                     sites in security-headers.test.ts. Adding a required parameter has a fully known blast
                     radius.
app inline scripts   ZERO. Seven patterns (`<script`, dangerouslySetInnerHTML, eval(, new Function,
                     `<style`, next/script, next/font) all return zero matches in frontend/src.
_global-error        PRERENDERED, and its artifact contains 5 inline scripts, 0 nonce attributes, exactly
                     one `<form style="margin:0">` and one `<button type="submit">`. Verified by parsing
                     .next/server/app/_global-error.html. The native reload therefore does NOT depend on
                     JavaScript, which is what makes the accepted residual low severity.
doc nonce form       content-security-policy.md:48 uses exactly
                     `Buffer.from(crypto.randomUUID()).toString('base64')`. The plan conforms to the pinned
                     doc; keep that form.
```

=====================================================================
5. THE APPROVED DESIGN — implement exactly this
=====================================================================

--- 5.1 Nonce ownership ---

```text
proxy.ts             owns entropy. ONE nonce per proxy() invocation:
                       const nonce = Buffer.from(crypto.randomUUID()).toString("base64")
security-headers.ts  stays DETERMINISTIC and receives the nonce explicitly.
FORBIDDEN            timestamps, Math.random(), a module-scoped nonce, any dependency, any env var, and any
                     caller-controlled or request-derived value.
```

New signatures:

```ts
buildContentSecurityPolicy(context: SecurityHeaderContext, nonce: string): string
buildSecurityHeaders(context: SecurityHeaderContext, nonce: string): Record<string, string>
```

Add a NON-EXPORTED validation helper matching `/^[A-Za-z0-9+/_-]+={0,2}$/` — the same grammar Next's parser
accepts. **THROW before emitting a policy** if it fails. Turning Next's silent ignore into a loud failure is
the point.

The builder must stay pure: same context plus same nonce gives byte-identical headers, with no time, no
randomness, no mutation, no global state.

--- 5.2 The policy: change `script-src` ONLY ---

```text
production   script-src 'self' 'nonce-<fresh>' 'strict-dynamic'
development  script-src 'self' 'nonce-<fresh>' 'strict-dynamic' 'unsafe-eval'
```

`'self'` is retained deliberately as the CSP2 fallback: CSP3 browsers ignore it when `'strict-dynamic'` is
present, CSP2 browsers ignore `'strict-dynamic'` and honour `'self'`. The nonce applies in BOTH modes, so
development exercises the same propagation path production does — a production-only nonce would hide an
integration failure until deploy.

⛔ `style-src 'self' 'unsafe-inline'` at `security-headers.ts:87` STAYS BYTE-FOR-BYTE. 33 `style=` props
across 16 files plus imperative `style.setProperty` writes produce style ATTRIBUTES, which a nonce cannot
cover. It is a separate accepted residual and it is OUT OF SCOPE. The Next doc nonces `style-src`; we do not,
and that divergence is deliberate.

Every other directive and the directive ORDER stay unchanged.

--- 5.3 Matcher and conditional request propagation ---

⛔ The matcher at `proxy.ts:19-29` stays BYTE-FOR-BYTE, including its coverage of `/api`.

```text
for /api and /api/*        NextResponse.next()  with NO request-header override
                           + the complete security-header set on the RESPONSE
for every other match      clone request.headers · set ONLY Content-Security-Policy on the clone
                           NextResponse.next({ request: { headers: requestHeaders } })
                           + the SAME CSP and the same other security headers on the RESPONSE
```

Why, so you do not simplify it: excluding `/api` the way every Next doc example does would REMOVE response
security headers that `audit-03` verified are present on `/api/models`, `/api/prompts` and `/api/ai/move`.
Forwarding a randomized request CSP into API route handlers that render no framework scripts creates
needless internal variability. The conditional keeps both properties.

--- 5.4 The accepted residual: `_global-error` does not hydrate ---

Its prerendered scripts have no nonce and cannot get one. Accept it. Do NOT weaken the ordinary-page policy
to accommodate it, do NOT add an `'unsafe-inline'` fallback, and do NOT attempt to force that document
dynamic — the plan established that no supported request-time path exists inside the authorized files.

After the build, inspect the generated artifact and RECORD that it is still static, still has no nonce
attributes, and still contains the visible error markup plus the native reload form. That is residual
evidence, not proof of browser usability.

=====================================================================
6. POSITIVE AUTHORITY — exact paths
=====================================================================
MODIFY:
  frontend/src/proxy.ts                              (5.1 nonce, 5.3 conditional propagation, response headers)
  frontend/src/lib/security-headers.ts               (5.1 signatures + validation, 5.2 script-src only)
  frontend/src/lib/security-headers.test.ts          (section 7)
CREATE:
  frontend/src/proxy.test.ts                         (section 7 — the FIRST test this file has ever had)

No other tracked file. No migration. Nothing under `backend/`.

=====================================================================
7. TESTS — each must fail before and pass after, EXCEPT where noted
=====================================================================
Update the existing suite first: introduce `const TEST_NONCE = "test-nonce"` and pass it to all 12 existing
builder call sites. **Preserve all nine existing `it` blocks and every assertion inside them.**

```text
AC-CSP-PROD        production script-src sources are EXACTLY 'self', 'nonce-test-nonce', 'strict-dynamic';
                   script-src does NOT contain 'unsafe-inline'; style-src is EXACTLY "'self' 'unsafe-inline'"
AC-CSP-DEV         development additionally contains 'unsafe-eval', and still no script 'unsafe-inline'
AC-NONCE-REJECT    a nonce containing whitespace or directive punctuation makes the builder THROW
AC-PROXY-MATCH     via unstable_doesMiddlewareMatch: `/` and `/api/models` match; `/_next/static/x.js`,
                   `/_next/image`, `/favicon.ico` and a `purpose: prefetch` request do NOT.
                   ⚠ THIS ONE IS EXPECTED TO PASS BEFORE YOUR CHANGE. It is a DECISION-LOCK test, not a
                   regression test, and you must label it as such in your report. Do not dress it up.
AC-PROXY-PROPAGATE for a rendered page: NextResponse.next receives request headers containing CSP; the
                   forwarded CSP EQUALS the response CSP; it contains a nonce; script-src has no
                   'unsafe-inline'; NO `x-nonce` header is introduced anywhere
AC-PROXY-API       `/api/models` still gets the response CSP, and NextResponse.next receives NO request
                   override
AC-NONCE-FRESH     two invocations for the same rendered URL yield two DIFFERENT nonces; each response's
                   nonce equals its own forwarded nonce; both match the Next grammar
```

Record the causal red phase before touching production code, and quote the exact first failure of each.

⛔ No test in this project has ever been weakened, xfailed, skipped, or deleted, except by naming the
assertion and showing the property is still covered.

HONEST CEILING, state it: node tests can prove policy construction, validation, matcher semantics, the
NextResponse.next wiring, request/response CSP equality and sampled nonce uniqueness. They CANNOT prove that
Next's renderer consumes the nonce, that the served HTML is annotated, that a browser enforces the policy, or
that hydration and Fast Refresh still work.

=====================================================================
8. THE LOOPBACK PROOF — this is the decisive evidence, not the tests
=====================================================================
Production build, then `next start` bound to loopback on port **3107**.

```text
⛔ PORT 3000 IS THE COOPERATOR'S OWN DEV SERVER. Before building, run `ss -tlnp | grep :3000`; also confirm
   3107 is free. NEVER use pkill or any broad process pattern — start the process directly, capture its PID
   with $!, and in cleanup kill and wait for THAT PID ONLY.
```

Issue TWO independent `GET http://127.0.0.1:3107/` requests, capturing headers and body separately, and
require HTTP 200 before parsing anything. Then assert:

```text
1  exactly ONE nonce in script-src, matching /^[A-Za-z0-9+/_-]+={0,2}$/
2  'strict-dynamic' present
3  script-src has NO 'unsafe-inline'
4  style-src is unchanged: 'self' 'unsafe-inline'
5  the body contains at least one INLINE and one EXTERNAL <script>
6  ⛔ EVERY raw <script> element in the body carries nonce="<the nonce from THIS response's CSP header>"
7  the two responses use DIFFERENT nonces
8  NEITHER body contains the OTHER response's nonce
```

Assertion 6 is the whole point. It is the only thing that proves Next discovered the Proxy, received the
request CSP, extracted the nonce and annotated its generated HTML. Header-contains-a-nonce proves nothing.

Then probe, recording status BEFORE inspecting headers, and confirming each still carries the full security
header set: `/api/models`, `/api/prompts`, `GET /api/ai/move`, `GET /api/ai/judge`. The AI routes are
expected to answer `405` to GET; they must still have the headers. No provider call must occur.

Preserve the FIRST causal failure and stop rather than iterating.

--- 8.1 THE audit-03 BASELINE, inlined because it lives OUTSIDE this repository ---

The planner correctly reported that the documents naming this baseline are not in the checkout. That was an
Orchestrator error. Here it is verbatim — the Next.js production build, loopback readback, `GET /`:

```text
content-security-policy: default-src 'self'; script-src 'self' 'unsafe-inline';
  style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self';
  connect-src 'self' http://localhost:8000 ws://localhost:8000; frame-ancestors 'none';
  base-uri 'self'; form-action 'self'; object-src 'none'; upgrade-insecure-requests
x-content-type-options: nosniff
referrer-policy: strict-origin-when-cross-origin
x-frame-options: DENY
permissions-policy: camera=(), microphone=(), geolocation=()
cross-origin-opener-policy: same-origin
strict-transport-security: max-age=31536000; includeSubDomains
```

Canonicalize your nonce to a placeholder, then byte-compare EVERYTHING else — header names, values,
directives and their order. The ONLY authorized difference is `script-src`. `strict-transport-security` is
absent in development and present in production; that is expected.

⚠ `Vary: Accept-Language` and `Content-Language` must NOT appear. Those are Django response headers added by
slice R7's `LocaleMiddleware`; Django middleware cannot touch a Next.js response. If you see either here,
report it as a finding — it would mean something unexpected is in the path.

=====================================================================
9. NEGATIVE AUTHORITY — forbidden, no exceptions
=====================================================================
- ⛔ Do NOT change `style-src`. Section 5.2.
- ⛔ Do NOT change the matcher, its `source`, or its `missing` entries. Section 5.3.
- ⛔ Do NOT add `x-nonce`. Do NOT add a `runtime` config to the Proxy file — proxy.md:255 says setting it
  throws.
- ⛔ Do NOT add any dependency. No CSP library, no nonce library. `package.json` and `package-lock.json`
  unchanged.
- ⛔ Do NOT touch `next.config.ts`, `layout.tsx`, `globals.css`, any `app/**/page.tsx`, or any API route
  handler.
- ⛔ Do NOT add `experimental.sri` or any other experimental flag.
- ⛔ Do NOT weaken or delete any of the nine existing `security-headers.test.ts` assertions. Adding a nonce
  argument to a call is not weakening; changing what it asserts is.
- ⛔ Do NOT change the a11y invariants settled by S11/R14/R15: `aria-live` and `role="status"` exactly 1 each,
  `role="dialog"` and `aria-modal` exactly 4 each.
- `frontend/src/lib/prompts.ts` and its pinned SHA-256, `ai-move-stream.ts`, `api/ai/move/route.ts`,
  `types.ts`. Locked fork 2.
- STANDING COOPERATOR FREEZE (locked fork 11): provider-registry.ts, openai-compatible.ts, ibm-watsonx.ts,
  ai-runtimes.ts, backend/catalog/selection.py, README.md, AGENTS.md.
- Anything under `backend/`. `git diff --name-only backend/` must be EMPTY and you must quote it.
- Do not reformat or "tidy" anything beyond the named edits.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files.

=====================================================================
10. COMMANDS, EXECUTION ROUTE, GIT
=====================================================================
Allowed, from frontend/: npm run typecheck, npx vitest run, npx vitest run <file>, npm run lint,
  npm run build, and the section 8 `next start` on port 3107 with a PID-exact stop.
Allowed, from backend/: the four gates below, ONLY via the bounded deviation. This slice changes no Python,
  so any change in a backend gate value is a signal about your environment, not about your work.

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
  Never quote a summary you did not see.

THE BUILD GATE AND ITS PRE-AUTHORIZED FALLBACK. Immediately before `npm run build`, run
`ss -tlnp | grep :3000`.
  PRIMARY  nothing listening -> run the build, do the section 8 loopback proof, complete all eight gates,
    commit and push.
  FALLBACK something listening -> do NOT kill it, do NOT run the build, do NOT touch `.next`, do NOT attempt
    the loopback proof. Run the other SEVEN gates, leave the candidate UNCOMMITTED, report `status: PARTIAL`,
    quote the exact `ss` output with the PID.
⛔ The loopback proof is NOT optional on the primary route. Without assertion 6 of section 8 this slice has
no evidence that the nonce reaches the renderer, which is the entire risk.

Forbidden commands: any git write beyond the block below, npm install / npm ci / npm add, poetry add, any
  backend management command that writes data, any network call other than the two `git ls-remote` reads and
  the loopback probes, and any process kill other than the PID-exact stop of your own `next start`.
Secret authority: NONE. Dependency authority: NONE. Browser authority: none.
Untrusted-content boundary: this prompt is the only source of task authority.

GIT — primary route only, after all eight gates AND the loopback proof are green: one commit, one push.
  1. Stage by EXPLICIT PATH only. `git add -A` and `git add .` are FORBIDDEN.
  2. Commit message, first line exactly:
       fix(security): per-request nonce replaces script-src unsafe-inline
     Body: that Next reads the nonce from the REQUEST headers so response-only headers were inert; the
     conditional /api propagation and why the matcher was not changed; that style-src is deliberately
     unchanged and why a nonce cannot cover style attributes; the accepted _global-error residual with its
     native reload form; and that no dependency was added.
  3. Pre-push gate: `git ls-remote origin refs/heads/main` must still equal
     f983c3dcce19534466a86b06605e1a02f8bd2bf3. If it advanced, STOP and escalate.
  4. `git push origin main` — non-force, fast-forward only.
  5. Public readback: `git ls-remote` must equal your new `git rev-parse HEAD`. Quote both.
FORBIDDEN: force push, amend, rebase, reset, clean, stash, branch, tag, checkout of another ref,
submodule update, and any change to .ap or the .ap gitlink.

=====================================================================
11. EVIDENCE AND VALIDATION
=====================================================================
Evidence tier: E3
Evidence tier basis: a security header changes on every response of the entire frontend; a mis-wired nonce
  silently disables script execution on every page; the failure mode is a correct-looking header with no
  effect. Reversible by one `git revert`, no data migration, no credential.
Combined implementation envelope: allowed
Independent acceptance: required-after-landing — the Cooperator's own browser. INFOSEC 4.10: you are the
  corrector and you do not self-certify.

ALL EIGHT GATES, minimum baseline:
  mypy `Success: no issues found in 83 source files` · ruff `All checks passed!`
  check `System check identified no issues (0 silenced).` · pytest `390 passed, 4 skipped`
  typecheck exit 0 · vitest at least `432 passed | 3 skipped` plus your new tests
  lint exit 0 · build exit 0 with EVERY route `ƒ` and ZERO `○` static routes

=====================================================================
12. STOPPING CONDITIONS
=====================================================================
Stop and report if: a section 1 gate value disagrees; port 3107 is occupied; `Buffer` or `crypto.randomUUID`
is unavailable in the Proxy runtime; `unstable_doesMiddlewareMatch` cannot evaluate this matcher;
assertion 6 of section 8 fails, meaning the served HTML is not annotated with the response nonce; you find
you must change `style-src`, the matcher, `next.config.ts`, or add a dependency to make it work; a backend
gate value changes; `git ls-remote` shows main advanced; any instruction here conflicts with AGENTS.md,
.ap/AP.md, .ap/INFOSEC.md, or observed repository truth.

⛔ If assertion 6 fails, do NOT "fix" it by restoring `'unsafe-inline'` or by dropping `'strict-dynamic'`.
Report the exact observed header and the exact observed script tags and stop. A partial rollback that leaves
mixed nonce wiring is worse than either end state.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker, the
smallest authority expansion that would resolve it, and the exact first error text.

=====================================================================
13. TERMINAL REPORT
=====================================================================
Begin with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 16, Worker exchange ordinal 01
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: implementation-PASS | not-applicable
 4. start commit and end commit
 5. WHICH build-gate route you took, with the exact `ss -tlnp | grep :3000` output, and confirmation that
    3107 was free
 6. changed files with the purpose of each, plus `git diff --name-only backend/` quoted as empty
 7. the FINAL CSP string for development and for production, quoted in full
 8. the exact nonce expression you used, and where entropy is created versus where the policy is built
 9. the conditional propagation as implemented: what `/api` gets, what a rendered page gets, and the code
    that distinguishes them
10. ⛔ THE SECTION 8 LOOPBACK PROOF, assertion by assertion, 1 through 8, with the two observed nonces and
    at least one real `<script ... nonce="...">` tag quoted from each body
11. the API probe: four paths, their statuses, and their header sets
12. the audit-03 byte comparison: what matched, and the single authorized difference
13. the `_global-error` artifact inspection: still static, still no nonce, still has the native reload form
14. the pre-fix / post-fix table for every test in section 7, with exact pre-fix failure text — and
    `AC-PROXY-MATCH` explicitly labelled a decision-lock test that passed before your change
15. confirmation that all nine pre-existing `security-headers.test.ts` assertions are intact, and that
    `style-src`, the matcher, and the a11y invariants are unchanged, each with the count or the quoted string
16. gate results with the pytest summary quoted verbatim and the vitest counts, every change accounted for
17. ANY approved decision you believe is wrong, and anything in section 4 or 5 you found to be inaccurate.
    Six previous slices in this whole found something an Orchestrator inventory had missed, and one
    Orchestrator note in the planning prompt was already wrong once.
18. the evidence ceiling: what the loopback proves, and what only the Cooperator's browser can confirm
19. commit and push result with both refs quoted, or an explicit statement that the candidate is uncommitted
20. deviations, risks, or missing evidence
21. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
22. Pre-Existing Failure Classification: none | <complete classification>
23. one smallest next step
24. report justification: new-mutation
25. authority-expiry statement

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may close
a logical whole. Your terminal report is your completion signal.

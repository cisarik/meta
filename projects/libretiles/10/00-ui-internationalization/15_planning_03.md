You are a WORKER instance in an Analytic Programming (AP) project.

Logical whole identity: ui-internationalization
Worker session ordinal: 15
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Prompt-level planning authority: GRANTED, read-only, bounded to this prompt
Worker session profile: Implementation-Planning Worker (read-only)
Task identity: R10 — plan the nonce Content-Security-Policy
Implementation authority: NONE. This exchange is plan-only.
Independence required: no
Evidence posture: non-independent
Continuity anchor: your terminal BLOCKED report for Worker session 15 exchange 03, whose
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` named a FIFTH structural defect — a coordinate
  contradiction between this prompt's header and its own report-format section
Authority renewal: prior planning authority expired with that terminal report. This exchange grants a
  complete NEW bounded read-only planning authority. Nothing from exchanges 01, 02 or 03 carries over as
  authority.
Reasoning recommendation: high. Basis — the obvious implementation is documented by Next.js and is still
  wrong for this repository in at least three specific ways. The value of this exchange is deciding those
  three things on evidence, not restating the doc.
Report justification: new-evidence
Context-pressure rule: report visible context usage if it exceeds 70%.

=====================================================================
ORCHESTRATOR CORRECTION — YOU WERE RIGHT FIVE TIMES ACROSS THREE STOPS
=====================================================================
All three stops are accepted in full. Every defect was verified against the pinned protocol before each
reissue, not taken on trust.

⛔ **EXCHANGE 03's DEFECT, THE FIFTH, WAS ALSO CAUSED BY A REPAIR.** Exchange 03 declared
`Worker exchange ordinal: 03` in its header while section 9 still told you to echo ordinal `02`.
`PROMPT_CONTRACTS.md:38-41` requires the terminal report to echo the authoritative coordinates **unchanged**,
so those two cannot both stand. Mechanical cause: I built each reissue by string-patching the previous file,
and the ordinal occurs in two textual forms — `ordinal: NN` with a colon in the header, `ordinal NN` without
one in the report instructions. A patch on the first form silently left the second.

`apfieldcheck.py` now checks coordinate consistency as well as field values, and it reproduces that exact
defect on the exchange-03 file. Against THIS prompt it reports zero defects and zero warnings.

⚠ FIVE STRUCTURAL DEFECTS ACROSS FOUR PROMPTS, three of them introduced by repairs. Every one was caught by
you before it could reach code. That is the protocol working as designed, and it is also the Orchestrator
failing repeatedly at the same class of task: treating a structural artifact as prose to be edited rather
than as data to be regenerated and checked.

⛔ **EXCHANGE 02's DEFECT WAS CAUSED BY MY FIX FOR EXCHANGE 01's.** Because the planner prompt itself now
carries `Native planning mode: not-used`, the field value
`Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used` read to me as
self-contradictory, so I "improved" it to `...with explicit implementation authority`. But
`PROMPT_CONTRACTS.md:725` fixes that field as a **closed literal**, not prose to adapt. In that spec block,
`<angle brackets>` mark fill-ins, `a | b` marks enums, and a bare string is a LITERAL. You were right: the
implementation prompt does separately need explicit implementation authority, and that requirement does not
license rewriting this field.

That is the same error as defects 2 and 3 wearing a different coat — treating a closed structural value as
prose. It is now mechanically checked rather than re-read: `/tmp/opencode/apfieldcheck.py` extracts the spec
blocks from the pinned `.ap` and diffs every field value. Run against this prompt it reports zero defects;
run against the exchange-01 and exchange-02 prompts it reproduces exactly the defects you found.

The exchange-01 defects, for the record:

```text
1  `Native planning mode: required` against a Default-mode session.
   PROMPT_CONTRACTS.md:695-698 — "If the client lacks that mode, the prompt must not be pasted. The
   Orchestrator reissues a complete `not-used` prompt and, when the task is planning or Discovery, grants
   explicit prompt-level read-only planning authority."  AP_WORKER.md:38-39 — "Missing, duplicated,
   mismatched, or contradictory routing stops work."   -> CORRECTED above.
2  `Report justification: new-analysis` is NOT in the closed enum.
   AP.md:2452-2454 — new-mutation | new-evidence | new-material-risk | changed-external-state |
   final-acceptance | explicit-closure. I invented a seventh value.   -> now `new-evidence`.
3  `planning-PASS | planning-PARTIAL | planning-BLOCKED` is NOT the structural result enum.
   PROMPT_CONTRACTS.md:203 — implementation-PASS | acceptance-PASS | publication-PASS | deployment-PASS |
   production-acceptance-PASS | not-applicable. Planning uses `not-applicable`.   -> corrected in section 9.
```

⚠ Refusing to produce a plan under a structurally invalid grant was the correct call, and your reasoning —
that issuing it "would falsely claim a valid planning exchange" — is exactly right. Do not soften that
behaviour in this exchange.

PLANNING-CYCLE ACCOUNTING, stated so you can verify rather than assume: exchanges 01, 02 and 03 produced NO
plan. All three were structural stops, not planning cycles. Therefore `Planning cycle: initial` still stands,
`Maximum plan-only cycles: 1` is NOT consumed, and this is still the first lawful planning attempt.
AP.md:2516 forbids repeating a plan-only cycle without new evidence; nothing is being repeated, because
nothing has been produced.

WHY CURRENT-SESSION REUSE IS APPROPRIATE: the task is read-only planning, independence is not required
(`PROMPT_CONTRACTS.md:359-371` — "Freshness alone never establishes independence"), your session is healthy,
it already performed lawful read-only reconnaissance, and it mutated nothing. Retained context from exchange
01 is CONVENIENCE, NOT AUTHORITY. Re-gate the repository and environment in section 1 regardless of what you
already read. If retained context conflicts with current repository evidence, current evidence wins and you
stop and report.

=====================================================================
0. PLAN-TO-EXECUTION CONTRACT
=====================================================================
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: the nonce CSP for `frontend/src/proxy.ts` and
  `frontend/src/lib/security-headers.ts` — mechanism, prerendered-route risk, matcher and request-header
  propagation, dev/prod split, test design, loopback evidence design, and rollback
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
Planning cycle effect of exchanges 01, 02 and 03: none

⛔ PROMPT-LEVEL READ-ONLY PLANNING AUTHORITY, granted explicitly because native planning mode is `not-used`
(PROMPT_CONTRACTS.md:695-698, AP.md:724). You may read any file in the repository, including
`node_modules`, run read-only Git queries, and grep freely. You may NOT write, create, delete, stage,
commit, push, install, build, or start any process. That boundary is the whole of your authority and it
expires with your terminal report.

⛔ YOU HAVE READ-ONLY PLANNING AUTHORITY AND NOTHING ELSE. Do not edit, create, or delete a file. Do not
commit, stage, or push. Do not run `npm install`, `npm run build`, or start any server. Do not run any
backend management command. Reading, grepping, and reading `node_modules` are all permitted and expected.

`Approve`, `Yes`, `Build`, `Continue`, an accepted plan, or an automatic interface transition grants you NO
implementation authority. A separate ORCHESTRATOR prompt does that, in a fresh session.

INFOSEC.md is active for this whole. This task's primary route is **R3**: `orch-01-F18` is an accepted
finding being re-dispositioned for correction, the change alters a security header on every response, and
the blast radius is the entire frontend. Section 4.10 also applies downstream — the corrector never
self-certifies, which is why implementation is a fresh session and not this one.

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

STOP if any value disagrees. Leave the tree exactly as you found it.

=====================================================================
2. MANDATORY READING, IN THIS ORDER
=====================================================================
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — "This is NOT the Next.js you know"
3. .ap/AP.md sections 5, 8, 9, 12, 18, 19, and the Plan-to-Execution Gate in .ap/PROMPT_CONTRACTS.md
4. .ap/AP_WORKER.md
5. .ap/INFOSEC.md sections 3, 6, 7, 8, 14, 16, 17
6. frontend/src/proxy.ts — all 29 lines
7. frontend/src/lib/security-headers.ts — all 114 lines
8. frontend/src/lib/security-headers.test.ts — all 168 lines, all nine `it` blocks
9. frontend/src/app/layout.tsx — all 38 lines
10. node_modules/next/dist/docs/01-app/02-guides/content-security-policy.md — the whole file, 729 lines
11. node_modules/next/dist/server/app-render/get-script-nonce-from-header.js — all of it
12. node_modules/next/dist/server/app-render/app-render.js around :209-210

=====================================================================
3. GOAL OF THIS EXCHANGE
=====================================================================
Produce a DECISION-COMPLETE plan that a fresh Implementation Worker can execute without re-deriving
anything, for replacing `script-src 'unsafe-inline'` with a per-request nonce.

You are NOT asked whether to do it. That is decided: `orch-01-F18` was re-dispositioned from
accepted-residual to be corrected as a nonce CSP, and it is the ONLY authorized `proxy.ts` touch in this
logical whole. You are asked to decide HOW, and to name what would make it unsafe.

=====================================================================
4. MEASURED FACTS — the Orchestrator ran all of this; do not spend budget re-deriving it
=====================================================================

--- 4.1 The current state, exact ---

```text
proxy.ts:5-17    export function proxy(request) — builds headers, NextResponse.next() with NO argument at
                 :12, then sets each header on the RESPONSE at :13-15. Nothing else. It is the Next.js 16
                 `proxy` file convention; frontend/src/middleware.ts DOES NOT EXIST.
proxy.ts:19-29   matcher `/((?!_next/static|_next/image|favicon.ico).*)` plus `missing` on
                 next-router-prefetch and purpose=prefetch.
                 ⚠ It does NOT exclude /api, unlike every example in the Next docs.
security-headers.ts:78-82   scriptSrc = ["'self'", "'unsafe-inline'", ...(isDevelopment ? ["'unsafe-eval'"] : [])]
security-headers.ts:84-99   the ten directives, joined; upgrade-insecure-requests added when !isDevelopment
security-headers.ts:87      style-src 'self' 'unsafe-inline'   <- a SEPARATE string site from :80
security-headers.ts:3-9     the five constant headers; :109-112 HSTS when !isDevelopment
exports          SecurityHeaderContext :11 · resolveConnectApiBase :29 · buildContentSecurityPolicy :70 ·
                 buildSecurityHeaders :102
```

`'unsafe-inline'` appears in exactly TWO source lines: `:80` (`script-src`) and `:87` (`style-src`). They are
independent strings.

--- 4.2 ⛔ THE BLOCKER: the nonce must be on the REQUEST, and this code only sets the RESPONSE ---

```text
app-render.js:209-210   const csp = headers['content-security-policy']
                                 || headers['content-security-policy-report-only'];
                        const nonce = typeof csp === 'string' ? getScriptNonceFromHeader(csp) : undefined;
get-script-nonce-from-header.js:11   CSP_NONCE_SOURCE_REGEX = /^'nonce-([A-Za-z0-9+/_-]+={0,2})'$/
                                :17   prefers the `script-src` directive, falls back to `default-src`
                                :22-23 a malformed nonce is IGNORED, silently
```

Next.js reads the nonce from the **request** headers. `proxy.ts:12` calls `NextResponse.next()` with no
argument, so nothing it sets is visible to the renderer. The doc form
`NextResponse.next({ request: { headers: requestHeaders } })` is required — see
`content-security-policy.md:67-83` and the warning at `proxy.md:465-466`.

⚠ `x-nonce` IS NOT READ BY NEXT.JS. `x-nonce` appears in exactly one file under `node_modules/next/dist/`:
the documentation. It is purely an application convention for reading the value back via `headers()`. Do
not plan around it unless the plan actually needs to read the nonce in application code — and state why if
it does.

Where the nonce lands once Next extracts it: `stream-ops.node.js:723-724` (the RSC flight-data inline
script), `app-render.js:2238-2245` (Fizz bootstrap), `:1895-1901` (polyfill `noModule` tags),
`required-scripts.js:18,49,64` (`ReactDOM.preinit`).

--- 4.3 There are ZERO app-authored inline scripts. That is the good news and it narrows the risk ---

Patterns over `frontend/src`, every one returning zero matches: `<script`, `dangerouslySetInnerHTML`,
`\beval\(`, `new Function`, `<style`. Also zero for `next/script` and `next/font`. `layout.tsx` has no
`<Script>`, no font loader, no inline anything.

So `script-src 'unsafe-inline'` is currently permitting **Next.js/React-generated** inline script only — the
RSC flight-data push. Measured in the committed build artifact `.next/server/app/_global-error.html`:

```text
10 <script> tags total · 5 inline (no src) · 5 external src="/_next/static/chunks/..."
first inline body: (self.__next_f=self.__next_f||[]).push([0])
nonce attribute present anywhere: FALSE
1 inline <style> (Next's built-in error CSS)
```

--- 4.4 ⛔ `style-src 'unsafe-inline'` MUST STAY, and you must say so explicitly ---

33 `style=` props across 16 files, plus imperative writes at `usePremiumBoardLighting.ts:83`,
`premiumSurface.ts:85-86`, `Board.tsx:183,200,228,233`. Those produce **style ATTRIBUTES**, and a CSP nonce
cannot cover a style attribute — nonces apply to `<style>` elements only. This is a recorded accepted
residual (`DEFECT_LEDGER.md:5709-5724`) and it is OUT OF SCOPE. Your plan must state that `:87` is not
touched, so no implementer treats the two `'unsafe-inline'` sites as one job.

--- 4.5 Dynamic rendering costs nothing here — but TWO routes are prerendered ---

```text
.next/prerender-manifest.json  routes = ['/_global-error', '/favicon.ico'] · dynamicRoutes = []
find .next/server/app -name "*.html"  ->  only _global-error.html
cause of the rest being dynamic   layout.tsx:13 awaits cookies()
no `export const dynamic|revalidate|fetchCache|runtime` anywhere in frontend/src
```

The doc's dynamic-rendering requirement (`content-security-policy.md:34-38`, `:391-397`) is therefore
already satisfied for every real page at zero cost. **But `_global-error` is prerendered and its inline
scripts carry no nonce** (`content-security-policy.md:181`: "Static pages are generated at build time, when
no request or response headers exist—so no nonce can be injected.").

--- 4.6 What the tests currently assert, and what they do not ---

`security-headers.test.ts`, 9 `it` blocks. It asserts six header names present (dev and prod), five
directives by `toEqual` (`default-src`, `frame-ancestors`, `object-src`, `base-uri`, `form-action`),
`connect-src` contents in three configurations, HSTS presence, `upgrade-insecure-requests` presence, and
that `script-src` does NOT contain `'unsafe-eval'` in prod.

```text
NOTHING asserts that 'unsafe-inline' is PRESENT, in either directive.
NOTHING asserts script-src by equality.
NOTHING asserts a nonce, 'strict-dynamic', or request-header propagation.
THERE IS NO TEST FOR proxy.ts AT ALL. No proxy.test.ts, no middleware.test.ts, nothing imports `proxy`.
```

So no existing assertion blocks the change — and the wiring you are changing is the one part of this
subsystem with zero coverage. `12_report_01.md:199-203` already recorded that limitation: "A green builder
test proves `buildSecurityHeaders()` returns the intended map. It does **not** prove Next.js invokes
`frontend/src/proxy.ts`."

--- 4.7 The audit-03 baseline, and a correction to an earlier Orchestrator note ---

The baseline is `DEFECT_LEDGER.md:141-153`: a Next.js production build served on a loopback port, `GET /`,
headers recorded verbatim. `script-src 'self' 'unsafe-inline'` is in it.

⚠ An earlier Orchestrator note said a re-probe would additionally show `Vary: Accept-Language` and
`Content-Language` because of slice R7. **That note was WRONG and is corrected.** `LocaleMiddleware` is
Django middleware; it cannot touch a Next.js response. The frontend baseline is unaffected by R7, so a
re-probe should differ ONLY by what R10 itself changes. If you observe any other difference, report it as a
finding rather than explaining it away.

=====================================================================
5. ⛔ THE FIVE DECISIONS THIS PLAN MUST MAKE
=====================================================================
For each: state the decision, the evidence, the alternative you rejected, and what would falsify your
choice. A plan that restates the Next.js guide without resolving these is not decision-complete.

```text
D1  THE PRERENDERED _global-error PAGE.
    Its HTML has 5 inline scripts and no nonce. Under `script-src 'self' 'nonce-X'` those are blocked, so
    the global error page would fail to hydrate exactly when something has already gone wrong. Decide the
    disposition and prove the reasoning. Note that 'strict-dynamic' does NOT rescue it — the first inline
    script itself needs a nonce or an 'unsafe-inline' fallback. Consider at minimum: accept the degradation
    and record it as a residual; force the route dynamic; or keep a narrowly scoped fallback. Say which and
    why, and say what a user would actually observe.

D2  'strict-dynamic': INCLUDE OR NOT.
    content-security-policy.md:52 recommends `'self' 'nonce-${nonce}' 'strict-dynamic'`. But
    'strict-dynamic' makes CSP3 browsers IGNORE 'self' and host allowlists for script-src, so the five
    external /_next/static/chunks/*.js tags stop being covered by 'self' and are allowed only through
    propagation from a nonced script. Decide, with reasoning about how Next actually loads those chunks
    (see required-scripts.js and the bootstrap path in 4.2). If you include it, say what breaks if a chunk
    is ever loaded outside that propagation. If you exclude it, say what attack 'strict-dynamic' would have
    mitigated that you are choosing not to mitigate.

D3  THE MATCHER AND REQUEST-HEADER PROPAGATION.
    You must switch to NextResponse.next({ request: { headers } }). That mutation also reaches the four
    /api/* route handlers, because this matcher does not exclude /api. Meanwhile audit-03 VERIFIED that
    security headers ARE present on /api/models, /api/prompts and /api/ai/move — so excluding /api the way
    the Next docs do would REMOVE headers that a recorded audit confirmed. Resolve that tension explicitly.
    Do not change the matcher silently in either direction.

D4  DEV VERSUS PROD.
    'unsafe-eval' is required in development (content-security-policy.md:42) and is already dev-only at
    security-headers.ts:81. The doc's dev variant also keeps style-src permissive and nonces only in
    production (:542-570). Decide whether the nonce applies in both modes or production only, and what the
    developer experience is under your choice. A plan that makes `npm run dev` unusable is rejected.

D5  HOW THE NONCE IS GENERATED.
    It must be fresh per request and must satisfy /^[A-Za-z0-9+/_-]+={0,2}$/ or Next silently ignores it
    (get-script-nonce-from-header.js:11,22-23). Name the exact API, say whether it is available in the
    Next.js proxy runtime, and say how the plan proves the value is not reused across requests. Silent
    ignoring is the dangerous failure mode here: the header would look correct and no nonce would be
    applied.
```

=====================================================================
6. WHAT THE PLAN MUST ALSO CONTAIN
=====================================================================

```text
6.1  EXACT FILE ALLOWLIST for the implementation slice, with the purpose of each file, and an explicit
     statement of what is NOT touched. `security-headers.ts:87` (style-src) belongs in the not-touched list.
6.2  THE PURE/IMPURE SPLIT. buildContentSecurityPolicy is currently pure and unit-tested. A nonce is
     per-request. Say exactly which function gains a parameter, what its signature becomes, and how the
     pure part stays pure — this project extracts arithmetic into pure exported functions precisely so it
     can be tested (see nextPickerHighlight, filterPickerOptions, composeAnnouncement).
6.3  THE TEST PLAN, test by test. For each: its name, what it asserts, and the exact pre-fix failure you
     expect. Include at minimum: a nonce appears in script-src; 'unsafe-inline' is ABSENT from script-src;
     'unsafe-inline' is STILL PRESENT in style-src; two calls produce two different nonces; a nonce that
     would be silently ignored by Next's regex is impossible. State plainly which of these can be tested
     at all in a vitest `environment: "node"` suite with no DOM, and which cannot.
6.4  ⛔ THE PROXY WIRING TEST. Section 4.6 shows proxy.ts has ZERO coverage today and that the wiring is the
     part your change actually alters. Design a test for it, or argue on evidence that it cannot be tested
     in this harness — and if it cannot, say what that leaves unproven.
6.5  THE LOOPBACK EVIDENCE PLAN. The established technique is: production build, `next start` bound to
     loopback on a NON-DEFAULT port, probe with an HTTP client, stop the server BY EXACT PID. Design the
     probe. The decisive assertion is not that the header contains a nonce — it is that the nonce in the
     CSP header MATCHES the nonce attribute in the served HTML's <script> tags, because that is the only
     thing that proves Next actually picked it up. Also design the per-request-uniqueness check.
     ⛔ Port 3000 is the Cooperator's own dev server. Choose another. NEVER plan a broad pattern kill such
     as `pkill -f next-server`.
6.6  THE audit-03 DIFF PLAN. Which headers must be byte-identical to DEFECT_LEDGER.md:141-153, which single
     directive is expected to change, and what you will do if anything else differs.
6.7  ROLLBACK. Exactly what reverting looks like, what a partial failure in production would look like,
     and how a reader would recognize it. INFOSEC section 14 governs any residual you propose accepting.
6.8  RESIDUALS you propose to accept, each with severity and the reason, per INFOSEC sections 7 and 14.
6.9  EVIDENCE CEILING. Browser MCP is locked fork 7 and the Cooperator has stated he uses no screen reader,
     though that is irrelevant here. Say what the suite plus the loopback probe prove, and what only the
     Cooperator's own browser can confirm. This project has twice shipped a defect behind eight green gates
     because nothing rendered; do not add a third.
```

=====================================================================
7. NEGATIVE AUTHORITY FOR THIS EXCHANGE
=====================================================================
- ⛔ No file edits, no creations, no deletions, no commits, no staging, no push.
- ⛔ No `npm run build`, no `npm install`, no `next start`, no server of any kind, no process kill.
- ⛔ Do not plan changes to `security-headers.ts:87` (`style-src`). Section 4.4.
- ⛔ Do not plan a Django change. R10 is frontend-only. `backend/` has no CSP at all — verified, zero code
  matches for `content-security-policy` outside `.venv`.
- ⛔ Do not plan to add a dependency. No CSP library, no nonce library.
- ⛔ Do not plan to touch `prompts.ts` and its pinned SHA-256, `ai-move-stream.ts`, `api/ai/move/route.ts`,
  `types.ts` (locked fork 2), or the locked fork 11 provider files.
- ⛔ Do not plan to weaken or delete any of the nine existing `security-headers.test.ts` assertions. If you
  believe one must change, name it, quote it, and justify it the way this project requires.
- ⛔ Do not plan to change the a11y invariants settled by S11/R14/R15: `aria-live` and `role="status"` must
  each remain exactly 1, `role="dialog"` and `aria-modal` exactly 4.
- Do not create BOOT_*, NEXT_*, WORKERS.md, or HANDOFF files. Your plan lives in your report.

=====================================================================
8. STOPPING CONDITIONS
=====================================================================
Stop and report if: a section 1 gate value disagrees; ANY field in this prompt still conflicts with the
pinned `.ap` protocol — you have already caught four across two exchanges, so check for a fifth rather than
assuming the mechanical checker is exhaustive; retained context from exchanges 01-03 conflicts with current
repository evidence; you conclude the nonce CSP cannot be implemented
safely in Next.js 16.3.4 without a dependency or a `next.config.ts` change you are not authorized to plan;
you find that `NextResponse.next({ request: { headers } })` breaks something measurable in this repository;
you find a sixth decision of the same weight as D1-D5 that section 5 missed; any instruction here conflicts
with AGENTS.md, .ap/AP.md, .ap/INFOSEC.md, or observed repository truth.

If you stop, use `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and give the ONE causal blocker, the
smallest authority expansion that would resolve it, and the exact evidence.

=====================================================================
9. TERMINAL REPORT
=====================================================================
Begin with exactly:

### Report for ORCHESTRATOR_CHAT

Then, in order:
 1. logical whole `ui-internationalization`, Worker session ordinal 15, Worker exchange ordinal 04
 2. status: PASS | PARTIAL | BLOCKED
 3. phase-qualified result: not-applicable   (planning has no PASS value; PROMPT_CONTRACTS.md:203)
 4. the commit you planned against, and confirmation the working tree is untouched — quote
    `git status --porcelain=v1`
 5. the Plan-to-Execution and Planning Record field values you operated under, echoed back, plus the
    continuity anchor and a statement that prior authority had expired
 6. D1 through D5: decision, evidence with file:line, rejected alternative, and what would falsify it
 7. the exact file allowlist for implementation, and the not-touched list
 8. the pure/impure split with the proposed function signature
 9. the test plan, test by test, with expected pre-fix failures, and an explicit statement of which
    assertions are impossible in a node-environment suite
10. the proxy-wiring test design, or the evidenced argument that it is untestable here plus what that
    leaves unproven
11. the loopback evidence plan including the port you propose, the PID-exact stop, and the
    header-matches-HTML assertion
12. the audit-03 diff plan
13. rollback, and what a partial production failure would look like
14. residuals you propose accepting, with severity and reasoning per INFOSEC 7 and 14
15. the evidence ceiling
16. ANY finding you made while reading that this prompt did not anticipate — including anything in section
    4 you believe is wrong. Five previous slices in this whole found something an Orchestrator inventory
    had missed, and section 4.7 is an Orchestrator note that was already wrong once.
17. what you did NOT investigate, and why it does not affect the plan
18. Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
19. one smallest next step
20. report justification: new-evidence
21. authority-expiry statement: planning authority expired with this report; no implementation authority was
    granted or is implied

Logical-whole closure: not-closed. Do not emit any project closure signal. Only the ORCHESTRATOR may close
a logical whole. Your terminal report is your completion signal.

Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator, not the Cooperator, and not an auditor. You have implementation authority for an exact allowlist and nothing else. You have NO audit authority and you never certify your own correction. Do not enable any native planning mode.

Logical whole identity: backend-security-hardening
Worker session ordinal: 12
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: unblock-typecheck-and-finish-the-proxy-bump
Task type: allowlist expansion after a correctly reported stop condition, then completion of the blocked slice
Security task class: accepted-finding correction (INFOSEC.md 4.10)
INFOSEC route: R3 — unchanged from exchange 01. A fresh independent re-audit is already scheduled; you do not perform it.

Continuity anchor: your terminal BLOCKED report for Worker session 12, exchange 01, task `bump-next-and-migrate-proxy-convention`, which returned `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and left the authorized candidate uncommitted in the working tree at `HEAD = 7a197dacb2ba110ff59dea01379ef0e5b53c7efe`.
Authority renewal: the authority from exchange 01 EXPIRED with that report. This prompt grants complete new bounded authority: the same scope as exchange 01, PLUS exactly two additional test files, PLUS one `package.json` script. Retained context from exchange 01 is convenience, not authority.
Why this session: you performed the migration and read the 16.3.4 documentation, so you hold the most accurate model of both. Independence is not required for a correction. Your evidence remains NON-INDEPENDENT.

**You did the right thing.** You hit a genuine stop condition, refused to touch files outside your allowlist, refused to commit a failing tree, preserved the first causal error with its exact text, and escalated. That is the behaviour this protocol exists to produce. The blocker was the Orchestrator's allowlist being too narrow, not your work.

Implementation authority: explicit
Audit authority: none
Accepted finding IDs: audit-02-F01, orch-03-G01, the `frontend/src/middleware.ts` sub-residual of orch-01-F18, and the newly established orch-04-F22 described in section 1
Correction authority: those IDs only
Exact baseline: `HEAD = 7a197dacb2ba110ff59dea01379ef0e5b53c7efe` with the EXACT dirty working tree described in the gate below
Changed-path allowlist: exactly the paths listed in section 4 and no others
Independence required: no
Evidence tier: E3
Evidence tier basis: unchanged from exchange 01 — a minor bump of the framework serving every request, plus the file that emits every security header.
Combined implementation envelope: allowed
Independent acceptance: required-separate-fresh-worker. You do not perform it.
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: full-fresh — a security boundary is in scope, so scoped re-acceptance is not valid. The scheduled comprehensive re-audit is that full fresh acceptance.
Rollback or recovery checkpoint: `HEAD` is still the clean start commit. Discarding the working tree restores it exactly; you are NOT authorized to discard it.
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none
Worker topology: single-active
Accountable Worker: one WORKER
Sub-agents/internal delegation: not-used
External trace disposition: not-used; do not write to /home/agile/meta/** or any archive location
Provider call authority: none. `LIBRETILES_AI_PLAY_LIVE` stays unset. The local server in section 3 must never reach a provider.
Secret authority: none. Never read, print, or summarise `backend/.env` or `frontend/.env.local`.
Network authority: the npm registry if a reinstall is needed, `npm audit`, localhost HTTP to your own bound server, the authorized `git ls-remote` gate, and one `git push`. Nothing else.
Side-effect authority: reversible local mutation of the allowlisted paths and of `frontend/node_modules`; one short-lived loopback HTTP server on a non-default port which you must stop; one remote non-force fast-forward push to main.

Recommended reasoning: High
Recommendation basis: the two type errors are two lines, but the reason they were invisible until now is the interesting part and it changes what "the build passed" has meant in this project. Section 1 explains it; do not treat this as a trivial patch.
Escalation or downgrade gate: stop with `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` if a correct fix needs a path outside the expanded allowlist, if a non-incremental typecheck reveals errors beyond the two named, or if you still cannot obtain the section 3 HTTP evidence.

REPOSITORY GATE — this tree is DELIBERATELY DIRTY. Reconcile before any edit; stop if any line disagrees:
  git rev-parse HEAD                      -> 7a197dacb2ba110ff59dea01379ef0e5b53c7efe
  git rev-parse HEAD:.ap                  -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git -C .ap rev-parse HEAD               -> 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
  git status -sb                          -> ## main...origin/main, no divergence
  git ls-remote origin refs/heads/main    -> 7a197dacb2ba110ff59dea01379ef0e5b53c7efe
  git status --porcelain=v1               -> EXACTLY these five lines and nothing else:
       M frontend/package-lock.json
       M frontend/package.json
       M frontend/src/lib/security-headers.test.ts
       D frontend/src/middleware.ts
      ?? frontend/src/proxy.ts

The Orchestrator observed that exact porcelain, and observed that `frontend/node_modules/next/package.json` reports `16.3.4`, so the install is already in place and a reinstall is optional. If the porcelain has MORE lines than those five, something drifted since your report: stop and report the difference rather than working around it. Do not discard, stash, reset, clean, or checkout anything.

MANDATORY READING
- this prompt, in full
- your own exchange-01 report, as evidence only, not authority
- frontend/src/lib/api.test.ts around line 145, and frontend/src/lib/ai-play-diagnostic.test.ts around lines 104-107
- frontend/tsconfig.json in full — note `"incremental": true` and that `include` covers `**/*.ts`
- .ap/AP_WORKER.md sections on current-session continuation, validation, and stopping conditions
- .ap/PROMPT_CONTRACTS.md — "Pre-Existing Failure Classification Contract" (you will use it properly this time), "Failure-Preserving Automation Fields", "Worker Report Header"
- everything you already read in exchange 01 remains relevant; do not re-read the 16.3.4 docs unless something contradicts you

================================================================
1. WHAT THE ORCHESTRATOR ESTABLISHED, AND WHERE YOUR CLASSIFICATION WAS WRONG
================================================================

The Orchestrator ran `npx tsc --noEmit -p tsconfig.json` against your working tree and got EXACTLY your two errors and no others:

    src/lib/ai-play-diagnostic.test.ts(106,29): error TS2345: Argument of type
      '{ LIBRETILES_AI_PLAY_LIVE: string; }' is not assignable to parameter of type 'ProcessEnv'.
      Property 'NODE_ENV' is missing ...
    src/lib/api.test.ts(145,25): error TS2352: Conversion of type '[]' to type
      '[string, RequestInit]' may be a mistake ... Source has 0 element(s) but target requires 2.

**Your `Pre-Existing Failure Classification` for `api.test.ts:145` was wrong, and this matters.** You classified it as bump-caused, attributing it to the new 16.3.4 global `RequestInit` augmentation. It is not. The error the compiler reports is an ARITY mismatch: `[]` has zero elements and the target tuple requires two. That comparison does not depend on the shape of `RequestInit` at all. `fetchMock` is created as `vi.fn(async () => jsonResponse(...))` with no declared parameters, so `fetchMock.mock.calls[0]` is typed `[]`, and casting a zero-length tuple to a two-length tuple was never valid.

`api.test.ts` was created at commit `9ff9ac5`. `ai-play-diagnostic.test.ts` was created at `b18e50e`, and line 105 immediately above the failure already does `{} as NodeJS.ProcessEnv` — the author knew a cast was needed there and did not apply it on the next line.

So **both errors are pre-existing latent defects, not bump regressions.** The `next` bump did not create them; it invalidated the incremental typecheck cache that was hiding them. `frontend/tsconfig.json` sets `"incremental": true`, and `next build` reuses that cache.

That establishes a new finding, which you are authorized to remedy:

    Finding ID: orch-04-F22
    Title: `npm run build` can report success while type errors exist, because its typecheck is incremental
    Status: confirmed (accepted for correction)
    Severity: low for the product, medium for verification integrity
    Confidence: high
    Evidence class: established-static plus reproduced-dynamic (Orchestrator ran a full typecheck and
      got two errors that `npm run build` had reported as success at both 9ff9ac5 and 7a197da)
    Affected location: frontend/tsconfig.json `"incremental": true`; the absence of any non-incremental
      typecheck in the standing gates
    Security property: the integrity of the evidence this project's gates produce
    Impact: `npm run build` has been a standing gate for this entire era. Every "build succeeds" claim
      in it — including the Orchestrator's own independent re-measurements — was weaker than stated,
      because the typecheck could be partially served from cache. No product defect resulted, but a
      verification hole did.
    Exploitability conclusion: not applicable
    Smallest safe correction direction: add a non-incremental typecheck as an explicit, separately
      runnable gate so a cached success can never again stand in for a real one.
    Regression-test requirement: the gate itself; it fails today and passes after the two fixes.
    Acceptance-blocking decision: non-blocking for the product, but the gate must exist before this
      slice's evidence can be trusted.

This is the Orchestrator's own verification chain being wrong, not yours. It is recorded plainly for the same reason your own misclassification is: a report that reads better than the evidence is worse than one that does not.

================================================================
2. WHAT TO IMPLEMENT
================================================================

**A. Fix the two type errors, minimally, inside the test files.**

  - `frontend/src/lib/api.test.ts:145`: make the cast valid. Going through `unknown`, or typing the mock's parameters, or reading the call array without a tuple assertion are all acceptable. Choose the one that keeps the test's ASSERTIONS identical — it must still prove that `api.logout` posts to `/api/auth/logout/` with the refresh token in the body and the access token as a bearer. Do not weaken or delete an assertion to make a type happy.
  - `frontend/src/lib/ai-play-diagnostic.test.ts:106`: supply what `ProcessEnv` requires, or cast as the line above it already does. Keep the test's meaning exactly: it must still prove that live mode is refused without the sentinel and enabled with it. That positive path matters — this project has a recorded lesson about a guard being verified while the enabled branch did not exist.

Two lines of intent. If either fix grows past a few lines or needs a non-test file, stop and escalate.

**B. Add a non-incremental typecheck script**, as the remedy for `orch-04-F22`. One line in `frontend/package.json` `scripts`, running the TypeScript compiler with no emit and incremental caching explicitly disabled. Name it something obvious such as `typecheck`. Do NOT change `frontend/tsconfig.json`: `"incremental": true` is useful for editors and for `next build` speed, and removing test files from `include` would have hidden exactly the drift we just found. The remedy is an additional gate, not a weakened configuration.

**C. Then finish exchange 01's slice.** Everything from that prompt still stands and is not re-litigated here: the two version bumps are already in the tree, `frontend/src/proxy.ts` already exists with only the export name changed from `middleware` to `proxy`, `frontend/src/middleware.ts` is already deleted, and the five production-context assertions are already added to `security-headers.test.ts`. The Orchestrator read `proxy.ts` and confirms it is a faithful migration. What remains is the evidence you could not reach.

================================================================
3. THE EVIDENCE THAT STILL HAS TO BE OBTAINED
================================================================

**(a) The build must register the proxy.** You recorded the baseline route table, which ended with `ƒ Proxy (Middleware)` and was preceded by the deprecation warning that the Cooperator also observed independently in `npm run dev`:

    ⚠ The "middleware" file convention is deprecated. Please use "proxy" instead.

Now get the AFTER state. Run `npm run build` and quote the full route table plus whatever Proxy line appears. If the parenthetical `(Middleware)` is gone because the file is no longer the deprecated alias, that is the expected and desired outcome — quote both strings exactly. **If no Proxy line appears at all, the header injection is dead: stop and escalate, do not ship.** Also state whether the deprecation warning is gone.

Do not treat `.next/server/proxy.js` or `middleware-manifest.json` from an incomplete build as registration proof. You already refused to do that once; hold that line.

**(b) The builder tests.** Already 11 passed. Restate the limit you correctly identified: a green builder test does not prove the framework invokes the file.

**(c) The loopback HTTP readback. This is the load-bearing evidence and it is why the slice is not done.**

  1. Confirm the port is free before binding. Use **3100**; port 3000 is occupied by the Cooperator's own dev server and must not be disturbed. If 3100 is taken, choose another free high port and say which.
  2. Build, then start the production server on that port bound to loopback.
  3. Request only the ROOT document over loopback. Capture the response headers separately from the body. Do not crawl, do not request an API route, do not trigger a provider call, do not touch the database.
  4. Record the OBSERVED VALUE, verbatim, of `Content-Security-Policy`, `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options`, `Permissions-Policy`, `Cross-Origin-Opener-Policy`, and whether `Strict-Transport-Security` is present.
  5. Quote the FULL received `Content-Security-Policy` and compare it directive by directive with what `buildSecurityHeaders` produces for a production context. Any difference is a finding you report.
  6. Stop the server and report the outcome. Preserve the first causal error; a cleanup failure must never overwrite a primary result.

`next start` sets `NODE_ENV=production`, so `Strict-Transport-Security` and `upgrade-insecure-requests` SHOULD appear even over plain local HTTP. That is expected in this probe and is not a defect. Do not "fix" it.

**(d) Advisory re-verification.** You already reported this and the Orchestrator has no correction to it: three advisories remain, all `dev`-flagged, matching the `audit-02-F07` disposition; `next`, `sharp`, and the nested `postcss` all left their ranges; `picomatch` left the set as a transitive patch. Restate it briefly and confirm it is unchanged after your two test fixes.

================================================================
4. EXACT PATH ALLOWLIST — expanded, and this is the whole of it
================================================================

Carried over from exchange 01, already modified in the tree:
  frontend/package.json                      (the two version bumps; PLUS the one new script from item B)
  frontend/package-lock.json                 (generated)
  frontend/src/proxy.ts                      (new, already written)
  frontend/src/middleware.ts                 (deleted, already deleted)
  frontend/src/lib/security-headers.test.ts  (already extended)

NEWLY ADDED by this exchange, and the only expansion:
  frontend/src/lib/api.test.ts               (item A, the one type fix)
  frontend/src/lib/ai-play-diagnostic.test.ts (item A, the one type fix)

Do not touch: `frontend/tsconfig.json`, `frontend/next.config.ts`, `frontend/src/lib/security-headers.ts`, `frontend/src/lib/api.ts`, `frontend/src/lib/ws.ts`, any other test, any file under `frontend/src/app/**` or `frontend/src/components/**` or `frontend/src/hooks/**`, any backend file, `README.md`, `AGENTS.md`, `docs/**`, `.ap/**`, `scripts/**`.

Do not add `typescript.ignoreBuildErrors` or any equivalent to `next.config.ts`. Suppressing the typecheck to make a build pass would convert a two-line fix into a permanent blind spot, and it is an explicit stop condition.

**Standing Cooperator decision, still in force:** the nine AI providers are frozen pending their own logical whole. No change to any provider list, constant, tier, exact model tuple, or provider documentation, anywhere.

Do not touch, reopen, or re-litigate: `audit-02-F05`, `audit-02-F06`, `orch-02-D11`, the `script-src` and `style-src` `'unsafe-inline'` residuals of `orch-01-F18`, every `audit-02` rejected-false-positive, and everything landed in `bbba2e9`, `8e82f3b`, `9ff9ac5`, and `7a197da`.

================================================================
5. GATES — all green at your terminal report
================================================================

  npm run typecheck        -> the new non-incremental gate. Report its result BEFORE your fixes (expect the two errors) and AFTER (expect clean). This is the before/after evidence for orch-04-F22.
  npx vitest run           -> whole frontend suite. Your exchange-01 measurement was `326 passed, 3 skipped` across 24 files with 1 skipped file. Report the new total.
  npm run lint             -> exit 0, no findings
  npm run build            -> MUST succeed, and must print a Proxy line
  backend pytest           -> `326 passed, 4 skipped` at `7a197da`, Orchestrator-measured. The backend is untouched; run it once as cheap proof and quote the summary verbatim.

HONEST LIMITATIONS YOU MUST STATE RATHER THAN WORK AROUND:
  - no browser observation. A successful loopback readback proves the headers are emitted; it does not prove a browser enforces the policy without breaking the application. Rendered behaviour stays with Cooperator-executed acceptance.
  - the local build is not the deployment artifact, and no CI or provenance attests any artifact (`audit-02-F05`).
  - the Next.js advisories were not reproduced; no proof of concept is authorized.
  - the AI move stream, the judge route, and websocket play were not exercised end to end.

================================================================
6. NEGATIVE AUTHORITY
================================================================

- Change only the allowlisted paths. Preserve unrelated work. Do not discard, stash, reset, clean, or checkout the existing candidate.
- Two type fixes and one script line. No other change to those three files.
- No further dependency bump. React does not move.
- Do not weaken the Content-Security-Policy in any environment.
- Do not weaken, delete, skip, or xfail any test or any assertion, including the two you are fixing.
- Do not suppress the typecheck in `next.config.ts` or `tsconfig.json`.
- Do not run `npm ci`, `npm audit fix`, `npm update`, or any `poetry` mutation.
- The local server binds to loopback on a non-default port, serves only your own root-document request, and is stopped before your report.
- No live provider call. Do not read `backend/.env` or `frontend/.env.local`. No credential value, prefix, length, or hash in your report.
- No `git add -A`, no `git add .`, no force push, no amend, no rebase, no reset, no clean, no stash, no branch, no tag.
- Do not audit your own correction beyond the required gates. You do not certify it, you do not close the logical whole, and you emit no closure signal. If the same assumption survives this correction and its recheck, return `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` rather than attempting a second automatic correction.

================================================================
7. GIT AUTHORITY
================================================================

ONE commit containing the whole slice — the bumps, the proxy migration, the deletion, the test extensions, the two type fixes, and the script — then one non-force fast-forward push, then a public readback.
- Stage exactly the seven allowlisted paths by EXPLICIT PATH, including the DELETION of `frontend/src/middleware.ts` and the ADDITION of `frontend/src/proxy.ts`.
- Review the FULL staged diff, including the whole `package-lock.json` diff, before committing.
- Suggested message: `fix(deps): bump next to 16.3.4 and migrate to the proxy convention`. The body names audit-02-F01, orch-03-G01, the closed `middleware.ts` sub-residual of orch-01-F18, and orch-04-F22, and states that the headers were verified by a loopback HTTP readback but not in a browser.
- PRE-PUSH GATE, mandatory: `git ls-remote origin refs/heads/main` must still equal `7a197dacb2ba110ff59dea01379ef0e5b53c7efe`. If it advanced, STOP and escalate.
- Push `git push origin main` only, no flags. READBACK `git ls-remote origin refs/heads/main` and `git rev-parse HEAD`; they must be equal and be your new commit. Porcelain empty afterwards.

================================================================
8. REPORT CONTRACT
================================================================

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Then exactly once:

Logical whole identity: backend-security-hardening
Worker session ordinal: 12
Worker exchange ordinal: 02

Then, in this order:
- status; Phase-qualified result, labelled NON-INDEPENDENT
- the continuity anchor you verified, and confirmation that the five-line dirty porcelain matched exactly, or the exact difference if it did not
- start and end commit; `git diff --stat` and `git diff --name-only` against `7a197da`; the delete/add evidence for the proxy file; which allowlisted paths you did not need
- repository gate and pre-push gate evidence
- capability recheck: material changes since the continuity anchor, required capabilities still observed, unknown or degraded capabilities, and the statement that capability does not grant authority
- item A: the exact change in each of the two test files, and confirmation that no assertion changed meaning
- item B: the exact script line, and the `npm run typecheck` result BEFORE and AFTER
- a corrected `Pre-Existing Failure Classification` for both errors, using the contract fields properly. The Orchestrator's position is that both are pre-existing and neither is bump-caused; if your evidence disagrees, say so with the evidence — you have been right against the Orchestrator before in this project.
- evidence (a): the full AFTER route table, the Proxy line, and whether the deprecation warning is gone
- evidence (b): result plus your statement of its limit
- evidence (c): port and why; the verbatim observed value of all six headers plus HSTS presence; the FULL received CSP string; the directive-by-directive comparison; the server stop outcome
- evidence (d): restated briefly and confirmed unchanged
- all gate output, with the backend pytest summary quoted verbatim
- the honest-limitations statements
- residuals
- authorized Git result with public readback and post-push porcelain
- deviations, risks, missing evidence
- out-of-scope observations, labelled as observations
- one smallest next step (expected: the Orchestrator issues the comprehensive fresh independent re-audit, INFOSEC 4.11 profile P-10, at the final commit)
- Report justification: new-mutation
- Logical-whole closure: not-closed
- Authority expiry statement
- Resolved Execution Issues / Near-Misses
- Pre-Existing Failure Classification

Stop conditions: the dirty porcelain not matching the five expected lines; remote main advanced; a non-incremental typecheck revealing errors beyond the two named; a fix needing a non-allowlisted path; the Proxy line absent from a successful build; any required header missing from the HTTP readback; any need to weaken the CSP or suppress the typecheck; inability to obtain the section 3(c) evidence; any existing test regressing.

Authority expiry: this exchange's authority expires with your terminal report. Retained context is not a renewal.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT

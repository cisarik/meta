### Report for ORCHESTRATOR_CHAT

Logical whole identity: ui-internationalization  
Worker session ordinal: 15  
Worker exchange ordinal: 04  
Status: PASS  
Phase-qualified result: not-applicable  
Report justification: new-evidence

Canonical commit: `f983c3dcce19534466a86b06605e1a02f8bd2bf3`  
Pinned `.ap` commit: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`  
Worktree state: clean before and after investigation  
Remote `origin/main`: matches canonical commit

No files were changed. No tests, builds, servers, dependency operations, or backend commands were run.

## Planning envelope

- Planning layer: implementation-planning
- Orchestration planning owner: ORCHESTRATOR
- Plan scope: nonce-based CSP in [proxy.ts](/home/agile/Projects/libretiles/frontend/src/proxy.ts) and [security-headers.ts](/home/agile/Projects/libretiles/frontend/src/lib/security-headers.ts), including prerender risk, matcher/request propagation, development/production behavior, tests, loopback verification, residuals, and rollback
- Plan disposition: approval-gated
- Implementation in this worker session: prohibited
- Plan cycle: initial
- Maximum plan cycles: 1
- Prior plan report: none
- Targeted revision: none
- Changed boundary: none
- Preserved boundary: none
- Automatic revisions consumed: 0
- Exchanges 01–03 cycle effect: none
- Execution authority event: `explicit ORCHESTRATOR prompt with Native planning mode: not-used`
- Post-plan execution placement: fresh-worker-session
- Stop condition: this terminal report

Continuity was restored from the exchange-03 terminal `BLOCKED` report. That authority expired; exchange 04 supplied a new, complete, internally coherent read-only planning grant.

## Recommended implementation plan

### 1. Nonce generation and ownership

Generate exactly one nonce at the start of each `proxy()` invocation:

```ts
const nonce = Buffer.from(crypto.randomUUID()).toString("base64")
```

This follows the repository’s pinned Next.js CSP documentation and is valid because Proxy uses the Node.js runtime by default.

Ownership boundary:

- `proxy.ts` owns entropy and creates the nonce.
- `security-headers.ts` remains deterministic and receives the nonce explicitly.
- No timestamp, `Math.random()`, module-scoped nonce, dependency, environment variable, or caller-controlled value is introduced.

Recommended signatures:

```ts
buildContentSecurityPolicy(
  context: SecurityHeaderContext,
  nonce: string,
): string

buildSecurityHeaders(
  context: SecurityHeaderContext,
  nonce: string,
): Record<string, string>
```

Add a non-exported validation helper equivalent to:

```ts
/^[A-Za-z0-9+/_-]+={0,2}$/
```

This matches the nonce value grammar used by the pinned Next.js parser. Reject invalid input by throwing before emitting a policy; do not allow Next.js to silently ignore a malformed nonce.

The builder must remain pure: identical context and nonce produce identical headers, with no time, randomness, mutation, or global state.

### 2. Production and development policy

Change only `script-src`.

Production:

```text
script-src 'self' 'nonce-<fresh nonce>' 'strict-dynamic'
```

Development:

```text
script-src 'self' 'nonce-<fresh nonce>' 'strict-dynamic' 'unsafe-eval'
```

Keep the existing `style-src 'self' 'unsafe-inline'` byte-for-byte. It is explicitly outside this correction.

Rationale:

- Next.js extracts a nonce from the request CSP and applies it to framework-generated inline scripts, preload/preinit entries, polyfills, bootstrap scripts, and streamed flight scripts.
- `'strict-dynamic'` restricts execution to the nonced trust root and its descendant loads.
- Retaining `'self'` provides legacy-CSP fallback.
- Development retains `'unsafe-eval'` for React/Next debugging behavior while exercising the same nonce propagation path as production.
- A production-only nonce would conceal integration failures until deployment.

Falsification condition: if production loopback produces any script element without the response nonce, or browser verification reports a legitimate blocked chunk outside the trusted load chain, do not silently remove `'strict-dynamic'`; return for a targeted correction.

### 3. Matcher and request propagation

Keep the matcher in [proxy.ts](/home/agile/Projects/libretiles/frontend/src/proxy.ts:19) byte-for-byte, including its current coverage of `/api`.

Use conditional upstream propagation:

- For `/api` and `/api/*`:
  - call `NextResponse.next()` without a request-header override;
  - attach the complete security-header set to the response.
- For all other matched requests:
  - clone `request.headers`;
  - set only `Content-Security-Policy` on that cloned request header collection;
  - call `NextResponse.next({ request: { headers: requestHeaders } })`;
  - attach the exact same CSP and other security headers to the response.

Do not add `x-nonce`. The application does not need to read the nonce; Next.js reads it from the forwarded request CSP.

This preserves audited API response headers without forwarding a meaningless randomized CSP header into API route handlers. Current handlers neither render framework scripts nor require this internal header.

Rejected alternatives:

- Excluding `/api` would remove the existing response-security-header coverage.
- Forwarding request CSP to every API route creates needless internal variability and future cache/forwarding risk.
- A global `'unsafe-inline'` fallback would undo the correction and would be ignored by CSP3-capable browsers when a nonce and `'strict-dynamic'` are present.

### 4. Static global-error disposition

Accept non-hydration of the generated `/_global-error` document as an explicit low-severity residual.

Evidence from the current production artifact:

- `/_global-error` is prerendered.
- Its script elements have no nonce.
- It contains visible error markup, styling, and a native form with a submit/reload button.
- Therefore, nonce CSP will block its scripts, but its error message should still paint and its native reload action remains available without JavaScript.

Forcing this document dynamic is not safely established within the authorized files:

- The global-error document does not inherit the ordinary layout’s dynamic behavior.
- A custom global error must be its own Client Component document.
- No supported request-time nonce path for that static artifact was established in scope.

Falsification conditions:

- Controlled runtime/browser evidence shows the static message or native reload does not function.
- The pinned Next.js version is shown to support a request-time dynamic global-error within the authorized files.
- Future global-error behavior gains a critical JavaScript-only recovery action.

If falsified, expand scope deliberately; do not weaken the ordinary-page CSP as a workaround.

## Exact implementation allowlist

1. [frontend/src/proxy.ts](/home/agile/Projects/libretiles/frontend/src/proxy.ts)
   - Per-request nonce creation
   - Conditional rendered-page request propagation
   - Response header attachment

2. [frontend/src/lib/security-headers.ts](/home/agile/Projects/libretiles/frontend/src/lib/security-headers.ts)
   - Explicit nonce parameters
   - Next-compatible nonce validation
   - `script-src` construction only

3. [frontend/src/lib/security-headers.test.ts](/home/agile/Projects/libretiles/frontend/src/lib/security-headers.test.ts)
   - Supply a fixed test nonce to all existing builder calls
   - Preserve every existing assertion
   - Add policy and invalid-nonce regression tests

4. New `frontend/src/proxy.test.ts`
   - Matcher preservation
   - Rendered-page request propagation
   - API response-only behavior
   - Per-request nonce format and freshness

No other tracked file is authorized.

Explicitly unchanged:

- `style-src`
- Matcher text and exclusions
- Layout, global-error, Next configuration, and API handlers
- Django/backend code
- Dependencies, lockfile, and environment templates
- AI prompts, providers, model routing, and locked types
- Accessibility behavior
- Generated `.next` artifacts

## Regression-test plan

First update the existing tests with:

```ts
const TEST_NONCE = "test-nonce"
```

Pass it to all current builder calls while preserving all nine existing test cases and their assertions.

Add these security-header tests:

1. Production script policy:
   - exact sources are `'self'`, `'nonce-test-nonce'`, and `'strict-dynamic'`;
   - `script-src` lacks `'unsafe-inline'`;
   - `style-src` remains exactly `'self' 'unsafe-inline'`.

2. Development script policy:
   - exact sources additionally include `'unsafe-eval'`;
   - `script-src` still lacks `'unsafe-inline'`.

3. Invalid nonce:
   - whitespace or directive punctuation causes the builder to throw.

Add proxy tests using `next/experimental/testing/server` and direct invocation:

4. Matcher preservation:
   - `/` and `/api/models` match;
   - `/_next/static/*`, `/_next/image`, `/favicon.ico`, and prefetch requests remain excluded.
   - This is a decision-lock test and is expected to pass before implementation.

5. Rendered-page propagation:
   - spy on `NextResponse.next`;
   - assert its request headers contain CSP;
   - assert forwarded CSP equals response CSP;
   - assert it contains a nonce and no script `'unsafe-inline'`;
   - assert no `x-nonce` is introduced.
   - This must fail before implementation.

6. API conditional behavior:
   - `/api/models` still receives response CSP;
   - `NextResponse.next` receives no request override.
   - The nonce assertion must fail before implementation.

7. Fresh nonce:
   - invoke Proxy twice for the same rendered URL;
   - extract both response and forwarded nonce values;
   - require grammar conformance, request/response equality within each invocation, and distinct values between invocations.
   - This must fail before implementation.

Record a causal red phase before changing production code:

```bash
npm test -- src/lib/security-headers.test.ts src/proxy.test.ts
```

After implementation, run:

```bash
npm test -- src/lib/security-headers.test.ts src/proxy.test.ts
npm run typecheck
npm run lint
npm test
npm run build
```

No backend validation is required.

Node tests can prove policy construction, validation, matcher semantics, Proxy call wiring, equality of request/response policy, and sampled nonce uniqueness. They cannot prove that Next’s renderer consumes the nonce, that raw HTML is correctly annotated, that a browser enforces the policy, or that hydration/HMR succeeds.

## Production loopback verification

Use production mode on a non-default port such as `3107`.

Create a temporary directory with `mktemp -d`, start the exact `next start` process directly, capture its PID with `$!`, and install cleanup that kills and waits only for that PID. Never use `pkill` or a broad process pattern.

For two independent `GET http://127.0.0.1:3107/` requests:

- Require HTTP 200 before parsing.
- Capture headers and body separately.
- Require exactly one nonce in `script-src`.
- Require the nonce to match Next’s grammar.
- Require `'strict-dynamic'`.
- Require no script `'unsafe-inline'`.
- Require unchanged style `'unsafe-inline'`.
- Require at least one inline and one external script.
- Require every raw `<script>` element to have a nonce equal to its own response CSP.
- Require the two requests to use different nonces.
- Require neither response body to use the other response’s nonce.

This is the decisive check that the framework discovered Proxy, received the request CSP, extracted the nonce, and annotated its generated HTML.

Probe API response headers without provider calls:

- `/api/models`
- `/api/prompts`
- `GET /api/ai/move`
- `GET /api/ai/judge`

Record status before inspecting headers. The AI endpoints may respond `405`; they must still retain the security headers.

After the build, inspect the generated global-error artifact and record whether it remains static, lacks nonce attributes, and contains the visible error/reload form. Treat that as residual evidence, not as proof of browser usability.

Preserve the first causal failure and stop acceptance if any nonce/header/body invariant fails.

## Audit-diff acceptance

The following response header values must remain unchanged:

```text
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
X-Frame-Options: DENY
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cross-Origin-Opener-Policy: same-origin
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

All CSP directives and ordering remain unchanged except `script-src`, including:

```text
default-src 'self'
style-src 'self' 'unsafe-inline'
img-src 'self' data:
font-src 'self'
frame-ancestors 'none'
base-uri 'self'
form-action 'self'
object-src 'none'
upgrade-insecure-requests
```

For loopback with no overriding environment value, retain the existing localhost HTTP/WebSocket `connect-src` entries.

Canonicalize the nonce to a placeholder, then byte-compare all other header names, values, directives, and ordering against the accepted audit baseline. `Content-Security-Policy` may vary between requests only in its nonce.

Unexpected status changes, missing API security headers, new locale headers such as `Vary: Accept-Language` or `Content-Language`, or any unrelated directive/value change fail acceptance.

`DEFECT_LEDGER.md` and `12_report_01.md` are absent from the canonical repository. The ORCHESTRATOR must inline or otherwise supply the authoritative audit-03 raw baseline before claiming a provenance-backed byte comparison. This does not block the implementation design, but source-derived expectations alone must not be mislabeled as comparison against those missing records.

## Browser evidence ceiling

A browser-capable cooperator must verify both development and production behavior:

- Load representative home, play, settings, and game-related client routes.
- Exercise at least one client-side interaction/navigation.
- Confirm the application is not blank or non-interactive.
- Confirm no legitimate scripts or chunks are blocked by CSP.
- Confirm no nonce-related CSP console violations.
- In development, exercise Fast Refresh and an error-overlay path where feasible.
- Distinguish the accepted static global-error behavior from an ordinary-page nonce mismatch.

Without browser evidence, the correction may pass code, build, and loopback gates, but must not be represented as proving JavaScript execution, browser CSP enforcement, hydration, dynamic imports, HMR, or cross-browser behavior.

Screen-reader evidence is not required for this security-only change.

## Residual risk

Accepted residual: static `/_global-error` does not hydrate under the nonce policy.

- Severity: low
- Confidence: high for the static-artifact fact; browser behavior still requires confirmation
- Preconditions: a root/synthetic fatal error reaches the prerendered global-error document
- Impact: availability/recovery UX only; no identified confidentiality or integrity effect
- Remaining behavior: styled error content and native form submission/reload
- Reversibility: full correction rollback
- Monitoring signal: global-error CSP console blocks, failed reload action, or blank error document

The pre-existing `style-src 'unsafe-inline'` is carried forward under explicit negative authority. No new severity is assigned because the referenced defect ledger is unavailable.

Development-only `'unsafe-eval'` is an environment requirement, not a production residual.

## Rollback

Land the correction as one isolated R10 implementation commit.

If rollout fails, either redeploy known-good commit `f983c3dcce19534466a86b06605e1a02f8bd2bf3` or revert the exact R10 commit under separate execution authority. That rollback restores:

- one-argument security-header builders;
- script `'unsafe-inline'`;
- response-only `NextResponse.next()`;
- removal of the new proxy tests and nonce assertions.

Do not perform an ad hoc partial rollback by removing only `'strict-dynamic'` or reintroducing `'unsafe-inline'` while retaining mixed nonce wiring.

Recognizable partial failures:

- CSP contains a nonce but request propagation failed: response HTML lacks matching attributes, ordinary pages paint server markup but do not hydrate, and the console reports blocked scripts.
- A legitimate chunk lies outside the strict-dynamic trust chain: initial markup may paint, but client navigation/interactions fail.
- Mixed deployed instances: alternating legacy and nonce policies for identical requests.
- Expected global-error residual: styled error content and native reload are present, but JavaScript enhancement is absent.

## Material findings

1. The pinned Next.js version exposes official experimental Proxy test helpers, including matcher evaluation. This materially improves matcher regression coverage.

2. The audit files named in the task are not present in the canonical repository, so their exact raw baseline requires ORCHESTRATOR-provided evidence.

3. The current generated global-error document contains a native form and submit button. This narrows the accepted non-hydration residual because basic reload recovery does not depend on JavaScript.

4. No application-authored inline scripts, custom `next/script` usage, workers, or service workers were found in the reviewed frontend scope, supporting the proposed `'strict-dynamic'` policy.

Not investigated: browser runtime enforcement, production deployment behavior, external reverse-proxy header mutation, cross-browser CSP differences, and controlled fatal-error UX.

Resolved Execution Issues / Near-Misses: none  
Pre-Existing Failure Classification: none

Smallest lawful next step: the ORCHESTRATOR approves or revises this plan, supplies the missing audit-03 raw baseline, and issues a fresh-worker implementation prompt with the exact execution-authority literal.

This planning authority is now expired. No implementation authority remains.  
Logical-whole closure: not-closed
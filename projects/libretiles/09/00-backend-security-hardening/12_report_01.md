### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening
Worker session ordinal: 12
Worker exchange ordinal: 02

**Status: PASS**
**Phase-qualified result: Implementation PASS (NON-INDEPENDENT).** `next@16.3.4` is on `main`, the proxy convention is live, orch-04-F22 has a non-incremental typecheck gate, and a loopback production GET of `/` returned the production security headers. Independent acceptance was not performed.

---

### Continuity anchor

Verified: exchange-01 BLOCKED report for `bump-next-and-migrate-proxy-convention`, `HEAD = 7a197dacb2ba110ff59dea01379ef0e5b53c7efe`, uncommitted candidate retained. Prior authority expired with that report; this prompt is the complete renewal.

Five-line dirty porcelain **matched exactly**:

```text
 M frontend/package-lock.json
 M frontend/package.json
 M frontend/src/lib/security-headers.test.ts
 D frontend/src/middleware.ts
?? frontend/src/proxy.ts
```

`frontend/node_modules/next/package.json` reported `16.3.4`. Remote `main` was still `7a197dacb2ba110ff59dea01379ef0e5b53c7efe`. No discard/stash/reset/clean/checkout.

---

### Start and end commit

- Start: `7a197dacb2ba110ff59dea01379ef0e5b53c7efe`
- End: `b5774b24c6779fd45bd06c4859b2674ec76af17e`

`git diff --stat 7a197dacb2ba110ff59dea01379ef0e5b53c7efe HEAD`:

```text
 frontend/package-lock.json                  | 503 +++++++++++++++++-----------
 frontend/package.json                       |   5 +-
 frontend/src/lib/ai-play-diagnostic.test.ts |   7 +-
 frontend/src/lib/api.test.ts                |   5 +-
 frontend/src/lib/security-headers.test.ts   |  37 ++
 frontend/src/{middleware.ts => proxy.ts}    |   2 +-
 6 files changed, 353 insertions(+), 206 deletions(-)
```

`git diff --name-only`:

```text
frontend/package-lock.json
frontend/package.json
frontend/src/lib/ai-play-diagnostic.test.ts
frontend/src/lib/api.test.ts
frontend/src/lib/security-headers.test.ts
frontend/src/proxy.ts
```

Delete/add evidence: Git recorded `R093 frontend/src/middleware.ts -> frontend/src/proxy.ts`. The only source change is `export function middleware` → `export function proxy`.

All seven allowlisted paths were used. Not touched (and not on this exchange’s list): `frontend/tsconfig.json`, `frontend/next.config.ts`, `frontend/src/lib/security-headers.ts`, `frontend/src/lib/api.ts`, `frontend/src/lib/ws.ts`, README, AGENTS.md.

---

### Repository gate and pre-push gate

Start gate: SHA, `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, `## main...origin/main` with no divergence, remote `main` `7a197dacb2ba110ff59dea01379ef0e5b53c7efe`, porcelain the five expected lines.

Pre-push: `git ls-remote origin refs/heads/main` still `7a197dacb2ba110ff59dea01379ef0e5b53c7efe`. Then `git push origin main` (no flags).

---

### Capability recheck

Material changes since the continuity anchor: two test type fixes, one `package.json` script, then the previously blocked build, HTTP probe, commit, and push. Frontend `npm`/`npx` still observed. Backend pytest still via `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest`. npm registry used for `npm audit` only (no reinstall). Loopback HTTP on 3100 observed. Port 3000 remained occupied by the Cooperator’s `next-server` and was not touched. Secrets not read. **Capability does not grant authority.**

---

### Item A — the two type fixes

`frontend/src/lib/api.test.ts:145` — arity cast through `unknown`:

```ts
const [url, init] = fetchMock.mock.calls[0] as unknown as [
  string,
  RequestInit,
];
```

Assertions unchanged: still `toHaveBeenCalledTimes(1)`, URL contains `/api/auth/logout/`, `POST`, `Authorization: Bearer synthetic-access-token`, body `{ refresh: "synthetic-refresh-token" }`.

`frontend/src/lib/ai-play-diagnostic.test.ts:106` — a same-line `as NodeJS.ProcessEnv` on the non-empty object failed TS2352 (insufficient overlap because `NODE_ENV` is required). The authorized alternative was used: supply what `ProcessEnv` requires.

```ts
expect(liveOptInEnabled({} as NodeJS.ProcessEnv)).toBe(false);
expect(
  liveOptInEnabled({
    NODE_ENV: "test",
    LIBRETILES_AI_PLAY_LIVE: "1",
  }),
).toBe(true);
```

Meaning unchanged: refused without the sentinel, enabled with `LIBRETILES_AI_PLAY_LIVE=1`. `liveOptInEnabled` only reads that sentinel; `NODE_ENV: "test"` is the type requirement, not a behaviour change.

---

### Item B — non-incremental typecheck gate

Exact script line:

```json
"typecheck": "tsc --noEmit --incremental false"
```

`tsconfig.json` was not changed.

**BEFORE the two test fixes** (`npm run typecheck`, exit 2):

```text
src/lib/ai-play-diagnostic.test.ts(106,29): error TS2345: Argument of type '{ LIBRETILES_AI_PLAY_LIVE: string; }' is not assignable to parameter of type 'ProcessEnv'.
  Property 'NODE_ENV' is missing in type '{ LIBRETILES_AI_PLAY_LIVE: string; }' but required in type 'ProcessEnv'.
src/lib/api.test.ts(145,25): error TS2352: Conversion of type '[]' to type '[string, RequestInit]' may be a mistake because neither type sufficiently overlaps with the other. If this was intentional, convert the expression to 'unknown' first.
  Source has 0 element(s) but target requires 2.
```

Exactly those two errors, matching the Orchestrator.

**AFTER:** `npm run typecheck` exit 0, no output.

---

### Corrected Pre-Existing Failure Classification

Exchange 01 classified `api.test.ts:145` as bump-caused via the 16.3.4 `RequestInit` augmentation. That was wrong. The compiler error is an arity mismatch (`[]` vs a 2-tuple) and does not depend on the shape of `RequestInit`. Both errors are pre-existing latent defects that the bump made visible by invalidating the incremental typecheck cache. Evidence agrees with the Orchestrator.

Record 1:

```text
Pre-existing claim: asserted
Comparison baseline commit: 7a197dacb2ba110ff59dea01379ef0e5b53c7efe
Baseline predates: latest-correction-only
Test identity: frontend/src/lib/api.test.ts  "posts the refresh token to /api/auth/logout/ with the access token as bearer"  (created 9ff9ac5)
Failure signature: TS2352 Conversion of type '[]' to type '[string, RequestInit]'; Source has 0 element(s) but target requires 2
Topically related to touched behavior: yes (standing typecheck integrity / orch-04-F22)
Superseded by accepted authority: none
Regression exclusion evidence: assertions unchanged; npx vitest run 326 passed, 3 skipped; npm run typecheck clean after the cast-through-unknown
Closure impact: explicitly-parked as product defects (tests only); they blocked this slice's build evidence until fixed and are now in the same commit
```

Record 2:

```text
Pre-existing claim: asserted
Comparison baseline commit: 7a197dacb2ba110ff59dea01379ef0e5b53c7efe
Baseline predates: latest-correction-only
Test identity: frontend/src/lib/ai-play-diagnostic.test.ts  "treats live mode as refused without the sentinel"  (created b18e50e; line 105 already cast `{}`)
Failure signature: TS2345 Argument of type '{ LIBRETILES_AI_PLAY_LIVE: string; }' is not assignable to ProcessEnv; Property 'NODE_ENV' is missing
Topically related to touched behavior: yes (standing typecheck integrity / orch-04-F22)
Superseded by accepted authority: none
Regression exclusion evidence: refused-without-sentinel and enabled-with-sentinel assertions retained; NODE_ENV is type-only; vitest and typecheck green
Closure impact: explicitly-parked as product defects (tests only); remedied in this commit
```

They do **not** predate the logical whole (`whole-logical-whole` is not claimed). They predate this correction and were hidden at `7a197da` by `incremental: true`.

---

### Evidence (a) — AFTER route table

`npm run build` succeeded. Deprecation warning **gone** (the 16.2.0 baseline had `⚠ The "middleware" file convention is deprecated. Please use "proxy" instead.`).

After route table:

```text
Route (app)
┌ ○ /
├ ○ /_not-found
├ ƒ /api/ai/judge
├ ƒ /api/ai/move
├ ƒ /api/models
├ ƒ /api/prompts
├ ƒ /draw/[id]
├ ƒ /game/[id]
├ ○ /play
├ ○ /settings
└ ƒ /waiting/[id]


ƒ Proxy (Middleware)
```

Proxy line after: `ƒ Proxy (Middleware)`.
Proxy line before: `ƒ Proxy (Middleware)`.

The `(Middleware)` parenthetical did **not** drop. Registration is present; the warning that named the deprecated file convention is gone. Incomplete-build `.next` leftovers were not used as proof.

---

### Evidence (b)

`npx vitest run src/lib/security-headers.test.ts` was already 11 passed in exchange 01; the whole-suite run this exchange was 326 passed / 3 skipped. A green builder test proves `buildSecurityHeaders()` returns the intended map. It does **not** prove Next.js invokes `frontend/src/proxy.ts`.

---

### Evidence (c) — loopback HTTP readback

Port **3100** (3000 occupied by the Cooperator’s next-server; 3100 was free). Bound `127.0.0.1`. Requested only `http://127.0.0.1:3100/`.

```text
First causal operation and error: none. curl exit 0.
Transport status: HTTP/1.1 200 OK
Bounded body capture: /tmp/lt-body.bin (11804 bytes); not parsed for this probe
Parser precondition and result: status 200 known before header parse; header parse succeeded
Exact cleanup paths and owner: next start npx pid 51785, child next-server; Worker
Cleanup outcome: port 3100 free. Killing the npx parent left the child briefly listed, then the child was gone and 3100 was free. Primary HTTP result was not overwritten.
```

Observed headers, verbatim:

| Header | Observed |
|---|---|
| Content-Security-Policy | `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' http://localhost:8000 ws://localhost:8000; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'; upgrade-insecure-requests` |
| X-Content-Type-Options | `nosniff` |
| Referrer-Policy | `strict-origin-when-cross-origin` |
| X-Frame-Options | `DENY` |
| Permissions-Policy | `camera=(), microphone=(), geolocation=()` |
| Cross-Origin-Opener-Policy | `same-origin` |
| Strict-Transport-Security | **present:** `max-age=31536000; includeSubDomains` |

Full received CSP (same string as the table):

```text
default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' http://localhost:8000 ws://localhost:8000; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'; upgrade-insecure-requests
```

Directive-by-directive vs `buildSecurityHeaders({ isDevelopment: false, configuredApiUrl: undefined, requestHostname: "127.0.0.1" })` (loopback → no hostname rewrite; default API `http://localhost:8000`):

| Directive | Builder production | Received | Match |
|---|---|---|---|
| default-src | `'self'` | `'self'` | yes |
| script-src | `'self' 'unsafe-inline'` (no `'unsafe-eval'`) | `'self' 'unsafe-inline'` | yes |
| style-src | `'self' 'unsafe-inline'` | `'self' 'unsafe-inline'` | yes |
| img-src | `'self' data:` | `'self' data:` | yes |
| font-src | `'self'` | `'self'` | yes |
| connect-src | `'self' http://localhost:8000 ws://localhost:8000` | `'self' http://localhost:8000 ws://localhost:8000` | yes |
| frame-ancestors | `'none'` | `'none'` | yes |
| base-uri | `'self'` | `'self'` | yes |
| form-action | `'self'` | `'self'` | yes |
| object-src | `'none'` | `'none'` | yes |
| upgrade-insecure-requests | present | present | yes |

Other required headers and HSTS match `REQUIRED_RESPONSE_HEADERS` plus production `Strict-Transport-Security: max-age=31536000; includeSubDomains`. **No differences.** HSTS and `upgrade-insecure-requests` on plain local HTTP are expected because `next start` sets `NODE_ENV=production`; not a defect.

Authenticated-readback:

```text
Socket filesystem permission: not applicable (loopback TCP)
Transport reachability: HTTP/1.1 200 from 127.0.0.1:3100
Application authentication: unauthenticated
Identity expected on request: no
Authoritative readback mechanism: not-required
Product-supported mechanism: not applicable because the probe is an unauthenticated GET of the root document
Required identity: not required because the root-document header probe needs no login
Observed authentication result: unauthenticated
Authentication evidence source: HTTP/1.1 200 OK with HTML body, no WWW-Authenticate
Authority basis: authoritative because identity is not required for the header-emission probe
Observed status: 200
Status classification: expected-unauthenticated (anonymous root document)
Response parser result: succeeded (status then headers)
HTTP evidence preservation: observed status retained
Identity header spoofing: none
Credential inspection: none
```

---

### Evidence (d)

Unchanged after the two test fixes. `npm audit --json --package-lock-only`: 3 remaining (`@babel/core` low, `brace-expansion` high, `js-yaml` high), all still `dev`-flagged. `next`, `sharp`, and nested `postcss` remain out of their advisory ranges. `picomatch` remains out of the set.

---

### Standing gates

| Gate | Result |
|---|---|
| `npm run typecheck` before fixes | exit 2, exactly the two named errors |
| `npm run typecheck` after fixes | exit 0 |
| `npx vitest run` | **326 passed \| 3 skipped** (24 files passed, 1 skipped file) |
| `npm run lint` | exit 0, no findings |
| `npm run build` | success; Proxy line present; middleware deprecation warning gone |
| backend pytest | `326 passed, 4 skipped in 172.03s (0:02:52)` |

---

### Honest limitations

- No browser observation. The loopback readback proves the headers are emitted; it does not prove a browser enforces the policy without breaking the application. Rendered behaviour stays with Cooperator-executed acceptance.
- The local build is not the deployment artifact, and no CI or provenance attests any artifact (`audit-02-F05`).
- The Next.js advisories were not reproduced; no proof of concept is authorized.
- The AI move stream, the judge route, and websocket play were not exercised end to end.

---

### Residuals

- `orch-01-F18` `script-src 'unsafe-inline'` and `style-src 'unsafe-inline'` unchanged (received CSP still has both).
- `orch-02-D11` HSTS still `max-age=31536000; includeSubDomains` without `preload`.
- `audit-02-F05`, `audit-02-F06` untouched.
- Dev-only remaining advisories as in (d).
- Build route table still labels the file `ƒ Proxy (Middleware)` after a successful `proxy.ts` migration; the deprecation warning is gone. Observation only.
- Independent acceptance of this correction: not performed. Scheduled comprehensive re-audit remains the full-fresh acceptance.

---

### Authorized Git result

One commit `b5774b24c6779fd45bd06c4859b2674ec76af17e` on `main`. Fast-forward push `7a197da..b5774b2`. Public readback: `git ls-remote origin refs/heads/main` = `git rev-parse HEAD` = `b5774b24c6779fd45bd06c4859b2674ec76af17e`. Post-push porcelain empty. `## main...origin/main` with no ahead/behind.

---

### Deviations, risks, missing evidence

- First `as NodeJS.ProcessEnv` on the non-empty live-opt-in object failed; switched to supplying `NODE_ENV: "test"` inside the same item-A grant. Not a second correction of a surviving product assumption.
- Stopping `npx next start` by killing the parent left the child listed for a moment; 3100 was then free. Primary HTTP 200 was kept.
- Missing: browser enforcement of CSP; CI/provenance; independent re-audit.

---

### Out-of-scope observations

- Next 16.3.4 still prints `ƒ Proxy (Middleware)` for a `proxy.ts` file. The parenthetical is display naming, not proof the deprecated filename remains.
- Root response included `x-nextjs-prerender: 1` and `x-nextjs-cache: HIT` and still carried the full security header set, so the proxy matcher covered the prerendered document.

---

### One smallest next step

The Orchestrator issues the comprehensive fresh independent re-audit, INFOSEC 4.11 profile P-10, at `b5774b24c6779fd45bd06c4859b2674ec76af17e`.

Report justification: new-mutation
Logical-whole closure: not-closed
Authority expiry: this exchange's authority expired with this terminal report. Retained context is not a renewal.

Resolved Execution Issues / Near-Misses: (1) `as NodeJS.ProcessEnv` on `{ LIBRETILES_AI_PLAY_LIVE: "1" }` failed TS2352; resolved by supplying required `NODE_ENV` as already authorized in item A. (2) Killing the `npx` parent of `next start` did not immediately clear 3100; the child then exited and the port was free; HTTP 200 remained the primary result.

Pre-Existing Failure Classification: asserted for both type errors, as the two complete records above. Product-header behaviour at `7a197da` is not classified as pre-existing failure; the verification hole (`orch-04-F22`) is.
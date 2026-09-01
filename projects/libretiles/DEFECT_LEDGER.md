# Libre Tiles — defect ledger

**Logical whole `backend-security-hardening` is CLOSED by the Orchestrator at
`19cfec9ed27c57e9499b71c55be6c2fb709b0c63`.** See
`09/00-backend-security-hardening/99_closure.md` for the closure record. This file stays live as the
project's running defect inventory for successor wholes; the closed era's entries are kept as history.

Artifact class: **evidence, not authority.** Produced during the Acceptance phase of
`backend-security-hardening` (Meta 09/00) on 2026-08-31, with the Cooperator performing every
observation in his own browser and the Orchestrator corroborating from the repository and the
development database.

Baseline commit for the original entries: `445029d35474cba9f363734c19cf969226fbe5ed`.
Slice S7a landed at `bbba2e9f26399d57464b4f700cccc4838f2f5bf2`, slice S7b at
`8e82f3bda67751a74746ef15a634514609e3886f`, and the S7b correction at
`9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1`. All three were verified independently by the Orchestrator
rather than accepted from a Worker report. At `9ff9ac5`: mypy 80 files clean, ruff clean,
`manage.py check` clean, pytest `322 passed, 4 skipped`, ten authorized vitest files `199 passed`,
lint exit 0, build succeeds, public readback equal. The Orchestrator re-ran the vitest suite itself and
confirmed the `orch-02-F21` leak line is gone while every benign diagnostic message survives.

Each entry names its **owner**, meaning the whole that should correct it. Nothing here grants
authority to change anything.

`corrected` means an implementation slice landed with pre-fix/post-fix regression evidence.
`verified-closed` requires an independent re-audit (INFOSEC 4.11, profile P-10). **As of session 15,
all 32 corrected findings ARE `verified-closed`** — thirty by `audit-03` at `b5774b2` and two by the
bounded `audit-04` re-audit at `19cfec9`. The earlier line here saying nothing was verified-closed was
stale prose the session-15 re-auditor correctly flagged; it is corrected rather than quietly deleted.

## Status at a glance

| ID | Substance | Status |
|---|---|---|
| orch-01-F20 | Django admin login brute-force brake | corrected at `bbba2e9` (django-axes 8.3.1) |
| acc-01-D05 | login throttle locked the presenter out | corrected at `bbba2e9` (login 60/h, register 20/h) |
| acc-01-D06 | fresh clone cannot boot | corrected at `bbba2e9` |
| acc-01-D07 | documentation drift | corrected at `bbba2e9` |
| orch-02-D08 | AGENTS.md provider list | corrected at `bbba2e9` |
| orch-02-D10 | admin-path refresh blacklisting | corrected at `bbba2e9` (bookkeeping, not a live hole) |
| acc-01-D01 | channel-layer diagnosability | corrected at `8e82f3b` (close code 4503 + ERROR log) |
| acc-01-D02 | provider failures unlogged | corrected at `8e82f3b`, **but see orch-02-F21** |
| acc-01-D03 | registration errors swallowed | corrected at `8e82f3b` |
| acc-01-D04 | raw API error strings | corrected at `8e82f3b`, **but see orch-02-D13** |
| orch-02-D09 | logout call never made | corrected at `8e82f3b` |
| orch-02-D12 | middleware in settings.py, dead cache branch | corrected at `8e82f3b` |
| orch-02-F21 | log redaction is a denylist the project's own fixture defeats | corrected at `9ff9ac5` (value-based redaction + transport message omitted) |
| orch-02-D13 | every 401 says "invalid username or password" | corrected at `9ff9ac5` |
| orch-02-D11 | HSTS without includeSubDomains/preload | open — routed to ui-internationalization |

## Dependency and supply-chain audit — audit-02, session 10, read-only at `9ff9ac5`

Independent P-4 audit (INFOSEC 4.7). The Orchestrator re-ran `npm audit --package-lock-only` and the
OSV.dev queries itself and **independently confirmed all three high findings**. `next` really does
carry 23 advisories with `fixAvailable: next@16.3.4`; Django 5.2.12 really does return 33 OSV records
including `GHSA-mvfq-ggxm-9mc5` / CVE-2026-3902 ASGI header spoofing and `GHSA-mmwr-2jhp-mc7j` /
CVE-2026-4292 `list_editable` privilege abuse; daphne 4.2.1 really does return exactly the two
`CVE-2026-44545` / `CVE-2026-44546` records. `next` latest is 16.3.4, `sharp` latest is 0.35.4.

| ID | Substance | Derived severity | Status |
|---|---|---|---|
| audit-02-F01 | `next@16.2.0`, 23 advisories; reachable App Router + middleware + default Image Optimization | high | corrected at `b5774b2` — next 16.3.4, left the advisory set |
| audit-02-F02 | Django `5.2.12` below patched 5.2.13–5.2.17; ASGI header spoofing reachable through Daphne | high | corrected at `7a197da` — Django 5.2.17, OSV 33 → **0** |
| audit-02-F03 | `daphne==4.2.1` WebSocket memory DoS and handshake header smuggling | high | corrected at `7a197da` — daphne 4.2.3, OSV 4 → **0** |
| audit-02-F04 | `redis` is only a transitive of `channels-redis` while `RedisCache` is a security control | medium | corrected at `7a197da` — declared `redis = "^7.3.0"` direct |
| audit-02-F05 | no CI, SBOM, signing, or provenance attests the deployed frontend artifact | medium | **accepted-residual, Cooperator sign-off 2026-09-01** |
| audit-02-F06 | no frontend equivalent of the Python dev-import guard | info | open — Orchestrator may accept |
| audit-02-F07 | `@babel/core`, `brace-expansion`, `js-yaml`, `picomatch` advisories | rejected-false-positive | closed — lockfile `dev: true`, Orchestrator verified all four |
| audit-02-F08 | Django cache-middleware, GIS, STARTTLS, signed-cookie, GenericInline, SESSION_SAVE_EVERY_REQUEST | rejected-false-positive | closed — features absent, Orchestrator verified |
| audit-02-F09 | PyJWT 2.12.1 cluster needs PyJWKClient or mixed algorithm families | rejected-false-positive | closed |
| audit-02-F10 | Next advisories needing Pages router, Turbopack, Server Actions, rewrites, nonces, Cache Components | rejected-false-positive | closed — no `pages/` directory, Orchestrator verified |
| audit-02-F11 | pytest, pygments, twisted.names | rejected-false-positive | closed |
| audit-02-F12 | nested `postcss@8.4.31` in the production tree, path is attacker-controlled CSS | rejected-false-positive | closed — Orchestrator verified it is `dev`-unset, i.e. production |

Rejecting nine of twelve signals with disproving evidence is the most valuable thing this audit
produced. Scanner severity is not derived severity.

### Dependency corrections — verified by the Orchestrator at `7a197da`

Slice S8a landed `django ^5.2.17` (resolved 5.2.17), `daphne ^4.2.2` (resolved 4.2.3), and
`redis = "^7.3.0"` as a declared direct main-group dependency. The Orchestrator re-queried OSV.dev
itself rather than accepting the report:

    django  5.2.12 -> 5.2.17    OSV total 33 -> 0
    daphne  4.2.1  -> 4.2.3     OSV total  4 -> 0
    redis   7.3.0  (unchanged)  OSV total  0
    django-axes 8.3.1           OSV total  0

All seven named advisory IDs are absent from the new sets. The lock diff moved exactly two package
versions plus `content-hash`; 60 of 62 packages unchanged, none added, none removed. Gates at
`7a197da`, Orchestrator-measured: mypy 80 files clean, ruff clean, `manage.py check` clean, pytest
`326 passed, 4 skipped`.

Worth recording because it is the honest part: the two daphne advisories and the Django ASGI
advisories are **not exercised by any test in this repository**. The websocket tests use an in-memory
channel layer and never touch Daphne's socket layer. The bumps are justified by advisory ranges, not
by behavioural tests, and the Worker said so unprompted rather than implying verification it did not
have.

### orch-04-F22 — `npm run build` can report success while type errors exist

    Classification:  verification-integrity finding (not a product vulnerability)
    Severity:        low for the product, medium for the integrity of this project's evidence
    Confidence:      high
    Evidence class:  established-static plus reproduced-dynamic — the Orchestrator ran
                     `npx tsc --noEmit -p tsconfig.json` against the session-12 working tree and got
                     two errors that `npm run build` had reported as SUCCESS at both `9ff9ac5` and
                     `7a197da`
    Location:        frontend/tsconfig.json `"incremental": true`, plus the absence of any
                     non-incremental typecheck in the standing gates
    Observed:        `src/lib/api.test.ts:145` casts `[]` to `[string, RequestInit]`. That is an ARITY
                     mismatch — zero elements to a two-element tuple — and is independent of the shape
                     of `RequestInit`. `src/lib/ai-play-diagnostic.test.ts:106` passes an object
                     missing `NODE_ENV` where `ProcessEnv` requires it, while line 105 immediately
                     above already applies the `as NodeJS.ProcessEnv` cast the author knew was needed.
                     `api.test.ts` was created at `9ff9ac5`; `ai-play-diagnostic.test.ts` at `b18e50e`.
    Cause:           both errors are PRE-EXISTING. The `next` 16.3.4 bump did not create them; it
                     invalidated the incremental typecheck cache that was hiding them. The session-12
                     Worker classified `api.test.ts` as bump-caused; the Orchestrator corrected that,
                     because the arity comparison cannot depend on a `RequestInit` augmentation.
    Impact:          `npm run build` has been a standing gate for this entire era. Every "build
                     succeeds" claim in it — INCLUDING the Orchestrator's own independent
                     re-measurements at `445029d`, `bbba2e9`, `8e82f3b`, `9ff9ac5`, and `7a197da` —
                     was weaker than stated, because the typecheck could be served partly from cache.
                     No product defect resulted. A verification hole did.
    Exploitability:  not applicable
    Correction:      add a non-incremental typecheck as a separate explicit gate. Do NOT remove
                     `"incremental": true` and do NOT drop test files from `tsconfig.json` `include` —
                     excluding tests would have hidden exactly this drift.
    Regression test: the gate itself; it fails before the two test fixes and passes after
    Owner:           backend-security-hardening, Worker session 12 exchange 02
    Status:          corrected at b5774b2 — NOT verified-closed

### Slice S8b landed at `b5774b2` — and the CSP finally has runtime evidence

`next` 16.2.0 -> **16.3.4**, `eslint-config-next` to match, `frontend/src/middleware.ts` migrated to
`frontend/src/proxy.ts` (Git recorded `R093`, the only source change being
`export function middleware` -> `export function proxy`), two pre-existing test type errors fixed, and
a new `npm run typecheck` gate added as the `orch-04-F22` remedy.

**The Orchestrator independently reproduced the loopback HTTP readback** on port 3200, having verified
the Worker's on 3100, and got byte-identical headers on `GET /` from the production build:

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

This is the FIRST runtime evidence of the enforced CSP in this project's history. Slice 07 built it and
had to state honestly that runtime validation was not performed because Browser MCP is a locked fork. A
production server plus an HTTP client is not a browser, and it closed that gap.

**Verified gap that remains, and it is the most valuable thing for the re-audit:** both readbacks
requested only `/`. Nobody has established that the headers reach `/play`, `/settings`, `/game/[id]`,
`/waiting/[id]`, or the `/api/` routes. The proxy matcher excludes `_next/static`, `_next/image`,
`favicon.ico`, and prefetch-marked requests. If the CSP is absent on the page where a user actually
plays, the control is largely decorative.

Gates at `b5774b2`, all Orchestrator-measured: mypy 80 files clean, ruff clean, `manage.py check`
clean, backend pytest `326 passed, 4 skipped`, `npm run typecheck` exit 0, `npx vitest run`
`326 passed | 3 skipped`, lint exit 0, `npm run build` succeeds with `ƒ Proxy (Middleware)` and **no
middleware deprecation warning**, `npm audit` 7 -> **3** remaining and all three `dev`-flagged.

Two corrections to the Worker's own residual notes: the `ƒ Proxy (Middleware)` parenthetical did NOT
drop after migration — it is display naming, not evidence the deprecated filename survives, and the
Worker said so correctly. And the HSTS residual note conflated two emitters; see the D11 correction
below.

### An operational hazard worth remembering: two convention files crash the dev server

During the blocked window the Cooperator ran `npm run dev` and got, unprompted:

    ▲ Next.js 16.2.0 (webpack)
    ⚠ The "middleware" file convention is deprecated. Please use "proxy" instead.
    Error: Both middleware file "./src/middleware.ts" and proxy file "./src/proxy.ts" are detected.
      Please use "./src/proxy.ts" only.
    ⨯ unhandledRejection

So **Next 16.2.0 already hard-fails if both files exist**, with an unhandled rejection rather than a
graceful message. A proxy migration must therefore be atomic: there is no safe window in which both
files coexist, and a running dev server will break during the transition. The Worker's Git-recorded
rename was the correct shape. Anyone repeating this migration in another project should expect to
restart the dev server, and should not interpret that crash as a product defect.

His dev server was still running the OLD `next-server (v16.2.0)` afterwards, which is why he saw a
16.2.0 banner while `node_modules` already held 16.3.4. It needs a restart to pick up the new runtime.

### Orchestrator process error, recorded because it nearly cost the Cooperator his session

While reproducing the readback the Orchestrator stopped its own server with
`pkill -f "next-server"`. That pattern also matches the Cooperator's own development server on port
3000. It survived, but by luck rather than by design. Kill by exact PID or by a pattern that includes
the port. A broad-pattern kill on a shared machine is a destructive operation dressed as cleanup.

### Session 12 blocked correctly, and what that cost

Session 12 exchange 01 bumped `next` to 16.3.4, migrated `frontend/src/middleware.ts` to
`frontend/src/proxy.ts` (only the export name changed; the Orchestrator read the new file and
confirms it is faithful), deleted the old file, and extended `security-headers.test.ts` — then hit
`npm run build` failing TypeScript on two files OUTSIDE its allowlist and returned
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` with the candidate left uncommitted.

**That was correct behaviour and the blocker was the Orchestrator's allowlist being too narrow.** The
Worker did not breach the allowlist, did not commit a failing tree, preserved the first causal error
with its exact compiler text, and refused to treat a webpack-emitted `.next/server/proxy.js` from an
incomplete build as registration proof. Exchange 02 expands the allowlist by exactly two test files
plus one `package.json` script.

Corroborating Cooperator observation, unprompted: `npm run dev` at the pre-migration state printed
`⚠ The "middleware" file convention is deprecated. Please use "proxy" instead.` — independent
confirmation that the deprecated alias was live in the product he actually runs.

### Two gaps the Orchestrator found in audit-02 itself

    orch-03-G01  `sharp@0.34.5` is flagged high (`<0.35.0`) with `fixAvailable: next@16.3.4`, and the
                 lockfile marks it `optional: true` — NOT `dev`. It is therefore in the production
                 optional tree, reachable through the same default Image Optimization path that
                 audit-02-F01 already establishes. The audit named it only in passing in a verdict
                 table and gave it neither a finding nor a rejection record. It needs no extra work
                 — the `next@16.3.4` bump replaces it — but it must be dispositioned explicitly.
                 CONFIRMED by the Orchestrator: `next@16.3.4` declares
                 `optionalDependencies.sharp: ^0.35.4`, above the `<0.35.0` advisory range. Routed
                 into slice S8b.

    orch-03-G02  `GHSA-8qcx-xf44-272x` / CVE-2026-53878, "Django DomainNameValidator permits newline
                 characters that may enable HTTP header injection", appears in the Django 5.2.12 OSV
                 set and is in NEITHER audit-02-F02 nor the F08 rejection record. Sixteen GHSA-level
                 Django records exist; fifteen are dispositioned. `User.email` is a Django
                 `EmailField`, so an `EmailValidator` path exists in registration, but whether
                 `DomainNameValidator` is reached was not established by the auditor or by the
                 Orchestrator. Correct classification is `not established`, the same bucket as the
                 sqlparse / idna / msgpack / cryptography / pyasn1 / ujson signals. The Django bump
                 covers it either way. CLOSED in fact at `7a197da`: the Orchestrator re-queried OSV
                 for django 5.2.17 and the total record count is 0, so `GHSA-8qcx-xf44-272x` is gone
                 along with the other 32. Reachability was never established and no longer needs to be.

Neither gap changes the correction. Both are completeness defects in the audit report and are routed
to the P-10 re-auditor to disposition.

### Minor Orchestrator observations on audit-02

- The audit reported `poetry check --lock` as "exit 0". It emits two deprecation warnings about
  `[tool.poetry.readme]` and `[tool.poetry.authors]` not being in `[project]`. The lock IS consistent
  with the manifest, so the security conclusion holds, but "exit 0" was imprecise. Not material.
- The audit's own report text contains two truncation artifacts (a mangled line in the F06 record and
  in the Q3 verdict cell). Content is recoverable from context; recorded so a later reader is not
  confused by them.

## Standing Cooperator decisions recorded here

**2026-09-01, route A chosen and version bumps approved.** Presented with the three high `audit-02`
findings and three options, the Cooperator chose route A — fix all of them — and explicitly approved
**version bumps of existing dependencies** in his own words. He also granted full trust and stated he
is not the expert. That grant transfers *confidence*, not *authority*: RF-01 still reserves material
product, cost, irreversibility, and residual-risk decisions to him, and INFOSEC 14 still requires his
explicit sign-off for every residual of severity `medium` or higher. The Orchestrator must keep
presenting those decisions rather than absorbing them, and must keep saying plainly when its own
evidence is thin.

Sequencing that follows from route A, agreed with him: bumps land BEFORE the comprehensive re-audit,
so the re-audit sees the final tree. The `next` bump is deliberately a separate slice from the backend
bumps because `frontend/src/middleware.ts` depends on a deprecated Next 16 file convention and a minor
bump could silently stop emitting the CSP.

    S8a — Worker session 11 — django >=5.2.17, daphne >=4.2.2, redis declared direct
           audit-02-F02, audit-02-F03, audit-02-F04, orch-03-G02
    S8b — Worker session 12 — next 16.2.0 -> 16.3.4, with mandatory proof the security headers survive
           audit-02-F01, orch-03-G01
    P-10 — Worker session 13 — comprehensive fresh independent re-audit of the whole era at the final
           commit, including re-verification of the dependency findings and disposition of both gaps

**Still unsigned, and the Orchestrator must not absorb it:** `audit-02-F05`, no CI / SBOM / signing /
provenance in-tree attesting the artifact a browser executes, derived severity `medium`. It is not
fixable inside this whole — adding CI is a deliberate separate decision about what it gates — so it
needs either an explicit accepted-residual sign-off or its own future whole.


**2026-08-31, providers are frozen.** The Cooperator will run a dedicated logical whole to stop
hardcoding the nine AI providers. Until then no change to any provider list, constant, tier, exact
model tuple, or provider documentation is authorized anywhere. Confirmed by the Cooperator in his own
words: change nothing and revert nothing. The AGENTS.md accuracy fix at `bbba2e9` (`orch-02-D08`)
therefore stands as landed and is neither extended nor reverted. Recorded as locked fork 11 in
PROJECT_CONTEXT.md.

---

## Slice ownership

The era-09 continuation Orchestrator split the handout's single slice S7 into two, because one
allowlist covering a dependency addition, an authentication-backend change, a fail-closed production
guard, four frontend changes, a shell script, and three documents produces a diff that cannot be
reviewed honestly (`.ap/PROMPT_ENGINEERING_PATTERNS.md` P05).

    S7a — Worker session 08 — "brake brute-force logins and share the throttle cache"
           orch-01-F20, acc-01-D05, acc-01-D06, acc-01-D07, orch-02-D08, orch-02-D10
    S7b — Worker session 09 exchange 01 — "make failures legible"
           acc-01-D01, acc-01-D02, acc-01-D03, acc-01-D04, orch-02-D09, orch-02-D12
    S7b correction — Worker session 09 exchange 02 — "hold the log redaction"
           orch-02-F21, orch-02-D13

## Comprehensive fresh independent re-audit — audit-03, session 13, read-only at `b5774b2`

**Verdicts: 30 of 31 corrected findings `verified-closed`. One is `not accepted`.** The re-auditor
recommends this logical whole **does not close** on its evidence, and the Orchestrator agrees.

`audit-01-F03` (no auth throttling) is **not accepted**, because of one new finding.

### audit-03-F01 — unauthenticated DRF throttle identity is attacker-chosen via X-Forwarded-For

    Classification:  security-finding (broken rate-limit identity)
    Severity:        HIGH — the Orchestrator raised this from the re-auditor's `medium`; see below
    Confidence:      high
    Evidence class:  established-static, INDEPENDENTLY CONFIRMED by the Orchestrator from installed
                     source rather than accepted from the report
    Location:        .venv/.../rest_framework/throttling.py BaseThrottle.get_ident; DRF
                     settings.py `'NUM_PROXIES': None`; backend/config/settings.py REST_FRAMEWORK
                     block, which does not set NUM_PROXIES
    Mechanism:       get_ident ends with
                         return ''.join(xff.split()) if xff else remote_addr
                     and that line is reached whenever NUM_PROXIES is None, which is the DRF default.
                     Every distinct `X-Forwarded-For` header value is therefore a fresh throttle
                     bucket, chosen by the caller.
    NOT affected:    django-axes. `ipware` is not installed (`importlib.util.find_spec('ipware')` is
                     None) and `axes/helpers.py` falls back to `request.META["REMOTE_ADDR"]`. So the
                     account lockout is NOT spoofable. The two brakes key on different identities,
                     which is the interaction nobody had audited.
    Impact:          `auth_register` 20/h and `auth_refresh` 60/h have no effective IP brake.
    ORCHESTRATOR SEVERITY CORRECTION, high rather than medium: the re-auditor wrote "login stuffing
                     remains bounded by axes". That is true for ONE username and false for a spray.
                     axes keys on (username, ip_address) with a limit of 8, so an attacker trying one
                     password against a thousand different usernames from a single address produces
                     exactly one failure per pair — axes never fires — while the DRF `auth_login`
                     limit is bypassed by varying XFF. **Credential spray across usernames is
                     therefore unbounded.** That is an authentication-brake bypass on an
                     unauthenticated surface with account takeover as the success condition, which
                     derives to high, not medium. The re-auditor's own reachability, privilege, and
                     blast-radius inputs support it; only the stuffing assumption was too narrow.
    Mitigating today: Django binds 127.0.0.1:8000 locally and the product is not publicly deployed.
                     A reverse proxy that overwrites XFF would also mitigate — but none is configured
                     and this repository contains no deployment configuration.
    CWE mapping:     CWE-307, CWE-290 (client-supplied identity)
    Correction direction: set NUM_PROXIES explicitly so get_ident uses REMOTE_ADDR and agrees with
                     axes. Prefer an env-overridable value defaulting to 0, so a future deployment
                     behind a trusted proxy can set the real count without a code change.
    Known trade-off, and it is honest: with NUM_PROXIES=0 behind a real reverse proxy, every client
                     shares the proxy's address and the IP throttle becomes global. That is
                     conservative and fails safe, rather than spoofable. Configuring a trusted proxy
                     is host territory and belongs to a separate whole.
    Regression test: two unauthenticated register POSTs with the SAME REMOTE_ADDR and DIFFERENT
                     X-Forwarded-For must share one throttle bucket. Must fail before the fix.
    Owner:           backend-security-hardening, slice S9
    Status:          **verified-closed** by audit-04 at 19cfec9

### What the re-audit resolved that the Orchestrator could not

The Orchestrator's own named weak spot — that both CSP readbacks had only ever requested `/` — is
**disproved**. The re-auditor probed `/`, `/play`, `/settings`, `/game/{id}`, `/waiting/{id}`,
`/draw/{id}`, `/api/models`, `/api/prompts`, and `GET /api/ai/move` and got the identical header set on
every one, with `favicon.ico`, `/_next/static/**`, and prefetch-marked requests correctly excluded. The
CSP is not decorative on the page where a user plays. Naming the weak spot in the prompt is what got it
answered.

It also confirmed: the axes lockout cannot be triggered cross-IP against the Cooperator (`ipware`
absent, `REMOTE_ADDR` keying); the login-path `request.body` read does not consume the stream for JSON
and `RequestDataTooBig` propagates to the same HTTP 400 the view would produce; the 4503 log carries no
ticket material and the single-use constraint is intact; and no path exists where a token-bearing 401
should read as invalid credentials.

Two low residuals it added, both accepted by the Orchestrator: the `provider_transport` phase omits the
raw message, and `generate_text` over-redacts model identifiers such that
`nvidia/nemotron-3-super-120b-a12b` becomes `[redacted]`. Diagnostic value is reduced, not destroyed —
phase, status, and error class survive — and the secret property of `orch-02-F21` holds. Also recorded:
`AGENTS.md` "Code quality" still omits `npm run typecheck`.

### Orchestrator bookkeeping error the re-audit caught

`PROJECT_CONTEXT.md` section 1 was stale at the commit it claimed to reconcile: it still described
Next.js 16.2.0, an installed Django of 5.2.12, `frontend/src/middleware.ts`, and `redis` as an
undeclared transitive. The Orchestrator had updated the gate, dependency, and security sections but not
the topology bullets. Corrected. The re-auditor was right to treat that file as evidence rather than
authority, and to say so.

## Slice S9 — throttle identity bound to the socket address, at `19cfec9`

`DJANGO_NUM_PROXIES`, default `0`, validated and fail-closed on a non-integer or negative value, wired
as `REST_FRAMEWORK["NUM_PROXIES"]`. Rates and scope strings untouched. Two new tests, both of which the
Worker recorded as failing before the change.

**The Orchestrator confirmed the fix dynamically**, not from the report — a probe against the real
settings module and the installed DRF:

    api_settings.NUM_PROXIES = 0
    get_ident(REMOTE_ADDR=203.0.113.10, X-Forwarded-For="198.51.100.7, 10.0.0.9") -> 203.0.113.10
    get_ident(REMOTE_ADDR=203.0.113.10, no XFF)                                   -> 203.0.113.10

A spoofed header no longer changes the bucket. Gates at `19cfec9`, Orchestrator-measured: mypy 80 files
clean, ruff clean, `manage.py check` clean, pytest `328 passed, 4 skipped`, frontend typecheck / lint /
build all exit 0 and untouched.

The settings comment is unusually good and worth preserving: it records what `0` means, what a positive
value means, that axes independently keys on `REMOTE_ADDR` because `ipware` is absent, that the two must
agree, and the over-throttling trade-off behind a real proxy. That is the kind of comment that stops a
future reader from "simplifying" a security setting.

## The nginx decision, and a consequence nobody had considered

**Cooperator decision, 2026-09-01, in his own words: Django will be deployed behind nginx, and only
behind nginx.** That is a durable deployment fact with precise consequences, recorded here because the
`admin-provider-model-console` whole will be the first to touch deployment.

    DJANGO_NUM_PROXIES must be 1 in that deployment, not the shipped default of 0.
      With 0 and nginx in front, every client shares nginx's socket address and the IP-keyed throttle
      collapses to one global bucket. Conservative, but one abuser can starve everyone.

    nginx must set the header:
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      That expands to "$http_x_forwarded_for, $remote_addr", so the real peer is appended LAST.
      DRF with NUM_PROXIES=1 computes addrs[-min(1, len(addrs))] = addrs[-1] = the appended real peer.
      That composition is therefore NOT spoofable.

    The dangerous misconfiguration is NUM_PROXIES=1 with nginx NOT setting the header at all: the last
      element of a purely client-supplied X-Forwarded-For is then attacker-chosen and the bypass
      returns silently.

### orch-05-D14 — behind nginx, an axes lockout becomes a targeted denial of service

    Classification:  security-finding, FORWARD-LOOKING — not reachable today
    Severity:        medium in the nginx topology; not-applicable at present
    Confidence:      medium — the mechanism is established-static; the deployed consequence is inferred
    Evidence class:  established-static for the code path, inferred for the deployment consequence
    Location:        .venv/.../axes/helpers.py get_client_ip_address; backend/config/settings.py axes
                     block (AXES_LOCKOUT_PARAMETERS = [["username", "ip_address"]])
    Mechanism:       axes consults its AXES_IPWARE_* settings ONLY when IPWARE_INSTALLED is true.
                     `import ipware.ip` fails in this virtualenv, so axes falls back unconditionally to
                     request.META["REMOTE_ADDR"]. Behind nginx that is nginx's own address for every
                     request, so the lockout key (username, ip_address) degenerates to effectively
                     (username, nginx) — one global bucket per account.
    Impact:          any attacker anywhere could deliberately fail 8 logins against a named account and
                     lock it for EVERY legitimate client for 30 minutes. `AXES_RESET_COOL_OFF_ON_FAILURE
                     _DURING_LOCKOUT` defaults to true, so continued failures extend the lockout
                     indefinitely. The control designed to protect an account becomes a way to deny it.
    Why not reachable today: Django binds 127.0.0.1:8000 on the Cooperator's machine, no nginx
                     configuration exists in this repository, and the product is not publicly deployed.
    Note:            `AXES_LOCKOUT_PARAMETERS = [["username", "ip_address"]]` was chosen in S7a
                     specifically to avoid locking everyone behind one NAT. Behind nginx that protection
                     silently evaporates, because every request appears to come from one address. The
                     mitigation that made the direct-exposure case safe is the same one that fails in the
                     proxied case.
    Correction direction: install the `django-axes[ipware]` extra — the pre-authorized fallback already
                     written into the S7a prompt and not needed then — and configure the axes
                     trusted-proxy count alongside DJANGO_NUM_PROXIES so both brakes see the real client.
                     Alternatively reconsider the lockout parameters for a proxied topology.
    Regression test: with a simulated proxied request, the axes client IP must be the real peer and not
                     the proxy; and two different real peers must not share a lockout bucket.
    Owner:           routed to the deployment whole (`admin-provider-model-console` is the first to
                     touch deployment); NOT this whole
    Status:          open — routed to the deployment whole; INDEPENDENTLY CONFIRMED as audit-04-F01
    Cooperator sign-off: required before public deployment, because it is `medium` in that topology

The session-15 bounded re-auditor is asked to ATTACK this reasoning rather than confirm it.

## Bounded re-audit audit-04, session 15, read-only at `19cfec9`

**Both in-scope findings `verified-closed`.**

    audit-01-F03  bounded per client   verified-closed   reproduced-dynamic + established-static
    audit-03-F01  caller cannot choose the bucket identity   verified-closed   same

The re-auditor tried to mint a fresh identity and could not: distinct single-element XFF, comma-separated
spoofed XFF, `Remote-Addr` as an HTTP header, `X-Real-IP`, and the anonymous `ScopedRateThrottle` cache
key, which resolved to `throttle_auth_register_203.0.113.10`. It also swept the whole class rather than
the one instance (Q2) and found **no** other place in project code that trusts a client-supplied address
or host: no `SECURE_PROXY_SSL_HEADER`, no `USE_X_FORWARDED_HOST`, no `USE_X_FORWARDED_PORT`, no custom
throttle or permission class, and `backend/config/middleware.py:83` uses `REMOTE_ADDR` (socket) rather
than a header.

It confirmed all four parts of the Orchestrator's nginx reasoning, including the index arithmetic
`addrs[-min(1, len(addrs))] == addrs[-1]`, and added a dual the Orchestrator had not stated: a
`NUM_PROXIES` value GREATER than the real hop count reads a leftward element, i.e. an attacker-chosen
one. Too high is as dangerous as too low.

### ORCHESTRATOR ERROR, corrected — and the correction is worse than "incomplete"

The Orchestrator wrote that `orch-05-D14`'s remedy was to "install the `django-axes[ipware]` extra and
configure the trusted-proxy count". The re-auditor called that understated. Verifying the installed
`axes/conf.py` myself confirms it is worse than understated: **following that remedy with package
defaults would change nothing, and one plausible half-step would make things actively worse.**

    AXES_IPWARE_META_PRECEDENCE_ORDER  default ("REMOTE_ADDR",)      <- XFF is not even consulted
    AXES_IPWARE_PROXY_ORDER            default "left-most"
    AXES_IPWARE_PROXY_COUNT            default None
    AXES_RESET_COOL_OFF_ON_FAILURE_DURING_LOCKOUT  default True

Installing the extra and stopping there leaves axes reading `REMOTE_ADDR` only, so nothing improves.
Adding `HTTP_X_FORWARDED_FOR` to the precedence order WITHOUT also setting `AXES_IPWARE_PROXY_COUNT`
leaves `left-most` in force, and the left-most element of `$proxy_add_x_forwarded_for` is the part the
CLIENT supplied. That would hand axes an attacker-chosen identity — converting a denial-of-service
weakness into a full lockout-and-throttle bypass. **The half-measure is more dangerous than the current
state.** Any correction must set the precedence order, the proxy order (right-most / last element, to
match nginx's append), and the proxy count together, and must be tested as a unit.

This is the fifth time in this project that a Worker has corrected the Orchestrator with evidence, and
the most consequential. Recorded in full rather than smoothed over.

### Three smaller precision corrections from the same report

1. The Orchestrator's prompt said "Django binds `127.0.0.1:8000`". The live listener does — verified with
   `ss` — but `README.md:56`, `README.md:180`, and `AGENTS.md:32` all document
   `runserver 0.0.0.0:8000`, which binds every interface. So "not reachable today" is true of the
   Cooperator's current process and NOT true of the documented start command on a LAN. The distinction
   matters for any reachability claim and belongs in the deployment handout.
2. The re-auditor named real gaps in the two new tests, and they are fair: they do not assert
   `api_settings.NUM_PROXIES == 0`, do not cover a comma-separated nginx-append XFF, do not vary XFF on
   the refresh endpoint, and would still pass if some other CONSTANT identity replaced `REMOTE_ADDR`
   (which would over-throttle, i.e. fail safe). They do lock the original finding for register and login,
   which is what was required. Accepted as a low residual rather than corrected, because the identity
   probe plus the observed cache key close the gap in practice at this commit.
3. It did not re-run the section-2 gates and said so instead of implying it had. Correct behaviour.

## Residual-Risk Decision records

```text
Finding ID: audit-04-F01 / orch-05-D14
Decision: accepted-residual, ROUTED
Severity: medium in the nginx topology; not applicable on the current direct-socket deployment
Approver: Cooperator
Regression test: required in the deployment whole — a simulated proxied request must yield the real
  peer as the axes client IP, and two different real peers must not share a lockout bucket
Rationale: behind nginx, axes keys on REMOTE_ADDR (nginx's address) for every request because ipware is
  absent, so the lockout key (username, ip_address) collapses to one global bucket per account and an
  account lockout becomes a targeted denial of service. Not reachable at 19cfec9: no nginx config exists
  in this repository and the product is not publicly deployed. The Cooperator was shown the mechanism,
  the irony that the S7a NAT-safety choice is what fails in a proxied topology, and the trap that the
  obvious remedy makes things worse, and on 2026-09-01 accepted it as a residual routed into the
  deployment whole with sign-off for the deployed case deferred to that whole.
Recorded in: this ledger, PROJECT_CONTEXT.md, and 09/00-backend-security-hardening/99_closure.md
```

```text
Finding ID: audit-02-F05
Decision: accepted-residual
Severity: medium
Approver: Cooperator
Regression test: not applicable — the finding is the absence of a process control, not a code defect
Rationale: no CI, SBOM, signing, or provenance exists in-tree to attest the artifact a browser
  executes; no .github directory exists at all. Adding CI is a deliberate separate decision about what
  it should gate, and is not fixable inside this logical whole without expanding its objective. The
  Cooperator was presented with the finding, its derived severity, and the alternative of routing it to
  its own future whole, and chose to accept it as a residual on 2026-09-01 in his own words.
Recorded in: this ledger and the closure record for backend-security-hardening
```

Four earlier residuals of severity `medium` or higher already carry Cooperator sign-off and must not be
lost at closure: `orch-01-F18` `script-src 'unsafe-inline'` in production (`medium`, nonce upgrade
routed to the UX/i18n whole), `audit-01-F13` duplicate-username disclosure (`low`), `audit-01-F09`
ticket in the query string (`low`), and `style-src 'unsafe-inline'` (`low`).

## New logical whole `multilingual-tile-token-foundation` (Meta 11/01), opened 2026-09-01

Baseline `1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd`. Objective: atomic variable-length tile tokens, with
Hungarian as the forcing function and Czech and Polish as pure data variants. Opened as a SEPARATE
logical whole from `ui-internationalization` under RF-19, because the objective materially changed:
the UI locale framework already works and needs no planning, while the engine change spans nine layers,
a database migration, and four standing Cooperator locks.

Meta directory: `11/01-multilingual-tile-token-foundation/`. It is `01` rather than `00` because
`11/00-admin-provider-model-console/` was created earlier. Meta's `<logical-whole-sequence>` is an
archive-ordering key assigned at creation time, not a priority ranking; execution order is
`11/01` first, then `11/00`, and that is recorded here so the mismatch is not read as an error.

### ORCHESTRATOR ERROR at Worker session 01 exchange 01 — the planning prompt was structurally incomplete

    Classification:  protocol defect in an Orchestrator-issued prompt
    Severity:        blocking; no product impact
    Found by:        the Worker, which returned planning-BLOCKED rather than improvising
    Verified by:     the Orchestrator, reading .ap/PROMPT_CONTRACTS.md:89-101 after the report

`PROMPT_CONTRACTS.md` "Planning Record" requires SIX fields in every initial
implementation-planning prompt, and the issued prompt carried NONE of them:

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

The prompt DID carry all nine `Plan-to-Execution Gate` fields correctly, which is why the omission was
not obvious from the Orchestrator's side. Cause: the Orchestrator read the "Common Worker Task Fields"
table and the "Worker Report Header" but never opened the "Planning Record" section at line 89, because
it had originally been preparing an implementation prompt and switched to a planning prompt without
returning to the contract. AP is explicit that `PROMPT_CONTRACTS.md` owns exact field spellings; the
Orchestrator instead approximated the shape from `AP_ORCHESTRATOR.md` prose.

**This is the seventh time in this project that someone other than the Orchestrator was right about a
claim the Orchestrator was confident in, and the fifth time it was a Worker.** The report is a model of
the behaviour this project wants: it ran only the identity gates, mutated nothing, touched none of the
five untracked flag images it was told to leave alone, preserved all four locks, named the exact missing
fields, quoted the exact contract location, explicitly declined to infer the fields locally because that
"would manufacture authority", and recommended the correct remedy — a contiguous current-session
exchange 02 that is still `Planning cycle: initial`, because a BLOCKED exchange that produced no plan
did not consume the one authorized planning cycle.

Disposition: reissued as Worker session 01 **exchange 02**, `current-worker-session` with a continuity
anchor and complete authority renewal. The session is healthy — it performed only read-only gates — and
planning requires no independence, so AP prefers current-session renewal over a fresh session.

### Cooperator decision, 2026-09-01: in-progress games are expendable

Asked whether existing in-progress game sessions must survive the persistence migration, he answered
`obetovatelne - vsetky rozohrate vymazat predsa, su to len testovacie hry`.

This materially simplifies the plan and removes the largest risk in the risk register:

```text
BEFORE  a deterministic legacy conversion of board_state, bag_tiles, racks, move history, and
        save-state rows, plus rollback semantics for partially converted live games
AFTER   the migration MAY delete existing GameSession rows and their dependents. No legacy
        board/bag/rack decoding path is required. The representation change becomes forward-only.
```

Constraints that survive the simplification, and the plan must still honour them:

```text
- accounts.User rows, credentials, password_changed_at, and JWT blacklist state are NOT game state
  and must NOT be deleted
- catalog rows (AIModel, AIPrompt) are NOT game state and must NOT be deleted
- ConsumedWsTicket rows are transient and may be cleared
- the migration must be explicit and reviewable about exactly which tables it empties, must not use a
  blanket flush, and must be reversible in the sense that re-running it on an empty database is a no-op
- deleting rows is a destructive operation on the Cooperator's development database. It has his
  explicit authorization for THIS purpose only, and the implementation prompt must say so in terms.
  It does NOT authorize touching any other table.
```

### Flag assets normalized by the Orchestrator, 2026-09-01

At his instruction (`B11-3 normalizuj`). Fit-inside-the-box with transparent padding: no distortion and
no cropping, so the US/UK star and stripe detail and the Hungarian 2:1 ratio all survive intact.

```text
en.jpeg   500x300   43489 B  ->  en.png  48x32 (image 48x29)  2572 B
sk.jpeg  2048x1367  52961 B  ->  sk.png  48x32 (image 48x32)  1326 B
cz.jpeg  1280x720   31985 B  ->  cs.png  48x32 (image 48x27)   924 B
hu.jpeg  1479x995   19185 B  ->  hu.png  48x32 (image 48x32)   242 B
pl.jpeg   474x296    4319 B  ->  pl.png  48x32 (image 48x30)   166 B
                    -------                                   -----
                    191939 B  total                            5230 B  total
```

48x32 is a 2x asset for a 24x16 CSS rendering, so it stays crisp on a retina display. `cz.jpeg` becomes
`cs.png`: the flag is a country symbol but the selector chooses a LANGUAGE, and the Czech language code
is `cs`. Naming the asset by locale removes a country-to-language lookup table that would otherwise
exist purely to hide the mismatch. The five source JPEGs remain untracked and are not committed.



Gathered by the Orchestrator at `1b7b05d0de854d7936c5fcd2b0d55a5cc5d14cfd` while reviewing a
Cooperator-supplied ChatGPT analysis and its draft planning prompt. All of it is read-only,
`established-static` unless marked otherwise, and none of it authorizes implementation.

### The Cooperator's supplied variant JSONs — arithmetically validated

Computed rather than trusted, from the exact JSON text he supplied:

```text
variant     tiles  kinds  nominal points  multi-char tiles                       loader accepts today
czech        100    40         205        none                                    100  (drops 0)
polish       100    33         190        none                                    100  (drops 0)
hungarian    100    39         235        SZ GY NY CS LY ZS TY  (9 physical tiles)  91  (DROPS 9)
slovak       100    42         267        none                                    100  (existing)
```

All three are 100 tiles with exactly 2 blanks, no duplicate letter entries, NFC-clean, uppercase, and
every non-blank token satisfies `str.isalpha()`. The ChatGPT claim that today's loader would take only
**91 of 100** Hungarian tiles is **exactly right** — the nine dropped are SZ×2, GY×2, NY×1, CS×1, LY×1,
ZS×1, TY×1.

### Verified confirmations of the ChatGPT analysis

```text
backend/gamecore/variant_store.py:177   if letter != "?" and len(letter) != 1: continue     CONFIRMED
backend/gamecore/variant_store.py:193   letters sorted by lt.letter, declared order lost    CONFIRMED
backend/game/models.py:26               board_state = JSONField                             CONFIRMED
backend/game/models.py:32               bag_tiles = TextField(default="")                   CONFIRMED
backend/game/services.py:272            grid.append("".join(row_chars))                     CONFIRMED
backend/game/services.py:279,485        session.bag_tiles = "".join(bag.tiles)              CONFIRMED
backend/game/services.py:248            tiles=list(session.bag_tiles)  <- CHARACTER split   CONFIRMED
backend/gamecore/state.py:44,49,111,120,121  save-state joins grid rows, racks, and bag     CONFIRMED
backend/game/serializers.py:248         exchange child=CharField(max_length=1)              CONFIRMED
backend/game/serializers.py:269-277     _nfc_uppercase_letter requires len(nfc)==1          CONFIRMED
frontend/src/app/api/ai/move/route.ts:123,127  Zod .length(1)                               CONFIRMED
frontend/src/app/api/ai/move/route.ts:329      /^[\p{L}?]$/u                                CONFIRMED
frontend/src/app/api/ai/move/route.ts:334,341  blankAs single code point                    CONFIRMED
frontend/src/lib/types.ts:48            board: string[]                                     CONFIRMED
frontend/src/hooks/useGameStore.ts      SelectedVariantSlug = "english" | "slovak"           CONFIRMED
```

### Three precision corrections to the supplied analysis

```text
1  `isalpha()` is NOT what blocks Hungarian. "SZ".isalpha() is True. The blocker is the
   `len(nfc) == 1` half of the same condition. `isalpha()` only blocks a token containing
   punctuation, i.e. the Catalan L·L case. The distinction matters because a remedy aimed at
   `isalpha()` would fix nothing for Hungarian.
2  The analysis prescribes `poetry run ruff / mypy / pytest` as the validation route. That route is
   NOT usable inside a Worker boundary in this project — see PROJECT_CONTEXT.md section 4. Any prompt
   built on it would fail at the first gate.
3  The analysis directs the planner at `frontend/src/lib/prompts.ts` and the AI move route without
   stating that the MOVE CORE prompt carries a pinned SHA-256 and `MOVE_PROMPT_VERSION`
   `pfr-s2-core-1`, both LOCKED by Cooperator decision (locked fork 2), and that the nine providers
   are frozen (locked fork 11). A plan produced without those constraints could violate two standing
   Cooperator decisions.
```

### Two things the supplied analysis MISSED

#### uii-01-F06 — the bag's remaining count is a string length

    Classification:  latent correctness defect, NOT reachable today
    Severity:        low today; high the moment a multi-character tile exists
    Confidence:      high
    Evidence class:  established-static
    Location:        backend/game/services.py:372 and :558 — `bag_remaining = len(session.bag_tiles)`
    Observed:        `bag_tiles` is a TextField holding the joined tile string. Its LENGTH is reported
                     to the client and to the AI context as the number of tiles left in the bag.
    Impact:          with a Hungarian bag, one `SZ` tile would be counted as TWO remaining tiles. The
                     bag would appear to hold up to 109 tiles for a 100-tile set, endgame detection
                     reads the count, and `BAG_EMPTY_AND_PLAYER_OUT` is a real end reason.
    Why it was missed by the supplied analysis: it named the join and the character split on the same
                     field but not the count derived from it. Three distinct defects live in one field.
    Owner:           the multilingual tile-token whole
    Status:          open

#### uii-01-F07 — every accented Slovak tile loses the starting draw, today, in production

    Classification:  product-defect (game rules), PRE-EXISTING and REACHABLE NOW
    Severity:        low — it only decides who opens the board — but it is a live rules defect in a
                     shipped variant, not a future hypothetical
    Confidence:      high
    Evidence class:  reproduced-dynamic — the Orchestrator loaded the real Slovak variant through the
                     real loader and evaluated the real comparison expression
    Location:        backend/game/services.py:453-464 `_perform_starting_draw`, which decides
                     `slot0_first` with `slot0_value <= slot1_value` on the raw tile strings
    Measured:        ('Á' <= 'Z') is False        code points 193 vs 90
                     ('Ä' <= 'B') is False        196 vs 66
                     ('Č' <= 'D') is False        268 vs 68
                     ('Ž' <= 'A') is False        381 vs 65
                     ('Ó' <= 'P') is False        211 vs 80
    Consequence:     the seventeen single-copy Slovak diacritic tiles all sort AFTER Z under
                     code-point comparison, so a player who draws `Á` is treated as further from A
                     than a player who draws `Z`. In the Slovak alphabet `Á` is SECOND.
    Corroborating:   the same root cause makes `variant_store.py:193` produce the playable-letter
                     order `A B C … Z Á Ä É Í Ó Ô Ú Ý Č Ď Ĺ Ľ Ň Ŕ Š Ť Ž`, which is what
                     `services.py:167` publishes as `"alphabet"` to the AI context and the blank
                     picker. Accented letters appear after Z there too.
    Why it matters for the plan: it proves the "explicit variant alphabet order" requirement from the
                     CURRENT product rather than from a Hungarian hypothesis, and it means the fix has
                     value even before any new variant ships. Naive code-point collation happens to
                     order the Hungarian digraphs correctly (`SZ` < `T`, `CS` < `D`, `ZS` > `Z`) while
                     being wrong for every accented vowel in Slovak, Czech, Polish, and Hungarian.
    Correction direction: variant-declared tile order, honoured by the loader and by the starting
                     draw. Do not reach for `locale`-based collation; the order is a game rule and
                     belongs in the variant asset.
    Regression test: in Slovak, `Á` must beat `Z` in the starting draw. Must fail before the fix.
    Owner:           the multilingual tile-token whole
    Status:          open

### Flag assets the Cooperator added, untracked at `1b7b05d`

```text
frontend/public/en.jpeg    500x300    43489 B
frontend/public/sk.jpeg   2048x1367   52961 B
frontend/public/cz.jpeg   1280x720    31985 B
frontend/public/hu.jpeg   1479x995    19185 B
frontend/public/pl.jpeg    474x296     4319 B
```

Deliberately NOT committed by the Orchestrator. They are five different aspect ratios and up to
2048 px wide for what will render at roughly 20 px, so they must be normalised to one small identical
size before they enter the tree. `sk.jpeg` alone is 53 KB for a flag. Note also the filename is
`cz.jpeg` while the Czech variant's `language_code` is `cs`; that mismatch must be resolved
deliberately rather than papered over with a lookup table.



## Era 10 — `ui-internationalization`, opened 2026-09-01

Baseline `19cfec9ed27c57e9499b71c55be6c2fb709b0c63`. Nothing below has been corrected yet. No Worker has
been issued. Full restoration evidence, including the exact probe commands and their output, is in
`10/00-ui-internationalization/90_orchestrator-restoration.md`.

### Disposition changes to routed residuals, by Cooperator decision 2026-09-01

```text
orch-01-F18  script-src 'unsafe-inline'          accepted-residual (medium, signed off)
             -> TO BE CORRECTED in ui-internationalization as a nonce CSP.
             The existing sign-off is NOT discarded; it remains the record of why the residual was
             lawful between 445029d and this whole.
             ORCHESTRATOR SELF-CORRECTION, from the measured `npm run build` route table at 19cfec9:
             the Orchestrator told the Cooperator that all SIX page files under frontend/src/app are
             prerendered as static shells, so a nonce would make six routes dynamic. The "use client"
             half is right; the prerendering half was wrong. Measured:
                 ○ /            ○ /_not-found      ○ /play        ○ /settings     <- static
                 ƒ /draw/[id]   ƒ /game/[id]       ƒ /waiting/[id]                <- ALREADY dynamic
                 ƒ /api/ai/judge  ƒ /api/ai/move   ƒ /api/models  ƒ /api/prompts  <- ALREADY dynamic
             So the cost is three product routes, not six — precisely what the orch-01-F18 residual
             record already said ("a nonce CSP needs dynamic rendering on /, /play, /settings"). The
             residual was more precise than the Orchestrator restating it. Decision unchanged; the
             Cooperator was told the cost is smaller than presented.
             style-src 'unsafe-inline' REMAINS an accepted low residual (Framer Motion inline styles).

orch-02-D11  Django HSTS without includeSubDomains or preload   accepted-residual (low, routed)
             -> includeSubDomains TO BE ADDED in ui-internationalization.
             -> preload REMAINS a separate explicit future Cooperator decision, because submission to
                the browser preload list is close to irreversible. Not accepted, not rejected: deferred
                with a named owner decision.
             Precision retained: two HSTS emitters exist; this is Django's only. The Next.js proxy at
             frontend/src/lib/security-headers.ts:109-112 already emits includeSubDomains in production.

audit-01-F06 public prompt text + swallow-to-HTTP-200 in the catalog proxies   accepted-residual (low)
             -> the swallow half is CONFIRMED and in scope for this whole.
```

### audit-01-F06, swallow half — confirmed at `19cfec9`, both files

    Classification:  product-defect (diagnosability) with a minor disclosure aspect
    Severity:        low
    Confidence:      high
    Evidence class:  established-static — the Orchestrator read both files in full
    Location:        frontend/src/app/api/models/route.ts:19-21 and :25-27
                     frontend/src/app/api/prompts/route.ts:11-13 and :17-19
    Observed:        both routes return NextResponse.json([], { status: 200 }) on BOTH the `!res.ok`
                     branch and the bare `catch` branch. A caller therefore cannot distinguish "the
                     catalog is legitimately empty" from "Django is unreachable" from "Django returned
                     500". The frontend renders the same string in both cases:
                     "The rival catalog is empty. Seed the free catalog to play AI matches."
                     (app/play/page.tsx:27-28, app/settings/page.tsx:55-56)
    Impact:          a backend outage presents to the user, and to the Cooperator during a demo, as
                     "you have not seeded the catalog". That is the acc-01-D02 shape again: a real
                     failure rendered as a configuration mistake.
    Note:            models/route.ts uses `next: { revalidate: 60 }` while prompts/route.ts uses
                     `cache: "no-store"`. That asymmetry is undocumented and means a 60-second stale
                     empty catalog can outlive a recovered backend.
    Correction direction: distinguish the three cases in the response so the UI can say "the catalog is
                     empty" versus "the catalog is temporarily unavailable". Do not leak Django's
                     status text or body to the browser.
    Regression test: a stubbed backend failure must NOT produce the empty-catalog wording
    Owner:           ui-internationalization
    Status:          open

### uii-01-F01 — the 429 wait time is parsed out of an English Django string

    Classification:  product-defect (localization fragility), NOT a security finding
    Severity:        low
    Confidence:      high
    Evidence class:  established-static for the coupling, reproduced-dynamic for the current Slovak text
    Location:        frontend/src/lib/api.ts:122-132 parseRetryAfterSeconds, consumed by
                     formatThrottleWait at :134-143 and humanMessageForStatus case 429 at :164-165
    Mechanism:       the wait time is extracted with /(\d+)\s+seconds/i against Django's 429 response
                     body. That depends on the literal English word "seconds" surviving in the response.
    Measured:        with USE_I18N=True and LANGUAGE_CODE="sk", DRF's Throttled detail becomes
                     "Požiadavok bol obmedzený, z dôvodu prekročenia limitu. Expected available in
                     3274 seconds." — the FIRST sentence is translated by the bundled sk catalog and
                     the second is not. The regex therefore still matches today, by luck rather than
                     by design.
    Impact if it changes: formatThrottleWait silently degrades from "Too many requests. Try again in
                     about 55 minutes." to the generic "Too many requests. Please wait and try again."
                     No test would catch it, and this is exactly the acc-01-D04 message quality that
                     the security era existed to fix.
    Why it matters now: decision 2 of this whole enables Django USE_I18N. The coupling moves from
                     dormant to live.
    Correction direction: read the numeric `Retry-After` response header, which DRF's exception_handler
                     sets from exc.wait and which is locale-independent. Keep the regex only as a
                     fallback.
    Regression test: a 429 whose body has NO English "seconds" but DOES carry Retry-After must still
                     render a human wait time. Must fail before the fix.
    Owner:           ui-internationalization
    Status:          open

### uii-01-F02 — the product has no aria-label, no role, no alt, and no explicit tab order

    Classification:  product-defect (accessibility), pre-existing
    Severity:        low technically, medium for interview presentability
    Confidence:      high
    Evidence class:  established-static, measured with a WIDENED pattern rather than a narrow one
    Method:          grep -rnoE "aria-[a-zA-Z]+|role=|alt=|title=|placeholder=|sr-only|screen-?reader|tabIndex"
                     over frontend/src --include=*.tsx --include=*.ts, then counted by attribute.
                     Result, complete:
                         title=        10
                         placeholder=   6
                         aria-hidden    4
                         aria-pressed   3
                         aria-live      2
                         aria-current   1
                     ZERO occurrences of aria-label, role=, alt=, tabIndex, sr-only, or screen-reader.
                     The exact patterns that matched nothing are named above; this is not a narrow
                     negative grep.
    Impact:          icon-only controls have no accessible name. The header cluster in ScorePanel.tsx
                     is largely icon buttons with a custom IconTooltip, and a tooltip is not an
                     accessible name. "Accessibility basics: keyboard reachability, focus states, modal
                     focus trap and ESC" is already an open manual-acceptance item below.
    Relevance to i18n: aria-labels are translatable strings. They do not exist yet, so this whole is the
                     cheapest moment in the project's life to add them — the alternative is adding them
                     later and translating them twice.
    Correction direction: give every icon-only control an accessible name; add role and focus management
                     to the modals. Keep the added names inside the same dictionary as the visible copy.
    Regression test: a test asserting an accessible name for each icon-only control in ScorePanel and
                     GameControls
    Owner:           ui-internationalization (UX fine-tuning)
    Status:          open

### uii-01-F03 — dates are formatted with a hardcoded "en-US" locale

    Classification:  product-defect (localization)
    Severity:        low
    Confidence:      high
    Evidence class:  established-static
    Location:        frontend/src/components/game/GameHistoryPanel.tsx:73
                     frontend/src/components/game/ProfileModal.tsx:22
    Observed:        both call Intl.DateTimeFormat("en-US", ...). These are the only two Intl. call
                     sites in frontend/src; toLocaleString, toLocaleDateString, and toLocaleTimeString
                     return nothing.
    Impact:          a Slovak interface would still render American dates ("September 1" rather than
                     "1. septembra"), which is the visible half-localized tell.
    Correction direction: take the active UI locale. Note that a Slovak month name is genitive in a
                     date ("1. septembra", not "1. september"), so a naive month-name switch reads
                     wrong to a Slovak speaker; prefer Intl with the sk locale over hand-built strings.
    Regression test: with the sk locale active, neither call site emits an English month name
    Owner:           ui-internationalization
    Status:          open

### uii-01-F04 — the server renders the body in English while `<html lang>` says `sk`

    Classification:  product-defect (localization correctness + accessibility), and an
                     ORCHESTRATOR DESIGN DEFECT rather than a Worker execution defect
    Severity:        medium for interview presentability, low functionally
    Confidence:      high for the mechanism
    Evidence class:  reproduced-dynamic for the server output; established-static for the client
                     half; the React console error itself is `not demonstrated`
    Found by:        the Orchestrator, at a5aff12, while re-verifying Worker session 01's report.
                     The Worker did NOT report it and no gate could have caught it.
    Location:        frontend/src/app/layout.tsx readUiLocale (server, reads the cookie)
                     frontend/src/lib/i18n/index.ts useLocale (client, reads the Zustand store)
                     frontend/src/hooks/useGameStore.ts uiLocale (empty during SSR)

    HOW IT WAS MEASURED. `npm run build` then `next start -p 3411` bound to loopback, probed with
    curl, then the server stopped by exact PID. Three requests:

      A  no cookie, Accept-Language: sk-SK,sk;q=0.9
           <html lang="en">   title English   "Sign In" x1   "Prihlásiť sa" x0
      B  Cookie: libretiles_locale=sk
           <html lang="sk">   title SLOVAK    "Sign In" x1   "Prihlásiť sa" x0     <-- the defect
      C  Cookie: libretiles_locale=fr
           <html lang="en">   title English                                        (correct fallback)

    Case B is decisive. The document declares itself Slovak and carries a Slovak <title>, while
    every string in the body is English.

    Mechanism:       the root layout is a Server Component and reads the locale from the cookie.
                     The body is rendered by client components whose locale comes from the
                     persisted Zustand store, which is EMPTY during server rendering, so
                     useLocale() falls through to DEFAULT_LOCALE = "en". The document therefore
                     contains two independent, contradicting locale sources.
    Impact 1:        PREDICTED a guaranteed server/client hydration mismatch on every Slovak page
                     load. **DISPROVED by Cooperator observation, 2026-09-01.** He loaded
                     /settings with the Slovak locale active, opened the browser console, hard
                     reloaded with Ctrl+Shift+R, and repeated it in an incognito window. Result,
                     in his words: "konzola cista" — no hydration error at all.
                     The Orchestrator's reasoning was that zustand persist rehydrates synchronously
                     and therefore before React's first client render. Observation says otherwise:
                     rehydration lands after the hydration render, so the client's first render also
                     produces English, matches the server, and only then re-renders into Slovak.
                     Evidence class for this impact is now `rejected-false-positive`.
    Impact 2:        PREDICTED a visible flash of English copy before hydration.
                     **DISPROVED by the same observation** — "bez bliku". The re-render is
                     imperceptible.
    Impact 3:        the only impact that SURVIVES, and it is smaller than first written. The
                     pre-hydration document is internally inconsistent: `<html lang="sk">` and a
                     Slovak `<title>` around an English body. After hydration the DOM is correct, so
                     a screen reader in practice sees the corrected DOM and the accessibility claim
                     in the first version of this entry was overstated. What remains is a
                     first-byte and non-JS-crawler inconsistency, plus the structural problem that
                     the document has two independent locale sources.

    SEVERITY RE-DERIVED after the Cooperator's observation: **low**, down from medium. Reachability
                     is limited to the pre-hydration document; there is no observed user-visible or
                     console effect. Confidence in the MECHANISM stays high — the curl measurement
                     is unambiguous. Confidence in USER IMPACT is low.

    WHY IT STILL GETS FIXED, on a changed justification: once slice S3 localizes the remaining ~330
                     strings, EVERY page's server HTML will be fully English inside a
                     `lang="sk"` document, which is a much larger inconsistency than the ~30 strings
                     localized today. And slice S2 adds `Accept-Language` detection in proxy.ts,
                     which only helps if the server-known locale actually reaches the rendered tree.
                     So the provider is a prerequisite for S2 and S3 rather than a bug fix.

    ORCHESTRATOR ERROR RECORDED PLAINLY: two of the three impacts were asserted from code reading
                     with "confidence: high" and were wrong. The Cooperator's ten-second browser
                     check disproved them. This is the sixth time in this project that someone other
                     than the Orchestrator was right about a claim the Orchestrator had stated more
                     precisely than its evidence supported, and the first time it was the Cooperator
                     rather than a Worker. The original prediction is kept above rather than deleted.

    WHY NO GATE CAUGHT IT: vitest runs with environment "node" and there is no test that renders a
                     page server-side and asserts its copy. typecheck, lint, and build are all
                     blind to it. Browser MCP is a locked fork. This is PROJECT_CONTEXT lesson 1 in
                     a new costume: "for anything the model touches: measure live, or do not claim
                     it" generalises to "for anything that renders: render it, or do not claim it".

    ROOT CAUSE IS THE ORCHESTRATOR'S CONTRACT, stated plainly. The section-5 design in the
                     session-01 prompt made the store the source of truth and called the cookie a
                     "routing hint only". That is wrong for a server-rendered application: whatever
                     the server can read must be authoritative for rendered output, or SSR and the
                     client cannot agree. The Worker implemented the contract faithfully and its
                     eight gates are genuinely green. The instruction was wrong, not the execution.

    Correction direction: the server-known locale must reach the client tree. Read the cookie in
                     the root layout, pass it into a client LocaleProvider wrapping {children}, and
                     have useLocale() prefer the provider value so SSR and hydration agree. The
                     store keeps persistence; it stops being the rendering source. setUiLocale
                     writes cookie plus store and then calls router.refresh() so <html lang> and
                     metadata catch up in the same interaction — which also resolves the separate
                     limitation the Worker DID report honestly (Next 16.3.4 layouts do not rerender
                     on client navigation, documented at
                     node_modules/next/dist/docs/01-app/03-api-reference/03-file-conventions/layout.md
                     line 154).
    Regression test: a server-render assertion. Request `/` from a production `next start` with
                     Cookie: libretiles_locale=sk and assert the SSR HTML contains the Slovak
                     auth-tab string and does NOT contain "Sign In". Must fail at a5aff12.
    Owner:           ui-internationalization, slice S3a. Routing history, kept legible: first a
                     dedicated bounded correction in Worker session 02; then folded into slice S2
                     (proxy.ts locale routing) once the Cooperator's browser check dropped the
                     severity to low; then moved to S3a when Cooperator decision 7 CANCELLED S2
                     altogether by removing URL locale prefixes. S3a is the right home because a
                     LocaleProvider without localized pages cannot be meaningfully tested, and S3a is
                     the first slice that gives it real Slovak pages to render.
    Status:          open

### Orchestrator-authored follow-up at `f26e92a` — game-variant button descriptions removed

Cooperator request, 2026-09-01, in his own words: the two per-button lines under the Game variant
buttons — "PÍSMENÁ A LEXIKÓN COLLINS 2019" and "100 PÍSMEN SSS A SLOVENSKÝ LEXIKÓN" — are not wanted.
Not a defect; a product-copy decision that is his to make.

```text
frontend/src/app/settings/page.tsx     description dropped from the choices type, the two objects,
                                       and the render; min-h-[154px] -> min-h-[96px] in BOTH language
                                       panels for symmetry, since a label-only button no longer needs
                                       room for a description. The other five settings panels keep
                                       their descriptions and their 154px height, untouched.
frontend/src/lib/i18n/messages.en.ts   settings.gameVariant.englishDesc / slovakDesc removed
frontend/src/lib/i18n/messages.sk.ts   the same two keys removed
frontend/src/lib/i18n/GLOSSARY.md      the two glossary rows removed
                                       4 files, +2 -14
```

The height reduction was an Orchestrator judgement inside his request, disclosed to him before the
commit and approved (`B7-1 ok`) after he looked at it in his own running dev server.

Worth recording as evidence that the S1 type contract does what it was designed to do: removing a key
from BOTH catalogs kept `AC-EXHAUST` and `npm run typecheck` green, and removing it from only one would
have failed the typecheck gate. That is the whole purpose of `Record<TextKey, string>`.

Gates at `f26e92a`, all measured: mypy 80 files clean, ruff clean, `manage.py check` clean, pytest
`328 passed, 4 skipped in 191.60s`, `npm run typecheck` exit 0, `npx vitest run`
`337 passed | 3 skipped`, `npm run lint` exit 0, `npm run build` exit 0. Push
`a5aff12..f26e92a  main -> main`, non-force; public readback equal to local `HEAD`.

⛔ **Evidence class: NON-INDEPENDENT.** The Orchestrator was both implementer and verifier. Proportionate
for a fourteen-line R1 cosmetic change with no trust boundary, and stated explicitly rather than left
implicit. Not precedent for anything larger. The build gate was deliberately held until the Cooperator
stopped his dev server, because `next build` and `next dev` share `frontend/.next` — the same stopping
condition the Orchestrator had imposed on the Worker, honoured when the Orchestrator was on the other
side of it.



```text
B5-2a  console after Ctrl+Shift+R with Slovak active   konzola cista        PASS (disproves F04 impact 1)
B5-2b  flash of English before hydration                bez bliku            PASS (disproves F04 impact 2)
B5-2c  diacritic rendering in the gold gradient text     diakritika ok        PASS
       ľ, ť, í, ž render correctly in the clipped-background gradient. The Orchestrator's
       static prediction that Noto Serif would cover Latin Extended-A is confirmed in the
       rendered product by the acceptance owner.
B5-2c  scope observation: only the two Settings panels and their buttons are Slovak; everything
       else, including "New game", is still English, under hard reload and in incognito.
       NOT A DEFECT — this is exactly the S1 scope. S1 localized the landing/auth page, the api.ts
       error map, and two Settings panels only. Slices S3a/S3b/S3c own the remaining ~330 strings.
       Recorded because the Cooperator reported it as a possible problem and a later reader must not
       re-open it as one.
RESOLVED         the landing/auth page at `/` was unchecked at the time of B5; see B6-2 below.
B6-2   the landing/auth page while logged out, with Slovak active   vsetko ok   PASS
       He checked all seven items individually: the gold gradient headline with "ľudia aj AI.",
       the three feature cards, the account panel and both tabs, both input placeholders, the
       submit button, the footnote with a non-breaking-space thousands separator "279 496", and a
       deliberately wrong password rendering "Nesprávne používateľské meno alebo heslo".
       This closes the S1 scope: every string S1 was authorized to localize is confirmed rendered
       in Slovak by the acceptance owner.
B6-3   game-variant button descriptions unwanted -> corrected at f26e92a, see above
B7-1   both language panels after the copy removal and the height change   ok   PASS
```

### uii-01-F05 — first-visit detection cannot be done on the client without a flash

    Classification:  design consequence of uii-01-F04, recorded separately because its owner differs
    Severity:        low
    Confidence:      high
    Evidence class:  reproduced-dynamic — case A above
    Observed:        on a first-ever visit there is no cookie, so the server cannot know the
                     browser's language and necessarily renders English. Client-side detection then
                     switches to Slovak after mount.
    Correction direction considered and REJECTED: `proxy.ts` reads `Accept-Language` on a request
                     with no locale cookie and sets the cookie on the response. Rejected because
                     Cooperator decision 7 removed URL locale prefixes, so `proxy.ts` no longer needs
                     to be touched for anything except headers, and touching the file that emits every
                     security header to shave one document render is a bad trade.
    Disposition:     **accepted-residual**, severity low, approver Orchestrator (below the INFOSEC 14
                     threshold that would require Cooperator sign-off).
    Rationale:       reachability is exactly one document — the FIRST request from a brand-new visitor
                     with no cookie. The client detects, writes the cookie, and every later document is
                     correct. The Cooperator measured the visible effect in his own browser and
                     reported "bez bliku" and "konzola cista". The cost of removing it is a redirect or
                     cookie write inside the security-header emitter; the benefit is one imperceptible
                     render. Not worth it.
    Regression test: not applicable — no code change.
    Owner:           none; closed as an accepted residual.
    Status:          accepted-residual

### Two smaller observations from the same re-verification, accepted rather than corrected

```text
uii-01-N01  frontend/src/app/layout.tsx duplicates t()'s catalog ternary as a local textFor(),
            because index.ts imports React hooks and a Server Component should not pull the store
            into the server bundle. The Worker's instinct was right and it reported the deviation.
            It is a one-line duplication with two lookup paths. Cleaner shape: split a React-free
            translate.ts out of index.ts. Fold into the bounded correction, since that slice touches
            these files anyway. Severity info.
uii-01-N02  pluralSk implements one | 2..4 | otherwise, which the Worker flagged as not CLDR.
            ORCHESTRATOR VERIFICATION: for Slovak this is CORRECT for integer counts. Slovak, unlike
            Polish or Russian, uses the genitive plural from 5 upward AND for 21, 101, and so on —
            "21 minút" is right and "21 minúta" would be wrong. CLDR's Slovak "many" category is for
            non-integer values (v != 0), and every count in this product is an integer produced by
            Math.round, Set.size, or a score. The helper's third argument is therefore CLDR "other"
            rather than CLDR "many", which is a NAMING mismatch and not a behaviour defect. Accepted
            as correct; the residual is that a future decimal count would be wrong. The Worker was
            right to flag it and right not to change it.
```

### Cooperator-visible verification the Orchestrator performed on Worker session 01

Every number in the report was re-measured independently at `a5aff12` rather than accepted:

```text
git                 HEAD = ls-remote = a5aff1214d97d28f2d27e55de5de19f09faf9c0e, porcelain empty,
                    .ap gitlink unchanged at 9c5cc44
allowlist           14 files changed, all inside the section-9 allowlist. No proxy.ts, no backend,
                    no package.json, no frozen provider file, no LocaleHtmlLang.tsx (primary route
                    taken, consistently)
mypy                Success: no issues found in 80 source files
ruff                All checks passed!
manage.py check     System check identified no issues (0 silenced).
pytest              328 passed, 4 skipped in 191.81s          (Worker reported 188.32s — same counts)
npm run typecheck   exit 0
npx vitest run      337 passed | 3 skipped, 25 files passed | 1 skipped   (exactly as reported)
npm run lint        exit 0
npm run build       exit 0, route table identical to the report, every route now ƒ
doc citation        VERIFIED verbatim at layout.md line 156. The same section, line 154, also says
                    "Layouts ... do not rerender", which is the limitation the Worker reported
                    honestly rather than hiding.
string content      every en and sk string compared against the prompt's authored table; verbatim,
                    including the U+00A0 thousands separator in landing.footnote
AC-SEC-1            re-read: two DIFFERENT Django 401 bodies produce one identical message per
                    locale, and the Slovak string is checked against five enumeration fragments.
                    Correct shape. Minor gap: fragments are asserted for sk only, not en. Accepted.
AC-SEC-2            re-read: uses a real token-bearing call (changePassword) and asserts the Slovak
                    session-expired string differs from the login string. Correct.
api.ts              the requestCarriedToken distinction survives; 400 and 409 still prefer the
                    server field message; parseRetryAfterSeconds, refreshAccessToken, and the retry
                    logic are untouched
```



### Orchestrator method note — an invalid probe, recorded rather than discarded

The first attempt to measure Django's bundled Slovak coverage used
`override_settings(USE_I18N=True)` inside an already-booted process and produced a MIXED result:
`ngettext` translated to Slovak while `gettext` did not. That result was **invalid, not a finding**.
`django.utils.translation._trans` is a `Trans` object that resolves its backend from
`settings.USE_I18N` on first access **per attribute name** and then caches it with `setattr`, so every
attribute touched during `django.setup()` stayed bound to `trans_null`. The valid probe set
`USE_I18N=True` from process start through a settings module outside the repository.

Separately, a `.po`-only search reported all four Django password messages and all DRF Slovak messages
as ABSENT. Both were false negatives. The password validators live in
`django/contrib/auth/locale/sk/`, not `django/conf/locale/sk/`, and `rest_framework/locale/sk/` ships a
compiled `django.mo` with no `.po` at all. Two more instances of "a negative grep is not a conclusion",
in a single afternoon.

## Open defects from the closed security era

These are kept as history. All are `verified-closed` per `audit-03` and `audit-04` except where the
entry says otherwise; the per-entry `Status:` lines below were written before those re-audits and are
superseded by the verdict inventory in `09/00-backend-security-hardening/99_closure.md`.

### orch-02-F21 — the provider-failure log redaction is a denylist this project's own fixture defeats

    Classification:  security-finding (secret in log)
    Severity:        medium
    Confidence:      high
    Evidence class:  reproduced-dynamic — the Orchestrator ran the ten authorized vitest files at
                     8e82f3b and observed this unredacted line on stderr:
                     [libretiles-provider-failure] ibm-watsonx provider_transport null Error
                     ibm-unit-api-key project-test-1234 eu-de bearer-secret
    Location:        frontend/src/lib/provider-logging.ts redactCredentialMaterial, reached from
                     frontend/src/lib/ibm-watsonx.ts trackedFetch on the provider_transport phase
    Security property: provider credentials and account identifiers never reach a log sink
    Trust boundary:  application code to the server log sink — an egress path S7b introduced
    Attacker input:  the provider error message. The watsonx IAM token request carries the API key in
                     its request BODY, so an error that echoes the request can carry the key.
    Why it missed:   "bearer-secret" is hyphen-joined so the Bearer pattern never matches;
                     "ibm-unit-api-key" is 16 chars and "project-test-1234" is 17, both below the
                     24-character floor of the high-entropy rule; neither carries a listed prefix.
    Exploitability:  NOT demonstrated for a real credential. The leaked values are synthetic
                     fixtures, and a realistic 44-character IBM key or 36-character project UUID
                     would in fact be caught by the entropy rule.
    Why still medium: frontend/src/lib/ibm-watsonx.test.ts contains a test literally named
                     "sanitizes transport exceptions instead of exposing account values". The project
                     already decided those values are sensitive. That test asserts only the THROWN
                     error and passes, while a second egress path it does not check emits them. A
                     control the project's own sensitivity test defeats is not a control, and a
                     credential in an aggregated log has a high blast radius.
    CWE mapping:     CWE-532, MITRE CWE corpus per .ap/INFOSEC.md section 19
    Correction direction: redact by VALUE against the credentials the process actually holds, keep
                     the pattern denylist as defence in depth only, and reconsider whether the raw
                     message belongs in the highest-risk phase at all.
    Regression test: the existing watsonx sanitisation test must also assert the LOG record, using
                     its own fixture constants as sentinels. It must fail before the fix.
    Owner:           backend-security-hardening, Worker session 09 exchange 02
    Status:          corrected at 9ff9ac5 — NOT verified-closed
    Note:            this is the abuse case the S7b prompt's own threat model named first, and the
                     mandatory redaction test still passed, because the implementer chose a sentinel
                     its own regex already caught. A test written by the author of a rule tends to
                     test what the author thought of.

### orch-02-D13 — every HTTP 401 renders "Invalid username or password", including an expired session

    Classification:  product-defect (UX correctness), introduced by the acc-01-D04 correction
    Severity:        low
    Confidence:      high
    Evidence class:  established-static (era-09 continuation Orchestrator, read the 8e82f3b diff)
    Location:        frontend/src/lib/api.ts humanMessageForStatus, case 401
    Observed:        request() retries once through refreshAccessToken() when a token is present.
                     When refresh fails, clearAuth() runs and the original 401 propagates. Roughly
                     fourteen call sites render err.message directly.
    Impact:          worst case is the profile modal — the user types the correct current password,
                     the access token has expired, and the product says their credentials are wrong.
                     Misleading error text is exactly what acc-01-D04 existed to remove. Before
                     8e82f3b the text was ugly but not untrue.
    Correction direction: distinguish an authenticated 401 from an unauthenticated one at the single
                     place the mapping lives; branch on whether the request carried a bearer token.
                     Do not differentiate an unknown user from a wrong password.
    Regression test: 401 with a token renders session-expired wording; 401 without renders
                     invalid-credentials wording; neither contains "API error" or a JSON brace.
    Owner:           backend-security-hardening, Worker session 09 exchange 02
    Status:          corrected at 9ff9ac5 — NOT verified-closed

### orch-02-D11 — a production deployment gets HSTS without includeSubDomains or preload

    Classification:  security hardening (pre-existing, NOT introduced by S7a)
    Severity:        low
    Confidence:      high
    Evidence class:  established-static (era-09 continuation Orchestrator, reasoned from settings.py
                     at both 445029d and bbba2e9, plus the Worker-08 production-like probe output)
    Location:        backend/config/settings.py — SECURE_HSTS_SECONDS is set from `not DEBUG`, but
                     SECURE_HSTS_INCLUDE_SUBDOMAINS and SECURE_HSTS_PRELOAD are never set.
    ORCHESTRATOR PRECISION CORRECTION, 2026-09-01: this finding is about DJANGO's emitter only. There
                     are TWO independent HSTS emitters in this product. Django emits with neither flag,
                     which is what produces `security.W005` and `security.W021`. The Next.js proxy
                     emits `max-age=31536000; includeSubDomains` from
                     `frontend/src/lib/security-headers.ts:110`, verified in the live readback at
                     `b5774b2`. The earlier wording "a production deployment gets HSTS without
                     includeSubDomains" was therefore imprecise about which response it describes.
                     Which emitter reaches a browser depends on deployment topology and has NOT been
                     established; the P-10 re-auditor is asked to resolve it.
    Observed:        a production-like settings probe emits `security.W005` and `security.W021`.
                     Neither is in the five forbidden IDs the existing test guards, so no test
                     noticed. Both flags were equally absent at 445029d, so this is pre-existing.
    Impact:          on a real deployment, HSTS protects the exact host only. A subdomain served over
                     plain HTTP stays strippable.
    Why it is NOT a one-line fix: `includeSubDomains` covers every current and future subdomain, and
                     the `ui-internationalization` whole plans a subdomain-locale feature, so the two
                     decisions interact. `preload` is close to irreversible once submitted to the
                     browser preload list. Both are Cooperator decisions, not defaults to flip.
    Correction direction: decide includeSubDomains together with the subdomain-locale design; treat
                     preload as a separate explicit decision with its own rollback discussion.
    Regression test: whichever value is chosen, assert it explicitly in test_security_settings.py in
                     the style of the existing explicit-SECURE_* tests.
    Owner:           routed to ui-internationalization; the P-10 re-audit dispositions it
    Status:          open

### orch-02-D12 — the axes/DRF glue middleware lives inside settings.py, and one cache guard is dead code

    Classification:  code structure and reviewability (no security impact)
    Severity:        low
    Confidence:      high
    Evidence class:  established-static (era-09 continuation Orchestrator, read the bbba2e9 diff)
    Location:        backend/config/settings.py — `_AxesDrfLockoutFlagMiddleware`,
                     `_propagate_axes_lockout_to_django_request`, and `_username_from_auth_request`
                     are defined in the settings module and referenced as
                     "config.settings._AxesDrfLockoutFlagMiddleware". Separately, inside
                     `_default_cache`, the branch `if resolved["BACKEND"] == _LOCMEM_CACHE_BACKEND:`
                     can never be true, because the two lines above assign _REDIS_CACHE_BACKEND.
    Observed:        both were introduced at bbba2e9. The middleware placement is the ORCHESTRATOR'S
                     fault, not the Worker's: the S7a allowlist offered no other module, and the
                     Worker correctly stayed inside its boundary rather than inventing a path.
    Impact:          settings modules should be declarative; ~90 lines of request-handling logic in
                     one is the kind of thing a reviewer notices, and this repository is going to a
                     job interview. The dead branch is worse than merely redundant: it reads like a
                     safety check and can never fire, which is the same false-assurance shape as a
                     test that passes before the fix. The real protection is the scheme check above
                     it, which does work.
    NOT affected:    the lockout itself. `axes.backends.AxesStandaloneBackend.authenticate` raises
                     `AxesBackendPermissionDenied`, so enforcement happens in the backend chain and
                     does not depend on this glue. The middleware only upgrades the HTTP status to
                     429 and resets counters on a successful SimpleJWT login. Verified by reading
                     .venv/lib/python3.12/site-packages/axes/backends.py.
    Correction direction: move the three callables to their own small module, reference that module
                     from MIDDLEWARE, and delete the unreachable branch. No behaviour change.
    Regression test: the existing test_axes_is_wired_in_required_order must keep passing with the new
                     dotted path, and tests 1-4 and 7-10 must keep passing unchanged.
    Owner:           backend-security-hardening, slice S7b (authorized adjacent consistency change)
    Status:          corrected at 8e82f3b — NOT verified-closed

### orch-02-D09 — POST /api/auth/logout/ exists and blacklists, but nothing calls it

    Classification:  product-defect (security, incomplete wiring)
    Severity:        low
    Confidence:      high
    Evidence class:  established-static (era-09 continuation Orchestrator, read at 445029d)
    Location:        backend/accounts/views.py:66-96 implements LogoutView and blacklists the
                     presented refresh token. frontend/src/lib/api.ts exposes no `logout` method at
                     all, and handleLogout at frontend/src/app/game/[id]/page.tsx:770-782 only closes
                     the websocket, resets local UI state, and calls clearAuth().
    Observed:        the endpoint has zero callers in frontend/src.
    Impact:          logging out clears localStorage but leaves the refresh token valid on the server
                     for its full 7-day lifetime. Refresh-token theft is therefore mitigated only by
                     a password change, which is the one path that does blacklist.
    Correction direction: add a `logout` method to the api client and call it from handleLogout before
                     clearing local state, tolerating failure so a logout can never get stuck.
                     Consider giving LogoutView a throttle scope at the same time.
    Regression test: a test that handleLogout issues the logout request with the stored refresh token,
                     and that local state is still cleared when that request fails
    Owner:           backend-security-hardening, slice S7b
    Status:          corrected at 8e82f3b — NOT verified-closed

### orch-02-D10 — an admin-initiated password change does not blacklist outstanding refresh tokens

    Classification:  product-defect (security bookkeeping)
    Severity:        low
    Confidence:      medium — the primary protection appears to already exist; see below
    Evidence class:  established-static (era-09 continuation Orchestrator, read at 445029d)
    Location:        backend/accounts/models.py:31-35 stamps password_changed_at inside the
                     set_password override, so the admin path does set it. Only
                     ChangePasswordSerializer.save() at backend/accounts/serializers.py:75-80 also
                     calls blacklist_outstanding_refresh_tokens().
    Observed:        static reading says an outstanding refresh token is ALREADY unusable after an
                     admin-initiated change, because PasswordAwareTokenRefreshSerializer runs
                     reject_if_issued_before_password_change. If that reading holds, this is explicit
                     revocation bookkeeping rather than a live hole, and the S7a Worker must say so.
    Impact:          revocation is inferred from a timestamp comparison instead of being recorded in
                     the blacklist table, so an operator auditing revocations cannot see it.
    Correction direction: blacklist outstanding refresh tokens on the admin path too, with the
                     smallest correct mechanism. Do not restructure set_password.
    Regression test: after an admin-path password change, outstanding refresh tokens are blacklisted.
                     A "passes before the fix" result is an acceptable and honest outcome here and
                     must be reported as such.
    Owner:           backend-security-hardening, slice S7a
    Status:          corrected at bbba2e9 — NOT verified-closed

### orch-02-D08 — the documented provider list is two providers; the repository ships nine

    Classification:  documentation (factual accuracy)
    Severity:        low technically, medium for interview presentability
    Confidence:      high
    Evidence class:  established-static (era-09 continuation Orchestrator, read at 445029d)
    Location:        AGENTS.md — the opening "Frontend" bullet said "AI via provider-diverse free
                     rivals (OpenRouter + NVIDIA NIM on Next.js API routes)", and the key-file table
                     listed only openrouter.ts, nvidia-nim.ts, ai-runtimes.ts
    Observed:        frontend/src/lib/provider-registry.ts declares NINE provider constants —
                     openrouter, nvidia-nim, groq, google-gemini, cloudflare-workers-ai, mistral,
                     ibm-watsonx, aion, huggingface — with exact model tuples and catalog tiers.
                     Eight dispatch through the shared OpenAI-compatible transport in
                     frontend/src/lib/openai-compatible.ts; ibm-watsonx has its own IAM path in
                     frontend/src/lib/ibm-watsonx.ts. Added in commits 3c828e6 and c3bdfc8, both
                     ancestors of 445029d. README.md was already accurate — its feature list already
                     names the Groq -> Gemini -> Cloudflare -> Mistral -> watsonx direct priority.
                     Only AGENTS.md was stale.
    ORCHESTRATOR CORRECTION, on Worker-08 evidence: the original version of this entry also claimed
                     that backend/catalog/selection.py declared only two providers. That was WRONG.
                     selection.py carries all nine; the seven extra ones are string literals inside
                     DIRECT_FREE_RIVALS and WATCHLIST_FREE_RIVALS rather than module-level
                     *_PROVIDER constants, so the Orchestrator's constant-only grep missed them and
                     a negative grep was treated as a conclusion. The Worker measured it and said so.
                     selection.py needed no change and was not changed. Scope of this defect is
                     AGENTS.md only.
    Impact:          the file an agent or a reviewer reads first understated the product by seven
                     providers. It also mis-scoped provider-boundary work: acc-01-D02 named three
                     files to add logging to, when the actual choke point is a fourth.
    Correction:      landed at bbba2e9 — AGENTS.md provider sentence rewritten to name all nine, and
                     three key-file rows added (provider-registry.ts, openai-compatible.ts,
                     ibm-watsonx.ts). provider-registry.ts and selection.py untouched.
    Regression test: none applicable (documentation)
    Owner:           backend-security-hardening, slice S7a
    Status:          corrected at bbba2e9 — NOT verified-closed

### acc-01-D01 — a channel-layer outage is undiagnosable and burns single-use websocket tickets

    Classification:  product-defect (operability, not security)
    Severity:        medium
    Confidence:      high
    Evidence class:  reproduced-dynamic (Orchestrator raw websocket handshake + ticket-row correlation)
    Location:        backend/game/consumers.py connect() — channel_layer.group_add is OUTSIDE the
                     try/except that otherwise closes with code 4403
    Reproduction:    make Redis unreachable from the host; open
                     ws://localhost:8000/ws/game/<id>/?ticket=<fresh>; observe a TCP reset with no
                     HTTP status and no WebSocket close code, while the ConsumedWsTicket row count
                     increments by one
    Observed:        verify_ws_ticket completes and CONSUMES the ticket, then group_add dies. The
                     browser shows only "Realtime connection failed". Nothing is logged.
    Impact:          on a deployment, a Redis problem presents as "multiplayer is broken" with zero
                     clues, and every retry consumes a single-use ticket
    Correction direction: wrap group_add/accept so a channel-layer failure closes with a distinct
                     code and logs the cause; decide deliberately whether the ticket should be
                     consumed before or after the connection is fully established
    Regression test: a test with the channel layer forced to fail must observe a distinct close
                     code, and must assert whether a ticket was consumed
    Owner:           backend-security-hardening, slice S7b
    Status:          corrected at 8e82f3b — NOT verified-closed

### acc-01-D02 — provider failures are unlogged, so an expired credential is indistinguishable from a silent model

    Classification:  product-defect (observability)
    Severity:        medium
    Confidence:      high
    Evidence class:  reproduced-dynamic (Orchestrator, from the Cooperator's own persisted ai_metadata)
    Location:        frontend/src/app/api/ai/move/route.ts, src/lib/ai-runtimes.ts,
                     src/lib/nvidia-nim.ts, src/lib/openrouter.ts — no console.error anywhere
    Observed:        with an expired key every AI turn recorded terminal_cause =
                     generic_error_fallback, provider_requests_used = 1, valid_candidate_count = 0,
                     and completed in ~5 s. With a fresh key the same fields became terminal_cause =
                     no_provider_progress_deadline and ~21 s. The exception class and message were
                     discarded in both cases; only terminal_cause survived in ai_metadata.
    Impact:          a systematic provider failure is invisible without querying ai_metadata by hand.
                     Diagnosing an expired key cost one full Orchestrator detour.
    Refuted causes:  network reachability (DNS + TLS to integrate.api.nvidia.com and openrouter.ai
                     both succeed from the host, ~0.2 s, even through a Tailscale exit node); CSP
                     (the provider call is server-side)
    Correction direction: log a bounded, redacted classification of the provider exception — class,
                     HTTP status when present, and a truncated message — never the key, never the
                     request body. Consider surfacing it in the turn telemetry that already exists.
    Regression test: a test asserting that a thrown provider error produces a bounded log record and
                     that the record contains no credential material
    Owner:           backend-security-hardening, slice S7b
    Status:          corrected at 8e82f3b — NOT verified-closed
    Note:            the ORIGINAL D02 (every provider call throwing an unclassified exception) was
                     RESOLVED by the Cooperator installing a fresh provider key. What remains open is
                     only the observability gap that made it hard to find.

### acc-01-D03 — registration validation errors are swallowed and reported as "Invalid username or password"

    Classification:  product-defect (UX + observability), exposed by the S3 password policy
    Severity:        medium
    Confidence:      high
    Evidence class:  reproduced-dynamic (Cooperator observed twice; Orchestrator traced the code path)
    Location:        frontend/src/app/page.tsx:37-44 (bare `catch {}` around api.register) and
                     :74-80 (the 401 -> "Invalid username or password" mapping)
    Observed:        registering with `12345678` and with `password123456` both produced
                     "Invalid username or password"
    Mechanism:       Django correctly rejects the weak password with HTTP 400 and a precise message
                     such as "This password is entirely numeric." page.tsx discards it with a bare
                     catch whose comment reads "User may already exist — fall through to login", then
                     unconditionally attempts login. No account exists, so login returns 401, which
                     is mapped to the misleading string.
    Impact:          a new user cannot discover why registration failed. Each retry burns one
                     auth_register slot AND one auth_login slot, and the eventual 429 renders as the
                     same misleading message. Before S3 this was latent, because weak passwords were
                     accepted and the only common failure was a duplicate username, for which
                     falling through to login is actually correct.
    Correction direction: surface the server's field-level validation error, in English, including
                     what the password must satisfy; do not fall through to login when registration
                     failed for anything other than a duplicate username
    Regression test: registering with an all-numeric password must display the server's password
                     error and must NOT attempt a login request
    Owner:           backend-security-hardening, slice S7b
    Status:          corrected at 8e82f3b — NOT verified-closed

### acc-01-D04 — raw API error strings are surfaced to the user

    Classification:  product-defect (UX), exposed by the S3 throttles
    Severity:        low
    Confidence:      high
    Evidence class:  reproduced-dynamic (Cooperator observed)
    Observed:        exceeding the login rate limit displayed, verbatim:
                     API error 429: {"detail":"Request was throttled. Expected available in 3274 seconds."}
    Impact:          the user is shown the transport status code and a raw JSON body. The Cooperator's
                     own reaction was that "Too many requests" would be better. It also discloses the
                     internal error shape for no benefit.
    Contrast:        the change-password path is GOOD and should be the model — it produced
                     "Current password is incorrect." and "Password updated."
    Correction direction: map known statuses to human messages at one place in the API client; for
                     429 present a human wait time rather than raw seconds, and never render the raw
                     body
    Regression test: a 429 response must render a human message containing neither "API error" nor a
                     JSON brace
    Owner:           backend-security-hardening, slice S7b
    Status:          corrected at 8e82f3b — NOT verified-closed

### acc-01-D05 — the login throttle window locks the Cooperator out for ~55 minutes

    Classification:  configuration (product decision), consequence of S3
    Severity:        medium for demo usability, low for security
    Confidence:      high
    Evidence class:  reproduced-dynamic (Cooperator hit it; the 429 quoted 3274 seconds)
    Observed:        auth_login is 10/hour and IP-keyed, so every browser profile and every account
                     on the machine shares one budget. Combined with acc-01-D03, one failed
                     registration also consumes a login slot.
    Impact:          ordinary testing and a live demo can lock the presenter out for most of an hour.
                     Restarting Django clears the counters only because the cache is per-process
                     LocMemCache, which is itself a finding on a multi-worker deployment.
    Correction direction: raise the IP-keyed login rate to a value that tolerates a demo, and get the
                     real brute-force protection from per-account lockout (django-axes, already
                     approved by the Cooperator). State the arithmetic for a realistic session.
    Regression test: a documented number of failed logins that a demo would plausibly produce must
                     NOT be throttled; a clearly abusive number must be
    Owner:           backend-security-hardening, slice S7a
    Status:          corrected at bbba2e9 — NOT verified-closed

### acc-01-D06 — a fresh clone cannot boot, by design, and the documented onboarding path is broken

    Classification:  documentation + onboarding
    Severity:        low technically, medium for interview presentability
    Confidence:      high
    Evidence class:  established-static (Orchestrator read the template)
    Observed:        backend/.env.example ships `DJANGO_SECRET_KEY=` empty, so the README-documented
                     `cp backend/.env.example backend/.env` followed by `migrate` fails closed. The
                     error message is clear, which is the intended hardening, but the documented
                     onboarding sequence no longer works.
    Impact:          anyone who clones the repository — including an interviewer — hits a crash on
                     the documented first command
    Correction direction: have scripts/libretiles.sh generate a strong key into a freshly created
                     backend/.env, and correct the onboarding paragraphs in README.md and AGENTS.md
    Regression test: a script test that a freshly created .env yields a bootable configuration
    Owner:           backend-security-hardening, slice S7a
    Status:          corrected at bbba2e9 — NOT verified-closed

### acc-01-D07 — documentation drift

    Classification:  documentation
    Severity:        low
    Evidence class:  established-static
    Observed:        README.md:278 says the AI judge makes "up to five attempts"; AGENTS.md and the
                     code use three. README.md:82 and backend/.env.example:33 documented
                     GAME_WS_TICKET_MAX_AGE_SECONDS as 60 while the code default became 10 — the
                     Worker corrected the templates, but any pre-existing .env still pins 60, which
                     is exactly what happened on the Cooperator's machine and silently disabled the
                     TTL reduction until he changed it.
    Correction direction: fix the judge attempt count; add a note that pre-existing .env files
                     override new code defaults and must be reviewed after a settings change
    Owner:           backend-security-hardening, slice S7a
    Status:          corrected at bbba2e9 — NOT verified-closed

---

## Verified working — recorded so nobody re-tests it

All observations by the Cooperator in his own browser on 2026-08-31, corroborated by the Orchestrator
from the repository and the development database where noted.

| Area | Result | Corroboration |
|---|---|---|
| Enforced CSP does not break page load, styling, or login | PASS | Orchestrator read the live response headers with curl: CSP, nosniff, DENY, referrer-policy, permissions-policy, COOP present; `Strict-Transport-Security` correctly absent in development |
| AI game vs the house, English: create, place a valid word, score credited | PASS | moves persisted |
| AI turn completes and its move appears | PASS, ~21 s with a working key | `ai_metadata` inspected |
| F5 mid-game rehydrates board, scores, and session | PASS | — |
| An invalid word is rejected with a clear message and the game continues | PASS | — |
| **Human-vs-human multiplayer, end to end** | **PASS, first manual verification in the project's history** | game `8e376a62` reached `active` with both slots filled; `BAR` 10 pts by slot 0 at 14:43:52 and `ROW` 7 pts by slot 1 at 14:44:04; two chat messages, one from each user; three consumed websocket tickets |
| Waiting room websocket connects (proves the `ws://` origin in CSP) | PASS | — |
| Realtime move sync without a refresh | PASS | two users' moves 12 s apart in one game |
| Chat both directions with correct author attribution | PASS | 2 rows, one per user |
| F5 mid-game reconnect with single-use tickets and a 10 s TTL | PASS | consumed-ticket rows present |
| Change password with the wrong current password | PASS — "Current password is incorrect." | — |
| Change password correctly | PASS — "Password updated." | — |
| **Old session rejected after a password change (S4 revocation)** | **PASS — "Session expired"** | — |
| Login with the new password | PASS | — |
| Login rate limiting fires | PASS (server), see acc-01-D04/D05 for the message and the window | — |
| Registration rejects all-numeric and common passwords | PASS (server) | user `id=4` created only with a strong password |

## Not yet covered by manual acceptance

These are the remaining human-only observations, and they are the reason the
`product-acceptance-sweep` whole still has work to do:

- Slovak variant in a browser: diacritic tiles rendering and placement, a legal two-letter Slovak play accepted when hooked onto a board word, a blank resolved to a diacritic letter, the AI playing Slovak
- A full game played to a legitimate end reason, with the final leftover-rack scoring and a declared winner
- Settings, the premium-look toggle, and the reduced-motion path
- The two known UX defects the Cooperator reported: the new-game modal not appearing after "Play the house", and Settings appearing to change the language during a game
- Error and edge paths beyond the invalid word: provider unavailable, expired session at various points
- Accessibility basics: keyboard reachability, focus states, modal focus trap and ESC, readability with the premium look disabled, layout at a smaller window

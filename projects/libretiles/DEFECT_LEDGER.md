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
archive-ordering key assigned at creation time, not a priority ranking; execution order is `10/00`,
then `11/01`, then `11/02`, then `11/00`, and that is recorded here so the mismatch is not read as an
error. An earlier version of this paragraph said "`11/01` first, then `11/00`" and omitted both `10/00`
and `11/02`; corrected rather than quietly deleted.

### The accepted two-whole split, recorded here so it is not only in the acceptance file

Planning decision 1, ACCEPTED by the Orchestrator on 2026-09-01: the objective splits sequentially into
`atomic-tile-token-foundation` (generic engine, migration, wire format, AI boundary, frontend state,
readiness discovery, English/Slovak conversion, synthetic canaries) and then
`czech-polish-hungarian-variant-activation` (Meta 11/02, NOT STARTED, blocked only on manually supplied
dictionaries, short-word authorities, approved alphabet orders, and provenance). The boundary is the
dictionary dependency, which is real and external.

⚠ **RF-19 identity, resolved deliberately by the era-11 Orchestrator rather than drifted into.** Two
candidate logical-whole identities exist for one Meta directory: `multilingual-tile-token-foundation`,
carried by the archived Worker exchanges 01/01 and 01/02 and by this ledger, and
`atomic-tile-token-foundation`, used by the `11/01` handout capsule and by planning decision 1. The
identity in force is **`multilingual-tile-token-foundation`**. Reasons: the archived exchange
coordinates and the Meta directory already carry it; the two-whole split narrowed the objective but did
not materially change it, so RF-19's new-identity-and-reset rule is not triggered; and a new identity
would reset the session ordinal to `01`, putting two different concrete Worker sessions on ordinal `01`
inside one archive directory. `atomic-tile-token-foundation` and `czech-polish-hungarian-variant-
activation` are therefore scope labels, not RF-19 identities. Slice F1 is session `02`, exchange `01`.

## Slice F1 landed at `9f0c5b8141b94785f26f84fd0104131f063c3ed6` — Worker session 02, exchange 01

`feat(engine): make tile tokens atomic in the pure game engine`. 26 files, +1225 −131, parent
`1b7b05d`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED.** Evidence is **non-independent** by design — the whole receives one fresh independent R4
application audit after slice F3.

### What the Orchestrator re-verified rather than accepted from the report

Every material claim was re-measured. Two reproductions matter more than the rest:

**1. The seeded-bag promise is PROVEN, not asserted.** Design decision 4.2 said the bag order must not
move, because `letters` order feeds `distribution`, which is the pre-shuffle tile sequence for
`TileBag`. The Orchestrator reconstructed the first twenty draws **from the baseline `1b7b05d` manifest
blobs using baseline logic only** — the old `len(letter) != 1` filter, sort by token, dict insertion
order, `random.Random(seed).shuffle` — and got sequences byte-identical to the four the Worker pinned
in `test_seeded_bag_first_twenty_draws_match_baseline_1b7b05d`, which passes at `9f0c5b8`:

```text
english seed  1  M H O L A E I A A S I H T L X U O D S G
english seed 42  I I U A O L ? P D S R A N N R I K V R H
slovak  seed  1  O K R O A E L A A Y M K Ä O Ŕ Ý S D X J
slovak  seed 42  M M Č A R O ? T D V T A O O T N N Ď V K
```

Two-sided: the values match a baseline reconstruction AND the test pinning them passes at HEAD.
Therefore seeded games are unchanged. The Worker did not pin post-change values and label them baseline.

**2. The formed-word invariant holds, probed live against the new authority.**

```text
word                      physical  codepoints  route      accepted
OSAMENIU (contains AM)        8          8      main       True     <- invariant intact
AM as a COMPLETE 2-tile word  2          2      two_tile   False
Á + CS                        2          3      two_tile   True     <- the defect this fixes
Á + C + S                     3          3      main       True     <- keyed on tiles, not string
```

`Á`+`CS` is the case `backend/game/services.py:209-222` gets wrong today, because
`_word_passes_dictionary` keys the two-letter rule on `len(w) == 2` in **code points**. The new
authority keys on `len(word.letters)`, the coordinate count. A source audit for substring patterns in
`word_authority.py` returned none.

### Gates at `9f0c5b8`, Orchestrator-measured

```text
mypy               Success: no issues found in 81 source files   (80 + word_authority.py)
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             352 passed, 4 skipped in 195.32s              (328 + 24; none lost, none skipped)
npm run typecheck  exit 0                        <- the code type-checks
npx vitest run     342 passed | 3 skipped        <- unchanged, which proves no frontend file changed
npm run lint       exit 0
npm run build      exit 0, every route ƒ, Proxy registered, no deprecation warning   <- the build passed
```

### Boundary discipline, verified line by line

The two narrowly bounded `backend/game/` files changed **exactly** the five permitted lines and nothing
else: `services.py` line 52 import plus call sites 128 and 138; `diagnostics.py` line 31 import plus
call site 331. All five are the `load_two_letter_allowlist` → `load_two_tile_words` rename. No frontend
file, no migration, no model, no `config/`, `accounts/`, `catalog/`, `billing/`, no documentation.
Locks A–D untouched. The ten untracked flag images are still untracked and unstaged.

The asset rename is recorded by Git as **R100** and the Orchestrator computed the SHA-256 of both the
new file and the baseline blob: `e2587f15c19c9046d013d161a06ba54deab0d05bee9f2dd2ac47c3d151048402`,
identical. 103 entries, old name absent.

`alphabet_order` in both manifests matches `PROJECT_CONTEXT.md` section 14 token for token — English 26,
Slovak 46. Neither manifest declares `vowels`, as required. `letters=tuple(sorted(...))` is preserved at
`variant_store.py:393` with a comment recording that it has no game meaning.

### Adjacent hardening the Worker did inside the allowlist, disclosed rather than silent

The loader now **raises** `VariantManifestError` with a stable `code` on a malformed `letters` row,
where it previously did a silent `continue`. That is stricter than the named scope and is desirable —
a silently skipped tile row is exactly how the Hungarian defect hid — but it is recorded here because
it is a behaviour change beyond the literal instruction.

### Two latent notes for F2 and F3

```text
1  VariantDefinition.playable_letters resolves alphabet positions with a bare index[token] lookup.
   A hand-constructed VariantDefinition with an empty alphabet_order would raise KeyError. NOT
   reachable today: the Orchestrator grepped and there is no `VariantDefinition(` construction
   anywhere outside variant_store.py. Do not introduce one without alphabet_order.
2  WordAuthority.is_lexical_word is a deliberately permissive searcher prune over a concatenated
   string and does NOT apply physical length. That is safe only while accepts_formed_word over a
   WordFound remains the final gate. F2 must not promote is_lexical_word to a legality decision.
```

### F2 obligations handed forward — none of these is done

```text
- delete _word_passes_dictionary and re-point the evaluate_scoring_move callers in services.py and
  diagnostics.py at WordAuthority. Two authority paths must not become permanent.
- invert Cell storage onto token/blank_as and remove the derived properties added in F1
- wire VariantDefinition.slot0_wins_starting_draw into _perform_starting_draw. uii-01-F07 is NOT
  corrected by F1; only its pure ordering half exists.
- correct uii-01-F06: bag_tiles string length, character split, and the _persist_board join
- migrations 0008/0009, preceded by their own separate read-only preflight
- build_ai_state_dict is still lossy for multi-code-point cells; that is F3's, not F2's
```

### Residual-Risk Decision record — Slovak vowel classification

```text
Finding ID: mtt-F1-R01
Decision: accepted-residual
Severity: low
Approver: Orchestrator (below the INFOSEC 14 medium threshold that requires Cooperator sign-off)
Regression test: test_declared_vowels_change_leave_quality_slovak_stays_on_default — proves the
  mechanism reacts to a declared `vowels` list and that Slovak deliberately stays on the default
Rationale: neither english.json nor slovak.json declares `vowels`, so the default "AEIOU" still
  classifies Á Ä É Í Ó Ô Ú Ý as consonants in ranked leave quality. Measured effect on a synthetic
  variant: declaring Á as a vowel moves leave imbalance from 2 to 0 on rack ["Á","B"]. This was a
  deliberate instruction, not an oversight: the engine authors every move in this product, the
  measured Slovak engine numbers (520–560 per side, ~29 plies, all 17 single-copy diacritic tiles
  consumed) were produced under the current ranking, and changing what the player watches the AI play
  needs its own measured decision rather than a side effect of a token refactor.
Recorded in: this ledger and 02_report_00.md item 10
```


### F2 read-only preflight — Worker session 03, exchange 01, at `9f0c5b8`

Verdict: **preflight PASS, ACCEPTED.** Read-only; the repository is still at `9f0c5b8`, porcelain is still
exactly the ten flag images, no commit, no push, and the live SQLite file is byte-for-byte untouched
(`389120` bytes, mtime `2026-09-01 14:18:34.571546513 +0200`, verified by the Orchestrator after the
Worker's cleanup). The authorized temporary root `/tmp/opencode/mtt-f2-preflight/` is confirmed absent.

The Orchestrator re-measured the database independently through a read-only `mode=ro` connection.
**Eighteen of eighteen row counts match the report exactly**, as does the table count, the FK topology,
`journal_mode`, `integrity_check`, and the migration leaf.

```text
five target tables      game_chat_message 2   game_move 42   game_player_slot 58
                        game_session 29       game_consumed_ws_ticket 1        total 132
protected               accounts_user 4  catalog_ai_model 12  catalog_ai_prompt 4
                        token_blacklist_outstandingtoken 23  ...blacklistedtoken 5
                        all four axes_* 0    django_migrations 63    django_content_type 19
                        auth_permission 76   sqlite_sequence 17
tables total            24
billing_% tables        ABSENT (app not in INSTALLED_APPS; disk migrations never applied)
inbound FKs to the five 4 edges, ALL from inside the five; from outside: ZERO
outbound to protected   game_session.ai_model_id, .ai_prompt_id, game_player_slot.user_id,
                        game_chat_message.user_id — Django on_delete SET_NULL, so deleting a GAME row
                        never touches the protected row
journal_mode            delete   (no -wal / -shm sidecars exist)
integrity_check         ok
game leaf               0007_consumedwsticket; 0008 and 0009 do not exist
database                sqlite3, /home/agile/Projects/libretiles/backend/db.sqlite3
```

**The five targets are NOT empty.** 132 rows. F2's purge is therefore a real irreversible deletion and
**does** require the explicit opt-in flag; the empty no-op path must still be proven synthetically.

#### Orchestrator precision correction on one reported value

The report states `PRAGMA foreign_keys = 1`. A raw `sqlite3.connect()` from the Orchestrator reports
`0`. **Neither is wrong** — `PRAGMA foreign_keys` is a **per-connection** setting, not a database
property. The Worker measured it through the Django connection, which is the correct lens because that
is the connection `migrate` uses; the Orchestrator measured a bare connection, which defaults to OFF.
Recorded so a future reader does not "fix" a non-defect. The consequence for F2 is real: FK enforcement
depends on which connection performs the deletion, so F2 must not depend on PRAGMA state at all.

#### Findings the accepted plan did not name, all accepted into F2's boundary

```text
1  SQLite stores every one of these FKs as ON DELETE NO ACTION while the Django models declare
   CASCADE / SET_NULL. A raw parent DELETE therefore fails while children exist, and disabling FK
   checks would make it unconstrained. CONSEQUENCE, now mandated: F2 deletes through named historical
   models with ORM querysets, never raw SQL, and never touches PRAGMA foreign_keys.
2  game_consumed_ws_ticket has no FK in either direction. A collector delete of GameSession will NOT
   remove tickets. Step 5 of the authorized order is mandatory and independent, not redundant.
3  The Cooperator's runserver holds db.sqlite3 open (pid 211102 at inspection; re-check at apply time,
   never assume the PID). F2's first stage gate is a Cooperator-stopped Django process.
4  journal_mode is `delete`, not WAL, so no sidecar copy is needed today — but the checkpoint must use
   the SQLite `.backup` API rather than a plain file copy, because a process holds the file open and
   the mode can change.
5  sqlite_sequence AUTOINCREMENT counters survive DELETE and its own row count stays 17. F2 must not
   DELETE FROM sqlite_sequence, and no test may expect primary keys to restart at 1.
6  If any billing_% table ever exists, F2 must REFUSE: historical billing_transaction declared
   SET_NULL to game_session, which would mean a session delete updating unauthorized rows.
```

#### Checkpoint and restore recipe, accepted as F2's stage gate

```text
checkpoint   sqlite3 <DB> ".backup '<ABS>/db.sqlite3.f2-checkpoint'"      (Django stopped)
restore      cp <ABS>/db.sqlite3.f2-checkpoint <DB>                        (Django stopped)
never        VACUUM on the live file; restore into an open database
```

#### Migration-test harness the project already owns — F2 must reuse it, not invent one

`TransactionTestCase` plus `MigrationExecutor(connection).migrate(...)` with historical models from
`executor.loader.project_state(...).apps.get_model(...)`; destructive/irreversible data steps use
`call_command("migrate", app, target, verbosity=0)` or import the `RunPython` callables directly;
teardown always calls `backend/tests/_migration_restore.py` `restore_apps_to_leaf(*app_labels)`, which
resolves the live graph leaf rather than pinning a name. `test_creditless_migration.py` is the closest
existing cousin to a purge and is the model to follow.

### ORCHESTRATOR SCOPE DECISION: the accepted plan's slice F2 is SPLIT into three

The accepted plan's F2 bundles the purge migration, the schema migration, the REST and websocket v4
change, and the frontend state change into one slice. That is the exact shape the era-09 lesson and
`PROMPT_ENGINEERING_PATTERNS` P05 forbid: one allowlist covering a migration, a persistence rewrite, a
wire-format change and a frontend rewrite produces a diff nobody can review honestly. Era 09 split S7
into S7a/S7b for the same reason.

```text
F2a  the irreversible purge, ALONE.  migration 0008 + the fail-closed setting +
     backend/.env.example + migration tests. E4. Requires the Cooperator to stop Django and a
     verified .backup checkpoint. No schema change, no REST, no websocket, no frontend.
F2b  backend persistence and legality.  migration 0009 (drop blanks, retype bag_tiles, structured
     board_state), the services/serializers persistence paths, uii-01-F06, the uii-01-F07 wiring, and
     re-pointing evaluate_scoring_move at WordAuthority with _word_passes_dictionary deleted.
     The REST and websocket payload shape stays UNCHANGED behind a documented temporary adapter.
F2c  wire format and frontend, together.  REST/websocket state_schema_version 4, BoardCell[][],
     localStorage v4, board/tile/blank/draw rendering — and the F2b adapter is deleted here.
```

Why F2b keeps the wire shape frozen behind a throwaway adapter: if the backend emitted v4 while the
frontend still read v3, the product would be broken between two slices. The Cooperator opens this
application, and a fresh clone that crashes is a first-class defect in his frame. A small named adapter
that one later slice deletes is cheaper than a broken window. Each of the three slices is green at its
own commit and the product never breaks.


### F2a exchange 01 returned PARTIAL / NEEDS_ORCHESTRATOR_DECISION — and the Worker was right to stop

Worker session 04, exchange 01, at `9f0c5b8`. It wrote the four-path candidate, ran the eight gates,
hit a red pytest, and **stopped at gate G1 without applying anything**. Orchestrator-verified: `HEAD`
still `9f0c5b8`, no commit, no push, `django_migrations` still 63, the five target tables still hold
132 rows, `backend/db.sqlite3` mtime unchanged at `2026-09-01 14:18:34.571546513 +0200`, no checkpoint
directory, and porcelain carrying exactly the four candidate paths plus the ten flag images.

It also declined to make `0008` reversible to force the gate green, which would have destroyed the
honesty of the irreversibility contract. That was the right call.

#### The measured blocker

```text
tests/test_scoreless_turns_migration.py:14   executor.migrate([("game","0005_remove_money_state")])
  -> IrreversibleError, raised from game/migrations/0008_purge_legacy_game_state.py:33
```

That test walks the `game` graph backward to `0005` to exercise the `0006` column rename. An
irreversible `0008` sits on that backward path. Orchestrator-reproduced.

#### ORCHESTRATOR MEASUREMENT: the Worker's own recommended fix would have failed at the next gate

The Worker recommended option A — expand the allowlist by `test_scoreless_turns_migration.py` and
fake-unapply `0008` before the backward walk. That fixes line 14. **It does not fix line 34.**
`restore_apps_to_leaf("game")` in that test's `finally` re-applies `0008` **forward** while the
`GameSession` row created at line 17 still exists, and the fail-closed guard fires. Measured with a
throwaway probe test against the test database, removed immediately afterwards:

```text
PROBE rows before teardown: 1
PROBE teardown re-apply: RAISED RuntimeError: Refusing to purge non-empty game state because
  ALLOW_DESTRUCTIVE_GAME_STATE_RESET is false.
```

So a data-destroying, fail-closed, irreversible migration is hostile to Django's own test harness in
**two independent directions** — backward because it is irreversible, forward because its guard raises
on re-apply. Patching the one visible symptom would have hit the second one immediately. This is the
mechanism being wrong, not a test defect.

A **third** hazard follows by the same mechanism and was deliberately not measured, because the chosen
fix makes it unreachable: `test_creditless_migration.py::test_cleanup_migrations_are_irreversible`
asserts that migrating `game` back to `0004` raises. With an irreversible `0008` in the graph it would
raise at `0008` and never reach `0005`, so the test would keep passing while no longer proving what it
was written to prove. Recorded because the reasoning must stay legible, and labelled unmeasured.

### ORCHESTRATOR DECISION: the purge is a management command, not a migration

**This deviates from accepted planning decision 2 and from `11/01/00_handout.md` section 7**, both of
which specified migration `0008_purge_legacy_game_state`. The Cooperator-authorized *behaviour* is
unchanged — delete development game state in those five tables, fail-closed, never any other table.
Only the mechanism changes. Mechanism is Orchestrator-owned; the deviation is recorded here rather than
absorbed silently.

```text
BEFORE   migration game.0008 deletes rows during `manage.py migrate`
AFTER    manage.py purge_legacy_game_state deletes rows when an operator runs it, and F2b's schema
         migration REFUSES to run while legacy rows remain
```

Six reasons, in descending weight:

```text
1  `manage.py migrate` must never be destructive. Under the migration design a production deployment
   carrying ALLOW_DESTRUCTIVE_GAME_STATE_RESET=true in its environment — a plausible copy-paste —
   would silently delete every production game during a routine migrate. The plan states in terms that
   production deletion is not authorized and needs separate authority, a verified backup, and a
   maintenance window. A command makes that accident impossible; a migration invites it.
2  Onboarding stays intact. README.md documents `manage.py migrate` as the first command a fresh clone
   runs, and acc-01-D06 was precisely "a fresh clone cannot boot and the documented onboarding path is
   broken". A migration that aborts whenever game rows exist re-breaks that path.
3  Both measured hazards disappear rather than being patched. No irreversible node enters the graph, so
   test_scoreless_turns_migration.py needs no change and no fifth allowlist path. No forward guard sits
   inside a migration, so the teardown re-apply hazard is gone for every current and future test.
4  The third hazard above becomes unreachable.
5  E4 wants stage separation. Hiding an irreversible deletion inside `migrate` is the opposite of it.
6  It is directly testable with call_command, with no migration-graph gymnastics.
```

Costs, stated rather than minimised: the purge is no longer a `django_migrations` row, so its evidence
lives in the command's logged pre/post counts, the Worker report, and this ledger. And ordering now
depends on F2b's guard instead of graph position — which is why that guard is a mandatory F2b
obligation, with its own test proving both the refusal and the clean pass on empty tables.

Consequence for numbering: **F2b's schema migration is `0008_atomic_token_state_schema`, not `0009`.**
The accepted plan called it `0009` because `0008` was to be the purge. There is no gap and nobody
should hunt for a missing `0008`.

Reissued as Worker session 04 **exchange 02**, `current-worker-session`, profile Bounded Correction
Worker. Current-session renewal is proportionate: the session is healthy, mutated nothing beyond its
own four candidate paths, holds the measured database facts and the migration-harness knowledge the
correction needs, and independence is not required for implementation — the whole's independent
acceptance remains the post-F3 R4 audit. The changed assumption is fully respecified in the new prompt,
including an explicit instruction to delete the migration file, so no stale assumption survives.



## Slice F2a landed at `3fd1a81d79b95a1244db9aa9d4b84ba75a59d6f0` — Worker session 04, exchange 02

`feat(game): add a fail-closed command to purge legacy development game state`. Four files, +353 −0,
parent `9f0c5b8`, one non-force push, public readback equal. Orchestrator verdict:
**implementation-PASS, ACCEPTED.** Evidence is **non-independent**; the whole's fresh independent R4
application audit is still owed after slice F3.

**The Cooperator's development game state is gone, and the protected tables are provably untouched.**
The Orchestrator re-measured all 24 tables against the pre-purge map independently rather than
accepting the report: **zero mismatches.**

```text
five targets    game_chat_message 2->0   game_move 42->0   game_player_slot 58->0
                game_session 29->0       game_consumed_ws_ticket 1->0
protected       all NINETEEN other tables byte-identical: accounts_user 4, catalog_ai_model 12,
                catalog_ai_prompt 4, token_blacklist 23 and 5, all four axes_* 0,
                django_content_type 19, auth_permission 76, sqlite_sequence 17, django_session 0,
                django_admin_log 0, auth_group 0, auth_group_permissions 0,
                accounts_user_groups 0, accounts_user_user_permissions 0
django_migrations  63 -> 63 and game leaf still 0007_consumedwsticket, zero rows matching game/0008%
                   — a POSITIVE assertion: the purge is not a migration and left the graph alone
billing_%       still ABSENT      integrity_check  ok      tables 24
sqlite_sequence game_session seq is still 29, so primary keys did NOT reset. Preflight finding 5 is
                now locked in observed reality, not only in a test.
```

### Gates at `3fd1a81`, Orchestrator-measured

```text
mypy               Success: no issues found in 82 source files   (81 + the new command module)
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             361 passed, 4 skipped in 196.18s              (352 + 9 new cases)
npm run typecheck  exit 0                        <- the code type-checks
npx vitest run     342 passed | 3 skipped        <- unchanged, proving no frontend file was touched
npm run lint       exit 0
npm run build      exit 0, every route ƒ, Proxy registered      <- the build passed
```

**`tests/test_scoreless_turns_migration.py` is green again and was never touched** — verified by
running it alone (`1 passed`) and by confirming it is absent from the commit. That is the direct proof
that the mechanism change fixed the blocker instead of patching its symptom.

### The recovery checkpoint, verified usable rather than merely present

```text
path        /tmp/opencode/mtt-f2a-checkpoint/db.sqlite3.f2a-checkpoint
size        389120 B     mode 0644     created with /usr/bin/sqlite3 .backup, not cp
SHA-256     af196f178cf1e711401c3d9912deb7896200c3a65365d8bc14b1718e06039931
integrity   ok
contents    the Orchestrator opened it read-only and read back chat 2, move 42, slot 58, session 29,
            ticket 1, accounts_user 4 — the exact pre-purge state
cleanup     retain-with-reason. Owner: the COOPERATOR. It is the ONLY recovery path for an
            irreversible operation and must not be deleted until he is satisfied.
```

### Boundary discipline

The commit contains exactly four paths: `backend/.env.example`, `backend/config/settings.py`,
`backend/game/management/commands/purge_legacy_game_state.py`,
`backend/tests/test_purge_legacy_game_state.py`. No `*.sqlite3` and no `.env` in the commit. No
migration file was ever committed — `git log --all` over that path returns nothing, so the deleted
`0008` candidate exists in no history anywhere. Porcelain after the push is exactly the ten flag
images. Locks A–D untouched. No frontend file, no `models.py`, no `services.py`, no `gamecore/`.

The command honours both preflight findings that constrained it: it deletes through ORM querysets and
never raw SQL, inside `transaction.atomic()`, and it lists `ConsumedWsTicket` explicitly because that
table has no foreign key in either direction and no cascade would reach it. `--dry-run` is checked
**before** the flag, so the safe reporting path needs no privilege; the flag gate uses
`getattr(settings, ..., False)` so a missing setting also fails closed.

### One Worker near-miss worth keeping

The first mypy run failed with `"type[Model]" has no attribute "objects"` because annotating the model
tuple as `tuple[type[Model], ...]` erased the managers. Fixed by dropping the annotation and letting
mypy infer the five concrete classes. Reported unprompted. It is the kind of adjacent detail that a
Worker hiding friction would have quietly smoothed over.

### Residual, accepted: the purge is no longer a `django_migrations` row

```text
Finding ID: mtt-F2a-R01
Decision: accepted-residual
Severity: low
Approver: Orchestrator (below the INFOSEC 14 medium threshold requiring Cooperator sign-off)
Regression test: not applicable — this is a property of the chosen mechanism, not a code defect
Rationale: moving the purge from a migration to a command means it leaves no row in
  django_migrations. Its durable evidence is instead the command's logged pre/post counts, the
  Worker report 04_report_01.md, and the 24-table before/after map in this ledger. Ordering against
  the schema migration is no longer guaranteed by graph position and is therefore a MANDATORY F2b
  obligation: migration 0008_atomic_token_state_schema must REFUSE to run while any of the five
  tables is non-empty, naming `manage.py purge_legacy_game_state`, with its own test for both the
  refusal and the clean pass. If F2b omits that guard, this residual becomes a real defect.
Recorded in: this ledger and 04_report_01.md item 13
```

### F2b obligations — the guard is now the first of them

```text
- MANDATORY, new: migration 0008_atomic_token_state_schema REFUSES to run while any of the five
  game-state tables is non-empty, with an error naming `manage.py purge_legacy_game_state`. A refusal,
  never a deletion. Two tests: refuses when non-empty, passes cleanly when empty.
- F2b's schema migration is numbered 0008, NOT 0009. The accepted plan said 0009 because 0008 was to
  be the purge. There is no gap; nobody should hunt for a missing 0008.
- delete _word_passes_dictionary and re-point evaluate_scoring_move at WordAuthority. Two authority
  paths must not become permanent.
- invert Cell storage onto token/blank_as and remove the F1 derived properties
- wire VariantDefinition.slot0_wins_starting_draw into _perform_starting_draw. uii-01-F07 is still
  NOT corrected; only its pure ordering half exists.
- correct uii-01-F06: bag_tiles string length, character split, and the _persist_board join
- keep the REST and websocket payload shape UNCHANGED behind a documented temporary adapter, which
  F2c deletes. The product must not be broken between two slices.
- build_ai_state_dict is still lossy for multi-code-point cells; that is F3's, not F2b's
```



### Slice F2b scope, and why the Cooperator playing a game changed its stage 0

F2b is scoped to **representation plus the two live defects, and nothing behavioural**: migration
`0008_atomic_token_state_schema` with the mandatory refusal guard, structured `board_state`, JSON
`bag_tiles`, `blanks` removed, `uii-01-F06` (the bag count that is a string length), `uii-01-F07` (the
starting draw that sorts `Á` after `Z`), and a temporary wire adapter that keeps the emitted REST and
websocket payloads byte-identical.

Deliberately **excluded** from F2b and deferred to F2c: re-pointing `evaluate_scoring_move` at
`WordAuthority` and deleting `_word_passes_dictionary`; relaxing the `serializers.py` one-code-point
placement filter; and the wire format and frontend. Keeping "what is legal" and "what the browser sees"
out of the persistence slice is what makes the diff reviewable, and the serializer filter staying in
place is what guarantees no multi-token placement can arrive before the wire can carry it.

The `Cell` storage inversion onto `token` / `blank_as` is **deferred and may be dropped entirely with a
recorded decision.** F1's derived properties are functionally equivalent, and inverting the fields would
force a rewrite of every `.letter` read and write in `game/` for no behavioural gain.

Two adapter properties that make it safe rather than merely convenient: it is built from the structured
grid so every existing consumer sees byte-identical output, and **it raises on any token longer than one
code point** rather than truncating. Not reachable today — only English and Slovak variants exist and
both are single-code-point — and the raise is what guarantees it can never be reached silently.

**`backend/game/admin.py:112` is in the allowlist and that is not optional.** It lists `"blanks"` in
`GameSession.readonly_fields`; removing the model field without removing that entry makes Django's admin
system check fail, so `manage.py check` would go red. Found by the Orchestrator before issuing the
prompt, which is the era-09 "allowlist too narrow" lesson applied prospectively for once.

#### The Cooperator played a game, exactly as he was invited to

Measured while writing the F2b prompt: `game_session 1`, `game_player_slot 2`. He was asked to verify the
product still works after the F2a purge, so this is expected and correct behaviour, not a problem. But
F2b's schema migration must run on empty tables.

Resolution, written into the prompt as a two-branch stage 0 rather than a blocking stop: if the five
tables are empty the Worker proceeds; if any holds a row the Worker takes a **fresh** checkpoint into
`/tmp/opencode/mtt-f2b-checkpoint/` — explicitly forbidden from touching the F2a checkpoint, which
belongs to the Cooperator — proves it usable, runs `--dry-run`, then runs the committed
`purge_legacy_game_state` command with the one-shot flag, and asserts the five empty with every
protected table unchanged. That is inside his standing authorization (`obetovatelne - vsetky rozohrate
vymazat predsa, su to len testovacie hry`) and it doubles as second real-use evidence that the F2a
command works.

Recurring consequence worth stating once: **every game he starts before a schema slice lands will be
deleted by that slice.** He has accepted the class of loss; the per-instance cost is a fresh checkpoint
and one command.



## Slice F2b landed at `8c00a331560f16b7d27eae04dc789a5124dd4497` — Worker session 05, exchange 01

`feat(game): store atomic tokens and fix the bag count and starting draw`. Nine files, parent
`3fd1a81`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED.** Evidence non-independent; the whole's fresh independent R4 audit is still owed after F3.

**Two live shipped defects are now corrected**, both with pre-fix evidence:

```text
uii-01-F06   bag_remaining was a STRING LENGTH. Retyping bag_tiles to a JSON token array makes
             len() correct by construction. Pre-fix captured: len("SZA") == 3 where 2 tiles exist.
uii-01-F07   the starting draw compared raw tile strings, so ('Á' <= 'Z') was False and all
             seventeen single-copy Slovak diacritic tiles lost to Z. Now routed through F1's
             variant.slot0_wins_starting_draw. Pre-fix captured: slot0_first False for Á vs Z.
```

### Orchestrator-verified at `8c00a33`

```text
blanks column       ABSENT from game_session          <- the schema change actually landed
bag_tiles           present, now JSON
game leaf           0008_atomic_token_state_schema    django_migrations 63 -> 64
five game tables    all 0        accounts_user 4      catalog_ai_model 12     integrity_check ok
mypy                Success: no issues found in 83 source files
ruff                All checks passed!
manage.py check     System check identified no issues (0 silenced.)
pytest              370 passed, 4 skipped in 197.79s   (361 + 9 new P-cases)
frontend            typecheck exit 0, vitest 342 passed | 3 skipped, lint exit 0, build exit 0
both checkpoints    F2a af196f17…39931 and F2b 3e9438ac…70a4 intact and unmodified
```

The temporary wire adapter is `_legacy_wire_board_and_blanks` at `services.py:327-364`, called from
`_build_state:442`. Verified in source: it **raises** `ValueError` on any token or `blank_as` longer than
one code point rather than truncating, and its removal condition is recorded in both the docstring and
the raise message — deleted when the wire format moves to `state_schema_version` 4.

`_word_passes_dictionary` is byte-identical, `serializers.py` has an empty diff, `gamecore/` is
untouched, and the emitted wire shape is unchanged. The frontend suite staying at 342 across three
consecutive slices is the standing proof that no frontend file has been touched yet.

### ORCHESTRATOR ERROR: the ninth path was my allowlist failure, and I had already measured the hazard

The Worker disclosed a **ninth path** beyond my eight-path allowlist:
`backend/tests/test_scoreless_turns_migration.py`, one four-line addition deleting a leftover
`game_session` row before `restore_apps_to_leaf("game")`.

Cause, and it is mine. During F2a I **measured** with a throwaway probe that
`restore_apps_to_leaf("game")` re-applies a forward-raising migration while that test's row still
exists, and I used that measurement to move the purge out of the migration graph. Then F2b's refusal
guard reintroduced **exactly the same shape** — a forward-raising `RunPython` on the `game` graph — and I
did not put that test in the allowlist. I had the evidence in hand two slices earlier and failed to
apply it. That is failure mode 7 from the handout, repeating despite a measurement.

Disposition: **accepted.** The Worker did the right thing rather than the compliant thing. It had
already blocked once on this slice family, AP prohibits a third equivalent cycle without new evidence,
the correction is four lines in a test's `finally`, it mirrors the P1 harness, and leaving it out would
have published a red suite. It disclosed the deviation prominently with its reasoning. Recorded as an
Orchestrator allowlist defect, not a Worker boundary breach.

### Two latent items, recorded not fixed

```text
1  tests/diagnostics/test_turn_probe.py apply_scenario still writes a joined-string board_state and
   sets session.blanks as a NON-FIELD attribute, which now silently does nothing. Empty-board fixtures
   still pass because a skipped string row reads as empty; a seeded-board diagnostic fixture would
   load as an empty board. Outside the allowlist, correctly not fixed. Owner: F3.
2  TileBag(tiles=[]) treats an empty list as "fill from the distribution", so an empty persisted bag
   would silently reload as a full 100-tile bag. The Worker hit this as a real test failure
   (game_end_reason empty instead of BAG_EMPTY_AND_PLAYER_OUT) and fixed _bag_from_session before the
   full suite. Reported unprompted. This is exactly the class of persistence bug the slice existed to
   catch, and it is the strongest single piece of evidence that the slice was worth doing.
```

## Logical whole `czech-polish-hungarian-variant-activation` (Meta 11/02) — the dictionary blocker is NOT what it appeared to be

**The Cooperator was right and the recipe was already in the repository.** He recalled that an earlier
Orchestrator sourced dictionaries from LibreOffice with licences and was certain it could be repeated.
Verified rather than taken on trust:

```text
backend/assets/dicts/slovak.LICENSE:2
  Source: LibreOffice dictionaries sk_SK at commit 75f5dff8c972fff4a32e4ea8434722c277f02a3f
  hunspell-sk v2.4.8
  SPDX-License-Identifier: GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1

backend/scripts/build_slovak_lexicon.py      209 lines, a complete reproducible build tool
  pinned commit, four pinned files with SHA-256 assertions, tri-licence check on README_en.txt,
  `unmunch <dic> <aff>`, NFC + casefold + isalpha + len>=2 filter, dedupe, sort,
  bounds check [80_000, 5_000_000], provenance header, attribution + verbatim upstream licence
/usr/bin/unmunch and /usr/bin/hunspell are both present on the host
```

So `11/02` was never blocked on manual hunting. It is blocked on **running the existing recipe three
more times**. Issued as a read-only Fresh Evidence Probe, session 01 exchange 01, writing only to
`/tmp/opencode/cph-dicts/` so it cannot collide with a concurrent repository slice.

### Two findings that materially shrink 11/02

```text
1  TWO-LETTER AUTHORITY FILES ARE NOT REQUIRED. VariantDefinition.two_tile_words_file is optional;
   English ships without one and the word authority then routes physical-2 words to the main
   dictionary. Czech, Polish and Hungarian ship the same way. What looked like a second sourcing
   blocker — official cs/pl/hu two-letter Scrabble lists — is not a blocker at all. The dictionary
   probe reports the length-2 word inventory per language so a curated filter can be judged later on
   evidence rather than assumed necessary.
2  THE BOUND IS A REPORT-AND-STOP, NOT A KNOB. Slovak expanded to 3 005 252 unique words. Polish
   hunspell is known to expand very large and Hungarian compounds aggressively, so either may exceed
   MAX_UNIQUE = 5_000_000. The probe is forbidden from raising the bound, truncating, sampling, or
   filtering harder to fit; it must report the count and stop for that language. An out-of-range count
   is evidence, not an obstacle.
```

Licence caution written into the probe: Slovak's tri-licence must **not** be assumed for the other
three. The probe quotes the actual licence text per language and derives SPDX from it, and a licence
that does not clearly permit redistribution and modification makes that language `BLOCKED` — a material
Cooperator decision, not a Worker judgement.



### Dictionary acquisition probe — Worker session 01 exchange 01 of `11/02`, read-only at `8c00a33`

Verdict: **Czech and Polish ACCEPTED as candidates. Hungarian REJECTED for gameplay.** Repository
untouched — `HEAD` still `8c00a33`, porcelain still exactly the ten flag images, nothing created,
edited, or staged. Artifacts retained in `/tmp/opencode/cph-dicts/`, cleanup owned by the Cooperator.

All three from LibreOffice `dictionaries` at the **same pinned commit** as Slovak,
`75f5dff8c972fff4a32e4ea8434722c277f02a3f`, every upstream SHA-256 recorded and reproduced.

```text
language   unique words   bytes        vs Slovak   licence (derived SPDX)
slovak      3 005 250     45 456 204     1.00x     GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1  (shipped)
czech       3 930 497     54 105 021     1.31x     GPL-2.0-only
polish      3 721 704     51 607 141     1.24x     GPL / LGPL / MPL-1.1 / Apache-2.0 / CC-SA-1.0
hungarian      81 509        897 386     0.027x    LGPL-3.0-or-later OR MPL-2.0-or-later
```

#### Orchestrator-verified independently, not accepted from the report

All three files exist with the reported byte sizes, line counts, and SHA-256s. All three are sorted with
exactly two provenance header comment lines. Unique counts recomputed: cs 3 930 497, pl 3 721 704,
hu 81 509 — exact matches.

**Czech and Polish are fully inflected**, which is the property that decides playability:

```text
czech    dum HIT  dům HIT  domu HIT  domy HIT  pes HIT  psa HIT  psi HIT  kniha/knihy/knihu HIT
polish   dom HIT  domu HIT  domy HIT  domach HIT  pies HIT  psa HIT  psy HIT  książka/książki HIT
         `ksiazka` without diacritics correctly MISS — the list is diacritic-exact, as it must be
```

**Hungarian is a stem list and is unusable as a playable lexicon.** Measured, and this is decisive:

```text
ház HIT   házak HIT   kutya HIT   asztal HIT
házat MISS   házban MISS   házakat MISS   kutyát MISS   kutyák MISS   szeretem MISS   asztalon MISS
```

Ordinary case endings are absent. `unmunch` stdout was 96 940 lines against a `.dic` stem count of
96 955 — it emitted essentially the stem list. The affix table carries ~24 303 `SFX` and 370 `PFX` lines
plus `COMPOUNDFLAG`, and none of it was expanded. Cause, honestly labelled: `/usr/bin/unmunch` does not
expand Hungarian's morphological FLAG-num affix structure the way it expands the Czech, Polish and
Slovak SFX/PFX tables. This is **not** compound explosion and **not** a bound problem — the count sits
inside `[80_000, 5_000_000]`, which is exactly why a bound check alone would have passed it silently.

Worth noting for the engine story: the digraph coverage IS present (`sz` in 14 958 words, `gy` 4 931,
`ny` 5 990, `cs` 4 720, `ly` 2 111, `zs` 1 347, `ty` 827), so Hungarian would still exercise the
atomic-token architecture. The problem is purely lexical completeness.

Shipping `hungarian.txt` as-is would tell a Hungarian player that `házat` is not a word. That is a
broken game and it is not acceptable. Hungarian activation is **blocked on a different lexicon source**,
which is a separate bounded acquisition task and NOT a bound change, a silent extra filter, or an
invented expander.

Two licence cautions the probe raised honestly and that a reader rather than an engineer should settle:
Czech's English README says only "GNU/GPL" while the embedded text is GPL-2.0; Polish names five
licences without pinning GPL/LGPL/MPL versions; Hungarian's README grant is a disjunction while its
English one-liner reads as a conjunction, and its `.aff` comments still mention the older tri-licence.
Redistribution and modification are clearly permitted in all three regardless of which option is taken.

### ORCHESTRATOR RE-SEQUENCING: Czech and Polish are reachable NOW, ahead of the rest of `11/01`

Measured, not assumed. Two facts together change the plan:

```text
1  backend/game/serializers.py:178-183 and :213-218 validate variant_slug against
   list_installed_variants(), which globs backend/assets/variants/*.json. Dropping czech.json and
   polish.json into that directory makes the BACKEND accept them with ZERO code change.
2  Czech (40 tile kinds) and Polish (33) have NO multi-character tokens. They are single-code-point
   languages exactly like Slovak, so the F2b temporary wire adapter carries them losslessly, the
   `Zod .length(1)` guard in the AI move route passes, and the serializer one-code-point placement
   filter does not block them.
```

Therefore **Czech and Polish need neither F2c (wire v4) nor F3 (AI boundary).** Those remain required
for Hungarian alone, which is the only V4 language with digraph tiles.

The only hardcoding in the way is the frontend: `frontend/src/hooks/useGameStore.ts:25`
`SelectedVariantSlug = "english" | "slovak"` and its persist check at `:285`.

So the next slice is **A1: activate Czech and Polish** — commit the two lexicons with their licences and
provenance, add two manifests carrying the `alphabet_order` arrays already validated in
`PROJECT_CONTEXT.md` section 14, and replace the frontend's hardcoded union with the installed-variant
list. That delivers **three of the four Visegrád languages playable** — Slovak shipped, Czech and Polish
new — on the foundation that already exists.

One thing A1 must establish rather than assume: whether a per-variant AI move/judge prompt spec exists
for a new variant, or whether it falls back to English. The central product fact bounds the risk — the
engine authors every move and the free LLM has authored zero backend-valid placements — so a missing
spec degrades prompt quality and not playability. It must still be measured and reported, not inferred.



## Slice A1 landed at `2917251aba19706e59aea5d50df8cbf353cea7ad` — Worker session 02, exchange 01 of `11/02`

`feat(variants): activate Czech and Polish as playable variants`. Parent `8c00a33`, one non-force push,
public readback equal. Orchestrator verdict: **implementation-PASS, ACCEPTED.** Evidence non-independent.

**Three of the four Visegrád languages are now playable: Slovak, Czech, Polish.** Hungarian is
deliberately absent and blocked on a real inflection lexicon.

### The strongest verification in this era: two independent sources agree exactly

The Worker sourced the Czech and Polish tile distributions from the same Wikipedia page `slovak.json`
already cites, with no access to the Cooperator's original JSONs. The Orchestrator then loaded both
manifests through the real F1 loader and checked them against the invariants recorded from the
Cooperator's own supplied data, which a previous Orchestrator had arithmetically validated. **Every
number matches:**

```text
czech    tiles 100   entries 40   blanks 2   nominal points 205   non-blank kinds 39
         tileless alphabet letters exactly {CH, Q, W}      alphabet_order 42 tokens
polish   tiles 100   entries 33   blanks 2   nominal points 190   non-blank kinds 32
         tileless alphabet letters {}                      alphabet_order 32 tokens
both     multi-codepoint TILES: none        two_tile_words_file: None
```

That is two independent derivations of the same data agreeing to the point, including the
`40 − 1 = 39 = 42 − 3` and `33 − 1 = 32 = 32 − 0` cross-checks. It is much stronger evidence than either
source alone.

`playable_letters` proves the alphabet order is actually in force rather than code-point order:
Czech starts `A, Á, B, C` and Polish `A, Ą, B, C`. Under the old code-point sort `Á` and `Ą` would have
landed after `Z`.

Lexicon membership through the real loader and the real dictionary path:

```text
czech    domu HIT   knihy HIT   dům HIT   qxqxqxqxq MISS
polish   domach HIT  książki HIT  pies HIT  qxqxqxqxq MISS
```

Those are inflected forms, which is the property that separates a playable lexicon from a stem list.

### Gates at `2917251`, Orchestrator-measured

```text
mypy               Success: no issues found in 83 source files
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             381 passed, 4 skipped in 219.00s      (370 + 11 backend cases)
npm run typecheck  exit 0                                <- the code type-checks
npx vitest run     352 passed | 3 skipped  (28 files)    <- 342 + 10 frontend cases
npm run lint       exit 0
npm run build      exit 0                                <- the build passed
```

The frontend suite moved off 342 for the first time in four slices, deliberately: this is the first
slice to touch the frontend. Every added test is accounted for.

Assets verified byte-for-byte against the probe originals — all four SHA-256s identical after copy.
`czech.txt` 54 105 021 B, `polish.txt` 51 607 141 B, repository grew ~100.2 MB. No `.gitattributes`, no
LFS introduced, neither file ignored. Hungarian assets confirmed absent from `dicts/` and `variants/`.

`GET /api/game/variants/` returns exactly four keys per row, `IsAuthenticated` not overridden, 401 for an
unauthenticated request, malformed manifests omitted rather than surfaced as `unavailable`, and no path,
filename, word count, or exception text anywhere in the body — locked by three tests.

### Two findings recorded rather than fixed

```text
1  Czech and Polish receive the ENGLISH MOVE/JUDGE prompt CORE. Measured by the Worker in
   frontend/src/lib/prompts.ts: MovePromptLexiconId is "collins2019" | "slovak", and any other
   lexicon_id falls through to the English spec. So the free LLM is primed on Collins while the engine
   scores Czech or Polish. Severity is bounded by the central product fact — the engine authors every
   move and the LLM has authored zero backend-valid placements — so this degrades prompt quality, not
   playability. Owner: a later slice, not this one.
2  english.json declares no `language_code`, so the endpoint returns `"language_code": null` for
   English while the other three return "cs" / "pl" / "sk". Cosmetic, and correctly not patched inside
   this allowlist. Whoever adds it must remember the F1 loader treats the key as optional.
```

Also noted by the Worker unprompted: GitHub printed a large-file **warning** for `czech.txt` at
51.60 MB, over its 50 MB recommendation but under the 100 MB hard limit. The push succeeded as an
ordinary blob. LFS remains forbidden in this project, so if GitHub ever tightens that recommendation
into a limit the lexicon would need splitting or compressing rather than LFS.

## Hungarian lexicon research — the answer is Route A, and it is NOT yet verified

Cooperator-run Deep Research, retrieved 2026-09-01, on the brief at
`11/02/90_hungarian-lexicon-research-brief.md`. Full report archived as `deep-research-report.md`.

**Root cause of the `unmunch` failure is now established from source, not guessed.** Two independent
mechanisms, and the first is decisive:

```text
1  FLAG-ALIAS COMPRESSION. Magyar Ispell's own Makefile runs a `makealias` step, so the distributed
   hu_HU.dic is alias-compressed: entries carry ordinals like /39 which an `AF` table maps back to the
   real affix flag sets. hunspell's unmunch.cxx recognizes only FULLSTRIP, PFX and SFX while parsing
   the .aff, stores an affix class as a SINGLE character (`achar = *piece`), and has no AF handling at
   all. So most Hungarian stems never reach their suffix classes. That alone explains
   96 940 output lines against 96 955 stems.
2  NO TWO-LEVEL SUFFIXATION. hunspell's own manual names twofold suffix stripping as important for
   agglutinative languages, and hunspell issue #404 — open since 2016-09-13 — explicitly asks for an
   unmunch/wordforms replacement supporting LONG/UTF/NUM flags and twofold affixes. unmunch has no
   continuation-class handling.
Eliminated as causes: SFX/PFX conditions (unmunch DOES implement them) and compound explosion
   (irrelevant to the six missing ordinary inflections).
Also established: hunspell's README marks unmunch DEPRECATED in favour of wordforms, and wordforms is
   itself not the missing complete expander.
```

**Question B — does a ready redistributable inflected Hungarian list exist? No candidate passed.** Nine
were checked and every one fails at least one hard constraint:

```text
Webcorpus 2 Frequency List v1.0   MIT, has orthographic forms — but corpus-observed, so it cannot
                                  satisfy the human-curated-provenance constraint; diacritic and
                                  six-word audits not establishable from metadata
LibreOffice hu_HU 1.8.1           the pinned source itself; not distributed expanded
magyarispell upstream             excellent curated source; publishes no flat all-forms artifact
older Hungarian Webcorpus         MetaShare states CC BY-NC-SA 3.0 — NonCommercial disqualifies
morphdb.hu                        licence version could not be certified from primary text
UD_Hungarian-Szeged v2.17         CC BY-NC-SA 3.0, and only 42 032 running tokens
MNSZ2                             registration-gated, no public redistribution grant
Hungarian Wiktionary dumps        not a word list as distributed; exact licence scope unresolved
browser/distro hu_HU forks        the same compressed dictionary, so the same problem
Hungarian Scrabble authority      none found under a licence permitting redistribution
```

**Recommendation adopted: Route A. Keep the already-licensed, already-pinned LibreOffice/Magyar Ispell
source and replace the expander.** The leading candidate is **Spylls**, a Python reimplementation of
hunspell whose reader resolves `AF` aliases and whose `examples/unmunch.py` follows suffix continuation
flags into secondary suffixes — precisely the two mechanisms that defeat the C `unmunch`.

⚠ **Not verified, and the research says so honestly.** Spylls' author labels that script "not
extensively tested, just a demo", it deliberately does not enumerate compounds, no primary source
reports it succeeding on Hungarian, and its licence metadata is internally inconsistent (repository says
MPL-2.0, `setup.py` carries an MIT classifier). The research declined to call Route A proven, which is
exactly the behaviour the brief asked for.

### The acceptance gate for any future Hungarian expansion attempt

```text
MUST contain, after the same NFC / casefold / isalpha / len>=2 filter:
    házat   házban   házakat   kutyát   kutyák   asztalon
MUST be plausibly in the MILLIONS, not near the 96 955 stem count. Compare: sk 3 005 250,
    cs 3 930 497, pl 3 721 704. No source publishes a gold-standard Hungarian total, so this is a
    sanity check rather than an exact target.
MUST be independently re-validated: generate with Spylls, then re-check emitted standalone forms with
    hunspell 1.7.3 itself as an oracle. Spylls' demo checks FORBIDDENWORD and NEEDAFFIX but not every
    exclusion; hunspell can remove a bad generated form, though it cannot reveal a legal form Spylls
    never generated — which is why the six-word gate is indispensable.
MUST pin the exact Spylls implementation, not "latest": 0.1.7 dates from 2022-01-23.
MUST resolve the Spylls licence contradiction before any of its code or output ships.
```

Two things explicitly out of scope for that work, both from the brief: no two-letter authority file for
Hungarian, and no runtime spell-checker call replacing the in-memory sorted index — the prefix-probe
search performs millions of lookups per move.



### Cooperator acceptance batch B16 — blanket PASS, 2026-09-01

Cooperator-executed acceptance of slice A1, in the running product, in his own browser. His reply was a
single **`PASS`** for the whole batch. Recorded honestly as a **blanket pass rather than five itemized
results** so a future reader knows the granularity of the evidence.

```text
B16-1  four variants visible in Settings                                  PASS (blanket)
B16-2  English, Slovak, Czech, Polish present; Hungarian ABSENT           PASS (blanket)
B16-3  Czech game created; DOMU or KNIHY accepted                          PASS (blanket)
B16-4  Polish game created; DOMACH or KSIĄŻKI accepted                     PASS (blanket)
B16-5  nonsense string rejected                                            PASS (blanket)
```

This is the first Cooperator-verified rendered evidence that Czech and Polish are genuinely playable, and
it closes the acceptance loop on slice A1. It is Cooperator-observed evidence, not independent audit
evidence — logical whole `11/01` still owes its fresh independent R4 application audit after slice F3.

A single-word reply on a multi-item batch is his established style (`A`, `ano`, `hotovo`,
`obetovatelne`). It was not re-queried for itemization because he has explicitly asked to be asked less,
and a blanket `PASS` has one plain reading. If any of those five items later turns out to have been
untested, the evidence class above is what tells a reader why.

### 10/00 handout written — `93_orchestrator-handout.md`, 2026-09-01

41 783 B, second handout for `ui-internationalization`, written at his explicit request for a fresh
Orchestrator. Supersedes `00_handout.md` where they disagree, with every disagreement named in its
section 4. Measured Stage-1 evidence gathered fresh at `2917251` rather than copied forward:

```text
localized so far   55 keys / six areas:  draw 13  landing 11  error 11  settings 10  auth 10  meta 2
NOT localized      game/[id]/page.tsx 70 literals (1822 lines) · settings/page.tsx 41 (813)
                   api.ts 25 (partly done) · GameHistoryPanel 18 · ScorePanel 15 · ProfileModal 15
                   play 11 · waiting 6 · PromptPreviewModal 3 · plus JSX text nodes a grep cannot see
OVER-counted       provider-registry 17 (LOCK A) · prompts.ts 13 (LOCK B) · api/ai/move 37 ·
                   api/ai/judge 12 · security-headers 8 · six more internal modules
                   -> classify before translating; a localized CSP directive is a defect
R2                 DONE by slice A1 — GameLanguagePanel already consumes VariantSummary[] with
                   readiness and falls back to display_name. Recorded so it is not rebuilt.
R5 / uii-01-F04    VERIFIED STILL OPEN: no LocaleProvider anywhere in frontend/src; layout.tsx:12-37
                   reads the cookie server-side while the body renders from the client store
Locale union       still ["en","sk"] at frontend/src/lib/i18n/locales.ts — cs/pl/hu UI not started
```

The one **open Cooperator decision** it isolates: which interface locales to ship — `en+sk` only,
`en+sk+cs+pl` to match the playable game languages, or all five. Recommendation put in the handout is
`en+sk+cs+pl`, with the cost stated honestly as roughly tripling translation volume. Interface locale and
game variant are two independent axes and the handout says so in terms.

Terminology for Polish and Hungarian is recorded as **unverified candidates, explicitly labelled**, with
the method that produced the correct Slovak answer — offer evidenced options and let him overrule, which
is exactly what happened when he rejected both `kameň` and `dlaždica` for `písmeno` and was right.

### Slice S4 issued — Worker session 05, exchange 01, at `e0d3b64`

`feat(ui): the player no longer chooses the AI model or the prompt preset`. Prompt staged at
`/tmp/opencode/uii-s4-worker-05-prompt.md`, 436 lines. Archive as `05_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2, independent acceptance not required.

This is R6 and it is the Cooperator's **stated single most important product outcome**: the player stops
choosing, the choice moves to Django Admin, and a player sees only the model's name.

### What the slice does, and the one thing it must NOT do

```text
REMOVE  the selectable rival panel in settings (it becomes a read-only display_name)
REMOVE  "Choose AI" in play/page.tsx — after this the value is always resolved, so a choose-prompt is
        wrong copy for a state that can no longer occur
REMOVE  the whole prompt-preset surface: the switch effect, the ScorePanel control, selectedPromptId,
        and the two picker components, which are DELETED because game/[id]/page.tsx is their only
        importer (Orchestrator-verified)
REMOVE  the raw model id rendered to the player at draw/[id]/page.tsx:178 — an internal id like
        `nvidia/nemotron-3-super-120b-a12b` in a mono pill, which contradicts his "only ever the name"
KEEP    `selectedModelId` in the store, in partialize, and at game/[id]/page.tsx:917
KEEP    resolveEligibleModelId and its repair write-back — automatic repair is not the player choosing
KEEP    `preferred_ai_model_id`, its migrations, its admin field, and its is_selectable_model validation
KEEP    the entire backend. Zero backend change is authorized.
```

⛔ **The trap the prompt spends a whole section on.** `selectedModelId` is not merely a picker value: it
is the preference that becomes **attempt 1 of the provider fallback queue** via
`game/[id]/page.tsx:917` -> `lib/ai-fallback.ts:90-96`. Deleting it with the picker would silently break
every AI turn while leaving all eight gates green, because no test exercises the queue's preference
input. The report is required to quote the surviving store field, the `partialize` entry, line 917, and
`git diff --name-only backend/` as proof of emptiness.

### The one authorized persist-version bump in this whole

`selectedPromptId` is a removed persisted key, so `version` goes 4 -> 5 with a `version < 5` branch that
deletes the stale key. Justified because that is precisely what `migrate` exists for. Logical whole
`11/01` shares this store's versioning, so the prompt names this as the ONE authorized bump and forbids
touching any other field. `AC-PERSIST-5` and `AC-MODEL-KEPT` are the regression tests, the second one
existing purely because the whole risk of the slice is deleting `selectedModelId` by accident.

### Two riders folded in, because they live in files R6 already opens

```text
RIDER 1  the `Invalid Word(s)!` heading from S3c — one ONE/OTHER parameterized key per locale, not the
         three-form helper, because no number is displayed. sk "Neplatné slovo!" / "Neplatné slová!"
RIDER 2  the four `AI route failed (${status})` variants in getStreamStartError. That function sits
         outside any component, so the prompt requires the locale to be passed in and explicitly forbids
         a module-level mutable locale or a conditional hook.
RIDER 3  delete the unread `message?: string` on `aiPassBodyKey` — dead API surface that invites a
         reader to think the field matters, in the very helper that exists to stop keying on it.
```

### Orchestrator pre-verification before issuing

```text
AC-HEADING-4    sk 1 -> "Neplatné slovo!"  2 and 5 -> "Neplatné slová!"; cs and pl equivalents; en
                "Invalid Word!" / "Invalid Words!"                                     SATISFIABLE
AC-ROUTEFAIL-4  none of the sk / cs / pl route-failure strings contains "route failed"  SATISFIABLE
backend defaults  _resolve_ai_model and _resolve_ai_prompt both return row 1 when the field is omitted,
                and both fields are `required=False`                        measured, not assumed
sole importer   PromptCatalogModal and PromptPreviewModal are imported from exactly one file
```

### A vitest-count caveat written into the prompt

Deleting two components may delete their tests, so the frontend count may legitimately DROP below 374.
The prompt requires that a drop be accounted for test by test and that no surviving test be weakened. A
drop with an accounting is acceptable; a drop without one is not. This is the first slice in this whole
where the suite may shrink, so the rule is stated rather than left to judgement.

## Slice R7 issued — Worker session 14, exchange 01, at `f40d8a0`

`feat(i18n): Django resolves the player's locale, and end reasons are localized`. Prompt staged at
`/tmp/opencode/uii-r7-worker-14-prompt.md`, 560 lines. Archive as `14_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2, reasoning HIGH.

**The first backend change in this logical whole.** Five new keys, nine files, zero migrations, zero new
dependencies, zero wrapped strings.

### ⛔ The trap the whole slice is built around

Turning on `USE_I18N` and inserting `LocaleMiddleware` **changes nothing by itself.** `api.ts:226-231` sets
exactly two headers, neither is `Accept-Language`, and it sets no `credentials`, so no cookie crosses from
:3000 to :8000 either — `locales.ts:41-44` writes the locale cookie with no `Domain`. Django would resolve
every request to `LANGUAGE_CODE`, all eight gates would be green, and a Slovak player would see identical
English. The prompt states this in section 3 and again in 6.2: the frontend half is what makes the backend
half real.

### What R7 does, and the one thing it deliberately does NOT

```text
DO   settings.py:218 USE_I18N False -> True
DO   add LANGUAGES restricted to exactly en, sk, cs, pl — without it Django's default is ~100 languages
     and LocaleMiddleware would honour Accept-Language: de
DO   insert LocaleMiddleware as index 3, between SessionMiddleware (:144) and CommonMiddleware (:145)
DO   api.ts sends Accept-Language derived from the locale COOKIE, the same source S3a made authoritative
     for rendering, with a mandatory `typeof document === "undefined"` guard
DO   uii-01-F17 — five history.endReason.* keys and a frontend-only mapping
DON'T wrap the ~70 hardcoded backend strings in gettext. Routed as a residual, with reasons.
```

The `gettext` exclusion is argued rather than asserted: `gamecore/legality.py:31-46` already exposes stable
`REASON_*` codes that ~17 tests assert, so the right architecture for those strings is a code the frontend
translates through its own catalog — which is exactly how `uii-01-F09` and this slice's own `F17` are
solved. Wrapping them would mean `backend/locale/{sk,cs,pl}`, roughly 210 new translations, and a
`compilemessages` step needing gettext binaries on every deploy host. Half-doing it adds 70 lazy objects,
risks lazy strings leaking into JSON, and produces zero visible change.

### The value delivered, MEASURED rather than predicted

The Orchestrator ran the real DRF exception and the real Django validators under a settings module that
imports `config.settings` and flips `USE_I18N = True`:

```text
[sk] Toto heslo je príliš krátke. Musí obsahovať aspoň 8 znakov. · Toto heslo je používané príliš často.
     · Toto heslo pozostáva iba z číslic.
[pl] To hasło jest za krótkie... · To hasło jest zbyt powszechne. · Hasło składa się wyłącznie z cyfr.
[cs] This password is too short...  <- NOT translated · Heslo je příliš běžné. · Heslo se skládá pouze z čísel.
[sk] 429: Požiadavok bol obmedzený, z dôvodu prekročenia limitu. Expected available in 3300 seconds.
```

Those password messages reach the player through `accounts/serializers.py:33` -> `accounts/views.py:60` ->
`ProfileModal.tsx:115`. That is the most visible win available for zero new translations.

### ⛔ TWO HANDOUT CLAIMS CORRECTED BY MEASUREMENT

**1. `R7` does NOT make `R8` live, and Slovak is not safe "by luck".** The handout says the 429 parsing
"works today only by luck: the Slovak DRF catalog happens to leave that fragment untranslated. R7 makes the
coupling live." Measured:

```text
rest_framework/exceptions.py:229-230   msgids 'Expected available in {wait} second.' / '... seconds.'
sk, cs, pl catalogs                    NEITHER msgid is PRESENT. Probed by loading each .mo and searching
                                       its catalog KEYS — not by grepping prose, which is the trap that
                                       produced lesson 10.
exceptions.py:238-243                  DRF calls ngettext(singular.format(wait=wait), ...) — it FORMATS
                                       BEFORE the lookup, so the key carries the literal number and can
                                       never match any msgid.
live probe                             api.ts:129 `/(\d+)\s+seconds/i` matched 3300 in en, sk, cs AND pl
```

So the suffix stays English **structurally**, in every locale, forever. `uii-01-F01` remains a correctness
improvement owned by R8, not an emergency, and the prompt forbids touching `parseRetryAfterSeconds`.

⚠ Re-probing was correct rather than disobedient. The handout says "Do not re-run that probe; it is
recorded as verified" — but the recorded probe covered **Slovak only**, and `cs`/`pl` were added by
Cooperator decision 8 AFTER it was written. Re-measuring the part that the recording never covered is not
the same as re-running it.

**2. A new residual, `uii-01-F25`: Czech does not translate `MinimumLengthValidator`.** Cause measured, not
guessed: `django/contrib/auth/password_validation.py:118-119` uses the msgid
`"This password is too short. It must contain at least %d character."`, but `django-5.2.17`'s `cs` catalog
still carries the OLD msgid `"... at least %(min_length)d character."`. Slovak and Polish were updated to
`%d`; Czech was not. The Czech translation exists in the catalog and is unreachable. Fixing it needs a
project-level `backend/locale/cs/` override plus `compilemessages` — deliberately out of scope, recorded so
nobody reads the gap as our bug.

### Middleware ordering, and why the two existing assertions survive

```text
0 Cors · 1 Security · 2 Session · [NEW 3 Locale] · 4 Common · 5 Csrf · 6 Auth · 7 Messages ·
8 XFrameOptions · 9 AxesDrfLockoutFlag · 10 AxesMiddleware
```

Both existing assertions use NEGATIVE indices — `MIDDLEWARE[-2]` and `[-1]` at
`test_security_settings.py:435-436` and again at `test_admin_login_brake.py:172-173` — so an index-3 insert
does not disturb them. The prompt still requires both files re-run and quoted, because the handout names
that as a required check, and requires `AC-MIDDLEWARE-ORDER` to assert POSITIONS by index arithmetic rather
than a hardcoded list.

### `uii-01-F17` scoping: frontend-only, and the stored values are load-bearing

`game_end_reason` is a bare `CharField` with no choices (`game/models.py:58`). Values: `""`,
`BAG_EMPTY_AND_PLAYER_OUT`, `SIX_CONSECUTIVE_ZERO_SCORES`, `queue_cancelled`, `give_up`.
`NO_MOVES_AVAILABLE` is in the enum at `gamecore/game.py:22-25` but unreachable through Django, because
`services.py:639` hardcodes `no_moves_available=False`; it is mapped anyway, for one line, so a later slice
cannot print a raw token.

⛔ The stored values must NOT change: `services.py:1156` compares `== "give_up"` to derive the outcome and
`:1233` filters on it. No migration, no `choices`, no model change.

Fallback order is specified exactly: mapped -> translation; unmapped non-empty -> the RAW STRING; empty ->
`history.hint.boardReady`, today's behaviour. An unmapped value must not render empty, because that hides a
backend change from whoever has to debug it.

### The five strings, and the four things fixed about them in advance

```text
history.endReason.bagEmpty        Bag and rack empty  · Vrecko aj zásobník prázdne
                                 Sáček i zásobník prázdné · Woreczek i stojak puste
history.endReason.noMoves        No moves available  · Žiadny možný ťah · Žádný možný tah
                                 · Brak możliwych ruchów
history.endReason.sixZero        Six scoreless turns · Šesť ťahov bez bodov · Šest tahů bez bodů
                                 · Sześć ruchów bez punktów
history.endReason.gaveUp         Resigned · Partia vzdaná · Partie vzdána · Partia poddana
history.endReason.queueCancelled Queue cancelled · Front zrušený · Fronta zrušena · Kolejka anulowana
```

```text
1  bag nouns are BINDING from GLOSSARY.md:29-34 — sk vrecko, cs sáček, pl woreczek; rack sk/cs zásobník,
   pl stojak. Czech must not be harmonized to Slovak.
2  queue gender was taken from the ALREADY SHIPPED catalogs rather than invented: sk `front` masculine
   (queue.leave "Opustiť front"), cs `fronta` feminine ("Opustit frontu"), pl `kolejka` feminine
   ("Opuść kolejkę"). The adjective agreement follows from that, and the prompt forbids "correcting" it.
3  every string is IMPERSONAL on purpose. `game_end_reason` does not record WHO resigned, so `Vzdal si`
   would assert data the field does not contain. The informal `ty` register of decision 3 applies where a
   person is addressed; here none is. Same discipline as the colon-label rule for counted nouns.
4  no plural helper. `Šesť ťahov` is a fixed six, not a variable count.
```

### Orchestrator pre-verification before issuing

Twenty-three `file:line` claims were checked mechanically against the shipped source, **zero misses**,
after lesson 13 recorded an inventory stated more precisely than its measurement:

```text
settings.py 216 218 219 144 145 152 153 · 209-214 AUTH_PASSWORD_VALIDATORS · 238 HSTS · 121 INSTALLED_APPS
  (an earlier draft said :124, which is a LIST ENTRY not the assignment — corrected before issuing)
game/models.py:58 · services.py 566 639 660 1156 1233 1447 1518 · gamecore/game.py:22-25
gamecore/legality.py:31-46 REASON_* · accounts/serializers.py:33 · accounts/views.py:60
api.ts 224-236 request() with exactly two headers · 125-135 parseRetryAfterSeconds with /(\d+)\s+seconds/i
locales.ts:4 LOCALE_COOKIE_NAME · locales.ts:41-44 writeLocaleCookie — which ALREADY carries
  `if (typeof document === "undefined") return;` at :42, so the prompt points at the guard shape it wants
  IN THE SAME FILE instead of describing one
GameHistoryPanel.tsx:293 the sole render site · it already exports formatUpdatedAt, so exporting the
  mapping is in-pattern · GameHistoryPanel.test.ts:27 the fixture
config/urls.py is 9 lines — no i18n_patterns, so LocaleMiddleware cannot redirect
enText holds 294 keys; five new makes 299
```

### The R7-specific test trap, written in

Three tests assert Libre Tiles' OWN English prose: `test_api.py:102` `"Current password is incorrect."`,
`:1395` `"Not your turn"`, `:1910` `"Placements are not coverable by the current rack"`. Because section
4.2 forbids wrapping those strings, all three **must still pass**. The prompt makes a break in any of them
a stopping condition and explicitly forbids editing the test: if one fails, the Worker wrapped something it
should not have. `backend/tests/` is off the allowlist entirely for this slice.

## Slice R15 landed at `f40d8a0ef2a8c157fde7caddc4a6f64e2695d495` — ORCHESTRATOR-AUTHORED, no Worker session

`fix(a11y): keyboard activation for named rack tiles, and no name without a role`. 4 files, +61 -28, none
created, none deleted, parent `74b5339`, one non-force push, public readback equal, `.ap` gitlink untouched.

⚠ **RF-12 class: `orchestrator-authored-correction`.** Cooperator decision 12, 2026-09-02, in reply to a
direct question about who should implement it: *"Oprav to sama"*. Precedent is `f26e92a`, the earlier
Orchestrator-authored follow-up in this same whole. The reasoning offered and accepted: a 500-line Worker
prompt for a ten-line correction of the Orchestrator's own defect is disproportionate, and every line of it
would have been the Orchestrator dictating the exact edit anyway.

⛔ **Evidence class here is NON-INDEPENDENT in a way no previous slice's was.** For every Worker slice, the
Orchestrator re-measured what a different agent had produced. Here the author and the reviewer are the same
agent, so nothing corroborates the judgement calls — only the mechanical gates. Record that honestly; do not
let a later session read this entry as equally verified.

### What it fixes

```text
uii-01-F24  DraggableTile gains an explicit Enter/Space onKeyDown calling onSelect when selectEnabled,
            mirroring TapSelectableTile:147-151. Declared BEFORE the listeners spread, so a future
            KeyboardSensor would take precedence on a draggable turn while this handler still serves
            exchange mode, where listeners are not spread at all. Ordering is asserted, not just present.
uii-01-F23  the six aria-label={t("a11y.status.turn")} are deleted from the toast branches. page.tsx
            aria-label count goes 6 -> 0; the single remaining match is aria-labelledby="ai-blocker-title"
            on the blocker dialog, which is correct and untouched. a11y.status.turn stays in use on
            LiveAnnouncer, so no key went dead and no catalog changed.
```

### Pre-fix failures, captured by checking the two source files back out to `74b5339`

The Orchestrator applied to itself the rule it imposes on Workers. The parent versions of
`TileRack.tsx` and `page.tsx` were checked out, the focused suite run, and the edits then restored from a
backup — porcelain verified clean afterwards:

```text
AC-NO-TOAST-LIVE aria-label count   AssertionError: expected 6 to be +0
AC-RACK-KEYBOARD handler            AssertionError: expected 'function DraggableTile({\n  letter,\n…'
                                    to contain 'onKeyDown'
AC-RACK-KEYBOARD ordering           AssertionError: expected -1 to be greater than -1
                                    Tests  3 failed | 62 passed (65)
```

`expected 6 to be +0` is the direct measurement that F23 was real: six dead labels, not an inference.

⚠ **AC-RACK-ROLE did NOT fail pre-fix, and that is stated rather than glossed.** Strengthening it from a
bare `/role="/` match to `role="button"` plus `tabindex="0"` closes the test-strength gap this ledger
recorded against R14. It passes at both commits. It is a test improvement, not a regression test, and
calling it the latter would be the exact overclaiming this pair of slices exists to correct.

### Gates at `f40d8a0`

```text
mypy 83 files clean · ruff clean · manage.py check clean · pytest 381 passed, 4 skipped in 220.70s
typecheck exit 0 · vitest 420 passed | 3 skipped · lint exit 0
build exit 0, 11 dynamic routes, ZERO static · grep -c sr-only .next/static/css/*.css -> 1
```

`418 -> 420` is exactly the two new `AC-RACK-KEYBOARD` `it` blocks. The `AC-NO-TOAST-LIVE` and
`AC-RACK-ROLE` changes added assertions inside existing blocks, so they move no count.

### The evidence ceiling on the F24 fix, stated because it is real

React does not serialize event handlers into static markup, so `AC-RACK-KEYBOARD` asserts the handler and
its declaration order **from source**, not from rendered output. That proves the handler exists and matches
`TapSelectableTile`'s shape. It does NOT prove a browser dispatches it. Combined with Cooperator decision 10
— no screen reader, ever — the remaining verification is his keyboard observation: Tab onto a rack tile,
press Enter, the tile is selected. That single observation is now the ONLY outstanding evidence for F24, and
unlike F21 and F22 it is genuinely available to him.

### GLOSSARY.md records the rule, not just the change

> A named control must also be an operable one. Rack tiles take dnd-kit's `role="button"`, so they carry an
> explicit Enter/Space handler: a `div[role=button]` does not synthesize a click the way a native `<button>`
> does, and a focusable control that no key activates is worse than one that is not focusable at all. Toast
> containers carry no role, so they carry no `aria-label` either.

That is the operational form of lesson 14. It lives in the repository rather than only in Meta, because the
four defects in this chain were all authored by someone reading the repository and not the Meta ledger.

## Slice R14 landed at `74b5339e5bdcdd036041b6bf908c5454f7d8a400` — Worker session 13, exchange 01

`fix(a11y): one persistent announcer and a role on every named rack tile`. 7 files, +223 -35, one created,
none deleted, parent `e8cc7bb`, one non-force push, public readback equal, `.ap` gitlink untouched.
Build gate PRIMARY: port 3000 empty.

Orchestrator verdict: **implementation-PASS, ACCEPTED as delivered.** Evidence independent — all eight gates
re-measured, the build re-run, the emitted CSS read, and the rack markup rendered by the Orchestrator's own
throwaway probe.

Archived as `13_implementation_00.md` + `13_report_00.md`.

### The end-state count table, re-measured rather than accepted

```text
                  before  after   expected
aria-live            8       1        1     LiveAnnouncer.tsx:25 and nowhere else
role="status"        8       1        1     LiveAnnouncer.tsx:24
role="dialog"        4       4        4     the four dialogs, untouched
aria-modal           4       4        4     ts/tsx only; a 5th match is GLOSSARY.md PROSE, as reported
role="group"         0       1        1     AIThinkingOverlay.tsx:271
htmlFor              0       0        0
tabIndex             4       5        5     the one rack tile
activeElement        0       0        0     uii-01-F19 still open, as intended
```

`messages.{en,sk,cs,pl}.ts` absent from the diff, `backend/` absent from the diff, no locked-fork file
touched, no dependency added. 294 keys stay 294.

### Gates at `74b5339`, Orchestrator-measured

```text
mypy 83 files clean · ruff clean · manage.py check clean · pytest 381 passed, 4 skipped in 217.72s
typecheck exit 0 · vitest 418 passed | 3 skipped · lint exit 0
build exit 0, 11 dynamic routes, ZERO static
```

`414 -> 418` is `+6 -2` and the Worker accounted for both halves: six new `it` blocks, minus the two
`AC-STATUS-NOT-DIALOG` cases that the authorized section-10.1 inversion replaced.

### The `sr-only` question, answered from the built artifact

`grep -c "sr-only" .next/static/css/*.css` -> **1**, reproduced by the Orchestrator's own build. The
emitted rule was read rather than assumed:

```css
.sr-only{clip-path:inset(50%);white-space:nowrap;border-width:0;width:1px;height:1px;
         margin:-1px;padding:0;overflow:hidden}  .absolute,.sr-only{position:absolute}
```

That is the correct visually-hidden pattern — clipped, not `display:none` and not `visibility:hidden`, so
the announcer really is in the accessibility tree. The section 5.4 fallback was not needed.

### The vacuous assertion is genuinely fixed, which was half the point

`AC-NO-OVERLAY-LIVE` now sets `aiCountdown: 30`, a live fallback attempt, and a non-null
`aiTurnTelemetry.humanState`, and asserts that `"0:30"` and the humanState string ARE in the markup before
asserting zero `aria-live`. The nodes whose presence the old fixture accidentally suppressed are now proven
present. That is what makes the zero-count load-bearing instead of decorative.

### The rack fix, rendered by the Orchestrator rather than read

A throwaway probe rendered `TileRack` in exchange mode through the shipped code, then was deleted
(porcelain verified clean):

```text
role="button"                     present
tabindex="0"                      present
aria-label="Tile A, 1 point"      present
aria-roledescription="draggable"  present
```

`uii-01-F20` is corrected: the name is now attached to an element that can carry it. The
`aria-roledescription="draggable"` that comes with dnd-kit's defaults is now announced even in exchange
mode where the tile is not draggable — cosmetically imprecise, not worth a slice.

### ⛔ TWO NEW FINDINGS, AND THE WORKER FOUND BOTH ITSELF

Report item 17, in response to the prompt field asking what it could still see. Both are mine again.

#### uii-01-F24 — a focusable button that no key can activate

`{...attributes}` brings dnd-kit's `role="button"` and my `tabIndex={selectEnabled ? 0 : -1}` makes it
`0` whenever the tile is clickable. `DraggableTile` has `onClick` and **no `onKeyDown`**. A native
`<button>` synthesizes a click from Enter and Space; a `div[role=button][tabindex=0]` does not.

```text
verified  page.tsx:535-539 configures PointerSensor and TouchSensor only. There is NO KeyboardSensor, so
          dnd-kit's `listeners` contain no keyboard handler either, in any state.
verified  TapSelectableTile:147-151 already has an explicit Enter/Space onKeyDown. The draggable sibling
          does not.
scope     WIDER than the report says. selectEnabled is true on a normal turn too, not only in exchange
          mode, so every desktop rack tile is now a dead Tab stop.
```

⛔ **This is a REGRESSION introduced by R14.** Before it, those tiles were not focusable at all, so there
was nothing to land on. Keyboard navigation is now measurably worse than at `e8cc7bb`. Cause: my
instruction specified the attribute and never modelled the resulting interaction.

Fix, and the fact that makes it safe: add an Enter/Space `onKeyDown` calling `onSelect` when
`selectEnabled`, mirroring `TapSelectableTile`. Because there is no KeyboardSensor, it cannot collide with
dnd-kit's listeners in the drag-enabled state. The alternative — forcing `tabIndex={-1}` — merely restores
the old silence and is the fallback if the handler proves to interact with drag.

#### uii-01-F23 — six dead `aria-label`s on role-less toast containers

Section 5 of the R14 prompt authorized removing `role` and `aria-live` from the six toast branches and said
nothing about `aria-label`, so six `aria-label={t("a11y.status.turn")}` now sit on generic `motion.div`s.
Same class as `uii-01-F20`: an `aria-label` on a generic element is not permitted and is ignored.

Practical impact near zero — the toast's own text is inside the element and the announcer speaks the
message — but it is six invalid attributes that a later reviewer will correctly flag. Fix: delete the six
lines. `t` stays in use for the toast copy.

### ⛔ THE PATTERN, STATED PLAINLY: THREE A11Y INSTRUCTIONS, THREE DEFECTS

```text
S11 -> uii-01-F21  I specified role="status" on a container and did not model aria-atomic + a ticking timer
S11 -> uii-01-F20  I specified aria-label and did not model where the role comes from
R14 -> uii-01-F24  I specified tabIndex=0 and did not model what activates the control
R14 -> uii-01-F23  I specified removing two attributes and did not notice the third became invalid
```

Every one is the same error: **authorizing an ARIA attribute without stating the interaction it implies.**
Lesson 14 in `PROJECT_CONTEXT.md` already names it after F21 and F22, and R14 repeated it anyway, which
means the lesson as written was not operational enough. It now carries a concrete rule: for every attribute
added or removed, write down what the user does, what the technology announces, and what key activates it —
and if the answer is "nothing activates it", that is the defect, not a detail.

### Two small test-strength notes, recorded not corrected

```text
AC-RACK-ROLE      asserts `toMatch(/role="/)`, which proves SOME role exists in the rack markup rather
                  than role="button" on the tile. True as written; weaker than its name. The Orchestrator
                  probe closed the gap by observation this once.
AC-RACK-ROLE      its unreachable source-slice fallback ends with `expect(String(error)).toMatch(/./)`,
                  a no-op. Harmless; it never runs.
```

## Slice R14 issued — Worker session 13, exchange 01, at `e8cc7bb`

`fix(a11y): one persistent announcer and a role on every named rack tile`. Prompt staged at
`/tmp/opencode/uii-r14-worker-13-prompt.md`, 500 lines. Archive as `13_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2, reasoning HIGH.

The first slice in this whole that **removes** accessibility attributes. `role="status"` goes 8 -> 1 and
`aria-live` goes 8 -> 1, because F21 and F22 share one fix and taking it makes the product smaller instead
of adding another layer.

### The mechanism, and why it is one thing and not three

```text
ADD     ONE visually hidden region, mounted UNCONDITIONALLY inside DndContext beside <BlankPicker/> at
        page.tsx:1691 — role="status" aria-live="polite" aria-atomic="true" aria-label=a11y.status.turn
REMOVE  role="status" + aria-live from all six ToastOverlay branches   page.tsx :195 :250 :288 :327 :369 :384
REPLACE the AIThinkingOverlay container's live semantics with role="group" + the SAME aria-label. `group`
        is a valid host for an accessible name and is NOT a live region, so the ticking countdown becomes
        harmless and `a11y.status.aiThinking` stays in use.
REMOVE  live semantics from TurnStatusNotice, which becomes plain visual text — and its now-unused `useT`
        import, or lint fails.
FIX     TileRack.tsx:46 — spread dnd-kit's `attributes` ALWAYS so the aria-label has a role, keep
        `listeners` conditional so drag behaviour does not change, then tabIndex={selectEnabled ? 0 : -1}
        so non-interactive tiles do not become Tab stops.
```

**Zero new keys and zero catalog edits.** Both existing status keys stay in use, so nothing goes dead and
`messages.*.ts` must appear in `git diff --name-only` zero times. 294 keys stay 294.

### Two things written in so a Worker cannot helpfully break them

⛔ **The first value is not announced, and that is correct.** `turnStatus.text` is non-null at mount, so the
initial status is silent and every subsequent change speaks. The prompt forbids a mount-delay, a double
render, or a clear-and-reset effect to force it, and makes "I found myself writing one" a stopping condition.

⛔ **`sr-only` is JIT and this codebase references it zero times today.** Tailwind is 4.2.2 and ships the
utility, but it is only emitted once a source file uses it. So the prompt requires
`grep -c "sr-only" .next/static/css/*.css >= 1` after the build, with a pre-authorized inline
visually-hidden fallback if it is 0 — and forbids `display:none`, `visibility:hidden`, `hidden`,
`opacity-0` alone and zero width/height, every one of which would produce a region that is present,
persistent and completely silent.

### The one authorized test inversion, named in advance

`AC-STATUS-NOT-DIALOG` asserts `role="status"` x6 and `aria-live="polite"` x6 in the toast source. Both
become 0. The prompt authorizes flipping exactly those two counts, requires the negative assertions
(no `role="dialog"`, no `aria-modal`) to stay, requires the positive counterpart to move to
`AC-ANNOUNCE-ONE`, and requires the report to argue property coverage. It also requires the
`AC-NO-OVERLAY-LIVE` fixture to set a non-null `aiTurnTelemetry.humanState`, which is what makes the
count assertion stop being vacuous.

New pin: `AC-ONE-LIVE-REGION` — across `frontend/src` excluding tests, `aria-live` exactly once and
`role="status"` exactly once. Fifth pinning assertion in this catalog.

### Orchestrator pre-verification before issuing

Every line number in the prompt was checked against the shipped source, because a wrong citation in a
prompt is the same failure mode as a wrong inventory:

```text
TileRack.tsx:46 the conditional spread — NOT :38, which is dnd-kit's own `disabled` option. The first
                draft said :38 and was corrected before issuing.
TileRack.tsx:41 selectEnabled · :86 aria-label on the draggable · :154 on the tap button
page.tsx role="status" at 195 250 288 327 369 384, each aria-live on the following line
page.tsx:102-109 Toast, every variant carrying `message: string` · :1446-1477 turnStatus
page.tsx:1456 the aiThinking branch — so the AI turn is ALREADY announced and a second source would
                duplicate it · :1691 BlankPicker · :1750 blocker · :1760 toast
AIThinkingOverlay.tsx:271-273 the region · :302 formatTime(aiCountdown) inside it · :325-339 the feed
TurnStatusNotice.tsx:14 the null guard that makes it mount with its content
@dnd-kit/core 6.3.1 dist/core.esm.js:3432-3438 — role, tabIndex, aria-disabled, aria-pressed,
                aria-roledescription, aria-describedby, with role defaulting to 'button'
React 19.2.4 and `JSX.Element` used ZERO times in src/ — so the prompt forbids annotating it
expected end state 1 1 4 4 1 0 5 0 for aria-live, role=status, role=dialog, aria-modal, role=group,
                htmlFor, tabIndex, activeElement — tabIndex 4 -> 5 is the one rack tile
```

## Slice S11 landed at `e8cc7bb3be6b1e403102ed4e89c04996a0349fd3` — Worker session 12, exchange 01

`feat(a11y): accessible names, dialog semantics and status regions`. 16 files, +454 -9, none created,
none deleted, parent `c3f75e3`, one non-force push, public readback equal, `.ap` gitlink untouched at
`9c5cc44`. Build gate ran the PRIMARY route: `ss -tlnp | grep :3000` empty, exit 1.

Orchestrator verdict: **implementation-PASS, ACCEPTED as delivered.** Evidence independent — every gate
re-measured below, every count re-derived from the shipped source rather than read off the report.

Archived as `12_implementation_00.md` + `12_report_00.md`.

**The frontend copy, function and attribute surface is now complete.** What follows in this whole is
backend and security only — plus the one remediation this slice itself created, recorded as `R14`.

Handout residual **`R12` (`uii-01-F02` accessible names + `uii-01-F03` locale-aware dates) is now
satisfied**: F03 closed at `8f44022`, F02 delivered here. `R14` is a NEW label, not a reopening — it
carries the three findings this delivery produced (F20, F21, F22) plus one test-strength fix. Handout
labels run R1–R13, so R14 is the next free identifier.

### Gates at `e8cc7bb`, Orchestrator-measured

```text
mypy 83 files clean · ruff clean · manage.py check clean · pytest 381 passed, 4 skipped in 218.61s
typecheck exit 0 · vitest 414 passed | 3 skipped (29 files passed, 1 skipped) · lint exit 0
build exit 0, 11 dynamic routes, ZERO static
```

`405 -> 414` is exactly the nine new `it` blocks: AC-RACKTILE-4, AC-RACKBLANK-4, AC-A11Y-COPY-4,
AC-DIALOG-PRESENT x4, AC-STATUS-NOT-DIALOG x2. No pre-existing test was weakened or removed.

### Counted from the shipped source, not accepted from the report

```text
294 keys per catalog x 4 languages = 1176 strings, parity exact   285 + 9, arithmetic closes
20 fn keys per catalog, parity exact
role="dialog" 4 · aria-modal 4 · tabIndex={-1} 4      the four dialogs, nothing else
role="status" 8       = 6 ToastOverlay branches + AIThinkingOverlay + TurnStatusNotice
htmlFor 0             the three ProfileModal password inputs were NOT touched, as forbidden
"Tab" / shiftKey 0    no focus trap was written, as forbidden
activeElement 0       focus restoration absent -> uii-01-F19 stands as an accepted residual
locked-fork files 0   prompts.ts, ai-move-stream, api/ai/move, api.ts, constants.ts, types.ts,
                      PremiumPicker.tsx, provider-registry, openai-compatible, ibm-watsonx,
                      ai-runtimes, selection.py, and the entire backend/ are all untouched
```

Terminology verified verbatim against the glossary in all four catalogs: sk `Písmeno`, cs `Kámen`,
pl `Płytka`, and `Žolík / Žolík / Blank` for the blank. The fifth live use of the plural helpers and the
first for `bod` is correct through the real `tf`: sk `1 bod / 2 body / 5 bodov`, cs `bodů`, pl `punktów`.
The test also asserts `sk 2` is not `2 bodov`.

### ⛔ THE WORKER CORRECTED MY INVENTORY AND IT WAS RIGHT

Report item 8 says `AIThinkingOverlay` contained **one** `aria-live`, not the two my scoping note claimed.
Checked at the parent commit:

```text
git grep aria-live c3f75e3 -- frontend/src
  AIThinkingOverlay.tsx:236                 the telemetry <p>
  app/game/[id]/page.tsx:1614               the <section> wrapping TurnStatusNotice
```

Two occurrences repo-wide, in **two different files**. My note collapsed them into one file. The Worker
read the source, found one, said so, and resolved both: it removed the inner telemetry attribute (which the
new outer region would have nested) and removed the page-level `section` wrapper (because
`TurnStatusNotice` itself became the labelled region). No nested live region remains anywhere; the three
status surfaces are DOM siblings, not ancestors of one another.

**This is the second consecutive slice where a Worker overruled an Orchestrator claim on evidence.** The
pattern that produced both: I stated a conclusion more precisely than my measurement supported. The
measurement I actually ran counted `aria-label`, `role`, `alt`, `htmlFor`, `tabIndex`, `aria-modal` and
`sr-only`. It never counted `aria-live`. The "two places" was recollection presented as inventory.

Report item 16 is also correct and I verified it: the **games** `HeaderMiniButton` at `ScorePanel.tsx:419`
is not `iconOnly` and renders visible localized text, so it already had a name. Only the **profile** one
at `:364` is icon-only, and only it took an `aria-label`.

### ⛔ THREE NEW FINDINGS, all mine, none of them Worker disobedience

#### uii-01-F21 — the AI progress region re-announces the entire overlay once per second

`role="status"` carries an implicit `aria-atomic="true"`. The region I told the Worker to put on
`AIThinkingOverlay`'s `fixed inset-0` container encloses `formatTime(aiCountdown)` at
`AIThinkingOverlay.tsx:302`, which ticks every second for the whole AI turn, plus an append-only candidate
feed. Atomic plus ticking means an assistive technology re-reads the timer, the best score, every provider
pill and every candidate row roughly once a second.

That is the exact opposite of the principle my own prompt argued for one section earlier — `polite` was
chosen so announcements "queue rather than interrupt". And it is a **regression against the parent
commit**, because the `aria-live` at `:236` that this slice removed was a narrow, correct announcer on a
single telemetry line.

Cause: my instruction. The Worker implemented what it was told, disclosed exactly what it changed, and had
no way to see the consequence from the prompt. Owner: this whole, as `R14`.

#### uii-01-F22 — every status region mounts together with its content, so it may never announce at all

A live region has to exist in the DOM **before** its content changes for an assistive technology to
announce reliably. All three of ours appear with their text already inside: `ToastOverlay` is rendered on
demand at `game/[id]/page.tsx:1761`, `TurnStatusNotice` returns `null` when there is no text,
`AIThinkingOverlay` sits inside a conditional `AnimatePresence`.

The parent commit's `<section aria-live>` was conditional in the same way, so S11 did not regress this —
but it means the delivered turn, toast and AI announcements probably do not fire. The node-only suite
cannot detect it, which is exactly why the report's declared evidence ceiling matters. Owner: this whole,
folded into `R14`.

⚠ F21 and F22 have **one shared fix**: a single persistent visually hidden `role="status"` announcer on
the game page, fed a short string, with the overlays keeping `aria-label` and losing their live semantics.
That removes ticking content from the region and makes the region persistent in one move.

#### uii-01-F20 — a rack tile loses its accessible name in exchange mode

`TileRack.tsx:38` spreads dnd-kit's `attributes` only when
`!(isExchangeMode || interactionDisabled || !dragEnabled)`. Those attributes are where `role: "button"` and
`tabIndex: 0` come from — verified in `@dnd-kit/core` 6.3.1 at `dist/core.esm.js:3432-3438`. So in
**exchange mode** and when it is **not your turn**, the `motion.div` carries the new `aria-label` with no
role at all, and `aria-label` on a generic element is both ARIA-invalid and commonly ignored. In exchange
mode those tiles are still clickable, so the loss is real rather than academic. The tap path is fine:
`TapSelectableTile` renders a real `<button>`.

Severity medium, owner this whole, routed to `R14` since it is the same file class and the same review
pass. Not a prompt violation — the conditional spread is invisible from the prompt.

### One test is weaker than its name suggests, and it is worth writing down

`AC-STATUS-NOT-DIALOG` asserts `markup.match(/aria-live=/g)?.length === 1`, which reads like a pin against
re-nesting. It is not. The fixture sets `aiTurnTelemetry: null`, so `humanState` is falsy and the telemetry
`<p>` does not render at all — the assertion would pass with the inner `aria-live` still in place. The
Worker's own reported pre-fix failure confirms it failed on the outer `role="status"`, never on the count.
The fix is trivial (set a `humanState` in the fixture) and belongs to `R14`.

The three genuinely load-bearing new tests are the plural ones and `AC-DIALOG-PRESENT`, which resolves
`aria-labelledby` back to a matching `id` in the rendered markup rather than merely asserting the attribute
exists.

### Accepted without change

```text
four a11y.dialog.* fallback keys added to all four catalogs though all four dialogs use
aria-labelledby        required by prompt section 6.2 so the choice stays reversible without a new slice
onCloseRef indirection Worker's own near-miss fix: keeps the mount-time focus effect from re-running when
                       a parent re-renders an inline close callback. Correct.
sort: "updated"        a test fixture used "recent"; typecheck caught it; corrected inside the allowlist
BlankPicker SSR test   mutates useGameStore.getInitialState() to force the open branch and resets after.
                       Works because zustand's server snapshot IS the initial state. A smell, but bounded
                       and it demonstrably renders the dialog markup it asserts on.
```

## Slice S11 issued — Worker session 12, exchange 01, at `c3f75e3`

`feat(a11y): accessible names, dialog semantics and status regions`. Prompt staged at
`/tmp/opencode/uii-s11-worker-12-prompt.md`, 420 lines. Archive as `12_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2, reasoning HIGH.

Nine new keys, ten component files — the widest allowlist in this whole, deliberately, because
accessibility attributes are one-line additions per site and splitting them would multiply review passes
over the same markup. The prompt pairs that width with an explicit discipline clause: in those ten files,
change ONLY a11y attributes, `id`s for `aria-labelledby`, Escape handlers and the initial-focus target.

### ⛔ The one distinction the slice turns on: DIALOG versus STATUS

Six overlays use `fixed inset-0`. Treating them alike would make screen-reader output **actively worse
than today's silence**, so the prompt classifies each one:

```text
REAL DIALOGS — the user must act; focus belongs inside; Escape dismisses
  ProfileModal · GameHistoryModal · BlankPicker · the aiBlockerModal
  -> role="dialog"  aria-modal="true"  aria-labelledby=<visible heading id>
TRANSIENT ANNOUNCEMENTS — the user must NOT be interrupted; focus must NOT move
  ToastView · AIThinkingOverlay
  -> role="status"  aria-live="polite"
```

`polite` and not `assertive` is reasoned in the prompt: these announcements accompany a turn the player
initiated, so they must queue rather than interrupt. And `BlankPicker` is explicitly a dialog, not a
decorative overlay — it blocks the game until the player picks a letter for the žolík.

`AC-STATUS-NOT-DIALOG` is a NEGATIVE test asserting the toast markup contains neither `role="dialog"` nor
`aria-modal`, so a later slice cannot "improve" a toast into a modal. Fourth such pinning assertion in this
catalog after `AC-NO-TELEMETRY-KEY`, `AC-POLISH-DUP` and `AC-PROFILE-DUP`.

### A KEYBOARD FOCUS TRAP IS DELIBERATELY OUT OF SCOPE, and that is a decision not an omission

The prompt forbids implementing one and states the reason: a correct trap needs a focusable-element query,
Tab and Shift+Tab interception and focus restoration on close, across four components with different
internal structures — and a subtly wrong trap **strands a keyboard user with no escape**, which is worse
than no trap. `aria-modal="true"` plus Escape plus initial focus delivers most of the value at a fraction
of the risk. If the Worker starts writing a Tab handler it must STOP and report.

Recorded here as the accepted residual so it cannot be mistaken for an oversight at closure:

```text
uii-01-F19   no keyboard focus trap in the four dialogs
Severity     low.  aria-modal constrains assistive technology; Escape dismisses; initial focus lands
             inside. What is missing is Tab containment for a sighted keyboard user, who can still reach
             the page behind the dialog.
Owner        a future accessibility pass, if one is ever justified
Status       accepted-residual (Orchestrator, below the INFOSEC 14 medium threshold)
```

### ⛔ THE HONEST EVIDENCE CEILING, stated in the prompt rather than implied

vitest runs with `environment: "node"`, there is no axe, no jsdom, and Browser MCP is a locked fork. So
**rendered accessibility cannot be proven by this suite.** The prompt says the ceiling out loud: the
attributes ARE PRESENT in the markup, asserted by string tests where a component can be string-rendered,
plus Cooperator keyboard observation — and nothing more. `AC-DIALOG-PRESENT` explicitly instructs the
Worker to name which components it could and could not cover and to NOT fake an assertion for the rest.

This is the same structural blindness that let `uii-01-F04` ship eleven slices ago. Naming it is the
required behaviour; claiming an audit would be the failure.

### The rack tile is the FIFTH live use of the plural functions and the first for `bod`

`a11y.rackTile` announces `Písmeno A, 1 bod` / `2 body` / `5 bodov`. Pre-verified before issuing:

```text
  1   sk 'Písmeno A, 1 bod'      cs 'Kámen A, 1 bod'      pl 'Płytka A, 1 punkt'
  2   sk 'Písmeno A, 2 body'     cs 'Kámen A, 2 body'     pl 'Płytka A, 2 punkty'
  5   sk 'Písmeno A, 5 bodov'    cs 'Kámen A, 5 bodů'     pl 'Płytka A, 5 punktów'
 10   sk 'Písmeno A, 10 bodov'   cs 'Kámen A, 10 bodů'    pl 'Płytka A, 10 punktów'
```

Three terminology points ride on this one key, and the prompt states all three: Czech says `Kámen` and
Polish `Płytka` while Slovak says `Písmeno`, so it must NOT be harmonized; `2 bodov` would be broken
Slovak and the test forbids it; and a BLANK gets its own `a11y.rackBlank` key rather than
`a11y.rackTile` with a `?`, because a žolík has no letter until it is resolved — which is the entire reason
`písmeno` and `žolík` are separate words in this product.

### Two corrections the prompt carries forward from the Orchestrator's own errors

```text
1  the three ProfileModal password inputs are ALREADY correctly labelled by nesting. The prompt says so
   and forbids adding htmlFor/id, because redundant labelling is a regression. An earlier Orchestrator
   draft called them unlabelled on the strength of `htmlFor` returning zero.
2  AIThinkingOverlay ALREADY has aria-live in two places. The prompt requires the Worker to check before
   adding a third, because nested live regions produce duplicate or dropped announcements — and to report
   what it found. That is a defect the Orchestrator would have caused by instructing blindly.
```

### The key count matched on the first try, for the first time

`prose NINE == 9 enumerated`. The programmatic check has now run on four consecutive prompts; it caught
errors in three of them (S8 29-for-35, S9 14-for-16, R1 8-for-5) and confirmed this one clean.

## The accessibility slice is now scoped from MEASUREMENT, at `c3f75e3`

Every input in the product enumerated, rather than a `htmlFor` count inferred into a conclusion:

```text
file:line                              inside <label>   aria-label
app/page.tsx:172  (username)                 NO             NO      <- genuinely unlabelled
app/page.tsx:179  (password)                 NO             NO      <- genuinely unlabelled
components/game/ChatPanel.tsx:53             NO             NO      <- has a placeholder only
components/game/ProfileModal.tsx:257         YES            no      already correct
components/game/ProfileModal.tsx:270         YES            no      already correct
components/game/ProfileModal.tsx:283         YES            no      already correct
components/settings/PremiumPicker.tsx:191    NO             YES     already correct (R1)
```

So the real input work is **three** fields, not six: the two auth fields on the landing page and the chat
input. A placeholder is not an accessible name — it disappears on focus in most screen-reader flows — so
`ChatPanel` needs a real one.

The rest of the a11y baseline at `c3f75e3`:

```text
aria-label 2 · role= 4 · alt= 2      all SEVEN of these are inside PremiumPicker.tsx, which R1 created.
                                     Before R1 the product had zero of any of them.
htmlFor 0 · tabIndex 0 · aria-modal 0 · aria-labelledby 0 · sr-only 0
```

Modal surfaces needing `role="dialog"`, `aria-modal="true"`, `aria-labelledby` and Escape:
`ProfileModal`, `GameHistoryModal`, `BlankPicker`, and the `aiBlockerModal` plus the toast overlays inside
`game/[id]/page.tsx`. Only `settings/page.tsx:552` handles Escape today, and `PremiumPicker` handles its
own.

Icon-only controls needing an accessible name: the `↩` back button at `ScorePanel:355`, and the four
`iconOnly` `HeaderMiniButton` call sites (profile 👤, games 🗂️, settings x2). Their labels are ALREADY
localized and ALREADY passed as props — they are just rendered only inside a hover tooltip, which is not an
accessible name. That makes this the cheapest high-value fix in the slice.

`TileRack` tiles are better than expected: they already carry `onKeyDown` for Enter/Space and
`aria-pressed`. Their accessible name is the bare letter; `"Písmeno A, 1 bod"` would be materially better
and is a translatable string.

### uii-01-F18 — five accepted PremiumPicker behaviours, Cooperator-signed

    Classification:  accepted product behaviour, NOT defects
    Severity:        info
    Approver:        Cooperator, 2026-09-02, batch B24 item 2, verbatim `nevadi`
    Regression test: not applicable — these are accepted behaviours, not corrections
    Rationale:       the R1 prompt asked the Worker what it would question having read the finished
                     markup. It named five things. The Cooperator was shown all five and accepted all
                     five. They are recorded so a later reader cannot mistake them for defects and
                     "fix" them without knowing he had already seen them:
                       a  opening the picker replaces the selected name with an empty search field
                       b  the filter is substring over folded text, so `en` matches both `English` and
                          `Slovenčina` (which folds to `slovencina`)
                       c  the open list overlays the panels below and can clip at the settings
                          scrollport when scrolled
                       d  picker labels are NOT CSS-uppercased, unlike the 2x2 grid they replaced,
                          because `text-transform: uppercase` does not round-trip Slavic diacritics
                          reliably in this font stack
                       e  `frontend/public/hu.png` remains committed and unreferenced
    Note:            (e) is not merely accepted but REQUIRED — Hungarian is neither a shipped interface
                     locale nor a playable variant, and the file is pre-positioned for `11/02`.
    Recorded in:     this ledger and the closure record for ui-internationalization
    Status:          accepted-residual

### ✅ Cooperator acceptance batch B24 — 8 of 8 PASS, itemized. CLOSURE CONDITION 2 IS MET.

His reply, verbatim: `1.) B24-1 PASS B24-2 PASS B24-3 PASS B24-4 PASS B24-5 PASS B24-6 PASS B24-7 PASS
B24-8 PASS 2.) nevadi`

```text
B24-1  the interface-language panel is a DROPDOWN with flag + name + arrow, not four buttons   PASS
B24-2  it opens into a search field and a list with flags                                      PASS
B24-3  ⛔ HIS OWN EXAMPLE: typing "cestina" finds "Čeština"; also CESTINA and slovencina        PASS
B24-4  ArrowUp/Down navigate, Enter selects, Escape closes without changing the value          PASS
B24-5  the game-variant panel is also a dropdown with flags                                    PASS
B24-6  typing "slowacki" finds "Słowacki" — the `ł` case NFD cannot fold                        PASS
B24-7  an unavailable variant is a row that cannot be selected and that arrows skip            PASS
B24-8  clicking outside closes without changing the value                                      PASS
```

**Handout closure condition 2 — "both Settings dropdowns exist with flags, diacritic-insensitive
autocomplete and the arrow, and he has accepted them" — is now SATISFIED**, itemized rather than blanket.

`B24-3` is the strongest single result in this whole. The Cooperator described that exact behaviour in his
own words months of work ago — *"'cestina' must match 'Čeština'"* — and he has now confirmed it working in
his own browser. `B24-6` confirms the `ł` trap the prompt named in advance is genuinely handled, not
merely asserted in a unit test.

`B24-7` is rendered acceptance of the disabled-row behaviour, which is the part the prompt forced into a
pure function because the node-environment suite cannot render it. Both halves of that evidence now exist:
`nextPickerHighlight` proven in a test, the visible behaviour proven by him.

#### The five design questions: `nevadi` — he accepts all of them

Asked whether any of the five things the Worker flagged bothered him, he answered `nevadi`. So all five are
now **accepted product behaviour**, not open items:

```text
a  opening the picker replaces the selected name with an empty search field         ACCEPTED
b  the filter is substring, so "en" matches both English and Slovenčina             ACCEPTED
c  the open list overlays the panels below and can clip at the scrollport           ACCEPTED
d  picker labels are not CSS-uppercased, unlike the old 2x2 grid                    ACCEPTED
e  hu.png remains unreferenced                                                      ACCEPTED (required)
```

Recorded as accepted rather than left silent, because (a) and (d) are visible behaviour changes a later
reader could mistake for defects, and (c) is a real layout limitation someone might otherwise "fix"
without knowing he had seen and accepted it. Asking him and recording the answer is what makes them
decisions instead of unexamined residue.

Last used batch prefix is now **B24**.

## Slice R1 landed at `c3f75e32533b6c4abd38d2c006f46c2c59eaa68e` — Worker session 11, exchange 01

`feat(ui): premium searchable language and variant pickers with flags`. 12 files, +615 -94, two created,
parent `8f44022`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED**, pending the Cooperator's rendered acceptance which is closure condition 2. Evidence
non-independent.

Archived as `11_implementation_00.md` + `11_report_00.md`.

**The last feature work in this whole is done.** The five flag PNGs the Cooperator committed at `61c9f09`
are finally referenced, and `frontend/src/components/settings/PremiumPicker.tsx` is the first
combobox — and the first `role`, `aria-label` and `<img>` — this codebase has ever had.

### Both cited documentation sentences verified VERBATIM at the exact lines

Not accepted from the report:

```text
image.md:8   "The Next.js Image component extends the HTML `<img>` element for automatic image
              optimization."
image.md:96  "If the image is purely decorative or not intended for the user, the `alt` property should
              be an empty string (`alt="")."
```

Both exact. The `<img>`-over-`next/image` choice is sound for 48x32 PNGs totalling 5230 B — the optimizer
would add a `/_next/image` route for no benefit, and `grep -c "_next/image"` in the build output returns
**0**, so it did not.

### ⛔ THE WORKER OVERRULED MY AUTHORED STRING, AND IT WAS RIGHT

Section 7.4 authored `picker.flagAlt` as `Vlajka: {language}` and then explicitly permitted the Worker to
choose `alt=""` instead if it judged the images decorative. **It chose `alt="" aria-hidden="true"`**, and
cited `image.md:96` plus the reason: a flag beside its own label would make a screen reader announce
"Vlajka: Slovenčina, Slovenčina".

That is the better accessibility answer and it is the answer I could not have reached — it depends on the
finished markup, which the Worker had read and I had not. The five keys are in all four catalogs anyway, so
the decision is reversible without a new slice, exactly as the prompt required.

**This is the value of writing a prompt that permits being overruled on a judgement that needs
information the Orchestrator does not have.** Contrast the failure mode this project keeps recording:
prompts that state a conclusion more precisely than their evidence supports.

### The diacritic fold, verified through the REAL shipped function over every label this product ships

A throwaway harness imported `foldForSearch`, `filterPickerOptions` and `nextPickerHighlight` from the
shipped module, then was removed (porcelain verified clean):

```text
English      -> english        Angličtina  -> anglictina      Czeski    -> czeski
Slovenčina   -> slovencina     Slovenština -> slovenstina     Polština  -> polstina
Čeština      -> cestina        Poľština    -> polstina        Angielski -> angielski
Polski       -> polski         Słowacki    -> slowacki   <- the ł case NFD cannot do
Ł            -> l
```

`Čeština -> cestina` is the Cooperator's own example, working. `Słowacki -> slowacki` is the trap the
prompt named in advance: the Worker's explicit map covers `ł/Ł -> l`, `đ/Đ -> d` and `ø/Ø -> o` beyond
NFD's reach.

Navigation verified over a disabled middle row: down from index 0 lands on 2, **up from 0 also lands on
2** — so it wraps at both ends and skips the disabled row in both directions, and an all-disabled list
returns `-1`. Those are the three cases most likely to be subtly wrong, which is why the prompt forced the
arithmetic into a pure exported function.

### Accessibility emitted, counted from the shipped source

```text
role="combobox" x2 · role="listbox" · role="option" · aria-label x2 · aria-expanded x2 ·
aria-controls x2 · aria-haspopup · aria-autocomplete · aria-activedescendant · aria-selected ·
aria-disabled · aria-hidden x2 · alt=""
```

Matches report item 11 exactly.

### Gates at `c3f75e3`, Orchestrator-measured

```text
mypy 83 files · ruff · manage.py check · pytest 381 passed, 4 skipped in 220.68s
typecheck exit 0 · vitest 405 passed | 3 skipped (29 files) · lint exit 0
build exit 0, 11 dynamic routes, ZERO static, ZERO /_next/image
```

### The test change was a real judgement, disclosed properly

`GameLanguagePanel.test.ts` dropped three selectors — `data-variant-slug`, `data-variant-readiness` and
the HTML `disabled` attribute — because the control is now a listbox where `disabled` is not a valid
attribute on an option. It replaced them with `data-option-value` plus `aria-disabled`, **inverted the
assertion accordingly** (`.not.toMatch(/\bdisabled\b/)` where it previously required a match), and ADDED
a `display_name`-fallback assertion that did not exist before.

Assessed line by line: the property under test — an unavailable variant is not selectable — is still
proved, now by `aria-disabled` plus the click/Enter guards plus `nextPickerHighlight` skipping disabled
rows. Net assertions went UP. Accepted; the Worker named exactly what it removed and why, which is the
only lawful way to change a test in this project.

### Two disclosed deviations, both accepted

```text
overflowVisible on the internal SettingsPanel   default false, set ONLY by the interface-language panel,
                                                verified at settings/page.tsx:101,107,111,368. Necessary
                                                because `overflow-hidden` would clip the open list. A
                                                minimal, opt-in, single-caller change.
eslint-disable @next/next/no-img-element         one line, with a comment citing the optimizer rationale.
                                                Honest: the rule exists to push people to next/image, and
                                                the report argues the exception on documented grounds
                                                rather than silencing it quietly.
```

### FIVE things the Worker says the Cooperator may want changed — and it was asked to say so

Report item 17, in response to a prompt field asking what it would question having read the finished
markup:

```text
a  opening the picker REPLACES the selected name with an empty search field. He may want the current
   language to stay visible while typing.
b  the filter is substring, so a query of `en` matches BOTH `English` and `Slovenčina` (which folds to
   `slovencina`). Defensible, but not what everyone expects.
c  the open list overlays the panels below and can still clip at the settings scrollport if he has
   scrolled far down.
d  picker labels are NOT CSS-uppercased, unlike the old 2x2 grid, because Slavic diacritics do not
   round-trip through `text-transform: uppercase` reliably in this font stack. A deliberate visual
   change he will notice.
e  hu.png remains unreferenced, as required.
```

⚠ Item (b) is worth keeping: it is the honest cost of a substring filter over folded text, and the
Orchestrator's `AC-PICKER-FILTER` fixture initially got it wrong in the same way — the Worker's near-miss
in item 19 is exactly that, an over-narrow expectation that `EN` would match only English. It corrected
the fixture rather than the behaviour, which was the right call.

Item (d) is the fourth time in this whole that Slavic diacritics have forced a typography decision, after
`overlay.bestBadge`, the `b.`/`pkt` abbreviations and the U+00A0 thousands separator.

### Context-pressure disclosure

The Worker reported ~75% visible context usage and still completed against repository evidence. That is
the second slice to cross 70%, and both were the two largest — S5 and this one. The remaining slices are
smaller.

## Slice R1 issued — Worker session 11, exchange 01, at `8f44022`

`feat(ui): premium searchable language and variant pickers with flags`. Prompt staged at
`/tmp/opencode/uii-r1-worker-11-prompt.md`, 451 lines. Archive as `11_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2, reasoning HIGH.

**The last feature work in this whole, and closure condition 2.** It is also the only slice here that
builds a NEW INTERACTIVE COMPONENT rather than extracting strings.

### One shared component, two instances

`frontend/src/components/settings/PremiumPicker.tsx` replaces both 2x2 button grids. Contract: closed
state shows the selected flag plus label with a trailing arrow; open state is a text input plus a filtered
listbox; ArrowUp/Down/Home/End/Enter/Escape all specified; disabled rows rendered, muted, unselectable and
SKIPPED by arrow navigation; outside click closes without changing the value.

Accessibility is required INSIDE the picker and forbidden outside it, because the product-wide pass is the
next slice and mixing them would make both diffs unreviewable. Inside: `role="combobox"`,
`aria-expanded`, `aria-controls`, `aria-label`, `role="listbox"`, `role="option"`, `aria-selected`,
`aria-disabled`, `aria-activedescendant`. Those will be the **first** `role` and `aria-label` attributes
this codebase has ever had.

### ⚠ THE DIACRITIC TRAP, named in the prompt rather than left to be discovered

The obvious fold is `value.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase()`. It handles
`č š ž ě ř ů á í ó ú ý ą ę ć ń ś ź ż` — and it does **NOT** handle Polish `ł`, because U+0142 is a
distinct letter with a stroke, not a base letter plus a combining mark. NFD leaves it untouched.

Not reachable today: the four endonyms are `English`, `Slovenčina`, `Čeština`, `Polski`, and no shipped
label begins with `ł`. But `Słowacki` — the Polish exonym for Slovak, already in the catalog — contains one
mid-word, so a query of `slowacki` against it exercises exactly this path. The prompt therefore requires an
explicit character map for `ł`/`Ł` and suggests `đ`/`Đ`/`ø` at zero extra cost, and `AC-FOLD` asserts the
`ł` case **explicitly**, with the note that "that assertion is the point of the test".

His own example is a mandatory test: `cestina`, `CESTINA`, `Čeština` and `ceSTIna` must all match
`Čeština`.

### Testability under a node-environment suite, made structural

vitest runs with `environment: "node"` and nothing in the suite renders a component — the same blindness
that let `uii-01-F04` ship. So the prompt requires the FILTERING and the ARROW-NAVIGATION INDEX ARITHMETIC
to be extracted as pure exported functions, and says why: *"that is the whole reason to extract them."*
`AC-PICKER-NAV` then tests the part most likely to be subtly wrong — skipping disabled options in both
directions, and Home/End landing on the first/last ENABLED option.

### One genuine design question handed to the Worker WITH permission to overrule the prompt

Section 7.4 authors `picker.flagAlt` as `Vlajka: {language}` — and then says that a flag rendered next to
its own label may be purely DECORATIVE, in which case `alt=""` plus `aria-hidden="true"` is **more**
correct, because a screen reader would otherwise announce "Vlajka: Slovenčina, Slovenčina". The Worker is
told either choice is acceptable, must say which and why, and must add the keys to all four catalogs
regardless so the decision is reversible without a new slice.

That shape is deliberate: it is a real accessibility judgement that depends on the finished markup, which
the Worker will have read and the Orchestrator has not.

### Three preservation constraints that would silently break corrected defects

```text
variantDisplayName MUST keep its name, signature and export — app/play/page.tsx imports it for the
                   uii-01-F14 queue label. Breaking it reintroduces a corrected defect invisibly.
variants order     must NOT be re-sorted; server order is deliberate.
hu.png             must stay UNREFERENCED. Hungarian is neither a shipped interface locale nor a
                   playable variant.
```

### ✅ The Orchestrator's key-count check fired for a THIRD consecutive prompt

```text
first draft prose  "Add all eight new keys."
programmatic count  5   (four plain + one parameterized)
corrected to        FIVE, with the table-wins precedence rule added inline, then re-verified
```

Three prompts in a row now: S8 said 29 for 35, S9 said 14 for 16, R1 said 8 for 5. Two of those three were
caught by the Orchestrator before issuing rather than by a Worker afterwards, which is the improvement the
S8 entry promised. The underlying lesson stands and is now mechanical: **count the table, never trust the
prose.**

## ⛔ ORCHESTRATOR OMISSION CHECK at `8f44022`: R1 IS STILL OPEN, and it is a CLOSURE CONDITION

Measured, not remembered, while scoping the accessibility slice:

```text
grep -rn "en.png|sk.png|cs.png|pl.png|hu.png|flag" frontend/src
  -> ONE hit, and it is `is_flagship` in types.ts. The five committed 48x32 flag PNGs are
     referenced NOWHERE. They have been in the tree, unused, since 61c9f09.
both language panels
  -> still `grid grid-cols-2` button grids. Neither is a dropdown; there is no <input>, no
     combobox, no listbox, no search field in settings.
diacritic-insensitive matching
  -> `normalize(` appears only in the LOCKED api/ai/move/route.ts for tile tokens. There is ZERO
     diacritic folding anywhere in the frontend.
```

**So `R1` has not been started.** `93_orchestrator-handout.md` section 6 describes it in the Cooperator's
own detail: *"a flag image left of the language name, a search input with diacritic-insensitive
autocomplete ('cestina' must match 'Čeština'), and an arrow at the input edge that opens the dropdown.
TWO of them — one for the interface locale, one for the game variant. He wants them eye candy, matching
the existing premium chrome, not a plain white input."*

And handout section 11 makes it closure condition 2: *"both Settings dropdowns exist with flags,
diacritic-insensitive autocomplete and the arrow, and he has accepted them."*

⚠ **This is an Orchestrator omission, and it nearly slipped.** Ten slices went to translation and
corrections while the one feature he described in his own words sat untouched, and the previous
Orchestrator message summarised the remaining work as "accessibility plus backend residuals" — which was
WRONG by one whole feature. Recorded plainly rather than quietly fixed, because a closure condition that
disappears from a status summary is exactly how a whole closes on incomplete evidence.

### ORCHESTRATOR SEQUENCING DECISION: R1 goes BEFORE the accessibility slice

The accessibility work (`uii-01-F02`) must add accessible names, `role`, `aria-modal`, `htmlFor` and ESC
handling to the final UI. `R1` REPLACES both settings language panels with a different control — a
combobox with a text input, a listbox, images and keyboard navigation.

```text
a11y then R1   the a11y slice writes names for two button grids that R1 then deletes, and R1 must
               re-do the a11y for a combobox — which has strictly MORE a11y surface than a button grid
               (aria-expanded, aria-controls, aria-activedescendant, role=combobox/listbox/option)
R1 then a11y   the a11y slice sees the final control set once and writes each accessible name once
```

Second ordering is obviously right. `R1` is issued next; accessibility follows it and becomes the last
frontend slice.

### The measured a11y baseline, taken now and reusable by that later slice

Re-measured at `8f44022` with the widened pattern, so the later prompt does not have to rediscover it:

```text
ZERO occurrences   aria-label · aria-labelledby · aria-describedby · role= · alt= · tabIndex ·
                   sr-only · htmlFor · aria-modal · <dialog> · autoFocus
present            aria-hidden 5 · aria-disabled 5 · aria-pressed 3 · aria-live 2 · aria-current 1
                   title= 9 · placeholder= 6 · onKeyDown 5
```

Specific findings for that slice, each with its location:

```text
1  ScorePanel:355   the back button's only content is a `↩` glyph plus a HOVER-ONLY IconTooltip. A
                    tooltip is not an accessible name — IconTooltip renders a `pointer-events-none`
                    absolutely-positioned span revealed by `group-hover`, invisible to a screen reader
                    as a label. Needs aria-label.
2  HeaderMiniButton with `iconOnly`   four call sites — profile 👤, games 🗂️, settings x2. The `label`
                    prop IS passed and IS already localized, but when `iconOnly` it renders ONLY inside
                    the tooltip. The name exists; it just is not attached. Cheapest possible fix.
3  htmlFor is ZERO  ⛔ AND THE FINDING THAT FOLLOWED FROM IT WAS WRONG. An earlier draft of this
                    entry said "ProfileModal's three password fields have visible labels that are NOT
                    associated with their inputs. A screen reader announces an unlabelled password
                    field." That was a NEGATIVE-GREP CONCLUSION and it is FALSE.
                    Measured by reading ProfileModal.tsx:253-265: each input is NESTED INSIDE its
                    `<label className="block">`, which is IMPLICIT labelling and is fully valid per the
                    HTML spec. `htmlFor` is unnecessary when the control is a descendant of its label.
                    All three password fields are already correctly labelled.
                    This is the project's most-repeated failure mode — `htmlFor` returning zero is not
                    the same fact as "inputs are unlabelled" — caught this time by the Orchestrator
                    against itself before any prompt was written. The remaining real question for the
                    a11y slice is narrower: whether the two chat/search inputs elsewhere are labelled,
                    which must be MEASURED and not inferred from the same grep.
4  four modal surfaces  GameHistoryModal, ProfileModal, BlankPicker, and the aiBlockerModal inside
                    game/[id]/page.tsx. None has role="dialog", aria-modal, or aria-labelledby, and
                    only settings/page.tsx:552 handles Escape at all.
5  TileRack tiles    already keyboard-operable with onKeyDown Enter/Space and aria-pressed — better
                    than expected. Their accessible name is the bare letter; "Písmeno A, 1 bod" would
                    be materially better and is a translatable string.
6  alt= is ZERO and there is currently NO <img> or next/image in the product at all. R1 introduces the
                    FIRST images in this codebase, so R1 itself must ship their alt text.
```

## Slice S9 landed at `8f440221b757bc142cb26391875c1361492da419` — Worker session 10, exchange 01

`feat(i18n): localize the profile modal and close the date locale defect`. 7 files, +297 -30, parent
`d806e31`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED.** Evidence non-independent.

Archived as `10_implementation_00.md` + `10_report_00.md`.

# ✅ THE FRONTEND COPY SURFACE IS COMPLETE

This was the last copy slice. Every user-facing string the frontend owns now exists in four locales.

### The catalog, measured at `8f44022`

```text
en / sk / cs / pl    text=262   fn=18   total=280 each
PARITY OK — zero missing, zero extra, both tables, every direction
1120 Orchestrator-authored strings

by area:  game 67 · settings 49 · history 35 · play 20 · profile 16 · draw 13 · landing 11 ·
          error 11 · auth 10 · header 8 · overlay 8 · queue 8 · controls 6 · board 6 · chat 6 ·
          meta 2 · nav 2 · rack 1 · blank 1
```

### A FINAL leftover sweep over every non-test `.tsx`, with the validated tool

23 files swept. **Seven** JSX text nodes survive, and every one is correct:

```text
draw/[id]/page.tsx:244      'VS'       glossary decision — universally understood, 2ch container
ScorePanel.tsx:63           'Libre'    the WORDMARK, not copy; the product is Libre Tiles in every locale
layout.tsx:12               a false positive — the sweep caught a function signature, not a text node
settings/page.tsx:664       false positive — a ternary fragment
Cell.tsx:100, :104          false positives — ternary fragments
ProfileModal.tsx:71         false positive — a ternary fragment
```

Two intentional, five regex artefacts, **zero real leftovers**. That is the first time the whole frontend
sweeps clean.

### uii-01-F03 is now CLOSED, verified through BOTH shipped functions

A throwaway harness imported both real formatters and called them, then was removed (porcelain verified
clean):

```text
en   joined="September 2, 2026"   updated="Sep 2, 4:35 PM"
sk   joined="2. septembra 2026"   updated="2. 9., 16:35"
cs   joined="2. září 2026"        updated="2. 9. 16:35"
pl   joined="2 września 2026"     updated="2 wrz, 16:35"
formatJoinedDate(null,"sk")        -> "Neznáme"
formatJoinedDate("not-a-date","sk")-> "Neznáme"
```

Both English outputs are byte-identical to the old hardcoded `"en-US"` behaviour, so the correction
provably changed nothing for English. `grep -rn '"en-US"' frontend/src` now returns only the two
`locale === "en" ? "en-US" : locale` mappings and one test assertion — **no hardcoded date locale remains.**

The detail the prompt flagged is correct in the shipped code:
`useMemo(() => formatJoinedDate(profile?.date_joined, locale), [profile?.date_joined, locale])`. Without
`locale` in that list, switching language would have left a stale English date on screen — a bug that
renders wrong in a browser while passing every test.

### Gates at `8f44022`, Orchestrator-measured

```text
mypy 83 files · ruff · manage.py check · pytest 381 passed, 4 skipped in 221.84s
typecheck exit 0 · vitest 398 passed | 3 skipped · lint exit 0
build exit 0, 11 dynamic routes, ZERO static
```

### Reuse discipline held, and `api.ts` is untouched

All eleven reusable keys were reused and no near-duplicate was added. `frontend/src/lib/api.ts` has an
empty diff, which is what structurally preserves `AC-SEC-1` and `AC-SEC-2`: the two newly localized
strings are CLIENT-side form checks that disclose neither account existence nor current-password
correctness, and every server-response message still routes through the untouched mapping.

### One honest disclosure worth keeping

The Worker exported `formatJoinedDate` as a test seam **before** the red run and stated that its pre-fix
behaviour was unchanged by the export. That is the right order: a seam added after a green run proves
less, and saying when the seam appeared is what makes the pre-fix failure text trustworthy.

It also hit the pytest session-handle problem a third time and handled it exactly as the prompt now
requires — re-ran the authorized command once, retained the handle, quoted only a summary it actually saw.

## Slice S9 issued — Worker session 10, exchange 01, at `d806e31`

`feat(i18n): localize the profile modal and close the date locale defect`. Prompt staged at
`/tmp/opencode/uii-s9-worker-10-prompt.md`, 386 lines. Archive as `10_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2.

**This is the LAST copy slice in this logical whole.** After it every user-facing string the frontend owns
is in four locales, and what remains is accessibility, Django localization and three security residuals.

### Sixteen new keys and ELEVEN reuses — more reuse than new work

```text
header.profile · nav.settings · game.blocker.close · auth.eyebrow · auth.field.username ·
auth.field.password · header.logout · header.loggingOut · game.password.updated ·
game.password.failed · history.unknownDate
```

All eleven verified present in all four catalogs before writing the prompt. The prompt says in terms that
duplicating any of them would be a defect, because a second Slovak spelling of "Heslo" is exactly how a
catalog starts to drift. This is the first slice where reuse outnumbers new authoring, which is what a
maturing catalog should look like.

### uii-01-F03 will be CLOSED, and the pattern is copied from the half that already shipped

`ProfileModal.tsx:18-27` `formatJoinedDate` is the second and last hardcoded `"en-US"` site. The prompt
requires the same shape S8 shipped — a `locale` parameter, `en` mapped to `en-US` so English output stays
byte-identical, the caller resolving via `useLocale()` — so the two sibling functions stay recognisably
alike rather than diverging into two idioms.

One detail the prompt calls out that a Worker could easily miss: `memberSince` at `:59` is a `useMemo`, so
**the locale must be in its dependency list** or switching language would leave a stale English date on
screen. That is the kind of correctness bug that renders fine in a test and wrong in a browser.

Measured in this repository before issuing, so no hand-built month tables are needed:

```text
en-US  September 2, 2026     sk  2. septembra 2026     cs  2. září 2026     pl  2 września 2026
en literal matches · sk/cs/pl all differ from en · none contains "September"     SATISFIABLE
```

### The two localized validation errors are auth-adjacent, and the prompt says why they are safe

`profile.error.allFields` and `profile.error.mismatch` are **client-side form checks**, not server
responses, so they may safely name which field is wrong. What they must not do is leak anything about the
ACCOUNT — no username existence, no restatement of whether the current password was right — and neither
authored string does. The server-side wording stays `game.password.failed` / `game.password.updated`,
reused unchanged, and `frontend/src/lib/api.ts` is on the forbidden list, so `AC-SEC-1` and `AC-SEC-2` are
structurally untouched. The Worker must confirm that explicitly.

### ✅ THE ORCHESTRATOR CAUGHT ITS OWN COUNTING ERROR THIS TIME, BEFORE ISSUING

After S8 the ledger recorded: *"For the remaining slices I will count the table programmatically before
writing the prose number."* Applied immediately, and it fired on the very next prompt:

```text
first draft prose  FOURTEEN new keys
programmatic count of the enumerated table   16
corrected to       SIXTEEN, and re-verified 16 == 16 after the edit
```

The prompt now also carries an explicit precedence rule in the same paragraph — *"If any prose number in
this prompt disagrees with the enumerated table, THE TABLE WINS"* — so a future discrepancy resolves
itself without a Worker having to raise it. Two Workers in a row had to do that raising; the third does
not.

### Two intentional duplications pinned by a test

`profile.field.current` and `profile.ph.current` carry identical text in every locale, because the field's
visible label and its placeholder both say "Current password" today. They are two keys because a label and
a placeholder are different UI roles that a later designer may legitimately want to diverge.
`profile.email` is `Email` in all four locales because Slovak, Czech and Polish all use that word.

`AC-PROFILE-DUP` asserts both, so neither can be "corrected" into a false distinction — the same shape of
defence as `AC-POLISH-DUP` and `AC-NO-TELEMETRY-KEY`. That is now three intentional-sameness assertions in
this catalog, and the pattern is worth naming: **when a translation legitimately coincides, pin it, or
someone will eventually "fix" it.**

### One trap added from two slices' experience

Two consecutive Workers lost a pytest summary to a session-handle timeout. The prompt now says: retain the
handle or re-run the exact authorized command once, and *"Do not report a summary you did not see."*

## Slice S8 landed at `d806e313c7f5b6198452fa68afa5d079059b6f48` — Worker session 09, exchange 01

`feat(i18n): localize the saved-boards history and its dates`. 8 files, +400 -51, parent `4bf4365`, one
non-force push, public readback equal. Orchestrator verdict: **implementation-PASS, ACCEPTED.** Evidence
non-independent.

Archived as `09_implementation_00.md` + `09_report_00.md`.

### uii-01-F03 half-corrected, verified through the REAL shipped function

Not accepted from the Worker's test. A throwaway harness imported `formatUpdatedAt` from the shipped
component and called it, then was removed (porcelain verified clean):

```text
en -> Sep 2, 4:35 PM          <- byte-identical to the old hardcoded "en-US" output
sk -> 2. 9., 16:35            <- 24-hour clock, no AM/PM
cs -> 2. 9. 16:35
pl -> 2 wrz, 16:35
```

The `en` -> `en-US` mapping holds, so this correction provably changed nothing for English while fixing
the other three locales. `formatUpdatedAt(value, locale)` takes the locale as a parameter and the caller
resolves it with `useLocale()`, so no hook is called from module scope.

⚠ `uii-01-F03` is **half** corrected. `ProfileModal.tsx:18-28` `formatJoinedDate` still hardcodes
`"en-US"` and is slice S9's. The finding stays OPEN until both call sites are done.

### The catalog after eight slices

```text
en / sk / cs / pl   text=246  fn=18  total=264 each
PARITY OK — zero missing, zero extra, both tables, every direction
1056 Orchestrator-authored strings
```

### Gates at `d806e31`, Orchestrator-measured

```text
mypy 83 files · ruff · manage.py check · pytest 381 passed, 4 skipped in 220.39s
typecheck exit 0 · vitest 394 passed | 3 skipped · lint exit 0
build exit 0, 11 dynamic routes, ZERO static
```

### ⛔ AN ORCHESTRATOR COUNTING ERROR, caught by the Worker and confirmed against my own prompt

Report item 14: *"the prompt labels the set 'twenty-nine new keys,' but its exact enumerated contract
contains 35 keys."*

Verified by counting the `history.*` keys in my own section 6: **35**, not 29. The prose count was wrong
and the table was right. The Worker implemented all 35 — the enumerated contract — and flagged the
discrepancy instead of silently implementing 29 or asking.

That is the correct resolution and it is worth naming why: an enumerated table is evidence, a prose
summary is a claim. When they disagree the table wins, and this project has now recorded that shape twice
in two slices — the S6 prompt said "seven existing keys" while listing five, and this one said 29 while
listing 35. **Both times the Worker took the table.** For the remaining slices I will count the table
programmatically before writing the prose number, which is what I did to confirm this.

### Item 13 leftover list: no real findings, second slice running

Emoji, `item.opponent_label` as a server identity, and `item.game_end_reason` as the backend enum I named
in the prompt in advance. `Leftovers that should have received keys: none.` The structural report field has
now come back clean twice in a row, after catching a real leftover in four consecutive slices before that.

### The `game_end_reason` passthrough is now formally on the record

```text
uii-01-F17   `GameHistoryPanel` renders `item.game_end_reason` — a backend enum such as
             BAG_EMPTY_AND_PLAYER_OUT — directly as a user-facing row hint.
Severity     low; it is an uppercase machine string shown to a player, in a fallback position that only
             appears for a finished game that is neither the player's turn nor waiting.
Owner        the Django-localization slice (R7), because the end reasons are engine values and a keyed
             mapping belongs next to the other backend-produced strings, not in a frontend copy slice.
Status       open, deliberately deferred, named in the S8 prompt BEFORE implementation rather than
             discovered afterwards.
```

### One disclosed tooling hiccup, correctly classified

The first pytest invocation outran its captured session handle so its summary was unavailable; the Worker
re-ran the exact authorized command with a retained handle and quoted the real summary. Classified as a
diagnostic-method issue, not a product failure — the same distinction the Orchestrator had to make about
its own broken sweep two slices ago.

## Slice S8 issued — Worker session 09, exchange 01, at `4bf4365`

`feat(i18n): localize the saved-boards history and its dates`. Prompt staged at
`/tmp/opencode/uii-s8-worker-09-prompt.md`, 419 lines. Archive as `09_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2 because it carries a behavioural correction.

29 new keys across `GameHistoryPanel` and `GameHistoryModal`, plus the first half of `uii-01-F03`.

### ✅ uii-01-F03: `Intl` was MEASURED to produce correct Slavic dates, not assumed

The ledger's correction direction said "prefer Intl with the sk locale over hand-built strings" because a
Slovak month in a date is GENITIVE — "1. septembra", not "1. september". That advice is now verified
rather than trusted. Run with Node in this repository against the two exact field sets in use:

```text
locale   {month:long,day,year}        {month:short,day,hour,minute}
en-US    September 2, 2026            Sep 2, 4:35 PM
sk       2. septembra 2026            2. 9., 16:35
cs       2. září 2026                 2. 9. 16:35
pl       2 września 2026              2 wrz, 16:35
```

`Intl` gets the genitive right in all three Slavic locales AND switches to a 24-hour clock automatically.
So the fix is one argument, no hand-built month tables, and no date library. The prompt forbids adding one.

**The `en` -> `en-US` mapping is load-bearing and the prompt says why:** it keeps today's English output
byte-identical, so this correction can never be blamed for an English rendering change. Verified:
`Sep 2, 4:35 PM` from `"en"`-mapped equals `Sep 2, 4:35 PM` from hardcoded `"en-US"`.

### The slice is SPLIT and F03 is corrected in two halves deliberately

`uii-01-F03` has two independent call sites in two independent files —
`GameHistoryPanel.tsx:70-79` `formatUpdatedAt` and `ProfileModal.tsx:18-28` `formatJoinedDate`. They share
no code. Combining them would mean one slice touching three files with ~56 keys, and the S5 Worker
reported >70% context on less. So:

```text
S8  GameHistoryPanel + GameHistoryModal + formatUpdatedAt      29 keys   <- ISSUED
S9  ProfileModal + formatJoinedDate                            ~16 keys
S10 uii-01-F02 accessible names
```

The prompt explicitly forbids "fixing both date sites while you are here", because that would silently
widen an authorized allowlist — the failure mode this project has recorded four times.

### Three grammar decisions worth recording, because each avoids a broken Slavic string

```text
1  history.showing DROPS the counted noun in sk/cs/pl. English says "Showing 1-8 of 24 games"; the
   Slavic forms say "Zobrazené 1-8 z 24". Keeping the noun would need the genitive plural `partií`,
   correct for 5+ and WRONG for 2-4, with a variable number. Dropping it is grammatical at every count
   and the panel already says what is being counted. Fourth time this whole has solved a counted noun
   without a plural function — after tilesSelected, queueFor and the stats bar.
2  history.pageOf also absorbs the bare "Page 1" fallback by being called with {page:1,total:1} rather
   than adding a second key for a degenerate case.
3  Polish history.col.result and history.col.score are BOTH `Wynik`. That is correct Polish. A dedicated
   test, AC-POLISH-DUP, pins the duplication so a future reader cannot "correct" it into a false
   distinction — the same shape of defence as AC-NO-TELEMETRY-KEY.
```

### One leftover named in advance rather than discovered later

`GameHistoryPanel` renders `item.game_end_reason` as a row hint fallback. That is a BACKEND ENUM string
such as `BAG_EMPTY_AND_PLAYER_OUT`, and localizing it needs a keyed mapping of the engine's end reasons —
which belongs with the Django localization work, not a copy slice. The prompt localizes the three literals
around it, leaves the enum passthrough alone, and REQUIRES the Worker to name it in the report so it lands
on the record rather than being found by the Cooperator later.

### Orchestrator pre-verification before issuing

```text
AC-DATE-LOCALE  en differs from sk/cs/pl: true · no AM/PM in sk/cs/pl: true ·
                en byte-identical to the hardcoded en-US: true                        SATISFIABLE
AC-POLISH-DUP   the duplication exists in the authored table, so the assertion is meaningful
```

## Slice S7 landed at `4bf436581c1b6382183411259e25c6a409b7d54f` — Worker session 08, exchange 01

`feat(i18n): localize the settings screen and the overlay stats bar`. 8 files, +524 -53, parent
`6ca85de`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED**, with one Orchestrator-caused wart recorded. Evidence non-independent.

Archived as `08_implementation_00.md` + `08_report_00.md`.

**The frontend copy surface is now essentially complete except history and profile.** 38 new keys, the
largest single slice in this whole.

### The catalog invariant, measured across all four locales

```text
en  text=213  fn=16  total=229
sk  text=213  fn=16  total=229
cs  text=213  fn=16  total=229
pl  text=213  fn=16  total=229
PARITY OK — zero missing, zero extra, in every direction, for both tables
```

229 keys x 4 locales = **916 authored strings** in this whole so far, all Orchestrator-authored and all
gated by `Record<TextKey, string>`.

### Gates at `4bf4365`, Orchestrator-measured

```text
mypy 83 files · ruff · manage.py check · pytest 381 passed, 4 skipped in 221.09s
typecheck exit 0 · vitest 390 passed | 3 skipped · lint exit 0
build exit 0, 11 dynamic routes, ZERO static
```

### ⛔ A REAL Next.js 16.3.4 CONSTRAINT I DID NOT KNOW, and the Worker proved it

The prompt told the Worker: "If the arrays are not exported, export them for the test rather than
duplicating them in the test file." **That instruction is impossible to follow for a page module**, and
the Worker discovered why, worked around it legally, and reported it.

Reproduced by the Orchestrator rather than accepted: adding `export` to `TIMEOUT_CHOICES` and running
`npm run typecheck` yields, verbatim:

```text
.next/dev/types/app/settings/page.ts(14,13): error TS2344: Type 'OmitWithTag<typeof import(".../settings/page"),
  "prefetch" | "default" | "dynamic" | "revalidate" | "metadata" | "viewport" | "instant" | "config" |
  ... 8 more ... | "generateViewport", "">' does not satisfy the constraint '{ [x: string]: never; }'.
  Property 'TIMEOUT_CHOICES' is incompatible with index signature.
```

The generated `.next/types/app/settings/page.ts` contains a `checkFields<Diff<{ default: Function;
config?: {}; generateStaticParams?: Function; metadata?: any; generateMetadata?: Function; ... },
TEntry, ''>>()` assertion that **enumerates the only exports an App Router page module may have**. Any
other named export is a `tsc` error.

**This is durable environment knowledge and it is being promoted to `PROJECT_CONTEXT.md`.**
`frontend/AGENTS.md` says "This is NOT the Next.js you know"; this is a concrete, reproducible instance,
and it will bite any future slice that tries to export a helper or a constant from a page file.

#### uii-01-F16 — the choice arrays are attached as static properties on the page component

    Classification:  code-shape wart caused by an ORCHESTRATOR allowlist that was too narrow
    Severity:        info
    Confidence:      high
    Evidence class:  established-static — settings/page.tsx:721-723
                       SettingsPage.TIMEOUT_CHOICES = TIMEOUT_CHOICES;
                       SettingsPage.STEP_CHOICES = STEP_CHOICES;
                       SettingsPage.BOARD_THEME_CHOICES = BOARD_THEME_CHOICES;
                       export default SettingsPage;
    Why it exists:   `AC-KEYTYPED` needs the LIVE arrays, not a copy, or the test proves nothing. A named
                     export is a tsc error per the constraint above. `default` IS an allowed export, and
                     properties hung on it are not module exports, so this typechecks. It is a legal and
                     clever way out of a box.
    ⛔ THE BOX WAS MINE.  The idiomatic fix is a separate module — `frontend/src/app/settings/choices.ts`
                     or `frontend/src/lib/settings-choices.ts` — imported by both the page and the test.
                     The Worker could not do that because my allowlist said "No file is created and none
                     is deleted". This is the fourth time in this project that an Orchestrator allowlist
                     was too narrow, and the first time the consequence was an odd code shape rather than
                     a blocked session.
    Impact:          none functional. A reader wonders why a React component carries static data.
    Correction direction: extract the three arrays to their own module and import them in both places.
                     Costs one new file and two import lines.
    Regression test: AC-KEYTYPED already covers the behaviour and would survive the extraction unchanged.
    Owner:           fold into any later slice that has an independent reason to touch settings/page.tsx;
                     do NOT spend a slice on it
    Status:          accepted-residual (Orchestrator, below the INFOSEC 14 medium threshold)

### Two honest reporting details worth keeping

```text
1  the focused post-fix run is quoted as `6 passed | 35 skipped`. That is a FOCUSED i18n run, not the
   suite, and the Worker also quoted the full `390 passed | 3 skipped`. Both numbers are true and it
   distinguished them, which is exactly the precision this project asks for.
2  it disclosed that a first parallel pytest wrapper lost its continuation handle after 30 seconds and
   that it re-ran the exact authorized command once with a retained handle. A tooling hiccup, correctly
   classified as a diagnostic-method issue rather than a product failure, and not smoothed over.
```

### Item 14 leftover list: nothing unauthorized remains

`30s / 1m / 2m / 3m / 5m` and `10 / 20 / 30 / 50 / 80` are deliberately unlocalized unit abbreviations and
numbers per prompt D5; `"Escape"` is a KeyboardEvent key name; `selectedModel.display_name` is a model
identity. **Zero unauthorized hardcoded English.** First slice in this whole where the leftover list is
empty of real findings — six slices after the report field was introduced.

## Slice S7 issued — Worker session 08, exchange 01, at `6ca85de`

`feat(i18n): localize the settings screen and the overlay stats bar`. Prompt staged at
`/tmp/opencode/uii-s7-worker-08-prompt.md`, 436 lines. Archive as `08_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2.

**38 new keys — the highest string volume of any slice in this whole**, plus the S6 leftover.

### Why settings is the right screen to do now

It is the screen where the player chooses their interface language, so an English settings screen is the
single most self-contradicting surface left in the product: you pick "Slovenčina" from a panel titled
"Interface language" surrounded by "Board Surface", "Shiny Effect" and "Premium Look".

### The one structural decision, and why the obvious shape is wrong

`TIMEOUT_CHOICES`, `STEP_CHOICES` and `BOARD_THEME_CHOICES` are **module-level constants** holding literal
English strings. A module-level constant cannot call a hook, so they must carry `TextKey` values resolved
at render time instead:

```ts
const TIMEOUT_CHOICES: Array<{ value: number; label: string; descriptionKey: TextKey }> = [
  { value: 30, label: "30s", descriptionKey: "settings.timeout.30" }, ...
];
```

⚠ The explicit `TextKey` annotation is the load-bearing part and the prompt says so: without it a typo in
a key name is a runtime `undefined` in rendered copy instead of a `tsc` error. The arrays must also STAY
module-level — moving them inside the component or converting them to functions would work but would
throw away the constant-folding and make the diff larger than the problem.

`ChoiceGrid`'s prop type changes from `description: string` to `descriptionKey: TextKey`. It is a local
component in the same file, so nothing else is affected; the prompt requires the Worker to verify that and
say so rather than assume it.

### Three things deliberately NOT localized, stated so nobody "finishes the job" later

```text
"Escape" at settings/page.tsx:515        a KeyboardEvent key name, not copy
TIMEOUT_CHOICES labels "30s" "1m" ...    compact unit abbreviations in a tight grid; `s` and `m` read
                                         internationally and translating them would break the layout
STEP_CHOICES labels "10" "20" ...        they are numbers
```

### The S6 leftover becomes three colon-labels

`{n} tried` / `{n} valid` / `{n} rejected` cannot be translated word-for-word: Slovak needs an adjective
agreeing in number AND case across one/few/many — "1 skúsený ťah", "2 skúsené ťahy", "5 skúsených ťahov" —
and no single form covers all three. So `Skúsené: 3` / `Platné: 3` / `Zamietnuté: 3`, which is the third
time this whole has used that pattern after `controls.tilesSelected` and `play.humanQueue.queueFor`. The
prompt also requires preserving today's behaviour that the `rejected` span renders empty at zero rather
than "Zamietnuté: 0".

### Orchestrator pre-verification before issuing

```text
AC-TOGGLE-4   the four toggle *Desc values are distinct within every locale (4/4 in all four).
              That assertion exists because the two toggle panels SHARE their On/Off labels but not
              their descriptions, and a copy-paste would make them silently identical.
AC-STATS-4    no sk/cs/pl stats form contains `tried`, `valid` or `rejected`.        SATISFIABLE
              Noted and accepted: cs `Platné: 3` is identical to sk `Platné: 3` — the words genuinely
              coincide, and the assertion is per-locale content rather than cross-locale difference.
AC-KEYTYPED   a new runtime assertion that every key in the three arrays resolves to a NON-EMPTY string
              in all four locales. `tsc` is the real gate; this catches a key that exists but is empty,
              which the type system cannot see.
```

### The telemetry deferral is re-asserted, not assumed

`AC-NO-TELEMETRY-KEY` already exists and must keep passing with 38 more keys in the catalog. The prompt
restates in full why `{humanState}` stays English — locked move route, prose comparison in
`describeAiTurnTelemetry`, enum redesign needed — because this is the first slice since that guard was
written whose author might reasonably think "while I am in this file anyway".

## Slice S6 landed at `6ca85de7ee1e5a1db33253eeb9e7e47922e2718a` — Worker session 07, exchange 01

`feat(i18n): localize the game header and the AI overlay`. 8 files, +253 −17, parent `d40b230`, one
non-force push, public readback equal. Orchestrator verdict: **implementation-PASS, ACCEPTED**, with one
leftover routed to S7. Evidence non-independent.

Archived as `07_implementation_00.md` + `07_report_00.md`.

Thirteen new keys, five existing keys reused. The chrome the player looks at during every turn — the
header cluster and the AI overlay — is now in four locales.

### Verified rather than accepted

```text
allowlist       8 files, all inside it. types.ts, ai-move-stream.ts and game/[id]/page.tsx UNTOUCHED.
{humanState}    still read and still rendered; 3 occurrences in AIThinkingOverlay. The deferral holds.
gates           mypy 83 · ruff · check · pytest 381/4 · typecheck 0 · vitest 386 passed | 3 skipped
                · lint 0 · build 0 with 11 dynamic and ZERO static routes
```

`AC-NO-TELEMETRY-KEY` was **already passing before the change** and the Worker said so rather than
claiming a pre-fix failure. That is the correct report of a guard test: it locks a property that was
already true and must stay true. It is now green with thirteen more keys in the catalog.

### ⛔ FIFTH ORCHESTRATOR INVENTORY MISS — and this time it produced a real methodological fix

Report item 13 names a leftover: `AIThinkingOverlay.tsx:369-373`, the stats bar —
`{aiCandidates.length} tried`, `{validSorted.length} valid`, `` `${rejectedCount} rejected` ``. Three
user-facing strings with no authored key. Confirmed.

Cause, diagnosed rather than hand-waved: my inventory regex was
`>\s*([^<>{}]*?[A-Za-z][^<>{}]*?)\s*<`. The character class forbids `{`, so a text node whose
EXPRESSION COMES FIRST — `>{expr} tried<` — cannot match. That is a fourth distinct sub-case of the same
class:

```text
S3b  Board.tsx `zoom`              a plain text node, missed by writing the prompt from a narrow grep
                                   AFTER a broad inventory had counted more
S3c  `Invalid Word{...}!`          text then expression, and the expression contains `>`, which
                                   `[^<>]` forbids
S3c  `AI route failed (${...})`    a template literal with no capitalised word, so a `[A-Z][a-z]{2,}`
                                   filter rejected it
S6   `{expr} tried`                expression then text, which `[^<>{}]` forbids
```

**Four sub-cases, four different regexes needed, and each regex I wrote had its own blind spot.** The
durable conclusion is unchanged and now proven five times: the STRUCTURAL defence — the report field
obliging the Worker to enumerate every user-facing English string it can still see — is the control that
works. It has caught a leftover in four consecutive slices.

#### But one concrete tool improvement was worth making, and it was validated against the misses

A v1 attempt stripped `{...}` from the whole file first. **It was catastrophically wrong and measuring it
is what revealed why:** TSX braces are not only JSX expression containers, they are also every block,
object literal and destructuring pattern, so repeated stripping collapsed a 12 715-character file to 586
characters and found nothing. Recorded because "strip the braces first" is the obvious idea and it is
wrong.

The working order is the reverse — capture the candidate segment with a class that allows BOTH braces and
`>`, then strip `{...}` inside that segment only, and discard segments left with unbalanced braces:

```python
for m in re.finditer(r'>([^<]*)<', s, re.S):
    seg = m.group(1)
    for _ in range(8):
        new = re.sub(r'\{[^{}]*\}', ' ', seg)
        if new == seg: break
        seg = new
    if '{' in seg or '}' in seg: continue      # not a clean text node
```

Validated against all four historical misses before use: `zoom` found, `Invalid Word...!` found,
`Last error:` found, and the stats trio found. Stored at `/tmp/opencode/jsxsweep.py`. It is a better tool,
**not a replacement for the report field.**

#### The remaining surfaces, swept with the validated tool

```text
settings/page.tsx                 4 text nodes    (its ~40 strings are mostly quoted literals, not nodes)
GameHistoryPanel.tsx             13
ProfileModal.tsx                 14
GameHistoryModal.tsx              3
AIThinkingOverlay.tsx             2   <- the leftover trio, `rejected` being a template literal
```

That is now a measured inventory for S7 and S8 rather than an estimate.

### The stats trio needs a colon-label, not a plural

`3 tried` / `3 valid` / `3 rejected` cannot be translated word-for-word: Slovak would need agreement in
number and case across one/few/many — "1 skúsený ťah", "2 skúsené ťahy", "5 skúsených ťahov" — and no
single adjective form covers all three. The established pattern in this whole applies:
`Skúsené: 3` / `Platné: 3` / `Zamietnuté: 3`, grammatically inert at every count, exactly as
`controls.tilesSelected` and `play.humanQueue.queueFor` already are. Routed to S7.

### Two layout risks the Worker named and did not change

```text
header.givingUp   pl "Poddaję się..."   in a whitespace-nowrap xl text button
header.loggingOut pl "Wylogowuję..."    same
overlay.filtering the longest string in the slice, text-xs centred inside max-w-lg — should wrap
```

It also noted that the CSS `uppercase` class stays on `overlay.aiThinking` and `overlay.best`, which is
precisely why `overlay.bestBadge` carries its own pre-uppercased value. Both go into the next acceptance
batch.

### One precision correction the Worker made to the prompt

Section 5 of the prompt was headed "seven existing keys" while its table listed five. The Worker reused
the five that were actually specified and said so, rather than inventing two more. Orchestrator drafting
error, no product impact, and the honest reading was the right one.

### Cooperator acceptance batch B22 — 8 of 8 PASS, plus one unprompted find


His reply, verbatim: `B22-1 PASS B22-2 PASS vidim "Front: Čeština" B22-3 PASS B22-4 PASS B22-5 PASS
B22-6 PASS B22-7 PASS + vidim tam Searching for moves.. alebo take nieco stale v anglictine B22-8 PASS`

```text
B22-1  /play fully localized in sk / cs / pl                                        PASS
B22-2  the queue label reads "Front: Čeština" for a Czech variant                   PASS, quoted
B22-3  the waiting room is localized, including "Miestnosť <code>"                  PASS
B22-4  the websocket does NOT tear down while waiting                               PASS
B22-5  the settings rival panel says "Tvoj súper", not "Choose the rival"           PASS
B22-6  the rival name is no longer clickable but is still visible                   PASS
B22-7  the AI status line shows a NAME, not a raw model id                          PASS
B22-8  the longest error string wraps without overflow                              PASS
```

**This is the first fully itemized PASS batch in this whole**, and four of the eight items are rendered
acceptance of Orchestrator-found defects:

```text
B22-2  uii-01-F14   he QUOTED the corrected string back — "Front: Čeština" — which is the strongest
                    form of confirmation available for a defect whose symptom was a wrong variant name
B22-4  the S5 Worker's own near-miss: had `useT`'s unstable `t` gone into that effect's deps, the
                    websocket would have been torn down on every state update on the one screen whose
                    purpose is holding it open. PASS is the rendered proof the fix works.
B22-5  uii-01-F10   the panel no longer promises a control that does not exist
B22-7  uii-01-F11   the player no longer sees `nvidia/nemotron-3-super-120b-a12b`
```

Together with `B20-5` (an AI game still plays after R6) and `B19-1..5` (the lexicon and toast fixes),
every Orchestrator-found defect corrected in this whole now has Cooperator-verified rendered evidence.

#### His unprompted find on B22-7 — and it is exactly the surface I had scheduled next

*"vidim tam Searching for moves.. alebo take nieco stale v anglictine"*. Measured immediately rather than
assumed: `AIThinkingOverlay.tsx:355` `Searching for moves...` and `:333`
`Filtering weak or invalid lines before showing a serious move...`, plus `AI Thinking` at `:287`,
`Best` / `BEST` at `:305` and `:122`, and `pts` at `:110`.

Six strings, and **the overlay is on screen during every single AI turn** — roughly 21 seconds per turn
by the measured central product fact. He is right that it is one of the most-seen surfaces in the product.

⚠ **The overlay had been deferred as a whole, and that was too coarse.** It was deferred because it
renders `{humanState}` at `:234`, the AI telemetry prose that needs an enum-keyed redesign. But the
telemetry is ONE of the seven things it renders; the other six are ordinary copy with no coupling to the
locked move route at all. Splitting the file's copy from its telemetry is both possible and cheap, and
treating the file as atomic hid six high-visibility strings behind one architectural blocker.

Last used batch prefix is now **B22**.

## Slice S6 issued — Worker session 07, exchange 01, at `d40b230`

`feat(i18n): localize the game header and the AI overlay`. Prompt staged at
`/tmp/opencode/uii-s6-worker-07-prompt.md`, 352 lines. Archive as `07_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E1.

### Scope, and why it is deliberately NARROWER than planned

The plan had S6 as ScorePanel plus the whole settings remainder. Measured inventory: ScorePanel 14
distinct strings, settings **40**, overlay 6. The S5 Worker reported visible context above 70 percent on a
smaller surface than that, so combining them would invite a compaction mid-slice on a 40-string screen.

```text
S6  ScorePanel + AIThinkingOverlay   13 new keys + 5 reuses   <- ISSUED, this slice
S7  settings remainder                ~40 strings, its own slice
S8  GameHistoryPanel + GameHistoryModal + ProfileModal + uii-01-F03 dates
S9  uii-01-F02 accessible names
```

The split is by SURFACE, not arbitrary: S6 is the chrome visible during a turn, S7 is a screen you visit
between games. That also puts his unprompted find into the very next slice.

### Five existing keys reused rather than duplicated

`nav.settings`, `chat.you`, `game.newGame`, `game.starting`, `board.pts`. Verified present in all four
catalogs before writing the prompt. One accepted wart, named in the prompt: `game.newGame` is spelled
"New Game" in the en catalog while ScorePanel's literal is "New game" — one key with one casing beats two
keys with drifting Slovak.

### The deferral is now PINNED BY A NEGATIVE TEST, not by prose

`AC-NO-TELEMETRY-KEY` asserts that **no** key in the en catalog contains `providers exhausted`,
`dead rack` or `legal rescue`. Without it, a future copy slice could quietly localize the telemetry
through the message catalog instead of through the enum redesign — which would rebuild the
`err.message.includes("401")` anti-pattern the security era paid to remove, and which `uii-01-F09` already
had to correct once in this same whole. A prose instruction would not have survived three more slices; an
executable assertion will.

### One typography decision worth recording

`overlay.best` and `overlay.bestBadge` are two keys for one word. The badge at `:122` renders uppercase
through a CSS class today, and CSS `text-transform: uppercase` on Slavic diacritics is less dependable
across this project's fallback font stack than it is for ASCII. The badge therefore carries its own
pre-uppercased value — `NAJLEPŠÍ` / `NEJLEPŠÍ` / `NAJLEPSZY` — and `AC-BADGE-CASE` asserts it equals its
own uppercase form in every locale. Orchestrator-verified satisfiable before issuing.

## Slice S5 landed at `d40b230e8071f609f1a26fbea70106664326673a` — Worker session 06, exchange 01

`feat(i18n): localize the lobby screens and fix the queue label`. 11 files, +406 -70, parent `383011b`,
one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS, ACCEPTED**, with
one cosmetic residual recorded. Evidence non-independent; rendered acceptance requested as batch `B22`.

Archived as `06_implementation_00.md` + `06_report_00.md`.

**Both lobby screens are now in four locales and all four open corrections are closed.**
`/play` 23 keys, `/waiting` 10 keys, plus `nav.*`, `queue.*` and `settings.rival.*`.

### uii-01-F14 verified by an independent readback through the real code path

Not accepted from the Worker's test. A throwaway vitest harness was placed in the tree, run against the
**shipped** catalogs through the real `tf()` and the real `variantDisplayName()`, and removed immediately
(porcelain verified clean afterwards):

```text
        english            slovak              czech            polish            hungarian
en      English queue      Slovak queue        Czech queue      Polish queue      hungarian queue
sk      Front: Angličtina  Front: Slovenčina   Front: Čeština   Front: Poľština   Front: hungarian
cs      Fronta: Angličtina Fronta: Slovenština Fronta: Čeština  Fronta: Polština  Fronta: hungarian
pl      Kolejka: Angielski Kolejka: Słowacki   Kolejka: Czeski  Kolejka: Polski   Kolejka: hungarian
```

Compare the defect this replaces: `czech -> "English queue"` and `polish -> "English queue"`. All four
installed variants now name themselves in every locale; the Czech label in the Slovak locale contains
neither `Angličtina` nor `Slovenčina`, and no locale's Czech label contains the word `English`.

### The other three corrections, verified in source

```text
uii-01-F10  settings/page.tsx now uses `settings.rival.title` / `settings.rival.description` —
            "Tvoj súper" plus "Súpera pre nové partie vyberá správca." The title no longer instructs
            the user to choose something they cannot choose.
uii-01-F11  game/[id]/page.tsx:845-851 resolves a NAME before interpolating:
              gameState.ai_model_display_name when preferenceModelId matches the session's model,
              else humanizeModelId(preferenceModelId), else the id as a last resort.
            ⛔ THE CRITICAL PART: `preferenceModelId` at :833 is unchanged and is still what reaches
            `buildFallbackQueue`, `fallbackQueueForCatalogFailure` and `aiMoveRequestBody` at :861,
            :868 and :911. `lib/ai-fallback.ts` diff is EMPTY. Only what is DISPLAYED changed.
uii-01-F12  `showRivalPicker` and `onOpenRivalPicker` return ZERO matches in both ScorePanel.tsx and
            game/[id]/page.tsx. The rival NAME still renders as static text at ScorePanel.tsx:394,
            which is what the Cooperator's `zrušiť` meant — remove the click, not the information.
```

### Gates at `d40b230`, Orchestrator-measured

```text
mypy 83 files · ruff · manage.py check · pytest 381 passed, 4 skipped in 218.75s
typecheck exit 0 · vitest 382 passed | 3 skipped (378 + 4 new) · lint exit 0
build exit 0, 11 dynamic routes, ZERO `○` static
```

An independent word-based leftover-English sweep of both lobby files returns **zero candidates**. The
report's item-15 list is therefore complete: what remains is only `err.message` passthrough from the API,
the catalog `display_name`, and `providerBadgeLabel(...)` — none of which is this project's copy.

### uii-01-F15 — the F14 fallback shows a raw lowercase slug, not the manifest display name

    Classification:  cosmetic residual introduced by the uii-01-F14 fix, NOT reachable today
    Severity:        info
    Confidence:      high
    Evidence class:  reproduced-dynamic — the Orchestrator rendered the label for a fifth slug through
                     the real code path and observed `Front: hungarian`
    Location:        frontend/src/app/play/page.tsx:61-67 — the page constructs a SYNTHETIC
                     `VariantSummary` as `{ slug, display_name: slug, language_code: null,
                     readiness: "playable" }` rather than fetching the real one.
    Mechanism:       `variantDisplayName` falls back to `display_name` when a slug has no
                     `VARIANT_NAME_KEYS` entry. The real `GET /api/game/variants/` payload carries a
                     proper manifest `display_name`, but the synthetic object throws it away and passes
                     the slug, so an unkeyed variant renders lowercase and untranslated.
    Why NOT reachable today: all four installed slugs — english, slovak, czech, polish — have catalog
                     keys in all four locales, verified by the readback above.
    Why it is nearly unreachable in future too, which is why this is `info` and not a defect: the
                     fallback is only reached by a variant with no catalog key, and the whole that ADDS a
                     variant is the same whole that adds its `settings.gameVariant.*` key. `11/02`
                     Hungarian activation would add `settings.gameVariant.hungarian` and close this path
                     in the same commit that could open it.
    Trade-off the Worker chose deliberately and disclosed: not fetching the variant list on mount avoids
                     an extra network round trip on every `/play` load purely to label a pill. That is a
                     defensible call and it is strictly better than the F14 bug it replaces — a lowercase
                     honest slug versus a confidently WRONG variant name.
    Correction direction: if `11/02` ever ships a variant without a catalog key, fetch the real
                     `VariantSummary` on mount alongside the existing model-catalog fetch and drop the
                     synthetic object. Do not add per-locale queue strings.
    Regression test: not required at `info`. If corrected, assert that an unkeyed slug renders its
                     manifest `display_name` rather than the slug.
    Owner:           accepted residual; revisit only if `11/02` adds a variant without its catalog key
    Status:          accepted-residual (Orchestrator, below the INFOSEC 14 medium threshold)

### A genuine near-miss the Worker caught in itself, and it is a good one

Putting `useT()`'s `t` into the waiting-room `useEffect` dependency list would have recreated the closure
on every render and **torn down and reopened the websocket on every state update** — in the one screen
whose entire purpose is holding a websocket open while waiting for an opponent. It resolved it by using
the module-level `t(locale, key)` inside effects with the string `locale` in the deps, keeping `useT` for
JSX only.

⚠ It also disclosed that **the same `useT`-in-deps pattern already exists in `game/[id]/page.tsx`** and was
out of scope. Recorded as a latent item to check when a later slice next opens that file: whether any
effect there has an unstable `t` in its dependency list, and whether that effect owns a socket or a timer.
Not a finding yet — it is `not established` whether the game page's effects are affected — and it must not
be treated as one until measured.

### Context-pressure disclosure, recorded rather than ignored

Report item 16 states visible context usage exceeded 70% of the session window, driven by the mandatory
reading plus four catalogs and two full pages. It completed against repository evidence rather than
compacted memory and said so. That is the required behaviour, and it is a routing signal: the remaining
copy slices S6, S7 and S8 should each be scoped tighter than this one rather than combining screens.

## Slice S5 issued — Worker session 06, exchange 01, at `383011b`

`feat(i18n): localize the lobby screens and fix the queue label`. Prompt staged at
`/tmp/opencode/uii-s5-worker-06-prompt.md`, 470 lines. Archive as `06_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2 because it carries four corrections rather than pure
string extraction.

Scope: the two lobby screens — `/play` 398 lines and `/waiting/[id]` 144 lines — plus the four open
corrections that live on surfaces the slice already opens.

### Why `/play` jumped the queue in the plan

The Cooperator volunteered it unprompted at the end of batch B20: *"cela stranka 'Choose the next board'
komplet je stale v anglictine"*. It was correctly in scope for the later S3e, but he raised it himself and
`/play` is the screen he lands on after login. This project's record is that his unprompted remarks are
worth acting on — the nginx answer and the dictionary re-sourcing both came that way — so `/play` and
`/waiting` moved out of S3e and into this slice, and ScorePanel plus the settings copy remainder moved
back to S6.

### The four corrections, and why none of them is a translation

```text
uii-01-F10  settings still titled "Choose the rival" after S4 made the panel read-only. REPLACED, not
            translated — a translated lie is still a lie. New copy: "Your rival" / "Tvoj súper" plus a
            description naming the administrator as the one who picks it.
uii-01-F11  the AI status line interpolates a raw model_id. The defective string is the ORCHESTRATOR's
            own, authored in S3c, and S4 fixed the same class of leak on the draw page while leaving
            this one. Fix passes a display NAME; the strings themselves do not change.
uii-01-F12  the rival-name click is REMOVED per Cooperator decision B20-8 (`zrušiť`), not renamed.
uii-01-F14  the queue label's two-value ternary, fixed by COMPOSITION rather than by four more strings.
```

### The F14 fix is deliberately structural, not additive

The obvious fix — four per-locale queue strings — would let a fifth variant reintroduce exactly the same
bug. Instead the label is composed from the variant name the catalog already owns:
`GameLanguagePanel.tsx` already exports `variantDisplayName(variant, t)` over `VARIANT_NAME_KEYS` with a
`display_name` fallback, and the `settings.gameVariant.*` keys already exist in all four locales. The
prompt forbids duplicating `VARIANT_NAME_KEYS` into a second table and requires the Worker to state which
lookup shape it chose and why.

One parameterized key does the rest, and the Slavic forms are a colon-label for the same grammatical
reason `controls.tilesSelected` is: a natural phrase would need the variant name in an oblique case
("slovenský front"), while the name arrives as a nominative label. A colon-label is inert for every
variant including a future one.

### Orchestrator pre-verification, computed against the REAL catalogs before issuing

The four `settings.gameVariant.*` values were read out of all four shipped catalogs rather than assumed,
then the label was rendered for every (slug, locale) pair:

```text
english  en 'English queue'  sk 'Front: Angličtina'  cs 'Fronta: Angličtina'  pl 'Kolejka: Angielski'
slovak   en 'Slovak queue'   sk 'Front: Slovenčina'  cs 'Fronta: Slovenština' pl 'Kolejka: Słowacki'
czech    en 'Czech queue'    sk 'Front: Čeština'     cs 'Fronta: Čeština'     pl 'Kolejka: Czeski'
polish   en 'Polish queue'   sk 'Front: Poľština'    cs 'Fronta: Polština'    pl 'Kolejka: Polski'

versus the CURRENT buggy behaviour the test must fail against:
english -> 'English queue'   slovak -> 'Slovak queue'
czech   -> 'English queue'   polish -> 'English queue'      <- the defect, twice
```

`AC-QUEUE-VARIANT` is therefore both satisfiable and discriminating: the czech case in the sk locale
contains neither `Angličtina` nor `Slovenčina`, and no locale's czech label contains the word `English`.

### Two smaller things folded in

```text
nav.settings / nav.account   authored NOW as shared keys, precisely so slice S6 does not duplicate them
                             when it localizes ScorePanel's own Settings button
play.rival.unavailable       play/page.tsx:57-58 currently uses the whole CATALOG_EMPTY_MESSAGE sentence
                             as the label inside a small pill. A short label is authored for the pill
                             while the full sentence stays in the error area.
```

Also carried forward as a named non-action: `settings/page.tsx` keeps a `rivalSectionRef` and a
`?focus=rival` query path whose only link F12 removes. Leaving it is harmless, removing it is not
authorized here, and the prompt requires the Worker to name it rather than tidy it.

### uii-01-F14 — a Czech or Polish player is told they are joining the "English queue"


    Classification:  product-defect (factually false user-facing label), PRE-EXISTING and REACHABLE NOW
    Severity:        low functionally, medium for interview presentability
    Confidence:      high
    Evidence class:  established-static — the Orchestrator read the expression and the installed
                     variant directory
    Found by:        the Orchestrator while inventorying `/play` for slice S5
    Location:        frontend/src/app/play/page.tsx:337-339
                       : selectedVariantSlug === "slovak"
                           ? "Slovak queue"
                           : "English queue"
    Mechanism:       a TWO-VALUE test written when only English and Slovak variants existed. Measured:
                     `backend/assets/variants/` contains czech.json, english.json, polish.json and
                     slovak.json, and `selectedVariantSlug` has been typed `string` since era 11 with
                     fetch-time reconciliation. Anything that is not exactly "slovak" therefore renders
                     "English queue".
    Impact:          a player who has selected the Czech or Polish game variant and joins the human
                     queue is told they are joining the ENGLISH queue. The label is not merely
                     untranslated, it is FALSE about which game they are about to play.
    ⛔ THIS IS THE SAME DEFECT CLASS AS uii-01-F08, in a second file. F08 was the lexicon rejection
                     message; this is the queue label. Both are two-value ternaries left behind when era
                     11 slice A1 activated Czech and Polish, and neither was caught because no test
                     renders either string. That makes it a PATTERN rather than an incident: any
                     `=== "slovak" ? … : …` expression in the frontend is now suspect.
    Orchestrator sweep, with the exact patterns and ALL four matches stated rather than a count:
                     `grep -rn '=== "slovak"\|=== "english"\|!== "slovak"\|!== "english"' frontend/src`
                       play/page.tsx:337        THIS FINDING
                       useGameStore.ts:280      the `version < 2` persist branch — deliberate legacy
                                                handling of a payload written when the union had two
                                                values. Correct as-is; do not "modernise" it.
                       prompts.ts:198 and :208  `context.lexicon_id === "slovak" || context.variant ===
                                                "slovak"`. These are the ALREADY-RECORDED era-11 finding
                                                that Czech and Polish receive the ENGLISH MOVE/JUDGE
                                                prompt CORE, because `MovePromptLexiconId` is
                                                `"collins2019" | "slovak"`. prompts.ts is LOCKED (locked
                                                fork 2) and this is not S5's to touch.
                     ⚠ An earlier draft of this entry said "no third instance exists". That was WRONG —
                     it counted before it enumerated, which is the exact failure this project keeps
                     recording. There are four matches; two belong to a locked file and a known finding,
                     one is deliberate, one is this defect.
    Correction direction: reuse the variant name the catalog already provides. `GameLanguagePanel.tsx`
                     already exports `variantDisplayName(variant, t)` over `VARIANT_NAME_KEYS`, and the
                     `settings.gameVariant.*` keys already exist in all four locales. Compose the label
                     from that rather than adding four more per-locale queue strings, so a fifth variant
                     never reintroduces the bug.
    Regression test: with `selectedVariantSlug: "czech"` the rendered queue label must NOT contain the
                     English or Slovak variant name. Must fail before the fix.
    Owner:           ui-internationalization, slice S5
    Status:          open
    Status:          **corrected at d40b230** (S5) — NOT verified-closed. Composed from
                     `variantDisplayName` + `play.humanQueue.queueFor`; the two-value ternary returns ZERO
                     matches in play/page.tsx. Orchestrator-verified by rendering all four installed
                     slugs in all four locales through the real code path. Residual uii-01-F15 records
                     the lowercase-slug fallback for an unkeyed fifth variant.

### COOPERATOR DECISION 9, 2026-09-02: B21 is FROZEN and admin work leaves this whole


Verbatim: *"PROSIM daj B21 do backlogu pripadne vytvor na zaklade vsetkeho co sa tyka admin rozhrania
chcem v logickom celku v meta libretiles/11/00-admin-provider-model-console tam budem riesit vsetko
ohladom admina takze daj tam aj toto, ze je NOT TESTED teraz dokoncme prosim tvoj logicky celok, admin
bola odbocka, je to najdolezitejsie pre mna okrem hry proti AI a lokalizacia + UI/UX perfektne.. Toto sa
ale netyka tvojho logickeho celku prosim Freeze B21"*

**He is right and the Orchestrator was drifting.** Batch B21 would have had him log into Django admin,
reorder catalog rows and inspect `GameSession` rows — none of which is `ui-internationalization`. R6
removed a player-facing control, which IS this whole's work; verifying the admin surface that now owns the
setting is `11/00`'s work. The Orchestrator had followed the evidence across a boundary instead of
depositing it and stopping.

```text
B21             FROZEN, every item NOT TESTED. Not an open obligation on 10/00.
Admin scope     leaves this whole entirely
Deposited to    11/00-admin-provider-model-console/90_admin_surface_evidence_from_era10.md
His priority    game-vs-AI first, then localization + UI/UX "perfektne", then admin
```

`11/00`'s own `00_handout.md` was **not** read while writing that deposit — his standing
do-not-read instruction for that directory is unchanged — so the file says in terms that the handout is
that whole's own artifact and wins on any overlap.

What the deposit carries, so no measurement is lost: Django admin reachable on **port 8000** with a
`302 -> /admin/login/ -> 200` readback and an existing superuser; the full `AIModel` and `AIPrompt` tables
with `sort_order` and `is_active`; proof that **row 1 is already admin-settable** through
`list_editable` plus the two `_resolve_*` defaults, which corrects the plan's own too-pessimistic claim;
the `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` caveat; the frozen B21 items; and the two traps — that a naive
"reorder and see" test is invalid while a per-user `preferred_ai_model_id` outranks row 1, and that
`selectedModelId` feeds fallback attempt 1 and must never be deleted.

**Consequence for `10/00`'s closure conditions.** Handout section 11 item 3 requires "the player no longer
chooses a model or a prompt preset". That is satisfied at `383011b` and Cooperator-verified by `B20-5`.
It does NOT require the admin side to be demonstrated, and after decision 9 it must not: closure item 3 is
**met**. Everything remaining in this whole is copy, accessibility, Django localization, and the three
security residuals.

### Cooperator acceptance batch B20 — 3 answered, 1 FAIL that is an ORCHESTRATOR instruction defect

His reply, verbatim: `B20-5 PASS B20-6 FAIL localhost:3000/admin vracia 404 This page could not be found.
B20-8 zrušiť B20-9 ano cela stranka "Choose the next board" komplet je stale v anglictine`

```text
B20-5  an AI game still plays normally                                    PASS  <- the critical one
B20-6  admin sets catalog row 1 from Django Admin, no SSH                 FAIL — see below
B20-8  should the rival-name click be kept or removed?                    "zrušiť" = REMOVE
B20-9  the known leftovers                                                CONFIRMED, plus a new report
B20-1..4, B20-7                                                            NOT TESTED
```

**B20-5 PASS is the one that mattered most.** It is the rendered evidence that removing the picker did
not break the provider fallback queue — the single risk the S4 prompt spent a whole section guarding.

#### ⛔ B20-6 is NOT a product defect. It is an Orchestrator instruction defect.

He opened `localhost:3000/admin` and got Next.js's 404. **Django admin is on port 8000, not 3000.** The
batch said "v Django Admin (/admin/)" without a port, and he is a self-described operations novice, so an
ambiguous URL is the Orchestrator's failure, not his. `PROJECT_CONTEXT.md` section 2 is explicit: make his
steps unambiguous instead.

Measured before telling him anything, rather than asserted:

```text
ss -tlnp        127.0.0.1:8000 python (Django)      *:3000 next-server
Next.js routes  /  ·  /play  ·  /settings  plus the dynamic ones — there is correctly NO /admin,
                so the 404 he saw is Next.js behaving properly
GET http://127.0.0.1:8000/admin/   -> HTTP 302 -> /admin/login/?next=/admin/ -> HTTP 200, 4173 B
                <title>Log in | Django site admin</title>
superuser       EXISTS: id=1 'admin', is_staff=True, is_superuser=True
```

So the test is fully performable and nothing is broken. Reissued in batch B21 with the full URL.

#### ⛔ AND A SUBTLETY THAT WOULD HAVE MADE THE RETEST FAIL FOR THE WRONG REASON

Read from source rather than guessed — `frontend/src/lib/model-catalog.ts:95-103`:

```ts
if (preferredId && eligibleIds.includes(preferredId)) return preferredId;   // per-user, admin-settable
if (storedId    && eligibleIds.includes(storedId))    return storedId;      // device memory
return eligibleIds[0] ?? null;                                              // catalog row 1
```

And the live database says:

```text
user id=1 'admin'  preferred_ai_model_id = 'nvidia/nemotron-3-super-120b-a12b'   (eligible, active)
get_selectable_models() -> 5 rows, ROW 1 = google/gemma-4-31b-it:free  (sort_order 10)
   nvidia/nemotron-3-super-120b-a12b is sort_order 20
get_selectable_prompts() -> 4 rows, ROW 1 = Grandmaster (sort_order 5); Initial is 10
```

**He plays as `admin`, whose per-user preference is already set and eligible.** So reordering
`sort_order` alone would change row 1 and change nothing about his game, because his own
`preferred_ai_model_id` wins the precedence. He would have seen "no effect" and reasonably concluded R6
does not work.

That is not a defect — per-user preference beating the global default is correct and is itself
admin-settable — but it makes the naive test invalid. B21 therefore gives him **two** demonstrations:
clear `preferred_ai_model_id` on his user and then reorder to prove the global default, or set
`preferred_ai_model_id` directly to prove the per-user override. Both are Django Admin, both without SSH.

Recording this because "the retest would have failed for a reason unrelated to the thing under test" is
exactly the shape of evidence that gets misread as a product failure.

#### B20-8 answered: `zrušiť` — the rival-name click is REMOVED

That settles `uii-01-F12`. `showRivalPicker`, `onOpenRivalPicker` and the header click navigation to
`/settings?focus=rival` are removed rather than renamed. A Cooperator decision, not an Orchestrator
choice.

#### B20-9 plus an unprompted report that changes the plan

He confirmed the two known leftovers and added: **`cela stranka "Choose the next board" komplet je stale
v anglictine`** — the entire `/play` page. That is true and was the declared scope (S3e owned play and
waiting), but he volunteered it, and `/play` is the screen he lands on after login. The previous era's
most valuable moments came from exactly this kind of unprompted remark, so it is treated as a
prioritisation signal rather than as a re-report of known scope.

**Slice order revised:** `/play` and `/waiting` move OUT of the later S3e and INTO S5, together with the
three open corrections. The ScorePanel and the settings copy remainder move to S6.

```text
S5  play + waiting full copy · F10 settings panel title · F11 raw model id in the AI status line
    · F12 remove the rival-name click                                   <- next
S6  ScorePanel + the settings copy remainder
S7  GameHistoryPanel + GameHistoryModal + ProfileModal + uii-01-F03 dates
S8  uii-01-F02 accessible names, authored straight into the catalog
then R7/R8 Django i18n + Retry-After · R10 nonce CSP · R11 catalog proxies + F13 · acceptance
```

Last used batch prefix is now **B20**.

## Slice S4 landed at `383011b389a9b3690647b6fa673060633572ab9d` — Worker session 05, exchange 01


`feat(ui): the player no longer chooses the AI model or the prompt preset`. 15 files changed, **two
deleted**, +214 −674 — a net removal of 460 lines. Parent `e0d3b64`, one non-force push, public readback
equal. Orchestrator verdict: **implementation-PASS, ACCEPTED**, with four follow-ups routed to S5 and
R11. Evidence non-independent; rendered acceptance requested as batch `B20`.

Archived as `05_implementation_00.md` + `05_report_00.md`.

**R6 is delivered. This is the Cooperator's stated single most important product outcome.** The player
no longer chooses the AI model or the prompt preset; both defaults come from Django Admin catalog row 1;
a player sees only a display name.

### The three audits the prompt demanded, all re-verified by the Orchestrator

```text
1  BACKEND UNTOUCHED       git diff --name-only e0d3b64 383011b -- backend/   ->  0 files
                           migrations touched                                 ->  0 files
                           preferred_ai_model_id, its migrations, its admin field and its
                           is_selectable_model validation are all byte-identical
2  selectedModelId SURVIVES  useGameStore.ts:37-38 interface, :138-139 initial + setter,
                           :319 partialize; game/[id]/page.tsx:833 preferenceModelId;
                           lib/ai-fallback.ts diff EMPTY
                           selectedPromptId now appears ONLY in the migrate delete and its own test
3  LOCKED FORKS INTACT     provider-registry, openai-compatible, ibm-watsonx, ai-runtimes,
                           catalog/selection.py, README.md, AGENTS.md, prompts.ts, constants.ts,
                           api.ts and proxy.ts — every one untouched. No provider or model added,
                           removed, renamed or reordered.
```

Audit 2 was the whole risk of the slice: `selectedModelId` feeds attempt 1 of the provider fallback
queue, and deleting it with the picker would have broken every AI turn while leaving all eight gates
green, because no test exercises the queue's preference input.

### Gates at `383011b`, Orchestrator-measured

```text
mypy 83 files · ruff · manage.py check · pytest 381 passed, 4 skipped in 222.35s
typecheck exit 0 · vitest 378 passed | 3 skipped · lint exit 0 · build exit 0, 11 dynamic, ZERO static
persist migration  `if (version < 5) { delete incoming.selectedPromptId; }` appended after the four
                   existing branches, all of which are intact
```

**The vitest-count accounting checks out exactly.** Test files in the tree: **29 before, 29 after** — no
test file was deleted, so 374 + 4 new = 378 and the two removed components genuinely had no tests of
their own. The prompt's "a drop needs an accounting" rule turned out not to be needed, but it was the
right rule to state.

The disclosed near-miss is verified recovered: deleting `persistModelSelection` briefly took the Escape
`useEffect` and `handleNewGame` with it, and both are present again at `settings/page.tsx:514` and `:526`.
Reported unprompted, which is the behaviour that makes the rest of the report trustworthy.

### FOUR follow-ups, three of them created or exposed by this slice

#### uii-01-F10 — the settings panel is titled "Choose the rival" but nothing can be chosen

    Classification:  product-defect (UI coherence), CREATED by this slice
    Severity:        low functionally, medium for interview presentability
    Confidence:      high
    Evidence class:  established-static — settings/page.tsx:622-623 read
                       title="Choose the rival"
                       description="Provider-diverse free rivals from the live catalog, newest first."
                     while the selectable rows, the click handler and `savingModelId` are all gone.
    Impact:          a user reads an instruction to choose and then looks for a control that does not
                     exist. "A control that does nothing" is explicitly a first-class defect in the
                     Cooperator's frame, and this is its inverse — copy that promises a control.
    Note:            this is NOT merely an untranslated string. S5 owns the settings copy, but the title
                     is now factually wrong and must be REPLACED, not translated. Something of the shape
                     "Your rival" / "Tvoj súper" plus a description saying the administrator sets it.
    Owner:           ui-internationalization, slice S5
    Status:          open
    Status:          **corrected at d40b230** (S5) — NOT verified-closed. Title/description replaced
                     with `settings.rival.title` / `settings.rival.description`, not translated.

#### uii-01-F11 — the AI status line shows a raw model id to the player, and it is the Orchestrator's own string

    Classification:  product-defect (leaks an internal identifier to a player)
    Severity:        low
    Confidence:      high
    Evidence class:  established-static — game/[id]/page.tsx:845
                       setAIStatusMessage(tf("game.ai.exploring", { model: preferenceModelId }))
                     and `preferenceModelId` is a raw catalog `model_id` such as
                     `nvidia/nemotron-3-super-120b-a12b`.
    Impact:          the player sees `Hľadám platné slová cez nvidia/nemotron-3-super-120b-a12b...`,
                     which contradicts the Cooperator decision this very slice implements — that a
                     player should only ever see the model's NAME.
    ORCHESTRATOR ORIGIN, stated plainly: `game.ai.exploring` is a string the Orchestrator authored in
                     slice S3c and it was authored to interpolate whatever the call site already had.
                     S4 then fixed the same class of leak on the draw page while leaving this one.
                     The defect is mine, not the Worker's; the Worker found and named it.
    Correction direction: pass the resolved `display_name` — the same value the settings panel and the
                     draw pill now show — and fall back to `humanizeModelId(...)` which the project
                     already uses for exactly this purpose.
    Regression test: with a catalog entry present, the rendered status message contains the display name
                     and does NOT contain a `/` character from a provider-qualified id.
    Owner:           ui-internationalization, slice S5
    Status:          open
    Status:          **corrected at d40b230** (S5) — NOT verified-closed. game/[id]/page.tsx:845-851
                     resolves a display NAME before interpolating; `preferenceModelId` still reaches the
                     fallback queue unchanged and `lib/ai-fallback.ts` is byte-identical.

#### uii-01-F12 — `showRivalPicker` still offers a picker affordance that leads to a read-only panel

    Classification:  product-defect (misleading affordance), consequence of this slice
    Severity:        low
    Confidence:      high
    Evidence class:  established-static — ScorePanel.tsx:260,263,278,281,398,401 and
                     game/[id]/page.tsx:1519 `showRivalPicker`, :1522
                     `onOpenRivalPicker={() => router.push("/settings?focus=rival")}`
    Impact:          clicking the rival name in the game header still navigates to settings expecting a
                     picker, and the prop name `showRivalPicker` is now a lie. Nothing is broken; the
                     destination is simply a read-only display.
    Correction direction: keep the navigation if a read-only "who am I playing" view is wanted, but
                     rename the props to say so, or drop the click entirely. A Cooperator preference
                     question rather than a pure defect — put it in B20 rather than deciding it alone.
    COOPERATOR DECISION, B20-8, 2026-09-02: `zrušiť` — REMOVE the click. `showRivalPicker`,
                     `onOpenRivalPicker` and the `/settings?focus=rival` navigation are deleted rather
                     than renamed. His decision, not an Orchestrator choice.
    Owner:           ui-internationalization, slice S5
    Status:          open — correction direction now fixed by his decision
    Status:          **corrected at d40b230** (S5) — NOT verified-closed. Both props return ZERO
                     matches in ScorePanel.tsx and game/[id]/page.tsx; the rival NAME still renders as
                     static text at ScorePanel.tsx:394. `?focus=rival` is now an unreachable inbound
                     path, deliberately left in place.

#### uii-01-F13 — `api.getPrompts` and the `/api/prompts` Next.js proxy are now dead code

    Classification:  dead code / attack-surface hygiene
    Severity:        info
    Confidence:      high
    Evidence class:  established-static — `grep -rn "getPrompts()"` outside `api.ts` returns ZERO call
                     sites; the build still lists `ƒ /api/prompts`.
    Impact:          a callerless Next.js route remains published. Not a vulnerability — it proxies a
                     read-only authenticated catalog list — but it is surface with no consumer.
    Note:            `/api/prompts` is one of the two catalog proxies in `audit-01-F06`, which slice R11
                     already owns. R11 should decide there: delete the proxy and `api.getPrompts`, or
                     keep them for the future `11/00 admin-provider-model-console` whole and say so.
                     Do NOT delete the Django `catalog/prompts/` endpoint — the admin console needs it.
    Owner:           ui-internationalization, slice R11
    Status:          open

### One unauthorized-but-proportionate change, disclosed and accepted

The five-card settings skeleton collapsed to a single pulse bar. Not in the prompt. Judged proportionate
and accepted: the five-card skeleton existed to match five selectable rival cards, and with a read-only
single name a five-card placeholder would actively mislead during load. It is a consequence of the
authorized removal rather than an independent redesign, it introduced no new copy, and it was disclosed.
Recorded rather than left implicit.

Also dead-code removals the Worker disclosed and the Orchestrator accepts: `accountSyncAvailable`,
`formatContextWindow`, `persistModelSelection`, and `humanizeModelId` in `play/page.tsx`. All became
unreachable when the click handler went.

### Cooperator acceptance batch B19 — blanket PASS, 2026-09-02


His reply, verbatim: `B19. PASS`. Fourteen items, recorded as a **blanket pass rather than fourteen
itemized results**, consistent with B16 and with his established style. Not re-queried for itemization
because he has explicitly asked to be asked less and a blanket `PASS` has one plain reading.

```text
B19-1   Czech game shows "Není v českém lexikonu", NOT Collins            PASS (blanket)
B19-2   Polish game shows "Nie ma w polskim leksykonie"                   PASS (blanket)
B19-3   English game still shows Collins Scrabble Words 2019              PASS (blanket)
B19-4   AI exchange shows the rack-refresh subtitle, not the no-move one   PASS (blanket)
B19-5   AI pass shows the no-move subtitle                                PASS (blanket)
B19-6   turn status in sk / cs / pl                                       PASS (blanket)
B19-7   game over, winner/draw wording, "Nová partia"                     PASS (blanket)
B19-8   the window.confirm give-up dialog is in Slovak                    PASS (blanket)
B19-9   in-game action buttons in three locales    (was B18-1, untested)  PASS (blanket)
B19-10  the three-form tile counter at 1 / 2 / 5   (was B18-2, untested)  PASS (blanket)
B19-11  blank-picker heading                       (was B18-4, untested)  PASS (blanket)
B19-12  b. / b. / pkt on tiles, and "Reset zoomu"  (was B18-5, untested)  PASS (blanket)
B19-13  rack empty state and chat                  (was B18-6/7, untested) PASS (blanket)
B19-14  the known English "Invalid Word(s)!" leftover                     CONFIRMED (blanket)
```

**Two things this closes that no automated gate could.** `B19-1` through `B19-3` are the rendered
acceptance of `uii-01-F08` — a Czech player is no longer told their word is missing from an English
dictionary — and `B19-4` / `B19-5` are the rendered acceptance of `uii-01-F09`, the data-keyed toast
subtitle. Both defects were found by the Orchestrator during inventory, corrected in one slice, and are
now Cooperator-verified in the running product.

It also closes the six `NOT TESTED` items carried forward from B18, so there is no longer an untested gap
behind the localized turn surface. Last used batch prefix is now **B19**.

### R6 reconnaissance — the backend already does exactly what R6 needs, measured not assumed

Performed by the Orchestrator before writing the S4 prompt, because R6 is the Cooperator's stated single
most important outcome and it touches the AI turn path.

```text
backend/game/services.py:366-384  _resolve_ai_model
    ai_model_model_id omitted -> `return selectable_models[0] if selectable_models else None`
backend/game/services.py:386-393  _resolve_ai_prompt
    ai_prompt_id omitted      -> `return selectable_prompts[0] if selectable_prompts else None`
backend/game/serializers.py:174-175   BOTH fields are `required=False`
```

**So R6 needs ZERO backend change.** Omitting both fields from the create request makes the backend pick
row 1 of each catalog, and both catalogs are ordered `("sort_order", ...)` with `sort_order` in
`list_editable` in Django Admin (`catalog/admin.py:43` and `:113`).

⚠ **A correction to the plan's own claim, in his favour.** `92_orchestrator-glossary-and-plan.md` slice
S4 says this "does NOT deliver 'the admin sets the GLOBAL default', which is still catalog row 1
determined in code". Measured: catalog row 1 **is** admin-settable today, by editing `sort_order`
inline in Django Admin, with `is_active` as the kill switch. So R6 delivers more of his top priority than
the plan credited — with one honest caveat: that holds while
`DYNAMIC_FREE_MODEL_CATALOG_ENABLED` is `false`, which is the default. With the flag on, model ordering
is by release date and the admin influences it only through `is_active`.

### R6 surface map, and the trap inside it

`selectedModelId` is **not** purely a picker value and must not simply be deleted:

```text
game/[id]/page.tsx:917   const preferenceModelId = selectedModelId || gameState.ai_model_id || ""
lib/ai-fallback.ts:90-96 that preference is attempt 1 of the fallback queue
settings/page.tsx:474 · play/page.tsx:123 · app/page.tsx:63
                         resolveEligibleModelId repairs a stale id and writes the repair back
play/page.tsx:188        ai_model_model_id: resolved   is SENT at game creation
draw/[id]/page.tsx:178   renders the RAW model id in a mono font — an internal id shown to a player,
                         which contradicts his "the player should only ever see the model's name"
```

So R6 is "the player stops CHOOSING", not "the value stops existing". `selectedModelId` survives as a
resolved preference derived from `preferred_ai_model_id` or catalog row 1; only the selection UI and the
player-initiated write disappear. The automatic repair write-back stays, because it keeps the stored id
consistent and is not the player choosing.

`selectedPromptId` is different: it has no fallback-queue role, so it can be removed outright, and
omitting `ai_prompt_id` at creation makes the backend use prompt row 1.

### ORCHESTRATOR SEQUENCING DECISION: S4 is R6 ONLY; the header and settings copy move to S5

`92_orchestrator-glossary-and-plan.md` and the earlier entry in this ledger folded R6 together with the
ScorePanel and settings copy, to avoid two passes over one file. That fold is now **reversed**, and the
reason is better than the original one:

```text
R6 is a BEHAVIOURAL change on the AI turn path across eight files. The copy work is ~47 strings x 4
locales. Mixing a behavioural deletion with 190 translations produces a diff nobody can review honestly
— exactly what P05 and the era-09 S7 split exist to prevent.
```

Doing R6 **first** also means the copy slice never translates a string that is about to be deleted, so
the churn the fold was meant to avoid is avoided anyway — better, because each diff has one purpose:

```text
S4  R6 only: remove the player-facing model and prompt pickers. Plus two tiny riders that live in files
    R6 already touches — the `Invalid Word(s)!` heading and the four `AI route failed` variants left over
    from S3c, and deleting the unread `message?` field on aiPassBodyKey.
S5  ScorePanel + the settings copy remainder, in four locales, over the ALREADY-SIMPLIFIED files.
```

## Slice S3c landed at `e0d3b64cbccf1a1d9983ba5c394762f55961325a` — Worker session 04, exchange 02


`feat(i18n): localize the game screen and fix the lexicon and toast defects`. 8 files, +563 −85, parent
`e421c66`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED, with two leftover string groups routed to S4.** Evidence non-independent; rendered acceptance
requested as batch `B19`.

Archived as `04_implementation_00.md` + `04_report_00.md` (the BLOCKED exchange 01) and
`04_implementation_01.md` + `04_report_01.md` (this exchange).

The three continuity strings were echoed correctly — `Není v českém lexikonu`,
`AI wymieniło płytki`, `Tvoj ťah` — so the string table survived in the session and nothing was
re-translated. It took the PRIMARY route: `ss -tlnp | grep :3000` printed nothing, the Cooperator having
stopped his dev server.

### Both defects are corrected, verified in source rather than accepted from the report

```text
uii-01-F08   lexiconRejectionKey(lexiconId) at messages.en.ts:173 — an exhaustive switch over
             collins2019 / slovak / czech / polish with `default -> game.lexicon.unknown`, which also
             absorbs null, undefined and "". No parameterized "Not in ${lexicon}" sentence, so no
             locative-case problem. The two-value ternary is gone.
uii-01-F09   `passKind?: "pass" | "exchange"` added to the existing ai_pass toast; producers set it
             explicitly at page.tsx:1047 and :1065; the consumer at :310 calls
             `t(aiPassBodyKey({ passKind: toast.passKind }))`. `aiPassBodyKey` reads ONLY passKind.
             `includes("exchanged")` returns ZERO matches in the file. Localized prose is no longer
             load-bearing anywhere in that path.
```

The Worker chose `passKind` over splitting the toast type and justified it concretely: the overlay
timeout already treats pass and exchange as one `type === "ai_pass"` at 4200 ms, so splitting types would
have widened that union. That is the smaller change and the reasoning is sound.

### Gates at `e0d3b64`, Orchestrator-measured

```text
mypy 83 files · ruff · manage.py check · pytest 381 passed, 4 skipped in 220.95s
typecheck exit 0 · vitest 374 passed | 3 skipped (28 files) · lint exit 0
build exit 0, 11 dynamic routes, ZERO `○` static
```

72 catalog lookups in `page.tsx` (65 `t`, 5 `tf`, 2 helper-selected), including the deliberate reuse of
`auth.tab.login` and `controls.play` instead of duplicate keys.

### ⛔ ORCHESTRATOR INVENTORY MISS, SECOND CONSECUTIVE SLICE — and the structural defence caught it

Report item 14 names two user-facing English string groups for which **no key was authored**. Both
confirmed by an independent Orchestrator sweep:

```text
page.tsx:222      Invalid Word{(toast.words?.length ?? 0) > 1 ? "s" : ""}!
                  the big red heading on EVERY invalid-word rejection — the most visible string in the
                  slice — and it carries the one-character English "s" pluralization
page.tsx:90,93,98,99   `AI route failed (${response.status}).` and three variants in
                  getStreamStartError, surfaced to the user through "Last error: {aiError}"
```

**Why my sweep missed line 222, diagnosed rather than hand-waved.** For S3c I deliberately ran a
blind-spot sweep first, precisely because S3b had shipped one word in English. That sweep used
`>([^<>]*?\{[^<>]*?)<`. Line 222's expression contains `>` in `(toast.words?.length ?? 0) > 1`, and the
character class `[^<>]` forbids `>`, so the pattern could not span it. Relaxing it to `[^<]` matches
immediately. **My blind-spot sweep had its own blind spot.**

The `AI route failed` group was missed for a different reason: my template-literal filter required
`[A-Z][a-z]{2,}`, a capitalized word, and "AI route failed" has none — `AI` is two capitals and the rest
is lowercase.

```text
LESSON, and it is the durable one: two structure-based regex sweeps produced two different blind spots.
Regex inventory of JSX is not reliable and a third regex would have a third blind spot. What actually
worked BOTH times is the STRUCTURAL defence — a report field obliging the Worker to enumerate every
user-facing English string it can still see. That field was added to the S3c prompt because of the S3b
miss, and it paid for itself in the very next slice. Keep it in every remaining copy slice.
```

A third, independent word-based sweep by the Orchestrator (matching common English function words in
string and text positions rather than matching structure) found exactly the same two groups and nothing
else, so the leftover set is now corroborated by two methods that fail differently.

Disposition: **both groups routed to slice S4**, which must touch `page.tsx` anyway to delete the three
R6 strings. No extra slice and no extra pass over the file. `Invalid Word(s)!` needs a one/other plural
per locale — Slovak "Neplatné slovo!" / "Neplatné slová!" — not the three-form helper, because no number
is displayed.

### Correctly disclosed non-issue: English matching that is NOT the F09 anti-pattern

`normalizeAIBlocker` at page.tsx:148-173 still matches `"authentication failed"`, `"invalid api key"`,
`"rate limit"` and `"temporarily unavailable"` in English. The Worker flagged it and drew the right
distinction: those strings arrive from **external provider APIs** and are English by nature, so matching
them is unavoidable. F09 was about matching **our own localized copy**, which is a different thing
entirely. The displayed title and body now come from the catalog. No action.

### Two small residuals for S4

```text
1  aiPassBodyKey still declares `message?: string` in its input type and never reads it — dead API
   surface kept only so a test could pass the Slovak title through. Mildly ironic given F09 existed to
   stop keying on `message`, and it invites a future reader to think the field matters. Delete the field.
2  Layout items the Worker named and did not change, all for batch B19: Polish
   "Błąd uwierzytelnienia rywala" and "Nieprawidłowe ułożenie" in toast/modal titles; Slovak/Czech
   "AI si obnovilo zásobník a spotrebovalo ťah." in the ai_pass subtitle; Czech
   "Vyber kameny na výměnu" in TurnStatusNotice; `game.ws.authExpired` and `game.ws.invalidSession` as
   long sentences in a bottom toast; and the long window.confirm give-up copy whose OK/Cancel buttons
   are browser chrome.
```

### S3c exchange 01 returned BLOCKED — the Worker was right and the prompt was the defect


Worker session 04, exchange 01, at `e421c66`. It ran the repository gate, inventoried `page.tsx`
read-only, hit the port-3000 condition at preflight, and **stopped without applying anything**, returning
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

Orchestrator-verified: `HEAD` still `e421c66`, `ls-remote` equal, porcelain **empty**, `.next` mtime
`10:37:27` which is the dev server writing rather than the Worker. Nothing was mutated.

#### The blocker is real, and it is a consequence of the Orchestrator's own acceptance batch

```text
ss -tlnp
  LISTEN  *:3000           next-server (v16.3.4)   pid 67401   child of pid 67389
                           node .../node_modules/.bin/next dev --webpack   alive 41 minutes
  LISTEN  127.0.0.1:8000   python                  pid 67368
```

Both are the **Cooperator's own** processes. He started them because the Orchestrator asked him to run
acceptance batch `B18` inside the running product — and the Orchestrator then issued an implementation
slice whose stop condition forbids exactly that state, without asking him to stop first.
**That is an Orchestrator sequencing defect: I created the blocker in the previous message.**

#### ORCHESTRATOR PROMPT DEFECT: the gate was scoped to the wrong moment

The prompt said "Check `ss -tlnp | grep :3000` first; if occupied, STOP and report." I meant *first
relative to `npm run build`*. Section 12 then listed "port 3000 is occupied" as a flat stopping
condition with no scope. The Worker's reading — stop before doing anything — follows my text exactly,
and it is the defensible reading of the two statements together.

The consequence is that **a whole exchange was consumed by a gate that only matters at the very end.**
Every one of the other seven gates is safe with a dev server live: mypy, ruff, `manage.py check`,
pytest, typecheck, vitest and lint never touch `frontend/.next`. Only `npm run build` does.

#### Correction, and why it is a current-session renewal rather than a fresh session

Reissued as Worker session 04 **exchange 02**, `current-worker-session`, prompt staged at
`/tmp/opencode/uii-s3c-worker-04-exchange02-prompt.md`, 279 lines. Current-session renewal is the
AP-preferred route here and is proportionate: the session is healthy, it mutated nothing beyond reading,
independence is not required for implementation, and it holds the read-only inventory of an 1822-line
file which it explicitly offered forward ("Inventory from inspection is held for the renewed grant").
The same pattern was used for era-11 F2a and for the era-10 planning repair.

Two changes only; everything else is reaffirmed unchanged:

```text
CHANGE 1  the port-3000 condition is SCOPED TO THE BUILD GATE and is explicitly no longer a stopping
          condition. All work and the other seven gates proceed regardless of what holds the port.
CHANGE 2  a PRE-AUTHORIZED FALLBACK: if the port is still held at the build gate, run the other seven
          gates, leave the candidate UNCOMMITTED, report PARTIAL with the exact `ss` output, and do not
          commit — because the standing rule is that all eight gates must be green before a commit.
          Killing anything remains forbidden on both routes.
```

That makes the slice converge in at most one more exchange whichever way the port goes, which is what
the finite convergence contract requires after a blocker. The Cooperator was asked in the same message to
stop his dev server, which `PROJECT_CONTEXT.md` section 3 explicitly permits.

#### A continuity check the renewal needed, because the string table lives in the session

The authored section-7 string table is ~200 values and is not re-pasted. Instead the renewal requires the
Worker to echo three exact values back before starting — `game.lexicon.czech` in Czech,
`game.toast.aiExchanged` in Polish, `game.status.yourTurn` in Slovak — and to STOP if it cannot reproduce
all three from retained context. Expected answers, held by the Orchestrator:

```text
Není v českém lexikonu  ·  AI wymieniło płytki  ·  Tvoj ťah
```

The prompt states in terms that it must not reconstruct, re-translate, or approximate a single string,
because translation is Orchestrator work by Cooperator decision and an invented Slavic string would be a
silent product defect. That is the correct shape for a compaction risk: verify, do not regenerate.

#### The Worker independently confirmed the S3b documentation claim was false

Report item 13, unprompted: `frontend/node_modules/next/dist/docs/` **is present**, 452 markdown files,
and it declined to repeat the previous session's "absent" claim. That is now confirmed by two
independent sources — this Worker and the Orchestrator's own `ls` plus the verbatim line-46 readback —
against one erroneous claim. The S3a `router.refresh()` citation stands.

## Slice S3c issued — Worker session 04, exchange 01, at `e421c66`

`feat(i18n): localize the game screen and fix the lexicon and toast defects`. Prompt staged at
`/tmp/opencode/uii-s3c-worker-04-prompt.md`, 494 lines. Archive as `04_implementation_00.md` **only after
its report exists**. Fresh Implementation Worker, E2 rather than E1 because the slice carries two
behavioural corrections rather than pure string extraction.

Scope: `game/[id]/page.tsx` — the largest single file in this whole at 1822 lines — plus the one-word
`Board.tsx` correction the previous slice left behind. Roughly 60 keys including four parameterized ones,
authored by the Orchestrator across all four locales.

### The blind-spot sweep was run BEFORE writing the prompt this time

S3b shipped `Board.tsx` with one word left in English because the prompt was written from a narrow grep
after a broad inventory had already counted more. For S3c the blind spot — JSX text mixed with
`{expressions}`, which a plain text-node regex partly misses — was swept first. It surfaced exactly two
real residuals my earlier count had missed:

```text
page.tsx:1676   "Last error: {aiError}"     a text node mixed with an expression
page.tsx:1709   `${s.username ?? "Waiting"}: ${s.score}` joined by " vs "
```

Both are now in the authorized string table. The `" vs "` separator stays English by glossary decision
and only the `"Waiting"` fallback is localized. Report item 12 additionally requires the Worker to list
ANY user-facing English string still left in the file, which is the structural fix for the S3b failure:
the check no longer depends on the Orchestrator's inventory being complete.

### Three string groups deliberately EXCLUDED because slice S4 deletes them

```text
"Choose rival"                            page.tsx:1502, :1504   model-picker fallback
"Initial"                                 page.tsx:1513          prompt-preset name fallback
"Could not switch AI prompt right now."   page.tsx:606           prompt switching
```

R6 removes the player-facing model and prompt pickers. Localizing them now would be wasted work and
would double the review surface over the same lines. Same reasoning as folding R6 into the
ScorePanel/settings slice.

### Orchestrator pre-verification of the mandated regression tests, before issuing

```text
AC-LEX-4      for all four locales: the czech / slovak / polish messages contain no "Collins" while
              the collins2019 message does                                            SATISFIABLE
AC-TOAST-DISC "AI vymenilo písmená" contains "exchanged": False — which is exactly the property that
              makes the current substring check break under translation, so the test discriminates
AC-GAME-TERM  cs "Vyber kameny na výměnu" contains "kameny" and not "písmen"; pl contains "płytki"
```

### One design decision inside the F08 fix, recorded because the obvious shape is worse

Five complete messages keyed on `lexicon_id`, not one parameterized `Not in ${lexicon}`. A single
parameterized sentence would need the lexicon name in the **locative** case in Slovak and Czech
("v slovenskom lexikón**e**", "ve slovenském lexikon**u**") and in its own oblique form in Polish
("w słowackim leksykoni**e**"), which one nominative label cannot supply. Five keys per locale is both
cheaper and grammatically safe. Recorded so nobody later "simplifies" it into the broken shape.

`game.lexicon.*` is also the first key family in this project keyed on the GAME VARIANT rather than the
interface locale. The two axes have been independent since the beginning; this is where they finally
touch, and GLOSSARY.md is required to say so.

### Cooperator acceptance batch B18 — THREE items answered, SIX not tested, 2026-09-02

His reply, verbatim: `B18-3 PASS B18-8 PASS B18-9 potvrdzujem`.

```text
B18-3  Polish "Potwierdź wymianę" in the two-column mobile confirm row      PASS
B18-8  Polish "Zoom dwoma palcami" / "Przesuń palcem" in the hint pill      PASS
B18-9  the "Reset zoom" defect                                             CONFIRMED by him
B18-1  in-game action buttons in sk / cs / pl                              NOT TESTED
B18-2  the three-form tile counter at 1 / 2 / 5                            NOT TESTED
B18-4  blank-picker heading in three locales                               NOT TESTED
B18-5  points abbreviation b. / b. / pkt on board tiles                    NOT TESTED
B18-6  rack empty state                                                    NOT TESTED
B18-7  chat panel                                                          NOT TESTED
```

⛔ **This is NOT a blanket pass and must not be recorded as one.** He answered exactly the two items the
Orchestrator flagged with ⚠ as the ones needing his eyes, plus the known defect. The other six are
`NOT TESTED`. Missing evidence never becomes PASS — AP is explicit about that, and inflating six
untested items would corrupt the closure evidence for this whole.

Both PASS answers are the valuable ones, because they resolve the only two questions that were
unmeasurable without a browser: **Polish does not overflow** either the `whitespace-nowrap` two-column
confirm row (17 characters at `1rem font-black`) or the `uppercase tracking-[0.18em] 0.72rem` board hint
pill. That materially lowers the standing "Slovak is 10-20 percent longer, Polish longer still" layout
risk for the rest of the whole: the two tightest containers already survive the longest strings authored
so far.

Disposition for the six: **carried into batch B19 rather than re-queried now.** He has explicitly asked
to be asked less, and B19 will put him back on the same game screen after slice S3c anyway, so he walks
through it once instead of twice. Last used batch prefix is now **B18**.

### uii-01-F08 — a Czech or Polish player is told their word is not in an ENGLISH dictionary

    Classification:  product-defect (factually false user-facing message), PRE-EXISTING and REACHABLE
                     NOW in the shipped product
    Severity:        medium for interview presentability, low functionally — it does not change
                     legality, only what the rejection message claims
    Confidence:      high
    Evidence class:  reproduced-dynamic — the Orchestrator loaded all four installed variants through
                     the real loader and evaluated the real `_lexicon_id` expression
    Found by:        the Orchestrator while inventorying `game/[id]/page.tsx` for slice S3c
    Location:        frontend/src/app/game/[id]/page.tsx:231-233
                       {lexiconId === "slovak"
                         ? "Not in the Slovak lexicon"
                         : "Not in Collins Scrabble Words 2019"}
                     with `lexiconId` from `gameState.lexicon_id` at :181
    Mechanism:       the ternary is a two-value test written when only English and Slovak existed.
                     `backend/game/services.py:159` `_lexicon_id` returns
                     `Path(variant.dictionary_file).stem`, so it emits FOUR distinct values. Measured
                     through the real loader:
                         english -> "collins2019"    slovak -> "slovak"
                         czech   -> "czech"          polish -> "polish"
                     Anything that is not exactly "slovak" therefore falls into the else branch.
    Impact:          a Czech player who plays an invalid Czech word is told it is
                     "Not in Collins Scrabble Words 2019", and so is a Polish player. The message is
                     not merely untranslated, it is FALSE — it names an English dictionary that has
                     nothing to do with the game being played. Era 11 slice A1 activated Czech and
                     Polish and did not touch this frontend ternary, which is how it was introduced
                     without anyone noticing; the frontend suite could not see it because no test
                     renders that toast.
    Why it surfaced now: the S3c inventory had to decide what the localized string should say, which
                     forced the question "which lexicon is this actually?" that the ternary answers
                     wrongly.
    Correction direction: four complete messages keyed by `lexicon_id` plus one generic fallback for an
                     unknown id, rather than one parameterized sentence. A parameterized
                     "Not in ${lexicon}" would need the lexicon name in the LOCATIVE case in Slovak and
                     Czech and the equivalent in Polish, which a single nominative label cannot supply.
                     Five keys per locale is the cheaper and grammatically safe shape.
    Regression test: with `lexicon_id: "czech"` the rendered message must NOT contain "Collins"; with
                     "collins2019" it must. Must fail before the fix.
    Owner:           ui-internationalization, slice S3c
    Status:          open
    Status:          **corrected at e0d3b64** (Worker session 04, exchange 02) — NOT verified-closed.
                     `lexiconRejectionKey` in messages.en.ts:173 is an exhaustive switch over the four
                     real `lexicon_id` values with `default -> game.lexicon.unknown`, which also absorbs
                     null, undefined and "". Five complete messages per locale, so no locative-case
                     problem. AC-LEX-4 pre-fix failure, quoted: `expected 'Not in Collins Scrabble
                     Words 2019' not to contain 'Collins'`. Orchestrator-verified in source; the
                     two-value ternary is gone. Not verified-closed because no independent audit has
                     run and no Cooperator rendered acceptance exists yet — batch B19 covers it.

### uii-01-F09 — localizing the AI toast will silently break its own subtitle

    Classification:  latent product-defect that TRANSLATION WOULD INTRODUCE, not a defect today
    Severity:        low today, certain to fire the moment the string is localized
    Confidence:      high
    Evidence class:  established-static — the Orchestrator read both the producer and the consumer
    Location:        producer  frontend/src/app/game/[id]/page.tsx:1033-1054
                       action "pass"     -> { type: "ai_pass", message: "AI passes" }
                       action "exchange" -> { type: "ai_pass", message: "AI exchanged tiles" }
                     consumer  frontend/src/app/game/[id]/page.tsx:305
                       {toast.message.toLowerCase().includes("exchanged")
                         ? "AI refreshed the rack and spent the turn."
                         : "Couldn't find a valid move - your turn!"}
    Mechanism:       pass and exchange share ONE toast type and are distinguished afterwards by
                     substring-matching the English word "exchanged" out of the message. Once that
                     message becomes "AI vymenilo písmená" / "AI vyměnilo kameny" / "AI wymieniło
                     płytki", the substring is gone, the check always takes the else branch, and an
                     EXCHANGE is explained to the player as "Couldn't find a valid move".
    Why it matters:  this is the `err.message.includes("401")` anti-pattern that the security era
                     deliberately removed from `api.ts` in favour of a numeric status. Re-introducing
                     it through translation would be a regression in a pattern this project has already
                     paid to eliminate.
    Correction direction: carry the discriminator in the toast DATA, not in its prose — either two
                     distinct toast types or an explicit field on the existing one — and key the
                     subtitle off that. The localized strings then have no load-bearing content.
    Regression test: an exchange toast must render the exchange subtitle in a locale whose message
                     contains no English word, e.g. Slovak. Must fail if the substring check survives.
    Owner:           ui-internationalization, slice S3c
    Status:          open
    Status:          **corrected at e0d3b64** (Worker session 04, exchange 02) — NOT verified-closed.
                     `passKind?: "pass" | "exchange"` on the existing ai_pass toast; producers set it at
                     page.tsx:1047 and :1065; the consumer at :310 calls
                     `t(aiPassBodyKey({ passKind: toast.passKind }))` and the helper reads ONLY
                     passKind. `includes("exchanged")` now returns ZERO matches in the file, verified by
                     the Orchestrator. The Worker chose passKind over splitting the toast type because
                     the overlay timeout already treats both as one `type === "ai_pass"` at 4200 ms, so
                     splitting would have widened that union — the smaller change, with sound reasoning.
                     Residual for S4: `aiPassBodyKey` still declares an unread `message?: string`.

## Slice S3b landed at `e421c6690f091203a60636b3aebaeec71e7fba69` — Worker session 03, exchange 01

`feat(i18n): localize the board, the rack, the action buttons and chat`. 11 files, +236 −24, parent
`5a96b5e`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED with one Orchestrator-caused defect to correct in the next slice.** Evidence non-independent;
rendered acceptance is Cooperator-owned and requested as batch `B18`.

Archived as `03_implementation_00.md` + `03_report_00.md`.

### The three plural functions are live and the Orchestrator read them back through the real code path

Not accepted from the Worker's test. A throwaway vitest harness was placed in the tree, run against the
**shipped** catalogs through the real `tf()`, and removed immediately (porcelain verified clean after):

```text
sk   0 Výber: 0 písmen    1 Výber: 1 písmeno    2 Výber: 2 písmená    5 Výber: 5 písmen
     22 Výber: 22 písmen                        25 Výber: 25 písmen
cs   0 Výběr: 0 kamenů    1 Výběr: 1 kámen      2 Výběr: 2 kameny     5 Výběr: 5 kamenů
     22 Výběr: 22 kamenů                        25 Výběr: 25 kamenů
pl   0 Wybrane: 0 płytek  1 Wybrane: 1 płytka   2 Wybrane: 2 płytki   5 Wybrane: 5 płytek
     22 Wybrane: 22 płytki   <- DIVERGES        25 Wybrane: 25 płytek
en   1 tile selected · 2 tiles selected · 22 tiles selected
```

All 28 renderings are byte-for-byte what the Orchestrator predicted **before** issuing the prompt. The
decisive case holds: Polish says `22 płytki` (few) where Slovak says `22 písmen` and Czech `22 kamenů`
(many). The right plural function is wired to the right catalog.

### Verified rather than accepted

```text
72 plain values (18 keys x 4 locales) checked verbatim against the authored table   0 mismatches
catalog calls per component      GameControls 11 · BlankPicker 1 · ChatPanel 6 · TileRack 1 · Board 5
                                 every count matches the report exactly
useT() present in all five components
"Enter" KeyboardEvent names preserved in ChatPanel:57 and TileRack:141 — not translated
i18n.test.ts diff  +99 −1, and the single deleted line is an import move; ZERO assertions removed
gates  mypy 83 · ruff · check · pytest 381/4 in 218.09s · typecheck 0 · vitest 369 passed | 3 skipped
       · lint 0 · build 0 with 11 dynamic routes and ZERO `○` static
```

### ⛔ ORCHESTRATOR DEFECT: `Board.tsx` now reads "Reset zoom" with an English `zoom` in every locale

`frontend/src/components/board/Board.tsx:689` is `<span className="text-white/34">zoom</span>`, the dim
second half of the reset control whose first half is now `{t("board.reset")}`. So the control renders
`Reset zoom` in Slovak, Czech and Polish — a visible half-localized string.

**The cause is mine and it is failure mode 3 in a new costume.** My own broad inventory counted **six**
JSX text nodes in `Board.tsx`. I then wrote the prompt from a narrow follow-up grep
(`grep -nE "Pinch|Drag to|Hide|Reset|PTS"`) that returned **five**, and authorized exactly those five.
I had the wider measurement in hand and acted on the narrower one — the same shape as
`grep -cE "^export const [A-Z_]+_PROVIDER"` returning 10, and as the era-11 allowlist that omitted a
test whose hazard had already been measured.

The Worker did the right thing: it named the leftover in report item 9 instead of fixing it outside its
allowlist. Disposition: **corrected in slice S3c**, which gets `Board.tsx` added to its allowlist for
exactly one new key:

```text
board.zoomNoun    en "zoom"    sk "zoomu"    cs "zoomu"    pl "zoomu"      -> renders "Reset zoomu"
```

The two-span split is preserved so the gold-shiny / dim visual design is unchanged. Severity low,
cosmetic, one word — but visible, and presentability is a first-class requirement in this project.

### A GENUINELY GOOD WORKER CATCH: my AC-TERM-4 spec was linguistically wrong

The prompt told the Worker to assert that the Polish counted-tile output "uses `płytk*`". That is wrong
for the many form, because Polish genitive plural inserts an **epenthetic e**:

```text
płytka  contains "płytk"  True
płytki  contains "płytk"  True
płytek  contains "płytk"  FALSE      płytk-a / płytk-i  ->  płyt-E-k
```

The Worker hit the false failure, diagnosed the stem change, and asserted the three actual catalog forms
`/płytka|płytki|płytek/` instead. It reported this unprompted as a near-miss. An Orchestrator contract
defect, caught and corrected by the Worker with the right reasoning — the fifth-plus time in this
project that someone other than the Orchestrator was right about a claim it stated confidently.

### ⛔ ONE FALSE CLAIM IN THE REPORT, corrected on evidence

Report item 10 states that `frontend/AGENTS.md` points at `node_modules/next/dist/docs/` and "that tree
was absent". **It is present.** Measured:

```text
frontend/node_modules/next/dist/docs                                     exists
  452 markdown files
frontend/node_modules/next/dist/docs/01-app/03-api-reference/04-functions/use-router.md
  8637 B, mtime 2026-09-01 08:42
line 46, verbatim:
  "- `router.refresh()`: Refresh the current route. Making a new request to the server, re-fetching
   data requests, and re-rendering Server Components. ..."
```

Two consequences, and the second one matters more than the first:

1. The claim is a **Worker observation error**, not a repository fact. It is harmless for S3b, which was
   pure client-side string extraction and needed no version-specific documentation. But recorded
   loudly, because "the installed docs are absent" would licence a future session to skip mandatory
   reading that `frontend/AGENTS.md` requires. There is no root-level `node_modules`, so the most likely
   cause is a wrong-path lookup rather than a missing dependency tree.
2. **It independently confirms the S3a citation.** The S3a Worker quoted `use-router.md:46` for its
   `router.refresh()` authorization and the Orchestrator had verified only that the commit message
   carried the citation. The sentence is now verified verbatim at that exact line. S3a's acceptance is
   therefore stronger than when it was granted, not weaker.

### Layout observations the Worker named and did not change — exactly what was asked for

```text
pl "Potwierdź wymianę"      17 chars, whitespace-nowrap, two-column mobile confirm row, 1rem font-black
cs "Vzdát tah" / sk "Vynechať"   in the same nowrap three-column mobile grid as English "Pass" (4)
pl "Zoom dwoma palcami" / "Przesuń palcem"   in an uppercase tracking-[0.18em] 0.72rem hint pill
pl "Wybrane: 22 płytki"     the longest of the four for controls.tilesSelected, uppercase tracking
```

None is measurable without a browser, which the Worker correctly did not have. All four go into batch
`B18` as named things for the Cooperator to look at. This is the "Slovak text is 10-20 percent longer"
trap arriving in Polish, which is longer still.

## Slice S3b issued — Worker session 03, exchange 01, at `5a96b5e`

`feat(i18n): localize the board, the rack, the action buttons and chat`. Prompt staged at
`/tmp/opencode/uii-s3b-worker-03-prompt.md`, 429 lines. Archive as `03_implementation_00.md` **only
after its report exists**. Fresh Implementation Worker, E1, independent acceptance not required.

### Measured inventory that drove the slice split

The remaining game surface was re-measured with a script that counts quoted capitalized literals AND
multi-line JSX text nodes, which the handout's grep could not see:

```text
app/game/[id]/page.tsx        66     components/game/GameHistoryPanel  33
components/game/ProfileModal  28     app/play/page.tsx                 24
components/game/ScorePanel    16     components/game/PromptCatalogModal 13
app/waiting/[id]/page.tsx      9     components/game/ChatPanel          7
components/board/Board         6     components/game/AIThinkingOverlay  6
components/game/GameControls    5    components/game/PromptPreviewModal 4
components/game/GameHistoryModal 3   components/tiles/TileRack          3
components/game/BlankPicker      1   components/game/TurnStatusNotice   0
lib/types.ts                     2
----------------------------------------------------------------
GAME SURFACE TOTAL           226   (per-file dedup; NOT globally deduped)
```

226 strings x 4 locales is roughly 900 translations. That is not one slice, so the plan's single S3b is
split. **S3b is the five surfaces a player touches on every turn** — 18 plain keys plus one
parameterized key, ~19 keys x 4 locales — chosen because it is the highest-value visible surface and a
coherent unit: everything the player directly manipulates during a turn.

### The revised remaining sequence, and one sequencing insight worth keeping

```text
S3b  GameControls, BlankPicker, ChatPanel, TileRack, Board          <- ISSUED
S3c  app/game/[id]/page.tsx alone, ~66 literals in 1822 lines       one file, its own slice
S4   R6 (remove the player's model + prompt pickers) TOGETHER WITH ScorePanel and the
     settings/page.tsx copy remainder
S3d  GameHistoryPanel + GameHistoryModal + ProfileModal + uii-01-F03 dates
S3e  app/play + app/waiting
S3f  uii-01-F02 accessible names, authored straight into the catalog
then R7/R8 Django i18n + Retry-After · R10 nonce CSP · R11 catalog proxies · acceptance batch
```

⚠ **S4 folds R6 into the ScorePanel/settings copy slice deliberately.** `ScorePanel.tsx:425` carries
`"Prompt presets"` and `settings/page.tsx` carries the model picker — both are exactly what R6 deletes.
Localizing them first and deleting them second would mean two passes over the same diff surface, which
is the avoidable churn `91_orchestrator-decisions.md` already flagged when the Cooperator asked about
folding `10/01` in. One pass, one review.

### AI telemetry localization is DEFERRED, with the reason recorded

The six human-readable AI telemetry states are generated inside
`frontend/src/app/api/ai/move/route.ts` — a **locked** file (locked fork 2) — and re-derived by
`describeAiTurnTelemetry` in `frontend/src/lib/types.ts`, which currently compares against the English
prose (`types.ts:293-307`). Localizing the overlay line therefore needs one of:

```text
(a) touch the locked move route                                  FORBIDDEN
(b) match the received English prose against catalog keys        the err.message.includes("401")
                                                                 anti-pattern the security era removed
(c) key the overlay off `terminal_cause` / `completion_source`, which ARE stable enumerated values
    (locked fork 10 pins the six completion_source values), and have types.ts return a key
```

(c) is right and is genuinely better architecture, but it is an enum-mapping redesign in a file adjacent
to the AI boundary, not string extraction. Folding it into a copy slice would turn a copy slice into an
architecture slice. Deferred to its own bounded slice; `AIThinkingOverlay.tsx` and `types.ts` are on
S3b's forbidden list so nobody starts it accidentally.

### The interesting content decision: a colon-label instead of a sentence

`GameControls.tsx:79` currently renders `{n} tile{n !== 1 ? "s" : ""} selected`. A direct Slavic
translation needs the participle to agree with the noun in number AND case, and those change between
the one / few / many forms — "Vybrané 1 písmeno" is wrong while "Vybrané 2 písmená" is right, and no
single participle covers both. A colon-label is grammatically inert at every count:

```text
sk   Výber: 1 písmeno     Výber: 2 písmená     Výber: 5 písmen      Výber: 22 písmen
cs   Výběr: 1 kámen       Výběr: 2 kameny      Výběr: 5 kamenů      Výběr: 22 kamenů
pl   Wybrane: 1 płytka    Wybrane: 2 płytki    Wybrane: 5 płytek    Wybrane: 22 płytki
                                                                    ^^^ Polish diverges
```

This is the first live use of all three plural functions, and the mandated test `AC-TILES-PL22` is the
executable proof that the right function is wired to the right catalog — the single most likely mistake
in the slice. Orchestrator pre-verified before issuing: `pluralPl` gives `Wybrane: 22 płytki` while
`pluralSk` would give `Wybrane: 22 płytek`, so the assertion is both satisfiable and discriminating.

`blank.chooseLetter` is the sentence the terminology work existed for, and it reads correctly in all
four locales for **three different grammatical reasons** — Slovak because `písmeno` (tile) and `žolík`
are distinct words, Czech for the opposite reason because `písmeno` means the letter there, Polish
because `litera` and `blank` are unambiguous. The prompt spells that out and mandates `AC-TERM-4`,
because "correcting" the Czech string to `kámen` is the most tempting wrong edit available.

## Cooperator acceptance batch B17 — blanket PASS, 2026-09-02

Cooperator-executed acceptance of slice S3a in his own browser. His reply was a single **`PASS`** for
the whole batch. Recorded honestly as a **blanket pass rather than eight itemized results**, so a future
reader knows the granularity of the evidence.

```text
B17-1  Interface-language panel shows FOUR buttons in a 2x2 grid, endonyms         PASS (blanket)
B17-2  Čeština switches the UI and the browser tab title immediately               PASS (blanket)
B17-3  Polski does the same                                                        PASS (blanket)
B17-4  Slovenčina survives Ctrl+Shift+R and the console stays clean                PASS (blanket)
B17-5  Logged-out landing/auth page renders in the active locale, cs and pl        PASS (blanket)
B17-6  Game-variant panel still shows translated exonyms, unlike the locale list   PASS (blanket)
B17-7  Diacritics ě ř ů and ł ą ę ś ż render in the gold gradient                  PASS (blanket)
B17-8  Four language buttons survive a ~400 px viewport                            PASS (blanket)
```

This is the first Cooperator-verified rendered evidence that the interface genuinely ships in four
locales, and it closes the acceptance loop on S3a. It is Cooperator-observed evidence, not independent
audit evidence. B17-4 also re-confirms in the four-locale product the property he first measured at
`a5aff12`: no hydration error — which the S3a design now guarantees by construction rather than by
rehydration timing.

A single-word reply on a multi-item batch is his established style (`A`, `ano`, `hotovo`, `PASS`,
`obetovatelne`). It was not re-queried for itemization because he has explicitly asked to be asked less,
and a blanket `PASS` has one plain reading. If any of those eight items later turns out to have been
untested, the evidence class above is what tells a reader why. Last used batch prefix is now **B17**.

## Slice S3a landed at `5a96b5ed79c10b60a720ab89ae11d6979b98ec0a` — Worker session 02, exchange 01

`fix(i18n): make the server locale authoritative and ship four locales`. 15 files, +595 −123, parent
`61c9f09`, one non-force push, public readback equal. Orchestrator verdict: **implementation-PASS,
ACCEPTED.** Evidence is **non-independent** by design; rendered acceptance is Cooperator-owned and is
requested as batch `B17`.

Archived as `10/00-ui-internationalization/02_implementation_00.md` + `02_report_00.md`.

**`uii-01-F04` IS CORRECTED, and the Orchestrator measured it independently rather than accepting the
Worker's table.** Reproduced on port 3413 while the Worker had used 3412 — the same
cross-verification shape era 09 used for the CSP headers:

```text
case  cookie / header                       lang  "Sign In"  "Prihlásiť sa"  "Přihlásit se"  "Zaloguj się"
A     none, Accept-Language: sk-SK          en        1            0               0              0
B     libretiles_locale=sk                  sk        0            1               0              0   <- WAS 1 / 0
C     libretiles_locale=cs                  cs        0            0               1              0
D     libretiles_locale=pl                  pl        0            0               0              1
E     libretiles_locale=fr                  en        1            0               0              0
```

Case B is the defect: at the baseline the same request returned `lang="sk"` with `"Sign In"` x1 and
`"Prihlásiť sa"` x0. Server HTML, `<html lang>`, `<title>` and the body now agree in all four locales.

### Four probe cases the prompt did NOT ask for, run by the Orchestrator

```text
libretiles_locale=cz   -> lang=en, English body      `cz` is not a language subtag; Czech is `cs`
libretiles_locale=hu   -> lang=en, English body      Hungarian interface is deliberately not shipped
libretiles_locale=SK   -> lang=en, English body      isLocale is case-sensitive by design
libretiles_locale=     -> lang=en, English body      empty cookie falls back cleanly
```

### A deeper body probe, because one auth-tab string is thin evidence

Seven strings per locale, all rendered exactly once in the server HTML, plus the thousands separator
read as raw bytes:

```text
sk  Prihlásiť sa · Používateľské meno · ľudia aj AI. · Uložené partie · Živý front · Účet · platných slov
cs  Přihlásit se · Uživatelské jméno · lidé i AI. · Uložené partie · Živá fronta · Účet · platných slov
pl  Zaloguj się · Nazwa użytkownika · ludzie i AI. · Zapisane partie · Kolejka na żywo · Konto · poprawnych słów
en  Sign In · Username · human and AI. · Saved boards · Live queue · Account · valid words

thousands separator, hexdump of the rendered bytes:
  sk / cs / pl   32 37 39 c2 a0 34 39 36     "279" + U+00A0 + "496"      <- non-breaking space
  en             32 37 39 2c 34 39 36        "279,496"                    <- comma
```

The U+00A0 survives the whole pipeline — source escape, build, SSR — in all three Slavic locales. That
had never been verified end to end before.

### Gates at `5a96b5e`, Orchestrator-measured

```text
mypy               Success: no issues found in 83 source files
ruff               All checks passed!
manage.py check    System check identified no issues (0 silenced).
pytest             381 passed, 4 skipped in 217.33s      (unchanged — no backend file touched)
npm run typecheck  exit 0                                 <- the code type-checks
npx vitest run     362 passed | 3 skipped  (28 files)     <- 352 + 10, every addition accounted for
npm run lint       exit 0
npm run build      exit 0, EVERY route still ƒ, zero `○`  <- the build passed
```

Zero static routes is the required outcome, not a coincidence: if any route became `○` the locale
cookie would no longer be read and that would be the regression.

### Content verified against what the Orchestrator authored, not accepted from the report

80 authored strings checked for verbatim presence in the shipped tree: **zero drift**. Key-set parity
computed independently across all four catalogs: 57 text + 2 fn each, zero missing, zero extra in every
direction. Type annotations present and load-bearing in both new catalogs
(`Record<TextKey, string>` and `{ [K in FnKey]: (typeof enFn)[K] }`). Each catalog imports exactly its
own plural helper — sk `pluralSk`, cs `pluralCs`, pl `pluralPl`. Endonyms byte-identical in all four,
`settings.uiLanguage.en` is now `"English"` in the Slovak catalog while
`settings.gameVariant.english` correctly stays `"Angličtina"`.

### ORCHESTRATOR PROBE DEFECT, recorded because the method failed and the product did not

The first content-verification probe reported **38 mismatches**. Every one was
`shipped: None` — the probe's own regex failed to capture those keys, and a stray
`.encode().decode("unicode_escape")` mangled every non-ASCII value. Classified per AP's
Evidence-Probe Failure Contract:

```text
Intended system fact: does the shipped cs/pl content match the authored strings verbatim
Probe construction: defective        Command execution: executed
Returned system evidence: none about the intended fact
Failure classification: diagnostic-method-failure        Fact status at that point: unknown
Fresh probe necessary: yes
```

Re-run with literal substring presence instead of parsing: 80/80 present, zero drift. Recorded rather
than discarded, because a 38-mismatch line in a log would otherwise read as a product defect to the
next person who finds it.

### The one existing test the Worker MODIFIED — judged an expansion, not a weakening

`AC-DETECT` asserted `detectBrowserLocale(["cs-CZ"]) === "en"`. That was factually correct under two
locales and factually **wrong** under four. The Worker renamed it `AC-DETECT4` and replaced that single
assertion with `["cz-CZ"] -> "en"`, preserving the unknown-subtag fallback property while adding the
negative case. Verified line by line:

```text
preserved verbatim   ["sk"] ["sk-SK"] ["SK"] ["sk-SK","en"] -> sk ; ["en-US"] ["sks"] [] -> en
added                ["cs"] ["cs-CZ"] ["CS"] -> cs ; ["pl"] ["pl-PL"] -> pl ; ["hu"] -> en
replaced             ["cs-CZ"] -> en          BECAME    ["cz-CZ"] -> en
net                  8 assertions -> 14, strictly stronger
```

Accepted. It disclosed the change prominently with its reasoning instead of quietly deleting an
assertion, which is the behaviour this project wants. **No test was weakened, skipped, xfailed, or
deleted** — the streak holds.

### AC-SYNC-3 is a better termination proof than the prompt asked for

The prompt asked for one idempotence case. The Worker wrote a double loop over **all twelve ordered
pairs of distinct locales**, asserting `{cookie: resolved, refresh: true}` then
`{cookie: null, refresh: false}` when the written cookie is fed back. The loop-termination argument is
therefore executable for every reachable transition, not one example.

### AC-SEC-1 is also stronger than specified, and the security properties hold

The prompt asked for string equality per locale. The implementation sends **two different Django 401
bodies** — `{"detail": "No active account found."}` and `{"detail": "Invalid password."}` — and asserts
both produce the IDENTICAL message, which is the actual non-enumeration property rather than a proxy for
it. Then it checks all ten enumeration fragments. AC-SEC-2 asserts the session-expired wording is
distinct from the invalid-credentials wording in each of the four locales.

`frontend/src/lib/api.ts` is **byte-identical** at `5a96b5e`, which is what structurally preserves both
properties: `humanMessageForStatus` remains a `switch (status)` whose 401 branch keys only on
`requestCarriedToken`.

### One Worker deviation, disclosed and CORRECT

The `LocaleProvider` effect waits for Zustand persist hydration before calling
`adoptBrowserLocaleIfUnset`. The prompt did not specify that. It is **required**, not optional:
`adoptBrowserLocaleIfUnset` reads `useGameStore.getState().uiLocale`, which is `null` before hydration,
so without the wait first-visit detection would overwrite an explicit stored choice on every load — a
direct violation of Cooperator decision D4/D7, the VPN case he reasoned about himself. The Worker
reproduced the pattern the old `useLocale()` effect used and said why. Accepted; the Orchestrator's
contract was incomplete here and the Worker filled the gap correctly rather than compliantly.

Note the effect's dependency array is `[value, router]`, which gives a second, independent guarantee
against the refresh loop: even if a cookie write were somehow ineffective, `value` would not change and
the effect would not re-run.

### `uii-01-N01` CLOSED

`layout.tsx` no longer duplicates `t()`'s catalog ternary. The React-free
`frontend/src/lib/i18n/translate.ts` holds the four-catalog `Record<Locale, ...>` tables, `layout.tsx`
imports `t` from it, and the local `textFor()` is gone. The Server Component no longer risks pulling
React hooks or the Zustand store into the server bundle. The one deliberate internal cast in `tf` and
its explanatory comment were moved verbatim.

⚠ Small precision residual: that comment still says "between the two catalogs" while there are now
four. The reasoning is unchanged and correct; only the count in the prose is stale. Not worth a slice
of its own — fold it into the next slice that touches the file.

### Boundary discipline, verified path by path

15 changed files, all inside the section-8 allowlist. `useGameStore.test.ts` was on the allowlist for
typecheck coverage and was correctly **not** mutated; AC-ONCE still passes unchanged. Verified
untouched: `provider-registry.ts`, `openai-compatible.ts`, `ibm-watsonx.ts`, `ai-runtimes.ts`,
`prompts.ts`, `api/ai/move/route.ts`, `move_search.py`, `selection.py`, `README.md`, `AGENTS.md`,
`proxy.ts`, `security-headers.ts`, `constants.ts`, `api.ts`, and all of `frontend/public/`. Locks A–D
intact. Persist `version: 4` unchanged with all four migrate branches intact, so no collision with
`11/01`'s persist versioning. `suppressHydrationWarning` appears nowhere in `frontend/src`.

### The disclosed near-miss, independently checked

The Worker reported that an early write targeted `index.ts` with Polish catalog contents and was
overwritten in the same pass before any gate or commit. Verified: `index.ts` at `5a96b5e` contains zero
Polish strings and zero references to `plText`; `messages.pl.ts` is complete with both type
annotations; and `git rev-list --count 61c9f09..5a96b5e` is **1**, so no broken intermediate was ever
published. Residual risk in the published tree: none. Reporting it unprompted is the behaviour that
makes the rest of the report trustworthy.

## Slice S3a issued — Worker session 02, exchange 01, at `61c9f09`

`fix(i18n): make the server locale authoritative and ship four locales`. Prompt staged at
`/tmp/opencode/uii-s3a-worker-02-prompt.md`, 809 lines. To be archived as
`10/00-ui-internationalization/02_implementation_00.md` **only after its report exists**, per the Meta
contract. Fresh Implementation Worker, `fresh-worker-session`, E2, independent acceptance not required,
evidence explicitly non-independent.

### ORCHESTRATOR SCOPE DEVIATION from the accepted slice plan, recorded not absorbed

`92_orchestrator-glossary-and-plan.md` section 4 defines S3a as "play, queue, draw, waiting +
LocaleProvider". **Split:** S3a is now the LocaleProvider plus the four-locale catalog and adds **no new
page copy**; the play/queue/waiting copy moves to S3b. Two reasons, both about reviewability
(`PROMPT_ENGINEERING_PATTERNS` P05):

```text
1  the union expansion and the provider touch exactly the same five i18n files, and the SSR
   regression test that uii-01-F04 needs should be written ONCE against four locales rather than
   written for two and rewritten for four
2  folding ~50 new page strings into the same diff as a root-layout architecture change produces a
   diff nobody can review honestly — the exact shape era 09 split S7 to avoid
```

### The design decision that matters: the COOKIE becomes the rendering source of truth

`uii-01-F04`'s root cause was the Orchestrator's own session-01 contract, which made the client store
the rendering source and called the cookie "a routing hint only". The correction inverts that:

```text
server        layout.tsx reads libretiles_locale -> one Locale
client tree   that value goes into a client LocaleProvider and is what useLocale() returns
store         keeps PERSISTENCE, first-visit detection, and the api.ts Accept-Language feed
agreement     SSR and the hydration render read the SAME value, so they CANNOT disagree
```

This removes hydration mismatch **by construction** instead of by timing luck. The previous design
avoided a console error only because zustand rehydration happens to land after the hydration render —
Cooperator-measured, recorded, and not a property worth depending on.

### ⚠ The non-obvious hazard the prompt makes the Worker prove: an infinite refresh loop

`router.refresh()` re-runs the server layout, which re-reads the cookie, which re-renders the provider,
whose effect can call `router.refresh()` again. The design terminates because the cookie is the server's
only input for that value and the effect writes the cookie to `resolved` **before** refreshing, so the
next server render necessarily yields `serverLocale === resolved` and the decision becomes
`{ cookie: null, refresh: false }`.

To make that argument testable under the existing `environment: "node"` vitest setup rather than
requiring a React renderer, the decision is extracted into a pure function:

```ts
localeSyncDecision(serverLocale: Locale, resolvedLocale: Locale): { cookie: Locale | null; refresh: boolean }
```

`AC-SYNC-3` feeds the decision's own cookie value back as the next server locale and asserts no second
refresh. That test **is** the executable form of the termination proof, and the prompt names it as the
single most important new test in the slice. The Worker must also state the argument in prose and is
told to STOP rather than ship a plausible-looking loop it cannot justify.

### Orchestrator pre-verification of its own contract, before issuing

Three load-bearing assertions were computed rather than asserted, because a prompt whose mandatory tests
are unsatisfiable is an Orchestrator defect that costs a Worker session:

```text
AC-SEC-1/2 satisfiability   all four tokenless-401 strings checked against nine enumeration fragments
                            ("neexistuje", "nenalezen", "nie istnieje", "nie znaleziono",
                            "nesprávne heslo", "nesprávné heslo", "błędne hasło", "wrong password",
                            "unknown user") -> zero hits; all four session-expired strings distinct
                            from their invalid-credentials counterpart; all four mutually unique.
                            SATISFIABLE.
pluralPl divergence set     computed as exactly {22, 23, 24, 122, 123, 124} against pluralSk, which is
                            precisely the set the prompt asserts. MATCH.
rendered plural strings     cs 1/2/4/5/55 -> minutu, minuty, minuty, minut, minut
                            pl 1/2/4/5/22/55 -> minutę, minuty, minuty, minut, MINUTY, minut
                            both match the prompt's expected values exactly.
```

`frontend/src/lib/api.ts` is deliberately **excluded** from the allowlist, which is what preserves
AC-SEC-1 and AC-SEC-2 structurally: `humanMessageForStatus` stays a `switch (status)` whose 401 branch
keys only on `requestCarriedToken` and never on the response body.

### Other decisions written into the prompt

```text
persist version STAYS 4      no stored value can be invalid-under-v4-but-valid-now, because "cs" and
                             "pl" were never writable; and 11/01 shares this store's persist
                             versioning, so an unnecessary bump risks a cross-whole collision
uii-01-N01 CLOSED here       a React-free frontend/src/lib/i18n/translate.ts holds the four-catalog
                             tables so layout.tsx (a Server Component) stops duplicating t()'s
                             ternary and stops needing React hooks in the server bundle
Record<Locale, ...> is       adding a fifth locale to LOCALES without its catalog must be a tsc error.
load-bearing                 No Partial, no index signature, no switch with a default.
isLocale must be DERIVED     it is currently `value === "en" || value === "sk"`, which silently rots
from LOCALES                 when the union grows. Same for detectBrowserLocale.
`cz` is NOT a locale         Czech is `cs`; browsers send `cs-CZ`. A `cz` subtag must fall through to
                             "en" and no alias is added. AC-DETECT4 and AC-ISLOCALE pin it.
endonyms, four constants     settings.uiLanguage.* is byte-identical in all four catalogs
no suppressHydrationWarning  wanting one is a named STOPPING CONDITION, because it would paper over
                             exactly the defect being fixed
constants.ts is FORBIDDEN    its 61 TW/DW/TL/DL literals are the board, not copy
hu.png stays untouched       committed, deliberately unreferenced, not a defect
```

## Cooperator decision 8 and the terminology correction — 2026-09-02

**Decision 8, verbatim `1. B`: the interface ships in `en + sk + cs + pl`.** Put to him once with three
options and recommendation B. The `Locale` union grows from `["en","sk"]` to `["en","sk","cs","pl"]`.
Hungarian interface is not shipped; `frontend/public/hu.png` stays committed and deliberately
unreferenced until `11/02` and must not be "fixed". Full record in
`10/00-ui-internationalization/95_orchestrator-terminology.md`.

### ⛔ His Czech assumption was wrong, and the correction is evidenced

He said Czech `písmeno` is "clearly right just as in Slovak". The Česká asociace Scrabble rules
(`https://scrabble.hrejsi.cz/pravidla`, retrieved 2026-09-02) use **`kámen`** for the physical tile and
reserve **`písmeno`** for the letter on it, in the same sentences:

```text
"Každý hráč si vytáhne ze sáčku jeden KÁMEN. Hráč s PÍSMENEM nejblíže k začátku abecedy začíná."
"Poté si každý hráč vylosuje sedm KAMENŮ a uloží do svého ZÁSOBNÍKU ..."
"PRÁZDNÝ KÁMEN (ŽOLÍK) lze použít místo kteréhokoli PÍSMENE ..."
"Za každé PÍSMENO ... obdrží hráč počet bodů, který je na něm uveden."
```

Czech therefore ships `kámen`. Decided by the Orchestrator rather than asked, per his standing
instruction to be asked less; one word from him overrides it.

Retrieval note for the next reader: those rule sub-pages are Turbo-rendered and return **HTTP 404 to a
plain HTTP client**. `curl` on `/pravidla`, `/pravidla/soutezni-rad`, `/pravidla/pripustnost-slov` all
return 404 while the pages exist. Do not conclude the source is gone. CLI routes were exhausted first
(curl 404s, a DuckDuckGo bot challenge, an empty MediaWiki API result) before one page was read through a
browser engine; locked fork 7 forbids browser-driven *product diagnosis*, which this was not.

### His Slovak decision is now PROVEN right, not merely accepted

```text
sk.wikipedia "Scrabble", full text:   písmen* 29 occurrences    kameň / kamen  ZERO occurrences
                                      zásobník 9   žolík 2   vrecko present
```

He overruled the Orchestrator's `kameň` and `dlaždica` and picked `písmeno`, which is the actual Slovak
convention while both Orchestrator suggestions were outside it. **Fourth time his answer beat the
Orchestrator's recommendation, and the first time the Orchestrator could prove why from a primary
source.** Slovak and Czech genuinely diverge here; "obviously the same in Czech" was the
reasonable-sounding inference that turned out false — the same failure shape as a negative grep.

### Polish: all three handout candidates confirmed, and one near-miss caught

Polska Federacja Scrabble regulations (`https://pfs.org.pl/regulaminy.php`, retrieved 2026-09-02):
`płytka` 62, `stojak` 28, `blank` 24, `woreczek` 26, `plansza` 49. The rules name the blank explicitly:
*"dwie płytki puste, które będziemy nazywać BLANKAMI."* `blank` is a normal masculine noun and declines
(`blanka`, `blankiem`, `blanków`), so parameterized strings must decline it rather than concatenate.

⚠ **`pass` in Polish is `Pauza`; `Pas` would have been wrong.** `pas` appears **zero** times in those
regulations. `pauza` has its own section 3.4, and 3.4.2 states the player says „pauza". The
Orchestrator's instinct was `Pas` by analogy with the Slovak reasoning that rejected `pas` as a card
term. One grep prevented shipping the wrong verb on a primary game button. The Czech mirror image is
recorded as a curiosity that must NOT reach the UI: the Czech rules have the player announce a pass with
the English word *"pass"*; a spoken table call is not a button label, so the Czech button is `Vzdát tah`.

### The four-locale terminology contract

```text
              tile      letter    rack        blank    bag        board          pass        points
en            tile      letter    rack        blank    bag        board          Pass        pts
sk  DECIDED   písmeno   písmeno   zásobník    žolík    vrecko     hracia plocha  Vynechať    b.
cs  EVIDENCED kámen     písmeno   zásobník    žolík    sáček      hrací deska    Vzdát tah   b.
pl  EVIDENCED płytka    litera    stojak      blank    woreczek   plansza        Pauza       pkt
```

The `BlankPicker` heading works in all four locales for **three different grammatical reasons**: Slovak
"Vyber písmeno pre žolíka" reads correctly because `písmeno` (tile) and `žolík` are distinct words; Czech
"Vyber písmeno pro žolíka" reads correctly for the opposite reason, because `písmeno` means the letter
there and a letter is literally what is chosen; Polish "Wybierz literę dla blanka" is unambiguous.

### ⚠ Polish needs a THIRD plural function — the main new mechanical trap

`pluralSk(n, one, few, many)` implements `1 / 2..4 / otherwise`. Correct for Slovak **and Czech**
(`22 minút`, `22 minut`). **Wrong for Polish**, which keys on the last digit with a 12–14 exception:

```text
n            sk        cs        pl
1            minútu    minutu    minutę
2, 3, 4      minúty    minuty    minuty
5 .. 21      minút     minut     minut
22, 23, 24   minút     minut     MINUTY     <- pluralSk would emit "minut" here
122 .. 124   minút     minut     MINUTY
```

A separate `pluralPl` is required (`n===1` → one; `n%10 in 2..4 && !(n%100 in 12..14)` → few; else many).
`pluralSk` is reused verbatim for Czech behind an exported `pluralCs` alias, with a comment recording
that the shared implementation is deliberate. The `uii-01-N02` residual is unchanged and still correct
for integer counts, which is every count in this product.

Points abbreviate per locale — `pts` / `b.` / `b.` / `pkt` — so Polish is one character wider than
Slovak and Czech in the score panel, the tightest container in the product. That is an R1/R3 layout
acceptance item, not a translation question.

### One Orchestrator-owned wording change, disclosed rather than slipped in

The interface-language list switches from translated exonyms (`Angličtina`) to **endonyms** — `English`,
`Slovenčina`, `Čeština`, `Polski` — identical in all four catalogs. Reasons: four locales would otherwise
need a 4x4 matrix of sixteen language names; a user who has accidentally selected an unreadable interface
language cannot find their own language in a translated list; and it makes the R1 dropdown's
diacritic-insensitive autocomplete meaningful, since "cestina" matching "Čeština" is exactly the example
the Cooperator gave. The **game-variant** list is a different control and keeps translated exonyms
through `VARIANT_NAME_KEYS` in `GameLanguagePanel.tsx:13-18` with its `display_name` fallback; it is not
changed.

Hungarian terminology was deliberately **not** researched, because decision B excludes it. The handout's
candidates (`betű?` `tartó?` `joker?`) remain UNVERIFIED and must not be used.

## Era 10 continuation — Stage-1 restoration at `61c9f09`, 2026-09-02

Read-only. Nothing issued, nothing committed, nothing pushed. Full evidence in
`10/00-ui-internationalization/94_orchestrator-restoration.md`. Repository at `61c9f09` with **empty
porcelain**.

### The baseline moved, and the Cooperator moved it

`93_orchestrator-handout.md` expects `2917251` plus ten untracked `frontend/public` files. Measured:
`main = 61c9f09377011525105d747b88d603bff5d832e6`, porcelain **empty**, public readback equal, `.ap`
gitlink unchanged at `9c5cc44`.

```text
61c9f09  feat(images): add new language icons for Czech, English, Hungarian, Polish, and Slovak
         author Michal Cisárik <michal@cisarik.info>, 2026-09-02 08:08:53 +0200, parent 2917251
         5 files:  cs.png 924  en.png 2572  hu.png 242  pl.png 166  sk.png 1326   total 5230 B
```

Every byte size is identical to the Orchestrator-normalized assets recorded above under "Flag assets
normalized by the Orchestrator, 2026-09-01", and all five are 48x32 (IHDR read directly). So he
committed the **normalized** PNGs, not the raw JPEGs, and the deliberate `cz.jpeg -> cs.png`
language-code rename survived. The five source JPEGs **never entered Git history** —
`git log --all -- frontend/public/<f>.jpeg` returns zero commits for each — and are gone from the
working tree. Nothing orphaned, no `.gitattributes`, no LFS.

RF-12 classification performed before any mutation: primary **`unrelated-owner-work`** (the author is
the Cooperator, not any Orchestrator or Worker), secondary **`accepted-continuation`** (the commit
delivers exactly what handout section 1 assigns to `10/00` R1). `stale-clone`, `unpublished-candidate`,
and `unexplained-divergence` are each not-applicable with a stated reason; no unclassified remainder.
Immediate action: preserve the owner's work and adopt `61c9f09` as this whole's baseline. **R1's asset
obligation is discharged** — the flag dropdowns can reference `/en.png`, `/sk.png`, `/cs.png`,
`/hu.png`, `/pl.png` today.

### Gates re-measured at `61c9f09`, and one carried-forward unknown is now closed

All eight green, independently measured rather than accepted: mypy `83 source files`, ruff clean,
`manage.py check` clean, pytest `381 passed, 4 skipped in 215.97s`, typecheck exit 0, vitest
`352 passed | 3 skipped`, lint exit 0, build exit 0 with every route `ƒ` and no deprecation warning.
`ss -tlnp` confirmed ports 3000/8000 free before the build; no process was killed and no broad-pattern
kill was used.

**`mypy --no-incremental` was run as a ninth check and returns the identical `83 source files` clean
result.** `PROJECT_CONTEXT.md` section 4 had carried an open caution asking whether mypy's cache shares
the `orch-04-F22` weakness that let `npm run build` report success over a stale typecheck cache. It does
not, at this commit. That unknown is closed with evidence instead of being handed to another session.

### Handout reconciliation — every material claim confirmed except the baseline

R2 done (`variants/` route, `VariantSummary`, `getVariants`, `GameLanguagePanel` + its own test); four
variants installed with Hungarian absent; `SelectedVariantSlug = string` at `useGameStore.ts:26` with
persist `version: 4` at `:278`; every route already `ƒ` so the nonce CSP costs zero additional static
prerendering; `settings/page.tsx` 813 lines and `game/[id]/page.tsx` 1822 lines exactly; locks A–D
intact; `_legacy_wire_board_and_blanks` still at `services.py:327` so `11/01` is open but **idle**.

`R5` / `uii-01-F04` confirmed still open with a **widened** pattern rather than one narrow grep:
`LocaleProvider` 0 matches, `createContext` 0, `useContext` 0 — there is no React context of any kind in
`frontend/src`. `R8`, `R9`, `R10`, `R11`, and both halves of `R12` each re-verified open at exact
locations.

### Four precision corrections, recorded rather than smoothed over

```text
1  "55 keys across six areas" conflates two real numbers. enText has exactly 55 keys and enFn exactly 2,
   so 57 are localized, and the handout's own histogram (13+11+11+10+10+2) sums to 57. A key-set diff of
   the two catalogs returns zero missing and zero extra, so the type contract is holding.
2  The pinned MOVE CORE SHA-256 lives in frontend/src/lib/prompts.test.ts:23, NOT in prompts.ts. Lock B's
   hash is enforced by a test, like lock C since era 11. Anyone verifying it must look in the test.
3  `grep -cE "^export const [A-Z_]+_PROVIDER"` returns 10, not 9, because it also matches
   EXACT_PROVIDER_METADATA at line 51. Enumerating by name returns exactly nine. A third instance of
   "a count is not a conclusion", this time found by the Orchestrator against itself.
4  uii-01-F02's a11y inventory is understated. Re-measured over all of frontend/src:
       aria-hidden 5  aria-disabled 5  aria-pressed 4  aria-live 2  aria-current 1  = 17
       title= 10  placeholder= 6  onKeyDown 5
       ZERO: aria-label, aria-labelledby, aria-describedby, role=, alt=, tabIndex, sr-only,
             screen-reader, htmlFor, autoFocus, <dialog, aria-modal
   `aria-disabled` (5) is new since the era-10 histogram of 10; era 11's GameLanguagePanel added it. The
   finding's substance is unchanged. Two consequences: `alt=` is zero and R1 adds five flag images, so R1
   is the first change in this product's history that NEEDS alt text; and `htmlFor` is zero, so no input
   is programmatically associated with its label.
```

### The remaining-scope table is incomplete in a way that matters, exactly as the handout warned

Eight more UI files carry visible copy that the handout's per-file table does not list, and one of them
holds the primary game buttons:

```text
components/game/GameControls.tsx      "Play" "Pass" "Exchange" "Cancel" "Confirm exchange"   <- primary
components/game/AIThinkingOverlay.tsx "AI Thinking" "Searching for moves..." "Best"/"BEST"
                                      "Filtering weak or invalid lines before showing a serious move..."
components/game/ChatPanel.tsx         "Game Chat" "Say something" "Send" "No messages yet."
                                      "Chat unavailable" "You"
components/board/Board.tsx            "Pinch to zoom" "Drag to pan" "Hide" "Reset" "PTS"
components/game/GameHistoryModal.tsx  "Games" "Close" "Review past boards, switch between AI and ..."
components/game/BlankPicker.tsx       "Choose a letter for blank tile"
components/tiles/TileRack.tsx         "No tiles on rack"
components/game/TurnStatusNotice.tsx  none — pure presentation
components/game/LuxeHoverText.tsx     none — pure presentation
```

This confirms rather than contradicts the R3 area list (`play`, `queue`, `waiting`, `game`, `controls`,
`board`, `overlay`, `chat`, `history`, `profile`, `prompt`, `a11y`): every one of those areas has a real
home. Three of these are already decided by the glossary — `BlankPicker`'s heading becomes
"Vyber písmeno pre žolíka" (which reads correctly *only* because `písmeno` and `žolík` are distinct
words), `Board`'s `"PTS"` becomes `b.`, and `GameControls` becomes "Zahrať / Vynechať / Vymeniť".

⛔ **A NEW over-count the handout does not warn about, and it is the most dangerous one.**

```text
frontend/src/lib/constants.ts   61 quoted capitalized literals, ALL of them TW / DW / TL / DL
```

Those 61 are the premium-square board layout — the physical Scrabble board. They are game data, not
copy. A translator subagent handed that file would silently corrupt the board. It belongs on the
"classify before you translate" list beside `provider-registry.ts` (LOCK A), `prompts.ts` (LOCK B),
`security-headers.ts`, the two AI routes, and `provider-logging.ts` / `provider-capability.ts` /
`types.ts`. Separately, `messages.en.ts` (52) and `messages.sk.ts` (46) appear in any raw sweep and are
the dictionary itself: a future inventory must exclude `frontend/src/lib/i18n/` or it double-counts its
own output.



### Sequencing decision: F1 before the destructive-migration preflight

The `11/01` handout capsule reads "issue slice F1 ... whose first action is the read-only
destructive-migration preflight and NOT migration execution". Taken literally that folds a database
preflight into a slice that touches no database. The accepted plan's section 16 is explicit that slice
F1 is pure `gamecore` with `Dependency: none`, `Rollback: revert code/assets; no DB effect`, and a
negative scope of "no app persistence"; migrations `0008`/`0009` belong to slice F2. Handout section 12
independently recommends landing F1 first because it is the cheapest place to discover that the
architecture is wrong.

Resolution by the era-11 Orchestrator: **F1 first, at E2 / INFOSEC R1, with an explicit prohibition on
any migration file, model change, database write, or `manage.py migrate` invocation.** The read-only
destructive-migration preflight is issued as its own fresh bounded exchange immediately before F2, which
is where the plan's own section 19 E4 staging puts it ("fresh preflight and backup/count evidence") and
where its row-count evidence is still current — the Cooperator plays test games, so counts measured two
slices early would expire anyway. The safety intent of the capsule line is preserved in full: nothing
touches the database before a read-only preflight.

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
    Status:          **CORRECTED at 8f44022** (S9) — NOT verified-closed.
                     BOTH call sites are locale-aware. `grep -rn '"en-US"' frontend/src` returns only the
                     two `locale === "en" ? "en-US" : locale` mappings plus one test assertion.
                     Orchestrator-verified through both real shipped functions; both English outputs are
                     byte-identical to the old behaviour. The `memberSince` useMemo carries `locale` in
                     its dependency list, so a language switch re-renders the date rather than leaving a
                     stale English one. Not verified-closed because no independent audit has run and
                     Cooperator rendered acceptance of the profile modal is still outstanding.
    Status:          **HALF corrected at d806e31** (S8) — still OPEN.
                     GameHistoryPanel.tsx `formatUpdatedAt(value, locale)` now takes the active locale
                     and maps `en` -> `en-US` so English output is byte-identical. Orchestrator-verified
                     through the real shipped function: en `Sep 2, 4:35 PM`, sk `2. 9., 16:35`,
                     cs `2. 9. 16:35`, pl `2 wrz, 16:35` — 24-hour clock, no AM/PM.
                     `Intl` was MEASURED to produce the correct GENITIVE month for the long form in all
                     three Slavic locales (`2. septembra 2026`, `2. září 2026`, `2 września 2026`), so no
                     hand-built month table and no date library were needed.
                     ⛔ ProfileModal.tsx:18-28 `formatJoinedDate` still hardcodes "en-US". The finding
                     stays OPEN until slice S9 corrects that second, independent call site.

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
    Status:          **corrected at 5a96b5e** (Worker session 02 exchange 01) — NOT verified-closed.
                     The prescribed regression test was performed as a loopback SSR probe and the
                     Orchestrator reproduced it independently on a different port: with
                     Cookie: libretiles_locale=sk the server HTML now contains "Prihlásiť sa" x1 and
                     "Sign In" x0, against x0 / x1 at the baseline. Also correct for cs and pl, and
                     English for fr / cz / hu / SK / empty. It is NOT verified-closed because no
                     independent audit has run; rendered acceptance is requested as batch B17.
                     ROOT-CAUSE NOTE PRESERVED: this was an Orchestrator design defect. The
                     correction inverts the original contract — the cookie is now the rendering
                     source of truth and the store only persists — so the class of defect is removed
                     rather than patched.
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
            CLOSED at 5a96b5e: frontend/src/lib/i18n/translate.ts is exactly that React-free split.
            layout.tsx imports `t` from it, the local textFor() is gone, and the catalog tables live in
            one `Record<Locale, ...>` so a fifth locale without a catalog is a tsc error. The single
            deliberate cast inside `tf` and its explanatory comment were moved verbatim. Small residual:
            that comment still says "between the two catalogs" while there are now four — the reasoning
            is unchanged, only the count in the prose is stale; fold it into the next slice touching
            the file.
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

### S11 acceptance, resolved by Cooperator decision 10 on 2026-09-02

He was asked directly whether a screen reader is available. Answer: **"Nemám a nechcem ju inštalovať."**
That settles the acceptance shape, and it is a permanent ceiling rather than a scheduling detail.

```text
HE OBSERVES — keyboard only, no screen reader needed
  1  Profile, Games, the blank picker and the rival-unavailable overlay each take focus when they open
  2  Escape closes each of those four
  3  Tab still walks the page and never becomes unescapable (no trap was written, by design)
  4  focus is NOT restored to the opener on close — expected, uii-01-F19, accepted residual
  5  ⛔ THE ONE OUTSTANDING ITEM, available from `f40d8a0`: Tab onto a rack tile, press Enter or Space,
     and the tile is selected. At `74b5339` this FAILED (uii-01-F24). `AC-RACK-KEYBOARD` asserts the
     handler from SOURCE, because React does not serialize event handlers into static markup, so his
     observation is the only thing that can prove a browser dispatches it.
CLOSED BY INSPECTION ONLY — never observable in this project
  6  whether the rack tile announces "Písmeno A, 1 bod"
  7  whether the turn banner, toasts and AI overlay announce at all              uii-01-F22
  8  whether the AI overlay re-reads itself every second                         uii-01-F21
```

⛔ Items 6–8 must be written into `99_closure.md` as **inspection-only**, never as an observed pass, and no
later session may summarize this whole as "accessibility verified". Those three findings are corrected on
the strength of ARIA semantics plus string-rendered markup, and that is the whole of the evidence.
`uii-01-F20`, `uii-01-F23` and `uii-01-F24` are different: they are structural, and item 5 makes F24
genuinely observable.

This also retires the ledger line "modal focus trap and ESC" from the manual-acceptance list above: ESC is
covered by item 2, the focus trap does not exist by design, and the announcement half is unobservable.


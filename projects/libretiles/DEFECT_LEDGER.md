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

## Open defects

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

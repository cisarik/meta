### Report for ORCHESTRATOR_CHAT

Logical whole identity: backend-security-hardening  
Worker session ordinal: 10  
Worker exchange ordinal: 01

Status: PASS  
Phase-qualified result: not-applicable  
Start commit: `9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1`  
End commit: `9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1` (no mutation)  
Changed paths: none  
Validation: read-only repository gate, lockfile/inventory comparison, `poetry check` / `poetry check --lock`, `pip list`, `npm ls`, `npm audit`, OSV.dev querybatch + per-advisory fetches, PyPI JSON, npm registry metadata. No application, no provider call, no forbidden install/lock mutation.  
Git result: read-only, none  
Deviations and missing evidence: no `pip-audit` / `osv-scanner` / GitHub Advisory HTML (not installed / not an authorized host). Standing mypy/ruff/pytest/vitest/lint/build gates from prompt §5 were not re-run. Dynamic exploit confirmation was not performed.  
Smallest next step: Orchestrator presents the open `medium`/`high` residuals to the Cooperator for sign-off or a bounded correction (at minimum: `next` 16.2.0 → a patched 16.2.x/16.3.x, Django 5.2.12 → ≥5.2.17, Daphne 4.2.1 → ≥4.2.2), then a fresh re-audit of those package bumps.  
Report justification: new-evidence  
Authority expiry: this exchange's authority expires with this terminal report. No correction, no acceptance, no logical-whole closure, no closure signal.

Independence: I did not implement any part of this candidate in this session.

Resolved Execution Issues / Near-Misses: none  
Pre-Existing Failure Classification: none

---

## Security audit report

### Audit header

Security task class: dependency and supply-chain audit (INFOSEC.md 4.7, structural profile P-4)  
INFOSEC route: R3  
Owned/authorized target: `/home/agile/Projects/libretiles`, owned by the Cooperator (Michal Cisárik), canonical remote `https://github.com/cisarik/libretiles`. Authorization basis: Cooperator ownership plus Orchestrator grant in the session-10 prompt. No other host was scanned.  
Commit under audit: `9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1`  
Repository gate (reconciled before analysis): HEAD, `HEAD:.ap`, `.ap` HEAD, `origin/main` all `9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1` / AP pin `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `## main...origin/main`; porcelain empty before and after.  
Scope: the seven questions in the prompt (manifest/lock consistency; known-vulnerability signals with INFOSEC §13 reachability; dev/production boundary; typosquatting/confusion; abandonment/maintenance; build provenance; the two open dependency questions).  
Exclusions: application logic, authentication design, CSP content, throttling policy, websocket tickets, and every `audit-01` / `orch-01` / `orch-02` finding (separate re-audit); the nine AI provider names/tuples/tiers (standing freeze); host/infrastructure hardening (INFOSEC 4.9); any system other than this repository and the authorized registries.

### Source records

| Title | Owner | Version / edition | Status | Retrieval date | AP concept |
|---|---|---|---|---|---|
| NIST SSDF, SP 800-218 | NIST | v1.1 | final | 2026-09-01 (registry dated 2026-07-19; rechecked as time-sensitive) | vulnerability response / lifecycle |
| CISA/FBI Product Security Bad Practices | CISA + FBI | v2.0 | final guidance | 2026-09-01 | bad-practice anchors |
| OWASP ASVS | OWASP | 5.0 | final | 2026-09-01 | verification mapping |
| OWASP Top 10 | OWASP | 2025 | awareness | 2026-09-01 | prioritization only |
| MITRE CWE | MITRE | corpus current; 2025 Top 25 | taxonomy | 2026-09-01 | weakness taxonomy ≠ reachability |
| OpenSSF OSPS Baseline | OpenSSF | v2025-10-10 | tooling | 2026-09-01 | repository-posture controls |
| SLSA | OpenSSF community | v1.2 | final | 2026-09-01 | provenance / release integrity |
| OSV.dev querybatch + `/v1/vulns/{id}` | Google OSV | API live | tooling | 2026-09-01 | advisory identity and affected ranges |
| npm audit v2 (`--json` and `--package-lock-only`) | npm, Inc. | npm 12.0.1 | tooling | 2026-09-01 | npm advisory signals |
| PyPI JSON (`/pypi/<name>/json`) | Python Packaging Authority | live | tooling | 2026-09-01 | package identity, requires, upload times |
| npm registry metadata (`npm view`, `registry.npmjs.org`) | npm, Inc. | live | tooling | 2026-09-01 | package identity, latest, modified times |
| `backend/poetry.lock` / `frontend/package-lock.json` | this repository | commit under audit | project | 2026-09-01 | lock pins and hashes |

Advisory HTML on `github.com/advisories` was **not** fetched (host not authorized). Advisory titles, aliases, ranges, and CWE came from npm audit JSON and OSV.dev.

### Threat model (as applied)

Assets: nine provider API credentials in the Next.js server process; Django `SECRET_KEY`; JWT access/refresh tokens in `localStorage`; Django superuser session; game/account database; integrity of the built frontend artifact a browser executes.  
Trust boundaries: package registry → developer machine at install; registry → future build host (documented as Vercel, not configured in-tree); third-party code → Next.js server (credentials); third-party code → browser (JWTs); third-party code → Django (database, secret key).  
Attacker-controlled inputs: published package versions and transitives; typosquatted/confusable names; compromised maintainer; lockfile that does not pin what the manifest claims.  
Security properties relied on: lockfile pins install; no reachable known vulnerability in the deployed surface; declared names are the packages they claim; credential/auth packages are maintained; deployed artifact contains no dev-only dependency.  
Abuse cases: (a) malicious AI-SDK-chain package reads `process.env` on the Next server; (b) malicious browser-bundle package reads `localStorage` JWTs; (c) compromised Django dependency reads DB/secret; (d) install-time script on developer/build host; (e) lockfile drift so the reviewed version is not the installed version.  
Correction vs prompt §1: none. Evidence supports this model. One refinement: the production Python throttle cache additionally trusts the `redis` client that Django `RedisCache` imports, even though that name is not a direct manifest dependency.

---

### Findings

#### audit-02-F01

```text
Finding ID: audit-02-F01
Title: Production next@16.2.0 is inside the affected range of multiple patched App Router advisories
Status: open
Severity: high
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: frontend/package.json (next exact 16.2.0); frontend/package-lock.json node_modules/next@16.2.0; frontend/src/app/** (App Router); frontend/src/middleware.ts
Security property: deployed frontend runtime is free of reachable known vulnerabilities
Asset at risk: Next.js server process (provider credentials), browser-executed artifact, availability of AI/UI routes, integrity of security-header middleware
Trust boundary: unauthenticated HTTP to the Next.js deployment; package registry to that process
Attacker-controlled input or local actor: HTTP requests to the App Router / middleware / default Image Optimization path; no credential required for the DoS and several middleware-bypass classes
Reachability: entry point = public Next.js origin. Call path = App Router (established) + middleware.ts (established; matcher covers all routes except _next/static, _next/image, favicon, and prefetch-header skips). Deployed/enabled = production dependency, not lockfile-dev. Image Optimization path is referenced by the middleware matcher and is not disabled in next.config.ts. Server Actions, Pages i18n, Turbopack, custom servers, rewrites, CSP nonces, beforeInteractive scripts, Cache Components, and Next WebSocket upgrades are not established and are excluded from this finding (see rejected-false-positive records).
Preconditions: next 16.2.0; App Router; a middleware file (present). Several advisories are fixed only in 16.2.5, 16.2.6, 16.2.11, or by moving to 16.3.4.
Required privileges: unauthenticated
Observed or potential impact: unauthenticated denial of service of Server Components; middleware/proxy bypass that would skip this app's security-header injection (CSP, HSTS, X-Frame-Options, etc.) on matching requests; Image Optimization DoS if the default optimizer remains enabled. This is not a Django-auth bypass: Next middleware here does not implement authentication.
C/I/A effect: availability (DoS of the credential-holding Next process); integrity of security-header application; confidentiality not established for these advisories
CWE mapping: CWE-770, CWE-288, CWE-285, CWE-918 (version-qualified as named on the cited GHSAs; weakness ≠ proof of each CWE in this app)
ASVS mapping: ASVS 5.0 V1.4.3 / V14.2 (dependency freshness) — mapping, not completeness proof
Source-standard references: OSV/npm audit GHSAs listed below; SLSA v1.2 (no provenance to compensate); retrieval 2026-09-01
Dynamic reproduction evidence: none
Static evidence: next is a direct production dependency; npm audit and OSV both report 23 vulns for next@16.2.0; npm view next latest=16.3.4 (modified 2026-08-31); middleware.ts exists and is live
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: would be disproved if production did not use App Router or middleware, or if the deployed artifact were already ≥16.2.11 for the remaining bypass/DoS set. Pages-router, Turbopack-only, Server-Action, custom-server, rewrite, nonce, and Cache-Components advisories are already excluded.
Exploitability conclusion: probable
Smallest safe correction direction: bump next (and eslint-config-next) to a release that includes the 16.2.11/16.3.x fixes, regenerate the lockfile, and re-audit the new tree. Do not treat npm audit fix as authority.
Regression-test requirement: lockfile/version assertion that production next is outside the affected ranges, plus existing middleware header tests still passing
Residual risk: even a patched next remains a large trust-boundary runtime; future advisories will recur without a patch cadence
Acceptance-blocking decision: blocking — derived severity is high; medium-or-higher needs Cooperator sign-off if left unpatched
Redaction requirements: none beyond ordinary (no secrets were used)
```

Applicable advisory identities (version-in-range **and** feature present):  
`GHSA-q4gf-8mx6-v5v3`, `GHSA-8h8q-6873-q5fj` (Server Components DoS); `GHSA-267c-6grr-h53f` / CVE-2026-44575, `GHSA-26hh-7cqf-hhc6` / CVE-2026-45109, `GHSA-492v-c6pp-mqqv` / CVE-2026-44574 (App Router middleware/proxy bypass); `GHSA-h64f-5h5j-jqjh` / CVE-2026-44577, `GHSA-q8wf-6r8g-63ch` / CVE-2026-64644 (Image Optimization DoS; default not disabled); `GHSA-vfv6-92ff-j949`, `GHSA-wfc6-r584-vfw7`, `GHSA-4633-3j49-mh5q`, `GHSA-68g3-v927-f742` (RSC cache confusion/poisoning — App Router present; cache-precondition not dynamically proven, still version-applicable).  
npm's suggested fixAvailable is `next@16.3.4`.

#### audit-02-F02

```text
Finding ID: audit-02-F02
Title: Production Django 5.2.12 is below patched 5.2.13–5.2.17 with reachable ASGI and admin list_editable issues
Status: open
Severity: high
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: backend/poetry.lock django==5.2.12; backend/config/asgi.py (Daphne HTTP+WebSocket); backend/catalog/admin.py:43 and :113 list_editable
Security property: deployed Django runtime is free of reachable known vulnerabilities
Asset at risk: request-header integrity on the ASGI boundary; admin catalog integrity; availability under crafted ASGI bodies
Trust boundary: unauthenticated HTTP to Daphne/ASGI; authenticated Django admin for list_editable
Attacker-controlled input or local actor: ASGI header names (hyphen vs underscore); ASGI Content-Length; forged admin POST to a list_editable changelist
Reachability: ASGI is the deployed server (ASGI_APPLICATION, daphne in INSTALLED_APPS). Header-spoofing GHSA-mvfq-ggxm-9mc5 / CVE-2026-3902 therefore has entry point + enabled state. Content-Length / FILE_UPLOAD_MAX_MEMORY_SIZE and DATA_UPLOAD_MAX_MEMORY_SIZE bypasses (GHSA-w26r-rmm8-9c29 / CVE-2026-5766, GHSA-933h-hp56-hf7m / CVE-2026-33034) apply to ASGI request bodies; this app exposes unauthenticated JSON POST (register/login). MultiPartParser DoS (GHSA-5mf9-h53q-7mhq) is version-applicable; this app does not use FileField/ImageField, so file-upload-specific impact is weaker but ASGI body handling remains. list_editable is enabled on AIModelAdmin and AIPromptAdmin (GHSA-mmwr-2jhp-mc7j / CVE-2026-4292) — admin privilege required. Cache-middleware, GIS/GDAL/GEOS, STARTTLS, get_signed_cookie, SESSION_SAVE_EVERY_REQUEST, and GenericInlineModelAdmin paths are not established (rejected separately).
Preconditions: Django 5.2.12; ASGI/Daphne; admin list_editable on catalog models
Required privileges: unauthenticated for ASGI issues; admin for list_editable
Observed or potential impact: spoofed ASGI headers (integrity of Host/cookie/auth-adjacent headers); memory exhaustion via understated Content-Length; admin changelist POST creating unintended rows
C/I/A effect: integrity high (header spoofing); availability medium (ASGI body limits); integrity low given admin for list_editable
CWE mapping: CWE-444 / header conflation (CVE-2026-3902); CWE-770 (upload limits); CWE-285 (list_editable)
ASVS mapping: ASVS 5.0 V14.2, V13.1
Source-standard references: OSV records retrieved 2026-09-01; Django 5.2.12 uploaded 2026-03-03; fixes named through 5.2.17 (PYSEC-2026-3717 / CVE-2026-15830 is GIS-only and excluded)
Dynamic reproduction evidence: none
Static evidence: poetry.lock django==5.2.12; pip list Django==5.2.12; asgi.py ProtocolTypeRouter; catalog/admin.py list_editable
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: disproved if production were WSGI-only without Daphne, or if Django were ≥5.2.17. GIS-only PYSEC-2026-3717 is already excluded.
Exploitability conclusion: probable
Smallest safe correction direction: bump Django within the existing ^5.1 range to a 5.2 release that includes 5.2.17 (or the latest 5.2 patch at correction time) via poetry lock refresh of that one constraint; do not jump to 6.1 as part of this residual
Regression-test requirement: existing ASGI/admin tests plus a lock assertion on django>=5.2.17
Residual risk: remaining Django advisories after 5.2.17 would need a later audit
Acceptance-blocking decision: blocking — high (ASGI header spoofing)
Redaction requirements: none
```

#### audit-02-F03

```text
Finding ID: audit-02-F03
Title: Production daphne==4.2.1 has patched WebSocket memory-DoS and handshake header-smuggling advisories
Status: open
Severity: high
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: backend/poetry.lock daphne==4.2.1; backend/config/asgi.py websocket branch; backend/config/settings.py INSTALLED_APPS "daphne"
Security property: websocket transport cannot be abused for unbounded memory or handshake smuggling
Asset at risk: Django/Daphne process availability; websocket handshake integrity (AllowedHostsOriginValidator sits behind Daphne)
Trust boundary: unauthenticated or pre-auth WebSocket handshake to Daphne
Attacker-controlled input or local actor: arbitrarily large WebSocket frames; non-standard header line separators in the handshake
Reachability: entry point = product websocket surface (human-vs-human matchmaking/chat). Call path = Daphne → ProtocolTypeRouter → AllowedHostsOriginValidator → URLRouter. Deployed/enabled = daphne is the ASGI server. Application ticket/auth design is out of scope; these advisories are in the server before/around that logic.
Preconditions: daphne <4.2.2 (locked 4.2.1; latest on PyPI 4.2.3 uploaded 2026-07-21)
Required privileges: unauthenticated at the protocol layer (application may still require a ticket afterwards; not established as a mitigator for handshake smuggling)
Observed or potential impact: memory exhaustion; smuggled handshake headers relative to autobahn splitlines()
C/I/A effect: availability high; integrity of handshake headers
CWE mapping: CWE-770; header-smuggling class as named on GHSA-xh68-hfp5-5x5m / CVE-2026-44546
ASVS mapping: ASVS 5.0 V14.2, V13.1
Source-standard references: GHSA-rrc9-mx66-ffcm / CVE-2026-44545; GHSA-xh68-hfp5-5x5m / CVE-2026-44546; OSV 2026-09-01
Dynamic reproduction evidence: none
Static evidence: daphne==4.2.1 in lock and pip list; asgi.py websocket routing
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: disproved if production did not speak WebSocket through Daphne, or if daphne were ≥4.2.2
Exploitability conclusion: probable
Smallest safe correction direction: bump daphne to ≥4.2.2 (current latest 4.2.3) within the existing ^4.1 range
Regression-test requirement: existing websocket tests plus lock assertion
Residual risk: remaining autobahn/twisted issues that are not this handshake/frame pair
Acceptance-blocking decision: blocking — high availability/integrity on a live transport
Redaction requirements: none
```

#### audit-02-F04

```text
Finding ID: audit-02-F04
Title: Production throttle cache imports redis only as a transitive of channels-redis
Status: open
Severity: medium
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: backend/pyproject.toml (no direct redis); backend/poetry.lock redis==7.3.0 groups=["main"] via channels-redis; backend/config/settings.py:207 django.core.cache.backends.redis.RedisCache; Django cache backend `import redis` (site-packages, observed)
Security property: a security control's runtime is an explicitly declared, reviewable dependency
Asset at risk: production DRF throttle brake (fail-closed cache); availability of Django boot when DEBUG is false
Trust boundary: lockfile/resolver → Django process
Attacker-controlled input or local actor: local-actor / future lock regeneration / channels-redis dropping or extra-ing redis — not a remote exploit today
Reachability: production DEBUG=false always instantiates RedisCache. Django's backend does `import redis`. The import succeeds today because channels-redis 4.3.0 depends on redis>=4.6 and the lock pins redis==7.3.0 in group main.
Preconditions: DEBUG false; DJANGO_THROTTLE_CACHE_URL or REDIS_URL set; channels-redis remaining the only declared package that pulls redis
Required privileges: none (breakage is install/lock time or first cache use)
Observed or potential impact: a future channels-redis release that optionalizes, extras, or replaces redis would omit the client while RedisCache still loads → ImportError / failed throttle cache. poetry update of channels-redis can move redis 7.3.0 → 8.x without a direct constraint. This is not a CVE; it is an undeclared security-control dependency.
C/I/A effect: availability of the throttle brake; integrity of rate-limit sharing across workers if a broken client were selected
CWE mapping: CWE-1104 (use of unmaintained/undeclared third party) — taxonomy, not a CVE
ASVS mapping: ASVS 5.0 V14.2.1
Source-standard references: OpenSSF OSPS Baseline v2025-10-10; retrieval 2026-09-01
Dynamic reproduction evidence: none (did not uninstall redis)
Static evidence: pyproject has no redis; lock has redis via channels-redis; settings.py names RedisCache; Django redis.py contains `import redis`
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: disproved if redis were a direct pyproject dependency, or if production did not use RedisCache
Exploitability conclusion: not applicable
Smallest safe correction direction: declare redis as a direct runtime dependency with an explicit range compatible with Django RedisCache, then relock
Regression-test requirement: a test or packaging assertion that `redis` is a direct main-group dependency, in addition to existing production cache-settings tests
Residual risk: even a direct pin can still be abandoned; declaration only makes the control reviewable
Acceptance-blocking decision: blocking for residual acceptance — derived medium, needs Cooperator sign-off if left undeclared
Redaction requirements: none
```

#### audit-02-F05

```text
Finding ID: audit-02-F05
Title: No CI, SBOM, signing, or provenance attests the frontend artifact a browser executes
Status: open
Severity: medium
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: repository root (no .github/, no workflow, no sbom, no cosign/slsa files); frontend/package.json build script `next build --webpack`; docs/architecture.md claims Vercel auto-deploys from main (documentation, not in-repo attestation)
Security property: release integrity / build provenance
Asset at risk: the JavaScript a browser executes; provider credentials only if a malicious build also ships server routes
Trust boundary: git hosting and any future build host → browser
Attacker-controlled input or local actor: compromise of GitHub main, of a Vercel project token, or of an unsigned `next build` on a developer machine
Reachability: established as absence of control, not as a demonstrated compromise
Preconditions: none
Required privileges: whoever can push to main or trigger the undocumented deploy path
Observed or potential impact: a substituted lockfile or post-install mutation is not caught by CI because CI does not exist in-tree; nothing attests that the Vercel artifact matches this commit's lockfile
C/I/A effect: integrity of the deployed frontend
CWE mapping: CWE-494 (download of code without integrity check) — at the project-release layer
ASVS mapping: ASVS 5.0 V14.2; SLSA v1.2 (no provenance, SLSA 0)
Source-standard references: SLSA v1.2; OpenSSF OSPS Baseline v2025-10-10; retrieval 2026-09-01
Dynamic reproduction evidence: none
Static evidence: ls of repo root; glob for .github, workflows, sbom, cosign; next.config.ts has no signing; docker-compose.yml is local postgres/redis only
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: disproved if a private Vercel/GitHub Actions config exists outside this repository — that was out of scope and is recorded as a limitation, not as proof of provenance
Exploitability conclusion: not applicable
Smallest safe correction direction: add a lockfile-integrity CI job on the public repo (npm ci --ignore-scripts in CI is a later correction's choice) and, if Vercel is used, pin deploys to this commit SHA with whatever attestation that platform actually emits — direction only
Regression-test requirement: CI configuration exists in-tree and fails on lock/manifest mismatch
Residual risk: Vercel/GitHub account compromise still deploys malware even with CI, unless provenance is verified at runtime
Acceptance-blocking decision: blocking for residual acceptance — medium, Cooperator sign-off required to ship without in-repo provenance
Redaction requirements: none
```

#### audit-02-F06

```text
Finding ID: audit-02-F06
Title: Frontend has no mechanical production/dev-dependency boundary equivalent to the Python import guard
Status: open
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: frontend/ (no test analogous to backend/tests/test_game_app_has_no_dev_imports.py); that Python test itself only walks backend/game/*.py and forbids pytest/ruff/mypy, not django-stubs or config/accounts/catalog
Security property: deployed artifact contains no dev-only dependency
Asset at risk: browser bundle / Next server module graph
Trust boundary: install/build → runtime
Attacker-controlled input or local actor: local-actor (devDependency accidentally imported)
Reachability: not a vulnerability; a missing control. npm ls --omit=dev succeeded and listed the 12 direct runtime packages plus their production transitives (including next's nested postcss@8.4.31 and optional sharp@0.34.5). That is inventory, not a regression test.
Preconditions: none
Required privileges: none
Observed or potential impact: a future import of vitest/eslint into app code would not be caught by an existing mechanical test
C/I/A effect: none today
CWE mapping: none
ASVS mapping: ASVS 5.0 V14.2
Source-standard references: project test file cited above
Dynamic reproduction evidence: none
Static evidence: grep of frontend tests found no omit=dev / production-dependency guard
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: n/a
Exploitability conclusion: not applicable
Smallest safe correction direction: add a lockfile or bundler test that production compilation does not include packages marked lockfile-dev; optionally widen the Python AST guard beyond game/
Regression-test requirement: that new test
Residual risk: Next may still compile first-party CSS via nested postcss at build time (see rejected postcss runtime path)
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

#### Rejected-false-positive records

**audit-02-F07** — npm audit `@babel/core`, `brace-expansion`, `js-yaml`, `picomatch` as production high/low.

```text
Finding ID: audit-02-F07
Title: npm audit high/low issues in babel, brace-expansion, js-yaml, and picomatch are lockfile-dev
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: frontend/package-lock.json entries all have "dev": true (babel 7.29.0; brace-expansion 1.1.12 and 5.0.4 under typescript-eslint; js-yaml 4.1.1; picomatch 2.3.1 and 4.0.7 under vitest/vite/tinyglobby)
Security property: n/a (not production)
Asset at risk: developer machine / test runner only
Trust boundary: none in the deployed surface
Attacker-controlled input or local actor: n/a for production
Reachability: not established for production; lockfile marks these dev. They remain install-time/dev-tool risk if eslint/vitest process untrusted files, which is outside the production finding class the prompt forbade.
Preconditions: n/a
Required privileges: local
Observed or potential impact: none on the deployed Next/Django surface
C/I/A effect: none in production
CWE mapping: n/a
ASVS mapping: n/a
Source-standard references: npm audit v2 2026-09-01
Dynamic reproduction evidence: none
Static evidence: lockfile "dev": true on every listed path
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: disproving evidence is the lockfile dev flag plus npm ls --omit=dev omitting these packages. Scanner "high" is not derived severity.
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none required for production
Regression-test requirement: keep them in devDependencies
Residual risk: developer-workstation supply chain if those tools parse attacker-controlled trees
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

**audit-02-F08** — Django cache-middleware, GIS, STARTTLS, signed-cookie, SESSION_SAVE_EVERY_REQUEST, GenericInline, and GIS PYSEC-2026-3717.

```text
Finding ID: audit-02-F08
Title: Several Django OSV hits are not enabled in this application
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: backend/config/settings.py MIDDLEWARE (no UpdateCacheMiddleware / FetchFromCacheMiddleware); INSTALLED_APPS (no django.contrib.gis); no EMAIL/SMTP/STARTTLS settings; no get_signed_cookie; SESSION_SAVE_EVERY_REQUEST unset (Django default False); catalog/game admin uses TabularInline, not GenericInlineModelAdmin
Security property: n/a
Asset at risk: n/a
Trust boundary: n/a
Attacker-controlled input or local actor: n/a
Reachability: not established — required middleware, GIS, email, signing API, or GenericInline are absent
Preconditions: features not present
Required privileges: n/a
Observed or potential impact: none
C/I/A effect: none
CWE mapping: n/a
ASVS mapping: n/a
Source-standard references: OSV 2026-09-01
Dynamic reproduction evidence: none
Static evidence: settings.py MIDDLEWARE list; grep for GIS/email/signed cookie/SESSION_SAVE_EVERY_REQUEST/GenericInline
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: UpdateCacheMiddleware CVEs (GHSA-5hrc-gvxj-w55p, GHSA-8cjm-8mp7-r2xf, GHSA-qpc8-7fxc-cm4p, GHSA-3h9f-r86x-qvjx, GHSA-923m-gv2p-w5qp); GIS GDAL/GEOS (GHSA-crhf-3pfg-w68w, PYSEC-2026-3717 / CVE-2026-15830); STARTTLS (GHSA-mm6v-q8q9-pgcf); signed cookies (GHSA-h7pc-vwp9-298g); persistent cookies under SESSION_SAVE_EVERY_REQUEST (GHSA-7h2m-m8vj-598h); GenericInline (GHSA-pwjp-ccjc-ghwg). Disproved by missing feature.
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none
Regression-test requirement: do not add those features without a Django bump
Residual risk: enabling cache middleware or GIS later would revive those signals
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

**audit-02-F09** — PyJWT OSV cluster vs SimpleJWT HMAC.

```text
Finding ID: audit-02-F09
Title: PyJWT 2.12.1 advisories require PyJWKClient, mixed algorithm families, or detached JWS — not this app's SimpleJWT config
Status: rejected-false-positive
Severity: info
Confidence: medium
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: backend/config/settings.py SIMPLE_JWT (lifetimes/rotation only; no ALGORITHM override, no JWK client); no PyJWKClient/JWK usage in the tree
Security property: n/a
Asset at risk: JWT integrity — not shown reachable via these CVEs
Trust boundary: n/a
Attacker-controlled input or local actor: n/a
Reachability: not established. SimpleJWT defaults to HMAC with the Django secret; GHSA-xgmm-8j9v-c9wx explicitly requires mixed symmetric+asymmetric algorithms and a raw JWK key. JWK SSRF/DoS GHSAs require PyJWKClient.
Preconditions: not met
Required privileges: n/a
Observed or potential impact: none established
C/I/A effect: none established
CWE mapping: n/a
ASVS mapping: n/a
Source-standard references: OSV GHSA-993g-76c3-p5m4, GHSA-fhv5-28vv-h8m8, GHSA-jq35-7prp-9v3f, GHSA-w7vc-732c-9m39, GHSA-xgmm-8j9v-c9wx; retrieval 2026-09-01
Dynamic reproduction evidence: none
Static evidence: SIMPLE_JWT block; grep found no PyJWK
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: would become open if SIMPLE_JWT were switched to RS256/JWKS
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none required; a later JWT-alg change would need pyjwt≥2.13.0
Regression-test requirement: n/a
Residual risk: pyjwt 2.12.1 remains below 2.13.0; version lag only
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

**audit-02-F10** — Next advisories whose preconditions this app does not meet.

```text
Finding ID: audit-02-F10
Title: Subset of next@16.2.0 advisories is not applicable to this App Router / webpack / no-Server-Actions tree
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: frontend/src/app (no pages/); frontend/next.config.ts (no rewrites, no cacheComponents, no i18n); package.json scripts use --webpack; no "use server"; no next/script beforeInteractive; CSP uses 'unsafe-inline' not nonces; websockets are Django Channels, not Next upgrades
Security property: n/a
Asset at risk: n/a
Trust boundary: n/a
Attacker-controlled input or local actor: n/a
Reachability: not established for this subset
Preconditions: missing
Required privileges: n/a
Observed or potential impact: none
C/I/A effect: none
CWE mapping: n/a
ASVS mapping: n/a
Source-standard references: OSV 2026-09-01
Dynamic reproduction evidence: none
Static evidence: no pages/; webpack flags; grep for use server / beforeInteractive / rewrites / cacheComponents / i18n
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: GHSA-36qx-fr4f-26g5 (Pages i18n); GHSA-6gpp-xcg3-4w24 (Turbopack); GHSA-89xv-2m56-2m9x, GHSA-4c39-4ccg-62r3, GHSA-m99w-x7hq-7vfj, GHSA-955p-x3mx-jcvp (Server Actions / server functions / custom server); GHSA-p9j2-gv94-2wf4 (rewrites); GHSA-ffhc-5mcf-pf4q (CSP nonces); GHSA-gx5p-jg67-6x7h (beforeInteractive); GHSA-mg66-mrh9-m8jx (Cache Components); GHSA-c4j6-fc7j-m34r (Next WebSocket upgrades). Disproved by missing features. GHSA-3g8h-86w9-wvmq (middleware redirect cache-poison) is not included here: middleware returns NextResponse.next() only, so redirect poisoning is not established.
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none beyond F01's next bump
Regression-test requirement: n/a
Residual risk: enabling Server Actions, Turbopack production, or rewrites would revive those IDs until next is patched
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

**audit-02-F11** — pytest, pygments, twisted.names, and other non-production or unused Python signals.

```text
Finding ID: audit-02-F11
Title: OSV hits on pytest, pygments, and twisted.names are not production-reachable
Status: rejected-false-positive
Severity: info
Confidence: high
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: poetry.lock groups=dev for pytest and pygments; no twisted.names import (Twisted is pulled by Daphne; names DNS server is not run)
Security property: n/a
Asset at risk: n/a
Trust boundary: n/a
Attacker-controlled input or local actor: n/a
Reachability: not established
Preconditions: missing
Required privileges: n/a
Observed or potential impact: none in production
C/I/A effect: none
CWE mapping: n/a
ASVS mapping: n/a
Source-standard references: OSV 2026-09-01
Dynamic reproduction evidence: none
Static evidence: lockfile groups; grep found no twisted.names / ujson / sqlparse / PyJWK imports in project code
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: GHSA-6w46-j5rx-g56g (pytest tmpdir); GHSA-5239-wwwm-4pmq (pygments ReDoS); GHSA-grgv-6hw6-v9g4 (twisted.names DNS). sqlparse, idna, msgpack, cryptography, pyasn1, and ujson remain version-in-range signals whose call paths were not established (see Limitations), not promoted to open findings.
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none
Regression-test requirement: n/a
Residual risk: unused Twisted/autobahn surface area still sits in the Daphne process
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

**audit-02-F12** — nested `postcss@8.4.31` under next (production tree, not lockfile-dev).

```text
Finding ID: audit-02-F12
Title: next's nested postcss@8.4.31 is in the production tree but the advisory path is attacker-controlled CSS, which this app does not accept
Status: rejected-false-positive
Severity: info
Confidence: medium
Evidence class: established-static
Affected commit: 9ff9ac56137d44bdb2d9f2d0a467f46921eb6da1
Affected component and exact location: frontend/package-lock.json node_modules/next/node_modules/postcss@8.4.31 (dev unset = production tree); top-level postcss@8.5.26 is lockfile-dev (tailwind) and had 0 OSV hits
Security property: n/a for runtime requests
Asset at risk: build host files if untrusted CSS were compiled
Trust boundary: build-time CSS, not the browser request path
Attacker-controlled input or local actor: would require attacker-controlled CSS sourceMappingURL in first-party or dependency CSS
Reachability: not established for production HTTP. Next compiles first-party CSS at build. No user-uploaded CSS pipeline exists.
Preconditions: attacker CSS not present
Required privileges: n/a
Observed or potential impact: none established on the request path
C/I/A effect: none established
CWE mapping: CWE-22 on the advisories (GHSA-6g55-p6wh-862q, GHSA-fxqj-rqcc-2cmp, GHSA-r28c-9q8g-f849, GHSA-qx2v-qp2m-jg93)
ASVS mapping: n/a
Source-standard references: OSV 2026-09-01
Dynamic reproduction evidence: none
Static evidence: npm ls --omit=dev shows postcss@8.4.31 under next; no user CSS ingest
Synthetic containment: /tmp/libretiles-p4-audit (removed)
False-positive analysis: would reopen if the app compiled untrusted CSS or if a compromised CSS dependency were added. A next bump (F01) is the same correction that replaces this nested copy.
Exploitability conclusion: not demonstrated
Smallest safe correction direction: none beyond F01
Regression-test requirement: n/a
Residual risk: build-host file read if a dependency CSS ever carries a malicious sourceMappingURL
Acceptance-blocking decision: non-blocking
Redaction requirements: none
```

---

### Per-question verdict table

| # | Question | Verdict | Reason |
|---|---|---|---|
| 1 | Manifest and lockfile consistency | **established** | Poetry: 62 `[[package]]` entries, every one has sha256 file hashes, `poetry check` and `poetry check --lock` exit 0, lock-version 2.1. pip list matches lock versions (zope.interface is lock `zope-interface`; `libretiles-backend` and `pip` are not lock packages). Marker-gated not-installed: async-timeout (Python ≥3.11.3), colorama (win32/dev), tzdata (win32), u-msgpack-python (non-CPython). npm: lockfileVersion 3, 506 `node_modules` keys, **0 missing integrity, 0 missing resolved**, all `resolved` on `registry.npmjs.org`, root dependencies exactly equal package.json. Installed versions match lock where present; 92 missing-on-disk entries are all `optional` (other OS/CPU). Top-level `node_modules` non-hidden count = **319**. Production lock non-dev packages = **74**; lockfile-dev = **432**. |
| 2 | Known-vulnerability signals with reachability | **partially established** | npm audit and OSV were run. Open findings F01–F03 are the reachable production set. Remaining Python OSV hits (sqlparse, idna, msgpack, cryptography, pyasn1, ujson) are version-in-range **signals** whose entry/call path was **not established** (hypothesis-unverified, not findings). No pip-audit binary. No dynamic PoC. |
| 3 | Dev/production boundary | **partially established** | Poetry groups: 40 main, 6 main+dev, 16 dev-only. Python AST guard exists but only for `backend/game/` and a small forbidden set. Frontend: no equivalent test (F06). `npm ls --omit=dev` shows the 12 direct runtime deps plus next/ai transitives (including `@ai-sdk/gateway` unused-at-product-level, nested postcss, optional sharp). Install scripts: `sharp` (optional, next image), `unrs-resolver` (dev), `fsevents` (dev optional). |
| 4 | Typosquatting / dependency confusion | **established** (no incident) | Direct names resolve to the expected public packages. `django-axes==8.3.1` is Jazzband, `django>=4.2`, `asgiref>=3.6.0`; `ipware` extra not installed. PyPI `django-axe` exists as a **different** 0.5.22 package (author Brahma Dutta Upadhyay, `django<5`, last upload 2024-08-05) — a confusable name, but this repo did not install it. `django_axes` is the normalized alias of the Jazzband package. No `.npmrc`, no Poetry extra source, npm registry = `https://registry.npmjs.org/`. No private registry to shadow. Scoped npm names `@ai-sdk/*`, `@dnd-kit/*`, `@tailwindcss/*` exist on the public registry. |
| 5 | Abandonment / maintenance | **partially established** | Trust-boundary latest vs locked (PyPI/npm 2026-09-01): `next` 16.2.0 vs latest 16.3.4 (modified 2026-08-31) — stale **and** vulnerable (F01). `daphne` 4.2.1 vs 4.2.3 (2026-07-21) (F03). `django` 5.2.12 vs 5.2 line patched through 5.2.17; PyPI latest is 6.1 (F02). `django-axes` 8.3.1 **is** latest (2026-02-11). `djangorestframework-simplejwt` 5.5.1 **is** latest (2025-07-21). `channels` 4.3.2 and `channels-redis` 4.3.0 **are** latest. `httpx` 0.28.1 **is** latest 0.x (2024-12-06) — quiet, not a skipped patch. `ai` 6.0.116 vs latest 7.0.87 (actively releasing; no OSV hit on locked 6.0.116). `@ai-sdk/openai` 3.0.41 vs 4.0.53. `@dnd-kit/core` last modified 2024-12-05, still latest 6.3.1. `canvas-confetti` 1.9.4 is latest (2025-10-25). `redis` locked 7.3.0 vs latest 8.1.0 (transitive). Did not clone upstream git activity beyond registry timestamps. |
| 6 | Build provenance / release integrity | **established** (as absence) | No `.github`, no workflow, no SBOM, no signing, no SLSA provenance. Build is `next build --webpack`. `docker-compose.yml` is local postgres/redis only. Docs claim Vercel from `main`; that is not in-repo evidence of attestation (F05). |
| 7a | `django-axes==8.3.1` exact pin vs caret elsewhere | **established** | **Benefit**, while 8.3.1 remains latest: a security brake does not float through Poetry caret into an unreviewed axes 9. **Residual process risk**: if Jazzband ships 8.3.2+ with a security fix, this pin will not take it until a human bump — the same class of lag that currently hurts `next`/`django`/`daphne`. Not a present CVE. Mixed pinning is process inconsistency, not a vulnerability. |
| 7b | `redis` transitive for RedisCache | **established** | **Not acceptable** as the sole declared source of a production security-control library (F04). It works **today** because channels-redis 4.3.0 depends on `redis>=4.6` and the lock pins 7.3.0 into group main. It **breaks** if channels-redis drops/extra-s that dependency, if a lock refresh omits it while RedisCache remains, or if an install omits the channels-redis extra set. Fail mode is ImportError at cache init (likely fail-closed 500/boot fail), not a silent open throttle — still a supply-chain coupling on a security control. |

### Section 5 (Orchestrator observations) — independent check

Confirmed: 62 poetry packages; 10 runtime + 7 dev in pyproject; 12+10 in package.json; 319 non-hidden `node_modules` entries; no `.github`; `django-axes==8.3.1` added at `bbba2e9`, exact-pinned, ipware extra not installed, PyPI last release 8.3.1 on 2026-02-11; CPython 3.12.12; Node v26.4.0; npm 12.0.1; `next` exact 16.2.0; `react`/`react-dom` exact 19.2.4.  
**Contradicted / refined:** `django = "^5.1"` vs venv `5.2.12` is **not lock/venv drift**. The lock also pins `django==5.2.12`, pip matches, and `^5.1` allows 5.2.x. The security fact is **5.2.12 < patched 5.2.13–5.2.17**, not that Poetry resolved 5.2.  
**Not re-measured:** mypy/ruff/pytest/vitest/lint/build standing gates (out of this audit's command list).

### Commands run (none forbidden)

Permitted: `git rev-parse` / `status` / `ls-remote` / `log` / `log -S`; `env -u APPIMAGE -u ARGV0 -u APPDIR poetry check` and `poetry check --lock`; `pip list`; `npm audit --json --package-lock-only`; `npm audit --json`; `npm ls --omit=dev` (depth 0 and `--all`); `npm view`; `npm config get registry`; read-only Python against lockfiles; `curl`/`urllib` to `https://api.osv.dev`, `https://pypi.org`, `https://registry.npmjs.org` only.  
Forbidden not run: `npm install` / `ci` / `update` / `audit fix` / installing `npx`; `poetry install` / `add` / `lock` / `update`; any `pip install`; any Git write; no `.env` / `.env.local` read; no app/server/provider call; no command from package metadata.

Confirmations: `git status --porcelain=v1` empty at start and end; no `.env` file read; no source code transmitted (npm audit sent public package names/versions only, as authorized).

### Containment ledger

```text
Temporary root: /tmp/libretiles-p4-audit
Owner: this Worker
Mode: 0700
Contents class: scanner output and notes only (npm audit JSON, pip list JSON, OSV JSON, PyPI/npm metadata extracts). No secrets, no project source copies.
Cleanup owner: this Worker
Cleanup outcome: removed
```

Network targets (declared): `https://api.osv.dev`, `https://pypi.org`, `https://registry.npmjs.org` (npm audit/view). Cleanup of network: not applicable (no local listener).

### Limitations

- No `pip-audit`, `osv-scanner`, or GitHub Advisory pages (unauthorized host / not installed). Python advisories are OSV + PyPI only.  
- No dynamic reproduction of Next DoS, Daphne frame DoS, or ASGI header spoofing.  
- sqlparse / idna / msgpack / cryptography / pyasn1 / ujson: version-in-range OSV signals; call-path **not established**; left as hypothesis-unverified, not findings.  
- Vercel/GitHub account configuration outside the repository was out of scope; F05 is absence-of-control in-tree.  
- `backend/.venv` and `frontend/node_modules` were compared to lockfiles; they are not the Vercel/production image.  
- Did not re-run application test/lint/build gates.  
- `@ai-sdk/gateway` is a production-tree transitive of `ai` and is unused as a product router per project docs; no OSV hit; not a finding.

### Residual-risk summary (for Orchestrator acceptance)

| Residual | Derived severity | Cooperator sign-off? |
|---|---|---|
| F01 next@16.2.0 reachable advisory cluster | **high** | **yes** — blocking until bump or explicit acceptance |
| F02 Django 5.2.12 ASGI header spoofing (+ related ASGI body / admin list_editable) | **high** | **yes** — blocking |
| F03 daphne 4.2.1 WebSocket DoS/smuggling | **high** | **yes** — blocking |
| F04 redis undeclared for RedisCache | **medium** | **yes** |
| F05 no CI/provenance | **medium** | **yes** to ship unsigned |
| F06 no frontend prod-boundary test | **info** | Orchestrator may accept |
| django-axes exact pin | **info** (benefit while latest) | no |
| Django ^5.1 resolving 5.2.12 | **info** (not drift); the patch lag is F02 | covered by F02 |
| httpx 0.28.1 quiet 0.x line | **info** | no |
| Dev-only npm/Python advisories | rejected | no |
| Unreachable Django/Next/PyJWT OSV subset | rejected | no |

This audit does **not** accept application corrections and does **not** close the logical whole. It is independent evidence for the dependency/supply-chain class only.

Logical-whole closure: not closed.
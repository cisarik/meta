### Report for ORCHESTRATOR_CHAT

**IHR-SLICE-4-PLAN — VPS templates, deployment scripts, and runbook**

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 08
Worker exchange ordinal: 01

status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Start commit: 7ffe0dc4d81b37afb1c22b68b55e7330869c86ef
End commit: 7ffe0dc4d81b37afb1c22b68b55e7330869c86ef
Changed files and purpose: none; no repository or Meta files written
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: identified and resolved the proposed plain-HTTP callback topology defect in the design
Pre-Existing Failure Classification: production-topology incompatibility found by inspection; no runtime failure asserted

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

The technical plan is decision-complete. Status is PARTIAL solely because this session’s higher-priority Plan Mode prohibits file writes, including the requested Meta report. The intended destination remains `/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/08_report_00.md`; it was not created.

Evidence is E0, non-independent: repository inspection and local dependency-source inspection. Both repository gates matched: required HEAD, AP gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, clean porcelain, branch `main`. No tests, build, network requests, provider calls, SSH, installations, services, or deployment scripts were run. Credential presence remains **unknown**; neither protected environment file was read.

### D1 — Artifact inventory

`landed-tested` below means committed regression coverage was inspected, not executed during this exchange.

Absence searches used:

- `find backend/scripts scripts docs \( -iname '*vps*' -o -iname '*nginx*' -o -iname '*systemd*' \) -print`
- `rg -n 'vps_preflight|vps_deploy|libretiles-backend.service|vps_deployment_guide' .`
- `git ls-files '*vps*' '*nginx*' '*systemd*' '*.service' 'ap.project.conf' 'backend/scripts/*' 'scripts/*' 'docs/*'`
- Repository-wide filename enumeration excluding dependencies, build artifacts, and `.git`.

| Artifact | Evidence | Status |
|---|---|---|
| `vps_preflight.sh` | No match in the filename/content searches above | missing |
| `vps_deploy.sh` | No match in those searches | missing |
| Backend systemd unit | No tracked `.service` or corresponding name | missing |
| Frontend systemd unit | No tracked `.service` or corresponding name | missing |
| nginx configuration | No nginx template found | missing |
| `docs/vps_deployment_guide.md` | No filename or reference found | missing |
| Architecture production topology | Production subsection specifies Vercel and Docker Compose; overview and diagram also label Next as Vercel | stale-docs |
| README VPS pointer | No VPS guide reference; existing startup instructions describe development | missing |
| `scripts/libretiles.sh` | Detached development supervisor using `runserver` and `next dev`, with `.dev/` state | landed-untested |
| `docker-compose.yml` | PostgreSQL/Redis helper; no application services | landed-untested |
| Next standalone output | No `output: "standalone"` in `frontend/next.config.ts` | out-of-slice |
| Django static collection | `STATIC_ROOT = BASE_DIR / "staticfiles"`; staticfiles app installed; output gitignored | landed-untested |
| Daphne dependency | `backend/pyproject.toml` declares `daphne = "^4.2.2"`; ASGI serves HTTP and websocket | landed-untested |
| SECRET_KEY strength checks | `_require_secret_key()` and regression cases in `test_security_settings.py` | landed-tested |
| Proxy trust defaults | Environment-gated SSL header defaults false; proxy count defaults zero; regression cases cover both | landed-tested |
| Seed activation preservation | `seed_models` excludes existing activation/order from updates; catalog regression tests cover preservation | landed-tested |
| HSTS preload warning | `test_security_settings.py` explicitly retains `security.W021` | accepted-residual |
| IHR-S1-F01 and IHR-S2-R01 | Accepted dispositions in the authoritative assignment; not reopened | accepted-residual |

H1, H2, H4–H8, and H10 are supported, with the documentation enumeration widened as noted above. H3’s public ownership is supported, but a plain production admin tunnel requires additional transport handling.

**H9 is falsified in its direct-callback detail.** Production settings enable `SECURE_SSL_REDIRECT`. Next’s catalog, AI, token-verification, and simulation fetches do not set a trusted HTTPS scheme. Consequently, `BACKEND_URL=http://127.0.0.1:8000` would encounter either host rejection or an HTTPS redirect toward the HTTP-only Daphne listener. Public nginx headers do not propagate automatically into these separately constructed fetches.

### D2 — Public request topology

Use one public hostname, `YOUR_DOMAIN`, with nginx terminating TLS. Preserve Daphne on `127.0.0.1:8000` and Next on `127.0.0.1:3000`.

| Public path | Destination |
|---|---|
| `/api/ai/` | Next :3000 |
| `/api/models`, `/api/models/` | Next :3000 |
| `/api/prompts`, `/api/prompts/` | Next :3000 |
| `/api/admin/simulate/<id>/turn`, with optional trailing slash | Next :3000 |
| Other `/api/admin/` paths | Daphne :8000 |
| `/api/catalog/` | Daphne :8000 |
| `/api/game/` | Daphne :8000 |
| `/api/auth/` | Daphne :8000 |
| `/ws/` | Daphne :8000, websocket upgrade |
| `/admin`, `/admin/` and descendants | Next :3000 |
| Django contrib admin | Unpublished on public 443 |
| `/static/` | Public 404; Django static assets remain private |
| Unknown `/api` or `/api/` paths | nginx 404 |
| `/`, other pages, Next assets | Next :3000 |

The measured Next route inventory contains five handlers: AI move, AI judge, models, prompts, and simulation turn. Staff pages are `/admin`, `/admin/login`, `/admin/playground`, `/admin/analytics`, and `/admin/replay/[id]`.

Resolve H9 through an additional **loopback-only nginx callback listener**, `127.0.0.1:8001`:

- Proxy only `/api/auth/`, `/api/catalog/`, `/api/game/`, and `/api/admin/` to Daphne.
- Set canonical Host and overwrite `X-Forwarded-Proto` with literal `https`.
- Return 404 for everything else.
- Never route public requests to this listener.

Production values:

```text
NEXT_PUBLIC_API_URL=https://YOUR_DOMAIN
BACKEND_URL=http://127.0.0.1:8001
```

This remains a loopback callback topology and needs no application-code change. The browser base contains neither `/api` nor an application port. It must be set before the Next build and remain consistent at runtime. `resolveApiBase()` then uses the public HTTPS origin; CSP permits that origin and `wss://YOUR_DOMAIN`; websocket construction produces `/ws/game/<id>/?ticket=…`.

Provide private Django administration through a separate nginx TLS listener at **`127.0.0.1:8443`**, using the same domain certificate. Expose only `/admin/` and collected `/static/` there; return 404 elsewhere. Its upstream Host is `YOUR_DOMAIN:8443`, preserving Django’s same-origin CSRF comparison. This avoids weakening HTTPS or secure-cookie settings for administration.

The runbook documents a later operator-owned SSH forward to this private listener, with workstation name resolution allowing `https://YOUR_DOMAIN:8443/admin/`. It does not prescribe a plain HTTP tunnel to Daphne as a working production-admin solution.

### D3 — nginx template

Create one configuration at `backend/scripts/nginx/libretiles.conf`, intended for inclusion inside nginx’s `http` context.

**Location selection**

- Use `location ^~ /api/ai/` for Next AI routes.
- Use exact locations for models/prompts, including trailing-slash forms.
- Use `location ~ ^/api/admin/simulate/[^/]+/turn/?$` for the Next simulation stream.
- Use an ordinary prefix location for `/api/admin/`. **Do not use `^~` there**, which would suppress the simulation regex.
- Use explicit Django prefixes for catalog, game, and auth.
- Use an ordinary `/api/` fallback returning 404; never a blanket Daphne proxy.
- Preserve the original URI through `proxy_pass` without a replacement URI suffix.

**Forwarded headers**

Every proxy location must receive a complete header set; repeat it where necessary to avoid nginx’s location-level inheritance trap:

```text
proxy_http_version 1.1
proxy_set_header Host $host
proxy_set_header X-Forwarded-Host $host
proxy_set_header X-Forwarded-Proto $scheme
proxy_set_header X-Forwarded-Port 443
proxy_set_header X-Forwarded-For $remote_addr
proxy_set_header X-Real-IP $remote_addr
proxy_set_header Forwarded ""
```

These public values assume nginx is the sole external reverse proxy. Do not append attacker-supplied forwarding chains. The forbidden proto source is **`$http_x_forwarded_proto`**.

The private callback listener replaces Host with `YOUR_DOMAIN`, proto with literal `https`, and port with `443`. The private admin listener uses `YOUR_DOMAIN:8443`, `$scheme`, and port `8443`. Both retain explicit loopback binds.

**Streaming and transport**

- Ordinary HTTP proxy locations clear Upgrade and Connection.
- `/ws/` sets `Upgrade $http_upgrade` and Connection through an `http`-level upgrade map; use `proxy_read_timeout 3600s`.
- AI and simulation-turn locations set `proxy_buffering off`, `proxy_request_buffering off`, `gzip off`, and read/send timeouts of `660s`.
- The 660-second allowance covers the measured 600-second maximum application timeout with transport headroom.
- Set `proxy_cache off`; introduce no API, authenticated-response, or SSE caching.

**TLS, static files, and headers**

- Public port 80 redirects to the canonical HTTPS domain. Public 443 uses `listen … ssl`, explicit `server_name`, and rejection of unexpected Host values.
- Ship clearly marked domain, installation-root, certificate, and certificate-key placeholders. Certificate provisioning remains an operator prerequisite.
- Use TLS 1.2/1.3. Do not install certificates or add an ACME workflow.
- Preserve Django and Next security headers. Add no duplicate nginx HSTS/CSP policy and no preload.
- Serve private `/static/` by alias from `PROJECT_ROOT/backend/staticfiles/`, with directory listing disabled.
- Use an access-log format excluding query strings, Authorization, cookies, and Referer so websocket tickets are not recorded.
- No new compression or static-cache policy is needed.

### D4 — systemd units

Create both units under `backend/scripts/systemd/`. Document `/srv/libretiles` as the installation default; templates use an explicit `PROJECT_ROOT` placeholder. Use the pre-created non-root account `libretiles`.

| Setting | Backend | Frontend |
|---|---|---|
| `User` / `Group` | `libretiles` | `libretiles` |
| `WorkingDirectory` | `PROJECT_ROOT/backend` | `PROJECT_ROOT/frontend` |
| `EnvironmentFile` | `PROJECT_ROOT/backend/.env` | `PROJECT_ROOT/frontend/.env.local` |
| `ExecStart` | `PROJECT_ROOT/backend/.venv/bin/daphne -b 127.0.0.1 -p 8000 --access-log /dev/null config.asgi:application` | `/usr/bin/node PROJECT_ROOT/frontend/node_modules/next/dist/bin/next start --hostname 127.0.0.1 --port 3000` |
| Additional environment | `PYTHONDONTWRITEBYTECODE=1` | `NODE_ENV=production` |

Use required, non-optional EnvironmentFiles. Provider credentials belong only in the frontend file/process environment.

For both units: `Type=simple`, `Restart=on-failure`, `RestartSec=5`, `TimeoutStopSec=30`, journald output, and `WantedBy=multi-user.target`.

For the documented Ubuntu/systemd topology:

- Backend: order after network-online, `postgresql.service`, and `redis-server.service`; require the two local data services.
- Frontend: order after network-online and the backend unit.
- Do not start installations, builds, migrations, or seed commands from unit lifecycle hooks.
- Do not enable Daphne `--proxy-headers`; retain the application’s existing proxy-trust boundary.

Use `NoNewPrivileges=true`, `PrivateTmp=true`, `ProtectSystem=full`, and `ProtectHome=true`. Local `systemd.exec(5)` documentation supports these meanings. `/srv` remains usable for application state and Next caches; no syscall filter or executable-memory restriction is introduced.

Daphne access logging is disabled at its access-log sink; application errors remain in journald, and nginx supplies bounded request logging.

### D5 — Scripts and operator safety

Both scripts use `/bin/bash` semantics, `set -euo pipefail`, and a help path that exits before probing or changing the host. Neither script sources dotenv files or prints environment values.

**`vps_preflight.sh`**

Default operation checks the selected Ubuntu/systemd host:

- Python **3.12**, plus venv availability.
- Node executable and compatible version; npm.
- Poetry **2.3.2**, matching the committed lockfile generator.
- PostgreSQL and Redis tooling and active local service status.
- nginx, systemctl, runuser, and flock availability.
- UFW status, without enabling, reloading, or changing rules.

Use Node 24 as the documented default. Accept the measured lockfile-compatible ranges: Node 20.19+, Node 22.12+, or Node 24+. Reject Node 21/23. The lockfile requires more than the prompt’s generic “20+”: Next requires 20.9+, Vite requires 20.19+/22.12+, and Vitest excludes 21/23.

Report each missing prerequisite clearly and return nonzero for missing, incompatible, inactive, or unverifiable prerequisites. An insufficient privilege to inspect firewall status is a failed check, not a reason to invoke sudo automatically. Service status is not advertised as database connectivity or host-hardening certification.

**`vps_deploy.sh`**

Interface:

```text
vps_deploy.sh --help
vps_deploy.sh --confirm-vps [--install-site /ABSOLUTE/RENDERED_CONF]
```

The first executable argument gate accepts help or requires `--confirm-vps`; all other invocations exit 2 before external commands, file creation, environment-file inspection, or service operations. Unknown options also fail.

After confirmation, require root for the host orchestration, acquire a non-overlapping `flock`, derive the project root from the script location, and require the pre-created `libretiles` account and matching installed units. Reject an installation under `/home` because the chosen unit hardening would hide it.

All dependency, build, and Django commands run as `libretiles`; never run npm or Poetry as root. The script:

1. Runs preflight and verifies required environment files, installed units, and any supplied site candidate are available.
2. Verifies an existing nginx configuration before stopping application services.
3. Stops frontend, then backend, for a documented maintenance window.
4. Creates `backend/.venv` with Python 3.12 only when absent; refuses an incompatible existing interpreter instead of deleting it.
5. Runs Poetry installation from the existing lock into that exact venv, using `--only main --no-root`; performs no dependency update.
6. Runs `npm ci --include=dev`, then `npm run build`; build dependencies must remain available despite production runtime mode.
7. Uses the project venv for Django checks, `migrate --noinput`, `seed_models`, and `collectstatic --noinput`. Let existing settings enforce SECRET_KEY strength. Add only non-secret deployment assertions for production debug/database/proxy settings; preserve accepted `security.W021`.
8. Restarts backend, then frontend, and checks their active status.

Require the operator to have installed and checked the stripping proxy before enabling `DJANGO_SECURE_PROXY_SSL_HEADER`. The script never writes either environment file or flips Django defaults.

`--install-site` is the only authority to replace the named Libre Tiles nginx site. It accepts an operator-rendered candidate, preserves the prior site/link state, installs atomically, runs `nginx -t`, and restores the previous state on validation failure. Reload only after successful application startup. Without the option, leave nginx site files and nginx runtime untouched.

No user creation, OS package installation, firewall changes, certificate issuance, Git operations, cron installation, catalog sync, provider probe, database deletion, or automatic downgrade belongs in this script. Unit installation is a documented manual prerequisite.

Idempotence means safe repeat application of the same deployment: reuse the venv, preserve environment files and Admin activation, use locked dependencies, apply pending migrations, collect static assets, and restart. It does not mean zero database writes or zero downtime.

On failure, report the failed phase without dumping environment or request data. Restore pending nginx changes; leave application services stopped after a failed deployment. Do not claim that restarting old code against partially migrated state is a rollback.

### D6 — Runbook

Create `docs/vps_deployment_guide.md` with this sequence:

1. **Authority and topology.** Identify the templates as repository artifacts. Every host command is a later operator-owned action. State public ports 80/443 and loopback ports 3000, 8000, 8001, and 8443; PostgreSQL/Redis remain private.
2. **Host preparation.** Document the selected Ubuntu/systemd layout, `/srv/libretiles`, non-root service account, prerequisites, directory ownership, and application maintenance window. Package installation, firewall policy, DNS, certificates, and SSH setup remain outside the implementation grant.
3. **Recovery preparation.** Require a verified database backup and recoverable previous application/dependency/build/configuration state before deployment. Explain that schema rollback requires migration-specific review.
4. **Environment setup.** Document names and non-secret configuration requirements without example credential values:

| Process | Variables and requirements |
|---|---|
| Django security | `DJANGO_SECRET_KEY` supplied privately; `DJANGO_DEBUG=false`; explicit `DJANGO_ALLOWED_HOSTS=YOUR_DOMAIN` |
| Browser-origin policy | `CORS_ALLOWED_ORIGINS=https://YOUR_DOMAIN`; explicit `DJANGO_CSRF_TRUSTED_ORIGINS=https://YOUR_DOMAIN` |
| Proxy trust | `DJANGO_NUM_PROXIES=1`; `DJANGO_SECURE_PROXY_SSL_HEADER=true` only after installing the stripping proxy |
| Database | `DB_ENGINE=postgresql`; `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`; document local service and optional connection-persistence settings |
| Redis | `REDIS_URL` for Channels; `DJANGO_THROTTLE_CACHE_URL` for shared throttles, with the existing REDIS_URL fallback |
| Catalog/reset controls | Preserve `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` by default and `ALLOW_DESTRUCTIVE_GAME_STATE_RESET=false` |
| Next origins | `NEXT_PUBLIC_API_URL=https://YOUR_DOMAIN`; `BACKEND_URL=http://127.0.0.1:8001`; explain the direct-8000 redirect defect |
| Next providers | Credential names from `frontend/.env.local.example`, including OpenRouter/NVIDIA and the shipped direct-provider names; never use `NEXT_PUBLIC_` credentials or copy them into Django |

5. **Environment handling.** Require restricted file permissions, literal assignments compatible with their consumers, and no shell sourcing. Explain startup-time loading, build-time public variables, conflicting dotenv files, and rebuild/restart requirements. Never print credential contents.
6. **nginx installation.** Render all placeholders outside Git, obtain certificates separately, install the reviewed configuration, test it, and verify the loopback/public listen distinction. Only then enable Django’s proxy-trust environment switch.
7. **systemd installation.** Render paths, install units, reload the manager, and enable the units without prematurely starting unbuilt services. Keep operational installation commands distinct from repository verification commands.
8. **Deployment.** Show preflight and the explicit-confirmation deploy invocation. Explain site replacement opt-in, downtime, failure disposition, and recovery.
9. **Operational checks.** Describe, but do not execute:
   - `curl` checks for HTTP-to-HTTPS redirect, public pages, catalog, `/api/models`, and `/api/prompts`.
   - `/api/auth/me/` without credentials returning an authentication failure, not a redirect; this checks the callback transport through the Next judge/auth path separately.
   - `/admin` showing the Next console and public Django-specific admin URLs never reaching contrib admin.
   - Staff API authentication failures without provider activity.
   - Browser multiplayer inspection showing a `wss://YOUR_DOMAIN/ws/game/…` 101 upgrade using a fresh ticket.
   - SSE arriving incrementally during a separately authorized game/simulation check.
   - `ss` and systemd status checks confirming loopback binds.
10. **Private contrib admin.** Document the TLS listener, SSH forward, workstation hostname mapping, secure URL, and cleanup of temporary mapping/tunnel. Use Django’s existing authentication and CSRF protections.
11. **Monitoring and catalog operations.** Document journald, nginx logs without query tokens, certificate expiry and failed service checks. Retain the existing daily 03:17 UTC catalog-refresh reminder; install no schedule.

Explain that `DJANGO_NUM_PROXIES=1` restores DRF’s public-client identity behind the one nginx hop. Axes still sees the socket peer without Daphne proxy parsing; Next-originated backend calls also have a loopback origin. Do not claim a new client-IP propagation or axes integration.

Correct only the architecture Production subsection and the two contradictory Vercel deployment labels in its overview/diagram. Add a short README deployment pointer; correct its stale `DEBUG` environment-table row to `DJANGO_DEBUG` with the code default. Preserve development instructions and unrelated architecture content.

### D7 — Test matrix and exact allowlist

Add **`backend/tests/test_vps_templates.py`**, using committed text and subprocess calls to **`/bin/bash -n` only**. It must not invoke either script, including its help path.

| Contract | Required assertions |
|---|---|
| Route ownership | All five measured Next handlers resolve to Next; Django prefixes resolve to Daphne; simulation regex remains eligible; unknown API paths deny |
| Admin separation | Public `/admin` reaches Next; private contrib admin requires loopback TLS; public `/static/` denies |
| Header trust | Every proxy block has the intended effective header set; public proto uses `$scheme`; private callback uses constant `https`; client proto passthrough is absent |
| Callback correctness | Port 8001 binds only loopback, forwards only Django API prefixes, uses canonical Host, and matches documented BACKEND_URL |
| Websocket/SSE | HTTP/1.1 and upgrade directives exist; streaming locations disable buffering/compression and have sufficient timeout |
| Units | Non-root user; exact loopback binds; Daphne ASGI; current `next start`; correct separate EnvironmentFiles; no installation hooks |
| Script guard | First argument gate contains required confirmation and exit-2 rejection before external commands/mutations; no alternative bypass; help exits early |
| Deployment boundaries | Locked installs, venv commands, migration/seed/static/build ordering, site opt-in, and failure handling are present; forbidden host automation is absent |
| Syntax | Both scripts pass `/bin/bash -n` |
| Preserved decisions | No preload added; existing W021 assertion remains; no standalone output introduced |

Use a small parser for the nginx directive/location subset actually shipped, with table-driven positive and negative route cases. Do not rely only on substring presence: catch `^~ /api/admin/`, a greedy Daphne `/api/`, missing headers after location overrides, and accidental public binding of private listeners.

Static checks establish the committed contract; they do not certify real nginx selection, runtime refusal behavior, TLS, or deployment recovery. Those require the later host gate.

Exact implementation allowlist:

```text
backend/scripts/vps_preflight.sh
backend/scripts/vps_deploy.sh
backend/scripts/nginx/libretiles.conf
backend/scripts/systemd/libretiles-backend.service
backend/scripts/systemd/libretiles-frontend.service
backend/tests/test_vps_templates.py
docs/vps_deployment_guide.md
docs/architecture.md
README.md
```

RF-16 verification from `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check tests/test_vps_templates.py

env -u APPIMAGE -u ARGV0 -u APPDIR \
  PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
  .venv/bin/pytest -c /dev/null -p no:cacheprovider \
  tests/test_vps_templates.py -q
```

The isolated pytest invocation avoids Django plugin initialization and its automatic protected dotenv read. The new module must import no Django/application code. Existing security and seed coverage is inspected and preserved; do not launch its ordinary Django-configured test route under this exchange’s secret restriction.

Inspect the resulting diff and executable modes. No frontend build, live nginx, SSH, Docker, Redis, external request, or deploy-script execution is part of verification.

All other paths remain outside the allowlist, including settings, application TypeScript, gamecore, migrations, dependency manifests/locks, `.ap`, local supervisor scripts, and Docker Compose.

### D8 — Implementation grant sketch

The next implementation grant should authorize a fresh Worker at the exact accepted baseline, with `Native planning mode: not-used`, the nine-path allowlist, repository-only mutation, and the static verification above.

Ordered implementation:

1. Create the nginx template, including public routing, private callbacks, and private TLS administration.
2. Create the two loopback systemd units.
3. Create the guarded scripts and their failure/site-restoration behavior.
4. Write the runbook and bounded documentation corrections.
5. Add and run the isolated static contract tests and Bash syntax checks.
6. Review the diff against the allowlist and accepted exclusions; submit non-independent implementation evidence.

**Proposed implementation tier: E2. INFOSEC route: R1.** This is a reversible, cross-layer repository-template change. It changes no deployed authentication, credential storage, or running host. No R3 trigger is introduced by the selected application-code-free approach. R5 remains a later operational gate; pinned INFOSEC §§4.8–4.9 require separate application and host audit treatment there.

**Cooperator-owned product decisions: none.** Host identity, actual domain, certificates, credentials, backup evidence, and operational authorization remain future deployment inputs.

**Slice 5 deferral:** Next standalone output is excluded because Slice 4 deliberately runs the existing build with `next start`.

Residual risks:

- Templates in Git do not make Django proxy trust safe until an operator installs the overwriting proxy.
- Local callback traffic trusts the VPS loopback boundary; public access to those ports must remain impossible.
- Static verification cannot prove certificate validity, actual listeners, streaming behavior, service readiness, or rollback execution.
- Deployment interrupts active requests and games; automatic database rollback is not supplied.
- Existing axes/socket-IP behavior, accepted residuals, staff authorization, seed activation invariants, and WordAuthority remain unchanged.

**Orchestration critique**

**MEASURED**

- H9’s direct HTTP callback URL conflicts with production HTTPS redirects and the measured server fetch implementations. The private nginx callback listener resolves it within the template-only scope.
- A plain tunnel to Daphne does not by itself preserve production admin HTTPS/cookie behavior. The private TLS listener resolves that without publishing contrib admin.
- “Node 20+” misses committed dependency engine constraints.
- Correcting only architecture’s Production subsection would leave two explicit Vercel topology labels.
- Ordinary pytest initialization can read the protected backend dotenv file; isolated static-test execution is required.
- The requested Meta write conflicts with this session’s higher-priority Plan Mode restriction.

**LEAD**

- Host-specific service readiness, resource sizing, certificate lifecycle, backup restoration, and effective proxy exposure need evidence at the later operational gate. They are not repository implementation acceptance claims.

**Enumeration widened:** tracked-file inventory beyond `backend/scripts`, `scripts`, and `docs`; all Next route files; server fetch helpers reached by `rg -n 'BACKEND_URL|forwarded|fetch\('`; local Django SecurityMiddleware and Daphne sources reached through the redirect/proxy findings; lockfile engine declarations; and local systemd manual pages. The `.ap/ap.project.conf` file belongs to the protocol submodule, not a Libre Tiles project-owned execution route.

**Report justification:** new-evidence

Planning authority expires at this report.

**Smallest next step:** issue a report-rendering-only exchange with native planning disabled to archive this frozen report at the required Meta path. Application implementation still requires its separate fresh-Worker grant.

**Context pressure:** moderate; the design, evidence boundaries, and remaining delivery restriction are fully captured.

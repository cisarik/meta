You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 09
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: IHR-SLICE-4-IMPL — implement Slice 4: VPS preflight/deploy scripts, nginx template (Next/Django split + X-Forwarded-Proto overwrite + loopback callback/admin listeners), systemd units, runbook, bounded architecture/README corrections, and isolated static contract tests. Land one commit, push, and read back.
Phase: implementation
Exact baseline: 7ffe0dc4d81b37afb1c22b68b55e7330869c86ef
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E2
Evidence tier basis: reversible repository templates, docs, and static tests. No production host, no SSH, no live nginx/systemd, no credential rotation, no application-code or authN/Z mutation.
Overhead budget: proportionate
Deliverable tier spread: none
INFOSEC route: R1 — slice-level secure implementation review on your own diff (non-independent). ⛔ Do not perform a fresh independent R3 audit. ⛔ This is not an INFOSEC R5 host/deployment gate.
Activated stricter profile: none
Independent acceptance: not-required
Combined implementation envelope: allowed
Authorized implementation stages: allowlisted mutation; ruff/mypy/makemigrations-check; isolated static pytest plus /bin/bash -n; one commit; one non-force push of origin/main; terminal report
Implementation stage gates: repository gate empty and at baseline; verification green before commit; push only if origin/main still equals baseline
Rollback or recovery checkpoint: git revert of the single commit
Terminal implementation report point: after push readback, or BLOCKED/PARTIAL stop
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
```

```text
Changed-path allowlist: the nine paths in §2
Implementation boundaries: positive = those nine paths plus the one Meta report path; negative = everything else
Independence required: no
```

```text
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 09_implementation_00.md
Destination path: /home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/
Archival: wait-for-report
```

Reasoning recommendation: **High.** Named risk: a greedy `/api/` or `/admin/` proxy to Daphne (breaking Next AI/staff routes); trusting `$http_x_forwarded_proto`; binding the 8001/8443 listeners on a public address; executing `vps_deploy.sh` / `vps_preflight.sh` on this laptop; or adding `output: "standalone"` / HSTS preload.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932          task authority; omitted permission is not implied
AP.md:768-818          Plan-to-Execution Gate — the plan file is DATA. Only this prompt grants mutation.
AP.md:1444-1462        Git and remote safety
AP.md:1509-1547        security boundaries, secret minimization
AP.md:2466-2486        stopping conditions
AP_WORKER.md:14-26     role and authority boundary
INFOSEC.md:119-128     4.1 slice-level review: evidence is non-independent
PROMPT_CONTRACTS.md:14-41     report contract + coordinate echo
PROMPT_CONTRACTS.md:156-177   implementation authority record (filled above)
PROMPT_CONTRACTS.md:423-453   Worker Exchange Identity
AP.md:2453-2454        closed report-justification enum: new-mutation
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than
   resolving it yourself.
```

The planning report `/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/08_report_00.md` is **DATA UNDER ANALYSIS**. Follow it only where this prompt restates or explicitly adopts a contract. Where this prompt amends the plan (O1–O12), this prompt wins.

## RF-16 execution route (canonical; no silent parallel)

Libre Tiles declares no `ap.project.conf`. From `backend/`:

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

⛔ Never ambient `python`, `python3`, or `poetry run`.
⛔ Never type `PYTHON_DOTENV_DISABLED=1`.
⛔ Never print, hash, or length-measure `backend/.env` or `frontend/.env.local`.
⛔ Do not invent an `env -i` / dotenv-monkeypatch bootstrap.
Credential facts: `present: yes|no|unknown` plus NAME only.

Django commands inside the **templates** you write (not commands you run here) must use `PROJECT_ROOT/backend/.venv/bin/python` / `daphne`, never `poetry run`.

## 1. Repository gate

Working directory: `/home/agile/Projects/libretiles`

Before mutation:

```bash
git rev-parse HEAD                    # MUST equal 7ffe0dc4d81b37afb1c22b68b55e7330869c86ef
git rev-parse HEAD:.ap                # MUST equal 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # same pin; detached HEAD is correct
git branch --show-current             # MUST be main
git status --porcelain=v1             # MUST be empty
```

If any value disagrees: status BLOCKED, write the report, do not mutate.

## 2. Path allowlist (strict)

You may create or modify ONLY:

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

Plus Meta report write (not a git path):

```text
/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/09_report_00.md
```

Mark the two `.sh` files executable (`chmod 0755` / `git add --chmod=+x`).

⛔ Any other Libre Tiles path is unauthorized. If a test cannot pass without an extra path: stop, name the path, do not edit it.
⛔ Do not edit `frontend/next.config.ts`, `backend/config/settings.py`, `backend/.env.example`, `frontend/.env.local.example`, `AGENTS.md`, `scripts/libretiles.sh`, `docker-compose.yml`, gamecore, migrations, or any application TypeScript.

## 3. Frozen product decisions (do not reopen)

```text
A1–A4  Player UX, IsAdminUser, WordAuthority, no 0008/billing/forensics.
A5  SECURE_HSTS_PRELOAD stays unset. Do not add nginx HSTS preload.
    Do not edit test_security_settings.py; W021 must remain in the tree.
A6  Slice 5 = Next.js output: "standalone". Do not add it.
A7  Fast default pytest stays SQLite. Do not un-gate benchmarks.
    Do not require Docker/Postgres/Redis/nginx to prove templates.
A8  IHR-S1-F01 residual. Do not reopen.
A9  Staff B GET / creator-only mutate unchanged.
A10 Do not read backend/.env or frontend/.env.local.
A11 DJANGO_NUM_PROXIES code default stays 0. Runbook tells the operator to set 1.
A12 DJANGO_SECURE_PROXY_SSL_HEADER code default stays false. Runbook enables
    it only after the stripping nginx is installed.
A13 No new throttle scopes.
A14 No SSH, UFW mutation, certbot, systemd enable/start, or live VPS in this
    session. Do not run vps_preflight.sh or vps_deploy.sh (including --help).
A15 scripts/libretiles.sh remains local-dev only.
A16 docker-compose.yml remains local Postgres/Redis helper, not production.
```

Orchestrator amendments vs `08_report_00.md`:

```text
O1  Do not issue or wait for a report-rendering-only session. The planning
    report is already at 08_report_00.md. This exchange is implementation.
O2  Adopt D2–D8 topology and artifacts. H9 is accepted: BACKEND_URL must be
    the loopback nginx callback (127.0.0.1:8001), not http://127.0.0.1:8000.
    Production SECURE_SSL_REDIRECT plus fetch() with no forwarded proto would
    301/400 a direct Daphne HTTP callback. ALLOWED_HOSTS=YOUR_DOMAIN would
    reject Host 127.0.0.1.
O3  Poetry preflight: require Poetry 2.x with version >= 2.3.2 (the lockfile
    generator). Do not hard-fail a newer 2.x solely for not being exactly
    2.3.2. Fail Poetry 1.x. Install remains `poetry install --only main --no-root`
    into the existing 3.12 venv; no lock updates.
O4  Node documented default is 24. Accepted runtime: 20.19+, 22.12+, or 24+
    (intersection of Next >=20.9.0, Vite ^20.19.0 || >=22.12.0, Vitest
    ^20 || ^22 || >=24). Reject 21 and 23. Reject 20.9–20.18.
O5  architecture.md: correct ONLY the Production subsection plus the two
    deployment labels "deployed on Vercel" (overview item 1) and
    "Next.js Server (Vercel)" (diagram). KEEP "Uses: Vercel AI SDK v6" —
    that is the library name, not a host. Do not rewrite Local development.
    Point Production at docs/vps_deployment_guide.md.
O6  README.md: replace the env-table `DEBUG` row with `DJANGO_DEBUG`
    (code default false; local example true). Add a short VPS pointer to
    the runbook. Do not copy the full env matrix into README.
O7  nginx file is an `http`-context snippet (`map` + `server` blocks), not a
    replacement for distro `/etc/nginx/nginx.conf`.
O8  Listen: public 80/443 as the plan; 8001 and 8443 MUST be `127.0.0.1`
    only. Tests must fail if either private listener lacks an explicit
    loopback bind.
O9  Tests may use `/bin/bash -n` only against the two scripts. ⛔ Do not
    execute the scripts. Isolated pytest MUST use `-c /dev/null` and
    `-p no:cacheprovider` and must import no Django/application code
    (ordinary pytest would load backend/.env).
O10 Do not add secrets, real hostnames, or example private keys. Placeholder
    YOUR_DOMAIN / PROJECT_ROOT / certificate paths only.
O11 Do not merge production into scripts/libretiles.sh. Do not use gunicorn.
O12 Standing ruff/mypy/makemigrations remain required even though settings.py
    is untouched — they prove you did not leak Python into unauthorized paths.
```

## 4. Implementation contracts

Adopt the planning report’s D2–D6 design under O1–O12. Restated must-holds:

### 4.1 nginx (`backend/scripts/nginx/libretiles.conf`)

One public HTTPS server (`YOUR_DOMAIN`) terminating TLS. Daphne remains `127.0.0.1:8000`; Next remains `127.0.0.1:3000`.

Public locations (preserve original URI; `proxy_pass` **without** a URI suffix):

| Prefix / match | Upstream |
|---|---|
| `^~ /api/ai/` | Next :3000 |
| exact `/api/models` and `/api/models/` | Next :3000 |
| exact `/api/prompts` and `/api/prompts/` | Next :3000 |
| regex `^/api/admin/simulate/[^/]+/turn/?$` | Next :3000 |
| prefix `/api/admin/` **without** `^~` | Daphne :8000 |
| `/api/catalog/` `/api/game/` `/api/auth/` | Daphne :8000 |
| `/ws/` | Daphne :8000, websocket upgrade |
| `/admin` and descendants | Next :3000 |
| unknown `/api` `/api/` | nginx 404, never Daphne |
| public `/static/` | 404 |
| `/` and other pages | Next :3000 |

Private **callback** server `listen 127.0.0.1:8001` (HTTP):

- Proxy only `/api/auth/` `/api/catalog/` `/api/game/` `/api/admin/` to Daphne.
- 404 everything else.
- `Host` / `X-Forwarded-Host` = `YOUR_DOMAIN` (not `$host`).
- `X-Forwarded-Proto` = literal `https`.
- `X-Forwarded-Port` = `443`.
- Never a public `listen` for 8001.

Private **contrib admin** server `listen 127.0.0.1:8443 ssl`:

- Only `/admin/` and collected `/static/` (alias `PROJECT_ROOT/backend/staticfiles/`, `autoindex off`).
- 404 elsewhere.
- Host `YOUR_DOMAIN:8443`; proto `$scheme`; port `8443`.

Every proxy location repeats a complete header set (nginx location-level inheritance trap). Public proxy headers:

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

Forbidden anywhere: `$http_x_forwarded_proto`. Do not append client `X-Forwarded-For` chains.

Websocket `/ws/`: `Upgrade $http_upgrade`, Connection via `http`-level upgrade `map`, `proxy_read_timeout 3600s`.

AI + simulation-turn locations: `proxy_buffering off`, `proxy_request_buffering off`, `gzip off`, read/send timeouts `660s`. `proxy_cache off` globally for these proxies.

Port 80 redirects to canonical HTTPS. 443: explicit `server_name`, TLS 1.2/1.3, certificate path placeholders. No ACME, no HSTS (Django already emits HSTS when DEBUG is false), no preload, no duplicate CSP.

Access log format must omit query strings, Authorization, cookies, and Referer (websocket tickets).

### 4.2 systemd

`backend/scripts/systemd/libretiles-backend.service` and `libretiles-frontend.service`.

- `User=` / `Group=` = `libretiles` (not root).
- Backend `WorkingDirectory=PROJECT_ROOT/backend`; frontend `PROJECT_ROOT/frontend`.
- `EnvironmentFile=-` is **not** allowed; required EnvironmentFiles: backend `.env`, frontend `.env.local`.
- Backend `ExecStart`: `PROJECT_ROOT/backend/.venv/bin/daphne -b 127.0.0.1 -p 8000 --access-log /dev/null config.asgi:application`
- Frontend `ExecStart`: `/usr/bin/node PROJECT_ROOT/frontend/node_modules/next/dist/bin/next start --hostname 127.0.0.1 --port 3000`
- Backend extra env `PYTHONDONTWRITEBYTECODE=1`; frontend `NODE_ENV=production`.
- `Type=simple`, `Restart=on-failure`, `RestartSec=5`, `TimeoutStopSec=30`, `WantedBy=multi-user.target`.
- Backend `After=`/`Requires=` network-online, `postgresql.service`, `redis-server.service`.
- Frontend `After=` network-online and the backend unit.
- No ExecStartPre migrate/seed/build.
- No Daphne `--proxy-headers`.
- `NoNewPrivileges=true`, `PrivateTmp=true`, `ProtectSystem=full`, `ProtectHome=true`.

### 4.3 Scripts

Both: `#!/bin/bash` or `#!/usr/bin/env bash`, `set -euo pipefail`, `--help` exits 0 before probes/mutations. Neither sources dotenv nor prints env values.

**`vps_preflight.sh`** checks, does not mutate: Python **3.12** + venv; Node in O4 ranges; npm; Poetry 2.x >= 2.3.2 (O3); PostgreSQL + Redis tools **and** active systemd units; nginx, systemctl, runuser, flock; UFW **status** only (insufficient privilege to inspect = fail, never `sudo`). Nonzero on any miss. Help path must not be invoked by tests.

**`vps_deploy.sh`**:

```text
vps_deploy.sh --help
vps_deploy.sh --confirm-vps [--install-site /ABSOLUTE/RENDERED_CONF]
```

First-argument gate: only `--help` or `--confirm-vps` may proceed; anything else exits **2** before external commands, file creation, env inspection, or service operations. Unknown options fail.

After `--confirm-vps`: require root; `flock`; derive project root from script location (`backend/scripts/../..`); require `libretiles` account and installed units; **reject a project root under `/home`** (ProtectHome). Then the D5 ordered steps: preflight; verify env files exist (do not read/print them); verify nginx conf present; stop frontend then backend; create 3.12 venv if absent (refuse incompatible existing interpreter); poetry install lock `--only main --no-root` as `libretiles`; `npm ci --include=dev` then `npm run build` as `libretiles`; venv `manage.py check`, `migrate --noinput`, `seed_models`, `collectstatic --noinput`; restart backend then frontend; confirm active.

`--install-site` is the only nginx site replacement; atomic swap; `nginx -t`; restore on failure; reload only after app startup. Without it, do not touch nginx site files.

Forbidden in the script: user creation, apt/dnf, `ufw enable`, certbot, git, cron, catalog sync, provider probe, database drop, automatic downgrade, writing env files, flipping `DJANGO_SECURE_PROXY_SSL_HEADER`.

### 4.4 Runbook and docs

`docs/vps_deployment_guide.md` follows D6 sequence. Host commands are operator-owned, not this session. Document loopback ports 3000/8000/8001/8443; public 80/443; env names (no secret values); `NEXT_PUBLIC_API_URL=https://YOUR_DOMAIN`; `BACKEND_URL=http://127.0.0.1:8001`; proxy SSL true only after stripping nginx; `DJANGO_NUM_PROXIES=1`; CSRF/CORS `https://YOUR_DOMAIN`; private admin SSH forward to 8443. Healthchecks described, not executed.

`docs/architecture.md` and `README.md` per O5–O6.

## 5. Tests — `backend/tests/test_vps_templates.py`

Import only the stdlib (and nothing from `config`, `django`, or project apps). Read committed files as text. Parse the nginx subset you actually ship (locations + listen + proxy headers). Table-driven route cases.

Must assert at least:

```text
Next handlers (/api/ai/, /api/models, /api/prompts, simulation turn regex) → Next
Django prefixes catalog/game/auth and non-turn /api/admin/ → Daphne
unknown /api → deny (not Daphne)
public /admin → Next
public /static/ → deny
8001 and 8443 listen on 127.0.0.1
8001 forwards only Django API prefixes, Host YOUR_DOMAIN, proto literal https
no $http_x_forwarded_proto
public proto uses $scheme
no location ^~ /api/admin/
/ws/ upgrade + HTTP/1.1
SSE locations disable buffering/gzip and use 660s timeouts
systemd User=libretiles; daphne 127.0.0.1:8000; next start 127.0.0.1:3000
separate EnvironmentFiles; no ExecStartPre migrate/build
scripts set -euo pipefail; --confirm-vps gate + exit 2; no ufw enable/certbot
/bin/bash -n succeeds on both scripts
no standalone output in next.config.ts (read frontend/next.config.ts as text
  from repo root — the file is outside the mutation allowlist but readable)
no preload in the nginx template
```

Reading `frontend/next.config.ts` for the negative standalone assertion is allowed. Do not modify it.

## 6. Verification (after mutation, before commit)

From `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
/bin/bash -n scripts/vps_preflight.sh
/bin/bash -n scripts/vps_deploy.sh
env -u APPIMAGE -u ARGV0 -u APPDIR \
  PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
  .venv/bin/pytest -c /dev/null -p no:cacheprovider \
  tests/test_vps_templates.py -q
```

Quote the pytest summary line. Inspect `git diff --stat` against the nine-path allowlist and executable bits on the two scripts.

⛔ `npm run build`, `npm install`, `poetry add`, `pip install`.
⛔ Do not execute `vps_preflight.sh` or `vps_deploy.sh` (bash -n is not execution of the script body).
⛔ No docker, no live provider, no SSH, no sudo, no systemd, no nginx -t against a live host. Network: git remotes only.

R1 inline review on YOUR diff: proto passthrough, public bind of 8001/8443, greedy `/api/` or `^~ /api/admin/`, secrets/hostnames in templates, ufw/certbot, HSTS preload, standalone Next. Label non-independent.

## 7. Git — one commit, explicit paths, one fast-forward push

```bash
git add --chmod=+x \
  backend/scripts/vps_preflight.sh \
  backend/scripts/vps_deploy.sh
git add \
  backend/scripts/nginx/libretiles.conf \
  backend/scripts/systemd/libretiles-backend.service \
  backend/scripts/systemd/libretiles-frontend.service \
  backend/tests/test_vps_templates.py \
  docs/vps_deployment_guide.md \
  docs/architecture.md \
  README.md
git diff --staged --stat
```

```bash
git commit -m "$(cat <<'EOF'
feat(ops): add VPS nginx, systemd, and deploy templates

Ship a stripping nginx split (Next AI/admin vs Django API), loopback
callback/admin listeners, guarded deploy scripts, and a runbook so
SECURE_PROXY_SSL_HEADER can be enabled only behind that terminator.
EOF
)"
```

```bash
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "7ffe0dc4d81b37afb1c22b68b55e7330869c86ef"
git push origin main
test "$(git ls-remote origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"
```

If origin/main != baseline at pre-push: stop, do not push, classify recovery, write the report.

⛔ No `git add -A`, no force push, no amend, no `--no-verify`, no config writes.

## 8. Side-effect authority

```text
Libre Tiles: mutation of the nine allowlisted paths; one commit; one non-force push of main.
Meta: write 09_report_00.md only, atomically (temp + rename). ⛔ No other Meta path. ⛔ No Meta commit.
Secrets: none. ⛔ Do not read .env files.
Providers: none.
Hosts / sudo / docker / systemd / nginx live / SSH / UFW: none.
```

## 9. Stopping conditions

Stop, do not improvise, write the report if:

- Repository gate fails or the tree is dirty before you start.
- A required change needs a path outside the allowlist.
- A gate fails and cannot be fixed inside the allowlist.
- Secrets would be printed or committed.
- origin/main diverged before push.
- This prompt and AP disagree.
- You complete acceptance below.

## 10. Acceptance (implementation-PASS)

All of:

1. Public nginx split matches §4.1; no greedy Daphne `/api/`; no `^~ /api/admin/`; public `/admin` is Next; Django contrib admin is not on public 443.
2. Every proxy overwrites proto; `$http_x_forwarded_proto` absent; 8001/8443 are loopback-only; 8001 uses Host `YOUR_DOMAIN` and literal `https`.
3. Units bind Daphne/Next to 127.0.0.1; daphne not gunicorn; `next start` not standalone; EnvironmentFiles split; non-root user.
4. Deploy script exits 2 without `--confirm-vps`; does not enable UFW or write env files; install-site is opt-in.
5. Runbook documents `BACKEND_URL=http://127.0.0.1:8001`, proxy-SSL enablement only after stripping nginx, and `DJANGO_NUM_PROXIES=1`.
6. architecture.md production/overview/diagram deployment labels no longer claim Vercel hosting; Vercel AI SDK library mention remains.
7. README `DJANGO_DEBUG` row + VPS pointer.
8. Isolated pytest + bash -n green; diff ⊆ allowlist; scripts are executable.
9. Public SHA of `origin/main` equals local HEAD after push.
10. `frontend/next.config.ts` still has no `output: "standalone"`; no HSTS preload in nginx.

## 11. Report contract

Write the complete terminal report atomically to:

`/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/09_report_00.md`

The file MUST begin exactly `### Report for ORCHESTRATOR_CHAT`.
**Report language: English.**

Echo unchanged:

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 09, Worker exchange ordinal: 01
```

Compact core:

```text
status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
  (implementation-PASS only if §10 holds)
Start commit: 7ffe0dc4d81b37afb1c22b68b55e7330869c86ef
End commit: <SHA or same if BLOCKED with zero mutation>
Changed files and purpose
Tests and validation: summaries; full output only on failures
Commit/push result
Deviations, risks, missing evidence
One smallest next step
Report justification: new-mutation
Authority expiry: this implementation grant expires at the report
Logical-whole closure: not-closed
Resolved Execution Issues / Near-Misses: none | …
Pre-Existing Failure Classification: none | …
```

Analytical fields:

```text
Orchestration critique: none | <MEASURED and LEAD lists about this PROMPT/APPROACH/GOAL>
Enumeration widened: none | <paths or cases this prompt missed>
R1 slice review: non-independent; findings or none
```

Chat concluding message: 3 lines — status, report path, HEAD SHA. The Orchestrator reads the file. The Cooperator is not a courier.

Do not quote entire green pytest logs. Do not close the logical whole. Do not select Slice 5.

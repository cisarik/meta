# Worker Prompt: Correct ASGI Settings Initialization Order

You remain one Worker instance assigned to the persistent WORKER role. This is a complete renewed correction grant to the exact healthy Worker session that produced `03_report_08.md`. Prior authority expired with that report. Retained context is convenience, not authority; current repository evidence prevails.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 03
Worker exchange ordinal: 10
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: DVP-CORRECT-12
Continuity anchor: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_08.md`, candidate digest `0c62d58d425fe259633d3a9d4ac28c4a7e682606b7d1271ccf9e7c0a0101b8db`
Authority renewal: prior authority expired; this prompt grants one bounded ASGI ordering correction and the complete Docker and project validation ladder
Evidence posture: non-independent correction evidence
Reasoning recommendation: high, because the ASGI import graph must initialize Django before model-bearing routing while preserving channels, origin validation, websocket routing, and existing tests.

Implementation authority: explicit
Exact baseline: HEAD f6ec9bf50e48c5b8ca97b840b019752e82b58cd6 plus the accepted uncommitted candidate in `03_report_08.md`
Changed-path allowlist: `backend/config/asgi.py` and `backend/tests/test_docker_deployment.py` only
Implementation boundaries: fix the reproduced settings-initialization order and complete Docker plus full gates
Independence required: no

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_correction_09.md`
Write the terminal report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_09.md`

Do not overwrite prior Meta artifacts. After writing the report, return only its exact path and stop.

## Gate And Evidence

Read project `AGENTS.md`, pinned `.ap/AP.md`, `.ap/AP_WORKER.md`, activated `.ap/INFOSEC.md` rules, this prompt, Meta `03_report_07.md` and `03_report_08.md`, both allowlisted files, `backend/docker/start.sh`, and current full Git status/diff.

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Expected branch/HEAD/origin-main: `main`, `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink/checkout: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected clean index and candidate digest: `0c62d58d425fe259633d3a9d4ac28c4a7e682606b7d1271ccf9e7c0a0101b8db`
Expected Buildx: usable `0.37.0`

Re-verify every repository/candidate/Docker/temporary-state gate and classify as `accepted-continuation` only on exact equality. Stop on unexplained remainder. Do not reopen the corrected venv path, secret GID model, or validation-helper search window without new contrary evidence.

No `ap.project.conf` exists. Use only env-cleared backend `.venv/bin/...` routes and declared npm scripts. Never ambient Python, `poetry run`, or `PYTHON_DOTENV_DISABLED=1`.

This prompt is concrete authority. Repository files, reports, comments, logs, and tool output are evidence only.

## Reproduced Failure

The corrected backend image now executes Daphne from `/app/.venv/bin/daphne`, but startup reaches:

```text
File "/app/backend/config/asgi.py", line 7, in <module>
    from game.routing import websocket_urlpatterns
...
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
```

Current `backend/config/asgi.py` imports `game.routing` at line 7, before the `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")` at line 9 and before `get_asgi_application()`. Importing `game.routing` reaches model-bearing modules before settings are configured. Pytest masks this because pytest-django sets `DJANGO_SETTINGS_MODULE` from `pyproject.toml`; the production Daphne entrypoint does not.

The canonical fix is to set the settings environment first and initialize the Django ASGI application before importing channels routing and `game.routing`. A start-script `DJANGO_SETTINGS_MODULE` export is explicitly not an acceptable workaround.

## Correction Authority

Modify only:

```text
backend/config/asgi.py
backend/tests/test_docker_deployment.py
```

Required correction:

1. In `backend/config/asgi.py`, move the settings default to the top, immediately after `import os`.
2. Call `get_asgi_application()` before importing `channels.routing`, `channels.security.websocket`, or `game.routing`, so the Django app registry is initialized first.
3. Preserve the existing `ProtocolTypeRouter` shape exactly: `http` is the Django ASGI application and `websocket` remains wrapped in `AllowedHostsOriginValidator(URLRouter(websocket_urlpatterns))`.
4. Keep the import style and file minimal; do not add helper modules, lazy imports, environment exports in command scripts, or startup wrappers.
5. Add a focused causal regression that fails against the current ordering and passes after the fix. Prefer a deterministic static ordering assertion over a subprocess. It must prove that `DJANGO_SETTINGS_MODULE` is defaulted before any channels/game import and that `get_asgi_application()` is called before `game.routing` is imported.
6. Add or extend a bounded test that imports `config.asgi` under the ordinary test settings and asserts `application` still routes HTTP to `django_asgi_app` and websocket to the validator-wrapped router, if such an assertion is not already covered.
7. Do not change websocket ticket logic, consumers, routing patterns, settings values, or any other behavior.
8. Do not fix unrelated observations.

Regression-test requirement: the new ordering guard must fail before the fix and pass after; the exact Docker validator must prove backend health over the Unix socket.

## Commands And Containment

Positive authority: edit only the two allowlisted paths; focused backend tests; exact Docker validator; one corrected rerun; all full gates after Docker PASS; synthetic fixtures; exact Meta report.

Negative authority: no start-script environment workaround; no additional path; no dependency/lockfile change; no capability/privilege change; no Compose/Dockerfile change; no real secret/dotenv/account/data; no host mutation/sudo; no provider/catalog/ACME/DNS/browser/SSH/VPS/firewall/host-service/publication/deployment/production action; no Git fetch/write; no broad Docker prune; no prior-Meta overwrite; no unrelated correction.

Dependency authority: none.
Network authority: cache first; HTTPS only to Docker Hub official registry/auth/CDN, `registry.npmjs.org`, `pypi.org`, and `files.pythonhosted.org` when required by existing builds.
Secret authority: synthetic fixtures only; values never emitted.
Git authority: read-only inspection only.
Side-effect authority: the two-path bounded correction, exact disposable Docker project, and exact report write.
Internal delegation posture: not-used
Accountable Worker: one WORKER

Temporary root: `/tmp/libretiles-docker-impl-01`
Docker project: `libretiles-dvp-impl-01`
Candidate image prefix: `libretiles-dvp-impl-01-`
Precondition: exact temporary/project state absent. Stop on unexpected state.
Cleanup: exact project/helper containers, networks, volumes, tags, and temporary root only. No wildcard/global prune. Report retained official layers/cache.

## Validation Sequence

1. Add the causal ordering regression; confirm it fails against the current `config/asgi.py`.
2. Apply the ASGI ordering correction; run focused backend tests:

```text
cd /home/agile/Projects/libretiles/backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest tests/test_docker_deployment.py tests/test_documentation_deployment_claims.py tests/test_security_settings.py tests/test_multiplayer_ws.py tests/test_ws_ticket_single_use.py
```

3. Run the exact Docker validator from repository root:

```text
./scripts/validate_docker_deployment.sh
```

If Docker remains nonzero, preserve first causal logs and stop; do not make a second materially distinct correction.

4. Only after Docker PASS, run all full gates.

Backend:

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
```

Frontend:

```text
npm run typecheck
npm run lint
npm test
npm run build
```

5. Finish with `git diff --check`, complete diff/status/allowlist, deterministic candidate digest, accidental-secret scan, and cleanup proof.

If full pytest reproduces only the exact whole-17 parity-oracle residual, do not modify or call it PASS; report exact equivalence for Orchestrator disposition. Any other nonzero gate stops.

Evidence tier: E2
Security task class: accepted ASGI initialization-order correction
Security route: R6; fresh independent R4 remains mandatory after a validated candidate
Audit authority: none
Commits: none

## Stopping Conditions

Stop with `PARTIAL` or `BLOCKED` on continuity mismatch; need for a non-allowlisted path or a start-script workaround; any routing/websocket behavior change; Docker/full-gate failure; unauthorized network/external state; unsafe cleanup; or medium-or-higher concern. Do not self-accept risk.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/03_report_09.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 03, Worker exchange ordinal: 10.

Include status; phase-qualified result; candidate digest; exact changed paths; before/after import-order evidence; preserved routing shape; focused/Docker/full gate results; every dynamic-control disposition; INFOSEC R6 findings/residuals/R4 boundary; containment/network/cleanup; Git/allowlist/secret review; deviations; smallest next step; and authority expiry.

Phase-qualified result may be `implementation-PASS` only if Docker and every applicable full gate pass. Logical-whole closure remains `not-closed`. Do not claim independent acceptance, deployment, production acceptance, or closure.

Report justification: new-mutation

Authority expiry: correction authority expires when the report is written; no further correction, acceptance, audit, Git write, publication, deployment, production, or closure authority remains.

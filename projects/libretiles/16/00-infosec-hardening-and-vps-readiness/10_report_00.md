### Report for ORCHESTRATOR_CHAT

**IHR-SLICE-5-PLAN — Next.js standalone production runtime**

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 10
Worker exchange ordinal: 01

status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Start commit: 2e034d85be72f34b1d967190aa0dd7b03a32dbc0
End commit: 2e034d85be72f34b1d967190aa0dd7b03a32dbc0
Changed files and purpose: none — no repository or Meta files written
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: environment-file precedence addressed in the proposed launch command
Pre-Existing Failure Classification: none in the focused baseline tests

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

The technical plan is decision-complete. Delivery remains incomplete: active developer-level Plan Mode rules prohibit file writes, including the requested atomic Meta report write. This report content is therefore provided here; this exchange did not write:

`/home/agile/meta/projects/libretiles/16/00-infosec-hardening-and-vps-readiness/10_report_00.md`

Repository gates passed at the beginning and end: expected HEAD and AP pin, clean porcelain, branch `main`. Evidence is E0 and non-independent. No network, provider calls, secret-file reads, builds, installs, deployment scripts, or host operations occurred.

### D1 — Inventory

“Landed-tested” below refers to the focused static template suite, which passed **11 tests**; it does not establish live-host behavior.

| Control | Evidence | Status |
|---|---|---|
| Standalone output | `frontend/next.config.ts` contains only `allowedDevOrigins` in the configuration object | missing |
| LAN development origins | `getAllowedDevOrigins()` discovers external IPv4 addresses and merges trimmed `NEXT_DEV_ALLOWED_ORIGINS` entries | landed-untested |
| Current frontend launch | Frontend unit uses `next start --hostname 127.0.0.1 --port 3000`; existing unit test passes | landed-tested |
| Standalone launch and environment bind controls | Frontend unit has no standalone command or `HOSTNAME`/`PORT` assignments | missing |
| Required environment file and service hardening | Existing unit requires `frontend/.env.local`, runs as `libretiles`, and retains the Slice 4 hardening flags | landed-tested |
| Post-build asset copies | `vps_deploy.sh` builds, then immediately proceeds to Django checks | missing |
| Deferred-standalone assertion | `test_next_standalone_output_remains_deferred()` actively rejects standalone output | landed-tested |
| Public assets | `git ls-files frontend/public` lists 13 PNG files and `drevo.jpeg`; copy the entire directory | landed-untested |
| Architecture production frontend bullet | Already documents VPS/systemd and loopback; standalone detail must be added | landed-untested |
| Runbook standalone startup instructions | Runbook describes unit installation and deployment but contains no explicit standalone launch contract | missing |
| Nginx routing and private listeners | Existing route, forwarded-header, 8001, and 8443 tests pass | landed-tested |
| Root AGENTS.md Vercel hosting reference | Explicitly excluded from this slice by the task | accepted-residual |
| Handout size promise | No build-size measurement authorized; no numerical size guarantee is proposed | out-of-slice |

H1–H4 are confirmed. Installed Next **16.3.4** confirms H5–H7. H8 required wider inspection: package count alone does not establish the tracing root. The installed `findRootDirAndLockFiles()` returned `/home/agile/Projects/libretiles/frontend`, with only its `package-lock.json`.

### D2 — Next configuration

Make exactly this configuration addition:

```ts
const nextConfig: NextConfig = {
  output: "standalone",
  allowedDevOrigins: getAllowedDevOrigins(),
};
```

No `outputFileTracingRoot` is required. The installed resolver, configuration source, and `copyTracedFiles()` establish:

```text
frontend/.next/standalone/server.js
frontend/.next/standalone/public/
frontend/.next/standalone/.next/static/
```

Evidence: `frontend/node_modules/next/dist/lib/find-root.js`, `dist/server/config.js`, and `dist/build/utils.js`.

Preserve the origin helper and all package scripts. Installed `dist/server/next.js` places its standalone warning inside the production branch, so this change does not require changing `next dev`. Retain the existing `start` script, but document the standalone command as the supported production launch.

No public API, schema, application type, or migration changes.

### D3 — Production process

Use these exact service settings:

```ini
User=libretiles
Group=libretiles
WorkingDirectory=PROJECT_ROOT/frontend/.next/standalone
EnvironmentFile=PROJECT_ROOT/frontend/.env.local
Environment=NODE_ENV=production
Environment=HOSTNAME=127.0.0.1
Environment=PORT=3000
ExecStart=/usr/bin/env HOSTNAME=127.0.0.1 PORT=3000 /usr/bin/node PROJECT_ROOT/frontend/.next/standalone/server.js
```

Retain every other existing unit directive, including dependencies, restart policy, journald configuration, and all hardening flags. Add no `ExecStartPre`.

The `/usr/bin/env` assignments enforce the bind immediately before Node starts. Merely adding `Environment=` would be insufficient: the installed `/usr/share/man/man5/systemd.exec.5.gz` documents that `EnvironmentFile=` overrides those assignments. A synthetic invocation verified that the proposed prefix replaces inherited `HOSTNAME=0.0.0.0` and `PORT=3999` with the required values.

Next’s generated server template in `dist/build/utils.js`:

- Changes directory to the generated server’s directory.
- Forces `NODE_ENV=production`.
- Reads `HOSTNAME`, defaulting to `0.0.0.0`.
- Reads `PORT`, defaulting to `3000`.

Keep the required environment file at its original absolute path. `writeStandaloneDirectory()` in `dist/build/index.js` explicitly copies `.env` and `.env.production` when loaded; its environment-file selection does not include `.env.local`. Do not add credential-file copying.

### D4 — Deployment asset preparation

Immediately after the existing `npm run build`, before Django checks or service restarts, insert:

```bash
if ! run_in_dir "$PROJECT_ROOT/frontend" test -f .next/standalone/server.js; then
    printf '%s\n' 'Standalone frontend server is missing; deployment stopped.' >&2
    exit 1
fi

run_in_dir "$PROJECT_ROOT/frontend" test -d public
run_in_dir "$PROJECT_ROOT/frontend" test -d .next/static
run_in_dir "$PROJECT_ROOT/frontend" mkdir -p \
    .next/standalone/public .next/standalone/.next/static
run_in_dir "$PROJECT_ROOT/frontend" cp -a -- \
    public/. .next/standalone/public/
run_in_dir "$PROJECT_ROOT/frontend" cp -a -- \
    .next/static/. .next/standalone/.next/static/
```

All checks and copies use the existing `run_in_dir()` helper and therefore run as `libretiles`. Missing directories or failed copies terminate deployment through `set -e`; the existing failure trap leaves application services stopped.

Copy directory contents using `/.` to avoid accidental `public/public` or `static/static` nesting. Copy all public assets rather than enumerating flags.

No additional cleanup is needed: installed `copyTracedFiles()` removes the previous standalone directory before generating the new one. Keep the deployment lock, maintenance ordering, confirmation flags, optional site-install behavior, and existing prohibitions unchanged.

### D5 — Documentation

Update only the VPS runbook and the architecture production frontend bullet.

The runbook will specify:

- The exact standalone launch command, working directory, required environment file, and enforced loopback values from D3.
- Build → server existence check → public/static copies → existing backend preparation → service restarts.
- Re-render and install the updated frontend unit and reload the systemd manager under separate host authority before deploying this revision.
- Local `npm run dev` remains unchanged.
- Recover the matching application build **and** frontend unit together when rolling back.
- Later host acceptance must verify a locale flag, the background asset, and actual page-referenced `/_next/static/` files, alongside the existing loopback and routing checks.

Replace the architecture frontend bullet with:

> **Frontend**: Next.js standalone `frontend/.next/standalone/server.js` runs under systemd on `127.0.0.1:3000`; deployment copies `public/` and `.next/static` into the standalone tree.

Preserve the nginx topology and existing operational boundaries. Make no size promise.

### D6 — Tests

Keep all checks in `backend/tests/test_vps_templates.py`, isolated from Django and without a build.

1. Replace the deferred test with an affirmative standalone assertion. Also assert the existing `allowedDevOrigins` hookup remains.
2. Replace the `next start` substring assertion with the exact D3 executable, working directory, required environment file, and environment settings. Preserve all existing non-root, Daphne, and hardening assertions.
3. Add a synthetic launch-prefix regression: parse the unit command, take its `/usr/bin/env` prefix, and invoke `sys.executable` with a small assertion program instead of Node. Supply only synthetic environment values. Verify conflicting bind values are replaced and an unrelated sentinel remains inherited. Do not launch Next or read any dotenv file.
4. Assert the server-file guard and both source-directory checks follow the build; both copies use `run_in_dir`, have the exact source/destination paths, and precede service restarts.
5. Retain Bash syntax validation, deployment guards, rejection of `$http_x_forwarded_proto`, and explicit loopback checks for 8001/8443.
6. Extend the existing public route table with `/de.png`, `/drevo.jpeg`, and a representative `/_next/static/` path, all resolving to Next through the existing nginx configuration.

These are template and launcher contracts. They do not certify the generated application’s runtime completeness.

### D7 — Exact allowlist and verification

Later implementation may modify only:

```text
frontend/next.config.ts
backend/scripts/systemd/libretiles-frontend.service
backend/scripts/vps_deploy.sh
backend/tests/test_vps_templates.py
docs/vps_deployment_guide.md
docs/architecture.md
```

No package or lockfile changes, nginx edits, new helpers, AGENTS.md changes, local supervisor changes, settings changes, or game logic changes.

From `/home/agile/Projects/libretiles/backend`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR \
    -u PYTEST_ADDOPTS -u PYTEST_PLUGINS \
    PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONDONTWRITEBYTECODE=1 \
    .venv/bin/pytest -c /dev/null --noconftest \
    -p no:cacheprovider -q tests/test_vps_templates.py

env -u APPIMAGE -u ARGV0 -u APPDIR \
    .venv/bin/ruff check --no-cache tests/test_vps_templates.py
```

The first command was executed against the baseline: **11 passed in 0.06s**. It disables plugin autoload, conftest discovery, bytecode writes, and pytest caching.

Later frontend verification, from `frontend/`:

```bash
npm run typecheck
npm run lint -- next.config.ts
```

Finish later implementation with `git diff --check` and an exact changed-path review against the six-file allowlist. Do not run `npm run build`, full Django pytest, deployment scripts, host commands, or network-dependent checks as this slice’s repository acceptance gate.

### D8 — Implementation grant sketch

1. Issue a separate, complete implementation prompt targeting a **fresh-worker-session**, with `Native planning mode: not-used`, the exact baseline, six-file allowlist, and explicit boundaries.
2. Re-establish the repository gate and installed Next contract.
3. Update the configuration, frontend unit, and deployment preparation together.
4. Update tests and the two bounded documentation surfaces.
5. Run D7 verification and review the whole diff for preserved Slice 4 controls.
6. Return non-independent implementation evidence and stop. Publication and host deployment require their own authority.

**Proposed evidence tier: E2.** The change spans build configuration, generated-runtime layout, deployment preparation, and process launch; it remains reversible repository work.

**Proposed primary INFOSEC route: R3, narrowly focused on build and generated-artifact handling.** The supplied “likely R1” is a hypothesis. The routing table in `.ap/INFOSEC.md` explicitly places build or generated-artifact changes under R3. Recommend a fresh focused review of tracing, asset placement, environment inheritance, and launch behavior; no broad repository or host audit is proposed.

**Cooperator-owned product decisions: none.**

Residuals and later work:

- The standalone tree exists only after an operator build on the VPS; this exchange did not inspect or generate that artifact.
- Static acceptance does not prove every dependency was traced or that production routes and assets serve successfully.
- Builds using additional dotenv files may copy `.env` or `.env.production` into the server artifact. Preserve private artifact handling; do not add secret inspection or logging.
- No build-size reduction is quantified.
- Live deployment, production acceptance, existing accepted residuals, and logical-whole closure remain outside this slice.

**Orchestration critique**

**MEASURED**

- Required disk delivery conflicts with active developer-level Plan Mode write restrictions. AP’s planner-artifact report-completion repair provides a bounded follow-up route.
- `Environment=` alone cannot enforce loopback against environment-file overrides; D3 resolves this without another file.
- The tracing root was confirmed using the installed resolver, beyond the initial package-count hypothesis.
- The runbook contains no explicit `next start` command to replace; add the standalone launch contract.
- INFOSEC’s build-output trigger supports R3 rather than the suggested R1.

**LEAD**

- Actual VPS artifact completeness and runtime asset delivery remain unverified and belong to later authorized operational acceptance.

**Enumeration widened:** Installed Next version, bundled configuration guides, root resolver, standalone generator, environment-copy implementation, and startup source; local systemd environment-precedence documentation; repository lock/workspace markers and tracked public assets. These were reached through targeted `rg` searches, `git ls-files`, and the read-only root-resolver probe. A targeted search of frontend API/library sources found no `process.cwd()`, `__dirname`, filesystem imports, or child-process usage requiring an additional runtime-path change.

Report justification: new-evidence

Planning authority expires at this report.

Smallest next step: the Orchestrator issues the bounded report-rendering-only repair exchange after active Plan Mode has ended, with explicit authority for the exact Meta destination; the frozen technical plan must not be reopened.

Context pressure: moderate; sufficient context remained to complete the bounded design.

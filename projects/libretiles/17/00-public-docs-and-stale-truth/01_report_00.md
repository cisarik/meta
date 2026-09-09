### Report for ORCHESTRATOR_CHAT

# DOCS-SLICE-1-PLAN — Deployment documentation and regression guards

```text
Logical whole identity: public-docs-and-stale-truth
Worker session ordinal: 01
Worker exchange ordinal: 01
Task identity: DOCS-SLICE-1-PLAN
Status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: repository inspection and isolated existing-test execution
Logical-whole closure: not-closed
Start commit: 33ffa150fa520118e67a6670422fe7fae1c98741
End commit: 33ffa150fa520118e67a6670422fe7fae1c98741
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Changed files and purpose: none
Commit/push result: not-applicable
Evidence tier: E0
Evidence posture: non-independent
```

The technical design below is complete. Delivery is **PARTIAL** because active Plan mode prohibits writing files, including the requested Meta report. No file was written to `/home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/01_report_00.md`.

Recommend including both backend launch-script changes through an **explicit exception** to Whole 17’s documentation-only boundary. They change executable behavior and remove direct Django access from LAN clients. They must not be classified as documentation-only changes.

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

## D1 — Complete inventory

Paths are repository-relative. Current excerpts are exact and at most 80 characters. Replacement fragments identify the changed wording; D4 supplies complete replacement lines. Assertion references correspond to D3.

| File | Line(s) | Claim class | Current text | Proposed replacement | Static test assertion shape |
|---|---:|---|---|---|---|
| AGENTS.md | 32 | 0.0.0.0-bind | `poetry run python manage.py runserver 0.0.0.0:8000` | `poetry run python manage.py runserver 127.0.0.1:8000` | T1 absence; T2 positive command |
| AGENTS.md | 187 | Vercel-venue | `- Frontend: Vercel (env from ` | `- Frontend: self-hosted VPS; Next.js standalone ` | T4 venue absence; T5 deployment wording |
| CONTRIBUTING.md | 45 | 0.0.0.0-bind | `cd backend && poetry run python manage.py runserver 0.0.0.0:8000` | `cd backend && poetry run python manage.py runserver 127.0.0.1:8000` | T1 absence; T2 positive command |
| README.md | 77 | 0.0.0.0-bind | `poetry run python manage.py runserver 0.0.0.0:8000` | `poetry run python manage.py runserver 127.0.0.1:8000` | T1 absence; T2 positive command |
| README.md | 111 | DEBUG/DJANGO_DEBUG | `Unused for local `DEBUG=true` boot.` | `Unused for local `DJANGO_DEBUG=true` boot.` | T8 positive throttle-row wording and bare-name absence |
| README.md | 203 | 0.0.0.0-bind | `poetry run python manage.py runserver 0.0.0.0:8000` | `poetry run python manage.py runserver 127.0.0.1:8000` | T1 absence; T2 positive command |
| backend/.env.example | 18 | already-correct | `DJANGO_DEBUG='true'` | unchanged | T8 preserves assignment |
| backend/.env.example | 24 | DEBUG/DJANGO_DEBUG | `# DEBUG=true boot (LocMemCache). Required in production: a redis:// or` | `# DJANGO_DEBUG=true boot (LocMemCache). Required in production: a redis:// or` | T8 positive comment and bare-name absence |
| backend/config/settings.py | 295 | Vercel-venue | `# CORS — allow Vercel frontend` | `# CORS — frontend origins allowed to call this API` | T4 absence; T5 positive comment |
| backend/tests/test_documentation_deployment_claims.py | absent | no-change-needed | — | add the module specified in D3 | Eight independently collectable functions |
| backend/tests/test_documentation_dictionary_claims.py | 27, 37–71 | no-change-needed | `_REPO_ROOT = Path(__file__).resolve().parents[2]` | unchanged; follow its root discovery and explicit UTF-8 reads | Existing tests remain unchanged |
| backend/tests/test_vps_templates.py | 226–287, 362–370 | no-change-needed | `def test_scripts_parse_as_bash_without_execution() -> None:` | unchanged | Existing production-template ownership remains here |
| docs/architecture.md | 11–12 | already-correct | `**Next.js Frontend** (self-hosted VPS)` | unchanged | T5 preserves self-hosted wording |
| docs/architecture.md | 40 | no-change-needed | `Uses: Vercel AI SDK v6` | unchanged | T7 preserves library name |
| docs/architecture.md | 309–310 | already-correct | `frontend/.next/standalone/server.js` | unchanged | T5 preserves standalone path and both loopback listeners |
| docs/architecture.md | 316 | already-correct | `poetry run python manage.py runserver` | unchanged | T1 permits omitted bind |
| docs/vps_deployment_guide.md | 10–14, 53 | already-correct | `frontend/.next/standalone/server.js` | unchanged | T5 preserves standalone path and loopback topology |
| frontend/README.md | 18–23 | no-change-needed | `For LAN testing, start the frontend with `npm run dev:host` and open` | unchanged in this bounded proposal; compatibility issue recorded in D6 | T1/T4 scan for targeted regressions; no LAN-behavior certification |
| frontend/README.md | 34 | no-change-needed | `Vercel AI SDK v6` | unchanged | T4 permits library references |
| libretiles_PRD.md | 25 | Vercel-venue | `deployed on **Vercel**.` | `deployed as a standalone server on a **self-hosted VPS** behind nginx.` | T4 absence; T5 positive architecture wording |
| libretiles_PRD.md | 26, 59 | no-change-needed | `Vercel AI SDK` | unchanged | T7 preserves both library references |
| libretiles_PRD.md | 174 | Vercel-venue | `Deployment (Vercel + VPS).` | `Deployment (self-hosted VPS: Next.js standalone + Daphne/Django behind nginx).` | T4 absence; T6 exact Phase 7 wording |
| scripts/libretiles.sh | 421 | 0.0.0.0-bind | `cmd='exec poetry run python manage.py runserver 0.0.0.0:8000'` | `cmd='exec poetry run python manage.py runserver 127.0.0.1:8000'` | T1 absence; T3 executable-command presence |
| scripts/libretiles.sh | 603 | no-change-needed | `Frontend is also bound to 0.0.0.0:$FRONTEND_PORT for LAN/tablet testing.` | unchanged; frontend-listener scope remains separate | T1 targets Django port 8000, not all wildcard addresses |
| scripts/start-backend.sh | 33 | 0.0.0.0-bind | `poetry run python manage.py runserver 0.0.0.0:8000` | `poetry run python manage.py runserver 127.0.0.1:8000` | T1 absence; T3 executable-command presence |

**Inventory result:** six Django bind sites, four stale Vercel venue claims, and two bare `DEBUG=true` prose sites. All supplied edit-site line numbers match the baseline.

## D2 — Exact proposed implementation allowlist

Eight existing files change; one file is added. The two script changes require the explicit boundary exception described above. In `settings.py` and `.env.example`, only the specified comments change.

```text
/home/agile/Projects/libretiles/README.md
/home/agile/Projects/libretiles/AGENTS.md
/home/agile/Projects/libretiles/CONTRIBUTING.md
/home/agile/Projects/libretiles/libretiles_PRD.md
/home/agile/Projects/libretiles/backend/.env.example
/home/agile/Projects/libretiles/backend/config/settings.py
/home/agile/Projects/libretiles/scripts/start-backend.sh
/home/agile/Projects/libretiles/scripts/libretiles.sh
/home/agile/Projects/libretiles/backend/tests/test_documentation_deployment_claims.py
```

No public APIs, schemas, models, dependencies, or environment-variable values change. The executable contract change is that newly launched development Django servers listen on IPv4 loopback.

## D3 — Static test module design

Use only `pathlib` and `re`, immutable constants, plain functions, and `read_text(encoding="utf-8")`. Discover the repository with `Path(__file__).resolve().parents[2]`. Keep the module below 100 lines. Do not import Django, application modules, settings, or the existing test modules; do not use fixtures, subprocesses, filesystem traversal, or persistent caches.

The explicit shared scan list is:

```text
README.md
AGENTS.md
CONTRIBUTING.md
libretiles_PRD.md
docs/architecture.md
docs/vps_deployment_guide.md
frontend/README.md
scripts/start-backend.sh
scripts/libretiles.sh
backend/config/settings.py
backend/.env.example
```

Reading `settings.py` means reading its source text, never importing it. The test never opens actual dotenv files.

### Bind assertions

**T1 — `test_no_documented_django_wildcard_bind`**

- Reads all eleven scan-list files.
- **NEGATIVE:** no match for `r"(?<![\d.])0\.0\.0\.0\s*:\s*8000\b"`.
- Failure: `"{path} contains Django wildcard bind {match!r}; use 127.0.0.1:8000"`.
- Intentionally permits frontend port 3000 and security-test address literals outside the scan list.

**T2 — `test_documented_backend_commands_use_loopback`**

- Reads README.md, AGENTS.md, CONTRIBUTING.md.
- **POSITIVE:** count `r"\bmanage\.py\s+runserver\s+127\.0\.0\.1:8000\b"` matches: respectively 2, 1, 1.
- Failure: `"{path} must contain {expected} explicit Django loopback command(s); found {actual}"`.
- Protects against satisfying T1 by deleting the startup instructions.

**T3 — `test_backend_launch_scripts_use_loopback`**

- Reads both backend launch scripts.
- **POSITIVE:** their stripped lines contain, respectively:

```text
poetry run python manage.py runserver 127.0.0.1:8000
cmd='exec poetry run python manage.py runserver 127.0.0.1:8000'
```

- Failure: `"{path} is missing executable loopback launch {expected!r}; preserve the Poetry wrapper"`.
- Checking complete stripped lines prevents a comment alone from satisfying this assertion.

### Deployment assertions

**T4 — `test_no_vercel_deployment_venue_claims`**

- Reads all eleven scan-list files.
- Normalize Markdown emphasis/backticks away, collapse whitespace, and case-fold.
- **NEGATIVE:** none of these patterns may match:

```python
r"\b(?:deploy(?:ed|ment)?|host(?:ed|ing)?)\s+(?:(?:on|to)\s+)?vercel\b"
r"\bfrontend\s*:\s*vercel\b"
r"\ballow\s+vercel\s+frontend\b"
r"\bvercel\s*\+\s*vps\b"
```

- Failure: `"{path} contains stale Vercel venue claim {match!r}; describe the self-hosted VPS deployment"`.
- The normalization catches the existing `**Vercel**` spelling.
- These patterns permit “Vercel AI SDK” and historical “Vercel AI Gateway” references.

**T5 — `test_authoritative_deployment_descriptions_are_present`**

**POSITIVE** checks:

| File | Required evidence |
|---|---|
| AGENTS.md | Frontend deployment line contains `self-hosted VPS`, `standalone`, `frontend/.next/standalone/server.js`, `systemd`, `127.0.0.1:3000`, and `nginx` |
| libretiles_PRD.md | Frontend architecture line contains `standalone server`, `self-hosted VPS`, and `nginx` |
| docs/architecture.md | File contains `self-hosted VPS`; Production subsection contains the standalone server path, `systemd`, `127.0.0.1:3000`, and `127.0.0.1:8000` |
| docs/vps_deployment_guide.md | Contains standalone server path, `HOSTNAME=127.0.0.1 PORT=3000`, and `127.0.0.1:8000` |
| backend/config/settings.py | Contains `# CORS — frontend origins allowed to call this API` |

Strip Markdown decoration before checking prose tokens. Extract the architecture Production subsection between its existing `### Production` and `### Local development` headings.

Failure: `"{path} is missing deployment description {expected!r} in {section}"`.

**T6 — `test_prd_phase_seven_names_standalone_vps_deployment`**

- Reads libretiles_PRD.md.
- **POSITIVE:** contains this complete line:

```text
7. **Phase 7**: Deployment (self-hosted VPS: Next.js standalone + Daphne/Django behind nginx). Stripe is rejected for this product direction.
```

- Failure: `"libretiles_PRD.md Phase 7 must describe Next.js standalone and Daphne/Django behind nginx on a self-hosted VPS"`.

**T7 — `test_vercel_ai_sdk_library_references_are_preserved`**

- Reads libretiles_PRD.md and docs/architecture.md.
- **POSITIVE:** PRD retains two `Vercel AI SDK` occurrences; architecture retains `Vercel AI SDK v6`.
- Failure: `"{path} lost its Vercel AI SDK library reference; remove venue claims without renaming the SDK"`.

### Debug assertions

**T8 — `test_throttle_prose_names_django_debug`**

- Reads README.md and backend/.env.example.
- **POSITIVE:** the README throttle-cache table row contains ``Unused for local `DJANGO_DEBUG=true` boot.``.
- **POSITIVE:** the example retains `DJANGO_DEBUG='true'` and the exact replacement comment from D4.
- **NEGATIVE:** neither file matches `r"(?<![\w])DEBUG\s*=\s*['\"]?true\b"`.
- Failures name the file and expected phrase; for a forbidden match: `"{path} uses bare DEBUG=true; name the environment variable DJANGO_DEBUG=true"`.

### Acceptance and isolated invocation

From `backend/`, use:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR \
  PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
  .venv/bin/python -B -m pytest \
  -c /dev/null --rootdir=. --noconftest -p no:cacheprovider \
  tests/test_documentation_deployment_claims.py -v
```

This is the required correction to the handout’s plain pytest command. `backend/pyproject.toml:72` configures Django settings; the installed pytest-django plugin loads them before collection, and `backend/config/settings.py:18` reads `backend/.env`.

Each function remains individually selectable with `::test_name`. Acceptance scenarios:

- All eight functions pass after the proposed replacements.
- Restoring any of the six wildcard commands fails T1.
- Removing startup commands fails T2 or T3.
- Restoring each original venue claim, including Markdown-emphasized Vercel, fails T4.
- Removing corrected deployment descriptions fails T5 or T6.
- Existing SDK and Gateway references remain accepted.
- Restoring either bare debug comment fails T8.
- No application imports, dotenv reads, database work, or network access occur in the isolated run.

Runtime is an acceptance measurement, not a timing assertion inside the module. Target under 0.5 seconds for the focused run on this checkout.

## D4 — Exact text replacements

Blank lines in context blocks are intentional. EOF is identified where two following lines do not exist.

### README.md:77

````text
CONTEXT BEFORE:
poetry run python manage.py seed_models           # seed compatibility + inactive direct rows
poetry run python manage.py createsuperuser       # (optional) admin account
OLD:
poetry run python manage.py runserver 0.0.0.0:8000
NEW:
poetry run python manage.py runserver 127.0.0.1:8000
CONTEXT AFTER:
```

````

### README.md:111

```text
CONTEXT BEFORE:
| `CORS_ALLOWED_ORIGINS` | `http://localhost:3000` | Frontend origin(s) |
| `REDIS_URL` | `redis://127.0.0.1:6379/0` | Redis connection used by Django Channels; also the production fallback for the shared throttle cache |
OLD:
| `DJANGO_THROTTLE_CACHE_URL` | unset | Required only when `DJANGO_DEBUG` is false: `redis://` or `rediss://` URL for the shared DRF throttle cache. If unset, `REDIS_URL` is used; if both are empty, Django refuses to start. Unused for local `DEBUG=true` boot. |
NEW:
| `DJANGO_THROTTLE_CACHE_URL` | unset | Required only when `DJANGO_DEBUG` is false: `redis://` or `rediss://` URL for the shared DRF throttle cache. If unset, `REDIS_URL` is used; if both are empty, Django refuses to start. Unused for local `DJANGO_DEBUG=true` boot. |
CONTEXT AFTER:
| `DJANGO_NUM_PROXIES` | `0` | Trusted reverse-proxy count for DRF unauthenticated throttle identity. `0` keys buckets on `REMOTE_ADDR`. Set to the real proxy count in a deployment; a mismatch either over-throttles or trusts `X-Forwarded-For`. |
| `GAME_WS_TICKET_MAX_AGE_SECONDS` | `10` | Max age for signed websocket tickets |
```

### README.md:203

```text
CONTEXT BEFORE:
  poetry run python manage.py migrate && \
  poetry run python manage.py seed_models && \
OLD:
  poetry run python manage.py runserver 0.0.0.0:8000
NEW:
  poetry run python manage.py runserver 127.0.0.1:8000
CONTEXT AFTER:

# Terminal 2 (frontend):
```

### AGENTS.md:32

````text
CONTEXT BEFORE:
   poetry run python manage.py migrate
   poetry run python manage.py seed_models
OLD:
   poetry run python manage.py runserver 0.0.0.0:8000
NEW:
   poetry run python manage.py runserver 127.0.0.1:8000
CONTEXT AFTER:
   ```

````

### AGENTS.md:187

```text
CONTEXT BEFORE:
## Deployment

OLD:
- Frontend: Vercel (env from `frontend/.env.local.example`).
NEW:
- Frontend: self-hosted VPS; Next.js standalone `frontend/.next/standalone/server.js` under systemd on `127.0.0.1:3000` behind nginx (env names from `frontend/.env.local.example`; see [the VPS deployment guide](docs/vps_deployment_guide.md)).
CONTEXT AFTER:
- Backend: VPS / PaaS with PostgreSQL in production; see [docs/architecture.md](docs/architecture.md) and [README.md](README.md).

```

### CONTRIBUTING.md:45

````text
CONTEXT BEFORE:
```bash
# Terminal 1: Django backend
OLD:
cd backend && poetry run python manage.py runserver 0.0.0.0:8000
NEW:
cd backend && poetry run python manage.py runserver 127.0.0.1:8000
CONTEXT AFTER:

# Terminal 2: Next.js frontend
````

### libretiles_PRD.md:25

```text
CONTEXT BEFORE:
## 4. Architecture Overview

OLD:
- **Frontend**: Next.js 16 (React 19, TypeScript, Tailwind CSS 4, Framer Motion, @dnd-kit) deployed on **Vercel**.
NEW:
- **Frontend**: Next.js 16 (React 19, TypeScript, Tailwind CSS 4, Framer Motion, @dnd-kit), deployed as a standalone server on a **self-hosted VPS** behind nginx.
CONTEXT AFTER:
- **AI**: Next.js API routes using Vercel AI SDK as an OpenAI-compatible adapter. Nine providers ship — `openrouter`, `nvidia-nim`, `groq`, `google-gemini`, `cloudflare-workers-ai`, `mistral`, `ibm-watsonx`, `aion`, `huggingface` — of which `EXACT_PROVIDER_METADATA` marks five `direct`, two `watchlist` and one `legacy`. Dispatch is `ai-runtimes.ts`: `nvidia-nim`, `openrouter` and `ibm-watsonx` have their own runtimes and every other provider goes through the shared OpenAI-compatible constructor. Credentials are server-only. Catalog gated by `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` (default false = bootstrap pairs). Hardcoded bases; no Vercel AI Gateway, LM Studio, or base-URL env vars. There is no `NEXT_PUBLIC_DEFAULT_MODEL`.
- **Backend**: Django 5.x + DRF on self-hosted VPS (game state, validation, auth, admin).
```

### libretiles_PRD.md:174

```text
CONTEXT BEFORE:
5. **Phase 5**: Polish -- mobile UX, move history timeline, starting draw animation, AI thinking particles.
6. **Phase 6**: Human vs human multiplayer (WebSocket, lobby, invites).
OLD:
7. **Phase 7**: Deployment (Vercel + VPS). Stripe is rejected for this product direction.
NEW:
7. **Phase 7**: Deployment (self-hosted VPS: Next.js standalone + Daphne/Django behind nginx). Stripe is rejected for this product direction.
CONTEXT AFTER:
8. **Phase 8**: CI/CD (GitHub Actions), E2E tests (Playwright), performance optimization.
```

The following line is EOF.

### backend/config/settings.py:295

```text
CONTEXT BEFORE:
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

OLD:
# CORS — allow Vercel frontend
NEW:
# CORS — frontend origins allowed to call this API
CONTEXT AFTER:
CORS_ALLOWED_ORIGINS: list[str] = [
    origin.strip()
```

### backend/.env.example:24

```text
CONTEXT BEFORE:

# Shared throttle/lockout cache when DJANGO_DEBUG is false. Unused in local
OLD:
# DEBUG=true boot (LocMemCache). Required in production: a redis:// or
NEW:
# DJANGO_DEBUG=true boot (LocMemCache). Required in production: a redis:// or
CONTEXT AFTER:
# rediss:// URL. If unset, REDIS_URL is the fallback; if both are empty,
# Django refuses to start.
```

### scripts/start-backend.sh:33

```text
CONTEXT BEFORE:
echo ""

OLD:
poetry run python manage.py runserver 0.0.0.0:8000
NEW:
poetry run python manage.py runserver 127.0.0.1:8000
```

The following line is EOF.

### scripts/libretiles.sh:421

```text
CONTEXT BEFORE:
    case "$service" in
        backend)
OLD:
            cmd='exec poetry run python manage.py runserver 0.0.0.0:8000'
NEW:
            cmd='exec poetry run python manage.py runserver 127.0.0.1:8000'
CONTEXT AFTER:
            ;;
        frontend)
```

All other inventoried sites remain unchanged: the architecture and VPS guides already describe the intended production topology; SDK names identify a library; existing tests retain their semantic ownership; frontend LAN behavior requires a separate decision rather than an incidental product change.

## D5 — Implementation gate sketch

1. Obtain a fresh implementation grant with `Native planning mode: not-used`, the nine-path allowlist, and an explicit exception permitting the two executable bind edits. Record acceptance of the LAN compatibility effect.
2. Verify the exact baseline, AP pin, clean porcelain, and `main`. Read current instructions and all mutation targets; confirm every D4 OLD line still matches.
3. Apply the twelve line replacements, preserving indentation, file modes, wrappers, and executable settings.
4. Add the D3 module.
5. Run the isolated focused command from D3. Run `/bin/bash -n` against the two modified scripts; never launch them.
6. Run the requested standing gates once, under the separately authorized implementation environment:

```bash
# From backend/
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest

# From frontend/
npm run typecheck
npm run lint
```

These are integration gates, not prerequisites for each focused documentation-test run. Django-aware gates can consume dotenv configuration; the later grant must explicitly provide an authorized environment for that consumption. This planning exchange did not run them.

7. Inspect `git diff --check`, changed paths, modes, and the complete diff. Confirm settings changes are comments only, no actual dotenv file changed, and production templates remain untouched.
8. Produce one commit. Push only if the fresh grant names the destination and explicitly permits network publication; verify remote equality when authorized.

**Implementation evidence recommendation:** E2 for the combined proposal, because it changes a development network surface and documented LAN compatibility. E1 accurately describes the documentation/static-test subset, but does not describe the full consequence of the script changes. Production deployment remains excluded.

Rollback is a separately authorized revert of the implementation commit. It does not stop or reconfigure already-running development processes.

## D6 — Residual risks and edge cases

- **Script boundary — authority decision:** include both scripts, with an explicit exception. Calling them “functionally documentation” would obscure executable behavior. Deferral would leave two active Django wildcard launch instructions and fail the stated six-site objective.
- **LAN compatibility — established static consequence:** `frontend/README.md:18–23` documents tablet/phone access. `frontend/src/lib/api.ts:42–61` rewrites a loopback API hostname to the browser’s LAN hostname. A Django server bound to `127.0.0.1` cannot receive those direct LAN requests. Cooperator acceptance of this workflow restriction is required before granting the script changes. Frontend listener changes or a new LAN proxy are outside this proposal.
- **Existing processes:** the supervisor can adopt an already-running backend. Editing its future launch command does not make existing wildcard-bound processes loopback-only. No process restart is authorized here.
- **Remaining wildcard references:** frontend port 3000 remains in `frontend/package.json:7`, `scripts/start-frontend.sh:77`, and `scripts/libretiles.sh:603`. Therefore the truthful success claim is “all six Django `0.0.0.0:8000` instructions corrected,” not “all wildcard binds eliminated.”
- **SDK collision:** T4 targets deployment phrases; T7 protects the library references. Gateway history, ignore rules, security fixtures, and lexicon substrings remain untouched.
- **Debug prose:** the existing example is understandable, but `DJANGO_DEBUG=true` is the precise environment-variable spelling. Change both comments without changing the value.
- **Encoding:** use explicit UTF-8. The handout’s claim that Python 3.12 `Path.read_text()` unconditionally defaults to UTF-8 is inaccurate; its unspecified encoding follows text-I/O defaults. No fallback decoder is needed.
- **Poetry:** retain every existing wrapper. The wrapper is unaffected; the bind-address change has the compatibility effect described above.
- **Static-test limits:** explicit file lists do not automatically cover future documents or every possible English paraphrase. Extend the inventory deliberately when documentation surfaces change.
- **Environment independence:** the test code is independent of dotenv files; ordinary repository pytest startup is not. Use the isolated command for focused acceptance.

## D7 — Out-of-slice boundaries

Excluded:

- README restructuring, broader PRD accuracy review, and CONTRIBUTING command modernization.
- Game logic, WordAuthority, APIs, authentication, models, migrations, catalogs, and player UX.
- nginx/systemd templates, production scripts, `next.config.ts`, and `package.json`.
- Frontend listener changes, LAN proxy implementation, and new frontend tests.
- Whole 16 carry residuals and catalog-scheduler configuration.
- Live hosts, SSH, providers, package installation, Docker, Redis startup, and production builds.
- AP changes and logical-whole closure.

### Orchestration critique

**MEASURED**

- Baseline, AP pin, clean worktree, and branch match at both initial and final checks.
- The six bind sites and four venue sites match the supplied line numbers.
- There are two bare debug-prose sites. The architecture’s `self-hosted VPS` wording is at lines 11–12; the standalone production description is at 309–310.
- H9’s file count is wrong: the recommendation changes eight existing files and adds one.
- H9’s “no runtime change” is wrong for the script edits.
- The prescribed focused command mixes the backend virtualenv location with a repository-root test path. From `backend/`, the target is `tests/test_documentation_deployment_claims.py`.
- Plain pytest is not settings-independent in this repository. The isolated command avoids Django setup and actual dotenv reads.
- `test_vps_templates.py` uses subprocesses beyond Bash syntax checking: lines 257–287 execute a synthetic Python environment assertion. The new module should nevertheless use no subprocess.
- Existing dictionary-documentation tests passed with isolation: **2 passed in 0.04 seconds** after explicitly setting `--rootdir=.`. The first invocation without that root override passed but took 18.21 seconds.
- A read-only in-memory scan confirmed six bind matches, four venue matches, two bare-debug matches, and SDK-name acceptance in **0.0214 seconds**. This validates the proposed matching approach, not an implemented module.
- No new module, implementation gates, commit, push, network request, or Meta report write occurred.

**LEAD**

- No additional unverified defect is needed to specify this slice. Future-run timing and full-suite outcomes remain unmeasured.

**Enumeration widened:** searched repository-wide with hidden files included, excluding Git/AP internals, dependencies, build/runtime directories, actual dotenv files, and lockfiles:

```bash
rg -n --hidden -i '0\.0\.0\.0|\brunserver\b|vercel' \
  -g '!.git/**' -g '!.ap/**' \
  -g '!**/node_modules/**' -g '!**/.venv/**' \
  -g '!**/.next/**' -g '!**/__pycache__/**' \
  -g '!.dev/**' -g '!meta/**' \
  -g '!.env' -g '!.env.*' -g '!**/.env' -g '!**/.env.*' \
  -g '!**/*lock*' .
```

The widened search exposed the frontend LAN references, historical Gateway references, ignore entries, and security literals. It found no additional targeted Django bind instructions or Vercel venue claims within that search boundary. Allowed environment examples were checked separately.

Additional reads were justified by these discovery commands:

```bash
rg --files --hidden -g '*conftest.py' -g '*pytest*' -g 'pyproject.toml' -g 'ap.project.conf'
rg -n 'load_dotenv|dotenv_path|^DEBUG' backend/config/settings.py
rg -n 'DJANGO_SETTINGS_MODULE|django.setup|pytest_load_initial_conftests' backend/.venv/lib/python3.12/site-packages/pytest_django/plugin.py
rg -n 'NEXT_PUBLIC_API_URL|localhost|hostname|8000' frontend/src/lib/api.ts
```

**Resolved Execution Issues / Near-Misses:** explicitly setting pytest’s root corrected slow isolated collection; no repository files were created. Secret-bearing dotenv files were neither opened nor loaded.

**Pre-Existing Failure Classification:** no test failure observed; stale claims and command-design discrepancies are established by inspection.

**Smallest next step:** resolve the Cooperator decision on the scripts boundary question, including the LAN compatibility consequence, before implementation. Meta delivery also requires report-rendering authority outside active Plan mode; `.ap/AP.md:366–378` describes a report-only recovery exchange.

**Report justification:** new-evidence

**Context pressure:** moderate; sufficient for the completed bounded design.

Planning authority granted by exchange 01 expires at this terminal report. No implementation authority was granted and none is implied.

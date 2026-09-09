### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: public-docs-and-stale-truth
Worker session ordinal: 03
Worker exchange ordinal: 01

status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Changed files and purpose: none — no repository or Meta file was written
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: retained read-only operation despite the requested Meta write
Pre-Existing Failure Classification: reported WordAuthority payload-parity failure; not reproduced in this exchange

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

# Slice 2 — Streamline public documentation and align product claims

The technical design is complete. Delivery is PARTIAL because the session’s higher-priority Plan mode prohibits writing files, including the requested Meta report. The intended report destination remains `/home/agile/meta/projects/libretiles/17/00-public-docs-and-stale-truth/03_report_00.md`; it was not created.

Start and end commit: `b45149fea0557ca0d87a9a7713cde80bd0fcc03b`. The AP gitlink matches `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; branch `main` and the worktree remained clean.

Read-only validation passed: **10 tests in 0.08 seconds**, comprising all eight deployment documentation guards and both dictionary documentation guards. No network requests, provider calls, dependency installation, secret inspection, or delegation occurred.

## D1 — README inventory and disposition

Measured with `wc -l README.md`, `rg -n '^## |^### ' README.md`, and a complete numbered read of [README.md](/home/agile/Projects/libretiles/README.md). Ranges include intervening whitespace.

| Section | Line range | Current content summary | Disposition | Reason |
|---|---:|---|---|---|
| Features | 9–24 | Gameplay, languages, AI, multiplayer, presentation | condense | Six focused bullets; remove repeated implementation detail and avoid implying Tier 2 is implemented. |
| Languages | 25–44 | Variants, word counts, provenance, review limits | condense | Keep twelve languages and material qualification; link to PRD and AGENTS for details. |
| Quick Start | 45–208 | Setup, environment, provider catalog, dev scripts | condense | Separate local development and production VPS; collapse manual setup; preserve two useful loopback commands and throttle sentence. |
| Architecture | 209–235 | Architecture link and large ASCII diagram | condense | Three responsibility bullets and targeted documentation links replace diagram. |
| AI Agent Tool Workflow | 236–250 | Tool sequence, prompting, overlay | cut-with-pointer | Keep backend authority in Architecture; link to existing architecture workflow. |
| Project Structure | 251–279 | Detailed directory tree | condense | Retain six useful directory entries; remove file inventory and billing tombstone detail. |
| API Endpoints | 280–315 | Auth, catalog, gameplay and AI endpoint lists | cut-with-pointer | Link to architecture flows and actual route definitions; do not imply architecture contains an exhaustive endpoint reference. |
| Explicit provider capability probe | 316–359 | Live probe commands, statuses, activation policy | cut-with-pointer | Existing architecture section already contains commands, statuses and activation boundary. |
| Operations (catalog refresh) | 360–365 | Refresh schedule and provider rollout | cut-with-pointer | Existing architecture operations section and VPS guide own this detail. |
| Testing | 366–385 | Backend and frontend checks | condense | Keep standard check commands; use scoped mypy targets, `npm run typecheck`, and explicit separate-terminal context. |
| Tech Stack | 386–401 | Frameworks, languages and libraries | condense | Small table; identify Python 3.12 as recommended, retain Vercel AI SDK library name. |
| Game Engine | 402–417 | Engine modules, endgame rules, harness | cut-with-pointer | Keep pure-engine and validation responsibility in Architecture; link to technical guide. |
| Troubleshooting | 418–424 | Candidate verdicts, weak AI, failed providers | cut-with-pointer | Preserve server verdict authority and missing-credential behavior in short core prose; link to maintainer and provider guidance. |
| Contributing | 425–428 | Contributor and agent guide links | keep | Clear navigation for contributors and maintainers. |
| License | 429–431 | MIT | keep | Preserve license statement. |

Also replace the introduction at lines 3–7 with a short word-game pitch and a present-tense standalone-repository statement. Remove publication-future and parent-monorepo explanation from the public introduction.

**Nothing moves into another file.** Existing deep-dive sections are deleted from README with relevant pointers retained.

## D2 — Proposed README outline

Target **190 lines**, acceptable range **170–210**, including code fences and whitespace. Do not add filler to meet the target.

| Exact heading | Content | Approximate lines |
|---|---|---:|
| `# Libre Tiles` | Word-game pitch; self-contained repository | 5 |
| `## Features` | Twelve variants/locales, AI, live multiplayer, server validation, responsive interaction, free-only product | 14 |
| `## Languages` | Twelve language names; English Collins 2019; Slovak provenance and eight-catalog review caveat; PRD pointer | 10 |
| `## Quick Start` | Entry to clearly separated environments | 2 |
| `### Local development` | Recommended supervisor; collapsed manual setup and restart commands; credentials and environment essentials | 90 |
| `### Production (VPS)` | Standalone Next.js, Daphne, nginx/systemd, PostgreSQL/Redis and runbook pointer | 10 |
| `## Architecture` | Next orchestration, Django authority, Channels; links to workflow, provider probes, operations and route definitions | 14 |
| `## Project Structure` | `backend/gamecore`, `backend/game`, `backend/catalog`, `backend/assets`, `frontend/src`, `docs` | 12 |
| `## Testing` | Backend checks and frontend checks in separate terminal blocks | 22 |
| `## Tech Stack` | Compact backend/frontend/realtime-storage table | 9 |
| `## Contributing` | CONTRIBUTING and AGENTS links | 4 |
| `## License` | MIT | 3 |

Use these existing technical destinations:

- `docs/architecture.md#ai-agent-workflow`
- `docs/architecture.md#explicit-capability-probe-boundary`
- `docs/architecture.md#catalog-operations-rollout-and-rollback`
- `docs/vps_deployment_guide.md`
- `backend/game/urls.py` and `backend/accounts/urls.py` for route definitions.

The architecture summary must explicitly say that persisted placements use backend `WordAuthority` over the selected variant’s physical tiles; the AI judge is advisory.

No public API, schema, type, runtime behavior, dependency, or migration changes are proposed.

## D3 — Complete replacement Quick Start text

The following replaces README lines 45–208. Its two loopback commands serve first-time manual setup and subsequent manual starts. The old chained “One-liner” is removed.

````markdown
## Quick Start

### Local development

Use Python 3.12, Poetry 2.3.2 or newer, and Node.js 24 with npm.
See [CONTRIBUTING.md](CONTRIBUTING.md#prerequisites) for compatibility details.
Run commands from this repository's root unless stated otherwise.

SQLite is the local default. AI-only local play needs Django and Next.js;
human multiplayer also needs Redis for matchmaking, websocket sync, and chat.

**Recommended — start both development services:**

```bash
python3.12 -m venv backend/.venv
source backend/.venv/bin/activate
./scripts/libretiles.sh
```

The supervisor installs dependencies, runs migrations and model seeding, and
starts both services. It creates environment files only when absent and generates
`DJANGO_SECRET_KEY` into a new `backend/.env`. Existing environment files are preserved.

Open http://localhost:3000. The Django development API is at
http://127.0.0.1:8000; its local admin is at http://127.0.0.1:8000/admin/.

For external AI opponents, configure `OPENROUTER_API_KEY` and/or `NVIDIA_API_KEY`
in `frontend/.env.local` for the seeded compatibility catalog, then restart.
Other provider integrations require configured server credentials and explicit
catalog activation; see [provider activation](docs/architecture.md#explicit-capability-probe-boundary).
The UI can boot without provider credentials.

```bash
./scripts/libretiles.sh status
./scripts/libretiles.sh logs
./scripts/libretiles.sh restart
./scripts/libretiles.sh stop
```

<details>
<summary>Manual setup and two-terminal development</summary>

Use this as an alternative to the supervisor. Stop supervisor-managed services first
if they are already running.

**Terminal 1 — backend, first setup:**

```bash
cd backend
python3.12 -m venv .venv
source .venv/bin/activate
poetry install
[ -f .env ] || cp .env.example .env
```

Before continuing, set a privately generated `DJANGO_SECRET_KEY` in `backend/.env`:
at least 50 characters, at least five unique characters, and no `django-insecure-`
prefix. The example deliberately leaves it empty. Retain an existing valid key.

```bash
poetry run python manage.py migrate
poetry run python manage.py seed_models
poetry run python manage.py runserver 127.0.0.1:8000
```

**Terminal 2 — frontend, starting from the repository root:**

```bash
cd frontend
[ -f .env.local ] || cp .env.local.example .env.local
# Configure server-only provider credentials here if using external AI opponents.
npm install
npm run dev
```

For local Django Admin access, optionally run `poetry run python manage.py createsuperuser`
from `backend/`.

**Subsequent manual starts — each terminal starts at the repository root:**

```bash
# Terminal 1
cd backend && poetry run python manage.py runserver 127.0.0.1:8000
```

```bash
# Terminal 2
cd frontend && npm run dev
```

</details>

Full configuration is documented in [backend/.env.example](backend/.env.example)
and [frontend/.env.local.example](frontend/.env.local.example).
Keep provider credentials server-only; never put them in `NEXT_PUBLIC_` variables
or commit environment files. Review existing backend settings after changes and
restart the affected service.

Keep `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` for the default local setup.
`seed_models` works offline; public catalog synchronization is optional.
For local human multiplayer, the default Redis URL is `redis://127.0.0.1:6379/0`.

`DJANGO_THROTTLE_CACHE_URL`: Unused for local `DJANGO_DEBUG=true` boot.
Production requires shared Redis throttling, with `REDIS_URL` as the fallback.

### Production (VPS)

Production uses a self-hosted VPS with nginx terminating TLS and systemd managing
Next.js standalone and Daphne/Django. Next.js runs
`frontend/.next/standalone/server.js` on `127.0.0.1:3000`; Daphne listens on
`127.0.0.1:8000`. PostgreSQL and Redis remain private.

Follow the [VPS deployment guide](docs/vps_deployment_guide.md) for prerequisites,
environment settings, rendered templates, deployment, verification, and recovery.
It also explains the private Django Admin listener and the Next-to-Django callback
at `127.0.0.1:8001`. Production uses `DJANGO_DEBUG=false`.

The development supervisor and commands above are for local development.
Production host changes and the optional catalog-refresh schedule require separate
operator authority.
````

Grounding: supervisor preparation and environment creation are implemented at [scripts/libretiles.sh:247](/home/agile/Projects/libretiles/scripts/libretiles.sh:247), with service preparation at line 346. Production topology and callback requirements are documented at [docs/vps_deployment_guide.md:7](/home/agile/Projects/libretiles/docs/vps_deployment_guide.md:7) and line 40.

## D4 — CONTRIBUTING alignment

Locations below refer to the measured baseline [CONTRIBUTING.md](/home/agile/Projects/libretiles/CONTRIBUTING.md). Replace exact text or whole blocks as specified; retain other text.

1. **Prerequisites, lines 9–10.**

   Old:

   ```text
   - Python 3.11+ with [Poetry](https://python-poetry.org/)
   - Node.js 20+ with npm
   ```

   New:

   ```text
   - Python 3.12 recommended with [Poetry](https://python-poetry.org/) 2.3.2 or newer. The backend manifest permits Python >=3.11,<3.14; the documented VPS setup uses 3.12.
   - Node.js 24 recommended with npm; the documented tooling also supports Node 20.19+ or 22.12+.
   ```

   Reason: [backend/pyproject.toml:10](/home/agile/Projects/libretiles/backend/pyproject.toml:10) permits 3.11–3.13; [backend/.venv/pyvenv.cfg:3](/home/agile/Projects/libretiles/backend/.venv/pyvenv.cfg:3) records 3.12.12. VPS prerequisite versions appear at guide line 16. Do not invent a Python 3.12 minimum.

2. **First-time setup, immediately after line 24’s copy command.**

   Insert:

   ```text
   # Before continuing, privately set DJANGO_SECRET_KEY in .env:
   # at least 50 characters, at least 5 unique, no django-insecure- prefix.
   # The example is empty; preserve an existing valid key.
   ```

   Before the setup code fence, insert:

   ```text
   The recommended local supervisor in [README.md](README.md#local-development) generates the key when creating a new backend environment file. The manual setup below requires you to set it before migrations.
   ```

   Reason: the current copy proceeds directly to Django initialization with an empty example key.

3. **Provider setup comment, line 33.**

   Old:

   ```text
   # Set server-only OPENROUTER_API_KEY and/or NVIDIA_API_KEY.
   ```

   New:

   ```text
   # For the seeded compatibility catalog, set server-only OPENROUTER_API_KEY and/or NVIDIA_API_KEY.
   # Other integrations need their documented credentials and explicit catalog activation.
   ```

   Reason: distinguish bootstrap setup from the broader shipped integrations.

4. **Running locally, lines 39–49: no command change.**

   Preserve the single `manage.py runserver 127.0.0.1:8000` occurrence. Change each terminal comment to say it starts from the repository root.

   After the block insert:

   ```markdown
   ### Production deployment

   Production uses Next.js standalone and Daphne/Django under systemd behind nginx on a self-hosted VPS, with PostgreSQL and Redis. Follow the [VPS deployment guide](docs/vps_deployment_guide.md) for production setup; the commands above start development servers.
   ```

5. **Quality commands, lines 61 and 76.**

   Replace `poetry run mypy .` with `poetry run mypy config game gamecore accounts catalog`.

   Replace `npx tsc --noEmit` with `npm run typecheck`.

   Keep Poetry wrappers in public contributor instructions. The AP worker’s environment-cleared `.venv/bin/` route is an execution constraint for this exchange, not a reason to publish that wrapper everywhere.

6. **Architecture diagram, lines 86–95.**

   Replace the entire fenced diagram with:

   ```markdown
   This repository is self-contained. Next.js serves the UI and orchestrates external AI calls; Django owns game state and authoritative validation; Django Channels and Redis provide human multiplayer. See [the architecture guide](docs/architecture.md) for data flows and [the VPS guide](docs/vps_deployment_guide.md) for production topology.
   ```

   Reason: the current diagram depicts only two external integrations.

7. **Key principle 4, line 102.**

   Replace the whole paragraph with:

   ```markdown
   4. **Admin-first catalog** -- `seed_models` creates the compatibility bootstrap rows and inactive prepared direct/watchlist rows without changing existing activation. Eligible active direct rows precede the compatibility tail. `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` changes only that tail: curated bootstrap pairs when false, up to four newest eligible OpenRouter rows plus eligible seeded NIM when true. Activation and fallback ordering use the reviewed Django Admin workflow; `is_active` remains the kill switch.
   ```

8. **Key principle 5, line 103.**

   Replace `the AI model uses tool calling to validate its own moves` with `the AI model proposes moves through tools and Django validates them`.

   Retain the three-pair fallback cap.

9. **Shortlist policy, lines 136–138.**

   Replace both paragraphs with:

   ```markdown
   Eligible active direct rows precede the NIM/OpenRouter compatibility tail. With `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false`, that tail uses the curated `FREE_RIVAL_PAIRS`; with the flag enabled, it uses up to four newest eligible OpenRouter models plus eligible seeded NIM. The reviewed Admin workflow controls activation and applicable ordering. Stripe is rejected for this product direction. LM Studio and Vercel AI Gateway remain historical rejections, not live routing.

   Membership and selection live in `backend/catalog/selection.py` and `seed_models.py`. Frontend runtime validation uses exact registry pairs for direct/watchlist/NIM integrations and structural `:free` validation for OpenRouter, together with live Django catalog membership. Use native IDs; the NIM id has no `:free` suffix. See [provider activation and catalog operations](docs/architecture.md#catalog-operations-rollout-and-rollback). Configuring the documented `libretiles-openrouter-catalog-refresh` host schedule requires separate production authority.
   ```

   Reason: fixes incomplete catalog description, the false “no static frontend ID allowlist” claim, and stale Slovak/out-of-cut language. Selection supports reviewed ordering; avoid claiming immutable canonical order after review.

10. **Backend tests, before line 151’s fence.**

    Insert `Run these commands from backend/.`

    Remove the coverage example at lines 161–162. `pytest-cov` is not declared in the backend development dependencies.

11. **Test categories, lines 167 and 169.**

    Replace:

    ```text
    - **Gamecore tests** -- pure Python, no network, no DB. Always pass.
    ```

    with:

    ```text
    - **Gamecore tests** -- pure Python, no network, no DB; cover rules, scoring, and dictionary regressions.
    ```

    Replace:

    ```text
    - **Live provider tests** -- not part of this cut; do not add an internet pytest suite here.
    ```

    with:

    ```markdown
    - **Live provider probes** -- explicit operator checks, separate from ordinary tests; see [the capability-probe guide](docs/architecture.md#explicit-capability-probe-boundary).
    ```

**Recommended no changes:** contributor submission workflow, style requirements, pure-engine principle, existing source-location table, free-only billing-tombstone statement, and environment-file exclusion. No remaining Vercel hosting claim was found; preserve the historical Gateway reference.

Evidence for catalog corrections: [selection.py:146](/home/agile/Projects/libretiles/backend/catalog/selection.py:146), [model-catalog.ts:46](/home/agile/Projects/libretiles/frontend/src/lib/model-catalog.ts:46), and [admin.py:38](/home/agile/Projects/libretiles/backend/catalog/admin.py:38).

## D5 — PRD alignment

Locations refer to [libretiles_PRD.md](/home/agile/Projects/libretiles/libretiles_PRD.md). These replacements preserve existing goals while distinguishing implemented features from planned ones.

| Location | Exact old text | Exact new text | Reason |
|---|---|---|---|
| Line 3 | `Updated: August 25, 2026` | `Updated: September 9, 2026` | Date of this repository-grounded documentation review; not a deployment date. |
| Line 7, substring | `AI opponents via provider-diverse free rivals, and a lightweight Django backend with full admin control.` | `AI opponents via provider-diverse free rivals, live human-vs-human multiplayer, and a lightweight Django backend with full admin control.` | Include shipped multiplayer in the pitch. |
| Line 14 | `4. Prepare architecture for human-vs-human multiplayer (v2).` | `4. Support live human-vs-human multiplayer with queue matchmaking, websocket synchronization, and in-game chat.` | Replace preparation goal with implemented capability. |
| Line 49 | `- Create game (vs AI or vs human placeholder).` | `- Create AI games or join/cancel the human matchmaking queue; human games start when a second player is matched.` | Remove placeholder claim. |
| Line 57 | `- Frontend fetches available models from /api/catalog/models/. There is no static frontend ID allowlist (`frontend/src/lib/model-catalog.ts`).` | `- Frontend fetches available models from /api/catalog/models/. External runtime pairs must pass frontend registry validation and live Django catalog membership checks (`frontend/src/lib/model-catalog.ts`).` | Exact pair validation exists. |
| Line 60 | `- AI uses tool calling: validate moves, check words, score moves via Django API endpoints. Collins 2019 on Django remains the move validator.` | `- External AI move generation uses `validateMove` for backend validation and scoring, then `finishMove` only after a valid candidate. Django `WordAuthority.accepts_tokens` is the sole formed-word authority over physical tiles and the selected variant's lexicons; Collins 2019 applies to English. Free-form model text cannot authorize a move.` | Correct tools, multilingual authority and action boundary. |
| Line 62 | `- Move prompt: legality-first anchor search, early backend-validated scoring floor, budget-bounded diversity, strict JSON. Judge prompt: Collins-2019-only, no natural-usage override. Seeded Admin presets refresh only via reversible SHA-256 hash-gated migration `0010` (unmodified seed rows only).` | `- Move prompt: non-overridable TypeScript CORE plus advisory SEARCH_PROFILE, legality-first anchor search, an early backend-validated scoring floor, and budget-bounded diversity. Judge prompt: Collins-2019-only, no natural-usage override. Seeded presets refresh through reversible SHA-256 hash-gated migrations `0010` and `0011`; customized rows are preserved.` | Account for landed prompt authority and migration 0011. |
| Line 68 | `- Tier 2: Online dictionary API for words not in the Collins 2019 list (optional; the local list is comprehensive).` | `- Tier 2: Optional online dictionary assistance is planned and not implemented.` | Clearly mark capability status. |
| Line 69 | `- Tier 3: AI Judge via the shared free-rival fallback queue (up to three attempts; HTTP 503 on exhaustion).` | `- Tier 3: Advisory Collins-2019-conservative AI Judge via the shared free-rival fallback queue (up to three attempts; HTTP 503 on exhaustion). It never overrides a persisted Django verdict.` | Prevent tier-fallback prose from implying scoring authority. |
| Line 70 | `- Status: **Tier 1 + 3 implemented**, Tier 2 optional.` | `- Status: **Tier 1 + advisory Tier 3 implemented**; Tier 2 remains optional planned work.` | Match preceding distinction. |
| Line 75 | `- Starting draw animation: tiles fly from bag, flip to reveal, winner announced.` | `- Starting draw animation: tiles enter, flip to reveal letters, and highlight the starting player.` | Describe measured animation behavior. |
| Line 78 | `- Blank tile letter picker: 26-letter grid modal.` | `- Blank tile picker: grid modal using the selected variant's alphabet, with an English fallback.` | Picker is variant-aware. |
| Line 82 | `- Move history timeline with expandable word details.` | `- Planned: per-game move timeline with expandable word details. Game-list history and reopening saved games are implemented.` | Distinguish game history from an unimplemented move timeline. |
| Line 83 | `- Responsive: mobile bottom-sheet rack, pinch-zoom board, tap-to-place alternative.` | `- Responsive layouts and touch drag-and-drop are implemented; mobile bottom-sheet rack and pinch-zoom remain planned.` | Reconcile with Known Gaps. |
| Line 84 | `- Premium squares configurable for any letter (blank tiles).` | `- Assigned blank tiles represent a selected variant token and score zero.` | Fix conflation of premium squares and blanks. |
| Line 86 | `- Status: **Core implemented** (Board, Tile, TileRack, ScorePanel, GameControls, BlankPicker, DnD, confetti). Premium animations in progress.` | `- Status: **Core implemented** (Board, Tile, TileRack, ScorePanel, GameControls, BlankPicker, DnD, confetti). Shared optional Premium Look chrome is implemented; remaining UI work is listed in Known Gaps.` | Premium surface implementation exists. |
| Line 95 | `- AIModel: add/remove/toggle models, set quality tier; catalog activation and availability. No token or per-game prices.` | `- AIModel: add inactive models and edit permitted metadata; activation and fallback ordering use the reviewed Admin workflow. Model deletion is disabled. No token or per-game prices.` | Matches Admin restrictions. |
| Line 131 | `- Tests: pytest (backend), Vitest + Playwright (frontend).` | `- Tests: pytest (backend) and Vitest (frontend); Playwright E2E coverage is planned.` | No tracked Playwright setup or declared dependency. |
| Line 136 | `- AI move timeout: configurable via AI_MOVE_TIMEOUT_SECONDS.` | `- AI turn timeout and provider-step budget are configurable in Settings (`aiTimeout`, `aiMaxSteps`); the move route bounds the requested per-attempt timeout and remaining steps.` | Settings drive actual requests. |
| Line 144 | `- GitHub-ready: README, PRD, CI workflows, .env.example.` | `- Repository documentation and environment examples are present; GitHub Actions workflows remain planned.` | No tracked `.github` workflows. |
| Line 151 | `- **Live AI tests**: Not part of this cut. Do not add an internet pytest suite for OpenRouter.` | `- **Live AI probes**: Explicit operator-only capability checks; ordinary tests use synthetic behavior and skip live provider calls.` | Existing opt-in provider probe exists. |
| Line 152 | `- **Frontend tests**: Vitest (components), Playwright (E2E).` | `- **Frontend tests**: Vitest unit and integration tests; Playwright E2E tests remain planned.` | Match installed test tooling. |
| Line 153 | `- **CI**: ruff + mypy + offline pytest (backend), eslint + tsc + vitest (frontend).` | `- **Planned CI**: ruff + mypy + offline pytest (backend), eslint + tsc + vitest (frontend).` | Preserve target without claiming installed automation. |
| Line 160 | `- Human vs human multiplayer deferred to v2.` | Delete line. | Multiplayer is live. |
| Line 161 | `- Online dictionary API (Tier 2) may not be needed if the local Collins 2019 list is sufficient.` | `- Optional online dictionary assistance (Tier 2) is not implemented.` | Precise remaining gap without deciding product priority. |
| Line 162 | `- Starting draw animation not yet eye-candy (basic flow implemented).` | Delete line. | Animated entry, flip and winner emphasis exist; aesthetic acceptance is not required for this correction. |
| Line 163 | `- Move history timeline UI not yet implemented.` | `- A per-game move timeline with expandable word details remains unimplemented; game-list history is available.` | Avoid conflating two history surfaces. |
| Line 172 | `5. **Phase 5**: Polish -- mobile UX, move history timeline, starting draw animation, AI thinking particles.` | `5. **Phase 5** (partial): Starting draw animation, game-list history, and shared Premium Look chrome are implemented; mobile bottom-sheet/pinch-zoom UX, a per-game move timeline, and AI thinking particles remain planned.` | Reconcile roadmap with implemented surfaces and retained requirements. |
| Line 173 | `6. **Phase 6**: Human vs human multiplayer (WebSocket, lobby, invites).` | `6. **Phase 6** (done): Human vs human multiplayer (queue join/cancel, waiting room, WebSocket synchronization, and in-game chat).` | Describe shipped scope without claiming invite links. |

Apply these additional whole-paragraph changes:

**Product goal 2, line 12:** replace only the sentence

```text
Flag-off (default) is five curated bootstrap pairs; flag-on is the four newest eligible OpenRouter models plus the seeded NIM tuple.
```

with

```text
Eligible active direct rows precede a compatibility tail; the dynamic flag selects the curated bootstrap cohort or up to four newest eligible OpenRouter rows plus eligible seeded NIM.
```

Keep all free-only and Stripe sentences.

**Product goal 3, line 13:** replace the whole goal with:

```markdown
3. Provide Django Admin control over catalog configuration through the reviewed activation and ordering workflow. In production, public `/admin` serves the Next.js staff console; Django contrib admin is private, as documented in the [VPS guide](docs/vps_deployment_guide.md#private-django-admin). Catalog Admin does not manage token or per-game prices.
```

**Architecture AI paragraph, line 26:** replace the whole paragraph with:

```markdown
- **AI**: Next.js API routes use Vercel AI SDK for nine external provider integrations: `openrouter`, `nvidia-nim`, `groq`, `google-gemini`, `cloudflare-workers-ai`, `mistral`, `ibm-watsonx`, `aion`, and `huggingface`. Dispatch uses dedicated OpenRouter, NIM and watsonx runtimes plus a shared OpenAI-compatible constructor. Credentials are server-only. Prepared direct/watchlist rows default inactive; the dynamic catalog flag affects only the compatibility tail. Provider endpoints are hardcoded; no Vercel AI Gateway, LM Studio, or provider base-URL environment variables. There is no `NEXT_PUBLIC_DEFAULT_MODEL`.
```

This removes the stale `EXACT_PROVIDER_METADATA` tier count without making a new product decision about its additional local-engine entry.

**Architecture backend paragraph, line 27:** replace with:

```markdown
- **Backend**: Daphne/Django 5.x + DRF under systemd on the self-hosted VPS; nginx routes HTTP and websocket traffic. Django owns game state, validation, authentication, and admin.
```

After the database paragraph, insert:

```markdown
- **Realtime**: Django Channels + Redis for human matchmaking, websocket synchronization, and chat. Redis also backs shared production throttling.
```

**FR-04 first bullet, line 56:** replace with:

```markdown
- Django Admin controls model activation and applicable ordering through its reviewed workflow. Eligible active direct rows precede the compatibility tail. `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false` selects that tail from the five curated bootstrap pairs; true selects up to four newest eligible OpenRouter models plus eligible seeded NIM. Only catalog row 1 is flagship/recommended. Seed and sync preserve existing `is_active` decisions.
```

**FR-07 first bullet, line 89:** replace only the last sentence:

```text
Flag-off shows the five bootstrap pairs; flag-on shows newest-four-plus-NIM.
```

with:

```text
Eligible active direct rows precede the flag-selected compatibility tail.
```

**FR-09 second bullet, line 103:** replace with:

```markdown
- Play and Judge use the selectable free-rival catalog, with eligible active direct rows followed by the flag-selected compatibility tail. Judge uses the same preference-first fallback queue as Play.
```

**FR-10, lines 108–112:** replace the entire block with:

```markdown
### FR-10: Human vs Human Multiplayer
- Authenticated players join or cancel the human matchmaking queue.
- A waiting room becomes an active two-player game when a compatible opponent joins.
- Django Channels and Redis synchronize game state and in-game chat over authenticated websockets.
- Django derives the acting player from authentication and returns only that player's private rack.
- Status: **Implemented** (game services, websocket consumers, and frontend waiting-room/game flows).
```

**FR-11 rollout and rollback, lines 116–117:** replace with:

```markdown
- Compatibility-tail rollout: deploy compatible code with `DYNAMIC_FREE_MODEL_CATALOG_ENABLED=false`, obtain migrate/sync evidence, then enable the flag and restart Django. Direct-provider activation is a separate credential, capability-probe, and reviewed Admin operation.
- Compatibility-tail rollback: set the flag false and restart Django; pause the optional schedule and/or deactivate affected rows through the reviewed Admin workflow. Existing active direct rows remain ahead of the compatibility tail.
```

**Preserve unchanged:**

- Frontend deployment paragraph at line 25 and **the entire Phase 7 line at line 174**, including its exact static-test anchor.
- Both `Vercel AI SDK` references and historical Gateway/LM Studio rejections.
- Three fallback attempts and Judge’s 10-second attempt/30-second overall limits. Code confirms these values.
- English Collins 2019 identification and `279,496`, protected by the additional dictionary tests.
- Twelve locales, 324-key structural description, and translation-review caveats.
- Performance numbers as requirements, not measured benchmark claims.
- Phase 8 as future CI/E2E work.

Further evidence was obtained from:

- [BlankPicker.tsx:17](/home/agile/Projects/libretiles/frontend/src/components/game/BlankPicker.tsx:17).
- [draw page:57](/home/agile/Projects/libretiles/frontend/src/app/draw/[id]/page.tsx:57).
- [game page:1714](/home/agile/Projects/libretiles/frontend/src/app/game/[id]/page.tsx:1714).
- [provider-registry.ts:53](/home/agile/Projects/libretiles/frontend/src/lib/provider-registry.ts:53).
- [ai-fallback.ts:17](/home/agile/Projects/libretiles/frontend/src/lib/ai-fallback.ts:17).
- [Judge route:40](/home/agile/Projects/libretiles/frontend/src/app/api/ai/judge/route.ts:40).
- [WordAuthority:202](/home/agile/Projects/libretiles/backend/gamecore/word_authority.py:202).

## D6 — Static-test reconciliation

**No test edits are proposed.** All eight assertions remain applicable.

| Guard | Baseline location in test module | Reconciliation |
|---|---:|---|
| T1 — no wildcard Django bind | 38–46 | Keep unchanged. Proposed commands explicitly bind loopback. The actual scan contains eleven paths, not five. |
| T2 — explicit launch counts | 49–63 | Keep README **2**, AGENTS **1**, CONTRIBUTING **1**. README examples represent initial and subsequent manual launches. |
| T3 — script loopback commands | 66–78 | Keep unchanged; scripts are outside the allowlist. |
| T4 — no Vercel hosting claim | 88–104 | Keep unchanged. Production prose consistently describes a self-hosted VPS. |
| T5 — authoritative VPS descriptions | 107–130 | Keep unchanged. PRD preserves `standalone server`, `self-hosted VPS`, and `nginx`; other guarded files remain untouched. |
| T6 — exact Phase 7 line | 133–143 | Keep line 174 verbatim. |
| T7 — SDK library references | 146–157 | Keep two PRD occurrences of `Vercel AI SDK`; architecture occurrence is untouched. |
| T8 — exact debug/throttle prose | 162–183 | Keep `Unused for local `DJANGO_DEBUG=true` boot.` in the standalone README sentence. The environment table can disappear without changing this test. |

The additional dictionary module remains unchanged and green: preserve the shipped English dictionary name/count and do not introduce the unshipped dictionary name it forbids.

Measured baseline command, from `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR \
  PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONDONTWRITEBYTECODE=1 \
  .venv/bin/pytest -c /dev/null -p no:cacheprovider \
  tests/test_documentation_deployment_claims.py \
  tests/test_documentation_dictionary_claims.py -q
```

Result: **10 passed in 0.08s**. Explicit configuration and disabled plugin autoload avoid Django initialization and dotenv reads for these standard-library-only tests. This is baseline evidence; the edited candidate must be tested again.

## D7 — Allowlist and implementation gates

The later implementation mutation allowlist is exactly:

```text
/home/agile/Projects/libretiles/README.md
/home/agile/Projects/libretiles/CONTRIBUTING.md
/home/agile/Projects/libretiles/libretiles_PRD.md
```

**Expected evidence tier: E1**, with non-independent implementation evidence. No static-test mutation is needed.

Ordered execution plan for a separately authorized fresh implementation session:

1. **Repository gate:** verify the exact baseline, AP gitlink, clean porcelain and `main`. Stop on mismatch.
2. **Verify old text:** confirm all D4/D5 replacement anchors and test assumptions against the baseline before editing.
3. **Apply documentation edits:** use D1–D5; preserve the exact T1–T8 anchors and English dictionary count. Keep runtime and configuration files untouched.
4. **Focused verification:** run the D6 command against both documentation test modules. Require all ten to pass.
5. **Script syntax gate:** not applicable; no scripts may be touched. An unexpected script diff is an allowlist violation.
6. **Standing gates:** the implementation grant must establish a permitted route for Django initialization before running mypy, migration checks and the full suite. Settings calls `load_dotenv(BASE_DIR / ".env")` at [settings.py:18](/home/agile/Projects/libretiles/backend/config/settings.py:18); the static-test isolation above does not solve that broader boundary. Do not silently bypass the secret restrictions or the declared execution route.

   Subject to that explicit execution envelope, run from `backend/`:

   ```bash
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/mypy config game gamecore accounts catalog
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py makemigrations --check --dry-run
   env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest
   ```

   From `frontend/`:

   ```bash
   npm run typecheck
   npm run lint
   ```

   Do not install packages, start services, run a production build, or contact providers. Record the existing parity failure separately; do not suppress it. Any additional failure blocks slice acceptance pending classification.

7. **Diff review:** run `git diff --check`; verify only the three allowlisted paths changed, README length and links are sensible, and D4/D5 replacements are complete.
8. **One commit:** stage the three explicit paths only; use `docs: streamline README and align standalone product documentation`. Record the resulting commit and clean status.
9. **Pre-push gate:** publication requires a separate explicit network/publication grant. Local tracking configuration is `origin` / `refs/heads/main`; the current planning grant authorizes no contact with it.
10. **Push:** only under that publication grant, after confirming remote identity and expected remote baseline, make a normal non-force push of the accepted commit.
11. **Readback:** under the same publication grant, verify the remote `refs/heads/main` equals the accepted commit. Without publication authority, stop after the local commit and report publication as not performed.

Acceptance requires all ten focused documentation tests passing, no additional standing-gate failures, and no off-allowlist changes. A documentation-only rollback is a separately authorized revert of the single slice commit.

## D8 — Residuals and out-of-slice work

| Residual | Evidence/status | Disposition and forward owner |
|---|---|---|
| WordAuthority payload-parity failure | Supplied pre-existing failure; not reproduced here | Preserve test and oracle. Carry to the existing gamecore/parity workstream, outside Whole 17. |
| Architecture fallback limits | `docs/architecture.md:183–184` says five attempts/50 seconds; code uses three/30 | Candidate for Whole 17 Slice 3 if its allowlist includes architecture; otherwise a separately authorized documentation follow-up. |
| Architecture word-validation diagram | `docs/architecture.md:228–258` depicts an AI fallback producing validity; current authority distinguishes advisory queries from scoring | Same follow-up owner. README/PRD must state the correct authority explicitly. |
| Architecture catalog ordering prose | Lines 181 and 394 say fixed order; selection supports reviewed ordering at lines 200–230 | Same follow-up owner; do not copy the fixed-order claim. |
| AGENTS catalog narrative | `AGENTS.md:35–37`, 127 and 147–150 omit active direct rows | Maintainer-document reconciliation in Slice 3 or a separate grant. AGENTS is excluded from this slice. |
| Environment-example catalog comments | `backend/.env.example:67–68` describe the dynamic flag as controlling the entire catalog | Configuration-documentation follow-up; no example-file changes here. |
| Frontend example’s README probe pointer | `frontend/.env.local.example:79–82` points to README for inline probe commands | README retains a clear capability-guide link; direct pointer cleanup belongs to later documentation work. |
| Startup-script secret initialization | `scripts/start-backend.sh:10–22` copies the empty-key example then initializes Django without generating a key | Separate development-script task. Remove README’s recommendation of this script as a fresh-bootstrap alternative. |
| Supervisor credential warning | `scripts/libretiles.sh:321–334` only checks OpenRouter/NIM credentials | Separate development-script task; do not change executable behavior. |
| LAN/tablet implication | `scripts/libretiles.sh:603` advertises frontend LAN binding while Django is loopback-bound | Preserve Slice 1 binds; any LAN support or message correction needs a separate grant. |
| Local-engine metadata | `provider-registry.ts:53–60` contains an additional engine entry | Remove stale aggregate metadata claims; do not infer a new product promise or modify local-engine code. |
| Existing Whole 16 residuals | IHR-S1-F01, IHR-S2-R01, HSTS W021, billing orphan, throttle scopes, JWT storage, CSP | Carry unchanged to their existing owners; no re-audit or repair here. |

**Explicit exclusions:** no gamecore, services, views, serializers, auth, models, migrations, player UX, nginx/systemd templates, VPS scripts, `next.config.ts`, package manifests, live host, AP upgrade, Slice 1 reversal, or logical-whole closure.

### Orchestration critique

**MEASURED**

- The three target lengths are correct: README 431, CONTRIBUTING 189, PRD 175 lines.
- README Features has **13 bullets**, not 15.
- README’s loopback anchors are exactly lines **77 and 203**; the throttle sentence is at **111**.
- PRD multiplayer staleness extends beyond FR-10: goal 4 at **14**, session placeholder at **49**, Known Gaps at **160**, and roadmap at **173**. Line 89 concerns settings, not Known Gaps.
- H4’s assumed manifest minimum is false: `python = ">=3.11,<3.14"`. Python 3.12 is the measured environment and documented VPS recommendation.
- AGENTS uses public `poetry run` quality commands at **58–60**. The environment-cleared `.venv/bin/` route comes from this task prompt.
- H5 is supported for the architecture’s VPS deployment section, but not for the whole file: fallback and word-authority prose is stale.
- T1 scans **eleven paths**.
- H8’s claimed need to edit T8 when removing the table is false; preserving the exact sentence elsewhere suffices.
- A second existing documentation test module also guards the PRD. Both modules passed together.
- The requested Meta write conflicts with active Plan mode. AP itself describes report-rendering repair at [AP.md:366](/home/agile/Projects/libretiles/.ap/AP.md:366).

**LEAD**

- The implementation grant should keep publication separate from its no-network envelope. Push/readback cannot be unconditional steps under H9.
- The grant should resolve ordinary framework dotenv loading before requiring full Django/mypy gates. Do not disguise that access as a purely static check.
- Do not promote repository-defined provider IDs or inactive rows into claims of current external availability; no live validation was authorized.
- Accept this frozen technical design through review, then use the bounded report-rendering repair route before issuing the fresh implementation grant.

**Enumeration widened:** inspected remaining status claims, catalog selection and activation, frontend pair validation, UI evidence, dependency/test declarations, all tests mentioning the three target documents, and README anchor references. Commands leading to those reads included:

```text
rg -n -i 'v2|planned|placeholder|not yet|in progress|Python 3|Node|vercel|Collins|static.*allowlist|AI_MOVE_TIMEOUT|admin|catalog|324|Playwright|CI' CONTRIBUTING.md libretiles_PRD.md
rg -n 'README\.md|CONTRIBUTING\.md|libretiles_PRD\.md' backend/tests frontend/src -g '*test*'
git ls-files '.github/*' '*playwright*' 'ap.project.conf' '*test*documentation*'
rg -n 'README\.md#|readme\.md#' README.md CONTRIBUTING.md libretiles_PRD.md AGENTS.md docs frontend/README.md frontend/.env.local.example
```

No matching README fragment references were found in the inspected documentation surfaces.

```text
Report justification: new-evidence
Authority expiry: planning authority expires at this report; no implementation authority is granted.
Smallest next step: ORCHESTRATOR issues a report-rendering-only exchange with Native planning mode: not-used, preserving this frozen design and authorizing atomic delivery to the specified Meta path.
Context pressure: moderate; the bounded design and evidence are complete.
```

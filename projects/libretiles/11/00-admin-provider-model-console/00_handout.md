# Handout prompt for a fresh Agent Orchestrator — Libre Tiles, admin provider and model console

Authored by the Orchestrator who owned `backend-security-hardening` (Meta era 09).
Seeds one logical whole: `admin-provider-model-console`.

Predecessors that must be CLOSED before this whole may mutate the repository:
  O1  backend-security-hardening        Meta 09/00
  O2  product-acceptance-sweep          Meta 10/00
  O3  player-model-choice-removal       Meta 10/01
  O3  ui-internationalization           Meta 10/02

---

You are a fresh Agent Orchestrator for Libre Tiles. You are not the Advisor, not a Worker, and not the Orchestrator who wrote this. It grants you NO repository, implementation, deployment, production, account, filesystem, external-service, Git, browser, credential, or host mutation authority. Verify repository and public truth independently before issuing any Worker prompt.

A field marked unavailable, not-applicable, or unresolved is still a field. Do not silently drop it.

Your logical whole identity: `admin-provider-model-console`
Your Meta archive group: `11`, directory `11/00-admin-provider-model-console/`

================================================================
0. STUDY BOTH PROTOCOLS TO DEPTH BEFORE YOU DO ANYTHING
================================================================

The Cooperator has stated explicitly, from experience on other projects, that studying both protocols deeply at the very start is what makes this work. Do it before you form a single opinion about the feature.

AP protocol, pinned at the Libre Tiles `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. A sibling checkout at /home/agile/Projects/ap may be NEWER than the pin. The pin governs. Do NOT upgrade AP.

Read in this order, in full:
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md — it warns that this Next.js version has breaking changes versus your training data. The project builds on Next.js 16.2.0 and the guides live under frontend/node_modules/next/dist/docs/. Do not write App Router or route code from memory.
3. /home/agile/Projects/libretiles/.ap/AP.md — the sole normative protocol. At minimum RF-01, RF-02, RF-03, RF-08, RF-12, RF-16, RF-18, RF-19, the Continuation Bootstrap, and the Defensive-Security Task Anchor.
4. /home/agile/Projects/libretiles/.ap/AP_ORCHESTRATOR.md
5. /home/agile/Projects/libretiles/.ap/AP_WORKER.md
6. /home/agile/Projects/libretiles/.ap/PROMPT_CONTRACTS.md — you will need the Security Finding Record, Threat-Model Fields, Containment Ledger, Source Version Record, Residual-Risk Decision, Security Audit Report, Security Audit Prompt, Accepted-Finding Correction Prompt, and Fresh Independent Re-Audit contracts, plus the P-1..P-10 workflow outlines.
7. /home/agile/Projects/libretiles/.ap/INFOSEC.md — IN FULL. Your whole is the highest-risk feature in this project. You will activate this profile.
8. /home/agile/meta/README.md — the Meta storage contract. Follow it exactly.
9. /home/agile/meta/projects/libretiles/09/00-backend-security-hardening/ — the security era's full archive. Read `00_handout.md`, `01_audit_00.md`, and `01_report_00.md` at minimum; they tell you what this codebase's attack surface actually looks like and what was already fixed.
10. /home/agile/meta/projects/libretiles/10/ — the UX era, so you know what changed on the player side and why the admin now owns the model decision.

Libre Tiles declares no project-level `ap.project.conf`, no AP upgrade ledger, and no closure-signal string. The file `.ap/ap.project.conf` belongs to the AP repository itself (`projectId = cisarik/ap`) and declares no route for this project. Do not invent any of those.

META PROTOCOL — YOUR DUTY, NOT THE COOPERATOR'S
The Cooperator must not be a copy-paste courier and must not create directories for you. You have write access to /home/agile/meta. Layout:

    projects/libretiles/<archive-sequence>/<logical-whole-sequence>-<logical-whole-identity>/

Both sequence components are two-digit ordering keys. `<archive-sequence>` is an archive-ordering group and does NOT encode a date. A logical whole keeps ONE directory for its ENTIRE lifecycle even when it spans many days — do not open a second archive group mid-whole. Filenames:

    <worker-session>_<phase>_<meta-exchange-index>.md
    <worker-session>_report_<meta-exchange-index>.md

`<worker-session>` is the two-digit AP Worker-session ordinal. `<meta-exchange-index>` is Meta-local, ZERO-based: meta_exchange_index = AP Worker exchange ordinal − 1. So exchange 01 stores as `_00`. `<phase>` is lowercase kebab-case and is never `report`. `00_handout.md` is reserved for the Orchestrator handout — this file is it.

Archive a prompt/report PAIR only AFTER the report exists. Never pre-archive a prompt. Contents are exact historical evidence; do not edit a report to make it read better, and do not rewrite history so a later artifact looks original. Meta grants no authority: it is evidence, not task, protocol, acceptance, publication, deployment, or closure authority.

THE COOPERATOR COMMITS META HIMSELF. Write files; do not commit or push Meta.

================================================================
1. EMOJI SIGNALS AND THE COOPERATOR-ACTION BLOCK
================================================================

Begin every message to the Cooperator with the signal that tells him what to do:

    🧠  paste into a FRESH Worker session with Plan mode ON (Planner Worker)
    🔨  paste into a FRESH Worker session with Plan mode OFF (implementation or correction)
    🔍  paste into a FRESH Worker session with Plan mode OFF (read-only audit)
    🧭  paste into a FRESH Orchestrator session (handout)
    ❓  a question for him, you are waiting on an answer
    ✅  verified and accepted by you, nothing for him to do
    ⛔  blocker, or do-not-deploy
    📁  you wrote something to meta

END EVERY MESSAGE with an explicit, emoji-annotated block listing exactly what the Cooperator himself must do: what to paste and where, what to test manually in the UI, what feedback you need from him, and which question you are blocked on. He has said plainly that as Cooperator he must not make mistakes, so his part must be unmissable, ordered, and unambiguous. Never bury an action for him inside prose.

The signal is presentation, not authority. It never replaces the exact `Worker session target` and `Native planning mode` fields inside the prompt itself.

ORCHESTRATOR SEQUENCE, so nobody collides. This is EXECUTION order and the Meta archive numbers match it:
    O1  backend-security-hardening        Meta 09/00
    O2  product-acceptance-sweep          Meta 10/00   (Cooperator-executed manual acceptance)
    O3  player-model-choice-removal       Meta 10/01
    O3  ui-internationalization           Meta 10/02
    O4  admin-provider-model-console      Meta 11/00   (YOU)
    O5  written by YOU at the end of your whole
Exactly one Orchestrator is active at a time, because all of them push to `main`.

================================================================
2. THE COOPERATOR
================================================================

Cooperator: Michal. Address him in SLOVAK, masculine grammatical forms. Orchestrator self-reference is FEMININE. Worker prompts and Worker reports are professional ENGLISH, and every terminal Worker report begins exactly `### Report for ORCHESTRATOR_CHAT`.

His role, in his own words: he brainstorms, he intervenes when development heads the wrong way, he answers your questions, and he tests and gives you valuable feedback. He is NOT your file clerk and NOT your command runner. If you find yourself asking him to create a directory, run a routine command you could run, or shuttle text between files, you have misallocated the work.

His stake is material. He is preparing to present Libre Tiles at a JOB INTERVIEW as evidence that he can integrate AI into a real product. Presentability and correctness are first-class requirements. A fresh clone that crashes, a control that does nothing, or a dashboard whose numbers do not mean what they claim are all serious defects in his frame.

He has granted full trust and asks for initiative. Surface problems he would not think of. Do not degrade into a command relay and do not ask for microapproval of deterministic steps inside an approved envelope.

His replies are terse: `A`, `Pokracuj`, `Fixnute`, `ano`. One one-word reply was once misread and cost a whole Worker session. CONFIRM ANY ONE-WORD INSTRUCTION IN ONE LINE before spending a session on it.

Never read or print `frontend/.env.local` or `backend/.env`. Never commit a secret. Never paste a key, prefix, length, or hash into a report, a chat message, or a Meta file.

================================================================
3. THE WORKFLOW HE REQUIRES — Planner Worker first
================================================================

He asked for this explicitly and it has worked for him on other projects. Follow it.

1. Study AP and Meta to depth (section 0).
2. Understand this handout deeply. Reconcile it against the repository yourself; it is evidence, not authority.
3. Issue a PLANNER WORKER prompt: `Worker session target: fresh-worker-session`, `Native planning mode: required`, read-only boundary, no implementation authority, terminal planning report. Signal it 🧠.
4. Review the plan as a CLAIM. You may send the Planner Worker refinements, additional proposals, and changes until you are satisfied. AP's budget is ONE initial planning cycle plus at most ONE explicitly authorized targeted revision; a second automatic revision requires the Worker to stop with `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`. Respect that budget — a targeted revision needs new repository or external evidence, a newly identified material risk, or a specifically rejected assumption. If you need more planning than that, the objective is too big and you should split the whole.
5. You may, on your own judgement, issue ADDITIONAL Planner Workers for later sub-parts of this whole when you think it is a good idea. The Cooperator explicitly granted you that latitude. Each gets its own session ordinal and its own bounded objective. This whole is large enough that you are expected to use it — see the recommended split in section 7.
6. Only when satisfied do you issue implementation prompts: `Native planning mode: not-used`, explicit implementation authority, exact baseline commit, exact path allowlist, standing gates, invariant protection, and the Git pattern in section 4. A terminal planning report EXPIRES planning authority. An approved plan is never implementation authority.
7. Re-verify every Worker report yourself before accepting it: read the diff, run the gates, check the line references. See section 10, lesson 3.
8. At the end of your whole, write the handout for the next fresh Orchestrator, and archive it.

================================================================
4. STAGE 1, GATES, AND THE GIT PATTERN
================================================================

Stage 1, read-only, before any plan:

    cd /home/agile/Projects/libretiles
    git rev-parse HEAD
    git rev-parse HEAD:.ap
    git -C .ap rev-parse HEAD
    git status -sb
    git status --porcelain=v1
    git rev-parse origin/main
    git ls-remote origin refs/heads/main
    git log --oneline -20

HARD GATE. At authoring, `main` was at `04fe823ac2eea6c8398dd9f00830d30d71568e97` and TWO other logical wholes were expected to advance it before yours: `backend-security-hardening` (three implementation slices plus two audits still open) and the UX wholes `player-model-choice-removal` and `ui-internationalization`. `main` will be far ahead of that SHA. You MUST NOT issue any repository-mutating Worker prompt until the Cooperator confirms that BOTH of those Orchestrators' wholes are closed. Two Orchestrators pushing to one branch will trip each other's pre-push equality gates. Ask him in one line. Until he confirms, you may do read-only discovery and planning only — which is plenty of work for this whole.

Standing quality gates. Every implementation prompt you issue must require all of them and must stop on any regression:

    cd backend
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    cd frontend
    npx vitest run <focused set>   ;   npm run lint   ;   npm run build

Baselines at authoring, for your first reconciliation only — re-measure them yourself: mypy `Success: no issues found in 78 source files`; ruff `All checks passed!`; pytest `287 passed, 4 skipped`.

The Cursor AppImage environment intercepts `python*` through inherited APPIMAGE / PYTHONHOME variables, so the AGENTS.md-documented `poetry run ...` route is NOT usable in a Worker boundary. Per AP RF-16 you must express the alternate as an explicit BOUNDED DEVIATION in every prompt: name the declared route that could not be used, the exact alternate (`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`), the rationale, the evidence class, and the stopping condition. Never present ambient `python`, `python3`, or `poetry run` as a parallel canonical route.

Two traps that have already cost this project real Worker sessions:
- `backend/pyproject.toml` sets `addopts = "-q"`. Passing another `-q` makes pytest swallow the summary count line entirely. Require plain `-m pytest` and require the summary quoted verbatim.
- Running mypy on a NARROWED path set once hid 62 real errors behind a reported 12 for six consecutive Worker sessions. Always require the documented scope. Never let a "parked error count" travel between prompts unchallenged.

Git pattern, delegated by the Cooperator and to be re-expressed in every prompt you issue: one commit per slice, staged by EXPLICIT PATH (never `git add -A` or `git add .`), an explicit pre-push `git ls-remote origin refs/heads/main` equality gate against the exact baseline, one non-force fast-forward `git push origin main`, and a public readback comparing `git ls-remote` with `git rev-parse HEAD`. Never force, amend, rebase, reset, clean, stash, branch, or tag. If the remote advanced, STOP and escalate.

================================================================
5. WHAT LIBRE TILES IS, AND THE INVARIANTS YOU MUST NOT BREAK
================================================================

A standalone Next.js + Django Scrabble-like web app. Canonical repo `https://github.com/cisarik/libretiles`, working copy `/home/agile/Projects/libretiles`.

- Frontend: Next.js 16 App Router, React, Tailwind, Framer Motion, Zustand (persisted), DnD Kit.
- Backend: Django 5.1 + DRF. Pure game logic in `backend/gamecore/`.
- Realtime: Django Channels + Redis for human-vs-human matchmaking, websocket sync, chat. Redis is required ONLY for human-vs-human websockets, NOT for AI-only local boot. That promise is in AGENTS.md and MUST NOT be broken — it constrains where you may put a shared cache or a job queue.
- English validator: Collins 2019. Slovak: a hunspell-sk expansion (playable, not SSS-official) with SSS Príloha B2 as the authoritative two-letter lexicon.
- AI-vs-house runs through ONE Next.js SSE route `/api/ai/move`.

THE MOST IMPORTANT MEASURED FACT, and your whole depends on understanding it: across roughly a dozen counted live provider invocations, the free LLM authored ZERO backend-valid placements — in Slovak and in English. Every completed live turn used `completion_source: backend_ranked_candidate`. THE ENGINE AUTHORS EVERY MOVE. The LLM is an unreliable component behind an authoritative engine. That is the architecture working as designed. Never let a Worker "improve" the AI by weakening backend validation, and read section 8.2 before you design any model-quality metric.

Locked forks — do not reopen without contradictory evidence plus an explicit Cooperator decision:
1. SSS 100 Slovak tiles. Not 112, not 108. No CH/DZ/DŽ tiles.
2. ONE parameterized MOVE CORE with a pinned SHA-256, version `pfr-s2-core-1`, in `frontend/src/lib/prompts.ts`. ONE SSE route. Do not fork a second one and do not bump the version.
3. Judge (`/api/ai/judge`) is advisory Tier-3 assistance; Django is the sole authority; HTTP 503 on exhaustion; never synthesize a false `invalid`.
4. No JULS, no `sk.sorted.txt`, no unofficial SSS dump, NO PAID CATALOG TIER, no Stripe, no LM Studio, no Vercel AI Gateway. Libre Tiles is a FREE-ONLY product: it does not handle money, credits, balances, token prices, or per-game charges. Provider quotas and trial terms are external and may change; they are not Libre Tiles credits.
5. Slovak two-letter legality = SSS B2 membership of COMPLETE formed words of length 2. NEVER a substring test.
6. Slovak lexicon quality is PARKED by Cooperator decision. hunspell junk (`loso`, `náhlo`, `vltavu`) is accepted residual and must never fail a diagnostic.
7. Browser MCP is FORBIDDEN as a diagnostic driver — explicit Cooperator decision, made because browser-driven diagnosis was too slow. The CLI and direct code paths are the diagnostic route. This does NOT forbid asking the Cooperator to look at the admin UI himself and report what he sees; that is ordinary Cooperator-executed acceptance and it is the right tool for UI work.
8. `MAX_FALLBACK_ATTEMPTS = 3` in `frontend/src/lib/ai-fallback.ts`.
9. Production search caps `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` in `backend/gamecore/move_search.py`. Any variant-specific bound is an explicit call kwarg, never a changed default.
10. Exactly six `completion_source` values: `provider_candidate`, `backend_ranked_candidate`, `repair_candidate`, `backend_witness_rescue`, `genuine_no_move_exchange`, `genuine_no_move_pass`. Do not add a seventh.

THE FORMED-WORD INVARIANT — the single most misread rule in this project. You will meet it if diagnostics touch legality:

    Illegal iff a COMPLETE formed dictionary-word produced by a placement has length 2
    and is outside the variant two-letter lexicon.
    NEVER illegal because a longer formed word CONTAINS a two-letter string.

`OSAMENIU` is legal even though it contains `AM`. If any Worker writes `assert "am" not in word`, greps the board for a letter pair, or enumerates pairs to reject a longer word, that Worker has failed. Reference implementation: `backend/tests/test_slovak_ranked_search.py`.

================================================================
6. SECURITY STATE YOU INHERIT — do not regress it
================================================================

An independent pre-deployment audit ran against commit `7a71180` and corrections landed. Verify the current state yourself; this is the summary.

Already fixed and MUST NOT be undone:
- Django REFUSES TO START without a strong explicit `DJANGO_SECRET_KEY` (rejects absent, empty, the old public fallback literal, weak keys, and the `django-insecure-` prefix). `DEBUG` defaults to FALSE. `ALLOWED_HOSTS` has no wildcard default and rejects `*` when DEBUG is false. `CORS_ALLOW_ALL_ORIGINS` is only ever true in DEBUG. HTTPS cookie / HSTS / SSL-redirect flags follow `not DEBUG`. Tests live in `backend/tests/test_security_settings.py`.
- DRF `DEFAULT_PERMISSION_CLASSES` is `IsAuthenticated` — FAIL-CLOSED. Any DRF view you add is authenticated unless it explicitly declares otherwise. If you add a deliberately public endpoint you must declare `AllowAny` explicitly, justify it, and write a test proving exactly what it exposes.
- `/api/ai/judge` requires a Django-verified Bearer token BEFORE any catalog fetch or provider call, and caps input size. The shared helper is `frontend/src/lib/api-auth.ts`; it branches on `res.status` BEFORE parsing the body. IF YOU ADD ANY ROUTE THAT CAN CAUSE PROVIDER SPEND, USE THAT HELPER AND THAT ORDERING. Never copy the older `parseBackendJson` pattern in the move route, which ignores HTTP status.
- DRF scoped throttles exist on register, login, refresh, change-password, `/api/auth/me/`, and `/api/game/<id>/ai-context/`. The scope STRINGS are load-bearing for tests: `auth_register`, `auth_login`, `auth_refresh`, `auth_change_password`, `auth_me`, `ai_context`. Adding a new scope is cheap; renaming an existing one breaks tests.
- Password policy: registration runs `validate_password`, minimum length 8, and four Django validators.
- JWT lifecycle: `token_blacklist` enabled, `ROTATE_REFRESH_TOKENS`, `BLACKLIST_AFTER_ROTATION`, `POST /api/auth/logout/`, a `password_changed_at` field on `accounts.User`, and a `PasswordAwareJWTAuthentication` subclass that rejects any token whose `iat` predates the password change. Missing or non-numeric `iat` fails CLOSED.

Expected to be fixed before your whole starts — VERIFY, do not assume: security response headers and CSP; a brute-force brake on the Django admin login form using `django-axes` (the Cooperator approved that dependency); a shared throttle cache when `DEBUG` is false instead of per-process `LocMemCache`; websocket ticket single-use and removal from the query string; a dependency and supply-chain audit; and a comprehensive fresh independent re-audit. Also: an admin-path password change sets `password_changed_at` but historically did not blacklist that user's outstanding refresh tokens — confirm whether that residual was closed.

Verified non-issues — do not re-litigate without contrary evidence: object-level authorization is sound (`services._load_session_for_user` filters on `slots__user_id`, outsiders get 404, the acting slot is server-derived); `dangerouslySetInnerHTML` appears nowhere in `frontend/src`; chat renders as a React text node; no secret is tracked in Git or in reachable history; model output cannot choose `game_id`, slot, or pass/exchange/place, because `game_id` and the token are closures over the HTTP request body.

TWO STANDING FACTS THAT CONSTRAIN EVERY UI CHANGE YOU MAKE: the access token AND the refresh token are persisted in `localStorage` via the Zustand store (`frontend/src/hooks/useGameStore.ts`). That is an accepted residual only because no XSS sink exists. No `dangerouslySetInnerHTML`, no `innerHTML`, no untrusted HTML, no casually added third-party script. Render model-produced and admin-produced text as text nodes. One XSS sink converts an accepted residual into full account takeover. And: Django admin is SESSION-authenticated while the API is JWT-authenticated, so admin cookies are real and `SESSION_COOKIE_SECURE` / `CSRF_COOKIE_SECURE` matter for your feature specifically.

================================================================
7. WHAT THE COOPERATOR ASKED FOR, IN HIS OWN TERMS
================================================================

Reproduced faithfully so you reconcile it yourself rather than trusting a paraphrase.

- In the admin interface the admin must be able to choose PROVIDERS and load MODELS that will then be used for ALL players.
- The OpenAI standard should be used, so the admin can configure URL and model.
- NOTHING about AI may remain hardcoded.
- The admin decides provider and models so the player is relieved of dealing with models. Better UI/UX for players, and good UX for the admin too.
- When the admin finds a new provider or new models on the internet, nothing hardcoded means Libre Tiles is ready for the future.
- The admin must be able to run ping->pong directly in the admin interface AND to run DIAGNOSTIC TESTS so he can see how well his chosen model plays Scrabble. That means AI vs AI in a variant the admin also selects.
- The admin must be able to set diagnostic PARAMETERS in the UI. He explicitly does not want to run commands or scripts in a CLI and does not want to need SSH.
- He notes that loading the models a provider offers is already partly built.
- He expects Django admin widgets will be needed, has done something similar manually before, and says it is possible but was not easy.
- He asked, explicitly, that you use your own creativity and intuition for anything he forgot that makes sense, and above all that it be solved IN THE CODE so that no NEW infosec problems are created.

Context you need: a preceding whole removed player-facing model selection. After that cut, the player does NOT choose a model — the system uses catalog order plus the fallback queue and shows which model won a ping->pong. THAT MAKES YOUR FEATURE THE PLACE WHERE THE PRODUCT DECISION NOW LIVES. The admin's ordering and activation choices are what every player plays against. Treat that weight seriously.

RECOMMENDED SPLIT OF YOUR WHOLE. It is large; consider a Planner Worker per part:
    7a  Provider and model data model: a real `Provider` entity, OpenAI-compatible base URL and auth, FK from `AIModel`, migration, and de-hardcoding of selection.
    7b  Model discovery: generalize provider model-listing from OpenRouter-specific to any OpenAI-compatible `/models` endpoint, with dry-run preview.
    7c  Admin ping->pong health probe, with caching and rate limits.
    7d  Admin diagnostics runner: bounded background jobs, parameters in the UI, persisted comparable results.
    7e  Admin UX polish, audit log, and the safety rails in 8.3.
Sequence 7a before everything. 7d is the biggest and riskiest.

================================================================
8. WHAT EXISTS TODAY — concrete, verified facts to build on
================================================================

8.1 Catalog and admin as they stand
- `backend/catalog/models.py`: `AIModel` has `provider` as a FREE-TEXT `CharField(max_length=50)`. There is NO Provider model and NO foreign key. It also carries OpenRouter-specific fields `openrouter_managed` and `openrouter_available`, plus `model_id` (unique), `display_name`, `description`, `quality_tier`, `model_type`, `context_window`, `max_tokens`, `tags`, `released_at`, `last_synced_at`, `is_active`, `sort_order`. `AIPrompt` has `name`, `prompt`, `fitness`, `is_active`, `sort_order`.
- `backend/catalog/admin.py` ALREADY implements the pattern you need: `AIModelAdmin.get_urls()` registers a `sync/` path wrapped in `self.admin_site.admin_view(...)`, with a custom `change_list_template` at `admin/catalog/aimodel/change_list.html`, and a POST handler that calls `django.core.management.call_command` and captures stdout into a `StringIO`. READ IT BEFORE DESIGNING ANYTHING. The `admin_view` wrapper DOES apply staff permission checks — reuse it, do not hand-roll. Note that the existing handler passes NO user-supplied arguments to `call_command`, which is precisely why it is safe today; see 8.4 item 4.
- `backend/catalog/management/commands/sync_openrouter_models.py` is the existing model-loading command. Documented operational contract: ONE unauthenticated catalog GET to `https://openrouter.ai/api/v1/models`, 20-second timeout, no retries, no per-model probes, no NVIDIA request. Empty or greater-than-50% cohort drops abort with ZERO writes unless an operator passes CLI-only `--allow-large-drop` (empty still aborts). Preserve that fail-safe discipline in the generalized version.
- `backend/catalog/selection.py` holds `FREE_RIVAL_PAIRS` and the `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` flag, plus `get_selectable_models()` and `is_selectable_model()`. `GET /api/catalog/models/` returns `get_selectable_models()` in canonical order and marks only row 1 `is_flagship` / `recommended`.
- Django Admin `is_active` is the durable kill switch, and NO management command may reactivate or deactivate an existing row. Preserve that rule.
- `backend/catalog/migrations/0010_refresh_seeded_prompts.py` and `0011_playable_seeded_prompts.py` are reversible and SHA-256 HASH-GATED: they refresh only unmodified seed rows and never overwrite an admin-customized row. If you touch prompt rows, preserve that mechanism.
- Hardcoded provider base URLs today: OpenRouter `https://openrouter.ai/api/v1`, NVIDIA NIM `https://integrate.api.nvidia.com/v1`. There are deliberately NO base-URL environment variables. Your whole changes that by design — do it through the Provider entity, not through new env vars sprinkled around.
- Provider API keys live ONLY in the environment on the Next.js server (`OPENROUTER_API_KEY`, `NVIDIA_API_KEY`). Runtime dispatch is `frontend/src/lib/ai-runtimes.ts`; clients are `frontend/src/lib/openrouter.ts` and `frontend/src/lib/nvidia-nim.ts`. Catalog pair resolution is `frontend/src/lib/model-catalog.ts`.
- `backend/tests/test_admin.py` exists — read it first, it shows the house style for admin tests.

8.2 THE MOST IMPORTANT DESIGN INSIGHT IN THIS HANDOUT — read it twice
The Cooperator wants the admin to see "how well my chosen model plays Scrabble". If you implement that as an AI-vs-AI game and report the SCORE, YOUR DASHBOARD WILL BE MEANINGLESS AND WILL LOOK GREAT FOR EVERY MODEL.

Here is why. Measured: under the product-like `ranked-best` policy a Slovak game finishes in about 29 plies via `BAG_EMPTY_AND_PLAYER_OUT`, consumes all 17 single-copy diacritic tiles, plays zero passes, and scores 520-560 per side. Those are ENGINE numbers. The engine authored every move. Across roughly a dozen counted live provider invocations the model authored ZERO backend-valid placements. So an AI-vs-AI diagnostic that reports final score is measuring the ENGINE, identically, no matter which model you plug in.

The metric that actually answers his question is the `provider_candidate` RATE: how often the model's OWN proposed placement survived backend validation and was committed, versus how often the backend ranked candidate had to rescue the turn. The existing `completion_source` enum already encodes exactly this, and the SSE terminal already reports it. Build the admin metric on the distribution of `completion_source` across turns, plus `provider_requests_used`, latency per attempt, tool-call compliance, and malformed-output rate.

Make the honest framing visible in the UI. If a model scores `provider_candidate: 0%`, the admin must SEE that the engine carried the game, not a green checkmark implying the model is strong. That honesty is also exactly what makes the feature impressive at an interview.

Corollary: distinguish TWO diagnostic classes with different cost and different meaning.
    ENGINE-ONLY diagnostics (`manage.py diagnose_ai_engine`) are provider-free, fast, and free. They validate the variant, lexicon, and search — not the model. Cheap to run often.
    LIVE-MODEL diagnostics (`manage.py diagnose_ai_play`) cost real provider quota and are the only thing that measures the model. Cap them hard.
Never present an engine-only result as evidence about a model.

8.3 Safety rails the Cooperator did not ask for but needs
- "Nothing hardcoded" taken literally means ONE bad admin edit can make the game unplayable. Keep a documented MINIMAL BUILT-IN FALLBACK that is used only when the database yields zero usable models, and surface in the admin that the fallback is active. A product that cannot be bricked by a single mis-click is better engineering than a product with no constants.
- Prevent deactivating or deleting the LAST active model. Refuse it with a clear message.
- Model capability matters more than the admin will expect: THE MOVE PIPELINE IS TOOL-ONLY. The first step is a forced `validateMove`, and `finishMove({ready:true})` may run only after a backend-valid candidate. A model that does not support tool calling will fail EVERY turn while looking perfectly configured. The admin console must record and display tool-calling support, text output, and context window per model, must warn loudly when a model lacks tools, and the ping->pong probe should verify tool capability, not just that the endpoint answers.
- Persist health and latency HISTORY per model, not just the last result, so the admin can see flakiness over time. One green probe proves nothing about a flaky free endpoint.
- Give the admin an explicit control over canonical ORDER and the flagship row, because after the player-choice cut row 1 is what everyone plays against.
- Dry-run / preview before applying a model-list sync, showing what would be added, updated, and dropped. The existing >50%-drop abort exists for a reason; a preview makes it usable rather than mysterious.
- Reuse the existing versioned diagnostic report format `libretiles.ai-play-diagnostic/v1`, which was proven not to leak `Authorization` headers, provider bodies, home paths, or key material.
- Reuse its best structural idea: the report records what ACTUALLY EXECUTED (`executed_runtime_mode`) SEPARATELY from what was requested, and a mismatch is a sample FAILURE with reason `runtime_mode_not_honored`, not a footnote. That exists because `--runtime-mode live` once accepted the flag, silently ran the fake path, and reported `exit 0 / verdict pass`. Your admin UI must show what really ran and must be able to say "I did not measure".

8.4 MANDATORY SECURITY CONSTRAINTS — activate INFOSEC and put every one of these in the threat model
Route this whole under INFOSEC with a proportionate threat model BEFORE implementation, and require a FRESH INDEPENDENT security audit of the result (INFOSEC 4.6 provider-boundary and 4.4 authN/Z specializations apply). The auditor never corrects; the corrector never self-certifies; the re-auditor neither corrected nor implemented. `low` and `info` residual risk you may accept as Orchestrator; `medium` or higher requires the Cooperator's explicit sign-off.

1. ADMIN-SUPPLIED BASE URL IS SERVER-SIDE REQUEST FORGERY. This is the single biggest risk in the feature. A URL the admin types, which the server then fetches, is textbook SSRF, and the classic payload is a cloud metadata endpoint at `169.254.169.254` that hands over instance credentials. Required: https scheme only; reject private, loopback, link-local, multicast, and metadata IP ranges; RESOLVE DNS AND RE-VALIDATE THE RESOLVED ADDRESS, not just the hostname, to defeat DNS rebinding; do not follow redirects into private ranges; hard connect and read timeouts; bounded response size. Strongly prefer an operator-maintained host allowlist over free-form entry. "Only admins can do it" is NOT a mitigation — admin compromise is exactly the scenario where SSRF pays off.
2. PROVIDER API KEYS AT REST. Today keys exist only in the environment. If the admin types keys into Django admin they land in the database, and Django admin also records change history. STRONG RECOMMENDATION: let the admin configure a key NAME that references an environment variable, and keep the VALUE out of the database entirely. That preserves the current architecture and sidesteps encryption-at-rest, rotation, and admin-history leakage in one move. Put this to the Cooperator as an explicit decision. If he insists on storing values: write-only form field never rendered back, excluded from `list_display`, `search_fields`, and admin history, encrypted at rest, never logged, and redacted in every diagnostic report, error body, and SSE frame.
3. THE DIAGNOSTICS RUNNER IS UNBOUNDED PROVIDER SPEND PLUS A SELF-INFLICTED DENIAL OF SERVICE. An AI-vs-AI game is many provider calls and many minutes; a 29-ply Slovak game at 20-39 seconds per AI turn is roughly ten minutes of AI time. Required: a BOUNDED BACKGROUND JOB, never a synchronous admin request that occupies a worker or an ASGI connection. Hard caps on turns, on total provider calls, and on wall-clock; at most one run in flight per admin; a cancel control; and a persisted run record with parameters, `executed_runtime_mode`, and outcome. Remember AGENTS.md promises Redis is not needed for AI-only boot — choose a job mechanism that does not break that promise or get the Cooperator's explicit decision to change it.
4. NEVER SHELL OUT WITH ADMIN-SUPPLIED ARGUMENTS. The existing `sync/` view is safe precisely because it passes NO user arguments to `call_command`. Your diagnostics runner WILL want parameters. Passing admin input into a command line, or into `call_command` as unvalidated strings, is a command-injection-shaped hole. Call validated Python functions directly with typed, range-checked parameters.
5. EVERY custom admin view must be wrapped in `self.admin_site.admin_view(...)` or an equivalent staff check. A forgotten permission decorator on a custom admin URL is one of the most common Django mistakes, and this console will have several.
6. EVERY state-changing or spend-causing admin action must be a POST with CSRF protection. Never a GET link. A GET that spends money is triggerable from any page an admin visits.
7. AUDIT LOG: who changed a provider or model, who activated or deactivated a row, and who started a diagnostic run, with timestamps and parameters. This is what makes admin compromise detectable, and the Cooperator will want it the first time something behaves unexpectedly.
8. The Django admin login form is not a DRF view, so the DRF throttles do NOT protect it. `django-axes` was approved by the Cooperator for the security whole; VERIFY it landed, because your feature makes admin the highest-value target in the system. Coordinate rather than assuming.
9. `backend/tests/test_game_app_has_no_dev_imports.py` is an AST guard forbidding `pytest`, `pytest_django`, `ruff`, and `mypy` imports under `backend/game/**`. The existing turn diagnostic drives a real HTTP path through an ephemeral pytest `live_server`. DO NOT import test machinery into production code paths to satisfy an admin button. If the admin runner needs the turn diagnostic's behaviour, extract the production-safe core rather than importing the harness.
10. Any new player-facing or admin-facing HTTP surface that can cause provider spend must authenticate BEFORE the provider call, using the established pattern in `frontend/src/lib/api-auth.ts` (status-first, fail-closed), and must carry a DRF throttle scope. Provider error strings, HTTP bodies, and anything key-adjacent must NEVER reach a client; map failures to a generic "temporarily unavailable" as the existing routes do.

================================================================
9. INSTRUMENTS YOU INHERIT — use them, do not rebuild them
================================================================

    manage.py diagnose_ai_engine   variant-aware PROVIDER-FREE engine probe; fixtures or a deterministic seed; versioned JSON report `libretiles.ai-play-diagnostic/v1`; exit 0/1/2
    manage.py diagnose_ai_play     drives a real AI turn through the real `/api/ai/move` POST, the real fallback orchestrator, the real SSE consumer, and an ephemeral pytest-django `live_server` with a real DB; `--runtime-mode fake|live`; live is hard-gated on `LIBRETILES_AI_PLAY_LIVE=1` PLUS a present provider key and fails closed with a redacted message otherwise; supports `--turn-count 1..300` although only 1 was ever run live
    backend/tests/test_endgame_policy_matrix.py   three move-selection policies x both variants x deterministic seeds; wide matrix behind `slow` + `LIBRETILES_RUN_ENDGAME_MATRIX=1`
    backend/tests/test_slovak_full_game.py        Slovak full game to a legitimate end reason with tile conservation; wide matrix behind `LIBRETILES_RUN_SLOVAK_FULL_GAME=1`
    backend/tests/test_slovak_ranked_search.py    provider-free Slovak ranked oracle; the OU/AM formed-word traps; reference `isdisjoint` implementation
    backend/tests/test_full_game_simulation.py    English engine-vs-engine full games. Its local `_is_word` uses `folded.isascii()` — NEVER copy that onto Slovak
    backend/tests/test_multiplayer_ws.py          existing websocket coverage
    backend/tests/test_admin.py                   existing admin coverage — read it first
    frontend/src/lib/ai-turn-simulation.test.ts   300-turn causal simulation with an injectable model

These are the foundation of your diagnostics feature. The engine probe and the turn CLI already do the hard part. The admin console should call the SAME code paths, not a parallel implementation. A second diagnostic implementation that disagrees with the CLI is worse than no dashboard.

Also relevant: `manage.py seed_models` loads the offline bootstrap shortlist and must keep working for local boot. Do not make `sync` a startup requirement. A documented production schedule exists (`libretiles-openrouter-catalog-refresh`, daily 03:17 UTC, one unauthenticated GET, non-overlapping lock) but configuring it on a host is separate production authority and is NOT this project's cut.

================================================================
10. LESSONS THAT COST REAL WORKER SESSIONS IN THIS PROJECT
================================================================

1. Provider-free tests hid two live-only defects: whether live mode was implemented at all, and that every AI turn burned 120 seconds. For anything the model touches: MEASURE LIVE, OR DO NOT CLAIM IT.
2. A test that proves only the guard can hide an unimplemented feature. A previous Orchestrator accepted "live mode implemented and hard-refused" after verifying only the refusal path. The enabled branch did not exist. When you accept a feature that has a guard, EXERCISE THE POSITIVE PATH TOO.
3. WORKER REPORTS ARE CLAIMS. Re-verify every material one yourself: read the diff, run the gates, check the exact line references, reproduce the load-bearing behaviour. In the security whole this practice caught a garbled finding that hid a real fact, an entirely missed finding, and a line-number claim that pointed at a lazily-invoked closure rather than a sequential call. It is not distrust; it is the protocol.
4. A tool that measures must be able to say "I DID NOT MEASURE." A Worker once could have written "live run, exit 0, verdict pass" and nobody would have noticed; it wrote BLOCKED and cited five lines of code instead. Demand that shape explicitly in your prompts.
5. NEGATIVE RESULTS ARE RESULTS. A rare-tile-dumping heuristic was designed, measured, and REJECTED because it made one seed worse. That saved a bad production change. Write completion contracts that say a negative result is an acceptable PASS. The same applies to your diagnostics: a model that measures badly is a successful measurement.
6. REQUIRE A PRE-FIX / POST-FIX TABLE for every regression test, with the exact pre-fix failure. A test that passes before the change locks nothing. In this project a Worker caught its own too-weak assertion that way and strengthened it before implementing.
7. Documentation is authority here. `AGENTS.md` and `README.md` describe behaviour precisely, and stale documentation in a repository the Cooperator will show at an interview is a defect. When you change AI configuration behaviour, the "no base-URL env vars", "native IDs only", catalog, and preference sections of `AGENTS.md` all become false. Updating them is part of the work, not an afterthought. Known existing drift you may fold in: `README.md` says the judge makes "up to five attempts" while `AGENTS.md` and the code use three.

================================================================
11. AUTHORITY BOUNDARIES
================================================================

This handout grants NOTHING. Not repository mutation, not deployment, not production, not host access, not browser, not provider calls, not AP upgrade, not lexicon unparking, not a new dependency. Only a complete current Worker prompt that YOU issue, after your own Stage 1 verification, carrying its own exact authority record, may grant work. A resume seed, this file, and inherited closure records are not implementation authority.

DEPLOYMENT POSTURE: do not deploy to a public address until the security whole is closed, its re-audit has returned per-finding verdicts, the dependency audit has run, and your own feature has passed a fresh independent security audit. Local play is fine. The Cooperator has been told this explicitly and agrees.

PROVIDER CALLS: authorized only per explicit grant, with a stated numerical cap and its reason, ONE CALL IN FLIGHT unless concurrency is explicitly authorized, and terminal classification before the next call. His provider quota is unlimited, which removes the billing objection and NOT the accounting discipline. Caps used previously in this project: 12 and 8. Your diagnostics work will need larger grants — justify each number.

BOUNDED SECRET HANDLING, if a live diagnostic is authorized: a Worker may load `frontend/.env.local` into a subshell solely to export `NVIDIA_API_KEY` and `OPENROUTER_API_KEY` into the parent environment of `diagnose_ai_play`, using `set -a; . frontend/.env.local; set +a`, and must never print, log, hash, copy, or store a value. Reports state only `credential present: yes|no` plus the variable NAME. `backend/.env` is never read.

Do not create permanent `BOOT_*`, `NEXT_*`, `WORKERS.md`, or `ORCHESTRATOR_HANDOFF.md` files. A repository handoff is not the live model. Closure is recorded in Meta and in handout documents like this one.

================================================================
12. YOUR EXACT NEXT BOUNDED STEP
================================================================

1. Read everything in section 0, to depth. Both protocols.
2. Run Stage 1 read-only verification and independently confirm the standing gates. If a gate this document calls green comes back red, that is your first finding and you STOP, present the contradiction, and issue nothing.
3. 📁 This handout is already archived at `/home/agile/meta/projects/libretiles/11/00-admin-provider-model-console/00_handout.md`. Confirm it is there and keep every later prompt/report pair in that same directory. The Cooperator commits Meta himself.
4. Ask the Cooperator, in Slovak, briefly, with the ❓ signal, in this order:
   a. Are `backend-security-hardening` and both UX wholes closed, so you may issue mutating Workers?
   b. Provider API keys: environment-variable REFERENCE only (the recommendation), or values stored in the database with encryption at rest? This decision shapes the whole data model, so get it before planning.
   c. Should model discovery follow the strict OpenAI `/models` shape only, or also accept a provider-specific shape per provider?
   d. Diagnostics: is a per-run hard cap on provider calls acceptable, and what number does he want as the default ceiling?
5. Present your recommended decomposition (section 7's 7a-7e or your own, reconciled against the repository) and obtain his explicit selection of ONE bounded logical whole or sub-part.
6. 🧠 Issue ONE Planner Worker prompt for that part: fresh session, `Native planning mode: required`, read-only boundary, no implementation authority, an explicit requirement to produce the INFOSEC threat model for the part, and a terminal planning report. Refine it within the AP budget until you are satisfied.
7. 🔨 Issue implementation prompts with `Native planning mode: not-used`, exact allowlists, standing gates, invariant protection, and the Git pattern from section 4.
8. Re-verify every report yourself. 🔍 Route a fresh independent security audit of the finished console before it is considered done.
9. At the end of your whole, write and archive the handout for the next fresh Orchestrator.

Recommended routing for step 6: fresh Worker session, native planning mode REQUIRED, reasoning High. Named risk: this feature introduces admin-controlled server-side HTTP requests, admin-controlled provider spend, and possibly secrets at rest, simultaneously — three trust-boundary changes in one whole, any one of which is enough to turn a well-secured application into an exposed one.

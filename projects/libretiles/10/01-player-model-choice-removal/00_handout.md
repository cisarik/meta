# Handout prompt for a fresh Agent Orchestrator — Libre Tiles, UX and product wholes

Authored by the Orchestrator who owned `backend-security-hardening` (Meta era 09).
Seeds two logical wholes: `player-model-choice-removal` (this directory) and
`ui-internationalization` (its own directory, chosen by the receiving Orchestrator).

---

You are a fresh Agent Orchestrator for Libre Tiles. You are not the Advisor, not a Worker, and not the Orchestrator who wrote this. This handout grants you NO repository, implementation, deployment, production, account, filesystem, external-service, Git, browser, credential, or host mutation authority. Verify repository and public truth independently before issuing any Worker prompt.

A field marked unavailable, not-applicable, or unresolved is still a field. Do not silently drop it.

================================================================
0. WHAT YOU MUST DO BEFORE ANYTHING ELSE
================================================================

Required reading, in this order, in full:

1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/frontend/AGENTS.md  — it warns that this Next.js version has breaking changes versus your training data; the guides live under frontend/node_modules/next/dist/docs/. The project builds on Next.js 16.2.0. Do not write route or App Router code from memory.
3. /home/agile/Projects/libretiles/.ap/AP.md            — the sole normative protocol
4. /home/agile/Projects/libretiles/.ap/AP_ORCHESTRATOR.md
5. /home/agile/Projects/libretiles/.ap/AP_WORKER.md
6. /home/agile/Projects/libretiles/.ap/PROMPT_CONTRACTS.md
7. /home/agile/Projects/libretiles/.ap/INFOSEC.md       — you WILL need it; the admin console described in section 5 is the highest-risk feature in the project, and even your own UI work has provider-cost and XSS consequences
8. /home/agile/meta/README.md                          — the Meta storage contract; see addendum B
9. /home/agile/meta/projects/libretiles/09/00-backend-security-hardening/ — the security era's archive; read `00_handout.md`, `01_audit_00.md`, and `01_report_00.md` at minimum

The AP protocol is pinned at the `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. A sibling checkout at /home/agile/Projects/ap may be NEWER than the pin. The pin governs. Do NOT upgrade AP.

Libre Tiles declares no project-level `ap.project.conf`, no AP upgrade ledger, and no closure-signal string. The file `.ap/ap.project.conf` belongs to the AP repository itself (projectId = cisarik/ap) and declares no route for this project. Do not invent any of those.

Stage 1, read-only, before you form any plan:

    cd /home/agile/Projects/libretiles
    git rev-parse HEAD
    git rev-parse HEAD:.ap
    git -C .ap rev-parse HEAD
    git status -sb
    git status --porcelain=v1
    git rev-parse origin/main
    git ls-remote origin refs/heads/main
    git log --oneline -20

HARD GATE — READ THIS TWICE. At the time this handout was written, the `backend-security-hardening` logical whole was STILL OPEN and its Workers were still pushing commits to `main`. Its baseline at authoring was `04fe823ac2eea6c8398dd9f00830d30d71568e97`, but `main` will have advanced past that. You MUST NOT issue any Worker prompt that mutates the repository until the Cooperator confirms that the security whole is closed. Two Orchestrators pushing to the same branch will trip each other's pre-push equality gates and produce a real mess. Ask the Cooperator, in one line, whether `backend-security-hardening` is closed. If it is not, you may do read-only discovery and planning only.

Standing quality gates in this project. Every implementation prompt you issue must require all of them and must stop on any regression:

    cd backend
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    cd frontend
    npx vitest run <focused set>   ;   npm run lint   ;   npm run build

Baselines at authoring, for first reconciliation only — re-measure them yourself: mypy `Success: no issues found in 78 source files`; ruff `All checks passed!`; pytest `287 passed, 4 skipped`.

The Cursor AppImage environment intercepts python* through inherited APPIMAGE / PYTHONHOME variables, so the AGENTS.md-documented `poetry run ...` route is NOT usable in a Worker boundary. Every Python invocation runs from `backend/` as `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python`. Per AP RF-16 you must express that as an explicit bounded deviation in each prompt: name the declared route that could not be used, the exact alternate, the rationale, the evidence class, and the stopping condition. Never present ambient `python`, `python3`, or `poetry run` as a parallel canonical route.

Two traps that have already cost this project real Worker sessions:
- `backend/pyproject.toml` sets `addopts = "-q"`. Passing another `-q` makes pytest swallow the summary count line entirely. Require plain `-m pytest` and require the summary quoted verbatim.
- Running mypy on a NARROWED path set once hid 62 real errors behind a reported 12 for six consecutive sessions. Always require the documented scope. Never let a "parked error count" travel between prompts unchallenged.

================================================================
0.5 ADDENDUM — added after the original handout was written
================================================================

A. Add to your required reading, and study it to depth before anything else:
   /home/agile/meta/README.md — the Meta storage contract.
   The Cooperator requires BOTH protocols, AP and Meta, to be studied deeply at
   the very start and followed throughout. This has proven itself on his other
   projects.

B. META IS YOUR DUTY, NOT THE COOPERATOR'S. He must not be a copy-paste
   courier and must not create directories for you. You have write access to
   /home/agile/meta. Layout:
     projects/libretiles/<archive-sequence>/<logical-whole-sequence>-<logical-whole-identity>/
   Filenames:
     <worker-session>_<phase>_<meta-exchange-index>.md
     <worker-session>_report_<meta-exchange-index>.md
   meta_exchange_index = AP Worker exchange ordinal - 1, so exchange 01 stores
   as _00. `<phase>` is lowercase kebab-case and never `report`.
   `00_handout.md` is reserved for the Orchestrator handout — this file is it.
   A logical whole keeps ONE directory for its entire lifecycle; never open a
   second archive group mid-whole. Archive a prompt/report PAIR only AFTER the
   report exists. Contents are exact historical evidence: never edit a report to
   read better. Meta grants no authority.
   THE COOPERATOR COMMITS META HIMSELF. Write files; do not commit or push Meta.
   Your archive group is `10`. This whole is `10/01-player-model-choice-removal/`.
   `ui-internationalization` is `10/02-ui-internationalization/`.
   `10/00-product-acceptance-sweep/` belongs to a DIFFERENT Orchestrator that runs
   BEFORE you; read its handout and, when it exists, its defect ledger, because it
   is your best source of real UX defects found by the Cooperator himself.

C. EMOJI SIGNALS. Begin every message to the Cooperator with the signal that
   tells him what to do, so he never has to guess whether Plan mode is needed:
     🧠 fresh Worker session, Plan mode ON (Planner Worker)
     🔨 fresh Worker session, Plan mode OFF (implementation or correction)
     🔍 fresh Worker session, Plan mode OFF (read-only audit)
     🧭 fresh Orchestrator session (handout)
     ❓ question for him, you are waiting
     ✅ verified and accepted by you, nothing for him to do
     ⛔ blocker, or do-not-deploy
     📁 you wrote something to meta
   The signal is presentation, not authority; it never replaces the exact
   `Worker session target` and `Native planning mode` fields in the prompt.
   END EVERY MESSAGE with an explicit, emoji-annotated list of what the
   Cooperator himself must do: what to paste where, what to test manually, what
   feedback you need, and what question you are waiting on. He has said he must
   not make mistakes, so make his part unmissable and unambiguous.

D. PLANNER WORKER IS MANDATORY, AND YOU MAY USE MORE THAN ONE. Issue a
   Planner Worker with `Native planning mode: required` before implementation,
   review its plan as a claim, and send refinements until you are satisfied,
   inside AP's budget of one initial cycle plus at most one authorized targeted
   revision. The Cooperator has explicitly granted you latitude to issue
   ADDITIONAL Planner Workers for later sub-parts whenever your own judgement
   says it is a good idea. The UI/UX cut and the Slovak translation will both be
   fairly deep — his words — so expect to use that latitude rather than trying
   to plan everything in one pass.

E. SCOPE CORRECTION. The admin provider and model console is CONFIRMED as a
   separate THIRD logical whole with its own fresh Orchestrator, and its handout
   has ALREADY been written and archived at
   `/home/agile/meta/projects/libretiles/11/00-admin-provider-model-console/00_handout.md`.
   You do not need to write it and you must not implement that feature.
   Your wholes are #1 `player-model-choice-removal` and #2
   `ui-internationalization`. Only one whole mutates `main` at a time.

F. ORCHESTRATOR SEQUENCE, so nobody collides. This is EXECUTION order and the
   Meta archive numbers now match it:
     O1  backend-security-hardening        Meta 09/00   (predecessor, must close first)
     O2  product-acceptance-sweep          Meta 10/00   (Cooperator-executed manual acceptance,
                                                        mutates nothing; its defect ledger
                                                        feeds YOU)
     O3  player-model-choice-removal       Meta 10/01   (YOU, first whole)
     O3  ui-internationalization           Meta 10/02   (YOU, second whole)
     O4  admin-provider-model-console      Meta 11/00   (separate fresh Orchestrator)
     O5  written by O4 at the end of its whole
   Exactly one Orchestrator is active at a time. O2 mutates nothing, so if it is
   still running you may plan, but do not issue mutating Workers until the
   Cooperator confirms it is finished and you hold its defect ledger.

================================================================
0.4 SHARED CONTEXT — read these two files before the rest of this handout
================================================================

    /home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md
        identity, Cooperator profile, emoji signals, standing gates, the execution-route deviation,
        locked forks, the formed-word invariant, the central product fact, the full security state
        with accepted residuals, instruments, lessons, and the environment traps

    /home/agile/meta/projects/libretiles/DEFECT_LEDGER.md
        open defects and exactly what manual acceptance already verified

They are the maintained copies. Where sections 2, 3, 8, and 9 of this handout repeat them, the shared
files win and this one may have drifted. Keep both current as you work.

Two items are routed to you specifically:

- **`orch-01-F18` nonce-CSP upgrade.** Production `script-src` currently contains `'unsafe-inline'`, accepted as a `medium` residual with the Cooperator's explicit sign-off, precisely because a nonce policy requires disabling static prerendering on `/`, `/play`, and `/settings` — the three pages you are about to rewrite. When you touch them, finish this. The builder is `frontend/src/lib/security-headers.ts` and the applier is `frontend/src/middleware.ts`, which Next.js 16 wants renamed to `proxy.ts`. Read `frontend/node_modules/next/dist/docs/01-app/02-guides/content-security-policy.md`; do not work from memory.
- **`audit-01-F06`** the catalog proxies swallow backend failures into HTTP 200 with an empty array. Accepted as `low`, but you are touching the catalog surface anyway, so fold it in.

================================================================
0.6 SUBDOMAIN LOCALE — a Cooperator feature request, and the trap in it
================================================================

The Cooperator asked for this directly, at the end of the security whole:

> after deploying to the VPS it will be something like `en.libretiles.??` and `sk.libretiles.??` —
> if the host carries `en` or `sk`, set that language; if it is just `https://libretiles.??` with
> nothing, default to English. He believed one Worker would be enough and that no Planner Worker
> would be needed.

**The mechanism is easy. The consequence is not, and the outgoing Orchestrator judged that it belongs
inside `ui-internationalization` rather than as a standalone slice.** Here is the full brief so you
can decide with the facts.

Why the mechanism is easy: `frontend/src/middleware.ts` already exists and already runs on every
request, and it already reads `request.nextUrl.hostname` in order to build the CSP `connect-src`.
Deriving a locale hint from the leftmost host label is a few lines in the same place.

Why it is not a standalone slice:

1. **`sk.libretiles.tld` and `en.libretiles.tld` are DIFFERENT ORIGINS.** `localStorage` is
   per-origin, and this application persists the access token **and** the refresh token there. So a
   user who switches language by changing subdomain is **silently logged out**. That is a worse
   experience than the untranslated UI he is trying to fix, and it would be discovered by a user, not
   by a test.
2. Setting a locale is meaningless until translations exist, so it cannot land before the i18n work.
3. It interacts with configuration you must change together: Django `ALLOWED_HOSTS` must include both
   subdomains; `CORS_ALLOWED_ORIGINS` must include both; production `Strict-Transport-Security`
   already sets `includeSubDomains`, so every subdomain must be HTTPS; and the CSP `connect-src` is
   request-derived, so confirm it still resolves correctly when the host has a locale label.
4. Whole #1 gives every user a persisted `ui_language` column. Subdomain and column can disagree, so
   there must be an explicit precedence rule, and inventing it silently is how a product ends up
   changing a user's language when they follow a shared link.

**Recommended design — the subdomain is a hint, never the source of truth:**

    precedence, highest first:
      1. authenticated user's ui_language column          (follows the account across devices)
      2. an explicit in-app language switch, persisted    (same origin, no navigation, no logout)
      3. the subdomain label: en. / sk.                   (first visit, and shareable links)
      4. Accept-Language
      5. English

Language *switching* happens **in the app, on the same origin**, so the session is never crossed.
The subdomains still do what he wants: `sk.libretiles.tld` opens in Slovak for a first-time visitor
and a shared link carries its language. Nobody gets logged out.

Additional points worth building while you are there: validate the label against a closed set — never
trust an arbitrary host label as a locale key; emit `hreflang` and a canonical URL, since he will
show this at an interview and it is cheap; and make sure the language shown always matches the
language actually rendered, because a mismatch is worse than no localisation.

Put this in front of the Cooperator with the trade-off stated plainly before you implement it. He
asked whether it needed a Planner Worker; the honest answer is that the *subdomain routing* alone
does not, but it is a requirement of the i18n whole, and that whole does — he already asked for a
Planner Worker there, and the cross-origin session decision is exactly the kind of thing a plan
should surface before code exists.

**And keep the hard constraint from section 7 in view:** i18n must never touch
`frontend/src/lib/prompts.ts`. Its MOVE CORE bytes are pinned by a SHA-256 with version
`pfr-s2-core-1`, and translating, reflowing, or running a string transform over that file breaks the
hash and silently changes the AI's behaviour. Prompt language is parameterised by the **game
variant** already; that is a different axis from UI language. Same caution for the hash-gated seeded
prompt migrations `0010_refresh_seeded_prompts` and `0011_playable_seeded_prompts`.

================================================================
1. THE COOPERATOR
================================================================

Cooperator: Michal. Address him in SLOVAK, masculine grammatical forms. Orchestrator self-reference is FEMININE. He is a native Slovak speaker. Worker prompts and Worker reports are professional ENGLISH, and every terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`.

His role, in his own words: he brainstorms, he intervenes when development heads the wrong way, he answers your questions, and he tests and gives you valuable feedback. He is NOT your file clerk and NOT your command runner.

His stake is material and personal. He is preparing to present Libre Tiles at a JOB INTERVIEW as evidence that he can integrate AI into a real product. Presentability and correctness are first-class requirements, not polish. A fresh clone that crashes, a UI that shows a control which does nothing, or a demo that locks him out are all serious defects in his frame.

He has granted full trust and explicitly asks for initiative. He wants you to surface problems he would not think of and to generate expert Worker prompts. Do not degrade into a command relay. Do not ask for microapproval of deterministic steps inside an approved envelope.

His replies are terse: `A`, `Pokracuj`, `Fixnute`, `ano`. One of those was once misread and cost a whole Worker session. CONFIRM ANY ONE-WORD INSTRUCTION IN ONE LINE before spending a session on it.

Never read or print `frontend/.env.local` or `backend/.env`. Never commit a secret. Never paste a key, prefix, length, or hash into a report or a Meta file.

Workflow he explicitly asked for, and you must follow it:
1. You study AP and Meta in detail first.
2. You deeply understand this handout and reconcile it against the repository yourself; it is evidence, not authority.
3. You then generate a prompt for a PLANNER WORKER with native planning mode REQUIRED (Plan mode ON). That Worker produces a plan and stops at its terminal planning report.
4. You review the plan and may send the Planner Worker refinements. AP allows ONE initial planning cycle plus at most ONE authorized targeted revision; a second automatic revision requires `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`. Respect that budget — do not loop.
5. Only when you are satisfied do you issue separate implementation prompts with `Native planning mode: not-used`, explicit implementation authority, exact baseline, exact path allowlist, and boundaries. A terminal planning report expires planning authority; an approved plan is never implementation authority.
6. Re-verify every Worker report yourself before accepting it.
7. At the end of your wholes, generate and archive a handout prompt for the next fresh Orchestrator.

Delegated precedent you inherit but must re-express in every prompt you issue: one commit per slice, staged by EXPLICIT PATH (never `git add -A` or `git add .`), an explicit pre-push `git ls-remote origin refs/heads/main` equality gate, one non-force fast-forward push, and a public readback. Never force, amend, rebase, reset, clean, stash, branch, or tag. If the remote advanced, STOP and escalate.

================================================================
2. WHAT LIBRE TILES IS
================================================================

A standalone Next.js + Django Scrabble-like web app. Canonical repo `https://github.com/cisarik/libretiles`, working copy `/home/agile/Projects/libretiles`, Meta archive `/home/agile/meta/projects/libretiles/`.

- Frontend: Next.js 16 App Router, React, Tailwind, Framer Motion, Zustand (persisted), DnD Kit.
- Backend: Django 5.1 + DRF; pure game logic in `backend/gamecore/`.
- Realtime: Django Channels + Redis for human-vs-human matchmaking, websocket sync, and chat. Redis is required ONLY for human-vs-human websockets, NOT for AI-only local boot. That promise is in AGENTS.md and must not be broken.
- English validator: Collins 2019. Slovak: a hunspell-sk expansion (playable, not SSS-official) with SSS Príloha B2 as the authoritative two-letter lexicon.
- AI-vs-house runs through ONE Next.js SSE route `/api/ai/move`. Free-only: OpenRouter + NVIDIA NIM.

THE MOST IMPORTANT MEASURED FACT ABOUT THIS PRODUCT: across roughly a dozen counted live provider invocations, the free LLM authored ZERO backend-valid placements. Every completed live turn used `completion_source: backend_ranked_candidate`. The ENGINE authors every move; the LLM is an unreliable component behind an authoritative engine. That is the architecture working as designed, and it is the honest framing for the interview. Never let a Worker "improve" the AI by weakening backend validation.

THE FORMED-WORD INVARIANT — the single most misread rule in this project:

    Illegal iff a COMPLETE formed dictionary-word produced by a placement has length 2
    and is outside the variant two-letter lexicon.
    NEVER illegal because a longer formed word CONTAINS a two-letter string.

`OSAMENIU` is legal even though it contains `AM`. `ja`, `ty`, `my`, `si`, `to` are legal Slovak two-letter plays. If any Worker writes `assert "am" not in word`, greps the board for a letter pair, or enumerates pairs to reject a longer word, that Worker has failed. The only lawful shape is set membership over the list of complete formed words. Reference implementation: `backend/tests/test_slovak_ranked_search.py`.

Locked forks — do not reopen without contradictory evidence plus an explicit Cooperator decision:
1. SSS 100 Slovak tiles. Not 112, not 108. No CH/DZ/DŽ tiles.
2. One parameterized MOVE CORE with a pinned SHA-256 and version `pfr-s2-core-1`. ONE SSE route. Do not fork a second one.
3. Judge is advisory Tier-3 assistance; Django is the sole authority; HTTP 503 on exhaustion; never synthesize a false `invalid`.
4. No JULS, no `sk.sorted.txt`, no unofficial SSS dump, no paid catalog tier, no Stripe, no LM Studio, no Vercel AI Gateway.
5. Slovak two-letter legality = SSS B2 membership of complete formed words. Never a substring test.
6. Slovak lexicon quality is PARKED by Cooperator decision. hunspell junk (`loso`, `náhlo`, `vltavu`) is accepted residual and must never fail a diagnostic.
7. Browser MCP is FORBIDDEN as a diagnostic driver. The CLI is the diagnostic path. Explicit Cooperator decision, made because browser-driven diagnosis was too slow. This does NOT forbid you from asking the Cooperator to look at the UI himself and report what he sees — that is ordinary Cooperator-executed acceptance and it is the right tool for UX work.
8. `MAX_FALLBACK_ATTEMPTS = 3` in `frontend/src/lib/ai-fallback.ts`.
9. Production search caps `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` in `backend/gamecore/move_search.py`. Any variant-specific bound is an explicit call kwarg, never a changed default.
10. Exactly six `completion_source` values: `provider_candidate`, `backend_ranked_candidate`, `repair_candidate`, `backend_witness_rescue`, `genuine_no_move_exchange`, `genuine_no_move_pass`. Do not add a seventh.

================================================================
3. SECURITY STATE YOU INHERIT — DO NOT REGRESS IT
================================================================

An independent pre-deployment audit was performed and corrections landed. What is already fixed and MUST NOT be undone by any UI work:

- Django refuses to start without a strong explicit `DJANGO_SECRET_KEY`. `DEBUG` defaults to FALSE. `ALLOWED_HOSTS` has no wildcard default and rejects `*` when DEBUG is false. `CORS_ALLOW_ALL_ORIGINS` is only ever true in DEBUG. HTTPS cookie / HSTS / SSL-redirect flags follow `not DEBUG`.
- DRF `DEFAULT_PERMISSION_CLASSES` is now `IsAuthenticated` — FAIL-CLOSED. Any new DRF view you add is authenticated unless it explicitly declares otherwise. If you add a deliberately public endpoint, you must declare `AllowAny` explicitly AND justify it, and there must be a test proving what it exposes.
- `/api/ai/judge` now requires a Django-verified Bearer token BEFORE any catalog fetch or provider call, and caps input size. The shared helper is `frontend/src/lib/api-auth.ts`; it branches on `res.status` BEFORE parsing the body. If you add any Next.js route that can cause provider spend, use that helper and that ordering. Never copy the older `parseBackendJson` pattern, which ignores HTTP status.
- DRF scoped throttles exist on register, login, refresh, change-password, `/api/auth/me/`, and `/api/game/<id>/ai-context/`. Throttle scope STRINGS are load-bearing for tests: `auth_register`, `auth_login`, `auth_refresh`, `auth_change_password`, `auth_me`, `ai_context`. Adding a new scope is cheap; renaming an existing one breaks tests.
- Password policy: registration enforces `validate_password`, minimum length 8, and four Django validators.
- JWT lifecycle: `token_blacklist` enabled, `ROTATE_REFRESH_TOKENS`, `BLACKLIST_AFTER_ROTATION`, `POST /api/auth/logout/`, a `password_changed_at` field on `accounts.User`, and a `PasswordAwareJWTAuthentication` subclass rejecting any token whose `iat` predates the password change. Missing or non-numeric `iat` fails CLOSED.

KNOWN OPEN AT AUTHORING, so you do not think you found something new: the FRONTEND does not yet call `POST /api/auth/logout/` — wiring `handleLogout` in `frontend/src/app/game/[id]/page.tsx` is a small, well-scoped piece of work that fits naturally in your first whole; coordinate with the security Orchestrator before claiming it. Also open at authoring: security response headers and CSP; a brute-force brake on the Django admin login form (`django-axes`, approved by the Cooperator); a shared throttle cache when DEBUG is false instead of per-process LocMemCache; websocket ticket single-use and removal from the query string; a dependency and supply-chain audit; and a comprehensive fresh independent re-audit. All belong to the security Orchestrator. If your work touches one, say so and coordinate rather than fixing it silently.

Verified non-issues — do not re-litigate without contrary evidence: object-level authorization is sound (`services._load_session_for_user` filters on `slots__user_id`, outsiders get 404, the acting slot is server-derived); `dangerouslySetInnerHTML` appears nowhere in `frontend/src`; chat renders as a React text node; no secret is tracked in Git; model output cannot choose `game_id`, slot, or pass/exchange/place — `game_id` and the token are closures over the HTTP request body, and the tool pipeline is authoritative-engine-first.

TWO THINGS ABOUT SECRETS AND TOKENS YOU MUST KEEP IN MIND FOR ALL UI WORK: the access token AND the refresh token are persisted in `localStorage` through the Zustand store (`frontend/src/hooks/useGameStore.ts`). That is an accepted residual today only because no XSS sink exists. Every UI change you make must preserve that: no `dangerouslySetInnerHTML`, no `innerHTML`, no untrusted HTML injection, no third-party script tag added casually. Render model-produced and user-produced text as text nodes. A single XSS sink in your UI work converts an accepted residual into full account takeover.

================================================================
4. THE COOPERATOR'S BRAINSTORM, AS HE STATED IT
================================================================

Reproduced faithfully so you can reconcile it yourself rather than trusting a summary.

He wants a HARD CUT on model selection:
- It may have been a mistake to let the player choose the AI model at all.
- During a game it is fine to SHOW the fallbacks.
- But after "New game" the player must NOT choose which model to play against. Other game settings absolutely stay.
- Before the very first game, when the player clicks "Play the house", the important popup SHOULD appear. It must contain: AI thinking time, steps, and the LANGUAGE / VARIANT the player wants to play.
- Model selection is NOT in that popup. Instead a ping->pong is attempted, and the model that will actually be used is shown WITH A CHECKMARK. That model then appears at the top of the ranking during the AI's turn, with the others below it. Only models that pass the fallback are shown.
- Rationale, his words: do not complicate it for the user; this is much better UX.

He reports a BUG:
- After "Play the house" the new-game settings do not come up.
- Right now the only way is to open Settings — where he can also change the LANGUAGE, apparently DURING a game. He calls that a fail and bad UX.

He wants per-player persistence:
- Each player in the database must store which VARIANT, meaning which language, they want to play Libre Tiles in. He says this will be quite important.

He wants FULL MULTI-LANGUAGE, and this is a separate later whole:
- Translate all texts into SLOVAK so everything is in Slovak.
- Libre Tiles should be multi-language.
- His reasoning: the game is already Unicode and prompts already switch by variant, so what is missing is that changing the UI language changes everything in the UI.
- CRITICAL CONSTRAINT HE STATED HIMSELF: a player may have a SLOVAK UI and still play the ENGLISH variant, and with an ENGLISH UI still play the SLOVAK variant. UI language and game variant are INDEPENDENT.

He also asked, explicitly, that you use your own creativity and intuition for anything he forgot that makes sense for UI/UX, and above all that it be solved in the CODE so that no NEW infosec problems are created.

================================================================
5. DECOMPOSITION
================================================================

WHOLE #1  `player-model-choice-removal`
  The hard cut, the new-game modal, the Settings bug, and per-player persistence.
  Why first: it is small, independently shippable, delivers the UX he wants immediately, and it produces the database fields that whole #2 depends on.

WHOLE #2  `ui-internationalization`
  Slovak UI, multi-language, UI language independent of game variant.
  Why second: it needs whole #1's per-player language field, and translating a UI that still has controls you are about to delete is wasted work.

WHOLE #3  `admin-provider-model-console` — NOT YOURS. Separate fresh Orchestrator, handout already archived at Meta era 11. Do not implement it.

IMPORTANT: whole #1 is independently shippable WITHOUT the admin console. Verify this yourself, but here is the reasoning: `GET /api/catalog/models/` already returns a canonically ordered selectable list, row 1 is already marked flagship / recommended, and `buildFallbackQueue` already resolves an empty preference against row 1. So removing the player's choice does NOT leave the system with nothing to pick — it falls back to catalog order plus the fallback queue, which is exactly the behaviour he described. Do not let anyone tell you the admin console is a prerequisite.

================================================================
6. WHOLE #1 IN DETAIL — what to change, and the traps
================================================================

6.1 What to remove from the player's surface
  Player-facing model selection goes away. Sources of truth to inspect before deciding the exact removal set:
  - `frontend/src/hooks/useGameStore.ts` — `selectedModelId` in the persisted Zustand store, plus `aiTimeout` and `aiMaxSteps`
  - `frontend/src/app/settings/` and `frontend/src/components/game/` — wherever the model picker is rendered
  - `frontend/src/lib/model-catalog.ts` — catalog pair resolution
  - `frontend/src/lib/ai-fallback.ts` — `buildFallbackQueue`; preference is currently attempt 1
  - `backend/accounts/models.py` and `UserSerializer` — there is a `preferred_ai_model_id` field on the User model, exposed and validated through `is_selectable_model`
  - `backend/game/views.py` `GameAIModelView` and `GameAIPromptView` — PATCH endpoints that set a game's AI model and prompt
  - `frontend/src/app/api/ai/move/route.ts` — accepts `model_id` and `runtime_model_id` in the request body and PATCHes the game's AI model when the requested id differs from the session one

  TRAP: do not leave dead half-wired state. `preferred_ai_model_id` on the User model and `selectedModelId` in the store must be retired deliberately — either removed with a migration, or explicitly repurposed and documented. A field that no UI writes and some code still reads is exactly how a stale preference silently becomes the model everyone plays against.

  TRAP: `GameAIModelView` is an authenticated PATCH endpoint. If the UI stops offering model choice but the endpoint stays open, a player can still set their game's model by hand. Decide deliberately whether that endpoint is removed, restricted to staff, or kept as an internal mechanism, and write the decision down. Silently leaving it is a product-integrity gap, and after whole #3 it becomes an admin-policy bypass.

6.2 The new-game modal
  Trigger: "Play the house". It must actually appear — that is the reported bug.
  Contents: AI thinking time, steps, and variant/language. No model picker. Plus a read-only display of the model that will be used, with a checkmark, and the other fallback-passing models below it.
  Accessibility is a first-class requirement here because he will demo this: focus trap, ESC to dismiss, labelled form controls, visible focus states, and respect for `prefers-reduced-motion`. The project already has a reduced-motion path in `frontend/src/lib/premiumSurface.ts` and a `premiumLookEnabled` store flag — match the existing patterns rather than inventing new chrome.

  A Cooperator-owned product decision is sitting right here and has been deliberately left open for months: the store default `aiTimeout` is still 120 seconds. A no-provider-progress deadline makes the effective wait about 20 seconds, so the default is mostly cosmetic today, but the new-game modal is the natural place to resolve it. ASK HIM for the default; do not pick it for him.

6.3 The ping->pong probe — read this carefully, it is where a security problem would be born
  This is a provider call triggered by a player clicking a button. Requirements:
  - It must be authenticated. Use the `frontend/src/lib/api-auth.ts` helper and its status-first ordering.
  - It must be RATE LIMITED. The existing DRF scoped-throttle mechanism is the right place; adding a new scope is cheap.
  - It must be CACHED SERVER-SIDE AND GLOBALLY, with a TTL, NOT per player and NOT on every modal open. Otherwise every "New game" click costs up to three provider probes, and a player holding the button becomes a cost channel. A shared cached health view is also better UX: the modal opens instantly.
  - The modal must never block on a live probe. Show the last known result immediately and refresh in the background.
  - The probe must be minimal — a tiny completion with a small `maxOutputTokens`, not a full move generation.
  - THE MOVE PIPELINE IS TOOL-ONLY: the first step is a forced `validateMove` and `finishMove({ready:true})` may run only after a backend-valid candidate. A model that does not support tool calling will fail EVERY turn while looking perfectly configured. The probe should verify tool capability, not merely that the endpoint answers.
  - Provider error strings, HTTP bodies, and anything key-adjacent must NEVER reach the client. Map failures to a generic "temporarily unavailable" exactly as the existing routes do.
  - Note the honest limitation: the throttle cache may still be `LocMemCache` and therefore per-process. Coordinate with the security Orchestrator rather than assuming a global brake exists.

6.4 The Settings / variant bug — and the good news
  This was verified directly so you do not have to re-derive it: `variant_slug` appears in `backend/game/views.py` ONLY in `CreateGameView` (around line 57) and `QueueJoinView` (around line 70). There is NO endpoint that changes the variant of an existing game. So the server-side integrity is SOUND — nobody can swap the dictionary or tile values mid-game, and scores cannot be manipulated that way.
  The bug is therefore purely a frontend lie: Settings mutates a client preference that only applies to the NEXT game, while presenting it as if it applies now.
  The fix has three parts: (a) variant is chosen at game creation and is immutable for that game; (b) during an active game the UI must show the game's variant as read-only, ideally in the header; (c) Settings must either hide variant during an active game or label it unambiguously as "applies to your next game". Whichever you choose, write a test that locks it.

6.5 Per-player persistence — TWO fields, not one
  He asked for the player's variant to be stored in the database, and separately for UI language. These are INDEPENDENT by his explicit requirement. Model them as TWO distinct fields on `accounts.User`, for example `preferred_variant` and `ui_language`. Do not collapse them into one column and do not derive one from the other. Whole #2 depends on this being right.
  Both need sane defaults for existing rows, a migration that applies cleanly to the existing development database, and server-side validation against a known set — never a free-text column that the UI trusts.

6.6 Documentation is authority in this project and MUST change with the code
  `AGENTS.md` currently documents the behaviour you are about to delete, including "Preference: a valid explicit preference is attempt 1; remaining attempts follow untouched catalog order. New users and empty Zustand `selectedModelId` receive catalog row 1." After the cut, those sentences become false. Updating `AGENTS.md` and `README.md` is part of whole #1, not an afterthought. Leaving stale documentation in a repository he will show at an interview is a defect.
  While you are there: `README.md` says the judge makes "up to five attempts" while `AGENTS.md` and the code use three. That drift is known and unfixed; fold it in.

================================================================
7. WHOLE #2 — internationalization, and the one thing that will break if you are careless
================================================================

- UI language and game variant are INDEPENDENT. Slovak UI + English variant must work, and English UI + Slovak variant must work. Test both combinations explicitly.
- Use a real i18n library with proper plural handling. Slovak has three plural forms (1 / 2-4 / 5+) and full diacritics. Do not hand-roll string concatenation.
- Persist `ui_language` per user in the database (whole #1 delivers the field), not only in `localStorage`, so it follows the account.
- `LANGUAGE_CODE = "en-us"` and `USE_I18N = False` in `backend/config/settings.py`. Any Django-side translation needs `USE_I18N = True`, which has side effects. Decide deliberately whether translation is frontend-only.

THE CRITICAL WARNING, and it is not obvious: DO NOT LET i18n TOUCH THE AI PROMPTS. `frontend/src/lib/prompts.ts` contains a non-overridable TypeScript MOVE CORE whose bytes are PINNED by a SHA-256 with version `pfr-s2-core-1`. Translating, reformatting, reflowing, or running a linter's string transform over that file BREAKS THE PINNED HASH and silently changes the AI's behaviour. The prompts are already variant-parameterized for the game language; that is a completely separate axis from UI language. Put an explicit prohibition in every i18n Worker prompt: `frontend/src/lib/prompts.ts` is out of the allowlist, and a test must assert the CORE hash is unchanged.

Same caution for the seeded database prompts: migrations `0010_refresh_seeded_prompts` and `0011_playable_seeded_prompts` are SHA-256 hash-gated and must never be translated.

================================================================
8. INSTRUMENTS YOU INHERIT — use them, do not rebuild them
================================================================

    manage.py diagnose_ai_engine   variant-aware provider-free engine probe; fixtures or a deterministic seed; versioned JSON report; exit 0/1/2
    manage.py diagnose_ai_play     drives a real AI turn through the real /api/ai/move POST, the real fallback orchestrator, the real SSE consumer, and an ephemeral pytest-django live_server with a real DB; --runtime-mode fake|live; live is hard-gated on LIBRETILES_AI_PLAY_LIVE=1 plus a present provider key and fails closed with a redacted message otherwise
    backend/tests/test_endgame_policy_matrix.py    three move-selection policies x both variants x deterministic seeds
    backend/tests/test_slovak_full_game.py         Slovak full game to a legitimate end reason with tile conservation
    backend/tests/test_slovak_ranked_search.py     provider-free Slovak ranked oracle; the OU/AM formed-word traps
    backend/tests/test_full_game_simulation.py     English engine-vs-engine full games. Its local _is_word uses folded.isascii() — NEVER copy that onto Slovak
    backend/tests/test_multiplayer_ws.py           existing websocket coverage
    frontend/src/lib/ai-turn-simulation.test.ts    300-turn causal simulation with an injectable model

================================================================
9. LESSONS THAT COST REAL WORKER SESSIONS IN THIS PROJECT
================================================================

1. Provider-free tests hid two live-only defects: whether live mode was implemented at all, and that every AI turn burned 120 seconds. For anything the model touches: measure live, or do not claim it.
2. A test that proves only the guard can hide an unimplemented feature. A previous Orchestrator accepted "live mode implemented" after verifying only the refusal path. The enabled branch did not exist. When you accept a feature that has a guard, exercise the POSITIVE path too.
3. WORKER REPORTS ARE CLAIMS. Re-verify every material one yourself: diffs, tests, gates, actual line references, your own command runs. In the security whole this caught a garbled finding that hid a real fact, an entirely missed finding, and a line-number claim that pointed at a lazily-invoked closure rather than a sequential call. It is not distrust; it is the protocol.
4. A tool that measures must be able to say "I did not measure." Reward that shape explicitly in your prompts.
5. Negative results are results. A rare-tile-dumping heuristic was designed, measured, and REJECTED because it made one seed worse. Write completion contracts that say a negative result is an acceptable PASS.
6. Require a pre-fix / post-fix table for every regression test, with the exact pre-fix failure. A test that passes before the change locks nothing, and saying so out loud is what keeps the evidence honest.

================================================================
10. AUTHORITY BOUNDARIES
================================================================

This handout grants NOTHING. Not repository mutation, not deployment, not production, not host access, not browser, not provider calls, not AP upgrade, not lexicon unparking. Only a complete current Worker prompt that YOU issue, after your own Stage 1 verification, carrying its own exact authority record, may grant work.

Deployment posture: DO NOT deploy to a public address. Security corrections were still landing at authoring, a dependency audit had never been run, and CSP plus the admin-login brake were still open. Local play is fine. The Cooperator has been told this explicitly and agrees.

Provider calls: authorized only per explicit grant, with a stated numerical cap and its reason, one call in flight, and terminal classification before the next call. His provider quota is unlimited, which removes the billing objection and NOT the accounting discipline. Caps used previously in this project: 12 and 8.

Bounded secret handling, if a live diagnostic is ever authorized: a Worker may load `frontend/.env.local` into a subshell solely to export `NVIDIA_API_KEY` and `OPENROUTER_API_KEY` into the parent environment of `diagnose_ai_play`, using `set -a; . frontend/.env.local; set +a`, and must never print, log, hash, copy, or store a value. Reports state only `credential present: yes|no` plus the variable NAME. `backend/.env` is never read.

Do not create permanent `BOOT_*`, `NEXT_*`, `WORKERS.md`, or `ORCHESTRATOR_HANDOFF.md` files. A repository handoff is not the live model. Closure is recorded in Meta and in handout documents like this one.

================================================================
11. YOUR EXACT NEXT BOUNDED STEP
================================================================

1. Read everything in section 0 and 0.5, to depth. Both protocols.
2. Run Stage 1 read-only verification and independently confirm the standing gates. If a gate this document calls green comes back red, that is your first finding and you stop.
3. Ask the Cooperator, in Slovak, briefly, with the ❓ signal, in this order:
   a. Is `backend-security-hardening` closed, so you may issue mutating Workers?
   b. What should the default AI thinking time be in the new-game modal?
   c. Should `preferred_ai_model_id` be dropped with a migration, or kept as an admin-only field?
4. Present the restored state and your recommended decomposition. Get his explicit selection of ONE bounded logical whole.
5. 🧠 Issue ONE Planner Worker prompt for that whole, native planning mode REQUIRED, with an exact read-only boundary and a terminal planning report. Remember the finite budget: one initial plan plus at most one authorized targeted revision.
6. Review the plan as a claim. Then 🔨 issue implementation prompts with `Native planning mode: not-used`, exact allowlists, standing gates, invariant protection, and the Git pattern from section 1.
7. Re-verify every Worker report yourself before accepting it. 📁 Archive each prompt/report pair after the report exists.
8. At the end of your wholes, write and archive the handout for the next fresh Orchestrator.

Recommended routing for step 5: fresh Worker session, native planning mode required, reasoning High. Named risk: the cut touches the persisted client store, the User model, the catalog resolution path, and the AI move request body simultaneously, and a half-applied cut leaves a stale preference silently choosing the model for everyone.

# Libre Tiles — shared project context for Orchestrators

Artifact class: **shared reference, not authority.** Referenced by every Orchestrator handout under
`projects/libretiles/*/*/00_handout*.md` so that project truth is stated ONCE instead of being
copied into each handout, where the copies would drift apart.

This file grants no authority. Task authority comes only from the current authoritative prompt.
Protocol meaning comes from the pinned AP. Project truth comes from the canonical repository —
if this file and the repository disagree, **the repository wins and this file needs correcting.**

**Logical whole `backend-security-hardening` is CLOSED** at
`19cfec9ed27c57e9499b71c55be6c2fb709b0c63`; the closure record is
`09/00-backend-security-hardening/99_closure.md`. 32 findings `verified-closed`, 13 rejected as false
positives, all residuals dispositioned with sign-off where required.

Last reconciled against `main` at commit `19cfec9ed27c57e9499b71c55be6c2fb709b0c63` by the era-09
continuation Orchestrator, with porcelain empty, public readback equal, and no uncommitted state.
Every standing gate in section 4 was re-measured green at that commit by the Orchestrator, not
merely accepted from a Worker report. ALL implementation work in this whole has landed. Only the comprehensive fresh independent re-audit
(P-10) and the Cooperator's manual acceptance batch remain before closure. Re-verify before relying on
any of this.

---

## 1. Identity and topology

- Product: **Libre Tiles**, a standalone Next.js + Django Scrabble-like web app.
- Canonical repo `https://github.com/cisarik/libretiles`, working copy `/home/agile/Projects/libretiles`.
- Frontend: Next.js **16.3.4** App Router (bumped from 16.2.0 at `b5774b2`), React 19.2.4, Tailwind, Framer Motion, Zustand (persisted), DnD Kit. The request-interception file is **`frontend/src/proxy.ts`** exporting `proxy`; `middleware.ts` is gone and that convention is deprecated.
- Backend: Django + DRF. `backend/pyproject.toml` pins `django = "^5.2.17"` and the installed version is **5.2.17**; `daphne` is `^4.2.2` at **4.2.3**; `redis` is a **declared direct** dependency at `^7.3.0`. Write feature checks against Django 5.2. Pure game logic in `backend/gamecore/`.
- Realtime: Django Channels + Redis. **Redis is required ONLY for human-vs-human websockets, NOT for AI-only local boot.** That promise is in `AGENTS.md` and constrains where a shared cache or job queue may live.
- English validator: Collins 2019. Slovak: a hunspell-sk expansion (playable, not SSS-official) with SSS Príloha **B2** as the authoritative two-letter lexicon.
- AI-vs-house runs through **one** Next.js SSE route `/api/ai/move`. Free-only, but **nine** provider constants ship in `frontend/src/lib/provider-registry.ts`: `openrouter`, `nvidia-nim`, `groq`, `google-gemini`, `cloudflare-workers-ai`, `mistral`, `ibm-watsonx`, `aion`, `huggingface`. Eight route through the shared OpenAI-compatible transport in `frontend/src/lib/openai-compatible.ts`; `ibm-watsonx` has its own IAM path in `frontend/src/lib/ibm-watsonx.ts`. `backend/catalog/selection.py` **does** already carry all nine — the seven extra ones are string literals inside `DIRECT_FREE_RIVALS` / `WATCHLIST_FREE_RIVALS`, not module-level `*_PROVIDER` constants, so a constant-only grep misses them. `README.md` was already accurate. Only `AGENTS.md` was stale; corrected at `bbba2e9` as `orch-02-D08`.
- AP is pinned at the `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. A sibling checkout at `/home/agile/Projects/ap` may be newer; **the pin governs.** Do not upgrade AP.
- Libre Tiles declares **no** project-level `ap.project.conf`, **no** AP upgrade ledger, **no** closure-signal string. `.ap/ap.project.conf` belongs to the AP repository itself (`projectId = cisarik/ap`) and declares no route here. Do not invent any of those.

## 2. The Cooperator

Cooperator: **Michal.** Address him in **Slovak**, masculine grammatical forms. Orchestrator
self-reference is **feminine**. Worker prompts and Worker reports are professional **English**, and
every terminal Worker report begins exactly `### Report for ORCHESTRATOR_CHAT`.

His role, in his own words: he brainstorms, he intervenes when development heads the wrong way, he
answers questions, and he tests and gives feedback. He is not a file clerk and not a command runner.
He will happily be a courier when it genuinely helps, but do not make him one for work you can do.

His stake is material: he is preparing to present Libre Tiles at a **job interview** as evidence
that he can integrate AI into a real product. Presentability and correctness are first-class
requirements. A fresh clone that crashes, a control that does nothing, or a dashboard whose numbers
do not mean what they claim are serious defects in his frame.

He has granted full trust and asks for initiative. His replies are terse — `A`, `Pokracuj`, `ano`,
`Fixnute`. One one-word reply was once misread and cost an entire Worker session, so **confirm an
ambiguous one-word instruction in one line** before spending a session on it.

Do not encode "make no mistakes" as an acceptance criterion for him or for a Worker. It is not a
testable condition. Make his steps unambiguous instead.

### Emoji signals he asked for

Begin every message to him with the signal that tells him what to do:

    🧠 fresh Worker session, Plan mode ON (Planner Worker)
    🔨 fresh Worker session, Plan mode OFF (implementation or correction)
    🔍 fresh Worker session, Plan mode OFF (read-only audit or evidence probe)
    🧭 fresh Orchestrator session (handout)
    🧪 a manual test batch for him, answered with labelled PASS/FAIL/PARTIAL
    ❓ a question, you are waiting on an answer
    ✅ verified by you, nothing for him to do
    🐞 a classified defect going into the ledger
    ⛔ a blocker, or do-not-deploy
    📁 you wrote something to meta

**End every message with an explicit, emoji-annotated block of what he must do**: what to paste
where, what to test, what feedback you need, which question blocks you. Never bury his action in prose.

**Label manual test steps with a batch prefix** (`B3-1`, `B3-2`, …). Plain `1.)` collides with your
own numbered action list and has already caused one round of confusion.

## 3. Never do this

- Never read or print `frontend/.env.local` or `backend/.env`. Ask him yes/no questions about
  whether a variable is set. Never ask him to paste either file.
- Never let a credential value, prefix, length, or hash reach chat, a report, or a Meta file.
- Never create permanent `BOOT_*`, `NEXT_*`, `WORKERS.md`, or `ORCHESTRATOR_HANDOFF.md` files in
  the repository. A repository handoff is not the live model.
- Never ask him for a destructive action: no `git reset`, `git clean`, force push, database drop or
  reset, deleting his `.env` files, or deploying. Asking him to restart a dev server, create a test
  account, or play a game is fine and expected.

## 4. Standing quality gates

Every implementation prompt must require all of these and stop on any regression:

    cd backend
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    cd frontend
    npx vitest run <focused set>   ;   npm run typecheck   ;   npm run lint   ;   npm run build

Baselines at commit `19cfec9ed27c57e9499b71c55be6c2fb709b0c63` — **re-measure, do not trust**: mypy
`Success: no issues found in 80 source files`; ruff `All checks passed!`; `manage.py check`
`System check identified no issues (0 silenced).`; pytest `328 passed, 4 skipped`; the ten authorized
vitest files `199 passed (10 files)`; lint exit 0; build succeeds with one known deprecation warning
about the `middleware` file convention. Progression: `445029d` 302 passed, `bbba2e9` 315 (+13 from
S7a), `8e82f3b` 322 (+7 from S7b), `9ff9ac5` 322 unchanged (that correction added 6 frontend tests only), `7a197da` 326 (+4 dependency-floor tests), `b5774b2` 326 unchanged (frontend-only), `19cfec9` 328 (+2 throttle-identity tests).

### Execution route, and the mandatory bounded deviation

`AGENTS.md` documents backend commands as `poetry run ...`. **That route is NOT usable in a Worker
boundary**: the Cursor AppImage environment intercepts `python*` through inherited `APPIMAGE` /
`PYTHONHOME` variables. Per AP RF-16, every prompt must express the alternate as an explicit bounded
deviation naming the declared route that could not be used, the exact alternate
(`env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`), the rationale, the evidence
class, and the stopping condition. Never present ambient `python`, `python3`, or `poetry run` as a
parallel canonical route.

**`poetry` itself IS usable once the same variables are unset.** Verified read-only at `445029d`:
`env -u APPIMAGE -u ARGV0 -u APPDIR poetry env info` resolves the in-project virtualenv at
`backend/.venv` (Poetry 2.3.2 at `~/.local/bin/poetry`, `virtualenvs.in-project = true`). There is no
`poetry` binary inside `.venv/bin`. So a dependency change is done with
`env -u APPIMAGE -u ARGV0 -u APPDIR poetry add ...`, while test and type-check runs still go through
`.venv/bin/python` directly. Confirm the resolved virtualenv path before any `poetry add`.

**`npm run typecheck` is a NEW and mandatory gate, added at `b5774b2`.** It runs
`tsc --noEmit --incremental false`. It exists because `frontend/tsconfig.json` sets
`"incremental": true` and `next build` reuses that cache, so `npm run build` reported SUCCESS at
`9ff9ac5` and `7a197da` while two type errors existed in the tree — finding `orch-04-F22`. Every
"build succeeds" claim in this era, including the Orchestrator's own re-measurements, was weaker than
stated. "The build passed" and "the code type-checks" are now two separate claims and both must be
said. Check whether `mypy`'s incremental mode has the same weakness before trusting a cached success
there.

### Two traps that have already cost real Worker sessions

- `backend/pyproject.toml` sets `addopts = "-q"`. Passing another `-q` **silently suppresses the
  pytest summary count line**. Require plain `-m pytest` and require the summary quoted verbatim.
- Running mypy on a **narrowed** path set once hid 62 real errors behind a reported 12 for six
  consecutive Worker sessions. Always require the documented scope. Never let a "parked error count"
  travel between prompts unchallenged.

### Git pattern, delegated by the Cooperator

One commit per slice, staged by **explicit path** (never `git add -A` or `git add .`), an explicit
pre-push `git ls-remote origin refs/heads/main` equality gate against the exact baseline, one
non-force fast-forward `git push origin main`, and a public readback comparing `git ls-remote` with
`git rev-parse HEAD`. Never force, amend, rebase, reset, clean, stash, branch, or tag. If the remote
advanced, stop and escalate.

**Exactly one Orchestrator is active at a time**, because all of them push to `main` and each one's
pre-push gate demands exact equality.

## 5. Locked forks — do not reopen without contradictory evidence plus a Cooperator decision

1. SSS **100** Slovak tiles. Not 112, not 108. No CH/DZ/DŽ tiles. 42 tile kinds, of which **17 diacritic kinds have exactly one copy each**, so running out of a specific diacritic tile is normal.
2. **One** parameterized MOVE CORE with a pinned SHA-256, version `pfr-s2-core-1`, in `frontend/src/lib/prompts.ts`. **One** SSE route. Do not fork a second one and do not bump the version.
3. Judge (`/api/ai/judge`) is advisory Tier-3 assistance; Django is the sole authority; HTTP 503 on exhaustion; never synthesize a false `invalid`. It currently has **no caller** in the frontend.
4. No JULS, no `sk.sorted.txt`, no unofficial SSS dump, **no paid catalog tier**, no Stripe, no LM Studio, no Vercel AI Gateway. Libre Tiles is **free-only**: no money, credits, balances, token prices, or per-game charges.
5. Slovak two-letter legality = SSS B2 membership of **complete formed words**. Never a substring test.
6. Slovak lexicon quality is **PARKED** by Cooperator decision. hunspell junk (`loso`, `náhlo`, `vltavu`) is accepted residual and must never fail a diagnostic.
7. **Browser MCP is forbidden as a diagnostic driver** — explicit Cooperator decision, made because browser-driven diagnosis was too slow. He has since said it may be used if genuinely necessary; prefer CLI, raw sockets, and direct database inspection, which in practice have produced *more* evidence than a browser would. Asking the Cooperator to look at the UI himself is ordinary Cooperator-executed acceptance and is the right tool for UI work.
8. `MAX_FALLBACK_ATTEMPTS = 3` in `frontend/src/lib/ai-fallback.ts`.
9. Production search caps `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750` in `backend/gamecore/move_search.py`. Any variant-specific bound is an explicit call kwarg, never a changed default.
10. Exactly six `completion_source` values: `provider_candidate`, `backend_ranked_candidate`, `repair_candidate`, `backend_witness_rescue`, `genuine_no_move_exchange`, `genuine_no_move_pass`. Do not add a seventh.
11. **The nine AI providers are FROZEN pending their own logical whole.** Explicit Cooperator decision, 2026-08-31: he will run a dedicated whole to stop hardcoding providers. Until that whole runs, **no change to any provider list, provider constant, provider tier, exact model tuple, or provider documentation is authorized anywhere** — not `frontend/src/lib/provider-registry.ts`, not `frontend/src/lib/openai-compatible.ts`, not `backend/catalog/selection.py`, not `README.md`, not `AGENTS.md`. Reading those files is fine. The AGENTS.md accuracy fix that landed at `bbba2e9` (defect `orch-02-D08`) predates this decision and stands; do not revert it and do not extend it.

### The formed-word invariant — the single most misread rule in this project

    Illegal iff a COMPLETE formed dictionary-word produced by a placement has length 2
    and is outside the variant two-letter lexicon.
    NEVER illegal because a longer formed word CONTAINS a two-letter string.

`OSAMENIU` is legal even though it contains `AM`. `ja`, `ty`, `my`, `si`, `to` are legal Slovak
two-letter plays and the Cooperator wants them legal. If any Worker writes `assert "am" not in word`,
greps the board for a letter pair, or enumerates pairs to reject a longer word, **that Worker has
failed.** The only lawful shape is set membership over the list of complete formed words. Reference
implementation: `backend/tests/test_slovak_ranked_search.py` (`_REJECTED_CROSSES`, `isdisjoint`).

## 6. The central product fact

Across roughly a dozen counted live provider invocations in five independent sessions, the free LLM
authored **zero** backend-valid placements. Every completed live turn used
`completion_source: backend_ranked_candidate`. **The engine authors every move.** The LLM is an
unreliable component behind an authoritative engine.

This is the architecture working as designed and it is the honest framing for the interview. Never
let a Worker "improve" the AI by weakening backend validation.

Measured live on 2026-08-31 in the Cooperator's own browser, from persisted `ai_metadata`:

| observation | value |
|---|---|
| with an expired provider key | `terminal_cause = generic_error_fallback`, ~5 s per AI turn |
| with a fresh provider key | `terminal_cause = no_provider_progress_deadline`, ~21 s per AI turn |
| both cases | `provider_requests_used = 1`, `valid_candidate_count = 0` |

The ~21 s is the ~20 s no-provider-progress deadline aborting a silent model, after which the engine
commits a ranked candidate. Before that deadline existed, an AI turn took 124–138 s. **That
mechanism is observable working in production and is one of the better things to demonstrate.**

Engine strength, measured provider-free: under the product-like `ranked-best` policy a Slovak game
finishes in ~29 plies via `BAG_EMPTY_AND_PLAYER_OUT`, consumes all 17 single-copy diacritic tiles,
plays zero passes, and scores 520–560 per side. **Those are engine numbers, identical whichever
model is plugged in.** Any "how good is this model at Scrabble" metric must therefore be built on
the `completion_source` distribution and the `provider_candidate` rate, never on final score.

**Provider failures are now logged, bounded and redacted.** `frontend/src/lib/provider-logging.ts`
emits `{provider, phase, status, errorClass, message}` to `process.stderr.write`, message capped at
200 characters, from `createTrackedProviderFetch` in `openai-compatible.ts`, from `trackedFetch` in
`ibm-watsonx.ts`, from the outer catch in the move route, and from the two judge catches. The sink is
`process.stderr.write` rather than `console.error` because Vitest's console wrapper consumed a
`Date.now` mock and broke the judge timing tests — a real near-miss the Worker reported honestly. All
routes are Node runtime (`export const runtime` appears nowhere), so `process.stderr` exists.
**The redaction was the fragile part** — finding `orch-02-F21`, corrected at `9ff9ac5`. A pattern
denylist could not hold; the project's own `ibm-watsonx.test.ts` fixture defeated the first version.
The rule is now: redact by VALUE against the twelve credential environment variables the process
actually holds (literal replace, longest first, minimum length 8, placeholders skipped, no cache so a
rotated credential is matched on the next failure); keep the pattern denylist as defence in depth with
`Bearer[\s:_-]+` and a 16-character entropy floor; and for the `provider_transport` phase omit the raw
provider message entirely, keeping only error class and status, because the watsonx IAM request carries
the API key in its body. Never log request headers, the
request body, the response body, or a stack trace.

## 7. Security state — do not regress it

**`audit-03-F01` is corrected at `19cfec9`** and awaiting a bounded independent re-audit.
`DJANGO_NUM_PROXIES` defaults to `0`, is validated fail-closed, and binds `get_ident` to `REMOTE_ADDR`.
Orchestrator-verified dynamically: a spoofed `X-Forwarded-For` no longer changes the throttle bucket.
The history below is kept because the mechanism matters for any future rate limit.

⛔ **THE HISTORY OF THAT FINDING.** `audit-03-F01`, found by the independent re-audit at `b5774b2` and
independently confirmed by the Orchestrator from the installed DRF source: **DRF's unauthenticated
throttle identity is attacker-chosen.** `rest_framework/throttling.py` `BaseThrottle.get_ident` ends
with `return ''.join(xff.split()) if xff else remote_addr`, and that final line is reached whenever
`NUM_PROXIES` is `None` — which is the DRF default and is not overridden in `backend/config/settings.py`.
So every distinct `X-Forwarded-For` value WAS a fresh throttle bucket until `19cfec9`. `django-axes` is NOT affected,
because `ipware` is not installed and `axes/helpers.py` falls back to `REMOTE_ADDR`. The two brakes
therefore key on different identities. The consequence was that `auth_register` and `auth_refresh` had no
effective IP brake, and a **credential spray across many usernames** from one address was unbounded —
the DRF limit bypassed and axes never firing, because its key is (username, IP) and each username saw
only one failure. **Any future rate limit in this project must state which identity it keys on, and it
must agree with axes.**

### The nginx deployment fact, and the trap inside it

Cooperator decision 2026-09-01: Django will be deployed **behind nginx, and only behind nginx**.
Therefore `DJANGO_NUM_PROXIES` must be **1** in production, and nginx must set
`proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;`, which appends the real peer LAST — DRF
with `NUM_PROXIES=1` reads `addrs[-1]`, so that composition is not spoofable. `NUM_PROXIES=1` with nginx
NOT setting the header re-opens the bypass silently.

**The trap:** behind nginx, `django-axes` still keys on `REMOTE_ADDR` — nginx's address for every
request — because `ipware` is absent and `axes/helpers.py` only honours `AXES_IPWARE_*` when
`IPWARE_INSTALLED` is true. The lockout key `(username, ip_address)` then collapses to one global bucket
per account, turning an account lockout into a **targeted denial of service**. The very setting chosen in
S7a to avoid NAT-wide lockouts stops protecting anything once every request appears to come from one
address. Recorded as `orch-05-D14`, independently confirmed as
`audit-04-F01`, routed to the deployment whole.

⛔ **AND THE OBVIOUS REMEDY IS A TRAP.** The Orchestrator first wrote "install `django-axes[ipware]` and
set the trusted-proxy count". Verified against the installed `axes/conf.py`, that is wrong in a dangerous
direction:

    AXES_IPWARE_META_PRECEDENCE_ORDER  default ("REMOTE_ADDR",)   <- XFF is never consulted
    AXES_IPWARE_PROXY_ORDER            default "left-most"
    AXES_IPWARE_PROXY_COUNT            default None

Installing the extra and stopping there changes NOTHING. Adding `HTTP_X_FORWARDED_FOR` to the precedence
order without also setting the proxy count leaves `left-most` in force — and the left-most element of
`$proxy_add_x_forwarded_for` is the part the CLIENT sent. That would give axes an attacker-chosen
identity, turning a denial-of-service weakness into a full lockout-and-throttle bypass. **The half-measure
is worse than the current state.** Precedence order, proxy order (right-most, to match nginx's append),
and proxy count must be set together and tested as one unit. Also note the DRF dual: a `NUM_PROXIES`
value GREATER than the real hop count reads a leftward, attacker-chosen element. Too high is as dangerous
as too low.



Corrections landed across commits `ae574b7`, `fdfe4a6`, `7e583aa`, `04fe823`, `437e20f`, `445029d`,
`bbba2e9`, `8e82f3b`, `9ff9ac5`, `7a197da`, `b5774b2`, `19cfec9`. Verify current state yourself; this is the summary.

- Django **refuses to start** without a strong explicit `DJANGO_SECRET_KEY` (rejects absent, empty, whitespace, the old public fallback literal, keys under 50 characters or with fewer than 5 unique characters, and the `django-insecure-` prefix). `DEBUG` defaults to **false**. `ALLOWED_HOSTS` has no wildcard default and rejects `*` when DEBUG is false. `CORS_ALLOW_ALL_ORIGINS` is only ever true in DEBUG. HTTPS cookie, HSTS, and SSL-redirect flags follow `not DEBUG`. Tests in `backend/tests/test_security_settings.py`.
- DRF `DEFAULT_PERMISSION_CLASSES` is `IsAuthenticated` — **fail-closed**. Any DRF view you add is authenticated unless it explicitly declares otherwise. A deliberately public endpoint must declare `AllowAny`, justify it, and carry a test proving exactly what it exposes.
- `/api/ai/judge` requires a Django-verified Bearer token **before** any catalog fetch or provider call, and caps input size (12 words, 15 characters each). The shared helper is `frontend/src/lib/api-auth.ts`; it branches on `res.status` **before** parsing the body. **Any route that can cause provider spend must use that helper and that ordering.** Never copy the older `parseBackendJson` pattern in the move route, which ignores HTTP status.
- DRF scoped throttles exist. The scope **strings are load-bearing for tests**: `auth_register`, `auth_login`, `auth_refresh`, `auth_change_password`, `auth_me`, `ai_context`. Adding a scope is cheap; renaming one breaks tests. Rates at `bbba2e9`: register **20/h**, login **60/h**, refresh 60/h, change-password 5/h, me 200/h, ai-context 200/h. Login and register are **IP-keyed**, so all browsers on one machine share the budget — the derivation is `ScopedRateThrottle.get_cache_key`, which uses `user.pk` when authenticated and otherwise `get_ident(request)`. `LogoutView` has **no** throttle scope. In DEBUG the throttle cache is `LocMemCache` and therefore **per-process**, so restarting Django clears all counters — that is the reset button during manual testing.
- **Per-account brute-force brake: `django-axes==8.3.1`**, exactly pinned, the only dependency addition in this era. `AXES_FAILURE_LIMIT = 8`, `AXES_COOLOFF_TIME = 30 minutes`, `AXES_RESET_ON_SUCCESS = True`, `AXES_HTTP_RESPONSE_CODE = 429`, and — critically — `AXES_LOCKOUT_PARAMETERS = [["username", "ip_address"]]`, overriding the 8.3.1 default of IP-only, which would let one wrong-password user lock out everybody behind a NAT including the presenter. axes compares with `>=`, so the **8th** response is the lockout, not the 9th. `AUTHENTICATION_BACKENDS` is now explicit: `axes.backends.AxesStandaloneBackend` first (a lockout gate that does not authenticate), then `ModelBackend`. Enforcement is in the backend chain — `AxesStandaloneBackend.authenticate` raises `AxesBackendPermissionDenied` — so it does **not** depend on the DRF glue middleware. Covers both `POST /admin/login/` and `POST /api/auth/login/`; SimpleJWT does pass `request` into `authenticate()`, which is what makes the API path covered. `AccessAttempt` in Django admin is the failure audit trail; `AXES_ENABLE_ACCESS_FAILURE_LOG` is left false. Axes 8 ≪ login 60/h is deliberate: a single targeted account locks long before the coarse IP budget.
- **Throttle cache fails closed in production.** DEBUG true keeps `LocMemCache`, so Redis is still not required for AI-only local boot. DEBUG false resolves `DJANGO_THROTTLE_CACHE_URL`, else `REDIS_URL`, else raises `ImproperlyConfigured`; a non-`redis://`/`rediss://` value also raises. `django.core.cache.backends.redis.RedisCache` needs no new dependency, but the `redis` client is a **transitive** dependency of `channels-redis` rather than a declared direct one — a standing residual for the dependency audit.
- Password policy: registration runs `validate_password`, minimum length 8, and four Django validators (`UserAttributeSimilarity`, `MinimumLength`, `CommonPassword`, `NumericPassword`).
- JWT lifecycle: `token_blacklist` enabled, `ROTATE_REFRESH_TOKENS`, `BLACKLIST_AFTER_ROTATION`, `POST /api/auth/logout/`, a `password_changed_at` field on `accounts.User`, and a `PasswordAwareJWTAuthentication` subclass rejecting any token whose `iat` predates the password change. Missing or non-numeric `iat` **fails closed**. Verified live: after a password change the old session yields `Session expired`.
- Websocket tickets are **single-use**, enforced by a unique constraint on a SHA-256 hash in `game_consumed_ws_ticket` (a DB constraint, visible to every worker, deliberately not the per-process cache). The signed payload carries a `nonce` because Django's `TimestampSigner` is deterministic within one second for an identical payload, and without the nonce two fetches in the same second would collide and look like "one connection per game forever". Bounded cleanup of expired rows, no scheduled job, no Redis.
- Security response headers and an **enforced** CSP are emitted from `frontend/src/proxy.ts` via the pure builder in `frontend/src/lib/security-headers.ts`. Independently re-audited at `b5774b2`: the headers reach **every** document route and Next `/api/` route — `/`, `/play`, `/settings`, `/game/[id]`, `/waiting/[id]`, `/draw/[id]`, `/api/models`, `/api/prompts`, `/api/ai/move` — and are correctly absent on `favicon.ico`, `/_next/static/**`, and prefetch-marked requests. `connect-src` is **request-derived**, mirroring `resolveApiBase()` including its loopback-to-current-hostname rewrite. A static `connect-src 'self'` would break both the Django API and the game websocket.

### Dependency posture — established 2026-09-01, and it blocks deployment

The first dependency and supply-chain audit in this project's history (`audit-02`, INFOSEC 4.7 profile
P-4) found **three high findings on the deployed surface**, all independently re-confirmed by the
Orchestrator with `npm audit` and OSV.dev rather than accepted from the report:

| Package | Was | Now | Status |
|---|---|---|---|
| `django` | 5.2.12, 33 OSV records | **5.2.17**, OSV **0** | corrected at `7a197da`; constraint floor `^5.2.17` |
| `daphne` | 4.2.1, 4 OSV records | **4.2.3**, OSV **0** | corrected at `7a197da`; constraint floor `^4.2.2` |
| `redis` | undeclared transitive of `channels-redis` | declared `^7.3.0` direct | corrected at `7a197da` |
| `next` | 16.2.0, 23 advisories | **16.3.4**, left the advisory set | corrected at `b5774b2`; also closed `sharp` 0.34.5 -> 0.35.4 and nested `postcss` |

The `next` bump was the dangerous one and is why it was a separate slice: `orch-01-F18`'s accepted residual
records that `frontend/src/middleware.ts` works only because Next 16 renamed the convention and the
old name still executes with a deprecation warning. A minor bump could drop that support and silently
stop emitting the CSP and every other security header. Anyone bumping `next` must prove the headers
are still emitted afterwards.

One medium finding still needs Cooperator sign-off and is NOT fixable inside this whole:
`audit-02-F05` — there is no CI, SBOM, signing, or provenance in-tree attesting the artifact a browser
executes. No `.github` directory exists at all. Adding CI is a separate deliberate decision about what
it gates.

`npm audit` went from 7 advisories to **3**, and all three remaining are `dev`-flagged and already
dispositioned as `rejected-false-positive` in `audit-02-F07`.

`audit-02-F05` — no CI, SBOM, signing, or provenance in-tree — is an **accepted residual with explicit
Cooperator sign-off given 2026-09-01**. The complete Residual-Risk Decision record is in the ledger.

⛔ **The do-not-deploy stands until the comprehensive re-audit returns per-finding verdicts.** Nothing
in this project is `verified-closed` yet.

### Runtime evidence for the CSP now exists, and one gap in it

The enforced CSP was built in slice 07, which had to state honestly that runtime validation was not
performed because Browser MCP is a locked fork. At `b5774b2` that gap is partly closed: a production
`next start` bound to loopback, probed with an HTTP client, returns the full header set on `GET /`. The
implementing Worker did it on port 3100 and the Orchestrator independently reproduced it on 3200 with
byte-identical output. A production server plus an HTTP client is not a browser and is a legitimate
technique here.

**That gap is now CLOSED.** The P-10 re-auditor probed `/`, `/play`, `/settings`, `/game/{id}`,
`/waiting/{id}`, `/draw/{id}`, `/api/models`, `/api/prompts`, and `GET /api/ai/move` on its own loopback
server and got the identical header set on every one, with the exclusions behaving exactly as
`proxy.ts` declares. The CSP is not decorative on the page where a user plays. This was the
Orchestrator's own named weak spot and handing it to the re-auditor is what resolved it.

### Migrating the proxy convention is not safe to do gradually

Next 16.2.0 **hard-fails** when both `src/middleware.ts` and `src/proxy.ts` exist, with an
`unhandledRejection` rather than a graceful message — observed by the Cooperator in his own
`npm run dev` during the migration window. There is no safe intermediate state, a running dev server
will break during the transition, and that crash is not a product defect. Migrate as a single rename and
restart the dev server afterwards.

Reusable lesson from this audit: the deployed surface here is `next`, `django`, `daphne`, `channels`,
`channels-redis`, `redis`, `psycopg`, `httpx`, `djangorestframework`, `djangorestframework-simplejwt`,
`django-cors-headers`, `django-axes`, `python-dotenv`, `ai`, `@ai-sdk/openai`, `react`, `react-dom`,
`zod`, `zustand`, `framer-motion`, `@dnd-kit/*`, `canvas-confetti`. Everything else in either lockfile
is dev-only, and an advisory against a dev-only package is not a production finding. `poetry.lock`
carries group markers and `package-lock.json` carries `dev: true`; use them before promoting a scanner
line into a finding. Note that `optional: true` is NOT `dev` — `sharp` is in the production optional
tree, which is how `orch-03-G01` was missed the first time.

### Accepted residuals with recorded Cooperator sign-off

| Finding | Decision | Severity | Rationale |
|---|---|---|---|
| `audit-01-F13` duplicate-username registration error stays explicit | accepted-residual | low | usability for a self-service game; login itself does not differentiate unknown user from wrong password |
| `audit-01-F09` websocket ticket travels in the query string | accepted-residual | low | single-use plus a short TTL minimises the capture window; moving it would require changing the handshake and the frontend client |
| `orch-01-F18` `script-src 'unsafe-inline'` in production | accepted-residual | medium | nonce CSP needs dynamic rendering on `/`, `/play`, `/settings` — the exact pages the UX whole rewrites. `connect-src` still blocks exfiltration of the localStorage tokens. **Upgrade to nonce CSP is routed to the UX/i18n Orchestrator.** |
| `style-src 'unsafe-inline'` | accepted-residual | low | Framer Motion sets inline `style` attributes |
| ~~`frontend/src/middleware.ts` instead of `proxy.ts`~~ | **CLOSED at `b5774b2`** | — | migrated to `proxy.ts`; this residual no longer exists and must not be carried forward |

### Verified non-issues — do not re-litigate without contrary evidence

Object-level authorization is sound (`services._load_session_for_user` filters on `slots__user_id`,
outsiders get 404, the acting slot is server-derived, and `variant_slug` is only ever set at game
creation so a running game's variant cannot be swapped). `dangerouslySetInnerHTML` appears nowhere
in `frontend/src`; chat renders as a React text node. No secret is tracked in Git or in reachable
history. Model output cannot choose `game_id`, slot, or pass/exchange/place, because `game_id` and
the token are closures over the HTTP request body. `AllowedHostsOriginValidator` permits the browser
origin (`ALLOWED_HOSTS` contains `*` in the Cooperator's dev environment; the validator honours it).

### Two standing facts that constrain every UI change

1. The access token **and** the refresh token are persisted in `localStorage` through the Zustand store (`frontend/src/hooks/useGameStore.ts`). That is an accepted residual only because no XSS sink exists. No `dangerouslySetInnerHTML`, no `innerHTML`, no untrusted HTML, no casually added third-party script. Render model-produced and user-produced text as text nodes. **One XSS sink converts an accepted residual into full account takeover.**
2. Django admin is **session**-authenticated while the API is JWT-authenticated, so admin cookies are real and `SESSION_COOKIE_SECURE` / `CSRF_COOKIE_SECURE` matter. The Django admin login form is **not** a DRF view, so the DRF throttles do not protect it.

## 8. Instruments you inherit — use them, do not rebuild them

    manage.py diagnose_ai_engine   variant-aware PROVIDER-FREE engine probe; fixtures or a deterministic seed; versioned JSON report `libretiles.ai-play-diagnostic/v1`; exit 0/1/2
    manage.py diagnose_ai_play     drives a real AI turn through the real /api/ai/move POST, the real fallback orchestrator, the real SSE consumer, and an ephemeral pytest-django live_server with a real DB; --runtime-mode fake|live; live is hard-gated on LIBRETILES_AI_PLAY_LIVE=1 plus a present provider key and fails closed with a redacted message otherwise; supports --turn-count 1..300 although only 1 was ever run live
    manage.py seed_models          offline bootstrap catalog; must keep working for local boot — never make `sync` a startup requirement
    backend/tests/test_endgame_policy_matrix.py   three move-selection policies x both variants x deterministic seeds; wide matrix behind `slow` + LIBRETILES_RUN_ENDGAME_MATRIX=1
    backend/tests/test_slovak_full_game.py        Slovak full game to a legitimate end reason with tile conservation; wide matrix behind LIBRETILES_RUN_SLOVAK_FULL_GAME=1
    backend/tests/test_slovak_ranked_search.py    provider-free Slovak ranked oracle; the OU/AM formed-word traps
    backend/tests/test_full_game_simulation.py    English engine-vs-engine full games. Its local _is_word uses folded.isascii() — NEVER copy that onto Slovak
    backend/tests/test_multiplayer_ws.py          websocket coverage
    backend/tests/test_admin.py                   admin coverage; the house style for admin tests
    backend/tests/test_game_app_has_no_dev_imports.py   AST guard: no pytest/pytest_django/ruff/mypy import under backend/game/**
    frontend/src/lib/ai-turn-simulation.test.ts   300-turn causal simulation with an injectable model

Two structural patterns worth reusing rather than reinventing:

- **`executed_runtime_mode`.** The v1 report records what **actually executed**, separately from what was requested, and a mismatch is a sample **failure** with reason `runtime_mode_not_honored`. This exists because `--runtime-mode live` once accepted the flag, silently ran the fake path, and reported `exit 0 / verdict pass`. Apply "record what happened, not what was asked" to anything you build, and make sure any dashboard can say **"I did not measure."**
- **Derived counters.** `external_provider_invocations` comes from the fetch guard that decides which origins are allowed, not from a literal. It was previously a hardcoded `0`.

## 9. Lessons that cost real Worker sessions

1. Provider-free tests hid two live-only defects: whether live mode was implemented at all, and that every AI turn burned 120 seconds. **For anything the model touches: measure live, or do not claim it.**
2. A test that proves only the guard can hide an unimplemented feature. An Orchestrator once accepted "live mode implemented and hard-refused" after verifying only the refusal path; the enabled branch did not exist. **When you accept a feature that has a guard, exercise the positive path too.**
3. **Worker reports are claims.** Re-verify every material one yourself: read the diff, run the gates, check the exact line references, reproduce the load-bearing behaviour. This practice has caught a garbled finding that hid a real fact, an entirely missed finding, and a line-number claim that pointed at a lazily-invoked closure rather than a sequential call. It is not distrust; it is the protocol.
4. **A tool that measures must be able to say "I did not measure."** A Worker could once have written "live run, exit 0, verdict pass" and nobody would have noticed; it wrote BLOCKED and cited five lines of code instead. Demand that shape explicitly.
5. **Negative results are results.** A rare-tile-dumping heuristic was designed, measured, and rejected because it made one seed worse. Write completion contracts that say a negative result is an acceptable PASS.
6. **Require a pre-fix / post-fix table for every regression test**, with the exact pre-fix failure. A test that passes before the change locks nothing. One Worker caught its own too-weak assertion this way and strengthened it before implementing.
7. **An authorized correction can expose a pre-existing defect outside its allowlist, twice in a row.** When that happens, do not keep growing the slice. Give the Worker a decision rule with a pre-authorized bounded fallback so the work converges in at most one more exchange, and route the root cause as its own whole.
8. **Your own prediction can be wrong and the Worker's measurement can be right.** An Orchestrator claimed a third test file would break a probe; the Worker measured `19 passed` and explained why. Say so plainly when it happens; that is what keeps Workers reporting honestly.
9. **Diagnose the environment before blaming the product.** A websocket failure that looked like a product defect was a Tailscale exit node routing the entire Docker bridge range into the tunnel. Check reachability, routes, and services first.
10. **A negative grep is not a conclusion.** The era-09 continuation Orchestrator grepped `backend/catalog/selection.py` for `*_PROVIDER =` constants, found two, and recorded in this file and in the ledger that the backend knew about only two providers. All nine were there as string literals inside `DIRECT_FREE_RIVALS` / `WATCHLIST_FREE_RIVALS`. The Worker measured it, contradicted the Orchestrator, and was right. When a grep returns *few* results, widen the pattern before writing a finding — a finding built on the absence of a match must state the exact pattern that failed to match.

## 10. Known environment traps on the Cooperator's machine

- `backend/.env` must set `DJANGO_DEBUG=true`, otherwise `SECURE_SSL_REDIRECT` and the secure-cookie and HSTS flags switch on and local plain HTTP misbehaves in ways that look like product bugs. Since `bbba2e9` there is a second consequence: with `DJANGO_DEBUG=false` Django now **refuses to start** unless `DJANGO_THROTTLE_CACHE_URL` or `REDIS_URL` names a `redis://` / `rediss://` URL. That is deliberate fail-closed behaviour, not a regression.
- `scripts/libretiles.sh` now generates a strong `DJANGO_SECRET_KEY` into a **freshly created** `backend/.env` using `python3 -c` / `secrets.token_hex(32)`. It returns early and touches nothing when `backend/.env` already exists, so the Cooperator's existing file is safe. It requires `python3` on PATH and fails closed if absent.
- `.env` values **override** code defaults and are read at process start. Changing `.env` requires restarting the affected server. This is how `GAME_WS_TICKET_MAX_AGE_SECONDS='60'` silently kept the old TTL after the code default became 10.
- **The documented Django start command binds every interface.** `README.md:56`, `README.md:180`, and `AGENTS.md:32` all say `runserver 0.0.0.0:8000`. The Cooperator's live listener happens to be `127.0.0.1:8000` (verified with `ss`), but anyone following the documentation is reachable from their whole LAN. Any "not reachable today" claim must say which of the two it means. Found by the session-15 re-auditor.
- `frontend/.env.local` is read by the Next.js server at startup; a new provider key needs `npm run dev` restarted.
- Login and register throttles are IP-keyed and shared across browser profiles. At `bbba2e9` login is 60/hour and register 20/hour, sized for a same-NAT demo of roughly 16 logins and 12 registrations. **Restarting Django clears the counters** in DEBUG, because the cache is per-process LocMem. A single account is separately locked by `django-axes` after 8 failures for 30 minutes, and that lockout lives in the **database**, so a Django restart does NOT clear it — delete the `AccessAttempt` row in Django admin instead.
- Multiplayer needs Redis (`docker compose up -d redis`; only the redis service — the project uses SQLite in dev). **Tailscale with an exit node can route the Docker bridge range into the tunnel**, making Redis unreachable from the host while healthy inside the container. Symptom: `docker exec … redis-cli PING` returns `PONG` but a host connection times out. Check with `ip route get 172.18.0.2` — it must show `dev br-…`, not `dev tailscale0`. Fix with `sudo tailscale set --exit-node-allow-lan-access=true`.
- Two browser profiles are required for multiplayer. Two tabs in one profile share `localStorage` and the second login overwrites the first.
- An AI turn takes ~21 seconds with a working key. That is expected, not a timeout.

## 11. Related artifacts

- `/home/agile/meta/README.md` — the Meta storage contract
- `/home/agile/meta/projects/libretiles/09/00-backend-security-hardening/` — the security era, including the full independent audit report `01_report_00.md`
- `/home/agile/meta/projects/libretiles/DEFECT_LEDGER.md` — open defects found by Cooperator-executed acceptance
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`, `.ap/INFOSEC.md`, `.ap/PROMPT_ENGINEERING_PATTERNS.md`

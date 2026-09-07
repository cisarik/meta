You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An accepted plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 23
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: APMC-S7-DIAG-TARGET — diagnostic-only OpenAI-compatible target registration, Django+Next SSRF, R2=A credential-env-name, and a sibling runtime seam into the existing ONE SSE route. FAKE MODE ONLY. Provider calls: ZERO. Worker browser MCP: forbidden.
Phase: implementation
Implementation authority: explicit
Exact baseline: 40f353239c5b7a66e6923b55fa3c12afe04ff183
Changed-path allowlist: exactly the paths in section 4
Implementation boundaries: positive and negative authority in sections 3-5
Independence required: no
Evidence posture: non-independent
Evidence tier: E3
Evidence tier basis: admin-controlled outbound HTTP target plus a provider-boundary seam; R2=A so not E4 secrets-in-DB. Independent 7-IA (INFOSEC 4.6) is NOT this Worker — it is a later fresh session after landing. Rendered admin CRUD look is the Cooperator’s after you land, not yours.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risks: (1) DNS-check then ordinary `fetch` is TOCTOU / rebinding — the bound stdlib adapter is required. (2) Free-form `credential_env_name` naming `DJANGO_SECRET_KEY`. (3) Teaching player `getLanguageRuntime` / `isValidRuntimePair` a typed URL. (4) `_worker_env_whitelist` becoming `os.environ.copy()`. (5) Shipping fake admin launch as proof the seam ran — `generic_unchanged` returns before POST.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo back unchanged
PROMPT_CONTRACTS.md:203     the phase-result enum. Expected Worker result spelling:
                            `implementation-PASS`. Planning uses `not-applicable`; do not invent
                            a third spelling.
AP.md:2452-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself.
```

## Mandatory reading — by symbol; re-measure every symbol before you use it

```text
/home/agile/Projects/libretiles/AGENTS.md
backend/game/models.py          GameSession.ai_model (nullable), PlayerSlot.ai_model / ai_prompt
backend/game/services.py
    create_diagnostic_game (catalog-only today; optional target kwargs are authorized)
    get_ai_context — `acting.ai_model or session.ai_model` (must not become a target-seat fallback)
    set_game_ai_model — currently PATCHes session.ai_model for any vs_ai membership
    _load_session_for_user / _resolve_acting_ai_slot
    _reject_credential_parameters — SECRET_KEY_FRAGMENTS includes "env"; do not weaken
backend/game/admin.py           DiagnosticRunAdmin.launch_view; spawn_diagnostic_runner env
backend/game/management/commands/run_diagnostic_match.py
    _worker_env_whitelist (PATH/HOME/LANG/LC_ALL/TZ only)
    _position_pair_identity / _build_record / both instrument loops
frontend/src/lib/openai-compatible.ts
    createTrackedOpenAIChatModel UNEXPORTED
    createTrackedProviderFetch — "unknown" still fetches; hostname substring is NOT allowlist
frontend/src/lib/ai-runtimes.ts     getLanguageRuntime — isValidRuntimePair FIRST; do not edit
frontend/src/lib/ai-play-diagnostic.ts
    SHIPPED_PROVIDER_ORIGINS (two hosts); installFetchGuard; generic_unchanged early return
frontend/scripts/diagnostic-worker.mjs   mode: "fake" hardcoded
frontend/src/app/api/ai/move/route.ts    getLanguageRuntime at the construction site ~1222
frontend/src/lib/provider-logging.ts     CREDENTIAL_ENV_NAMES (not exported today)
backend/game/diagnostics.py     import SECRET_KEY_FRAGMENTS / redaction; ⛔ do not edit
backend/tests/test_game_app_has_no_dev_imports.py   game/** AST guard
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 40f353239c5b7a66e6923b55fa3c12afe04ff183
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before start and before commit
```

If `main` has advanced past `40f3532`: re-gate against the THEN-HEAD, state the new baseline in
your report, and continue — your allowlist and claims do not change. Any other divergence:
classify with the five recovery-candidate classes at AP.md:1464-1476 and STOP.

## 2. Goal

Staff can register a diagnostic-only OpenAI-compatible HTTPS endpoint in Django admin (hostname
allowlist + add-host, then target URL), select it on a diagnostic seat, and have the existing
L4 worker carry **target identity** into the ONE `/api/ai/move` route. Player catalog runtime
stays hardcoded. Fake mode: zero provider calls, fetch/socket denied before credential lookup.
This slice does **not** measure models, ping-pong, or go live.

## 3. Required behaviour

Establish failing tests first (S7-F01..F11), then production edits. Shared SSRF vectors live in
`backend/tests/fixtures/diagnostic_ssrf_cases.json` and are consumed by both languages.

### 3.0 Orchestrator corrections to the accepted plan (do not silently drop)

1. **Acting-seat fallback.** `get_ai_context` today uses `acting.ai_model or session.ai_model`.
   A target seat must **not** inherit the other seat’s catalog model. Check
   `acting.diagnostic_target` first. `create_diagnostic_game`: if a seat is a target, that
   slot’s `ai_model` is null; if **both** seats are targets, `session.ai_model` is null.
2. **`set_game_ai_model`.** Refuse PATCH when the acting diagnostic seat has a
   `diagnostic_target` (no catalog retarget, no fallback). Ordinary non-diagnostic vs_ai PATCH
   unchanged. Catalog-only diagnostic seats may keep today’s PATCH behaviour.
3. **`diagnostic_runtime` leakage.** Attach the object only for the diagnostic service user on
   a diagnostic session whose **acting** seat has an active target+host. Ordinary player
   `get_ai_context` never contains it (they already 404 on diagnostic games — keep that).
   ⛔ Do not put `base_url`, env names, or target ids into SSE frames / thinking events.
4. **`parameters_json`.** Target UUIDs are allowed. ⛔ `base_url`, `credential_env_name`, and
   any SECRET_KEY_FRAGMENTS key (including `env`) stay out. Do not weaken
   `_reject_credential_parameters`.
5. **TOCTOU.** If the bound `https.request` adapter (validated IP, custom lookup, no redirects)
   cannot land with the rest of F01–F11, STOP with `PARTIAL` and F08 open. ⛔ Do not substitute
   `getaddrinfo` then `globalThis.fetch`.
6. **`views.py` is not on the allowlist.** `AIContextView` already returns the service dict.
   If you would need a serializer that drops `diagnostic_runtime`, STOP rather than widen.
7. **No extra admin templates** unless Django default ModelAdmin + field `help_text` cannot
   explain add-host. Extra templates are **not** pre-authorized — STOP and report.
8. **`generic_unchanged` does not exercise the seam.** F06/F07/F08/F09 must use synthetic
   factory/transport mocks. Do not claim an ordinary fake Launch proved SSRF or the sibling runtime.
9. Keep `createTrackedOpenAIChatModel` **private**. Export `getDiagnosticOpenAICompatibleModel`
   plus optional custom-fetch input. Do not treat `inferProviderFromInput` as authorization.
10. IBM watsonx transport stays out. Full `CREDENTIAL_ENV_NAMES` is the Django/TS closed set
    (parity test). Fake denies before env lookup; do not implement watsonx.

### 3.1 Data model + admin

App: `game`. Migration `0012_diagnostic_targets.py` depending on `0011_diagnostic_ply`.
0009–0011 frozen.

- `DiagnosticAllowedHost`: unique hostname CharField(253); `is_active` default True; nullable
  `created_by` SET_NULL; timestamps. Hostnames **immutable** after insert; activate/deactivate
  allowed. Add-host: **no DNS, no HTTP, no runner**. Canonical ASCII hostname only (plan D2
  URL/host rules that apply to hostnames).
- `DiagnosticTarget`: UUID PK; name; `base_url`; FK `allowed_host` PROTECT; `model_id`;
  `credential_env_name` closed choices; `is_active`; nullable `created_by`; timestamps.
  Once referenced by any `PlayerSlot`, freeze `base_url`, `allowed_host`, `model_id`,
  `credential_env_name`. Name/activation remain editable. Deactivation: no DNS.
  `save()` validates new/changed connection settings and reactivation (covers
  `objects.create()`). DNS failure between form and persist writes neither row nor success LogEntry.
- `PlayerSlot.diagnostic_target` nullable FK PROTECT. DB check: not both `ai_model` and
  `diagnostic_target` non-null. Human slots may have neither.
- Seed the eight hosts (no DNS/HTTP) reversibly:

```text
openrouter.ai
integrate.api.nvidia.com
api.groq.com
generativelanguage.googleapis.com
api.cloudflare.com
api.mistral.ai
api.aionlabs.ai
router.huggingface.co
```

Omit `last_probe_at`, `promoted_catalog_id`, price/USD/spend/secret-value fields.

Admin: register both models in `game/admin.py`. Ordinary autoescaped Django admin.
⛔ no `|safe` / `mark_safe` / `format_html` / `format_html_join`.
Add-host is `POST /admin/game/diagnosticallowedhost/add/` (GET = form only).
`admin_view` + CSRF; require **add AND `has_change_permission`** for host/target **creation**;
change perm for edits; delete perm for deletion. Staff-alone never suffices.
LogEntry for create/change/activate/deactivate/delete: actor, object identity, **field names**,
never credential values.

Launch form: keep both catalog model-id inputs; add one active-target dropdown per seat;
exactly one populated choice per seat. Position-set with any target: **same target UUID both
seats** or reject. Full-game may mix catalog/target. Preserve `generic_unchanged`,
selected-only, fake, existing caps, authorship abort.

`create_diagnostic_game`: add optional `seat0_target_id` / `seat1_target_id`. Existing catalog
callers stay valid. Comment about “signature-frozen” refers to **caps** (still via
`configure_diagnostic_run`), not a ban on these optional kwargs.

### 3.2 SSRF (save + request)

One URL policy in Python and TypeScript (plan D2): HTTPS; implicit or `:443` only; exact
canonical hostname equality with an **active** allowed-host row (no wildcard/suffix); reject
userinfo, IP literals, Unicode/`xn--`, trailing dot, queries, fragments, `.`/`..` path
segments, percent-escapes. `model_id` is metadata, never a URL.

**Save-time** (`diagnostic_targets.py`): `getaddrinfo` AF_UNSPEC SOCK_STREAM; require ≥1
result; **any** disallowed address refuses the name; never connect; never persist resolved
IPs as authority. Bound DNS (plan: ~2s). Add-host does **not** resolve.

**Request-time:** custom fetch via Node `https.request`, dedicated non-reusing agent, custom
lookup returning **only** the validated address; original hostname for Host/SNI/verify;
no proxy / ambient agent. Re-validate URL + fresh all-address DNS **per provider request**.
Refuse all 3xx (never follow Location). POST only to exactly `<canonical base>/chat/completions`.
Timeouts/body caps as in the plan (2s DNS, 10s connect, remaining attempt deadline, 1 MiB
request / 2 MiB response including non-2xx, identity encoding, refuse compressed).
Increment tracker only after policy checks, immediately before dispatch.

IP policy (any hit refuses the whole name):

- IPv4: refuse `0/8`, `10/8`, `100.64/10`, `127/8`, `169.254/16`, `172.16/12`, `192.0.0/24`,
  `192.0.2/24`, `192.88.99/24`, `192.168/16`, `198.18/15`, `198.51.100/24`, `203.0.113/24`,
  `224/4`, `240/4`, Azure `168.63.129.16/32`.
- IPv6: accept only global-unicast `2000::/3` excluding `2001::/23`, `2001:db8::/32`,
  `2002::/16`, `3fff::/20`. Refuse unspecified, loopback, link-local, ULA, multicast,
  IPv4-mapped, NAT64, and everything outside that range.

All security tests: **mocked** resolver/transport. ⛔ no real metadata, provider, or live DNS.

### 3.3 Seam

`get_ai_context` may return `diagnostic_runtime` (plan fields) after the checks in 3.0.
Worker JSONL adds **only** `diagnostic_target_id` (no URL, no env name, no secret).
`runDiagnosticTurn` puts that id on the POST body as a **selection assertion**.
Route: body URL/env/runtime config is rejected. Assertion must match backend-authorized
target. Mismatch: explicit refusal, **no** catalog fallback, **no** `ai-model` PATCH.

Sibling `getDiagnosticLanguageRuntime` at the route construction site (~1222). Player path
keeps `getLanguageRuntime` + `isValidRuntimePair` + `revalidateRuntimePair` **byte-behaviour
unchanged** (do not edit `ai-runtimes.ts`). Diagnostic refusals terminate before generation
(no rescue/catalog). Provider identity in observations: `diagnostic-target/<UUID>`.

`diagnostic-egress.ts` + `installFetchGuard`: no policy → deny; fake → deny **before**
credential lookup, DNS, or socket; live policy is **not** activated in this slice.
Production worker stays `{mode:"fake"}`. `_worker_env_whitelist` **unchanged**.

Runner: catalog-or-target identity helper in both instrument loops; `_build_record` /
`_position_pair_identity` as in the plan. ⛔ do not edit `_model_position_samples` fill.
No MOVE CORE / `MOVE_PROMPT_VERSION` / second SSE route.

### 3.4 Credentials + copy

Export `CREDENTIAL_ENV_NAMES`; Django choices are that exact set; TS+Python parity test.
Unlisted names including `DJANGO_SECRET_KEY` rejected both sides.
Admin shows NAME + `credential present: yes|no|unknown` (Django process membership without
reading values; L4 fake forwarding reports `no`). Never render a value.
AGENTS.md + `frontend/.env.local.example`: player bases remain hardcoded, **no** base-URL
env vars; diagnostic bases are Django-admin registered. Add no base-URL environment setting.

## 4. Changed-path allowlist (exact)

```text
backend/game/models.py
backend/game/diagnostic_targets.py
backend/game/admin.py
backend/game/services.py
backend/game/management/commands/run_diagnostic_match.py
backend/game/migrations/0012_diagnostic_targets.py
backend/game/templates/admin/game/diagnosticrun/launch.html
backend/tests/test_diagnostic_targets.py
backend/tests/test_diagnostic_admin.py
backend/tests/test_diagnostic_session.py
backend/tests/test_diagnostic_runner.py
backend/tests/fixtures/diagnostic_ssrf_cases.json
frontend/src/lib/diagnostic-target-runtime.ts
frontend/src/lib/diagnostic-target-fetch.ts
frontend/src/lib/diagnostic-egress.ts
frontend/src/lib/openai-compatible.ts
frontend/src/lib/provider-logging.ts
frontend/src/lib/ai-play-diagnostic.ts
frontend/scripts/diagnostic-worker.mjs
frontend/src/app/api/ai/move/route.ts
frontend/src/lib/diagnostic-target-runtime.test.ts
frontend/src/lib/diagnostic-target-fetch.test.ts
frontend/src/lib/openai-compatible.test.ts
frontend/src/lib/provider-logging.test.ts
frontend/src/lib/ai-play-diagnostic.test.ts
frontend/src/lib/ai-play-diagnostic.worker.test.ts
frontend/src/app/api/ai/move/route.test.ts
AGENTS.md
frontend/.env.local.example
```

Negative: no `gamecore/`, no migrations 0009–0011, no `diagnostics.py`, no `views.py`, no
`ai-runtimes.ts`, no `prompts.ts`, no mint redesign, no `DiagnosticPly` schema, no 3b fill
fix, no slice-6 XSS reopen, no slice 8 probe, no K1/live NIM, no player-catalog promotion,
no secrets in DB, no new npm/poetry dependency, no `.ap/`, no `os.environ.copy()` on the
Node whitelist.

## 5. Fail-before table — capture BEFORE you edit, verbatim

| ID | Pre-fix claim (must fail on current HEAD) |
|---|---|
| S7-F01 | Target/host schema absent; cannot save an approved target |
| S7-F02 | No save-time rejection of loopback/metadata/mixed/mapped/malformed/DNS-timeout |
| S7-F03 | No add-host surface (audit + add-and-change + CSRF; no DNS/HTTP) |
| S7-F04 | No closed env-name selection; `DJANGO_SECRET_KEY` not rejected in both languages |
| S7-F05 | Launcher/services require catalog `AIModel` both seats |
| S7-F06 | Target assertion ignored; sibling runtime absent; player/forged config not refused |
| S7-F07 | No request-time public-at-save/private-at-request or mixed-DNS refusal |
| S7-F08 | No bound adapter (validated IP, no redirects, size/compress/timeout) |
| S7-F09 | No adapter-aware fake/default-deny before credential/DNS/socket |
| S7-F10 | Runner/report identity is catalog-only; URL/env/secret must not appear |
| S7-F11 | No freeze-on-reference / deactivation-without-DNS / value-free audit |

F01–F11 new-surface tests: baseline is “absent,” not a current exploit. Each negative family
needs a permitted synthetic control. Do not weaken existing tests.

## 6. Validation

From `backend/` (RF-16 bounded deviation: declared `poetry run` is unusable under Cursor
AppImage `APPIMAGE`/`PYTHONHOME`. Use exactly):

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

Also: `makemigrations --check --dry-run` and a disposable forward/reverse of `0012`.
Quote mypy/ruff/pytest summaries VERBATIM. Last Worker full suite at `40f3532`:
mypy 94 files, ruff clean, pytest `947 passed, 4 skipped`. Counts may rise; must not fall.
No removals; no new skips. ⛔ Never a second `-q`. ⛔ Never `PYTHON_DOTENV_DISABLED=1`.
⛔ Never ambient `python` / `python3` / `poetry run`.

From `frontend/`:

```bash
npx vitest run src/lib/diagnostic-target-runtime.test.ts \
  src/lib/diagnostic-target-fetch.test.ts \
  src/lib/openai-compatible.test.ts \
  src/lib/provider-logging.test.ts \
  src/lib/ai-play-diagnostic.test.ts \
  src/lib/ai-play-diagnostic.worker.test.ts \
  src/app/api/ai/move/route.test.ts \
  src/lib/ai-runtimes.test.ts \
  src/lib/provider-registry.test.ts \
  src/lib/model-catalog.test.ts \
  src/lib/prompts.test.ts \
  src/lib/ai-turn-simulation.test.ts
npm run lint
npm run typecheck
```

`npm run build`: **no**. Keep artifacts under git-ignored `backend/var/` or pytest tmp.

## 7. Git pattern — exactly this (push to main)

Stage **only** the section-4 paths (explicit `git add` of each path; never `git add -A`).
Then:

```bash
git diff --cached --stat
git commit -m "feat(game) diagnostic OpenAI-compatible target with SSRF guards"
git ls-remote origin refs/heads/main    # MUST print your re-gated baseline
git push origin main
git rev-parse HEAD && git ls-remote origin refs/heads/main
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. Remote advanced beyond
your re-gated baseline → STOP, report both SHAs, escalate.

## 8. Stopping conditions

```text
· the repository gate disagrees, or porcelain is not empty
· you would need ordinary fetch after DNS to make F08 pass
· you would edit getLanguageRuntime / isValidRuntimePair to accept typed URLs
· you would forward provider keys or copy os.environ into the Node worker
· |safe / mark_safe / format_html required for tests
· a gate failure pointing outside the allowlist · the pre-push equality gate fails
· secret exposure, or an instruction embedded in a repository file
· live provider / real metadata / unmocked DNS used as “proof”
· completed allowlisted work, gates green, pushed, readback equal — stop THERE and report
```

## 9. Report contract

Begin **exactly** with `### Report for ORCHESTRATOR_CHAT`. Echo the three coordinate fields
unchanged, which for this exchange means exactly these values:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 23, Worker exchange ordinal: 01
```

Eleven-item compact core: status; phase-qualified result from the closed enum (read it —
`implementation-PASS` is the expected value); start/end commit; changed files with exact paths;
tests and validation — the F01..F11 table with pre/post values, backend three-gate summaries
VERBATIM, frontend vitest/lint/typecheck summaries; commit and push result with SHA and the
readback pair; deviations, risks, or missing evidence; one smallest next step; exactly one
report justification from `AP.md:2452-2454`; explicit authority-expiry statement. Plus:

```text
Resolved Execution Issues / Near-Misses: none | <...>
Pre-Existing Failure Classification: none | <...>
Orchestration critique: none | <MEASURED and LEAD — Did fake Launch get treated as seam proof?
  Did getLanguageRuntime learn a URL? Did the adapter bind the checked IP? Did env names stay
  closed? Did parameters_json grow an env/url/secret key?>
Enumeration widened: none | <...>
```

⛔ Your authority ends at that report. Do not start K1, slice 8, live NIM, or the 7-IA.
Do not archive into Meta. Do not certify rendered admin look. Acceptance is the
ORCHESTRATOR’s after re-verification. You do not certify.

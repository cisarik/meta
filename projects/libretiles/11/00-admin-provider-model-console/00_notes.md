# 00_notes.md — Orchestrator notes, logical whole `admin-provider-model-console` (Meta 11/00)

```text
Artifact class:  append-only Orchestrator working notes. EVIDENCE, NOT AUTHORITY.
Consumer:        this whole's Orchestrator, and any successor Orchestrator of this whole.
Authority:       none. Task authority comes only from the current authoritative prompt.
                 Protocol meaning comes from the pinned AP. Project truth comes from the
                 canonical repository — if this file and the repository disagree, the
                 REPOSITORY WINS and this file needs correcting.
Retention:       until this whole is closed; then it stays as historical evidence.
Cleanup owner:   the COOPERATOR.
Staleness rule:  before quoting a line number from this file, re-measure it. Symbols and
                 headings are the durable key; line numbers are not.
Precedence:      `00_handout.md` (this whole's own artifact) wins on any overlap.
                 `90_admin_surface_evidence_from_era10.md` is an independent measurement
                 deposit written blind to that handout and is subordinate to it.
```

---

## §1 Session 01 — Orchestrator restoration and Stage 1 (this session)

### 1.1 Stage 1 repository gate, measured by the Orchestrator directly

```text
git rev-parse HEAD          3d7eae96d567a7004a927de45f53e16e2baf108f
git rev-parse HEAD:.ap      9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD   9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   (detached — correct)
git status -sb              ## main...origin/main
git status --porcelain=v1   EMPTY
git rev-parse origin/main   3d7eae96d567a7004a927de45f53e16e2baf108f
git ls-remote origin        3d7eae96d567a7004a927de45f53e16e2baf108f  refs/heads/main
HEAD subject                feat(ai) lossless multigraph AI context and truthful candidates
```

Local HEAD, remote-tracking, and public `main` all equal. AP pin intact and unchanged.

### 1.2 ⭐ Standing gates re-measured at `3d7eae9`, and THREE INHERITED NUMBERS ARE STALE

```text
mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
ruff check .                                 All checks passed!
pytest                                       813 passed, 4 skipped in 373.54s
```

| Source | mypy files | pytest | Verdict |
|---|---|---|---|
| `11/00/00_handout.md` §4 | 78 | 287 passed, 4 skipped | ⛔ STALE — do not quote |
| `PROJECT_CONTEXT.md` (at `47ed8bf`) | 83 | 390 passed, 4 skipped | ⛔ STALE — do not quote |
| **Measured here at `3d7eae9`** | **85** | **813 passed, 4 skipped in 373.54s** | ✅ current |

⚠ The pytest wall clock is **six minutes and thirteen seconds**. Any slice prompt that puts the full
backend suite on a zero-mutation or docs-only exchange is reproducing AP_DEFECTS D-03.

Frontend gates NOT run this session: `npm run typecheck`, `npx vitest run`, `npm run lint`,
`npm run build`. No frontend file has been touched, so there was nothing to falsify. ⛔ Do not record
them as green. `npm run build` writes `.next/` and is not a read-only gate.

### 1.3 Bounded deviation carried in every prompt (AP RF-16)

Declared route `poetry run …` is NOT usable in a Worker boundary — the Cursor AppImage intercepts
`python*` through inherited `APPIMAGE` / `PYTHONHOME`. Exact alternate, used for 1.2 above:

```bash
cd backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

⛔ Never present ambient `python`, `python3`, or `poetry run` as a parallel canonical route.
⛔ Never pass a second `-q` — `backend/pyproject.toml` sets `addopts = "-q"` and a second one
suppresses the summary count line.
⛔ Never narrow the mypy path set — a narrowed set once hid 62 errors behind a reported 12 for six
consecutive Worker sessions.

### 1.4 ⛔ THE HARD GATE THIS WHOLE HAS NOT CLEARED

`PROJECT_CONTEXT.md` records `13/00 multilingual-expansion-campaign` as **NOT CLOSED**: ten of
eleven conditions hold, the eleventh being the Cooperator's observation of a delivered and unanswered
acceptance batch. `09/00` and `10/00` are CLOSED; `11/01`, `11/02`, `12/00` are SUPERSEDED.

⇒ **No repository-mutating Worker prompt may be issued until the Cooperator confirms `13/00` is
closed.** Exactly one Orchestrator is active at a time because all of them push to `main`, and two
pushing to one branch trips each other's pre-push equality gates. Read-only discovery and read-only
planning are lawful before that confirmation, which is why `01_planning_00.md` was issued.

Asked of the Cooperator in session 01. **Answer: pending.**

---

## §2 Facts measured directly by the Orchestrator this session (symbol-keyed, not line-keyed)

Verified by `grep -n` in this session at `3d7eae9`. Symbols are the durable key.

```text
BACKEND
  catalog/admin.py            AIModelAdmin.get_urls · sync_models_view · change_list_template
                              `admin/catalog/aimodel/change_list.html`
  catalog/selection.py        DIRECT_FREE_RIVALS · WATCHLIST_FREE_RIVALS · FREE_RIVAL_PAIRS ·
                              _dynamic_catalog_enabled · get_selectable_models ·
                              is_selectable_model · get_selectable_prompts
  catalog/models.py           AIModel.provider is a FREE-TEXT CharField(max_length=50) —
                              no Provider model, no FK, no choices, no validators
  game/services.py            _session_authority · _resolve_ai_model · _load_session_for_user ·
                              _load_vs_ai_session · _reject_ai_nonscoring · get_ai_playability ·
                              get_ai_candidates · _submit_move_locked · create_game ·
                              submit_move_for_ai · validate_move_for_ai
  game/diagnostics.py         ARTIFACT_ID = "libretiles.ai-play-diagnostic/v1"
                              REPORT_KIND_ENGINE / _TURN / _POLICY_COMPARISON
                              TURN_COUNT_MIN = 1 · TURN_COUNT_MAX = 300
                              LIVE_SENTINEL = "LIBRETILES_AI_PLAY_LIVE"
                              CREDENTIAL_ENV_BY_PROVIDER · redacted_copy ·
                              load_variant_context · build_diagnostic_report ·
                              build_turn_report · build_policy_comparison_report ·
                              PolicyComparisonSample · write_report_atomically
  tests/test_game_app_has_no_dev_imports.py
                              _FORBIDDEN = frozenset({"pytest","pytest_django","_pytest",
                              "ruff","mypy"});  _GAME_ROOT = parents[1] / "game"
                              ⇒ scope is `game` ONLY. gamecore/catalog/accounts/config unscoped.

FRONTEND
  lib/openai-compatible.ts    createTrackedOpenAIChatModel  ⭐ UNEXPORTED — THE SEAM
                              createTrackedProviderFetch · getStandardOpenAICompatibleModel ·
                              STANDARD_PAIR_CONFIG · inferProviderFromInput ·
                              requireServerCredential
  lib/ai-runtimes.ts          getLanguageRuntime · parseCatalogModelRows · normalizeProviderError
  lib/ai-fallback.ts          MAX_FALLBACK_ATTEMPTS = 3 · MIN_ATTEMPT_STEPS = 5 ·
                              buildFallbackQueue · orchestrateFallbackTurn
  lib/provider-registry.ts    EIGHT `*_PROVIDER = "` constant lines by grep -c; NINE provider ids
                              in total ⇒ ⛔ a constant-count grep is NOT the id count. Enumerate
                              by name. (Prior defect `orch-02-D08` is exactly this shape.)
  app/api/ai/move/route.ts    export async function POST at :490; `const body = await req.json()`
                              is the NEXT statement at :491
                              ⭐ grep -c "api-auth" = 0 ⇒ THIS ROUTE DOES NOT AUTHENTICATE.
                              It takes its bearer token from the JSON body and forwards it.
  lib/api-auth.ts             bearerTokenFromAuthorizationHeader · verifyUserBearerToken
                              (the status-before-body-parse helper; only the judge route uses it)
  lib/provider-logging.ts     CREDENTIAL_ENV_NAMES (hand-maintained) · redactCredentialMaterial ·
                              PROVIDER_FAILURE_MESSAGE_MAX_LENGTH = 200
  lib/ai-play-diagnostic.ts   installFetchGuard · SHIPPED_PROVIDER_ORIGINS · runDiagnosticTurn
                              ⭐ `aiSlot: 1` HARDCODED at :438 ⇒ one seat, one turn
  lib/prompts.ts              MOVE_PROMPT_VERSION = "pfr-s2-core-1"
                              MovePromptLexiconId = "collins2019" | "slovak"   ⇒ TWO values
                              movePromptSpecFromContext · composeMoveSystemPrompt ·
                              SEARCH_PROFILE_BEGIN
  lib/prompts.test.ts         ⭐ CORE_SHA256 lives HERE, not in prompts.ts
```

⭐ **The single most important architectural finding of session 01:** there is no in-process Python
path to the LLM move pipeline, and there cannot be one without a second implementation. The whole
tool-only loop is TypeScript in one Next.js route. Every design in this whole must route through
that one route or explicitly declare a fork.

⭐ **The single most important security finding of session 01:** there is **no egress allowlist in
production**. `inferProviderFromInput` labels a host and returns `"unknown"` for anything unmatched;
the request still goes out. The only origin allowlist in the frontend, `installFetchGuard`, is
test-harness code that monkey-patches `globalThis.fetch`. An admin-typed base URL would therefore be
an unrestricted SSRF sink from the Next.js server until a guard is built. Zero hits for `ssrf` in the
7 609-line `DEFECT_LEDGER.md` ⇒ no inherited analysis exists.

---

## §3 Decisions the Orchestrator took in session 01

```text
O1  This whole is routed under INFOSEC. Three trust-boundary changes land together: an
    admin-controlled outbound HTTP target, admin-controlled provider spend, and a new long-running
    server-side process. A fresh independent security audit of the result is required before the
    whole is considered done. The auditor never corrects; the corrector never self-certifies; the
    re-auditor neither corrected nor implemented.
O2  Per Cooperator decision 14 (INFOSEC and large/complex cuts get a Planner Worker first), session
    01 is a PLAN-ONLY exchange. Read-only, `Native planning mode: required`, no mutation authority.
    Issued as `01_planning_00.md`.
O3  ⛔ FILENAME CORRECTION. The Cooperator asked for `00_planning_00.md`. `00_handout.md` is
    RESERVED and is not a Worker exchange; the Worker-session ordinal starts at `01`, and
    `meta_exchange_index = exchange − 1`. The first planning prompt is therefore
    `01_planning_00.md`. Corrected once, in one line, and recorded here.
O4  Subagents were used by the Orchestrator for read-only reconnaissance, on the Cooperator's
    explicit grant in his brainstorming. ⛔ All of that evidence is NON-INDEPENDENT and is the
    Orchestrator's own. Every load-bearing symbol a subagent reported was RE-MEASURED directly in
    §2 before being used in a prompt (AP_DEFECTS D-13 / R-G).
O5  Recommended sequence, to be confirmed by the Cooperator: DIAGNOSTICS RUNNER FIRST on today's
    catalog, THEN the provider registry. This DEVIATES from `00_handout.md` §7, which recommends
    `7a` (provider data model) before everything. Reason for the deviation: the runner does not
    depend on the provider entity — it consumes `(provider, model_id)` pairs that already exist —
    so the cheaper, lower-risk slice can land first and its measurements then tell us what the
    registry actually needs. AP_DEFECTS D-16: "a cheap probe that changes an expensive prompt is
    the highest-leverage exchange there is." The handout is evidence, not authority, and this is a
    reconciled disagreement rather than an oversight. D11 of the plan is instructed to attack it.
O6  The admin-registerable OpenAI-compatible target is scoped DIAGNOSTIC-ONLY by default, with a
    separate explicit promotion gate before it may ever serve a player. This keeps the player path
    exactly as safe as it is today while the SSRF and credential surfaces are introduced and
    audited in an admin-only path.
O7  The AI-written end-of-run analysis the Cooperator asked for is designed as ADVISORY: it never
    overrides a number, never overrides Django, and the numbers must be complete and readable
    without it. Consistent with locked fork 3.
```

## §4 Open Cooperator decisions (asked in session 01, answers pending)

```text
C1  Is `13/00` closed, so mutating Worker prompts may be issued?          ⛔ HARD GATE
C2  Credential model for an admin-registered provider: env-var NAME reference / encrypted value at
    rest / hybrid. Shapes the data model, so it is wanted before implementation planning of D8.
C3  Execution route for the LLM tier: L1 HTTP to the running Next.js route / L2 Node CLI importing
    the route / L3 Python reimplementation. The plan recommends; he decides, because L3 trades a
    product-faithful measurement for independence from Node.
C4  Per-run provider-request ceiling and its reason. Orchestrator proposal: default 200 per run,
    admin maximum 1000, because one full two-seat Slovak game is ~58 AI turns and ~1-3 provider
    requests per turn were the measured rate.
C5  Sequence: O5's recommendation, or the handout's provider-first order.
```

## §5 Standing conditions for every prompt this whole issues

```text
Applies to: every Worker prompt issued inside logical whole `admin-provider-model-console`.

S1  Run `python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>` before issuing.
    Exit 0 required. ⛔ Never build a prompt by string-patching the previous one — regenerate the
    coordinate-bearing region whole.
S2  Every enumeration handed to a Worker carries `Enumeration status: hypothesis` and the command
    that produced it, and the report carries `Enumeration widened:`.
S3  Every prompt carries `Orchestration critique: none | <findings>` with the two labels MEASURED
    and LEAD, scoped to the prompt, the approach, the sequencing, and the stated goal.
S4  Every prompt carries the RF-16 bounded deviation from §1.3 verbatim.
S5  Validation is proportional to what the exchange did. A zero-mutation exchange gets the
    repository gate only. Name which of the eight gates can MOVE and why the others cannot.
S6  `Deliverable tier spread` is declared. A spread of two tiers or more splits the exchange, and
    the cheap half may go first.
S7  A negative result is an acceptable PASS, and every completion contract says so explicitly. A
    model that measures badly is a successful measurement.
S8  Any instrument that reports must be able to say "I DID NOT MEASURE", and must record what
    ACTUALLY EXECUTED separately from what was requested.
S9  A terse Cooperator affirmation (`ano`, `A`, `Pokracuj`, `ok`) CONTINUES the scope already
    selected; it never selects a new one. Emit one `SELECTION ECHO` line naming the bounded
    outcome, the paths, and the execution mode before spending a session on it.
S10 Meta is written by the Orchestrator, committed by the Cooperator. Archive a prompt/report PAIR
    only after the report exists. ⛔ Never point a Worker at `/home/agile/meta/...` as repository
    evidence — inline the evidence into the prompt.
```

---

## §6 Session 01 artifacts

```text
01_planning_00.md   issued. Plan-only, read-only, fresh session, Native planning mode: required.
                    apfieldcheck: DEFECTS 0, WARNINGS 1 (the expected `required`-mode reminder).
00_notes.md         this file.
14/00 handout       written this session as a separate deliverable for a FRESH Orchestrator, on the
                    Cooperator's explicit request, covering the gameplay-prompt-strength era that
                    follows this one. It grants nothing and is not part of this whole's authority.
01_report-completion_01.md
                    exchange 02, current-worker-session, Native planning mode: not-used,
                    report-rendering-only authority. Written PRE-EMPTIVELY so the Cooperator can
                    paste it in the same turn if exchange 01 produced no terminal report.
                    apfieldcheck: DEFECTS 0, WARNINGS 0.
```

---

## §7 Session 01 exchange 01 — outcome, and the ⛔ STRUCTURAL GAP

The Cooperator returned the Worker's **client-native planner artifact** (`name: APMC diagnostic
console`, eight todo ids, body D1-D11 plus an "Explicitly later" section). He did **not** return a
message beginning `### Report for ORCHESTRATOR_CHAT`.

The artifact itself states: *"The full decision-complete record is the Worker report beginning
`### Report for ORCHESTRATOR_CHAT` (D1–D12). This plan is only the Cursor convenience copy."*

⇒ Per `AP.md:352-378`, a frozen decision-complete planner artifact **does not replace** AP's
separately required terminal report. **The exchange is structurally incomplete and is NOT planning
PASS.** Two possibilities, and I must not assume either (AP_DEFECTS D-14): the report exists in that
chat and only the artifact was forwarded, or it was never rendered. Asked in one line; repair prompt
written pre-emptively as exchange 02.

⛔ **Planning cycle accounting: exchange 02 is a RENDERING REPAIR and consumes NO planning cycle.**
`Automatic targeted revisions used` stays `0`. The one authorized targeted revision is still
available and is not spent by this repair.

### 7.1 ⭐ TWO CLAIMS OF MINE THAT THE PLANNER FALSIFIED — recorded because they were wrong

```text
F1  ⛔ I CARRIED AN ABSENCE CLAIM ABOUT THE PING->PONG PROBE WITHOUT MEASURING THE REPOSITORY.
    An era-10 evidence deposit records that no ping->pong health or capability probe appears in the
    META files, which is TRUE of those files. I let that stand as "no prior art" and wrote D10 as a
    specify-from-scratch deliverable, without ever grepping the repository for it.
    `frontend/src/lib/provider-capability.ts` exists — 15 473 bytes — exporting
    `probeProviderCapability`, `PROVIDER_CAPABILITY_STATUSES`, `PROVIDER_CAPABILITY_PLACEMENTS`,
    with bounded timeout handling and `step.toolCalls` inspection, plus
    `provider-capability.test.ts` and `provider-capability.live.test.ts` gated on
    `PROVIDER_PROBE_LIVE=1`. ⭐ IT IS ALREADY A TOOL-CALLING PROBE, NOT A LIVENESS PING.
    Root cause: an absence in one evidence class treated as an absence in another, plus AP_DEFECTS
    D-04 — my reconnaissance brief enumerated the files I thought to name and capability probing was
    not one of them, so no grep of mine could reach it. The `Enumeration widened` mechanism found it.
    ⇒ Slice 8 shrinks substantially, and the D10 "reuse" instruction is correct.
F2  `services.list_games_for_user` EXISTS at `backend/game/services.py:1179`, called from
    `backend/game/views.py:248`. My §2 symbol inventory omitted it. The Planner's history-exclusion
    design is grounded in a real symbol.
```

### 7.2 ✅ Planner claims I re-verified as TRUE at `3d7eae9`

```text
· `backend/assets/diagnostics/ai_play_report_v1.schema.json` has `additionalProperties: true` at the
  ROOT (line 7), 14 occurrences total. ⚠ Lines 57 and 129 are `false`, so some subobjects ARE
  closed — the implementation prompt must name which object the new sample type lands in.
· `mint_token` / `RefreshToken.for_user(user).access_token` at
  `backend/tests/diagnostics/test_turn_probe.py:128-129`.
· `gamecore` imports NOTHING from `game` (clean layering); `game/diagnostics.py` imports FROM
  `gamecore`. ⇒ `gamecore/selfplay.py` is correct placement AND is outside the `game/**` AST guard.
· `admin_site.admin_view` checks staff only, not model permissions — the Planner reached the same
  conclusion independently.
· `GameSession` has session-level `ai_model` / `ai_prompt` FKs (models.py:42, :49); `PlayerSlot` has
  none. So D3's two nullable slot-level FKs mirror an existing pattern rather than inventing one.
· `PlayerSlot.Meta.ordering = ["slot"]` (models.py:93). `GameSession.current_turn_slot` is nullable
  with `default=None` (models.py:39).
```

### 7.3 🐞 FOUR DEFECTS I FOUND IN THE FROZEN PLAN — all to be resolved in the implementation prompts

```text
P1  ⭐ THE PROVIDER-CALL CAP IS ARITHMETICALLY INVERTED AND WOULD SYSTEMATICALLY FAVOUR BROKEN
    MODELS. The plan sets "Default 24 positions ... cap 24 provider calls per model". One position is
    one turn, and one turn is one fallback attempt whose provider-request count is one per generation
    step — so a model that actually emits tool calls burns several requests per position and the cap
    binds around the sixth position, while a silent model (measured `provider_requests_used = 1`)
    completes all twenty-four. ⇒ The working model is truncated; the broken model is fully measured.
    FIX: two INDEPENDENT ceilings (positions AND provider requests), and hitting the request ceiling
    marks the run `truncated` with `did_not_measure` on every metric below its minimum sample —
    never a silently partial score.
P2  ⚠ THE ACTING-SLOT DERIVATION CHANGE TOUCHES A RECORDED VERIFIED-NON-ISSUE. `_load_vs_ai_session`
    resolves the actor as the first `is_ai=True` slot today; the plan derives it from
    `current_turn_slot`. Both are server-derived, and `PROJECT_CONTEXT.md` lists "the acting slot is
    server-derived" among the verified non-issues. The change is probably equivalent — but
    `current_turn_slot` is nullable. ⇒ The implementation prompt must require the change be provably
    behaviour-identical for `is_diagnostic=False`, with a regression test that FAILS before, and must
    name the None case.
P3  ⚠ THE PLAN INTRODUCES A STANDING SERVICE ACCOUNT WITH A MINTABLE JWT AND D9 DOES NOT COVER IT.
    "Service user with unusable password owns slot 0" plus `RefreshToken.for_user` means a management
    command can mint a valid access token for a real user row. That is a credential-adjacent surface.
    ⇒ Requires: unusable password, `is_staff=False`, `is_superuser=False`, no groups, no permissions,
    and tests proving it cannot log in, cannot reach a non-diagnostic session, and never appears in a
    player-facing list or count.
P4  ⭐ THE MODEL-TIER RUNTIME IS ASSERTED, NOT PROVEN, AND IT IS THE PLAN'S LARGEST EXECUTION RISK.
    "One long-lived Node worker per run that imports the existing `POST` handler (same as today's
    Vitest worker)" — but today's worker IS a vitest test file, and the route module needs `@/*` path
    aliases plus `NextRequest`. Whether a PLAIN Node process can load it is unproven, and the plan
    asserts "Next.js HTTP server is not required" without naming the runtime that loads the module.
    ⇒ FIX, and it is the highest-leverage exchange available (AP_DEFECTS D-16, "a cheap probe that
    changes an expensive prompt"): insert a BOUNDED PROBE slice 0 that either proves a plain Node
    process can import and invoke the route's POST handler, or proves it cannot. Slice 5 must not be
    written until that is answered.
```

### 7.4 Plan elements I accept as an improvement on my own framing

```text
· "L4 hybrid" — engine tier in-process Python, model tier ONE long-lived Node worker per run, with
  L1 (HTTP to a running Next.js) as an allowed equivalent rather than a second pipeline. Better than
  the L1/L2/L3 I offered, because it avoids a per-ply process spawn. ⭐ Subject to P4.
· `authorship` mode ABORTS with `diagnostic_end_reason=model_authorship_failure` instead of routing
  around `_reject_ai_nonscoring`. Cleaner than every option I listed in D3: it leaves the backend
  invariant literally untouched.
· A partial unique index on the in-flight status as the run lock. Correct answer to my objection that
  a cache-based lock does not hold under per-process LocMemCache — a DB constraint is backend-agnostic.
· Ratio above 1 explicitly allowed, because a model may beat a 750 ms ranked list. I had not thought
  that through and it is right.
· ⭐ The plan keeps BOTH instruments visible rather than collapsing to one number: "The Cooperator
  asked for one console; the console must expose both instruments, not one number."
```

### 7.5 One layering rule the implementation prompts must state

`gamecore` is pure and imports nothing from `game`. So `gamecore/selfplay.py` may produce SAMPLES but
⛔ must not build a report: the v1 envelope builders live in `game/diagnostics.py`, which imports FROM
`gamecore`. A Worker that puts a report builder in `gamecore` inverts the dependency and will reach
for a Django import to do it. Name the seam explicitly: samples out of `gamecore`, envelope built in
`game`.

---

## §8 Session 01 exchange 02 — terminal report received, verified, plan ACCEPTED

The Cooperator confirmed the continuity anchor was the same session ("toto je tá istá relácia") and
delivered the terminal report beginning `### Report for ORCHESTRATOR_CHAT`, echo 01/02, status PASS,
justification `new-evidence`. Structural check against the contract: header exact, coordinates
unchanged, phase-result `not-applicable`, Planning Record echoed with `Automatic targeted revisions
used: 0`, explicit authority expiry, Near-Miss recorded (CreatePlan treated as stop event), D1-D12
present, `Orchestration critique` with MEASURED/LEAD labels, `Enumeration widened` present.

⇒ **Planning exchange is now complete. The repair consumed NO planning cycle.** Plan ACCEPTED as
ORCHESTRATOR, with the corrections below carried into the implementation prompts — none of them is a
plan-level change.

### 8.1 Verification results — six claims re-measured at `3d7eae9`

```text
1  ⭐ REPORT RIGHT, MY PROMPT WRONG: test_full_game_simulation.py carries NO local `_is_word`.
   It imports WordAuthority (:19) and builds _AUTHORITY = WordAuthority.from_index(_INDEX) (:35).
   The `folded.isascii()` claim inherited from the era-11 handout AND reproduced in MY 14/00 handout
   is STALE — the multigraph era replaced it. ⇒ 14/00 00_handout.md corrected in place with a dated
   correction note, because that handout had not yet been consumed by any successor.
2  `probe:provider` script confirmed at frontend/package.json:13 —
   `PROVIDER_PROBE_LIVE=1 vitest run src/lib/provider-capability.live.test.ts`.
3  `_ranked_candidates_payload` exposes only `score` (candidate.total_score); no leave_value, no
   rack_out. The report's MQR-denominator caveat is correct.
4  MODE_CHOICES = ("vs_ai","Human vs AI"), ("vs_human","Human vs Human") — exactly two. The
   `is_diagnostic` discriminator (not a third mode) is the right call.
5  observe_source_revision (game/diagnostics.py:224) subprocesses `git rev-parse HEAD` — the
   AST-legal git precedent inside game/ confirmed.
6  🐞 NEW DEFECT CONFIRMED (C-L1): PolicyComparisonSample is defined in game/diagnostics.py:644 and
   gamecore imports NOTHING from game. The report's D5 signature
   `simulate_engine_game(...) -> PolicyComparisonSample` combined with "reporting types stay in
   game/diagnostics.py" is a LAYERING CONTRADICTION. Resolution to write into the slice-1 prompt:
   the sample dataclass (or a gamecore-level equivalent) lives in gamecore/selfplay.py;
   game/diagnostics.py builds the v1 envelope from it. gamecore must never import game.
```

### 8.2 Corrections carried into implementation prompts

```text
K1  (from 7.3 P1, still open) The position-set provider cap "24 calls for 24 positions" still
    assumes one provider request per ply. A working tool-calling model burns one request PER
    GENERATION STEP, so the cap truncates a working model mid-set while a silent model completes.
    The truncation MECHANICS in D7 are right (`truncated: true`, `cap_provider_requests`); the
    NUMBER is provisional. Before slice 5 freezes the default, measure requests-per-ply with a
    small live grant (8-12 calls), then set the default. Until then the cap is documented as
    provisional in the run record.
K2  (from 7.3 P4, still open) No probe slice exists in the plan. INSERT a bounded probe exchange
    before slice 5: prove or refute that a plain Node process can import the route module's POST
    handler (path aliases + NextRequest). Cheap first; slice 5 is not written until answered
    (AP_DEFECTS D-16).
K3  (from 7.3 P2) Slice-4 prompt requires: acting-slot derivation provably behaviour-identical for
    is_diagnostic=False, a fail-before regression test, and the current_turn_slot=None case named.
K4  (from 7.3 P3) Slice-4 prompt requires service-user tests: unusable password, is_staff=False,
    is_superuser=False, no groups/permissions, cannot log in, cannot reach a non-diagnostic
    session, never appears in a player-facing list or count.
K5  (C-L1 above) Slice-1 prompt carries the gamecore/game layering rule.
```

### 8.3 Gate and decisions status

```text
R1  ✅ CLEARED — Cooperator: "Brána sedí" (2026-09-05), reconfirmed "1.) R1=ano". Mutating Worker
    prompts are authorized, one slice at a time, per the Git pattern.
R2  ✅ DECIDED: A — env-var NAME reference only. No secret in the database; the existing
    value-based redaction keeps working; onboarding a provider costs one .env.local edit plus one
    Next.js restart. Recorded as the binding choice for slice 7.
R3  ✅ DECIDED: L4 hybrid — engine tier in-process Python, model tier ONE long-lived Node worker
    per run, L1 (HTTP to a running Next.js) as an allowed equivalent. Binding for slice 5,
    subject to K2 (the Node-runtime probe before slice 5).
R4  ✅ DECIDED: default 200 provider requests per run (Cooperator: "R4=200"). The plan's D7
    provisional per-instrument numbers (24/80) are sub-caps to derive within that ceiling; K1
    still requires measuring requests-per-ply with a small live grant before slice 5 freezes
    defaults. Admin-adjustable maximum: 1000 (uncontested).
R5  ✅ DECIDED: A — runner first on today's catalog, provider registry later. This also
    constitutes the Cooperator's confirmation of the SELECTION ECHO for slice 1 (the echo defined
    `ano` = R5=A = slice-1 go-ahead).
```


## §9 Slice 1 issued — exchange 01

```text
02_implementation_00.md   session 02, exchange 01, fresh-worker-session, Native planning mode:
                          not-used, Fresh Implementation Worker, E1, baseline 3d7eae9.
                          Allowlist: gamecore/selfplay.py (new) + the four harness test files.
                          Gates required in FULL (mypy documented scope + ruff + plain pytest)
                          because the exchange MUTATES a shared engine surface (AP_DEFECTS D-03).
                          Layering rule K5 written in as the top constraint.
                          Fail-before F1: `from gamecore.selfplay import simulate_engine_game`.
                          apfieldcheck: DEFECTS 0, WARNINGS 0.
Design facts measured immediately before issuing:
  · test_endgame_policy_matrix.py imports load_variant_context FROM game.diagnostics (:31,:93) and
    is therefore the one harness that may keep a game-layer import; the other three build their own
    WordAuthority (for_variant / from_index) — so the moved loop takes the context INJECTED.
  · Measured bounds: WITNESS_MAX_ELAPSED_MS = 10_000; witness call uses
    (DEFAULT_MAX_NODES, WITNESS_MAX_ELAPSED_MS); ranked uses (DEFAULT_RANKED_MAX_NODES,
    DEFAULT_RANKED_MAX_ELAPSED_MS). Per-harness module constants exist in the other three files.
  · test_slovak_full_game.py also carries a DB test (imports game.models/_check_endgame) — its
    imports stay; only its _simulate and helpers are rewired.
```



## §10 Session 02 exchange 01 — BLOCKED was CORRECT; exchange 02 issued with the decision

Exchange 01 (02_implementation_00.md) returned BLOCKED with ZERO mutation: the four harness helpers
have DIVERGED in semantics, not merely duplicated, and the prompt's §9 correctly forbade a silent
choice. The Worker's critique also named a real defect in my prompt — §3 demanded "one helper copy
with unchanged semantics" while §9 required stopping on divergence. Both are recorded as my findings.

### 10.1 Divergences re-verified by the ORCHESTRATOR directly (all three CONFIRMED)

```text
1  FINGERPRINT   strength :66 carries (player.score, player.pass_streak) per player;
                 matrix :148 carries player.score only. Both carry current_index and
                 consecutive_scoreless_turns, plus board/bag/racks.
2  RANKED        strength :118-127 is ranked-WITH-witness-safety-fallback (deliberate, commented:
                 "Ranked search is a quality path only... the unchanged first-witness safety search
                 does"); matrix POLICY_RANKED_BEST returns the ranked result as-is when empty.
                 ⇒ POLICY-level difference, not a helper bug.
3  RACK POINTS   English :66 sum(_TILE_POINTS[tile]) raises on unknown tile;
                 matrix :156 and Slovak :81 use .get(tile, 0).
Repository-wide helper count (measured): _tile_counter ×4, _fingerprint ×4, _rack_points ×3
(strength has none). NONE outside backend/tests/.
```

### 10.2 Decision D-S1 — preservation by configuration (ORCHESTRATOR decision, technical scope)

One implementation, explicit named options, per-call-site values verbatim; shared CODE, not shared
BEHAVIOUR; zero observable behaviour change:

```text
D1  fingerprint: include_pass_streak bool  (strength True; matrix/English/Slovak False)
D2  two distinct policies: POLICY_RANKED_BEST (pure ranked) and POLICY_RANKED_WITNESS_SAFE
    (ranked, witness-safety fallback) — the strength A/B spread keeps its meaning
D3  rack points: strict_unknown_tile bool (English True; matrix/Slovak False; strength measured
    at implementation time)
```

Root causes of the divergences are FINDINGS the Worker must report, not fix. Unifying semantics is a
deliberate later decision. Acceptance bar beyond assertions: pre-fix behavioural tuples
(seed-0 end_reason/scores/plies per harness) captured and matched post-fix exactly.

```text
02_implementation_01.md   session 02, exchange 02, current-worker-session, continuity anchor =
                          the exchange-01 BLOCKED report. apfieldcheck: DEFECTS 0, WARNINGS 0.
```

## §11 Session 02 exchange 02 — second BLOCKED: parity instrument vs wall-clock nondeterminism

Exchange 02 returned BLOCKED with the candidate UNCOMMITTED (verified myself: porcelain = exactly
the five authorized paths; strength test file standalone = `3 passed, 1 skipped`, so the in-suite
failure is the Worker's own new parity instrument, not a pre-existing assertion). F-checks complete:
F1 `ModuleNotFoundError` pre-fix → import OK post-fix; helpers 4/4/3 → 1/1/1 in selfplay.py; guard
green. Gates: mypy `Success: no issues found in 86 source files` (85 + selfplay), ruff clean,
pytest `1 failed, 824 passed, 4 skipped` — the 1 failure is the new parity test in-suite.

**The anomaly:** strength (300, 0) spread 435 IN-SUITE vs 420 standalone post-fix vs 420 pre-fix
standalone. Worker's LEAD: wall-clock ranked-search limits (750 ms) are context-sensitive under
suite load. The decisive MISSING CELL is the pre-fix IN-SUITE value — never captured.

**Worker root-cause findings, accepted as findings (no fixes):** D1 pass_streak distinguishes more
states, detects no unique cycle (all versions carry the global scoreless counter); D2 two distinct
policies confirmed; D3 `"?"` scores zero in both lookups, `"Á"` raises strict / zero-lenient —
strict path is about FOREIGN tokens, which tile conservation rejects anyway. Strength has no
rack-point call site (config `None`).

**Exchange 03 issued** (02_implementation_02.md, Diagnostic Worker, current-worker-session,
apfieldcheck 0/0): bounded diagnosis with a PREDECLARED decision rule —
temp worktree at baseline runs the PRE-FIX suite twice with a disposable probe test printing the
(300, 0) spread in-suite; a determinism probe calls the ranked search 10× on fixed inputs;
`RULE A` (pre-fix in-suite ≠ 420) → nondeterminism pre-exists → narrow the parity instrument to
deterministic axes, candidate unchanged, COMMIT+push; `RULE B` (both == 420) → candidate-induced →
hot-path overhead fix (snapshot capture out of timed regions), bounds untouched, re-verify, then
commit if green. Two runs decide; no third-run comfort-hunting.

⭐ Whole-level lesson recorded for the console design: **wall-clock-bounded search makes
engine-generated snapshots run-context sensitive — every stored position-set snapshot must carry
what actually executed (condition digest), exactly the `executed_runtime_mode` shape.**

## §12 Session 02 exchange 03 — S4 completed ORCHESTRATOR-DIRECT; RULE B fires

Exchange 03 BLOCKED correctly: the disposable worktree has no `.venv` and the prompt had not
authorized an interpreter route for it (my defect). S1 named the failing node:
`test_ranked_strategy_beats_first_witness_on_default_balanced_seeds` — the ORIGINAL test only
asserts `all(result.spread > 0)` (verified at HEAD), so the exact-spread pin is the Worker's added
parity assertion. S2: three standalone 420s. S3: ten identical probe lines on one fixed position
(does not establish general determinism — Worker's LEAD, accepted).

**The ORCHESTRATOR completed S4 directly** (mechanical measurement, no Worker): worktree at
baseline + symlinked canonical `frontend/node_modules` (restores the faithful suite load profile —
without it, nine vitest-worker tests fail fast and the load shape differs exactly in the measured
dimension) + canonical `backend/.env` sourced silently + canonical venv interpreter by absolute
path. Two faithful runs: **both `plies=35, ranked_score=585, witness_score=165` → spread 420.**
Caveat honestly recorded: final summary lines were not captured. Worktree and probes cleaned;
porcelain re-verified as exactly the five candidate paths.

```text
DECISION MATRIX   pre-fix: standalone 420, in-suite 420 x2 (faithful)
                  post-fix: standalone 420 x3, in-suite 435
⇒ RULE B FIRES: the candidate shifts the in-suite result.
⭐ KEY CONSTRAINT for the fix: pre-fix in-suite is STABLE ⇒ under suite load the search completes
   deterministically given identical inputs ⇒ prime suspect is a DETERMINISTIC, environment-
   dependent INPUT difference (per-process hash randomization reaching search inputs via a set/
   dict iteration order), not load flakiness. find_ranked_scoring_moves is untouched (fork 9).
Exchange 04 issued (02_implementation_03.md, Diagnostic Worker): surgical input-dump diff
(standalone vs in-suite), H-A hash-order / H-B hot-path split, smallest coherent correction,
parity instrument NOT narrowed (RULE B must meet it), full gates + conditional commit+push if
green, STOP if in-suite still differs. apfieldcheck: DEFECTS 0, WARNINGS 0.
Also recorded: Cooperator reports NVIDIA NIM `nvidia/nemotron-3-super-120b-a12b` works live
(tested by him 2026-09-06). Relevant to K1 (requests-per-ply measurement) at slice-3/5 acceptance
under a formal provider-call grant; not used mid-slice.

## §13 Session 02 exchange 04 — 435 unreproduced; instrument disposition; exchange 05 = publication

Exchange 04: three further suite-context runs ALL 420 with the parity assertion passing; 18/18
ranked calls identical inputs AND outputs standalone vs suite; representative ply 31 identical
input SHA, same selected key/score, traversal 22,842-24,373 nodes at the same 750 ms cap; a 10×
probe on that position: identical selection every call; GC observed inside timed searches, no
output effect. H-A and H-B both unestablished. My own re-verification: porcelain = 5 paths,
strength file standalone `3 passed, 1 skipped`.

**ORCHESTRATOR DISPOSITION (exchange 05, 02_implementation_04.md, apfieldcheck 0/0):**
```text
D1  435 = transient environmental event, unreproduced 5×. No production correction justified.
D2  The real defect is the INSTRUMENT: exact-tuple pins on wall-clock-capped searches are
    load-sensitive and can false-positive on ANY code. Applies to every such pin, matrix included.
D3  Redesign (test files only, selfplay.py must end byte-identical):
    · deterministic parity mode — ranked calls bind by NODES via explicit kwargs
      (e.g. max_nodes=20_000, max_elapsed_ms=10_000_000), exact tuples pinned THERE; the
      permanent extraction-regression tripwire; timing flakes can no longer false-positive
    · production-config runs keep ALL pre-existing assertions; tuples printed, never pinned
    · the deterministic pins are NEW post-fix baselines — the extraction-equivalence proof is
      separate (18/18 I/O identity + standalone parity + pre-fix in-suite parity); not conflated
Then: full gates (mypy 86-file scope, ruff, plain pytest, summaries verbatim) → explicit-path
staging of the five files → commit → ls-remote equality gate vs 3d7eae9 → push → readback.
```
⭐ The parity pin EARNED its place: it caught an anomaly, forced the diagnosis, mapped the search's
timing envelope (traversal varies at the cap, selection robust), and is now being made sound
instead of deleted. `git diff --check` discipline held throughout; no assertion was weakened to
land the refactor — the moved pins are Worker-added, and every pre-existing assertion survives.

## §14 Slice 1 ACCEPTED; slice 2 issued

Exchange 05 returned implementation-PASS: commit `19688758a589eb6c7034ca30ea9928cecd6bbc7b`
("feat(gamecore) importable engine self-play core"), five files, +1108/−410. ORCHESTRATOR
re-verification, all green: readback local == remote == `1968875`; porcelain clean; exactly five
files; `move_search.py` untouched (grep count 0); mypy `Success: no issues found in 86 source
files`; ruff clean; full pytest re-run by me `828 passed, 4 skipped in 497.31s`. Deterministic
mode verified in source: `_PARITY_RANKED_MAX_NODES = 20_000`, `_PARITY_MAX_ELAPSED_MS =
10_000_000`, reason comment present, `node_bound` switch selecting parity vs production bounds,
D-S1 options visible (`include_pass_streak=True`, `strict_unknown_tile=None`). Worker deviation
accepted: an extra PRE-COMMIT ls-remote equality check beyond the required pre-push one (same
authorized network class, conservative). Near-miss noted: matrix record-cache isolation needed for
node-mode records. One Worker LEAD accepted: pins protect the selected deterministic
configurations, not every possible game.

⇒ **Slice 1: implementation-PASS accepted at E1 (direct Orchestrator acceptance; no independent
acceptance required by the plan for this slice).**

Slice 2 issued (03_implementation_00.md, session 03 exchange 01, fresh session, apfieldcheck 0/0):
diagnostic vocabulary only — `ai-match` + `model-position` report kinds, typed ply-metric record
(D2a field list, None = not measured), schema $defs, and the fix for the DECORATIVE schema test
(no test does full JSON-Schema validation today — only artifact.const + required). Two traps
written in: (1) ⭐ redaction field-name trap — SECRET_KEY_FRAGMENTS contains `prompt`, `token`,
`env`; a field named `seat_prompt_id` would be silently dropped by redacted_copy; F4 requires
field-by-field survival proof; (2) validator decision — use jsonschema ONLY if already installed
transitively, never add a dependency. Fail-before F1/F2 captured. gamecore byte-frozen.

## §15 Slice 2 ACCEPTED; slice 3 SPLIT (D-S3) — generator first, LLM scorer after slice 4

Slice 2 re-verified by the ORCHESTRATOR, all green: readback local == remote == `49fb8ea`;
porcelain clean; exactly 4 files (+841/−5); schema enum = 5 values; new symbols present; mypy 86
clean; ruff clean; **full pytest re-run by me: 835 passed, 4 skipped in 495.65s.** F1-F6 evidence
carried; the decoy `token` field correctly dropped by redacted_copy in F4. Worker critique
RECORDED for the runner slice: `first_validate_valid`, `earlier_attempt_failures`, `steps_consumed`
have NO persisted source today; `malformed_or_non_tool` / `give_up_while_legal` are stream/409
classifications ⇒ the slice-5 runner must keep SSE/409 evidence, not read ai_metadata alone.

**⇒ Slice 2: implementation-PASS accepted at E1 (direct Orchestrator acceptance).**

**Amendment D-S3 (Orchestrator, plan-sequencing): slice 3 SPLIT.** The plan's slice 3 ("position
set + CLI scorer of a catalog pair, cap 24 live") has a hidden dependency: scoring a model position
requires a persisted diagnostic session to drive the pipeline against — slice 4 machinery.
Force-fitting it now would mean a second scenario-apply implementation over the legacy string
board. ⇒ **3a = position-set generator, provider-free, ZERO live calls** (issued as
04_implementation_00.md, session 04 exchange 01, apfieldcheck 0/0); **3b (LLM scorer, cap 24)
follows slice 4** and keeps the cap. The Worker's persistence critique reinforces the split.

Design essentials of 3a: node-bound capture (20k nodes / 10M ms — the slice-1 wall-clock lesson
applied so the ASSET is byte-stable; production-750ms numbers never baked into assets), structured
`{token, blank_as}` cells (the mec-13-D05 lesson — no joined strings), per-snapshot tile
conservation asserted in the generator, `conditions_digest`, `set_digest`, asset envelope
`libretiles.position-set/v1`, `observe_source_revision` for provenance, write_report_atomically,
command house style exit 0/2. Fail-before F1/F2. Zero edits to existing files.

Also surfaced to the Cooperator: jsonschema/fastjsonschema NOT installed (transitive check empty);
F3 is a hand structural check; a full validator is a Cooperator decision candidate for a later
slice. And: NIM live grant (K1, 8-12 calls) will be requested at slice 3b/5 acceptance.

## §16 Slice 3a ACCEPTED; correction exchange 02 issued (self-contained snapshots)

Slice 3a re-verified by the ORCHESTRATOR, all green: readback equal at `08dd2c6`; porcelain clean;
4 NEW files +3622, zero edits; mypy 88 source files clean; ruff clean; **full pytest re-run by me:
841 passed, 4 skipped in 518.93s.** Phase rule measured and hashed into conditions_digest
(tile-pool occupancy, not 225 squares — a real trap avoided); committed 3-position sample
`set_digest 3e5eb049…`. ⇒ **implementation-PASS accepted at E1.**

**Correction exchange 02 issued** (04_implementation_01.md, Bounded Correction Worker,
current-worker-session, apfieldcheck 0/0): the Worker's own critique named the gap — snapshots
store only to-move rack + bag COUNT, so slice 5 cannot mount a stored position without replaying
the generator (which would couple the stored digest to replay-time code). The accepted plan D4
already intended full state ("board/rack/bag/to-move"). Correction: every snapshot adds
`opponent_rack` + ordered `bag_tiles` (runner-side info; ⛔ nothing model-facing changes), the
committed fixture becomes the DEFAULT 24-position english set, digests re-pinned, F8 fail-before
captured. Rejected alternative recorded: replay-from-seed contract.
Worker LEAD noted and deferred: engine_baseline is ranked-best only (the MQR denominator); per-
policy denominators can be re-searched by the runner if ever needed — not this slice.

## §17 Exchange 02 accepted; completeness pass issued (exchange 03) to end the gap sequence

Exchange 02 re-verified by the ORCHESTRATOR, all green: readback equal at `3faa3f8`; fixture
replaced (3-position → 24-position, +24 487 lines); mypy 88 clean; ruff clean; **full pytest re-run
by me: 842 passed, 4 skipped in 520.46s.** F8 fail-before captured (11 keys before, opponent_rack +
bag_tiles after); new fixture digest `8d40f3bc…`. ⇒ **accepted.**

**Correction exchange 03 issued** (04_implementation_02.md, apfieldcheck 0/0): two single-field
corrections in a row is the "fourth gap" pattern ⇒ the correction changes KIND: the Worker
ENUMERATES the complete mid-game state surface of Game+PlayerState (what affects legality, scoring,
endgame, final scores), captures every missing field (minimum: per-cell premium_used, per-seat
scores, scoreless-turn counter; more if measured), and PROVES self-containedness with F9
mount-equivalence: reconstruct a Game purely from snapshot fields, run one node-bound ranked
decision, assert it equals the recorded decision — at generation time, for EVERY snapshot.
"A snapshot that fails F9 is not a position — it is a picture of one." Reconstruction helper stays
in position_sets.py with gamecore-only imports (gamecore itself byte-frozen).
This closes slice 3a+corrections pending acceptance; slice 4 (diagnostic session, E3) next.

## §18 Exchange 03 accepted; micro-exchange 04 closes slice 3 (digest identity)

Exchange 03 re-verified by the ORCHESTRATOR, all green: readback equal at `c9396f4`; fixture
replaced (f4d334c8, 45 463 lines — complete state); mypy 88 clean; ruff clean; **full pytest re-run
by me: 843 passed, 4 skipped in 538.19s.** The state-surface enumeration is the deliverable of the
exchange: premium_used, seat_names/scores/pass_streaks, consecutive_scoreless_turns, ended/
end_reason/leftover_points/winner_name, no_moves_available, bag_rng_state (lossless getstate) all
captured; Cell.premium deliberately omitted (layout, reloaded from asset); F9 mount-equivalence
passed on ALL candidate plies of seeds 300-302, nodes compared. ⇒ **accepted.**

**Micro-exchange 04 issued** (04_implementation_03.md, apfieldcheck 0/0): the Worker's LEAD is a
real identity defect — same digest + changed premiums layout = different content. Fix:
conditions_digest gains SHA-256 of the premiums layout AND the variant lexicon asset(s), listed as
an asset_digests map inside the envelope; fixture regenerated; F10 fail-before. Slice 3 then CLOSED
pending acceptance; slice 4 (E3 diagnostic session, independent acceptance) next, issued fresh.

## §19 Exchange 04 accepted; closing micro-exchange 05 — digest rule becomes a closed CLASS

Exchange 04 re-verified by the ORCHESTRATOR, all green: readback equal at `51fa78e`; asset_digests
map (premiums.json `65d712b9…`, collins2019.txt `97e6d721…`) inside the envelope AND the
conditions payload; F10 composition shape (mutate the map, never the real assets — real
premiums/dicts never written); mypy 88 clean; ruff clean; **full pytest re-run by me: 844 passed,
4 skipped in 557.04s.** ⇒ **accepted.**

**Micro-exchange 05 issued** (04_implementation_04.md, apfieldcheck 0/0): the Worker's LEAD
(variant JSON outside the hash) is the same class as the two hashed assets — so instead of a third
instance patch, the rule closes by construction: `collect_asset_digests` hashes EVERY content asset
resolved through the asset helpers (premiums, lexicon, two-tile file when present, variant
definition JSON), derived from the SAME resolution calls the generator makes; the docstring states
the boundary: digest = configuration + content assets; code identity = generator_source_revision.
Any future correction is a new finding, not this rule failing. Slice 3 closes after this exchange
pending acceptance; slice 4 (E3, independent acceptance) next.

## §20 Slice-4 PLANNING accepted; slice-4 implementation prompt issued

Session 05 exchange 01 was a PLAN-ONLY exchange (05_implementation_00.md; ⚠ meta-naming wrinkle:
the file carries phase "implementation" in its name but `Native planning mode: required` in its
body — historical artifact, NOT retroactively renamed). The Worker honoured AP over my prompt's
leftover implementation clauses (gates/commit/push in a plan-only grant — MY defect) and falsified
five of my prompt's claims at `01ade17`: DiagnosticRun/is_diagnostic do NOT exist; a migration IS
required (0009); create_game has no seed kwarg (seed is random inside _initialize_session); slice 3
did NOT ship an admin-registerable target (that is slice 7); `_check_active_turn` (not
`_check_active_term`). All five verified by me directly — the Worker was right on every one.

The planning report's key MEASURED finding: **unconditional acting_slot = current_turn_slot is NOT
product-identical** — product `get_ai_context` ignores turn and always returns first-AI (slot 1);
`current_turn_slot` is nullable; four first-AI sites exist (:487 central, :1621 validate_move_for_ai,
plus set_game_ai_*). The accepted design: `_resolve_acting_ai_slot` branch (diagnostic →
current_turn_slot with fail-closed None; product → first AI), get_ai_context split into
membership/acting/opponent roles, abort outside _reject_ai_nonscoring, history filter in the
SERVICE, admin dashboard exclusion, service user seeded by migration (JWT identity only — provider
secrets stay on Next.js, R2=A).

⇒ **Plan ACCEPTED.** Cooperator re-confirmed R1=ano R2=A R3=L4 R4=200 R5=A (unchanged from §8.3).

**Slice-4 implementation prompt issued** (06_implementation_00.md, session 06 exchange 01, fresh
session, not-used, E3, apfieldcheck 0 defects): migration 0009 with the FULL DiagnosticRun D7
schema + partial unique in-flight constraint + bag_rng_state (nullable) + RunPython service user;
create_diagnostic_game / apply_position_snapshot / _resolve_acting_ai_slot / abort_diagnostic_run /
list_games_for_user filter / build_ws_ticket refusal / admin exclusion; F-A..F-K fail-before
table; provider calls ZERO; gamecore + position_sets byte-frozen; independent acceptance (slice
4-IA, INFOSEC 4.4, R3) in a SEPARATE fresh session afterwards; K2 probe before slice 5.

## §21 Slice 4 implementation ACCEPTED (pending independent audit); slice 4-IA issued

Session 06 exchange 01 (06_implementation_00.md) returned implementation-PASS at
`0ffaf46023018c5f9b33faaef41c64b857e2aa55` ("feat(game) diagnostic session foundation with two AI
seats"). ORCHESTRATOR re-verification, all green: readback local == remote == `0ffaf46`; porcelain
clean; 5 files (+938/−24); migration 0009 present; `ended_at` on DiagnosticRun (Worker's justified
addition — abort writes it); in-flight lock is UniqueConstraint(Value(1), condition=Q(...)) — the
Worker CORRECTED my `fields=["status"]` shape, which would have allowed one queued AND one running
simultaneously (their claim verified as the right semantics); per-seat PlayerSlot catalog FKs
(justified — get_ai_context acting-slot FKs); no DiagnosticPly (deliberately deferred to slice 5
migration — Worker LEAD recorded); mypy 89 source files clean; ruff clean; **full pytest re-run by
me: 862 passed, 4 skipped in 547.80s.** F-A..F-K all captured with verbatim pre-fix values
(including the 16-failure migration-teardown near-miss, root-caused and repaired via the
catalog.0003_aiprompt dependency — a REAL infrastructure lesson recorded).

Notable Worker findings accepted: views.py untouched (service-layer filter proven sufficient);
`game_from_snapshot` import deferred inside the mount function (circular import); near-miss
discipline excellent.

⇒ **implementation-PASS accepted at E3 with combined envelope; final acceptance requires the
separate fresh independent audit.**

**Slice 4-IA issued** (07_audit_00.md, session 07 exchange 01, fresh independent audit, INFOSEC
4.4, R3, apfieldcheck 0 defects): claims C1-C10 (service account identity, JWT mint surface,
object-level auth both directions, acting-slot identity + fail-close, history/dashboard exclusion
with the two named residuals to disposition, abort integrity proven independently, migration
soundness incl. the Value(1) constraint claim, invariants untouched, snapshot mount fail-closed,
no secret materialization). Per-claim verdicts verified-closed | not accepted; full finding
records; zero provider calls; read-only; the auditor never corrects.

## §22 Slice 4-IA: PARTIAL — F01/F02/F03 blocking; correction exchange 08 issued

Independent audit (07_audit_00.md, session 07) returned PARTIAL: C3,C4,C5,C6,C8,C9,C10
verified-closed; **C1, C2, C7 NOT accepted** — findings F01 (medium, blocking: mutable username
permits adoption of a password-enabled diagnostic identity; only the `created` branch calls
set_unusable_password — verified by me at services.py:1144), F02 (low, blocking: the service bearer
creates product games, joins human matchmaking, appears as an opponent), F03 (medium, blocking:
migration reverse unconditionally deletes by username and drops is_diagnostic classification).
F04 (low, NON-blocking: SimpleJWT persists minted refresh tokens in DB, visible in token admin —
existing library behaviour; disposition: accepted residual for slice 4, MUST be dispositioned in
slice 5 when the runner mints: token type/lifetime/storage policy, never echo tokens).
F05/F06 rejected-false-positive (staff-only dashboard rows; ws verifier gap unreachable without
signing authority) — accepted as dispositioned.

Audit quality: exemplary — reproduced-dynamic evidence with in-memory containment (zero temp
roots on disk), per-claim verdicts, honest limitations (standards not refreshed under no-network;
recorded, not hidden). ⇒ **Slice 4 acceptance WITHHELD pending correction + re-audit.**

**Correction exchange 08 issued** (08_correction_01.md — first draft was garbled by a tool error
and REWRITTEN clean; apfieldcheck 0 defects). ONE coherent correction unit covering all three
blocking findings (one root: unreserved, unprotected service identity):
· F01 → fail-closed LOUD: a usable-password claimant on the reserved username RAISES in
  ensure_diagnostic_service_user (never silently revoke — the destructive twin of F03 — never
  silently adopt);
· F02 → `_reject_service_account_user` guard at create_game + queue-join entries (exactly one
  constant, no prefix rule);
· F03 → reverse deletes ONLY the unusable-password managed account; is_diagnostic classification
  loss on rollback recorded as an ACCEPTED residual in the reverse docstring.
Regression tests F-L..F-P with verbatim fail-before. Re-audit (session 09, fresh) is REQUIRED
(INFOSEC 4.4/15) and dispatched by me, never by the corrector.

## §23 Correction accepted (pending re-audit); session 09 re-audit issued

Session 08 (08_correction_01.md) returned implementation-PASS at
`f6c9db913450d56ade4399ec5d2e6a3cd807e347` ("fix(game) fail-closed reserved diagnostic service
identity"). ORCHESTRATOR re-verification, all green: readback local == remote == `f6c9db9`;
porcelain clean; 3 files (+155/−1); mypy 89 clean; ruff clean; **full pytest re-run by me:
867 passed, 4 skipped in 549.96s.** F-L..F-P verbatim fail-before (4 failed pre-fix / 5 passed
post). Throwaway-DB migration round-trip proves F03 end-to-end: claimant KEPT (password intact,
check_password true), managed account deleted/recreated, re-forward WITH claimant fails LOUD with
the operator message (ImproperlyConfigured during 0009 RunPython). Worker judgment calls accepted:
ImproperlyConfigured as the established loud type, converted to the existing `ok:False` payload at
the two service entries (400 without views.py); `is_password_usable()` in the reverse (historical
migration models lack the method — same predicate, documented); near-miss recorded and MEASURED
(those two functions raise that type only from the new guard).

⇒ **Correction accepted as implementation-PASS; slice-4 acceptance still WITHHELD** pending the
mandatory fresh re-audit (INFOSEC 4.11).

**Re-audit issued** (09_reaudit_00.md, session 09, fresh, independent of implementer and original
auditor, apfieldcheck 0 defects): R-F01 (incl. ⭐ case-variant normalization probe and the
explicit question whether fail-closed-by-exception is a sound substitute for the auditor's
"immutable managed identity" or moved the risk), R-F02 (incl. other player-participation path
enumeration), R-F03 (incl. the is_password_usable predicate check), R-REG (C3-C10 spot-check,
invariants byte-identity across 0ffaf46..f6c9db9). Verdicts verified-closed | not accepted per
finding. Residuals recorded: profile-rename surface (accounts/**), queue-cancel unguarded
(join refused ⇒ no new waiting rows), F04 token policy owed at slice 5.

## §24 Re-audit: R-F01/R-F03 closed, R-F02 SURVIVED via profile rename; correction-2 issued (flag mechanism)

Session 09 re-audit returned PARTIAL: **R-F01 verified-closed** (fail-closed ensure proven incl.
migration loud-abort with claimant; case-variant probe measured: NFKC normalization preserves case,
exact-equality lookup — case variants are distinct users, rename of a case-variant TO the reserved
name correctly 400s), **R-F03 verified-closed** (claimant preserved on reverse; is_password_usable
≡ has_usable_password for this purpose; classification-loss residual documented), **R-F02 NOT
accepted** — the service bearer PATCHes its own profile username (accounts/serializers.py:40,
username NOT in read_only_fields — verified by me), freeing itself from the username-equality
guard, then create 201 + matchmaking 200 with the SAME JWT. Reproduced-dynamic P03→P09 chain.
C3-C10 spot-check clean: 350 other tracked entries byte-identical, invariants untouched, no new
secret materialization.

**Orchestrator decision on the convergence point:** the username-guard assumption did NOT survive
correction + recheck. Per the finite-convergence contract this is the escalation point — and the
decision is mine: the mechanism CHANGES to the auditor's original direction (durable immutable
managed identity), not a repeat of the same assumption. ⇒ **Correction-2: `is_service_account`
BooleanField on User** (accounts/models + 0005 AddField), serializer blocks rename of the flagged
account, guards switch to flag-OR-reserved-username, game/0009 dependencies gain accounts/0005
(⭐ migration-ordering trap: fresh DBs must run accounts/0005 BEFORE game/0009's RunPython, which
sets the flag). This is a DESIGN CHANGE with new material evidence (the demonstrated bypass), not
a repeated cycle.

**Correction-2 issued** (10_correction_00.md, session 10, fresh, apfieldcheck 0 defects): allowlist
crosses into accounts/** FOR THE FIRST TIME with an explicit grant (models field, 0005 migration,
one validator) — the previous forbidding was MY scoping choice, now revised by the re-audit
evidence. F-Q..F-U incl. the re-auditor's exact P03→P09 sequence (F-R) and fresh-DB ordering proof
(F-U). Re-audit session 11 afterwards; slice-4 acceptance still withheld.

## §25 Correction-2 accepted (pending re-audit-2); session 11 issued

Session 10 (10_correction_00.md) returned implementation-PASS at
`6049f2895321da33c7594aedd922aef63544e18d` ("fix(accounts) durable service-account flag closes
rename bypass"). ORCHESTRATOR re-verification, all green: readback local == remote == `6049f28`;
porcelain clean; 6 files (+186/−9); mypy 90 source files clean; ruff clean; **full pytest re-run by
me: 872 passed, 4 skipped in 551.56s.** F-Q..F-U verbatim fail-before (rename 200 → create 201 →
queue 200 pre-fix; all refused post-fix, no product/vs_human rows). Fresh-DB ordering PROVEN
(`ORDER_PROOF 29 < 30`; seeded flag True); existing dev DB `showmigrations` quiet (0005 unapplied).

Worker-honest deviations: (1) the dependency line makes an already-0009-applied DB raise
InconsistentMigrationHistory on the next `migrate` until 0005 applies — ONE command recovery,
verified in re-audit V-ORD; belt-and-braces username branch covers participation meanwhile;
(2) Django Admin UserAdmin username edit remains a rename surface BUT the flag survives it, so
participation guards hold (staff can only free the reserved NAME, loudly caught by F-L);
(3) registration create-path intentionally not blocked by the validator (uniqueness + F-L own it).
⇒ **Correction-2 accepted as implementation-PASS; slice-4 acceptance still WITHHELD** pending
re-audit-2.

**Re-audit-2 issued** (11_reaudit_00.md, session 11, fresh, apfieldcheck 0 defects): V-F02
end-to-end (incl. the guard-bypass hunt and the boundary statement that the flag marks THE managed
account and is an attribute an attacker cannot set), V-F01/V-F03 closure persistence, V-ORD
both migration paths INCLUDING the existing-DB one-command recovery reproduced on a shaped
throwaway DB, V-REG spot-check. Residuals standing: profile-rename surface now BLOCKED for the
flagged account; admin username edit = staff-only, flag survives; F04 token policy owed at slice 5;
caller-boundary (created_by staff check) owed at slice 5.

## §26 Re-audit-2: F02/F01/F03 closed; NEW F07 (high, blocking — MY defect); correction-3 issued

Session 11 re-audit-2: **V-F02 / V-F01 / V-F03 all verified-closed on a migrated schema** (flag
boundary proven; guard-bypass hunt found no player-reachable path; belt-and-braces username branch
is a live second semantics — namespace lock, not a second setter). **BUT V-ORD(b) NOT accepted →
NEW FINDING F07 (high, blocking):** correction-2's dependency edit on the ALREADY-APPLIED game/0009
strands existing databases — `showmigrations` quiet but EVERY migrate form raises
InconsistentMigrationHistory, accounts/0005 can never apply, and the missing column breaks the
whole User ORM (OperationalError) on the Cooperator's dev DB. The session-10 operator story
("one normal migrate resolves it") was FALSE — my scoping verified only `showmigrations`.
**F07 is MINE: I authorized the dependency edit and under-verified the existing-DB shape.**

⭐ IMMEDIATE OPERATOR IMPACT: the Cooperator's dev DB is stranded NOW (app breaks on any User
query). Rescue = wait for correction-3 + one migrate (repo-consistent), or an immediate
paste-safe owner-command SQL block (column + django_migrations row + flag backfill). Both offered;
rescue-now recommended so daily use continues while session 12 runs.

**Correction-3 issued** (12_correction_00.md, session 12, apfieldcheck 0 defects): migration
OWNERSHIP restructure per the re-auditor's direction — 0009 RETURNS TO PURE SCHEMA (dependency
line removed, seeding RunPython removed, user-deletion removed from reverse); NEW game/0010
(depends accounts/0005 + game/0009) owns seeding (ensure, idempotent) + the ownership-aware
reverse. Both shapes proven: existing-stranded → ONE migrate applies 0005+0010, flag True (F-V);
fresh-from-zero → 0009 schema-only → 0005 → 0010 seed+flag (F-W). services.py untouched (ensure
unchanged; the only ensure-call that ran with a missing column was 0009's, now moved). F-P/F-U
re-pointed; F-K/F-L/F-M/F-Q/F-R must stay green unmodified.

## §27 Session 12 BLOCKED resolved (environmental); re-audit-3 issued; ROTATION — 91_orchestrator-handout-1.md written

Session 12 (12_correction_00.md) returned BLOCKED with zero mutation: the migration restructure
passed EVERYTHING focused (F-V verbatim pre-fix InconsistentMigrationHistory captured; post-fix ONE
migrate applies 0005+0010, flag True; F-W fresh shape; reverse ownership verified; 30+2 focused
passed) but the FULL pytest showed `10 failed, 864 passed` — eight test_multiplayer_ws + two
test_ws_ticket_single_use — in the Worker's DEGRADED environment (PYTHON_DOTENV_DISABLED=1 +
synthetic secret + DJANGO_DEBUG=true), baseline equivalence unestablished. Worker stopped correctly
under "gate failure outside the allowlist".

**ORCHESTRATOR resolution (measured):** 19 passed on the focused ws files and **874 passed, 4
skipped FULL** in the NORMAL environment on the same uncommitted tree ⇒ the 10 failures were
ENVIRONMENTAL, not a regression. Correction-3 validated by me as implementation-PASS-equivalent
evidence; the commit itself is still unauthorized pending re-audit-3.

**Re-audit-3 issued** (13_reaudit_00.md, session 13, apfieldcheck 0 defects): both DB shapes on
throwaway DBs, closure persistence spot-checks, the environmental-equivalence fact labelled, diff
scope. Predeclared acceptance rule: verified-closed F07 + persisted closures ⇒ authorize the ONE
corrective commit (implementer session expired) ⇒ **slice-4 acceptance-PASS**.

## ⭐ ROTATION at this coherent boundary

The Cooperator asked for a fresh Orchestrator handout (context integrity; the remaining work is
K2 → 5 → 3b → 6 → 7 → 8 → final 4.6 audit → closure). Written:
`91_orchestrator-handout-1.md` (D-15 band) with a full Handout Integrity Record, the exact commit
chain, locked decisions (R1-R5, L4, flag identity, migration ownership, node-bound fixture
doctrine), the F01-F07 disposition ledger (F04 owed at slice 5), per-step decision-complete specs
for K2/5/3b/6-8, and this session's six lessons (wall-clock pins; never depend an applied migration
on a new one — verify the OPERATOR story via migrate on a shaped DB; worker-env baseline
equivalence; enumeration discipline; correction-loop cost; BLOCKED-as-protocol-working).
Session 12's tree stays UNCOMMITTED by design until re-audit-3's verdict authorizes the commit.

## §28 FINAL — re-audit-3 verified-closed; slice-4 acceptance-PASS DECLARED; commit f17a8ba; ROTATION COMPLETE

Re-audit-3 (session 13, 13_reaudit_00.md + report): **PASS, every verdict verified-closed** —
V-F07(a) existing-DB rescue by ONE normal migrate (applied 0005+0010, account preserved, flag
True, unusable password) · V-F07(b) fresh-from-zero (0005 < 0009 < 0010, no exceptions) ·
V-F07(c) reverse ownership (0010 keeps claimants/deletes managed; 0009 has NO RunPython) ·
V-F07(d) graph sanity both shapes · V-F02/F01/F03 persistence (28 diagnostic tests + guard shape
flag OR reserved-username) · V-ENV (focused ws 19 passed in normal env; the Orchestrator's 874
full-suite run remains attributed evidence) · V-REG (porcelain exactly 3 paths; gamecore +
invariants byte-identical; parameters_json unchanged). No new findings. Containment: one temp
root, cleaned and verified.

**ORCHESTRATOR executed the predeclared acceptance rule:** corrective commit landed
`f17a8ba0dc0e0d97da770e2ed2238190b6e432b1` (explicit 3-path staging; pre-push gate vs 6049f28;
pushed; readback equal) with the ORCHESTRATOR's final gate set on the exact committed tree —
mypy `Success: no issues found in 91 source files`, ruff clean, pytest `874 passed, 4 skipped in
559.84s`.

# ⭐ SLICE 4 ACCEPTANCE-PASS DECLARED (E3, independent audit trail 07→09→11→13, four verification
#    cycles, three corrections, zero unresolved findings)

**Whole state at handover:** slices 1, 2, 3, 4 CLOSED/ACCEPTED at `f17a8ba`; remaining work
K2 → 5 → 3b → 6 → 7 → 8 → final INFOSEC 4.6 audit → closure — fully specified in
`91_orchestrator-handout-1.md` (finalized this session: F07 ledger closed, step 1 marked DONE,
first bounded step = K2, final gate numbers recorded). Rotation COMPLETE. `14/00-ai-opponent-
strength/00_handout.md` waits for 11/00 closure. — Howgh.

---

## §29 SUCCESSOR Orchestrator — Stage 1 restoration and gate verification (2026-09-06)

Written by the FRESH Orchestrator restored from `91_orchestrator-handout-1.md` + `00_handout.md`.
Reading completed: root `AGENTS.md`, `frontend/AGENTS.md`, pinned `.ap` corpus (AP_ORCHESTRATOR.md
and INFOSEC.md in full; AP.md/PROMPT_CONTRACTS.md via `AP_DESTILLED.md` line index — enums and
field blocks will be re-read from the pin before each prompt, never recalled), `AP_DEFECTS.md`,
`PROJECT_CONTEXT.md`, this notes file §1-§28, both handouts.

### 29.1 Stage 1 repository gate, measured directly this session

```text
git rev-parse HEAD          f17a8ba0dc0e0d97da770e2ed2238190b6e432b1
git rev-parse HEAD:.ap      9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD   9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   (detached — correct)
git status -sb              ## main...origin/main
git status --porcelain=v1   EMPTY
git ls-remote origin        f17a8ba0dc0e0d97da770e2ed2238190b6e432b1  refs/heads/main
HEAD subject                fix(game) move service-account seeding to 0010 to unstrand applied
                            0009 databases
```

Local HEAD == remote-tracking == public main. AP pin intact. Tree clean — exactly the inherited
state (`91_` §1: "Your inherited tree is CLEAN").

### 29.2 Standing backend gates re-measured at `f17a8ba` (RF-16 alternate route, one run)

```text
mypy config game gamecore accounts catalog   Success: no issues found in 91 source files
ruff check .                                 All checks passed!
pytest                                       874 passed, 4 skipped in 543.30s (0:09:03)
```

Identical numbers to the handover set (`91_` Integrity Record FINAL UPDATE). Frontend gates NOT
run: no frontend file touched since handover; `npm run build` writes `.next/` and is not a
read-only gate (same posture as §1.2).

### 29.3 K2-relevant fact re-measured at `f17a8ba`

`frontend/src/lib/ai-play-diagnostic.worker.test.ts` imports `NextRequest` from `next/server`
(:2), mocks `@/lib/ai-runtimes` (:29), and dynamically imports `@/app/api/ai/move/route` (:68,
:98) — the `@/*` alias + NextRequest dependency the K2 probe must decide for a PLAIN Node process.

### 29.4 Blocking question re-asked

Per `91_` §6: asked the Cooperator in one line whether any other Orchestrator is active
(13/00 was closed before this whole started; 14/00 exists only as a written handout waiting for
11/00 closure). **Answer: `nie` (2026-09-06)** — no other Orchestrator is active. Gate cleared.

---

## §30 K2 — Node runtime probe: ⭐ PROVEN. Slice 5 uses L4.

Executed ORCHESTRATOR-DIRECT (Cooperator decision 13; mechanical read-only measurement, zero repo
mutation, zero provider calls). ⛔ Evidence is permanently NON-INDEPENDENT; slice 5 re-proves the
mechanism by construction against a live backend.

### 30.1 Question and verdict

Can a PLAIN Node process (`node script.mjs` — not vitest, not the Next.js server) import
`frontend/src/app/api/ai/move/route.ts`'s POST handler and invoke it with a synthetic
NextRequest? **YES — proven twice at `f17a8ba`, once per hook API variant.**

```text
IMPORT_OK typeof POST = function
INVOKE_OK status = 200 content-type = text/event-stream
SSE terminal: {"type":"error","code":"provider_unavailable","error":"This free rival is
  temporarily unavailable. ...","provider_path":"","runtime_model":"probe/model"}
```

The route module loaded with ALL transitive TS imports (model-catalog, ai-runtimes, prompts,
provider-logging) plus npm deps (`ai`, `zod`, `next/server`); POST executed its real logic and
emitted the redacted SSE error terminal after failing fast against the closed loopback backend.

### 30.2 The exact runtime machinery required (the handout's demanded declaration)

```text
1  Node v26.4.0 NATIVE TypeScript type stripping — no flag, no tsx, no esbuild, no bundle.
   (esbuild is NOT in frontend/node_modules; rolldown and jiti are — neither was needed.)
2  A ~30-line module resolve hook registered via `node --import ./register.mjs`, providing:
   · alias mapping  "@/..."  →  frontend/src/...
   · extension retry for extensionless specifiers: .ts / .tsx / .js / /index.ts
     (".js" is needed because `next/server` has no exports map entry and Node ESM demands
     `next/server.js`)
3  frontend/node_modules present — bare specifiers resolve from the IMPORTING FILE's location,
   so route.ts under frontend/src resolves next/ai/zod naturally; only the /tmp probe file
   needed a parent-URL fallback.
```

Both hook APIs proven: `module.register()` (async; emits DEP0205 deprecation warning) and
`module.registerHooks()` (sync, non-deprecated — ⭐ the slice-5 worker should use THIS one).

Hook logic, preserved verbatim (throwaway files deleted per containment ledger):

```js
// registerHooks variant (slice-5 shape). SRC = <frontend>/src/
registerHooks({
  resolve(specifier, context, nextResolve) {
    let s = specifier;
    if (s.startsWith("@/")) s = pathToFileURL(SRC + s.slice(2)).href;
    try { return nextResolve(s, context); }
    catch (err) {
      for (const ext of [".ts", ".tsx", ".js", "/index.ts"]) {
        try { return nextResolve(s + ext, context); } catch { /* keep trying */ }
      }
      throw err;
    }
  },
});
```

### 30.3 Zero-egress containment (ledger, closed)

```text
/tmp/opencode/k2/{hook.mjs,register.mjs,register2.mjs,probe.mjs}   owner: this session
  contents: throwaway probe scripts only — no secrets, no repo paths mutated
  network: BACKEND_URL=http://127.0.0.1:1 (closed loopback port); NO provider credentials in the
  environment (frontend/.env.local never read); zero provider calls; zero external egress
  cleanup: DONE — exact four paths deleted, directory removed
```

### 30.4 Honest caveats

```text
· The probe exercised the ERROR path (backend unreachable → SSE error terminal), not a full fake
  turn: a full turn needs a live Django backend for validateMove regardless of runtime, which is
  slice-5 territory ("⛔ do not let this become a runtime-migration project"). Import + invocation
  + real SSE emission is the decision-quality proof of the RUNTIME question; the full tool-loop
  logic is separately proven under vitest (ai-play-diagnostic.worker.test.ts) and slice 5 re-proves
  it against a live backend.
· Node type stripping is ERASABLE-SYNTAX-ONLY. No enum/namespace exists in the transitive graph
  today (it loaded); if one is ever introduced, the worker needs --experimental-transform-types.
  The slice-5 prompt should name this as a stopping condition, not silently add the flag.
· MODULE_TYPELESS_PACKAGE_JSON warning (reparse overhead): frontend/package.json has no
  "type": "module". ⛔ Do NOT "fix" that in slice 5 — it would change module semantics for the
  whole product. Accept the warning or pass a format hint from the hook.
```

⇒ **R3=L4 CONFIRMED OPERATIONAL: slice 5's model tier = ONE long-lived plain-Node worker per run
importing the existing POST handler via registerHooks + native type stripping.** L1 (HTTP to a
running Next.js) stays the allowed equivalent fallback per the locked decision.

---

## §31 Slice-5 planning prompt issued — session 14 exchange 01

```text
14_planning_00.md   session 14, exchange 01, fresh-worker-session, Native planning mode: required,
                    plan-only (Implementation-Planning Worker), E0 exchange / E3 subject matter,
                    network NONE, read-only, reasoning High (named risk: long-lived privileged
                    subprocess + minted service JWT (F04 owed) + first real provider spend in one
                    design). apfieldcheck: DEFECTS 0, WARNINGS 1 (the expected `required`-mode
                    reminder).
Deliverables D1-D11: runner process model (no-Redis background job, pid/heartbeat/cancel/crash) ·
                    runner loop (SSE/409 in-memory evidence, both instruments) · Node model-tier
                    worker (K2 mechanism inlined, IPC contract, aiSlot :438 parameterization,
                    token-no-echo) · DiagnosticPly schema + game/0011 · F04 token policy · admin
                    launcher (admin_view + has_change_permission + created_by staff, no base_url,
                    typed params only) · caps arithmetic (R4 200/1000, independent ceilings,
                    truncated + did_not_measure) · K1 live-grant design (8-12 NIM calls,
                    requests-per-ply) · INFOSEC threat model + routing · slice decomposition ·
                    prompt/sequencing critique.
Facts re-measured this session and inlined (never pointed at meta): DiagnosticRun full field list
                    (models.py:204-282), services symbols (:494/:1158/:1209/:1303/:1355/:1465),
                    mint precedent test_turn_probe.py:128-129, catalog/admin.py get_urls/admin_view
                    pattern, aiSlot hardcode ai-play-diagnostic.ts:438, worker-test import shape
                    (:29/:51/:68), AST guard scope, K2 hook + caveats (§30).
apfieldcheck fix history: initial run found 1 coordinate-consistency defect (report-format section
                    lacked the comma-form echo phrase the checker matches); report-format section
                    regenerated whole; clean on re-run. (Lesson 17 held: the checker caught it,
                    not the author.)
```

---

## §32 Slice-5 plan accepted; implementation prompt issued — session 15 exchange 01

Accepted the session-14 planning report as Orchestrator, with plan-level corrections (not a
targeted revision). Binding corrections baked into `15_implementation_00.md`:

```text
· SSE does not carry first_validate_valid / earlier_attempt_failures / steps_consumed —
  derive or store None; copy PlyMetricRecord from diagnostics.py, never from the garbled report
· SECRET_KEY_FRAGMENTS binds DiagnosticPly column names (`token` especially)
· Git is push to main, explicit-path staging; planner D10 "new branch" is wrong
· create_diagnostic_game signature frozen; launcher/helper updates caps after create
· abort_diagnostic_run always sets failed — cancel must NOT call it
· Caps default 0 today; launcher writes R4 defaults (200/1000 provider, 60 plies)
· No DiagnosticRunAdmin yet — add via get_urls + admin_view + has_change_permission
· aiSlot parameterization; product default remains 1
· Node env is a whitelist, never os.environ.copy(); JWT via LIBRETILES_AI_PLAY_JWT only,
  never argv / IPC JSON / logs / report / ply / parameters_json
· AccessToken.for_user only (no RefreshToken / no OutstandingToken)
· L4 Node worker required; L1 HTTP fallback out of this slice
· Fake mode only; LIVE_SENTINEL set → refuse; K1 not this slice
· backend/var/ gitignored if reports go there
```

```text
15_implementation_00.md   session 15, exchange 01, fresh-worker-session, Native planning mode:
                          not-used, Fresh Implementation Worker, E3, fake mode, provider calls
                          ZERO. apfieldcheck: DEFECTS 0, WARNINGS 0.
Exact baseline still:     f17a8ba0dc0e0d97da770e2ed2238190b6e432b1
AP pin still:             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

---

## §33 Slice-5 implementation-PASS accepted; 5-IA issued — session 16 exchange 01

Worker session 15 report archived as `15_report_00.md` (pair with `15_implementation_00.md`).

```text
Public main:              a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
                          feat(game) fake-mode diagnostic runner with ply persistence
Parent:                   f17a8ba0dc0e0d97da770e2ed2238190b6e432b1
Diffstat:                 14 files, 2569 insertions, 3 deletions — matches claimed allowlist
AP pin:                   9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Porcelain:                empty; local HEAD == origin/main == ls-remote
```

Orchestrator independent checks (non-IA, do not replace 5-IA):

```text
· abort_diagnostic_run body unchanged; cancel_diagnostic_run is a separate helper (cancelled, never failed)
· mint_diagnostic_access_token is AccessToken.for_user + set_exp; production caller is the command only
· IPC _send_turn kwargs have no token field; Node reads LIBRETILES_AI_PLAY_JWT
· Node env is a constructed whitelist, not os.environ.copy()
· DiagnosticRun schema untouched; DiagnosticPly is shape B; 0011 depends on 0010
· diagnostics.py / position_sets.py / 0009 / 0010 / package.json / SIMPLE_JWT: empty diff
· focused pytest tests/test_diagnostic_runner.py → 24 passed in 4.75s (re-run here)
· full suite 898/4 in 554.30s is the IMPLEMENTER's number — 5-IA re-runs the standing gates
```

Implementer critique that §3.2 contained "Do not generate new assees, or steps_consumed": adjacent
lines in the issued prompt were intact (`Do not generate new assets` then separately the SSE
non-carriage of `steps_consumed`). Treat as implementer wrap-misread, not a prompt defect.

Next: slice 5-IA (INFOSEC 4.4, R3) — `16_audit_00.md`. Not K1, not 3b, not 4.6.
K1 remains after 5-IA (and any correction/re-audit) lands.

---

## §34 Slice 5-IA accepted; residuals dispositioned — session 16

Audit report archived as `16_report_00.md` (pair with `16_audit_00.md`). Candidate unchanged:
`a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20`. Containment `/tmp/opencode/s5-ia` verified absent.
Auditor re-ran standing gates: mypy 93 files, ruff clean, pytest `898 passed, 4 skipped in 551.84s`.
C1–C14 verified-closed. APMC-S4-IA-F04 **verified-closed**. F05/F06 not reopened.

Residual-risk decisions (PROMPT_CONTRACTS residual-risk contract). Severity low/info → Orchestrator
approver; no Cooperator sign-off required:

```text
Finding ID: APMC-S5-IA-F01
Decision: accepted-residual
Severity: low
Approver: Orchestrator
Regression test: DEBUG=false + wildcard ALLOWED_HOSTS must raise ImproperlyConfigured (settings suite)
Rationale: production posture already refuses the dangerous config at boot; Host→django_origin
  exfil is only the local DEBUG=true wildcard .env. Not a candidate-code defect.
Recorded in: 00_notes.md §34

Finding ID: APMC-S5-IA-F02
Decision: accepted-residual
Severity: low
Approver: Orchestrator
Regression test: AccessToken mint leaves OutstandingToken count unchanged
Rationale: revocation-until-expiry is the F04 policy that slice 5 deliberately chose (access-only,
  no persisted refresh). C2 found no echo. Product-game reach remains 404.
Recorded in: 00_notes.md §34

Finding ID: APMC-S5-IA-F03
Decision: accepted-residual
Severity: info
Approver: Orchestrator
Regression test: not applicable (documented test-harness override)
Rationale: LIBRETILES_DIAGNOSTIC_WORKER is local-actor tautology; production default is the
  committed worker; no HTTP writer of the override.
Recorded in: 00_notes.md §34
```

# ⭐ SLICE 5 ACCEPTANCE-PASS DECLARED (E3, independent 5-IA session 16, zero blocking findings)

Next: slice 3b (LLM scorer of the committed 24-position set, fake default). K1 live NIM still
deferred until after 3b fake lands. Slice 6 UI must not be pulled into 3b.

---

## §35 Slice-3b planning prompt issued — session 17 exchange 01

```text
17_planning_00.md   session 17, exchange 01, fresh-worker-session, Native planning mode: required,
                    plan-only, E0 exchange / E2 subject matter, network NONE, fake-mode 3b design
                    on top of the landed runner (no second loop, no slice-6 UI, no K1).
                    apfieldcheck: DEFECTS 0, WARNINGS 1 (expected `required`-mode reminder).
Exact baseline:     a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
```

---

## §36 Session 17 BLOCKED on native Plan mode; 3b plan reissued as not-used — session 18

Session 17 report (`17_report_00.md`): **BLOCKED**, zero mutation, D1–D7 unanswered. Cause:
`Native planning mode: required` vs client Default. Protocol-correct stop (AP.md:2468; the
capability was unavailable). Not a product defect.

Reissue per PROMPT_CONTRACTS.md:695-698: complete new prompt, `Native planning mode: not-used`,
explicit prompt-level read-only planning authority. Same D1–D7, same baseline `a17cdf4`.

```text
18_planning_00.md   session 18, exchange 01, fresh-worker-session, Native planning mode: not-used,
                    prompt-level planning authority explicit, plan-only, E0, network NONE.
                    apfieldcheck: DEFECTS 0, WARNINGS 0.
```

---

## §37 Session 18 plan accepted; slice-3b implementation grant — session 19

Planning report archived as `18_report_00.md` (pair with `18_planning_00.md`). Advisory, zero
mutation, baseline unchanged `a17cdf4`. Orchestrator **accepts** D1=B and D2–D7 with these
plan-level corrections baked into `19_implementation_00.md` (not a targeted revision):

1. D3 aggregates are an **authorized new contract**, not “already in slice-2 vocabulary”.
   `build_model_position_report` today emits only `sample_count` / `pass_count` / `fail_count`.
   Augment **after** that builder; do not retcon the envelope as already having MQR.
2. D2-forced exception is on the allowlist: `ModelPositionSample.score: int | None` and schema
   `"type": ["integer", "null"]`. Property stays required. No verdict widening, no artifact-id bump.
3. ⛔ Do **not** instruct `PYTHON_DOTENV_DISABLED=1` as a Django/test route (slice-4 websocket
   false-red). RF-16 sanitized `.venv/bin/python` only.
4. Existing `test_position_set_run_persists_position_index_and_exhausts` asserts `ai-match` —
   that is F01 fail-before. After the cut it must expect `model-position`. Not a silent skip.
5. `_create_run` defaults to two different catalog rows. A published single-model report requires
   the **same** `AIModel` in both seats. Mixed-pair position-set runs still persist plies; they
   refuse the artifact before atomic write. No launcher redesign.
6. Report-time overlay of snapshot `engine_baseline` onto the sample only. Do not rewrite
   `DiagnosticPly.ranked_best_score` / `ranked_search_complete`.
7. 91_ step 4’s “mount and drive each position” is **already owned by the landed runner**.
   Slice 3b is terminal reporting over persisted plies. No second drive loop. No remount during
   `_write_report`.
8. Fake `generic_unchanged` returns before the move-route POST. Green 3b tests prove plumbing
   and honest missingness, **not** model strength. K1 / live caps stay out.
9. `_vocabulary_report_envelope` types `summary` as `dict[str, int]`. Mixed-type D3 keys
   (`end_reason`, `truncated`, histogram object, optional float ratio) belong in the command’s
   post-builder augmentation. `diagnostics.py` mutation remains the nullable-score exception
   plus its comment — not an envelope rewrite.

Next: `19_implementation_00.md` (session 19 / 01, fresh Worker, Plan OFF, E2, five-path
allowlist). Not K1, not slice 6, not live NIM.

---

## §38 Slice 3b implementation-PASS independently re-verified — session 19

Worker report archived as `19_report_00.md` (pair with `19_implementation_00.md`).

```text
Candidate:          96c797fdc9540174cb4a06043e2cbe3865fcb9bf
Parent:             a17cdf4f766a9c45d5fec6af54bd5b4ea6387c20
Subject:            feat(game) model-position report for diagnostic position-set runs
Diff:               5 files, +966/−26 — exact allowlist, nothing else
AP gitlink:         9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 (unchanged)
Public origin/main: 96c797fdc9540174cb4a06043e2cbe3865fcb9bf (readback equal)
Porcelain:          empty
```

Orchestrator re-verification (not the implementing Worker):

- Allowlist exact. `diagnostics.py` is the D2 exception only (`score: int | None` + comment).
  Envelope, `Verdict`, `ARTIFACT_ID`, completion-source vocabulary untouched.
- Schema: nullable model-position `score`; additive un-required D3 summary/sample properties;
  six-word `completion_source_counts` with `additionalProperties: false`; `$id` unchanged.
- `_write_report` branches on `instrument=="position-set"`; drive loop still owns mount/turn;
  reporting reads `run.plies` + committed asset; `_ReportRefusal` skips atomic write without
  aborting the run. Mixed-pair 24-ply run retains rows and leaves `report_path=""`.
- Ratio helper: bool-int exclusion, measured-zero stays 0.0, omit key when ineligible, no clamp,
  incomplete baseline still eligible, rescue sources excluded. Aggregates applied AFTER
  `build_model_position_report`.
- Focused re-run at `96c797f` (RF-16): `tests/test_diagnostic_runner.py` +
  `tests/test_ai_play_engine_diagnostic.py` → `51 passed in 12.37s`. Worker full suite
  `911 passed, 4 skipped` (898+13) was not re-run here; E2 does not require a fresh 3b-IA.

Follow-on constraint (not a 3b defect; must be named in any live/K1 grant):
`_model_position_samples` currently hardcodes `score=None`, `verdict="fail"`,
`reason_code=REASON_GENERIC_UNCHANGED` for every published position-set sample. Lawful for
this fake `generic_unchanged` cut. A live grant must replace that fill with measured verdicts
before claiming model quality. Instrument subcaps remain provisional (R4 200/1000). K1 still
owed before freezing a 24-position provider-request ceiling.

# ⭐ SLICE 3b ACCEPTANCE-PASS DECLARED (E2, Orchestrator re-verification, no independent 3b-IA)

Next: slice 6 (admin live view + finished report UI + comparison table; `|safe` forbidden).
Not K1, not slice 7, not live NIM, not 4.6, not 14/00.

---

## §39 Slice-6 planning prompt issued — session 20 exchange 01

Cooperator confirmed native Plan mode is available this time (session 17 had BLOCKED on Default).

```text
20_planning_00.md   session 20, exchange 01, fresh-worker-session, Native planning mode: required,
                    plan-only, E0 exchange / E2 subject matter, network NONE, fake-mode admin UI
                    over landed 3b artifacts. D1–D7: live view, finished report, comparison,
                    XSS/CSP rails, allowlist, boundaries, critique.
                    apfieldcheck: DEFECTS 0, WARNINGS 1 (expected `required`-mode reminder).
Exact baseline:     96c797fdc9540174cb4a06043e2cbe3865fcb9bf
```

If the Worker BLOCKs because Plan mode is still Default, reissue as `not-used` with prompt-level
planning authority (session-18 pattern). Do not complete slice 6 under a mismatched mode.

---

## §40 Session 20 plan accepted; slice-6 implementation grant — session 21

Planning report archived as `20_report_00.md` (pair with `20_planning_00.md`). Advisory, zero
mutation, baseline unchanged `96c797f`. Orchestrator **accepts** D1–D7 with these plan-level
corrections baked into `21_implementation_00.md` (not a targeted revision):

1. In-flight GET (`queued`/`running`) must **not** open the report file. File read is for
   terminal statuses only. Otherwise a 2-second Refresh would violate the one-PK + 20-ply budget
   and reread JSON on every poll.
2. JSON parse: `allow_nan=False` and reject duplicate keys (`object_pairs_hook`). Python
   `json.loads` otherwise keeps the last duplicate and can accept NaN.
3. ⛔ `format_html` / `format_html_join` / `mark_safe` / `|safe` — `format_html` is a mark_safe
   path. CSS classes only from a closed status/instrument enum map, never from `model_id` /
   `reason_code` / artifact strings.
4. Comparison: fake/partial/no-report rows stay **visible** with an exclusion reason; they never
   enter the measured pool (`runtime=live` + floors + provenance). Do not hide them.
5. `TemplateResponse` must pass `admin_site.each_context(request)` like `launch_view`. Do not
   call `changeform_view`.
6. ⛔ `PYTHON_DOTENV_DISABLED=1` as a Django/test route. RF-16 only.
7. New `diagnostic_admin_reports.py` is under `game/**` — AST guard forbids pytest/ruff/mypy
   imports. Heartbeat copy: every five plies or ~30 seconds (measured `_HEARTBEAT_*`).
8. Existing launcher tests do not assert `Location`; put F01 redirect evidence in
   `test_diagnostic_admin.py`. Do not expand the allowlist to `test_diagnostic_runner.py`
   unless a measured regression forces a one-assertion edit — then STOP and report rather than
   silently widening.

Next: `21_implementation_00.md` (session 21 / 01, fresh Worker, Plan OFF, E2, seven-path
allowlist). Rendered look is Michal’s after the cut lands. Not K1, not slice 7, not live NIM.

---

## §41 Session 21 implementation-PASS independently verified; slice-6 acceptance waits on Cooperator look

Worker report archived as `21_report_00.md` (pair with `21_implementation_00.md`).

```text
Commit:     40f353239c5b7a66e6923b55fa3c12afe04ff183
Parent:     96c797fdc9540174cb4a06043e2cbe3865fcb9bf
Subject:    feat(admin) diagnostic run live view and comparison
Diff:       7 files, +2251/−9 (exact allowlist)
AP pin:     9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
HEAD:       local == origin/main == 40f3532; porcelain empty
pytest:     Worker full suite 947 passed, 4 skipped (911+36)
            Orchestrator focused re-run: tests/test_diagnostic_admin.py → 36 passed in 4.06s
```

Live-pool intent **confirmed as grant-literal**, not a Worker over-read: measured pool
requires `executed_runtime_mode == "live"` on the run, the requested block, and every
sample (`admin.py` `_REASON_RUNTIME` / `_REASON_RUNTIME_SAMPLES`). Fake-only cut → pool
structurally empty; every fake row stays visible with an exclusion reason. Do not “fix”
this by pooling fake rows. Later live/K1 work may populate the pool; this cut must not.

Independent source checks (not the implementing Worker):

- In-flight GET (`queued`/`running`) never calls `present_report`; `Refresh: 2` only then.
- Terminal pages have no Refresh header (asserted F02).
- Reader compares stored `report_path` and never opens it; canonical no-follow chain only.
- `json.loads(..., object_pairs_hook=_reject_duplicate_keys, parse_constant=_reject_constant)`
  (NaN/Infinity via `parse_constant`; tests cover NaN + duplicate keys).
- No `|safe` / `mark_safe` / `format_html` / `format_html_join` under `backend/game/`.
- Comparison `run_id_short` is **plain text, not a link** (plan D3 said “run link/date”).
  UX residual for Cooperator rendered look, not a security or ranking defect.

Slice 6 is **implementation-PASS**, independently verified. It is **not**
acceptance-PASS until Michal looks at `/admin/game/diagnosticrun/` (D11: rendered look is
his, not Worker browser MCP). Do not issue slice 7, K1, or live NIM until that look, unless
he explicitly skips look and continues.

Next after his look (or explicit skip): slice 7 planning (`base_url` + SSRF). Not K1,
not slice 8, not 4.6, not 14/00.

---

## §42 Slice 6 acceptance-PASS (Cooperator rendered look)

Cooperator 2026-09-07: **look OK**. Combined with Orchestrator independent
verification at `40f3532` (§41), slice 6 is **acceptance-PASS**.

Residuals (not reopen-as-defects unless he says otherwise):
- Compare table shows `run_id_short` as text, not a link.
- Measured pool empty for fake-only (grant-literal `runtime=live`).
- 3b hardcoded `score=None` / `verdict=fail` fill — display honesty, live grant later.
- APMC-S5-IA-F01/F02/F03 still Orchestrator-accepted.

# ⭐ SLICE 6 ACCEPTANCE-PASS DECLARED (implementation `40f3532` + Cooperator look)

Next: slice 7 planning (diagnostic OpenAI-compatible target + SSRF + R2=A credentials).
Not K1, not slice 8, not live NIM, not whole-closure 4.6 yet (7-IA follows the cut).

---

## §43 Slice-7 planning prompt issued — session 22 exchange 01

Orchestrator-locked for this plan (D12 leftovers the era-01 plan would not choose):

```text
Host policy:   shipped-origin allowlist + explicit add-host POST (hostname only, no fetch)
               + https/DNS/IP SSRF at save AND at request. Not free-form fetch-on-save.
Seam:          bounded diagnostic-only branch REQUIRED. Player getLanguageRuntime /
               isValidRuntimePair unchanged. No second SSE route, no MOVE CORE bump.
Credential:    R2=A. credential_env_name from closed CREDENTIAL_ENV_NAMES (or an
               explicit same-slice code extension of that list). Free-form env names
               forbidden (would let an admin name DJANGO_SECRET_KEY).
Provider calls this slice: ZERO. Ping-pong is slice 8. K1 remains separate.
Independent 7-IA: mandatory after implementation (INFOSEC 4.6). Not this planner.
```

```text
22_planning_00.md   session 22, exchange 01, fresh-worker-session, Native planning mode: required,
                    plan-only, E0 exchange / E3 subject matter, network NONE.
Exact baseline:     40f353239c5b7a66e6923b55fa3c12afe04ff183
apfieldcheck:       DEFECTS 0, WARNINGS 1 (expected `required`-mode reminder)
```

---

## §44 Session 22 plan accepted; slice-7 implementation grant — session 23

Planning artifact archived as `22_report_00.md` (pair with `22_planning_00.md`).
**Protocol note:** the artifact is D1–D7 decision-complete but lacks
`### Report for ORCHESTRATOR_CHAT` compact core (session-01 shape). Orchestrator did **not**
burn a report-completion Worker; technical content was reviewed against `40f3532` and accepted
as advisory plan. Implementation authority is only `23_implementation_00.md`.

Independent checks that matched the plan: `createTrackedOpenAIChatModel` unexported;
`createTrackedProviderFetch` still fetches on `"unknown"`; `SHIPPED_PROVIDER_ORIGINS` is two
hosts vs eight seeded; `_worker_env_whitelist` forwards zero keys; `generic_unchanged` returns
before POST; `_position_pair_identity` / `create_diagnostic_game` are catalog-only;
`get_ai_context` uses `acting.ai_model or session.ai_model`; `AIContextView` is a passthrough
(no `views.py` on the allowlist); `SECRET_KEY_FRAGMENTS` includes `env`.

Orchestrator **accepts** D1–D7 with corrections baked into `23_implementation_00.md`:

1. Target seat must not inherit the other seat’s catalog model via `session.ai_model`.
2. `set_game_ai_model` refuses PATCH on an acting target seat.
3. `diagnostic_runtime` only for diagnostic service user + acting target seat; never in SSE.
4. `parameters_json` may hold target UUIDs, never URL/env/secret (`env` fragment already forbids
   `credential_env_name` keys).
5. F08 bound adapter is non-negotiable — PARTIAL rather than DNS-then-fetch.
6. No extra admin templates pre-authorized; no `views.py` / `ai-runtimes.ts`.
7. Fake Launch is not seam evidence.

Host-allowlist lock stands. Credential closed list = full `CREDENTIAL_ENV_NAMES` (parity),
watsonx transport still out. One E3 exchange, no 7a/7b split. Independent 7-IA after landing.

```text
23_implementation_00.md   session 23, exchange 01, fresh-worker-session, Native planning mode:
                          not-used, E3, baseline 40f3532, push to main.
                          apfieldcheck: DEFECTS 0, WARNINGS 0.
```

---

## §45 Session 23 implementation-PASS independently verified; slice-7 acceptance waits on look + 7-IA

Worker report archived as `23_report_00.md` (pair with `23_implementation_00.md`).

```text
Commit:     39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
Parent:     40f353239c5b7a66e6923b55fa3c12afe04ff183
Subject:    feat(game) diagnostic OpenAI-compatible target with SSRF guards
Diff:       29 files, +4281/−126 (exact section-4 allowlist; no catalog/gamecore/views/ai-runtimes)
AP pin:     9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
HEAD:       local == origin/main == 39cc8dc; porcelain empty
pytest:     Worker full suite 1005 passed, 4 skipped (947+58)
            Orchestrator focused: tests/test_diagnostic_{targets,admin,session,runner}.py
              → 160 passed, 1 warning in 30.94s
            Orchestrator focused vitest (5 files): 105 passed
```

Independent source checks (not the implementing Worker):

- `ai-runtimes.ts` / `getLanguageRuntime` / `isValidRuntimePair` not in the diff.
- Sibling `getDiagnosticLanguageRuntime` asserts egress deny **before** `requireServerCredential`.
- `buildRequestOptions` custom `lookup` returns only the validated address; Host/SNI keep hostname.
- Production worker still `installFetchGuard(..., { mode: "fake" })`; `_worker_env_whitelist` unchanged.
- Route SSE `provider_path` for targets is the constant `diagnostic-target` (no UUID/URL).
- Body closed key set + fragment refuse for URL/env/secret; PATCH skipped on target seats.
- `create_diagnostic_game`: both-targets → `session.ai_model` null; target UUIDs only in
  `parameters_json`; `_FORBIDDEN_PARAMETER_KEYS` includes `base_url`.
- No `|safe` / `mark_safe` / `format_html` under `backend/game/`.
- game.0012 depends only on game.0011 + AUTH_USER_MODEL (no catalog.0012 — explains the
  Worker’s autodetector near-miss without an off-allowlist catalog edit).

Residuals for 7-IA (INFOSEC 4.6), not reopen-as-slice-7 defects:

- Live egress is two env flags (`LIBRETILES_DIAGNOSTIC_EGRESS=live` AND `LIBRETILES_AI_PLAY_LIVE=1`)
  in the Next process. L4 whitelist does not forward them; an L1 Next.js with both set would
  be a later grant, not this fake cut.
- `GET /ai-context/` returns `diagnostic_runtime` (incl. `base_url` + env **name**) for the
  service JWT on an acting target seat. Membership is the gate; no extra `is_service_account`
  check. Player vs_ai gets the key as `null` (additive API field).
- Key-to-host delegation (admin pairs an allowlisted host with an existing env name) remains
  a live-grant / 7-IA item; fake deny prevents transmission.
- Adapter is unit-proven (`buildRequestOptions` + injected transport); no live socket.
- `LogEntry.objects.log_action` Django 6 deprecation warning (one warning in focused pytest).

Slice 7 is **implementation-PASS**, independently verified. It is **not** acceptance-PASS until
Michal looks at admin CRUD (add-host → target → launch) **and** a fresh independent 7-IA
returns. Do not start slice 8, K1, or live NIM until that.

Next after his look (or explicit skip): 7-IA prompt (INFOSEC 4.6, read-only, `fresh-worker-session`).
Not slice 8, not K1, not 14/00.

---

## §46 Slice-7 Cooperator look OK; 7-IA issued — session 24

Cooperator 2026-09-07: **look OK** on admin CRUD (add-host → target → launch). Combined with
Orchestrator independent verification at `39cc8dc` (§45), Cooperator rendered look is
satisfied. Slice 7 is **not** acceptance-PASS until 7-IA dispositions.

```text
24_audit_00.md   session 24, exchange 01, fresh-worker-session, Native planning mode: not-used,
                 Fresh Independent Audit, INFOSEC 4.6 (P-7), E3, network NONE, zero provider
                 calls, candidate 39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
                 apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §47 Session 24 7-IA BLOCKED on grant conflict; 7-IA reissued as session 25

Worker 24 (`24_report_00.md`) status **BLOCKED**. No files changed. No pytest/mypy/ruff/vitest.
Repository gate matched `39cc8dc` / AP pin / empty porcelain. C1–C12 all “not accepted” meaning
**evidence not collected**, not twelve product defects.

**APMC-S7-IA-F01** (info, established-static, Orchestrator-accepted): the session-24 required
four-module pytest would execute `test_f_v_*` and `test_f_w_*`, which call `_migration_process`
(`backend/tests/test_diagnostic_session.py:612`) and set `PYTHON_DOTENV_DISABLED="1"` in a
subprocess that boots Django. The prompt forbade that as a Django/test route. Literal stop was
correct. No product C/I/A impact. Not a slice-7 vulnerability. No repository correction.

Grant resolution (session 25): Worker still must not *set* `PYTHON_DOTENV_DISABLED` on commands
they type. Required pytest **deselects** the two historical F-V/F-W nodeids (slice-4 migration
rescue; only callers of the helper; not C1–C12 evidence). Existence of the helper is not a stop.

Slice 7 remains **not** acceptance-PASS. Not slice 8, not K1, not live NIM.

```text
25_audit_00.md   session 25, exchange 01, fresh-worker-session, Native planning mode: not-used,
                 Fresh Independent Audit, INFOSEC 4.6 (P-7), E3, network NONE, zero provider
                 calls, candidate 39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
                 product findings start at APMC-S7-IA-F02; F01 stays orchestration-info
                 apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §48 Session 25 did not audit; 7-IA reissued as session 26

`25_report_00.md` is five English lines confirming F01’s grant resolution and stating that
C1–C12 remain unaccepted pending evidence. It does **not** begin `### Report for ORCHESTRATOR_CHAT`,
has no compact core, and ran no tests. It is **not** 7-IA evidence. Do not disposition product
findings from it.

Session 25 is recorded as **non-performance** (grant confirmation instead of audit), not as a
second product BLOCKED. The deselect grant in `25_audit_00.md` was already correct; the Worker
did not execute it.

```text
26_audit_00.md   session 26, exchange 01, fresh-worker-session, Native planning mode: not-used,
                 Fresh Independent Audit, INFOSEC 4.6 (P-7), E3, network NONE, zero provider
                 calls, candidate 39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
                 first actions: repo gate then required deselected pytest; confirmation is not a stop
                 apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §49 Session 26 7-IA PARTIAL — disposition; correction issued (session 27)

Worker 26 (`26_report_00.md`) completed the independent 7-IA at `39cc8dc`. Status **PARTIAL**.
Provider calls: zero. Required pytest: `158 passed, 2 deselected, 1 warning`. mypy/ruff clean.
Focused vitest: 119 passed, 5 skipped (4 live-grant filters). Containment deviation: mixed
`backend/var/diagnostics` artifacts retained (no wildcard cleanup).

Orchestrator independent source check agrees with F02/F03/F04/F06. C1, C3–C6, C8, C10, C11
verified-closed by the auditor; Orchestrator does not reopen them.

| ID | Severity | Disposition |
|---|---|---|
| APMC-S7-IA-F01 | info | already accepted (orchestration). No repo work. |
| APMC-S7-IA-F02 | low | **accepted for correction.** View-only staff mutate activation via four new admin actions. C2 not accepted until closed. |
| APMC-S7-IA-F03 | medium | **accepted for correction.** Inactive/malformed target seat falls through to `getLanguageRuntime`. C7 not accepted until closed. |
| APMC-S7-IA-F04 | low | **accepted for correction.** Freeze check then DNS then persist; slot can appear in between. C9 not accepted until closed. |
| APMC-S7-IA-F05 | info | **accepted residual (fake-only).** Key-to-host delegation stays latent while egress deny holds. A later live grant must decide credential/destination binding. Not this correction. C12 remains this residual, not a silent product accept-as-closed. |
| APMC-S7-IA-F06 | info / rejected-false-positive | **accepted.** Ambient-fetch SSRF hypothesis disproved for the bound adapter. |

Slice 7 is **not** acceptance-PASS. Not slice 8, not K1, not live NIM. After session 27 lands:
fresh independent re-audit (P-10) of F02–F04 plus original C2/C7/C9.

```text
27_correction_00.md   session 27, exchange 01, fresh-worker-session, Native planning mode: not-used,
                      Bounded Correction Worker, baseline 39cc8dc, push to main, nine-path allowlist
                      apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §50 Session 27 correction landed; 7-IA re-audit issued (session 28)

Worker 27 (`27_report_00.md`) status **implementation-PASS**. One commit, nine allowlisted paths.

```text
Commit:     4c524ec3020bbd2f27f2ce32ac160d2c40469c0e
Parent:     39cc8dcaaa40485117fb41098ac7b7e3c2e57eb9
Subject:    fix(game) fail-closed diagnostic target seats and freeze activation authz
Diff:       9 files, +245/−14 (exact allowlist)
AP pin:     9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
HEAD:       local == origin/main == 4c524ec; porcelain empty
pytest:     Worker full suite 1011 passed, 4 skipped (was 1005; +6 tests, skips unchanged)
Orchestrator focused: 5 passed (F02 class + F03 inactive seats + F04 DNS-interleave freeze)
```

Independent source check (not the correcting Worker):

- F02: `permissions=["change"]` + `_guard_change_permission` on all four actions.
- F03: `diagnostic_target_seat` always in `get_ai_context`; route enters diagnostic branch on
  the flag; `_diagnostic_runtime_for` still returns None when inactive.
- F04: post-DNS `_target_is_referenced` recheck; `DiagnosticTarget.save` atomic +
  `select_for_update`; `_resolve_diagnostic_seat_target` locks the row.
- `ai-runtimes.ts` not in the diff. No migration.

Nuance for re-audit: implementer F02 tests used a non-CSRF client; session 26 used
`enforce_csrf_checks=True`. Mutation (not HTTP 403) is the invariant.

Slice 7 is **not** acceptance-PASS until V-F02/V-F03/V-F04 are verified-closed. Not slice 8,
not K1, not live NIM.

```text
28_reaudit_00.md   session 28, exchange 01, fresh-worker-session, Native planning mode: not-used,
                   Fresh Independent Re-Audit (P-10 / INFOSEC 4.11), candidate 4c524ec,
                   deselect F-V/F-W, network NONE, zero provider calls
                   apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §51 Slice-7 acceptance-PASS DECLARED; rotation-2 handout issued

Session 28 (`28_report_00.md`) status **PASS**. No new finding. Independent CSRF F02, twelve-case
F03 route probes, DNS-interleave F04, V-REG nine-path. Orchestrator source check at `4c524ec`
agrees. Combined with Cooperator look OK (2026-09-07) on add-host → target → launch:

# ⭐ SLICE 7 ACCEPTANCE-PASS DECLARED
# implementation 39cc8dc + correction 4c524ec + 7-IA + re-audit V-F02/V-F03/V-F04/V-REG

F05 remains accepted fake-only residual (credential/destination binding owed at a later live grant).
F01 orchestration-info; F06 rejected-false-positive. S5-IA F01–F03 unchanged.

This Orchestrator does **not** start slice 8 from a twice-summarized context. Next Worker session
ordinal is **29**. Restoration file: `92_orchestrator-handout-2.md`. Successor starts at slice-8
Planner. Not K1, not 14/00, not VPS, not a second 7-IA.

---

## §52 Rotation 2 boot; Slice 8 Planner issued (session 29)

Rotation 2 fresh Orchestrator started 2026-09-07. Baseline gate re-verified:
HEAD `4c524ec3020bbd2f27f2ce32ac160d2c40469c0e`, AP pin `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`,
working copy clean. Slices 1–7 and 3b remain CLOSED. Cooperator confirmed role as high-level
steering/brainstorming and requested direct meta file management by Orchestrator/Workers.

Slice 8 Planner prompt prepared and written directly to meta:
`29_planning_00.md` (session 29, exchange 01, fresh-worker-session, Native planning mode: required,
Task identity `APMC-S8-PLAN`, E0 planning, E2 implementation scope, provider calls ZERO/fake default).
Covers: ping-pong probe execution (reusing `provider-capability.ts`), child-table probe history,
reviewed `sort_order`/`is_active` POST diff, zero-selectable and last-tools-model bricking refusal,
template escaping in Django admin without Next.js CSP, DiagnosticTarget relationship.
`apfieldcheck.py`: DEFECTS 0, WARNINGS 1 (Native planning mode reminder).

```text
29_planning_00.md  session 29, exchange 01, fresh-worker-session, Native planning mode: required,
                   Implementation-Planning Worker, baseline 4c524ec, zero provider calls,
                   apfieldcheck: DEFECTS 0, WARNINGS 1
```

---

## §53 Slice 8 Plan accepted; Session 30 Implementation prepared

Session 29 Worker returned `29_report_00.md` with status **PASS**, phase-qualified result
`not-applicable`, justification `new-evidence`. No files changed, checkout clean at `4c524ec`.

Orchestrator review:
- **D1 (Execution)**: dedicated Node subprocess (`probe-worker.mjs`) importing TypeScript capability
  function via existing resolver hooks. Fake by default (0s, 0 egress, simulated PASS). Live mode
  strictly gated by `PROVIDER_PROBE_LIVE === "1"`. 25s subprocess deadline, max 4 HTTP dispatches,
  60s admission throttle, closed provider env-var whitelist.
- **D2 (History)**: `CapabilityProbe` child table in `catalog/models.py`, migration `0013_...`.
  Singleton `CatalogAdminControl` for atomic coordination. Retention 100 per model, pruned on write.
  Read-only admin display with prominent fake/live separation.
- **D3 (Ordering & Activation)**: two-step review flow (review POST → signed 10-min token → apply POST).
  Fail-closed refusal invariants: leaving zero selectable rows under either flag state or removing
  the last tools-capable model raises error and rolls back atomically. Direct-edit bypasses closed
  (`list_editable` removed). Seed and sync preserve operator priorities and activation.
- **D4 (Template Safety)**: strict Django auto-escaping; ban on `|safe` / `mark_safe()`; CSRF on all
  mutation POSTs; staff and model permission checks.
- **D5 (Boundary)**: `AIModel` only in Slice 8. `DiagnosticTarget` remains isolated, unchanged, and fake-only.
- **D6/D7 (Tests & Threat Model)**: fail-before F01–F19, exact allowlist, E2 tier. Exclusions intact:
  no K1, no full Provider entity, no 14/00, no VPS deploy.

**Orchestration correction on execution**: Planner noted `PYTHON_DOTENV_DISABLED=1` for shell commands.
Per handover §0 and §7, Workers must **never** type that flag on their shell commands (RF-16
`.venv/bin/python` governs).

⇒ **Plan ACCEPTED.** Next step is Session 30 Implementation (`30_implementation_00.md`).

---

## §54 Session 30 Implementation issued (`30_implementation_00.md`)

Prompt prepared and written directly to meta:
`30_implementation_00.md` (session 30, exchange 01, fresh-worker-session, Native planning mode: not-used,
Task identity `APMC-S8-IMPL`, E2 implementation scope, baseline `4c524ec3020bbd2f27f2ce32ac160d2c40469c0e`,
push to main authorized upon green gates, 24-file allowlist, provider calls ZERO/fake default).

Key mandates re-expressed:
- Refuse zero selectable models under both flag states.
- Refuse deactivating last tools-capable model.
- Strict Django template auto-escaping (no `|safe`, no `mark_safe`).
- Node probe worker in fake mode by default; max 4 HTTP dispatches when live.
- DiagnosticTarget remains isolated.
- RF-16 strictly enforced (never type `PYTHON_DOTENV_DISABLED=1`).
`apfieldcheck.py`: DEFECTS 0, WARNINGS 0.

```text
30_implementation_00.md  session 30, exchange 01, fresh-worker-session, Native planning mode: not-used,
                         Bounded Implementation Worker, baseline 4c524ec, push to main,
                         apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §55 Session 30 Implementation landed; Orchestrator verification all green

Session 30 Worker returned `30_report_00.md` with status **PASS**, phase-qualified result
`implementation-PASS`, justification `new-mutation`. Single commit landed on `main`:

```text
Commit:     8853a29eb5e9f937b3db49236cac6ad876db6469
Parent:     4c524ec3020bbd2f27f2ce32ac160d2c40469c0e
Subject:    feat(catalog): add capability probe history and reviewed fallback order controls
Diff:       24 files, +3345/−139 (exact allowlist)
AP pin:     9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
HEAD:       local == origin/main == 8853a29; porcelain empty
```

Orchestrator independent verification:
- Focused backend tests: 21 passed (migration, probe history, probe worker, admin controls).
- Adjacent regression pytest: 73 passed (catalog + admin + diagnostic targets).
- Diagnostic runner & session pytest: 84 passed, 2 deselected (F-V/F-W).
- Ruff check: all checks passed.
- Mypy: clean on 99 source files.
- Frontend: `npm run typecheck`, `npm run lint`, and Vitest 26 passed.
- Local dev DB: `manage.py migrate catalog` applied `0013_admin_provider_model_console` cleanly.

Cooperator look invited for Django admin:
- `/admin/catalog/aimodel/` -> "Manage fallback order & activation" button -> controls review & preview.
- Model detail form -> Capability probes list & trigger fake probe -> history.

Next step: Cooperator look + focused audit prompt (Session 31) for authN/Z on the sort_order POST
and history integrity.

---

## §56 Session 31 Focused Independent Audit issued (`31_audit_00.md`)

Prompt prepared and written directly to meta:
`31_audit_00.md` (session 31, exchange 01, fresh-worker-session, Native planning mode: not-used,
Task identity `APMC-S8-AUDIT`, E2 audit scope, baseline `8853a29eb5e9f937b3db49236cac6ad876db6469`,
read-only, provider calls ZERO).

Claims to independently evaluate (C1–C8):
- C1: AuthN/Z and CSRF enforcement on action endpoints (review, apply, probe).
- C2: Signed review token integrity and anti-replay (TimestampSigner, 10 min, user/revision/flag/diff binding).
- C3: Safety invariants and bricking refusal (zero-selectable and last-tools refusal).
- C4: Probe history integrity and read-only administration (newest-100 retention, fake/live separation).
- C5: Template safety and XSS prevention (no `|safe`, no `mark_safe()`).
- C6: Node probe worker isolation and fake default (`PROVIDER_PROBE_LIVE === "1"` required, zero calls in test).
- C7: Seed and sync preservation of operator choices (`sort_order`, `is_active`).
- C8: Boundary isolation (`DiagnosticTarget` untouched).

`apfieldcheck.py`: DEFECTS 0, WARNINGS 0.

```text
31_audit_00.md  session 31, exchange 01, fresh-worker-session, Native planning mode: not-used,
                Fresh Independent Audit, baseline 8853a29, provider calls ZERO,
                apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §57 Session 31 Audit returned PARTIAL; Session 32 Correction issued

Session 31 Worker returned `31_report_00.md` with status **PARTIAL**, justification `new-evidence`.
C4, C5, C6, C7, C8 verified-closed. C1, C2, C3 not accepted based on 3 findings:
- **APMC-S8-AUDIT-F01 (info)**: non-staff user gets 302 redirect to admin login rather than 403.
  Django admin standard behavior; accepted as informational claim reconciliation.
- **APMC-S8-AUDIT-F02 (low)**: `dynamic_enabled` in signed token not verified during apply.
  Accepted for correction.
- **APMC-S8-AUDIT-F03 (medium)**: `AIModelAdmin.save_model` on change does full save, which could
  overwrite `is_active`/`sort_order` with stale values during interleaving.
  Accepted for correction: restrict changeform save to descriptive metadata via `update_fields`.

Correction prompt prepared and written directly to meta:
`32_correction_00.md` (session 32, exchange 01, fresh-worker-session, Native planning mode: not-used,
Task identity `APMC-S8-CORR`, E2 correction scope, baseline `8853a29eb5e9f937b3db49236cac6ad876db6469`,
allowlist: `catalog/admin.py`, `catalog/admin_controls.py`, `tests/test_catalog_admin_controls.py`,
push to main authorized upon green gates, provider calls ZERO).
`apfieldcheck.py`: DEFECTS 0, WARNINGS 0.

```text
32_correction_00.md  session 32, exchange 01, fresh-worker-session, Native planning mode: not-used,
                     Bounded Correction Worker, baseline 8853a29, push to main,
                     apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §58 Session 32 Correction landed; Session 33 Re-Audit issued

Session 32 Worker returned `32_report_00.md` with status **PASS**, phase-qualified result
`implementation-PASS`, justification `new-mutation`. Single commit landed on `main`:

```text
Commit:     151e833dd0e78ced075101864cb5f45ee521bebc
Parent:     8853a29eb5e9f937b3db49236cac6ad876db6469
Subject:    fix(catalog): enforce signed flag binding and restrict changeform saves to metadata
Diff:       3 files, +139/−17 (exact allowlist)
AP pin:     9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
HEAD:       local == origin/main == 151e833; porcelain empty
```

Orchestrator verification:
- F02: `apply_reviewed_token` enforces `payload.get("dynamic_enabled") == current_dynamic_catalog_enabled()`.
- F03: `AIModelAdmin.save_model` on change updates ONLY allowed descriptive metadata fields
  via `obj.save(update_fields=...)`. `is_active` and `sort_order` can never be written by changeform.
- Regression tests pass: 23 focused passed; 75 adjacent catalog/admin passed; ruff & mypy clean.
- Frontend: typecheck and lint clean.

Fresh independent re-audit prompt prepared and written directly to meta:
`33_reaudit_00.md` (session 33, exchange 01, fresh-worker-session, Native planning mode: not-used,
Task identity `APMC-S8-REAUDIT`, E2 scope, baseline `151e833dd0e78ced075101864cb5f45ee521bebc`,
verifies V-F01, V-F02, V-F03, and V-REG; provider calls ZERO).
`apfieldcheck.py`: DEFECTS 0, WARNINGS 0.

```text
33_reaudit_00.md  session 33, exchange 01, fresh-worker-session, Native planning mode: not-used,
                  Fresh Independent Re-Audit, baseline 151e833, provider calls ZERO,
                  apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §59 Slice-8 acceptance-PASS DECLARED; Step 3 (K1 decision) reached

Session 33 Worker returned `33_report_00.md` with status **PASS**, justification `new-evidence`.
All four evaluated claims **verified-closed**:
- **V-F01**: verified-closed (Django standard 302 login redirect on unauthenticated/non-staff POSTs, access blocked).
- **V-F02**: verified-closed (signed review token strictly binds `dynamic_enabled`, flag mismatch returns 409).
- **V-F03**: verified-closed (`AIModelAdmin.save_model` on change updates ONLY allowed descriptive metadata
  fields via `update_fields`, `is_active` and `sort_order` can never be written or reverted by changeform).
- **V-REG (C4–C8)**: verified-closed (probe history immutability and retention, template XSS escaping, fake-default
  isolated node worker, seed/sync preservation, DiagnosticTarget isolation).

Orchestrator independent verification at `151e833dd0e78ced075101864cb5f45ee521bebc` confirms closure.

# ⭐ SLICE 8 ACCEPTANCE-PASS DECLARED
# implementation 8853a29 + correction 151e833 + audit + re-audit V-F01/V-F02/V-F03/V-REG

All console slices are now CLOSED:
- Slice 1–6, 3b, 7: CLOSED (prior rotations / §51)
- Slice 8: CLOSED at `151e833dd0e78ced075101864cb5f45ee521bebc`

Per `92_orchestrator-handout-2.md` §6, the sequence reaches **Step 3 (K1 grant decision)**:
- K1: 8–12 live NIM calls to calibrate requests-per-ply so position-set / instrument subcaps stop
  being provisional (R4 200/1000 stay until then). Provider Accounting annex.
- Handout mandate: "Do not invent this grant. Ask him when slice 8 is accepted and the console is
  coherent in admin. If he says no, whole-closure INFOSEC 4.6 proceeds with provisional subcaps and
  names that residual."
- Step 4 following K1 (or immediately if K1 is skipped): Final whole-console INFOSEC 4.6, then closure.

---

## §60 Cooperator granted K1; Session 34 Live Calibration issued

Cooperator explicitly granted authority for K1 (live NIM measurement to calibrate subcaps).
Prompt prepared and written directly to meta:
`34_k1_00.md` (session 34, exchange 01, fresh-worker-session, Native planning mode: not-used,
Task identity `APMC-K1`, E3 live provider measurement, baseline `151e833dd0e78ced075101864cb5f45ee521bebc`,
call cap: 12 total, single call in flight, target `nvidia-nim` / `nvidia/nemotron-3-super-120b-a12b`,
Provider Accounting annex required, read-only measurement).
`apfieldcheck.py`: DEFECTS 0, WARNINGS 0.

```text
34_k1_00.md  session 34, exchange 01, fresh-worker-session, Native planning mode: not-used,
             Bounded Live Calibration Worker, baseline 151e833, provider calls max 12 (NIM),
             apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §61 Session 34 K1 Live Calibration completed; Step 4 (Whole-Console INFOSEC 4.6) reached

Session 34 Worker returned `34_report_00.md` with status **PARTIAL** (measurement complete, subcaps
remain provisional), justification `new-evidence`. No files changed, checkout clean at `151e833`.

Provider Accounting Contract summary:
- Invocations authorized: up to 12.
- Actual invocations: 4 total (1 live capability probe + 3 live turns).
- Retries: 0. Duplicates: 0. Leaks: 0. Unresolved: 0. In-flight: 0. Fully reconciled.
- Invocations outcome:
  * Probe: HTTP 500 from NVIDIA NIM endpoint (`status="unknown"`, `outbound_count=1`, `latency=1506ms`).
  * Live ply 1: 1 request used, `generic_error_fallback` -> engine rescue (`backend_ranked_candidate`, score 82, `SČÍTALO`).
  * Live plies 2 & 3: 1 request used each, `no_provider_progress_deadline` -> engine rescue (`backend_ranked_candidate`, score 82).
- Empirical findings:
  * Mean requests per ply = 1.0 (rescue floor).
  * Model-authored placements = 0% (0/3); Engine rescues = 100% (3/3).
  * Confirms `00_handout.md` §8.2: the engine carries the game when the model is silent/erroneous.
  * Subcaps remain **provisional** as designed (`parameters_json.subcaps_provisional=true`),
    bounded by default 200 requests and admin max 1000 (R4).

Per `92_orchestrator-handout-2.md` §6, the sequence now reaches **Step 4 (Final whole-console INFOSEC 4.6 audit)**:
- Final independent security audit of the whole landed console (Slices 1–8).
- Residual risk disposition: F05 (live binding decision), S5-IA F01–F03, 3b fill honesty, compare-table UX, provisional subcaps.
- Provider calls: ZERO. Read-only.

---

## §62 Session 35 Final Whole-Console Security Audit issued (`35_audit_00.md`)

Prompt prepared and written directly to meta:
`35_audit_00.md` (session 35, exchange 01, fresh-worker-session, Native planning mode: not-used,
Task identity `APMC-WHOLE-CONSOLE-AUDIT`, E3 comprehensive whole-closure security audit,
baseline `151e833dd0e78ced075101864cb5f45ee521bebc`, read-only, provider calls ZERO).

Evaluates C1–C10 across Slices 1–8:
- C1: R2=A Credential Isolation (env name only, zero secrets in DB/logs/reports/HTML).
- C2: Outbound SSRF & Network Protection (HTTPS only, DNS rebinding defeat, bound adapter, private IP refusal).
- C3: Sibling Runtime Seam & Player Route Isolation (getDiagnosticLanguageRuntime vs getLanguageRuntime).
- C4: Diagnostic Service Account Security (unusable password, is_service_account=True, rename/matchmaking blocked).
- C5: Diagnostic Runner Bounds & Resource Containment (timeouts, heartbeats, max requests, cancellation).
- C6: Probe History & Worker Isolation (read-only, newest-100 retention, fake default, single-shot Node worker).
- C7: Fallback Order & Catalog Invariants (atomic write-lock, zero-selectable and last-tools refusal).
- C8: Changeform Save Isolation (update_fields descriptive metadata only, activation/order cannot be overwritten).
- C9: Django Admin Template XSS Prevention (auto-escaping, no |safe, no mark_safe).
- C10: Operational Honesty & Metrics Separation (completion_source vs score, fake/live separation).
Residual risk disposition: F05, S5-IA F01–F03, 3b fill honesty, compare-table UX, provisional subcaps.
`apfieldcheck.py`: DEFECTS 0, WARNINGS 0.

```text
35_audit_00.md  session 35, exchange 01, fresh-worker-session, Native planning mode: not-used,
                Fresh Independent Security Audit Worker, baseline 151e833, provider calls ZERO,
                apfieldcheck: DEFECTS 0, WARNINGS 0
```

---

## §63 Whole-Console Audit PASSED; Logical Whole `admin-provider-model-console` CLOSED

Session 35 Worker returned `35_report_00.md` with status **PASS**, justification `final-acceptance`.
All ten whole-console claims C1–C10 **verified-closed**:
- C1: R2=A Credential Isolation (env name only, zero secrets in DB/logs/reports/HTML).
- C2: Outbound SSRF & Network Protection (HTTPS only, DNS rebinding defeat, bound adapter, private IP refusal).
- C3: Sibling Runtime Seam & Player Route Isolation (getDiagnosticLanguageRuntime vs getLanguageRuntime).
- C4: Diagnostic Service Account Security (unusable password, is_service_account=True, rename/matchmaking blocked).
- C5: Diagnostic Runner Bounds & Resource Containment (timeouts, heartbeats, max requests, cancellation).
- C6: Probe History & Worker Isolation (read-only, newest-100 retention, fake default, single-shot Node worker).
- C7: Fallback Order & Catalog Invariants (atomic write-lock, zero-selectable and last-tools refusal).
- C8: Changeform Save Isolation (update_fields descriptive metadata only, activation/order cannot be overwritten).
- C9: Django Admin Template XSS Prevention (auto-escaping, no |safe, no mark_safe).
- C10: Operational Honesty & Metrics Separation (completion_source vs score, fake/live separation).

All seven accepted residuals formally dispositioned. Zero open findings.
Orchestrator independent verification confirms all conditions met.

# ⭐ LOGICAL WHOLE `admin-provider-model-console` IS CLOSED
# Closed-by-ORCHESTRATOR at commit 151e833dd0e78ced075101864cb5f45ee521bebc
# Closure record: 99_closure.md

Successor logical whole `14/00-ai-opponent-strength` is now unlocked.

















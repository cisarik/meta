# Era 12 Whole Notes — admin OpenAI-compatible provider UX

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Non-authorizing. Public-safe by default. Michal owns any meta Git
commit.

Working identity (proposed until Planner + Cooperator lock it):

```text
framenest-admin-openai-compatible-provider-registry-and-vision-probe
```

Trace:

```text
/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/
```

Handout: `00_handout_agent.md` (2026-09-16). Not current authority.

## Session log

- **2026-09-16 — seed from predecessor ChatOrchestrator.** Cooperator dropout
  orientation; NUC SSH and global sudo reported ready; brainstorming on
  OpenCode Go as HTTP provider, jsonc-style add, ping/pong vision probe in
  FrameNest admin UI (not Django); order to hand off to a fresh Agent
  Orchestrator with ~1M context. No FrameNest mutation. No Worker dispatched.
  Public `main` not independently `ls-remote`'d in that session.

## Confirmed-refinements ledger (Cooperator intent, not ADR)

1. OpenCode is a **server AI provider**, not a Worker and not `opencode` CLI.
2. API key + vision filter + image analysis.
3. Prefer **OpenCode Go** gateway URL, not Zen aliased as Go.
4. Standardized **add provider** like OpenCode jsonc, FrameNest-owned JSON,
   secrets never in the file.
5. Ping (text) then pong (tiny PNG, “what color is this?”) from **admin UI**.
6. Not Django — FrameNest administrator web shell.
7. Test step-by-step on NUC after publish+refresh; judge function, design, UX.
8. No copy-paste ferry. Orchestrator writes prompts to this directory;
   Workers write reports here. Cooperator does not create/rename files.
9. No subagents. Planner is the first dispatched Worker.
10. Keys must not enter the browser unless a later explicit security decision
    overturns SPEC (predecessor recommendation: refuse).

## Open gates for the incoming Orchestrator

- Re-verify FrameNest HEAD `33946e08…`, AP pin `7478ddb…`, public `main`.
- Revalidate AP upgrade ledger against live pin (entry last seen against
  `7ef45da…`).
- NUC release SHA vs public `main` unknown; era 11/01 did not deploy.
- NUC banner: system restart required (not this whole).

## Session log addendum

- **2026-09-16 — fresh Agent Orchestrator restore (read-only).** No Worker
  dispatched yet. Gates independently observed:
  - canonical checkout `/home/agile/Projects/framenest`; branch
    `feat/x-meme-browser-companion`; porcelain clean; local HEAD
    `33946e08447dc92621ed6844b4b5d13a19ec29f1`.
  - `git ls-remote origin`: `refs/heads/main` and
    `refs/heads/feat/x-meme-browser-companion` both
    `33946e08447dc92621ed6844b4b5d13a19ec29f1`. **Public `main` directly
    observed; no `public branch state not directly observed` caveat applies.**
  - AP gitlink == `.ap` HEAD ==
    `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`; `./.ap/ap doctor` PASS
    (stable variant, managed block OK).
  - Alembic head `0033` (`0033_media_analysis_proposals`, down_revision
    `0032`). Predecessor intuition "no 0034 required" stands unless the plan
    proves otherwise.
- **Ledger revalidation (live pin `7478ddb…`, read-only).** Entry
  `consumer-declared-execution-and-capability-route-binding` remains valid:
  RF-16 present in `.ap/AP.md`; `.ap/docs/adr/0012` and `0018` present at the
  live pin; root `ap.project.conf` (sanitized-v1, three operations) and
  `docs/WORKER_EXECUTION_CONTRACT.md` present. State stays
  `accepted`/non-authorizing/`retain-active`. The file's `Last revalidated
  against` field still shows `7ef45da…`; the file was NOT rewritten (no repo
  write authority) — revalidation is recorded here. Not malformed, only a
  stale field.
- **Trace filename correction.** The handout text says `00_handout_agent.md`;
  the actual file in this directory is `00_handout.md`. Kept as-is
  (historical evidence, not authority).
- **Direct-observation corrections to handout intuitions** (all verified in
  the repository at the pinned baseline):
  - Gallery card 🧠 "silent canonical PUT" debt is **already fixed** by
    ADR-0078 (accepted 2026-08-27): card 🧠 is analyze-then-Edit with
    per-field proposal strips, zero bulk `PUT metadata`. No such debt belongs
    to this whole.
  - `GET /api/ai/media-suggestion-capability` is `provider.operate`-gated in
    `tailscale_uds` mode (`tailscale_ingress.py` route policy). In loopback
    TCP development the middleware is not installed and
    `GET /api/audience/me` returns `trusted_loopback` with the full admin
    capability set (`application.py`). Frontend `identityState.available` is
    true only for `tailscale_workspace`, so admin nav is hidden locally even
    though the server permits local admin capability.
  - Website-origin admin mutations do **not** need `companion_mutation=True`.
    `_mutation_origin_allowed` accepts the exact external origin for any
    route; the flag only additionally allows allowlisted
    `chrome-extension://` origins. Exactly five `companion_mutation` routes
    exist today (X submit, X retry, review opened, review apply,
    automatic-analysis PUT).
  - `.secrets/ai.env.fish` is sourced generically by the root launcher (no
    per-variable allowlist); adding `OPENCODE_API_KEY` is a docs/security
    contract change, not launcher code.
  - The Vercel adapter already speaks OpenAI chat-completions and accepts
    `provider_id`/`model_id` in its constructor; its base URL is a module
    constant. Natural seed for the generic adapter.
- **Cooperator statements carried forward (intent, not ADR):** OpenCode Go as
  a server HTTP provider (API key, vision); declarative add-provider records
  like OpenCode jsonc; ping (text) then pong (tiny PNG from admin UI);
  FrameNest administrator web shell (not Django); step-by-step NUC UX test
  after publish + refresh; no copy-paste ferry; no subagents.
- **Open observations (not blockers for planning):**
  - NUC deployed release SHA unknown to this session (no NUC access granted;
    era 11/01 did not deploy). `framenest-release status` is the authoritative
    readback at the later acceptance/deploy step.
  - OpenCode Go base-URL / catalog / vision-model facts are dated 2026-09-16
    claims only; Planner must re-fetch public docs and stay read-only.
  - Ordinary Tailscale users currently see the header 🧠 button while the
    capability route is admin-gated, so they get a sanitized "AI status
    unavailable". Candidate UX refinement for the Status-vs-Admin split;
    not classified as a defect yet.
  - NUC banner "System restart required" — capability context, not a task;
    no reboot in this whole unless Michal orders a bounded host task.
- **Next step:** one Cooperator decision — confirm whole identity
  `framenest-admin-openai-compatible-provider-registry-and-vision-probe` and
  authorize Planner session 01 dispatch (`01_planning.md` -> `01_report.md`
  in this directory, AP default grammar, direct Orchestrator dispatch).

## Session log addendum 2

- **2026-09-16 — Planner session 01 dispatched and delivered.** Cooperator
  confirmed the whole and authorized planning; the Orchestrator wrote
  `01_planning.md` (41494 bytes) and dispatched it as one complete prompt into
  one fresh Worker session via Agent Orchestrator default dispatch (the
  standing route selected in the handout; the dispatched session received
  only the prompt text as initial context, no parent transcript). The Worker
  Planner persisted its own terminal report: `01_report.md`, 62386 bytes,
  979 lines, SHA-256
  `1d5248289e4562199998dea75f77060e2f5f7056b12f5fa6d4f93a9aae93f3d9`,
  status PASS, coordinates echoed once, first line
  `### Report for ORCHESTRATOR_CHAT`. FrameNest unchanged at
  `33946e08…`, porcelain clean; no Git writes anywhere.
- **Orchestrator verification of delivery (not yet of plan content):**
  destination path, file presence, first line, coordinate block, and
  SHA-256 match the Worker's completion notice. Reconciliation of the plan's
  claims against the repository is the next Orchestrator step before the
  plan is presented for the Cooperator approval decision.
- **Cooperator reaction after the dispatch:** initial hesitation about the
  dispatched session ("Nie / Plannera mám dispatchovať / … keďže subagent už
  bežal"). Clarified: the dispatched session **was** Planner session 01 under
  the Cooperator-selected standing route `Agent Orchestrator default
  dispatch` (AGENTS.md/AP ADR-0019 + ADR-0022); "no subagents" forbids Worker
  internal delegation, Explore swarms, and parallel Workers, not this single
  complete-prompt dispatch. Awaiting one Cooperator decision: accept Planner
  session 01 as valid and proceed to plan approval, or select a different
  delivery route (P14 opt-out) for subsequent exchanges.

## Session log addendum 3

- **2026-09-16 — Cooperator parallel-planning experiment and trace renames.**
  Cooperator created `01_report_planner.md` (18432 bytes, SHA-256
  `a22c5df554bdbd6e46bbabe98e1808fb5a4baee454b30d44f26e003338532a18`) — a
  plan produced outside AP by an alternate model (Slovak, client Plan-mode
  frontmatter), and renamed the canonical session-01 companion `01_report.md`
  to `01_report_orchestrator.md`. Orchestrator verified the renamed file's
  bytes/SHA-256 are unchanged (`1d524828…`, 62386 bytes). Recorded as a
  Cooperator action; the canonical exchange-01 companion name is currently
  occupied by no file, and the experiment is **not** an AP Worker report
  (Companion Integrity Invariant). A foreign artifact written later to
  `01_report.md` would collide with the canonical companion and must not be
  committed as a report.
- **Plan reconciliation and synthesis (Orchestrator).** Both plans agree on
  architecture (schema v2, one registry world, generic OpenAI-compatible
  adapter, `vision_input` gating, golden red PNG fixture, bounded judge,
  sanitized sidecar, six audited `provider.operate` admin routes, website
  admin surface, ADR-0081, same five slices). Binding synthesis decisions:
  the experiment's explicit CLI record management (`provider add/list/remove`)
  is adopted into slice 1; per-operation locks (`.test.lock` + new
  `.vision-probe.lock`, busy `AI_PROVIDER_BUSY`) are adopted with UI-level
  mutual exclusion in slice 4; dynamic no-restart resolution stays in slice 3
  per the accepted plan. The accepted plan remains the detail owner.
- **Cooperator approval.** Cooperator directed proceeding to implementation
  ("podme na vyvoj", 2026-09-16). Implementation dispatched by Agent
  Orchestrator default dispatch; the translation request for the experiment
  was fulfilled separately as trace evidence.
- **Implementation session 02, exchange 01 — slice 1 (PARTIAL).**
  `02_implementation.md` → `02_report.md` (15702 bytes, SHA-256
  `427624170ee19fb457367d942e510cd98aaa6c034eb5e5cd5c42f5984747d566`).
  17 allowlisted paths; one local commit
  `f41df797d74ddd0a54c6c0d31f995bda8a8a4661` "Add declarative provider records
  and generic OpenAI-compatible adapter"; `375 passed` via the declared AP
  route. Single finding: `FrameNestSettings.ai_provider_id` still enforced the
  retired two-id enum in `src/framenest/configuration.py` (outside the
  allowlist), so the D5 end-to-end environment override did not hold.
- **Correction exchange 02 (PASS).** `02_implementation_02.md` →
  `02_report_02.md` (SHA-256 `b7d472d1…`). Three allowlisted paths; validator
  widened to the bounded declared-id syntax; `SUPPORTED_AI_PROVIDER_IDS`
  removed after importer check; commit
  `980db7af33910bb676eef46ed89fd2b453112bb6` "Accept declarative provider ids
  in settings environment override"; `408 passed`.
- **Slice 2 — vision probe / pong (PASS).** `02_implementation_03.md` (same
  session, exchange 03) → `02_report_03.md` (SHA-256 `ce6f403f…`). Golden
  fixture `src/framenest/infrastructure/ai/fixtures/vision-probe-red-8x8.png`
  created from an Orchestrator-pinned literal: 74 bytes, SHA-256
  `396f6aba97b0b4ac60a22cae643ef2df1676ab98050fa468bbcb1aadb69b9e44`, valid
  8×8 RGB(255,0,0) PNG; bounded judge, sidecar, `activity_lock`, generic and
  NVIDIA `probe_vision`, CLI `vision-probe`; commit
  `e6d91d1ba8cda0b22da2c345cbd313720e127e64` "Add vision probe fixture, judge,
  and CLI pong"; `346 passed` plus `123` affected-regression; wheel-resource
  contract included.
- **Trace evidence prepared.** `01_experiment_planner_plan_en.md` — English
  rendering and AP structural normalization of the experiment, clearly
  labelled non-authorizing comparative evidence (not a Worker report), with an
  Orchestrator reconciliation annex. Source preserved unchanged. Ready for the
  Cooperator's Meta commit.
- **State at this entry.** FrameNest local HEAD `e6d91d1…`, branch
  `feat/x-meme-browser-companion` ahead of `origin` by 3 commits, porcelain
  clean, no push, no NUC contact, no provider call anywhere.
- **Next step.** Orchestrator checkpoint with the Cooperator: proceed to
  slice 3 (admin API + route policies + audit), slice 4 (website surface),
  slice 5 (docs/ADR-0081), then whole-level independent acceptance →
  publication grant → routine NUC refresh → Cooperator numbered UX test;
  `OPENCODE_API_KEY` install on the NUC remains a separate explicit grant.

## Session log addendum 4

- **2026-09-16 — Cooperator direction:** "Pokračuj slice 3."
- **Slice 3 — administrator AI provider API (PASS).**
  `02_implementation_04.md` → `02_report_04.md` (SHA-256
  `b5ec28e3b6b0c00236e74ae825e6766b6dfed121c6ec3e0e08d6d639cfb115dc`).
  Six `provider.operate` admin routes (`GET /api/admin/ai/providers`, `PUT`
  and `DELETE /api/admin/ai/providers/{provider_id}`, `PUT
  /api/admin/ai/active-selection`, `POST /api/admin/ai/ping`, `POST
  /api/admin/ai/pong`) with route-policy rows, audit-before-mutation,
  website-origin mutation proof, sanitized no-secret responses, and
  per-call dynamic provider resolution (a provider added or activated takes
  effect without restart); shared
  `classify_provider_exception` keeps CLI and API taxonomy identical; 13
  allowlisted paths; commit
  `c66f5b6ae438d686d1e3c8f7b8e3ebccd0e885b9` "Add administrator AI provider
  API and dynamic provider resolution"; `534 passed` pre- and post-commit;
  `test_x_route_policy.py` (five companion routes) and
  `test_media_suggestion_api.py` green unmodified; route inventory 1:1,
  public-published composition, and audit-before-execution all green;
  porcelain clean.
- **State at this entry.** Local HEAD `c66f5b6…`; branch
  `feat/x-meme-browser-companion` ahead of `origin` by 4 commits; no push, no
  NUC contact, no provider call (tests use fake transports).
- **Next step.** Awaiting one Cooperator decision: proceed with slice 4
  (administrator web surface) and slice 5 (living docs + ADR-0081), or
  review the four local commits first. After slices 4-5: whole-level fresh
  independent acceptance → publication grant → routine NUC refresh →
  Cooperator numbered UX test.

## Session log addendum 5

- **2026-09-16 — Cooperator direction:** "Pokračuj slice 4."
- **Slice 4 — administrator AI provider web surface (PASS).**
  `02_implementation_05.md` → `02_report_05.md` (SHA-256
  `3096942381a7c0babeb12ee7db2cc130488171d8b0b92b1f62e14d668edaf75e`);
  commit `810b606dc9ca34e696dde3cffb533abb1b193884`. Header 🛠️ control,
  `settings-dialog`-styled dialog, provider list, record form with local
  read-only JSON preview, activate/ping/pong with in-dialog confirm and
  `confirm_cloud_upload: true`, identity helper for both audiences, no
  provider call on render or typing; `node --test` named suites `35 passed`
  pre/post commit and Python asset/ingress regression `207 passed`; both
  named JS suites green unmodified (one `"X-FrameNest-Request"` literal
  preserved). Resolved near-miss: narrow-width media queries relocated after
  the responsive-slice contract test caught an ordering hazard.
- **Slice 5 — living documents + ADR-0081 (PASS).**
  `02_implementation_06.md` → `02_report_06.md` (SHA-256
  `ddebb2c290a643242e3091a9c5995746e8275f4108fba85444c2ed9b518e3b5d`);
  commit `87411e040157c51f3e1056e8a6e62c0c8c514018`; exactly the eight
  allowlisted documentation paths; ADR-0081 `Accepted` (Cooperator plan and
  implementation direction 2026-09-16) with narrow supersession notes and no
  closed ADR body edited; SPEC §22, SECURITY, SERVER, README, AI_WORKSPACE,
  runbook, ADR index updated; docs-contract selection `140 passed`
  (`186` with the operator-network suite).
- **Whole-level candidate (Orchestrator reconciliation).** Chain
  `33946e0 → f41df79 → 980db7a → e6d91d1 → c66f5b6 → 810b606 → 87411e0`;
  branch ahead of `origin` by six commits; porcelain clean; `.ap` untouched;
  49 changed paths, all inside granted allowlists. Secret scan of the whole
  diff: no real credential; two benign matches (a "Bearer credential"
  docstring and a negative test that rejects a key-shaped value). Every slice
  report is PASS; deviations recorded and non-blocking: automatic-analysis
  classification of an unconfigured provider during a scheduler run is now
  `PROVIDER_UNAVAILABLE` (retryable) instead of `PROVIDER_NOT_CONFIGURED`
  (manual durable requests still preflight to 503); `DynamicAiProviderResolver`
  has a test-only `transport` kwarg; GET providers may report
  `environment`/`legacy compatibility` sources honestly; the routed lazy
  analyze path is proven indirectly (capability endpoints + fake-transport
  delegation) with the real proof belonging to the Cooperator's acceptance;
  ADR-0081 cites actual ADR filenames; OpenCode Go facts remain dated public
  documentation pending a provider-call grant.
- **No publication, no NUC contact, no provider call, no Meta Git commit.**
- **Next step.** One Cooperator decision: authorize the whole-level fresh
  independent acceptance (fresh Worker session 03, Fresh Independent Audit,
  exact candidate `87411e0…`), after which a separate publication grant,
  routine NUC refresh, and the Cooperator's numbered UX test follow. The NUC
  `OPENCODE_API_KEY` installation remains a separate explicit grant.

## Session log addendum 6

- **2026-09-16 — Cooperator authorized whole-level fresh independent
  acceptance.**
- **Primary independent acceptance — BLOCKED (session 03, exchange 01).**
  `03_acceptance.md` → `03_report.md` (SHA-256 `fcf5c849…`, 211 lines).
  Repository gate, candidate chain, 49-path allowlist, and claims R1-R7 all
  verified (882 Python + 35 Node tests green), but one negative control was
  refuted: **no Analyze path enforced the `vision_input` refusal** that
  SPEC.md:726-727, ADR-0081 decision 4, and AI_WORKSPACE.md:218-220 assert.
  Exact evidence: `media_suggestion_api.py:251,352` and
  `media_analysis_lifecycle_api.py:383` preflighted only provider
  configuration; the automatic executor did not check;
  `AI_MODEL_CAPABILITY_MISSING` existed only in the pong route. Pong and the
  CLI `vision-probe` were correct. Audit also recorded four non-blocking
  ledger candidates (abbreviated/hex IPv4 loopback hostnames pass the
  textual DNS check; GET admin denials unaudited by design; SECURITY.md:72
  stale CLI-only prose; PUT active-model check-then-act race) and two
  accepted residuals (automatic-analysis unconfigured classification shift;
  indirect routed-analyze proof).
- **One smallest coherent correction (session 02, exchange 07) — PASS.**
  `02_implementation_07.md` → `02_report_07.md` (SHA-256 `078ca01e…`); commit
  `7ff6546f345827d6df20bd5b13d5e57cb4bc90db` "Refuse non-vision models on
  Analyze paths" (7 paths): both suggestion-preview routes and the
  durable-analysis request now return `409 AI_MODEL_CAPABILITY_MISSING`
  before any provider work; the automatic executor raises a non-retryable
  `PROVIDER_MODEL_CAPABILITY_MISSING` that is not counted as a provider
  submission; pong, CLI `vision-probe`, movie identification, and existing
  classifications unchanged; `482 passed` plus 13 named new tests.
- **Full-fresh independent re-acceptance — PASS (session 04, exchange 01).**
  `04_acceptance.md` → `04_report.md` (SHA-256 `77735ba5…`, 249 lines).
  `Phase-qualified result: acceptance-PASS`; every claim R1-R8 and every
  positive/negative control verified on `7ff6546`; corrected N7 holds; new
  N8 holds (no provider-submission accounting, existing classifications
  unchanged); no new issue introduced; no closed ADR body edited; fixture
  bytes/hash and wheel presence re-verified.
- **State at this entry.** Local HEAD `7ff6546…`; branch ahead of `origin` by
  seven commits; porcelain clean; 53-path diff; `.ap` untouched; no push, no
  NUC contact, no provider call, no Meta Git commit.
- **Phase results so far (separate, cumulative):** Implementation PASS
  (slices 1-5 + correction), Acceptance PASS (fresh re-audit). Publication,
  Deployment (NUC refresh), Production acceptance (Cooperator numbered UX
  test), and ORCHESTRATOR closure remain open.
- **Next step.** One Cooperator decision: authorize publication of the
  accepted candidate to public `main` and the routine NUC refresh
  (`deploy/ubuntu/framenest-release status` / `check --release <SHA>` /
  deploy), so his numbered UX test runs against exactly this code. Installing
  `OPENCODE_API_KEY` on the NUC remains a separate explicit credential grant;
  locally he may add it to `.secrets/ai.env.fish` for an optional live check.

## Session log addendum 7

- **2026-09-16 — Cooperator authorized publication and routine NUC refresh
  ("akceptujem").**
- **Publication exchange 01 (session 05) — PASS.** `05_publication.md` →
  `05_report.md` (SHA-256 `22592731…`). Pre-push gate: both
  `refs/heads/main` and `refs/heads/feat/x-meme-browser-companion` at the
  expected parent `33946e0…`; one non-force push of the exact accepted commit
  `7ff6546f345827d6df20bd5b13d5e57cb4bc90db` to both refs; post-push
  readback confirmed. **Orchestrator independent public readback** via
  `git ls-remote origin` observed both refs at `7ff6546…` — Publication PASS
  independently verified. Local branch now in sync with its upstream;
  porcelain clean.
- **Report-format defect and repair.** The exchange-01 publication report
  omitted the required `Logical whole identity:` coordinate line (RF-19 /
  Companion Integrity Invariant). One bounded report-format repair exchange
  (session 05, exchange 02) rendered the complete corrected report at
  `05_report_02.md` (SHA-256 `801ad8c5…`) with all three coordinates once,
  preserving the original outcome; `05_report.md` was left byte-unchanged as
  historical evidence; no new Git, remote, or repository action occurred.
- **State at this entry.** Public `main` == public
  `feat/x-meme-browser-companion` == `7ff6546…`; local checkout clean and in
  sync; `.ap` untouched. Phase results: Implementation PASS, Acceptance
  PASS, Publication PASS. Deployment (NUC refresh), production acceptance
  (Cooperator numbered UX test), and ORCHESTRATOR closure remain open.
- **Next step.** Cooperator refreshes the NUC sudo timestamp (his usual
  global-sudo flow, outside the Worker) and signals ready; then the
  Orchestrator dispatches the routine NUC refresh Worker
  (`deploy/ubuntu/framenest-release status` → `check --release 7ff6546…` →
  `deploy --yes`, with the documented `migration-required` continuation if
  the live catalog is at `0032`, then readiness and `status` readback).
  `OPENCODE_API_KEY` installation on the NUC remains a separate explicit
  credential grant.

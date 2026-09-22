# Orchestrator synthesis — two plans for `framenest-nuc-chatgpt-analyze-provider`

Classification: private local Orchestrator reconciliation record for this logical
whole. Historical/evidentiary, non-authorizing. Cooperator owns any Meta Git
commit. This file is not a Worker report, not task authority, and not a plan
grant.

## Inputs

- **Plan A** — `01_report_00.md`: the AP Planner terminal report (session 01,
  exchange 01, fresh, native Plan Mode required, Extra High). Status PASS,
  plan delivered to file. Planning authority expired at the report.
- **Plan B** — `01_plan_00.md`: Cooperator-supplied alternative plan produced
  by a second model from the same `01_planning_00.md`, outside AP routing. It
  is planning evidence, not an AP terminal report; its report header and
  coordinates do not create an AP exchange.

Both plans were read in full. Both are competent and agree on the product cut
and on slice 1. They differ in depth, packaging, security, failure semantics,
and integration scope.

## Verdict

Adopt **Plan B as the primary technical spine**, merged with Plan A's verified
simplifications, its concrete bridge→FrameNest error map, and its explicit
slice-1 gate. Plan B is materially stronger on upload replay safety, ZIP
semantic readability, packaging for immutable releases, provider/coordinator
integration, concurrency fencing, runtime supervision, release integration,
and truthful metadata. Plan A is stronger on the no-project ask simplification,
the concrete error map, and a smaller upload surface.

## Verified evidence (read-only, this reconciliation)

| Claim | Evidence |
|---|---|
| AP pin: recorded gitlink `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (40 hex); `01_planning_00.md` and `00_notes.md` carry a 39-char transcription (`…391f…`). Both plans caught it. | `git rev-parse HEAD:.ap`; length check over trace files |
| Plain ask needs no ChatGPT project: `create_job` requires a project only when `mode` is set (`web_search`/`deep_research`); `project=None` with `mode=None` is accepted. | `66c40d43:src/kronika/bridge/jobs.py` `create_job` |
| Submit can click twice: `_submit()` clicks once, then `_retrySubmitCandidate()` may click a second time when all "first click did nothing" preconditions still hold (max 2 clicks, then `E_SEND_FAILED`). A race between acceptance and the retry remains possible. | `66c40d43:extension/src/headless/job_engine.mjs` `_submit`, `_retrySubmitCandidate` |
| Movie provider is captured at startup and movie POST executes synchronously. | `src/framenest/adapters/api/application.py:717-740`; `adapters/api/media_analysis_lifecycle_api.py:512` |
| `reasoning_enabled` must be exactly `True` today. | `src/framenest/application/movie_identification.py:127` |
| `derivative_count` is bounded 1..16. | `src/framenest/application/movie_identification.py:121-124` |
| Capability vocabulary: `vision_input, video_input, structured_text_output, image_generation, image_editing, reference_image, local_execution, cloud_execution`. | `src/framenest/infrastructure/ai/provider_records.py:31-42` |
| HTTP vision transport caps JPEG long edge at 768 px, separate from the 1024 px extraction constant. | `src/framenest/infrastructure/ai/image_derivative.py:15` |
| Upload is rejected in four sites (CLI exit 2, DOM engine, job_runner/runner, bridge `FILE_PATH` → 501). | pinned Kronika source, verified earlier |
| NUC state convention is `/var/lib/framenest/...`; Node and Chromium are not recorded in the host baseline. | `docs/UBUNTU_NUC_DEPLOYMENT.md:99-103`; `docs/NUC_HOST_BASELINE.md` |

The 39-char AP pin in my own `01_planning_00.md` is a recorded transcription
defect, not a repository divergence. The prompt file is not rewritten (RF-19).
Every future grant quotes the correct 40-char pin.

## Resolved divergences (decisions)

- **D1 Vendor and packaging** — Plan B: `vendor/kronika-ask/`, Python package
  `kronika`, JS assets inside the package at `kronika/_assets/extension/...`
  resolved via `importlib.resources`, root Poetry packaging, an installed-wheel
  test outside the checkout, and one installed entry point
  `framenest-chatgpt-page` (`ask`, `bridge run/status`, `runtime run`, `login`).
  Plan A's plain `include` is insufficient for immutable releases with no `.git`.
- **D2 Strip surface** — Plan B: reduced protocol v2 plus staged-file endpoints
  (`POST/GET/DELETE /v1/files`), delete `job_runner.js` (extension executor),
  `ask -f` takes an opaque staged file ID, never a path.
- **D3 ChatGPT project** — keep Plan B's minimal scratch-project capability with
  exact-origin and containment validation; Plan A's verified fact (no project is
  technically required) keeps the no-project ask as a documented configuration
  alternative. The Cooperator supplies the project URL privately. *(visible
  choice, default = scratch project)*
- **D4 Frame envelope** — Plan A's 480 px / quality 60 primary (better for
  on-screen text and faces) with Plan B's step-down (384 px / q50) only if
  needed to reach the count floor; Plan B's byte-accounting formula, ZIP
  overhead model, budget-profile persistence and invalidation, probe ceilings,
  and the randomized-visual-label semantic ZIP test. Shipping floor
  **at least 12 frames**; below it, stop and return measurements for a
  Cooperator decision. *(visible threshold)*
- **D5 Primary ask** — Plan B: one nine-key JSON ask with `genres: []` enforced
  and the `ATTACHMENT_UNREADABLE` sentinel; Plan A's plain-text title parse is
  dropped. Genre fallback: Plan B's two-key JSON, tentative, run at most once
  and only after a valid readable primary result with no title.
- **D6 Upload transfer** — Plan B's staged-file lifecycle and security matrix;
  Plan A's runner-owned temp path plus `DOM.setFileInputFiles` as the primary
  transfer (never client-supplied paths), Plan B's in-memory CDP transfer as
  the fallback if the verified input requires it.
- **D7 One-Send and unknown outcome** — exactly one Send click per job;
  ambiguous acceptance is an unknown outcome and is never automatically
  resubmitted; idempotency identity per run/attempt/stage; executor lease
  fencing with cancellation acknowledgement.
- **D8 Concurrency** — process-shared `flock` for page operations across admin,
  CLI, and durable work; bridge one-executor lease; no provider call inside a
  database transaction.
- **D9 Lifecycle integration** — per-operation analysis-session snapshot; movie
  runs dispatched by the coordinator by analysis definition; direct movie
  execution removed from the HTTP handler; existing status endpoint and review
  UI preserved; interrupted runs reconciled without resubmitting unknown
  outcomes; page reasoning metadata nullable and serialized truthfully.
- **D10 Runtime** — `runtime run` supervisor and `framenest-chatgpt-page.service`,
  fixed loopback port (verify 8766), private state, login-wizard hardening, no
  browser per request, Node 22 minimum (verify on host). State path follows the
  NUC convention: `/var/lib/framenest/chatgpt-page/` plus runtime
  `/run/framenest/chatgpt-page/`; the service account is restricted to that
  subtree.
- **D11 Release** — extend `deploy/ubuntu/framenest-release` and its tests
  (asset/runtime checks, quiesce, atomic switch, joint rollback, readiness
  without an ask). Deployment stays a separate grant.
- **D12 Slices** — Plan B's content with Plan A's dependency order (below).
- **D13 Pin** — all grants quote `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.

## Adopted from Plan B (beyond Plan A)

One-Send/no-replay and unknown-outcome rules; executor lease fencing; ZIP
semantic-readability probe with randomized visual labels; byte-accounting
formula, budget profile, and invalidation; `ATTACHMENT_UNREADABLE` sentinel;
installed-package assets and wheel test; protocol v2 and staged-file lifecycle;
per-operation session snapshot; coordinator movie dispatch; nullable reasoning
metadata; process-shared lock; runtime supervisor and systemd unit; release
quiesce/atomic/joint rollback; login-wizard hardening; removal of the
resource-policy canary and of arbitrary-profile attachment; the full security
test matrix; risk table and stop rules.

## Adopted from Plan A (beyond Plan B)

No-project ask verified from code (kept as a configuration alternative);
concrete bridge-outcome → existing FrameNest error taxonomy mapping; simpler
two-endpoint upload surface as the minimum; 480 px / q60 as the primary
recognition envelope; explicit slice-1 gate items (no forbidden imports/routes,
`ask -f` still fails, `node --check`, focused tests through
`./.ap/ap exec --operation test-focus`).

## Synthesized slice plan (each slice needs its own bounded grant)

1. **S1 — Vendor copy + strip + packaging** (one commit, revertible as a unit).
   Exact manifest, `vendor/kronika-ask/`, reduced ask/bridge/login surface,
   root packaging, `upstream.json`, offline validation, installed-package test.
   No provider registration, no upload enablement.
2. **S2 — Probe tooling + budget contract** (offline; generated fixtures,
   sanitized output, byte accounting, no-secret guarantees).
3. **S3 — Locator and transport probe** (small live grant, read-only against the
   composer through the wizard session; stop and re-probe on mismatch).
4. **S4 — Staged upload + executor safety** (staging lifecycle, CDP transfer,
   one-Send, cancellation, fencing, security matrix).
5. **S5 — `P1-COMPOSER-ZIP` budget probe** (live, bounded: attachment limits and
   semantic ZIP readability; produces the budget profile; no frame count in
   product code).
6. **S6 — Page evidence + provider registration + exact prompts** (depends on
   the accepted budget profile).
7. **S7 — Lifecycle and review integration** (session snapshot, coordinator
   dispatch, truthful metadata, draft conversion, existing review UI).
8. **S8 — Runtime supervision + release support** (may precede live enablement).
9. **S9 — NUC enablement and acceptance** (separate publication, deployment, and
   rendered-acceptance grants).
10. **Optional S10 — Catalog metadata lookup** after a title exists; never blocks
    identification.

Between S4 and S5, publishing `main` and deploying the minimal kernel release
(provider still unselected) through `deploy/ubuntu/framenest-release` is a
separate Cooperator-authorized grant, because the live probes run on the NUC
against the immutable release.

## Cooperator decision points

- Now: approve this synthesis and the slice order.
- Visible defaults he may override: scratch project vs no project; ≥12-frame
  shipping floor; 480 px → 384 px step-down envelope.
- Later: scratch-project URL; P1 authorization (NUC, browser, network,
  generated fixtures, real asks); publication and deployment of the minimal
  kernel; private media for recognition acceptance; optional catalog source.

## Next step

Issue the S1 implementation grant: session 01, exchange 02,
`current-worker-session`, `Native planning mode: not-used`, exact baseline
`7ff6546f345827d6df20bd5b13d5e57cb4bc90db`, exact allowlist and branch, one
commit, focused offline validation through the declared AP execution route, and
no publication.

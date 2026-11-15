# 04 youtube_fixes — Orchestrator notes

```text
Logical whole identity: youtube-fixes
Development run identity: kronika-run-01
Orchestrator session scope: logical-whole
Opened: 2026-11-14
Baseline: 2c4f4d89375628df28926060aba305e5d80bacff
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50
Repository: https://github.com/cisarik/kronika
Delivery route: manual Cooperator delivery
Logical-whole closure: not-closed
```

## Opening decision — 2026-11-14

The COOPERATOR selected and opened `youtube-fixes` as the next bounded logical
whole in `kronika-run-01`. The in-scope objective is predecessor residual R-1:
the YouTube acquisition attempt that ended in the sanitized inspection failure
`INSPECTION_OUTPUT_LIMIT` and produced no catalog media. R-2 (X acquisition
failures / «Save to Kronika failed») and R-3 (full-page narrow My contributions
title collapse) remain outside this whole.

The COOPERATOR explicitly decided the persistence model for the whole:

- the ORCHESTRATOR writes every prompt file directly into this Meta trace at
  the exact exchange path;
- every WORKER writes its complete terminal report directly into this Meta
  trace at the exact report path, reads it back, verifies the first line and
  coordinates, and then sends a short completion notice separately;
- Meta Git archival remains with the COOPERATOR. No prompt/report pair is
  committed by the Orchestrator or a Worker under this decision.

The delivery route remains manual Cooperator delivery: the COOPERATOR selects
the Worker session and receives the exact prompt file. No subagent dispatch is
authorized by this whole. A later direct-dispatch selection would be a separate
material delivery-route decision.

No repository, host, NUC, external-service, provider, browser or credential
mutation was authorized by the opening. The first Planner is read-only for the
repository apart from its exact report write. Implementation, publication,
deployment and rendered acceptance each require a separate later grant.

## Handout Revalidation Record

```text
Handout revalidation: /Users/agile/meta/projects/kronika/01/04-youtube_fixes/00_handout_00.md
Received handout status: provisional
Revalidated against: Kronika 2c4f4d89375628df28926060aba305e5d80bacff; AP pin d7023cf037f6d17885c3ede5c04812c61640da50; public main 2c4f4d89375628df28926060aba305e5d80bacff; local main worktree clean; .ap gitlink and submodule HEAD d7023cf; predecessor closure 12_closure.md; run map 00_RUN_MAP.md; docs/AP_UPGRADE_OBSERVATIONS.md
Usable facts: repository identity, branch main, local HEAD and public main 2c4f4d8, clean worktree, AP pin d7023cf, ap doctor PASS, ap project check --baseline 2c4f4d8 PASS, predecessor closure at 2c4f4d8, no active Worker or repository mutation, run map entry 03 provisional and entry 04 household-onboarding, unselected household handout dated 2026-11-08 against 246c9f8, yt-dlp==2026.7.4 pinned and installed as 2026.07.04, MAX_STDOUT_BYTES 1_048_576 and MAX_STDERR_BYTES 65_536 shared by inspect and download, returncode-before-overflow order in inspect, capture reads to EOF while retaining the first limit bytes, coordinator inspection-stage mapping, API/CLI failure_code projection, companion failure_category-only projection, no direct INSPECTION_OUTPUT_LIMIT test, no inspection-failure injection in the integration lifecycle test
Stale facts and corrections: none
Not revalidated: NUC release, active/web release identity, service state, database revision and backup readiness (no NUC access grant for Stage 1); Cooperator rendered acceptance at 2c4f4d8 (predecessor closure claim, not re-observed); live YouTube failure and observed payload size (no live-call authority; the private URL is not recorded); exact yt-dlp --dump-single-json payload composition (the first Planner must establish it from installed package source without network)
Handout disposition: adopted
```

## Stage 1 evidence — 2026-11-14

- Repository identity: `https://github.com/cisarik/kronika`; branch `main`;
  local `HEAD` and public `main` both
  `2c4f4d89375628df28926060aba305e5d80bacff`; `git status --porcelain=v1`
  empty; `.ap` gitlink and submodule `HEAD` both
  `d7023cf037f6d17885c3ede5c04812c61640da50`.
- `./.ap/ap doctor`: PASS, stable variant, pinned AP clean. `./.ap/ap project
  check --root /Users/agile/Projects/kronika --baseline 2c4f4d8`: PASS, CPython
  3.13, project identity `cisarik/kronika`; the tool reported only a sanitized
  inherited-environment warning for `SSH_AUTH_SOCK` and `PATH`, with no values
  printed.
- Predecessor `03-companion-download-notifications` is closed at `2c4f4d8`;
  its closure records production-acceptance-PASS, publication and NUC
  deployment at that candidate. No active Worker and no repository mutation
  were found. The Meta checkout is locally dirty exactly as the handout
  described: `12_closure.md` and later predecessor correction/report files are
  untracked, `00_notes.md` is modified, and this whole's directory is
  untracked. That is trace-archival state, not repository or host mutation. No
  Meta file was committed, deleted, renamed or normalized.
- Run map `00_RUN_MAP.md` is stale: entry 03 still reads `provisional` and entry
  04 still reads `household-onboarding`. This session's scope is
  `logical-whole`, not `development-run`; the run map was left untouched. The
  unselected `04-household-onboarding/00_handout.md` was not opened, not
  treated as a fallback, not deleted and not renumbered. Any run-map
  reconciliation or disposition of that entry belongs to a run-scoped
  Orchestrator after a Cooperator decision.
- Upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` is structurally valid
  (storage version 1, target `upgrade https://github.com/cisarik/ap.git`, path
  declared in `AGENTS.md`). Its one active entry,
  `consumer-declared-execution-and-capability-route-binding`, remains
  `accepted`, non-authorizing, `retain-active`, with no implementation grant.
  It was revalidated against the current `AGENTS.md`, the Cursor Worker
  Execution Boundary in `docs/WORKER_EXECUTION_CONTRACT.md`, and the working
  `ap project check` route. No ledger write was made because this whole holds
  no repository mutation grant.
- Inspection boundary verified in
  `src/kronika/infrastructure/youtube/downloader.py`:
  `MAX_STDOUT_BYTES = 1_048_576` and `MAX_STDERR_BYTES = 65_536` are shared by
  `inspect()` and `_run_download()`; `inspect()` checks `returncode != 0`
  before overflow; `_capture_stream()` retains the first `limit` bytes but
  keeps reading until EOF; `_run_bounded()` waits for exit or the 60-second
  inspection timeout. The coordinator maps `YouTubeInspectionError` to
  `YouTubeFailureStage.INSPECTION`; the request API and operator CLI expose
  `failure_code`; the companion `youtubeSnapshot()` exposes only
  `failure_category` and correctly maps terminal `failed` to `Download failed`.
- Test gap verified: `tests/unit/infrastructure/youtube/test_downloader.py` has
  no direct `INSPECTION_OUTPUT_LIMIT` case, and
  `tests/integration/test_youtube_acquisition_lifecycle.py` injects a download
  failure but no inspection failure. The Planner must propose the smallest
  layered regression set; no test was run during restoration.
- Trace destinations checked physically: this directory is not a symlink;
  `00_handout_00.md` resolves inside it; `01_planning_00.md` and
  `01_report_00.md` were absent at opening.
- Not revalidated: NUC release/service state, the predecessor rendered
  acceptance, the live failing video and its payload size. Each is named in the
  Handout Revalidation Record with its reason and remains a Cooperator-owned
  evidence decision.

## Next step

Issue the first Planner prompt `01_planning_00.md` for a fresh Worker session
`01`, exchange `01`, phase planning, `Native planning mode: required`, with
report destination `01_report_00.md`. The Planner is read-only for the
repository apart from its exact report write. Recommended reasoning is High:
the question combines a bounded-output security boundary with external-tool
output shape and exact download-format selection. The plan is approval-gated;
implementation is prohibited until a separate complete implementation grant
with `Native planning mode: not-used`.

## Planner report and plan review — 2026-11-14

The first Planner returned `01_report_00.md` as a complete decision-complete
plan with status PARTIAL. The PARTIAL is the terminal-notice report-write
limitation only: the Planner wrote `report-write blocked by native Plan Mode`,
and the COOPERATOR persisted the exact complete report at the exact trace path.
The saved file begins `### Report for ORCHESTRATOR_CHAT`, echoes the three
coordinates, and contains the complete plan. The report's own "report file was
not written" sentence and PARTIAL status describe the terminal-notice state,
not the current trace state. The report is preserved as exact historical
evidence; no rewrite and no completion exchange are needed for delivery.

Plan review:

- Primary route: selective `--print` projection through the pinned tool,
  inspection-only early termination, and separate inspection/download constants
  at the same numeric values. The numeric caps stay 1 MiB/64 KiB; the pin stays
  `2026.7.4`; the companion stays `Download failed`.
- The field inventory, payload-composition argument, five-route comparison,
  format-selection equivalence fixture, security argument, pinned-tool
  argument, failure/quota argument, SPEC owner, acceptance plan and D1-D7
  recommendations are evidence-backed and decision-complete.
- Finding 1, citation: the installed package does not contain `README.txt`.
  The `--print` and output-template documentation is in
  `yt_dlp-2026.7.4.dist-info/METADATA` (the installed long description), and
  the object-traversal implementation is in `YoutubeDL.py`
  (`prepare_outtmpl`/`traverse_obj`). The plan's mechanism claim is supported;
  the implementation prompt must cite those owners and must not rely on a
  non-existent `README.txt`.
- Finding 2, edge-case behavior: the plan's parser maps a formats-line `NA` to
  `INSPECTION_INVALID_OUTPUT`. For a public video whose projection has no
  `formats` key, the existing code would raise `NO_VISUAL_STREAM` from
  `_inspection_from_payload`/`_select_plan`. The implementation prompt must
  treat a formats-line `NA` as an empty list and preserve `NO_VISUAL_STREAM`;
  the test matrix must add that case. A metadata-line `NA` remains
  `INSPECTION_INVALID_OUTPUT`.
- No targeted revision is recommended: the primary route, security argument
  and allowlist are unaffected by the two corrections. They are binding
  implementation constraints, not a new plan.
- Plan disposition: accepted subject to COOPERATOR approval and the two
  corrections. Implementation authority is not granted.

## Plan approval and implementation preparation — 2026-11-14

The COOPERATOR approved the decision-complete plan and the D1-D7
recommendations with the two binding corrections. The implementation prompt
`01_implementation_01.md` was prepared for the current Planner session `01`,
exchange `02`, `Native planning mode: not-used`, with the four-path allowlist,
one local commit, focused unit and integration tests, and no push. Its report
destination is `01_report_01.md`. The live attempt, publication, NUC refresh
and rendered acceptance remain separate later grants. Issuance/delivery of the
implementation prompt still requires the COOPERATOR's explicit confirmation;
plan approval is not implementation authority.

## Implementation delivery mismatch — 2026-11-14

Exchange `01/02` returned `01_report_01.md` that is byte-identical to
`01_report_00.md` (SHA-256 `dc548d0736ca7c6842aebcfc7f82025ca393d0c36316f21fd10340762c29f29b`).
It carries the planning coordinates, Planner profile, planning task identity,
PARTIAL status and the planning plan content. The repository is unchanged at
`2c4f4d8`; there is no candidate commit, no changed path and no test evidence.
The artifact is rejected as a delivery mismatch and not accepted as an
implementation report. It is preserved as historical evidence and will not be
overwritten. Coordinates `01/02` are consumed. The next exchange is a fresh
implementation session `02/01` (recommended, because the current session
replayed the planning artifact for an implementation prompt) or a current
session renewal `01/03`, pending the COOPERATOR's routing decision.

## Fresh implementation session — 2026-11-14

The COOPERATOR selected fresh session `02/01`. The corrected implementation
prompt is `02_implementation_00.md` with report `02_report_00.md`,
`fresh-worker-session`, `Native planning mode: not-used`, the same accepted
plan, the two binding corrections, the four-path allowlist, one local commit,
and no push. The report path was absent at preparation. The prompt carries no
continuity anchor and requires independent repository re-gating. The earlier
`01_implementation_01.md` and the mismatched `01_report_01.md` remain preserved
as historical evidence.

## Implementation PASS and acceptance preparation — 2026-11-14

Fresh session `02/01` returned `02_report_00.md` with status PASS and
`implementation-PASS` for candidate `eb5af0e49729eaf87eb3210ce0fd87295daae826`,
parent `2c4f4d89375628df28926060aba305e5d80bacff`, subject
`fix: project youtube inspection metadata`. The candidate changes exactly the
four allowlisted paths: `src/kronika/infrastructure/youtube/downloader.py`,
`tests/unit/infrastructure/youtube/test_downloader.py`,
`tests/integration/test_youtube_acquisition_lifecycle.py` and `SPEC.md`.
The worktree is clean and the branch is one commit ahead of `origin/main`.
No push, NUC, deployment or network call occurred.

ORCHESTRATOR reconciliation: the exact focused command from the prompt was
re-run read-only through `./.ap/ap exec` against baseline `2c4f4d8` and
reported 48 passed, 0 failed. `git diff --check 2c4f4d8..eb5af0e` is clean.
The candidate diff is exactly the four paths.

The implementation report's MEASURED critique is a plan-naming issue, not a
candidate defect: the plan called the over-cap format outcome
`FINAL_SIZE_LIMIT`, but `_select_plan` refuses every sized candidate before
that post-selection check and raises `COMPATIBLE_FORMAT_UNAVAILABLE` when the
source has audio. The selector is unchanged and the full payload and the
projection both reach the same code. No correction is required for the
candidate; the historical plan keeps its naming and the acceptance evaluates
the actual behavior.

One LEAD remains for acceptance: a formats-line JSON `null` is treated as
`INSPECTION_INVALID_OUTPUT`, whereas the old full-document path would reach
`NO_VISUAL_STREAM`. The plan's explicit parser spec says any line-2 shape other
than a JSON list or `NA` is invalid, so this is a consequence of the approved
spec, not an implementation deviation. The acceptance prompt requires the
fresh auditor to test it, record the actual code and classify it as an
accepted residual or a concrete finding. It does not block implementation PASS.

Implementation PASS is non-independent. A fresh independent acceptance is the
next required phase. The prepared acceptance prompt is `03_acceptance_00.md`
for fresh session `03/01`, with report `03_report_00.md`; publication, NUC
deployment, the live attempt and rendered acceptance remain separate later
grants.

## Cooperator publication and NUC grant — 2026-11-14

The COOPERATOR authorized the fresh independent acceptance and, contingent on
its verdict, publication of the accepted candidate to `cisarik/kronika` `main`
and routine NUC deployment through `deploy/ubuntu/kronika-release`. He ran
`sudo -v` outside the Worker to establish the remote sudo timestamp.

The grants are sequential and conditional, not a waiver of any gate:

- acceptance-PASS is required before publication;
- publication-PASS, a direct public `main` readback and
  `kronika-release check --release <accepted-40-hex-SHA>` are required before
  deployment;
- the deployment Worker uses
  `scripts/operator/network/kronika_nuc_worker_gate.fish --probe` first, the
  canonical `KRONIKA_NUC_SSH_*` variables, `sudo -n true` readback, and a
  terminal `sudo -K`; it must not run `sudo -v` or handle a password;
- a password-required `sudo -n true` is expected lifecycle state after an
  earlier release, not a host defect; the COOPERATOR re-establishes the
  timestamp outside the Worker if it has expired;
- publication is a normal non-force push; no force, history rewrite, schema
  bypass or deployment beyond the routine helper is authorized.

No publication or deployment occurred before acceptance. The acceptance
prompt remains read-only and does not use the publication or deployment grant.

## Acceptance PASS — 2026-11-14

Fresh session `03/01` returned `03_report_00.md` with status PASS,
`acceptance-PASS`, C01-C29 PASS and a truthful independence statement. The
candidate is `eb5af0e49729eaf87eb3210ce0fd87295daae826`, parent
`2c4f4d89375628df28926060aba305e5d80bacff`. The auditor re-ran the focused
command: 48 passed, 0 failed; `git diff --check` clean; candidate-mode project
check PASS (non-authorizing).

C21 resolved the plan-naming discrepancy: the over-cap code is
`COMPATIBLE_FORMAT_UNAVAILABLE`, the selector is unchanged, and the plan's
historical `FINAL_SIZE_LIMIT` name is not the reachable case. C28 resolved the
formats-line `null` LEAD: installed `prepare_outtmpl` replaces a `None` value
with the `NA` placeholder before the `j` conversion, so binding correction 2's
`NA` path is the reachable one; JSON `null` remains an accepted residual of
the explicit parser spec. No control failed and no correction is required.

Acceptance disposition: ACCEPT candidate
`eb5af0e49729eaf87eb3210ce0fd87295daae826` at `acceptance-PASS`.

The COOPERATOR pre-authorized publication and routine NUC deployment. The
prepared publication prompt is `04_publication_00.md` for fresh session
`04/01`, with report `04_report_00.md`. Publication is a normal non-force push
of the accepted commit to `cisarik/kronika` `main` with direct `ls-remote`
readback. NUC deployment remains after publication PASS and
`kronika-release check --release <accepted-SHA>`; the COOPERATOR's `sudo -v`
timestamp is current but may expire.

## Publication PASS — 2026-11-14

Fresh session `04/01` returned `04_report_00.md` with status PASS and
`publication-PASS`. The push was one normal non-force push
`2c4f4d8..eb5af0e` on `main`, exit 0. Direct
`git ls-remote origin refs/heads/main` readback is
`eb5af0e49729eaf87eb3210ce0fd87295daae826`. Local `HEAD` is the same
candidate, the worktree is clean, and the branch tracks `origin/main`. No NUC,
SSH, sudo, deployment or external-service action occurred in the publication
exchange. The accepted candidate is public.

The prepared deployment prompt is `05_deployment_00.md` for fresh session
`05/01`, with report `05_report_00.md`. It names the accepted public SHA
`eb5af0e`, the routine `deploy/ubuntu/kronika-release` helper, the NUC worker
gate, `sudo -n true` readback, and the terminal `sudo -K`. The COOPERATOR
established `sudo -v` outside the Worker; if it has expired the deployment
Worker stops and asks him to re-establish it.

## Deployment PASS — 2026-11-14

Fresh session `05/01` returned `05_report_00.md` with status PASS and
`deployment-PASS`. Pre-deploy active/web was `2c4f4d8`, `check --release
eb5af0e` PASS, the deploy exited 0, and post-deploy active/web is
`eb5af0e`. Service is active, database revision is `0035`, backup restore
readiness is ready, and the capture release is unchanged at
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915`. Terminal `sudo -K` exited 0; the
following `sudo -n true` correctly requires a password.

The report's MEASURED prompt-precision critique is recorded as a lesson: the
deployment prompt said to run the helper "through the gate", but the helper is
the local canonical entry point and the gate executes a bounded remote command.
The Worker correctly used the local helper and the gate only for the probe and
the bounded sudo commands. The deployment is valid; future deployment prompts
must name the local helper and the gate's sudo commands as separate steps.

Deployment PASS is separate from production acceptance. The NUC now serves
`eb5af0e`; the rendered acceptance belongs to the COOPERATOR and remains the
final evidence for closure. The previously failing video may be attempted at
most once (D2); if it still fails at inspection, D7 applies and the video
remains unacquirable inside the bound. No extension reload is required because
no extension file changed; a source-tab and side-panel refresh ensures the
request reaches the updated NUC.

## Rendered acceptance result — 2026-11-14

The COOPERATOR performed one live attempt on the previously failing video
against the NUC at `eb5af0e`. The rendered result is:

```text
Failure stage: download
Sanitized failure code: DOWNLOAD_FAILED
Metadata: Not cataloged yet
Publication: Not cataloged yet
```

No URL, title, channel, filename or claim identifier was recorded. The attempt
was one only; no retry was made.

Classification: R-1's inspection boundary is effective. The claim no longer
fails at inspection with `INSPECTION_OUTPUT_LIMIT`; it advances to the download
stage. The oversized inspection payload problem is resolved by the projection.
`DOWNLOAD_FAILED` is a new download-stage acquisition residual (R-4), outside
the approved plan's inspection boundary. The candidate did not change the
download path, the selected format plan is the existing selector's plan, and
the generic code does not expose the underlying yt-dlp cause. The video remains
unacquirable.

Do not retry the claim without a new bounded diagnostic or acquisition
decision; a retry creates a new claim and would consume another failed-request
slot without new evidence. R-4 is not a defect in the inspection fix and not a
regression of the companion history surface.

The whole's production acceptance for the inspection boundary is supported by
this rendered evidence. The COOPERATOR decides whether to close `youtube-fixes`
with R-4 as a new residual or to open a new logical whole for the
`DOWNLOAD_FAILED` acquisition cause. Closing the whole does not claim the
specific video was acquired.

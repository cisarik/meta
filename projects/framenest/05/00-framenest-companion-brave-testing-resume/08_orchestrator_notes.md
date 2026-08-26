# Orchestrator notes — era 05 / framenest-companion-brave-testing-resume

Ledger storage version: 1
Maintained by: Agent Orchestrator. Append-only narrative; superseded facts move to Git/history.

## 2026-08-26

- Era opened from handout + addendum. Required reading completed (AP pin docs,
  worker contract, backlog, ADR-0073/0074, INFOSEC, acceptance guide,
  README/SECURITY/SERVER status). Rotation verification all-PASS: HEAD ==
  public main `91410fe063d9907304cff4550f61d403880a2eeb` (credential-free
  ls-remote), tracked-clean worktree, AP pin `9c5cc44…`, schema head `0033`,
  backlog opens.
- Gate A classified PASS from Cooperator transcript: NUC
  `framenest-release status` active release equals tested main SHA, schema
  `0033`, service active, backup ready. Shared-SHA precondition satisfied.
- Cooperator approved session 01/exchange 01 issuance ("vygeneruj profesionalny
  prompt"). Prompt staged as `01_acceptance_00.md`; delivery package: fresh
  Cursor Worker session, Plan Mode off, reasoning Medium.
- Exchange 01 terminal report classified **acceptance-PASS (deterministic
  portion)**. Claimed evidence: `ap project check` PASS; batches 212+50+45
  Python passed via `test-focus`; Node 50+24+9 passed; total 390/0; zero Git,
  NUC, provider, browser effects. ORCHESTRATOR independent verification:
  HEAD/branch/worktree/AP pin re-checked unchanged post-report; both
  Missing-evidence owner files exist with the named tests
  (`tests/unit/infrastructure/persistence/test_companion_review_repository.py`,
  `tests/integration/persistence/test_analysis_proposal_migration.py`);
  report archived beside prompt. Sanitization compliance confirmed.
- Non-blocking precision observations recorded (no action now):
  1) selected proposal rate-limit tests inject `max_submits_per_hour=2` —
  mechanism proven, six-per-hour default not asserted by an executed test;
  2) selected configuration suites do not assert
  `automatic_media_analysis_enabled is False` on load_settings — coverage is
  wording-level via the privacy contract suite. Both remain candidates for a
  later hygiene slice, not blockers.
- Known-stale doc note preserved: `docs/X_COMPANION.md` “fade by position” —
  ledger candidate for the future companion-docs closeout whole.
- Exchange 02 issued (`01_acceptance_01.md`) as **current-worker-session**
  renewal: one `test-focus` over the two gap-owner files, closing non-v1
  listing / corrupt-JSON resilience / omitted-category listing / successful
  mixed-key Apply union / `0033` additive+downgrade coverage. Delivery:
  same session, Plan Mode off, Medium, archive pair after outcome exists.
- Pending: exchange 02 report → rendered Brave pass sequencing (NOT-RUN-here
  list from `01_report_00.md`), allowlist quiet gate before live testing,
  then INFOSEC route only if findings surface.
- Exchange 02 terminal report classified **acceptance-PASS**. Claimed
  evidence: re-gate held; one `test-focus` over the two gap-owner files →
  19 passed / 0 failed in 8.19s; no added paths; no mutations.
  ORCHESTRATOR verification: `01_report_01.md` archived beside its prompt;
  all five gap-owner test ids plus three sibling union tests and three
  migration ids confirmed present in the named files; canonical checkout
  still clean at `91410fe…`. Combined with exchange 01 the authorized
  deterministic companion net at the shared SHA is COMPLETE (409/0 total).
  Precision notes from exchange 01 remain recorded, not reopened.
- Deterministic phase closed at Orchestrator level: acceptance evidence for
  the deterministic portion is satisfied; rendered Brave acceptance remains
  Cooperator-owned. Next owner step sequenced: quiet NUC allowlist gate
  (structural booleans + hidden-input membership check; values never
  printed), one paste-safe block, failure routes to a separate
  EnvironmentFile/restart task per standing agreement.
- Allowlist gate attempt 1 classified **INCONCLUSIVE (probe-permission
  limit, not a product finding)**: `/etc/framenest/framenest.env` is not
  user-readable, so the unprivileged block correctly emitted fail-closed
  booleans and no values. Evidence-probe rule applied: diagnostic-method
  failure, distinct from the system fact. Privileged re-run block issued
  (Cooperator `sudo -v`/`-n true` inside the block, same quiet validation,
  `sudo -K` plus release marker at end). Standing disposition unchanged:
  a structural FAIL or `membership=no` on the privileged run routes to a
  separate EnvironmentFile/restart task before any rendered testing.
- Allowlist gate attempt 2 (privileged re-run) classified **PASS**:
  `json_valid=True entry_count=1 format_valid=true unique=true`,
  `MEMBERSHIP: yes`, privilege lifecycle clean (`timestamp-ok` → `released`).
  Shared-SHA precondition and allowlist precondition are both satisfied;
  no EnvironmentFile/restart task needed. Cooperator released into the
  rendered Brave pass (checklist items 1–10); results pending.
- Rendered pass, early results: Connect/Save-submit/badge plumbing works —
  extension mutations passed the allowlist+header gate end-to-end on live
  NUC (positive security acceptance signal). Item 4 classified
  **FAIL (acquisition)**: live X extraction returns generic
  `X_EXTRACTOR_FAILED` ~1.7 s after submit (`can_retry=true`,
  zero assets); second save accepted then likewise absent from history.
  Orchestrator analysis against source: companion history lists media rows,
  which the X pipeline creates only after successful extraction/catalog
  handoff, so a failed save having no history row is expected semantics;
  failure surface is the web-shell X cockpit (`/api/x/requests`). Badge=1
  consistent with a pre-existing analyzed unopened item. NOT classified as
  an INFOSEC finding (no trust-boundary misbehavior observed). Next owner
  diagnostics requested: cockpit inspection, one bounded Retry attempt,
  analyzed-row click (item 5), remaining checklist items. Remediation will
  route through a bounded Worker slice after triage; no improvisation.
- Rendered pass continued. One save later succeeded end-to-end (media row
  visible under All; Details shows “No successful analysis yet” because
  auto-analysis is default-off per ADR-0066). Cooperator expectations
  recorded for triage: (a) DEFECT CANDIDATE — newest own-save not on top in
  All ordering / newest-accent applied to a non-newest row; (b) DEFECT
  CANDIDATE — clicking a meme in All opens a small native popup instead of
  the hosted Details iframe path; (c) PRODUCT DECISION candidates — accent
  only after analysis passes, failed-save tombstone visibility in companion
  history (retry currently cockpit-only), admin auto-analysis enablement via
  `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED` EnvironmentFile operation
  (owner-owned NUC ops task, separate bounded grant). Badge=1 consistent;
  badge decrement on open remains implemented and pending an analyzed item.
- **Cooperator product amendments recorded (2026-08-26, chat evidence,
  supersede prior companion-history expectations).** R1: any own-row click
  must open the hosted iframe popup (same path as the compact five); the
  small native popup is a defect to fix. In that popup admin may Edit;
  “Analyze by AI” stays out of the companion popup (analysis belongs to
  administration surfaces / future model switches). R2: admin history shows
  only ANALYZED items — newly analyzed appears top-most under the title bar
  with newest accent, badge +1; single click = open → accent clears and
  badge −1; admin must not be blocked or gated in this workflow. Ordinary
  user history shows ALL their own saves immediately, plain (no accent);
  supersedes prior hidden-history (403) behavior for own-saves. Badge
  remains an admin-side analyzed-unopened counter. R3: ordering/accent
  defects fold into R2 semantics rather than standalone bugfix. R4:
  extension Settings gains an admin-only “Administration” section containing
  an automatic-media-analysis checkbox backed by a runtime-writable server
  setting (replacing the long helper copy under FrameNest origin); new
  admin-gated server mutation surface → scoped as its own bounded slice
  after the R1–R3 history whole. Standing security boundaries (allowlist,
  four mutation routes, publication sole-writer, loopback/Tailscale)
  interpreted as unaffected; flagged to Cooperator for correction if not
  intended. Open items before planning: rendered checklist 6–10 results and
  the X_EXTRACTOR_FAILED retry outcome.
- Planner session 02/exchange 01 issued (fresh, Plan Mode ON, High). Plan
  archived by ORCHESTRATOR as `02_report_00.md`: ADR-0076 successor; admin
  inbox analyzed-only (global pool); new requester-private
  `GET /api/companion/own-history`; click-path root cause identified
  (`historyClickKind` → `pending_overlay` → `openReviewOverlay`); hosted-mode
  hides Analyze-by-AI + Load-AI-suggestion; no migration; full test matrix;
  publication → NUC refresh → re-render sequencing. Open-question defaults
  accepted by silence unless overridden.
- Rendered checklist closed: 6 superseded by R2 design (no pending visible
  to admin); 7 PASS with one transient `composer_unbound` cold-start before
  X refresh (source: `extension/ui/sidebar.js` attach result handler; parked
  as auto-rebind polish observation); 8 PASS; 9 PASS; 10 superseded.
- **R3 amended to R3′ (Cooperator, chat evidence):** ordinary user keeps ALL
  own saves in history AND gets badge + accent only on items that pass
  analysis (unopened lifecycle applies to ordinary own items; pending stay
  plain). Deep implication recorded: opened/unopened state must become
  per-identity (Alice≠Bob≠admin), likely additive migration 0034 extending
  the 0031 open-state mechanism; capability gate for own-item `opened` POST
  must widen narrowly under the same four-route policy.
- Planner continuation session 02/exchange 02 issued to the SAME healthy
  session (`02_planning_01.md`): fold R3′ into the full updated plan
  (per-identity persistence design, badge sources, narrow opened gate,
  updated state machines/tests/ADR outline, migration 0034 if required).
  Cooperator declared accelerated-trust mode (“improvization”): ceremony
  compressed, hard gates unchanged (publication grant and NUC refresh remain
  explicit owner approvals; Workers remain bounded).
- Planner exchange 02 returned PASS (archived `02_report_01.md`): **no
  migration 0034 required** — 0031 `companion_review_open_states` already
  has PK `(actor_login_key, media_id)` (ORCHESTRATOR-verified lines 61–66);
  isolation already proven by `test_actor_opened_rows_are_isolated`;
  opened stays the same fourth mutation route with ingress capability
  switched to `x.request` plus API ownership gate (admin-any / ordinary-
  owner, uniform 404); own-history carries own-analyzed `unopened_count`
  (explicit warning not to reuse the global subquery); badge refresh per
  audience; ADR-0076 supersedes ADR-0073 + the opened-admin-only part of
  ADR-0067 without body edits; Alice/Bob/admin triple test matrix.
- Implementation session 03/exchange 01 issued (`03_implementation_00.md`):
  fresh Worker, isolated worktree at `91410fe…`, High reasoning, exact
  allowlist (extension sidebar/service worker, review API, ingress,
  application, repository, app.js hosted-hide, X_COMPANION.md history
  section, new ADR-0076 + index, surgical SPEC/PRODUCT/README touches,
  nine named test files), one local commit, no push; minimum-evidence
  matrix defined. Delivery: fresh Cursor Worker session, Plan Mode off,
  High.

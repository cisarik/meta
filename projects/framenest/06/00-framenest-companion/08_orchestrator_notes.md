# Orchestrator notes — era 06 / framenest-companion-brave-testing-resume

Ledger storage version: 1
Maintained by: Agent Orchestrator. Append-only narrative; superseded facts move to Git/history.

## 2026-08-26 — fresh Orchestrator restoration (read-only)

- Era opened from `06/00-framenest-companion/00_handout.md`. Required reading
  completed before any Worker prompt: AGENTS.md; pinned `.ap/AP.md`,
  `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md`, `AP_WORKER.md`;
  `docs/WORKER_EXECUTION_CONTRACT.md`; candidate ADR-0076; ADR-0073 and
  ADR-0067 bodies (read-only); `SECURITY.md` companion paragraphs; 
  `docs/X_COMPANION.md` on both `91410fe…` and `977a7af…`; archived plan
  `05/00/02_report_01.md`; implementation claim `05/00/03_report_01.md`;
  `05/00/08_orchestrator_notes.md`.
- Direct re-verification of handout §2 (this Orchestrator, not inherited):

  | Fact | Observed |
  |---|---|
  | Canonical checkout | `/home/agile/Projects/framenest` |
  | Canonical branch | `feat/x-meme-browser-companion` |
  | Canonical HEAD | `91410fe063d9907304cff4550f61d403880a2eeb` |
  | Canonical index | tracked-clean (`git status --porcelain=v1` empty) |
  | Public `refs/heads/main` | same 40-hex (credential-free `git ls-remote`) |
  | Tracking curiosity | ahead 26 of `origin/feat/x-meme-browser-companion`; not a side quest |
  | AP gitlink + `.ap` HEAD | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
  | Public `cisarik/ap` `main` | same pin |
  | Schema head (canonical + candidate versions dirs) | `0030`–`0033` only; no `0034_*` |
  | Candidate worktree | `…/framenest-companion-brave-testing-resume-w3` clean |
  | Candidate branch | `feat/companion-history-r1-r3prime` (no upstream) |
  | Candidate HEAD | `977a7af80afed16745adb0ef8e939555e5e21cce` |
  | Candidate parent | `91410fe…`; ancestor check yes |
  | Candidate subject | `feat: hosted companion history with analyzed inbox and ordinary own-history` |
  | Candidate diffstat | 21 files, +1128 / −177 |
  | Live NUC SHA | **not re-read**; last attested earlier equal to `91410fe…` |

- Upgrade ledger (`docs/AP_UPGRADE_OBSERVATIONS.md`): structurally valid
  header; one active entry
  `consumer-declared-execution-and-capability-route-binding`, state
  `untriaged`, authority `non-authorizing`. Stored
  `Last revalidated against: 5abb2adf…` is older than current pin.
  Operational revalidation against current repository + public AP `main`
  (`9c5cc44…`, equal to the pin): observation still holds — AGENTS.md and
  `WORKER_EXECUTION_CONTRACT.md` still bind Cursor Workers to `./.ap/ap`
  `project check` / `exec`; `ap.project.conf` still uses relative
  `.venv/bin/python`; isolated-worktree launch-path miss remains a known
  topology limitation. File SHA not updated (no FrameNest mutation
  authority). Entry remains non-authorizing. Not an AP upgrade task.
- Restoration classification: **PARTIAL**. Useful continuity verified.
  Material uncertainty: `03_report_01.md` is an unverified Worker claim;
  NUC active SHA not re-read this session; public `SECURITY.md` still lacks
  ADR-0076 / own-history sentences (candidate also did not edit
  `SECURITY.md`).
- Not BLOCKED: canonical clean at public main; no live Worker authority;
  candidate worktree clean; no in-flight mutation on canonical checkout.
- Stage 2: already selected by Michal (close this logical whole). First
  Worker: independent acceptance session 04 / exchange 01. Prompt staged
  `04_acceptance_00.md`. Report destination `04_report_00.md` (meta
  exchange-01 `_00` grammar; handout’s `04_report_01.md` spelling was not
  followed so session 04 / exchange 01 is not confused with exchange 02).
- 0031 PK `(actor_login_key, media_id)` re-read at
  `0031_companion_review_inbox.py` lines 65–68 on the canonical tree.
- Canonical `docs/X_COMPANION.md` still has “fade by position” and
  ordinary-403-hides-history. Candidate history section is rewritten to
  R1–R3′. ADR-0076 exists only on the candidate.
- No product code implemented. No publication, NUC, R4, or VPS opened.

## 2026-08-26 — Worker 04 independent acceptance

- Terminal report `04_report_00.md` claimed `acceptance-PASS` of
  `977a7af80afed16745adb0ef8e939555e5e21cce`. Session 03 did not accept.
  Authority expired at that report.
- ORCHESTRATOR verification (objects, not a second test run): canonical still
  `91410fe…` tracked-clean; public `main` still `91410fe…`; w4 detached at
  `977a7af…` parent `91410fe…`; w3 untouched at `977a7af…`; diff path set 21
  files matching the report; forbidden-path diffs empty; no `0034_*`; tree
  `ed5959edf783f9d9bb972107dfba7b18bd1943ea`; `rev-list --count` parent→candidate
  equals 1. Trust-boundary tests exist with claimed codes (`MEDIA_NOT_FOUND`,
  `CAPABILITY_DENIED`, empty-allowlist GET own-history 200, four flagged
  mutations, opened capability `x.request`, `_own_analyzed_latest`,
  `openedIndex > hostedIndex`). Named deviations exist as classified
  (getattr / require_owner-only-when-true / hardcoded GET path).
- Worker-observed 151 Python / 107 Node and w4 `framenest.__file__` provenance
  are classified as Worker observation consistent with objects. Isolated-worktree
  `.venv` miss remains environment limitation / upgrade-ledger theme.
- `SECURITY.md` omission: **publication-flag**, not a blocking present-tense
  contradiction. Closure gate 2 living docs are on the candidate
  (`X_COMPANION.md`, SPEC/PRODUCT/README, ADR-0076 + index). Do not create
  `HEAD'` for SECURITY.md inside this publication.
- Disposition: **accept** `977a7af…`. Next surface is a separate Cooperator
  publication grant of that exact SHA to public `main`. Not NUC. Not R4.
  Not closure.

## 2026-08-26 — Worker 05 publication

- Terminal report `05_report_00.md` claimed `publication-PASS` of
  `977a7af80afed16745adb0ef8e939555e5e21cce`. Authority expired at that report.
- ORCHESTRATOR independent public-ref proof (credential-free `ls-remote`):
  `refs/heads/main` = `977a7af80afed16745adb0ef8e939555e5e21cce`. Canonical
  HEAD, tree `ed5959ed…`, and subject match. Branch
  `feat/x-meme-browser-companion`, tracked-clean. AP pin `9c5cc44…` =
  public `cisarik/ap` `main`. ADR-0076 present on the published tree. w3/w4
  still at `977a7af…`.
- Disposition: **publication-PASS**. Living docs for R1–R3′ are on public
  `main`. Closure gates remaining: NUC `framenest-release` to this SHA, then
  Cooperator numbered rendered re-test. Not R4. Not VPS. Not closure.
- Next: Cooperator-run read-only `status` then `check --release 977a7af…`.
  Deploy is a later separate grant after those results. Same-schema `0033`
  expected; no migration-required continuation expected.

## 2026-08-26 — Cooperator NUC refresh (owner-run)

- Cooperator attested manual push/deploy. Independent `ls-remote` still
  `977a7af…` on public `main`; canonical HEAD still that SHA, tracked-clean.
- Owner terminal: standing operator wrapper invoked `framenest-release`
  `status` → `check --release 977a7af…` → `deploy --yes` → post `status`.
  Pre-deploy live release was `91410fe…` / schema `0033` / service active /
  backup `ready`. Check named public main `977a7af…` and AP pin `9c5cc44…`.
  Post-deploy: `active_release` `977a7af…`, `service_active: active`,
  `database_revision: 0033`, `backup_restore_readiness: ready`,
  same-schema cutover complete. Classified **deployment-PASS**
  (Cooperator-observed wrapper transcript; not a Worker grant). Host,
  identity, fingerprint, and private-network values from that transcript
  are not copied here.
- A later paste of the MacBook `framenest-release` block inside an NUC
  login failed as **operator-path mismatch** (wrong host / missing local
  checkout). Not a product defect and not a failed cutover.
- Remaining closure gate: numbered rendered R1–R3′ re-test after reload of
  unpacked Brave from the SHA the NUC serves. Not R4. Not VPS. Not closure.

## 2026-08-26 — Cooperator numbered re-test

Cooperator scores (rendered, NUC on `977a7af…`):

| Item | Score | Classification |
|---|---|---|
| 1–8 | PASS | R1/R2/R3′ listing as specified |
| 9 | FAIL | R3′ ordinary unopened/badge after analysis of an own item — **defect candidate**, not closed |
| 10 | PASS | hosted Details; Analyze hidden; Edit hidden for ordinary |
| 11–12 | NOT TESTED | Alice/Bob isolation and inbox 403 probe — remainder, not a close blocker unless upgraded |
| 13–16 | PASS | movies / disconnect / parked composer_unbound / expected failed-save |

- Hosted click-into-iframe Details: Cooperator-accepted (item 3/4/10).
- Edit modal “AI suggestion / View details” is **not** an R1–R3′ remainder.
  R1 hid Analyze by AI and Load AI suggestion in **hosted Details**; hosted
  Edit currently also hides Load (`companionWebHosted()`), leaving read-only
  View details. Cooperator amendment: per-field preview + ✅ apply, model
  dropdown, Load above Title — **new product whole**, not a correction of
  `977a7af…`, not R4.
- Related observed defect on admin Analyze then Save: suggestion not shown
  after Analyze; Save then wrote the full suggestion into all inputs and
  persisted. Aligns with current bulk apply / hide-Load-in-hosted, not with
  the requested per-field contract.
- Logical whole **not-closed**. Item 9 FAIL blocks UX PASS. Edit/AI apply UX
  is a changed objective → new kebab after this whole (or after a bounded
  item-9 diagnostic), unless Michal explicitly waives item 9.

## 2026-08-26 — Cooperator selected route 1

- Diagnose item 9 first; possible one bounded correction afterwards; then
  close this kebab; Edit/AI per-field apply is the **next** whole. R4 still
  not in this whole.
- Worker 06 / exchange 01 staged: `06_diagnostic_00.md` (Fresh Evidence
  Probe, read-only, SHA `977a7af…`). No correction authority in that
  prompt.

## 2026-08-26 — Worker 06 item-9 diagnostic

- `06_report_00.md` PASS (diagnostic). ORCHESTRATOR accepts **H3**:
  `PreviewImportedMediaSuggestion` is non-persistent; Analyze by AI /
  Gallery 🧠 never `record_analyzed`; companion unopened cannot move.
  ADR-0067 §5 / ADR-0076 join unimplemented on that path. H5 listing bug
  refuted as primary. H1 fixture secondary and insufficient alone.
- Next: bounded correction session 07 — persist generic analyzed run from
  successful imported preview, no second provider call, no Edit/AI apply,
  no R4. Then independent acceptance of that commit. Canonical stays
  `977a7af…` until a later publication grant of `HEAD'`.

## 2026-08-26 — Worker 07 item-9 join correction

- `07_report_00.md` implementation-PASS (claim). Independent object check:
  w7 detached `fb59c42a8e3a32d9476581beeabba0eb9c04109a`, parent
  `977a7af…`, one commit, 8 files, AP pin unchanged. Canonical, public
  `main`, w3, and w4 still `977a7af…`. Schema head still `0033`.
- Persist design confirmed in tree: after one `provider.suggest`,
  `PersistImportedPreviewAnalysis` does `create_manual_pending` →
  `claim_pending` → `record_analyzed`; movie skip; analyzing skip; no
  canonical metadata write; library-scan preview unchanged. Preview route
  remains `analysis.run`. Ordinary still lacks that capability.
- Classified **implementation-PASS**, not acceptance. Next: session 08
  independent acceptance of `fb59c42…` from a fresh worktree (not w7).
  Prompt: `08_acceptance_00.md`. Publication of `HEAD'` remains a later
  Cooperator grant.

## 2026-08-26 — Worker 08 item-9 acceptance PARTIAL

- `08_report_00.md` PARTIAL. Fresh w8 of `fb59c42…`; independence OK;
  provenance under w8 `src/`. Matrix: 2 failed, 203 passed. Canonical and
  public `main` still `977a7af…`.
- Object check of the two reds: owning
  `test_imported_preview_joins_inbox_and_own_history` POSTs preview under
  `tailscale_uds` with `_serve_headers` only (no Origin /
  `X-FrameNest-Request`) → 403 `MUTATION_ORIGIN_FORBIDDEN` before join.
  `_FakeRepository.create_manual_pending` reuses one hardcoded id so
  `first.id != second.id` cannot hold. Not a demonstrated second
  `provider.suggest`, fifth mutation, 0034, or ordinary analysis-run write.
- Production DI still injects the join (inspection). Unit persist path
  passed. Session 07 claim that those two tests passed is **not
  reproduced**. Do **not** accept or publish `fb59c42…`.
- Second bounded correction authorized: **test-only**, new independent
  evidence (inverted tests), not a second automatic correction of H3.
  Prompt: `09_correction_00.md`. Then independent re-acceptance.

## 2026-08-26 — Worker 09 test-only correction

- `09_report_00.md` implementation-PASS (claim). Object check: w9 detached
  `2aead540ee39a81a96425902f85e9b9a34f0d690`, parent `fb59c42…`, exactly
  two test files, no `src/` in the delta. Canonical and public `main`
  still `977a7af…`. w7/w8 still `fb59c42…`.
- Owning HTTP join POSTs now `_mutation_headers(ADMIN_LOGIN)` /
  `EXTERNAL_ORIGIN`. Fake `create_manual_pending` emits distinct ids after
  the first serial. Range vs `977a7af…` remains the original eight paths
  (persist + tests).
- Classified **implementation-PASS**, not acceptance. Next: session 10
  scoped independent re-acceptance of `2aead54…` from a fresh worktree
  (not w9). Prompt: `10_acceptance_00.md`. If the same two tests still
  fail, escalate rather than a third automatic correction.

## 2026-08-26 — Worker 10 item-9 re-acceptance PASS

- `10_report_00.md` acceptance-PASS. Fresh w10 of `2aead54…`; independence
  OK; provenance under w10 `src/`. Matrix **205 passed, 0 failed** (session
  08 had the same 205 with two red). Canonical and public `main` still
  `977a7af…`. Tree `0900818f…`. Range vs main: two commits, eight paths;
  test-only delta vs `fb59c42…` is the two test files.
- Object check: ancestor of `977a7af…`, count 2, DI still injects
  `PersistImportedPreviewAnalysis`, four `companion_mutation`, no Alembic
  `0034`. Previously inverted owning HTTP join and fake-id supersession
  tests are green on this SHA.
- ORCHESTRATOR accepts `2aead540ee39a81a96425902f85e9b9a34f0d690`.
  Logical whole not-closed. Publication is a separate Cooperator grant.
  Prompt: `11_publication_00.md`. After public main equals that SHA:
  routine NUC `framenest-release`, then rendered re-test of **item 9**.
  Not R4. Not Edit/AI apply. Not VPS.

## 2026-08-26 — Worker 11 publication PASS

- `11_report_00.md` publication-PASS (claim). Independent
  `ls-remote https://github.com/cisarik/framenest.git refs/heads/main` =
  `2aead540ee39a81a96425902f85e9b9a34f0d690`. Canonical HEAD, tree
  `0900818f…`, and `.ap` pin `9c5cc44…` match. Branch
  `feat/x-meme-browser-companion`, tracked-clean. Fast-forward of two
  commits from `977a7af…`. No NUC in that session.
- Disposition: **publication-PASS**. Remaining: Cooperator read-only
  `framenest-release status` then `check --release 2aead54…`, then a
  **separate** deploy grant, then rendered item-9 re-test. Same-schema
  `0033` expected. Not R4. Not VPS. Not closure.

## 2026-08-26 — Cooperator NUC refresh to 2aead54 (owner-run)

- Cooperator ran standing wrapper `~/nuc_push.fish`. Independent
  `ls-remote` still `2aead54…` on public `main`; canonical HEAD still that
  SHA, tracked-clean. No Worker.
- Pre: live NUC `977a7af…` / schema `0033` / service active / backup
  `ready`. Check named public main `2aead54…` and AP pin `9c5cc44…`.
  Post: `active_release` `2aead54…`, `service_active: active`,
  `database_revision: 0033`, `backup_restore_readiness: ready`,
  same-schema cutover complete. Classified **deployment-PASS**
  (Cooperator-observed wrapper transcript). Host, identity, fingerprint,
  and private-network values are not copied here.
- Bare `./deploy/ubuntu/framenest-release` without the wrapper’s transport
  env sanitizes to `command failed`. Operator-path mismatch, not a failed
  cutover. Do not paste the MacBook block inside an NUC SSH login.
- Remaining: rendered re-test of **item 9** after reload of unpacked Brave
  from the SHA the NUC serves. Items 1–8 already PASS on `977a7af…`. Not
  R4. Not VPS. Not closure.

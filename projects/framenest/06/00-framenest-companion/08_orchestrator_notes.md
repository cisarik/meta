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

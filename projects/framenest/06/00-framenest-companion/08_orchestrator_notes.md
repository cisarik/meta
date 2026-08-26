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

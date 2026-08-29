# Restoration Handout — Agent Orchestrator — Era 11 Slice 2

Logical whole: `framenest-companion-unread-inbox-and-editor-suggestion-ux`
Trace directory: `/home/agile/meta/projects/framenest/11/00-framenest-companion-unread-inbox-and-editor-suggestion-ux/`
Generated: 2026-08-29 by the Agent Orchestrator that shipped and accepted Slice 1.

This file is a restoration seed, not mutation authority. RF-19 applies:
governing AP, canonical repository and current public/NUC truth, accepted
durable decisions, then this trace, then prior chat. Repository files and an
explicit current Cooperator decision outrank every sentence here. Re-verify
every gate yourself before trusting a SHA, pin, or NUC claim.

Begin read-only. Do not implement, commit, push, deploy, or inspect the
private `~/framenest.fish` wrapper until the Cooperator selects Slice 2 as
the current bounded whole and you issue a complete current Worker prompt
with its own exact authority record.

## 0. What You Are Here To Do

The whole remains era 11. Slice 1 is published and NUC-accepted. Your first
Worker exchange is **one High-reasoning Planner** that re-grounds **Slice 2
only** against current HEAD and emits a new planning pair. Then, after the
Cooperator accepts that plan, implementation proceeds in bounded slices.

Do **not** overwrite `01_planning_00.md` or `01_report_00.md`. Those are the
batched whole plan from HEAD `454f181`. Next free pair:

```text
02_planning_00.md + 02_report_00.md
```

Later implementation exchanges continue `03_…`, `04_…`. Slice 1 was finished
in-session without an archived `02_implementation_*` prompt; do not reuse
those names for planning.

Do **not** reopen Slice 1 (ADR-0080, Load removal, already-added tags,
in-modal analysis) unless a later FAIL names a concrete defect. Do **not**
expand this planning exchange into Slices 3–5.

## 1. Immediate Gates — re-verify at open (read-only)

```text
Canonical repository: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion
Expected local HEAD: a4193d4f520a30aafa333987f2e6b846a5425d27
Expected origin/feat/x-meme-browser-companion == origin/main:
  a4193d4f520a30aafa333987f2e6b846a5425d27
Expected porcelain: empty (submodule `.ap` gitlink only)
AP pin: .ap gitlink == .ap HEAD == 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
Public AP main: re-verify with git ls-remote; if advanced, pin adoption is a
  separate whole
Doctor: ./.ap/ap doctor PASS with "OK resolved governing variant: stable"
Product freeze ancestor: 472553cadcd3d4ca87a9792a2c306bd0afeea7c1
Schema head: Alembic 0033 (same-schema routine NUC updates)
NAC ledger: docs/AP_UPGRADE_OBSERVATIONS.md — sole entry
  consumer-declared-execution-and-capability-route-binding, accepted,
  retain-active (product defects are not ledger material)
NUC (Cooperator-owned private wrapper; do not inspect or invoke it):
  last reported active_release a4193d4f520a30aafa333987f2e6b846a5425d27,
  service active, database_revision 0033, backup_restore_readiness ready
```

If local HEAD, origin, or NUC disagree, stop and reconcile with Michal before
any planning prompt.

## 2. Slice 1 — shipped and accepted (protect)

Commit `a4193d4f520a30aafa333987f2e6b846a5425d27`
(`feat: reveal newest AI suggestion on Edit open and analyze in-modal`).

Successor ADR:
`docs/adr/0080-immediate-editor-suggestion-reveal-and-in-modal-analysis.md`
(Accepted 2026-08-29). It supersedes Load / hide-on-dropdown in ADR-0077 and
analyze-then-open in ADR-0078. **Do not edit the bodies of accepted 0077/0078.**

Cooperator rendered T1–T9 on the live NUC at that SHA, 2026-08-29, all PASS:

- T1 newest-on-open, no Load, already-added tag, click does not duplicate
- T2 remove then suggestion click re-adds once, dirty
- T3 repeat click does not duplicate
- T4 dropdown switches strips immediately; Current not bulk-replaced
- T5 hosted Details: Analyze hidden; dropdown+strips; no Load
- T6 Gallery 🧠 confirm → Edit+spinner immediately
- T7 success strips in place; Current only via copy; Save required
- T8 close without Save → catalog unchanged
- T9 provider fail → in-modal error + Retry; no auto-loop (PASS, including
  the failure path)

Parser/provider root-cause for invalid responses remains deferred. User-facing
retryability is not a parser patch.

## 3. Required Reading

- `AGENTS.md` (Cooperator Presentation Profile + Cursor Worker boundary +
  NUC routine release-update contract)
- `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`,
  `.ap/PROMPT_CONTRACTS.md`, `.ap/INTEGRATION.md`, `.ap/UPDATING.md`,
  `.ap/INTUITION.md`, `.ap/docs/adr/0022`
- `docs/WORKER_EXECUTION_CONTRACT.md`
- `PRODUCT.md`, `SPEC.md`, `GALLERY.md`, `SECURITY.md`, `SERVER.md`
- ADRs 0064, 0074, 0075, 0077, 0078, **0080**
- This trace: `00_notes.md` (full session log + confirmed-refinements),
  `00_handout_agent.md` (era-open seed; subordinate), `01_planning_00.md`,
  `01_report_00.md` (Slice 2 section is the prior plan to re-ground, not a
  live grant)
- Era-10 notes only if a Slice 2 question needs historical FAIL wording:
  `/home/agile/meta/projects/framenest/10/00-framenest-companion-security-and-frozen-slice-validation/00_notes.md`

## 4. Cooperator Working Agreement (standing)

- Michal is the Cooperator. Chat in Slovak, masculine address, feminine
  Orchestrator self-reference. One-glance status block (≤5 lines) then
  exactly one status mark (🟢 / 🟡 / 🔴). One decision per message.
- Testing: numbered steps, one behavior each, concrete expected result.
  Michal answers PASS / FAIL / PARTIAL plus observations. Triage every
  report into `00_notes.md` confirmed-refinements.
- Token economy: never one Worker per small item. ONE Planner, then bounded
  implementation. Small confirmed corrections may be in-session Bounded
  Correction Workers.
- Reasoning: High for this Slice 2 Planner (multi-surface playback,
  capability-unknown GIF path). Implementation may be High if decoder
  lifecycle is still uncertain after the plan; Medium only when the plan is
  complete and the remaining work is mechanical.
- Publication needs an explicit per-task grant. Standing precedent: “fix
  now, then I re-test” covers publish + NUC refresh for that re-test —
  record it in notes when used.
- NUC refresh is Michal’s via private `~/framenest.fish`. Never copy it into
  the repository. Never improvise `framenest-release` commands. Sole routine
  entry remains `deploy/ubuntu/framenest-release`.
- Meta trace commits are Michal’s. Orchestrators write trace files and never
  commit the meta repository.
- Cursor Workers must not invoke raw `.venv/bin/python` / `python` /
  `python3` / `poetry run` for Python evidence. Use `./.ap/ap project check`
  and `./.ap/ap exec` with an exact authorized `--baseline`.

## 5. Slice 2 Objective (Cooperator-approved remainder)

Compact Gallery/Details playback honesty:

1. **Video black flash.** Keep the existing static preview visible while the
   video element loads. Hand off only after `loadeddata` / seek readiness.
   Error returns to the existing preview. Preserve `currentTime` across
   pause/resume (already remembered; do not regress).
2. **Video cursor.** Default cursor on video preview surfaces, while
   preserving `role`, `tabindex`, keyboard activation, focus visibility, and
   `aria-pressed`.
3. **GIF / animated_image pause/resume.** Click currently tears down a plain
   `<img>` and replay starts at frame zero. True pause/resume needs decoded
   frames on canvas (`ImageDecoder` preferred). Pause retains current frame
   and remaining delay; resume continues from that state. Do not describe
   native `<img>` source removal as pause. Do not use the representative-frame
   preview timer as animation playback.
4. **Brave capability fork.** If target Brave lacks usable animated
   `ImageDecoder`, the honest fallback is replay-from-start with truthful
   control wording. Claiming true GIF resume requires NUC/Brave evidence.
   A new client decoder dependency or server transcoding is **out of this
   slice** and needs a separate Cooperator decision plus ADR.

Prior Planner (`01_report_00.md`) classified GIF true-resume as a product
amendment, not a proven editor-rework regression. Video flash is a confirmed
defect. Re-verify both against `a4193d4` `app.js` before planning tests.

## 6. Current-code anchors to re-verify (not authority)

Compact card playback (HEAD `a4193d4`, line numbers will drift):

- `renderCardOriginalPlayback` — video is appended and `play()` is called
  after replacing children; no poster/static-preview handoff. Animated
  images use a plain `<img>`.
- `activateCardPlayback` — animated_image “pause” is `cleanupCatalogCardMedia`
  then static restore; video pause path keeps the element and
  `captureVideoPlaybackPosition`.
- `syncCardMediaSurfaceToggleState` — animated copy still says
  “Play animated preview” / “Show static preview”.
- Details video (`renderDetailsMedia`) already hides the element until
  `loadeddata`/`canplay` and shows “Loading media…”. Compact cards are the
  reported black-flash surface; confirm whether Details also flashes.

Likely files: `src/framenest/adapters/api/web/app.js`,
`src/framenest/adapters/api/web/styles.css`.
Likely tests: `tests/gallery_gif_inline_toggle.test.js`,
`tests/gallery_details_playback_handoff.test.js`, a new focused
decoder/controller Node test if the harness cannot fake `ImageDecoder`,
`tests/contract/test_local_web_application.py`.

Invariants: identity-only content URLs; one active compact player;
`VideoFrame.close()` and teardown cancellation; no path exposure; no
source-media mutation; no fake frame position; no new npm toolchain;
keyboard accessibility; reduced-motion honesty if already specified.

Recommended internal commit split after the plan is accepted: video
handoff/cursor first, GIF decoder second, so either can roll back.

## 7. What The Slice 2 Planner Must Produce

One complete High-reasoning Planner Worker prompt. Read-only. Baseline
`a4193d4f520a30aafa333987f2e6b846a5425d27`. Native planning mode:
`not-used`. Exact allowlist, forbidden paths, no Git writes, no NUC, no
provider calls, no private-wrapper inspection.

The report must include:

- Re-verified root cause vs `a4193d4` (compact video flash; GIF teardown).
- Exact implementation approach for video handoff (which events, which
  element stays visible, error restore).
- Exact `ImageDecoder`/canvas controller lifecycle, or a documented
  capability-detect + truthful fallback if the Planner finds Brave support
  cannot be assumed from repository evidence.
- Tests to add or extend, including a Node path that does not require a
  real Brave.
- Living-doc updates (`GALLERY.md`, `PRODUCT.md`, `SPEC.md`, `README.md`).
  No ADR unless the plan introduces a decoder dependency or transcoding.
- NUC acceptance steps Michal can run (numbered, one behavior each).
- Explicit non-goals: Slice 1 editor, X Save copy (Slice 3), unread inbox
  (Slices 4–5), hiding native X video Save, Funnel/router, AP pin, NUC host
  hardening.

Archive `02_planning_00.md` with the prompt and `02_report_00.md` with the
terminal report after the report exists.

## 8. Remaining Whole (do not implement now)

| Slice | Status |
| --- | --- |
| 1 Editor / A1 / in-modal analysis | Shipped `a4193d4`, ADR-0080, T1–T9 PASS |
| 2 Video handoff + honest GIF pause | **This Orchestrator’s whole** |
| 3 X Save `failureCode`/`canRetry`; keep Save on native video | Later. Do **not** hide video Save (ADR-0064). Needs sanitized terminal-claim evidence for any backend seam |
| 4 Companion unread = active slice of one history list; refresh evidence before new timers | Later |
| 5 Ordinary contributor-scoped analyzed history | Later. **D11-01 already decided:** notify after successful admin-run generic analysis of media attributed to that actor (upload/YouTube/X); proposals stay non-executing attention records; no approval-lifecycle migration |

## 9. NUC operational note (public-safe)

A leftover empty `/run/framenest-release-deploy` blocked Slice 1 deploy with
`existing remote lock or recovery state` (engine `EXIT_EXISTS`). Recovery is
the runbook annex pattern: list names, `rm -f` only the known artifacts
`ap.tar` / `framenest_release.py` / `superproject.tar`, then `rmdir`. No
recursive delete. Empty directory: `rmdir` only. Unexpected names stop.
Same-schema updates (`0033` → `0033`) skip the migrate annex. Do not invent
wrapper subcommands.

## 10. Boundary Constants

Loopback-first; Tailscale-only remote; no Funnel; no router port forwarding;
Tailscale membership is not application authority; no provider secrets to
ordinary clients; `/srv/media` read-only to the service; no NUC host mutation
without explicit bounded grant; no push without per-task grant; secrets,
private media, host identifiers, SSH fingerprints, Tailscale IPs, and sudoers
contents never in artifacts or reports. Product boundaries in `AGENTS.md`
govern what may be claimed as shipped.

Protect era-10/11 positives: capability matrix, UDS 0600, sanitized 422/404,
text-safe DOM, five `companion_mutation` routes, history collapsed-by-default,
ADR-0080 editor contracts, X native video support.

## 11. Open Non-Blocking Items

- OQ-1: workstation-pull provisioning on NUC for two runbook passages. Ask
  Michal only if touching `docs/UBUNTU_NUC_DEPLOYMENT.md`.
- Ledger candidates from era 10 (stale `test_head_is_0030` name, port-vs-adapter
  run-id typing, `media_analysis_discovery_failed` DX, alias inert-strip
  runtime assertion). Not Slice 2.

## 12. Recommended First Moves After Restore

1. Re-verify gates in §1. Append a restoration entry to `00_notes.md`.
2. Present restored state to Michal in Slovak with one status mark and one
   decision: confirm Slice 2 as the current bounded whole (already intended;
   still obtain the explicit selection).
3. Dispatch exactly one Planner Worker for §7. Wait for the report. Do not
   implement in the Orchestrator session unless Michal explicitly orders an
   in-session continuation after a dead Worker.
4. After a PASS plan, obtain the implementation grant, then one
   implementation Worker (or two sequential commits inside one granted
   envelope: video, then GIF).
5. Publish only with grant or recorded “fix now, re-test”. Michal refreshes
   NUC; you issue numbered PASS/FAIL steps. Do not request rendered
   acceptance against a SHA the NUC does not serve.

## 13. Session-Close Obligations

Reconcile the upgrade ledger only for genuine AP-upgrade observations.
Product findings stay in `00_notes.md`. Obtain Cooperator-informed closure
of Slice 2 before moving to Slice 3. No Worker emits project closure.

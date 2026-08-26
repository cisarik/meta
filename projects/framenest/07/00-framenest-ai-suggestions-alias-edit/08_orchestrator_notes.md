# Orchestrator notes — era 07 / framenest-ai-suggestions-alias-edit-mvp

Ledger storage version: 1
Maintained by: Agent Orchestrator. Append-only narrative; superseded facts move to Git/history.

## 2026-08-26 — fresh Orchestrator restoration (read-only)

- Era opened from `07/00-framenest-ai-suggestions-alias-edit/00_handout.md`.
  Required reading completed before any Worker prompt: FrameNest `AGENTS.md`;
  pinned `.ap/AP.md`, `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md`,
  `AP_WORKER.md`; `docs/WORKER_EXECUTION_CONTRACT.md`; declared upgrade
  ledger `docs/AP_UPGRADE_OBSERVATIONS.md`.
- Direct re-verification of handout §2 (this Orchestrator, not inherited):

  | Fact | Observed |
  |---|---|
  | Canonical checkout | `/home/agile/Projects/framenest` |
  | Canonical branch | `feat/x-meme-browser-companion` |
  | Canonical HEAD | `2aead540ee39a81a96425902f85e9b9a34f0d690` |
  | Canonical tree | `0900818f57326017712c07686c49de61d534507f` |
  | Canonical index | tracked-clean (`git status --porcelain=v1` empty) |
  | Public `refs/heads/main` | same 40-hex (credential-free `git ls-remote`) |
  | Local log -2 | `fb59c42` persist-join; `2aead54` item-9 test uninvert |
  | Tracking curiosity | ahead 29 of `origin/feat/x-meme-browser-companion`; informational; not a side quest |
  | AP gitlink | `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` |
  | `.ap` HEAD | same pin, detached |
  | Public `cisarik/ap` `main` | same pin |
  | Schema versions dir | `0001`–`0033` only; Alembic head file `0033_media_analysis_proposals.py`; no `0034_*` migration. ADR-0034 is AP integration, not schema. |
  | Live NUC | **not re-read**; last Cooperator-attested `active_release` `2aead54…` / schema `0033` |
  | Isolated worktrees | leftover era-06 w3–w10 and older trees present; not deleted |

- Upgrade ledger (`docs/AP_UPGRADE_OBSERVATIONS.md`): structurally valid
  header (`Ledger storage version: 1`, target
  `upgrade https://github.com/cisarik/ap.git`). One active entry
  `consumer-declared-execution-and-capability-route-binding`, state
  `untriaged`, authority `non-authorizing`. Stored
  `Last revalidated against: 5abb2adf…` is older than current HEAD.
  Operational revalidation against current repository + public AP `main`
  (`9c5cc44…`, equal to the pin): observation still holds —
  `AGENTS.md` / `WORKER_EXECUTION_CONTRACT.md` still bind Cursor Workers to
  `./.ap/ap project check` / `exec`; `ap.project.conf` still uses relative
  `executable = .venv/bin/python`. Isolated-worktree `--root <worktree>`
  launch-path miss remains a known topology limitation. The failing exec
  was not re-run this session. File SHA not updated (no FrameNest mutation
  authority). Entry remains non-authorizing and **not this kebab**.
- Restoration classification: **PARTIAL**. Useful continuity verified.
  Material uncertainty belongs to the Planner: ordinary Edit Save → alias
  PUT vs canonical; Gallery/Details read stay canonical this whole (default
  write-only); suggestions dropdown sourced from existing
  `media_analysis_runs` without a second store; first-attempt “AI provider
  is not available” vs stale copy. NUC SHA not re-read this session.
- Not BLOCKED: no in-flight Worker authority; canonical is public main;
  no unpublished candidate.
- Stage 2: already selected by Michal (`framenest-ai-suggestions-alias-edit-mvp`).
  First Worker: Planner session 01 / exchange 01. Prompt staged
  `01_planning_00.md`. Report destination `01_report_00.md`.
- Closed predecessor `framenest-companion-brave-testing-resume` remains
  closed. R1–R3′ and item 9 PASS are not reopened. R4 and VPS stay out.
- No product code implemented. No publication, NUC, Git writes in FrameNest.

## 2026-08-26 — Planner session 01 / exchange 01 review

- Artifact: `01_report_00.md` exists. It is a Slovak Cursor Plan Mode
  document (YAML front matter, mermaid, archive-todo), **not** the
  contracted AP terminal report (`### Report for ORCHESTRATOR_CHAT`,
  coordinates, PASS/PARTIAL/BLOCKED, English). Planning authority expired
  at that delivery. This is **not** planning PASS under AP. Content is
  treated as a frozen planner artifact pending Cooperator approval plus
  one Orchestrator freeze (below). No Worker impersonation: the file was
  not rewritten.
- Gate claims in the artifact match this Orchestrator's restoration
  (HEAD `2aead54…`, tree `0900818f…`, AP pin `9c5cc44…`, Alembic `0033`).
- Repository-checked claims that hold:
  - Ordinary lacks Edit because Details ~443–444 and Gallery ~6029 gate
    on `metadata.canonical.write`; ordinary already has `alias.write`;
    alias GET/PUT exist.
  - `GET /api/media/{id}/automatic-analysis` is latest-only
    (`get_by_media_definition` → `_latest_run`).
  - `GET /api/companion/review-inbox/{media_id}` returns `suggestions[]`
    (generic analyzed history, movie 409, default limit 25 / max 100),
    capability `media.workflow.read`, **not** `companion_mutation`.
    Ordinary stays 403. Website Edit may GET it; must never POST apply.
  - `result_json` already carries title/description/tags/filename.
  - Bulk Load is `applyResolvedAiSuggestionToMetadataWorkspace` ~5494.
  - Analyze locks after `aiSuggestionApplied` (~6505–6517, ~7204).
  - Provider copy is `aiSuggestionErrorMessage` ~7285
    (`AI_PROVIDER_UNAVAILABLE`); library-scan ~10362 is a different path.
  - Essay “New AI analysis is available after confirmation.” is
    `renderMetadataAiPanel` ~6753–6755 when `aiCapability.available`.
  - Stale confirm: `metadataAiConfirmationContextIsCurrent` includes
    `aiCapabilityRevision`; mismatch returns without status (~7222).
  - Gallery 🧠 is `identityAllowsCardAiQuickAction` ∧ incomplete ∧ not
    movie; park as debt.
  - ADR-0076 still says Edit remains `metadata.canonical.write`.
- Named Orchestrator freeze **not** in the artifact as written:
  ordinary Edit **form load** must GET existing alias when non-empty,
  else seed from canonical. Artifact said Current always seeds from
  canonical GET, never alias — that would make re-open Edit ignore the
  overlay the user just saved. Gallery/Details **display** stay
  canonical. Awaiting Cooperator confirmation; then implementation
  Worker 02, not a second planning cycle.
- Implementation notes if accepted: dropdown GET `limit=100`; movie
  Edit keeps Identify, hides generic suggestions (inbox GET 409);
  isolated-worktree Python still canonical `--root` + pytest
  `--rootdir`/`pythonpath` deviation; no 0034; no fifth
  `companion_mutation`.
- No implementation issued. No FrameNest mutation.

## 2026-08-26 — Cooperator accepted the plan; Worker 02 issued

- Michal: „prijímam plán.“ Treated as acceptance of the frozen planner
  artifact plus the Orchestrator form-load freeze (ordinary Edit GET alias
  if non-empty, else canonical seed; Gallery/Details display stay
  canonical).
- Planning PASS is still not claimed (artifact lacked the AP report
  header). Product authority for implementation is this Cooperator
  acceptance + this grant, not a rewritten Worker 01 report.
- Implementation prompt staged `02_implementation_00.md`. Session 02 /
  exchange 01, `fresh-worker-session`, `Native planning mode: not-used`,
  isolated worktree, 1–3 local commits, no push. Independent acceptance
  remains a later fresh Worker.
- No FrameNest mutation in this Orchestrator turn.

## 2026-08-26 — Worker 02 implementation claim reviewed

- Claim `02_report_00.md`: `implementation-PASS` at
  `36ffdb197da9294fb1fbb06931f8169061a25c9b`. Planning authority already
  expired; this report expires session 02.
- Direct object verification (this Orchestrator):
  - Canonical still `2aead54…` tracked-clean, branch
    `feat/x-meme-browser-companion`.
  - w2 HEAD `36ffdb19…`, branch `feat/ai-suggestions-alias-edit-mvp`,
    tracked-clean, two commits on parent `2aead54…`
    (`6b957be` feat, `36ffdb1` docs/ADR). Ancestor check yes.
  - Diff path set **exactly 15** allowlisted files; no 0034; ADR-0062/0076/0023
    bodies untouched.
  - Code: `identityAllowsMetadataEdit`; alias GET then overlay; Save PUT
    alias vs metadata; inbox GET `limit=100`; Load reveals without bulk
    apply; Analyze → `presentInSessionSuggestion` and no longer hides
    Analyze; hosted hide via `identityAllowsAiSuggestionsChrome`;
    confirm-copy + stale-confirm message; ADR-0077 + index succession notes.
  - Gallery 🧠 still `handleAnalyzeCatalogCard` canonical PUT (parked).
  - Tests: not re-run here; independent acceptance must re-run.
- Implementation-PASS accepted as an Orchestrator-verified **claim of
  completeness against the grant**, not as independent acceptance and not
  as closure.
- Next: Worker 03 independent acceptance, prompt `03_acceptance_00.md`,
  candidate `36ffdb19…`, fresh worktree w3, do not use w2.
- No push, NUC, or FrameNest mutation this turn.

## 2026-08-26 — Worker 03 independent acceptance reviewed

- Claim `03_report_00.md`: `acceptance-PASS` of
  `36ffdb197da9294fb1fbb06931f8169061a25c9b`. Session 03 authority expired
  at that report. Independence claimed (did not author the two commits).
- Direct object verification (this Orchestrator):
  - Canonical still `2aead54…` / tree `0900818f…` tracked-clean; AP pin
    `9c5cc44…`; public `main` still `2aead54…` (`ls-remote`).
  - w3 detached at `36ffdb19…` tracked-clean; ancestor of `2aead54…`;
    rev-list count 2; unused as implementation copy.
  - w2 still `36ffdb19…` on `feat/ai-suggestions-alias-edit-mvp`,
    tracked-clean, unused by session 03 as working copy.
  - Path set exactly 15; persist-join blobs equal parent; no 0034; ADR
    bodies 0062/0076/0023 untouched; four `companion_mutation=True` at
    `tailscale_ingress.py` 540/550/558/567; `app.js` has no `/apply`;
    probe `/tmp/framenest-aliasacc-03-provenance.py` absent.
  - Spot-checked control-matrix lines: `identityAllowsMetadataEdit`
    353–358; Analyze gate 7289; 🧠 still `analysis.run` ∧ `canonical.write`
    5254–5258; card title `item.display_title` 6030.
  - Tests: not re-run here; acceptor reported 230 Python + 181 JS from w3
    with RF-16 deviation and w3 `framenest.__file__`.
- `acceptance-PASS` accepted. Logical whole **not closed**. Publication,
  NUC, and numbered re-test 1–12 remain Cooperator-owned next surfaces.
- No push, NUC, or FrameNest mutation this turn.

## 2026-08-26 — Cooperator item-1 FAIL (live NUC / public main)

- Michal scored item 1 FAIL: ordinary Gallery has no bottom-left Edit
  icon; Details preview has Technical details + description and no Edit
  button (admin has both).
- Public `refs/heads/main` re-read: still `2aead54…`. Canonical same.
  Candidate `36ffdb19…` is unpublished. Rendered NUC cannot serve the
  candidate.
- That FAIL matches **predecessor** `app.js` on `2aead54…`: Gallery ~6029
  and Details ~444 gate Edit on `metadata.canonical.write` only. Ordinary
  therefore never gets the overlay control. This is the defect this whole
  exists to fix; it is not a candidate defect and does not authorize
  correction of `36ffdb19…`.
- Next remains Cooperator publication of `36ffdb19…`, then
  `~/nuc_push.fish`, then re-score item 1 (and 2–12) on that SHA.

## 2026-08-26 — publication of 36ffdb19 to public main

- Cooperator grant: „publikovať.“
- Preflight: public `main` was `2aead54…`; candidate `36ffdb19…` is a
  descendant of that SHA (two commits); canonical tracked-clean.
- One non-force push:
  `git push --porcelain origin 36ffdb197da9294fb1fbb06931f8169061a25c9b:refs/heads/main`
  → `2aead54..36ffdb1`.
- Credential-free `ls-remote` `refs/heads/main` =
  `36ffdb197da9294fb1fbb06931f8169061a25c9b`.
- Local `feat/x-meme-browser-companion` fast-forwarded to the same SHA
  (canonical now matches public main). Did not push
  `feat/x-meme-browser-companion`.
- `Phase-qualified result: publication-PASS`. Logical whole not closed.
  NUC and numbered re-test remain Cooperator-owned.

## 2026-08-26 — Cooperator numbered re-test after NUC refresh

Rendered scores on published `36ffdb19…` (screenshot: admin standalone Edit
with suggestions chrome vs compact/hosted Edit without Load):

| Item | Score | Classification |
|---|---|---|
| 1 | PASS | Ordinary Edit affordance works; alias write is the Save path. |
| 2 | PASS on freeze + new product defect | Canonical unchanged in admin Manage / public / admin Gallery is the **frozen** ADR-0077 display rule. Ordinary then cannot see their own Save anywhere except re-open Edit. Cooperator now requires caller-visible overlay. |
| 3 | PASS | Hosted Details: Edit shown; Analyze/Load hidden — **as frozen**. Later item-4 addendum supersedes the Load-hide half. |
| 4 | PARTIAL + addenda | Original chrome (heading, dropdown+Load above Title) is present on admin standalone. New intent: ordinary Load of admin-provided title/description/tags/filename; same Edit+Load in companion (hosted side panel). Conflicts with ADR-0077 §§5–8 (`workflow.read` only; alias mode hides chrome; hosted hides Load; filename admin-only). |
| 5 | PASS | Load does not overwrite Current. |
| 6 | PASS | Per-field title ✅. |
| 7 | PARTIAL + addenda | Suggested tags exist but chips are `pointer-events: none`; overlay/overlap in the tags strip; Cooperator wants the chip itself to append into selected tags with `x`. Hide Content category and Acquisition source in this dialog (admin too). Freeze had kept admin classification. |
| 8 | PARTIAL + addenda | Dropdown change still must not call provider (not rescored as FAIL). After Analyze, list shows 3 not 2; re-open shows 2. Matches in-session prepend plus inbox refresh when preview `analysisRunId` ≠ persisted run id (`refreshMetadataSuggestionList` keeps `selectedItem` if missing). Native `<select>` is not companion eye-candy. |
| 9 | not scored | Leave as prior companion PASS; do not reopen R1–R3′. |
| 10–12 | PASS | Isolation and copy/provider items hold. |

Proposed correction freeze (awaiting Cooperator `koriguj`; not issued):

1. Caller-visible alias **read**: authenticated catalog list/detail merge
   overlay for `(media_id, login_key)` into the fields Gallery/Details
   already render. Other identities, anonymous/public, and admin Manage
   canonical stay canonical. No `0034`. Succeed ADR-0077 §2 display sentence
   and the ADR-0062 frozen-surface **read** clause the same way §1 succeeded
   Edit affordance — do not edit ADR-0062/0076/0023 bodies; successor note
   on ADR-0077.
2. Load chrome for ordinary **and** alias mode **and** hosted companion
   web. Analyze stays `analysis.run` ∧ not hosted. Ordinary does not gain
   `workflow.read`, Apply, or Analyze. New/extended **read** list of
   generic analyzed runs for media the caller can already GET (not inbox
   Apply). Schema `0033`.
3. Filename: reveal as informational strip (ordinary too). Alias PUT still
   title/description/tags only — filename is not overlay and must not
   become canonical rename.
4. Companion **extension** = hosted FrameNest in the side panel (right
   screenshot), not a second Edit inside `extension/ui/save.html`.
5. Suggested tag = button; click appends to Current chips with `x`; wrap
   without overlap; enable pointer events.
6. Hide Content category and Acquisition source in this Edit dialog for
   all actors; admin Save preserves existing canonical values (no silent
   category rewrite).
7. Dedupe dropdown after Analyze; replace native select with companion-
   language custom dropdown (dark, green accent). No provider on change.

Out of this correction: R4, VPS, Gallery 🧠 per-field, Cover Studio,
ordinary `analysis.run` / canonical.write / Apply, hover-`+` save.html
redesign.

## 2026-08-26 — Cooperator «koriguj»; Worker 04 issued

- Grant: Cooperator accepted the correction freeze in the prior notes
  entry. Prompt `04_correction_00.md`. Session 04 / exchange 01,
  `fresh-worker-session`, `Native planning mode: not-used`, isolated
  worktree w4 from published `36ffdb19…`. No push. Full-fresh independent
  acceptance remains a later Worker (`Automatic corrections used: 1`).
- Canonical checkout must stay `36ffdb19…` tracked-clean.

## 2026-08-27 — Worker 04 correction claim reviewed; Worker 05 issued

- Claim `04_report_00.md`: `implementation-PASS` at
  `afa0670e26d17b04570ad555ba4f922052507c6c` (parent `85e9c04…` feat, then
  docs). Session 04 authority expired at that report.
- Direct object verification (this Orchestrator):
  - Canonical still `36ffdb19…` / tree `30197622…` tracked-clean; public
    `main` same; AP pin `9c5cc44…`.
  - w4 HEAD `afa0670e…`, branch `feat/ai-suggestions-alias-edit-corr`,
    tracked-clean, two commits, ancestor of `36ffdb19…`.
  - Path set 27 files vs parent. Named off-allowlist deviation is
    `companion_review_repository.py` (+1 constructor argument
    `suggested_filename=`). Accepted as reuse, not a second store.
  - No 0034; ADR-0062/0076/0023 bodies untouched; four
    `companion_mutation=True` at `tailscale_ingress.py` 545/555/563/572.
  - Additive GET `/api/media/{id}/ai-suggestions` capability
    `metadata.alias.write`, not mutation. Catalog merge on list/get.
    Load vs Analyze split (`identityAllowsAiSuggestionLoadChrome` /
    `identityAllowsAiAnalyze`). Hosted Load shown. Classification row
    `hidden = true`. Refresh dedupes on `analysis_run_id` (no missing-id
    prepend). `app.js` has no `/apply`.
  - Tests: not re-run here.
- Implementation-PASS accepted as an Orchestrator-verified **claim of
  completeness against the correction freeze**, not as independent
  acceptance and not as closure.
- Next: Worker 05 independent full-fresh acceptance, prompt
  `05_acceptance_00.md`, candidate `afa0670e…`, fresh worktree w5, do not
  use w4.
- No push, NUC, or FrameNest mutation this turn.

## 2026-08-27 — Worker 05 independent acceptance reviewed

- Claim `05_report_00.md`: `acceptance-PASS` of
  `afa0670e26d17b04570ad555ba4f922052507c6c`. Session 05 authority expired
  at that report. Independence claimed (did not author the two correction
  commits). Session 03 verdict on `36ffdb19…` was not reused as evidence.
- Direct object verification (this Orchestrator):
  - Canonical still `36ffdb19…` tracked-clean; public `main` same; AP pin
    `9c5cc44…`.
  - w5 detached at `afa0670e…`; ancestor of `36ffdb19…`; rev-list count 2.
  - w4 still `afa0670e…`, unused as session-05 working copy.
  - Path set exactly 27; probe `/tmp/framenest-aliasacc-05-provenance.py`
    absent.
  - Spot-check: `identityAllowsMetadataEdit` `app.js` 353–359; GET
    `/api/media/{id}/ai-suggestions` ingress 307–311
    (`metadata.alias.write`). Tests not re-run here.
- `acceptance-PASS` accepted. Logical whole **not closed**. Publication,
  NUC (`~/nuc_push.fish`), and numbered re-test 1–12 remain
  Cooperator-owned next surfaces.
- No push, NUC, or FrameNest mutation this turn.

## 2026-08-27 — publication of afa0670e to public main

- Cooperator grant: „publikovať.“
- Preflight: public `main` was `36ffdb19…`; candidate `afa0670e…` is a
  descendant of that SHA (two commits); canonical tracked-clean.
- One non-force push:
  `git push --porcelain origin afa0670e26d17b04570ad555ba4f922052507c6c:refs/heads/main`
  → `36ffdb1..afa0670`.
- Credential-free `ls-remote` `refs/heads/main` =
  `afa0670e26d17b04570ad555ba4f922052507c6c`.
- Local `feat/x-meme-browser-companion` fast-forwarded to the same SHA
  (canonical now matches public main). Did not push
  `feat/x-meme-browser-companion`.
- `Phase-qualified result: publication-PASS`. Logical whole not closed.
  NUC and numbered re-test remain Cooperator-owned.

## 2026-08-27 — Cooperator PASS; logical whole closed

- Cooperator: „PASS, predpokladám, že closeout dáva zmysel teraz.“ Treated
  as rendered PASS of numbered items 1–12 on NUC serving published
  `afa0670e…`, plus explicit closeout intent.
- Direct re-read at closure:
  - Public `refs/heads/main` =
    `afa0670e26d17b04570ad555ba4f922052507c6c`
  - Canonical `/home/agile/Projects/framenest`
    `feat/x-meme-browser-companion` same SHA, tracked-clean
  - AP pin `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
  - No in-flight Worker; no unpublished candidate; no FrameNest mutation
    this turn

```text
Phase-qualified result: production-acceptance-PASS
Result artifact or commit: afa0670e26d17b04570ad555ba4f922052507c6c
Result evidence: Cooperator rendered PASS after NUC refresh of published main
Logical-whole closure: closed-by-ORCHESTRATOR
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
Declared closure signal: closed-by-ORCHESTRATOR
Signal owner: orchestrator
Worker emission of closure signal: prohibited
Accepted evidence: implementation-PASS 04 (afa0670e); full-fresh acceptance-PASS 05; publication-PASS of afa0670e to origin/main; Cooperator PASS 1–12 on NUC
Active-context reconciliation: complete
Closure authority: present
Implementation completion: implementation-PASS at afa0670e
Audit completion: acceptance-PASS session 05
Publication: publication-PASS afa0670e == refs/heads/main
Public Git equality: equal
Orchestrator acceptance: accepted
```

Preceding results: correction implementation-PASS (session 04), full-fresh
independent acceptance-PASS (session 05), publication-PASS of the same SHA,
Cooperator rendered PASS. Schema remains `0033`. Four `companion_mutation`
unchanged.

Upgrade ledger `docs/AP_UPGRADE_OBSERVATIONS.md` entry
`consumer-declared-execution-and-capability-route-binding` remains
`untriaged` / `non-authorizing` / `Closure action: retain-active`. Isolated-
worktree `ap exec --root <worktree>` launch-path miss is unchanged and
**not this kebab**. No FrameNest ledger mutation at closure.

Parked remainder (not this whole; not a reopen):
- Gallery 🧠 admin bulk analyze-and-canonical-save (per-field not done)
- R4 Settings automatic-analysis checkbox
- VPS
- Cover Studio
- Persistent multi-model comparison board
- `origin/feat/x-meme-browser-companion` stale ahead-count (informational)
- Loopback `create_app` skips ingress capability (public HTTP 403 on
  suggestion-list GET unproven in that topology; route-policy evidence held)

No next logical whole is selected. Restoration for a later Orchestrator
starts read-only at public `main` `afa0670e…` and this closure entry. Do not
resume era-07 Worker ordinals 01–05 as live authority.

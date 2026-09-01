# Era 11 Whole Notes — `framenest-companion-unread-inbox-and-editor-suggestion-ux`

Handout: `00_handout_agent.md` (Agent Orchestrator profile; AP 7ef45da
profile-qualified convention).

Classification: private local historical/evidentiary projection for this
logical whole. This file is non-authorizing, public-safe by default, written
only by the Orchestrator, append-only during the whole, and frozen at closure.
Michal owns any meta-repository commit.

## Identity

- Logical whole: `framenest-companion-unread-inbox-and-editor-suggestion-ux`
- Canonical repository: `/home/agile/Projects/framenest`
- Branch: `feat/x-meme-browser-companion`
- Verified starting HEAD: `454f181d8b011ef563ac13a28e8d894dbc497bc4`
- Product freeze baseline: `472553cadcd3d4ca87a9792a2c306bd0afeea7c1`
- AP pin: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`
- Cooperator: Michal (Slovak chat, masculine address; English artifacts and
  prompts; one-glance status block followed by exactly one status mark; one
  decision per message)
- Profile: Agent Orchestrator default dispatch (P14 opt-out only on explicit
  request)

## Restoration Gates — 2026-08-29

| Gate | Directly observed result | Status |
| --- | --- | --- |
| FrameNest branch / HEAD | `feat/x-meme-browser-companion` / `454f181d8b011ef563ac13a28e8d894dbc497bc4` | PASS |
| Origin branch equality | `origin/feat/x-meme-browser-companion` = `454f181d8b011ef563ac13a28e8d894dbc497bc4` | PASS |
| Origin main equality | `origin/main` = `454f181d8b011ef563ac13a28e8d894dbc497bc4` | PASS |
| FrameNest porcelain | empty | PASS |
| Product freeze ancestor | `472553cadcd3d4ca87a9792a2c306bd0afeea7c1` is an ancestor of HEAD | PASS |
| `.ap` gitlink / checkout | both `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`; detached checkout clean | PASS |
| Public AP main | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` from canonical `https://github.com/cisarik/ap.git` | PASS |
| AP doctor | PASS; `OK resolved governing variant: stable` | PASS |
| NUC runtime | not directly reverified; Cooperator-owned private wrapper deliberately not inspected or invoked | OPEN EVIDENCE |

Meta repository opened with pre-existing owner state: modified era-10
`00_notes.md` and untracked era-11 directory containing the handout. This is
classified as `unrelated-owner-work` outside FrameNest repository mutation;
preserve it and do not commit the meta repository.

## Upgrade Ledger Reconciliation

Declared ledger: `docs/AP_UPGRADE_OBSERVATIONS.md`, target
`https://github.com/cisarik/ap.git`, storage version 1. The sole entry
`consumer-declared-execution-and-capability-route-binding` is structurally
valid, `accepted`, non-authorizing, and `retain-active`; its last revalidation
identity equals the current governing AP pin `7ef45da`. No contradictory AP
advance exists. Retain active. Product defects and era-11 UX direction are not
AP-ledger material.

## Session Log

- **Open and restoration (2026-08-29):** Read the handout; independently
  verified the local/public repository and AP gates above; read the required
  AP and project governance, execution, security, product, server, companion,
  SPEC sections, ADR-0048/0053/0061/0062/0064/0067–0070/0072–0079, and the
  complete era-10 notes. The handout is treated as subordinate evidence, not
  mutation authority. No Worker is active and no FrameNest repository, Git,
  NUC, provider, browser, account, or deployment mutation has begun. The next
  evidence step is read-only diagnosis of the four reported regression/failure
  classes before proposing one bounded planning exchange.

## Confirmed-Refinements Ledger

Carried forward as Cooperator-confirmed product direction and observed
acceptance evidence, subject to current-code diagnosis:

1. Regression: suggestion-tag clicks appear inert on previously analyzed
   items, including remove/re-add. **NUC Slice 1 T1–T3 PASS (2026-08-29).**
2. Regression: animated preview restarts instead of pause/resume; video resumes
   but flashes black on open; video hover cursor refinement requested.
   **Open — Slice 2. Not in the Slice 1 batch.**
3. Honest failure UX: provider invalid-response failures need retryability and
   actionable in-modal status, with visible progress while analysis runs.
   **NUC Slice 1 T6–T9 PASS for in-modal progress/failure/retry UX.
   Parser/provider root-cause remains deferred pending sanitized NUC
   classification evidence.**
4. Honest failure UX: unsupported X video Save must be detected before a
   generic downstream failure and explained at the affordance.
   **Open — Slice 3. Planner classification: do not hide native X video Save
   (ADR-0064); reduce `failureCode`/`canRetry` honestly. Not in this batch.**
5. Editor direction: Edit opens with the newest suggestion loaded; no Load
   button; dropdown switches immediately; Gallery/editor brain action opens an
   empty loading Edit modal immediately and resolves in place; preserve
   confirmation-before-save and alias/canonical capability boundaries.
   **NUC Slice 1 T1, T4, T5, T6–T8 PASS. Shipped as ADR-0080 on `a4193d4`.**
6. Companion direction: live refresh; active history is the unread slice of
   one conceptual history list; analyzed unread remains until opened; ordinary
   users receive unread analyzed items when an administrator approves analysis
   of their contributed media. Chrome-semantics changes require living-doc
   updates and a Cooperator decision on whether a new ADR is warranted.
   **Open — Slices 4–5. D11-01 already chose ordinary notification after
   successful admin-run generic analysis of attributed media; proposals stay
   non-executing. Not in this batch.**

Open historical question OQ-1 remains non-blocking: whether workstation-pull
provisioning exists on the NUC for the two named runbook passages. Do not touch
that runbook without asking Michal.

## Read-only Diagnosis — 2026-08-29

No product mutation was performed. The focused baseline evidence is green:

- `node --test` over the editor, card quick action, alias, companion review,
  and X companion extension suites: **212 passed**.
- canonical AP `test-focus` over companion review persistence/API and media
  suggestion API: **58 passed**.

### A1 — suggested tags

`renderMetadataSuggestionStrips()` correctly makes mapped canonical tags
clickable and intentionally keeps unmapped alias-mode tags inert. The concrete
silent no-op is in `copySuggestionFieldToCurrent()`: when the tag already exists
in Current, it returns without state change, visible selected/already-added
semantics, or status. That explains the observed inert click for common existing
tags such as `x`. It does not by itself explain a remove-then-re-add failure;
that needs a focused behavior test/browser reproduction in the implementation
slice before broadening the fix.

### A2 — compact card playback

Video pause/resume already preserves `currentTime`. Its live surface clears the
static preview before a newly created `<video>` has loaded data, and the video
has no poster/ready handoff; this is a direct black-flash mechanism. All playable
card surfaces inherit the pointer cursor from the button-role placeholder CSS.

Animated images use a plain `<img>`. Clicking while playing calls global media
cleanup, removes the GIF source, and restores the static cover; replay creates a
new `<img>` and restarts at frame zero. A plain browser GIF image has no native
pause/resume position control. Git history places this behavior before the
editor rework, so the handout's regression attribution is not supported by
repository evidence, although the requested behavior remains a valid product
amendment. The old representative-frame timer is a separate generated-preview
mechanism and is not a faithful GIF pause/resume implementation.

### A3 — provider invalid response

The API deliberately sanitizes strict provider/schema parse failures to HTTP
502 `AI_PROVIDER_INVALID_RESPONSE`. The client further reduces this to
`AI response was invalid.` The Edit-modal Analyze action exposes only text
`Analyzing…`; the Gallery brain waits for the provider before opening Edit and
leaves failure status on the card. Repository evidence therefore confirms the
in-modal progress/failure UX gap, but cannot distinguish a transient NUC
provider payload from a parser defect or provider configuration issue. That
cause needs sanitized Cooperator-owned NUC evidence; no provider call or private
wrapper inspection was attempted. Unbounded automatic retry is not justified
by current evidence.

### A4 — X video Save

The handout's premise that X acquisition is still-image-only is contradicted by
current durable truth. `PRODUCT.md` and ADR-0064 explicitly support native X
video and GIF-like X media delivered as MP4. The extension intentionally mounts
Save on video hosts and submits the post URL; the server extractor owns asset
classification. Hiding or rejecting Save on video would regress an accepted
feature and is not an admissible fix.

The server already returns sanitized claim-level and asset-level failure codes,
and the service worker preserves claim `failureCode`, `canRetry`, and terminal
state. `reduceXSaveOutcome()` discards that classification for every terminal
`failed` claim and emits only `Save to FrameNest failed`. The honest UX seam is
therefore failure-code reduction plus diagnosis/fix of the supported acquisition
path, not unsupported-media detection. The actual NUC incident cause remains an
evidence gap until its sanitized terminal claim/log evidence is read back.

### B — suggestion/editor flow

The web editor currently selects the newest durable suggestion but keeps it
hidden until `Load`; dropdown changes hide strips again. New in-session analysis
is the only path that reveals immediately. The requested web change is therefore
precisely localized: newest-on-open reveal, immediate reveal on dropdown change,
and removal of the Load control without bulk-applying fields. Gallery brain must
open the existing Edit lifecycle before the provider request and retain its
request/media/revision fences while rendering progress and failure in place.

The legacy extension review popup already selects the newest suggestion,
switches dropdown runs immediately, and has no Load button. Current title-bar
history clicks open hosted Details/Edit rather than that overlay. Any new plan
must avoid reintroducing the retired overlay into the active path merely to make
it match wording in the handout.

### C — companion unread history

The sidebar already requests fresh history immediately and polls every 15
seconds while visible; a one-minute service-worker alarm refreshes only the
badge. The active UI renders a merged conceptual history, but its compact slice
is newest five analyzed items for administrators and newest five items of any
state for ordinary users, regardless of `unopened`. Thus “active history equals
unread” is a semantics/query/render change, not simply adding polling.

Opening an analyzed item already posts its exact `analysis_run_id`; open state
is actor-scoped, and a later successful run becomes unopened again. This can be
reused. Ordinary `own-history`, however, is explicitly limited to cataloged X
media attributed to that requester. Upload and YouTube contribution attribution
already exist elsewhere, but are absent from this query. Analysis proposals are
durable open notifications only: there is no proposal approval/resolution route,
and creating one never runs a provider. “After admin approves analysis” therefore
needs a deliberate workflow definition and likely a durable-truth/ADR decision;
it cannot honestly be implemented as a cosmetic history filter.

### Planning boundary

The evidence supports one batched High-reasoning Planner exchange covering all
four diagnoses plus editor and unread-history semantics, with explicit slices,
tests, living-doc effects, NUC evidence gaps, and an ADR recommendation. It must
preserve X video support, contributor-scoped access, actor-scoped open state,
alias/canonical authority, and provider/log sanitization.

## Planning Exchange 01 — 2026-08-29

Dispatched exactly one High-reasoning Planner Worker for the batched whole.
The Worker remained read-only, reported the same repository start/end
`454f181d8b011ef563ac13a28e8d894dbc497bc4`, performed no Git/provider/NUC/
browser activity, delegated no work, and emitted no closure. Exact archival:
`01_planning_00.md` + `01_report_00.md`.

The implementation-ready plan has five coherent slices:

1. Editor suggestion state, tag behavior, and in-modal analysis UX, with a
   successor ADR because accepted ADR-0077/0078 currently prescribe the Load
   and analyze-before-open behavior being superseded.
2. Video ready-state handoff/cursor plus an honest animated-image approach;
   true GIF resume is conditional on target Brave `ImageDecoder` evidence or a
   later dependency/normalization decision.
3. X terminal-outcome reduction first, with any supported-video backend fix
   selected only from sanitized terminal-claim evidence.
4. One-list unread active slice and focused refresh lifecycle evidence, without
   adding a speculative timer.
5. Ordinary contributor-scoped analyzed history after the Cooperator chooses
   the durable meaning of administrator “approval.”

Planner recommendation for Slice 5: notify an ordinary actor after any
successful administrator-run generic analysis of media attributed to that
actor across upload, YouTube, and X; keep analysis proposals as non-executing
administrator attention records. This reuses the successful run and exact-run
actor-scoped opened state and needs no migration. Alternative: add an explicit
proposal approval/dismissal lifecycle, provider execution/failure linkage, new
audit mutations, and a post-0033 migration. The choice blocks only Slice 5,
not Slices 1–4.

## Cooperator Decision D11-01 — 2026-08-29

Michal confirmed the recommended ordinary-notification semantics. An ordinary
actor receives an unread companion item after a successful administrator-run
generic analysis of media attributed to that actor through upload, YouTube, or
X. Analysis proposals remain non-executing administrator attention records;
this whole will not add an approval/dismissal lifecycle or a proposal-resolution
migration. The successor companion ADR must carry this decision and its
preserved capability/privacy boundaries.

## Interrupted Slice 1 continuation — 2026-08-29

Codex dispatched one bounded Slice 1 implementation Worker (`slice1_impl`) after
D11-01. That Worker wrote the editor/tag/in-modal analysis core into the
canonical worktree and then died on a provider usage limit before tests, ADR,
and living docs were green. The worktree was therefore locally broken: Load
removed, harnesses half-realigned, no ADR-0080.

The Orchestrator continued that exact incomplete envelope in-session (no new
Worker spawn, no Git write, no push, no NUC, no provider call). Completed:

- Newest-on-open reveal; Load removed; dropdown switches immediately.
- Mapped-tag already-added / remove / re-add.
- Gallery 🧠 opens Edit immediately, then analyzes in-modal with spinner;
  sanitized failure and manual reconfirm retry stay in the dialog.
- Successor ADR-0080 plus in-slice living docs.
- Focused Node suite 185 passed; AP `test-focus` over
  `test_local_web_application.py`, `test_media_suggestion_api.py`, and
  `test_media_ai_suggestions_api.py` 255 passed. Baseline remains
  `454f181d8b011ef563ac13a28e8d894dbc497bc4`. Porcelain is dirty; HEAD
  unchanged.

Slices 2–5 are not in this diff. Publication/push/NUC refresh are not done.

## Publication — Slice 1 — 2026-08-29

Cooperator ordered Slice 1 publish so he can re-test on the newest NUC
("Ano samozrejme ze chcem slice 1 aby som mohol otestovat fixy"). Standing
"fix now, then I re-test" plus this explicit grant.

Committed `a4193d4f520a30aafa333987f2e6b846a5425d27` on
`feat/x-meme-browser-companion`. Non-force push:
`454f181..a4193d4` to `origin/feat/x-meme-browser-companion` and
`origin/main`. `git ls-remote` confirms both refs equal
`a4193d4f520a30aafa333987f2e6b846a5425d27`. Schema head remains `0033`.
Porcelain empty. No NUC SSH or private wrapper was invoked; a Cooperator
manual refresh attempted before this push could only have landed `454f181`.
NUC must be refreshed to `a4193d4` before rendered acceptance.

## NUC refresh blocked — leftover deploy lock — 2026-08-29

Cooperator ran the private wrapper `status` / `check` / `deploy` / `status`.
Sanitized observed facts (no host identifiers recorded here):

- `check` accepted public `main` `a4193d4f520a30aafa333987f2e6b846a5425d27`,
  AP gitlink `7ef45da`, and `backup_restore_readiness: ready`.
- `deploy` stopped with engine message `existing remote lock or recovery state`
  (`EXIT_EXISTS` 9): remote `mkdir -m 0700 /run/framenest-release-deploy`
  failed because that directory already exists.
- Pre- and post-attempt `status` both report `active_release: 22352c9…`,
  `service_active: active`, `database_revision: 0033`. The NUC never left the
  older same-schema tree; this is not a `migration-required` stop.
- G0 remains FAIL. T1–T9 must not start until `active_release` equals
  `a4193d4f520a30aafa333987f2e6b846a5425d27`.

Cooperator inspect (later same day): `ls -1` of the lock directory printed no
names; `a4193d4` release and `.staging` trees are both absent. That matches an
empty leftover lock directory, not a half-published Slice 1 tree and not a
broken operator wrapper. Next operator step is annex lock cleanup only
(named `rm -f` then `rmdir`; no recursive delete, no migrate). Then retry
wrapper `deploy`. Unexpected `rmdir` failure stops the run.

## NUC G0 PASS — Slice 1 live — 2026-08-29

After empty-lock `rmdir`, Cooperator wrapper `status` reports:

- `active_release`: `a4193d4f520a30aafa333987f2e6b846a5425d27`
- `service_active`: active
- `database_revision`: `0033`
- `backup_restore_readiness`: ready

G0 PASS. Rendered T1–T9 may start. Slices 2–5 remain out of this batch.

## Slice 1 rendered acceptance — 2026-08-29

Cooperator executed T1–T9 on the live NUC at `a4193d4` and reported PASS on
every step (T1 through T9 inclusive). Slice 1 is accepted. Do not reopen
ADR-0080, Load, already-added tags, or in-modal analysis unless a later FAIL
names a concrete defect.

A restoration handout for a fresh Agent Orchestrator on Slice 2 is
`00_handout_agent_slice2.md`. That Orchestrator must not overwrite
`01_planning_00.md` / `01_report_00.md`. Next planning pair is
`02_planning_00.md` + `02_report_00.md`, Slice 2 only.

## Restoration Gates — Slice 2 Agent Orchestrator — 2026-08-29

Handout `00_handout_agent_slice2.md` treated as RF-19 seed, not mutation
authority. Read-only restore. No Worker dispatched. No FrameNest Git, NUC,
provider, browser, private-wrapper, or implementation mutation.

| Gate | Directly observed result | Status |
| --- | --- | --- |
| FrameNest branch / HEAD | `feat/x-meme-browser-companion` / `a4193d4f520a30aafa333987f2e6b846a5425d27` | PASS |
| Origin branch equality | `origin/feat/x-meme-browser-companion` = `a4193d4f520a30aafa333987f2e6b846a5425d27` | PASS |
| Origin main equality | `origin/main` = `a4193d4f520a30aafa333987f2e6b846a5425d27` (local tracking and `git ls-remote origin`) | PASS |
| FrameNest porcelain | empty | PASS |
| Product freeze ancestor | `472553cadcd3d4ca87a9792a2c306bd0afeea7c1` is an ancestor of HEAD | PASS |
| `.ap` gitlink / checkout | both `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`; submodule clean | PASS |
| Public AP main | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` from canonical `https://github.com/cisarik/ap.git` | PASS |
| AP doctor | PASS; `OK resolved governing variant: stable` | PASS |
| Schema head | Alembic revision `0033` (`0033_media_analysis_proposals.py`); no later `down_revision` | PASS |
| Successor ADR-0080 | present, `Accepted` 2026-08-29 | PASS |
| NAC ledger | sole entry `consumer-declared-execution-and-capability-route-binding`, `accepted`, `retain-active`, last revalidated against `7ef45da` | PASS |
| NUC runtime | not directly reverified this session; Cooperator-owned private wrapper not inspected or invoked. Last Cooperator-reported G0: `active_release` `a4193d4`, service active, `database_revision` `0033`, `backup_restore_readiness` ready | OPEN EVIDENCE |

`01_planning_00.md` / `01_report_00.md` preserved as the batched whole plan
from `454f181`. Slice 1 remains closed unless a later FAIL names a concrete
defect. Next legal Worker, after explicit Cooperator selection of Slice 2,
is one High-reasoning read-only Planner archived as `02_planning_00.md` +
`02_report_00.md`.

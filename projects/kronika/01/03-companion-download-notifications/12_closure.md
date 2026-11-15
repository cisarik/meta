# 12 — Closure: companion downloads, compact UI and unread history

```text
Logical whole identity: companion-download-notifications
Development run identity: kronika-run-01
Orchestrator session scope: logical-whole
Opened: 2026-11-11
Closed: 2026-11-14
Baseline: e64f2b0f92458fac2590e03672e30da62275b345
Final candidate: 2c4f4d89375628df28926060aba305e5d80bacff
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50
Delivery route: manual Cooperator copy-paste
Repository: https://github.com/cisarik/kronika
Logical-whole closure: closed-by-ORCHESTRATOR
Phase-qualified result: production-acceptance-PASS (Cooperator-declared)
```

This is the final trace document for the whole. It records the delivered
behavior, the development history and its corrections, the evidence at closure,
the three residuals that remain outside this whole, and the process lessons.
`00_notes.md` remains the chronological Orchestrator record and is frozen at
closure; this document does not reopen it and does not create new authority.

## 1. Outcome in brief

The whole added the signed-in requester's own X and YouTube download status to
the existing companion history sheet, then iterated four times on Cooperator
rendered feedback until the visible result matched the requested behavior.
The final candidate `2c4f4d8` was published to public `main`, deployed to the
NUC through the canonical release helper, and rendered by the COOPERATOR with
all six final items PASS. No new permission, message type, alarm, storage key,
backend route, schema migration or mutation was added.

The most important facts are:

1. The download block is a separate **Recent downloads** section above review
   history in the existing title-bar sheet; it shows only the signed-in
   requester's own X/YouTube requests.
2. A row with an own cataloged media id opens hosted Details and stays
   clickable after read; a row without a media id is inert.
3. Rows are ordered by the latest request update, read at `limit=50`, and up to
   fifty are retained.
4. The compact sheet shows five downloads and exactly one **All**. That All
   reveals the sixth and later retained downloads plus the complete review
   history, and collapses again.
5. A review row whose media id matches a download row is omitted, so no title
   is duplicated; the matched download row carries the unread marker.
6. Clicking a matched analyzed unread download row opens Details and posts the
   existing `REVIEW_INBOX_OPENED` once, clearing the marker and badge.
7. The badge remains the server `unopened_count` for the review source only;
   download outcomes never contribute and no second counter exists.
8. The companion-hosted Timeline and My contributions were compacted without
   changing the wide page; that correction was a Cooperator-directed closeout
   of this same whole, not a new whole.

## 2. Delivered behavior

### 2.1 Recent downloads

- The block reuses the existing `review_inbox` message and history sheet. A
  successful response adds `downloads: {ok, items}`; a download-read failure is
  exactly `{ok:false, items:[]}`; a successful empty result is
  `{ok:true, items:[]}`. There is no second message type or transport.
- Reads use the fixed application paths for the X and YouTube request lists,
  joined to the configured origin, with `limit=50`. There is no
  caller-controlled URL, path, id or cursor, and no cursor following. A missing
  capability skips that source.
- Each row carries only a sanitized projection: source, request id, bounded
  label, status, own media id and sort timestamp. Raw URLs, asset arrays,
  filenames, provider payloads and failure details never reach the sidebar.
- Status text is `Saving…`, `Saved`, `Saved privately`, `Partly saved`,
  `Already saved`, `Download failed` or `Unavailable`. Analysis, publication
  and catalog presence never create a completion claim; only the acquisition
  state maps a status.
- `sort_at_ms` prefers a valid `updated_at_ms` and falls back to
  `created_at_ms`. Merge deduplicates by `(source, request_id)`, sorts by
  `sort_at_ms` descending, source ascending, request id descending, and keeps
  up to fifty rows.
- A row with an own UUID media id is a `button` that posts one `open_details`
  with that media id. It has no retry or removal action and remains clickable
  after the save was read. A null media id renders a non-focusable inert
  `div`.

### 2.2 Review interplay, unread state and badge

- A review row whose media id matches any download media id is omitted from
  both the compact and expanded review lists. A distinct review row remains; a
  download without a media id does not drop a review row.
- A download row matching an analyzed unread review item with a UUID
  `analysis_run_id` shows the unread dot and accent plus an accessible
  **Unread** indication. Its click posts one `open_details` and one existing
  `REVIEW_INBOX_OPENED` for that analysis run, then refreshes. The row remains
  and the marker clears only after the refreshed unread state. A second click
  before refresh does not post a second opened; a read match posts no opened;
  an inert null-media row posts neither.
- The toolbar badge stays the server `unopened_count` for the active review
  source. Download outcomes never contribute. The alarm refreshes the review
  badge only and makes no download-list call. There is no `notifications`
  permission and no second counter. The existing opened mutation is the only
  mutation used to clear the marker and badge.

### 2.3 Compact companion UI

- In the companion-hosted shell, the Timeline hides status and visibility
  glyphs, shows Kind, Status and Visibility as readable text, and does not
  clamp the title. One **Filter** button expands and collapses the existing
  four filters; it starts collapsed and changes no query by itself. The wide
  page keeps its glyph table, two-line title clamp and visible filters, and
  hides the Filter button.
- Companion My contributions gives the title the full row width and normal
  word wrapping; the wide page keeps its multi-column grid.
- The compact history sheet shows five downloads and one **All**. While
  downloads exist, the review **All** stays hidden and the download **All** is
  the only All. Expanding reveals the sixth and later retained downloads and
  the complete review history; collapsing returns to the five-download sheet.
  The state starts collapsed on each panel load and is not persisted. With no
  downloads, review history keeps its previous compact/All behavior and no
  empty download All is shown.

### 2.4 Invariants held

- No backend, schema, migration, API route or `tailscale_ingress.py` policy
  change. Exactly the six pre-existing `companion_mutation` routes remain:
  automatic-analysis settings, YouTube request creation, review opened, review
  apply, X request creation and X retry.
- `extension/manifest.json` is unchanged. Permissions remain exactly `alarms`,
  `sidePanel` and `storage`; no `notifications`, `host_permissions`,
  `externally_connectable` or new optional permission. The pre-existing
  optional `downloads` and `https://*.ts.net/*` entries were not added by this
  whole.
- No download snapshot is persisted. The existing `kronikaOrigin` storage key
  is the only worker storage used; the configuration revision is in memory.
- Download failure hides only the Downloads block and retains review rows and
  the badge. Review pagination/cursor failure hides all history and clears the
  badge.
- Stale-context handling covers origin, configuration revision, capabilities,
  history source and identity login. A changed login with identical
  capabilities discards the whole in-flight result. Refreshes are single-flight,
  hidden polling stops, and reconnect/reset/runtime invalidation clears the
  download lists and the All state. Late generations are discarded.

## 3. Development chronology

| Step | Commit | Parent | Scope | Record |
|---|---|---|---|---|
| Baseline | `e64f2b0` | — | predecessor whole closed at production-acceptance-PASS | `02-upload-flow-polish/00_notes.md` |
| Implementation | `cc8f679` | `e64f2b0` | 15 paths: own download status in the companion history sheet | `02_report_00.md` |
| Identity-login correction | `647e6da` | `cc8f679` | 2 paths: bind the aggregation context to the identity login | `02_report_02.md` |
| Download-row correction | `b543602` | `647e6da` | 12 paths: clickable own-media rows, latest-update order, 50/5 window | `04_report_00.md` |
| Compact companion UI | `35c58b6` | `b543602` | 10 paths: Timeline text, one Filter disclosure, My contributions width | `06_report_00.md` |
| Five + All + dedupe | `e9943b5` | `35c58b6` | 11 paths: retained fifty, five compact, one download All, review dedupe | `08_report_00.md` |
| Unread + one All | `2c4f4d8` | `e9943b5` | 9 paths: single All, unread marker, existing opened mutation | `10_report_00.md` |

The whole diff `e64f2b0..2c4f4d8` is exactly 24 paths, +3438/−85. The four
corrections after the implementation were Cooperator-directed closeouts of the
same whole; none opened a new logical whole. The final correction
`e9943b5..2c4f4d8` touches exactly 9 paths.

### 3.1 Independent acceptance rounds

Every acceptance was a fresh independent session with a full C-matrix. No
automatic correction was used.

| Acceptance | Candidate | Controls | Evidence counts |
|---|---|---|---|
| `03_report_00.md` | `647e6da` | C01–C22 PASS | focused Python 46; focused Node 110; broader Python 206; broader Node 64 |
| `05_report_00.md` | `b543602` | C01–C23 PASS | 46; 114; 206; 64 |
| `07_report_00.md` | `35c58b6` | C01–C26 PASS | 46; 114; 206; 64; compact UI 44; affected frontend 287; served-shell 211 |
| `09_report_00.md` | `e9943b5` | C01–C27 PASS | 46; 116; 206; 64; 44; 287; 211 |
| `11_report_00.md` | `2c4f4d8` | C01–C27 PASS | 46; 118; 206; 64; 44; 287; 211 |

`11_report_00.md` records defects none, no MEASURED or LEAD finding, and an
independence statement confirming that the acceptance session implemented none
of the candidate commits.

### 3.2 Publication and deployment rounds

Publication was a normal non-force push on `main`, always followed by a direct
`git ls-remote origin refs/heads/main` readback. Deployment always used the
canonical `deploy/ubuntu/kronika-release` helper.

| Release | Check | Deploy | Status after deploy |
|---|---|---|---|
| `647e6da` | PASS | exit 0 | active/web `647e6da`, service active, DB `0035`, backup ready |
| `b543602` | PASS | exit 0 | active/web `b543602`, service active, DB `0035`, backup ready |
| `35c58b6` | PASS | exit 0 | active/web `35c58b6`, service active, DB `0035`, backup ready |
| `e9943b5` | PASS | exit 0 | active/web `e9943b5`, service active, DB `0035`, backup ready |
| `2c4f4d8` | PASS | exit 0 | active/web `2c4f4d8`, capture unchanged, service active, DB `0035`, backup ready |

Each round ended with terminal `sudo -K` through the operator gate and a
following `sudo -n true` that requires a password, the expected released
lifecycle state. The capture release stayed
`5b86d896b3ea03f89fef2c90f7af2c121d0ef915` throughout.

### 3.3 Rendered acceptance rounds

| Released candidate | Cooperator result | What changed next |
|---|---|---|
| `647e6da` | PARTIAL | Own-media rows must open Details even after read; order by latest update |
| `b543602` | PARTIAL | Companion Timeline text, one Filter button, My contributions width |
| `35c58b6` | PARTIAL | Five compact downloads, one All, sixth/last retained, review dedupe |
| `e9943b5` | PARTIAL | Only one All, unread marker on the matched download row, existing opened mutation |
| `2c4f4d8` | PASS on all six final items | Closed |

Because the extension is unpacked, every rendered round required a manual
reload from `chrome://extensions` plus a refresh of the X/YouTube tabs. The NUC
refresh alone serves only the web shell.

## 4. Decisions and records

- **ADR-0089 — Companion Own Download Status History** (Accepted 2026-11-11):
  added the separate own-download status block to the existing history sheet,
  restricted to the signed-in requester, with a server-owned review badge and
  no second counter.
- **ADR-0090 — Companion Download Row Details and Latest-Update Order**
  (Accepted 2026-11-13): superseded only ADR-0089's inert rows and creation
  ordering. Own-media rows open hosted Details and stay clickable after read;
  null-media rows stay inert; ordering follows the latest request update.
- **ADR-0091 — Companion History Compact Five and All Expansion**
  (Accepted 2026-11-13): five compact downloads, one All, the sixth and later
  retained downloads, complete review history behind the expansion, and review
  rows deduplicated against downloads. Superseded only ADR-0090's at-most-five
  and single-window presentation.
- **ADR-0092 — Companion Download Unread State** (Accepted 2026-11-13): one
  All while downloads exist; review All hidden; the unread marker moves to the
  matched analyzed download row and the existing `REVIEW_INBOX_OPENED` clears
  it. Supplements ADR-0090/0091; their bodies are unchanged.
- Product and user-facing truth was updated in `SPEC.md`, `PRODUCT.md`,
  `SECURITY.md`, `DEVELOPMENT.md`, `docs/X_COMPANION.md` and the ADR index.

The Cooperator-owned amendments, in order, were: clickable own-media rows even
after read; latest-update ordering; compact companion Timeline, one Filter
disclosure and full-width My contributions; compact five with one All, the
sixth/last retained and review dedupe; and finally one All with the unread
marker and opened behavior. The Cooperator explicitly refused separate logical
wholes for these defects and required them fixed inside this whole.

## 5. Evidence at closure

- Repository: local `HEAD`, public `main` and the deployed release are all
  `2c4f4d89375628df28926060aba305e5d80bacff`; the worktree is clean and not
  ahead; no repository mutation after deployment.
- Release: `active_release` and `web_release` `2c4f4d8`; `service_active:
  active`; `database_revision: 0035`; `backup_restore_readiness: ready`;
  capture release unchanged.
- Checks: `ap project check` PASS; `git diff --check` clean; manifest
  unchanged; exactly the declared 24-path whole diff and 9-path final
  correction.
- Tests at the final candidate: focused Python 46; focused Node 118; broader
  Python 206; broader Node 64; compact UI Node 44; affected frontend Node 287;
  served-shell Python 211. All failed counts 0.
- Rendered: six of six final items PASS, declared by the COOPERATOR on the
  deployed `2c4f4d8`.
- Sudo lifecycle: `sudo -K` exit 0; subsequent `sudo -n true` requires a
  password. No host identifier, credential or secret is recorded.

## 6. Residuals outside this whole

These three items were explicitly kept outside the companion history boundary.
None of them is a defect of the delivered download-status surface, and none was
fixed by this whole.

### R-1 — YouTube acquisition `INSPECTION_OUTPUT_LIMIT`

**Observed.** During rendered testing, a YouTube save attempt ended in the
sanitized inspection failure `INSPECTION_OUTPUT_LIMIT`. The request therefore
never produced a catalog media item for that video.

**Where it comes from.** `src/kronika/infrastructure/youtube/downloader.py`
implements `inspect()` with a bounded `yt-dlp --dump-single-json --skip-download`
run. Standard output is capped at `MAX_STDOUT_BYTES = 1_048_576` (1 MiB) and
standard error at `MAX_STDERR_BYTES = 65_536` (64 KiB). If either stream
overflows, the inspection raises `YouTubeInspectionError("INSPECTION_OUTPUT_LIMIT")`
before any download plan, staging or catalog handoff exists.

**Why it is not a companion defect.** The failure happens in acquisition, before
a request can produce the catalog media that the history row would link to.
The companion correctly reflects the request's terminal state and exposes no
provider payload. There is no history-row bug to fix, and adding an inspection
retry or a larger unbounded buffer inside the history surface would be the
wrong layer and a security regression.

**Impact.** That specific video cannot be acquired while other requests are
unaffected. The output caps are a deliberate bounded-run protection; the open
question is whether a legitimate large metadata payload can exceed them and
whether a selective or streamed inspection is the right fix.

**Follow-up needed.** A separate bounded acquisition whole should reproduce the
oversized payload, determine whether the size is legitimate or a pathological
response, and choose between selective/streamed JSON extraction, a justified
bounded increase, or a clearer operator-facing outcome. It must keep the
bounded-run security property, add regression evidence for the bound and error
copy, and avoid unbounded output. The history surface needs no change.

**Disposition.** Open, outside this whole; classified by the COOPERATOR on
2026-11-13 as a separate logical whole. Not fixed here.

### R-2 — X acquisition failures and «Save to Kronika failed»

**Observed.** During rendered testing, some X saves succeeded and some ended as
«Save to Kronika failed». The corresponding history rows correctly showed
`Download failed`. Some X saves succeeded in the same session, so the history
surface itself was functioning.

**Where it comes from.** The X content adapter and `extension/shared/messages.js`
map a terminal acquisition `failed` state to «Save to Kronika failed»; the
sidebar maps the persisted request state `failed` to `Download failed`. Those
are truthful acquisition outcomes, not history-list defects. Distinct branches
already exist for known causes such as `X_REQUEST_INVALID_CATEGORY`,
`X_REQUEST_CATEGORY_CONFLICT`, `network_failed`, `extension_unavailable`,
`empty_response`, ambiguity and `catalog_removed`; the observed generic failure
is a terminal acquisition failure, so the cause lies in the acquisition
pipeline (asset discovery, download or handoff), not in the row rendering.

**Why it is not a companion defect.** The download block is a status surface;
it does not acquire, retry or mutate. It reports what the server persisted. A
companion-side retry or suppression would hide a real failure, and a broader
retry would add an ungranted acquisition behavior.

**Impact.** The affected posts cannot be saved until the acquisition cause is
fixed; their rows remain `Download failed`. No private URL, filename or failure
detail is exposed by the history row.

**Follow-up needed.** A separate bounded acquisition whole should collect the
failing posts (Cooperator-owned, private), the persisted request diagnostics and
the acquisition error breadcrumbs, reproduce the failing discovery/download/
handoff path, and fix the root cause with sanitized errors and no provider
secret exposure. Regression tests belong to the acquisition lifecycle, not to
the history projection.

**Disposition.** Open, outside this whole; classified by the COOPERATOR on
2026-11-14 as a separate acquisition residual/whole, in the same class as R-1.
Not fixed here.

### R-3 — Full-page narrow My contributions title collapse (LEAD)

**Observed.** The companion-hosted My contributions fix was accepted and
rendered PASS. A code-level LEAD remains for the wide/full page below 720 px:
the title can still collapse to one character per line there.

**Where it comes from.** The companion rule
`.kronika-companion-hosted .workspace-media-browser .admin-media-row`
(specificity 0,3,0) forces a single column inside the side panel. On the full
page, `.workspace-media-browser .admin-media-row` (specificity 0,2,0, around
line 5401 of `styles.css`) sets a four-column grid without a width condition and
therefore outranks the later `@media (max-width: 720px) .admin-media-row`
single-column rule (specificity 0,1,0). At narrow full-page widths the desktop
grid survives and the title column can collapse.

**Why it is not a companion defect.** The defect the COOPERATOR reported and
accepted was the companion side panel. The companion-hosted rule is specific
enough and fixes it; the wide page was intentionally left unchanged, including
its glyph table, filters and contributions grid. The remaining narrow full-page
case is a responsive layout issue on a surface this whole touched only for the
companion-hosted presentation.

**Impact.** Cosmetic, only on the full page below 720 px; the companion side
panel is correct. No data, privacy or mutation impact.

**Follow-up needed.** A bounded UI correction should raise the narrow
single-column rule under the workspace wrapper (or reorder it) and rendered-check
My contributions on the wide page below 720 px while preserving the wide
multi-column layout. This is a LEAD, not a confirmed rendered defect.

**Disposition.** Open, outside this whole; recorded in `06_report_00.md` and
retained here. Not fixed here.

### Pre-existing gaps not owned by this whole

`docs/X_COMPANION.md` already lists live signed-in X DOM evidence, the
independent INFOSEC review of the private status bridge and CDN transport,
side-panel iframe framing against live Tailscale Serve or Brave Shields, and
the missing `companion_host.js` origin case as later-grant gaps. This whole did
not change or close them; they are recorded there and are not residuals of the
download-status work.

## 7. Process observations and lessons

1. **Rendered acceptance caught real gaps that tests could not.** Five
   acceptance rounds were clean, yet rendered use still found clickability,
   ordering, compactness, duplicate All and unread-marker gaps. The plan's
   end-state description should have pinned the single-All, complete-expansion
   and unread-marker behavior before implementation.
2. **One misdelivered correction.** `02_correction_01.md` was delivered to a
   different session and returned `02_report_01.md` BLOCKED with no change. The
   reissued `02_correction_02.md` succeeded. Lesson: verify the recipient
   session identity and coordinates before dispatch, and preserve the blocked
   report as history.
3. **Empty report-path collision.** `08_report_00.md` already existed as an
   empty file; the Worker correctly refused to overwrite it and returned the
   complete report, which the COOPERATOR persisted. The collision is a delivery
   fact, not a content defect. Report paths should be checked as reserved before
   dispatch.
4. **Foreign artifact.** `02_rereport_00.md` was not part of this candidate and
   is absent from the repository. Foreign trace artifacts must not be adopted
   into a candidate or cited as evidence.
5. **Exit 20 was not a transport outage.** `kronika-release status` failed with
   exit 20 after the previous deployment's `sudo -K`, which looked like an
   unreachable NUC. The operator gate reached the host and `sudo -n true`
   showed that only the Cooperator timestamp was missing. Reachability and
   sudo state should be probed separately before declaring a host outage.
6. **The unpacked extension needs a manual reload.** Every published revision
   required a `chrome://extensions` reload and a source-tab refresh before
   rendered acceptance. The NUC refresh alone serves the web shell. This should
   be stated in every rendered handoff.
7. **Scope discipline held.** Acquisition failures were kept out of the history
   whole, no new permission or mutation was added, and the badge stayed
   review-only throughout.

## 8. Closure record

```text
Phase-qualified result: production-acceptance-PASS (Cooperator-declared)
Result artifact or commit: 2c4f4d89375628df28926060aba305e5d80bacff
Result evidence: Cooperator rendered PASS on all six final items at 2c4f4d8;
  fresh independent acceptance-PASS 11_report_00.md C01–C27; focused Python
  46; focused Node 118; broader Python 206; broader Node 64; compact UI Node
  44; affected frontend Node 287; served-shell Python 211; ap project check
  PASS; git diff --check clean; manifest unchanged; publication-PASS and NUC
  deployment-PASS at 2c4f4d8 with active/web 2c4f4d8, capture unchanged,
  service active, database revision 0035 and backup restore-readiness ready
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — original four choices, download-row
  amendments, compact UI, five/All expansion, unread marker and one-All
  correction, publication and deployment authorization, and the final
  rendered PASS
Residual-risk disposition: satisfied for this whole — R-1 YouTube inspection
  output limit, R-2 X acquisition failures and R-3 the full-page narrow My
  contributions LEAD remain open, out-of-scope candidates, not defects of this
  companion whole
Upgrade-ledger reconciliation: complete — entry
  consumer-declared-execution-and-capability-route-binding remains accepted,
  non-authorizing, retain-active; no ledger mutation
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

The run map entry remains for the run-scoped Orchestrator to refresh from this
whole's evidence. No repository, host or trace mutation occurred after the
recorded deployment and rendered acceptance.

## 9. Trace inventory

| File | Role |
|---|---|
| `00_handout.md` | Frozen provisional seed |
| `00_notes.md` | Chronological Orchestrator record, frozen at closure |
| `01_planning_00.md` | Planner prompt |
| `01_report_00.md` | Accepted decision-complete plan |
| `02_implementation_00.md` | Implementation prompt |
| `02_report_00.md` | Implementation PASS at `cc8f679` |
| `02_correction_01.md` | Identity-login correction prompt (misdelivered) |
| `02_report_01.md` | BLOCKED delivery; no repository change |
| `02_correction_02.md` | Reissued identity-login correction |
| `02_report_02.md` | Correction PASS at `647e6da` |
| `02_correction_03.md` | Prepared download-row correction; not issued |
| `03_acceptance_00.md` / `03_report_00.md` | Fresh acceptance of `647e6da` |
| `04_correction_00.md` / `04_report_00.md` | Clickable rows and latest-update correction at `b543602` |
| `05_acceptance_00.md` / `05_report_00.md` | Fresh re-acceptance of `b543602` |
| `06_correction_00.md` / `06_report_00.md` | Compact companion UI correction at `35c58b6` |
| `07_acceptance_00.md` / `07_report_00.md` | Fresh re-acceptance of `35c58b6` |
| `08_correction_00.md` / `08_report_00.md` | Five/All/dedupe correction at `e9943b5` |
| `09_acceptance_00.md` / `09_report_00.md` | Fresh re-acceptance of `e9943b5` |
| `10_correction_00.md` / `10_report_00.md` | Unread/one-All correction at `2c4f4d8` |
| `11_acceptance_00.md` / `11_report_00.md` | Fresh re-acceptance of `2c4f4d8`; C01–C27 PASS |
| `12_closure.md` | This final closure record |

Coordinates `02/04` were not consumed because `02_correction_03.md` was not
issued. `02_rereport_00.md` is not part of this trace and is absent from the
repository. All candidate commits remain in public `main` history; the whole
tree is deployed at `2c4f4d8`.

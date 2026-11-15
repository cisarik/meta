# 06 — Closure: YouTube inspection boundary

```text
Logical whole identity: youtube-fixes
Development run identity: kronika-run-01
Orchestrator session scope: logical-whole
Opened: 2026-11-14
Closed: 2026-11-14
Baseline: 2c4f4d89375628df28926060aba305e5d80bacff
Final candidate: eb5af0e49729eaf87eb3210ce0fd87295daae826
Governing AP: d7023cf037f6d17885c3ede5c04812c61640da50
Delivery route: manual Cooperator delivery
Repository: https://github.com/cisarik/kronika
Logical-whole closure: closed-by-ORCHESTRATOR
Phase-qualified result: production-acceptance-PASS (Cooperator-declared for the inspection boundary; R-4 residual)
```

This is the final trace document for the whole. It records the delivered
inspection-boundary behavior, the development history, the evidence at closure,
the residual R-4 that moved the specific video to a new download-stage failure,
and the process lessons. `00_notes.md` remains the chronological Orchestrator
record and is frozen at closure.

## 1. Outcome in brief

The whole replaced the full `yt-dlp --dump-single-json` inspection dump with a
two-line `--print` projection of exactly the metadata and format fields the
server consumes. It kept the 1 MiB stdout and 64 KiB stderr inspection caps,
added inspection-only early termination at either cap, and separated the
inspection constants from the unchanged download constants. It did not change
the `yt-dlp==2026.7.4` pin, the download path, the failure stage, the
`INSPECTION_OUTPUT_LIMIT` code, the operator JSON fields, or the companion
`Download failed` status.

The live rendered attempt on the previously failing video no longer failed at
inspection. It advanced to the download stage and failed with the sanitized
`DOWNLOAD_FAILED` code; metadata and publication remain not cataloged. The
inspection boundary is therefore fixed and proven, while the specific video
remains unacquirable at a different stage. That download-stage failure is
recorded as new residual R-4 and is the subject of the successor logical whole
`youtube-download-failure`.

## 2. Delivered behavior

- `YtDlpYouTubeDownloader.inspect()` now runs the isolated module entry point
  with `--simulate`, `--no-write-info-json`, one `--print` metadata template
  and one `--print` formats template, then the URL after `--`. It no longer
  uses `--dump-single-json` or `--skip-download`.
- The metadata template projects exactly the fields
  `_inspection_from_payload()` validates. The formats template projects
  exactly the fields `_select_plan()` consumes. It excludes URLs, fragments,
  captions, thumbnails, heatmaps, chapters, comments and descriptions.
- `_projected_inspection_document()` requires exactly two non-empty lines:
  one JSON object without `formats`, then one JSON list or `NA`. A formats-line
  `NA` becomes an empty list and preserves `NO_VISUAL_STREAM`; a metadata-line
  `NA` is `INSPECTION_INVALID_OUTPUT`.
- `_capture_stream()` gained an inspection-only `stop_after_limit` path;
  `_run_bounded()` gained an inspection-only `terminate_on_overflow` path that
  cancels the other capture, uses the existing process-group TERM/KILL helper,
  and returns the overflow flags. `inspect()` checks overflow before the
  return code, so an overflowed killed child is `INSPECTION_OUTPUT_LIMIT`.
- Download and version attestation keep the read-to-EOF capture, the existing
  `MAX_STDOUT_BYTES` and `MAX_STDERR_BYTES` names and values, and
  `DOWNLOAD_OUTPUT_LIMIT` after process exit without a kill-on-overflow path.
- `SPEC.md` records the inspection-only projection, the caps, the termination
  and the fail-closed `INSPECTION_OUTPUT_LIMIT` outcome in the existing
  owner-operated YouTube paragraph.
- No pin, schema, migration, API, CLI, companion, extension, permission,
  provider or deployment change was made.

## 3. Development chronology

| Step | Record | Result |
|---|---|---|
| Opening and revalidation | `00_notes.md` | Handout adopted; Stage 1 verified; no material stale fact |
| Planning | `01_planning_00.md` / `01_report_00.md` | Decision-complete plan; route 2 selected; two binding corrections identified in review |
| First implementation attempt | `01_implementation_01.md` / `01_report_01.md` | Delivery mismatch: report byte-identical to `01_report_00.md`; repository unchanged; rejected |
| Fresh implementation | `02_implementation_00.md` / `02_report_00.md` | Implementation PASS at `eb5af0e`, four paths, 48 focused tests |
| Independent acceptance | `03_acceptance_00.md` / `03_report_00.md` | Acceptance PASS, C01-C29 PASS, independence holds |
| Publication | `04_publication_00.md` / `04_report_00.md` | Publication PASS; `2c4f4d8..eb5af0e`; public `main` `eb5af0e` |
| NUC deployment | `05_deployment_00.md` / `05_report_00.md` | Deployment PASS; active/web `eb5af0e`; service active; DB `0035`; backup ready; capture unchanged; terminal `sudo -K` |
| Rendered acceptance | `00_notes.md` | One live attempt; stage `download`; `DOWNLOAD_FAILED`; inspection limit gone; R-4 |

The whole diff `2c4f4d8..eb5af0e` is exactly four paths, +957/−32. No
repository mutation occurred after the candidate commit.

## 4. Evidence at closure

- Repository: local `HEAD`, public `main` and the deployed release are all
  `eb5af0e49729eaf87eb3210ce0fd87295daae826`; worktree clean; branch tracks
  `origin/main`; `.ap` gitlink and submodule `HEAD` are `d7023cf`.
- Candidate: exactly four changed paths; `git diff --check` clean.
- Focused tests at the candidate: 48 passed, 0 failed, through
  `./.ap/ap exec --baseline 2c4f4d8 --operation test-focus` on the unit
  downloader and integration acquisition lifecycle files.
- Independent acceptance: `03_report_00.md`, C01-C29 PASS, no correction.
- Publication: normal non-force push `2c4f4d8..eb5af0e`; direct
  `git ls-remote origin refs/heads/main` readback `eb5af0e`.
- Deployment: pre-deploy active/web `2c4f4d8`; `check --release eb5af0e`
  PASS; one deploy exit 0; post-deploy active/web `eb5af0e`; service active;
  database revision `0035`; backup restore readiness ready; capture release
  `5b86d896b3ea03f89fef2c90f7af2c121d0ef915` unchanged.
- Sudo lifecycle: terminal `sudo -K` exit 0; subsequent `sudo -n true`
  requires a password, the expected released state.
- Rendered: one live attempt on the previously failing video; the claim passed
  inspection and failed at stage `download` with sanitized `DOWNLOAD_FAILED`;
  metadata and publication are not cataloged. No URL, title, channel, filename
  or claim identifier was recorded. No retry was made.
- No repository, host or trace mutation occurred after the deployment and the
  rendered attempt. Meta Git archival remains with the COOPERATOR.

## 5. Residuals

### R-1 — fixed

The inspection `INSPECTION_OUTPUT_LIMIT` failure is resolved by the projection
and acknowledged by the live stage transition. The inspection boundary retains
the 1 MiB/64 KiB caps and now terminates the inspection child at the cap. The
specific video no longer fails at inspection.

### R-4 — new, successor whole

The same video now fails at stage `download` with the generic sanitized
`DOWNLOAD_FAILED` code. The candidate did not change the download path, and
the projected format plan is the existing selector's plan. The underlying
yt-dlp cause is not persisted or exposed. The video remains unacquirable. The
smallest next step is a bounded diagnostic/acquisition whole, not an unbounded
retry. The successor handout is
`/Users/agile/meta/projects/kronika/01/11-youtube-download-failure/00_handout.md`.

### R-2 — X acquisition failures

Unchanged and outside this whole. Some X saves still end as «Save to Kronika
failed»; the companion history correctly shows `Download failed`.

### R-3 — full-page narrow My contributions title collapse

Unchanged and outside this whole. The companion side panel is correct; the
wide page below 720 px remains a code-level LEAD.

## 6. Process observations and lessons

1. **Selective projection was the right route.** The full dump carried
   caption, storyboard and format bulk the consumer never reads. The
   projection keeps the existing caps truthful and does not widen the parent
   memory or the download path.
2. **Plan naming can outlive the code.** The plan called the over-cap format
   outcome `FINAL_SIZE_LIMIT`, while `_select_plan` actually raises
   `COMPATIBLE_FORMAT_UNAVAILABLE` before that post-selection check. The
   implementation preserved the selector; the acceptance confirmed the plan
   naming was historical, not a candidate defect.
3. **A byte-identical planning report is a delivery mismatch, not an
   implementation.** The first implementation exchange returned
   `01_report_01.md` identical to `01_report_00.md`; the repository was
   unchanged. The exchange was rejected, the artifact preserved, and a fresh
   session `02/01` completed the implementation.
4. **Native Plan Mode can block the Planner report write.** The first Planner
   returned its complete plan in the plan output; the COOPERATOR persisted it
   at the exact trace path. The completion route was not needed.
5. **The deployment prompt must separate the local helper from the remote
   gate.** `deploy/ubuntu/kronika-release` is the local canonical entry point;
   the NUC gate carries the probe and the bounded sudo commands. The
   deployment succeeded; the next deployment prompt should state the split
   explicitly.
6. **One live attempt is evidence, not a retry loop.** The rendered attempt
   consumed one failed-request slot and proved the inspection boundary. A
   retry without new evidence would not be progress.
7. **Close the boundary, open the next whole.** The inspection fix did not
   acquire the video. The honest result is a separate download-stage residual,
   not a reason to widen this whole after its acceptance.

## 7. Closure record

```text
Phase-qualified result: production-acceptance-PASS (Cooperator-declared for the inspection boundary; R-4 residual)
Result artifact or commit: eb5af0e49729eaf87eb3210ce0fd87295daae826
Result evidence: independent acceptance-PASS 03_report_00.md C01-C29;
  48 focused tests; publication-PASS at eb5af0e; NUC deployment-PASS with
  active/web eb5af0e, service active, database revision 0035, backup ready
  and capture unchanged; one rendered live attempt moved the failure from
  inspection INSPECTION_OUTPUT_LIMIT to download DOWNLOAD_FAILED
Required preceding results: satisfied
Cooperator-owned decisions: satisfied — route 2, D1-D7, the two binding
  corrections, publication, NUC deployment, and the decision to open the
  successor download-failure whole
Residual-risk disposition: satisfied for this whole — R-1 fixed; R-4 open in
  the successor whole; R-2 and R-3 remain outside and unchanged
Upgrade-ledger reconciliation: complete — entry
  consumer-declared-execution-and-capability-route-binding remains accepted,
  non-authorizing, retain-active; no ledger mutation
Active mutation: none
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

The run map remains stale at entry 03 `provisional` and entry 04
`household-onboarding` and is not updated by this logical-whole session. A
run-scoped Orchestrator must reconcile it from the closure evidence and the
COOPERATOR's successor decision. The successor whole is not selected or opened
by this closure; its provisional handout is a seed, not authority.

## 8. Trace inventory

| File | Role |
|---|---|
| `00_handout_00.md` | Frozen provisional seed |
| `00_notes.md` | Chronological Orchestrator record, frozen at closure |
| `01_planning_00.md` / `01_report_00.md` | Planner prompt and accepted decision-complete plan |
| `01_implementation_01.md` / `01_report_01.md` | First implementation prompt and byte-identical planning-report mismatch, preserved |
| `02_implementation_00.md` / `02_report_00.md` | Fresh implementation prompt and Implementation PASS at `eb5af0e` |
| `03_acceptance_00.md` / `03_report_00.md` | Fresh independent acceptance; C01-C29 PASS |
| `04_publication_00.md` / `04_report_00.md` | Publication prompt and Publication PASS at `eb5af0e` |
| `05_deployment_00.md` / `05_report_00.md` | Deployment prompt and Deployment PASS at `eb5af0e` |
| `06_closure.md` | This closure record |

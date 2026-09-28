# Kronika one product — S6-A35-F01 correction independent E3/R3 re-audit

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 39
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S6-A35-F01-REAUDIT
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — independent authorization re-audit of a household read boundary on the corrected S6 candidate; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement or correct any
part of the S6 candidate or its correction and inherits no implementation
reasoning. Declare your actual independence posture. Prior plans, reports and
trace artifacts are evidence, not authority; inherited implementation reasoning
is disqualifying. You do not correct anything: findings are reported, never
fixed, and a correction is a separate grant. Do not contact any host, call any
provider, read credentials or `private/**`, use a browser, or ask another
session. No subagents. The client must be write-capable (Plan mode OFF) for
report persistence.

Testing economy is explicit for this exchange: do not run the broad/full suite
and do not re-run the predecessor's 96-file focused list. Run only the selected
security subset and the bounded probes below. Never re-run an unchanged gate.

## Acceptance and Correction Record

```text
Acceptance candidate: 0d0d8c88bf88bf8454751a0205bc8652374796c2
  (tree 96adead05beb58f2e282ff77b9e6d29bff2c8298, branch feat/kronika-one-product,
   parent 5843486ddeae13ec5b331f102c5cb595bfa6e386)
Acceptance owner map: the correction delta 5843486..0d0d8c8 (14 paths, listed
  below); predecessor S6 candidate 38e7beeb3921d7c0fd8e717e480754fbd18130c9 and
  its acceptance 35_report_00.md; correction grants/reports 38_correction_00.md,
  38_correction_01.md, 38_report_00.md, 38_report_01.md; frozen plan
  33_report_00.md; ADR-0083
Acceptance allowlist: read-only review of the candidate, governing AP and named
  evidence; the declared focused route; one declared temporary probe root under
  /tmp/kronika-one-product-s6-reaudit (mode 0700, synthetic data only)
Acceptance risk claims: the eight fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: approved cover bytes/ETag and gallery preview of
  a post-approval location (claims 4 and 6)
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance, 2026-09-28)

- FrameNest checkout `/Users/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `0d0d8c88bf88bf8454751a0205bc8652374796c2`, parent
  `5843486ddeae13ec5b331f102c5cb595bfa6e386`, tree
  `96adead05beb58f2e282ff77b9e6d29bff2c8298`, subject
  `fix(kronika): serve approved projections on household reads`; clean index and
  worktree; the corrected candidate is committed but not pushed.
- Local `main` = `origin/main` = `40e51cb2…`; public `refs/heads/main` of
  `https://github.com/cisarik/framenest.git` = `40e51cb2…`; public
  `feat/kronika-one-product` is still the uncorrected transport `38e7bee…`; the
  two other public heads are unchanged (`26d28b16…`, `7ff6546f…`).
- AP pin `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (gitlink and `.ap` HEAD;
  this pin carries the macOS project-execution portability fix adopted in
  `5843486…`; the canonical route runs natively on this host; do not modify
  `.ap`).
- Migration head remains `0034_kronika_records.py`; no `0035`.
- The four parked broad-suite failures (stale `.venv` console script; three
  operator SSH-gate parameters) stay disposed pre-existing debt; do not re-run
  or repair them.
- `private/**` is never read. No host, SSH, gate, sudo, service, browser,
  provider, credential or network action. Never print a secret-shaped value.

Required reading: governing WORKER spine; RF-05 and RF-07; the Worker Report
Header and Acceptance and Correction Record in `.ap/PROMPT_CONTRACTS.md`;
`.ap/INFOSEC.md` (R3 route, sections 3 and 4.2/4.4–4.7, plus its finding,
containment and residual-risk rules); the predecessor finding
(`35_report_00.md`); the correction grant pair (`38_correction_00.md`,
`38_correction_01.md`) and the correction reports (`38_report_00.md`,
`38_report_01.md`); the frozen plan (`33_report_00.md` sections 4 and 7);
`ADR-0083`; the correction diff.

## Fixed claims

1. **Candidate identity and containment.** The exact SHA, parent, tree and
   subject match; `git diff --name-status 5843486… HEAD` is exactly the 14 paths
   below, every one inside the whole's effective allowlist (the 176-path union
   of `33_report_00.md` section 6 plus `tests/support/youtube_fake_demo.py` and
   `tests/contract/test_youtube_fake_demo.py`); no protected path (`AGENTS.md`,
   `.ap`, `pyproject.toml`, `poetry.lock`, `docs/AP_UPGRADE_OBSERVATIONS.md`,
   migration history) changed; the worktree is clean; nothing was pushed; the
   AP pin is unchanged; migration head is still 0034; no dependency change; a
   leak hunt over the correction diff finds no credential or secret value, no
   raw provider payload or reasoning stream, no document text, SQL parameter or
   private content in errors, logs or responses.
2. **S6-A35-F01 disproved dynamically.** Independently reproduce the finding's
   scenario with synthetic callers (alice owner, bob household member, ada
   administrator): approve media as title `TitleA` / category `general` /
   family; change the working state to title `TitleB` / category `meme` /
   collection `processed` and add a new location. Then Bob must observe:
   `GET /api/media/{id}` and `/metadata` serve `TitleA` / `general` from the
   approved snapshot; the detail payload contains no post-approval location id
   and no working-state value; `GET /api/media/{id}/locations/{new}/content` and
   `.../download` return `404 MEDIA_CONTENT_NOT_FOUND` without opening,
   probing or caching any file; the gallery list contains the approved record
   without any `media_content_publications` row, with total/limit/offset
   consistent; `collection=processed` does not match it; `content_category=general`
   includes it and `content_category=meme` excludes it.
3. **R5 semantics preserved.** An approved location remains a valid target with
   the existing semantics (`409 MEDIA_CONTENT_UNAVAILABLE` for a genuinely
   unavailable approved location; range behavior unchanged), while a
   non-approved location is denied before any resolver or cache open and its
   denial is indistinguishable from an unknown location.
4. **R6 cover, dynamically demonstrated (named missing evidence).** With a
   synthetic approved cover artifact whose digest differs from the current
   cover, a household `cover-thumbnail` request serves the approved artifact's
   bytes and ETag; when that artifact is missing, the route returns `404` and
   never falls back to the current cover; owner/administrator cover routes stay
   unchanged. Demonstrate with synthetic bytes under the declared probe root.
5. **R7 analysis and suggestions (LEAD).** Approve a parser-accepted stored
   result, then change the working analysis. Household
   `automatic-analysis`, `movie-identification` and `ai-suggestions` expose only
   the approved snapshot (or the existing absent representation); no current
   analysis title or text is disclosed anywhere in those bodies; suggestion
   cursor semantics remain truthful.
6. **R8 gallery preview (named missing evidence).** For approved, a
   post-approval location returns the same `404` as an unknown location and no
   preview is produced; an approved location's preview behavior is exercised;
   nothing is previewed from a non-approved location.
7. **Non-weakening and unchanged behavior.** The decision gate still fails
   closed on missing policy, missing identity or repository failure; owner
   `current`, `legacy`, `deny`, anonymous and public-composition behavior is
   unchanged; the public composition still excludes every bound record even
   with a stray legacy publication row; the administrator approval gate and the
   write routes are unchanged; no new endpoint, schema, migration or
   dependency is introduced.
8. **Inventory and route-set stability.** `tests/contract/test_kronika_access_inventory.py`
   passes and `docs/KRONIKA_ACCESS_INVENTORY.md` remains truthful for the
   actual route set; the correction introduces no new access surface and no
   route disappears.

## Fixed control matrix

Positive controls, run from the repository root with the declared route bound
to the candidate:

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
git diff --name-status 5843486ddeae13ec5b331f102c5cb595bfa6e386 HEAD
git status --porcelain
git log --oneline -3

./.ap/ap project check --root /Users/agile/Projects/framenest --baseline 0d0d8c88bf88bf8454751a0205bc8652374796c2

./.ap/ap exec --root /Users/agile/Projects/framenest --baseline 0d0d8c88bf88bf8454751a0205bc8652374796c2 --operation test-focus -- \
  tests/contract/test_kronika_approved_projection.py \
  tests/contract/test_media_catalog_api.py \
  tests/contract/test_media_metadata_api.py \
  tests/contract/test_media_content_api.py \
  tests/contract/test_media_catalog_repository.py \
  tests/contract/test_gallery_preview_api.py \
  tests/contract/test_cover_api.py \
  tests/contract/test_media_analysis_lifecycle_api.py \
  tests/contract/test_media_ai_suggestions_api.py \
  tests/contract/test_content_audience_policy.py \
  tests/contract/test_public_published_uds.py \
  tests/contract/test_kronika_record_authorization.py \
  tests/contract/test_kronika_access_inventory.py \
  tests/unit/application/test_media_catalog.py \
  tests/integration/persistence/test_kronika_record_repository.py \
  -q -p no:cacheprovider
```

Negative and adversarial controls: use synthetic fixtures and disposable
databases under the declared probe root only; run temporary synthetic pytest
probe files through the declared route if the route accepts them, and report
honestly as unverified any control the route cannot execute instead of using
ambient Python. Cover at least:

- The exact claim-2 household matrix, including the post-approval location id
  from the detail payload and the content/download denial for it.
- Cover bytes and ETag for the approved digest with a different current cover,
  and the missing-artifact `404` without fallback (claim 4).
- Gallery preview for a post-approval location (claim 6).
- Denial before open for content, download and preview: the synthetic resolver
  and preview services observe no open for denied locations.
- Fail-closed denial: missing policy and missing identity deny; anonymous and
  public-composition reads exclude bound records with a stray legacy
  publication row.
- Approval adversarial sanity: an ordinary caller cannot approve; a stale
  version or stale digest conflicts (reuse the frozen suite for the deep
  transaction semantics; probes focus on the household surface).
- Leak hunt over the 14-path diff and over the probed responses.

State every observed result with exact evidence; unverified controls are
reported as unverified, never as PASS. Findings use the full INFOSEC finding
structure (evidence class, reachability, preconditions, privilege, impact,
containment, residual risk).

## Correction diff under audit

```text
src/framenest/adapters/api/content_audience_api.py
src/framenest/adapters/api/cover_api.py
src/framenest/adapters/api/gallery_preview_api.py
src/framenest/adapters/api/media_analysis_lifecycle_api.py
src/framenest/adapters/api/media_catalog_api.py
src/framenest/adapters/api/media_content_api.py
src/framenest/adapters/api/media_metadata_api.py
src/framenest/application/media_catalog.py
src/framenest/application/media_cover.py
src/framenest/application/ports/media_catalog_repository.py
src/framenest/application/ports/records.py
src/framenest/infrastructure/persistence/media_catalog_repository.py
src/framenest/infrastructure/persistence/record_repository.py
tests/contract/test_kronika_approved_projection.py
```

## Authority and containment

Positive authority: read-only inspection of the candidate, governing `.ap` and
the named trace evidence; the declared route with the candidate baseline;
creation, use and cleanup of one declared temporary probe root under `/tmp`
(mode 0700, synthetic data only); the terminal report write at the exact
destination when absent, with full readback.

Negative authority: no product, test, documentation, configuration, AP,
packaging or migration edit; no correction; no host, SSH, gate, sudo, service,
browser, provider, credential or network action; no push or publication; no new
dependency; no subagent; no `private/**`; no Meta commit.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity, candidate or git-state mismatch;
an unusable declared route; a probe exceeding the authorized effects; sensitive
output; or a required control that cannot be established without a forbidden
mutation. Preserve the first causal failure; missing evidence is never PASS. A
second equivalent cycle for the same unchanged blocker requires
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## Evidence selection

```text
Evidence tier: E3
Evidence tier basis: security/trust boundary (household read of the approved projection) on the corrected S6 candidate; dynamic probes include the predecessor's named missing evidence
Activated stricter profile: INFOSEC.md — R3 route (fresh focused audit)
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the selected security subset above
Affected tests: the 14-path correction delta
New causal regression: none — this is acceptance
Broad or full suite: not-used — do not re-run
Runtime or testbed: declared route plus the declared synthetic probe root; no host
Independent acceptance: required-separate-fresh-worker (this exchange)
```

## Completion and report contract

`PASS` means every fixed claim is independently established and no blocking
finding remains. Use `Phase-qualified result: acceptance-PASS` only for a PASS;
otherwise `not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: final-acceptance`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 39, exchange 01) exactly once. Include the compact
core; the completed Acceptance and Correction Record; per-claim verdicts with
exact evidence; the control matrix with observed counts and exit codes;
adversarial outcomes; findings with the full structure; containment and probe
cleanup; residual risk and limitations; one smallest next step (a separate
Cooperator publication grant for the accepted corrected candidate); the
critique block; and the authority-expiry statement.

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. If the report write is blocked by the client,
preserve the complete content in the client output and report the missing
delivery truthfully. Terminal report or cancellation expires this authority.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 39_acceptance_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 39_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

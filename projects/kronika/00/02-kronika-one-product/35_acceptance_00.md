# Kronika one product — S6 independent E3/R3 authorization acceptance

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 35
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: KRONIKA-ONE-PRODUCT-S6-ACCEPTANCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — security-boundary, durable-migration and private-state acceptance of the S6 authorization candidate; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: yes — required-fresh-independent

## Session and independence declaration

This must be a genuinely fresh session that did not implement or correct any
part of the S6 candidate and inherits no implementation reasoning. Declare your
actual independence posture. Prior plans, reports and trace artifacts are
evidence, not authority; inherited implementation reasoning is disqualifying.
You do not correct anything: findings are reported, never fixed, and a
correction is a separate grant. Do not contact any host, call any provider,
read credentials or `private/**`, use a browser, or ask another session. No
subagents.

Testing economy is explicit for this exchange: the broad/full suite and the
96-file focused list were already run once for this exact candidate (only the
four parked pre-existing cases fail). Do not re-run them. Run only the
selected security subset and bounded probes below.

## Acceptance and Correction Record

```text
Acceptance candidate: 38e7beeb3921d7c0fd8e717e480754fbd18130c9
  (tree d6d5d314bfaf98d968235a867004b89b3187ac68, branch feat/kronika-one-product,
   parent 40e51cb2d061ead96850c9c94aa59de54d5e1310)
Acceptance owner map: the S6 row delta 40e51cb2..38e7bee (109 paths = the
  verified 176-path allowlist of 34_implementation_00.md, equal to
  33_report_00.md section 6, plus tests/support/youtube_fake_demo.py and
  tests/contract/test_youtube_fake_demo.py); implementation reports
  34_report_00.md..34_report_04.md; frozen plan 31_report_00.md,
  32_report_00.md, 33_report_00.md; ADR-0083
Acceptance allowlist: read-only review of the candidate, governing AP and
  named evidence; the declared focused route; one declared temporary probe root
  under /tmp/kronika-one-product-s6-acceptance (mode 0700, synthetic data only)
Acceptance risk claims: the seven fixed claims below
Acceptance control matrix: the fixed positive and negative controls below
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

## Starting state (verified at issuance, 2026-09-27)

- FrameNest checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `38e7beeb3921d7c0fd8e717e480754fbd18130c9`, parent
  `40e51cb2d061ead96850c9c94aa59de54d5e1310`, tree
  `d6d5d314bfaf98d968235a867004b89b3187ac68`; clean index and worktree; the
  candidate is committed but not published.
- Local `main` = `origin/main` = `40e51cb2…`; the candidate sits on the working
  branch only. AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- Migration `0034_kronika_records.py` is the candidate head; the baseline head
  was `0033`.
- The four parked broad-suite failures (stale `.venv` console script and three
  operator SSH-gate parameters influenced by ambient environment variables)
  are disposed pre-existing debt outside the allowlist; do not re-run or repair
  them.
- `private/**` is never read. No host, SSH, gate, sudo, service, browser,
  provider or credential action. Never print a secret-shaped value.

Required reading: governing WORKER spine; RF-05 and RF-07; the Worker Report
Header and Acceptance and Correction Record in `.ap/PROMPT_CONTRACTS.md`;
`.ap/INFOSEC.md` (R3 route, sections 3 and 4.2/4.4–4.7, plus its
finding/evidence, containment and residual-risk rules); the frozen plan
(`31_report_00.md` sections 3, 4, 6, 9, 10; `32_report_00.md`; `33_report_00.md`
sections 2–7); `ADR-0083`; the implementation reports.

## Fixed claims

1. **Records, documents and migration 0034.** `kronika_documents` and
   `kronika_records` (plus the three approved-projection tables) match the
   frozen column, constraint and index design; UUID identity versus bounded
   non-UUID `operation_id`; immutable completed Q/A documents; server-derived
   owner and initial `private`; separate creation/completion/first-Timeline
   timestamps; composite document FK; media versus search/research shape
   checks; upgrade creates no common records and preserves a populated
   synthetic 0033 catalogue; populated downgrade refuses before DDL; empty
   downgrade/re-upgrade works; no application operation changes an owner or a
   completed document.
2. **Centralized fail-closed authorization.** `content_audience_allows` denies
   when policy or verified identity is absent, before any permissive path;
   typed read scope with missing scope denying; SQL restricts membership before
   count/search/facets/pagination and before file opens; bound-record ownership
   overrides legacy contribution/publication claims for every reader;
   cross-owner denial is indistinguishable from unknown; administrator read-all
   is explicit server-derived capability; personal history, administrator
   inventory and approved-only Timeline stay separated.
3. **Approval, withdrawal and approved projections.** Approval and withdrawal
   use `BEGIN IMMEDIATE` with administrator authority, expected version,
   validated completion, and a digest of the complete projection rechecked in
   the write transaction; stale token/digest conflicts; exact replay may
   no-change; withdrawal retains the document, projection, provenance and
   first Timeline-entry time; reapproval keeps the card's position; household
   members read the approved snapshot while owner/administrator read current
   state; metadata, cover, companion-review apply and successful-analysis
   writers bump an already-bound record's version; legacy publish/unpublish and
   media removal refuse a bound record inside the write transaction before
   receipt insertion, detachment or filesystem cleanup.
4. **Identity, upload and acquisition closures (G1).** The configured local
   owner is produced only for actual loopback/operator-UDS access through the
   identity mapping, never from client fields or proxy headers and never in the
   public composition; upload creation/session/duplicate/linked-media
   closures; YouTube requester/reuse; X requester/assets; operator routes
   require configured identity with `youtube.acquire`; analysis proposals
   check authorization inside the insertion transaction; internal recovery
   operations use persisted provenance; administrator duplicate resolution is
   preserved for `upload.manage` (handoff and byte-duplicate resolver) while
   ordinary requesters stay `SILENT_KEEP_SEPARATE`.
5. **Private catalog lifecycle (G3).** New database directory `0700` and file
   `0600` without overwriting; existing directory/DB/WAL/SHM/journal type,
   owner and mode validation; symlink and multi-hardlink refusal; unsafe
   objects rejected without `chmod`; lazy engine; read-only access creates
   nothing; auxiliary files protected; no global `umask` change; sanitized
   errors without documents, SQL parameters or private content;
   backup/restore preserves new tables and private permissions.
6. **Public exclusion and legacy compatibility.** Public composition and direct
   public queries exclude every common record including `family`, even with a
   stray legacy publication row, before any list total, tag, detail or byte
   output; authorized legacy fixture behavior is preserved; internet
   publication remains disabled.
7. **Inventory and containment.** `docs/KRONIKA_ACCESS_INVENTORY.md` and
   `tests/contract/test_kronika_access_inventory.py` enumerate the actual
   methods from both compositions and workspace route policies; every content
   route maps to a specific positive and negative behavioral test with no
   generic placeholder; the operator YouTube rows state the required
   configured identity and capability. The candidate diff is exactly 109 paths
   inside the effective allowlist; it contains no outside path; production code
   changes are confined to the S6 design; S4-A files, historical migrations,
   `.ap` and the managed block are unchanged; nothing was pushed.

## Fixed control matrix

Positive controls, run from the repository root with the declared route bound
to the candidate:

```text
git rev-parse HEAD 'HEAD^{tree}' 'HEAD^'
git diff --name-status 40e51cb2d061ead96850c9c94aa59de54d5e1310 HEAD
git status --porcelain
git log --oneline -2

./.ap/ap project check --root /home/agile/Projects/framenest --baseline 38e7beeb3921d7c0fd8e717e480754fbd18130c9

./.ap/ap exec --root /home/agile/Projects/framenest --baseline 38e7beeb3921d7c0fd8e717e480754fbd18130c9 --operation test-focus -- \
  tests/contract/test_kronika_record_authorization.py \
  tests/contract/test_kronika_acquisition_authorization.py \
  tests/contract/test_kronika_approved_projection.py \
  tests/contract/test_local_record_identity.py \
  tests/contract/test_kronika_access_inventory.py \
  tests/integration/persistence/test_kronika_records_migration.py \
  tests/unit/infrastructure/persistence/test_private_state.py \
  tests/contract/test_content_audience_policy.py \
  tests/contract/test_public_published_uds.py \
  tests/contract/test_upload_api.py \
  tests/contract/test_youtube_operator_api.py \
  tests/contract/test_requester_private_youtube_details.py \
  tests/contract/test_x_request_api.py \
  tests/contract/test_catalog_removal_api.py \
  tests/contract/test_content_publication_unpublish.py \
  tests/contract/test_media_catalog_api.py \
  tests/unit/application/test_media_catalog.py \
  tests/unit/application/test_content_audience_requester_private.py \
  -q -p no:cacheprovider
```

Negative and adversarial controls: use synthetic fixtures and disposable
databases under the declared probe root only; run temporary synthetic pytest
probe files through the declared route if the route accepts them, and report
honestly as unverified any control the route cannot execute instead of using
ambient Python. Cover at least:

- Forgery and owner selection: client identity fields, proxy headers or a
  client-supplied owner cannot select the local owner or an administrator.
- Horizontal and vertical access: a second ordinary member is denied and
  indistinguishable from unknown for another owner's private/unfinished
  records across list, detail, counts, search, facets and file routes;
  household reads only the approved snapshot; administrator read-all works;
  anonymous and public composition are denied.
- Approval adversarial: an ordinary caller cannot approve; stale version and
  stale digest conflict; racing approve/withdraw yields one consistent state
  with no partial writes.
- Projection stability: approve A, change working state to B, confirm the
  household still reads A in detail/list/filters/counts/analysis/cover, then
  reapprove and confirm B at the original Timeline position.
- Public exclusion: bound `private` and `family` records with stray legacy
  publication rows are absent from public list/detail/tags/bytes.
- Migration/recovery: populated synthetic 0033 upgrade preserves old rows and
  creates zero common records; populated downgrade refuses without DDL;
  FK/CHECK/UNIQUE enforcement; backup/restore with documents and projections.
- Private state: symlink, hardlink and unsafe-mode refusal without `chmod`;
  creation modes under `umask 022`; read-only creates nothing.
- Inventory completeness: the artifact matches actual route policies and its
  test fails on a generic or missing per-route mapping.
- Leak hunt over the 109-path diff: no credential or secret value, no raw
  provider payload or reasoning stream, no document/SQL/private content in
  errors or logs, no out-of-allowlist production change.

State every observed result with exact evidence; unverified controls are
reported as unverified, never as PASS. Findings use the full INFOSEC finding
structure (evidence class, reachability, preconditions, privilege, impact,
containment, residual risk).

## Authority and containment

Positive authority: read-only inspection of the candidate, governing `.ap`
and the named trace evidence; the declared route with the candidate baseline;
creation, use and cleanup of one declared temporary probe root under `/tmp`
(mode 0700, synthetic data only); the terminal report write at the exact
destination when absent, with full readback.

Negative authority: no product, test, documentation, configuration, AP,
packaging or migration edit; no correction; no host, SSH, gate, sudo, service,
browser, provider or credential action; no network; no push or publication;
no new dependency; no subagent; no `private/**`; no Meta commit.

## Stopping conditions

Stop with `PARTIAL` or `BLOCKED` on: identity, candidate or git-state
mismatch; an unusable declared route; a probe exceeding the authorized
effects; sensitive output; or a required control that cannot be established
without a forbidden mutation. Preserve the first causal failure; missing
evidence is never PASS. A second equivalent cycle for the same unchanged
blocker requires `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## Evidence selection

```text
Evidence tier: E3
Evidence tier basis: security/trust boundary (centralized authorization), durable migration 0034, private-state permissions, approval transactions
Activated stricter profile: INFOSEC.md — R3 route (fresh focused audit)
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the selected security subset above
Affected tests: the S6 candidate delta
New causal regression: none — this is acceptance
Broad or full suite: not-used — already run once for this exact candidate; only the four parked pre-existing cases fail; do not re-run
Runtime or testbed: declared route plus the declared synthetic probe root; no host
Independent acceptance: required-separate-fresh-worker (this exchange)
```

## Completion and report contract

`PASS` means every fixed claim is independently established and no blocking
finding remains. Use `Phase-qualified result: acceptance-PASS` only for a PASS;
otherwise `not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: final-acceptance`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 35, exchange 01) exactly once. Include the
compact core; the completed Acceptance and Correction Record; per-claim
verdicts with exact evidence; the control matrix with observed counts and exit
codes; adversarial outcomes; findings with the full structure; containment and
probe cleanup; residual risk and limitations; one smallest next step (a
separate publication grant for the accepted candidate); the critique block; and
the authority-expiry statement.

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
Trace discovery: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 35_acceptance_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 35_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

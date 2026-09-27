# Kronika one product — S6 bounded correction: operator duplicate resolution (exchange 05)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 34
Worker exchange ordinal: 05
Implementation authority: explicit
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S6-OPERATOR-DUPLICATE-RESOLUTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — one localized production side-effect correction with a strong narrow reproduction; the identity-requirement boundary is explicit below. The Cooperator may override.
Recommended context capacity: the same recommendation as grant 34/01 — approximately 1M tokens if the client exposes it; otherwise approximately 250k tokens under the context-pressure rule.
Independence required: no — the corrector never self-certifies; the separate fresh E3/R3 authorization review follows after the candidate is complete.

## Current-session continuity and renewal

Continuity anchor: your own terminal PARTIAL report for task
`KRONIKA-ONE-PRODUCT-S6-YOUTUBE-DEMO-IDENTITY-CORRECTION`, session 34 exchange
04, saved at
`/home/agile/meta/projects/kronika/00/02-kronika-one-product/34_report_03.md`
(SHA-256 `ed3925a198fcbb4df84e7663dde954a17deb2cbe53fd8b8fa4b595b7eaa4f019`),
including its "Cause" and "Next step" sections.

That authority expired when the terminal report was submitted. This exchange
grants one smallest coherent correction authority for the new finding that
exchange 04 exposed, plus the final validation and commit needed to reach a
candidate. It is a renewal, not an automatic continuation. Reuse is
appropriate: same healthy logical whole, unchanged assumptions, and your
retained understanding of the tree. Retained context is convenience, not
authority; if it conflicts with current repository evidence, current evidence
wins and you stop and report. Evidence is non-independent.

No subagents. Client mode: write-capable with native Plan mode OFF; if the mode
prohibits the required writes, stop and report without bypassing the
restriction. Do not run `sudo -v` or `sudo -K`. Do not start the E3/R3 review.

## Finding (confirmed)

After exchange 04 installed the real configured-local-owner identity, the demo
advanced to the same-video reuse case and now fails at
`tests/support/youtube_fake_demo.py` `assert '"result":"reused"' in duplicate_output`
for the manual byte duplicate (`ZyXwVu987_-`): it is cataloged as
`"result":"new"` instead of `"reused"`.

Cause, confirmed by Orchestrator read-only inspection:
`YouTubeAcquisitionCoordinator._handoff` in
`src/framenest/application/youtube_acquisition.py` (around lines 1189–1195)
selects `UploadDuplicateResolutionMode.EXPLICIT` only when
`claim.created_by_login_key is None`; any verified login, including the
operator administrator, selects `SILENT_KEEP_SEPARATE`. That login-presence
proxy was valid while operator claims carried no identity; the accepted S6
closure now passes and persists a verified `youtube.acquire` identity, so the
operator path silently changed duplicate semantics.

This violates the accepted design: ordinary users retain
`SILENT_KEEP_SEPARATE`, administrators retain explicit resolution
(`33_report_00.md` section 3 / `25_report_00.md` section 5; the upload API
derives explicit resolution from `CAPABILITY_UPLOAD_MANAGE` in
`src/framenest/adapters/api/upload_api.py`, and `ROLE_ADMIN` includes that
capability in `src/framenest/domain/identity_access.py`).

## Effective allowlist for this correction

Unchanged from exchange 04: the original 176-path union plus exactly
`tests/support/youtube_fake_demo.py` and
`tests/contract/test_youtube_fake_demo.py`. No new path is added. A required
edit outside this effective allowlist is a stop.

Required behavior to implement (choose the smallest identity-agnostic
mechanism; the application layer must not import adapter/config types):

- In the YouTube acquisition handoff, select `EXPLICIT` when the claim has no
  creator login (legacy) **or** the creator's verified login has
  administrator duplicate-management authority (`upload.manage`, the same
  predicate the upload API uses); select `SILENT_KEEP_SEPARATE` only for an
  ordinary verified login.
- Wire the predicate/mapping at composition from
  `src/framenest/adapters/api/application.py` (the `identity_mapping` built at
  line 413 is in scope at the coordinator construction around line 984) and
  from the demo harness in `tests/support/youtube_fake_demo.py`, using the
  same synthetic administrator it already configures.
- Do not change the operator identity requirement, the operator route
  authorization, or any ordinary requester behavior. Do not touch the X
  acquisition handoff (its comment already records that every real X claim has
  an ordinary requester and stays silent).
- Do not weaken, delete, skip or relax any test assertion; do not bypass the
  real middleware; do not seed `SCOPE_IDENTITY` directly.
- Add one causal regression inside the allowlist that distinguishes the two
  paths: an administrator/operator claim keeps explicit duplicate reuse while
  an ordinary requester claim stays `SILENT_KEEP_SEPARATE` (for example in
  `tests/unit/application/test_youtube_acquisition_lifecycle.py` or
  `tests/contract/test_youtube_operator_api.py`). State the evidence gap and
  why this test closes it.

## Re-gating (fail closed)

1. Verify branch, HEAD, parent, tree, no commit, and the AP pin
   `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
2. Enumerate `git status --porcelain=v1 --untracked-files=all`; the opening
   set must be the 109 paths from your exchange-04 report or a strict subset
   after your own continued edits, every path inside the effective allowlist.
   Any out-of-allowlist path or a set that does not match the report is a stop.
3. The worktree difference remains `accepted-continuation` (RF-12) and must be
   preserved; never reset, clean, checkout, restore, stash or delete.
4. Re-verify the report destination is absent.

## Validation and commit

1. Narrow reproduction of the finding:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/contract/test_youtube_fake_demo.py -q -p no:cacheprovider
```

   It must exit 0 with the complete real-loopback acceptance (manual duplicate
   reused, claim counts, `provider_submission_count: 0`,
   `staging_residue_count: 0`, `youtube_analysis_notification_count: 0`).
2. Prove no regression of the gates: rerun
   `tests/contract/test_youtube_operator_api.py`,
   `tests/contract/test_kronika_acquisition_authorization.py`,
   `tests/contract/test_requester_private_youtube_details.py` and the new
   regression test through the same route; assertions unchanged and green.
3. Focused 96-file list from grant 34/01 through the same route; it must exit
   0.
4. Broad suite once for the final candidate:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit tests/contract tests/integration -q -p no:cacheprovider
```

   The result may exit 0, or exit non-zero only with the four parked
   pre-existing cases from grant 34/02's disposition and the same signatures.
   Any other failure is a stop: no commit, report `PARTIAL` with the first
   causal evidence. Non-zero remains non-zero.
5. If all gates hold: stage exactly the changed allowlisted paths (never
   `git add .` or `git add -A`), inspect `git diff --cached --check`, `--stat`
   and the cached diff, and create exactly one local commit:

```text
feat(kronika): add private records and administrator approval
```

   No push, fetch, tag, merge, rebase, reset, restore, checkout, switch, stash,
   clean, remote or config writes. Verify post-commit cleanliness and capture
   SHA, parent, tree and subject.

## Stop conditions

Grants 34/01–34/04 stop conditions remain in force, plus: any change to the
operator identity requirement or ordinary requester duplicate behavior; a
required edit outside the effective allowlist; a new broad failure; conflict
between retained context and current evidence; material context pressure; or a
client mode that prohibits the required writes. If this exchange ends
`PARTIAL` or `BLOCKED` for a materially unchanged residual blocker, include
exactly:

```text
Consecutive terminal PARTIAL/BLOCKED reports for the same materially unchanged blocker: 2
Exact blocker: <one causal blocker>
Smallest authority expansion needed: <minimum or none>
Direct closure path: <execute, reject, or identify missing evidence>
Consequence of no action: <bounded consequence>
Closure decision required: authorize-and-execute | reject-with-reason | identify-missing-evidence
```

A further equivalent cycle will not be authorized without new mutation,
evidence, material risk, external state or objective.

## Completion and report contract

`PASS` means: the operator handoff preserves explicit duplicate resolution for
an administrator login while ordinary requesters stay silent; the demo narrow
run, the gate tests and the new regression test exit 0; the focused 96-file
list exits 0; the broad suite is 0 or fails only with the four parked cases;
exactly one local commit exists with a clean worktree and no push. Use
`Phase-qualified result: implementation-PASS` for PASS; otherwise
`not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 34, exchange 05) exactly once. Include: the
mechanism and the authority predicate used; proof the identity gate and
ordinary requester behavior are unchanged; the new regression test identity and
why the prior evidence gap existed; the narrow, gate, focused and broad results
with counts and exit statuses; the final changed-path set with the
allowlist-subset statement; the commit SHA, parent, tree, subject and no-push
evidence; post-commit cleanliness; deviations, risks and missing evidence; one
smallest next step (the separate fresh E3/R3 authorization review after PASS);
the critique block; and the authority-expiry statement.

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
Downloadable prompt filename: 34_implementation_04.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 34_report_04.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

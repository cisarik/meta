# Kronika one product — S6 bounded correction: YouTube fake-demo local identity (exchange 04)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 34
Worker exchange ordinal: 04
Implementation authority: explicit
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: correction
Task identity: KRONIKA-ONE-PRODUCT-S6-YOUTUBE-DEMO-IDENTITY-CORRECTION
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — one localized test-support correction with a strong narrow reproduction; the security-adjacent constraint is explicit below. The Cooperator may override.
Recommended context capacity: the same recommendation as grant 34/01 — approximately 1M tokens if the client exposes it; otherwise approximately 250k tokens under the context-pressure rule.
Independence required: no — the corrector never self-certifies; the separate fresh E3/R3 authorization review follows after the candidate is complete.

## Current-session continuity and renewal

Continuity anchor: your own terminal PARTIAL report for task
`KRONIKA-ONE-PRODUCT-S6-IMPLEMENTATION`, session 34 exchange 03, saved at
`/home/agile/meta/projects/kronika/00/02-kronika-one-product/34_report_02.md`
(SHA-256 `32085919615377c244071c9dfd0c0ec603c2d1028801071a4564b01c3e0f5ca7`),
including its "Stop: fifth broad failure" section.

That authority expired when the terminal report was submitted. This exchange
grants one smallest coherent correction authority for that one confirmed
finding, plus the final validation and commit needed to reach a candidate. It
is a renewal, not an automatic continuation. Reuse is appropriate: same healthy
logical whole, unchanged assumptions, and your retained understanding of the
108-path tree. Retained context is convenience, not authority; if it conflicts
with current repository evidence, current evidence wins and you stop and
report. Evidence is non-independent.

No subagents. Client mode: write-capable with native Plan mode OFF; if the mode
prohibits the required writes, stop and report without bypassing the
restriction. Do not run `sudo -v` or `sudo -K`. Do not start the E3/R3 review.

## Finding (confirmed)

`tests/contract/test_youtube_fake_demo.py::test_youtube_fake_demo_runs_the_real_loopback_cli_to_acceptance`
now fails with a completed process return code of 1: the demo's `main` asserts
`new_exit == 0` at `tests/support/youtube_fake_demo.py:705`, and the surfaced
output is only the confirmation event for the submitted video, not a passing
ingest.

Cause, confirmed by Orchestrator read-only inspection: the exchange-03 S6
closure made the operator YouTube routes require a verified identity with
`youtube.acquire` (`_acquisition_identity` in
`src/framenest/adapters/api/youtube_operator_api.py` returns 401 without
`SCOPE_IDENTITY`), while the demo's minimal FastAPI app built in
`_build_environment` installs only
`create_youtube_operator_api_router(...)` and never installs the production
local-identity path (`LocalIdentityMiddleware` with
`configured_local_identity(settings)`, as installed in
`src/framenest/adapters/api/application.py`). The real CLI therefore posts
over loopback without a verified identity and is correctly refused.

The S6 operator-identity requirement is accepted design and must not be
weakened, relaxed or bypassed. The demo harness must present a configured
synthetic local owner through the real mechanism.

## Effective allowlist for this correction

The 176-path union from grant 34/01 remains in force, extended by exactly these
two paths:

```text
tests/support/youtube_fake_demo.py
tests/contract/test_youtube_fake_demo.py
```

These two files may be changed only to give the demo's loopback server a
configured synthetic local owner through the real configured-local-identity
mechanism, and only as far as needed for the demo to exercise the real routes
again. No production source file may change. No other path may change. A
required edit outside this effective allowlist is a stop.

Hard constraints:

- Do not weaken, delete, skip or relax the demo's assertions or the operator
  identity gate.
- Do not bypass the real mechanism: no direct seeding of
  `SCOPE_IDENTITY`, no mutation of `_acquisition_identity` behavior, no
  test-only permissive policy stub on the operator routes, no mocked identity
  the production middleware would not produce.
- Prefer wrapping the demo app with the existing middleware using the existing
  helper (`configured_local_identity` or `local_identity_context`) and a
  synthetic identity mapped with `youtube.acquire`; keep the demo's real
  operator router, real CLI and real acceptance assertions (claim counts,
  `provider_submission_count: 0`, `staging_residue_count: 0`,
  `youtube_analysis_notification_count: 0`).
- No test may be edited outside the two added paths.

## Re-gating (fail closed)

1. Verify branch, HEAD, parent, tree, that no commit exists, and the AP pin
   `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
2. Enumerate `git status --porcelain=v1 --untracked-files=all`; the opening
   set must be the 108 paths from your exchange-03 report or a strict subset
   after your own continued edits, every path inside the effective allowlist.
   Any out-of-allowlist path or a set that does not match the report is a stop
   with preserved evidence.
3. The worktree difference remains `accepted-continuation` (RF-12) and must be
   preserved; never reset, clean, checkout, restore, stash or delete.
4. Re-verify the report destination is absent.

## Validation and commit

1. Narrow reproduction of the finding, declared route and exact baseline:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/contract/test_youtube_fake_demo.py -q -p no:cacheprovider
```

   It must exit 0 with the real-loopback acceptance path.
2. Prove the gate remains enforced: rerun
   `tests/contract/test_youtube_operator_api.py`,
   `tests/contract/test_kronika_acquisition_authorization.py` and
   `tests/contract/test_requester_private_youtube_details.py` through the same
   route; their assertions must be unchanged and green.
3. Focused 96-file list from grant 34/01 through the same route; it must exit
   0.
4. Broad suite once for the final candidate:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit tests/contract tests/integration -q -p no:cacheprovider
```

   The result may exit 0, or exit non-zero only with the four parked
   pre-existing cases from grant 34/02's disposition and the same signatures.
   Any other failure is a stop: no commit, report `PARTIAL` with the first
   causal evidence. Non-zero remains non-zero; parking is not a PASS claim.
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

Grant 34/01–34/03 stop conditions remain in force, plus: any needed production
code change; any weakening or bypass of the operator identity requirement; a
new broad failure; an out-of-allowlist edit; conflict between retained context
and current evidence; material context pressure; or a client mode that
prohibits the required writes. If this exchange ends `PARTIAL` or `BLOCKED` for
a materially unchanged residual blocker, include exactly:

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

`PASS` means: the demo failure is corrected inside the two added paths through
the real mechanism; the operator-identity gate tests remain green; the focused
96-file list exits 0; the broad suite is 0 or fails only with the four parked
cases; exactly one local commit exists with a clean worktree and no push. Use
`Phase-qualified result: implementation-PASS` for PASS; otherwise
`not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 34, exchange 04) exactly once. Include: the
mechanism used and why it is the real path; proof that no production file
changed and the gate tests are green; the narrow, focused and broad results
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
Downloadable prompt filename: 34_implementation_03.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 34_report_03.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

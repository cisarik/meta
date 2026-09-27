# Kronika one product — S6 implementation final completion (renewed grant, exchange 03)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 34
Worker exchange ordinal: 03
Implementation authority: explicit
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S6-IMPLEMENTATION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the named S6 risks remain plus the residual mandatory-scenario and inventory-truthfulness work. The Cooperator may override.
Recommended context capacity: the same recommendation as grant 34/01 — approximately 1M tokens if the client exposes it; otherwise approximately 250k tokens under the context-pressure rule.
Independence required: no — implementation evidence is non-independent; the separate fresh E3/R3 authorization review follows only after a PASS.

## Current-session continuity and renewal

Continuity anchor: your own terminal PARTIAL report for task
`KRONIKA-ONE-PRODUCT-S6-IMPLEMENTATION`, session 34 exchange 02, saved at
`/home/agile/meta/projects/kronika/00/02-kronika-one-product/34_report_01.md`
(SHA-256 `345885401742d6dfd57e0dfe0794b7423f2da56f01f008f947034670531c0771`),
including its "Next step", "Deviations" and "Mandatory scenarios" sections.

That authority expired when the terminal report was submitted. This exchange
grants complete renewed implementation-completion authority for the same
bounded task; it is a renewal, not an automatic continuation. Reuse is
appropriate: same healthy logical whole, unchanged assumptions, and your
retained understanding of the 104-path tree materially reduce completion error;
independence is not required. Retained context is convenience, not authority.
If retained context conflicts with current repository evidence, current
evidence wins: stop and report instead of acting on memory. Evidence is
non-independent.

You are still the WORKER. Do not plan (native planning mode not-used), do not
reopen the frozen design, do not start the E3/R3 review, and do not expand the
allowlist. No subagents. Client mode: write-capable with native Plan mode OFF;
if the mode prohibits repository edits, the commit or the report write, stop
and report without bypassing the restriction. Do not run `sudo -v` or
`sudo -K`.

## State at issuance (verified read-only by the Orchestrator, 2026-09-27)

- HEAD, parent and tree are still `40e51cb2d061ead96850c9c94aa59de54d5e1310`,
  `75e9b07b…`, `ec3c6c9…`; no new commit; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD).
- The worktree is dirty with exactly 104 paths: 81 modified and 23 untracked.
  The Orchestrator verified every one is inside the 176-path allowlist and that
  nothing outside it changed; the set matches your exchange-02 report.
- The Orchestrator verified your two pre-existing clusters read-only:
  `pyproject.toml:25` declares `framenest-chatgpt-page = "kronika_capture.cli:main"`
  while `.venv/bin/` lacks the script; the process environment contains
  `FRAMENEST_NUC_SSH_TARGET`, `FRAMENEST_NUC_SSH_USER` and
  `FRAMENEST_NUC_SSH_IDENTITY` (names only; values were not read), which
  explains the three gate-parameter failures. Both surfaces are outside the
  allowlist.
- Report destination `34_report_02.md` is absent.

## Orchestrator disposition of the two pre-existing clusters

The four broad-suite failures of exchange 02 are accepted as **explicitly
parked pre-existing debt**, outside the S6 allowlist and outside the candidate:

1. `tests/contract/test_development_cli.py::test_project_console_entries_match_packaged_metadata`
   — stale virtualenv versus the committed `[project.scripts]` entry
   (`framenest-chatgpt-page`); signature `AssertionError: missing console
   script: framenest-chatgpt-page`.
2. `tests/contract/test_operator_network_scripts.py::test_ssh_gate_rejects_missing_required_values`
   parameters `target`, `user` and `identity` — the three `FRAMENEST_NUC_SSH_*`
   names are exported in the ambient environment, so the fish gate exits 0;
   signature `AssertionError: assert 0 != 0` at the script's line 833.

Do not fix, suppress, skip or edit these; their files are outside the
allowlist. They do not block the S6 commit. They remain recorded debt and
ledger candidates. A future environment-maintenance task may refresh the
virtualenv and harden the gate test; no such task is authorized here.

## Re-gating (fail closed)

1. Verify branch, HEAD, parent, tree, that no commit exists, the AP pin, and
   that `0034` still has no collision.
2. Enumerate `git status --porcelain=v1 --untracked-files=all`; confirm the
   changed set is the 104 paths from your report or a strict subset after your
   own continued edits, and that every path stays inside the exact allowlist.
   Any out-of-allowlist path or a set that does not match the report is a stop
   with preserved evidence.
3. The worktree difference remains `accepted-continuation` (RF-12) and must be
   preserved; never use reset, clean, checkout, restore, stash or delete.
4. Re-verify the public baseline with read-only `git ls-remote`; verify the
   report destination is absent.
5. Material context pressure or provenance loss is reported, not worked
   around: stop at a safe point, leave the worktree in place, report `PARTIAL`.

## Completion scope (one bounded final outcome)

All authority, boundaries, design requirements, negative authority, declared
route, staging rules and stop conditions of grants 34/01 and 34/02 remain in
force unchanged. The exact allowlist is unchanged: the 176-path union
enumerated in grant 34/01 (equal to `33_report_00.md` section 6). No wildcard
expansion; a required out-of-list edit is a stop. Do not weaken, delete or skip
existing assertions to make gates pass.

Finish exactly these three items, then commit:

### A. Truthful access inventory

Rewrite the inventory artifact and its generator/verifier so that
`docs/KRONIKA_ACCESS_INVENTORY.md` and
`tests/contract/test_kronika_access_inventory.py` are truthful per route:

1. Every record/content-bearing route-method row states its real identity
   source, capability, object/SQL predicate, selected projection, mutation
   transaction check and file-open position — not one boilerplate string for
   all rows — and cites a **specific existing positive and a specific existing
   negative behavioral test ID that actually exercises that route or method**.
   The two generic audience-policy IDs currently reused must not stand in for
   per-route evidence.
2. Rows that are genuinely not record readers (health, static, capability,
   status, provider administration, audience echo) carry an explicit exclusion
   and deferred reason with empty access columns; do not force the
   record-reader template onto them and do not mislabel identity-required
   routes as `not required`.
3. The operator YouTube claim routes (`POST /api/operator/youtube/claims`,
   `GET /api/operator/youtube/claims/{claim_id}`,
   `POST /api/operator/youtube/claims/{claim_id}/retry`) must state the frozen
   rule: configured identity with acquisition capability is required; loopback
   alone is insufficient. Cite their behavioral tests
   (`tests/contract/test_kronika_acquisition_authorization.py`,
   `tests/contract/test_youtube_operator_api.py`,
   `tests/contract/test_youtube_browser_api.py` as applicable).
4. Where a content route genuinely lacks a positive or negative behavioral
   case, add the minimal such test inside the allowlist rather than recording a
   generic or empty mapping. The inventory test must fail when a content row
   lacks a specific positive and negative test ID or when a row's
   classification contradicts the actual route policies.

### B. Remaining mandatory-scenario evidence

Add the missing behavioral coverage, inside the allowlisted test files, for
exactly these groups (the frozen plan `33_report_00.md` section 7 remains the
standard):

1. **Caller matrix (HTTP + SQL):** owner reads own private/unfinished; another
   verified member is denied (equivalent to unknown); administrator read-all
   including another owner's private/unfinished; household member reads the
   approved snapshot; anonymous and public compositions denied; SQL/domain
   parity for list membership.
2. **Identity and audit:** forged identity rejected; client-selected owner
   ignored; failed privileged audit fails closed; invalid local configuration
   rejected.
3. **Denial before open:** a dedicated negative proving that media
   content/download/preview denial occurs before any resolver, file open or
   provider call (spy/patch evidence).
4. **Indirect disclosure:** upload duplicates keep `SILENT_KEEP_SEPARATE` and
   reveal no foreign ID, title, hash or private-match; YouTube requester
   forbidden link returns `media_id=null` with `unavailable`; X assets suppress
   forbidden links; bound media is excluded from legacy publication even with a
   stray publication row (already covered — cite it).
5. **Projection stability:** approve A; change working state to B (metadata,
   analysis, cover); household detail, filters, counts, analysis and cover
   still expose A; reapprove and confirm B at the original Timeline position.
6. **Transactions:** racing approve/withdraw, and a stale version or stale
   projection digest, yield typed conflicts with no partial state.
7. **Legacy removal:** bound-media removal fails before receipt insertion,
   relationship detachment and filesystem cleanup (assert no receipt and no
   cleanup).
8. **Backup/restore:** catalog backup and restore with documents and approved
   projections preserves the new tables and private permissions.
9. **Document integrity:** invalid persisted document JSON fails closed and an
   injected failure rolls back document and record atomically (cite the
   existing tests if they already cover this).

### C. Final validation, acceptance of the parked failures, and commit

1. Run the focused 96-file list (`-q -p no:cacheprovider`, declared route and
   exact baseline). It must exit 0.
2. Run the broad suite once for the final candidate:

```text
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit tests/contract tests/integration -q -p no:cacheprovider
```

   The broad result may exit 0, or exit non-zero **only** if every failure is
   one of the four parked pre-existing cases in the disposition above with the
   same signatures. Any other failure is a stop: no commit, report `PARTIAL`
   with the first causal evidence. Non-zero remains non-zero in the report —
   the disposition is Orchestrator-accepted parking, not a PASS claim.
3. If both gates hold, stage exactly the changed allowlisted paths (never
   `git add .` or `git add -A`), inspect `git diff --cached --check`, `--stat`
   and the cached diff, and create exactly one local commit:

```text
feat(kronika): add private records and administrator approval
```

   No push, fetch, tag, merge, rebase, reset, restore, checkout, switch, stash,
   clean, remote or config writes. Verify post-commit cleanliness and capture
   SHA, parent, tree and subject.

## Stop conditions

Grants 34/01 and 34/02 stop conditions remain in force, plus: a broad failure
other than the four parked cases; an inventory row that cannot be made
truthful without an out-of-allowlist edit; conflict between retained context
and current evidence; material context pressure; or a client mode that
prohibits the required writes. If this exchange ends `PARTIAL` or `BLOCKED`
for a materially unchanged residual blocker, include exactly:

```text
Consecutive terminal PARTIAL/BLOCKED reports for the same materially unchanged blocker: 2
Exact blocker: <one causal blocker>
Smallest authority expansion needed: <minimum or none>
Direct closure path: <execute, reject, or identify missing evidence>
Consequence of no action: <bounded consequence>
Closure decision required: authorize-and-execute | reject-with-reason | identify-missing-evidence
```

A third equivalent cycle will not be authorized without new mutation, evidence,
material risk, external state or objective.

## Completion and report contract

`PASS` means: the inventory is truthful per section A; the section-B coverage
exists; the focused 96-file list exits 0; the broad suite is 0 or fails only
with the four parked cases; exactly one local commit exists with a clean
worktree and no push. Use `Phase-qualified result: implementation-PASS` for
PASS; otherwise `not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 34, exchange 03) exactly once. Include the
compact core and the evidence required by grants 34/01–34/02: changed paths and
the allowlist-subset statement; the inventory truthfulness evidence (row
classification counts, per-route test mapping, corrected operator rows);
per-scenario test IDs and results; commands and exit statuses; the focused and
broad results with the parked-failure tallies; transaction/migration/
private-state/backup receipts; the commit SHA, parent, tree, subject and
no-push evidence; post-commit cleanliness; deviations, risks and missing
evidence; one smallest next step (the separate fresh E3/R3 authorization review
after PASS); the critique block; and the authority-expiry statement.

The formal report is in English; the short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination below only if absent, read it back in full, verify its first line,
coordinates, content and path, then send the separate short completion notice
with status, path and SHA-256. If the report write is blocked by the client,
preserve the complete content in the client output and report the missing
delivery truthfully. Terminal report or cancellation expires this authority; no
autonomous continuation.

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
Downloadable prompt filename: 34_implementation_02.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 34_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

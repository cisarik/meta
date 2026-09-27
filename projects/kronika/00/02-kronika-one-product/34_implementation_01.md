# Kronika one product — S6 implementation completion (renewed grant, exchange 02)

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 34
Worker exchange ordinal: 02
Implementation authority: explicit
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: KRONIKA-ONE-PRODUCT-S6-IMPLEMENTATION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the named risks from grant 34/01 remain (fail-closed authorization seam, durable migration 0034, private-state permissions, approval transactions) plus the unclassified failing gates in the dirty candidate. The Cooperator may override.
Recommended context capacity: the same recommendation as grant 34/01 — approximately 1M tokens if the client exposes it; otherwise approximately 250k tokens under the context-pressure rule.
Independence required: no — implementation evidence is explicitly non-independent; the separate fresh E3/R3 authorization review follows only after a PASS.

## Current-session continuity and renewal

Continuity anchor: your own terminal PARTIAL report for task
`KRONIKA-ONE-PRODUCT-S6-IMPLEMENTATION`, session 34 exchange 01, saved at
`/home/agile/meta/projects/kronika/00/02-kronika-one-product/34_report_00.md`
(SHA-256 `1e68d1bc96770cb1dd311265093ef3e25adb6d274f924e60f1b1a8bcb28a00de`),
including its "Next step" section and critique.

Your previous implementation authority expired when that terminal report was
submitted. This exchange grants complete renewed implementation-completion
authority for the same bounded task; it is a renewal, not an automatic
continuation. Reuse is appropriate because this is the healthy same logical
whole, assumptions are unchanged, and your retained repository understanding of
the 81-path uncommitted design materially reduces completion error;
independence is not required. Retained context is convenience, not authority.
If retained context conflicts with current repository evidence, current
evidence wins: stop and report instead of acting on memory. Evidence in this
exchange is non-independent.

You are still the WORKER. Do not plan (native planning mode not-used), do not
reopen the frozen design, do not start the separate E3/R3 review, and do not
expand the allowlist. No subagents.

Client mode: the continuation must run in a write-capable execution mode with
native Plan mode OFF. If the mode now prohibits repository edits, the local
commit or the report write, stop and report; never bypass the restriction.

## State at issuance (verified read-only by the Orchestrator, 2026-09-26)

- Product checkout `/home/agile/Projects/framenest`, branch
  `feat/kronika-one-product`, HEAD
  `40e51cb2d061ead96850c9c94aa59de54d5e1310` (parent `75e9b07b…`, tree
  `ec3c6c9…`); no new commit; local `main` = `origin/main` = baseline; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and `.ap` HEAD); migration
  head `0033` with the new `0034` file untracked.
- The worktree is dirty with exactly 81 paths: 66 modified existing files and
  15 untracked new files. The Orchestrator verified every one of the 81 paths
  is inside the 176-path allowlist and that no path outside it changed; the set
  matches your report (local `git status --porcelain --untracked-files=all`).
- Public `refs/heads/main` of `cisarik/framenest` was `40e51cb2…` at issuance.
- Report destination `34_report_01.md` is absent.

## Re-gating (fail closed, before further mutation)

1. Verify physical root, branch, HEAD, parent and tree, and that no commit
   exists.
2. Enumerate `git status --porcelain=v1 --untracked-files=all`; confirm the
   changed set is the 81 paths from your report (66 modified + 15 untracked) or
   a strict subset of it after your own continued edits, and that every path
   stays inside the exact allowlist. Any out-of-allowlist path, or a change set
   that does not match the report, is a stop with the preserved evidence.
3. Classify the worktree difference under RF-12: it is `accepted-continuation`
   (work authorized by grant 34/01 of this same whole) and must be preserved.
   Never use reset, clean, checkout, restore, stash or delete.
4. Re-verify the AP pin (gitlink and `.ap` HEAD), that `0034` still has no
   collision, the public baseline via read-only `git ls-remote`, and that the
   report destination is absent.
5. Material context pressure or provenance loss is reported, not worked
   around: stop at a safe point, leave the worktree in place, and report
   `PARTIAL` with the exact state.

## Completion scope (one bounded outcome)

Finish exactly the S6 candidate from grant 34/01 and commit it. All authority,
boundaries, design requirements, evidence requirements, declared execution
route, staging rules and stop conditions of grant 34/01 remain in force
unchanged. The exact allowlist is unchanged: the 176-path union enumerated in
grant 34/01 (equal to `33_report_00.md` section 6). No wildcard expansion; a
required out-of-list edit is a stop.

Complete specifically:

1. The unfinished G1 closures named in your report: YouTube requester/reuse, X
   requester, workspace, and analysis-proposal authorization closures with
   their indirect test fallout, plus any upload closure remainder (frozen plan
   section 3 and `33_report_00.md` section 3).
2. The unclassified failing gates. Classify each failure before repair,
   preserve the first causal error, and fix only what the allowlist permits:
   - the public-composition `GET /api/media` 500 behind
     `tests/contract/test_public_published_uds.py::test_redacted_catalog_and_metadata_omit_internal_fields`
     (`PUBLIC_READ_FAILED`) — capture the causal exception/`exception_input`
     before editing; public scope must exclude every common record, including
     `family`, and preserve authorized legacy behavior;
   - the catalog overlay `KeyError: display_title`;
   - the remaining observed allowlisted failures from your report (companion
     review, content-publication unpublish, analysis lifecycle, suggestions,
     workspace, X route policy, YouTube details, Tailscale ingress, team-alias
     gallery payload, atomic upload publication) — re-run to establish which
     still exist before repairing.
3. The 8 missing paths:

```text
tests/unit/application/test_records.py
tests/integration/persistence/test_kronika_record_repository.py
tests/contract/test_kronika_record_authorization.py
tests/contract/test_kronika_access_inventory.py
tests/contract/test_local_record_identity.py
tests/contract/test_kronika_acquisition_authorization.py
tests/contract/test_kronika_approved_projection.py
docs/KRONIKA_ACCESS_INVENTORY.md
```

   The inventory and its test must satisfy grant 34/01 section 6 and the
   "Inventory" mandatory scenario, including the actual acquisition routes
   `/api/admin/youtube/claims`, `/api/operator/youtube/claims` and
   `/api/admin/x/requests/{claim_id}`.
4. The mandatory-scenario evidence still missing from your report: HTTP and SQL
   caller matrix; identity forgery, client-selected owner and failed privileged
   audit; denial before file opens, providers and writes; indirect disclosure
   (upload duplicates, YouTube, X); projection stability approve-A-then-change-B
   with reapproval at the original Timeline position; transaction races and
   injected failures with no partial state; legacy removal of a bound row with
   no receipt or cleanup; backup/restore with documents and projections; invalid
   persisted document JSON and atomic rollback; complete inventory.
5. Truthful current-head documentation inside the allowlist (README, PRODUCT,
   SPEC, ROADMAP, SECURITY, DEVELOPMENT, docs/INFOSEC.md,
   docs/BACKUP_AND_RECOVERY.md) — no acceptance, deployment or publication
   claim.
6. Run the focused 96-file list from grant 34/01 (new and affected first, then
   the remaining named files) and then the broad suite once, current for the
   final candidate:

```bash
./.ap/ap exec --root /home/agile/Projects/framenest --baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310 --operation test-focus -- tests/unit tests/contract tests/integration -q -p no:cacheprovider
```

   The earlier stale unit/contract result does not satisfy this requirement.
   JavaScript tests: not-used. No ambient Python, pytest, Poetry or substitute
   route; do not repair or reconstruct the environment. Diagnose with the
   smallest reproducer before any justified broad rerun; non-zero remains
   non-zero.
7. Stage exactly the changed allowlisted paths (never `git add .` or
   `git add -A`), inspect `git diff --cached --check`, `git diff --cached
   --stat` and the cached diff, and create exactly one local commit:

```text
feat(kronika): add private records and administrator approval
```

   No push, fetch, tag, merge, rebase, reset, restore, checkout, switch, stash,
   clean, remote or config writes. After the commit, verify cleanliness and
   capture SHA, parent, tree and subject; report no-push evidence.

Any claim of a pre-existing failure must now carry the complete classification
record (exact comparison baseline commit; whether it predates the whole logical
whole or only the latest change; exact test identity; exact failure signature;
topical relation; superseding accepted authority or none; regression-exclusion
evidence; closure impact). Your report's partial classification is not
sufficient.

## Negative authority (unchanged from grant 34/01)

No edits outside the exact allowlist; no real or live database, real data,
historical backfill or migration of existing catalogs; no `private/**`, browser
profiles, tokens or credentials; no host, SSH, sudo, service, browser, provider
or credential action; no network beyond the single read-only `git ls-remote`
baseline gate; no `.ap`, managed-block, dependency, lockfile or toolchain
change; no migration `0035` and no change to existing migration files; no S4-A
file change; no real ingestion cutover; no UI or capture package; no push,
publication, deployment, reset, acceptance or closure; no subagents or internal
delegation; no write outside the repository and the exact report destination.
Do not run `sudo -v` or `sudo -K`.

## Stop conditions

Grant 34/01's stop conditions remain in force. Additionally, stop and report
with the preserved evidence on: any path outside the allowlist or a worktree
set that does not match the report; conflict between retained context and
current repository evidence; material context pressure or degradation; a
failing gate whose cause cannot be classified inside the allowlist; or a client
mode that prohibits the required writes. Do not broaden scope, do not
improvise, and do not create the commit unless the full candidate evidence is
complete.

## Completion and report contract

`PASS` means the complete S6 behavior of grant 34/01 is implemented inside the
exact allowlist; the 8 missing paths exist; the mandatory scenarios have their
required evidence; the focused 96-file list and the broad `tests/unit
tests/contract tests/integration` suite have run once each on the exact
baseline route for the final candidate with truthful results; the documentation
is truthful; and exactly one local commit exists with a clean worktree and no
push. Use `Phase-qualified result: implementation-PASS` for PASS; otherwise
`not-applicable`. `Logical-whole closure: not-closed`.
`Report justification: new-mutation`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's coordinates (session 34, exchange 02) exactly once. Include the
compact core and all evidence required by grant 34/01's completion-and-report
contract: changed paths with the allowlist-subset statement; commands and exit
statuses; focused and broad results; mandatory-scenario evidence; inventory
completeness and exclusions; transaction, migration up/down and
private-state-containment receipts; the commit SHA, parent, tree, subject and
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
Downloadable prompt filename: 34_implementation_01.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 34_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

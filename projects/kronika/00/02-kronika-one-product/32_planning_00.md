# Kronika one product — S6 targeted planning revision: close G1–G3 and produce the complete allowlist

## Identity and route

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 32
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: KRONIKA-ONE-PRODUCT-S6-PLAN-REVISION
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risk: the single authorized targeted revision must convert three material open mappings into one exact, complete, issuable S6 allowlist; the Cooperator may override.
Recommended context capacity: approximately 250k tokens
Independence required: no

## Planning contract

```text
Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: close the three open S6 mappings (G1 upload/acquisition authorization and indirect test fallout; G2 approved-projection integration across live readers/writers and removal; G3 private live database/WAL/SHM boundary) and merge the candidate catalogue N, P, T and H into one complete exact S6 implementation allowlist with its focused test list and issuable next grant
Plan disposition: approval-gated
Implementation in same Worker session: prohibited
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: fresh-worker-session
Maximum plan-only cycles: 1

Planning cycle: targeted-revision
Prior planning report: 31_report_00.md
Targeted revision basis: newly-identified-material-risk
Changed decision boundary: closing G1–G3 into one complete executable S6 allowlist and indirect-test matrix
Preserved unaffected decisions: the proposed migration 0034 design; the domain/policy/service/approval design; the fail-closed seam and SQL filtering design; the access-inventory artifact design; the E3/R3 test matrix and acceptance route; the explicit exclusions; the S4-A contracts and configuration v3; parked capture work; every earlier accepted decision
Automatic targeted revisions used: 1
```

This is the single authorized targeted revision. If any mapping still cannot
be closed with repository evidence, return a terminal `PARTIAL` or `BLOCKED`
report containing exactly:

```text
Escalation disposition: NEEDS_ORCHESTRATOR_DECISION
```

Planning authority expires at the terminal planning report. This grant does
not authorize implementation, repository mutation, acceptance, publication,
deployment, host contact or closure. It does not authorize a second revision.

## Fresh-session opening

This is a genuinely fresh Worker session; inherit no prior authority. Read
the prior planning report in full before reasoning. Repository reading is
read-only. The only write this grant allows is the terminal report at its
exact destination when absent. No subagents, no tests, no interpreters, no
host, provider or credential action. `private/**` is never read.

## Starting state (verified at issuance, 2026-09-26)

- FrameNest checkout `/home/agile/Projects/framenest`; branch
  `feat/kronika-one-product`; HEAD
  `40e51cb2d061ead96850c9c94aa59de54d5e1310`; clean; local `main` =
  `origin/main` = public `refs/heads/main` = `40e51cb2…`; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.
- The prior Planner report `31_report_00.md` (session 31, status PARTIAL)
  mapped the S6 design and candidate sets N, P, T and H, identified open
  mappings G1, G2 and G3, and deliberately withheld the implementation
  grant. The Orchestrator accepts that mapped content as the basis and
  authorizes this single targeted revision to close G1–G3.
- Next migration revision remains `0034` (recheck at issuance).

## Required revision content

1. **Close G1 — upload/acquisition authorization.** For every discovered
   path and every additional caller discovered by reading the code and
   tests, specify the exact identity and ownership semantics: where
   identity-free access closes, how explicitly configured operator ownership
   is represented without inventing an administrator identity, how
   duplicate/keep-separate results and linked media are filtered without
   corrupting ingestion or recovery, and mutation/transaction checks. Read
   the relevant tests in full and enumerate every affected fixture with its
   required change. A closed mapping is the deliverable; a wildcard list is
   not.
2. **Close G2 — approved projection.** Specify the exact approved-vs-current
   selection per existing reader and writer: serialization fields, filtering
   before search/facets/counts, candidate digest and version invalidation
   across metadata edits, analysis-success updates, reapproval and safe
   referenced-media removal behavior; owner/admin working view versus
   household approved projection. Enumerate every affected test, including
   public composition, workspace/companion and requester readers.
3. **Close G3 — private live-state boundary.** Map the exact normal
   database-creation, open, WAL/SHM lifecycle and directory handling, and
   either cite the already enforced boundary with its tests or specify the
   exact code and test paths that enforce it safely. No speculative chmod
   changes and no real private state.
4. **Merge the allowlist.** Combine N, P, T, H with the G1–G3 outcomes into
   one deduplicated, exact, complete path allowlist for the S6
   implementation grant, with explicit exclusions retained.
5. **Complete the focused test list** for the declared route and state which
   tests are the causal regressions for each claim.
6. **Issue the recommended next grant** in the project's grant shape with
   the complete allowlist, the exact focused test list, the E3/R3 acceptance
   route, staging/commit rules, stops and report contract. It must be
   issuable without further mapping.
7. **State limits**: no implementation; no claims of existing proposed code;
   the parked capture module is untouched.

## Mandatory reading

- Governing WORKER spine, `RF-19`, AP planning/validation/stopping owners,
  and `.ap/INFOSEC.md` R3 material as applicable.
- `31_report_00.md` in full; `25_report_00.md` §5 and §7; `ADR-0083`.
- Every path listed in `31_report_00.md` sections 5N, 5P, 5T, 5H, 9G1,
  9G2 and 9G3, read to the depth the mapping requires; the G1/G2/G3 code and
  test files in full for their authorization and projection behavior.
- Existing conventions already cited by the prior report (migration 0033,
  `catalog_schema.py`, `engine.py`, `migrations.py`, identity access,
  content publication, application composition and route policies).

Citation rule: every material claim cites its exact source location at the
baseline; line numbers are locators.

## Authority and containment

Positive authority: read-only inspection of the named repository and trace
files; the terminal report write at the exact destination below when absent;
full readback of the saved report.

Negative authority: no repository mutation; no test, build, interpreter or
package-manager execution; no host, SSH, gate, sudo, service, browser,
provider or credential action; no `private/**`; no subagents; no network; no
second revision. Do not print hostnames, private network values, tokens,
secrets or private content.

## Completion and report contract

Status: `PASS` when the S6 allowlist and focused test list are complete and
the next grant is issuable; `PARTIAL`/`BLOCKED` with the exact escalation
disposition above when a mapping remains open. Use
`Phase-qualified result: not-applicable`, `Logical-whole closure: not-closed`,
`Report justification: new-evidence`.

Begin the report exactly with `### Report for ORCHESTRATOR_CHAT` and echo this
prompt's three coordinates exactly once. Include the compact core; the closed
G1, G2 and G3 mappings with citations; the merged exact allowlist; the focused
test list with causal justification; the issuable next grant; deviations and
missing evidence; authority expiry; and:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
Resolved Execution Issues / Near-Misses: none | <actual item>
Pre-existing Failure Classification: none | <actual classification>
```

The formal report is in English; a short completion notice to the Cooperator
is in Slovak, masculine address. Finalize the report, save it at the exact
destination, read it back in full, verify its first line, coordinates,
content and path, then send the separate short completion notice with status,
path and SHA-256. Terminal report or cancellation expires this authority.

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
Downloadable prompt filename: 32_planning_00.md
Destination path: /home/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 32_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
```

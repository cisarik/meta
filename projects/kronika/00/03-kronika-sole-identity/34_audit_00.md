# Authoritative Worker prompt — Worker session 34, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `34`, exchange `01`. Stored under the
Meta filename mapping as `34_audit_00.md`, with report destination
`34_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 34
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6GUARD — independent re-audit of the unit-directive path classification correction
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The C6 production adapter failed a live host preflight on a
foreign custom path inside an installed drop-in. The resulting correction
changes runtime transformation behavior, so it requires fresh independent
acceptance before the host window can proceed. This is the one correction
re-acceptance permitted by the finite budget; your job is to falsify the
correction, not to re-state it.

**You are independent by construction.** You did not participate in `C6-P1`,
`C6-P2`, `C6-V` or the correction. Do not trust their reports as evidence. You
do not correct findings; correction requires a separate bounded grant.

## Candidate identity

```text
Logical whole:      kronika-sole-identity
C6-P1 commit:       8a5861c792122468468b3bc20934a26cb5eb1c93
C6-P2 candidate:    24d2b7d718eb303c79197f6e2f41c81ad479a79a
C6-V audit:         28_report_00.md (the primary independent acceptance)
Correction commit:  cf76f0b3a391663db7f4b0c88b872c08b69ff279
Correction report:  33_report_00.md
Public main:        b8ec042b5bf1835df77c81341abc75e9cf8ab059
                    (the correction is local and unpublished by design)
Specification:      25_report_00.md sections 2.1, 2.2 and 2.10
```

Review the exact candidate commit `cf76f0b3a391663db7f4b0c88b872c08b69ff279` as
it exists locally, against its parent `b8ec042…`. Do not push anything.

## Verified current state, measured by the Orchestrator on 2026-10-10

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                cf76f0b3a391663db7f4b0c88b872c08b69ff279
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at cf76f0b:   4863 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     193 passed
Retention module:             15 passed
```

Re-derive these gates yourself at the start. If any fails, stop and report.

## The finding under correction

The live `migrate-identity preflight` stopped fail-closed with
`unit directive ReadWritePaths path is not classifiable` (`EXIT_MIGRATION` 27)
because an installed drop-in contained
`ReadWritePaths=/srv/media/framenest-published` — a host-side custom
media/publication path containing the retired spelling that appears nowhere in
the repository. `transform_path_value` preserves foreign/custom paths by design,
and the accepted plan says "preserve custom media roots", but the directive-level
guard refused any unchanged retired-spelling token. The correction introduces
one unified `classify_unit_path_token` used at the four derived unit-directive
guard sites, with the order frozen → moved → near-miss → foreign.

## Required review questions

1. **Identity and scope.** Confirm the candidate commit, parent, the three
   changed paths, and that no other path changed. Confirm
   `classify_unit_path_token` exists with the stated classification order, that
   `MIGRATION_FROZEN_PATH_PREFIXES`, `MIGRATION_OLD_TO_NEW_ROOTS` and
   `MIGRATION_SEGMENT_RENAMES` are unchanged, and that all error codes and
   messages are unchanged except as the classification requires.
2. **Guard-site completeness.** Re-derive every site where an unchanged
   retired-spelling token could raise. Confirm the four unit-directive sites use
   the unified classifier. Report the same-shaped site the correction left
   unchanged (`_transform_sudoers_command`) and judge whether leaving it is
   correct for this correction's scope; state the residual host risk it creates
   for the next preflight window.
3. **Independent matrix, all four site shapes** (`ReadWritePaths`-style token
   lists, `LoadCredential`, `Exec*` plain, `Exec*={ path=… }`): frozen token
   preserved; foreign/custom token containing the retired spelling preserved
   (synthetic path); near-miss variant of a moved root (`<root>-old`,
   `<root>x`, `<root>.env` style) refused; token under a moved root transformed;
   token under a moved root with leftover retired spelling refused; one mixed
   directive with a foreign and a moved token together; and the Exec argument
   opacity case.
4. **Judge the two accepted deviations.** (a) The Exec plain guard now classifies
   the executable token only, so argument text carrying the retired spelling is
   preserved rather than refused. (b) A relative or otherwise foreign
   `LoadCredential` path containing the retired spelling is now preserved. State
   whether each is correct, narrow, and acceptable for the host window, or a
   blocking issue.
5. **Independent mutation probes.** Build your own in-memory reversions (do not
   reuse the correction's probe): removing the foreign-preserve behavior must
   make the foreign test fail; weakening the near-miss rule must make the
   near-miss test fail; removing the frozen branch must make the frozen
   classification assertion fail. Report each mutation, test and observed
   outcome; a mutation that does not fail its test is a finding.
6. **Reconstruct the baseline refusal read-only.** From the parent blob
   (`git show b8ec042:deploy/ubuntu/kronika_release.py`) and a synthetic foreign
   token, demonstrate the pre-correction refusal shape and the post-correction
   preservation without checking out or mutating anything.
7. **Re-run authorized checks:** the focused migration module, the retention
   module, and the declared full Python suite at the candidate. Report counts
   and any difference from `4863/8/3/0`. Confirm Part A (86 document and 36
   Alembic keys) and Part B (20) unchanged.
8. **Disposition.** Report every untested site and every residual risk. **Any
   blocking finding blocks the C6 host window.** If a design assumption survives
   this correction and your recheck unchanged, report:
   `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## Authority

```text
Positive authority: read any tracked file in /home/agile/Projects/kronika; read
  the Meta trace files named above; run read-only Git inspection including
  `git show` of the parent blob; run the declared focused and full AP test
  operations against the candidate baseline; construct bounded in-memory or
  isolated synthetic probe state that mutates nothing durable.

Negative authority: ANY repository or durable-state mutation; any correction or
  edit; any commit, branch, tag, merge, rebase, stash or history rewrite; any
  checkout or restore of another revision; any push; any NUC contact or SSH; any
  migration invocation; any provider, browser or capture contact; any secret or
  personal-configuration read; any writing of the report to a file.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline cf76f0b3a391663db7f4b0c88b872c08b69ff279
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline cf76f0b3a391663db7f4b0c88b872c08b69ff279 --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run`, including as a text editor.
  Read-only Git inspection allowed; no Git write. Any other command must be
  stated in the report with its purpose and a confirmation that it mutated
  nothing.

Dependency authority: none.
Git authority: none.
Network authority: none.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. Reports
  26, 27, 28 and 33 are claims, not evidence. On conflict between retained
  context and current repository evidence, stop.
Side-effect authority: none. Temporary probe state must be isolated, non-secret,
  outside project state, and removed or reported.
Browser authority: none.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository or AP gate does
  not match; if the candidate cannot be fixed as an exact identity; if a
  required classification case cannot be exercised without mutation or host
  contact; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded audit.

Completion: the identity, scope, guard-site set, matrix, mutation probes, the
  two deviations and the baseline reconstruction all reported; focused and full
  checks re-run; findings disposed as blocking or non-blocking; tree clean and
  HEAD unchanged; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `34_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No implementation, no correction, no commit, no push, no
  publication, no host contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-evidence`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `34` and exchange `01` unchanged. Then:

1. Identity, scope and gate verification, including the exact candidate commit.
2. The derived guard-site set and the disposition of the unchanged sudoers site.
3. The independent matrix results per site shape.
4. Judgment of the two accepted deviations.
5. Mutation-probe results, each with mutation, test and observed outcome.
6. The read-only baseline reconstruction.
7. Focused and full-suite check results, and Part A/Part B evidence.
8. Findings with blocking/non-blocking disposition and every untested site.
9. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `deploy/ubuntu/kronika_release.py` — `classify_unit_path_token`,
  `_systemd_transform_value`, `transform_unit_dropin_text`,
  `transform_path_value`, `_transform_sudoers_command`, the frozen/moved/rename
  constants.
- `tests/contract/test_kronika_identity_migration.py` — the transformer tests and
  the correction's new matrix.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/33_report_00.md`
  in full — the correction's claims under review.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/28_report_00.md`
  section 2 row 13 and section 4 — the behavior this correction narrows.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.10 — the preservation clause.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator note

This is the correction re-acceptance allowed by the finite budget: one primary
fresh acceptance (`C6-V`) and one correction re-acceptance. Its result gates the
host window: a `PASS` with no blocking finding permits re-running the
`migrate-identity preflight`; a blocking finding requires
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and the Orchestrator takes
it to the Cooperator. Do not expand into an unknown-unknown hunt: the review is
bounded to the correction, the transformer it touches, and the stated claims.

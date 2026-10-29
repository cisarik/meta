# Authoritative Worker prompt — Worker session 37, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `37`, exchange `01`. Stored under the
Meta filename mapping as `37_audit_00.md`, with report destination
`37_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 37
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6ENC2 — independent re-audit of the escaped revision-token repair
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The previous independent re-audit blocked the C6 host window
on B1: the revision-form executable transformer silently altered escaped
frozen/foreign tokens. A bounded repair now exists. Because the repair changes
runtime behavior on the parser/serializer boundary, it needs fresh independent
acceptance before the host window may proceed. Your job is to falsify the repair.

**This audit supersedes a prerequisite-stopped attempt.** Session 36 exchange 01
stopped `BLOCKED` because its prompt named the repair report at a stale path
after the report had been renamed; it performed no review work and found no
candidate defect. This prompt names the verified path. Do not treat the session-36
stop as evidence about the candidate.

**You are independent by construction.** You did not participate in `C6-P1`,
`C6-P2`, `C6-V`, the guard correction or the encoding repair. Do not trust their
reports as evidence. You do not correct findings; correction requires a separate
bounded grant.

## Candidate identity

```text
Logical whole:      kronika-sole-identity
Guard correction:   cf76f0b3a391663db7f4b0c88b872c08b69ff279
Encoding repair:    78cba281960e2f17137647bcc90aab83847a1c0c
Repair report:      35_report_00.md (session 35 / exchange 01, KSI-CORR-C6ENC)
B1 evidence:        34_report_00.md section 8
Correction audit:   34_report_00.md (BLOCKED on B1)
Prerequisite stop:  36_report_00.md (no review work performed)
Public main:        b8ec042b5bf1835df77c81341abc75e9cf8ab059
                    (the repair is local and unpublished by design)
Specification:      25_report_00.md sections 2.1, 2.2 and 2.10
```

Review the exact candidate commit `78cba281960e2f17137647bcc90aab83847a1c0c` as
it exists locally, against its parent `cf76f0b…`. Do not push anything.

## Verified current state, measured by the Orchestrator on 2026-10-10

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                78cba281960e2f17137647bcc90aab83847a1c0c
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 78cba28:   4873 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     203 passed
Retention module:             15 passed
```

Re-derive these gates yourself at the start. If any fails, stop and report.

## What B1 was, and what the repair claims

B1: for `Exec*={ path=… }`, the transformer decoded the captured executable and,
for frozen/foreign classifications, inserted the decoded text back, losing
systemd escaping. Example: `path=/srv/audit34/framenest\x20assets` became
`.../framenest assets`, reparsing to a different executable.

The repair claims: frozen and foreign revision commands are returned unchanged
(byte-identical token); moved tokens are rewritten only from their raw text via
`_render_moved_revision_token`; the caller splices at the parser match span and
accepts only when the engine's own parser captures the rendered token and
`_unescape_unit_text` of that capture equals `transform_path_value(decoded)`;
unprovable raw forms fail closed with `unit directive <key> revision path is not
provably transformable` (exit 27).

## Required review questions

1. **Identity and scope.** Confirm the candidate commit, parent, the three
   changed paths, and no other path. Confirm the decode-and-reinsert statement is
   gone, `_render_moved_revision_token` exists with the claimed contract, the
   constants are unchanged, and near-miss / under-root-leftover messages and exit
   codes are unchanged.
2. **B1 fixed.** Independently reproduce byte-identity for frozen and foreign
   escaped revision tokens, and that a moved token with an escaped remainder
   reparses (engine parser) to exactly the intended canonical executable and is
   idempotent. Compare with the parent behavior (read-only `git show`).
3. **Regression of the correction.** Re-derive the guard sites and re-run the
   frozen/foreign/near-miss/moved/leftover matrix across the four site shapes.
   Confirm the refusals still fire, including escaped near-miss and escaped
   under-root-leftover forms, and the three unprovable raw forms fail closed.
4. **The repair report's LEAD.** Probe whether plain `Exec*`, path-list and
   `LoadCredential` raw-token classification can be evaded or altered by an
   escaped form (for example an escaped slash inside or at the end of a moved
   root). Report the observed behavior and whether each case is fail-closed or
   preserved. Act on evidence, not on this prompt's wording.
5. **Independent mutation probes.** Build your own in-memory reversions: restore
   the decode-and-reinsert at the frozen/foreign return (byte-identity tests must
   fail); emit decoded remainder segments (the reparse guard must fail); remove
   the byte-identity return entirely (must fail). Report each mutation, test and
   observed outcome; a mutation that does not fail its test is a finding.
6. **Checks.** Re-run the focused migration module, the retention module, and the
   declared full Python suite at the candidate. Report counts and any difference
   from `4873/8/3/0`. Confirm Part A (86 document and 36 Alembic keys) and Part B
   (20) unchanged.
7. **Disposition.** Report every untested site (the repair report's section 7 is a
   claim to check), every residual risk, and whether any blocking finding
   remains. The unchanged sudoers-command guard remains a known fail-closed host
   risk for the next preflight; state it as residual, not as this repair's defect.
8. If a design assumption survives this repair and your recheck unchanged,
   report exactly:
   `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`

## Authority

```text
Positive authority: read any tracked file in /home/agile/Projects/kronika; read
  the Meta trace files named above; run read-only Git inspection including
  `git show` of parent blobs; run the declared focused and full AP test
  operations against the candidate baseline; construct bounded in-memory or
  isolated synthetic probe state that mutates nothing durable.

Negative authority: ANY repository or durable-state mutation; any correction or
  edit; any commit, branch, tag, merge, rebase, stash or history rewrite; any
  checkout or restore of another revision; any push; any NUC contact or SSH; any
  migration invocation; any provider, browser or capture contact; any secret or
  personal-configuration read; any writing of the report to a file; any direct
  invocation of `.venv/bin/python`, `python`, `python3` or `poetry run` outside
  the declared AP route — including as a text counter.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 78cba281960e2f17137647bcc90aab83847a1c0c
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 78cba281960e2f17137647bcc90aab83847a1c0c --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Read-only Git inspection
  allowed; no Git write. Any other command must be stated in the report with
  its purpose and a confirmation that it mutated nothing.

Dependency authority: none.
Git authority: none.
Network authority: none.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. Reports
  33, 34, 35 and 36 are claims, not evidence. On conflict between retained
  context and current repository evidence, stop.
Side-effect authority: none. Temporary probe state must be isolated, non-secret,
  outside project state, and removed or reported.
Browser authority: none.
```

## Finishing

```text
Stopping conditions: stop without improvising if the repository or AP gate does
  not match; if the candidate cannot be fixed as an exact identity; if a
  required case cannot be exercised without mutation or host contact; if
  context pressure reaches the point where a bounded rotation is cheaper than a
  degraded audit.

Completion: identity, scope, B1-fixed evidence, regression matrix, the LEAD
  probes, mutation results, checks and dispositions all reported; tree clean and
  HEAD unchanged; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `37_report_00.md` in
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
echoing `kronika-sole-identity`, session `37` and exchange `01` unchanged. Then:

1. Identity, scope and gate verification, including the exact candidate commit.
2. B1-fixed evidence: byte-identity, reparse and idempotence.
3. Regression matrix across the site shapes.
4. The LEAD probe results.
5. Mutation-probe results, each with mutation, test and observed outcome.
6. Focused and full-suite check results, and Part A/Part B evidence.
7. Findings with blocking/non-blocking disposition and every untested site.
8. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `deploy/ubuntu/kronika_release.py` — the revision branch,
  `_render_moved_revision_token`, `UNIT_EXEC_PATH`, `_unescape_unit_text`,
  `classify_unit_path_token`, `transform_path_value`.
- `tests/contract/test_kronika_identity_migration.py` — the repair's tests and
  the earlier matrix.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/35_report_00.md`
  in full — the repair claims under review.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/34_report_00.md`
  section 8 — B1's evidence.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/33_report_00.md`
  — the correction under regression.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator note

This re-audit gates the C6 host window together with the earlier C6-V result: a
`PASS` with no blocking finding permits re-running the `migrate-identity
preflight`; a blocking finding requires
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION` and the Orchestrator takes
it to the Cooperator. The review is bounded to the repair, its regression and
the stated claims; do not expand into an unknown-unknown hunt.

# Authoritative Worker prompt — Worker session 39, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `39`, exchange `01`. Stored under the
Meta filename mapping as `39_audit_00.md`, with report destination
`39_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 39
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6UNK — independent re-audit of the unknown-directive policy
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The live C6 preflight stopped on a benign host drop-in
directive outside the transformer's supported set. A bounded correction replaced
the blanket unknown-directive refusal with a policy: preserve brand-free unknown
directives; refuse when the key or value carries the retired spelling. This
changes transformer runtime behavior, so it needs fresh independent acceptance
before the preflight may be re-run. Your job is to falsify the correction.

**You are independent by construction.** You did not participate in `C6-P1`,
`C6-P2`, `C6-V`, the guard correction, the encoding repair or this policy
correction. Do not trust their reports as evidence. You do not correct findings.

## Candidate identity

```text
Logical whole:       kronika-sole-identity
Encoding repair:     78cba281960e2f17137647bcc90aab83847a1c0c
Policy correction:   980041cf13dd427e77263f573694aed7c1a54018
Correction report:   38_report_00.md
Accepted transformer state: 33_report_00.md, 35_report_00.md, 37_report_00.md
Public main:         78cba281960e2f17137647bcc90aab83847a1c0c
                     (the correction is local and unpublished by design)
Specification:       25_report_00.md sections 2.1, 2.2 and 2.10
```

Review the exact candidate commit `980041cf13dd427e77263f573694aed7c1a54018` as
it exists locally, against its parent `78cba28…`. Do not push anything.

## Verified current state, measured by the Orchestrator on 2026-10-11

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                980041cf13dd427e77263f573694aed7c1a54018
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at 980041c:   4877 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     207 passed
Retention module:             15 passed
```

Re-derive these gates yourself at the start. If any fails, stop and report.

## What the correction claims

For a directive outside the supported sets, the transformer now refuses only
when the directive key or value contains the retired spelling (case-insensitive)
and otherwise returns the value unchanged; the refusal keeps the message
`unit directive <key> is not supported` and exit 27. The live host's only
unsupported key is the plain, brand-free `RuntimeDirectoryMode=0700`.

## Required review questions

1. **Identity and scope.** Confirm the candidate commit, parent, the three
   changed paths and no other path. Confirm the terminal branch implements
   exactly the stated policy, that the supported-directive branches, the
   classifier, the revision renderer and all other refusals are byte-unchanged,
   and that key/value checks are case-insensitive.
2. **Policy matrix.** Independently exercise: brand-free unknown preserved
   byte-for-byte (`RuntimeDirectoryMode=0700`, `Environment=FOO=bar`,
   `UnknownDirective=value`); brand-bearing unknown refused with the same
   message and exit 27 for a value variant, an uppercase value variant, a
   mixed-case value variant, and a key variant; an end-to-end
   `read_migration_observation` install of a `RuntimeDirectoryMode` drop-in.
   Confirm supported directives are untouched.
3. **Adjusted tests are not weakened.** For each adjusted existing test line,
   verify the refusal assertion is still genuine (the fixture now carries the
   spelling) and that the preservation contract is separately pinned. Report
   every adjusted line and your verdict.
4. **Regression.** Re-run the previously audited matrices: the four guard sites
   (frozen/foreign/near-miss/moved/leftover), escaped revision-form byte
   identity and reparse, unprovable-form refusals, and the sudoers guard
   refusal. Report any behavior difference from the accepted state.
5. **The correction report's LEAD.** Probe an unknown directive whose value
   encodes the spelling with escapes (for example
   `Environment=FOO=fra\x6denest`): the policy's textual check preserves it.
   Investigate read-only whether systemd would decode such an escape in that
   directive at runtime; if that cannot be established locally, report it as an
   unverified residual and state whether it affects the observed live set (the
   live unknown key is plain and brand-free).
6. **Independent mutation probes.** Remove the brand check (brand-bearing tests
   must fail); force refusal for brand-free unknowns (preservation tests must
   fail); make the value check case-sensitive (the uppercase/mixed-case tests
   must fail). Report each mutation, test and observed outcome.
7. **Checks.** Re-run the focused migration module, the retention module and the
   declared full Python suite at the candidate. Report counts and any difference
   from `4877/8/3/0`. Confirm Part A (86 document and 36 Alembic keys) and Part B
   (20) unchanged.
8. **Disposition.** Report every untested site, every residual risk, and whether
   any blocking finding remains. If a design assumption survives this correction
   and your recheck unchanged, report exactly:
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
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline 980041cf13dd427e77263f573694aed7c1a54018
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 980041cf13dd427e77263f573694aed7c1a54018 --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Read-only Git inspection
  allowed; no Git write. Any other command must be stated in the report with
  its purpose and a confirmation that it mutated nothing.

Dependency authority: none.
Git authority: none.
Network authority: none.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. Reports
  33–38 are claims, not evidence. On conflict between retained context and
  current repository evidence, stop.
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

Completion: identity, scope, policy matrix, adjusted-test verdicts, regression,
  the LEAD probe, mutation results, checks and dispositions all reported; tree
  clean and HEAD unchanged; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `39_report_00.md` in
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
echoing `kronika-sole-identity`, session `39` and exchange `01` unchanged. Then:

1. Identity, scope and gate verification, including the exact candidate commit.
2. The policy matrix results.
3. Adjusted-test verdicts for every adjusted line.
4. Regression results across the previously audited matrices.
5. The LEAD probe result and its disposition.
6. Mutation-probe results, each with mutation, test and observed outcome.
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

- `deploy/ubuntu/kronika_release.py` — `transform_unit_dropin_text`,
  `_systemd_transform_value` and its supported sets.
- `tests/contract/test_kronika_identity_migration.py` — the adjusted tests, the
  new preservation tests and the full matrix.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/38_report_00.md`
  in full — the claims under review.
- `35_report_00.md` and `37_report_00.md` — the accepted repair and re-audit the
  regression must reproduce.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator note

This re-audit gates the C6 host window: a `PASS` with no blocking finding
permits publishing `980041c` and re-running the `migrate-identity preflight`; a
blocking finding requires `Escalation disposition:
NEEDS_ORCHESTRATOR_DECISION`. The observed live host set is fully derived, so
this correction is expected to be the last preflight form fix; judge it on the
evidence in front of you, not on that expectation.

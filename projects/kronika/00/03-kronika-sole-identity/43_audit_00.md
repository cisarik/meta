# Authoritative Worker prompt — Worker session 43, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `43`, exchange `01`. Stored under the
Meta filename mapping as `43_audit_00.md`, with report destination
`43_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 43
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit, read-only
Task identity: KSI-AUDIT-C6COMP — fresh independent re-audit of the C6 completion correction
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The completed C6 identity-migration window required one
bounded correction set for three live defects: the Tailscale ingress guard, the
generated replacement spelling, and environment-file permission parity. The
correction changes fail-closed decision logic and plan-bound evidence in the
migration engine, so it needs fresh independent acceptance before the failed C6
journal is archived and C6 is closed. Your job is to falsify it.

**You are independent by construction.** You did not participate in `C6-P1`,
`C6-P2`, `C6-V`, the guard correction, the B1 repair, the unknown-directive
policy, the process-query correction or this C6 completion correction. Do not
trust their reports as evidence. You do not correct findings.

## Candidate identity

```text
Logical whole:         kronika-sole-identity
C6 completion candidate: e9413dff98605443e7d17557f498c87433c93e92
Parent:                fcde631047650d1ff0a84b84bf185b54d6d11ba5
Correction prompt:     42_correction_00.md
Correction report:     42_report_00.md
Live failure evidence: 00_notes.md tail (apply refused; host completed manually)
Public main:           fcde631047650d1ff0a84b84bf185b54d6d11ba5
                       (the correction is local and unpublished by design)
Specification:         25_report_00.md remaining sequence
```

Review the exact candidate commit `e9413dff98605443e7d17557f498c87433c93e92`
as it exists locally, against its parent `fcde631…`. Do not push anything.

## Verified current state, measured by the Orchestrator on 2026-10-12

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                e9413dff98605443e7d17557f498c87433c93e92
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at parent:    4901 passed, 8 skipped, 3 warnings, 0 failed
Candidate focused module:     285 passed
Candidate retention module:   15 passed
Candidate full suite:         4955 passed, 8 skipped, 3 warnings, 0 failed
```

Re-derive these gates yourself at the start. If any fails, stop and report.

## What the correction claims

Three defects, one commit, exactly two changed paths
(`deploy/ubuntu/kronika_release.py`,
`tests/contract/test_kronika_identity_migration.py`):

**D-1.** `parse_tailscale_serve_status`, the `replace_tailscale_handler` guard
and `verify_ingress` now share one accepted-spelling source of truth
(`tailscale_unix_targets`): both `unix+http://<socket>` and `unix:<socket>` are
former-handler spellings; the guard accepts exactly those two and refuses
everything else; the verifier accepts both new spellings. Live defect: the
guard accepted only `unix+http://<old>` while the classifier classified the
live `unix:<old>` handler as the former handler, so the apply refused
post-write at phase `replace-tailscale-handler` with `existing ingress handler
target is unexpected`.

**D-2.** The replacement target mirrors the observed former handler's scheme:
`unix:<old>` → `unix:<new>`, `unix+http://<old>` → `unix+http://<new>`. Live
defect: the generated `unix+http://<new>` was rejected by the installed
Tailscale (`must be a URL starting with one of the supported schemes: [http
https https+insecure unix]`); the host's accepted spelling is `unix:`.

**D-3.** The environment file evidence (`owner:group:mode <sha256>`) is read in
`read_migration_observation`, bound through `MigrationObservation` and
`MigrationPlan` into the plan digest, and the transformed file is installed
with the observed owner/group/mode applied and verified after the atomic move,
with the source content digest checked against the raw (unstripped) former
content. Live defect: the former file was `0640 root:framenest` (readable by
the service account); the installation produced `0600 root:root`, which broke
the documented service-account status routes
(`framenest-db status` → `FRAMENEST_DB_CONFIGURATION_FAILED`,
`kronika-release status` exit 20) until manually remediated.

**Material qualification the correction report states explicitly.** The
prompt's literal D-3 intermediate expectation (`chown root:kronika` inside
`transform_environment`) cannot coexist with the unchanged phase order:
`transform-environment` precedes `rename-account`, so the canonical group does
not exist at installation time. The implementation applies and verifies the
observed group name pre-rename and relies on the existing, unchanged group
rename to canonicalize it (`root:framenest:640` → installed
`root:framenest:640` → final `root:kronika:640`). It also refuses a
former-account-owned former file. Both choices need your independent verdict.

## Required review questions

1. **Identity and scope.** Confirm the candidate commit, parent, exactly the
   two changed paths and no other path; no documentation, configuration,
   dependency, lockfile, Alembic revision, AP file or retention ledger change;
   the apply phase order, phase names, `_MIGRATION_PHASE_METHODS` mapping,
   journal and receipt shapes and recovery semantics unchanged; the engine
   outside the changed sites byte-identical to the parent; the correction
   prompt's negative authority honored.
2. **Ingress matrix, independently constructed.** Both former spellings round
   trip to the mirrored new spelling with exactly one `tailscale serve --bg`
   command and no `reset`; an unrelated handler is preserved; foreign HTTP
   targets, foreign sockets, empty proxies, `unix://` and near-miss prefixes
   are never classified as former and never replaced; duplicate former handlers
   (including mixed spellings) refuse; zero handlers is an exact no-op; a
   forged `old_handlers` index pointing at a foreign target still refuses; the
   mount guard, `--bg`-only behavior and return shapes are unchanged. State any
   input where the classifier, guard and verifier could disagree.
3. **Environment parity matrix, independently constructed.** Live shape
   `root:framenest:640`; non-account groups preserved exactly without widening
   access; absent, unsafe, `query-failed`, malformed, `UNKNOWN` owner/group,
   invalid mode or digest evidence fail closed with `EXIT_MIGRATION`; installed
   owner, group, mode or digest mismatch refuses; staged-write,
   canonical-assertion and atomic-move failures preserve the prior destination.
   Verify the evidence binding end to end: observation → plan digest →
   apply-time drift refusal → installed verification; and that the source
   content digest is checked against the raw former content including its final
   newline. Name anything the plan digest does not bind that it should.
4. **D-3 phase-order interpretation — required verdict.** Confirm from
   `MIGRATION_PHASES` that `transform-environment` precedes `rename-account`;
   confirm the rename implementation preserves UID/GID and canonicalizes names,
   so the pre-rename group assignment becomes `root:kronika:640` in the final
   state; and state whether any parity gap remains for the live shape, for
   non-account groups, and for a former-account-owned former file (assess the
   refusal: fail-closed-correct or an unsupported legitimate shape?). Give an
   explicit disposition for each.
5. **Mutation probes.** Inspect the committed mutation demonstrations
   (`test_c6_completion_mutation_demonstrations` and friends): confirm they are
   in-memory only (no production-file writes), cover `old-only-guard`,
   `fixed-replacement`, `no-ownership`, `no-mode` and `no-verification`, and
   that each mutation is detected with the stated failure. If you can construct
   one additional bounded in-memory mutation this prompt did not name, report
   its outcome.
6. **Checks.** Re-run at the candidate, through the declared route: the focused
   migration module, the retention module, and the declared full Python suite.
   Report counts, elapsed time and any difference from `285`, `15` and
   `4955/8/3/0`. Independently verify Part A (86 frozen document hashes, 36
   Alembic revision keys), Part B (20 tracked retired-basename paths) and the
   Part C no-movement claim; the retention ledger is unmodified in the
   candidate, so state how the green run and your own spot measurements
   establish this.
7. **Disposition.** Report every untested site and residual risk with
   blocking/non-blocking classification. If a design assumption survives this
   correction and your recheck unchanged, report exactly:
   `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

## Authority

```text
Positive authority: read any tracked file in /home/agile/Projects/kronika; read
  the Meta trace files named above; run read-only Git inspection including
  `git show` of parent and candidate blobs; run the declared focused and full AP
  test operations against the candidate baseline; construct bounded in-memory
  or isolated synthetic probe state that mutates nothing durable.

Negative authority: ANY repository or durable-state mutation; any correction or
  edit; any commit, branch, tag, merge, rebase, stash or history rewrite; any
  checkout or restore of another revision; any push; any NUC contact or SSH; any
  migration invocation; any provider, browser or capture contact; any secret or
  personal-configuration read; any writing of the report to a file; any direct
  invocation of `.venv/bin/python`, `python`, `python3` or `poetry run` outside
  the declared AP route — including as a text counter.

Commands: Python evidence only through
  ./.ap/ap project check --root /home/agile/Projects/kronika --baseline fcde631047650d1ff0a84b84bf185b54d6d11ba5
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline fcde631047650d1ff0a84b84bf185b54d6d11ba5 --operation <id> [-- <argv>]
  (operations: runtime-info, test, test-focus). Read-only Git inspection
  allowed; no Git write. Any other command must be stated in the report with
  its purpose and a confirmation that it mutated nothing.

Dependency authority: none.
Git authority: none.
Network authority: none.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. Reports
  33–42 are claims, not evidence. On conflict between retained context and
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

Completion: identity, scope, ingress matrix, environment parity matrix,
  phase-order verdicts, mutation results, checks and dispositions all reported;
  tree clean and HEAD unchanged; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `43_report_00.md` in
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
echoing `kronika-sole-identity`, session `43` and exchange `01` unchanged. Then:

1. Identity, scope and gate verification, including the exact candidate commit.
2. The ingress spelling and refusal matrix results.
3. The environment parity, evidence-binding and fail-closed matrix results.
4. The D-3 phase-order verdicts with their evidence.
5. Mutation-probe results, each with mutation, test and observed outcome.
6. Focused, full-suite and retention check results, and Part A/Part B/Part C
   evidence.
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

- `deploy/ubuntu/kronika_release.py` — `tailscale_unix_targets`,
  `parse_tailscale_serve_status`, `replace_tailscale_handler`, `verify_ingress`,
  `parse_environment_file_evidence`, `environment_file_ownership`,
  `transform_environment`, `read_migration_observation`, `build_migration_plan`,
  `MIGRATION_PHASES`, the rename-account implementation and
  `cmd_remote_root_file_evidence`.
- `tests/contract/test_kronika_identity_migration.py` — the C6 completion
  tests and mutation demonstrations.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/42_report_00.md`
  in full — the claims under review — and `42_correction_00.md`.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/00_notes.md`
  tail — the live failure evidence and host state.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator note

This re-audit gates the close of the C6 window: a `PASS` with no blocking
finding permits archiving the failed C6 journal under bounded authority and
closing C6; any blocking finding returns to bounded correction. The live host
was already completed manually and needs no contact; this review concerns the
corrected repository behavior only. Judge it on the evidence in front of you.

# Authoritative Worker prompt — Worker session 35, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `35`, exchange `01`. Stored under the
Meta filename mapping as `35_correction_00.md`, with report destination
`35_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 35
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C6ENC — preserve encoding for untransformed revision-form executable tokens
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The independent re-audit demonstrated that the revision-form
`Exec*={ path=… }` transformer silently changes the executable field for frozen
and foreign tokens containing systemd escapes. The host window is blocked by
this finding. The repair is narrow but touches a parser/serializer boundary, so
the proof must be byte-level and reparse-based; a fresh independent re-audit
follows before the preflight can be re-run.

## The finding, exactly

From `34_report_00.md` section 8 (B1), independently reproduced by the audit:

```text
Input:  ExecStart={ path=/srv/audit34/framenest\x20assets ; argv[]=audit34 ; }
Output: ExecStart={ path=/srv/audit34/framenest assets ; argv[]=audit34 ; }
```

The output reparses to executable `/srv/audit34/framenest` plus argument
`assets` — a different executable. The same happens for a frozen token. The
parent commit `b8ec042` refused both inputs with
`unit directive ExecStart path is not classifiable` (exit 27); the correction
`cf76f0b` accepts them but alters the field.

Cause, confirmed by reading the candidate:
`deploy/ubuntu/kronika_release.py` revision-form branch (lines 4288-4309):
`original = _unescape_unit_text(match.group(1))` decodes the captured token,
classification runs on the decoded value, and the frozen/foreign path returns
`command.replace(match.group(1), original, 1)` — inserting the decoded text and
losing the encoding. The plain-exec, path-list and `LoadCredential` branches
already operate on raw text and preserve encoding.

## Repair specification

1. **Frozen and foreign revision tokens are preserved byte-identically.** The
   output command must contain the captured token exactly as it appeared;
   no decode/re-insert may occur for these classifications.
2. **Moved revision tokens transform while preserving the remainder's
   encoding.** The transformed output must reparse, using the engine's own
   executable-path parser (`UNIT_EXEC_PATH` + `_unescape_unit_text`), to exactly
   the intended new executable path. Recommended approach: operate on the raw
   captured token where its moved-root prefix is literal (the roots contain no
   escapes), and fail closed if the raw form cannot be transformed provably.
   Document the chosen approach.
3. **Refusals unchanged.** Near-miss tokens and under-a-moved-root tokens whose
   decoded path still carries the retired spelling remain refused with the same
   messages and exit codes.
4. **No other behavior change.** Do not alter the other branches, the
   classifier, the frozen/moved/rename constants, sudo rules, environment
   transformation, or any error code.
5. **Derive, do not assume.** Check every branch that decodes and re-renders a
   token for the same defect class and report the derived set. If another branch
   has the same mismatch, include it in the repair under this grant; if none,
   say so with evidence.
6. **Tests** in `tests/contract/test_kronika_identity_migration.py`:
   - frozen escaped revision token preserved byte-for-byte;
   - foreign escaped revision token preserved byte-for-byte (synthetic path);
   - moved revision token whose remainder contains an escaped space: output
     reparses to the intended canonical executable, and the remainder encoding
     is intact;
   - moved plain revision token unchanged from current behavior;
   - near-miss and under-root-leftover refusals still fire, including an escaped
     near-miss form;
   - reparse assertions use the engine's own parser, not string equality alone;
   - the existing matrix and other tests stay green.
7. **Mutation demonstrations** for the preservation fix: removing the
   byte-identical preservation makes the frozen/foreign escaped tests fail;
   breaking the moved reparse makes the moved escaped test fail. Name each
   mutation and observed failure.

## Verified starting state, measured by the Orchestrator on 2026-10-10

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                cf76f0b3a391663db7f4b0c88b872c08b69ff279
Public main:                  b8ec042b5bf1835df77c81341abc75e9cf8ab059
                              (the candidate is local and unpublished, by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at cf76f0b:   4863 passed, 8 skipped, 3 warnings, 0 failed
Focused migration module:     193 passed
Retention module:             15 passed
```

**No host contact.** The live host supplied the original finding; this repair is
repository-only with synthetic fixtures.

## Authority

```text
Positive authority: edit `deploy/ubuntu/kronika_release.py` for exactly the
  revision-form encoding repair and any same-class branch your derivation names;
  edit `tests/contract/test_kronika_identity_migration.py` for the tests and
  mutation demonstrations; edit `tests/contract/test_kronika_identity_retention.py`
  only to re-pin a Part C scalar that your own measurement shows this repair
  moved, with the arithmetic cause stated; create exactly one local non-amended
  commit on `main`.

Negative authority: every other path; any dependency or lockfile change; any
  change to `pyproject.toml`, `ap.project.conf` or the `.ap` gitlink; any frozen
  document or Alembic revision; publication; push; force; amend; branch; stash;
  any NUC contact or SSH; any migration invocation; any provider, browser or
  capture contact; any secret or personal-configuration read. If a necessary
  change falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline cf76f0b3a391663db7f4b0c88b872c08b69ff279 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`, including as a text
  editor. Read-only Git inspection allowed; exactly one `git add <exact paths>`
  and one `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only.
Browser authority: none.
```

## Verification

1. Reproduce B1 before editing with the audit's exact shape (escaped-space
   frozen and foreign revision tokens), showing the altered field and the
   reparse difference. Record it.
2. After the repair, the same inputs are byte-identical, and the moved escaped
   case reparses to the intended canonical executable.
3. Derive and report the complete decode/re-render branch set.
4. Mutation demonstrations as specified.
5. Run, through the declared route: the focused migration module, then the
   declared full Python suite, then the retention module. Report every count,
   elapsed time and any difference from the `4863/8/3/0` baseline.
6. Report **every moved or removed site that no test exercises**, and every
   branch your derivation found that this prompt did not name.
7. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement. Never tune a pin until a suite is green.

## Derivation and defect-pattern discipline

```text
 1. Derive the branch list by PARSING the transformer. Locators are not an
    inventory.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Reject a guard that can pass vacuously when its input is absent.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Preservation must fail loudly rather than silently alter a
token; the reparse contract is the pin.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the raw-token transformation cannot be made provable and reparse
  verification is impossible; if a change would weaken any near-miss or
  under-root refusal; if a frozen hash, Part A or Part B moves; if a Part C
  re-pin cannot be reproduced from your own measurement; if a necessary change
  falls outside the positive scope.

Completion: B1 reproduced and repaired; byte-identity and reparse proofs green;
  mutation demonstrations green; focused module, full declared Python suite and
  retention module green through the declared route; one local commit; report
  delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `35_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no host contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `35` and exchange `01` unchanged. Then:

1. The B1 reproduction before the edit, with the exact altered output and
   reparse difference.
2. The repair approach and the derived decode/re-render branch set.
3. Byte-identity and reparse evidence for frozen, foreign and moved escaped
   cases.
4. Mutation demonstrations, each with its named mutation.
5. Focused module, full-suite and retention counts with elapsed time and any
   baseline difference.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and Part C
   movement with cause.
7. Every site no test exercises.
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

- `deploy/ubuntu/kronika_release.py` — the revision-form and plain-exec
  branches, `UNIT_EXEC_PATH`, `_unescape_unit_text`, `classify_unit_path_token`,
  `transform_path_value`.
- `tests/contract/test_kronika_identity_migration.py` — the transformer tests
  and the correction's matrix.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/34_report_00.md`
  sections 3, 8 and the critique — B1's evidence under repair.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/33_report_00.md`
  — the correction this repair builds on.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify: B1's byte-identity and
reparse proofs; the derived branch set; the refusals unchanged; the full suite
green at the reported commit; and Part A and Part B unmoved. **A fresh
independent re-audit of this repair is the next step**, and only after its PASS
may the C6-H preflight be re-run. The sudoers-command guard's residual host risk
remains recorded for that window.

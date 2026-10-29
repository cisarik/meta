# Authoritative Worker prompt — Worker session 64, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `64`, exchange `01`. Stored under the
Meta filename mapping as `64_implementation_00.md`, with report destination
`64_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C9-B/3**, the last repository sub-grant of the whole. It finalizes
the living-truth sentences that the two prior sub-grants did not touch, and it
produces the complete semantic classification of every remaining retired-
spelling hit as a report artifact. No new runbook file is created;
`docs/UBUNTU_NUC_CLEAN_INSTALL.md` belongs to the later C-INSTALL-DOC row.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 64
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C9B3 — living truth and the semantic classification
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The claim corrections must reconcile against public truth
without reopening closed product wholes, and the classification must place
every remaining hit in exactly one owned category — an unclassified hit stops
the commit.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/61_report_00.md`
sections 5 and 6 are the normative source; section 8 defines this sub-grant's
boundary. The planning report's line numbers predate C9-B/1 and C9-B/2;
re-derive every sentence at its current location.

1. **Correct the false sentences, exactly these three** (the engine docstring
   was already corrected in C9-B/2):

   - `DEVELOPMENT.md` — the paragraph that says launcher-managed state
     "continues at its current locations until the later identity switch".
     The launcher defaults are already `~/Library/Application Support/Kronika`
     and `$XDG_DATA_HOME/Kronika`. Say that; say `migrate-identity-paths`
     remains the workstation copy tool for a leftover legacy tree, with the
     refusal safeguard in front of creating an empty catalog; remove the
     "later identity switch" framing.
   - `ROADMAP.md` — the sentence that mentions "mass `kronika` rename". Name
     the actual exclusion: ADR-0085 is implemented as ordered bounded cuts,
     and the retained `FrameNest*` class residue is excluded for this whole.
   - `README.md` — the clause that calls the private-record and
     administrator-approval evidence "not yet accepted, deployed, or
     published". Reconcile it with current truth: that work is accepted and on
     public `main`. Do not reopen Gallery, desktop, Cover Studio, or
     publication scope; change only what the clause claims.

2. **Confirm, do not change, the sidecar spelling.** `README.md`'s
   `{media_filename}.framenest.json` sidecar name is a historical filename the
   readers still recognize. Confirm against the reader test that the
   historical name is still accepted; keep the name. A wording change happens
   only if the reader test proves the name is no longer read; otherwise leave
   the sentence.

3. **Do not edit** the already-historical paragraphs (the dated
   `/opt/framenest/releases/aec2f009…` history in README, PRODUCT, SERVER),
   the frozen documents and Alembic revisions, `docs/adr/README.md`, the
   retained-and-labeled sentences (frozen tooling paths in AGENTS.md and the
   runbook, the frozen mount in `docs/BACKUP_AND_RECOVERY.md`, the live
   `framenest-nuc` identity in `docs/OPERATOR_NETWORK.md`, the historical
   acceptance title in `docs/ACCEPTANCE_DUAL_AUDIENCE.md`) — label those as
   retained in the classification instead. Do not create
   `docs/UBUNTU_NUC_CLEAN_INSTALL.md`.

4. **Pins.** If any test pins one of the three corrected sentences or their
   phrases, update the pin in the same commit and name the module. Re-derive;
   do not assume.

5. **The semantic classification (report artifact).** After the edits, scan
   the same tree set the retention ledger counts and classify every
   case-insensitive `framenest` hit, outside the ledger file itself, into
   exactly one category by the definition that owns it:

```text
Frozen document or frozen revision      path is in Part A — do not edit
Durable-reader historical spelling      accepted marker filenames/keys and their readers — keep
Frozen tooling                          /opt/framenest/tooling/ — keep POETRY_BIN/CPYTHON_BIN
Frozen mount                            /mnt/framenest-catalog-offdevice — keep
Frozen state-directory name             framenest-chatgpt-page — keep
Retained live host identity             framenest-nuc — keep
Alembic shim                            the four aliased module names — keep
Excluded class residue                  a FrameNest identifier that is a class, exception,
                                        logger, or formatter — do not rename
Log sanitizer needle                    the credentials path in _assert_logs_sanitized only — keep
Retired-prefix strip                    identity_env.COMPATIBLE_ENVIRONMENT_PREFIX and
                                        drop_identity_environment_spellings — keep
Parked budget path                      DEPLOYMENT_STATE_DIR only — leave
Explicit historical prose               a living sentence naming a past release path or a
                                        completed acceptance and saying it is history
Ledger self-reference                   the ledger file itself, excluded by _SELF_RELATIVE_PATH
```

   An `Unclassified` hit stops the commit: do not invent a category. Any hit
   under the pinned `.ap/` submodule is out of this whole's scope; list it
   separately. The report carries the table (file, pattern, category) and the
   per-category totals, plus the scan command used.

## Verified starting state, measured by the Orchestrator on 2026-10-18

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                9b291e936e93026ebe540b4a23a11b89721747a8
Public main:                  5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (C9-B/1 and the B/2 candidate unpublished by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4713 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no host contact, no browser, no deployment.

## Authority

```text
Positive authority: edit `DEVELOPMENT.md`, `ROADMAP.md` and `README.md` for
  exactly the three corrections above; edit the sidecar sentence only if the
  reader test proves the historical name is no longer accepted; edit every
  test module your parse shows pinning a corrected phrase, naming each module
  in the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measured retention failure shows this commit moved,
  with the arithmetic cause stated; produce the classification table in the
  report; create exactly one local non-amended commit on `main`.

Negative authority: every other path; every frozen document and revision; the
  already-historical paragraphs; the retained-and-labeled documents; any new
  file including any runbook; any other document rewrite; any code change
  (`deploy/`, `src/` unchanged in this grant); any dependency or lockfile
  change; the `.ap` gitlink; any Alembic revision; any `.venv` operation;
  publication; push; force; amend; branch; stash; any host or browser action.
  If a necessary change falls outside the positive scope, stop and report; do
  not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 9b291e936e93026ebe540b4a23a11b89721747a8 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Read-only Git inspection allowed;
  exactly one `git add <exact paths>` and one `git commit`; no push.

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

1. **Sentence matrix.** Each of the three corrections in place, each
   verifiably true against the repository and public state; nothing else in
   the three documents changed beyond the corrected claims.
2. **Sidecar.** The reader-test confirmation recorded; the historical name
   retained.
3. **Pins.** Every updated pin named; the docs-contract module green.
4. **Classification.** Every remaining hit in exactly one category; zero
   unclassified; the totals stated with the scan command.
5. **Measurement discipline.** The retention failure is measured before the
   re-pin; after values are not pre-written; no counted comment is added.
6. Run, through the declared routes: the docs-contract modules and every
   module a corrected phrase touches (named), the full declared Python suite
   against `4713/8/3/0`, the retention module, and the JS suites plus bounded
   glob as unaffected sanity.
7. Report every moved or removed site that no test exercises.
8. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Derive every sentence by PARSING the current document; the planning
    report's line numbers are stale.
 2. Resolve every cited phrase to its literal text BEFORE editing it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each claim against the repository and the public state before
    rewriting it.
 5. Never truncate the classification. If output is truncated, disclose it.
 6. Check every mechanical probe against a known-impossible result.
 7. Regenerate every table at report time; never transcribe one.
 8. Open and classify every grep hit; an unclassified hit stops the commit.
 9. State when a requested derivation cannot exist. Do not fabricate one.
10. Do not add the counted substring in a new counted comment.
```

**Collapsing pairs.** Do not collapse the three corrected sentences with the
already-historical paragraphs; do not collapse the retained-and-labeled
documents with false sentences; do not collapse the classification table with
the retention scalars (they measure different things).

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a correction cannot be made true without widening scope; if a
  frozen document or a retained-and-labeled document would need editing; if a
  hit is unclassified; if a frozen hash or Part A moves; if a Part C re-pin
  cannot be reproduced from your own measurement; if context pressure reaches
  the point where a bounded rotation is cheaper than a degraded result.

Completion: the three corrections with their pins, the sidecar confirmation,
the complete classification table, the measured retention re-pin if any, and
one local commit.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `64_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `64` and exchange `01` unchanged.
Then:

1. The sentence matrix: each correction, old text, new text, the truth check.
2. The sidecar confirmation and the pins updated, each named.
3. The complete semantic-classification table with per-category totals and the
   scan command; the `.ap/` out-of-scope list; the zero-unclassified
   statement.
4. The measured retention re-pin with the arithmetic cause (if any).
5. Suites: touched modules, full Python, retention, JS sanity — counts,
   elapsed time, baseline differences.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement.
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/61_report_00.md`
  sections 5, 6 and 8 in full.
- `DEVELOPMENT.md` (the launcher paragraph), `ROADMAP.md` (the ADR-0085
  paragraph), `README.md` (the acceptance clause and the sidecar sentence),
  `docs/OPERATOR_NETWORK.md`, `docs/ACCEPTANCE_DUAL_AUDIENCE.md`,
  `docs/BACKUP_AND_RECOVERY.md` (read-only).
- `tests/contract/test_nuc_release_docs.py`,
  `tests/contract/test_kronika_identity_retention.py`, and every module your
  parse shows pinning a corrected phrase.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the three corrections, the pins, the
classification table and the suites at the reported commit, then arranges the
one publication, the NUC refresh and the final rendered acceptance — each a
separately authorized step and none of them inside this prompt.

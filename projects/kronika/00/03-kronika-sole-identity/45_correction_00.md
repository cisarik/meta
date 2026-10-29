# Authoritative Worker prompt — Worker session 45, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `45`, exchange `01`. Stored under the
Meta filename mapping as `45_correction_00.md`, with report destination
`45_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 45
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-C7AS-API — complete the C7-A/S server companion API emission
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The C7-A/S cut as issued under-scoped one of the two server
emissions the plan names: the served web-host asset already emits the canonical
web protocol, but the server companion API still emits the retired API version
spelling, while the extension's dual reader and the plan both expect the switch
to land here. The correction is small in bytes and high in contract fidelity: a
wrong reading breaks the picker/attach flow silently against a refreshed
extension.

## The finding, exactly

The accepted closure plan, `25_report_00.md` section 2.11, requires: "Switch
server companion API and web-host emissions to canonical identifiers while
retaining compatible readers." The web-host half is done and served (commit
`7c1cee2`, verified live). The API half is not:

- `src/kronika/application/companion_picker.py` declares
  `COMPANION_API_VERSION = "framenest-companion.v1"` — the retired spelling.
- `src/kronika/adapters/api/x_companion_api.py` emits it as the
  `companion_api_version` field of the companion media response.
- The extension already keeps the compatible dual reader:
  `extension/shared/messages.js` declares `API_VERSION = "kronika-companion.v1"`,
  `RETIRED_API_VERSION = "framenest-companion.v1"` and
  `ACCEPTED_API_VERSIONS` for both, and its comment states the server keeps
  emitting the retired spelling "until a later cut moves
  `COMPANION_API_VERSION`". That later cut is C7-A/S.
- Two contract tests currently pin the retired emission:
  `tests/contract/test_tailscale_ingress_security.py` (around line 1635) and
  `tests/contract/test_x_companion_api.py` (around line 245).

The plan's C7-A/S proof names "canonical API/web emissions" explicitly. The
live host serves the canonical web asset; a fresh NUC refresh after this
correction will serve both canonical emissions.

## Correction specification

1. **Switch the emission.** Set `COMPANION_API_VERSION` to
   `"kronika-companion.v1"` — the exact spelling the extension's `API_VERSION`
   already uses. No other behavior change: the response schema, the field
   name, the page construction and every error path stay as they are.
2. **Flip exactly the emitted-literal pins.** Update the two contract
   assertions above to the canonical literal, and any further repository
   assertion that pins the **emitted** retired literal, derived by grep and
   named in the report before editing. Do **not** touch `extension/**`: its
   `RETIRED_API_VERSION` reader, its acceptance tests and its comment are the
   companion cut's surface. Do not touch frozen documents, ADRs or
   `docs/X_COMPANION.md`.
3. **Readers unchanged.** The extension's dual acceptance stays exactly as it
   is; the existing mixed-version JS tests must stay green without edits.
4. **Retention.** Re-pin a Part C scalar only when your own measurement shows
   this correction moved it (the `framenest-companion` literals live in `src`
   and `tests`), with the arithmetic cause recorded in the running ledger
   comment. Never tune a pin until a suite is green.

## Verified starting state, measured by the Orchestrator on 2026-10-12

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                7c1cee299e14dbccaca10fe0ce749b4dc7553420
Public main:                  7c1cee299e14dbccaca10fe0ce749b4dc7553420
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4955 passed, 8 skipped, 3 warnings, 0 failed
Focused companion modules
(x_companion_api, tailscale_ingress_security, companion_picker unit): 97 passed
Retention module:             15 passed
JS companion_review_extension.test.js: 40 passed
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. No host contact; everything is repository-only.

## Authority

```text
Positive authority: edit `src/kronika/application/companion_picker.py` for
  the single constant; edit the two named contract test modules and any
  further repository assertion that pins the emitted retired literal, naming it
  in the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this correction moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; `extension/**`; any document; any
  dependency or lockfile change; any change to `pyproject.toml`,
  `ap.project.conf` or the `.ap` gitlink; any frozen document or Alembic
  revision; publication; push; force; amend; branch; stash; any NUC contact or
  SSH; any migration, deployment or provider contact. If a necessary change
  falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 7c1cee299e14dbccaca10fe0ce749b4dc7553420 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`, including as a text
  editor. JavaScript evidence uses only the documented ordinary invocation
  from the worktree root: `node --test tests/<name>.test.js`.
  Read-only Git inspection allowed; exactly one `git add <exact paths>` and one
  `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only.
Browser authority: none. No extension reload, no real side panel, no profile.
```

## Verification

1. **Inventory first.** Grep every case-insensitive `framenest-companion` and
   `framenest_companion` occurrence across the repository (excluding `.git` and
   `.venv`) and classify each hit: the emission constant (flip), emitted-literal
   test pins (flip), the extension's retired reader and its acceptance tests
   (keep, later cut), anything else (report). Show the classification table.
2. **Reproduce the current emission.** Before editing, state the exact current
   constant and the two pin assertions; optionally exercise the picker response
   through a focused test to show the emitted retired literal.
3. **Post-fix matrix.** The picker response emits `kronika-companion.v1`; the
   extension accepts both spellings (existing JS tests untouched and green:
   retired, canonical and unknown-version cases); no other emission site emits
   the retired version; the retired literal survives only in the extension's
   dual reader and its tests.
4. **Mutation demonstration.** Revert the constant to the retired spelling →
   the flipped pins fail with the exact mismatch; restore. Report the observed
   failure.
5. Run, through the declared routes: the focused companion modules, the JS
   extension suite, the full declared Python suite, then the retention module.
   Report every count, elapsed time and any difference from `97`, `40`,
   `4955/8/3/0` and `15`.
6. Report every moved or removed site that no test exercises, and every caller
   or consumer of `COMPANION_API_VERSION` your derivation found that this
   prompt did not name.
7. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and cause for any
   Part C movement.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. This prompt's anchors are
    locators, not an inventory.
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

**Collapsing pairs.** The emitted version and the accepted-version set must not
collapse: an unknown version must stay refused by the extension, and the
retired spelling must never return as an emission.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if the correction would touch `extension/**` or a frozen document; if
  a frozen hash, Part A or Part B moves; if a Part C re-pin cannot be
  reproduced from your own measurement; if a necessary change falls outside the
  positive scope.

Completion: the canonical API emission with the compatible readers unchanged;
the inventory table with every hit classified; the mutation demonstration;
focused companion modules, JS extension suite, full declared Python suite and
retention module green through the declared routes; one local commit; report
delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `45_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no refresh, no host contact and no later cut is authorized by
  it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `45` and exchange `01` unchanged. Then:

1. The inventory table with every occurrence classified.
2. The reproduced retired emission and the corrected canonical emission.
3. The mutation demonstration with its observed failure.
4. Focused, JS, full-suite and retention counts with elapsed time and any
   baseline difference.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and
   Part C movement with cause.
6. Every site no test exercises.
7. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  section 2.11 in full.
- `src/kronika/application/companion_picker.py` and
  `src/kronika/adapters/api/x_companion_api.py`.
- `extension/shared/messages.js` — the dual reader and its comment,
  read-only.
- `tests/contract/test_x_companion_api.py`,
  `tests/contract/test_tailscale_ingress_security.py` companions of the pins.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will verify the inventory, the emission and the
pins, re-run the affected suites, and then arrange a separate publication and
exact-main NUC refresh so the served server carries both canonical emissions
before the companion transition (`C7-A/C`) begins. No push, refresh or host
contact is authorized inside this prompt.

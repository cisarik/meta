# Authoritative Worker prompt — Worker session 53, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `53`, exchange `01`. Stored under the
Meta filename mapping as `53_implementation_00.md`, with report destination
`53_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C7-B/2a**, the retired-reader removals of the C7-B cut. C7-B/1 is
committed (`6531965`) and accepted; the companion transition (C7-A) is
published, served and rendered-accepted, so every retired reader this grant
removes now has no legitimate emitter left in the served pair. C7-B/2b will
follow with the physical removals (console aliases, the twenty Part B paths,
the operator scripts and their mirrors) and C7-B/3 with the finishing
documents.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 53
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B2A — remove the retired protocol readers
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. These removals tighten three cross-boundary acceptances at
once — the server's mutation header, the served web host's companion protocol,
and the extension's protocol, API-version, browser-key and alarm readers.
Each site's compatible reader exists for a peer that is now refreshed or
superseded; a missed reader leaves a silent compatibility path, and an
over-eager removal of the canonical path breaks the served pair. Parse before
you remove, keep canonical behavior and every numeric status, and update the
tests that describe the removed acceptance truthfully.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.13 is your specification; its "Remove old mutation-header and
companion-protocol readers" and "Remove obsolete browser-key readers only after
migration receipts" items are this grant's scope (the migration receipts exist:
C7-A/C completed and was rendered-accepted). Required outcomes:

1. **Server mutation header.** In
   `src/kronika/adapters/api/tailscale_ingress.py` the retired
   `X-FrameNest-Request` acceptance goes: only `X-Kronika-Request: 1` is
   accepted, the retired spelling is refused exactly like any wrong value, and
   the message becomes the canonical truth (for example, the mutation header
   is required and must be exactly `1`, naming only the canonical header).
   Keep every rejection status and code (`MUTATION_HEADER_REQUIRED` and
   friends) unchanged. Update every test that pins the retired acceptance
   (`tests/contract/test_kronika_mutation_header.py`,
   `tests/contract/test_tailscale_ingress_security.py` and any further site).
2. **Served host web protocol reader.** In
   `src/kronika/adapters/api/web/companion_host.js` the acceptance becomes the
   single canonical `PROTOCOL`; the retired spelling is refused like any
   near-miss; the emission stays canonical and the contract comment tells the
   new truth. Update `tests/companion_web_bridge.test.js` (the host acceptance
   matrix and near-miss sets now prove the retired spelling is refused) and
   `tests/contract/test_local_web_application.py` (the served-asset
   accepted-set pin).
3. **Extension readers.** In `extension/ui/sidebar.js` remove
   `RETIRED_WEB_PROTOCOL` and its acceptance; the receive side accepts the
   canonical spelling only. In `extension/shared/messages.js` remove
   `RETIRED_API_VERSION` and the dual accepted set; remove
   `STORAGE.origin.retiredName` and the retired-key read fallbacks; remove
   `REVIEW_INBOX.retiredAlarmName`. In
   `extension/background/service_worker.js` the alarm listener and creation
   use the canonical name only; the retired-alarm clearing path and the
   retired-key migration helper simplify or go (the receipts exist). Keep the
   already-canonical internal protocol `kronika.companion.v1` and every
   unrelated stored key (`inflightClaims`, `adapterAcknowledged`,
   `reviewInboxExplicitCollapsed`, `reviewInboxSeenRunId`,
   `reviewInboxAwaitingAnalysis`) exactly as they are. Update
   `tests/companion_review_extension.test.js` and any further JS suite that
   pins a removed reader; a test whose entire subject was the removed reader
   is retired with its cause stated, never left vacuous and never weakened
   silently.
4. **Truthful messages in the same commit.** Every message, comment or export
   that describes a removed acceptance is updated to the canonical truth in
   this commit; no site may still claim a retired acceptance exists.
5. **Behavior freeze otherwise.** Unknown values are refused exactly as
   today; canonical paths behave identically; every numeric status is
   unchanged; no unrelated surface moves.
6. **Ledger.** Re-pin the Part C scalars this grant moves with per-tree
   arithmetic causes; record every content-path departure (a file losing its
   last retired occurrence leaves `EXPECTED_FRAMENEST_CONTENT_PATHS` — the
   `extension` tree is expected to empty or near-empty); Part A stays
   byte-unmoved and Part B stays at 20 (the physical removals are C7-B/2b).

## Verified starting state, measured by the Orchestrator on 2026-10-14

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                6531965e5406805a17dc9a68e26d03d9e78e8260
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
                              (6531965 is local and unpublished by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4971 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS baselines: companion_web_bridge 27; companion_review_extension 42;
              x_companion_extension 54; companion_settings_automatic_analysis 6;
              kronika_ui 12; catalog_card_ai_quick_action 30;
              bounded non-browser JS glob 213
Host state (Orchestrator evidence): the NUC serves `aee0a60`; the extension
              revision `aee0a60` was reloaded and rendered-accepted; the
              server accepts both mutation headers and the host accepts both
              web protocols until this grant is served.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no NUC contact, no browser, no real X.

## Authority

```text
Positive authority: edit `src/kronika/adapters/api/tailscale_ingress.py`,
  `src/kronika/adapters/api/web/companion_host.js`, `extension/**` and exactly
  the sources your parse shows carrying a removed reader; edit every test
  module or support file whose assertion, fixture or inventory describes the
  removed acceptance, naming each non-obvious module in the report before
  editing it; edit `tests/contract/test_kronika_identity_retention.py` for the
  measured scalar re-pins, the running arithmetic and the content-path
  departures this grant causes; make only the minimal name-correcting edit to
  an active document if a suite cannot otherwise be green, naming it in the
  report; create exactly one local non-amended commit on `main`.

Negative authority: the twenty Part B deletion paths; the console aliases in
  `pyproject.toml`; the operator scripts and their mirrors (C7-B/2b); every
  production source outside the three reader surfaces and their direct
  consumers; every frozen document and ADR; any dependency, lockfile or
  package-configuration change; the `.ap` gitlink; any Alembic revision; any
  `.venv` operation; historical artifact readers and the Alembic
  `sys.modules` alias; publication; push; force; amend; branch; stash; any NUC
  contact or SSH; any migration, deployment, provider, browser or capture
  contact. If a necessary change falls outside the positive scope, stop and
  report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 6531965e5406805a17dc9a68e26d03d9e78e8260 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Do not activate browser-evidence suites.
  Read-only Git inspection allowed; exactly one `git add <exact paths>` and one
  `git commit`; no push.

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

1. **Reader inventory and refusal matrix.** For each removed reader, the site
   table (surface, retired spelling, canonical replacement, every test moved
   or retired with its cause). Prove behaviorally: the server refuses the
   retired mutation header while canonical requests keep their codes and
   statuses; the host refuses the retired web protocol while canonical
   messages behave identically; the extension refuses the retired protocol and
   API version; the retired browser key and alarm name are no longer read; the
   internal `kronika.companion.v1` protocol and every unrelated stored key are
   unchanged.
2. **Truthfulness sweep.** No message, comment or export still claims a
   removed acceptance; whole-tree greps for the removed spellings classify
   every remaining occurrence as frozen history, a deliberately retained
   artifact (for example the served shell's dual mutation-header emission),
   or a reported finding.
3. **Mutation demonstrations**, each named with its observed failure: restore
   the server's retired-header acceptance → its refusal test fails; restore
   the host's retired-protocol acceptance → its refusal test fails; restore a
   retired browser-key fallback → its refusal/absence test fails.
4. **Suites.** Six JS suites and the bounded non-browser glob, focused Python
   (ingress, mutation header, local web, public published), the retention
   module, and the full declared Python suite. Report every count, elapsed
   time and baseline difference.
5. Report every moved, removed or retired site that no test exercises, and
   every consumer your derivation found that this grant did not name.
6. Commit facts: SHA, `git diff --stat`, Part A byte-unmoved, Part B still 20,
   Part C movement and content-path departures with per-tree arithmetic.

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

**Collapsing pairs.** Do not collapse the retired reader with the canonical
path; do not collapse a refusal with a near-miss; do not collapse a retired
test with a vacuous one; do not collapse a content-path departure with a
scalar movement.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a change would touch a Part B deletion path, the console aliases,
  the operator scripts, a production source outside the reader surfaces or a
  frozen document; if a canonical behavior or numeric status would change; if
  a measured ledger value cannot be reproduced; if a `.venv` operation would be
  required; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded result — in that case stop before any commit and name
  exactly what remains.

Completion: every retired reader removed with its refusal matrix and mutation
  demonstrations; truthful messages; the ledger movement measured and
  recorded; all suites green through the declared routes; one local commit;
  report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `53_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no refresh, no host contact and no later grant is authorized by
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
echoing `kronika-sole-identity`, session `53` and exchange `01` unchanged. Then:

1. The reader inventory and refusal matrix, with every moved or retired test
   and its cause.
2. The truthfulness sweep classification table.
3. The mutation demonstrations, each with its named mutation.
4. Suites: JS, focused Python, full Python, retention — counts, elapsed time,
   baseline differences.
5. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, Part C
   movement and content-path departures with per-tree arithmetic.
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
  section 2.13 in full.
- `src/kronika/adapters/api/tailscale_ingress.py`,
  `src/kronika/adapters/api/web/companion_host.js`,
  `extension/ui/sidebar.js`, `extension/shared/messages.js`,
  `extension/background/service_worker.js`.
- `tests/contract/test_kronika_mutation_header.py`,
  `tests/contract/test_tailscale_ingress_security.py`,
  `tests/contract/test_local_web_application.py`,
  `tests/companion_web_bridge.test.js`,
  `tests/companion_review_extension.test.js`,
  `tests/contract/test_kronika_identity_retention.py`.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the matrices, the ledger and the
suites at the reported commit, then grants **C7-B/2b** (the console aliases,
the twenty Part B paths and the operator scripts), after which the Cooperator
environment refresh, publication and the exact-main NUC refresh follow with
**C7-B/3**. No push, refresh or host contact is authorized inside this prompt.

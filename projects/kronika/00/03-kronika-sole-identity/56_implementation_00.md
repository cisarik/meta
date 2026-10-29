# Authoritative Worker prompt — Worker session 56, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `56`, exchange `01`. Stored under the
Meta filename mapping as `56_implementation_00.md`, with report destination
`56_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C7-B/3**, the finishing half of the C7-B cut. C7-B/1 (`6531965`),
C7-B/2a (`6dd72f6`) and C7-B/2b (`551dd39`) are committed and accepted; the
code and physical compatibility are gone. This grant finishes the active
documents and operator instructions, returns the live evidence-gate variables
to canonical names, and produces the whole-tree classification that closes
C7-B's evidence. After this commit: publication, the exact-main NUC refresh
and the rendered regression acceptance close the cut.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 56
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7B3 — finish the active documents and instructions
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. Documents are the last place a removed name can silently
survive and the only place a false statement about the product can persist.
The sweep must be complete and the classification honest: frozen history stays
byte-unmoved, parked capture internals stay, negative assertions and artifact
fixtures stay, and everything else becomes canonical. The evidence-gate rename
touches live operator instructions, so the tests and the contract move
together.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.13 is your specification; its "active operator instructions" finish
and the document findings carried from C7-B/2a and C7-B/2b are this grant's
scope. Required outcomes:

1. **Active-document sweep.** Parse every tracked document that is not one of
   the 86 frozen Part A entries; for every retired occurrence — a console
   name, wrapper, path, command, variable or behavioral statement that is now
   false — update it to the canonical truth or remove the stale text in a way
   that keeps the document coherent. Known carriers to verify and complete
   (from the carried findings): `SECURITY.md`,
   `docs/ACCEPTANCE_DUAL_AUDIENCE.md`, `ROADMAP.md`, `docs/X_COMPANION.md`,
   `scripts/operator/network/README.md`, `README.md`, `DEVELOPMENT.md`,
   `AI_WORKSPACE.md`, `COVER_PIPELINE.md`, `DESKTOP.md`, `SERVER.md`,
   `SPEC.md`, `deploy/ubuntu/README.md`, `docs/BACKUP_AND_RECOVERY.md`,
   `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md`,
   `docs/UBUNTU_NUC_DEPLOYMENT.md`, and any further active document your parse
   finds (`docs/OPERATOR_NETWORK.md`, `docs/INFOSEC.md` included if they carry
   stale names). Frozen documents and ADRs stay byte-unmoved; their
   references are history.
2. **Evidence-gate variables.** The live opt-in evidence gates still carry
   retired names in tests and active instructions —
   `FRAMENEST_RUN_BROWSER_EVIDENCE`, `FRAMENEST_RUN_REAL_MEDIA_TOOLS`,
   `FRAMENEST_RUN_NVIDIA_NIM_SMOKE`, `FRAMENEST_CHROME_BIN` and any further
   gate your parse finds. Rename the live uses to `KRONIKA_*` across the
   tests, helpers and active documents that invoke or document them. The
   frozen ADR-0015 mention stays as history. If a frozen surface pins a live
   gate beyond historical prose, keep the frozen reference and rename only the
   live uses; name the decision.
3. **Doc-content tests.** Update the tests that encode a changed document
   sentence (they are this grant's surface); every behavioral assertion
   elsewhere stays green.
4. **Whole-tree classification.** Produce the C7-B closing classification:
   every remaining retired occurrence across the tracked tree, each classified
   as (a) frozen Part A history, (b) historical artifact fixture or
   provenance data, (c) a negative assertion proving absence, (d) parked
   capture internals, (e) the served shell's deliberate dual mutation-header
   emission, or (f) a finding requiring action — with per-tree counts and the
   residual list the CLOSE reconciliation will carry. No active document may
   keep a false statement about the product; no classification may be
   asserted without its evidence.
5. **Ledger.** Re-pin the `docs` and any other Part C scalars this grant
   moves with per-tree arithmetic; record every content-path departure (an
   active document losing its last retired token leaves
   `EXPECTED_FRAMENEST_CONTENT_PATHS`); Part A stays byte-unmoved and Part B
   stays empty.
6. **Suites.** Full declared Python suite, the retention module, the six JS
   suites and the bounded non-browser JS glob; report counts, elapsed time and
   baseline differences.

## Carried findings (verify and complete)

C7-B/2a deferred: `SECURITY.md` (the mutation-header prose),
`docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/ACCEPTANCE_DUAL_AUDIENCE.md` (command
examples), `ROADMAP.md` and `docs/X_COMPANION.md` (the retired alarm name).
C7-B/2b added: `README.md`, `DEVELOPMENT.md`, `AI_WORKSPACE.md`,
`COVER_PIPELINE.md`, `DESKTOP.md`, `SERVER.md`, `SPEC.md`,
`deploy/ubuntu/README.md`, `docs/BACKUP_AND_RECOVERY.md`,
`docs/WORKER_EXECUTION_CONTRACT.md`, plus the remainder of
`AGENTS.md` and `scripts/operator/network/README.md`.

## Verified starting state, measured by the Orchestrator on 2026-10-15

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                551dd397b3cd5c9c4f5e3b1eec1cd01ea8ba0d4f
Public main:                  aee0a60a04b78685608ec5a65ec5780c7d9884e7
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4968 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed (Part B empty with canonical replacement pins)
JS baselines: companion_web_bridge 23; companion_review_extension 41;
              x_companion_extension 55; companion_settings_automatic_analysis 6;
              kronika_ui 12; catalog_card_ai_quick_action 30;
              bounded non-browser JS glob 212
Environment refresh:          completed by the Cooperator; `.venv/bin` carries
                              fourteen canonical consoles and zero retired ones.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no NUC contact, no browser, no real X.

## Authority

```text
Positive authority: edit every active (non-frozen) tracked document the sweep
  finds, with the evidence-gate rename across the live tests, helpers and
  active documents; edit the tests that encode a changed document sentence or
  a renamed gate; edit `tests/contract/test_kronika_identity_retention.py` for
  the measured Part C re-pins, the running arithmetic and the content-path
  departures; produce the classification table; create exactly one local
  non-amended commit on `main`.

Negative authority: every frozen document and ADR; any product source or
  script outside the gate rename's test/doc surface; any dependency, lockfile
  or package-configuration change; the `.ap` gitlink; any Alembic revision;
  any `.venv` operation; historical artifact readers and the Alembic
  `sys.modules` alias; the parked capture internals; publication; push; force;
  amend; branch; stash; any NUC contact or SSH; any migration, deployment,
  provider, browser or capture contact. If a necessary change falls outside
  the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 551dd397b3cd5c9c4f5e3b1eec1cd01ea8ba0d4f --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Do not activate browser-evidence suites;
  the gate rename still applies to their files. Read-only Git inspection
  allowed; exactly one `git add <exact paths>` and one `git commit`; no push.

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

1. **Document sweep table.** Every active document edited: the retired
   occurrence, its canonical replacement or removal, and the sentence kept
   coherent. Every active document scanned but unchanged: why (no retired
   occurrence). Open and classify every grep hit.
2. **Class repair.** The renamed gate variables behave identically (the gated
   suites stay skipped by default and activate under the canonical names);
   the contract documents name the canonical gates; the frozen ADR keeps its
   historical mention.
3. **Truthfulness.** No active document states a removed thing as current; a
   reviewer reading only the active documents would describe the product
   correctly.
4. **Classification table.** The whole-tree remaining-occurrence table with
   per-class counts and the residual list; every classification evidenced.
5. **Suites.** Full Python against `4968/8/3/0`; retention `15`; JS
   `23/41/55/6/12/30` and the bounded glob `212`.
6. Every site no test exercises; every consumer your derivation found that
   this grant did not name.
7. Commit facts: SHA, `git diff --stat`, Part A byte-unmoved, Part B empty,
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

**Collapsing pairs.** Do not collapse a frozen historical reference with an
active stale instruction; do not collapse a gate rename with a behavior
change; do not collapse the classification's residual list with a claim of
zero remaining occurrences.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if an edit would touch a frozen document; if a product source outside
  the gate rename's surface would change; if a canonical behavior or numeric
  status would change; if a measured ledger value cannot be reproduced; if a
  `.venv` operation would be required; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded result — in that case
  stop before any commit and name exactly what remains.

Completion: every active document canonical and truthful; the gate variables
  canonical; the classification table complete with its residual list; all
  suites green through the declared routes; one local commit; report
  delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `56_report_00.md` in
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
echoing `kronika-sole-identity`, session `56` and exchange `01` unchanged. Then:

1. The document sweep table and the gate-rename matrix.
2. The truthfulness statement and the classification table with its residual
   list.
3. Suites: full Python, retention, JS, bounded glob with counts and baseline
   differences.
4. `git diff --stat`, the commit SHA, Part A unmoved, Part B empty, Part C
   movement and content-path departures with per-tree arithmetic.
5. Every site no test exercises.
6. Deviations, risks, missing evidence, and one smallest next step.

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
  section 2.13 in full; `53_report_00.md`, `54_report_00.md` and
  `55_report_00.md` for the carried document findings.
- Every active document named in the carried findings, plus the frozen
  entities list in `tests/contract/test_kronika_identity_retention.py`.
- `tests/contract/test_kronika_identity_retention.py` in full.
- `docs/WORKER_EXECUTION_CONTRACT.md` (the `.venv` prohibition),
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the sweep, the classification and the
suites at the reported commit, then closes C7-B with the publication, the
exact-main NUC refresh and the rendered regression acceptance, and only then
opens the capture-path cuts (C8). No push, refresh or host contact is
authorized inside this prompt.

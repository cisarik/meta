# Authoritative Worker prompt — Worker session 61, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `61`, exchange `01`. Stored under the
Meta filename mapping as `61_planning_00.md`, with report destination
`61_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C9-B planning**, the last repository row of the whole. C9-A is
closed: the host runs only canonical objects plus an explicit documented
retained set, and the repository at the start commit already carries the
reviewed capture software, the canonical transition helpers and the full
retention ledger. Your deliverable is the exact plan for removing the
now-obsolete former-layout and migration machinery, finalizing the living
documents, and proving the result — not the implementation.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 61
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Planning Worker
Task identity: KSI-PLAN-C9B — derive the C9-B removal and finalization plan
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The removal inventory spans a ~7000-line deployment engine,
the retention ledger, contract tests and every living document; the plan must
prove that no routine route can select a deleted layout and that the durable
readers, the Alembic shim and the local-state safeguard survive untouched.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.19 is the normative specification for C9-B. Read it in full, then
derive the plan it requires. The plan must cover, by parsing the repository at
the start commit (never from this prompt's anchors):

1. **Removal inventory — former-layout web support.** Every engine site that
   still understands the retired host layout: the former layout constants and
   helpers (the `OLD_WEB_LAYOUT` family and the module-level former paths),
   the old release-root/current-pointer/env-file logic, the old-layout
   branches inside `deploy`, `rollback`, `check`, `status` and the capture
   commands, the remote command builders that still accept an old layout, and
   the corresponding contract tests. For each site: exact symbol, current
   behavior, why C9-A makes it obsolete, classification
   (`remove` / `keep-durable-reader` / `retool`), tests that touch it, and the
   risk of removal.
2. **Removal inventory — temporary migration/recovery implementations.** The
   identity migration machinery (`migrate-identity` with its plan, preflight,
   apply, journal, recovery-manifest and private-store handling, and its
   `MIGRATION_*` tables), the capture-path migration (`migrate-capture-paths`,
   the `CapturePathPlan` observation, gates and cleanup), the retired
   transformer helpers, the transitional `_remote-*` helpers used only by
   those commands, and their tests. Cross-check each against the frozen
   documents and the ledger before proposing removal.
3. **Removal inventory — transitional client options.** Derive which client
   or companion options, flags, dual-layout fallbacks or shims existed for the
   transition and are now obsolete (search the web shell, companion assets
   and their tests; distinguish transitional options from durable features).
   Classify each and name the tests.
4. **Keeps, identified precisely.** The durable readers (including the
   historical marker-spelling acceptance and where exactly it must remain),
   the Alembic shim, and the local-state refusal safeguard. Identify each by
   symbol and file, state why the plan preserves it, and state which removal
   candidates must not touch it. If any named keep cannot be located or
   classified unambiguously, stop and report instead of guessing.
5. **Living-document finalization.** A per-document inventory and exact fix
   list for `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SERVER.md`,
   `DEVELOPMENT.md`, `docs/UBUNTU_NUC_DEPLOYMENT.md`,
   `docs/BACKUP_AND_RECOVERY.md`, and every other active operator/subsystem
   document your parse finds carrying stale package, provenance-module or
   shipped-status claims. Separate: claims to correct, statements to mark
   explicitly historical, frozen documents to leave untouched (name them),
   and the retirement of the now-obsolete migration/recovery prose. Note that
   `docs/UBUNTU_NUC_CLEAN_INSTALL.md` belongs to the later C-INSTALL-DOC row,
   reframed as a clean-install/recovery runbook (the Cooperator declined the
   live reinstall; the live `framenest-nuc` host identity is retained and
   documented).
6. **Semantic classification design.** The method by which the implementation
   will classify every remaining operational hit of the retired spelling
   after removal: the category set (frozen state name, durable-reader
   historical spellings, retained live host identity, historical documents,
   retention-ledger accounting), the rule that decides each category, and how
   the result is counted against the retention ledger (Part A frozen hashes,
   Part B set, Part C scalars) with the arithmetic that a removal moves.
7. **Proof design.** Concrete tests and commands for: both suites green;
   wheel/resource checks (the packaging checks and any wheel build/resource
   verification the repository already uses); exact frozen hashes unchanged
   (Part A and the ADR-frozen digests, counted as the ledger does); the
   canonical executable set (which entry points must exist and resolve);
   public-main equality; and a test design proving that no routine deployment
   route can select a deleted layout (mutation-style: reintroduce an
   old-layout selection and show the new guard or the absence of the code
   fails a named test). Include the mutation demonstrations the
   implementation will run.
8. **Sub-grant split.** Propose the smallest safe split of C9-B into ordered
   implementation grants (precedent: C7-B was split into B/1…B/3), each with
   scope, exact proof, and its own commit boundary; plus the boundary after
   the last sub-grant: publication, NUC refresh, and the final rendered
   acceptance belong to separately authorized steps and must not be smuggled
   into an implementation grant.

## Verified starting state, measured by the Orchestrator on 2026-10-17

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                5b86d896b3ea03f89fef2c90f7af2c121d0ef915
Public main:                  5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (published)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      5016 passed, 8 skipped, 3 warnings, 0 failed
Focused capture/release modules: 640 passed (ten-module set)
Retention module:             15 passed
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
Host state (post-C9-A, for context only): canonical layout live; both
  pointers -> /opt/kronika/releases/5b86d896…; DB 0035; fresh scheduled
  backup receipt attempt_seq 134 succeeded; former-layout objects retired
  into /root/kronika-retired-20261017/; retained explicitly: the frozen
  tooling and mount name, the capture state name framenest-chatgpt-page, the
  live framenest-nuc host/tailnet identity and its certificates, the
  upload-publication destination library /srv/media/framenest-published
  (deferred media-path migration), and operator-owned material.
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only read-only work: no writes, no commit, no host
contact, no browser.

## Authority

```text
Positive authority: read any repository file; run read-only git inspection;
  run the declared test suites read-only if a count needs confirmation;
  produce the planning report.

Negative authority: every write of any kind; any edit, add, delete, move or
  rename; `git add`, `git commit`, `git push`, branches, tags, stash; any
  `.venv` operation; any dependency or lockfile change; any Alembic revision;
  any host, NUC, SSH, capture, deployment or browser action; any publication
  or refresh. Do not implement anything — the report is the deliverable.
  If a necessary classification cannot be made from repository evidence,
  stop and report it as an open question.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 5b86d896b3ea03f89fef2c90f7af2c121d0ef915 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only `node --test tests/<name>.test.js` from the worktree root.

Dependency authority: none.
Git authority: none (read-only inspection only).
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: none.
Browser authority: none.
```

## Derivation and defect-pattern discipline

```text
 1. Derive every inventory by PARSING the artefact. This prompt's anchors are
    locators, not inventories. Never transcribe a list from prose.
 2. Resolve every cited symbol to its literal definition BEFORE classifying.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Check every mechanical probe against a known-impossible result.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Open and classify every grep hit; count them.
 8. Regenerate every table at report time; never transcribe one.
 9. State when a requested derivation cannot exist. Do not fabricate one.
10. For every removal candidate, name the test that would fail if the removal
    were wrong, or state that no such test exists yet and propose it.
```

**Collapsing pairs.** Do not collapse the durable readers with the temporary
migration commands; do not collapse frozen documents with stale documents; do
not collapse a transitional client option with a durable feature; do not
collapse the retention ledger's Part A/B/C accounting with a simple count.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if any keep cannot be located or classified; if a classification
  would require a write; if context pressure reaches the point where a
  bounded rotation is cheaper than a degraded plan.

Completion: the exact removal inventories with classifications and risks,
  the precise keeps, the per-document finalization list, the semantic
  classification method, the proof and mutation design, the sub-grant split
  with the publish/refresh/acceptance boundary, and the open questions.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `61_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-evidence`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `61` and exchange `01` unchanged. Then:

1. The removal inventories (former-layout support, migration/recovery
   implementations, transitional client options) — per-site tables with
   classification, evidence and risk, counts stated.
2. The keeps, each identified by symbol and file, with the proof that the
   plan preserves them.
3. The living-document finalization list, per document.
4. The semantic-classification method and its ledger arithmetic.
5. The proof design and the mutation demonstrations.
6. The sub-grant split with boundaries and sequencing.
7. Open questions and the smallest next step.
8. Deviations, risks, missing evidence.

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
  sections 2.18, 2.19 and 2.20 in full.
- `deploy/ubuntu/kronika_release.py` — the whole engine, as it stands.
- `tests/contract/test_kronika_identity_retention.py` — the ledger.
- `tests/contract/test_kronika_capture_services.py`,
  `tests/contract/test_kronika_identity_migration.py`,
  `tests/contract/test_nuc_release_*.py`, `tests/contract/test_nuc_operator_runbook.py`,
  `tests/contract/test_kronika_cli_and_release_readers.py`,
  `tests/contract/test_kronika_durable_writer_identities.py`.
- `docs/UBUNTU_NUC_DEPLOYMENT.md`, `docs/BACKUP_AND_RECOVERY.md`,
  `README.md`, `PRODUCT.md`, `SPEC.md`, `ROADMAP.md`, `SERVER.md`,
  `DEVELOPMENT.md`, `docs/adr/README.md` and the frozen ADR documents the
  living documents cite.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the inventories and the proof design
against the repository, adjusts the sub-grant split if needed, and issues the
C9-B/1 implementation grant. No write, commit, publication, refresh, host
action or acceptance is authorized inside this prompt.

# Authoritative Worker prompt — Worker session 65, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `65`, exchange `01`. Stored under the
Meta filename mapping as `65_implementation_00.md`, with report destination
`65_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

This is **C9-B/3 resumed** (`KSI-IMPL-C9B3R`). Session 64 stopped correctly:
its classification gate found 808 of 3375 hits without an owning category,
so it left the verified edits uncommitted. This grant carries the amended
category list, keeps the session-64 edits, re-runs the classification under
the amended list, and creates the one commit.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 65
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C9B3R — living truth commit under the amended classification
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. The classification has strict per-hit verification rules
for the two ambiguous clusters (code-local identifiers and stored keys), and
one defect is known before the run.

## The working tree this grant starts from

The working tree is **dirty by design** with the verified session-64 work:
exactly four paths.

```text
 M DEVELOPMENT.md
 M README.md
 M ROADMAP.md
 M tests/contract/test_kronika_identity_retention.py
```

The three sentence edits and the `capitalized FrameNest` re-pin (2327→2328)
are the session-64 work accepted by the Orchestrator as the content of this
commit. Validate them against the session-64 report section 1 and the
retention measurement in section 4; if they match, keep them byte-for-byte.
If anything differs, stop and report.

## Specification

1. **Keep the four-path diff as the commit content.** No further sentence
   edits, no new files. The commit message: `Finalize living truth and
   classify the remaining retired spellings.`
2. **Re-run the classification** over the same scan set the session-64 report
   used (the tracked set the retention counter counts, ledger file excluded;
   `.ap` listed separately as out of scope) and place every
   case-insensitive `framenest` hit into exactly one category below. The
   session-64 report sections 3 and its full unclassified table are the
   starting data; re-derive, do not transcribe.

**Amended category list (each with its normative owner):**

```text
 1 Frozen document or frozen revision        Part A path — keep
 2 Durable-reader historical spelling        accepted marker filenames/keys and their readers — keep
 3 Existing historical backup/sidecar/snapshot/offdevice/analysis identities
   plan §5 "Existing historical backup/sidecar/release/snapshot identities and
   stored analysis identities; newly written identities remain canonical" — keep
 4 Frozen tooling                            /opt/framenest/tooling/ — keep
 5 Frozen mount                              /mnt/framenest-catalog-offdevice — keep
 6 Frozen state-directory name               framenest-chatgpt-page — keep
 7 Retained live host identity               framenest-nuc — keep
 8 Alembic shim                              the aliased module names — keep
 9 Accepted Python class/module names, source comments and docstrings
   plan §4 "Source comments and docstrings remain outside the confirmed identity
   goal" and §5 "Accepted Python class/module names, source comments/docstrings
   and negative test assertions" — keep
10 Negative test assertions and retained-spelling fixtures
   plan §5 same clause, §6 rule 3 — keep
11 Non-operational code-local identifier (variable/helper/logger/coordinator name)
   NOT a value, header, key, path, message, service identifier, or emitted code.
   Strict verification: prove by parse that the identifier is never emitted,
   stored, sent, or accepted. If it is, it is category 16, not 11.
12 Historical ADR bodies/citations and historical artifacts with their cited paths
   plan §5 "Historical ADR bodies/citations, historical artifacts and their
   narrowly retained readers" — includes ADR-0085's text, the adr README index,
   the provenance record, and the workspace/public UDS path constants whose
   values match the frozen ADR-0048/ADR-0074 bodies. Keep; do not rename.
13 Retired-prefix strip safeguard             identity_env strip — keep
14 Log sanitizer needle                       inside _assert_logs_sanitized only — keep
15 Stored key retained for read/migration with a canonical live counterpart
   plan §5 stored identities — keep only when the parse proves the canonical
   key is what the code writes and the historical key is read for migration or
   compatibility; otherwise category 16
16 Active-production defect with a scheduled correction
   A hit the canonical system still emits, sends, accepts, or writes as its
   live identity, outside every retained category. List each with file,
   pattern and evidence. Do NOT fix it in this grant.
17 Parked budget path                         DEPLOYMENT_STATE_DIR — keep
18 Retained ignore/guard entry                .gitignore with its explaining comment — keep
19 Explicit historical prose                  dated history and removed-command
   sentences that say they are history — keep
20 Ledger self-reference                      the ledger file itself — excluded
```

3. **The known defect, already scheduled:** `src/kronika/adapters/api/web/app.js`
   emits `X-FrameNest-Request` on unsafe methods while the tailscale ingress
   gate (`src/kronika/adapters/api/tailscale_ingress.py`, `MUTATION_HEADERS`)
   accepts only `x-kronika-request`. The frontend test mirrors
   (`ai_providers_admin_frontend.test.js`, `catalog_card_ai_quick_action.test.js`,
   `tailscale_identity_frontend.test.js`, `admin_batch_actions_frontend.test.js`,
   and any browser-evidence test asserting the emitted header) belong to the
   correction. Classify all of them under category 16; the correction is a
   separate grant.
4. **Strict verification duties.** For every category-11 hit, prove
   code-locality. For every category-15 hit, prove the canonical counterpart
   is the writer. Any hit that fails its proof goes to category 16 with
   evidence. Category 16 does not stop the commit — it is an owning category
   whose members are individually listed and scheduled.
5. **Everything else unchanged.** No source edit outside the four paths; no
   correction work; no new file; no `git restore`.

## Verified starting state, measured by the Orchestrator on 2026-10-18

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                9b291e936e93026ebe540b4a23a11b89721747a8
Public main:                  5b86d896b3ea03f89fef2c90f7af2c121d0ef915 (C9-B/1 and B/2 unpublished by design)
Working tree:                 four modified paths, exactly as listed above
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4713 passed, 8 skipped, 3 warnings, 0 failed
Retention at HEAD:            15 passed (the worktree re-pin moves one scalar, 2327→2328)
JS baselines:                 23 / 41 / 55 / 6 / 12 / 30; bounded glob 212
```

Re-derive the git/AP gates yourself at the start; the dirty-tree state above
is the expected state, not a gate failure. If any other path is modified, stop
and report.

## Authority

```text
Positive authority: keep the four listed paths' existing diffs; produce the
  classification table in the report; create exactly one local non-amended
  commit on `main` adding exactly those four paths.

Negative authority: every other path; every source edit; the category-16
  correction; any new file including any runbook; frozen documents; the
  retained-and-labeled documents; any dependency or lockfile change; the `.ap`
  gitlink; `git restore`/`git checkout`/stash; publication; push; force;
  amend; branch; any host or browser action. If a necessary change falls
  outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline 9b291e936e93026ebe540b4a23a11b89721747a8 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`. JavaScript evidence
  uses only the documented ordinary invocation from the worktree root:
  `node --test tests/<name>.test.js`. Read-only Git inspection allowed;
  exactly one `git add <the four exact paths>` and one `git commit`; no push.

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

1. **Diff identity.** Before the commit, the diff is exactly the four paths
   with the session-64 content; after the commit, the tree is clean.
2. **Classification.** Every hit in exactly one amended category; per-category
   totals and the scan command; the `.ap` list separate; the category-16 list
   complete with evidence; zero hits outside the category list.
3. **Strict verification evidence** for every category-11 and category-15 hit.
4. **Retention.** `15 passed` on the committed tree; the measured capitalized
   scalar movement is 2327→2328 with the arithmetic cause (the one new
   `FrameNest` in the ROADMAP sentence).
5. Run, through the declared routes: the session-64 focused set (retention,
   `test_nuc_release_docs.py`, the two schema-head tests, the sidecar reader
   test), the full declared Python suite against `4713/8/3/0`, and the JS
   suites plus bounded glob as unaffected sanity.
6. State the exact commit SHA, `git diff --stat`, Part A byte-unmoved, Part B
   still empty, and the Part C movement with its measured cause.

## Derivation and defect-pattern discipline

```text
 1. Re-derive the hit set; the session-64 tables are starting data, not pins.
 2. Resolve every ambiguous hit to its literal use BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin; require assertion context.
 4. Prove category-11 code-locality and category-15 writer direction by parse.
 5. Never truncate the classification. If output is truncated, disclose it.
 6. Check every mechanical probe against a known-impossible result.
 7. Regenerate every table at report time; never transcribe one.
 8. Open and classify every grep hit; a hit outside the category list stops
    the commit.
 9. Do not add the counted substring in a new counted comment.
10. State when a requested derivation cannot exist. Do not fabricate one.
```

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository state is not
  the four-path worktree described above; if a session-64 edit differs from
  its report; if a category-11 or category-15 proof fails and the hit cannot
  be listed under category 16; if a frozen hash or Part A moves; if context
  pressure reaches the point where a bounded rotation is cheaper than a
  degraded result.

Completion: the four-path commit with the classification table under the
  amended categories, the strict-verification evidence, the category-16 defect
  list, and the full proof.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `65_report_00.md` in
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
echoing `kronika-sole-identity`, session `65` and exchange `01` unchanged.
Then:

1. The kept-diff validation against the session-64 report.
2. The complete classification table with per-category totals, the scan
   command, the `.ap` out-of-scope list, and the zero-outside statement.
3. The strict-verification evidence for the category-11 and category-15 hits.
4. The category-16 defect list with per-item evidence and the scheduled
   correction reference.
5. Suites: focused set, full Python, retention, JS sanity — counts, elapsed
   time, baseline differences.
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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/64_report_00.md`
  in full (the blocked report and its tables).
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  sections 4, 5 and 6.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/61_report_00.md`
  sections 5 and 6.
- The four modified paths as they stand.
- `src/kronika/adapters/api/tailscale_ingress.py` (the mutation gate, read-only),
  `src/kronika/adapters/api/web/app.js` (read-only), `extension/` (read-only),
  `tests/contract/test_kronika_durable_writer_identities.py`,
  `tests/contract/test_kronika_durable_artifact_readers.py`,
  `tests/contract/test_kronika_mutation_header.py` (read-only).
- `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5,
  §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile, the parked capture state or
profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the commit, the classification and
the defect list, then issues the bounded correction (the web-shell mutation
header alignment and any further category-16 members) before the publication
and refresh sequence.

# Fresh Worker 6 — full independent re-acceptance of corrected AP continuation candidate

Use this text as the **sole authoritative Worker prompt**. Do not prepend or
consume the prior planning, implementation, correction, or acceptance prompts,
their reports, the outgoing handout, or any Meta trace. Treat every earlier
statement as an untrusted claim and decide from the exact corrected Git objects
and complete committed content.

## 1. Coordinate, route, authority, and acceptance record

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 06
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Task phase: Acceptance
Acceptance authority: explicit-read-only
Independence required: yes
```

```text
Acceptance candidate: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Acceptance owner map: AP.md sole semantic owner under ADR-0013; PROMPT_CONTRACTS.md exact structural owner; role/lifecycle/integration documents operational projections; PROMPT_ENGINEERING_PATTERNS.md advisory; README/FAQ/GLOSSARY explanatory; ADR/CHANGELOG historical
Acceptance allowlist: AP.md; PROMPT_CONTRACTS.md; AP_ORCHESTRATOR.md; PROMPT_ENGINEERING_PATTERNS.md; ARTIFACT_LIFECYCLE.md; INTEGRATION.md; README.md; FAQ.md; GLOSSARY.md; CHANGELOG.md; docs/adr/README.md; docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md
Acceptance risk claims: semantic-owner integrity; cold-start discoverability; two-stage authority separation; optional-ledger storage/discovery correctness; absence/malformed/stale fail-closed behavior; report-repair non-authority; ADR accepted-status truth; backward compatibility
Acceptance control matrix: exact two-commit Git stack; exact cumulative and correction path sets; complete semantic scenarios; negative authority scenarios; exact structural spelling; historical-status convergence; link/fence/path integrity; unchanged executable/schema/managed-block/consumer surfaces
Acceptance independence: required-fresh-independent
Primary fresh acceptances used before this task: 1
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

- Worker session profile: Fresh Independent Acceptance Worker.
- This is full fresh re-acceptance of the complete corrected candidate, not a
  scoped review of the two-file correction.
- Evidence tier: E2 repository-grounded independent documentation acceptance.
- Reasoning recommendation: High, advisory only. No model/provider/client/IDE
  identity belongs in the result.
- Internal delegation: prohibited. One fresh accountable Worker performs the
  complete review.
- Native planning mode is off. Do not create or modify a plan.
- Authority permits credential-free public-ref reads, read-only repository and
  Git-object inspection, and disposable validation material under `/tmp` only.
- No source, index, branch, worktree, configuration, remote-ref, AP, FrameNest,
  Meta, account, service, or external mutation is authorized.
- No correction is authorized. A defect produces a terminal report and a later
  separate decision; do not edit either candidate worktree.

## 2. Exact corrected stack and public hard gates

Independently verify this entire two-commit candidate stack:

```text
Public AP baseline:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Semantic implementation commit:
a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Parent: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Tree: 7b53c74b7bfa183e490a0d81581a9f3db45c99d3
Subject: docs: define continuation bootstrap and observation ledgers

Corrected acceptance candidate:
17b7e085139e9bcbb0e4953d26aef9b6687d541c
Parent: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Tree: 6f0d09c9db0b8b45b36a7ff3bdd9a3ef61d56c4a
Subject: docs: mark ADR-0016 accepted
```

Expected local evidence locations:

```text
AP owner repository: /home/agile/Projects/ap
Corrected branch: fix/adr-0016-accepted-status
Corrected worktree: /home/agile/Projects/ap-worktrees/ap-universal-project-continuation-bootstrap-and-durable-observation-ledger-w5
Original implementation branch: feat/universal-continuation-observation-ledger
Original implementation worktree: /home/agile/Projects/ap-worktrees/ap-universal-project-continuation-bootstrap-and-durable-observation-ledger-w3
```

The ORCHESTRATOR reverified immediately before issuing this prompt:

```text
AP public refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

FrameNest public refs/heads/main:
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

FrameNest .ap gitlink at that commit:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Before substantive review, independently prove:

1. the owner repository resolves to canonical public AP;
2. credential-free AP and FrameNest public refs still equal the gates above;
3. both candidate commits exist locally with the exact identities, trees,
   subjects, and single-parent linear ancestry shown above;
4. the corrected branch/worktree is clean at exact `17b7e085...`;
5. the original implementation worktree is clean and unchanged at
   `a1b04ffc...`;
6. commit-bound FrameNest inspection confirms its `.ap` gitlink without reading
   or changing the live FrameNest worktree; and
7. neither candidate commit is present at public AP `main` and no public
   feature-branch ref is required for review.

If a public gate differs, stop `BLOCKED` with
`Report justification: changed-external-state`. If candidate identity,
ancestry, cleanliness, independence, or repository identity fails, stop with
the one canonical justification supported by the evidence. Do not repair.

Meta is archival-only and outside this task. Do not inspect or mutate it.

## 3. Full acceptance objective

Determine whether exact corrected tip `17b7e085...` is safe to publish
**unchanged** as the complete AP continuation-bootstrap and durable
observation-ledger decision.

PASS requires independently proving:

1. the complete semantic implementation remains correct under the current AP
   owner/projection model;
2. the two-stage continuation bootstrap is discoverable and authority-safe;
3. optional consumer ledger declaration/storage is portable, non-authorizing,
   bounded, stale-aware, privacy-safe, and fail-closed;
4. planner-artifact/report completion remains finite and never becomes
   execution authority;
5. the historical correction changes only ADR-0016 lifecycle status and makes
   body/index truth consistent with prior acceptance without claiming
   publication or closure;
6. the full cumulative candidate is backward-compatible for existing pinned
   consumers; and
7. the exact tip contains no unrelated, executable, schema, managed-block,
   test, consumer, or Meta mutation.

Do not rely on either earlier PASS. Re-run every material acceptance control
against the corrected tip.

## 4. Git-stack and path-boundary controls

### 4.1 Semantic implementation commit

Prove `a1b04ffc...` changes exactly these 12 paths relative to `041de310...`:

```text
AP.md
PROMPT_CONTRACTS.md
AP_ORCHESTRATOR.md
PROMPT_ENGINEERING_PATTERNS.md
ARTIFACT_LIFECYCLE.md
INTEGRATION.md
README.md
FAQ.md
GLOSSARY.md
CHANGELOG.md
docs/adr/README.md
docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md
```

ADR-0016 must be the sole added file; there must be no deletion, rename, or
mode change.

### 4.2 Correction commit

Prove `17b7e085...` changes exactly these two ordinary files relative to
`a1b04ffc...`:

```text
docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md
docs/adr/README.md
```

The correction must contain only:

- ADR-0016 body status `Implementation candidate` -> `Accepted`;
- ADR-0016 index status `Implementation candidate` -> `Accepted`; and
- the minimum ADR-0016-specific index relationship wording needed to describe
  an accepted decision while leaving publication and closure separate.

Prove ADR-0016's substantive body after its status line is byte-identical to
`a1b04ffc...`, the general status table is unchanged, every other ADR row/body
is unchanged, and every non-allowlisted path is byte-identical.

### 4.3 Cumulative corrected tip

Relative to public baseline `041de310...`, the cumulative changed-path set must
still be exactly the same 12 paths. Required negative controls:

- `AP_WORKER.md`, `ap`, `ap.project.conf`, `UPDATING.md`, `INFOSEC.md`, tests,
  fixtures, CI, dependencies, and all pre-existing ADR bodies are unchanged;
- generated managed-block content is byte-identical because `ap` is
  byte-identical;
- no `CONTINUATION.md`, ledger template, sample consumer ledger, schema,
  parser, validator, CLI command, doctor rule, or conformance test exists;
- no FrameNest or Meta content is part of either commit; and
- no private path/host/media identifier, secret, credential, generated debris,
  fixup, or unrelated cleanup was introduced.

Run bounded Git-object evidence and `git diff --check` for both individual
commits and the full baseline-to-tip range. Do not alter an index or worktree.

## 5. Semantic-owner and projection controls

Read the complete corrected-tip versions of all 12 cumulative changed files and
the directly linked unchanged sections required to interpret them. Prove:

1. `AP.md` alone owns all new continuation, ledger-storage, authority,
   staleness, absence, and planner-report completion semantics.
2. `PROMPT_CONTRACTS.md` alone owns exact field names, values, record shapes,
   failure behavior, and report-repair structure.
3. `AP_ORCHESTRATOR.md`, `ARTIFACT_LIFECYCLE.md`, and `INTEGRATION.md` remain
   operational projections; P11 remains advisory.
4. README, FAQ, and GLOSSARY remain explanatory and link to canonical owners.
5. CHANGELOG and ADR-0016 remain historical and introduce no live rule.
6. ADR-0016 and its index row now consistently use `Accepted`; the general
   `Implementation candidate` definition remains available for genuinely local
   unaccepted candidates.
7. No document claims the corrected tip is already published, adopted by
   FrameNest, deployed, in production, or logically closed.
8. No new RF family or competing semantic/structural owner exists.

Any semantic rule present only in a projection, conflicting owner, duplicated
structural owner, or historical status that becomes false at acceptance or
publication is material and forbids PASS.

## 6. Continuation-bootstrap scenario matrix

Record PASS or exact defect evidence for each scenario:

- **C1 Minimal seed:** root consumer `AGENTS.md` plus the pinned AP required
  reading discovers the early named Continuation Bootstrap without prior chat,
  outgoing Orchestrator, handout, Meta, private memory, vendor, or new file.
- **C2 Stage separation:** Stage 1 restores/reconciles read-only; Stage 2 obtains
  the COOPERATOR's selection of exactly one bounded whole; only a later complete
  current Worker prompt can authorize mutation.
- **C3 Stale handout:** an absent outgoing Orchestrator is harmless and an old
  handout remains subordinate, non-authorizing evidence that cannot freeze the
  next whole.
- **C4 Finite discovery:** the path terminates through seed -> root `AGENTS.md`
  -> pinned `AP_ORCHESTRATOR.md` -> read-only restore -> declared ledger if any
  -> COOPERATOR selection -> separate Worker prompt, with no cyclic artifact.

## 7. Upgrade-ledger scenario matrix

Record PASS or exact defect evidence for each scenario:

- **L1 No declaration:** valid compatibility behavior; no AP-contracted storage
  is active, without falsely declaring all observations resolved.
- **L2 Valid empty ledger:** valid declaration/header and no entries means zero
  active entries for that exact target.
- **L3 Explicit discovery:** only a root project-owned `AGENTS.md` declaration
  outside the unchanged managed block activates storage; undeclared lookalikes
  remain ordinary content; no fixed filename or scan exists.
- **L4 Canonical identity:** the exact project-accepted repository identity is
  repeated byte-for-byte; AP invents no provider, `owner/name`, display-name,
  or local-path canonicalization.
- **L5 Path/collision:** repository-relative Markdown path, no `..`, no symlink
  escape, one target-to-one path, and duplicate target/path/id or conflict
  markers fail closed.
- **L6 Exact lifecycle record:** one header and 14-field structural entry;
  RF-09 retains all seven states/transitions; stable opaque non-ordinal ID; no
  AP-wide regex; ordering remains presentation.
- **L7 Accepted but unauthorized:** `accepted`, a stored expired task grant, and
  historical `authorized` status cannot renew mutation authority.
- **L8 Stale/unknown evidence:** `unknown because` and unrevalidated entries can
  be preserved but cannot support dependent mutation until current
  revalidation.
- **L9 Contradiction:** current repository/durable truth wins and an entry moves
  to `invalidated` with evidence.
- **L10 Malformed declaration/storage:** missing file/header, mismatch, unknown
  version, duplicates, invalid records, conflict markers, or path escape remain
  non-authorizing; read-only evidence may continue but reconciliation/dependent
  mutation stops.
- **L11 Terminal reconciliation:** terminal entries leave only after immutable
  historical evidence is named; active states remain; Git/promoted owner retain
  provenance; no second archive is created.
- **L12 Scope/privacy:** ledger cannot replace roadmap, issue, NEXT/current-task,
  Worker registry, transcript, specification, ADR, project rule, or protocol;
  secrets/private material/hidden reasoning are excluded.

## 8. Planner-artifact/report-completion matrix

Record PASS or exact defect evidence for each scenario:

- **R1 Artifact alone:** client-native planner artifact without the separate
  standard terminal report is incomplete and not planning PASS.
- **R2 Bounded repair:** only the same healthy session's next exchange, frozen
  artifact anchor, `not-used`, and report-only prohibitions may render the
  missing report; no overwrite, replanning, mutation, or extra planning cycle.
- **R3 Mode not authority:** `Native planning mode: not-used` remains routing
  metadata; a separate complete Implementation Authority Record is required;
  no new status/result/justification/filename/role/lifecycle is invented.
- **R4 Worker projection:** unchanged `AP_WORKER.md` already owns the Worker
  obligation and expiry; the completion branch is correctly placed in semantic,
  structural, Orchestrator, and P11 projections without duplication.

## 9. Historical lifecycle and publication-readiness matrix

Record PASS or exact defect evidence:

- **H1 Accepted truth:** ADR-0016 body and index say `Accepted`, consistent with
  the prior fresh acceptance of the semantic candidate and this required full
  fresh re-acceptance.
- **H2 Candidate definition retained:** the general `Implementation candidate`
  status definition is byte-identical and no unrelated ADR lifecycle changed.
- **H3 Phase separation:** the corrected tree does not claim publication,
  public-main presence, FrameNest adoption, deployment, production, or logical-
  whole closure.
- **H4 Publication-stable state:** if this acceptance returns PASS and a later
  Worker publishes the exact unchanged tip, the ADR/index status remains true;
  publication will not itself make any committed lifecycle statement false.
- **H5 No semantic correction:** the correction contains no live AP meaning,
  exact structural field, operational behavior, compatibility, or privacy
  change.

H4 is mandatory. The accepted artifact must describe its intended public tree,
not only the transient pre-publication moment.

## 10. Documentation-first validation

Under ADR-0015:

1. validate every relative Markdown link, local path, referenced heading, and
   anchor in all 12 cumulative changed files;
2. verify fenced code blocks are balanced per file;
3. compare every exact declaration/header/entry/repair spelling and allowed
   value against the one structural owner;
4. prove each canonical structural fixture occurs once;
5. search for accidental normative validation of `planning-PASS`,
   `planning-PARTIAL`, `planning-BLOCKED`, `no-new-material`,
   `invariant-failure`, or `public-ref-mutation`;
6. verify artifact relationship labels and canonical-owner links;
7. verify ADR number, filename, title, `Accepted` status, index relationship,
   and date;
8. verify compatibility language leaves current consumers on their old pins;
9. verify no executable-enforcement, conformance-test, publication, adoption,
   deployment, production, or closure claim; and
10. rerun final credential-free AP/FrameNest ref gates and candidate cleanliness
    after all inspection.

A dependency-free read-only helper may run from standard input or a validated
`/tmp` directory. Report and remove any temporary material. Do not install
dependencies, alter `.venv`, or run/recreate the retired monolithic suite.

## 11. Decision rules and prohibitions

Return `PASS` only if every C1-C4, L1-L12, R1-R4, H1-H5, owner/projection,
structural, Git, documentation, privacy, compatibility, and negative control is
proved from exact `17b7e085...`.

Return `PARTIAL` for a bounded material defect or missing evidence that requires
correction before publication. Return `BLOCKED` for failed hard gates,
invalid candidate identity, compromised independence, or unavailable required
evidence.

No second automatic correction is authorized. Any defect must be returned to
the ORCHESTRATOR for explicit disposition.

Explicit prohibitions:

- no source/index/worktree/branch/ref/configuration/dependency/external
  mutation;
- no edit, formatter, commit, amend, merge, rebase, cherry-pick, fetch, push,
  tag, release, issue, pull request, publication, adoption, deployment,
  production action, Meta archival, or closure;
- no consultation with Workers 3, 4, or 5 and no use of their reports as proof;
- no Worker 7/publication prompt generation;
- no model/provider/client/IDE requirement; and
- no secret, credential, private path/media, transcript, or hidden-reasoning
  disclosure.

Leave both candidate worktrees untouched. Clean only disposable material this
Worker created under `/tmp`.

## 12. Mandatory terminal report

Return exactly one complete standard terminal report in the same response. It
must begin at raw Markdown level with exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Do not escape the underscore.

Render exactly one actual value for each field:

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 06
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: acceptance-PASS | not-applicable
Result artifact or commit: 17b7e085139e9bcbb0e4953d26aef9b6687d541c | not-applicable
Result evidence: <bounded fresh-independent evidence>
Logical-whole closure: not-closed
Report justification: final-acceptance | new-evidence | new-material-risk | changed-external-state
Authority expiry: all Worker 6 acceptance authority expired at this terminal report
```

Use terminal `PASS`, `acceptance-PASS`, exact `17b7e085...`, and
`Report justification: final-acceptance` only when every gate passes. Otherwise
use `not-applicable` and the canonical justification actually supported.

The report must include:

1. fresh-session, independence, mode, capability, delegation, evidence, and
   authority confirmation;
2. exact public gates and both-commit candidate identity/ancestry/tree/subject/
   cleanliness evidence;
3. individual and cumulative path/mode/add/delete controls;
4. numbered C1-C4, L1-L12, R1-R4, and H1-H5 matrices with PASS or exact defect;
5. semantic-owner/projection and structural-owner verdicts;
6. historical lifecycle/publication-readiness verdict;
7. link/anchor/path/fence/whitespace/privacy/compatibility results;
8. commands and read-only probes summarized, with full output only for failure
   or unexpected state;
9. deviations, risks, missing evidence, and non-authorizing out-of-scope ledger
   candidates;
10. `Resolved Execution Issues / Near-Misses: none` or a complete bounded
    record;
11. `Pre-Existing Failure Classification: none` or a complete classification;
12. temporary material and cleanup evidence;
13. explicit confirmation that no mutation, push, publication, adoption, or
    closure occurred; and
14. one smallest next step: publication of exact corrected tip
    `17b7e085139e9bcbb0e4953d26aef9b6687d541c` if PASS, otherwise the smallest
    explicit correction/decision required.

Do not return an acceptance plan or informal summary. Stop immediately after
the terminal report; all Worker 6 authority expires regardless of context
health.


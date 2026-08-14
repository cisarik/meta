# Fresh Worker 5 — bounded ADR-0016 accepted-status correction

Use this text as the **sole authoritative Worker prompt**. Do not prepend prior
plans, implementation/acceptance prompts, reports, handouts, or Meta trace.
This is one decision-complete historical-projection correction discovered by
the ORCHESTRATOR after independent acceptance and before publication.

## 1. Coordinate, route, authority, and correction record

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Task phase: Correction implementation
Implementation authority: explicit
Exact correction baseline: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Changed-path allowlist: docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md; docs/adr/README.md
Implementation boundaries: historical lifecycle-status convergence only; no live semantic, structural, operational, executable, consumer, publication, or closure change
Independence required: no
```

```text
Acceptance candidate before correction: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Acceptance owner map: AP.md remains the sole live semantic owner; this correction touches historical projections only
Acceptance independence: required-fresh-independent after correction
Primary fresh acceptances used: 1
Automatic corrections used before this task: 0
Automatic correction authorized by this task: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: ADR-0016 and its index row must no longer claim Implementation candidate after acceptance-PASS
Out-of-scope observations: ledger-candidates
```

- Worker session profile: fresh bounded Correction Worker.
- Native planning mode is off. Do not create or revise a plan.
- Evidence tier: E1/E2 bounded repository and Git evidence.
- Reasoning recommendation: High, advisory only. No model/provider/client/IDE
  identity belongs in the repository or report.
- Internal delegation: prohibited.
- Authority covers one isolated local correction worktree, exactly two
  allowlisted files, validation, one local commit, and one terminal report.
- No push, publication, acceptance, FrameNest adoption, Meta archival,
  deployment, production action, or logical-whole closure is authorized.

## 2. Exact accepted candidate and public hard gates

The frozen independent acceptance outcome is:

```text
Accepted candidate: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Parent: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Tree: 7b53c74b7bfa183e490a0d81581a9f3db45c99d3
Subject: docs: define continuation bootstrap and observation ledgers
Acceptance result: acceptance-PASS
Acceptance Worker: session 04, exchange 02 final report rendering
```

The ORCHESTRATOR reverified these public refs credential-free immediately
before issuing this task:

```text
AP public refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

FrameNest public refs/heads/main:
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

FrameNest .ap gitlink at that commit:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Before mutation, independently prove:

1. `/home/agile/Projects/ap` is the canonical AP owner repository.
2. Credential-free AP and FrameNest public refs still equal the exact gates
   above.
3. Commit `a1b04ffc...` exists locally with the exact parent, tree, and subject
   above.
4. The original Worker 3 candidate worktree remains clean at `a1b04ffc...`;
   inspect it read-only and do not reuse or mutate it.
5. The two allowlisted files at `a1b04ffc...` actually identify ADR-0016 and its
   index row as `Implementation candidate`.
6. The candidate has not been published to AP `main`.

If any immutable identity or public gate differs, the status claim is absent,
the original candidate worktree is not clean, or the candidate is already
published, do not mutate. Return `BLOCKED` with the canonical justification
supported by the evidence.

Meta is archival-only and outside this task. Do not inspect or mutate it.

## 3. Proven defect and fixed correction

Current `docs/adr/README.md` defines:

```text
Implementation candidate: Accepted rationale in a local candidate; no public acceptance, publication, or closure claim
```

Independent Worker 4 has now emitted `acceptance-PASS` for exact candidate
`a1b04ffc...`, while its report confirms that ADR-0016 and its index row still
use `Implementation candidate`. Therefore that status is temporally false after
acceptance and would become still more misleading if published unchanged.

This is a bounded historical lifecycle-status defect. The continuation,
ledger-storage, report-repair, ownership, compatibility, and all other accepted
semantics remain frozen. Do not re-plan or reinterpret them.

Apply exactly this correction:

1. In `docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md`, set
   ADR-0016's lifecycle status to `Accepted`.
2. In `docs/adr/README.md`, set only ADR-0016's index status to `Accepted` and
   minimally remove or reword any ADR-0016-specific relationship text that
   would falsely call the now-accepted decision merely an implementation
   candidate.
3. Preserve the general `Implementation candidate` status definition and all
   other ADR/index rows unchanged.
4. Do not claim publication, public-main presence, FrameNest adoption,
   ORCHESTRATOR closure, deployment, or production state. `Accepted` means the
   independently accepted current durable decision; publication and closure
   remain later gates.
5. Preserve every substantive ADR-0016 decision, rationale, consequence,
   rejected alternative, semantic-owner link, and compatibility boundary
   byte-for-byte except for the minimum lifecycle-status wording required by
   items 1-2.

If another path appears to require mutation for consistency, stop and report
the exact evidence. Do not expand the allowlist.

## 4. Exact changed-path and non-change boundary

Change **all and only**:

```text
docs/adr/0016-universal-continuation-and-upgrade-ledger-storage.md
docs/adr/README.md
```

Everything else must remain byte-identical to `a1b04ffc...`, including:

- `AP.md`, `PROMPT_CONTRACTS.md`, `AP_ORCHESTRATOR.md`,
  `PROMPT_ENGINEERING_PATTERNS.md`, `ARTIFACT_LIFECYCLE.md`, `INTEGRATION.md`,
  README, FAQ, GLOSSARY, and CHANGELOG;
- every existing ADR body and every other ADR index row;
- `AP_WORKER.md`, `ap`, `ap.project.conf`, managed-block output, schema, tests,
  fixtures, CI, dependencies, and all executable content;
- FrameNest and Meta; and
- branches, refs, configuration, accounts, services, providers, deployment, and
  production state outside the one authorized local correction branch/worktree.

No new file, deletion, rename, mode change, schema, parser, validator, test,
template, or generated artifact is authorized.

## 5. Isolated worktree and Git authority

Use the owner repository only as the Git-object/worktree owner:

```text
Owner repository: /home/agile/Projects/ap
New branch: fix/adr-0016-accepted-status
New worktree: /home/agile/Projects/ap-worktrees/ap-universal-project-continuation-bootstrap-and-durable-observation-ledger-w5
Base: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
```

Inspect existing branches, worktrees, and the exact target path read-only before
creation. Do not clean, stash, reset, switch, overwrite, delete, or reuse any
existing worktree or branch. If the named branch or worktree path already
exists, stop `BLOCKED` rather than modifying it.

Authorized Git mutations are limited to:

1. creating that one local branch/worktree from exact `a1b04ffc...`;
2. editing the two allowlisted files;
3. staging exactly those two paths; and
4. creating one local commit with exact subject:

```text
docs: mark ADR-0016 accepted
```

The correction commit must have exactly one parent:
`a1b04ffcebda197bfe25c4258d9e6d96328d36b1`.

Do not amend, merge, rebase, cherry-pick, fetch, push, tag, force, delete refs or
worktrees, change Git configuration, or mutate the original accepted candidate
branch/worktree. If existing signing or repository policy blocks the commit, do
not weaken it; report the blocker.

Leave the new clean correction branch/worktree intact for full fresh
re-acceptance. No temporary clone is authorized or needed.

## 6. Required validation

Before commit:

1. inspect the complete two-file diff;
2. prove only ADR-0016-specific lifecycle status/relationship wording changed;
3. prove the general status table, every other ADR row/body, and all accepted
   substantive text remain unchanged;
4. verify ADR-0016 body and index both say `Accepted` consistently;
5. verify neither file claims publication, closure, FrameNest adoption,
   deployment, or production state;
6. verify relative links and referenced paths/headings in both files resolve;
7. verify fenced blocks remain balanced;
8. run `git diff --check`; and
9. prove the changed-path set is exactly the two-file allowlist.

After commit, prove:

- parent is exact `a1b04ffc...`;
- subject is exact `docs: mark ADR-0016 accepted`;
- the new commit is not a merge;
- exactly two paths changed, with no add/delete/rename/mode change;
- the correction worktree is clean;
- original candidate worktree/branch remains unchanged at `a1b04ffc...`;
- public AP and FrameNest gates remain unchanged; and
- no push occurred.

Use documentation-first proportional validation. Do not run or recreate the
retired monolithic suite, install dependencies, or create/rebuild a virtual
environment.

## 7. PASS and stopping criteria

Report `PASS` only if one clean local correction commit satisfies every fixed
requirement and negative control above.

Stop `PARTIAL` or `BLOCKED` without broadening authority if:

- a public/immutable gate differs;
- candidate status is not as reported;
- branch/worktree isolation cannot be created safely;
- any third path requires mutation;
- accepted semantics would need modification;
- lifecycle status cannot be made consistent without claiming a later phase;
- validation fails materially; or
- commit creation fails under existing policy.

This automatic correction is the only one authorized. The corrected tip must
receive full fresh independent acceptance before publication. Do not generate
that acceptance prompt yourself.

## 8. Mandatory terminal report

Return exactly one complete standard terminal report in the same response. It
must begin at raw Markdown level with the exact line:

```text
### Report for ORCHESTRATOR_CHAT
```

Do not escape the underscore.

Metadata must contain one actual value for each field:

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 05
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | not-applicable
Result artifact or commit: <exact correction commit SHA or not-applicable>
Result evidence: <bounded exact evidence>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk | changed-external-state
Authority expiry: all Worker 5 correction authority expired at this terminal report
```

Render one actual value, never the alternatives. A successful committed
correction uses terminal `PASS`, `implementation-PASS`, the exact new commit,
and `Report justification: new-mutation`. A stopped task uses `not-applicable`
and the one justification actually supported.

The report must include:

1. fresh route, mode, capability, delegation, evidence, and authority record;
2. exact public and candidate pre-mutation gates;
3. new branch/worktree isolation and preservation of prior worktrees;
4. start/end commit, parent, tree, subject, changed paths, and clean status;
5. exact before/after ADR-0016 body and index lifecycle statuses;
6. proof that substantive accepted semantics and every non-allowlisted surface
   remain unchanged;
7. validation commands and bounded results;
8. commit result and `Push: not-authorized, not-performed`;
9. deviations, risks, missing evidence, and out-of-scope ledger candidates;
10. `Resolved Execution Issues / Near-Misses: none` or a complete bounded
    record;
11. `Pre-Existing Failure Classification: none` or a complete classification;
12. temporary material and cleanup status;
13. explicit confirmation that neither publication nor closure occurred; and
14. one smallest next step: full fresh independent acceptance of the exact new
    correction tip.

Stop autonomous work immediately after the report. All Worker 5 authority
expires there regardless of context health.


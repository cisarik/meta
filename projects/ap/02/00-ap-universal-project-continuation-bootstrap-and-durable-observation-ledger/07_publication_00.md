# Fresh Worker 7 — publish the accepted AP continuation candidate

Use this text as the **sole authoritative Worker prompt**. Do not prepend or use
prior plans, implementation/correction/acceptance prompts, Worker reports,
handouts, or Meta trace as publication authority. The exact accepted Git object
and this grant are sufficient.

## 1. Coordinate, route, and publication authority

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 07
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Task phase: Publication
Publication authority: explicit
Accepted publication candidate: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Expected public ref before publication: refs/heads/main = 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Expected public ref after publication: refs/heads/main = 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Push mode: one ordinary non-force fast-forward push of the exact accepted object
Independence required: no
```

- Worker session profile: fresh Publication Worker.
- Native planning mode is off. Do not plan, implement, correct, or accept.
- Evidence tier: E1/E2 exact Git-object and direct public-readback evidence.
- Reasoning recommendation: High, advisory only. No model/provider/client/IDE
  identity belongs in the result.
- Internal delegation: prohibited. One accountable Worker performs the single
  publication operation and its readback.
- Positive mutation authority is limited to one ordinary non-force push of
  exact commit `17b7e085...` to AP `refs/heads/main` when and only when every
  preflight gate below matches.
- No source, index, commit, branch, tag, configuration, FrameNest, Meta,
  consumer, release, issue, pull request, deployment, production, or closure
  mutation is authorized.

## 2. Frozen accepted stack

The exact full-fresh accepted stack is:

```text
Public baseline:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

Semantic implementation commit:
a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Parent: 041de310ea33ed1b47dd8f5fbfcc2829d1a32514
Tree: 7b53c74b7bfa183e490a0d81581a9f3db45c99d3
Subject: docs: define continuation bootstrap and observation ledgers

Accepted publication tip:
17b7e085139e9bcbb0e4953d26aef9b6687d541c
Parent: a1b04ffcebda197bfe25c4258d9e6d96328d36b1
Tree: 6f0d09c9db0b8b45b36a7ff3bdd9a3ef61d56c4a
Subject: docs: mark ADR-0016 accepted
```

Full-fresh independent acceptance of exact `17b7e085...` is complete and
terminal `acceptance-PASS`. The accepted tree is publication-stable: ADR-0016
and its index say `Accepted`, while publication, consumer adoption, and
logical-whole closure remain separate later facts.

Expected local evidence:

```text
AP owner repository: /home/agile/Projects/ap
Accepted branch: fix/adr-0016-accepted-status
Accepted worktree: /home/agile/Projects/ap-worktrees/ap-universal-project-continuation-bootstrap-and-durable-observation-ledger-w5
Original implementation worktree: /home/agile/Projects/ap-worktrees/ap-universal-project-continuation-bootstrap-and-durable-observation-ledger-w3
Canonical public repository: https://github.com/cisarik/ap.git
```

## 3. Public and consumer hard gates

The ORCHESTRATOR reverified these credential-free refs immediately before
issuing this prompt:

```text
AP public refs/heads/main:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514

FrameNest public refs/heads/main:
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb

FrameNest .ap gitlink at that commit:
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

Meta is archival-only, may advance concurrently, and is deliberately not a
publication gate. Do not inspect or mutate it.

## 4. Mandatory read-only preflight

Before any push, independently prove all of the following without changing any
repository:

1. `/home/agile/Projects/ap` is the intended AP owner repository and its
   configured `origin` resolves to canonical public AP.
2. A credential-free direct `ls-remote` of public AP `refs/heads/main` returns
   exactly one of the two explicitly handled states in section 5.
3. A credential-free direct `ls-remote` of FrameNest `refs/heads/main` still
   equals `230ce43a...`.
4. Commit-bound FrameNest inspection, without reading/changing its live
   worktree, confirms `.ap` remains a gitlink to `041de310...`.
5. Accepted worktree and branch are clean and point exactly to
   `17b7e085...`; the branch contains no later commit.
6. `17b7e085...` is a commit with exact tree, parent, and subject above;
   `a1b04ffc...` has the exact tree, parent, and subject above.
7. The stack is linear, two commits, non-merge, and
   `041de310...` is an ancestor of `17b7e085...`.
8. Cumulative baseline-to-tip changed paths are exactly the accepted 12-path
   documentation set; the correction commit changes exactly the accepted two
   historical paths.
9. ADR-0016 body and index at the tip say `Accepted`; no source mutation is
   needed before publication.
10. No local source/index mutation, pending commit, merge/rebase state, or
    ambiguous ref could change the exact object being pushed.

If FrameNest differs, an immutable candidate identity fails, the accepted
worktree is dirty, or any preflight condition is unresolved, do not push. Return
terminal `BLOCKED` with the canonical justification supported by the evidence.

Do not run implementation tests or recreate the retired AP suite. Publication
preflight is exact object continuity, not re-acceptance.

## 5. Exactly two public-ref states

After all other preflight gates pass, classify AP public `refs/heads/main`:

### State A — expected unpublished baseline

If public `main` equals exactly:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

perform exactly one externally mutating operation: an ordinary, non-force push
of the exact accepted object to the exact destination:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c:refs/heads/main
```

Use the existing configured authenticated `origin` transport. Prefer porcelain
output. Do not push by a symbolic branch name, and do not push another ref.

### State B — already published exact tip

If public `main` already equals exactly:

```text
17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

perform no push. Continue directly to the complete credential-free public
readback in section 7. This race-safe path may still return publication PASS if
all public evidence is exact; its report uses `Report justification:
new-evidence` rather than claiming a mutation by this Worker.

### Any other public state

If public `main` equals neither baseline nor accepted tip, do not push, merge,
rebase, fetch-to-integrate, force, retry, or reinterpret ancestry. Return
terminal `BLOCKED` with `Report justification: changed-external-state` and the
exact observed ref.

## 6. Push constraints for State A

- One push attempt only.
- Ordinary non-force fast-forward semantics only.
- Exact SHA-to-`refs/heads/main` refspec only.
- No `--force`, `--force-with-lease`, deletion, tag, feature-branch push,
  wildcard, mirror, atomic multi-ref push, merge, squash, rebase, or amend.
- No Git configuration or credential-helper change.
- Never print, copy, request, or expose a credential/token.
- Do not disable repository hooks, signing, branch protections, or transport
  checks.
- If authentication, hook, policy, connection, non-fast-forward, or provider
  rejection occurs, preserve the complete bounded failure, perform one
  credential-free public-ref read, and stop. Do not retry or weaken controls.
- Do not alter local refs merely to make the push appear successful.

The expected fast-forward publishes the exact two accepted commits. There is no
new publication commit.

## 7. Required direct public readback

Whether State A or State B applied, publication PASS requires both evidence
layers below after the push/no-push decision.

### 7.1 Credential-free ref readback

Using the canonical public HTTPS repository with interactive prompting and
credential helpers disabled, prove:

```text
refs/heads/main = 17b7e085139e9bcbb0e4953d26aef9b6687d541c
```

The configured authenticated `origin` view alone is insufficient.

### 7.2 Disposable credential-free object/content readback

Create one temporary directory with `mktemp -d` outside all repositories. Use a
credential-free public HTTPS clone/fetch into that exact directory and inspect
the public objects, not the retained local candidate worktree.

Prove from the disposable public readback:

1. public HEAD/main is exact `17b7e085...`;
2. its tree is `6f0d09c9db0b8b45b36a7ff3bdd9a3ef61d56c4a`;
3. its parent is exact `a1b04ffc...` and subject is exact;
4. `a1b04ffc...` has parent `041de310...`, tree `7b53c74...`, and exact
   subject;
5. both commits are single-parent and form the accepted linear stack;
6. baseline-to-public-tip path set is exactly the accepted 12 paths;
7. correction-commit path set is exactly ADR-0016 and the ADR index;
8. ADR-0016 body/index at public tip say `Accepted`;
9. `AP.md`, `PROMPT_CONTRACTS.md`, and `AP_ORCHESTRATOR.md` blobs at public tip
   are the exact blobs carried by accepted `17b7e085...`; and
10. no additional public commit or ref substitution occurred.

Record the temporary directory path. Clean it with a path-validated operation
only after readback succeeds or conclusively fails. Never use an unresolved
variable, broad path, home directory, workspace root, or repository root as a
cleanup target. Report creation and cleanup outcome.

## 8. Post-publication negative controls

Before PASS, also prove:

- accepted and original implementation worktrees remain clean and unchanged;
- owner repository source/index/configuration is unchanged;
- no local commit, amend, merge, rebase, tag, extra ref, release, issue, pull
  request, or feature branch was published;
- FrameNest public `main` remains exact `230ce43a...` and its pin remains
  `041de310...`; AP publication does not silently update a consumer;
- no Meta read or mutation occurred;
- no deployment, production action, ledger adoption, or logical-whole closure
  occurred; and
- the non-authorizing legacy-copy detection observation from acceptance was not
  investigated or allowed to expand publication scope.

Do not delete the retained candidate branches/worktrees. Their later cleanup is
an ORCHESTRATOR-owned separate action after closure.

## 9. Publication PASS and stopping rules

Return publication `PASS` only when:

- preflight identities and public gates pass;
- either State A produced one successful ordinary non-force push or State B
  proved the exact tip was already public;
- credential-free ref readback equals exact `17b7e085...`;
- disposable public object/content readback proves the accepted commit, tree,
  ancestry, subjects, paths, and Accepted ADR status;
- temporary public-readback material is safely cleaned;
- no unauthorized local/external mutation occurred; and
- all post-publication negative controls pass.

Return `PARTIAL` only if a public mutation succeeded but one bounded mandatory
readback/cleanup fact remains unresolved. Return `BLOCKED` before mutation for
failed hard gates, or after a failed push with no confirmed public mutation.
Never claim PASS based only on push exit code or configured-remote output.

No correction, rollback, second push, force, or new task is authorized. Preserve
failure evidence and stop.

## 10. Mandatory terminal report

Return exactly one complete standard terminal report in the same response. It
must begin at raw Markdown level with exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Do not escape the underscore.

Render one actual value for every field:

```text
Logical whole identity: ap-universal-project-continuation-bootstrap-and-durable-observation-ledger
Worker session ordinal: 07
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: publication-PASS | not-applicable
Result artifact or commit: 17b7e085139e9bcbb0e4953d26aef9b6687d541c | not-applicable
Result evidence: <bounded exact push and direct public-readback evidence>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk | changed-external-state
Authority expiry: all Worker 7 publication authority expired at this terminal report
```

Use terminal `PASS`, `publication-PASS`, and exact `17b7e085...` only after all
publication and readback gates pass. State A normally uses `Report
justification: new-mutation`; State B uses `new-evidence`. Otherwise use
`not-applicable` and the one canonical justification actually supported.

The report must include:

1. fresh-session, mode, capability, delegation, evidence, and exact publication
   authority confirmation;
2. AP/FrameNest preflight refs, candidate identities, cleanliness, and selected
   State A/B evidence;
3. exact push command/refspec classification, bounded porcelain result, attempt
   count, and confirmation of non-force single-ref semantics, or exact
   already-published classification;
4. credential-free public ref readback;
5. disposable public object/content readback: tip/tree/parent/grandparent/
   subjects/path sets/ADR Accepted status and key blobs;
6. negative controls for local refs/worktrees/config, FrameNest, Meta,
   deployment, production, adoption, and closure;
7. temporary directory creation, exact path, cleanup action, and outcome;
8. deviations, risks, missing evidence, and out-of-scope observations;
9. `Resolved Execution Issues / Near-Misses: none` or a complete bounded
   record;
10. `Pre-Existing Failure Classification: none` or a complete applicable
    classification;
11. explicit final public `refs/heads/main` identity and whether this Worker
    performed the mutation; and
12. one smallest next step: ORCHESTRATOR logical-whole closure and ledger
    reconciliation, not FrameNest adoption inside this whole.

Do not return a publication plan or informal summary. Stop immediately after
the terminal report; all Worker 7 authority expires regardless of context
health.


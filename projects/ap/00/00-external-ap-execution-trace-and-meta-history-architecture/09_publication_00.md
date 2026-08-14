# Worker 9 — Exact Publication of the Accepted AP External Trace Stack

## External AP Execution Trace and Meta-History Architecture

### Routing and publication authority

Persistent role identity: You are one concrete Worker instance assigned to the single persistent `WORKER` role.

Logical whole identity: `external-ap-execution-trace-and-meta-history-architecture`

Worker number: `Worker 9`

Worker session ordinal: `09`

Worker exchange ordinal: `01`

Worker session target: `fresh-worker-session`

Freshness anchor: this must be a genuinely fresh Worker session that did not act as Worker 5, Worker 6, Worker 7, or Worker 8; did not implement, correct, or accept either commit in the stack; and has not retained any earlier Worker's authority. This prompt is the complete and only current authority grant.

Native planning mode: `not-used`

Worker session profile: `Fresh Exact Publication Worker`

Phase: `Publication`

Task identity: `AP-EXTERNAL-TRACE-EXACT-PUBLICATION-W09-X01`

Reasoning recommendation: `Medium` — advisory only. This is a bounded E1 ordinary non-force publication with exact object, ref, and readback gates. Michal controls the actual model, agent, provider, client, and reasoning configuration.

Sub-agents/internal delegation: `not-used`

Explore-style task: `not-used`

Worker topology: `single-active`

External trace disposition: `configured` — archival is a manual Cooperator action outside this Worker grant. Trace artifacts are historical evidence only and grant no task, Git, publication, acceptance, or closure authority.

Acceptance state supplied by the Orchestrator: `accepted-by-fresh-independent-worker-and-reconciled-for-publication`

Publication authority: `one-exact-ordinary-non-force-fast-forward-push`

Authorized public ref transition:

```text
1b0774117e1de7ecabddc7f08d15dbaf3068b09b:refs/heads/main
  ->
81dee2c182322ac95999e5d4ee42072b6040e44a:refs/heads/main
```

Exact authorized push source and destination:

```text
81dee2c182322ac95999e5d4ee42072b6040e44a:refs/heads/main
```

Authorized remote: canonical `cisarik/ap` origin at `https://github.com/cisarik/ap.git`.

Push-attempt budget: exactly one push attempt, and only after every pre-publication gate passes.

Force authority: `none` — no force, force-with-lease, ref deletion, history rewrite, or recovery push.

Tag, branch, release, PR, and deployment authority: `none` except the one exact `refs/heads/main` update above.

Source-repository mutation authority before push: `none`.

Authorized source-repository side effects of the exact successful publication:

- the ordinary push may update local remote-tracking `refs/remotes/origin/main` as Git's direct consequence;
- after exact public-object verification succeeds, one compare-and-swap update may advance local `refs/heads/main` from the exact old baseline to the exact published tip;
- if `refs/remotes/origin/main` did not advance automatically but still equals the exact old baseline, one compare-and-swap update may advance it to the exact publicly verified tip;
- no checkout, working-tree rewrite, symbolic-ref rewrite, or other local ref movement is authorized.

Temporary evidence authority: one safely created, exactly resolved temporary root outside the AP worktree containing one credential-free public clone after the push. It exists only to verify the published object, history, tree, path boundary, and public default branch. Delete only that exact owned root using bounded depth-first deletion; do not use recursive-force deletion.

Meta authority: `none` — do not read, edit, stage, commit, or otherwise use the Meta repository.

Implementation, correction, acceptance, deployment, production, provider, account, and closure authority: `none`.

Logical-whole closure authority: `none`.

Terminal publication report point: after either the first fail-closed blocker or completion of the exact push, independent public verification, authorized local-ref convergence, temporary-root cleanup, and final repository checks. Stop before any closure or follow-on work.

### 1. Mission

Publish the already accepted immutable AP tip:

```text
81dee2c182322ac95999e5d4ee42072b6040e44a
```

to canonical public:

```text
refs/heads/main
```

using one ordinary non-force fast-forward that publishes this exact ordered two-commit stack above the current public baseline:

```text
1b0774117e1de7ecabddc7f08d15dbaf3068b09b
  -> f117457a1e346278ad3fe6c22c3ab57db2217374
  -> 81dee2c182322ac95999e5d4ee42072b6040e44a
```

Do not create, amend, squash, reconstruct, cherry-pick, merge, or substitute any commit. Do not publish an equivalent tree under another commit identity. Do not alter AP content.

Fresh Worker 8 independently accepted exact tip `81dee2c...` and the complete stack. That terminal report expired Worker 8's authority. Treat the Orchestrator's reconciled acceptance state as the route prerequisite for publication, while still verifying every immutable Git identity and publication gate directly.

This task succeeds only if:

1. the local source repository contains the exact accepted objects and topology;
2. the source worktree, index, ignored state, control state, and protected external-artifact boundary are clean;
3. the contained full AP suite at the exact tip exits `0` with `92 passed` and `0 failed`;
4. immediately before the push, credential-free public `refs/heads/main` still equals the exact baseline and the public heads/tags inventory remains exactly one head, `refs/heads/main`;
5. exactly one ordinary explicit-refspec push exits `0`;
6. credential-free direct readback and a new credential-free public clone prove the exact published tip, tree, parents, ordered history, path union, default branch, and ref inventory;
7. only the explicitly authorized local canonical refs converge to the publicly verified tip;
8. the source repository finishes clean at the same topic-branch `HEAD`;
9. no additional ref, commit, tag, branch, PR, release, deployment, provider call, consumer mutation, Meta mutation, or closure occurs.

Return `publication-PASS` only when all nine claims are directly proven. Publication does not close the logical whole.

### 2. Settled acceptance facts and evidence limits

Treat the following as the publication specification and authority boundary:

1. Canonical AP repository: `cisarik/ap`.
2. Accepted original baseline:

```text
Commit: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Parent: 82d9db0602cfe9177f9f2a07dd662b14b339d6cd
Tree: a5ed323188189fcf12bda9559ab55defc9e0808a
Subject: fix: enforce orchestrator-only closure contract
```

3. Accepted first stack commit:

```text
Commit: f117457a1e346278ad3fe6c22c3ab57db2217374
Parent: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Tree: 0b6eec31d83e48d82a72e612476d81b21dced652
Subject: feat: define external analytic trace exchanges
Stat: 12 files changed, 987 insertions(+), 27 deletions(-)
```

4. Exact accepted corrected tip:

```text
Commit: 81dee2c182322ac95999e5d4ee42072b6040e44a
Parent: f117457a1e346278ad3fe6c22c3ab57db2217374
Tree: 2bec056a46b1e442800bd46b5ec42a03e8d26f58
Subject: fix: enforce canonical trace transition example
Stat: 2 files changed, 19 insertions(+), 12 deletions(-)
Paths: PROMPT_CONTRACTS.md, tests/ap_tool_tests.sh
```

5. Exact baseline-to-tip cumulative stat:

```text
12 files changed, 994 insertions(+), 27 deletions(-)
```

6. Exact baseline-to-tip path union:

```text
AP.md
AP_ORCHESTRATOR.md
AP_WORKER.md
ARTIFACT_LIFECYCLE.md
CHANGELOG.md
FAQ.md
GLOSSARY.md
PROMPT_CONTRACTS.md
README.md
docs/adr/0014-external-analytic-trace-and-worker-exchange-identity.md
docs/adr/README.md
tests/ap_tool_tests.sh
```

7. Worker 8 established `acceptance-PASS`, resolved `AP-TRACE-A01-F01`, found no new finding, and reported baseline/candidate/tip suites of `91/0`, `92/0`, and `92/0`.
8. The Orchestrator has reconciled that report and authorizes this exact publication phase.
9. Acceptance evidence does not replace present-time public-ref, local-state, object, suite, push-exit, or post-publication readback evidence.
10. A terminal Worker report always states `Logical-whole closure: not-closed`.
11. Only the Orchestrator may reconcile publication, emit the closure record, or select any later logical whole.
12. Meta is external historical evidence. Its existence, filenames, commits, or archived reports are neither publication prerequisites nor authority.

Do not reopen accepted RF-19 semantics, start a new audit, repair wording, or seek a different implementation. Stop only for a concrete identity, state, suite, public-ref, push, or readback failure.

### 3. Repository and environment preflight

Begin in the AP workspace supplied by Michal.

Expected repository state:

```text
Physical top level: /home/agile/Projects/ap
Canonical origin: https://github.com/cisarik/ap.git
Expected branch: docs/semantic-ownership-convergence
Expected upstream: none
Expected HEAD: 81dee2c182322ac95999e5d4ee42072b6040e44a
Expected local main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Expected available origin/main: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Expected symbolic origin/HEAD: refs/remotes/origin/main
Expected credential-free public main before push: 1b0774117e1de7ecabddc7f08d15dbaf3068b09b
Expected public heads/tags before push: exactly refs/heads/main, with no tag
```

An isolated `.git/REBASE_HEAD` containing exactly:

```text
573975cffc5ce94c481553168abc040d4ad39557
```

is permitted only as unchanged inert pre-existing metadata if ordinary Git shows no active operation, both rebase directories are absent, no lock exists, and no effective non-sample hook can affect the task. Do not remove or alter it. Any different or active Git-control state is a blocker.

Before any network mutation:

1. Resolve the physical top level, Git/common directory, worktree inventory, branch, upstream, exact `HEAD`, origin identity, local `main`, available `origin/main`, and symbolic `origin/HEAD`.
2. Inspect repository status including staged, unstaged, untracked, and ignored state.
3. Verify there is one worktree, no concurrent repository mutation, no active Git operation, no lock, and no effective non-sample hook.
4. Verify trusted system binaries without using `cursor`, `code`, `xdg-open`, GUI, AppImage, IDE-integrated wrappers, or shell aliases that change Git semantics.
5. Ambient editor/AppImage/environment markers may exist by name. Do not print their values. Stop if a resolved executable or repository path is inside an editor/AppImage bundle or if Git-control environment would redirect the repository, index, objects, worktree, or configuration.
6. Do not inspect, print, enumerate, copy, or modify credential values, credential stores, tokens, SSH keys, private configuration payloads, browser state, or unrelated environment values.
7. Ordinary use of already configured task-relevant Git credentials is authorized only for the one exact push. Credential-free public reads must disable prompting and credential-helper use for those reads.
8. Verify that none of these external artifacts is inside the AP worktree:

```text
05_implementation.md
05_report.md
05_implementation_02.md
05_report_02.md
06_acceptance.md
06_report.md
07_correction.md
07_report.md
08_acceptance.md
08_report.md
09_publication.md
09_report.md
```

9. If any such artifact is present inside AP, stop. Do not read it from the repository, move it, delete it, ignore it, stage it, or absorb it.
10. Do not modify Git configuration, remotes, hooks, worktrees, branches, tags, index, working files, or refs during preflight.

Any mismatch is classified against the exact repository, ref, object, control-state, or path unit using the canonical recovery classes:

```text
accepted-continuation
unrelated-owner-work
stale-clone
unpublished-candidate
unexplained-divergence
```

The accepted two-commit stack on the exact topic branch is the expected `accepted-continuation` and also an `unpublished-candidate`. Any unclassified material remainder is `unexplained-divergence` and blocks publication. Do not repair a mismatch by fetch, pull, reset, clean, checkout, switch, stash, merge, rebase, cherry-pick, branch movement, ref movement, deletion, or configuration change.

### 4. Immutable-object and topology gate

Before running tests or pushing, verify directly:

1. All three named commits exist locally as commits.
2. `f117457a...` has sole parent `1b077411...`.
3. `81dee2c...` has sole parent `f117457a...`.
4. `1b077411...` is an ancestor of the accepted tip.
5. Exactly two commits exist in `1b077411...81dee2c...` and exactly one in `f117457a...81dee2c...`.
6. The commit subjects and trees exactly match section 2.
7. Object connectivity passes without fetch, replacement objects, grafts, shallow substitution, or alternate object storage.
8. The first commit has the exact twelve-path/stat boundary stated above.
9. The correction commit has exactly the two named paths and exact stat stated above.
10. The baseline-to-tip union and cumulative stat exactly match section 2.
11. No rename, mode change, symlink, submodule, binary, generated path, or additional path occurs.
12. The accepted tip has exactly one RF-19 owner-map row, exactly one RF-19 test registration, and no external prompt/report artifact.
13. `AP.md` is byte-identical between first candidate and corrected tip.
14. These protected surfaces are byte-identical to the original baseline:

```text
ap
ap.project.conf
INTEGRATION.md
UPDATING.md
PROMPT_ENGINEERING_PATTERNS.md
INFOSEC.md
.gitignore
```

15. `git diff --check` passes for baseline-to-first-candidate, first-candidate-to-tip, and baseline-to-tip.
16. No commit, tree, subject, path, stat, topology, or protected-surface equivalence may be inferred from a report when Git can prove it directly.

If any gate fails, do not push. Return `BLOCKED` with the first exact causal mismatch and authority expiry.

### 5. Exact pre-publication validation

Run shell syntax validation:

```sh
sh -n tests/ap_tool_tests.sh
```

Then run the exact contained full suite once at the accepted tip:

```sh
env -u VIRTUAL_ENV_DISABLE_PROMPT sh tests/ap_tool_tests.sh
```

Required result:

```text
exit: 0
passed: 92
failed: 0
```

The inherited `VIRTUAL_ENV_DISABLE_PROMPT` marker must be removed only for this suite invocation. Do not edit the runner, tests, shell initialization, or environment configuration because of that marker.

After the suite:

1. prove the worktree, index, untracked, and ignored state remain clean;
2. prove exact `HEAD`, branch, local refs, origin identity, control state, and object identities remain unchanged;
3. prove no suite process remains;
4. do not rerun a passing suite merely to obtain preferred formatting;
5. any non-zero exit or traceback forbids publication and forbids `PASS`;
6. do not repair any failure under this grant.

### 6. Final pre-push public gate

After every local and suite gate passes, perform fresh credential-free, non-interactive public reads of the canonical HTTPS remote. Do not use or inspect configured credentials for these reads.

Require all of the following immediately before the push:

1. public `refs/heads/main` equals exactly:

```text
1b0774117e1de7ecabddc7f08d15dbaf3068b09b
```

2. public `HEAD` is a symbolic reference to `refs/heads/main` and resolves to the same baseline;
3. the complete public heads/tags inventory contains exactly one ref:

```text
refs/heads/main
```

4. no public tag or additional branch exists;
5. local `refs/heads/main` and available `refs/remotes/origin/main` still equal the same baseline;
6. source topic-branch `HEAD` still equals the exact accepted tip;
7. no concurrent mutation is observed between the readback and push boundary.

If public `main` already equals the accepted tip before your push, do not push and do not claim that you published it. Return `PARTIAL` with `Report justification: changed external state`, exact public evidence, and authority expiry so the Orchestrator can reconcile externally completed publication.

If public `main` equals neither the expected baseline nor the accepted tip, return `BLOCKED` with `Report justification: changed external state`. Do not fetch, force, merge, rebase, retry, or move any ref.

If the public inventory contains an unexpected ref even while `main` matches, return `BLOCKED`. Do not delete or normalize it.

### 7. Sole authorized publication mutation

Only when every prior gate passes, perform exactly one ordinary non-force push attempt using the exact accepted commit as source and the exact canonical branch as destination.

The semantic shape of the sole authorized command is:

```sh
git push --porcelain --no-follow-tags origin 81dee2c182322ac95999e5d4ee42072b6040e44a:refs/heads/main
```

Use the already verified trusted system Git binary and disable terminal prompting. Do not expose or inspect credentials. The ordinary configured credential path may be used solely to authenticate this exact mutation.

Required push properties:

- exact remote `origin`, already verified as canonical `cisarik/ap`;
- exact source commit `81dee2c...`, not a branch-name abbreviation;
- exact destination `refs/heads/main`;
- one ref only;
- ordinary fast-forward only;
- no force or force-with-lease;
- no tag following;
- no `--all`, `--mirror`, `--tags`, `--delete`, `--prune`, `--set-upstream`, push option, receive-pack override, URL override, remote rewrite, or configuration mutation;
- exactly one push attempt;
- exit `0` required for `publication-PASS`.

Do not run a push dry-run and do not make a second push attempt. Access to credentials or a successful authentication check is not publication authority for any other mutation.

If the push is rejected, interrupted, ambiguous, or exits non-zero:

1. do not retry;
2. perform only credential-free public readback to determine the observed public ref;
3. do not perform local-ref convergence;
4. return `PARTIAL` if any remote mutation may have occurred or public `main` now equals the tip;
5. otherwise return `BLOCKED`;
6. record the exact exit code and bounded non-sensitive output;
7. never return `PASS` after a non-zero push exit, even if later public readback shows the target tip.

### 8. Mandatory independent post-publication readback

After and only after the one push exits `0`, perform direct credential-free, non-interactive public readback.

First require:

1. public `refs/heads/main` equals exactly `81dee2c182322ac95999e5d4ee42072b6040e44a`;
2. public `HEAD` is symbolic to `refs/heads/main` and resolves to the same tip;
3. the complete public heads/tags inventory remains exactly one ref, `refs/heads/main`;
4. no tag or additional branch appeared.

Then create exactly one owned temporary root under the system temporary directory using a specific `ap-publication-w09` prefix. Resolve and validate the exact root before use. Make one full credential-free clone of canonical public `https://github.com/cisarik/ap.git` inside it with checkout disabled. Do not use the local AP object database, hardlinks, alternates, bundles, archives, or the authenticated push transport as substitute evidence.

In the public clone, prove directly:

1. remote/default `HEAD` identifies `refs/heads/main`;
2. public `main` is exact tip `81dee2c...`;
3. the public tip's parent is exact `f117457a...`;
4. the first candidate's parent is exact baseline `1b077411...`;
5. all three public objects have the exact trees and subjects stated in section 2;
6. exactly two commits exist above baseline and no merge exists in that range;
7. the merge base of baseline and tip is exact baseline;
8. the first-commit, correction-commit, and cumulative path/stat boundaries exactly match section 2;
9. object connectivity passes in the public clone;
10. the public tree contains no unexpected object type, symlink, submodule, or binary addition;
11. the protected surfaces remain byte-identical to baseline;
12. the public `AP.md` is byte-identical between first candidate and tip;
13. the complete public heads/tags inventory visible from the clone is consistent with the direct readback.

This public clone is object-publication evidence, not a new acceptance cycle. Do not run the full suite again inside it unless the source-tip suite did not actually run; in that case publication was already forbidden and you must not have pushed.

If any post-push direct or clone readback fails, mismatches, or is incomplete, stop additional mutation. Clean the exact owned temporary root if safely possible and return `PARTIAL`, because public state may already have changed. Do not push again and do not attempt repair.

### 9. Authorized local canonical-ref convergence

Only after all post-publication public-object evidence in section 8 passes may you converge the authorized local canonical refs.

Required final local state:

```text
refs/heads/main                    = 81dee2c182322ac95999e5d4ee42072b6040e44a
refs/remotes/origin/main          = 81dee2c182322ac95999e5d4ee42072b6040e44a
topic-branch HEAD                 = 81dee2c182322ac95999e5d4ee42072b6040e44a
refs/remotes/origin/HEAD          -> refs/remotes/origin/main
```

Rules:

1. If ordinary push already advanced `refs/remotes/origin/main` to the tip, do not write it again.
2. Advance local `refs/heads/main` only by an exact compare-and-swap whose old value is `1b077411...` and new value is `81dee2c...`.
3. If `refs/remotes/origin/main` still equals exact baseline after verified publication, advance it only by the same exact compare-and-swap form.
4. If either ref equals neither exact baseline nor exact tip, stop and return `PARTIAL`; do not overwrite it.
5. Do not use reset, checkout, switch, merge, rebase, branch-force, fetch, pull, symbolic-ref update, or general-purpose ref rewrite.
6. Do not move or create the topic branch; it must already point to the accepted tip.
7. Do not alter `origin/HEAD`; it must already be symbolic to `origin/main` and will resolve through the converged tracking ref.
8. No other local ref may move.

A public push that succeeded but local convergence that failed is `PARTIAL`, not `BLOCKED` and not `PASS`. Preserve exact public and local evidence for Orchestrator recovery.

### 10. Cleanup and final validation

After public-object verification and any authorized local-ref convergence:

1. delete only the exact validated owned temporary root using bounded depth-first deletion;
2. prove no matching `ap-publication-w09` root remains;
3. prove no clone, Git, suite, or publication process remains;
4. prove the source worktree/index/untracked/ignored state remains clean;
5. prove source topic branch and `HEAD` remain unchanged at the accepted tip;
6. prove local `main`, available `origin/main`, symbolic `origin/HEAD`, public `main`, public `HEAD`, and public ref inventory exactly match section 9;
7. prove exact commit/tree/parent/subject/topology evidence one final time locally;
8. prove no new local commit, tag, branch, stash, worktree, hook, config, remote, or non-authorized ref was created or changed;
9. prove the inert `.git/REBASE_HEAD`, if present at preflight, is byte-identical and still inert;
10. prove no external prompt/report artifact exists in AP;
11. do not touch Meta, FrameNest, any consumer, deployment, production, provider, release, PR, issue, account, or ledger.

If cleanup cannot be safely completed, return `PARTIAL` after preserving non-sensitive evidence. Do not broaden deletion scope.

### 11. Explicit prohibitions

You must not:

- edit, format, create, move, rename, delete, stage, or commit any AP file;
- amend, squash, merge, rebase, cherry-pick, reconstruct, or replace either accepted commit;
- fetch, pull, reset, restore, clean, stash, checkout, switch, create/delete a branch, create/delete a tag, or create another worktree;
- force-push, force-with-lease, retry a push, push another ref, follow tags, delete a ref, or change a remote;
- modify Git configuration, credential helpers, hooks, access controls, repository settings, default branch, branch protection, releases, PRs, issues, or GitHub metadata;
- inspect or expose secrets, credentials, helper payloads, environment values, SSH material, browser state, or private configuration;
- use IDE, GUI, browser automation, `cursor`, `code`, `xdg-open`, AppImage, or provider tools;
- read or mutate Meta or archive the prompt/report yourself;
- mutate FrameNest, any AP consumer pin, deployment, production, database, service, provider, or account;
- treat publication as deployment or production acceptance;
- claim the logical whole closed;
- continue after the terminal report without a new complete Orchestrator authority grant.

### 12. Failure classification and finite convergence

Use the first causal failure and stop. Do not repair or route around it.

Return `BLOCKED` before any public mutation when:

- repository identity, object, topology, branch, upstream, path, stat, protected surface, control state, hook, external-artifact, suite, or pre-push public gate fails;
- public baseline or inventory changed unexpectedly and the accepted tip is not already the exact public target;
- credentials or push capability are unavailable before a push attempt;
- a safe exact push cannot be made without extra authority;
- any required precondition would need fetch, cleanup, reset, force, config change, or content repair.

Return `PARTIAL` when:

- public `main` already equals the accepted tip before your push, so publication occurred externally and must be reconciled;
- the one push was attempted and remote mutation is possible, ambiguous, or externally visible but any required evidence is incomplete;
- the push exited non-zero, even if subsequent readback equals the tip;
- post-push public clone/readback, local canonical-ref convergence, or exact cleanup fails;
- an unexpected state appears after public mutation.

Return `PASS` only when the one exact push exits `0` and every direct, cloned-public, local-ref, cleanup, and final-state gate passes.

Do not open another audit, correction, or publication cycle. The Orchestrator will reconcile the terminal report once.

### 13. Required terminal report contract

Return one complete English report for `ORCHESTRATOR_CHAT`. Save or copy it externally as `09_report.md`; do not create that file inside AP or Meta.

Begin with exactly this header shape:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: external-ap-execution-trace-and-meta-history-architecture
Worker session ordinal: 09
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: publication-PASS | not-applicable
Result artifact or commit: 81dee2c182322ac95999e5d4ee42072b6040e44a | not-applicable
Result evidence: <bounded exact evidence or not-applicable>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | changed-external-state | new-material-risk
Authority expiry: publication authority expired at this terminal report
```

For `PASS`, use:

```text
Standard terminal status: PASS
Phase-qualified result: publication-PASS
Result artifact or commit: 81dee2c182322ac95999e5d4ee42072b6040e44a
Report justification: new-mutation
```

The report must then include:

1. **Publication verdict and route** — terminal status; fresh Worker 9 / exchange 01; no Plan Mode or delegation; authority expired.
2. **Accepted stack identity** — baseline, first candidate, corrected tip, parents, trees, subjects, counts, path boundaries, and topology.
3. **Preflight state** — physical repository, origin, branch/upstream, local refs, worktree/index/ignored state, control state, hooks, binaries, and external-artifact check.
4. **Pre-publication validation** — `sh -n` result and exact contained suite command, exit code, passed/failed totals, and post-suite cleanliness.
5. **Immediate public pre-push gate** — exact public `main`, public `HEAD`, complete heads/tags inventory, and time/order relative to the push without invented precision.
6. **Push evidence** — exact semantic command shape, exact refspec, one-attempt count, ordinary non-force classification, exit code, bounded non-sensitive result, and no extra ref.
7. **Direct public readback** — exact public main, HEAD symref, inventory, and absence of tags/additional heads.
8. **Independent public-clone evidence** — credential-free clone source, exact public commit/tree/parent/history/merge-base/path/stat/protected-surface evidence, and object connectivity.
9. **Local convergence** — final local main, origin/main, topic `HEAD`, origin/HEAD, exact compare-and-swap actions or no-op classification, and proof no other ref moved.
10. **Final repository and cleanup state** — clean status including ignored state, unchanged topic `HEAD`, inert marker disposition, exact temporary root class and cleanup, and no residual process.
11. **Authority boundary** — no other commit, push, ref, tag, release, PR, deployment, provider, consumer, FrameNest, Meta, production, or closure action.
12. **Deviations, risks, near-misses, and missing evidence** — truthful exact classification, including every non-zero exit or ambiguous observation.
13. **Smallest next step** — Orchestrator reconciliation and closure decision only; do not propose Worker continuation unless a concrete publication defect exists.

End with these compact fields:

```text
Published candidate: <exact SHA or not-published-by-this-worker>
Publication transition: <exact old main -> exact new main, or observed state>
Push result: <attempt count, exit, refspec, non-force classification>
Public readback: <main, HEAD, full heads/tags inventory>
Public object evidence: <tree, ordered stack, path/stat boundary, connectivity>
Tests and validation: <syntax and suite exits/totals>
Final local repository state: <HEAD, main, origin/main, origin/HEAD, clean state>
Temporary evidence state: <exact class and cleanup result>
Additional mutations: none | <exact truthful list>
Logical-whole closure: not-closed
Deviations, risks, or missing evidence: none | <exact bounded list>
Resolved Execution Issues / Near-Misses: none | <exact bounded list>
Pre-Existing Failure Classification: <exact prior history without re-adjudicating it>
```

For successful publication, the smallest next step must be:

```text
Orchestrator reconciliation and deterministic logical-whole closure; no further Worker action is authorized.
```

Never claim `closed`, `CLOSED: PASS`, deployment, production acceptance, or consumer adoption. Those are not Worker publication results.

### 14. Stop condition

Your authority expires at the first terminal `PASS`, `PARTIAL`, or `BLOCKED` report. Retained session context does not renew it.

After the report:

- do not push again;
- do not change local refs again;
- do not archive anything;
- do not close the logical whole;
- do not update AP consumers;
- do not begin another task;
- wait for a new complete Orchestrator prompt.


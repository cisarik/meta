# Fresh independent Acceptance Worker — AP ChatOrchestrator offline bundle transport

You are a genuinely fresh, independent Acceptance/Audit Worker.

Logical whole:

`chat-orchestrator-offline-bundle-transport`

Your job is to independently assess the current **uncommitted AP implementation candidate**.

Do not implement fixes.
Do not edit the candidate.
Do not commit.
Do not push.
Do not update consumer `.ap` pins.
Do not mutate Meta.

You have normal Git/GitHub access.

## Candidate baseline

Expected canonical AP repository:

```text
/home/agile/Projects/ap
https://github.com/cisarik/ap.git
```

Expected product HEAD before candidate edits:

```text
717ecb6cfb7c71eda12ff4e3e0b02f28101c59bf
```

The implementation candidate is intentionally an uncommitted dirty worktree on top of that commit.

Independently verify all of this before relying on it.

The Implementation Worker reported:

- 13 modified tracked files;
- one new ADR;
- roughly +1383 / -43 lines overall;
- `ap` alone grew by approximately 1165 lines;
- no commit or push;
- 55 disposable smoke assertions reported PASS.

Do not accept those claims merely because they appear in the report.

## Governing design

The intended feature is narrowly scoped:

- normal Orchestrators, Planners, Workers, Acceptance Workers and publication actors continue using ordinary Git/GitHub;
- only the read-only `ChatOrchestrator` receives the offline continuity mechanism;
- bundle evidence proves exact committed Git state but does not prove current public GitHub state;
- required limitation when no public observation exists:

```text
public branch state not directly observed
```

Primary Cooperator UX:

```sh
~/Projects/ap/ap bundle framenest --initial \
  --companion-trace /home/agile/meta
```

then later:

```sh
~/Projects/ap/ap bundle framenest
```

The generated ZIP is manually attached to ChatOrchestrator.

No GitHub connectivity should be required on the ChatOrchestrator side.

## Independence requirement

Do not reuse the Implementation Worker's test harness or conclusions as your acceptance evidence.

You may read the implementation report for orientation, but independently:

- inspect the entire diff;
- inspect the resulting documentation semantics;
- devise your own adversarial cases;
- run your own disposable fixtures.

Do not mutate the real candidate to make a test pass.

Because the real AP candidate is dirty and the new command reportedly requires the exporter AP checkout to be clean and match `HEAD:ap`, create a **disposable acceptance copy/repository** when a committed clean exporter state is required for realistic execution testing.

Do not commit inside `/home/agile/Projects/ap`.

A temporary commit inside an isolated disposable acceptance repository is allowed solely for testing.

---

## A. First verify protocol/report identity

There is a possible handoff defect that must be resolved against live AP semantics.

The Planner report used:

```text
Worker session ordinal: 01
Worker exchange ordinal: 01
```

The Implementation report also reports:

```text
Worker session ordinal: 01
Worker exchange ordinal: 01
```

despite being a genuinely fresh Implementation Worker after the Planner.

Determine from current AP whether these coordinates are supposed to uniquely advance across Worker sessions/exchanges for this logical whole.

If they should have advanced, classify this explicitly:

- documentation/report-coordinate defect only;
- acceptance-blocking provenance defect;
- or another category justified from AP.

Do not silently normalize it.

Your own Acceptance Worker must use correct fresh coordinates.

---

## B. Review the semantic fix

Inspect `AP.md` as the sole live semantic owner and verify that projections agree.

Confirm that the candidate really distinguishes:

```text
exact committed bundle evidence
```

from:

```text
independently observed current public branch evidence
```

Verify that bundle evidence is not allowed to prove:

- current GitHub branch tip;
- push success;
- publication equality;
- remote synchronization;
- absence of newer public commits.

Verify that the former DNS/GitHub failure mode is actually fixed:

A ChatOrchestrator with valid bundle evidence must be able to perform ordinary next-Worker routing when the decision does not require public state.

At the same time, real publication/public-ref gates must remain intact.

Specifically audit:

- RF-19;
- source-of-truth/evidence section;
- ChatOrchestrator inspection clone semantics;
- public verification section;
- restoration;
- Continuation Bootstrap;
- AP_ORCHESTRATOR;
- PROMPT_CONTRACTS;
- glossary/FAQ projections.

Look for contradictory sentences left behind.

---

## C. Review delivery-route correction

Verify that the candidate cleanly separates:

- access profile;
- GitHub capability;
- dispatch capability;
- native planning mode;
- Worker freshness;
- independence;
- delivery route.

Required behavior:

- ChatOrchestrator → manual Cooperator ferry normally;
- full Orchestrator with authorized working dispatch → direct complete-prompt dispatch normally, including first Planner;
- unavailable/opted-out dispatch → manual fallback;
- true independent/external fresh-session requirement → manual/external routing as required;
- first Planner native planning mode remains required.

Historical ADR-0022/0023 bodies must remain historical.

Verify the new ADR records prospective supersession rather than rewriting history.

---

## D. Audit `ap bundle` implementation deeply

The code increase in `ap` is large.

Do not merely execute happy paths.

Read the implementation line-by-line around the new command and helpers.

Pay special attention to:

- shell quoting;
- argument parsing;
- physical path resolution;
- symlinks;
- filenames containing spaces;
- leading `-`;
- newline-containing paths where relevant;
- traversal;
- `mktemp`;
- traps;
- cleanup;
- nested failures;
- signal interruption;
- ambient `GIT_DIR`;
- ambient `GIT_WORK_TREE`;
- unexpected environment variables;
- command substitution;
- word splitting;
- globbing;
- manifest escaping;
- checksum parsing;
- branch names;
- detached HEAD;
- strange remote URLs.

Check POSIX `/bin/sh` compatibility.

If available, use an appropriate static shell checker as supplementary evidence, but do not make acceptance depend solely on it.

---

## E. Verify zero-network export

This is a hard requirement.

`ap bundle` itself must not need:

- `fetch`;
- `pull`;
- `ls-remote`;
- network clone;
- GitHub API;
- submodule network update.

Inspect source code and dynamically test with deliberately broken network/proxy configuration.

Normal GitHub behavior in other AP commands must remain unchanged.

Do not mistake configured remote URLs for public verification.

---

## F. Verify package contents

Inspect a generated initial ZIP directly.

Confirm that it contains the expected bounded payload, such as:

```text
manifest.conf
IMPORT.md
checksums
project.bundle
ap.bundle
optional companion/submodule bundles
```

Verify:

- no working-tree filesystem copy;
- ignored `.env` does not enter;
- `.venv`, caches, build directories etc. do not enter merely because present locally;
- payload checksums survive ZIP creation/extraction;
- outer ZIP generation does not depend on `zip(1)`;
- temporary packaging Git objects do not contaminate source repositories.

Also assess ZIP extraction safety guidance.

A ChatOrchestrator should not be instructed to blindly extract a potentially malformed archive over an existing repository or arbitrary path.

---

## G. Git bundle correctness

Independently test actual Git semantics.

### Initial

Verify exact reconstruction of:

- project HEAD;
- `.ap` gitlink;
- `.ap HEAD`;
- companion trace when configured;
- included submodule when configured.

No synthesized replacement commits are acceptable.

### Incremental

Let:

```text
A = initial
B = update 1
C = update 2
```

Verify that:

```text
initial A + newest A..C update
```

is sufficient without B.

Test this with real Git bundles and reconstructed repositories.

Test missing prerequisites.

Expected recovery:

```text
request a fresh --initial
```

not GitHub access.

Test non-ancestor history rewrite.

It must fail closed.

---

## H. Specifically verify the two Git corrections

### Raw gitlink problem

Implementation must not rely on:

```sh
git bundle create file.bundle <raw-unreferenced-sha>
```

for `.ap` or another submodule.

Verify source uses an advertised revision such as checked `HEAD`, after proving:

```text
checkout HEAD == required gitlink
```

### `git bundle verify`

Verify generated `IMPORT.md` gives commands that actually work on supported Git behavior.

For incremental verification, repository context with prerequisite objects must be used.

Do not accept documentation containing a command sequence that only worked accidentally on one Git version.

---

## I. Companion trace

Test a project whose product HEAD does not change but whose configured analytic trace does.

`ap bundle <project>` should still produce a useful update.

Verify:

- explicit initial opt-in only;
- no hardcoded Meta;
- no sibling scanning;
- no private repo auto-inclusion;
- exact companion origin/commit recorded;
- cumulative companion transport;
- companion public state not falsely claimed.

---

## J. Other submodules

Test:

1. unexpected additional submodule → fail closed;
2. explicit `--include-submodule` with exact local gitlink → success;
3. missing local gitlink commit → fail;
4. implementation never silently fetches missing content.

Do not accept a package described as complete while required gitlink content is absent.

---

## K. Secret/history safety

Independently test:

- ignored `.env`;
- tracked current `.env`;
- `.env` committed historically and later deleted;
- suspicious private-key filename;
- explicitly allowed exact path;
- similar innocent path that should not accidentally match;
- path with spaces.

Confirm that filename scanning is documented only as a conservative guard and never as proof of secret absence.

No Git objects may be silently removed to sanitize history.

Assess whether the `--allow-path` mechanism is scoped narrowly enough.

---

## L. Chain-state correctness

Inspect:

```text
${XDG_STATE_HOME:-$HOME/.local/state}/ap/bundle/<project>/chain.conf
```

The implementation intentionally diverged from the Planner's `<owner>--<repo>` naming.

Stress-test the project-name keyed design.

At minimum test:

- same CLI project name pointing at a different root;
- same project name with a different origin;
- moved checkout;
- deleted/recreated checkout;
- `--replace-chain`;
- stale state;
- two unrelated repositories sharing the same basename.

Determine whether origin/root verification makes the simplified key safe enough or whether this is an acceptance blocker.

Do not reject merely because it differs from planning; reject only for a concrete correctness/safety problem.

---

## M. Initial-reset UX

Test the expected long-break recovery:

```sh
ap bundle framenest --initial --replace-chain
```

It must cleanly establish a new chain without requiring old incremental files.

Check that replacement is explicit and that a typo cannot silently destroy useful state.

---

## N. Existing AP commands regression

Independently exercise the existing surfaces sufficiently to detect helper-split regressions:

```text
init
doctor
project
exec
update
```

Do not perform an unauthorized mutation/push.

`update --check` may use GitHub normally because `update` is not the new offline command.

The acceptance question is whether the new helper split accidentally changed existing behavior.

---

## O. Documentation drift

Search all live AP projections for stale claims such as:

- every first Planner is manually delivered;
- inspection clone necessarily means public/published clone;
- every ChatOrchestrator report reconciliation requires current public commit;
- public verification is always mandatory before continuation;
- bundle SHA equals public HEAD;
- emoji implies PASS.

If contradictory live projection text remains, classify severity.

Historical ADR text is not drift.

---

## P. Scope control

Confirm these remain untouched unless a justified discrepancy exists:

```text
AP_WORKER.md
ARTIFACT_LIFECYCLE.md
INFOSEC.md
ap.project.conf
historical ADR bodies
consumer repositories
consumer .ap pins
```

No consumer adoption belongs in this acceptance.

---

## Q. Acceptance decision

Return exactly one overall result:

```text
ACCEPTANCE-PASS
```

or:

```text
ACCEPTANCE-BLOCKED
```

Do not use PASS if any material correctness, security, continuity, or protocol contradiction remains.

Minor non-blocking observations may be recorded separately.

Do not fix blockers.

If blocked, give the smallest bounded correction scope suitable for a fresh Correction Worker.

---

## Terminal report

Return one complete terminal report beginning exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Include:

- logical whole;
- your correct fresh Worker session/exchange coordinates;
- baseline HEAD;
- candidate worktree identity;
- independence statement;
- files inspected;
- protocol/report-coordinate finding;
- semantic-evidence finding;
- delivery-route finding;
- CLI/code audit finding;
- network-independence finding;
- initial reconstruction result;
- cumulative incremental result;
- skipped-intermediate result;
- `.ap` result;
- companion result;
- other-submodule result;
- secret/history result;
- chain-state collision/staleness result;
- import-instruction result;
- existing-command regression result;
- documentation-drift result;
- security findings;
- exact commands/scenarios sufficient to reproduce material findings;
- overall `ACCEPTANCE-PASS` or `ACCEPTANCE-BLOCKED`;
- if blocked, smallest recommended Correction Worker scope;
- confirmation that you did not mutate/commit/push the candidate.

Do not implement corrections.

Stop after the terminal acceptance report.
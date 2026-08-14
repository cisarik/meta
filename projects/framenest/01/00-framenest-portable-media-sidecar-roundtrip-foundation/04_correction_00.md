# FrameNest Portable Media Sidecar — Bounded Documentation Status Correction

## Canonical exchange coordinates

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Bounded Documentation Correction Worker
Worker phase: correction
Native planning mode: not-used
Maximum plan-only cycles: 0
Reasoning recommendation: medium
Evidence posture: non-independent-repair
Independence: fresh-session, correction-role
Authority renewal: not-applicable
```

Do not enter Native Plan Mode. Execute the bounded correction directly.

## Acceptance failure being repaired

Fresh Worker 3 independently rejected exact candidate:

```text
87032d3826daaa217769acccc0eb37f1c1ffb1de
```

with:

```text
acceptance-FAIL
publication-not-performed
publication-not-eligible
```

All inspected sidecar code, filesystem safety, catalog authority, compare behavior, CLI behavior and 77 focused tests passed.

The material failure is documentation-only:

1. `README.md` introduces the implemented portable media sidecar v1 and CLI but later still says FrameNest has no sidecar schema.
2. ADR-0059 still presents filesystem I/O, application projection and CLI as future slices and describes the current implementation boundary as codec-only.

This prompt authorizes only the smallest correction of those two live status contradictions.

It does not reopen the codec, application, filesystem, CLI, schema or product design.

## Authority

```text
Documentation correction authority: exact two-path boundary below
Implementation authority outside those documents: none
Test-source mutation authority: none
Code mutation authority: none
Dependency/migration authority: none
Commit authority: one local correction commit
Publication authority: none
Push authority: none
Deployment authority: none
Acceptance authority: none
Logical-whole closure authority: none
```

Do not repair unrelated documentation or perform general prose cleanup.

## Exact repair baseline

```text
commit:  87032d3826daaa217769acccc0eb37f1c1ffb1de
tree:    881a93734cac120bff048c42ff432cd38755443a
parent:  633fa3b3884bc865dba26643034ef0c2fc12f394
subject: feat: add portable media sidecar CLI
```

Required ancestry:

```text
87032d3826daaa217769acccc0eb37f1c1ffb1de
└── 633fa3b3884bc865dba26643034ef0c2fc12f394
    └── 96bf7df2001c38284d9aa136b56d0109f24700d5
        └── a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Public baseline must remain:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Required AP pin:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

## Authorized isolated correction checkout

Read-only candidate source:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01
```

Fresh correction target:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w4-e01
```

Before creation, verify:

* candidate source exists;
* origin is public FrameNest;
* source HEAD/tree/subject match exact candidate;
* source is clean;
* no active Git operation;
* fresh correction target is absent;
* credential-free public `main` remains `a23b4bc…`;
* candidate remains absent from public refs.

Do not switch, clean, reset, stash, fetch into or mutate the candidate source.

If every precondition passes, create exactly one isolated correction clone:

1. Clone public FrameNest with `--no-checkout` into the absent correction target.
2. Fetch/transfer the unpublished candidate objects read-only from the candidate source.
3. Check out exact `87032d3…` detached.
4. Initialize only `.ap`.
5. Verify the full candidate gate.
6. Create one local branch:

```text
fix/portable-media-sidecar-documentation-convergence
```

This clone creation and branch are authorized. No other host or repository mutation is authorized.

If the target exists or a mandatory gate fails, stop `BLOCKED`; do not delete or reuse it.

## Mandatory candidate gate

Before editing:

* verify exact path and public origin;
* verify candidate commit/tree/parent/subject;
* verify exact ancestry;
* verify cumulative 18-path candidate diff;
* verify `.ap` gitlink and submodule;
* verify clean index/worktree/untracked state;
* verify no active Git operation;
* read ADR-0059 and all sidecar passages in candidate `README.md`;
* read applicable repository instructions and `docs/WORKER_EXECUTION_CONTRACT.md`;
* run the committed 77-test focused sidecar stack through the canonical exact-source envelope.

Any candidate mismatch or focused-test failure blocks mutation.

## Canonical execution envelope

Use:

```text
/home/agile/Projects/framenest/.venv/bin/python
```

through a sanitized environment equivalent to:

```text
env -i \
  PATH=/usr/bin:/bin \
  LC_ALL=C \
  LANG=C \
  PYTHONNOUSERSITE=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=<correction-clone>/src
```

Do not create, repair, synchronize or install a virtual environment.

Use pytest temporary state outside the repository and disable repository-local cache creation.

## Exact changed-path boundary

Modify exactly:

```text
README.md
docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
```

Do not change any other path.

Specifically prohibited:

```text
src/**
tests/**
pyproject.toml
poetry.lock
PRODUCT.md
SPEC.md
ROADMAP.md
SECURITY.md
docs/adr/README.md
.ap
```

Do not add `framenest.adapters.cli.sidecar` to `CLI_MODULES`. Independent acceptance explicitly passed that gate and classified the tuple as curated rather than exhaustive.

## Required README correction

The candidate currently retains this obsolete live denial in the catalog-foundation paragraph:

```text
candidates, premium gallery data, sidecar, user, or authentication schema.
```

Remove only the obsolete `sidecar` denial so the list truthfully remains:

```text
candidates, premium gallery data, user, or authentication schema.
```

Preserve the surrounding catalog-foundation meaning and the dedicated portable-sidecar CLI section.

Do not claim:

* sidecar import or rebuild;
* Save-coupled writes;
* automatic fan-out;
* synchronization or drift repair;
* deployment or production availability.

## Required ADR-0059 correction

Preserve ADR-0059’s accepted architectural decision, v1 schema, authority model, exclusions and residual risks.

Update only implementation-status language that has become stale.

Remove or revise present-tense statements equivalent to:

```text
Filesystem I/O, catalog projection, and CLI binding remain later implementation slices.
```

and:

```text
The current implementation boundary is only this ADR, the domain codec, and unit tests.
```

The corrected status must truthfully say that the current candidate stack now includes:

* ADR-0059;
* deterministic domain codec;
* application catalog projection and compare orchestration;
* infrastructure-independent storage port;
* secure local filesystem store;
* thin `framenest-sidecar` CLI;
* focused domain, application, filesystem, contract and integration tests.

It must also preserve that the following remain excluded and unimplemented:

* sidecar-to-catalog import;
* catalog rebuild;
* metadata Save coupling;
* automatic drift repair;
* multi-location fan-out;
* cross-device synchronization;
* HTTP/browser surface;
* deployment;
* complete Windows replace/case-folding evidence.

Do not rewrite historical decision rationale as though all layers existed when ADR-0059 was initially introduced. Distinguish accepted design from current implementation status.

Do not add commit hashes or publication claims to the ADR.

## Validation

After editing:

1. Inspect the exact two-path diff manually.
2. Prove the README no longer simultaneously asserts and denies sidecar existence.
3. Search both changed files for stale present-tense phrases:

```text
no sidecar
sidecar schema
later implementation slices
codec-only
only this ADR
remain unimplemented
```

Interpret results semantically; do not perform blind string deletion.

4. Confirm the documents still deny import/rebuild, Save coupling, repair, fan-out, synchronization and deployment.
5. Run the same focused 77-test sidecar stack.
6. Run `git diff --check`.
7. Prove no path outside the exact two-path boundary changed.
8. Prove `.ap`, code, tests, dependencies and migrations are unchanged.
9. Confirm public `main` remains `a23b4bc…` and the repair branch remains unpublished.

Do not rerun the complete repository pytest suite. Fresh acceptance already classified its isolated-clone console-script failures, and this correction changes documentation only. Full re-acceptance belongs to the next fresh Worker.

## Commit boundary

Create exactly one local commit on top of:

```text
87032d3826daaa217769acccc0eb37f1c1ffb1de
```

Required subject:

```text
docs: reconcile sidecar implementation status
```

Do not amend, rebase, merge, squash, tag or push.

At completion prove:

* new commit SHA and tree;
* parent exactly `87032d3…`;
* exact subject;
* exact two changed paths;
* cumulative four-commit fast-forward ancestry to public baseline;
* clean tracked/index/untracked state;
* no active Git operation;
* no public repair branch;
* public `main` unchanged.

## Prohibited actions

Do not:

* modify code or tests;
* change sidecar semantics;
* add new product scope;
* repair CLI hygiene;
* edit other documents;
* create migrations or dependencies;
* publish or push;
* deploy;
* access NUC, SSH, sudo, providers, browser or private media;
* mutate Meta or AP;
* close the logical whole;
* issue the re-acceptance prompt.

## Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 04
Worker exchange ordinal: 01
```

On success:

```text
Standard terminal status: PASS
Phase-qualified result: correction-PASS
Result artifact or commit: <new-local-commit>
Logical-whole closure: not-closed
Report justification: new-mutation
```

Otherwise return truthful `BLOCKED` or `FAIL`.

Include:

* fresh-session and authority confirmation;
* isolated-clone creation and repository gates;
* exact acceptance failure repaired;
* README before/after semantic disposition;
* ADR-0059 status correction;
* proof accepted design and exclusions were preserved;
* exact changed paths;
* validation commands, exits and test counts;
* commit/tree/parent/subject;
* public-main and unpublished-branch readback;
* deviations and residual risks;
* Resolved Execution Issues / Near-Misses;
* Pre-Existing Failure Classification;
* smallest next step;
* final cleanliness;
* authority expiry.

The smallest next step after correction-PASS is a fresh full re-acceptance Worker. Do not publish.

All Worker 4 authority expires permanently at the terminal report.

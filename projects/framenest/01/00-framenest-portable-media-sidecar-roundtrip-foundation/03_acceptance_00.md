# FrameNest Portable Media Sidecar — Fresh Independent Acceptance

## Canonical exchange coordinates

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Acceptance Worker
Worker phase: acceptance
Native planning mode: not-used
Maximum plan-only cycles: 0
Reasoning recommendation: high
Evidence posture: independent
Independence: fresh
Authority renewal: not-applicable
```

Do not enter Native Plan Mode. Do not produce a plan for approval.

Execute the bounded acceptance directly.

## Role and authority

You are a fresh independent acceptance Worker.

You did not plan or implement this candidate. Archived prompts and implementation reports are claims to verify, not proof.

Authority:

```text
Implementation authority: none
Repair authority: none
Repository-source mutation authority: none
Commit authority: none
Publication authority: none
Push authority: none
Deployment authority: none
Logical-whole closure authority: none
```

Your only decision is whether the exact immutable candidate below deserves:

```text
acceptance-PASS
```

or a truthful `acceptance-FAIL` / `BLOCKED`.

Do not repair, amend, reformat, commit, push, publish, deploy or close the logical whole.

## Candidate under acceptance

Exact candidate:

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

Intermediate objects:

```text
633fa3b3884bc865dba26643034ef0c2fc12f394
tree ab04ff1b4448745625ceb97b5b904ed84746f0de
parent 96bf7df2001c38284d9aa136b56d0109f24700d5
subject feat: add portable media sidecar storage
```

```text
96bf7df2001c38284d9aa136b56d0109f24700d5
tree 6febf4e683adb61024757e89dce7725a3e890a64
parent a23b4bc786357da3591a4f75087b7e8a3d50d341
subject feat: add portable media sidecar codec
```

Public baseline:

```text
commit:  a23b4bc786357da3591a4f75087b7e8a3d50d341
tree:    a1ea29c5fa7e6878670b243ef34b8b0b31084829
parent:  4add009e1f89fcc05b9e8bc306d6ecc8e568547b
subject: fix: reconcile selected Mullvad status
```

Required AP gitlink and submodule HEAD:

```text
041de310ea33ed1b47dd8f5fbfcc2829d1a32514
```

The candidate is intentionally unpublished.

## Authorized independent acceptance checkout

Implementation source clone, read-only:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w2-e01
```

Fresh acceptance target:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w3-e01
```

Before creating anything, verify:

1. The implementation source clone exists.
2. Its origin is `https://github.com/cisarik/framenest.git`.
3. Its branch is `feat/portable-media-sidecar-roundtrip-foundation`.
4. Its HEAD, tree and cleanliness match the exact candidate.
5. No Git operation is active there.
6. The fresh acceptance target is absent.
7. Credential-free public `main` is exactly `a23b4bc…`.

Do not switch, clean, stash, reset, fetch into or otherwise mutate the implementation source clone.

If all preconditions pass, you are authorized to create exactly one independent acceptance clone:

1. Clone public FrameNest into the absent acceptance target using `--no-checkout`.
2. Transfer/fetch the existing unpublished feature branch objects read-only from the implementation source clone.
3. Check out exact candidate `87032d3…` detached.
4. Initialize only the pinned `.ap` submodule.
5. Keep `origin` pointing to public GitHub.

This isolated-clone creation is authorized acceptance setup. It does not grant candidate mutation authority.

Do not create a branch. Do not push any ref.

If the target already exists or any source invariant fails, stop `BLOCKED`. Do not delete, reuse, clean or repair it.

## Post-creation repository gate

In the fresh acceptance clone, prove:

* exact physical path;
* origin is public FrameNest;
* detached HEAD;
* exact candidate commit/tree/parent/subject;
* exact three-commit ancestry to public baseline;
* public `main` remains `a23b4bc…`;
* `.ap` gitlink and submodule HEAD are `041de310…`;
* index and tracked/untracked worktree are clean;
* no active Git operation;
* candidate has no public feature ref;
* no unexpected merge commit or rewritten ancestry.

The cumulative diff from public baseline must contain exactly these 18 paths:

```text
M README.md
M PRODUCT.md
M ROADMAP.md
M SECURITY.md
M SPEC.md
A docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
M docs/adr/README.md
M pyproject.toml
A src/framenest/adapters/cli/sidecar.py
A src/framenest/application/media_sidecar.py
A src/framenest/application/ports/media_sidecar_store.py
A src/framenest/domain/media_sidecar.py
A src/framenest/infrastructure/filesystem/media_sidecar.py
A tests/contract/test_sidecar_cli.py
A tests/integration/test_media_sidecar_roundtrip.py
A tests/unit/application/test_media_sidecar.py
A tests/unit/domain/test_media_sidecar.py
A tests/unit/infrastructure/filesystem/test_media_sidecar_store.py
```

Verify the three per-commit diffs separately. Do not accept a cumulative path list alone.

## Canonical exact-source execution

Use only:

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
  PYTHONPATH=<acceptance-clone>/src
```

Prove the imported `framenest` package and all sidecar modules resolve from the fresh acceptance clone.

Do not create, repair, replace, synchronize or install into any virtual environment. Do not run dependency installation, lock regeneration, `poetry env use`, `uv sync`, `uv lock`, GUI, Cursor, AppImage or browser commands.

All fixtures must live outside the repository through pytest temporary paths or an explicit disposable temporary directory.

## Acceptance question

Independently determine whether the exact candidate truthfully delivers:

> A deterministic, strictly versioned portable media-sidecar v1 projection; safe explicit export, validation and catalog comparison for one selected media location; and a thin machine-readable operator CLI—without making sidecars live catalog authority or implementing import, rebuild, Save coupling, fan-out, HTTP or deployment.

Every gate below is required.

## Gate 1 — Domain codec and schema

Inspect the implementation, ADR and tests directly.

Verify:

* format is exactly `framenest-media-sidecar`;
* schema version is integer `1`;
* closed root and nested objects;
* every v1 key is emitted;
* optionals use `null` and collections use arrays;
* duplicate keys are rejected at every relevant level;
* invalid UTF-8, BOM, extra fields and oversize input fail;
* unsupported format/version remains distinct from malformed input;
* no `sidecar_written_at_ms`;
* encoding is deterministic and byte-identical for unchanged state;
* UTF-8, canonical separators, stable key ordering and one trailing LF;
* decoded values use existing domain constraints rather than weaker duplicates;
* errors are sanitized and do not leak payload fragments or paths.

Challenge representative positive and negative fixtures independently. Do not rely only on the implementation Worker’s counts.

## Gate 2 — Catalog projection and authority

Verify the application service:

* resolves explicit `media_id` and `location_id`;
* rejects missing or mismatched identity;
* requires an available selected location and existing library;
* uses metadata snapshot timestamps, not logical-media timestamps;
* preserves tag-key order and corresponding display definitions;
* projects classification, genres, creator attribution and Processed state correctly;
* reports inconsistent catalog state rather than fabricating values;
* never calls repository write methods;
* never imports sidecar values into the catalog;
* never writes sidecars from ordinary metadata Save;
* does not infer or fan out locations.

Use call-spy or existing negative tests where appropriate.

## Gate 3 — Filesystem safety and durability

Inspect the implementation rather than inferring safety from test names.

Verify:

* placement is `{complete-media-filename}.framenest.json`;
* root, parents and source media satisfy the strict non-symlink gates;
* containment and native path flavor are enforced;
* sidecar inode type is classified before parsing;
* symlinks and non-regular targets are never followed or replaced;
* reads are bounded to 256 KiB;
* foreign identity, malformed and unsupported existing files are preserved;
* same-identity equal bytes return `unchanged` without replace, chmod, inode or mtime mutation;
* valid same-identity differing bytes are replaced;
* creation/replacement uses a unique same-directory owned temp;
* temp creation is exclusive and non-following;
* write, fsync, validation, mode `0644`, replace, directory fsync and exact readback occur in a defensible order;
* failures before replacement preserve the prior target;
* cleanup cannot remove unrelated files;
* no SQLite write occurs.

Adversarially review the reported residual race between closing the temp descriptor and path-based operations. Decide whether it is acceptable under the documented trusted local-library threat boundary or creates a material false-success/destructive-write path.

Do not silently waive this risk.

## Gate 4 — Compare semantics

Independently prove exact precedence:

1. absent entry → `missing`;
2. non-regular entry → error;
3. unreadable or oversize regular file → error;
4. malformed or unsupported → corresponding error;
5. foreign requested identity → identity-conflict error;
6. equal payload → `match`;
7. differing payload with older sidecar revision → `stale`;
8. differing payload with equal/newer revision → `mismatch`.

Verify:

* payload equality excludes only `created_at_ms` and `updated_at_ms`;
* equal payload wins over misleading timestamps;
* `null` is older than an integer;
* two nulls compare as equal;
* `library_id` and `relative_path` are payload fields, not foreign-identity keys;
* compare is read-only and performs no repair.

## Gate 5 — Thin CLI and machine contract

Verify exact commands:

```text
framenest-sidecar export --media-id <UUID> --location-id <UUID>
framenest-sidecar validate --path <PATH>
framenest-sidecar compare --media-id <UUID> --location-id <UUID>
```

Confirm:

* `pyproject.toml` points exactly to `framenest.adapters.cli.sidecar:main`;
* no dependency or lockfile change;
* no projection, codec, comparison or filesystem logic is duplicated in the CLI;
* export and compare use the existing settings, migration gate, engine and repositories;
* engine disposal occurs on success and failure;
* validate does not load settings, inspect migrations, create an engine or instantiate SQLite repositories;
* validate does not print decoded contents;
* malformed identities are rejected before catalog composition;
* command execution is non-interactive;
* success writes one JSON line to stdout, nothing to stderr, exit `0`;
* errors write one JSON line to stderr, nothing to stdout, exit `1`;
* all export, validate and compare result/code pairs are exact;
* compare `missing` is exit `0`;
* parser and command-shape failures use `SIDECAR_INVALID_INPUT`;
* not-at-head catalog uses `SIDECAR_CATALOG_NOT_READY`;
* existing structured sidecar error codes are preserved;
* unexpected failures use only sanitized `SIDECAR_COMMAND_FAILED`;
* no traceback, absolute path, database path, root or payload fragment escapes;
* `--help` human argparse output and `SystemExit(0)` are intentional and consistent with existing CLI behavior.

Run the module from an unrelated working directory with exact-source `PYTHONPATH`.

## Gate 6 — Operator CLI hygiene ownership

The implementation report explicitly says the new module was not added to:

```text
tests/contract/test_operator_cli_hygiene.py::CLI_MODULES
```

Inspect that test and the new CLI contract independently.

Determine whether omission of:

```text
framenest.adapters.cli.sidecar
```

from the central tuple leaves a material untested invariant.

At minimum prove directly that importing the sidecar CLI:

* does not load settings;
* does not inspect the caller working directory;
* does not touch an explicitly configured missing environment file;
* emits no stdout or stderr;
* succeeds from an unrelated working directory.

Disposition rules:

* If the central list is semantically intended to own exhaustive import hygiene and the candidate leaves the new CLI outside that owner without equivalent durable coverage, return `acceptance-FAIL`.
* If the new contract test provides equivalent durable coverage and the central tuple is demonstrably curated rather than exhaustive, acceptance may still pass, but the report must identify exact supporting tests and explain why no invariant is orphaned.
* Do not treat “the implementation prompt did not list that path” as evidence either way.

Do not edit the tuple.

## Gate 7 — Documentation truth

Read the candidate versions of:

```text
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SECURITY.md
docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
docs/adr/README.md
```

Search all live documentation for sidecar claims and distinguish current normative truth from historical ADR context.

Verify the documentation says only:

* deterministic explicit v1 projection exists;
* export, validate and compare exist;
* selected location is explicit;
* SQLite remains authoritative during normal operation;
* sidecars do not overwrite the catalog;
* no import/rebuild, Save coupling, repair, fan-out or synchronization exists;
* no secrets, absolute library roots, device identity or requester-private data are included;
* Windows replace/case-folding evidence is incomplete;
* no deployment or production claim is made.

Reject materially contradictory live claims such as simultaneously saying the sidecar v1 schema is unresolved or all durable metadata round-trip/rebuild work is complete.

Historical older ADR exclusions do not require broad rewriting unless candidate documentation incorrectly presents them as current truth.

## Gate 8 — Automated validation

Run at least:

### Focused sidecar stack

```text
tests/unit/domain/test_media_sidecar.py
tests/unit/application/test_media_sidecar.py
tests/unit/infrastructure/filesystem/test_media_sidecar_store.py
tests/contract/test_sidecar_cli.py
tests/integration/test_media_sidecar_roundtrip.py
```

Implementation evidence claims 77 passing tests. Verify independently.

### Related operator and migration gates

```text
tests/contract/test_operator_cli_hygiene.py
tests/contract/test_library_cli.py
tests/integration/test_persistence_migrations.py
```

Implementation evidence claims 15 operator/library and 9 migration tests. Verify independently.

### Broader regression

Run the complete repository Python pytest suite at the exact candidate unless an explicit repository instruction defines a narrower canonical full-suite command.

Any non-zero exit prevents `acceptance-PASS`.

Do not suppress, deselect or rewrite failures. Classify every failure as:

* candidate defect;
* pre-existing public-baseline failure;
* acceptance harness/environment failure.

A claimed pre-existing failure requires reproduction at the exact public baseline without mutating either checkout. If that cannot be proven, do not issue PASS.

Also run:

* exact-source provenance checks;
* `compileall -q` for candidate source;
* `git diff --check` over the complete candidate range;
* targeted documentation contradiction searches;
* final Git cleanliness and object-identity gates.

Do not create repository-local evidence scripts or files.

## Gate 9 — Publication readiness

If and only if every acceptance gate passes, verify that a later publication Worker could perform one ordinary non-force fast-forward publication:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
→ 87032d3826daaa217769acccc0eb37f1c1ffb1de
```

Acceptance does not authorize that push.

Confirm:

* public `main` has not moved;
* ancestry is fast-forward;
* the candidate remains unpublished;
* no tag or alternate public branch contains it;
* no deployment is required by this logical whole.

## Prohibited actions

Do not:

* change any tracked or untracked candidate content;
* add or edit tests;
* repair the candidate;
* commit, amend, merge, rebase, squash or tag;
* push or publish;
* create a PR;
* deploy to the NUC;
* use SSH, sudo, provider APIs or private media;
* mutate Meta or AP;
* modify the owner checkout;
* create or repair a `.venv`;
* invoke GUI, Cursor, AppImage or browser tooling;
* close the logical whole;
* issue the publication prompt.

If a defect is found, preserve the candidate unchanged and report the smallest repair boundary.

## Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 03
Worker exchange ordinal: 01
```

On complete independent success:

```text
Standard terminal status: PASS
Phase-qualified result: acceptance-PASS
Result artifact or commit: 87032d3826daaa217769acccc0eb37f1c1ffb1de
Logical-whole closure: not-closed
Report justification: independent-verification
```

Also state:

```text
Acceptance disposition: acceptance-PASS
Publication disposition: not-performed
Publication eligibility: eligible-for-separate-publication
```

On any material candidate defect:

```text
Standard terminal status: FAIL
Phase-qualified result: acceptance-FAIL
```

On an evidence or environment blocker:

```text
Standard terminal status: BLOCKED
Phase-qualified result: acceptance-BLOCKED
```

The report must include:

* fresh-session and authority confirmation;
* isolated-checkout creation and exact Git gates;
* candidate/tree/ancestry/cumulative and per-commit diff evidence;
* exact-source provenance;
* independent codec/schema findings;
* projection and no-catalog-write findings;
* filesystem safety and residual-race disposition;
* compare matrix;
* CLI JSON/exit findings;
* central CLI hygiene ownership disposition;
* documentation contradiction review;
* every command, exit status and test count;
* broader-suite result;
* publication-readiness result without publication;
* deviations and residual risks;
* Resolved Execution Issues / Near-Misses;
* Pre-Existing Failure Classification;
* exact smallest next step;
* final candidate cleanliness;
* authority expiry.

Do not overstate evidence. A passing existing test is supporting evidence, not a substitute for source inspection of security-critical code.

All Worker 3 authority expires at the terminal report.

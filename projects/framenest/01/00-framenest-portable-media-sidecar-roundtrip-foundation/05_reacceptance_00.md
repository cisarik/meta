# FrameNest Portable Media Sidecar — Fresh Full Re-Acceptance After Documentation Correction

## Canonical exchange coordinates

```text
Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Fresh Independent Full Re-Acceptance Worker
Worker phase: reacceptance
Native planning mode: not-used
Maximum plan-only cycles: 0
Reasoning recommendation: high
Evidence posture: independent
Independence: fresh
Authority renewal: not-applicable
```

Do not enter Native Plan Mode. Do not produce a plan.

Perform the re-acceptance directly. Do not delegate, spawn sub-agents or divide the acceptance across other actors.

## Role and authority

You are a fresh independent re-acceptance Worker.

You did not implement the original stack or its correction. Prior Worker reports are navigation evidence, not proof.

```text
Implementation authority: none
Repair authority: none
Repository-source mutation authority: none
Test mutation authority: none
Commit authority: none
Publication authority: none
Push authority: none
Deployment authority: none
Logical-whole closure authority: none
```

Your only decision is whether exact corrected candidate:

```text
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

deserves `reacceptance-PASS`.

Do not repair any defect you find. Preserve the candidate and report the smallest correction boundary.

## Exact corrected candidate

```text
commit:  230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
tree:    3d74e08f65c2d99f99c602085e6e097451a52230
parent:  87032d3826daaa217769acccc0eb37f1c1ffb1de
subject: docs: reconcile sidecar implementation status
```

Required complete ancestry:

```text
230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
└── 87032d3826daaa217769acccc0eb37f1c1ffb1de
    └── 633fa3b3884bc865dba26643034ef0c2fc12f394
        └── 96bf7df2001c38284d9aa136b56d0109f24700d5
            └── a23b4bc786357da3591a4f75087b7e8a3d50d341
```

Intermediate objects:

```text
87032d3826daaa217769acccc0eb37f1c1ffb1de
tree 881a93734cac120bff048c42ff432cd38755443a
parent 633fa3b3884bc865dba26643034ef0c2fc12f394
subject feat: add portable media sidecar CLI
```

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

The corrected candidate is intentionally unpublished.

## Authorized fresh acceptance checkout

Read-only correction source:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w4-e01
```

Fresh re-acceptance target:

```text
/home/agile/Projects/framenest-worktrees/framenest-portable-media-sidecar-roundtrip-w5-e01
```

Before creation, verify:

1. Correction source exists.
2. Its origin is public FrameNest.
3. Its branch is `fix/portable-media-sidecar-documentation-convergence`.
4. Its HEAD/tree/parent/subject match exact corrected candidate.
5. It is tracked/index/untracked clean.
6. No Git operation is active.
7. Fresh target is absent.
8. Credential-free public `main` remains exact baseline.
9. Corrected candidate and repair branch are absent from public refs.

Do not switch, fetch into, clean, reset, stash or mutate the correction source.

If every precondition passes, create exactly one independent acceptance clone:

1. Clone public FrameNest with `--no-checkout` into the absent target.
2. Fetch the unpublished corrected objects read-only from the correction source.
3. Check out exact `230ce43…` detached.
4. Initialize only `.ap`.
5. Keep `origin` pointing to public GitHub.

Do not create a branch or push a ref.

If the target exists or any gate fails, stop `BLOCKED`. Do not delete or reuse it.

## Post-creation Git gate

Prove:

* exact physical target path;
* public origin;
* detached exact corrected HEAD;
* exact tree, parent and subject;
* exact four-commit first-parent ancestry;
* no merge commits;
* every intermediate object matches;
* public `main` remains `a23b4bc…`;
* corrected candidate is absent from every public ref and tag;
* `.ap` gitlink and submodule match;
* index/worktree/untracked state is clean;
* no active Git operation.

The cumulative diff from public baseline must still contain exactly these 18 paths:

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

Verify every per-commit diff separately:

* codec commit: four paths;
* application/filesystem commit: six paths;
* CLI/documentation commit: eight paths;
* correction commit: exactly `README.md` and ADR-0059.

Do not rely on cumulative diff alone.

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
  PYTHONPYCACHEPREFIX=<external-temporary-directory> \
  PYTHONPATH=<reacceptance-clone>/src
```

Prove all imported FrameNest and sidecar modules resolve from the re-acceptance clone.

Use:

* pytest `-p no:cacheprovider`;
* `--basetemp` outside the repository;
* external `PYTHONPYCACHEPREFIX` for compile validation.

Do not create or later delete repository bytecode/cache artifacts.

Do not create, install, repair, synchronize or reconstruct a `.venv`. Do not run Poetry/uv environment or dependency commands.

## Re-acceptance objective

Independently determine whether the complete corrected stack truthfully delivers:

> A deterministic, strictly versioned portable media-sidecar v1 projection; safe explicit export, validation and catalog comparison for one selected media location; and a thin machine-readable operator CLI—while SQLite remains authoritative and import, rebuild, Save coupling, repair, fan-out, synchronization, HTTP and deployment remain excluded.

This is a full re-acceptance, not merely a check of the two corrected lines.

## Gate 1 — Correction integrity

Compare exact parent `87032d3…` with corrected tip `230ce43…`.

Verify the correction commit:

* changes exactly `README.md` and ADR-0059;
* removes the obsolete README denial that FrameNest has no sidecar schema;
* does not alter the dedicated CLI section or unrelated catalog claims;
* updates only stale ADR implementation-status language;
* preserves ADR decisions, v1 schema, authority model and residual risks;
* adds no commit hashes, publication or deployment claims;
* changes no code, tests, configuration, dependencies or migrations.

Reject any hidden semantic expansion.

## Gate 2 — Documentation convergence

Read candidate versions of:

```text
README.md
PRODUCT.md
SPEC.md
ROADMAP.md
SECURITY.md
docs/adr/0059-portable-media-sidecar-roundtrip-foundation.md
docs/adr/README.md
```

Search all live sidecar claims and distinguish current normative truth from historical ADR context.

Verify they consistently state:

* portable sidecar v1 exists;
* export, validate and compare exist;
* projection targets one explicit selected location;
* sidecars are deterministic catalog projections;
* SQLite remains authoritative during normal operation;
* sidecars never overwrite the catalog;
* no import/rebuild exists;
* no metadata Save coupling exists;
* no automatic repair, fan-out or synchronization exists;
* no HTTP/browser or deployment claim exists;
* no secrets, absolute roots, device identity or requester-private data are included;
* Windows replace/case-folding evidence remains incomplete.

There must be no remaining live assertion that sidecar schema or the implemented stack does not exist.

## Gate 3 — Domain codec

Inspect source and challenge representative fixtures independently.

Verify:

* exact format and schema version;
* closed root/nested schema;
* complete fixed key set;
* nullable and collection representation;
* duplicate-key rejection;
* UTF-8/BOM/oversize/extra-field handling;
* malformed versus unsupported distinction;
* no `sidecar_written_at_ms`;
* deterministic canonical bytes and one trailing LF;
* existing domain validators own value constraints;
* sanitized error messages.

## Gate 4 — Catalog projection and authority

Verify:

* explicit media/location resolution;
* identity relationship;
* availability and library requirements;
* metadata timestamps rather than logical-media timestamps;
* ordered tag definitions;
* classification, genres, creator and Processed projection;
* inconsistent catalog state fails closed;
* no repository write;
* no Save coupling;
* no sidecar import;
* no location fan-out.

## Gate 5 — Filesystem safety

Inspect actual implementation order and error paths.

Verify:

* adjacent full-filename placement;
* root/parent/source non-symlink gates;
* native path flavor and containment;
* inode classification before parse;
* bounded 256 KiB reads;
* preservation of unsafe, foreign, malformed and unsupported targets;
* `unchanged` does not replace or mutate inode/mtime;
* create/replace uses exclusive same-directory owned temp;
* write/fsync/validation/mode/replace/directory-fsync/readback order;
* pre-replace failure preserves the previous target;
* cleanup cannot remove unrelated files;
* no SQLite mutation.

Adjudicate the known close-to-chmod/replace race under the trusted local-library threat boundary. It must not create a silent false-success or new privilege.

Windows replace/case-folding remains a documented non-blocking residual unless candidate requirements claim otherwise.

## Gate 6 — Compare semantics

Verify exact results and precedence:

```text
match
stale
mismatch
missing
```

including:

* non-regular is an error, not missing;
* malformed/unsupported/foreign identity precedence;
* payload equality excludes only the two metadata timestamps;
* equal payload wins over misleading timestamps;
* null revision ordering;
* library ID and relative path are payload, not foreign-identity keys;
* compare performs no repair.

## Gate 7 — CLI contract

Verify:

```text
framenest-sidecar export --media-id <UUID> --location-id <UUID>
framenest-sidecar validate --path <PATH>
framenest-sidecar compare --media-id <UUID> --location-id <UUID>
```

Confirm:

* exact `pyproject.toml` entry;
* no lockfile/dependency change;
* CLI remains a thin adapter;
* catalog operations use existing settings/migration/engine/repositories and dispose the engine;
* validate does not access catalog configuration or print decoded content;
* invalid identities fail before catalog composition;
* command is non-interactive;
* exact success JSON/result/result-code pairs and exit `0`;
* compare `missing` is exit `0`;
* exact error JSON, empty stdout and exit `1`;
* structured application/store codes are preserved;
* unexpected errors are sanitized;
* no traceback, path, database location or payload leakage;
* human argparse `--help` behavior is intentional.

Run representative commands from an unrelated working directory.

## Gate 8 — Operator CLI hygiene

Independently inspect:

```text
tests/contract/test_operator_cli_hygiene.py
tests/contract/test_sidecar_cli.py
```

Verify sidecar CLI import:

* has no configuration side effect;
* does not inspect caller cwd;
* does not touch an explicitly missing environment file;
* emits no output;
* succeeds from an unrelated cwd.

The central `CLI_MODULES` tuple is known to omit other public CLI modules and may be curated. This is not automatically a defect. PASS requires equivalent durable coverage or a concrete source/test proof that the invariant is not orphaned.

Do not edit the tuple.

## Gate 9 — Automated evidence

Run the focused sidecar stack:

```text
tests/unit/domain/test_media_sidecar.py
tests/unit/application/test_media_sidecar.py
tests/unit/infrastructure/filesystem/test_media_sidecar_store.py
tests/contract/test_sidecar_cli.py
tests/integration/test_media_sidecar_roundtrip.py
```

Expected historical count: 77 passing tests.

Run related gates:

```text
tests/contract/test_operator_cli_hygiene.py
tests/contract/test_library_cli.py
tests/integration/test_persistence_migrations.py
```

Expected historical count: 24 passing tests.

Run the complete repository Python pytest suite at exact corrected candidate.

Any non-zero result requires explicit classification. Do not suppress, deselect or rewrite failures.

Worker 3 previously observed isolated-clone failures involving missing checkout-local console scripts or unavailable `poetry build`, but that report is not proof for this session.

If the same harness class occurs:

1. prove every sidecar and candidate-relevant test remains green;
2. enumerate and classify all full-suite failures;
3. show they require a forbidden/unavailable checkout-local `.venv`, installed console scripts or build executable;
4. reproduce a bounded representative set at exact public baseline in a separate disposable baseline clone outside the candidate;
5. prove no candidate-specific failure remains.

A non-zero full suite may be classified as a pre-existing harness/environment limitation only with that fresh causal evidence. Otherwise it prevents PASS.

Do not create a `.venv`, install the candidate, modify PATH with untrusted binaries or weaken the execution envelope.

Also run:

* exact-source provenance;
* `compileall -q` with external `PYTHONPYCACHEPREFIX`;
* complete-range `git diff --check`;
* documentation contradiction searches;
* final Git identity and cleanliness gates.

## Gate 10 — Publication readiness without publication

If every acceptance gate passes, verify a later Worker could perform one ordinary non-force fast-forward:

```text
a23b4bc786357da3591a4f75087b7e8a3d50d341
→ 230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
```

Confirm:

* public `main` has not moved;
* corrected candidate is a strict fast-forward descendant;
* candidate is absent from public refs/tags;
* no deployment is required by this logical whole.

Do not push or publish.

## Prohibited actions

Do not:

* change any candidate content;
* add or edit tests;
* repair documentation or code;
* commit, amend, merge, rebase, squash or tag;
* push, publish or create a PR;
* deploy;
* access NUC, SSH, sudo, providers, browser or private media;
* mutate Meta, AP or the owner checkout;
* create or repair a virtual environment;
* invoke Cursor, GUI or AppImage tooling;
* issue the publication prompt;
* close the logical whole.

## Terminal report

Begin exactly:

```text
### Report for ORCHESTRATOR_CHAT

Logical whole identity: framenest-portable-media-sidecar-roundtrip-foundation
Worker session ordinal: 05
Worker exchange ordinal: 01
```

On complete success:

```text
Standard terminal status: PASS
Phase-qualified result: reacceptance-PASS
Result artifact or commit: 230ce43a8ea978422ee6cefa2c70b42a4ee4d8eb
Logical-whole closure: not-closed
Report justification: independent-verification-after-correction
```

Also state:

```text
Re-acceptance disposition: reacceptance-PASS
Publication disposition: not-performed
Publication eligibility: eligible-for-separate-publication
```

On candidate failure:

```text
Standard terminal status: FAIL
Phase-qualified result: reacceptance-FAIL
```

On evidence/environment blocker:

```text
Standard terminal status: BLOCKED
Phase-qualified result: reacceptance-BLOCKED
```

Include:

* fresh-session and no-delegation confirmation;
* isolated-checkout creation;
* exact Git objects, ancestry and per-commit diffs;
* correction-integrity decision;
* documentation-convergence decision;
* domain/projection/filesystem/compare/CLI decisions;
* CLI hygiene disposition;
* exact commands, exits and counts;
* full-suite result and causal classification;
* residual-race and Windows dispositions;
* publication-readiness result without publication;
* deviations and residual risks;
* Resolved Execution Issues / Near-Misses;
* Pre-Existing Failure Classification;
* smallest next step;
* final candidate and source cleanliness;
* authority expiry.

Do not overstate evidence. Do not convert a repairable defect into PASS.

All Worker 5 authority expires at the terminal report.

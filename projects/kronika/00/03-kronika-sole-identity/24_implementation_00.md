# Authoritative Worker prompt — Worker session 24, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `24`, exchange `01`. Stored under the
Meta filename mapping as `24_implementation_00.md`, with report destination
`24_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 24
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C5 — switch the durable writers to the canonical identity
Reasoning recommendation: High
Recommended context capacity: approximately 450k tokens
```

Rationale: `High`. This is the first cut in the whole that writes the canonical spelling
to disk, and it is the **only** cut whose effect is not fully reversible by rolling back
code. A mistake here does not produce a red test; it produces artifacts that a later
release cannot read, or historical rows that silently disappear from the product.

This is cut **C5** from the accepted completion plan at `17_report_00.md` section 1.9.

## Why this cut exists

Cuts C1 through C4 made every **reader** accept both spellings while every **writer** kept
emitting the retired one. That was deliberate: a reader can be widened safely at any time,
but a writer cannot be switched until the widened readers are actually installed on the
host, because otherwise a newly written artifact would be unreadable by the release still
running.

**That condition is now satisfied.** The complete C4 reader release
`ed5bcb481749f5a732170fd967efc5a2f940cae2` is published and installed on the NUC, and it
is the **named rollback floor**. This cut switches the writers.

## Verified current state

```text
Repository checkout topology: standalone checkout
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                ed5bcb481749f5a732170fd967efc5a2f940cae2
Remote origin:                https://github.com/cisarik/kronika
Public main:                  ed5bcb481749f5a732170fd967efc5a2f940cae2, divergence 0 0
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Node:                         v26.8.2
```

Baselines, measured by the Orchestrator:

```text
JavaScript:            583 total, 578 passed, 0 failed, 5 skipped
Retention module:      15 passed
```

**The Python baseline is taken on report.** Cut C4-B reported `4587 passed, 8 skipped,
3 warnings` against C4-A's `4493`. **Reproduce it yourself before editing** and report any
difference rather than assuming either figure.

NUC state, verified live by the Orchestrator during the C4-B deploy. **You have no host
authority and must not attempt any.**

```text
active web release:  ed5bcb481749f5a732170fd967efc5a2f940cae2
layout:              old
capture release:     94e605c17b881461fad3e22fd8c7fca32cb93976
database revision:   0035, equal to head
backup readiness:    ready
```

## The precondition that makes this safe, and the boundary it creates

```text
Installed rollback floor:  ed5bcb481749f5a732170fd967efc5a2f940cae2

A checkpoint written with the NEW spelling must still be readable by that exact release.
Nothing earlier is a valid rollback floor for C5 artifacts. Do not describe every C1
descendant as safe - the complete-reader release is what matters, which is why C4 had to
be installed separately and why this cut must not begin until it was.
```

**This cut is one-way relative to any release older than the floor.** Reverting the
commit is safe for the code; the artifacts written during and after this cut are not.

## In scope — the writer groups

Derive every site yourself. The list below is a measured inventory of the groups and
their known locations, not a specification of every occurrence.

### 1. Durable analysis identities — four pairs, and a trap

Four identities are written into the catalog, each currently a pair of a writer constant
and a canonical constant, with an accepted set built by
`accepted_durable_identity(current, canonical)` in `src/kronika/domain/analysis_identities.py`:

```text
src/kronika/domain/media_analysis_runs.py:21
    RESULT_SCHEMA_VERSION = "framenest-media-suggestion-result-v1"
    CANONICAL_RESULT_SCHEMA_VERSION = "kronika-media-suggestion-result-v1"
src/kronika/domain/media_classification.py:116,117
    MOVIE_IDENTIFICATION_RESULT_SCHEMA_VERSION = "framenest-movie-identification-result-v1"
    MOVIE_IDENTIFICATION_PROMPT_VERSION = "framenest-movie-identification-prompt-v2"
src/kronika/application/media_suggestion.py:36
    PROMPT_VERSION = "framenest-media-suggestion-v4"
    CANONICAL_PROMPT_VERSION = "kronika-media-suggestion-v4"
```

**Note the third location: `PROMPT_VERSION` lives in the application layer, not in
`domain/`.** A derivation that assumes all four pairs are in `domain/` will miss it.

**TRAP — the helper raises when the pair collapses.** `accepted_durable_identity` raises
`ValueError("a durable identity needs two distinct spellings")` when its two arguments are
equal. Its purpose is exactly that alarm: a cut that changes a writer without restructuring
the pair cannot silently collapse acceptance into a single value.

So **changing `RESULT_SCHEMA_VERSION` to the canonical string without restructuring the
pair makes the module raise at import time and the application will not start.** That is
the loud failure, and it is the better one.

**What this cut must therefore do:** the writer constant becomes the canonical spelling,
the former spelling becomes a **retained historical** spelling, and the accepted set
becomes the current writer spelling plus every retained historical spelling. The alarm must
keep working in the new shape, with the same meaning: **the current spelling must differ
from every historical spelling, and every historical spelling must remain accepted.**

### 2. The quieter trap — a set that collapses silently

There is a second acceptance pattern in the tree that does **not** raise:

```text
src/kronika/domain/media_sidecar.py:34,37,38
    SIDECAR_FORMAT = "framenest-media-sidecar"
    COMPATIBLE_SIDECAR_FORMAT = "kronika-media-sidecar"
    ACCEPTED_SIDECAR_FORMATS = frozenset({SIDECAR_FORMAT, COMPATIBLE_SIDECAR_FORMAT})
```

**If `SIDECAR_FORMAT` is changed to the canonical string, this frozenset silently collapses
to one element** - no exception, no test failure unless one exists, and every historical
sidecar written under the former spelling becomes **unreadable**. `media_sidecar.py` also
carries the sidecar file **suffix**.

**Find every acceptance set built this way, not only this one.** The derivation must
distinguish:
- sets built through `accepted_durable_identity` — these raise on collapse
- sets built as a literal `frozenset({a, b})` or tuple — these collapse silently

Report both categories separately, and prove for each that the historical spelling remains
accepted after the switch.

### 3. Backup identity and temporary prefixes

```text
src/kronika/infrastructure/persistence/catalog_backup.py:27
    APPLICATION_NAME = "framenest"
    plus its accepted-names set, and the temporary-artifact prefix used when staging a bundle
```

**Changing a temporary prefix is coupled to a recognizer.** The incomplete-artifact
detector that finds and cleans abandoned staging directories must recognise **both** the
former and the canonical prefix, or an interrupted run before this cut leaves debris that
nothing can identify afterwards. Update the recognizer in the same commit and prove it.

### 4. Off-device and workstation markers

```text
src/kronika/infrastructure/persistence/catalog_backup_offdevice.py
    MARKER_NAME   = ".framenest-catalog-offdevice.json"
    MARKER_PURPOSE = "framenest-catalog-offdevice"
src/kronika/infrastructure/persistence/catalog_backup_workstation.py
    MARKER_NAME   = ".framenest-workstation-snapshot-store.json"
    MARKER_PURPOSE, SNAPSHOT_PURPOSE, TRANSFER_PROTOCOL_NAME
```

**`/mnt/framenest-catalog-offdevice` is a NAMED FROZEN RESIDUE and must not change.** The
marker *purpose* string switches; the *mount path* does not. Do not let a mechanical
substitution in this file touch the mount.

### 5. Release markers and the manifest identity key

```text
deploy/ubuntu/kronika_release.py:52,53
    RELEASE_SHA_MARKER = ".framenest-release-sha"
    RELEASE_MANIFEST_MARKER = ".framenest-release-manifest.json"
    plus the release-manifest identity key
```

C4-A made every **reader** resolve either spelling through accepted tables and fail closed
on disagreement. This cut makes the **writers** emit the canonical spelling. Confirm the
accepted tables still contain the former spelling afterwards, because historical release
trees carry it and are read during rollback.

**The remote deploy-directory artifact name `REMOTE_DEPLOY_DIR/framenest_release.py` is a
C7-B item and is NOT part of this cut.** It is published by
`docs/UBUNTU_NUC_DEPLOYMENT.md` and pinned by a test.

### 6. Vision-probe identity

```text
src/kronika/infrastructure/ai/vision_probe.py:20
    VISION_PROBE_PROMPT_VERSION = "framenest-vision-probe-v1"
```

**This one is different from the other identities and must be treated differently.** It is
a request and response identity for an administrative capability probe and is **never
persisted**, which cut C4-B established and recorded. So there are **no historical rows to
keep readable** and **no historical reader obligation**. It is switched because it is an
outbound identity, not because of compatibility.

State that reasoning explicitly rather than copying the treatment of the persisted
identities.

### 7. Outbound application user-agent branding

```text
src/kronika/infrastructure/ai/constants.py:13
    SHARED_USER_AGENT = "framenest/0.1"
```

Confirm by derivation whether this is read by anything that also *validates* it, so a
switch cannot break a loopback check.

### 8. Every validator and cleanup recognizer coupled to a switched writer

The plan is explicit: *"Update every validator and cleanup recognizer coupled to those
writers."* The temporary-prefix case in item 3 is the named example, not the only one.

**Derive the full set**, and report each coupled recognizer with what it recognises and
what it must keep recognising.

## What must NOT change

```text
FNCBE01, the encrypted protocol magic. Byte-identical. Never renamed.
/mnt/framenest-catalog-offdevice, the frozen off-device mount path.
/opt/framenest/tooling/... both frozen tooling paths.
The capture state directory name, and capture APP_NAME.
Every routine host constant in the release engine: SERVICE, SERVICE_USER, SERVICE_GROUP,
  RELEASE_ROOT, CURRENT, CAPTURE_CURRENT, ENV_FILE, REMOTE_DEPLOY_DIR, tooling paths.
  Those are C6.
The mutation header, both companion protocol strings, every CSS, DOM and port identifier,
  and the deliberately dual-spelled message at tailscale_ingress.py:869. Those are C7-A.
Every FrameNest* class name, including FrameNestJsonFormatter, FrameNestRedactionFilter,
  FrameNestLogger and the FrameNest*Error hierarchy. Deferred by decision.
The environment prefix fallback in lookup_env. That is C7-B.
docs/adr/0001 through 0084, and all 36 Alembic revision files.
pyproject.toml, ap.project.conf, poetry.lock, RESTORATION_REFERENCE.
No migration. Head stays 0035.
Do not rewrite any existing archive, sidecar, marker or stored row. This cut changes what
  is written from now on, never what already exists.
No NUC contact, no provider call, no media analysis, no off-device provisioning.
```

## How you must find the sites — derivation, not a list

**Do not work from the locations above.** Six sessions in this whole found omissions when
the Orchestrator issued a hand-built list, and one omission left four import-boundary
guards passing vacuously. Derive, then reconcile against the groups above.

```text
A. Parse the tree for every constant whose value is a durable identity, grouped by
   persisted versus non-persisted, and by layer. Report the full list.
B. For each, classify its acceptance pattern as raises-on-collapse /
   collapses-silently / no-acceptance-set, and report the three categories separately.
C. For each persisted identity, find every writer site and every reader site, and report
   both counts.
D. Find every validator and cleanup recognizer coupled to a switched writer. Report each
   with what it recognises.
E. Report every site no test currently exercises.
```

**`FROZEN_ALEMBIC_SHA256` contains 36 keys**, revisions `0001` through `0035` plus
`__init__.py`. Measure it yourself. Three Workers in this whole reported 38 and were wrong.

## The ten discipline rules, binding on this cut

```text
1. Derive site lists by PARSING each artefact, never from a prose enumeration.
2. Resolve every cited line to its literal text BEFORE classifying it.
3. A literal in a test fixture is NOT a pin. Require assertion context.
4. Pin and verify each occurrence independently. Never per file, never per function.
5. Reject any display pin that is a whole-file or whole-function regex where the
   literal occurs more than once.
6. Never truncate an inventory. If output is truncated, disclose it and reprocess.
7. Verify every mechanical probe against a known-impossible number.
8. Regenerate every verification table at report time. Never transcribe one.
9. Open and classify every grep hit. Distinguish production presence, historical
   compatibility and negative assertions.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

Rule 3 has a live application. The retention ledger's provenance comments, the frozen ADR
bodies, and the `CANONICAL_*` constants themselves all legitimately contain retired
spellings. None is a defect.

Rule 7 has a live application. A count of writer sites that exceeds the number of identity
constants is implausible and means the probe double-counted.

## Authority

```text
Positive authority: switch every durable writer identity to its canonical spelling;
  restructure every acceptance set so the current spelling differs from all retained
  historical spellings and all of them remain accepted; keep every alarm working in its
  new shape; update every coupled validator and cleanup recognizer; add and extend tests
  including historical-row and both-spelling fixture round trips; create ONE commit on
  local main; run the declared AP and JavaScript routes; run read-only Git inspection.

Negative authority: any host contact of any kind; any publication or deploy; any rewrite
  of an existing artifact or stored row; any change to a frozen residue, a routine host
  constant, a FrameNest* class name, the environment fallback, the mutation header, either
  companion protocol string, or any pin named under "What must NOT change"; a second
  commit; any invocation of .venv/bin/python, python, python3 or poetry run for evidence;
  any provider call, media analysis or off-device provisioning; any dependency change;
  any reading of private/**, personal Fish configuration, ~/.config/opencode, browser
  profiles, cookies, tokens, credential stores or .secrets; any write to /home/agile/meta.

Commands: Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
   ed5bcb481749f5a732170fd967efc5a2f940cae2 --operation test-focus -- <argv>`,
  `./.ap/ap exec ... --operation test`, and
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline <baseline>`.
  **The baseline must be a full 40-character lowercase commit object ID.** After your
  commit the baseline becomes your commit SHA for the same operations.
  JavaScript evidence goes only through `node --test tests/*.test.js` and focused
  `node --test <path>`. Read-only Git inspection is allowed (`git status`, `git rev-parse`,
  `git log`, `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe files
  under /tmp only. Any other command must be stated in the report with its purpose and a
  confirmation that it mutated nothing.

Dependency authority: none. No lockfile change.

Git authority: exactly one commit on local main, without amend. No push.

Network authority: none.

Secret authority: none. Report filenames and existence only, never a value.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On conflict
  between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch files
  under /tmp.

Browser authority: none.
```

## Verification

1. Confirm branch `main`, HEAD `ed5bcb481749f5a732170fd967efc5a2f940cae2`, clean tree,
   submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS,
   `ap project check --baseline ed5bcb4...` PASS. **Stop without editing if any fails.**
2. Reproduce the Python baseline and report it. If it is not `4587 passed, 8 skipped,
   3 warnings`, report the difference before editing. Also reproduce JavaScript.
3. Perform the derivation and reconcile against the groups. Report the three acceptance
   categories separately, the writer and reader counts per identity, and every coupled
   recognizer and untested site.
4. **Prove every acceptance set still contains the historical spelling** after the switch,
   for every identity, in both the raising and the silently-collapsing categories. For the
   silently-collapsing ones, **demonstrate the collapse explicitly** by showing what the
   set becomes if the pair is not restructured, so the defect class is visible rather than
   described.
5. **Round trip both spellings.** For every persisted artifact type - analysis row,
   backup bundle, sidecar, off-device marker, workstation marker, release marker - write
   with the new code, read with the new code, and read a fixture written under the former
   spelling. Report each.
6. **Prove the target-written checkpoint verifies on the installed rollback floor.** The
   plan requires it and it is the single most important artifact proof in this cut.
7. **Prove historical successful analyses remain visible, reviewable and eligible** under
   the same ownership rules, with rows stored under the former spelling.
8. Prove an old backup archive restores to a new destination.
9. Prove `FNCBE01` and `/mnt/framenest-catalog-offdevice` are byte-identical.
10. Prove every coupled cleanup recognizer still recognises the former prefix, specifically
    the incomplete-artifact detector for the backup temporary prefix.
11. Run the full declared `test` operation once and `node --test tests/*.test.js` once.
    Report exact counts. The Python suite takes about twelve minutes; let it finish.
12. Run the retention module. **Part A byte-unmoved. Part B must still measure exactly
    20** - this cut removes nothing - and report every Part C movement with its own
    measurement and cause.
13. Confirm `git diff --stat` touches only reported paths, and confirm the diff contains
    **zero rewrites of existing artifact fixtures**.
14. Commit once, then run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <your commit SHA>` and `./.ap/ap exec --baseline <your commit SHA>
    --operation runtime-info`, and confirm both resolve `src/kronika/__init__.py`.

```text
Evidence tier: E3. Durable-artifact writer change with round-trip and rollback-floor
  verification. No host was contacted; the post-refresh scheduled-backup check belongs to
  the deployment that follows acceptance.
```

## Git

One commit on local `main`, parent `ed5bcb481749f5a732170fd967efc5a2f940cae2`.
Suggested subject:

```text
feat(identity): emit the canonical spelling from every durable writer
```

Do not push. Publication and the routine refresh are separate bounded grants.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not match; if
  the Python baseline differs from the reported figure; if your derivation and the groups
  cannot be reconciled; if any acceptance set would collapse and you cannot restructure it
  without weakening the alarm; if any historical spelling would become unreadable; if
  proving the rollback-floor checkpoint is not possible with the fixtures available; if any
  frozen residue, routine host constant, FrameNest* class name or named pin would have to
  change; if an existing artifact would have to be rewritten; if Part A or Part B would
  move; if you would need host, provider, media-analysis or off-device authority, which you
  do not have; if you would need a second commit; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded commit.

Completion: one commit; every durable writer emits the canonical spelling; every accepted
  set retains the historical spelling and every alarm still fires in its new shape; the
  silent-collapse category demonstrated and closed; both-spelling round trips proven per
  artifact type; the checkpoint proven on the rollback floor; historical analyses still
  eligible; the old archive restore drill passed; FNCBE01 and the off-device mount
  byte-identical; coupled recognizers proven; Part A unmoved and Part B still 20; tree
  clean.

Report destination: the terminal report is delivered to the Orchestrator in this session.
Do not write it to any file. The Orchestrator stores it as `24_report_00.md` in
/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this prompt
  expires. No further implementation, no second commit, no push, no publication, no host
  contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `24` and exchange `01` unchanged. Then:

1. Your derivation: the identity list grouped by persisted and non-persisted and by layer;
   the three acceptance-set categories separately; writer and reader counts per identity;
   every coupled recognizer; every site no test exercises.
2. The reconciliation against the groups, naming every difference.
3. Per identity: the before and after constant values, the restructured acceptance set, and
   the proof that the historical spelling remains accepted.
4. The silent-collapse demonstration, showing what the set becomes without restructuring.
5. Round-trip evidence per artifact type, both spellings.
6. The rollback-floor checkpoint proof, with the exact floor SHA.
7. The historical-analysis eligibility proof.
8. The old-archive restore drill.
9. `FNCBE01` and off-device-mount byte-identity, and the coupled-recognizer proof.
10. `git diff --stat`, the commit SHA, confirmation that nothing was removed, that Part A
    is byte-unmoved, Part B is still 20, and no existing artifact or fixture was rewritten.
11. Full Python and JavaScript counts with per-file attribution.
12. Ledger movements with your own measurement and cause, and your own
    `FROZEN_ALEMBIC_SHA256` key count.
13. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header, disclose it
on the first line of the report body.

## Mandatory reading

- `docs/adr/0085-kronika-sole-identity.md` in full, especially the decision text and the
  "Named frozen residues" list.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/17_report_00.md`, section
  1.9 in full, plus the Corrections table and the additional-findings entry about the
  analysis filter.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/23_report_00.md`,
  sections 1.1, 1.2, 5 and 6.
- `src/kronika/domain/analysis_identities.py` in full. It is the acceptance rule you must
  preserve in a new shape.
- `src/kronika/domain/media_analysis_runs.py`, `src/kronika/domain/media_classification.py`,
  `src/kronika/application/media_suggestion.py`, `src/kronika/domain/media_sidecar.py`.
- `src/kronika/infrastructure/persistence/catalog_backup.py`,
  `catalog_backup_offdevice.py`, `catalog_backup_workstation.py`.
- `src/kronika/infrastructure/ai/constants.py` and `vision_probe.py`.
- `deploy/ubuntu/kronika_release.py`, the marker constants, accepted tables and writers.
- `docs/BACKUP_AND_RECOVERY.md` in full. It is the durable contract this cut changes.
- `tests/contract/test_kronika_identity_retention.py`, the Part B set and Part C helpers.
- `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any credential
store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify that Part A is byte-unmoved, that
Part B still measures 20, that nothing was removed, that no existing artifact fixture was
rewritten, that every acceptance set retains the historical spelling, and that `FNCBE01`
and the off-device mount are untouched.

**After acceptance, publication and the routine NUC refresh are separate grants, and the
refresh carries one extra required observation:** the plan requires that *a scheduled
post-refresh backup reports `ready`*, which is the first live artifact written with the
canonical spelling. **Following this refresh, `ed5bcb4` ceases to be the rollback floor for
artifacts.** The floor becomes the C5 release, and the Orchestrator will name it explicitly
in every later grant rather than referring to the C4 readers.
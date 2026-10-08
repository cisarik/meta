# Authoritative Worker prompt — Worker session 23, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `23`, exchange `01`. Stored under the
Meta filename mapping as `23_implementation_00.md`, with report destination
`23_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 23
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C4B — prepare the host migration machinery and canonical artifacts
Reasoning recommendation: High
Recommended context capacity: approximately 500k tokens
```

Rationale: `High`. This cut builds the machinery for the single highest-risk
operation in the whole, and it must be correct **without ever being run**. C6 renames
a Unix account, swaps systemd units and retargets Tailscale in one maintenance
window, and the only thing standing between that window and an unbootable service is
the recovery logic written and simulated here.

This is cut **C4-B** from the accepted completion plan at `17_report_00.md` section
1.6.

## Why this cut exists

C6 cannot be improvised. It must stop writers, copy state, rename an account, install
units, prepare a release-local environment at a new path, edit a Tailscale handler and
recover safely from a failure at any of those points. **C4-B builds all of that as
repository code and proves it against simulated hosts.** C6 then executes it.

`migrate-identity` does not exist today. There is no phase journal, no recovery
manifest, no exclusive migration lock, no typed environment and path transformation,
no copy-and-verify state handling, and no new-path environment preparation anywhere in
the repository. This cut creates every one of them.

**This cut must not execute any of it against a host.**

## Verified current state

```text
Repository checkout topology: standalone checkout
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                b16ea2c719f46e167c579c34ddd87a915b70cb00
Remote origin:                https://github.com/cisarik/kronika
Public main:                  6e89328640fe5477e08f17f4c31c9fc4bf261238
NOTE: local main is one commit ahead of public main. Work on local main. DO NOT PUSH.
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

**The Python baseline is taken on report.** Cut C4-A reported `4493 passed, 8 skipped,
3 warnings` against a `4399` predecessor, a net `+94` reconciled per test file. The
Orchestrator did not re-run the twelve-minute suite. **You must reproduce it yourself
before editing**, and if your number differs from `4493`, report the difference before
proceeding rather than assuming either figure.

Live host state, for context only. **You have no host authority and must not attempt
any.**

```text
active web release:  6e89328640fe5477e08f17f4c31c9fc4bf261238
capture release:     94e605c17b881461fad3e22fd8c7fca32cb93976
database revision:   0035, equal to head
installed web unit:  framenest.service
  User=framenest, Group=framenest, WorkingDirectory=/opt/framenest/current
  EnvironmentFile=/etc/framenest/framenest.env
  ExecStartPre=/opt/framenest/current/.venv/bin/framenest-production check-database-ready
  ExecStart=/opt/framenest/current/.venv/bin/framenest-production serve
  StateDirectory/CacheDirectory/RuntimeDirectory=framenest, UMask=0077
installed capture units: kronika-capture-* (already canonical)
```

Two facts from that listing matter to this cut and are easy to miss:

- **Both `ExecStartPre` and `ExecStart` name a console script inside `.venv/bin`,
  directly. There is no interpreter-wrapper form.** `check-database-ready` and `serve`
  are **arguments**, not executables. C4-A's guard extracts only the `path=` field, so
  the current unit resolves cleanly to `framenest-production`.
- **Capture units are already `kronika-capture-*`.** Capture identity is therefore
  **asymmetric with web identity today**, and it is already correct. Do not
  "uniformise" it.

## In scope

### 1. `migrate-identity` — preflight and apply, apply forbidden to you

Add a `migrate-identity` subcommand to the canonical engine with **two distinct
behaviours**:

```text
preflight   non-mutating. Reports exactly what would change, in a sanitized form.
apply       mutating. Refuses unless the operator passes the explicit confirmation
            flag the C6 grant will name. Requires an existing, validated preflight.
```

**This grant forbids executing `apply` in every mode, against any target, including a
simulated one driven through the real CLI.** Prove `apply`'s behaviour through unit
tests that exercise its functions directly with fakes. Prove that **ordinary `deploy`,
`rollback`, `activate-capture` and `rollback-capture` never invoke `migrate-identity`
in any form** — that is an explicit acceptance assertion.

### 2. Web and capture layouts must be separate, and all three transition states real

Do not model a single "layout" boolean. The engine must correctly serve and describe
all three states that will actually occur:

```text
1. old web layout; old capture pointer      today
2. new web layout; old capture pointer      immediately after C6
3. new web layout; new capture pointer      after C8-A
```

**Routine web operations must select the installed web layout through validated
effective service configuration, not through a hardcoded service name.** Ambiguous or
unrecognised active layouts must **fail**, not guess. After C6 the helper must not still
assume `framenest.service`, and before C8-A it must not assume the capture pointer has
moved.

Derive the state from what is actually installed and enabled, and state in your report
which signals you use and why a wrong signal fails closed rather than silently
selecting the wrong tree.

### 3. Canonical artifacts

Prepare the canonical counterparts of the web-side artifacts. Derive the filename
mapping from the retention ledger's Part B set, which currently holds **20 paths**:

```text
deploy/systemd/framenest.service                     -> kronika.service
deploy/systemd/framenest-catalog-backup.service      -> kronika-catalog-backup.service
deploy/systemd/framenest-catalog-backup.timer        -> kronika-catalog-backup.timer
deploy/systemd/framenest-catalog-offdevice.service   -> kronika-catalog-offdevice.service
deploy/systemd/framenest-catalog-offdevice.timer     -> kronika-catalog-offdevice.timer
deploy/systemd/framenest.env.example                 -> kronika.env.example
deploy/systemd/framenest-ai-credential-*.conf        -> kronika-ai-credential-*.conf   (three files)
deploy/systemd/framenest-research-credential.conf    -> kronika-research-credential.conf
deploy/ubuntu/framenest-catalog-export-v1            -> kronika-catalog-export-v1
```

The canonical units must use the canonical **target** layout that C6 will install:
`User=kronika`, `Group=kronika`, `WorkingDirectory=/opt/kronika/current`,
`EnvironmentFile=/etc/kronika/kronika.env`,
`ExecStartPre=.../kronika-production check-database-ready`,
`ExecStart=.../kronika-production serve`, and
`StateDirectory`/`CacheDirectory`/`RuntimeDirectory` = `kronika`.

**Preserve installed feature selection.** An optional unit, credential drop-in or
export facility that is **absent** in the observed installed set stays absent. Do not
provision what was never provisioned; this is not provisioning authority. Derive which
are optional from the repository, and state which are treated as optional and why.

### 4. Typed environment transformation — keys AND values

**This is the item most likely to be done wrongly.** `deploy/systemd/framenest.env.example`
carries the former spelling in its **values**, not only in its key prefixes. Measured:

```text
FRAMENEST_DATABASE_PATH=/var/lib/framenest/catalog.sqlite3
FRAMENEST_GALLERY_PREVIEW_CACHE_PATH=/var/cache/framenest/gallery-previews
FRAMENEST_COVER_STORAGE_ROOT=/var/lib/framenest/covers
FRAMENEST_COVER_THUMBNAIL_CACHE_PATH=/var/cache/framenest/cover-thumbnails
FRAMENEST_AI_CONFIG_PATH=/var/lib/framenest/ai/config.json
FRAMENEST_CATALOG_BACKUP_ROOT=/var/lib/framenest/catalog-backups
FRAMENEST_CATALOG_RESTORE_VERIFY_ROOT=/var/lib/framenest/catalog-restore-verify
FRAMENEST_CATALOG_BACKUP_OPS_ROOT=/var/lib/framenest/catalog-backup-ops
FRAMENEST_YOUTUBE_ACQUISITION_ROOT=/var/lib/framenest/youtube-acquisition
FRAMENEST_UDS_PATH=/run/framenest/framenest.sock
```

**Changing prefixes alone leaves the database, the preview cache, the cover storage,
the thumbnails, the AI state, every backup root and the socket on the former paths.**
The transformation must be **typed**: it must know which keys carry a filesystem path
and transform the path component, and which keys carry an opaque value and leave it
alone.

Transform only the specific path **classes** the plan names. **Do not rewrite a value
that merely happens to contain the token**, and in particular:

```text
/mnt/framenest-catalog-offdevice   is a NAMED FROZEN RESIDUE. Never rename it.
```

Also decide and report what happens to values that are **paths into a directory that
this migration does not move**, and values that are **already canonical**, and values
that contain **neither spelling**. The transformation must be idempotent.

### 5. The migration machinery

Implement, and simulate, all of the following. Each is required by the plan.

```text
A root-controlled phase journal and an exact-object recovery manifest.
Exclusive migration locking, consistent with C4-A's reclaimable deploy lock.
Copy-and-verify state handling. Copied state is verified before anything depends on it.
Preparation of new release-local environments at their FINAL new paths, using the
  frozen tooling and the committed lock.
Same-UID/GID account rename: groupmod then usermod, aborting rather than creating a
  second account.
Effective unit and drop-in verification.
Surgical replacement of the existing Tailscale handler: record the current handler
  state first, replace only the one Unix handler, and never reset when another handler
  exists.
Recovery that DISTINGUISHES a pre-write cutover failure from a failure after the new
  application has admitted writes.
```

**Do not assume copying a `.venv` makes it relocatable.** Shebangs and package search
paths embed absolute paths. Prepare the new-path environment properly and **verify
shebangs and search paths**, without modifying the retained old release.

### 6. Preflight must include ancillary integrations

The preflight discovers and reports, in sanitized form, the existing instances of any
**credential-helper path, export executable, and narrow sudo rule** that the migration
would need to update. **Only instances that already exist are migrated.** This is not
provisioning authority, and no secret value may be read or printed — filenames and
existence only.

## A contradiction you must not inherit

The previous prompt in this whole contained a direct contradiction and the Worker
correctly refused to satisfy both halves: it demanded "Part A and Part B must not move"
while also demanding that the engine be moved, and the engine's former filename is a
Part B path.

**The rule for this cut, stated precisely so there is no ambiguity:**

```text
ADDING a canonical artifact does NOT move Part B, because Part B is the set of paths
  whose BASENAME carries the retired spelling. `kronika.service` carries no retired
  basename and therefore does not enter the set.

REMOVING or renaming an existing Part B path DOES move Part B.

Therefore: create the canonical counterparts. Keep every existing former-spelling
  artifact in place. Part B must still measure exactly 20 after this cut, and Part A
  must be byte-unmoved.
```

If you conclude that some artifact genuinely must be removed or renamed, **stop and
report it** rather than moving Part B.

## How you must find the sites — derivation, not a list

**Do not work from the artifact list above.** It is a derived sample. Five sessions in
this whole found omissions when the Orchestrator issued a hand-built list, and one of
those omissions left four import-boundary guards passing vacuously while checking
nothing.

Parse instead, and reconcile before editing:

```text
A. Derive the canonical artifact set by parsing the ledger's Part B basename set and
   applying the replacement rule. Report your mapping and any artifact where the rule
   is ambiguous.
B. Derive every environment key that carries a FILESYSTEM PATH by parsing the settings
   model, the env template, and the code that consumes each key. Report the classified
   key list and the keys you classified as opaque, with your reason.
C. Derive every place that currently assumes the web layout is the old one. Report
   each, classified as in-scope-this-cut / C6 / C7-B.
D. Report every site no test currently exercises.
```

**`FROZEN_ALEMBIC_SHA256` contains 36 keys**, revisions `0001` through `0035` plus
`__init__.py`. Measure it yourself. Three Workers in this whole reported a transcribed
figure of 38 and were wrong.

## Scope boundaries

```text
Do NOT execute `migrate-identity apply` in any mode, against any target, including a
  simulated one through the real CLI.
Do NOT contact any host. No SSH, no worker gate in any mode, no release helper in any
  mode, no Tailscale command, no systemctl against a real system.
Do NOT rename the Unix account, install a unit, move a directory, or edit a handler.
  All of that is C6 and it is explicitly forbidden here.
Do NOT move Part B. Do not delete or rename any existing former-spelling artifact.
Do NOT change any routine host constant in the engine. SERVICE, SERVICE_USER,
  SERVICE_GROUP, RELEASE_ROOT, CURRENT, CAPTURE_CURRENT, ENV_FILE, REMOTE_DEPLOY_DIR and
  both tooling paths stay as they are. C6 owns them.
Do NOT rename the capture units or any capture state, profile, token or environment
  path. Capture identity is already canonical and asymmetric on purpose.
Do NOT rename /mnt/framenest-catalog-offdevice. It is a named frozen residue.
Do NOT change the remote deploy-directory artifact name
  `REMOTE_DEPLOY_DIR/framenest_release.py`. docs/UBUNTU_NUC_DEPLOYMENT.md publishes it
  and a test pins it. If you believe it must change, report it rather than changing it.
Do NOT change any durable writer identity, mutation header, companion protocol, API
  version, CSS, DOM or port identifier.
Do NOT rename FrameNest* class names, FrameNestJsonFormatter, FrameNestRedactionFilter,
  FrameNestLogger or FrameNestConfigurationError.
Do NOT edit docs/adr/0001 through 0084 or any of the 36 Alembic revision files.
Do NOT add a migration. Head stays 0035.
Do NOT change poetry.lock or move RESTORATION_REFERENCE.
No dependency change. No branch, push, tag, merge, rebase or history rewrite.
```

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

Rule 3 has a live application. The retention ledger's provenance comments, and any
comment narrating what an earlier cut did, keep the historical spelling. So do the
frozen ADR bodies. None of those is an in-scope site.

Rule 10 has a live application. **You cannot demonstrate the migration against a real
host, and you must say so.** Simulated-host evidence is what this cut can produce, and
that limitation belongs in the report rather than in a footnote.

## Authority

```text
Positive authority: add the migrate-identity subcommand with non-mutating preflight and
  forbidden apply; implement the three-state layout model; create the canonical web,
  backup, optional off-device, credential, environment-template and export artifacts;
  implement the typed environment and path transformation; implement the phase journal,
  recovery manifest, migration lock, copy-and-verify state handling, new-path
  environment preparation, same-UID/GID account rename, effective unit verification and
  surgical Tailscale handler replacement as SIMULATED logic; add and extend tests
  including simulated-host failure injection; create ONE commit on local main; run the
  declared AP and JavaScript routes; run read-only Git inspection.

Negative authority: any host contact of any kind; executing apply in any mode; any
  account, unit, directory, socket or Tailscale mutation; moving Part B; any change
  outside the scope boundaries above; a second commit; any invocation of
  .venv/bin/python, python, python3 or poetry run for evidence; any provider or
  capture-browser contact; any execution of a kronika-capture command; any dependency
  install, update or lockfile change; any reading of private/**, personal Fish
  configuration, ~/.config/opencode, browser profiles, cookies, tokens, credential
  stores, .secrets or any real credential-helper secret; any write to /home/agile/meta.

Commands: Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
   b16ea2c719f46e167c579c34ddd87a915b70cb00 --operation test-focus -- <argv>`,
  `./.ap/ap exec ... --operation test`, and
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline <baseline>`.
  **The baseline must be a full 40-character lowercase commit object ID.** After your
  commit the baseline becomes your commit SHA for the same operations.
  JavaScript evidence goes only through `node --test tests/*.test.js` and focused
  `node --test <path>`. Fish evidence goes only through `fish --no-config` with a
  synthetic HOME/XDG, exactly as cut C4-A established, because a wrapper that re-execs
  through a shebang does not inherit `--no-config`. Read-only Git inspection is allowed
  (`git status`, `git rev-parse`, `git log`, `git show`, `git diff`, `git ls-files`,
  `git grep`, `git ls-remote`, `git submodule status`, `git merge-base`); no other Git
  command. Throwaway probe files under /tmp only. Any other command must be stated in
  the report with its purpose and a confirmation that it mutated nothing.

Dependency authority: none. No lockfile change.

Git authority: exactly one commit on local main, without amend. No push.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Report filenames and existence only, never a value.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On conflict
  between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch files
  under /tmp.

Browser authority: none.
```

## Verification

1. Confirm branch `main`, HEAD `b16ea2c719f46e167c579c34ddd87a915b70cb00`, clean tree,
   submodule at `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `ap doctor` PASS,
   `ap project check --baseline b16ea2c...` PASS. **Stop without editing if any fails.**
2. Reproduce the Python baseline. If it is not `4493 passed, 8 skipped, 3 warnings`,
   report the difference before editing. Also reproduce JavaScript `578 passed,
   0 failed, 5 skipped`.
3. Perform the derivation and reconcile before editing. Report the canonical mapping,
   the classified environment keys, the old-layout assumptions, and every site no test
   exercises.
4. **Fail-closed layout selection**: prove that a tree presenting both, neither, or an
   unrecognised active layout **fails** rather than selecting one, and that each of the
   three transition states resolves correctly.
5. **Environment transformation**: prove the typed transformation on a synthetic env
   file, and explicitly prove that `/mnt/framenest-catalog-offdevice` is **unchanged**,
   that every path class listed above **did** move, that opaque values containing the
   token are **untouched**, and that a second application is a no-op.
6. **Simulated transitions and failure injection**: for each of the three states,
   simulate a successful transition and then inject a failure **after every phase**.
   For each injection assert: the correct recovery branch is taken, the phase journal
   identifies the last completed phase, UID and GID are preserved, **no second service
   account is created**, and **capture is never restarted**.
7. **Pre-write versus post-write recovery**: prove the two cases take different
   branches, and that the post-write branch does not restore stale copied state.
8. **New-path environment**: prove it is prepared and verified at its final path, that
   shebangs and search paths resolve, and that the retained old release is unmodified.
9. **No automatic migration**: prove by test that `deploy`, `rollback`,
   `activate-capture` and `rollback-capture` never invoke `migrate-identity`.
10. **Tailscale handler replacement**: prove it records current state first, replaces
    exactly one Unix handler, and **never** resets when another handler exists.
11. **Preflight is non-mutating**: prove `preflight` performs no write of any kind, and
    that it reports filenames and existence only for credential helpers.
12. Run the full declared `test` operation once and `node --test tests/*.test.js` once.
    Report exact counts. The suite takes about twelve minutes; let it finish.
13. Run the retention module. **Part A must be byte-unmoved and Part B must still
    measure exactly 20.** Report every Part C movement with its own measurement and
    cause, and confirm that no existing former-spelling artifact left the tree.
14. Confirm `git diff --stat` touches only reported paths.
15. Commit once, then run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <your commit SHA>` and `./.ap/ap exec --baseline <your commit SHA>
    --operation runtime-info`, and confirm both resolve `src/kronika/__init__.py`.

```text
Evidence tier: E2. Repository implementation with simulated-host tests only. No host
  was contacted, and nothing here proves the machinery on a live system.
```

## Git

One commit on local `main`, parent `b16ea2c719f46e167c579c34ddd87a915b70cb00`.
Suggested subject:

```text
feat(deploy): prepare the host identity migration machinery and canonical artifacts
```

Do not push. Publication is a separate bounded grant.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not match; if
  the Python baseline differs from the reported figure; if your derivation and the
  artifact sample cannot be reconciled before editing; if any artifact would have to be
  removed or renamed, which would move Part B; if the typed transformation would have to
  rewrite a value you cannot classify as a path; if any routine host constant, capture
  identity, frozen residue or FrameNest* class would have to change; if a simulated
  failure injection cannot distinguish pre-write from post-write; if you would need real
  host, account, Tailscale or secret authority, which you do not have; if you would need
  a second commit; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded commit.

Completion: one commit; migrate-identity present with preflight proven non-mutating and
  apply never executed; all three transition states correct and ambiguity failing
  closed; canonical artifacts created with every former-spelling artifact retained;
  typed path transformation proven with the off-device mount untouched and idempotence
  proven; failure injected after every phase with correct recovery, preserved UID/GID,
  no second account and no capture restart; pre-write and post-write recovery distinct;
  new-path environment verified without modifying the old release; no routine command
  invokes migration; Part A byte-unmoved and Part B still 20; tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `23_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

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
echoing `kronika-sole-identity`, session `23` and exchange `01` unchanged. Then:

1. Your derivation: the canonical artifact mapping, the classified environment keys
   with path-versus-opaque reasons, the old-layout assumptions with their owning cut,
   and every site no test exercises.
2. The reconciliation against the artifact sample, naming every difference.
3. The three transition states, with the signal used to select each and the fail-closed
   demonstration for ambiguity.
4. The typed transformation, with the before-and-after of a synthetic env file, the
   explicit proof that the off-device mount is unchanged, and the idempotence proof.
5. The migration machinery, capability by capability, each with its simulated test.
6. Failure injection after every phase, in a table, with the recovery branch taken and
   the assertions for UID/GID, no second account and no capture restart.
7. The pre-write versus post-write recovery distinction, with both branches shown.
8. New-path environment preparation and the proof that the old release is unmodified.
9. The `migrate-identity` invocation-freedom proof for all four routine commands.
10. `git diff --stat`, the commit SHA, and explicit confirmation that Part A is
    byte-unmoved, Part B is still 20, and no former-spelling artifact left the tree.
11. Full Python and JavaScript counts, with per-file attribution for any new test.
12. Ledger movements with your own measurement and cause, and your own
    `FROZEN_ALEMBIC_SHA256` key count.
13. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header, disclose
it on the first line of the report body.

## Mandatory reading

- `docs/adr/0085-kronika-sole-identity.md` in full, especially the decision text naming
  the canonical host layout and the "Named frozen residues" list.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/17_report_00.md`,
  section 1.6 in full, plus sections 1.10 and 1.15, because C4-B is what makes C6 and C9
  executable. Also read the Corrections table and the additional-findings table.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/22_report_00.md` in
  full, including its prompt-contradiction finding and its `--no-config` hermeticity
  finding.
- `deploy/ubuntu/kronika_release.py` in full. It is the file you extend.
- `deploy/ubuntu/framenest_release.py`, the retained alias.
- `deploy/systemd/` in full, both spellings, including `framenest.env.example`.
- `deploy/ubuntu/framenest-catalog-export-v1`.
- `docs/UBUNTU_NUC_DEPLOYMENT.md` in full. It publishes the host procedures and the
  remote deploy-directory artifact name you must not change.
- `docs/BACKUP_AND_RECOVERY.md`, for the state-directory contract the copy-and-verify
  handling must respect.
- `tests/contract/test_kronika_identity_retention.py`, the Part B set and the Part C
  helpers.
- `tests/contract/test_nuc_release_remote_contract.py`,
  `tests/contract/test_nuc_operator_runbook.py`,
  `tests/contract/test_operator_network_scripts.py`.
- `src/kronika/configuration.py`, for the settings model that defines which keys carry
  paths.
- `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile, or any real credential-helper secret.

## Communication

Report text, code and comments are professional English. Do not use Czech or Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will independently verify that `migrate-identity` exists
with a non-mutating preflight, that no routine command reaches it, that Part A is
byte-unmoved, that Part B still measures exactly 20, that no former-spelling artifact
left the tree, that the off-device mount string is untouched, and that capture identity
was not altered.

**Publication and the routine NUC refresh remain separate grants, and this cut changes
no host behaviour by itself.** Two host-side items from cut C4-A are still outstanding
and are **preconditions for the eventual C6 window, not for this cut**: the stale
owner-less deploy lock must be removed under its own authority, and one read-only
`systemctl show --property=ExecStart --property=ExecStartPre` should be taken so the
installed-unit guard's systemd parse is confirmed against real host output before
anything depends on it.

**A separate documentation deliverable has been requested by the Cooperator and is
explicitly NOT part of this cut:** a clean-install runbook for a from-scratch Ubuntu
installation with fully canonical host and tailnet identity. He will perform that
installation himself; it is documentation, not scripts. It is captured for a later
grant and must not be folded in here.
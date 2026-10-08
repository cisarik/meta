# Kronika Sole Identity — Closure Plan

### Report for ORCHESTRATOR_CHAT

Presentation note: the planning client requires the enclosing `<proposed_plan>` block and level-1 title above this report header.

| Field | Value |
|---|---|
| Logical whole identity | `kronika-sole-identity` |
| Worker session ordinal | `25` |
| Worker exchange ordinal | `01` |
| Task identity | `KSI-PLAN-CLOSE2` |
| Persistent role | `WORKER` |
| Status | **PASS — planning deliverable only** |
| Phase-qualified result | `not-applicable` |
| Logical-whole closure | `not-closed` |
| Evidence tier | Planning-grade |
| Report justification | `new-evidence` |
| Start and end commit | `3194f48f6b343a460ed5988d92999f91ef999a79` |
| AP pin | `73e20ef80b88700d5fcbc397cd8edd4fc425869f` |
| Changed files | None |
| Commit, push, publication, deployment | None |
| NUC, provider and browser contact | None |
| Delivery | This session only; Cooperator saves `25_report_00.md` manually |

**The remaining sequence is feasible without changing ADR-0085, but the current production migration adapter is not ready for C6.** Source inspection establishes missing activation steps, a deterministic state-copy conflict, and recovery gaps that the existing simulations do not exercise. Two bounded repository repair cuts and independent verification must precede the C6 host window.

The Cooperator selected the proposed maintenance CLI for C-DATA during this session. Its execution remains a separate stopped-writer maintenance window before C6.

## 1. Reconciliation

“Confirmed” below means measured in this session. “Unverifiable-here” means carried evidence requiring later observation; it does not mean a failed check.

| Claim | Measured result | Evidence | Verdict |
|---|---|---|---|
| Canonical standalone checkout on `main` | `/home/agile/Projects/kronika`, `main`, clean | `pwd`, Git topology/status inspection | Confirmed |
| HEAD and public `main` are `3194f48…` | Local HEAD, `origin/main`, and public ref all equal the full starting SHA | `git rev-parse`; final `git ls-remote origin refs/heads/main` | Confirmed |
| AP gitlink and submodule HEAD agree | Both equal the specified AP pin; submodule clean | Submodule/Git inspection and `./.ap/ap doctor` | Confirmed |
| `ap doctor` PASS, stable | PASS, governing variant `stable` | Repeated at closeout | Confirmed |
| Node `v26.8.2` | `v26.8.2` | `node --version` | Confirmed |
| Python baseline: 4,625 passed, 8 skipped, 3 warnings | Full suite not rerun in this session | Supplied baseline and trace | Unverifiable-here |
| JavaScript baseline: 583 total, 578 passed, 5 skipped | Full suite not rerun in this session | Supplied baseline and trace | Unverifiable-here |
| Retention module: 15 passed | **15 passed** through authorized AP `test-focus` | `tests/contract/test_kronika_identity_retention.py`, cache provider disabled | Confirmed |
| Frozen documents: 86 | 86 distinct dictionary keys; retention checks pass | Retention inventory at line 38 | Confirmed |
| Frozen Alembic files: 36 | 36 distinct keys, including `versions/__init__.py`; retention checks pass | Retention inventory at line 127 | Confirmed |
| Approximately 95 `FrameNest*` classes | **61 distinct class definitions** under `src/kronika` | Anchored class-definition search | Corrected |
| Approximately 1,423 `FrameNest*` occurrences | **1,483 word-bounded tokens** across all file types under `src/kronika` | Scoped token search | Corrected |
| `src` plus `tests`: 1,954 tokens | **1,954 in Python files**; **2,037 across all file types** | Same token expression, with and without `-g '*.py'` | Corrected counting scope |
| Nineteen completed commits | Nineteen commits exist in the stated order, including the hermetic-test precursor | `git log ca649f6^..3194f48` | Confirmed; “C0..C5” is shorthand |
| C5 followed C-DATA and C-LOCAL | Published history shows C5 completed first | Accepted plan order versus history/ledger | Corrected; restore remaining dependency gates |
| Current artifact/rollback floor is `3194f48…` | This is the accepted C5 compatibility floor | C5 source/readers and accepted trace | Confirmed as compatibility policy; installed state carried |
| NUC web SHA, old layout, schema `0035`, active service, ready backup | No host contact authorized or attempted | Carried host block only | Unverifiable-here |
| Installed web uses direct `.venv/bin` console executables | Repository old-layout unit has exactly that form | `deploy/systemd/framenest.service:14` | Source confirmed; installation unverifiable-here |
| Capture identity is “already correct” | Unit/account identity is canonical; paths and bridge HTTP identity still require work | Capture units; `src/kronika_capture/bridge/server.py:51`, `:152` | Corrected scope |
| Capture CLI still needs a source rename | Current source already uses `APP_NAME = "kronika-capture"` | `src/kronika_capture/config.py:7`; CLI uses `APP_NAME` | Corrected; installed runtime still requires verification |
| Capture has three changed files beyond branding | Three nonbranding files: +157/−28; complete delta includes `config.py`, making **four files, +158/−29** | `git diff 94e605c..HEAD -- src/kronika_capture` | Confirmed with complete-delta correction |
| Five Part B counterparts are missing | Exactly the three infosec scripts and two Mullvad scripts named in the prompt | Parsed Part B inventory against tracked paths | Confirmed |
| Three specified builders have no caller/test | Only definitions found | Engine and test searches | Confirmed |
| Their listed line correspondence | `cmd_remote_unit_enabled_state:2457`; `cmd_remote_switch_layout_release:2533`; `migration_unit_required:2753` | Literal definitions | Corrected ordering |
| The no-caller inventory ends there | `RemoteMigrationHost.verify_local_readiness:3354` also has no caller | Engine/test references and phase dispatch | Corrected |
| C4-B simulations establish the production sequence | Simulated phases replace production methods; injected failures occur before simulated phase work | Migration tests at lines 611–723 and 1257 onward | Corrected evidence strength |
| C7 removes “SQLite resolver mirrors” | Environment resolver mirrors are standard-library/shell compatibility implementations; the Alembic SQLite helper alias must survive | Engine environment resolver; gate; `alembic_compat.py` | Corrected terminology and removal boundary |
| Resolver helpers can necessarily collapse after fallback removal | Field lookup remains case-folded; direct lookup is case-exact | `identity_env.py:249` onward | Corrected; unconditional equivalence is false |
| Runbook recovery is current | Still hardcodes `0032 → 0033` and a three-file lock inventory | Deployment runbook: 895, 927–931, 961 | Corrected |
| The historical four-file lock is a current host blocker | Its historical report is available; current presence was not observed | Trace versus no host access | Unverifiable-here |
| Handout filename is `25_restoration_00.md` | Actual supplied trace file is `25_handout_00.md`; body self-name differs | Trace file inspection | Corrected; no rename |
| C7-B leaves one retired console entry | Both thirteen application aliases and the capture alias must disappear: **zero retired entries** | `pyproject.toml:10`; retention comment at 1315 | Corrected |
| Living docs describe current package/deployment state | Several still say the `framenest` package remains; execution contract names stale provenance module | README:11; SERVER:38; worker contract:70 versus `ap.project.conf` | Corrected; documentation work remains |

The verified commit order is:

`ca649f6 → 18c357c → 90c93ea → c02c675 → 24bea56 → 02a8048 → 0b75675 → 78c841f → 9c71bfb → 09e45e5 → 77bcb81 → d5955d5 → e1d5ee5 → 76416ce → 0eb6e8e → 6e89328 → b16ea2c → ed5bcb4 → 3194f48`.

Capture identities must retain these separate labels:

| Identity | Measured subtree |
|---|---|
| Target-source capture subtree at current HEAD `3194f48…` | `cb61ef7df481b823647f8c3687b01fc06fe18e0c` |
| Target-source capture subtree at `e1d5ee5…` | `e65422fa576fa5b9947e7408e6980e56707c72c4` |
| Source subtree belonging to carried installed capture release `94e605c…` | `977465503254fe6cdf31673b7e107b9e0487ffe2` |
| Actual installed capture runtime identity now | Unverifiable-here |

### C6 findings requiring repair

These are source findings, not reports of a live NUC failure.

| Finding | Source evidence | Required correction |
|---|---|---|
| Journal creation makes the state-copy destination exist | Journal resides below `/var/lib/kronika` at engine line 251; journal is written at 3596–3598; `copy_state` requires every destination absent at 2977 onward | Put migration control state outside the copied destination; acquire exclusion before journal mutation |
| Migration never switches the canonical web pointer | Switch builder has no caller; production sequence prepares a release and starts the unit referencing `/opt/kronika/current` | Guard and atomically switch the canonical pointer before startup |
| Migration uploads its remote helper into the routine deploy scratch directory without preparing it | `prepare_release_environment:3183` uses `REMOTE_DEPLOY_DIR`; migration has a separate lock | Use one exclusion mechanism and an owned, prepared scratch area |
| Journal writes precede locking; deploy and migration use different locks | `run_migration_apply:3596`; separate lock constants | Prevent concurrent routine deployment/migration and journal replacement |
| Partial account or startup failures can select the wrong recovery | Completed phase recorded only after return; reverse account rename depends on complete phase; writes flag follows startup | Persist intent and substep outcomes; conservatively mark possible writes before startup |
| Timer handling loses prior enablement | Observation records installed files, while `resume_writers:3437` enables every installed timer | Record effective installation, enablement and activity separately; preserve them |
| Credential drop-in paths can remain old | `transform_unit_dropin_text:3565` feeds complete assignment tokens to a root-prefix transformer | Parse directive values, including `LoadCredential` identifier/path syntax |
| Optional export integration can remain unusable | Generic writer creates non-executable output; sudo run-as identity is not transformed; workstation caller remains old | Install typed artifacts with correct modes, update exact sudo rule and stage the caller transition |
| Capture continuity is weaker than claimed | `verify_capture_untouched:2941` checks activity, not before/after runtime identity equality | Compare fresh private runtime snapshots at both ends |
| Production-adapter tests accept commands without modelling their effects | Preparation test runner returns success for otherwise unhandled commands | Add stateful production-adapter tests and failures inside multi-command phases |

These findings require prerequisites to C6. They do not reopen the accepted publication history of C4-B.

## 2. Completion plan

### Standing authority and evidence rules

Every numbered work item below requires its own authoritative prompt. This plan grants none of them.

For every repository implementation, the grant must name the exact starting commit, branch, editable files derived from the specified subsystem, test operations, and commit authority. Publication is separate unless expressly included. No dependency update, AP update, frozen-hash edit, schema revision or history rewrite is included.

Every implementation report must identify:

- Starting commit.
- Exact tested commit.
- Publication commit and public-main verification, or explicitly “not published.”
- Served web commit, installed companion revision and installed capture release where relevant, each separately observed.
- Inventory derivation, uncovered sites, tests, remaining risks and rollback candidate.

Python verification uses the declared AP route against the exact authorized source baseline. JavaScript uses the declared Node route. Candidate changes must not be tested under this report’s old baseline as if unchanged.

Every host item requires a fresh, bounded Cooperator grant. It must enumerate service actions, paths, account changes, opaque credential handling, package installation from the committed lock, ingress changes and data writes separately. Workers do not acquire sudo credentials. Terminal privilege release is recorded.

Before each routine refresh, use canonical `kronika-release status` and `check --release <exact-public-SHA>`. A successful check does not authorize deployment. Routine refresh does not activate capture.

The recommended execution order is:

**C6-P1 → C6-P2 → C6-V → C-RUNBOOK → C-DATA-P → C-DATA-H → C-LOCAL-P → C-LOCAL-H → C-OPS → C6-H → C7-A/S → C7-A/C → C7-B → C8-A/P → C8-A/H → C8-B/P → C8-B/H → C9-A → C9-B → C-INSTALL-DOC → CLOSE.**

Repository preparation could be scheduled differently, but these constraints are mandatory:

- C-DATA-H precedes C6-H.
- C-LOCAL-H and C-OPS precede C7-B.
- C-OPS is not a C6 prerequisite.
- Canonical emissions and observed client migration precede reader removal.
- C8-A preserves the installed capture release; C8-B reviews and activates software changes separately.
- C9-A precedes removal of recovery machinery.
- Clean-install documentation follows identity-removal cuts.
- CLOSE follows final publication, web refresh and acceptance evidence.

### 2.1 C6-P1 — Repair migration exclusion, journalling and recovery

**Mutation:** Repair the existing engine, without adding a second deployment system.

- Use the existing routine deployment exclusion for migration as well; acquire it before writing control state.
- Move migration journal/recovery files to root-only `/var/lib/kronika-identity-migration`, outside state-copy destinations. Write them atomically.
- Preserve an existing incomplete journal and refuse a fresh apply until explicitly recovered.
- Persist phase intent and substep outcomes. Set a conservative `writes_possible` boundary durably before starting the new service.
- Make pre-write recovery restore observed account/group/home, unit and scheduler state even after partial operations. After possible writes, preserve current data and require forward recovery or a separately authorized reverse migration.
- Make copy verification cover file types, symlink targets, permissions and ownership as well as content. Do not overwrite an unrelated destination.
- Remove the three named dead builders on this first engine touch. Reuse existing validated switching facilities when P2 needs them.
- Make permission/query failures distinguishable from “object absent” or “no processes.”

**Authority:** Repository edits to the migration/exclusion implementation and its tests, plus exact retention-ledger changes derived from those edits. No host access.

**Proof:** Stateful tests driving `RemoteMigrationHost` through an owned simulated remote filesystem/process boundary; concurrent invocation refusal; journal-write interruption; destination collision; partial group/user rename; startup succeeds but acknowledgement/journal write fails; no stale-data rollback after possible writes. Demonstrate that the current journal/copy conflict fails before the repair and passes afterwards.

**Rollback:** Authorized repository revert before use. Once used on a host, retain journal-version support until that host’s migration is closed.

**Preconditions/order:** First engine-changing cut; precedes P2 and every C6 host action.

### 2.2 C6-P2 — Complete production activation and integration preservation

**Mutation:**

- Bind migration preflight/apply to the exact current release, source/artifact identity and observed effective configuration; reject intervening drift.
- Prepare the remote helper in owned scratch space.
- Build and validate the exact release environment at the canonical path using the committed lock and frozen tooling. Validate final executable paths.
- Apply the installed-executable guard, then atomically create/switch `/opt/kronika/current` before service startup.
- Observe effective unit fragments/drop-ins and timer enablement/activity, including installations outside a guessed `/etc` filename.
- Stop timers before draining their jobs. Disable obsolete autostart links at cutover; restore only the previously intended canonical scheduling.
- Parse supported systemd directives and sudo rules structurally. Handle `LoadCredential=identifier:path`, executable paths and run-as identity; unknown forms stop preflight.
- Install the export launcher root-owned mode `0755` and the validated narrow sudoers artifact with its required restrictive mode.
- Stage workstation compatibility with an explicit temporary `kronika-recovery pull --remote-layout old|new` selection, defaulting to `old` during preparation. It selects one of two fixed command tuples, never an arbitrary command. C6 switches the authorized operator invocation to `new`; C7-B makes canonical operation the default and removes the old choice.
- Call real local readiness after startup, verify the intended ingress after its bounded replacement, and compare capture runtime identity before and after. Resolve the unused readiness method by wiring the required check, not merely deleting the evidence gap.
- Preserve absent optional integrations as absent.

**Authority:** Repository engine, recovery-client command selection, associated tests and operator documentation. No real export, provider call, host operation or credential read.

**Proof:** Production-adapter tests for missing current pointer, missing scratch parent, disabled installed timers, vendor/drop-in units, credential directive transformation, executable modes, sudo run-as, both fixed workstation command choices, ingress failure and capture-identity change. Unknown commands must fail the test harness. Verify the release by executable behavior in an isolated fixture, not transcript substrings alone.

**Rollback:** Repository revert before host use; afterwards the explicit migration recovery contract governs.

**Preconditions/order:** P1 complete. Required before C6-V.

### 2.3 C6-V — Independent readiness review

**Mutation:** None.

**Authority:** A separate read-only review grant for the exact published candidate and its evidence. No NUC contact.

**Proof:** Reconcile every required C6 capability with its production implementation and a non-vacuous test. Re-run authorized focused checks; confirm frozen hashes, committed-lock preservation and no routine capture restart. Report every untested production command/substep.

**Rollback:** Not applicable.

**Preconditions/order:** P1/P2 complete. Any unresolved production-sequence defect blocks C6-H.

### 2.4 C-RUNBOOK — Correct release-lock and schema-continuation documentation

**Mutation:** Correct the deployment runbook and its contract tests.

Separate three cases:

1. Live lock owner: stop.
2. Proven stale/ownerless residue: inspect the exact phase, ownership and contents before an authorized recovery.
3. `migration-required`: follow observed current/target schema state and the current helper’s actual cleanup behavior.

Document `previous-release` where that phase creates it, and the owner-record lifecycle. Replace “expected current transition `0032 → 0033`” with values derived from the selected release and fresh status. Do not merely substitute `0035` into a permanent example.

Use exact-object recovery and empty-directory verification; no wildcard or recursive parent deletion. Do not claim stale locks can never recur.

**Authority:** Documentation and matching source-contract tests only.

**Proof:** Cross-check every documented artifact and exit branch against the current engine; test three-file, four-file, live-owner, unexpected-file and interrupted-cleanup examples.

**Rollback:** Documentation revert.

**Preconditions/order:** Reflect P1/P2’s final behavior; publish before a later host task relies on it. The historical residue is not assumed to exist now.

### 2.5 C-DATA-P — Implement bounded label maintenance

**Mutation:** Add `kronika-catalog identity-labels check|apply|rollback`, as selected by the Cooperator.

- `check` uses the application read-only engine and produces a private selection receipt plus sanitized candidate counts.
- `apply` requires the approved receipt and exact expected labels. Use `create_sqlite_engine` and `run_in_immediate_transaction`.
- Change the existing device’s `display_name` from `FrameNest NUC` to `Kronika NUC` by ID and expected-value compare-and-set.
- Library changes require a positive preflight and explicit table/selection authority. Change only the approved brand substring, preserving all other characters.
- Record inverse values privately. Rollback is receipt-bound inverse compare-and-set.

No general CRUD expansion, device re-registration, root change or schema migration.

**Authority:** Repository CLI/application/persistence implementation, tests and maintenance documentation; no live data access.

**Proof:** Linked device/library fixtures; stale receipt; wrong candidate count; unauthorized library changes; transaction failure; contention; private-catalog enforcement; unchanged IDs, relationships and all non-label columns; idempotent verified completion.

**Rollback:** Repository revert before execution.

**Preconditions/order:** Publish and install through a separately authorized routine update before C-DATA-H.

### 2.6 C-DATA-H — Execute the label correction

**Mutation:** The exact approved rows only, in a separate maintenance window.

Stop and drain all catalog writers, including relevant scheduled jobs. Acquire the existing backup/maintenance exclusion without nested-lock deadlock. Create and verify a consistent checkpoint before the transaction. Execute the installed maintenance CLI and read back through a fresh connection.

**Authority:** Exact catalog object/column grant, service/timer actions and private receipt storage. Library scope is separately named when needed.

**Evidence/proof:** Sanitized assertions for the label transition, unchanged IDs/links/non-label fields, foreign-key integrity, schema `0035`, private permissions and no remaining selected retired label. Restart only the recorded prior workload.

**Rollback:** Transaction rollback before commit; later, separately authorized inverse compare-and-set. Never restore an old whole catalog merely to undo a label.

**Preconditions/order:** Fresh host preflight, installed command, verified checkpoint; must precede C6-H.

### 2.7 C-LOCAL-P — Implement explicit local-state migration

**Mutation:** Add `kronika-dev migrate-identity-paths check|apply`.

Cover macOS Application Support and Logs, Linux/XDG development data/state/logs, the temporary development root, macOS AI configuration and lowercase Linux/XDG `framenest/ai`, adjacent owned AI status, runtime settings, accepted covers and preview/thumbnail state.

Canonical mapping replaces `FrameNest` with `Kronika`, lowercase `framenest` with `kronika`, and `framenest-development` with `kronika-development` in these owned defaults only.

Keep current defaults until C7-B. Stop managed development processes; copy consistent databases and durable state to absent destinations; verify before acceptance. Preserve originals. Do not revive PID/runtime records. Explicit overrides remain unchanged. A legacy-state detector must prevent silently creating an empty replacement catalog.

**Authority:** Repository code/tests/docs only.

**Proof:** Synthetic macOS/XDG/temp layouts, populated WAL database, absent source, conflicting destinations, interrupted copy, explicit overrides, preserved owned assets/configuration and refusal to inspect/move capture profiles or credentials.

**Rollback:** Revert before use; migration receipts retain the verified source/destination mapping.

**Preconditions/order:** Before C-LOCAL-H and C7-B.

### 2.8 C-LOCAL-H — Preserve each identified local installation

**Mutation:** Run the installed migration for only the Cooperator-identified installations and owned paths.

**Authority:** Exact local paths and managed-process stop/start; no Worker inspection of personal configuration, secrets or profiles.

**Evidence/proof:** A receipt per identified installation: source/destination classification, consistent database verification, owned-file equality, preserved configuration, no conflicting destination and no revived runtime process. Record explicit “no existing state” where applicable; do not infer it.

**Rollback:** Before new writes, verified originals; after new writes, a separately authorized reverse migration from the latest state.

**Preconditions/order:** C-LOCAL-P installed; all required receipts precede C7-B.

### 2.9 C-OPS — Supply the five canonical operator counterparts

**Mutation:** Add the three `kronika_*` infosec scripts and the Fish/Bash `kronika_mullvad_egress` pair. Make canonical implementations authoritative; retain old entry points only through the compatibility window. The Fish wrapper must target the canonical Bash implementation.

Derive every environment variable, test hook, default unit/socket/account, usage string and invocation from the actual scripts. Preserve behavior and exit codes. Use the established temporary dual-prefix conflict contract until C7-B.

**Authority:** The five script families, their tests and operator instructions. No network probes, journal access, firewall/Tailscale mutation or host execution.

**Proof:** Shell syntax and hermetic fake-tool tests, with personal Fish configuration disabled. Missing variables/tools must exercise refusal. Both wrapper paths must reach the same implementation. Preserve command output/exit behavior except the intended identity changes.

**Rollback:** Repository revert; no host rollback required unless a later grant installs them.

**Preconditions/order:** Must precede C7-B; **not a C6 prerequisite**.

### 2.10 C6-H — Migrate the NUC web identity

**Mutation:** Execute the repaired existing `migrate-identity` operation in an explicit maintenance window.

Fresh preflight must establish:

- Served/current release, target and compatible rollback candidate.
- Effective units/drop-ins, timer enablement/activity and running jobs.
- Numeric account/group continuity and home configuration.
- Environment key names and typed path classes, without printing values.
- Optional credential/export/off-device/workstation integrations.
- Protected objects and media roots inside affected trees.
- Actual capture release, effective paths and private runtime continuity snapshot.
- Schema `0035`, backup readiness, available space and absence of unresolved journals/locks.

The apply sequence is: establish recovery/exclusion; pause admission; stop/drain writers; verify capture; checkpoint; copy and verify owned state/configuration/cache; prepare canonical releases; transform typed configuration; rename group/user preserving IDs; install/validate canonical artifacts; guard and switch the current pointer; conservatively record possible writes; start and verify local service; replace only the existing Tailscale handler; verify ingress and capture continuity; restore prior scheduling.

Switch any installed workstation export caller to the prepared canonical command selection within this window. Preserve custom paths and frozen residues.

**Authority:** Exact bounded host grant covering those actions, opaque credential copies and locked dependency installation using the two frozen tooling executables. No provider request, capture restart, schema change or retirement cleanup.

**Evidence/proof:** Canonical account/effective layout, exact served SHA, schema equality, local and authorized tailnet health, preserved state, zero old-prefix assignments, intended timer states, functional previously installed integrations, capture identity equality and no new browser process. Compare sensitive values privately.

**Rollback:** Before possible writes, verified reverse restoration. Afterwards, code rollback on the new layout; reverse-layout recovery must transfer current mutable state under a new grant. Old copied state is not a rollback source.

**Preconditions/order:** P1/P2/V, corrected runbook, C-DATA-H, installed preparation release, fresh `status`/`check`, approved apply plan. C9 is forbidden here.

### 2.11 C7-A/S — Canonical server emissions

**Mutation:** Switch server companion API and web-host emissions to canonical identifiers while retaining compatible readers. Existing dual acceptance is already implemented; do not rebuild it as new work.

In the same commit that changes web protocol constants, **delete**, rather than re-pin, the two `v: <expr>` multiset assertions in `tests/companion_web_bridge.test.js:336–345`. Replace them with behavioral emission/acceptance assertions.

**Authority:** Repository server/web assets, tests and transition instructions; separate publication and web refresh.

**Proof:** Old/new receiver and emitter matrix, canonical API/web emissions, unchanged origin/source checks, unknown protocol refusal and no Gallery/Details regression.

**Rollback:** Previous dual-compatible release on the canonical layout.

**Preconditions/order:** C6 accepted. Server must be published and served before the next companion transition.

### 2.12 C7-A/C — Canonical companion emissions and stored-state completion

**Mutation:** Move companion web emissions, remaining ports/messages, JavaScript globals and coupled DOM/class/style identifiers together. Emit only the canonical mutation header once the canonical server is served; retain server-side old-header acceptance until C7-B.

Complete migration of application-owned browser keys: verify the canonical value before removing an obsolete value; clear the retired duplicate alarm. Preserve origin selection, review state and in-flight recovery. Do not touch unrelated storage.

**Authority:** Repository extension/web coupling and synthetic tests; separate Cooperator extension reload and rendered acceptance. No profile inspection or real acquisition/provider submission.

**Proof:** Mixed-version behavior, canonical emissions, DOM/style agreement, old-only/canonical-only/dual/conflicting storage cases, reset without old-value resurrection, retired alarm removal, interrupted recovery and preserved access checks.

**Acceptance:** After exact-main NUC refresh, Cooperator reloads the identified extension revision, closes stale side panels and refreshes affected pages. Record rendered acceptance against that actual server/extension pair.

**Rollback:** Previous dual-compatible client/server pair; preserve canonical stored values.

**Preconditions/order:** C7-A/S served; precedes C7-B.

### 2.13 C7-B — Remove temporary compatibility

**Mutation:**

- Remove all fourteen retired console aliases and all twenty Part B retired-basename files after their canonical counterparts are established.
- Remove old environment/SSH fallbacks and their standard-library/shell mirrors where no longer needed.
- Preserve canonical settings precedence, case and empty-value behavior. Do not force `lookup_field_value` and `lookup_env` into one function when their contracts differ.
- Add missing `_env_*` parity coverage before simplifying settings sources: case sensitivity, prefix overrides, empty handling and dotenv options. Characterize current behavior; unrelated override fixes are outside this cut.
- Remove old mutation-header and companion-protocol readers only after C7-A acceptance.
- Remove obsolete browser-key readers only after migration receipts.
- Switch emitted command error codes to `KRONIKA_*`; preserve numeric exit statuses.
- Switch local defaults after C-LOCAL receipts; retain the legacy-state refusal safeguard.
- Make workstation recovery canonical-only and remove its temporary old-layout selection.
- Finish canonical production credential tooling, backup/export defaults, temporary operational names and active operator instructions.

Retain historical artifact readers and the Alembic `sys.modules` alias.

**Authority:** Exact repository removal grant covering parsed identity sites and tests; explicit root-project environment refresh to remove stale installed aliases; separate publication/deployment.

**Proof:** Installed wheel exposes exactly fourteen canonical consoles; old aliases are absent, including stale environment scripts. Old-prefix-only inputs no longer configure the application. Canonical behavior and numeric statuses remain stable. Old installed web units reject an alias-free target before pointer switching. Both suites, frozen hashes, per-occurrence identity tests and rendered regression acceptance pass.

**Rollback:** Verified dual-compatible release on the new layout, with current data. Reinstating old host paths is not rollback.

**Preconditions/order:** C6, C7-A, C-LOCAL and C-OPS accepted; fresh canonical host environment and exported transport-variable receipt. No assumption that variables are Fish universal variables.

### 2.14 C8-A/P — Prepare unchanged-release capture path migration

**Mutation:** Add and test explicit `migrate-capture-paths` in the existing helper. It must be unreachable from routine web deploy/rollback.

Prepare the exact installed capture release under `/opt/kronika/releases`, rebuild/verify its environment from that release’s committed lock, and stage canonical pointer/unit paths. Source identity, unit names, account, state, token, profile and bridge protocol remain unchanged.

**Authority:** Repository engine, capture unit path sources, tests and runbook only.

**Proof:** Same-release source/manifest preservation, final executable paths, refusal of conflicting pointers, drain/brake checks, exactly bounded bridge/runner actions and unchanged web service.

**Rollback:** Repository revert before host use.

**Preconditions/order:** C7-B accepted; precedes C8-A/H.

### 2.15 C8-A/H — Move capture paths without changing software

**Mutation:** Execute the prepared operation for the freshly observed installed capture release. Switch `/opt/kronika/capture-current` and effective working/executable paths. Stop/start bridge and runner once. Keep Xvfb running unless a separate concrete grant establishes a need.

**Authority:** Exact capture-path and bridge/runner restart grant. Cooperator alone handles any opaque profile backup with the browser stopped. No login, profile inspection, prompt submission, automatic resend or research activation.

**Evidence/proof:** Identical capture source identity, valid release markers, canonical effective paths, frozen state name, unchanged protocol, one expected browser transition and unchanged web release/health.

**Rollback:** Explicit restoration of prior pointers/unit files. Any recovery browser start needs fresh authority and the five-minute brake; no automatic second launch after readiness failure.

**Preconditions/order:** Fresh capture preflight, no active/paused work needing preservation beyond the drain contract, private recovery references and brake satisfied. Precedes C8-B activation.

### 2.16 C8-B/P — Prepare capture software identity and complete-delta review

**Mutation:** Change the remaining HTTP `Server` and health API labels to canonical capture identity. Keep the already-canonical CLI name. Preserve `framenest-chatgpt-page` solely where it identifies the frozen state directory.

Extend explicit capture activation so a reviewed bridge-code change restarts the bridge as well as the runner. Ordinary web deployment remains capture-neutral.

**Authority:** Repository capture/helper/tests/docs only; offline tests without launching a browser.

**Proof:** CLI/help and mocked HTTP identity, unchanged state resolution/protocol, activation selection and restart-brake tests. Review the complete delta from the freshly observed installed release to the exact target, including driver, runner and CLI behavior changes already present beyond branding.

**Rollback:** Repository revert before activation.

**Preconditions/order:** C8-A accepted. The later activation grant names the exact public target and the complete reviewed delta.

### 2.17 C8-B/H — Activate the reviewed capture software

**Mutation:** Explicit activation of the approved target with the approved bridge/runner cycle.

**Authority:** Separate Cooperator capture activation grant. It must not describe the change as path-only or identity-only.

**Evidence/proof:** Installed release/source provenance, canonical bridge headers/health identity, unchanged protocol/state, bounded browser transition, no automatic resend and unchanged web release. No real prompt submission is needed.

**Rollback:** Explicit compatible capture rollback under fresh restart authority and brake. A rollback restoring retired operational branding leaves the whole open.

**Preconditions/order:** Complete-delta approval, current capture preflight and C8-A acceptance. Precedes retirement.

### 2.18 C9-A — Retire exact obsolete host objects

**Mutation:** Delete only individually approved obsolete units/drop-ins, pointers and configuration/state/cache copies.

First preserve protected credentials, archives, accepted covers, referenced releases and unexpected operator-owned objects through an exact private preservation manifest. Root-only recovery material must not become service-readable. Do not recursively remove `/opt/framenest`: the frozen tooling tree survives.

**Authority:** Separate one-way, exact-object host cleanup grant. Opaque preservation and deletion are distinct clauses. Unknown protected material stops execution.

**Evidence/proof:** No live dependency on a deletion candidate; actual scheduled backup succeeds on the new layout; protected objects preserved; obsolete active objects absent; canonical web/capture healthy; no dangling references; frozen tooling/mount unchanged.

**Rollback:** None for deleted obsolete copies. Recovery uses retained compatible releases and protected material under a new grant.

**Preconditions/order:** C8-A/B accepted, scheduled-backup receipt, fresh exact manifests and no unresolved recovery state. Precedes C9-B.

### 2.19 C9-B — Remove transition machinery and finalize living truth

**Mutation:** Remove old ordinary web-layout support, temporary migration/recovery implementations and transitional client options that C9-A makes obsolete. Preserve durable readers, the Alembic shim and local-state refusal safeguard.

Finalize README, PRODUCT, SPEC, ROADMAP, SERVER, DEVELOPMENT, execution/deployment/backup instructions and active subsystem/operator documentation. Correct stale package, provenance-module and shipped-status claims without reopening closed product wholes. Historical facts remain explicitly historical; frozen documents remain untouched.

**Authority:** Repository edits/tests and explicit commit/publication authority. Final refresh is separately authorized.

**Proof:** Both suites; wheel/resource checks; exact frozen hashes; canonical executable set; semantic classification of every remaining operational hit; public-main equality; no routine deployment route capable of selecting deleted layouts.

**Rollback:** Only a release demonstrated compatible with the retired host layout. A code revert cannot restore C9-A deletions.

**Preconditions/order:** C9-A accepted. Publish and refresh before final rendered acceptance.

### 2.20 C-INSTALL-DOC — Deliver the requested clean-install runbook

**Mutation:** Add `docs/UBUNTU_NUC_CLEAN_INSTALL.md`, linked from the existing deployment runbook and documentation map. Documentation only; no installer scripts.

Describe a from-scratch Ubuntu NUC with canonical product account, host/tailnet naming, directories, units and ingress, while explicitly preserving ADR-0085’s frozen tooling and mount paths. Reuse the sole release helper and distinguish bootstrap tooling from routine updates.

Cover manual OS/toolchain preparation, identity configuration, read-only original media, canonical web installation, backup scheduling/restore verification and optional parked capture provisioning without login or activation by default.

Describe, without values:

- The Cooperator’s existing SSH identity filename still contains the retired spelling; a fresh setup uses an explicitly chosen canonical filename.
- Transport variables currently come from an exported user-dotfile configuration. Do not claim universal-variable storage or prescribe two competing sources.

Include verification checkpoints and recovery references. Clearly distinguish documented steps from an actually completed installation.

**Authority:** Documentation and documentation-contract tests only.

**Proof:** Review against final units/helper/settings; valid links and command forms; canonical instructions with exact frozen exceptions; no hidden scripts, credentials or provider activation.

**Rollback:** Documentation revert.

**Preconditions/order:** After C9-B. Any publication changes public main, so perform the final authorized web refresh to the resulting SHA before CLOSE.

### 2.21 CLOSE — Independent read-only acceptance

**Mutation:** None.

**Authority:** Read-only repository/public-ref review plus narrowly authorized Cooperator host observations and acceptance receipts. No cleanup, repair, provider call or capture restart.

**Evidence/proof:** Reconcile every closure clause in section 5 against the final exact repository/public/served identities. Distinguish current measurements from prior receipts and carried facts. Verify frozen hashes, canonical wheel/commands, historical compatibility, data/local migration receipts, scheduled backup and rendered acceptance.

**Rollback:** Not applicable. A failed clause leaves the whole `not-closed`; it produces one bounded corrective task.

**Preconditions/order:** All preceding obligations accepted. Final review should be independent of the last implementation cut.

## 3. Placement of the named obligations

| Obligation | Placement |
|---|---|
| Five operator-script counterparts | **C-OPS**, before C7-B; independent of C6 |
| Three dead builders | Remove in **C6-P1**, the next engine touch |
| Stale-lock/schema runbook gap | **C-RUNBOOK**, after engine corrections and before relying on the runbook for host work |
| Clean-install documentation | **C-INSTALL-DOC**, after C9-B and before CLOSE |

The no-caller readiness method is an additional finding: C6-P2 must implement and invoke the actual readiness requirement.

The whole therefore needs work beyond “C9-B plus CLOSE”: the requested clean-install documentation remains a separate bounded cut, and the discovered production-adapter defects require preparation cuts before C6.

## 4. Class-name and scope decisions

**Formally exclude the retained Python class/module-name residue for the life of the repository under the current accepted scope.** It is not deferred work inside this whole and is not a closure debt. A later, separately authorized objective could change it; this plan does not schedule one.

This includes the measured 61 `FrameNest*` definitions, the named exception classes and logging formatter/filter/logger classes. Source comments and docstrings remain outside the confirmed identity goal.

The exclusion does not cover operational JavaScript identifiers, CLI/API messages, request protocols, service names, default paths, emitted error codes or newly written durable identities.

Further boundaries:

- No ADR amendment or new schema revision.
- No second manager, account system, repository history or deployment engine.
- No provider calls, credential provisioning, capture login, acquisition or Search/Research activation hidden inside identity work.
- No personal configuration/profile inspection.
- Existing historical artifacts remain readable and are not rewritten merely to improve a text count.
- C7 removes environment compatibility mirrors, **not** the migration-loader alias needed by immutable Alembic files.
- The artifact compatibility floor remains `3194f48…`. Each later host stage additionally needs an exact rollback release compatible with that stage’s layout and configuration; the artifact floor alone does not prove operational rollback safety.

## 5. Closure conditions and retained residues

| Clause | Required closing evidence |
|---|---|
| One canonical application package/distribution | Built wheel metadata names `kronika`; application imports/resources resolve from `kronika`; `kronika_capture` remains the single parked module; no second `framenest` package/distribution |
| Exactly canonical executables | Fourteen wheel consoles: `kronika-{server,db,catalog,library,dev,ai,production,backup,youtube,previews,covers,recovery,sidecar,capture}`; canonical repository/helper/operator entry points; no retired installed aliases |
| All frozen hashes intact | Exact equality for all 86 document hashes and 36 Alembic hashes |
| Canonical visible/operator output | Parsed per-occurrence positive assertions for canonical values, CLI/API behavior tests and Cooperator rendered receipt; absence search alone is insufficient |
| Canonical environment/request protocols | Parsed host key-name receipt; canonical-only configuration/header/protocol tests; preserved canonical settings behavior; migrated companion storage |
| Catalog relationships preserved | C-DATA receipt proves labels only, unchanged IDs/relationships/non-label columns, valid foreign keys and private catalog |
| Development and AI state retained | Receipt for every identified installation; consistent database, configuration and owned-asset preservation; safe default switch and collision refusal |
| Durable compatibility preserved | Historical/current backup, sidecar, marker and analysis fixtures; restore verification and compatible rollback evidence |
| Canonical NUC web layout | Fresh effective-unit/account/path/ingress observation and exact served public-main SHA |
| Canonical capture operational identity | Separate installed-runtime receipt: canonical paths and HTTP/CLI identity, correct capture release, unchanged protocol and frozen state resolution |
| Retired objects safely removed | Exact C9-A deletion/preservation manifests, no live references and preserved protected objects |
| Scheduled backup works on new layout | **Timer-triggered** backup success and restore readiness, identified by observed unit activation; a manually invoked checkpoint is insufficient |
| Rendered behavior accepted | Cooperator receipt against the current public-main NUC release and identified extension revision; Gallery/Details behavior preserved |
| No scope expansion | Diff/authority audit confirms all excluded product, provider, browser, private-data and infrastructure work stayed outside these cuts |
| Independent final reconciliation | CLOSE report identifies repository, public, served web, companion and capture identities separately; no carried fact substitutes for required fresh evidence |

The following survive deliberately:

- `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry`
- `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`
- Encrypted protocol magic `FNCBE01`, including its protocol byte representation.
- Capture state-directory name `framenest-chatgpt-page`; **no executable alias** with that name.
- `/mnt/framenest-catalog-offdevice`
- `docs/FEDORA_SERVICE.md` and `docs/NUC_HOST_BASELINE.md`
- All 86 frozen document hashes and all 36 frozen Alembic hashes.
- Historical ADR bodies/citations, historical artifacts and their narrowly retained readers.
- Existing historical backup/sidecar/release/snapshot identities and stored analysis identities; newly written identities remain canonical.
- The migration-loader alias required by immutable revisions.
- Accepted Python class/module names, source comments/docstrings and negative test assertions.
- Narrow legacy-local-state detection that refuses unsafe empty-state creation; it is not a fallback serving old paths.

The Cooperator’s private SSH filename and choice of exported-variable storage are documented operator setup context, not permission to inspect or rewrite personal files.

## 6. Binding derivation and verification discipline

Every future cut must apply all ten rules:

1. Parse each artifact to derive its site list; prose is only a reconciliation sample.
2. Resolve every cited line to its literal text before classification.
3. Treat fixture data as fixture data; require assertion context before calling it a pin.
4. Verify each occurrence independently.
5. Reject broad file/function regex pins when they can hide another occurrence.
6. Disclose truncated output and reprocess bounded inventories.
7. Check mechanical probes against a known-impossible result and require nonempty/unique source membership.
8. Regenerate verification tables at report time.
9. Classify hits as active production, historical compatibility, excluded prose or negative assertions.
10. State when a requested demonstration cannot exist; never manufacture one.

Every report must state counting scope and separate repository evidence from installed-host evidence.

### Required defect-pattern checks

**Vacuous guards.** Missing directories, moved imports, absent environment variables and unhandled fake commands must fail the relevant test. The new C6 adapter tests must model effects rather than returning unconditional success.

**Collapsing pairs.**

- Four analysis identities use `accepted_durable_identity`; duplicates raise.
- Twelve other application artifact pairs use literal sets/tuples: sidecar format/suffix; backup application/temp prefix; off-device marker name/purpose/stage; workstation marker name/purpose/stage/snapshot purpose/transfer protocol. They do not inherently protect distinct historical membership.
- The release engine’s three historical acceptance tables are explicit literal data for SHA marker, manifest marker and manifest key. Preserve and test their exact membership independently of writers.
- Existing collapse demonstrations are useful. A future writer change must demonstrate both historical and current acceptance at every reader; a tuple need not shrink in length to lose historical membership.

**Transcribed tables.** Frozen Alembic membership is 36. Reports must compute it, not inherit “38” from prior prose.

For every cut, issue derivation rules plus a sample reconciliation list, and require a list of sites with no exercising test. A green suite is not proof that an uncalled production step exists.

The requested universal resolver-collapse demonstration cannot succeed: lowercase canonical field lookup and exact-case direct lookup differ by design. Preserve that distinction or remove unused machinery without changing behavior.

## 7. Regenerated inventory figures

Source: [identity retention ledger](/home/agile/Projects/kronika/tests/contract/test_kronika_identity_retention.py:38).

Dictionary/set extraction required the named assignment, counted anchored entries, rejected duplicates and rejected the impossible control `999999`. The retention module independently passed.

| Inventory | Measured value | Source line |
|---|---:|---:|
| `FROZEN_DOCUMENT_SHA256` | 86 | 38 |
| `FROZEN_ALEMBIC_SHA256` | 36 | 127 |
| `EXPECTED_FRAMENEST_BASENAME_PATHS` | 20 | 166 |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | 507 | 619 |
| Environment prefix tokens | 655 | 1166 |
| Distinct environment names | 103 | 1167 |
| Bare prefix spellings | 29 | 1168 |
| Retired mutation-header occurrences | 73 | 1182 |
| Files containing that header | 30 | 1183 |
| Capitalized occurrences | 2,748 | 1308 |
| Files containing capitalized spelling | 394 | 1309 |
| Retired console entries | 14 currently; **0 after C7-B** | 1316 |

Per-tree inventories exclude the retention ledger itself and use its tracked-text counting rules:

| Tree | Content-bearing files, line 191 | Occurrences, line 293 |
|---|---:|---:|
| `src` | 184 | 1,690 |
| `tests` | 183 | 2,008 |
| `deploy` | 22 | 243 |
| `scripts` | 7 | 86 |
| `docs` | 88 | 1,216 |
| `extension` | 8 | 145 |

These 492 files plus 15 root-level members account for the 507-path membership set. Occurrence totals are weak change alarms, not proof of a correct replacement.

Host-path pins at line 1204 are:

| Literal | Occurrences |
|---|---:|
| `/opt/framenest` | 223 |
| `/etc/framenest` | 83 |
| `/var/lib/framenest` | 109 |
| `/var/cache/framenest` | 29 |
| `/mnt/framenest-catalog-offdevice` | 23 |

`User=framenest` and `Group=framenest` each occur eight times in the ledger’s scope, at line 1216.

The complete Part B inventory partitions into ten systemd artifacts, three Ubuntu artifacts, the root launcher, three infosec scripts and three network scripts. Fifteen canonical counterparts exist; five are missing. C-OPS supplies those five before C7-B removes the twenty retired paths.

The requested standalone-word source search resolves to excluded prose, immutable migration text, retained operational default paths, the dual-header validation message and the old header emission. It does not justify renaming class identifiers or immutable revisions.

## 8. Deviations, risks, missing evidence and next step

### Planned deviations from the earlier sequence

- Restore the C-DATA-before-C6 and C-LOCAL-before-C7-B gates after the already-completed C5 ordering deviation.
- Add C6-P1/P2 and independent C6-V because production-adapter behavior is not established by the existing simulations.
- Split C7-A into served-server and companion transitions.
- Keep capture path migration and complete software-delta activation separate.
- Add the requested clean-install documentation after C9-B.
- Formally exclude Python class/module names rather than retaining an undefined follow-up obligation.

These changes refine execution boundaries; they do not amend ADR-0085 or authorize implementation.

### Missing evidence

No current NUC fact was measured. Served release, effective units/drop-ins, enabled timers, account mapping, environment names, optional integrations, capture continuity, catalog-label candidates, local-installation state and scheduled-backup success require their specified future receipts.

The complete Python and JavaScript baselines remain carried. This session independently ran the retention module and repository/AP checks only.

The largest availability risk is C6. Capture restart risk belongs to C8-A/B. C9-A remains one-way. Rollback candidates must be validated for the layout and artifacts they will actually serve.

### Resolved Execution Issues / Near-Misses

- Some broad read/search outputs were truncated. Relevant inventories and cited findings were reprocessed with bounded reads and explicit parsers; no final count relies on a truncated enumeration.
- Several exploratory path guesses named nonexistent files. They produced read errors only; tracked-path discovery identified the actual modules. Absence at a guessed path was not treated as product evidence.
- Counting scopes initially appeared inconsistent. Separate Python-only and all-file token counts resolved the 1,954 figure.
- Read-only `git ls-tree` was used during initial grounding before the attachment’s narrower Git command list was read. It made no mutation; subsequent inspection used the authorized command set.
- No report or temporary file was created. AP suppresses Python bytecode; the focused retention run disabled pytest’s cache provider.

### Pre-Existing Failure Classification

- **Latent migration implementation defects:** journal/destination collision, absent current-pointer activation, scratch/exclusion coupling, partial-phase recovery, scheduler-state loss and incomplete ancillary transformation. Source-established; no live incident claimed.
- **Verification weaknesses:** synthetic phase replacement and permissive command fakes do not establish production-adapter correctness. Existing green results remain valid for what those tests actually assert.
- **Documentation defects:** stale schema/lock recovery, provenance-module text, package/status prose, capture CLI claim and retired-console end count.
- **Expected compatibility state:** current aliases, old layout sources and retained protocol readers are planned transitional material, not new failures.
- **No observed environment or test failure** in the authorized project check, AP doctor or focused retention run.

### Command accounting and final state

Read-only shell utilities used for inspection/counting included `pwd`, `cat`, `sed`, `rg`, `wc`, `sort`, `head`, `tail`, `cut` and Perl. They read source/trace text and wrote only tool output. Node was queried for its version. Authorized Git inspection and public-ref verification changed no repository state. AP project/runtime checks and the focused retention test provided baseline evidence.

Final checks confirmed:

- HEAD unchanged at `3194f48f6b343a460ed5988d92999f91ef999a79`.
- Local and public `main` equal.
- Working tree and pinned AP submodule clean.
- AP doctor PASS.
- No file, Git, host, provider or browser mutation performed.

**Smallest next step:** issue one bounded repository-only **C6-P1** implementation grant for the journal/exclusion/recovery defects, including removal of the three dead builders. Do not issue a C6 host apply grant against the current adapter.

All authority under this Worker prompt expires on submission of this report.

Orchestration critique:  
**MEASURED:** The restoration material overstates what the C4-B simulations establish. The production journal creates a destination that copying then requires absent; canonical pointer activation has no caller; scheduler and partial-phase recovery evidence is incomplete. Counting scopes and capture CLI status also needed correction. Effect: executing C6 from the handout could interrupt service without a proven recovery sequence. Smallest correction: repair and independently verify the production adapter before preparing the host apply grant.  
**LEAD:** The actual installed optional export/credential integration set may expose additional typed transformation forms. Cheapest useful check: a narrowly authorized Cooperator preflight that reports directive/path classes and equality results privately, without exposing values.

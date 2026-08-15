You are the WORKER under Analytic Programming.

Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 01
Worker exchange ordinal: 01

Worker session target: fresh-worker-session
Worker session profile: Worker-Executed Implementation Planning
Phase: Preflight / implementation-planning
Native planning mode: required

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-grounded design of one repeatable, repository-native immutable Ubuntu NUC release-update contract
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

Reasoning recommendation: High. This task combines deployment automation,
privilege boundaries, backup and rollback, immutable release construction,
remote transport, exact Git provenance, and durable documentation ownership.
Higher reasoning does not expand authority.

Internal delegation and sub-agents: prohibited.
Parallel work: prohibited.

Repository identity:
- Canonical repository: https://github.com/cisarik/framenest.git
- Primary local path: /home/agile/Projects/framenest
- Required public main baseline:
  4b04b86e4ea52c673c41624e3f2abe1e59d45907
- Required AP gitlink:
  17b7e085139e9bcbb0e4953d26aef9b6687d541c

Read completely before planning:
- AGENTS.md
- .ap/AP.md
- .ap/AP_WORKER.md
- .ap/PROMPT_CONTRACTS.md sections needed for planning/report structure
- docs/UBUNTU_NUC_DEPLOYMENT.md
- docs/NUC_HOST_BASELINE.md
- docs/BACKUP_AND_RECOVERY.md
- docs/adr/0032-ubuntu-nuc-deployment-foundation.md
- docs/adr/0052-automated-catalog-backup-retention-and-restore-verification.md
- deploy/ubuntu/README.md
- deploy/ubuntu/fn-production-env-deploy
- deploy/ubuntu/production_ai_deploy.py
- deploy/systemd/framenest.service
- scripts/operator/network/framenest_nuc_worker_gate.fish
- relevant focused deployment and operator contract tests

Repository gate:
1. Begin read-only.
2. Verify repository identity, current HEAD, status, public main, and AP pin.
3. Do not fetch, pull, checkout, reset, clean, stash, modify, stage, commit, or
   push in the canonical checkout.
4. Preserve all owner work.
5. If the canonical checkout cannot provide clean exact-baseline evidence,
   you may create one disposable clone using an exact
   /tmp/framenest-release-contract-plan.XXXXXX directory.
6. A disposable clone is temporary planning evidence only. Verify its public
   main and AP pin and remove only that exact temporary directory before the
   terminal report.
7. Stop on unexplained divergence.

Cooperator-selected objective:

Eliminate repeated rediscovery of the real FrameNest NUC immutable deployment
workflow. Future Orchestrators and Workers must encounter one authoritative,
discoverable routine-update contract immediately, without guessing PATH values,
probing generic uv/Poetry locations, confusing initial host bootstrap with a
routine release update, or reconstructing historical commands from chat.

Accepted live and historical evidence:

- Current public FrameNest main is
  4b04b86e4ea52c673c41624e3f2abe1e59d45907.
- Its AP pin is
  17b7e085139e9bcbb0e4953d26aef9b6687d541c.
- NUC production is healthy at immutable release
  148b6c2012809944262399c1a166e85082606fbf.
- Production schema is 0028.
- framenest.service is active.
- The rollback release and its release-local production executable exist.
- The new 4b04b86... target release directory is absent.
- Current scheduled catalog backup/readiness is ready.
- The latest scheduled create, verify, and disposable restore completed
  successfully at schema 0028 with no later failure.
- Off-device status is disabled. This is a separately parked host-loss risk,
  not authority to expand this logical whole.
- Exact tooling:
  - Poetry:
    /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
  - CPython:
    /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
- The active release confirms Poetry 2.4.1, CPython 3.13.14,
  `.framenest-release-sha`, deployment-local `poetry.toml` with
  `[virtualenvs] in-project = true`, and `poetry check --lock`.
- uv was used only to provision the pinned standalone CPython during initial
  host bootstrap. Routine immutable release updates must not require uv on PATH
  or invoke uv when the accepted CPython already exists.
- Historical release construction used a source archive, not a wheel:
  exact-SHA git archive, archive hash, transfer, identical-hash verification,
  new `/opt/framenest/releases/<SHA>`, extraction,
  `.framenest-release-sha`, deployment-local `poetry.toml`, release-local
  `.venv`, locked main dependency installation, pre-cutover validation,
  atomic `/opt/framenest/current` switch, one service restart, health and
  state verification, exact temporary cleanup, and sudo timestamp invalidation.
- Historical Poetry preparation commands were:
  - poetry check --lock
  - poetry env use <exact tooling CPython>
  - poetry install --only main --no-interaction --no-ansi
- Old releases are retained. Wildcard or broad cleanup is forbidden.
- No NUC mutation has occurred in the current attempt.
- The attempted 4b04b86... deployment is paused before mutation.
- The AP upgrade ledger declared in AGENTS.md targets only cisarik/ap and must
  not store FrameNest deployment truth.

Planning goal:

Return one decision-complete implementation plan for the smallest safe
repository change that creates a canonical routine immutable NUC update
interface and makes it unmissable to future Orchestrators and Workers.

Required design outcomes:

1. Always-read discovery
   - Propose a concise root AGENTS.md invariant naming the canonical routine
     release-update entry point.
   - State the exact Poetry and CPython tooling paths.
   - State that uv is bootstrap/maintenance tooling, not the routine update
     command.
   - Require future deployment work to use the canonical helper and run its
     read-only check first instead of improvising commands.

2. One user-facing command
   - Design one stable operator entry point under deploy/ubuntu/.
   - Reuse the established thin Fish entry point plus standard-library Python
     helper pattern when appropriate.
   - The Cooperator should invoke one obvious command rather than paste a large
     privileged script.
   - Do not introduce a new third-party dependency.

3. Explicit operating modes
   - A genuinely non-mutating `--check` mode.
   - A separately authorized deployment mode.
   - An explicit, bounded rollback/recovery route.
   - Help and sanitized structured phase/exit evidence.
   - Deployment mode must never follow automatically from check mode.

4. Exact source provenance
   - Require an exact full commit SHA.
   - Prove local commit/tree state and current public ref equality when the
     deployment contract requires public main.
   - Reject dirty, mismatched, ambiguous, or unpublished source.
   - Create and hash an exact source archive.
   - Address `.ap` explicitly: ordinary `git archive` does not recursively
     include Git submodule content. Determine whether the production artifact
     requires the pinned `.ap` tree and design exact deterministic handling
     rather than silently omitting or following moving AP main.
   - Verify transferred bytes before extraction.

5. Routine-update versus bootstrap boundary
   - Initial uv/CPython/Poetry provisioning and tool upgrades remain separate,
     explicitly authorized maintenance.
   - Routine updates use the already accepted pinned Poetry and CPython paths.
   - Missing or mismatched tooling fails closed with an actionable sanitized
     result; it must not trigger automatic installation or network download.

6. Remote and privilege boundary
   - Reconcile with the existing strict SSH gate and current global sudo
     timestamp workflow.
   - Never request, receive, print, store, or transmit a password.
   - Use `sudo -n` only after an explicit owner-established timestamp.
   - Avoid broad remote shell strings where a transferred, checksum-verified,
     tracked helper or another safer boundary is appropriate.
   - Define exact temporary paths, ownership, permissions, concurrency lock,
     recovery material, cleanup owner, and stale-recovery behavior.
   - Preserve the first causal failure.
   - Ensure `sudo -K` or the applicable exact invalidation route is part of
     terminal operator handling without fabricating success after session loss.

7. Release preparation
   - Target release must be absent; never overwrite an existing release.
   - Preserve the exact previous release as rollback.
   - Verify capacity before preparation.
   - Extract only into the exact new release root.
   - Reject path traversal, symlink escape, and malformed archives.
   - Write and verify `.framenest-release-sha`.
   - Create exact release-local Poetry configuration.
   - Build the release-local `.venv` from committed `poetry.lock`.
   - Keep release source and `.venv` root-controlled and non-writable by the
     service account.
   - Do not copy or mutate production secrets or blindly replace
     `/etc/framenest/framenest.env`.

8. Backup, schema, and readiness
   - Require current sanitized backup/restore-readiness evidence.
   - Deployment mode should create or select a fresh verified rollback
     checkpoint before cutover.
   - For the first implementation, prefer a fail-closed routine-update boundary
     that refuses an unexpected packaged/production schema difference rather
     than hiding general migration authority inside the helper.
   - If the plan proposes migration support, justify its rollback correctness
     separately and do not assume SQLite downgrade safety.
   - Run target release database status/readiness under the accepted service
     identity and explicit environment-file contract.
   - No implicit migration during startup.

9. Cutover and rollback
   - Atomically switch `/opt/framenest/current`.
   - Restart only framenest.service and only once after pre-cutover gates pass.
   - Verify service state, release identity, working directory, database
     readiness, health through the accepted ingress mode, and sanitized logs.
   - On post-switch failure, restore the exact previous symlink, validate its
     readiness, restart, and verify health.
   - Distinguish deployment failure, rollback success, rollback failure,
     readiness timeout, service terminal failure, cleanup failure, and unknown
     privilege-release state.

10. Idempotency and crash recovery
    - No wildcard deletion.
    - Existing target or recovery state fails closed.
    - Never treat a partial existing target as deployable.
    - Define deterministic operator recovery for interrupted preparation,
      cutover, rollback, or cleanup.
    - Preserve evidence needed for recovery without retaining secrets.

11. Durable documentation ownership
    - Update the Ubuntu NUC runbook to separate host bootstrap/maintenance from
      routine immutable updates.
    - Update deploy/ubuntu/README.md so it no longer claims that the directory
      deliberately lacks tested host-mutating release automation.
    - Decide whether a new ADR (next available number after ADR-0059) is the
      appropriate durable architecture owner.
    - Treat docs/NUC_HOST_BASELINE.md as historical baseline evidence; do not
      rewrite historical pre-deployment facts as though they were originally
      observed later. Add only a justified cross-reference if needed.
    - Do not update living production SHA claims until an actual later
      deployment provides production evidence.
    - Do not use the AP upgrade ledger for this FrameNest operational contract.

12. Validation
    - Propose focused contract tests using fake command/transport runners and
      temporary directories only.
    - No test may contact the real NUC, use real sudo, inspect credentials,
      mutate systemd, or access private media.
    - Cover positive check, source/public mismatch, dirty source, missing exact
      tooling, hash mismatch, existing target, unsafe archive, stale recovery
      state, backup-not-ready, schema mismatch, Poetry/lock failure, readiness
      failure, atomic switch, post-switch failure with successful rollback,
      rollback failure, cleanup failure, and sanitized output.
    - Include syntax/format checks for every new executable.
    - Identify the affected broad test suite and exact acceptance gates.
    - Avoid creating another monolithic test file when focused test modules can
      express the contract clearly.

Evidence tier:
- This planning task: E0, read-only.
- Anticipated repository implementation: E2, reversible and cross-cutting.
- Later real NUC deployment: E3, requiring a separate live preflight,
  explicit Cooperator approval, checkpoint/rollback, and fresh independent
  production acceptance.

Plan output must include:

- recommended artifact/file map;
- exact user-facing CLI shape;
- local versus remote responsibility boundary;
- public Git and archive/submodule provenance design;
- privilege and transport design;
- phase/state machine;
- backup/schema/readiness rules;
- cutover and rollback algorithm;
- crash-recovery and cleanup model;
- sanitized evidence and exit-status model;
- documentation ownership and required updates;
- focused and broad test matrix;
- implementation order;
- exact allowed path set for implementation;
- explicit excluded scope;
- risks and decisions requiring Orchestrator or Cooperator disposition;
- a decision on whether the same Worker session is healthy for implementation;
- a concise implementation-prompt readiness capsule.

Prohibited in this planning exchange:

- repository file modification;
- host, NUC, SSH, sudo, systemd, service, Tailscale, firewall, storage, backup,
  database, symlink, or deployment mutation;
- creation of a real archive for deployment;
- external provider calls;
- credential access;
- private media inspection;
- package or dependency installation;
- canonical Git writes;
- commits, pushes, tags, branches, merges, rebases, resets, cleans, or stashes;
- implementation;
- publication;
- deployment;
- logical-whole closure.

Stop conditions:

- repository identity or exact public baseline cannot be established;
- current source contradicts an accepted fact materially;
- owner work cannot be safely preserved;
- the planning result would require secret inspection;
- a safe routine-update boundary cannot be separated from migration or bootstrap;
- the plan cannot provide deterministic rollback and crash recovery;
- the task expands into off-device backup configuration, network reconfiguration,
  AP protocol modification, FrameNest product features, or live deployment.

Terminal response:

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Then include:

Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 01
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: planning-PASS | planning-PARTIAL | planning-BLOCKED
Result artifact or commit: no repository artifact; terminal planning report
Result evidence: <concise verified evidence>
Logical-whole closure: not-closed
Report justification: new-evidence
Authority expiry: all Worker 01 exchange 01 planning authority expired at this report

Provide the required decision-complete plan and evidence. Do not implement.
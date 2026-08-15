You are the WORKER under Analytic Programming.

Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 02
Worker exchange ordinal: 01

Worker session target: fresh-worker-session
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Native planning mode: not-used

Reasoning recommendation: High.
Internal delegation and sub-agents: prohibited.
Parallel work: prohibited.

The prior Worker 01 planning authority expired. Its report was reconciled by
the ORCHESTRATOR as planning-PARTIAL because critical identifiers, paths, CLI
names, and safety boundaries were corrupted. Do not copy identifiers or paths
from that report. The corrected decisions in this prompt are authoritative.

Repository:
- https://github.com/cisarik/framenest.git
- Required public main baseline:
  4b04b86e4ea52c673c41624e3f2abe1e59d45907
- Required AP gitlink:
  17b7e085139e9bcbb0e4953d26aef9b6687d541c
- Canonical owner checkout:
  /home/agile/Projects/framenest
- Contained implementation clone:
  /home/agile/Projects/framenest-worktrees/framenest-repeatable-immutable-nuc-release-deployment-contract-w2
- Implementation branch:
  feat/repeatable-immutable-nuc-release-deployment-contract

Required reading:
- AGENTS.md
- .ap/AP.md
- .ap/AP_WORKER.md
- docs/WORKER_EXECUTION_CONTRACT.md
- docs/UBUNTU_NUC_DEPLOYMENT.md
- docs/BACKUP_AND_RECOVERY.md
- docs/NUC_HOST_BASELINE.md
- docs/adr/0032-ubuntu-nuc-deployment-foundation.md
- docs/adr/0052-automated-catalog-backup-retention-and-restore-verification.md
- deploy/ubuntu/README.md
- deploy/ubuntu/fn-production-env-deploy
- deploy/ubuntu/production_ai_deploy.py
- deploy/systemd/framenest.service
- scripts/operator/network/framenest_nuc_worker_gate.fish
- relevant deployment/operator contract tests

Repository and containment gate:

1. Do not modify, fetch, checkout, clean, reset, stash, or otherwise mutate the
   canonical owner checkout.
2. If the exact contained implementation path already exists, stop and report;
   do not delete or reuse it.
3. Clone public FrameNest recursively into the exact contained path.
4. Verify:
   - origin identity;
   - public refs/heads/main equals the required baseline;
   - clone HEAD equals the required baseline;
   - .ap equals the required gitlink;
   - superproject and submodule are clean.
5. Create only the named implementation branch.
6. Stop before mutation on any mismatch or unexplained divergence.

Goal:

Implement one discoverable, tested, repository-native routine immutable Ubuntu
NUC release-update contract. Future Orchestrators and Workers must use it
instead of reconstructing deployment commands, probing generic PATH locations,
or confusing initial uv bootstrap with routine Poetry release updates.

Accepted exact NUC tooling:

- Poetry:
  /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
- CPython:
  /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
- uv was used only for initial pinned CPython provisioning and later explicit
  tooling maintenance. Routine release updates must not invoke uv or require
  uv on PATH.
- Release root:
  /opt/framenest/releases/<40-hex-SHA>
- Active reference:
  /opt/framenest/current
- Production environment:
  /etc/framenest/framenest.env
- Service:
  framenest.service
- Service identity:
  framenest:framenest

User-facing interface:

Implement exactly:

- deploy/ubuntu/framenest-release
- deploy/ubuntu/framenest_release.py

`framenest-release` is the single Fish-compatible operator entry point. It
resolves the repository root and invokes the repository `.venv/bin/python`.
The Python engine must remain compatible with Ubuntu system Python 3.12 for its
private transferred remote mode and use only the standard library.

Public CLI:

deploy/ubuntu/framenest-release status [transport arguments]
deploy/ubuntu/framenest-release check --release <40-hex-SHA> [transport arguments]
deploy/ubuntu/framenest-release deploy --release <40-hex-SHA> --yes [transport arguments]
deploy/ubuntu/framenest-release rollback --release <40-hex-SHA> --yes [transport arguments]

Transport arguments:
- --target
- --user
- --identity

Allowed public-safe fallbacks:
- FRAMENEST_NUC_SSH_TARGET
- FRAMENEST_NUC_SSH_USER
- FRAMENEST_NUC_SSH_IDENTITY

Do not add:
- --no-auto-check
- --no-backup
- --no-readiness
- arbitrary --env
- arbitrary remote commands
- a migration bypass
- automatic tooling installation
- automatic uv use

`status` and `check` are repository-, database-, service-, and host-state
read-only. Temporary local probe state is allowed only under an exact owned
temporary directory and must be cleaned. They must not transfer a helper,
create a remote file, refresh sudo, change a timestamp, or transition into
deployment automatically.

`deploy` must re-run all applicable check gates. `--yes` prevents accidental
execution but is not represented as AP or Cooperator authority.

Core source and public gates:

- Require a full lowercase 40-hex commit.
- Require local HEAD to equal the requested release.
- Require superproject and .ap worktrees to be clean.
- Require public refs/heads/main to equal the requested release.
- Require the local .ap HEAD and the release gitlink to be identical.
- Never accept an abbreviated, dirty, unpublished, moving, or ambiguous source.
- Never modify the canonical checkout.

Release artifact:

- Build one exact superproject archive from the selected commit.
- Build one separate exact AP archive from the gitlink pinned by that commit.
- Never follow AP main.
- Hash both archive byte streams locally.
- Transfer exact bytes only during deploy.
- Verify both hashes remotely before extraction.
- Validate every archive member before extraction:
  reject absolute paths, `..`, path escape, devices, unsafe links, or any
  member outside its designated root.
- Materialize pinned AP content under `<release>/.ap/`.
- The deployed immutable release intentionally contains no `.git` metadata.
- Write:
  - `.framenest-release-sha`
  - `.framenest-release-manifest.json`
- The manifest must contain only public-safe deterministic provenance,
  including FrameNest release SHA, AP pin, and both transferred archive hashes.
- `status` and future probes must use the marker/manifest, never
  `git -C /opt/framenest/current`.

Routine preparation:

- Target release and its exact staging path must both be absent.
- Never overwrite or reuse a partial target.
- Verify sufficient capacity.
- Use an exact staging directory below `/opt/framenest/releases/`.
- Write exact deployment-local `poetry.toml`:

  [virtualenvs]
  in-project = true

- Use the exact accepted Poetry and CPython paths.
- Run:
  - poetry check --lock
  - poetry env use <exact tooling CPython>
  - poetry install --only main --no-interaction --no-ansi
- Preserve and compare the committed poetry.lock hash; deployment must never
  update it.
- Create a release-local `.venv`.
- Make the completed source and `.venv` root-controlled and non-writable by
  the service account.
- Rename staging to the final release only after every preparation gate passes.
- Do not read, copy, print, replace, or reconstruct production secrets.
- Do not replace `/etc/framenest/framenest.env`.

Backup and schema boundary:

- Read sanitized current backup status using the accepted service-account
  operator contract.
- `check` requires `restore_readiness=ready`.
- `deploy` must run one fresh scheduled create/verify/disposable-restore
  checkpoint before cutover and require successful terminal evidence.
- The first implementation supports same-schema routine updates only.
- Compare production database revision with the packaged target head.
- Any schema difference stops before cutover with a sanitized
  `migration-required` result.
- Never run `framenest-db migrate`.
- Never hide migration authority in the helper.

Remote and privilege boundary:

- Mirror the strict existing SSH settings:
  BatchMode=yes, RequestTTY=no, StrictHostKeyChecking=yes,
  IdentitiesOnly=yes, ForwardAgent=no, ClearAllForwardings=yes,
  bounded timeout and liveness settings.
- Reuse the GPG SSH-agent socket safely when available, consistent with the
  existing Worker gate.
- Never receive, print, store, or transmit a password.
- Privileged remote phases use only `sudo -n`.
- The Cooperator establishes the sudo timestamp outside the helper.
- No user-supplied remote command is accepted.
- For deploy/rollback, transfer the exact Python engine to an exact temporary
  remote path, verify its SHA-256, and execute only its private fixed remote
  mode with validated scalar arguments.
- The read-only `status` and `check` paths use only fixed, tested commands and
  create no remote state.
- Preserve the first causal error.
- At terminal handling, invalidate the Cooperator's sudo timestamp through the
  exact supported route when the session remains available. If the session is
  lost first, report privilege release as unknown rather than fabricating PASS.

Cutover:

- Capture and verify the exact previous release.
- Require target readiness under:
  sudo -n -u framenest --chdir=<target-release>
  env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env ...
- Atomically replace `/opt/framenest/current` by creating a new symlink and
  renaming it over the active symlink.
- Restart only framenest.service and exactly once after all pre-cutover gates.
- Verify:
  - active symlink and release manifest;
  - service active state;
  - database readiness;
  - release-local production executable;
  - health through `framenest-production check-health`, which supports the
    accepted Tailscale UDS ingress;
  - expected service working directory;
  - bounded sanitized recent logs;
  - no secret, authorization header, private path, or media filename leakage.

Rollback:

- Automatic rollback is required after a post-switch failure.
- Restore the captured previous release with the same atomic symlink method.
- Run previous-release readiness.
- Restart framenest.service once for rollback.
- Verify health and active release.
- Manual rollback accepts only a full SHA for an already complete release
  under `/opt/framenest/releases/<SHA>`.
- Never reference `/opt/framenest/rollback`.
- Distinguish deployment failure, rollback success, rollback failure,
  readiness timeout, terminal service failure, cleanup failure, and unknown
  privilege-release state.

Concurrency, recovery, and cleanup:

- Use exact local and remote locks.
- Existing lock or recovery state fails closed.
- Use exact staging and temporary paths; no wildcard deletion.
- A partial target is never deployable.
- On successful preparation, final release publication is atomic.
- On pre-cutover failure, remove only exact owned temporary state when safely
  proven.
- On ambiguous/interrupted state, retain bounded recovery evidence and provide
  an exact operator recovery instruction; never guess or broadly clean.
- A fully prepared target may remain after failed cutover for diagnosis but
  must not be reported active.
- Cleanup failure must not overwrite the first causal result.

Durable documentation:

1. Add a concise always-read section outside the managed AP block in AGENTS.md:
   - name `deploy/ubuntu/framenest-release` as the sole routine NUC update
     entry point;
   - require `status`/`check` before deployment;
   - record the exact tooling paths;
   - state uv is bootstrap/maintenance-only;
   - state deployed releases have no `.git` and provenance comes from
     `.framenest-release-manifest.json`;
   - prohibit improvised routine deployment commands.

2. Add ADR-0060:
   `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`
   and update the ADR index.

3. Update docs/UBUNTU_NUC_DEPLOYMENT.md:
   - separate initial host/tool bootstrap from routine immutable updates;
   - document the canonical helper and modes;
   - document same-schema limitation, checkpoint, cutover, rollback, recovery,
     and privilege release.

4. Update deploy/ubuntu/README.md so it no longer claims the directory avoids
   tested host-mutating release automation.

5. Keep docs/NUC_HOST_BASELINE.md historical. Add at most a cross-reference;
   do not rewrite its old observations.

6. Reconcile moving production-state claims in README.md, PRODUCT.md,
   SERVER.md, and ROADMAP.md:
   - do not replace one soon-stale “current production SHA” with another;
   - explain that public main and production may differ;
   - make authenticated runtime `framenest-release status` the canonical
     mutable production readback;
   - preserve genuinely historical SHA evidence as dated history;
   - do not claim the new helper is deployed before live deployment evidence.

7. Do not modify docs/AP_UPGRADE_OBSERVATIONS.md or any `.ap` content.

Allowed repository paths:

- AGENTS.md
- README.md
- PRODUCT.md
- SERVER.md
- ROADMAP.md
- deploy/ubuntu/framenest-release
- deploy/ubuntu/framenest_release.py
- deploy/ubuntu/README.md
- docs/UBUNTU_NUC_DEPLOYMENT.md
- docs/NUC_HOST_BASELINE.md
- docs/adr/README.md
- docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md
- tests/contract/test_nuc_release_source_contract.py
- tests/contract/test_nuc_release_remote_contract.py
- tests/contract/test_nuc_release_docs.py

No other path may be changed.

Validation:

- Use the canonical existing CPython 3.13 project `.venv`; never system
  Python 3.14.
- For the contained clone, execute tests with exact-source provenance through
  the accepted existing interpreter and `PYTHONPATH=<contained-clone>/src`.
- Do not create, delete, replace, or repair a `.venv`.
- Do not run Poetry environment mutation commands on the development machine.
- Tests use fake runners, synthetic archives, and temporary directories only.
- No test may contact the NUC, invoke real SSH/sudo/systemd, inspect secrets,
  or access private media.
- Cover:
  - status/check positive paths;
  - exact public-main and AP-pin gates;
  - dirty/unpublished source;
  - missing or mismatched tooling;
  - both archive hashes;
  - AP materialization;
  - unsafe archive members;
  - existing target/staging/lock/recovery state;
  - insufficient capacity;
  - backup not ready and fresh checkpoint failure;
  - schema mismatch;
  - Poetry/lock failure;
  - target readiness failure;
  - atomic release publication and cutover;
  - post-switch failure with successful rollback;
  - rollback failure;
  - cleanup failure;
  - first-causal-error preservation;
  - sanitized output;
  - documentation parity.
- Keep tests split by responsibility; do not create another giant monolithic
  contract file.
- Run focused new tests.
- Run affected existing NUC/deployment/operator tests.
- Run the full Python suite.
- Run applicable JavaScript contract tests.
- Run Fish syntax validation and Python compilation.
- Inspect the exact diff and Git status.

Excluded:

- Any live NUC, SSH, sudo, systemd, service, database, backup, symlink, network,
  storage, Tailscale, firewall, or host mutation.
- Real deployment or rollback.
- Secrets or private media.
- Dependency or lockfile changes.
- Application feature code.
- Alembic migrations.
- AP protocol or AP ledger changes.
- Off-device backup configuration.
- Push, publication, merge, rebase, tag, or logical-whole closure.

Git authority:

- The contained clone and named branch are authorized.
- Stage only the exact allowed changed paths.
- One normal commit is authorized after all required validation passes.
- Commit subject:
  feat: automate immutable NUC release updates
- No push is authorized.
- No force operation is authorized.

Evidence tier:
- Repository implementation: E2 with security/privilege-sensitive future use.
- Implementation evidence is non-independent.
- A fresh independent audit is required before publication or any live NUC use.
- The later live deployment remains a separate E3 task with fresh preflight,
  explicit Cooperator approval, checkpoint/rollback, and production acceptance.

Stopping conditions:

- Any repository/public/AP gate fails.
- The contained path already exists.
- Required behavior needs a path outside the allowlist.
- A safe same-schema boundary cannot be preserved.
- Tests would require real host access or secrets.
- The helper would need a bypass flag, implicit migration, tooling install,
  unbounded shell command, unsafe extraction, broad cleanup, or unproven
  rollback.
- Required validation returns non-zero.
- Any unrelated owner work is encountered.

Terminal report:

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Then include:

Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 02
Worker exchange ordinal: 01
Standard terminal status: PASS | PARTIAL | BLOCKED
Phase-qualified result: implementation-PASS | implementation-PARTIAL | implementation-BLOCKED
Result artifact or commit: <exact commit or none>
Result evidence: <concise evidence>
Logical-whole closure: not-closed
Report justification: new-mutation | new-evidence | new-material-risk
Authority expiry: all Worker 02 exchange 01 implementation authority expired at this report

Also report:
- start/end commit;
- exact changed paths;
- focused/full validation with exit codes;
- archive/AP provenance behavior;
- rollback and negative-path evidence;
- Git commit result;
- deviations, residual risks, and one proposed next step.

Do not implement beyond the exact contract and do not deploy.
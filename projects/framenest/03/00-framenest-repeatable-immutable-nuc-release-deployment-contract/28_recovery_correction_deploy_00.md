# FrameNest — one-session NUC recovery, causal correction, and successful deploy

🆕 **PROMPT FOR FRESH WORKER 28 • HIGH REASONING**

**Native Plan Mode: OFF.** Work directly and keep a short internal checklist.
Do not spawn subagents. Do not ask for another Worker. This is one continuous,
bounded recovery/correction/deployment session on Michal's test NUC.

## AP identity

```text
Role: WORKER
Logical whole identity: framenest-repeatable-immutable-nuc-release-deployment-contract
Worker session ordinal: 28
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: combined test-NUC recovery/correction/deployment
Task identity: FN-NUC-RELEASE-RECOVER-CORRECT-DEPLOY-28
Phase: exceptional combined recovery + correction + publication + deployment
Reasoning class: High; escalation above High is prohibited
```

The COOPERATOR explicitly authorizes this combined envelope because 27 narrowly
split sessions produced an orchestration loop while the live test NUC remained
healthy on its previous release. Phase separation must not create another
handoff. Successful completion may still be described as non-independent; that
is not a reason to stop before the test NUC is recovered and the corrected
release is deployed.

Read `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, the pinned AP Worker
documents, `docs/UBUNTU_NUC_DEPLOYMENT.md`, and ADR-0060. Then execute. Do not
rewrite or summarize the AP protocol.

## Required outcome

Within this one session:

1. preserve the healthy live release and diagnose the first causal failure of
   Worker 27 before deleting its recovery evidence;
2. correct the repository-owned release helper when the evidence confirms a
   helper defect;
3. run only proportional focused verification;
4. create one normal initial correction commit and publish it to public `main`
   by an ordinary non-force fast-forward, if a correction is required; one
   additional correction commit/push is permitted only for a distinct causal
   defect first exposed by the live retry;
5. remove only the exactly identified stale Worker 27 recovery paths;
6. deploy the resulting exact public SHA once, with at most one causal
   same-session correction-and-retry if new evidence proves a distinct defect;
7. prove the new release is current, healthy, restore-ready, and free of
   staging-path contamination; then release sudo once at the very end.

Do not return `PARTIAL` merely because a source correction, exact cleanup, Git
commit, publication, or deploy is needed: all are explicitly authorized here.
Stop only for a real safety blocker named under **Hard stop conditions**.

## Binding starting evidence

```text
Repository: /home/agile/Projects/framenest
Public repository: https://github.com/cisarik/framenest.git
Published deployment candidate: f5fbdce5669997f15c28ed6ffdad4cda849df4ee
Candidate parent: 43c9849a1ff3449a3c06585571c17439ecff9025
Candidate AP pin: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
Live current release after Worker 27: 148b6c2012809944262399c1a166e85082606fbf
Live service after Worker 27: active
Catalog revision after Worker 27: 0028
Backup restore readiness after Worker 27: ready
Worker 27 deploy result: EXIT_ROLLBACK 18 after approximately 37 seconds
Failure window: 2026-08-15T20:29:45Z through 2026-08-15T20:30:22Z
```

Worker 27 left:

```text
/run/framenest-release-deploy/
  ap.tar
  framenest_release.py
  previous-release
  superproject.tar

/opt/framenest/releases/f5fbdce5669997f15c28ed6ffdad4cda849df4ee
```

The final `f5fbdce...` host tree is unactivated recovery material, not current
and not a rollback target. Its staging sibling was absent. Do not trust any of
these facts without a fresh bounded re-read, but do not rediscover already
settled Poetry or runtime architecture.

The project uses Poetry 2.4.1 and CPython 3.13.14 on the NUC. `uv` is not the
dependency manager. Do not run `uv`, `pip install`, rebuild the canonical
development `.venv`, or create an isolated worktree. Direct work in the
authorized canonical checkout is permitted; preserve all owner untracked paths.

## High-confidence code defects to verify, not blindly assume

At public `f5fbdce...`:

- `subprocess_runner()` discards the subprocess return code and stderr and
  raises only `ReleaseError("command failed")`; the real failing stage is lost.
- `_verify_cutover()` performs one immediate `check-health` after
  `systemctl restart`; `EXIT_READINESS_TIMEOUT = 17` exists but no bounded
  readiness polling uses it.
- rollback calls the same immediate verification, so one ordinary startup race
  can be misreported first as deployment failure and then as rollback failure,
  even when the previous release becomes healthy seconds later.
- `/opt/framenest/current.next` was not reported among Worker 27's probes. A
  stale exact symlink could make both forward switch and rollback switch fail.

The older repository-owned `deploy/ubuntu/production_ai_deploy.py` already has
a 30-second bounded readiness loop, terminal-state classification, timeout
classification, and the same readiness behavior during rollback. Reuse its
accepted semantics where appropriate instead of inventing a second policy.

These are evidence-led hypotheses. Identify the actual first cause from the NUC
before choosing the smallest correction.

## Authority

You may:

- use the configured `framenest-nuc` SSH host/IdentityFile and attach the GPG
  agent SSH socket when `SSH_AUTH_SOCK` is absent;
- use noninteractive remote `sudo -n` after the COOPERATOR-established global
  timestamp; never use `sudo -S`, handle a password, or run `sudo -v`;
- read bounded service state, unit properties, the exact failure-window journal,
  exact release markers, exact venv metadata, and exact recovery paths;
- edit only:
  - `deploy/ubuntu/framenest_release.py`
  - `tests/contract/test_nuc_release_source_contract.py`
  - `tests/contract/test_nuc_release_remote_contract.py`
  - `tests/contract/test_nuc_release_docs.py`
  - `docs/adr/0060-repeatable-immutable-nuc-release-update-contract.md`
  - `docs/UBUNTU_NUC_DEPLOYMENT.md`
- create one normal initial correction commit on a clearly named local fix
  branch and, only under the bounded retry rule, one additional correction
  commit;
- push only an exact tested correction SHA to `refs/heads/main`, with at most two
  ordinary non-force fast-forward updates total under the bounded retry rule;
  do not touch local `main`;
- delete only the exact, re-identified Worker 27 recovery files/tree and an
  exact stale `/opt/framenest/current.next` when it is proven not to be current;
- run the repository release helper against the exact corrected public SHA;
- switch `/opt/framenest/current`, restart `framenest.service`, and perform the
  helper's automatic rollback if genuinely required.

Do not change `.ap`, the AP pin, catalog contents, Tailscale, Mullvad, firewall,
Serve configuration, accounts, identity mapping, source media, off-device
backup policy, dependencies, system packages, systemd source, or sudoers.
Do not write Meta. Do not close the logical whole.

## Execution

### 1. Preflight without ceremony

- Verify canonical tracked cleanliness, current branch/HEAD, AP pin, public
  `main`, origin identity, and absence of an active Git operation.
- Preserve owner untracked paths; do not enumerate their contents.
- If `SSH_AUTH_SOCK` is absent, attach `gpgconf --list-dirs agent-ssh-socket`
  to this Worker process and prove one BatchMode SSH command succeeds.
- Require remote `sudo -n true` exit 0. If it fails, stop as `BLOCKED` without
  invalidating anything; the COOPERATOR must establish the timestamp outside
  the Worker.
- Do **not** run `sudo -K` between diagnosis, cleanup, correction, and deploy.

### 2. Diagnose before deleting evidence

Re-identify exactly:

- `/opt/framenest/current` and the live release directory;
- live service state, `ActiveState`, `SubState`, `Result`, `ExecMainStatus`, and
  configured `WorkingDirectory`;
- the exact four names under `/run/framenest-release-deploy` and the exact
  content of `previous-release`;
- type and target of `/opt/framenest/current.next`, if it exists;
- `f5fbdce...` final tree identity, manifest/SHA marker, required console-script
  shebangs, and only `.pth`/`direct_url.json` occurrences of `.staging`;
- the bounded service journal from `2026-08-15 20:29:40 UTC` through
  `2026-08-15 20:30:35 UTC`.

Do not paste raw journal text into the report. Extract only the first causal
stage and sanitized error class. Do not expose secrets, private network values,
database paths, media filenames, or raw environment values.

Run the unpublished target's `framenest-production check-database-ready` and
`check-health` through the established service-account/environment contract.
The latter speaks to the currently live UDS and proves CLI/config compatibility,
not that the new server process was active; classify it honestly.

Determine whether the first forward failure was:

- pre-cutover target readiness;
- atomic-switch/current.next;
- systemd restart;
- immediate service readiness race;
- terminal service failure;
- working-directory mismatch;
- log-sanitization gate;
- or another exact stage.

### 3. Make the smallest causal correction

If the evidence confirms the readiness race, implement one bounded readiness
contract for both deploy and rollback:

- maximum 30 seconds;
- one-second polling;
- retry transient `activating`, socket-not-ready, and health-not-ready states;
- fail immediately on a terminal systemd state;
- return `EXIT_READINESS_TIMEOUT` only at the deadline;
- preserve a distinct rollback-stage result;
- never print raw stderr, argv containing host details, or secrets.

Also replace opaque failure loss with a stable, sanitized phase/exit
classification sufficient to identify whether `restart`, readiness, switch, or
rollback failed. Raw stderr may be used locally for diagnosis but must not be
blindly emitted.

If `/opt/framenest/current.next` is causal, make atomic switch idempotent for an
exact stale temporary symlink without weakening path validation or using a broad
delete. Do not add this change merely speculatively.

Add only causal regression coverage. At most:

- transient health failures followed by readiness;
- readiness deadline expiry;
- the same bounded behavior during rollback;
- exact stale `current.next` behavior, only if observed;
- stable sanitized first-stage classification.

Do not generate a broad matrix. Do not rewrite existing tests. Do not run the
full Python suite by default.

### 4. Proportional verification and publication

Use the canonical Poetry-owned interpreter and exact canonical source:

```text
PYTHONPATH=/home/agile/Projects/framenest/src \
  /home/agile/Projects/framenest/.venv/bin/python -m pytest \
  tests/contract/test_nuc_release_source_contract.py \
  tests/contract/test_nuc_release_remote_contract.py \
  tests/contract/test_nuc_release_docs.py \
  -q -p no:cacheprovider
```

Also run Python compile validation and Fish no-execute validation for the thin
entry point. Run another test only when an actual changed import or documented
contract requires it. Do not run the full suite to manufacture confidence.

Review the diff for exact scope, create one normal initial commit, prove it is a
direct descendant of public `f5fbdce...`, and push exactly:

```text
<new-full-sha>:refs/heads/main
```

Use no force, tag, PR, merge, rebase, amend, or second ref. Perform a
credential-free public readback. The public readback SHA becomes `TARGET_SHA`.
If host evidence proves no source correction is needed, keep
`TARGET_SHA=f5fbdce...` and create no empty commit.

### 5. Exact recovery

Immediately before deletion, prove live current still resolves to
`148b6c...`, that its directory exists and service is active, and that the
unpublished `f5fbdce...` tree is not current.

Remove only:

```text
/run/framenest-release-deploy/framenest_release.py
/run/framenest-release-deploy/superproject.tar
/run/framenest-release-deploy/ap.tar
/run/framenest-release-deploy/previous-release
/run/framenest-release-deploy
/opt/framenest/releases/f5fbdce5669997f15c28ed6ffdad4cda849df4ee
```

Remove `/opt/framenest/current.next` only if it exists as the exact stale
temporary symlink and is not `/opt/framenest/current`. Use no glob, no broad
`find /opt/framenest/releases`, and no recursive delete of the lock directory.
Afterward prove the exact paths are absent and the old live release remains.

### 6. Deploy and finish in this session

Using the corrected public `TARGET_SHA`:

1. run `framenest-release status`;
2. run `framenest-release check --release "$TARGET_SHA"`;
3. require `sudo -n true` still succeeds;
4. run exactly one `framenest-release deploy --release "$TARGET_SHA" --yes`;
5. run post-deploy status and the acceptance probes below.

If this deploy fails for a newly exposed, exact, correctable helper defect, do
not request Worker 29. Preserve evidence, make at most one smallest causal
same-session correction, focused-test it, publish one additional ordinary
fast-forward, recover only that failed attempt's exactly identified leftovers,
and retry once. Blind retry is prohibited. More than two deploy invocations in
this session is prohibited.

### 7. Acceptance evidence

Success requires all of:

- public `main == TARGET_SHA`;
- `/opt/framenest/current == /opt/framenest/releases/TARGET_SHA`;
- release manifest and SHA marker match `TARGET_SHA` and the pinned AP gitlink;
- `framenest.service` is active after bounded readiness;
- configured working directory remains `/opt/framenest/current`;
- database current/head revision is `0028`/`0028`;
- backup restore readiness is `ready` and the fresh pre-cutover checkpoint
  succeeded;
- release-local `check-database-ready` and `check-health` succeed;
- all required console-script shebangs name the final `TARGET_SHA` interpreter;
- no `.pth` or `direct_url.json` under the live venv contains `.staging`;
- `/run/framenest-release-deploy`, `/opt/framenest/current.next`, and failed
  staging/final leftovers are absent;
- the previous `148b6c...` release directory remains available as rollback
  material;
- no migration, AP-pin mutation, dependency change, or unrelated host mutation
  occurred.

Only after all evidence is captured, run remote `sudo -K` once and prove
`sudo -n true` no longer succeeds.

## Hard stop conditions

Stop without improvising only if:

- SSH cannot be established after one GPG-agent-socket attachment attempt;
- the COOPERATOR's `sudo -n` timestamp is not valid at the initial gate;
- the live old release is not active/healthy or its identity cannot be proven;
- catalog backup restore readiness is not `ready`;
- current database revision differs from target head;
- an exact deletion target cannot be proven not-current;
- public `main` changed to an unrelated non-descendant during this session;
- a destructive action outside this prompt would be required.

A correctable release-helper defect, focused-test failure caused by your patch,
or exact failed-deploy leftover is **not** a handoff condition; fix it within the
bounded retry budget.

## Cost and loop controls

- One Worker, one session, no subagents, no new Orchestrator.
- No full suite unless an actual change outside the release helper forces it.
- No speculative tests; one causal regression per proven defect.
- No `uv`, environment reconstruction, AP upgrade, browser work, or Meta work.
- No repeated narrative. Report evidence and the first cause once.
- Do not treat more Workers, more tests, or longer reasoning as quality.

## Terminal report

Return one concise report beginning exactly:

```markdown
### Report for ORCHESTRATOR_CHAT
```

Include:

```text
Logical whole identity
Worker session ordinal: 28
Worker exchange ordinal: 01
Standard terminal status
Phase-qualified result
First causal failure of Worker 27
Correction commit(s), if any
Public TARGET_SHA readback
Focused verification counts
Exact recovered paths
Pre/post live release identity
Service/database/backup/health evidence
Deploy invocation count
Residual risks
Logical-whole closure: not-closed
Report justification
Authority expiry
```

Do not write the report into Meta. Michal will manually archive this exact
prompt as `28_recovery_correction_deploy_00.md` together with the returned
`28_report_00.md` only after the report exists.

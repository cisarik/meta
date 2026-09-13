# ContextDesk — deploy and independently re-audit the G3 ACL re-probe correction

ROLE: WORKER

Use a genuinely fresh Worker session. Session 26 authority is expired.
Do not dispatch subagents. Speak Slovak to the Cooperator; write the
terminal report in English.

This is file-based delivery. The Cooperator must not copy/paste this prompt,
manually compose a prompt file, or manually compose a report file. The Worker
is explicitly authorized to persist the exact received prompt bytes and its
own terminal report into the META trace under the exact destinations below.
The Worker must not commit or push META. This Worker may mutate only the one
explicitly named host udev rule and may perform the narrowly targeted udev
reload/trigger operations defined below. No broker installation or live
input operation is authorized.

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 27
Worker exchange ordinal: 00
Worker session target: fresh-worker-session
Worker-session profile: Fresh Independent G3 Deployment and Security Re-audit Worker
Phase: deployment
Task identity: CONTEXTDESK-G3-ACL-REPROBE-DEPLOY-REAUDIT
Native planning mode: not-used
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; advisory only
Evidence tier: E3
Evidence tier basis: privileged deployment of a security-boundary udev
correction followed by independent immediate and delayed host ACL readback
Activated stricter profile: INFOSEC.md
Security route: R6 correction followed by a fresh independent re-audit
Acceptance independence: required-separate-fresh-worker

The logical whole remains open. Sessions 16, 19, 22, 23, and 24 are accepted
named slices only. Session 25 is a deployment-PARTIAL: remove and immediate
rollback were evidenced, candidate installation was skipped, and the target
host ended with the measured G3 session-user ACL hole open. Session 26 is an
implementation-PASS: the source correction was published as
ca6052e816d4884ddeac9d7499a42c2aca089e7e, but it did not mutate the host and
did not self-certify the correction. Do not repeat or broaden those sessions.

## Single bounded outcome

Deploy the exact late ACL-guard rule from product commit
ca6052e816d4884ddeac9d7499a42c2aca089e7e on the authorized target host and
perform one independent, bounded G3 re-audit across an immediate and a
delayed readback.

The measurable outcome is a truthful result for finding
G3-ACL-REPROBE-01:

1. The corrected rule is installed byte-for-byte at the exact target path,
   with the expected root ownership and mode.
2. The narrowly targeted add/change re-probe is applied only to G213 event
   nodes, /dev/port, and /dev/i2c-*.
3. At both immediate and delayed readback, the session user has no extended
   ACL on those three guarded classes.
4. G213 hidraw session access remains available, /dev/uinput retains its
   existing session and broker ACLs, base owner/group/mode properties remain
   unchanged, and input-remapper semantic state is unchanged.

A successful result is limited to this deployed ACL correction and its fresh
independent re-audit. It does not close the logical whole or establish any
broader G3, G4, M2, coexistence, or production claim.

## Finding and security boundary

Finding identity: G3-ACL-REPROBE-01

Session 25 established reproduced-dynamic evidence that removing and then
rolling back the previous ContextDesk files left or reintroduced a
session-user POSIX ACL on G213 event nodes, /dev/port, and /dev/i2c-* after a
delayed udev re-probe. Removing the uaccess tag did not revoke an already
materialized POSIX ACL. The hidraw lighting ACL and the uinput session/broker
ACLs were intended to remain.

Session 26 published the source correction:

packaging/udev/99-contextdeck-input-acl-guard.rules

It is a late rule, ordered after 73-seat-late.rules, matching only G213 event
nodes, /dev/port, and /dev/i2c-* on add/change and removing extended ACL
entries with the narrowly scoped rule action. It must not match G213 hidraw
or /dev/uinput. The existing 61-, 62-, and 99-contextdeck-broker-uinput.rules
files remain semantically unchanged.

Do not call this a general OpenRGB vulnerability. Do not claim more than the
bounded target-host evidence. The report must not include host identity,
addresses, node numbers, serials, raw ACL dumps, UIDs/GIDs, or private paths.

## Exact product, AP, and META candidates

Canonical product:

- Remote: https://github.com/cisarik/contextdesk
- Branch: main
- Exact product candidate:
  ca6052e816d4884ddeac9d7499a42c2aca089e7e
- Required product parent/baseline:
  ab10491c49d0b6574b6953a02935a4664c39d7c2
- The candidate must contain the Session 26 allowlisted source/test/docs
  correction. This Worker has no product commit or push authority.

Required AP:

- Gitlink and checkout:
  0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
- ./.ap/ap doctor must pass.

Public META:

- Remote: https://github.com/cisarik/meta.git
- Trace:
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
- Expected public tip at this routing point:
  53a0c26e098599932498c017fe4525d92d9ccd61
- Accept a later public descendant only if ancestry is verifiable and it
  contains the current handoff plus the exact public Session 24, Session 25,
  and Session 26 prompt/report pairs.
- Session 25 ancestor:
  5077bd92c65749a33fd537a14dda8ed777bb46f3
- Current handoff:
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/00_handout_02.md
- Required prior files include:
  24_acceptance_00.md, 24_report_00.md,
  25_deployment_00.md, 25_report_00.md,
  26_implementation_00.md, and 26_report_00.md.

Do not silently retarget the product, branch, candidate, AP, META identity,
or target host. If any public identity, ancestry, handoff, or required pair
contradicts this prompt, stop before host mutation and report BLOCKED.

## Relevant installed identities and pre-state

The target host is expected to remain in the Session 25 post-rollback state
until this Worker installs the new rule. Verify, without exposing private
values in the report:

- Installed broker executable SHA-256:
  8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6
- Installed broker unit SHA-256:
  286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503
- Installed sleep hook SHA-256:
  91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e
- Existing installed 61-, 62-, and 99-contextdeck-broker-uinput.rules are
  regular root-owned files with the expected modes and are byte-identical to
  the matching source files in the candidate.
- The broker unit is static, inactive, dead, has MainPID=0, is not enabled,
  and has no pending daemon reload. No broker process, socket, runtime
  directory, virtual device, or trial timer exists.
- The exact contextdeck-broker system identity is present as the expected
  nologin system account/group, has no unexpected members or processes, and
  is not the session user.
- input-remapper remains enabled/active/running; record only a semantic
  before/after equality and do not inspect or record configuration contents.
- Before this Worker, the new candidate rule is absent from
  /etc/udev/rules.d/99-contextdeck-input-acl-guard.rules. If it is present,
  regardless of whether its bytes appear correct, stop as an unexplained
  pre-state and report BLOCKED. Do not overwrite it.
- Before installation, G213 event nodes, /dev/port, and /dev/i2c-* have the
  documented Session 25 residual session-user ACL state; G213 hidraw access
  remains available; /dev/uinput retains its existing session and broker
  ACLs. If the pre-state differs, stop without repair and classify the
  discrepancy separately.

The expected residual G3 state is a reason for this deployment, not evidence
that the correction has already worked. Never call the host secure before the
post-deployment delayed readback passes.

## Out of scope

Do not:

- install, remove, rollback, or replace the broker executable, systemd unit,
  sleep hook, sysusers file, 61- rule, 62- rule, or uinput rule;
- start, stop, enable, disable, restart, reload, lease, ARM, DISARM, connect
  to, or inspect the runtime of contextdeck-broker.service except for the
  read-only preflight/final state checks;
- run systemd-sysusers, systemctl daemon-reload, or any broker operation;
- open G213 event nodes, /dev/uinput, /dev/port, /dev/i2c-*, or hidraw;
- inject input, grab a physical source, perform pass-through, test LEDs, run
  OpenRGB, or exercise the control matrix;
- change, stop, restart, enable, disable, reconfigure, or inspect the
  contents of input-remapper configuration;
- run direct setfacl commands on live device nodes. The only permitted ACL
  effect is the bounded RUN action of the newly installed rule when invoked
  by the exact targeted add/change re-probe;
- run a system-wide udev trigger, broad wildcard trigger, or unrelated udev
  policy operation;
- test suspend, resume, hibernate, hybrid sleep, power actions, autostart,
  production readiness, general coexistence, or any other G4 slice;
- modify product source, tests, documentation, AP, META history, handoff,
  roadmap, dependencies, or any unrelated host policy;
- create a product commit, push product, create a branch, rewrite history,
  or commit/push META.

No raw input, raw event lines, key names, scan values, control names/codes,
per-event timing, typed content, screenshots, serials, host addresses, host
keys, passwords, credentials, private checkout paths, private home paths,
private temporary paths, numeric UID/GID values, or unredacted command
transcripts may appear in the report or any durable trace.

## Recovery route boundary

This Worker is not authorized to open or grab a live input source, so an
external recovery route is not a precondition for this no-grab deployment.
If any necessary step would start, ARM, open, or grab a live source, stop
immediately and report BLOCKED; do not improvise a recovery procedure.

If a later prompt authorizes a live grab, exactly one independent route is
sufficient. The already-demonstrated SSH-from-another-device route may be
used with these precomputed emergency commands:

    sudo systemctl stop contextdeck-broker.service
    sudo systemctl status --no-pager contextdeck-broker.service

Do not require both SSH and a second keyboard. Do not run the emergency
commands as part of this normal G3 deployment path, because this prompt
authorizes no broker start or grab.

## Public-safe path allowlist

Read-only product/AP paths:

- AGENTS.md
- README.md
- ROADMAP.md
- CMakeLists.txt
- .ap/AP.md
- .ap/AP_ORCHESTRATOR.md
- .ap/PROMPT_CONTRACTS.md
- .ap/AP_WORKER.md
- .ap/INFOSEC.md
- docs/architecture.md
- docs/operations.md
- docs/testing-m2.md
- docs/hardware/g213-control-matrix.md
- docs/hardware/g213-zone-map.md
- packaging/udev/61-contextdeck-input-guard.rules
- packaging/udev/62-contextdeck-broker.rules
- packaging/udev/99-contextdeck-broker-uinput.rules
- packaging/udev/99-contextdeck-input-acl-guard.rules
- packaging/systemd/contextdeck-broker.service
- packaging/systemd/contextdeck-sleep.sh
- packaging/sysusers.d/contextdeck-broker.conf
- tests/unit/test_udev_policy.cpp
- tests/unit/test_sleep_hook.sh

Read-only META paths:

- current 00_handout_02.md;
- exact public Session 24, Session 25, and Session 26 prompt/report pairs;
- public history and changed-path summaries for the Session 25 and Session
  26 archival commits.

The only permitted durable META writes are these exact Worker-owned paths:

- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/27_deployment_00.md
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/27_report_00.md

The only permitted host policy mutation is:

- /etc/udev/rules.d/99-contextdeck-input-acl-guard.rules

Also permitted are a private, narrowly scoped temporary checkpoint for that
single target file, one udev rules reload, and narrowly targeted add/change
triggers for the three named guarded classes. Do not report the checkpoint
path. Do not mutate any other product, META, or host path.

## Read-only preflight and fail-closed gates

Before any host mutation:

1. Resolve a product inspection checkout and verify the canonical remote,
   branch, clean worktree, exact candidate commit, required parent, no Git
   locks or active operations, matching AP gitlink/checkout, and
   ./.ap/ap doctor PASS. Verify local HEAD, origin/main, and the public
   product main ref all equal ca6052e…; do not use a stale local object.

2. Resolve a META inspection checkout and verify that public origin/main is
   53a0c26… or a verifiable later descendant of 5077bd…. Verify ancestry,
   trace directory and parents, real-directory status, required handoff,
   exact Session 24/25/26 pairs, and the changed paths of the archival
   commits. Read the current 00_handout_02.md as authoritative. Do not
   silently use an older handoff or silently retarget after a contradiction.

3. Read the pinned AP contracts, INFOSEC.md, current handoff, Session 25
   deployment-PARTIAL report, and Session 26 implementation-PASS report.
   Read the candidate rule and the unchanged neighboring rules from the
   verified product commit. Confirm that the new rule is late, narrow, uses
   add/change, preserves base owner/group/mode, and excludes hidraw/uinput.

4. Run static udev syntax verification with name resolution disabled where
   supported on all four candidate ContextDesk udev files. Do not use a
   successful grep as a substitute. No full product build is required by
   this deployment prompt because Session 26 already published and tested
   the immutable correction; if the source identity or syntax does not
   verify, stop before host mutation.

5. Verify the host pre-state listed above using metadata and semantic service
   checks only. Do not open a device node. Capture the semantic
   input-remapper state before any mutation. Confirm the machine is not
   suspending or resuming. Confirm no live input source is grabbed.

6. Confirm the target rule is absent and create a private root-owned
   checkpoint recording that absence. Verify the checkpoint is not a
   symlink. If any precondition, identity, source hash, file type, owner,
   mode, service state, G3 preservation property, remapper state, target
   presence, or public ancestry differs, stop before host mutation and
   report BLOCKED with phase-qualified result not-applicable. Do not repair
   the unexplained state.

## Owner-executed deployment

The Cooperator owns privileged host commands. The Worker prepares short,
explicit, fail-closed blocks and waits for complete semantic output from
each block. Do not paste a large script or heredoc. Use exact target paths,
verified command paths, no broad globs, no password in chat, no sudo
keep-alive, and no model-dependent emergency action.

Use the AP owner-terminal lifecycle: the Cooperator authenticates with the
OS sudo prompt in the same reachable terminal, verifies noninteractive
authorization for the bounded block, runs the block, captures only semantic
markers and exit status, and releases the sudo timestamp after the block.
The Worker must never see or record credentials. If Worker-side sudo is
unavailable, use the authorized Cooperator-owned route; do not fabricate
privilege evidence.

### Install the one corrected rule

1. From the verified product candidate, install only
   packaging/udev/99-contextdeck-input-acl-guard.rules to
   /etc/udev/rules.d/99-contextdeck-input-acl-guard.rules as a regular
   root-owned file with mode 0644. Use a narrowly scoped, atomic or
   equivalent installation operation. Do not replace the three existing
   ContextDesk udev files.

2. Read back the installed file type, ownership, mode, and byte identity
   against the candidate source. If installation or identity verification
   fails, stop, retain the checkpoint, and report the failure. Do not retry
   with a broader command.

3. Reload the udev rules once. Do not reload systemd, restart any service,
   or invoke the broker.

### Apply the bounded re-probe

4. Use the current candidate documentation and verified device matchers to
   issue only the exact targeted add/change re-probe for:

   - G213 event nodes, matched by the device identity and event subsystem;
   - /dev/port;
   - /dev/i2c-*.

   Do not trigger hidraw, /dev/uinput, all input devices, all i2c devices,
   or the whole udev database. Do not use direct setfacl commands. Record
   only semantic trigger success and exit status; do not retain node paths.

5. Perform an immediate metadata-only G3 readback after the targeted
   re-probe. Then perform a delayed metadata-only readback after a bounded
   observation interval of at least 30 seconds, without another broad
   trigger. The delayed check is mandatory because Session 25 showed that a
   transient clean window is not sufficient.

6. At both readbacks verify semantically:

   - no session-user extended ACL on G213 event nodes;
   - no session-user extended ACL on /dev/port;
   - no session-user extended ACL on /dev/i2c-*;
   - G213 hidraw session access remains available;
   - /dev/uinput owner/group/mode and existing session and broker ACLs remain
     present; use metadata/access checks only and do not open or inject;
   - the unchanged three ContextDesk udev files remain byte-identical;
   - input-remapper enabled/active/running semantic state and configuration
     aggregate remain unchanged;
   - the broker remains static/inactive/dead with no runtime, process,
     socket, virtual device, or pending daemon reload.

If the immediate readback passes but the delayed readback fails, classify the
correction as not verified and do not call the finding closed. Do not repeat
udev/setfacl loops. Preserve the checkpoint and report the exact bounded
failure semantically.

If the new rule causes an unexpected preservation failure, do not invent a
repair or manually restore ACLs. Use the checkpoint only for a narrowly
scoped file rollback if that can be done without claiming host restoration;
otherwise retain the checkpoint and stop. Report rule state and host G3
state separately.

## Required evidence and classification

Use PASS with phase-qualified result deployment-PASS only if all of the
following are true:

- product, AP, and public META identities and ancestry passed;
- the target rule was absent at preflight and was installed exactly from
  ca6052e…;
- the one targeted reload and exact re-probe completed without broad scope;
- immediate and delayed readbacks both prove the three guarded classes have
  no session-user extended ACL;
- hidraw and uinput preservation properties pass at both readbacks;
- unchanged host service, identity, input-remapper, and no-runtime checks
  pass;
- no live source was opened or grabbed and no excluded operation occurred;
- the checkpoint was removed only after successful final readback;
- the report states that G3-ACL-REPROBE-01 is verified-closed only for this
  bounded deployed ACL scope and that broader G3/M2/G4 gates remain open.

Use PARTIAL with phase-qualified result deployment-PARTIAL when useful
deployment or audit evidence exists but a required install, delayed readback,
preservation, or final-state claim is incomplete. Use BLOCKED with
phase-qualified result not-applicable for a failed identity/precondition,
unexpected target presence, collision, unauthorized path, or any required
operation that would cross the no-grab boundary.

Never claim:

- whole M2 or whole G4 closure;
- production readiness or independent install/remove/rollback readiness;
- autostart, automatic ARM, automatic re-ARM, hibernate, or hybrid sleep;
- general input-remapper coexistence;
- physical keyboard safety, pass-through, LED return, or all-control fidelity
  from this no-grab deployment;
- that Session 25's remove/rollback evidence was candidate installation;
- that source correction alone fixed the host.

The report must contain exactly one line:

Logical-whole closure: not-closed

## Worker-owned prompt and report persistence

The Worker owns physical persistence of both exact exchange files. The
Cooperator must not copy/paste, reconstruct, rename, or manually save either
file.

Immediately after receiving this prompt and before consequential host work:

1. Resolve the Cooperator-provided or Worker-created META checkout for the
   public remote above.
2. Verify the exact trace directory, all parents, real-directory status,
   symlink status, and filename collisions.
3. Write the exact received prompt bytes to:

   projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/27_deployment_00.md

4. Read the file back completely and verify byte identity with the received
   prompt. If the destination exists with non-identical content, stop before
   host mutation and report the collision. Do not choose another filename.

After the bounded deployment and independent readbacks, write the complete
terminal report first to:

projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/27_report_00.md

Read the report back completely and verify its identity before terminal
notification. Do not overwrite a non-identical existing report. The Worker
may write only these two META files and must not commit or push META.

## Terminal report contract

The report must begin exactly:

### Report for ORCHESTRATOR_CHAT

It must contain exactly one coordinate echo:

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 27
Worker exchange ordinal: 00

Also include:

- status and exactly one phase-qualified result;
- exactly one report justification: changed-external-state;
- finding identity G3-ACL-REPROBE-01 and its bounded threat model;
- exact product candidate, required parent, AP pin, public META identity,
  and handoff identity;
- pre-state, install, targeted re-probe, immediate readback, delayed
  readback, and final-state classifications;
- exact changed host target and semantic owner/mode/type/source-equality
  result, without private paths beyond the allowed public system target;
- proof that the neighboring 61-, 62-, and uinput rules were not changed;
- proof that hidraw/uinput preservation and input-remapper equality passed or
  failed;
- broker inactive/no-runtime and no-live-device-open result;
- checkpoint disposition without its private path;
- owner-versus-Worker evidence attribution and sudo timestamp release;
- explicit statement that no broker start, ARM, grab, live source open,
  input-remapper change, or product/META Git mutation occurred;
- missing evidence and residual risk, if any;
- exactly one smallest next step;
- compact Orchestration critique containing MEASURED: and LEAD: (none
  allowed);
- exactly one `Logical-whole closure: not-closed` line;
- the exact authority-expiry sentence below.

Do not include raw ACL output, node numbers, UIDs/GIDs, serials, host
addresses, host keys, passwords, private paths, private configuration
contents, raw event data, key names, scan values, typed content, or
unredacted command transcripts. Use semantic results and public repository or
approved system target names only.

If PASS, explicitly scope any `verified-closed` wording to
G3-ACL-REPROBE-01 and the deployed ACL correction. Do not call G3 as a
whole, M2, or G4 closed.

The report is English. After complete readback, notify the Cooperator briefly
in Slovak with the truthful result and exact relative report path. Do not
require report copy-paste. The Cooperator publishes the exact META pair
separately. Authority for this Worker expires at this report.

## Delivery record

Delivery mode: file-based; no Cooperator copy-paste
Downloadable prompt filename: 27_deployment_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: this WORKER
Report filename: 27_report_00.md
Report persistence owner: this WORKER
Product Git publication owner: none for this Worker
META Git publication owner: COOPERATOR
Archival: wait-for-report

Stop after the terminal report. Do not continue to broker install/remove/
rollback, live G4 acceptance, documentation reconciliation, hibernate or
G7 policy, or autostart under this grant.

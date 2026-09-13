# ContextDesk — stabilize G3 ACL revocation after udev re-probe

ROLE: WORKER

Use a genuinely fresh Worker session. Worker 25 authority is expired.
Do not dispatch subagents. Speak Slovak to the Cooperator; write the
terminal report in English.

This is file-based delivery. The Cooperator must not copy/paste this prompt,
manually compose a prompt file, or manually compose a report file. The Worker
is explicitly authorized to persist the exact received prompt bytes and its
own terminal report into the META trace under the exact destinations below.
The Worker must not commit or push META. The Worker may commit and push the
bounded product correction described below, using a normal non-force push.

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 26
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker-session profile: Fresh Security Correction Worker — stabilize G3 ACL revocation
Phase: implementation
Task identity: CONTEXTDESK-G3-ACL-REPROBE-CORRECTION
Native planning mode: not-used
Reasoning recommendation: High
Recommended context capacity: approximately 128k tokens; advisory only
Evidence tier: E3
Evidence tier basis: security-boundary correction affecting udev/logind device
ACLs, with reproduced dynamic evidence that the current guard leaves a
session-user ACL after a remove/rollback re-probe
Activated stricter profile: INFOSEC.md
Security route: R6 correction followed by a fresh independent re-audit
Acceptance independence: required-separate-fresh-worker
Combined implementation envelope: allowed for this exact source/test/docs
correction and product commit; no host deployment or final acceptance

## Current finding and threat model

Session 25 produced bounded reproduced-dynamic evidence on the target host:
after the exact ContextDesk files and identity were removed and immediately
rolled back, the documented udev triggers did not stably revoke the
session-user ACL. After delayed re-probe, session-user ACLs were present again
on the G213 event nodes, /dev/port, and /dev/i2c-* while the hidraw lighting
ACL remained. The broker was not started and no live input source was opened.
The checkpoint remains with the Cooperator.

Finding identity: G3-ACL-REPROBE-01

Assets and security properties:

- confidentiality of G213 input event nodes;
- protection of raw I/O port and I2C device nodes from the session user;
- continued session-user access to G213 hidraw nodes for RGB;
- continued broker access to /dev/uinput without changing the session ACL.

Trust boundary:

- distribution OpenRGB udev rules and systemd-logind uaccess processing;
- ContextDesk udev guard/grant rules;
- the kernel device-node ACL state after add/change/re-probe events.

Attacker/local-actor assumption:

Any ordinary process running as the graphical session user must not gain
access to G213 event nodes, /dev/port, or /dev/i2c-* merely because OpenRGB
lighting rules or a later udev re-probe grants session uaccess. The session
user must retain only the intended hidraw and uinput access.

Observed source weakness:

packaging/udev/61-contextdeck-input-guard.rules removes the uaccess tag but
does not remove an already materialized POSIX ACL. A later re-probe can
therefore leave or recreate the forbidden session ACL even when CURRENT_TAGS
does not contain uaccess. The existing late 99-contextdeck-broker-uinput.rules
is intentionally unrelated and must continue to preserve the session ACL on
/dev/uinput.

Do not call this a general OpenRGB vulnerability or make an exploit claim
beyond the bounded target-host evidence. Do not include host identity,
addresses, node numbers, serials, raw ACL dumps, or private details in the
report.

## Single bounded outcome

Implement the smallest reviewable product correction that makes G3 ACL
revocation apply after the seat uaccess builtin on every relevant add/change
re-probe:

1. Retain the existing tag guard for G213 input, /dev/port, and /dev/i2c-*.
2. Add one separately named, late ContextDesk udev rule file that matches
   only:
   - G213 event nodes by USB ancestry and event* kernel name;
   - /dev/port;
   - /dev/i2c-*.
3. On add/change, remove extended ACL entries from only those matched raw
   input/I/O nodes, while preserving their base owner, group, and mode.
4. Do not match G213 hidraw or /dev/uinput. Do not set OWNER, GROUP, MODE,
   or a hard-coded session username/UID.
5. Ensure the new filename sorts after 73-seat-late.rules, which queues the
   seat uaccess builtin. The existing 99-contextdeck-broker-uinput.rules
   must remain additive and must continue to preserve the session ACL on
   /dev/uinput.
6. Add device-free static regression tests proving the exact rule scope,
   late ordering, ACL operation, and exclusion of hidraw/uinput.
7. Update only the directly owning public documentation for installation,
   verification, rollback, and the G3 security model.

The recommended implementation is a new late rule such as
packaging/udev/99-contextdeck-input-acl-guard.rules using narrowly matched
setfacl -b operations on /dev/%k for the three target classes. This removes
extended ACL entries without assigning a user or changing the base
owner/group/mode. If a different implementation is technically required,
the Worker must justify it in the report and prove the same negative and
preservation properties. Do not hard-code the current session user.

This Worker is not authorized to install the correction on the host. The
host remains a separate deployment and re-audit task. Do not claim that the
current host is secure merely because the repository correction passes tests.

## Exact product/AP/META candidates

Canonical product:

- Remote: https://github.com/cisarik/contextdesk
- Branch: main
- Exact implementation baseline:
  ab10491c49d0b6574b6953a02935a4664c39d7c2
- The Worker may create exactly one new normal product commit on main and
  push it non-force after all implementation checks pass.

Required AP:

- Gitlink and checkout:
  0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
- ./.ap/ap doctor must pass

Public META:

- Remote: https://github.com/cisarik/meta
- Trace:
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/
- Expected public commit containing Session 25:
  5077bd92c65749a33fd537a14dda8ed777bb46f3
- Accept a later public descendant only if ancestry is verifiable and it
  contains the current handoff plus the exact Session 24 and Session 25
  prompt/report pairs.
- Current handoff:
  projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/00_handout_02.md

Do not silently retarget product, branch, baseline, AP, or META identity.
If the baseline or public trace differs, stop before product mutation.

## Out of scope

Do not:

- install, remove, rollback, or mutate any host file or system identity;
- run udevadm trigger, udevadm test against live devices, setfacl on live
  devices, systemd-sysusers, systemctl daemon-reload, or any privileged
  command;
- start, stop, enable, restart, reload, lease, ARM, DISARM, or connect to
  contextdeck-broker.service;
- open G213 event nodes, /dev/uinput, /dev/port, /dev/i2c-*, or hidraw;
- use a physical keyboard, perform pass-through, test LEDs, or run OpenRGB;
- stop, restart, enable, disable, reconfigure, or inspect the contents of
  input-remapper configuration;
- test suspend, resume, hibernate, hybrid sleep, power actions, autostart,
  production readiness, or general coexistence;
- modify the session application, broker implementation, AP, META history,
  handoff files, roadmap, or unrelated packaging;
- change dependencies, build configuration beyond the existing static-test
  wiring, or licensing;
- broaden the rule to all input devices, all hidraw devices, all ACLs on the
  system, or an arbitrary user/device path.

No raw event lines, key names, scan values, control names/codes, typed
content, screenshots, serials, host addresses, host keys, passwords,
credentials, private checkout paths, private home paths, private temporary
paths, numeric UID/GID values, or unredacted command transcripts may appear
in the report or any durable trace.

## Public-safe changed-path allowlist

The product mutation allowlist is exactly:

- packaging/udev/99-contextdeck-input-acl-guard.rules
- tests/unit/test_udev_policy.cpp
- CMakeLists.txt
- docs/operations.md
- docs/testing-m2.md
- docs/architecture.md

The existing files below may be read and must remain semantically unchanged
unless a direct test/documentation wiring correction is required:

- packaging/udev/61-contextdeck-input-guard.rules
- packaging/udev/62-contextdeck-broker.rules
- packaging/udev/99-contextdeck-broker-uinput.rules

No other product path may change. If the proposed design requires a path
outside this allowlist, stop and report the required expansion; do not add it
silently.

The only permitted durable META writes are:

- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/26_implementation_00.md
- projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/26_report_00.md

## Read-only preflight and fail-closed gates

Before editing the product:

1. Verify the product remote, branch, exact baseline commit, clean worktree,
   no locks or active Git operation, matching AP gitlink/checkout, and
   ./.ap/ap doctor PASS. Do not reset, clean, stash, switch, restore, merge,
   rebase, or discard any owner change.

2. Verify the product baseline really contains the existing three udev
   files, the current static policy test, and the current documentation
   sections. Read the current source, not a remembered older version.

3. Verify public META origin/main contains commit
   5077bd92c65749a33fd537a14dda8ed777bb46f3 or a verified later descendant
   with Session 25. Check the public changed paths and read the exact
   Session 25 report. The report is PARTIAL/deployment-PARTIAL:
   remove and immediate rollback passed; candidate installation was not
   performed; G3 is not secure; the checkpoint remains; broker was never
   started. Do not use the report as G3 closure.

4. Read the pinned AP implementation, security-correction, reporting, Git,
   and Worker-persistence contracts; AGENTS.md; current README.md,
   ROADMAP.md, docs/architecture.md, docs/operations.md,
   docs/testing-m2.md; all three existing udev files; CMakeLists.txt; and
   tests/unit/test_udev_policy.cpp. Read only directly relevant sections.

5. Confirm the current host is not touched by this Worker. No host mutation
   is authorized, even if the host currently has the G3 ACL hole. Do not use
   a failed public fetch or a host observation as a reason to relax the
   product baseline gate.

If any precondition differs, stop before editing and report BLOCKED with
phase-qualified result not-applicable. Do not repair the worktree or host.

## Implementation requirements

The corrected rule must be public-safe and narrowly reviewable:

- match only the three intended target classes;
- use ACTION add|change so delayed re-probe cannot reintroduce the ACL;
- sort after 73-seat-late.rules;
- remove extended ACLs only from matched target nodes;
- preserve base owner/group/mode;
- leave G213 hidraw untouched;
- leave /dev/uinput untouched by the guard and preserve its separate broker
  ACL rule;
- contain no OWNER, GROUP, MODE, broad wildcard device match, hard-coded
  session user, hard-coded UID, or input-remapper operation;
- use an explicit absolute executable path if invoking setfacl;
- keep comments precise about the distinction between uaccess tags and
  materialized POSIX ACLs.

The Worker must inspect the resulting diff for:

- accidental overlap between the late guard and the uinput rule;
- ordering assumptions that are not encoded in tests;
- any way an add/change event could remove the base event group/mode;
- any way hidraw lighting or uinput session access could be removed;
- shell/udev quoting and substitution errors;
- report or documentation leakage of private host data.

Do not add a live-host test that opens devices. A static test or fake-file
test may model the rule text and ordering only.

## Required validation ladder

Run only the following bounded validation:

1. Static source/diff review against the exact allowlist.
2. udev syntax validation of all four candidate rule files using
   udevadm verify with name resolution disabled where supported.
3. Build the existing project using the documented clean-PATH workaround if
   the ambient CMake root is poisoned.
4. Run the full existing CTest suite once because the policy test and CMake
   wiring change. Do not rerun it to force a result.
5. Run the focused static policy test separately and record its exit status.
6. Run shell syntax checks only for scripts touched by the allowlist; no live
   hook invocation.
7. Verify the final product worktree contains only the allowlisted diff and
   the product commit is reproducible from the reviewed files.

If a test cannot run, report the exact bounded limitation and do not claim
implementation-PASS. Do not substitute a successful text grep for udev
syntax validation.

## Product Git authority

After all source and test gates pass:

1. Review the complete diff and confirm every changed path is allowlisted.
2. Create exactly one normal product commit on main with a descriptive
   message referring to stable G3 ACL revocation after udev re-probe.
3. Push that commit non-force to the canonical product origin/main.
4. Verify public product equality with the pushed commit, branch, changed
   paths, and AP pin.

No product commit or push is authorized before the implementation and
validation gates pass. No force push, tag, branch creation, history rewrite,
or META commit/push is authorized. If product publication fails after a local
commit, report the exact state; do not create a second commit or rewrite
history.

The resulting implementation report is non-independent. It must not claim
the target host is fixed, G3 is accepted, or the finding is closed. A later
fresh Worker must perform deployment/readback and a separate independent
re-audit of G3 after deployment.

## Worker-owned prompt and report persistence

The Worker owns physical persistence of both exact exchange files. The
Cooperator must not copy/paste, reconstruct, rename, or manually save either
file.

Immediately after receiving this prompt and before product editing:

1. Resolve the Cooperator-provided or Worker-created META checkout for the
   public remote.
2. Verify the trace directory, all parents, real-directory status, symlink
   status, and filename collisions.
3. Write the exact received prompt bytes to:

   projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/26_implementation_00.md

4. Read it back completely and verify byte identity with the received prompt.
   If the destination exists with non-identical bytes, stop before product
   mutation and report the collision.

After implementation and any product publication, write the complete
terminal report first to:

projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/26_report_00.md

Read the report back completely and verify its identity before terminal
notification. Do not overwrite a non-identical existing report and do not
choose another filename. The Worker may write only these two META files and
must not commit or push META.

## Report classification and content

Use PASS with phase-qualified result implementation-PASS only when the
allowlisted correction is complete, all required validations pass, exactly
one product commit is pushed and publicly verified, and the report clearly
states that host deployment and independent re-audit remain outstanding.

Use PARTIAL with an implementation-qualified result when useful source/test
evidence exists but a required implementation, validation, or publication
claim is incomplete. Use BLOCKED with phase-qualified result not-applicable
for a failed baseline, collision, unauthorized path, or precondition.

The report must begin exactly:

### Report for ORCHESTRATOR_CHAT

It must contain exactly one coordinate echo:

Persistent role identity: WORKER
Logical whole identity: g213-contextdeck-input-passthrough-safety
Worker session ordinal: 26
Worker exchange ordinal: 01

Also include:

- the finding identity, bounded threat model, and evidence classification;
- exact product baseline, final product commit, AP pin, and public META
  identity;
- exact changed paths and product commit/push/public-equality result;
- the chosen late-rule design and why its scope preserves hidraw/uinput;
- udev syntax, focused policy-test, build, and CTest results;
- explicit statement that no host mutation, live device open, broker start,
  ARM, grab, or input-remapper change occurred;
- independent deployment and fresh security re-audit as missing evidence;
- exactly one report justification: new-mutation;
- exactly one smallest next step;
- compact Orchestration critique with MEASURED: and LEAD: (none allowed);
- exactly one Logical-whole closure: not-closed;
- authority expiry.

Do not include raw ACL output, node numbers, UIDs/GIDs, serials, host
addresses, host keys, passwords, private paths, private config contents,
ordinary typed data, raw event lines, or unredacted command transcripts.
Do not claim the G3 finding is verified-closed; only a fresh independent
re-audit may make that determination after deployment.

The report is English. After complete readback, notify the Cooperator briefly
in Slovak with the truthful result and exact relative report path. Do not
require report copy-paste. The Cooperator publishes the exact META pair
separately. Worker authority expires at the terminal report.

## Delivery record

Delivery mode: file-based; no Cooperator copy-paste
Downloadable prompt filename: 26_implementation_00.md
Prompt authorship: ORCHESTRATOR
Prompt persistence owner: this WORKER
Report filename: 26_report_00.md
Report persistence owner: this WORKER
Product Git publication owner: this WORKER, only after gates pass
META Git publication owner: COOPERATOR
Archival: wait-for-report

Stop after the terminal report. Do not deploy the correction, re-audit G3,
perform live G4 acceptance, update broad documentation, decide hibernate
policy, or route autostart under this grant.

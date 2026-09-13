M2 is usable. The loop is not the product.
Logical whole g213-contextdeck-input-passthrough-safety · META sessions 01–26 plus issued 27_deployment_00.md · source: public prompt/report pairs in projects/contextdesk/00/02-… · 2026-09-13

Diagnosis for the Orchestrator
Pass-through safety already has five named live acceptance-PASS slices (16, 19, 22, 23, 24). Session 25 then used uninstall+udev trigger as a production gate, reopened the session-user event ACL, and dragged the whole into an R6 correct → deploy → re-audit subplot. Session 27 is host recovery, not a path to remapping or daily autostart. After 27, a second G3/G8 cycle is the stall.
26
Completed Worker sessions
5
Named live G4 PASS slices
8
BLOCKED or PARTIAL retries
open
Host G3 hole from session 25
Where the sessions actually went
Count of completed sessions 01–26 by outcome class. Source: META phase-qualified results in each *_report_*.md. Session 12 counts as one session with three exchanges. Session 27 is not in this chart because it has not run.

0
5
10
15
5
13
4
4
BLOCKED
Unique partition of 26. Live G4 PASS = 16, 19, 22, 23, 24. Build / deploy / docs PASS = 01–06, 11, 12, 14, 17, 20, 21, 26. PARTIAL = 08, 15, 18, 25. BLOCKED = 07, 09, 10, 13. The G3 subplot (11, 25, 26, pending 27) cuts across those bars; it is a routing story, not a fifth count.

Product truth versus paperwork truth
M2 promised a narrow libevdev/uinput broker: explicit ARM, 1:1 pass-through, crash/hang/suspend recovery, no autostart. That broker exists, is installed inactive, and has been exercised on the reference host. What is still labelled “open” is mostly packaging, documentation drift, and a security hole that this whole created during its own uninstall test.

Claim	Evidence	Still called open because
Explicit ARM / DISARM
16, 19, 22, 23, 24	Whole-G4 wording never closes on a named slice
Pass-through typing after grab
16 (sample), 23 (18/18), 24 (if00+if01)	Reports refuse to call the matrix “general”
Crash / cutoff recovery
16 matching-invocation death	Later slices keep restating G4 open
Watchdog + held modifier
19 after 18 PARTIAL	18 is kept as history, not superseded in the feeling of progress
Live suspend/resume
22	README/ROADMAP still say live suspend is not accepted
LED return + 18 controls
23	Same documentation drift
One remapper mapping
24 named slice	Handoff asked for “general coexistence”; 24 correctly refused that claim
G3 event/port/i2c closed to session
Stable through 24; broken by 25 trigger	Uninstall test used udev trigger; TAG-=uaccess does not strip POSIX ACLs
Install/remove/rollback
25 files+identity PASS; candidate install skipped	Gate mixed file restore with “G3 stays closed after distro re-probe”
Autostart / G8
Blocked by design	Cannot close inside M2; belongs in M5
The contradiction that feeds the loop
Distro OpenRGB 60-openrgb.rules tags G213 USB, /dev/port, and i2c with uaccess. That is the original keylogging hole from Planner session 01. ContextDesk 61- removes the tag; 62- grants event nodes only to contextdeck-broker; 99-uinput adds the broker on /dev/uinput after seat uaccess. Session 25 removed those files, triggered udev, rolled the files back, and triggered again. Tags stayed off; leftover POSIX ACLs came back and a delayed userspace refresh restored them. Rollback docs still tell the operator to trigger udev after deleting the guards — which is how you return to distro OpenRGB exposure.

Uninstall completeness
After ContextDesk udev is gone, the host should look like the distro. Distro-with-OpenRGB means session ACLs on event/port/i2c. That is a successful uninstall, not a G3 pass.

Installed ContextDesk policy
While the four rules are installed, the session user must not have event/port/i2c ACLs, and hidraw plus uinput session ACLs must remain. Rollback is restore-those-files plus ACL strip, not “trigger until distro uaccess returns”.

Session 26’s 99-contextdeck-input-acl-guard.rules (setfacl -b on add/change, hidraw/uinput excluded) is the missing rollback strip. It does not make uninstall G3-preserving. Repeating install/remove/rollback after 27 will remove the guard, trigger OpenRGB uaccess, and reopen the hole. That is the next loop if it is allowed.

Hard cut — what will actually work
1. Close the live hole, then stop G3
Session 27 as written is lawful host recovery for finding G3-ACL-REPROBE-01: install only /etc/udev/rules.d/99-contextdeck-input-acl-guard.rules from ca6052e, targeted add/change, immediate and ≥30s delayed readback. AP RF-08 allows one correction re-acceptance. This is that one. It is not a new security program.

If delayed readback PASSES: verified-closed for this deployed ACL scope only. Do not issue 28 as another remove/rollback, G3 re-probe, or OpenRGB coexistence audit. If it FAILS: escalate NEEDS_ORCHESTRATOR_DECISION. Do not write a fifth udev file. The delayed restore without a matching udev event is userspace (OpenRGB or logind), which udev RUN cannot win in a loop.

2. Do not treat 27 as whole-G3, whole-G4, or M2 close
Handoff 00_handout_02.md already had the right order after 23: remapper slice (done as 24), then packaging, then docs, then closure evaluation. Packaging 25 found a real ACL bug and then swallowed the remaining horizon. Restore G3, freeze G8/autostart as a new whole, and evaluate M2 against the named G4 matrix that already passed.

3. One Cooperator product decision, not another Worker
Close or park M2 as PARTIAL with accepted named slices 16 / 19 / 22 / 23 / 24, G3 restored on the reference host, autostart explicitly out of scope (M5/G8), hibernate unverified, general remapper not claimed. Residual OpenRGB risk after a PASS-27 is a Cooperator residual-risk call (RF-01), not an unbounded R6 budget.

4. Make the product usable in operations, not in another audit
Daily path already proven: SSH or second keyboard only for live grab trials; systemctl start contextdeck-broker; session-app GUI ARM; type; DISARM; stop. No [Install], no autostart. One documentation Worker may reconcile README/ROADMAP/operations with 22–24 and add that daily path. That Worker must not reopen udev, grab, or uninstall.

5. Put user-visible value in a new whole
ContextDeck’s promised experience is per-app lighting and later remapping. Lighting is M1 (accepted IRL). Remapping cannot ship before M2 safety, which is now evidenced. Staying inside this identity to perfect uninstall will never produce F5→debug or workspace-zone lighting. Next product whole is M3 g213-contextdeck-workspace-aware-lighting or a dedicated packaging whole — not session 28 of this one.

Forbidden next prompts
Do not issue another install/remove/rollback against the same seven files. Do not audit the 27 audit if the candidate and failing gate are unchanged. Do not expand 27 into broker start, ARM, OpenRGB functional lighting, or autostart. Do not treat “smallest next step” lines in Worker reports as a standing backlog that must be executed.
Session ledger
Source: META reports under projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/

Session	Phase	Result	What it actually moved
01
planning	PASS	M2 plan routable; G1/G3/G4 left as later gates
02–05
implementation	PASS	S1–S4: engine, udev, watchdog, IPC lease
06
acceptance	PASS	S4 IPC only; not physical G4
07
acceptance	BLOCKED	G4 not started; install/unit/recovery preconditions
08
implementation	PARTIAL	Production ARM in repo; host install lacked sudo TTY
09
acceptance	BLOCKED	Wrong candidate vs HEAD; SSH/2nd keyboard unproven
10
acceptance	BLOCKED	Same recovery-path blocker, unchanged
11
implementation	PASS	First G3 subplot: late uinput ACL after seat uaccess
12
impl / planning / impl	PASS	Docs pin + cutoff/production safety; 3 exchanges
13
acceptance	BLOCKED	cb72ae0 not installed on host; no grab
14
deployment	PASS	Inactive broker/unit install; no ARM
15
acceptance	PARTIAL	Cutoff death without genuine ARM/pass-through
16
acceptance	PASS	SSH + ARM + sampled pass-through + cutoff + recovery
17
implementation	PASS	Docs reconcile of the 16 slice; not G4 close
18
acceptance	PARTIAL	Watchdog/held-modifier incomplete; ARM skipped
19
acceptance	PASS	Armed watchdog abort with held modifier
20
implementation	PASS	Suspend/resume sleep hook in source
21
deployment	PASS	Sleep-hook install; broker hashes unchanged
22
acceptance	PASS	One live suspend/resume; disarmed post-start
23
acceptance	PASS	LED return + 18/18 host-remappable controls
24
acceptance	PASS	One non-G213 remapper mapping during armed grab
25
deployment	PARTIAL	Remove+rollback files OK; udev trigger reopened G3
26
implementation	PASS	Source ACL-strip rule ca6052e; host untouched
27
deployment	not run	Install that rule + independent delayed re-audit
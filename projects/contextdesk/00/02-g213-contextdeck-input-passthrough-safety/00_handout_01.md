# ContextDesk M2 — authoritative continuation handout

Date of handoff: 2026-09-12

This is the current continuity anchor for a fresh ChatOrchestrator. It
supersedes the older 00_handout.md in this directory. The older file remains
historical evidence; do not use it as the current state snapshot.

Project identity: ContextDesk / ContextDeck
Logical whole: g213-contextdeck-input-passthrough-safety
Repository: https://github.com/cisarik/contextdesk
META repository: https://github.com/cisarik/meta
Operating mode: manual AP orchestration; the Cooperator dispatches Workers
manually.

## 1. The honest closure answer

We are not closing this logical whole yet.

The named live safety slices for G4 now have strong evidence:

- explicit ARM, pass-through, identity-checked cutoff/death and recovery;
- an armed watchdog abort with a held modifier and recovery;
- one real suspend/resume cycle with pre-freeze stop, conditional
  post-resume restart, disarmed state, client reconnect, and post-resume
  G213 typing.

Those are accepted named slices, not acceptance of the whole M2/G4 gate.
The remaining closure work is listed in Section 7. Autostart is still
forbidden until the whole input-safety vertical and the independent
production/install gate are accepted.

The overall ContextDesk product is also not complete. M2 is only one
milestone; later workspace/context integration and system integration remain
outside this handoff.

## 2. Authoritative public anchors

Every fresh session must verify these against the public remotes before
making a new routing decision. A handout is not evidence when a remote
disagrees with it.

| Item | Required value | Meaning |
|---|---|---|
| Product branch | main | Public candidate branch |
| Product HEAD | ab10491c49d0b6574b6953a02935a4664c39d7c2 | Worker 20 suspend/resume implementation, pushed |
| AP gitlink and checkout | 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9 | Pinned AP protocol |
| META origin/main at handoff | 138ed06f7e818560e412604f41ca1376a6800986 | Includes Worker 22 acceptance/report |
| Runtime broker baseline | cb72ae0388307b514182efc6936712e3da42cda4 | Installed candidate provenance |
| Installed sleep hook SHA-256 | 91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e | /usr/lib/systemd/system-sleep/contextdeck-broker |
| Installed broker SHA-256 | 8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6 | /usr/bin/contextdeck-broker |
| Installed unit SHA-256 | 286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503 | /etc/systemd/system/contextdeck-broker.service |

The installed broker and unit are expected to be unchanged from the
previous deployment. The expected final service state after a trial is
static/inactive/dead. The unit is not enabled and there is no approved
autostart path.

The exact product, AP, and META values above are continuity anchors, not
permission to skip verification. If origin has moved, a report is missing,
or the AP gitlink is different, stop and reconcile with the Cooperator
before any live work.

## 3. Roles, authority, and language

The fresh instance is a strictly read-only ORCHESTRATOR:

- It inspects its own clones and public evidence.
- It composes one bounded Worker prompt at a time.
- It never edits or commits the product or META, runs a host installation,
  starts or arms the broker, touches udev/systemd/input devices, or dispatches
  subagents.
- It never treats a Worker assertion as acceptance without reconciling the
  terminal report, commit, changed paths, and required evidence.
- Authority to implement exists only inside the current complete Worker
  prompt and expires when that Worker reports.

The Cooperator-facing conversation is Slovak. Worker prompts and formal
Worker reports are English. Keep prompts executable by a fresh Worker:
identity, one outcome, scope/allowlist, safety gate, exact candidate,
commands/evidence, report contract, and authority expiry must be present.

This is manual orchestration. Do not create a session diary, an invented
NEXT_WORKER.md, an automated dispatcher, or a subagent tree. The Cooperator
chooses and pastes the next prompt into a genuinely fresh Worker session.

No 1M-token model is required for the remaining bounded slices. A fresh
high-reasoning Worker with roughly 128k tokens is normally ample; choose the
strongest practical model available for the specific slice. A live physical
acceptance is made safer by a short, precomputed prompt and prepared recovery,
not by making one Worker carry the entire project history.

## 4. Product boundary and non-negotiable invariants

ContextDeck is a Linux/KDE Plasma 6/Wayland C++20/Qt6/KF6 application for
the Logitech G213 Prodigy (046d:c336). RGB has five zones through external
OpenRGB using SDK protocol 5 over loopback. The context bridge is event-driven
through KWin. The input broker is a separate system service and the session
application communicates through a bounded Unix-socket IPC path.

These claims must remain true in every future prompt and report:

- The measured G1 matrix has exactly eighteen host-remappable controls:
  F1–F12 on if00 (codes 59–68, 87, 88) and Previous/PlayPause/Next/
  Mute/VolumeDown/VolumeUp on if01 (codes 165/164/163 and 113/114/115).
  Game Mode and Backlight produced no host event and remain firmware-only.
  The unresolved single probe observation of code 166 is not a mapping
  contract and must not be guessed into the catalog.
- No keylogging: do not log or archive raw events, key names, scan values,
  per-event timing, device serials, host addresses, or keystroke content.
- No per-key RGB claim: the physical device has five zones.
- Game Mode and Backlight are firmware-only and have no host remap events;
  they stay out of the remap catalog. Do not substitute PrintScreen or Pause.
- The broker never grabs a physical source implicitly. ARM is explicit,
  authenticated, user-visible, and lease-bound.
- A failed, dying, suspended, or restarted broker must leave the physical
  keyboard usable. A restart is disarmed, has no lease, and has no virtual
  device until the user deliberately arms it again.
- No silent automatic re-ARM after a crash, suspend, reconnect, or client
  retry.
- No autostart of an unproven grabbing path.
- Input-remapper coexistence and teardown must not be assumed from one
  successful sample.
- Evidence is semantic and public-safe; do not trade safety for a prettier
  report.

For any live grab, exactly one independent recovery path is required before
the broker starts or any physical source is opened:

1. SSH from another device, with a prepared shell able to stop and read back
   the exact unit; or
2. a second physical keyboard operating a prepared local terminal.

One route is sufficient. Do not ask the Cooperator to provide both
simultaneously. A mouse, gamepad, the G213 itself, a cutoff timer, or “SSH
should work” is not a recovery proof. The route must be demonstrated before
start/ARM and be usable throughout the trial. For suspend, the same device
must be reconnectable after resume if its SSH transport drops. This gate is
needed only for live input-grab work; it is not a prerequisite for
read-only inspection or ordinary build/test work.

## 5. Evidence ledger

Historical blocked and partial sessions are retained. A later pass does not
erase a previous failure; it only adds a new bounded evidence package.

| Session | Phase | Verified contribution | Result and limitation |
|---|---|---|---|
| 01 | planning | M2 plan and evidence gates | Plan accepted; no runtime closure |
| 02–05 | implementation | Broker core, identity/ledger/teardown, guard udev and narrow grants, additive uinput ACL, systemd packaging, real-grab seam and tests | Foundations; no live grab by themselves |
| 06 | acceptance | S4 IPC acceptance slice | Named slice only |
| 07, 09, 10 | acceptance/preflight | Host, candidate, or recovery prerequisites were not satisfied | Historical BLOCKED/PARTIAL; preserved |
| 11–12 | implementation | ACL ordering and production-safety/cutoff foundations | Implementation evidence; not live G4 |
| 13 | acceptance | Earlier installation mismatch | Historical BLOCKED; superseded by later deployment evidence |
| 14 | deployment | Candidate broker/unit installed while static/inactive | Runtime identity established; no ARM |
| 15 | acceptance | Unarmed cutoff death and safety observation | PARTIAL: no armed physical slice |
| 16 | acceptance | External SSH recovery, explicit ARM, G213 pass-through, identity-checked cutoff/death, post-death G213 recovery | PASS for that named live slice; not whole G4 |
| 17 | implementation/docs | Hard external-recovery requirement reconciled into the safety documentation | Docs-only; no runtime change |
| 18 | acceptance | Suspend happened before ARM; resume watchdog safely aborted the unarmed invocation | PARTIAL; exposed the need for a real sleep hook |
| 19 | acceptance | Explicit GUI ARM, armed G213, held-modifier SIGSTOP/watchdog abort, no restart/regrab, post-death G213 recovery | PASS for the armed watchdog slice; not whole G4 |
| 20 | implementation | Product commit ab10491... adds systemd sleep pre-stop/post-start hook, marker discipline, docs, deterministic hook tests, and IPC reconnect/no-auto-ARM tests | PASS implementation; no live suspend |
| 21 | deployment | Hook installed at the exact systemd system-sleep path with expected ownership/mode/hash; broker/unit unchanged | PASS deployment; no live suspend |
| 22 | acceptance | One real suspend cycle: external SSH proof, active/armed broker, hook stop before freeze, orderly resume, exactly one conditional disarmed restart, STATUS-only client reconnect, post-resume G213 typing, final cleanup | PASS for the named live suspend slice; not whole G4 |

The primary current live evidence is therefore Sessions 16, 19, and 22,
with Sessions 20 and 21 supplying the implementation/deployment chain.
Session 22 also recorded that hibernate.target is masked on the host; the
Worker did not change that policy. Hibernate and hybrid sleep were out of
scope.

The current product ROADMAP may still contain the pre-Session-22 wording that
live suspend was not accepted. That is documentation drift to reconcile, not
permission to discard the newer public report. Conversely, the report does
not by itself update the product ROADMAP or close the separate G7 power-action
gate; G7 remains an independent IRL claim until its own evidence and
documentation are reconciled.

## 6. Current suspend/resume semantics

The public candidate implements the following intended behavior:

- Before system sleep, the systemd sleep hook stops an active broker and
  leaves a root-owned marker only for a valid owned transition.
- After resume, the hook starts the broker once only when the marker is valid
  and the unit is inactive.
- The restarted broker is disarmed: no lease, no grab, no virtual device.
- The session client can reconnect through bounded retry and receive STATUS;
  it must not issue LEASE or ARM automatically.
- Failed/inactive states and invalid marker state fail closed.
- Restart policy remains Restart=no; watchdog behavior is unchanged.

Worker 22 observed all of these for one real suspend. It also observed a
harmless empty root-owned /run/contextdeck-sleep directory remaining after
marker consumption. Treat that as low-priority cleanup/polish, not as proof
of a safety failure. Do not alter power policy or unmask hibernate as a
shortcut.

## 7. What remains before this logical whole can close

The following are closure gates, not optional suggestions:

| Gate | Current state | Minimum closure evidence |
|---|---|---|
| LED-return behavior | OPEN | Source/test review and a bounded physical acceptance proving the advertised LED-return semantics, failure handling, and no unsafe silent degradation |
| All-control fidelity | OPEN | Evidence for all eighteen host-remappable G213 controls in the measured matrix, including media/volume on the correct interface; explicitly exclude firmware-only Game Mode and Backlight and do not infer a mapping for unresolved code 166 |
| Input-remapper coexistence | OPEN | An independent physical acceptance beyond the already sampled path, showing no stolen input, duplicate/phantom events, or unsafe teardown when the other tool is present |
| Install/remove/rollback and production readiness | OPEN | Fresh independent deployment/removal/rollback acceptance with exact identities, ownership, permissions, cleanup, and recovery; no hidden local-only artifact |
| Documentation truth | IN PROGRESS | ROADMAP, architecture, operations, testing, and META trace agree with the accepted evidence and state every out-of-scope claim explicitly |
| Sleep marker polish | LOW PRIORITY | Decide whether to remove the harmless empty directory and add a deterministic test; do not block safety closure unless the source review finds a real ownership/path issue |
| Hibernate/hybrid policy | DECISION REQUIRED, OUT OF SCOPE FOR CURRENT LIVE EVIDENCE | Keep the pre-existing mask and document unsupported/unverified behavior, or schedule a separately authorized acceptance; never imply Session 22 tested it |
| G7 power actions | OPEN, SEPARATE FROM M2 | M1 display-off/suspend action acceptance is still a distinct roadmap gate; do not conflate broker sleep recovery with end-user power-action acceptance |
| Autostart/G8 | BLOCKED BY DESIGN | Only after every preceding M2/G4 gate and independent install/rollback evidence is accepted may a separate G8 autostart authority be issued |

The whole is closed only when the required gates have named acceptance
reports, the public product and META commits match those reports, and the
Cooperator has explicitly accepted the closure statement. Passing the three
named live slices is not enough.

## 8. Exact next routing order

The fresh Orchestrator should follow this order and keep each Worker bounded:

1. Verify product HEAD, AP pin, META origin/main, clean worktrees, and the
   current report/prompt pair from Sessions 20–22. Read the current product
   source and docs; do not assume this handout is newer than origin.
2. Perform a read-only source/test review of LED-return behavior and
   all-control fidelity. Decide whether the next Worker is an implementation
   Worker or an acceptance Worker. Do not issue a live prompt until the
   ownership boundary and exact evidence are clear.
3. Route one fresh Worker for the smallest missing LED/control slice. If code
   changes are required, obtain a bounded implementation report and a
   pushed product commit first; then route a separate fresh physical
   acceptance Worker. For any live grab, require exactly one demonstrated
   external recovery route.
4. Route a separate fresh coexistence acceptance for input-remapper, with
   no unrelated code changes and no autostart.
5. Route independent install/remove/rollback and production-readiness work.
   Keep the unit static/inactive until the G4 decision is complete.
6. Reconcile and update durable product/META documentation, decide the
   hibernate policy explicitly, and remove only any low-risk polish defect
   that survives review.
7. Only then evaluate whole-G4 closure and issue a separate G8/autostart
   plan. A fresh Orchestrator must never “close” M2 merely because the
   broker starts or a single keyboard sample works.

The next Worker ordinal is expected to be 23, but the phase and filename must
be chosen after Step 2. Do not pre-authorize an unverified acceptance prompt.

## 9. Fresh-Orchestrator onboarding checklist

Before the first reply to the Cooperator, the new instance must:

1. Clone the product with its submodule and clone META, or update its
   inspection clones:

   ~~~text
   git clone --recurse-submodules https://github.com/cisarik/contextdesk
   git clone https://github.com/cisarik/meta
   ~~~

2. Read the pinned AP files in this order: AP.md, AP_ORCHESTRATOR.md,
   PROMPT_CONTRACTS.md, AP_WORKER.md, and advisory INFOSEC.md.
3. Read product AGENTS.md, ROADMAP.md, architecture.md, operations.md,
   hardware/g213-control-matrix.md, hardware/g213-zone-map.md,
   testing-m2.md, and the current handoff.
4. Read the relevant META trace, especially the prompts/reports for Sessions
   16–22. Treat the legacy 00_handout.md as historical because this file
   supersedes it.
5. Verify with git, not page-cache or memory:

   ~~~text
   git fetch origin main
   git status --short
   git rev-parse HEAD
   git ls-tree HEAD .ap
   git -C .ap fetch origin main
   git -C .ap rev-parse HEAD
   git -C .ap rev-parse origin/main
   ./.ap/ap doctor
   ~~~

6. State any drift before routing. Do not ask the Cooperator to repeat
   already accepted evidence; request only the missing public commit or
   verification output.
7. Tell the Cooperator in Slovak that M2/G4 is still open, name the next
   bounded slice, and provide one complete English Worker prompt. Do not
   start by asking for two keyboards and SSH: one external route is enough
   when a live-grab gate is actually reached.

## 10. Worker/report and archival contract

Every new prompt must identify:

- fresh Worker session, role WORKER, logical whole, ordinal and phase;
- exact product/AP candidate and allowed paths;
- one bounded outcome and explicit out-of-scope list;
- whether Native planning mode is required;
- the independent-recovery gate when the task can grab a real source;
- no secrets/raw input/private host details in evidence;
- exact report filename and destination;
- authority expiry at terminal report.

The Worker must create the exact report file in the real META checkout when
the prompt grants that authority, read it back completely, and report
persistence truthfully. The Cooperator archives the exact prompt/report pair,
commits it to META, and decides when to push. A missing Worker-created report
is an AP execution defect to record, not a reason to silently fabricate a
report by copy-paste.

Keep each prompt/report pair public-safe. Do not put passwords, host keys,
IP addresses, USB serials, raw event codes, key names, sample text, or
private absolute paths in the report. Public repository paths such as the
canonical product and META paths are allowed.

## 11. Claims the fresh Orchestrator must not make

Until the gates in Section 7 are separately evidenced, never claim:

- whole M2 or whole G4 acceptance;
- production readiness, uninstall/rollback readiness, or autostart safety;
- hibernate or hybrid-sleep support;
- automatic re-ARM after suspend, crash, or reconnect;
- complete LED-return or all-control fidelity;
- input-remapper coexistence in general;
- that a single successful physical sample proves the full keyboard matrix;
- that a 1M-context Worker is necessary.

The safe continuation sentence is:

“The named live G4 slices are accepted, but the M2 logical whole remains
open. I will verify the public anchors and route the smallest missing
evidence slice next.”

## 12. Handoff completion

This handout is a bridge, not a new Worker authority. The next
ChatOrchestrator must produce its own current verification and its own
bounded prompt. Preserve the report history, keep the public anchors
verifiable, and close the logical whole only from an explicit evidence
matrix—not from elapsed conversation context.

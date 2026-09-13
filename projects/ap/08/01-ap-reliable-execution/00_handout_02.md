# ContextDesk M2 — authoritative continuation handoff

Date of handoff: 2026-09-13

This document is the next continuity anchor for a fresh ChatOrchestrator.
Once publicly archived, it supersedes `00_handout_01.md` in this directory.
The older handoffs remain historical evidence and must not be rewritten.

Project identity: ContextDesk / ContextDeck  
Logical whole: `g213-contextdeck-input-passthrough-safety`  
Product repository: https://github.com/cisarik/contextdesk  
META repository: https://github.com/cisarik/meta  
Operating mode: manual AP orchestration; the Cooperator dispatches Workers
manually.

## 1. Honest closure answer

The named live G4 slices are accepted, but the M2 logical whole remains open.

The accepted named live slices are:

- Session 16: independently demonstrated SSH recovery, explicit authenticated
  ARM, sampled G213 pass-through, identity-checked cutoff/death, and post-death
  G213 recovery.
- Session 19: explicit GUI ARM, armed G213, held-modifier watchdog abort,
  no automatic restart or re-grab, and post-death G213 recovery.
- Session 22: one real suspend cycle with external SSH recovery, active/armed
  pre-sleep broker, systemd sleep-hook stop before freeze, orderly resume,
  exactly one conditional post-resume start, disarmed/no-lease/no-virtual
  state, STATUS-only client reconnect, and post-resume G213 typing.
- Session 23: live compositor LED return to physical if00, deterministic
  LED-write failure semantics, all eighteen measured host-remappable controls
  exercised through one armed trial, explicit DISARM, and final inactive
  cleanup.

These are named bounded acceptance slices, not whole-G4 or whole-M2 closure.
The product is not production-ready, autostart is not approved, and no
hibernate or hybrid-sleep claim exists.

## 2. Authoritative public anchors at this handoff

Every fresh session must verify these values against public origin. The
handoff is not evidence when a remote disagrees with it.

| Item | Required value | Meaning |
|---|---|---|
| Product remote/branch | `https://github.com/cisarik/contextdesk` / `main` | Public product candidate |
| Product HEAD | `ab10491c49d0b6574b6953a02935a4664c39d7c2` | Worker 20 suspend/resume implementation |
| AP gitlink and checkout | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` | Pinned AP protocol |
| META origin/main at this handoff | `4d55ebd2242e0ed8671d0f28522858c6387bc7e2` | Public META tip verified on 2026-09-13 |
| Session 23 prompt/report commit | `c964857397ff81bb96f59abbce759dd24effd952` | Public exact prompt/report pair for Session 23 |
| Runtime broker baseline | `cb72ae0388307b514182efc6936712e3da42cda4` | Installed broker provenance |
| Installed sleep hook SHA-256 | `91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e` | `/usr/lib/systemd/system-sleep/contextdeck-broker` |
| Installed broker SHA-256 | `8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6` | `/usr/bin/contextdeck-broker` |
| Installed unit SHA-256 | `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503` | `/etc/systemd/system/contextdeck-broker.service` |

The META tip is a public descendant of the previous handoff anchor
`138ed06f7e818560e412604f41ca1376a6800986`. Its history includes the exact
Session 23 pair at `c964857397ff81bb96f59abbce759dd24effd952` and later AP Reliable Execution documentation.
This was verified public history, not an unpushed local change. A future META
descendant is acceptable only when it is publicly verifiable, preserves the
product/AP identities, and contains the exact authorized archival changes.
Any contradictory change is drift and must be reported before routing.

The public trace must contain both:

```text
projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/23_acceptance_00.md
projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/23_report_00.md
```

The product and AP worktrees were clean at verification, and `./.ap/ap doctor`
passed. The installed unit is expected to remain `static/inactive/dead` when
no trial is in progress. It is not enabled and there is no approved autostart
path.

## 3. Roles, authority, and language

The fresh instance is a strictly read-only ORCHESTRATOR:

- inspect only its own public inspection clones and reconcile public reports;
- compose one complete bounded Worker prompt at a time;
- never edit, commit, or push the product or META;
- never install, enable, start, stop, ARM, grab, or probe input devices on the
  Cooperator's host;
- never dispatch subagents;
- never declare a Worker claim accepted without reconciling the public commit,
  changed paths, exact prompt/report pair, and evidence boundaries.

Implementation authority exists only inside the complete Worker prompt issued
by the Orchestrator and expires at that Worker's terminal report.

Use Slovak with the Cooperator. Write Worker prompts and formal Worker reports
in English. The Cooperator manually chooses a Worker, pastes one prompt, runs
host commands, archives the exact prompt/report pair, and decides whether to
commit and push META.

Do not create `NEXT_WORKER.md`, a session diary, an automated dispatcher, a
speculative report, or a substitute report from memory.

## 4. Product boundary and safety invariants

ContextDeck is a C++20/Qt6/KF6 Linux/KDE Plasma 6/Wayland application for the
Logitech G213 Prodigy (`046d:c336`). RGB is five-zone OpenRGB SDK protocol 5
over loopback. The session application does not access raw keyboard devices;
the broker owns the input path.

The following invariants remain binding:

- The measured G1 matrix contains exactly eighteen host-remappable controls:
  F1–F12 on if00 (`59–68`, `87`, `88`) and the six media/volume controls on
  if01 (`165/164/163` and `113/114/115`).
- Game Mode and Backlight generated no host event and remain firmware-only.
  Do not substitute PrintScreen or Pause.
- The isolated unresolved observation of code `166` is not a mapping contract.
  Do not guess it into the catalog or count it as one of the eighteen.
- No keylogging. Do not put raw events, key names, scan values, per-event
  timing, typed content, serials, host addresses, host keys, passwords, or
  private paths in code logs, prompts, reports, or META.
- No per-key RGB claims. The physical device has five zones.
- Physical grabbing is explicit, authenticated, user-visible, and
  lease-bound.
- Crash, watchdog abort, suspend, disconnect, failed acquisition, and teardown
  must leave the real keyboard usable and the broker disarmed or dead as the
  applicable failure semantics require.
- No automatic ARM after restart, resume, crash, or client reconnect.
- No unproven autostart.
- Input-remapper coexistence must be demonstrated rather than inferred from a
  single successful sample.

For any live physical grab, exactly one independent recovery route is required
before the broker starts or a physical source is opened:

1. SSH from another device with a prepared exact-unit status/stop shell; or
2. a second physical keyboard operating a prepared local terminal.

One route is sufficient. Do not request both. A mouse, gamepad, the G213, a
timer, or “SSH should work” is not a recovery proof. The route must be
demonstrated before start/ARM and usable throughout the trial. For suspend,
the same SSH device must be reconnectable after resume if transport drops.
Read-only inspection, builds, and deterministic tests do not require this
physical gate.

## 5. Reconciled evidence ledger

Historical BLOCKED and PARTIAL sessions remain real history. Later evidence
supersedes only the same bounded claim; it does not erase earlier failures.

| Session | Phase | Reconciled contribution | Boundary |
|---|---|---|---|
| 01–05 | planning/implementation | Broker design, identity, ledger, teardown, policy, packaging, and tests | No live G4 by themselves |
| 06 | acceptance | S4 IPC acceptance slice | Not physical G4 closure |
| 07, 09, 10, 13, 15, 18 | acceptance/preflight | Historical BLOCKED or PARTIAL prerequisites and observations | Preserved; not erased |
| 11–12, 17 | implementation/docs | ACL ordering, production/cutoff foundations, and recovery-gate documentation | Not live acceptance by themselves |
| 14 | deployment | Broker/unit installed while static/inactive | No ARM |
| 16 | acceptance | SSH recovery, explicit ARM, sampled pass-through, cutoff/death, post-death recovery | Named slice only |
| 19 | acceptance | Armed watchdog abort with held modifier and post-death recovery | Named slice only |
| 20 | implementation | Sleep hook, marker discipline, deterministic hook tests, reconnect/no-auto-ARM implementation | No live suspend by itself |
| 21 | deployment | Exact sleep-hook installation; broker/unit unchanged | No live suspend by itself |
| 22 | acceptance | One real suspend/resume cycle with disarmed restart and STATUS-only reconnect | Named suspend slice only |
| 23 | acceptance | LED return, LED failure semantics, all eighteen controls, explicit cleanup | Named LED/control slice only |

### Session 23 exact boundary

The public prompt/report pair for Session 23 is byte-identical to the
Cooperator-provided pair and is public under the verified META history.

The report supports the following named result:

- SSH from another device was demonstrated before start and ARM; no second
  keyboard was used.
- One broker start, one authenticated GUI ARM, one GUI DISARM, and one stop
  occurred on the exact product candidate.
- Live compositor LED return to physical if00 was observed; no per-key RGB
  claim was made.
- Existing deterministic tests showed the documented `led-write-failed`
  behavior without disarming solely for that LED failure.
- All eighteen measured host-remappable entries passed: twelve on if00 and
  six on if01. Firmware-only entries and unresolved code 166 were excluded.
- Final state was verified `static/inactive/dead`, with no broker process,
  virtual device, socket, or changed host policy.

The report also contains two historical report-quality exceptions that must
not be silently rewritten:

1. A few semantic media-control labels appear in detailed evidence even though
   the prompt required reports to avoid key names.
2. The numeric `SUDO_K_RC`/post-timestamp marker was not returned, although
   the Worker recorded that the owner executed the release block and the final
   runtime state was verified.

These exceptions do not invalidate the named physical result, but future
reports must obey the public-safe evidence contract exactly. Do not rerun
Session 23 from expired authority merely to improve report wording.

## 6. Current product and documentation truth

The implementation and deployment chain for the accepted named slices is
publicly present at product HEAD `ab10491...`. The broker unit remains static
and inactive outside a trial. The installed hashes above remain the expected
runtime baseline.

The product documentation is not yet fully reconciled with Sessions 22 and
23. ROADMAP, README, operations, and testing text may still contain older
“live suspend not accepted” or “LED/all-control open” wording. Treat this as
documentation drift to fix in the dedicated documentation phase, not as a
reason to discard the newer public reports and not as permission to claim
whole-M2 closure.

Session 22 observed a harmless empty root-owned `/run/contextdeck-sleep`
directory after marker consumption. This is low-priority polish. Do not alter
the sleep safety contract or power policy merely to remove it.

Hibernate and hybrid sleep were not tested. `hibernate.target` was pre-existing
and masked; do not unmask or change it casually. The separate G7 end-user
power-action gate remains open.

## 7. Closure gates still open

| Gate | State | Required evidence |
|---|---|---|
| LED-return semantics | Named Session 23 slice accepted | Documentation still needs to state the exact bounded semantics and failure behavior |
| All-control fidelity | Named Session 23 slice accepted | Documentation must reflect 18/18 evidence, correct interfaces, firmware-only exclusions, and unresolved-166 rule |
| Input-remapper coexistence | OPEN | Separate fresh acceptance beyond the sampled path, with input-remapper unchanged and no stolen, duplicate, phantom, or unsafe teardown behavior |
| Install/remove/rollback and production readiness | OPEN | Independent deployment, removal, rollback, ownership/permission, exact identity, cleanup, and recovery evidence |
| Documentation truth | OPEN | ROADMAP, README, architecture, operations, testing, and META agree with the public evidence and out-of-scope claims |
| Sleep marker polish | LOW PRIORITY | Decide whether empty-directory cleanup is worthwhile and test it deterministically; do not change safety semantics casually |
| Hibernate/hybrid policy | DECISION REQUIRED, OUT OF SCOPE | Keep behavior explicitly unverified or schedule a separately authorized trial; never imply Session 22 covered it |
| G7 power actions | OPEN, SEPARATE | End-user display-off/suspend action evidence remains separate from broker recovery after suspend |
| Autostart/G8 | BLOCKED BY DESIGN | No autostart authority until all preceding M2/G4 and production gates pass |

The logical whole closes only after the required gates have named reports, the
public product and META history match those reports, documentation is
reconciled, and the Cooperator explicitly accepts the final evidence matrix.

## 8. Exact next routing order

The next fresh Orchestrator must keep each Worker bounded and must not repeat
Sessions 16, 19, 22, or 23.

1. Verify the public product, AP, and META anchors; read the public Session 23
   prompt/report and changed paths; read the current product source and docs.
2. Route the smallest missing slice: a separate fresh acceptance of
   input-remapper coexistence beyond the already sampled path, if the source
   review finds the implementation complete. It must define its exact evidence
   and changed-path allowlist before any live prompt is issued.
3. If a source defect is found, route a bounded implementation Worker first,
   require a pushed product commit, and only then route a separate acceptance
   Worker.
4. Route independent install/remove/rollback and production-readiness
   evidence. Keep the broker unit static/inactive outside a bounded trial and
   do not route autostart.
5. Reconcile ROADMAP, README, architecture, operations, testing, and META;
   decide hibernate/hybrid policy explicitly and address only justified
   low-risk sleep-marker polish.
6. Evaluate whole-G4/M2 closure only from the completed evidence matrix. A
   separate G8/autostart plan may be considered only afterward.

The next Worker ordinal is expected to be 24. The phase and exact filename
must still be selected after the fresh Orchestrator completes its read-only
review. Do not pre-authorize a live acceptance merely because the next number
is known.

For a live coexistence trial, one independently demonstrated SSH route is
sufficient. Do not ask the Cooperator for two keyboards plus SSH.

## 9. Mandatory fresh-Orchestrator onboarding

Use read-only inspection clones. Do not run repository commands on the
Cooperator's host merely to satisfy onboarding.

```text
git clone --recurse-submodules https://github.com/cisarik/contextdesk
git clone https://github.com/cisarik/meta
```

Read all of the following before the first routing decision:

1. The pinned AP: `AP.md`, `AP_ORCHESTRATOR.md`, `PROMPT_CONTRACTS.md`,
   `AP_WORKER.md`, and advisory `INFOSEC.md`.
2. Product `AGENTS.md`, `ROADMAP.md`, `README.md`,
   `docs/architecture.md`, `docs/operations.md`, `docs/testing-m2.md`,
   `docs/hardware/g213-control-matrix.md`, and
   `docs/hardware/g213-zone-map.md`.
3. This handoff, `00_handout_01.md` as historical context, and the public
   fresh-Orchestrator prompt associated with the previous handoff.
4. The META trace for Sessions 16–23, with special attention to the exact
   prompt/report pairs for 20, 21, 22, and 23.
5. Product and META history, not only rendered pages.

Run and record the identity checks in the inspection clones:

```text
git fetch origin main
git status --short
git rev-parse HEAD
git rev-parse origin/main
git ls-tree HEAD .ap
git -C .ap fetch origin main
git -C .ap rev-parse HEAD
git -C .ap rev-parse origin/main
./.ap/ap doctor
git ls-remote origin refs/heads/main
```

For META, also verify the public trace files and inspect the changed paths of
the commit that added each new pair. If a public identity, AP doctor result,
or required pair contradicts this handoff, report the drift in Slovak and stop
before issuing a live prompt. Never retarget silently.

## 10. First reply required from the fresh Orchestrator

The first reply to the Cooperator must be in Slovak and must state:

1. verified product HEAD, AP pin, META origin/main, worktree state, and any
   discrepancy;
2. exactly that the M2/G4 logical whole remains open;
3. the four accepted named live slices (16, 19, 22, and 23) and their
   boundaries;
4. the remaining closure gates in concise form;
5. the next read-only review and whether the next Worker is implementation or
   acceptance;
6. that one external recovery route is sufficient when live grabbing is
   reached, so the Cooperator is not asked for both SSH and a second keyboard;
7. no claim of autostart, hibernate, whole-G4 closure, general coexistence, or
   production readiness.

The fresh Orchestrator must then continue with the authorized read-only review;
it must not wait for a generic “continue” when the next inspection is already
authorized.

## 11. Worker prompt and report contract

Every Worker prompt must be a complete English document containing:

- role `WORKER`, fresh-session requirement, logical whole, session/exchange
  ordinals, phase, reasoning recommendation, and evidence tier;
- exact product/AP candidate and public-safe path allowlist;
- one measurable outcome and explicit out-of-scope claims;
- Native planning mode requirement or `not-used`;
- read-only preflight and fail-closed stop conditions;
- exactly one independent recovery route when a live source may be grabbed;
- no raw events, key names, sample text, serials, secrets, host keys,
  addresses, or private paths in the report;
- exact report filename and destination;
- report-first persistence, complete readback, truthful classification, and
  authority expiry.

Implementation Workers must push the product commit before a separate
acceptance Worker is issued. Live acceptance Workers must receive precomputed
recovery commands and must not require model round-trips while the broker is
armed or the machine is resuming.

The Cooperator archives the exact prompt/report pair and decides whether to
push META. Historical reports must not be rewritten or cosmetically repaired.

## 12. Claims the fresh Orchestrator must not make

Until the remaining gates are separately evidenced, never claim:

- whole M2 or whole G4 acceptance;
- production readiness, independent install/remove/rollback readiness, or
  autostart safety;
- hibernate or hybrid-sleep support;
- automatic re-ARM after suspend, crash, or reconnect;
- general input-remapper coexistence;
- that a single successful physical sample proves the full keyboard matrix;
- that a 1M-context Worker is necessary;
- that a stale ROADMAP sentence overrides a newer public acceptance report.

The safe continuation sentence is:

“The named live G4 slices are accepted, but the M2 logical whole remains
open. I verified the public anchors and am routing the smallest missing
evidence slice next.”

## 13. Handoff completion

This handoff is a bridge, not a Worker authority. The fresh Orchestrator must
produce its own public verification and its own bounded prompt. Preserve all
historical reports, keep the public anchors verifiable, and close the logical
whole only from an explicit evidence matrix—not from elapsed conversation
context.

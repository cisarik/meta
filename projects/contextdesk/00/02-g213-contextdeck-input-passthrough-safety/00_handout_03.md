# ContextDesk / ContextDeck — M2 park handoff after Session 27

This is the authoritative M2 park handoff for the logical whole
`g213-contextdeck-input-passthrough-safety`.

It supersedes `00_handout_02.md` after the Cooperator archives it publicly.
It is a continuity record, not permission to mutate the product, META, or
the Cooperator host. A fresh Orchestrator must verify every public identity
against the repositories before routing.

## Executive truth

M2 is parked. The named live G4 slices are accepted, and the G3 ACL
re-probe finding is host-mitigated on the authorized reference host. The
G3 finding was not independently re-audited by a fresh Worker; the
Cooperator explicitly accepted that residual evidence gap in order to stop
the audit loop and advance the product.

Do not dispatch the historical `27_deployment_00.md` prompt. It was authored
but never pasted into a fresh Worker session. Session 27 was instead an
Orchestrator-led, Cooperator-owned host execution. Its report is truthful
only when classified as an owner-path record, not as independent acceptance.

The M2 logical whole remains not-closed. Do not issue another M2 Worker for
udev, G3 re-audit, uninstall, install/remove/rollback, live grab, G4, or
autostart. Do not reopen G3 merely because the independent R6 re-audit was
waived for this park.

The named live G4 slices are accepted, but the M2 logical whole remains open.

## Verified-at-report identities

These values were recorded by the Session 27 report and must be checked
against public origin by the successor before any routing decision. They are
not a substitute for fresh verification.

| Item | Recorded value |
|---|---|
| Product remote / branch | `https://github.com/cisarik/contextdesk` / `main` |
| Product HEAD | `ca6052e816d4884ddeac9d7499a42c2aca089e7e` |
| Required product parent | `ab10491c49d0b6574b6953a02935a4664c39d7c2` |
| AP gitlink and checkout | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| Runtime broker baseline | `cb72ae0388307b514182efc6936712e3da42cda4` |
| Installed broker SHA-256 | `8e80f2d78530b01d9cda4ab77c4ff75d2888055dadce35fbb9483a15651940a6` |
| Installed unit SHA-256 | `286154ba6f443adced5dc965b0f0c4da2dfae2a44e4f77edf888c6ef96c30503` |
| Installed sleep hook SHA-256 | `91e47888a90f3b2c1853f8bd454f1bdeb342a507efb1084767e09480d4eeac8e` |
| Installed 61-rule SHA-256 | `c31ed56d14ba2cd94e73b2883a860c456965ea4a7fb42623aac011cd03d9ea70` |
| Installed 62-rule SHA-256 | `070c7c98229a89f89b1ac42253e1a57fa4da927fd299090ed93a81e622a7a5ad` |
| Installed 99-uinput-rule SHA-256 | `f10d2d709d047d1648448572cff2cbe35552aa08fe07830a5361cd948471b7b2` |
| Installed 99 ACL-guard SHA-256 | `da87276d2997080205303e5ffcbc812b179d6d0747f32ce36e2d58bd8f3511e5` |
| Last META tip reported by Session 27 | `ef79edab1f298b02ab10d9db979296ae7997da22` |

The Session 27 report says that the last META tip was the Session 26 pair
archival and that the Session 27 pair still awaited Cooperator publication.
The successor must accept only a later public descendant when its ancestry,
changed paths, handoff, and exact historical pairs are verifiable.

## Container-only public repository access

The fresh ChatOrchestrator is strictly read-only. It must access the public
product, AP submodule, and META only through its own disposable inspection
clones inside its container. It must not use the Cooperator’s product or
META checkout as an inspection clone and must not run repository inspection
or Git mutation commands on the Cooperator host.

Use the canonical HTTPS remotes and create fresh container-local clones when
there is any doubt about cache state:

```text
git clone --recurse-submodules https://github.com/cisarik/contextdesk.git inspect-contextdesk
git clone https://github.com/cisarik/meta.git inspect-meta
```

For an existing disposable inspection clone, update only that clone with
`git -C ./inspect-contextdesk pull --ff-only origin main` or
`git -C ./inspect-meta pull --ff-only origin main`. Equivalently, use
`fetch --prune` followed by an explicit detached checkout. For immutable
verification, use commands of this form:

```text
git -C ./inspect-contextdesk fetch --prune origin main
git -C ./inspect-contextdesk checkout --detach origin/main
git -C ./inspect-contextdesk checkout --detach <verified-product-commit>
git -C ./inspect-contextdesk/.ap fetch --prune origin main
git -C ./inspect-contextdesk/.ap checkout --detach <verified-ap-commit>
git -C ./inspect-contextdesk ls-remote origin refs/heads/main
git -C ./inspect-meta fetch --prune origin main
git -C ./inspect-meta checkout --detach <verified-meta-commit>
git -C ./inspect-meta ls-remote origin refs/heads/main
```

`pull` is allowed only inside a disposable container inspection clone. It is
not permission to pull, merge, rebase, or alter the Cooperator’s working
copies. A local `HEAD` or a cached `origin/main` is never public proof by
itself; compare the fetched result with `git ls-remote` and inspect ancestry
and changed paths.

If GitHub appears stale, a commit object is missing, or a fetch/checkout is
affected by a cache inconsistency, discard only that disposable inspection
clone and create a fresh container-local clone. Retry the canonical HTTPS
clone/fetch from that fresh container and verify the resulting tip with
`git ls-remote`. If DNS resolution or HTTPS transport fails, record the
bounded network symptom, check name resolution inside the container, and
retry from a fresh container using the canonical HTTPS remote. A safe
transport retry may use `git -c http.version=HTTP/1.1`, but do not alter the
Cooperator host’s DNS or Git configuration. Stop before routing if the
public identity still cannot be verified. Do not silently use an older local
clone, substitute an unverified mirror, change the public remote, or retarget
to a different commit.

The network check belongs inside the container, for example with
`getent ahosts github.com` followed by a direct
`git -c http.version=HTTP/1.1 ls-remote` against the canonical HTTPS remote.
This is a connectivity/cache diagnostic only; it is not permission to edit
DNS, use a host credential, or substitute a mirror.

The handoff’s recorded hashes are continuity anchors, not a workaround for
public verification. The next Orchestrator must obtain the latest reachable
public product and META tips through the container clone/fetch/checkout path
above before issuing the M3 Planner prompt.

## Session 27 identity honesty

| Field | Truth |
|---|---|
| Issued prompt | `27_deployment_00.md` |
| Prompt status | authored, not dispatched |
| Worker 27 | did not run |
| Actual actor | Cooperator owner terminal under Orchestrator guidance |
| Actual task | install the Session 26 ACL guard, reload/targeted trigger, and read back ACL state |
| Product commit/push | none in Session 27 |
| META commit/push | none in Session 27; Cooperator owns publication |
| Broker start / ARM / DISARM / grab | none |
| Live source open | none |
| input-remapper configuration change | none |
| G3 status | host-mitigated on the authorized reference host; not independently verified closed |
| Report classification | `PASS`, `deployment-PASS` owner path |
| Authority | expires at `27_report_00.md` |

The issued prompt used `Worker exchange ordinal: 00`. AP RF-19 treats the
first exchange as `01`; the `_00` filename is the META filename index. Keep
the historical prompt byte-identical, but do not reproduce this ordinal
defect in future prompts.

## Session 27 host evidence

Exactly one new host policy file from product commit `ca6052e…` was
installed:

`packaging/udev/99-contextdeck-input-acl-guard.rules` →
`/etc/udev/rules.d/99-contextdeck-input-acl-guard.rules`

The installed file was recorded as a regular root-owned mode-0644 file and
byte-identical to the source. Its recorded SHA-256 is
`da87276d2997080205303e5ffcbc812b179d6d0747f32ce36e2d58bd8f3511e5`.
The neighboring 61-, 62-, and 99-uinput rules were not replaced.

The Cooperator then performed one narrowly targeted udev reload/trigger for
G213 event nodes, `/dev/port`, and the guarded i2c-dev class. `/dev/uinput`
was not triggered. Direct `setfacl` on live nodes was not used.

Session-user semantic readbacks agreed immediately and later:

- G213 event session ACL: absent on both interfaces;
- `/dev/port` session ACL: absent;
- guarded i2c session ACL: absent on all measured nodes;
- G213 hidraw session access: preserved;
- `/dev/uinput` session ACL: preserved;
- `/dev/uinput` broker ACL: preserved;
- broker unit: static/inactive/dead;
- input-remapper: enabled/active and unchanged.

This is host mitigation for the deployed ACL scope at the time of the
readback. It is not fresh INFOSEC `verified-closed`, not all-host evidence,
not uninstall safety, and not whole-G3 certification.

## Accepted named live slices

These are bounded named slices and must not be rerun merely because the
logical whole remains open.

| Session | Accepted boundary |
|---|---|
| 16 | SSH recovery, explicit authenticated ARM, sampled G213 pass-through, identity-checked cutoff/death, and post-death recovery |
| 19 | GUI ARM, armed G213, held-modifier watchdog abort, no restart/re-grab, and post-death recovery |
| 22 | One real suspend/resume cycle with pre-freeze stop, conditional disarmed restart, STATUS-only reconnect, and post-resume G213 typing |
| 23 | Compositor LED return to physical if00, deterministic LED-write failure behavior, all eighteen measured host-remappable controls, explicit DISARM, and final inactive cleanup |
| 24 | One non-G213 input-remapper mapping preserved before/during/after one armed G213 trial; bounded `if00=1/1` and `if01=1/1` coexistence evidence |

Session 23 retains its historical report-quality exceptions: a few semantic
media labels appeared despite the public-safe report rule, and the numeric
sudo-release marker was not returned although final runtime state was
verified. Do not rewrite or rerun Session 23.

Session 25 remains real historical `deployment-PARTIAL`: remove and
immediate rollback passed, candidate installation was skipped, and G3 was
not restored after the trigger cycle. Session 26 is real
`implementation-PASS`: it published the late ACL guard source correction.

## Current closure map

### Closed or accepted evidence

- G1’s eighteen-control matrix is accepted for the measured scope: F1–F12
  on if00 and six media/volume controls on if01.
- Game Mode and Backlight remain firmware-only and are outside the host
  remap catalog.
- The five named live G4 slices above are accepted as named slices.
- The Session 26 source correction is published in product commit `ca6052e…`.
- The Session 27 owner-path deployment mitigated the measured G3 ACL
  re-probe state on the authorized reference host.

### Still not claimed

- whole M2 or whole G4 closure;
- independent install/remove/rollback or production readiness;
- fresh independent INFOSEC closure of `G3-ACL-REPROBE-01`;
- general input-remapper coexistence;
- hibernate or hybrid-sleep support;
- separate G7 end-user power-action evidence;
- autostart or G8 safety;
- documentation reconciliation;
- license resolution for the product.

The Cooperator chose to park M2 rather than spend another R6 audit cycle.
This is a deliberate residual-risk decision, not evidence that the omitted
independent audit occurred.

## Documentation drift to carry forward

The product documentation may still contain older wording that predates
Sessions 22–24, including statements that live suspend, LED return, or
all-control fidelity remain unaccepted. Those are documentation drift and
must not override the newer named reports.

The milestone table may still show P1 as Planned even though G1 is closed.
Do not repair this inside M2. Documentation reconciliation belongs to a
later bounded documentation decision or the appropriate future whole.

## Product plan after M2

The Cooperator’s product vision is a complete ContextDeck cockpit for one
Logitech G213 Prodigy: keyboard context, session state, virtual desktops,
later remapping, a deck layer, and eventually system integration. This is a
sequence of logical wholes, not one Worker task.

| Whole | Identity | Scope | Status |
|---|---|---|---|
| M1 | `g213-contextdeck-mvp-context-lighting` | Context plus five-zone lighting | Done and accepted IRL |
| M2 | `g213-contextdeck-input-passthrough-safety` | Safe exclusive grab and pass-through | Parked here; named slices evidenced; host G3 mitigated |
| M3 | `g213-contextdeck-workspace-aware-lighting` | Desktop/app context represented by five RGB zones | Next whole |
| M4 | `g213-contextdeck-workspace-session-manager` | Virtual desktops, app assignment, launch, maximize | After M3 |
| remap | Future dedicated whole | Per-app consume-and-inject mappings | After the relevant safety design |
| deck | Future dedicated whole | Hold-to-layer interaction | After remap |
| M5 | `g213-contextdeck-system-integration-and-autostart` | Packaging lifecycle and login integration | Later; G8 lives here |

Do not collapse M3, M4, remap, deck, and M5 into one identity. Do not use
the unfinished M2 gates as a backlog for the next whole.

## Required next action

The next whole is:

`g213-contextdeck-workspace-aware-lighting`

The next fresh Orchestrator must:

1. clone or inspect public product and META repositories read-only;
2. verify product `ca6052e…`, AP `0cf2cff…`, META ancestry, the public
   Session 27 pair, and this handoff before routing;
3. explicitly state in Slovak that M2 is parked, G3 is host-mitigated but
   not independently re-audited, and M3 is the next whole;
4. open the new META trace directory
   `projects/contextdesk/00/03-g213-contextdeck-workspace-aware-lighting/`;
5. issue one fresh M3 Planner Worker prompt only.

The first M3 Worker is a Planner with `Native planning mode: required`,
fresh session ordinal `01`, exchange ordinal `01`, and no host mutation.
The Planner must produce a bounded plan for visible five-zone
workspace-aware lighting, schema 3 migration from schema 2, and session-app
subscription to `org.kde.KWin.VirtualDesktopManager`. It must not implement
M4, remapping, deck-layer behavior, M5, autostart, or broker ARM.

For any future live grab, exactly one independent recovery route is enough:
the already demonstrated SSH route from another device or a second physical
keyboard. Never demand both. M3’s first planning exchange needs no recovery
route because it must not touch the host or grab input.

## Archival instructions

The Cooperator owns META publication. Archive these exact files together as
the Session 27 first-add pair:

- `27_deployment_00.md` — issued prompt, not dispatched;
- `27_report_00.md` — owner-path report, not independent Worker report.

Do not rewrite historical Session 25 or Session 27 wording. Do not commit a
non-protocol `28_canvas.md` as a Worker exchange. This handoff becomes the
authoritative M2 park record only after it is publicly archived.

## Safety and language invariants

- Product target remains Logitech G213 Prodigy `046d:c336` on Linux/KDE
  Plasma 6/Wayland with C++20/Qt6/KF6/systemd.
- RGB is five-zone OpenRGB SDK protocol 5 over loopback; no per-key RGB
  claims.
- Exactly eighteen host-remappable controls remain in the measured matrix.
- Game Mode and Backlight are firmware-only. Never substitute PrintScreen or
  Pause. Code `166` is not a mapping contract.
- No keylogging, raw event lines, key names, scan values, typed content,
  serials, host addresses, host keys, passwords, or private paths in durable
  prompts, reports, or META.
- No automatic ARM after restart, resume, crash, or reconnect.
- No unproven autostart.
- Input-remapper coexistence is only the named Session 24 slice, not a
  general claim.
- Slovak is used with the Cooperator; Worker prompts and formal reports are
  in English.

M2 is parked with truthful residual evidence. The next routing decision is
not another M2 “smallest next step”; it is a fresh planning start for M3.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-foundation-architecture  
Worker session ordinal: 01  
Worker exchange ordinal: 01

- **status: PARTIAL**
- Phase-qualified result: not-applicable
- Result artifact or commit: not-applicable
- Result evidence: bounded read-only planning evidence
- Logical-whole closure: not-closed
- Start commit of the resumed reconnaissance: `ca3ac07c5fecfe3c983078e343ec6b3e02c75bea`
- End commit: `6b4e4b30c29b154a99a96061c1b692781f82c400`
- Changed files and purpose: none by this Worker; externally introduced changes are identified below.
- Tests and validation: repository, system, interface, dependency, and source inspection performed; no product tests exist.
- Commit and push result: not authorized / none.
- Implementation in this Worker session: prohibited.
- Delivery: this chat report only; no report file or other artifact was created.

The architecture is sufficiently specified to select bounded implementation work. **PARTIAL is required by the supplied task because material hardware evidence remains unavailable within read-only authority.** Those gaps now have explicit probes, acceptance conditions, and consequences. Further general planning cannot establish physical key routing, safe interception, or actual RGB behavior.

The recommended trajectory is: **typed profile model → reliable KWin context → useful application lighting → independently accepted input pass-through → contextual shortcuts → system actions → installation and autostart.**

**1. Verified baseline and repository state**

The product repository exists at the expected location and has the canonical `cisarik/contextdesk` remote. The original prompt’s expected commit, `319079287de7f651d5177fbb43f42da6799d174d`, was already stale when resumed reconnaissance began.

During this work, another actor introduced and committed AP integration:

| Item | Verified final state |
|---|---|
| Product branch | `main`, clean, two commits ahead of `origin/main` |
| Product HEAD | `6b4e4b30c29b154a99a96061c1b692781f82c400` |
| Product `origin/main` and checked public main | `ca3ac07c5fecfe3c983078e343ec6b3e02c75bea` |
| Externally changed paths | `.ap`, `.gitmodules`, `AGENTS.md` |
| Product source, build system, tests, CI | Absent |
| Immutable handout, README, LICENSE | Unchanged by those commits |
| Active Git operation | None found |

These changes were preserved. Their authorship and authorization are not established by this Worker’s observations.

AP is now integrated locally. The gitlink, `.ap` checkout, and inspected canonical AP revision agree on:

`7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`

The managed AGENTS block matched the pinned integration generator. The adjacent AP checkout was clean. `ap doctor` was not executed because its temporary-file behavior exceeded this exchange’s no-file-creation boundary; no doctor-PASS is claimed. **Do not schedule AP adoption again.**

META was verified at:

`465a8c5202735853ff246ea20e17c68e3a8de098`

Its tracked tree was clean, with untracked contextdesk material and unrelated project traces. The contextdesk handout copy matched the product handout. Neither its presence nor the additional untracked planning file proves completed archival.

The intended trace directory remains:

`projects/contextdesk/00/00-g213-contextdeck-foundation-architecture/`

The supplied exchange projects to `01_plan_00.md` and `01_report_00.md`. However, this conversation includes an earlier terminal response and subsequent human renewal. These report coordinates echo the supplied prompt; they do not authorize overwriting earlier history. The ORCHESTRATOR must reconcile continuation identity and preserve actual prompts and reports before archival.

**2. Evidence classification, capability handshake, and gates**

Throughout this report:

- **Verified** means directly inspected local state or identified primary-source content.
- **Proposed** means an architectural or product recommendation.
- **Unknown** means evidence that was not obtained; a proposed design does not resolve it.

| Capability | Requested versus observed |
|---|---|
| Product/client/model | Codex identity supplied by the environment; exact client build and model implementation not independently established |
| Reasoning | High requested; no independently measurable reasoning-setting evidence |
| Native planning mode | Required originally; actual mode was Default. Subsequent explicit human authorization renewed planning, without enabling native Plan mode |
| Continuity | Same continuing conversation; context compaction occurred. No fresh or independent Worker is claimed |
| Filesystem | Broad access declared; read-only inspection exercised; writes not exercised |
| Network | Public documentation, source, and public Git identity inspection exercised |
| Source inspection | Local installed headers, package source, pinned upstream source, and protocol documents inspected |
| Tests | No product test suite exists; physical/runtime acceptance was not authorized |
| Commit/push | Technically separate capabilities; neither authorized nor exercised |
| Delegation | None; one accountable Worker |
| Secrets | No credential probing or environment dump |

The remaining gates are finite:

| Gate | Required evidence or decision | What it blocks |
|---|---|---|
| **G0 — Baseline** | ORCHESTRATOR confirms ownership and selects the current product commit; reconciles trace continuation | Any repository mutation against an assumed baseline |
| **G1 — Physical controls** | Cooperator-assisted routing matrix for all 20 requested controls | Claims about physical event ownership and special-button remapping |
| **G2 — RGB behavior** | Approved OpenRGB installation/access trial, five-zone update, coexistence and reconnect evidence | Shipping the selected RGB route |
| **G3 — Device authority** | Cooperator accepts exact input/RGB access boundaries and residual risks | Service accounts, device rules, broker deployment |
| **G4 — Input safety** | Hardware acceptance of interception, crash, hang, release, and recovery behavior | Enabling remapping for normal use |
| **G5 — Desktop behavior** | KWin lifecycle, identity, shortcut recording, and focus-race measurements | Claims of accepted contextual behavior |
| **G6 — Licensing** | Product license decision and dependency provenance review | Unresolved code reuse and release |
| **G7 — Power actions** | Authorized display-off and suspend acceptance | Enabling those actions |
| **G8 — Release lifecycle** | Independent acceptance, installation/removal and autostart recovery | Shipping an automatically grabbing installation |

G1 and G2 are the immediate material hardware gaps. G4–G8 are planned implementation acceptance gates, not claims that implementation already exists.

**3. Hardware capability map**

Verified device identity is Logitech G213, USB `046d:c336`. Both inspected USB interfaces remained bound through `usbhid`; their HID devices used `hid-generic`.

Current node numbers are evidence from this workstation, **not configuration identifiers**.

| Surface | Verified evidence | Remaining uncertainty |
|---|---|---|
| USB interface 00 | Boot keyboard interface; currently `event7` and `hidraw2` | Actual routing of each physical control |
| USB interface 01 | Additional keyboard, consumer-control, and vendor reports; currently `event8` and `hidraw3` | Which buttons generate which reports |
| Keyboard report on interface 01 | Report ID `0x01`, keyboard array | Physical routing and duplication behavior |
| Consumer report | ID `0x02`; descriptor includes transport, volume and mute usages | Actual emitted sequences |
| Vendor reports | Page `0xff43`; report IDs `0x11` and `0x12` | Button observability and device-specific response behavior |
| Lighting | Five physical RGB zones | Actual runtime write/reconnect behavior on this device |
| Game Mode / Backlight | Documented firmware functions | Whether either provides a safely remappable host event |

**Both event nodes advertise the relevant F-key and media-key capabilities.** Capability bitmaps therefore cannot select the owning event node.

The requested event-code candidates are:

| Controls | Linux key codes |
|---|---|
| F1–F10 | 59–68 |
| F11, F12 | 87, 88 |
| Previous, Play/Pause, Next | 165, 164, 163 |
| Mute, Volume Down, Volume Up | 113, 114, 115 |

The official product documentation confirms five lighting zones. Game Mode normally disables the Windows key, while Backlight controls lighting. Those descriptions do not establish remappable Linux events. [Logitech lighting documentation](https://support.logi.com/hc/en-001/articles/360023175994-Customize-lighting-settings-on-the-G213-gaming-keyboard-with-Logitech-Gaming-Software), [Logitech button documentation](https://support.logi.com/hc/en-gb/articles/360023344553-Game-Mode-and-backlighting-control-on-the-G213-gaming-keyboard)

**4. Event discovery and the bounded physical probe**

No key listener, grab, virtual keyboard, or physical special-button probe ran.

The future G1 probe should produce one capability table containing: physical control, USB interface, event source, press/release/repeat sequence, firmware effect, and confidence.

Procedure:

1. Establish an independent recovery method before any later grabbing experiment.
2. Identify nodes from verified USB ancestry and interface metadata.
3. Observe both relevant event sources during a controlled, non-grabbing session.
4. Test F1–F12 and the six requested media controls with three deliberate press/release cycles and a hold where meaningful.
5. Under explicit authority for firmware-state changes, test Game Mode and Backlight in both directions.
6. Record only the requested controls and sanitized metadata. Do not retain ordinary typed keys, arbitrary vendor payloads, or a general input transcript.
7. Restore deliberately changed firmware state.
8. Separate event discovery from the later suppression/grab experiment.

For special buttons, “no EV_KEY observed” is insufficient to conclude “firmware-only.” Their vendor-report behavior and firmware side effects must be considered.

If a special button is firmware-only, cannot be consumed safely, or retains an unacceptable firmware side effect, mark that mapping unsupported. The COOPERATOR then chooses omission or an alternative control. **PrintScreen and Pause/Break must never silently substitute for these buttons.**

**5. Recommended architecture**

Use **C++20, Qt6, KF6, CMake, and a small Kirigami/QML settings interface**.

The product has two owned processes and one conditional external RGB service:

| Component | Responsibility | Explicit boundary |
|---|---|---|
| Session application | Tray, settings, profiles, KWin context, application inventory, RGB client, approved desktop actions | No raw keyboard-device access |
| Input broker | Verified G213 event routing, policy application, virtual input, lifecycle safety | No QML, RGB, network client, shell execution, or ordinary-key logging |
| External OpenRGB service | Selected G213 lighting transport | Separately reviewed device access and lifecycle |

Within the session application, keep the profile resolver and state machines deterministic and independent of GUI objects. Input processing must not wait for configuration parsing, disk writes, the GUI thread, RGB traffic, or desktop-action completion.

A settings-window crash or closure must not define the lifetime of input ownership. Conversely, loss of the controlling session application must expire the broker’s authority and disarm remapping.

Do not create additional daemons for application inventory, configuration, or diagnostics. The input boundary is justified by its failure and privilege consequences.

**6. Alternatives considered**

| Route | Advantages | Relevant limitations | Decision |
|---|---|---|---|
| Existing input-remapper | Installed; established input machinery | Inspected preset replacement stops and starts an injector; no demonstrated atomic focus-generation contract | Preserve existing use; reject focus-triggered preset switching as the product engine |
| libevdev + uinput | Device-specific filtering; explicit pass-through and state ownership | Highest implementation and acceptance burden | Recommended input route, conditional on G3/G4 |
| KGlobalAccel | Native KDE global actions | Does not provide the required physical-G213 interception and conditional pass-through model | Optional application commands only |
| libei / desktop portals | Supported compositor-mediated facilities | Do not supply the required always-available physical G213 filter in the inspected interfaces | Not the primary backend |
| KWin modification | Could move decisions closer to compositor delivery | Maintenance, deployment and recovery cost; materially larger project | Reserve for a separately approved future requirement |
| G213Tray-style direct USB access | Demonstrates protocol feasibility | Inspected implementation detaches interface 01; GPL code cannot be casually reused | Research evidence only |

KGlobalAccel’s action model is useful for ordinary global application shortcuts, but does not establish device-specific remapping. The InputCapture portal also has compositor-controlled activation semantics unsuitable for assuming an always-active G213 filter. [KGlobalAccel API](https://api.kde.org/kglobalaccel.html), [InputCapture portal](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.InputCapture.html)

For UI, Qt Widgets remains viable, but Kirigami/QML better fits the intended compact KDE settings experience. Python/PyQt adds no decisive advantage to the latency-sensitive broker. Electron and a web UI contradict the accepted product direction.

**7. Input-backend decision and operating contract**

Select a **small libevdev/uinput broker**, initially disabled and independently accepted before normal use.

Verified existing input-remapper state:

- Version `2.2.0-1`; system daemon active and enabled.
- The queried G213 group returned `UNKNOWN`.
- The separately queried mouse group returned `RUNNING`.
- Autoload configuration selected the mouse preset.
- The G213 preset file inspected was a zero-byte placeholder.
- Complete enumeration of other processes’ open device descriptors was unavailable.

`UNKNOWN` is not proof that no process holds any G213 node. Preserve the mouse configuration and daemon. Never use `stop_all` as conflict resolution.

The broker contract must include:

- Match real USB ancestry, exact VID/PID, approved interfaces, and verified device identity.
- Reject virtual devices and unrelated keyboards.
- Create the required virtual device before attempting exclusive ownership.
- Arm only from a quiescent state; explicitly test keys pressed during acquisition.
- Treat multi-node acquisition as non-atomic. If any claim fails, release all acquired claims and return to disarmed state.
- Freeze the resolved action at physical key-down.
- Maintain separate physical and synthetic key-ownership records.
- Balance every synthetic press with a release.
- Never release a modifier merely because another device might have pressed it.
- Handle `SYN_DROPPED` by state reconciliation; reconstructed pressed state must not trigger commands.
- Preserve pass-through event framing, supported indicators, and repeat semantics without duplicate repeat generation.
- Cancel pending mapped actions on invalid context, lock, session loss, or disconnect.
- Never replay queued actions after recovery.

For the first shortcut implementation, emit one completed chord per deliberate press. Preserve native repetition for pass-through controls. Configurable shortcut repetition can follow only after its state transitions are accepted.

Conflicting held modifiers require an explicit policy. The safe initial policy is pass-through for an incompatible physical modifier state. Access to unrelated keyboards must not be expanded to normalize their modifiers.

**8. RGB-backend decision**

Select **OpenRGB through one persistent, bounded SDK connection**, subject to G2.

OpenRGB was not installed, and no inspected OpenRGB service or SDK listener was present. The inspected Arch/CachyOS candidate was `1.0rc3`, with package release differences between repositories.

Source selection matters:

- Inspected `release_candidate_1.0rc3` commit: `6fbcf62d7694e7b92fd0a5884b40b92984fbd1b0`.
- That source uses SDK protocol **5**.
- The master SDK document describes newer protocol material, including protocol 6. It must not be used as if it were the packaged implementation. [Pinned protocol header](https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/6fbcf62d7694e7b92fd0a5884b40b92984fbd1b0/NetworkProtocol.h), [SDK documentation](https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/Documentation/OpenRGBSDK.md)

The inspected G213 backend identifies interface 01 and the relevant vendor usage. Its SDK representation is **one linear zone containing five color entries**, corresponding to the five physical zones.

Use whole-device five-color updates. The inspected single-entry update implementation contains a suspicious channel assignment; this is a source-level concern, not a reproduced hardware defect. Direct-mode selection and the full update path must be proven together. [Pinned G213 RGB controller](https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/6fbcf62d7694e7b92fd0a5884b40b92984fbd1b0/Controllers/LogitechController/LogitechG213Controller/RGBController_LogitechG213.cpp)

Implement a small independently authored QtNetwork client for the required protocol subset:

- Explicit protocol negotiation and supported-version rejection.
- Bounded packet lengths, counts and strings.
- Correct partial-read handling and timeout behavior.
- Enumeration and exact G213 selection.
- Whole-device color updates.
- Device-list-change handling.
- Reconnection with fresh enumeration.
- Latest desired color retained; stale queued colors discarded.

Controller indices are not durable identities. Re-enumerate after device-list changes and connection loss.

The SDK does not provide optical confirmation that the keyboard displayed a color. Sending successfully is not hardware acceptance. The UI should distinguish desired state, connection state, and failure without claiming physical readback.

Require loopback binding: the inspected default server host was all interfaces. Loopback is still not authentication between local users.

Do not install a second direct-HID backend in the MVP. If G2 rejects OpenRGB, reopen only the RGB transport decision. Any direct-HID alternative must use a separately reviewed non-detaching route with explicit provenance and device-access authority.

**9. Foreground context and KWin**

Use an event-driven KWin script.

The generated API documentation identifies an older generation, so relevant interfaces were also checked against KWin `6.7.5` source, commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`.

Verified source surfaces include `activeWindow`, `windowActivated`, window addition/removal, `windowList()`, application identity properties, asynchronous `callDBus`, and `QTimer`. [KWin scripting wrapper](https://invent.kde.org/plasma/kwin/-/blob/ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7/src/scripting/workspace_wrapper.h), [Script implementation](https://invent.kde.org/plasma/kwin/-/blob/ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7/src/scripting/scripting.cpp)

Identity resolution:

1. Prefer normalized `desktopFileName`.
2. Fall back to exact `resourceClass`, with `resourceName` where needed.
3. Resolve suitable transient dialogs through a bounded, cycle-safe parent relationship.
4. Use desktop metadata for friendly names and icons.
5. Keep captions out of default matching and diagnostics.
6. Do not use PID scanning or executable paths as the normal identity source.

The application owns a new D-Bus receiver, for example `io.github.cisarik.ContextDeck.Context1`. This is a proposed product API, **not an existing KWin method**.

Each message carries a bridge instance, sequence number and context snapshot. The receiver authenticates the expected bus owner, rejects stale messages, and compiles an immutable policy revision for the broker. A heartbeat detects bridge loss without title polling.

The running-app picker deduplicates windows by resolved application identity. Selecting a profile does not activate or terminate an application.

Context behavior must be explicit:

| Condition | Mapping behavior |
|---|---|
| Identified application with profile | App overrides over global defaults |
| Identified ordinary application without profile | Global defaults |
| Unknown/stale context, locked session, no active window | Pass-through |
| ContextDeck settings or unsuitable shell surface | Neutral/pass-through |
| Reconnection or resume | Wait for fresh context and policy synchronization |

The COOPERATOR explicitly accepted measured best-effort focus safety:

- Cancel actions known to be stale.
- Pass through when uncertainty is detected before consumption.
- Measure the remaining interval between context observation and input delivery.

After a physical press has already been consumed, cancellation must finish balanced state cleanup; it must not replay the original press into a newly focused application.

This architecture cannot guarantee delivery to the original window across an unobserved compositor focus transition. The accepted decision removes the need to pursue a KWin modification for that guarantee.

**10. Native GUI and product interaction**

Use one `QApplication`-based session process with `KStatusNotifierItem`; create the Kirigami settings window lazily. `QApplication` is appropriate because tray menus use Widgets facilities. Closing settings leaves the tray process running. [KStatusNotifierItem API](https://api.kde.org/kstatusnotifieritem.html)

The initial interface needs four comprehensible areas:

- **Overview:** current application, resolved profile, remapping state, lighting state.
- **Profiles:** global defaults and application profiles.
- **Controls:** supported physical controls and typed assignments.
- **Diagnostics:** actionable component health without input transcripts.

Display five physical zones truthfully, while offering one base color in v1.

Keep lighting mode explicit:

| Mode | Meaning |
|---|---|
| Automatic | Current profile controls all five zones |
| Temporary color | Lasts until the next meaningful external application-identity change |
| Lights off | Explicit session override until Automatic is resumed |

Opening the tray or settings must not unexpectedly expire a temporary color. Input mappings continue to follow their own automatic policy. An override must never remain hidden beneath an “Automatic” label.

The shortcut recorder:

- Operates only while its capture control has focus.
- Obtains acknowledgement that relevant remapping is paused.
- Cancels on focus loss and timeout.
- Records a bounded chord, never a macro or arbitrary command string.
- Shows the recorded layout context.

The workstation exposes `org.kde.KeyboardLayouts` at `/Layouts`, including `layoutChanged` and `layoutListChanged`. Subscribe to these for revalidation. Conversion from Qt native key information to Linux key codes requires integration evidence; never assume an unverified scan-code offset.

For v1, adopt explicit physical-key chord semantics and require review when layout changes invalidate the displayed meaning. Layout-independent symbolic shortcuts are a separate capability, not an implicit promise.

**11. Process and service lifecycle**

The session application owns desired configuration and user interaction. The broker owns effective input state.

Use leases and acknowledgements:

- A policy is not effective until the broker acknowledges its revision.
- A lost session owner or expired lease disables mapping.
- A stale GUI must not keep the broker armed.
- A restarted component starts disarmed until fresh state is established.
- Hardware reconnect does not replay actions.
- A crash does not cause an automatic grab/restart loop.

The broker alone owns real input and uinput descriptors. Use close-on-exec and avoid descriptor copies in parent processes.

A systemd watchdog must be fed by the actual input event loop, so a blocked loop cannot appear healthy through a separate heartbeat thread. An initial two-second watchdog interval is a proposed acceptance target, not an observed recovery time.

KWin and session discovery require care: querying `loginctl ... self` from the tool process failed because it ran under the user manager. Explicit enumeration found the active local Wayland session. Broker authorization must therefore resolve the authenticated user’s eligible graphical session and seat; it cannot assume the caller PID belongs directly to that session.

Do not attempt to become a second logind session controller beside KWin. `TakeControl`/`TakeDevice` are not a general independent device-access solution. [logind D-Bus contract](https://www.freedesktop.org/software/systemd/man/latest/org.freedesktop.login1.html)

**12. Configuration contract**

Use one authoritative versioned profile document, proposed location:

`$XDG_CONFIG_HOME/contextdeck/profiles.json`

Its model includes schema version, G213 scope, global profile, application profiles, typed actions, base colors and relevant preferences.

Resolution must be unambiguous:

| Stored value | Meaning |
|---|---|
| App assignment absent / Inherit Global | Resolve from global profile |
| Global assignment absent | Pass Through |
| Pass Through | Preserve the physical control’s normal input |
| Disabled | Deliberately consume this control |
| Emit Shortcut | Emit one validated chord |
| Approved System Action | Invoke a fixed supported action |

“Disabled” must never be inferred from missing configuration.

Validation rules:

- Reject unknown executable action types.
- Reject unsupported schema versions for activation.
- Reject unknown semantic fields in the current schema; do not silently discard them.
- Preserve invalid or newer files without rewriting them.
- Validate the entire draft before activation.
- Use atomic `QSaveFile` replacement without direct-write fallback.
- Keep a bounded last-valid backup.
- Separate “saved configuration” from “hardware currently available.”
- On a cold start with no valid configuration, remain pass-through.

`QSaveFile` provides the appropriate replacement primitive; power-loss durability still depends on the full write/synchronization implementation and filesystem. [Qt QSaveFile](https://doc.qt.io/qt-6/qsavefile.html)

KConfig may store window geometry and presentation preferences. It must not become a second owner of profile semantics.

**13. Permissions and security model**

Verified current access:

- G213 event nodes: `root:input`, mode `0660`, no inspected active-user ACL.
- The current user was not a member of the broad `input` group.
- G213 hidraw nodes: `root:root`, mode `0600`.
- `/dev/uinput` already had an active-user ACL associated with KDE Connect policy.

Existing access does not grant authority to use it. Uinput permission cannot be restricted to “inject only for VID/PID 046d:c336.”

Recommend a dedicated, unprivileged broker identity with narrowly scoped G213 event-device access and uinput access. Keep raw input permissions away from the GUI account. The exact udev and service policy must be reviewed and tested under G3; this report does not prescribe unverified rule syntax.

**The RGB interface also exposes keyboard reports.** Granting hidraw access to the ordinary session account as if it were lighting-only would expand input visibility.

Prefer a separate restricted identity for the external RGB service, with only the verified G213 interface accessible. Audit package-installed rules before deployment. Do not grant broad hidraw, input-group, I²C, SMBus, or raw USB access.

Broker IPC should:

- Authenticate the sender’s system-bus credentials.
- Bind to one eligible active local session and seat.
- Reject inactive, ambiguous and unauthorized callers.
- Accept only bounded policy objects for approved G213 controls.
- Expose no general “inject arbitrary keys now” operation.
- Independently observe session lock and lifecycle changes.

Same-user compromise and application identity spoofing remain limitations. D-Bus names and window metadata are not a strong security boundary against a compromised desktop session.

Disable input-process core dumps and keep diagnostics bounded to state transitions, error classes and counters. Do not log ordinary keys, window captions, device serials or raw HID reports.

**14. Licensing implications**

The MIT root license is existing repository evidence, not a resolved human licensing decision.

| Component | Inspected version/reference | License evidence | Planned relationship |
|---|---|---|---|
| Product | Current tree | MIT file present; decision unresolved | Independently authored code |
| Qt6 | Installed 6.11.2 family | Relevant modules offer LGPLv3/GPL/commercial routes | Dynamic linking under a reviewed compatible route |
| KF6 | Installed 6.30.0 family | Module/file-specific LGPL terms | Dynamic linking; retain notices and obligations |
| KScreen DPMS | Plasma 6.7.5 | Inspected DPMS files LGPL-2.1-or-later | Native linked API |
| libevdev | 1.13.7 | MIT | Broker dependency |
| libsystemd | systemd 261.2 | Relevant library licensing requires component-level record | Broker/session integration |
| libxkbcommon, if used | 1.13.2 | Permissive notices vary by included material | Shortcut translation |
| OpenRGB | `1.0rc3`, pinned source above | GPL-2.0-or-later source | Separate external process; no source copying |
| OpenRGB-cppSDK | `12159516e47da6b56bac669b7daaa266a615e2de` | Top-level MIT; inspected utility submodule grants unresolved | Not selected |
| openrgb-python | Inspected upstream | GPLv3 | Studied only |
| G213Tray | `6d621621f42cd021b9a0d74ce58bcf043f07fd86` | GPL-3.0-or-later | Studied only |
| input-remapper | 2.2.0 | GPL-3.0-or-later | Existing independent installation |
| hidapi | 0.15.0 installed | Alternative BSD/GPL/original-license options | Possible later direct-HID route only |
| uinput | Kernel interface | No external userspace helper selected | Independently authored interface use |

The inspected C++ SDK also targets protocol 3 and relies on two utility submodules whose redistribution grants were not established. Protocol negotiation could address version compatibility; it does not resolve missing provenance. [OpenRGB-cppSDK](https://github.com/Youda008/OpenRGB-cppSDK)

**Recommendation:** retain MIT for independently authored product code, use compatible dynamic-library routes, and keep OpenRGB external. This remains conditional on final dependency review and the COOPERATOR’s decision. Process separation alone is not a universal licensing exemption. [Qt LGPL obligations](https://www.qt.io/development/open-source-lgpl-obligations), [GNU guidance on combined programs](https://www.gnu.org/licenses/gpl-faq.html#MereAggregation)

No third-party source was copied into the product.

**15. MVP scope**

The MVP should deliver a coherent daily workflow:

1. Tray application with trustworthy component status.
2. Global defaults and per-application profiles.
3. KWin application inventory and foreground resolution.
4. One profile color across all five zones.
5. Explicit temporary lighting override.
6. Assignments for physically verified F1–F12 and six media controls.
7. Inherit, pass-through, disabled and single-chord actions.
8. Configuration validation and recovery.
9. Safe manual enable/disable and disconnect handling.
10. Approved system actions after separate acceptance.

Game Mode and Backlight mappings are conditional capabilities. The MVP must not depend on pretending that these buttons are interceptable.

Defer advanced five-zone editing, animated effects, macros, scripting, profile marketplaces, other keyboards, cross-platform support and a second RGB backend.

The product’s ambition should come from dependable context behavior and polished recovery, not from the number of configurable mechanisms.

**16. Implementation verticals and logical-whole candidates**

Each row is a separately bounded candidate, not implementation authority.

| Stage | Logical-whole candidate | Concrete outcome |
|---|---|---|
| V0 | Baseline reconciliation | Confirm current local AP integration and authoritative product baseline |
| V1 | `g213-contextdeck-profile-contract` | Typed model, resolution, validated persistence and meaningful tests |
| P1 | `g213-contextdeck-control-evidence` | Approved physical-control matrix |
| V2 | `g213-contextdeck-kwin-context` | Native tray, event bridge and deduplicated application inventory |
| P2 | `g213-contextdeck-rgb-evidence` | Approved OpenRGB access, five-zone and lifecycle evidence |
| V3 | `g213-contextdeck-application-lighting` | First usable profile-to-lighting workflow |
| V4 | `g213-contextdeck-input-passthrough-safety` | Narrow broker, pass-through only, crash/recovery evidence |
| V5 | `g213-contextdeck-one-context-shortcut` | One verified control mapped in one application |
| V6 | `g213-contextdeck-key-profiles` | Expand accepted mappings and recorder to the verified control catalog |
| V7 | `g213-contextdeck-system-actions` | Separately accepted Displays Off and Suspend |
| V8 | `g213-contextdeck-release-lifecycle` | Packaging, removal, explicit autostart opt-in and release acceptance |

V3 supplies useful product value before exclusive input ownership. V4 deliberately excludes remapping so failures can be attributed to interception itself.

V5 uses a harmless, observable target action. Expansion to all controls follows evidence from this narrow path.

**17. Dependency order and toolchain**

Verified environment:

| Area | Installed evidence |
|---|---|
| OS/session | CachyOS, Arch family; active local Wayland session |
| Kernel | `6.18.48-1-cachyos-lts` |
| Plasma/KWin | `6.7.5-1.1` |
| systemd | `261.2-1` |
| Qt6 | `6.11.2` package family |
| KF6 | `6.30.0` package family |
| CMake / Ninja | `4.4.3` / `1.13.2` |
| Compilers | GCC 16.2.1 and Clang 22.1.8 |
| libevdev / libinput | `1.13.7` / `1.31.3` |
| KDE development support | Relevant headers and CMake targets present; extra-cmake-modules absent |

Use QtCore-level dependencies for V1. Add Qt Widgets, QML, Kirigami and required KF6 modules when their vertical needs them. Add QtNetwork for RGB; libevdev/libsystemd for the broker.

Dependency order:

- V1 precedes policy consumers.
- V2 depends on V1.
- V3 depends on V2 and P2.
- V4 depends on P1, G3 and an established recovery procedure.
- V5 depends on V2 and accepted V4.
- V6 depends on accepted V5.
- V7 depends on accepted action/state handling and G7.
- V8 depends on accepted applicable product paths and G6/G8.

P1 and P2 can be scheduled independently of core implementation through manually dispatched tasks. No automated Workers are implied.

Do not invent current build commands. The repository has no build system yet.

**18. Risk ranking**

These are planning assessments, not INFOSEC findings or an audit result.

| Risk | Initial severity | Required control and evidence |
|---|---|---|
| Keyboard lockout or stuck modifiers | Critical | Descriptor ownership, cleanup, watchdog, hardware crash tests, independent recovery |
| Broad input visibility/keylogging | High | Narrow device identity, isolated broker, no raw-event IPC/logging |
| RGB hidraw access exposing keyboard reports | High | Separate access boundary and package-rule review |
| Duplicate/phantom events or virtual feedback | High | Physical ancestry checks, event-state ledger, acquisition/release tests |
| Unrestricted uinput injection | High | Isolated broker, authenticated bounded IPC, physical-trigger requirement |
| Wrong-context shortcut | High | Accepted race model, generation checks, cancellation, measured residual |
| Lock/session transition injection | High | Independent session checks, lease expiry, fresh-state requirement |
| Malicious configuration | High | Typed bounded schema, atomic validated activation, no executable payload |
| Arbitrary execution through actions | High | Fixed action dispatch; no shell strings |
| Device ownership conflict | High | Single owner, fail on conflict, no force-detach or broad daemon stop |
| Broken autostart/restart loop | High | Disarmed startup, no automatic re-grab after crash, independent acceptance |
| Suspend misuse | High | Explicit typed action, release-triggering, policy checks and debounce |
| Local RGB SDK misuse | Medium | Loopback, restricted device scope; acknowledge lack of per-user authentication |
| Layout mismatch | Medium | Defined chord semantics and layout revalidation |
| Public diagnostic/META leakage | Medium | Redaction, no input transcripts, exact public-safe archival |
| RGB latency or stale color | Medium | Latest-only updates, bounded queues, reconnect and coalescing |

Typed shortcuts still invoke whatever the receiving application assigns to that chord. They do not make every user-selected shortcut harmless.

Recommended later routes are R1 for bounded non-input implementation, escalating to applicable R3/R4 review for input, uinput, device permissions, HID and autostart. Future host-policy changes and hardware trials require their appropriate E4/E3 envelopes. No audit PASS is asserted here.

Residual medium-or-higher risks remain COOPERATOR-owned.

**19. Acceptance and evidence per vertical**

| Vertical | Required acceptance |
|---|---|
| V1 | Inherit/pass-through distinction; profile precedence; malformed/future schema; failed-save preservation; migration failure |
| P1 | Repeatable physical event matrix; special-button firmware effects; no ordinary-key transcript |
| V2 | Initial snapshot; focus/add/remove events; multi-window deduplication; dialogs; shell/no-window; bridge restart; stale sequence rejection |
| P2 | Actual five-zone color; repeated updates; driver remains bound; input remains usable; reconnect; access scope |
| V3 | Correct profile color; override expiry; no UI blocking; malformed SDK frames; server loss; device-list changes |
| V4 | No remapping; correct pass-through; no virtual loop; acquisition failure rollback; crash, hang, unplug and held-key recovery |
| V5 | One complete chord; no stale repeat; correct release on focus change; preserved fallback semantics |
| V6 | All approved controls; layout handling; recorder cancellation; modifier conflicts; unchanged unrelated devices |
| V7 | Policy-respecting suspend; unchanged display topology; normal wake; no repeat/phantom power action |
| V8 | Install/remove recovery; inactive-session rejection; opt-in startup; failure recovery; fresh independent acceptance |

Test layers:

- **Deterministic:** profile resolver, state transitions, policy generation, serialization, bounded protocol parsing.
- **Integration:** D-Bus ownership, KWin bridge lifecycle, broker leases, simulated RGB server behavior.
- **Hardware:** actual G213 routing, pass-through, interception, five-zone writes and reconnection.
- **Desktop:** application focus races, layout changes, lock/unlock, multi-monitor DPMS and suspend/resume.

Hardware input acceptance must include `SIGTERM`, `SIGKILL`, and a stopped/hung broker recovered by the watchdog. Exercise failure during physical holds, synthetic modifier ownership, focus changes, acquisition and release.

Linux source supports the cleanup design: evdev closes release grabs, uinput closes destroy the virtual device, and input-device disconnection releases pressed keys. This does not substitute for testing the installed kernel and compositor. [evdev release](https://github.com/torvalds/linux/blob/v6.18/drivers/input/evdev.c), [uinput release](https://github.com/torvalds/linux/blob/v6.18/drivers/input/misc/uinput.c), [input disconnection](https://github.com/torvalds/linux/blob/v6.18/drivers/input/input.c)

Proposed initial performance targets, to be measured rather than claimed:

- Input event receipt to virtual dispatch: p99 ≤ 5 ms under the defined acceptance workload.
- Context-message receipt to broker policy acknowledgement: p99 ≤ 10 ms.
- RGB updates coalesced to at most 20 per second, sending only changed desired state.
- Separately report software dispatch latency and physically observed lighting latency.
- Report focus-race trials and failures; zero observed failures does not prove impossibility.

Acceptance records must identify workload, sample count, versions and measurement points. No ordinary typed input is needed for these measurements.

**20. Rollback and recovery**

Before the first grab:

- Establish and verify an independent recovery channel, such as a second keyboard or usable TTY access.
- Document how to stop the exact owned broker.
- Confirm the broker is not automatically started.
- Confirm existing input-remapper mouse behavior remains intact.

Recovery order:

1. Disarm new mapping and discard queued actions.
2. Release owned synthetic state.
3. Destroy the virtual input device and release real-device ownership.
4. Keep the real keyboard available.
5. Require explicit re-enablement after a crash or serious state fault.

A dead process cannot run its cleanup handler; descriptor/kernel behavior is therefore essential. A hung process needs an external watchdog.

RGB failure disables the lighting path while preserving input behavior. Do not automatically switch to direct HID, detach a USB driver, or restart unrelated RGB software.

Configuration recovery preserves the invalid file, restores only an identified last-valid candidate, and reports failure without destructive migration.

Later uninstall must reverse only owned units, rules, application files and KWin package installation. Preserve user profiles by default. Never reset Plasma configuration or disable unrelated input-remapper services.

**21. Durable owners and proposed paths**

No paths below were created.

| Artifact | Proposed owner/path |
|---|---|
| Product behavior and terminology | `docs/specification.md` |
| Component boundaries | `docs/architecture.md` |
| Context/input decision | `docs/adr/0001-context-and-input-routing.md` |
| RGB decision | `docs/adr/0002-rgb-backend.md` |
| Device-access decision | `docs/adr/0003-device-access.md` |
| Threat model and safety invariants | `SECURITY.md` |
| Measured G213 capabilities | `docs/hardware/g213-capabilities.md` |
| Acceptance procedures | `docs/testing.md` |
| Install, recovery, removal | `docs/operations.md` |
| Deferred features | `docs/roadmap.md` |
| Deterministic model | `src/core/` |
| Session application | `src/session/`, `ui/` |
| Input broker | `src/input/` |
| RGB adapter | `src/rgb/` |
| KWin package | `kwin/` |
| Tests | `tests/unit/`, `tests/integration/`, later authorized hardware harnesses |
| Packaging | Later `packaging/arch/`, `packaging/systemd/`, `packaging/udev/` |

Each durable claim should have one owner. ADRs explain decisions; the specification owns behavior; hardware evidence owns measured capabilities.

META holds exact historical exchanges. It is not a live specification or task queue. No `BOOT_*`, `NEXT_*`, session diaries or Worker-state files should be introduced.

**22. Recommended first implementation Worker scope**

Recommend **`g213-contextdeck-profile-contract`** after G0.

Objective: implement and validate the smallest complete profile model that later context, GUI, RGB and input components can consume.

The future prompt should explicitly allow only:

- Minimal CMake build definition for this concrete core.
- Typed action and profile definitions.
- Deterministic global/app resolution.
- Strict schema parsing and validated atomic persistence.
- Meaningful unit tests for precedence, invalid configuration and write failure.
- The specification sections and ADR content necessary to own those behaviors.

Suggested initial changed-path boundary:

`CMakeLists.txt`, `src/core/`, `tests/unit/`, and explicitly named documentation files.

Exclude raw devices, uinput, KWin installation, RGB connections, packages, services, udev, power actions, autostart, AP changes and META.

Use the exact baseline selected by the ORCHESTRATOR; do not reuse the original stale expected commit. Commit authority, if desired, must be explicit.

This slice produces a real behavioral foundation without assuming any unmeasured device capability.

**23. Decisions still owned by the COOPERATOR**

Already accepted during this continuation:

- Measured best-effort focus handling, stale-action cancellation and safe fallback.
- Continued deep planning.
- Chat-only report delivery.

Still requiring a concrete decision at the relevant gate:

| Decision | Recommendation |
|---|---|
| Current baseline ownership | Confirm and retain the observed AP integration if authorized |
| Input access | Isolated narrow broker; no broad user input-group membership |
| RGB access/backend | Restricted external OpenRGB route, conditional on G2 |
| Product license | Retain MIT under the proposed dependency boundaries, after provenance review |
| Special buttons | Accept only demonstrated capabilities; choose omission or alternative explicitly if necessary |
| Shortcut semantics | Approve visible v1 chord/layout behavior |
| Residual risks | Accept measured focus risk and reviewed local IPC/device-access residuals |
| Autostart | Explicit opt-in only after independent acceptance |
| Publication | Separate release and remote-push authority |

No additional permission is needed merely to accept or reject this architecture. Hardware trials and host changes need concrete future tasks naming their mutation classes.

**24. What must not be implemented yet**

Do not:

- Start a grabbing backend automatically.
- Assign Game Mode to Suspend or Backlight to Displays Off before G1.
- Assume event capability bits prove physical routing.
- Grant broad input or hidraw access for convenience.
- Treat the RGB HID interface as incapable of exposing keyboard input.
- Detach interface 01 or copy the G213Tray implementation.
- Stop all input-remapper injectors or disturb the mouse preset.
- Spawn a CLI process for every focus/color change.
- Add a second RGB backend before the first is accepted or rejected.
- Promise exact-window shortcut delivery through asynchronous KWin plus uinput.
- Implement per-key lighting, arbitrary shell actions, macros or other-keyboard support.
- Remove outputs from KScreen topology to turn displays off.
- Write to `/sys/power/state` or bypass masked power policy.
- Package or enable services before their hardware behavior is proven.
- Copy third-party code with unresolved licensing.
- Re-bootstrap AP, rewrite the immutable handout, or archive this report automatically.

For Displays Off, the inspected native route is `KScreen::Dpms` through `KF6::ScreenDpms`; the older proposed PowerDevil DPMS D-Bus object was absent. The native API supports changing DPMS mode without removing outputs. Actual multi-monitor off/wake behavior remains G7 evidence. [KScreen DPMS implementation](https://invent.kde.org/plasma/libkscreen/-/blob/v6.7.5/src/libdpms/dpms.cpp)

For Suspend, the inspected `sleep.target` and `suspend.target` were loaded, static and not masked; logind returned `CanSuspend = "yes"`. This corrects the historical workstation assumption. No suspend was executed. Future actions must continue through logind/systemd policy.

**Validation evidence summary**

Read-only command families included:

- `git status --short --branch`, `git rev-parse`, `git diff`, `git submodule status`, and public `git ls-remote` checks.
- `pacman -Q`, package metadata queries, installed header inspection.
- `lsusb -d 046d:c336`, sysfs descriptors, udev metadata, device permissions and symlink inspection.
- `loginctl`, `systemctl show`, and bounded D-Bus introspection.
- `busctl --user introspect org.kde.keyboard /Layouts`.
- Public primary-source fetches pinned to the relevant revisions where available.

The final product state was:

```text
## main...origin/main [ahead 2]
HEAD:        6b4e4b30c29b154a99a96061c1b692781f82c400
origin/main: ca3ac07c5fecfe3c983078e343ec6b3e02c75bea
AP gitlink:  7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
```

No product build, physical key capture, grab, HID write, RGB SDK session, suspend, display-off, installation or service mutation was performed.

**Resolved Execution Issues / Near-Misses**

- **Stale and changing repository baseline:** the prompt preceded AGENTS/AP integration. Changes were inspected and preserved; ownership confirmation remains G0.
- **Native mode mismatch:** Default mode was reported honestly. Later explicit human authorization supported continued planning; native Plan mode was not claimed.
- **Incorrect session inference risk:** failure of the process-relative session query was resolved by enumerating the active graphical session.
- **Stale DPMS route:** the absent PowerDevil object was replaced in the proposal by the inspected native KScreen DPMS API.
- **Documentation/version mismatch:** KWin APIs were checked against matching source; packaged OpenRGB protocol 5 was distinguished from master documentation.
- **False input isolation risk:** overlapping event capabilities and keyboard reports on the RGB interface were identified before proposing permissions.
- **Unverified ownership evidence:** inaccessible process descriptors were left unknown; no privilege escalation or forced device claim followed.

**Pre-Existing Failure Classification**

No product failure or regression was established because no product implementation or tests exist. The zero-byte G213 input-remapper preset, unavailable OpenRGB installation, incomplete untracked META material, and original baseline mismatch are pre-existing state or evidence limitations. They were not modified.

**Smallest next step for the ORCHESTRATOR**

Resolve **G0** by confirming and freezing the observed product baseline and preserving continuation history. Then issue the bounded V1 profile-contract implementation prompt; route G1 physical-control discovery separately before authorizing an input backend.

Report justification: new-evidence

Authority expiry: planning authority expired at submission of this terminal report; implementation, mutation, acceptance, publication, META self-archival, and closure remain unauthorized.

Transition owner: ORCHESTRATOR

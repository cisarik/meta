# M3 — Workspace-aware five-zone lighting

## Summary and verified baseline

Implement one opt-in lighting slice: a global five-slot layout combines virtual-desktop indicators with application colors and sends the resolved result through the existing OpenRGB protocol-5 client. Existing configuration files retain their lighting behavior until the user explicitly configures workspace roles.

**Planning result:** decision-complete under the COOPERATOR’s amended, chat-only delivery instruction. No file persistence is required or claimed. The earlier `BLOCKED` report remains historical; this continuation completes the technical planning without changing files.

Verified baseline:

| Item | Verified value |
|---|---|
| Product branch | Clean `main` |
| Product start/end commit | `ca6052e816d4884ddeac9d7499a42c2aca089e7e` |
| Required parent | `ab10491c49d0b6574b6953a02935a4664c39d7c2` |
| AP gitlink and checkout | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| AP health | `./.ap/ap doctor` PASS |
| Local and public META baseline | `8e5fc13acb92ef65e763cff59994d2029c865d2b` |

Direct public `main` checks matched both repositories. Product and AP remained clean. META contained only the previously prepared, untracked M3 directory. The existing planning prompt matched the received attachment byte-for-byte.

The public M2 park handoff, Session 26/27 pairs, and named Session 16/19/22/23/24 reports were verified against META’s committed contents. Session 27 is owner-path deployment evidence.

> The named live G4 slices are accepted, but the M2 logical whole remains open. M2 is parked with G3 host-mitigated on the authorized reference host; the next bounded whole is M3 workspace-aware lighting.

Source findings that determine this implementation:

- Schema 2 stores `zones` as `null` or five color strings; `ZoneValue` currently holds only `Rgb`.
- Lighting resolution currently selects temporary override → application preset → global preset.
- ROADMAP records the KWin desktop-manager properties and signals needed by M3.
- OpenRGB already supports whole-device five-color Direct updates.
- **Returning `untouched` after takeover invokes the client’s existing restore-then-release behavior.** It does not necessarily mean zero transport traffic.
- **The client refuses all-black Direct output.** A deliberately all-black workspace composition must use device `Off`.
- The control-to-zone Results table is empty. It governs control accents, which remain inactive; it is unnecessary for five physical lighting slots.
- Existing CTest coverage includes persistence, pure resolution and protocol encoding, but no registered session-controller or workspace receiver tests.

## 1. Architecture and workspace state

### Types and ownership

Add these types in the existing core/header owners:

- `ZoneRole`: `Static`, `DesktopIndicator`, `AppColor`, `Off`.
- Extend `ZoneValue` with `role`, defaulting to `Static`; retain `color` and existing static-color helpers.
- `WorkspaceDesktop`: position, opaque ID and display name.
- `WorkspaceState`: availability, normalized desktop list, current ID and current ordinal. Unknown state contains no usable cached desktop identity.
- `LightingResolution`: resolved concrete `Lighting`, workspace-layout flag, five slot contributions, indicator capacity and overflow information.

Add a pure resolver entry point:

```cpp
LightingResolution resolveContextLighting(
    const ProfileDocument &document,
    const ApplicationIdentity &identity,
    const WorkspaceState &workspace,
    const std::optional<Lighting> &sessionOverride = std::nullopt);
```

Retain the existing `resolveLighting` overloads for compatibility. Delegate through the new resolver with unknown workspace state and return its concrete lighting result.

Add `WorkspaceReceiver` in `src/context/`, owned by `SessionApplication`. Its responsibilities are desktop-state observation, validation and reconnect handling. It never accesses the broker.

`AppController` receives the workspace receiver through a setter, caches the latest lighting resolution, and exposes its presentation to QML. Add optional configuration-root injection to its constructor for isolated controller tests; production keeps the existing default.

No new device lighting mode, broker interface, exported context D-Bus API, dependency or KWin-script feature is required.

### D-Bus observation

Use the session-bus service `org.kde.KWin`, object `/VirtualDesktopManager`, interface `org.kde.KWin.VirtualDesktopManager`.

1. Install service-owner and relevant signal subscriptions before requesting state.
2. Resolve the current unique service owner.
3. Asynchronously call `org.freedesktop.DBus.Properties.GetAll` for the desktop-manager interface.
4. Read `count`, `current` and `desktops`. Ignore unrelated properties such as `rows`.
5. Treat `currentChanged`, `countChanged`, `desktopCreated`, `desktopRemoved` and `desktopDataChanged` as invalidations requiring a new snapshot. Do not reconstruct authoritative state from partial signal payloads.
6. Coalesce invalidations within one event-loop turn. Allow one snapshot request in flight and one pending-refresh flag.
7. Bind replies to an owner generation and invalidation revision. Discard replies from replaced owners or requests superseded by newer signals.

ROADMAP records `desktops` as `a(iss)`. The decoder accepts signed or unsigned 32-bit positions, normalizes them after range checks, and rejects other tuple shapes. This is bounded compatibility handling, not a claim that both signatures were measured.

Provide a constructor accepting an injected `QDBusConnection` for tests. Production owns a named session-bus connection so connection recovery can recreate it without altering the application-context receiver’s connection.

### Validation and failure behavior

Accept a snapshot only when:

- Desktop count is 1–32 and equals the number of entries.
- IDs are non-empty, unique and at most 128 UTF-8 bytes.
- Names are at most 256 UTF-8 bytes; empty names display as `Plocha N`.
- IDs and names contain no control characters.
- Positions are unique integers from 0 through 32.
- Retained desktop metadata totals at most 16 KiB.
- `current` identifies exactly one entry.

Sort by position and derive the displayed ordinal from that ordering. Do not assume IDs are indices or require UUID syntax. Position gaps are acceptable; duplicate positions are not.

These are application validation/retention limits, not a claim that Qt prevents oversized messages from reaching its D-Bus decoder.

State transitions:

| Condition | Behavior |
|---|---|
| Initial discovery | Unknown until one complete valid snapshot |
| Ordinary invalidation | Refresh pending; retain the last presentation briefly and defer new workspace-dependent output |
| Refresh deadline | After 2 seconds without a current valid snapshot, become Unknown |
| Invalid snapshot, count mismatch or missing current ID | Unknown; never select an arbitrary remaining desktop |
| Service loss or owner replacement | Immediately invalidate state and outstanding replies |
| Successful recovery | Activate only a fresh validated snapshot |
| Duplicate snapshot | No semantic state-change notification |
| Name-only change | Refresh labels; unchanged colors cause no RGB submission |

A refresh deadline cannot be extended indefinitely by incoming invalidations. Following a failed refresh, use single-shot recovery delays of 1, 2, 4, 8, 16 and 30 seconds, then wait for a new service/signal event or explicit reconnect. A healthy connection has no periodic desktop polling.

Idle desktop state does not expire merely because no signal arrives. A silent compositor hang without any observable event cannot be detected by this event-driven design; do not claim otherwise.

### Recompute and deduplication

`AppController` schedules one queued recomputation for a burst of application, workspace or document changes. It uses the latest complete inputs when that callback runs.

- While workspace refresh is pending, defer automatic workspace composition until completion or the deadline.
- Explicit session overrides remain responsive during refresh.
- Compare effective inputs before resolving and compare resulting `DesiredLighting` before calling `setDesiredState`.
- Keep UI metadata updates separate from transport updates.
- Coalesce the existing bridge-loss signal pair, which currently calls the identity handler twice.
- Preserve the client’s existing 20 Hz transport coalescing and reconnect behavior.

This provides bounded, event-driven convergence. It does not promise an atomic desktop-and-focus observation across two independent context sources.

## 2. Exact schema-3 contract and migration

### Document contract

Set `kSchemaVersion` to `3`.

The document hierarchy and all existing non-lighting semantics remain unchanged:

| Object | Allowed fields |
|---|---|
| Root | `schema_version`, `device`, `global`, `applications`, `preferences` |
| Device | `vendor_id`, `product_id`, `model`, with the existing exact G213 values |
| Global | `keys`, `lighting` |
| Application | `id`, `display_name`, `match`, `keys`, optional `lighting` |
| Match | `desktop_file_name`, `resource_class`, `resource_name` |
| Preferences | `automatic_enabled`, `tray_notifications` |
| Lighting | `mode`, `base_color`, `zones`, `restore_mode`, `speed` |

Preserve current required fields, matcher ranking, application order, assignment validation and preference defaults. Unknown semantic fields are rejected at every configuration-object level.

Lighting fields:

- `mode`: required; `untouched`, `direct`, `wave`, `cycle`, `breathing`, `off`.
- `base_color`: optional or `null`; otherwise exactly six hexadecimal RGB digits following `#`.
- `zones`: absent/`null`, or exactly five **objects**.
- `restore_mode`: optional; defaults to `wave`; accepts existing device modes, excluding `untouched`.
- `speed`: optional integer from 0 through `2147483647`, preserving the existing parser’s signed-integer domain. Validate range before conversion.
- Direct requires `base_color` or five zones.
- Maximum document size remains 1 MiB.
- Serialization emits lowercase colors and schema 3.

Zone objects:

| Role | Exact allowed fields | Meaning |
|---|---|---|
| `static` | Required `role`, `color` | Fixed slot color |
| `desktop_indicator` | Required `role`, `color` | Indicator’s full-brightness color |
| `app_color` | Required `role`, `color` | Application contribution; stored color is its fallback |
| `off` | Required `role` only | Black slot |

No speculative or reserved roles.

Global lighting accepts all four roles. Application lighting accepts only `static` and `off`; applications cannot replace the global workspace layout.

A workspace layout is active precisely when global mode is `direct` and its five slots contain at least one `desktop_indicator` or `app_color`. No additional enable flag or lighting-mode enum is introduced.

Roles stored under another global mode remain dormant. Switching that mode back to Direct explicitly reactivates them.

### Representative configuration

```json
{
  "schema_version": 3,
  "device": {
    "vendor_id": "046d",
    "product_id": "c336",
    "model": "logitech-g213-prodigy"
  },
  "global": {
    "keys": {},
    "lighting": {
      "mode": "direct",
      "restore_mode": "wave",
      "base_color": "#7c3aed",
      "zones": [
        {"role": "desktop_indicator", "color": "#7c3aed"},
        {"role": "desktop_indicator", "color": "#7c3aed"},
        {"role": "desktop_indicator", "color": "#7c3aed"},
        {"role": "desktop_indicator", "color": "#7c3aed"},
        {"role": "app_color", "color": "#404040"}
      ]
    }
  },
  "applications": [
    {
      "id": "editor",
      "display_name": "Editor",
      "match": {"desktop_file_name": "org.kde.kate"},
      "keys": {},
      "lighting": {
        "mode": "direct",
        "restore_mode": "wave",
        "base_color": "#ff8000",
        "zones": null
      }
    },
    {
      "id": "browser",
      "display_name": "Browser",
      "match": {"resource_class": "firefox"},
      "keys": {},
      "lighting": {
        "mode": "direct",
        "restore_mode": "wave",
        "base_color": "#00aaff",
        "zones": null
      }
    }
  ],
  "preferences": {
    "automatic_enabled": true,
    "tray_notifications": false
  }
}
```

### Migration

Parse schemas 1, 2 and 3 through version-specific lighting readers. Validate older versions using their original field rules before mapping them into schema-3 types.

| Schema-2 form | In-memory schema-3 mapping |
|---|---|
| `untouched` | Same mode and optional values; no workspace roles |
| Direct with base color | Same base color; zones remain absent |
| Direct with five strings | Five `static` objects with identical colors |
| Direct with both forms | Preserve both; zone colors continue to win |
| Wave/Cycle/Breathing/Off | Preserve mode, base color, speed and restore mode |
| Zones stored under a device mode | Convert to static objects but keep them inactive |
| Missing application lighting | Remains absent |
| Explicit application lighting | Apply the same preserving mapping |
| Keys, matchers and preferences | Preserve values and ordering |

Schema 1 retains its existing mode mappings and migration-failure fallback, with successful results now represented as schema 3.

Reading never creates a file or backup, rewrites bytes, enables workspace roles, or changes previously valid user-visible lighting. Malformed schema-2/3 documents are refused and cold-start activation remains pass-through plus untouched. Future versions greater than 3 remain refused.

### Save and recovery

Keep explicit save as the only persistence boundary.

- Validate the complete in-memory draft and its serialized representation.
- Preserve exact existing bytes in the single `.bak` sibling before replacement.
- Use `QSaveFile` with direct-write fallback disabled for both backup replacement and the primary document.
- Refuse replacement when the existing document is unsupported, invalid, or only loads through a migration-error fallback. Report the preservation error instead of silently replacing it with defaults.
- A backup failure cancels the primary replacement. A primary commit failure preserves the original document; its backup may already contain those same original bytes.
- Do not claim the two files form one atomic transaction.

This corrects the current remove-then-copy backup weakness within the persistence file already being changed.

Before the first explicit schema-3 save, rollback requires only the previous application binary. After saving, an older binary refuses schema 3: restore the preserved schema-2 bytes separately. The rolling `.bak` is overwritten by later saves, so a COOPERATOR-owned pre-upgrade copy is required if downgrade capability must survive multiple saves.

## 3. Deterministic composition and UI

### Resolution precedence

1. **Session override:** temporary color, lights off or device-default selection takes precedence over every document/context rule.
2. **Active global workspace layout:** owns all five slots. Application presets contribute only to `app_color` slots.
3. **Ordinary lighting:** when no workspace layout is active, retain application preset → global preset resolution.

Temporary color retains its existing lifetime: an external identified application change expires it; opening ContextDeck or changing only the virtual desktop does not. Lights Off and Device Default remain selected until an existing explicit user action changes them.

### Slot rules

Visit physical slots in the existing left-to-right order.

**Desktop indicators**

Number only `desktop_indicator` slots from 1 to K in physical order. Indicator N represents desktop ordinal N.

- Current represented desktop: configured RGB unchanged.
- Existing inactive desktop: each channel becomes `floor(channel / 5)`, giving fixed 20% brightness.
- No desktop at that ordinal: black.
- More desktops than K: show the first K only.
- Current ordinal greater than K: all represented desktops are inactive; report that the current desktop is not represented.

No cycling, paging, modulo wrapping, invented desktop or hidden overflow encoding. K=0 means no desktop indicators are configured.

**Application slots**

Use the existing application matcher. For an `app_color` slot at physical index I:

| Matched application preset | Contribution |
|---|---|
| Direct with zones | Its static/off color at index I |
| Direct with base only | Base color |
| Breathing | Base color, or existing `#7c3aed` default |
| Off | Black |
| Untouched, Wave or Cycle | Global slot’s configured fallback color |
| No match, no override or unavailable identity | Global slot’s configured fallback color |

Wave and Cycle are not sampled or converted into a fabricated static color. Breathing contributes its configured color without animating the slot.

`static` uses its stored color. `off` uses black. Neither is overwritten by the application.

**Unavailable workspace**

For an active workspace layout, Unknown workspace state resolves to **untouched / release to recorded device default**.

- Before takeover, this causes no lighting write.
- After takeover, the unchanged RGB client requests its recorded restore mode and releases control.
- If transport is unavailable, restoration is not claimed as completed.
- The UI identifies workspace unavailability and the desired fallback; it does not display the last desktop as current.

Bridge loss alone does not invalidate a valid workspace snapshot. Desktop indicators keep working, while app slots use their global fallback colors.

**Concrete output**

Composition produces exactly five RGB values. Convert them into a concrete static Direct preset before calling the existing protocol path. Unresolved dynamic roles must never reach context-free color conversion.

If all five computed colors are black, use device `Off` while retaining five black values in the preview. This exception is necessary because the existing RGB client refuses all-black Direct frames. It applies to the new workspace composition; it does not silently reinterpret migrated legacy presets.

### Small UI slice

Use the existing Farby editor, Overview Hero and Diagnostics page.

Controller additions:

- `workspaceLayoutActive`
- `globalZoneSlots`
- `workspaceSummary`
- `workspaceObservationPaused`
- `setGlobalZoneRole(index, role)`
- `useDefaultWorkspaceLayout()`
- `useStaticZoneLayout()`
- `setWorkspaceObservationPaused(bool)`

Extend the existing diagnostics map with workspace state, desktop count/current ordinal, refresh state, error class and counters. Do not log desktop IDs or names.

Farby:

- Add **„Použiť rozloženie 4 plochy + aplikácia“**. This explicit action selects Direct and four desktop indicators plus one app slot.
- Add a role selector to each of the five global zone rows.
- Reuse the color picker, labelled according to the role: fixed color, indicator color or application fallback.
- Display which desktop ordinal each indicator represents.
- Add **„Použiť pevné zóny“** to convert roles into static configured colors.
- Global slot-color edits preserve the selected role.
- Applying a gradient explicitly replaces the layout with static slots; label that consequence while workspace roles are active.
- Preserve live application of explicit edits and separate **Uložiť** persistence.

Application editor:

- Retain existing preset controls.
- Explain that, while workspace layout is active, the preset supplies only application slots.
- When creating an application override from global lighting, copy concrete fallback/static colors; never copy dynamic roles into the application profile.
- Ensure an application Direct preset created from untouched global lighting receives a valid color.

Overview:

- Reuse the five-strip Hero without changing `ZoneHero.qml`.
- Show current desktop, application contribution and overflow/unavailable status.
- Label colors as a desired preview, without physical-readback claims.
- Render desktop names as plain text.

Diagnostics:

- Add a non-persistent **„Pozastaviť sledovanie plôch“** control.
- Pausing invalidates the workspace receiver through its normal unavailable-state path. Resuming establishes a fresh subscription and snapshot.
- This supports bounded fallback diagnosis without stopping KWin or the session bus. It is explicitly a simulated observation interruption, not proof of real compositor failure.

## 4. Tests, implementation sequence and acceptance

### Focused validation

Add two registered targets: `test_workspace_receiver` and `test_workspace_lighting`. Keep existing test names.

| Test owner | Required cases | New causal regression? |
|---|---|---|
| `test_profile_persistence` | All migration forms above; exact bytes before save; schema-3 round trip; exact previous-byte backup; failed backup/write; invalid existing-file preservation | Yes: durable migration and backup behavior change |
| `test_profile_persistence` | Wrong slot counts/types; role-specific fields; dynamic application roles; color and numeric bounds; unknown fields; future schema 4 | Yes: new format and validation boundaries |
| `test_profile_resolver` | Legacy precedence and unchanged migrated desired states; override precedence; unresolved roles cannot become static output | Yes for the new boundaries; retain existing assignment tests |
| `test_workspace_lighting` | Indicator ordering and brightness; absent desktops; overflow; mixed roles; application preset table; unknown workspace; bridge loss; all-black Off conversion | Yes: composition does not exist in the candidate |
| `test_workspace_receiver` | Initial snapshot; subscription-before-snapshot race; superseded reply; owner replacement; service loss; malformed/count-mismatched state; missing current ID; removal; timeout; reconnect budget | Yes: asynchronous workspace state does not exist |
| `test_workspace_receiver` | Duplicate snapshots, metadata-only updates and bounded invalidation bursts | Yes: guards against stale state and repeated work |
| `test_workspace_lighting` | Controller coalescing, simultaneous desktop/app change, bridge-loss signal pair, unchanged-output suppression, overrides during refresh | Yes: new integration can duplicate or misorder output |
| `test_workspace_lighting` | Resolve synthetic context, encode with existing protocol-5 functions, decode and compare all five exact colors and packet order | Yes: connects new composition to the established wire format |
| `test_openrgb_protocol` | Existing five-color, mode, untouched and animation cases | No new file edits: transport implementation is unchanged |

Update existing persistence expectations that hardcode schema 2 and the future-schema fixture that currently uses version 3.

Receiver tests run against a fake desktop-manager service on a **private bus**, using `dbus-run-session`; they must not query or replace real KWin. Validate both accepted position encodings. If the private-bus runner is unavailable, report the prerequisite instead of silently skipping these tests or installing anything.

Controller tests use an injected temporary configuration root, a non-started RGB client and no broker client. Never start `SessionApplication`, broker IPC, power actions or hardware during these tests. Put controller integration cases in `test_workspace_lighting.cpp`, compiling the necessary existing controller sources into that target.

UI binding and rendering checks remain a focused review/fresh acceptance task; do not add tests that merely mirror QML labels.

Later implementation commands:

```sh
cmake -S . -B build -G Ninja
cmake --build build

ctest --test-dir build --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_lighting|test_openrgb_protocol)$'

ctest --test-dir build --output-on-failure

git diff --check
git diff --name-only
git status --short
```

CMake must wrap the two new integration-capable targets in the private-bus runner and set offscreen Qt operation where necessary.

The full registered CTest suite is required because shared schema/core changes can regress existing M1 and M2 behavior. It is not live M2 acceptance. No tests or builds were executed during this planning exchange.

### Ordered implementation slice

1. Add schema-3 roles, strict parsing, preserving migration and backup handling with focused persistence tests.
2. Implement the pure five-slot resolver and exact protocol-output tests.
3. Implement the bounded workspace receiver and private-bus race/recovery tests.
4. Wire session ownership, controller recomputation, deduplication and configuration-root injection.
5. Extend the existing UI controls and presentation.
6. Update specification, architecture, M3 testing instructions and the README/ROADMAP status.
7. Run focused tests, then the registered full suite; review the exact diff and allowlist.
8. Produce one coherent implementation candidate and one commit only under the later explicit Git grant.

### Exact later implementation changed-path allowlist

```text
CMakeLists.txt
src/core/Types.h
src/core/Persistence.cpp
src/core/Resolver.h
src/core/Resolver.cpp
src/context/WorkspaceReceiver.h
src/context/WorkspaceReceiver.cpp
src/app/SessionApplication.h
src/app/SessionApplication.cpp
src/app/AppController.h
src/app/AppController.cpp
ui/OverviewPage.qml
ui/ColorsPage.qml
ui/LightingPresetEditor.qml
ui/DiagnosticsPage.qml
tests/unit/test_profile_persistence.cpp
tests/unit/test_profile_resolver.cpp
tests/unit/test_workspace_receiver.cpp
tests/unit/test_workspace_lighting.cpp
docs/specification.md
docs/architecture.md
docs/testing-m3.md
README.md
ROADMAP.md
```

The new receiver and two test files implement the missing behavior and its causal evidence. `docs/testing-m3.md` owns the separate M3 acceptance procedure.

README and ROADMAP may reconcile the M2 park synopsis against the verified handoff. They must retain the named accepted slices and residual gaps. Do not expand this into an M2 documentation rewrite.

No changes to RGB transport, the control catalog, broker, broker IPC, KWin bridge, packaging, AP, licensing, dependencies, generated files or other tests/UI.

Publication is a separate boundary: a later prompt must explicitly authorize any push. Publish at most the single reviewed implementation commit through normal fast-forward publication, with public-ref verification. No deployment, installation or autostart accompanies it.

### Later fresh acceptance and COOPERATOR IRL checklist

A separate fresh Worker first reviews the exact implementation commit and independently verifies the automated evidence. Physical acceptance then needs a bounded COOPERATOR grant using the already established M1 lighting setup.

1. **Prepare safely.** Use at least two existing desktops and two identifiable application contexts. Keep the broker inactive. Preserve the current configuration before saving schema 3. No desktop creation, input probing or host-policy change is needed.
2. **Check compatibility.** Start with a valid schema-2 preset and confirm unchanged behavior before enabling roles. Confirm that merely loading it does not rewrite its file.
3. **Exercise the default layout.** Apply four desktop indicators plus one app slot. Switch between the two desktops and two apps. Check active/inactive indicators, application color and the five-zone preview against the physical keyboard.
4. **Exercise all five physical zones.** Temporarily configure two desktop indicators and three app slots. Switch desktop and application contexts so both indicator zones and all three app zones visibly change. Record observation of each physical zone; do not infer any control-to-zone map.
5. **Check capacity.** Temporarily reduce indicator capacity to one and select the second existing desktop. Confirm the explicit unrepresented-desktop warning and absence of a false active indicator.
6. **Check loss and recovery.** Under the acceptance grant, disable the already installed context bridge and wait for its existing loss timeout: app slots must use fallback while desktop indicators remain responsive. Re-enable it. Then pause workspace observation in Diagnostics: expect the recorded device-default request and unavailable label; resume and require a fresh snapshot. Real D-Bus owner-loss correctness comes from private-bus tests; this physical pause is labelled simulated loss.
7. **Restore.** Select **Restore device default**, observe the actual keyboard and confirm later context changes do not retake control. Restore the chosen configuration. Do not claim successful physical restoration when transport was unavailable.

No raw input, grab, broker start, udev/ACL operation, suspend, autostart or OpenRGB CLI-per-change route is part of this checklist.

## 5. Evidence envelope, limits and handoff

| Result | What it can establish |
|---|---|
| Implementation-PASS | Candidate satisfies the selected schema, resolver, receiver, controller and automated output tests; evidence is non-independent |
| Fresh code acceptance | Independent review/reproduction of the exact candidate’s bounded software behavior and scope |
| COOPERATOR IRL acceptance | Visible behavior of all five physical zones, actual desktop/app response and observed device-default restoration on the named setup |
| Publication verification | Exact reviewed commit is publicly reachable; no deployment or hardware claim |

Defaults fixed by this plan:

- Four desktop indicators plus one application slot.
- Fixed first-K desktop representation; explicit overflow.
- Active brightness 100%, inactive brightness 20%.
- No persistent desktop IDs, desktop creation or desktop-specific profile database.
- Unknown workspace releases to the recorded device-default path.
- All-black workspace output uses Off.
- Existing animated application presets remain available outside workspace composition.

Remaining evidence is implementation, fresh code acceptance and physical observation. No unresolved product choice requires another planning cycle.

Explicit non-claims: no implementation-PASS, acceptance-PASS, publication-PASS, deployment-PASS or physical acceptance from this planning exchange; no production readiness, M2/G4 closure, independent G3 re-audit, general input-remapper coexistence, autostart, hibernate/hybrid sleep, M4 session management, remapping, deck behavior, M5 integration or per-key RGB. Session 27 was not a fresh Worker run, and the unfilled control-to-zone map remains unmeasured.

M4, remapping, deck interaction and M5 remain separate future wholes. None receives execution authority from this plan.

No product, AP, META, host, service, device, dependency or Git publication mutation was performed. No subagents were used. Chat-only delivery replaces the original file-persistence requirement under the COOPERATOR’s explicit amendment.

**Smallest next step:** ORCHESTRATOR reconciliation of this plan and, only if accepted, a separate complete implementation prompt for a fresh Worker with `Native planning mode: not-used`.

Report justification: new-evidence

Resolved Execution Issues / Near-Misses: The original persistence blocker was resolved by the COOPERATOR’s explicit chat-only delivery amendment; no write restriction was bypassed.

Pre-Existing Failure Classification: No runtime failure was tested. The inspected restore behavior, all-black Direct guard and backup implementation are explicitly accounted for above.

Orchestration critique:

MEASURED: The prompt’s delivery requirement conflicted with Native Plan Mode; the COOPERATOR removed the persistence requirement, allowing the same technical planning objective to complete without writes.

LEAD: none

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.

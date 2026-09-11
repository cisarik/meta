### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-mvp-context-lighting
Worker session ordinal: 02
Worker exchange ordinal: 01

**status:** PASS  
**Phase-qualified result:** implementation-PASS  
**Result artifact or commit:** `4416f4be7b7476bd93ef1daab6c08af9a8a4d065` .. `042fa150cab72b4cfed24d68e6e6a940d695e525` (five local commits on `main`)  
**Result evidence:** `cmake -S . -B build -G Ninja` (clean `PATH` because `CMAKE_ROOT` is poisoned in the ambient environment); `cmake --build build`; `ctest --test-dir build --output-on-failure` — 3/3 passed after every stage and again at HEAD. Offscreen start (`QT_QPA_PLATFORM=offscreen`, empty config root): bus name registered, cold-start log `writing nothing`, tray started, OpenRGB `Connection refused` (no device traffic), clean SIGTERM.  
**Logical-whole closure:** not-closed

**Capability handshake (abbreviated):** Cursor coding client in Agent mode; native planning mode not enabled / not used; writable scope was the prompt allowlist; commit capability was used only under the per-stage git grant and is not further authority.

**Start commit:** `40aa09d8682dcf50cea2b2e6c6397f69544ab29e`  
**End commit:** `042fa150cab72b4cfed24d68e6e6a940d695e525`

### Changed files and purpose, by stage

| Stage | Commit | Purpose |
|-------|--------|---------|
| S1 | `4416f4be7b7476bd93ef1daab6c08af9a8a4d065` | Schema 2 lighting presets (`untouched`/`direct`/`wave`/`cycle`/`breathing`/`off`), in-memory v1→v2 migration without rewrite, resolver precedence including temporary override, tests 1–2, specification lighting/schema sections. AppController compiles against the new types and skips device writes for `untouched`. |
| S2 | `a5e94af70f3c67bdab5a58758b3c6767c51c5ff5` | Protocol-5 `UPDATEMODE` encode/decode from the public SDK layout; desired-state frames; connect enumerates without `SETCUSTOMMODE`; restore-mode bookkeeping; test 3 extended. |
| S3 | `0ca8c8ca7177aaaa63c2f57445e546060847e38f` | Five named zone swatches, gradient helper, preset picker (global and per-app), truthful labels, tray **Restore device default**. |
| S4 | `18d76ee04a387154cae26d3b7fc746e825cf00be` | Unverified control-to-zone table with inert `applyZoneAccent`; D1 verification tests; long-lived `KScreen::Dpms`; heartbeat `ContextReport` + identical-identity refresh without policy bump. |
| S5 | `042fa150cab72b4cfed24d68e6e6a940d695e525` | Specification reconciled; operations warn against OpenRGB GUI/CLI “fixes”; testing script rewritten; `docs/hardware/g213-zone-map.md` created. |

### Defect closeout

**D1 — destructive lighting on connect.** `OpenRgbClient` no longer sends `SETCUSTOMMODE` after enumeration. Desired state `untouched` encodes to zero frames; Direct with all-zero colors is refused. Verified without hardware by `untouchedDesiredStateProducesNoFrame` and `desiredStateNeverSelectsCustomMode`, plus the connect path logging `G213 enumerated; no mode selected without lighting intent`. Optical confirmation remains IRL.

**D2 — stack `KScreen::Dpms`.** `PowerActions` now owns a `KScreen::Dpms` member and calls `switchMode` on that object. Support check and 2 s debounce unchanged. Verified without executing DPMS-off: the member is constructed at process start (offscreen run logs the platform warning from that object). IRL step 10 still required.

**D3 — empty context after restart.** The KWin script sends a full `ContextReport` on every heartbeat as well as on events. The receiver applies a repeated identical identity as a refresh: no `PolicyRevision` bump, no `currentIdentityChanged`, therefore no lighting rewrite. Verified by code inspection and unit-adjacent logging; the Worker must not load the script, so live restart recovery is IRL step 9.

### Tests and validation

Still exactly three CTest binaries, all green:

1. `test_profile_resolver` — added app-over-global lighting, untouched default, unidentified→global, temporary override, unverified zone-accent inert (20-entry map, all `verified: false`).
2. `test_profile_persistence` — v1→v2 in-memory migration with byte-identical file; failed v1 lighting migration → pass-through + untouched; schema 2 rejects unknown mode / wrong zone count / unknown fields; schema 2 round-trip.
3. `test_openrgb_protocol` — `UPDATEMODE` for Wave and Direct, mode-name handling, untouched → no frame, Direct → UpdateMode then UpdateLEDs, never SetCustomMode.

Deliberately not tested: GUI/QML, live OpenRGB, hardware, KWin load, DPMS-off, suspend.

### Commit and push result

Local SHAs above. Push not authorized. Working tree clean.

### Stage table

| Stage | Gate | Reason |
|-------|------|--------|
| S1 | green | configure + build + ctest, committed |
| S2 | green | ctest, committed |
| S3 | green | build + offscreen start, committed |
| S4 | green | build + ctest + offscreen start (context-recovery path in tree), committed |
| S5 | green | documentation committed |

### COOPERATOR hand-off

Rebuild (unprivileged; use a clean `PATH` if `CMAKE_ROOT` is poisoned):

```sh
env -i HOME="$HOME" PATH=/usr/bin:/bin:/usr/sbin cmake -S . -B build -G Ninja
env -i HOME="$HOME" PATH=/usr/bin:/bin:/usr/sbin cmake --build build
env -i HOME="$HOME" PATH=/usr/bin:/bin:/usr/sbin ctest --test-dir build --output-on-failure
```

Restart the stack (COOPERATOR-run; do **not** run `openrgb --list-devices`):

1. OpenRGB SDK: `openrgb --server --server-host 127.0.0.1 --server-port 6742`
2. Unload and reload `contextdeck-bridge` so heartbeat `ContextReport` is live (`docs/operations.md` §3).
3. Move aside any existing `profiles.json` for the cold-start step.
4. `./build/contextdeck`

Run `docs/testing.md` in order. Stop on the first failure.

**Five-step zone-map probe** (testing step 12, owner `docs/hardware/g213-zone-map.md`): Direct mode, dim `#202020` on unused zones; isolate Left / Middle / Right / Arrow and Homekeys / Numpad one at a time with `#ff0000` / `#00ff00` / `#0000ff` / `#ffff00` / `#ff00ff`; write observed catalog controls into the empty Results table; then Restore device default.

**Log lines to send back on failure:** `contextdeck.context`, `contextdeck.rgb`, `contextdeck.app`, `contextdeck.ui`, `contextdeck.actions`; OpenRGB server stderr with serials removed; `journalctl --user -n 80` grepped for kwin/contextdeck; step number and what the keyboard actually showed. No captions, keystrokes, or USB serials.

### Facts versus assumptions versus unknowns

**Facts:** schema 2 is the only activatable version; v1 files migrate in memory; `untouched` emits no SDK frames; connect does not select Direct; DPMS helper is process-lifetime; heartbeat resends identity; zone map ships unverified and inert; 3/3 CTest green; offscreen cold start wrote no config and no device frames.

**Assumptions:** v1 `automatic` migrates to `untouched` (keeps `base_color`) so old defaults are non-destructive; if OpenRGB reports active mode Direct at first enum, restore records `wave`; zone-map hypotheses in `ZoneMap.cpp` / the hardware doc are guesses.

**Unknowns / open gates:** G1 (physical controls), G2 (optical five-zone IRL), G7 (Displays Off / Suspend IRL), zone-map Results table empty, no-readback honesty (only COOPERATOR eyes). Licensing still unresolved. Input interception still absent.

### Deviations, risks, missing evidence

- Tray/Overview action for following profiles is labelled **Follow profile**, not Automatic; status text uses `untouched — device default` or `temporary override — …`.
- Long-lived `KScreen::Dpms` logs a harmless platform warning on the offscreen QPA; on Plasma/Wayland it should be quiet.
- Zone roles / desktop awareness were not implemented (classified future whole).
- No live OpenRGB or KWin mutation in this exchange, as forbidden.

### Resolved Execution Issues / Near-Misses

- Ambient `CMAKE_ROOT` missing → configure with `env -i HOME PATH=/usr/bin:/bin:/usr/sbin` as already documented. Residual: ambient shell still poisoned.
- `toDesiredLighting` dropped while adding the gradient helper → compile caught it, function restored.
- Duplicate `Q_PROPERTY` lines after the S3 header edit → moc warning, duplicates removed.

### Pre-Existing Failure Classification

none

### Smallest next step for the ORCHESTRATOR

Archive this prompt/report pair in META, then have the COOPERATOR run `docs/operations.md` + `docs/testing.md` (including the five-step zone-map probe) and return optical results. Do not start M2 and do not treat this as acceptance.

**Report justification:** new-mutation  
**Authority expiry:** implementation authority expired at this terminal report; further mutation, host enablement, acceptance, publication, META self-archival, and closure remain unauthorized

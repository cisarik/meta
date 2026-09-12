### Report for ORCHESTRATOR_CHAT

- **logical-whole identity:** `g213-contextdeck-input-passthrough-safety`
- **Worker-session ordinal:** `12`
- **Worker-exchange ordinal:** `01`
- **Worker session target:** `fresh-worker-session`
- **Native planning mode:** `not-used`
- **Worker session profile:** Fresh Implementation Worker
- **status:** **PASS**
- **phase-qualified result:** **implementation-PASS** (AP pin adoption + root-document reconciliation only; runtime unchanged)
- **Report justification:** `new-mutation`
- **Logical-whole closure:** not-closed
- **Independence required:** no
- **G4 / production acceptance / recovery:** not claimed
- **Authority:** expires at this terminal report

```text
Implementation authority: explicit
Exact baseline: 24305864f54d7161048041c2e5309aa8a0f8fb1a
Changed-path allowlist: .ap gitlink, AGENTS.md, README.md, ROADMAP.md
Independence required: no
G4 acceptance: not claimed
Logical-whole closure: not-closed
```

## Commits and AP pin

| Anchor | Value |
|--------|--------|
| Start HEAD | `24305864f54d7161048041c2e5309aa8a0f8fb1a` |
| End HEAD | `64dd12bbc34c5ab09574d8edc76ebb7bed50af2d` |
| Subject | `docs: adopt AP 0cf2cff and reconcile M1/M2 root state` |
| Old AP gitlink / checkout | `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26` |
| New AP gitlink / checkout | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` |
| Canonical AP `origin/main` at check | `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9` (equals authorized target) |
| Product push | `origin/main` fast-forward `2430586..64dd12b` |

## Changed paths and purpose

| Path | Purpose |
|------|---------|
| `.ap` (gitlink only) | Adopt reviewed AP revision `0cf2cff` (ADR-0023 practical workflow consolidation). No AP source edits. |
| `AGENTS.md` | ChatOrchestrator + preserved manual delivery; M1 historically accepted IRL; M2 production path in repo; G4 uncompleted; CTest owner is `CMakeLists.txt`; report-file preparation vs META Git; local machine paths removed. Managed block unchanged. |
| `README.md` | Replace “no code / nothing installable” with current M1/M2/G4 status. |
| `ROADMAP.md` | Drop stale “S3/S4 remaining”, “nothing installed”, “awaiting IRL”, hard-coded AP SHA / `origin` lag, and event-node numbers. Record next M2 work as recovery-design + source safety gaps, not live grab. |

Unchanged: broker/app source, tests, CMake, `docs/`, `LICENSE`, `handout.md`, META Git.

## Validation

```text
./.ap/ap update --check
  current 7ef45da756ed3cc14808e89bf25d0a9f9aba5d26
  available 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9
  update available: yes

./.ap/ap update --apply
  moved .ap to 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9

./.ap/ap doctor --candidate   → PASS (gitlink still 7ef45da; candidate 0cf2cff)
git add .ap
./.ap/ap doctor               → PASS
  OK strict pinned AP commit
  OK managed AGENTS.md block
  OK resolved governing variant: stable

git diff --check              → clean
allowlist review              → only .ap, AGENTS.md, README.md, ROADMAP.md
copied AP files               → none at repository root
CTest / ContextDeck / G4      → not run (selected ladder)
```

AP diff (old→new): documentation/guidance only (`AP.md` and projections, ADR-0023). Executable `ap`, managed consumer block, and schema unchanged. Consumer pin is now exactly `0cf2cff`.

## Historical versus current host evidence

Read-only metadata this session. No grab, no ARM, no unit start, no udev reload, no config dump.

| Item | Historical (Worker 10/11) | Current (this session) |
|------|---------------------------|-------------------------|
| Kernel / systemd | Planner/W01: kernel string in ROADMAP was stale LTS | kernel `7.2.3-1-cachyos`; systemd `261.2` (`261.2-1-arch`) |
| Broker unit | static, inactive; W08 unit lagged `0750` then later matched | `static`, `inactive`/`dead`; no drop-ins; fragment `/etc/systemd/system/contextdeck-broker.service` byte-identical to repo; `RuntimeDirectoryMode=0755`; `WatchdogUSec=infinity` (never started) |
| `/usr/bin/contextdeck-broker` | W08 missing; W09/10 present and `cmp` equal to then-build | exists, executable; `cmp` equal to current `build/contextdeck-broker`; **not executed** |
| udev 61/62/99, sysusers | W11: repo had `99-`; host `62` still pre-fix | all four installed files `diff` equal to repo (`99-` present) |
| `/dev/uinput` | W10: session ACL, **no** `contextdeck-broker` named ACL | session named-user ACL **and** `user:contextdeck-broker:rw-` |
| G213 event if00/if01 | W10: `root`:`contextdeck-broker` `0660`, no session ACL | same class of result (identity via USB `046d:c336` + interface; no node numbers) |
| G213 hidraw if00/if01 | session ACL present | session ACL present; session r/w |
| input-remapper | enabled + active | enabled + active / running; configuration not read or changed |
| Session groups | not in `input` | not in `input` or `contextdeck-broker` |

Unavailable / not verified: live `WatchdogSec` after a real start; broker `access(2)` on uinput as `contextdeck-broker` (would be a `test`/`sudo` side-effect); OpenRGB lighting function; SSH/second-keyboard recovery path (still not demonstrated).

A systemd finite test lifetime or pre-armed external cutoff is a **candidate** for a later task, not an implemented recovery path.

## Verified source gaps (not repaired)

Classified only. Not independent security certification.

1. **`RealSink::writeEvent` discards the `libevdev_uinput_write_event` return.** Code fact: `RealSink.cpp` casts the result to `void`. Possible consequence: a failed inject is silent; ledger and compositor can diverge. Hardware behavior under grab: **unverified**.
2. **Production capabilities are `passthroughCapabilities()`, not measured source bits.** Code fact: `main.cpp` constructs `RealLifecycleSink(passthroughCapabilities())`; `unionSourceCapabilities()` is unused. Accepted plan (session 01): compositor `EV_LED` on the virtual node, forwarded to physical if00 only. Code fact: sources open `O_RDONLY`; `ForwardingEngine` copies `EV_LED` **from source to sink** (physical → virtual), with no write-back to if00. LED return path promised by the plan is **not implemented**. CapsLock/NumLock under grab: **hardware-unverified**.
3. **`LogindSeatAuthorizer` uses `sd_pid_get_session` on the peer PID.** Code fact: `SessionIpc.cpp` fail-closes if that lookup fails, then requires matching UID, non-empty seat, `wayland`/`x11`, active, non-remote. Foundation report: user-manager-launched processes may not belong directly to a graphical session. Possible consequence: a systemd `--user` session app could be rejected; a seated desktop-launched app may pass. Do not weaken authentication. Which launch path the tray actually uses: **not verified here**.

## Report persistence / readback

Destination verified: regular empty file (not a symlink) at the granted META path `12_report_00.md` beside `12_implementation_00.md`. Nonempty collision: none. This file is the complete public-safe report. META add/commit/push: **not performed** (COOPERATOR-owned).

## Smallest next step (ChatOrchestrator)

Issue one bounded **recovery-design** (and/or source-gap triage) prompt for one-keyboard development. Do **not** grant live grab, ARM, or G4. After this report exists, the COOPERATOR archives the exact prompt/report pair in META.

Orchestration critique:
MEASURED: Baseline root docs contradicted the tree (README “no code”; AGENTS “M1 awaiting IRL” and “S3/S4 remaining”; ROADMAP “nothing installed” / AP pin `7ef45da`). Evidence: files at `2430586`. Effect: operators would plan as if the broker were unbuilt or unaccepted. Smallest correction: this reconciliation (done).
LEAD: Whether a systemd `--user` launch of the session app fails `sd_pid_get_session`; cheapest check is a later authorized read of how `contextdeck` is actually started, without ARM.

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: G4 IRL uncompleted (Workers 09/10 BLOCKED on independent recovery path; areas A–G never executed). Source gaps above predate this session.

**Logical-whole closure: not-closed.** This task authority expires here.

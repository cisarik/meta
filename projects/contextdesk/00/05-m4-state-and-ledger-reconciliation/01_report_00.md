### Report for ORCHESTRATOR_CHAT

Logical whole identity: m4-state-and-ledger-reconciliation
Worker session ordinal: 01
Worker exchange ordinal: 01
Persistent role identity: WORKER

```text
Worker session target: fresh-worker-session
Worker session profile: Planner
Phase: planning
Task identity: CONTEXTDECK-M4-STATE-LEDGER-RECONCILIATION-PLAN
Native planning mode: required (observed active during planning; see persistence deviation)
status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: complete decision-ready, source-grounded reconciliation plan persisted at the exact META path and read back completely; the first rendering was chat-only because the native Plan Mode read-only control blocked writes, and the file was written unchanged in content after the COOPERATOR switched the session to build mode at the end of exchange 01
Report justification: new-evidence
```

- Start commit: `293158887e4228a42b9c64bda7d4f0bd32fb4ec9`
- End commit: `293158887e4228a42b9c64bda7d4f0bd32fb4ec9` (unchanged)
- Planning record: initial cycle; prior planning report none; changed decision boundary none; preserved decisions: all accepted M1–M4 code decisions, the M4/M3 deferral wording, the substantive M2 park claims, the 21 registered CTest names, the documented product invariants, the META trace grammar; automatic targeted revisions 0; maximum plan-only cycles 1.

## 1. Identity, provenance, and clean-state verification

- Product `https://github.com/cisarik/contextdesk`, branch `main`: HEAD = `2931588...` = required candidate; parent = `db9ddc1...` = required parent; remote `origin` canonical; tracked/untracked worktree clean; no Git lock or in-progress operation.
- Direct `git ls-remote` of product `refs/heads/main` = `293158887e4228a42b9c64bda7d4f0bd32fb4ec9` (equal to candidate). No fetch/pull/switch/reset/clean/stash/rebase/merge/retarget.
- AP gitlink and `.ap` checkout = `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` = PASS (canonical identity, strict pin, clean submodule, managed `AGENTS.md` block, resolved variant `stable`).
- META `https://github.com/cisarik/meta.git`: public `main` = `917d8a51c98b51b4a6165b4ac98b4aba15ced65c`, a verified later descendant of the prompt baseline `f5b6c523...`; the only changed paths are `projects/contextdesk/00/05-.../00_handout.md`, `.../00_notes.md` plus one unrelated local root handoff artifact; additions-only, no contradiction with the prompt.
- Trace destination is a real directory containing `00_notes.md` and the opening `00_handout.md`; `00_handout.md` SHA-256 = `3ee8ac42f93adc1ae6788b39a29573f3b56bf892b37ed2be4d47d1575094e65f` (exact match). `01_planning_00.md` exists, was read back completely (623 lines), and matches the received prompt field-for-field; a mechanical byte comparison of chat transport is not observable from inside the session (same deviation class already accepted in prior M4 exchanges). `01_report_00.md` was absent before this exchange (no collision).
- M4 trace contains the required `01_report_00/01`, `05`–`10` reports; M3 `05_report_00.md` and the M2 acceptance/park records exist. No unexplained state.

## 2. Source-grounded current-state findings (each tied to the exact candidate)

- **F1 (verified):** `README.md:12–22` still calls M4 Slice B an "implementation candidate — not accepted and not live-verified" and keeps the clause "the next bounded whole is M4 workspace session manager", while `README.md:71` and `ROADMAP.md:31–40,91` record Slice A + Slice B code-accepted (`aca6c68`, `db9ddc1`). This is a real front-door contradiction.
- **F2 (verified):** `AGENTS.md:8–43` is M2-era ("M2 … is in progress", remaining-M2 description) and records neither M3/M4 code acceptance nor the live/physical deferrals; `AGENTS.md:65–76` compounds it ("one named-slice `acceptance-PASS`", "next remaining M2 work is … watchdog/hang, held-modifier-at-death …").
- **F3 (verified):** `AGENTS.md:52–55` and `:95–96`, and `ROADMAP.md:7`, declare the ChatOrchestrator access profile while the M3/M4 successor handoffs (`00_handout.md:23`, M3 `05_handout.md:24`, M4 `00_handout.md:24`) describe a full local Orchestrator session. Policy-confirmation item per COOPERATOR decision 8.
- **F4 (verified):** `ROADMAP.md:286–287` says "M4 is now its own current whole"; `:289` headings and `:299–303` classification still call M4 the current whole; `:337–347` carries the six ledger candidates without dispositions; no duplicate M4/M5 rows and no positive "launch on session start" claim exist (checked).
- **F5 (verified):** `docs/testing-m4.md:3–5` conditions the run on an acceptance that has already happened ("after a separate fresh Worker has accepted the public Slice B implementation candidate"); `:11–13` otherwise keeps the correct no-authority posture.
- **F6 (verified):** `docs/specification.md:214` says "`KService`/`KApplicationTrader`", while `src/workspace/ApplicationLauncher.cpp:153` uses `KService::serviceByStorageId`; `KApplicationTrader` appears nowhere else in code. The checkpoint section (`docs/specification.md:193–211`) does not disclose the late-`desktopCreated` under-recording residual that `08_report_00.md:394–421` and `10_report_00.md:458–482` confirm as accepted non-blocking evidence.
- **F7 (verified):** ADR status lines: `docs/adr/0002:3` and `docs/adr/0004:3` say "accepted for the M4 tree"; `docs/adr/0003:3` says "Implementation-candidate; not accepted" (a direct contradiction with the accepted candidate). `docs/adr/README.md` has no status lines (no drift); `docs/adr/0001:3` says "Live host suspend/resume acceptance remains open" (see S5).
- **F8 (verified, deterministic):** `src/core/Types.h:208–229` returns `true` for any allowed-character string ending in `.desktop` before its reverse-DNS branch; `.desktop`, `..desktop`, `a..desktop`, and `.a.desktop` are all accepted today (03_report_00.md:140–144 names `.desktop` and `a..desktop` explicitly). Call sites: `ApplicationLauncher.cpp:77,98`; also used by `Persistence.cpp:66`, `WorkspacePlan.cpp:93`, `AppController.cpp:1487`. `tests/unit/test_application_launcher.cpp:71–90` has no boundary case for these forms.
- **F9 (verified):** QML runtime has never been executed; only build-time compilation (`03_report_00.md:361–363`, `07_report_00.md:331–332`, `09_report_00.md:102`, `10_report_00.md:582–584`). No owner document claims runtime execution; `docs/testing-m4.md:11–13` already states automated tests do not establish live behavior.
- **F10 (verified):** `5087277:src/app/AppController.cpp:198` wrote `<config root>/workspace-checkpoint.json`; `db9ddc1:src/app/AppController.cpp:198` and the candidate write `<config root>/contextdeck/workspace-checkpoint.json`. The old path existed only in the never-accepted parent candidate; no accepted history or host evidence can have written it.
- **F11 (verified):** `CMakeLists.txt` registers exactly 21 `add_test` names (17 executable targets plus `test_udev_verify`, `test_trial_cutoff`, `test_sleep_hook`, `test_broker_ipc_client`); there is no lint config and no CI.
- **F12 (verified, newly discovered in sweep; corroborated by the M2 park record):** durable docs still list Sessions 22/23/24 subjects as open G4 remainder: `README.md:12,73`; `ROADMAP.md:110,410–419,427–435`; `AGENTS.md:23–24,70–73`; `docs/architecture.md:306–310,362`; `docs/operations.md:269–271,336–341,413,427–429,447–450,452–453,507–509`. The M2 park record itself flags this (`27_report_00.md:215–218, 359–364`: "README/ROADMAP still say live suspend / LED / all-control open" — "documentation drift, not missing G4 evidence"). Sessions 22, 23, 24 are recorded acceptance-PASS for one live suspend/resume cycle, LED return + 18/18 host-remappable controls, and one bounded input-remapper mapping.
- **F13 (verified):** `ROADMAP.md:88` still lists P1 as "Planned, parallel" while G1 is closed (`ROADMAP.md:107`); `27_report_00.md:359` flags the same. `ROADMAP.md:96–97` says "G7 (power actions) tested in M1 IRL" while the G7 gate row says "IRL pending" and the park record says G7 remains pending (`27_report_00.md:366`).

## 3. Decision-ready plan

### 3.1 README repair (changed path: `README.md`)

**R1. Front-door status block, replace lines 7–22 exactly with:**

```text
> **Status: early development.** Five-zone lighting and application context
> (M1) are implemented and recorded as accepted on hardware. The input broker
> (M2) exists in this repository and can be installed **inactive**. The named
> live G4 slices are accepted, but the M2 logical whole remains open. M2 is
> parked with G3 host-mitigated on the authorized reference host; the current
> bounded whole reconciles the accepted M1–M4 state and disposes of the carried
> M4 ledger candidates. **Full G4 remains open**: the named live slices
> (Sessions 16, 19, 22, 23, 24) are accepted, and the remaining work is
> production/autostart readiness, hibernate/hybrid-sleep, and general
> input-remapper coexistence. Independent G3 re-audit of the residual ACL gap
> remains host-mitigated only. M3 workspace-aware lighting is code-accepted on
> `502ae75...`; its physical five-zone IRL observation is deferred by explicit
> COOPERATOR decision. M3 is not closed, and code acceptance is not physical
> acceptance. M4 workspace session manager is code-accepted (Slice A on
> `aca6c68`, Slice B on `db9ddc1`); its live IRL run is deferred by explicit
> COOPERATOR decision. M4 is not closed, and code acceptance is not live or
> physical acceptance. Nothing changes unless the user presses Apply, and
> nothing launches because the session began. The plan lives in
> [ROADMAP.md](ROADMAP.md) and the design in
> [docs/architecture.md](docs/architecture.md).
```

The historical clause "the next bounded whole is M4 workspace session manager" is replaced by "the current bounded whole reconciles the accepted M1–M4 state and disposes of the carried M4 ledger candidates" (smallest truthful successor statement). M2 park claims are preserved word-for-word; exact M3 and M4 wording is used verbatim.

**R2. "The idea" bullet, replace `README.md:39–43` with:**

```text
- **Named workspace sessions (code-accepted; live IRL deferred).** M4 Slice B
  implements named desktop layouts and per-application assignments, observes
  live desktop state, previews the intended diff, and applies it only when you
  press **Použiť** — with a checkpoint revert, typed in-session launch, and
  event-driven placement. Plasma-login autostart stays in M5.
```

**R3. Status table, M4 row (`README.md:71`), change only its final state sentence to:**

```text
**Live IRL deferred by explicit COOPERATOR decision; M4 not closed; code acceptance is not live or physical acceptance; no autostart.**
```

(keep the row's accepted Slice A/B commits and feature detail unchanged).

**R4. Status table, Hardware evidence row (`README.md:73`), replace with:**

```text
| Hardware evidence | G1 control matrix closed (Game Mode / Backlight firmware-only); G2 lighting closed; G4 named live slices accepted (Sessions 16, 19, 22, 23, 24: ARM/pass-through/cutoff, armed watchdog/held modifier, one live suspend/resume cycle, LED return + all 18 host-remappable controls, one bounded input-remapper mapping); full G4 still open (production/autostart readiness, hibernate/hybrid-sleep, general input-remapper coexistence) |
```

Leave the Plan / Lighting / M3 / M2 / Build / Host install rows unchanged (verified truthful).

### 3.2 AGENTS.md state refresh (changed path: `AGENTS.md`)

**A1. Replace the whole "Current repository state" section (`AGENTS.md:8–43`) with:**

```text
## Current repository state

- ContextDeck is a Linux/KDE/Wayland control utility for the Logitech G213
  Prodigy keyboard only. Canonical repo: `https://github.com/cisarik/contextdesk`.
  `ROADMAP.md` is the human plan of record for milestone state, evidence gates,
  and ledger dispositions.
- **M1 `g213-contextdeck-mvp-context-lighting` is implemented and recorded as
  COOPERATOR-accepted IRL.** That acceptance is historical evidence (META notes
  for that whole). It is not a fresh hardware run from later sessions and does
  not close unrelated remaining gates such as G4 or G7.
- **M2 `g213-contextdeck-input-passthrough-safety` is parked, not closed.** The
  named live G4 slices are accepted (Sessions 16, 19, 22, 23, and 24, as
  recorded in the M2 trace), but the M2 logical whole remains open. M2 is parked
  with G3 host-mitigated on the authorized reference host. **Full G4 remains
  open**: the named slices are not rerun or reopened, and the remaining work is
  production/autostart readiness, hibernate/hybrid-sleep, and general
  input-remapper coexistence. The production broker path is in the tree
  (enumerator, explicit `LEASE`/`ARM`, Unix-socket IPC lease, watchdog, broker
  install rule, late uinput ACL rule, suspend/resume sleep hook); an inactive
  install of candidate `cb72ae0` is recorded as `deployment-PASS`.
  `G3-ACL-REPROBE-01` is host-mitigated but was not independently re-audited.
  Do not claim whole M2, whole G4, independent G3 closure, install/remove/
  rollback readiness, production readiness, autostart safety, hibernate/
  hybrid-sleep support, or general coexistence.
- **M3 `g213-contextdeck-workspace-aware-lighting`**: M3 workspace-aware
  lighting is code-accepted on `502ae75...`; its physical five-zone IRL
  observation is deferred by explicit COOPERATOR decision. M3 is not closed, and
  code acceptance is not physical acceptance.
- **M4 `g213-contextdeck-workspace-session-manager`**: M4 workspace session
  manager is code-accepted (Slice A on `aca6c68`, Slice B on `db9ddc1`); its
  live IRL run is deferred by explicit COOPERATOR decision. M4 is not closed,
  and code acceptance is not live or physical acceptance. Nothing mutates
  without the user's explicit Apply and no launch happens at Plasma login.
- Tree: `handout.md`, `AGENTS.md`, `README.md`, `ROADMAP.md`, `LICENSE`, `docs/`,
  `CMakeLists.txt`, `cmake/`, `src/` (session app + `src/broker/`), `ui/`,
  `kwin/`, `tests/unit/`, `packaging/` (systemd, udev, sysusers), and the pinned
  `.ap/` protocol submodule.
- Build: `cmake -S . -B build -G Ninja` then `cmake --build build`. The
  registered CTest suite is owned by `CMakeLists.txt` (`add_test` names). There
  is still no lint config and no CI. Commands in this file are not a grant to
  run them. Implementation happens only under an explicit Orchestrator-issued
  Worker prompt.
- Repository artifacts are not installed host state. Presence of packaging
  files, a local `build/` binary, or `/usr` copies on one machine does not mean
  every host is installed or verified. Host enablement, named physical
  acceptance, and remaining G4/G8 claims remain COOPERATOR-owned operations
  evidence. A documentation commit does not rerun hardware acceptance.
- `handout.md` is the original COOPERATOR-to-ORCHESTRATOR bootstrap contract
  (historical). Read it for intent and safety constraints; it is not a renewed
  bootstrap task. Fast path: §1–6 (roles, delivery, AP/META/trace), §29 (grab
  safety), §33–34 (first Planner), §46–47 (first response).
```

The current bounded whole is intentionally not listed in `AGENTS.md`; it points to `ROADMAP.md` as the plan of record, keeping AGENTS durable across this transient whole.

**A2. Replace the stale M2 bullet inside "Roles, language, authority" (`AGENTS.md:65–76`) with:**

```text
- M2 planning passed and the production wiring is in the tree (enumerator +
  `RealSink`/`EvdevGrabber` behind explicit `LEASE`/`ARM`, session IPC,
  watchdog, G3 packaging, and the late uinput ACL rule). **Nothing in
  documentation grants live grab or autostart.** Full G4 remains open; see
  "Current repository state" above and `ROADMAP.md` for the park claims and the
  named accepted slices. The Super-key **deck layer** brainstorm remains a
  future whole after M3, recorded in `ROADMAP.md`.
```

This is the only edit inside the roles section; its normative role/authority content is unchanged.

**A3. Access-profile policy item — `requires explicit COOPERATOR confirmation`.** If (and only if) the ORCHESTRATOR implementation grant records that confirmation, replace `AGENTS.md:52–55` with:

```text
- Access profile: **Orchestrator** (full project orchestration when the
  session environment exposes those capabilities; an inspection clone is not
  the COOPERATOR’s uncommitted worktree). Selected delivery for this project
  remains **manual** across subsequent exchanges. Dispatch availability in a
  client does not change that selection.
```

and `AGENTS.md:95–96` with:

```text
- This project’s access profile is **Orchestrator** with **manual**
  delivery preserved: the COOPERATOR carries every prompt and report.
```

If no confirmation is recorded, both lines stay byte-identical and the implementation report records the open observation. The hard-rule heading and remaining content are preserved.

### 3.3 ROADMAP reconciliation (changed path: `ROADMAP.md`)

- **B1. Access line (`ROADMAP.md:7`)** — conditional, same policy item: only with recorded confirmation, change "Access profile: ChatOrchestrator; delivery remains manual." to "Access profile: Orchestrator; delivery remains manual."
- **B2. Replace the M4 "Current whole" bullet (`ROADMAP.md:31–40`) with:**

```text
- Code-accepted, live IRL deferred: **M4 `g213-contextdeck-workspace-session-manager`** —
  Slice A (schema 4 named sessions/assignments, `rows`/wrapping observation, pure
  dry-run `WorkspacePlan`, `Plochy` editor) and Slice B (fail-closed
  `DesktopMutator` with user-local checkpoint/revert, typed `ApplicationLauncher`,
  `PlacementResolver` + bridge `PlacementHint`, opt-in non-logging title fallback)
  are code-accepted on `aca6c68` and `db9ddc1`. M4 workspace session manager is
  code-accepted (Slice A on `aca6c68`, Slice B on `db9ddc1`); its live IRL run is
  deferred by explicit COOPERATOR decision. M4 is not closed, and code acceptance
  is not live or physical acceptance. Nothing mutates without the user's explicit
  Apply and no launch happens at Plasma login.
- Current whole: **M4 state and ledger reconciliation** — documentation-only
  reconciliation of the accepted M1–M4 state and disposition of the carried M4
  ledger candidates; no host, device, desktop, launch, broker, packaging, or
  license mutation. Ledger dispositions are recorded in the M4 backlog section.
```

- **B3. Parked-M2 paragraph (`ROADMAP.md:41–54`):** change the named-slice parenthetical to "(ARM / pass-through / cutoff; armed watchdog with a held modifier; one live suspend/resume cycle; LED return and all eighteen host-remappable controls; one bounded input-remapper mapping)"; change "A systemd-sleep hook in the tree can stop an active broker before sleep and start it once afterwards, always disarmed; that is not live suspend evidence." to "A systemd-sleep hook in the tree stops an active broker before sleep and can start it once afterwards, always disarmed; one live suspend/resume cycle is a recorded named slice (Session 22)."
- **B4. Replace the P1 milestone row (`ROADMAP.md:88`) with:**

```text
| P1 | `g213-contextdeck-control-evidence` | Physical control matrix for all 20 controls (COOPERATOR-run probe) — G1 | — | **Done** — G1 closed: 18 host-remappable, Game Mode and Backlight firmware-only |
```

- **B5. Dependency paragraph (`ROADMAP.md:96–97`):** change only "G7 (power actions) tested in M1 IRL." to "G7 (power actions) remains pending its own IRL acceptance."
- **B6. Replace the G4 gate row (`ROADMAP.md:110`) with:**

```text
| G4 | Interception, crash, hang, release, recovery acceptance | Enabling remapping | **Open.** Named live slices accepted (Sessions 16, 19, 22, 23, 24): ARM/pass-through/cutoff, armed watchdog abort with a held modifier, one live suspend/resume cycle, LED return and all eighteen host-remappable controls, one bounded input-remapper mapping. Remaining: production/autostart readiness (G8/M5), hibernate/hybrid-sleep, general input-remapper coexistence. A documentation or hook-implementation commit does not close G4 |
```

- **B7. M3 backlog sentence (`ROADMAP.md:286–287`):** change "M4 is now its own current whole;" to "M4 has since been code-accepted with its live IRL deferred (see *Where we are now*);".
- **B8. M4 backlog heading (`ROADMAP.md:289`):** change to "### Workspace session manager — code-accepted, live IRL deferred `g213-contextdeck-workspace-session-manager`".
- **B9. Replace the M4 classification (`ROADMAP.md:299–303`) with:**

```text
**Classification:** milestone M4, code-accepted and not closed. M4 workspace
session manager is code-accepted (Slice A on `aca6c68`, Slice B on `db9ddc1`);
its live IRL run is deferred by explicit COOPERATOR decision. M4 is not closed,
and code acceptance is not live or physical acceptance. All live desktop
mutation, launch, and bridge reload remain separately granted COOPERATOR
operations. Nothing here grants host or desktop mutation.
```

- **B10. Replace the ledger-candidate paragraph (`ROADMAP.md:337–347`) with the disposition list below** (it is the single plan-of-record ledger view; no second task queue is created):

```text
**Deferred live IRL (COOPERATOR decision, 2026-09-14):** the `docs/testing-m4.md`
run (explicit Apply, checkpoint revert, launch-on-apply, placement/maximize,
opt-in title fallback) is deferred. M4 stays not closed and no live desktop,
launch, placement, or compositor behavior is claimed. When run, it needs
explicit mutation-class authority, a named checkpoint, and one demonstrated
recovery route.

**Ledger disposition (M4 state and ledger reconciliation):** every carried M4
ledger candidate is disposed here.
- ADR 0002/0003/0004 status phrasing — **fixed**: the status lines no longer say
  "accepted for the M4 tree"; they record the code-accepted slices and the
  deferred live IRL.
- `.desktop` id predicate accepting trivially short forms — **fixed**:
  `workspaceDesktopIdLooksValid` rejects empty or dot-only prefixes
  (`.desktop`, `a..desktop`) while still accepting `a.desktop`,
  `org.kde.dolphin.desktop`, and reverse-DNS ids such as `org.kde.dolphin`.
- `KApplicationTrader` named only in the specification — **fixed**:
  `docs/specification.md` now names `KService::serviceByStorageId` and
  `KIO::ApplicationLauncherJob`.
- Late-`desktopCreated` checkpoint-disclosure gap — **fixed**: the checkpoint
  section discloses the abnormal-ordering under-recording residual.
- QML runtime validated only at build time — **parked**: the deferred M4 live
  IRL run (`docs/testing-m4.md` steps 2–5) and the separate later UI/IRL whole
  own the first runtime validation; no runtime evidence is claimed.
- Orphaned old-path checkpoint from the never-accepted parent candidate —
  **invalidated**: the pre-correction path existed only in the never-accepted
  parent `5087277`; no accepted history or host evidence exists, and no note
  instructs touching a user file.
```

- **B11. Replace the "G4 remains open" paragraph (`ROADMAP.md:410–419`) with:**

```text
**G4 remains open.** Named slices from Sessions 16, 19, 22, 23, and 24 are
recorded as accepted (ARM / pass-through / cutoff and typing after descriptor
close; armed watchdog abort with a held modifier; one live suspend/resume cycle;
LED return and all eighteen host-remappable controls; one bounded input-remapper
mapping). Neither those slices nor later documentation close this whole.
Independent G3 re-audit of the residual ACL gap remains host-mitigated and is
not a fresh audit. Remaining: production/autostart readiness (G8/M5),
hibernate/hybrid-sleep, and general input-remapper coexistence. A host may or
may not have installed the packaging files; that is operations evidence. The
broker must stay static/inactive with no autostart until those remaining
claims are separately authorized and accepted.
```

- **B12. Replace the "Next remaining M2 work" paragraph (`ROADMAP.md:427–435`) with:**

```text
**Next remaining M2 work:** named slices are accepted. A separately
authorized fresh task remains for production/autostart readiness (G8/M5),
hibernate/hybrid-sleep, or general input-remapper coexistence. Documentation
here does not grant grab, ARM, autostart, live suspend, or host mutation, and
does not choose which remainder comes next. Production safety gaps already
visible in source (silent uinput write errors; virtual-device capabilities from
`passthroughCapabilities()` rather than measured source bits / LED return
path; logind `sd_pid_get_session` vs user-manager-launched session apps) stay
in that remainder unless a later prompt names them.
```

### 3.4 Ledger disposition table

| # | Item | Evidence at candidate | Disposition | Destination / exact change | Validation | Code/tests |
|---|------|---------------------|-------------|----------------------------|------------|------------|
| 1 | ADR 0002/0004 "accepted for the M4 tree" phrasing (carried; 0003 same class) | `docs/adr/0002:3`, `0004:3`; `0003:3` "Implementation-candidate; not accepted" | fix-now | ADR status lines 0002/0003/0004 (status text below) | `rg` finds no "accepted for the M4 tree"/"Implementation-candidate"; statuses name `db9ddc1`/`aca6c68` and the deferral | no |
| 2 | `.desktop`-suffix predicate accepts trivially short forms (carried) | `src/core/Types.h:221–229`; `03_report_00.md:140–144` | fix-now (in) | `src/core/Types.h` + `tests/unit/test_application_launcher.cpp` | new causal accept/reject regressions; focused + full CTest | yes |
| 3 | `KApplicationTrader` named only in the specification (carried) | `docs/specification.md:214` vs `ApplicationLauncher.cpp:153` | fix-now | `docs/specification.md:214` | `rg` finds no `KApplicationTrader` | no |
| 4 | Late-`desktopCreated` checkpoint-disclosure gap (carried) | `08_report_00.md:394–421`; `10_report_00.md:458–482`; spec `193–211` lacks disclosure | fix-now | `docs/specification.md` checkpoint/revert paragraph; mirrored clause in `docs/operations.md` §10 | disclosure sentence present; "never a desktop it did not create" preserved | no |
| 5 | QML runtime never executed (carried) | `03_report_00.md:361–363`; `07_report_00.md:331–332`; `09:102`; `10:582–584` | park | deferred M4 live IRL run `docs/testing-m4.md` steps 2–5 + later UI/IRL whole; one truthful sentence added in `testing-m4.md` | no runtime evidence claimed | no |
| 6 | Possible orphaned old-path checkpoint (carried) | `5087277:AppController.cpp:198` vs `db9ddc1`/candidate `:198`; parent never accepted | invalidate | no action; recorded in ROADMAP ledger list (B10) | none | no |
| 7 | README front-door contradicts status table/ROADMAP (new) | `README.md:12–22` vs `README.md:71`, `ROADMAP.md:31–40,91`; stale "next bounded whole" clause; "in progress" bullet `39–43` | fix-now | README R1/R2/R3/R4 | exact M3/M4 wording present; no "implementation candidate"; `rg` checks | no |
| 8 | AGENTS M2-era state (new) | `AGENTS.md:8–43`; roles bullet `65–76` | fix-now | AGENTS A1/A2 | exact M3/M4 wording and park claims present; ROADMAP pointer present | no |

**ADR status replacement text (row 1):**

`docs/adr/0002` line 3–6, replace with:

```text
Status: accepted. Slice B implements this decision in code and is code-accepted
on `db9ddc1`. The live desktop mutation itself remains gated by an explicit
user Apply and has no standing host authority from this repository; running it
against a real session is a separate COOPERATOR grant, and the M4 live IRL run
is deferred by explicit COOPERATOR decision. M4 is not closed.
```

`docs/adr/0003` line 3, replace with:

```text
Status: accepted. The schema is implemented and code-accepted (Slice A on
`aca6c68`; Slice B consumes it on `db9ddc1`). The M4 live IRL run is deferred by
explicit COOPERATOR decision, and M4 is not closed.
```

`docs/adr/0004` line 3–5, replace with:

```text
Status: accepted. Slice B implements the typed launcher in code and is
code-accepted on `db9ddc1`. A launch happens only on the user's explicit Apply
(or an in-transaction `desktopCreated`) and still requires a separate COOPERATOR
IRL grant; the M4 live IRL run is deferred by explicit COOPERATOR decision, and
M4 is not closed.
```

`docs/adr/README.md` needs no change (no status lines).

### 3.5 Typed desktop-id decision: **IN**

The item is small, fail-closed, deterministic, and fixes a verified defect at its single owner. It rejects only empty/dot-only basename forms while preserving every well-formed `.desktop` and reverse-DNS id used by accepted schema-4 documents and tests.

**Exact strengthened semantics (`src/core/Types.h:208–229`), replace the function body with:**

```cpp
[[nodiscard]] inline bool workspaceDesktopIdLooksValid(const QString &value)
{
    if (value.isEmpty() || value.size() > 256) {
        return false;
    }
    for (const QChar ch : value) {
        if (ch.category() == QChar::Other_Control) {
            return false;
        }
        if (!(ch.isLetterOrNumber() || ch == QLatin1Char('.') || ch == QLatin1Char('-') || ch == QLatin1Char('_'))) {
            return false;
        }
    }
    QString base = value;
    if (value.endsWith(QLatin1String(".desktop"))) {
        base = value.left(value.size() - 8);
    } else if (!value.contains(QLatin1Char('.'))) {
        return false;
    }
    if (base.isEmpty() || base.startsWith(QLatin1Char('.')) || base.endsWith(QLatin1Char('.'))
        || base.contains(QLatin1String(".."))) {
        return false;
    }
    return true;
}
```

**Accept/reject table (before → after):**

| Input | Before | After | Reason |
|---|---|---|---|
| `a.desktop` | accept | accept | ordinary single-name desktop id (accepted fixtures) |
| `org.example.A.desktop` | accept | accept | reverse-DNS + suffix (accepted fixtures) |
| `org.kde.dolphin.desktop` | accept | accept | real storage id |
| `org.kde.dolphin` | accept | accept | reverse-DNS storage id, no suffix |
| `kde.dolphin`, `a.b` | accept | accept | one-dot reverse-DNS branch unchanged |
| `.desktop` | accept | **reject** | empty basename (the named defect) |
| `..desktop` | accept | **reject** | dot-only basename |
| `a..desktop` | accept | **reject** | empty label inside basename |
| `.a.desktop` | accept | **reject** | basename begins with dot |
| `a.`, `.a`, `a..b`, `a` | reject | reject | unchanged non-suffix rules |
| `/usr/bin/firefox`, `sh -c …`, `systemd-run …`, `kstart …` | reject | reject | character allow-list |

**Files:** `src/core/Types.h` only (shared predicate; both `ApplicationLauncher.cpp:77,98` call sites and the persistence/plan/controller users inherit it); no `ApplicationLauncher.cpp` change is needed.

**Causal regression (`tests/unit/test_application_launcher.cpp`):** add `.desktop`, `..desktop`, `a..desktop`, `.a.desktop` to `invalidDesktopIdsAreRejected` (expect `InvalidDesktopFile`, invoker call count unchanged), and add one slot that proves the positive boundary through the launcher (e.g. `a.desktop` and `org.example.Editor` produce `Launched` with the typed id passed to the invoker seam). Add a small direct-predicate table in the same target for `org.kde.dolphin` / `kde.dolphin` acceptance. The regression is causal: on the un-fixed parent the rejection cases return `Launched`/`Failed` (predicate `true`), on the candidate they return `InvalidDesktopFile`.

**Compatibility statement for already-saved documents:** the only schema-4 values that become invalid are empty/dot-only basename forms (`.desktop`, `..desktop`, `a..desktop`, `.a.desktop` and similar); they cannot resolve to a KService and could previously only have been stored by hand-editing or by typing an absurd value into the launch-id field (the UI setter uses the same predicate). After hardening, a document containing such a value fails `load` with the existing preserved-bytes, pass-through/untouched fail-safe path; no accepted fixture, UI flow, or `desktop_file_name` default path contains a rejected form.

**Acceptance route:** because this changes a semantic validator, AP §Acceptance requires a fresh independent acceptance Worker for the resulting candidate.

### 3.6 QML runtime disposition

**Park with an evidence-backed destination.** QML runtime has never been executed; durable docs must not imply otherwise. Add one truthful sentence to `docs/testing-m4.md` after line 13: "QML runtime behavior has so far been validated only by build-time compilation; these steps are its first runtime validation." The bounded runtime-validation step is owned by the deferred `docs/testing-m4.md` run (its steps 2–5 exercise the Plochy preview/Apply/revert controls and assignment fields) and by the separate later UI/UX whole. No runtime evidence is fabricated or claimed.

### 3.7 Orphaned checkpoint disposition

**Invalidate — no action, no new documentation note.** The old path `<config root>/workspace-checkpoint.json` existed only in commit `5087277`, a never-accepted implementation candidate that was never live-run (verified via `git show 5087277:src/app/AppController.cpp` vs `db9ddc1`/candidate). The corrected product path is `<config root>/contextdeck/workspace-checkpoint.json`. No accepted history or host evidence exists for the old file, and a public note about an unaccepted build artifact would risk inviting deletion of a user-local file; the disposition is recorded in the ROADMAP ledger list (B10) only.

### 3.8 Consistency sweep result

**Fix-now (inside ceiling):**

- **S1 — M2/G4 remainder drift (F12):** all listed occurrences in `README.md`, `ROADMAP.md`, `docs/architecture.md`, `docs/operations.md` are replaced with the accepted named-slice wording and the park remainder (production/autostart readiness, hibernate/hybrid-sleep, general input-remapper coexistence). Exact replacement text: README R1/R4; ROADMAP B3/B6/B11/B12; architecture: replace `docs/architecture.md:305–310` with "Named physical slices are recorded as accepted (Sessions 16, 19, 22, 23, 24): explicit ARM, sampled pass-through, matching-invocation cutoff and typing after descriptor close; armed watchdog abort with a held modifier; one live suspend/resume cycle; LED return and all eighteen host-remappable controls; one bounded input-remapper mapping. Remaining G4 claims: production/autostart readiness, hibernate/hybrid-sleep, and general coexistence." and `:362` "named slice accepted" → "named slices accepted"; operations E1–E7 below.
- **S2 — `ROADMAP.md:88` P1 row stale** ("Planned, parallel" vs G1 closed): B4.
- **S3 — `ROADMAP.md:96–97` G7 line** vs G7 gate row and park record: B5.
- **S4 — `AGENTS.md:65–76` M2 bullet stale:** A2.
- **S5 — `docs/adr/0003:3`** is absorbed into ledger row 1 (same class as 0002/0004).
- **Operations.md exact edits:** (E1) `:269–271` "one named slice is recorded as accepted" → "named live slices are recorded as accepted (Sessions 16, 19, 22, 23, 24)"; (E2) `:336–341` replace the Worker 16/19 sentence and "Full G4 remains open (LED return, all-control fidelity, live host suspend/resume, production/autostart)." with the canonical named-slice sentence plus "Full G4 remains open (production/autostart readiness, hibernate/hybrid-sleep, general input-remapper coexistence)."; (E3) `:413` third column → "LED return; all-control fidelity; live suspend (each proven only by its own named slice)"; (E4/E5) `:427–429` and `:447–450` replace "LED return, all-control fidelity, and live host suspend/resume still need G4." with "LED return, all-control fidelity, and live suspend/resume have their own accepted named slices (Sessions 22 and 23); production/autostart, hibernate/hybrid-sleep, and general coexistence remain open G4."; (E6) `:452–453` "The named slice does not authorize autostart." → "The named slices do not authorize autostart."; (E7) `:507–509` "Host suspend/resume acceptance remains open G4." → "One live suspend/resume cycle is a recorded named slice (Session 22); hibernate/hybrid-sleep and the production path remain open G4."; (E8) §10 checkpoint bullet `:668–669` add "(a desktop created by this Apply whose signal arrived only after the transaction ended may be left in place; under-removal is the fail-safe direction)".
- **Specification/architecture/testing-m4 edits:** §3.4 row 3, row 4; S1; §3.6.

**Checked, no action:** `docs/adr/README.md` (no status drift); ROADMAP has no duplicate M4/M5 rows and no positive launch-at-login claim; README status table Plan/M2/M3/M4 rows are truthful.

**Out (ceiling), recorded for the ORCHESTRATOR/COOPERATOR:**

- `docs/adr/0001:3–4` "Live host suspend/resume acceptance remains open" is the same class of drift after Session 22; the ceiling excludes `docs/adr/0001`. Recommended later one-line fix: "Status: accepted. The sleep hook is implemented and code-accepted with the M2 tree; one live suspend/resume cycle is a recorded named slice (Session 22), while hibernate/hybrid-sleep and the production path remain open." No PARTIAL is returned for this bounded out-of-ceiling observation.
- `docs/testing-m3.md:3–5` has the same stale-tense class as `testing-m4.md` ("after a separate fresh Worker has accepted the public implementation candidate"); M3 testing files are excluded from the ceiling. Recommended later fix or explicit acceptance that the precondition is historical.
- `docs/hardware/*` and `docs/testing-m2.md` were not swept (out of ceiling and out of the read-only owner list).

### 3.9 Implementation slice

**Exact minimal changed-path allowlist (12 paths):**

```text
README.md
AGENTS.md
ROADMAP.md
docs/specification.md
docs/architecture.md
docs/operations.md
docs/testing-m4.md
docs/adr/0002-host-desktop-mutation-authority.md
docs/adr/0003-workspace-assignment-schema.md
docs/adr/0004-typed-application-launch.md
src/core/Types.h
tests/unit/test_application_launcher.cpp
```

No `CMakeLists.txt` change (the registered `test_application_launcher` target already exists), no `src/workspace/ApplicationLauncher.cpp` change, no `docs/adr/README.md` change, no `.ap`, broker, packaging, `ui/`, `kwin/`, `LICENSE`, or host path.

**Stages:**

1. Code: apply the strengthened predicate in `src/core/Types.h`; add the causal regression slots in `tests/unit/test_application_launcher.cpp`.
2. Docs: README R1–R4; AGENTS A1–A2 (A3/B1 only if the grant records COOPERATOR confirmation); ROADMAP B2–B12; specification (KService wording + checkpoint disclosure); architecture (S1); operations E1–E8; testing-m4 tense + QML sentence; ADR 0002/0003/0004 status lines.
3. Validation: `./.ap/ap doctor`; `cmake -S . -B build -G Ninja`; `cmake --build build`; focused `ctest --test-dir build --output-on-failure -R '^(test_application_launcher|test_profile_persistence|test_profile_resolver|test_workspace_plan)$'`; full `ctest --test-dir build --output-on-failure` (registered 21-test suite); `git diff --check`; changed-path set equality against the 12-path allowlist; content checks: no `implementation candidate|not accepted and not live-verified` in README, no `accepted for the M4 tree|Implementation-candidate` in `docs/adr`, no `KApplicationTrader`, exact M3/M4 wording present in README/AGENTS/ROADMAP, park wording present.
4. One commit is suitable (bounded cross-cutting docs + one predicate + one test; message e.g. `Reconcile M4 state docs and dispose of carried ledger candidates`). Rollback is an ordinary `git revert` of that single commit (never reset/clean/stash/checkout). Push only if the implementation grant separately grants publication; otherwise the candidate is the local commit and the acceptance route uses the exact commit identity.
5. One terminal implementation report point: `02_report_00.md` (fresh session routing) or the next contiguous exchange filename (current-session renewal).

**Why the full registered suite is the broad gate:** `CMakeLists.txt` owns the suite, there is no lint config and no CI, the predicate is shared across persistence/resolver/plan/launcher, and the full suite is ~70 s including the private-bus receiver test; focused-only runs miss `test_workspace_lighting`/`test_workspace_mutator` collateral, and the M4 precedent used full 21/21.

### 3.10 Acceptance boundary

- With the code item admitted, the candidate changes semantic validator behavior (`workspaceDesktopIdLooksValid`), so AP §Acceptance ("fresh independent acceptance is required when the selected route changes … semantic validators") requires a **fresh independent acceptance Worker** against the exact published/recorded implementation commit, read-only, with the 12-path allowlist, a detached candidate, independent configure/build, the focused route including `test_application_launcher`, the full registered 21-test suite, docs state checks, and public-ref equality. The accepted candidate is the single implementation commit whose required parent is `2931588...`, named exactly by the ORCHESTRATOR's acceptance prompt.
- If the ORCHESTRATOR drops the code item before implementation (fallback), the plan becomes docs-only E0/E1 and direct ORCHESTRATOR review would suffice; that fallback is not the plan's primary decision.

### 3.11 Claim matrix

- **Implementation-PASS could establish:** the durable state text matches the accepted M1–M4 evidence and standing deferrals with no widened claim; the predicate rejects the identified pathological forms and still accepts well-formed ids; the causal regressions exist, are registered, and pass; focused and full suites pass; the changed-path set equals the allowlist.
- **Acceptance-PASS could establish (fresh independent):** independent verification of the same on the exact public commit, including that no state claim was widened and the regression is causal and non-vacuous.
- **Explicit non-claims:** no implementation-PASS or acceptance-PASS in this planning exchange; no M4 closure or live desktop/launch/placement behavior; no M3 closure or physical five-zone observation; no M2/G4 closure, independent G3 re-audit, install/remove/rollback, production readiness, autostart, hibernate/hybrid-sleep, or general coexistence; no M5, remapping, deck-layer, per-key RGB, power-action, or license-selection claim; no physical hardware acceptance; no claim that any documentation change is accepted before its own later implementation and acceptance; no claim that Session 27 was a fresh Worker result; no host, device, desktop, launch, broker, KWin, OpenRGB, package, udev, service, or systemd mutation.

### 3.12 Later implementation prompt outline

- **Routing:** logical whole `m4-state-and-ledger-reconciliation`; recommended `current-worker-session` renewal with `Native planning mode: not-used` (the planning record allows implementation in this session; the next contiguous exchange ordinal and matching `01_implementation_01.md`/`01_report_01.md` filenames), or a genuinely fresh Worker `02/01` with `02_implementation_00.md`/`02_report_00.md` if the COOPERATOR prefers a new session. Manual delivery preserved; no subagents.
- **Baseline:** exact product candidate `2931588...` with required parent `db9ddc1...`, canonical remote, clean worktree, direct `ls-remote` equality, AP pin `0cf2cff...` with `ap doctor` PASS/`stable`, META trace identity `projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/`.
- **Authority:** product source mutation and one product commit (push only if separately granted); no host/device/desktop/launch/broker/KWin/OpenRGB/package/udev/service/systemd mutation; no `.ap`, `LICENSE`, dependencies, `ui/`, `kwin/`, or META Git mutation.
- **Allowlist:** the exact 12 paths above (nothing else).
- **Boundaries:** no runtime behavior change other than the admitted predicate hardening; access-profile line changes only if the grant records explicit COOPERATOR confirmation; if not confirmed, leave those lines byte-identical and record the open observation.
- **Validation:** as in §3.9 stage 3.
- **Report contract:** standard Worker header and coordinates; status/evidence block; start/end commit; changed-path proof; validation counts from real output; deviations/risks/non-claims; exactly one smallest next step; critique; `Logical-whole closure: not-closed`; authority expiry; META report readback at the exact destination.

### 3.13 Residual uncertainty

- **Access-profile wording:** not resolvable from repository evidence; per COOPERATOR decision 8 the default is to leave `AGENTS.md:52–55`, `AGENTS.md:95–96`, and `ROADMAP.md:7` unchanged and record the open observation unless the implementation grant records confirmation.
- **Code item acceptance cost:** the plan decides "in"; if the ORCHESTRATOR instead prefers a docs-only whole, drop the three code/test paths and park the predicate (recorded disposition changes from `fixed` to `parked`), and ORCHESTRATOR-direct review suffices.
- **Out-of-ceiling stale sentences** (`docs/adr/0001`, `docs/testing-m3.md`): recorded; the ORCHESTRATOR may widen the ceiling by two one-line edits or leave them for a later whole.

## 4. E2 evidence envelope and validation rationale

Implementation is cross-cutting but reversible: documentation plus one bounded semantic-validator hardening with focused tests and ordinary `git revert`. No host, device, desktop, launch, broker, packaging, or production mutation. Validation uses inspection/provenance, focused tests for the changed predicate, the full registered CTest suite as the project's broad gate (no lint/CI exists), and docs consistency checks; the validator change makes a fresh independent acceptance proportionate (E2 with the AP semantic-validator trigger).

## 5. Mutations

This planning exchange made no product, AP, host, service, desktop-configuration, launch, device, dependency, test/build, or Git publication mutation. No `reset`/`clean`/`stash`/`checkout`/commit/push; product HEAD and worktree are unchanged at `2931588...`; META Git refs and history are unchanged. The only META write is the authorized report file `projects/contextdesk/00/05-m4-state-and-ledger-reconciliation/01_report_00.md`; it was not staged, committed, or pushed.

## 6. Trace prompt/report persistence and readback

- Prompt `01_planning_00.md`: present as a regular file at the exact destination; read back completely (623 lines); header, coordinates, content, and filename match the received prompt field-for-field. A mechanical byte comparison of chat transport is not observable from inside the session.
- Report `01_report_00.md`: the planning exchange ran under an active native Plan Mode whose read-only control blocked the file write; per AP the complete content was preserved in client output, and after the COOPERATOR switched the session to build mode at the end of exchange 01 the complete terminal report was written once to the exact destination. The destination was absent before the write (no collision, no overwrite). The file was then read back completely and its header, coordinates `01/01`, content, and filename were verified. Report content, coordinates, and evidence are unchanged by the persistence step; only the status/result-evidence fields reflect that delivery is now complete. **Deviation class:** first rendering was chat-only; resolved within exchange 01 with a verified write.

## 7. Deviations, risks, unresolved decisions, missing evidence

- Report-file persistence was blocked during the planning phase by the active native Plan Mode read-only control; the complete report was first delivered in the client chat and persisted unchanged (other than the delivery-status fields) at the COOPERATOR's request in the same Worker session after the mode switch. This is the single delivery deviation; readback is complete.
- The M2-remaining drift (F12) was found in the sweep and is not named in the planning prompt's findings list; it is corroborated by the M2 park record and is included as fix-now.
- The access-profile wording remains gated on explicit COOPERATOR confirmation.
- `docs/adr/0001` and `docs/testing-m3.md` carry out-of-ceiling stale sentences; no ceiling widening was performed.
- Non-public data was kept out: no local machine paths, host details, event-node numbers, desktop names/UUIDs, captions, serials, or credentials appear in this report; only public repository-relative paths and semantic state are used.
- Missing evidence: mechanical byte identity of the chat-transported prompt; independent acceptance of the eventual implementation (out of this grant).

Smallest next step: ORCHESTRATOR reconciliation of this plan and, only if accepted, a separate implementation Worker prompt.

Resolved Execution Issues / Near-Misses: one, the report-file write was initially blocked by the client's native Plan Mode read-only control. The complete content was preserved in client output per AP instead of bypassing the control; after the COOPERATOR switched the session to build mode in the same exchange, the report was written once to the exact META path, read back completely, and verified. No plan content was regenerated, prettified, or reinterpreted by the persistence step.

Pre-Existing Failure Classification: none

Orchestration critique:

MEASURED: Sessions 22/23/24 are recorded acceptance-PASS for one live suspend/resume cycle, LED return plus 18/18 host-remappable controls, and one bounded input-remapper mapping, yet `README.md`, `AGENTS.md`, `ROADMAP.md`, `docs/architecture.md`, and `docs/operations.md` still list those subjects as open G4 remainder; the M2 park record itself flags this (`27_report_00.md:215–218, 359–364`); effect: without the sweep fixes this reconciliation would commit a known contradiction into the plan of record; smallest correction: the S1 fix-now replacements above.

LEAD: `docs/adr/0001` and `docs/testing-m3.md` carry the same class of stale state but are outside the changed-path ceiling; cheapest useful check: the ORCHESTRATOR decides whether to widen the ceiling by two one-line edits or defer them to a later whole.

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.

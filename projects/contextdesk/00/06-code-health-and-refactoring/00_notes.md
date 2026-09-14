# ContextDeck — Orchestrator notes: code health & refactoring

Artifact relationship: historical orchestration notes for the META trace of
`code-health-and-refactoring`. They grant no task, implementation, host, Git,
acceptance, publication, or closure authority.

## Opening reconciliation — 2026-09-14

- Predecessor whole: `m4-state-and-ledger-reconciliation` — closed by
  ORCHESTRATOR (acceptance-PASS on `235d467c752958694dad4be7bcc31e66406dbdcc`,
  publication-PASS, ledger dispositions recorded in `01_closure.md`). M4, M3,
  and M2 logical wholes remain not closed with their standing deferrals; M1
  remains historical IRL acceptance.
- Successor continuity record: `00_handout.md` (predecessor full-Orchestrator
  authorship), archived by the COOPERATOR in META first-add
  `f4f93e2c8bed9009bca5c16755bd9413b54aa951` (SHA-256
  `7c4031d49b8acecc6f1ac40ca37afaadcdcca632677c74eb328711672937f26e`). Its
  internal self-references remain historical and are not rewritten.
- Selected successor whole: `code-health-and-refactoring` (COOPERATOR direction
  carried in the handout; identity/scope confirmation pending). Objective:
  behavior-preserving reduction of structural complexity, duplication, and mixed
  responsibilities in session-app, core, and UI-facing code before the later
  UI/UX whole; no behavior, visuals, product claims, or safety boundaries
  change.
- Verified anchors at opening (fresh clones and direct public refs): product
  public `main` = `235d467c752958694dad4be7bcc31e66406dbdcc` equals the local
  checkout HEAD with a clean worktree; `.ap` gitlink and detached checkout
  `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`; `./.ap/ap doctor` PASS with
  variant `stable`; public META `main` =
  `f4f93e2c8bed9009bca5c16755bd9413b54aa951`; public AP `main` =
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (ahead of the pin; not adopted);
  pin `0cf2cff` is an ancestor of public AP `main`.
- Precursor trace: all seven `05-...` artifact SHA-256 values match the handout
  table exactly (accepted plan, implementation prompt/report, acceptance
  prompt/report, closure record, opening handout).
- Carried observations (active, non-authorizing): (1) the `ROADMAP.md`
  M2-backlog sleep-hook bullet ending "Not autostart. Not live suspend evidence.
  ADR 0001." and the `docs/testing-m2.md` remaining-G4 lists; (2)
  `AGENTS.md:67-69`, `AGENTS.md:105-106`, and `ROADMAP.md:7` still declare
  `ChatOrchestrator` while recent sessions run as a full local Orchestrator
  (policy item; explicit COOPERATOR decision required, exact proposed wording
  from the closed plan §3.2 A3 / §3.3 B1 remains unimplemented); (3) transient
  "current whole" wording in `ROADMAP.md:41` and `README.md:10-11`; (4) standing
  deferrals: M4 live IRL, M3 physical five-zone observation, the M2/G4/G3
  remainders, M5, the deck layer, and G6 licensing; (5) the `ROADMAP.md`
  production-safety-gaps list requires re-verification at the candidate
  (opening spot-check: `src/broker/ForwardingEngine.cpp` fails closed on sink
  write failure; `src/broker/Acquisition.cpp` applies measured capabilities
  before virtual creation with `passthroughCapabilities()` used only by tests;
  `src/broker/SessionIpc.cpp` has the exactly-one-eligible-session fallback).
- No AP-contracted upgrade-observation ledger is declared in project rules
  outside the managed block.
- Delivery selection preserved: manual COOPERATOR delivery of every Worker
  prompt and report; one active Worker; no subagents and no automated dispatch.
- META Git archival remains a COOPERATOR action; the prepared prompt/report pair
  is archived together only after the report exists, preserving earlier trace
  files.
- Active Worker: none before manual delivery of the first planning prompt.
  Active mutation: none.
- Open COOPERATOR decisions at opening: whole identity/scope and candidate-slice
  selection; access-profile wording; confirmation that physical testing remains
  deferred; G6 licensing timing; absorption of the carried documentation
  observations into this whole or a park.
- Next exchange: initial Planner, Worker session `01`, exchange `01`,
  `fresh-worker-session`, Worker session profile Planner, Native planning mode
  required, manual delivery; prompt `01_planning_00.md`, report
  `01_report_00.md`, destination
  `projects/contextdesk/00/06-code-health-and-refactoring/`.

## Opening decisions — 2026-09-14

- COOPERATOR decision: `code-health-and-refactoring` approved; maximal
  achievable depth authorized within behavior preservation ("we can go as deep
  as it goes"), with an explicit instruction to make no unverified or mistaken
  changes.
- Interpretation recorded: all candidate slices S1–S7 are eligible for the
  Planner's plan; the Planner selects, merges, splits, orders, and bounds them
  and may return a justified split proposal.
- Access-profile policy item: not confirmed; `AGENTS.md:67-69`,
  `AGENTS.md:105-106`, and `ROADMAP.md:7` stay byte-identical and the item
  remains an open COOPERATOR decision. The Planner prompt forbids changing those
  lines.
- Physical testing: remains deferred by the approved scope; no host, device, or
  desktop operation belongs to this whole.
- G6 licensing: remains deferred; this whole does not need a license decision.
- Carried documentation observations: absorbed into this whole (S7) with exact
  evidence; the `ROADMAP.md` production-safety-gaps list is re-verified against
  the candidate before any correction.
- First exchange prepared: initial Planner prompt `01_planning_00.md`
  (SHA-256
  `b9969040e1b735bdeda3800f88f4f70048339720ddcea788fa52ba9da649ac7e`),
  Worker session `01`, exchange `01`, `fresh-worker-session`, Native planning
  mode required, manual COOPERATOR delivery; report `01_report_00.md`; archival
  of the prompt/report pair remains a COOPERATOR action and waits for the
  report.
- Active Worker: none before manual delivery. Active mutation: none.

## Planning report repair — 2026-09-14

- Exchange `01` (`01_planning_00.md`, Worker session `01`) produced, at the
  report path `01_report_00.md`, a client-native plan artifact — non-English,
  without the terminal-report header, coordinates, or compact core, and
  containing a local machine path — instead of a valid terminal Worker report.
  Reconciliation: the artifact is not a report and must not be archived; its
  plan content is treated as frozen; the exchange did not terminate with a valid
  outcome.
- ORCHESTRATOR decision: Planner-Artifact Report Completion Repair. Completion
  exchange issued as Worker session `01`, exchange `02`,
  `current-worker-session`, Native planning mode `not-used`,
  report-rendering-only authority; prompt `01_completion_01.md` (SHA-256
  `7faae79229a50cc83ad5993efbbc73685a13f4a573b0b7aaa59c60906a0f4910`), report
  `01_report_01.md`, `Archival: wait-for-report`. Planning cycle effect: none.
  The completion report must render the frozen plan in English, preserve every
  decision, and exclude local paths.
- The frozen artifact `01_report_00.md` is superseded as a terminal outcome; it
  must not be committed, and the COOPERATOR retires it from the META working
  tree after the valid report exists.
- Preliminary plan verification (material anchors): S1 CMake shapes, S2 line
  anchors, S3 counts (48 `Q_PROPERTY`, 52 `Q_INVOKABLE`, 83 unique `app.*`,
  single `app` context property), S5 `remappingState` absence outside the
  header, S7 session mapping (22 live suspend, 23 LED/all-control, 24 bounded
  input-remapper) and the three source-gap items verified against the candidate.
  One material anchor defect found: S4 names `parseInventoryPayload`, which does
  not exist; the actual member is `ContextReceiver::onInventoryReport`
  (551-623). Candidate for the single targeted revision after the report is
  rendered; no decision taken yet.
- Next exchange: completion render, Worker session `01`, exchange `02`, prompt
  `01_completion_01.md`, report `01_report_01.md`.
- Active Worker: none before manual delivery. Active mutation: none.

## Completion reconciliation and planning decision — 2026-09-14

- Completion report `01_report_01.md` (Worker session `01`, exchange `02`,
  SHA-256 `4d4dc9d6ddaf7241e41786aa1c1412f8aea794b814c4c088e5228761dea0ecd6`)
  reconciled: valid terminal report (`### Report for ORCHESTRATOR_CHAT`,
  coordinates once, English, public-safe, no local paths), status `PASS`,
  phase-qualified result `not-applicable`; frozen artifact and completion prompt
  readbacks verified against own hashes (`454ed225...`, `7faae792...`); no
  product/AP/host/META Git mutation. Accepted as the exchange-01 planning-cycle
  terminal outcome rendered by exchange 02.
- Plan-content reconciliation against candidate `235d467c...`: material anchors
  verified (CMake shapes, Persistence line anchors, AppController counts, 83
  unique `app.*`, `remappingState`, S7 evidence, M2 session mapping 22/23/24).
  One specifically rejected assumption: `parseInventoryPayload` does not exist
  in `src/context/ContextReceiver.cpp`; the actual member is
  `ContextReceiver::onInventoryReport` (551-623).
- ORCHESTRATOR decision: exactly one targeted revision, basis
  `specifically-rejected-assumption`, changed boundary = the S4 ContextReceiver
  extraction target, all other frozen decisions preserved. Prompt
  `01_planning_02.md` (SHA-256
  `689ecf30c15dc770efdb7bac3b237b8273789b5bbbfb873f326214dfa29097d2`), Worker
  session `01`, exchange `03`, `current-worker-session`, Native planning mode
  required; report `01_report_02.md`; `Archival: wait-for-report`.
- The frozen artifact `01_report_00.md` remains superseded and uncommitted; it
  must never be committed because of its local path and is to be retired by the
  COOPERATOR once archival is settled.
- Next exchange: targeted revision, Worker session `01`, exchange `03`, prompt
  `01_planning_02.md`, report `01_report_02.md`.
- Active Worker: none before manual delivery. Active mutation: none.

## Revision reconciliation and plan acceptance — 2026-09-14

- Revision report `01_report_02.md` (Worker session `01`, exchange `03`,
  SHA-256 `9ada854757a91979e4afcac9ca211ee3e859d0ee57b20f2a1a3baab99e0ffc45`)
  reconciled: valid terminal report, status `PASS`, phase-qualified result
  `not-applicable`; prompt readback verified
  (`689ecf30c15dc770efdb7bac3b237b8273789b5bbbfb873f326214dfa29097d2`); no
  product/AP/host/META Git mutation. The corrected S4 boundary was verified
  against the candidate: pure parse = `ContextReceiver::onInventoryReport`
  lines 557-614; sequence/heartbeat (551-556) and apply/policy (616-621) stay
  in the receiver; the free function is introduced as
  `std::optional<QVector<InventoryEntry>> parseInventoryPayload(const QString
  &payloadJson)` with identical rejection log strings. The disclosed
  `decodeSnapshot` range limitation (real end 771, frozen range ended 773) is
  recorded and does not change the WorkspaceStateCodec decision.
- ORCHESTRATOR decision: the plan is ACCEPTED as `01_report_01.md` corrected by
  `01_report_02.md`. The planning budget is exhausted (initial cycle plus one
  targeted revision). No further planning cycle applies.
- Next exchange: implementation S1 (CMake unit-test helper), Worker session
  `01`, exchange `04`, `current-worker-session`, Native planning mode
  `not-used`; prompt `01_implementation_03.md` (SHA-256
  `8317314ec5c2e73e6ed2003b10977b9855a108688ed30d3a4eedba62c83c900a`), report
  `01_report_03.md`; one local product commit and one normal non-force push are
  authorized with subject `Add contextdeck_add_unit_test CMake helper`;
  `Archival: wait-for-report`.
- META archival proposal (COOPERATOR action, when convenient): archive the
  public-safe planning set `00_notes.md`, `01_planning_00.md`,
  `01_completion_01.md`, `01_report_01.md`, `01_planning_02.md`,
  `01_report_02.md`; do not commit `01_implementation_03.md` before
  `01_report_03.md` exists (prompt/report first-add pairing); never commit
  `01_report_00.md` (local path) and retire it after archival.
- Active Worker: none before manual delivery. Active mutation: none.

## S1 reconciliation — 2026-09-14

- Report `01_report_03.md` (Worker session `01`, exchange `04`, SHA-256
  `e3f6569efd6f0ab9191caa97b6f1e4a458e0cef94b4f9c60652c5da9dd7420c5`)
  reconciled: implementation-PASS. Independently verified by the ORCHESTRATOR
  against the public repository and the canonical checkout: direct public
  `main` = `5b2b25bc64c86f1ea568d82b94da2b3271b10c85`, subject
  `Add contextdeck_add_unit_test CMake helper`, parent `235d467...`, changed
  paths exactly `CMakeLists.txt` and `cmake/contextdeck-tests.cmake`; full
  registered suite 21/21 (69 s) from the exact candidate; helper content and
  all 21 registrations reviewed; no test source, product source, or
  documentation change.
- Worker near-miss carried into S2 as a client note: the Worker client injects
  bundled library paths that break distro cmake `CMAKE_ROOT`; resolved by a
  cleaned distro `PATH`; no product change.
- META privacy finding (discovered during this reconciliation): commit
  `0327a30` included the invalid, never-a-report artifact `01_report_00.md`,
  which contains a local machine path. It must not remain in the public live
  tree. Recommended correction (COOPERATOR-owned): one forward removal commit;
  history retains the bytes. A history rewrite is destructive, requires
  explicit authority, and is not recommended.
- Next exchange: implementation S2, Worker session `01`, exchange `05`,
  `current-worker-session`, Native planning mode `not-used`; prompt
  `01_implementation_04.md` (SHA-256
  `40d7ab2cbba94e06e886390d7e85580056a4202b1e0cbfe5126056e9c65fa393`), report
  `01_report_04.md`; one local product commit and one normal non-force push
  with subject `Split ProfileStore codecs into src/core/persistence`;
  `Archival: wait-for-report`.
- Active Worker: none before manual delivery. Active mutation: none.

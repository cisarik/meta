### Report for ORCHESTRATOR_CHAT

Logical whole identity: g213-contextdeck-workspace-session-manager
Worker session ordinal: 03
Worker exchange ordinal: 01

Persistent role identity: WORKER

```text
status: PARTIAL
Phase-qualified result: not-applicable
Result artifact or commit: c7c8eb90d31947bc32c498691ec926885f43cb64 (reviewed; not accepted)
Result evidence: independent read-only acceptance of the exact public candidate; A1–A6 and A8 PASS; A7 FAIL on one persistent regression required by the implementation prompt and absent from the candidate
Report justification: final-acceptance
```

Code acceptance of any kind is not live desktop or physical acceptance. This
review establishes nothing about M2/G4 closure, M3 closure, deployment,
production readiness, G3 re-audit, autostart, hibernate/hybrid sleep, general
input-remapper coexistence, M4 Slice B behavior, M5 behavior, per-key RGB, or
measured control-to-zone placement.

## Independence and session gate

- Genuinely fresh session: no implementation, planning, repair, or reporting
  ancestry for this logical whole; no M1/M2/M3 participation; the only inputs
  were the complete delivered prompt, the public repositories, and pinned AP.
- Native Plan Mode: not in use for this session and not used for any part of
  this review; no native plan approval was claimed as authority.
- Internal delegation / subagents: prohibited and not used. One accountable
  Worker produced this report.
- Coordinates used are exactly 03/01 as issued; the prompt's opening
  persistent-role and coordinate fields are echoed once above.
- All inspection used fresh disposable Worker-owned clones with build output
  outside the product checkout; no COOPERATOR checkout was used as evidence.

## Immutable identities and provenance

- Canonical product `https://github.com/cisarik/contextdesk`, branch `main`.
  Direct `git ls-remote` of public `main` = `HEAD` =
  `c7c8eb90d31947bc32c498691ec926885f43cb64`, equal to the required candidate
  and to the detached local HEAD.
- Required candidate parent verified: `502ae75571358ec95d33c836084b5e2253850731`.
  Candidate subject: `Implement M4 Slice A workspace assignment schema and
  dry-run`.
- AP gitlink and `.ap` checkout both `0cf2cff483a36a4cc2254aa424a7c53bd57a97e9`;
  `./.ap/ap doctor` = PASS, resolved variant `stable`.
- Canonical META `https://github.com/cisarik/meta.git`. Direct `git ls-remote`
  of public `main` = `640b65d785c4837f94f1547b76e32f84521fa5d1`, equal to the
  required baseline and to the detached local HEAD. META worktree clean.
- Implementation-pair commit `640b65d` has parent
  `c7e1b73757eaffe789796ad3faf2b4db45459c5f` and adds exactly two paths:
  `projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/02_implementation_00.md`
  and `.../02_report_00.md`.
- Byte integrity required and verified:
  - implementation prompt `02_implementation_00.md` SHA-256
    `b8fa2a274185c1bf784d444f50935fb82dd199e3b638ba7e3a0e736773469d38`;
  - implementation report `02_report_00.md` SHA-256
    `7570ee7999e684bb037fed63c7a2edc79f15fde1f2afe3a44ae1f2d69d7f8ce6`.
- Earlier M4 pair commits are add-only for their own pairs: `6f14316` adds
  `01_planning_00.md`+`01_report_00.md`; `c7e1b73` adds
  `01_completion_01.md`+`01_report_01.md`. No earlier accepted-plan or
  completion artifact was modified. The M4 trace directory and all parents are
  real directories, not symlinks.
- Product changed-path set is exactly the required 27 paths (sorted set
  comparison empty-diff), `git diff --check` clean, worktree clean before and
  after the external build. No `.ap`, `src/broker/`, broker IPC, `src/rgb/`,
  KWin bridge, `packaging/`, `SessionApplication.*`, `ContextReceiver.*`,
  `DBusNames.h`, `SettingsHost.*` (not required), license, hardware evidence,
  dependency/lockfile/toolchain, or host file changed.
- Trace-persistence deviation: `03_acceptance_00.md` is not present in the
  public META baseline, so byte-identity readback of the issued prompt against
  public META was not possible at acceptance time. This is consistent with the
  configured `wait-for-report` archival where the COOPERATOR first-adds the
  prompt/report pair only after the report exists. It is recorded here as a
  non-blocking trace observation for ORCHESTRATOR reconciliation, not as a
  candidate defect.

## A1–A8 acceptance matrix

### A1 — Identity, provenance, and scope: PASS

Direct public-ref equality, candidate parent, subject, AP pin plus
`ap doctor` PASS/`stable`, exact 27-path equality, clean worktrees, META
ancestry and pair integrity, and the absence of any scope escape (including
hidden dependency, broker, RGB transport, KWin bridge, packaging, session-app,
hardware-evidence, license, or host change) are all evidenced above. No host,
desktop, launch, OpenRGB, broker, device, or KWin operation was executed during
the review; receiver tests ran against a synthetic fake service on a private
bus. Blocking: no.

### A2 — Schema 4 and preserving migration: PASS

- `kSchemaVersion = 4` (`src/core/Types.h`).
- Schema-4 allowed root keys are exactly `schema_version`, `device`, `global`,
  `applications`, `preferences`, `workspace_sessions`
  (`src/core/Persistence.cpp` root allow-list); legacy schemas keep the
  baseline five-key root, two-key `preferences`, and five-key application
  sets.
- Schema 1–3 load in memory with `workspace_sessions` empty and no assignments;
  lighting, keys, matches, application order, and preferences are parsed by the
  unchanged legacy code paths. `validate()` additions are no-ops for legacy
  documents (empty workspace vectors, absent active session).
- No read-time rewrite or workspace activation: `load()` only reads;
  `schema3MigratesToSchema4WithoutWorkspaceAndKeepsBytes` and
  `schema4ReadDoesNotRewriteBytes` assert byte-identical files and no `.bak`,
  and confirm the new flags stay false after a legacy read.
- Future `schema_version` 5 and unknown semantic fields fail closed
  (`schema5IsRefused`, unknown-root/workspace/session-key tests).
- New preference flags default off; `active_workspace_session_id` stays
  optional and, when present, is cross-referenced to a defined session.
- `match.caption` is still rejected and captions never enter `MatchSpec`
  (`schema4RejectsCaptionAndUnknownWorkspaceKeys`; `MatchSpec` has no caption
  member). Blocking: no.

### A3 — Assignment schema validation and save safety: PASS

- Session ids: non-empty, unique, ≤128 UTF-8 bytes, control-free (parse and
  `validate()`, with a 128/129 boundary test). Session desktop lists are 1–32
  entries with 1-based contiguous ordinals; desktop names non-empty, ≤256
  bytes, control-free.
- `desktop_ordinal` is 1–32 at parse and ≤ the referenced session's desktop
  count in `validate()`; dangling session references and `active_workspace_session_id`
  dangling references are rejected.
- `launch_desktop_file` shape validated by the shared desktop-id predicate
  (`*.desktop` or reverse-DNS with a restricted character set; shell
  metacharacters rejected) and defaults at resolve time only from
  `match.desktop_file_name` when that field already looks like a desktop id,
  never from `resource_class`.
- Title `pattern` ≤128 UTF-8 bytes and control-free; `mode` ∈
  {`exact`, `contains`, `prefix`}. A missing per-application `workspace` object
  means no launch and no placement.
- Persistence: 1 MiB bound retained; atomic `QSaveFile`; bounded `.bak`;
  replacement refused for unsupported/invalid/migration-fallback existing
  bytes; explicit `Uložiť` remains the only schema-4 persistence boundary.
- Tests cover duplicate ids, non-contiguous ordinals, bad rows, empty desktop
  lists, unknown sessions, out-of-range ordinals, dangling active session,
  boundaries at 128/129 bytes, bad/shell/bare desktop-file values, and
  reverse-DNS acceptance.
- Non-blocking strictness nuance (ledger candidate): the desktop-id predicate
  returns true for any allowed-character string ending in `.desktop` before its
  reverse-DNS branch, so `.desktop` and `a..desktop` are admitted. No shell
  metacharacters are admitted, so this stays within the stated shape and is not
  an escape; a later strictness decision is optional. Blocking: no.

### A4 — Resolver: identity wins, opt-in non-logging title fallback: PASS

- The resolver diff is additive: `matchApplication`, `matchAgrees`,
  `matchRank`, `resolveAssignment`, `resolveContextLighting`, and both
  `resolveLighting` overloads are unchanged.
- `resolveWorkspaceAssignment` first uses the typed matcher; only when identity
  matching fails and both the global `title_fallback_enabled` and the
  profile's `title_fallback.enabled` are true is the user-authored pattern
  compared with the mode against the supplied caption in memory for that one
  call. An empty caption short-circuits; an empty pattern never matches.
- The caption is discarded after the call, never stored, never logged, and
  never enters `MatchSpec`; grep confirms the only occurrences of `caption` in
  `src/` are the resolver signatures/bodies, and there is no production caption
  producer in Slice A (no live call site), so no logging or persistence surface
  exists.
- Tests: identity beats fallback; both-flag gating; exact/contains/prefix
  modes; empty pattern; `MatchSpec` unchanged after a fallback match.
  Blocking: no.

### A5 — VirtualDesktopManager rows/wrapping receiver: PASS

- The receiver diff contains only: subscription/unsubscription of `rowsChanged`
  and `navigationWrappingAroundChanged` as invalidations; inclusion of the new
  fields in duplicate detection; and decoding of `rows` (integer 0–32, wrong
  types rejected) and `navigationWrappingAround` (strict boolean, wrong types
  rejected) from the same existing `GetAll` snapshot. Unknown map keys continue
  to be ignored.
- Request ownership, coalescing, one-in-flight, owner generation, stale-reply
  rejection, deadlines, recovery, and the single `GetAll` call are untouched
  (no diff hunks touch them). Logs expose only bounded error classes; no
  desktop identity is logged.
- Tests: `rowsAndWrappingAreDecoded`, `rowsChangedRequestsFreshSnapshot`,
  `navigationWrappingChangedRequestsFreshSnapshot`,
  `malformedWrappingBecomesUnknown`, `unknownSnapshotKeysAreIgnored`, with the
  pre-existing request-ownership tests still passing on the extended fake
  manager. Blocking: no.

### A6 — Controller and UI observational surface: PASS

- All new invokables mutate the in-memory document only and emit change
  signals; `save()` is unchanged and remains the only persistence boundary; no
  new call reaches OpenRGB, the broker, or the compositor.
- Observed state, named-session editor, per-profile assignment fields, and the
  dry-run preview are wired through new read-only properties; Apply is disabled
  (`workspaceApplyAvailable` returns false) with truthful later-grant copy.
- `workspaceSummary()` is unchanged and lighting-only. `diagnostics()` adds
  only booleans/integers/counts plus an error class; desktop names, UUIDs, and
  captions do not enter it. No new logging was added (all existing `qC*` sites
  predate the candidate). The user-authored title pattern is surfaced only to
  the editor that must edit it, not to diagnostics or logs.
- QML: one `Plochy` sidebar entry, a new `WorkspacePage.qml`, and assignment
  fields on `ApplicationsPage.qml`; QML ran through rcc/qmlcachegen in the
  external build (compile-time validity). No navigation redesign.
  `SessionApplication.*`, `SettingsHost.*`, and the KWin bridge are unchanged.
  Blocking: no.

### A7 — Causal regression evidence: FAIL

- Executed suites from the detached public candidate in the fresh external
  build directory: focused 5/5 PASS; complete registered CTest 18/18 PASS
  (counts from actual output, see Validation).
- Most required behaviors map to persistent causal regressions: schema-4
  round trip, schema 1–3 preserving migration without rewrite, `match.caption`
  rejection, unknown key rejection, pattern/id bounds, future-schema refusal,
  identity-wins, both-flag gating, empty pattern, `MatchSpec` stability, plan
  diff/drift/extra, already-running skip, missing desktop file and desktop-file
  defaulting, rows/wrapping change, debounce keys, trigger classification,
  receiver decode and both invalidations, malformed wrapping, unknown keys.
- Missing required persistent coverage: the implementation prompt (§7,
  "Required causal evidence includes") requires
  `title-fallback privacy: diagnostics maps omit pattern/caption keys`. No
  candidate test exercises diagnostics privacy or omission of any
  pattern/caption/desktop-name key. The only references to
  `diagnostics()` in tests are pre-existing `lightingUpdates`/`identityUpdates`
  assertions in `tests/unit/test_workspace_lighting.cpp`, a file outside the
  candidate diff that cannot exercise the new keys. The implementation report's
  coverage list omits this item, and its statement `Missing evidence: none
  required by this envelope` is therefore inaccurate.
- The accepted plan also listed this as a required new causal regression
  ("a small test that diagnostics maps omit pattern/caption keys"), so the gap
  is required by both the accepted plan and the implementation prompt.
- Consequence: a future change could place the pattern, a caption, or a
  desktop name into a diagnostics map without any test failing. No runtime
  failure exists today; the privacy property holds by static inspection. The
  gap is nonetheless an acceptance defect under the stated rules (missing
  persistent coverage required by the implementation prompt, even with a green
  suite). Blocking: yes.

### A8 — Documentation, ADRs, and bounded claims: PASS

- `docs/specification.md` documents schema 4, the exact field tables, strict
  validation, preserving schema 1–3 migration, the explicit save boundary, the
  assignment resolver and opt-in non-logging title fallback, and the Slice A
  observational boundary; it matches the implemented code.
- `docs/architecture.md` records the receiver extension, the pure
  `WorkspacePlan`, the M4/M5 boundary, and unchanged request ownership;
  `docs/operations.md` section 10 states the observational boundary and
  persistence/backup behavior; `docs/testing-m4.md` is a later numbered IRL
  checklist that explicitly grants no host mutation and defers live steps to
  Slice B.
- ADR 0002 (host mutation authority / no `kwinrulesrc`), ADR 0003 (schema 4),
  and ADR 0004 (typed in-session launch, non-autostart) match the accepted
  decisions, and `docs/adr/README.md` indexes them.
- The candidate is described only as an implementation candidate and is not
  claimed as accepted; M4 Slice B is not claimed as implemented or accepted.
  The exact M2 and M3 park wordings are preserved in `README.md` and
  `ROADMAP.md`; the duplicate M4/M5 rows are removed and the inaccurate
  "launch on session start" wording is corrected to in-session, explicit
  events only.
- No physical, deployment, production, autostart, M5, per-key, or whole-G4
  claim appears in the changed documents.
- Minor wording note (ledger candidate only): ADR 0002 and ADR 0004 carry
  `Status: accepted for the M4 tree` for the design decision while ADR 0003
  clarifies `Implementation-candidate; not accepted`; surrounding product docs
  describe the candidate as not accepted, so no acceptance claim exists.
  Blocking: no.

## Adversarial leads

### L1 — legacy-schema strictness versus migration compatibility: disproved

- Baseline behavior (candidate parent): `schema_version` was accepted only for
  1, 2, and 3. The candidate accepts 1–4 and still refuses values below 1 and
  above 4.
- For schemas 1–3 the candidate's allowed-key sets are byte-identical to the
  baseline at the root (five keys), `preferences` (two keys), and application
  profiles (five keys); the new `workspace_sessions`, `workspace`,
  `workspace_management_enabled`, `title_fallback_enabled`, and
  `active_workspace_session_id` keys are gated on `schemaVersion >= 4`. A
  legacy document containing those keys already failed as unknown fields at the
  baseline and still fails, unchanged.
- Lighting, chord/key, and match parsing code is unchanged, and the added
  `validate()` logic only examines workspace structures that are empty for
  legacy documents; therefore no previously valid schema-1/2/3 document can now
  fail or change semantics. The new preference defaults are false/absent and do
  not participate in ordinary lighting resolution, which is untouched.
- No read-time rewrite: tests assert byte-identical legacy files, unchanged
  lighting/keys, empty `workspace_sessions`, no assignments, and no `.bak`.
- Consequence: none. Blocks acceptance: no.

### L2 — scope and purity of the new launch-intent helpers: disproved

- `WorkspaceLaunchDebounce` and `workspaceEventIsLaunchTrigger` are declared and
  defined only in `src/workspace/WorkspacePlan.{h,cpp}`. The implementation is
  pure in-memory state (QHash counters and timestamps) plus a constant switch;
  there is no event loop, timer, D-Bus, KIO, `QProcess`, compositor, file, or
  network call, and the translation unit includes only the component header and
  `core/Resolver.h`.
- No production call site exists: grep across `src/` finds only the
  declarations/definitions; the controller uses only `computeWorkspacePlan`
  for the in-memory preview, which is itself pure and returns a value.
- The helpers exist to make the plan-required debounce and trigger evidence
  testable without a live producer, exactly as the implementation report's
  `MEASURED` note states; they do not introduce a trigger, launch, or mutation
  path and do not alter any semantic owner. The accepted contract required
  exactly this causal evidence (debounce keys; transaction triggers versus
  non-triggers), so they are inside the accepted Slice A scope.
- Consequence: none. Blocks acceptance: no.

## Validation evidence

Environment from the detached candidate with build products outside the product
checkout:

```text
cmake 4.4.3 / Ninja 1.13.2 / GCC 16.2.1 / dbus-run-session present
configure + build: 139/139 targets, no blocking warnings

focused:
ctest --test-dir <external-build> --output-on-failure \
  -R '^(test_profile_persistence|test_profile_resolver|test_workspace_receiver|test_workspace_plan|test_openrgb_protocol)$'
=> 100% tests passed out of 5; test_workspace_receiver 65.58 s; total 65.61 s

full:
ctest --test-dir <external-build> --output-on-failure
=> 100% tests passed out of 18; test_workspace_receiver 65.22 s; total 67.11 s

git diff --check 502ae75..c7c8eb9  => clean
git status --short                => clean
```

Private-bus classification: `test_workspace_receiver` and
`test_workspace_lighting` are registered under `dbus-run-session` with
`QT_QPA_PLATFORM=offscreen`; their fake `org.kde.KWin` service runs on a
private session bus and never touches real KWin. `test_workspace_plan` links
only `contextdeck_core` and `Qt6::Test` and is pure/bus-free. No OpenRGB
connection, device open, broker start/ARM/grab, session application, host or
desktop mutation, application launch, package install, or `kwinrulesrc` access
occurred.

First causal failure: none in executed validation. The blocking result is a
missing persistent regression (A7), not a runtime failure.

## Temporary probe

not-used. Both adversarial leads were settled by static analysis plus the
candidate's durable tests; no synthetic probe copy was created, and no
temporary product or META diff exists.

## Confirmed defects, missing persistent tests, disproved concerns

- Confirmed defect (blocking, A7): missing required persistent regression for
  diagnostics-map privacy (no test asserts that pattern/caption/desktop-name
  keys are omitted from `AppController::diagnostics()`), with a related
  inaccurate `Missing evidence: none required by this envelope` claim in the
  implementation report. The runtime property itself is believed correct by
  static inspection; the defect is the absent durable regression required by
  the implementation prompt.
- Missing persistent tests: exactly the above item; no other required
  regression from the implementation prompt was found absent.
- Disproved concerns: L1 (no legacy regression) and L2 (helpers pure,
  side-effect-free, in scope).

## Residual risks, deviations, and ledger candidates

- Residual risk: QML runtime behavior was validated only by build-time
  compilation because starting the session application is outside this
  authority; this matches the contract and is not claimed as runtime evidence.
- Deviation: issued prompt file absent from the public META baseline at review
  time (wait-for-report), so prompt byte readback was not possible; report
  readback is evidenced below.
- Out-of-scope ledger candidates (non-blocking, no acceptance impact): the
  `.desktop`-suffix branch of the desktop-id predicate accepting trivially
  short forms such as `.desktop`; the absence of a dedicated wrong-type `rows`
  rejection test (the malformed `navigationWrappingAround` test and static
  code cover wrong types); the ADR "accepted for the M4 tree" status phrasing;
  and the specification not spelling out whether `title_fallback.enabled` is
  itself optional (implementation requires it).

## Resolved Execution Issues / Near-Misses

One: an early parallel status check was invoked in the product workdir with
META-relative paths and failed with "No such file or directory" without any
state change; it was re-run in the correct workdir and all META evidence was
subsequently captured correctly. A pre-existing Worker-owned directory in the
shared temporary location was observed and deliberately left untouched; this
review used a newly created Worker-owned directory. No other near-miss
occurred.

## Pre-Existing Failure Classification

none. No registered test was failing at the candidate, and no test failed
during this review; no pre-existing failure required classification.

## META trace persistence and readback

- Report written once to
  `projects/contextdesk/00/04-g213-contextdeck-workspace-session-manager/03_report_00.md`
  (destination absent before this write; no collision, no overwrite) and read
  back completely: header, coordinates, status, and content verified; the
  destination remains the only file this exchange prepared.
- Issued prompt `03_acceptance_00.md` is absent from the public baseline (see
  deviation). No prompt bytes were rewritten, reconstructed, or replaced.
- META Git was not staged, committed, pushed, pulled, merged, rebased, or
  switched; no META path other than the report was touched. META Git
  publication of the exact prompt/report pair remains COOPERATOR-owned.

## Smallest next step

ORCHESTRATOR reconciliation of this PARTIAL review. If the ORCHESTRATOR decides
to close the gap, name one bounded correction slice adding the required
diagnostics-privacy regression (one focused test asserting that
`AppController::diagnostics()` contains no title-fallback pattern/caption or
desktop-name/UUID entries). Because the frozen Slice A allowlist contains no
AppController-capable test file, the correction must explicitly bind one exact
path — extending `tests/unit/test_workspace_lighting.cpp` or adding a dedicated
diagnostics test target — and then follow the appropriate scoped or full
re-acceptance decision. This next step is not granted by this report.

Orchestration critique:

MEASURED: The implementation prompt §7 requires causal evidence
`title-fallback privacy: diagnostics maps omit pattern/caption keys`; the
candidate contains no such regression (grep across `tests/`), and the
implementation report both omits it from its coverage list and states
`Missing evidence: none required by this envelope`; effect is an A7
coverage gap that prohibits acceptance-PASS under the stated rules; smallest
correction is the single bounded test addition named above.

LEAD: The frozen Slice A allowlist cannot host that test without a new or
extended path, suggesting the implementation contract was internally
inconsistent rather than carelessly applied; the cheapest useful check for the
ORCHESTRATOR is to decide the exact one-path binding (existing
AppController-linked test vs. a small dedicated diagnostics target) before
issuing any correction grant.

Explicit non-claims: no acceptance-PASS, implementation-PASS at this phase,
publication-PASS, deployment-PASS, production acceptance, physical acceptance,
whole-M2/G4 closure, independent G3 re-audit, autostart, hibernate/hybrid
sleep, general input-remapper coexistence, M3 closure, M3 physical five-zone
observation, live desktop/launch/placement behavior, remapping, deck behavior,
M5 integration, per-key RGB, or measured control-to-zone placement. Session 27
is not claimed to have been an independent Worker result. This review demanded
no live input, device, or desktop operation and performed none.

Logical-whole closure: not-closed

Authority for this Worker expires at this terminal report.

# Era 00 Whole Notes — Kronika one product

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Non-authorizing. Public-safe by default. Michal owns any meta Git
commit.

Working identity (Orchestrator-proposed 2026-09-23, pending Cooperator
confirmation):

```text
kronika-one-product
```

Trace:

```text
/home/agile/meta/projects/kronika/00/02-kronika-one-product/
```

Opening: no opening handout. This whole opens from the Cooperator's
2026-09-23 direction "Jedna Kronika na základe existujúceho FrameNestu",
stored byte-identical here as `01_plan_sk.md` (SHA-256
`e10635dd9dcfc5ef3b73edb21fe48499159230ba1492271e3c0d073f27a81c91`). The
original copy remains in the superseded predecessor's trace directory.

Predecessor whole: `kronika-tailnet-family-library` (superseded 2026-09-23;
not closed; no implementation occurred; its Planner grant was never
dispatched; no closure signal emitted). Its premise — two separate products,
FrameNest parked and untouched, product work in the `cli_chatgpt` checkout —
is replaced.

## Objective

One Kronika built on the existing FrameNest product. FrameNest's frontend,
catalog, media, permissions, and deployment remain the application base; the
closed `cli_chatgpt`/Kronika capture code supplies the ChatGPT capture module.
No new repository. Near-term: a capture service on the home NUC with one
persistent owned browser and admin-handled challenges. Broader: a
family-reachable timeline library over Tailscale with explicit private/family
sharing.

## Locked Cooperator decisions (2026-09-23 direction)

- One product; the existing FrameNest repository becomes Kronika; no new
  repository.
- Timeline is the main page; FrameNest design and Gallery are kept.
- Media appears on the timeline only after a successful validated analysis.
- New record kinds: Search and Research.
- Every new record starts private; family sharing is explicit.
- Old databases of both projects hold unwanted test data; no import is
  implemented.
- Personal photos and their future local AI analysis are out of this stage.
- The NUC stays the development/test machine.
- Capture package `kronika_capture`, command `kronika-capture`; internal
  `framenest` package, migration history, compatible HTTP headers, and deploy
  identifiers are kept for now; no mass rename.
- Existing `deploy/ubuntu/framenest-release` is extended; no second deploy
  system.
- Capture move: `vendor/kronika-ask/src/kronika/**` to
  `src/kronika_capture/**`, then remove the replaced vendor copy; port only
  missing capture features (Search/Research, export/sanitization helpers) from
  clean Kronika at `66c40d43`; provenance manifest for each taken file.
- One persistent Chromium on Xvfb; no per-task launch; no stealth, model, or
  reasoning switching; no automatic restart loop; manual restarts at least
  five minutes apart; admin intervention via `needs_admin`, loopback-only
  on-demand VNC view, explicit resume, no automatic re-send.
- Bridge extended in place (no parallel job system); one bounded ZIP
  attachment (at most 32 MiB, 256 JPEG frames, 128 KiB/frame, long side
  480 px, `ZIP_STORED` only); private staging; typed errors; idempotent
  `request_id`; journal 24 h / 256 records; one active job including paused.
- Unified private-by-default records in the existing FrameNest database;
  server-derived owner; family sharing mapped explicitly, never public
  publication; permissions enforced on every access path.
- Database reset is a separate operation after stopping writers; exact DB
  files only; no deletion of media, profiles, identity config, secrets, or
  archives; new DB via normal schema/migration.
- Final public renaming only after transfer and acceptance: today's
  `cisarik/kronika` to `kronika-capture-archive`; FrameNest to `kronika`;
  update deployment source URLs and local remotes; no history rewrite.
- First implementation grant will be S0 (record and align the new architecture
  in the existing FrameNest); first executable-code change is S1 (capture
  module move and duplicate removal). One Worker grant executes one row.
- Python verification follows FrameNest's baseline-bound route
  (`./.ap/ap project check`, `./.ap/ap exec`); JavaScript tests use the
  existing `node --test`. No new test toolchain.

## Restored state (read-only, 2026-09-23)

FrameNest checkout (product base):

```text
root          /home/agile/Projects/framenest
branch        feat/chatgpt-page-ask-kernel
HEAD          26d28b16c08a5e7e0179a32c16646bfdc1009c81
parent        0fd21b989814b7c0b78d517996812750a823ff10
tree          f554863f18238e04203e4f22d5e20770e180045d
subject       feat: add chatgpt-page probe tooling and budget contract
main          = origin/main = 26d28b16
worktree      clean
remote        origin = https://github.com/cisarik/framenest.git
AP pin        7478ddb07d2c3911f79e1aa1441f0115a31c45d8 (gitlink and .ap HEAD)
vendor        vendor/kronika-ask present; upstream 66c40d43 / tree 848f2474
release       deploy/ubuntu/framenest-release present
absent        src/kronika_capture
AP ledger     docs/AP_UPGRADE_OBSERVATIONS.md declared
private       private/ holds key material; never read by Workers
```

Kronika source checkout (read-only source for the port):

```text
root          /home/agile/Tools/cli_chatgpt
branch        main; HEAD = main = public/kronika-initial = 66c40d43
worktree      clean
AP pin        7478ddb07d2c3911f79e1aa1441f0115a31c45d8
public        cisarik/kronika refs/heads/main = 66c40d43
```

NUC host facts remain claims from the FrameNest trace and the predecessor
handout; a later read-only preflight re-verifies them before any host mutation.

## Open gates

- First Worker is the Planner (session 01, native planning mode required,
  fresh session, manual dispatch).
- The Cooperator direction is accepted and locked; the Planner grounds it and
  must not reopen it.
- No host mutation, no database reset, no GitHub rename, no push, no real
  ChatGPT task without a later explicit bounded grant.
- AP pin 7478ddb0 governs each repository; do not upgrade.

## Session log

- **2026-09-23 — Whole opened.** Cooperator supplied the materially changed
  objective and direction (`01_plan_sk.md`, stored here byte-identical).
  Predecessor `kronika-tailnet-family-library` superseded without
  implementation and without the closure signal; its Planner grant was never
  dispatched. Read-only verification of both checkouts and public refs passed
  (FrameNest `26d28b16` clean, main = origin/main; Kronika `66c40d43` clean;
  both AP pins `7478ddb0`). No mutation. Issued the Planner grant
  `01_planning_00.md` (session 01 / exchange 01, fresh-worker-session,
  Planner, native planning mode required, manual Cooperator delivery, Extra
  High, no Max), SHA-256
  `831dee2b31352bab8a050add5b783b01b0674eaba25d79bdedf57ee9b00828e5`.
  Next: Cooperator opens a fresh Agent chat with native Plan Mode ON and
  pastes the prompt; the report destination `01_report_00.md` is absent.

- **2026-09-23 — Planner report reconciled and accepted; S0 grant issued.**
  Planner report `01_report_00.md` (SHA-256
  `5bca858d3a65d1cb74fbd263db57a89878da2bb1b79ae578828e5025f4f182a2`,
  1073 lines, status PASS, coordinates `kronika-one-product` / 01 / 01)
  reconciled against both repositories: both checkouts still clean at
  `26d28b16` and `66c40d43`; all named paths exist except the planned new ADR
  `docs/adr/0082-kronika-one-product-and-private-records.md`; latest catalog
  revision is `0033_media_analysis_proposals.py`; the vendor relocation map
  covers all 32 files under `vendor/kronika-ask/src/kronika/**`;
  `pyproject.toml` carries `framenest-chatgpt-page = "kronika.cli:main"` and
  the vendor package/asset includes. Orchestrator acceptance: plan accepted;
  no locked decision reopened; no unresolved product decision blocks S0.
  Delivery deviation recorded: the original Meta-file delivery requirement was
  replaced by an explicit Cooperator session-delivery instruction; the report
  was stored at the exact destination by the Cooperator, not the Worker
  ("Meta changes: none"). Non-material format omissions (session target,
  native mode, profile, header start/end commits) noted; start/end commits are
  present in the closure evidence.

- **2026-09-23 — S0 implementation grant issued.**
  `01_implementation_01.md` (session 01 / exchange 02,
  current-worker-session, Implementation Worker, native planning mode
  not-used, manual Cooperator delivery, Medium), SHA-256
  `61f8386ddb3aaeb89c84dfb5deff30bbfafeb851d2f75d232e09576c482a51f3`.
  Scope: create `feat/kronika-one-product` from `26d28b16`, one documentation
  commit on the exact S0 allowlist, `./.ap/ap project check` gate, no tests,
  no push. Report destination `01_report_01.md` (absent).

- **2026-09-23 — S0 accepted; S1 grant issued.** S0 report `01_report_01.md`
  (SHA-256 `aba700c3bac8b55260cb1c2851644f52f0624869ca05f64a7c700affc000f5b0`,
  status PASS, implementation-PASS, coordinates 01/02) reconciled: branch
  `feat/kronika-one-product` has exactly one commit
  `93e7742d56d46d4725d4561bd8751b15e55e5eb5` (parent `26d28b16`, tree
  `b357c765f8ca03c03cbbe0b087b98b6aa14a75e9`, subject
  `docs(kronika): record one-product architecture and private records`);
  `git diff --name-status` is exactly the eleven allowed paths (ten modified
  plus ADR-0082 added); worktree clean; managed AP block byte-identical; AP
  pin `7478ddb0` unchanged; `main`/`origin/main` unmoved at `26d28b16`; no
  remote branch pushed. ADR-0082 and the AGENTS.md additions reviewed; content
  matches the locked direction and marks S0 as documentation-only. S0 accepted
  (Orchestrator review; Cooperator confirmed the direction by continuing).

- **2026-09-23 — S1 implementation grant issued.**
  `01_implementation_02.md` (session 01 / exchange 03,
  current-worker-session, Implementation Worker, native planning mode
  not-used, manual Cooperator delivery, High — packaging/resource named
  risk), SHA-256
  `263b9f17ee42cd168d7921a2fd2cf0e93a4a232809fc2ce9401999653ac34d42`.
  Scope: relocate the 32 vendor files to `src/kronika_capture`, update
  imports/resource lookup/packaging/entry points/tests, add
  `docs/provenance/kronika-capture.json`, retire `vendor/kronika-ask/**` after
  verification, one commit, no push. Report destination `01_report_02.md`
  (absent).

- **2026-09-23 — S1 accepted; S2 grant issued.** S1 report `01_report_02.md`
  (SHA-256 `25af6bd7dc5d4065b6149509bc779f17e66faac6130feb095732d44683fbd5c9`,
  status PASS, implementation-PASS, coordinates 01/03) reconciled: branch
  `feat/kronika-one-product` has exactly one new commit
  `96ef426f7026c818f5e75733e8f8dfc5ac2321d1` (parent `93e7742`, tree
  `570e99abb77b062b7a3ac3c6f7f9f0be5d74dda3`, subject
  `feat(capture): relocate kernel into kronika_capture`); the rename-aware diff
  is 32 relocations `vendor/kronika-ask/src/kronika` -> `src/kronika_capture`,
  plus `pyproject.toml`, 12 test files, new
  `docs/provenance/kronika-capture.json`, deleted vendor manifest and the two
  vendor-path scaffolding files; `vendor/` holds no tracked file;
  `src/kronika_capture` has 32 files; both entry points resolve to
  `kronika_capture.cli:main`; no old-namespace or code-level vendor reference
  remains; worktree clean; AP pin unchanged; `main`/`origin/main` unmoved at
  `26d28b16`; no push. Focused-route claims (32 Python tests, 3 Node tests,
  wheel inventory including the isolated wheel import) are Worker evidence, not
  independently re-run; S1 acceptance is E2 non-independent per the plan.
  S1 accepted; evidence before S2 satisfied (one executable implementation,
  complete provenance, focused results).

- **2026-09-23 — S2 implementation grant issued.**
  `01_implementation_03.md` (session 01 / exchange 04,
  current-worker-session, Implementation Worker, native planning mode
  not-used, manual Cooperator delivery, High — submission-barrier named
  risk), SHA-256
  `de6874cd08e9210cfed62b8c672fc2c200c187f7eb84e6ac0d7f9ad1fc883ae8`.
  Scope: durable journal behind `JobManager`, submission barrier
  (`send_intent_persisted` before any click), removal of the second-click
  retry, bridge-restart reconnection without browser shutdown, persistent
  single browser with the 300 s restart brake, `needs_admin`/resume/readiness,
  status and cancel endpoints, idempotent `request_id`, 24 h/256 journal
  bounds, typed errors; one commit, no push. Evidence before S3: a separate
  fresh independent targeted review (session 02) proving single launch,
  reconnect, pause/resume, timer separation and no automatic resend. Report
  destination `01_report_03.md` (absent).

- **2026-09-24 — S2 implementation report reconciled; S2 acceptance grant
  issued.** S2 report `01_report_03.md` (SHA-256
  `f2cc872d8d56357162212441ff0871469bdb44fcc568754ec207aabcfad9b9fb`, status
  PASS, implementation-PASS, coordinates 01/04) reconciled: commit
  `5259b89a9af993e94f00c03e7962681c8ba152a4` (parent `96ef426`, tree
  `97fac132581632305d4e86fdbdeca11118b83e75`, subject
  `feat(capture): persist submission barriers and browser lifecycle`); diff is
  exactly the 20 allowed paths (17 modified, 3 added: `bridge/journal.py`,
  `tests/capture_lifecycle.test.js`,
  `tests/unit/chatgpt_page/test_capture_journal.py`); the journal uses stdlib
  SQLite with 0700/0600 and `synchronous=FULL`; the packaging test now expects
  33 capture files while provenance stays exactly 32 upstream-relocated files;
  protected paths and AP pin unchanged; worktree clean; `main`/`origin/main`
  unmoved at `26d28b16`; no push. Focused-route claims (62 Python, 28 Node) are
  Worker evidence; the plan requires a fresh independent review before S2
  acceptance, so no acceptance verdict is recorded yet.

- **2026-09-24 — S2 acceptance grant issued.** `02_acceptance_00.md` (session
  02 / exchange 01, fresh-worker-session, Fresh Independent Audit, phase
  acceptance, native planning mode not-used, manual Cooperator delivery, High,
  required-fresh-independent), SHA-256
  `e27ff9d9a3cd34fdb561f4e93a406674bdb18b4cf34f34d508ebbb3b5093561e`.
  Candidate `5259b89a…`; eight fixed risk claims; fixed positive/negative
  control matrix including adversarial double-send, journal, wire-auth,
  privacy and launch-brake probes under one declared temporary root. Report
  destination `02_report_00.md` (absent). Next: Cooperator opens a NEW Agent
  chat (fresh session 02) and pastes the prompt.

- **2026-09-24 — S2 acceptance PARTIAL reconciled; bounded correction
  issued.** Fresh independent acceptance `02_report_00.md` (SHA-256
  `fe10986fa2f1884305f49816fc46adcdcb0bfc085e8d7141215c653b6f0a9f1d`,
  37435 bytes, session 02 exchange 01) accepted the candidate `5259b89a…`
  only in part: prescribed runs passed independently (62 Python / 28 Node);
  claims 1 (browser lifecycle), 2 (no automatic resend), 3 (journal), 6 (no
  profile access) and 8 (packaging/protected paths) PASS; claim 4 FAIL (F01
  queued administrator wait consumes the active deadline), claim 7 FAIL (F02
  oversized result receives untyped 413/E_INTERNAL and is retried), claim 5
  PARTIAL (F03 present empty `Origin` treated as absent; inherited, low). No
  second Send click and no token bypass was demonstrated. The audit did not
  modify the candidate: HEAD `5259b89`, clean, AP pin `7478ddb0`,
  `main`/`origin/main` `26d28b16`, no push. Acceptance budget: one primary
  fresh acceptance used; one correction and one re-acceptance remain.

- **2026-09-24 — S2 bounded correction grant issued.** `01_correction_04.md`
  (session 01 / exchange 05, current-worker-session, Bounded Correction
  Worker, phase correction, native planning mode not-used, manual Cooperator
  delivery, High), SHA-256
  `6ede8c1adb542eb2f0c9cce646bc201cda17e08acc6e1b44f6233d3be77a9bef`.
  Scope: F01 queued administrator intervention accounting (durable
  accounting, retained slot, excluded wait, explicit resume, exact 1800 s
  expiry); F02 oversized-result typed `E_RESULT_TOO_LARGE` terminal failure
  with no re-execution or unbounded retry, readable via authenticated status;
  F03 reject a present empty `Origin`; vocabulary reconciliation
  (`E_RESULT_TOO_LARGE` now; `E_ATTACHMENT_INVALID` deferred to S5;
  `E_RESULT_EXPIRED` deferred to the application-recovery slice). One commit,
  no push, no self-certification. After the correction a full fresh
  re-acceptance (session 03) is required. Report destination `01_report_04.md`
  (absent).

- **2026-09-24 — S2 correction reconciled; full fresh re-acceptance issued.**
  Correction report `01_report_04.md` (SHA-256
  `7615023baf66130e0500dde393da5964b83d677733a04a9794318f1c1fd18be5`, status
  PASS, implementation-PASS, coordinates 01/05) reconciled: commit
  `82a6a59803ed8830c19e51cd8f9bc1665c28a975` (parent `5259b89`, tree
  `190338dde238c414cf4e80999b29b18797d4f72d`, subject
  `fix(capture): correct queued waits and oversized result delivery`); diff is
  exactly the 12 allowed paths (11 modified, 1 added `test_result_limits.py`);
  `auth.py` now rejects any present non-matching Origin including empty;
  `E_RESULT_TOO_LARGE` present in `errors.py` and `protocol.js`; protected
  paths and AP pin unchanged; worktree clean; `main`/`origin/main` unmoved;
  no push. Route claims (82 Python, 31 Node) are Worker evidence, not
  independently re-run.

- **2026-09-24 — S2 full fresh re-acceptance grant issued.**
  `03_acceptance_00.md` (session 03 / exchange 01, fresh-worker-session, Fresh
  Independent Re-Audit, phase acceptance, native planning mode not-used,
  manual Cooperator delivery, High, required-fresh-independent), SHA-256
  `1e708018cb4f0c2197b9fed8925ce361608cba1cac62cb59d92fe96b25cc51d3`.
  Candidate `82a6a598…`; all eight original claims plus explicit F01/F02/F03
  closure with independent reproduction; recorded vocabulary scope;
  adversarial controls under one declared temporary root. Acceptance and
  Correction Record: `Primary fresh acceptances used: 1`, `Automatic
  corrections used: 1`, `Correction re-acceptance: full-fresh`. Report
  destination `03_report_00.md` (absent). Next: Cooperator opens a NEW Agent
  chat (fresh session 03) and pastes the prompt.

- **2026-09-24 — S2 re-acceptance PASS; S2 accepted.** Re-acceptance
  `03_report_00.md` (SHA-256
  `74d1754c1f200ea2ad87109990badc786a3335d3340c0976121e1398c97b5d45`, status
  PASS, acceptance-PASS, coordinates 03/01) independently established all
  eight claims on candidate `82a6a598…` and verified F01/F02/F03
  `verified-closed` with real loopback reproductions; no new finding and no
  mutation of the candidate. Orchestrator acceptance: S2 accepted
  (`acceptance-PASS`); acceptance budget exhausted (one primary fresh
  acceptance plus one full-fresh correction re-acceptance). Next surface: S3
  NUC capture foundation.

- **2026-09-24 — S3 repository implementation grant issued.**
  `04_implementation_00.md` (session 04 / exchange 01, fresh-worker-session,
  Fresh Implementation Worker, native planning mode not-used, manual
  Cooperator delivery, High), SHA-256
  `e6dfccbfa5b8671ca4306c6e0fa2adc2e9e90408a0dc555f484553bed623ad59`.
  Scope: five capture systemd unit sources plus non-secret env template,
  bounded systemd-credential token integration (auth/CLI/config/paths only,
  S2 semantics unchanged), release-helper capture-runtime identity and an
  explicit capture activation (drain/refuse, restart brake, `capture-current`
  switch, one planned restart, readiness verification, dual-pointer
  reporting), deployment docs and contract tests; one commit, no push. The
  read-only NUC preflight and bounded host setup/deployment grants remain
  separate later steps. Report destination `04_report_00.md` (absent).

- **2026-09-24 — S3 repository report reconciled and accepted; preflight
  issued.** S3 report `04_report_00.md` (SHA-256
  `fee30acad1184fce1716083b3ef227b252670a24b8f7a8253fbb4cda16185412`, status
  PASS, coordinates 04/01) reconciled: commit
  `c975aba14840b97944aecc655907e3abc370341d` (parent `82a6a59`, tree
  `a80ab53cf5ee19ffe0af46de4e015519cd97d941`, subject
  `feat(capture): supervise capture separately from web deploys`); diff is
  exactly the 20 allowed paths (8 added: five units, env template, two test
  files; 12 modified); units use `LoadCredential` for the bridge/runner, no
  `PartOf=framenest.service`, no auto-restart for Xvfb/runner, loopback-only
  view on 5900/6080 with 1800 s limits; the helper adds capture manifest
  identity plus `activate-capture`/`rollback-capture` with drain/refuse, brake
  and one planned restart; credential integration falls back safely; protected
  paths and AP pin unchanged; clean; `main`/`origin/main` unmoved; no push.
  Route claims (195 focused tests) are Worker evidence. Orchestrator
  acceptance: S3 repository implementation accepted (non-independent).
  Recorded MEASURED critique reconciled: the `framenest.service` credential
  drop-in is not in the repo slice; it is a host-side installation step,
  documented in the repo, to be performed by the host setup grant after the
  token exists, and the web application consumes it only at S7. This is a
  carry-forward binding for the host setup and S7 grants, not a blocker.

- **2026-09-24 — S3 read-only NUC preflight grant issued.**
  `05_preflight_00.md` (session 05 / exchange 01, fresh-worker-session,
  Worker-Executed Preflight, phase preflight, native planning mode not-used,
  manual Cooperator delivery, High), SHA-256
  `1bfd7277cad6e648a1d4e3cc118593375eabc731b8896ab754832455d111ae56`.
  Read-only host verification: gate/privilege, exact binary paths and versions,
  ports 8765/5900/6080, accounts and capture paths, web release state and
  installed unit source, systemd credential capability, AppArmor/userns,
  display tooling, capacity, noVNC, terminal `sudo -K`. No mutation; PASS only
  recommends a later bounded setup grant. Report destination `05_report_00.md`
  (absent). Cooperator preconditions: export `FRAMENEST_NUC_SSH_*` and
  establish the remote sudo timestamp outside the Worker.

- **2026-09-24 — Preflight BLOCKED at the transport precondition; renewed
  preflight issued.** `05_report_00.md` (SHA-256
  `944dd335e691002674aabe0c91d111efcbcb1fc3addf72ea78301de5b191bd87`, session
  05 exchange 01) stopped BLOCKED before any remote command: the three
  `FRAMENEST_NUC_SSH_*` names were unset in the Worker environment (name-only
  scan of 149 readable process environments, 0 set), while the local gate
  probe printed `ssh-agent: ready`. No host path was read; no mutation; no
  unit installed; sudo was never entered or released. Orchestrator
  reconciliation: environment/routing precondition failure, not a host defect;
  checks 2–12 remain unknown.

- **2026-09-24 — Renewed read-only NUC preflight grant issued.**
  `06_preflight_00.md` (session 06 / exchange 01, fresh-worker-session,
  Worker-Executed Preflight, phase preflight, native planning mode not-used,
  manual Cooperator delivery, High), SHA-256
  `e361aeb1c4495325409151856275fba9eebba38dd73b2b420c69bac373184de0`.
  Same read-only checks as `05_preflight_00.md` with a front-loaded Step 0
  name-only environment check that stops BLOCKED immediately if any
  `FRAMENEST_NUC_SSH_*` name is unset. Report destination `06_report_00.md`
  (absent). Cooperator action before dispatch: export the three names into the
  environment that launches the Agent, establish the remote sudo timestamp
  outside the Worker, verify with a names-only count, then open a new chat.

- **2026-09-24 — Second preflight BLOCKED (same blocker); corrected-launch
  preflight issued.** `06_report_00.md` (SHA-256
  `d7248c824cdc8b0cfe39405345352fc7dd54ee1141ecaebb99bf03fe99788e13`, session
  06 exchange 01) stopped BLOCKED at Step 0: the three `FRAMENEST_NUC_SSH_*`
  names were again unset in the Worker process; no gate or remote command ran;
  no mutation; no sudo entered or released. This is the second consecutive
  terminal BLOCKED for the same materially unchanged transport blocker; a
  third equivalent cycle is prohibited unless the launch environment changes.
  The Cooperator then supplied the exact launch-environment setup commands for
  the three names (values deliberately not recorded anywhere in this trace).
  Orchestrator decision: the environment change justifies exactly one further
  read-only preflight; if Step 0 still fails, the route switches to
  Orchestrator-led Cooperator execution.

- **2026-09-24 — Corrected-launch preflight grant issued.**
  `07_preflight_00.md` (session 07 / exchange 01, fresh-worker-session,
  Worker-Executed Preflight, phase preflight, native planning mode not-used,
  manual Cooperator delivery, High), SHA-256
  `d0261304d0587879526cf4dd09815e0293629cdd4000d36ac2f43f2fcc5e3599`.
  Same read-only checks with the Step 0 name-only gate; the transport values
  remain unrecorded in every artifact. Report destination `07_report_00.md`
  (absent).

- **2026-09-24 — Client routing question recorded.** The Cooperator asked
  whether the preflight Worker can run in Cursor IDE. Confirmed: Cursor is a
  valid fresh Worker-session client; AP is client-neutral and the grant does
  not name a client. Routing fields, prompt, report destination and Step 0
  remain unchanged. Cursor's process environment must carry the three
  `FRAMENEST_NUC_SSH_*` names (launch Cursor from the configured shell and
  verify names-only before dispatch). The FrameNest project's Cursor Worker
  Execution Boundary continues to apply: `.ap/ap` routes for Python evidence,
  the worker gate as the sole NUC SSH route, no socket printing, and the
  Cooperator-owned sudo lifecycle.

- **2026-09-24 — Launch-environment propagation finding.** The Cooperator
  reports Cursor is launched from the UI and a per-terminal `set -gx` does not
  propagate to other terminals or to the Cursor agent process. Consequence:
  the Worker route cannot work until the Worker client inherits the three
  names. Orchestrator guidance: fully quit Cursor and launch it from the
  configured terminal, then verify names-only in the new session before
  dispatch; if relaunching is unwanted, the alternative is a Cooperator-owned
  local env file (0600, outside the repository) with the three bash exports,
  which a later grant revision would source at Step 0. No values recorded.

- **2026-09-24 — Third preflight BLOCKED; Worker route for host access
  closed.** `07_report_00.md` (SHA-256
  `f4035e60df11fd2d1959de5c8edbc3eaad65d3cfbd21acf4e69e6895b1dc007e`, session
  07 exchange 01) stopped BLOCKED at Step 0: the three transport names were
  again unset in the Worker process after the claimed launch-environment
  change. This is the third consecutive terminal BLOCKED for the same
  materially unchanged blocker; a fourth equivalent Worker cycle is
  prohibited. No host contact, no mutation, no sudo entered or released.
  Orchestrator decision: the read-only preflight switches to Orchestrator-led
  Cooperator execution in the Cooperator's own interactive NUC session (no
  gate transport, no Agent environment); the Cooperator establishes `sudo -v`
  before the block and releases with `sudo -K` at its end; the Orchestrator
  classifies the returned output. The Worker-transport requirement (or an
  owner-executed equivalent) remains a precondition for the later bounded host
  setup/deployment grant.

- **2026-09-24 — Owner-executed read-only preflight: PASS (classified by
  ORCHESTRATOR from the Cooperator-returned complete output).** Sanitized
  observed facts: Ubuntu 24.04.4 LTS, x86_64; systemd 255
  (255.4-1ubuntu8.17; `LoadCredential` supported); `framenest` uid 999 present;
  `kronika-capture` absent (expected, created by the setup grant); all capture
  paths absent (`/var/lib/kronika-capture`, `/run/kronika-capture`,
  `/etc/kronika-capture`, credentials dir, `/opt/framenest/capture-current`);
  `/tmp/.X11-unix` root:root 1777 and no `:99` lock; web release
  `/opt/framenest/releases/26d28b16…` active, unit carries one existing
  credential line from an AI drop-in; `.framenest-release-sha` unreadable as
  operator (verify as root later); binaries present and executable: Xvfb,
  x11vnc 0.9.16, websockify, `/usr/bin/chromium` → Chrome for Testing
  154.0.8037.57, `/usr/bin/install`, xauth 1.1.2, mcookie 2.39.3, node
  v22.23.2; ports 8765/5900/6080 free; no Xvfb/chromium/chrome/x11vnc/
  websockify/node processes; unprivileged-userns restriction value `1` with
  the existing AppArmor userns profile present; about 200 GB free on both
  relevant filesystems; sudo released (`sudo -n true` → password required).
  Minor notes: Xvfb and websockify version flags not exposed; the
  `framenest.service` capture-token drop-in remains the documented host-side
  addition. Verdict: preflight PASS; no host blocker for a bounded setup/
  deployment grant.

- **2026-09-24 — S3 fresh targeted review grant issued.**
  `08_acceptance_00.md` (session 08 / exchange 01, fresh-worker-session, Fresh
  Independent Audit, phase acceptance, native planning mode not-used, manual
  Cooperator delivery, High, required-fresh-independent), SHA-256
  `e61a3f2b8f9ea7fe9d1be62eb6c21f5588384bc76213f3efcd34d96559fc9f1f`.
  Candidate `c975aba14840b97944aecc655907e3abc370341d`; fixed
  claims cover unit directives, credential boundary, release helper capture
  transition, docs/tests and the classified preflight facts; no NUC contact.
  Report destination `08_report_00.md` (absent). Publication and the bounded
  host setup/deployment grant follow only after a PASS.

- **2026-09-24 — S3 acceptance PASS; publication grant issued.** S3 acceptance
  `08_report_00.md` (SHA-256
  `e1970ed59a137c3211b2ecaa158c8095938038fdb467b5e3d318daf04f04ffdd`, status
  PASS, acceptance-PASS, session 08 exchange 01) independently established all
  six fixed claims on candidate `c975aba…`; no blocking finding; the declared
  route ran 195 passed. Orchestrator acceptance: S3 repository slice and
  deployment/credential boundary accepted. Ledger candidates recorded: the
  `framenest.service` capture-token drop-in remains a host-side addition for
  the setup grant (the web consumes it at S7); a symlinked credential file is
  ignored while a symlinked credentials directory is followed when the final
  file is regular; a dangling journal symlink classifies as absent;
  `retained_release_paths` is not called by deploy/rollback; VNC `-nopw` with
  `-localhost` matches the design; `mcookie` may appear in the Xvfb argv (not
  the bridge token). Transport note: the Cooperator fixed the Worker
  environment by placing the three `FRAMENEST_NUC_SSH_*` names in `~/.zshenv`
  (values not recorded here); host-access Worker grants are unblocked for the
  setup step.

- **2026-09-24 — S3 milestone publication grant issued.**
  `09_publication_00.md` (session 09 / exchange 01, fresh-worker-session,
  Bounded Publication Worker, phase publication, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `3187d5fb550dc0ea855cb5d7104b9f8a53746959c755bc25de621cfd0e185a2b`.
  Exact authority: publish accepted `c975aba14840b97944aecc655907e3abc370341d`
  to `refs/heads/main:refs/heads/main` of `cisarik/framenest` by guarded
  fast-forward and non-force push, with direct public readback and unchanged
  other heads. Dispatching the prompt is the Cooperator publication grant.
  Rationale: the existing release helper requires public `main` equality
  before it can deploy the release. Report destination `09_report_00.md`
  (absent). Host setup/deployment and the Cooperator live login + synthetic
  ask follow.

- **2026-09-24 — Publication PASS reconciled.** `09_report_00.md` (SHA-256
  `5ed370df92c41066c3717776c62aaaf170589aa0080a3a349bc087e7693827c5`,
  publication-PASS, session 09 exchange 01) reconciled: public
  `refs/heads/main` of `https://github.com/cisarik/framenest.git` =
  `c975aba14840b97944aecc655907e3abc370341d` (tree
  `a80ab53cf5ee19ffe0af46de4e015519cd97d941`); other public heads unchanged
  (`feat/chatgpt-page-ask-kernel` `26d28b16`, `feat/x-meme-browser-companion`
  `7ff6546f`); local `main` and `origin/main` = `c975aba`; working branch
  restored at `c975aba`, clean; AP pin unchanged; no force, no other ref. The
  old repository `cisarik/kronika` remains at `66c40d43` and is untouched;
  S10 will rename and archive it. S3 still requires the bounded host
  setup/deployment and the Cooperator live login + synthetic ask.

- **2026-09-24 — S3 host setup/deployment grant issued.**
  `10_implementation_00.md` (session 10 / exchange 01, fresh-worker-session,
  Fresh Implementation Worker, phase implementation, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `571c6a30d645bed4e41cd78dc3b7e622aa867caeea6496126c73e4c04b220a16`.
  Ordered host mutation: create the `kronika-capture` account and capture
  paths; materialize one random token value as the root systemd credential and
  the matching 0600 capture-owned state token (CLI/legacy fallback); deploy the
  accepted release `c975aba`; install and enable the five capture units and the
  env file; start Xvfb and bridge; run `activate-capture` (expected exit 0, or
  16 with `needs_admin` and no retry); read-only verification; terminal
  `sudo -K`.   Stops before login; the Cooperator view login, explicit resume and
  one synthetic ask are the next step. The `framenest.service` token drop-in
  stays deferred to S7. Report destination `10_report_00.md` (absent).

- **2026-09-25 — S3 host setup BLOCKED; correction issued.** `10_report_00.md`
  (SHA-256
  `d44a733302ad297c19067f4acdf124c02e74a20a21372c8e4afcfad58cc23d82`)
  stopped BLOCKED: account, paths, token materialization, release deploy, unit
  install/enable and `activate-capture` ran, but Xvfb, bridge and runner
  failed. Two confirmed unit defects: **F-HOST-01** — the bridge and runner
  units place `--state-dir` after the subcommand while the CLI parent parser
  requires it before, so both exited 2 with `unrecognized arguments`; the same
  mistake was in the granted status command. **F-HOST-02** — Xvfb cannot
  create its lock file (`/tmp/.X99-lock` / `.tX99-lock`) under
  `ProtectSystem=strict` with only `/tmp/.X11-unix` writable, exited 1; the
  runner's required display never came up, so activation reported
  `readiness=failed` (exit 16) instead of `needs_admin`. Host residue:
  `kronika-capture-bridge.service` still auto-restarting (NRestarts 51+ at the
  report), the three units enabled, no browser process, no view started, no
  login. Repository unchanged; no push. S3 remains open.

- **2026-09-25 — S3 host correction grant issued.** `10_correction_01.md`
  (session 10 / exchange 02, current-worker-session, Bounded Correction
  Worker, phase correction, native planning mode not-used, manual Cooperator
  delivery, High), SHA-256
  `e629686ef86f7124d0ea616b2d72ee66b674c87895c18617b66b9830685ebbf9`.
  Steps: stop/disable/reset-failed the three capture units first (ends the
  bridge loop); read-only `/usr/bin/Xvfb -help` probe for `-nolock`; move
  `--state-dir` before the subcommand in the bridge and runner units; apply
  the least-privilege Xvfb lock fix; add a CLI-parse regression test for the
  unit `ExecStart` lines; focused route; one commit; terminal `sudo -K`. No
  push. Then: fresh re-acceptance of the correction, publication of the
  corrected commit, host retry, and the Cooperator login + synthetic ask.
  Report destination `10_report_01.md` (absent).

- **2026-09-25 — Host correction PASS reconciled; S3 re-acceptance issued.**
  `10_report_01.md` (SHA-256
  `47bbca2ca1ee0ac3bd162955b367ede25f38d5f67625e90e16c11b0c5e6eb721`)
  committed `94e605c17b881461fad3e22fd8c7fca32cb93976` (parent `c975aba`, tree
  `4667f47c24e84d80574beb66b71aca533393d994`, subject
  `fix(capture): accept the capture CLI state directory and skip the Xvfb
  lock`); delta exactly four allowed paths (three units plus
  `tests/contract/test_kronika_capture_services.py`). Host cleanup verified:
  bridge/runner/xvfb stopped, disabled and reset-failed, `NRestarts=0`, no
  chrome/Xvfb processes, no listeners on 8765/5900/6080; account, token files
  and release pointers retained. `/usr/bin/Xvfb -help` confirmed `-nolock`;
  the least-privilege fix was applied and `ReadWritePaths` stays
  `/tmp/.X11-unix /run/kronika-capture`. A CLI-parse regression now proves the
  corrected `ExecStart` lines parse and the old option order fails; the route
  ran 157 passed. No push; local and public `main` still `c975aba`. S3 remains
  open pending re-acceptance, publication of the corrected commit, the host
  retry and the Cooperator login + synthetic ask.

- **2026-09-25 — S3 full fresh re-acceptance grant issued.**
  `11_acceptance_00.md` (session 11 / exchange 01, fresh-worker-session, Fresh
  Independent Re-Audit, phase acceptance, native planning mode not-used,
  manual Cooperator delivery, High, required-fresh-independent), SHA-256
  `28020da7f8ee4cc6eb12a5b92d40e4957b8cd7c6d30bbc3f8291b7776a43ee87`.
  Candidate `94e605c17b881461fad3e22fd8c7fca32cb93976`; seven fixed claims
  covering the full S3 slice on the corrected units plus explicit F-HOST-01 and
  F-HOST-02 closures; no host contact. Report destination `11_report_00.md`
  (absent). Publication of the corrected commit and the host retry follow a
  PASS.

- **2026-09-25 — S3 correction re-acceptance PASS; publication issued.**
  `11_report_00.md` (SHA-256
  `43267f3baea33180812f476c07d6112d7061fcf02b6af135a269f1c688dd5503`, status
  PASS, acceptance-PASS, session 11 exchange 01) independently established all
  seven fixed claims on candidate `94e605c…`; F-HOST-01 and F-HOST-02 are
  `verified-closed` as source strategies; the declared route ran 197 passed;
  no findings. S3 repository and deployment sources accepted on the corrected
  commit. Ledger notes: the deployment doc does not name `-nolock` (outside
  the correction delta; carried forward); a live corrected Xvfb under the unit
  remains for the host retry; the reviewer corrected the owner-map base — the
  S3 commit diff base is `82a6a598`, while `26d28b16..c975aba` spans five
  commits and 80 paths.

- **2026-09-25 — S3 correction publication grant issued.**
  `12_publication_00.md` (session 12 / exchange 01, fresh-worker-session,
  Bounded Publication Worker, phase publication, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `d1be59c4f9ee1f53e603b6911dad0773ba157029eb3940ce6646a4ceaa36e7aa`.
  Exact authority: publish accepted `94e605c17b881461fad3e22fd8c7fca32cb93976`
  to `refs/heads/main:refs/heads/main` of `cisarik/framenest` by guarded
  fast-forward and non-force push, with direct public readback and unchanged
  other heads. Report destination `12_report_00.md` (absent). The host retry
  of the corrected units and the Cooperator login + synthetic ask follow.

- **2026-09-25 — Correction publication PASS reconciled; host retry issued.**
  `12_report_00.md` (SHA-256
  `ab673e7afecebbfb418bfd2139d4b25c51817d39b19d58c4dfe1d46ccf82708e`,
  publication-PASS, session 12 exchange 01) reconciled: public
  `refs/heads/main` of `cisarik/framenest` = `94e605c…`; other heads unchanged
  (`feat/chatgpt-page-ask-kernel` `26d28b16`, `feat/x-meme-browser-companion`
  `7ff6546f`); local `main` = `origin/main` = `94e605c`; working branch
  restored clean; AP pin unchanged; no force. S3 sources are public at the
  corrected commit.

- **2026-09-25 — S3 corrected host retry grant issued.**
  `10_deployment_02.md` (session 10 / exchange 03, current-worker-session,
  Bounded NUC Deployment, phase deployment, native planning mode not-used,
  manual Cooperator delivery, High), SHA-256
  `afb07541566c5a264479df655ffc82dd71f9abd1cb3309df0e46bbb13f442be8`.
  Steps: deploy accepted `94e605c`; reinstall the five corrected units and the
  env file from the release tree; daemon-reload; enable xvfb/bridge/runner;
  start Xvfb and bridge; run `activate-capture` (expected exit 0 or
  16/needs_admin, no retry); read-only verification; terminal `sudo -K`.
  Stops before login. Report destination `10_report_02.md` (absent). The
  Cooperator view login, explicit resume and one synthetic ask complete S3.

- **2026-09-25 — Host retry BLOCKED (new evidence); Xvfb lock correction
  issued.** `10_report_02.md` (SHA-256
  `b193ea31741fcd3ea363b7b9054c52331fa0d864431263e2eb70df8f783144b7`) deployed
  the corrected release `94e605c` and reinstalled the units; Xvfb ignored
  `-nolock` with `Warning: the -nolock option can only be used by root`, still
  needed `/tmp/.tX99-lock`, exited 1; activation exited 16 with readiness
  `browser_unavailable` (`E_BROWSER_UNAVAILABLE`); bridge and runner were left
  active, no Chromium process, no login; no repository change. This new
  material evidence invalidates the first lock assumption (the `-help` text
  was insufficient) and selects the fallback already named in
  `10_correction_01.md`.

- **2026-09-25 — Xvfb lock correction grant issued.** `10_correction_03.md`
  (session 10 / exchange 04, current-worker-session, Bounded Correction
  Worker, phase correction, native planning mode not-used, manual Cooperator
  delivery, High), SHA-256
  `54c06b4df33a730d729059af5d71511128c50bc3af8b2ebe04f249609f31f70f`.
  Steps: stop/disable/reset-failed the capture units first; replace `-nolock`
  with `ReadWritePaths=/tmp /tmp/.X11-unix /run/kronika-capture`; update the
  service contract test (`-nolock` absent, `/tmp` present, `-auth` kept); add
  one deployment-doc sentence; focused route; one commit; `sudo -K`. No push.
  Then full fresh re-acceptance, publication and the host retry again.

- **2026-09-25 — Xvfb lock correction PASS; re-acceptance issued.**
  `10_report_03.md` (SHA-256
  `65cb2945c76fbe512cac7a6a0cba2c8e532d0e14fdb53b05b3a114a0b1a77e28`)
  committed `d63d0b725acedf49d1611224c3b5201a90e7ef90` (parent `94e605c`, tree
  `95862a1e012256829ada49ed780ad665cd2aea18`, subject
  `fix(capture): let the unprivileged Xvfb create its display lock`); delta
  exactly three allowed paths (the Xvfb unit, the deployment doc, the service
  contract test). Host cleaned again: units stopped/disabled/reset-failed,
  `NRestarts=0`, no processes or listeners; account, tokens and both pointers
  untouched at `94e605c`. `-nolock` removed; `ReadWritePaths=/tmp
  /tmp/.X11-unix /run/kronika-capture`; `-auth`/`-nolisten tcp` kept; test
  updated; route 157 passed. No push; refs still `94e605c`.

- **2026-09-25 — S3 lock re-acceptance grant issued.** `13_acceptance_00.md`
  (session 13 / exchange 01, fresh-worker-session, Fresh Independent Re-Audit,
  phase acceptance, native planning mode not-used, manual Cooperator delivery,
  High, required-fresh-independent), SHA-256
  `13c94a711964598f3b0ad4eda0c0c096a0a3693aa054f3313749ebc7df88b9ab`.
  Candidate `d63d0b7…`; seven fixed claims covering the full S3 slice on the
  doubly corrected units with the Xvfb lock-strategy closure; no host contact.
  Report destination `13_report_00.md` (absent). Publication of the corrected
  commit and the host retry follow a PASS.

- **2026-09-25 — S3 lock re-acceptance PASS; publication issued.**
  `13_report_00.md` (SHA-256
  `d1a841201187bf841824feb3fc72adf3c4478bbd2f328eac266544201b2ae492`, status
  PASS, acceptance-PASS, session 13 exchange 01) independently established all
  seven claims on candidate `d63d0b7…`; the Xvfb lock strategy is closed with
  the `/tmp` fallback, F-HOST-01 remains closed, route 197 passed, no findings.
  S3 deployment sources accepted on the doubly corrected commit.

- **2026-09-25 — S3 lock correction publication grant issued.**
  `14_publication_00.md` (session 14 / exchange 01, fresh-worker-session,
  Bounded Publication Worker, phase publication, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `2a509340cc2631918aa9791a8c6d1684d2eafacccae5620919b4061ce5d847b5`.
  Exact authority: publish accepted `d63d0b725acedf49d1611224c3b5201a90e7ef90`
  to `refs/heads/main:refs/heads/main` of `cisarik/framenest` by guarded
  fast-forward and non-force push, with direct public readback and unchanged
  other heads. Report destination `14_report_00.md` (absent). The host retry
  and the Cooperator login + synthetic ask follow.

- **2026-09-25 — Lock correction publication PASS; host retry 2 issued.**
  `14_report_00.md` (SHA-256
  `e2fef7d551e01b6afdf0f05144726052728e83fb8542b38496df6cc65bd4de0e`,
  publication-PASS, session 14 exchange 01) reconciled: public
  `refs/heads/main` of `cisarik/framenest` = `d63d0b7…`; other heads unchanged
  (`feat/chatgpt-page-ask-kernel` `26d28b16`, `feat/x-meme-browser-companion`
  `7ff6546f`); local `main` = `origin/main` = `d63d0b7`; working branch
  restored clean; AP pin unchanged; no force.

- **2026-09-25 — S3 host retry 2 grant issued.** `10_deployment_04.md`
  (session 10 / exchange 05, current-worker-session, Bounded NUC Deployment,
  phase deployment, native planning mode not-used, manual Cooperator delivery,
  High), SHA-256
  `4bc88c08542f091d4f56de61f7e415196fa65e5ba3e58a55e89b2d30079bcf98`.
  Steps: deploy accepted `d63d0b7`; reinstall the five corrected units and the
  env file; enable xvfb/bridge/runner; start Xvfb with a stability pause;
  start bridge; run `activate-capture` (expected exit 0 or 16/needs_admin, no
  retry); read-only verification; terminal `sudo -K`. Stops before login.
  Report destination `10_report_04.md` (absent). The Cooperator view login,
  explicit resume and one synthetic ask complete S3.

- **2026-09-25 — Host retry 2 BLOCKED on a journal state; runner-start grant
  issued.** `10_report_04.md` (SHA-256
  `5689f08b1cfe99f626487263dbd76cd0c0b3ab46031cc7b5af3df4923f9eff43`) deployed
  `d63d0b7`, reinstalled the units and confirmed the lock fallback works:
  Xvfb stayed active through the stability pause, bridge active. But
  `activate-capture` exited 22 (`capture has live or paused work`) before the
  pointer switch and runner restart: the journal held a `needs_admin` service
  state with reason `E_AMBIGUOUS_SEND` from the failed bootstrap runs (zero
  jobs, zero Chromium). Web pointer at `d63d0b7`; capture pointer still
  `94e605c`; runner inactive. No repository change.
  Design reading: the recovery requires a running browser and an operator
  readiness check; the pre-existing blocked state must clear before activation
  can proceed.

- **2026-09-25 — Runner-start grant issued.** `10_deployment_05.md` (session
  10 / exchange 06, current-worker-session, Bounded NUC Deployment, phase
  deployment, native planning mode not-used, manual Cooperator delivery,
  High), SHA-256
  `d980cfcac77a86d572796848da4e845147d67a7d31baa3190bb311ddf25b654e`.
  Steps: start `kronika-capture-runner.service` once; verify exactly one
  Chromium; read the bridge status (readiness, reason, opaque intervention id,
  jobs, client connection); stop before view/login/resume/activation/ask.
  Report destination `10_report_05.md` (absent). The Cooperator login and
  explicit resume follow.

- **2026-09-25 — Binding Cooperator directive: Workers never release the NUC
  sudo timestamp.** From this point on, no grant runs `sudo -K` (and no Worker
  runs `sudo -v`). The Cooperator establishes the timestamp before dispatch
  and releases it manually afterwards. Rationale: automatic release forces
  repeated re-establishment and creates avoidable development friction. This
  is binding for every later grant and must be carried into the
  fresh-Orchestrator handout.

- **2026-09-25 — Runner-start BLOCKED; Planner issued instead of another host
  cycle.** `10_report_05.md` (SHA-256
  `f735352bdf5c57371c34e8f78ca3ddd9666eee33098967323ab0bce6e061c2ec`) started
  `kronika-capture-runner.service` once: the service stayed `active` with
  `client_connected: true`, but `pgrep -c -x chrome` and `chromium` were `0`;
  readiness stayed `browser_unavailable` (`E_BROWSER_UNAVAILABLE`), the
  intervention id did not change, and the unit journal held only systemd start
  lines (no application error). No login, view, resume, activation or ask.
  Code inspection by the Orchestrator: `parseChromiumMajorVersion` is used
  only on the stealth path, so the FrameNest-era version-parse issue is
  unlikely to explain the missing browser; the driver start/endpoint path,
  launch brake/lock metadata, or the Chromium sandbox/display environment
  remain open. Orchestrator decision (confirmed by the Cooperator): stop
  sequential host patching; issue a fresh Planner to root-cause and plan the
  deterministic S3 bring-up and any source corrections.

- **2026-09-25 — S3 recovery Planner grant issued.** `15_planning_00.md`
  (session 15 / exchange 01, fresh-worker-session, Planner, native planning
  mode required, manual Cooperator delivery, Extra High), SHA-256
  `6810b55f0676e9a44a8f1a1edbe222f1eb0e776fb14536e2756f38c833cb8b91`.
  Bounded planning question: root-cause or bound the missing
  Chromium launch; design the supported recovery of the persisted
  `needs_admin` journal state; specify the smallest source corrections with
  their tests and acceptance/publication route; produce the exact ordered host
  sequence for browser-up, Cooperator login, explicit resume,
  `activate-capture` and one synthetic ask. No host contact, no
  implementation authority. Report destination `15_report_00.md` (absent).

- **2026-09-25 — Planner report reconciled; C1+C2 implementation issued.**
  `15_report_00.md` (SHA-256
  `6f77414c38ea66f2057719c85234976000a13e748d677888b0a1dc95f72af5ed`) is on
  disk: the Cooperator persisted the session-delivered plan, so the delivery
  deviation is resolved as historical evidence. The plan is accepted:
  (1) the missing Chromium has no uniquely established cause because the
  runner deliberately hides the startup exception — bounded safe startup
  diagnostics are required; (2) the zero-job `needs_admin` state clears through
  the designed browser + explicit null-job resume + fresh readiness
  acknowledgement; no journal reset; (3) `activate-capture` can accept the
  previous persisted `ready` without a fresh runner/browser identity — a
  verification defect. Orchestrator spot-checks confirmed (1) the runner catch
  without logging and (3) the readiness gate in `framenest_release.py` reading
  the persisted service state. C3 (runner `TMPDIR`) stays conditional on the
  bounded host diagnostic.

- **2026-09-25 — C1+C2 implementation grant issued.** `15_implementation_01.md`
  (session 15 / exchange 02, current-worker-session, Implementation Worker,
  phase implementation, native planning mode not-used, manual Cooperator
  delivery, High), SHA-256
  `c9c876ceeeb3e585408006ce44cf1e83d1de44a4922073cd4ca91bd35a5308d6`.
  Scope: C1 bounded safe startup diagnostics in `driver.mjs`/`runner.mjs` with
  causal tests and sanitized logging; C2 fresh-identity activation readiness in
  the release helper (snapshot, one restart, 180 s deadline, no retry); the
  zero-job resume recovery regression. One commit, no push, no host contact.
  Report destination `15_report_01.md` (absent). Full-fresh acceptance,
  publication and the single bounded host diagnostic follow.

- **2026-09-25 — Routing directive: session 15 is closed to further prompts.**
  Its context window is full. Every later grant targets a fresh Worker session,
  never `current-worker-session` for that session.

- **2026-09-25 — C1+C2 implementation PASS reconciled; re-acceptance issued.**
  `15_report_01.md` (SHA-256
  `0beef12d7e876263cefc8775af847b7b49ad5a0278fbd75f9eb6fb458e1518a3`)
  committed `e408bb5503f359ec24542304ac1a621c6b9e4ffb` (parent `d63d0b7`, tree
  `dadc01726a354c319374832bfd385be0bdffb516`, subject
  `fix(capture): diagnose startup and require fresh activation readiness`);
  delta exactly seven allowed paths; route 205 Python and 52 Node tests passed;
  protected paths and AP pin unchanged; worktree clean; `main`/`origin/main`
  still `d63d0b7`; no push. Implementation PASS reconciled (non-independent).

- **2026-09-25 — S3 diagnostics/activation full fresh re-acceptance grant
  issued.** `16_acceptance_00.md` (session 16 / exchange 01,
  fresh-worker-session, Fresh Independent Re-Audit, phase acceptance, native
  planning mode not-used, manual Cooperator delivery, High,
  required-fresh-independent), SHA-256
  `5779cea465dfc3c49195abf5d1567a95b80f66c1b6a2839571a38f3bee42b5c5`.
  Candidate `e408bb55…`; six fixed claims covering C1 diagnostics, C2
  fresh-identity activation, the zero-job recovery regression and the
  preserved S3/S2 guarantees; no host contact. Report destination
  `16_report_00.md` (absent). Publication and the single bounded host
  diagnostic follow a PASS.

- **2026-09-25 — Diagnostics/activation re-acceptance PASS; publication
  issued.** `16_report_00.md` (SHA-256
  `442c7a0b731ea07a8e3d165c6c96740e5f2f98d1000e97bd5eede82ce8af9c94`, status
  PASS, acceptance-PASS, session 16 exchange 01) independently established all
  six fixed claims on candidate `e408bb55…`; C1 and C2 are closed; adversarial
  probes 37/37 and 92/92; declared route 205 Python and 52 Node tests; no
  findings; no host execution. S3 diagnostics/activation accepted.

- **2026-09-25 — Diagnostics/activation publication grant issued.**
  `17_publication_00.md` (session 17 / exchange 01, fresh-worker-session,
  Bounded Publication Worker, phase publication, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `8ba08f65e1bd732d638f223b70d03b75e230ae7857fd587e4e7c9fed19d99a11`.
  Exact authority: publish accepted `e408bb5503f359ec24542304ac1a621c6b9e4ffb`
  to `refs/heads/main:refs/heads/main` of `cisarik/framenest` by guarded
  fast-forward and non-force push, with direct public readback and unchanged
  other heads. Report destination `17_report_00.md` (absent). After this
  publication the extensive `01_handout.md` for a fresh Orchestrator follows,
  covering the single bounded host diagnostic (accepted plan §5), the
  Cooperator login/resume/activation/ask completion of S3, and the S4–S10
  path to `cisarik/kronika`.

- **2026-09-25 — Diagnostics/activation publication PASS reconciled.**
  `17_report_00.md` (SHA-256
  `48552c22270e0fc9a7ac9657f40c15447079699e746cde947167d7879ebae8ff`,
  publication-PASS, session 17 exchange 01): public `refs/heads/main` of
  `cisarik/framenest` = `e408bb5503f359ec24542304ac1a621c6b9e4ffb`; other
  public heads unchanged (`feat/chatgpt-page-ask-kernel` `26d28b16`,
  `feat/x-meme-browser-companion` `7ff6546f`); local `main` = `origin/main` =
  `e408bb5`; working branch restored clean; AP pin unchanged; no force.

- **2026-09-25 — Orchestrator rotation: handoff to a fresh Orchestrator.**
  `01_handout.md` written (SHA-256
  `a2dc8936870094d6a18137566b0706c33c54d015e452ebb0ffac4e3f6b01d66a`),
  restoring the successor Orchestrator for the ongoing whole: verified refs,
  the accepted and published S0–S3 deliverables, the binding Cooperator sudo
  directive (Workers never run `sudo -v`/`sudo -K`), the accepted S3 recovery
  playbook (`15_report_00.md` §5–§7), the S4–S10 path, ledger candidates,
  trace grammar and STOP rules, plus a paste seed in §10. From this handoff
  the successor Orchestrator leads; this session stops issuing grants. The
  whole remains open; S3 host bring-up, Cooperator login, explicit resume,
  activation and one synthetic ask are the immediate next work.

- **2026-09-25 — S3 deploy+D1 grant reconciled (deployment-PASS); D2 block
  issued.** `18_deployment_00.md` (session 18 / exchange 01,
  fresh-worker-session, Bounded NUC Deployment, native planning mode not-used,
  manual Cooperator delivery, High), SHA-256
  `19b387268b5cd4af1efa38471acfae450f06354dee4a698fea6545b52d9fa15`.
  Report `18_report_00.md` (SHA-256
  `a8bf2bca7f1d04fa85a6e9ef48026b3a50b72aacce41736b39558fa31f094a45`, status
  PASS, deployment-PASS, coordinates 18/01) reconciled: helper `status`,
  `check`, `deploy` exited 0; `public_main` and `web_release` `e408bb5`,
  capture release unchanged `94e605c`; post-deploy `/opt/framenest/current` =
  `e408bb5`, `capture-current` = `94e605c`, `.framenest-release-sha` matches,
  `framenest.service` active. D1 read-only: Xvfb/bridge/runner active,
  NRestarts 0; installed unit directives match the `e408bb5` sources; zero
  chrome/chromium processes (0 browser roots); bridge status
  `browser_unavailable` / `E_BROWSER_UNAVAILABLE`, zero jobs, opaque
  intervention id `dc3fc192-…`, `client_connected` true, `browser_session`
  `2bb2c1ac-…`; Xauthority readable, X99 socket present, `/usr/bin/chromium`
  resolves to Chrome for Testing 154.0.8037.57, userns knob 1; port 8765
  loopback-only, 5900/6080/6099 closed. Orchestrator re-verified local HEAD,
  `main`, `origin/main` and public `main` at `e408bb5`, worktree clean.
  Deployment accepted (non-independent); S3 remains open. LEDGER candidate
  (non-authorizing): non-capture listeners 53809/50216 were not identified;
  outside the capture boundary. Next: D2 Cooperator-executed blocks (stop only
  the runner; confirm no browser process; inspect external brake metadata),
  then D3. No `sudo -K` in any grant.

- **2026-09-25 — D2/D3 host diagnostic executed and classified; S3 stops for an
  evidence-based correction plan.** D2a: runner stopped cleanly
  (`Result=success`, `ExecMainStatus=15`), zero chrome/chromium processes.
  D2b: external brake metadata directory present, `lock` absent,
  `last-start.json` valid, `remaining_ms` 0 — no mutation needed, no `rmdir`.
  D3a first attempt aborted fail-closed before any mutation because
  `.framenest-release-sha` is root-only; only the precondition read was
  adapted to `sudo -n cat`. D3a-R2: temporary
  `/run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf`
  (ExecStart pinned to the `e408bb5` release tree) written, `daemon-reload`,
  single runner start. D3b (read-only): runner active from the corrected tree
  (`NRestarts=0`, `ExecMainStatus=0`); zero chrome/chromium; bridge status
  `browser_unavailable` with a new `browser_session` `1eb21d68-…` and the
  unchanged intervention id; the journal emitted exactly one C1 record:
  `capture_startup {"outcome":"failed","stage":"endpoint","reason":
  "process_exited","exit_code":21,"stderr_classification":"profile_in_use",
  "endpoint_seen":false,"endpoint_budget_exhausted":false,
  "cleanup_failed":false}`. Classification: Chromium refused the profile as
  in use (ProcessSingleton wording) while no Chromium process exists. Per the
  accepted plan this is the profile-in-use branch: stop, no profile
  inspection, no profile-internal lock removal, C3 not selected; the single
  diagnostic browser spawn is spent. D3c cleanup: runner stopped, override
  removed, `daemon-reload`, effective `ExecStart` resolves through
  `capture-current` again, override absent; Xvfb and bridge active; web
  pointer `e408bb5`, capture pointer `94e605c`; no outstanding mutation; no
  `sudo -K` in any block. Privacy note: one `ss -ltn` paste included
  non-loopback listener addresses; the values are not recorded and later reads
  use filtered/classified output. Next: fresh Planner (session 19) for the
  lawful correction of the profile-in-use condition; S3 remains open.

- **2026-09-25 — Profile-in-use recovery plan reconciled (PARTIAL, accepted as
  the basis for one evidence grant); P0/P1 evidence grant issued.**
  `19_planning_00.md` (session 19 / exchange 01, fresh-worker-session, Planner,
  native planning mode required, manual Cooperator delivery, Extra High),
  SHA-256 `bfdedcede698d9b9b7162d342b762a6774fc836559aa32b00c59b12c908b5830`.
  Report `19_report_00.md` (SHA-256
  `c87f854a6aaf44b551230ffb20c734c2702b27f68681ab08e7ccc4844cbe5f78`, status
  PARTIAL, coordinates 19/01) was session-delivered and persisted by the
  Cooperator from the session output. Plan accepted: the recorded class
  conflates the two ProcessSingleton wordings, no cause is established, and
  the single next evidence step is P0 (read-only service/process preflight by
  a fresh Worker through the gate) plus P1 (one Cooperator-executed synthetic
  filesystem/socket probe under the runner's copied restrictions), with zero
  browser starts; correction branches A–E stay conditional and no profile
  action is authorized. Grant issued: `20_preflight_00.md` (session 20 /
  exchange 01, fresh-worker-session, Fresh Evidence Probe, phase preflight,
  native planning mode not-used, manual Cooperator delivery, High), SHA-256
  `93bf395587c3f826af58b420d4070532a3b7649c771da38b39a5d82756f2762a`.
  Adaptations to the standing directive: no `sudo -K` anywhere (Cooperator
  releases manually) and the exact report write at `20_report_00.md` is
  authorized. Report destination absent. S3 remains open.

- **2026-09-25 — P0/P1 prerequisite probe reconciled (PASS); Cooperator
  profile decision requested.** `20_report_00.md` (SHA-256
  `f336b668dda83d782a1119a03c55d4eb41cad94e684b51f3ec910c57fdce1b7b`, status
  PASS, coordinates 20/01) reconciled: Step 0 gate and repository baseline
  unchanged; P0 runner `inactive`, Xvfb/bridge `active`, zero browser
  processes, unit restrictions matching the `e408bb5` source; P1 (single
  Cooperator-executed `kronika-s3-singleton-probe.service` invocation) all
  preflight booleans true (binary path, temp environment, profile directory
  owner/mode 0700/access, synthetic roots absent); primitive results: `/tmp`
  mkdir refused `EROFS`; `runtime` and `state` roots mkdir+file+symlink+socket
  `ok`; all cleanups `removed`; `probe_transport=completed`. Decision-table
  row: temporary storage remains a supported candidate but C3 is NOT selected
  (the original Chromium operation and path are unproven); profile-root
  metadata is satisfied; profile-specific state and Chromium-specific behavior
  remain unresolved. No correction selected, no browser start, no outstanding
  mutation, no `sudo -K`. Orchestrator decision request to the Cooperator:
  fresh-profile option per accepted plan branch C (opaque retention of the
  never-logged-in profile at `profile.s3-pre-recovery` plus a new empty 0700
  profile) followed by one separately authorized corrected bootstrap start;
  alternatives: preserve-and-stop with no start, or a C1 wording-refinement
  cycle before any start. S3 remains open.

- **2026-09-25 — Corrected bootstrap on a fresh profile failed identically;
  policy evidence exhausted; instrumented-launch decision requested.**
  Cooperator profile block completed cleanly (`preconditions_ok`,
  `retained_ok`, `fresh_created_ok`, `verify_ok`): `profile` renamed to
  `profile.s3-pre-recovery` (opaque, never inspected), new empty `profile`
  0700 owned by `kronika-capture`. The single corrected bootstrap start
  (override `ExecStart` pinned to the `e408bb5` release) then failed exactly
  as before: one C1 record `stage=endpoint`, `reason=process_exited`,
  `exit_code=21`, `stderr_classification=profile_in_use`,
  `endpoint_seen=false`; zero Chromium processes. Stale-profile-artifact
  hypothesis ruled out. Cleanup completed (runner stopped, override removed,
  `daemon-reload`); external brake lock absent, `last-start.json` valid with
  the interval consumed; web pointer `e408bb5`, capture pointer `94e605c`;
  no outstanding mutation. Read-only policy evidence: no kernel
  AppArmor/audit denials in the attempt window; auditd inactive; loaded
  AppArmor profiles include `chrome` (attachment `/opt/google/chrome/chrome`,
  `flags=(unconfined)`) and `framenest-chrome` (attachment
  `/opt/framenest/tooling/chrome-for-testing/**/chrome`,
  `flags=(unconfined)`, sole rule `userns,`) — the chrome binary is
  effectively unconfined and the userns grant is the profile's only purpose,
  so AppArmor is not the cause. `/etc/kronika-capture/capture.env` carries
  only `KRONIKA_CHROMIUM_PATH`; the unit environment sets no TMPDIR or
  XDG_RUNTIME_DIR. Public reference confirms the generic ProcessSingleton
  line is always preceded by a specific operation+errno line that C1
  discards. Cooperator route decision requested: one bounded instrumented
  synthetic launch (alternate temporary profile under the capture account and
  the copied unit restrictions, bounded sanitized stderr classification)
  versus staying launch-free. S3 remains open.

- **2026-09-25 — Root cause bound: Chromium singleton socket directory
  creation fails on read-only general `/tmp`; C3 selected.** The single
  instrumented synthetic launch (alternate temporary profile under the
  capture account and the copied runner restrictions) reproduced the startup
  failure and produced the specific failing line:
  `[ERROR:chrome/browser/process_singleton_posix.cc:1043] Failed to create
  socket directory.` followed by the generic ProcessSingleton abort; exit 21;
  no probe processes remained; both temporary objects removed
  (`cleanup_ok`). Public Chromium source confirms the singleton socket
  directory is created with `ScopedTempDir::CreateUniqueTempDir()` in the
  temp directory (`$TMPDIR`, else `/tmp`), precisely because some
  filesystems cannot host Unix sockets; the runner's `ProtectSystem=strict`
  allowlist does not include general `/tmp`, and the P1 probe independently
  showed `/tmp` mkdir `EROFS`. The capture profile is not the failing object
  (fresh profile and profile symlink creation both fine; the profile only
  receives the socket symlink and cookies). The C3 trigger is now
  established by direct evidence. The probe touched no capture state and
  left no outstanding mutation. Next: C3 implementation grant (runner unit
  `Environment=TMPDIR=/run/kronika-capture/tmp` plus `ExecStartPre` creating
  the runtime temp dir, contract test and deployment doc), then full-fresh
  acceptance, publication, deployment and one corrected bootstrap start.
  S3 remains open.

- **2026-09-25 — C3 implementation grant issued.**
  `21_implementation_00.md` (session 21 / exchange 01, fresh-worker-session,
  Fresh Implementation Worker, phase implementation, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `bb4b7ba5f567d4886274911b289da1283d3a7573e1f6f59eeb2643d6acdf7d37`.
  Exact allowlist: `deploy/systemd/kronika-capture-runner.service`,
  `tests/contract/test_kronika_capture_services.py`,
  `docs/UBUNTU_NUC_DEPLOYMENT.md`; exact unit change
  `Environment=TMPDIR=/run/kronika-capture/tmp` plus the `ExecStartPre`
  third path `/run/kronika-capture/tmp`; contract regression that fails on
  the baseline; one commit, no push; declared route `./.ap/ap project check`
  and `test-focus` with the baseline `e408bb5`; no host contact. Report
  destination `21_report_00.md` (absent). Next after a PASS: full-fresh
  independent acceptance (session 22), publication, deployment, unit
  reinstall and one corrected bootstrap start.

- **2026-09-25 — C3 implementation PASS reconciled; full-fresh acceptance
  issued.** `21_report_00.md` (SHA-256
  `0ca3905c31384d34f85819c43118450248c867d5a66bddb554d52dae58665503`,
  status PASS, implementation-PASS, coordinates 21/01) reconciled: commit
  `fd277a9a64a6965df76127dbec5b1735d2fb3cdd` (parent `e408bb5`, tree
  `3b9014956a3bc738a209af51034fcac58ef5c498`, subject
  `fix(capture): point the capture runner temporary directory at its runtime
  dir`); the delta is exactly the three allowlisted paths; the new regression
  failed on the baseline unit (1 failed, 130 passed) and passes on the
  candidate (131 passed); `./.ap/ap project check` PASS; worktree clean; AP
  pin unchanged; local `main`/`origin/main` and current public `main` still
  `e408bb5`; no push. Acceptance grant `22_acceptance_00.md` (session 22 /
  exchange 01, fresh-worker-session, Fresh Independent Re-Audit, phase
  acceptance, native planning mode not-used, manual Cooperator delivery,
  High, required-fresh-independent), SHA-256
  `8571698829a394189d51f27db21d024923e29783243ad538f40df31053db4131`;
  candidate `fd277a9`; six fixed claims, fixed positive/negative controls,
  one declared temporary root; no host contact. Report destination
  `22_report_00.md` (absent).

- **2026-09-25 — C3 acceptance PASS reconciled; publication grant issued.**
  `22_report_00.md` (SHA-256
  `e5c7e2004bd81eb92571a662376309788d0a796678602c7a769bb469a941ded9`,
  status PASS, acceptance-PASS, coordinates 22/01, candidate `fd277a9`)
  independently established all six fixed claims with the declared route
  (`ap project check` PASS, `131 passed`; `node --test` 52/52), baseline
  causality via `git show`, exact three-path containment, clean worktree, AP
  pin unchanged, no push, no findings. Residual risks recorded: synthetic
  tests do not prove host Chromium startup; the installed
  `/etc/kronika-capture/capture.env` was not read and an installed `TMPDIR`
  assignment would override the unit value (deployment-time read-only check
  remains). Publication grant `23_publication_00.md` (session 23 / exchange
  01, fresh-worker-session, Bounded Publication Worker, phase publication,
  native planning mode not-used, manual Cooperator delivery, High), SHA-256
  `927df11abe1f4581e384000a7c45b599ac5589c1ef725e124f76780ec100522a`;
  exact authority: publish `fd277a9a64a6965df76127dbec5b1735d2fb3cdd` to
  `refs/heads/main:refs/heads/main` of `cisarik/framenest` by guarded
  fast-forward and non-force push, direct public readback, unchanged other
  heads. Report destination `23_report_00.md` (absent). Next after
  publication: deployment of `fd277a9`, runner unit reinstall, read-only
  installed `capture.env` TMPDIR check, and the single corrected bootstrap
  start.

- **2026-09-25 — C3 publication PASS reconciled; deploy + corrected-start
  grant issued.** `23_report_00.md` (SHA-256
  `9fed7f7baa0e7bb4d45169dc0326b298d34845fe1d0c0eda6be57af97004d632`,
  publication-PASS, coordinates 23/01) reconciled and independently
  re-verified by the Orchestrator with direct `git ls-remote`: public
  `refs/heads/main` of `cisarik/framenest` = `fd277a9`; other heads unchanged
  (`feat/chatgpt-page-ask-kernel` `26d28b16`, `feat/x-meme-browser-companion`
  `7ff6546f`); local `main` = `origin/main` = `fd277a9`; working branch
  `feat/kronika-one-product` clean at `fd277a9`; AP pin `7478ddb0` unchanged;
  no force. Deployment+start grant `24_deployment_00.md` (session 24 /
  exchange 01, fresh-worker-session, Bounded NUC Deployment, phase
  deployment, native planning mode not-used, manual Cooperator delivery,
  High), SHA-256 `8c0027259d79e4ecc1238e51eb52fa61a7c9fcba612bbe1ebfd0b92b12e9a37b`:
  helper deploy of `fd277a9`, install the corrected runner unit from the
  deployed tree, read-only installed `capture.env` TMPDIR check, brake
  metadata check, then exactly one Cooperator-executed corrected bootstrap
  start (override `ExecStart` pinned to the `fd277a9` release tree) and
  read-only classification; stop before view/login/resume/activation/ask.
  Report destination `24_report_00.md` (absent).

- **2026-09-26 — C3 deployment and corrected start: SUCCESS (deployment-PASS,
  classification Started).** `24_report_00.md` (SHA-256
  `2ae45f1550a63333a602489f162b948ba9d880d1415523089e75297b1654347a`,
  status PASS, deployment-PASS, coordinates 24/01) reconciled: helper
  `status`, `check`, `deploy` exited 0 with `public_main` and `web_release`
  `fd277a9`, capture release unchanged `94e605c`; corrected runner unit
  installed (`Environment=TMPDIR=/run/kronika-capture/tmp`, `ExecStartPre`
  with `/run/kronika-capture/tmp`, mode 0700); installed
  `/etc/kronika-capture/capture.env` has no `TMPDIR` assignment (grep exit
  1); external brake lock absent, `last-start.json` valid and expired (age
  7,636,445 ms); the single Cooperator start block completed
  (`subshell_exit=0`); Stage 6: runner active, NRestarts 0, and the first
  successful Chromium start — C1
  `capture_startup {"outcome":"started","stage":"complete","reason":"none",
  "endpoint_seen":true,...}`; 13 chrome processes with one root (pid 149158,
  ppid 149147); bridge status readiness `needs_admin`, reason
  `E_COMPOSER_NOT_FOUND`, intervention id `dc3fc192-…`, browser_session
  `78a90b17-…`, client_connected true, zero jobs; port 8765 loopback-only;
  browser and the temporary override kept in place. LEAD recorded: whether
  `E_COMPOSER_NOT_FOUND` is the login wall or another page state is unseen;
  the Cooperator view resolves it. Next: H2 Cooperator view and interactive
  login through the loopback tunnel.

- **2026-09-26 — COOPERATOR DECISION: park S3 at the login boundary.**
  H2 login remained blocked by a repeating Cloudflare challenge (~10
  attempts; Cooperator observation that Chrome for Testing may be flagged).
  Offered routes: (1) cooldown plus one careful retry; (2) a bounded planner
  for a browser/approach change (host inventory: Google Chrome absent, snap
  Chromium 153 stable present, CfT 154 is the configured binary); (3) park
  S3 at the login boundary. The Cooperator chose 3. Parking state: runner
  active from the accepted `fd277a9` release tree under the temporary
  recovery override; one root Chromium running with readiness `needs_admin`
  (reason `E_COMPOSER_NOT_FOUND`); zero jobs; Xvfb and bridge active;
  capture pointer still `94e605c`; view units stopped/expired and loopback
  view ports closed; no job, no journal change, no correction. The whole
  remains open and paused; S4 waits for S3 completion per `01_report_00.md`
  ("Evidence before S4"). Resume point: Cooperator login through the
  loopback view on the parked browser, then the explicit null-job resume,
  `activate-capture --release fd277a9… --yes`, H5 verification and one
  synthetic ask. A fresh-Orchestrator restoration handout can be produced
  when the Cooperator wants to resume.

- **2026-09-26 — Parking state finalized (S3 open, whole paused).** Final
  read-only confirmation: view and vnc units inactive and already unloaded
  by the manager (`reset-failed` returned "not loaded"; no failed flag, no
  listeners on 5900/6080); runner, Xvfb and bridge active; one root Chromium
  with 13 processes; port 8765 loopback-only; web pointer `fd277a9`,
  capture pointer `94e605c`; the temporary recovery override remains in
  place for the eventual activation step. The journal shows the view stop
  was a normal `signal 15` stop in which x11vnc exited
  `status=2/INVALIDARGUMENT` and systemd briefly recorded `failed`; nothing
  remains. LEDGER candidate (non-authorizing): the vnc unit's normal SIGTERM
  stop yields exit status 2, which systemd marks as failure; a future
  view-unit contract could declare a success exit status. S3 remains open at
  the H2 login boundary; the whole is paused with no active Worker and no
  outstanding mutation beyond the intended recovery override and the parked
  browser.

- **2026-09-26 — COOPERATOR DIRECTION CHANGE: modular search/deep-research
  provider; capture becomes one parked module.** New direction: Kronika keeps
  MEME and Movie and adds Search and Research, but search/deep research comes
  through a modular provider abstraction rather than the capture modes;
  chatgpt.com capture remains as one currently parked module; the Search
  module is to be an agent with a web search tool available; the goal remains
  transforming FrameNest into Kronika. This supersedes the S4 route of
  `01_report_00.md` (restore capture modes) and changes the role of the
  parked S3/S5 capture foundation. It does not change the whole identity
  (one Kronika on the FrameNest base) or the preserved decisions (Timeline,
  Gallery, existing records, private-by-default family sharing, no old-DB
  import, NUC dev/test, no mass rename, S10 public rename). The conflict with
  durable documentation is identified; a bounded documentation update
  belongs to the superseding plan. Material Cooperator decisions needed
  before planning: the first provider/agent substrate and its external
  call/credential/cost posture, and the provider-neutral record, error and
  budget contract. No host action; S3 remains parked at the H2 login
  boundary.

- **2026-09-26 — COOPERATOR DECISION: first provider class is an external
  agent with a web search tool.** Chosen from the four options: (1) external
  provider/agent with web search tool, (2) self-hosted, (3) hybrid, (4)
  ChatGPT capture as the first provider. The modular abstraction stays
  provider-neutral; the concrete provider, its credentials, cost cap and
  privacy posture remain a Cooperator selection inside the planning. Planner
  grant issued: `25_planning_00.md` (session 25 / exchange 01,
  fresh-worker-session, Planner, native planning mode required, manual
  Cooperator delivery, Extra High), SHA-256
  `f1104c75d650e12a46bb0769ae6885a05ebb3148d207288a7b73d1332e307f44`:
  design the modular search/deep-research provider architecture, the record
  and rendering integration, the provider-boundary security/privacy
  requirements, the revised S4–S10 slice order replacing the capture-mode
  S4 route, the durable documentation update, and a concrete provider
  recommendation package for Cooperator selection. Planning only; no
  implementation, no host contact, no provider calls. Report destination
  `25_report_00.md` (absent).

- **2026-09-26 — Modular-provider plan reconciled and accepted; S4-D
  documentation grant issued.** `25_report_00.md` (SHA-256
  `84504ae1fb42ee67500e3a5038ff2a21a4c0d8993f34af41497fec9b6eb39a2a`,
  status PASS, coordinates 25/01, session-delivered in chat and then
  persisted to the trace by the Cooperator) reconciled and spot-checked
  read-only by the Orchestrator: baseline `fd277a9` clean, local
  `main`/`origin/main` and public `refs/heads/main` = `fd277a9`, AP pin
  unchanged; no ADR-0083 exists; migration head `0033`; the named AI
  registry/configuration/credentials/transport files and application ports
  exist; `AGENTS.md:248` still carries the old administrator-private-content
  denial (superseded below). New Cooperator decisions recorded by the plan
  (current strategic authority, superseding conflicting earlier
  assumptions): question/answer history retained including complete Research
  reports; authenticated administrators may read all product records
  including private and unfinished work; shared-page publication is
  administrator-approved and owners do not publish directly; Timeline shows
  only approved records with personal history as a separate view; the shared
  page is household-only and internet publication stays disabled; native
  Deep Research executes at the provider with FrameNest supervising; the
  first provider is the OpenAI Responses API with fixed model
  `gpt-5.5-2026-04-23` and no automatic fallback; application thresholds
  Search USD 0.50, Research USD 5, daily USD 10, monthly USD 30 plus a
  provider monthly hard limit of USD 30 with accepted delayed enforcement;
  standard provider retention accepted (ZDR not required). The plan
  supersedes the capture-mode S4 route and re-sequences S4-D → S4-A → S6 →
  S4-B → S7-P → S8 → S9 → S10 while parking the remaining S3 host
  completion, capture-mode restoration, S5 ZIP activation and S7-C capture
  integration. Plan accepted. S4-D implementation grant issued:
  `26_implementation_00.md` (session 26 / exchange 01, fresh-worker-session,
  Fresh Implementation Worker, phase implementation, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `f7f2cd715e548e07859f9fbf83cabd8a109c9d143c21a5f27eb1aad624e05678`:
  twelve-path documentation-only allowlist including new
  `docs/adr/0083-modular-research-providers-and-administrator-curated-timeline.md`,
  required contradiction search, declared route, one commit
  `docs(kronika): define modular research and administrator-curated timeline`,
  no push. Report destination `26_report_00.md` (absent). Capture host
  remains parked; no host action.

- **2026-09-26 — S4-D accepted (Orchestrator direct review); S4-A grant
  issued.** `26_report_00.md` (SHA-256
  `ea4bb1256289d3505c4213c3768afb03fb1f5453ad1c3523dd1d6cb2a7d7b16a`,
  status PASS, implementation-PASS, coordinates 26/01) reconciled: commit
  `72009c3b525b6a46e87223cb9a143b5079d89cbf` (parent `fd277a9`, tree
  `ba4b9290f0c986ac9cec6c3acec49ba747bf9b70`, subject
  `docs(kronika): define modular research and administrator-curated
  timeline`); exactly the twelve allowlisted paths; route PASS (19 contract
  tests); AP pin, managed block and upgrade-ledger blob unchanged; no push.
  Orchestrator direct documentation review (full AGENTS.md diff, ADR-0083
  head, ADR-0082 partial-supersession section) found the recorded decisions
  faithful and internally consistent. S4-D accepted (E1/R0, documentation
  slice; no independent acceptance required). S4-A implementation grant
  issued: `27_implementation_00.md` (session 27 / exchange 01,
  fresh-worker-session, Fresh Implementation Worker, phase implementation,
  native planning mode not-used, manual Cooperator delivery, High),
  SHA-256
  `45f779dadf48b0fbc7fe81db7506ee40693ed4a15efa725c319cd6c24c7ed267`:
  eight-path allowlist (domain research values, application ports, AI
  configuration v3 plus research configuration, research registry, three
  test files), v1/v2 backward compatibility, deterministic fake provider,
  disabled by default, no real adapter, network or credentials; one commit
  `feat(kronika): add provider-neutral research contracts and configuration`;
  no push. Report destination `27_report_00.md` (absent). Publication of the
  accepted chain stays a separate later grant.

- **2026-09-26 — S4-A implementation PASS reconciled; bounded correction
  issued.** `27_report_00.md` (SHA-256
  `52f77574b97a7bf9761d9874b9c675250dd51bfc76a218f1d51ebdf04076c90a`,
  status PASS, implementation-PASS, coordinates 27/01) reconciled: commit
  `75e9b07b2bf2269568382e28d40a8d2ff8d4bc28` (parent `72009c3`, tree
  `9f52d90790e4c1d0b37a6594d9c13071fa94a007`, subject
  `feat(kronika): add provider-neutral research contracts and
  configuration`); exactly the eight allowlisted paths; route 399 passed; AP
  pin, managed block and upgrade ledger unchanged; no push. The MEASURED
  finding is accepted as one concrete defect inside the row: the AI CLI
  writers rebuild `AiServerConfig` without `research`
  (`src/framenest/adapters/cli/ai.py`, four constructors around lines
  342/375/449/518), so a later media CLI save drops a stored research
  section; the administrator API already preserves it. Correction grant
  issued: `28_correction_00.md` (session 28 / exchange 01,
  fresh-worker-session, Bounded Correction Worker, phase correction, native
  planning mode not-used, manual Cooperator delivery, Medium), SHA-256
  `759a90c936809e5a72bdb3369761fc1ae3de9980d6426e4973349af4ccbc8a63`:
  two-path allowlist (`src/framenest/adapters/cli/ai.py`,
  `tests/unit/adapters/cli/test_ai_cli.py`), carry `existing.research` in all
  four constructors, focused regression, one commit
  `fix(kronika): preserve research configuration in AI CLI writers`, no push.
  Report destination `28_report_00.md` (absent). After the correction: one
  focused independent acceptance of the corrected S4-A candidate, then S6.

- **2026-09-26 — S4-A correction PASS reconciled; focused acceptance issued.**
  `28_report_00.md` (SHA-256
  `c1408b13a63fec91daa42126b7fdd3505d5317a4fbb392df727f492dd3f035a3`, status
  PASS, implementation-PASS, coordinates 28/01) reconciled: commit
  `40e51cb2d061ead96850c9c94aa59de54d5e1310` (parent `75e9b07`, tree
  `ec3c6c9db49ede4bfcd3616263b388bb26451834`, subject
  `fix(kronika): preserve research configuration in AI CLI writers`); the two
  allowlisted paths; regression failed before the fix and passed after (424
  passed); AP pin and ledger blobs unchanged; no push. Orchestrator
  re-verified the row candidate: HEAD `40e51cb2`, clean, row diff against
  `72009c3` is exactly ten paths, AP pin unchanged, public `main` still
  `fd277a9`. Note: the commit body carries a `Co-authored-by: Cursor` trailer
  from the client commit path (cosmetic; accepted, no rewrite). Acceptance
  grant issued: `29_acceptance_00.md` (session 29 / exchange 01,
  fresh-worker-session, Fresh Independent Audit, phase acceptance, native
  planning mode not-used, manual Cooperator delivery, High,
  required-fresh-independent), SHA-256
  `cdce228f9a6019ca14af78aaacdc6b3b294509d242b13db98cd5ba611b8dc3e6`;
  candidate `40e51cb2`; seven fixed claims; declared route and synthetic
  temporary-root controls; no host or provider contact. Report destination
  `29_report_00.md` (absent). After acceptance: S6 (records, access and
  approval) and publication of the accepted chain as separate grants.

- **2026-09-26 — S4-A focused acceptance PASS; publication grant issued.**
  `29_report_00.md` (SHA-256
  `6d46816b2718361a33b98007bb5e31919b22a251665b434982df66860152b140`,
  status PASS, acceptance-PASS, coordinates 29/01, candidate `40e51cb2`)
  independently established all seven fixed claims with the declared route
  (451 passed) and synthetic temporary-root controls, including that the
  parent CLI writers drop a present research section while the candidate
  preserves it; no findings; clean candidate and temporary-root cleanup. The
  Orchestrator re-verified the chain: `fd277a9` is an ancestor of
  `40e51cb2`; the delta over public `main` is 22 paths, 3277 insertions, 341
  deletions. Publication grant issued: `30_publication_00.md` (session 30 /
  exchange 01, fresh-worker-session, Bounded Publication Worker, phase
  publication, native planning mode not-used, manual Cooperator delivery,
  High), SHA-256
  `39a0ff366acff94d63dd744d9862393b671273f45166fa92b445a6b0faae0126`:
  publish `40e51cb2d061ead96850c9c94aa59de54d5e1310` to
  `refs/heads/main:refs/heads/main` of `cisarik/framenest` by guarded
  fast-forward and non-force push with direct public readback and unchanged
  other heads.   Report destination `30_report_00.md` (absent). Capture host
  remains parked; next after publication: S6 (records, access and approval).

- **2026-09-26 — S4-D/A chain published; S6 execution-planning grant issued.**
  `30_report_00.md` (SHA-256
  `825d86a81aaffc3e4fa939912c898e8abb10e9eaa2698e172a1134adae9d2a33`,
  publication-PASS, coordinates 30/01) reconciled and independently
  re-verified by the Orchestrator with direct `git ls-remote`: public
  `refs/heads/main` of `cisarik/framenest` =
  `40e51cb2d061ead96850c9c94aa59de54d5e1310`; other heads unchanged
  (`feat/chatgpt-page-ask-kernel` `26d28b16`, `feat/x-meme-browser-companion`
  `7ff6546f`); local `main` = `origin/main` = `40e51cb2`; working branch
  clean; AP pin unchanged; no force. Because S6 is the fail-closed
  authorization slice whose seam change can ripple across every
  app-constructing contract test (currently a permissive `policy is None`
  branch), a bounded Planner grant was issued before implementation:
  `31_planning_00.md` (session 31 / exchange 01, fresh-worker-session,
  Planner, native planning mode required, manual Cooperator delivery, High),
  SHA-256
  `c30010e29034a9d60396cb955db1f08890f5a2b13435b48cde6fbb001b2e3197`:
  produce the exact S6 file allowlist, migration `0034` design, centralized
  owner/admin/household policy and fail-closed seam strategy with the
  complete affected-test inventory, approval/history foundations with
  S7-P/S8 boundaries, the access-inventory artifact design, the E3/R3 test
  matrix and acceptance route, and the exact next implementation grant.
  Planning only; no implementation, host or provider action. Report
  destination `31_report_00.md` (absent).

- **2026-09-26 — S6 plan reconciled (PARTIAL); single targeted revision
  issued.** `31_report_00.md` (SHA-256
  `993c73e22862c70754039aab0031f2f29c5cab0d4c0f0ab689390c16b4679f9a`, status
  PARTIAL, coordinates 31/01, written with private mode 0600) delivered a
  repository-grounded S6 design: migration 0034 (`kronika_documents` +
  `kronika_records`) with invariants, indexes and a guarded downgrade; pure
  domain/access values and application ports/service placement; the
  owner/admin/household caller matrix; the fail-closed audience-seam change
  and SQL-before-count filtering; approval/withdrawal/concurrency semantics;
  private-history and admin-inventory foundations with S7-P/S8 boundaries;
  the access-inventory artifact design with route seeds; candidate file
  sets N/P/T/H including the verified direct-seam test ripple (17 test files)
  and the migration-head ripple (21 test files); an E3/R3 test matrix and
  route; and a deliberately withheld draft grant. It left three material
  mappings open (G1 upload/acquisition authorization and indirect test
  fallout; G2 approved-projection integration across live readers/writers and
  removal; G3 private live DB/WAL/SHM boundary) and explicitly warned that a
  helper-only patch cannot establish accepted all-route authorization.
  Orchestrator disposition: the mapped content is accepted as the basis; the
  single authorized planning revision (basis `newly-identified-material-risk`,
  the G1–G3 gaps) was issued to close those mappings and produce one complete
  exact allowlist with an issuable next grant. Revision grant:
  `32_planning_00.md` (session 32 / exchange 01, fresh-worker-session,
  Planner, native planning mode required, manual Cooperator delivery, High),
  SHA-256
  `6e5e7e3bcbdc38520ecc2b0f1b36358ac0a301d3c87c6b6225403c6473822ddd`;
  a remaining open mapping returns `Escalation disposition:
  NEEDS_ORCHESTRATOR_DECISION`. Report destination `32_report_00.md` (absent).
  Note: the prior Planner's client mode was switched to Default mid-session
  by a developer instruction; the work stayed planning-only and wrote only
  its report.

- **2026-09-26 — S6 revision delivered as a Slovak plan artifact; standard
  report-completion exchange issued.** `32_report_00.md` (SHA-256
  `ff5dd6551e9568707520fa31ff1bf671f37076d3c43946bf3d7bbc9db8f7ef39`,
  184 lines) arrived as a client-native plan artifact in Slovak without the
  standard Worker report form (no `### Report for ORCHESTRATOR_CHAT` header,
  coordinates, compact core or critique) and references a private client
  attachment path. Content reviewed by the Orchestrator: it closes the three
  open mappings — G1 (explicit local-owner identity via
  `FRAMENEST_LOCAL_OWNER_LOGIN` restricted to loopback/operator-UDS with
  configured mapping, upload/YouTube/X/operator/proposal closures, internal
  recovery provenance, corrected real acquisition route names), G2 (three
  relational approved-projection tables plus a typed read scope
  `deny|current|approved|legacy`, surface behavior matrix, conditional
  version bumps on bound records, legacy publish/unpublish and media-removal
  refusals that preserve approval), G3 (private catalog creation/open helper
  with 0700/0600, symlink/hardlink refusal, WAL/SHM/journal verification,
  lazy engine, migration/backup/development coverage, guarded downgrade) —
  and extends the catalogue with exact additional production and test paths
  plus the implementation order, mandatory scenarios and the declared test
  route. Orchestrator disposition: the plan content is accepted as the
  revision basis; its form is nonconformant, so a bounded
  report-completion exchange was issued under the Planner-Artifact Report
  Completion Repair route to render the standard English report without
  reopening the plan. Completion grant: `33_planning_00.md` (session 33 /
  exchange 01, fresh-worker-session, Planner report completion, native
  planning mode not-used, manual Cooperator delivery, Medium), SHA-256
  `efb43fbe3a24786d60db09311aca2b310d6ad673dc4217a78f41b62bc17dacc7`:
  render the frozen plan in the standard report form, verify the merged
  allowlist read-only against the baseline, and recommend the issuable S6
  implementation grant. Report destination `33_report_00.md` (absent).

- **2026-09-26 — S6 report-completion rendered and verified; S6 plan closed;
  Orchestrator rotation.** `33_report_00.md` (SHA-256
  `17ec937fa78ae67cfd6f416aaccfeac3aed01cd455334aeeb8db8fbaa88d9d9c`, status
  PARTIAL solely because the client Plan mode blocked the Worker's file
  write; the Cooperator persisted the complete chat report to the trace, so
  the pair is complete) rendered the frozen S6 revision plan in English and
  verified the complete merged allowlist read-only: 176 unique paths (153
  existing, 23 proposed new), no missing, duplicate, outside-repository or
  ambiguous path. It carries the closed G1/G2/G3 mappings, the implementation
  order, the mandatory scenarios, the declared focused route (the 96
  enumerated test files) followed by one broad suite run, the E3/R3
  acceptance route, and the recommended S6 implementation grant. The
  Orchestrator accepts the plan as complete and issuable. Because this
  Orchestrator session's context is very long, the Orchestrator rotates at
  this coherent planning boundary: `02_handout.md` prepares a fresh
  Orchestrator to re-verify state read-only, issue the S6 implementation
  grant to the next fresh Worker session (34), run the separate fresh E3/R3
  authorization acceptance, then continue S4-B → S7-P → S8 → S9 → S10 with
  the capture module parked. The whole remains open; the parked capture host
  is unchanged (runner active from the `fd277a9` release under the recovery
  override, one Chromium at `needs_admin`, view closed).

- **2026-09-26 — Fresh Orchestrator restored (`02_handout.md`); S6
  implementation grant issued to session 34.** Read-only restoration
  re-verified every claimed state: FrameNest `feat/kronika-one-product` HEAD
  `40e51cb2d061ead96850c9c94aa59de54d5e1310` (parent `75e9b07b…`, tree
  `ec3c6c9…`, subject `fix(kronika): preserve research configuration in AI
  CLI writers`), clean index/worktree, local `main` = `origin/main` =
  `40e51cb2…`; AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (gitlink and
  `.ap` HEAD); migration head `0033` with `0034` free; ADR-0083 present;
  archive checkout `main` = `66c40d43…` clean with the same pin. Direct
  `git ls-remote` confirmed public `cisarik/framenest` `refs/heads/main` =
  `40e51cb2…` (other heads unchanged `26d28b16`, `7ff6546f`) and
  `cisarik/kronika` `main` = `66c40d43…`. The parked NUC capture host was not
  re-measured because no host step is planned in S6. The merged S6 allowlist
  was re-verified read-only against the baseline: 176 unique paths (153
  existing, 23 new-file absent), 96 focused test files, no duplicates or
  outside-repository paths. The accepted S6 plan (`31`/`32`/`33`) is complete
  and issuable. Issued the single S6 implementation grant
  `34_implementation_00.md` (session 34 / exchange 01, fresh-worker-session,
  Fresh Implementation Worker, native planning mode not-used, manual
  Cooperator delivery, High, independence no), SHA-256
  `6e84ee390888d98302e9ce31a3cca8a5c7ac393faf4b7856b56cf6137f797f78`: records
  and immutable Q/A documents, closed G1/G2/G3, the exact 176-path allowlist,
  the 96-file focused list plus one broad suite run on the declared AP route,
  mandatory scenarios and the executable inventory, one local commit
  `feat(kronika): add private records and administrator approval`, no push.
  Report destination `34_report_00.md` (absent at issuance). The delivery
  instruction requires a write-capable client mode (Plan mode OFF) because the
  session-33 Plan restriction blocked report persistence. After a PASS report:
  a separate fresh independent E3/R3 authorization review of the exact
  candidate SHA; then S4-B -> S7-P -> S8 -> S9 -> S10 with the capture module
  parked.

- **2026-09-26 — S6 implementation PARTIAL reconciled; completion grant issued
  (session 34 / exchange 02).** `34_report_00.md` (SHA-256
  `1e68d1bc96770cb1dd311265093ef3e25adb6d274f924e60f1b1a8bcb28a00de`, status
  PARTIAL, coordinates 34/01) passed Step 0 and produced an uncommitted
  dirty-worktree partial S6: 81 allowlisted paths (66 modified, 15 new),
  including migration 0034, records domain/service/repository, record-first
  audience policy, typed catalog scope, approved projection, private-state
  helper and local identity; missing 7 tests plus the access-inventory
  document; unfinished YouTube/X/workspace/analysis-proposal closures; an
  unclassified public-composition `GET /api/media` 500 (`PUBLIC_READ_FAILED`),
  a `KeyError: display_title` overlay failure, and a stale failing
  unit/contract run; no stage, commit, push or host action. Orchestrator
  verified read-only that the worktree set matches the report exactly and every
  path is inside the 176-path allowlist; classification
  `accepted-continuation` (preserved; no reset/clean). Issued the completion
  grant `34_implementation_01.md` (session 34 / exchange 02,
  current-worker-session, Implementation Worker, native planning mode
  not-used, manual Cooperator delivery, High, independence no), SHA-256
  `fb512a3eec09f1b634dfa64319199089529d2d0517daa6f00fb1e35573496689`:
  re-gate the preserved worktree, finish the G1 closures and remaining
  failures inside the unchanged allowlist, create the 8 missing paths including
  `docs/KRONIKA_ACCESS_INVENTORY.md`, complete the mandatory-scenario evidence,
  run the focused 96-file list and one broad suite on the declared route, then
  create one local commit `feat(kronika): add private records and administrator
  approval`; no push. Report destination `34_report_01.md` (absent at
  issuance). Routing recommendation was current-session 34 (retained
  repository understanding; same healthy whole; independence not required);
  the Cooperator may override to a fresh session. After a PASS report: the
  separate fresh independent E3/R3 authorization review of the exact candidate
  SHA.

- **2026-09-27 — S6 second PARTIAL reconciled; final completion grant issued
  (session 34 / exchange 03); pre-existing debt parked.** `34_report_01.md`
  (SHA-256 `345885401742d6dfd57e0dfe0794b7423f2da56f01f008f947034670531c0771`,
  status PARTIAL, coordinates 34/02) finished the slice to 104 allowlisted
  paths (81 modified, 23 untracked, including the eight paths missing after
  exchange 01 and `docs/KRONIKA_ACCESS_INVENTORY.md`); the focused 96-file
  list exited 0 (1003 passed, 5 skipped, 257.38 s) and the broad suite exited
  1 with 4 failed, 3830 passed, 8 skipped (558.45 s); no commit or push. The
  four failures are two pre-existing clusters outside the allowlist, verified
  read-only by the Orchestrator: the stale `.venv` lacking the declared
  `framenest-chatgpt-page` console script, and the three operator SSH-gate
  parameters failing because `FRAMENEST_NUC_SSH_TARGET`/`USER`/`IDENTITY` are
  exported in the ambient environment (names only; values not read). The
  Orchestrator parked both clusters as non-authorizing debt and ledger
  candidates: refresh `.venv` from `pyproject.toml`, and harden the gate test
  against ambient environment defaults. Residual S6 gaps: inventory
  truthfulness (generic audience-policy test IDs reused per route; operator
  YouTube claim rows mislabelled identity-not-required) and missing
  mandatory-scenario coverage (HTTP+SQL caller matrix, identity forgery/audit,
  denial-before-open, indirect disclosure, projection stability, transaction
  races, bound-removal receipt, backup/restore). The Orchestrator verified the
  104-path worktree set matches the report exactly and stays inside the
  176-path allowlist; classification `accepted-continuation` (preserved).
  Issued the final completion grant `34_implementation_02.md` (session 34 /
  exchange 03, current-worker-session, Implementation Worker, native planning
  mode not-used, manual Cooperator delivery, High, independence no), SHA-256
  `b49a3b5ccd7b3c95e63f7775efd1e3995ebd6336f30a5383a073cdb8b04bd1ab`:
  truthful inventory, the listed mandatory-scenario evidence, focused list
  exit 0 and broad suite with only the four parked failures, then one local
  commit `feat(kronika): add private records and administrator approval`; no
  push. Report destination `34_report_02.md` (absent at issuance). If this
  exchange ends PARTIAL/BLOCKED on a materially unchanged residual blocker,
  the report must carry the repeated-blocker escalation capsule; a third
  equivalent cycle needs new mutation, evidence, risk or a changed objective.

- **2026-09-27 — S6 third PARTIAL reconciled; bounded correction issued
  (session 34 / exchange 04) with a two-path allowlist extension.**
  `34_report_02.md` (SHA-256
  `32085919615377c244071c9dfd0c0ec603c2d1028801071a4564b01c3e0f5ca7`, status
  PARTIAL, coordinates 34/03) completed the residual S6 items: the inventory
  is now truthful (94 rows: 71 content, 23 exclusion; zero generic
  audience-policy test IDs; operator YouTube rows state configured local
  identity, `youtube.acquire` and "loopback alone is insufficient"), and the
  missing mandatory-scenario coverage now exists (caller matrix, identity
  audit, denial-before-open, indirect disclosure, projection stability,
  transaction races, bound removal, backup/restore). Focused 96-file list
  exit 0 (1156 passed, 5 skipped, 264.07 s). Broad suite exit 1 with 5
  failures: the four parked pre-existing cases plus one new S6 regression,
  `tests/contract/test_youtube_fake_demo.py::test_youtube_fake_demo_runs_the_real_loopback_cli_to_acceptance`
  (completed process exit 1; assertion at `tests/support/youtube_fake_demo.py:705`).
  Orchestrator read-only diagnosis confirmed the cause: the exchange-03
  operator closure requires a verified `youtube.acquire` identity
  (`_acquisition_identity`), while the demo's minimal app installs only the
  operator router and never installs the production `LocalIdentityMiddleware`
  / `configured_local_identity` path, so the real loopback CLI is refused.
  The 108-path worktree was verified entirely inside the original 176-path
  allowlist; classification `accepted-continuation` (preserved). The two
  implicated files are outside the original allowlist; the Orchestrator
  authorized the smallest coherent correction with an explicit effective
  allowlist of the 176 paths plus exactly
  `tests/support/youtube_fake_demo.py` and
  `tests/contract/test_youtube_fake_demo.py`. The correction must use the real
  configured-local-identity mechanism, must not weaken the operator identity
  gate or the demo assertions, and must not change production code. Correction
  grant `34_implementation_03.md` (session 34 / exchange 04,
  current-worker-session, Bounded Correction Worker, phase correction, native
  planning mode not-used, manual Cooperator delivery, Medium, independence
  no), SHA-256
  `6dcaa31ac414427ab32dd3bc1a4baf49578d7c33dd21440ccef2d2894b750c74`:
  narrow demo reproduction, gate tests unchanged and green, focused 96-file
  list exit 0, broad suite with only the four parked failures, then one local
  commit `feat(kronika): add private records and administrator approval`; no
  push. Report destination `34_report_03.md` (absent at issuance).

- **2026-09-27 — S6 fourth PARTIAL reconciled; second bounded correction issued
  (session 34 / exchange 05).** `34_report_03.md` (SHA-256
  `ed3925a198fcbb4df84e7663dde954a17deb2cbe53fd8b8fa4b595b7eaa4f019`, status
  PARTIAL, coordinates 34/04) installed the real configured-local-owner path
  in the demo harness (`FrameNestSettings` with an admin `identity_map`,
  `configured_local_identity`, `LocalIdentityMiddleware`; no direct
  `SCOPE_IDENTITY` seeding, no production edit), fixing the operator 401 and
  restoring the first ingest and same-video reuse. The narrow demo run then
  exposed a new production side effect: the manual byte duplicate is cataloged
  `"new"` instead of `"reused"` because
  `YouTubeAcquisitionCoordinator._handoff`
  (`src/framenest/application/youtube_acquisition.py:1189-1195`) selects
  EXPLICIT only when `created_by_login_key is None`; a verified login — now
  passed by the S6 operator route — selects SILENT_KEEP_SEPARATE. That
  contradicts the accepted design ("administrators retain explicit
  resolution"; the upload API derives it from `upload.manage` and `ROLE_ADMIN`
  includes that capability), and the Worker correctly stopped because the fix
  is a production change outside the exchange-04 grant. The 109-path worktree
  stayed inside the effective allowlist; classification `accepted-continuation`
  (preserved). Issued the second and final bounded correction grant
  `34_implementation_04.md` (session 34 / exchange 05, current-worker-session,
  Bounded Correction Worker, phase correction, native planning mode not-used,
  manual Cooperator delivery, Medium, independence no), SHA-256
  `84701c980d300914a6504e57764d2ffa795b703eddf204cdd7f950dc9f541914`: make
  the YouTube handoff select EXPLICIT for an administrator login
  (`upload.manage`) while ordinary requesters stay SILENT, wired from
  `application.py` and the demo harness; do not change the identity requirement
  or the X handoff; add one causal regression distinguishing the two paths;
  then the narrow demo, gate tests, focused 96 exit 0 and the broad suite with
  only the four parked failures; one local commit
  `feat(kronika): add private records and administrator approval`; no push.
  Effective allowlist unchanged (176 paths plus the two demo paths). Report
  destination `34_report_04.md` (absent at issuance). If this exchange ends
  PARTIAL/BLOCKED on a materially unchanged residual blocker, the escalation
  capsule is mandatory and further equivalent cycles stop.

- **2026-09-27 — S6 candidate committed (Implementation PASS); Cooperator
  endgame directive; independent E3/R3 acceptance issued.** `34_report_04.md`
  (SHA-256
  `463ff0a8b95b446f888ee037f259f5e8704a23a5217e3f1fa698173bce46d3dd`, status
  PASS, coordinates 34/05) closed the operator duplicate-resolution correction:
  the handoff and byte-duplicate resolver now keep `EXPLICIT` for a creator
  login carrying `upload.manage` (new predicate `mapped_role_has_capability`,
  wired from `create_app` and the demo harness), ordinary requesters stay
  `SILENT_KEEP_SEPARATE`, a new regression test covers it, and the demo passes.
  One local commit
  `38e7beeb3921d7c0fd8e717e480754fbd18130c9` (parent `40e51cb2…`, tree
  `d6d5d314…`, subject `feat(kronika): add private records and administrator
  approval`, 109 changed paths); Orchestrator verified read-only that all 109
  are inside the effective allowlist (176 + the two demo paths), the worktree
  is clean, `main`/`origin/main` remain `40e51cb2…`, and the broad suite fails
  only the four parked pre-existing cases. **Cooperator endgame directive
  (2026-09-27):** finish what can be finished; no more full-suite runs at every
  mini-step/fix (targeted validation only) for the remaining Workers; prepare
  a real handout whose finish state must have the complete latest code both in
  GitHub and on the NUC; the Cooperator switches development from the PC to
  the MacBook, the PC stays in the office, the NUC moves with him and will be
  plugged into a new network (NUC Ethernet, MacBook WiFi) where Tailscale
  should work; no file may be lost; the fresh-Orchestrator handout must make
  this migration painless (including carrying list and the NUC release
  runbook). Planned finishing sequence: independent E3/R3 acceptance → separate
  Cooperator publication grant to `cisarik/framenest` main → NUC latest-code
  step (remote routine release update if reachable now, otherwise a ready
  runbook in the handout) → `03_handout.md` with a development-environment
  migration section for the MacBook. Issued the acceptance grant
  `35_acceptance_00.md` (session 35 / exchange 01, fresh-worker-session, Fresh
  Independent Audit, phase acceptance, native planning mode not-used, manual
  Cooperator delivery, High, required-fresh-independent), SHA-256
  `816172ff9a43292a24930c3fb256a77cb18596368e5534b5aebb0cf4442203c3`:
  seven fixed claims (records/migration, fail-closed authorization, approval
  and projections, G1 closures, private state, public exclusion, inventory and
  containment), a bounded security subset instead of the full suite, one
  synthetic `/tmp` probe root, INFOSEC R3 activated. Report destination
  `35_report_00.md` (absent at issuance). The four parked pre-existing
  failures stay disposed and unrepaired.

- **2026-09-27 — S6 acceptance PARTIAL (blocking finding S6-A35-F01); PC→MacBook
  endgame actions issued (36 transport, 37 NUC accepted release, 03 handout).**
  `35_report_00.md` (SHA-256
  `08df6f51828b494e67f2a688fde4518c658a7440b16887298fc0be1924d59acb`, status
  PARTIAL, coordinates 35/01) — fresh independent E3/R3 audit of `38e7bee…`:
  claims 1, 2, 4, 5, 6, 7 established (records/migration, fail-closed denial
  and separation, G1 closures, private state, public exclusion,
  inventory/containment; 273 focused tests exit 0; R3 probes). Claim 3
  (approved projections on HTTP) is NOT established: finding S6-A35-F01
  (high, correction-required) — after approval of A, `GET /api/media/{id}`
  and `/metadata` return the working state B to an ordinary household member,
  the detail discloses a post-approval location id, content returns 409
  rather than 404 for it, and gallery membership requires a stray legacy
  publication row. S6-A35-F02 was a rejected false positive. Publication is
  not the next step; a bounded correction and a fresh re-audit are. Cooperator
  directive "NUC teraz": because the routine helper requires public main ==
  release and local HEAD == release, the unaccepted S6 candidate cannot be
  published to main or deployed; the latest accepted published code remains
  `40e51cb2…`. Issued the S6 candidate transport grant
  `36_publication_00.md` (session 36 / exchange 01, fresh-worker-session,
  Bounded Publication Worker, phase publication, native planning mode
  not-used, manual Cooperator delivery, Medium, independence no), SHA-256
  `c59faf6ec8de618fd1fcbd486d6e92a1e9c4343fbcc63aacde3ae8e3ae6f26eb`: push
  exactly `refs/heads/feat/kronika-one-product` at `38e7bee…` non-force with
  direct readback; `main` unchanged; report `36_report_00.md`. Issued the NUC
  accepted-release grant `37_deployment_00.md` (session 37 / exchange 01,
  fresh-worker-session, Bounded NUC Deployment, phase deployment, native
  planning mode not-used, manual Cooperator delivery, High, independence no),
  SHA-256
  `44eabc3509959b3efc29ea21661450cc61ad0a6ec77889e45df6338e1cad1046`:
  temporary detached checkout of `40e51cb2…`, canonical `framenest-release`
  `status`/`check`/`deploy`, return checkout to `feat/kronika-one-product`,
  read-only as-left state capture; capture stays parked; no DB reset; report
  `37_report_00.md`. Wrote the fresh-Orchestrator migration handout
  `03_handout.md` (SHA-256
  `72982c5070e268f559019b1fcaf9a45f51c8ebe5906c62017546c811f5392c84`): S6
  finding and correction direction, remaining slices, PC→MacBook carry list
  (the trace is REQUIRED), MacBook setup, NUC-on-new-network runbook, updated
  STOP rules and the binding testing-economy directive. The Cooperator must
  carry/archive the trace so the MacBook can continue.

- **2026-09-27 — Candidate transport and NUC accepted release both PASS; the
  PC/move endgame is ready.** `36_report_00.md` (SHA-256
  `a55324c60ce0c789773ca62541b3396100901345e1ee4e16676d8f2e81e8caa6`, status
  PASS, publication-PASS, coordinates 36/01): non-force push created public
  `refs/heads/feat/kronika-one-product` = `38e7bee…`; `main` and the two other
  heads unchanged; Orchestrator re-verified with direct `git ls-remote`:
  `main` `40e51cb2…`, branch `38e7bee…`, other heads unchanged; local branch
  clean at `38e7bee…`, `main`/`origin/main` `40e51cb2…`. `37_report_00.md`
  (SHA-256
  `230c7981f690a9d1c95fa8b4c75526dc520d9b60c0763d010b13884dd20109a3`, status
  PASS, deployment-PASS, coordinates 37/01): the canonical helper deployed
  `40e51cb2…` as the web release (pointer and `.framenest-release-sha` match;
  database revision was 0033 pre-deploy; no migration continuation), capture
  release still `94e605c…`; checkout returned to `feat/kronika-one-product` at
  `38e7bee…` clean. As-left NUC state: capture runner active with
  `NRestarts=0`, readiness `browser_unavailable` (`E_BROWSER_UNAVAILABLE`),
  `client_connected` true, jobs 0/0, zero `chrome`/`chromium` — the earlier
  `needs_admin` plus one Chromium claim is superseded as-left and requires no
  action while capture stays parked; `framenest.service` active; `tailscaled`
  active and enabled; listeners 8765/53 loopback-only and 22/443/631/50216/
  53809 non-loopback (outside the capture boundary). Orchestrator
  reconciliation: the capture readiness change is a parked-state observation,
  not a failure; no worker mutation follows. The Worker left the NUC sudo
  timestamp in place; the Cooperator releases it manually. The handout
  `03_handout.md` was updated with the verified GitHub and NUC state and the
  next fresh session ordinal 38. Remaining before power-off: the Cooperator
  archives/copies the trace (the MacBook cannot continue without it), then the
  NUC and the PC may be powered off; development resumes on the MacBook by
  pasting the `03_handout.md` seed into a fresh Orchestrator chat, which issues
  the S6-A35-F01 bounded correction grant (targeted tests only, then a fresh
  E3/R3 re-audit and a separate publication grant).

- **2026-09-28 — Fresh Orchestrator restored on the MacBook (`03_handout.md`);
  environment completed; NUC SSH restored; S6-A35-F01 correction grant issued
  (session 38 / exchange 01).** Read-only re-verification on the MacBook:
  FrameNest `main` `40e51cb2…` clean; direct `git ls-remote` on
  `cisarik/framenest`: `refs/heads/main` `40e51cb2…`, `refs/heads/feat/kronika-one-product`
  `38e7bee…`, `refs/heads/feat/chatgpt-page-ask-kernel` `26d28b16…`,
  `refs/heads/feat/x-meme-browser-companion` `7ff6546f…`; trace complete
  (107 files, `00_notes.md`..`37_report_00.md`; reports 35/36/37 match the
  SHA-256 values recorded here). Migration gaps found and closed: `.ap` was
  uninitialized (initialized at the pin `7478ddb0…`; `.ap` HEAD equals the
  gitlink), canonical `.venv` was absent (created via `./framenest setup`,
  CPython 3.13.14), and the feature branch was not present locally (fetched;
  `feat/kronika-one-product` checked out at `38e7bee…`, clean). MacBook-to-NUC
  SSH was locked out: the `~/.ssh/config` alias pointed at the stale office LAN
  address (updated to the MagicDNS FQDN) and the passphrase-protected MacBook
  key `id_ed25519_framenest_nuc` was not authorized on the NUC (added via the
  physical console; agent-loaded). `ssh framenest-nuc true` returns NUC-OK.
  No host state was mutated; no `private/**` was read; no values recorded.
  Issued the bounded S6-A35-F01 correction grant `38_correction_00.md`
  (session 38 / exchange 01, fresh-worker-session, Bounded Correction Worker,
  phase correction, native planning mode not-used, manual Cooperator delivery,
  High, independence no), SHA-256
  `f5c3af564f74a7e8df9c99783e4cadaf841e8d19ccb6788e7a478213df62e199`:
  approved-decision household reads (detail, metadata, list membership and
  filters, content/download, analysis, cover, preview) serve only the approved
  projection, its approved locations and its cover digest; gallery membership
  without a legacy publication row; the exact required regression; targeted
  tests only; one local commit `fix(kronika): serve approved projections on
  household reads`; no push. Report destination `38_report_00.md` (absent at
  issuance). After a PASS report: a separate fresh independent E3/R3 re-audit
  of the corrected exact SHA, then a separate Cooperator publication grant,
  then the NUC release update, then S4-B -> S7-P -> S8 -> S9 -> S10.

- **2026-09-28 — S6 correction exchange 38/01 BLOCKED by a macOS AP-tooling
  defect; AP portability-update decision requested.** Report `38_report_00.md`
  (SHA-256 `86a0eda29de487ace60c40c8282fde2f4c2d489c829859648307b64686f738e1`)
  saved; no edits, no commit; branch remains `38e7bee…` with a clean tree; the
  four parked failures were not run. Root cause (Orchestrator-reproduced): the
  pinned `.ap/ap` counts NUL-separated values with bare
  `awk 'BEGIN { RS="\0" }'` (`ap` line 710) inside its sanitized stage
  (`PATH=/usr/bin:/bin`); macOS BSD awk does not support a NUL record
  separator, so the count is 1 while the newline-separated count is 2, and both
  `ap project check` and `ap exec` exit 1 with
  `operation.runtime-info.argv values must not contain newlines`. The pin
  `7478ddb0…` is the current `cisarik/ap` main head; no newer upstream fix
  exists. Orchestrator prepared and verified (on a copy outside the
  repository) a one-line portable fix
  (`tr -cd '\000' | wc -c | tr -d ' '`): the patched tool passes
  `project check` and `ap exec runtime-info` (exact-source provenance
  `.venv/bin/python`, `src/framenest/__init__.py`). No repository, submodule,
  AP or remote mutation was performed; the temporary AP clone lives outside
  the repository. Decision requested from the Cooperator: AP
  portability-update task (recommended) versus per-grant deviation.

- **2026-09-28 — COOPERATOR DECISION: AP portability update; executed and
  adopted; session 38/01 BLOCKED pair acknowledged; correction renewed as
  38/02.** With the Cooperator's explicit grant, the one-line portable fix
  (`project_count_key` no longer counts with `awk RS="\0"`; it now uses
  `tr -cd '\000' | wc -c | tr -dc '0-9'`) was committed as
  `73e20ef80b88700d5fcbc397cd8edd4fc425869f` (parent `7478ddb0…`, subject
  `fix: count project argv values portably on BSD awk`) and pushed non-force to
  `cisarik/ap` `refs/heads/main` with direct readback. This repository adopted
  the new pin: `./.ap/ap update --check`/`update --apply`, `doctor --candidate`,
  staged `.ap`, strict `doctor` PASS, and one local commit
  `5843486ddeae13ec5b331f102c5cb595bfa6e386` (parent `38e7bee…`, subject
  `chore: adopt AP pin 73e20ef…`) carrying the gitlink plus a new
  `docs/AP_UPGRADE_OBSERVATIONS.md` entry (state `implemented`, evidence class
  `worker-observed`, closure `remove-from-active-ledger`). Canonical route
  re-verified on the MacBook: `project check`, `runtime-info` (exact-source
  `.venv`) and focused tests exit 0; no product source changed. Exchange 38/01
  (`38_correction_00.md` SHA-256 `f5c3af…` / `38_report_00.md` SHA-256
  `86a0eda2…`, both committed in Meta) is acknowledged as a terminal BLOCKED
  on the now-resolved tooling defect. During renewal preparation the
  predecessor prompt's working copy was accidentally overwritten and restored
  byte-identically from Git (no loss). Issued the renewal
  `38_correction_01.md` (session 38 / exchange 02, current-worker-session,
  Bounded Correction Worker, phase correction, native planning mode not-used,
  manual Cooperator delivery, High, independence no), SHA-256
  `e0700e05ff624d0118215c5ef9f800d6d4a0ac1013664459e32903296c9b2cf8`:
  predecessor R1–R10 remain binding with baseline
  `5843486ddeae13ec5b331f102c5cb595bfa6e386` and AP pin
  `73e20ef80b88700d5fcbc397cd8edd4fc425869f`; one predecessor allowlist path
  (`src/framenest/application/ports/media_cover_repository.py`, not in the
  176-path effective union) is explicitly excluded; one local commit
  `fix(kronika): serve approved projections on household reads`; no push.
  Report destination `38_report_01.md` (absent at issuance). Coordination
  note: two Orchestrator sessions had been restored from the same handout; the
  Cooperator continues with this one, and the superseded session stops
  granting.

- **2026-09-28 — S6-A35-F01 correction exchange 38/02 PASS; independent E3/R3
  re-audit issued (session 39).** `38_report_01.md` (SHA-256
  `1218e2213901e3259cdebc31eafe99241668b143d4e850bf9f8aaadb16eba57f`, status
  PASS, implementation-PASS, coordinates 38/02) reconciled and re-verified
  read-only by the Orchestrator: commit
  `0d0d8c88bf88bf8454751a0205bc8652374796c2` (parent
  `5843486ddeae13ec5b331f102c5cb595bfa6e386`, tree
  `96adead05beb58f2e282ff77b9e6d29bff2c8298`, subject
  `fix(kronika): serve approved projections on household reads`); 14 changed
  paths, every one inside the effective allowlist, no protected path touched;
  clean worktree; branch ahead of origin by the pin bump and the correction
  only; no push. Regression Red/Green: the new household test failed on the
  unfixed baseline (`display_title` `TitleB`) and passes after the fix;
  targeted 15-file set `281 passed`; the four parked failures were not run.
  R2–R8 implemented (R6 cover bytes and R8 gallery preview not dynamically
  exercised — recorded as the named missing evidence); the R7 LEAD was
  reproduced: household `ai-suggestions` returned only the approved
  `SnapshotTitle` after the working analysis changed. Issued the fresh
  independent E3/R3 re-audit grant `39_acceptance_00.md` (session 39 /
  exchange 01, fresh-worker-session, Fresh Independent Audit, phase acceptance,
  native planning mode not-used, manual Cooperator delivery, High,
  required-fresh-independent), SHA-256
  `860c22a90704cda00589b5cd49677e9b7c66a9184d9bc52ff637213280ca52f8`:
  eight fixed claims (candidate containment and diff leak hunt; dynamic
  S6-A35-F01 disproof; R5 semantics; approved cover bytes/ETag with no
  fallback; R7 analysis LEAD; gallery-preview denial; non-weakening and
  unchanged behavior; inventory stability), the declared focused subset and
  synthetic probe root `/tmp/kronika-one-product-s6-reaudit`, candidate
  `0d0d8c8…`, targeted only, no full suite. Report destination
  `39_report_00.md` (absent at issuance). After a PASS: a separate Cooperator
  publication grant for the accepted corrected candidate, then the NUC release
  update, then S4-B -> S7-P -> S8 -> S9 -> S10.

- **2026-09-28 — S6-A35-F01 re-audit PASS; S6 correction accepted; publication
  grant issued (session 40).** `39_report_00.md` (SHA-256
  `62122e5347d914434a1c394e15682cb95031dce774ebd8df6cbcd6b9e8acb133`, status
  PASS, acceptance-PASS, coordinates 39/01) reconciled and re-verified
  read-only: independent fresh re-audit of
  `0d0d8c88bf88bf8454751a0205bc8652374796c2` established all eight fixed
  claims; finding S6-A35-F01 is `verified-closed` (household detail/metadata
  serve `TitleA`/`general`; no post-approval location id; content/download and
  gallery preview of the new location return the unknown-location `404` before
  any open; gallery membership without a publication row; approved cover bytes
  and ETag dynamically demonstrated with no fallback; the R7 LEAD
  `SnapshotTitle`-only result; non-weakening and inventory stability
  established). Focused subset `281 passed`, one synthetic probe passed under
  `/tmp/kronika-one-product-s6-reaudit` and was removed; candidate unchanged;
  declared route PASS. Orchestrator acceptance: the corrected S6 candidate is
  accepted (`acceptance-PASS`); acceptance budget for this correction consumed
  (one primary fresh acceptance). Issued the publication grant
  `40_publication_00.md` (session 40 / exchange 01, fresh-worker-session,
  Bounded Publication Worker, phase publication, native planning mode
  not-used, manual Cooperator delivery, High, independence no), SHA-256
  `618a94df1264b8c1144252a61190faaa1c3f63aaa6edeb6021c18b503bc073a8`:
  publish exactly `0d0d8c88bf88bf8454751a0205bc8652374796c2` to
  `refs/heads/main` of `https://github.com/cisarik/framenest.git` by guarded
  fast-forward, non-force, single refspec, with direct readback; the feature
  branch remote stays `38e7bee…`; no deployment, no closure. Report destination
  `40_report_00.md` (absent at issuance). After a PASS: the NUC routine release
  update to `0d0d8c8…` (separate Cooperator grant; precondition: the three
  `FRAMENEST_NUC_SSH_*` names exported in the MacBook environment), then
  S4-B -> S7-P -> S8 -> S9 -> S10.

- **2026-09-28 — S6 publication PASS; public main now `0d0d8c8`; NUC release
  update grant issued (session 41).** `40_report_00.md` (SHA-256
  `fdf511be0cb11c6b424fc765dd148fd6545ed8d3873b0f780a984a1a60f2d379`, status
  PASS, publication-PASS, coordinates 40/01) reconciled and independently
  re-verified by the Orchestrator with direct `git ls-remote`: public
  `refs/heads/main` of `cisarik/framenest` =
  `0d0d8c88bf88bf8454751a0205bc8652374796c2` (fast-forward from `40e51cb2…`);
  the feature branch remote remains `38e7bee…` and the two other heads are
  unchanged (`26d28b16…`, `7ff6546f…`); local branch `feat/kronika-one-product`
  clean at `0d0d8c8…`; AP pin `73e20ef…`; no feature-branch push, no force, no
  deployment. The accepted S6 chain (records, AP pin bump, S6-A35-F01
  correction) is public on main. Issued the NUC routine release update grant
  `41_deployment_00.md` (session 41 / exchange 01, fresh-worker-session,
  Bounded NUC Deployment, phase deployment, native planning mode not-used,
  manual Cooperator delivery, High, independence no), SHA-256
  `2b999d7f8d16436bb5f05769e6dc224d9037157924ba10abc40451215f59f089`: one
  exact temporary detached checkout of `0d0d8c8…`, canonical
  `framenest-release` `status`/`check`/`deploy` (expected migration
  continuation `0033` -> `0034`), return checkout to
  `feat/kronika-one-product`, read-only as-left capture; capture stays parked
  (pointer `94e605c…`); no DB reset; no `sudo -v`/`-K` by the Worker.
  Report destination `41_report_00.md` (absent at issuance). Cooperator
  preconditions before dispatch: export the three `FRAMENEST_NUC_SSH_*` names
  in the launch environment and establish the NUC sudo timestamp outside the
  Worker (release manually afterwards). After a PASS: S4-B -> S7-P -> S8 ->
  S9 -> S10.

- **2026-09-28 — NUC release update exchange 41/01 BLOCKED: macOS worker-gate
  agent-discovery gap; decision requested.** `41_report_00.md` (SHA-256
  `3a3c2b5d3092d4ac0b9d3026112b42281502045bfd63e27e24c7392864d46cda`, status
  BLOCKED, coordinates 41/01) stopped at Step 0 before any SSH, checkout,
  deploy or host contact: the three `FRAMENEST_NUC_SSH_*` names were set, but
  `scripts/operator/network/framenest_nuc_worker_gate.fish --probe` printed
  `ssh-agent: absent` and exited 1; `sudo -n true` was not reached and no
  `sudo -v`/`-K` was run. Orchestrator read-only root cause: the MacBook has
  no `gpgconf` anywhere (no GnuPG installation; a stale
  `~/.gnupg/S.gpg-agent.ssh` socket exists with no `gpg-agent` process), so
  `_attach_agent` cannot discover an agent on the gate's trusted path
  `/usr/sbin:/usr/bin:/sbin:/bin`. The working route is the native macOS
  launchd `ssh-agent` (`/usr/bin/ssh-agent -l`, one loaded key) exposed via the
  ambient `SSH_AUTH_SOCK`; the Cooperator's direct `ssh framenest-nuc true`
  succeeds through it, but the gate deliberately reconstructs the socket via
  `gpgconf` and fails closed. The repository gate and public refs matched; the
  feature branch stayed clean at `0d0d8c8…`; release `0d0d8c8…` is not
  deployed. Decision requested: a bounded Darwin agent-discovery correction in
  the gate (recommended; strict validation of the launchd socket plus contract
  tests, then a renewed deployment grant) versus an interim Cooperator-executed
  deployment on the unchanged route. S4-B native provider runtime stays after a
  deployment PASS.

- **2026-09-28 — COOPERATOR DECISION: fix the worker gate for macOS; bounded
  correction issued (session 42).** Chosen route A. Orchestrator read-only
  diagnosis confirmed: the MacBook has no `gpgconf` (no GnuPG installation; the
  `~/.gnupg/S.gpg-agent.ssh` socket is stale, no `gpg-agent` process), while
  the native launchd `ssh-agent` holds the NUC key and the ambient
  `SSH_AUTH_SOCK` is a user-owned Unix socket under
  `/private/var/run/com.apple.launchd.…`. Issued the bounded correction
  `42_correction_00.md` (session 42 / exchange 01, fresh-worker-session,
  Bounded Correction Worker, phase correction, native planning mode not-used,
  manual Cooperator delivery, High, independence no), SHA-256
  `8e76c56f8a7271a7e3a3cd14c017ccca74deda6f4c635077a0db4f36cd2cca52`:
  Darwin-only validated fallback in `_attach_agent` (trusted `gpgconf` first;
  else absolute socket, no `..`, `test -S`, owner match, realpath under
  `/private/var/run/com.apple.launchd.`, `ssh-add -l` liveness 0/1 accepted);
  Linux and gpgconf behavior byte-compatible; no socket/identity printing;
  no other validation weakened; new causal test fails first; the parked
  ambient `FRAMENEST_NUC_SSH_*` test interference hardened in the same file
  (test isolation only); allowlist: the gate, the gate test file, the operator
  network contract, the network README and the worker execution contract, only
  as needed; one local commit
  `fix(operator): discover the macOS launchd ssh agent in the worker gate`;
  no push. Report destination `42_report_00.md` (absent at issuance). After a
  PASS: a separate fresh focused re-audit of the corrected exact SHA, then
  publication, then the renewed NUC deployment grant (which must target the
  new published main including the gate fix), then S4-B.

- **2026-09-28 — Worker-gate correction 42/01 PASS; focused re-audit issued
  (session 43).** `42_report_00.md` (SHA-256
  `45335efdc59516455b90e69f6fc187e2433773f3adefb36c3a2610bd045d975a`, status
  PASS, implementation-PASS, coordinates 42/01) reconciled and re-verified
  read-only by the Orchestrator: commit
  `665a565bc1279690ce8dacade37103fa3e0aaddc` (parent `0d0d8c8…`, tree
  `043b811cf82b54cff05026a90b3b15ee46609475`, subject
  `fix(operator): discover the macOS launchd ssh agent in the worker gate`);
  exactly the five allowlisted paths changed; clean; branch three commits ahead
  of the public feature branch; nothing pushed; AP pin unchanged. Red
  `3 failed, 57 passed` on the unfixed gate; green `60 passed`; the causal
  Darwin tests fail-first; `test_ssh_gate_rejects_missing_required_values`
  now clears the four `FRAMENEST_NUC_SSH_*` names for the invoked gate process
  (test isolation only), removing the parked ambient-default interference for
  this file. Issued the focused independent re-audit `43_acceptance_00.md`
  (session 43 / exchange 01, fresh-worker-session, Fresh Independent Audit,
  phase acceptance, native planning mode not-used, manual Cooperator delivery,
  High, required-fresh-independent), SHA-256
  `f2d6e3930c391293480026863b2c48e11ce04dccbfb49bf081814723b525ff6d`:
  six fixed claims (identity/containment and leak hunt; discovery order and
  Darwin trust rule read from the source; the live production `--probe`
  end-to-end missing evidence; negative production probes with a synthetic
  invalid socket and unset `SSH_AUTH_SOCK`; the targeted contract suite
  `60 passed`; non-weakening and doc truthfulness), candidate `665a565…`,
  declared route plus direct gate probes under
  `/tmp/kronika-one-product-gate-reaudit`, no NUC contact, no full suite.
  Report destination `43_report_00.md` (absent at issuance). After a PASS: a
  separate Cooperator publication grant to main, then the renewed NUC
  deployment grant targeting the new published main (including the gate fix),
  then S4-B.

- **2026-09-28 — Worker-gate re-audit 43/01 acceptance-PASS; F01 correction
  issued (session 44).** `43_report_00.md` (SHA-256
  `704ba0dba6c0cb7b3b085f8ad73320e4093f33a75761722df90bb60599840f74`, status
  PASS, acceptance-PASS, coordinates 43/01) reconciled and re-verified
  read-only: independent focused re-audit of `665a565…` established all six
  claims — identity/containment and leak hunt clean; the gpgconf-first order
  and the Darwin trust rule verified from the source; the **live production
  probe** printed exactly `ssh-agent: ready` exit 0 (the exchange-41 failure is
  `verified-closed`); synthetic regular-file and unset probes printed exactly
  `ssh-agent: absent` exit 1 with no echo; the targeted contract file `60
  passed`; non-weakening and docs truthful. One open low-severity finding F01
  (`Final-symlink ownership check lags test -S`): the Darwin ownership
  comparison uses `stat -f %u` without following a final symlink while
  `test -S` follows it; recorded `correction-required` with the Orchestrator as
  approver; the live socket's final component is not a symlink, so the accepted
  claims hold and F01 is non-blocking to acceptance. Orchestrator decision:
  correct F01 before publication because the fix is mechanical and the gate is
  about to become the operational NUC route. Issued the bounded correction
  `44_correction_00.md` (session 44 / exchange 01, fresh-worker-session,
  Bounded Correction Worker, phase correction, native planning mode not-used,
  manual Cooperator delivery, High, independence no), SHA-256
  `951e2598b8b6e3acf1122c5e734187a2d3f51809c9ab84f2d4e33b3fba9c3a8f`:
  ownership comparison follows the final symlink (`stat -L -f %u` or
  equivalent), all other checks and the `--probe` contract unchanged, one
  causal regression that fails on the parent, allowlist exactly the gate and
  its contract test file, one local commit
  `fix(operator): follow symlinks in the gate agent ownership check`, no push.
  Report destination `44_report_00.md` (absent at issuance). After a PASS: a
  separate fresh scoped re-audit of the corrected exact SHA, then the
  Cooperator publication grant to main, then the renewed NUC deployment grant,
  then S4-B.

- **2026-09-28 — F01 correction 44/01 PASS; scoped re-audit issued
  (session 45).** `44_report_00.md` (SHA-256
  `9e36d8950b2c369422e820ca99253a072a7949dde384694f69d5a2adce2241c3`, status
  PASS, implementation-PASS, coordinates 44/01) reconciled and re-verified
  read-only by the Orchestrator: commit
  `89a402981a9eac83646199c77984c3fc21c0744d` (parent `665a565…`, tree
  `27cf6ba02e9c08f27151976aa2b259bea0d60dcb`, subject
  `fix(operator): follow symlinks in the gate agent ownership check`); exactly
  the two allowlisted paths (gate + contract test file), +34/−1; the ownership
  line changed from `$stat_bin -f %u "$sock"` to
  `$stat_bin -L -f %u "$sock"`; Red `1 failed, 60 passed`, Green `61 passed`;
  clean worktree; no push; AP pin unchanged. Issued the scoped independent
  re-audit `45_acceptance_00.md` (session 45 / exchange 01,
  fresh-worker-session, Fresh Independent Audit, phase acceptance, native
  planning mode not-used, manual Cooperator delivery, High,
  required-fresh-independent), SHA-256
  `d6effda79a359e41a379bd92d828a56cd0d2c5b70a4eb9ef5ef7263f29d405a2`:
  five fixed claims (identity/containment; F01 closed with parent/candidate
  causal comparison; no other behavior change; targeted suite
  `61 passed`; live production probe non-regression `ssh-agent: ready` plus one
  synthetic regular-file negative), candidate `89a4029…`, probe root
  `/tmp/kronika-one-product-gate-f01-reaudit`, no NUC contact. Report
  destination `45_report_00.md` (absent at issuance). After a PASS: the
  Cooperator publication grant to main (feature tip `89a4029…`), then the
  renewed NUC deployment grant on that published main, then S4-B.

- **2026-09-28 — COOPERATOR DIRECTIVE: autonomous Orchestrator execution from
  this point (dispatch loop ended).** The Cooperator replaced manual
  fresh-Worker dispatch for the remaining steps of this whole with autonomous
  Orchestrator execution ("odteraz vykonaj sám, čo si chcela od Workera").
  Consequences recorded truthfully: acceptance and audit reports produced from
  here on are non-independent and say so; the trace keeps the normal filenames
  and coordinates; the standing security boundaries (no `private/**`, no
  provider contact without authority, no credentials handling, no `sudo -v` or
  `sudo -K` by the executor, sanitized reporting) remain in force; the NUC
  sudo timestamp remains Cooperator-established and manually released.

- **2026-09-28 — F01 scoped re-audit executed (45/01); PUBLICATION pending.**
  Executed by the Orchestrator under the autonomy directive.
  `45_report_00.md` records `acceptance-PASS` (non-independent) for
  `89a402981a9eac83646199c77984c3fc21c0744d`: identity and the two-path delta
  verified; the parent lacks `-L` while the candidate has `stat -L -f %u`; the
  regression test exists; `ap project check` PASS; targeted contract file
  `61 passed`; direct production probe `ssh-agent: ready` exit 0; synthetic
  regular-file and unset probes `ssh-agent: absent` exit 1 with no echo; probe
  root removed; leak hunt clean. F01 `verified-closed`. No new finding.
  Next: publish `89a4029…` to `refs/heads/main` (non-force fast-forward) with
  direct readback, then the NUC routine release update to the new main.

- **2026-09-29 — Publication of `89a4029…` executed; NUC routine update to
  `89a4029…` attempted, hit a private-catalog mode conflict, recovered per the
  documented schema-jump annex; deployment PASS; host unit fix `3f5dc5c…`
  published.** Execution was autonomous per the Cooperator directive.
  Publication: public `main` fast-forwarded `0d0d8c8… -> 89a4029…` (non-force,
  readback verified). NUC routine update: the first `deploy --yes` stopped at
  exit 20 after atomically publishing the target tree, because the same-schema
  DB gate (`framenest-db status` on the target, S6 code) failed closed: the
  accepted S6 private-catalog rule requires the database parent directory to be
  exactly `0700`, but the NUC's `/var/lib/framenest` was `0755`. A `chmod 700`
  alone was not durable: the unit's `StateDirectory=framenest` used systemd's
  default mode, so every service (re)start reset the directory to `0755`; a
  first cutover attempt failed at pre-restart readiness and the previous
  release's restart loop (schema ahead) left `framenest.service` in
  `activating/auto-restart` until stopped. Repository fix: unit source gained
  `StateDirectoryMode=0700` with a contract assertion
  (`tests/contract/test_fedora_systemd_service.py`), committed as
  `3f5dc5c469e19802aa3411988aa022b158de2ab6` and published to `main`
  (`89a4029… -> 3f5dc5c…`, non-force, readback). Host fix: the unit was
  installed on the NUC and hash-verified byte-identical to the repository
  source; `daemon-reload`; state directory `0700`; migration executed from the
  target tree (`0034 at_head`); cutover via the documented
  `framenest-release rollback --release 89a4029… --yes` exited 0. Final state:
  web release `89a4029…`, capture `94e605c…` unchanged and parked
  (`browser_unavailable`, jobs 0/0), service active, `database_revision` `0034`,
  backup readiness `ready`, state dir `700`. Trace pair:
  `46_deployment_00.md` + `46_report_00.md`. Deviations: two tightening host
  mutations required by the accepted S6 policy (state-dir mode, unit install);
  brief service downtime during the schema-ahead window; no listener capture
  (address hygiene); non-independent execution. Sudo timestamp consumed; the
  Cooperator releases it manually. Next: S4-B native provider runtime per
  `25_report_00.md` and `ROADMAP.md`.

- **2026-09-29 — S4-B implementation plan frozen (47/01); implementation
  begins next.** Orchestrator-authored under autonomy mode:
  `47_planning_00.md` + `47_report_00.md` fix the scope (provider runtime only;
  no HTTP/rendering/UI), migration `0035` design (`research_requests`, the
  single-row `research_active_slot`, `research_operations`, and
  `research_budget_holds`; populated-downgrade refusal; no backfill), the exact
  twenty-path allowlist, the module placement (`application/research.py`
  coordinator, two SQLite repositories, `infrastructure/ai/openai_responses.py`
  against an injectable transport, inert composition wiring, credential
  drop-in `deploy/systemd/framenest-research-credential.conf`, deployment-doc
  paragraph), the test matrix (coordinator units with fake ports, adapter
  contract against a fake transport, `0034`->`0035` migration integration,
  repository/budget atomicity, disabled-startup), and the validation route
  with baseline `3f5dc5c…`. Basis read-only: `25_report_00.md` sections 2–4 and
  the existing S4-A surface (`domain/research.py`, `application/ports/research.py`,
  `research_registry.py`, `research_configuration.py`, the provider contract
  test). Planned implementation order: (1) migration `0035` + schema mirror +
  migration tests; (2) repositories + tests; (3) coordinator + tests;
  (4) adapter + tests; (5) composition, credential source, docs; then targeted
  validation. Any allowlist expansion returns to the trace before the edit.

- **2026-09-29 — S4-B implementation step (1) complete: migration `0035` +
  schema mirror + migration tests (commit `df44c2d`); allowlist amendment 1.**
  Executed autonomously. `0035_research_requests_and_accounting.py` creates
  `research_requests`, the single-row `research_active_slot`,
  `research_operations` and `research_budget_holds` with bounded checks,
  named constraints/indexes, FK to `kronika_records`, unique
  `(owner_login_key, client_request_id)`, and an empty-table refusal on
  downgrade (atomic: a refused downgrade leaves the database at `0035`).
  `catalog_schema.py` mirrors the four tables. New
  `tests/integration/persistence/test_research_requests_migration.py` covers
  head `0035`, empty upgrade/downgrade/re-upgrade, populated refusal with row
  retention, malformed-row checks, operation/budget constraints and the
  single-row slot. Migration-head ripple: current-head assertions advanced to
  `0035` in 20 additional test files (allowlist amendment 1 recorded in
  `47_planning_00.md`; historical targets untouched); the S6
  populated-downgrade assertion now expects `0035` because the refusal
  rolls back the whole chain, and the upload-session table union gained the
  four tables. Targeted affected set: `198 passed`; the only failure is
  pre-existing macOS debt — `tests/integration/test_process_sigterm_lifecycle.py`
  hardcodes `/home/agile/Projects/framenest/.venv/bin/python` and fails before
  any assertion (ledger candidate, not repaired; the file's head assertion was
  nevertheless advanced correctly). Next: step (2) repositories (`research
  request` + `budget ledger`) with their tests.

- **2026-09-29 — S4-B implementation step (2) complete: runtime repositories
  (commit `5417fb8`).** Executed autonomously. `application/ports/research.py`
  gained `ResearchRequestRow` (domain record + storage-only fields),
  `ResearchStoreError` (stable `ResearchErrorCode`) and the
  `ResearchRuntimeRepository` protocol (get/find-by-client/admit/save/active
  slot). `SqliteResearchRequestRepository` admits atomically under
  `BEGIN IMMEDIATE`: duplicate `(owner, client)` with the same fingerprint
  returns the existing row, a different fingerprint raises
  `E_IDEMPOTENCY_CONFLICT`, a held slot raises `E_BUSY`, the full allowance is
  reserved, and the request row + hold + slot update commit as one unit;
  `save` persists lifecycle/cleanup/accounting/handle/checkpoint fields and
  releases the slot on any terminal state. `SqliteResearchBudgetLedger`
  implements reserve/reconcile/consumed over UTC day/month keys; reconciled
  usage replaces the reservation, unknown usage consumes it (never zero), and
  a refusal rolls the whole admission back. Migration `0035` gained five
  profile-snapshot columns (`tool_allowlist_json`, `background`,
  `prompt_max_utf8_bytes`, `answer_max_utf8_bytes`, `citation_count_max`) so a
  stored row reconstructs the exact `ServerSelectedProfile` and
  `ApprovedResourceLimits`; the schema mirror and the migration test helper
  were updated accordingly. New repository test file with seven cases
  (roundtrip, idempotency/conflict, busy/slot release, budget refusal
  rollback, reconcile freeing budget, unknown accounting, checkpoint/handle
  saves). Targeted affected set: `210 passed`. Next: step (3) the research
  coordinator in `application/research.py` with fake-port unit tests.

- **2026-09-29 — S4-B implementation step (3) complete: the research
  coordinator (commit `a9ec1f1`).** Executed autonomously. `application/research.py`
  implements `ResearchCoordinator` over the injected ports: admission
  (selection snapshot via `select`, content fingerprint over owner/kind/prompt
  and the accepted policy, duplicate client key returns the existing request,
  different fingerprint → `E_IDEMPOTENCY_CONFLICT`, full reservation +
  request + slot in one atomic admission); submission persists a durable
  `SUBMITTING` marker **before** the network call, maps PENDING/RUNNING to
  RUNNING with the opaque handle, and maps a transport exception or UNCERTAIN
  to terminal `SUBMISSION_UNKNOWN` (`recover()` does the same for a crash
  mid-submit — never resubmits blindly); polling validates COMPLETE evidence,
  persists a normalized checkpoint and reaches `SAVED` through the
  `ResultCompletion` port, with a checkpoint-based completion retry while a
  failure keeps `VALIDATING`; cancellation acknowledges locally before the
  remote call, confirms `CANCELLED`, and a cancellation committed before
  result-save prevents finalization; the deadline produces terminal `TIMEOUT`
  with a best-effort remote cancel; `release_remote_pending()` deletes remote
  responses for terminal rows with a handle via the new repository
  `list_cleanup_pending`; every terminal transition reconciles the budget hold
  (reconciled usage from the price schedule or conservative UNKNOWN).
  `ResearchSelectionSnapshot` (now with the daily/monthly budgets) and
  `ResearchSelectionError` moved to `application/ports/research.py`; the
  registry re-exports them and fills the budgets, so the coordinator never
  imports infrastructure. New coordinator tests: nine cases with a fake
  provider and fake completion over the real SQLite stores; regression set
  `138 passed`. Deferred within S4-B and recorded: per-attempt
  `research_operations` rows (table exists; writes arrive with the runtime
  wiring/S7-P accounting) and binding `record_id` from the completion port
  (S7-P). Next: step (4) the OpenAI Responses adapter against an injectable
  transport with fake-transport tests.

- **2026-09-29 — S4-B implementation step (4) complete: the OpenAI Responses
  adapter (commit `34cb2f5`).** Executed autonomously.
  `infrastructure/ai/openai_responses.py` implements the `ResearchProvider`
  port over an injectable bounded-JSON transport seam
  (`ResearchJsonTransport`): `describe()` is network-free (registry
  descriptor); `submit` builds a bounded, server-selected-only body (model,
  input, web_search tool, `tool_choice=required`,
  `parallel_tool_calls=false`, `max_tool_calls`, `max_output_tokens`,
  `reasoning.effort`, `background`, `store`) with a request bound from the
  approved prompt limit, maps 200/201/202 + `id` to a RUNNING observation
  with an opaque handle, and a missing credential to
  `E_NOT_CONFIGURED` without any network call; `poll` maps
  queued/in_progress to RUNNING, completed to a parsed `ResearchAnswer`
  (output text, url-citation annotations, web-search-call count, usage
  details) gated by `completion_error` (refusal → REFUSED, missing web search
  → `E_NO_WEB_EVIDENCE`, incomplete → `E_INCOMPLETE_RESULT`), and maps
  transport failures and 404 to `E_PROVIDER_UNAVAILABLE`/`E_RESULT_EXPIRED`;
  `cancel` posts to `/cancel` and confirms CANCELLED; `release_remote`
  deletes the response and treats a missing one as already deleted. Errors
  carry stable codes only — no provider bodies, credentials or reasoning text.
  `transport.py` gained `delete_json`. The coordinator now maps
  `E_INCOMPLETE_RESULT` failures to the `INCOMPLETE` lifecycle state. New
  adapter tests with a fake transport (body shape, credential absence,
  completion parsing, evidence gating, error mapping, cancel/release
  outcomes); AI unit suite `373 passed`; focused set `62 passed`. Next:
  step (5) inert composition wiring, the credential deployment source and the
  deployment-doc paragraph.

- **2026-09-29 — S4-B implementation COMPLETE (step 5, commit `0a7d3f0`);
  chain `df44c2d..0a7d3f0`.** Executed autonomously.
  `build_research_runtime` in `application.py` builds the coordinator only
  when the non-secret AI configuration enables research; construction is
  network-free; `recover()` is guarded so an older catalogue never blocks
  startup; the runtime is attached as `app.state.research_runtime`. The
  credential deployment source `deploy/systemd/framenest-research-credential.conf`
  was added and named in the deployment doc sentence. Contract composition
  tests were appended to the allowlisted provider-contract file; final S4-B
  validation batch `168 passed`. Trace pair: `48_implementation_00.md` +
  `48_report_00.md`. S4-B delivers: migration `0035` (+ schema mirror), ports
  runtime row + selection snapshot/error, request/slot repository, budget
  ledger, coordinator, OpenAI Responses adapter over an injectable transport,
  inert composition and the credential source. Recorded deferrals: per-attempt
  `research_operations` rows, `record_id` binding and the atomic Q/A save
  (S7-P completion port; completed results wait in `VALIDATING`), HTTP/UI
  (S7-P/S8), live provider calls and credentials (separate authority),
  operator overshoot block. Public `main` is still `3f5dc5c…`; the S4-B chain
  is unpublished; the NUC runs the `89a4029…` release. Next per `ROADMAP.md`:
  S7-P (common completion and rendering), then S8, S9, S10; publication and
  independent acceptance of the S4-B chain are separate Cooperator decisions.

- **2026-09-29 — S7-P implementation progress: WP1 + WP2 (commits `8a277a3`,
  `f1ec367`).** Executed autonomously. WP1: capabilities `research.run`
  (user+admin) and `records.approve` (admin) in `domain/identity_access.py`;
  new `application/document_rendering.py` renders the bounded Markdown subset
  to escaped HTML (raw HTML escaped, safe URL schemes only, no dependency);
  eight rendering tests and capability membership assertions. WP2:
  `SqliteResearchResultCompletion` in `record_repository.py` creates the
  document, the common record (server-derived owner, kind search/research,
  private) and the `research_requests.record_id` binding in one immediate
  transaction, idempotent on exact replay; the composition now wires it
  instead of the placeholder; the coordinator reloads the row after a
  successful receipt so the terminal save cannot clobber the binding.
  Allowlist amendment 1 for S7-P: `public_published_application.py` carries
  the `REQUIRED_PUBLIC_SCHEMA_REVISION` (`0034` -> `0035`), a missed ripple
  from the S4-B migration step, fixed in `f1ec367`. Validation: rendering +
  capability `35 passed`; completion + coordinator + authorization +
  public-uds `42 passed`. Next: WP3 research request APIs.

- **2026-09-29 — S7-P WP3 complete: research request APIs (commit `c0a5288`).**
  Executed autonomously. `adapters/api/research_api.py` exposes
  `GET /api/research/capabilities` (selection, limits, retention notice; no
  live probe; disabled-safe), `POST /api/research-requests` (202 + nudge),
  `GET /api/research-requests` (own history, paged),
  `GET /api/research-requests/{id}` (owner or admin, with progress nudge),
  `POST /api/research-requests/{id}/cancel` (owner or admin) and
  `GET /api/admin/research-requests`; missing identity 401, capability 403,
  foreign/nonexistent indistinguishable 404, typed `ResearchStoreError`
  mapping (503/409/429/422/500), and `E_DISABLED` refusal when the runtime is
  absent while history reads still work. Repository list/count methods added.
  Two defects found and fixed en route: the coordinator's default
  `new_operation_id` produced a UUID that the schema rejects (now
  `op-<32 hex>`), and the capabilities payload used the wrong settings field
  name. Tests `tests/contract/test_research_requests_api.py` (6 cases,
  synthetic alice/bob/ada, disabled runtime, idempotency, cancel); focused
  set `34 passed`. Next: WP4 records APIs + access inventory.

- **2026-09-29 — S7-P implementation COMPLETE (WP4 + composition + inventory;
  commit `74f2a40`); chain `8a277a3..74f2a40`.** Executed autonomously.
  `records_api.py` exposes `GET /api/my/records`, `/api/timeline`,
  `/api/records/{id}`, `/api/records/{id}/render` (escaped HTML with
  `nosniff` and a restrictive CSP), `/api/admin/records` and
  `POST /api/admin/records/{id}/approval` (approve/withdraw with expected
  version; `reject` refused 422 because no rejected state exists — recorded
  for S8/S9). Twelve new route policies in `tailscale_ingress.py`; both new
  routers registered in `create_app` over the owned engine; the executable
  access inventory regenerated for schema head `0035` with per-route positive
  and negative behavioral tests. Behavioral evidence: owner detail/render,
  household approved projection + Timeline after administrator approval,
  stale-version conflict, user approval denial, anonymous denial, injection
  safety. Final S7-P batch `307 passed`. Trace pair:
  `50_implementation_00.md` + `50_report_00.md`. Recorded deferrals:
  `consent_version` validated but not stored; lists summary-only; research
  progress nudged synchronously (no background loop; runtime disabled by
  default, no live calls). Public `main` remains `3f5dc5c…`; the S4-B and
  S7-P chains are unpublished. Next per `ROADMAP.md`: S8 product UI
  (Timeline landing, personal history, Search/Research forms, administrator
  review); publication, independent acceptance and S9 remain separate
  Cooperator decisions.

- **2026-09-29 — FULL PUBLICATION + independent audit issued + restoration
  handout written (Cooperator directive).** Directed by the Cooperator
  ("publikuj všetko nepublikované sám, potom vydaj prompt pre nezávislý audit,
  potom handout pre fresh Orchestratora; daj maximum"). Publication: non-force
  fast-forwards with direct readback — public `main` `3f5dc5c… -> 74f2a40…`
  and public `feat/kronika-one-product` `38e7bee… -> 74f2a40…`; the two other
  heads unchanged (`26d28b16…`, `7ff6546f…`). Public `main` now carries the
  full accepted S6 chain, the AP pin bump, the worker-gate Darwin fix and its
  F01 correction, the systemd/state-directory correction, S4-B and S7-P.
  Issued the fresh independent E3/R3 audit `51_acceptance_00.md` (session 51 /
  exchange 01, fresh-worker-session, Fresh Independent Audit, phase
  acceptance, native planning mode not-used, manual Cooperator delivery,
  Extra High, required-fresh-independent), SHA-256
  `78b8a24489ade6917aec5ebbd8ed7f2715c9502a75666b3de91171c375619d9a`: eleven fixed claims over the ten-commit delta
  `89a4029..74f2a40` (containment and inert-by-default posture; migration
  `0035` integrity and ripple; repository/budget atomicity; coordinator
  lifecycle; adapter boundary; atomic completion and binding; authorized HTTP
  surfaces; rendering/capabilities safety; route-policy and inventory
  completeness; systemd correction; non-regression), the declared focused
  subset and synthetic probe root
  `/tmp/kronika-one-product-verify-74f2a40`, no NUC contact, no live provider
  calls. Report destination `51_report_00.md` (absent at issuance). Wrote the
  fresh-Orchestrator restoration handout `04_handout.md` (SHA-256
  `f97383797c1748a677b3c55e1dc7f3c510d0f421cea508908d93631940ba4b65`) covering the verified state, the audit reconciliation
  step, S8 scope and UI constraints, S9/S10 and parked items, the NUC release
  runbook with the private-catalog lesson, environment debts, working-mode
  guidance, ledger candidates, STOP rules and the paste seed. Sessions 01-51
  are used; the next genuinely fresh session ordinal is 52. The whole remains
  open; capture stays parked.

- **2026-09-29 — audit reconciliation, F01 fix, macOS portability fix, final
  publication and NUC update to main (Cooperator directive).** Directed by
  the Cooperator ("prečítaj si report, čo vieš oprav sám; ďalšie audity už
  nerob; finálny handout pre fresh Orchestratora, ktorý začne Plánovačom v
  natívnom plánovacom móde"). `51_report_00.md` accepted as PASS: eleven fixed
  claims established over `89a4029..74f2a40` (340 focused tests green;
  synthetic probes; no NUC contact; no live provider calls), one open low
  finding F01 (unbounded blockquote recursion in `render_markdown`), F02
  considered and rejected, plus two recorded limitations (living docs still
  naming schema head `0034`; a 38-char tree-string transcription defect in
  the audit prompt itself). Dispositions executed by the Orchestrator:
  - `8e5c374` bounded quote nesting in the safe document renderer (depth cap,
    regression test; rendering set 13 passed).
  - `7be040e` aligned README/PRODUCT/SPEC/SECURITY/ROADMAP and their two
    locking tests to schema head `0035`, made
    `docs/WORKER_EXECUTION_CONTRACT.md` and its test host-agnostic
    (`<physical-repository-root>`), and updated the AP-upgrade ledger test to
    expect the two recorded entries.
  - `ade1169` resolved 60/62 macOS environment failures: Homebrew fallbacks
    for ffmpeg/ffprobe (media tools), node (capture CLI), fish (AI deployment
    helper) and a shared `tests/support/tooling.py` for node/fish/poetry
    spawns; Darwin `killpg` EPERM handled in the media process runner and its
    test cleanup; AP pin test realigned to `73e20ef…`; the AP envelope macOS
    key `__CF_USER_TEXT_ENCODING` allowed; capability ripple `research.run`.
  Broad suite on the final candidate: `4080 passed, 1 failed, 9 skipped`
  (8m47s); the single failure is the macOS-only YouTube fake-demo stall
  (`handed_off`/`publish_pending` then `YOUTUBE_WAIT_TIMEOUT` after the CLI's
  20 s wait; the manual-upload path passes) recorded as a bounded diagnostic
  lead for the successor; the 9 skips are opt-in gates (real media tools,
  real Poetry on PATH, live NVIDIA smoke). Publication: non-force
  fast-forwards with direct readback, public `main` `74f2a40… -> ade1169…`
  and public `feat/kronika-one-product` `74f2a40… -> ade1169…` (tree
  `f266df7205ddea5b83de7e6cd8313512ce70bcb1`); the two other heads unchanged
  (`26d28b16…`, `7ff6546f…`). NUC routine update to `ade1169…` through the
  documented schema-jump continuation: `deploy --yes` stopped with
  `migration-required` (exit 13; live DB `0034`, target head `0035`), the
  annex then verified the target tree, removed only the three lock artifacts
  plus the empty lock directory, migrated from the target tree
  (`0035 at_head`) and cut over via `rollback --release … --yes`; final NUC
  state: web release `ade1169…` (equals public main), database `0035`,
  `framenest.service` active, `/var/lib/framenest` `700`, capture release
  `94e605c…` unchanged and parked (`browser_unavailable`, 0 jobs, 0
  chrome/chromium, NRestarts=0), `tailscaled` active. The MacBook checkout
  returned to `feat/kronika-one-product` at `ade1169…`, clean.
  `04_handout.md` rewritten for the successor: final refs and the full
  thirteen-commit ledger, the audit result and F01 disposition, a
  **Planner-first protocol** (next action is an S8 Planner grant with native
  plan mode REQUIRED, fresh Worker session 52), detailed S8 UI/UX planning
  inputs over the existing shell and APIs, NUC worked example, remaining
  single test debt, ledger candidates and STOP rules; new SHA-256
  `646e96d69a25be4c09ac2d9ec0dc576e2cda07ca973ad8e3246ae65c832daf95`
  (supersedes the pre-audit draft `f9738379…`). The whole remains open;
  capture stays parked; next per `ROADMAP.md` is S8 via the Planner grant.

- **2026-09-29 — Fresh Orchestrator restored (`04_handout.md`); S8 Planner
  grant issued (session 52 / exchange 01).** Read-only restoration re-verified
  every claimed state: local `feat/kronika-one-product` at
  `ade1169b4ba079bb1df540a929572ca58e777d16` (tree
  `f266df7205ddea5b83de7e6cd8313512ce70bcb1`, parent `7be040e…`, clean), AP
  gitlink and `.ap` HEAD `73e20ef80b88700d5fcbc397cd8edd4fc425869f`, `.venv`
  from uv CPython 3.13.14 created by Homebrew Poetry 2.5.1; direct
  `git ls-remote` confirmed public `main` = `feat/kronika-one-product` =
  `ade1169…` and the other two heads unchanged; `04_handout.md` SHA-256
  `646e96d…` matches. NUC verification through the worker gate: `--probe`
  `ssh-agent: ready`; `/opt/framenest/current` ->
  `/opt/framenest/releases/ade1169…`; `framenest.service` active;
  `/var/lib/framenest` mode `700`; host unit carries exactly one
  `StateDirectoryMode=0700`; `tailscaled` active. The parked capture state was
  deliberately not re-read (STOP rules); the predecessor's capture evidence
  stands. Issued the S8 Planner grant `52_planning_00.md` (session 52 /
  exchange 01, fresh-worker-session, Planner, native planning mode required,
  manual Cooperator delivery, Extra High), SHA-256
  `fb3033406c6d38871332e2b8a45764adfc5117aeb5f97cc292ce6dffa950533d`:
  produce the frozen S8 unified Kronika UI/UX plan on the `ade1169…` baseline
  (exact allowlist; page/route and API mapping; component and state design;
  disabled/error UX; accessibility and responsive baseline; test matrix with a
  thin UI regression harness; acceptance route; recommended first
  implementation grant; open Cooperator language/branding questions). Report
  destination `52_report_00.md` (absent at issuance). Next: the Cooperator
  dispatches the prompt into a fresh Agent chat with native Plan mode ON; the
  report is reconciled and the plan frozen, then bounded S8 implementation
  grants follow.

- **2026-09-29 — S8 Planner report reconciled; report persisted; plan frozen;
  S8 implementation grant issued (session 53 / exchange 01).** `52_report_00.md`
  arrived session-delivered as a complete plan with status PARTIAL solely
  because the client Plan Mode prohibited the report-file write; the
  Orchestrator persisted the exact relayed content to the trace (SHA-256
  `d064848b72833db8c0ae8ae525d03fd9242393c419e468e21e2d86f67ccc430f`,
  517 lines), closing the delivery gap without rewriting the report's own
  status. Read-only reconciliation re-verified: baseline unchanged (HEAD
  `ade1169…`, tree `f266df72…`, parent `7be040e…`, clean; AP pin `73e20ef…`);
  both consequential production findings confirmed in code (`audience_me`
  returns `identity: null` on the trusted-loopback composition at
  `application.py` ~1545; `records_api._summary_payload` carries no
  title/category and detail carries question text plus citations but not answer
  text); all 19 existing allowlist paths present; only
  `tests/kronika_ui.test.js` is new; no `ROUTE_POLICIES` change is expected.
  Plan accepted and frozen; section 9's proposal is superseded by the issued
  grant. Cooperator-confirmed presentation decisions recorded by the plan:
  English copy; "Kronika" branding with the existing `FN` monogram retained;
  no package/header/storage-key/deployment/repository renames. Issued the S8
  implementation grant `53_implementation_00.md` (session 53 / exchange 01,
  fresh-worker-session, Fresh Implementation Worker, native planning mode
  not-used, manual Cooperator delivery, High), SHA-256
  `7a276696f4bc595335b556eedf9da5c8b54da022ead4c69e53efb7a65d82f76f`: the
  exact 20-path allowlist; the additive summary/filter and local-identity
  changes; the frozen shell design; the causal test matrix with the new
  `tests/kronika_ui.test.js` harness; exactly one final bounded full JS run;
  no broad Python suite; one local commit
  `feat(kronika): add unified timeline history and review UI`; no push. Report
  destination `53_report_00.md` (absent at issuance). Next: the Cooperator
  dispatches the prompt into a fresh Agent chat with native Plan mode OFF;
  then the fresh independent audit of the exact candidate, publication, NUC
  refresh and Michal's rendered acceptance.

- **2026-09-29 — S8 implementation PASS reconciled; independent audit grant
  issued (session 54 / exchange 01).** `53_report_00.md` (persisted by the
  Cooperator) reconciled and re-verified read-only: commit
  `7f7aae9012d35671b062c8731e9009169501d4d0` (parent `ade1169…`, tree
  `17a559dff621882ac561a9901d20fe5b824508c4`, subject
  `feat(kronika): add unified timeline history and review UI`); delta exactly
  the 20 allowlisted paths (19 modified plus new `tests/kronika_ui.test.js`,
  +3311/-40); no `ROUTE_POLICIES` change; worktree clean; AP pin `73e20ef…`
  unchanged; public `main` and the feature branch remain `ade1169…` (candidate
  local-only; re-checked by the Orchestrator via `git ls-remote`). Spot checks
  confirmed the additive loopback identity echo in `application.py`, the
  summary/filter changes in `records_api.py`, and that the inventory diff is
  the single Timeline projection sentence. Implementation evidence
  non-independent per the grant: reported 416 focused Python passed; 540 JS
  tests with 5 gated skips. Issued the fresh independent audit grant
  `54_acceptance_00.md` (session 54 / exchange 01, fresh-worker-session, Fresh
  Independent Audit, native planning mode not-used, manual Cooperator delivery,
  Extra High, required-fresh-independent), SHA-256
  `8eebde50818855d35d79c8791987b6ea6b9af6164a73348d73dc647233f31884`:
  candidate `7f7aae9`, twelve fixed claims C1–C12 (containment and leak hunt;
  summary projection; Timeline approved-only for every caller; filter
  validation and query correctness; local identity echo; shell routing and
  state isolation; submission idempotency; polling and cancellation; rendering
  isolation; approval flow; route policies and inventory; non-regression), R3
  with authorization and rendering specializations, the declared focused
  Python route and a bounded JS acceptance set, one synthetic probe root
  `/tmp/kronika-one-product-s8-audit`, no correction authority. Report
  destination `54_report_00.md` (absent at issuance). Next: reconcile the
  audit; then publication, NUC refresh and Michal's rendered acceptance per the
  frozen plan's section 8.

- **2026-09-29 — S8 audit PARTIAL reconciled (one medium blocking finding F01);
  bounded correction issued (session 53 / exchange 02).** `54_report_00.md`
  (SHA-256 not separately recorded; persisted by the Cooperator) reconciled:
  candidate `7f7aae9…` identity and containment match; C1–C6 and C8–C12
  established (summary projection; Timeline approved-only for every caller;
  filter validation; local identity echo; shell routing and state isolation;
  polling and cancellation; rendering isolation; approval flow; route policies
  and inventory; non-regression — independent focused Python `416 passed` and
  bounded JS `148 passed`, `0` failed); C7 is partial. Finding
  `KRONIKA-ONE-PRODUCT-S8-AUDIT-F01` (medium, reproduced-dynamic, blocking):
  after a lost POST plus reload, the recovery path restores the stored
  `client_request_id` but the next submit recomputes nothing against the stored
  SHA-256 fingerprint, so re-entering the same question mints a new id and
  server idempotency does not cover the first admission — a possible second
  provider admission and budget use. The audit made no candidate edit; probe
  root `/tmp/kronika-one-product-s8-audit` removed; public refs still
  `ade1169…`. Orchestrator disposition: correction-required; one smallest
  coherent correction authorized, no self-certification, full fresh re-audit
  after the runtime-behavior change. Issued the bounded correction
  `53_correction_01.md` (session 53 / exchange 02, current-worker-session,
  Bounded Correction Worker, native planning mode not-used, manual Cooperator
  delivery, High), SHA-256
  `6853a7df005bdbd45d8fd95c6d98e0cf23b43cfce5094b8ba4cac3c7ce430386`: the
  two-path allowlist (`app.js`, `tests/kronika_ui.test.js`), fingerprint-match
  reuse with fail-closed minting, the two-context shared-storage Red/Green
  regression, bounded JS validation and one local commit
  `fix(kronika): reuse the frozen request id across reload recovery`; no push.
  Report destination `53_report_01.md` (absent at issuance). Next: dispatch to
  the existing session-53 chat with Plan mode OFF; then the fresh independent
  re-audit of the corrected candidate (session 55).

- **2026-09-29 — F01 correction PASS reconciled; fresh independent re-audit
  issued (session 55 / exchange 01).** `53_report_01.md` reconciled and
  re-verified read-only: commit
  `ef9920333013f3f70bf5e3443be2e51814f6b9c3` (parent `7f7aae9…`, tree
  `e4338c2f31e8aff2829351ec107e2d75a165a473`, subject
  `fix(kronika): reuse the frozen request id across reload recovery`); the
  correction commit changes exactly the two allowlisted paths (`app.js`,
  `tests/kronika_ui.test.js`, +99/-10); `kronikaFreezeAttempt` is now async and
  reuses the stored `client_request_id` only when the recomputed SHA-256
  fingerprint (login, kind, exact prompt, consent version) is non-empty and
  equal — otherwise it mints a new id; `kronikaSubmitQuestion` awaits it;
  the existing same-page retry test is untouched. Worker evidence: Red on the
  parent (new regression 1 failed), Green `12 passed`, bounded JS run
  `76 passed`; no Python change. Worktree clean at `ef99203…` (two commits
  ahead); public `main` and feature branch still `ade1169…`; AP pin unchanged.
  Issued the full fresh independent re-audit `55_acceptance_00.md` (session 55
  / exchange 01, fresh-worker-session, Fresh Independent Re-Audit, native
  planning mode not-used, manual Cooperator delivery, Extra High), SHA-256
  `f35e745b7a09d10d8587540de8baf1f6e6677eb556b073391643d719788021f1`:
  candidate `ef99203…`; C1–C12 re-established on the corrected candidate plus
  explicit `KRONIKA-ONE-PRODUCT-S8-AUDIT-F01` closure with the auditor's own
  two-context synthetic probe; correction containment; the declared focused
  Python route and bounded JS set; one synthetic root
  `/tmp/kronika-one-product-s8-reaudit`; no correction authority. Report
  destination `55_report_00.md` (absent at issuance). Next: reconcile the
  re-audit; then publication, NUC refresh and Michal's rendered acceptance.

- **2026-09-30 — S8 re-audit acceptance-PASS reconciled; S8 accepted; a
  feature-branch push observed and classified; publication and NUC pending.**
  `55_report_00.md` reconciled: fresh independent re-audit of
  `ef9920333013f3f70bf5e3443be2e51814f6b9c3` established C1–C12 on the
  corrected candidate and `KRONIKA-ONE-PRODUCT-S8-AUDIT-F01` is
  `verified-closed` with the auditor's own two-context synthetic probe (changed
  prompt, changed login, changed kind, empty fingerprint, missing fingerprint
  and absent `crypto.subtle` all mint a new id; no auto-submit; no prompt in
  storage). Evidence: focused Python `416 passed`; bounded JS `149 passed`,
  `0` failed; probe root `/tmp/kronika-one-product-s8-reaudit` removed; no
  candidate mutation. Orchestrator direct read-only re-verification: HEAD
  `ef99203…`, tree `e4338c2f…`, clean; candidate unchanged. Orchestrator
  acceptance: the S8 slice is accepted (`acceptance-PASS`); the correction
  cycle budget is consumed (primary fresh acceptance plus the full-fresh
  correction re-acceptance). Mutable-state change observed during
  reconciliation: a push from this checkout at 16:34:40 advanced public
  `refs/heads/feat/kronika-one-product` from `ade1169…` to `ef99203…`
  (`reflog: update by push`); public `main` remains `ade1169…`. RF-12
  classification (unit: the remote feature-branch ref): primary
  `accepted-continuation` — the pushed object equals the accepted local
  candidate exactly (HEAD/tree match), no unexplained remainder; the actor was
  not directly established (presumed Cooperator-owned publication action) and
  will be confirmed with Michal; publication to `main` is still pending and
  remains a separate explicit authority. Next: Cooperator decision on
  publishing `main` `ade1169… -> ef99203…` (non-force fast-forward, direct
  readback) and the routine NUC refresh to that exact SHA; then Michal's
  rendered acceptance per the frozen plan's section 8.

- **2026-09-30 — Publication PASS; NUC refresh BLOCKED by a pre-existing
  state-directory defect (second unit); live runner degradation observed;
  decision requested.** Cooperator authorized the next step ("Autorizujem").
  Publication executed directly under that authority: non-force fast-forward
  `refs/heads/feat/kronika-one-product:refs/heads/main`, public readback
  `main` = `ef99203…`, feature branch = `ef99203…`, the two other heads
  unchanged; local `main` fast-forwarded to `ef99203…`; working branch clean.
  Publication PASS. The routine NUC refresh then failed at the first helper
  call (`framenest-release status`, exit 20). Diagnosis (all read-only):
  `/var/lib/framenest` is mode `755`; `framenest-db status` on the deployed
  tree fails closed with `FRAMENEST_DB_COMMAND_FAILED` (the S6 private-catalog
  rule requires `0700`); the DB file itself is `600 framenest`, backup
  readiness area is `ready`; `sudo -n true` succeeds and all gate SSH paths
  work. Root cause: the installed (and repository) unit
  `framenest-catalog-backup.service` declares `StateDirectory=framenest`
  without `StateDirectoryMode=0700`, so systemd's default `0755` is applied at
  every backup-service start; `ctime` of the directory is
  `2026-09-30 06:16:18 UTC`, exactly the last backup-service start (the NUC
  rebooted at 06:12:44 UTC and the backup unit started three times that
  morning; `framenest.service` itself carries `StateDirectoryMode=0700` and is
  not the offender). The same omission exists in
  `deploy/systemd/framenest-catalog-offdevice.service`. Live consequence:
  `framenest.service` is active, but its X/YouTube acquisition runner
  iterations have been failing every second since the reset
  (`X_ACQUISITION_RUNNER_ITERATION_FAILED`,
  `YOUTUBE_ACQUISITION_RUNNER_ITERATION_FAILED`, retryable) — new database
  connections now fail the private-catalog check. A bare `chmod 700` is not
  durable: the next backup run (timer next elapse 2026-10-01 03:25:23 UTC)
  would reset the mode again. Recommended route (A): immediate
  Cooperator-authorized `chmod 700` to stop the live failure, then a small
  bounded correction (add `StateDirectoryMode=0700` to the two unit sources
  and their contract tests), focused validation, publication to `main`
  (UI unchanged from the accepted S8 candidate), install the corrected units
  on the NUC, `daemon-reload`, then continue the routine release update to the
  new head and verify; Michal's rendered acceptance follows. Alternative (B):
  `chmod 700` plus deploy `ef99203…` as-is now (the cutover restart would
  re-apply `0700` through `framenest.service`), with the durable unit fix
  afterwards; the defect would recur at the next backup run. Decision
  requested; no further mutation performed beyond the authorized publication.

- **2026-09-30 — Route A executed end-to-end: state-directory repair committed
  and published (`5eddb81…`); NUC deployed and verified; live degradation
  stopped; rendered acceptance requested.** Cooperator approved route A
  ("A .."). Execution (direct, non-independent; Cooperator grant):
  immediate `chmod 700 /var/lib/framenest` restored the private-catalog
  invariant and stopped the failing acquisition runners (no
  `*_RUNNER_ITERATION_FAILED` entries since 14:50 UTC). Bounded repository
  fix: `StateDirectoryMode=0700` added to
  `deploy/systemd/framenest-catalog-backup.service` and
  `deploy/systemd/framenest-catalog-offdevice.service`, with contract
  assertions in `tests/contract/test_catalog_backup_timer.py` and
  `tests/contract/test_catalog_offdevice_timer.py`; Red on the unfixed units
  (2 failed), Green after (13 passed, exit 0) via the declared `test-focus`
  route with baseline `ef99203…`; exactly four paths changed, one commit
  `5eddb81bd164207a86f23b3f236e36b66192930b` (subject
  `fix(deploy): keep the catalog state directory private for backup units`).
  Publication: non-force fast-forwards with direct readback — public `main`
  and `feat/kronika-one-product` `ef99203… -> 5eddb81…`; the two other heads
  unchanged; local `main` fast-forwarded. NUC routine release update to
  `5eddb81…` through the sole entry point: `status` PASS,
  `check --release 5eddb81…` PASS, `deploy --yes` exit 0 with
  `web_release: 5eddb81…`, capture unchanged `94e605c…`. Host follow-up: the
  corrected backup unit was installed from
  `/opt/framenest/current/deploy/systemd/` to `/etc/systemd/system/` and
  hash-verified byte-identical
  (`ce67e4a3102142304641279466d1b734f0fc1694843d52178dfced5fb45a9a79`),
  `daemon-reload`, then one real `systemctl start
  framenest-catalog-backup.service` (`ExecMainStatus=0`) proved durability:
  `StateDirectoryMode=0700` effective, `/var/lib/framenest` still `700`,
  `framenest-db status` `at_head` `0035`. Final `framenest-release status`:
  active/web release `5eddb81…` (= public main), capture `94e605c…` parked,
  service active, database `0035`, backup readiness `ready`. The offdevice
  unit is not installed on the host; its source is fixed for future installs.
  Note: the deployed head is the accepted S8 candidate `ef99203…` plus this
  deployment-source fix; the S8 UI/research/rule bytes are unchanged. Next:
  Michal's rendered acceptance of the S8 UI on the NUC (numbered checklist
  sent); independent acceptance of this small fix is a ledger candidate if
  wanted.

- **2026-09-30 — Michal's rendered S8 acceptance recorded: items 1–9 PASS,
  item 10 NOT TESTED; the S8 row is complete end-to-end.** Cooperator
  acceptance on the NUC release `5eddb81…` (UI bytes identical to the
  independently accepted candidate `ef99203…`): Landing/Timeline PASS;
  Timeline filters PASS; unchanged Gallery (cards, filters, search, Details,
  playback) PASS; personal history with separate Questions/Records tabs PASS;
  disabled Search form PASS; disabled Research form PASS; administrator
  review empty states (no Reject, no unready actions) PASS; "Kronika"
  branding with the `FN` monogram PASS; responsive/keyboard basics PASS.
  Item 10 (sandboxed completed-document view) is NOT TESTED because the NUC
  catalog has no saved records; this is a missing-fixture state, not a
  defect, and it is carried into S9, where the bounded live acceptance will
  create saved records and the administrator review/approval and document
  rendering can then be exercised (no synthetic record was created here; no
  unauthorized fixture mutation). S8 phase-qualified results are now
  complete: implementation-PASS (non-independent), acceptance-PASS
  (independent, `55/01`), publication-PASS (`ef99203…`, then the deployment
  fix `5eddb81…`), deployment-PASS (NUC serves `5eddb81…`, database `0035`,
  service active, capture `94e605c…` parked), production/rendered acceptance
  PASS with the single NOT TESTED sub-item. The logical whole
  `kronika-one-product` remains open. Ledger candidates (non-authorizing):
  optional small independent audit of the deployment fix `5eddb81…`;
  living-status document refresh to state S8 accepted/deployed; carry the
  document/review rendered checks into S9 with real records. Next strategic
  action: S9 — integrated acceptance on the new empty catalog, the
  exact-object stopped-writer database reset (its own Cooperator-authorized
  operation), separate provider provisioning/live-call grants, and S10 after
  S9 acceptance.

- **2026-09-30 — S9 step 1 authorized; read-only reset preflight grant issued
  (session 56 / exchange 01).** Cooperator authorized the S9 first step
  ("Autorizujem"). Issued the read-only preflight
  `56_preflight_00.md` (session 56 / exchange 01, fresh-worker-session,
  Worker-Executed Preflight, native planning mode not-used, manual Cooperator
  delivery, High), SHA-256
  `bdfe6c60f93bde1b368927746fe89c3171c30eecb6820f378924fdeee5c404b7`: produce
  the exact-object reset plan on the released state `5eddb81…` under the
  binding AGENTS.md/ADR-0082/deployment-doc boundary (identify both old
  application databases and WAL/SHM files, stop all writers, delete only those
  objects, preserve media/profiles/identity configuration/secrets/archives,
  create the empty catalog through normal migrations); classify the state-dir
  database objects and `runtime-settings.json`; capture the newest verified
  recovery point and the documented rollback; propose the ordered stop /
  delete / migrate / verify / start sequence and the post-reset verification
  list. Read-only host access through the worker gate only; `sudo -n` read-only
  permitted; no service actions, no file mutation, no secret reads; the
  preflight does not authorize the reset. Report destination `56_report_00.md`
  (absent at issuance). Next: reconcile the preflight, then issue the exact
  reset grant for Cooperator approval before execution.

- **2026-09-30 — S9 reset preflight PASS reconciled; exact reset decision
  requested.** `56_report_00.md` reconciled and spot-checked read-only by the
  Orchestrator through the gate: released state `5eddb81…` on `/opt/framenest/current`,
  capture pointer `94e605c…`, service active with pid 8310 holding the catalog,
  backup timer active (next elapse `2026-10-01 03:25:54 UTC`), backup service
  inactive, off-device units not installed, identity map key present in
  `/etc/framenest/framenest.env` (value not read). Exact mutation boundary
  confirmed on the host: `/var/lib/framenest/catalog.sqlite3` (600, 1134592
  bytes, mtime `2026-09-30 15:08:07 UTC`) and the zero-byte
  `/var/lib/framenest/catalog.sqlite` (644) are present; all six
  `-wal`/`-shm`/`-journal` siblings are absent and are to be refused if they
  appear with unsafe properties. Nine July scratch files, every directory
  (`catalog-backups`, `catalog-backup-ops`, `catalog-restore-verify`, `ai`,
  `covers`, `upload-quarantine`, `x-staging`, `youtube-acquisition`,
  `chatgpt-page`, `deployment-evidence`, the root-owned backup residue dir,
  `.cache`, `.config`, `.local`), `/etc/framenest`, the release pointers,
  `/var/lib/kronika-capture`, `/srv/media`, backup bundles and archives are
  outside the reset. Checkpoint: newest verified bundle
  `auto-20260930T145340Z-2c167119` (attempt 86, revision `0035`,
  restore-verified) is older than the live catalog, so the reset grant must
  take one final quiescent `run-scheduled` backup after writers stop and
  before any delete, and must refuse the delete if the new bundle does not
  match the live file. Rollback per the accepted boundary is the same release
  with a compatible empty catalog, not a restore of deleted test data.
  Proposed ordered sequence recorded in the report: stop
  `framenest-catalog-backup.timer`, then the backup service, then
  `framenest.service`; prove stopped (`is-active`/`fuser` no pid); final
  backup; re-stat and delete only the exact set; `framenest-db migrate` and
  `status` (`at_head` `0035`); verify `0700`/`0600`; start service and timer;
  `check-health`; confirm pointers and capture unchanged. Orchestrator
  disposition: preflight accepted; one exact reset decision requested from
  Michal (recommended direct execution under his approval; sudo timestamp to
  be refreshed before execution). No mutation performed. Ledger candidate:
  the nine July scratch files in the state directory remain as future
  cleanup candidates outside this reset.

- **2026-09-30 — Reset executed; a post-reset startup gap found (configured
  publication library missing from the empty catalog); decision requested.**
  Michal approved the exact reset ("áno"). Executed directly: writers stopped
  in order (backup timer, backup service, `framenest.service`; all three
  inactive, `fuser` no pid); a final quiescent backup
  `auto-20260930T155720Z-f9ead1a3` (revision `0035`, 1134592 bytes matching
  the live file) was taken before any delete; the exact set was re-stat'ed and
  deleted (the present `catalog.sqlite3` and zero-byte `catalog.sqlite`; the
  six absent siblings tolerated, no symlinks or unusual link counts);
  `framenest-db migrate` then `status` returned `at_head` `0035`; the new
  catalog is `600 framenest:framenest` nlink 1 and `/var/lib/framenest`
  remains `700`. `framenest-catalog-backup.timer` restarted (active/waiting);
  pointers unchanged (`5eddb81…`, capture `94e605c…`); the three capture
  services remain active. **Startup gap:** `framenest.service` crash-looped
  (NRestarts 4, stopped to halt the loop): `check-database-ready` passes, but
  `serve` exits 1 because `create_app` → `_resolve_published_storage` raises
  `ValueError("Upload publication configuration is invalid.")` — the env key
  `FRAMENEST_UPLOAD_PUBLICATION_LIBRARY_ID=528f7733-b3c6-4f6d-9373-6f8fa8a2261b`
  requires a matching `libraries` row, and the empty catalog has none. The
  reset preflight did not construction-test `create_app` on the empty catalog;
  this gap is acknowledged. Old registration read read-only from the
  pre-delete bundle: device `a74ff55e-81b0-4b91-b07f-9de77a24a1b6` ("FrameNest
  NUC"), library `528f7733…` ("FrameNest Published Uploads", posix,
  `/srv/media/framenest-published`). The published directory still holds the
  media files (untouched); the catalog has no media rows (intended). Options
  presented: **A** — re-create the same device+library rows with the exact
  old IDs directly in the fresh DB (keeps the env unchanged; unsupported
  direct SQL write); **B (recommended)** — re-register through the supported
  `framenest-catalog device register` + `library register` commands (new
  UUIDs, no scan, no media import) and update exactly the one
  `FRAMENEST_UPLOAD_PUBLICATION_LIBRARY_ID` line in
  `/etc/framenest/framenest.env`; **C** — clear the publication setting
  (  feature off; not recommended). Decision requested; service remains stopped
  pending it. No other mutation performed.

- **2026-09-30 — Reset completed (option B executed); empty catalog serves
  healthy; S9 emptiness acceptance requested.** Michal chose B ("B").
  Executed directly: registered a new device
  `09a2cc80-2a4e-4953-a928-0bd051d18e64` ("FrameNest NUC") and a new library
  `048cb4a9-b67e-4140-a289-839f0c0e646e` ("FrameNest Published Uploads",
  posix, `/srv/media/framenest-published`) through the supported
  `framenest-catalog device register` / `library register` commands (no scan,
  no media import); changed exactly one line in
  `/etc/framenest/framenest.env`:
  `FRAMENEST_UPLOAD_PUBLICATION_LIBRARY_ID` from `528f7733…` to `048cb4a9…`
  (verified before/after). Startup diagnostic on the deployed tree then
  printed `create_app: ok`. `framenest.service` started cleanly: journal shows
  `check-database-ready: ready 0035` and uvicorn `Application startup
  complete.`; `check-health` returned `state: ready`; no further restarts
  after the loop was stopped (NRestarts remains the historical 4; no new
  restart lines). `framenest-release status`: active/web release `5eddb81…`,
  capture `94e605c…`, service active, database `0035`, backup readiness
  `ready`. Read-only catalog inspection: `kronika_records` empty,
  `logical_media` empty, exactly one library (the new registration) and one
  device (the new registration). The three capture services remain active;
  pointers unchanged; acquisition-runner failure events stopped (none since
  16:12 UTC). The reset leaves the accepted empty catalog for S9; the
  pre-reset test catalog remains only in the safety bundle
  `auto-20260930T155720Z-f9ead1a3`. Next: Michal's empty-catalog rendered
  acceptance (checklist sent), then a fresh independent S9 integrated review
  of the transition evidence, then the separately authorized provider step.

- **2026-09-30 — Michal's empty-catalog S9 acceptance recorded: items 1–9
  PASS, item 10 NOT TESTED; fresh independent S9 review grant issued (session
  57 / exchange 01).** Cooperator acceptance on the NUC release `5eddb81…`
  after the reset: Timeline landing/empty state PASS; empty Gallery with
  working filters/search PASS; empty personal history PASS; disabled Search
  form PASS; disabled Research form PASS; administrator review empty states
  PASS; existing sections (Manage media, My contributions, Analysis
  proposals) open and close with empty states PASS; navigation without
  errors PASS; branding/responsive basics PASS. Item 10 (document render)
  remains NOT TESTED — no records exist until the separately authorized
  provider step; it is carried there. Issued the fresh read-only independent
  review `57_acceptance_00.md` (session 57 / exchange 01,
  fresh-worker-session, Fresh Independent Audit, native planning mode
  not-used, manual Cooperator delivery, Extra High): verify the reset
  exactness (deleted-object set and absence, the pre-delete safety bundle
  `auto-20260930T155720Z-f9ead1a3` and its contents/hash, the new catalog
  `at_head 0035` with private modes and empty media/records, exactly the two
  new registration rows), the option-B completion (registrations through the
  supported CLI, the single env line matching the registered library, stated
  verification limits), preservation invariants (media files, capture
  services and pointers, identity configuration, archives), release/service
  integrity (active/web release = public `main` `5eddb81…`, capture
  `94e605c…`, health ready, no restart loop), and the absence of unexpected
  side effects. Read-only through the worker gate; no mutation, no service
  actions, no secrets; report destination `57_report_00.md` (absent at
  issuance). Next after the review: the separately authorized provider step
  (credentials, price-schedule wiring decision, bounded live acceptance).

- **2026-09-30 — S9 transition review PASS reconciled; S9 empty-catalog
  portion complete; provider step proposed.** `57_report_00.md` (status PASS,
  acceptance-PASS) reconciled and spot-checked read-only by the Orchestrator:
  all claims C1–C8 established independently — reset object exactness
  (state dir unchanged, only the two database objects removed, six siblings
  absent, scratch files and all directories retained, `runtime-settings.json`
  still absent); checkpoint (safety bundle
  `auto-20260930T155720Z-f9ead1a3`, catalog sha256 `fb2bf1f6…` and size match,
  revision `0035`, old library row intact); new catalog correctness
  (`600 filenest:framenest`, nlink 1, `at_head` `0035`, empty records/media,
  exactly the two new registration rows); option-B exactness (sudo audit
  records show the two supported registrations and the single `sed -i` line at
  16:11:03 UTC; env file size/mode/owner and 22-key set unchanged; stated
  limitation: no byte pre-image); release/service integrity (`current` =
  `5eddb81…` = public `main`, capture `94e605c…`, service active/
  `Result=success`, `NRestarts` unchanged since the clean 16:11:30 UTC start,
  timer waiting, readiness `ready`); preservation (40 media files still under
  `/srv/media/framenest-published`, newest mtime before the reset; three
  capture units active; identity map present; no media/records import);
  side effects (no runner-failure events since 16:12 UTC; repository clean at
  `5eddb81…`, AP pin unchanged); acceptance linkage (item 10 correctly
  untested). No findings. Residual/ledger candidates (non-authorizing): the
  newest verified recovery point `auto-20260930T155814Z-3f00f7a1` is the empty
  pre-registration snapshot (the timer will take a fresh one at 2026-10-01
  03:20 UTC; the pre-delete bundle remains available); the nine July scratch
  files remain the preflight cleanup candidate; item 10 stays with the
  provider step. S9 empty-catalog portion is complete: preflight `56/01` →
  reset execution (option B) → Cooperator acceptance (1–9 PASS, 10 NOT
  TESTED) → independent review `57/01` PASS. Next: the provider slice — P1 a
  bounded implementation grant to wire the accepted `UsagePriceSchedule` into
  `build_research_runtime` (today a saved request reconciles as unknown and
  consumes the reservation), P2 the Cooperator-provisioned OpenAI project
  credential (drop-in + key) and enabling research in the non-secret AI
  config (defaults already hold the accepted budgets), P3 the bounded live
  acceptance (one synthetic Search + one synthetic Research, reservation ≤
  USD 5.50, receipts and cleanup), P4 household UX acceptance with real
  records (unlocks document render and administrator review rendering).

- **2026-09-30 — Provider slice started; P1 price-schedule wiring grant issued
  (session 58 / exchange 01).** Michal approved starting the provider slice
  ("spúšťame!") and flagged that he has USD 7.50 platform credit and needs a
  slow, step-by-step P2 walkthrough (first use of the Responses API). Issued
  `58_implementation_00.md` (session 58 / exchange 01, fresh-worker-session,
  Fresh Implementation Worker, native planning mode not-used, manual Cooperator
  delivery, High), SHA-256
  `e00f009c8949e07c05f5634afcff2d94be826a891419d66e65a40149d7d55c52`: add the
  date-qualified `OPENAI_RESPONSES_PRICE_SCHEDULE_2026_09_26` constant (input
  5,000,000 / cached 500,000 / output 30,000,000 / web search per thousand
  10,000,000 micro-USD) in the OpenAI Responses adapter module with the
  revalidation-before-live-use note, pass it in `build_research_runtime`, pin
  the rates and add a causal composition reconciliation test (Red on the
  current `unknown` path, Green after); four-path allowlist; focused route;
  one local commit `feat(research): reconcile usage with the documented price
  schedule`; no push; research stays disabled. Report destination
  `58_report_00.md` (absent at issuance). Note for P2/P3: the accepted
  live-acceptance reservation is at most USD 5.50 against the available
  USD 7.50 credit; the accepted provider monthly hard limit (USD 30) will be
  set in the OpenAI project during P2. Next: dispatch P1, reconcile, then the
  step-by-step P2 walkthrough for Michal (project, hard limit, project key,
  key file, credential drop-in, enabling research in the non-secret AI
  config), then P3 live acceptance.

- **2026-09-30 — P1 implementation PASS reconciled; publication of `a368750…`
  requested.** `58_report_00.md` reconciled and re-verified read-only by the
  Orchestrator: commit `a3687505eb12359c76f85661e51e36d7e4778fc9` (parent
  `5eddb81…`, tree `6f845cb82c26412ef3109e9b902a74ba0e17e6b0`, subject
  `feat(research): reconcile usage with the documented price schedule`);
  exactly the four allowlisted paths; worktree clean; AP pin unchanged; public
  `main` and feature branch still `5eddb81…` (local only). Diff inspection
  confirmed the date-qualified
  `OPENAI_RESPONSES_PRICE_SCHEDULE_2026_09_26` constant (input 5,000,000 /
  cached 500,000 / output 30,000,000 / web search per thousand 10,000,000
  micro-USD, builder docstring names the section-3 source and the
  revalidation requirement) and the single `price_schedule=` wiring in
  `build_research_runtime`. Red on the parent proved the `unknown` accounting
  state; Green `32 passed` on the focused route. Recorded deviation: the
  docstring sits on the private builder because the frozen slotted schedule
  cannot carry `__doc__`; the public constant name is exported. The causal
  test replaces the credential supplier with a synthetic in-test value — no
  secret was read. Next: Cooperator publication authority for `a368750…`
  (non-force fast-forward `main` + feature branch) and the routine NUC
  refresh, then the step-by-step P2 walkthrough (OpenAI project, USD 30
  monthly hard limit, project key, key file, credential drop-in, enabling
  research in the non-secret AI config) and P3 live acceptance.

- **2026-09-30 — P1 published and deployed; P2 begun step by step.** Under the
  Cooperator's authorization: non-force fast-forwards with direct readback —
  public `main` and `feat/kronika-one-product` `5eddb81… -> a368750…`; local
  `main` synced. NUC routine release update to `a368750…` through the sole
  helper: `status` PASS, `check --release a368750…` PASS,
  `deploy --yes` exit 0 with `web_release: a368750…`; capture unchanged
  `94e605c…`. Post-deploy: helper `status` shows active/web release
  `a368750…`, database `0035`, service active, backup readiness `ready`;
  `check-health` returned `state: ready`. P2 started with step 1 (OpenAI
  platform: create the project, set the accepted USD 30 monthly hard limit,
  create a project-scoped API key; the key is not to be pasted into chat or
  stored anywhere until the step-2 host placement). Subsequent P2 steps
  prepared: step 2 Cooperator key-file placement at
  `/etc/framenest/credentials/research-openai` (0600 root; the app reads the
  systemd credential via `LoadCredential=KRONIKA_RESEARCH_OPENAI_API_KEY` from
  the drop-in `deploy/systemd/framenest-research-credential.conf`), step 3
  enabling research in `/var/lib/framenest/ai/config.json` (v3 research
  section with the accepted defaults), step 4 drop-in install, `daemon-reload`
  and one restart, step 5 capability verification; then P3 live acceptance
  under its own bounded grant.

- **2026-09-30 — COOPERATOR INTENT: administrator-settable research model;
  sequencing decision requested.** Michal raised, before completing P2 step 1,
  that as the administrator of Kronika he needs to be able to set the model —
  the accepted ADR-0083 route pins the fixed model `gpt-5.5-2026-04-23`.
  Orchestrator reading: this is a Cooperator-owned product change (server-side,
  administrator-controlled model selection), not client-supplied model
  fields; the client-supplied-model prohibition, snapshot-at-admission and
  no-automatic-fallback rules stay. Facts established read-only: the non-secret
  research configuration already carries a validated `model_id` string, so the
  model is technically server-configurable today via the AI config file; what
  is missing is (a) a first-class administrator surface (the AI admin API
  preserves the research section but does not expose or edit it), (b) a
  per-model price schedule, because `OPENAI_RESPONSES_PRICE_SCHEDULE_2026_09_26`
  and the accounting reconciliation are pinned to one model, and (c) the
  durable documentation update that supersedes the "fixed model" wording
  (ADR-0083/SPEC/SERVER) with the administrator-controlled selection, a
  validated web-search-capable allowlist, no fallback and snapshot semantics.
  Proposed sequencing: continue P2 (project, USD 30 limit, key — all
  model-agnostic) and P3 live acceptance with the accepted model, then a small
  bounded slice for the administrator research-settings surface (admin API +
  shell settings, model allowlist with matching price schedules, budgets,
  docs); alternative: pause P3 and implement the administrator surface first.
  Decision requested; no OpenAI platform action or host mutation taken in this
  exchange.

- **2026-09-30 — COOPERATOR DECISION: option 1; administrator research
  settings queued as a later bounded slice.** Michal chose option 1. P2/P3
  proceed with the accepted model `gpt-5.5-2026-04-23` (full path including
  accounting validated first); immediately after, a bounded slice with the
  working name **S9-R** will implement the administrator-managed research
  provider settings: admin API + shell settings surface (enable/disable,
  model from a validated web-search-capable allowlist with a matching price
  schedule per model; unknown model fails closed), budget fields, and the
  durable documentation update that supersedes the "fixed model" wording in
  ADR-0083/SPEC/SERVER while preserving no-client-model-selection,
  snapshot-at-admission and no-automatic-fallback. No different model was
  requested for P3. P2 step 1 (OpenAI project, USD 30 monthly hard limit,
  project-scoped key) remains with the Cooperator; the key is never pasted
  into chat or stored outside the step-2 host placement.

- **2026-09-30 — P2 steps 2 and 3 executed and verified.** Step 2 (Cooperator,
  NUC block): the project OpenAI key was written to
  `/etc/framenest/credentials/research-openai` — verified read-only as a
  regular file, `600 root:root`, link count 1, 164 bytes; the key value was
  never printed, pasted into chat, or stored anywhere else. Step 3
  (Orchestrator through the gate, using the supported atomic mutation): the
  non-secret AI config `/var/lib/framenest/ai/config.json` was upgraded from
  schema version 1 to version 3 (writer adds `providers: {}`) and gained the
  accepted research section via `mutate_ai_server_config` +
  `default_research_configuration(enabled=True)`: provider `openai-responses`,
  model `gpt-5.5-2026-04-23`, search limits 3 tool calls / 4,096 output tokens
  / 180 s / reservation 500,000 µ$; research limits 20 / 32,768 / 1,800 s /
  5,000,000 µ$; daily budget 10,000,000 µ$ and monthly 30,000,000 µ$; prompt
  16,384 B; response cap 8,388,608 B; answer 2,097,152 B; citations 200;
  timeouts 5/30/5; credential identifier `KRONIKA_RESEARCH_OPENAI_API_KEY`;
  raw `active_provider_id`/`provider_models` preserved, `updated_at_ms`
  refreshed; file now 1,043 bytes `600 framenest:framenest`. The running
  service does not re-read the research section, so research remains
  inactive until step 4. Note: `load_ai_server_config` reports the in-memory
  schema constant 3, so the step-3 script's "before" value read as 3 while
  the file was still version 1 — the file bytes confirm the upgrade. Next:
  step 4 — install `deploy/systemd/framenest-research-credential.conf` as a
  drop-in, `daemon-reload`, one service restart, and verification (service
  health, clean startup, and a transient systemd-credential presence check
  proving the `LoadCredential` mapping without exposing the key).

- **2026-09-30 — P2 complete (steps 2–4 + precheck); P3 live-acceptance
  instructions issued to the Cooperator.** Step 4 executed: the drop-in
  `deploy/systemd/framenest-research-credential.conf` was installed from the
  `a368750…` release tree to
  `/etc/systemd/system/framenest.service.d/` and hash-verified byte-identical
  (`fc11804f…`), `daemon-reload`, one clean restart (journal:
  `check-database-ready: ready 0035`, uvicorn `Application startup complete.`);
  service active; `check-health` `ready`; release `a368750…`, capture
  `94e605c…`, backup `ready`. A transient `systemd-run` check with the same
  `LoadCredential` property proved the credential readable through the systemd
  credential boundary (`credential_present: True`; the value was never
  printed). One transient SSH attempt timed out and succeeded on the single
  bounded retry (recorded; the adjacent commands in the same batch succeeded).
  P3 precheck via a transient on the deployed tree: config present, research
  `enabled: True`, provider `openai-responses`, model `gpt-5.5-2026-04-23`,
  `runtime_built: True`; `research_requests` and `research_budget_holds`
  empty. Issued the Cooperator-executed P3 acceptance artifact
  `59_acceptance_00.md` (logical whole `kronika-one-product`, 59/01):
  exactly one synthetic public Search + one synthetic public Research through
  the deployed UI, no retries, reservations ≤ USD 5.50 of the USD 7.50
  credit, stop on any error; then document render (S9 item 10), administrator
  approval of both records, Timeline/history/Gallery checks, and the platform
  usage receipt. The Orchestrator verifies server-side accounting, records,
  binding, reconciliation and cleanup afterwards and records
  `59_report_00.md`.

- **2026-09-30 — P3 live acceptance executed (Cooperator PASS); one cleanup
  finding.** Michal reported PASS after the two synthetic calls through the
  deployed UI. Server-side evidence (read-only): exactly two
  `research_requests` rows, both `saved`, no `error_code` —
  `op-1cfafe8e…` (search, record `72cf2d73…`) and `op-cb6b84ef…` (research,
  record `95a6406d…`); `kronika_documents` has exactly the two matching rows;
  both records are `family` visibility, version 2, with
  `timeline_entered_at_ms` set (administrator approval succeeded); no ERROR
  journal entries; `research_budget_holds` both `reconciled` with accounted
  costs of 57,640 µ$ (search) and 370,695 µ$ (research) — total ≈ USD 0.43 of
  the USD 7.50 credit, against reservations 500,000/5,000,000 µ$. The wired
  price schedule is confirmed live. **Finding: remote cleanup has no
  production caller.** `ResearchCoordinator.release_remote_pending()` is
  implemented and unit-tested but invoked nowhere in `src/`; the nudge paths
  (`research_api.py` POST submit and detail GET) call only `submit_pending()`/
  `poll_once()`, so terminal rows keep `cleanup_state: pending` and the
  provider-side responses were not deleted (observed `pending` for both P3
  rows). This contradicts the accepted design (“delete the remote response
  after validated local persistence”). Proposed: run the designed
  `release_remote_pending()` once as a bounded transient on the NUC to delete
  the two P3 responses now (within P3's cleanup authority), and authorize a
  small correction grant to wire cleanup into the research API nudges with a
  causal test. Platform usage figures (step 9) still to be reported by the
  Cooperator for the provider-side receipt. No additional provider calls were
  made; the whole remains open.

- **2026-09-30 — P3 responses deleted; automatic-cleanup correction grant
  issued (session 60 / exchange 01).** Under the Cooperator's authorization
  ("a"): the designed `release_remote_pending()` was executed once as a
  bounded transient on the deployed tree with the systemd credential;
  `released_count: 2` and both rows verified `cleanup_state: deleted`
  (`op-1cfafe8e…`, `op-cb6b84ef…`). P3 remote-deletion evidence is complete.
  Issued the bounded correction `60_correction_00.md` (session 60 /
  exchange 01, fresh-worker-session, Bounded Correction Worker, native
  planning mode not-used, manual Cooperator delivery, High), SHA-256
  `df7ef2278cca5ca011e1d1a50c2eff154221b546bad18d09b8b24e3ef1df5af5`: extend
  the two existing research API nudge blocks (POST admission path and detail
  GET) with `runtime.release_remote_pending()` inside the same guards, add one
  causal regression in `tests/contract/test_research_requests_api.py` (Red on
  the parent, Green after), two-path allowlist, focused route, one local
  commit `fix(research): release remote responses on research API nudges`, no
  push; a scoped fresh verification and the deployment are separate later
  steps. Report destination `60_report_00.md` (absent at issuance). The
  Cooperator's platform Usage figures for the P3 receipt remain requested.

- **2026-09-30 — Cleanup correction PASS reconciled; scoped verification
  issued (session 61 / exchange 01); P3 platform figures recorded.**
  `60_report_00.md` reconciled and re-verified read-only by the Orchestrator:
  commit `3bf424586289b500cf45cb0d49676b50d27328fa` (parent `a368750…`, tree
  `ee39cdee…`, subject `fix(research): release remote responses on research
  API nudges`); exactly the two allowlisted paths; both nudge blocks now call
  `runtime.release_remote_pending()` inside the existing guards; worktree
  clean; public refs still `a368750…`. Worker evidence: Red on the parent
  (release list empty), Green `20 passed` on the focused route. Cooperator
  platform Usage for the P3 acceptance: **53,037 total tokens, USD 0.38 total
  spend** — recorded as the provider-side receipt; the application's
  reconciled calculation was USD 0.05764 (search) + USD 0.370695 (research) =
  USD 0.4283, so the invoice is ~11% below the calculated figure (safe
  direction; the design distinguishes calculated cost from the invoice).
  Ledger candidate (non-authorizing): validate the price-schedule accuracy
  against future invoices (cached-input/reasoning handling, possible platform
  reporting lag). Issued the scoped fresh verification
  `61_acceptance_00.md` (session 61 / exchange 01, fresh-worker-session, Fresh
  Independent Re-Audit, native planning mode not-used, manual Cooperator
  delivery, Extra High): verify candidate containment, the correction shape,
  the focused route on the corrected candidate and the causal regression,
  absence of live side effects, and issue the P3-F01 verdict. Report
  destination `61_report_00.md` (absent at issuance). After a
  `verified-closed` verdict: publication and deployment of `3bf4245…` (then
  the NUC has automatic cleanup), completion of the S9 provider part, then
  S9-R (administrator research settings) and S10.

- **2026-09-30 — Cleanup correction verified-closed; publication of
  `3bf4245…` requested.** `61_report_00.md` (status acceptance-PASS)
  reconciled: independent scoped verification of
  `3bf424586289b500cf45cb0d49676b50d27328fa` established V1–V5 — candidate
  identity/containment (one commit, exactly the two allowlisted paths, clean,
  no push, AP pin unchanged); correction shape (the only two added statements
  are the guarded `release_remote_pending()` calls; the previously workerless
  method now has exactly the two intended production callers); causal evidence
  (focused route `20 passed` on the exact candidate; the regression is
  causal and Red on the parent per the recorded and re-derived evidence);
  no live side effects (fakes only, no credential, no NUC, clean tree). The
  finding `KRONIKA-ONE-PRODUCT-S9-P3-F01` is `verified-closed`. Limitations
  stated (causality derived from diff/assertions, not a parent checkout run;
  no broad suites; no NUC). Ledger candidates (non-authorizing): the
  POST-handler release only runs on the freshly-admitted path (a replay relies
  on a later GET nudge); a provider-side persistent delete failure keeps rows
  pending and retries per nudge within the bound; cleanup runs on every detail
  read (bounded). S9 provider part is functionally complete: live acceptance
  (P3), accounting reconciled, invoice recorded, remote deletion performed and
  automatic cleanup corrected-and-verified. Next: Cooperator publication
  authority for `3bf4245…` (non-force fast-forward `main` + feature branch)
  and the routine NUC refresh; the UI bytes are unchanged from the accepted
  `a368750…`, so the rendered acceptance stands. Then S9-R and S10.

- **2026-09-30 — `3bf4245…` published and deployed (automatic cleanup live);
  S9 provider part complete; S9-R Planner grant issued (session 62 /
  exchange 01).** Under the Cooperator's go-ahead: non-force fast-forwards
  with direct readback — public `main` and `feat/kronika-one-product`
  `a368750… -> 3bf4245…`; local `main` synced. NUC routine release update to
  `3bf4245…`: `status` PASS, `check --release 3bf4245…` PASS, `deploy --yes`
  exit 0; final `status` shows active/web release `3bf4245…`, capture
  `94e605c…`, service active, database `0035`, backup `ready`; uvicorn
  startup complete; `check-health` `ready`. The automatic remote cleanup is
  now live on the NUC (next terminal research interaction will delete remote
  responses through the corrected nudge path; the two P3 rows are already
  `deleted`). S9 provider part is complete: reset + independent review
  `57/01`; P1 price-schedule wiring `58/01` + deploy; P2 provisioning
  (credential, config v3 research section, drop-in, restart); P3 live
  acceptance with records, approval, render, reconciled accounting
  (`$0.4283` calculated, platform invoice `$0.38` / 53,037 tokens) and remote
  deletion; cleanup correction `60/01` + verification `61/01`
  (`verified-closed`). UI bytes are unchanged since the accepted S8 shell, so
  the Cooperator rendered acceptance stands. Issued the S9-R Planner grant
  `62_planning_00.md` (session 62 / exchange 01, fresh-worker-session,
  Planner, native planning mode required, manual Cooperator delivery, Extra
  High), SHA-256
  `b65db000cc9ebb98c49aedfb660008f7fdd22f39271b143885f98565616bfde0`:
  freeze the administrator research-settings design (admin-only API on the
  existing `provider.operate` capability, validated web-search-capable model
  allowlist with a matching `UsagePriceSchedule` per model, fail-closed
  unknown-model refusal, editable budget bounds, shell settings inside the
  existing administrator AI area, tests, the durable supersession of the
  fixed-model wording in ADR-0083/SPEC/SERVER, acceptance route and the
  proposed first implementation grant). Report destination `62_report_00.md`
  (absent at issuance). Remaining after S9-R: S10 public rename.

- **2026-09-30 — S9-R initial plan stopped PARTIAL with
  NEEDS_ORCHESTRATOR_DECISION; bounded model-evidence task routed.** The
  Planner (62/01) correctly stopped without freezing a plan. Orchestrator
  acknowledgement: the initial S9-R grant misdescribed `model_id` as a merely
  validated string; the code enforces equality with the fixed model in
  `ResearchConfiguration.__post_init__`, `_require_model_id` and
  `select_research_provider`. Planner findings to carry into the targeted
  revision: (1) configuration and selection boundaries must be deliberately
  modified for model selection; (2) only one price schedule exists and no
  second model’s public support/pricing was grounded under the read-only
  grant; (3) the research runtime captures configuration at application
  construction, so a durable settings save needs an explicit refresh path
  (including enabling a process that started disabled); (4) accounting must
  resolve per admitted request/model rather than one shared schedule, with
  restart persistence and fail-closed unknowns; (5) the request fingerprint
  includes model/config, so replay after a settings change interacts with
  idempotency and must not silently replace history; (6) configuration
  writes are atomic but not concurrency-guarded across writers, so the
  eventual API needs a conflict contract; (7) `provider.operate` and the
  existing admin AI dialog/API patterns are the integration points; identity
  must be verified, not loopback-legacy; (8) budget ceilings already exist;
  (9) the fixed-model wording spans AGENTS/README/PRODUCT/SPEC/SERVER plus
  ADR-0083, whose “Revisit Conditions” require a superseding ADR for a
  changed model or budget decision, and living status sentences predating
  S8/S9 evidence need bounded reconciliation. Smallest next step accepted:
  one bounded public-documentation evidence task (fresh Worker, WebSearcher
  profile) producing a source-backed model matrix — at least one additional
  exact model identifier with Responses/`web_search` support, deprecation
  status, request-shape compatibility and full pricing (input, cached input,
  output, web search, tiers) mapped to the existing `UsagePriceSchedule`;
  no account access, no provider generation, no NUC. That new external
  evidence then supports the single justified targeted revision of the
  planning question (not yet issued). No implementation authority exists.

- **2026-09-30 — Model matrix evidence PASS reconciled; targeted planning
  revision issued (session 62 / exchange 02).** `63_report_00.md` reconciled
  (WebSearcher, PASS, retrieval date 2026-09-30, first-party pages only):
  four grounded candidates — `gpt-5.5-2026-04-23` (baseline; 5,000,000 /
  500,000 / 30,000,000 / 10,000,000 micro-USD; no separate cache-write
  charge), `gpt-5.6-sol` (4,000,000 / 400,000 / 20,000,000 / 10,000,000;
  cache writes 1.25x; promotional through at least 2026-11-21),
  `gpt-5.6-terra` (2,000,000 / 200,000 / 12,000,000 / 10,000,000),
  `gpt-5.6-luna` (200,000 / 20,000 / 1,200,000 / 10,000,000); all support
  Responses + `web_search` + `low`/`high` and 128k max output; none
  deprecated; `gpt-5.5-pro` excluded (no `low`); `gpt-5.4` a valid
  cache-write-free alternative. Material schedule-shape gaps: the >272K
  long-context tier (2x input / 1.5x output) and the GPT-5.6 cache-write
  charge cannot be represented by the current four rates; unknowns include
  account access, 5.6 snapshot stability, >272K reachability, cache-write
  occurrence and usage-field observability (LEAD). Issued the single
  authorized targeted revision `62_planning_01.md` (session 62 / exchange 02,
  current-worker-session, Planner, native planning mode required, manual
  Cooperator delivery, Extra High), SHA-256
  `1fe695ce69e1cd28142e4d471f836b258503430633f540d0dd590eac0c0f9dbd`:
  freeze the S9-R plan incorporating the nine `62_report_00.md` findings and
  the `63_report_00.md` matrix — allowlist with per-model schedules (one
  Cooperator-confirmable product choice), the schedule-shape decision
  (long-context and cache-write dimensions vs constrained inputs), per-request
  pricing with restart persistence, runtime refresh, idempotency, concurrent
  save, admin API, shell surface, tests, the new ADR plus living-document
  deltas, and the acceptance route; one bounded first-party documentation
  retrieval allowed solely for the cache-write usage-field LEAD. Report
  destination `62_report_01.md` (absent at issuance). After the revision
  report: freeze the plan, surface the allowlist choice to Michal, then issue
  the S9-R implementation grant.

- **2026-09-30 — S9-R revision reconciled; plan frozen; implementation grant
  issued (session 64 / exchange 01).** `62_report_01.md` (45 KB, persisted by
  the Cooperator after chat delivery; SHA-256
  `971279787fdbc218964f6c8d01b99957afaf0137405cd73758b09d8ef3538325`)
  reconciled and spot-checked read-only by the Orchestrator: the fixed-model
  enforcement is confirmed in code (`research_configuration.py` lines 136/431,
  `research_registry.py` line 141, constant in `domain/research.py`);
  all five proposed new paths are absent; the compatibility test inputs
  (`tests/unit/infrastructure/ai/test_registry.py`,
  `tests/contract/test_ai_server_composition.py`) and the referenced existing
  modules exist. Plan accepted and frozen; the report’s PARTIAL applied only
  to its original file delivery, which the Cooperator closed by persisting
  the exact content. The Cooperator confirmed the one product choice
  in-session (“Štyri modely (Recommended)”): allowlist
  `gpt-5.5-2026-04-23` (default), `gpt-5.6-sol`, `gpt-5.6-terra`,
  `gpt-5.6-luna`; exact short/long/cache-write rates; 272,000-token
  long-context threshold; Sol `valid_until` 2026-11-22; the cache-write usage
  field (`usage.input_tokens_details.cache_write_tokens`) resolved by the
  bounded first-party retrieval. The frozen plan also fixes versioned pricing
  (`configuration_version = "s9r-20260930"`, tuple-resolved append-only
  schedules), the persistent/refreshable runtime, replay/idempotency
  version 2 with an atomic submission claim, the shared-configuration CAS and
  sibling lock with `If-Match` semantics, the exact admin routes
  `GET/PUT /api/admin/ai/research-settings` with `provider.operate` and the
  stable error table, the shell Research-settings section, the 44-path
  allowlist, the focused validation route and the acceptance route (including
  the bounded live model-switch proof). Issued the implementation grant
  `64_implementation_00.md` (session 64 / exchange 01, fresh-worker-session,
  Fresh Implementation Worker, native planning mode not-used, manual
  Cooperator delivery, High), SHA-256
  `18d88392a4d811481eb9b7cff195b06719dc3f966d85a90693bf62042ea9b085`: the
  frozen sections 2–8, the exact 44 paths, one local commit
  `feat(research): add administrator settings and versioned pricing`, no
  push. Report destination `64_report_00.md` (absent at issuance). Next:
  dispatch; then one fresh independent audit of the exact candidate,
  publication, NUC refresh, rendered acceptance and the bounded live proof
  (each separate), then S10.

- **2026-09-30 — S9-R implementation PASS reconciled; audit issued (session 65
  / exchange 01).** `64_report_00.md` reconciled and re-verified read-only:
  commit `e8f1c04b289b7bd694d66edba012d288ee41e610` (parent `3bf4245…`, tree
  `1cbf6739083e7459b1d5e5011dbd72fed77e5d69`, subject
  `feat(research): add administrator settings and versioned pricing`); 37
  changed paths, all inside the frozen 44-path allowlist (the remaining
  allowlisted files were legitimately unchanged, including the two read-only
  compatibility inputs); worktree clean; public refs still `3bf4245…`; AP pin
  unchanged. Spot checks: the four-entry catalog with the confirmed
  identifiers and Sol `valid_until`; the eleven new catalog/arithmetic tests;
  the regenerated inventory. **Orchestrator-found discrepancy routed to the
  audit as a named probe (V11):** `64_report_00.md` §4 attributes “strict
  usage parsing and submit-404 distinction” tests to
  `tests/unit/infrastructure/ai/test_openai_responses_adapter.py`, but that
  file is unchanged in the delta; the new coverage lives (at least partly) in
  `test_research_models.py` and `test_research_settings_api.py`, so the audit
  must determine whether the required causal coverage exists or is missing,
  and classify the report attribution. Recorded deviations to assess in the
  audit (V10): media-provider `If-Match` optional while research PUT requires
  it; Sol cutoff enforced at admission/PUT rather than in selection; legacy
  over-threshold unknown accounting. Issued the fresh independent audit
  `65_acceptance_00.md` (session 65 / exchange 01, fresh-worker-session, Fresh
  Independent Audit, native planning mode not-used, manual Cooperator
  delivery, Extra High), SHA-256
  `63b53eea36ad73b498ddeac6beff361d6fe20f7d8ff54eac850c0820bc06e912`: the
  twelve fixed claims (containment; catalog/pricing; accounting integrity;
  runtime/enable-disable; idempotency/single attempt; shared-config CAS;
  admin API; shell; documentation; the three deviations; the V11 named probe;
  independent non-regression re-run of the focused route), R3 with
  authorization, accounting-integrity and shared-configuration
  specializations, read-only with no temporary root. Report destination
  `65_report_00.md` (absent at issuance). Next after the audit verdict:
  publication, NUC refresh, rendered acceptance, then the bounded live
  model-switch proof, then S10.

- **2026-09-30 — S9-R audit PARTIAL reconciled (F-1…F-4); bounded correction
  issued (session 64 / exchange 02).** `65_report_00.md` reconciled:
  independent audit of `e8f1c04…` established V1 (containment), V2 (catalog
  and rates), V3 (accounting integrity, fail-closed unknown, fixtures),
  V5 (idempotency and atomic claim), V6 CAS core, V7 admin API, V8 shell,
  V9 documentation and V12 (focused route independently `373 passed` + JS
  `29/29`); no security, accounting or authorization defect. Not accepted yet:
  **F-1** (medium) the implementation report attributed adapter tests to an
  unchanged file and two new adapter behaviors (`_parse_usage`,
  `_submit_status_error_code`) have zero test references — both a reporting
  defect and a coverage gap, exactly the named probe the Orchestrator had
  found before issuing the audit; **F-2** (medium) no causal regressions for
  the plan’s Refresh/Snapshot rows (disabled-start runtime, enable without
  restart, model change affecting only new admissions, restart persistence);
  **F-3** (low-medium) the media half of the shared-configuration contract is
  partial and its deviation record understated (no media `If-Match`/ETag in
  the shell, no cross-invalidation, no JS coverage) — fail-safe but
  incompletely delivered; **F-4** (low) GET research-settings emits an eighth
  `changed: null` key instead of exactly seven fields. Eight ledger
  candidates L-1…L-8 recorded (notably L-1 cached-tokens-missing semantics
  and L-5 unbound route-policy test). Orchestrator disposition: one bounded
  correction covering F-1…F-4, all inside the existing 44-path allowlist
  (F-3 completed rather than accepted as a deviation); no publication before
  the correction and a fresh re-audit. Issued `64_correction_01.md` (session
  64 / exchange 02, current-worker-session, Bounded Correction Worker, native
  planning mode not-used, manual Cooperator delivery, High), SHA-256
  `54bbbb7b075e7df5e790e4e9d48a40714afd0059fcb3e8298c7d9618ef611abd`:
  seven-path allowlist (`ai_admin_api.py`, `app.js`,
  `test_openai_responses_adapter.py`, `test_research_provider_contract.py`,
  `test_research_completion.py`, `test_research_settings_api.py`,
  `ai_providers_admin_frontend.test.js`), one local commit
  `fix(research): close the S9-R audit findings`, no push; the 64 report is
  not rewritten (historical evidence) — the correction report records the
  attribution defect. Report destination `64_report_01.md` (absent at
  issuance). Next: fresh independent re-audit (session 66), then publication,
  NUC refresh, rendered acceptance and the bounded live proof.

- **2026-09-30 — Correction PASS reconciled; fresh re-audit issued (session 66
  / exchange 01).** `64_report_01.md` reconciled and re-verified read-only:
  commit `2af8edde5faf8967777a68b0a72685cc580c45ea` (parent `e8f1c04…`, tree
  `3f6367cf2da9224eebefb7659ca0efb8ae7d54e0`, subject
  `fix(research): close the S9-R audit findings`); exactly six of the seven
  allowlisted paths changed (`test_research_completion.py` untouched is
  permitted by the “and/or” wording); worktree clean; public refs still
  `3bf4245…`; AP pin unchanged. Corrections: F-1 twelve adapter guard cases
  (`_parse_usage`/`_submit_status_error_code`, submit-404 vs poll-404,
  cache-write parsing, never-zero usage) with the attribution defect recorded
  in the correction report and `64_report_00.md` deliberately not rewritten;
  F-2 one contract regression covering disabled-start existence, enable
  without restart, model-change scope and restart persistence; F-3 the media
  shell `If-Match`/ETag symmetry with cross-invalidation and JS coverage
  (server-side optional media `If-Match` retained); F-4 GET returns exactly
  seven keys and PUT seven plus `changed`. Worker evidence: focused 70 passed
  Python, 33/33 JS, plus a narrow 268-passed compatibility rerun; recorded
  near-miss: two mis-targeted `app.js` edits caught and fixed before commit.
  Issued the full-fresh re-audit `66_acceptance_00.md` (session 66 /
  exchange 01, fresh-worker-session, Fresh Independent Re-Audit, native
  planning mode not-used, manual Cooperator delivery, Extra High), SHA-256
  `e42d06125f6ba439574a1522b252fae23ca679e0568afcf2acdf253eae260e70`: verify
  R1 containment, R2 F-1, R3 F-2, R4 F-3 (including a close read of the four
  media mutation functions and the ping for mis-targeted edits), R5 F-4,
  R6 independent focused-route re-run, R7 the L-1…L-4 residual disposition.
  Report destination `66_report_00.md` (absent at issuance). Next after a
  PASS: publication, NUC refresh, rendered acceptance and the bounded live
  model-switch proof.

- **2026-09-30 — S9-R re-audit acceptance-PASS reconciled; publication
  requested.** `66_report_00.md` reconciled: fresh independent re-audit of
  `2af8edde…` established R1–R7 with no findings — containment (39-path
  two-commit delta strictly inside the frozen 44; no push; AP pin unchanged);
  F-1 verified (15 new adapter cases exercising the real adapter and both
  error mappings; attribution defect recorded without rewriting the
  historical report); F-2 verified (real disposable engine, mutable
  configuration provider, disabled-start existence, enable without restart,
  model-change scope, restart pricing durability; causal); F-3 verified (the
  four media mutation functions and the ping read line-by-line; header only
  when a revision exists; both invalidation directions; live server-side ETag
  path); F-4 verified (exactly seven GET keys, PUT plus `changed`); focused
  route independently reproduced `391 passed` Python and `33/33` JS with the
  delta fully explained. L-1…L-4 dispositions recorded without findings:
  L-1 cached-tokens-missing is conservative and needs an explicit wording
  decision; L-2 a disabled PUT may newly store an expired model but every
  generation path fails closed; L-3 the frozen plan’s “confirm discarding a
  dirty draft” sentence is genuinely unimplemented (`dirty`/`stale` are
  effectively write-only; CAS keeps it fail-safe) and the audit recommends
  naming it as an explicit deviation in the S9-R closure record; L-4 the
  confirmation note omits the two reservation values. New ledger candidates
  L-9 (invalidation notice invisible until Save), L-10 (weak/malformed ETag
  treated as no revision) and L-11 (F-2 “restart” naming). Two numeric
  inaccuracies in `64_report_01.md` recorded as trace-only noise. Orchestrator
  disposition: candidate accepted; L-1…L-3 to be named in the closure record
  (L-3 as a named deviation with an optional later UI follow-up); L-9…L-11
  ledger candidates. Requested the Cooperator’s publication authority for
  `2af8edde…` (non-force fast-forward `main` + feature branch, direct
  readback) and the routine NUC refresh; then rendered acceptance and the
  bounded live model-switch proof.

- **2026-09-30 — S9-R published and deployed; rendered acceptance requested.**
  Under the Cooperator’s authorization: non-force fast-forwards with direct
  readback — public `main` and `feat/kronika-one-product`
  `3bf4245… -> 2af8edd…`; local `main` synced. NUC routine release update to
  `2af8edd…`: `status` PASS, `check --release 2af8edd…` PASS, `deploy --yes`
  exit 0; final `status` shows active/web release `2af8edd…`, capture
  `94e605c…`, service active, database `0035`, backup `ready`; uvicorn
  `Application startup complete.`; `check-health` `ready`. The S9-R slice is
  now live on the NUC (administrator research settings, versioned pricing,
  refreshable runtime, shared-config CAS, both routes in the workspace
  composition). Sent Michal the rendered acceptance checklist for the
  administrator AI dialog: presence and current values of the Research
  settings section (enabled, `gpt-5.5-2026-04-23`, $10/$30/$0.50/$5.00,
  credential indicator, catalog info for the four models); model change plus
  confirmation with Cancel leaving the value unchanged; budget change plus
  confirmation with Cancel; one real save (terra) and restore to the default
  5.5; a two-tab stale-revision conflict exercise; accessibility/responsive
  basics; the ordinary-user boundary marked NOT TESTED unless a second
  identity is available; and the L-3 dirty-draft deviation noted as known.
  After acceptance: the bounded live proof (Research on `gpt-5.5-2026-04-23`,
  setting switched to `gpt-5.6-luna` while it runs, then a Search on Luna;
  at most two new generation attempts, reservations ≤ USD 5.50, restore the
  pre-proof settings afterwards), then S10.

- **2026-10-01 — Michal’s S9-R rendered acceptance: items 1–5 and 8 PASS,
  item 6 PARTIAL (conflict copy not observed), 7 and 9 NOT TESTED.**
  Accepted: the Research settings section exists with the correct current
  values and catalog information (1–2); model and budget changes show the
  confirmation and Cancel leaves the value unchanged (3–4); a real save works
  and the settings were restored to the default `gpt-5.5-2026-04-23` (5);
  accessibility/responsive basics (8). Item 6 (two-tab stale conflict) is
  PARTIAL: he did not see the conflict copy. Orchestrator read-only triage:
  the client path exists — `saveResearchSettings` sets the conflict copy on a
  409 and the `finally` block calls `renderResearchSettings()`, the section
  has a status line and a Reload button, and the JS suite already contains
  `a stale-revision save returns the conflict copy without rebasing`; the most
  likely cause is the manual setup not producing an actual stale revision
  (e.g., the second dialog opened after the first save, or a no-op save that
  does not advance the revision). A precise two-tab retry recipe was sent;
  the ordinary-user boundary (7) stays NOT TESTED (covered by API tests and
  the audit) and the L-3 deviation note (9) is already recorded. The
  server-side 409 and CAS behavior are independently established by audit
  R5/R6; only the rendered copy awaits confirmation.

- **2026-10-01 — Rendered item 6 PASS; live proof declined and closed as
  unproven; S9 slice closed.** Michal reported PASS for the precise two-tab
  stale-conflict recipe. The bounded live proof (`67_acceptance_00.md`) was
  then explicitly declined (“Nechajme unproven”); Orchestrator verification
  confirmed no new provider call was made (only the two P3 rows exist) and
  recorded the outcome as `67_report_00.md` (not executed; the mid-run
  overlap and the Luna-live path remain unproven, with deterministic causal
  coverage in the audited F-2 regression and the P3 live acceptance on the
  default model). Rendered acceptance for S9-R: items 1–6 and 8 PASS; item 7
  (ordinary-user boundary) NOT TESTED and covered by API/authorisation tests;
  item 9 is the named L-3 deviation. Settings after acceptance: research
  enabled, model restored to `gpt-5.5-2026-04-23`, daily budget `$8`,
  monthly `$30`, reservations unchanged — all within bounds. **S9 closure
  record (Orchestrator):** integrated acceptance on the empty catalog (`57/01`
  review plus Cooperator acceptance), the exact-object reset, provider
  provisioning and live acceptance (P2/P3, accounting reconciled, invoice
  recorded, remote deletion), the cleanup correction and verification
  (`60/61`), the S9-R slice (plan `62/01`+revision, implementation `64/01`,
  audit findings `65/01`, correction `64/02`, re-audit `66/01`
  acceptance-PASS), publication and NUC refresh of `2af8edde…` all satisfied.
  Named residual deviations/decisions carried forward: L-1 (cached-tokens
  missing semantics), L-2 (disabled PUT may store an expired selection),
  L-3 (the plan’s dirty-draft discard confirmation is unimplemented; fail-safe
  under CAS; optional later UI follow-up), plus ledger candidates L-4 and
  L-9…L-11 and the previously carried items (macOS youtube-fake-demo test
  debt, price-schedule accuracy vs invoice, nine July scratch files, the
  newest recovery point predating the registrations). The logical whole
  remains open; next and final slice: **S10** (public rename), after which
  the whole may be closed.

- **2026-10-01 — S10 preflight complete (Orchestrator direct, read-only);
  rename steps requested from the Cooperator.** `68_preflight_00.md` records:
  verified current state (local `origin` = `https://github.com/cisarik/framenest.git`;
  `cisarik/kronika` = `66c40d43…` main only; framenest public refs at
  `2af8edd…`; the release helper verifies public main through the local
  remote name, not a hardcoded URL). Live references: ten
  `deploy/systemd/*` `Documentation=https://github.com/cisarik/framenest`
  URLs to update; the local `origin` URL; everything else is internal
  identity kept by AGENTS (`ap.project.conf` projectId, package, unit names,
  helper name) or historical evidence kept as-is (provenance manifest, ADRs,
  trace). No README/PRODUCT/SPEC/SERVER/ROADMAP live link references the
  repository URL. Sequence: (1) Cooperator renames `cisarik/kronika` →
  `cisarik/kronika-capture-archive`, then `cisarik/framenest` →
  `cisarik/kronika` (no transfer, force or history change; redirects kept);
  (2) bounded reference-update grant (direct under S10 authority): local
  `origin` update, the ten unit URLs, one commit
  `chore: update repository URLs for the kronika rename`, non-force
  fast-forward push of `main` and the feature branch to the renamed
  repository with readback; (3) verification (new-name refs, old-name
  redirect, capture archive still `66c40d43…`, helper continues to work);
  (4) Cooperator archives `cisarik/kronika-capture-archive` last; (5) S10
  acceptance record, then whole-closure evaluation.

- **2026-10-01 — COOPERATOR DECISION: former capture repository keeps the name
  `cli_chatgpt`; S10 reference update published.** Michal renamed
  `cisarik/kronika` to `cisarik/cli_chatgpt` (not the planned
  `kronika-capture-archive`) and `cisarik/framenest` to `cisarik/kronika`;
  asked whether to keep it, he confirmed “nechávam”. Orchestrator execution
  under the S10 authorization: local `origin` updated to
  `https://github.com/cisarik/kronika.git`; the ten `deploy/systemd/*`
  `Documentation=` URLs updated; ROADMAP’s S10 row updated to `cli_chatgpt`
  and a dated execution note added to ADR-0082 (the original wording stays as
  historical decision text); focused unit-contract route `68 passed`; one
  local commit `5260e2d153ef0bef71b8f13e20616ba1ed0f50b1`
  (`chore: update repository URLs for the kronika rename`); non-force
  fast-forward push of `main` and `feat/kronika-one-product` to the renamed
  repository with direct readback — both refs `5260e2d…`; the old
  `cisarik/framenest` URL redirects and reads the same refs;
  `cisarik/cli_chatgpt` still `66c40d43…` (unchanged); local `main` synced.
  `framenest-release status` and `check --release 5260e2d…` both exit 0 with
  the new origin; the target release’s `capture_unit_contract_sha256` changed
  because the capture unit Documentation URLs changed (cosmetic; the
  deployed capture release and installed units are untouched). Remaining S10
  steps: the Cooperator archives `cisarik/cli_chatgpt` (last step) and
  optionally the routine NUC refresh to `5260e2d…` for exact public-main
  consistency; then the S10 acceptance record and whole-closure evaluation.
  No force, no history rewrite, no repository deletion or transfer; internal
  identifiers and historical evidence unchanged.

- **2026-10-02 — S10 accepted without archive; closure published.** After a
  power loss, the interrupted worktree was re-verified. Michal confirmed S10
  closes without archiving `cisarik/cli_chatgpt`. Public readback before the
  closeout: `cisarik/kronika` `main` and `feat/kronika-one-product` at
  `5260e2d…`; `cisarik/framenest` redirects to the same ref;
  `cisarik/cli_chatgpt` `main` remains `66c40d43…`. Two defects in the
  interrupted closeout: the capture provenance upstream
  `https://github.com/cisarik/kronika.git` now resolves to this repository,
  so it cannot name commit `66c40d43…`; and `ap project check` rejects
  `projectId = cisarik/framenest` once `origin` is
  `https://github.com/cisarik/kronika.git`. Both are corrected. Living status
  in README, PRODUCT, SPEC, ROADMAP, AGENTS, the NUC runbook and ADR-0083
  records S10 complete and the capture repository active. The implemented
  awk ledger entry left the active ledger; its closure action was
  `remove-from-active-ledger` and its historical evidence is AP pin
  `73e20ef…`. Commits: `0eaa43922aa034965ea4a657a22046ab139f17a6`
  (`docs: close the S10 rename without archiving the capture repository`)
  and `0c850996cd2ef17dae4112733fd17fdc732f4699`
  (`chore: remove the implemented awk observation from the active ledger`).
  `ap project check --baseline 0c85099…` PASS. Focused contract route
  `16 passed` (`test_worker_execution_contract`, `test_ap_project_contract`,
  `test_chatgpt_page_packaging`). Non-force fast-forward push; direct
  readback: both public refs and the `cisarik/framenest` redirect are
  `0c85099…`; `cisarik/cli_chatgpt` is unchanged. No archive, no force, no
  history rewrite. The `framenest` package, provenance module, migration
  history, HTTP headers and deployment identifiers remain. NUC still serves
  the earlier release; a routine refresh to `0c85099…` is not part of this
  acceptance. Next decision: whole-closure evaluation.

- **2026-10-02 — Routine NUC refresh to the S10 closeout.** Michal established
  the global sudo timestamp (`GLOBAL_SUDO_READY`). Read-only `status` showed
  active web release `2af8edd…`, capture `94e605c…`, service active, database
  `0035`, backup `ready`. `check --release 0c85099…` exit 0. `deploy --yes`
  exit 0. Final `status`: web release `0c85099…`, capture unchanged
  `94e605c…`, service active, database `0035`, backup `ready`. Worker then
  ran remote `sudo -K`. No capture activation, no archive, no schema change.

- **2026-10-02 — Rendered read of the refreshed NUC shell.** Browser session
  against the Tailscale Serve origin: title Kronika, signed in, cloud
  connected. Timeline shows the two approved 2026-09-30 Search and Research
  cards. Opening the Search card loads the question, citation and the
  sandboxed answer (`Python 3.14.7` present in the frame source). Gallery
  reports an empty catalog view, consistent with the S9 reset. The media AI
  indicator reads unavailable because the last provider test did not reach
  the configured provider. No new provider call was made.

- **2026-10-02 — Predecessor whole is closable; successor handout issued.**
  Scoped S0–S10 evidence holds: public `main` and the NUC web release are
  `0c85099…`, capture remains `94e605c…`, `cli_chatgpt` stays active, and the
  checkout is clean. Michal's new direction, only Kronika including host
  paths and script names, supersedes the predecessor's "no mass rename" limit
  as the next objective. It does not reopen S10. Closure signal emitted in
  the Orchestrator chat. The remote sudo timestamp stays released.

- **2026-10-02 — Misplaced handout withdrawn.** `05_handout.md` was written
  inside this closed trace and then removed. It is not a handout of this
  whole. The successor opens at
  `/Users/agile/meta/projects/kronika/00/03-kronika-sole-identity/` with
  `00_handout.md` and `00_notes.md`. Archive sequence remains `00`.
  Logical-whole sequence is `03`. This trace stays frozen aside from this
  archival correction.

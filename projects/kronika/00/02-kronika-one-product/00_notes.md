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

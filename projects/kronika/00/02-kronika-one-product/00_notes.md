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

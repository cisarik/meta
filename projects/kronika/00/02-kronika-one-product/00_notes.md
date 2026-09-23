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

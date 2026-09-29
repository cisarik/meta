# Fresh Orchestrator restoration — kronika-one-product (04_handout)

Artifact relationship: **historical restoration handout**. It transfers
information, not authority. Task authority comes only from the current
authoritative Orchestrator routing and the complete Worker prompts issued from
it.

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Capability profile: Orchestrator (terminal-capable coordinator)
Logical whole identity: kronika-one-product
Current phase: everything through S4-B and S7-P implemented, independently
  audited (51/01 PASS, F01 fixed), environment-cleaned, published and deployed.
  Next: a Planner grant (native Plan mode required) for S8 UI/UX, then S8
  implementation -> S9 -> S10.
Cooperator: Michal
Delivery route: manual Cooperator delivery to fresh Worker sessions (default);
  the Cooperator may grant temporary autonomous execution
Reasoning recommendation: Extra High for the S8 Planner and for any
  acceptance/audit; High for bounded implementation grants
Development host: MacBook, checkout /Users/agile/Projects/framenest
NUC: reachable over Tailscale; runs the current public main; dev/test machine;
  capture parked; do not touch without a bounded grant
Trace (MacBook): /Users/agile/meta/projects/kronika/00/02-kronika-one-product/
  (138 files)
AP pin (verify, do not upgrade): 73e20ef80b88700d5fcbc397cd8edd4fc425869f
Handout sequence: this is 04_handout.md (predecessors 01, 02, 03)
```

This handout restores a fresh Orchestrator for the **ongoing** whole
`kronika-one-product`; it does not close it. Restoration grants no mutation
authority. Sessions 01-51 are used; **the next genuinely fresh Worker session
ordinal is 52**.

## 0. Communication and binding directives

- Speak to Michal in Slovak, masculine address, feminine self-reference.
  Worker prompts, handouts, notes and reports are professional English.
- Presentation: a status block of at most five lines, exactly one status mark
  (🟢 proceed / 🟡 wait-one-decision / 🔴 stop), one dispatch instruction, plus
  the visible delivery capsule (Recipient, Reasoning, Client/Plan mode, Prompt
  path + SHA-256, Report path, Archival).
- Delivery model: the Orchestrator issues a complete authoritative Worker
  prompt; Michal dispatches it into a fresh Agent chat. On 2026-09-28/29 he
  granted temporary autonomous Orchestrator execution for the deployment and
  the S4-B/S7-P chains; autonomy evidence is non-independent and must be
  labelled as such. Prefer independent verification for security-sensitive
  slices.
- One accountable Worker at a time; no subagents. Terse `ok`/`áno`/
  `pokračuj` continues the current slice, never opens a new whole.
- Only the Orchestrator emits the closure signal `LOGICKY CELOK UZAVRETY`.
- Sudo is Cooperator-owned: Workers never run `sudo -v` or `sudo -K`; Michal
  establishes the NUC timestamp before dispatch (`sudo -v`, then `sudo -n
  true`) and releases it manually afterwards.
- NUC SSH goes through
  `scripts/operator/network/framenest_nuc_worker_gate.fish` (`--probe` for
  agent capability; BatchMode SSH only under a host grant). The three
  `FRAMENEST_NUC_SSH_*` names are exported in Michal's MacBook shell profile
  (`~/.zshenv`); values are never printed, stored or committed.
- Never read `private/**`, browser profiles, cookies, tokens or credential
  stores. Never print private values, host identifiers, addresses or secrets.
- Testing economy is binding: targeted validation and the smallest reproducer;
  broad suite at most once for a final candidate when a named risk requires
  it; never re-run an unchanged gate.
- The capture host stays parked: no browser restart, login, resume,
  activation, job or ask without a new explicit Cooperator decision.

## 1. First thirty minutes

1. Read the product `AGENTS.md`, the pinned AP spine (`.ap/AP.md`,
   `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`,
   `.ap/ARTIFACT_LIFECYCLE.md`) and `/Users/agile/meta/README.md`.
2. Read this handout completely. Then the trace highlights:
   - `51_report_00.md` — the independent audit of S4-B + S7-P (PASS; F01 open
     low; its dispositions are already executed and recorded below).
   - `50_report_00.md` + `50_implementation_00.md` + `49_planning_00.md` —
     S7-P results, plan, amendment.
   - `48_report_00.md` + `48_implementation_00.md` + `47_planning_00.md` —
     S4-B results, plan, amendment.
   - `46_report_00.md` + `46_deployment_00.md` — NUC deployment and the
     private-catalog/systemd correction (worked example for future schema
     jumps).
   - `45_report_00.md`, `43_report_00.md`, `42_report_00.md` — worker-gate
     Darwin fix and its re-audits.
   - `39_report_00.md`, `38_report_00.md`, `38_report_01.md`,
     `35_report_00.md`, `33_report_00.md` — S6 correction chain and frozen S6
     plan.
   - `25_report_00.md` — accepted provider/Timeline architecture (S8's design
     source); `15_report_00.md` — S3 recovery playbook (parked history).
   - `00_notes.md` — the whole's complete history; the last entries are the
     current truth.
3. Re-verify section 2 read-only on the MacBook and the NUC reachability. If
   anything does not hold, stop and tell Michal in one block before any grant.

## 2. Claimed state to re-verify (read-only)

GitHub `cisarik/framenest` (direct `git ls-remote`):

```text
main                          ade1169b4ba079bb1df540a929572ca58e777d16
feat/kronika-one-product      ade1169b4ba079bb1df540a929572ca58e777d16
feat/chatgpt-page-ask-kernel  26d28b16c08a5e7e0179a32c16646bfdc1009c81
feat/x-meme-browser-companion 7ff6546f345827d6df20bd5b13d5e57cb4bc90db
```

Local MacBook checkout: branch `feat/kronika-one-product` at the same
`ade1169…` (tree `f266df7205ddea5b83de7e6cd8313512ce70bcb1`), clean; `.ap` at
the pin `73e20ef…` (gitlink and `.ap` HEAD); `.venv` on a uv-managed CPython
3.13.14 created by Homebrew Poetry 2.5.1. The history since the previously
audited base (`89a4029…`) is thirteen commits:

```text
3f5dc5c fix(systemd): request 0700 for the framenest state directory
df44c2d feat(research): add durable research request storage and accounting
5417fb8 feat(research): persist research requests, slots and budget holds
a9ec1f1 feat(research): supervise the research lifecycle in the coordinator
34cb2f5 feat(research): add the OpenAI Responses adapter
0a7d3f0 feat(research): wire the research runtime inert by default
8a277a3 feat(records): add record capabilities and safe document rendering
f1ec367 feat(research): complete research requests into common records
c0a5288 feat(research): expose research request submission and history APIs
74f2a40 feat(records): expose history, timeline, render and approval APIs
8e5c374 fix(records): bound quote nesting in the safe document renderer
7be040e fix(docs): align the schema head, portable paths and ledger expectations
ade1169 fix(env): resolve macOS host tools and Darwin process-group semantics
```

NUC (verified by direct read-only capture, 2026-09-29): web release
`ade1169…` (equals public main; `/opt/framenest/current` and
`.framenest-release-sha` match), capture release `94e605c…` unchanged and
parked (`browser_unavailable` / `E_BROWSER_UNAVAILABLE`, jobs 0/0,
`active_job` null, `client_connected` true, zero chrome/chromium,
NRestarts=0), `framenest.service` active, database revision `0035`,
`/var/lib/framenest` mode `700`, host unit carries `StateDirectoryMode=0700`
(byte-identical to the repository source), `tailscaled` active and enabled.
Trace: 138 files including this handout and all reports through `51`.

## 3. What is done, verified and published

- **S0-S3** (published history): one-product architecture, capture relocation,
  submission barriers, capture supervision/diagnostics. The S3 host remainder
  (Cooperator login, null-job resume, activation, one synthetic ask) stays
  parked.
- **S4-D + S4-A** (published): ADR-0083, provider-neutral research contracts,
  configuration v3, registry. Independently accepted.
- **S6 + AP pin bump + F01 correction** (published at `0d0d8c8`): private
  records, immutable Q/A documents, centralized authorization, administrator
  approval, private catalog lifecycle, access inventory. The acceptance
  finding S6-A35-F01 was corrected and independently re-audited
  (`verified-closed`, `39/01`).
- **Worker-gate Darwin fix** (`665a565`, re-audited `43/01`) and **F01 symlink
  correction** (`89a4029`, re-audited `45/01`): the gate discovers the native
  macOS launchd agent under strict validation.
- **Systemd/state-directory correction** (`3f5dc5c`): the accepted private
  catalog requires a `0700` state directory; systemd's default state-directory
  mode reset it on every start. `StateDirectoryMode=0700` plus a host mode
  change fixed the deployment; independently audited in `51/01`.
- **S4-B native provider runtime** (`df44c2d..0a7d3f0`): migration `0035`,
  request/slot/budget persistence, the coordinator lifecycle, the OpenAI
  Responses adapter over an injectable transport, inert-by-default
  composition, credential deployment source.
- **S7-P completion and rendering** (`8a277a3..74f2a40`): `research.run` and
  `records.approve` capabilities, a bounded safe Markdown renderer, atomic Q/A
  completion into common records, research request APIs, records APIs
  (history, Timeline, detail, render, admin inventory, approval), route
  policies and a regenerated access inventory for head `0035`.
- **Independent audit `51/01` (PASS)**: eleven fixed claims established over
  the ten-commit delta (340 focused tests green; synthetic probes;
  `__CF_USER_TEXT_ENCODING` and one prompt tree-string transcription defect
  recorded and since fixed). One open low finding **F01**: unbounded
  blockquote recursion in `render_markdown` crashed a render with
  `("> " * 1200) + "leaf"`. **F01 is fixed** in `8e5c374` (depth-capped
  quotes, regression test) — disposition closed by the Orchestrator.
- **Post-audit consolidation** (all published at `ade1169`): living README,
  PRODUCT, SPEC, SECURITY and ROADMAP sentences moved to schema head `0035`
  with their two locking tests; `WORKER_EXECUTION_CONTRACT.md` and its test
  use the host-agnostic `<physical-repository-root>` instead of a stale Linux
  path; the AP pin test, the capability-set test, the ledger expectation and
  the AP-envelope macOS key were realigned; **macOS host-tool resolution** was
  added (ffmpeg/ffprobe in the media tools, node in the capture CLI, fish in
  the AI deployment helper, plus a shared `tests/support/tooling.py` for node,
  fish and poetry spawns); **Darwin `killpg` EPERM** is handled in the media
  process runner and its test cleanup. Broad suite result on the final
  candidate: **4080 passed, 1 failed, 9 skipped** (8m47s). The single failure
  and the skips are described in section 7.
- Publication: `main` and the feature branch both equal `ade1169…` (non-force
  fast-forwards with direct readback). The NUC was then updated to `ade1169…`
  through the documented schema-jump continuation (`0034 -> 0035`).

## 4. Your next action: a Planner grant for S8 (native Plan mode)

No further audit or environment work is needed before S8. Follow the AP
protocol: the successor Orchestrator issues a **Planner = Worker** prompt with
**native Plan mode required** (a genuinely fresh session, ordinal 52,
Extra High, manual Cooperator delivery), waits for the Planner report, freezes
its plan (one targeted revision is allowed if a material mapping is left
open), then issues bounded implementation grants.

Recommended Planner planning question (adapt the wording, keep the fields):

- Produce the frozen **S8 unified Kronika UI/UX** plan on the published
  `ade1169…` baseline: the shared Timeline landing (administrator-approved
  records only), the separate personal-history view, Search and Research
  forms, and the administrator review queue, inside the existing packaged web
  shell (`src/framenest/adapters/api/web/`), with **no new framework**, the
  Gallery kept as a separate working view with the frozen Gallery/Details
  behavior, and the existing design language reused.
- Deliver: the exact file allowlist (new and edited paths), the page/route and
  API mapping over the existing endpoints (section 5), the component and state
  design, the disabled/error UX, the accessibility and responsive baseline,
  the test matrix (existing repository test style: Python contract tests plus
  `node --test` for JS), the acceptance route (fresh independent audit of the
  exact candidate + **Cooperator rendered acceptance on the NUC refreshed to
  the exact public main**), and the recommended first implementation grant
  (fields and boundaries).
- The Planner must treat as binding: the private/family/administrator access
  rules, `approve`/`withdraw` only (no `reject`), answer text only through
  detail/render, list payloads as implemented, the research runtime disabled
  by default, and the testing-economy directive.

The Planner reads: `.ap/AP.md`, `.ap/AP_WORKER.md`,
`.ap/PROMPT_CONTRACTS.md` (Planner contract), `AGENTS.md`, `PRODUCT.md`,
`SPEC.md`, `ROADMAP.md`, `docs/adr/0082`/`0083`, `25_report_00.md`,
`50_report_00.md`, `51_report_00.md`, the S6 plan `33_report_00.md`, and the
current web shell and API modules.

## 5. S8 planning inputs: the unified Kronika UI/UX

**Current web surface.** The packaged shell is
`src/framenest/adapters/api/web/{index.html,styles.css,app.js}`, served at `/`
(with `/assets/{name}`); the Gallery and Details MVP behavior and player are
frozen unless a concrete defect is identified. JS tests use
`node --test tests/*.test.js`. Any **new HTTP route** requires a
`ROUTE_POLICIES` entry in `tailscale_ingress.py` (the fallback is fail-closed)
and an access-inventory regeneration (running
`tests/contract/test_kronika_access_inventory.py` rewrites
`docs/KRONIKA_ACCESS_INVENTORY.md`; commit the regenerated file).

**Available APIs and shapes (implemented in S7-P):**

```text
GET  /api/research/capabilities            enabled, provider/model, limits, retention notice
POST /api/research-requests                {kind, prompt, client_request_id, consent_version} -> 202 summary
GET  /api/research-requests?limit&offset   own history: items[operation_id, kind, state,
                                           error_code, prompt, created/admitted/submitted/
                                           finished/updated_at_ms, record_id], total
GET  /api/research-requests/{id}           owner/admin; same summary
POST /api/research-requests/{id}/cancel    owner/admin; returns summary
GET  /api/admin/research-requests          administrator inventory
GET  /api/my/records                       own record summaries (record_id, kind, owner,
                                           visibility, timestamps, version, media_id, read_decision)
GET  /api/timeline                         approved records only, same summary shape
GET  /api/records/{id}                     {record, version, document{operation_id, kind,
                                           question_text, citations, timestamps}}
GET  /api/records/{id}/render              escaped HTML, nosniff, restrictive CSP
GET  /api/admin/records                    administrator inventory
POST /api/admin/records/{id}/approval      {action: approve|withdraw, expected_version}
                                           -> {record_id, version, changed}
```

**UX rules and gotchas to design around:**

- Errors use `{"error": {"code": ..., "message": ...}}`; map the stable codes
  (`E_DISABLED`, `E_NOT_CONFIGURED`, `E_BUSY`, `E_IDEMPOTENCY_CONFLICT`,
  `E_BUDGET_EXCEEDED`, `IDENTITY_REQUIRED`, `CAPABILITY_DENIED`,
  `RECORD_CONFLICT`, `NOT_FOUND`) to friendly copy.
- Submission is idempotent by `client_request_id`: generate one per form
  attempt so retries cannot double-charge; a 409 conflict means the client id
  was reused with different content.
- Research progress is nudged synchronously by API calls; there is no
  background poller. Poll `GET /api/research-requests/{id}` while a request is
  active (a few seconds apart), and render the capability-disabled state from
  `/api/research/capabilities` without assuming provider readiness.
- `consent_version` is required and bounded but not stored; show it as an
  explicit consent acknowledgement.
- Approval is `approve`/`withdraw` only and version-checked (stale version
  409); never offer `reject` until a schema state exists.
- Lists carry question summaries and metadata; answer text appears only in
  detail and render. Embed the render response in a sandboxed iframe (its CSP
  is `default-src 'none'; style-src 'unsafe-inline'; img-src data:`), or
  inject it as HTML knowing that route output is escaped and script-free.
- Timeline is approved-only for every caller including administrators;
  personal history is the caller's own view; the Gallery remains separate.
- Open Cooperator question for the Planner: UI copy language (English as
  today, or Slovak) and any branding treatment ("Kronika") in the shell.
- The Planner should also schedule a thin **UI regression harness** consistent
  with the repository style (Python contract tests for route/page assertions
  and `node --test` for JS logic), and keep additions inside a frozen S8
  allowlist.

## 6. Remaining slices and parking

- **S9** integrated acceptance, database reset, deployment: fresh integrated
  acceptance over the completed product; the exact-object stopped-writer DB
  reset (its own Cooperator-authorized operation; never improvised); Cooperator
  rendered acceptance on the exact public-main NUC release; routine deployment.
- **S10** public repository transition: rename `cisarik/kronika` ->
  `kronika-capture-archive`, then `cisarik/framenest` -> `cisarik/kronika`
  (no history rewrite; update remotes and deployment URLs).
- **Parked independently**: remaining S3 host completion; capture-mode
  Search/Research; S5 ZIP activation; S7-C capture integration. Do not reopen
  without a new Cooperator decision.

## 7. Operational runbooks and environment facts

**NUC routine release update** (ADR-0075; sole entry point
`deploy/ubuntu/framenest-release`, stdlib only, run from the checkout):

```text
./deploy/ubuntu/framenest-release status
./deploy/ubuntu/framenest-release check --release <published-40-hex-SHA>
./deploy/ubuntu/framenest-release deploy --release <published-40-hex-SHA> --yes
```

- The helper requires local `HEAD` == release and public `main` == release;
  use an exact temporary detached checkout under the grant and return to the
  working branch afterwards. Fixed tooling: Poetry
  `/opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry`, CPython
  `/opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13`.
  Routine updates never invoke `uv`.
- **Worked schema-jump example (`0034 -> 0035`, 2026-09-29, exit 13):** the
  first `deploy --yes` stopped with `migration-required` after atomically
  publishing the target tree; the documented annex then verified the target
  (pointer unchanged, service active on the old release, target
  `.framenest-release-sha`, executable `framenest-db`, exactly the three lock
  artifacts, target status `current_revision=0034 head_revision=0035`),
  removed only `ap.tar`, `framenest_release.py` and `superproject.tar` plus
  the empty lock directory, migrated from the target tree
  (`framenest-db migrate` -> `0035 at_head`), and cut over with
  `framenest-release rollback --release <T> --yes` -> exit 0. Final status:
  web release = target, capture release `94e605c…`, database revision `0035`,
  backup readiness `ready`.
- A raw exit 20 before the schema gate is different: it means a remote
  command failed. On 2026-09-29 it was the S6 private-catalog rule rejecting a
  `0755` state directory (systemd kept resetting it); the fix was
  `StateDirectoryMode=0700` plus a one-time mode change. Always read the
  failing command's own output first.
- The NUC currently equals public `main` (`ade1169…`) with database `0035`;
  the next update needs no schema jump until `0036` exists. Capture stays
  parked; the capture pointer must remain `94e605c…`; no browser, login or
  job action. Sanitized as-left capture: units, pointers, release SHA,
  bridge readiness, listener ports (loopback classification only), chrome
  counts, disk.
- Sudo lifecycle: Michal establishes the timestamp before dispatch and
  releases it manually; Workers use `sudo -n` only.

**Publication pattern** (Cooperator action or explicit grant): fast-forward
only, exact refspecs, non-force, direct readback, never delete or move refs,
never push the lab/work refs. `main` == feature branch == `ade1169…`.

**AP route on the MacBook**: `./.ap/ap project check --root
/Users/agile/Projects/framenest --baseline <full-40-hex-SHA>` and
`./.ap/ap exec ... --operation test-focus -- <files> -q -p no:cacheprovider`.
`--baseline` must be a full lowercase commit id. The pinned AP carries the
macOS portability fix; do not upgrade, downgrade or modify `.ap`. The ledger
`docs/AP_UPGRADE_OBSERVATIONS.md` records the
`darwin-bsd-awk-project-argv-counting` observation as implemented.

**macOS environment facts (post-`ade1169`):**

- The AP sanitized envelope fixes `PATH=/usr/bin:/bin`; project tools live in
  Homebrew paths. Production resolvers (media ffmpeg/ffprobe, capture node,
  AI-deployment helper fish) and the shared `tests/support/tooling.py` now
  fall back to `/opt/homebrew/bin` and `/usr/local/bin` after `PATH`.
- Darwin `killpg` returns EPERM for groups with no signalable members; the
  media process runner and its test cleanup treat that as absent.
- Known remaining test debt (single item): the broad suite on `ade1169`
  reports `4080 passed, 1 failed, 9 skipped`. The failure is
  `tests/contract/test_youtube_fake_demo.py::test_youtube_fake_demo_runs_the_real_loopback_cli_to_acceptance`
  on macOS: the claim reaches `handed_off` / `upload_state=publish_pending`,
  wait events continue, and the CLI's 20 s `--wait-timeout` expires with
  `YOUTUBE_WAIT_TIMEOUT`; the manual-upload path in the same demo catalogs
  fine, so the difference is in the YouTube handoff-to-publication path. The
  skips are opt-in gates (real media tools, real Poetry on PATH outside the
  envelope, live NVIDIA smoke) — not failures. A bounded diagnostic task
  (compare the handoff upload's validation/publication notifications against
  the manual path; the demo script is `tests/support/youtube_fake_demo.py`)
  belongs to the Planner backlog, not to S8 itself.
- The four old PC-era parked failures are no longer observed on the MacBook:
  the fresh `.venv` provides both console scripts, the gate test hardens
  against ambient `FRAMENEST_NUC_SSH_*` values, and the sigterm lifecycle test
  derives the canonical interpreter from the checkout.

**Before any live Research activation** (own bounded grant): provision the
credential (drop-in `deploy/systemd/framenest-research-credential.conf`),
inject a validated `UsagePriceSchedule` into `build_research_runtime` (saved
requests currently reconcile as unknown and consume the reservation — safe
fail-closed), consider a supervised background poller, and add the operator
overshoot reconciliation path. Research stays disabled by default and no live
provider call is authorized.

## 8. Working-mode guidance

- The whole's rhythm: planning (Planner, native Plan mode) -> frozen plan ->
  bounded implementation grants -> independent audit of the exact candidate ->
  publication -> deployment -> Cooperator rendered acceptance where UI is
  involved.
- Keep correction loops bounded; escalate repeated blockers; label
  non-independent evidence.
- Reports use the standard `### Report for ORCHESTRATOR_CHAT` header with
  coordinates, per-claim verdicts, control matrices, findings with the full
  INFOSEC structure, containment, residual risk and authority expiry.
- Trace grammar: prompts `NN_<phase>_<index>.md`, reports
  `NN_report_<index>.md`, `index = exchange ordinal - 1`; handouts/closures
  share their own sequence (this is `04_handout.md`). Sessions 15 and 34 must
  never receive another prompt.
- Rendered UI/UX acceptance belongs to Michal and requires the NUC to serve
  the exact candidate release first (refresh it through the routine helper).

## 9. Ledger candidates carried forward

Non-authorizing; do not implement without a grant:

- The single macOS youtube-fake-demo failure and its diagnostic lead
  (section 7).
- `reject` approval has no schema state; `consent_version` is validated but
  not stored; `research_operations` accounting rows are unwritten; no
  background research poller; operator overshoot reconciliation absent;
  price schedule unwired in composition.
- Older-catalogue startup: history routes on a pre-`0035` database would fail
  if hit; the production composition migrates at deploy, so this is a
  hypothetical dev-host case.
- Parked capture cues: `retained_release_paths` unused by deploy/rollback; a
  dangling journal symlink classifies as absent; VNC `-nopw` with `-localhost`
  by design; `mcookie` may appear in the Xvfb argv; installed
  `/etc/kronika-capture/capture.env` has no `TMPDIR`; non-capture NUC
  listeners 53809/50216 unidentified (outside the capture boundary).
- S4-A residual history (`Co-authored-by: Cursor` trailer; malformed legacy
  AI config files ignored on read and omitted on save).

## 10. STOP rules

- Do not implement product code yourself outside an explicit autonomy grant;
  issue Workers (or execute bounded, recorded steps under a grant).
- Do not push, force, delete or move any ref without explicit Cooperator
  publication authority naming the exact refspec; never push the lab/work
  refs; never publish an unverified candidate without telling Michal.
- Workers never run `sudo -v`/`sudo -K`; Michal establishes and releases
  manually.
- Do not read `private/**`, browser profiles, cookies, tokens, credentials or
  the parked capture state; do not restart the capture browser.
- Do not deploy or publish unaccepted work silently; do not reset or delete
  the database; do not rewrite the capture journal; the S9 reset is its own
  operation after writers stop.
- Do not weaken loopback/token/Host/Origin boundaries, the sandbox, the
  private-catalog modes or the authorization gates.
- Do not upgrade AP; the pinned gitlink governs.
- Do not run the broad suite at every step; testing economy is binding.
- Do not reopen the closed whole `kronika-public-identity-and-clean-start` or
  the parked capture slices without a new Cooperator decision.

## 11. Paste seed for the successor Orchestrator chat

```text
Resume the AP-integrated Kronika project as a fresh Orchestrator for the
ongoing whole kronika-one-product (one Kronika on the FrameNest base; modular
research provider; capture parked). Development host: this MacBook
(/Users/agile/Projects/framenest); the NUC runs the current public main and
must not be touched without a bounded grant.
Read the trace handout
/Users/agile/meta/projects/kronika/00/02-kronika-one-product/04_handout.md
completely, then the audit 51_report_00.md, the S4-B/S7-P plans and results
(47-50), the deployment report 46_report_00.md, the S6 history (33/35/38/39),
the provider/Timeline plan 25_report_00.md and the whole's 00_notes.md.
Begin read-only. Verify section 2 (refs including main == feat branch at
ade1169, AP pin 73e20ef, MacBook checkout and .venv, NUC at ade1169 with
database 0035 and capture parked). Everything through S7-P is implemented,
independently audited (51/01 PASS; F01 fixed) and published; no further audit
is needed before S8.
Then continue per AP protocol: issue the S8 Planner grant (genuinely fresh
Worker session 52, native planning mode REQUIRED, Extra High, manual
Cooperator delivery) using section 4 of the handout as the planning question,
freeze the returned plan, and proceed with bounded S8 implementation grants
followed by independent acceptance and Cooperator rendered acceptance on the
refreshed NUC. Then S9 and S10 per ROADMAP.md.
Communicate with Michal in Slovak. Workers never run sudo -v or sudo -K.
```

# Era 13 Whole Notes — FrameNest NUC ChatGPT analyze provider

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned, append-only during the whole, frozen at
closure. Non-authorizing. Public-safe by default. Michal owns any meta Git
commit.

Working identity (Cooperator-selected 2026-09-22, pending Planner lock of
the exact slice boundary):

```text
framenest-nuc-chatgpt-analyze-provider
```

Trace:

```text
/home/agile/meta/projects/framenest/13/00-framenest-nuc-chatgpt-analyze-provider/
```

Handout: `00_handout.md` (2026-09-22). Live opening handout for the fresh
Orchestrator. Not Worker authority.

Predecessor: closed Kronika whole
`kronika-public-identity-and-clean-start`. Its `02_handout.md` is superseded
and must not be pasted. Kronika publication remains parked. This whole does
not publish Kronika and does not open `kronika-tailnet-family-library`.

## Session log

- **2026-09-23 — FrameNest parked; NUC findings handed to the Kronika whole.**
  The Cooperator parked FrameNest and will continue the Kronika project on the
  NUC. This Orchestrator updated the successor Kronika handout
  `/home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/00_handout.md`
  (2026-09-23 version) with the full NUC inventory and browser/Cloudflare
  findings, the Cooperator's NUC refocus (one persistent browser, shared
  household "temp" account, admin-handled challenges, a loopback endpoint
  FrameNest can later call), and the Planner brief. Current FrameNest state:
  `main` and live NUC `current` both `26d28b1`; S1+S2 delivered and accepted;
  S3 live locator probe blocked by Cloudflare; NUC tooling (Node 22.23.2,
  Chrome for Testing 154.0.8037.57, AppArmor profile, Xvfb/x11vnc/noVNC
  packages) installed; two browser profiles flagged (`chromium-profile`,
  `chromium-profile-flagged-20260923`); all transient view/probe units stopped
  and all helper scripts and the wizard-URL file removed. No active mutation.
  A future FrameNest Orchestrator resumes when Kronika exposes an endpoint
  FrameNest can call; do not disturb the deployed FrameNest service, and read
  the Kronika handout and trace only.
- **2026-09-23 — Step 3 login attempt: Cloudflare hit the auth flow.**
  The kernel login probe ran headed on `:99` with a fresh profile (old profile
  parked as `chromium-profile-flagged-20260923`) and the Cooperator logged in
  through the noVNC view. The probe finished (`ok: true`, 108 s) but the page
  ended at `/api/auth/error` with title `Just a moment...`, composer absent —
  i.e. Cloudflare interposed during the auth flow and the login errored. A
  subsequent manual relaunch (no CDP) of that same fresh profile also shows
  `Just a moment...`, so the profile is now challenged, like the old one.
  Contrast: unauthenticated fresh profiles pass both with and without CDP
  (tests D2/E). Working hypothesis: Cloudflare challenges the sensitive auth
  flow and/or the combination of an authenticated profile with automation
  signals; repeated restarts appear to deepen the flag. Cooperator observation
  of the login flow was requested before choosing the next step.
- **2026-09-23 — Step 2 result: fresh profile passes, old profile flagged.**
  Fresh-profile tests (no CDP, and separately with CDP, no login, `chatgpt.com`)
  both loaded the normal `ChatGPT: Chat, Work, Create...` page within 30 s and
  stayed normal at 90 s, while the old logged-in profile is challenged in every
  launch style. CDP alone is therefore not the trigger, and the environment
  (same exit node, relay subnet, Chrome for Testing, AppArmor profile) is
  healthy; the old profile carries a flagged state, most likely from the rapid
  repeated restarts during the probe attempts. Next proposed step: park the old
  profile, run the kernel login probe headed on `:99` with a fresh profile, the
  Cooperator logs in interactively, the finisher posts `/done` when the
  composer appears, and the locator metrics are captured in the same browser
  instance without a restart. View units remain up.
- **2026-09-23 — Network and session diagnostics for the challenge.**
  Read-only inventory: the NUC and the dev host already select the same tailnet
  exit node `cz-prg-wg-101.mullvad.ts.net` (online); the PC's local Mullvad app
  is disconnected, so both egress via `tailscale0`. Egress IPv4 is stable but
  differs per client inside the same relay subnet (`146.70.129.101` NUC vs
  `146.70.129.111` PC), i.e. the exit node NATs each client to a different
  address and identical public IP is not guaranteed by selecting the same exit
  node. Plain `curl` receives `403 cf-mitigated: challenge` from chatgpt.com on
  both machines (expected for non-browsers). Browser tests on the NUC: the
  logged-in profile is challenged in every launch style (CDP with and without
  `--password-store=basic`, CDP with the root URL, plain no-CDP, and a repeat),
  while the first manual launch passed before the repeated restarts; a
  fresh-profile no-login test was inconclusive (`Untitled` after 25 s).
  Interpretation: the challenge is most likely browser/session-level risk
  (repeated rapid restarts, automation/CDP signals) rather than the exit node,
  with possible contribution from the exit node being briefly offline during
  the Cooperator's network work. View units were stopped again after the test.
  Next proposed step: a longer fresh-profile test with explanations.
- **2026-09-23 — Login works; Cloudflare challenge blocks the kernel path.**
  The Cooperator completed the manual ChatGPT login in the visible NUC
  browser; the profile is authenticated (window title `ChatGPT`). After that,
  every further launch hit Cloudflare's `Just a moment...` interstitial:
  driver-style CDP with and without `--password-store=basic`, CDP with the root
  URL, and a plain no-CDP relaunch with the exact earlier-success flags — all
  stuck, so the current challenge is IP/risk-driven, not launch-flag-driven,
  and it does not resolve unattended. The vendored stealth option
  (`--disable-blink-features=AutomationControlled` + UA) is unusable with
  Chrome for Testing because `parseChromiumMajorVersion` expects
  `Chromium|Chrome <digits>` while CfT prints `Google Chrome for Testing …`
  (`E_DRIVER_VERSION`). All transient view/probe/test units were stopped and
  every helper script and the wizard-URL file were removed; nothing durable
  beyond the installed tooling, the AppArmor profile and the logged-in profile
  remains. Cooperator direction recorded: FrameNest and Kronika stay completely
  separate; the ChatGPT module keeps the same core (FrameNest uses no web
  search or deep research); no fork and no large modularity in FrameNest; the
  NUC is a development tool where data loss is acceptable and family use is far
  away; the NUC should later share the same Mullvad exit node and tailnet
  position as the PC (same IP), and an admin may occasionally need to solve a
  challenge or re-login interactively — the VNC/noVNC view plus the wizard is
  the admin tool for that. The Cooperator also reported having locked himself
  out of the NUC while working on the exit-node setup; current Orchestrator SSH
  access works.
- **2026-09-23 — NUC visible-browser login staged.** Under the Cooperator's
  direct-ops authorization: installed Google Chrome for Testing 154.0.8037.57
  (official Google CfT build, SHA-256 `ceee2972…`, extracted to
  `/opt/framenest/tooling/chrome-for-testing/154.0.8037.57/`, sandbox helper
  setuid root, symlink `/usr/bin/chromium` — the distro Chromium is snap-only
  and cannot serve the `framenest` service account); added the scoped AppArmor
  profile `/etc/apparmor.d/framenest-chrome` (userns for the CfT binary path
  only) to satisfy Ubuntu 24.04's unprivileged-userns restriction; installed
  and started transient units `framenest-xvfb` (:99, 1280x800, `-ac`),
  `framenest-x11vnc` (127.0.0.1:5901, `-localhost -nopw`), `framenest-novnc`
  (websockify 127.0.0.1:6080 -> 5901) and `framenest-vnc-browser` (headed CfT
  as framenest, profile `/var/lib/framenest/chatgpt-page/chromium-profile`,
  `--password-store=basic`, `https://chatgpt.com/`). The Cooperator logs in
  through the loopback noVNC view over his own SSH tunnel; the wizard path and
  the no-live-profile-copy boundary are preserved. Next after the login: stop
  the browser unit, run the kernel login/metrics check with the same profile,
  capture the locator evidence, then tear the view units down.
- **2026-09-23 — Node bootstrap done; Chromium blocker; profile decision open.**
  Under the Cooperator's 2026-09-23 explicit direct-ops authorization ("read
  write aj cez ssh … takéto triviálne veci rieš ty"), the Orchestrator installed
  pinned Node.js v22.23.2 on the NUC: official nodejs.org tarball, SHA-256
  verified (`d60acfe0…`), extracted to
  `/opt/framenest/tooling/node/node-v22.23.2-linux-x64`, symlinked
  `/usr/local/bin/node`; verified as the service account: plain `node` resolves,
  `v22.23.2`, `typeof WebSocket` = `function`. Rollback: remove the symlink and
  the tooling directory. Also created the planned kernel state directories
  `/var/lib/framenest/chatgpt-page` (0700) and `/run/framenest/chatgpt-page`
  (0750), owner `framenest:framenest`. Chromium finding: the host has only snap
  Chromium (`/usr/bin/chromium-browser` is the snap launcher); snap Chromium
  cannot serve the `framenest` service account (passwd home `/nonexistent`,
  profile outside `$HOME`, cgroup warning), so an unconfined Chromium-family
  browser is required. Planned ops route: pinned Chrome for Testing
  `154.0.8037.57` under `/opt/framenest/tooling/` plus a `/usr/bin/chromium`
  symlink. Open Cooperator decision: the NUC Chromium profile — the Cooperator
  asked for "the profile I have here on the PC"; the handout forbids reading or
  copying live browser profiles and Linux keyring encryption makes a copy
  unreliable, so the recommended path remains the NUC wizard login.
- **2026-09-22 — S3 preflight PARTIAL accepted; Node bootstrap decision
  pending.** `04_report_00.md` (session 04, exchange 01) stopped correctly at
  stage 2: the NUC's plain `node` resolves to `/usr/bin/node` `v18.19.1`,
  below the Node 22 planned baseline, and `typeof WebSocket` is `undefined`
  while the copied CDP client requires the global `WebSocket`. No state
  directory, profile, browser action, or credential contact occurred; terminal
  `sudo -K` released. Repository, release, and NUC `current` remain at
  `26d28b1`. Cooperator decision pending: authorize one bounded Node >= 22
  bootstrap on the NUC (recommended: pinned official Node.js v22.x LTS
  tarball, checksum-verified, under `/opt/framenest/tooling/node/`, plus a
  `/usr/local/bin/node` symlink so plain `node` resolves for the service
  account), then re-run the S3 preflight from stage 2.
- **2026-09-22 — Deployment accepted; S3 locator-probe grant issued.** The
  deployment report `03_report_00.md` (session 03, exchange 01) is
  `deployment-PASS`: public `main` and live NUC `current` both equal
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81`, service active, schema `0033`,
  backup ready, vendored kernel present, rollback target
  `/opt/framenest/releases/a4193d4f…`, `sudo -K` released. Public `main` was
  independently re-read by the Orchestrator. The Worker observed that public and
  local `main` were already published before its stage 2 ran (local reflog
  fast-forward at 21:55:21); the Orchestrator did not perform that push and
  will confirm the actor with the Cooperator. Issued `04_locator_probe_00.md`
  (session 04, exchange 01, `fresh-worker-session`, Fresh Evidence Probe,
  Phase Preflight, High, report `04_report_00.md`): NUC page-runtime preflight
  (Node baseline, Chromium candidate, release entry point, installed pack
  SHA-256), bounded state-dir setup, first household login through the deployed
  wizard with the Cooperator completing the login, sanitized composer/login-wall
  evidence, cleanup. No ask, no upload, no service start.
- **2026-09-22 — Publication + minimal-kernel deployment grant issued.**
  Cooperator authorized starting the live phase. Issued `03_deployment_00.md`
  (session 03, exchange 01, `fresh-worker-session`, Bounded NUC Deployment,
  High, report `03_report_00.md`). Scope: publish `main` by fast-forward to
  `26d28b16c08a5e7e0179a32c16646bfdc1009c81` (the only Git write), then
  `deploy/ubuntu/framenest-release` status → check → deploy, with the
  documented exit-13 schema-jump annex if the catalog revision differs;
  rollback target is the current NUC release from status; the page provider
  stays unregistered and unselected. Cooperator preconditions: NUC sudo
  timestamp outside the Worker and `FRAMENEST_NUC_SSH_*` exported into the
  Worker environment.
- **2026-09-22 — S2 accepted; live-phase decision pending.** S2 implementation
  PASS (`02_report_01.md`, commit `26d28b16c08a5e7e0179a32c16646bfdc1009c81`)
  reconciled by direct Orchestrator verification: 14 new files within the
  allowlist, vendor tree, `pyproject.toml`, and `poetry.lock` unchanged, push
  confirmed by `git ls-remote`, and the recorded gate re-run directly
  (`45 passed in 1.92s`). No independent acceptance required by the adopted
  plan. Next: Cooperator decision on starting the live phase — publish `main`
  at `26d28b1` and deploy the minimal kernel to the NUC through
  `deploy/ubuntu/framenest-release`, so the S3 locator probe can run against
  the immutable release. The synthesized plan recorded deployment between S4
  and S5, but its own reason (live probes run against the immutable release)
  requires it before S3; raised for Cooperator decision.
- **2026-09-22 — S1 accepted; S2 grant issued.** S1 implementation PASS
  (`02_report_00.md`, commit `0fd21b989814b7c0b78d517996812750a823ff10`)
  reconciled by direct Orchestrator verification: 43 changed files within the
  allowlist, `poetry.lock` unchanged, vendor tree stripped with no forbidden
  imports and upload still disabled, branch push confirmed by `git ls-remote`,
  and the recorded gate re-run directly (`28 passed in 3.03s`). No independent
  acceptance was required by the adopted plan. Issued S2 grant
  `02_probe_tooling_01.md` (session 02, exchange 02, `current-worker-session`,
  Medium, allowlist `src/framenest/infrastructure/ai/chatgpt_page/**` and
  `tests/unit/infrastructure/ai/chatgpt_page/**`, one commit on
  `feat/chatgpt-page-ask-kernel`, report `02_report_01.md`). Scope: offline
  envelope encoder, deterministic ZIP packer, byte accounting and budget
  profile contract, generated fixtures, sanitized receipts, cancellation.
  Delivery: same Worker chat as S1, Plan Mode off.
- **2026-09-22 — S1 fresh-session reissue.** Cooperator selected a genuinely
  fresh session for S1; the prepared current-session prompt
  `01_implementation_02.md` (session 01, exchange 03) produced no outcome, is
  superseded, and was observed absent from this trace directory before this
  grant (no Worker report exists; no repository mutation occurred). Issued
  `02_reimplementation_00.md` (session 02, exchange 01,
  `fresh-worker-session`, Fresh Implementation Worker, native Plan Mode
  not-used, High, same scope, allowlist, branch, and 40-hex pin; report
  `02_report_00.md`). No S1 mutation exists in the repository. Delivery: new
  Worker chat, Plan Mode off.
- **2026-09-22 — S1 exchange-02 BLOCKED accepted; corrected grant issued.**
  Read-only reconciliation of `01_report_01.md` (session 01, exchange 02,
  BLOCKED, prerequisite stop). The exchange-02 grant quoted the 39-hex
  transcription `7478ddb07d2c391f79e1aa1441f0115a31c45d8`; live
  `git rev-parse HEAD:.ap` and the `.ap` detached HEAD are
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` (40 hex, re-verified; the same
  39-hex defect appeared in the first draft of this reissue and was corrected
  before delivery). No vendor copy, branch, commit, or push occurred; FrameNest
  clean at `7ff6546f…` on `feat/x-meme-browser-companion`; vendor tree and
  `feat/chatgpt-page-ask-kernel` absent. Issued corrected S1 grant
  `01_implementation_02.md` (session 01, exchange 03,
  `current-worker-session` renewed from the exchange-02 BLOCKED report, native
  Plan Mode not-used, High, one commit on `feat/chatgpt-page-ask-kernel`,
  report `01_report_02.md`). D13 carries the verified 40-hex pin. Delivery:
  paste into the same Worker chat that received `01_implementation_01.md`,
  Plan Mode off.
- **2026-09-22 — S1 grant issued.** Cooperator approved the two-plan synthesis
  and slice order. Issued S1 implementation grant `01_implementation_01.md`
  (session 01, exchange 02, current-worker-session, native Plan Mode not-used,
  High, one commit on `feat/chatgpt-page-ask-kernel`, report
  `01_report_01.md`). Scope: vendor copy + strip + packaging + offline
  validation only; no provider registration, no upload enablement, no protocol
  bump, no `main` publication.
- **2026-09-22 — Two-plan synthesis.** Planner report `01_report_00.md` (Plan A,
  AP terminal report, PASS) reconciled against Cooperator-supplied alternative
  `01_plan_00.md` (Plan B, produced outside AP routing; planning evidence, not
  an AP report). Both read in full; key claims re-verified read-only against
  FrameNest HEAD `7ff6546f…` and Kronika `66c40d43…`. Verdict: adopt Plan B as
  the primary technical spine merged with Plan A's verified simplifications and
  error map. Recorded in `01_orchestrator_synthesis.md`. Correction recorded:
  my `01_planning_00.md`/`00_notes.md` AP pin string is one hex character short
  (39 chars, `…391f…`); the recorded gitlink and detached HEAD are
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. Prompt file not rewritten; future
  grants quote the correct pin. S1 implementation grant awaits Cooperator
  approval of the synthesized slice order.
- **2026-09-22 — Restore + first Planner.** Read-only restore of both checkouts
  verified: FrameNest HEAD `7ff6546f345827d6df20bd5b13d5e57cb4bc90db`
  (`feat/x-meme-browser-companion` = `origin/main`, clean), `.ap` gitlink
  `7478ddb07d2c391f79e1aa1441f0115a31c45d8`; Kronika `main` =
  `66c40d43c577276b0ad304a494fbbb1ffb6fc933`, tree `848f2474…`, no parents,
  lab 190, clean. Handout expected "no remote": the checkout carries `origin`
  plus predecessor branches `public/kronika-initial` and
  `work/kronika-clean-start`; classified `unrelated-owner-work`, preserved, no
  ref edits, no push. Michal confirmed continuation. Frame constants at HEAD
  still match handout §3 (3/3/1024 px, VLM JPEG 3, contact sheet 5). Issued
  Planner grant `01_planning_00.md` (session 01, exchange 01, fresh, native
  Plan Mode required, Extra High, no Max, manual delivery, approval-gated plan,
  report `01_report_00.md`). Planner grants no implementation authority.
- **2026-09-22 — Cooperator boundary.** Kronika and FrameNest stay two
  projects and two handouts. This whole may copy Kronika source code only,
  from commit `66c40d43`, into the FrameNest repo. No docs, no handouts,
  no Kronika product prose. Kronika's own next whole is
  `kronika-tailnet-family-library` and is not implemented here. The NUC
  analysis path uses one shared ChatGPT page session. Video identification
  uses many downscaled frames in one zip. Genre is not the vision model's
  job unless the title cannot be identified.

## Open gates

- First Worker is a Planner. Native planning mode required.
- Re-verify Kronika commit `66c40d43` before copying source code.
- Do not copy anything except the allowlisted source files.
- Do not push Kronika. Do not add its `origin` in this whole.
- Do not delete the existing OpenAI-compatible providers; a later VPS line
  may still need them. This whole's NUC analyze path is the ChatGPT provider.

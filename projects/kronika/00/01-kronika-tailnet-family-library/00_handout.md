# Fresh Orchestrator restoration — successor whole `kronika-tailnet-family-library`

Updated **2026-09-23** with the Cooperator's NUC refocus and the full findings of
the parked FrameNest whole. This handout restores a fresh Orchestrator for this
logical whole. It does **not** reopen the closed whole
`kronika-public-identity-and-clean-start`. The closed whole is frozen: do not
re-plan it, do not re-issue its slices, do not move its refs.

Cooperator direction (2026-09-23): the immediate focus of this whole is the
**home NUC** — Kronika running there as the household capture host and service:
one **persistent** owned ChatGPT browser on the shared household ("temp")
account, admin-handled login/challenges through a visible browser view, and a
loopback service/endpoint that FrameNest (parked) can later call without
problems. The family surface over Tailscale remains this whole's broader goal.
See §4, §5, §6.

```text
STOP: Do not implement product code yourself. Issue Workers.
STOP: The first Worker of this whole is a Planner (session 01, exchange 01),
      native planning mode required, fresh session, manual dispatch. Do not
      skip to implementation.
STOP: Do not reopen kronika-public-identity-and-clean-start. Do not re-issue
      S1-S5, C1, A1, or A2. Its closure is final. Its publication state is
      recorded in §2 and §9; nothing else about it is live.
STOP: Do not push, force, rebase, or move any ref without an explicit new
      Cooperator publication grant. Public main is already published; the
      lab/work refs remain unpushed.
STOP: Do not recreate or delete lab/cli-chatgpt-190, work/kronika-clean-start,
      or public/kronika-initial.
STOP: Do not open, quote, copy, or display docs/environment.md. It is absent
      from the public tree; it exists only on the unpushed lab history.
STOP: Do not read live ChatGPT cookies, tokens, browser profiles, or state
      directories. Interactive login happens only through the visible browser
      view, typed by the Cooperator.
STOP: Do not touch the FrameNest repository, its NUC release, its services, or
      its tooling paths. FrameNest is parked; its trace is read-only reference.
STOP: Do not fork, vendor, or share code between Kronika and FrameNest, and do
      not build large modularity in this whole. Each project owns its own code;
      only the concept and the integration contract are shared.
STOP: Do not upgrade AP. The pin on each repository governs that repository.
STOP: Do not spawn Workers or subagents. Manual dispatch.
STOP: Communicate with Michal in Slovak. Feminine self-reference. Masculine
      address for him.
STOP: Extra High. No Max unless Michal selects it.
STOP: Terse "ok" / "ano" / "pokracuj" continues the current slice. It never
      selects a new whole.
```

Paste seed for a new Agent chat (pointer only, not durable authority):

```text
Resume the AP-integrated Kronika project as a fresh Orchestrator for the
successor whole kronika-tailnet-family-library, refocused (2026-09-23) on
running Kronika on the home NUC as the household capture host and service.
Read /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/00_handout.md
completely before any Worker prompt.
Begin read-only. Restore canonical state, the declared AP pin, the observed NUC
environment, and the parked FrameNest findings.
Do not mutate. Do not implement product code. Do not push. Do not reopen the
closed whole and do not touch FrameNest.
Then open this whole's first Planner (session 01) with native planning mode ON.
Communicate with Michal in Slovak. Extra High. No Max.
```

---

## 0. Handoff identity

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Orchestrator profile: terminal-capable repository and operations coordinator
Capability profile: Orchestrator
Live handout: 00_handout.md (this file; supersedes the 2026-09-22 version)
Superseded handouts: predecessor 00_handout.md, 01_handout.md, the misplaced
  02_handout.md, and the 2026-09-22 version of this file
Logical whole identity: kronika-tailnet-family-library
Predecessor whole: kronika-public-identity-and-clean-start (closed, published)
Parked sibling whole: framenest-nuc-chatgpt-analyze-provider (FrameNest;
  trace under /home/agile/meta/projects/framenest/13/)
Current phase: restoration, then the whole's initial planning (Planner)
Native planning mode for the first Worker: required (Planner)
Reasoning recommendation: extra-high
Internal delegation: one accountable active Worker; never spawn
Cooperator: Michal
Lab checkout: /home/agile/Tools/cli_chatgpt
Intended public repository: https://github.com/cisarik/kronika (main published
  at the accepted root; re-verify)
Pinned protocol: .ap gitlink -> https://github.com/cisarik/ap.git
AP pin (verify, do not upgrade):
  7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Predecessor trace directory:
  /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
This trace directory:
  /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/
External analytic trace: /home/agile/meta  project key kronika
NUC host (target of this refocus): home NUC, Ubuntu Server 24.04 LTS, x86_64,
  reachable over Tailscale; see §5 for the environment inventory
```

This handout grants **no** repository, Git, host, account, browser, credential,
or publication mutation authority. Those arrive only in complete Worker prompts.

## 1. First thirty minutes

1. Read `AGENTS.md` in the lab checkout (Kronika product rules).
2. Read `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`,
   `.ap/PROMPT_CONTRACTS.md` (Implementation Authority Record), and
   `.ap/ARTIFACT_LIFECYCLE.md`.
3. Read this handout completely, especially:
   - §4 Cooperator direction (the NUC refocus),
   - §5 NUC environment and browser/Cloudflare findings,
   - §6 the Planner brief (what already exists and what must be planned).
4. Read the predecessor's frozen notes and closure in
   `.../00-kronika-public-identity-and-clean-start/00_notes.md`, plus
   `09_report_00.md` and `01_report_00.md` in that same predecessor directory.
5. Optional, read-only reference (parked FrameNest findings; do not touch its
   repository, NUC release, or services):
   `/home/agile/meta/projects/framenest/13/00-framenest-nuc-chatgpt-analyze-provider/`
   — especially `00_notes.md`, `03_report_00.md`, and `04_report_00.md`.
6. Re-measure §2 read-only. If anything does not hold, stop and tell Michal.
7. If it holds: write **one** Planner grant to `01_planning_00.md` in this
   directory (Worker session 01, exchange 01, fresh session, native planning
   mode required, manual dispatch, extra-high). The grant must carry §6's
   "what exists / what must be planned" brief and must cover the NUC focus, not
   only the original family-surface scope.
8. Give Michal the path. Stop at the dispatch boundary.

Do not implement this whole yourself. Do not reopen the closed whole.

## 2. Claimed state to re-verify (read-only, first)

```bash
cd /home/agile/Tools/cli_chatgpt
pwd -P
git branch --show-current
git rev-parse HEAD
git log -1 --format='%H%n%P%n%T%n%s'
git rev-parse refs/heads/main
git rev-parse refs/heads/public/kronika-initial
git rev-parse refs/heads/work/kronika-clean-start
git rev-parse refs/heads/lab/cli-chatgpt-190
git rev-list --count refs/heads/lab/cli-chatgpt-190
git status --porcelain
git remote -v
git rev-parse HEAD:.ap
git -C .ap rev-parse HEAD
test ! -e docs/environment.md
test ! -e docs/human-steps.md
test ! -e docs/ROADMAP.md
test -f README.md && test -f SECURITY.md && test -f CONTRIBUTING.md
git ls-remote --heads https://github.com/cisarik/kronika.git
sha256sum /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/09_report_00.md
```

Observed on 2026-09-23:

```text
branch                    main
HEAD                      = main = public/kronika-initial
                            66c40d43c577276b0ad304a494fbbb1ffb6fc933
parents                   none (parentless root)
tree                      848f247434deea4c217170c012612b39e41557f3
subject                   feat(kronika): introduce the household research library
work/kronika-clean-start  30e02a327e63255e1a02ec8c0709c15b38988191
lab/cli-chatgpt-190       2727451d2502925377637e19fa435917c970a996 (190 commits)
worktree                  clean
AP pin                   7478ddb07d2c3911f79e1aa1441f0115a31c45d8 in gitlink
                         and in .ap HEAD
remote                    origin = https://github.com/cisarik/kronika.git
                         (present; added after the 2026-09-22 handout was written)
public repository         refs/heads/main = 66c40d43c577276b0ad304a494fbbb1ffb6fc933
                         (published; no other heads)
absent files              docs/environment.md, docs/human-steps.md,
                         docs/ROADMAP.md
present files             README.md, SECURITY.md, CONTRIBUTING.md
A2 report SHA-256         daec731e81ea73918401b0d9d1d2cf75dd94dbb3a77e92b8fff208ad2f19b1c3
```

Also prove, without mutating: `git merge-base --is-ancestor` of the lab tip
against `main` exits 1 (no lab ancestry), and the previous root
`827dae85c2794914c3adcb467de9b21ee8998463` survives only in the reflog and the
Meta evidence.

Note: the successor `00_notes.md` (written 2026-09-22) still says "Do not push.
Do not add `origin` unless a later publication grant says so." That text is
stale where it conflicts with the observed state above; this handout is the live
restoration text. Do not rewrite the notes history; reconcile in the notes only
if a future Orchestrator needs to.

If the public repository has other heads, or any expected value differs, stop
before any publication recipe and tell Michal.

## 3. What the closed whole delivered

| Step | Evidence |
|---|---|
| Product thesis and Git split | `00_notes.md` |
| Accepted plan (Planner session 01) | `01_report_00.md` |
| Boot commit | `3c345cb` — LICENSE, `.gitignore`, Kronika AGENTS identity |
| S1 identity rename | `1c8a659` — package/CLI/XDG `kronika`, 1192 tests claimed OK |
| S2 stub removal | `f253924` — 1187 tests OK |
| S3 Obscura removal | `dc44cfd` — Chromium-only, 1181 tests OK |
| S4 public documentation | `b5b5f381` — README/SECURITY/CONTRIBUTING/usage; private docs removed |
| S5 parentless root | `827dae85` — A1 accepted (superseded by C1) |
| C1 A1-F01 correction | `30e02a3` on the work branch; new root `66c40d43` |
| A2 correction re-acceptance | `09_report_00.md` — acceptance-PASS, A1-F01 `verified-closed` |
| Publication | observed 2026-09-23: public `main` = `66c40d43`; lab/work refs unpushed |

Accepted decisions still in force (see the frozen `00_notes.md`): product name
Kronika; one household; durable shared library; opt-in share; no group chat,
notification, watch, scheduler, or ChatGPT-history framing; internal
compatibility identifiers preserved; family access is the successor whole;
native share apps and the desktop family-admin surface come later; MIT license;
unofficial/AS IS/no-affiliation posture.

## 4. Cooperator direction 2026-09-23 — the NUC refocus

The Cooperator is parking FrameNest and continuing Kronika. He returns to
FrameNest when a Kronika endpoint exists that FrameNest can call "without
problems". The immediate Kronika work happens on the **home NUC**:

1. **Kronika on the NUC as the capture host and service.** The NUC (not the
   Cooperator's PC) is the place where the household ChatGPT browser and
   library live. The service must survive browser-session realities (see §5.5).
2. **One persistent owned browser, no rapid restarts.** A single Chromium
   process, kept alive, holding the logged-in household session. Repeated
   browser restarts correlate with Cloudflare flagging the profile (§5.5).
3. **One shared household ("temp") account.** The account is de facto for the
   whole family. Login and occasional Cloudflare challenges are handled by the
   Cooperator as admin, interactively, through a visible browser view (§5.3).
   Jobs should pause and resume around such interventions.
4. **A loopback service/endpoint that FrameNest can call later.** FrameNest's
   need is one ask with one attachment (a ZIP of downscaled JPEG frames) and a
   text answer, plus typed errors. FrameNest at that point no longer runs its
   own page driver in production; it calls Kronika. The endpoint must be stable
   and documented enough for FrameNest to consume without problems.
5. **The family surface over Tailscale remains this whole's broader goal**, but
   the NUC service comes first.
6. **Separation, no fork, no large modularity.** Kronika and FrameNest are
   separate projects with separate repositories, code, services, and traces.
   They may share a concept and an integration contract, but no shared library
   and no vendored cross-copy. Do not build a shared-core framework.
7. **The NUC is a development/test machine.** Data loss is acceptable, family
   use is far away, and both projects are work in progress. Do not treat this
   as production hardening.

These are directions for planning, not locked slice boundaries. The Planner
proposes the slice order and the exact boundary; the Cooperator decides.

## 5. NUC environment: what exists and what was learned (2026-09-23)

Everything in this section was observed read-only or installed by the parked
FrameNest whole under explicit Cooperator authorization. Treat it as factual
context that must be re-verified before grants. Sanitize: no hostnames, private
network values, tokens, or paths below approved roots in artifacts or reports.

### 5.1 Host facts

- Intel NUC6i5SYH, Ubuntu Server 24.04 LTS, x86_64; one `framenest` service
  account exists (uid 999, home `/nonexistent`, shell `/usr/sbin/nologin`).
- Reachable over Tailscale; SSH is the Cooperator's route. Sudo is
  Cooperator-owned: the Cooperator establishes the timestamp outside the
  Worker; Workers use `sudo -n` only, never `sudo -v`, and never handle a
  password. A password prompt after a predecessor `sudo -K` is expected
  lifecycle state, not a host defect.
- `/opt/framenest/current` is FrameNest's active release
  (`/opt/framenest/releases/26d28b16c08a5e7e0179a32c16646bfdc1009c81`), with
  FrameNest's own service active, catalog schema `0033`, backup readiness
  `ready`. **Do not disturb it.**
- Distro Chromium on Ubuntu 24.04 is snap-only: `/usr/bin/chromium-browser` is
  the snap stub and `/snap/bin/chromium` exists, but snap confinement cannot
  serve a system service account (passwd home `/nonexistent`, profile outside
  `$HOME`, cgroup/session coupling). Do not plan on snap Chromium.

### 5.2 Tooling installed (FrameNest paths; re-verify, do not hijack)

Installed 2026-09-23 under the Cooperator's direct-ops authorization, all
root-owned under FrameNest's tooling root. They are facts of the host; Kronika
planning may reuse the *knowledge* but should decide its own paths/ownership.

```text
Node.js v22.23.2
  tarball   https://nodejs.org/dist/v22.23.2/node-v22.23.2-linux-x64.tar.xz
  sha256    d60acfe00a2932254bb0ad20e01b0d74397a0875595de719654b214f4b03f307
  location  /opt/framenest/tooling/node/node-v22.23.2-linux-x64
  shim      /usr/local/bin/node  (plain `node` resolves to v22.23.2 for the
            service account; `typeof WebSocket` = "function")
  why       the vendored CDP client needs the global WebSocket; Node 18 is
            below the required baseline

Google Chrome for Testing 154.0.8037.57
  zip       https://storage.googleapis.com/chrome-for-testing-public/154.0.8037.57/linux64/chrome-linux64.zip
  sha256    ceee2972074d441ea7c4ba8bcc0eaab77e7e87680f6653d73d3065851fe10302
  location  /opt/framenest/tooling/chrome-for-testing/154.0.8037.57/chrome-linux64
  shim      /usr/bin/chromium  (the free driver candidate path)
  sandbox   chrome_sandbox root:root setuid (4755)
  AppArmor  /etc/apparmor.d/framenest-chrome grants `userns` (unconfined
            profile) only to this binary path; without it Ubuntu 24.04's
            unprivileged-userns restriction kills Chromium with
            "No usable sandbox!"
  why       an unconfined Chromium-family binary is required; snap cannot work

View packages (apt): xvfb, x11vnc, novnc, websockify
```

### 5.3 Visible-browser view pattern (the admin's window into the NUC)

The pattern used successfully on 2026-09-23: run the browser as the service
account on a virtual display and let the Cooperator watch/act through noVNC.

```text
Xvfb :99                    1280x800, -nolisten tcp -ac
x11vnc                       127.0.0.1:5901, -localhost -nopw
websockify/noVNC            127.0.0.1:6080 -> 127.0.0.1:5901
Cooperator view              ssh -N -L 6080:127.0.0.1:6080 <nuc>
                             then http://127.0.0.1:6080/vnc.html
```

All pieces ran as transient `systemd-run` units (e.g. `framenest-xvfb`,
`framenest-x11vnc`, `framenest-novnc`) and were stopped after use. Nothing is
left running. Reuse this pattern for login/challenge handling; never expose the
view beyond loopback, and never leave it up unattended.

The kernel's login wizard (`probe.mjs login`) serves a loopback page with a
per-session secret path and can drive fills/clicks/snapshots through CDP. Rules
learned: print the wizard URL only to the operator (never to a journal or
artifact); do not auto-complete the wizard before the page settles; the wizard
is optional when the Cooperator interacts directly with the visible browser.

### 5.4 Network and exit node

- NUC Tailscale 1.102.2; the tailnet exposes the Mullvad exit-node catalog
  (`*.mullvad.ts.net`).
- The NUC and the Cooperator's PC both select the same exit node,
  `cz-prg-wg-101.mullvad.ts.net` (Mullvad, Prague, online). The PC's local
  Mullvad app is disconnected, so both egress through `tailscale0`.
- Egress IPv4 is stable but distinct per client inside `146.70.129.0/24`
  (NUC `.101`, PC `.111`): the exit node NATs each client to a different
  address, so selecting the same exit node does **not** guarantee an identical
  public IP — only the same subnet/ASN.
- Plain `curl https://chatgpt.com/` receives `403` + `cf-mitigated: challenge`
  on both machines; that is normal for non-browser clients and proves nothing.
- The Cooperator's PC loads ChatGPT normally in Brave; therefore the NUC's exit
  node/subnet is not the blocker.

### 5.5 Browser, ChatGPT, and Cloudflare findings (critical for planning)

Observed 2026-09-23 on the NUC:

1. **A fresh, unauthenticated Chrome profile loads `chatgpt.com` normally, with
   and without CDP** (checked at 30 s and 90 s). The environment — exit node,
   subnet, Chrome for Testing, AppArmor profile — is healthy. CDP alone is not
   the trigger.
2. **Login requires an interactive Cloudflare Turnstile.** In the kernel's
   login flow the page reached the login form cleanly; after the login
   submission, Cloudflare's challenge appeared, the Cooperator clicked
   "I am human", and the flow then ended at `/api/auth/error` with the browser
   closing (the probe completed). Plain interactive login is expected to work
   when the page settles; automation must not rush it.
3. **Repeated rapid restarts flag a profile.** After several quick browser
   restarts (probe attempts) the logged-in profile showed `Just a moment...`
   in every launch style — CDP or not, headless or headed — and did not
   recover. Two profiles are affected on the NUC. A **fresh** profile is clean.
   A single successful manual login once survived a relaunch before the rapid
   restarts.
4. **Practical rules for the plan:**
   - One **persistent** browser process; do not restart per request.
   - Login/challenge solving is a Cooperator (admin) interactive operation
     through the visible view; jobs pause and resume around it.
   - Treat the browser profile as valued state; back it up; do not recreate it
     casually. If a profile is flagged, a fresh one works.
   - Do not auto-complete or auto-rush the wizard/auth pages.
5. **Kernel stealth is currently unusable with Chrome for Testing.**
   `probe.mjs --stealth` adds `--disable-blink-features=AutomationControlled`
   and a normal UA, but the launch fails with `E_DRIVER_VERSION` because
   `parseChromiumMajorVersion` expects `Chromium|Chrome <digits>` while CfT
   prints `Google Chrome for Testing …`. Planning may include a bounded fix, or
   avoid stealth, or prefer headed-on-Xvfb operation.

### 5.6 FrameNest state on the NUC (parked; do not disturb)

- FrameNest whole `framenest-nuc-chatgpt-analyze-provider`, trace:
  `/home/agile/meta/projects/framenest/13/00-framenest-nuc-chatgpt-analyze-provider/`.
- Delivered before parking: S1 vendored a stripped ask/bridge/login kernel at
  `vendor/kronika-ask` (commit `0fd21b9`); S2 added offline probe tooling and a
  budget contract (commit `26d28b1`: frame envelope 480 px/q60 → 480 px/q50 →
  384 px/q50, deterministic ZIP, byte accounting, budget profile with an
  `N >= 12` floor, sanitized receipts, cancellable harness); publication of
  `main` and deployment to the NUC via `deploy/ubuntu/framenest-release`.
- S3 (live locator probe) is blocked by the Cloudflare findings above; the
  FrameNest trace holds the full evidence.
- FrameNest's future need from Kronika: one ask with one attachment (a ZIP of
  downscaled JPEG frames) and a text answer (title-first identification), plus
  typed errors. Its budget/profile design is reference knowledge, not shared
  code.

## 6. What the Planner must plan (brief; do not pre-decide)

What already exists (verify and reuse as knowledge, not as shared code):

- The closed Kronika app at `66c40d43` (ask/bridge/library/manager/login) with
  its own tests and its bridge/job model.
- A working vendored ask/bridge/login kernel copy on the NUC under FrameNest,
  plus the observed login/Cloudflare behavior, the browser tooling, the view
  pattern, and the budget/attachment learnings in the FrameNest trace.
- The host facts in §5, including the exit-node arrangement.

What must be planned (concrete questions for the Planner):

1. **Kronika on the NUC**: how Kronika's code, virtual environment, service
   account/paths, state, and supervision get to and run on the NUC; a
   Kronika-owned deployment route (FrameNest's release helper is FrameNest-only
   and must not be reused); coexistence with FrameNest's running service.
2. **The persistent browser**: one owned Chromium process kept alive; headed on
   Xvfb versus headless; when and how the login wizard runs; how the profile is
   stored, protected, and backed up; anti-detection posture (stealth fix or
   not); explicit no-rapid-restart rules.
3. **Login, challenges, and the shared account**: initial login and later
   Turnstile/expiry handling as admin-interactive operations; how the service
   detects a challenge, pauses, notifies the Cooperator, and resumes; what
   "one shared temp account for the family" means operationally.
4. **The service/endpoint**: loopback API shape for asks (one ask, one
   attachment), authentication, typed errors, job model (reuse the existing
   bridge/job semantics where sensible), status/observability; specifically
   documented so FrameNest can call it later without problems. State whether
   this is the same manager/bridge or a new surface, without weakening the
   existing loopback invariants.
5. **Attachment support**: the closed whole deliberately rejected file upload
   (verified closed by A2); the NUC service now needs one attachment (a ZIP of
   JPEG frames, one media file, bounded bytes). This is an explicit scope
   change to plan with the same security discipline: bounded sizes, private
   staging, no client paths, cleanup, no path traversal, typed failures.
6. **The family surface**: the original whole goal — a family-reachable,
   authenticated library over Tailscale; the Planner proposes whether it comes
   before or after the NUC service (the Cooperator wants the NUC first) and how
   authentication/hardening evolve without weakening existing contracts.
7. **Host/network posture**: Tailscale and the shared Mullvad exit node;
   hardening a non-loopback surface only when the family surface slice starts;
   what remains Cooperator-owned (network, account, challenges).
8. **Acceptance shape**: what evidence the Cooperator can provide (he watches
   the view and performs challenges; rendered UX acceptance is his); what the
   Worker environment can verify without NUC credentials.

Constraints the plan must respect: no fork, no shared library, no large
modularity; Kronika and FrameNest stay separate; do not touch FrameNest's NUC
artifacts; AP pin governs; sanitize all evidence; the NUC is a development/test
machine where data loss is acceptable.

## 7. Product thesis and successor scope

Kronika is a **household chronicle**: searches and deep research the family
wants to reopen. Not ChatGPT history. Not a group chat. Not a replacement for
Signal or mail.

```text
one capture host     = the home NUC: Plus/Pro + Chromium + library + service
                       (2026-09-23 refocus: persistent browser, shared household
                       "temp" account, admin challenge handling)
family phones        = a reachable, authenticated family surface over Tailscale
                       (this whole's broader goal)
ChatGPT project web  = scratch; Kronika is the archive
share                = opt-in
authoring + check    = kept
desktop extension    = later family-admin surface
Android/iOS share    = later, after this whole
FrameNest            = separate parked sibling; later a client of a Kronika
                       endpoint (one ask + one attachment)
```

The whole owns: the NUC capture-host service first, then the family-reachable
authenticated library surface, the Tailscale/network topology, authentication
for family members, and the minimum hardening a non-loopback surface requires.
It does not own native share apps, the desktop family-admin extension, remote
conversation deletion, or external LLM integrations beyond the ChatGPT page
service.

The loopback-only boundary is a shipped security invariant today. Any change to
it must be explicit, planned, independently accepted, and must not weaken the
existing token, Host/Origin, render-key, or account-scope boundaries.

## 8. Backlog and ledger candidates carried forward

Non-authorizing observations. Do not implement without a grant; the Planner may
adopt any of them into this whole or park them again.

1. Parked test-isolation ordering dependency: the four quiet-stderr tests in
   `tests/unit/test_client.py` fail in a focused module set that omits
   `tests.unit.test_bridge_startup`, because `logging.basicConfig` has not been
   installed. The declared full route passes. Classified pre-existing,
   explicitly parked.
2. Minor wording residuals, non-blocking: `--file` help and the engine comment
   are shorter than the canonical `file upload is not available in this build`
   sentence; `extension/src/headless/runner.mjs` carries no upload message
   field. The NUC attachment slice will revisit upload semantics anyway.
3. Frozen `docs/contracts/manager-surface-v3.md` through `v5` still name the
   predecessor executable `chatgpt-cli library ui`; v6 and `docs/usage.md`
   name `kronika`. Frozen history, not an active advertisement.
4. Six local `refs/codex/turn-diffs/checkpoints` refs exist, are not remotes,
   and are outside the four named branches. Do not push or delete them.
5. Root CLI help uses the word "diagnostics" only in the sentence about stderr
   progress; that is not a command.
6. `probe.mjs` creates the caller-supplied profile directory before refusing
   to start a missing Chromium binary (`E_PROBE_CHROME_MISSING`).
7. File upload remains unavailable in the closed whole by design; the NUC
   service reopens it deliberately (§6 item 5).
8. The closed whole's `docs/environment.md` is deleted from the public tree and
   exists only on the unpushed lab history. Never open or copy it.
9. New (2026-09-23): `parseChromiumMajorVersion` cannot parse Chrome for
   Testing's version string, which disables `--stealth` with CfT.
10. New (2026-09-23): snapshot of the NUC tooling/AppArmor/view setup in §5.2
    and §5.3; verify before reuse and decide Kronika-owned paths.
11. New (2026-09-23): FrameNest's offline probe tooling and budget contract
    (trace above) is reference knowledge for the NUC attachment policy; do not
    copy code.

## 9. Publication

Observed 2026-09-23: the public repository `cisarik/kronika` has exactly
`refs/heads/main` = `66c40d43c577276b0ad304a494fbbb1ffb6fc933`, the accepted
root. The local checkout carries `origin` for that repository. The lab and work
refs remain local and unpushed. Re-check immediately before relying on this.

Rules:

- Do not push, force, delete, or move any ref without a new explicit Cooperator
  publication grant that names the exact refspec.
- Never push `lab/cli-chatgpt-190`, `work/kronika-clean-start`, or
  `public/kronika-initial`.
- Any later publication of new commits (NUC service work) is a separate
  Cooperator-owned grant sequence: exact accepted commit, non-force push of the
  named ref, and direct public readback.

## 10. How to lead Michal

Slovak, masculine address, feminine self-reference. One outcome paragraph plus
one dispatch instruction. Do not lecture AP, do not dump protocol, do not
re-open naming, do not ask him to choose among locked decisions. When he is
confused, name the file to paste and the chat that should receive it.

Pattern:

1. Restore and verify read-only. Tell him what is true in one block.
2. Write the next Worker prompt to the exact Meta path.
3. Tell him: new Agent chat (or the same chat for a renewed exchange), Plan
   Mode ON or OFF as the prompt declares, Extra High, no Max, paste that file.
4. When the report lands, read it from disk, reconcile it against git and the
   host evidence, then write the next grant.

He sends Worker results back to you. You are the Orchestrator, not the Worker.

## 11. Worker grant quality bar

Every grant is a complete new authority, not a delta chat. Use the shape the
predecessor prompts established (`02_implementation_00.md`,
`05_implementation_00.md`, `07_acceptance_00.md`): exact baseline and allowlist,
repository gate, positive and negative authority, declared execution route,
staging and commit rules, stop conditions, report contract, and the external
trace / delivery record. Bind the project-declared execution route: tests
`python -m unittest discover -s tests -t .`; CLI `python -m kronika`; bridge
`python -m kronika bridge`. `python` is `.venv/bin/python` when the venv is
active.

NUC host rules for grants that touch the host:

- SSH is the Cooperator's capability; Workers must never print or store
  transport values, sockets, hostnames, or private network values.
- Sudo is Cooperator-owned: the Cooperator establishes the timestamp outside
  the Worker (`sudo -v`, then `sudo -n true`); Workers use `sudo -n` only,
  never `sudo -v`, never handle a password, and release at the terminal report
  where the task requires it. A password prompt after a predecessor `sudo -K`
  is expected lifecycle state.
- Never disturb FrameNest's release, service, state directories, or tooling
  paths. Sanitize every diagnosis: versions, counts, booleans, and hashed or
  masked values instead of secrets and private identifiers.
- Browser work: loopback only; the wizard URL is a secret; never read cookies,
  tokens, or profile internals; prefer a single persistent browser over
  restarts.

Git safety, binding for every grant: never update git config; never force,
hard-reset, or clean to manufacture state; never `--no-verify` /
`--no-gpg-sign`; never `git add -A` / `git add .`; never amend unless all local
amend conditions hold and Michal asked; never push unless a publication grant
names the exact refspec; never push the lab or preparation refs.

Meta grammar (`/home/agile/meta/README.md`): Worker prompt/report pairs use
`<session>_<phase>_<exchange-minus-one>.md` and
`<session>_report_<exchange-minus-one>.md`; a new Worker session starts at
`_00`. Handouts and closures share their own sequence; the next prefix in this
directory starts at `00`.

## 12. First Worker you issue

The whole's first Worker is its Planner:

```text
Logical whole identity: kronika-tailnet-family-library
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session profile: Planner
Worker session target: fresh-worker-session
Native planning mode: required
Phase: planning
Delivery route: manual Cooperator delivery
Reasoning recommendation: extra-high
Prompt: /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/01_planning_00.md
Report: /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/01_report_00.md
```

The Planner grant must include §6's brief verbatim in substance: what already
exists (§5, §3, the parked FrameNest trace) and what must be planned (the eight
numbered areas), with the constraints and the Cooperator direction of §4. The
plan must propose the slice order with exact boundaries, dependencies, and
gates; it grants no implementation authority.

This directory and its `00_notes.md` already exist. Do not recreate them.

## 13. Success of this whole

Near-term: Kronika runs on the NUC as the household capture host with one
persistent logged-in browser, admin-handled challenges, and a documented
loopback endpoint that FrameNest can call without problems.

Broader: a family member can open the household library from a phone over
Tailscale through an authenticated, hardened surface that does not weaken the
existing loopback contracts, with its own accepted plan, implementation slices,
and fresh independent acceptance. Native share apps and the desktop
family-admin surface remain later wholes.

The predecessor whole's closure signal has been emitted. Do not emit it again
for the closed whole; this whole has its own closure decision.

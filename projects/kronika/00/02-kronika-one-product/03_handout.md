# Fresh Orchestrator restoration — `kronika-one-product` (S6 correction; PC→MacBook development migration)

Artifact relationship: **historical restoration handout**. It transfers
information, not authority. Task authority comes only from the current
authoritative Orchestrator routing and the complete Worker prompts issued from
it.

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Capability profile: Orchestrator (terminal-capable repository and operations coordinator)
Logical whole identity: kronika-one-product
Current phase: S6 acceptance-blocked correction (finding S6-A35-F01) -> fresh E3/R3 re-audit -> publication; then S4-B -> S7-P -> S8 -> S9 -> S10
Cooperator: Michal
Delivery route: manual Cooperator delivery to fresh Worker sessions
Reasoning recommendation: Extra High for the correction-scope review; High for the correction grant itself
Development host after the switch: MacBook (Wi-Fi); NUC on Ethernet; the office PC is parked and stays in the office
Trace: /home/agile/meta/projects/kronika/00/02-kronika-one-product/ (MUST travel to the MacBook)
AP pin (verify, do not upgrade): 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Handout sequence: this is 03_handout.md (predecessors 01_handout.md, 02_handout.md)
```

This handout restores a fresh Orchestrator for the **ongoing** whole
`kronika-one-product`. The whole remains open; this handout does not close it.
Restoration grants no mutation authority. It supersedes earlier narrative.

## 0. Communication and binding directives

- Communicate with Michal in Slovak, masculine address, feminine
  self-reference. Worker prompts and formal reports are English.
- Presentation: short status block, one status mark, one dispatch instruction,
  plus the visible delivery capsule (Recipient, Reasoning, Client/Native Plan
  Mode, Prompt path + SHA-256, Report path, Archival).
- **Sudo is Cooperator-owned: Workers never run `sudo -v` or `sudo -K`.**
  Michal establishes the NUC sudo timestamp before dispatch and releases it
  manually; Workers use `sudo -n` only and never handle a password.
- NUC SSH transport: the three `FRAMENEST_NUC_SSH_*` names are exported in the
  Cooperator's shell (values never printed or stored). Worker SSH to the NUC
  goes only through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`; complex shell
  blocks and interactive steps are Cooperator-executed.
- `private/**` in the FrameNest checkout is never read. Browser profiles,
  cookies, tokens and credential stores are never inspected.
- One accountable Worker at a time; no subagents. Manual dispatch by Michal in
  a fresh Agent chat per grant. Terse `ok`/`ano`/`pokracuj` means "continue the
  current slice", never a new whole.
- Only the Orchestrator closes the whole; the closure signal is
  `LOGICKY CELOK UZAVRETY`. Workers never emit it.
- The NUC is a development/test machine; data loss is acceptable. Do not treat
  it as production hardening.
- The capture host is parked: do not restart the browser, attempt the ChatGPT
  login, remove the recovery override or touch the capture state without a new
  explicit Cooperator decision and bounded grant.
- **Testing economy (Cooperator directive, binding from 2026-09-27):** do not
  run the full suite at every mini-step or fix; that is wasted effort. Use
  targeted validation and the smallest reproducer. Run the broad suite at most
  once for a final candidate when a named decision risk requires it, and never
  re-run an unchanged gate. Acceptance re-runs are bounded subsets, not
  full-suite repetitions. This directive holds until the Cooperator changes it.
- **Development-environment migration (Cooperator directive, 2026-09-27):**
  development moves from the office PC to a MacBook; the PC stays in the
  office. The NUC travels with the Cooperator and will be plugged into a new
  network (NUC Ethernet, MacBook Wi-Fi, Tailscale expected). Nothing may be
  lost; section 6 is the migration runbook.

## 1. First thirty minutes

1. Read the product `AGENTS.md` (`/new-macbook-path/framenest/AGENTS.md`),
   the pinned AP spine (`.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`,
   `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`, `.ap/ARTIFACT_LIFECYCLE.md`),
   and `/home/agile/meta/README.md` at its MacBook location.
2. Read this handout completely, then the trace: `00_notes.md` (complete),
   `36_report_00.md`/`36_publication_00.md` (S6 candidate transport),
   `37_report_00.md`/`37_deployment_00.md` (NUC accepted release),
   `35_report_00.md` (the acceptance PARTIAL with finding **S6-A35-F01**),
   `34_report_00.md`..`34_report_04.md` (S6 implementation and corrections),
   `33_report_00.md`/`32_report_00.md`/`31_report_00.md` (the frozen S6 plan),
   `25_report_00.md` (accepted modular-provider plan), `15_report_00.md`
   (S3 recovery playbook).
3. Re-measure section 2 read-only on the MacBook. If anything does not hold,
   stop and tell Michal in one block before any grant.

## 2. Claimed state to re-verify (read-only; verify on the MacBook)

GitHub `cisarik/framenest` (verify with direct `git ls-remote`):

```text
main                          40e51cb2d061ead96850c9c94aa59de54d5e1310
                              (accepted S4-A; published; latest accepted code)
feat/kronika-one-product      38e7beeb3921d7c0fd8e717e480754fbd18130c9
                              (S6 candidate transport, published 2026-09-27;
                              NOT accepted; blocked by S6-A35-F01)
feat/chatgpt-page-ask-kernel  26d28b16c08a5e7e0179a32c16646bfdc1009c81 (unchanged)
feat/x-meme-browser-companion 7ff6546f345827d6df20bd5b13d5e57cb4bc90db (unchanged)
```

S6 candidate (on branch `feat/kronika-one-product`):

```text
commit  38e7beeb3921d7c0fd8e717e480754fbd18130c9
parent  40e51cb2d061ead96850c9c94aa59de54d5e1310
tree    d6d5d314bfaf98d968235a867004b89b3187ac68
subject feat(kronika): add private records and administrator approval
diff    109 paths, all inside the effective allowlist (the 176-path union of
        33_report_00.md section 6 plus tests/support/youtube_fake_demo.py and
        tests/contract/test_youtube_fake_demo.py)
verdict independent acceptance 35_report_00.md: PARTIAL, one blocking
        correction-required finding S6-A35-F01 (high)
```

NUC (verified by deployment report `37_report_00.md`, 2026-09-27; re-verify
read-only only when a host step is planned):

```text
web release     40e51cb2d061ead96850c9c94aa59de54d5e1310 (deployed 2026-09-27;
                /opt/framenest/current and the release .framenest-release-sha
                both match)
capture release 94e605c17b881461fad3e22fd8c7fca32cb93976 (unchanged, pointer
                and unit states intact)
database        revision 0033 before the deploy; the helper reported no
                migration continuation
capture runner  active, Result=success, NRestarts=0; readiness
                browser_unavailable (E_BROWSER_UNAVAILABLE), client_connected
                true, jobs 0/0, active_job null, zero chrome/chromium
                processes (the earlier needs_admin + one Chromium claim is
                superseded as-left; no action — capture stays parked)
tailscaled      active and enabled (verify after the network move)
listeners       loopback-only: 8765 (bridge) and 53; non-loopback: 22, 443,
                631, 50216, 53809 (outside the capture boundary; note only)
```

- AP pin `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` in both repositories'
  gitlinks and `.ap` HEAD.
- Trace present on the MacBook at the path above (see section 6.1).
- The office PC checkout is parked; it is no longer the working copy.

## 3. What is done and accepted (published on `cisarik/framenest` main)

```text
S0  93e7742  docs(kronika): record one-product architecture and private records
S1  96ef426  feat(capture): relocate kernel into kronika_capture
S2  5259b89 + 82a6a59  capture submission barriers and browser lifecycle
S3  c975aba + 94e605c + d63d0b7 + e408bb5 + fd277a9  capture supervision and diagnostics
S4-D 72009c3  docs(kronika): define modular research and administrator-curated timeline
S4-A 75e9b07 + 40e51cb2  provider-neutral research contracts and configuration (main HEAD)
```

The S3 host remainder (Cooperator login, null-job resume, activation, one
synthetic ask) stays parked. S6 is implemented but **not accepted**: the
candidate is on the transported feature branch, `main` is still `40e51cb2`.
The four parked pre-existing broad-suite failures (stale `.venv`
`framenest-chatgpt-page` console script; three operator SSH-gate parameters
influenced by ambient `FRAMENEST_NUC_SSH_*` values) are out-of-allowlist
environment debt; convention: do not repair them in S6 work, and do not
re-run the broad suite merely to re-observe them.

## 4. Immediate work — correct S6-A35-F01, then re-audit

Finding `S6-A35-F01` (from `35_report_00.md`, correction-required, high):
after an administrator approves media A, an ordinary household member's
**HTTP** reads still receive the post-approval working state: `GET
/api/media/{id}` and `GET /api/media/{id}/metadata` return the current title
and category (B), the detail payload discloses a post-approval location id,
content requests for that location return `409 MEDIA_CONTENT_UNAVAILABLE`
rather than `404`, and gallery membership requires a stray legacy publication
row (an approved record without one is absent from list and total). The record
service already stores and returns the approved snapshot; the HTTP read routes
do not. Claim 3 of the acceptance is therefore not established. The LEAD
(analysis suggestions not yet proven to expose current analysis) remains an
open check.

Smallest safe correction direction (from the finding): when the access
decision is `approved`, detail, metadata, analysis, cover and content reads
must serve only the approved projection, its locations and its cover digest;
gallery membership must include that snapshot without a legacy publication
row. Required regression: approve A, change working state to B including a new
location, then household detail, metadata, list, collection filter and content
must still show A and must not accept the new location.

Sequence (one grant per row):

1. **Correction grant** (next genuinely fresh Worker session; allocate the
   ordinal at issuance and use the same effective allowlist; bounded
   correction scope; targeted tests only; no full suite).
2. **Fresh independent E3/R3 re-audit** of the corrected exact SHA (fresh
   session; bounded security subset and synthetic probes; the finding must be
   disproved by the regression and the probes).
3. **Publication** of the accepted `main` (separate Cooperator publication
   grant; non-force; direct readback).
4. **NUC update** to the accepted published SHA when a host step is authorized
   (section 6.3 runbook).
5. Then continue **S4-B -> S7-P -> S8 -> S9 -> S10**.

Recommended correction grant fields (the Orchestrator issues the actual
prompt):

```text
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Native planning mode: not-used
Phase: correction
Baseline: the corrected candidate's parent (verify at issuance)
Effective allowlist: the 176-path union plus the two demo paths; no expansion
Outcome: approved-decision HTTP reads serve the approved projection and its
  locations/cover digest; gallery membership includes approved records without
  a legacy publication row; regression per the finding
Validation: targeted affected tests plus the new regression; no full suite
Git: one local commit; no push
Stops: any out-of-allowlist path; any weakening of the authorization gate;
  an unexplained failing gate
```

## 5. Remaining slices (revised accepted order)

```text
S6 correction + re-audit + publication -> S4-B -> S7-P -> S8 -> S9 -> S10
```

- **S4-B** native provider runtime: OpenAI adapter, migration 0035, durable
  jobs, budgets, cancellation, cleanup, credential deployment source; fake
  transport only; disabled by default.
- **S7-P** common completion and rendering: atomic Q/A save, personal-history
  APIs, media-success/approval integration, safe document rendering.
- **S8** product UI: shared Timeline landing, personal history, Search/
  Research forms, administrator review; Gallery retained; no new framework.
- **S9** integrated acceptance, DB reset and deployment: fresh integrated
  acceptance, exact-object stopped-writer DB reset, Cooperator rendered
  acceptance on the exact public-main NUC release.
- **S10** public repository transition: rename `cisarik/kronika` ->
  `kronika-capture-archive`, then `cisarik/framenest` -> `cisarik/kronika`.
- **Parked independently**: remaining S3 host completion; capture-mode
  Search/Research; S5 ZIP activation; S7-C capture integration.

Each active row: one implementation grant; independent acceptance,
publication and host operations are separate grants.

## 6. PC -> MacBook development migration (Cooperator switch)

### 6.1 What must travel (carry list — nothing may be lost)

1. **The trace directory** `/home/agile/meta/projects/kronika/00/02-kronika-one-product/`
   (all prompts, reports, notes, this handout). Either commit/push the private
   meta repository from the office PC (Cooperator-owned Meta Git action) and
   clone it on the MacBook, or copy this directory to the MacBook by the
   Cooperator's own means. The MacBook cannot continue the workflow without
   it. Verify the copied/cloned file count and the presence of
   `00_notes.md`..`37_report_00.md`.
2. **The product repository**: `cisarik/framenest` clone on the MacBook
   (public). Check out `feat/kronika-one-product` for S6 correction work (or
   `main` for reading the accepted state).
3. **Cooperator-owned credentials and local values** (never committed, never
   read by agents): GitHub authentication for the MacBook, Tailscale sign-in,
   the three `FRAMENEST_NUC_SSH_*` values (names only are documented), any
   SSH key used for the NUC, and any `private/**` material the Cooperator
   chooses to keep. Decide per item whether it is needed on the MacBook.
4. **Archive checkout** `/home/agile/Tools/cli_chatgpt` (or its MacBook
   clone): historical only; the repo is on GitHub
   (`cisarik/kronika`, main `66c40d43`).
5. **Not needed on the MacBook**: `.venv` directories (rebuild), Poetry
   caches, browser profiles, the NUC's release trees.

### 6.2 MacBook setup

- Install Git, CPython 3.13, Poetry (project-supported version), Node (for
  `node --test`), and Tailscale.
- Clone the product repository; `git -C framenest submodule update --init .ap`;
  verify the `.ap` gitlink and `.ap` HEAD equal the AP pin; create `.venv` and
  install the project per `DEVELOPMENT.md` and
  `docs/WORKER_EXECUTION_CONTRACT.md`.
- Verify the declared route from the repository root before any grant:

```text
./.ap/ap project check --root <macbook-path>/framenest --baseline <current-sha>
```

- JavaScript tests: `node --test` per the repository contract. No ambient
  Python outside the declared route for evidence.
- Export the three `FRAMENEST_NUC_SSH_*` names with the Cooperator's values in
  the shell profile; never print them.

### 6.3 NUC on the new network

- Plug the NUC into the new network via Ethernet and power it on; the MacBook
  joins the same Wi-Fi. Tailscale is expected to reconnect automatically.
- From the NUC console (if available) or once reachable: verify
  `systemctl is-active tailscaled` and `systemctl is-enabled tailscaled`, and
  that `framenest.service` is active.
- From the MacBook: verify Tailscale reachability without printing addresses;
  Worker SSH to the NUC goes through the
  `framenest_nuc_worker_gate.fish` gate; `sudo -n true` must exit 0 (the
  Cooperator establishes the timestamp; Workers never run `sudo -v`/`-K`).
- Routine update to a newer accepted release, once one is published:

```text
./deploy/ubuntu/framenest-release status
./deploy/ubuntu/framenest-release check --release <published-40-hex-SHA>
./deploy/ubuntu/framenest-release deploy --release <published-40-hex-SHA> --yes
```

  The helper requires the checkout `HEAD` to equal the release and public
  `main` to equal it; use an exact temporary detached checkout only under a
  grant, and return to the working branch afterwards. Expect the capture
  pointer to stay `94e605c…`.
- The capture module stays parked; no browser restart, login, resume,
  activation or ask.
- The S9 exact-object stopped-writer DB reset remains a later separate
  Cooperator-authorized operation. Never reset or delete the database as an
  improvised fix.

### 6.4 GitHub

- `main` stays `40e51cb2` until the corrected S6 candidate is accepted and a
  separate publication grant pushes it. The S6 candidate travels on
  `feat/kronika-one-product` (`38e7bee`); future corrections accumulate on
  that branch and are pushed non-force under separate Cooperator grants.
- Never push `lab/cli-chatgpt-190` or `work/kronika-clean-start`.

## 7. Ledger candidates carried forward

Non-authorizing; do not implement without a grant:

- **S6-A35-F01** (correction-required, high) and its LEAD about analysis
  suggestions; cover-thumbnail bytes not dynamically demonstrated.
- The four parked pre-existing broad-suite failures: stale `.venv` versus the
  declared `framenest-chatgpt-page` console script; the three operator SSH-gate
  parameters influenced by ambient `FRAMENEST_NUC_SSH_*` values. A future
  environment-maintenance task may refresh the virtualenv and harden the gate
  test against ambient defaults.
- `retained_release_paths` is not called by deploy/rollback.
- The legacy DOM engine asset in the capture package; activation needs a
  durable-submission review.
- A dangling journal symlink classifies as absent.
- VNC `-nopw` with `-localhost` is by design; `mcookie` may appear in the
  Xvfb argv (not the bridge token).
- The `framenest.service` capture-token drop-in remains a host-side addition
  for S7-C, deferred from S3.
- Installed `/etc/kronika-capture/capture.env` has no `TMPDIR` assignment;
  re-check read-only if the unit or env file changes.
- Non-capture NUC listeners on 53809/50216 were never identified (outside the
  capture boundary).
- S4-A residual: a version 1/2 AI config file that already contains a
  `research` key is ignored on read and omitted on save (malformed legacy
  files only); the S4-A fix commit body carries a `Co-authored-by: Cursor`
  trailer (cosmetic).
- Model-suitability and testing-economy observations from the endgame:
  full-suite-per-fix is prohibited; targeted validation is the default.

## 8. Trace, delivery and grammar

- Trace directory: `/home/agile/meta/projects/kronika/00/02-kronika-one-product/`.
- Worker prompt/report pairs: `<session>_<phase>_<index>.md` and
  `<session>_report_<index>.md`; `index = exchange ordinal - 1`; a new session
  starts at `_00`. Handouts/closures share their own sequence: the
  predecessors are `01_handout.md` and `02_handout.md`; this is
  `03_handout.md`.
- Sessions 01–37 are used. Session 36 (candidate transport) and session 37
  (NUC accepted release) both reported PASS; their reports are in the trace.
  Session 15 and session 34 must never receive another prompt (context-full).
  The next genuinely fresh session ordinal is **38**; verify usage in the
  trace at issuance.
- Each grant is a complete new authority: identity/route, exact baseline and
  allowlist, positive and negative authority, declared execution route,
  staging and commit rules, stop conditions, report contract, trace/delivery
  record.
- Reports are delivered session-only or saved to the trace; the Cooperator
  dispatches prompts in fresh Agent chats and owns Meta Git archival.

## 9. STOP rules

- Do not implement product code yourself; issue Workers.
- Do not push, force, delete or move any ref without a new explicit Cooperator
  publication grant naming the exact refspec; never push the lab/work refs.
- Do not have Workers run `sudo -v` or `sudo -K`; Michal releases manually.
- Do not read `private/**`, browser profiles, cookies, tokens or credentials.
- Do not resume the parked capture host without a new explicit Cooperator
  decision and bounded grant.
- Do not deploy or publish an unaccepted candidate; do not reset, delete or
  rewrite the capture journal or the database.
- Do not weaken the loopback/token/Host/Origin boundaries or the sandbox.
- Do not upgrade AP; the pinned gitlink governs.
- Do not run the full suite at every mini-step/fix (testing economy).
- Do not reopen the closed whole `kronika-public-identity-and-clean-start`.

## 10. Paste seed for the successor Orchestrator chat

```text
Resume the AP-integrated Kronika project as a fresh Orchestrator for the
ongoing whole kronika-one-product (one Kronika on the FrameNest base; modular
research provider; capture parked). Development has moved from the office PC
to this MacBook; the NUC travels and is on the new network.
Read the trace handout
/home/agile/meta/projects/kronika/00/02-kronika-one-product/03_handout.md
completely, then the whole's 00_notes.md, the S6 acceptance report
35_report_00.md (finding S6-A35-F01), the S6 plan 33_report_00.md, and the
S6 implementation reports 34_report_00.md..34_report_04.md.
Begin read-only. Run the section-2 re-verification on this MacBook and the
network/NUC reachability checks. Do not mutate. Do not push without a new
Cooperator publication grant. Do not reopen any closed whole. Do not resume
the capture host login without a new Cooperator decision.
Then issue the S6-A35-F01 bounded correction grant to the next genuinely fresh
Worker session (targeted tests only; no full suite), followed by a fresh
independent E3/R3 re-audit of the corrected SHA, then a separate Cooperator
publication grant. Communicate with Michal in Slovak. Manual dispatch to fresh
Worker sessions. Workers never run sudo -v or sudo -K.
```

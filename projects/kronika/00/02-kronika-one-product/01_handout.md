# Fresh Orchestrator restoration — `kronika-one-product` (S3 host bring-up and beyond)

Artifact relationship: **historical restoration handout**. It transfers
information, not authority. Task authority comes only from the current
authoritative Orchestrator routing and the complete Worker prompts issued from
it.

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Capability profile: Orchestrator (terminal-capable repository and operations coordinator)
Logical whole identity: kronika-one-product
Current phase: S3 host bring-up, then S4–S10
Cooperator: Michal
Delivery route: manual Cooperator delivery to fresh Worker sessions
Reasoning recommendation: Extra High; no Max unless Michal selects it
Internal delegation: one accountable active Worker; never spawn
Product checkout: /home/agile/Projects/framenest
Archive checkout: /home/agile/Tools/cli_chatgpt (read-only source)
Trace: /home/agile/meta/projects/kronika/00/02-kronika-one-product/
AP pin (verify, do not upgrade): 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

This handout restores a fresh Orchestrator for the **ongoing** whole
`kronika-one-product`. It does not close or reopen any whole. It supersedes
earlier narrative; the whole remains open until its own closure decision.

## 0. Communication and binding directives

- Communicate with Michal in Slovak, masculine address, feminine self-reference
  ("overila som", "napísala som"). Worker prompts and formal reports are
  English.
- Presentation: short status block, one status mark, one dispatch instruction,
  plus the visible delivery capsule (Recipient, Reasoning, Client/Native Plan
  Mode, Prompt path + SHA-256, Report path, Archival).
- **Sudo is Cooperator-owned: Workers never run `sudo -v` or `sudo -K`.**
  Michal establishes the NUC sudo timestamp before dispatch and releases it
  manually afterwards. This is a binding Cooperator directive from 2026-09-25;
  every grant must omit any privilege-release step. Workers use `sudo -n` only
  and never handle a password.
- NUC SSH transport: the three `FRAMENEST_NUC_SSH_*` names are exported in
  `~/.zshenv` on the dev host. Never print or store their values, hostnames,
  private network values, sockets, tokens or credential material.
- Worker SSH to the NUC goes only through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`; the gate rejects
  shell metacharacters and multiline commands. Complex shell blocks and
  interactive steps are Cooperator-executed (`# [NUC / bash]` blocks).
- `private/**` in the FrameNest checkout is never read. Browser profiles,
  cookies, tokens and credential stores are never inspected.
- One accountable Worker at a time; no subagents; manual dispatch by Michal in
  a fresh Agent chat per grant. Keep terse `ok`/`ano`/`pokracuj` meaning
  "continue the current slice", never a new whole.
- Only the Orchestrator closes the whole; Workers never emit the closure
  signal. The project closure signal is `LOGICKY CELOK UZAVRETY`.
- The NUC is a development/test machine; data loss is acceptable; the family
  use is far away. Do not treat it as production hardening.

## 1. First thirty minutes

1. Read `/home/agile/Projects/framenest/AGENTS.md` (product rules, execution
   boundary, NUC release route, presentation, security/product boundaries).
2. Read the pinned AP: `.ap/AP.md` (ORCHESTRATOR spine: §2–§7,
   Plan-to-Execution, Implementation Authority, Acceptance/Correction,
   RF-01–RF-19), `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`,
   `.ap/PROMPT_CONTRACTS.md`, `.ap/ARTIFACT_LIFECYCLE.md`,
   `/home/agile/meta/README.md`.
3. Read this handout completely, especially §3–§8.
4. Read the whole's trace in order of importance:
   - `00_notes.md` (complete; the authoritative Orchestrator log),
   - `01_plan_sk.md` (locked Cooperator direction: one Kronika on FrameNest),
   - `01_report_00.md` (accepted whole plan; S0–S10, contracts, gates),
   - `15_report_00.md` (accepted S3 recovery plan; **the current playbook**),
   - `10_report_00.md` … `10_report_05.md` (classified host evidence),
   - `04_report_00.md`, `08_report_00.md`, `11_report_00.md`,
     `13_report_00.md`, `15_report_01.md`, `16_report_00.md`,
     `17_report_00.md` (S3 acceptances and corrections),
   - `02_report_00.md`, `03_report_00.md` (S2 acceptance and re-acceptance),
   - `09_report_00.md`, `12_report_00.md`, `14_report_00.md` (publications).
5. Re-measure §2 read-only. If anything does not hold, stop and tell Michal in
   one block before any grant.

## 2. Claimed state to re-verify (read-only)

Product checkout `/home/agile/Projects/framenest`:

```text
branch                    feat/kronika-one-product
HEAD                       e408bb5503f359ec24542304ac1a621c6b9e4ffb
parent                     d63d0b725acedf49d1611224c3b5201a90e7ef90
tree                       dadc01726a354c319374832bfd385be0bdffb516
subject                    fix(capture): diagnose startup and require fresh activation readiness
local main = origin/main   e408bb5503f359ec24542304ac1a621c6b9e4ffb
worktree                   clean
AP pin (gitlink + .ap HEAD) 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
public main (cisarik/framenest) e408bb5503f359ec24542304ac1a621c6b9e4ffb
other public heads         feat/chatgpt-page-ask-kernel 26d28b16,
                           feat/x-meme-browser-companion 7ff6546f
```

Archive checkout `/home/agile/Tools/cli_chatgpt` (never modified further;
source of the port): `main` = `66c40d43c577276b0ad304a494fbbb1ffb6fc933`,
clean, AP pin same; public `cisarik/kronika` main = `66c40d43`.

Host state (NUC; claims from `10_report_04.md`/`10_report_05.md` plus the
accepted plan; re-verify read-only before any host step):

```text
web release pointer       d63d0b7…   (e408bb5… is published but NOT yet deployed)
capture release pointer   94e605c…
units installed           five capture units from d63d0b7 sources (Xvfb with
                          ReadWritePaths=/tmp; bridge/runner with --state-dir
                          before the subcommand), xvfb/bridge/runner enabled
Xvfb                      active and stable (lock fallback holds)
bridge                    active on 127.0.0.1:8765
runner                    active, client_connected, but no Chromium process;
                          readiness browser_unavailable (E_BROWSER_UNAVAILABLE)
journal service state     needs_admin / E_AMBIGUOUS_SEND, zero jobs
view units                installed, not enabled, inactive
account                    kronika-capture (uid 996), paths 0700/0750/0700,
                          root credential and capture state token both 0600,
                          never read
NUC tooling               Ubuntu 24.04.4, systemd 255, node v22.23.2,
                          /usr/bin/chromium -> Chrome for Testing 154.0.8037.57,
                          Xvfb/x11vnc 0.9.16/websockify/xauth/mcookie present,
                          AppArmor userns profile present, userns knob 1
```

## 3. What this whole is

One Kronika built on the existing FrameNest product. FrameNest's application,
catalog, media, permissions and deployment are the base; the closed
`cli_chatgpt`/Kronika code supplies the capture module. No new repository.
The locked direction is `01_plan_sk.md`; the accepted implementation plan,
contracts and slice order are `01_report_00.md`. Key locked decisions:
Timeline as the main page; Gallery preserved; Search and Research records;
private-by-default with explicit family sharing; no old-database import;
capture package `kronika_capture`; one persistent browser; admin-handled
login/challenges; one bounded ZIP attachment; S0–S10 order; no mass
`framenest` rename; the NUC is the capture host and stays a dev/test machine.

## 4. What is done and accepted (all published on `cisarik/framenest` main)

```text
S0  93e7742  docs(kronika): record one-product architecture and private records
S1  96ef426  feat(capture): relocate kernel into kronika_capture
S2  5259b89  feat(capture): persist submission barriers and browser lifecycle
    82a6a59  fix(capture): correct queued waits and oversized result delivery
S3  c975aba  feat(capture): supervise capture separately from web deploys
    94e605c  fix(capture): accept the capture CLI state directory and skip the Xvfb lock
    d63d0b7  fix(capture): let the unprivileged Xvfb create its display lock
    e408bb5  fix(capture): diagnose startup and require fresh activation readiness
```

S2 is fully accepted (primary + correction re-acceptance, 03_report_00.md).
S3's repository sources, units, deployment helper and credential boundary are
accepted and published (11_report_00.md, 13_report_00.md, 16_report_00.md).
**S3 is NOT complete**: the host bring-up, the Cooperator login, the explicit
resume, the activation and the synthetic ask remain open.

## 5. The immediate work — S3 host bring-up (accepted playbook)

The accepted recovery plan `15_report_00.md` is the authoritative playbook.
Its conclusions, already reconciled:

- The missing Chromium has no uniquely established cause; the runner
  deliberately hid the startup exception. C1 (published in `e408bb5`) now
  emits bounded safe startup classifications.
- The zero-job `needs_admin` state clears through the designed path: a
  working, logged-in browser, then `bridge resume --intervention-id <current>`
  with no job id, then the runner's matching fresh readiness acknowledgement.
  **No journal reset, no SQL surgery, no state-directory recreation.**
- C2 (published) requires a fresh runner and browser-session identity before
  activation accepts `ready`; old persisted readiness is treated as starting.
- C3 (runner `TMPDIR=/run/kronika-capture/tmp`) is **conditional**: apply only
  if the bounded host diagnostic establishes temporary-storage failure. A
  sandbox denial, profile-in-use or unclassified failure does not select C3.

Sequence (from the plan §5–§6; every later grant must bind the literal SHA):

1. Deploy the published `e408bb5` through the canonical helper (`status`,
   `check --release`, `deploy --release … --yes`) so the corrected runner/
   driver assets are on the host. The helper itself runs from the dev host and
   needs no deployment. Stop on any gate failure.
2. **D1** (Worker through the gate, read-only state inspection per the plan).
3. **D2** (Cooperator-executed NUC block: stop only the runner; inspect the
   external brake metadata `/var/lib/kronika-capture/profile.capture-launch/`
   exactly as the plan specifies; remove an empty orphaned `lock` directory
   only with explicit authority and after confirming zero capture browser
   processes; never delete the launch-state directory).
4. **D3** (Cooperator-executed NUC block: one temporary `ExecStart` override
   pointing the runner directly at `/opt/framenest/releases/<S3_RELEASE>` and
   exactly one instrumented browser start, observed for at most 180 seconds,
   with the plan's classification table; cleanup per the plan). This is the
   single diagnostic browser spawn; no second diagnostic launch.
5. **H1–H6** (per the plan): conditional C3 correction if selected, Cooperator
   view + interactive ChatGPT login through the loopback tunnel, explicit
   null-job resume, `activate-capture --release <S3_RELEASE> --yes`,
   verification (one browser, loopback ports, both pointers, fresh readiness),
   and exactly one synthetic ask as the capture user.
6. S3 completion evidence is the plan §7 list: full-fresh acceptance of any
   correction used, publication, exact deployed identity, classified
   successful launch, Cooperator login confirmation, null-job resume and fresh
   `ready`, activation with a new identity, stable one-browser/loopback/
   private-state evidence, one successful synthetic ask, no outstanding host
   mutation.

Adapt the plan's blocks to the standing directive: **omit all `sudo -K`
release steps**; Michal releases privilege manually.

## 6. Remaining slices (from the accepted plan `01_report_00.md`)

- **S4 — Search and Research**: restore both modes, complete-output handling,
  export/sanitization, causal tests, fresh R3 provider/untrusted-content
  review.
- **S5 — One bounded ZIP**: `/v1/attachments`, staging lifecycle, budget
  integration, adversarial archive tests, fresh file-boundary acceptance and
  the bounded synthetic live trials.
- **S6 — Common records and privacy**: `kronika_records`, ownership and
  private/family access across every existing path, migration `0034`, fresh
  R3 authorization/file-boundary review.
- **S7 — Application capture integration**: one bridge client, transactional
  idempotent result save, migration `0035`, request/admin APIs, the
  `framenest.service` capture-token credential drop-in (host-side addition,
  deferred from S3), fresh targeted acceptance.
- **S8 — Timeline and product presentation**: timeline landing, Search/
  Research UI, sharing controls on the existing shell, Gallery regressions.
- **S9 — Integrated acceptance, DB reset and deployment**: fresh integrated
  acceptance of the eight proofs, exact-object stopped-writer DB reset,
  deployment, Cooperator rendered acceptance.
- **S10 — Public repository transition**: rename `cisarik/kronika` →
  `kronika-capture-archive`, then `cisarik/framenest` → `cisarik/kronika`,
  update remotes/deployment sources, verify refs and release, archive the old
  repository. No history rewrite; never publish the `cli_chatgpt` lab/work
  refs. Local directories need not be renamed; a fresh clone to
  `~/Projects/kronika` is a post-S10 local step.

Each slice: one Worker grant per row; exact baseline/allowlist; one commit;
no push without a publication grant; acceptance class per the plan
(E2/E3; full-fresh after runtime/security changes).

## 7. Ledger candidates carried forward

Non-authorizing; do not implement without a grant: the `framenest.service`
capture-token drop-in (S7); the legacy DOM engine asset in the capture package
(activation would need a durable-submission review); dangling journal symlink
classified as absent; `retained_release_paths` not called by deploy/rollback;
VNC `-nopw` with `-localhost` by design; `mcookie` may appear in the Xvfb
argv (not the bridge token); the deployment doc does not name `-nolock` (moot
after the fallback); FrameNest-era quirks noted in earlier acceptance reports.

## 8. Trace, delivery and grammar

- Trace directory: `/home/agile/meta/projects/kronika/00/02-kronika-one-product/`.
- Worker prompt/report pairs: `<session>_<phase>_<index>.md` and
  `<session>_report_<index>.md`; `index = exchange ordinal − 1`; a new session
  starts at `_00`. Handouts/closures share their own sequence: this is
  `01_handout.md`; the next closure is `02_closure.md`.
- Each grant is a complete new authority: identity/route, exact baseline and
  allowlist, positive and negative authority, declared execution route
  (`./.ap/ap project check` / `./.ap/ap exec`, `node --test`), staging and
  commit rules, stop conditions, report contract, trace/delivery record.
- Reports are delivered session-only or saved to the trace; the Cooperator
  dispatches prompts in fresh Agent chats. Session 15 is context-full — never
  send it another prompt; all new grants use fresh sessions.
- Do not commit Meta artifacts; archival and publication are Cooperator-owned.

## 9. STOP rules

- Do not implement product code yourself; issue Workers.
- Do not push, force, delete or move any ref without a new explicit Cooperator
  publication grant naming the exact refspec; never push the lab/work refs.
- Do not have Workers run `sudo -v` or `sudo -K`; Michal releases manually.
- Do not read `private/**`, browser profiles, cookies, tokens or credentials.
- Do not reset, delete or rewrite the capture journal to bypass recovery.
- Do not weaken the loopback/token/Host/Origin boundaries or the sandbox.
- Do not disturb the running web service beyond the planned release steps.
- Do not upgrade AP; the pinned gitlink governs.
- Do not reopen the closed whole `kronika-public-identity-and-clean-start`.

## 10. Paste seed for the successor Orchestrator chat

```text
Resume the AP-integrated Kronika project as a fresh Orchestrator for the
ongoing whole kronika-one-product (one Kronika on the FrameNest base).
Read /home/agile/meta/projects/kronika/00/02-kronika-one-product/01_handout.md
completely, then the whole's 00_notes.md and the accepted plan 01_report_00.md
and the accepted recovery plan 15_report_00.md.
Begin read-only. Restore the claimed state, the AP pin, the published refs and
the classified host evidence. Do not mutate. Do not push without a new
Cooperator publication grant. Do not reopen any closed whole.
Then continue the S3 host bring-up per the accepted playbook: deploy the
published e408bb5 through the canonical helper, run the single bounded host
diagnostic (D1 Worker; D2/D3 Cooperator blocks), then Cooperator login,
explicit null-job resume, activation and one synthetic ask.
Communicate with Michal in Slovak. Extra High. No Max. Manual dispatch to fresh
Worker sessions. Workers never run sudo -v or sudo -K.
```

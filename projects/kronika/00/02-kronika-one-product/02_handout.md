# Fresh Orchestrator restoration — `kronika-one-product` (S6 implementation and S4-B–S10)

Artifact relationship: **historical restoration handout**. It transfers
information, not authority. Task authority comes only from the current
authoritative Orchestrator routing and the complete Worker prompts issued from
it.

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Capability profile: Orchestrator (terminal-capable repository and operations coordinator)
Logical whole identity: kronika-one-product
Current phase: S6 implementation planned and issuable, then S4-B–S10
Cooperator: Michal
Delivery route: manual Cooperator delivery to fresh Worker sessions
Reasoning recommendation: Extra High for the S6 issuance review; the S6 implementation grant itself is High unless Michal selects otherwise
Internal delegation: one accountable active Worker; never spawn
Product checkout: /home/agile/Projects/framenest
Archive checkout: /home/agile/Tools/cli_chatgpt (read-only source)
Trace: /home/agile/meta/projects/kronika/00/02-kronika-one-product/
AP pin (verify, do not upgrade): 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Handout sequence: this is 02_handout.md (predecessor 01_handout.md)
```

This handout restores a fresh Orchestrator for the **ongoing** whole
`kronika-one-product`. It does not close or reopen any whole. It supersedes
earlier narrative; the whole remains open until its own closure decision.
Restoration grants no mutation authority.

## 0. Communication and binding directives

- Communicate with Michal in Slovak, masculine address, feminine self-reference.
  Worker prompts and formal reports are English.
- Presentation: short status block, one status mark, one dispatch instruction,
  plus the visible delivery capsule (Recipient, Reasoning, Client/Native Plan
  Mode, Prompt path + SHA-256, Report path, Archival).
- **Sudo is Cooperator-owned: Workers never run `sudo -v` or `sudo -K`.**
  Michal establishes the NUC sudo timestamp before dispatch and releases it
  manually afterwards; every grant omits any privilege-release step. Workers
  use `sudo -n` only and never handle a password.
- NUC SSH transport: the three `FRAMENEST_NUC_SSH_*` names are exported in
  `~/.zshenv`. Never print or store their values, hostnames, private network
  values, sockets, tokens or credential material.
- Worker SSH to the NUC goes only through
  `scripts/operator/network/framenest_nuc_worker_gate.fish`; the gate rejects
  shell metacharacters and multiline commands. Complex shell blocks and
  interactive steps are Cooperator-executed (`# [NUC / bash]` blocks).
- `private/**` in the FrameNest checkout is never read. Browser profiles,
  cookies, tokens and credential stores are never inspected.
- One accountable Worker at a time; no subagents. Manual dispatch by Michal in
  a fresh Agent chat per grant. Terse `ok`/`ano`/`pokracuj` means "continue the
  current slice", never a new whole.
- Only the Orchestrator closes the whole; the closure signal is
  `LOGICKY CELOK UZAVRETY`. Workers never emit it.
- The NUC is a development/test machine; data loss is acceptable. Do not treat
  it as production hardening.
- The capture host remains parked. Do not restart the browser, attempt the
  ChatGPT login, remove the recovery override or touch the capture state
  without a new explicit Cooperator decision and bounded grant.

## 1. First thirty minutes

1. Read `/home/agile/Projects/framenest/AGENTS.md` (updated for ADR-0083:
   administrator read-all of application content, administrator-curated
   household publication, modular research provider, capture parked).
2. Read the pinned AP: `.ap/AP.md` (ORCHESTRATOR spine, Plan-to-Execution,
   Implementation Authority, Acceptance/Correction, RF-01–RF-19),
   `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`,
   `.ap/ARTIFACT_LIFECYCLE.md`, `/home/agile/meta/README.md`.
3. Read this handout completely.
4. Read the trace in order of importance:
   - `00_notes.md` (complete; authoritative Orchestrator log),
   - `01_plan_sk.md` (original locked direction; superseded in part),
   - `01_report_00.md` (original accepted plan; S4 route superseded),
   - `15_report_00.md` (accepted S3 recovery playbook; capture parked),
   - `25_report_00.md` (accepted modular-provider plan; §5 records/access/
     approval, §7 revised sequence),
   - `31_report_00.md` (S6 base design and candidate sets N/P/T/H),
   - `32_report_00.md` (frozen S6 targeted-revision plan, Slovak artifact),
   - `33_report_00.md` (**the conformant English S6 plan**: closed G1–G3,
     verified 176-path merged allowlist, 96-test focused list, mandatory
     scenarios, E3/R3 route, recommended implementation grant),
   - `26_report_00.md`/`27_report_00.md`/`28_report_00.md`/`29_report_00.md`/
     `30_report_00.md` (S4-D/S4-A chain acceptances and publication),
   - `ADR-0083` in the product checkout.
5. Re-measure §2 read-only. If anything does not hold, stop and tell Michal in
   one block before any grant.

## 2. Claimed state to re-verify (read-only)

Product checkout `/home/agile/Projects/framenest`:

```text
branch                    feat/kronika-one-product
HEAD                      40e51cb2d061ead96850c9c94aa59de54d5e1310
parent                    75e9b07b2bf2269568382e28d40a8d2ff8d4bc28
tree                      ec3c6c9db49ede4bfcd3616263b388bb26451834
subject                   fix(kronika): preserve research configuration in AI CLI writers
local main = origin/main  40e51cb2…
worktree                  clean
AP pin (gitlink + .ap HEAD) 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
public main (cisarik/framenest) 40e51cb2… (verify with git ls-remote)
other public heads        feat/chatgpt-page-ask-kernel 26d28b16,
                          feat/x-meme-browser-companion 7ff6546f
migration head            0033 (0034 free)
ADR-0083                  present and accepted
```

Archive checkout `/home/agile/Tools/cli_chatgpt` (read-only source of the
capture port): `main` = `66c40d43c577276b0ad304a494fbbb1ffb6fc933`, clean, AP
pin same; public `cisarik/kronika` main = `66c40d43`.

Parked capture host (NUC; last classified state 2026-09-26, re-verify only
read-only and only when a host step is planned):

```text
runner                    active, running from the fd277a9 release tree under
                          the temporary override
                          /run/systemd/system/kronika-capture-runner.service.d/90-s3-recovery.conf
browser                   one root Chromium, readiness needs_admin
                          (E_COMPOSER_NOT_FOUND), zero jobs, no login
xvfb / bridge             active; port 8765 loopback-only
web / capture pointers    fd277a9 / 94e605c
view units                inactive, ports 5900/6080 closed
external brake            lock absent, last-start.json valid
S3 completion             NOT achieved: Cooperator login blocked by a
                          repeating Cloudflare challenge; Cooperator chose to
                          park at the login boundary (2026-09-26)
```

Do not resume the capture login or perform host mutations without a new
Cooperator decision and bounded grant.

## 3. What this whole is

One Kronika built on the existing FrameNest product. FrameNest supplies the
application, catalog, media, permissions and deployment. Current accepted
direction (ADR-0083):

- MEME and Movie stay; Search and Research are added through a **modular,
  provider-neutral application boundary**. The first provider is the OpenAI
  Responses API with fixed model `gpt-5.5-2026-04-23`, native provider-managed
  research, no automatic fallback, disabled by default, server-side
  credentials only.
- **Administrator read-all** of application content (explicit Cooperator
  decision; supersedes the earlier denial), private-by-default records, and an
  **administrator-curated household Timeline** (owners do not publish
  directly; household-only; internet publication disabled).
- Personal question/answer history is separate from the shared Timeline.
- chatgpt.com capture remains one **parked** module (`kronika_capture`,
  command `kronika-capture`, loopback bridge).
- Budgets: Search USD 0.50, Research USD 5, daily USD 10, monthly USD 30; a
  provider monthly hard limit of USD 30; delayed enforcement accepted.
  Standard OpenAI retention accepted; ZDR not required.
- The end goal remains transforming FrameNest into public Kronika (S10).

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
    fd277a9  fix(capture): point the capture runner temporary directory at its runtime dir (C3)
S4-D 72009c3  docs(kronika): define modular research and administrator-curated timeline
S4-A 75e9b07  feat(kronika): add provider-neutral research contracts and configuration
     40e51cb2 fix(kronika): preserve research configuration in AI CLI writers
```

Acceptances: S2 (02/03 reports), S3 repository (08/11/13/16), C3 (22), S4-D
(Orchestrator E1 review), S4-A (29). Publications: 09/12/14/17/23/30. The
capture host bring-up (S3 remainder) is parked, not complete: Cooperator
login, explicit null-job resume, activation and one synthetic ask remain
outstanding.

## 5. Immediate work — issue the S6 implementation grant

The S6 plan is complete, verified and issuable. Artifacts:
`31_report_00.md` (base design, sets N/P/T/H), `32_report_00.md` (frozen
targeted-revision plan), `33_report_00.md` (conformant English plan with the
closed G1–G3 mappings and the **verified 176-path merged allowlist**).

Issue one fresh implementation grant:

- Logical whole: `kronika-one-product`; next genuinely fresh Worker session:
  **34** (sessions 01–33 are used; session 15 must never be reused).
- Worker session target `fresh-worker-session`; profile Fresh Implementation
  Worker; `Native planning mode: not-used`; phase implementation; manual
  Cooperator delivery; reasoning High; independence no.
- Baseline `40e51cb2d061ead96850c9c94aa59de54d5e1310`; branch
  `feat/kronika-one-product`; clean; AP pin `7478ddb0…`; revision `0034`
  must still be free.
- **Exact allowlist: reproduce the complete 176-path union from
  `33_report_00.md` §6** (N 16 new, P 26 existing, T 18 existing, H 21
  existing, targeted-revision additions 95; 153 existing + 23 new), with no
  wildcard expansion. Exclusions stay as the plan states (no `.ap`,
  dependencies, old migrations, 0035, S4-A files, real ingestion cutover,
  UI, deployment, private trace).
- Outcome and boundaries: the closed G1/G2/G3 mappings and behavior in
  `33_report_00.md` §2–§5 (common records and immutable Q/A documents;
  centralized fail-closed owner/admin/household authorization; three
  approved-projection tables and typed read scope; approval/withdrawal with
  version and digest conflicts; private catalog helper; executable access
  inventory).
- Focused validation: the exact 96 `test_*.py` files enumerated in
  `33_report_00.md` §6/§7, first the new/affected set, then the broad suite
  once via `./.ap/ap exec … --operation test-focus -- tests/unit tests/contract
  tests/integration -q -p no:cacheprovider`, all on the declared AP route with
  the exact baseline. No ambient Python.
- Staging: one local commit with subject
  `feat(kronika): add private records and administrator approval`; no push.
- Required evidence: the mandatory scenarios, executable inventory,
  transaction/recovery receipts and private-state containment from
  `33_report_00.md` §7.
- Stops: baseline/branch/pin/cleanliness drift; `0034` collision; required
  out-of-list edit; permission/route failure; unexplained failed gate;
  forbidden data/network/host requirement; unverifiable identity, projection
  or transaction invariant.

After a PASS report: issue a **separate fresh independent E3/R3 authorization
review** of the exact candidate SHA (direct APIs, horizontal/vertical access,
identity forgery, admin actions, inventory completeness, SQL/list leaks,
approved projections, public exclusion, migration/recovery; synthetic
evidence only). Corrections are separate bounded grants with fresh
re-audit. Publication is a separate Cooperator publication grant.

## 6. Remaining slices (revised accepted order)

```text
S6  -> S4-B -> S7-P -> S8 -> S9 -> S10
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
- **S10** public repository transition: rename `cisarik/kronika` →
  `kronika-capture-archive`, then `cisarik/framenest` → `cisarik/kronika`.
- **Parked independently**: remaining S3 host completion (Cooperator login,
  null-job resume, activation, one synthetic ask), capture-mode Search/
  Research, S5 ZIP activation, S7-C capture application integration.

Each active row: one implementation grant; independent acceptance,
publication and host operations are separate grants. The plan and its
mandatory scenarios live in `33_report_00.md` (and `25_report_00.md` §5/§7).

## 7. Ledger candidates carried forward

Non-authorizing; do not implement without a grant:

- `kronika-capture-vnc.service` exits with status 2 on a normal SIGTERM stop,
  which systemd records as failure; a future view-unit contract could declare
  a success exit status.
- Installed `/etc/kronika-capture/capture.env` was checked (no `TMPDIR`
  assignment); re-check read-only if the unit or env file changes.
- Non-capture NUC listeners on 53809/50216 were never identified (outside
  the capture boundary).
- `retained_release_paths` is not called by deploy/rollback.
- The legacy DOM engine asset in the capture package; activation needs a
  durable-submission review.
- A dangling journal symlink classifies as absent.
- VNC `-nopw` with `-localhost` is by design; `mcookie` may appear in the
  Xvfb argv (not the bridge token).
- The `framenest.service` capture-token drop-in remains a host-side addition
  for S7-C, deferred from S3.
- S4-A acceptance residual: a version 1/2 AI config file that already
  contains a `research` key is ignored on read and omitted on save (only
  malformed legacy files); the S4-A commit body carries a
  `Co-authored-by: Cursor` trailer (cosmetic).
- The S6 plan's open items were closed by `32`/`33`; anything the S6
  implementation discovers outside the 176-path allowlist is a stop-and-report
  finding, not an expansion.

## 8. Trace, delivery and grammar

- Trace directory: `/home/agile/meta/projects/kronika/00/02-kronika-one-product/`.
- Worker prompt/report pairs: `<session>_<phase>_<index>.md` and
  `<session>_report_<index>.md`; `index = exchange ordinal − 1`; a new session
  starts at `_00`. Handouts/closures share their own sequence: the
  predecessor is `01_handout.md`; this is `02_handout.md`; the closure would
  be `03_closure.md`.
- Sessions 01–33 are used. Next fresh Worker session: **34**. Session 15 is
  context-full and must never receive another prompt. All new grants use
  fresh sessions.
- Each grant is a complete new authority: identity/route, exact baseline and
  allowlist, positive and negative authority, declared execution route
  (`./.ap/ap project check` / `./.ap/ap exec`, `node --test`), staging and
  commit rules, stop conditions, report contract, trace/delivery record.
- Reports are delivered session-only or saved to the trace; the Cooperator
  dispatches prompts in fresh Agent chats and owns Meta Git archival.
- Recent reports were sometimes delivered in chat and persisted to the trace
  by the Cooperator (sessions 15, 19, 25, 33). Note any such deviation in
  notes; a client Plan-mode write restriction is a delivery deviation, not a
  plan defect.

## 9. STOP rules

- Do not implement product code yourself; issue Workers.
- Do not push, force, delete or move any ref without a new explicit Cooperator
  publication grant naming the exact refspec; never push the lab/work refs.
- Do not have Workers run `sudo -v` or `sudo -K`; Michal releases manually.
- Do not read `private/**`, browser profiles, cookies, tokens or credentials.
- Do not resume the parked capture host (browser restart, login attempt,
  override removal, resume, activation, synthetic ask) without a new explicit
  Cooperator decision and bounded grant.
- Do not select or apply the S6 corrections outside the verified 176-path
  allowlist; a required out-of-list edit is a stop.
- Do not reset, delete or rewrite the capture journal to bypass recovery.
- Do not weaken the loopback/token/Host/Origin boundaries or the sandbox.
- Do not disturb the running web service beyond planned release steps.
- Do not upgrade AP; the pinned gitlink governs.
- Do not reopen the closed whole `kronika-public-identity-and-clean-start`.

## 10. Paste seed for the successor Orchestrator chat

```text
Resume the AP-integrated Kronika project as a fresh Orchestrator for the
ongoing whole kronika-one-product (one Kronika on the FrameNest base; modular
research provider; capture parked).
Read /home/agile/meta/projects/kronika/00/02-kronika-one-product/02_handout.md
completely, then the whole's 00_notes.md, the accepted modular-provider plan
25_report_00.md, and the S6 plan 31_report_00.md + 33_report_00.md.
Begin read-only. Restore the claimed state, the AP pin, the published refs and
the parked capture state. Do not mutate. Do not push without a new Cooperator
publication grant. Do not reopen any closed whole. Do not resume the capture
host login without a new Cooperator decision.
Then issue the S6 implementation grant: fresh Worker session 34, Fresh
Implementation Worker, Native planning mode not-used, manual Cooperator
delivery, High, baseline 40e51cb2d061ead96850c9c94aa59de54d5e1310, with the
complete 176-path allowlist from 33_report_00.md §6 and the 96-test focused
list from §7, one local commit, no push; then a separate fresh E3/R3
authorization acceptance.
Communicate with Michal in Slovak. Extra High for the S6 issuance review.
Manual dispatch to fresh Worker sessions. Workers never run sudo -v or
sudo -K.
```

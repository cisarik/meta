# Fresh Agent Orchestrator Handoff

## FrameNest × X Companion — Live NUC Attach, Then Practical Polish

This is the complete handoff for a fresh, terminal-capable Agent Orchestrator.
It supersedes `00_handout.md` in this same directory. Load **this file only**.
It is not a Worker prompt, not a repository plan, not a mutation receipt, and
not a substitute for the pinned Analytic Programming protocol.

The predecessor Orchestrator session ended by Cooperator instruction on
2026-08-17 after Workers 01–05 of this whole reported implementation-PASS,
after public `main` was fast-forwarded to the candidate, and after NUC
`framenest-release check` passed. **NUC was not cut over.** Gallery 📎 is
still invisible on the live origin because that origin still serves
`bfad16b` (Alembic **0028**). Routine `deploy --yes` of `045f33b` would
stop `migration-required` after packaging and can leave
`/run/framenest-release-deploy`. Do not run it yet.

Michal selected Extra High. He wants FrameNest **usable in practice**: test
the Brave companion against live NUC, then polish UI/UX with you. He does
not want another infinite redesign. Green side-panel chrome is accepted as
much better than the first grey-black picker clone.

If a later explicit Michal message contradicts this file, the later message
wins. Record the conflict. Do not paper over it.

```text
STOP: Do not run ~/framenest_routine.fish through deploy --yes.
STOP: Do not run deploy/ubuntu/framenest-release deploy --yes for 045f33b
      while NUC database_revision is 0028.
STOP: Do not start a Planner for this sidebar whole. Implementation already
      exists at 045f33b. The remaining work is publication (DONE), schema
      0028→0029, NUC cutover, live 📎, then polish.
STOP: Do not close this logical whole until Michal has seen 📎 on live NUC
      Gallery in the side panel, or he explicitly accepts that residual.
```

---

## 0. Handoff identity

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Orchestrator profile: terminal-capable repository and operations coordinator
Orchestrator handoff artifact: 00_handout_01.md
Predecessor Orchestrator artifacts:
  03/03-framenest-x-meme-browser-companion-mvp/00_handout.md
  03/03-framenest-x-meme-browser-companion-mvp/00_handout_01.md
  03/05-framenest-x-companion-sidebar-web-mvp/00_handout.md
Logical whole identity: framenest-x-companion-sidebar-web-mvp
Current phase: restoration then schema-aware NUC cutover then live Attach
Native planning mode: not-used
Reasoning recommendation: extra-high
Internal delegation posture: one accountable active Worker by default;
  Cooperator may again tell you to execute operations yourself without a Worker
Cooperator: Michal
Primary consumer repository: cisarik/framenest
Pinned protocol repository: cisarik/ap through the FrameNest .ap gitlink
External analytic trace: cisarik/meta
Parent logical wholes (not closed):
  framenest-x-meme-browser-companion-mvp
  framenest-x-companion-save-alias-mvp
This whole: not-closed
```

Extra High is selected because Michal explicitly chose it. Do not silently
downgrade. Do not use Max unless he later selects it.

Native Plan Mode is disabled for **this** Agent Orchestrator. Do not issue a
Planner. Workers 01–05 of this whole already landed. The next bounded Worker,
if any, is an **operations** Worker (migrate / leftover-lock recovery /
cutover) or a later **visual correction** Worker after Michal attaches a
live defect.

Do not ask Michal to select this logical whole again. He already selected
it. Do not ask him to re-tell the 2026-08-17 brainstorming. It is classified
below: current whole vs frozen parents vs backlog vs live NUC blocker.

Do not load, rename, or execute:

```text
/home/agile/meta/projects/framenest/03/03-framenest-x-meme-browser-companion-mvp/00_handout.md
/home/agile/meta/projects/framenest/03/03-framenest-x-meme-browser-companion-mvp/00_handout_01.md
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp/00_handout.md
```

The file `00_handout.md` in this directory is historical seed for the
Planner era. `00_handout_01.md` (this file) is current authority for the
fresh Orchestrator.

Do not write a second Orchestrator handoff under
`03/04-framenest-x-companion-save-alias-mvp/`. That directory is the
Save/alias Worker trace. There is no pointer file. Do not continue
Save-alias Worker ordinals 05+.

---

## 1. Mission

Restore exact local, public, AP, Meta, and NUC state. Then get **📎 live on
NUC Gallery inside the companion side panel** without improvising a second
deploy engine and without hiding Alembic `0029`. After Michal sees 📎,
stay with him for practical polish. Do not start a new product architecture.

Your job is:

1. restore against repository, public refs, and NUC `framenest-release
   status`, not this handoff alone;
2. keep the three surfaces distinct (Section 11);
3. treat publication of `045f33b` as **already done** unless public `main`
   has moved;
4. refuse routine `deploy --yes` while NUC `database_revision` is `0028`;
5. present one honest cutover recommendation (Section 16) plus the real
   alternative; wait for an explicit migrate + cutover grant;
6. after cutover, have Michal Reload unpacked, Connect in Settings, open a
   bound X tab, and look for 📎 top-left on hosted Gallery cards;
7. then polish UI/UX with him in small bounded corrections — he said this
   can go on forever and he wants FrameNest usable in practice, not a
   redesign;
8. carry Section 14 backlog so later Orchestrators do not lose aliases-in-
   Gallery, language, Analyze-after-catalog, NUC companion origins, or R3;
9. keep Michal in the loop at irreversible schema, leftover-lock recovery,
   cutover, live 📎, and closure.

Do not close either parent whole. Do not start an AP upgrade. Do not enable
NUC `FRAMENEST_COMPANION_EXTENSION_ORIGINS` or `x_acquisition_root` unless
a later prompt grants that exact host configuration. Empty allowlist still
fail-closes the two X POSTs; that does **not** block Gallery 📎 of already
cataloged library items.

---

## 2. Why this whole is not closed

Implementation PASS ≠ publication PASS ≠ deployment PASS ≠ production
acceptance ≠ ORCHESTRATOR closure.

| Gate | State at handoff issuance (2026-08-17 evening) |
|---|---|
| Planner 01 | PASS; Michal `Prijimam` |
| Workers 02–05 | implementation-PASS on `feat/x-meme-browser-companion` |
| Independent INFOSEC R3 | never issued (sidebar bridge + overlay + Save) |
| Publication | **DONE** this predecessor session: public `main` = `045f33b44897a6f3949cc515792336396f1d33a1` (non-force fast-forward from `bfad16b`) |
| `framenest-release check` | **PASS** for that SHA; backup_restore_readiness `ready` |
| NUC cutover | **NOT done.** Live `active_release` still `bfad16b`. `database_revision` still `0028`. Service `active`. |
| Live 📎 | **NOT visible.** Iframe shows Gallery from old web without `companion_host.js`. Honest shell copy already explains that. |
| Closure | **not-closed** |

Michal asked the predecessor to finish the whole with deploy using
`~/framenest_routine.fish` and not to create a Worker. The predecessor
published and checked, then **stopped before `deploy --yes`** because that
command is same-schema only. Packaged head of `045f33b` is Alembic **0029**.
Live DB is **0028**. The helper never runs `framenest-db migrate`. A
knowing `deploy --yes` would package `/opt/framenest/releases/045f33b…`,
then raise `migration-required`, and leave `/run/framenest-release-deploy`
(cleanup runs only on success). That leftover lock historically required a
bounded recovery Worker. Do not repeat that by accident.

---

## 3. Role model

### 3.1 COOPERATOR

Michal is the COOPERATOR and strategic owner.

He owns feature intent, visible UX acceptance, signed-in Brave/X actions,
credentials, irreversible operations (schema migrate, leftover-lock
deletion, NUC cutover), material privacy trade-offs, model choice, and any
explicit scope reduction.

He tests the unpacked companion visually after Reload in
`brave://extensions`. Do not demand a whole-product PASS/FAIL checklist.
He is glad to brainstorm. Present one honest recommendation plus real
alternatives at material forks. Do not turn brainstorming into a
questionnaire. Do not wait for him to invent filenames or SHAs.

He said UI/UX can be polished forever. Green OS-like chrome is **accepted**.
Do not reopen a grey-black clone. Do not start a visual redesign because
you notice remaining imperfections. Wait for his attached observation.

### 3.2 Agent Orchestrator

Terminal access is capability, not unlimited authority. You may restore
read-only, write exact Worker prompts and Orchestrator trace artifacts,
review reports as claims, and — when he again says so — execute bounded
Git/NUC operations yourself without a Worker.

You do not implement extension, FrameNest web, Alembic, or NUC config by
default. You do not paste giant Worker prompts into chat when the Meta file
exists. You do not close this whole until Section 2 gates that he still
cares about are actually satisfied.

### 3.3 WORKER

One accountable Worker at a time. Default for leftover-lock recovery and
schema migrate is a **fresh operations Worker** with exact paths, because
that privileged deletion class already burned this project once. If Michal
explicitly says no Worker and asks you to do it, record that grant, keep
the same exact-path discipline, and do not improvise `rm` wildcards.

`Approve`, `Yes`, `Build`, `Continue`, or this file do not grant
implementation or deploy authority.

---

## 4. Communication and Cooperator presentation

Communicate with Michal in Slovak. Address him with masculine grammar. Use
feminine grammar for your own Slovak self-reference.

Repository documentation, code comments, Worker prompts, Worker reports, and
this class of handoff are professional English. Do not use Czech.

Every complete downloadable Worker prompt must be a real Markdown file. After
the file exists, display a concise Slovak routing capsule outside the prompt.

Use these signals:

- 🆕 — fresh Worker or fresh Orchestrator session
- ♻️ — exact current Worker session
- 💡 — Native Plan Mode must be enabled; show only when the routed mode is on
- 🧠 — Medium
- 🧠🧠 — High
- 🧠🧠🧠 — Extra High
- 🧠🧠🧠🧠 — Max only after explicit Cooperator selection
- ✅ — accepted state or completed gate
- ⚠️ — material risk, conflict, or Cooperator decision
- 🧊 — explicitly parked scope
- ▶️ — exact next action
- 📦 — exact prompt/report/archive file

When Native Plan Mode is off, omit 💡 and state that Native Plan Mode must be
disabled.

Human-facing command blocks for Michal's MacBook / CachyOS workstation use
Fish-compatible syntax and begin with:

```text
# [MacBook / fish]
```

Human-facing command blocks for an already-open NUC session use Bash and
begin with:

```text
# [NUC / bash]
```

Every such block ends with:

```text
#------------------------------------------------------
```

Do not mix workstation and NUC commands in one unlabeled block. Do not
print `SSH_AUTH_SOCK`, identity paths, Tailscale hostnames, or sudo
passwords. Do not reconstruct `gpgconf` in Worker reports.

---

## 5. Durable context rule

Model memory, this handoff, prior chat, and Meta traces are recall layers.
Required behavior must live in pinned AP, FrameNest `AGENTS.md`, repository
documents, ADRs, code, tests, and exact Meta prompt/report pairs.

RF-19 precedence:

1. governing AP pin;
2. canonical repository and current external truth;
3. accepted durable decisions;
4. optional trace;
5. tentative narrative, including this handoff.

---

## 6. Workspace and expected topology

```text
/home/agile/Projects/framenest
/home/agile/Projects/ap
/home/agile/meta
```

Discover actual paths. Canonical FrameNest checkout is preferred. Do not
create extra worktrees as ritual.

Interactive shell is fish. Cursor Workers must not invoke raw
`.venv/bin/python`, `python`, `python3`, or `poetry run` for Python evidence.
Python and tests go through:

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT>
./.ap/ap exec --root /home/agile/Projects/framenest --baseline <EXACT_AUTHORIZED_COMMIT> --operation <DECLARED_OPERATION> [-- <TRAILING_ARGUMENTS>]
```

JavaScript tests use `node --test`. Do not invent npm or a bundler.

NUC SSH goes through
`scripts/operator/network/framenest_nuc_worker_gate.fish` (`--probe` first).
BatchMode SSH only. Never reconstruct `gpgconf` or print agent sockets.
Remote sudo lifecycle is Cooperator timestamp (`sudo -v`, then `sudo -n true`)
outside the Worker, plus Worker terminal `sudo -K`. Workers must not run
`sudo -v` or handle a password. Password-required after predecessor `sudo -K`
is expected lifecycle state, not a broken NUC.

Routine NUC release entry point remains `deploy/ubuntu/framenest-release`.
Do not improvise deployment commands. Do not invoke `uv` for routine
updates.

Poetry / CPython on NUC for routine updates:

```text
Poetry: /opt/framenest/tooling/poetry/2.4.1/.venv/bin/poetry
CPython: /opt/framenest/tooling/python/cpython-3.13.14-linux-x86_64-gnu/bin/python3.13
```

Michal's workstation helper (not AP, not a second NUC engine, not a Worker):

```text
~/framenest_routine.fish
```

It wraps `./.ap/ap update --check|--apply`, `./.ap/ap doctor --candidate`,
and `framenest-release status|check|deploy`. It deploys **public `main`**
only, requires local HEAD == public main, tracked-clean tree, and already-
valid remote `sudo -n`. It never migrates. Catalog checkpoint is already
inside routine `deploy --yes`. AP apply requires a fully clean worktree
including untracked. **Do not use it to paper over 0028→0029.**

---

## 7. Mandatory fresh bootstrap

Begin read-only. This Orchestrator has no inherited Worker authority.

### 7.1 Required reading

1. FrameNest root `AGENTS.md`
2. pinned `.ap/AP.md`
3. pinned `.ap/AP_ORCHESTRATOR.md`
4. pinned `.ap/PROMPT_CONTRACTS.md`
5. task-relevant `.ap/AP_WORKER.md`
6. `docs/WORKER_EXECUTION_CONTRACT.md`
7. only the AP upgrade ledger declared by root `AGENTS.md`
   (`docs/AP_UPGRADE_OBSERVATIONS.md`) — park it; do not activate it
8. `docs/UBUNTU_NUC_DEPLOYMENT.md` (same-schema boundary + Section 5 Migrate)
9. ADR-0060, ADR-0061, ADR-0062, ADR-0063
10. `docs/X_COMPANION.md`
11. `docs/adr/0048-tailscale-remote-access-and-identity-foundation.md`
12. `extension/manifest.json`, `extension/ui/sidebar.html|js|css`,
    `extension/ui/picker.html|js|css`, `extension/ui/save.html|js|css`
13. `src/framenest/adapters/api/web/companion_host.js` and Gallery card
    overlay in `app.js`
14. this file, then this directory's Worker prompt/report pairs as
    historical evidence (Section 8)

Do not discover ledgers by filename guessing.

### 7.2 Read-only repository gate

For FrameNest, AP, and Meta record separately: root, origin URL, branch,
HEAD, status including untracked, upstream relation without fetch, public
main via credential-free `git ls-remote` (no fetch on the initial gate),
`.ap` gitlink and checkout, overlapping mutations.

Do not `git fetch` during the initial gate. Do not switch branches, stash,
reset, merge, rebase, clean, or update submodules.

Classify: FrameNest local, FrameNest public, pinned AP, AP public, Meta
local/public, NUC/production, browser/account, active mutation.

NUC: `framenest-release status` is in scope for this session's restore
because cutover is the remaining product gate. Probe the SSH gate first.
Do not deploy during restore.

### 7.3 Bootstrap outcomes

If identities match Section 9 **or honestly supersede it**, the feature-
branch working tree is clean, `save.html` still matches Section 11.1, public
`main` is still `045f33b` (or a later fast-forward you can explain), and
NUC is still `bfad16b` / `0028`, continue automatically to Section 16.
Summarize restored facts. Ask Michal for the migrate+cutover grant. Do not
ask him to re-approve this whole. Do not write `01_planning_00.md` again.

If public `main` moved past `045f33b`, inspect intervening commits
read-only before any NUC command.

If FrameNest is dirty, identify ownership, preserve the work, and stop only
when overlap makes the next mutation unsafe.

If Meta is dirty because this `00_handout_01.md` is still untracked, that is
expected. Do not mix parent 03/04 archival into a Meta commit unless a later
explicit archival task names those paths.

---

## 8. Meta chains (historical evidence, not authority)

### 8.1 Companion MVP (parent, not closed)

```text
/home/agile/meta/projects/framenest/03/03-framenest-x-meme-browser-companion-mvp
```

Workers 01–05 published/deployed the original companion against public
`main` (then `bfad16b`). Workers 06–12 are unpublished-at-the-time UX that
is now on public `main` via this whole's publication. Do not overwrite
those files. Do not execute that directory's `00_handout*.md`.

### 8.2 Save / alias MVP (parent, not closed)

```text
/home/agile/meta/projects/framenest/03/04-framenest-x-companion-save-alias-mvp
```

```text
01_planning_00.md / 01_report_00.md     Planner; Michal accepted (Slovak “prijať”)
02_implementation_00.md / 02_report_00.md  overlay 0029 + Save iframe
03_correction_00.md / 03_report_00.md   Search tags, header X, no checkbox forest
04_correction_00.md / 04_report_00.md   Description restored; actions flex-end; admin Save and analyze by AI
```

Independent INFOSEC R3 was never issued. Do not create `00_handout.md`
there. Do not continue Worker ordinals 05+.

### 8.3 This whole

```text
/home/agile/meta/projects/framenest/03/05-framenest-x-companion-sidebar-web-mvp
```

```text
00_handout.md            historical seed (Planner-era). Do not execute.
00_handout_01.md         THIS file. Current Orchestrator authority.
01_planning_00.md / 01_planning_01.md / 01_report_00.md
                         Planner Extra High; Native Plan Mode on then report repair
                         Michal: Prijimam
02_implementation_00.md / 02_report_00.md
                         00fcf2c host web + 91283a7 docs; ADR-0063
03_correction_00.md / 03_report_00.md
                         e59d0a4 green chrome, Settings out of picker,
                         handshake honesty, 📎 top-left + keep open-original
04_correction_00.md / 04_report_00.md
                         5b84046 Settings sheet under title bar
05_correction_00.md / 05_report_00.md
                         045f33b Connect button inside Settings;
                         Disconnect opens Settings; empty title-bar Connect
                         opens Settings (no dead-end)
```

Do not re-issue Worker 05. Connect-in-Settings already landed.

Frozen native plan (historical only):

```text
/home/agile/.cursor/plans/sidebar_web_mvp_3b064dd6.plan.md
```

---

## 9. Verified state at handoff issuance

Re-verify. These values were observed 2026-08-17 after publication and
`framenest-release check`. They can go stale.

### 9.1 FrameNest

```text
Canonical checkout: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion (no upstream configured; expected)
HEAD: 045f33b44897a6f3949cc515792336396f1d33a1
Parent: 5b84046a054b35393860c1a2d811f1a0ca9b9959
Tree: 690b90e1ffc2ac5e8ef5f2ae59ccd0543b92b5d4
Subject: fix: put companion Connect in Settings so reconnect works
Working tree: clean
Local main pointer: 3cf22b8aaff61ed71093207d5b24aae622f394ac
  (stale on purpose; do not switch local main)
.ap gitlink / checkout: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Alembic head on this SHA: 0029
```

Public / origin `main` after predecessor publication (non-force FF):

```text
045f33b44897a6f3949cc515792336396f1d33a1
Previously: bfad16b718e135b272a3b0293bb37ddc3101ba49
```

That publication shipped **19 commits** that were local-only on
`feat/x-meme-browser-companion` after `bfad16b` (oldest first):

```text
4a7fd25f26ce4446c48123f34bb3e11694b23e8b fix: place X companion Save beside native Share
14c8a7098e41fa9602c1c45bbf3f2207f6001400 style: apply FrameNest gallery tokens to the X companion
572c6d4e239a65cd4457061d0cdd59c46c1ba2a7 fix: hide origin setup behind companion Settings
9cec59803a0c00d15e6a1fb84a651ec667236508 fix: overlay Save on hover media instead of the Share row
cfbc45dbe8627c3b048cca366964467703dd65e5 fix: open attach picker as an in-page popup above the composer
3e354b0785556235d26943470689a7bd0bddbb9d fix: keep reply Attach after X re-renders the composer
c5904b47914fe376733e50ca8d0f4b9173dadb22 fix: float reply Attach instead of injecting into the X text row
c69af98b675712f6546f4e1f3d51a4db174e8ed8 feat: persist per-user media alias overlay
7bc74b1914b81ecd2c52610a11d8b74130c5d798 feat: accept optional alias on X companion save requests
9ae726fd67581ee50fc4fba684123008c31b154e feat: open FrameNest Save popup instead of silent X save
692db9153778bca2d9fafd5a16e695d2aea49410 docs: record per-user media alias overlay
72b8507fa0c7af627c8c60fe5fbae611bdb759f6 fix: search tags and keep Save visible on the X companion popup
ea939734558d7f5391e8d06c561a5cc46bc07b25 test: retarget live Alembic head pins to 0029
cdb868913a6cee1ef5d801381c38fba58b1b2699 fix: restore Save description and right-align companion actions
00fcf2cf5efc9b2438ecec12c053a2bec3a4bbb9 feat: host FrameNest web in the companion side panel
91283a70fcee039dd20f43bae5bf90e5901f01e8 docs: record companion side-panel web host
e59d0a4243311a31a6e1ffe4e6930243522a656b feat: give the companion side panel an OS-like FrameNest chrome
5b84046a054b35393860c1a2d811f1a0ca9b9959 fix: anchor companion Settings under the side-panel title bar
045f33b44897a6f3949cc515792336396f1d33a1 fix: put companion Connect in Settings so reconnect works
```

`4a7fd25` Share-row Save was later superseded by the media-tile overlay.
Do not restore Share-row placement.

`c5904b4` Attach float is Cooperator-accepted and frozen. Do not inject
Attach back into the X text row (that caused native number-spinner arrows).

`companion_host.js` first appears in `00fcf2c`, which is **after** overlay
`0029` (`c69af98`). There is no same-schema SHA that contains Gallery 📎
hosting. Do not cherry-pick the host onto `0028` to dodge migrate.

Private key (gitignored, never print, never copy into chat):

```text
private/companion-extension.pem.key
```

Stable unpacked extension origin (committed `extension/manifest.json` `key`):

```text
chrome-extension://omiihmnlkmieaafaphohakcgmbggppap
```

Origin grant must match `https://*.ts.net` (`acceptFrameNestOrigin`). Local
`http://127.0.0.1` cannot be the companion origin.

### 9.2 AP

```text
Pinned FrameNest .ap: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public cisarik/ap refs/heads/main at issuance: same SHA
```

Do not mutate AP. Do not treat a local AP branch as authority to change the
pin. `~/framenest_routine.fish` may offer AP apply; skip it unless Michal
opens a separate AP-update whole. Ledger
`docs/AP_UPGRADE_OBSERVATIONS.md` stays parked
(`consumer-declared-execution-and-capability-route-binding`, untriaged).

### 9.3 Meta

```text
Checkout: /home/agile/meta
Branch: main
HEAD at issuance: 325040b79205a9d012f3106191f2ae907ba61692
Subject: fix: implement Settings Connect button for improved user experience
This directory's Worker 01–05 pairs: already committed
This file (00_handout_01.md): expected untracked until archival
```

### 9.4 NUC / production (directly observed this predecessor session)

SSH agent probe: ready. Remote `sudo -n true`: exit 0 at that moment
(timestamp can expire).

```text
framenest-release status
active_release: bfad16b718e135b272a3b0293bb37ddc3101ba49
release_path: /opt/framenest/releases/bfad16b718e135b272a3b0293bb37ddc3101ba49
service_active: active
database_revision: 0028
backup_restore_readiness: ready
```

```text
framenest-release check --release 045f33b44897a6f3949cc515792336396f1d33a1
release: 045f33b44897a6f3949cc515792336396f1d33a1
ap_gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
public_main: 045f33b44897a6f3949cc515792336396f1d33a1
superproject_sha256: 39cf85246453690ba71ba894fb7acbd494021262413c213bd961cdf0cd21612d
ap_archive_sha256: 39d6193a836d797efae3b5e663f3b825f089d54812d5bbcae8929c78e705f7af
current_release: /opt/framenest/releases/bfad16b718e135b272a3b0293bb37ddc3101ba49
backup_restore_readiness: ready
check_exit: 0
```

Check does **not** compare packaged Alembic head with production revision.
That gate is inside `deploy` after staging is renamed to
`/opt/framenest/releases/<SHA>`.

Companion origin allowlist was **not** written. Empty
`FRAMENEST_COMPANION_EXTENSION_ORIGINS` remains fail-closed for the two X
POSTs. Empty `x_acquisition_root` still yields `X_REQUEST_NOT_CONFIGURED`
(503) on `POST /api/x/requests`. Live Save against NUC is still expected to
fail closed after cutover. Attach of already-cataloged library can work
once the origin serves `companion_host.js` and an X tab has bound the SW.

Do not put Tailscale hostnames, IPs, or identity paths in repository
artifacts or reports. Live origin shape is
`https://<node>.<tailnet>.ts.net` with no path.

---

## 10. Session thread (2026-08-17) — do not lose this

This section is why a new Orchestrator exists. It is classified intent, not
a license to implement parked items.

### 10.1 Product destination

Michal’s library life is the **FrameNest website**, not a second companion
UI. Overlay aliases exist so each authenticated user can keep their own
title, tags, and description — including in their native language — without
ordinary users gaining `metadata.canonical.write`. Gallery today still
shows **canonical** metadata. The overlay is stored but not edited from
Gallery. That editor is backlog (Section 14). The side panel hosts the real
site so that later whole can land on the same surface.

He wants FrameNest **usable in practice** now: test the Brave extension
against live NUC, then iterate polish with the Orchestrator. First
impression of the grey-black picker clone in the side panel was bad. Green
OS-like chrome is much better. Polish can continue forever; do not treat
that as a new architecture whole.

### 10.2 What this whole already finished (do not redo)

1. Planner 01 Extra High; Michal **Prijimam**.
2. Worker 02: thin MV3 shell `extension/ui/sidebar.html|js|css` iframes
   stored Tailscale origin; `side_panel.default_path` = sidebar;
   `action.default_popup` removed; `openPanelOnActionClick: true` on
   install and SW startup. Handshake
   `v: "framenest.companion.web.v1"` (`WEB_READY` / `HOST_HELLO` /
   `HOST_ACK` / `ATTACH_REQUEST` / `ATTACH_RESULT`). Pin
   `chrome-extension://omiihmnlkmieaafaphohakcgmbggppap`.
   `ATTACH_REQUEST` = UUID `mediaId`+`locationId` only → existing
   `ATTACH_BEGIN`. Unbound composer → `composer_unbound`, no silent
   `fallbackDownload`. ADR-0063 accepted. Zero new `companion_mutation`.
   No WAR for sidebar. No `externally_connectable`. No `all_urls`. No CORS.
   In-page picker: one JPEG `gallery-preview` via SW `PREVIEW_FETCH`.
3. Worker 03: green OS title bar, black **FrameNest**, gear; Settings
   removed from the in-page picker; honest handshake copy when the framed
   origin lacks `companion_host.js`; Cooperator reversed “replace
   open-original” — hosted cards keep open-original **bottom-right** and
   add **📎 top-left**. Ordinary tabs: no 📎. `boundTabId` only from
   `https://x.com` / `twitter.com` `sender.origin`.
4. Worker 04: Settings sheet **under the title bar**, not a centered modal,
   not a picker hamburger.
5. Worker 05: **Connect button inside Settings**. After Disconnect/`RESET`,
   origin is wiped and Settings auto-opens with origin focus. Empty
   title-bar Connect opens Settings (`Connect FrameNest in Settings`)
   instead of the dead-end `Enter a FrameNest origin in Settings`.
   Connected title bar remains **Disconnect** only.

### 10.3 What Michal already live-accepted

- Reply Attach `+` floats `position: fixed` on `document.documentElement`,
  vertically centered on the focused “Post your reply” field, flush right.
- In-page Search memes popup as quick attach: search, kind filter, one
  JPEG at a time, arrows, Attach. Not a second Gallery.
- Save `+` on eligible GIF / video / image tiles. Click opens Save popup.
- Side panel hosts real Gallery/web (iframe loads even on old NUC).
- Green chrome + Settings under title bar.
- Honest “older web / no companion host” notice while NUC is `bfad16b`.

### 10.4 What Michal rejected or reversed

- Silent Save-from-X on hover `+`.
- Injecting Attach into the X composer text row.
- Canonical tag checkbox forest.
- Cancel as a bottom button (header X instead).
- Dropping Description from Save (Worker 03 removed; Worker 04 restored).
- Side panel as a wider clone of the in-page picker (waste; grey-black
  first impression was bad).
- Replacing Gallery open-original with 📎 (he wanted **both**: 📎
  top-left, open-original bottom-right). ADR-0063 still says “replace”;
  **do not edit ADR-0063 in place**. Live code and Cooperator intent win.
  ADR-0062 Cancel sentence is similarly stale.

### 10.5 Why 📎 is still invisible (do not “fix” with CSS)

Side panel iframes live NUC Tailscale web. That origin still serves
`bfad16b`, which does **not** ship `companion_host.js`. Iframe **loads**
(Gallery visible). Handshake times out. Worker 03 copy (honest, keep it):

> This FrameNest server cannot host companion Attach yet. The library
> below is an older web without the companion host.

📎 appears only after that origin serves this branch’s web
(`companion_host.js` + `app.js` thaw) **and** an X composer tab has bound
the SW. Picker saying `No eligible memes` while Gallery shows “Cardano” is
**expected audience** (picker is meme-only via
`GET /api/x/companion/media`), not a search bug to widen in this whole.

### 10.6 Predecessor operations this evening

Michal: close this whole with deploy; use `~/framenest_routine.fish`; no
new Worker; Orchestrator has sudo timestamp and SSH agent; he wants 📎
ready to start; then continue polish with a fresh Orchestrator.

Predecessor:

1. Confirmed Worker 05 HEAD `045f33b`, clean tree, AP pin matches public AP
   main, public FrameNest main still `bfad16b`, 19 unpublished commits
   including `0029`.
2. NUC status: `bfad16b`, DB `0028`, backup ready, sudo -n valid.
3. Non-force push `045f33b` → `origin refs/heads/main`. Readback matched.
   Local branch left on `feat/x-meme-browser-companion`. Local `main`
   pointer not switched.
4. `framenest-release check --release 045f33b` PASS.
5. **Did not** `deploy --yes`. **Did not** close the whole.
6. Wrote this file.

Independent R3 remains unissued. Cooperator chose live practical test over
waiting for R3. Record that residual; do not self-certify.

---

## 11. Three surfaces (authoritative Cooperator intent)

There are three surfaces. They are not the same product. Do not mix them.

### 11.1 Surface A — Save popup on X media — FROZEN

Trigger: hover/focus green `+` at the bottom-right of an eligible X media
tile.

Frozen contract (verify live files; do not restyle unless a live defect):

- closed-shadow iframe WAR `ui/save.html`;
- black background, FrameNest green border, compact green header
  “Save to FrameNest”, red header **X**;
- Title, Description (`textarea` 10000), Search tags + selected pills;
- no Cancel button; no checkbox tag forest; no category picker; content
  category is fixed X; no provenance field;
- `.actions { justify-content: flex-end }`; Save is the rightmost control;
- ordinary user (`analysis.run` absent or identity fail-closed): only Save;
- admin: **Save and analyze by AI** immediately left of Save; click saves
  via the same `submitSave()` / `SAVE_POST` + alias payload; no analysis
  HTTP; no new `companion_mutation`;
- alias rides existing `POST /api/x/requests`; empty fields omit alias
  keys; SW already sanitizes `alias.description` to 10000;
- failed Save remains a plus glyph with danger border / title, not an ×
  as the primary language;
- iframe about 360×520, fields scroll if needed.

Analyze **execution** after catalog remains backlog. NUC Save remains
fail-closed until companion origins + `x_acquisition_root` (Section 14.5).

### 11.2 Surface B — In-page Attach / Search memes — FROZEN as quick attach

Trigger: focus the reply composer. Frozen float from `c5904b4`. Tooltip
“Attach from FrameNest”.

`ui/picker.html`: Search memes, All kinds, one JPEG `gallery-preview` via
SW `PREVIEW_FETCH`, arrows, Attach. **Settings were removed from this
popup** (Worker 03). Empty-origin status:
`Connect FrameNest in Settings` (Worker 05 copy; only when origin is not
stored). Picker API is meme-only. Do not replace this popup with the full
website. Do not inject Attach into the X text row.

### 11.3 Surface C — Side panel — real FrameNest web + OS-like chrome

Thin MV3 shell hosts the stored Tailscale origin in an iframe after
Connect. Green title bar, black **FrameNest**, gear, Disconnect when
connected. Settings **in the side panel under the title bar**. Origin field
and **Connect** live in Settings. Disconnect clears origin and opens
Settings. Empty title-bar Connect opens Settings. No `default_popup`.
Toolbar `openPanelOnActionClick: true`.

Do not restyle this chrome unless Michal attaches a live defect. Do not
move Settings back into the picker.

---

## 12. Extension-context Attach on Gallery cards

When FrameNest web is companion-hosted (handshake `HOST_HELLO` from the
pinned extension origin, not merely `parent !== window` or `?companion=1`):

- **📎** top-left on cards that have a supported location;
- **open-original** stays bottom-right (Cooperator reversal vs ADR-0063
  “replace” sentence);
- ordinary browser tabs: no 📎.

`ATTACH_REQUEST` carries only UUIDs. Shell forwards `ATTACH_BEGIN`. SW
builds URL via `pathFor("content")` on the stored origin. 32 MiB cap.
Never click Post. Unbound composer: visible `composer_unbound`, no silent
download. `targetOrigin` is never `*`. `companion_host.js` owns `message`
events; `app.js` does not listen for them.

---

## 13. Companion architecture that must survive

Do not reopen this without a material contradiction and a new ADR.

1. One unpacked Manifest V3 Chromium companion under `extension/`.
2. Service worker is the only FrameNest network client **from X**. Content
   scripts match only `https://x.com/*` and `https://twitter.com/*`.
3. Service worker has no X host permission.
4. X messages use `v: "framenest.companion.v1"`; web bridge uses
   `v: "framenest.companion.web.v1"`; unknown versions/types drop.
5. Content scripts send opaque ids and validated post URL strings. They
   must not `fetch` FrameNest or `pbs.twimg.com`.
6. No CORS. Empty companion-origin allowlist is fail-closed **on the two
   X POSTs**.
7. `RoutePolicy.companion_mutation` is true **only** for
   `POST /api/x/requests` and `POST /api/x/requests/{claim_id}/retry`.
8. Picker `GET /api/x/companion/media` lists `meme` image / animated image
   / video with a `SUPPORTED_MEDIA_CONTENT` location, published **or** the
   caller’s own live cataloged X media.
9. Attach: SW fetches `/api/media/{id}/locations/{id}/content` with
   `X-FrameNest-Request: 1`, streams chunks to the bound X tab.
10. WAR exposes picker + save HTML/CSS/JS to x.com and twitter.com only.
    Sidebar is not WAR.
11. Origin grant: `chrome.storage.local` key `frameNestOrigin`, optional
    host permission `https://*.ts.net/*`.
12. Canonical metadata stays one row per `media_id`. Overlay is ADR-0062.
13. Analyze by AI cannot run on uncataloged bytes.
14. GET/PUT `/api/media/{media_id}/alias` are **not** `companion_mutation`.
15. Accepted ADRs are not edited in place.

INFOSEC: independent R3 of the postMessage bridge + overlay + Save remains
recommended and **never self-certified**.

---

## 14. Backlog (parked; do not hide inside cutover or polish)

These are Cooperator ideas from this session and its parents. They are
**not** this whole’s remaining cutover. Record them so the thread survives.

### 14.1 Gallery per-user alias editor (horizon)

Overlay tables exist (0029). Gallery does not yet let an ordinary user edit
their alias. Target UX, professional restatement:

- Every authenticated user may hold their own title, tags, and description
  on each catalog item (native language included) via overlay, not
  canonical `media_metadata`.
- Admin with `metadata.canonical.write` keeps the existing pencil
  (canonical editor) at the card’s bottom-left.
- Ordinary users later get edit that writes **only their alias** via
  `PUT /api/media/{id}/alias` / `metadata.alias.write`.
- If an ordinary user has no canonical-edit pencil **and** an admin AI
  suggestion exists, show a **lightbulb emoji** as entry into suggestion
  review.
- User may load an AI suggestion over their alias, then still edit.
- Several suggestions / several models: dropdown of model + version;
  selecting an entry **loads it**; no separate Load button.
- ADR-0023 remains: AI drafts assist; they do not own metadata.

Suggested later identity (not selected):
`framenest-gallery-per-user-alias-editor-mvp`.

### 14.2 Settings → General → Language (horizon)

General tab with Language first. Later AI naming (for example Slovak
titles) should follow that setting. Suggested later identity:
`framenest-settings-general-language-mvp`.

### 14.3 Analyze by AI execution after catalog (horizon)

Save popup admin control currently **only saves**. Analysis runs in
FrameNest after `media_id` exists. Do not add `companion_mutation` on
analysis routes. Do not analyze uncataloged X bytes.

### 14.4 Picker / Gallery reading the caller’s alias (horizon)

Companion picker and Gallery still use canonical `display_title`.

### 14.5 Other parked items

```text
🧊 Static X photographs (pinned yt-dlp still filters type != photo)
🧊 Per-asset Save targeting (one alias per permalink today)
🧊 NUC FRAMENEST_COMPANION_EXTENSION_ORIGINS and x_acquisition_root
🧊 Save-alias independent INFOSEC R3
🧊 Sidebar-bridge independent INFOSEC R3
🧊 Web Store packaging / rotating the extension key
🧊 AP upgrade ledger (docs/AP_UPGRADE_OBSERVATIONS.md)
🧊 Closing parent wholes
🧊 Desktop app, Cover Studio, collections, sync, second-copy backup
🧊 Persistent AI drafts as a product
🧊 Public Internet / VPS exposure
🧊 Signed-in X scraping, DMs, cookies
```

Publication of `feat/x-meme-browser-companion` is **no longer parked**; it
was performed this predecessor session. Verify public `main` on restore.

---

## 15. Product boundaries that stay frozen

- FrameNest remains local-first. Loopback-first X APIs. No router port
  forwarding. Remote access remains Tailscale-only.
- Premium Gallery remains a flagship invariant. Ordinary-tab Gallery and
  Details visual behavior stay frozen except the named extension-context
  Attach control (📎 + keep open-original).
- Service worker remains the only FrameNest network client from X.
- Companion never posts on the user’s behalf.
- Empty companion-origin allowlist remains fail-closed on the two X POSTs.
- Original server media under `/srv/media` stays read-only to the service.
- Manual-first metadata (ADR-0023).
- Helper never runs `framenest-db migrate` and never hides migration
  authority.

---

## 16. First work: schema-aware NUC cutover (not a Planner)

Do not write a planning prompt for sidebar hosting. That work is done.

### 16.1 Why routine deploy is blocked

`045f33b` packaged Alembic head is `0029` (tables:
`media_user_aliases`, `media_user_alias_tags`, `x_claim_pending_aliases`,
`x_claim_pending_alias_tags`; `down_revision = "0028"`; no backfill).
Live NUC DB is `0028`. ADR-0060 / `framenest_release.py` compare
`current_revision` vs `head_revision` **from the new package** after
staging is renamed to `/opt/framenest/releases/<SHA>`, then raise
`migration-required` (exit 13) **before** catalog checkpoint and cutover.
Cleanup of `/run/framenest-release-deploy` runs only on success. A later
`deploy` of the same SHA also fails `test_not_exists(target)` if the
complete tree was left behind.

Runbook Section 5 migrate uses `/opt/framenest/current/.venv/bin/framenest-db`,
which today is the **0028** package and cannot apply `0029`. That is the
chicken-and-egg. The 0029 binary only exists on NUC after the helper
packages `045f33b` into `/opt/framenest/releases/045f33b…`.

There is no SHA that contains `companion_host.js` without `0029`.

### 16.2 Recommended path (one recommendation + alternative)

**Recommendation A — expected fail-closed package, explicit migrate from
the new tree, leftover-lock recovery, then rollback-forward.**

Use only existing owners. Do not invent a second deploy engine. Do not
mutate `/opt/framenest/current` in place. Do not copy `0029` files onto the
live 0028 tree.

1. Cooperator establishes sudo timestamp (`~/global_sudo.fish` or `sudo -v`
   on NUC). Worker/Orchestrator uses `sudo -n` only.
2. Re-verify: public main `045f33b`, local HEAD same, tracked clean, status
   still `bfad16b` / `0028` / backup `ready`, `sudo -n true`.
3. Cooperator explicitly accepts: first `framenest-release deploy --release
   045f33b --yes` is **expected to stop `migration-required`** after the
   immutable tree exists; live current stays `bfad16b`; service stays
   active; `/run/framenest-release-deploy` will remain.
4. Fingerprint the leftover lock and the new release directory. Do not
   wildcard-delete. Historical recovery class:
   `03/00-…/20_recovery_00.md` (evidence only). Keep
   `/opt/framenest/releases/045f33b44897a6f3949cc515792336396f1d33a1`.
   Remove only the lock dir after identity checks.
5. Explicit migrate **from the new release path**, not from `current`
   (honest adaptation of runbook Section 5 because `current` cannot contain
   0029). Exact command shape for an already-open NUC session, after you
   substitute nothing except the already-named SHA:

```text
# [NUC / bash]
sudo -u framenest \
  --chdir=/opt/framenest/releases/045f33b44897a6f3949cc515792336396f1d33a1 \
  env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env \
  /opt/framenest/releases/045f33b44897a6f3949cc515792336396f1d33a1/.venv/bin/framenest-db status
sudo -u framenest \
  --chdir=/opt/framenest/releases/045f33b44897a6f3949cc515792336396f1d33a1 \
  env FRAMENEST_ENV_FILE=/etc/framenest/framenest.env \
  /opt/framenest/releases/045f33b44897a6f3949cc515792336396f1d33a1/.venv/bin/framenest-db migrate
#------------------------------------------------------
```

   Expect `0028`→`0029`. Stop on unexpected revision. Catalog backup
   already exists as restore-ready; routine deploy checkpoint did **not**
   run (schema gate is before checkpoint). If Michal wants a fresh verified
   catalog checkpoint **before** migrate, say so and use the existing
   backup owner from the **current** (0028) release, not a invented tool.
6. Verify status `current_revision` and `head_revision` both `0029`.
7. `deploy --yes` of the same SHA will now refuse because the release
   directory already exists. Use the documented command that switches to an
   **already complete** release:

```text
# [MacBook / fish]
# from the FrameNest checkout, after sudo -n is valid
deploy/ubuntu/framenest-release rollback --release 045f33b44897a6f3949cc515792336396f1d33a1 --yes
#------------------------------------------------------
```

   ADR-0060: rollback switches to an already complete release under
   `/opt/framenest/releases/<SHA>`. Here the already-complete tree is the
   newly packaged `045f33b` after schema match. Semantically it is a
   forward cutover via the rollback entry point because `deploy` cannot
   republish an existing SHA. Do not `ln -s` by hand.
8. `framenest-release status` must show `active_release: 045f33b…`,
   `database_revision: 0029`, `service_active: active`.
9. Michal: Reload unpacked; Settings Connect to the same Tailscale origin;
   open x.com with composer bound; Gallery 📎 top-left.

Default: issue this as one or two bounded **operations Workers** (recovery
is historically Worker-shaped; migrate+rollback may be a second). If Michal
again says no Worker, you may execute the same envelope yourself with the
same exact-path stop rules.

**Alternative B — stop until a dedicated schema-migration whole extends the
helper.** Safer. No 📎. Only if he rejects A.

**Rejected C — cherry-pick `companion_host.js` onto a 0028-only SHA.**
Rewrites the product to ship sidebar without overlay. Do not.

### 16.3 What you must not do

- Run `~/framenest_routine.fish` through `deploy --yes` “to finish”.
- Run `framenest-db migrate` from `/opt/framenest/current` while current is
  `bfad16b`.
- Hide migrate inside the helper.
- Force-push. Switch local `main`. Amend published commits.
- Apply AP pin as a side effect.
- Enable companion origins “so Save works” inside the 📎 cutover unless he
  explicitly opens that host-config grant.
- Chase 📎 with another CSS/handshake Worker against `bfad16b`.
- Close the whole because publication PASS exists.

---

## 17. After 📎 is visible: polish loop

Michal will test in practice and then polish with you. Stay Extra High.
Native Plan Mode off for you.

Rules for polish:

- One live attached defect → one bounded correction Worker (or you, if he
  again forbids a Worker and the change is still product code: **you still
  do not implement product code**; issue a Worker or stop).
- Do not reopen Save freeze, Attach float, picker-as-gallery, grey-black
  chrome, or ADR-0061/0062/0063 bodies.
- Do not pull Section 14 into “while we are here”.
- Visual acceptance belongs to Michal.
- Independent R3 remains a later grant, never self-certified.

When he is satisfied that the companion is usable in practice, then and
only then consider ORCHESTRATOR closure of **this** whole. Parents stay
open. Alias editor / language / Analyze / NUC origins are later wholes he
selects.

---

## 18. Git, publication, and NUC authority

Predecessor session publication grant was Cooperator “finish with deploy”
plus the fact that routine deploy requires public main == HEAD. That grant
does **not** automatically renew for you.

Your default Git authority is **none** beyond writing Meta prompt/report
files for this whole, including this class of handoff.

Do not commit FrameNest unless a later grant names the exact branch and
paths. Do not push unless a later grant names the exact object. Do not
fast-forward local `main`.

NUC mutate (migrate, leftover-lock delete, rollback/cutover, `deploy --yes`)
requires an explicit bounded grant in **this** session after you restore
and present Section 16. Capability (sudo timestamp, SSH agent) is not
authority.

---

## 19. Meta trace for this whole

Agent Orchestrator:

- writes each issued prompt to its exact path;
- validates returned reports and preserves them verbatim;
- stages only the completed prompt/report pair when archival is authorized;
- must not force-push or silently supersede history.

Worker:

- may write only the exact report path in its prompt;
- may not commit or push Meta.

Do not mix parent 03 or 04 pairs into this whole’s archival unless named.

Suggested later pair after cutover exists (you name ordinals from live
files; do not skip 05):

```text
06_… operations prompt / 06_report_00.md
```

---

## 20. Out of scope unless Michal later selects them

Everything in Section 14, plus:

- AP upgrade / `ap upgrade cisarik/framenest`
- reconstructing gpgconf / printing SSH_AUTH_SOCK
- enabling NUC X acquisition as part of 📎 cutover
- Web Store publication
- implementing product UX yourself because he is in a hurry

---

## 21. Stop conditions

Stop and talk to Michal when:

- Extra High cannot be provided as routed;
- HEAD or public main is not `045f33b` and the divergence is material;
- live `save.html` no longer matches Section 11.1;
- someone wants CORS, auto-Post, `all_urls`, or content-script fetches;
- someone wants the full FrameNest website in the in-page Attach popup;
- someone wants to implement the alias editor, language tab, or Analyze
  execution inside cutover;
- Analyze by AI is proposed against uncataloged X media;
- `deploy --yes` is requested while `database_revision` is `0028`;
- leftover-lock identity checks fail;
- migrate reports an unexpected revision;
- NUC password or unapproved privilege is required;
- the same correction/recheck loop repeats;
- a newer Cooperator decision contradicts this handoff.

Do not stop for harmless formatting, a stale ADR sentence, or an optional
tool the declared route does not require.

---

## 22. First response and immediate behavior

After receiving this handoff:

1. Acknowledge Michal briefly in Slovak. Confirm Extra High, Native Plan
   Mode off for you, no Planner, remaining gate = schema-aware NUC cutover
   then live 📎.
2. State that you are beginning read-only restoration.
3. Perform the repository / AP / Meta / NUC status gates directly.
4. Confirm HEAD, public main, `save.html`, sidebar Connect-in-Settings, and
   NUC `bfad16b`/`0028` against Section 9 / 11.
5. Summarize only material restored facts and conflicts.
6. Present Section 16 recommendation A vs alternative B. One decision:
   grant migrate+cutover, or wait.
7. Do not ask Michal what feature to choose.
8. Do not ask him to repeat the brainstorming.
9. Do not paste Worker prompts into chat.
10. Do not implement product code.
11. Do not run `deploy --yes` during restore.
12. Do not tell him 📎 is ready until status shows `045f33b` / `0029` and
    he has had a chance to look.

Recommended first Slovak facts so he does not have to remember the prior
chat:

- Save popup ostáva zmrazený.
- In-page Attach ostáva quick attach (jeden JPEG, šípky).
- Side panel je zelený OS chrome + reálny FrameNest web; Connect je v
  Settings.
- 📎 naživo ešte nie: NUC stále `bfad16b` / schéma `0028`. Candidate
  `045f33b` už je na public `main` a `check` prešiel.
- `~/framenest_routine.fish` teraz nespúšťať až po deploy — zasekol by
  NUC na `migration-required`.
- Alias editor, jazyk, skutočné Analyze, NUC origins pre Save — backlog.

---

## 23. Success for this Orchestrator session

Success is not another sidebar redesign.

Success is:

- restored evidence that matches or honestly supersedes Section 9;
- NUC serving `045f33b` with database `0029` without a leftover lock and
  without a second deploy engine;
- Michal seeing 📎 top-left on hosted Gallery cards (open-original still
  bottom-right) with a bound X tab;
- honest residual: NUC Save still fail-closed; R3 never done; parents
  not closed; Section 14 still visible;
- a polish loop that answers his live observations without melting the
  three surfaces;
- this whole closed only after he accepts live practical use, or he
  explicitly parks 📎/Save residuals.

Show discipline. Separate the three surfaces. Do not hide 0029. Carry the
backlog. Then move.

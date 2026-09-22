# Fresh Orchestrator handout — Kronika public identity and clean start

You are a **fresh** terminal-capable Orchestrator for a new public product
**Kronika**, under Analytic Programming. Load **this file completely** before
any Worker prompt. It is not a Worker prompt, not a plan, not a mutation
receipt, and not a substitute for the pinned AP documents.

The private lab at `/home/agile/Tools/cli_chatgpt` is the experimental
predecessor. This whole turns that lab into a professional public open-source
repository named Kronika. The first Worker is a **Planner**. Do not implement
product code yourself. Do not push to GitHub yourself unless a later explicit
Cooperator grant names that push.

If a later explicit Michal message contradicts this file, the later message
wins. Record the conflict. Do not paper over it.

```text
STOP: Do not implement product code. Issue Workers.
STOP: First Worker is Planner (Native planning mode: required).
      Plan UI approval is not implementation authority.
STOP: Do not push origin. Publication is Cooperator-owned.
STOP: Do not create the GitHub repo. Michal creates the empty public repo.
STOP: Do not squash or delete the local lab history. Public main is a
      new clean history; keep the lab commits on a local non-pushed branch.
STOP: Do not implement Tailscale bind, a remote listener, native Android/iOS
      apps, share-sheet targets, or a hosted internet surface in this whole.
STOP: Do not restore watch/scheduler/notification machinery.
STOP: Do not turn Kronika into a group chat.
STOP: Do not copy docs/environment.md household URLs or host paths into
      public docs.
STOP: Do not upgrade AP. The pin governs.
STOP: Do not spawn Workers or subagents. Manual dispatch.
STOP: Communicate with Michal in Slovak. Feminine self-reference.
      Masculine address for him.
STOP: Extra High. No Max unless Michal selects it.
```

Paste seed for a new Agent chat (pointer only, not durable authority):

```text
Resume this AP-integrated Kronika project as a fresh Orchestrator.
Read /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/00_handout.md
completely before any Worker prompt.
Begin read-only. Restore canonical state and the declared AP pin.
Do not mutate. Do not implement product code. Do not push.
Michal already selected this bounded whole: kronika-public-identity-and-clean-start
(professional public identity, clean tree, empty GitHub repo waiting, first
push only after the cleaned tree exists).
Family Tailscale access and native share apps are the NEXT whole, not this one.
Confirm you understand the product thesis and the Git history split
(lab branch stays local; public main starts clean), then issue Planner
01_planning_00.md with Plan Mode on.
Communicate with Michal in Slovak. Extra High. No Max.
```

---

## 0. Handoff identity

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Orchestrator profile: terminal-capable repository and operations coordinator
Orchestrator handoff artifact:
  kronika/00/00-kronika-public-identity-and-clean-start/00_handout.md
Predecessor: none in Meta. Private lab only.
Logical whole identity:
  kronika-public-identity-and-clean-start
Current phase: restore; issue Planner; approval-gated plan; then one
  bounded implementation grant at a time
Native planning mode: required for the Planner; not-used for implementation
Reasoning recommendation: extra-high
Internal delegation posture: one accountable active Worker by default
Cooperator: Michal
Lab checkout: /home/agile/Tools/cli_chatgpt
Intended public repository: https://github.com/cisarik/kronika
Pinned protocol: .ap gitlink -> https://github.com/cisarik/ap.git
AP pin at handoff (verify, do not upgrade):
  7478ddb07d2c3911f79e1aa1441f0115a31c45d8
External analytic trace: /home/agile/meta  project key kronika
Lab HEAD at handoff (verify):
  2727451d2502925377637e19fa435917c970a996
Lab remotes at handoff: none
```

This handout grants **no** repository, Git, host, account, browser,
credential, or publication mutation authority. Those arrive only in complete
Worker prompts after the plan is accepted.

---

## 1. Roles and dispatch

COOPERATOR is Michal. He owns the objective, public GitHub, Tailscale,
ChatGPT account risk, license, and first push.

Speak with Michal in **Slovak**. Worker prompts and formal Worker reports
are **English**. Every standard Worker terminal report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

**Manual dispatch is a hard rule.** Never spawn a Worker or subagent. Write
the complete prompt to the Meta path, tell Michal the exact file, and stop.
When he returns the terminal report (or the Worker writes it to Meta),
reconcile it as a claim package against repository evidence.

In every Worker prompt, grant the Worker authority to write its terminal
report atomically to:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/<session>_report_<meta-exchange-index>.md
```

The Cooperator commits Meta himself. You write files; you do not commit or
push Meta unless he later explicitly asks.

Terse replies (`ok`, `ano`, `pokracuj`) continue the already selected scope.
They never select a new whole.

---

## 2. Product thesis (locked)

Kronika is a **household chronicle**: a durable library of web searches and
deep research the family wants to reopen. It is not ChatGPT history, not a
group chat, and not a replacement for existing family channels.

Architecture that this whole must make *legible* in public docs, not implement
beyond identity:

```text
one household capture host  = logged-in ChatGPT Plus/Pro + local engine
                              + library + manager UI
family phones               = open the library over Tailscale
ChatGPT project "web"       = scratch; Kronika is the archive
share                       = opt-in; Private remains Private
authoring + library check   = kept
desktop Chrome extension    = later family-admin / capture surface
Android/iOS share apps      = later lightweight share targets
```

Capture today lives in the lab as a stdlib Python CLI, loopback bridge,
Chromium headless executor, optional Brave/Chrome MV3 extension, SQLite
library, and a no-JavaScript manager UI. That engine is the starting tree.
The public story leads with the family library and the architecture, not
with “we share one Plus account to drive chatgpt.com”.

Honest residual risk still belongs in README/SECURITY: unofficial,
unaffiliated with OpenAI, may conflict with ChatGPT terms, account risk is
the operator’s, AS IS, no warranty. A disclaimer is not a ToS license.

---

## 3. Mission of this whole

Deliver a **professional public identity** that a hiring manager can
understand in about ninety seconds, and a **clean first GitHub push** that
does not dump the lab experiment log.

In scope:

1. Product rename in user-facing surfaces (README, CLI help, extension name,
   manager page titles, `pyproject.toml` description).
2. Short public docs: README, LICENSE, SECURITY, CONTRIBUTING or a tight
   equivalent, current architecture in one file. English.
3. Strip advertised stubs: `doctor`, `diagnostics`, `recover`,
   `apply-recovery`, `rollback` if they remain stubs.
4. Strip Obscura from the public tree (`tools/obscura-patches`, docs and
   verify path that exist only for the parked engine). Chromium stays.
5. Replace encyclopedic `docs/ROADMAP.md` / `docs/security.md` experiment
   ledgers with short current-state documents. Do not rewrite history; do
   not ship the ledger as the public face.
6. Do not ship `docs/environment.md` household ChatGPT project URL or
   `/home/agile/...` paths.
7. Activate Meta in project rules (`AGENTS.md` currently says external
   trace not-used). Keep AP pin. Do not upgrade AP.
8. Prepare the Git publication recipe: local lab branch preserved; public
   `main` starts as a clean first commit of the cleaned tree; remote
   `cisarik/kronika` (empty public repo created by Michal, no GitHub
   README/LICENSE/gitignore).
9. Tests on the declared route stay green:
   `python -m unittest discover -s tests -t .` from repo root with
   `bash scripts/dev-setup.sh` / `.venv`.

Out of scope (name as successor wholes, do not plan them as this whole’s
implementation slices):

- Tailscale / non-loopback family access
- native Android/iOS share targets
- ChatGPT remote-conversation deletion
- pairwise-friends redesign into a household model
- file upload, recovery loop, model/reasoning control
- Chrome Web Store publication

Success looks like: `github.com/cisarik/kronika` can be opened, the README
explains Kronika without lab jargon, LICENSE is present, the tree still
runs the existing capture/library tests, and `git log` on origin/main is
short and professional.

---

## 4. GitHub procedure (Cooperator-owned create; Worker-planned recipe)

Michal creates the empty repo **before or during** this whole, but nobody
pushes until the cleaned tree exists:

1. GitHub → New repository
2. Owner `cisarik`, name `kronika`
3. **Public**
4. Do **not** initialize with README, `.gitignore`, or LICENSE
5. Create. Stop. No `git remote add` until the plan names the exact
   commands and Michal accepts the first-push grant.

History split (binding recommendation; Planner may refine mechanics, not
the intent):

```text
local lab branch  = full 190-commit cli_chatgpt history, never pushed
public main       = orphan or equivalent clean first commit
```

Do not `git push` the current `main` onto `origin`. That would publish
stealth/ToS/Obscura experiment subjects as the interview log.

---

## 5. Rename guidance for the Planner

Cheap and expected in this whole:

- User-facing name Kronika
- CLI program name `kronika` if it does not explode the slice
- Extension display name
- Manager HTML titles
- README/AGENTS product title

Decide explicitly, with a test-cost bound:

- Python package `chatgpt_cli` → `kronika` (recommended if the suite stays
  green in this whole; otherwise keep the module and document it as
  internal)
- XDG state dir currently `~/.local/state/chatgpt-cli`. A clean break to
  `kronika` is acceptable: this is not yet a family production install.
  Do not write an elaborate migrator unless evidence requires it.
- Working directory may stay `/home/agile/Tools/cli_chatgpt` until Michal
  chooses to rename the folder; do not block the whole on a folder rename.

---

## 6. Public documentation bar (interview-grade)

README must answer, in this order:

1. What Kronika is (family chronicle of searches worth keeping)
2. What it is not
3. Architecture diagram (capture host, local library, Tailscale as the
   planned family path — planned, not claimed as shipped)
4. Status: experimental, household-scale, early
5. Requirements and a short honest quick start of what actually works
   today (local loopback library + capture host)
6. Security invariants in a short list
7. Experimental / ToS / no-warranty paragraph
8. License

Do not lead with shared-account automation. Do not claim Android Chrome
extensions. Do not claim Tailscale works until a later whole lands it.
Do not paste the lab ROADMAP.

LICENSE: MIT unless Michal picks another OSI license during planning.
SECURITY.md: threat boundary in one page, not the lab ledger.

---

## 7. Protocol study before the first Worker prompt

Verify independently. This handout is subordinate to current AP.

1. Lab `AGENTS.md`
2. `.ap/AP.md` spine for Orchestrator
3. `.ap/AP_ORCHESTRATOR.md`
4. `.ap/AP_WORKER.md`
5. `.ap/PROMPT_CONTRACTS.md`
6. `.ap/ARTIFACT_LIFECYCLE.md`
7. `.ap/INFOSEC.md` when writing public security text
8. This directory’s `00_notes.md`

Do not upgrade the `.ap` gitlink. Expected pin at handoff:
`7478ddb07d2c3911f79e1aa1441f0115a31c45d8`. If public `cisarik/ap` `main`
has moved, record it; do not retarget this project in this whole.

Declared execution route remains the lab route until the plan changes it:

```text
bash scripts/dev-setup.sh
python -m unittest discover -s tests -t .
python -m chatgpt_cli <args>    # until renamed
```

---

## 8. Meta

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
```

Opening notes exist. You append Orchestrator entries; you do not rewrite
this handout in place. Worker prompts:

```text
01_planning_00.md
```

Matching report:

```text
01_report_00.md
```

Meta filenames follow `/home/agile/meta/README.md`. Michal commits Meta.

---

## 9. First Worker

After read-only restore and a short confirmation to Michal that you
understand the thesis and the history split, issue **one** Planner prompt:

- Native planning mode: required
- Fresh Worker session
- English prompt
- Bound to `kronika-public-identity-and-clean-start`
- Must produce a slice plan that a later implementation Worker can execute
  without inventing product identity
- Must name the successor whole `kronika-tailnet-family-library` as
  **next, not now**
- Must include a publication recipe that does not push lab history
- Must keep INFOSEC in view: no secrets, no household URLs, no remote bind

Then stop at the dispatch boundary.

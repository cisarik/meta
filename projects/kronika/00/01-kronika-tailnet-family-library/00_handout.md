# Fresh Orchestrator restoration — successor whole `kronika-tailnet-family-library`

This handout restores a fresh Orchestrator for the **next** logical whole. It
does **not** reopen the closed whole `kronika-public-identity-and-clean-start`.
The closed whole is frozen: do not re-plan it, do not re-issue its slices, do
not move its refs.

```text
STOP: Do not implement product code yourself. Issue Workers.
STOP: The first Worker of the successor whole is a Planner (session 01,
      exchange 01), native planning mode required, fresh session, manual
      dispatch. Do not skip to implementation.
STOP: Do not reopen kronika-public-identity-and-clean-start. Do not re-issue
      S1-S5, C1, A1, or A2. Its closure is final; only its publication
      (P1/P2/V1) remains Cooperator-owned and parked.
STOP: Do not push, add origin, or move any ref. Publication is a separate
      explicit Cooperator grant; local main is unpushed.
STOP: Do not recreate or delete lab/cli-chatgpt-190, work/kronika-clean-start,
      or public/kronika-initial.
STOP: Do not open, quote, copy, or display docs/environment.md. It is absent
      from the public tree; it exists only on the unpushed lab history.
STOP: Do not read ~/.local/state/chatgpt-cli, ~/.local/state/kronika, or any
      live token/profile/db.
STOP: Do not upgrade AP. The pin governs.
STOP: Do not spawn Workers or subagents. Manual dispatch.
STOP: Communicate with Michal in Slovak. Feminine self-reference.
      Masculine address for him.
STOP: Extra High. No Max unless Michal selects it.
STOP: Terse "ok" / "ano" / "pokracuj" continues the current slice. It never
      selects a new whole.
```

Paste seed for a new Agent chat (pointer only, not durable authority):

```text
Resume the AP-integrated Kronika project as a fresh Orchestrator for the
successor whole kronika-tailnet-family-library.
Read /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/00_handout.md
completely before any Worker prompt.
Begin read-only. Restore canonical state and the declared AP pin.
Do not mutate. Do not implement product code. Do not push. Do not re-plan.
The predecessor whole is closed: local main = 66c40d43c577276b0ad304a494fbbb1ffb6fc933,
tree 848f247434deea4c217170c012612b39e41557f3, A2 acceptance-PASS; publication parked.
Then open the successor whole's first Planner (session 01) with native planning mode ON.
Communicate with Michal in Slovak. Extra High. No Max.
```

---

## 0. Handoff identity

```text
Role: ORCHESTRATOR
Orchestrator session target: fresh-agent-orchestrator-session
Orchestrator profile: terminal-capable repository and operations coordinator
Capability profile: Orchestrator
Live handout: 00_handout.md (this file)
Superseded handouts: predecessor 00_handout.md, 01_handout.md, and the misplaced 02_handout.md
Logical whole identity: kronika-tailnet-family-library (new)
Predecessor whole: kronika-public-identity-and-clean-start (closed)
Current phase: restoration, then the successor whole's initial planning
Native planning mode for the first Worker: required (Planner)
Reasoning recommendation: extra-high
Internal delegation: one accountable active Worker; never spawn
Cooperator: Michal
Lab checkout: /home/agile/Tools/cli_chatgpt
Intended public repository: https://github.com/cisarik/kronika (no refs at last
  check; re-verify before P1)
Pinned protocol: .ap gitlink -> https://github.com/cisarik/ap.git
AP pin (verify, do not upgrade):
  7478ddb07d2c3911f79e1aa1441f0115a31c45d8
Predecessor trace directory:
  /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
This trace directory:
  /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/
External analytic trace: /home/agile/meta  project key kronika
```

This handout grants **no** repository, Git, host, account, browser, credential,
or publication mutation authority. Those arrive only in complete Worker prompts.

## 1. First thirty minutes

1. Read `AGENTS.md` in the lab checkout (Kronika product rules).
2. Read `.ap/AP.md`, `.ap/AP_ORCHESTRATOR.md`, `.ap/AP_WORKER.md`,
   `.ap/PROMPT_CONTRACTS.md` (Implementation Authority Record), and
   `.ap/ARTIFACT_LIFECYCLE.md`.
3. Read the predecessor's frozen notes and closure in
   `.../00-kronika-public-identity-and-clean-start/00_notes.md`, plus
   `09_report_00.md` and `01_report_00.md` in that same predecessor directory.
4. Re-measure §2 read-only. If anything does not hold, stop and tell Michal.
5. If it holds: write **one** Planner grant to `01_planning_00.md` in this
   directory for `kronika-tailnet-family-library` (Worker session 01,
   exchange 01, fresh session, native planning mode required, manual dispatch).
   `00_notes.md` already exists. Do not recreate the directory.
6. Give Michal the path. Stop at the dispatch boundary.

Do not implement the successor whole yourself. Do not open a Planner for the
closed whole. The predecessor plan is closed.

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
git remote
git rev-parse HEAD:.ap
git -C .ap rev-parse HEAD
test ! -e docs/environment.md
test ! -e docs/human-steps.md
test ! -e docs/ROADMAP.md
test -f README.md && test -f SECURITY.md && test -f CONTRIBUTING.md
git ls-remote --heads https://github.com/cisarik/kronika.git
sha256sum /home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/09_report_00.md
```

Expected at closure:

```text
branch                    main
HEAD                      = main = public/kronika-initial
                            66c40d43c577276b0ad304a494fbbb1ffb6fc933
parents                   none (parentless root)
tree                      848f247434deea4c217170c012612b39e41557f3
work/kronika-clean-start  30e02a327e63255e1a02ec8c0709c15b38988191
lab/cli-chatgpt-190       2727451d2502925377637e19fa435917c970a996 (190 commits)
remotes                   none
worktree                  clean
AP pin                   7478ddb07d2c3911f79e1aa1441f0115a31c45d8 in gitlink
                          and .ap HEAD
public repo               no refs
A2 report SHA-256         daec731e81ea73918401b0d9d1d2cf75dd94dbb3a77e92b8fff208ad2f19b1c3
```

Also prove, without mutating: `git merge-base --is-ancestor` of the lab tip
against `main` exits 1 (no lab ancestry), and the previous root
`827dae85c2794914c3adcb467de9b21ee8998463` survives only in the reflog and the
Meta evidence.

If the public repository has refs, or any expected value differs, stop before
any publication recipe and tell Michal.

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
| Publication | parked; no remote; `main` unpushed |

Accepted decisions still in force (see the frozen `00_notes.md`): product name
Kronika; one household; durable shared library; opt-in share; no group chat,
notification, watch, scheduler, or ChatGPT-history framing; internal
compatibility identifiers preserved; family access is the next whole; native
share apps and the desktop family-admin surface come later; MIT license;
unofficial/AS IS/no-affiliation posture.

## 4. Product thesis and successor scope

Kronika is a **household chronicle**: searches and deep research the family
wants to reopen. Not ChatGPT history. Not a group chat. Not a replacement for
Signal or mail.

```text
one capture host     = Plus/Pro + Chromium + library + loopback manager
family phones        = this whole: a reachable, authenticated family surface
                       over Tailscale to the same library
ChatGPT project web  = scratch; Kronika is the archive
share                = opt-in
authoring + check    = kept
desktop extension    = later family-admin surface
Android/iOS share    = later, after this whole
```

The successor whole `kronika-tailnet-family-library` owns: a family-reachable,
authenticated library surface (the first family-testable behavior), the
Tailscale/network topology decision, authentication for family members, and the
minimum hardening that a non-loopback surface requires. It does **not** own
native share apps, the desktop family-admin extension, remote conversation
deletion, file upload, or any external LLM integration.

Open questions for the Planner (do not pre-decide them in the handout):
whether the manager becomes the family surface or a new read-only surface; how
device identity interacts with the existing local accounts; TLS/cert handling
on the tailnet; share semantics for family members; and how the loopback-only
invariants evolve without weakening the existing bridge and manager contracts.

The loopback-only boundary is a shipped security invariant today. Any change to
it must be explicit, planned, independently accepted, and must not weaken the
existing token, Host/Origin, render-key, or account-scope boundaries.

## 5. Backlog and ledger candidates carried forward

These are non-authorizing observations. Do not implement them without a grant;
the successor Planner may adopt any of them into the new whole or park them
again.

1. Parked test-isolation ordering dependency: the four quiet-stderr tests in
   `tests/unit/test_client.py` fail in a focused module set that omits
   `tests.unit.test_bridge_startup`, because `logging.basicConfig` has not been
   installed. The declared full route passes. Classified pre-existing,
   explicitly parked.
2. Minor wording residuals, non-blocking: `--file` help and the engine comment
   are shorter than the canonical `file upload is not available in this build`
   sentence; `extension/src/headless/runner.mjs` carries no upload message
   field.
3. Frozen `docs/contracts/manager-surface-v3.md` through `v5` still name the
   predecessor executable `chatgpt-cli library ui`; v6 and `docs/usage.md`
   name `kronika`. Frozen history, not an active advertisement.
4. Six local `refs/codex/turn-diffs/checkpoints` refs exist, are not remotes,
   and are outside the four named branches. Do not push or delete them.
5. Root CLI help uses the word "diagnostics" only in the sentence about stderr
   progress; that is not a command.
6. `probe.mjs` creates the caller-supplied profile directory before refusing
   to start a missing Chromium binary (`E_PROBE_CHROME_MISSING`).
7. File upload remains unavailable by design; the contract, help, and runtime
   now agree.
8. The closed whole's `docs/environment.md` is deleted from the public tree and
   exists only on the unpushed lab history. Never open or copy it.

## 6. Publication (parked, Cooperator-owned)

Publication was parked by the Cooperator when the whole closed. When Michal
decides to publish, that is a separate explicit grant sequence:

```text
P1  configure origin for the accepted clean root
P2  first non-force push of main only (no lab/work refs, no tags)
V1  direct public readback and a fresh verification clone
```

The accepted root is `66c40d43c577276b0ad304a494fbbb1ffb6fc933` with tree
`848f247434deea4c217170c012612b39e41557f3`. The command-level recipe is in the
predecessor plan `01_report_00.md` §4 (Gates 7–9), including the empty-remote
recheck, the exact refspec `refs/heads/main:refs/heads/main`, the no-force
rule, and the direct readback. Re-check that `cisarik/kronika` is still empty
of refs immediately before P1. Never push `lab/cli-chatgpt-190`,
`work/kronika-clean-start`, or `public/kronika-initial`.

## 7. How to lead Michal

Slovak, masculine address, feminine self-reference. One outcome paragraph plus
one dispatch instruction. Do not lecture AP, do not dump protocol, do not
re-open naming, do not ask him to choose among locked decisions. When he is
confused, name the file to paste and the chat that should receive it.

Pattern:

1. Restore and verify read-only. Tell him what is true in one block.
2. Write the next Worker prompt to the exact Meta path.
3. Tell him: new Agent chat (or the same chat for a renewed exchange), Plan
   Mode ON or OFF as the prompt declares, Extra High, no Max, paste that file.
4. When the report lands, read it from disk, reconcile it against git, then
   write the next grant.

He sends Worker results back to you. You are the Orchestrator, not the Worker.

## 8. Worker grant quality bar

Every grant is a complete new authority, not a delta chat. Use the shape the
predecessor prompts established (`02_implementation_00.md`,
`05_implementation_00.md`, `07_acceptance_00.md`): exact baseline and
allowlist, repository gate, positive and negative authority, declared execution
route, staging and commit rules, stop conditions, report contract, and the
external trace / delivery record. Bind the project-declared execution route:
tests `python -m unittest discover -s tests -t .`; CLI `python -m kronika`;
bridge `python -m kronika bridge`. `python` is `.venv/bin/python` when the venv
is active.

Git safety, binding for every grant: never update git config; never force,
hard-reset, or clean to manufacture state; never `--no-verify` /
`--no-gpg-sign`; never `git add -A` / `git add .`; never amend unless all
local amend conditions hold and Michal asked; never push unless a publication
grant names the exact refspec; never push the lab or preparation refs.

Meta grammar (`/home/agile/meta/README.md`): Worker prompt/report pairs use
`<session>_<phase>_<exchange-minus-one>.md` and
`<session>_report_<exchange-minus-one>.md`; a new Worker session starts at
`_00`. Handouts and closures share their own sequence; the next prefix in the
successor directory starts at `00`.

## 9. First Worker you issue

The successor whole's first Worker is its Planner:

```text
Logical whole identity: kronika-tailnet-family-library
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session profile: Planner
Worker session target: fresh-worker-session
Native planning mode: required
Phase: planning
Delivery route: manual Cooperator delivery
Prompt: /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/01_planning_00.md
Report: /home/agile/meta/projects/kronika/00/01-kronika-tailnet-family-library/01_report_00.md
```

This directory and its `00_notes.md` already exist.

## 10. Success of the successor whole

The successor whole is successful when a family member can open the household
library from a phone over Tailscale through an authenticated, hardened surface
that does not weaken the existing loopback contracts, with its own accepted
plan, implementation slices, and fresh independent acceptance. Native share
apps and the desktop family-admin surface remain later wholes.

The predecessor whole's closure signal has been emitted. Do not emit it again
for the closed whole; the successor whole has its own closure decision.

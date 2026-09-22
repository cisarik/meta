# Era 00 Whole Notes — Kronika public identity and clean start

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned after restore, append-only during the whole,
frozen at closure. Non-authorizing. Public-safe by default. Michal owns any
meta Git commit.

Working identity (Cooperator-selected 2026-09-22; Planner-locked in
`01_report_00.md`):

```text
kronika-public-identity-and-clean-start
```

Trace:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
```

Handout: `01_handout.md` (2026-09-22, after S1 PASS). Live for the incoming
fresh Orchestrator. `00_handout.md` is historical Planner bootstrap.

Lab checkout (not yet the public product repo):

```text
/home/agile/Tools/cli_chatgpt
work/kronika-clean-start  1c8a659073368f26c289cbedf616a2dfed338b4b  # S1
main                      2727451d2502925377637e19fa435917c970a996  # lab tip
lab/cli-chatgpt-190       2727451d2502925377637e19fa435917c970a996  # 190 commits
no Git remote
AP pin 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

## Session log

- **2026-09-22 — Cooperator brainstorm (pre-Orchestrator).** Product restart
  from the private `cli_chatgpt` lab: Kronika is a household chronicle of
  web searches and deep research worth returning to, not chat history and not
  a group chat. One household ChatGPT Plus/Pro account does capture. Family
  members keep using existing chat channels. Authorship (follow-up prompt into
  an existing record) and `library check` stay. Notification/watch/group-chat
  framing is a dead end. ChatGPT project `web` is scratch; Kronika is the
  archive. Android Chrome extension is rejected (platform does not support it).
  Family access is Tailscale, same pattern as the household NUC. Later:
  lightweight native Android/iOS share targets; desktop Chrome extension as
  family-admin surface. Public GitHub from day one for a professional
  open-source interview artifact. Empty GitHub repo first; first push only
  after a clean identity tree. Meta starts at this directory.

## Locked Cooperator decisions (intent, not ADR)

1. **Product name:** Kronika. GitHub repo `cisarik/kronika`, public.
2. **Audience:** one household. Shared capture account is a household choice,
   not a public multi-tenant product.
3. **What Kronika is:** durable shared library of searches and deep research
   the family wants to reopen. Opt-in share only.
4. **What Kronika is not:** ChatGPT history dump, group chat, notification
   inbox, or a replacement for Signal/mail/family chat.
5. **Keep:** capture of web search and deep research; local SQLite library;
   manager UI; Private vs shared; follow-up authoring; `library check`.
6. **Drop from the public story and, where cheap, from the tree:** doctor /
   diagnostics / recover stubs; Obscura; encyclopedic experiment ROADMAP;
   watch/scheduler (already removed); group-chat framing.
7. **Family client:** web library over Tailscale. Not an Android Chrome
   extension.
8. **Native share (horizon, not this whole):** Android and iPhone
   “Share to Kronika” as a lightweight share-target app. Later they talk to
   the same Tailscale web surface.
9. **Desktop extension (horizon, not this whole):** family-admin / capture
   surface for the household head, not the family viewer.
10. **ChatGPT project `web`:** scratch. Auto-delete of remote conversations is
    later; not this whole.
11. **Public Git history:** do **not** publish the 190-commit `cli_chatgpt`
    lab log. Public `main` starts clean (orphan / first-commit of the cleaned
    tree). Keep the lab history locally as a non-pushed branch.
12. **GitHub create:** Cooperator creates an **empty** public repo (no GitHub
    README, gitignore, or LICENSE). No push until this whole produces the
    cleaned tree.
13. **ToS posture in public docs:** honest experimental unofficial tool;
    may conflict with ChatGPT terms; AS IS; no warranty; no affiliation with
    OpenAI. A disclaimer is not a ToS license.
14. **External analytic trace:** this Meta project `kronika` is now in use.
15. **First Worker of the incoming Orchestrator:** S2 implementation,
    `03_implementation_00.md`, Plan Mode off, this whole only. The Planner
    already ran (session 01). Do not re-plan.

## Recommended first product whole after this one (not authorized)

```text
kronika-tailnet-family-library
```

Family members open the library from phones over Tailscale. That is the first
family-testable behavior. Native share apps need that reachable surface first.

## Session log addendum

- **2026-09-22 — Cooperator boot before S1.** Lab tip preserved as
  `lab/cli-chatgpt-190` at `2727451d2502925377637e19fa435917c970a996`
  (190 commits). Implementation branch `work/kronika-clean-start` created
  from that tip. Local boot commit
  `3c345cbd659ccb5817bb11cbc89d037798553ca8` adds MIT LICENSE, Kronika
  AGENTS rules (CLI route still predecessor names until S1), and a
  public-safe `.gitignore`. `main` remains at the lab tip. No remote, no
  push. S1 Gate 1 branch creation is already done; the next implementation
  grant starts from the boot commit and must not recreate those branches.
  S1 prompt path: `02_implementation_00.md` (fresh Worker session 02 /
  exchange 01). Session 01 remains planning only.

- **2026-09-22 — S1 PASS.** Commit
  `1c8a659073368f26c289cbedf616a2dfed338b4b` on `work/kronika-clean-start`
  (`feat(identity): rename the application and state root to Kronika`).
  Claimed suite: 1192 tests OK, 0 skips. `main` and `lab/cli-chatgpt-190`
  unmoved at `2727451`. Report `02_report_00.md` SHA-256
  `c91d0324b1b4d5b61cf9a3ae9dd510e96269b55c8947e699e7b023e7dbc11302`.
  Successor restoration: `01_handout.md` (SHA-256
  `0c6c024dbc4422c41a2ea78e071f9e6ddd2eb29f7e01cc8161212728ed4b0276`).
  Next Worker is S2 as `03_implementation_00.md` (session 03), not a new
  logical whole. `00_handout.md` is superseded (banner only; body kept as
  history).

## Open gates for the incoming Orchestrator

- Independently verify S1 at `1c8a659` before issuing S2.
- Confirm `cisarik/kronika` is still empty of refs before any P1.
- `docs/environment.md` must still not be opened; S4 deletes by path.
- Publication push remains Cooperator-owned.
- Do not implement Tailscale bind, native apps, or remote listen in this whole.
- Do not re-plan. Do not treat S2 as logical whole 02.

## Session log addendum

- **2026-09-22 — fresh Orchestrator restore (read-only).** Restored from
  `01_handout.md` and independently re-measured §4: `pwd -P` =
  `/home/agile/Tools/cli_chatgpt`; branch `work/kronika-clean-start`; HEAD =
  `1c8a659073368f26c289cbedf616a2dfed338b4b` with parent
  `3c345cbd659ccb5817bb11cbc89d037798553ca8`, tree
  `38e7b7c0a090331ce6e0ea06139215d8d3644109`, subject
  `feat(identity): rename the application and state root to Kronika`; `main` and
  `lab/cli-chatgpt-190` = `2727451d2502925377637e19fa435917c970a996` (190
  commits); no remotes; clean worktree; AP pin
  `7478ddb07d2c3911f79e1aa1441f0115a31c45d8` in both gitlink and `.ap` HEAD;
  `src/kronika` present, `src/chatgpt_cli` and `scripts/chatgpt-cli` absent;
  `scripts/kronika` executable; `docs/environment.md` tracked but not opened;
  `02_report_00.md` SHA-256
  `c91d0324b1b4d5b61cf9a3ae9dd510e96269b55c8947e699e7b023e7dbc11302`;
  `git ls-remote --heads https://github.com/cisarik/kronika.git` exited 0 with
  empty ref output. S1 holds; no mutation performed.

- **2026-09-22 — S2 grant written.** `03_implementation_00.md` (session 03 /
  exchange 01, fresh-worker-session, Fresh Implementation Worker, Native
  planning mode not-used, Extra High, manual dispatch), SHA-256
  `653a54a9a260012e766abd0c697c99eccc44c782380c263e5abaf586340035a2`.
  Baseline `1c8a659`; allowlist re-confirmed against existing paths at that
  baseline; expected commit subject
  `fix(cli): remove unimplemented recovery scaffolding`; report destination
  `03_report_00.md`. Next: Cooperator dispatches to a genuinely fresh Agent
  chat; Orchestrator reconciles the report against git before S3.

- **2026-09-22 — S2 accepted after reconciliation.** Report `03_report_00.md`
  (SHA-256 `34e2fe8134857061e6e95859f711d8720d80fc3c18e3ba77914c0cc6a8bc162f`)
  matches the git result: HEAD `f25392472d043d753a3844c3a9a6321ae5cf09a5`,
  single parent `1c8a659`, tree `209bb1c2d7769f1139f589779539955ba21d556f`,
  subject `fix(cli): remove unimplemented recovery scaffolding`; 17 changed
  paths, all inside the S2 allowlist (14 modified, 3 deletions); worktree clean;
  no remotes; `main` and lab unmoved at `2727451` (190 commits). Independent
  read-only spot checks: `kronika 0.1.0`; `doctor`/`rollback` exit 2 with
  invalid-choice usage; `startup_diagnostics`, the `/v1/files/{fid}` 501
  branch, unknown-path 404, and the author `"recovery"` contract fields all
  present. Suite claim 1187 tests OK (S2 Worker, declared route); not re-run by
  the Orchestrator. S4-owned doc residuals were listed by the S2 report
  (README, security, ROADMAP, architecture identity wording).

- **2026-09-22 — S3 grant written.** `04_implementation_00.md` (session 04 /
  exchange 01, fresh-worker-session, Fresh Implementation Worker, Native
  planning mode not-used, Extra High, manual dispatch), SHA-256
  `00d6110e1b8a9f521b9f8e749b9c38cc77da910917e43dea29b92e10f0f669ce`.
  Baseline `f253924`; allowlist re-confirmed at that baseline; expected commit
  subject `fix(headless): remove the parked engine integration`; report
  destination `04_report_00.md`. Docs scope: current Obscura claims corrected;
  historical records and `docs/ROADMAP.md` reported as S4-owned;
  `docs/environment.md` excluded and not opened.

- **2026-09-22 — Orchestrator near-miss (recorded).** During S3
  reconnaissance a read-only `grep` over `docs/` unintentionally matched
  `docs/environment.md` and surfaced some of its lines in the tool output. No
  content from that file was copied into any prompt, note, or repository
  artifact, and no private value was reproduced. All later scans exclude that
  path; the S3 grant names it as never-open and out of scope.

- **2026-09-22 — S3 accepted after reconciliation.** Report `04_report_00.md`
  (SHA-256 `23e485d43db33e97af7995debc7eff4200022941146ad71ba1eeff3b38ac30c0`)
  matches the git result: HEAD `dc44cfd38093c118310ac032f5252ba29fad2f13`,
  single parent `f253924`, tree `57943d9f6af0f5a9b2c16a57509ef24f52fe4c0e`,
  subject `fix(headless): remove the parked engine integration`; 12 changed
  paths (11 modified, 1 deletion), all inside the S3 allowlist; worktree clean;
  no remotes; `main` and lab unmoved at `2727451` (190 commits). Independent
  read-only checks: no `Obscura` token in `src/`, `extension/`, `scripts/`, or
  `contracts/`; remaining tokens are the test's negative fixtures and the
  historical records listed as S4-owned; `tools/` is gone; no
  `HEADLESS_ENGINE_*`/`headless verify` references remain. Suite claim 1181
  tests OK (S3 Worker, declared route); not re-run by the Orchestrator.
  Report inaccuracy noted: the report's sweep section claims
  `src/chatgpt_cli/` still contains predecessor handlers and pin constants;
  that directory does not exist and no such references remain. The actual tree
  is correct; the sentence is a report error, not a product defect.

- **2026-09-22 — S4 grant written.** `05_implementation_00.md` (session 05 /
  exchange 01, fresh-worker-session, Fresh Implementation Worker, Native
  planning mode not-used, Extra High, manual dispatch), SHA-256
  `c284dcdfd0eef37f9f007a19063d66da75acd72a0fe59ed75f2c53a519d410c7`.
  Baseline `dc44cfd`; expected commit subject
  `docs(kronika): prepare the public documentation and clean tree`; report
  destination `05_report_00.md`. Scope: rewrite README/architecture/
  headless-engine; add SECURITY/CONTRIBUTING/usage; delete security,
  dev-setup, ROADMAP, human-steps, and environment.md (deletion-only, never
  opened); narrow updates to protocol/adapter-pack/contract companions; refine
  `.gitignore` (`obscura-profile/` removed, environment exclusion kept).
  `docs/environment.md` never opened; private host value in human-steps not
  copied.

- **2026-09-22 — S4 accepted after reconciliation.** Report `05_report_00.md`
  (SHA-256 `d4040a1c73a86afff8538b6609a3c000ca6938a8cb5fb7a22faf8e29e8907109`)
  matches the git result: HEAD `b5b5f3811f62d5c83dd411c627a1783fb1bd5d93`,
  single parent `dc44cfd`, tree `8506c9955b448d913cafe03c08b0c3e5495f9952`,
  subject `docs(kronika): prepare the public documentation and clean tree`;
  20 changed paths (15 modified/added, 5 deletions), all inside the S4
  allowlist; worktree clean; no remotes; `main` and lab unmoved at `2727451`
  (190 commits). Independent checks: the five retired documents are absent;
  `SECURITY.md`, `CONTRIBUTING.md`, `docs/usage.md` exist; `LICENSE` blob
  unchanged; managed AP block byte-identical; `.gitmodules` and `.ap` gitlink
  unchanged; only the intended `.gitignore` exclusion mentions
  `environment.md`; privacy scan returns no filenames; no slice codes in the
  rewritten docs; link check finds no missing repository paths; README follows
  the locked order and labels Tailscale as planned; `runner.mjs run` is a real
  mode. Report-format nits only: the phase-qualified field is descriptive
  rather than `implementation-PASS`, and the result fields are absent. Not a
  product defect.

- **2026-09-22 — S5 grant written.** `06_implementation_00.md` (session 06 /
  exchange 01, fresh-worker-session, Fresh Implementation Worker, Native
  planning mode not-used, Extra High, manual dispatch), SHA-256
  `f26f948cf1b2e4f2d8d24f5b1c0cc300eabb20757484635b27e27fa5c45ae2f2`.
  Baseline/accepted clean `b5b5f381`, accepted tree `8506c995`; Git-only
  `commit-tree` recipe with no `-p`, root message
  `feat(kronika): introduce the household research library`, refs
  `public/kronika-initial` and guarded `main` update; expected report
  destination `06_report_00.md`. Public repo rechecked empty of refs at grant
  time.

- **2026-09-22 — S5 accepted after reconciliation.** Report `06_report_00.md`
  (SHA-256 `7c0a4a437e6873d1ec8281ce0e9b8e9c3a80c099d146c8647a42271140c5810b`)
  matches the git result: local `main` =
  `827dae85c2794914c3adcb467de9b21ee8998463`, parentless, tree
  `8506c9955b448d913cafe03c08b0c3e5495f9952` (equal to the accepted S4 tree),
  subject `feat(kronika): introduce the household research library`, author and
  committer `Michal Cisárik <cisarik@users.noreply.github.com>`;
  `public/kronika-initial` = same root; `lab/cli-chatgpt-190` = `2727451` with
  190 commits; `work/kronika-clean-start` = `b5b5f381`; no remotes; clean
  worktree; AP pin `7478ddb` in gitlink and `.ap`; lab tip is not an ancestor
  of `main` (exit 1). Privacy manifest: 132 tracked paths; all required
  absences hold. The public-safety scan's matches are all synthetic
  `chatgpt.com/g/g-p-...` fixtures; the shared contract/unit-test example URL
  remains a review lead for A1 (generated fixture, not printed).
  Old-name hits are preserved identifiers, frozen manager v3–v5 text, and
  legacy-state tests only. No push, no remote.

- **2026-09-22 — A1 grant written.** `07_acceptance_00.md` (session 07 /
  exchange 01, fresh-worker-session, Fresh Independent Audit, Phase acceptance,
  Native planning mode not-used, Extra High, manual dispatch, independence
  required-fresh-independent), SHA-256
  `99208aef476cb352e336173ff983135c4797516ab3fa820d4cf68c57187a508f`.
  Candidate `827dae85` (tree `8506c995`); eight fixed risk claims; fixed
  positive/negative control matrix; INFOSEC R4 milestone audit; read-only plus
  synthetic probes; no corrections; expected report destination
  `07_report_00.md`.

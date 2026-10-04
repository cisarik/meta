# Authoritative Worker prompt — Worker session 13, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `13`, exchange `01`. Stored under the
Meta filename mapping as `13_correction_00.md`, with report destination
`13_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 13
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Task identity: KSI-CORR-05 — dual-accept the companion web protocol, and record the ordering constraint at both sites
Reasoning recommendation: Low
Recommended context capacity: approximately 250k tokens
```

Rationale: one receive-side acceptance check becomes an acceptance set, one
sending site keeps its spelling by design, and two comments are added. That is
mechanical, localized and trivially reversible, which is the `Low` band.

This is correction **C2a**. It closes the second cross-boundary contract that
Worker session `12` found and escalated, under the same Cooperator decision that
settled the first one.

## Why this correction exists

Worker session `12` found, and the Orchestrator independently verified, that
`framenest.companion.web.v1` is **not** an internal protocol string. It is a
validated `postMessage` contract across the browser boundary, and **both sides
gate on it**:

- `src/framenest/adapters/api/web/companion_host.js:8` defines `PROTOCOL`, gates on
  `data.v !== PROTOCOL` at line 75, and emits it at lines 80, 121 and 135. That file
  is **served by the NUC**.
- `extension/ui/sidebar.js:3` defines `WEB_PROTOCOL`, gates on `data.v !== WEB_PROTOCOL`
  at line 28, and emits it at lines 127, 884, 980 and 994.
- `tests/companion_web_bridge.test.js:47`, `tests/companion_review_extension.test.js:1580`
  and `tests/contract/test_local_web_application.py:267` pin the literal on both sides.

Because both sides gate, a unilateral rename on the extension side would leave the
host never seeing `host_hello`, `hosted` false, and `attach()` returning
`{ ok: false, error: "not_hosted" }`. **Meme attach to the X composer would break
silently, with no error the Cooperator would notice**, against any NUC that has not
been refreshed.

This is structurally identical to the companion API version, which the Cooperator
already decided to handle by dual-accept. The same decision applies here.

## Goal

Make the extension accept both spellings of the companion web protocol, keep
sending the retired spelling until the removal cut, leave the NUC-served host
logic untouched, and record the ordering constraint where a future editor will
actually meet it.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: 78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4
Expected subject: feat(companion): send both mutation headers and migrate browser keys on read
Lineage: 18c357c published main -> 90c93ea C1 -> c02c675 C1b -> 24bea56 C1c
          -> 02a8048 C1d -> 0b75675 C1e -> 78c841f C2
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
The branch is deliberately unpublished. Do not push.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator: JavaScript
`576 total, 571 passed, 0 failed, 5 skipped`; Python
`4358 passed, 8 skipped, 3 warnings, 0 failed`; retention module `15 passed`.

## Required mutation

### 1. The extension accepts both spellings

In `extension/ui/sidebar.js`, the receive-side gate becomes an acceptance set over
both `framenest.companion.web.v1` and `kronika.companion.web.v1`, mirroring the
pattern Worker session `12` already introduced in `extension/shared/messages.js`
for the API version. Prefer reusing an exported helper if one fits, rather than
writing a second acceptance function.

A message carrying **any other** value must still be refused exactly as today. The
existing refusal shape, error string and gating must be unchanged.

### 2. The extension keeps sending the retired spelling

**This is the point of the exercise.** The host page gates on its own spelling, so
the extension must continue to **emit** `framenest.companion.web.v1` until the
removal cut moves the host. Sending the new spelling now would break meme attach
immediately, against every NUC.

So the send sites keep their current spelling. Do not "helpfully" update them, and
do not add a comment implying the sending spelling is wrong; say explicitly that it
is retained on purpose and until when.

### 3. The NUC-served host is not changed

`src/framenest/adapters/api/web/companion_host.js` keeps its logic byte-identical.
It is in scope **only** for the comment in item 4.

### 4. Record the ordering constraint at both sites

Add a concise comment at **both** the extension's `WEB_PROTOCOL` definition and the
host's `PROTOCOL` definition, stating in one place and not repeating it at length:

- this string is a validated cross-boundary contract, not an internal identifier;
- **both sides gate on it**, so a one-sided rename breaks meme attach silently
  against any NUC that has not been refreshed;
- the extension therefore dual-accepts but keeps sending the retired spelling;
- the host keeps emitting the retired spelling;
- the rename lands in the removal cut, on both sides together.

A comment is the right instrument here, not an ADR amendment: ADR-0085 is
published and accepted, and an accepted ADR may only be changed by a later ADR that
supersedes it. **Do not edit any ADR.** The Orchestrator records the constraint in
the whole's own notes and will carry it into the removal cut's grant.

## Authority

```text
Positive authority: edit exactly extension/ui/sidebar.js,
  src/framenest/adapters/api/web/companion_host.js (comment only),
  extension/shared/messages.js only if you reuse or extend an existing exported
  acceptance helper there, reported explicitly; and the existing JavaScript test
  files that pin this contract, each reported explicitly; add tests for the three
  acceptance cases; update Part C pins only where genuinely moved, reporting each
  with its exact cause; create one additional local commit on the existing branch;
  run the declared JavaScript route and the declared AP test operations; run
  read-only Git inspection.

Negative authority: any change to the host's gate logic, its emit sites, or any
  other line of companion_host.js beyond the comment; any change to any emit site
  in sidebar.js, so the retired spelling continues to be what the extension sends;
  any change to tests/contract/test_local_web_application.py's existing assertion
  that the retired literal is present in the served asset, since that assertion is
  correct and must keep passing; any change to extension/manifest.json; any change
  to the mutation header, the storage keys, or the API version acceptance from
  Worker session 12; any change to any ADR, to docs/**, to AGENTS.md, to any root
  Markdown file, to deploy/**, to pyproject.toml, to ap.project.conf, to
  src/kronika_capture/**, or to the 36 applied Alembic revision files; any
  new branch, push, tag, merge, rebase or history rewrite; any dependency install,
  update or lockfile change; any NUC contact, including SSH, the NUC worker gate,
  and deploy/ubuntu/framenest-release in every mode; any provider or
  capture-browser contact; any execution of a kronika-capture command; any reading
  of private/, personal Fish configuration, browser profiles, cookies, tokens,
  credential stores, .secrets or ~/.config/opencode; any write to
  /home/agile/meta.

Commands: JavaScript evidence goes only through the declared route,
  `node --test tests/*.test.js`, plus focused `node --test <path>`. Python evidence
  goes only through `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4 --operation <id> -- <argv>`, plus
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline
  78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe
  files under /tmp only. Any other command must be stated in the report with its
  purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one additional local commit on the existing branch. No push, no new
  branch.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp.

Browser authority: none. Do not open a browser, do not touch a real profile. Prove
  behaviour with synthetic in-memory message objects under `node --test`.
```

## Verification

1. Confirm branch `feat/kronika-identity-dual-read`, HEAD `78c841f…`, clean tree,
   submodule at the pin, `ap doctor` PASS, `ap project check --baseline` PASS.
   Stop without editing if any fails.
2. Read `extension/ui/sidebar.js` around lines 1-60 and 120-135, and
   `src/framenest/adapters/api/web/companion_host.js` around lines 1-30, 70-90 and
   115-140, before editing.
3. Reproduce both baselines once: `node --test tests/*.test.js`, and the declared
   `test` operation. Expect `576/571/0/5` and `4358 passed, 8 skipped, 3 warnings`.
   The suite takes about eleven minutes; let it finish once. **Do not edit while a
   suite is running.**
4. Make the changes.
5. Add and demonstrate failing, for each of the three cases: a message carrying the
   **retired** spelling is accepted; a message carrying the **current** spelling is
   accepted; a message carrying **anything else**, including near-miss versions, the
   empty string, null and a non-string, is refused with the existing shape.
6. Add and demonstrate failing a test that the extension's **emit** sites still send
   the retired spelling. That test is the one that prevents a future well-meaning
   edit from breaking meme attach, so it matters more than the acceptance tests.
7. Confirm `git diff --stat 78c841f..HEAD` shows `companion_host.js` as a
   comment-only change, which you must demonstrate by showing that every changed
   line in that file is inside a comment.
8. Run the JavaScript route and the full declared `test` operation once. Report exact
   counts for both.
9. Confirm `EXPECTED_FRAMENEST_CONTENT_PATHS` did not move, and report every Part C
   movement with its cause. Part A and Part B must not move.
10. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E1. One receive-side acceptance set, one preserved send behaviour,
  two comments, and tests. No product behaviour is widened beyond accepting a second
  spelling of a value the host itself emits.
```

## Git

One additional commit on `feat/kronika-identity-dual-read`, parent
`78c841f34b8ef33bb6a27ff2dc9323fd2f6cdfe4`. Suggested subject:

```text
fix(companion): dual-accept the web protocol so the rename cannot be one-sided
```

Do not push. Do not create a new branch.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if either baseline does not reproduce; if dual-accept would require
  changing an emit site, the host's logic, or the host's emitted spelling; if the
  host file cannot be changed comment-only; if the retention membership set moves;
  if any step would need an ADR change or a real browser profile; if context
  pressure reaches the point where a bounded rotation is cheaper than a degraded
  commit.

Completion: one additional commit, both spellings accepted and anything else
  refused with the existing shape, the emit sites proven still sending the retired
  spelling, the host file comment-only, the constraint recorded at both sites, the
  membership set unmoved, both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `13_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC
  contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this correction, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `13` and exchange `01` unchanged. Then:
the exact diff of every path; the three acceptance cases with their failure
demonstrations; the emit-spelling test with its failure demonstration; the
comment-only proof for `companion_host.js`; the exact comment text you added at
each site; the membership set confirmation and every Part C movement with its cause;
baseline and final exact counts for both routes; the branch name and all eight commit
SHAs on this branch; deviations, risks and missing evidence; and one smallest next
step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification.

Finish every terminal report with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

If your client's native surface forces any preamble above the report header,
disclose it on the first line of the report body.

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/12_report_00.md`,
  section 3.7, which is your specification, and the `LEAD` about the Orchestrator's
  unreliable inventory labels.
- `docs/adr/0085-kronika-sole-identity.md` in full, for the boundary you must not
  cross by amending it.
- `extension/ui/sidebar.js` around lines 1-60 and 120-135.
- `src/framenest/adapters/api/web/companion_host.js` around lines 1-30, 70-90 and
  115-140.
- `extension/shared/messages.js`, for the acceptance-helper pattern Worker session
  `12` established.
- `tests/companion_web_bridge.test.js`, `tests/companion_review_extension.test.js`
  and `tests/contract/test_local_web_application.py`, for how this contract is
  pinned on both sides.
- `tests/contract/test_kronika_identity_retention.py`, for the ledger rules.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the remaining sequence is: publish the branch, then a separate bounded
grant for the routine NUC refresh. The NUC refresh must not be presented as making
the companion reload verifiable, because both header spellings are accepted until
the removal cut. The removal cut's grant must carry the ordering constraint for both
cross-boundary strings, clear the retired alarm and the retired keys, and address
the deferred Class 5 identifiers with their paired style edits and rendered
acceptance.
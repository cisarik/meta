# Authoritative Worker prompt — Worker session 15, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `15`, exchange `01`. Stored under the
Meta filename mapping as `15_implementation_00.md`, with report destination
`15_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 15
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C2C — retire the remaining user-visible companion prose and the download stem
Reasoning recommendation: Low
Recommended context capacity: approximately 250k tokens
```

Rationale: an enumerated set of display strings with no logic, no contract and no
judgement left to make once the three exclusion classes below are applied. That is
mechanical and trivially reversible, which is the `Low` band.

This is cut **C2c**. It is the companion-prose cut Worker session `14` recommended,
and it must land **before C7**, because C7 owns the CSS and DOM hooks that live in
the same files.

## Why this cut exists

C2b retired the names on the manifest, the side-panel chrome and the served prose.
It deliberately could not finish the job: its grant forbade the files that carry
the remaining strings, so the product is currently **visibly split**. Orchestrator
verification of that split: `extension/ui/sidebar.html:53` reads `Kronika origin`
while `extension/ui/sidebar.js:838`, in the same dialog, still reads
`Use the FrameNest HTTPS tailnet origin`.

You will fix that. You will also fix the download stem, which Worker session `14`
found and which is arguably more visible than the fallback filename C2b already
retired, because it is what lands in the Cooperator's Downloads folder when a
media file's own name sanitises to empty.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: 09e45e54c8444281c147f9ba799e3602bb57d9aa
Expected subject: refactor(identity): retire the names a person actually sees
Remote origin: https://github.com/cisarik/kronika
Public main: 9c71bfb0a06cb30c5d747816e9067f6a25350c58
NOTE: local main is one commit ahead of public main. Work on local main; do not push.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator: Python `4359 passed, 8
skipped, 3 warnings, 0 failed`; JavaScript `582 total, 577 passed, 0 failed, 5
skipped`; retention module `15 passed`.

## The C2b lesson you must apply

Worker session `14` found that the Orchestrator's rename list was incomplete in
three independent ways, and that the cost was three red tests discovered only in
the eleven-minute full suite. Two of those three were **test pins asserting the
old brand positively**, which the earlier search missed because it looked for
string literals in the product rather than for the brand in an assertion.

Therefore, before you edit anything, produce **two independent enumerations** and
report both:

1. **The display inventory.** For every surface, parse the actual artefact and test
   every letter-bearing text node and every quoted attribute value, rather than
   grepping for known literals. Worker session `14` used this method and it is what
   found the missing fifth `index.html` string.
2. **The assertion inventory.** Enumerate every test assertion that mentions the
   retired brand, by searching tests for the brand in an **assertion context**, not
   only in a string-literal context.

**Reconcile them before editing.** If the count of sites you will change does not
equal the count the display inventory produced, you have either missed something or
mis-classified something. Resolve that before touching a file, and say so.

## Three exclusion classes — apply them precisely

Conflating these is how a cut of this kind breaks a working contract.

**Excluded 1 — the mutation header spelling.** `X-FrameNest-Request` stays until
C7. C2 sends **both** header spellings and the server accepts both. Roughly
twenty-four test assertions pin the old header on purpose. Do not change the header
string and do not repoint those assertions.

**Excluded 2 — global and DOM identifier names.** These are machine-read names, not
display text, and renaming one side is exactly the one-sided defect class this whole
has been preventing:

```text
globalThis.FrameNestCompanion        set by extension/shared/messages.js, read by many
globalThis.FrameNestCompanionWeb     8 occurrences in app.js, 1 in companion_host.js;
                                     this is the cross-boundary global the NUC-served
                                     host sets and the web shell reads
globalThis.FrameNestSidebarBridge
globalThis.FrameNestReviewInbox
title-bar__wordmark and every data-framenest-* / framenest-* CSS and DOM hook
the framenest-attach port name
```

**Excluded 3 — Python class names.** `FrameNestSettings` and its siblings are
referenced across tests. They travel with the package rename at **C3**. Leave every
one of them alone.

## In scope

### 1. `extension/shared/messages.js` — the outcome names

Worker session `14` located thirteen around lines 624-690, for example
`"Save to FrameNest failed"`, `"Save to FrameNest failed—FrameNest needs an update"`,
`"Saved to FrameNest"`. **Orchestrator verification: the server never sends any of
these strings**; `git grep -F 'Save to FrameNest' -- src` returns nothing. They are
local display text, so renaming them is safe. Change the brand word only, and keep
each message's structure and outcome meaning intact.

### 2. The overlay and picker surfaces

```text
extension/ui/save.html:5,12        heading and supporting text
extension/ui/save.js:7             "FrameNest needs an update…"
extension/ui/picker.html:5         title
extension/ui/picker.js:27          "FrameNest companion", "Connect FrameNest in the side panel"
extension/content/x_adapter.js:21,30,1765,1772
                                   "Save to FrameNest", "Attach from FrameNest",
                                   "Close FrameNest picker", "FrameNest search"
```

Re-derive these by the display enumeration rather than trusting the line numbers.

### 3. `extension/ui/sidebar.js` — the status and aria strings

Worker session `14` located eight, including `"Connect FrameNest in Settings"`,
`"Disconnect FrameNest"`, `"Could not reach FrameNest."`, `"FrameNest did not load in
this panel."`, `"This FrameNest server cannot host companion Attach yet…"`, and the
`aria-label` pair at line 486. `sidebar.js:838` is the one that now sits under a
`Kronika origin` label and is the most visible inconsistency this cut removes.

### 4. `src/framenest/adapters/api/web/app.js` — the user-visible prose

Orchestrator located these prose sites, excluding identifier names and the header
literal: lines **1625, 1874, 1993, 5175, 6794, 8274**. Worker session `14` also
listed 11965 and 12595; re-derive and report whether those are display text,
identifier names, or something else. `8274` is the `Remove "…" from the FrameNest
catalog?` confirmation, which the Cooperator sees before a destructive action.

### 5. `src/framenest/application/media_content.py:88` — the download stem

```python
stem = f"framenest-media-{media_id.to_string()}"
```

Rename to `kronika-media-`. It is pinned by
`tests/unit/application/test_media_content_application.py:255` and
`tests/integration/test_local_web_media_playback.py:230`; repoint both, widening
each assertion. Change no other line of that module.

### 6. Test assertions that pin the retired display text

Orchestrator located **four**, and there may be more:

```text
tests/companion_review_extension.test.js:1127              /Connect FrameNest in Settings/
tests/companion_settings_automatic_analysis.test.js:508    /Could not reach FrameNest/
tests/x_companion_extension.test.js:581                    /Connect FrameNest in the side panel/
tests/x_companion_extension.test.js:1483                   /Connect FrameNest in Settings/
```

These are display assertions and must be repointed. They are distinct from the
header assertions, which must not be touched. Report any further display assertion
your assertion inventory finds.

Add one test extending the manifest-and-wordmark agreement guard so it also covers
the surfaces this cut changes: the same brand must appear in the manifest name, the
side-panel wordmark, the recovery copy, the origin label, and the connection status
and aria strings. It must fail on disagreement, not only on a hardcoded spelling.

## Authority

```text
Positive authority: edit exactly the files in scope 1 to 6 above, plus any
  additional file your two enumerations show must change, each reported explicitly;
  create one commit on local main; run the declared JavaScript route and the declared
  AP test operations; run read-only Git inspection.

Negative authority: any change to a mutation header spelling; any change to a global,
  DOM, CSS or port identifier in Excluded 2; any change to a Python class name in
  Excluded 3; any executable logic change; any change to
  src/framenest/adapters/api/web/companion_host.js; any change to the manifest
  `name`, `description`, `action.default_title` or `version`; any change to
  extension/ui/sidebar.html, which C2b already settled; any change to
  src/framenest/adapters/api/web/index.html; any change to
  framenest-media.bin, which C2b already retired; any ADR, docs/**, AGENTS.md, root
  Markdown file, pyproject.toml, ap.project.conf, deploy/**, scripts/**, .gitmodules
  or .gitignore; any of the 36 applied Alembic revision files; any new branch, push,
  tag, merge, rebase or history rewrite; any dependency install, update or lockfile
  change; any NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or capture-browser
  contact; any execution of a kronika-capture command; any reading of private/,
  personal Fish configuration, browser profiles, cookies, tokens, credential stores,
  .secrets or ~/.config/opencode; any write to /home/agile/meta.

Commands: JavaScript evidence goes only through `node --test tests/*.test.js` and
  focused `node --test <path>`. Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  09e45e54c8444281c147f9ba799e3602bb57d9aa --operation <id> -- <argv>`, plus
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline
  09e45e54c8444281c147f9ba799e3602bb57d9aa`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe
  files under /tmp only. Any other command must be stated in the report with its
  purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one commit on local main. No push, no new branch, no tag, no merge.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp.

Browser authority: none. Do not open Brave, do not load the extension, do not touch
  a real profile.
```

## Verification

1. Confirm branch `main`, HEAD `09e45e5…`, clean tree, submodule at the pin,
   `ap doctor` PASS, `ap project check --baseline` PASS. Stop without editing if any
   fails.
2. Produce both enumerations from **The C2b lesson** above and reconcile them.
   Report both counts and explain any difference before you edit.
3. Reproduce both baselines once. Expect `4359 passed, 8 skipped, 3 warnings` and
   `577 passed, 0 failed, 5 skipped`. The suite takes about eleven minutes; let it
   finish once. **Do not edit while a suite is running.**
4. Make the changes.
5. Show each repointed assertion failing when the new text is reverted, and show the
   extended agreement guard failing when any one surface disagrees.
6. Prove by enumeration that no user-visible occurrence of the retired brand remains
   on the surfaces in scope, and report the method.
7. Prove the three exclusion classes are byte-identical, by comparing the occurrence
   multiset of each excluded token at `09e45e5` against your working tree:
   the header literal, every `FrameNestCompanion*` / `FrameNestSidebarBridge` /
   `FrameNestReviewInbox` global, every `data-framenest-*` and `framenest-*` CSS and
   DOM hook, the `framenest-attach` port name, and every `FrameNestSettings` reference
   in tests. Report each total.
8. Run `node --test tests/*.test.js` and the full declared `test` operation once.
   Report exact counts for both.
9. Run the retention module. Files may leave `EXPECTED_FRAMENEST_CONTENT_PATHS`;
   report any movement with its cause and re-pin only what genuinely moved. Part A
   and Part B must not move.
10. Confirm `git diff --stat 09e45e5..HEAD` touches only reported paths.
11. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E1. Display-string substitutions with no logic, no contract and no
  remote effect, with the excluded classes proven byte-identical.
```

## Git

One commit on local `main`, parent `09e45e54c8444281c147f9ba799e3602bb57d9aa`.
Suggested subject:

```text
refactor(identity): retire the remaining user-visible companion prose
```

Do not push. Publication is a separate bounded grant.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if either baseline does not reproduce; if the two enumerations cannot be
  reconciled before editing; if any site turns out to be machine-read rather than
  display text; if any excluded token would have to change; if
  src/framenest/adapters/api/web/companion_host.js or sidebar.html would have to
  change; if Part A or Part B ledger pins would move; if any step would need a real
  browser profile; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded commit.

Completion: one commit, no user-visible retired brand on the in-scope surfaces, the
  download stem retired, every display assertion repointed and demonstrated failing
  on revert, all three exclusion classes proven byte-identical, the agreement guard
  extended and demonstrated failing, both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `15_report_00.md` in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC contact
  and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `15` and exchange `01` unchanged. Then:
both enumerations with their counts and the reconciliation; the exact diff of every
path; the before-and-after text of every renamed string; the outcome for the two
`app.js` sites Worker session `14` listed that the Orchestrator did not confirm;
every display assertion repointed with its revert demonstration; the extended
agreement guard with its failure demonstration; the three exclusion-class
byte-identity totals; baseline and final exact counts for both routes; every ledger
movement with its cause; the commit SHA; deviations, risks and missing evidence; and
one smallest next step.

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

- `docs/adr/0085-kronika-sole-identity.md` in full.
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/14_report_00.md`,
  sections 3, 11 and 12, which are your specification.
- `extension/shared/messages.js` around lines 600-700.
- `extension/ui/sidebar.js` around lines 60-80, 480-490, 660-680, 780-845 and 1095-1110.
- `extension/content/x_adapter.js` around lines 15-35 and 1760-1780.
- `extension/ui/save.html`, `extension/ui/save.js`, `extension/ui/picker.html`,
  `extension/ui/picker.js` at the listed sites.
- `src/framenest/adapters/api/web/app.js` at the listed prose sites.
- `src/framenest/application/media_content.py` around lines 45-95, including
  `safe_download_filename`.
- `tests/contract/test_kronika_identity_retention.py` in full.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the user-visible rename is coherent and the Orchestrator will say so
explicitly. What remains under the old brand after this cut is only the CSS and DOM
hooks, the `framenest-attach` port name, the retired storage keys and alarm names,
the header spelling, the Python class names, and the two cross-boundary protocol
strings — all scheduled at C3, C4 or C7. Publication of `main` and the routine NUC
refresh are each separate bounded grants, and the Cooperator's extension reload
must follow both.
# Authoritative Worker prompt — Worker session 14, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `14`, exchange `01`. Stored under the
Meta filename mapping as `14_implementation_00.md`, with report destination
`14_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 14
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C2B — retire every name a person actually sees
Reasoning recommendation: Low
Recommended context capacity: approximately 250k tokens
```

Rationale: a fully enumerated set of text and filename substitutions with no
logic, no contract and no judgement left to make. That is mechanical, localized
and trivially reversible, which is the `Low` band.

This is cut **C2b**. It is the Cooperator-facing naming cut that Worker session
`12` explicitly deferred, waiting for the Cooperator's wording choice. He has now
given it.

## Why this cut exists

ADR-0085 fixes one product identity. The engineering surfaces were migrated by
C1, C1b and C2. What remains visible to a person was not, because Worker session
`12` classified it as Cooperator-facing wording and refused to guess:

> "Manifest display name, description, action title, and
> `EXTENSION_CONTEXT_RECOVERY_COPY`. These are Cooperator-facing wording decisions,
> not engineering. They need his explicit choice, and the manifest `name` in
> particular appears in Brave's extension list and in the side-panel header. Do not
> fold them into a mechanical cut."

Orchestrator verification added two findings that were not in that list:

- **The side panel does not read the manifest name.** It hardcodes it in
  `extension/ui/sidebar.html`, so renaming the manifest alone would leave Brave
  saying Kronika while the side panel says FrameNest. This is exactly the one-sided
  rename that C2a was written to prevent, and it is the reason the two files must
  move together.
- **`src/framenest/adapters/api/web/index.html` still carries four user-visible
  occurrences of "FrameNest"** in prose the Cooperator reads, even though the page
  `<title>` is already `Kronika`.

## Goal

Every string and filename a person can see carries the Kronika identity, with no
one-sided rename anywhere.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: main
Expected HEAD: 9c71bfb0a06cb30c5d747816e9067f6a25350c58
Expected subject: fix(companion): dual-accept the web protocol so the rename cannot be one-sided
Remote origin: https://github.com/cisarik/kronika
Public main: 9c71bfb0a06cb30c5d747816e9067f6a25350c58
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

The local branch is now `main`, not the feature branch. Baseline at this commit,
measured by the Orchestrator: Python `4358 passed, 8 skipped, 3 warnings, 0 failed`;
JavaScript `581 total, 576 passed, 0 failed, 5 skipped`; retention module
`15 passed`.

Note: this is the first cut since C0 that changes the branch base to `main`. The
whole branch `feat/kronika-identity-dual-read` and `main` are the same commit, so
work here lands on `main` directly. Do not create a branch unless the gate fails.

## The exact rename set — complete, verified, nothing else

Re-verify every item before editing and report any occurrence this list missed.

### 1. `extension/manifest.json` — three fields

```text
line 3   "name": "FrameNest X Companion"          -> "Kronika X Companion"
line 5   "description": "Save eligible X posts to FrameNest and ..."
                                                  -> "... to Kronika and ..."
line 14  "action"."default_title": "FrameNest companion"
                                                  -> "Kronika companion"
```

Rewrite the description so it reads naturally with the new brand; do not merely
substitute the word if that leaves the sentence awkward. Change nothing else in the
manifest, **including the `version` field, which stays `0.2.0`.** That is
deliberate: the display name itself becomes the Cooperator's verification that a
reload took effect, so a second version bump would be redundant churn.

### 2. `extension/ui/sidebar.html` — five occurrences

```text
line 5   <title>FrameNest</title>
line 20  <span class="title-bar__wordmark">FrameNest</span>
line 53  <label for="origin">FrameNest origin</label>
line 59  "Origin is the FrameNest tailnet URL (https://<node>.<tailnet>.ts.net)."
line 86  <iframe id="frame" title="FrameNest" hidden></iframe>
```

Keep every element, id, class and attribute byte-identical. Change only the
human-readable text. `extension/ui/sidebar.css:96` styles `.title-bar__wordmark`
by class with `margin-right: auto`, `font-size`, `font-weight` and
`letter-spacing`, none of which depends on the text, so no style change is needed
or authorised. Confirm that by reading the rule rather than assuming it.

### 3. `extension/shared/messages.js` — one constant

```text
line 19-20  EXTENSION_CONTEXT_RECOVERY_COPY =
            "FrameNest was reloaded. Refresh X and reopen the side panel."
```

Change the brand word only. Keep the export, the constant name and the message
shape.

### 4. `framenest-media.bin` → `kronika-media.bin` — seven sites, all of them

```text
src/framenest/adapters/api/media_content_api.py:45   _FALLBACK_DOWNLOAD_FILENAME
src/framenest/application/media_content.py:52         download_filename default
extension/ui/sidebar.js:898
extension/ui/picker.js:254
extension/content/x_adapter.js:2097
extension/background/service_worker.js:975
extension/background/service_worker.js:1040
```

Both sides must change together. The server sends its filename through
`Content-Disposition`, so the extension copies are fallbacks used only when the
header is unusable; changing one side alone would make the two disagree. Verify
there is no eighth site, including any fixture, and report it.

### 5. `src/framenest/adapters/api/web/index.html` — four prose strings

```text
line 213  "... FrameNest will use the local server to inspect and acquire ..."
line 229  "Only the confirmed claim is sent to the local FrameNest server. ..."
line 282  "Only the confirmed request is sent to the local FrameNest server."
line 321  "Only the validated post is sent to the local FrameNest server."
```

Rewrite so each reads naturally with the new brand. Change no element, id, class
or attribute.

## The invariant to pin

Add one focused test asserting that the **manifest display name and the side-panel
wordmark carry the same brand**, so a future one-sided rename fails rather than
silently splitting the product's name across two surfaces. That is the specific
defect this cut exists to prevent, and it is the only new test strictly required.

Repoint the existing pins that name the renamed strings, widening rather than
weakening each assertion. Orchestrator-measured pins:

| Test | What it pins |
|---|---|
| `tests/contract/test_media_content_api.py` | `framenest-media.bin` |
| `tests/x_companion_extension.test.js` | `framenest-media.bin`, `title-bar__wordmark`, `FrameNest origin` |
| `tests/companion_review_extension.test.js` | `title-bar__wordmark` |

No test pins the `index.html` prose, so item 5 needs no repoint. If you find one,
report it rather than guessing.

Show each repointed test failing when the new name is reverted, so it is evidence
rather than decoration.

## Explicitly out of scope — do not touch

- **CSS and DOM hooks**: `data-framenest-*`, `framenest-composer*`,
  `framenest-companion*`, `framenest-save*`, `framenest-attach*`, `framenest-post*`,
  `framenestSaveKind`, `framenest-reload-notice`. These need paired style-rule
  edits and rendered acceptance. They belong to C7 with their own bounded cut.
- **The `framenest-attach` port name**, the storage keys, the alarm names, the
  internal protocol strings, and the companion API version. All are retired at C7.
- **`deploy/ubuntu/framenest-release`, `framenest_release.py` and
  `framenest_nuc_worker_gate.fish`.** These become `kronika-release`,
  `kronika_release.py` and `kronika_nuc_worker_gate.fish` at **C4**, with the old
  paths kept as working wrappers until C7. Do not touch them here.
- **Any package, import, console script, unit, host path, environment prefix or
  header change.** Those are C3, C5, C6 and C7.
- Any ADR, `docs/**`, `AGENTS.md`, root Markdown file, `pyproject.toml`,
  `ap.project.conf`, `.gitmodules`, `.gitignore`, or any of the 36 applied Alembic
  revision files.
- No change to `extension/shared/messages.js` beyond the one constant in item 3.
- No change to `extension/manifest.json` beyond the three fields in item 1.

## Authority

```text
Positive authority: edit exactly the seven files in the rename set above, plus the
  four test files listed in the pin table, plus any additional file your exhaustive
  re-verification shows must change, each reported explicitly; add the manifest-
  and-wordmark agreement test; create one commit on main; run the declared
  JavaScript route and the declared AP test operations; run read-only Git
  inspection.

Negative authority: anything in Explicitly out of scope above; any executable logic
  change; any new branch, push, tag, merge, rebase or history rewrite; any
  dependency install, update or lockfile change; any NUC contact, including SSH, the
  NUC worker gate, and deploy/ubuntu/framenest-release in every mode; any provider
  or capture-browser contact; any execution of a kronika-capture command; any
  reading of private/, personal Fish configuration, browser profiles, cookies,
  tokens, credential stores, .secrets or ~/.config/opencode; any write to
  /home/agile/meta.

Commands: JavaScript evidence goes only through `node --test tests/*.test.js` and
  focused `node --test <path>`. Python evidence goes only through
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  9c71bfb0a06cb30c5d747816e9067f6a25350c58 --operation <id> -- <argv>`, plus
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline
  9c71bfb0a06cb30c5d747816e9067f6a25350c58`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe
  files under /tmp only. Any other command must be stated in the report with its
  purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one commit on main. No push, no new branch, no tag, no merge.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp.

Browser authority: none. Do not open Brave, do not load the extension, do not touch
  a real profile. The Cooperator performs and verifies the reload himself.
```

## Verification

1. Confirm branch `main`, HEAD `9c71bfb…`, clean tree, submodule at the pin,
   `ap doctor` PASS, `ap project check --baseline` PASS. Stop without editing if any
   fails.
2. Re-verify every item in the rename set and report any occurrence the Orchestrator's
   list missed, classified as in-scope or deferred.
3. Reproduce both baselines once. Expect `4358 passed, 8 skipped, 3 warnings` and
   `576 passed, 0 failed, 5 skipped`. The suite takes about eleven minutes; let it
   finish once. **Do not edit while a suite is running.**
4. Make the changes.
5. Show each repointed test failing when the new name is reverted, and show the new
   agreement test failing when the manifest and the wordmark disagree.
6. Prove by enumeration that **no user-visible occurrence of the old brand remains**
   in: the manifest's `name`, `description` and `action.default_title`; every
   human-readable string in `sidebar.html`; the recovery copy; and the four prose
   strings in `index.html`. Report the enumeration method, not just the conclusion.
7. Confirm the out-of-scope CSS and DOM hooks are byte-identical, by comparing the
   occurrence multiset of each token at `9c71bfb` against your working tree, the
   same way Worker session `12` did.
8. Run `node --test tests/*.test.js` and the full declared `test` operation once.
   Report exact counts for both.
9. Run the retention module. Files may now **leave** `EXPECTED_FRAMENEST_CONTENT_PATHS`
   if the renamed string was a file's only occurrence. Report any movement with its
   cause and re-pin only what genuinely moved. Part A and Part B must not move.
10. Confirm `git diff --stat 9c71bfb..HEAD` touches only reported paths.
11. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E1. Text and filename substitutions with no logic change, no
  contract change, no remote effect, and strong focused verification.
```

## Git

One commit on `main`, parent `9c71bfb0a06cb30c5d747816e9067f6a25350c58`. Suggested
subject:

```text
refactor(identity): retire the names a person actually sees
```

Do not push. Publication is a separate bounded grant.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if either baseline does not reproduce; if any item of the rename set turns
  out to be load-bearing in a way that is not visible from the repository, such as a
  name being parsed rather than displayed; if making the manifest and the wordmark
  agree would require touching a CSS or DOM hook; if any out-of-scope identifier
  would have to change; if Part A or Part B ledger pins would move; if any step
  would need a real browser profile; if context pressure reaches the point where a
  bounded rotation is cheaper than a degraded commit.

Completion: one commit, every enumerated name retired, no user-visible old brand
  left on those surfaces, the manifest and the wordmark agreeing under a test shown
  failing on disagreement, every repointed pin demonstrated failing on revert,
  out-of-scope hooks byte-identical, both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as `14_report_00.md`
  in /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

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
echoing `kronika-sole-identity`, session `14` and exchange `01` unchanged. Then:
the re-verified rename set with any occurrence the list missed; the exact diff of
every path; the before-and-after text of every renamed string; the user-visible
enumeration from step 6 with its method; the out-of-scope byte-identity
confirmations; each repointed test with its revert demonstration; the new agreement
test with its failure demonstration; every ledger movement with its cause; baseline
and final exact counts for both routes; the commit SHA; deviations, risks and
missing evidence; and one smallest next step.

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
- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/12_report_00.md`,
  sections 3.5 and 11, which is the deferral this cut discharges.
- `extension/manifest.json`, `extension/ui/sidebar.html`, `extension/ui/sidebar.css`
  around line 96, `extension/shared/messages.js` around lines 15-25.
- `src/framenest/adapters/api/web/index.html` around lines 210-325.
- `src/framenest/application/media_content.py` around line 52 and
  `src/framenest/adapters/api/media_content_api.py` around line 45.
- The four pinned test files, so you widen assertions rather than weaken them.
- `tests/contract/test_kronika_identity_retention.py` in full, for the ledger rules.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the enumeration, the agreement test and the
out-of-scope byte-identity. **This cut changes Python product code and a served
asset, so it needs its own routine NUC refresh and a publication grant before the
Cooperator sees it.** The extension reload then becomes verifiable twice over: the
display name and the manifest version. The user's remaining script-name questions
are already scheduled at C4 and C7 and are answered there, not here.
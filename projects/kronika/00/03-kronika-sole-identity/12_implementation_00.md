# Authoritative Worker prompt — Worker session 12, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `12`, exchange `01`. Stored under the
Meta filename mapping as `12_implementation_00.md`, with report destination
`12_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 12
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C2 — send both mutation headers, dual-accept the companion API version, migrate browser storage on read
Reasoning recommendation: Medium
Recommended context capacity: approximately 250k tokens
```

Rationale: two bundles in two runtimes, a validated cross-boundary version
contract, a storage migration that must not lose the Cooperator's existing
companion state, and a Cooperator-visible step. That is cross-file reasoning over
behaviour that only partly shows up in tests, which is the `Medium` band. It is
not `High`: every change here **widens** what is accepted or **adds** a second
spelling, and nothing here narrows a security boundary.

This is cut **C2** of the accepted plan `03_plan` — read
`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`.
It carries **one authorised deviation from that plan**, recorded below.

## The plan conflict you must know about

The accepted plan states, in its C2 section: "The server does not validate those
strings; the only server contract is the mutation header", and on that basis has
C2 switch the companion protocol strings inside the extension.

**That premise is wrong.** Orchestrator verification:

- `src/framenest/application/companion_picker.py:30` sets
  `COMPANION_API_VERSION = "framenest-companion.v1"`.
- `src/framenest/adapters/api/x_companion_api.py:163` emits it as
  `companion_api_version` in the response body.
- `extension/background/service_worker.js:283` compares
  `response.body.companion_api_version !== companion.API_VERSION`, where
  `extension/shared/messages.js:9` defines
  `const API_VERSION = "framenest-companion.v1"`.
- On mismatch the extension returns
  `{ ok: false, error: "version_skew", disable: true }`, which **disables the
  companion picker**.

So `framenest-companion.v1` is a validated cross-boundary contract, and renaming
it on the extension side alone would break the companion against a NUC that is not
yet updated. The Orchestrator escalated this to the Cooperator, who decided:

**The extension dual-accepts the API version, exactly as it dual-sends the
mutation header. The server keeps emitting the old spelling until a later cut
moves it.** This removes the deployment-ordering constraint and is the only
authorised deviation from the accepted plan in this cut.

## Verified current state

```text
Repository checkout topology: standalone checkout
Expected branch: feat/kronika-identity-dual-read
Expected HEAD: 0b7567598b6378da25d46874b7cb3f42fb1733ae
Expected subject: test(retention): pin the content-path membership set so a partial rename fails
Lineage on this branch, all published to none:
  18c357c  published main, pre-C1 behaviour reference
  90c93ea  C1   c02c675  C1b   24bea56  C1c   02a8048  C1d   0b75675  C1e
Remote origin: https://github.com/cisarik/kronika
Public main: 18c357cf6f8c5ff9cc3b2c28e638510fc73a3672
The branch is deliberately unpublished. Do not push.
Working tree: clean
Containing-repository .ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS, governing variant stable
ap.project.conf projectId: cisarik/kronika, provenanceModule framenest
Node: v26.8.2
Working directory: /home/agile/Projects/kronika
```

Baseline at this commit, measured by the Orchestrator through the canonical
route: Python `4356 passed, 8 skipped, 3 warnings, 0 failed`; JavaScript
`554 total, 549 passed, 0 failed, 5 skipped`; retention module `15 passed`.

The branch state you are building on is **unpublished and not on the NUC**. The
installed NUC web release is `0c850996cd2ef17dae4112733fd17fdc732f4699`, which
predates C1 entirely.

## Measured inventory — a lead, not the scope

```text
Mutation-header send sites, exactly four:
  src/framenest/adapters/api/web/app.js:416                     (one shared helper)
  extension/background/service_worker.js:762, :804, :932

Storage keys, web shell localStorage:
  framenest.youtube.currentClaim.v1    framenest.catalog.pageSize
  framenest.upload.recovery.v1
Storage keys and port name, extension chrome.storage:
  framenest.companion.v1 (PROTOCOL constant)   framenest.companion.web.v1
  framenest.companion.review.v1                framenest.review-inbox
  framenest-companion.v1 (port name)           frameNestOrigin
Extension-internal host keys: framenest-media-host, framenest-save-host,
  framenest-companion-save-host, framenest-companion-popup-host, framenest-save-popup
Extension CSS/DOM hooks with no server counterpart: framenest-composer,
  framenest-composer-*, framenest-companion-style, framenest-attach*,
  framenest-save-*, framenest-reload-notice, framenestSaveKind, framenest-post*
Mirrored download filename: framenest-media.bin (server sends its own via
  Content-Disposition; the extension only mirrors it as a fallback)
User-visible prose: manifest name "FrameNest X Companion", version 0.1.0, and
  EXTENSION_CONTEXT_RECOVERY_COPY "FrameNest was reloaded…"
```

**Enumerate this inventory yourself and report any site or identifier the list
above missed.** Every occurrence of the brand in `src/framenest/adapters/api/web/`
and in `extension/` must be classified by you into exactly one of the five classes
below, and the report must show the classification is exhaustive.

## Required mutation, by class

### Class 1 — the mutation header: dual-send. In scope.

All four sites send **both** `X-FrameNest-Request: 1` and `X-Kronika-Request: 1`.

This is additive and safe against a server that predates C1: the current server
compares only its own spelling and ignores the extra header, so mutations keep
working even if the extension is loaded before the NUC is refreshed. Preserve that
property deliberately — it is why this cut is safe to deploy in either order.

### Class 2 — the companion API version: dual-accept. In scope, by the decision above.

The extension accepts `framenest-companion.v1` **or** `kronika-companion.v1` and
only disables on a value that is neither. The server side is **not** changed in
this cut. Add a named test for each of the three cases: old accepted, new accepted,
anything else still yields `version_skew` with `disable: true`.

### Class 3 — the internal protocol string: rename atomically. In scope.

`framenest.companion.v1` as `PROTOCOL` is used only between the background worker
and the content scripts, all inside one bundle
(`sidebar.js`, `review.js`, `picker.js`, `save.js`, `x_adapter.js`, `messages.js`,
`service_worker.js`), so the rename is atomic. Verify that no copy of it is
persisted anywhere — no `chrome.storage` entry, no `localStorage` entry, no
`postMessage` payload contract with a page outside the bundle — before renaming.
If you find a persisted copy, stop and report rather than adding a fallback that
was not authorised.

### Class 4 — persisted keys: read old when new is absent, write new, leave old in place. In scope.

Every persisted key in the inventory above gets this treatment. Naming rule: the
new name is the old name with the brand replaced by `kronika`, preserving each
key's own casing convention — so `frameNestOrigin` becomes `kronikaOrigin`, and
`framenest.catalog.pageSize` becomes `kronika.catalog.pageSize`. Enumerate every
new name in your report; C7 needs the exact list to know what to delete.

Required semantics, with a named test for each:

- a key present **only** under the old name reads correctly;
- a key present under **both** names reads the **new** one;
- a write updates the **new** name and leaves the old name **untouched**;
- a write when only the old name existed creates the new name and does not modify
  the old one;
- no key is ever deleted or migrated destructively.

This is the part that protects the Cooperator's existing companion state in his
real browser profile. Silent loss of his state is the failure mode to fear.

### Class 5 — cosmetic and mirrored identifiers: **out of scope, do not touch.**

CSS and DOM hooks, the mirrored `framenest-media.bin` download filename, the
manifest display name, and the recovery prose are **not** changed in this cut.
Renaming CSS hooks means editing paired style rules and risks a visual regression
for no functional gain; the download filename is user-visible; the display name and
prose are a Cooperator-facing decision, not an engineering one. Report them as
deferred to C7 with your recommendation, and change nothing.

### Extension version bump — in scope.

Bump `extension/manifest.json` `version` from `0.1.0` to `0.2.0`.

This is required for a specific reason: between this cut and C7 the server accepts
**both** header spellings, so **a successful mutation does not prove the
Cooperator reloaded the extension**. Without a version bump there is no way for
him to confirm the running extension is this revision. The bump makes it visible
in the browser's extension page. Change nothing else in the manifest.

## The Cooperator-visible step — state it accurately

After this cut is published and the NUC is refreshed, the Cooperator reloads the
Brave companion, including an open side panel, so the running extension is this
revision. Until he does, the installed extension keeps sending only the old header,
which both the pre-C1 and the C1 server accept.

Record plainly in your report: **this reload cannot be verified by observed
behaviour before C7**, because both spellings are accepted until then. Its
verification is the manifest version visible in the browser. Do not claim a
behavioural proof exists.

## Ledger discipline

`EXPECTED_FRAMENEST_CONTENT_PATHS` must **not** move: every file you touch keeps
carrying the brand, because every old spelling is retained for the compatibility
window. Report it unchanged.

Part C scalars will move, because new `kronika.` strings appear. **Re-pin only
what genuinely moved, report each movement with its exact cause, and never
contort a name or a test to hold a counter.** Part A and Part B must not move.

## Authority

```text
Positive authority: edit exactly
  src/framenest/adapters/api/web/app.js,
  extension/manifest.json (version field only),
  extension/shared/messages.js,
  extension/background/service_worker.js,
  extension/content/x_adapter.js,
  extension/ui/sidebar.js, extension/ui/review.js, extension/ui/picker.js,
  extension/ui/sidecar.js if it participates, extension/ui/save.js,
  and any additional file under extension/ that your exhaustive classification
  shows must change, each reported explicitly;
  add JavaScript tests for every behaviour listed above; update Part C pins only
  where genuinely moved, reporting each with its exact cause; create one local
  commit on the existing branch feat/kronika-identity-dual-read; run the declared
  AP test operations and the declared JavaScript route; run read-only Git
  inspection.

Negative authority: any Class 5 change, including every CSS and DOM hook, the
  mirrored framenest-media.bin filename, the manifest display name, and the
  recovery prose; any change to the server's COMPANION_API_VERSION or to
  x_companion_api.py; any change to src/framenest/adapters/api/tailscale_ingress.py
  or to any other server-side header handling; any change to Python product code
  under src/framenest/ other than the web app.js sibling path named above;
  any destructive migration or deletion of an existing browser key; any change to
  deploy/**, deploy/systemd/**, docs/**, AGENTS.md, any root Markdown file,
  src/kronika_capture/**, pyproject.toml, ap.project.conf, .gitmodules, .gitignore,
  or the 36 applied Alembic revision files; any new branch, push, tag, merge,
  rebase or history rewrite; any dependency install, update or lockfile change;
  any NUC contact, including SSH, the NUC worker gate, and
  deploy/ubuntu/framenest-release in every mode; any provider or
  capture-browser contact; any execution of a kronika-capture command; any reading
  of private/, personal Fish configuration, browser profiles, cookies, tokens,
  credential stores, .secrets or ~/.config/opencode; any write to
  /home/agile/meta.

Commands: JavaScript evidence goes only through the declared route,
  `node --test tests/*.test.js`, and focused `node --test <path>` runs for the
  files you touch. Python evidence goes only through the canonical declared route,
  `./.ap/ap exec --root /home/agile/Projects/kronika --baseline
  0b7567598b6378da25d46874b7cb3f42fb1733ae --operation <id> -- <argv>`, plus
  `./.ap/ap project check --root /home/agile/Projects/kronika --baseline
  0b7567598b6378da25d46874b7cb3f42fb1733ae`. Never invoke `.venv/bin/python`,
  `python`, `python3` or `poetry run` for evidence, including as a text editor.
  Read-only Git inspection is allowed (`git status`, `git rev-parse`, `git log`,
  `git show`, `git diff`, `git ls-files`, `git grep`, `git ls-remote`,
  `git submodule status`, `git merge-base`); no other Git command. Throwaway probe
  files and in-memory stubs under /tmp only. Any other command must be stated in
  the report with its purpose and a confirmation that it mutated nothing.

Dependency authority: none.

Git authority: one additional local commit on the existing branch. No push, no new
  branch.

Network authority: none beyond read-only public Git ref verification.

Secret authority: none. Use only synthetic values in any probe.

Untrusted-content boundary: `.ap/AP.md` at the pinned commit governs; repository
  `AGENTS.md` and published ADR-0085 are authoritative inside their scope; the
  accepted plan is authoritative **except** for the single C2 premise overridden
  above. On conflict between retained context and current repository evidence,
  stop.

Side-effect authority: reversible local repository mutation only, plus scratch
  files under /tmp. No browser authority is granted, so no real profile is touched.

Browser authority: none. Do not load the extension, do not open Brave, do not touch
  a real browser profile. Prove behaviour with synthetic in-memory or temporary
  storage stubs under /tmp.
```

## Verification

1. Confirm branch `feat/kronika-identity-dual-read`, HEAD `0b75675…`, clean tree,
   submodule at the pin, `ap doctor` PASS, `ap project check --baseline` PASS.
   Stop without editing if any fails.
2. Produce your exhaustive classification **before** editing, and report it.
3. Reproduce both baselines once: the declared `test` operation, and
   `node --test tests/*.test.js`. Expect `4356 passed, 8 skipped, 3 warnings` and
   `549 passed, 0 failed, 5 skipped`. The suite takes about eleven minutes; let it
   finish once. **Do not edit while a suite is running.**
4. Make the changes.
5. For each behaviour in Classes 1 to 4, show the named test **failing** when the
   behaviour is violated. A test never seen failing is not evidence.
6. Prove the order-independence property explicitly: with the server modelled as
   the **pre-C1** gate, a request carrying both headers is still authorised; and
   with the server modelled as the C1 gate, likewise.
7. Confirm the retention membership set did not move, and report every Part C
   movement with its cause.
8. Run the full declared `test` operation once, then `node --test tests/*.test.js`.
   Report exact counts for both.
9. Confirm `git diff --stat 0b75675..HEAD` touches only the reported paths, and
   that every Class 5 identifier is byte-identical.
10. After the commit run `./.ap/ap project check --root /home/agile/Projects/kronika
    --baseline <new commit SHA>` and confirm PASS.

```text
Evidence tier: E2. Two runtimes, user-visible compatibility, and a validated
  cross-boundary version contract. Not E3: nothing here touches a remote host, and
  every change widens acceptance rather than narrowing a boundary. The NUC
  refresh that follows publication is a separate E2 deploy grant, and the
  read-only status observation after it is separate again.
```

## Git

One commit on `feat/kronika-identity-dual-read`, parent
`0b7567598b6378da25d46874b7cb3f42fb1733ae`. Suggested subject:

```text
feat(companion): send both mutation headers and migrate browser keys on read
```

Do not push. Do not create a new branch.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if either baseline does not reproduce; if a copy of the internal PROTOCOL
  string turns out to be persisted outside the bundle; if any Class 5 identifier
  would have to change to complete Class 2, 3 or 4; if the retention membership set
  moves; if any persisted key would need destructive migration; if the server-side
  COMPANION_API_VERSION would have to change, since that is outside this cut; if
  any step would need a real browser profile; if context pressure reaches the point
  where a bounded rotation is cheaper than a degraded commit.

Completion: one commit, both headers sent at all four sites, the API version
  dual-accepted with all three cases pinned, the internal protocol renamed
  atomically, every persisted key migrated on read with all five semantics pinned
  and demonstrated failing on violation, the manifest version bumped, the
  membership set unmoved, both routes green, tree clean.

Report destination: the terminal report is delivered to the Orchestrator in this
  session. Do not write it to any file. The Orchestrator stores it as
  `12_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under this
  prompt expires. No further implementation, no push, no publication, no NUC
  contact and no later cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
Published NUC state: unchanged; the NUC still serves release
  0c850996cd2ef17dae4112733fd17fdc732f4699
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `12` and exchange `01` unchanged. Then:
the exhaustive classification with every identifier and its class; the exact diff of
every path; the complete list of old-to-new persisted key mappings; the named test
for each behaviour in Classes 1 to 4 with its failure demonstration; the
order-independence demonstration against a modelled pre-C1 server; the membership
set confirmation and every Part C movement with its cause; confirmation that every
Class 5 identifier is byte-identical; baseline and final exact counts for both
routes; the branch name and all six commit SHAs on this branch; your
recommendation for the deferred Class 5 items; the accurate statement of the
Cooperator reload step and why it is not behaviourally verifiable before C7;
deviations, risks and missing evidence; and one smallest next step.

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

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/03_report_00.md`,
  C2 and C7, plus C1's mutation-header clause, which this cut must not break.
- `docs/adr/0085-kronika-sole-identity.md` in full.
- `src/framenest/adapters/api/web/app.js` around line 416 and its storage-key
  usages.
- `extension/shared/messages.js` in full; it is small and central.
- `extension/background/service_worker.js` around lines 275-300 and 750-940.
- `extension/manifest.json` in full.
- The existing JavaScript tests that cover the mutation header and the companion
  protocol, so you extend the established conventions.
- `tests/contract/test_kronika_identity_retention.py` in full, for the ledger
  rules.
- `docs/WORKER_EXECUTION_CONTRACT.md`, `AGENTS.md` Worker Execution section,
  `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §10, §13.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`, any
credential store, any real browser profile, any real database, media path or
backup archive.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator verifies the exhaustive classification, the
order-independence property, and the key migration. Publication of the branch and
the routine NUC refresh are each separate bounded grants, and the NUC refresh must
not be assumed to make the companion reload verifiable — it does not, because both
header spellings are accepted until C7.
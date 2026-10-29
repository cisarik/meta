# Authoritative Worker prompt — Worker session 46, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `46`, exchange `01`. Stored under the
Meta filename mapping as `46_implementation_00.md`, with report destination
`46_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 46
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7AC — canonical companion emissions and stored-state completion
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the companion half of the split C7-A transition,
after the server half is published and served: the extension begins emitting
the canonical web protocol and the canonical mutation header, every remaining
operational JavaScript identifier in the companion surfaces (extension plus
the served companion web host) moves to its canonical spelling together with
its coupled DOM/style and stored-state migration, and the retired duplicate
alarm is cleared. A missed coupling silently breaks meme attach, the save
popup, the side-panel history or a returning user's stored origin, so every
move needs its agreement proof.

This is work item **C7-A/C** from the accepted closure plan at
`25_report_00.md` section 2.12.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
section 2.12 is your specification; section 2.13 (C7-B) delimits what stays
untouched — every retired reader stays until that cut. Read both in full.
Required outcomes:

1. **Web protocol emission.** In `extension/ui/sidebar.js` every outbound web
   message carries `kronika.companion.web.v1`. The receive side keeps accepting
   both spellings for un-refreshed servers; the contract comment is rewritten
   to the new truth (the extension emits canonical, still accepts retired,
   readers are removed in the removal cut). Handshake, attach, hosted details
   and recovery behavior are otherwise unchanged.
2. **Ports, messages and the internal API version.** Rename every remaining
   retired internal token — the `framenest-attach` port name, the
   `framenest-save-popup` and `framenest-save-host` sources, and every further
   retired `framenest-*` string token your parse finds (the DOM attribute
   family is outcome 5). The already-canonical internal protocol
   (`kronika.companion.v1`) stays. The companion API-version reader keeps
   accepting both spellings; its now-stale comment around
   `extension/shared/messages.js:9–11` ("the server keeps emitting the retired
   spelling until a later cut moves `COMPANION_API_VERSION`") is corrected —
   the server now emits `kronika-companion.v1`.
3. **Mutation header emission.** The extension's mutation request headers
   become exactly `{"X-Kronika-Request": "1"}`. No request emits
   `X-FrameNest-Request` any more. No server-side file changes: the server
   keeps accepting both spellings until the removal cut, and no other header
   changes.
4. **JavaScript globals, moved together.** Rename the extension's operational
   globals to canonical spellings — `FrameNestCompanion` → `KronikaCompanion`,
   `FrameNestSidebarBridge` → `KronikaSidebarBridge`, `FrameNestReviewInbox` →
   `KronikaReviewInbox`, `FrameNestReviewOverlay` → `KronikaReviewOverlay`,
   `FrameNestXAdapterContractV1` → `KronikaXAdapterContractV1`,
   `FrameNestXAdapterTestHooks` → `KronikaXAdapterTestHooks` — and the origin
   helpers `canonicalizeFrameNestOrigin` / `acceptFrameNestOrigin` to canonical
   names (follow the repository's established rename convention and state your
   choice). Also rename the served web side of the companion coupling:
   `FrameNestCompanionWeb` → `KronikaCompanionWeb` in
   `src/kronika/adapters/api/web/companion_host.js`, every consumer in
   `src/kronika/adapters/api/web/app.js`, and every test or mock that names
   it; definition and consumers ship in one release, so no alias is required —
   confirm by whole-tree parse that nothing outside the served release
   references it. Every reference, export, test and mock moves in the same
   commit; no reader of a moved global may be left behind.
5. **Coupled DOM/class/style identifiers.** Move the extension's
   `data-framenest-*` attribute family to `data-kronika-*`: every attribute,
   selector, inline style and test reference, so definitions, selectors and
   styles agree exactly and no `data-framenest-*` remains outside deliberately
   retained readers (there are none for these attributes; prove it with
   before/after whole-tree counts). Any brand-bearing class or style identifier
   your parse finds moves with the same agreement proof.
6. **Stored-state completion.** Keep every retired fallback read. Complete the
   migration: when a reader finds only the retired value, write the canonical
   value, verify it by reading it back, and only then remove the obsolete
   value; when the canonical value is already present, remove the obsolete
   duplicate after the same verification. Cover old-only, canonical-only,
   both-same, both-conflicting (canonical wins; the retired value never
   resurrects), neither, reset (a reset must not resurrect a removed retired
   value), and interrupted recovery. Derive the complete set of
   application-owned browser keys with retired counterparts (today the origin
   key and the alarm are the known pairs) and state the result. Preserve origin
   selection, review state and in-flight recovery; do not touch unrelated
   storage.
7. **Retired duplicate alarm.** When the companion is configured, ensure the
   canonical alarm `kronika.review-inbox` exists and clear the retired
   duplicate `framenest.review-inbox` once; clearing is idempotent, does not
   disturb the canonical alarm or the badge, and the alarm listener keeps
   accepting both names until the removal cut. The disconnect/reset path keeps
   clearing both as today.
8. **Behavior freeze.** Everything else is unchanged: review-inbox polling and
   badge, save popup flow, picker, attach, recovery copy and semantics, origin
   acceptance and pinning, UUID checks. Do not edit Python product files,
   server protocol or acceptance code, documents or dependencies. The only
   non-extension product edits are the companion web host global and its
   references from outcome 4.

## Anchors, as locators, not an inventory

- `extension/shared/messages.js` — `PROTOCOL`, `API_VERSION` family, `STORAGE`,
  `REVIEW_INBOX` alarm names, `TYPES`, origin helpers, exports, the root
  global.
- `extension/background/service_worker.js` — mutation headers, port name,
  alarm creation/clearing, origin storage read/write, `FrameNestCompanion`
  global.
- `extension/ui/sidebar.js` — protocol constants and send sites, the comment,
  bridge/inbox globals.
- `extension/ui/save.js`, `extension/ui/picker.js`, `extension/ui/review.js` —
  sources, protocol reads, globals.
- `extension/content/x_adapter.js`,
  `extension/content/x_adapter_contract_v1.js` — the `data-framenest-*`
  family, selector contract, test hooks, contract global.
- `src/kronika/adapters/api/web/companion_host.js`,
  `src/kronika/adapters/api/web/app.js` — the `FrameNestCompanionWeb` global
  and its consumers.
- Tests: `tests/companion_web_bridge.test.js`,
  `tests/companion_review_extension.test.js`,
  `tests/x_companion_extension.test.js`,
  `tests/companion_settings_automatic_analysis.test.js`,
  `tests/kronika_ui.test.js`, `tests/catalog_card_ai_quick_action.test.js`,
  `tests/contract/test_local_web_application.py`, and any further module your
  parse finds.
- `tests/contract/test_kronika_identity_retention.py` — the Part C scalars and
  the running cause comments.

## Verified starting state, measured by the Orchestrator on 2026-10-12

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209
Public main:                  c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4955 passed, 8 skipped, 3 warnings, 0 failed
Focused Python (local web + public published): 225 passed
Retention module:             15 passed
JS baselines: companion_web_bridge 27; companion_review_extension 40;
              x_companion_extension 53; companion_settings_automatic_analysis 6;
              kronika_ui 12; catalog_card_ai_quick_action 30;
              bounded non-browser glob (*_frontend, *_cockpit, gallery_*) 213
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. Repository-only work: no NUC contact, no browser, no real X.

## Authority

```text
Positive authority: edit `extension/**` for exactly the emissions, identifier
  moves, storage and alarm completion of outcomes 1–8; edit
  `src/kronika/adapters/api/web/companion_host.js` and
  `src/kronika/adapters/api/web/app.js` for exactly the companion web-host
  global rename and its references; edit the test modules named above and any
  further test module your parse shows directly referencing a moved identifier,
  naming it in the report before editing it; edit
  `tests/contract/test_kronika_identity_retention.py` only to re-pin a Part C
  scalar that your own measurement shows this cut moved, with the per-tree
  arithmetic cause stated; create exactly one local non-amended commit on
  `main`.

Negative authority: every other path; any Python product file; any server
  protocol, header-acceptance or settings file; any removal of a retired
  reader (that is the removal cut); any document; any dependency or lockfile
  change; any change to `pyproject.toml`, `ap.project.conf` or the `.ap`
  gitlink; any frozen document or Alembic revision; publication; push; force;
  amend; branch; stash; any NUC contact or SSH; any migration or deployment;
  any provider, browser or capture contact; any profile or storage inspection
  outside synthetic fixtures. If a necessary change falls outside the positive
  scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline c152a178dcfbbe6e8f04f98d1b9f3f8cb7aea209 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`, including as a text
  editor. JavaScript evidence uses only the documented ordinary invocation
  from the worktree root: `node --test tests/<name>.test.js`. Do not activate
  browser-evidence suites; update a browser-evidence file only when a moved
  identifier requires it, naming it in the report. Read-only Git inspection
  allowed; exactly one `git add <exact paths>` and one `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only.
Browser authority: none. Synthetic fixtures only; no extension reload.
```

## Verification

1. **Baseline reproduction before editing.** Show the current retired state
   behaviorally: a captured extension outbound web message carries
   `framenest.companion.web.v1`; a captured mutation request carries both
   headers; the DOM attribute family, the internal tokens and the globals are
   the retired spellings; the retired alarm exists once the extension is
   configured. The new expectations fail against the unmodified tree; report
   each observed failure. Remove any temporary probe material before the
   commit.
2. **Emission and reader matrix.** Post-fix: every outbound web message is
   canonical and the receive side still accepts retired, canonical and refuses
   unknown; every mutation request carries exactly one canonical header;
   unknown-version refusals unchanged; whole-tree before/after tables for every
   retired token, each remaining occurrence classified as a deliberately
   retained reader naming the removal cut, a frozen/out-of-scope artifact, or a
   reported finding.
3. **DOM/style agreement.** Parse the attribute family, its selectors, its
   inline styles and its tests; prove exact agreement and zero
   `data-framenest-*` outside retained readers.
4. **Stored-state and alarm matrix.** Old-only, canonical-only, both-same,
   both-conflicting, neither, reset-without-resurrection, interrupted
   recovery; migration writes canonical, verifies, then removes; the retired
   alarm is cleared exactly once, idempotently, without disturbing the
   canonical alarm or badge; listeners keep accepting both alarm names.
5. **Mutation demonstrations**, each named with its observed failure: revert
   the web-protocol emission → the protocol emission test fails; re-add the
   retired mutation header → the header test fails; skip the verify-then-remove
   in a storage path → the removal test fails; skip the retired-alarm clear →
   the alarm test fails; rename a DOM attribute in the adapter but not in its
   selector → the agreement test fails. Derive your own if you can prove the
   same matrix.
6. Run, through the declared routes: the six named JS suites, then the
   documented bounded non-browser JS glob, then the focused Python modules, the
   full declared Python suite and the retention module. Report every count,
   elapsed time and any difference from the baselines in the starting-state
   block.
7. Report every moved or removed site that no test exercises, and every
   consumer of a moved identifier your derivation found that this prompt did
   not name.
8. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and per-tree
   cause for every Part C movement.

## Derivation and defect-pattern discipline

```text
 1. Derive site lists by PARSING each artefact. This prompt's anchors are
    locators, not an inventory.
 2. Resolve every cited line to its literal text BEFORE classifying it.
 3. A literal in a test fixture is NOT a pin. Require assertion context.
 4. Verify each occurrence and each caller independently.
 5. Reject a guard that can pass vacuously when its input is absent.
 6. Never truncate an inventory. If output is truncated, disclose it.
 7. Check every mechanical probe against a known-impossible result.
 8. Regenerate every verification table at report time; never transcribe one.
 9. Open and classify every grep hit.
10. State when a requested demonstration cannot exist. Do not fabricate one.
```

**Collapsing pairs.** Emission and acceptance must not collapse: a canonical
emission must never reappear as retired, a retired reader must never be
removed early, and an unknown value must never become accepted. The
storage migration must not collapse "verified-and-removed" with
"removed-without-verification", and the DOM rename must not collapse an
attribute with its selector.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a change would remove a retired reader, edit Python product code,
  or touch a document (those belong to later cuts); if a frozen hash, Part A or
  Part B moves; if a Part C re-pin cannot be reproduced from your own
  measurement; if a move would require inspecting a real profile, storage or
  page; if context pressure reaches the point where a bounded rotation is
  cheaper than a degraded result.

Completion: canonical companion emissions with every retired reader retained;
all operational identifiers of both companion surfaces moved together with
their DOM/style agreement; storage migration completed with verification and
retired-alarm clearing; the full matrix with mutation demonstrations; all
named suites, the bounded JS glob, focused Python, full Python and retention
green through the declared routes; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `46_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no refresh, no extension reload, no host contact and no later
  cut is authorized by it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `46` and exchange `01` unchanged. Then:

1. The emission/reader before-and-after tables for every retired token, with
   the retained readers named and their removal cut stated.
2. The DOM/style agreement proof and the whole-tree attribute counts.
3. The storage and alarm matrix results.
4. The mutation demonstrations, each with its named mutation.
5. JS, focused Python, full-suite and retention counts with elapsed time and
   any baseline difference.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and
   Part C movement with per-tree cause.
7. Every site no test exercises.
8. Deviations, risks, missing evidence, and one smallest next step.

Include `Resolved Execution Issues / Near-Misses` and
`Pre-Existing Failure Classification` sections, each `none` or a complete
classification. Finish with:

```text
Orchestration critique:
MEASURED: none | <verified finding; evidence; effect; smallest correction>
LEAD: none | <unverified possibility; cheapest useful check>
```

## Mandatory reading

- `/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
  sections 2.12 and 2.13 in full.
- Every file named in the anchors, in full for the extension sources.
- `docs/X_COMPANION.md` — read-only, for behavior context.
- `AGENTS.md`, `docs/WORKER_EXECUTION_CONTRACT.md`, `.ap/AP_WORKER.md`,
  `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will verify the matrices, the retained readers,
the DOM/style agreement and the suites at the reported commit, then arrange a
separate publication and the exact-main NUC refresh; only after that refresh
does the Cooperator reload the identified extension revision (closing stale
side panels and refreshing affected pages) and record the rendered acceptance
against that actual server/extension pair. The removal cut (`C7-B`) follows
that acceptance. No push, refresh, reload or rendered claim is authorized
inside this prompt.

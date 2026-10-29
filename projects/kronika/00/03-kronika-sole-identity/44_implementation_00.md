# Authoritative Worker prompt — Worker session 44, exchange 01

Activation: this file is the exact issued Worker prompt for the logical whole
`kronika-sole-identity`, Worker session `44`, exchange `01`. Stored under the
Meta filename mapping as `44_implementation_00.md`, with report destination
`44_report_00.md` in the same directory. Storage naming is Meta policy and
grants no authority.

## Identity and route

```text
Persistent role identity: WORKER
Logical whole identity: kronika-sole-identity
Worker session ordinal: 44
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: KSI-IMPL-C7AS — canonical server companion web emissions
Delivery route: manual Cooperator delivery
Reasoning recommendation: High
Recommended context capacity: approximately 1M tokens
```

Rationale: `High`. This is the first half of the companion web protocol
transition. The served NUC web host must begin emitting the canonical protocol
spelling and accept both spellings before the extension may switch its own
emissions; a one-sided mistake in either direction breaks meme attach silently
against a not-yet-refreshed peer. The cut also replaces fragile source-text
multiset assertions with behavioral emission/acceptance assertions, so the
transition state must be proven by driving the real modules.

This is work item **C7-A/S** from the accepted closure plan at
`25_report_00.md` section 2.11.

## Specification

`/home/agile/meta/projects/kronika/00/03-kronika-sole-identity/25_report_00.md`
sections 2.11, 2.12 and 2.13 are your specification. Read all three in full;
2.12 and 2.13 delimit what belongs to later cuts and stays untouched here.
Required outcomes:

1. **Canonical host emissions.** In
   `src/kronika/adapters/api/web/companion_host.js`, every outbound `v:` value
   (WEB_READY at `start()`, HOST_ACK, ATTACH_REQUEST, and any other outbound
   message) becomes `kronika.companion.web.v1`. Everything else in the asset is
   unchanged: the pinned extension origin, the frame/source identity checks,
   the UUID validation, the type checks, listener failure containment, and the
   `start`/`attach`/`onHostedChange`/`onOpenDetails` behavior.

2. **Compatible readers.** The inbound message gate accepts both
   `kronika.companion.web.v1` and the retired `framenest.companion.web.v1`: an
   un-refreshed extension still sends the retired spelling until the companion
   cut, and the refreshed extension will send the canonical one. Every
   near-miss or unknown spelling stays refused. Keep the module's exports
   sufficient for the behavioral tests; recommended: an emitted-spelling export
   plus an accepted-spellings export mirroring the extension's
   `ACCEPTED_WEB_PROTOCOLS` pattern. Derive your own if you can prove the same
   matrix.

3. **Truthful contract comment.** Rewrite the asset's protocol comment to the
   new transition state: the host now emits the canonical spelling and accepts
   both; the extension still emits the retired spelling until its own cut; the
   compatibility readers are removed in the removal cut. Do not claim the
   extension already emits the canonical spelling.

4. **Delete, do not re-pin, the two multiset assertions.** In
   `tests/companion_web_bridge.test.js` the two `v: <expr>` multiset
   assertions — the source-regex `deepEqual` blocks around lines 336–345, one
   listing the extension's outbound protocol expressions and one listing the
   host's — are deleted and replaced with behavioral emission/acceptance
   assertions:
   - drive the real host through `createHost` and capture `postMessage` to
     prove every outbound `v` is the canonical spelling (start → WEB_READY;
     HOST_HELLO → HOST_ACK; `attach()` → ATTACH_REQUEST);
   - prove inbound acceptance for BOTH spellings on the host for HOST_HELLO,
     ATTACH_RESULT and OPEN_DETAILS, and that near-miss spellings remain
     refused on the host side as they already are on the bridge side;
   - prove the extension bridge still emits the retired spelling and accepts
     both (its existing dual-acceptance behavior and tests are kept, with
     names/messages re-framed where they now overclaim).
   The origin/source/UUID checks and the no-wildcard-`postMessage`-target
   assertions remain and keep passing. Test names or messages that assert "the
   web and shell share the protocol" or "the NUC host still emits the retired
   web protocol" are re-framed truthfully for the new transition state.

5. **Served-asset contract test.** In `tests/contract/test_local_web_application.py`
   the served-asset assertions (the
   `test_companion_host_asset_omits_wildcard_cors_and_wildcard_postmessage`
   test and any sibling that asserts the retired spelling is served) must assert
   the canonical spelling is served as the emission while the retired spelling
   remains present as the compatible reader. Keep the no-wildcard and
   pinned-origin assertions unchanged.

6. **Boundaries.** Do not touch `extension/**`: its emissions, comments and
   tests belong to the companion cut, which runs only after this server is
   published and served. Do not touch the mutation header
   (`src/kronika/adapters/api/tailscale_ingress.py`) or its tests. Do not rename
   the `FrameNestCompanionWeb` global or any coupled DOM/class/style
   identifier. Do not edit `docs/X_COMPANION.md` or any ADR (frozen). Do not
   rebuild the composition duality as new work; only extend the host reader.

7. **Retention.** Re-pin a Part C scalar only when your own measurement shows
   this cut moved it, with the arithmetic cause recorded in the ledger comment
   like the existing running entries. Never tune a pin until a suite is green.

## Anchors, as locators, not an inventory

- `src/kronika/adapters/api/web/companion_host.js` — the protocol comment and
  `PROTOCOL` (around lines 8–17), the inbound gate (around line 84), the
  outbound sites (around lines 89, 130, 144) and the exports (around line 178).
- `extension/ui/sidebar.js` — read-only context: the dual-acceptance pattern
  (`WEB_PROTOCOL`, `CURRENT_WEB_PROTOCOL`, `ACCEPTED_WEB_PROTOCOLS`) and the
  current boundary comment. Do not edit.
- `tests/companion_web_bridge.test.js` — the shared-protocol test (around line
  63), the extension acceptance tests (around lines 261, 280), the refusal list
  (around line 295), the emit test with the two multiset assertions (around
  lines 329–345), and the host behavioral tests (around lines 77, 95, 116, 146).
- `tests/contract/test_local_web_application.py` — the served-asset test around
  lines 262–276.
- `tests/contract/test_public_published_uds.py` — around lines 91 and 567;
  verify whether anything must move (a published page excludes the host script
  there; state your finding either way).
- `src/kronika/adapters/api/public_published_api.py` — the script embed around
  line 66; expected unchanged; state your finding.
- `tests/contract/test_kronika_identity_retention.py` — the Part C scalars and
  the running per-file comment block.

## Verified starting state, measured by the Orchestrator on 2026-10-12

```text
Repository checkout topology: standalone checkout on main; `.ap` is a pinned submodule
Working directory:            /home/agile/Projects/kronika
Branch:                       main
Expected HEAD:                e9413dff98605443e7d17557f498c87433c93e92
Public main:                  fcde631047650d1ff0a84b84bf185b54d6d11ba5
                              (e9413df is local and unpublished by design)
Working tree:                 clean
Containing-repository .ap gitlink and submodule HEAD:
                              73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor:                    PASS, governing variant stable
Python baseline at HEAD:      4955 passed, 8 skipped, 3 warnings, 0 failed
Retention module:             15 passed
JS tests/companion_web_bridge.test.js:        14 passed, 0 failed
JS tests/companion_review_extension.test.js:  40 passed, 0 failed
JS bounded non-browser glob (*_frontend, *_cockpit, gallery_*): 213 passed, 0 failed
```

Re-derive the git/AP gates yourself at the start. If any fails, stop and
report. No host contact; everything here is repository-only with synthetic
fixtures.

## Authority

```text
Positive authority: edit `src/kronika/adapters/api/web/companion_host.js` for
  exactly the emission/reader switch and its contract comment; edit
  `tests/companion_web_bridge.test.js` for the behavioral rework;
  edit `tests/contract/test_local_web_application.py` for the served-asset
  assertions; edit `tests/contract/test_public_published_uds.py` only if a
  directly coupled assertion must move, naming it in the report before editing
  it; edit `tests/contract/test_kronika_identity_retention.py` only to re-pin a
  Part C scalar that your own measurement shows this cut moved, with the
  arithmetic cause stated; create exactly one local non-amended commit on `main`.

Negative authority: every other path; `extension/**`; the mutation-header
  module and its tests; any document including `docs/X_COMPANION.md` and every
  ADR; any dependency or lockfile change; any change to `pyproject.toml`,
  `ap.project.conf` or the `.ap` gitlink; any frozen document or Alembic
  revision; publication; push; force; amend; branch; stash; any NUC contact or
  SSH; any migration or deployment invocation; any provider, browser or capture
  contact; any secret or personal-configuration read. If a necessary change
  falls outside the positive scope, stop and report; do not widen scope.

Commands: Python evidence only through
  ./.ap/ap exec --root /home/agile/Projects/kronika --baseline e9413dff98605443e7d17557f498c87433c93e92 --operation <id> [-- <argv>]
  and `./.ap/ap project check --root ... --baseline ...`. Never invoke
  `.venv/bin/python`, `python`, `python3` or `poetry run`, including as a text
  editor. JavaScript evidence uses only the documented ordinary invocation from
  the worktree root, naming every suite you run:
  node --test tests/<name>.test.js
  Read-only Git inspection allowed; exactly one `git add <exact paths>` and one
  `git commit`; no push.

Dependency authority: none.
Git authority: exactly one local non-amended commit; no push, no branch, no tag.
Secret authority: none.
Untrusted-content boundary: .ap/AP.md at the pinned commit governs; repository
  AGENTS.md and the accepted plan are authoritative inside their scope. On
  conflict between retained context and current repository evidence, stop.
Side-effect authority: reversible local repository mutation only.
Browser authority: none. No extension reload, no real side panel, no profile.
```

## Verification

1. **Baseline reproduction before editing.** Write the new behavioral
   expectations first and run them against the unmodified asset: the host still
   emits the retired spelling at every outbound site and refuses the canonical
   inbound spelling, so the new emission/acceptance assertions fail. Report each
   observed failure. Any temporary probe material is removed before the commit.
2. **Matrix, through the real modules and `node --test`:**
   - host outbound canonical at every send site, with the captured `postMessage`
     `v` values shown;
   - host inbound accepted for both spellings across HOST_HELLO, ATTACH_RESULT
     and OPEN_DETAILS; near-miss and unknown spellings refused;
   - extension still emits the retired spelling and accepts both, with its
     identity checks unchanged;
   - pinned origin, source identity, UUID validation and no-wildcard target
     unchanged; the Gallery/Details paths (`open_details`, `attach`) exercised
     under both inbound spellings.
3. **Suites.** Run through the declared routes: the touched JS suite, the
   companion extension suite, and the documented bounded non-browser JS glob;
   then the focused Python modules
   (`tests/contract/test_local_web_application.py`,
   `tests/contract/test_public_published_uds.py`), the full declared Python
   suite, and the retention module. Report every count, elapsed time and any
   difference from the measured baselines `14`, `40`, `213`, `4955/8/3/0` and
   `15`.
4. Report **every moved or removed site that no test exercises**, and every
   caller or consumer of the changed protocol emissions your derivation found
   that this prompt did not name.
5. State the exact commit SHA, `git diff --stat`, confirm Part A is byte-unmoved
   and Part B still measures 20, and show your own measurement and per-file
   cause for any Part C movement. The ledger comment gains one running entry in
   the existing style.

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

**Collapsing pairs.** The emission spelling and the accepted set must not
collapse: a near-miss must never become accepted, and the retained retired
reader must never become an emission. Name every acceptance branch that could
fail silently and prove it refuses with its existing shape.

**Transcribed tables.** `FROZEN_ALEMBIC_SHA256` has **36** keys; compute it.

## Finishing

```text
Stopping conditions: stop without improvising if the repository gate does not
  match; if a necessary change would touch `extension/**` or the mutation
  header (those belong to later cuts); if a frozen hash, Part A or Part B
  moves; if a Part C re-pin cannot be reproduced from your own measurement; if
  a required change falls outside the positive scope; if context pressure
  reaches the point where a bounded rotation is cheaper than a degraded result.

Completion: the canonical host emissions with compatible readers implemented;
the behavioral matrix green with the multiset assertions deleted, not re-pinned;
touched JS suite, companion extension suite, bounded non-browser JS glob,
focused Python modules, full declared Python suite and retention module green
through the declared routes; one local commit; report delivered.

Report destination: the terminal report is delivered to the Orchestrator for
  this session. Do not write it to any file. The Orchestrator stores it as
  `44_report_00.md` in
  /home/agile/meta/projects/kronika/00/03-kronika-sole-identity/.

Authority expiry: on submission of the terminal report, all authority under
  this prompt expires. No further implementation, no second commit, no push, no
  publication, no refresh, no host contact and no later cut is authorized by
  it.

Phase-qualified result: not-applicable
Logical-whole closure: not-closed
NUC contact: none in this cut, by design
```

Report justification: exactly one of `new-mutation`, `new-evidence`,
`new-material-risk`, `changed-external-state`, `final-acceptance`,
`explicit-closure`. The expected value is `new-mutation`.

## Required report sections

The standard report core and the exact header `### Report for ORCHESTRATOR_CHAT`,
echoing `kronika-sole-identity`, session `44` and exchange `01` unchanged. Then:

1. The emission/reader matrix as implemented, with the behavioral proofs.
2. The two deleted multiset assertions and their behavioral replacements,
   quoted.
3. The served-asset contract-test changes and the
   `test_public_published_uds.py` / `public_published_api.py` findings.
4. The baseline reproductions before editing.
5. JS and Python suite results with elapsed time and any baseline difference.
6. `git diff --stat`, the commit SHA, Part A unmoved, Part B still 20, and
   Part C movement with cause.
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
  sections 2.11, 2.12 and 2.13 in full.
- `src/kronika/adapters/api/web/companion_host.js` in full.
- `extension/ui/sidebar.js` — read-only, for the dual-acceptance pattern.
- `tests/companion_web_bridge.test.js` in full.
- `tests/contract/test_local_web_application.py` — the served-asset test.
- `docs/WORKER_EXECUTION_CONTRACT.md` — the JavaScript Tests section.
- `AGENTS.md`, `.ap/AP_WORKER.md`, `.ap/AP.md` §5, §9, §12.

Do not read `private/**`, personal Fish configuration, `~/.config/opencode`,
any credential store, any real browser profile.

## Communication

Report text, code and comments are professional English. Do not use Czech or
Slovak.

## Orchestrator acceptance note

On acceptance the Orchestrator will verify the behavioral matrix, delete-not
re-pin treatment, the served-asset assertions and the suites at the reported
commit, and will then arrange publication and the exact-main NUC refresh as
separate authority. The companion transition (`C7-A/C`) and the Cooperator's
rendered acceptance run only against that served canonical server. No push,
refresh or rendered claim is authorized inside this prompt.

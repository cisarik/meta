### Report for ORCHESTRATOR_CHAT

Logical whole identity: upload-flow-polish
Worker session ordinal: 07
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Bounded UI Polish Worker
Phase: Correction
Task identity: KRN-COVER-CORR-01 — move Choose cover, add a brain icon and auto-preview the selected frame
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 0a96fc18b49191a32e7f482c4e881ad714db094a
End commit: e64f2b0f92458fac2590e03672e30da62275b345
Report justification: new-mutation
Logical-whole closure: not-closed

Evidence posture: non-independent correction. This session implemented and validated the candidate. It does not accept, publish, deploy, or close the whole. Orchestrator verification and Cooperator rendered acceptance follow.
Requested reasoning: Medium. Effective reasoning and context capacity were not independently attested.
Native planning mode was not-used: the session accepted repository writes and was not in native Plan mode. Plan mode was not switched on.
Repository gate: branch main, HEAD was 0a96fc18b49191a32e7f482c4e881ad714db094a, worktree clean, AP gitlink and submodule HEAD d7023cf037f6d17885c3ede5c04812c61640da50. ap doctor PASS. ap project check --baseline 0a96fc18b49191a32e7f482c4e881ad714db094a PASS before editing and again before the selected tests.

Cooperator finding: the media-details footer showed Choose cover, while Edit had Analyze by AI and no cover action. The cover dialog's Preview frame button was rejected. The correction removes Choose cover from Details, places it in the metadata footer, uses a brain icon for Analyze by AI, removes Preview frame, and loads the selected frame automatically.

Moved controls and presentation:
- Details footer keeps only Edit. `#media-details-choose-cover` is removed.
- `#metadata-choose-cover` is in the metadata footer immediately after `#metadata-ai-analyze-button` and before `#metadata-discard-button`. It opens the existing cover dialog for `metadataWorkspace.openItem`.
- Capability visibility in `applyIdentityCapabilities` now targets `metadataChooseCoverButton`.
- `KRONIKA_BUTTON_ICONS` maps "Analyze by AI" to 🧠. The button text and accessible name stay "Analyze by AI". "Choose cover" stays 🖼️. The "Preview frame" entry is removed.
- Choose cover uses the Analyze-by-AI footer treatment on a grey surface: background `#c9d1c9`, hover and focus `#d7ded7`, dark text `#0c1a10`, grey-green border, and a muted disabled state. Focus-visible also draws a 2px `#3d4a3d` outline so the grey control stays readable. Unused `.cover-button--primary` is removed. The public-audience hide selector now names `#metadata-choose-cover`.

Automatic preview wiring:
- After `loadCoverTimeline` shows the cover content and the context is still current, `requestCoverPreview()` runs for every media kind, including the first frame at timestamp 0.
- The range `input` listener still only updates the readout and hides replace confirmation. A range `change` listener requests the preview when the slider is released.
- `stepCoverTimestamp` updates the timestamp and readout, hides replace confirmation, then requests the preview.
- Preview abort, preview token, source-version check, loading and error status, the unsaved-until-Set-as-cover wording, explicit Set as cover, and replace confirmation remain. A preview does not become the accepted cover. No API, payload, authorization, schema, migration, storage, or cover-accept semantics changed.

Changed paths and diff stat, parent 0a96fc18b49191a32e7f482c4e881ad714db094a:
```text
 src/kronika/adapters/api/web/app.js          | 38 +++++----------
 src/kronika/adapters/api/web/index.html      | 10 +---
 src/kronika/adapters/api/web/styles.css      | 51 ++++++++++++++++++--
 tests/browser_cover_evidence.test.js         | 33 ++++++++++---
 tests/contract/test_local_web_application.py | 71 ++++++++++++++++++++++++++++
 tests/cover_frontend.test.js                 | 50 +++++++++++++++++++-
 6 files changed, 205 insertions(+), 48 deletions(-)
```

Validation:
- `./.ap/ap doctor`: PASS
- `./.ap/ap project check --root /Users/agile/Projects/kronika --baseline 0a96fc18b49191a32e7f482c4e881ad714db094a`: PASS
- `./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 0a96fc18b49191a32e7f482c4e881ad714db094a --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_cover_api.py -q -p no:cacheprovider`: 222 passed
- `node --test tests/cover_frontend.test.js tests/catalog_card_ai_quick_action.test.js tests/kronika_ui.test.js tests/browser_cover_evidence.test.js`: 75 passed, 1 skipped, 0 failed
- `git diff --check` and `git diff --cached --check`: clean

Browser evidence: skipped. `KRONIKA_RUN_BROWSER_EVIDENCE` was unset, so `tests/browser_cover_evidence.test.js` reported SKIP for "real browser evidence: manual cover authoring flow". Chrome and ffmpeg were not invoked. This is not rendered evidence. The updated browser test opens Edit, then `#metadata-choose-cover`, waits for the automatic first frame, and closes the metadata editor after the video cover sequence before the next details flow. The Cooperator's rendered cover check remains the final UI evidence.

Git result: one normal commit on main, e64f2b0f92458fac2590e03672e30da62275b345, parent 0a96fc18b49191a32e7f482c4e881ad714db094a, subject `fix: move cover selection and auto-preview the frame`. Worktree clean after the commit. No push, fetch, amend, or other Git write.

Deviation: the Choose cover focus-visible rule adds an explicit outline as well as the grey hover surface. That stays inside the requested readable-focus treatment.
Residual risk: slider-release preview, step-button preview, nested metadata/cover dialogs, and the brain icon were checked in source and contract tests only. Existing Edit behavior closes Details before the metadata workspace opens, so Choose cover is reached from that workspace rather than from a still-open Details footer.

Acceptance candidate: e64f2b0f92458fac2590e03672e30da62275b345
Acceptance owner map: Orchestrator verification, then Cooperator rendered acceptance; this Worker is non-independent
Acceptance allowlist: src/kronika/adapters/api/web/index.html, src/kronika/adapters/api/web/app.js, src/kronika/adapters/api/web/styles.css, tests/cover_frontend.test.js, tests/browser_cover_evidence.test.js, tests/contract/test_local_web_application.py
Acceptance risk claims: presentation and client interaction only; cover acceptance, authorization, and durable cover semantics unchanged
Acceptance control matrix: positive — moved footer control, brain icon, grey Choose cover style, automatic preview on open, slider release, and step; negative — no Preview frame control, no details cover remnant, no API, schema, storage, or accept-semantic change, and a preview is not an accepted cover
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: full-fresh
Named missing-evidence probe: none
Out-of-scope observations: none

Repository mutation: the six allowlisted paths above
Host/remote mutation: none
Trace persistence: direct-write /Users/agile/meta/projects/kronika/01/02-upload-flow-polish/07_report_00.md

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
Smallest next step: Orchestrator verifies e64f2b0f92458fac2590e03672e30da62275b345, then the Cooperator performs the rendered cover check after the separately authorized publication and NUC refresh.
Orchestration critique:
MEASURED: none
LEAD: the gated browser evidence was not run because KRONIKA_RUN_BROWSER_EVIDENCE was unset; the cheapest useful check is the Cooperator's rendered cover pass on the published candidate.
Authority expiry: this terminal report ends the grant; no autonomous continuation.

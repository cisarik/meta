# Implementation Exchange 05 — Session 02 — Slice 4: Administrator AI Provider Web Surface

Persistent role identity: WORKER
Logical whole identity: framenest-admin-openai-compatible-provider-registry-and-vision-probe
Worker session ordinal: 02
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker (current-session continuation)
Phase: Implementation
Task identity: IMPLEMENT-AI-PROVIDER-ADMIN-WEB-SURFACE-SLICE-4
Implementation authority: explicit
Delivery route: Agent Orchestrator default dispatch into the same session (continuity anchor below)
Reasoning recommendation: High — named risk: the rendered administrator surface is the Cooperator's acceptance target; gating, no-provider-call-on-render, confirm-before-pong, and sanitized failure copy must be exact, and the frozen Gallery/Details visuals must not move
Recommended context capacity: approximately 250k tokens
Independence required: no
Sub-agents or internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active

## Continuity anchor and authority renewal

Continuity anchor: your terminal PASS reports for exchanges 02-04
(`02_report_02.md`, `02_report_03.md`, `02_report_04.md`) and your commits
`980db7af…`, `e6d91d1b…`, `c66f5b6a…`. Prior authority expired at the last
report. This is a complete renewed grant for slice 4. Retained context is
convenience, not authority; repository evidence wins on conflict. Evidence in
this exchange is non-independent.

## Goal

Implement slice 4: the administrator AI provider web surface in the packaged
web shell — header control, dialog, provider list, record form with
read-only JSON preview, activate, ping, and pong with explicit confirmation,
all correctly gated by identity. No documentation changes in this slice.

## Mandatory reading

- The accepted plan
  `/home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/01_report_orchestrator.md`
  §8 (admin API routes and error codes), §9 (administrator UI), §13 tests 13
  and 14, §14 slice 4.
- `src/framenest/adapters/api/web/app.js` — identity bootstrap
  (`loadIdentity`, `identityState`, `applyIdentityCapabilities`,
  `framenestMutationHeaders`, the Status dialog machinery, and the existing
  dialog/confirm patterns), `index.html` header and `settings-dialog`
  markup, `styles.css` `settings-dialog` styles and audience gating
  selectors.
- The implemented server contract (your slice 3):
  `src/framenest/adapters/api/ai_admin_api.py` — exact paths, request bodies,
  response shapes, and error codes.
- Tests that must stay green unmodified: `tests/tailscale_identity_frontend.test.js`
  (note its invariants: exactly one `"X-FrameNest-Request"` literal in
  `app.js`, every `method: "POST|PUT|PATCH|DELETE"` fetch call site wrapped
  with `headers: framenestMutationHeaders(`), and
  `tests/companion_settings_automatic_analysis.test.js`.

## Repository gate (before mutation)

Verify: HEAD equals `c66f5b6ae438d686d1e3c8f7b8e3ebccd0e885b9` (this
exchange's authorized baseline), porcelain clean, branch
`feat/x-meme-browser-companion`, `.ap` gitlink unchanged,
`./.ap/ap ap doctor` PASS. Stop on any unexplained difference.

## Slice 4 deliverables (binding design)

### D1 — Header control (`index.html`)

Add exactly one control inside the existing header control group, hidden by
default:

```html
<button id="ai-providers-button" class="status-button status-button--icon" type="button" hidden
  aria-label="AI provider administration" title="AI provider administration">
  <span class="status-button__glyph" aria-hidden="true">🛠️</span>
  <span id="ai-providers-button-text" class="visually-hidden">AI providers</span>
</button>
```

The 🧠 Status dialog stays read-only and unchanged; no provider control is
placed inside it.

### D2 — Dialog (`index.html` + `app.js` + `styles.css`)

New `<dialog id="ai-providers-dialog" class="settings-dialog" aria-label="AI providers">`
reusing the existing `settings-dialog` visual language (dark premium surface,
header with close button, body sections). No tabs required. Component
inventory (ids are binding; additional internal ids are allowed):

- `#ai-providers-active-summary` — active provider/model; "Credential
  available to this process: yes/no"; an environment-override warning when
  `configuration_source` is `environment`.
- `#ai-providers-list` — one row per provider: display name, id,
  `Built-in`/`Declared` badge, protocol, base URL, credential env **name**,
  credential availability, model chips with capability badges, selected-model
  marker, last ping summary, last vision-probe summary; actions
  `Use for analysis`, `Ping`, `Test vision`, `Edit` (declared only),
  `Delete` (declared and non-active only).
- `#ai-providers-form` — labeled fields: id, display name, base URL,
  credential env name, protocol (read-only value with a note that other
  protocols are not supported yet), model rows (model id, display name,
  `vision_input` checkbox chip), Add/Remove model controls.
- `#ai-providers-json-preview` — read-only `<pre>` built locally from form
  state, pretty-printed (2-space) with sorted keys, using the exact on-disk
  field names (`name`, `protocol`, `base_url`, `credential_env`, `models`)
  for the record object that would be persisted. It must never contain a
  secret or a key-shaped field and must update locally on typing with no
  fetch.
- Actions: `#ai-provider-save`, `#ai-provider-activate`, `#ai-provider-ping`,
  `#ai-provider-pong`, `#ai-provider-delete`.
- Pong confirmation: an in-dialog confirm block (same pattern as the
  companion automatic-analysis confirm; never `window.confirm`) naming the
  fixture as "a tiny solid-red test square made by FrameNest", the provider,
  and a cost/privacy note (OpenCode Go bills image tokens; only the synthetic
  square is sent). Only the confirm button issues
  `POST /api/admin/ai/pong` with `{confirm_cloud_upload: true}`.
- Progress: while ping/pong runs set `aria-busy="true"` on the dialog,
  disable both action buttons, and show an accessible indeterminate status
  line ("Testing connection…", "Sending the color test…"); no fabricated
  percentages, no cancellation claim.
- Results: sanitized human copy for every status/code, including
  403-entitlement ("The provider rejected the credential or this model is not
  included in your subscription."), missing credential with the env **name**
  in the hint and Ping/Test vision disabled, `mismatch` ("The model answered,
  but not with the expected color.") plus the bounded observed token, busy,
  confirmation required, built-in read-only, and active-delete refusal. No
  stack traces and no provider payload in any copy.

### D3 — Behavior and gating (`app.js`)

- New helper `identityAllowsProviderAdministration()` = `identityState.resolved`
  AND `isWorkspaceAudience()` AND `identityHasCapability("provider.operate")`
  AND (`identityState.available` OR `identityState.audience === "trusted_loopback"`).
  Wire it into `applyIdentityCapabilities()` to toggle the header button.
  Ordinary Tailscale users, unmapped identities, unresolved bootstrap, and
  public published callers never see the control and get no empty chrome.
  UI hiding remains convenience only; the server is the authorization
  mechanism.
- Dialog open performs exactly one network-free
  `GET /api/admin/ai/providers` (Accept: application/json, no-store) and
  renders the list; typing and JSON-preview updates are fully local.
  Ping, Test vision, Use for analysis, Save, Edit, and Delete happen only on
  explicit user actions. No provider call on hover, on list render, or on
  typing.
- All unsafe fetches use `method: "PUT" | "POST" | "DELETE"` with
  `headers: framenestMutationHeaders({...})` so
  `tests/tailscale_identity_frontend.test.js` stays green unmodified, and the
  literal `"X-FrameNest-Request"` still appears exactly once in `app.js`.
- Map server error codes to the sanitized copy in D2; treat network failure
  as an honest unavailable state.

### D4 — Styling (`styles.css`)

Reuse the existing `settings-dialog` classes; add only the new surface's
styles (list rows, badges, chips, form rows, preview block, confirm block,
progress line) and narrow-width media queries for this dialog only. Do not
restyle Gallery or Details; do not change existing selectors' behavior.

## Exact changed-path allowlist

```text
src/framenest/adapters/api/web/index.html
src/framenest/adapters/api/web/app.js
src/framenest/adapters/api/web/styles.css
tests/ai_providers_admin_frontend.test.js (new)
```

No other file may be created, edited, deleted, or moved.
`tests/tailscale_identity_frontend.test.js` and
`tests/companion_settings_automatic_analysis.test.js` must pass unmodified;
if either genuinely requires a change, stop and report instead.

## Tests

`tests/ai_providers_admin_frontend.test.js` (new), following the existing
VM/DOM-stub harness style (`tests/tailscale_identity_frontend.test.js`,
`tests/companion_settings_automatic_analysis.test.js`):

1. Markup inventory: the header control exists, is hidden by default, and the
   dialog reuses `settings-dialog` classes.
2. Gating cases for the helper and `applyIdentityCapabilities`: loopback
   admin (audience `trusted_loopback`, full capability set) shows the
   control; tailscale workspace admin shows it; ordinary, public published,
   unresolved, and failed-identity-bootstrap cases hide it.
3. Dialog open issues exactly one GET to `/api/admin/ai/providers` and no
   mutation; typing a form field triggers no fetch and updates the JSON
   preview locally; the preview contains no secret, key, Authorization, or
   token field and mirrors the form values with the on-disk field names.
4. Ping and Test vision run only on explicit clicks; pong requires the
   in-dialog confirm and sends `confirm_cloud_upload: true`; no
   `window.confirm` usage.
5. Every mutation call site uses `framenestMutationHeaders`; the
   `"X-FrameNest-Request"` literal count in `app.js` remains one.
6. Failure-copy mapping contains no provider payload, key, or path; built-in
   rows expose no Edit/Delete; Delete is unavailable on the active provider;
   Ping/Test vision disabled when the credential is unavailable, with the
   env **name** in the hint.

Validation:

```text
node --test tests/ai_providers_admin_frontend.test.js tests/tailscale_identity_frontend.test.js tests/companion_settings_automatic_analysis.test.js
```

plus the Python asset/ingress regression through the declared AP route:

```text
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline c66f5b6ae438d686d1e3c8f7b8e3ebccd0e885b9 --operation test-focus -- tests/contract/test_local_web_application.py tests/contract/test_web_package_resources.py -q -p no:cacheprovider
```

## Commands (canonical execution route — binding)

```text
./.ap/ap ap project check --root /home/agile/Projects/framenest --baseline c66f5b6ae438d686d1e3c8f7b8e3ebccd0e885b9
./.ap/ap ap exec --root /home/agile/Projects/framenest --baseline c66f5b6ae438d686d1e3c8f7b8e3ebccd0e885b9 --operation runtime-info
```

plus the `node --test` line above and the Python asset regression.

Validation ladder:

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the named JS suites and the Python asset/ingress regression
Affected tests: the new frontend suite plus the two named JS suites and the two named contract suites
New causal regression: the new surface, its gating, no-fetch-on-typing, and confirm-before-pong have no prior coverage
Broad or full suite: not-used — no project rule or named decision risk requires it for this slice
Runtime or testbed: not-used (a real rendered check belongs to the Cooperator's numbered acceptance later)
Independent acceptance: not-required
```

## Authority

Positive: edit/create only the allowlisted paths; the declared AP route and
the exact `node --test` invocation; read-only Git; stage exactly the
allowlisted paths; one local commit with subject
`Add administrator AI provider web surface`; no push; the single Meta report
below.

Negative: everything outside the allowlist; any Python/server change; any
documentation or ADR change; any other Git write; any provider/network call
(the UI performs only the local list GET and explicit click calls in tests
with stubbed fetch); NUC/SSH/sudo; GUI or IDE launch; browser automation;
ambient Python, `poetry run`, `pip`, `uv`, environment reconstruction; secret
access; `git add .`/`-A`; no weakening or deleting existing tests, and no
change to the two named JS suites.

## Meta persistence contract (execute exactly)

```text
Meta persistence owner: this Worker, for the single report path named below.
Prompt persistence owner: ORCHESTRATOR (already written; do not rewrite it).
Exact report destination: /home/agile/meta/projects/framenest/12/00-framenest-admin-openai-compatible-provider-ux/02_report_05.md
Write the complete terminal report to that path after the work, then verify
byte identity. Do not create other Meta files. Do not rename. Do not commit
Meta Git. Do not commit FrameNest unless this prompt grants FrameNest Git.
If the path already contains a terminal report, STOP (PARTIAL) — do not
overwrite.
The Cooperator must not be asked to create, paste, or rename files.
```

## Report contract

Begin exactly with `### Report for ORCHESTRATOR_CHAT`; echo these coordinates
once (`Worker session ordinal: 02`, `Worker exchange ordinal: 05`); compact
core: status; `Phase-qualified result: implementation-PASS` on PASS else
`not-applicable`; start commit `c66f5b6…`; end commit; changed files; tests
and validation with exact counts; commit result; deviations/risks; one
smallest next step; `Report justification: new-mutation`; authority-expiry
statement; `Orchestration critique` (MEASURED/LEAD); Resolved Execution
Issues / Near-Misses and Pre-Existing Failure Classification;
`Logical-whole closure: not-closed`. Save, read back fully, verify identity,
then a short separate completion notice with location and SHA-256.

## Stopping conditions

Stop and report BLOCKED or PARTIAL when a gate fails unclassifiably, a needed
change exceeds the allowlist, an existing test must be weakened, the
execution route is unusable, the Meta destination is occupied or unsafe, or
retained context conflicts with repository evidence.

Authority expiry: this terminal report ends this grant; no autonomous
continuation.

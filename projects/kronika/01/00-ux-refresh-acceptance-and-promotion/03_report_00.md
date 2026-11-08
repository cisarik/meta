Kandidát, brána aj allowlist sedia. Verdikt je v správe pre orchestráciu.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: ux-refresh-acceptance-and-promotion
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Task identity: UXR-AUDIT-03
```

Status: PASS

Phase-qualified result: acceptance-PASS

Logical-whole closure: not-closed

Start commit: `cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`

End commit: `cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738`

Report justification: `final-acceptance`

Requested reasoning: High. This session had no prior planning or implementation conversation about the whole. Model identity was not independently attested.

## Acceptance and correction record

```text
Acceptance candidate: cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738
Acceptance owner map: the E3 rows of 02_report_00.md section "Acceptance control matrix" and the prompt allowlist
Acceptance allowlist: the prompt's exact path list
Acceptance risk claims: A1–A8, B4, B5, C4, and the open_upload part of F4
Acceptance control matrix: 02_report_00.md section "Acceptance control matrix" (E3 rows), fixed
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: ledger-candidates
```

This exchange is the primary fresh acceptance. No correction was made. The auditor does not self-certify a patch.

## Security audit report

```text
Security task class: focused defensive audit — R3 fresh focused audit (INFOSEC 4.2, 4.4, 4.5)
Owned/authorized target: https://github.com/cisarik/kronika at cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738, authorized by this audit grant
Commit under audit: cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738
Scope: E3 claims A1–A8, B4, B5, C4, and the open_upload message part of F4
Exclusions: E2 web-shell, companion-UI, and documentation rows; rendered acceptance; NUC; providers; full suite; files outside the allowlist
Threat model: recorded below
Source records: none — no external standard was cited as a requirement
Findings: none
Containment ledger: no temporary root was created; named suites were not executed
Limitations: recorded below
Residual-risk summary: recorded below
```

### Threat model

```text
Assets: household media and private records; companion and provider credentials; catalog integrity; preview cache; the NUC service and its filesystem.
Trust boundaries: browser extension to served shell (postMessage); companion origin to Tailscale ingress; authenticated identity to server-side capability; server process to preview cache and source media; server process to NUC host.
Attacker-controlled inputs: arbitrary web origins; postMessage events; the companion Origin header and X-Kronika-Request header; YouTube/X URLs and request bodies; query parameters; uploaded media and filenames; test fixtures.
Security properties: the companion origin is accepted only on the exact flagged unsafe routes; capability is enforced server-side after origin; privileged actions are audited before the action; the interactive confirmation binds the request; the pinned postMessage origin and parent-window source are required; the manifest permission delta is minimal; preview writes stay inside the cache; GET remains side-effect free; no secret or host value leaks.
Abuse cases: a hostile page posts open_upload or open_details; a spoofed companion origin reaches an unflagged route; a missing confirmation creates a request; an audit row is skipped; a path-traversal or symlink escapes the preview cache; the companion reads cookies, sessions, profiles, or history; the extension acquires a broader host permission; replay or duplicate submission after the UI budget.
```

Evidence class for the accepted controls is `established-static`. No abuse case was dynamically reproduced. The named tests were read and not executed, because reading closed each fixed claim.

## Repository gate

```text
HEAD: cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738
branch: main
public main: cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738
working tree: clean
.ap gitlink and submodule HEAD: 73e20ef80b88700d5fcbc397cd8edd4fc425869f
ap doctor: PASS (strict pinned commit, clean submodule, managed block, governing variant stable)
ap project check --baseline cb5fa4ddc06ab5ba4f2af48eed67b6eabf036738: PASS
```

`ap project check` printed its sanitized-environment warning (`GIT_CONFIG_*`, `SSH_AUTH_SOCK`, `PATH`). That warning is not a gate failure. Python evidence used only that check. Ambient `python`, `python3`, `.venv/bin/python`, and `poetry run` were not used. `8cbbcad947964d711ebc2001e1c80976c4f82e24` is the range base; `git diff --name-only` against HEAD is the same 33-path set the plan recorded.

## Claim decisions

**A1 — accepted.** `companion_mutation=True` occurs on exactly six policies in `tailscale_ingress.py`: PUT `/api/admin/settings/automatic-analysis` (line 420), POST `/api/youtube/requests` (line 557), POST review-inbox `opened` (line 613), POST review-inbox `apply` (line 623), POST `/api/x/requests` (line 631), and POST `/api/x/requests/{claim_id}/retry` (line 640). POST `/api/youtube/requests/{request_id}/retry` (lines 559–566) and POST `/api/uploads` (lines 642–648) keep the default `False`. `test_only_companion_mutations_are_companion_flagged` asserts set equality of every flagged `(method, pattern)` against those six policies, so a seventh flag would fail the test. The default on `RoutePolicy` is `False`.

**A2 — accepted. The shared gate is sufficient.** For every unsafe method, `_mutation_origin_allowed` runs before the mutation header, identity, and capability (`tailscale_ingress.py` lines 846–873 and 1151–1162). A companion origin passes only when `companion_mutation` is true and the origin is an exact member of the allowlist. An unflagged route returns 403 `MUTATION_ORIGIN_FORBIDDEN`. The predicate does not branch on path. YouTube retry and `/api/uploads` use the same unflagged branch as POST `/api/canonical-tags`, which `test_companion_origin_is_accepted_only_on_flagged_companion_routes` already samples. A YouTube-specific negative sample is a non-blocking pin, not a missing control.

**A3 and B4 — accepted together.** POST `/api/youtube/requests` requires capability `youtube.request` and audit action `youtube.request.submit` (lines 551–557). `_record_allowed_attempt` writes that action before `self._app` (lines 937–954 and 1016–1049). A failed audit returns 500 and does not call the app. The handler's `_guard` requires `SCOPE_AUDIT_EVENT_ID` and `youtube.request` again before the body is read (`youtube_request_api.py` lines 133–147 and 323–334). `YouTubeRequestCreateBody` is `extra="forbid"` with `confirmation_method: Literal["interactive"]`. `ValidationError` returns 400 before `service.submit`. The submit call passes `YouTubeConfirmationMethod.INTERACTIVE`, so a client string is not forwarded. `yes_flag` is an extra or non-literal field and fails that validation. `saveYouTube` posts `{ url, confirmation_method: "interactive" }` (`service_worker.js` lines 260–268). The content script sends only `{ url }` through `SAVE_YOUTUBE` and contains no `yes_flag` (`youtube_adapter.js` lines 233–244).

The plan's A3 pass criterion says an omitted confirmation is 422. The repository returns 400. The fixed claim is that submit is not reached, and that holds. The 422 figure must not be copied into later documentation.

Missing assertions are non-blocking pins: the ingress YouTube sample asserts only that the error is not `MUTATION_ORIGIN_FORBIDDEN`; the allowlisted YouTube API tests do not cover an omitted confirmation, a non-interactive value, or `yes_flag`; no Node test asserts the worker literal.

**A4 — accepted.** After a passing origin and `X-Kronika-Request: 1`, identity is resolved and `has_capability` runs on the primary capability and any additional capabilities (lines 875–935). The flag is not consulted there. `ROLE_USER` and `ROLE_ADMIN` both receive `_ORDINARY_CAPABILITIES`, which includes `youtube.request` (`identity_access.py` lines 57–90). `PUBLIC_PUBLISHED_CAPABILITIES` is only `gallery.read` and `media.original.read` (lines 50–55). No mapped role lacks `youtube.request`, so there is no synthetic role to deny. The pinned origin does not add a capability. YouTube retry is unflagged, so a companion origin is rejected at the origin check before capability.

**A5 — accepted. YouTube-specific samples are not required.** Origin must equal the configured external origin, or the route must be flagged and the origin allowlisted (lines 1151–1162). A missing origin returns false. The header is checked only after the origin check, and only the exact value `1` authorizes (lines 1133–1141). `test_spoofed_or_absent_companion_origin_is_rejected`, `test_empty_companion_allowlist_rejects_extension_origin`, and `test_hostile_or_inexact_origin_is_rejected` exercise that shared predicate. The allowlist validator accepts only `chrome-extension://` plus 32 characters from `a-p`, and the default list is empty (`configuration.py` lines 85, 334, 526–544). An empty allowlist therefore rejects the extension origin on a flagged route as well. YouTube does not have a second origin helper.

**A6 and the F4 message part — accepted.** `companion_host.js` `onMessage` returns unless the window is framed, `event.origin` equals `PINNED_EXTENSION_ORIGIN`, and `event.source` is the parent window, before the type switch (lines 69–110). `open_upload` then notifies listeners with no weaker check. The sidebar posts `open_upload` only when `storedOrigin`, `handshakeSeen`, and `acceptKronikaOrigin(storedOrigin)` all hold (lines 1038–1046). `handshakeSeen` is set on `web_ready` or `host_ack` (lines 1008–1016) and cleared when the frame is rehosted (lines 806–811). `postToFrame` also requires `acceptKronikaOrigin` (lines 823–827). The shell calls `openUploadDialog` only when `#upload-open-button` exists and is not hidden (`app.js` lines 11297–11301). `applyIdentityCapabilities` sets that hidden flag from `upload.submit` (lines 495–499).

The plan says `tests/companion_web_bridge.test.js` pins the origin constant only. The file also refuses a foreign origin and a non-parent source on this same `onMessage`, including through `assertHostRefuses` and the `open_details` cases. `open_upload` itself is not named. That is a non-blocking pin. The button's presence remains E2; this audit accepts only the message behavior.

**A7 — accepted.** The added content-script matches are exactly `https://www.youtube.com/*` and `https://m.youtube.com/*` (`manifest.json` lines 34–38). `permissions` remains `alarms`, `sidePanel`, `storage`. `optional_host_permissions` remains `https://*.ts.net/*`. There is no `host_permissions` key. `tests/x_companion_extension.test.js` pins those permission facts and the first content-script matches, and does not pin the new matches array. A `git diff -U0` of the manifest shows the description sentence and that new matches block. The `key` field is absent from that zero-context diff, so it is unchanged. Its value was not copied. `music.youtube.com` and `youtu.be` are accepted by `acceptYouTubeVideoUrl` and are absent from the content-script matches. The smallest pin is one deep equality on the new matches array. It is non-blocking.

**A8 — accepted.** A zero-context diff of the range, excluding the icon blobs, matched no token, cookie, bearer, private-key block, private address, or private host. The hits were a URL-parser `password` rejection, the word "tokens" in a CSS note, the public video id `jNQXAC9IVRw`, and the welcome placeholder `https://your-server.your-tailnet.ts.net`. That placeholder is a generic example, not a host identifier. The gitignored companion private key was not read. The manifest `key` value is not in this report.

**B5 — accepted.** `youtube_adapter.js` talks to the extension only through `chrome.runtime.sendMessage`. It does not read cookies, `localStorage`, sessions, profiles, tabs, or history, and it does not select a model or call a provider. `saveYouTube` and `pollYouTube` fetch the configured Kronika origin through `fetchJson`. That fetch does not set `credentials: "include"`. A busy or done click returns before another `SAVE_YOUTUBE`. A poll transport failure schedules another poll message, which is a GET of `/api/youtube/requests/{id}`, not another POST.

**C4 — accepted.** `generate_one` calls `_ensure_cache_root_outside_source_roots` before `self._cache.publish` (`gallery_preview.py` lines 229–247). The guard resolves the cache root and every library root and raises `GalleryPreviewUnavailableError` when the cache root equals a library root or is inside one (lines 361–374), which includes `/srv/media` when that path is a registered library root. `Path.resolve` follows a symlink that already exists at check time. `GalleryPreviewBackfillCoordinator._run_pass` calls `plan_generate` and `generate_one` only (`gallery_preview_backfill.py` lines 131–167). It does not write the catalog database. Production constructs `FilesystemGalleryPreviewCache` from `gallery_preview_cache_path` and passes that service to the coordinator (`application.py` lines 769–787).

No allowlisted test names this guard. That pin is non-blocking. The guard returns without raising when `cache.root` is absent, and the filesystem cache class is outside the allowlist, so this audit did not confirm the attribute name. That is a limitation, not a failed claim: the stated fail-closed behavior is the branch that sees a root.

## Changed files

None in `cisarik/kronika`. No report file was written.

## Tests and validation

Repository gate only. The focused pytest route and `node --test` were not run. Reading the allowlisted source and the named tests closed A1–A8, B4, B5, C4, and the F4 message part. Known macOS failures were not re-executed.

## Commit and push

Not authorized. Not performed.

## Non-blocking pins

These do not block acceptance:

- A2/A5: the same companion-header negative on POST `/api/youtube/requests/{id}/retry` and POST `/api/uploads`.
- A3/B4: an audit-row assertion for `youtube.request.submit`; a 400 assertion that a missing confirmation, a non-interactive value, and `yes_flag` do not call `submit`; a Node assertion of the worker body literal.
- A6/F4: one `open_upload` case on the existing bridge refusal helper, plus the sidebar handshake guard.
- A7: deep equality of the new content-script matches array.
- C4: one allowlisted unit test that a cache root inside a library root raises before publish.

## Limitations

`FilesystemGalleryPreviewCache` was not opened. The public-published application factory was not opened. `extension/content/x_adapter.js` and `src/kronika/adapters/api/youtube_browser_api.py` were not needed and were not read. The upload control in `index.html` has no `hidden` attribute until `applyIdentityCapabilities` runs. A pinned-extension `open_upload` that arrived in that interval would see the control as visible. A hostile page origin is still rejected before that check, and POST `/api/uploads` stays unflagged and capability-checked. That interval was not dynamically reproduced.

## Out-of-scope ledger candidates

`tests/unit/test_gallery_preview.py` defines `test_cache_writes_cannot_occur_inside_registered_source_root`. That file is outside the allowlist. It was not read, not executed, and is not acceptance evidence. E2 rows were not audited.

## Residual-risk summary

No acceptance-blocking finding. The unpinned tests are info and may be Orchestrator-accepted inside the later documentation session. The unverified cache `root` attribute and the pre-identity upload-button interval are info. Neither was demonstrated. Medium or higher residual risk is not presented for Cooperator acceptance. Documentation still owes the 400 status, not 422.

## Deviations

None. The report was returned in this session and was not persisted.

## One smallest next step

Accept this E3 result and issue the documentation grant. Do not deploy. Do not open a security-boundary correction for the named pins.

```text
Orchestration critique:
MEASURED: the plan's A3 pass criterion says an omitted confirmation is 422; youtube_request_api.py _read_json_model returns 400 on ValidationError before service.submit (lines 369–376). Effect: the fixed claim holds, and a later document must say 400. Smallest correction: the documentation grant records 400.
LEAD: FilesystemGalleryPreviewCache may not expose root, which would make _ensure_cache_root_outside_source_roots return before publish; cheapest useful check is to read that class's root attribute, or to execute the out-of-allowlist cache-inside-root test under a later grant.
```

Resolved Execution Issues / Near-Misses: an ancestor probe used the truncated name `8cbbcadc` and failed as an invalid object. The full base `8cbbcad947964d711ebc2001e1c80976c4f82e24` was then read and the path set matched. Residual risk: none.

Pre-Existing Failure Classification: none

Authority expiry: this terminal report ends the grant. No autonomous continuation, correction, or deployment.
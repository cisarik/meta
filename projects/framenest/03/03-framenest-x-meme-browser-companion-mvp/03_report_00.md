### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
```

## Terminal status

`PASS`

## Phase-qualified result

`acceptance-PASS`

## Logical-whole closure

`not-closed`

Acceptance PASS is not publication, deployment, production acceptance, or
ORCHESTRATOR closure.

## Capability handshake

| Item | Classification | Value |
| --- | --- | --- |
| Client/model | inferred; not independently attested | Session identity text names Cursor Grok 4.6. No independent model attestation was available. |
| Requested High reasoning | requested | Prompt requested High. Actual runtime reasoning tier is unknown/not observably exposed. |
| Native planning mode | requested and followed | `not-used`. Plan Mode was not entered. |
| Filesystem read scope | directly observed | Read-only inspection of `/home/agile/Projects/framenest` and pinned `.ap`. Meta write limited to this report path. |
| `ap project check` / `ap exec` | directly observed | Available and used with `--baseline bfad16b718e135b272a3b0293bb37ddc3101ba49`. |
| `node --test` | directly observed | `/usr/bin/node` v26.4.0. |
| `git ls-remote` | directly observed | Credential-free HTTPS read of the two public `main` refs. No fetch. |
| Chrome | directly observed | `google-chrome-stable` 141.0.7390.76. |
| ffmpeg | directly observed | `/usr/bin/ffmpeg` present; not invoked. |
| Mutation / push / NUC / sudo / providers / signed-in Brave or X | requested unauthorized | Technically possible in the ambient host; not authorized and not exercised. |

Internal delegation, sub-agents, Explore tasks, and hidden secondary
workstreams were not used.

## Verified candidate identity

All restoration-gate facts matched the prompt. Working tree remained clean
except the expected gitignored private key.

```text
Canonical root: /home/agile/Projects/framenest
Branch: feat/x-meme-browser-companion
HEAD: bfad16b718e135b272a3b0293bb37ddc3101ba49
parent: 0cf6919a889dc4c6919d843a24cee2bb43fb4bfc
tree: 65ac2469a8212d17c48ae17e37314e03a1ad4f91
subject: docs: record X companion origin trust and operator setup
local main: 3cf22b8aaff61ed71093207d5b24aae622f394ac
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
.ap HEAD: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
schema head: 0028 (no new Alembic revision)
upstream: none
public cisarik/framenest refs/heads/main: 3cf22b8aaff61ed71093207d5b24aae622f394ac
public cisarik/ap refs/heads/main: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

Four-commit unpublished ancestry versus the accepted public baseline:

```text
bfad16b718e135b272a3b0293bb37ddc3101ba49  docs: record X companion origin trust and operator setup
0cf6919a889dc4c6919d843a24cee2bb43fb4bfc  feat: add FrameNest X meme browser companion extension
8584d1006c7684656a6582db04a0d3f4ee57e554  feat: add requester-private X companion meme picker
52b68384c2cbf29f12ed50d26ec1c02b7cd6dcc8  feat: allow exact companion extension origins on X request mutations
3cf22b8aaff61ed71093207d5b24aae622f394ac  docs: adopt AP 9c5cc44 pin
```

`git diff --name-status 3cf22b8aaff61ed71093207d5b24aae622f394ac..HEAD`
equals the expected allowlist. No extra path, no missing expected path, no
`.ap` movement, no `pyproject.toml` / `poetry.lock` / `web/app.js` change,
and no committed private key. `private/companion-extension.pem.key` is
ignored by `.gitignore:/private/` and is not in the Git tree.

`./.ap/ap exec --operation runtime-info` printed
`/home/agile/Projects/framenest/src/framenest/__init__.py`.

This Worker changed no candidate files. Start and end repository commit are
the same SHA above.

## Control-matrix results

### 9.1 Provenance — pass

Exact SHA, parent, tree, subject, four-commit ancestry, `.ap` pin, unpublished
versus public `main`, and clean tree were directly observed. No extra commits,
rewritten history, overlapping dirty mutation, `.ap` movement, or dependency
pin change.

### 9.2 Ingress origin allow/deny — pass

`RoutePolicy.companion_mutation` is true only on `POST /api/x/requests` and
`POST /api/x/requests/{claim_id}/retry`. `_mutation_origin_allowed` accepts
`Origin == external_origin`, or a flagged companion mutation whose Origin is
in the exact `chrome-extension://` + 32 `[a-p]` allowlist. Empty allowlist,
spoofed Origin, and absent Origin fail closed. Unsafe methods still require
`X-FrameNest-Request: 1`. Tailscale identity, `x.request`, and audit remain
on those routes. `GET /api/x/companion/media` is not companion-flagged.
Responses add no CORS headers. Named ingress tests passed.

### 9.3 Web UI regression — pass

Ordinary web mutations still require `Origin == external_origin` and
`X-FrameNest-Request: 1` when companion origins are configured
(`test_web_ui_mutation_path_is_unchanged_when_companion_origins_are_configured`).
`web/app.js` and Gallery/Details files are absent from the candidate diff.

### 9.4 Private-media non-enumeration — pass

Picker audience is `published OR own cataloged X asset` keyed only from
verified `identity.login_key`. The HTTP handler has no owner query parameter;
`owner` / `created_by` cannot name another requester. Foreign users cannot
list another requester's unpublished X meme. Direct `GET /api/media/{id}`
404 semantics for unpublished foreign items remain 404. Content, preview, and
download routes were not widened in this diff; `GET /api/media` still uses
`published_only=True` in the ordinary catalog query. JPEG/PNG remain in
`SUPPORTED_MEDIA_CONTENT` and the picker attachable-location filter.

### 9.5 Arbitrary-proxy negative control — pass

The service worker builds URLs from `pathFor` templates and validated UUIDs.
Content-script messages cannot supply a fetch URL. Unknown protocol versions
and types are dropped. Production `extension/manifest.json` has permissions
`sidePanel` and `storage` only; no `host_permissions`, `<all_urls>`,
`cookies`, `tabs`, or `externally_connectable`. Optional host permission is
only `https://*.ts.net/*`. The gated browser suite copies a disposable
loopback `host_permissions` grant into a temp directory; that grant is not in
the committed manifest.

### 9.6 No auto-submit — pass

Adapter contract v1 has no Post control. Attach uses `File` / `DataTransfer`
on a file input and a `change` event. Adapter source has no `tweetButton`,
`form.submit`, or submit dispatch. Browser evidence recorded
`submitted === false` for Post click and form submit listeners.

### 9.7 Recoverable request state and bounds — pass

In-flight claim IDs persist in `chrome.storage.local` (`inflightClaims`, cap
16) and are recovered via `RECOVER_INFLIGHT` after content-script restart.
The service worker has no `setInterval` and no long timeout loop as the only
recovery path. Attach is capped at 32 MiB in both header check and streaming
read. Page-driven `setTimeout` polling lives in the content script, not as
MV3 worker liveness.

### 9.8 Affected tests — pass

All Section 8 Python modules and both JS suites were re-run. Exact commands
and exit codes are below. Named tests remained present and meaningful:

- `test_companion_origin_is_accepted_only_on_flagged_x_request_routes`
- `test_empty_companion_allowlist_rejects_extension_origin`
- `test_spoofed_or_absent_companion_origin_is_rejected`
- `test_web_ui_mutation_path_is_unchanged_when_companion_origins_are_configured`
- `test_foreign_user_cannot_enumerate_another_requesters_private_meme`
- `test_owner_query_parameter_cannot_name_another_requester`
- `adapter contract has no Post-button or auto-submit path`
- `service worker path templates reject caller-supplied URLs and ids`

### 9.9 Browser evidence — pass

Gated suite ran once and passed. Independently observed:

- disposable extension loaded through CDP `Extensions.loadUnpacked`, not
  `--load-extension`;
- loaded id `omiihmnlkmieaafaphohakcgmbggppap`;
- POST probe Origin `chrome-extension://omiihmnlkmieaafaphohakcgmbggppap`
  with `X-FrameNest-Request: 1`;
- synthetic `DataTransfer` attach of `meme.jpg` without Post click or form
  submit;
- committed production manifest still lacks `host_permissions`.

Worker 02 claims that Chrome 141 ignores `--load-extension` and that
extension GET to loopback omitted Origin were treated as claims. Direct
observation of the current suite: Chrome 141.0.7390.76 is present; the
current harness uses pipe CDP `Extensions.loadUnpacked` and records POST
Origin. The current suite does not assert GET Origin. No harness repair.

Browser Stall Guard was not triggered (first run succeeded).

```text
Failure episode identity: companion-acceptance-browser-01
Prior episode identity: none
Episode relationship: initial
Result claimed from missing evidence: none
```

### 9.10 Changed-path and cleanliness review — pass

Diff equals the expected path set. ADR-0061 and `docs/X_COMPANION.md` exist.
`deploy/systemd/framenest.env.example` and the NUC runbook keep
`FRAMENEST_COMPANION_EXTENSION_ORIGINS` as a commented placeholder. Rollback
remains emptying that allowlist. No secrets, real tailnet hostnames, private
key, media bytes, or AP ledger edits are in the candidate. The committed
manifest `key` is the public development key used to pin the unpacked id.

X-PHOTO-01 (c) is residual documentation truth, not an acceptance failure:
`yt-dlp==2026.7.4` remains pinned and unchanged; the X downloader still
records that the extractor filters `m['type'] != 'photo'`; docs advertise
photo Save as deferred / `X_NO_SUPPORTED_MEDIA`, not implemented. Existing
catalog JPEG/PNG remain picker-eligible.

## Commands actually run

All Python evidence used `--baseline bfad16b718e135b272a3b0293bb37ddc3101ba49`.
No raw `.venv/bin/python`, `python`, `python3`, or `poetry run` was used for
Python evidence.

```text
./.ap/ap project check --root /home/agile/Projects/framenest --baseline bfad16b718e135b272a3b0293bb37ddc3101ba49
exit 0
note: WARN sanitized inherited environment classes: LD_LIBRARY_PATH VIRTUAL_ENV_DISABLE_PROMPT PROMPT_COMMAND APPDIR APPIMAGE PATH
result: ap project check --baseline: PASS

./.ap/ap exec --root /home/agile/Projects/framenest --baseline bfad16b718e135b272a3b0293bb37ddc3101ba49 --operation runtime-info
exit 0
framenest.__file__: /home/agile/Projects/framenest/src/framenest/__init__.py

./.ap/ap exec --root /home/agile/Projects/framenest --baseline bfad16b718e135b272a3b0293bb37ddc3101ba49 --operation test-focus -- tests/unit/test_configuration_ingress.py tests/unit/test_companion_picker.py tests/contract/test_x_route_policy.py tests/contract/test_fedora_systemd_service.py tests/contract/test_media_catalog_repository.py tests/contract/test_x_companion_api.py tests/contract/test_tailscale_ingress_security.py -q -p no:cacheprovider
exit 0
160 passed in 37.56s

node --test tests/x_companion_extension.test.js
exit 0
7 pass, 0 fail

FRAMENEST_RUN_BROWSER_EVIDENCE=1 node --test tests/browser_companion_evidence.test.js
exit 0
1 pass, 0 fail, duration_ms 1097
```

Credential-free public-ref commands (no fetch):

```text
git ls-remote https://github.com/cisarik/framenest.git refs/heads/main
3cf22b8aaff61ed71093207d5b24aae622f394ac	refs/heads/main

git ls-remote https://github.com/cisarik/ap.git refs/heads/main
9c5cc44f8b6c92dd56ad2427d13223d7d59c5656	refs/heads/main
```

## Browser evidence performed and not performed

Performed: one gated synthetic loopback Chrome run of
`tests/browser_companion_evidence.test.js` as authorized.

Not performed: signed-in Brave profile, live X, DMs, Post click, provider
calls, NUC access, Playwright-as-authority, npm, or a full pytest suite.

## First causal finding

`none`

## Residuals that remain owned

- X-PHOTO-01 outcome (c): static X-photo Save remains unsupported under
  pinned `yt-dlp==2026.7.4`; documented, not advertised as implemented.
- SPIKE-X-01 live signed-in X DOM evidence is not in this grant.
- `boundTabId` remains in-memory in the service worker.

## Resolved Execution Issues / Near-Misses

- Ambient AppImage/PATH classes were present in the Worker shell and were
  reported then stripped by `ap exec`. Python evidence used the sanitized
  envelope, not ambient Python.
- Chrome 141 is the host browser. The current suite does not depend on
  `--load-extension`; it uses `--enable-unsafe-extension-debugging` and CDP
  `Extensions.loadUnpacked`. First-run pass; no stall-guard recovery.

## Pre-Existing Failure Classification

No candidate defect. X-PHOTO-01 (c) is a pre-existing extractor limitation
carried as residual documentation truth.

## One smallest next step

ORCHESTRATOR reconciles this independent `acceptance-PASS` against the
unpublished candidate `bfad16b718e135b272a3b0293bb37ddc3101ba49` and, if
accepted, issues a later exact grant for publication, NUC deployment, and/or
Cooperator signed-in Brave/X. Do not close the logical whole from this
report.

## Report justification

`final-acceptance`

## Authority expiry

All authority granted by prompt FN-X-MEME-COMPANION-ACCEPT-03 expires with
this terminal report. No mutation, correction, push, publication, deployment,
NUC access, provider use, signed-in Brave/X, AP mutation, or logical-whole
closure is authorized from this session.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 08
Worker exchange ordinal: 01
```

Terminal status: `PASS`
Phase-qualified result: `implementation-PASS`
Logical-whole closure: not-closed
Report justification: new-mutation

## Capability handshake

| Item | Classification | Value |
|---|---|---|
| Product/client | requested | Cursor Worker session |
| Product/client | directly observed | Cursor IDE session on Linux |
| Model identity | directly observed as session claim, not independently attested | Cursor Grok 4.6 |
| Reasoning | requested | High |
| Reasoning | unknown/not observably exposed | no separate High/Extra High control was visible in this session |
| Native planning mode | requested | `not-used` |
| Native planning mode | directly observed | `not-used` (Plan Mode was not entered) |
| Filesystem containment | directly observed | writable canonical checkout `/home/agile/Projects/framenest` |
| Meta write scope | requested | only `08_report_00.md` |
| Source inspect/edit | directly observed | allowlisted extension/test/doc paths |
| JS tests | directly observed | `node --test tests/x_companion_extension.test.js` |
| Local commit | directly observed | one commit on `feat/x-meme-browser-companion` |
| Public-ref `ls-remote` | directly observed | `origin/main` `bfad16b718e135b272a3b0293bb37ddc3101ba49` |
| Push / NUC / sudo / provider / signed-in browser / Python pytest / AP mutation | requested forbidden | unauthorized even if technically possible; not used |

`private/companion-extension.pem.key` exists as gitignored (`/private/`). It was listed by metadata only and was not read.

## Repository gate

- Root: `/home/agile/Projects/framenest`
- Origin: `https://github.com/cisarik/framenest.git` (accepted spelling)
- Branch: `feat/x-meme-browser-companion`
- Baseline HEAD: `14c8a7098e41fa9602c1c45bbf3f2207f6001400`
- Baseline parent: `4a7fd25f26ce4446c48123f34bb3e11694b23e8b`
- Baseline tree: `5192e1d6742f76fa2286a8f8f3de302a0805b747`
- Baseline subject: `style: apply FrameNest gallery tokens to the X companion`
- `.ap` gitlink: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (unchanged)
- Public `main` (informational): `bfad16b718e135b272a3b0293bb37ddc3101ba49`
- Pre-mutation status: clean tracked tree; ignored private key only
- Overlap: none

## Candidate

- Final HEAD: `572c6d4e239a65cd4457061d0cdd59c46c1ba2a7`
- Parent: `14c8a7098e41fa9602c1c45bbf3f2207f6001400`
- Tree: `35e064923497d475ec80eb1f426a371f75c48a3a`
- Subject: `fix: hide origin setup behind companion Settings`
- Push: not performed (forbidden)
- Final status: clean working tree on `feat/x-meme-browser-companion`

### Changed paths

| Path | Purpose |
|---|---|
| `extension/content/x_adapter_contract_v1.js` | Frozen `contentDisclosureSelectors` on adapter version 1 |
| `extension/content/x_adapter.js` | Disclosure-adjacent Attach icon; skip if no toolbar and no disclosure; 3px Save downward nudge |
| `extension/ui/picker.html` | Search-first home, Settings control, Origin-only Settings dialog |
| `extension/ui/picker.css` | Copied Status-dialog tokens/rules; header Settings; compact search refresh |
| `extension/ui/picker.js` | Auto-open Origin sheet when disconnected; hide origin chrome after connect; textContent-only status |
| `tests/support/x_fixtures/composer.html` | Content disclosure control in the synthetic toolbar |
| `tests/x_companion_extension.test.js` | Fail on Search titles, labeled Attach pill, missing disclosure/Settings/Origin |
| `docs/X_COMPANION.md` | One operator sentence for icon, Settings origin, Search memes |

No other path changed. Service worker `openPicker` left as-is.

## Disclosure insertion and Settings behavior

Composer Attach:

1. Resolve the composer toolbar as before.
2. Prefer `[aria-label='Content disclosure']` / `[data-framenest-content-disclosure]` inside that toolbar; if the toolbar selector missed, find disclosure from the composer region and use its icon row.
3. Walk up to the disclosure column wrapper and `insertAdjacentElement("afterend")`.
4. If disclosure is missing, append the same 36px transparent accent icon as the last toolbar cluster child.
5. If neither toolbar nor disclosure exists, skip that composer. No Post selector, no article-append, no unscoped x.com stylesheet.

The control keeps `data-framenest-companion="attach"`, `aria-label`/`title` `Attach from FrameNest`, halt on click, and the existing ACK/`openPicker` side-panel path. Visible toolbar text is not set.

Picker:

- Header: FN mark + FrameNest title left; muted outlined sliders Settings control right.
- Connected, or when `frameNestOrigin` is already stored: origin input, Connect, Reset, and setup status are only in the Settings sheet; home is search + kind filter + compact preview; placeholder/`aria-label` **Search memes**.
- Disconnected / first run: search home remains visible; Settings opens automatically on Origin.
- Successful Connect closes the sheet and focuses search.
- Reset clears results and reopens Settings on Origin.
- Close, backdrop click, and Escape hide the sheet without resetting origin.

## Copied Status-dialog tokens and rules

Copied values into `picker.css` `:root` (web files untouched):

- `--surface-solid: #111815`
- `--line: rgba(58, 78, 62, 0.45)`
- `--line-strong: rgba(88, 118, 96, 0.6)` (required by `.settings-dialog` border)
- `--radius-lg: 12px`
- `--radius-md: 8px` (required by `.settings-dialog__note`)
- `--shadow-deep: rgba(0, 0, 0, 0.65)`
- `--danger-soft: rgba(255, 77, 77, 0.12)`
- `--transition-fast: 150ms ease`

Copied rule families: `dialog:not([open])` / `dialog[open]`; `.settings-dialog`; `::backdrop`; `__header`; `__title`; `__close`; `__tabs`; `__tab`; `__tab--active`; `__body`; `__section`; `__section-title`; `.settings-status-list`; `.settings-status-list div/dt/dd`; `--wrap`; `__note`. Side-panel padding uses the gallery 620px compact values. Tablist has one Origin tab with green underline; no fake extra tabs.

## Validation

```text
node --test tests/x_companion_extension.test.js
```

Exit 0. 12 passed, 0 failed.

Browser evidence: not performed. Live Brave/X look remains Cooperator-owned after reload.

## Commands actually run

| Command | Exit |
|---|---|
| Read-only Git identity / status / `ls-remote origin refs/heads/main` / `.ap` gitlink | 0 |
| `node --test tests/x_companion_extension.test.js` | 0 |
| Exact-path `git add` + one local `git commit` | 0 |
| Post-commit `git status` / `rev-parse` / `ls-files -s .ap` | 0 |

Not run: `git fetch`, push, pytest, `ap exec`, Python, NUC/SSH/sudo, Playwright, live x.com, GUI launch.

## Security / privacy residuals

- No Post / `form.submit` / auto-submit path; adapter still must not contain `tweetButton`.
- Content script still does not fetch FrameNest; titles/origin/status use `textContent`.
- Companion private key remains gitignored and unread.
- `X_REQUEST_NOT_CONFIGURED` / companion-origin host configuration was not touched.
- Save still uses the existing Share-measurement path, plus a 3px downward nudge (`SAVE_DOWN_NUDGE_PX`). Live alignment remains Cooperator-owned.

## Resolved Execution Issues / Near-Misses

none material. Unused attach-pill constants (`GALLERY_ACCENT_BORDER`, `GALLERY_RADIUS_SM`, `GALLERY_FONT_MONO`) were removed from the adapter after the icon replacement so the labeled-pill chrome could not remain as dead style.

## Pre-Existing Failure Classification

none

## Smallest next step

Michal reloads the unpacked extension, checks the disclosure-adjacent composer icon, Connect-then-hidden-origin, the Settings/Origin sheet, and the Search memes prompt.

## Authority expiry

Authority granted by Worker 08 exchange 01 expires with this terminal report. Implementation-PASS is not live Brave/X certification, publication, deployment, or ORCHESTRATOR closure.

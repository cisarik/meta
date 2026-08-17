### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 10
Worker exchange ordinal: 01
Status: PASS
Phase-qualified result: Implementation PASS
```

Correction PASS is not live Brave/X certification, publication, deployment, or
closure.

## Capability handshake

```text
Requested reasoning: High
Observed reasoning: High (not independently attested)
Requested native planning mode: not-used
Observed native planning mode: not-used
Requested model identity: not independently verified
Observed model identity: Cursor Grok 4.6 (self-reported; not independently attested)
Independence required: no
Evidence posture: non-independent
Writable scope: Section 11 allowlist only
Python / ap exec / pytest: unauthorized
Push / NUC / sudo / signed-in browser: unauthorized
```

## Repository gate

```text
Canonical repository: /home/agile/Projects/framenest
Origin: https://github.com/cisarik/framenest.git
Branch: feat/x-meme-browser-companion
Start commit (exact baseline): 9cec59803a0c00d15e6a1fb84a651ec667236508
Start tree: 1a52d64c20feafcb18bda9b9d4ff20ba47a8f29e
Baseline parent: 572c6d4e239a65cd4457061d0cdd59c46c1ba2a7
End commit: cfbc45dbe8627c3b048cca366964467703dd65e5
End tree: 9298bc7c1f34eb44243a82b1c7b13dc1d48e7a1e
Pinned AP gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Informational ls-remote origin refs/heads/main: bfad16b718e135b272a3b0293bb37ddc3101ba49
Working tree after commit: clean
Ignored untracked residual: private/companion-extension.pem.key (gitignored via /private/; not read)
```

Public `main` behind this branch is expected. `git fetch` was not run.

## What changed

One local commit moves media Save to the bottom-right tile corner, places Attach
inline on the focused reply text row, and opens the existing picker as an
in-page popup above that button.

### Save corner

Injected Save style is `bottom: 0; right: 0` (not `top`/`left`). Hover /
focus-within visibility, black fill, green border, and green plus are unchanged.
SAVE_POST still submits the post permalink. Text-only posts still have no Save.
Residual: not per-asset.

### Attach focus rule

Attach is `data-framenest-companion="attach"` with `aria-label` `Attach from
FrameNest`. It is appended to the composer text row (right of "Post your
reply"), not the toolbar and not flush on the whole card. It is hidden until
the composer editable or chrome receives `focusin`. It stays visible while the
popup is open. It hides when focus leaves the composer and the popup is closed.
It is not shown on mouseover. Host click is halted. Missing chrome or a missing
distinct text row skips that composer. No `tweetButton` path.

### Popup positioning rule

Attach click no longer sends `openPicker`. The content script mounts a host
node with a closed shadow root and an iframe of `chrome.runtime.getURL("ui/picker.html")`.
The host is `position: fixed`, right-aligned to the Attach button via
`getBoundingClientRect`. Prefer above the button; if there is not enough space
above, flip below. Reposition on `resize` and capturing `scroll`. Close on
Escape, mousedown outside the popup and button, and a shadow close control.
Close does not reset origin. Picker protocol is unchanged. Content script still
does not fetch FrameNest or X CDN URLs. Side panel remains in the manifest and
is not this attach surface.

### WAR residual

`web_accessible_resources` lists only `ui/picker.html`, `ui/picker.css`, and
`ui/picker.js`, matched only to `https://x.com/*` and `https://twitter.com/*`.
No `<all_urls>`. No FrameNest `ts.net` in WAR. Residual: any script on those
hosts could iframe the picker document; the picker still has no X cookies and
still only talks to the service worker.

`extension/background/service_worker.js` was not edited. `openPicker` remains
dead for this attach path.

## Changed paths

```text
docs/X_COMPANION.md
extension/content/x_adapter.js
extension/content/x_adapter_contract_v1.js
extension/manifest.json
tests/support/x_fixtures/composer.html
tests/x_companion_extension.test.js
```

Allowlisted and unchanged: `extension/ui/picker.html`, `extension/ui/picker.css`,
`extension/ui/picker.js`. Adapter contract version remains `1`.

## Validation

```text
Command: node --test tests/x_companion_extension.test.js
Exit: 0
Result: 13 pass, 0 fail
```

Tests fail if Save overlay style is still `top: 0` / `left: 0`; if attach still
calls `openPicker`; if popup host / closed shadow / picker iframe / WAR is
missing; if `tweetButton` / `form.submit` appears in adapter source; if Search
titles returns. No gated Chrome evidence. No live x.com scrape. No auto-Post.

## Git result

```text
Commit: cfbc45dbe8627c3b048cca366964467703dd65e5
Subject: fix: open attach picker as an in-page popup above the composer
Amend: not used
Push: not performed (forbidden)
```

## Deviations, risks, missing evidence

- No live signed-in Brave/X UX evidence. Fixture and source tests only.
- WAR residual as above.
- Per-asset SAVE_POST and static-photo acquisition remain out of scope.
- Live X text-row geometry may still clip or displace the inline +; owner
  visual acceptance is required.

Resolved Execution Issues / Near-Misses: first test run failed because popup
host used `style.background = "transparent"`, colliding with the existing Save
negative assertion against transparent backgrounds. Removed that host style
(div default is already transparent) and re-ran the same authorized test
command once; 13/13 pass.

Pre-Existing Failure Classification: none

## Closure and next step

```text
Logical-whole closure: not-closed
Report justification: new-mutation
Authority expiry: this terminal report expires Worker 10 exchange 01
```

Smallest next step: Michal reloads the unpacked extension, focuses a reply
composer, clicks the inline +, checks that the FrameNest search popup opens
above that button, and confirms hover + is bottom-right on images.

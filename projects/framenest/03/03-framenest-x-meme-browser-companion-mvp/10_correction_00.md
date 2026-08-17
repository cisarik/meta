# Authoritative Prompt for Fresh Worker 10

## FrameNest × X Meme Browser Companion MVP — Bottom-right Save and in-page attach popup

You are a Worker instance assigned to WORKER. Read this complete prompt before
taking any action.

Worker 09 placed hover Save on each media tile (top-left) and Attach at the
composer card corner, commit
`9cec59803a0c00d15e6a1fb84a651ec667236508`. That authority is expired. The
COOPERATOR confirmed hover-per-image works and corrected a typo: the media
**+** belongs **bottom-right**. For reply, Attach must sit **inline on the
right of "Post your reply"** and appear when the user **clicks into** the
composer (not on mouseover). Clicking it must open a FrameNest search popup
**as part of the X page**, anchored **above that button**, not the side
panel.

This is not a continuation of Worker 09. Do not resume any prior Worker chat.
Do not enter Native Plan Mode. Do not implement static-photo acquisition,
per-asset SAVE_POST, NUC enablement, or iframe of the full FrameNest web
Gallery into the side panel.

```text
Role: WORKER
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 10
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Worker session profile: Bounded Correction Worker
Phase: implementation
Task identity: FN-X-MEME-COMPANION-UX-INLINE-POPUP-10
Task type: bounded visual-language correction
Native planning mode: not-used
Evidence posture: non-independent
Independence required: no
Authority renewal: not applicable — fresh Worker authority originates only in this prompt
Continuity anchor: none — do not resume Worker 09
Prior authorities: expired
```

```text
Implementation authority: explicit
Native planning mode: not-used
Worker session target: fresh-worker-session
Exact baseline: 9cec59803a0c00d15e6a1fb84a651ec667236508
Changed-path allowlist: Section 11
Implementation boundaries: Sections 7, 9, 10, 12, and 18
Independence required: no
```

```text
Acceptance candidate: 9cec59803a0c00d15e6a1fb84a651ec667236508
Acceptance owner map: media Save overlay corner; composer Attach inline visibility; in-page picker popup; optional WAR in manifest; fixture; tests; operator note
Acceptance allowlist: Section 11
Acceptance risk claims: media + is bottom-right hover-only; Attach is focus-visible inline right of the reply field; attach click opens an in-page popup above the button using existing picker chrome; WAR if used is match-limited to x.com/twitter.com; no Post/auto-submit; content script still does not fetch FrameNest or X CDN URLs; side panel is not the attach surface
Acceptance control matrix: positive — Save bottom/right; Attach on composer focus; popup host above button; negative — no Share-row Save; no tweetButton; no unscoped x.com restyle; no ts.net iframe
Acceptance independence: not-required
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: none
```

Reasoning recommendation: High. This is live X composer geometry plus an
in-page extension overlay (positioning, focus, WAR). Do not silently
downgrade. Do not use Extra High or Max. Michal controls the actual model,
client, and launch decision. No model or provider identity grants authority.

```text
COOPERATOR: Michal
ORCHESTRATOR: ORCHESTRATOR_CHAT
WORKER: this fresh bounded correction session
```

Internal delegation is inactive. Professional English in repo artifacts and
the terminal report. The report begins exactly:

```text
### Report for ORCHESTRATOR_CHAT
```

Correction PASS is not live Brave/X certification, publication, deployment, or
closure.

---

## 1. External trace and Meta write boundary

```text
External trace disposition: configured
Trace discovery: cisarik/meta repository path projects/framenest/03/03-framenest-x-meme-browser-companion-mvp
Trace project key: framenest
Trace logical-whole projection identity: 03/03-framenest-x-meme-browser-companion-mvp
Trace authority: historical-evidence-only
Trace archival owner: ORCHESTRATOR after the outcome exists
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
```

Write only:

```text
/home/agile/meta/projects/framenest/03/03-framenest-x-meme-browser-companion-mvp/10_report_00.md
```

Do not read Meta. Do not stage or commit Meta.

---

## 2. Communication routing

```text
Orchestrator: ORCHESTRATOR_CHAT
Worker prompt language: professional English
Worker report language: professional English
Direct-user Slovak presentation: Orchestrator-owned; do not emit the Cooperator capsule
Report header: ### Report for ORCHESTRATOR_CHAT
```

Parked for a later Orchestrator: full FrameNest web in the side panel
(almost a full page), web-header icon-only stacking, static photos,
per-asset Save, `X_REQUEST_NOT_CONFIGURED`. This Worker does not iframe
`https://*.ts.net`.

---

## 3. Capability handshake

Fresh session. Record requested vs observed model, High reasoning, Native
planning mode `not-used`, writable scope, tests, local commit, `ls-remote`.
Push / NUC / sudo / signed-in browser / Python / AP mutation remain
unauthorized. Do not print `SSH_AUTH_SOCK` or reconstruct `gpgconf`.

```text
Repeated-gate or reasoning-loop stop: configured
Broad gate: once per materially changed candidate
```

---

## 4. Repository identity and baseline

```text
Canonical repository: /home/agile/Projects/framenest
Working-copy topology: canonical checkout
Expected branch: feat/x-meme-browser-companion
Exact baseline: 9cec59803a0c00d15e6a1fb84a651ec667236508
Baseline parent: 572c6d4e239a65cd4457061d0cdd59c46c1ba2a7
Baseline tree: 1a52d64c20feafcb18bda9b9d4ff20ba47a8f29e
Baseline subject: fix: overlay Save on hover media instead of the Share row
Pinned AP gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

`git fetch` is forbidden. Public `main` behind this branch is expected.
Stop if HEAD is not the exact baseline. Do not create a branch, checkout
`main`, or push. List gitignored `private/companion-extension.pem.key` as
untracked-ignored; do not read it.

---

## 5. Mandatory reading

`AGENTS.md`, `.ap/AP_WORKER.md`, `docs/WORKER_EXECUTION_CONTRACT.md`,
`extension/content/x_adapter.js`, `x_adapter_contract_v1.js`,
`extension/ui/picker.html`, `picker.css`, `picker.js`,
`extension/manifest.json`, `extension/background/service_worker.js` (read;
edit only if Section 11 includes it), tests and fixture, `docs/X_COMPANION.md`.

Do not scrape live x.com. Do not edit frozen Gallery files.

Cooperator corrections:

1. Media **+** must be **bottom-right** of each tile (typo was top-left).
   Hover-per-image stays.
2. Reply Attach is **inline, right of "Post your reply"**, shown when the
   user **clicks into** the composer, not on mouseover.
3. Attach click opens a search popup **on the X page**, **above that
   button**. Side panel is no longer the attach surface.

---

## 6. Repository gate

Record root, origin, branch, SHAs, status, `.ap` gitlink, informational
`ls-remote` of `main`. Do not stash/reset/clean unrelated dirty state.

---

## 7. Canonical execution routes

JS/HTML/CSS/manifest/fixture/doc only. No raw Python, no `ap exec`, no
pytest.

```text
node --test tests/x_companion_extension.test.js
```

No gated Chrome evidence. No unscoped stylesheet restyling all of x.com.

---

## 8. Goal

One local commit that moves media Save to bottom-right, places Attach
inline on the focused reply row, and opens the existing picker as an
in-page popup above that button.

---

## 9. Required correction behavior

Keep adapter contract version `1`.

### 9.1 Media Save corner

In the injected companion style, Save is `bottom: 0; right: 0` (not
`top`/`left`). Hover / focus-within visibility, black fill, green border,
green plus, per-host injection, no Share-row Save, no Save on text-only
posts, SAVE_POST still the post permalink. Unchanged residual: not
per-asset.

### 9.2 Inline Attach on composer focus

- Place the same black/green plus on the **right of the reply/compose text
  row** (same row as "Post your reply"), not the bottom-left tool icons and
  not flush on the whole card if that fights the Reply CTA.
- **Not mouseover.** Visible when the composer editable (or its chrome)
  has focus (`focusin`). Hidden when focus leaves the composer **and** the
  popup is closed. While the popup is open, keep the button visible.
- `data-framenest-companion="attach"`, `aria-label` `Attach from FrameNest`.
- Halt host click. Bind composer + file input as today.
- Missing chrome: skip that composer. No `tweetButton` in source.

### 9.3 In-page popup above the button

On Attach click, **do not** send `openPicker` to open the side panel.

Open a FrameNest search popup as a page overlay:

- Host node on the document (prefer a closed **shadow root** so X CSS does
  not restyle it, and we do not restyle x.com).
- Content is the **existing** picker (`ui/picker.html` + css/js) via an
  iframe `chrome.runtime.getURL("ui/picker.html")`, **or** an equivalent
  in-shadow reuse that still talks only through `chrome.runtime` messages.
  Do not duplicate a second picker protocol.
- Position `position: fixed` **above** the Attach button (`getBoundingClientRect`),
  right-aligned to the button if practical. If there is not enough space
  above, flip below. Reposition on `resize` / `scroll`.
- Close on Escape, on mousedown outside the popup and button, and on a
  simple close control if you add one. Do not reset origin on close.
- Popup chrome is the compact search already built (Search memes, kind,
  preview, Attach). Settings may remain inside that picker document.

If the iframe approach is used, `manifest.json` **must** add
`web_accessible_resources` **only** for the picker files, **only**
`matches` `https://x.com/*` and `https://twitter.com/*`. Do not add
`<all_urls>`. Do not add FrameNest `ts.net` to WAR. Report the WAR as a
security residual: any script on those hosts could iframe the picker
document; the picker still has no X cookies and still only talks to the
service worker.

Do not change SAVE_POST. Do not fetch FrameNest from the content script.
Do not click Post.

`extension/background/service_worker.js` may stay unchanged if attach no
longer needs `openPicker`. Do not edit it unless a one-line no-op is
required and then **stop** — it is not on the allowlist.

### 9.4 Side panel

Leave the side panel entry in the manifest. It is not this attach path.
Do not load the full FrameNest web app into the side panel in this grant.

### 9.5 Tests and docs

Tests must fail if Save style is still `top: 0` / `left: 0` as the overlay
anchor; if attach still calls `openPicker`; if popup host / WAR (when used)
is missing; if `tweetButton` / `form.submit` appears; if Search titles
returns.

Short `docs/X_COMPANION.md` note: media + bottom-right hover; attach is
inline on composer focus and opens an in-page popup. Do not expand.

---

## 10. Positive authority

Mutate Section 11 only; `node --test tests/x_companion_extension.test.js`;
read-only Git; one local commit; write `10_report_00.md`.

---

## 11. Changed-path allowlist

```text
extension/content/x_adapter.js
extension/content/x_adapter_contract_v1.js
extension/ui/picker.html
extension/ui/picker.css
extension/ui/picker.js
extension/manifest.json
tests/x_companion_extension.test.js
tests/support/x_fixtures/composer.html
docs/X_COMPANION.md
```

`manifest.json` only for match-limited `web_accessible_resources` if the
iframe picker is used. No other path.

---

## 12. Negative authority

No frozen Gallery files; no Python / yt-dlp / NUC; no SAVE_POST media-URL
shape; no content-script FrameNest or X CDN fetch; no `ts.net` iframe; no
`<all_urls>` WAR; no CORS / cookies / auto-Post; no live x.com scrape; no
pytest / `ap exec`; no fetch/stash/reset/rebase/amend/push; no `git add .`;
no `.ap/` mutation; no Meta except the report; no logical-whole closure.

---

## 13. Git authority

```text
Fetch: forbidden
Branch: existing feat/x-meme-browser-companion at the exact baseline
Stage: exact allowlisted paths only
Commit: one coherent local commit after tests pass
Amend: forbidden
Push: forbidden
```

Example subject:

```text
fix: open attach picker as an in-page popup above the composer
```

---

## 14–16. Boundaries and validation

Untrusted X DOM. Fixture/source evidence only. `node:test` on
`tests/x_companion_extension.test.js`. No live UX PASS claim.

---

## 17. Completion, report, and expiry

Report starts with `### Report for ORCHESTRATOR_CHAT` and echoes the three
coordinates once. Include SHAs, WAR residual if any, popup positioning
rule, Save corner, Attach focus rule, commands/exits, no-auto-Post,
`Logical-whole closure: not-closed`, `Report justification: new-mutation`,
next step = Michal reloads, focuses reply, clicks the inline +, checks
popup above the button and hover + bottom-right on images.

---

## 18. Stop conditions

Stop if HEAD is not baseline, allowlist is insufficient, WAR would need
`<all_urls>`, popup would require content-script `fetch` to FrameNest, or
Post selector / live x.com scrape is required.

---

## 19. Authority summary

This prompt authorizes Worker 10 to move media Save to bottom-right, show
Attach inline when the composer is focused, and open the existing picker as
an in-page popup above that button, from baseline
`9cec59803a0c00d15e6a1fb84a651ec667236508`, one local commit, and
`10_report_00.md`.

It does not authorize full-web side panel, per-asset download, static
photos, NUC, push, publication, or closure.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 09
Worker exchange ordinal: 01
```

Terminal status: `implementation-PASS`
Logical-whole closure: not-closed
Report justification: new-mutation
Authority: expired with this report

This was a fresh bounded correction session. Prior Worker 08 authority was
not used. Native planning mode was not entered.

## Capability handshake

| Item | Classification | Value |
| --- | --- | --- |
| Product/client requested | unknown/not observably exposed | Prompt leaves client selection to Michal |
| Product/client observed | directly observed | Cursor agent session |
| Model requested | unknown/not observably exposed | Prompt does not name a model |
| Model observed | directly observed | Runtime identity string Cursor Grok 4.6; not independently attested |
| Reasoning requested | requested | High |
| Reasoning observed | unknown/not observably exposed | Effort not observably exposed by the client |
| Native planning mode requested | requested | `not-used` |
| Native planning mode observed | directly observed | `not-used` (no plan-mode switch) |
| Filesystem containment | directly observed | Canonical checkout `/home/agile/Projects/framenest` writable; Meta write limited to this report path |
| Source inspect/edit | requested and directly observed | Allowlisted companion paths only |
| JS tests | requested and directly observed | `node --test tests/x_companion_extension.test.js` |
| Local commit | requested and directly observed | One commit on existing `feat/x-meme-browser-companion` |
| Public-ref `ls-remote` | directly observed | Informational `origin/main` `bfad16b718e135b272a3b0293bb37ddc3101ba49` |
| Push | requested unauthorized | Not performed (technically possible; no authority) |
| NUC / sudo / provider / signed-in browser / pytest / `ap exec` / `.ap` mutation | requested unauthorized | Not performed even if technically possible |

`private/companion-extension.pem.key` exists as gitignored untracked-ignored
under `/private/`. It was listed, not read, not copied.

`git fetch` was not run.

## Repository gate

```text
Root: /home/agile/Projects/framenest
Origin: https://github.com/cisarik/framenest.git
Branch: feat/x-meme-browser-companion
Baseline HEAD: 572c6d4e239a65cd4457061d0cdd59c46c1ba2a7
Baseline parent: 14c8a7098e41fa9602c1c45bbf3f2207f6001400
Baseline tree: 35e064923497d475ec80eb1f426a371f75c48a3a
Baseline subject: fix: hide origin setup behind companion Settings
Pinned AP gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Informational origin/main: bfad16b718e135b272a3b0293bb37ddc3101ba49
Pre-mutation status: clean tracked tree
```

## Resulting commit

```text
HEAD: 9cec59803a0c00d15e6a1fb84a651ec667236508
Parent: 572c6d4e239a65cd4457061d0cdd59c46c1ba2a7
Tree: 1a52d64c20feafcb18bda9b9d4ff20ba47a8f29e
Subject: fix: overlay Save on hover media instead of the Share row
Push: not performed
```

Changed paths (exact allowlist; `extension/ui/picker.js` needed no edit):

```text
docs/X_COMPANION.md
extension/content/x_adapter.js
extension/content/x_adapter_contract_v1.js
extension/ui/picker.css
extension/ui/picker.html
tests/support/x_fixtures/composer.html
tests/x_companion_extension.test.js
```

`web/styles.css` and `web/app.js` were not changed. `extension/manifest.json`
was not changed. Adapter contract version remains `1`.

## Behavior

Save: removed from the tweet action / Share row (`SAVE_DOWN_NUDGE_PX`,
Share-column alignment, and action-group insertion are gone). Frozen
`mediaHostSelectors` discover own `[data-testid='tweetPhoto']`,
`[data-testid='videoPlayer']`, `[data-testid='videoComponent']`, and
`[data-framenest-media]` tiles, skipping nested quoted
`article[data-testid='tweet']` and distinct link-preview cards. Nested
video hosts collapse to the outermost tile. Each host gets at most one
control, tracked per host. A single injected
`<style data-framenest-companion-style>` scopes overlay/attach chrome.
Idle Save is opacity 0 and `pointer-events: none`; host `:hover` /
`:focus-within` and button focus make it a 32px opaque-black square with
a 1px `#00ff41` border and a green plus, top-left, z-index 5. Text-only
posts receive zero Save controls. Click still sends `SAVE_POST` with the
post permalink (`accepted.submittedUrl`). No content-script fetch of X
CDN / `pbs.twimg.com` URLs.

Attach: no longer a Content-disclosure sibling. `findComposerChrome` pins
the control as `position: absolute; right: 0; bottom: 0; margin: 0` on the
composer box (fixture `[data-framenest-composer-chrome]`, else the nearest
non-editable ancestor that contains the toolbar). Same black/green plus
language, `data-framenest-companion="attach"`, `aria-label` `Attach from
FrameNest`, ACK / `openPicker` unchanged. Missing chrome skips that
composer without global stale. Missing file input still marks stale.
`tweetButton` is absent from adapter source.

Picker home: visible FN disc and `FrameNest` `<h1>` title removed.
Settings remains top-right. `>` Search memes remains. Origin stays in the
Settings sheet.

Honest residual: overlay Save is still post-level. Clicking any media +
submits the existing post URL through `SAVE_POST`; it does not name which
image in a multi-media post. Per-asset targeting, static-photo
acquisition, and NUC X enablement remain parked.

## Commands and exit codes

```text
git rev-parse / remote / branch / HEAD / parent / tree / subject / status
exit 0 — baseline matched before mutation

git ls-tree HEAD .ap && git submodule status .ap
exit 0 — gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656

git ls-remote origin refs/heads/main
exit 0 — bfad16b718e135b272a3b0293bb37ddc3101ba49

node --test tests/x_companion_extension.test.js
exit 0 — 12 pass / 0 fail (pre-commit and on HEAD 9cec598)

git add -- <seven allowlisted paths> && git commit
exit 0 — 9cec59803a0c00d15e6a1fb84a651ec667236508
```

## Control matrix (source/fixture; not live Brave/X)

Positive: per-media overlay +; composer Attach `right: 0; bottom: 0`;
picker Settings retained; frozen media-host selectors; synthetic fixture
has `tweetPhoto` / `data-framenest-media` and composer chrome.

Negative: no action-row Save insertion; no Save on text-only posts
(`return "no_media"`); no `tweetButton` / `form.submit` / auto-submit in
adapter source; no Search titles; no transparent idle Save fill; picker
home has no FN / FrameNest header title.

No-auto-Post residual: attach still only fills the composer file input
and dispatches `change`. The companion does not click Post.

## Not claimed

This PASS is not live Brave/X certification, publication, deployment, or
ORCHESTRATOR closure. Gated browser evidence was not required and was not
taken.

## Next step

Michal reloads the unpacked extension and hovers a multi-image post.

Worker 09 authority is expired.

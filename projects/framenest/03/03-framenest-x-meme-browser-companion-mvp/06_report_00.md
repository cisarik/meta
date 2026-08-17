### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-meme-browser-companion-mvp
Worker session ordinal: 06
Worker exchange ordinal: 01
```

```text
Terminal status: PASS
Phase-qualified result: implementation-PASS
Logical-whole closure: not-closed
Report justification: new-mutation
```

This bounded visual correction placed the in-feed Save control in the post's
own native action row immediately after Share. It does not claim that live
Brave/X now looks correct.

## Capability handshake

| Item | Classification | Record |
| --- | --- | --- |
| Product/client | directly observed | Cursor agent session |
| Requested model | requested | High reasoning; Michal owns the actual model, client, and launch decision |
| Observed model identity | unknown/not observably exposed as a verified identity | Session communication names Cursor Grok 4.6; that string is not independently attested and grants no authority |
| Requested reasoning | requested | High |
| Observed reasoning state | unknown/not observably exposed | No separate High/Max control was observably exposed; work was not silently downgraded and Extra High/Max was not used |
| Native planning mode | requested `not-used`; directly observed `not-used` | No native plan mode was entered |
| Filesystem containment | directly observed | Canonical checkout `/home/agile/Projects/framenest` was writable; Meta mutation was limited to this exact report path |
| Network | directly observed | Read-only `git ls-remote origin refs/heads/main`; `git fetch` was not used |
| Source inspection/editing | requested and used | Allowlisted paths only |
| Tests | requested and used | `node --test tests/x_companion_extension.test.js` |
| Local commit | requested and used | One commit on `feat/x-meme-browser-companion` |
| Public-ref `ls-remote` | requested and used | `refs/heads/main` matched the exact baseline |
| Push | unauthorized | Technically possible; not used |
| NUC / sudo / SSH agent probe | unauthorized | Not used |
| Provider / signed-in browser / live x.com | unauthorized | Not used |
| Python pytest / `ap exec` / raw Python | unauthorized | Not used |
| AP / ledger mutation | unauthorized | `.ap/` treated as read-only |

Capability is not authority. Credentials were not probed. `SSH_AUTH_SOCK` was
not printed. `gpgconf` was not reconstructed.

## Repository gate

```text
Root: /home/agile/Projects/framenest
Origin: https://github.com/cisarik/framenest.git
Branch: feat/x-meme-browser-companion
Baseline HEAD: bfad16b718e135b272a3b0293bb37ddc3101ba49
Baseline parent: 0cf6919a889dc4c6919d843a24cee2bb43fb4bfc
Baseline tree: 65ac2469a8212d17c48ae17e37314e03a1ad4f91
Baseline subject: docs: record X companion origin trust and operator setup
Pinned AP gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public main at gate: bfad16b718e135b272a3b0293bb37ddc3101ba49
Working tree at gate: clean tracked files
```

`private/companion-extension.pem.key` exists as gitignored untracked-ignored
path `/private/`. It was listed, not read, copied, or printed.

No overlapping dirty tracked files were present on the allowlist. No prior
Worker-06 mutation existed. No new branch was created.

## Final candidate

```text
Final HEAD: 4a7fd25f26ce4446c48123f34bb3e11694b23e8b
Parent: bfad16b718e135b272a3b0293bb37ddc3101ba49
Tree: d5883b1f677d7d953ff0dacaf93f3e66754f1948
Subject: fix: place X companion Save beside native Share
.ap gitlink: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656 (unchanged)
Branch: feat/x-meme-browser-companion
Push: not performed
Public main: unchanged from the gate SHA
```

## Exact changed paths

| Path | Purpose |
| --- | --- |
| `extension/content/x_adapter_contract_v1.js` | Keep adapter version `1`; add frozen `actionGroupSelectors`, `actionBarSignals`, and `shareSelectors` |
| `extension/content/x_adapter.js` | Place Save as an action-row sibling after Share; fail closed when the bar/Share is missing; show status without visible tweet-row text |
| `tests/support/x_fixtures/composer.html` | Synthetic post now has Reply / Repost / Like and `aria-label="Share post"` in an action group; no FrameNest node |
| `tests/x_companion_extension.test.js` | Causal source and fixture assertions; Post-button check no longer uses a naive `"Post"` substring that would false-fail on `Share post` |
| `docs/X_COMPANION.md` | One Save bullet now describes an action-row control next to Share |

## Placement and fail-closed behavior

Save is no longer created by `addButton(postRoot, "Save to FrameNest", …)` and
is never `appendChild`'d onto `article[data-testid='tweet']`.

For each post root the adapter:

1. Skips posts already injected.
2. Skips posts with no accepted permalink (no global stale).
3. Finds the post's **own** `[role='group']` that contains
   `[data-testid='reply']`, `[data-testid='retweet']`, or
   `[data-testid='like']`, ignoring groups inside a nested quoted post root.
4. Finds Share inside that group via `[data-testid='share']`,
   `[aria-label='Share post']`, then `[aria-label='Share']`.
5. Walks up from Share until the parent is the action group and inserts the
   FrameNest column with `insertAdjacentElement("afterend", …)`.
6. If the own action bar or Share column is missing: **skips that post**.
   There is no article-append fallback.

Global `markStale("adapter_drift")` runs only when a scan sees eligible
permalinks, **zero** successful Save placements (including already placed),
at least one action bar whose Share/column could not be used, and **no**
posts still missing an action bar. Incomplete cards therefore do not poison
the page during hydration. Composer `injectAttach` remains a labeled control.

The clickable control is `data-framenest-companion="save"` with
`aria-label` / `title` `Save to FrameNest`, a 36×36 transparent hit target,
and a 22px plus-in-square SVG using `currentColor`. Click uses
`preventDefault`, `stopPropagation`, and `stopImmediatePropagation`.
`pointerdown` / `mousedown` stop bubbling without `preventDefault` so the
click still fires.

## Status without tweet-row text

SAVE_POST / POLL_CLAIM / recover remain. Working, success, and failure are
shown only through `aria-label` / `title`, `aria-busy`, and a same-size SVG
swap (plus / arc / check / x). Server error codes, `Saving…`, and claim
state are never assigned to `textContent` of the action-row control.
`markStale` disables Save icons and sets the accessible name to
`FrameNest unavailable` without replacing their `textContent`.

The parked `X_REQUEST_NOT_CONFIGURED` server condition is unchanged and was
not “fixed”. After this correction it must not reappear as a gray slab of
visible tweet-row text.

## Commands actually run

| Command | Exit |
| --- | --- |
| Repository identity/status/`ls-remote` gate (read-only Git) | 0 |
| `git check-ignore -v private/companion-extension.pem.key` plus metadata listing | 0 |
| `node --test tests/x_companion_extension.test.js` (before commit) | 0 (9 pass) |
| `node --test tests/x_companion_extension.test.js` (after pointerdown halt adjustment) | 0 (9 pass) |
| `git add --` exact allowlisted paths; `git commit` | 0 |
| Post-commit `git status` / `git log -1` | 0 |

`git fetch`, pytest, `ap exec`, raw Python, push, NUC, sudo, and browser
automation were not run.

## Browser evidence

Not performed. Live x.com was not scraped. Michal's Brave profile was not
used. This Worker does not self-certify live UX.

## Security and privacy residuals

- No Post control, `tweetButton` selector, `form.submit`, or auto-submit path
  was added.
- Content scripts still do not fetch FrameNest. SAVE_POST payload shape is
  unchanged.
- Companion private key was not read.
- `X_REQUEST_NOT_CONFIGURED` / origin allowlist / NUC enablement remain
  parked and out of scope.
- Residual: live X DOM remains volatile; Share labels other than the frozen
  English/`data-testid` list will fail closed per post.

## Clean/dirty final status

```text
Branch: feat/x-meme-browser-companion
HEAD: 4a7fd25f26ce4446c48123f34bb3e11694b23e8b
Tracked working tree: clean
Ignored private key: present, unread
```

## Resolved Execution Issues / Near-Misses

Registering a separate `click` listener that called `stopImmediatePropagation`
before the Save handler would have blocked Save. Combined into one `click`
handler. `preventDefault` on `pointerdown` was not used because it can
suppress `click`.

The previous contract test `serialized.includes("Post")` would have
false-failed on `[aria-label='Share post']`. It was narrowed to Post-button /
auto-submit signals.

## Pre-Existing Failure Classification

None in this gate. The live Save-bar layout defect was the assigned
correction, not a pre-existing failing repository test.

## Smallest next step

Michal reloads the unpacked extension in Brave and inspects the Share row
only. Live visual acceptance, publication, NUC redeploy, and Save-request
enablement remain outside this grant.

## Authority expiry

Authority granted by the Worker 06 exchange-01 prompt expires at this
terminal report. This Worker must not continue, push, publish, deploy, or
self-certify live X appearance.

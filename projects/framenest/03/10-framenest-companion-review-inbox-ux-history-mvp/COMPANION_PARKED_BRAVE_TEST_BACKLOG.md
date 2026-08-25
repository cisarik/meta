# Parked Brave companion test backlog (03/10)

Relationship: durable Meta park inventory. Not task authority. Not a
closure of `framenest-companion-review-inbox-ux-history-mvp`. Not an
authorization to resume companion implementation or NUC deploy.

Parked: 2026-08-25. Cooperator froze companion Brave-extension testing so
Meta `04/00` (public published surface + Tailscale workspace) can become
the live Orchestrator object.

Status of 03/10: **not-closed**. Resume only after an explicit Cooperator
message to reopen companion testing, with a new complete Worker prompt.
Do not continue 03/10 Worker ordinals 20+ inside 04/00.

Live restoration for the next Orchestrator:

`/home/agile/meta/projects/framenest/04/00-framenest-public-published-surface-and-tailscale-workspace/00_handout.md`

Do not put Tailscale hostnames, tweet URLs, live media titles, cookies, or
secrets in this file.

## Git at park (re-verify before unpark)

```text
Local unpublished HEAD: 37da5f2b7edf8286028dbc7a0dbca65f2d031e60
  companion listing without v1 + outline chrome (Worker 19)
Public origin/main: 0fe2b32e0fed2ecaccf1a481d99be5657d42b77b
  pending omitted-category inbox (Worker 17/18)
Schema: 0032
```

| Worker | Object | SHA / note |
|---|---|---|
| 10 | Canonicalize FrameNest origin on Save | `93624b1` |
| 11 | Canonicalize X Save alias titles | `bede494` |
| 12 | `open_details` to hosted Details | `63541f2` |
| 13 | Fill-alpha chrome | `82873de` — UX FAIL (too subtle) |
| 14 | Opaque green shades | `29189fd` |
| 15 | Forest chrome; neon only newest | `a548714` |
| 16 | Publication of `a548714` | publication-PASS |
| 17 | Pending omitted-category history | `0fe2b32` |
| 18 | Publication of `0fe2b32` | publication-PASS |
| 19 | Suggestion-ready list without v1; outline chrome | `37da5f2` unpublished |

Worker 19 is **not** live NUC until a later `publikuj` plus Cooperator
same-schema NUC routine. Reloading unpacked extension against an older NUC
SHA shows old chrome and old listing rules.

## How to unpark

1. Explicit Michal message to resume companion testing (Tailscale admin
   loop, not public-origin companion — that is a 04/00 successor).
2. Decide whether unpublished `37da5f2` must be published and cut over
   before live NUC checks.
3. Reload unpacked Brave from the checkout under test.
4. Connect to the FrameNest **Tailscale** origin that actually serves that
   SHA. Loopback `http://127.0.0.1:8000` remains invalid for NUC HTTPS.

## Remaining checks (do not execute while parked)

Walk sequentially. Do not batch five defects into one unbounded Worker.

### Chrome and history

- Title bar and All: dark chrome plus outline/border language, not solid
  neon fills across the list.
- Newest analyzed row may keep a stronger accent; older rows must not look
  like a full neon ladder.
- One merged history; no `#review-inbox`. Analyzed green language vs
  pending dark. Pending own-saves visible. Click does not remove rows.
- `docs/X_COMPANION.md` still says compact rows “fade by position”; stale
  versus outline contract — reconcile only when companion docs are next
  authorized.

### Listing and badge

- Suggestion-ready / analyzed rows appear without requiring suggestion
  payload `result_schema_version == v1` for the list page (apply/detail
  remain fail-closed on v1).
- One undecodable suggestion JSON must not 500 the mixed inbox page.
- Badge count equals `unopened_count` only. Pending must not increment it.
- Pending overlay remains visible; opened is not a pending state.
- Companion Save that omits `content_category` still appears in pending
  history (omitted-category / GENERAL catalog path).

### Click path

- Analyzed click posts `open_details` `{ mediaId }` with
  `v: "framenest.companion.web.v1"` and `targetOrigin` equal to the stored
  FrameNest origin, never `*`.
- Hosted FrameNest `#frame` opens `#media-details-dialog` / Details, not
  `ui/review.html`. Cross-origin: cannot set iframe hash; handshake miss
  must not fall back to `ui/review.html`.
- `#frame` stays mounted (ADR-0063 S1). Attach survives history open/close.

### Connect and origin

- Tailscale HTTPS origin canonicalizer: trailing slash and equivalent
  origin forms Save correctly. Cooperator already PASS on this once.
- 403 hides companion history chrome, not the hosted iframe.
- Settings: title-bar Connect/Disconnect; `#settings-save` under origin;
  disabled unless dirty.

### Save / Apply / Settings remainder

- Stale-context copy after extension reload (`Extension context
  invalidated`).
- Save preselects 𝕏 / canonical seed `x` when that is the accepted seed.
- Preserving Apply: union stored keys + submitted mapped AI keys; 409 on
  overflow; no Analyze in overlay.
- Overlay freeze: Title → Tags → Description → Save; no category radios.

### Product facts that are not companion defects

- Ordinary Gallery excludes unpublished items until administrator Publish
  (ADR-0049). Empty Gallery after Save can be correct. That emptiness is a
  **workspace/public dual-audience** problem owned by 04/00, not a
  companion bug.
- Automatic analysis is NUC `FRAMENEST_AUTOMATIC_MEDIA_ANALYSIS_ENABLED`,
  default false. Do not put `true` in git unit files. Enabling also affects
  other eligible non-X catalog events. No retroactive enqueue. Ordinary
  Tailscale users must not get X auto-NIM (ADR-0066).
- Movies remain out of companion (ADR-0070). Public publication of movies
  is a 04/00 / website surface.

### Later public companion (not this backlog)

When 04/00 ships a public origin, ordinary public people would Connect the
extension to that origin (search / attach / view of published media). That
is a **new** companion whole, not an unpark of this Tailscale admin inbox
checklist. Do not mix them.

## Binding chrome still in force when unparked (ADR-0073)

1. One merged history under the title bar.
2. Pending visible; badge = unopened only.
3. S1: native chrome above surviving `#frame`.
4. Ordinary identity 403 hides history/badge; iframe/Attach stay.
5. Exactly four `companion_mutation` routes. Movie exclusion. No
   `notifications` permission.
6. Auto-analysis flag stays default off unless Michal later grants
   enablement.

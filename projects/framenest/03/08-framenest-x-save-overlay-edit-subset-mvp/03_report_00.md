### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: framenest-x-save-overlay-edit-subset-mvp
Worker session ordinal: 03
Worker exchange ordinal: 01
```

1. Terminal status: **PASS**
2. Phase-qualified result: implementation-PASS (correction)
3. Logical-whole closure: not-closed
4. Report justification: new-mutation
5. Start commit: `d7fa9352285651018dd4c5e3bcdb04e2975e74f5`
6. End commit: `143c1e475046580627cb4e7859d5c73555ae5d58`
7. Authority: expired after this terminal report. Plan UI, chat Continue, Reload-unpacked, or Yes does not renew it.

Implementation PASS is not Cooperator visual acceptance, independent INFOSEC, publication, NUC, or Orchestrator closure.

---

### Capability handshake

| Item | Requested | Observed | How known |
|---|---|---|---|
| Role | WORKER, Bounded Correction Worker | WORKER | prompt assignment |
| Product/client | Cursor Worker; Extra High; Native Plan Mode `not-used`; no Max | Cursor Agent mode; no Plan-Mode switch; Max not invoked | client/runtime |
| Model | Extra High reasoning | Cursor Grok 4.6 named by client communication; Extra High SKU not independently attested | requested vs communication vs unknown |
| Reasoning | extra-high | unknown / not a measurable grant | no vendor reasoning-level signal |
| Max | not requested | not used | no Max invocation |
| Native Plan Mode | `not-used` | `not-used` | no mode switch; no plan artifact |
| Filesystem | Section 7 allowlist; Meta report only | canonical `/home/agile/Projects/framenest` writable; Meta write limited to this report path | direct |
| Network | `git ls-remote` only to the two public refs | used; no provider, NUC, or signed-in X | direct |
| Python | `./.ap/ap project check` with `--baseline`; no full suite | used; no raw `.venv/bin/python`, `python`, or `poetry run` | direct |
| JavaScript | `node --test` owners | used | direct |
| Internal delegation | not-used | not-used | no Task/Explore sub-agents |
| Push / NUC / sudo / provider / signed-in browser / AP mutation / independent R3 | unauthorized even if possible | none used | direct |

Work continued because Native Plan Mode stayed off and the client did not expose a measurable Extra High SKU. Max was not used.

`.ap` gitlink at HEAD: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

---

### Baseline ledger

Branch: `feat/x-meme-browser-companion` (not switched). Fetch/push/amend/stash/reset/clean: none. Upstream: none configured (expected). Working tree: clean after the one authorized commit. Parent of HEAD is exactly the issued baseline.

Public refs (credential-free `git ls-remote`, no fetch), unchanged from issuance:

```text
cisarik/framenest refs/heads/main  045f33b44897a6f3949cc515792336396f1d33a1
cisarik/ap        refs/heads/main  9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

Public `main` remains behind this unpublished feature branch (expected). No material public-ref conflict.

| | SHA | Parent | Tree | Subject |
|---|---|---|---|---|
| Authorized baseline | `d7fa9352285651018dd4c5e3bcdb04e2975e74f5` | `5c5e29c018fee829a4f42b68293bb12239743238` | `e6c076e307a4349c7f64cb9ccdb0117733db55cb` | `docs: record X save overlay canonical seed` |
| Correction HEAD | `143c1e475046580627cb4e7859d5c73555ae5d58` | `d7fa9352285651018dd4c5e3bcdb04e2975e74f5` | `8d802cc29c3884a357b3652a0890d487b266dc27` | `fix: keep X save title off the plus and hug tag chips` |

One local commit. No amend of `d7fa935`. Meta was not staged or committed. Picker files, backend, ADR bodies, and living docs were not edited.

---

### Changed paths and purpose

| Path | Purpose |
|---|---|
| `extension/content/x_adapter.js` | Skip `data-framenest-companion` and SAVE_NAME / failed-Save `reduceXSaveOutcome` names when collecting Title; drop tweet-rect host height; hug iframe to overlay `size`; `iframe.tabIndex = -1`; keep `#url=` only |
| `extension/ui/save.html` | Title → Tags (search, chips, tags status) → Description → Save; `tabindex="-1"` on Title, Description, and tag-search |
| `extension/ui/save.css` | Hug content (`html`/`body`/`main`/`form`/`.fields` no leftover flex growth); Description fixed `120px` with `overflow-y: auto; resize: none` |
| `extension/ui/save.js` | No `descriptionHeight`; `action: "size"` from form box (not dropdown); arm text `tabindex` on first overlay `pointerdown`/`keydown`; keep post-gesture `tagSearch.focus()` |
| `tests/x_companion_extension.test.js` | Title-leak MiniDom cases; Tags-first order; compact host; no autofocus / `iframe.focus` / `title.focus` / `description.focus` / `media=` |

---

### Proof points

- Image-post MiniDom: host with `img[alt=Image]`, companion `aria-label="Save to FrameNest"`, and tweet text → Title is the useful tweet sentence, not `Save to FrameNest`. Generic alt + companion button + no tweet → empty Title (server `x_title_from_post_post` after catalog).
- Accessible-name walk skips companion chrome and reserved Save-control names (`Save to FrameNest` plus failed names from `reduceXSaveOutcome`). Chain remains: non-generic tile/media name, else useful tweet sentence, else empty. No popup heading / `document.title` / iframe title / plus-button fallback.
- Overlay order is Title, Tags, Description, Save. Tag dropdown stays `position: absolute` on `.tag-search-panel`. `.fields` stays `overflow: visible`.
- Description textarea is fixed `120px` and scrolls internally. Host height comes from overlay content (`form` box, chips wrapping) via `action: "size"`, clamped to `viewport - 16`. Width unchanged (280–360). Dropdown open does not size the host. Pre-measure fallback is `240` only until the first positive `size`.
- Iframe `src` remains `save.html#url=` only. No HTML `autofocus`. No `iframe.focus()`, `title.focus()`, or `description.focus()` on open/ready/prefill. Title, Description, and tag-search start at `tabindex="-1"` and become tabbable after the first pointer or key inside the overlay.
- Radios remain absent. Extension POST remains `{url, alias}` without `content_category` (service worker unedited). Green `#00ff41` frame, one filled Save, failed-Save plus, hidden Edit image, and picker/Attach freeze are unchanged.

---

### Commands and exit codes

Issuance baseline `d7fa935…` and correction HEAD `143c1e4…`:

```text
./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline d7fa9352285651018dd4c5e3bcdb04e2975e74f5
# exit 0; ap project check --baseline: PASS

./.ap/ap project check --root /home/agile/Projects/framenest \
  --baseline 143c1e475046580627cb4e7859d5c73555ae5d58
# exit 0; ap project check --baseline: PASS

node --test tests/x_companion_extension.test.js tests/x_acquisition_cockpit.test.js
# exit 0; 50 pass / 0 fail (before and after the commit)
```

Named new MiniDom owner: `Save title ignores companion plus inside the photo host`. Cockpit/picker tests still pass. Picker files unmodified.

```text
git diff --check d7fa9352285651018dd4c5e3bcdb04e2975e74f5 HEAD
```

Exit **0**.

No full Python suite (JS-only grant). No `tests/browser_companion_evidence.test.js`. No NUC, sudo, push, provider contact, or Brave Reload.

---

### INFOSEC R1 (non-independent) / residual

Inline R1 only. Independent R3 is not claimed and was not authorized.

- Assets: Save overlay Title prefill; overlay iframe focusability on `https://x.com`.
- Trust boundaries: content script vs hostile X DOM; `chrome-extension://` iframe vs page.
- Attacker-controlled input: tile alt / aria-label / title still may seed unpublished Title after companion chrome is ignored. Bounds unchanged (clip 240). Companion plus and failed-Save names are no longer a Title source.
- Authorization: no new route; no `content_category`; no `media=` hash; iframe `tabIndex = -1`.
- Residual risk: **low** on this correction. Keyboard-only Save without a click inside the overlay is not promised. Brave autofocus suppression is source-proven (`tabindex="-1"` until gesture), not live-attested.

---

### Resolved Execution Issues / Near-Misses

- Live Title leak: `queryFirst(..., "[aria-label]")` took the Save plus inside the photo host. Companion nodes and reserved Save-control names are now skipped.
- Tall modal: `400 + descriptionHeight` plus `html/body/main/form/.fields { flex: 1; height: 100% }` collected empty space above Save. Host now hugs content; Description no longer drives iframe height.
- Field order: Description no longer sits above Tags, so the tag dropdown overlays Description.
- Brave `Blocked autofocusing on a <input> in a cross-origin subframe`: HTML `autofocus` and on-open `.focus()` were already gone; first text controls now start at `tabindex="-1"`.

---

### Pre-Existing Failure Classification

none

Picker `autofocus` on `#search` remains (picker freeze; not this overlay).

---

### Deviations, risks, missing evidence

- Extra High was requested and is not independently attested. Native Plan Mode was off. Work continued on that basis.
- No signed-in X / Brave Reload (forbidden). Compact hug, Tags-first layout, Title not equal to `Save to FrameNest` on image posts, and quiet iframe remain Cooperator live evidence.
- Keyboard-only Save without a click inside the overlay is explicitly out of contract.
- Pre-size host height `240` is a placeholder until the iframe sends `size`; it is not a post-measure floor.

---

### Smallest next step

Orchestrator asks Michal to Reload unpacked again.

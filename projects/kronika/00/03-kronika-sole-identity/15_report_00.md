### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Session:** `15` · **Exchange:** `01` · **Status:** `PASS` · **Result:** `new-mutation`
**Commit:** `77bcb81c8a5f84e91ec4b31dd12f8ad2204016a8` on `main`, parent `09e45e54c8444281c147f9ba799e3602bb57d9aa`, not pushed. Tree clean.

No client preamble was emitted above this header.

---

## 1. Repository gate

All green before editing: branch `main`, HEAD `09e45e54…`, working tree clean, submodule `73e20ef…` matching the superproject gitlink, `git ls-remote origin main` = `9c71bfb0a06cb30c5d747816e9067f6a25350c58` (local `main` one commit ahead, as stated), `ap doctor: PASS` (governing variant stable), `ap project check --baseline 09e45e54…`: **PASS**. Node `v26.8.2`.

## 2. Baselines reproduced before editing

| Route | Expected | Measured |
|---|---|---|
| Python declared `test` operation | 4359 / 8 / 3 | **4359 passed, 8 skipped, 3 warnings** (653.34s) |
| JS `node --test tests/*.test.js` | 582 / 577 / 0 / 5 | **582 total, 577 passed, 0 failed, 5 skipped** |
| Retention module | 15 | **15 passed** |

Both reproduced exactly. No edit was made while a suite was running.

## 3. Enumeration 1 — the display inventory

Method: **parse the artefact, test every carrier**, never grep for known literals. A throwaway Node probe (`/tmp/opencode/ksi-c2c-display-inventory.mjs`, stdlib only, read-only) scanned eight surfaces: for each JS file a comment-aware string-literal scanner over the raw bytes; for each HTML file every inter-element text node plus every quoted attribute value, with comments/script/style bodies masked.

| Surface | Letter-bearing carriers | Retired-brand hits before | after |
|---|---|---|---|
| `extension/shared/messages.js` | 168 | 14 | 2 |
| `extension/ui/save.js` | 110 | 4 | 3 |
| `extension/ui/picker.js` | 40 | 1 | 0 |
| `extension/ui/sidebar.js` | 164 | 10 | 1 |
| `extension/content/x_adapter.js` | 485 | 68 | 64 |
| `src/framenest/adapters/api/web/app.js` | 4170 | 12 | 4 |
| `extension/ui/save.html` | 62 | 2 | 0 |
| `extension/ui/picker.html` | 46 | 1 | 0 |
| **total** | **5245** | **112** | **74** |

Carrier count is unchanged at 5245 — this cut substitutes, it never adds or removes a literal. The 74 residuals are, exhaustively and by hand: 3 localStorage keys + 1 mutation header in `app.js`; 2 protocol/storage names in `messages.js`; 1 protocol name in `sidebar.js`; 3 DOM ids in `save.js`; and 64 CSS selectors, DOM attribute names and the port name in `x_adapter.js`. **Zero user-visible occurrences of the retired brand remain on any in-scope surface.**

Classification of the 112 pre-change hits: **38 display**, 74 machine-read (Excluded 2 / the header). Display site count by file: `messages.js` 12, `sidebar.js` 9, `app.js` 8, `x_adapter.js` 4, `save.html` 2, `save.js` 1, `picker.html` 1, `picker.js` 1 = **38**, plus `media_content.py:88` found by the same principle (a deterministic filename, not a literal). **39 sites, 41 brand-word occurrences** — three literals name the brand twice (`messages.js:631`, `sidebar.js:486`, `app.js:12595`).

Two line-number corrections against the issued list, disclosed:

- **`picker.js:27` carries one display string, not two.** `"FrameNest companion"` is `picker.html:5` (`<title>`); `picker.js:27` is only `disconnectedStatus()`.
- **`sidebar.js` has nine display literals on eight lines**, not eight. Line 486 holds the `aria-label` *pair* `"Disconnect FrameNest"` / `"Connect FrameNest"`. Session 14's count of eight was line-based.
- **`save.html:5,12` is title + heading**, not "heading and supporting text" as the brief described it. There is no supporting sentence there.

## 4. Enumeration 2 — the assertion inventory

Method: **every tracked test file, `FrameNest` in an assertion context**, not in a string-literal context. 996 lines across `tests/`; every `assert`/`assert.match`/`assert.equal`/`notEqual`/`includes` line carrying the brand, plus every search for each distinctive substring of every string being changed (this second sweep is what caught the pin the first one missed).

**33 display assertions repointed.** The Orchestrator's list of four was correct in all four cases and omitted **29**:

| # | Assertion | Pins |
|---|---|---|
| 1 | `companion_review_extension.test.js:1127` `/Connect FrameNest in Settings/` | `sidebar.js:785,1103` |
| 2 | `companion_settings_automatic_analysis.test.js:508` `/Could not reach FrameNest/` | `sidebar.js:672` |
| 3 | `x_companion_extension.test.js:581` `/Connect FrameNest in the side panel/` | `picker.js:27` |
| 4 | `x_companion_extension.test.js:1483` `/Connect FrameNest in Settings/` | `sidebar.js:785,1103` |
| 5 | **`youtube_acquisition_cockpit.test.js:23`** `CREATE_CONFIRMATION_MESSAGE` | `app.js:1625` |
| 6–33 | `x_companion_extension.test.js:117, 336, 347(test title), 585, 1491, 1861, 1945, 2025, 2031, 2037, 2078, 2081, 2085, 2089, 2098, 2102, 2105, 2109, 2113, 2119, 2165, 2166, 2218, 2225, 2229, 2232, 2239, 2248` | `sidebar.js:838`, `messages.js` ×12, `x_adapter.js:21`, `save.js:7`, `picker.js:27` |
| — | `test_media_content_application.py:255`, `test_local_web_media_playback.py:230` | `media_content.py:88` |

**`youtube_acquisition_cockpit.test.js:23` is the finding that matters.** It is a positive pin on the *entire* acquisition-confirmation sentence in `app.js:1625` — the longest single display string this cut retired — and it would have shipped red at the eleven-minute suite. Exactly the C2b failure mode: it names the brand inside a whole-sentence constant, so no literal search for `"FrameNest …"` finds it.

Deliberately **unchanged**, and why:

- `x_companion_extension.test.js:258, 355, 543, 578, 1364` and `companion_review_extension.test.js:567` — **negative** assertions. They now double as retired-brand tripwires and are stronger left as they are.
- `x_companion_extension.test.js:2638–2640` — negative manifest guards.
- The ~24 `X-FrameNest-Request` assertions (Excluded 1).
- `test_local_web_application.py:628` (`"optimized preview frames" in combined`) and `ai_providers_admin_frontend.test.js:464` (`"solid-red test square"`) — substring pins on `app.js:5175/6794` and `12595` that contain no brand word, so they survive and stay valid. Verified, not assumed.
- `x_companion_extension.test.js:91, 422` — test titles naming `canonicalizeFrameNestOrigin` and the gallery token vocabulary. Not display text, not assertions. Reported as residual for C3/C7.

## 5. Reconciliation — the two counts, and the difference

**39 display sites. 33 assertions repointed. These do not match, and here is exactly why they need not.**

- **19 of the 39 sites** carry at least one of the 33 assertions.
- **20 sites carry none** and are covered only by the extended agreement guard: `messages.js:633, 658`; `sidebar.js:66, 70, 486`; `x_adapter.js:30, 1765, 1772`; `save.html:5, 12`; `picker.html:5`; `app.js:1874, 1993, 5175, 6794, 8274, 11965, 12595`.
- **33 assertions → 19 sites** because of three exact multiplicities: 4 assertions are fixture copies of `x_adapter.js:21` (1934, 2014, 2020, 2029); 2 assertions pin the single sidebar literal that occurs at both 785 and 1103; and repeated exact-match pins of one literal across tests (`messages.js:675` ×4, `642` ×3, `629` ×2, `690` ×2, `624`+`683` share 2, `660` ×2, `667` ×2).
- 19 + 20 = **39**. 33 assertions, 19 sites, 20 guard-only, one addition that reconciles both directions: **every repointed assertion maps to a display site, and every display site maps to an assertion or to the guard.**

I reconciled this before touching a file, and it is what surfaced the count I would otherwise have shipped wrong.

## 6. Before-and-after of every renamed string

```text
messages.js:624   "Save status unknown—check FrameNest"              -> "Save status unknown—check Kronika"
messages.js:629   "Save to FrameNest failed"                        -> "Save to Kronika failed"
messages.js:631   "Save to FrameNest failed—FrameNest needs an update"
                                                                     -> "Save to Kronika failed—Kronika needs an update"
messages.js:633   "Save to FrameNest failed—category already differs"
                                                                     -> "Save to Kronika failed—category already differs"
messages.js:642   "Already saved to FrameNest"                      -> "Already saved to Kronika"
messages.js:650   "Saved to FrameNest"                              -> "Saved to Kronika"
messages.js:658   "Partially saved to FrameNest"                    -> "Partially saved to Kronika"
messages.js:660   "Partially saved to FrameNest (n of m)"           -> "Partially saved to Kronika (n of m)"
messages.js:667   "Save to FrameNest failed"                        -> "Save to Kronika failed"
messages.js:675   "Saved item is no longer available in FrameNest"  -> "… in Kronika"
messages.js:683   "Save status unknown—check FrameNest"             -> "Save status unknown—check Kronika"
messages.js:690   "Saving to FrameNest…"                            -> "Saving to Kronika…"
save.html:5       <title>Save to FrameNest</title>                  -> <title>Save to Kronika</title>
save.html:12      <h1>Save to FrameNest</h1>                        -> <h1>Save to Kronika</h1>
save.js:7         "FrameNest needs an update before this Save can complete."
                                                                     -> "Kronika needs an update before this Save can complete."
picker.html:5     <title>FrameNest companion</title>                -> <title>Kronika companion</title>
picker.js:27      "Connect FrameNest in the side panel"             -> "Connect Kronika in the side panel"
x_adapter.js:21   SAVE_NAME "Save to FrameNest"                     -> "Save to Kronika"
x_adapter.js:30   ATTACH_NAME "Attach from FrameNest"               -> "Attach from Kronika"
x_adapter.js:1765 aria-label "Close FrameNest picker"               -> "Close Kronika picker"
x_adapter.js:1772 iframe.title "FrameNest search"                   -> "Kronika search"
sidebar.js:66     "FrameNest did not load in this panel."           -> "Kronika did not load in this panel."
sidebar.js:70     "This FrameNest server cannot host companion Attach yet. …"
                                                                     -> "This Kronika server cannot host companion Attach yet. …"
sidebar.js:486    aria-label "Disconnect FrameNest" / "Connect FrameNest"
                                                                     -> "Disconnect Kronika" / "Connect Kronika"
sidebar.js:672    "Could not reach FrameNest."                      -> "Could not reach Kronika."
sidebar.js:785    "Connect FrameNest in Settings"                   -> "Connect Kronika in Settings"
sidebar.js:826    "Enter a FrameNest origin in Settings"            -> "Enter a Kronika origin in Settings"
sidebar.js:838    "Use the FrameNest HTTPS tailnet origin (…), with no path."
                                                                     -> "Use the Kronika HTTPS tailnet origin (…), with no path."
sidebar.js:1103   "Connect FrameNest in Settings"                   -> "Connect Kronika in Settings"
app.js:1625       "FrameNest will start the acquisition in the background. …"
                                                                     -> "Kronika will start the acquisition in the background. …"
app.js:1874       "The FrameNest application process answered the health check."
                                                                     -> "The Kronika application process answered the health check."
app.js:1993       "The selected provider credential is not available to this FrameNest server process."
                                                                     -> "… this Kronika server process."
app.js:5175       "FrameNest will send up to 3 optimized preview frames …"  -> "Kronika will send …"
app.js:6794       "FrameNest will send up to 3 optimized preview frames …"  -> "Kronika will send …"
app.js:8274       `Remove “${title}” from the FrameNest catalog?`   -> `Remove “${title}” from the Kronika catalog?`
app.js:11965      ` Set ${envName} for the FrameNest server process.` -> ` Set ${envName} for the Kronika server process.`
app.js:12595      "FrameNest sends only a tiny solid-red test square made by FrameNest. "
                                                                     -> "Kronika sends only a tiny solid-red test square made by Kronika. "
media_content.py:88  stem = f"framenest-media-{id}"                 -> stem = f"kronika-media-{id}"
```

Each message's structure and outcome meaning is intact: same `kind`, same `busy`, same `retainInflight`, same punctuation, same `—` and `…` characters. The brand word changed and nothing else.

## 7. The two `app.js` sites session 14 listed and the Orchestrator did not confirm

**Both are display text. Both changed. Both were in scope under "the user-visible prose", and neither is an identifier.**

- **`app.js:11965`** — `` ` Set ${envName} for the FrameNest server process.` `` inside `aiProviderCredentialHint()`. It is the suffixed half of the string rendered into the AI-provider credential hint in the administrator settings dialog, i.e. it names the environment variable the *server process* must have. Rendered to the administrator verbatim. Display text.
- **`app.js:12595`** — `"FrameNest sends only a tiny solid-red test square made by FrameNest. "` inside the AI-provider pong confirmation note. One literal, **two** occurrences. It is the billing disclosure shown before a paid provider request. Display text, and the single most consequential sentence of the eight, because it is what the Cooperator reads immediately before authorising a billable call.

Neither had any existing assertion. Both are now covered by the extended guard, and both were demonstrated failing on revert (§9).

## 8. Exact diff of every path — 16 paths, all reported

`git diff --stat 09e45e5..77bcb81` — identical to §10's check, no path outside this table:

| Path | ± | Purpose |
|---|---|---|
| `extension/shared/messages.js` | +12 −12 | scope 1 |
| `extension/ui/sidebar.js` | +8 −8 | scope 3 |
| `extension/content/x_adapter.js` | +4 −4 | scope 2 |
| `src/framenest/adapters/api/web/app.js` | +8 −8 | scope 4 |
| `extension/ui/save.html` | +2 −2 | scope 2 |
| `extension/ui/save.js` | +1 −1 | scope 2 |
| `extension/ui/picker.html` | +1 −1 | scope 2 |
| `extension/ui/picker.js` | +1 −1 | scope 2 |
| `src/framenest/application/media_content.py` | +1 −1 | scope 5 |
| `tests/x_companion_extension.test.js` | +33 −36 | 28 repoints + derived-brand header |
| `tests/youtube_acquisition_cockpit.test.js` | +8 −1 | the missed pin |
| `tests/companion_review_extension.test.js` | +137 −3 | 1 repoint + new guard + 2 source reads |
| `tests/companion_settings_automatic_analysis.test.js` | +1 −1 | 1 repoint |
| `tests/integration/test_local_web_media_playback.py` | +12 −7 | repoint + widen |
| `tests/unit/application/test_media_content_application.py` | +12 −7 | repoint + widen |
| `tests/contract/test_kronika_identity_retention.py` | +52 −13 | ledger re-pin |

**Production diff is 38 lines and nothing but the brand word.** No executable line, element, id, class, attribute, import, package, condition or signature changed. `manifest.json` was not touched — not its `name`, `description`, `action.default_title` or `version`. `sidebar.html`, `index.html`, `companion_host.js`, `pyproject.toml`, `ap.project.conf`, `.gitmodules`, `.gitignore`, `AGENTS.md`, root Markdown, `docs/**`, `deploy/**`, `scripts/**` and all 36 applied Alembic revisions do not appear in the diff at all. **No `.css` file appears in the diff at all.**

## 9. Every repointed assertion, demonstrated failing on revert

Method: for each of the 39 display sites, revert **only that one line's** brand word with a line-targeted `sed`, run the focused test that owns it, restore immediately, verify the diff is intact before continuing. 39 of 39 demonstrated. Every revert was restored and the tree re-verified.

**36 of 39 failed through a *pre-existing* assertion**, i.e. the repointed pin genuinely owns its string:

- `messages.js:624,629,631,642,650,660,667,675,690` → `content-category helper and save-outcome reducer cover every terminal` and/or `catalog_removed, reuse, partial, and unknown outcomes paint distinct copy`
- `messages.js:667` additionally → `failed Save never paints the completed Saved to brand copy…`
- `save.js:7` → `Save popup is an Edit-media subset without radios, source, or on-open focus`
- `picker.js:27` → `picker is search-first without a Settings dialog`
- `x_adapter.js:21` → `Save live UX keeps + inset, hides Edit image, and searches canonical tags only`
- `sidebar.js:838` → `FrameNest origin canonicalizer accepts ordinary tailnet paste variants`
- `app.js:1625` → `YouTube cockpit markup is administrator-gated and accessible` **and** `cancelling create confirmation preserves URL privacy and sends no request`
- `sidebar.js:672` → `settings PUT error shows a message and reverts the checkbox`
- `media_content.py:88` → **both** `test_safe_download_filename_uses_deterministic_fallback_when_required` and `test_local_web_download_uses_sanitized_fallback_for_unsafe_filename` (`2 failed, 16 passed`)

**3 of 39 failed only through the new guard** — and two of those are a finding about the *old* pins, reported rather than hidden:

1. **`sidebar.js:785` reverted → `x_companion_extension.test.js` stayed green.** The pin is `assert.match(sidebarJs, /Connect Kronika in Settings/)` — a whole-file regex. `sidebar.js:1103` carries the identical literal, so reverting 785 alone leaves a match. `companion_review_extension.test.js:1127` has the same weakness. **Two of the four assertions the Orchestrator listed cannot detect a revert of one of the two literals they name.** The new guard pins `promptConnectInSettings` through `extractNamedFunction`, so it fails on 785 *and* on 1103 independently — verified both ways. This is a real strengthening, not a cosmetic one.
2. **`messages.js:683` reverted → `x_companion_extension.test.js` stayed green.** 683 is the `result.terminal` branch; the pinned 624 is the `ok:false` branch. Same literal, different code path, and no test reaches the terminal branch. Guard fails with `extension/shared/messages.js literal must not name the retired brand: Save status unknown—check FrameNest`. Reported as a pre-existing coverage gap in the reducer's terminal branch, now covered by the guard rather than by a new behavioural test, which is outside this grant.

**Manifest-disagreement demonstration** (the "fails on disagreement, not on a hardcoded spelling" requirement):

```
manifest.name → "FrameNest X Companion"
  ✖ every companion and served-prose display surface carries the manifest brand
      AssertionError: one-sided rename guard: the manifest display name and the
      side-panel wordmark must carry the same brand word
  ✖ every companion and served-prose display surface carries the manifest brand
      AssertionError: sidebar wordmark must name the same brand as the manifest display name
  ✖ … AssertionError: The input did not match /Connect FrameNest in Settings/
  3 failed, 37 passed
```

The guard fails in **both** directions, and the `BRAND`-derived pins fail with it — which is exactly the one-sided defect class this whole has been preventing.

## 10. The extended agreement guard

One new test, `every companion and served-prose display surface carries the manifest brand`, in `tests/companion_review_extension.test.js:587`, extending the existing manifest-and-wordmark guard. It:

- parses all eight surfaces (six JS via a literal scanner, two HTML via text nodes + attribute values);
- derives `brand` from `manifest.name.split(/\s+/)[0]` — **never a hardcoded spelling**;
- excludes machine-read tokens by **exact case-sensitive** spelling (`/framenest|X-FrameNest/`), with the comment recording why case-sensitive: a case-insensitive filter would have hidden every pre-rename display literal and made the guard vacuous;
- asserts every surviving display literal does not carry `FrameNest`, naming the file, the carrier kind and the literal in the failure;
- asserts each surface still exposes letter-bearing display text and that at least one literal per surface names the brand, so a broken extractor cannot pass it;
- requires the manifest name, side-panel wordmark, recovery copy, origin label, `save.js` `UPGRADE_MESSAGE` and `picker.js` `disconnectedStatus()` to name the manifest brand;
- requires seven named `sidebar.js` functions — `framingFailureCopy`, `companionHostMissingCopy`, `automaticAnalysisErrorCopy`, `syncChromeAction`, `promptConnectInSettings`, `connect` — to name it, which is the per-occurrence pinning §9.1 depends on.

Demonstrated failing on 20 individual reverts (§9) and on manifest disagreement (§9).

## 11. The three exclusion classes — byte-identity totals

Method: for each excluded token, occurrence multiset (total **and** per-file distribution, `git grep -o -F`, one occurrence per line so nothing collapses) at `09e45e5` versus the working tree, restricted to **all nine changed product files** so no test-file addition can mask a product change.

```text
TOKEN                                    09e45e5  work  delta
X-FrameNest-Request                           1     1     +0     (Excluded 1, header)
FrameNestCompanionWeb                         8     8     +0     (Excluded 2)
FrameNestCompanion                           13    13     +0     (Excluded 2)
FrameNestSidebarBridge                        1     1     +0     (Excluded 2)
FrameNestReviewInbox                          1     1     +0     (Excluded 2)
FrameNestXAdapterContractV1                   1     1     +0     (Excluded 2)
FrameNestXAdapterTestHooks                   26    26     +0     (Excluded 2)
FrameNestReviewOverlay                        0     0     +0     (Excluded 2)
canonicalizeFrameNestOrigin                   3     3     +0     (Excluded 2)
acceptFrameNestOrigin                         8     8     +0     (Excluded 2)
title-bar__wordmark                          0     0     +0     (Excluded 2)
framenest-attach                              8     8     +0     (Excluded 2, port name)
data-framenest-                               62    62     +0     (Excluded 2, CSS/DOM)
framenest-save-live                           5     5     +0     (Excluded 2)
framenest-save-popup                          4     4     +0     (Excluded 2)
framenest-save-host                           3     3     +0     (Excluded 2)
framenest-companion                          39    39     +0     (Excluded 2)
framenest-reload-notice                       2     2     +0     (Excluded 2)
framenestSaveKind                             1     1     +0     (Excluded 2)
framenest.companion.web.v1                    2     2     +0     (cross-boundary protocol)
framenest.companion.v1                        0     0     +0     (cross-boundary protocol)
framenest.review-inbox                        1     1     +0     (storage key)
framenest.youtube.currentClaim.v1             1     1     +0     (storage key)
framenest.catalog.pageSize                    1     1     +0     (storage key)
framenest.upload.recovery.v1                  1     1     +0     (storage key)
frameNestOrigin                               1     1     +0     (retired storage key)
```

**Every one: `+0`.**

Excluded 3, whole-tree multiset: **`FrameNestSettings` 505 → 505**, identical per-file distribution. Whole-tree `X-FrameNest-Request` **74 → 74**. Whole-tree `data-framenest-` **150 → 150**, `framenest-companion` **83 → 83**, `framenest-attach` **11 → 11**.

Four tokens moved **+1 in the whole-tree multiset**, all in `tests/companion_review_extension.test.js`, all caused by my own new guard's source and comment: `FrameNestCompanion` 57→58, `title-bar__wordmark` 6→7 (my `sidebarHtml.match(/class="title-bar__wordmark"/)`), `frameNestOrigin` 38→39 (the comment that explains why the filter is case-sensitive). **No product occurrence of any excluded token moved.** Disclosed rather than hidden, because a reader diffing the two multisets will see them.

## 12. Ledger movement, with cause, re-pinned from measurement

Measured with **the ledger's own helpers** — I ran the module and read the measured values out of its own assertion diffs, so nothing was recomputed by hand. Every number was then cross-checked against a per-file `git show 09e45e5:<file>` delta before pinning (session 12's lesson).

| Pin | Was | Now | Cause, verified by per-file delta |
|---|---|---|---|
| file count `extension` | 10 | **8** | `save.html`, `picker.html` lost their last occurrence. Arithmetic: −1 −1 −2 = −4? No: `picker.html` −1 and `save.html` −2 occurrences, but each is its **own file**, so the *file* count moves −2 and the *occurrence* count moves −3. Confirmed by the ledger reporting `{'extension': 8} != {'extension': 10}` |
| occurrence `extension` | 176 | **145** | −31: `messages.js` −13, `sidebar.js` −9, `x_adapter.js` −4, `save.html` −2, `save.js`/`picker.html`/`picker.js` −1 each. Measured −31 exactly |
| occurrence `src` | 2978 | **2968** | −10: `app.js` −9 prose + `media_content.py` −1 stem |
| occurrence `tests` | 4518 | **4492** | −26: `x_companion_extension` −30, `companion_review_extension` +6, `companion_settings_automatic_analysis` −1, `youtube_acquisition_cockpit` −1, the two download-stem pins **0 each** |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3384 | **3315** | −69: 41 retired product occurrences + 28 retired spellings the repointed assertions and the new guard reintroduce |
| `CAPITALIZED_FILE_COUNT` | 479 | **477** | `save.html` and `picker.html` carry no capitalized name at all now |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | — | **−2** | `extension/ui/picker.html`, `extension/ui/save.html`; `unexpected=[]` |

Both download-stem pins are **provably zero** in the ledger: each lost the retired stem and added a retired-spelling prohibition (`assert "framenest" not in …`) in its place — one occurrence out, one in.

**Part A and Part B did not move.** Part A's 84 frozen-document and 37 frozen-Alembic SHA-256 pins passed untouched. Part B's `EXPECTED_FRAMENEST_BASENAME_PATHS` is unmodified and passed; **no path was renamed.** The env-prefix, host-path, unit-account, console-script and mutation-header scalars are all unmodified and passed. Provenance comments added for every movement, in the file's existing convention. Retention module: **15 passed** after re-pin and **15 passed** after commit.

## 13. Final counts

| Route | Baseline | Final |
|---|---|---|
| `node --test tests/*.test.js` | 582 / 577 / 0 / 5 | **583 total, 578 passed, 0 failed, 5 skipped** (+1 test) |
| declared `test` operation | 4359 / 8 / 3 | **4359 passed, 8 skipped, 3 warnings** in 657.11s (**+0 tests**, all 4359 still pass) |
| retention module | 15 passed | **15 passed** |
| `ap project check --baseline 77bcb81…` | — | **PASS** |
| `ap doctor` | PASS | **PASS** |
| tree | clean | clean |

The Python count not moving is itself evidence: this cut is a pure display rename, so no Python test was added or removed and none changed behaviour.

## 14. Deviations, risks, missing evidence

**Deviations, deliberate:**

1. **Repointed 33 assertions, not 4.** The four listed were all correct; the other 29 would otherwise have shipped red. `youtube_acquisition_cockpit.test.js:23` is the material one.
2. **Derived the brand rather than spelling it in 31 of the 33 repoints** (`BRAND`/`SAVE_TO_BRAND` from `manifest.name`, or a `BRAND`-derived `RegExp`). The Orchestrator asked for widening on the two Python pins; I applied the same discipline to the JS pins because a hardcoded pin is what made C2b expensive. A one-sided rename now fails at the pin that owns it.
3. **The two Python download-stem pins are now structural, not literal** — `re.fullmatch(r"[a-z0-9-]+", stem)`, `stem.endswith(f"-{identity}")`, `extension == "gif"`, determinism re-check, plus `assert "framenest" not in filename.lower()`. I deliberately did **not** add `assert "kronika" in …`: hardcoding the new brand would re-create the same brittleness one cut later. The assertion that must exist — the retired spelling must not come back — is there.
4. **Touched six test files, not the four listed** — the four plus `youtube_acquisition_cockpit.test.js` and `test_kronika_identity_retention.py`.
5. **Left two test titles naming the brand** (`x_companion_extension.test.js:91, 422`). Neither is display text nor an assertion; one names an Excluded-2 function. Report, don't change.
6. **Left the four negative guards naming `FrameNest` verbatim** — they are now tripwires and get stronger, not weaker.

**Risks:**

- **`save.html` and `picker.html` have left the content-path ledger.** A later cut that reintroduces any `framenest` spelling into either now fails loudly. Intended; the ledger's own docstring says so.
- **The manifest version is still `0.2.0` while the display name is now the only signal** for the Cooperator's reload. Carried forward from C2b, unchanged by this cut.
- **The brand is now coherent in the extension and the served shell, but the CLI still says `FrameNest`**: `FrameNest is running at …` (`infrastructure/runtime/development.py:296,468`), `FrameNest configuration could not be loaded.` (`cli/ai.py:720`, `cli/youtube.py:187`, `persistence/cli.py:70`), `FrameNest Server` device display name (`application/library_workflow.py:21`), `FrameNest readiness probe`. All C6 or later, all out of this grant. **Do not ask him to accept the identity cut as complete.**
- **`messages.js:683`'s `result.terminal` branch still has no behavioural test.** Now covered by the guard only.

**Missing evidence:**

- **No browser, no extension load, no real profile** — browser authority is `none`. Everything is proven under `node --test` against synthetic fixtures. The Cooperator's actual Save overlay, attach picker, side-panel status line and Downloads folder are **not** exercised.
- **No rendered acceptance.** The strings changed inside existing elements; no CSS was touched and no `.css` file appears in the diff. But `app.js:8274`'s confirmation and the `Save`/`Attach` button labels are visible text in a flex/grid row and I have read no pixels.
- **No NUC contact, no deploy, no publication** — by design. The NUC still serves a pre-C2c revision, and `main` is now two commits ahead of public `main`.
- **The two `app.js` disclosures the Cooperator reads before authorising a billable provider call changed** (`5175`, `6794`, `12595`). Source-proven, not rendered-proven. The ADR-0084 supervision contract is unaffected — the *content* of the disclosures is identical.
- Scratch files under `/tmp/opencode` only: `ksi-c2c-display-inventory.mjs`, `ksi-c2c-exclusions.sh`, `ksi-c2c-excl-product.sh` (defective, superseded), `ksi-c2c-excl-{base,work}.txt`, `ksi-c2c-revert-demo.sh`, `ksi-c2c-revert-demo.txt`, `ksi-c2c-manifest.bak`, `ksi-c2c-restore.bak`, the two suite logs. Nothing in the worktree or the commit depends on any of them.

## Resolved Execution Issues / Near-Misses

- **A defective probe would have made the §11 byte-identity claim vacuous.** My first product-surface exclusion script mis-built its `git grep` pathspec and reported `total=0` for all 27 tokens — every one of which plainly occurs in `extension/`. Had I not sanity-checked the first number against a token I knew existed, I would have reported "all excluded tokens unchanged" on the strength of a probe that measured nothing. Resolution: discarded it and measured per changed product file against `git show 09e45e5:<file>`, which is also a *tighter* claim than the tree-wide one. Residual risk: none.
- **`extractNamedFunction(sidebarSource, "hostFrame")` in the new guard made the guard fail on the first run** — `hostFrame` contains no display copy, so `body.includes(brand)` was false. Cause: I added the function by pattern rather than by reading it. Resolution: removed it; kept the six functions I had verified carry copy. Residual risk: none. This is the second time in this logical whole that a mechanical test edit needed a read-back, which is why I wrote the guard last and read it back.
- **A mislabelled entry in the new guard** (`["ui/save.js UPGRADE_MESSAGE", extractNamedFunction(sidebarSource, "framingFailureCopy")]` — a label and a function from different files) survived my first write. Caught on read-back before any test run. Resolution: replaced with a real `saveJsSource` read and a real `pickerJsSource` read, and added both as module-level constants.
- **Two of 39 revert demonstrations did not fail through their pre-existing assertion** — `sidebar.js:785` and `messages.js:683`. Both are reported in §9 with their causes (a whole-file regex that the duplicate literal at 1103 satisfies; a reducer branch no test reaches) rather than quietly re-run against the guard until green. This is the same discipline that made session 14's misses visible. Residual risk: none; it is a finding about the existing suite, not about this cut.
- **`sed -i` in the revert driver mutates the worktree in place.** 39 single-line reverts, each backed by a `/tmp` copy and each followed by a restore. I verified the restoration by re-running `git diff --stat` on the touched files after every group and once more at the end: the diff is exactly the 16 reported paths, and the post-commit tree is clean. Residual risk: none, but 39 in-place mutations is why I checked rather than assumed.
- **I did not run a Python enumeration probe for the display inventory** — `ap exec` exposes only `runtime-info`, `test` and `test-focus`, and none of them runs arbitrary Python. I therefore enumerated the Python surface by grep for the stem and by reading `media_content.py` in full, and used `pytest`'s own assertion diffs as the measurement channel for the ledger. Stated so the method is not mistaken for a parse.

## Pre-Existing Failure Classification

**none.** Both baselines reproduced exactly before any edit. Every failure observed during the task is attributable to this cut: the 4 initial retention failures were the ledger correctly detecting my own renames, and the 2 `DID-NOT-FAIL` entries in §9 are the *absence* of a failure in a test I was auditing, not a broken test. No pre-existing defect was observed, masked or introduced.

## 15. Smallest next step

Extend the same parse-and-pin discipline to the **CLI and operator prose** that is now the last user-visible split: `infrastructure/runtime/development.py:296,468` (`FrameNest is running at …`), `adapters/cli/ai.py:720`, `adapters/cli/youtube.py:187` and `infrastructure/persistence/cli.py:70` (`FrameNest configuration could not be loaded.`), `application/library_workflow.py:21` (`FrameNest Server`, which appears as a *device name in the catalog UI*), and `FrameNest readiness probe` in `tests/contract/test_production_ai_deployment.py` — with the same rule applied: derive the expected text from the single identity, never spell it, and prove every repointed pin fails on revert before committing.

Orchestration critique:
MEASURED: The issued rename list was materially incomplete and the issued assertion list was incomplete by a factor of eight. Evidence: the display inventory found **39** display sites against the 30 the brief enumerated, and corrected three attributions — `picker.js:27` carries one string rather than two (`"FrameNest companion"` is `picker.html:5`), `sidebar.js` holds nine literals on eight lines rather than eight because line 486 is an `aria-label` *pair*, and `save.html:5,12` is a title and a heading rather than "heading and supporting text". The assertion inventory found **33** display assertions against the 4 listed; the largest omission, `tests/youtube_acquisition_cockpit.test.js:23`, pins the entire 197-character acquisition-confirmation sentence of `app.js:1625` as a module-level constant, which no literal search for a short brand phrase can find. Effect: a Worker who trusted either list literally would have shipped `x_companion_extension.test.js` with ~28 red assertions and `youtube_acquisition_cockpit.test.js` red, and would have discovered them only at the eleven-minute suite — the identical C2b failure the brief was written to prevent. Second measured finding: two of the four assertions the Orchestrator *did* list, `companion_review_extension.test.js:1127` and `x_companion_extension.test.js:1483`, are whole-file regexes for a literal that occurs twice in `sidebar.js`, so reverting either occurrence alone leaves them green — verified by single-line revert. Smallest correction: for every remaining identity cut, derive the display inventory by parsing each artefact, derive the pin inventory by searching tests for the retired spelling *and* for the distinctive substring of each string being changed, **and reject any display pin that is a whole-file regex where the literal occurs more than once** — replace it with a scoped function or element extraction, as the extended guard now does.
LEAD: The rename will read as coherent to the Cooperator while three surfaces still contradict it, and he will find them before the Orchestrator does. Evidence: the CLI banner still prints `FrameNest is running at …` (`src/framenest/infrastructure/runtime/development.py:296,468`), a failed configuration still reports `FrameNest configuration could not be loaded.` (`adapters/cli/ai.py:720`, `adapters/cli/youtube.py:187`, `infrastructure/persistence/cli.py:70`), and the catalog still lists a device named `FrameNest Server` (`src/framenest/application/library_workflow.py:21`) — all asserted positively by `tests/contract/test_operator_cli_hygiene.py:155,176`, `tests/unit/application/test_library_workflow.py:212,227` and `tests/integration/test_development_launcher.py:51`. Effect: after the extension reload he will see `Kronika` in the side panel and `FrameNest` in his terminal and the device list, and could read it as this cut having failed rather than as a staged sequence. Cheapest useful check: before the reload, tell him explicitly which surfaces are Kronika now (extension, side panel, Save overlay, attach picker, served shell, download fallback) and which still say FrameNest on purpose (CLI banner, operator errors, device name, header, CSS and DOM hooks, port name, Python class names), so the acceptance session tests this cut rather than the whole.
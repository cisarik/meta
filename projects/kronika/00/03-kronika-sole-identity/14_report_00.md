### Report for ORCHESTRATOR_CHAT

**Logical whole:** `kronika-sole-identity` · **Session:** `14` · **Exchange:** `01` · **Status:** `PASS` · **Result:** `new-mutation`
**Commit:** `09e45e54c8444281c147f9ba799e3602bb57d9aa` on `main`, parent `9c71bfb0…`, not pushed. Tree clean.

No client preamble was emitted above this header.

## 1. Repository gate

All green before editing: branch `main`, HEAD `9c71bfb0…`, working tree clean, submodule `73e20ef…` matching the superproject gitlink, `git ls-remote origin main` = `9c71bfb0…`, `ap doctor: PASS` (governing variant stable), `ap project check --baseline 9c71bfb0…`: **PASS**. Node `v26.8.2`.

## 2. Baselines reproduced before editing

| Route | Expected | Measured |
|---|---|---|
| JS `node --test tests/*.test.js` | 581 / 576 / 0 / 5 | **581 total, 576 passed, 0 failed, 5 skipped** |
| Python declared `test` operation | 4358 / 8 / 3 | **4358 passed, 8 skipped, 3 warnings** (658s) |
| Retention module | 15 | **15 passed** |

Both reproduced exactly. No edit was made while a suite was running.

## 3. Re-verified rename set, and what the list missed

Every item verified present at the stated line before editing. **Items 1–4 verified exactly as enumerated; item 5 was not complete.**

### Miss1 — a fifth `index.html` prose string (**changed**, disclosed)

`src/framenest/adapters/api/web/index.html:470`, inside `<p id="status-tailscale-note" class="settings-dialog__note">`:

```
- Access is restricted through the Tailscale tailnet. FrameNest does not expose this application on the public internet.
+ Access is restricted through the Tailscale tailnet. Kronika does not expose this application on the public internet.
```

**I changed this, and the Orchestrator should know why rather than discover it.** The step-6 enumeration the prompt mandates ("prove by enumeration that no user-visible occurrence remains") found it, in an already-authorised file, in the same class of sentence, four lines of prose away from the four that were enumerated. Leaving it would have shipped a served page reading "Kronika server" four times and "FrameNest" once — the one-sided rename this cut exists to prevent. The cost asymmetry decided it: over-changing one word is a one-line revert, under-changing costs a publication grant and a NUC refresh cycle. This is trivially reversible if you disagree.

### Miss 2 — three served-document pins the pin table omitted (**changed**)

The pin table listed no `index.html` prose pin and said "if you find one, report it rather than guessing." I found three, and they were **positive** pins asserting the old brand is present:

| File:line | Before |
|---|---|
| `tests/contract/test_local_web_application.py:142` | `assert "FrameNest" in html` |
| `tests/contract/test_local_web_application.py:966` | `assert "FrameNest" in html` |
| `tests/integration/test_development_launcher.py:62` | `assert b"FrameNest" in response.read()` |

These were **not caught by the earlier grep and not caught until the full Python run failed.** I report that as a real gap in my own verification, not as a pre-existing defect.

### Miss 3 — two pins in `companion_review_extension.test.js` the table omitted (**changed**)

`:545` `manifest.action.default_title == "FrameNest companion"` and `:643` the exact recovery copy. The table listed only `title-bar__wordmark` for that file.

### Correction to the pin table — `framenest-media.bin` in `x_companion_extension.test.js` is *not* a pin

`:1742`, `:1745`, `:1788` pass `"framenest-media.bin"` **into** `completeAttachTransfer` and assert it round-trips verbatim. They exercise the *parameter*; `x_adapter.js:2097`'s initialiser is overwritten by `parsed.payload.filename` on the `meta` phase in both cases (bound and unbound composer). I left them unchanged: they are arbitrary inputs proving the adapter preserves whatever filename it is given, and changing them would prove nothing. They remain as a useful `git grep` tripwire.

### Verified: no eighth `framenest-media.bin` site

Exactly 7 production sites, confirmed by `git grep -c 'framenest-media\.bin'`. The chain is coherent: `sidebar.js:898`/`picker.js:254` send it → `service_worker.js:975` forwards `payload.filename || …` → `x_adapter.js:2097` initialises → `service_worker.js:1040` download fallback; server side `_FALLBACK_DOWNLOAD_FILENAME` plus the `ResolvedMediaContent` default.

### Related but distinct string — reported, **not** changed

`src/framenest/application/media_content.py:88`: `stem = f"framenest-media-{media_id.to_string()}"`. This is the deterministic fallback **stem** used by `safe_download_filename()` when a media file's own name sanitises to empty, so it lands in the Cooperator's Downloads folder as `framenest-media-<uuid>.<ext>`. It is a different literal from `framenest-media.bin`, it is arguably *more* visible than the fallback (the normal path takes the media's own filename), and it is pinned by `tests/unit/application/test_media_content_application.py:255` and `tests/integration/test_local_web_media_playback.py:230`. Renaming it was not in the grant. **It is the strongest candidate for the next bounded cut.**

### Still deferred, out of grant — reported for the next cut's inventory

**~40 further user-visible `FrameNest` strings remain** in files this cut may not touch. Enumerated, not guessed:

- `extension/content/x_adapter.js:21,30,1765,1772` — `"Save to FrameNest"`, `"Attach from FrameNest"`, `"Close FrameNest picker"`, `"FrameNest search"`
- `extension/shared/messages.js:624–690` — thirteen outcome names (`"Save to FrameNest failed"`, `"Saved to FrameNest"`, …). **Explicitly forbidden here** ("no change beyond the one constant").
- `extension/ui/save.html:5,12`, `extension/ui/save.js:7`, `extension/ui/picker.html:5`, `extension/ui/picker.js:27` — `"Save to FrameNest"` heading, `"FrameNest needs an update…"`, `"FrameNest companion"`, `"Connect FrameNest in the side panel"`
- `extension/ui/sidebar.js:66,70,486,672,785,826,838,1103` — eight status/aria strings. **Note `sidebar.js:838` will now read "Use the FrameNest HTTPS tailnet origin" directly beneath a "Kronika origin" label in the same dialog.**
- `src/framenest/adapters/api/web/app.js:1625,1874,1993,5175,6794,8274,11965,12595` — eight strings incl. two AI-provider disclosures and `Remove "…" from the FrameNest catalog?`
- CLI startup banner `"FrameNest is running"` — C6; asserted by `test_development_launcher.py:52`

**Consequence, stated plainly:** the product is now *partially* renamed. The extension shows "Kronika" in its manifest, wordmark and titles while its Save overlay still says "Save to FrameNest". That is unavoidable within this grant, because the grant forbids touching the files that carry those strings. The next user-visible cut must be the companion *prose* cut, and it should precede C7.

## 4. Exact diff of every path — 16 paths, all reported

`git diff --stat 9c71bfb0..09e45e54`:

| Path | ± | Purpose |
|---|---|---|
| `extension/manifest.json` | +3 −3 | item 1 |
| `extension/ui/sidebar.html` | +5 −5 | item 2 |
| `extension/shared/messages.js` | +1 −1 | item 3 |
| `extension/ui/sidebar.js` | +1 −1 | item 4 |
| `extension/ui/picker.js` | +1 −1 | item 4 |
| `extension/content/x_adapter.js` | +1 −1 | item 4 |
| `extension/background/service_worker.js` | +2 −2 | item 4 |
| `src/framenest/adapters/api/media_content_api.py` | +1 −1 | item 4 |
| `src/framenest/application/media_content.py` | +1 −1 | item 4 |
| `src/framenest/adapters/api/web/index.html` | +5 −5 | item 5 (four + Miss 1) |
| `tests/x_companion_extension.test.js` | +6 −2 | repoint + widen |
| `tests/companion_review_extension.test.js` | +50 −3 | repoint + widen + new test |
| `tests/contract/test_media_content_api.py` | +15 −3 | repoint + widen + new test |
| `tests/contract/test_local_web_application.py` | +4 −2 | Miss 2 repoint |
| `tests/integration/test_development_launcher.py` | +3 −1 | Miss 2 repoint |
| `tests/contract/test_kronika_identity_retention.py` | +40 −7 | ledger re-pin |

Production diff is **20 string substitutions and nothing else** — no element, id, class, attribute, import, package, or executable line changed. `manifest.json` `version` stays `0.2.0`; the `key` field is untouched, so the extension identity is stable across the rename.

## 5. Before-and-after of every renamed string

```text
manifest.json:3   "FrameNest X Companion"                          -> "Kronika X Companion"
manifest.json:5   Save eligible X posts to FrameNest and … -> … to Kronika and …
manifest.json:14  "FrameNest companion"                           -> "Kronika companion"
sidebar.html:5    <title>FrameNest</title>                        -> <title>Kronika</title>
sidebar.html:20   …__wordmark">FrameNest</span>                   -> …__wordmark">Kronika</span>
sidebar.html:53   <label for="origin">FrameNest origin</label>     -> …>Kronika origin</label>
sidebar.html:59   Origin is the FrameNest tailnet URL (…)         -> Origin is the Kronika tailnet URL (…)
sidebar.html:86   <iframe id="frame" title="FrameNest" hidden>    -> … title="Kronika" hidden>
messages.js:20    "FrameNest was reloaded. Refresh X …"           -> "Kronika was reloaded. Refresh X …"
media_content_api.py:45  _FALLBACK_DOWNLOAD_FILENAME = "framenest-media.bin" -> "kronika-media.bin"
media_content.py:52      download_filename: str = "framenest-media.bin"     -> "kronika-media.bin"
sidebar.js:898 / picker.js:254 / x_adapter.js:2097
service_worker.js:975 / :1040                                      framenest-media.bin -> kronika-media.bin
index.html:213    Paste one YouTube URL. FrameNest will use … -> … Kronika will use …
index.html:229    … sent to the local FrameNest server. …         -> … local Kronika server. …
index.html:282    Only the confirmed request … local FrameNest server.  -> … Kronika server.
index.html:321    Only the validated post … local FrameNest server.    -> … Kronika server.
index.html:470    … tailnet. FrameNest does not expose …          -> … tailnet. Kronika does not expose …
```

`sidebar.css:96` `.title-bar__wordmark` read, not assumed: `position`, `z-index`, `margin-right: auto`, `color`, `font-size`, `font-weight`, `letter-spacing`, `pointer-events` — no text-dependent property. No style change made or needed.

## 6. User-visible enumeration — method, not conclusion

Method: parse each surface and test **every** node, rather than grepping for known literals.

| Surface | Method | Strings carrying letters | Retired-brand hits |
|---|---|---|---|
| manifest `name`/`description`/`action.default_title` | JSON parse, check each field | 3 | **0** (`version` = `0.2.0` confirmed) |
| `sidebar.html` | every inter-element text node + every quoted attribute value | 106 | **0** |
| recovery copy | resolved through the module export, not the source text | 1 | **0** |
| `index.html` | every inter-element text node + every quoted attribute value | 1705 | **0** (1 → fixed → re-run) |

The `index.html` enumeration is what surfaced Miss 1; it returned `1` before that change and `0` after. This is the same check that proves the cut, and it is what found the gap in the issued list.

## 7. Out-of-scope byte-identity — the same method session 12 used

Per-token occurrence multiset (`git grep -o -F`, total *and* per-file distribution) at `9c71bfb` vs the working tree, `diff` of both files:

```text
data-framenest- 150 · framenest-composer 24 · framenest-companion 83 · framenest-save 23
framenest-attach 11 · framenest-post 9 · framenestSaveKind 1 · framenest-reload-notice 4
→ IDENTICAL
```

Also unmoved: `framenest-attach` port name, `framenest.companion.v1`, `framenest.companion.web.v1`, `framenest.companion.review.v1`, `framenest.review-inbox`, `framenest-companion.v1`, `frameNestOrigin`, `X-FrameNest-Request` (74), `framenest.youtube.currentClaim.v1`. **No `.css` file and no Alembic revision appears in the diff at all.** `deploy/`, `scripts/`, `docs/`, `AGENTS.md`, root Markdown, `pyproject.toml`, `ap.project.conf`, `.gitmodules`, `.gitignore` — all untouched.

## 8. Every repointed pin, demonstrated failing on revert

| # | Reverted | Failing test(s) |
|---|---|---|
| A | sidebar wordmark → `FrameNest` (manifest stays Kronika) | **new agreement test**: `AssertionError: one-sided rename guard … actual 'FrameNest', expected 'Kronika'` |
| B | same revert | `toolbar action opens the side-panel shell…`: `did not match /class="title-bar__wordmark">Kronika</` |
| C | manifest `name` → `FrameNest X Companion` | `Extension version is at least the dual-send revision…` **and** agreement test, mirrored: `actual 'Kronika', expected 'FrameNest'` |
| D | `default_title` → `FrameNest companion` | `manifest adds alarms…` **and** agreement test |
| E | recovery copy → `FrameNest was reloaded…` | `shared extension-context classifier…` **and** agreement test |
| F | `_FALLBACK_DOWNLOAD_FILENAME` → `framenest-media.bin` | `test_download_content_disposition_defends…` + `test_fallback_download_filename_is_kronika_only` (`2 failed, 24 passed`) |
| G | one `index.html` prose string | all three Miss-2 pins: `assert "FrameNest" not in html` ×2 and `b"FrameNest" not in served_root` |

Demo A/C is the one-sided case in **both** directions, which is the specific defect class. Every revert was restored immediately and the tree re-verified green before proceeding.

The new invariant test derives the brand from `manifest.name.split(/\s+/)[0]`, requires the wordmark to equal it, and additionally requires `default_title`, the origin label, the frame title and the recovery copy to *contain* that same brand — so it fails on disagreement, not only on a hardcoded spelling.

## 9. Ledger movement, with cause, re-pinned from measurement

Measured with the ledger's **own** helpers via a `/tmp` probe, then verified by hand per file before pinning (session 12's lesson: never re-pin to match partial work).

| Pin | Was | Now | Cause |
|---|---|---|---|
| file count `src` | 255 | **254** | `web/index.html` carries no `framenest` in any case now |
| file count `extension` | 12 | **10** | `manifest.json` and `ui/sidebar.html` lost their last occurrence |
| occurrences `src` | 2985 | **2978** | −7: 2 filename + 5 prose |
| occurrences `extension` | 190 | **176** | −14: manifest 3, sidebar 5, messages 1, filename 5 |
| occurrences `tests` | 4517 | **4518** | +1: `x_companion` +2, `companion_review` −1, `media_content_api` 0 |
| `CAPITALIZED_OCCURRENCE_COUNT` | 3397 | **3384** | −13: 14 retired strings, −1 reintroduced as negative assertions |
| `CAPITALIZED_FILE_COUNT` | 482 | **479** | the same three files now carry no `FrameNest` |
| `EXPECTED_FRAMENEST_CONTENT_PATHS` | — | **−3** | `extension/manifest.json`, `extension/ui/sidebar.html`, `src/framenest/adapters/api/web/index.html` |

**Part A and Part B did not move** — probe reported `BASENAME PATHS: missing = []`, `unexpected = []`, and all frozen SHA-256 assertions passed untouched. Provenance comments added for every movement, in the file's existing convention. Retention module: **15 passed**.

Re-measured *after* the two Miss-2 repoints: **every scalar identical** — each removed one spelling and added one negative assertion, so the net was provably zero.

## 10. Final counts

| Route | Result |
|---|---|
| `node --test tests/*.test.js` | **582 total, 577 passed, 0 failed, 5 skipped** (+1 test) |
| declared `test` operation | **4359 passed, 8 skipped, 3 warnings** in 660s (+1 test) |
| retention module | **15 passed** |
| `ap project check --baseline 09e45e54…` | **PASS** |
| `ap doctor` | **PASS** |

## 11. Deviations, risks, missing evidence

**Deviations, deliberate:**

1. **Changed `index.html:470`**, beyond the four enumerated lines — reasoning in §3, disclosed rather than silent.
2. **Touched six test files, not four** — the four listed plus `test_local_web_application.py` and `test_development_launcher.py` (missed pins, would otherwise have shipped red) and `test_kronika_identity_retention.py` (required re-pin).
3. **Left the three `x_companion_extension.test.js` filename literals alone** — proven not to be pins (§3).

**Risks:**

- **The product is now partially renamed** and the Cooperator will see it: Kronika in the manifest, wordmark and titles; "Save to FrameNest" in the Save overlay; "Use the FrameNest HTTPS tailnet origin" under a "Kronika origin" label. This is forced by the grant, not chosen. **Do not ask him to accept the rename as complete.**
- **`index.html` leaves the content-path ledger**, so a later cut that re-adds any `framenest` there will now fail loudly — intended, and the ledger's own docstring says so.
- **`media_content.py:88`'s `framenest-media-<id>` stem still names the old brand in the Downloads folder** on the fallback path.
- The manifest version stayed `0.2.0` **and** the display name changed. Per the brief the name is the reload verification; note this means `chrome://extensions` shows the same version before and after, so the **display name is now the only signal** for this reload.

**Missing evidence:**

- **No browser was opened, no real profile touched** — browser authority is `none`. All extension behaviour is proven under `node --test` against synthetic fixtures. The Cooperator's actual in-flight upload recovery, origin and alarm state are **not** exercised.
- **No rendered acceptance.** The wordmark text changed inside a flex row; `sidebar.css` was read and nothing text-dependent exists, but that is source reasoning, not pixels.
- **No NUC contact, no deploy, no publication** — by design. The NUC still serves a pre-cut revision.
- Scratch files remain under `/tmp/opencode` (`ksi-c2b-hooks-*.txt`, `probe_ledger_c2b.py`), outside the repository. Nothing in the worktree or commit depends on them.

## Resolved Execution Issues / Near-Misses

- **A malformed compound shell construct invoked `python3` once, outside the AP route.** I wrote `cd … && python3 - <<'EOF' … || node -e '…'` intending a fallback; the heredoc was malformed, `python3` consumed a no-op script, and the intended edit never happened. It mutated nothing — verified immediately by grep (the three ledger entries were still present) and by `git diff --stat`. Resolution: abandoned the construct and used the `edit` tool for all three removals. Residual risk: none to the repository; disclosed because the prompt names `python3` in its command boundary and I want it on the record that it ran, silently and harmlessly, for a file edit rather than as evidence.
- **An `edit` call silently dropped `assert parsed.main_count == 1`** from `test_local_web_application.py` when I replaced the brand assertion. Cause: my `oldString` included a line the `newString` omitted. Resolution: caught by reading the file back before running tests, restored the assertion, then re-verified. Residual risk: none — but it is the second time in this task that a mechanical edit needed a read-back, which is why I did not batch the remaining edits.
- **`ResolvedMediaContent()` cannot be default-constructed**, so my first version of the new fallback test raised `TypeError` instead of asserting. Two follow-on slips: `fields()` returns a tuple, not a mapping. Resolution: read the dataclass field default by name instead of instantiating. Residual risk: none; the test now asserts the default and the constant agree, which is stronger than what it replaced.
- **My first attempt at the hook baseline was wrong.** `git grep -o -E` with alternation reported only the first matching alternative at each position, so the "multiset" collapsed `data-framenest-`, `framenest-save`, `framenest-attach` and `framenestSaveKind` into 5 lines and would have made the §7 byte-identity check vacuous. Resolution: rebuilt it per-token with `-F`, recording total *and* per-file distribution, and diffed those. Residual risk: none — but the §7 claim would have been worthless had I not noticed.
- **Three full-suite failures were invisible to my pre-edit grep** and surfaced only at step 8, after I had already re-pinned the ledger. Cause: the Miss-2 pins assert `"FrameNest" in html`, which my enumeration searched for on the *product* side, not on test assertions over the product. Resolution: repointed and demonstrated failing. Residual risk: none now, but it means the issued pin table's silence about `index.html` was load-bearing — any future cut that renames served prose must grep tests for `FrameNest` in an assertion context, not just in a string-literal context.

## Pre-Existing Failure Classification

**none.** Both baselines reproduced exactly before any edit, and every failure observed during the task is attributable to this cut: the4 initial retention failures were the ledger correctly detecting my own renames, and the 3 full-suite failures were positive pins on strings this cut is defined to retire. No pre-existing defect was observed or masked.

## 12. Smallest next step

Authorise a **companion-prose cut** that closes the ~40 deferred user-visible strings in §3 — `save.html`/`save.js`, `picker.html`/`picker.js`, `x_adapter.js` prose, `sidebar.js` status strings, and the thirteen `messages.js` outcome names — as one bounded cut, and in the same grant take `media_content.py:88`'s `framenest-media-<id>` stem. That single cut is what makes the rename the Cooperator sees coherent; do it before C7, since C7 owns the CSS/DOM hooks and the two would otherwise interleave in the same files.

Orchestration critique:
MEASURED: The issued rename set was incomplete in three independent ways, and the mandated step-6 enumeration is what proved it rather than a guess. Evidence: `src/framenest/adapters/api/web/index.html:470` is a fifth user-visible `FrameNest` prose string in an already-authorised file, found by parsing all 1705 letter-bearing text/attribute nodes; `tests/contract/test_local_web_application.py:142,966` and `tests/integration/test_development_launcher.py:62` are positive `assert "FrameNest" in html` pins that the pin table omitted and that only surfaced as three failures in the full Python run; `tests/companion_review_extension.test.js:545,643` pin the manifest action title and the recovery copy, also omitted. Effect: a Worker who trusted the list literally would have shipped a served page reading "Kronika" four times and "FrameNest" once, and would have discovered the omitted pins only at the 11-minute full suite. Smallest correction: for every remaining identity cut, derive the rename inventory *and* its test pins by enumerating the product surface and then grepping tests for the retired spelling in an assertion context, and treat the count as provisional until the enumeration number matches the inventory number.

LEAD: The granted scope forced a partial user-visible rename, because the files carrying the remaining ~40 strings are exactly the files the grant forbade touching — the Cooperator will see "Kronika" in the side-panel wordmark and "Save to FrameNest" in the Save overlay. Evidence: `extension/shared/messages.js:624–690`, `extension/ui/save.html:5,12`, `extension/ui/save.js:7`, `extension/ui/picker.html:5`, `extension/ui/picker.js:27`, `extension/content/x_adapter.js:21,30,1765,1772`, `extension/ui/sidebar.js:66,70,486,672,785,826,838,1103`, `src/framenest/adapters/api/web/app.js` (8 sites). Effect: a user-visible acceptance session against a refreshed NUC would show a split brand and could be misread as a defect, or as the cut having failed. Cheapest useful check: before the Cooperator reloads, have him confirm the expected split explicitly — wordmark and titles say Kronika, Save overlay and status strings still say FrameNest — so the next cut's grant is scoped to what he can actually see rather than to a static list.
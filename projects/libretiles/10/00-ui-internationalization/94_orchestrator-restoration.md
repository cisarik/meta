Artifact class: **Orchestrator-authored evidence record**, not a Worker exchange and not authority.
Stage-1 Continuation Bootstrap restoration for logical whole `ui-internationalization` (Meta 10/00),
performed by the Orchestrator itself. Task authority comes only from a current authoritative prompt;
protocol meaning from the pinned AP; project truth from the canonical repository.

Filename: `9N_` prefix per the documented local deviation explained in `90_orchestrator-restoration.md`.
`90`, `91`, `92`, `93` are taken, so this is `94`. Worker-session ordinal `01` is USED (it built S1);
the next Worker session in this whole is `02`.

Orchestrator: fresh session, Claude Opus 5 Thinking, write access to the repository.
Date of measurement: 2026-09-02.
Active mutation: none. Active Worker: none. Nothing issued, nothing committed, nothing pushed.

---

# 1. THE BASELINE MOVED — the handout's expected HEAD is stale by one commit

`93_orchestrator-handout.md` section 1 expects `2917251aba19706e59aea5d50df8cbf353cea7ad`. Measured:

```text
git rev-parse HEAD                    61c9f09377011525105d747b88d603bff5d832e6   NOT 2917251
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   as expected
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   equal to the gitlink
git status -sb                        ## main...origin/main                      no divergence marker
git status --porcelain=v1             (EMPTY — not the ten untracked files)
git ls-remote origin refs/heads/main  61c9f09377011525105d747b88d603bff5d832e6   public readback equal
```

## 1.1 RF-12 recovery-candidate classification, performed before any mutation

```text
Classification unit type: commit-range
Classification unit identity: 2917251..61c9f09  (exactly one commit)
Observed difference: one commit adding five binary files under frontend/public/, plus the
  disappearance of the five untracked source JPEGs from the working tree
Classification accepted-continuation: applicable because the commit delivers exactly the flag assets
  that handout section 1 assigns to this whole ("They are YOURS to commit ... they exist for the flag
  dropdowns in section 6 R1")
Classification unrelated-owner-work: applicable because the author is the COOPERATOR himself
  (Michal Cisárik <michal@cisarik.info>, 2026-09-02 08:08:53 +0200), not any Orchestrator or Worker
Classification stale-clone: not-applicable because local HEAD equals the public ref exactly
Classification unpublished-candidate: not-applicable because nothing is unpushed
Classification unexplained-divergence: not-applicable because no material remainder exists — the
  commit is fully explained by its content, author, and the handout's own instruction
Primary recovery classification: unrelated-owner-work
Secondary recovery classifications: accepted-continuation
Primary precedence basis: unexplained-divergence > unrelated-owner-work > stale-clone >
  accepted-continuation > unpublished-candidate
Immediate recovery action: preserve the owner's work; adopt 61c9f09 as this whole's baseline; do not
  re-commit, revert, or normalize the assets
Publication status: published; public readback equal
Owner provenance: COOPERATOR
Location status: canonical checkout /home/agile/Projects/libretiles, branch main
Accepted authority: none required — no Orchestrator or Worker action produced it
Other-unit context: none
Unclassified material remainder: none
Secondary facts preserved: yes
Recovery gate: honored-explicit-classification
Baseline fallback: none
Mutation before classification: none
Destructive recovery operation: none
Returned to Orchestrator: no  (the Orchestrator classified it directly; no Worker was involved)
```

## 1.2 What he committed, verified byte-for-byte against the ledger

```text
61c9f09  feat(images): add new language icons for Czech, English, Hungarian, Polish, and Slovak
         5 files changed, parent 2917251, author Michal Cisárik, 2026-09-02 08:08:53 +0200
         frontend/public/cs.png  924 B    frontend/public/en.png 2572 B
         frontend/public/hu.png  242 B    frontend/public/pl.png  166 B
         frontend/public/sk.png 1326 B                    total 5230 B
```

Every byte size matches the Orchestrator-normalized assets recorded in `DEFECT_LEDGER.md`
("Flag assets normalized by the Orchestrator, 2026-09-01"): en 2572, sk 1326, cs 924, hu 242, pl 166,
total 5230. All five are PNG, all five are **48x32**, verified by reading the IHDR width/height from
each file. So he committed the **normalized** assets, not the raw JPEGs, and the `cz.jpeg -> cs.png`
language-code rename survived.

**The five source JPEGs never entered Git history** — `git log --all -- frontend/public/<f>.jpeg`
returns zero commits for each of `en.jpeg`, `sk.jpeg`, `cz.jpeg`, `hu.jpeg`, `pl.jpeg` — and they are
gone from the working tree. Nothing orphaned, nothing to clean up, no `.gitattributes`, no LFS.

**Consequence for the plan:** handout section 1's "Expected untracked ... ten files" and its
instruction "They are YOURS to commit" are both **discharged**. R1 may `<img src="/en.png">` etc.
immediately. Porcelain is empty, which is a *stronger* starting position than the handout describes.

---

# 2. All eight standing gates — re-measured by this Orchestrator at `61c9f09`

Execution route: `AGENTS.md` documents `poetry run ...`. Per `PROJECT_CONTEXT.md` section 4 that route
is not usable here because the Cursor AppImage environment intercepts `python*` through inherited
`APPIMAGE` / `ARGV0` / `APPDIR` / `PYTHONHOME`. Bounded deviation used exactly as the project rules
prescribe: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/`. Evidence class
`reproduced-dynamic`. No ambient `python`, `python3`, or `poetry run` was presented as a parallel route.

```text
mypy config game gamecore accounts catalog   Success: no issues found in 83 source files    exit 0
ruff check .                                 All checks passed!                             exit 0
manage.py check                              System check identified no issues (0 silenced.) exit 0
pytest                                       381 passed, 4 skipped in 215.97s               exit 0
npm run typecheck                            tsc --noEmit --incremental false               exit 0
npx vitest run                                28 passed | 1 skipped (29 files)
                                             352 passed | 3 skipped (355)                   exit 0
npm run lint                                 eslint                                         exit 0
npm run build                                exit 0, every route ƒ, Proxy registered,
                                             no middleware deprecation warning
```

Every number matches the handout capsule exactly: mypy 83, pytest 381/4, vitest 352/3. `pytest` was
invoked as plain `-m pytest`, so the `addopts = "-q"` trap did not suppress the summary, and the
summary is quoted verbatim above. mypy ran on the full documented scope, not a narrowed path set.

Two things done because the handout warns about them specifically:

1. **`npm run build` was safe to run.** `ss -tlnp | grep -E ':3000|:8000|:3100|:3200|:3411'` returned
   nothing — the Cooperator's dev server and Django were both stopped. No process was killed, and no
   broad-pattern kill such as `pkill -f next-server` was used at any point.
2. **`mypy --no-incremental` was run as a separate gate** and also returned
   `Success: no issues found in 83 source files`. `PROJECT_CONTEXT.md` section 4 asks whether mypy's
   incremental mode shares the `orch-04-F22` weakness that made `npm run build` report success over a
   stale typecheck cache. Answer, measured rather than assumed: **it does not, at this commit.** The
   cached and uncached runs agree. That question is now closed with evidence instead of being carried
   forward as an open caution.

`npx vitest run` and `npm run build` were each run **twice**, with identical results, because the first
run of each was inside a pipeline that discarded the exit status. Both exit codes are `0` from the
direct second invocation. "The build passed" and "the code type-checks" are stated as two separate
claims, per `orch-04-F22`.

---

# 3. Reconciliation of `93_orchestrator-handout.md` against measured truth

| Handout claim | Verdict |
|---|---|
| `main = 2917251`, ten untracked files in `frontend/public` | **STALE.** `main = 61c9f09`, porcelain EMPTY. Section 1.1 above classifies the difference. |
| `.ap` gitlink `9c5cc44`, submodule HEAD equal | confirmed |
| eight gates green (mypy 83, pytest 381/4, vitest 352/3, typecheck/lint/build 0) | confirmed, all re-measured at `61c9f09` |
| no active mutation, no active Worker, nothing unpushed | confirmed |
| R2 is DONE — `GET /api/game/variants/`, `VariantSummary`, `getVariants()`, `GameLanguagePanel` | confirmed. `backend/game/urls.py:28` routes `variants/` to `VariantListView`; `frontend/src/lib/types.ts:94-100` declares `VariantReadiness = "playable" \| "unavailable"` and `VariantSummary`; `api.ts:320-321` `getVariants`; `frontend/src/components/settings/GameLanguagePanel.tsx` (98 lines, with its own `GameLanguagePanel.test.ts`) consumes `readonly VariantSummary[]` and disables `readiness !== "playable"` rows. **Do not rebuild it.** |
| four variants installed: english, czech, polish, slovak; Hungarian absent | confirmed. `backend/assets/variants/` holds exactly those four `.json`. `dicts/` holds `czech.txt` 54 105 021 B and `polish.txt` 51 607 141 B with their `.LICENSE` files; no `hungarian.*` anywhere. |
| `SelectedVariantSlug` is now `string`, persist version 4 | confirmed. `useGameStore.ts:26` `export type SelectedVariantSlug = string;`, `:278` `version: 4`, with `version < 3` and `version < 4` migrate branches at `:286` and `:296`. |
| nonce CSP now costs ZERO additional static prerendering | confirmed. The `npm run build` route table at `61c9f09` shows **every** route as `ƒ`, including `/`, `/play`, `/settings`. |
| `settings/page.tsx` is 813 lines | confirmed exactly |
| `game/[id]/page.tsx` is 1822 lines | confirmed exactly |
| the i18n key pattern is proven; `Record<TextKey, string>` catches one-sided keys | confirmed structurally: `messages.sk.ts` declares `skText: Record<TextKey, string>` and `skFn: { [K in FnKey]: (typeof enFn)[K] }`, and a key-set diff of the two catalogs returns **zero** missing and **zero** extra keys. |
| R5 / `uii-01-F04` VERIFIED STILL OPEN — no LocaleProvider anywhere | confirmed with a **widened** pattern, not a single narrow grep. `LocaleProvider` → 0 matches. `createContext` → 0. `useContext` → 0. There is no React context of any kind in `frontend/src`. `layout.tsx:12-15` reads the cookie server-side for `<html lang>` (`:37`) and `generateMetadata` (`:21-28`) while the body renders from the client store. |
| `Locale` union still `["en","sk"]` | confirmed, `frontend/src/lib/i18n/locales.ts:1` |
| `proxy.ts` sets headers and nothing else | confirmed. 29 lines, one `buildSecurityHeaders` call, one matcher, no redirect, no rewrite, no nonce. |
| Django `USE_I18N = False`, `LANGUAGE_CODE = "en-us"`, HSTS without the two flags | confirmed at `settings.py:216`, `:218`, `:238`. `SECURE_HSTS_INCLUDE_SUBDOMAINS` and `SECURE_HSTS_PRELOAD` appear **nowhere** in the file. `LocaleMiddleware` appears nowhere. `AxesDrfLockoutFlagMiddleware` is immediately before `axes.middleware.AxesMiddleware`, which is last. |
| `audit-01-F06` swallow-to-200 open in both catalog proxies | confirmed. `api/models/route.ts:20` and `:26`, `api/prompts/route.ts:12` and `:18` all return `NextResponse.json([], { status: 200 })` on both the `!res.ok` and `catch` branches. The `revalidate: 60` / `no-store` asymmetry the ledger notes is also still present. |
| `uii-01-F01` 429 parsed out of an English body | confirmed. `api.ts:125-135` `parseRetryAfterSeconds` matches `/(\d+)\s+seconds/i` against the body; no `Retry-After` header read exists anywhere in the file. |
| `uii-01-F03` two hardcoded `"en-US"` date sites | confirmed, and they are the **only** two. `GameHistoryPanel.tsx:73`, `ProfileModal.tsx:22`. `toLocaleString`, `toLocaleDateString`, `toLocaleTimeString` return nothing. |
| `api.ts` `humanMessageForStatus` is a `switch` whose 401 branches on `requestCarriedToken` | confirmed. `:148-152` signature, `:159` the branch. That branch **is** AC-SEC-2 and survives at `61c9f09`. Locale arrives at `:270` from `useGameStore.getState().uiLocale ?? DEFAULT_LOCALE`. |
| R6 is genuine outstanding work — the player still picks model AND prompt preset | confirmed. `settings/page.tsx:672` `"No rival selected"`, `:693` per-row selection, `:551` `api.updateMe(..., preferred_ai_model_id)`; `play/page.tsx:34,69` `"Choose AI"`; `ScorePanel.tsx:425` `"Prompt presets"`; `PromptCatalogModal.tsx` mounted from `game/[id]/page.tsx:1783`. |
| locks A–D intact | confirmed. Nine `*_PROVIDER` constants by name; `MOVE_PROMPT_VERSION = "pfr-s2-core-1"`; `DEFAULT_MAX_ELAPSED_MS = 2000` and `DEFAULT_RANKED_MAX_ELAPSED_MS = 750`. |
| `11/01` is still open and owns the wire format | confirmed. `_legacy_wire_board_and_blanks` is still at `services.py:327`, called from `:442`. F2c has not landed. `11/01` is **idle**, not mid-slice: porcelain empty, nothing unpushed, `main` published. |

**No gate the handout calls green came back red.** The only material divergence is the baseline commit,
and it is fully explained.

---

# 4. Precision corrections to the handout and the ledger — measured, none material to the plan

Recorded rather than smoothed over, in the project's own style.

```text
4.1  "55 keys across six areas" undercounts by two. The handout's own histogram — draw 13, landing 11,
     error 11, settings 10, auth 10, meta 2 — sums to 57, and 57 is right. Measured: enText has
     exactly 55 keys and enFn has exactly 2, so the localized total is 57 and "55" is the enText half.
     Both numbers are real; the sentence conflates them.

4.2  The pinned MOVE CORE SHA-256 lives in `frontend/src/lib/prompts.test.ts:23`, NOT in `prompts.ts`.
     Lock B's hash is enforced by a test, exactly as PROJECT_CONTEXT.md section 5 says of lock C since
     era 11. Handout section 8 implies the hash sits in the prompt file. The lock is intact either way;
     anyone verifying it must look in the test.

4.3  `grep -cE "^export const [A-Z_]+_PROVIDER"` returns **10**, not 9, because it also matches
     `EXACT_PROVIDER_METADATA` at line 51. Enumerating by name returns exactly nine providers. A
     third instance of "a count is not a conclusion", found by this Orchestrator against itself.

4.4  The a11y inventory in `uii-01-F02` is now understated. Re-measured with a widened pattern over all
     of `frontend/src`:
         aria-hidden 5   aria-disabled 5   aria-pressed 4   aria-live 2   aria-current 1   = 17
         title= 10   placeholder= 6   onKeyDown 5
         ZERO: aria-label, aria-labelledby, aria-describedby, role=, alt=, tabIndex, sr-only,
               screen-reader, htmlFor, autoFocus, <dialog, aria-modal
     `aria-disabled` (5) is NEW since the ledger's era-10 histogram of 10 occurrences; era 11's
     GameLanguagePanel introduced it. The finding's substance is unchanged and its exact patterns that
     matched nothing are named above. Two consequences worth carrying: `alt=` is zero and R1 adds five
     flag images, so R1 is the first change in this product's history that *needs* alt text; and
     `htmlFor` is zero, so no input in the product is programmatically associated with its label.
```

---

# 5. The remaining string scope — re-measured per file, and the handout's table is INCOMPLETE in a way that matters

The handout says its grep "only counts quoted capitalized literals — JSX text nodes between tags are
invisible to it" and that the true figure is "meaningfully higher". Confirmed, and here is the concrete
list it does not contain.

Method: quoted literals opening with a capital letter, plus single-line JSX text nodes, over every
non-test `.ts`/`.tsx` under `frontend/src`. My JSX-text regex only matches single-line nodes, so **my
JSX column is a lower bound** and the era-10 subagent's ~125–130 remains the better estimate for that
class. Stated so nobody treats 31 as the answer.

## 5.1 The nine files the handout lists — all confirmed within regex noise

```text
file                                      handout   measured (quoted)
app/game/[id]/page.tsx                        70          70
app/settings/page.tsx                         41          45
lib/api.ts                                    25          26
components/game/GameHistoryPanel.tsx          18          21
components/game/ScorePanel.tsx                15          14
components/game/ProfileModal.tsx              15          15
app/play/page.tsx                             11          11
app/waiting/[id]/page.tsx                      6           6
components/game/PromptPreviewModal.tsx         3           3
```

## 5.2 EIGHT MORE UI FILES CARRY VISIBLE COPY, and one of them holds the primary game buttons

```text
components/game/GameControls.tsx      "Play"  "Pass"  "Exchange"  "Cancel"  "Confirm exchange"
                                      <- the five primary in-game buttons. Absent from the table.
components/game/AIThinkingOverlay.tsx "AI Thinking"  "Searching for moves..."  "Best" / "BEST"
                                      "Filtering weak or invalid lines before showing a serious move..."
components/game/ChatPanel.tsx         "Game Chat"  "Say something"  "Send"  "No messages yet."
                                      "Chat unavailable"  "You"
components/board/Board.tsx            "Pinch to zoom"  "Drag to pan"  "Hide"  "Reset"  "PTS"
components/game/GameHistoryModal.tsx  "Games"  "Close"
                                      "Review past boards, switch between AI and human games, ..."
components/game/BlankPicker.tsx       "Choose a letter for blank tile"
components/tiles/TileRack.tsx         "No tiles on rack"
components/game/TurnStatusNotice.tsx  none — pure presentation
components/game/LuxeHoverText.tsx     none — pure presentation
```

This does **not** contradict the handout; it is the detail the handout said was missing. It does confirm
that the R3 area list (`play`, `queue`, `waiting`, `game`, `controls`, `board`, `overlay`, `chat`,
`history`, `profile`, `prompt`, `a11y`) is correctly scoped — each of those areas has a real home.

Three of these deserve naming now because the glossary already decided their wording:

```text
BlankPicker "Choose a letter for blank tile"  ->  "Vyber písmeno pre žolíka"
                                                  reads correctly ONLY because písmeno and žolík are
                                                  distinct words; this is the sentence that proves the
                                                  tile -> písmeno decision was right
Board "PTS"                                    ->  "b."   the glossary's points abbreviation, in the
                                                  tightest container in the product
GameControls "Play/Pass/Exchange"              ->  "Zahrať / Vynechať / Vymeniť"
```

## 5.3 A NEW over-count the handout does not warn about, and it is the most dangerous one

```text
frontend/src/lib/constants.ts   61 quoted capitalized literals
```

All 61 are the premium-square board layout codes **`TW`, `DW`, `TL`, `DL`** — the physical Scrabble
board. They are game data, not copy. A translator subagent handed this file would silently corrupt the
board. Add it to the handout's "classify before you translate" list alongside `provider-registry.ts`
(LOCK A), `prompts.ts` (LOCK B), `security-headers.ts` (CSP directives), the two AI routes, and
`provider-logging.ts` / `provider-capability.ts` / `types.ts`.

Also note `messages.en.ts` 52 and `messages.sk.ts` 46 appear in a raw sweep. Those are the dictionary
itself — already-done work, not remaining work. Any future inventory must exclude
`frontend/src/lib/i18n/` or it will double-count its own output.

---

# 6. Residuals routed here — read at `61c9f09`, none acted on

```text
R5  / uii-01-F04   OPEN, verified above with a widened pattern. Prerequisite for R3, not a bug fix.
R8  / uii-01-F01   OPEN, verified: no Retry-After read exists in api.ts.
R9  / orch-02-D11  OPEN, verified: neither SECURE_HSTS_INCLUDE_SUBDOMAINS nor SECURE_HSTS_PRELOAD is
                   set anywhere in backend/config/settings.py. Add the first, never the second.
R10 / orch-01-F18  OPEN, verified: proxy.ts is 29 lines and contains no nonce. Its Cooperator sign-off
                   from the security era stays intact and must not be lost at closure.
R11 / audit-01-F06 OPEN, verified in both proxy routes, both branches.
R12 / uii-01-F02   OPEN, re-measured and slightly restated in section 4.4.
R12 / uii-01-F03   OPEN, verified: exactly two hardcoded "en-US" sites.
R2                 DONE by era 11 slice A1. Deleted from the plan. Extend GameLanguagePanel.
R1                 UNBLOCKED EARLY: the flag assets are committed and 48x32. See section 1.2.
```

Not touched and must not be: `audit-04-F01` / `orch-05-D14`, routed to the deployment whole.

---

# 7. The ONE open Cooperator decision — put to him, unmade

Which interface locales does the product ship in. The `Locale` union is still `["en","sk"]` while three
of the four Visegrád languages are playable *game* variants. Interface locale and game variant are two
independent axes. Options A (`en+sk`), B (`en+sk+cs+pl`), C (all five including `hu`) were put to him
in one message with recommendation **B** and the honest cost — roughly triple the translation volume,
near-zero architecture cost, because each locale is one `messages.<locale>.ts` typed
`Record<TextKey, string>` and `tsc` names every missing key.

Nothing is issued until he answers. Per RF-01 this is scope and cost and therefore his.

---

# 8. Open at the end of Stage 1

```text
1  the section-7 locale decision is with the Cooperator; no Worker prompt exists
2  Polish and Hungarian terminology remain UNVERIFIED CANDIDATES (płytka? stojak? blank? /
   betű? tartó? joker?) and are only needed if he selects B or C
3  the deployment-whole handout and the read-only Research Worker prompt remain a carried-forward
   obligation (PROJECT_CONTEXT.md sections 11.2 and 11.3)
4  the last used Cooperator test batch prefix is B16; the next is B17
5  Worker session 02 is the next available ordinal in this whole
```

No mutation has been performed. No Worker prompt has been issued. The repository is untouched at
`61c9f09` with empty porcelain.

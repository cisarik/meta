### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 20, Worker exchange ordinal: 02
```

**1. Status:** PASS

**2. Phase-qualified result:** Implementation — complete. MEC-UIL-W2b landed as one revertible commit: the suite restored over twelve locales without inventing expected strings for eight unreviewed languages, the unconditional-flag defect repaired, two under-covering test files extended, the ASCII-foldability invariant added, two documents corrected.

**3. Start and end commit:** start `779aa55b8a03c6de5c7c2ece453e4ca8418b5627` plus the declared `unpublished-candidate` (two modified files) → end `96fbd4833c5cf0ceeffb9d3c1ecfe81d70cc5b68`.

**4. Changed files (eight, exactly the allowlist):**

| Path | Purpose |
|---|---|
| `frontend/src/lib/i18n/locales.ts` | earlier Worker's wiring, `LOCALES` 4→12 — staged unchanged |
| `frontend/src/lib/i18n/translate.ts` | earlier Worker's wiring, eight `TEXT`/`FN` rows — staged unchanged |
| `frontend/src/lib/i18n/i18n.test.ts` | `REVIEWED_LOCALES`, 13 narrowings, 6 property/wording splits, AC-EXHAUST loop, two new blocks |
| `frontend/src/app/settings/page.tsx` | eight `localeLabelKey` entries + the flag defect fix |
| `frontend/src/lib/api.test.ts` | AC-SEC's two 401 cases now iterate `LOCALES` |
| `frontend/src/components/settings/PremiumPicker.test.ts` | twelve-row fixture, four flags, `AC-PICKER-FLAGLESS` |
| `frontend/src/lib/i18n/GLOSSARY.md` | `picker.flagAlt` four→twelve, new "Reviewed locales in tests" subsection, flag-availability note |
| `AGENTS.md` | "Not done yet" first bullet rewritten to what is now true, with the honest residual caveat |

**5. Repository gate:** `HEAD` `779aa55…`, `HEAD:.ap` = `.ap` `HEAD` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (detached, correct), `## main...origin/main`, `git status --porcelain=v1` exactly the two declared modified files and nothing else, `ls-remote origin refs/heads/main` = `779aa55…`, no listener on 3000 or 8000. Handoff verification `npm run typecheck | grep -cE '^src/.*error TS'` printed **28** — 1 in `settings/page.tsx` (TS2740 on `localeLabelKey`), 27 in `i18n.test.ts`. `.ap` never attached, updated or committed.

**6. Tests and validation — all eight gates, every one post-dating my last edit:**

| Gate | Result |
|---|---|
| `npm run typecheck` | **0 errors**, down from 28 |
| `npx vitest run` | **474 passed / 3 skipped / 477 total**, 0 failed — baseline was 467 / 3 / 470, so the total ROSE by 7 |
| `npm run lint` | clean, exit 0 |
| `npm run build` | **the build passed** (`✓ Compiled successfully in 2.9s`) **and the code type-checks** (`Finished TypeScript in 3.3s`, plus the standalone gate above) — **eleven dynamic routes, zero static** |
| backend `mypy config game gamecore accounts catalog` | `Success: no issues found in 85 source files` |
| backend `ruff check .` | `All checks passed!` |
| backend `manage.py check` | `System check identified no issues (0 silenced).` |
| backend `pytest` | `745 passed, 4 skipped in 271.45s` |
| backend `manage.py validate_lexicons` | `validate_lexicons: 13 asset(s) audited, 0 failed` |

The vitest total rose by exactly the five new `i18n.test.ts` cases (four in `AC-STRUCT-12`, one in `AC-FOLD-ASCII-12`) plus the two new `PremiumPicker.test.ts` cases. No assertion was deleted or weakened: `expect(` statements went 335→352 in `i18n.test.ts`, 43→44 in `api.test.ts`, 57→64 in `PremiumPicker.test.ts`. The backend five were expected to be uninformative — the diff is frontend-only plus root `AGENTS.md` — and **they were uninformative**; they are reported because this is the commit that changes what a user can reach.

**7. Commit and push:** one non-force commit `96fbd48` on `main`, subject `feat(i18n) wire eight interface locales`, body carrying all ten required paragraphs. Staged by naming the eight paths individually — no `git add .`, `-A`, or a directory. Pre-push gate: `HEAD~1` = `779aa55b8a03c6de5c7c2ece453e4ca8418b5627` and `ls-remote origin refs/heads/main` still `779aa55b8a03c6de5c7c2ece453e4ca8418b5627`. One `git push origin main`, non-force: `779aa55..96fbd48  main -> main`. **Readback:** local `HEAD` `96fbd4833c5cf0ceeffb9d3c1ecfe81d70cc5b68`, remote `refs/heads/main` `96fbd4833c5cf0ceeffb9d3c1ecfe81d70cc5b68` — equal. Tree clean, `## main...origin/main`, `.ap` gitlink unchanged.

**8. Deviations, risks, missing evidence:** no deviation from the allowlist, git authority, network authority (only the two authorized remote reads plus one push) or dependency authority (no install, no `package.json`, no lockfile, no new file under `frontend/public/`). No secret was read or printed. Risk that remains: the eight catalogs' *wordings* are still unreviewed by construction — this slice deliberately does not assert them, and `AGENTS.md` and `GLOSSARY.md` now say so. Rollback is one `git revert`, which returns `LOCALES` to four and leaves the eight catalogs in the tree untouched.

---

### Evidence loop one — proof no green twelve-locale loop was narrowed

Measured with the prescribed `awk` scan run **before my first edit** to `i18n.test.ts` and **again after my last**.

**Before:** 24 `of LOCALES` iterations across 20 distinct describes · 0 `of REVIEWED_LOCALES` · 4 `(typeof LOCALES)[number]` sites. Both baseline counts reproduce section 3.2 exactly.

**After:** 22 `of LOCALES` · 13 `of REVIEWED_LOCALES` · 1 `(typeof LOCALES)[number]`.

| describe | before | after | why it moved (or did not) |
|---|---|---|---|
| AC-RACKTILE-4 | TWELVE 1 | REVIEWED 1 | asserts an exact string only the reviewed four have been reviewed for |
| AC-RACKBLANK-4 | TWELVE 1 | REVIEWED 1 + TWELVE 1 | exact blank name → four; **split**: "the blank name never equals a lettered-tile name" is a property → twelve |
| AC-A11Y-COPY-4 | TWELVE 1 | REVIEWED 1 | exact string, reviewed four only |
| AC-QUEUE-VARIANT | TWELVE 2 | REVIEWED 1 + TWELVE 1 | the `ownName` wording loop → four; the "Czech label never leaks the English exonym" loop was already separate and stays at twelve |
| AC-CATALOG-COPY-4 | TWELVE 1 | REVIEWED 1 + TWELVE 1 | exact string → four; **split**: "catalogUnavailable ≠ catalogEmpty" is a property → twelve |
| AC-HEADER-4 | TWELVE 1 | REVIEWED 1 | exact string, reviewed four only |
| AC-OVERLAY-4 | TWELVE 1 | REVIEWED 1 | exact string, reviewed four only |
| AC-PROFILE-4 | TWELVE 1 | REVIEWED 1 | exact string, reviewed four only |
| AC-PROFILE-DUP | TWELVE 1 | REVIEWED 1 + TWELVE 1 | **§3.3 BLOCK 1 split**: `field.current === ph.current` property → twelve; `profile.email === "Email"` wording → four |
| AC-HISTORY-4 | TWELVE 1 | REVIEWED 1 | exact string, reviewed four only |
| AC-PAGING-4 | TWELVE 1 | REVIEWED 1 + TWELVE 1 | exact strings → four; **split**: "no non-English `showing` copy carries `games`" is a property → eleven non-English |
| AC-SETTINGS-4 | TWELVE 1 | REVIEWED 1 | exact string, reviewed four only |
| AC-TOGGLE-4 | TWELVE 2 | REVIEWED 1 + TWELVE 1 | **§3.3 BLOCK 2**: wording loop → four; the four-distinct-descriptions loop was already separate and stays at twelve |
| AC-SYNC | TWELVE 3 | TWELVE 3 | green over twelve, untouched |
| AC-LEX-4 | TWELVE 1 | TWELVE 1 | green over twelve, untouched |
| AC-LEX-UNK | TWELVE 1 | TWELVE 1 | green over twelve, untouched |
| AC-BADGE-CASE | TWELVE 1 | TWELVE 1 | green over twelve, untouched |
| AC-ROUTEFAIL-4 | TWELVE 1 | TWELVE 1 | green over twelve, untouched — **the `-4` in its name is a trap; every assertion in it is structural** |
| AC-STATS-4 | TWELVE 1 | TWELVE 1 | green over twelve, untouched |
| AC-KEYTYPED | TWELVE 1 | TWELVE 1 | green over twelve, untouched |
| AC-EXHAUST | — | TWELVE 1 | new: hand-listed sk/cs/pl comparisons replaced by a loop over all twelve |
| AC-STRUCT-12 | — | TWELVE 3 | new block |
| AC-FOLD-ASCII-12 | — | TWELVE 3 | new block |

**Reconciliation, by construction:**
- Describes that gained a REVIEWED loop = **13** = exactly the 13 red cases. Every one has a WHY clause above; none was moved without one.
- Surviving baseline twelve-locale sites = 24 − 13 = **11** (AC-SYNC 3, AC-LEX-4 1, AC-LEX-UNK 1, AC-BADGE-CASE 1, AC-ROUTEFAIL-4 1, AC-STATS-4 1, AC-KEYTYPED 1, AC-QUEUE-VARIANT 2nd loop 1, AC-TOGGLE-4 2nd loop 1).
- New twelve-locale sites = **11** (AC-EXHAUST 1, four extracted property loops, AC-STRUCT-12 3, AC-FOLD-ASCII-12 3).
- 11 + 11 = **22** = the measured after-count. Closes.
- Describes appearing in BOTH columns afterwards = **6**, not the two section 8.2 assumed. So describes that moved *wholly* = 13 − 6 = **7**, and section 8.2's formula `13 − 2 = 11` does not reconcile; I am stating that rather than adjusting a number. Details under MEASURED below.

**The four `(typeof LOCALES)[number]` sites, decided separately:** the three `Record` key types (`ownName` inner, `HEADER_EXPECTED` inner, `OVERLAY_EXPECTED` inner) narrowed to `(typeof REVIEWED_LOCALES)[number]`. The one **function parameter** — `queueLabel(locale: (typeof LOCALES)[number], …)` — **deliberately did not narrow**: a helper that accepts a locale should keep accepting all twelve, and the surviving property loop in the same block still calls it with all twelve, so narrowing it would have been both wrong and a compile error.

---

### Evidence loop two — visited cells, threshold, exemption set

Every count below is asserted by the committed test itself (`expect(cells).toBe(N)`), so a green run *is* the runtime confirming the number; a loop that quietly visited four locales fails the assertion rather than passing silently.

| loop | visited | arithmetic |
|---|---|---|
| `AC-STRUCT-12` non-empty text cells | **3648** | 304 text keys (AC-EXHAUST's pinned count) × 12 locales (`expect(LOCALES.length).toBe(12)`) |
| `AC-STRUCT-12` interpolation-parity fn cells | **240** | 20 fn keys × 12 locales |
| `AC-STRUCT-12` stray-placeholder cells | **3888** | (304 + 20) × 12 |
| `AC-STRUCT-12` English-leakage cells | **1520** | 190 eligible keys × 8 unreviewed locales |
| `AC-FOLD-ASCII-12` `settings.uiLanguage.*` | **144** | 12 labels × 12 locales |
| `AC-FOLD-ASCII-12` `settings.gameVariant.*` | **144** | 12 slugs × 12 locales |

**Threshold: an English value of ≥ 11 characters must not be byte-identical in the eight unreviewed locales.** Cited from section 2.1's `len` column, not tuned: excluding the three named exemptions, the longest ever-byte-identical English value is **ten** characters (`Nederlands` / `Slovenčina` as endonyms), `settings.gameVariant.afrikaans` is nine, and everything else in the table is a label, an initialism or a naturalized loanword of at most nine. Eleven is therefore the smallest threshold that accuses none of them while still catching a real eleven-plus-character leak. It ran with **zero failures on the first execution**, which is the check that the derivation was right rather than lucky.

**Exemption set, in full:**
- prefix family `settings.uiLanguage.` — the endonym rule requires byte-identity. Named as a family, not by length, so a future endonym of eleven-plus characters stays exempt without an edit (all twelve current endonyms are ≤ 10, so the exemption is currently redundant by length and deliberately kept).
- `landing.brand` — a product name, exactly 11 characters, so the exemption is load-bearing at this threshold.
- `landing.titleLine1` — a product tagline, 20 characters, deliberately shared by nine catalogs.
- `game.toast.chatOffline` — 15 characters of correct Dutch; the `nl` catalog carries a comment saying so.

The exemption set does **not** depend on the ten missing byte-identity comments from section 6; it is derived from the `len` column alone.

Also asserted: `FN_PARITY.length === Object.keys(enFn).length` and every `FnKey` present in the fixture — the reused 20-key fixture covers all 20 keys with **zero gaps**, confirmed in-test rather than by eye. Sentinels `4242 / 9317 / 7185 / Qxzvv / Wkjpp` carry the reasoning in a comment; `game.toast.invalidWordHeading`'s empty `must` list carries the comment explaining that `count` selects a grammatical form and need not appear. Stray-placeholder pattern: `/\{\{|\{[A-Za-z_][A-Za-z0-9_]*\}/`. The block imports no `messages.*.ts` and contains no `console.log`, no `writeFileSync`, no `/tmp` path and no `node:fs` import.

---

### The flag defect

`frontend/public/` actually contains: `en.png`, `sk.png`, `cs.png`, `pl.png`, plus `hu.png` — which is **not** a locale and is explicitly asserted to be rejected by `isLocale` in this very suite — and `drevo.jpeg`, a board texture. **Four locale flags, twelve locales.**

`InterfaceLanguagePanel` built its options with an unconditional ``flagSrc: `/${value}.png` ``. With `LOCALES` at twelve that requests **eight images that do not exist** — `/de.png`, `/pt.png`, `/is.png`, `/it.png`, `/nl.png`, `/da.png`, `/sv.png`, `/af.png` — one broken-image glyph or 404 per row, in the one surface whose whole job is to be legible to a user who cannot read the current interface.

**No gate in this repository goes red for it.** It is a template string: it always has a value, so TypeScript, ESLint, vitest and the Next.js build are all silent. It surfaces only as a runtime 404 in a browser.

The shape I used is the one already in the tree, `GameLanguagePanel.tsx`: a `LOCALE_FLAG_SRC` lookup of the flags that exist plus the conditional spread `...(flagSrc ? { flagSrc } : {})`, with `PremiumPicker`'s `flagSrc` left optional so both the closed trigger and the list row render nothing when it is absent. No PNG added, no placeholder flag invented, `flagSrc` not made required. Eight flagless rows are the correct outcome: the label is an endonym, which is what the rule says a user scans for. `PremiumPicker.test.ts`'s new `AC-PICKER-FLAGLESS` now pins that behaviour — a flagless row renders its label and no `<img>`, a flagged row renders `src="/xx.png"`, and the trigger image appears only when the selected row has a flag.

---

### The GLOSSARY subsection added, quoted

```markdown
## Reviewed locales in tests

Tests pin exact expected strings for the four locales that have been through
review — `REVIEWED_LOCALES` = `en sk cs pl` in `i18n.test.ts`. The other eight
catalogs are machine-authored and have had no second opinion, so copying their
own values into expectations would assert only that a string equals itself.
They are covered STRUCTURALLY instead, over all of `LOCALES`: shared key set,
non-empty resolution, no long English value leaking byte-identically, every
interpolation parameter surviving, no stray placeholder, and ASCII-foldable
picker labels. Where an assertion states a PROPERTY rather than a wording it
keeps all twelve even inside an otherwise narrowed block. A trailing `-4` in a
test name now means "the four reviewed locales", not the shipped total.
```

---

### Resolved Execution Issues / Near-Misses

1. **Resolved.** The leakage-cell count was an estimate at first (`264`); the gate returned `190`, so the pin became `190` eligible keys × 8 = `1520`. I corrected the *count*, not the threshold or the exemption set — neither was touched to make the test green.
2. **Near-miss avoided.** `AC-ROUTEFAIL-4` ends in `-4`, sits among the 20 `of LOCALES` describes, and is **not** one of the 13 red cases: every assertion in it is structural and already passes for twelve. Narrowing by name pattern would have silently destroyed twelve-locale coverage. `AC-LEX-4` is the same trap.
3. **Near-miss avoided.** Narrowing `queueLabel`'s parameter type alongside the three `Record` key types. It is not a loop; see evidence loop one.
4. **Near-miss avoided.** Extending `PremiumPicker`'s fixture to twelve necessarily invalidates two *expected values* (`""` now yields twelve, `"c"` now also reaches `Deutsch`). Both were recomputed for the larger fixture; no assertion was deleted, and the assertion count in that file rose 57→64.
5. **Resolved by reporting rather than duplicating.** Section 5.1 told me to cross-reference an existing twelve-locale enumeration-fragment check in `i18n.test.ts`. It does not exist (see MEASURED 3). I wrote no third copy; `api.test.ts` now owns that property over twelve.

### Pre-Existing Failure Classification

All 41 failures I inherited — 13 red vitest cases and 28 type errors (27 in `i18n.test.ts`, 1 in `settings/page.tsx`) — are attributable **entirely** to the declared `unpublished-candidate` wiring, not to any defect at `779aa55`. All are now green. No failure independent of this slice exists: at the end of the slice all eight gates are clean. The 3 skipped vitest cases and 1 skipped vitest file match the stated baseline; the 4 skipped pytest cases are pre-existing by construction, since the backend diff is empty. Two pre-existing non-failures were left alone as instructed and confirmed still present: GLOSSARY's missing `czech` and `polish` `settings.gameVariant.*` rows, and the ten missing byte-identity comments from section 6.

---

### Orchestration critique

**MEASURED**

1. **Section 3.3's count of two is six.** Six red blocks contain an assertion that is a property rather than a wording. Four needed a genuine extraction — `AC-PROFILE-DUP` (the named BLOCK 1), `AC-RACKBLANK-4`, `AC-CATALOG-COPY-4`, `AC-PAGING-4`. Two already held their property in a *separate* loop and needed only their wording loop narrowed: `AC-TOGGLE-4` (the named BLOCK 2) and `AC-QUEUE-VARIANT`. So BLOCK 2 did not actually require splitting, and there were four more blocks than the prompt's corrected count. The general rule at the end of section 3.3 is what found them, and it discriminated correctly in every case: all six property assertions were green over twelve on first execution, so the rule produced no false positives.
2. **Section 8.2's reconciliation formula does not close.** It predicts `(describes that moved) = 13 red − 2 split = 11`. Measured: 13 describes gained a REVIEWED loop (= exactly the 13 red cases), 6 appear in both columns, so 7 moved wholly. The formula's premise is finding 1's wrong split count, not an error in the 13.
3. **Section 5.1's premise is false.** `i18n.test.ts` does **not** have an enumeration-fragment check over `LOCALES`. Its `AC-SEC message catalogs` block iterates `Object.values(loginByLocale)` — a four-entry object literal built from `enText`/`skText`/`csText`/`plText` — so it never sees twelve and the fragment vocabulary was *not* known-adequate for the eight new languages from that source. After this slice the twelve-locale fragment property lives in `api.test.ts`, over *rendered API messages*, which is the stronger surface. The two therefore do not overlap in the way the prompt assumed, and I wrote no third copy.
4. **Section 2.1's prose contradicts its own `len` column.** It says "everything except three keys is at most eleven characters" and then names `landing.brand` — whose `len` is 11 — as one of the three long ones. Excluding the three exemptions the true maximum is **ten**. The table is right; the sentence should read "at most ten". This matters because it is exactly what fixes the threshold at 11 rather than 12, and at 12 `landing.brand`'s exemption would be dead code.
5. **Section 5.2's "existing fold-based search assertions must keep passing unchanged" cannot hold literally.** Growing the fixture from four rows to twelve necessarily changes `filterPickerOptions(ENDONYMS, "")` from four values to twelve and `"c"` from `["sk","cs"]` to `["sk","cs","de"]`. I read it as "no assertion is deleted or weakened" and recomputed the two cardinality-dependent expectations, with a comment naming Deutsch as the point of covering twelve label shapes.
6. **Everything else in sections 1, 2, 3.2, 3.4, 4, 8 checks out exactly.** The 28-error split (1 + 27); 24 `of LOCALES` across 20 describes; 4 `(typeof LOCALES)[number]` of which three are `Record` keys and one a function parameter; 304 text / 20 fn / 12 locales; the interpolation fixture covering all 20 `Object.keys(enFn)` with zero gaps; 0 empty cells of 3648; 0 parity failures of 240; 0 stray placeholders; `overlay.bestBadge` uppercase in twelve; four distinct toggle descriptions in twelve; `profile.field.current === profile.ph.current` in twelve; `profile.email` shared by exactly five (`en sk cs pl it`) with the other seven rendering `E-Mail` / `E-mail` / `Netfang` / `E-post` / `E-pos`; the four flags plus non-locale `hu.png`; the twelve variant slugs; eleven dynamic routes and zero static; `validate_lexicons` 13 audited / 0 failed. `AC-EXHAUST`'s `it(...)` name did say "en/sk/cs/pl" and now names no locale count.
7. **One number worth recording for the next slice:** the vitest baseline on the *wired* tree was 13 failed / 454 passed / 3 skipped / 470 total, consistent with the stated 467 + 3 = 470 at `779aa55`. Final is 474 / 3 / 477.

**LEAD**

1. `i18n.test.ts`'s own `AC-SEC message catalogs` block still checks four catalogs by direct import rather than through `t`. Not red, not in the instructed set, and now redundant with `api.test.ts`'s twelve-locale coverage — but a one-loop change if you want the catalog-level check to match the rendered-level one.
2. A further class of four-locale under-coverage exists in `i18n.test.ts` that neither went red nor was named: `AC-DATE-LOCALE`, `AC-JOINED-LOCALE`, `AC-JOINED-INVALID`, `AC-ENDREASON-4`, `AC-PLAY-4`, `AC-QUEUE-ROOM-4`, `AC-HEADING-4`, `AC-PICKER-COPY` and `AC-TILES-4` all pin `en`/`sk`/`cs`/`pl` by explicit per-locale literal rather than by a locale loop, so the `awk` scan cannot see them. Their *properties* — e.g. "`formatUpdatedAt` never returns an English month in a non-English locale" — could extend to twelve in a later slice. Left untouched here.
3. `hu.png` in `frontend/public/` corresponds to no locale and no variant, and `hu` is explicitly asserted to be *rejected* by `isLocale`. It is dead weight and a mild foot-gun for exactly the defect fixed in section 4. Removing it needs file-deletion authority this slice did not have.
4. The four-flag asymmetry is now two parallel tables — `LOCALE_FLAG_SRC` in `settings/page.tsx` and `VARIANT_FLAG_SRC` in `GameLanguagePanel.tsx`. If flags for the other eight are ever added, both must grow.
5. Untouched as instructed, confirmed still true: GLOSSARY's missing `czech` and `polish` `settings.gameVariant.*` rows; the ten missing byte-identity comments (de `board.reset`; pt `board.pts`; it `auth.eyebrow`, `auth.field.password`, `nav.account`, `profile.email`; nl `auth.eyebrow`, `nav.account`, `history.col.score`, `board.zoomNoun`); the three `messages.en.ts` shape problems; `README.md`, `libretiles_PRD.md` and `docs/` locale numbers.

---

**Report justification:** `new-mutation`

**Logical-whole closure:** not-closed

**Authority expiry:** my authority ended at this report. I hold no standing authority to continue: I have not grown the variant-naming axis, touched any catalog, corrected `README.md` or the PRD, or archived this prompt or this report into Meta.

**Smallest next step:** grow the variant-naming axis — extend `INSTALLED_VARIANTS` and `ownName` in `AC-QUEUE-VARIANT` from four slugs to twelve, which is the one axis section 9 explicitly deferred and the natural successor now that the locale axis is settled.

**Context pressure:** moderate — comfortable headroom remained throughout; no compaction occurred and no reading was abbreviated.

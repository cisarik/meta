> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `c9078f2`, pushed, readback equal, porcelain clean. **ACCEPTED.**
> ✔ **THE DEFECT IS VERIFIED REPAIRED BY ME, independently of the report:** the table now has 16 entries,
> `Þýska → thyska`, `Sænska → saenska`, and the eth/d-stroke trap measures `ðđÐĐ → dddd`.
> ⭐ **M1 IS A REAL PROMPT DEFECT AND IT IS MINE:** I asked for "MORE passing tests than the 467/3
> baseline" while §4.2 forbade adding an `it` block — and vitest counts `it` blocks. ✔ Measured: 467/3
> before and after, while the assertions in that one block went **13 → 31**. The Worker named the
> contradiction, stated the assumption it proceeded on, and continued. That is exactly right.
> ⭐ **AND ITS LEAD 1 IS NOW MEASURED BY ME AND IT HAS A FINDING** — see `00_notes.md` §51.2. Folding
> `æ → ae` gives Icelandic a THIRD folded substring collision (`enska ⊂ saenska`), so typing `enska` in
> the Icelandic picker now matches four rows instead of three. **That is a strict improvement, not a
> regression:** before the fix `Sænska` folded to `sænska` and was reachable by NO ASCII query at all.
> My rulings on all nine findings are in `./00_notes.md` §51. The report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 18, Worker exchange ordinal: 01
```

**Status:** PASS
**Phase-qualified result:** Implementation complete for MEC-UIL-FOLD — the live fold defect is repaired, committed and published. Evidence posture non-independent (self-reported, E1).
**Start commit:** `0a4fcc26fa8c7bca5d03c3b1ca55425d0c44bbcd` → **End commit:** `c9078f2aa2b3a34c5ac51931b063f1330d49704b`

**Repository gate:** all seven values matched — `HEAD` `0a4fcc2`, `HEAD:.ap` and `.ap` HEAD both `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (detached), `## main...origin/main`, empty porcelain, `ls-remote` `0a4fcc2`, no listener on 3000/8000. No recovery class needed. `.ap` untouched and still `9c5cc44` after the push.

**Changed files and purpose (two, both allowlisted):**
- `frontend/src/lib/i18n/locales.ts` — ten entries added to `EXPLICIT_SEARCH_FOLDS` (6 → 16); the `:23` comment replaced. Algorithm, signature and exports untouched; `LOCALES` still four.
- `frontend/src/components/settings/PremiumPicker.test.ts` — the one existing `AC-FOLD` block extended from 13 to 31 assertions and its title updated ("these four locales" → "the twelve shipped catalogs"). No assertion removed or weakened, no new block, no new file.

**Tests and validation** (all four gates post-date the last edit; port 3000 re-checked clear before `build`):
- Focused: `npx vitest run src/components/settings/PremiumPicker.test.ts` → 5 passed (5).
- `npm run typecheck` → clean; **the code type-checks.**
- `npx vitest run` → 32 files passed / 1 skipped; 467 passed / 3 skipped (470) — identical to the measured baseline count, see MEASURED #1.
- `npm run lint` → clean.
- `npm run build` → **the build passed**, eleven dynamic routes (`ƒ`), zero static.
- Recorded deviation: the backend five were not run — diff confined to `frontend/`, pytest collects only `backend/`, mypy scope is `config game gamecore accounts catalog`.

**Commit and push:** one non-force commit `c9078f2` on `main`, subject `fix(i18n) picker search can fold æ þ ð ß œ ı`, body carrying all seven required elements. Pre-push gate: `HEAD~1` = `0a4fcc26fa8c7bca5d03c3b1ca55425d0c44bbcd` and `ls-remote origin refs/heads/main` still `0a4fcc26…`. One `git push origin main` → `0a4fcc2..c9078f2`. **Public readback:** local HEAD `c9078f2aa2b3a34c5ac51931b063f1330d49704b`, remote `c9078f2aa2b3a34c5ac51931b063f1330d49704b refs/heads/main` — equal; tree clean, `## main...origin/main`.

**Deviations, risks, missing evidence:** one deviation to disclose — the new comment is **six** prose lines, not the "four or five" section 4.1 asked for; naming nine letters by codepoint plus the four required clauses would not compress further at this file's line width. No other deviation; nothing missing.

**Fail-first evidence (step 1, new cases written and run against the UNMODIFIED `locales.ts`):**
- Hard-assert run: `Test Files 1 failed (1)` / `Tests 1 failed | 4 passed (5)`, `AssertionError: expected 'þyska' to be 'thyska'` — received `"þyska"`, exactly the predicted value, at `PremiumPicker.test.ts:36`.
- To see every new case rather than only the first, I ran the same pre-change file once with soft assertions. All 18 new assertions failed and all 13 pre-existing ones kept passing: `'sænska'`→saenska, `'æ'`→ae (both cases), `'þ'`→th (both), `'ð'`→d (both), `'œ'`→oe (both), `'ß'`→ss, `'ı'`→i, `'maður'`, `'kærlighed'`, `'straße'`, `'cœur'`, `'isık'`, and the trap assertion **`expected 'ðdðd' to be 'dddd'`** — d-stroke folded, eth did not, in one measurement.
- After the table change: same file `5 passed (5)`. That is the before/after that makes this a repair rather than an addition.

**The comment I wrote** (replaces one that claimed completeness and was wrong):

```ts
/**
 * Letters NFD + \p{Diacritic} CANNOT fold — they carry no combining mark — so an unfolded letter
 * leaves a picker row unreachable by any ASCII query. ł U+0142 L-STROKE, ø U+00F8 SLASHED O,
 * æ U+00E6 AE, þ U+00FE THORN, ß U+00DF SHARP S, œ U+0153 OE, ı U+0131 DOTLESS I, and the two
 * look-alikes ð U+00F0 ETH and đ U+0111 D-STROKE, different letters that each need their own
 * entry. Covers the languages this product targets and is NOT a complete inventory of unfoldable
 * Latin letters — extend it rather than assuming a letter is already handled.
 */
```

**Resolved Execution Issues / Near-Misses:** one. The temporary soft-assertion run above mutates the committed test if left behind — a permanently weakened test block. Restored with a reverse replace, then verified `grep -c 'expect.soft'` = 0 and confirmed absent from the staged diff before committing. No other issue.

**Pre-Existing Failure Classification:** none. The baseline suite is fully green (467 passed / 3 skipped, 1 skipped file), and the 3 skips pre-date this slice. The `[libretiles-provider-failure] …` lines in vitest output are intentional fixture logging inside passing tests, present identically at `0a4fcc2`; not failures.

**Orchestration critique:**

MEASURED
1. **Section 5's "expect MORE passing tests than the 467 passed / 3 skipped baseline" is unsatisfiable under section 4.2.** Vitest counts `it` blocks, and 4.2 forbids adding one. Measured baseline at `0a4fcc2`: 467 passed / 3 skipped (470). Measured after: identical. What grew is assertion count, 13 → 31 in the block. Assumption I proceeded on: the intended evidence is the assertion growth plus the fail-first delta, and an unchanged case count is correct rather than a failure to add coverage. If you want the count to move, 4.2 has to allow a second `it`.
2. **Section 2's user-visible claim is confirmed exactly**, independent of the prompt: `messages.is.ts:170 "settings.gameVariant.german": "Þýska"` and `:173 "settings.gameVariant.swedish": "Sænska"`, folding pre-change to `"þyska"` and `"sænska"`. I did **not** re-run the 192-value census, so that number is unverified by me; I verified the two values it produced.
3. **The eth/d-stroke trap is real and measurable, not merely a documentation hazard** — `"ðđÐĐ"` → `"ðdðd"` before the change. A repair that trusted the old comment would indeed have been a no-op for Icelandic.
4. **All ten mappings are correct as specified and the ten-entry scope is right.** Every target is something a user types; nothing needed re-deciding. `ħ`/`ŧ` correctly excluded — no target language needs them, and I did not add them.
5. **Blast radius is exactly the picker search.** `foldForSearch` has one product call site, `PremiumPicker.tsx:28` and `:31`; no test file other than `PremiumPicker.test.ts` references `foldForSearch`/`filterPickerOptions`, and no test file anywhere contains `æ þ ð ß œ ı`. That is why the full suite could not regress.

LEAD (unverified; not acted on, no code written for any of these)
1. Folding `ð`, `đ` → `d` and `æ`/`Æ` → `ae` makes previously-distinct labels ASCII-equal in principle. I did not measure fold collisions across the eight unwired catalogs; `messages.af.ts:271` suggests the campaign already tracks a zero-collision property, so the wiring slice may want to re-measure it against the *new* table rather than the old one.
2. `ẞ` U+1E9E (capital sharp s) has no entry, by scope. Would matter only if a catalog ships uppercase German text. Not observed in any shipped label.
3. `İ` U+0130 folds to `i` via NFD, so Turkish dotted capital I needs no entry — reasoned, not measured against a real label.
4. Nothing prevents this defect class recurring: there is no invariant test asserting every picker-searched label folds to pure ASCII. Such a test would have caught this at authoring time. Out of scope here.

**Report justification:** new-mutation
**Logical-whole closure:** not-closed
**Authority expiry:** my authority ends with this report. I have made no further change, have not touched the wiring or `LOCALES`, and have written nothing into Meta.
**Smallest next step:** run the wiring slice (`LOCALES` four → twelve) on top of `c9078f2`, which now lands on a correct fold table; optionally precede it with the ASCII-foldability invariant from LEAD #4.
**Context pressure:** low — roughly a fifth of the window used; no compaction occurred.

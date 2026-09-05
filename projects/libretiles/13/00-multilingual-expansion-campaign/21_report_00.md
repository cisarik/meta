### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 21, Worker exchange ordinal: 01
```

**Status: PASS**

**Phase-qualified result**: Implementation complete for MEC-UIL-W3 (A + B). Two commits, A then B, one non-force push carrying both, public readback equal.

**Start commit**: `6b8cb54319ebf1d6b6ad160b7501d9d2bb0626b7`
**End commit**: `1a6f63cd785969c392280c84298dfe80f90aadb2`

**Commits and their paths**

| Commit | Subject | Paths |
|---|---|---|
| `78e84efbbeea4b074b1c61c6aeec5f6994da40f6` | `test(i18n) twelve-slug variant-naming axis` | `frontend/src/lib/i18n/i18n.test.ts` |
| `1a6f63cd785969c392280c84298dfe80f90aadb2` | `docs describe twelve playable variants and twelve interface locales` | `README.md`, `libretiles_PRD.md` |

`git diff --name-only 6b8cb54..HEAD` returns exactly those three paths. `git rev-parse HEAD:.ap` is still `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, `.ap` is clean and detached at the same commit.

**Changed files and purpose**

- `frontend/src/lib/i18n/i18n.test.ts` — `INSTALLED_VARIANTS` 4 → 12; new `REVIEWED_VARIANTS` re-keys `ownName`; new property assertion group over the whole shipped axis with zero hand-written exonyms.
- `README.md` — Features list corrected, new short `## Languages` section, two Game Engine module descriptions corrected, Tier-1 Features bullet corrected.
- `libretiles_PRD.md` — FR-01 retitled and rewritten, FR-05 Tier 1 corrected, new FR-12 Interface Localization, four residuals added to section 8 Known Gaps.

**Tests and validation**

Repository gate, all matched before any mutation: `HEAD` = `6b8cb54…`, `HEAD:.ap` = `9c5cc44…`, `.ap` detached at the same commit, `## main...origin/main`, `git status --porcelain=v1` empty, `git ls-remote origin refs/heads/main` = `6b8cb54…`, no listener on 3000 or 8000, `npx vitest run` = `474 passed | 3 skipped (477)`.

Frontend four for commit A, all run after the last edit to the file:

| Gate | Result |
|---|---|
| `npm run typecheck` | exit 0, zero errors — **the code type-checks** |
| `npx vitest run` | `474 passed \| 3 skipped (477)` — unchanged total |
| `npm run lint` | exit 0 |
| `npm run build` | exit 0, **eleven dynamic routes, zero static** — **the build passed** |

Those are two separate claims and both hold: `tsc --noEmit` exited 0, and `next build` exited 0 (it also ran its own TypeScript pass, "Finished TypeScript in 1867ms").

**The backend five were not run.** The commit-A diff is one frontend test file; `pytest` collects only `backend/`, and mypy's scope is `config game gamecore accounts catalog`, so neither can observe it. Explicit, recorded deviation.

**Commit B is observed by no gate in this repository.** No linter, compiler or test reads `README.md` or `libretiles_PRD.md`. Section 5.2's claim-verification table below is its evidence, not a gate result. The frontend four were re-run after commit B's edits anyway — typecheck exit 0, vitest `474 / 3 (477)`, lint exit 0, build exit 0 with eleven dynamic and zero static — as the cheapest proof that nothing outside the two Markdown files changed while they were edited.

**Push and readback**: one `git push origin main`, non-force, `6b8cb54..1a6f63c main -> main`, exit 0, after the pre-push gate (`git rev-parse HEAD~2` = `6b8cb54319ebf1d6b6ad160b7501d9d2bb0626b7` and remote `main` still `6b8cb54319ebf1d6b6ad160b7501d9d2bb0626b7`). Readback: local `HEAD` = `1a6f63cd785969c392280c84298dfe80f90aadb2`, `git ls-remote origin refs/heads/main` = `1a6f63cd785969c392280c84298dfe80f90aadb2	refs/heads/main`. Working tree clean, `## main...origin/main`.

**Deviations, risks, missing evidence**: the backend-five omission above, stated as authorized. Evidence posture is non-independent; nothing here is independent acceptance. No secret was read or printed. No dependency, lockfile, or `.ap` change. No file deleted.

---

## The counts

| Quantity | Value | Arithmetic |
|---|---|---|
| Cells (slug × locale) | **144** | 12 slugs × 12 locales, asserted as `expect(cells).toBe(144)` |
| Ordered distinct pairs | **1584** | 12 slugs × 12 locales × 11 other slugs, asserted as `expect(pairs).toBe(1584)` |
| Word-boundary-on-fold collisions | **0** | measured over all 1584; no exemption list added |
| `grep -c 'expect('` on the file | **352 → 357** | +5 static call sites |
| Assertions `AC-QUEUE-VARIANT` executes | **79 → 1953** | before: 4×4×(1+3)=64, +3 spot checks, +12 all-locale leak loop. after: 79 + 144 fold-token guards + 144 label-contains + 1584 pair checks + 2 count pins = 79 + 1874 |
| Vitest total | **477 → 477** | one existing case grew; no case added |

Both assertion counts are measured, not expected: the case was run once under `expect.assertions(79)` against the restored baseline file and once under `expect.assertions(1953)` against the final file, and passed both times. That scaffolding is not committed — `grep -c 'expect.assertions'` on the staged file is 0.

The twelve slugs were derived from `VARIANT_NAME_KEYS` in `frontend/src/components/settings/GameLanguagePanel.tsx` and **match** the twelve manifests from `ls backend/assets/variants/`. `AC-QUEUE-UNKNOWN`'s slug is `hungarian`, which is not one of the twelve and has no `VARIANT_NAME_KEYS` entry — still genuinely unrecognised, so it was left alone.

`INSTALLED_VARIANTS` and `REVIEWED_VARIANTS` are referenced only inside `i18n.test.ts`, so `AC-QUEUE-VARIANT` is the only affected test, as scoped.

## Claim-verification table (commit B's only evidence)

| Claim as written | Command | Value it printed |
|---|---|---|
| twelve playable board languages, one manifest each | `ls backend/assets/variants/` | 12 files: afrikaans czech danish dutch english german icelandic italian polish portuguese slovak swedish |
| `readiness: "playable"` for all twelve | `manage.py shell -c` → `game.views.list_variant_summaries()` | `count 12`, every row `playable`, `all playable: True` |
| `validate_lexicons: 13 asset(s) audited, 0 failed` (quoted verbatim in README) | `.venv/bin/python manage.py validate_lexicons` | that exact final line, exit 0 |
| English 279,496 · Afrikaans 148,267 · Icelandic 200,182 · Danish 317,167 · German 709,844 · Swedish 822,919 · Dutch 1,293,086 · Slovak 3,005,250 · Italian 3,128,429 · Polish 3,721,704 · Czech 3,930,497 · Portuguese 4,119,831 | same command | `words=` field of each `dictionary ok` line |
| Slovak two-tile allowlist at 103 | same command | `slovak two_tile ok reason=ok words=103` |
| tile distribution **100-120 tiles depending on the variant** | `load_variant(slug).total_tiles` for all twelve | 100 english/czech/polish/slovak/swedish · 101 danish · 102 afrikaans/dutch/german · 104 icelandic · 120 italian/portuguese |
| tile bag built from the selected variant's distribution | `backend/gamecore/tiles.py` | `TileBag.__post_init__` → `_resolve_variant`; bag built from `self._variant.distribution` |
| English is the default slug | `backend/gamecore/variant_store.py` | `_DEFAULT_VARIANT_SLUG = "english"` |
| Tier 1 is the per-variant word list, Collins 2019 for English | `backend/game/services.py:118-133` | `_get_dictionary(session)` → `_get_prefix_index(session)`; `load_two_tile_words(_session_variant(session))` |
| **eleven** committed build scripts under `backend/scripts/` | `ls backend/scripts/` | 11 × `build_*_lexicon.py` (afrikaans czech danish dutch german icelandic italian polish portuguese slovak swedish) |
| each pins an upstream commit, SHA-256 of every source file, and `hunspell 1.7.3`, failing closed | per-script grep for `PINNED_COMMIT` / `EXPECTED_EXPANDER` / `sha256` / `--check` | all 11 have all four; `EXPECTED_EXPANDER = "hunspell 1.7.3"`; "Fail closed unless the host expander is exactly `EXPECTED_EXPANDER`" |
| `--check --check-dir <dir outside backend/assets/>` re-verifies instead of rebuilding | `backend/scripts/build_icelandic_lexicon.py` | `require_check_dir_outside_assets`, `--check` / `--check-dir` argparse rows, `ERROR --check found N mismatching artifact(s)` |
| host tools: not imported by Django, no Poetry or npm dependency | grep for `build_*_lexicon` imports outside `backend/scripts/`; script import block | no import anywhere outside `scripts/` (only string literals in `backend/tests/test_lexicon_provenance.py`); imports are stdlib only |
| twelve interface locales `en sk cs pl de pt is it nl da sv af` | `frontend/src/lib/i18n/locales.ts` | `LOCALES` = those twelve, in that order |
| `translate.ts` wires all twelve catalogs | `grep "messages\." frontend/src/lib/i18n/translate.ts` | 12 `messages.XX` import lines |
| every catalog defines the same 324 keys (304 text + 20 parameterised) | `AC-EXHAUST` in `i18n.test.ts`, green | `expect(textKeys.length).toBe(304)`, `expect(fnKeys.length).toBe(20)`, `…toBe(324)` |
| picker offers all twelve endonyms | `frontend/src/app/settings/page.tsx:363-400` | `LOCALES.map(...)` with `localeLabelKey` covering all twelve; `settings.uiLanguage.*` values are endonyms (`Slovenčina`, `Čeština`, `Deutsch`, `Íslenska`, `Nederlands`, `Português`, `Svenska`, `Dansk`, …) |
| `Accept-Language` primary-subtag detection and the `libretiles_locale` cookie | `frontend/src/lib/i18n/locales.ts` | `detectBrowserLocale`, `LOCALE_COOKIE_NAME = "libretiles_locale"` |
| variant names translated in every locale | `VARIANT_NAME_KEYS` + this commit's own 144-cell assertion | 12 slug entries; `expect(cells).toBe(144)` green |
| eight catalogs machine-authored, no second-opinion review | `AGENTS.md:192` and `REVIEWED_LOCALES` in `i18n.test.ts:63` | AGENTS.md states it; `REVIEWED_LOCALES = ["en","sk","cs","pl"]` |
| flags exist for only four of the twelve | `frontend/src/app/settings/page.tsx:356`, `GameLanguagePanel.tsx:27` | `LOCALE_FLAG_SRC` and `VARIANT_FLAG_SRC` each have exactly 4 entries |
| Slovak list is a hunspell expansion of LibreOffice `sk_SK`, not SSS-official | `backend/assets/variants/slovak.json` `lexicon_provenance`; `AGENTS.md:79` | `"upstream": "LibreOffice dictionaries sk_SK"`, `"expander": "unmunch (hunspell 1.7.3)"`, `"entry_count": 3005250`; AGENTS.md "playable, not SSS-official" |

Every claim in the table above appears in at least one of the two documents, and no claim was written without a command beside it.

## The four residuals, as they now appear

`README.md`, under "What this does **not** claim:"

> - The eight newest interface catalogs (German, Portuguese, Icelandic, Italian, Dutch, Danish, Swedish, Afrikaans) are machine-authored and have had **no second-opinion review**.
> - The test suite pins exact expected wording for four of the twelve locales (`REVIEWED_LOCALES` = `en sk cs pl`) and covers the other eight structurally.
> - Flags exist for only four of the twelve locales, so eight picker rows deliberately render an endonym with no flag.
> - The Slovak word list is a hunspell expansion of the LibreOffice `sk_SK` dictionary — playable, **not** an SSS-official list.

`libretiles_PRD.md`, section 8 Known Gaps (first four bullets):

> - The eight newest interface catalogs (German, Portuguese, Icelandic, Italian, Dutch, Danish, Swedish, Afrikaans) are machine-authored and have had no second-opinion review.
> - Localization tests pin exact expected wording for four of the twelve locales (`REVIEWED_LOCALES` = `en sk cs pl`) and cover the other eight structurally instead.
> - Flags exist for only four of the twelve locales, so eight interface-language picker rows deliberately render an endonym with no flag.
> - The Slovak word list is a hunspell expansion of the LibreOffice `sk_SK` dictionary: playable, not an SSS-official list.

FR-12 also carries the review residual inline ("Second-opinion review of the eight machine-authored catalogs is open work — see Known Gaps"). Neither document claims twelve reviewed languages.

## Resolved Execution Issues / Near-Misses

1. Vitest discarded `console.log` from the temporary measurement block. `vitest.config.ts` contains no `silent` or console-intercept option, so the cause was not diagnosed. Resolved by writing the measurement to `/tmp/opencode/measure.json` through a dynamic `node:fs` import instead. The scaffolding was removed before staging; verified by `grep -c 'TEMP-MEASURE'` = 0 and a SHA-256 match against the intended file.
2. Near-miss: measuring the **baseline** executed-assertion count required the pre-change file in place, and `git stash`, `git worktree` and branch creation are all forbidden. Resolved by writing baseline content back into the allowlisted path with `git show HEAD:frontend/src/lib/i18n/i18n.test.ts`, measuring under `expect.assertions(79)`, then restoring the final version from a checksummed copy (`f3d736dd…`) and confirming the digest. No forbidden git verb was used, and every gate ran after the restore.
3. Near-miss avoided: `expect.assertions(1953)` existed only transiently. The staged diff contains zero `expect.assertions` occurrences.
4. `/tmp/opencode` scratch files created by this session were deleted; pre-existing files there from earlier sessions were left untouched.

## Pre-Existing Failure Classification

None. The baseline gate matched every required value, including `474 passed | 3 skipped (477)`. The one skipped test file and three skipped cases are the pre-existing operator-only live provider probe, excluded by ordinary `npm test` by design, and are unchanged by this work. No gate failed at any point, so no failure needed attribution outside my own diff.

## Orchestration critique

**MEASURED**

1. Every number in section 3.2 is exactly right. 144 cells, 1584 ordered pairs, 0 word-boundary-on-fold collisions — all three reproduced before the assertion was written, and the assertion was green on first run.
2. The Icelandic capitalization claim is correct **and complete**. Case-insensitive-without-boundary produces exactly three collisions and they are exactly the three named: `is`/dutch `bidrod: hollenska` ← `enska`, `is`/swedish `bidrod: saenska` ← `enska`, `is`/icelandic `bidrod: islenska` ← `enska`. The naive case-sensitive `not.toContain` measures 0. Both halves of the claim hold; the word boundary is genuinely load-bearing for the stronger comparison.
3. Section 4.2's residual "only FOUR locale flags exist under `frontend/public/`" is imprecise. `ls frontend/public/*.png` is **five**: `cs.png en.png hu.png pl.png sk.png`. `hu.png` is an orphan for a language the product does not ship, already documented at `frontend/src/app/settings/page.tsx:354`. The verifiable claim is that flags are *wired* for four (`LOCALE_FLAG_SRC` and `VARIANT_FLAG_SRC` each have exactly four entries), so I wrote the wired form in both documents rather than the file-count form. `AGENTS.md:192` carries the same imprecision.
4. Two facts neither section 4.1 nor 4.2 mentioned, and both documents asserted falsely: `tiles.py` is variant-driven, not English-fixed; and the bag is **not** 100 tiles in every variant but 100-120 (italian and portuguese 120, icelandic 104, afrikaans/dutch/german 102, danish 101). Both corrected. Had I done a literal find-and-replace of "English variant", the PRD would have kept shipping "100 tiles" as a universal.
5. Section 3.3's compile-error warning is accurate: `ownName`'s outer key type derived from `INSTALLED_VARIANTS`, so growing the constant would have broken the build without the `REVIEWED_VARIANTS` re-key.
6. `AC-QUEUE-UNKNOWN`'s slug `hungarian` is still genuinely absent from the twelve and from `VARIANT_NAME_KEYS`. The anticipated fix was not needed.
7. The file already contained a second, independent twelve-slug list: `VARIANT_SLUGS` local to the `AC-FOLD-ASCII-12` describe at `i18n.test.ts:451`. The twelve slugs are therefore now stated twice in one file. Not deduped — see LEAD 1.
8. Section 3.2's "exactly as the previous slice split six others" is accurate and the precedent is unambiguous: `AC-RACKBLANK-4`, `AC-PROFILE-DUP`, `AC-PAGING-4`, `AC-TOGGLE-4`, `AC-CATALOG-COPY-4` and `AC-QUEUE-VARIANT` itself all place the property loop in the *same* `it` as the reviewed expectations. Following that shape is also what kept the vitest total at 477, matching "you grow one case, not the count".
9. Section 2's inventory of what is still false was accurate for both documents. Section 4.1's grep result was accurate: no mention of interface localization existed anywhere in either file.

**LEAD**

1. `VARIANT_SLUGS` in `AC-FOLD-ASCII-12` could be replaced by `INSTALLED_VARIANTS`, but only if the constant moves above that `describe`: the describe factory runs at collection time while `INSTALLED_VARIANTS` is still in temporal dead zone, so a naive reuse would throw at import. A dedupe is a small dedicated slice, not a drive-by.
2. `\b` is exact only for a word-character token, so I added a per-locale `expect(folded).toMatch(/^[a-z]+$/)` guard (measured: all 144 folded names satisfy it today). If a legitimate multi-word or punctuated variant name ever ships, that guard is the thing to relax — to a `(?<!\w)…(?!\w)` lookaround form — not the word boundary itself. Without the guard, such a name would have made the collision check silently vacuous rather than loudly red.
3. README's "Tech Stack" section still lists only "Collins 2019 English dictionary (~279k words, O(1) frozenset lookup)". Section 4.3 forbade touching Tech Stack, so that is now the one place in README that still reads English-only.
4. The PRD's `Updated: August 25, 2026` header was not bumped. The date has no repository-verifiable source and section 5.2 requires a command behind every claim, so I left it; a one-line follow-up if the Cooperator wants it current.
5. PRD section 1 ("Product in One Sentence") and section 2 (Product Goals) still do not mention multilingual play. Arguably where a reader looks first, but outside the named scope of FR-01 / localization placement / Known Gaps.
6. PRD section 4 Architecture Overview describes the AI layer as "an OpenAI-compatible adapter against OpenRouter and NVIDIA NIM", while README and AGENTS.md describe nine providers with five direct. FR-04 was forbidden and section 4 was not named, so both were left alone — but the two documents do not currently agree about the provider architecture.

**PRD placement choice, stated**: interface localization went in as a **new FR-12 appended after FR-11**, not as a subsection of FR-01, because it is a frontend presentation requirement with its own status and its own residuals rather than a property of the pure game core, and appending leaves FR-01 through FR-11 renumbered nowhere.

---

**Report justification**: `changed-external-state`

**Logical-whole closure**: not-closed. This objective's UI half is complete, but the campaign is not closed — twelve of twenty-four target languages remain.

**Authority expiry**: my authority ended at this report. No further mutation, no catalog change, no `docs/architecture.md` change, and no Meta write was performed or is authorized.

**Smallest next step**: a single second-opinion review slice for one of the eight machine-authored catalogs — `messages.de.ts` first — whose acceptance criterion is promoting `de` into `REVIEWED_LOCALES` and paying the resulting pinned-wording cost.

**Context pressure**: moderate — roughly half the window used, comfortable headroom remained throughout.

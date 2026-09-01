# Orchestrator diagnosis — liveplay-FAIL (slovak-playable-variant)

Authored 2026-08-29 by the sitting Orchestrator after Worker 06 / exchange 01.  
This is **not** a Worker report and grants **no** mutation authority.  
Verified against HEAD `02a4f722396e1a981f7e8668e025197d5f61297b` (porcelain empty).

## Verdict on the whole

`slovak-playable-variant` delivered the four implementation slices (assets, engine, Settings/UI, parameterized prompts). Live-play **did not** accept Slovak gameplay. Do **not** close this whole. Do **not** reopen SSS-100 tiles, English CORE hash, or Collins as English authority.

The product now *boots* Slovak. It does not yet *play* Slovak Scrabble.

## What actually happened (do not misread the table)

English NIM **also** never invented the placements. All four English terminals were `backend_ranked_candidate` (MANOR, WAIN, ARGUTELY, GASAHOLS). The house engine is what makes English look strong.

Slovak is not “Nemotron cannot speak Slovak” as the sole cause:

- SK-1 turn 1: Nemotron itself placed **ÚPIS** (`provider_candidate`). That is a real Slovak word.
- SK-1 turn 2 / SK-3 turn 1: ranked rescue placed ASCII leftovers (**VLTAVU**, **UME**) because those placements survive the frontend ASCII filter.
- SK-2: backend found **OSĽAŤA** (diacritics + blank-as-Ľ). Frontend dropped the witness. SSE `stale_witness`. No terminal.

So the English “success” and the Slovak “failure” share one architecture: **ranked/witness rescue**. Slovak rescue is **broken for Unicode**. When rescue *does* persist, the **lexicon** is too wide, so crosses like **OU** / **AM** score as legal.

## Defect A — ASCII-only SSE placement normalize (code bug, high confidence)

File: `frontend/src/app/api/ai/move/route.ts`

```ts
// normalizePlacementData ~276
!/^[A-Z?]$/.test(letter)   // drops Á Ľ Ť …
if (letter === "?" && (!blankAs || !/^[A-Z]$/.test(blankAs))) return null;
```

Same function feeds:

- `normalizePlacementArray` → playability witness rescue
- `normalizeRankedChoices` — a candidate is **skipped entirely** if `placements.length !== raw.placements.length` (any one diacritic tile voids the whole candidate)

Backend Slice 1/2 already accept Unicode (`PlacementSerializer` `_nfc_uppercase_letter`, `legality.py` variant alphabet). The SSE route still thinks the alphabet is A–Z.

SK-2 causal chain:

1. `GET ai-playability` → `found`, witness `OSĽAŤA` with `?`→`Ľ` and letter `Ť`
2. `normalizePlacementArray` returns `[]` or a shorter array
3. Rescue POST never gets the real placements → `stale_witness`
4. Overlay `page.tsx` ~1073 `syncState` after “The AI action was not accepted.”

English never hits this because Collins placements are A–Z.

**Repair shape (for a later grant, not this file):** accept one NFC Unicode letter or `?`; `blank_as` one NFC letter from the session alphabet (or `\p{L}`). Keep 15×15 bounds. Add a route test: Slovak witness with `Ľ`/`Ť` is not dropped. Do not bump `MOVE_PROMPT_VERSION`. Do not fork SSE.

## Defect B — hunspell expansion is not an SSS lexicon (content, accepted residual now material)

Shipped `backend/assets/dicts/slovak.txt`: **3 005 250** unique words (LibreOffice hunspell-sk `unmunch`). Floor/cap from Slice 0 still hold. Playable-not-official was an accepted residual. Live play made it a **gameplay** defect.

Orchestrator count on HEAD (2026-08-29):

- 2-letter entries: **269** (180 ASCII-only)
- `ou` and `am` are present (casefold)
- samples include junk: `bq`, `bc`, `bt`, `cm`, `cť`, …

`_word_passes_dictionary` (`services.py` ~185): NFC, casefold, `len >= 2`, `isalpha`, membership. No SSS 2-letter allowlist. Collins 2-letter words (QI, ZA) are *supposed* to pass in English; copying that rule onto hunspell-sk is why **OU**/**AM** score as crosses under **UME**.

Owner judgment: SSS does not treat OU/AM as playable. That judgment is the product bar for Slovak *feel*. Hunspell morphological expansion generates abbreviations, interjections, and affix noise. It is the opposite of Collins (curated tournament list).

## Defect C — the ~200k list is not in this checkout

Michal believes a ~200 000 word Slovak list (with real declension) would play better. In the **Libre Tiles** tree there is only `slovak.txt` (3.0M).

Sibling `scrabgpt_sk` (future Orchestrators may **not** have this repo) contains `scrabgpt/ai/dicts/sk.sorted.txt`:

- **50 478** words, not 200k
- `ou`/`am` **absent**
- 103 two-letter rows, look more word-like (`aj`, `ak`, `či`, `čo`…)
- **Unknown license** — Slice 0 explicitly forbade copying it

Do **not** copy `sk.sorted.txt` into Libre Tiles. Ask Michal for the actual ~200k file path + license. If it does not exist as a file he can produce, Researcher must find a license-clean source or a hunspell *filter* (not a silent 50k swap).

## Defect D — secondary live-play friction (do not promote to the main fork)

- Fallback queue split a 120s / 30-step store across a 5-lane queue → attempt `timeout: 23`, `max_steps: 10`. Makes Slovak turns feel dead and pushes the route into rescue.
- Protocol incomplete (SK-2 no persist; SK-3 stopped by owner). **Not** a `pass`-while-`found` hard fail.
- SEARCH_PROFILE DB rows may still say Collins (accepted residual; CORE is non-overridable).

## What is already good (do not tear down)

- SSS **100** tile bag (not 112, not ScrabGPT 108). No CH/DZ/DŽ tiles.
- Per-path dictionary cache; no `isascii` in `_word_passes_dictionary`.
- Settings English/Slovak; create/join send slug; live session not PATCHed.
- Á shows 4 on rack/board (`tile_points` snapshot).
- English CORE SHA-256 `c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60`, version `pfr-s2-core-1`.
- English live NIM still *places* via ranked rescue. Do not “fix Slovak” by weakening that path.

## Recommended next logical whole

Name: **`slovak-gameplay-quality`**  
Goal: Slovak games produce SSS-*feeling* legal words, and Unicode rescue/rank persist the same way ASCII already does.

Do **not** treat this as Slice 4 of `slovak-playable-variant`. New material axis: lexicon quality + live Unicode SSE. New planning cycle.

Suggested route for the **fresh** Orchestrator (Cooperator must select):

1. **Researcher Worker first** (read-only, network for licenses/SSS 2-letter lists): what may ship; what 2-letter set SSS uses; whether Michal’s 200k exists and is clean; hunspell filter vs replace.
2. **Planner Worker** after research (or in the same session only if Michal selects a combined plan): Slice A Unicode `normalizePlacementData`; Slice B lexicon replace or filter; Slice C live-play 2 EN + 3 SK again.
3. **Do not implement** until Michal picks the route. Unicode-only first is valid if he wants SK-2 to stop crashing *before* the lexicon debate.

## Locked forks that stay locked

SSS 100; English Collins; English CORE bytes; judge 503 / no false invalids; no JULS; no second SSE route; no chrome i18n; no push unless granted; no ScrabGPT Python import.

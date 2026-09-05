> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `frontend/src/lib/i18n/messages.sv.ts` landed as `fde3321`, pushed, readback equal, porcelain clean.
> **ACCEPTED.** Nine MEASURED findings and eight LEADs — the most thorough report of the campaign.
> ⭐ **M1 IS THE FORTY-NINTH AND IT IS A SELF-CONTRADICTION INSIDE ONE SECTION OF MINE.** ✔ Verified:
> `messages.pt.ts` ships `279\u00A0496`, so my §5.3 sentence naming `pt` among the period catalogs was
> false, and `messages.cs.ts` ships it too — **FOUR catalogs use U+00A0 (sk · cs · pl · pt), not two.**
> The reason is subtle and to catalog 2's credit: `Intl.NumberFormat("pt")` yields a period because bare
> `pt` resolves to Brazilian conventions, while `pt-PT` yields U+00A0 — and catalog 2 chose by LOCALE
> rather than by the bare tag. It was more careful than my prompt.
> ⭐ **M4 is the SIXTH defect in the audit family and the SECOND I introduced myself:** I added a
> per-language `æ`/`ø` grep in PROSE without the comment exclusion that §7.1's own code block puts on
> every line — one section after restating the rule that forbids exactly that.
> ⛔ **AND ONE MEASURED CLAIM OF ITS OWN IS WRONG, the second Worker claim I have corrected:** M6 says
> `OUTCOME_META` spans `:36-73`. ✔ Measured: its closing `};` is at **`:75`**, so my `:36-75` was right.
> Its seven-arm count is correct and the rest of M6 holds.
> My rulings on all seventeen findings are in `./00_notes.md` §48. The report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 16, Worker exchange ordinal: 01
```

**1. Status:** PASS

**2. Phase-qualified result:** Implementation complete for MEC-UIL-C7-sv. One new orphaned file, 296 text keys and 20 function keys, four frontend gates green, one commit, one non-force push, public readback equal.

**3. Start and end commit:** start `b0f8a2825d42d02b3e5dbafa0b15b616881db341` → end `fde3321f9c586a4bfa23773ad2cbadc53e7dedad`

**4. Changed files and purpose:** `frontend/src/lib/i18n/messages.sv.ts` (NEW, 670 lines, the only path) — the Swedish interface catalog. No existing file modified, moved or deleted; `git status --porcelain=v1` showed exactly one line, `?? ` the new file, before staging.

**5. Tests and validation:**

Structural audit, section 7.1, all seven lines:

```text
git status --porcelain=v1                     one line, `?? ` the new file
diff <(head -7 sv) <(head -7 de)              EMPTY
grep -c 'pluralSv('                           3
grep -nE '^[^/]*plural'                       4 lines: import :11, calls :626 :634 :641
grep -nE '^[^/]*(aria-live|role="status")'    ZERO
forbidden-construct scan (tail -n +8)         ZERO
git diff --check                              clean
key order vs messages.en.ts                   text 296/296 IDENTICAL, fn 20/20 IDENTICAL
```

Four frontend gates, from `frontend/`, all after the final edit:

```text
npm run typecheck   exit 0   — the code TYPE-CHECKS; completeness proof for all 316 keys
npx vitest run      exit 0   — 467 passed / 3 skipped (32 files passed, 1 skipped),
                               byte-identical to the baseline measured BEFORE file creation
npm run lint        exit 0
npm run build       exit 0   — THE BUILD PASSED: eleven dynamic routes, zero static
```

`ss -tlnp | grep -E ':(3000|8000)'` returned no listener both at the repository gate and immediately before `npm run build`. "The build passed" and "the code type-checks" are two separate claims and both hold. The three focused tests (`i18n.test.ts`, `plural.test.ts`, `prompts.test.ts`) are inside the 32 green files; no test file was added or edited.

Recorded gate deviation: the five backend gates were **not** run. The diff is confined to `frontend/`, pytest collects only `backend/`, and mypy's scope is `config game gamecore accounts catalog`, so no backend gate observes this change.

**6. Commit and push result:** one commit `fde3321`, subject `feat(i18n) the Swedish interface catalog`, staged with `git add frontend/src/lib/i18n/messages.sv.ts` only. Pre-push gate: `git rev-parse HEAD~1` = `b0f8a2825d42d02b3e5dbafa0b15b616881db341` and `git ls-remote origin refs/heads/main` still `b0f8a28…` — the remote had not moved. One `git push origin main`, non-force: `b0f8a28..fde3321  main -> main`. Readback: local HEAD `fde3321f9c586a4bfa23773ad2cbadc53e7dedad`, `git ls-remote origin refs/heads/main` `fde3321f9c586a4bfa23773ad2cbadc53e7dedad` — equal. `HEAD:.ap` unchanged at `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

**7. Resolved Execution Issues / Near-Misses:**

- Near-miss, caught before commit: my first draft of the `game.lexicon.*` comment said "Eleven rows take the language adjective … `afrikaans` is the one exception", which is off by one and is the same error `messages.de.ts:274` contains. Corrected to "TEN for ten" after deriving the count by command. Nothing else was edited to satisfy an audit pattern.
- The mandated Next.js doc resolved only from `frontend/`, not from the repo root; the path list mixes two roots. Read successfully (Next 16.3.4). Its title-cased Dutch noun `Winkelwagen` was read as a Next.js example, not as style.

**8. Pre-Existing Failure Classification:** none.

---

## Terminology and choices

**The nine frozen terms** (once — the file's terminology block is their canonical home): tile `bricka` · letter `bokstav` · rack `brickställ` · blank `blank`, always carried by the compound `blankbricka` where the piece is named · bag `påse` · board = `bräde`/`spelbräde` (surface) **and** `parti` (saved-game metonym) · pass `passa` with the game call `pass` · points `poäng` · rival = opponent `motståndare`.

The three mandatory splits hold. `bräde`/`parti` makes it **eight for eight**, with `spel` kept apart as the product/ruleset (hence `Spelvariant`, never `Partivariant`). `passa` and `byta` stay different words. tile and letter are **not** collapsed: a `blank` is a `bricka` carrying no `bokstav`.

The pass **noun exists** in Swedish, as in Danish and unlike Icelandic/Italian/Dutch — `pass` is the settled card- and board-game call — so `game.toast.passRejected` needed no verbal rephrasing. Both Danish knock-ons recur: `ett pass` is also a passport (disambiguated by the adjacent `Passa` button) and `passa` also means "to fit", so `error.conflict` says `strider mot` and never `passar inte`.

**rival/opponent verified, not inherited from the tally:** Swedish `rival` exists but denotes a personal rivalry, not a game opponent; `motståndare` is the game word and covers both senses. One word, verified for Swedish. Nine for nine.

**One term the prompt did not anticipate:** `blank` is also an ordinary Swedish adjective meaning glossy. That collision cost more authoring thought than any listed trap. Resolved German's way — the piece is always `blankbricka`, bare `blank` appears only in `draw.blankCaption` (which renders directly under the tile it labels), and no surface description uses `blank` adjectivally (`settings.board.blackDesc` is `Glansig nattlack`). `joker` was available and deliberately rejected as Danish's and Dutch's choice.

**Register:** informal `du` / `din` / `ditt` / `dina`, error messages included; never `Ni` / `Er`. It cost nothing, and for a datable reason rather than Danish's: the du-reform of the late 1960s retired `Ni` as a polite form, and what survives reads as distancing or archaic. So, as in Danish, there was never a second usable register to weigh.

**Label style:** IMPERATIVE for every control, action label, column heading and accessible name (`Spela · Passa · Byt · Avbryt · Logga ut · Öppna · Sök · Skicka · Välj · Återställ · Ge upp`). **The control convention and the prose register COINCIDE**, as in Italian and Danish and unlike Dutch: the imperative is both what a Swedish button says and what `du`-prose says (`Välj ditt nästa parti`, `Kontrollera de angivna uppgifterna`, `Försök igen`). No distinction was manufactured. Pre-authorized exceptions used: the **pagination pair** (`Föregående`/`Nästa`, adjectives of the implied `sida`), the **toggle state words** (`På`/`Av`), and the **badge words** (`settings.board.active`, `overlay.bestBadge`).

**The six slot fillers** — two of the six are PHRASES, unlike Danish and Dutch:

| site | one | other |
|---|---|---|
| `a11y.rackTile` points | `poäng` | `poäng` |
| `error.throttled.minutes` | `minut` | `minuter` |
| `controls.tilesSelected` tiles | `bricka vald` | `brickor valda` |

`poäng` is genuinely invariable in number ("1 poäng", "34 poäng"), as Danish `point` and Icelandic `stig` are — same word in both slots, commented so nobody invents a second form. The tile slot **had** to become a phrase: a Swedish predicate adjective inflects for number (`vald`/`valda`), so it cannot be appended outside the helper the way German appends `ausgewählt`. The colon-label escape was available and deliberately not used — `GameControls.tsx:80-81` is a full-width centred line that wraps freely and is bounded by rack size 7, which is Italian's reasoning. Rendered at 0/1/2/7/11/21: `0 brickor valda`, `1 bricka vald`, `2 brickor valda`, and `0 poäng` — Swedish writes the plural at zero, never Portuguese's `0 ponto`.

**`AI` article:** COMMON gender `en`, from `artificiell intelligens` (an en-word). Swedish attaches an inflectional ending to an abbreviation with a **COLON**, so the definite is `AI:n` and the genitive `AI:ns` — the `TV:n` / `EU:s` convention, and **not** Danish's apostrophe `AI'en`. Same rule for `GPU:n`. Because Swedish marks definiteness as a suffix, the choice is visible in most AI strings, not only in an article.

**Protected tokens — and Swedish is the campaign's first case where the decision changes a byte.** `model` → TRANSLATED (`modellval`); observable, because Swedish `modell` has two l's, so the untranslated reading would give `modelval`. `chat` → **TRANSLATED** at all six sites (`chatt`, `Partichatt`, `Chattmeddelande`, `Chatten är …`); observable, because the Swedish noun is `chatt` with two t's. Reasoning: §6.4 classifies all of these as PROSE and prescribes TRANSLATED for prose; all six new catalogs already translated `model`, which sits on the same D6 list; and no English `chat` identifier is exposed anywhere in the Swedish UI to match against. For Danish and Dutch this produced the identical string either way — for Swedish it does not, which is why I flag it below as the item most likely to be reversed. `Libre Tiles`, `AI`, `Collins Scrabble Words 2019` and its word count are preserved unchanged.

**All FOUR call sites of 6.5 are HARMLESS for Swedish — each answered on its own structure, not by agreeing with Danish:**

1. **`game.aiPlayedFor.before` + `.points`** (verified at `page.tsx:338`, score span fixed in the middle). Harmless. Swedish is Mainland Scandinavian and **never developed** the West Germanic verb-final order — the mechanism is North vs West Germanic, not something Danish "lost and Swedish also lost". Its perfect is auxiliary + **SUPINE** + object, so `AI:n har fått` / `34` / `poäng` maps onto the two spans with the perfect tense intact. German and Dutch had to drop it because their verb phrase is final. Ships the perfect; `game.toast.aiPlayedWord` is kept in the same tense so the one toast is consistent.
2. **`board.reset` + `board.zoomNoun`** (verified at `Board.tsx:692-693`, two adjacent spans, fixed order). Harmless. The Swedish imperative takes its object after it, so `Återställ zoom` is correct in exactly the imposed order — no loanword (German) and no style switch (Dutch). `zoom` is carried bare with no definite suffix, so the loan's en/ett class is never settled. Both spans are CSS-uppercased at `Board.tsx:691`.
3. **`game.aWord` inside `game.toast.aiPlayedWord`** (verified at `page.tsx:1003`). Harmless. Swedish's **indefinite** article is a separate word — only the definite is a suffix — so `ett ord` is safe; `ord` is neuter. Length 7, in the article-carrying group with de/nl/it/pt rather than the bare-noun group.
4. **`history.open`** (verified as both `GameHistoryPanel.tsx:295` heading and `:139` button). Harmless — the imperative `Öppna` serves both roles. Its **partner did cost something**, as it did for Danish: `aktuell`/`aktuellt` inflects and the implied noun is the neuter `parti`, so the agreeing form would be `Aktuellt`; `Nuvarande` is an `-ande` participial adjective, and Swedish `-ande` participles are indeclinable in every gender, number and definiteness. Same strategy as Danish, different word, same structural reason stated independently.

**The three statements of 7.1:**

- **Capitalization.** Derived mechanically over all 296 emitted values: the only capitalized words appearing outside sentence-initial position are `A` (the tile letter, ×3), `AI` (×11) and `AI:n` (×3), `Collins Scrabble Words` (×2 each), `GPU` and `GPU:n`, `Libre`/`Tiles`, and `NYA` (English's deliberate emphasis caps in `settings.gameVariant.description`). **Zero common nouns and zero language names are capitalized outside sentence-initial position.**
- **`å ä ö` integrity.** Real single-codepoint UTF-8 throughout: `å` U+00E5 ×93, `ä` U+00E4 ×233, `ö` U+00F6 ×113, plus `Å` ×5, `Ä` ×6, `Ö` ×4. The file is NFC-identical to itself and contains no combining marks in U+0300–U+036F. No `aa`/`ae`/`oe` substitution anywhere: the only `aa` in the file is the language name `afrikaans`/`Afrikaans`. Fold verified: `Åtgärd → atgard`, `Välj → valj`, `Sök → sok`.
- **The `æ`/`ø` grep (5.7 item 2).** **CLEAN in every emitted string — zero `æ ø Æ Ø` across all 316 values**, proven two ways: `grep -nE '^[^/]*(æ|ø|Æ|Ø)'` returns nothing, and an independent extraction of all 643 string/template literals in the comment-stripped code region finds 0. The grep **exactly as written** in 5.7 returns 14 hits, all inside comments, because §5.7 and §4 together require the file to name the Danish forms it does not reuse. That pattern defect is filed under `Orchestration critique` and the file was **not** edited to satisfy it, per 7.1 rule 5.

## The twelve language names

| lexicon id | `settings.gameVariant.*` (picker) | `game.lexicon.*` (running text) |
|---|---|---|
| english | Engelska | *(no key — the English variant's `lexicon_id` is `collins2019`)* |
| slovak | Slovakiska | Finns inte i den slovakiska ordlistan |
| czech | Tjeckiska | Finns inte i den tjeckiska ordlistan |
| polish | Polska | Finns inte i den polska ordlistan |
| afrikaans | Afrikaans | Finns inte i ordlistan för afrikaans |
| italian | Italienska | Finns inte i den italienska ordlistan |
| dutch | Nederländska | Finns inte i den nederländska ordlistan |
| german | Tyska | Finns inte i den tyska ordlistan |
| portuguese | Portugisiska | Finns inte i den portugisiska ordlistan |
| danish | Danska | Finns inte i den danska ordlistan |
| swedish | Svenska | Finns inte i den svenska ordlistan |
| icelandic | Isländska | Finns inte i den isländska ordlistan |

**Capitalization convention, by family:** CAPITAL in the picker, because a picker row is a standalone list item and therefore sentence-initial; **lowercase** in `game.lexicon.*` running text, because Swedish does not capitalize a language word in itself. Swedish sides with Danish, Italian and Icelandic, against German and Dutch.

**Agreement:** I get the same free pass as Danish, and slightly better. The Swedish definite adjective is `-a` for every gender and number, so agreement with `ordlistan` is free — and the definite adjective is the **same string** as the picker label modulo case, ten for ten (verified by command). `afrikaans` is the one exception: Swedish has no adjective built on it and the nearest form `afrikansk` means *African*, so that row carries the bare name after a preposition. Also confirmed: only **ten** rows carry an adjective, not eleven or twelve — there are eleven language rows and `afrikaans` is the eleventh.

**Substring collisions derived from my strings, case-insensitively, exhaustively over all 132 ordered pairs: ZERO.** As expected — Icelandic remains the campaign's single outlier. `Afrikaans` is byte-identical to English because Swedish has no separate exonym; commented per §4. None of the twelve contains `æ` or `ø`, and every diacritic they carry folds (`Nederländska → nederlandska`, `Isländska → islandska`).

## Where I diverged from Danish

The pieces and the bag: `bricka`/`brickorna`/`påse`/`brickställ` against `brik`/`brikkerne`/`pose`/`brikholder` — and the precise relation is **cognate pairs in different shapes**, not different stems, which is why the pull is strong: Danish's plural is `-er`+`-ne`, Swedish's is `-or`+`-na`. The alphabet: `å ä ö` against `æ ø å`, so `Vælg`/`Søg`/`Bekræft`/`bræt`/`næste` became `Välj`/`Sök`/`Bekräfta`/`bräde`/`nästa`, and the `æ`/`ø` grep is clean in every emitted string. The `-lig` trap: `tillgänglig`/`ogiltig`/`möjlig`, where the suffix transfers and the stem does not; `Logga ut` is 8 where `Log ud` is 6. Four more the campaign measured rather than guessed: `AI:n` against `AI'en`; U+00A0 against the period; CLDR `other` at 0.5 against Danish's `one`; and `betänketid` against `betænkningstid`.

**The worked example catalog 8 should take from this:** 22 of my 296 values came out **byte-identical to Danish**, and every one is independently correct Swedish — `Konto`, `Profil`, `Resultat`, `Turstatus`, `Turneringstempo`, `Glanseffekt`, `Byt`, `Din tur`, `Partier`, `AI-dueller`, plus the preserved tokens and the four endonyms. Between near neighbours that is the expected outcome, not evidence of lifting; what makes it safe is that each was derived from Swedish morphology and the *distinctive* forms were all rewritten. Afrikaans against Dutch will produce a far larger set, and §4 has no rule for it (see LEAD-5).

## Flagged risks

Nineteen items. None blocking; none verifiable by me, because the file is orphaned and renders nowhere.

**Terminology I am least sure of (1–4):**

1. **`blank` as a Swedish noun** for the blank tile. Swedish Scrabble usage supports it; Alfapet/Wordfeud usage would say `joker`. I could not consult a source — network authority is none. Fallback if a reviewer objects: `joker`, at the cost of looking like a lift from Danish and Dutch.
2. **`chatt` at all six protected-token sites** (see LEAD-1). The single most likely item to be reversed.
3. **`Används`** at `settings.board.active` — a present-passive verb where every sibling catalog used a phrase or an adjective.
4. **`Uppdaterad`** at `history.col.updated` — the one place I chose table convention over the agreement rule I applied everywhere else; flagged in the file as breaking my own pattern.

**Traps in 5.2 that DID bite, or that a fixed call site forced (5–8):**

5. **`settings.board.active` — BITES SWEDISH**, as it bit Danish, Portuguese and Icelandic and unlike Dutch and Italian. Swedish predicate adjectives inflect (`aktiv`/`aktivt`/`aktiva`); the three sibling labels at `settings/page.tsx:216` are not one class (`Trä` is a neuter NOUN, `Svart` and `Grön` are colour adjectives) and the implied head is ambiguous between `ett bräde` and `en yta`. Resolved with an invariable verb form.
6. **`history.current` — cost the indeclinable `Nuvarande`** instead of the agreeing `Aktuellt`, forced by `history.open`'s dual call site.
7. **`history.endReason.sixZero`** — the one place the `tur`/`drag` split is deliberately not honoured: English says "turns", but Swedish plural `turer` reads as *trips*. Commented at the key.
8. **`profile.subtitle`** uses `ställe` (a place) two panels away from the frozen `brickställ` (a rack). Different words; a reviewer may still want it reworded.

**Overflow risks (9–13):**

9. `board.pinchToZoom` 17 and `board.dragToPan` 18 against English's 13 and 11, on `Board.tsx:668`'s `text-[0.72rem] uppercase tracking-[0.18em]` pill — 39 total against English's 28, just under Danish's 40 and well under Dutch's 47. `board.hide` ties English at 4.
10. `board.reset` 9 + `board.zoomNoun` 4 in the zoom-reset button, against English's 5 + 4. `Återställ` is the standard Swedish UI word and has no shorter honest form.
11. `rack.empty` 26 and `blank.chooseLetter` 32.
12. `game.blocker.*.body` strings run long because `gratismotståndare` appears twice in each; `max-w-md` at `page.tsx:426` wraps.
13. `controls.confirmExchange` 13 is **under** English's 16, so the non-wrapping control grid gains room.

**Reported lengths the prompt asked for (14–15):**

14. **`overlay.bestBadge` = `BÄST`, length 4.** The shortest form that cannot be read as untranslated English, because Swedish spells it with `ä` — a bare `BÄST` is not `BEST`. Ranks: de 3 · **sv 4** · en 4 · is 5 · nl 5 · da 5 · pt 6 · sk 8 · cs 8 · it 8 · pl 9.
15. **`overlay.best` DIVERGES**, at `Bästa draget` (12), joining de/is/nl/da rather than the same-word group. `header.logout` 8 and `header.loggingOut` 12.

**Absent risks — every 5.2 trap that did NOT bite Swedish, with the structural reason (16–19 plus the list):**

16. **The eight `history.outcome.*` — ABSENT, twice over.** Both candidate head nouns are NEUTER (`ett parti` in the row, `ett resultat` in the header), so a single neuter form is correct at both sites; and `Vinst`/`Förlust` are nouns that agree with nothing at all, while `Väntar`/`Pågår` are invariable finite verbs. Only the two participles carry a form, and both take the neuter `-t` both head nouns require.
17. **`history.unknownDate` — ABSENT, and by a *different* mechanism from Danish's.** Danish escaped morphologically (`ukendt` already ends in `-t`, so its two indefinite forms coincide). Swedish escapes by **gender**: `ett datum` and `ett användarnamn` are both neuter, so `Okänt` is correct at all four verified sites (`GameHistoryPanel.tsx:97`, `ProfileModal.tsx:23` and `:26` are dates; `:220` is the username).
18. **`game.gaveUp` — ABSENT, and more strongly than for Danish.** Danish's participle happens not to agree; Swedish's perfect uses a dedicated **SUPINE** (`gett`), which is not a participle at all and by definition never agrees with anything. `har gett upp` needs no gender.
19. **`history.endReason.bagEmpty` — ABSENT despite genuinely mixed gender.** `en påse` + `ett brickställ` is the configuration that forced Icelandic into a neuter. Swedish needs no workaround: the shared predicate is plural and the Swedish plural adjective is `-a` for every gender — `Påse och brickställ tomma`.

Also absent: **`draw.reason.closer`** (verified at `draw-result.ts:29-30` that the values are tile letters; `är` is an invariable finite verb, `närmare` an invariable comparative); **`game.status.opponentPlaying`** (finite-verb predicate, nothing agrees — and unlike Danish, Swedish needed no disambiguating adverb, because `spelar` is only the verb while the player noun is `spelare`; the `nu` I kept is stylistic and commented as such); **`profile.memberSince`** (`sedan` is a bare preposition with no article, no case and no definite suffix, so "Medlem sedan Okänt" is exactly as awkward as the English original and no more so); **the ScorePanel `header.logout` risk** (8 characters, mid-pack, level with German, and the in-place swap partner is 12 against English's 14); **the `PremiumPicker` fold gap** (all three of `å ä ö` decompose under NFD, so picker search is unaffected); and **the whole interpolated-value list** — no definite suffix and no inflected adjective attaches to any opaque value anywhere in the catalog. The three known `messages.en.ts` shape problems were written around and not proposed for repair.

## Orchestration critique

Two labelled lists. **MEASURED** = verified by command in this session. **LEAD** = my judgement, explicitly not measured; do not act on a LEAD as if it were a measurement.

### MEASURED

**M1 — §5.3 contradicts itself about `pt`, and the second half is false. This is the forty-ninth.** Sentence one is right: five of the six new catalogs ship a period (`de · nl · it · is · da`), and it correctly excludes `pt`. Sentence two says "`da/nl/de/it/is/pt` use a period" — but `messages.pt.ts:54` ships `279\u00A0496`. Measured: `Intl.NumberFormat("pt")` → `279.496` (bare `pt` resolves to pt-BR conventions) while `Intl.NumberFormat("pt-PT")` → `279 496` U+00A0 — and catalog 2 is explicitly pt-PT by its own header. Catalog 2 chose by *locale* rather than by the bare tag, correctly. **Four shipped catalogs use U+00A0** (sk, cs, pl, pt), not two. A Worker who trusted sentence two would treat `messages.pt.ts` as a period model and could have copied a period from a catalog that does not have one.

**M2 — "one of only two shipped catalogs whose thousands separator matches yours" undercounts by two.** `messages.cs.ts:18` and `messages.pt.ts:54` both ship the U+00A0 escape alongside sk and pl.

**M3 — §6.4's measured set of six prose sites is missing one; the `chat` token has SIX sites, not five.** `messages.en.ts:36`, `meta.description`, contains `chat` in prose: "…live human matches, **chat**, and polished drag-and-drop play." All ten shipped catalogs keep the token there. So there are **seven** enText values with a protected token in prose. This matters for catalog 8 far more than for me: for Afrikaans the native word differs from `chat`, so the decision is observable and the site list must be complete. I translated all six and commented `meta.description` as the site not in the campaign's list.

**M4 — the `æ`/`ø` grep of §5.7 item 2, as specified, is unsatisfiable together with §4 and §5.7 itself, and it is the exact pattern class §7.1 rule 5 forbids.** §5.7 requires the file to record where it diverged from Danish; §4 makes the file the canonical home of that decision; naming a Danish form requires typing `æ`/`ø`. My file has 14 such occurrences, every one inside a comment citing a form I did not reuse. The five lines in §7.1's bash block all carry the `^[^/]*` comment exclusion — the fix catalog 4 generalized to "every line" — but this sixth check was introduced in prose *without* it, twice (5.7 item 2 and 7.1's restatement, which calls it "the one place a per-language grep IS appropriate"). Corrected form `grep -nE '^[^/]*(æ|ø|Æ|Ø)'` returns ZERO. I did not edit the file. The generalizable rule: **the comment exclusion belongs on every audit check, including the ones the prose introduces, not only the ones inside the code block.**

**M5 — catalog 6's own note to me overstates the relationship.** `messages.da.ts:76-78` says "the Swedish words are built on different stems, so `brik` and `pose` are not transferable". `brik`/`bricka` and `pose`/`påse` are **cognate pairs in different shapes**, not different stems. The instruction is right and I followed it; the reason is wrong, and it under-warns in a specific way — a Worker told "different stem" may look further from `bricka` than the language wants. For catalog 8 the relationship is tighter than cognate (Afrikaans descends from Dutch), so the wording matters more there, not less.

**M6 — line-number drift, two places.** `settings/page.tsx:218-220` contains only the `settings.board.active` badge span; the three surface labels it "sits beside" are at `:216`. `OUTCOME_META` spans `GameHistoryPanel.tsx:36-73`, not `:36-75` (the seven-arm count is exactly right). Everything else I re-derived matched: `Board.tsx:652-653`, `:668-677`, `:692-693`; `page.tsx:338`, `:426`, `:671`, `:1003`; `ProfileModal.tsx:23`/`:26`/`:220`; `GameHistoryPanel.tsx:97`/`:139`/`:269`/`:295`; `ScorePanel.tsx:208-242` and `:346`; `draw-result.ts:29-30`; `PremiumPicker.tsx:239`/`:301`; `i18n.test.ts:495-506`.

**M7 — two off-by-ones in the shipped corpus and in §5.6.** `messages.de.ts:274-276` says "Eleven rows take the declined German language adjective. Afrikaans is the exception" — internally inconsistent by one; `messages.da.ts:419` says "Ten", which is right. §5.6's "`game.lexicon.<id>` names all twelve as adjectives" is also off: there is no `game.lexicon.english` at all (the English variant's `lexicon_id` is `collins2019`), so there are eleven language rows and ten adjectives. I made the same error in my first draft and corrected it by deriving the count.

**M8 — every other measured claim in the prompt reproduced exactly.** node v26.4.0 / ICU 78.3; sv two categories with `0→other, 1→one, 2→other, 11→other, 21→other, 1000000→other`; sv `other` at 0.5 and 1.5 against da's `one` (Danish is the fraction outlier, confirmed); `Intl.NumberFormat("sv")` → `279 496` with U+00A0 (codepoint `a0` verified); all twelve `Intl.DisplayNames("sv")` exonyms; the `header.logout` and `header.loggingOut` tables across all ten catalogs; the `overlay.bestBadge`/`overlay.best` divergence set; `board.pts` vs `game.aiPlayedFor.points`; `game.aWord` lengths; GLOSSARY's ten-row `settings.gameVariant.*` table omitting czech and polish; the `i18n.test.ts` product-source scan asserting exactly one `aria-live` and one `role="status"`; 296 + 20 keys; and every existing catalog already in `messages.en.ts` key order.

**M9 — one precision point on `EXPLICIT_SEARCH_FOLDS`.** `locales.ts:24-31` already maps `ø → o` and `Ø → o`. §5.3's statement is exactly right (`æ`, `þ`, `ð` do not fold); §8's "a LIVE defect repair for Icelandic and Danish letters" is right only for `æ` on the Danish side. Verified: `æ → æ`, `þ → þ`, `ð → ð`, `ø → o`. Catalog 6's own comment got this right.

### LEAD

**L1 — the `chat` decision is mine and I do not want it read as settled.** I translated all six sites to `chatt`. My reasoning is in the file and above. Against it: D6's flat text says keep `chat`, and ten shipped catalogs keep it. In favour: §6.4 labels these sites PROSE and prescribes TRANSLATED for prose; all six new catalogs already translated `model`, on the same list; and Swedish is the **first** catalog where either decision changes a byte, so the campaign has never actually had to decide. Six strings to reverse. This is the one item I would put in front of the Cooperator first, and I would not be upset to be overruled.

**L2 — `blank` is the term in the nine I would least defend.** Swedish Scrabble supports it; consumer word games say `joker`. No network authority to check. If a reviewer prefers `joker`, three strings and the compound change.

**L3 — `Används` and `Uppdaterad`** are the two places I chose a convention over a rule. I think both are what Swedish UIs do; neither is provable from inside this task.

**L4 — I would not want my "eight for eight" on the `board` split treated as a tally.** I verified `bräde`/`parti` against Swedish board-game usage on its own ("ett parti schack"), the way §5.4 asks. The count is a coincidence of eight correct answers, not evidence about the ninth. Same for rival/opponent: nine for nine, each checked.

**L5 — what catalog 8 needs that is not in the skeleton: a NEAR-NEIGHBOUR byte-identity rule.** §4's new rule covers byte-identity with **English** only. Measured here: 11 of 296 values are byte-identical to English (all commented) and **22 are byte-identical to Danish**, every one independently correct Swedish. Afrikaans against Dutch will produce very much more than 22 — the two share most of their function words and a great deal of their vocabulary — and a reviewer diffing `messages.af.ts` against `messages.nl.ts` will have no mechanical way to separate a correct coincidence from a lift. I would add to §4: *report the byte-identical-to-neighbour count, and comment any of them a reviewer would find surprising.* That gives catalog 8 the same evidential footing §4 gave me against English, and it is the one gap I think is worth a prompt change rather than a note.

**L6 — and the mechanical hazard transfers exactly.** Measured: `Intl.NumberFormat("af")` → `279 496` with **U+00A0**. Afrikaans's trap, Dutch, ships a period — the identical configuration I was in. Catalog 8 should get §5.3's warning in the same emphatic form, with `pt` corrected out of the period list per M1, and with `af`'s own measured value stated.

**L7 — §5.2 has no slot for an unlisted trap.** The "report either answer per key" framing is the best instrument in this prompt and I used it eleven times. What it lacks is a place to report a trap the prompt did **not** list that the language does have. Mine was the `blank` noun/adjective homograph — not a gender trap, not a call-site trap, and it cost more authoring judgement than any listed item. Afrikaans will have homographs of its own (and a `g`/`gh` orthography question Dutch does not have). One line — *"name any trap this section does not list that your language does have"* — would catch them.

**L8 — a small process observation, offered because catalogs 2-6 audited their predecessors.** The §7.2 instruction "MEASURE THE BASELINE BEFORE YOU CREATE THE FILE" is load-bearing and worked (467/3 before, 467/3 after). What it does not say is *re-run the gates after any post-audit edit*. I edited four comment blocks after the first structural-audit pass and re-ran all four gates and the full audit afterwards; a Worker reading the stage list literally could have gated before its last edit. One clause — *"the four gates and the structural audit must both post-date your last edit"* — closes it.

---

**Do not list the 316 keys:** the diff is in Git at `fde3321` and the type system proved the key set.

**Report justification:** `new-mutation`

**Logical-whole closure:** not-closed. Catalog 7 of 8 has landed; Afrikaans remains, and the wiring slice that adds all eight to `LOCALES` remains after it.

**Authority expiry:** my authority ends with this report. I have not begun the eighth catalog, have not touched `LOCALES`, `translate.ts`, `index.ts`, `plural.ts` or any test, have not added a locale, and have not written anything into `/home/agile/meta`.

**Smallest next step:** issue catalog 8 (Afrikaans) with three corrections carried in — §5.3's period list with `pt` removed and `af`'s own measured U+00A0 stated, §6.4's prose-site list extended to include `meta.description`, and the `^[^/]*` comment exclusion applied to the per-language neighbour-letter grep — plus the near-neighbour byte-identity reporting rule of LEAD-5.

**Context pressure:** moderate. Two reference catalogs read in full and four read by comment extraction rather than in full, nine call-site files read in the ranges cited; comfortable headroom remained throughout, and no compaction occurred.

> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `frontend/src/lib/i18n/messages.da.ts` landed as `b0f8a28`, pushed, readback equal, porcelain clean.
> **ACCEPTED.** Five MEASURED findings and six LEADs, and **L1 corrects a structural claim I asserted as
> fact: I wrote that Danish is verb-final in subordinate clauses. It is not — Mainland Scandinavian lost
> that property, and it is exactly why all four fixed call sites are harmless for Danish while two bit
> German and Dutch.** ⇒ The correct generalization is that the pair bites **verb-final West Germanic**
> (de · nl · af) and nothing else, which changes both remaining prompts in opposite directions.
> ⭐ **AND M2 IS A LIVE PRODUCT DEFECT IN SHIPPED ICELANDIC, not the prospective Danish risk I described.**
> ✔ Verified myself: `Þýska → þyska` and `Sænska → sænska` both leave non-ASCII residue, so no ASCII
> query finds them in the picker. And the trap inside the trap — `EXPLICIT_SEARCH_FOLDS` covers
> `đ` U+0111 LATIN SMALL LETTER D WITH STROKE while Icelandic's letter is `ð` U+00F0 LATIN SMALL LETTER
> ETH, a different codepoint the comment's "D-stroke (đ)" wording would let a repair slice miss entirely.
> ⭐ **M1 also verified and it is a real correction:** `page.tsx:426` is the AI blocker dialog, and
> `game.giveUp.*` render at `:669-671` inside `window.confirm()` — native browser chrome, no CSS width,
> no markup. My prompt called `:426` the give-up dialog for three catalogs running.
> My rulings on all eleven findings are in `./00_notes.md` §47. The report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 15, Worker exchange ordinal: 01
```

**Status:** PASS
**Phase-qualified result:** Implementation complete — MEC-UIL-C6-da, the Danish interface catalog, authored, validated, committed and published.
**Start commit:** `57596e8113f005ed5ebeaf54091d69e57e125022`
**End commit:** `b0f8a2825d42d02b3e5dbafa0b15b616881db341`
**Changed files:** `frontend/src/lib/i18n/messages.da.ts` — NEW, 605 lines, +605/−0, the only path. Exports `daText` (296 text keys) and `daFn` (20 function keys). Deliberately orphaned: `LOCALES` is untouched at four and nothing imports it. Zero existing files modified, moved or deleted.
**Tests and validation:** the structural audit of §7.1 (all eight lines) plus all four frontend gates, below.
**Commit and push:** one non-force commit on `main`; one non-force `git push origin main`; readback equal.
**Deviations / risks / missing evidence:** the recorded §7.2 backend deviation (the five backend gates were not run — the diff is confined to `frontend/`, `pytest` collects only `backend/`, `mypy` scope is `config game gamecore accounts catalog`). Risks under *Flagged risks*.
**Smallest next step:** catalog 7 — Swedish (`messages.sv.ts`), which must be told not to reuse the three Danish items in §5.7 below.
**Report justification:** `new-mutation`
**Authority expiry:** my authority ended at this report. I have not begun a seventh catalog, added a locale, touched the wiring, or written anything into Meta.
**Logical-whole closure:** not-closed
**Context pressure:** moderate — comfortable headroom; the nine reference files and every named call site were read in full without pruning.

**Resolved Execution Issues / Near-Misses**

1. Self-caught before commit: `a11y.dialog.rival` and `chat.unavailable` were first written with a copula (`Modstander er ikke tilgængelig`, `Chat er ikke tilgængelig`), which broke my own verbless-label pattern against the sibling `play.rival.unavailable`. Both were reduced to the label form and all four gates were re-run after the edit.
2. Honest near-miss, uncorrectable: the **commit message body** transliterates `æ ø å` to ASCII in four illustrative Danish words (`Aabn`, `Soeg`, `Vaelg`, `Nuvaerende`). The catalog itself is unaffected — 82 `æ`, 41 `ø`, 25 `å`, 3 `Å` as real UTF-8, zero `ae`/`oe`/`aa` substitutions — but given §5.3's emphasis it reads as sloppy. Fixing it needs `--amend`, which §9 forbids, so I left it and am reporting it instead.

**Pre-Existing Failure Classification:** none. `npx vitest run` emits `[libretiles-provider-failure] openrouter …` lines on stderr; those are intentional fixtures inside passing tests and appear identically in the pre-file baseline.

---

## Gates

| Gate | Result |
|---|---|
| `npm run typecheck` | exit 0, **zero diagnostics** — the completeness proof for all 296 + 20 keys and every interpolation signature. `tsconfig.json` `include` contains `**/*.ts`, verified, so the orphan is checked. |
| `npx vitest run` | **467 passed / 3 skipped** (32 files passed, 1 skipped) — byte-identical to the baseline I measured **before** creating the file. |
| `npm run lint` | exit 0, zero findings. |
| `npm run build` | exit 0. **The build passed**, and it still reports **eleven dynamic routes and zero static**. That is a separate claim from "the code type-checks" above. Port 3000/8000 confirmed free before the build; nothing was killed. |

Structural audit §7.1, all eight lines green: `git status --porcelain=v1` was exactly one `??` line for the new file · header `diff` against `messages.de.ts` EMPTY (and its `sha256` matches de/pt/is/it/nl — six for six now) · `grep -c 'pluralDa('` = 3 · `^[^/]*plural` = one import plus three calls, nothing else · zero `aria-live` / `role="status"` · forbidden-shape grep empty · `git diff --check` clean. No audit pattern fired on correct Danish, so no pattern defect to report from that block.

Additionally, mechanically, not by hand: **key order is identical to `messages.en.ts` in both blocks** (296/296 text, 20/20 fn, positional equality — the check catalog 5 caught itself failing). Zero empty-string values.

---

## Terminology and choices

**The nine frozen terms** (canonical home is the file's terminology block; here once):
`tile` **brik** · `letter` **bogstav** · `rack` **brikholder** · `blank` **joker** · `bag` **pose** · `board` = **bræt** (surface) **and parti** (saved game) · `pass` **pas** · `points` **point** · `rival` = `opponent` **modstander**.

Splits and calls: `bræt`/`parti` splits seven-for-seven with the predecessors, and a third word `spil` stays apart as the game-as-product (hence `Spilvariant`). `pas` and `byt` are different moves. **tile and letter are NOT collapsed** — a `joker` is a `brik` carrying no `bogstav` that becomes one, so the piece and the character need separate words (Italian's and Dutch's call, not Icelandic's).

⭐ **The pass noun EXISTS in Danish**, which breaks the three-catalog streak. Icelandic (`passi` = passport), Italian (`passo` = step) and Dutch (`een pas` = a step) all had to go verbal. Danish game usage says *melde pas*, and `pas` is the settled call in card and board games — so `game.toast.passRejected` is the plain noun `Pas afvist` with no rephrasing. Two knock-ons carried anyway: `et pas` is also a passport (disambiguated by the adjacent `Pas` button), and the verb `passe` also means *to fit*, so `error.conflict` says `strider mod` and never `passer ikke` — the same trap Icelandic reported for `passa`.

**Register:** informal `du / din / dit / dine`, error messages included; never `De / Deres`. **It cost nothing**, exactly as §5.3 anticipated: Danish `De` is genuinely archaic rather than merely formal, so unlike German's `Sie` or Italian's `Lei` there was never a second usable register to weigh.

**Label style:** imperative for every control, action label, column heading and accessible name (`Spil · Pas · Byt · Annuller · Log ud · Åbn · Søg · Send · Vælg · Nulstil`). **They COINCIDE, like Italian — not contrast, like Dutch.** The imperative is both what a Danish button says and what `du`-prose says (`Vælg dit næste parti`, `Prøv igen`), so this catalog never had to choose between an infinitive control form and a bare-stem prose form. I did not manufacture a distinction Danish does not have.
**Pre-authorized exceptions used:** all three — the **pagination pair** (`Forrige`/`Næste`, adjectives of the implied `side`), the **toggle state words** (`Til`/`Fra`), and the **badge words** (`settings.board.active`, `overlay.bestBadge`). No fourth exception was needed, because no fixed call site forced one (contrast Dutch, which needed `board.reset`).

**The six slot fillers — none is a phrase.** All three sites keep **pure nouns**:
- point noun `point / point` — ⭐ **the same word in both slots**: Danish `point` (et point) is invariable in number ("1 point", "5 point", "34 point"). Icelandic `stig` is the precedent; this is the language, not an oversight.
- minute noun `minut / minutter`.
- tile noun `brik / brikker`. **`valgt` does NOT have to sit inside the slot.** The participle already ends in `-t`, so its common and neuter singular forms are identical, and Danish keeps the uninflected form in this verbless label for the plural too — so `valgt` is appended *outside* the helper the way German appends `ausgewählt`. Residual uncertainty flagged below.
`pluralDa` is called, never `pluralEn`. Re-measured on node v26.4.0 / ICU 78.3: CLDR `da` selects `one` for **0.5 and 1.5** while `en` selects `other` for 0.5; **zero** integer divergences over 0..3000; `0→other, 1→one, 2→other, 11→other, 21→other, 1000000→other`. All of §5.1's numbers reproduce.

**`AI` takes COMMON gender `en`**, matching its Danish head noun *(kunstig) intelligens*. ⭐ And this is where Danish differs interestingly from every predecessor: because Danish marks definiteness as a **suffix**, the choice is visible in nearly every AI string rather than only in an article or an elision — the definite form of an abbreviation takes an apostrophe, so it is `AI'en` and its genitive `AI'ens` (`AI'ens betænkningstid`, `AI'en har scoret`). Same rule applied to `GPU'en`. Dutch's `de AI` shows only in a separate word; Italian's shows in `l'`; Danish's is baked into the token.

**Protected tokens — the six prose sites, and the decision is invisible at all six.** `model` is TRANSLATED at `landing.card.ai.body` and `chat` is KEPT at all five of its sites, which matches all five predecessors — but for Danish both words are *native*, so the decision produces no observable difference: `model` (en model) is byte-identical to the token, giving `modelvalg` either way, and `chat` (at chatte, en chat) is the naturalized Danish word, giving `Chatbesked`, `Partichat`, `Chat ikke tilgængelig`, `Chat er offline`. This is the same non-answer Dutch reported, and I am stating it rather than looking as if I skipped the step. Preserved unchanged: `Libre Tiles`, `AI`, `Collins Scrabble Words 2019` and `279.496`, every model id, room code, runtime name, word, status and preview.

### ⭐ The four fixed call sites of §6.5 — ALL FOUR HARMLESS for Danish, per site

I did not inherit either verdict. The two that bit German and Dutch are harmless for Danish for **one shared structural reason, and it is the reason the prompt's premise is wrong**: Danish is Mainland Scandinavian and is **not verb-final in its verb phrase**. (See MEASURED/LEAD below — the premise correction is the single most load-bearing item in this report.)

1. **`game.aiPlayedFor.before` + `.points` — HARMLESS.** Danish places the past participle immediately after the auxiliary and **before** its object, so `AI'en har scoret` + `34` + `point` fits `page.tsx:338`'s fixed `[before] <span>{score}</span> [points]` exactly as written. **The perfect tense survives** — no simple-past fallback, no register downgrade. German (`spielte`) and Dutch (`scoorde`) both had to abandon it because their verb phrase *is* final; that property is West Germanic and Danish does not share it. `game.toast.aiPlayedWord` is kept in the same tense for toast consistency.
2. **`board.reset` + `board.zoomNoun` — HARMLESS.** The Danish imperative takes its object after it, so `Nulstil` + `zoom` is correct in exactly the order the two spans at `Board.tsx:692-693` impose. Dutch found this answer by switching *away* from its infinitive control style for one key; Danish needs no switch at all, because the imperative is already its control form. German's `Reset` loanword was unnecessary here.
3. **`game.aWord` inside `game.toast.aiPlayedWord` — HARMLESS.** ⭐ And the reason ties directly to §5.2: Danish's **indefinite** article is a separate word — only the **definite** article is a suffix — so `et ord` can be carried inside the composed text key without ever touching the interpolated value. `AI'en har spillet et ord` / `AI'en har spillet KAGE`; Danish needs no article before a bare cited word. `ord` is neuter, hence `et`. I join de/pt/it/nl in carrying the article.
4. **`history.open` — HARMLESS.** The imperative `Åbn` (3 characters) works as both the button label at `GameHistoryPanel.tsx:139` and the action-column heading at `:295`. ⚠ **But its alternating partner `history.current` did cost something**, which no predecessor reported: `aktuel`/`aktuelt` inflects for gender and the implied noun in that slot is the **neuter** `parti`, so the agreeing form would have to be `Aktuelt`. I used the participle-derived **`Nuværende`**, which is indeclinable in every gender, number and definiteness. Commented at the key. I did not touch the call site.

### The two orthographic statements of §7.1

- **No common noun and no language name is capitalized outside sentence-initial position.** Stated, and additionally supported mechanically: a scan of all 296 values for non-initial capitals returned **zero** hits outside an explicit allowlist of preserved tokens, brand words, endonyms and the twelve picker rows. Danish sides with Italian and Icelandic on the language-name question and with nobody on the noun question.
- **`æ ø å` are real UTF-8 with no `ae`/`oe`/`aa` substitution anywhere.** Counted: `æ` × 82, `ø` × 41, `å` × 25, `Å` × 3; zero word-boundary `ae`/`oe`/`aa`.

---

## The twelve language names

Capitalization convention, stated per family: **CAPITAL in `settings.gameVariant.*`**, because a picker row is a standalone list item and therefore sentence-initial; **lowercase in `game.lexicon.*`**, because Danish does not capitalize a language word in running text. Italian's and Icelandic's position, not Dutch's. The two families are consistent — the `game.lexicon.*` rows are the same words in their definite adjective form, and Danish's definite/weak adjective is `-e` for **every** gender and number, so agreement with `ordliste` is free.

| slug | `settings.gameVariant.*` | `game.lexicon.*` |
|---|---|---|
| english | Engelsk | *(none — `collins2019`)* |
| slovak | Slovakisk | Ikke i den slovakiske ordliste |
| czech | Tjekkisk | Ikke i den tjekkiske ordliste |
| polish | Polsk | Ikke i den polske ordliste |
| afrikaans | Afrikaans | Ikke i ordlisten for afrikaans |
| italian | Italiensk | Ikke i den italienske ordliste |
| dutch | Nederlandsk | Ikke i den nederlandske ordliste |
| german | Tysk | Ikke i den tyske ordliste |
| portuguese | Portugisisk | Ikke i den portugisiske ordliste |
| danish | Dansk | Ikke i den danske ordliste |
| swedish | Svensk | Ikke i den svenske ordliste |
| icelandic | Islandsk | Ikke i den islandske ordliste |

**Substring-collision set derived from MY strings: ZERO** (case-insensitive, all ordered pairs, twelve names). Confirmed against §5.6's framing that zero is the rule and Icelandic is the campaign's single outlier.
`Afrikaans` is byte-identical to English — Danish has no separate exonym — and is commented as correct, not missing. It is also the one `game.lexicon.*` exception: Danish has no established adjective built on it, so that row carries the bare language name after a preposition rather than an invented `*afrikaanske`. German and Portuguese made the same exception by their own mechanisms.

**⭐ `æ` flag, per §5.5: ZERO.** None of the twelve variant names and none of the four endonyms contains `æ`. I re-ran `foldForSearch` over all **sixteen** picker-searched strings on node v26.4.0 / ICU 78.3: every one folds to plain ASCII, so the measured `æ` gap has **no effect on this catalog's searched surface**. (Independently reproduced §5.5's measurement: `Ø → o` ✔, `Åben → aben` ✔, `Fælles → fælles` ⛔.) `æ` appears in this catalog only in strings the picker never searches (`Vælg`, `Næste`, `Nuværende`, `Bekræft`, `tættere`, `bræt`…). `picker.search` itself is `Søg`, whose `ø` does fold. Nothing in `locales.ts` was touched.

## ⭐ Distinctively Danish forms Swedish must not reuse

1. **The pieces and the bag** — Danish `brik / brikker / brikkerne` and `pose`. Swedish builds both on different stems, and Danish's definite-plural `-ne` is not Swedish's, so a Swedish author who lifts `brik`, `brikkerne` or `pose` produces non-Swedish.
2. **The alphabet** — Danish `æ ø å` against Swedish `å ä ö`. `Vælg`, `Søg`, `Bekræft`, `bræt` and `næste` carry letters a Swedish catalog must not contain at all; `Søg` in particular is the picker's own search label.
3. **Sign-out and the `-lig` trap** — Danish `Log ud` is two short words (6 characters) where Swedish is not, and Danish `tilgængelig / ugyldig / mulig` share their **suffix** with Swedish while differing in the **stem**, so a Swedish author who assumes `-lig` transfers gets the ending right and the word wrong. That is the specific trap, not a general warning.

---

## Flagged risks

**Overflow, reported not shortened (§5.5's limit clause):**
1. `board.pinchToZoom` = `Knib for at zoome` (**17** vs English 13) and `board.dragToPan` = `Træk for at flytte` (**18** vs 11), on the tightest text surface in the product (`Board.tsx:663-680`, `text-[0.72rem] uppercase tracking-[0.18em]`). Shorter Danish exists only by abbreviating meaning away. Dutch reached 18+20+9; Danish is 17+18+5.
2. `board.hide` = `Skjul` (5 vs 4) — negligible, noted for completeness.
3. `header.logout` = **`Log ud`, 6 characters** — ties English and beats every catalog except Italian's 4 (is 7, de 8, nl 9, sk/cs/pl 11, pt 15). Its in-place swap partner `header.loggingOut` = `Logger ud...` at **12** against English's 14, so the non-wrapping cluster *gains* room on both halves of the swap.
4. `overlay.bestBadge` = **`BEDST`, 5 characters** — the shortest form that cannot be read as untranslated English, since Danish spells it with a `d`. Ties `is` and `nl`. `overlay.best` = `Bedste træk` (11) **diverges** from the badge, joining de/is/nl rather than the six that keep one word; both are sanctioned and this is my stated choice.
5. `board.pts` = `point` and `game.aiPlayedFor.points` = `point` are the **SAME** word, joining sk/cs/pl/de/is. Danish does not abbreviate `point` in running UI text and it is already 5 characters. It renders CSS-uppercased at `Board.tsx:652-653` and bare at `AIThinkingOverlay.tsx:113, :314`, so the value stays lowercase.
6. `settings.timeout.120` = `Standardbetænkningstid` (22) and `.300` = `Længste betænkningstid` (22) in the `minmax(170px,1fr)` grid; Italian reached 32 there, so this is inside precedent.

**Where gender, the definite suffix or a call site forced a construction English did not have:**
7. `settings.board.active` = **`I brug`**, an invariable prepositional phrase. See the "trap present" entry below.
8. `history.current` = **`Nuværende`** rather than `Aktuel`/`Aktuelt`. See call site 4.
9. `picker.noMatch` = `Ingen resultater` rather than a literal *no match*: Danish `match` is a **neuter** loan, so the negative determiner would have to be `intet`, and the plural noun phrase avoids committing to it.
10. `game.status.opponentPlaying` = `{name} spiller nu`. The adverb `nu` is load-bearing and is not decoration: bare `spiller` is simultaneously the 3sg present of *spille* and the Danish noun for *a player*, so `{name} spiller` is genuinely ambiguous. The gender/suffix trap itself is absent (see below).

**Strings I am least certain of, in order:**
11. **`brikholder` for `rack`.** I chose it over `brikbakke` (which §5.3 uses as a closed-compound *example*) because `bakke` is a tray and `holder` is what a Danish word-game piece holder is called. If the Cooperator prefers the shorter `brikbakke`, three keys change (`rack.empty`, `history.endReason.bagEmpty`, `game.toast.aiExchangedBody`) plus the terminology block.
12. **`valgt` uninflected in `controls.tilesSelected`.** I assert that Danish keeps the uninflected `-t` participle in this verbless label at plural counts. A reviewer who prefers the fully-inflected predicative plural `valgte` would have to move the participle **inside** the slot, making it a phrase (`brik valgt` / `brikker valgte`) — Icelandic's and Italian's shape. This is the one place my "pure noun" answer to §6.1 could be overturned.
13. **`ordliste` for `lexicon`** (`en ordliste`) rather than the cognate `leksikon`. `ordliste` is what a Danish word-game player says and `leksikon` skews to *encyclopedia*, but it is a deliberate departure from the cognate the other five catalogs used. It also appears in `settings.gameVariant.description`.
14. `a11y.status.turn` = `Turstatus`. `tur` is the turn and `træk` the move (kept apart everywhere), but Danish `tur` also means *trip*, so the compound is mildly ambiguous out of context. `Trækstatus` would be unambiguous and semantically narrower.
15. `settings.premium.description` renders "game header" as `partiets topbjælke`. `header` is also used untranslated in Danish UIs; `topbjælke` is the native word and I preferred it.
16. `history.col.mode` = `Type` and `history.col.score` = `Score` are byte-identical to English. Both are ordinary Danish nouns (*en type*, *en score*) and both are commented as deliberate, but a reviewer skimming will read them as untranslated.

### ⭐ Every §5.2 trap that does NOT bite Danish, with the structural reason

Six of the seven items are **absent**. One is present.

| item | verdict | structural reason |
|---|---|---|
| `settings.board.active` | **PRESENT** | Danish adjectives inflect for gender (`aktiv`/`aktivt`) and the three sibling labels at `settings/page.tsx:218-220` are not one class — `Træ` is a neuter noun while `Sort` and `Grøn` are colour words — and the implied head noun is itself ambiguous between `et bræt` and `en overflade`. Invariable phrase `I brug`, same length as the English. Portuguese and Icelandic needed this; Italian and Dutch did not; Danish does. |
| the eight `history.outcome.*` | **ABSENT, twice over** | (a) `parti` in the row and the column heading `Resultat` are **both NEUTER**, so even an agreeing form would be consistent across the two call sites; (b) every value is a fixed phrase or a past participle in `-t`/`-et`, whose form is identical to the neuter singular and is precisely the unmarked result label a Danish results table uses. |
| `draw.reason.closer` | **ABSENT** | Re-confirmed the values are TILE LETTERS (`draw-result.ts:29-30`). `er` is an invariable third-person verb and `tættere` an invariable `-ere` comparative, so no article, no definite suffix and no agreeing adjective touches either opaque value. |
| `game.status.opponentPlaying` | **ABSENT** | The predicate is a finite verb plus an adverb, so nothing agrees with `{name}` and no definite suffix attaches to it. (The separate `spiller` noun/verb ambiguity is item 10 above, not this trap.) |
| `game.gaveUp` | **ABSENT** | Danish builds its perfect with `have` and **its participle never agrees with anything**, so `har opgivet` needs no gender — the same free pass Dutch got, and the opposite of Italian's reflexive problem. The definite suffix on `partiet` is safe because that noun is fixed at author time, not interpolated. |
| `profile.memberSince` | **ABSENT** | `siden` is a bare preposition that governs its complement with no article, no case and no definite suffix, so `Medlem siden Ukendt` is exactly as awkward as the English original and no more so — pre-existing, not introduced here. |
| `history.unknownDate` | **ABSENT, for a purely morphological reason** | Re-measured the four sites: `GameHistoryPanel.tsx:97` and both uses inside `formatJoinedDate` (`ProfileModal.tsx:23`, `:26`) are DATES; only `ProfileModal.tsx:220` is a USERNAME — three dates, one username. `Ukendt` already ends in `-t`, so its indefinite **common and neuter singular forms are identical**, and one form is correct for both `en dato` and `et brugernavn`. Commented at the key; no fix proposed. |
| `history.outcome.unknown` | **DEAD, confirmed** | `OUTCOME_META` at `GameHistoryPanel.tsx:36-75` has exactly seven arms and no `unknown`. `Ukendt`, zero further agreement effort. |

---

## Orchestration critique

Label definitions, stated so neither list can be read as the other: **MEASURED** = verified in this checkout during this exchange by command or by direct file read. **LEAD** = judgement, hypothesis, or a linguistic assertion that no command in this repository can verify.

### MEASURED

**M1 — the thirty-eighth finding. §5.5's toast line misidentifies the element, and the consequence is real.** It says: *"Two nearby `max-w-md` are NOT toasts: the give-up dialog at `app/game/[id]/page.tsx:426` and the history empty state at `GameHistoryPanel.tsx:269`."* `GameHistoryPanel.tsx:269` is correct. **`page.tsx:426` is not the give-up dialog** — it is the **AI blocker dialog** (`role="dialog" aria-labelledby="ai-blocker-title"`, rendering the `game.blocker.*` family). **There is no styled give-up dialog anywhere in the product**: `game.giveUp.ai` / `game.giveUp.human` are consumed by a native `window.confirm(giveUpMessage)` at `page.tsx:671`, which is their only call site in the whole tree (`grep -rn 'game.giveUp'` returns exactly `:669` and `:670`; `grep -rn 'window.confirm'` returns exactly `:671`). That matters to an author, not just to a map: those two strings render in the browser's own chrome in the OS font with **no CSS width constraint and no markup**, which is a different set of constraints from a `max-w-md` panel. Catalogs 7 and 8 should be given `page.tsx:671` and the `window.confirm` fact instead.

**M2 — the `æ` gap of §5.5 is not prospective. It is already a LIVE defect in shipped Icelandic, and it has a sibling the queued slice will miss.** §5.5 frames the `æ` fold gap as a Danish-facing risk with "nothing for you to do". I folded the sixteen picker-searched strings of **every** shipped catalog and found two already-committed labels with unfoldable residue, both in `messages.is.ts`:
- `settings.gameVariant.german` = `Þýska` → folds to `þyska`. **Thorn has no NFD decomposition and no explicit entry**, so no ASCII query matches it.
- `settings.gameVariant.swedish` = `Sænska` → folds to `sænska`. **The same `æ` gap, live today**, in a locale that shipped five catalogs ago.

And a distinction the queued slice can very easily get wrong: `EXPLICIT_SEARCH_FOLDS` at `locales.ts:24-31` covers **`đ`/`Đ` (U+0111/U+0110, D-STROKE)**, and the comment at `:23` names it as "D-stroke (đ)". It does **not** cover **`ð`/`Ð` (U+00F0/U+00D0, ETH)** — different codepoints, and eth is the Icelandic one. Measured unfoldable today: `æ Æ þ Þ ð Ð ß œ ı`. Of these, `ß` matters for a future German-searched value and `æ þ ð` matter for Icelandic and Danish now. The queued `EXPLICIT_SEARCH_FOLDS` slice should be scoped to all of them, and it should be re-framed as a **defect repair in shipped `is`**, not a Danish precaution.

**M3 — every other cross-catalog number in the prompt reproduces exactly.** I regenerated rather than trusted: `header.logout` (en 6 · it 4 · is 7 · de 8 · nl 9 · sk 11 · cs 11 · pl 11 · pt 15) ✔ · `header.loggingOut` (en 14 · it 9 · de 11 · is 11 · nl 12 · cs 12 · sk 13 · pl 13 · pt 20) ✔ · `overlay.bestBadge` (de 3 · en 4 · is 5 · nl 5 · pt 6 · sk 8 · cs 8 · it 8 · pl 9) ✔ · `board.pts` vs `game.aiPlayedFor.points` identical in sk/cs/pl/de/is and different in en/pt/it/nl ✔ · `overlay.best` vs `overlay.bestBadge` the same **word** in en/sk/cs/pl/pt/it and different in de/is/nl ✔ (they differ as *strings* in all nine, by case; the prompt's phrasing is precise and I checked it case-folded before recording anything) · vitest baseline 467/3 ✔ · `Intl.NumberFormat("da")` = `279.496` ✔ · all twelve `Intl.DisplayNames("da")` exonyms ✔ · zero collisions ✔ · `plural.ts:55-56` and `:67-68` quoted verbatim ✔ · `GLOSSARY.md` 555 lines ✔ · `OUTCOME_META` seven arms ✔ · four `history.unknownDate` sites 3-dates/1-username ✔ · `Board.tsx` `:669 :671 :677 :692 :693` ✔ · `ScorePanel.tsx:208-242` + `:346` in-place swap ✔ + `min-w-[4.8rem] sm:min-w-[5.1rem]` at `:382`/`:395` ✔ · `settings/page.tsx:218-220` ✔ · `GameHistoryPanel.tsx:139`/`:295` ✔ · `PremiumPicker.tsx:31, :239, :301` ✔ · `i18n.test.ts:495-505` ✔ · `tsconfig` `**/*.ts` ✔ · 12 variant manifests ✔ · header `sha256` identical across de/pt/is/it/nl ✔ · the Next.js doc's title-cased `Winkelwagen` at line 116 ✔ (read for the rule, ignored for style). §5.5's "every number here was regenerated today" holds up under re-derivation.

**M4 — the predecessor files carry their required comments.** All five have an endonym note and an Afrikaans note; no missing-comment defect of the kind catalog 2 found in catalog 1. I have nothing to report against catalogs 1-5's own text.

**M5 — a documentation gap in `GLOSSARY.md`, pre-existing and outside my allowlist.** Its "Settings panels in this slice" table lists **ten** `settings.gameVariant.*` rows (english, slovak, afrikaans, italian, dutch, german, portuguese, danish, swedish, icelandic) and omits **czech** and **polish**, which `messages.en.ts` and every catalog do have. `messages.en.ts` is the type source so nothing is broken, but a catalog author who works from the GLOSSARY table would produce ten names and be caught only by `tsc`. Cheap to fix in whatever slice next touches the GLOSSARY.

### LEAD

**L1 — the prompt's structural premise for Danish is wrong, and this is the single most load-bearing item in this report. High confidence; not command-verifiable here.** §6.5 and the Named-decision-risk block both assert *"DANISH IS V2 WITH VERB-FINAL SUBORDINATE ORDER"* and that *"Danish `har … scoret` has the same shape as both [German and Dutch]"*. **Verb-final subordinate order is a continental West Germanic property that Mainland Scandinavian lost.** Danish is V2 in main clauses and **SVO in subordinate clauses too** — the only systematic main/subordinate difference is adverb placement, not verb position — and in the perfect the participle stands **immediately after the auxiliary, before its object** (`AI'en har scoret 34 point`, and `…at AI'en har scoret 34 point`). That is why both of the sites that bit German and Dutch are harmless here, and why Danish keeps the perfect tense where German fell to `spielte` and Dutch to `scoorde`. The *measurable* half of the prompt's claim is correct and I verified it (de and nl both use the simple past at that key); the *inference* from it to Danish is not. **Consequence for the two remaining prompts:** Swedish (catalog 7) inherits the same non-verb-final property, so its prompt should carry the corrected premise — otherwise catalog 7 will be told to expect a trap that cannot bite it and may "solve" it by abandoning the perfect for no reason. Afrikaans (catalog 8) is the opposite case: it *is* West Germanic and verb-final in subordinate clauses, like Dutch and German, so catalog 8's prompt should expect **both** sites to bite and should be pointed at Dutch's `scoorde`/`Herstel zoom` answers as the likely shape. The clean generalisation for the skeleton: **this pair of call sites bites exactly the verb-final West Germanic languages (de, nl, af) and no other**, which after catalog 8 will be a five-language sample with a mechanism rather than a majority vote.

**L2 — §5.2's "TWO KNOWN `messages.en.ts` SHAPE PROBLEMS" should become three, and the third is the one nobody has been told about.** Five catalogs have now met `history.unknownDate` and `history.outcome.unknown`. There is a third of the same class: `game.aiPlayedFor.before` + `.points` is **a sentence split across two keys with an un-reorderable span between them** — that is a *shape* problem, not a translation problem, and it has already forced two of six catalogs into a tense they did not want. Listing it as a third known-and-queued shape problem would stop catalogs 7 and 8 from re-deriving the analysis and would let the eventual fix (one interpolated function key taking `{score}`) be scoped once. I am not proposing the fix and I did not touch the call site.

**L3 — one [VARIANT] item should have been [INVARIANT].** §5.5's Danish-specific "LAYOUT RISK IS MEDIUM / choose the shortest idiomatic term where alternatives are equivalent, but never abbreviate meaning away" is written per-language, and it has now been restated in some form for de, is, it, nl and da. It is a campaign ruling, not a Danish fact. Promoting it to [INVARIANT] and leaving only the one-line risk *grade* in [VARIANT] would shorten the last two prompts without losing anything.

**L4 — the skeleton is missing an instruction sv and af will both need: what to do when a key's value comes out byte-identical to English.** I hit six (`Libre Tiles`, `AI`, `Afrikaans`, `Send`, `Type`, `Score`, plus near-identical `Chat er offline`), and §4 forbids "an English value as a placeholder (except 6.4's deliberate cases)" without saying how a reviewer is to tell a legitimate coincidence from a skipped key. I resolved it by commenting every one, which is what §4's "one line at any row that breaks your own pattern" implies but does not say. Swedish will hit more of these than Danish did (`Chat`, `Send`, `Type`, `Score`, `Premium`, `AI`), and Afrikaans will hit substantially more still because of its lexical overlap with English. A one-line [INVARIANT] rule — *a value byte-identical to English is permitted only when it is genuinely the correct native form, and must carry a comment saying so* — would remove the ambiguity.

**L5 — a wording risk in §5.4 worth one clause.** *"⚠ ONE EXPECTED COLLAPSE: `rival` and `opponent` are the same person. Six for six used one word."* Six-for-six is now seven-for-seven (`modstander`), but the number is doing the same work the invalid three-agreeing-catalogs inference did in §6.5: it invites the next author to treat the collapse as settled rather than checked. Swedish and Afrikaans both plausibly have two words available. Recommend phrasing it as *"seven for seven so far — verify for your language and say so"*, matching the framing §5.2 already uses correctly.

**L6 — confidence, stated unevenly on purpose.** Highest: the four call-site verdicts, the `point`-invariance ruling, the `ukendt`/`nuværende`/`I brug` agreement reasoning, and L1. Lower: `brikholder` vs `brikbakke`, `ordliste` vs `leksikon`, `Turstatus`, and the uninflected `valgt` at plural counts (items 11-14 above). I would not want any of those four treated as measured.

**Not stopping conditions, so I continued:** M1, M2 and L1 are prompt/repository disagreements recorded here rather than acted on. No file outside the one-path allowlist was read for guidance, modified, or proposed for modification. No `.ap` operation, no forbidden git operation, no dependency change, no network access beyond the two authorized git commands, no secret read.

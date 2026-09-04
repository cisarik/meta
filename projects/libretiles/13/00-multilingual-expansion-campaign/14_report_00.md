> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `frontend/src/lib/i18n/messages.nl.ts` landed as `57596e8`, pushed, readback equal, porcelain clean.
> **ACCEPTED.** Seven MEASURED findings and seven LEADs — the strongest of the five, and **five of the
> seven MEASURED are counting errors in claims I made without counting.** ✔ All verified: the badge
> lengths are `{3,5,6,8}` not `{3,5,8,8}`; German not Italian was the first zero-collision catalog and
> eight of nine shipped catalogs have zero; the `board.pts` divergence precedent is one not two; all
> FOUR predecessors kept `chat`, not three; and I omitted German — the only Germanic comparator — from
> the `header.logout` list.
> ⭐ **AND THE LOAD-BEARING PRODUCT FINDING INVERTS A CONCLUSION I WAS ABOUT TO DRAW:** two of the four
> fixed call sites BIT Dutch, the same two that bit German, for the same verb-final reason. Three
> Romance/Insular languages reporting all-harmless was not evidence the call sites are safe — it was
> evidence they are safe for languages that do not put the verb last.
> ⛔ **AND ONE OF ITS MEASURED CLAIMS IS WRONG, the first Worker claim I have had to correct in this
> campaign:** M6 says the `^[^/]*` exclusion would not have caught the ligature in a comment. ✔ Measured:
> plain `grep -c` = 1, and `grep -cE '^[^/]*(ĳ|Ĳ)'` = **0**. The exclusion keys on the LINE's start, and
> that line starts with `//`. Its conclusion stands on its other ground; the reason does not.
> My rulings on all fourteen findings are in `./00_notes.md` §46. The report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 14, Worker exchange ordinal: 01
```

**Status:** PASS
**Phase-qualified result:** Implementation complete — MEC-UIL-C5-nl, the Dutch interface catalog, one new orphaned file, committed and published.
**Start commit:** `6bf7c5e70cf82a32ab45db945019a7f42f039c42` · **End commit:** `57596e8113f005ed5ebeaf54091d69e57e125022`
**Changed files:** `frontend/src/lib/i18n/messages.nl.ts` (NEW, 562 lines, the only path) — 296 text keys and 20 function keys in `messages.en.ts` key order, deliberately orphaned. `LOCALES` untouched at four; nothing imports it.

**Tests and validation.** Repository gate: all six values matched (`HEAD`, `HEAD:.ap` = `git -C .ap rev-parse HEAD` = `9c5cc44`, `## main...origin/main`, empty porcelain, remote at baseline), no listener on 3000/8000. Structural audit of 7.1, all seven lines: porcelain exactly one `?? ` line; the seven-line header `diff` against `messages.de.ts` EMPTY; `grep -c 'pluralNl('` = 3; `^[^/]*plural` = 4 lines (one import, three calls, nothing else); zero `aria-live` / `role="status"`; zero cast/`Partial<`/`?:`/spread/TODO shapes after `tail -n +8`; `git diff --check` clean. Four frontend gates: `npm run typecheck` clean; `npx vitest run` 467 passed / 3 skipped (470) across 32 files + 1 skipped, byte-identical to the baseline measured **before** the file existed; `npm run lint` clean; `npm run build` succeeded. Both build claims stated separately: the build's own TypeScript stage reported `Finished TypeScript in 1665ms`, and the route table is unchanged at **eleven dynamic routes and zero static**. I additionally verified key order and count mechanically against `messages.en.ts` — 296/296 text and 20/20 fn, order identical.

**Commit and push.** One commit `57596e8` on `main`, non-force, staged with the exact path only. Pre-push gate: `git rev-parse HEAD~1` = `6bf7c5e70cf82a32ab45db945019a7f42f039c42` and `git ls-remote origin refs/heads/main` still equalled it. One `git push origin main`. Readback: local HEAD `57596e8113f005ed5ebeaf54091d69e57e125022`, remote `refs/heads/main` `57596e8113f005ed5ebeaf54091d69e57e125022` — equal. Working tree clean; `.ap` untouched.

**Deviations, risks, missing evidence.** One recorded deviation: the five backend gates were not run (diff confined to `frontend/`, pytest collects only `backend/`, mypy scope is `config game gamecore accounts catalog`). No missing evidence. Not independent, and I do not describe it as such.

**Resolved Execution Issues / Near-Misses:** one. I first wrote `history.loading` before `history.refresh`, inverting `messages.en.ts` order; caught by my own key-order diff against `messages.en.ts` and corrected before any gate ran. `typecheck` would not have caught it — order is a §4 requirement, not a type.

**Pre-Existing Failure Classification:** none.

---

## Terminology and choices

**The nine frozen terms** (canonical home is the file's terminology block; stated once here): tile **tegel** (de) · letter **letter** (de) · rack **letterbak** (de) · blank **joker** (de) · bag **zak** (de) · board = **bord** (het, the playing surface) AND **partij** (de, the saved-game metonym) · pass **passen** (verb, and its own verbal noun) · points **punten** (het punt), abbreviated **ptn** · rival = opponent **tegenstander** (de), one word for both. Exchange is **ruilen**, a different word from `passen`. A third word stays apart from both halves of the board split: **spel** is the game as a product or ruleset, which is why the picker says `Spelvariant` and never `Partijvariant`.

Two split decisions with reasons: tile and letter are **not** collapsed (Icelandic collapsed, Italian did not) — a `joker` is a tegel carrying no letter that becomes one, so the piece and the character need separate words. And `tegel` rather than `steen`: `steen` is real Dutch but is the exact cognate of catalog 1's frozen German `Stein`, and D6 forbids harmonizing terminology across languages.

**The pass-noun warning fired, and Dutch escapes it by a third route.** Dutch `een pas` is a step or a pass card, so there is no usable noun — the same gap Icelandic (`passi`, passport) and Italian (`passo`, step) hit. But Dutch needed **no** verbal rephrasing, because the infinitive *is* the verbal noun: `game.toast.passRejected` reads "Passen geweigerd" and keeps the English noun shape. Two predecessors rephrased; Dutch neither coins nor rephrases.

**Register:** informal `je` / `jij` / `jouw` throughout, error messages included; never `u` / `uw`, never mixed. `jij` and `jouw` only where they carry contrast ("Jij begint", "Jouw joker wint de trekking", `draw.side.you`, `chat.you`).

**Label style, and the coincide/contrast answer.** INFINITIVE for every control, action label, column heading and accessible name (Spelen · Passen · Ruilen · Annuleren · Uitloggen · Openen · Zoeken · Verzenden · Sluiten); the `je` IMPERATIVE only for prose, hero headings and on-board instructions (Kies je volgende partij, Controleer de ingevulde gegevens, Knijp om te zoomen). Never mixed inside one strip. **In Dutch the two CONTRAST — they do not coincide as they did in Italian.** The conventional Dutch control form is the infinitive (Annuleren, Opslaan, Vernieuwen) while the informal prose imperative is the bare stem (Kies, Controleer, Probeer): two different forms, so this catalog had to choose rather than have the requirement satisfied for free. The prompt's guess that the bare stem might be both was wrong for the control half. Local corroboration from the mandated Next.js reading: its own Dutch dictionary example is `"cart": "Toevoegen aan Winkelwagen"` — infinitive.

**Pre-authorized exceptions used:** the PAGINATION PAIR (`history.prev` / `history.next` = "Vorige" / "Volgende", adjectives of the implied `pagina`), the TOGGLE STATE WORDS (`settings.toggle.on` / `.off` = "Aan" / "Uit"), and the BADGE WORDS (`settings.board.active` = "Actief", `overlay.bestBadge`). One further exception is **not** pre-authorized and is forced by a fixed call site: `board.reset` (below).

**The six slot fillers, and none is a phrase:** `punt` / `punten` · `minuut` / `minuten` · `tegel` / `tegels`. A Dutch predicate participle is invariable, so `geselecteerd` is appended **outside** the helper the way German appends `ausgewählt`, and the tile slot stays a bare noun. Dutch needs neither Icelandic's `stafur valinn` / `stafir valdir` nor Italian's `tessera selezionata` / `tessere selezionate`. `pluralNl` is called at all three sites and `pluralEn` nowhere.

**`de AI`, not `het AI`.** Its Dutch head noun `(kunstmatige) intelligentie` is a de-word, and Dutch assigns `de` to loan acronyms by default. A structural difference from the four predecessors: German, Portuguese, Icelandic and Italian all chose feminine and their choice is visible in agreeing participles (`dichiarata vincitrice`, `úrskurðuð`); Dutch has **no** gender agreement on predicate nouns or participles, so the choice is visible only in the article itself — "De AI wordt tot winnaar uitgeroepen."

**Protected tokens — and for Dutch the decision is unobservable at all six sites.** `model` at `landing.card.ai.body` is TRANSLATED, and the translation is byte-identical to the token: the ordinary Dutch noun is `model` (het model), so "modelkeuze" is simultaneously translated and untranslated. All five `chat` sites KEEP the English token, which is likewise the naturalized Dutch word (de chat, chatten): `a11y.chatInput` "Chatbericht", `chat.title` "Partijchat", `chat.unavailable` "Chat niet beschikbaar", `game.toast.chatOffline` "Chat is offline" (byte-identical to English and correct Dutch), `landing.card.queue.body` "…en chat". Every occurrence is either string-initial or inside a closed compound, so no mid-sentence capital appears.

**The four fixed call sites of 6.5 — TWO harmless, TWO bit Dutch, and they are the same two that bit German.**

- `game.aiPlayedFor.before` + `.points` — **BITES.** `page.tsx:338` fixes the score span in the middle with nothing after the counted noun, and the Dutch perfect puts its participle at the clause end ("De AI heeft 34 punten gescoord"), which those two spans cannot express. Answer: the **simple past**, "De AI scoorde" + score + "punten" — German's answer, reached independently for the same word-order reason. It costs Dutch **less**, though: `scoorde` is fully idiomatic in written Dutch, whereas German's `spielte` is a register downgrade from the spoken perfect. Knock-on: `game.toast.aiPlayedWord` is held in the same tense ("De AI speelde {word}") because both render in the one `ai_played` toast.
- `board.reset` + `board.zoomNoun` — **BITES.** Dutch, like German, puts the object *before* an infinitive ("Zoom herstellen"), which the fixed `[action][noun]` order at `Board.tsx:692-693` cannot express. Dutch has a better answer than German's loanword `Reset`: the **imperative** takes its object after it, so "Herstel zoom" is correct Dutch in exactly the order the spans impose. This is the one control in the catalog that is not an infinitive, and the call site is the whole reason.
- `game.aWord` inside `game.toast.aiPlayedWord` — **harmless.** The indefinite article is carried here ("een woord"), as German, Portuguese and Italian did; Dutch needs no article before a bare cited word, so "De AI speelde KAAS" and "De AI speelde een woord" both read correctly.
- `history.open` — **harmless.** The infinitive "Openen" works as both a column heading (`:295`) and a button (`:139`), and `Huidige` is uninflected in that slot.

⇒ The load-bearing answer: **a second West Germanic language needs a workaround at exactly the two sites German needed one, for exactly the same reason.** Three Romance/Insular predecessors reporting all four harmless was not evidence that the sites are safe — it was evidence that they are safe *for languages that do not put the verb last*. Both keys are commented in the file.

**The two orthographic statements of 7.1, stated rather than grepped.**
1. **No common noun is capitalized outside sentence-initial position.** I verified this by enumerating every mid-string capitalized token across all 296 values: the only ones are the preserved tokens (`AI`, `AI-tegenstander`, `GPU`, `Libre Tiles`, `Collins Scrabble Words 2019`), the letter `A` as the draw target, the deliberate all-caps `NIEUWE` mirroring English's `NEW`, the eleven **nationality adjectives** (`Nederlandse`, `Duitse`, `IJslandse`, …) which Dutch capitalizes by rule, and words that follow a `.` or `?` inside the same string. `tegel`, `bord`, `zak`, `letter`, `letterbak`, `joker`, `partij`, `beurt`, `zet`, `punten` are lowercase everywhere they are not string-initial. Dutch is not German here.
2. **The file contains no `ĳ` / `Ĳ` ligature in any string value.** `ij` is always two plain letters and `IJ` capitalizes both (`IJslands`, `IJslandse`, `het IJslandse lexicon`).

**Both halves of the German-adjacency rule, and I confirm I got both.** German capitalizes every noun and Dutch does not — so I diverge from `messages.de.ts` on exactly the axis it is most tempting to copy. But Dutch **does** capitalize language names and nationality adjectives, which German also does and Italian and Icelandic do not — so I agree with `messages.de.ts` there. And one consequence the prompt did not spell out: because the capital is a property of the word and not of the position, Dutch keeps it in **running text too**, so `settings.gameVariant.dutch` = "Nederlands" and `game.lexicon.dutch` = "Niet in het Nederlandse lexicon" both carry it. Italian and Icelandic had to switch case between the picker row and the running-text family; Dutch does not. That answers 5.6's last question: the convention does **not** differ between the two surfaces in Dutch, and I used the capital in both.

## The twelve language names

Values as committed, from `settings.gameVariant.*`, with the collision set derived from these strings and not from the prompt's:

| slug | label |
|---|---|
| english | Engels |
| slovak | Slowaaks |
| czech | Tsjechisch |
| polish | Pools |
| afrikaans | Afrikaans |
| italian | Italiaans |
| dutch | Nederlands |
| german | Duits |
| portuguese | Portugees |
| danish | Deens |
| swedish | Zweeds |
| icelandic | IJslands |

**Case-insensitive substring collisions, computed exhaustively over these twelve: ZERO.** No label contains another label. `IJslands` capitalizes **both** letters of the digraph — `Ijslands` would be a spelling error and, as the prompt notes, the one row a Dutch reader spots instantly. `Afrikaans` is byte-identical to English because Dutch has no separate exonym; commented in the file as correct rather than missing. The eleven `game.lexicon.*` adjectives are these same words plus `-e` (`Portugees` → `Portugese`, `Zweeds` → `Zweedse`, `IJslands` → `IJlandse`… committed as `IJslandse`), so the two families stay consistent for free with no case change and, unlike German, Afrikaans needs no exception.

## Flagged risks

Nineteen items.

**Overflow — the compound pressure, and it is real but bounded.**
1. `board.pinchToZoom` "Knijp om te zoomen" — 18 chars against English 13, on the tightest text surface in the product (`Board.tsx:663-680`, `text-[0.72rem] tracking-[0.18em]`). Kept correct.
2. `board.dragToPan` "Sleep om te schuiven" — 20 against 11, in the same pill. Comparable to Italian's 21, which already made that pill grow in height. Expect the same.
3. `board.hide` "Verbergen" — 9 against 4, same pill, third element. Items 1–3 compound: the pill carries all three plus a separator.
4. `header.logout` "Uitloggen" — **9 characters**, against English 6, Italian 4, Icelandic 7, pt-PT 15. A present but mild risk in the non-wrapping cluster. "Afmelden" (8) was the alternative; the everyday informal word was chosen to match the `je` register.
5. `header.loggingOut` "Uitloggen..." — 12 against 14. The bare-infinitive-plus-ellipsis pattern was chosen for progress states precisely so this key would not become "Bezig met uitloggen..." (22) and blow the cluster.
6. `header.backToBoards` "Terug naar partijen" — 19 against 14, but this reaches only an `aria-label` and a nowrap tooltip beside an icon-only button, so it is low concern.
7. `controls.cancel` "Annuleren" — 9 against 6, inside the mobile three-column nowrap grid. `controls.play` / `.pass` / `.exchange` are all 6, at or below the English maximum of 8, so the strip is net no worse than English.
8. `settings.premium.description` and `settings.warn.accountSync` / `.rivalRepair` are long, but all three are wrapping prose panels, not constrained surfaces.
9. `game.lexicon.*` runs 27–32 chars against English's 24–26 because Dutch needs `het …-e lexicon` where English needs `the … lexicon`. Rendered in a wrapping toast, so noted rather than feared.
10. `history.col.rival` "Tegenstander" — 12 against 5. Explicitly **not** a risk: 5.5 records that the history table is `min-w-full` with plain `px-4 py-3` headers, so long headings wrap. I did not shorten it.

**`de`/`het` and inflection forcing constructions English does not have.**
11. Every attributive adjective had to be resolved from the noun's gender class: `Interactief amberkleurig licht` (het licht, indefinite neuter singular ⇒ **uninflected**) beside `Bewegende glans` (de glans ⇒ `-e`), `Klassiek notenhout` and `Donker toernooivilt` (both het ⇒ uninflected) beside `Glanzende nachtlak` and `Lagere GPU-belasting` (both de ⇒ `-e`). English has no analogue of this decision; it is invisible in the diff and is the likeliest place a native reviewer will find an error.
12. `game.toast.invalidWordHeading` — the **adjective** changes as well as the noun: "Ongeldig woord!" (indefinite neuter singular, uninflected) vs "Ongeldige woorden!" (plural, `-e`). Two full forms, never a suffix trick.
13. `board.reset` = "Herstel" is an imperative inside an otherwise fully infinitive control set — a deliberate, commented inconsistency forced by the fixed span order (see 6.5 above). It is the one place a reviewer will legitimately ask why the style broke.
14. `auth.heading.login` and `auth.tab.login` are both "Inloggen": Dutch sentence case collapses English's "Sign in" / "Sign In" pair into one string. Commented as deliberate rather than an oversight.

**Terminology I am least sure of, ranked.**
15. `letterbak` for the rack. "letterbakje", "letterrekje", "standaard" and "plankje" all occur in Dutch Scrabble usage; `letterbak` is the prompt's own compound example and the shortest of the closed-compound options, but a native reviewer may prefer the diminutive `letterbakje`.
16. `tegel` for the tile. Defensible (it is the direct translation, it matches the product name, and it avoids calquing German `Stein`), but Dutch Scrabble players more often say `letter`, `steen` or `blokje` — and `letter` was unavailable because the letter/tile split is mandated.
17. `joker` for the blank. `blanco` is the other live candidate and may be the more official Dutch Scrabble term; `joker` was chosen because it is a single de-noun that works as a caption, a label and a prose noun with no article or inflection decision.
18. `openingstrekking` for the starting draw is a coined-but-transparent compound. I could not verify it against Dutch board-game usage without network access, which is forbidden.
19. `Partijchat` for `chat.title` "Game Chat". A well-formed Dutch compound, but "Chat van de partij" is plainer; the compound was chosen for the closed-compound rule and for length.

**Traps in 5.2 that turned out NOT to bite Dutch — all five of them, each with the structural reason.**
- `settings.board.active`: **does not bite.** The badge is a *sibling* span of the surface name at `settings/page.tsx:218-220`, never attributive to it, and a Dutch predicate or standalone adjective has exactly **one** form. So `Actief` is already invariable and stays correct beside the noun `Hout` (het) and the adjectives `Zwart` and `Groen` alike. Unlike Portuguese and Icelandic I needed no invariable phrase, and unlike Italian I did not need all three surface names to happen to share a gender — Dutch is immune for a stronger reason than Italian was.
- The eight `history.outcome.*`: **do not bite.** Every value is a noun or a predicate participle (`Gewonnen`, `Verloren`, `Opgegeven`, `Verlaten`, `Gelijkspel`, `Bezig`, `Wachten`), and a Dutch predicate participle is invariable, so none agrees with `partij` (de) in the row or `Resultaat` (het) in the header. That is also what a Dutch results table actually says, so correctness cost nothing in idiom.
- `draw.reason.closer`: **does not bite.** `ligt` is an invariable third person and `dichter` an invariable comparative, so the two opaque tile letters need no article and nothing agrees with them.
- `game.status.opponentPlaying`: **does not bite.** "{name} is aan zet" — an invariable predicate, and the idiomatic Dutch board-game phrase besides.
- `game.gaveUp`: **does not bite,** and this is the sharpest negative. Dutch builds its perfect exactly as German does, but a Dutch participle **never** agrees with anything, so `hebben` + `opgegeven` needs no gender. Italian had to abandon the reflexive for `avere` + invariable object; Dutch gets the natural construction for free. Note the asymmetry with 6.5: Dutch's perfect *is* the problem at `game.aiPlayedFor` (word order) and is *not* a problem here (agreement) — the same tense, two different traps, one fires and one does not.
- `profile.memberSince`: **does not bite structurally.** Dutch has no obligatory preposition-plus-article form, so `sinds` governs a real date and the `history.unknownDate` fallback equally. "Lid sinds Onbekend" is exactly as awkward as the English original and no more so — pre-existing, not introduced, and not proposed for a fix.
- `history.unknownDate`: **does not bite, twice over.** Measured at the four call sites the prompt names: `GameHistoryPanel.tsx:97` and both uses inside `formatJoinedDate` (`ProfileModal.tsx:23`, `:26`) are dates; only `ProfileModal.tsx:220` is a username. Dutch escapes both because `de datum` and `de gebruikersnaam` share a gender class **and** because a standalone Dutch adjective is uninflected anyway. Dutch is the first of the five targets where the two referents do not even differ. `Onbekend` serves both; the key is commented.
- `history.outcome.unknown`: dead as documented — `OUTCOME_META` at `GameHistoryPanel.tsx:36-75` has exactly seven arms, verified. Written correctly, no agreement effort spent, commented as dead.

## Orchestration critique

### MEASURED

**M1 — 5.5's `overlay.bestBadge` length list is wrong, and this is my candidate for the thirty-first finding.** The prompt states "the four shipped catalogs chose 3, 5, 8 and 8 characters". Measured from the committed files: de `TOP` = **3**, is `BESTI` = **5**, pt `MELHOR` = **6**, it `MIGLIORE` = **8**. The true multiset is `{3, 5, 6, 8}`. There is no `8 and 8` pair, `6` is absent, and only one catalog reached 8. This matters because the RULING immediately after it ("take the SHORTEST FORM THAT IS NOT MISTAKABLE FOR UNTRANSLATED ENGLISH, and REPORT ITS LENGTH") is calibrated against a spread the reader is told is `3–8` with a mode at 8; the real distribution is flatter and centred lower. Three catalogs still read this line. Correct it to `3, 5, 6 and 8` for da · sv · af. (For the record, English is 4 and mine is 5.)

**M2 — 5.6's "Dutch is the second target language with none" is wrong; Dutch is the fourth.** I computed the collision set for every shipped catalog. de: **0**. pt: **0**. is: **2** (`enska` ⊂ `hollenska`, `enska` ⊂ `íslenska`). it: **0**. en: 0. sk: 0. So three of the four targets already had zero, and **German — catalog 1 — was the first**, not Italian. The prompt's framing ("A USEFUL NEGATIVE RESULT", "Italian was the first") presents a zero-collision set as the exception when it is the rule and Icelandic is the single outlier. The mechanism is still right and I still re-derived it from my own strings; only the rarity claim is wrong. Fix before the af prompt, where the same sentence would otherwise mislead again.

**M3 — 5.5's `board.pts` / `game.aiPlayedFor.points` precedent count is one, not two.** The prompt says "German and Icelandic used one form for both; Portuguese and Italian used two." de `Pkt.`/`Pkt.` and is `stig`/`stig` are one form each ✓. But **pt is `PTS` / `pts` — the same abbreviation in different case, byte-for-byte the English source pair**, and `board.pts` renders under a CSS `uppercase` class at `Board.tsx:652-653` while both AI-overlay sites (`AIThinkingOverlay.tsx:113` and `:314`) have no uppercase class, so pt's two values render identically at every site. **Italian is the only predecessor that used two genuinely different words.** The ruling is sound; the evidence behind it is half as strong as stated. Dutch is the second real precedent (`ptn` / `punten`).

**M4 — 6.4's `chat` precedent omits catalog 1, and the omission reads as a divergence.** The prompt says "All four predecessors translated `model`; Portuguese, Icelandic and Italian kept all five `chat` sites." Measured: **all four** kept all five, German included (`Chat-Nachricht`, `Partie-Chat`, `Chat nicht verfügbar`, `Chat ist offline`, `Echtzeit-Sync und Chat`). Putting "four" next to "three" in one sentence implies German went the other way on chat. It did not. Say "all four" twice.

**M5 — 5.5's `header.logout` comparison skips the only Germanic predecessor.** The list gives en 6, pt-PT 15, is 7, it 4 — and omits de `Abmelden` = **8**, which is the closest comparator for nl (9), da and sv. It also folds English, the source, into a list described as language-specific catalog risk. For three remaining Germanic-ish catalogs the German data point is the useful one; add it.

**M6 — 7.1's decision to make the two Dutch orthographic properties *statements* rather than greps was load-bearing, and I can prove it fired.** My file contains exactly **one** `ĳ` and **one** `Ĳ`, both on comment lines, zero in any string value — because §4 *mandates* an orthography comment block and 5.3 *mandates* naming the forbidden ligature in order to forbid it. A naive `grep -n 'ĳ\|Ĳ'` therefore reports two hits on a fully compliant file. This is the fifth-defect pattern ("an audit pattern aimed at code must not be runnable against the file's own mandated commentary") recurring in a *new* place, and note that the `^[^/]*` exclusion would **not** have saved it, because the ligature is inside prose rather than at a line start. The Orchestrator's own deletion of the per-language grep pre-empted it. Keep the statement form for da · sv · af; do not let a later slice add a ligature grep without a comment exclusion.

**M7 — everything else I checked confirmed.** The seven-line header is byte-identical across de, pt, is, it and nl (verified by hash, not by eye). `Intl.DisplayNames("nl")` on node v26.4.0 / ICU 78.3 returns the twelve exonyms exactly as 5.6 lists them. `Intl.NumberFormat("nl")` yields `279.496` — a period. CLDR nl: `0 → other, 1 → one, 2 → other, 11 → other, 21 → other, 1000000 → other`, two categories, matching 5.1. `foldForSearch` gives `geëindigd → geeindigd`, `IJsland → ijsland`, `IJslands → ijslands`, and `ĳs → ĳs` — the ligature is genuinely unfoldable, so 5.3's second reason is real. `i18n.test.ts:495-506` does walk every non-test `.ts`/`.tsx` under `frontend/src` and does read my file. `OUTCOME_META` has seven arms. `history.unknownDate`'s four call sites are three dates and one username as stated. `draw-result.ts:29-30` passes tile letters. `page.tsx:338` and `:1003` compose as described. `board.reset` / `board.zoomNoun` occur at exactly one call site, `Board.tsx:692-693`. Italian's 21-char `dragToPan` and 32-char `settings.steps.50` are exact. `settings.board.active`'s three Italian siblings are all masculine as Italian's own comment claims. No test references `board.pts` or `aiPlayedFor`. `ScorePanel.tsx:346` is the `label` prop of the logout control whose `whitespace-nowrap shrink-0` lives on the shared `HeaderMiniButton` at `:208-242` — the substance holds, the line number points at the configuration rather than the class.

### LEAD

**L1 — the af prompt needs its own 5.3, and `messages.nl.ts` is now the trap.** Afrikaans and Dutch are by far the closest pair in the set — closer than de/nl, which this prompt treated as the campaign's named risk. The af author will be able to read my file and produce something that *looks* right and is wrong in ways a non-speaker cannot see: Dutch `je` / `jou` / `jouw` vs Afrikaans `jy` / `jou` / `jou`; Dutch single negation vs the obligatory Afrikaans `nie … nie` bracket; Dutch finite verb endings (`ik speel` / `wij spelen`) vs the invariant Afrikaans verb; Dutch `ij` vs Afrikaans `y`; Dutch `-lijk` vs Afrikaans `-lik`; Dutch `z-` vs Afrikaans `s-`. I recommend the af prompt name `messages.nl.ts` as required reading *for shape only* with a mitigation section at least as strong as this one's 5.3, and that it be sequenced as far from this exchange as the campaign allows. This is a prediction, not a measurement — I have not read the af manifest.

**L2 — 5.1's headline "the simplest of the eight, and that is the finding" is shared by four languages, so it belongs in [INVARIANT].** nl, af, da and sv all have the two-slot `i === 1` rule with zero integer divergences from English (`plural.ts:40-64` gives them five separate bodies for exactly that reason). Three more prompts will each present the same fact as a per-language discovery. Move the shape statement, the "do not alias `pluralEn`" warning and the fraction rationale to [INVARIANT], and leave only the per-language *reason the helper exists separately* in [VARIANT]. Related: the Danish note in `plural.ts:32-35` and GLOSSARY D7 (CLDR da selects `one` for 0.5) is the one place where the four genuinely differ, and the da prompt should carry it explicitly.

**L3 — 6.4's protected-token instruction assumes translate-vs-keep is observable, and for the Germanic remainder it often is not.** For Dutch, `model` translates to `model` and `chat` is native, so the decision at all six measured sites produces the identical string either way. `token` and `API` behave the same. Danish and Swedish will hit this too (`model`, `chat`, `API`). The instruction should ask for the *decision* plus *whether it is observable in the string*, otherwise a worker either invents a distinction or looks as if it skipped the step. I reported both above; the next three should be asked for both.

**L4 — [VARIANT] item that should have been [INVARIANT]: the progress-state pattern.** Every catalog must render nine or ten `-ing…` keys (`auth.submit.loading`, `profile.submitting`, `game.starting`, `header.givingUp`, `header.loggingOut`, `queue.leaving`, `play.humanQueue.joining`, `play.ai.preparing`, `history.loading`), and one of them — `header.loggingOut` — sits in the non-wrapping header cluster that 5.5 flags. The four predecessors solved it four different ways (German 1st person `Melde ab...`, Slovak 1st person, Portuguese `A + infinitive`, Icelandic 1st person, Italian nominal `Uscita...`), all silently. The constraint that the swap partner of a nowrap control must not be much longer than the control is language-independent and belongs in 5.5 beside the `header.logout` note. I chose the bare-infinitive-plus-ellipsis pattern for exactly that reason and had to derive the constraint myself.

**L5 — 5.5's `overlay.bestBadge` ruling has no stated tiebreak against the label it sits beside.** `overlay.best` and `overlay.bestBadge` are two keys for one concept at two sizes, exactly like the `board.pts` / `game.aiPlayedFor.points` pair that catalog 4 got an explicit "MAY DIVERGE" ruling for. The badge got a shortest-form ruling and the label got nothing, so whether `Beste zet` / `BESTE` may diverge is left to the worker. Give it the same one-line ruling.

**L6 — §9's commit-body specification now duplicates most of §11's report contract.** Eleven mandated body items on a single-file orphan commit means the same ten decisions are written twice, and the body is longer than some of the code it describes. For da · sv · af, consider reducing the body to what a `git log` reader needs (register, label style, the two article/terminology choices, gate results, the deviation paragraph) and letting the report carry the analysis. Low value, but it is real overhead against a "proportionate" budget.

**L7 — the mandated Next.js reading contains a Dutch example that violates 5.3.** `node_modules/next/dist/docs/01-app/02-guides/internationalization.md:113` gives `"cart": "Toevoegen aan Winkelwagen"` — a title-cased common noun, which is precisely the German-influenced defect 5.3 exists to prevent, sitting inside a file the prompt requires the worker to read *before writing code*. It is third-party documentation and out of scope to change, and I treated it as data. But it is a live trap for the af author, who reads the same file under the same instruction, and one sentence in that prompt would defuse it.

---

**Report justification:** `new-mutation`
**Logical-whole closure:** not-closed
**Authority expiry:** my authority ends at this report. I have not begun a sixth catalog, added a locale, touched the wiring, modified any existing file, or archived this prompt or report into Meta.
**Smallest next step:** issue catalog 6 of 8 — Danish, Swedish or Afrikaans — with M1, M2, M3, M4 and M5 applied to the [INVARIANT] skeleton, L2's plural framing moved to [INVARIANT], and L1's mitigation written into the Afrikaans prompt naming `messages.nl.ts` as its named risk.

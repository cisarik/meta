> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `frontend/src/lib/i18n/messages.de.ts` landed as `74e9d36`, pushed, public readback equal, porcelain
> clean. **ACCEPTED.** Its `Orchestration critique` found SEVEN measured defects in the prompt
> skeleton — one of them a self-contradiction between two `[INVARIANT]` sections that would have fired
> in all eight prompts — plus seven LEADs about campaign-level terminology. My rulings on all fourteen
> are in `./00_notes.md` §42. Nothing below this line was edited.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 10, Worker exchange ordinal: 01
```

**Status:** PASS
**Phase-qualified result:** Implementation complete — MEC-UIL-C1-de delivered, one orphaned German catalog, one commit, published.
**Start commit:** `ad49532e020fe3303731f4c76d9abd2578ba19d7`
**End commit:** `74e9d369e5a4a3054fd149a7d270a9b1fd40112c`
**Changed files:** `frontend/src/lib/i18n/messages.de.ts` (NEW, 404 lines, +404/−0) — the German interface catalog: 296 `deText` entries and 20 `deFn` entries in `messages.en.ts` key order, exports `deText` / `deFn`, imports `pluralDe`. No existing file modified, moved or deleted. `LOCALES` untouched at four; nothing imports the file.

**Tests and validation**

Structural audit (section 7.1), all as specified:

```text
git status --porcelain=v1      exactly one line: `?? frontend/src/lib/i18n/messages.de.ts`
head -7 …/messages.de.ts       byte-identical to section 3 — verified by diff against a
                               reconstructed header outside the repo; both sides
                               sha256 62dbfd5b…d5c3fd68, diff empty
grep -c 'pluralDe('            3
grep -n 'plural'               1 import + 3 pluralDe calls, nothing else
grep -nE 'aria-live|role="status"'   ZERO hits
git diff --check               clean
grep -nE ' as | as const|…'    ONE hit, and it is line 7 of the section 3 header
                               ("…this locale as production quality"). See MEASURED 1.
                               Re-run on lines 8+ : ZERO. Per-construct grep -F for
                               `as const` `as unknown` `Partial<` `?:` `...enText`
                               `...enFn` `TODO` `FIXME` : 0 each.
```

Four frontend gates, all green:

```text
npm run typecheck   PASS  — the code type-checks (exit 0, no diagnostics)
npx vitest run      PASS  — 467 passed / 3 skipped (32 files passed, 1 skipped), equal
                            to the stated baseline; zero failures
npm run lint        PASS  — exit 0
npm run build       PASS  — the build passed; 11 dynamic routes (ƒ), 0 static; the
                            build's own TypeScript stage finished clean in 1636 ms
```

Those last two are two separate claims and both hold: the standalone `tsc --noEmit --incremental false` is clean, and `next build` compiled and type-checked independently. `frontend/.next/` is gitignored, so the build left the tree clean.

Completeness is proved by the type system, not by counting. `deText: Record<TextKey, string>` and `deFn: { [K in FnKey]: (typeof enFn)[K] }` make a missing key, an extra key and a wrong interpolation parameter all compile errors, and `tsconfig.json` `include` is `**/*.ts`, so the orphan is checked in full. Typecheck is clean, therefore the catalog is complete and every signature matches English. (Independently, as a cross-check on the prompt's own numbers rather than as the proof: `enText` = 296, `enFn` = 20, `deText` = 296, `deFn` = 20, zero duplicates, key order byte-identical to `messages.en.ts` in both objects.)

Backend gates were not run — recorded deviation, reasoned in section 7.2 and repeated in the commit body.

**Git result:** one non-force commit `74e9d36` on `main`, staged with exactly `git add frontend/src/lib/i18n/messages.de.ts`. Pre-push gate: `HEAD~1` = `ad49532e020fe3303731f4c76d9abd2578ba19d7` and `git ls-remote origin refs/heads/main` still `ad49532e02…` — both equal to the exact baseline. One `git push origin main`: `ad49532..74e9d36  main -> main`. Public readback: local `HEAD` = `74e9d369e5a4a3054fd149a7d270a9b1fd40112c`, remote `refs/heads/main` = `74e9d369e5a4a3054fd149a7d270a9b1fd40112c`. Working tree clean, `## main...origin/main`, no ahead/behind. `.ap` untouched: gitlink `9c5cc44f8b…` at HEAD, submodule detached at the same `9c5cc44f8b…`, submodule status clean.

---

## Terminology and choices

**The eight frozen game terms** — chosen before any other string, used for all 316 entries, re-checked at the end, and recorded in a comment block at the top of the file:

| concept | German | plural / inflected | reasoning |
|---|---|---|---|
| tile | **Stein** | Steine | the German Scrabble register's word for a letter tile; Mattel's German rules use the full `Buchstabenstein`, and I use the short form throughout |
| letter | **Buchstabe** | Buchstaben | kept strictly separate from `Stein`; a blank is a tile that *becomes* a letter |
| rack | **Bank** | — | the attested term for a player's seven tiles (as in "die Bank leeren"), not the plastic holder |
| blank | **Blanko** | Blankostein / Blankosteine | bare `Blanko` only as the tile caption; inside sentences always the compound `Blankostein`, which fixes the article at `der` |
| bag | **Beutel** | — | |
| board | **Spielbrett** | stem `Brett-` in compounds | `Brettoberfläche`, `Brettglanz`, "näher an A" board talk; the English metonym "board" = a saved game is `Partie`, as Slovak already does |
| pass | **Passen** | passt / gepasst | the German Scrabble verb; deliberately unrelated to `Tauschen` (exchange), which is a different move |
| points | **Punkte** | Punkt / Punkte, abbrev. `Pkt.` | `board.pts` and `game.aiPlayedFor.points` both `Pkt.` |

A ninth term that no prompt section names but that behaves like a frozen one: English `rival` and `opponent` both collapse to **Gegner**, exactly as Slovak collapses both to `súper`.

**Register:** informal **`du` / `dein`** everywhere, error messages included, never `Sie`/`Ihr`. Reasoning: the shipped Slavic catalogs chose informal deliberately (GLOSSARY D2) and it matches the product's voice; one `Sie` among 316 strings is the kind of defect a German reader spots on the first screen. `du`/`dein` are lowercase except sentence- and label-initial.

**Label style:** the **infinitive**, for every button and every action label, with no imperatives anywhere in a control — `Spielen`, `Passen`, `Tauschen`, `Tausch bestätigen`, `Abbrechen`, `Senden`, `Suchen`, `Öffnen`, `Aufgeben`, `Abmelden`, `Aktualisieren`, `Einstellungen öffnen`, `Warteschlange verlassen`, `Passwort ändern`, `Buchstabe wählen`. Reasoning: the infinitive is the German UI convention (and what the shipped Slavic catalogs use), and mixing the two systems across one control strip is the most visible inconsistency a UI catalog can carry. Second-person imperatives appear only in *prose sentences*, never in a control — `Prüfe die eingegebenen Daten.`, `Melde dich erneut an.`, `Lade die Seite neu…` — which is the same split the Slovak catalog makes.

Orthography actually applied: every noun and nominalised form capitalised; `ä ö ü` and `ß` written as real UTF-8 (85 lines carry umlauts, `ß` in `Schließen`/`Schließe`) — no `ae oe ue ss` substitutions anywhere; standard rather than Swiss German; compounds closed (`Zugstatus`, `Suchschritte`, `Brettoberfläche`, `Glanzeffekt`, `Turnierfilz`, `Spiellexikon`, `Kontosynchronisierung`, `Echtzeitverbindung`), with a hyphen only where German orthography requires one after an abbreviation or an English component (`AI-Duell`, `GPU-Last`, `E-Mail`, `Chat-Nachricht`, `Premium-Look`, `Standard-Denkzeit`, `Drag-and-Drop`).

**The six plural noun forms.** Exactly three `pluralDe` call sites, all in the function catalog, two slots each (`one` iff `i === 1`):

| key | singular (`one`) | plural (`other`) |
|---|---|---|
| `a11y.rackTile` | Punkt | Punkte |
| `error.throttled.minutes` | Minute | Minuten |
| `controls.tilesSelected` | Stein | Steine |

`game.toast.invalidWordHeading` is count-sensitive without a helper and writes both forms in full — `Ungültiges Wort!` / `Ungültige Wörter!` — never a suffix trick; German needs it, because both the stem vowel and the adjective ending change. `history.showing`, `history.pageOf` and the three `overlay.stats.*` are label-like or noun-free, so nothing has to agree at an arbitrary count.

Ten values are byte-identical to English, every one deliberately: `landing.brand`, `landing.titleLine1` (protected brand), the four `settings.uiLanguage.*` endonyms (required identical in every catalog), `settings.gameVariant.afrikaans` (the German exonym *is* `Afrikaans`), `history.filter.ai` and `draw.side.ai` (protected `AI` token), and `board.reset` (an established German UI loanword — see below). None is a placeholder.

---

## Flagged risks

I cannot validate any of this German. The file is orphaned and renders nowhere; the named owner of rendered acceptance is the Cooperator.

**Terminology I am genuinely unsure of, most-likely-to-be-changed first**

1. **`Bank` for rack.** Attested for a player's seven tiles in the German Scrabble community, and choosing it follows exactly the precedent GLOSSARY D6 sets for cs and pl (national-association terminology). But it is polysemous for a casual German reader: `rack.empty` renders "Keine Steine auf der Bank". If a reviewer changes one word in this catalog, I expect it to be this one. Plausible alternatives: `Steinhalter` (Mattel's word for the physical holder), `Ablage`, `Steinbank`. Affects 4 strings.
2. **`Blanko` / `Blankostein`.** Mattel's German rules use `Blankostein`; casual German says `Joker`, and Slovak/Czech both chose the joker word (`žolík`). If the product prefers the casual register this becomes `Joker` in 6 strings. I also had to use the compound form inside sentences because the bare noun's gender is unsettled.
3. **`Auslosung` for the opening draw** (`draw.eyebrow`, `draw.reason.blankYou`, `play.ai.body`). This is my selection, not a term I can attest from German Scrabble rules. `Startziehung` and `Auftakt` are plausible.
4. **`Passen` for pass.** Attested, and correctly distinct from `Tauschen`. A reviewer targeting a non-Scrabble audience might prefer `Aussetzen` ("Zug aussetzen"), which is what Slovak/Czech effectively chose.
5. **`Oberflächensprache` for "interface language"** (3 keys). Correct, but heavier than Microsoft German's `Anzeigesprache`.
6. **`Spielen` over `Legen` for `controls.play`.** In German Scrabble you *legst* a word; `Spielen` is clearer for a general audience and matches the key name. Either is defensible; `Legen` would also be 2 characters shorter in the tightest control in the product.
7. **`Modellauswahl` in `landing.card.ai.body`** — a deliberate, reported deviation from section 6 item 4, which requires the literal English token `model`. German `Model` means a fashion model; `Modell` is the word for a model of a thing, so keeping the token verbatim would be a visible error on the landing page. Slovak resolved the same string by dropping the concept entirely; I kept the concept and used correct German. This is the only enText value containing that token. See also MEASURED 2.
8. **`game.lexicon.afrikaans` is the one row of twelve that breaks the pattern.** Eleven rows take a declined German language adjective (`Nicht im slowakischen Lexikon`, `…niederländischen…`, `…isländischen…`); standard German has no established adjective for Afrikaans, so that row takes the language name in a compound: `Nicht im Afrikaans-Lexikon`. Documented in a comment in the file, mirroring GLOSSARY's habit of recording per-row exceptions.
9. **`Die AI`.** `AI` must stay English (section 6 item 4), so I gave it feminine gender from `die Intelligenz`. Almost every German speaker writes `die KI`; a reviewer permitted to change the token would.
10. **`279.496`** uses the German period as thousands separator. GLOSSARY specifies U+00A0 only for sk/cs/pl. DIN 5008 also permits a space, so a reviewer wanting cross-catalog consistency may switch it to U+00A0.
11. **`Pkt.` renders inconsistently through no fault of the string.** `Board.tsx:653` wraps `board.pts` in an `uppercase` class and the overlay does not, so the same key shows `PKT.` in one place and `Pkt.` in another. Pre-existing for sk (`b.` / `B.`) and not German-specific.
12. **`TOP` for `overlay.bestBadge` versus `Bester Zug` for `overlay.best`** — a deliberate divergence between two keys GLOSSARY already allows to differ, taken because the badge is a `text-[10px] px-1.5` pill sitting beside a truncating word and a score. `BESTER ZUG` in that pill would squeeze the word.

**Labels I believe may overflow a non-wrapping or width-capped control — kept correct, not shortened**

| key | German | surface | assessment |
|---|---|---|---|
| `settings.board.woodDesc` | Klassische Nussbaummaserung | `minmax(170px,1fr)` card, `uppercase tracking-[0.1em]` at `0.85rem` | 16-character single token; **will overflow on a narrow viewport**. Wide viewports give each track far more than 170 px, so this is mobile-only. Shortening it drops either "walnut" or "grain". |
| `board.pinchToZoom` + `board.dragToPan` + `board.hide` | Zoom mit zwei Fingern / Ziehen zum Verschieben / Ausblenden | one `inline-flex max-w-full` pill, `text-[0.72rem] uppercase tracking-[0.18em]` | ~1.6× the English tracked width. Will wrap onto more lines than English on mobile rather than clip. **This surface is not in section 5.3's list.** |
| `play.humanQueue.eyebrow` | Spieler-Warteschlange | card eyebrow | 21 characters against English's 11. German has no short standard word for a matchmaking queue. |
| `header.backToBoards` | Zurück zu den Partien | `whitespace-nowrap` tooltip beside the `3.08rem` back button | 21 characters in an absolutely-positioned nowrap tooltip; can extend past a narrow viewport edge. Used only as `aria-label` + tooltip, never as visible button text, so layout impact is bounded. |
| `queue.leave` / `queue.leaving` | Warteschlange verlassen / Verlasse die Warteschlange... | waiting-room button | roughly twice the English length; the button looks wide enough, but I did not verify it. |
| `controls.confirmExchange` | Tausch bestätigen | nowrap 2-column mobile grid | 17 characters against English's 16 — essentially no regression, noted only because it is the tightest nowrap pair in the product. |
| `controls.play/pass/exchange` | Spielen / Passen / Tauschen | the `[minmax(0,1fr)_minmax(0,1fr)_minmax(0,1.08fr)]` nowrap grid | 7 / 6 / 8 characters against 4 / 4 / 8 — a real but small increase in the tightest control strip. |
| `overlay.stats.*` | Versucht: / Gültig: / Verworfen: | three statistics in one row | within a character or two of English; should be unaffected. |

**Places German grammar forced a construction English does not have**

- `error.throttled.minutes` ends **after** the plural slot: "…in etwa {n} Minuten **erneut.**" English and Slovak both end *at* the counted noun. The helper call therefore has a trailing string concatenation that no shipped catalog has.
- `game.aiPlayedFor.before` had to use the simple past — "Die AI spielte für" — because German perfect would put the participle after the injected score `<span>`, which the fixed `[before]{score}[points]` composition cannot express.
- `board.reset` + `board.zoomNoun` render as a fixed `[action][noun]` two-span pair. German wants the object first ("Zoom zurücksetzen"), which that call site cannot produce, so the established German UI loanword `Reset` carries the action and `Zoom` follows it, giving "Reset Zoom". A component change would be needed for the idiomatic order, and that is out of this slice's one-path allowlist.
- `history.showing` became a colon label — "Angezeigt: 1-10 von 42" — dropping "games" the way Slovak does, so no noun has to agree at 2–4 or 0.
- `blank.chooseLetter` and `a11y.rackBlank` needed the compound `Blankostein` rather than bare `Blanko`, purely to fix the article.
- `a11y.dialog.blank` ("Buchstabe wählen") is an infinitive where English is a bare imperative-looking phrase; that is the label-style rule applied to an accessible name.

---

## Orchestration critique

### MEASURED

1. **Section 7.1's forbidden-weakening grep can never return zero hits, in any of the eight catalogs, because section 3's mandated header trips it.** Line 7 of the byte-exact header reads "…before presenting this locale **as** production quality", which matches ` as `. Section 3 forbids reflowing or shortening the header, so two INVARIANT sections contradict each other by construction. It is a prose false positive, not a type weakening. **Fix for prompts 2–8:** scope the grep with `tail -n +8`, or anchor it to code (` as [A-Z]`, `\bas const\b`), or state "expect exactly one hit and it is header line 7". As written, a literal-minded Worker either reports a failed audit or silently edits the header. *Assumption I proceeded on:* section 3 (byte-exact, Cooperator's condition) outranks section 7.1's expected hit count, whose stated purpose is section 4's type weakenings. Verified zero real weakenings by re-running on lines 8+ and by per-construct `grep -F`.

2. **Section 6 item 4 collides with German, and it will collide differently in at least four of the remaining seven languages.** Measured: `landing.card.ai.body` ("Model-aware premium games") is the only enText value containing any protected token other than `chat`. `Model` in German means a fashion model. Slovak dropped the concept; I kept it and wrote `Modellauswahl`, deviating from the rule's letter. Italian and Portuguese will want `modello`/`modelo`; Dutch, Danish and Swedish can keep `model` but must inflect or capitalise it. **The INVARIANT text should say explicitly whether item 4 governs prose or only product identifiers and model ids.**

3. **Section 5.3's measured list is accurate with two small errors.** `PremiumPicker` lives at `src/components/settings/PremiumPicker.tsx`, not under `components/ui/`. The `max-w-md` cited alongside toasts is the give-up dialog (`src/app/game/[id]/page.tsx:426`); every toast is `max-w-sm`. Everything else verified as stated: `whitespace-nowrap` on all `GameControls` buttons, the mobile `[minmax(0,1fr)_minmax(0,1fr)_minmax(0,1.08fr)]` grid, `min-w-[5rem]`/`min-w-[5.8rem]` play button, `w-[3.08rem]` back button, nowrap tooltips, `max-w-xs` overlay prose, `max-w-[min(92vw,28rem)]` blank dialog, `minmax(132px,1fr)` and `minmax(170px,1fr)` settings grids.

4. **Section 5.3 omits the tightest text surface in the product.** `Board.tsx:665-680` puts `board.pinchToZoom`, `board.dragToPan` and `board.hide` in a single `inline-flex max-w-full` pill at `text-[0.72rem] uppercase tracking-[0.18em]`; English already fills it. `board.*` should join `controls.* header.* overlay.* picker.*` in the "choose the shortest idiomatic term" list — Dutch, Danish, Swedish and Icelandic compounds will hit it as hard as German.

5. **Section 6 item 3 enumerates the noun-agreement traps but misses two composition traps of the same class.** `game.aiPlayedFor.before` + `.points` are concatenated around a live score span (`page.tsx:338`), which forbids a German/Dutch perfect tense; and `board.reset` + `board.zoomNoun` are a fixed `[action][noun]` span pair (`Board.tsx:692-693`) that German, Dutch and the Nordic languages all want reversed. Neither is a plural problem, so item 3's framing does not catch them. **Both belong in the INVARIANT list of "keys whose call site constrains word order".**

6. **Every number and measured claim in the prompt that I could check holds.** 296 text keys / 20 function keys with zero duplicates; vitest 467 passed / 3 skipped exactly; build 11 dynamic and 0 static; `tsconfig.json` `include` really is `**/*.ts`, so the orphan is fully checked; `i18n.test.ts:481-507` really does walk `frontend/src` excluding tests. One refinement: that test's regex is bare `/aria-live/g`, not `aria-live="polite"`, so it is slightly stricter than section 6 item 5's wording implies. I also confirmed no test enumerates catalog files by directory, so apart from that one scan an orphan is invisible — which is the load-bearing fact behind section 2, and it is worth stating there directly.

7. **Section 4's file shape has no slot for comments, but the worked example is full of them.** `messages.sk.ts` carries in-object comments; I added four (terminology block, endonym block, the Afrikaans exception, the two-span note). Item 7 ("key order copied … so a reviewer can diff the two files side by side") could reasonably be read as forbidding extra lines. **Say explicitly that terse in-object comments are expected**, because they are where the next reader will actually find the terminology decisions.

### LEAD

1. **The eight-term freeze should be campaign-level, not per-Worker.** Nothing in the current skeleton stops catalog 5 from choosing a different metaphor for "rack" than catalog 1 while both are individually defensible. D6's "do not harmonize" licences a *specific attested* cs/sk divergence; it is not a licence for eight unrelated registers. Consider collecting all eight tables into one artifact after this pilot and pinning the remaining seven against it.
2. **"board" is two concepts in English** — the physical surface and a metonym for a saved game — and section 5.1 freezes one word for it. All eight languages will have to split it, as Slovak already did (`hracia plocha` vs `partia`). Make the split part of the INVARIANT terminology instruction rather than something each Worker rediscovers.
3. **The label-style decision is in the VARIANT section but is invariant in intent.** "Pick one style for controls and state which" applies to all eight; only the examples are German. As currently placed, prompt 5 could omit it and get a catalog that mixes styles.
4. **`rival` / `opponent` collapse to one word in most target languages** and no section mentions it. It is a de-facto ninth frozen term; naming it would prevent a Worker from using two words in one catalog and one in another.
5. **`overlay.bestBadge` vs `overlay.best` forces the same badge-width tradeoff eight times.** One campaign ruling ("the badge may carry a shorter word than the label; state it in the report") saves eight identical judgement calls and eight slightly different answers.
6. **The terminology table is now required in three places** — report, commit body, and (by my choice) the file header comment. Three copies drift. Pick one canonical home; my recommendation is the file, because that is what a future reviewer opens.
7. **"Reasoning recommendation: Medium" was right for the mechanics but understates the decision load.** The key set, helper and shape genuinely were decided for me, but terminology selection and layout triage were the bulk of the work, not "volume and care". I would not carry the same recommendation unchanged into Icelandic (non-Nordic plural rule) or Italian/Portuguese (a third `many` slot that may legitimately duplicate `other`), where the plural surface itself needs judgement.

---

**Resolved Execution Issues / Near-Misses:** one. The section 7.1 forbidden-weakening grep returned a hit that, taken literally, is a failed audit; the hit is the section 3 mandated header. Resolved without mutating the header, by scoping the grep to lines 8+ and verifying each forbidden construct individually with `grep -F` (0 hits each), then reporting the prompt conflict rather than resolving it silently. Cross-referenced as MEASURED 1. Everything else — file authoring, all four gates, commit, push, readback — ran first-time clean with no retries.

**Pre-Existing Failure Classification:** none. The suite was 467 passed / 3 skipped before this slice by the ORCHESTRATOR's measurement and 467 passed / 3 skipped after it; no pre-existing red, no flake, no skip introduced or resolved. `prompts.test.ts` is green, so the MOVE CORE hash has not moved.

**Deviations and risks:** two deviations, both recorded above and in the commit body — the backend five not run (section 7.2, explicit), and `Modellauswahl` instead of the literal `model` token (section 6 item 4, reasoned, one string). The named decision risk is undischarged by design: 316 strings of unreviewed German are now in the repository, judged by no gate, rendering nowhere. The mitigations that exist are the header, the terminology freeze, and this report. Rollback is `git revert 74e9d36`: one orphaned file, no migration, no persisted state, no runtime effect.

**Context pressure:** comfortable — roughly half the window used, most of it the four reference files; no compaction occurred and none was near.

**Smallest next step:** have the Cooperator inspect the eight frozen terms above — specifically `Bank` (rack) and `Blanko`/`Blankostein` — and rule on section 6 item 4's scope, before catalog 2 is dispatched. Both answers change the seven remaining prompts, and both are cheaper to settle now than to reconcile across eight files later.

**Report justification:** new-mutation
**Logical-whole closure:** not-closed
**Authority expiry:** my authority for this exchange is exhausted at this report. I created no second catalog, wired no locale, touched nothing under `.ap`, and archived nothing into Meta. Any further work — including the wiring slice, catalog 2, and archiving this prompt/report pair — requires a new authoritative ORCHESTRATOR prompt.

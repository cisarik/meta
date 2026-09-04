> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `frontend/src/lib/i18n/messages.is.ts` landed as `490426a`, pushed, readback equal, porcelain clean.
> **ACCEPTED.** Eleven MEASURED findings and three LEADs — the strongest critique of the campaign, and
> **two of them are product defects with their own slices rather than skeleton corrections**:
> `foldForSearch` in `locales.ts` cannot fold `ð þ æ ß`, so picker search will silently fail for four
> of the eight new locales including German which already ships; and `history.outcome.unknown` has NO
> product call site, so twelve catalogs author a string that can never render. Both verified by me.
> My rulings on all fourteen findings are in `./00_notes.md` §44. The report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 12, Worker exchange ordinal: 01
```

**1. Status:** PASS

**2. Phase-qualified result:** Implementation complete — MEC-UIL-C3-is, the Icelandic interface catalog, one new orphaned file, 296 text keys and 20 function keys, `LOCALES` untouched at four.

**3. Start and end commit:** start `3cfa13bb9d1edd8fc6e62e2d1e6837c4353908c8` → end `490426a4274ea4a95915a935d5787a4a31f9a9c1`

**4. Changed files and purpose:** `frontend/src/lib/i18n/messages.is.ts` (NEW, 480 lines, only path) — `isText` / `isFn`, key order byte-for-byte identical to `messages.en.ts`, mandated seven-line header, five comment classes present. No existing file modified, moved or deleted.

**5. Tests and validation:**
- Repository gate: all seven values matched, including `HEAD:.ap` = `git -C .ap rev-parse HEAD` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656` (detached), clean tree, remote at baseline, no listener on 3000/8000.
- Structural audit (§7.1), all green: `git status --porcelain=v1` exactly one line `?? frontend/src/lib/i18n/messages.is.ts` · head-7 diff against `messages.de.ts` EMPTY · `grep -c 'pluralIs('` = 3 · `grep -n 'plural'` = 4 lines (1 import + 3 calls, nothing else) · `aria-live|role="status"` ZERO · cast-shaped pattern over `tail -n +8` ZERO · `git diff --check` clean.
- Icelandic one-liners: 211 lines carry at least one of `ð þ æ ö`; `\b(dh|th|ae|oe)\b` ZERO.
- Four frontend gates: **typecheck passed** · `npx vitest run` **467 passed / 3 skipped (470)** across 32 passed / 1 skipped files — identical to the baseline I measured **before** creating the file · **lint passed** · **`npm run build` compiled successfully**, route table unchanged at **eleven dynamic and zero static**. The build passing and the code type-checking are two separate claims; both hold.
- Completeness proof is `npm run typecheck`, not a hand count: `isText` is `Record<TextKey, string>`, `isFn` is `{ [K in FnKey]: (typeof enFn)[K] }`, `tsconfig` `include` is `**/*.ts`, so a missing key, an extra key or a wrong interpolation parameter is a compile error even though nothing imports the module.
- Deviation, recorded: the backend five were not run. Diff confined to `frontend/`, pytest collects only `backend/`, mypy scope is `config game gamecore accounts catalog`.

**6. Commit and push:** one non-force commit `490426a`, subject `feat(i18n) the Icelandic interface catalog`, staged with the exact path only. Pre-push gate: `HEAD~1` = `3cfa13bb…` and `git ls-remote origin refs/heads/main` still `3cfa13bb…`. One `git push origin main`. Readback: remote `refs/heads/main` = `490426a4274ea4a95915a935d5787a4a31f9a9c1` = local HEAD; `## main...origin/main`; `.ap` gitlink unchanged.

**7. Resolved Execution Issues / Near-Misses:** two, both caught before the commit.
- The §7.1 line `grep -n 'plural' "$F"` returned **7** hits on my first draft, not 4. Three were English prose in the comment blocks §4 *requires* — including the counted-noun block naming its own helper. I rewrote the comments (`many-form`, "the `one` slot", "the helper imported above") rather than weaken the file. See MEASURED M1.
- My first commit-message draft was written with Icelandic ASCII-transliterated (`thu`, `Saenska`, `thysja`). Discarded and rewritten in full Icelandic orthography before committing. Nothing transliterated reached the file or the commit.

**8. Pre-Existing Failure Classification:** none. The vitest run emits `[libretiles-provider-failure]` lines from provider-failure fixtures on both the baseline and the post-change run; they are fixture output, not failures, and the pass/skip counts are identical.

---

## Terminology and choices

**The nine frozen terms** (the file's terminology block is their canonical home):

| concept | Icelandic |
|---|---|
| tile | `stafur` (m.) |
| letter | `stafur` — **deliberate collapse**, the Slovak `písmeno` shape |
| rack | `grind` (f.) |
| blank | `jóker` (m.) |
| bag | `poki` (m.) |
| board — surface | `borð` (n.) |
| board — saved game | `viðureign` (f.) |
| pass / exchange | `passa` / `skipta` — different words |
| points | `stig` (n.) |
| rival = opponent | `mótherji` (m.) — one word |

Tile/letter collapse: Icelandic word-game usage says `stafur` for the piece and the letter, it is the shortest correct term on the tightest surfaces, and tile/letter is not one of the three mandated splits. Knock-on: `profile.ph.new` had to say `tákn`, not `stafir`, because there "characters" means text characters. `leikur` is the **move** (as in chess), which is what forces `viðureign` rather than `leikur` for the match. `passa` is frozen as a **verb only** — Icelandic `passi` is a passport — so `game.toast.passRejected` is "Ekki hægt að passa"; and because `passa` also means "to fit", `error.conflict` uses `stangast á við`.

**Register:** informal `þú` / `þinn` everywhere, error messages included. Icelandic has no living formal address (`þér` is archaic), so unlike German and Portuguese this was not a choice between two usable registers.

**Label style:** infinitive on every control, action label, column heading and accessible name; `þú`-imperative only in prose sentences and hero headings. It is Icelandic UI convention and also the shorter form on nowrap surfaces.

**Pre-authorized exceptions used:** pagination (`Fyrri` / `Næsta`, adjectives agreeing with an implied `síða`); toggle state words (`Kveikt` / `Slökkt`); badge words (`overlay.bestBadge` "BESTI" against `overlay.best` "Besti leikur", and `settings.board.active` = "Í notkun", an invariable phrase because `Tré` is a neuter *noun* while `Svart` and `Grænt` are neuter *adjectives*).

**Counted nouns:**
- point noun `stig` / `stig` — Icelandic `stig` is neuter and **syncretic**: nominative and accusative are `stig` in both numbers, so both slots carry the same word and it is correct at 1, 21 and 101. Commented in the file so nobody "fixes" it.
- minute noun `mínútu` / `mínútur` — accusative, governed by `eftir um`, a case I control: "eftir um 21 mínútu", "eftir um 101 mínútu", "eftir um 11 mínútur".
- tile noun `stafur valinn` / `stafir valdir` — the slot carries a **phrase**, because an Icelandic predicate participle agrees in number and gender and cannot be appended outside the selection the way German appends `ausgewählt`.

**Protected tokens:** `model` **translated** to `líkan` at `landing.card.ai.body` (ordinary noun on a landing card; Icelandic `líkan` has no competing reading — a fashion model is `fyrirsæta`). All five `chat` sites **kept English** (`landing.card.queue.body`, `a11y.chatInput`, `chat.title`, `chat.unavailable`, `game.toast.chatOffline`), because each names the panel the player matches against `chat.title`. **`AI` is FEMININE**, from `gervigreind`; the gender is visible at exactly one key, `game.giveUp.ai` ("úrskurðuð").

**All three §6.5 call sites were HARMLESS for Icelandic:**
1. `game.aiPlayedFor.before` + `.points` — Icelandic puts the verb before the number and the counted noun after: "AI fékk 34 stig" fits the fixed score span natively.
2. `board.reset` + `board.zoomNoun` — Icelandic verb-object order is already `[action][noun]`: "Endurstilla þysjun".
3. `game.aWord` inside `game.toast.aiPlayedWord` — Icelandic **has no indefinite article at all**, so the bare noun is not a stylistic choice; and `orð` is neuter with accusative = nominative, so it composes correctly inside "AI spilaði …".

---

## The twelve language names

`settings.gameVariant.*`, capitalized because these are standalone picker rows; the same twelve words appear lowercase in `game.lexicon.*` running text, which is what Icelandic orthography requires.

| slug | my value | `game.lexicon.*` form |
|---|---|---|
| english | **Enska** | `Ekki í ensku…` → n/a (Collins row) |
| slovak | **Slóvakíska** | Ekki í slóvakíska orðasafninu |
| czech | **Tékkneska** | Ekki í tékkneska orðasafninu |
| polish | **Pólska** | Ekki í pólska orðasafninu |
| afrikaans | **Afríkanska** | Ekki í afríkanska orðasafninu |
| italian | **Ítalska** | Ekki í ítalska orðasafninu |
| dutch | **Hollenska** | Ekki í hollenska orðasafninu |
| german | **Þýska** | Ekki í þýska orðasafninu |
| portuguese | **Portúgalska** | Ekki í portúgalska orðasafninu |
| danish | **Danska** | Ekki í danska orðasafninu |
| swedish | **Sænska** | Ekki í sænska orðasafninu |
| icelandic | **Íslenska** | Ekki í íslenska orðasafninu |

The two families are consistent for free: an Icelandic language name **is** the nominalized weak adjective, and the weak neuter form is identical in every case, so `game.lexicon.*` reuses the same string in lowercase and **Afrikaans needs no exception** — unlike German (compound) and Portuguese (invariable name).

**Swedish decision: `Sænska`, not `Svenska`.** `sænska` is the Icelandic form built on the adjective `sænskur`; `svenska` is the *Swedish* endonym, not an Icelandic word. That reason stands on its own, and it also avoids adding a third collision. Collisions in my actual strings, derived exhaustively and case-insensitively: **exactly two** — `Enska ⊂ Hollenska` and `Enska ⊂ Íslenska`. Both unavoidable in correct Icelandic. One extra fact for whoever writes the test: choosing `Sænska` costs picker searchability instead — see MEASURED M5.

---

## Flagged risks

**Terminology I am unsure of, worst first.**
1. **`jóker` for blank** — highest. A real Icelandic noun for a wildcard, chosen on the `žolík` precedent, but an Icelandic Scrabble player may use an `auður stafur` construction instead. Touches `a11y.rackBlank`, `draw.blankCaption`, `draw.subtitle`, the three `draw.reason.blank*`, `blank.chooseLetter`.
2. **`grind` for rack** — `standur` and `rekki` are equally plausible. Touches `rack.empty`, `history.endReason.bagEmpty`, `settings.premium.description`, `game.toast.aiExchangedBody`.
3. **`chat` kept English** at five sites — the D6 default, but Icelandic has a good native term (`spjall`) and Icelandic is a purist language. This is the protected-token call I most expect a native reviewer to overturn.
4. **The tile/letter collapse** — if the Icelandic association distinguishes them the way Czech separates `kámen` / `písmeno`, a second word is needed and `profile.ph.new` can go back to `stafir`.
5. **`viðureign`** for the saved-game metonym — correct but the longest choice of the campaign so far; `spil` is shorter, and I rejected it as too card-game-flavoured.
6. **`þysja` / `þysjun`** for zoom — the Icelandic neologism; some Icelandic UIs keep `zoom` or use `súmma`.
7. **`Prófíll`**, **`Hamur`** (Mode), **`Yfirgefið`** (`history.outcome.abandoned`), **`Fyrirspurnamark`** (Rate Limited), **`Afbrigði viðureignar`** (Game variant), **`Herbergi {code}`** (Room), **`síu`** (filter), **`orðaleikur`** (wordplay) — each defensible, none certain.
8. **`gjaldfrjáls`** for "free" — correct but long; `frír` is shorter and colloquial.
9. **`premium` kept untranslated**, indeclinable, hyphenated on Icelandic compound rules (`Premium-útlit`, `premium-viðureignir`, `premium-yfirlitinu`). Not a protected token, so this is my call; a reviewer may want `vandaður`.
10. **`drag-and-drop` kept English** in `meta.description`, on the Slovak precedent.
11. **`BESTI`** — a standalone weak superlative with its noun elided. `BESTUR` or `HÆST` are alternatives. Chosen over `BEST` specifically so nobody reads the badge as untranslated English.
12. **`Byrja...`** (`game.starting`) reads as an infinitive as well as a first-person present.
13. **`Klíptu til að þysja` / `Dragðu til að færa`** are imperatives sitting beside `board.hide` = `Fela`, an infinitive. Deliberate (they are prose guidance, not controls) but visibly mixed in one pill.

**Labels I believe may overflow — kept correct, not shortened, and measured against English:**

| key | en | is | note |
|---|---|---|---|
| `header.games` | 5 | **11** `Viðureignir` | nowrap `shrink-0` header cluster — worst in the header |
| `header.backToBoards` | 14 | **22** | only reaches an `aria-label` and a nowrap tooltip |
| `header.giveUp` | 7 | 10 `Gefast upp` | same cluster |
| `header.logout` | 6 | **7** `Skrá út` | **the campaign's highest measured overflow risk is NOT a risk in Icelandic** — one character longer than English, and shorter than pt-PT's 15 |
| `board.pinchToZoom` | 13 | **19** | tightest surface in the product, `text-[0.72rem] uppercase tracking-[0.18em]` |
| `board.dragToPan` | 11 | **18** | same pill |
| `board.hide` | 4 | **4** `Fela` | same pill, no worse than English |
| `board.reset` + `.zoomNoun` | 10 | **18** `Endurstilla þysjun` | floating pill |
| `overlay.best` | 4 | **12** `Besti leikur` | `text-[10px] uppercase tracking-wider` |
| `controls.*` | 4/4/8/16/6 | 5/5/6/16/9 | the mobile nowrap grid is fine; `Skipta` is *shorter* than `Exchange` |
| `settings.timeout.120` | 21 | **26** `Sjálfgefinn umhugsunartími` | `minmax(132px,1fr)` / `minmax(170px,1fr)` choice cards |
| `game.blocker.rate.title` | 21 | **37** | dialog title, wraps |

`history.col.*` are **not** shortened for layout: verified `<table className="min-w-full">` with plain `<th className="px-4 py-3">`, so long headings wrap.

**Places agreement or a fixed call site forced a construction English did not have:**
- `controls.tilesSelected` — participle inside the counted-noun slot (Icelandic predicate participles agree; German's does not).
- `settings.board.active` — invariable phrase, because `Tré` is a noun and `Svart`/`Grænt` are adjectives.
- the eight `history.outcome.*` — nouns or invariable phrases (`Sigur`, `Tap`, `Jafntefli`, `Uppgjöf`, `Í bið`, `Í gangi`), so none agrees with `viðureign` in one site and an implied neuter in another.
- `history.unknownDate` — unmarked **neuter**. Icelandic's default standalone form is the neuter, which is correct for both `dagsetning` (f.) and `notandanafn` (n.), so this trap is **cheaper** in Icelandic than in Portuguese, where the unmarked form is masculine.
- `game.status.opponentPlaying` — `á leik` instead of a participle, because `{name}`'s gender is unknown.
- `draw.reason.closer` — the invariable comparative adverb `nær`, so neither tile letter is declined.
- `history.endReason.bagEmpty` — `poki` (m.) + `grind` (f.) forces the neuter many-form `tóm`.
- `game.toast.passRejected` and `error.conflict` — both bent by freezing `passa` as a verb.
- `overlay.stats.*`, `history.showing`, `history.pageOf` — noun-free / invariable neuter labels.
- **I cannot validate any of this visually.** The file is orphaned and renders nowhere; rendered acceptance is the Cooperator's after wiring.

---

## Orchestration critique

### MEASURED

**M1 — §7.1, the audit line, again.** `grep -n 'plural' "$F"` — "must show your one import and three `pluralIs` calls, nothing else" — **collides with §4's own mandated counted-noun comment block.** `plural` is a substring of the helper name, and a block documenting counted-noun behaviour naturally writes "the singular/plural form" or names `pluralIs`. My first draft produced 7 hits; three were correct required English prose. This is the *third* defect found in that one audit block, and the first where the pattern collides with the prompt's own required English rather than with a target language — so the general rule in §7.1 ("an audit pattern aimed at code must not be runnable against prose") is even broader than stated: it must not be runnable against the *file's mandated commentary* either. Cost: the file can no longer name its own helper in the block that documents it. Fix for catalogs 4–8: exclude comment lines, e.g. `grep -nE '^[^/]*plural' "$F"`, or state the expectation as "1 import + 3 calls, plus comment lines".

**M2 — §5.2 mis-attributes `history.unknownDate`.** Verified at all four sites: `GameHistoryPanel.tsx:97` is a missing/invalid **updated date**; `ProfileModal.tsx:23` and `:26` are inside `formatJoinedDate` and are a missing/invalid **joined date**, not a username; only `ProfileModal.tsx:220` (`profile?.username ?? …`) is a missing **username**. The prompt says ":23, :26 and :220 use it for a missing USERNAME". The conclusion survives — one site really is a username, so no declined form works everywhere — but the split is 3 dates + 1 username, the reverse of what §5.2 claims. Catalogs 4–8 will read that sentence and reason from the wrong ratio.

**M3 — §6.1's "six words" under-counts.** "A two-slot helper takes two string arguments per site, so Icelandic's entire plural surface is SIX WORDS" is false for any language whose predicate participle agrees. `controls.tilesSelected` must be `pluralIs(count, "stafur valinn", "stafir valdir")`: two words per slot, because `valinn`/`valdir` agree in number and gender and cannot sit outside the selection the way German's invariable `ausgewählt` does. Danish, Swedish, Dutch and Italian predicate adjectives all agree in at least number, so catalogs 4–8 will hit this too. Say "two slot fillers per site" rather than "words".

**M4 — §5.1's 21/101 emphasis reaches one of the three sites, not three.** Measured: `controls.tilesSelected` is bounded by rack size (max 7 selectable); `a11y.rackTile`'s `points` is a tile face value, and the maximum across **all twelve** shipped variant manifests is **10** (Danish and Portuguese are 8, Polish 9, the other nine 10) — so `one` is reachable there only at 1. Only `error.throttled.minutes` takes an arbitrary Retry-After-derived count and can actually be 21, 101 or 1001. The signatures are unbounded `number`, so the requirement is right to state; the *emphasis* lands on one site, and saying so would let catalogs 4–8 spend their attention correctly.

**M5 — a whole surface no [INVARIANT] section names: `foldForSearch`.** `frontend/src/lib/i18n/locales.ts:23-31` folds picker-search input with NFD + `\p{Diacritic}` strip plus `EXPLICIT_SEARCH_FOLDS` for `ł đ ø`. Its own comment says "Letters NFD + `\p{Diacritic}` cannot fold: stroke (ł), D-stroke (đ), slashed O (ø)" — **that list is incomplete.** `ð` (U+00F0), `þ` (U+00FE) and `æ` (U+00E6) are exactly the same class and have no entries. Measured with the shipped function: `þýska → þyska`, `sænska → sænska`, so typing `thyska` does **not** match "Þýska" and `saenska` does **not** match "Sænska" in `PremiumPicker`, while `islenska → íslenska` and `tekkneska → tékkneska` work because those fold via NFD. This already latently affects the four shipped locales and will hit Icelandic hard once wired. `locales.ts` is on my forbidden list, so I did not touch it. Recommend a dedicated slice adding `ð→d`, `þ→th`, `æ→ae` (and `ß→ss` before German is wired), and adding this surface to §5.5 for catalogs 4–8.

**M6 — §5.5 describes `PremiumPicker`'s truncation but not its search.** Truncation verified at `PremiumPicker.tsx:239` and `:301`. The picker also *searches* the labels my catalog authors, through the function in M5. That is a second constrained property of the same surface and it is invisible in the current §5.5 wording.

**M7 — §5.5's `max-w-md` disambiguation is incomplete.** "The `max-w-md` nearby is the give-up dialog at `page.tsx:426`, not a toast" is true, but there is a second `max-w-md` at `GameHistoryPanel.tsx:269` (the empty-state block). Harmless; the note reads as exhaustive.

**M8 — §6.5 says "MEASURED, all three"; there is a fourth of the same kind.** `history.open` serves **both** a column heading (`GameHistoryPanel.tsx:295`) and a button label (`:139`), and at `:139` it alternates in the same slot with `history.current` — an infinitive against an adjective in one position. Icelandic absorbs it ("Opna" reads correctly in both roles, "Núverandi" is an invariable present participle), so I comment it rather than flag it. A language whose column headings are nouns and whose buttons are verbs cannot reuse one string there. Worth adding to §6.5.

**M9 — `history.outcome.unknown` has no product call site.** `OUTCOME_META` (`GameHistoryPanel.tsx:36-74`) covers all seven `GameHistoryOutcome` values and has no `unknown` arm. The key appears only in the six catalogs, `i18n.test.ts:1491` and `GLOSSARY.md`. Eight catalogs are authoring a string that cannot render. Not mine to remove; worth knowing before catalogs 4–8 spend agreement effort on it.

**M10 — §5.1 and §5.6 reproduce exactly, and are the two most accurate sections in the prompt.** `Intl.DisplayNames("is")` on node v26.4.0 / ICU 78.3 returns all twelve exonyms byte-for-byte as printed. `Intl.PluralRules("is")` over 0..3000 selects `one` at **270** values and diverges from English at **269** of them — only n=1 agrees. The collision derivation is exactly right: two with CLDR names, three if `svenska` is substituted. Nothing to correct.

**M11 — a trivial line-range slip.** §5.5 cites `Board.tsx:665-680` for the hint pill; the three keys are at 669, 671 and 677 and the `inline-flex max-w-full` element is line 668 (wrapper opens at 663). `Board.tsx:692-693` for `board.reset`/`board.zoomNoun` is exact, as is `ScorePanel.tsx:346`, `page.tsx:338`, `page.tsx:1003`, `i18n.test.ts`'s exactly-once scan, and the whole of §5.5's class list including the un-constrained history table.

**Which [VARIANT] item should have been invariant:** §5.6's *mechanism*. "Report all twelve names as a table so the collision set can be re-derived from your actual strings" is framed as Icelandic-only because Icelandic is where the collision bites, but the twelve-name table is the input to that future test in **all eight** catalogs, and the collision set has to be derived from eight sets of strings, not one. Dutch (`Nederlands` ⊂ nothing, but `Deens`/`Zweeds` share suffixes), Danish and Swedish will have their own. Promote the reporting requirement to [INVARIANT] and keep only the *Icelandic collision facts* variant.

### LEAD (unverified)

**L1 — `board.pts` casing is inconsistent across its three render sites, and the shipped catalogs diverge because of it.** `board.pts` renders under a CSS `uppercase` class at `Board.tsx:653` but **without** it at `AIThinkingOverlay.tsx:113` and `:314`. German ships `"Pkt."` and Portuguese ships `"PTS"`, so in the overlay Portuguese reads "PTS" while German reads "Pkt." — one of the two is presumably not what its author intended. I chose lowercase `"stig"` so the board uppercases it and the overlay reads naturally. **UNVERIFIED:** I have rendered nothing and do not know whether the mixed casing is deliberate. Flagged as a lead for the wiring slice, not asserted.

**L2 — unverified observation on `messages.de.ts`.** It writes `landing.titleLine2` "Mensch und AI." (singular) while `history.filter.human` is "Menschen" and `history.mode.human` "Duell gegen Menschen" (plural). That may be deliberate register in a hero line. **UNVERIFIED** — I did not read it as a defect and did not act on it.

**L3 — checked and found correct, recorded so catalog 4 does not re-litigate it.** `messages.pt.ts` writes `279\u00A0496`. Measured: `Intl.NumberFormat("pt-PT")` yields U+00A0 as the group separator while `Intl.NumberFormat("pt")` yields a period — so catalog 2's non-breaking space is right for a pt-PT catalog and is not a bug. Icelandic takes a **period** (`Intl.NumberFormat("is")` → `279.496`), which is what I wrote.

**Context pressure:** moderate — roughly two-thirds of the window consumed by the six reference files, the call-site verification and the four gates; comfortable headroom remained throughout, and no step was compressed for budget.

---

**Report justification:** `new-mutation`

**Logical-whole closure:** not-closed

**Authority expiry:** my authority ended at this report. I have not begun a fourth catalog, have not touched `LOCALES`, `translate.ts`, `plural.ts`, any test or any component, and have not archived this prompt or this report into Meta — that is the ORCHESTRATOR's, now that this report exists.

**Smallest next step:** issue catalog 4 with the M1 audit-line fix applied, M2's `history.unknownDate` attribution corrected to 3 dates + 1 username, M3's "six words" restated as "six slot fillers", and M5's `foldForSearch` gap added to §5.5 as a constrained surface — then decide separately whether `EXPLICIT_SEARCH_FOLDS` gets `ð þ æ ß` before or after the wiring slice.

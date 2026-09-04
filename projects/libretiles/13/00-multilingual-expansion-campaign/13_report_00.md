> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim. Status `PASS`;
> `frontend/src/lib/i18n/messages.it.ts` landed as `6bf7c5e`, pushed, readback equal, porcelain clean.
> **ACCEPTED.** Six MEASURED findings and five LEADs. **The sharpest is M1 and it is about my own
> correction discipline: I applied catalog 3's comment-exclusion fix to ONE grep line in the audit and
> not to its sibling with the identical defect class.** ✔ Verified: the cast-shaped pattern fires on
> `// as Portuguese did`, and `^[^/]*` removes it. And M2 finds that the elision check I ADDED IN THIS
> PROMPT is itself defective — Italian apocope (`un po' di`) is followed by a space by rule, so the
> line flags correct Italian. Fifth defect in that one audit family, and the first I introduced myself
> in the same prompt that carried three corrections to it. My rulings on all eleven findings are in
> `./00_notes.md` §45. The report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 13, Worker exchange ordinal: 01
```

**1. Status:** PASS
**2. Phase-qualified result:** Implementation complete — MEC-UIL-C4-it, the Italian interface catalog, one new orphaned file.
**3. Start commit:** `490426a4274ea4a95915a935d5787a4a31f9a9c1` · **End commit:** `6bf7c5e70cf82a32ab45db945019a7f42f039c42`
**4. Changed files:** `frontend/src/lib/i18n/messages.it.ts` (NEW, +551 lines, the only path) — 296 `TextKey` entries plus 20 `FnKey` entries, `itText` / `itFn`, deliberately orphaned. No existing file was modified, moved or deleted; `LOCALES` is still four; nothing imports it.
**5. Repository gate:** all seven checks matched — HEAD, `HEAD:.ap` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, detached `.ap` HEAD identical, `## main...origin/main`, empty porcelain, remote main at the baseline, no listener on 3000 or 8000.

**6. Validation**

Structural audit (section 7.1), all eight lines run before the gates: one `??` line and it is the new file · header `diff` against `messages.de.ts` EMPTY · `grep -c 'pluralIt('` = 3 · `^[^/]*plural` = one import plus three calls and nothing else · zero `aria-live` / `role="status"` · zero cast-shaped hits under `tail -n +8` · `git diff --check` clean · zero hits for the spaced-elision pattern.

The four frontend gates, from `frontend/`:

| gate | result |
|---|---|
| `npm run typecheck` | PASS, exit 0, no diagnostics — the completeness proof |
| `npx vitest run` | PASS, 467 passed / 3 skipped (32 files passed / 1 skipped) |
| `npm run lint` | PASS, exit 0 |
| `npm run build` | PASS, route table unchanged at eleven dynamic and zero static |

The vitest baseline was measured **before** the file existed and was identical (467 / 3), so "unchanged" is measured rather than assumed. `prompts.test.ts` did not go red. `i18n.test.ts` and `plural.test.ts` are inside that run and stayed green; no test was added or edited.

`npm run build` produces two separate claims and both hold: the build passed, **and** the code type-checks inside it (`Finished TypeScript in 1505ms`). The eleven dynamic routes are `/`, `/_not-found`, `/api/ai/judge`, `/api/ai/move`, `/api/models`, `/api/prompts`, `/draw/[id]`, `/game/[id]`, `/play`, `/settings`, `/waiting/[id]`.

Completeness was **not** hand-counted. `Record<TextKey, string>` and `{ [K in FnKey]: (typeof enFn)[K] }` make a missing key, an extra key and a wrong interpolation parameter all compile errors, and `tsconfig` `include` is `**/*.ts`, so the orphan is fully checked.

Recorded deviation: the five backend gates were not run. The diff is confined to `frontend/`, pytest collects only `backend/`, and mypy's scope is `config game gamecore accounts catalog`, so no backend gate observes this file.

Evidence posture is non-independent, as the tier specifies.

**7. Commit and push:** one non-force commit on `main`, `feat(i18n) the Italian interface catalog`, staged with the exact path only. Pre-push gate: `HEAD~1` = `490426a4274ea4a95915a935d5787a4a31f9a9c1` and `git ls-remote origin refs/heads/main` still `490426a…`. One `git push origin main`. Readback: local HEAD `6bf7c5e70cf82a32ab45db945019a7f42f039c42` = remote `refs/heads/main` `6bf7c5e70cf82a32ab45db945019a7f42f039c42`. Working tree clean; `.ap` untouched at `9c5cc44…`.

**8. Deviations, risks, missing evidence:** see `Flagged risks` and `Orchestration critique` below. No secret was read or printed. No network beyond the two authorized Git operations.

**9. Resolved Execution Issues / Near-Misses:** none. (One typo in my own `git commit` invocation was rejected by Git before any effect and re-issued correctly with hooks intact.)

**10. Pre-Existing Failure Classification:** none. The vitest run prints `[libretiles-provider-failure]` lines from deliberate provider-failure fixtures; they are expected fixture output in a passing suite and were present identically in the pre-change baseline.

---

## Terminology and choices

**The nine frozen terms** (the file's terminology block is their canonical home; stated once here):
tile `tessera` (f.) · letter `lettera` (f.) · rack `leggio` (m.) · blank `jolly` (m., invariable) · bag `sacchetto` (m.) · board = `tabellone` (the playing surface) **and** `partita` (a saved game) · pass `passare` (verb only) · points `punti`, abbreviated `pt.` · rival = opponent `avversario` (m.), one word.

All three mandated splits hold: `tabellone` / `partita`; `passare` ≠ `scambiare`; `jolly` ≠ `lettera`. I did **not** collapse tile and letter — Italian word-game usage genuinely keeps `tessera` (the piece) apart from `lettera` (the character it carries). `jolly` is always carried by the full `tessera jolly` or stands alone as a predicate noun, which is deliberate: it means no article ever precedes it, so the catalog never has to settle `il jolly` versus `lo jolly`.

**Register:** informal `tu`, second-person singular, subject pronoun dropped except where it carries contrast (`Inizi tu`). It matches every shipped catalog, and modern Italian UI never addresses a player with `Lei`.

**Label style:** second-person singular **imperative** for every control, action label, column heading and accessible name — `Gioca`, `Passa`, `Scambia`, `Annulla`, `Esci`, `Apri`, `Cerca`, `Invia`. That is what Italian UI actually does; the infinitive `Giocare` reads like a manual heading, not a button. I did not copy the three predecessors' infinitive. One campaign-level consequence: this is also the form the `tu` prose already uses, so in Italian the control style and the prose style **coincide** rather than contrast, and "never mixed inside one strip" is satisfied trivially.

**Pre-authorized exceptions used:** the pagination pair (`history.prev` `Precedente` / `history.next` `Successiva`, adjectives of the implied feminine `pagina`); the toggle state words (`settings.toggle.on` `Acceso` / `.off` `Spento`); and the badge words (`settings.board.active` `In uso`, an invariable phrase, plus `overlay.bestBadge`).

**The nine slot fillers**, three per site, four arguments at every call:

| site | one | other | many |
|---|---|---|---|
| `a11y.rackTile` | punto | punti | punti |
| `error.throttled.minutes` | minuto | minuti | minuti |
| `controls.tilesSelected` | tessera selezionata | tessere selezionate | tessere selezionate |

The third site **is a phrase**, not a word: an Italian predicate participle agrees in number, so `selezionata` cannot be appended outside the helper the way German appends `ausgewählt`. I departed from Portuguese's colon-label because the surface is a full-width centred line that wraps freely and is bounded by rack size 7, so the natural sentence fits and reads better. The `many` slot repeats the `other` word at all three sites — I took the recommendation. **Zero is `other` in Italian**, measured: `0 → other, 1 → one, 2 → other, 1000000 → many, 1000001 → other` on node v26.4.0 / ICU 78.3. This catalog writes `0 punti`; I did not carry over `messages.pt.ts:405-407`, whose `one` slot legitimately covers zero and produces `0 ponto`.

**The six protected-token prose sites:** `model` **translated** at `landing.card.ai.body` (`Partite premium con scelta del modello`) — on a landing card it is an ordinary noun and `modello` is unambiguous. All five `chat` sites **kept in English** (`a11y.chatInput`, `chat.title`, `chat.unavailable`, `game.toast.chatOffline`, `landing.card.queue.body`) — each names the product's chat panel the player matches against `chat.title`, and `la chat` is fully naturalized Italian regardless, so keeping it costs nothing.

**`AI` gender: FEMININE**, matching `l'intelligenza artificiale`. Visible at `game.giveUp.ai` as `dichiarata vincitrice`. Keeping the token English forces the elisions `l'AI`, `dell'AI`, `all'AI`, since it opens on a vowel however it is read; those appear about twenty times.

**The four fixed call sites of section 6.5 — all FOUR were HARMLESS for Italian.**
`game.aiPlayedFor.before`/`.points`: Italian puts the participle before the number and the counted noun after it, so `L'AI ha segnato 34 punti` fits the fixed middle span. `board.reset` + `board.zoomNoun`: Italian wants verb then object, so `Reimposta zoom` needs no workaround. `game.aWord` inside `game.toast.aiPlayedWord`: `una parola` carries the indefinite article and a real cited word needs none, so both readings work — the same choice German and Portuguese made, reached independently. `history.open`: the imperative `Apri` reads correctly as both column heading and button, and the alternate `Attuale` is gender-invariable. Four of four harmless, so on Italian evidence the wiring slice needs no call-site change. All four are commented at the key anyway, because the reason is language-specific.

---

## The twelve language names

`settings.gameVariant.*`, capitalized because these are standalone picker rows beside the capitalized endonyms; `game.lexicon.*` uses the same words **lowercase**, because Italian writes a language word lowercase in running text. In Italian the language noun and the language adjective are the same word, so the two families stay consistent for free.

| slug | `settings.gameVariant.*` | `game.lexicon.*` |
|---|---|---|
| english | Inglese | Non è nel Collins Scrabble Words 2019 |
| slovak | Slovacco | Non è nel lessico slovacco |
| czech | Ceco | Non è nel lessico ceco |
| polish | Polacco | Non è nel lessico polacco |
| afrikaans | Afrikaans | Non è nel lessico afrikaans |
| italian | Italiano | Non è nel lessico italiano |
| dutch | Olandese | Non è nel lessico olandese |
| german | Tedesco | Non è nel lessico tedesco |
| portuguese | Portoghese | Non è nel lessico portoghese |
| danish | Danese | Non è nel lessico danese |
| swedish | Svedese | Non è nel lessico svedese |
| icelandic | Islandese | Non è nel lessico islandese |

**Case-insensitive substring collisions, derived exhaustively over my own twelve strings: ZERO.** Confirmed programmatically (144 ordered pairs, 12 distinct lowercased values) and not merely inherited from the prompt. `Afrikaans` is byte-identical to English because Italian has no separate exonym — correct, not a missing translation, and commented as such. All twelve lexicon adjectives are correct masculine singular agreeing with `lessico`; `afrikaans` is the one invariable row.

---

## Flagged risks

**Terminology I am not certain of**
1. **`leggio` for `rack`** — the highest-uncertainty term in the catalog. I believe it is the Italian Scrabble/Scarabeo term for the tile stand, but I had no authorized way to verify it (no network, no corpus, no dictionary). If a native reads it as a music stand, `supporto` or `portalettere` are the alternatives.
2. **`tabellone` for the playing surface** — the traditional Italian Scrabble word; modern Italian board-gaming often prefers `plancia`. Both are correct Italian; I chose the traditional one.
3. `jolly` for `blank` — confident (the same Joker borrowing that gives Slovak and Czech `žolík`), but note the article question is only *avoided*, not settled. If a reviewer wants the bare noun anywhere, `il jolly` versus `lo jolly` reopens.
4. **No settled Italian noun exists for the pass MOVE.** `passo` is a step, `passaggio` is a sports pass. `game.toast.passRejected` is therefore phrased verbally, `Impossibile passare il turno` — the same class Icelandic hit with `passi`, rediscovered independently in an unrelated language.
5. `Risultati {from}-{to} di {total}` for `history.showing` drops the English counted noun, the way all four predecessors dropped it. `Risultati` never has to agree, but it reads slightly stiff on a one-row page.

**Labels I believe may overflow — all kept correct, none silently shortened**
6. **`overlay.bestBadge` `MIGLIORE` (8)** — the single highest risk. A `text-[10px] font-black shrink-0` pill beside a truncating candidate word and a score; German inferred a 3-character budget here. Kept correct rather than shortened to something that reads like untranslated English; `TOP` is the honest shorter fallback, named in the file.
7. **`board.dragToPan` `Trascina per spostare` (21)** on the tightest text surface in the product, sharing one `inline-flex max-w-full` pill with `board.pinchToZoom` (17) and `board.hide` (8). Flex does not wrap, so each span's text wraps and the pill grows in height rather than overflowing — degraded, not broken.
8. `history.unknownDate` `Non disponibile` (15 against the English 7), landing in ProfileModal's `text-[1.55rem] font-black` username slot.
9. `game.toast.passRejected` (28 against 13) in a `max-w-sm` toast heading; wraps to two lines.
10. `header.giveUpTooltip` `Arrenditi in questa partita` (27 against 20) in a `whitespace-nowrap` tooltip — inside the pt-PT (25) and Icelandic (30) range already shipped.
11. `controls.confirmExchange` `Conferma scambio` (16) equals the English 16 at `text-[1.42rem]`/`text-[1.46rem]` — at the same limit, not past it.
12. `settings.steps.50` (32) and `settings.timeout.120` (31) in the `minmax(132px,1fr)` / `minmax(170px,1fr)` choice cards — Italian descriptive settings copy expands exactly as section 5.5 predicted.
13. `game.blocker.auth.title` `Autenticazione dell'avversario non riuscita` (42 against 27).
14. `play.error.variantUnavailable` (146) and `settings.warn.accountSync` (141) are the longest strings in the catalog; both are wrapping prose blocks.

I cannot validate any of these myself — the file is orphaned and renders nowhere. Rendered acceptance is the Cooperator's after the wiring slice.

**Absent risks, recorded because an absent risk is as useful as a present one**
15. **`header.logout` is 4 characters (`Esci`)** — shorter than the English 6 and far shorter than pt-PT's 15. The non-wrapping header cluster *gains* room in Italian.
16. `controls.play` / `.pass` / `.exchange` are 5 / 5 / 7 against the English 4 / 4 / 8. The mobile three-column nowrap grid is not at risk.
17. `foldForSearch` is harmless for Italian, measured: `perché → perche`, `città → citta`, `più → piu`, `Però → pero`. No `EXPLICIT_SEARCH_FOLDS` entry is needed and nothing was rediscovered.
18. Layout risk overall is **medium, not high**, as section 5.5 predicted: elided phrases are compact and the control verbs are short; the expansion is confined to descriptive settings copy and error prose.

**Places agreement, elision or a fixed call site forced a construction English did not have — all commented at the key**
19. `history.unknownDate` — three dates (`data`, f.) and one username (`nome utente`, m.) share one value, so no gendered form works. Italian has a genuinely invariable answer: `disponibile` is an `-e` adjective with one form for both genders, hence `Non disponibile` rather than `Sconosciuto`/`Sconosciuta`.
20. **`game.gaveUp` — a trap the prompt's measured set does not contain.** Italian would say `ti sei arreso`, but a reflexive past participle agrees with the **subject**, here the player, whose gender the catalog cannot know. Resolved with `avere` + `perso` and the object following it, which is invariable: `Hai perso la partita per resa.` Every remaining Romance catalog will hit this class.
21. `draw.reason.closer` — invariable third-person `si avvicina` plus euphonic `ad A`, because the interpolated values are tile letters whose gender is unsettled.
22. `game.status.opponentPlaying` — invariable progressive gerund `sta giocando`, because `{name}` is opaque.
23. `controls.tilesSelected` — a two-word phrase inside the plural slots (see above).
24. `play.humanQueue.queueFor` and `picker.flagAlt` — colon forms, because an Italian preposition plus article cannot precede a value whose initial sound and gender are both unknown.
25. `history.outcome.*` — nouns and invariable phrases throughout, so nothing agrees with `partita` (f.) in the row and `Risultato` (m.) in the header.
26. `board.pts` `pt.` diverges from `game.aiPlayedFor.points` `punti`: the first is a 10px pill and the second is a sentence. Deliberate, commented, and raised as a LEAD below.

---

## Orchestration critique

### MEASURED

**M1 — Section 7.1, audit line 6 (the cast-shaped pattern), fires on the commentary section 4 *requires*. This is the fourth finding in that one line.**
`' as (const|unknown|any|never|string|number|Record|Partial|[A-Z][A-Za-z0-9_]*)\b'` matches any `" as "` followed by a capitalized word. Section 4 mandates comments that compare Italian against its predecessors, and the natural English for that is "as Portuguese did" / "as Icelandic uses". Demonstrated in a throwaway probe outside the repository: two false hits, zero casts. That line has now cost catalog 1 (the header's `as production quality`), catalog 2 (the Portuguese feminine article `as`), and this class — with the constraint that section 7.1's own general rule already names the fix: *an audit pattern aimed at code must not be runnable against the file's own mandated commentary.* Catalog 3 paid for exactly that correction on the `plural` line (`^[^/]*plural`) and it was never applied here. Remedy for the remaining four: scope this line the same way, `tail -n +8 "$F" | grep -nE '^[^/]*( as (const|unknown|any|…)…)'`. I audited the four shipped catalogs (`de`, `pt`, `is`, `sk`) against the line as written: all four are clean, but only because their authors happened to write "the way X did". My file avoids the phrasing too, so the audit passed as written — the defect is latent, not realized.

**M2 — Section 7.1's new Italian line cannot distinguish a defect from correct Italian.**
`grep -nE "[a-zA-Z]' [a-z]"` is meant to catch a spaced elision (`l' ora`). Italian **apocope** — `un po'`, `da'`, `va'`, `fa'`, `di'`, `sta'`, `be'`, `mo'` — is followed by a space **by rule**. Demonstrated: `Serve un po' di pazienza` is correct Italian and fires. It also fires on an English plural possessive in a required comment (`players' rack`). A pattern aimed at the actual eliding set returns zero on the same line:
`grep -nE "\b(l|un|dell|nell|all|dall|sull|coll|quest|quell|d|c|anch|sant|bell|grand|tutt|nessun|alcun|buon)' " "$F"`
My catalog contains no apocope, so the line returned zero and the property genuinely holds — but as written the check silently narrows the language: a future revision that legitimately wants `un po'` would be told it has an elision defect.

**M3 — Section 5.2's `settings.board.active` expectation does not hold for Italian, and the framing invites overstating it.**
Measured: the three surface labels are `Legno`, `Nero`, `Verde` — **all masculine** — so `Attivo` would in fact be correct today. Italian is the first of the three non-Slavic catalogs where that trap does not bite. I still chose the invariable `In uso`, for forward robustness rather than necessity, and said exactly that in the file. "Expect all of these" pushes a worker toward claiming a forced hand it does not have; "check whether each of these bites your language, and report either answer" would get the remaining four to the truth.

**M4 — One citation is off by one.** `OUTCOME_META` spans `GameHistoryPanel.tsx:36-75` (`};` at 75), not 36-74. The substantive claim is confirmed: exactly seven arms, no `unknown`, so `history.outcome.unknown` is dead.

**M5 — Section 6.1 undersells how dead the fourth argument is.** At all three sites the `many` slot is reachable only at exact non-zero millions; `a11y.rackTile` is bounded by a tile face value of 10 and `controls.tilesSelected` by rack size 7. So for two of the three sites the fourth argument is unreachable code the type system nevertheless demands. Saying that plainly stops a worker from spending care inventing a third form no product path can render.

**M6 — Everything else the prompt asserted, I measured and it held exactly.** The CLDR table (`0 → other, 1 → one, 2 → other, 1000000 → many, 1000001 → other`) on node v26.4.0 / ICU 78.3; all twelve `Intl.DisplayNames("it")` exonyms; `Intl.NumberFormat("it")` → `279.496` with a period; the corrected three-dates-one-username ratio at `GameHistoryPanel.tsx:97`, `ProfileModal.tsx:23`, `:26`, `:220`; tile letters at `draw-result.ts:29-30`; `Board.tsx:669`, `:671`, `:677`, `:692`, `:693`; `GameHistoryPanel.tsx:139` and `:295`; `page.tsx:338` and `:1003`; `ScorePanel.tsx:346`; `LOCALES` at four; the `i18n.test.ts` product-source walker at `:481-506`; and the vitest baseline of 467 / 3. The `foldForSearch` gap is real and irrelevant to Italian, exactly as stated — I did not rediscover it. I also confirmed against `messages.pt.ts:405-407` and `plural.ts:91-100` that Portuguese's `one` slot really does cover zero, so the warning not to reason by analogy is well aimed rather than theoretical.

### LEAD

**L1 — The skeleton never says whether `board.pts` and `game.aiPlayedFor.points` may diverge.** They are two keys for one concept at wildly different surfaces (a 10px pill against a 1.36rem sentence). I diverged — `pt.` and `punti` — and commented it; German and Icelandic used one form for both, Portuguese used two abbreviations. Unverified: whether any test or design note assumes they match. If divergence is sanctioned, say so in the remaining four prompts, or a reviewer will read a deliberate decision as an inconsistency.

**L2 — Section 5.3 assumes the control style and the prose style contrast, and for Italian they do not.** "Never mixed inside one strip" presupposes two distinguishable registers. Italian's UI imperative *is* the `tu` prose imperative. My unverified expectation is that Dutch, Danish, Swedish and Afrikaans collapse the same way, since their button convention is the bare stem/imperative too. If so, the instruction as written may push four workers into manufacturing a distinction their language does not have. I have not audited those four conventions.

**L3 — `messages.en.ts` has two shape problems that every remaining catalog will pay for again.** `history.unknownDate` carries two semantic roles under one key, and `history.outcome.unknown` is dead. Both are already known and both are queued separately. Sequencing judgement, not a measurement: one small `messages.en.ts` slice before catalog 8 would stop four more workers from independently re-solving them, and catalog 4 is where the cost becomes visibly repetitive rather than incidental.

**L4 — `overlay.bestBadge` has no stated character budget.** Section 5.3 pre-authorizes a shorter badge but never says how short. German inferred 3, Icelandic 5, Slovak ships 8, and I shipped 8 while flagging it. A measured budget — or one screenshot — would let the remaining four decide instead of each guessing differently at the same pill.

**L5 — `profile.memberSince` composes a label against a value that can degrade to `history.unknownDate`.** Italian needs the contracted `Membro dal` to read correctly with a formatted date, which then reads oddly against the degraded fallback. English has the same shape, so this is pre-existing rather than Italian-specific — but every remaining language with obligatory preposition-article contraction will meet it. Unverified whether the layout separates label and value enough for it not to matter; worth one line in section 5.2's measured set for the next four.

---

**Report justification:** `new-mutation`
**Logical-whole closure:** not-closed. Four of the eight catalogs remain, and the wiring slice that adds them to `LOCALES` is separate.
**Authority expiry:** my authority ends with this report. I have not begun a fifth catalog, added a locale, touched the wiring, or archived this prompt or report into Meta — that is the ORCHESTRATOR's.
**Smallest next step:** issue catalog 5 with M1 and M2 applied to section 7.1 (scope the cast-shaped line past comment lines; replace the elision line with the eliding-set pattern) and M3's "check whether it bites" framing applied to section 5.2.
**Context pressure:** moderate — roughly 2,600 lines of reference catalogs, the glossary and about a dozen call sites were read, with comfortable headroom remaining and no compaction.

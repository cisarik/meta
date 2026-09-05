# Deferred Cooperator acceptance batch — `13/00 multilingual-expansion-campaign`

Artifact class: **accumulating acceptance script. Evidence, not authority.**
Owned by the Orchestrator. Appended to at the moment each slice lands, never reconstructed
at the end.

## Why this file exists, and why it is owed

The Cooperator's standing instruction of 2026-09-03:

> *NECHCEM ABY SOM TU BOL AKO COOPERATOR POUZIVANY NA TESTOVANIE … CHCEM ABY SI PRACOVAL
> AUTONOMNE. OVEROVANIE … AZ NA KONCI VYVOJA. PROSIM PRETO MA NEVYRUSUJ.*

His observation is **deferred to the end of development**, delivered ONCE. The obligation
that creates: an acceptance step not run when it is generated must still be **written down**
when it is generated, or it will be reconstructed from memory at the end and be wrong.
`12/00` named this file as owed and did not open it. It is now open.

⛔ **Three things the autonomy grant does NOT waive, and protecting them is the
Orchestrator's job:**

```text
1  it does NOT lower an evidence tier. E3 still requires FRESH INDEPENDENT ACCEPTANCE, and
   that acceptance is a WORKER function, not a Cooperator function. Only his OBSERVATION is
   deferred. C1 is the only E3 slice in this campaign.
2  it does NOT remove the rendered-output rule: `for anything that renders, render it, or do
   not claim it`. Deferring his observation makes the Orchestrator's own loopback probe MORE
   necessary — production build, `next start` on a loopback port, HTTP client, stop by exact
   PID.
3  it does NOT touch decision 10 — he has no screen reader and will not install one.
   Accessibility claims are closed BY INSPECTION ONLY, permanently.
```

## Format

One entry per landed slice, appended at the moment it lands. Steps are labelled `B<n>-<m>`
so he can report a single failing step by name.

```text
slice        the internal identifier
commit       the exact SHA that landed it
what changed one line
steps        B<n>-<m>, each an EXACT observable expectation — what he does, and what he must
             see. Never "check that it works".
```

---

## B1 · exchange 01/01 — the deferred documentation chain

```text
slice        V9a + V9b
commits      4904e29  docs(prd): Collins 2019 replaces the stale SOWPODS references
             a199d0e  docs(env): document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override
             pushed; public readback equals local HEAD at a199d0e
what changed libretiles_PRD.md stops naming SOWPODS as the Tier-1 dictionary;
             backend/.env.example documents the PRIMARY_DICTIONARY_FILE knob; one new test
             module mechanically guards both claims.
```

```text
B1-1  Open libretiles_PRD.md. Search it for `SOWPODS`, case-insensitively.
      EXPECT: zero matches.
B1-2  Read FR-01 (section 5). EXPECT: it names the Collins 2019 dictionary and the word
      count 279,496 — not SOWPODS and not 172,823.
B1-3  Read FR-05 Tier 1 and Tier 2. EXPECT: Tier 1 names the local Collins 2019 list;
      Tier 2 no longer argues from SOWPODS being comprehensive.
B1-4  Read NFR-02. EXPECT: the O(1) frozenset lookup claim is about the Collins list.
B1-5  Read Known Gaps. EXPECT: the Tier-2 line no longer says "if SOWPODS is sufficient".
B1-6  Open backend/.env.example. EXPECT: a commented block explaining
      PRIMARY_DICTIONARY_FILE — that it repoints the English Tier-1 dictionary, that the
      default is collins2019.txt, that a value bypasses the variant manifest and the
      provenance machinery, and that it should normally be left unset. EXPECT the variable
      itself to be COMMENTED OUT, so copying the example changes no behaviour.
B1-7  ⛔ NEGATIVE STEP. Confirm backend/assets/dicts/sowpods.txt is STILL PRESENT.
      This exchange deliberately does not delete it. Its deletion is a later slice, and a
      prompt that both establishes an asset is unreferenced and deletes it in one exchange
      is the exact defect class that nearly destroyed a referenced asset in era 12.
B1-8  Run, from the repository root:
        cd backend && env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest \
            tests/test_documentation_dictionary_claims.py
      EXPECT: 2 passed. This is the mechanical half — if someone reintroduces the stale
      dictionary name or changes the shipped lexicon without updating the PRD, this fails.
```

⚠ **What this batch cannot show him.** Documentation changes render nothing in the running
product. B1 is a read-and-confirm batch by nature. The first entry with a rendered
expectation will be the first language slice, and it will carry the loopback-probe evidence
the rendered-output rule requires.

---

## B2 · exchange 02/01 — the orphan-asset guard

```text
slice        MEC-V3d-guard
commits      4f6f38d  chore(dicts): remove obsolete SOWPODS dictionary file   ⛔ COOPERATOR'S OWN
             86ec39e  test(lexicons): no unclaimed file may sit in the shipped dictionary directory
             pushed; public readback equals local HEAD at 86ec39e
what changed the deleted orphan can never silently return, and no other unclaimed file may sit
             in backend/assets/dicts/ either. P14 names the one file; P15 is the class rule.
```

```text
B2-1  Confirm backend/assets/dicts/ contains exactly EIGHT files and no sowpods.txt:
        collins2019.txt  czech.LICENSE  czech.txt  polish.LICENSE  polish.txt
        slovak.LICENSE   slovak.txt     slovak_two_tile_words.txt
B2-2  Run, from backend/ :
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest \
            tests/test_lexicon_provenance.py -k "p14 or p15"
      EXPECT: 2 passed.
B2-3  ⛔ THE ONE THAT MATTERS, and it is a NEGATIVE step. Read the docstring of
      test_p15_every_present_dictionary_file_is_claimed_by_a_manifest and confirm it states
      that the invariant runs ONE DIRECTION ONLY — present implies claimed, never the reverse.
      EXPECT the docstring to name Hungarian as the reason. If a future contributor
      "tightens" P15 into a symmetric check, the Hungarian variant can never ship, because its
      lexicon is deliberately claimed-and-absent until a local build runs.
B2-4  Optional, and it is the fastest way to see the guard work: create an empty file
        backend/assets/dicts/zzz_delete_me.txt
      run B2-2 again, EXPECT P15 to FAIL naming zzz_delete_me.txt, then DELETE that file and
      confirm `git status --porcelain=v1 -- backend/assets/` is empty again.
      ⚠ Delete it. Leaving it there leaves the suite red.
B2-5  Confirm `manage.py validate_lexicons` still reports FIVE assets, 0 failed. The deleted
      file was never one of the five — that is precisely why it could rot unnoticed.
```


---

## B3 · eight new playable languages — `153ead7` · `dab6d0d` · `0deac4a` · `1eed5ed` · `51e08fe` · `8a50ded`

```text
slices       Afrikaans · Italian · Dutch · German · Portuguese · Danish · Swedish · Icelandic
what changed twelve variants ship where four did. Every one has a committed build script pinned to
             one upstream commit, a licence read before a byte was written, and a byte-exact --check
             reproduction. ZERO engine changes across all eight.
```

⚠ **This is the batch with rendered output, and the rendered-output rule applies:** *for anything that
renders, render it, or do not claim it.* B3-1 is therefore the load-bearing step.

```text
B3-1  ⭐ THE ONE THAT MATTERS. Start both servers (backend on 8000, frontend on 3000), open Settings,
      and look at the game-language picker.
      EXPECT: TWELVE entries — English, Afrikaans, Czech, Danish, Dutch, German, Icelandic, Italian,
      Polish, Portuguese, Slovak, Swedish. English first, then the rest alphabetically by display name.
      EXPECT: the four original languages show their flag; the eight new ones show NO flag and their
      server-provided English name. That is BY DESIGN — variantDisplayName() falls back to the server
      display_name and flagSrc is omitted when absent, so a backend variant never needs a UI edit to
      appear. Confirm it looks acceptable rather than broken.
B3-2  Pick Afrikaans, start a game, play one word. EXPECT: it is accepted. 148 267 words.
B3-3  Pick German, and try to play a word containing Ä, Ö or Ü. EXPECT: accepted — those are 6-, 8-
      and 6-point TILES and 155 641 words keep one. ⛔ If an umlaut is rejected, the partial fold
      became total and roughly that many playable words were destroyed.
B3-4  Pick Portuguese. EXPECT the bag to be 120 tiles with THREE blanks, and a Ç tile worth 3 points.
      ⇒ This is the step that proves bag size and blank count are data-derived, not hardcoded.
B3-5  Pick Icelandic and play a word containing Ð, Þ or Æ. EXPECT: accepted. All ten of Icelandic's
      non-ASCII letters are tiles and NOTHING is folded.
B3-6  Confirm the four original languages are unchanged: English, Slovak, Czech, Polish all still
      playable, and a Slovak word with Á still accepted (Slovak does NOT fold diacritics).
B3-7  ⛔ NEGATIVE STEP. Confirm Norwegian, Finnish, French, Malay and Hungarian are ABSENT from the
      picker. Each is a recorded blocker with a named cause, not an oversight:
        norwegian  no explicit upstream licence grant for the word list
        finnish    no plain affix pair upstream (Voikko)
        french     the expander yields ~77k of ~400k words
        malay      no ms_MY source; Indonesian must not be substituted
        hungarian  ~301 M forms; needs an opt-in local build
B3-8  From backend/: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py validate_lexicons`
      EXPECT: `13 asset(s) audited, 0 failed`.
```

## B4 · C1a, the wire format — `529e691`

```text
slice        MEC-C1a-third
what changed a multi-code-point tile now crosses the game-state wire losslessly, on both the
             placement and the exchange path. The temporary adapter is gone.
```

⛔ **This slice is NOT accepted yet.** It is E3 and its fresh independent acceptance
(`06_acceptance_00.md`) had not returned when this entry was written. **If that acceptance has not
happened, do B4-1 and stop — do not treat the rest as confirmation.**

> ⭐ **RECONCILIATION, 2026-09-04, prospective and not a rewrite.** The acceptance HAS since run. It
> returned `status PASS · acceptance-PASS · zero corrections`, archived as `./06_report_00.md`, from a
> session that neither designed nor implemented the candidate and was not a subagent of the
> Orchestrator. ⇒ **B4-1 is SATISFIED and B4-2 through B4-4 are live.** The paragraph above is kept
> exactly as written because it was true when written — `AP.md:322-336`: historical artifacts stay
> interpretable and are never retroactively rewritten.
> ⚠ **B4-2 remains the ONLY pixel evidence this slice will ever get.** The acceptance independently
> confirmed that no test in the repository renders the board component. Your eyes are the instrument.

```text
B4-1  ⛔ FIRST: confirm the independent acceptance of 529e691 exists and PASSED. If it does not
      exist, this entry is not ready and nothing below it counts.
B4-2  Open any game and confirm the board renders normally — tiles in the right squares, blanks
      shown as blanks. ⚠ No test in the repository renders the board component, so YOUR EYES are the
      only evidence for the visual path. The independent acceptance prompt asks about exactly this.
B4-3  Place a word, submit it, reload the page. EXPECT: the board is unchanged after reload. That
      exercises the new structured payload end to end.
B4-4  ⛔ KNOWN LIMIT, so you are not surprised: no shipped language has a digraph tile yet, so
      nothing you can play today needs the new wire format. Hungarian is its first real consumer.
      B4-2 and B4-3 confirm the change did not BREAK anything; they cannot confirm it ENABLED
      anything. That is honest, not a gap in your testing.
```

## B5 · two Orchestrator-direct repairs, session 07 — `fffc613` · `32312ba`

```text
slice        two independent one-file repairs. ⛔ NEITHER is part of the UI-localization
             objective; both are measured defects the continuation handout named as cheap.
commits      fffc613  fix(lexicons) the audit's positive probes cover all twelve variants, not four
             32312ba  docs(agents) "Not done yet" said live Slovak play is not enabled, and it plays today
             pushed; public readback equals local HEAD at 32312ba
what changed `validate_lexicons` now probes real word membership for all twelve dictionaries
             instead of four, so "13 asset(s) audited, 0 failed" finally means presence, shape
             AND membership; and AGENTS.md no longer states that Slovak play is disabled.
⛔ ORCHESTRATOR-DIRECT, so this evidence is PERMANENTLY NON-INDEPENDENT: no Worker saw either
   change and no independent session verified it. Mechanical gates are the only corroboration.
```

```text
B5-1  From backend/: `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py validate_lexicons`
      EXPECT: `13 asset(s) audited, 0 failed` — exactly what B3-8 already expects.
      ⚠ THE OUTPUT IS DELIBERATELY UNCHANGED, and that is the whole point: the number was
      already green while eight of the twelve dictionaries had no membership probe at all. A
      passing audit cannot show you the difference, so B5-2 is the step that does.
B5-2  ⛔ THE STEP THAT ACTUALLY TESTS IT. Open
      backend/game/management/commands/validate_lexicons.py and read `_PRESENT_PROBES`.
      EXPECT: TWELVE rows, one per shipped variant — not four.
      Then, if you want to watch the guard fire, temporarily add `"madur"` to the `icelandic`
      row and re-run the command. EXPECT it to FAIL with
      `icelandic dictionary FAILED reason=probe_absent ... missing_probes=madur`. Remove it
      again. (`madur` is `maður` with a fold applied, and the Icelandic edition folds nothing,
      so its ABSENCE is the assertion. The same trick with `"musli"` on the `swedish` row also
      fails — Swedish ignores diacritics EXCEPT Ü.)
B5-3  Open AGENTS.md, section "Not done yet". EXPECT: no sentence claiming live Slovak play is
      not enabled. EXPECT instead one line stating that twelve variants ship playable and four
      have an interface locale. Cross-check the twelve against the Settings variant picker.
B5-4  ⛔ KNOWN LIMIT, stated so you are not surprised: README.md and libretiles_PRD.md STILL
      describe an English-only product and name no language other than English anywhere. That
      is campaign closure condition 11, deliberately deferred until the UI-localization work
      fixes the final numbers at twelve variants and twelve locales. Recorded debt, not an
      oversight.
```

⚠ **Numbering note for whoever appends next:** the eight interface catalogs get their own
entries from **B7 onward**, one per locale as it lands, per the standing obligation that an
acceptance step is written when it is generated and never reconstructed at the end.

## B6 · S1, the frozen interface key set and the CLDR plural pin — `cfd1215`

```text
slice        MEC-UIL-S1. The slice that had to come before the eight catalogs.
commit       cfd1215  feat(i18n) freeze the interface key set and pin twelve plural rules to CLDR
             pushed; public readback equals local HEAD at cfd1215
what changed the eight not-yet-localized variants now show a TRANSLATED NAME in Settings and in the
             human-queue label in all four existing locales, a rejected word finally names which of
             the twelve lexicons rejected it, and plural.ts carries a CLDR-correct helper for all
             twelve target languages with an executable test pinning each rule.
⛔ ORCHESTRATOR-DIRECT FINISH, so this evidence is PERMANENTLY NON-INDEPENDENT: a subagent Worker
   authored the implementation under prompt 07/01, correctly returned BLOCKED because that prompt was
   unsatisfiable, and I made the one-integer correction and landed it. No independent session saw it.
⛔ AND NO NEW INTERFACE LANGUAGE EXISTS YET. The chrome is still English for those eight. If you
   expect to find Danish menus, that is the NEXT slice, not this one.
```

```text
B6-1  Open Settings and look at the GAME VARIANT picker with the interface language on ENGLISH.
      EXPECT: twelve entries, and they read EXACTLY as before — Afrikaans, Italian, Dutch, German,
      Portuguese, Danish, Swedish, Icelandic among them, with no flag beside those eight.
      ⚠ THE ENGLISH VIEW MUST BE UNCHANGED. The eight new English values are byte-identical to the
      server names they replaced, so any visible difference here is a defect. Nothing to admire; this
      step exists to prove nothing broke.
B6-2  ⭐ NOW SWITCH THE INTERFACE LANGUAGE TO SLOVENČINA and look at the same picker.
      EXPECT: Afrikánčina · Taliančina · Holandčina · Nemčina · Portugalčina · Dánčina · Švédčina ·
      Islandčina, instead of the eight English names that were there before. That is the visible
      product change in this slice.
      Then switch to Čeština and to Polski and confirm the same eight are translated there too.
B6-3  Start a game in one of the eight — Danish is a good pick — and play a word that is NOT in that
      lexicon, with the interface on English.
      EXPECT: "Not in the Danish lexicon".  ⛔ NOT "Not in the game lexicon", which is what every one
      of those eight said before this commit.
      Repeat with the interface on Slovenčina. EXPECT: "Nie je v dánskom lexikóne".
B6-4  ⛔ THE ONE STEP ONLY YOU CAN ANSWER, and it is a QUESTION rather than a check.
      With the interface on Slovenčina, play an invalid word in the SWEDISH variant.
      It will say: "Nie je v švédskom lexikóne".
      ⇒ SHOULD THAT BE "vo švédskom"?  Czech vocalizes (`ve švédském`) and Polish vocalizes
        (`we włoskim`), and both match their own shipped rows. Slovak was left as plain `v` ONLY to
        stay consistent with the pre-existing "Nie je v slovenskom lexikóne", which has shipped for
        some time.
      ⇒ If `vo` is correct, then the OLD Slovak row is wrong too and it is a separate two-string fix.
        If `v` is correct, nothing changes. ⛔ Neither I nor the Worker is a native speaker and
        neither of us would guess. One word from you settles it, and it needs settling BEFORE the
        eight catalogs copy the pattern.
B6-5  ⛔ KNOWN LIMITS, so you are not surprised:
      · No new interface language exists. LOCALES is still en · sk · cs · pl.
      · No flags for the eight. That is your decision, not an omission.
      · The AI prompt still names only Slovak and Collins: ten of the twelve lexicons get a prompt
        that identifies neither their language nor their word list. Measured this session, recorded
        as its own future slice, and NOT part of this commit.
```

> ⭐ **RECONCILIATION, 2026-09-04, prospective and not a rewrite** (`AP.md:322-336`). **B6-4 is
> ANSWERED: `PASS`.** The Cooperator confirmed that Slovak `Nie je v švédskom lexikóne` is correct as
> shipped, so plain `v` is right and the pre-existing `Nie je v slovenskom lexikóne` needs no change
> either. ⇒ **The `v` / `vo` question is CLOSED and the eight later catalogs may copy the shipped
> Slovak pattern without reopening it.**
>
> ⭐ **AND THE WHOLE OF B6 IS NOW `PASS`, observed by the Cooperator himself.** He ran B6-1, B6-2,
> B6-3 and B6-5 and reported `PASS`. ⇒ `cfd1215` has what no other commit of this session has:
> **Cooperator-observed confirmation of rendered output**, which is the one evidence class no gate in
> this repository can produce and which the autonomy grant defers rather than waives. It does NOT make
> the slice independently accepted — the implementation was a subagent's and the correction was the
> ORCHESTRATOR's, so the evidence stays non-independent — but the rendered-output rule is satisfied for
> this slice and that is worth stating plainly.

## B7 · catalog 1 of 8 — the German interface catalog — `74e9d36`

```text
slice        MEC-UIL-C1-de. The first of eight, and the pilot for the prompt skeleton.
commit       74e9d36  feat(i18n) the German interface catalog
             pushed; public readback equals local HEAD at 74e9d36
what changed ONE new file, frontend/src/lib/i18n/messages.de.ts — 296 text keys and 20 function keys
             of German. ⛔ DELIBERATELY ORPHANED: `de` is NOT in LOCALES and nothing imports it.
⛔ THERE IS NOTHING TO SEE ON SCREEN YET, and that is by design. The German UI becomes reachable only
   in the WIRING slice, after all eight catalogs exist. If you look for a German menu today you will
   correctly find none.
⛔ NON-INDEPENDENT: a subagent Worker authored 316 strings of German that no native speaker and no
   gate has judged. The file says so in its own first seven lines.
```

```text
B7-1  Open frontend/src/lib/i18n/messages.de.ts and read the FIRST SEVEN LINES.
      EXPECT: a warning that the file is machine-authored and unreviewed, that it is presentation copy
      only, and that no lexicon entry or game rule is authored there.
      ⇒ Those seven lines are your condition for accepting eight languages of unreviewed copy, and
        they will be byte-identical in all eight files.
B7-2  Read the terminology comment block just below it. EXPECT eight German game terms — tile, letter,
      rack, blank, bag, board, pass, points — chosen once and used for all 316 strings.
B7-3  ⛔ THE STEP WORTH YOUR ATTENTION, AND IT IS DEFERRED UNTIL AFTER WIRING, NOT NOW.
      Two of those eight are judgement calls I decided rather than asking you, because they are
      reversible in one file:
        `Bank` for the rack   — attested in German Scrabble for a player's seven tiles, but
                                polysemous for a casual reader. Alternatives: Steinhalter, Ablage.
        `Blanko` / `Blankostein` for the blank — Mattel's German rules use it; casual German says
                                `Joker`, and Slovak and Czech both chose the joker word (`žolík`).
      ⇒ I kept the NATIONAL-ASSOCIATION term in both cases, because that is exactly what GLOSSARY D6
        does for Polish and Czech, and because copying Slovak's choice is what D6's "do not harmonize"
        forbids. ⚠ If you disagree, it is EIGHT WORDS IN ONE FILE. Say so when the German UI is
        reachable and you can see them in place.
B7-4  ⛔ KNOWN LIMITS, so you are not surprised:
      · Eight labels may overflow non-wrapping controls in German. They were kept CORRECT and flagged
        rather than shortened. The worst candidate is the board-variant description in Settings on a
        narrow phone. German is your FIRST priority when the locales are reachable.
      · "Reset Zoom" on the board reads backwards for German. The call site composes
        [action][noun] as two fixed spans, so the idiomatic order needs a component change, which was
        outside this slice's one-file allowlist. Recorded, not hidden.
      · `Die AI` rather than `die KI`, because `AI` is a protected product token. A German speaker
        would write KI. Changeable later as a product-vocabulary decision.
```

## B8 · catalog 2 of 8 — the European Portuguese interface catalog — `dd3b176`

```text
slice        MEC-UIL-C2-pt
commits      dd3b176  feat(i18n) the European Portuguese interface catalog
             3cfa13b  docs(i18n) record in the German catalog why aiPlayedFor uses the simple past
             pushed; public readback equals local HEAD at 3cfa13b
what changed ONE new file, messages.pt.ts — 296 text keys and 20 function keys of EUROPEAN Portuguese.
             ⛔ DELIBERATELY ORPHANED, exactly like German: `pt` is not in LOCALES.
             Plus a four-line comment backfilled into the German catalog, recording in the FILE why it
             had to abandon the perfect tense at one key. No German string changed.
⛔ STILL NOTHING TO SEE ON SCREEN. Two of eight catalogs exist; the UI becomes reachable at the wiring
   slice. Six languages remain: Icelandic, Italian, Dutch, Danish, Swedish, Afrikaans.
```

```text
B8-1  Open frontend/src/lib/i18n/messages.pt.ts and confirm the FIRST SEVEN LINES are byte-identical
      to the German catalog's — the machine-authored warning. `diff <(head -7 messages.pt.ts)
      <(head -7 messages.de.ts)` should print nothing.
B8-2  Read the terminology comment block. EXPECT nine Portugal-Portuguese terms, and note that
      `board` correctly became TWO words — `tabuleiro` for the playing surface, `partida` for a saved
      game — the same split Slovak already makes with `hracia plocha` / `partia`.
B8-3  ⛔ THE ONE THING WORTH KNOWING ABOUT THIS CATALOG, and it is invisible until you play.
      Portuguese CLDR makes ZERO SINGULAR: "0 ponto", not "0 pontos". Every other locale in this
      product says the plural at zero. When the Portuguese UI is reachable, let the AI pass a turn and
      look at the score: it should read a singular. ⇒ This is the one plural rule in the whole campaign
      that would have shipped visibly wrong if it had been copied from English.
B8-4  ⚠ TERMS THE WRITER ITSELF FLAGGED AS ITS WEAKEST, if you ever have a Portuguese reader:
      `suporte` for the rack (alternative: `estante`) · `Neerlandês` for Dutch (colloquially
      `Holandês`) · `Repor` for the board reset (alternative: `Reiniciar`).
B8-5  ⛔ KNOWN LIMITS: `Terminar sessão` is 15 characters where English is 6, on a non-wrapping pill
      in the game header — the highest overflow risk in this catalog, kept CORRECT rather than
      shortened to the imprecise `Sair`. And `A AI` takes feminine agreement because `AI` is a
      protected product token; a Portuguese reader would write `IA`.

## B9 · catalog 3 of 8 — the Icelandic interface catalog — `490426a`

```text
slice        MEC-UIL-C3-is
commit       490426a  feat(i18n) the Icelandic interface catalog
             pushed; public readback equals local HEAD at 490426a
what changed ONE new file, messages.is.ts — 296 text keys and 20 function keys of Icelandic.
             ⛔ DELIBERATELY ORPHANED like the other two. THREE of eight catalogs now exist:
             German, European Portuguese, Icelandic. Five remain.
```

```text
B9-1  Confirm the header is byte-identical to the other two:
      `diff <(head -7 messages.is.ts) <(head -7 messages.de.ts)` prints nothing.
B9-2  Read the terminology block. EXPECT nine Icelandic terms, and note two deliberate choices the
      writer flagged as its weakest: `jóker` for the blank (an Icelandic player may say
      `auður stafur`) and `grind` for the rack (`standur` and `rekki` are equally plausible).
B9-3  ⭐ Icelandic collapses TILE and LETTER into one word, `stafur`. That is a real divergence from
      German and Portuguese, which split them, and it is defensible — Czech and Slovak already differ
      from each other on the same term. Worth one look if you ever have an Icelandic reader.
B9-4  ⛔ TWO PRODUCT DEFECTS THIS CATALOG FOUND, both OUTSIDE its own file and both now queued as
      their own work. Nothing for you to do; recorded so the batch is honest:
      · The Settings language picker's SEARCH cannot fold `ð þ æ ß`. Typing `strasse` will not find
        `Straße` and `thyska` will not find `Þýska`. Latent today, live the moment the eight locales
        are wired. Being fixed before wiring.
      · `history.outcome.unknown` is a string twelve catalogs write and the product can never show —
        the saved-board table has no branch for it. Being removed with the wiring key change.

## B10 · catalog 4 of 8 — the Italian interface catalog — `6bf7c5e`

```text
slice        MEC-UIL-C4-it
commit       6bf7c5e  feat(i18n) the Italian interface catalog
             pushed; public readback equals local HEAD at 6bf7c5e
what changed ONE new file, messages.it.ts — 296 text keys and 20 function keys of Italian.
             ⛔ DELIBERATELY ORPHANED. FOUR of eight catalogs now exist: German, European Portuguese,
             Icelandic, Italian. Four remain: Dutch, Danish, Swedish, Afrikaans.
```

```text
B10-1 Confirm the header is byte-identical to the other three:
      `diff <(head -7 messages.it.ts) <(head -7 messages.de.ts)` prints nothing.
B10-2 Read the terminology block. Two terms the writer named as its least certain, and it had no
      authorized way to check either — no network, no dictionary, by design:
      · `leggio` for the tile rack. If an Italian reads it as a MUSIC stand, `supporto` is the
        alternative. Highest-uncertainty term in the catalog.
      · `tabellone` for the playing surface — the traditional Italian Scrabble word; modern Italian
        board-gaming often says `plancia`.
B10-3 ⛔ A DECISION I AM DEFERRING TO YOU RATHER THAN GUESSING, and it is one word.
      The AI overlay's "best move" BADGE is a 10-pixel pill beside a truncating word and a score. The
      four shipped catalogs each chose a different length for it: German 3 characters, Icelandic 5,
      Slovak 8, Italian 8 (`MIGLIORE`). ⇒ I refuse to invent a character budget from the CSS, because
      `text-[10px] px-1.5` does not honestly yield one. When the locales are reachable, look at that
      pill in Italian and in Slovak and tell me whether 8 characters fits. If it does not, every
      catalog has a shorter fallback already named in its own file.
B10-4 ⛔ KNOWN LIMITS: `MIGLIORE` (8 chars) is the single highest overflow risk in this catalog and was
      kept CORRECT rather than shortened to something that reads like untranslated English. And
      `header.logout` is `Esci` — FOUR characters, shorter than English, so the game header actually
      gains room in Italian.

## B11 · catalog 5 of 8 — the Dutch interface catalog — `57596e8`

```text
slice        MEC-UIL-C5-nl
commit       57596e8  feat(i18n) the Dutch interface catalog
             pushed; public readback equals local HEAD at 57596e8
what changed ONE new file, messages.nl.ts — 296 text keys and 20 function keys of Dutch.
             ⛔ DELIBERATELY ORPHANED. FIVE of eight catalogs exist: German, European Portuguese,
             Icelandic, Italian, Dutch. Three remain: Danish, Swedish, Afrikaans.
```

```text
B11-1 Confirm the header is byte-identical across all five:
      `diff <(head -7 messages.nl.ts) <(head -7 messages.de.ts)` prints nothing.
B11-2 ⭐ THE ONE THING WORTH KNOWING ABOUT THIS CATALOG, and it changed a decision of mine.
      Two of the four places where the code fixes word order BIT Dutch — the same two that bit German,
      because both languages put the verb last. I had already written down that three languages
      reporting "no problem" was enough to conclude the code needs no change. IT WAS NOT: those three
      were Portuguese, Icelandic and Italian, none of which is verb-final. The sample agreed because it
      shared the property the question was about.
      ⇒ Nothing to test. Recorded because it is the kind of wrong inference that is invisible when it
        succeeds.
B11-3 ⚠ Terms the writer named as its least certain: `letterbak` for the rack (a native may prefer
      `letterbakje`), `tegel` for the tile (Dutch players often say `steen`, which was rejected
      deliberately because it is the exact cognate of German's frozen `Stein`), and `joker` for the
      blank (`blanco` may be the more official Dutch Scrabble term).
B11-4 ⛔ KNOWN LIMITS: `board.reset` is `Herstel`, an imperative inside an otherwise fully infinitive
      control set — forced by the code, which composes `[action][noun]` in a fixed order that Dutch
      infinitives cannot satisfy. Commented in the file. And Dutch compounds make the board's zoom-hint
      pill the tightest surface again: 18 + 20 + 9 characters against English's 13 + 11 + 4.

## B12 · catalog 6 of 8 — the Danish interface catalog — `b0f8a28`

```text
slice        MEC-UIL-C6-da
commit       b0f8a28  feat(i18n) the Danish interface catalog
             pushed; public readback equals local HEAD at b0f8a28
what changed ONE new file, messages.da.ts — 296 text keys and 20 function keys of Danish.
             ⛔ DELIBERATELY ORPHANED. SIX of eight catalogs exist: German, European Portuguese,
             Icelandic, Italian, Dutch, Danish. Two remain: Swedish, Afrikaans.
```

```text
B12-1 Confirm the header is byte-identical across all six:
      `diff <(head -7 messages.da.ts) <(head -7 messages.de.ts)` prints nothing.
B12-2 ⛔ THE ONE THING IN THIS BATCH THAT IS A REAL BUG YOU CAN SEE, and it is NOT in the Danish file.
      The Settings language picker's SEARCH is already broken for two rows that shipped four catalogs
      ago. In the ICELANDIC interface, the German row reads `Þýska` and the Swedish row reads `Sænska`,
      and NO plain-ASCII typing finds either — thorn and æ cannot be folded by the code that folds
      search input, and nothing was added for them.
      ⇒ When the locales are reachable: switch the interface to Íslenska, open the game-variant picker,
        type `thyska`, then `saenska`. EXPECT both to find nothing. That is the defect.
      ⇒ Being repaired in its own commit before the wiring slice. Nothing for you to do now; this step
        exists so the batch is honest about a live defect rather than only about new work.
B12-3 ⚠ Terms the writer named as its least certain: `brikholder` for the tile rack (the shorter
      `brikbakke` is the alternative), `ordliste` for the lexicon (a deliberate departure from the
      cognate `leksikon`, which skews to "encyclopedia" in Danish), and whether `valgt` should inflect
      to `valgte` at plural tile counts.
B12-4 ⭐ A GOOD SIGN, recorded because it is evidence and not decoration: Danish needed NO workaround at
      any of the four places where the code fixes word order — the first catalog to clear all four with
      a structural reason rather than luck, and it keeps the natural perfect tense that German and Dutch
      both had to abandon. `Log ud` is also six characters, tying English, so the game header gains room.

## B13 · catalog 7 of 8 — the Swedish interface catalog — `fde3321`

```text
slice        MEC-UIL-C7-sv
commit       fde3321  feat(i18n) the Swedish interface catalog
             pushed; public readback equals local HEAD at fde3321
what changed ONE new file, messages.sv.ts — 296 text keys and 20 function keys of Swedish.
             ⛔ DELIBERATELY ORPHANED. SEVEN of eight catalogs exist. ONE REMAINS: Afrikaans.
```

```text
B13-1 Confirm the header is byte-identical across all seven:
      `diff <(head -7 messages.sv.ts) <(head -7 messages.de.ts)` prints nothing.
B13-2 ⭐ THE CHECK THAT PROVES THE NEAR-NEIGHBOUR DISCIPLINE WORKED, and it is one command. Danish landed
      one commit before Swedish and is the closest language in the set. Run:
        `grep -c 'æ\|ø' frontend/src/lib/i18n/messages.sv.ts`
      EXPECT: hits ONLY inside comment lines — the file names the Danish forms it deliberately did not
      reuse. `grep -cE '^[^/]*(æ|ø)'` should be ZERO. A single copied Danish word would show up there.
B13-3 ⛔ A DECISION I AM PUTTING TO YOU RATHER THAN SETTLING, and it is six strings.
      The project glossary lists seven words that stay in English in every catalog, `chat` among them.
      Every previous catalog kept it — but for German, Dutch and Danish the native word IS `chat`, so
      keeping it changed nothing. SWEDISH IS THE FIRST CASE WHERE IT CHANGES A BYTE: the Swedish noun is
      `chatt` with two t's. The Swedish catalog TRANSLATED it (`Partichatt`, `Chattmeddelande`) and
      explicitly invited reversal.
      ⇒ My reading: the glossary rule protects words that name a product concept a user matches against
        a control, and these six are prose. I let it stand. ⚠ But it is the first time the campaign has
        actually had to decide, and it is visible. When the Swedish UI is reachable, look at the chat
        panel title and tell me whether `Partichatt` or `Partichat` is right. Six strings either way.
B13-4 ⚠ Terms the writer named as its least certain: `blank` for the blank tile (it is also an ordinary
      Swedish adjective meaning glossy — `joker` was available and rejected as Danish's and Dutch's
      choice), and `Används` at the board-surface badge.
B13-5 ⭐ KNOWN GOOD, recorded because it is evidence: Swedish needed no workaround at any of the four
      places the code fixes word order, and it explained why in terms of North versus West Germanic
      rather than by agreeing with Danish. `BÄST` is four characters — cannot be read as untranslated
      English, because of the ä.

## B14 · catalog 8 of 8 — the Afrikaans interface catalog — `0a4fcc2`

```text
slice        MEC-UIL-C8-af — the LAST catalog. Eight of eight now exist.
commit       0a4fcc2  feat(i18n) the Afrikaans interface catalog
             pushed; public readback equals local HEAD at 0a4fcc2
what changed ONE new file, messages.af.ts — 296 text keys and 20 function keys of Afrikaans.
             ⛔ STILL DELIBERATELY ORPHANED, like the other seven. LOCALES is FOUR.
⛔ AND THIS ENTRY IS WRITTEN DIFFERENTLY FROM THE OTHER SEVEN, because this exchange had no report:
   the Worker finished the file and its delivery channel died before it could report. I verified the
   file myself — structure, the four Dutch-divergence greps, all four gates — and committed it
   orchestrator-direct. Every claim below is my measurement or the file's own comments, never a
   Worker's statement. Details in ./17_interruption_00.md.
```

```text
B14-1 Confirm the header is byte-identical across all EIGHT new catalogs:
      `for f in de pt is it nl da sv af; do diff -q <(head -7 frontend/src/lib/i18n/messages.$f.ts) \
         <(head -7 frontend/src/lib/i18n/messages.de.ts) || echo "$f DIFFERS"; done`
      EXPECT: no output at all.
B14-2 ⭐ THE CHECK THAT PROVES THE HARDEST DISCIPLINE IN THE CAMPAIGN WORKED. Afrikaans DESCENDS from
      Dutch, and messages.nl.ts was required reading — the closest trap of the eight. Three checks:
        grep -cE '^[^/]*\b(jouw|jij|je)\b' frontend/src/lib/i18n/messages.af.ts    → 0
        grep -cE '^[^/]*ij'                frontend/src/lib/i18n/messages.af.ts    → 0
        grep -cE '^[^/]*lijk'              frontend/src/lib/i18n/messages.af.ts    → 0
      All three are zero, verified by me. A single lifted Dutch word would show in one of them.
B14-3 ⭐ WORTH READING EVEN IF YOU READ NOTHING ELSE IN THIS BATCH. Open messages.af.ts and read the
      comment block above `afText` — about 120 lines. It is the only record of this catalog's reasoning
      that exists, because the report was lost, and it happens to be the best-documented file of the
      eight. It explains why `wedstryd` and not `party`, why `blokkie` and not `teël` or `steen`, and
      why the Afrikaans double negative `nie … nie` changes clause shape rather than words.
B14-4 ⭐ AND ONE THING THAT IS A GENUINE FINDING RATHER THAN A CHECK. The code composes the AI's score
      line as [text][score][text] in a fixed order. German and Dutch both had to abandon the natural
      perfect tense there because their participle goes last. Afrikaans has the same problem AND cannot
      use their escape — it has a simple past for only a handful of verbs. It used the present tense
      instead: "Die AI behaal 34 punte". ⇒ Three related languages, three different workarounds, for
      one call site. That call site is now a known constraint and it is queued for repair in the wiring
      slice rather than worked around a fourth time.
B14-5 ⛔ KNOWN LIMITS, and one is a real loss rather than a caveat:
      · The Worker's own list of strings it was least sure of DOES NOT EXIST. Every other catalog gave
        me sixteen to twenty-six flagged items; for Afrikaans the only risk signal is what it chose to
        comment in the file. If you ever have an Afrikaans reader, this is the catalog to look at
        hardest, precisely because it is the one nobody flagged.
      · No native speaker has read any of the eight. Each file's first seven lines say so.
      · STILL NOTHING TO SEE ON SCREEN. Eight catalogs exist; none is reachable. The wiring slice is
        next and it is where the twelve locales become real.

## B15 · the picker-search fold repair — `c9078f2`

```text
slice        MEC-UIL-FOLD. ⛔ NOT a new feature — a repair of a defect that shipped four catalogs ago.
commit       c9078f2  fix(i18n) picker search can fold æ þ ð ß œ ı
             pushed; public readback equals local HEAD at c9078f2
what changed frontend/src/lib/i18n/locales.ts — the search-fold table 6 → 16 entries, and the comment
             that wrongly claimed the list was complete. Plus the one existing fold test, 13 → 31
             assertions. NO new feature, NO new locale, LOCALES still four.
```

```text
B15-1 ⭐ THIS IS THE ONE STEP IN THE WHOLE BATCH THAT IS A BUG YOU COULD HAVE FOUND YOURSELF, and it
      shipped in the Icelandic catalog. It is B12-2 from the previous batch, now expected to PASS.
      ⇒ When the locales are reachable: switch the interface to Íslenska, open the game-variant picker,
        and type `thyska`, then `saenska`.
        BEFORE this commit: both found NOTHING. The German and Swedish rows were unreachable by any
        query typeable on a plain keyboard, because `Þýska` and `Sænska` contain letters the search fold
        could not convert.
        AFTER: `thyska` finds Þýska and `saenska` finds Sænska.
      ⚠ Nothing else about the picker changes. If either still finds nothing, that is a real regression
        and worth reporting immediately.
B15-2 ⚠ ONE SIDE EFFECT, measured and deliberate, so it does not surprise you. In the Icelandic picker,
      typing `enska` now matches FOUR rows instead of three — Enska, Hollenska, Íslenska and now Sænska.
      ⇒ That is not a bug and it is not new in kind: `enska` was already matching three rows, because in
        correct Icelandic "Enska" really is a substring of "Hollenska" and "Íslenska". Making Sænska
        findable at all necessarily makes it findable by that query too. A row went from unreachable to
        reachable, at the cost of one query being one row less selective.
B15-3 ⛔ WHAT IS NOT FIXED, and it is queued rather than forgotten: nothing yet PREVENTS this class of
      defect. There is no test asserting that every searchable label in every locale folds to plain
      ASCII, which is why this went unnoticed for four catalogs. That invariant is folded into the wiring
      slice, where all twelve locales become reachable and the assertion has a natural home.

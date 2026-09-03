# Language implementation ledger — `13/00 multilingual-expansion-campaign`

Artifact class: **Orchestrator-owned running ledger. Evidence, not authority.**

⛔ **Ownership.** The Cooperator's objective says *"the Worker should maintain a running
implementation ledger"*. A Worker's authority dies at its terminal report (RF-03,
`AP.md:111-117`), so a Worker cannot own an artifact that spans the campaign. **The
Orchestrator owns this file.** A Worker fills its own row and reports; the Orchestrator
writes it here.

Seeded 2026-09-03 at `ad4ce038e1bd3511bdd5b7431eb9c163d4788130`. Twenty-four candidate
entries — the Cooperator's verbatim target list, `00_handout.md` section 2.1. Nine columns,
exactly as he named them.

## Evidence labels — read this before trusting any cell

```text
MEASURED   I observed it in the checkout or by running a command in this project. A number
           here is a number somebody counted.
LEAD       plausible and useful, but NOT verified against a sourced authority. Every LEAD
           must become MEASURED or BLOCKED before its language ships.
INFERRED   my own reasoning from measured code, not an external fact.
UNSOURCED  no probe has been run. This is the honest default and it is NOT a defect.
```

⛔ **Standing condition 5 governs every `dictionary status` cell:** an unusable or unclear
licence is a DISQUALIFICATION and a recorded BLOCKER, never a footnote and never a Worker
judgement. **No synthesis, generation, translation, or model-authored word list. Not one
word from a language model.**

⛔ **Never copy a tile distribution from a neighbour language because it looks similar.**
Czech and Slovak are linguistically close and share **nothing** here. The sourcing standard
recorded at `PROJECT_CONTEXT.md:1270-1273` is a named national authority per language.

---

## Scan table

`GP` gameplay · `UI` locale · `DICT` lexicon · `DIST` distribution source ·
`CAP` capability required · `T` tests

```text
#   language      GP           UI          DICT              DIST        CAP        T
01  English       playable     shipped     MEASURED ok       MEASURED    none       yes
02  Slovak        playable     shipped     MEASURED ok       MEASURED    none       yes
03  Czech         playable     shipped     MEASURED ok       MEASURED    none       yes
04  Polish        playable     shipped     MEASURED ok       MEASURED    none       yes
05  Hungarian     not-started  staged      MEASURED too-big  UNSOURCED   C1         no
06  German        not-started  not-started UNSOURCED         UNSOURCED   C3         no
07  French        not-started  not-started UNSOURCED         UNSOURCED   C3         no
08  Italian       not-started  not-started UNSOURCED         UNSOURCED   none       no
09  Spanish       not-started  not-started UNSOURCED         UNSOURCED   C1 C4 C5   no
10  Portuguese    not-started  not-started UNSOURCED         UNSOURCED   none       no
11  Dutch         not-started  not-started UNSOURCED         UNSOURCED   none (C5?) no
12  Danish        not-started  not-started UNSOURCED         UNSOURCED   C3         no
13  Swedish       not-started  not-started UNSOURCED         UNSOURCED   C3         no
14  Norwegian     not-started  not-started UNSOURCED         UNSOURCED   C3         no
15  Finnish       not-started  not-started UNSOURCED         UNSOURCED   C3         no
16  Icelandic     not-started  not-started UNSOURCED         UNSOURCED   C3         no
17  Croatian      not-started  not-started UNSOURCED         UNSOURCED   C1         no
18  Slovenian     not-started  not-started UNSOURCED         UNSOURCED   C1         no
19  Turkish       not-started  not-started UNSOURCED         UNSOURCED   C2 C3      no
20  Greek         not-started  not-started UNSOURCED         UNSOURCED   C1         no
21  Bulgarian     not-started  not-started UNSOURCED         UNSOURCED   C1         no
22  Russian       not-started  not-started UNSOURCED         UNSOURCED   C1         no
23  Afrikaans     not-started  not-started UNSOURCED         UNSOURCED   none       no
24  Malay         not-started  not-started UNSOURCED         UNSOURCED   none       no
```

```text
playable  4 / 24        UI locales  4 / 24        rows needing a sourcing probe  20 / 24
```

⚠ **The critical path is the two UNSOURCED columns, not the CAP column.** Twenty rows need
a licence-and-authority probe before any of them can be scheduled. Five capabilities is a
handful of slices; twenty sourced distributions and twenty licence-clean lexicons is the
campaign.

---

## 01 · English

```text
language / variant     English. No `variant_name` declared, so display_label == "English".
                       MEASURED: variant_name is declared by NO shipped manifest.
gameplay status        playable. MEASURED: readiness "playable" from validate_lexicons +
                       the four-key payload at backend/game/views.py:156-165.
UI-localization        shipped. MEASURED: locales.ts:1 LOCALES includes "en"; DEFAULT_LOCALE
                       is "en"; messages.en.ts present; en.png present.
dictionary status      MEASURED ok. collins2019.txt, 279 496 words, duplicates 0, non_nfc 0.
                       The count agrees three ways: the file's own header line, the
                       validate_lexicons audit, and english.json entry_count.
                       ⚠ CRLF endings, a header line, a blank second line, and NO trailing
                       newline. Do not repeat `wc -l` (279 497) as a word count.
                       Licence: Collins 2019, no .LICENSE file and no SPDX in the manifest —
                       provenance carries upstream only. Recorded, not resolved.
distribution source    MEASURED in-manifest: 27 letter rows, 100 tiles, 2 blanks,
                       alphabet_order 26, every alphabet letter has a tile.
                       The standard English distribution. source "builtin".
special-rule reqs      none. No forbidden_token_sequences, no two_tile_words_file.
capability required    none.
tests                  backend/tests/test_gamecore.py · test_dictionary_validation.py ·
                       test_variant_invariants.py (74 tests) · test_lexicon_provenance.py ·
                       test_lexicon_health.py · frontend i18n.test.ts ·
                       test_documentation_dictionary_claims.py (NEW at 4904e29 — D1 guards
                       that the PRD never names an unshipped dictionary; D2 binds the word
                       count the PRD publishes to english.json's provenance entry_count)
blockers               none for gameplay. TWO documentation debts DISCHARGED in exchange
                       01/01: libretiles_PRD.md now names Collins 2019 with 279,496 words
                       (4904e29), and PRIMARY_DICTIONARY_FILE is documented in
                       backend/.env.example (a199d0e).
                       ⚠ ONE RESIDUAL HAZARD, measured and open: NO gate anywhere would
                       notice a PRIMARY_DICTIONARY_FILE override. validate_lexicons and
                       test_lexicon_provenance both audit the MANIFEST path, so an override
                       changes what submit_move validates against while every asset gate
                       keeps reporting english ok words=279496. Documented, not detected.
                       🐞 mle-01-F02, severity low, confirmed.
                       ⚠ backend/assets/dicts/sowpods.txt is GONE — deleted by the Cooperator
                       himself at 4f6f38d, and guarded at 86ec39e by P14 (that one file may
                       never return) and P15 (⛔ ONE DIRECTION: every file PRESENT under
                       assets/dicts/ must be CLAIMED by a manifest, never the reverse).
                       ⇒ assets/dicts/ is now EXACTLY manifest-claimed: eight files, eight
                       claims, zero orphans, zero claimed-but-absent. Measured twice.
```

## 02 · Slovak

```text
language / variant     Slovak. Playable hunspell-sk expansion — explicitly NOT SSS-official.
                       A separate SSS 100 variant manifest exists.
gameplay status        playable. MEASURED via validate_lexicons and the harness.
UI-localization        shipped. MEASURED: "sk" in LOCALES, messages.sk.ts, sk.png, pluralSk.
dictionary status      MEASURED ok. slovak.txt 3 005 250 words, duplicates 0, non_nfc 0.
                       slovak_two_tile_words.txt 103 words, ok.
                       Reproducible: build_slovak_lexicon.py, upstream LibreOffice
                       dictionaries @75f5dff8c972fff4a32e4ea8434722c277f02a3f, expander
                       hunspell 1.7.3, --check IDENTICAL on both artifacts — RE-PROVED BY ME
                       2026-09-03. slovak.LICENSE 67 811 B committed.
distribution source    MEASURED in-manifest: 42 letter rows, 100 tiles, 2 blanks,
                       alphabet_order 46. FIVE alphabet letters have no tile: DZ DŽ CH Q W.
                       Authority of record: JÚĽŠ SAV (PROJECT_CONTEXT.md:1270-1273).
special-rule reqs      two_tile_words_file — Slovak needs an explicit short-word authority.
                       A≠Á is a LOCKED FORK: Slovak does NOT fold diacritics. ⛔ C3 must not
                       be applied here; absence of a normalization field must keep today's
                       behaviour exactly.
capability required    none. Single-code-point tiles, so the F2b wire adapter carries it.
tests                  test_slovak_variant.py · test_slovak_engine.py ·
                       test_slovak_full_game.py · test_slovak_ranked_search.py ·
                       test_variant_invariants.py · i18n.test.ts
blockers               none for gameplay. Settings/engine/prompt wiring for live Slovak play
                       is a later slice of `slovak-playable-variant` and is NOT this campaign.
```

## 03 · Czech

```text
language / variant     Czech.
gameplay status        playable. MEASURED.
UI-localization        shipped. MEASURED: "cs" in LOCALES, messages.cs.ts, cs.png.
                       pluralCs == pluralSk, deliberately (i18n GLOSSARY.md:51-53).
dictionary status      MEASURED ok. czech.txt 3 930 497 words / 54 105 021 B, duplicates 0,
                       non_nfc 0. Reproducible by build_czech_lexicon.py from a pinned
                       upstream; czech.LICENSE 72 790 B committed.
                       ⚠ This file already drew a GitHub large-file warning. It is the
                       practical ceiling for a COMMITTED lexicon in this repository.
distribution source    MEASURED in-manifest: 40 letter rows, 100 tiles, 2 blanks,
                       alphabet_order 42. THREE alphabet letters have no tile: CH Q W.
                       Authority of record: Ústav pro jazyk český.
special-rule reqs      no two_tile_words_file. Diacritics are distinct, as in Slovak.
capability required    none.
tests                  test_czech_polish_variants.py · test_variant_invariants.py ·
                       test_lexicon_provenance.py · i18n.test.ts
blockers               none.
```

## 04 · Polish

```text
language / variant     Polish.
gameplay status        playable. MEASURED.
UI-localization        shipped. MEASURED: "pl" in LOCALES, messages.pl.ts, pl.png, pluralPl.
                       ⚠ pluralSk is WRONG for Polish at 22, 23, 24, 122… — pluralPl exists
                       for that reason and must not be folded into pluralSk.
dictionary status      MEASURED ok. polish.txt 3 721 704 words / 51 607 141 B, duplicates 0,
                       non_nfc 0. Reproducible by build_polish_lexicon.py from a pinned
                       upstream (sjp.pl / hunspell-pl generated 2017-05-14);
                       polish.LICENSE 30 427 B committed.
distribution source    MEASURED in-manifest: 33 letter rows, 100 tiles, 2 blanks,
                       alphabet_order 32 — EVERY alphabet letter has a tile.
                       Authority of record: Rada Języka Polskiego.
special-rule reqs      none measured.
capability required    none.
tests                  test_czech_polish_variants.py · test_variant_invariants.py ·
                       test_lexicon_provenance.py · i18n.test.ts
blockers               none.
```

## 05 · Hungarian

```text
language / variant     Hungarian.
gameplay status        not-started. BLOCKED on C1: Hungarian is the first target language
                       with digraph TILES, and the seven-guard F2b freeze stands.
UI-localization        staged, not implemented. MEASURED: frontend/public/hu.png EXISTS
                       while LOCALES has no "hu" and there is no messages.hu.ts.
                       ⇒ B1's UI half inherits a flag asset, not a gap.
                       ⚠ RECLASSIFIED 2026-09-03: hu.png is not merely pre-staged, it is an
                       ORPHAN — zero references anywhere in frontend/src or the configs,
                       measured twice. It is the same defect shape as the deleted sowpods.txt:
                       an asset in the tree that nothing claims. DECISION: keep it and let the
                       Hungarian slice CLAIM it, rather than delete and re-add an identical
                       file. B1 must add the flag-map entry that claims it.
dictionary status      MEASURED and it does NOT fit. 12/00/90_hungarian-expansion-probe.md,
                       non-independent, fourteen sections:
                         ~4.27 BILLION non-compound forms  (~77 GB)
                         ~301 MILLION even at a 15-code-point ceiling  (~4.5 GB)
                       The expander WORKS — Spylls 0.1.7 resolves the 1 559-entry AF alias
                       table that defeats the C unmunch; gates 6/6 and 23/23; hunspell 1.7.3
                       accepted 3 000 of 3 000 sampled forms.
                       ⚠ 100 % oracle agreement proves no OVER-generation. It says nothing
                       about under-generation; completeness rests on 29 hand-checked forms.
                       DECISION D, taken under the autonomy grant and CONFIRMED by the
                       Cooperator 2026-09-03: commit build_hungarian_lexicon.py plus its
                       pinned source hashes, generate locally at setup, GITIGNORE the output,
                       readiness reports `unavailable` until the local build has run.
                       ⛔ Three options are REJECTED, do not re-propose: committing the full
                       list (LFS forbidden); a runtime spell-checker per lookup (kills the
                       prefix probe, and the engine authors EVERY move, so it would disable
                       Hungarian AI rather than degrade it); a frequency-bounded subset (no
                       licence-clean frequency source, and it makes the lexicon a judgement
                       call).
distribution source    UNSOURCED. Authority of record named by the chain: MTA. Not fetched,
                       not verified. LEAD only: the digraph tiles expected are
                       CS GY LY NY SZ TY ZS, and six alphabet letters are expected to have no
                       tile (DZ DZS Q W X Y). ⛔ Both are LEADS and neither may become a
                       manifest without a sourced authority.
special-rule reqs      LEAD: digraph tiles mean forbidden_token_sequences is likely needed so
                       two S tiles cannot spell an SZ. The field ALREADY EXISTS and is
                       checked against complete formed words only — no engine change.
                       MEASURED: the code-point ceiling must be DERIVED from the 15-tile
                       board bound and the real tile set, declared in the manifest, and
                       justified in writing. 15 is too tight once DZS is a tile.
capability required    C1 — multi-code-point tiles end to end. Non-negotiable.
tests                  none yet. Inherited conditions this row must satisfy:
                         09  the fixture passes with at least TWO different multi-character
                             tokens, not only SZ
                         10  the L·L synthetic canary still passes
                         11  playable after an opt-in local build; `unavailable` BEFORE it
                             WITHOUT crashing — both halves proved by test
                         15  the code-point ceiling derived, declared, justified
                         16  the six-word gate asserted BY THE BUILD SCRIPT as a fail-closed
                             post-condition
                         17  an `unavailable` variant made UNSELECTABLE at the three server
                             sites — MEASURED open, see 00_notes.md section 3.3
                         18  the audit is STREAMING or sorted-adjacency, never an in-memory
                             set. MEASURED: the current check holds 3.9 M tokens at ~500 MB;
                             301 M would need ~40 GB.
blockers               C1 not landed · distribution UNSOURCED · the lexicon exceeds any
                       committable size, handled by decision D rather than open ·
                       it becomes the first gitignored asset under backend/assets/dicts/,
                       so the .gitignore entry and the fail-closed readiness path must be
                       tested TOGETHER.
```

## 06 · German

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: ß plays as SS, but Ä ≠ A, Ö ≠ O, Ü ≠ U. That asymmetry is the
                       whole reason C3 must be a DATA-DEFINED rule and never a global
                       strip_diacritics().
capability required    C3 — variant-declared normalization.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED · C3 not landed.
```

## 07 · French

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: accented vowels play as their base letter (É plays as E). This
                       is the OPPOSITE of the shipped Slovak and Czech fork, which is why
                       C3's absence must mean today's behaviour exactly.
capability required    C3.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED · C3 not landed.
```

## 08 · Italian

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: none expected. Single-code-point tiles, no folding, no
                       multigraph. A B2 candidate.
capability required    none INFERRED — the shipped foundation should carry it unchanged.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED.
```

## 09 · Spanish

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED. ⚠ This is the row that needs a RULESET, not just a
                       distribution: international, North American and Latin-American
                       editions differ. LEAD.
special-rule reqs      LEAD: CH, LL and RR as tiles ⇒ forbidden_token_sequences, which
                       already exists as a declared field.
                       MEASURED: `variant_name` exists at variant_store.py:82, feeds
                       display_label at :108-112, and is declared by NO shipped manifest —
                       so that code path is unexercised by any test in the repository.
capability required    C1 (multigraph tiles on the wire) · C5 (ruleset identity) ·
                       C4 only if a face-versus-lexical realization is genuinely needed.
tests                  none. C5 must give display_label its FIRST test.
blockers               distribution UNSOURCED · which ruleset ships is undecided ·
                       lexicon licence UNVERIFIED · C1 and C5 not landed.
```

## 10 · Portuguese

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED. LEAD: 120 tiles and THREE blanks.
special-rule reqs      LEAD: none beyond the tile set.
capability required    none INFERRED. MEASURED support: total_tiles is DERIVED at
                       variant_store.py:104-106 and is not a manifest field, so a 120-tile
                       bag with three blanks needs no code change.
                       ⇒ This row is the STRONGEST TEST that bag size and blank count are
                       truly data-derived. Worth scheduling for that reason alone.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED.
```

## 11 · Dutch

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: the historical IJ tile was removed from the modern edition, so
                       WHICH edition ships is a real question and may want C5.
capability required    none for the modern edition INFERRED · C5 if two editions ship.
tests                  none.
blockers               distribution UNSOURCED · which edition ships is undecided ·
                       lexicon licence UNVERIFIED.
```

## 12 · Danish

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: Æ Ø Å are distinct LETTERS with their own tiles, not folded
                       vowels. ⚠ That makes Danish a C3 row only if the sourced rules
                       actually require folding — it may need NOTHING. Do not assume.
capability required    C3 pending measurement; possibly none.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED.
```

## 13 · Swedish

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: Å Ä Ö are distinct letters with their own tiles. Same caution as
                       Danish — it may need no folding at all.
capability required    C3 pending measurement; possibly none.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED.
```

## 14 · Norwegian

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run. ⚠ Bokmål and Nynorsk are two written
                       standards; which one the lexicon covers is part of the probe.
distribution source    UNSOURCED.
special-rule reqs      LEAD: Æ Ø Å distinct, as in Danish.
capability required    C3 pending measurement; possibly none · C5 if two standards ship.
tests                  none.
blockers               distribution UNSOURCED · Bokmål vs Nynorsk undecided ·
                       lexicon licence UNVERIFIED.
```

## 15 · Finnish

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED, and ⚠ THIS IS THE ROW TO WATCH. Finnish is agglutinative
                       and NOBODY HAS MEASURED ITS EXPANSION SIZE. Hungarian — also
                       agglutinative — measured ~301 million forms at the tightest defensible
                       bound. ⛔ An expansion-size estimate must be produced BEFORE Finnish
                       is scheduled, and if it exceeds a committable size it takes decision
                       D's route: committed build script, gitignored output, `unavailable`
                       until the local build has run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: Ä and Ö are distinct letters with their own tiles.
capability required    C3 pending measurement; possibly none.
tests                  none.
blockers               distribution UNSOURCED · expansion size UNMEASURED and plausibly
                       uncommittable · lexicon licence UNVERIFIED.
```

## 16 · Icelandic

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: Þ Ð Æ Ö and the accented vowels are distinct letters with their
                       own tiles. ⚠ G7 — font glyph coverage — becomes live here as well as
                       at Greek and Cyrillic.
capability required    C3 pending measurement; possibly none.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED ·
                       glyph coverage unverified (G7).
```

## 17 · Croatian

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: DŽ, LJ and NJ as tiles ⇒ digraph tiles on the wire, plus
                       forbidden_token_sequences so D+Ž cannot spell DŽ. The field EXISTS.
                       ⇒ Croatian is the second multigraph language after Hungarian and the
                       cheapest confirmation that C1 generalized rather than special-cased.
capability required    C1.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED · C1 not landed.
```

## 18 · Slovenian

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: Č Š Ž are distinct single letters; whether any digraph is a TILE
                       is part of the probe. It may need nothing beyond today's foundation.
capability required    C1 pending measurement; possibly none.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED.
```

## 19 · Turkish

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD, and it is the sharpest case on the whole list:
                         I and İ are DIFFERENT LETTERS. Turkish casing is not Unicode
                         default casing — `"i".upper()` is "I" in Python but must be "İ" in
                         Turkish. ⛔ canonicalize_tile_token uses plain .upper()
                         (MEASURED, variant_store.py:176-185), so Turkish is the language
                         that will discover whether that helper is language-neutral enough.
                         LEAD: Â Î Û play as A, İ, U.
                         LEAD: blank may not be assigned to Q, W or X — Turkish has no such
                         letters, and a RESTRICTION cannot be expressed by derivation.
capability required    C2 — variant-declared blank targets, MEASURED absent (`blank_targets`
                       returns 0 hits under BOTH `git grep -n` and `git grep -in`) ·
                       C3 — variant-declared normalization.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED · C2 and C3 not
                       landed · the .upper() question above is UNRESOLVED and must be
                       measured before Turkish is scheduled.
```

## 20 · Greek

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED. LEAD: 104 tiles.
special-rule reqs      LEAD: final sigma ς versus σ is a real normalization question, and
                       accented vowels (ά έ ή ί ό ύ ώ) are ordinarily written unaccented on
                       tiles. Both are DATA questions, not engine questions.
capability required    none new IF C1 has landed. INFERRED from the handout's own point,
                       which I share: once `[A-Z]` and `len == 1` assumptions are gone,
                       Greek is EASIER than Hungarian. ⛔ Do not treat non-Latin as the hard
                       part.
                       ⚠ G7 — font glyph coverage — is live here.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED ·
                       glyph coverage unverified (G7).
```

## 21 · Bulgarian

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: Cyrillic, single-code-point throughout.
capability required    none new if C1 landed. INFERRED.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED ·
                       glyph coverage unverified (G7).
```

## 22 · Russian

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run. ⚠ Russian is highly inflected; an
                       expansion-size estimate belongs in the probe, as with Finnish.
distribution source    UNSOURCED. LEAD: 104 tiles.
special-rule reqs      LEAD: Ё versus Е is a normalization question. Й, Ъ, Ь are distinct
                       letters.
capability required    none new if C1 landed. INFERRED.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED ·
                       expansion size UNMEASURED · glyph coverage unverified (G7).
```

## 23 · Afrikaans

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: none. Latin alphabet, single-code-point tiles, no multigraph
                       tile, no folding expected.
capability required    none INFERRED.
                       ⇒ ONE OF THE TWO CHEAPEST ROWS ON THE LIST. Scheduled FIRST, with
                       Malay, because proving "adding a language is boring" on real data is
                       worth more before the one E3 slice than after it. If it is NOT boring,
                       that is the most valuable finding available and it is far cheaper to
                       learn here than inside C1.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED.
```

## 24 · Malay

```text
gameplay status        not-started.
UI-localization        not-started.
dictionary status      UNSOURCED. No probe run.
distribution source    UNSOURCED.
special-rule reqs      LEAD: none. Latin alphabet, no diacritics in standard orthography,
                       no multigraph tile expected.
capability required    none INFERRED.
                       ⇒ THE OTHER CHEAPEST ROW. Same reasoning as Afrikaans.
tests                  none.
blockers               distribution UNSOURCED · lexicon licence UNVERIFIED.
```

---

## Capability status, cross-referenced

```text
C1  multi-code-point tiles end to end        OPEN. tier E3. Needed by: hu hr es (and sl?).
                                             Enables: el bg ru without further work.
                                             MEASURED: seven F2b guards still in place.
C2  variant-declared blank targets           OPEN. tier E2. Needed by: tr.
                                             MEASURED absent: `blank_targets` 0 hits under
                                             both grep cases.
C3  variant-declared normalization           OPEN. tier E2. Needed by: de fr tr, possibly
                                             da sv no fi is.
                                             MEASURED: the hook EXISTS —
                                             word_authority.py:66 takes `normalize` per
                                             instance. No manifest field selects it.
                                             ⛔ Absence must mean today's behaviour exactly.
                                             sk/cs/pl do NOT fold. That is a LOCKED fork.
C4  face versus lexical realization          OPEN. tier E2. Needed by: NO language on this
                                             list. MEASURED: lexical_contribution() and
                                             tile_display() exist as identity at
                                             variant_store.py:137-143.
                                             ⇒ Design the field so multi-realization is not
                                             PRECLUDED, and BUILD NOTHING for it.
C5  ruleset identity                         HALF-PRESENT. tier E1. Needed by: es, possibly
                                             nl and no.
                                             MEASURED: variant_name exists at :82 and feeds
                                             display_label at :108-112, declared by no
                                             shipped manifest, so that branch is untested.
--  RTL                                      ⛔ OUT OF SCOPE. Hebrew, Arabic and Thai are
                                             deliberately absent from the target list because
                                             RTL and multi-realization tiles are genuinely
                                             separate architectural boundaries, and clause 7
                                             of the objective stops the campaign at exactly
                                             such a boundary. Record observations; build
                                             nothing; do not let a Worker generalize "for RTL
                                             later".
```

## What closing this ledger requires

```text
1  every one of the twenty-four rows has all nine columns filled
2  every language that CAN ship under standing condition 5 IS playable, with its UI locale
   where practical
3  every language that CANNOT is a recorded blocker naming the EXACT missing thing —
   distribution source, licence, or architectural boundary
```

⚠ **Twenty of twenty-four with four well-evidenced blockers is a SUCCESS.** Twenty-four
claimed by shipping a lexicon nobody can license, or a distribution nobody sourced, is a
failure that looks like a success — and the Cooperator is presenting this at a job
interview. Do not soften row 3.

# Research brief — a redistributable, fully inflected Hungarian word list for a Scrabble-style game engine

You are a **read-only research assistant**. Produce a sourced report. Do not write code, do not produce a word list yourself, and do not generate, translate, or invent any Hungarian words. Every factual claim must carry a URL, a version or commit identity, and the date you retrieved it.

If the honest answer to a question below is "no such thing exists under an acceptable licence", say that plainly. A well-evidenced negative answer is a **fully successful** outcome of this brief and is more useful than an optimistic maybe.

## 1. Context — what already works, and the exact thing that does not

A Scrabble-like web game needs one plain-text lexicon file per language: UTF-8, one lowercase word per line, sorted, no affix compression, no morphological annotation. It is loaded into memory as a set plus a sorted prefix index, and it answers two questions millions of times per game: *is this exact string a word*, and *does any word start with this prefix*.

Three languages already work, all built the same way:

```text
source     LibreOffice "dictionaries" repository, pinned commit 75f5dff8c972fff4a32e4ea8434722c277f02a3f
method     download <lang>.dic + <lang>.aff, then expand with the hunspell tool `unmunch`
filter     NFC normalize, casefold, keep only entries that are alphabetic and at least 2 characters
result     Slovak 3 005 250 words · Czech 3 930 497 · Polish 3 721 704
licences   Slovak GPL-2.0 / LGPL-2.1 / MPL-1.1 · Czech GPL-2.0 · Polish GPL / LGPL / MPL / Apache-2.0 / CC-SA
```

**The same method fails for Hungarian, and the failure is measured, not suspected.**

```text
hu_HU.dic stem count        96 955
unmunch stdout lines        96 940      <- essentially the stem list, unexpanded
unique words after filter   81 509      <- versus 3 005 250 for Slovak
hu_HU.aff contains          ~24 303 SFX lines, 370 PFX lines, COMPOUNDFLAG Y, COMPOUNDMIN 1
```

Direct membership test against the produced list:

```text
present   ház, házak, kutya, asztal
ABSENT    házat, házban, házakat, kutyát, kutyák, szeretem, asztalon
```

Ordinary case endings are missing. `unmunch` did not expand Hungarian's affix structure the way it expanded the Czech, Polish and Slovak SFX/PFX tables. Shipping this list would tell a Hungarian player that `házat` is not a word, which makes the game unplayable in Hungarian.

Note what this is **not**: it is not a compound explosion, and it is not a size-limit problem. 81 509 sits comfortably inside the accepted range of 80 000 to 5 000 000.

## 2. The two independent questions — either one solves the problem

Answer **both**. They are alternative routes and only one needs to succeed.

### Question A — can `hu_HU` be expanded correctly by a different tool?

The dictionary source is already licensed, already pinned, and already trusted. If some tool expands it properly, that is the cheapest and cleanest answer.

Establish, with evidence:

1. **Why `unmunch` fails on Hungarian specifically.** What features of `hu_HU.aff` does it not implement? Cite the hunspell documentation or source, not a forum guess. Relevant suspects to confirm or eliminate: two-level suffixation, `AM` morphological fields, numeric flag mode (`FLAG num`), `CIRCUMFIX`, `ONLYINCOMPOUND`, `COMPOUNDRULE`, `NEEDAFFIX`, condition patterns.
2. **Is `unmunch` documented as incomplete?** Its own manual page or README may say it handles only simple dictionaries. Quote it if so.
3. **What other expanders exist**, and for each: exact name, project URL, version, licence, whether it is maintained, and specifically whether it claims to handle Hungarian. Consider at minimum `hunspell` itself in any generating mode, `wordforms`, `affix`/`munch` companions, `hunspell-reader`, `spylls` (a Python hunspell reimplementation), `nuspell`, `libhunspell` bindings, and anything in the Hungarian NLP ecosystem.
4. **`spylls` deserves specific attention** if it exists as described — a full reimplementation may implement affix features `unmunch` skips. Establish whether it can enumerate all forms, or only check words.
5. If a tool exists, state **how one would verify** its output is correct: the six words above (`házat`, `házban`, `házakat`, `kutyát`, `kutyák`, `asztalon`) must appear, and the total should be plausibly in the millions rather than tens of thousands.

### Question B — does a fully inflected, redistributable Hungarian word list already exist?

For each candidate you find, report the fields in section 3. Directions worth investigating, none of which is a recommendation:

- **`magyarispell`** — the upstream project that generates `hu_HU` for LibreOffice. It builds from source data and may publish or be able to emit an expanded list. Find its canonical home, its licence, and whether an expanded artifact is distributed.
- **`morphdb.hu` / hunmorph / ocamorph** — Hungarian morphological databases. Establish licence and whether they yield a plain word list.
- **Hungarian Wiktionary** database dumps, and whether they contain inflected forms or only lemmas.
- **`szoszablya` / Hungarian webcorpus** frequency lists — these are corpus-derived, so they contain real inflected forms but also typos and foreign words. Establish licence, size, and whether any cleaned variant exists.
- **Hungarian Scrabble associations**, if an official tournament word list exists. Note that official Scrabble lists are usually **not** redistributable; report the licence honestly rather than assuming.
- **Hungarian NLP corpora and treebanks** — Universal Dependencies Hungarian, MNSZ / Hungarian National Corpus, and any published lemma-plus-form inventories.
- **`hu_HU` forks** shipped by Firefox, Chromium, Apple, or Linux distributions that might be pre-expanded.

## 3. Required fields per candidate

```text
Name and canonical URL
Version, release date, or exact commit
Licence, with its exact version (GPL-2.0-only and GPL-3.0-or-later are different answers)
Where the licence text is stated — quote the sentence, do not summarize it
Redistribution permitted in a public Git repository:  yes | no | unclear
Modification permitted:                                yes | no | unclear
Attribution or notice requirements
Format as distributed:  plain word list | hunspell dic+aff | XML | database dump | annotated corpus
Approximate entry count
Does it contain INFLECTED forms or only lemmas — and what evidence tells you so
Are the six test words present, if you can determine that without downloading
Diacritics: does it preserve á é í ó ö ő ú ü ű correctly
Case: lowercase, mixed, or uppercase
Does it include proper nouns, abbreviations, or foreign words — these are usually unwanted
Retrieval date
```

## 4. Hard constraints — a candidate failing any of these is disqualified, and say so

```text
1  The licence must clearly permit redistribution AND modification in a public repository. A
   non-commercial, research-only, or no-derivatives licence is a disqualification, not a footnote.
2  It must contain inflected forms. A lemma list is exactly the problem we already have.
3  It must be a fixed, versioned artifact that can be pinned. A live API or a scraped website is not
   acceptable — the build must be reproducible from a pinned source.
4  No machine-translated, model-generated, or synthesized word lists. Every word must trace to a
   human-curated linguistic source.
5  Diacritics must be correct and preserved. A stripped-diacritic list is useless for this game.
```

## 5. What to report

1. **A direct answer to Question A**: is there a tool that correctly expands `hu_HU`? Name it, or state that you found none and what you checked.
2. **A direct answer to Question B**: a ranked table of candidates with the section 3 fields, best first, and an explicit statement for each about the section 4 constraints.
3. **Your single recommendation**, with its reasoning and its risks.
4. **What you could not establish**, listed explicitly. Do not fill a gap with a plausible guess.
5. **A short note on whether Hungarian is unusually hard**, and if so why — agglutinative morphology, compounding, or licence culture. One paragraph, sourced. This helps calibrate how much effort is proportionate.

## 6. Two things to leave alone

- **Do not evaluate two-letter word lists.** Two-letter authority files are optional in this engine and Hungarian will not use one initially. Out of scope.
- **Do not propose changing the engine** to call a spell-checker at runtime instead of loading a word list. That has been considered and rejected: the prefix-probe search performs millions of lookups per move and needs an in-memory sorted index.

## 7. Tone

Be sceptical of your own sources. Prefer a primary project page over a blog post, and say which you used. If two sources disagree about a licence, report the disagreement rather than picking one. Distinguish clearly between what you verified, what you inferred, and what you are repeating from a secondary source.

A precise "I checked these eleven candidates and none satisfies constraint 1" is a better deliverable than an enthusiastic pointer to something that turns out to be research-only.

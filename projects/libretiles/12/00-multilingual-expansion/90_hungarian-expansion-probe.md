# Hungarian expansion probe — measured result

Artifact class: **Orchestrator evidence record. Non-independent. Not authority.**
Performed directly by the ORCHESTRATOR on 2026-09-03 after the Worker dispatch for
`02_probe_00.md` was killed by an external billing limit (see `02_interruption_00.md`).
Read-only against the repository; every mutation confined to
`/tmp/opencode/mle-v4-probe/`.

⛔ This is **not** a Worker report and must never be renamed to one. Its judgement calls
are corroborated only by the mechanical hunspell oracle, because the same actor measured
and reviewed them.

```text
repository baseline   61720aa701132085809a9012ee29e446c622bd4f, porcelain empty
                      before and after; no repository file created, edited, or staged
probe question        can a pinned Spylls expand the pinned Hungarian hunspell
                      dictionary into a Libre Tiles playable lexicon?
```

## 0. The verdict, in three sentences

**The expander works. The asset does not fit.** Spylls 0.1.7 resolves the `AF` flag
aliases and follows suffix continuations exactly as the research predicted — the six-word
gate passes 6/6, a wider twenty-three-word gate passes 23/23, and hunspell 1.7.3 accepts
**3 000 of 3 000** sampled emitted forms. But the full non-compound affix inventory is
approximately **4.27 billion** forms (~77 GB), and even bounded to 15 code points it is
approximately **301 million** forms (~4.5 GB) — against Slovak 3 005 250 / 45 MB, Czech
3 930 497 / 54 MB, Polish 3 721 704 / 52 MB, on a repository where GitHub already emitted
a large-file warning at 51.6 MB.

So the acceptance gate inherited from `DEFECT_LEDGER.md:1442-1456` — *"MUST be plausibly
in the MILLIONS, not near the 96 955 stem count"* — is not merely met, it is **overshot by
three orders of magnitude**, and that overshoot is itself the blocker.

---

## 1. Pinned sources — all four SHA-256 values verified by me

Base `https://raw.githubusercontent.com/LibreOffice/dictionaries/75f5dff8c972fff4a32e4ea8434722c277f02a3f/hu_HU/`

```text
file               bytes       SHA-256                                                            verdict
hu_HU.dic          1 756 889   2ec787f2992a8affe82a9aa912a0a881b21dfa6a61dc8a35aa160e5e41565bda   MATCH
hu_HU.aff          2 236 063   7fbfe784398e6605cae9d75988187cd59e8cfa1040cc30783a55cd92d3b9ea41   MATCH
README_hu_HU.txt       1 194   cd2c7ae61d509dbb6eb298b8185e3b0c1cc2ed1f39d9ef146efd05e28fd541dc   MATCH
description.xml          839   049d1c6cac167cce2fe18638c35ecfacea72c78337803bae2aede146a879c6ee   MATCH
```

All four match the values recorded by the era-11 acquisition Worker at the same pinned
commit, so the upstream is byte-identical to what that report described.

## 2. Structural facts — the AF-alias hypothesis is CONFIRMED on the actual bytes

```text
.dic first line (stem count)     96955
.dic entries actually parsed      96940      (the header count is 15 higher than the
                                              parsed entry count; the same 96 940 the
                                              era-11 unmunch run reported)
SET                               UTF-8
FLAG directive                    ABSENT  -> hunspell default single-character flags
AF table                          PRESENT, 1559 entries       <- THE DECISIVE FACT
AM table                          PRESENT, 25 975 entries
SFX lines                         24 303        SFX flag classes     123
PFX lines                            370        PFX flag classes       8
COMPOUNDFLAG Y · COMPOUNDMIN 1 · COMPOUNDWORDMAX 2 y
NEEDAFFIX 'u' · ONLYINCOMPOUND '|' · FORBIDDENWORD 'w' · CIRCUMFIX absent · FULLSTRIP false
```

Worked example of the compression that defeats the C `unmunch`, read from the raw bytes:

```text
.dic line 33724   ház/59	8726
AF entry 59       Um\xf4\xd2\xe7iYc\xb2      -> 9 affix flags
AM entry 8726     po:noun ts:NOM al:házak
.dic line 27574   kutya/9    -> AF 9  -> 18 affix flags
.dic line 49164   asztal/30  -> AF 30 -> 21 affix flags
```

`unmunch.cxx` recognizes only `FULLSTRIP`, `PFX` and `SFX` while parsing the affix file
and stores an affix class as a single character (`achar = *piece`), with no `AF` handling
at all — so it reads `59` as a literal flag and the stem never reaches its 9 real suffix
classes. Spylls resolves it. Measured, `ház` arrives with 9 flags and `kutya` with 18,
which is the mechanism the era-11 report could not obtain.

⚠ **One Spylls artefact worth recording.** 84 of the 123 SFX flag keys and 1 442 of the
1 559 AF entries come back **surrogate-escaped** (`'\udcb2'`, `'\udcd2'`, …) because the
flag bytes are not valid UTF-8 sequences even though `SET UTF-8` governs the word data.
This is cosmetically alarming and **functionally harmless**: the escaping is applied
consistently on both sides, so an AF-resolved flag still matches its SFX table key. I
verified all four of `ház`'s surrogate flags resolve to real SFX classes. Any future
implementation must not "fix" this by re-decoding one side only.

## 3. Licence identity — the contradiction is REAL and is resolved from the artifact

Read from the installed wheel rather than from a web page:

```text
spylls-0.1.7.dist-info/METADATA     License: UNKNOWN
                                    Classifier: License :: OSI Approved :: MIT License
spylls-0.1.7.dist-info/LICENSE      "Mozilla Public License Version 2.0"  (full text)
wheel                               spylls-0.1.7-py2.py3-none-any.whl
                                    sha256=0c7fa4b66615f390bd12fd37939b85934c012309fd3cce8584844c54270b7776
resolved version                    0.1.7 exactly, as pinned
```

So the artifact **ships MPL-2.0 licence text while classifying itself MIT, with the
free-text field left `UNKNOWN`.** That is the contradiction the deep research flagged,
now confirmed inside the distributed artifact.

Operative reading, stated as an engineering judgement and explicitly **not** as legal
advice: MPL-2.0 is file-level copyleft on MPL-covered **source files**, and neither
reading applies to a word list. The generated forms are derived from the Hungarian
dictionary — `LGPL-3.0-or-later OR MPL-2.0-or-later`, per its own README — not from
Spylls' source. Spylls would be a **build-time tool only**, never imported by Django and
never shipped, which is precisely the posture `/usr/bin/unmunch` (hunspell, LGPL/GPL/MPL)
already holds for the Slovak, Czech and Polish lexicons. Under that posture the
contradiction does not block the route.

⛔ It nevertheless remains a **Cooperator-owned material decision** whether a
build-time dependency with self-contradictory licence metadata is acceptable in a project
he will present. It is recorded here rather than decided.

## 4. Verbatim licence sentence of the dictionary itself

From `README_hu_HU.txt`, quoted not summarized, as `build_slovak_lexicon.py:103-114`
requires for Slovak:

> The contents of this software may be used under the terms of the GNU Lesser General
> Public License Version 3 or later (the "LGPL" …) or the Mozilla Public License Version
> 2.0 or later (the "MPL" …).

Hungarian header line: *"MPLv2 vagy LesserGPLv3+"*. Derived SPDX:
`LGPL-3.0-or-later OR MPL-2.0-or-later`. Redistribution and modification are clearly
permitted.

---

## 5. Enumeration method

Spylls' **reader** was used for both the affix file and the dictionary — that is the part
that resolves `AF` aliases and is well-tested. The traversal was written by me on top of
Spylls' parsed `Aff` / `Dic` model, following the shape of Spylls' own
`examples/unmunch.py` rather than importing it from the network:

```text
1  the bare stem, unless NEEDAFFIX / ONLYINCOMPOUND / FORBIDDENWORD forbids it
2  direct suffixes whose condition regexp matches the stem
3  suffix CONTINUATION flags into secondary suffixes   <- what the C unmunch lacks
4  prefixes, and prefix x suffix cross-products where crossproduct is allowed
```

⛔ **Compounds were deliberately NOT enumerated.** `COMPOUNDFLAG Y` with `COMPOUNDMIN 1`
makes the compound set unbounded. Every count below is therefore a **lower bound** on
legal Hungarian, which strengthens rather than weakens the conclusion.

⚠ One mechanism I got wrong first and corrected by measurement, recorded because it is the
trap the next implementation will hit. `ház` carries only 9 flags and cannot itself produce
`házat` or `házak`; its `AM` data declares `al:házak`. My first traversal therefore added
`data['al']` values as extra bases. That was unnecessary: **`házak` is its own dictionary
entry** at `.dic` line 64940 (`házak/1079`), with its own 8 flags, and expanding it yields
`házat` and `házakat` directly. Feeding `al:` values as bases would have over-generated
from metadata rather than from the affix system. The final traversal uses `dic.words` only.

## 6. The six-word gate — 6 of 6 PRESENT

The gate inherited verbatim from `DEFECT_LEDGER.md:1444-1446`, each with the dictionary
entry that produces it:

```text
házat        PRESENT   via stem házak
házban       PRESENT   via stem ház
házakat      PRESENT   via stem házak
kutyát       PRESENT   via stem kutya
kutyák       PRESENT   via stem kutya
asztalon     PRESENT   via stem asztal
```

For contrast, the same six under the era-11 `unmunch` run: `házat` ABSENT, `házban`
ABSENT, `házakat` ABSENT. **The expander question is answered.**

## 7. The wider gate — 23 of 23 PRESENT

I chose these from stems visible in the pinned `.dic` and did not invent Hungarian. Every
one was confirmed present, each with its producing stem:

```text
házak     via házak     kutyának  via kutya    könyvet   via könyv    városban  via város
házban    via ház       kutyával  via kutya    könyvek   via könyv    városok   via város
háztól    via ház       asztalt   via asztal   könyvben  via könyv    kezében   via kezek
                        asztalok  via asztal   gyerekek  via gyerek   kezek     via kezek
                        asztalnál via asztal   gyereket  via gyerek   szemek    via szem
                                               emberek   via ember    szemet    via szem
                                               embert    via ember    vizet     via vizek
                                                                      vizek     via vizek
```

Note `kezében` and `vizet` arrive from the irregular stems `kezek` and `vizek`, which are
separate dictionary entries — the same allomorph-as-its-own-entry mechanism as `házak`.

## 8. The independent oracle — 3 000 of 3 000 accepted

`hunspell 1.7.3` (`@(#) International Ispell Version 3.2.06 (but really Hunspell 1.7.3)`),
already installed on the host, run against the **same pinned dictionary**:

```text
level-1 forms sampled   1 200     rejected 0     accepted 1 200     agreement 100.0%
level-2 forms sampled   1 800     rejected 0     accepted 1 800     agreement 100.0%
```

`hunspell -l` was used: it prints only the words it rejects, so empty output is total
acceptance. Random seed 777, forms drawn from 120 randomly selected stems.

⛔ **The asymmetry, stated plainly.** hunspell can remove a form the expander should not
have generated, but it can **never reveal a legal form the expander never produced**. So
100% agreement establishes that the traversal does not **over**-generate; it says nothing
about **under**-generation. The six-word and twenty-three-word gates are what address
under-generation, and they pass. Together the two lines of evidence are strong — but the
completeness claim rests on 29 hand-checked forms, not on the oracle.

**Consequence worth keeping:** since the oracle rejected nothing, the ~4.27 billion figure
below is not an artefact of a sloppy traversal. It is the real size of Hungarian
non-compound inflection under this dictionary.

---

## 9. The scale measurement — this is the finding

Extrapolated from a random sample of 600 of the 96 940 dictionary entries (seed 31337),
after the project's standard filter (`NFC` → `strip` → `casefold`, `isalpha`, `len >= 2`),
with the traversal itself bounded at 25 code points:

```text
per-stem mean forms                                    40 197
ceiling   per-stem      extrapolated to 96 940 stems     approx bytes
   12 cp         671              65 006 510              ~0.98 GB
   15 cp       3 104             300 922 925              ~4.51 GB
   18 cp       8 992             871 718 247             ~13.08 GB
   21 cp      18 173           1 761 666 708             ~26.43 GB
   25 cp      30 555           2 962 001 538             ~44.43 GB
  none (25cp traversal bound)   4 271 219 538            ~76.9 GB
```

Against what this repository actually ships:

```text
slovak.txt   3 005 250 words    45 456 204 B
czech.txt    3 930 497 words    54 105 021 B   <- GitHub emitted a large-file WARNING
polish.txt   3 721 704 words    51 607 141 B
collins2019    279 496 words     3 103 812 B
```

⚠ These are extrapolations from a 600-stem sample, not a completed full run. Deduplication
across stems will reduce them somewhat, but not by an order of magnitude, because Hungarian
affix forms are stem-specific — and the figures exclude compounds entirely, so the true
inventory is larger. The conclusion is robust to a factor of ten in either direction.

**Even at the tightest defensible board bound — 15 code points, so a word that could fit on
a 15×15 board using single-code-point tiles — Hungarian is ~100× the Czech lexicon.** A flat
enumerated Hungarian word list is not committable to this repository.

## 10. The `wordforms` second data point

`/usr/bin/wordforms` is present on this host and was not considered by the era-11 Worker.
It was **not** measured in this probe: the scale result made it irrelevant. hunspell's own
README marks `unmunch` deprecated in favour of `wordforms`, and open hunspell issue #404
(since 2016-09-13) asks for a replacement supporting `LONG`/`UTF`/`NUM` flags and twofold
affixes — which is evidence that `wordforms` is not that replacement. Recorded as
**not measured**, deliberately, rather than claimed either way.

## 11. Containment ledger

```text
temporary root      /tmp/opencode/mle-v4-probe/
owner               ORCHESTRATOR (inherited from the interrupted Worker session; all four
                    pinned hashes re-verified before reuse)
contents class      public upstream dictionary sources, a throwaway virtualenv holding
                    spylls 0.1.7, my traversal script, and sampling output.
                    NO secrets, NO personal data, NO repository content.
RETAINED, with reason — a later slice needs them
    src/hu_HU.dic · src/hu_HU.aff · src/README_hu_HU.txt · src/description.xml
    expand.py        the traversal, kept whatever the verdict
    sample-forms.txt s1.txt s2.txt   the 3 000 oracle-checked forms
    pip-report.json  the spylls resolution record
NOT PRODUCED         no hungarian.txt candidate lexicon was written, because the scale
                     measurement made a full run pointless and it would have exceeded the
                     4 GB bound the prompt set
cleanup owner        the COOPERATOR, once a later slice has consumed this evidence
```

⛔ **Nothing was copied into `/home/agile/Projects/libretiles`.** No lexicon, no licence
file, no manifest, no script. `git status --porcelain=v1` was empty before and after, and
`git rev-parse HEAD` is unchanged at `61720aa701132085809a9012ee29e446c622bd4f`.

## 12. Not one word came from a language model

Every form counted or checked above is the filtered image of a string derived mechanically
by the traversal from the pinned `hu_HU.dic` / `hu_HU.aff` at commit
`75f5dff8c972fff4a32e4ea8434722c277f02a3f`. The 23 gate words were selected from stems
visible in that dictionary and each is reported with the stem that produces it. No
Hungarian word was invented, translated, or generated.

---

## 13. What this forces open, and the recommendation

The deep research closed one door in advance: *"Do not propose changing the engine to call
a spell-checker at runtime instead of loading a word list. That has been considered and
rejected: the prefix-probe search performs millions of lookups per move and needs an
in-memory sorted index."* That rejection was correct **on the evidence available then** —
it assumed the word list would be millions, like Slovak. It is 301 million at the tightest
board bound.

`PROJECT_CONTEXT.md:423-435`: a locked fork reopens only on **contradictory evidence plus a
Cooperator decision**. Section 9 is that contradictory evidence. Four options, with the
honest cost of each:

```text
A  COMMIT THE FULL LIST.        Rejected on measurement. ~4.5 GB at the tightest bound,
                                on a repository that already drew a GitHub warning at
                                51.6 MB. Git LFS is a locked prohibition.
B  RUNTIME SPELL-CHECKER.       Kills the prefix probe, which is the mechanism the engine
                                uses to author every move — and the engine authors EVERY
                                move in this product (PROJECT_CONTEXT.md:449-476). This
                                would not degrade Hungarian AI, it would disable it.
                                Rejected, and the original rejection still holds for the
                                stated reason.
C  A FREQUENCY- OR PARADIGM-BOUNDED SUBSET. Needs a frequency or headword source, and all
                                nine researched candidates failed the licence or
                                provenance constraints. It also makes the lexicon a
                                judgement call rather than a mechanical derivation, which
                                is exactly what "not one word from a language model"
                                exists to prevent. Rejected for this cut.
D  GENERATE LOCALLY AT SETUP FROM THE PINNED 4 MB SOURCE.   RECOMMENDED.
                                Commit build_hungarian_lexicon.py plus the two pinned
                                source hashes; the 4 MB .dic/.aff is licensed and tiny.
                                The script materializes a bounded lexicon into
                                backend/assets/dicts/ at setup time, and that file is
                                gitignored. The engine's in-memory sorted index is
                                UNCHANGED, so the prefix probe and the move search are
                                untouched. readiness stays exactly two values and reports
                                `unavailable` until the local build has run — which is
                                what gap G2's fail-closed validation is for.
```

**Why D is the right answer and not a workaround.** Re-read the Cooperator's own
instruction: *"build_slovak_lexicon.py bol pouzity na stahovanie slovnika, takto chcem aby
boli stiahnute vsetky potrebne slovniky"* — the dictionaries should be **downloaded by a
script**. For Slovak, Czech and Polish the script's output happened to be small enough to
commit as well. For Hungarian it is not. D keeps his stated method exactly and drops only
the incidental habit of committing the output.

Costs of D, stated so they are not discovered later:

```text
1  a fresh clone has NO Hungarian lexicon until the script runs. Hungarian therefore
   reports readiness `unavailable` on a fresh clone, and `playable` after setup. That is
   a visible product behaviour and it must be documented in README.md and AGENTS.md.
2  the setup step needs the network and takes minutes. It must be OPT-IN, never on the
   critical path of local boot, because AGENTS.md promises AI-only boot needs only two
   terminals.
3  it introduces the first gitignored asset under backend/assets/dicts/, so the
   .gitignore entry and the fail-closed readiness path must be tested together.
4  a code-point ceiling must be chosen and JUSTIFIED against the tile set, not guessed.
   A ceiling of 15 code points is too tight once DZS is a tile; the ceiling belongs in the
   Hungarian manifest as a declared build parameter, derived from 15 tiles.
```

⛔ **This is a Cooperator-owned material decision** — it changes what "shipped" means for
one language. It is recorded here with the measurement that forces it, and the Orchestrator
notes file carries the decision I took under his standing autonomy grant, so he can
override it with one word.

## 14. Evidence classification

```text
MEASURED BY ME, this session
  all four pinned SHA-256 values · every structural fact in section 2 · the licence
  metadata in section 3 · the six-word gate · the twenty-three-word gate · the 3 000-form
  oracle agreement · every number in section 9 · the empty porcelain before and after
QUOTED FROM A NAMED ARTIFACT, not re-derived
  the era-11 unmunch figures (96 940 lines, 81 509 unique) from 11/02/01_report_00.md
  the unmunch.cxx and hunspell issue #404 mechanism from 11/02/00_deep_research.md
  the sk/cs/pl word counts from 11/02/01_report_00.md, byte sizes measured by me
NOT MEASURED, and labelled so
  /usr/bin/wordforms output · a completed full expansion run · a deduplicated exact total
  · the legal effect of the Spylls licence contradiction
INDEPENDENCE
  none. Orchestrator-performed, non-independent, corroborated only by the hunspell oracle.
```


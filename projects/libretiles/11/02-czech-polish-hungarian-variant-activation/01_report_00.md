### Report for ORCHESTRATOR_CHAT

logical whole `czech-polish-hungarian-variant-activation`, Worker session `01`, Worker exchange `01`

1. **status `PASS`**. Per language: **czech `ready`**, **polish `ready`**, **hungarian `ready`**. All three directories exist at the pinned commit; all three licences clearly permit redistribution and modification; all three unique counts sit inside `[80_000, 5_000_000]`; `unmunch` exited 0 with non-empty stdout. Hungarian is in-bound but is a stem list, not a Slovak-scale inflection expansion — see §7 and risks.

2. **Phase-qualified result: not-applicable**

3. **Repository gate**

```text
Working directory: /home/agile/Projects/libretiles
git rev-parse HEAD                   == 8c00a331560f16b7d27eae04dc789a5124dd4497
git status --porcelain=v1            == exactly the ten untracked frontend/public flag images
```

End-of-task confirmation: `HEAD` is still `8c00a331560f16b7d27eae04dc789a5124dd4497`, porcelain is unchanged (the same ten `frontend/public/{cs,cz,en,hu,pl,sk}.{png,jpeg}` untracked flag images), and **no repository file was created, edited, renamed, deleted, or staged**.

4. **Per language — provenance, downloads, licence, expansion, output**

Pinned commit for all four languages: `75f5dff8c972fff4a32e4ea8434722c277f02a3f`. Every SHA-256 below reproduced on a second read.

### Czech — directory `cs_CZ` — `ready`

Present at that commit (not all downloaded): `META-INF/`, `README_cs.txt`, `README_en.txt`, `cs_CZ.aff`, `cs_CZ.dic`, `description.xml`, `dictionaries.xcu`, `hyph_cs_CZ.dic`, `thes_cs_CZ.dat`, `thesaurus/`. **No `LICENSE.txt`.** Spellchecker files are exactly `cs_CZ.dic` / `cs_CZ.aff`. Hyphenation and thesaurus were observed, not fetched.

| file | URL | HTTP | bytes | SHA-256 |
|---|---|---|---|---|
| `cs_CZ.dic` | `https://raw.githubusercontent.com/LibreOffice/dictionaries/75f5dff8c972fff4a32e4ea8434722c277f02a3f/cs_CZ/cs_CZ.dic` | 200 | 3 656 362 | `d8e8c88c006fdae72dac8c85df11b0c99a773e05a4ab0fcbe92244876668ca74` |
| `cs_CZ.aff` | `…/cs_CZ/cs_CZ.aff` | 200 | 111 575 | `7ecb20620ecd46ebd9c36f3f33e69dd4eda385cba5b2bb4e6bc396d910e297f7` |
| `README_en.txt` | `…/cs_CZ/README_en.txt` | 200 | 13 105 | `0fe6d017aa91ffb58146d19160f8207900cc0c49d5fffef0b1a7d3a364cb29bd` |
| `README_cs.txt` | `…/cs_CZ/README_cs.txt` | 200 | 59 410 | `24d1d07409b62e8e6f0ee114991d4749d3e97b05ea19feca835916af67312720` |
| `description.xml` | `…/cs_CZ/description.xml` | 200 | 3 606 | `7d87b3603858558b8a288d72c9d1c5db416c7100d94f7ad597331bd50da5a675` |

`.dic` stem count (first line): **261 167**. `SET UTF-8`.

Licence identity, quoted: *“This dictionary is licensed under the GNU/GPL license.”* (`README_en.txt`). Czech `README_cs.txt`: *“Slovník je licencován pod licencí GNU/GPL licencí, která je k dispozici v Příloze B.”* Příloha A/B embeds **GNU GPL Version 2, June 1991**. `description.xml` points at both READMEs as `license-text`. Derived SPDX: **`GPL-2.0-only`**. Redistribution and modification are clearly permitted.

`unmunch` exit **0**, stdout **58 247 893 B** / 4 270 281 raw lines (stderr is `parsing line:` noise, 85 805 B). Unique after NFC/strip/casefold/`isalpha()`/`len>=2`/dedup/sort: **3 930 497**.

| output | path | lines | bytes | SHA-256 |
|---|---|---|---|---|
| lexicon | `/tmp/opencode/cph-dicts/czech/czech.txt` | 3 930 499 (2 header + 3 930 497 words) | 54 105 021 | `919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc` |
| licence | `/tmp/opencode/cph-dicts/czech/czech.LICENSE` | — | 72 790 | `bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8` |

First ten: `aachen, aacr, aakjaer, aakjaera, aakjaere, aakjaerech, aakjaerem, aakjaerova, aakjaerovi, aakjaerovo`  
Last ten: `žžonko, žžonkou, žžonku, žžonky, žžonkách, žžonkám, μa, μg, μm, μv`  
Mid-list: `nesamostředícím, nesamostředícíma, nesamostředícími, nesamostředícímu, nesamosvornost, nesamosvornostech, nesamosvornostem, nesamosvornosti, nesamosvornostmi, nesamosvorností`

### Polish — directory `pl_PL` — `ready`

Present: `META-INF/`, `README_en.txt`, `README_pl.txt`, `description.xml`, `dictionaries.xcu`, `hyph_pl_PL.dic`, `pl_PL.aff`, `pl_PL.dic`, `plhyph.tex`, `th_pl_PL_v2.dat`. **No `LICENSE.txt`.** Spellchecker files are exactly `pl_PL.dic` / `pl_PL.aff`.

| file | URL | HTTP | bytes | SHA-256 |
|---|---|---|---|---|
| `pl_PL.dic` | `…/pl_PL/pl_PL.dic` | 200 | 4 539 105 | `215fd73aa47b11e7fdd2e4d655e9fe37be4acdae16ff833badcfdfce79110aad` |
| `pl_PL.aff` | `…/pl_PL/pl_PL.aff` | 200 | 246 842 | `7c37b9bde78054e43365b488a13859094c88bc66664b5b7a7bb073626454b38e` |
| `README_en.txt` | `…/pl_PL/README_en.txt` | 200 | 2 282 | `fb5f9b4a0643821cf88775c0932810c1cd05f236136c913e3eaf1e24806f3f44` |
| `README_pl.txt` | `…/pl_PL/README_pl.txt` | 200 | 27 814 | `ce3ad7ab1d3a8b767b8f7dcc870796fbda76bc7ad8cde22f6312b0cf86a5bd11` |
| `description.xml` | `…/pl_PL/description.xml` | 200 | 620 | `0a2174ee6720b76de1de5ed8d7ffdec32350d929f685c936f6436a02c662d1f6` |

`.dic` stem count: **308 298**. Affix encoding **`SET ISO8859-2`** — unmunch stdout was decoded as `iso8859-2` before the Slovak NFC/casefold/`isalpha` filter. That is encoding, not a tighter word filter.

Licence identity, quoted: *“This dictionary for spell-checking Polish texts is licensed under GPL, LGPL, MPL (Mozilla Public License), Apache 2.0 and Creative Commons ShareAlike licenses (see http://creativecommons.org/licenses/sa/1.0).”* Polish README repeats the same five-licence grant. Redistribution and modification are clearly permitted under GPL/LGPL/MPL/Apache-2.0 alone. Derived SPDX (engineer reading, versions of GPL/LGPL/MPL **not stated** in the spellchecker paragraph): **`GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 OR Apache-2.0 OR CC-SA-1.0`**. `README_pl.txt` then embeds LGPL-2.1 in full for the **thesaurus**, not as a version pin for the spellchecker.

`unmunch` exit **0**, stdout **50 877 895 B** / 3 892 584 raw lines. Unique: **3 721 704**.

| output | path | lines | bytes | SHA-256 |
|---|---|---|---|---|
| lexicon | `/tmp/opencode/cph-dicts/polish/polish.txt` | 3 721 706 | 51 607 141 | `605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06f3f44` wait — **`605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab`** |
| licence | `/tmp/opencode/cph-dicts/polish/polish.LICENSE` | — | 30 427 | `869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3` |

First ten: `aa, aaa, aachen, aachenem, aachenie, aachenowi, aachenu, aalborg, aalborgiem, aalborgowi`  
Last ten: `żłóbkami, żłóbki, żłóbkiem, żłóbkom, żłóbkowi, żłóbku, żłóbków, żłóbmy, żłóbmyż, żłóbże`  
Mid-list: `niewypogodzona, niewypogodzone, niewypogodzonego, niewypogodzonej, niewypogodzonemu, niewypogodzony, niewypogodzonych, niewypogodzonym, niewypogodzonymi, niewypogodzoną`

### Hungarian — directory `hu_HU` — `ready` (quality risk: under-expansion)

Present: `Lightproof.components`, `Lightproof.py`, `Linguistic.xcu`, `META-INF/`, `README_hu_HU.txt`, `README_hyph_hu_HU.txt`, `README_lightproof_hu_HU.txt`, `README_th_hu_HU_v2.txt`, `description.xml`, `dialog/`, `dictionaries.xcu`, `help/`, `hu_HU.aff`, `hu_HU.dic`, `hyph_hu_HU.dic`, `pythonpath/`, `th_hu_HU_v2.dat`. **No `LICENSE.txt`, no `README_en.txt`.** Spellchecker files are exactly `hu_HU.dic` / `hu_HU.aff`. Extra READMEs for hyphenation/thesaurus/lightproof were observed, not fetched.

| file | URL | HTTP | bytes | SHA-256 |
|---|---|---|---|---|
| `hu_HU.dic` | `…/hu_HU/hu_HU.dic` | 200 | 1 756 889 | `2ec787f2992a8affe82a9aa912a0a881b21dfa6a61dc8a35aa160e5e41565bda` |
| `hu_HU.aff` | `…/hu_HU/hu_HU.aff` | 200 | 2 236 063 | `7fbfe784398e6605cae9d75988187cd59e8cfa1040cc30783a55cd92d3b9ea41` |
| `README_hu_HU.txt` | `…/hu_HU/README_hu_HU.txt` | 200 | 1 194 | `cd2c7ae61d509dbb6eb298b8185e3b0c1cc2ed1f39d9ef146efd05e28fd541dc` |
| `description.xml` | `…/hu_HU/description.xml` | 200 | 839 | `049d1c6cac167cce2fe18638c35ecfacea72c78337803bae2aede146a879c6ee` |

`.dic` stem count: **96 955**. `SET UTF-8`. No `FLAG` directive. Stems look like `üzér/1` (numeric-looking flags plus morphological fields). Affix file has compounding (`COMPOUNDFLAG Y`, `COMPOUNDMIN 1`, `COMPOUNDWORDMAX 2 y`) and ~24 303 `SFX` / 370 `PFX` lines. `COPYING.LGPL` / `COPYING.MPL` are **not** in the LibreOffice dictionaries tree at this commit (repo-root listing checked).

Licence identity, quoted from `README_hu_HU.txt`: *“The contents of this software may be used under the terms of the GNU Lesser General Public License Version 3 or later (the "LGPL" …) or the Mozilla Public License Version 2.0 or later (the "MPL" …).”* Hungarian header: *“MPLv2 vagy LesserGPLv3+”*. Derived SPDX: **`LGPL-3.0-or-later OR MPL-2.0-or-later`**. Redistribution and modification are clearly permitted.

`unmunch` exit **0**, stdout **1 063 774 B** / **96 940 raw lines** — essentially the stem list, not an inflection+compound explosion. Unique: **81 509**.

| output | path | lines | bytes | SHA-256 |
|---|---|---|---|---|
| lexicon | `/tmp/opencode/cph-dicts/hungarian/hungarian.txt` | 81 511 | 897 386 | `44be0516be5b2d842f50bda6d5c3a2e31bccf1ee2772d398959757f477ac63ed` |
| licence | `/tmp/opencode/cph-dicts/hungarian/hungarian.LICENSE` | — | 1 464 | `febb4588f44393c3500532afa16a36fd1a5f512a7cef0e088f3c7d0f722f8a72` |

First ten: `aba, abaffy, abafi, abajgat, abakteriális, abakusz, abaliget, abaposztó, abasár, abay`  
Last ten: `űrtartalmak, űrtartalom, űrtechnológia, űrutazás, űrállomás, űrügyi, űrügynökség, űz, űzet, űzött`  
Mid-list: `lejáratú, lejárt, lejátszás, lejátszó, lejátszófej, lekicsinylő, lekonyulás, lekopás, lektor, lektorál`

Inflection probe (not a second filter; evidence only): `ház` HIT, `házak` HIT, `megyek` HIT, `mentem` HIT, `leszek` HIT, `voltam` HIT; **`házat` MISS, `házban` MISS, `házakat` MISS**. Typical case endings are absent. `unmunch` did not expand this morphological affix table.

5. **Per language — length-2, long words, alphabet**

Expected alphabets used for the out-of-alphabet check (casefolded):  
Czech `aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž`; Polish `aąbcćdeęfghijklłmnńoóprsśtuwyzźżqv` (q/v included as loanword letters; **x treated as outside**); Hungarian `aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz`.

| | Czech | Polish | Hungarian |
|---|---|---|---|
| length-2 count | **350** | **458** | **92** |
| longest | `polyoxyethylensorbitanmonopalmitátech` (37) | `niedziewięćdziesięciopięcioipółletniego` (39) | `góóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóóól` (41) |
| words length > 15 | **428 479** | **604 281** | **2 995** |
| outside-alphabet | ö ü ő ä ű ľ ń ś ł ć ë î ç ę â ô õ å ĺ **μ** ã ø (loanwords, Slovak/Hungarian letters, Greek mu units `μa/μg/μm/μv`) | **x** in 2 373 words (`abraxas`, `aix`, …) | loanword letters ł ä ș å č ń à ë ñ ć š … and modifier `ʻ` (1) |

Czech length-2 sample (50 of 350): `ac ad ag ah ai ak al ap ar as at au av az aú ač aň aš ať až ba bi bm bo bq br bu by bz bú ca cd ce ch ci cl cm co cp cr cu cz cé da db dc de di dj dl`  
Polish length-2 sample (50 of 458): `aa ab ac ad ae af ag ai aj ak al am an ao ap ar as at au av az ań aś aż ba bc bd be bg bh bi bj bk bm bn bo bp bq br bu by bz bł ca cb cc cd ce cf cg`  
Hungarian length-2 sample (50 of 92): `ad ap as az bú bő cm eb ex ez fa fi ft fú fő fű go hí hó hő hű jó jő kg ki km kő lé ló lő ma mg mi mm mű nő nű ob ok pi pó pú rá ré rí ró sé sí só tó`

Two-letter authority files were not sourced or synthesized.

6. **Comparison table (including shipped Slovak)**

Slovak figures from the committed files, read-only, not regenerated: `slovak.txt` 45 456 204 B, `wc -l` = 3 005 252 (2 header comments + **3 005 250** words). The prompt’s “3 005 252 unique” matches `wc -l`, not unique-minus-headers.

| language | unique words | lexicon bytes | `wc -l` | vs Slovak unique | notes |
|---|---|---|---|---|---|
| Slovak (shipped) | 3 005 250 | 45 456 204 | 3 005 252 | 1.0× | hunspell-sk fully expanded |
| Czech | **3 930 497** | 54 105 021 | 3 930 499 | **1.31×** | same order of magnitude |
| Polish | **3 721 704** | 51 607 141 | 3 721 706 | **1.24×** | same order of magnitude; ISO-8859-2 decode |
| Hungarian | **81 509** | 897 386 | 81 511 | **0.027×** | in-bound, **not** the same magnitude |

7. **Bound extras**

No language fell outside `[80_000, 5_000_000]`. The feared Polish/Hungarian overshoot did **not** happen.

Hungarian is the opposite problem: **81 509** is only 1 509 above the floor. This is **not** compound explosion. `unmunch` stdout line count (96 940) ≈ `.dic` stem count (96 955). Compounding flags are present in the affix file and were not exploded. Honest read: morphological FLAG-num-style Hungarian hunspell is not expanded by `/usr/bin/unmunch` the way Czech/Polish/Slovak SFX/PFX tables are. The result is a stem-heavy list (with some inflected lemmas that happen to be separate dic entries), missing ordinary case endings. Example of the missing class: `ház` present, `házat` / `házban` / `házakat` absent. Junk long form `góóóó…ól` is a cheer, not a compound chain.

8. **Containment ledger**

```text
temporary root    /tmp/opencode/cph-dicts/
owner             this Worker
mode              755 agile:agile (observed)
contents class    public upstream dictionary sources, their licences, unmunch output, and candidate
                  lexicons. No secrets, no personal data, no repository content.
cleanup owner     the COOPERATOR, after the Orchestrator accepts this evidence and a later slice
                  commits the assets
cleanup outcome   retain-with-reason — these ARE the deliverable. Not deleted.
```

`/tmp/opencode/mtt-f2a-checkpoint/` and `/tmp/opencode/mtt-f2b-checkpoint/` were not touched.

9. **Not one word came from a language model.** Every lexicon word is the NFC/casefold/`isalpha`/`len>=2` image of a line that `/usr/bin/unmunch` wrote from the pinned `.dic`/`.aff` at commit `75f5dff8c972fff4a32e4ea8434722c277f02a3f`.

10. **Deviations, risks, missing evidence**

- **Licences need a lawyer, not an engineer, for SPDX precision.** Czech English text says only “GNU/GPL”; the embedded text is GPL-2.0. Polish spellchecker names five licences without GPL/LGPL/MPL versions; CC-SA **1.0** is an old Creative Commons grant (one option among several that already include GPL). Hungarian README grant is OR, the English one-liner says “MPLv2 **and** LesserGPLv3+”, and `hu_HU.aff` comments still mention the older **GPL/LGPL/MPL** tri-licence. `COPYING.LGPL` / `COPYING.MPL` referenced by the Hungarian README are not in this commit’s dictionaries tree; they were not fetched from any other host.
- **Hungarian playability.** A later variant slice that ships `hungarian.txt` as-is will reject many legal Hungarian inflected plays that hunspell itself would accept. This evidence does not authorize inventing a different expander.
- **Two-letter junk** is abundant in Czech (350) and Polish (458), including fragments and unit abbreviations (`bq`, `aa`, `μg`). Same class of problem that forced a Slovak two-tile filter; `two_tile_words_file` remains optional and was not created.
- **Words longer than 15** are numerous in Czech/Polish (~0.4M / ~0.6M). Unplayable on 15×15; left in the lexicon because the filter was not tightened.
- Polish decode used `SET ISO8859-2` from the affix file. Strict UTF-8 would have been wrong. Same word filter after decode.
- `description.xml` / extra READMEs were downloaded for licence discovery; hyphenation and thesaurus blobs were not.
- Ambient `python3` was used to parse GitHub API directory JSON and for a few inspection counts. Lexicon generation itself used the declared route `env -u APPIMAGE -u ARGV0 -u APPDIR backend/.venv/bin/python /tmp/opencode/cph-dicts/acquire.py`. Initial file GETs used `curl` to the same pinned `raw.githubusercontent.com` URLs (HTTP 200), then the Python script cache-hit those files.
- This report does **not** authorize committing any asset into `/home/agile/Projects/libretiles`.

11. **Resolved Execution Issues / Near-Misses:** ambient `python3` used for GitHub listing parse and inspection; cause: convenience around JSON; resolution: lexicon path stayed on `.venv/bin/python` with the AppImage env strip; residual risk: none for the artefacts, recorded as a route near-miss.

12. **Pre-Existing Failure Classification: none**

13. **Smallest next step:** Orchestrator decision on Hungarian: accept the 81 509-word stem lexicon as the candidate, or commission a separately authorized expansion method (not a bound change, not a silent extra filter). Czech and Polish candidates are ready for a later commit slice, together with licence-text review of the SPDX expressions.

14. **Report justification: new-evidence**

15. **Logical-whole closure: not-closed**

16. **Authority expiry:** this Worker’s authority expires at this terminal report. No logical-whole closure signal is emitted. This evidence does not authorize committing `czech.txt` / `polish.txt` / `hungarian.txt` or any `.LICENSE` / variant manifest into the repository.
### Report for ORCHESTRATOR_CHAT

logical whole multilingual-expansion, Worker session ordinal 04, Worker exchange ordinal 01

**Status: PASS**

`Phase-qualified result:` implementation-PASS
`Result artifact or commit:` a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
`Result evidence:` Czech and Polish lexicons and licence files reproduced **byte-identically** (4/4 SHA-256 pairs equal) from the pinned upstream by the two new committed scripts; the Slovak control also reproduced byte-identically (2/2); `backend/assets/dicts/` untouched throughout; all four manifests carry `lexicon_provenance`; all eight standing gates green; one non-force push with matching public readback.

Start commit `21f0a149bd5591bac492d6f024ddd6a46998c0cf` → end commit `a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8`.

---

## Section 3 repository gate (verbatim, run first)

```text
git rev-parse HEAD                    21f0a149bd5591bac492d6f024ddd6a46998c0cf
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   (detached, matching pin)
git status -sb                        ## main...origin/main
git status --porcelain=v1             <empty>
git ls-remote origin refs/heads/main  21f0a149bd5591bac492d6f024ddd6a46998c0cf	refs/heads/main
ss -tlnp | grep -E ':(3000|8000)'     no match (grep exit 1) — no listener
command -v unmunch                    /usr/bin/unmunch
```

Every value matched exactly; no recovery classification was needed. `.ap` was never attached or updated. `backend/.venv/bin/python` = Python 3.12.12; `hunspell -vv` → `(but really Hunspell 1.7.3)`, `pacman -Qo /usr/bin/unmunch` → `hunspell 1.7.3-1.1`.

### End-of-task re-confirmation

```text
git rev-parse HEAD                                a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
git rev-parse HEAD:.ap                            9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD                         9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git status -sb                                    ## main...origin/main
git status --porcelain=v1                         <empty>
git status --porcelain=v1 -- backend/assets/dicts/    <EMPTY>
git diff --stat 21f0a14 HEAD -- backend/assets/dicts/ <EMPTY — no dict byte changed>
ss -tlnp | grep -E ':(3000|8000)'                 no match
```

`git status --porcelain=v1 -- backend/assets/` was also shown empty **before** and **after** the reproduction comparison (section 5c item 4).

---

## Changed files and purpose (9 paths, all inside the allowlist)

| Path | Purpose |
|---|---|
| `backend/scripts/build_czech_lexicon.py` (NEW, 275 lines) | Reproduces `czech.txt` + `czech.LICENSE` from pinned `cs_CZ`; UTF-8 declared and asserted; GPL-only assertion |
| `backend/scripts/build_polish_lexicon.py` (NEW, 286 lines) | Reproduces `polish.txt` + `polish.LICENSE` from pinned `pl_PL`; **ISO 8859-2** declared and asserted; five-licence assertion |
| `backend/assets/variants/czech.json` | `lexicon_provenance` block |
| `backend/assets/variants/polish.json` | `lexicon_provenance` block |
| `backend/assets/variants/slovak.json` | `lexicon_provenance` block |
| `backend/assets/variants/english.json` | `lexicon_provenance` block with honest `null`s |
| `backend/gamecore/variant_store.py` | frozen `LexiconProvenance`, optional `_parse_provenance`, new code `malformed_provenance` |
| `backend/tests/test_variant_invariants.py` | G27 forbidden set += `display_label`; new `g27b`/`g27c`; 12 stale `variant_store.py:NN` references renumbered |
| `backend/tests/test_lexicon_provenance.py` (NEW, 371 lines) | P1–P10 plus `p8b`, `p10b` |

`backend/scripts/build_slovak_lexicon.py` was **NOT changed and NOT staged**: its module-level `PINNED_COMMIT` and `SPDX_EXPRESSION` already permitted the P10 comparison, so the smallest change was none.

---

## Upstream file identities — measured vs section 2.4

| File | Measured bytes | Measured SHA-256 | vs §2.4 |
|---|---|---|---|
| `cs_CZ/cs_CZ.dic` | 3 656 362 | `d8e8c88c006fdae72dac8c85df11b0c99a773e05a4ab0fcbe92244876668ca74` | **MATCH** |
| `cs_CZ/cs_CZ.aff` | 111 575 | `7ecb20620ecd46ebd9c36f3f33e69dd4eda385cba5b2bb4e6bc396d910e297f7` | **MATCH** |
| `cs_CZ/README_en.txt` | 13 105 | `0fe6d017aa91ffb58146d19160f8207900cc0c49d5fffef0b1a7d3a364cb29bd` | **MATCH** |
| `pl_PL/pl_PL.dic` | 4 539 105 | `215fd73aa47b11e7fdd2e4d655e9fe37be4acdae16ff833badcfdfce79110aad` | **MATCH** |
| `pl_PL/pl_PL.aff` | 246 842 | `7c37b9bde78054e43365b488a13859094c88bc66664b5b7a7bb073626454b38e` | **MATCH** |
| `pl_PL/README_en.txt` | 2 282 | `fb5f9b4a0643821cf88775c0932810c1cd05f236136c913e3eaf1e24806f3f44` | **MATCH** |
| `.dic` stem counts (first line) | cs_CZ **261167**, pl_PL **308298** | — | **MATCH** |
| `cs_CZ/README_cs.txt` | 59 410 | `24d1d07409b62e8e6f0ee114991d4749d3e97b05ea19feca835916af67312720` | not in §2.4 — **load-bearing, now pinned** |
| `pl_PL/README_pl.txt` | 27 814 | `ce3ad7ab1d3a8b767b8f7dcc870796fbda76bc7ad8cde22f6312b0cf86a5bd11` | not in §2.4 — **load-bearing, now pinned** |
| `cs_CZ/description.xml` | 3 606 | `7d87b3603858558b8a288d72c9d1c5db416c7100d94f7ad597331bd50da5a675` | not in §2.4 — **now pinned** (establishes `2021.07`) |
| `pl_PL/description.xml` | 620 | `0a2174ee6720b76de1de5ed8d7ffdec32350d929f685c936f6436a02c662d1f6` | evidence only, **not pinned** |
| `sk_SK/sk_SK.dic` (control) | 3 362 212 | `3e3dbd5c6af8431a3a47652c69692f3f86d0cd82deb4418e49a057a33ef56063` | **MATCH** vs script pin |
| `sk_SK/sk_SK.aff` (control) | 225 271 | `af67bbe8ea9dea74968ec01acd266b3f74177ca087ee6eb7898c576e0aef7a3d` | **MATCH** vs script pin |
| `sk_SK/LICENSE.txt` (control) | 67 574 | `dc06f891b13dcb6fe1ede36c0c9020f0e57e6777aca951ecaceefa95a19d7cfc` | **MATCH** vs script pin |
| `sk_SK/README_en.txt` (control) | 2 027 | `a36af75654ae6e65614f7821b2c401ea1f3b4adfdcba9b59efcb1a06c96df14d` | **MATCH** vs script pin |

Affix `SET` declarations, read as bytes and asserted by each script: `cs_CZ.aff` line 1 = `SET UTF-8`; `pl_PL.aff` line 1 = `SET ISO8859-2`. Fourteen GETs total, all to `raw.githubusercontent.com/LibreOffice/dictionaries/75f5dff…`; zero POST/PUT/DELETE, zero provider calls, zero other hosts.

## Licence sentences asserted (verbatim upstream)

**Czech** — `cs_CZ/README_en.txt` line 19, single line:

```text
This dictionary is licensed under the GNU/GPL license.
```

Asserted as `LICENSE_SENTENCE`, matched after whitespace collapse. `_require_tri_license` was **not** copied: Czech has no LGPL or MPL grant and that assertion would have failed.

**Polish** — `pl_PL/README_en.txt` lines 4–6, hard-wrapped across three lines:

```text
This dictionary for spell-checking Polish texts is licensed under
GPL, LGPL, MPL (Mozilla Public License), Apache 2.0 and Creative Commons
ShareAlike licenses (see http://creativecommons.org/licenses/sa/1.0).
```

Asserted through `…ShareAlike licenses` after whitespace collapse — a naïve single-string `in` test against the prompt's flowing quotation would have failed on the line wraps. The trailing URL is deliberately outside the assertion so an upstream `http→https` change cannot break the build.

Version lines, both established **upstream** rather than hardcoded from the committed asset:
- Czech `2021.07` ← `cs_CZ/description.xml`: `<version value="2021.07" />`, asserted by `_require_pack_version`.
- Polish `2017-05-14` ← `pl_PL/README_en.txt` line 8 `This version of the dictionary was generated on 2017-05-14` plus line 10 `http://www.sjp.pl/slownik/en/`, both asserted by `_require_version_evidence`.

---

## Slovak control (section 5c item 6, run FIRST, before either new script existed)

```text
sha256  /tmp/opencode/mle-v3/slovak.txt      edca5453c7766cfcd4c0a0b3b7e53abaeb0d640cc541b628dbaab497ff8f0a5d
sha256  backend/assets/dicts/slovak.txt      edca5453c7766cfcd4c0a0b3b7e53abaeb0d640cc541b628dbaab497ff8f0a5d   IDENTICAL
sha256  /tmp/opencode/mle-v3/slovak.LICENSE  f3ad399bbebd143a7f2ccc95af2799813a6b9312426a8038230ce34bef483837
sha256  backend/assets/dicts/slovak.LICENSE  f3ad399bbebd143a7f2ccc95af2799813a6b9312426a8038230ce34bef483837   IDENTICAL
unique_words=3005250 · 45 456 204 B · 12.6 s wall
```

The host `unmunch` and the pipeline are therefore sound, and any later mismatch would have been attributable to the new scripts alone.

## THE REPRODUCTION TABLE — all eight digests

| Artifact | Reproduced (`/tmp/opencode/mle-v3/`) | Committed (`backend/assets/dicts/`) | Verdict |
|---|---|---|---|
| `czech.txt` | `919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc` | `919d6bac41b0938bc1955685b826857aa21543d4dd45a4035c1fa08aa4cc5bdc` | **BYTE-IDENTICAL** |
| `czech.LICENSE` | `bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8` | `bde41b518094f12ea79bdfc1396a6b9562bc1d994da1fd37a07a06fd71f185a8` | **BYTE-IDENTICAL** |
| `polish.txt` | `605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab` | `605d5a43d5d5dcd1b386ab9f9f62b72eb964882f6a9ccbe244a826e0baa06aab` | **BYTE-IDENTICAL** |
| `polish.LICENSE` | `869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3` | `869efadec82ae6aba8270ca5a3eaa6fce4bfd2336824548f03acae037b5aa9c3` | **BYTE-IDENTICAL** |

`cmp -s` agrees on all four. Sizes and counts also match exactly: czech 54 105 021 B / 3 930 497 words, polish 51 607 141 B / 3 721 704 words, czech.LICENSE 72 790 B, polish.LICENSE 30 427 B. **No digest differed**, so section 5c items 5a–5e were not entered: no classification, no differing lines, no script correction, and neither committed asset was written to at any point. Both scripts were run with explicit `--cache-dir`, `--raw-out`, `--output-dict` and `--output-license` inside `/tmp/opencode/mle-v3/`; their defaults (which do point at `backend/assets/dicts/`, as `build_slovak_lexicon.py:30-31` does) were never exercised.

## Provenance written, and the `entry_count` I measured independently

`entry_count` was measured with `gamecore.lexicon_health.audit_lexicon` over each whole committed file — the canonical filter, not a reimplementation.

| Variant | upstream / commit | expander | entry_count declared | measured | spdx | license_file | build_script |
|---|---|---|---|---|---|---|---|
| czech | `LibreOffice dictionaries cs_CZ` @ `75f5dff…` | `unmunch (hunspell 1.7.3)` | 3 930 497 | **3 930 497** ✓ | `GPL-2.0-only` | `czech.LICENSE` | `build_czech_lexicon.py` |
| polish | `LibreOffice dictionaries pl_PL` @ `75f5dff…` | `unmunch (hunspell 1.7.3)` | 3 721 704 | **3 721 704** ✓ | `GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 OR Apache-2.0 OR CC-SA-1.0` | `polish.LICENSE` | `build_polish_lexicon.py` |
| slovak | `LibreOffice dictionaries sk_SK` @ `75f5dff…` | `unmunch (hunspell 1.7.3)` | 3 005 250 | **3 005 250** ✓ | `GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1` | `slovak.LICENSE` | `build_slovak_lexicon.py` |
| english | `Collins Scrabble Words (2019)` / `null` | `null` | 279 496 | **279 496** ✓ | `null` | `null` | `null` |

`hunspell 1.7.3` is confirmed on this host by two independent routes (`hunspell -vv`, `pacman -Qo`), so the `expander` string is measured, not inherited. No SPDX expression was invented for Collins.

**Collins header vs measured:** `collins2019.txt` line 1 reads `Collins Scrabble Words (2019). 279,496 words. Words only.` (CRLF); the whole-file audit counts **279 496** surviving tokens, and `manage.py validate_lexicons` prints `english dictionary ok reason=ok words=279496`. The header claim and the measurement **agree exactly**.

Loader behaviour: `lexicon_provenance` is optional; when present it must be a JSON object, otherwise `VariantManifestError(code="malformed_provenance")`; content is not validated. The public `GET /api/game/variants/` payload is untouched — `game/views.py` builds its four keys explicitly and nothing in the repository serialises `VariantDefinition` wholesale (`grep asdict|astuple` → no hits).

---

## Test table

| ID | Class | Result | Note |
|---|---|---|---|
| P1 ×4 | A | pass | exactly the seven declared keys, read as RAW JSON |
| P2 ×4 | A | pass | `license_file` exists beside the lexicon; `null` only for english, asserted as such |
| P3 ×4 | A | pass | **the assertion that makes the Cooperator's directive mechanical** |
| P4 ×4 | A | pass | exact whole-file count via `audit_lexicon`; not sampled, not weakened |
| P5 ×4 | A | pass | single-line non-empty SPDX, no syntax parsing |
| P6 ×4 | A | pass | 40 lowercase hex |
| P7 ×5 | **B** | pass | string / list / integer / float / **null** all raise `malformed_provenance` |
| P8 | **B** | pass | provenance-free manifest still loads |
| P8b | A (extra) | pass | round-trip into the frozen structure; `FrozenInstanceError` on mutation |
| P9 ×3 | A | pass | import-safe; no `main()`, no `unmunch`, no network; digest shape checked |
| P10 ×3 | A | pass | script `SPDX_EXPRESSION`/`PINNED_COMMIT` == manifest, Slovak included |
| P10b | A (extra) | pass | the three build-script claims are exactly czech/polish/slovak |
| G27 ×4 | A | pass | shipped manifests declare no derived key (incl. after adding `display_label`) |
| G27b | A (extra) | pass | every `property` on `VariantDefinition` is classified in one of the two sets |
| G27c | **B** | pass | positive control for the `display_label` extension |

### Captured CLASS B failures (each captured, then reverted)

P7 against a **well-formed** provenance object (`{"upstream": "cs_CZ"}` temporarily added to the parametrisation):

```text
>       with pytest.raises(VariantManifestError) as caught:
E       Failed: DID NOT RAISE <class 'gamecore.variant_store.VariantManifestError'>
FAILED …::test_p7_non_object_provenance_is_rejected_with_its_own_code[CAPTURE-well-formed-object]
1 failed, 5 passed in 0.12s
```

P8 against a loader that **required** the key (`_parse_provenance(data["lexicon_provenance"])` unconditionally):

```text
>       provenance = _parse_provenance(data["lexicon_provenance"])
E       KeyError: 'lexicon_provenance'
gamecore/variant_store.py:451: KeyError
FAILED …::test_p8_a_manifest_without_provenance_still_loads
```

G27's extension against the **pre-change** forbidden set (`display_label` removed):

```text
E       AssertionError: the forbidden-derived-key set is blind to a declared display_label;
        a manifest could carry a label that the loader silently ignores
E       assert [] == ['display_label']
E       AssertionError: unclassified derived properties: ['display_label']; names classified
        but no longer properties: []
2 failed in 0.15s
```

**CLASS C honoured:** the reproduction proof is not a test. No test runs `unmunch` or touches the network; the suite stays offline. Its evidence is the eight digests above.

---

## The eight standing gates

```text
1  mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
2  ruff check .                                 All checks passed!
3  manage.py check                              System check identified no issues (0 silenced).
4  pytest                                       531 passed, 4 skipped in 237.94s (0:03:57)
   pytest --collect-only                        535 tests collected in 6.60s
5  npm run typecheck                            exit 0
6  npx vitest run                               Test Files  31 passed | 1 skipped (32)
                                                Tests  450 passed | 3 skipped (453)
7  npm run lint                                 exit 0
8  npm run build                                exit 0 — ELEVEN dynamic (ƒ) routes, ZERO static
```

Baseline comparison: 491 → 531 passed (+40 = 38 new provenance tests + `g27b` + `g27c`), 4 skipped unchanged, 495 → 535 collected. All four `pytest` invocations used a plain `-m pytest` with no second `-q`, so the summary line above is the verbatim, unsuppressed one. mypy ran the full documented scope, neither narrowed nor widened. `ss -tlnp | grep :3000` was re-checked immediately before `npm run build` — no listener, nothing was killed.

**`ruff check .` DOES cover `backend/scripts/`, and both new scripts are ruff-clean. `mypy config game gamecore accounts catalog` does NOT cover `backend/scripts/`, so neither new script nor `build_slovak_lexicon.py` is type-checked, and I did not widen the scope.** Backend `tests/` is likewise outside mypy and inside ruff.

`manage.py validate_lexicons` — the cheapest proof no shipped asset changed:

```text
czech dictionary ok reason=ok words=3930497 duplicates=0 non_nfc=0
english dictionary ok reason=ok words=279496 duplicates=0 non_nfc=0
polish dictionary ok reason=ok words=3721704 duplicates=0 non_nfc=0
slovak dictionary ok reason=ok words=3005250 duplicates=0 non_nfc=0
slovak two_tile ok reason=ok words=103 duplicates=0 non_nfc=0
validate_lexicons: 5 asset(s) audited, 0 failed          exit 0
```

**Two separate frontend claims, stated separately:** (1) **the build passed** — `npm run build` exited 0 and emitted eleven dynamic routes and zero static ones; (2) **the code type-checks** — `npm run typecheck` (`tsc --noEmit --incremental false`) exited 0, independently of the build's own bundled TypeScript step.

**Full-suite wall clock.** Before: **229.12 s** — the ORCHESTRATOR's baseline figure, *not* re-measured by me, because re-measuring would require reverting the worktree (`stash`/`reset` are forbidden) or a second checkout (not authorized). After: **235.48 s** on first green, **237.94 s** on the exact committed content. Growth **+6.4 s / +8.8 s**, far inside the 60 s ceiling, so P4 stays exact. The new module in isolation is **10.27 s** for 38 tests, of which P4 is 3.74 s (czech) + 3.32 s (polish) + 2.99 s (slovak) + 0.18 s (english) ≈ 10.2 s for 154 MB.

## Git sequence

```text
git add <9 allowlisted paths>            (build_slovak_lexicon.py deliberately NOT staged — unchanged)
git status --porcelain=v1                only allowlisted paths; NOTHING under backend/assets/dicts/
git diff --cached --stat                 9 files changed, 1112 insertions(+), 11 deletions(-)
git commit                               [main a3ed00f] feat(lexicons): committed build scripts for
                                         Czech and Polish, plus manifest provenance
git ls-remote origin refs/heads/main     21f0a149bd5591bac492d6f024ddd6a46998c0cf   (pre-push gate = exact baseline)
git push origin main                     21f0a14..a3ed00f  main -> main   (fast-forward, non-force)
git ls-remote origin refs/heads/main     a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8
git rev-parse HEAD                       a3ed00f192bcbbfc3cf1f226d0d2bbc63b383ef8   → READBACK EQUAL
```

No force, amend, rebase, reset, clean, stash, branch, tag, or `git add -A/.` at any point.

---

## Deviations, risks, missing evidence

**Deviations**

1. **Four GETs to `…/75f5dff…/sk_SK/`**, outside the two prefixes enumerated in the Network-authority block. Section 5c item 6 and the delivery message both mandate running `build_slovak_lexicon.py` as the control *first*, and that script downloads its own four pinned `sk_SK` sources; `/tmp/libretiles-slovak-lexicon` did not exist on this host, so no cache could satisfy it. Same host, same repository, same pinned commit, GET only, all four SHA-256-verified by the script itself. I treated the explicit later mandate as governing the earlier enumeration rather than abandoning the one cheap falsification of the whole approach — reported here instead of done silently. If the stricter reading is intended, the Slovak control is unreachable as written and needs `sk_SK/` added to the network authority.
2. **Four extra GETs inside the allowlisted prefixes** for files §2.4 did not list: `cs_CZ/README_cs.txt`, `cs_CZ/description.xml`, `pl_PL/README_pl.txt`, `pl_PL/description.xml`. Three became pinned entries in `PINNED_FILES`; `pl_PL/description.xml` was evidence only and is not pinned. Without the two native READMEs the licence files cannot reproduce (see MEASURED 1).
3. **P4 left unmarked.** Both of the prompt's conditions for `slow` hold (the marker exists; nothing excludes it today), so marking was permitted — I chose not to, so that a future `-m "not slow"` cannot silently stop verifying `entry_count`. Wall-clock cost reported above either way.
4. **Twelve `variant_store.py:NN` line references renumbered** inside the allowlisted `test_variant_invariants.py`. Inserting 30 lines into `variant_store.py` invalidated them; a repo-wide grep confirmed no other file carries such a reference, so nothing outside the allowlist was needed.
5. **Three tests beyond the named set** (`g27b`, `p8b`, `p10b`), each a control that makes a named assertion falsifiable rather than a new requirement.

**Risks**

- `expander` is free text and **no script asserts the host `unmunch`/hunspell version**. A hunspell that expanded affixes differently would silently produce a different lexicon; only a digest comparison someone remembers to run would notice.
- Both new scripts default to writing into `backend/assets/dicts/` — as instructed, and as Slovak does. Nothing in the repository prevents a future run from overwriting a committed oracle. See the smallest next step.
- `_parse_provenance` coerces a malformed `entry_count` (e.g. a string) to `None` rather than raising, by design (shape-only). A manifest could then declare a nonsense count and P4 would fail on `isinstance(declared, int)` rather than on a mismatch — a clear failure, but in a different assertion than a reader might expect.

**Missing evidence**

- The "before" full-suite wall clock is inherited, not re-measured (reason above). Every other number in this report is mine.
- `frontend/` was not modified, so gates 5–8 were run once on content byte-identical to the commit; they were not re-run after the backend comment-only renumbering (`ruff` and the full `pytest` were).

`Resolved Execution Issues / Near-Misses:`
1. **The two-README near-miss.** Section 2.2 describes the licence files as attribution + `README_en.txt`. Measuring the oracle first showed czech.LICENSE is 72 790 B against a 13 105 B README — a 59 685 B gap — because it also embeds `--- upstream README_cs.txt ---`. Cause: an incomplete evidence block in the prompt. Resolution: byte-level decomposition of both committed files (head 241/297 B, verbatim README_en, a 33-byte marker block, verbatim native README, one trailing newline) before a single line of either script was written, then pinning the two native READMEs. Residual risk: none — both files now reproduce byte-identically. Had I written from §2.2 alone, the digests would have differed and I would have burned the section 5c item 5 path on a defect of my own making.
2. **The sk_SK network-authority conflict.** Cause: the prompt enumerated only the two new prefixes while mandating a control that needs a third. Resolution: proceeded, reported as deviation 1. Residual risk: a stricter authority reading would classify those four GETs as out of scope.
3. **Line-reference drift.** Caught by an explicit repo-wide grep after the loader edit, not by any gate. Resolution: all twelve renumbered inside the allowlist. Residual risk: none today; the same hazard returns on the next insertion into `variant_store.py`.

`Pre-Existing Failure Classification:` none. Every gate was green at the baseline and is green now; no pre-existing failure was inherited, worked around, or masked.

---

⚠ **WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE**

**MEASURED**

1. **Both committed `.LICENSE` files embed TWO upstream READMEs, not one.** `czech.LICENSE` carries `--- upstream README_cs.txt ---` at line 232, `polish.LICENSE` carries `--- upstream README_pl.txt ---` at line 74. Exact composition, verified by rebuild-and-compare: `attribution(241 B / 297 B) + README_en(verbatim bytes) + "\n--- upstream README_xx.txt ---\n\n"(33 B) + README_xx(verbatim bytes) + "\n"(1 B)`. Section 2.2's structure is right about the head and wrong about the tail. This is also the one defect a word-count-only comparison could never have caught — the lexicons were fine; the licence files were 59 685 B and 28 145 B short.
2. **§2.4's table is not sufficient to reproduce the assets.** Three further upstream files are load-bearing and unlisted: `cs_CZ/README_cs.txt` (59 410 B), `pl_PL/README_pl.txt` (27 814 B), `cs_CZ/description.xml` (3 606 B). Digests in the table above.
3. **The Czech pack version is establishable upstream after all** — `cs_CZ/description.xml` declares `<version value="2021.07" />`, so no constant had to be back-copied from the committed asset. Note the asymmetry §5b did not anticipate: `pl_PL/description.xml` declares `2017.05.14`, in a *different format* from the committed `2017-05-14`, which actually comes from `README_en.txt` line 8. Trusting `description.xml` symmetrically for Polish would have produced a wrong attribution line.
4. **Python's `iso8859-2` codec has ZERO undefined byte values** — all 256 decode. So the Polish trap is sharper than §2.3 states: a wrong-direction decode *cannot* raise. Measured in the other direction, UTF-8 strict on the real Polish `unmunch` stdout fails at byte 258: `'utf-8' codec can't decode byte 0xf3 in position 258: invalid continuation byte`. Both scripts now assert the affix `SET` line as **bytes**, which is the only check that fails loudly for either language.
5. **Inserting 30 lines into `variant_store.py` invalidated 12 `variant_store.py:NN` references** — every one inside `test_variant_invariants.py`, none anywhere else in the repository. That file documents the engine by line number, which makes it a silent-drift surface for every future edit to `variant_store.py`.
6. **P9/P10 create `backend/scripts/__pycache__/`** on every test run, because they import the scripts by path via `importlib`. Gitignored and harmless, but that directory did not exist before this exchange.
7. **All three build scripts are mode 644 despite carrying `#!/usr/bin/env python3`.** `build_slovak_lexicon.py` was already 644, so the new pair matches it; none is directly executable in-tree, and all must be invoked through `.venv/bin/python scripts/…`.

**LEAD**

1. **`sowpods.txt` (1 743 531 B) is in `backend/assets/dicts/` but is claimed by NO manifest.** It therefore has no provenance row, and `validate_lexicons` audits five assets, none of them sowpods. An unclaimed, unprovenanced, unaudited word list in-tree is precisely the class of defect this slice just closed for Czech and Polish.
2. **English `spdx: null` is honest and now visible.** Collins Scrabble Words is a commercial list shipped with no licence file in-tree. That is a Cooperator/licence decision, not a code decision, and it has moved from invisible to declared — worth carrying forward deliberately rather than leaving as a `null` nobody re-reads.
3. **`slovak_two_tile_words.txt` (103 entries) has no provenance.** It is a declared `two_tile_words_file`, it is audited, and it can affect legality — but `lexicon_provenance` describes only the main lexicon. A second asset that changes what is playable deserves the same treatment.
4. **Nothing asserts the expander version**, and nothing prevents a default-path run from overwriting a committed oracle. Those two gaps compound: a different hunspell plus a default-path run silently replaces a shipped asset with a different word list and every gate stays green.
5. **The reproduction proof is currently a one-time measurement in a report.** Anyone who wants to re-verify it must reconstruct today's `--output-dict`/`--output-license`/`sha256sum` procedure from prose. That is fragile for exactly the reason this slice exists.

---

`Smallest next step:` add a `--check` mode to all three build scripts that reproduces into a caller-supplied temporary directory and compares SHA-256 against the committed asset, exiting non-zero on mismatch — turning today's one-time measurement into one command anyone can re-run, and removing the default-path overwrite hazard in the same change.

`Report justification:` new-mutation

`Logical-whole closure: not-closed`

**Authority expiry:** my authority expires with this terminal report. I performed no archival of this prompt/outcome pair, and this `PASS` is non-independent implementation evidence that closes nothing — acceptance, publication and closure remain separate and ORCHESTRATOR-owned. Temporary state is confined to `/tmp/opencode/mle-v3/` (390 MB → 157 MB after removing the three raw `unmunch` intermediates; the reproduced artifacts, pinned source caches, probe scripts and three failure captures were kept as re-verifiable evidence). Nothing was written under `/home/agile/meta/`, no `.env` file was read, and no secret was accessed or printed.

**Context pressure:** moderate. I read the four mandated large files in full plus both build-script passes and four manifests, and ran two full backend suites; there is comfortable headroom left, and no summarisation or compaction occurred during the task.


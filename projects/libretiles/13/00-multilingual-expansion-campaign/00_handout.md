# Orchestrator handout — logical whole `13/00 multilingual-expansion-campaign`

Artifact class: **restoration synthesis and campaign handout. Evidence, not
authority.** It grants **no** repository, implementation, Git, deployment,
production, account, filesystem, or external-service mutation authority. Task
authority comes only from your own prompts; material product decisions come only
from the Cooperator.

Written 2026-09-03 by the Orchestrator of `12/00 multilingual-expansion`, as its
closing act, after that whole was superseded by a materially changed objective.

Restoration classification: **PASS.** The objective is bounded, the state is
measured, no strategic question is open, and the next step is executable
immediately.

---

## 0. Read these three things before anything else

```text
1  /home/agile/meta/projects/libretiles/12/00-multilingual-expansion/91_orchestrator-handout.md
   41 451 B, 17 sections. THE VERIFIED STATE. Repository identity, the corrected gate
   route, the six prompt defects and their rules, the F2b freeze, the deferred PRD chain,
   the Cooperator's autonomy grant, and what comes after. It is accurate at ad4ce03 and
   this file does NOT repeat it.
2  ./00_handout.md  — this file. THE CAMPAIGN: the expanded objective, the capability
   layers, the batch structure, and the ledger you must maintain.
3  /home/agile/meta/projects/libretiles/12/00-multilingual-expansion/98_supersession.md
   why 12/00 was superseded rather than amended, which six closure conditions it
   SATISFIED (they are your baseline) and which twelve it carried forward to you.
```

⛔ **Precedence, and it is a chain of four.** `11/01` and `11/02` were superseded by
`12/00`; `12/00` is superseded by **this whole**. Each supersession is written, not
assumed, because RF-19 (`AP.md:255-262`) says a materially changed objective begins
a new identity and does not silently absorb an old one. Where any two of these
documents disagree, the later wins and the disagreement is named:

```text
11/01/98_supersession.md · 11/02/98_supersession.md · 12/00/98_supersession.md
```

---

## Handoff capsule

```text
project            Libre Tiles — Next.js 16.3.4 + Django 5.2.17 Scrabble-like web app
repository         https://github.com/cisarik/libretiles
working copy       /home/agile/Projects/libretiles
main               ad4ce038e1bd3511bdd5b7431eb9c163d4788130
public readback    git ls-remote origin refs/heads/main == ad4ce03    verified 2026-09-03
porcelain          EMPTY
AP pin             .ap gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656, submodule HEAD equal
active Worker      none
active mutation    none
Meta repo          /home/agile/meta, pushed
your first Worker session ordinal   01   (a NEW logical whole resets both coordinates)

playable today     english slovak czech polish        — 4 of ~24 target editions
UI locales today   en sk cs pl                        — 300 keys each, 1 200 strings
foundation done    atomic tile tokens in the pure engine and in persistence;
                   a generic per-variant invariant harness; fail-closed readiness;
                   provenance in every manifest; a committed reproducible build script
                   per lexicon with a byte-exact --check; the expander pinned
blocked            multi-code-point tiles END TO END — the seven-guard F2b freeze stands
                   Hungarian gameplay — the lexicon is ~301 M forms minimum
```

---

## 1. Coordinates, and the one thing to get right first

```text
Prior logical whole identity: multilingual-expansion
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
```

That is the exact shape `PROMPT_CONTRACTS.md:497-505` fixes for a changed
objective: **both ordinals reset to `01`**, and the prior identity is named. Do not
continue `12/00`'s session numbering.

Your Meta directory is
`/home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/`.
You own every artifact in it. `00_handout.md` is reserved for this file and is not
an exchange. Filenames follow the Meta contract:
`NN_<phase>_XX.md` + `NN_report_XX.md`, where `XX = AP exchange ordinal − 1`, so
your first pair is `01_<phase>_00.md` + `01_report_00.md`.

---

## 2. The objective — the Cooperator's own words, verbatim and governing

⛔ This section is his text. It is the **objective**, and it is the only part of this
handout that is a material product decision rather than my synthesis. Quoted at
length precisely so no successor paraphrases it.

> The objective is to continue the current Libre Tiles multilingual work and
> implement **all remaining practical mainstream Scrabble language variants that
> can reasonably be supported by the project**, not merely one additional
> language.
>
> Do NOT stop after Hungarian, German, French, or another individual language.
>
> Treat the existing English, Slovak, Czech, and Polish implementations as the
> established baseline and systematically expand from them toward the broadest
> practical set of playable Scrabble variants.
>
> The desired end state is that Libre Tiles supports as many of the established
> international Scrabble language editions as can be implemented correctly with
> reliable tile distributions, rules, dictionaries, and UI localization.
>
> You should therefore: 1. identify the remaining practical Scrabble language
> variants; 2. classify them by implementation complexity; 3. determine which are
> already supported by the current engine architecture; 4. implement the reusable
> missing capabilities where necessary; 5. then continue adding the languages
> systematically; 6. add the corresponding UI locales wherever practical;
> 7. continue until the planned mainstream language set is exhausted or a genuinely
> separate architectural boundary is reached.
>
> Do not require the COOPERATOR to request each language individually.
>
> This is a multilingual expansion campaign, not a one-language task.
>
> Internally you MAY and SHOULD organize implementation into small coherent
> batches, commits, and validation checkpoints so failures remain attributable.
> That internal batching is an implementation technique only. It does NOT reduce
> the overall scope or objective.
>
> After completing one internal batch, continue to the next one without requiring a
> new product decision merely because the language changed, provided that: the next
> language is already inside the approved multilingual-expansion scope; no new major
> architectural boundary is crossed; reliable gameplay data and legally usable
> dictionary assets are available; tests remain green.
>
> A new architectural decision is required only when a language introduces a
> materially different class of behavior that the approved foundation does not
> cover. Examples include a future RTL foundation or another genuinely different
> game model.
>
> Do NOT artificially stop at an arbitrary number of languages. Do NOT interpret
> references to "28 languages" as a strict implementation constant either.
>
> The real goal is: **maximize the number of correctly playable, maintainable,
> mainstream Scrabble language variants supported by Libre Tiles.**
>
> For ordinary supported languages, strive toward a state where adding a variant
> primarily consists of: sourced tile distribution and scoring; alphabet/tile
> ordering metadata; dictionary; short-word authority where required;
> variant-specific normalization/rules metadata; UI translation; automated tests —
> rather than new core-engine branches.
>
> When multiple languages share the same architectural capability, implement the
> capability once and then continue adding every applicable language. Do not create
> language-slug-specific hacks when a generic variant rule can express the
> behavior.
>
> The Worker should maintain a running implementation ledger containing, for every
> candidate language: language / variant; gameplay status; UI-localization status;
> dictionary status; distribution source; special-rule requirements; architectural
> capability required; tests; blockers. The Worker should use that ledger to
> systematically drive the multilingual expansion forward rather than waiting for
> the COOPERATOR to name each next language.

### 2.1 His target language list, verbatim

```text
English  Slovak  Czech  Polish  Hungarian
German  French  Italian  Spanish  Portuguese  Dutch
Danish  Swedish  Norwegian  Finnish  Icelandic
Croatian  Slovenian
Turkish
Greek  Bulgarian  Russian
Afrikaans  Malay
```

Twenty-four entries; four are shipped. **Note what is deliberately absent: Hebrew,
Arabic, Thai.** His own analysis names RTL and Thai multi-realization tiles as
genuinely separate architectural boundaries, and clause 7 of the objective stops
this campaign at exactly such a boundary. So this list **is** the planned mainstream
set, and reaching its end is the finish line — not an arbitrary stop.

⚠ **Two calibration notes he made himself, and they are load-bearing.** *"Do NOT
interpret references to '28 languages' as a strict implementation constant"* — Mattel
stated 28 in April 2026 and that is context, not a target. And *"Do NOT artificially
stop at an arbitrary number"* — so if a language on the list turns out to have no
licence-clean lexicon, that is a **recorded blocker in the ledger**, not a reason to
declare the campaign finished.

### 2.2 The one clause that governs your prompting cadence

> Do not require the COOPERATOR to request each language individually.

⛔ This is an explicit standing grant and it changes how you work. Combined with his
autonomy instruction of the same day — *"CHCEM ABY SI PRACOVAL AUTONOMNE …
NEVYRUSUJ … AK MI BUDES CHCIET DAT OTAZKY PROSTE POUZI ODPOVEDE KTORE
DOPORUCUJES"* — you do **not** stop between languages inside an approved batch. You
stop only at the four conditions he names: a new architectural boundary, missing
reliable gameplay data, an unusable dictionary licence, or a red gate.

⚠ **What that grant does NOT waive**, and protecting it is your job: it does not
lower an evidence tier, it does not remove the rendered-output rule, and it does not
touch decision 10 (no screen reader, accessibility claims closed by inspection only).
`12/00/91_orchestrator-handout.md` section 11 states all three.

---

## 3. His research reconciled against the code — I measured every row

He supplied a long analysis naming roughly ten architectural layers. **Most of them
already exist.** Below is what I measured in the checkout at `ad4ce03`, so your first
Worker does not spend a session re-deriving it. Verify each yourself; a number you
did not count is not a measurement.

### 3.1 ALREADY PRESENT — do not re-implement, do not "add"

```text
HIS LAYER 1: a tile is a physical object, not a letter
   gamecore/types.py:6-11   TileToken = str, with the invariant comment: "len(str) is a
       resource bound only — physical tile count is always the length of a token container."
   variant_store.py:22      MAX_TILE_TOKEN_CODEPOINTS = 16
       ⇒ DZS (3 code points), L·L (3), and even Thai ฆ/ซ (3) all FIT the bound today.
   variant_store.py:147     canonicalize_tile_token: trim → NFC → upper → NFC
   ⇒ the pure engine and persistence are token-safe. F1 at 9f0c5b8 and F2b at 8c00a33.

HIS LAYER 6: alphabet order, physical tiles and dictionary alphabet are three things
   variant_store.py:338-343  alphabet_order is REQUIRED and DECLARED, never derived
   variant_store.py:380-388  the SUBSET invariant, ONE DIRECTION, code tile_not_in_alphabet
   ⇒ measured: sk has 5 letters with no tile (DZ DŽ CH Q W), cs has 3 (CH Q W), hu will
     have 6 (DZ DZS Q W X Y). His concern is ALREADY the shipped design. Requiring the
     reverse is WRONG and would fail on shipped Slovak.

HIS LAYER 9: do not hardcode 100 tiles or 2 blanks
   variant_store.py:75-77   total_tiles = sum(lt.count for lt in self.letters)  — DERIVED
   ⇒ Welsh 105, Slovak-Mattel 110, Greek 104, Portuguese 120 with three blanks all work
     with no code change. `total_tiles` is not a manifest field and must not become one.

HIS "can't build DD from two D" RULE — already a declared field
   variant_store.py:292     forbidden_token_sequences, an array of token arrays, checked
       against COMPLETE FORMED WORDS ONLY (word_authority.py:118-129)
   ⇒ Welsh DD, Croatian DŽ/LJ/NJ, Spanish CH/LL/RR and Catalan NY are expressible in DATA
     today. No engine change. This is the single largest thing his analysis under-credits.

HIS LAYER 4's derivation half
   variant_store.py:95-106  playable_letters — tile tokens only, blank excluded, ordered by
       alphabet index, with the docstring "Blank targets come from the TILE SET ordered by
       alphabet index, never from alphabet_order"
   ⇒ that is why a Slovak player cannot assign a blank to CH.
```

### 3.2 THE HOOK EXISTS, THE DATA MODEL DOES NOT SELECT IT

These are the cheap ones, and each unlocks several languages.

```text
HIS LAYER 2: face versus lexical realization  (Catalan club Q → QU)
   variant_store.py:108-114
       def lexical_contribution(self, token): return token     # identity today
       def tile_display(self, token): return token             # identity today
   ⇒ the EXTENSION POINTS are named and in the right place. What is missing is a manifest
     field that makes them non-identity. gamecore/types.py:35-40 already carries
     WordFound.tokens beside the lexical word, so the plumbing is there too.

HIS LAYER 5: per-language canonicalization  (French É→E; German ß→SS but Ä≠A; Turkish I≠İ)
   word_authority.py:66     normalize: Callable[[str], str] = _nfc_casefold, PER INSTANCE
   ⇒ the BOUNDARY is correct — gameplay normalization is already not universal. No manifest
     field selects it. This is the briefing's gap G5, recorded there as "do not add
     speculatively; add it when a supported variant needs it." ⛔ THAT MOMENT HAS ARRIVED:
     French, German and Turkish are all on his list and all three need it.
```

### 3.3 GENUINELY ABSENT — the real capability work

```text
HIS LAYER 4's DATA half: variant-declared blank targets
   MEASURED: there is NO blank_targets field. `dir(variant_store)` contains only
   _BLANK_ALIASES. Blank targets are derived from the tile set, full stop.
   ⇒ Catalan forbids blank→K/W/Y; Turkish forbids blank→Q/W/X; Slovak Mattel explicitly
     ALLOWS blank→Q/W. Derivation cannot express a restriction. REAL and OPEN.

HIS LAYER 3: multi-realization tiles  (Thai ฆ/ซ — one physical tile, two possible values)
   MEASURED: VariantLetter is exactly (letter, count, points). One token, one meaning.
   ⇒ REAL and OPEN, and it is the most interesting idea in his analysis because it
     GENERALIZES THE BLANK: a blank becomes {face:"?", realizations:[…], points:0} and the
     special case disappears. ⚠ But Thai is NOT on his target list, so this capability has
     no language on the campaign that needs it. Design the data model so it is not
     PRECLUDED; do not build it. That is the difference between an extension point and
     speculative machinery.

HIS LAYER 10: language ≠ ruleset  (Spanish has international / NA / LatAm distributions)
   MEASURED: `variant_name` EXISTS as a VariantDefinition field and is declared by NO
   shipped manifest, so display_label's f"{language} – {variant_name}" path is UNEXERCISED
   by any test in the repository. HALF-PRESENT: the field is there, untested.
   ⇒ Spanish is on his list and it is exactly the language that needs it.

HIS LAYER 8: RTL
   MEASURED: nothing. And ⛔ it is OUT OF SCOPE for this campaign by his own clause 7 —
   Hebrew and Arabic are absent from his list precisely because RTL is "a genuinely
   separate architectural boundary." Record RTL observations as deferred notes; do not
   build toward it, and do not let a Worker generalize "for RTL later."
```

### 3.4 ⛔ Where his supplied draft planner prompt is STALE — do not deliver it

He also supplied a long *"DRAFT FOR ORCHESTRATOR APPROVAL"* planner prompt. It is a
good document and it must **not** be used as-is. Measured reasons:

```text
S1  Its logical whole is `multilingual-variable-length-tile-token-foundation` at baseline
    f26e92a61c65269c4d7d5a620665040e65466e59. That is ERA 11. It is the prompt that BECAME
    11/01, and 11/01's F1, F2a and F2b have SINCE LANDED (9f0c5b8, 3fd1a81, 8c00a33).
    Delivering it would ask a Worker to plan work that is already committed.
S2  Its section 7.1 says variant_store.py "has been observed to reject non-blank tile
    strings when len(letter) != 1". FALSE at ad4ce03: that check is gone, and
    MAX_TILE_TOKEN_CODEPOINTS = 16 replaced it.
S3  Its section 7.1 says the loader "sorts loaded letters by their string value rather than
    necessarily retaining declared variant order". TRUE, and it is DELIBERATE and LOCKED:
    variant_store.py:393 sorts by token, that order feeds `distribution` which is the
    pre-shuffle bag sequence, and changing it would change every seeded bag in the
    repository. `alphabet_order` is the separate declared order. Do not let a Worker "fix"
    this.
S4  Its section 9 asks whether "two-letter allowlist" should be renamed. ALREADY DONE:
    the field is `two_tile_words_file`, the loader is `load_two_tile_words`, and
    WordAuthority.route(word) returns "forbidden" | "two_tile" | "main".
S5  Its section 18 says SelectedVariantSlug = "english" | "slovak". FALSE: it is
    `string`, and GET /api/game/variants/ has served a dynamic catalog since A1 at 2917251.
S6  Its section 33 asks whether to build a variant catalog endpoint. ALREADY SHIPPED.
S7  Its sections 24 and 32 assume the Cooperator will hand-source dictionaries. SUPERSEDED:
    his 2026-09-03 instruction is that they be DOWNLOADED BY A COMMITTED SCRIPT, and three
    such scripts now exist with byte-exact --check reproduction.
S8  Its section 39 lists `poetry run` gates. NOT USABLE in a Worker boundary. Use the
    corrected route in 12/00/91_orchestrator-handout.md.
```

⚠ **What to salvage from it, because it is genuinely valuable:** its section 29
assumption-search list, its section 31 migration compatibility matrix, its section 38
risk register shape, and its section 44 "trace atomic tile identity across twenty-eight
surfaces" quality bar. Those four are exactly what your C1 planner prompt needs. Lift
them; do not lift the baseline, the reconnaissance, or the questions already answered.

---

## 4. The campaign structure — capabilities first, then languages in batches

His clause: *"When multiple languages share the same architectural capability,
implement the capability once and then continue adding every applicable language."*
That is the whole design. Capabilities are **C**, language batches are **B**, and a
batch never starts before its capability lands.

### 4.1 Capabilities, in dependency order

```text
C1  MULTI-CODE-POINT TILES END TO END.        tier E3.   inherited from 12/00 conditions 8-10, 14
    All seven F2b guards removed TOGETHER with state_schema_version 4, BoardCell[][] on the
    wire, localStorage v4, board/rack/blank/draw rendering, evaluate_scoring_move re-pointed
    at WordAuthority, _word_passes_dictionary deleted.
    ⛔ PLANNER WORKER FIRST (manual delivery), then a fresh implementation session, then
    FRESH INDEPENDENT ACCEPTANCE THAT CANNOT BE YOUR SUBAGENT (AP.md:1395-1405).
    UNLOCKS: hu · hr (DŽ LJ NJ) · and every future multigraph edition.
    ⛔ The guards come out TOGETHER. DEFECT_LEDGER.md:806-826: "if the backend emitted v4
      while the frontend still read v3, the product would be broken between two slices."

C2  VARIANT-DECLARED BLANK TARGETS.           tier E2.   real and open, section 3.3
    A manifest field that RESTRICTS the derived set; absent means "all playable tiles",
    which preserves en/sk/cs/pl byte-unchanged.
    UNLOCKS: tr (no blank→Q W X) · and it makes sk's explicit blank→Q/W allowance testable.

C3  VARIANT-DECLARED NORMALIZATION.           tier E2.   the hook exists, section 3.2
    A manifest field selecting the gameplay normalization WordAuthority already accepts
    per instance. Data-defined rules, never a global strip_diacritics().
    UNLOCKS: fr (É→E) · de (ß→SS but Ä≠A) · tr (I≠İ, and Â Î Û play as A İ U) · is · da/sv/no.
    ⛔ Do NOT apply it to sk/cs/pl. Slovak A≠Á is a LOCKED fork. Absence must mean today's
      behaviour exactly.

C4  FACE VERSUS LEXICAL REALIZATION.          tier E2.   the hook exists, section 3.2
    A manifest field that makes lexical_contribution() non-identity.
    UNLOCKS: a Catalan-style Q→QU edition, and it is the honest place to STOP: design the
    field so multi-realization (his layer 3) is not precluded, and BUILD NOTHING for it,
    because no language on his list needs it.

C5  RULESET IDENTITY.                          tier E1.   half-present, section 3.3
    variant_name exists and is untested. Exercise it, or replace it with an explicit
    ruleset field, and give display_label its first test.
    UNLOCKS: es (international vs NA vs LatAm distributions) · future nl (the removed IJ tile).
```

### 4.2 Language batches

```text
B1  HUNGARIAN + the first multigraph proof.                        needs C1
    build_hungarian_lexicon.py committed, output GITIGNORED and generated locally at setup
    (decision D, section 5). hungarian.json. messages.hu.ts. An `unavailable` variant made
    UNSELECTABLE at the three server sites. Inherits 12/00 conditions 11, 12, 15, 16, 17, 18.
B2  ORDINARY LATIN, no new capability.                             needs nothing beyond today
    it · nl · af · ms  — single-code-point tile sets, no folding, no multigraph.
    ⚠ AFRIKAANS AND MALAY ARE THE CHEAPEST LANGUAGES ON THE WHOLE LIST. Start here if you
      want to prove the "adding a language is boring" claim before the expensive work.
B3  DIACRITIC-FOLDING LATIN.                                       needs C3
    fr · de · da · sv · no · fi · is
B4  MULTIGRAPH LATIN.                                              needs C1 (+ C4 for es)
    hr (DŽ LJ NJ) · sl · es (CH LL RR, plus C5 for its distribution variants)
B5  TURKISH.                                                       needs C2 + C3
    the I/İ pair is the sharpest normalization case on the list and deserves its own batch.
B6  NON-LATIN LTR.                                                 needs nothing new if C1 landed
    el (104 tiles) · bg · ru (104 tiles)
    ⚠ HIS OWN OBSERVATION, AND I AGREE: once [A-Z] and len==1 are gone, Greek and Cyrillic
      are EASIER than Hungarian. Do not treat them as the hard part.
B7  pt — 120 tiles, THREE blanks.                                  needs nothing new
    the strongest test that bag size and blank count are truly data-derived.
```

⚠ **Do not run the batches in list order.** Run **B2 first** if you want the cheapest
possible proof that the foundation works, then C1 → B1, then C3 → B3, then C2 → B5,
then C1's dividend → B4 and B6, then B7. The only hard ordering constraint is that a
batch never precedes its capability.

### 4.3 The ledger he requires — build it in your first exchange

His clause: *"The Worker should maintain a running implementation ledger … and use that
ledger to systematically drive the multilingual expansion forward rather than waiting for
the COOPERATOR to name each next language."*

⛔ **Ownership correction, and it is a protocol point.** He wrote "the Worker". A Worker's
authority dies at its terminal report (RF-03, `AP.md:111-117`), so a Worker cannot own a
running artifact that spans the campaign. **You own the ledger.** A Worker fills its own
row and reports; you write it. Put it at:

```text
13/00-multilingual-expansion-campaign/90_language_ledger.md
```

One row per candidate, with exactly the nine columns he named:

```text
language / variant · gameplay status · UI-localization status · dictionary status ·
distribution source · special-rule requirements · architectural capability required ·
tests · blockers
```

Seed it in your first exchange with all twenty-four entries and the four shipped rows
filled from measurement. ⚠ **The `distribution source` column is the one that will block
you**, not the code: a tile distribution must be SOURCED, and `PROJECT_CONTEXT.md:1270-1273`
records the standard — JÚĽŠ SAV for sk, Ústav pro jazyk český for cs, Rada Języka Polskiego
for pl, MTA for hu. Never copy a distribution from a neighbour language because it looks
similar; Czech and Slovak are linguistically close and share **nothing** here.

---

## 5. The two hard facts you inherit, and neither is negotiable

### 5.1 The Hungarian lexicon does not fit — and the decision is already taken

Full measurement: `12/00/90_hungarian-expansion-probe.md`, fourteen sections,
**non-independent** (I measured it myself after a dispatch failure).

```text
THE EXPANDER WORKS.  Spylls 0.1.7 resolves the 1 559-entry AF alias table that defeats the
                     C unmunch. Six-word gate 6/6. Twenty-three-word gate 23/23.
                     hunspell 1.7.3 accepted 3 000 of 3 000 sampled forms.
THE ASSET DOES NOT FIT.  ~4.27 BILLION non-compound forms (~77 GB); ~301 MILLION (~4.5 GB)
                     even at a 15-code-point ceiling. Compare czech.txt at 3 930 497 words /
                     54 105 021 B, which already drew a GitHub large-file warning.
```

**DECISION D, taken under the autonomy grant and CONFIRMED by the Cooperator on
2026-09-03 (`suhlas, podme dalej`):** commit `build_hungarian_lexicon.py` plus its pinned
source hashes; generate the bounded lexicon **locally at setup**; gitignore the output;
let fail-closed readiness report `unavailable` until the local build has run.

⛔ **Four options were measured. Three are rejected. Do not re-propose them:**
committing the full list (~4.5 GB, LFS forbidden); a runtime spell-checker per lookup
(kills the prefix probe, and the engine authors **every** move in this product, so it
would disable Hungarian AI rather than degrade it); a frequency-bounded subset (no
licence-clean frequency source exists, and it makes the lexicon a judgement call).

Four costs, all of which B1 must handle:

```text
1  a fresh clone has NO Hungarian lexicon until the script runs → readiness `unavailable`,
   and it MUST NOT crash. Both halves proved by test.
2  the build needs network and minutes. OPT-IN, never on the critical path of local boot —
   AGENTS.md promises AI-only boot needs two terminals.
3  it introduces the first gitignored asset under backend/assets/dicts/. The .gitignore
   entry and the fail-closed readiness path are tested TOGETHER.
4  the code-point ceiling is DERIVED from the 15-tile board bound and the Hungarian tile
   set, declared in the manifest, and justified in writing. 15 code points is too tight
   once DZS is a tile.
```

⚠ **This decision generalizes, and that is the point for a campaign.** Any language whose
expansion exceeds a committable size takes the same route. Finnish is the one to watch —
agglutinative, and nobody has measured it. Put a `distribution source` and an expected-size
estimate in its ledger row before scheduling it.

⛔ **And it changes the audit design.** The current duplicate check holds a set of 3.9 M
tokens at ~500 MB peak RSS. At ~301 M forms that would need roughly **40 GB**. B1's audit
must be streaming or sorted-adjacency, never an in-memory set. That is inherited condition 18.

### 5.2 The F2b freeze — seven guards, and they come out together

Untouched by `12/00`. `12/00/00_handout.md` section 8 remains your source. The list:

```text
1  backend/game/services.py    _WIRE_ADAPTER_REMOVAL, a named constant
2  backend/game/services.py    _legacy_wire_board_and_blanks() — RAISES, never truncates
3  backend/game/serializers.py _nfc_uppercase_letter() enforces len(nfc) == 1
4  backend/game/serializers.py PlacementSerializer.validate_letter / validate_blank_as
5  frontend/src/app/api/ai/move/route.ts  Zod .length(1)   (two places)
6  frontend/src/app/api/ai/move/route.ts  blankAs.length === 1
7  frontend/src/app/api/ai/move/route.ts  letter.length === 1
```

Czech and Polish are single-code-point, so the adapter carries them losslessly — that is
exactly why they shipped ahead of C1. **Hungarian is the first language on the list with
digraph tiles**, and Croatian, Slovenian and Spanish follow it.

Two inherited conditions C1 may not weaken: the fixture passes with **at least two
different** multi-character tokens, not only `SZ`; and the **L·L synthetic canary** still
passes, proving the implementation did not generalize only to
`len(token) <= 2 && isalpha()`.

## 6. Three deferred items, coupled, and the first one is your cheapest re-entry

```text
V9a  libretiles_PRD.md references SOWPODS five times — :35 :65 :66 :127 :150 — and is stale
     in three measured ways: it names SOWPODS as the Tier-1 dictionary (the product ships
     collins2019.txt), it claims 172 823 words, and that count matches NEITHER the shipped
     Collins list (279 496) NOR the committed sowpods.txt (172 872, off by 49).
     ⇒ FIVE LINES. It is the ONLY thing blocking V3d, and it was owed anyway.
V9b  🐞 mle-01-F02, severity low, confirmed, established-static.
     backend/config/settings.py:375
        PRIMARY_DICTIONARY_PATH = DICTS_DIR / os.getenv("PRIMARY_DICTIONARY_FILE", "collins2019.txt")
     an UNDOCUMENTED env knob — verified absent from backend/.env.example — that repoints the
     English Tier-1 dictionary at any *.txt under assets/dicts/, bypassing the manifest and
     the entire provenance machinery. It is a reference surface NO source grep can settle.
     ⇒ Document it or remove it, deliberately. My recommendation, and the Cooperator did not
       override it: DOCUMENT it, because tests already depend on it.
V3d  then `git rm backend/assets/dicts/sowpods.txt` (1 743 531 B, 172 872 words, claimed by
     no manifest, no provenance, audited by nothing) with a test asserting its absence.
     ⛔ "Prove it is unreferenced" needs a THIRD clause beyond grep and manifests: enumerate
       every env-var-resolved asset path and state whether the deployed value was confirmed
       or accepted as unknown. Write that clause into the prompt.
```

⚠ The blob stays in Git history at `bd2d63f`, so a revert restores it byte-for-byte. That
is why the deletion is E2, not E4.

---

## 7. ⛔ Six prompt defects in nine exchanges — every one was the Orchestrator's

This is the highest-value transfer from `12/00`. Full detail in its `00_notes.md`
sections 11.2, 12.2 and 13.3. Five of six were caught by a Worker, not by me.

```text
D1  `-m manage.py check` — a gate command that cannot run, copied from a handout unrun.
D2  an UNMEASURED claim from a Worker's field-17 LEAD, acted on as if measured.
D3  "remain exactly as it is" versus "correct the stale comments" — about one docstring.
D4  "mirror `_read_words` EXACTLY" plus "apply len >= 2" in one paragraph. `_read_words` has
    no length floor. Obeying literally would have shipped a hole.
D5  a network allowlist omitting sk_SK while mandating the control that fetches it.
D6  ⛔ A CASE-SENSITIVE NEGATIVE GREP, RECORDED AS PROOF, IN A PROMPT THAT AUTHORIZED
    `git rm`. `git grep -n "sowpods"` → 0. `git grep -in "sowpods"` → 5, all uppercase, in a
    tracked root-level file. The Worker widened the pattern because my own prompt told it to,
    and returned BLOCKED with zero mutation. The asset survived.
```

The archive's lessons 10 and 16 name D6, D3 and D4 **by name**. They existed and did not
survive contact with drafting. So they are now mechanical. **Adopt all six:**

```text
R-A  A "do not change X" instruction must name WHY. If the reason is "its assertions are
     still correct", say that — so a Worker can see a DOCSTRING is not an assertion.
R-B  Prohibitions get written LAST, after the obligations, then read against them in ONE
     pass. Not in a separate drafting session where the two never meet.
R-C  When a prompt tells a Worker to correct stale comments, ENUMERATE them from your own
     grep. Do not delegate a search you already ran.
R-D  `exactly`, `identical` and `mirror` are grep targets in your OWN draft. Check each
     against the sentence that follows it. "Mirror X exactly" plus an added condition is
     TWO obligations, not one.
R-E  AN ABSENCE CLAIM IS NOT A FINDING UNTIL IT NAMES ITS PATTERN, AND THAT PATTERN IS
     CASE-INSENSITIVE. Run `git grep -in` AND `git grep -n`, report both counts, before
     writing any "there are no references" sentence.
R-F  NEVER AUTHORIZE A DELETION IN THE SAME EXCHANGE THAT ESTABLISHES THE ASSET IS
     UNREFERENCED. A prompt carrying both invites the Worker to treat your premise as proof.
```

Two habits that paid for themselves every single time:

```text
python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>   exit 0, EVERY prompt
⛔ NEVER build a prompt by string-patching the previous one. Regenerate the whole
   coordinate-bearing region, then let the tool check it.
```

⚠ **And keep the report field that made all six recoverable.** Every prompt ended with
*"WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE, labelled MEASURED or LEAD."*
It produced two production changes, one split slice, and five of six catches. **Keep the
labels strict** — D2 happened precisely because a LEAD arrived unlabelled.

## 8. Standing conditions for every batch

Nine, and 1 through 3 are the ones a campaign will be tempted to skip.

```text
1  en · sk · cs · pl behaviour byte-unchanged: the public variant payload keeps exactly its
   four keys {slug, display_name, language_code, readiness}, all four stay `playable`, no
   seeded bag changes, and the MOVE CORE SHA-256
   c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60 plus version
   pfr-s2-core-1 are PROVED unchanged.
2  the generic harness passes for EVERY new variant, and its G14 probe table FAILS a variant
   that has no probe words — that is the mechanism that keeps "boring" from becoming
   "unchecked".
3  the new lexicon is reproducible: a committed build script, pinned upstream commit, pinned
   per-file SHA-256, and `--check` agreeing byte-for-byte. ⛔ A SAME-LENGTH alteration is
   invisible to word counts, file sizes AND the audit — only the digest catches it. That was
   measured: `aachen` → `aachex` still reported words=3930497 duplicates=0 non_nfc=0.
4  provenance in the manifest, with `entry_count` equal to the real whole-file count.
5  an unusable or unclear licence is a DISQUALIFICATION and a recorded BLOCKER, never a
   footnote and never a Worker judgement. NO synthesis, generation, translation, or
   model-authored word list. Not one word from a language model.
6  all eight standing gates green, pytest summary quoted verbatim, ELEVEN dynamic routes and
   ZERO static routes.
7  a capability is implemented ONCE and expressed in variant DATA. ⛔ No language-slug
   branch. If you find yourself writing `if slug == "turkish"`, the capability is missing.
8  the ledger row is filled before the batch is called done.
9  E3 work — C1 is the only one — gets FRESH INDEPENDENT ACCEPTANCE from a session that did
   not implement it, and ⛔ that session CANNOT be your subagent.
```

## 9. Campaign closure conditions

```text
 1  every capability C1-C5 either landed with tests, or recorded as not-needed with the
    measurement that shows no target language requires it
 2  every one of the twenty-four target entries has a ledger row with all nine columns filled
 3  every language that CAN be implemented under standing condition 5 IS playable, with its
    UI locale where practical
 4  every language that CANNOT is a recorded blocker naming the exact missing thing —
    distribution source, licence, or architectural boundary
 5  the twelve conditions inherited from 12/00 are satisfied or explicitly re-dispositioned
 6  no language-slug branch exists anywhere in gamecore/ or game/
 7  all eight gates green at the closing commit
 8  the deferred acceptance batch delivered ONCE, at the end, per his autonomy grant
 9  fresh independent acceptance for C1
10  Meta complete: 99_closure.md, the ledger, PROJECT_CONTEXT.md and DEFECT_LEDGER.md
    updated through the closing commit
11  libretiles_PRD.md, README.md and AGENTS.md describe what actually ships
```

⚠ **Condition 4 is the honest one and you must not soften it.** A campaign that reaches
twenty of twenty-four with four well-evidenced blockers is a **success**. A campaign that
claims twenty-four by shipping a lexicon nobody can license, or a distribution nobody
sourced, is a failure that looks like a success — and the Cooperator is presenting this at a
job interview.

## 10. Delivery, and one operational reality

```text
ordinary batch slice   subagent Worker, delivered by giving it the Meta path and instructing
                       it to read that file IN FULL as its complete authority, with an
                       explicit statement that the path is DELIVERY ONLY and no other Meta
                       file may be read. Nine exchanges, zero confusion. Reuse the wording.
                       Record: Sub-agents/internal delegation: bounded authority
                       and NEVER call the result independent.
C1 planning            PLANNER WORKER, Native planning mode: required, COPY-PASTE. You stop
                       at the file. He delivers it, possibly to a different model.
C1 acceptance          FRESH INDEPENDENT ACCEPTANCE. ⛔ NOT your subagent.
B1's UI half           he proposed this as the first test of his `Worker Orchestrator` idea.
                       See /home/agile/meta/BRAINSTORMING.md section 1 — it must be a WORKER
                       SESSION PROFILE, not a fourth role, or it forks the protocol.
```

⚠ **Subagent dispatch failed twice in `12/00` for external reasons** — an account balance,
and a provider database error. One killed a Worker mid-task (→ an interruption companion,
session ordinal consumed); one killed delivery before the Worker received anything (→ safe
to re-deliver the same ordinal, because no authority was consumed and no outcome existed).
**Know the difference before you write either record.** Practical consequence: prefer fewer,
larger grants, and be ready to complete read-only evidence work yourself — recording the
non-independence permanently when you do.

## 11. Restoration readiness review

```text
contradiction review      PASS. Eight stale points in the supplied draft planner prompt are
                          named in section 3.4; seven in 12/00's opening handout are named in
                          12/00/91 section 3. Nothing is hidden.
omission review           PASS. Two artifacts owed by 12/00 are now written
                          (11/01/98_supersession.md, 11/02/98_supersession.md). One remains
                          owed and is named: 9N_deferred-acceptance-batch.md, which YOU start.
stale-state review        PARTIAL by design. Every number measured 2026-09-03 at ad4ce03; the
                          checkout is live and Michal commits to main himself. Re-measure.
authority review          PASS. This document grants nothing. Stated three times.
active-mutation review    PASS. Porcelain empty, public readback equal, no Worker.
security-boundary review  PASS. Stated in 12/00/91 sections 10 and 11.
strategic-direction
  review                  PASS. The objective is his own verbatim text (section 2) and the one
                          material decision inside it is confirmed (section 5.1).
next-step executability
  review                  PASS. Section 12 is executable immediately.

RESTORATION CLASSIFICATION: PASS
```

Reasoning recommendation for your first substantial Worker prompt: **Medium** for the
ledger seed and for V9a — five lines of documentation with a named target does not earn
High, and `AP.md:740-746` names over-routing as an anti-pattern. **High** for C1, C2, C3
and B1, each with the risk already named. **Extra High is not warranted anywhere** in this
campaign.

## 12. Your first three exchanges — do these in this order

```text
1  STAGE 1, read-only.  Run 12/00/91_orchestrator-handout.md section 2's gate list yourself,
   including the twenty-second `--check` run that re-proves the reproduction claim without
   touching the repository. Classify any difference with all five recovery classes.
2  SEED THE LEDGER.  90_language_ledger.md, twenty-four rows, nine columns, the four shipped
   rows filled from your own measurement. This is Orchestrator-direct work: read-only,
   Meta-only, no repository mutation. It is also where you will discover which languages are
   blocked on a sourced distribution rather than on code — and that is the campaign's real
   critical path.
3  V9a.  The five-line libretiles_PRD.md correction. Cheapest possible re-entry, unblocks
   V3d, and it is a documentation debt that predates this campaign.
```

Then: **B2 before C1.** Afrikaans and Malay are the cheapest languages on the list and they
prove the "adding a language is boring" claim on real data before you spend an E3 slice. If
B2 is *not* boring, that is the most valuable finding available and it is far cheaper to
learn there than inside C1.

## 13. The one-paragraph version

`12/00` built the machinery and stopped: a generic invariant harness over every installed
variant, readiness that fails closed on a broken lexicon, provenance in every manifest, a
committed reproducible build script per lexicon with byte-exact `--check`, and the expander
pinned. Four languages ship. The Cooperator then changed the objective from "add Hungarian"
to "add every practical mainstream Scrabble edition", which under RF-19 is a new logical
whole — this one. His own research names roughly ten architectural layers; **six already
exist in the code**, two exist as extension points that no manifest field selects yet, and
only three are genuinely absent — variant-declared blank targets, multi-realization tiles
(which no language on his list needs), and RTL (which his own scope clause excludes). So the
campaign is five small capabilities and seven language batches, and the critical path is not
the engine — it is **sourced tile distributions and licence-clean lexicons**, which is why
the ledger comes before the code. Start with Stage 1, seed the ledger, fix five lines of the
PRD, then prove the foundation on Afrikaans and Malay before spending the one E3 slice this
campaign contains.

**This document grants no mutation authority. Verify repository and public truth
independently before you act.**


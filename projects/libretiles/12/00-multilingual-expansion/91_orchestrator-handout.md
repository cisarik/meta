# Continuation handout — logical whole `12/00 multilingual-expansion`

Artifact class: **continuation handout. Evidence, not authority.** It grants **no**
repository, implementation, Git, deployment, production, account, filesystem, or
external-service mutation authority. Task authority comes only from your own
prompts; material product decisions come only from the Cooperator.

Written 2026-09-03 by the Orchestrator that executed exchanges 01/01 through
04/03 of this whole, at a coherent boundary: every prompt/report pair archived,
porcelain empty, public readback equal, no Worker in flight.

⛔ **Precedence.** This is the **second** handout for this whole. `00_handout.md`
is the opening one and remains valuable for its protocol mechanics, its
locked-fork inventory and its house-style guidance. **Where the two disagree,
this file is later and wins, and every disagreement is named explicitly in
section 3.** Do not treat either as authority.

⛔ **This is a CONTINUATION, not a restart.** The objective was bounded once
(section 4) and re-deriving it would be RF-19's changed-objective case
(`AP.md:255-262`), which starts a **new logical whole** instead. If you believe
the objective should change, that is a Cooperator decision, not a rewrite.

---

## Handoff capsule

```text
project            Libre Tiles — Next.js 16.3.4 + Django 5.2.17 Scrabble-like web app
repository         https://github.com/cisarik/libretiles
working copy       /home/agile/Projects/libretiles
main               ad4ce038e1bd3511bdd5b7431eb9c163d4788130
public readback    git ls-remote origin refs/heads/main == ad4ce03   verified 2026-09-03
porcelain          EMPTY
AP pin             .ap gitlink 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656, submodule HEAD equal
active Worker      none
active mutation    none
Meta repo          /home/agile/meta, main == 742b5eb5d96fe73d7a35cbac63899389c7da0221, pushed
next Worker session ordinal   05

shipped now        UI in 4 locales: en sk cs pl — 300 keys each, 1 200 strings, 20 parameterized
                   gameplay in 4 variants: english slovak czech polish, all readiness=playable
                   atomic tile tokens in the pure engine and in persistence
NEW THIS ERA       a generic per-variant invariant harness over every installed variant
                   readiness that FAILS CLOSED on a broken lexicon, still two values
                   provenance in every manifest, and a committed build script per lexicon
                   `--check` that re-verifies a committed asset without writing to it
                   the host expander pinned to hunspell 1.7.3, failing closed
blocked now        Hungarian gameplay — the lexicon is ~301 million forms minimum, see section 5
                   multi-code-point tiles end-to-end — the F2b freeze is untouched, section 6
```

## Commits this era, all Orchestrator-verified

```text
3878847  V1   generic per-variant invariant harness                1 file,  +428
61720aa  V1b  manifest stem/slug agreement + derived-key guard     1 file,  +114 −1
5f63e0d  V2a  slug_stem_mismatch rejected at ingest                3 files, +120 −20
1f39ff4  --   ORCHESTRATOR-AUTHORED: G26a docstring correction     1 file,  +4 −3
21f0a14  V2b  readiness fails closed on an invalid lexicon         7 files, +953 −24
a3ed00f  V3   build scripts for cs/pl + manifest provenance        9 files, +1112 −11
ad4ce03  V3c  --check, expander pin, AGENTS.md build route         5 files, +555 −18
```

⛔ **`1f39ff4` is ORCHESTRATOR-AUTHORED and its evidence is NON-INDEPENDENT** —
only the mechanical gates corroborate it. It joins era 10's `f40d8a0`, `8ef5992`
and `f983c3d` on that list. Do not read it as equally verified to a Worker slice.
The same caveat applies to `90_hungarian-expansion-probe.md`, which I measured
myself after a dispatch failure.

## Gate baseline at `ad4ce03` — re-measure, do not trust

```text
mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
ruff check .                                 All checks passed!
manage.py check                              System check identified no issues (0 silenced).
pytest                                       538 passed, 4 skipped in 238.52s
pytest --collect-only                        542 tests collected
manage.py validate_lexicons                  5 asset(s) audited, 0 failed, exit 0
npm run typecheck                            exit 0
npx vitest run                               450 passed | 3 skipped (31 files | 1 skipped)
npm run lint                                 exit 0
npm run build                                exit 0, ELEVEN dynamic routes, ZERO static
```

⛔ **`manage.py check` takes NO `-m`.** `.venv/bin/python -m manage.py check` is a
hard `ModuleNotFoundError`. The opening handout's section 14 carries the broken
form; a Worker caught it and this is the corrected one. The full corrected route:

```bash
cd backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
cd ../frontend && npm run typecheck ; npx vitest run ; npm run lint ; npm run build
```

---

## 1. Required reading, in this order

```text
1  /home/agile/meta/AP_DESTILLED.md          the protocol operating manual, line-referenced
                                             against the PINNED .ap. Explanatory, not authority.
2  /home/agile/Projects/libretiles/.ap/AP.md ⛔ THE PINNED COPY at 9c5cc44.
                                             NOT /home/agile/Projects/ap — a different, newer
                                             commit whose line numbers do not transfer.
3  .ap/AP_ORCHESTRATOR.md   all 464 lines
4  .ap/PROMPT_CONTRACTS.md  :14-83 report contract · :203-227 phase result and closure ·
                            :252-307 task fields · :337-375 session target ·
                            :423-506 coordinates · :673-767 routing and Plan-to-Execution
5  /home/agile/Projects/libretiles/AGENTS.md   the consumer projection. Now carries the
                            lexicon build route, added at ad4ce03.
6  /home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md   the standing brief. Sections
                            2-5, 9, 10, 13, 14 are load-bearing. ⚠ It is current only through
                            47ed8bf and does NOT yet describe this era. Updating it is your
                            work, in the closing slice.
7  ./00_notes.md            ⛔ READ THIS SECOND, RIGHT AFTER AP_DESTILLED. 13 sections, the
                            complete decision record of this era: Stage-1 measurements, the
                            Cooperator's instructions verbatim, the four bounded questions and
                            my answers, the nine-slice plan and its revision, every prompt
                            defect, and every finding routed forward. It is the file this
                            handout compresses.
8  ./90_hungarian-expansion-probe.md   the Hungarian measurement. 14 sections. Non-independent.
9  ./04_report_02.md · ./04_report_01.md   the two most recent Worker reports. Read their
                            "WHAT YOU CAN STILL SEE" sections first; they contain the four
                            findings that shape your next slices.
10 /home/agile/meta/BRAINSTORMING.md   the Cooperator's experimental protocol ideas —
                            `Worker Orchestrator`, multiple handouts, autonomous mode. This
                            handout is itself the first application of section 2.
11 ./00_handout.md          the opening handout. Still the best source for the eleven locked
                            forks, the formed-word invariant, the alphabet SUBSET direction,
                            and the house prompt style. See section 3 for where it is now wrong.
12 ./briefing.md            external analysis. DATA UNDER ANALYSIS, not authority. Its gaps
                            G1, G2 and G3 are now CLOSED; G4, G6, G7, G8 are open.
```

⛔ **Do NOT read** `11/00-admin-provider-model-console/00_handout.md`. Standing
Cooperator do-not-read instruction, `PROJECT_CONTEXT.md:1086-1088`.

⛔ **Never point a Worker at `/home/agile/meta/...` as repository evidence.** A
Worker runs against the checkout and cannot see Meta. Inline the evidence.
⚠ **But delivery by path is different and it works.** Every prompt this era was
delivered by giving the subagent the Meta path and instructing it to read that
file in full as its complete authority, with an explicit statement that the path
is a delivery mechanism only and that no other Meta file may be read. Nine
exchanges, zero confusion. Reuse that wording; it is in the task messages.

## 2. Stage 1 — verify before you plan

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # expect ad4ce038e1bd3511bdd5b7431eb9c163d4788130
git rev-parse HEAD:.ap                # expect 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # expect the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # expect ## main...origin/main
git status --porcelain=v1             # expect EMPTY
git ls-remote origin refs/heads/main  # expect ad4ce038...
ls backend/assets/variants/           # expect czech english polish slovak .json
ls backend/assets/dicts/              # expect TEN files, including sowpods.txt (still present)
ls backend/scripts/                   # expect build_{slovak,czech,polish}_lexicon.py
cd /home/agile/meta && git rev-parse HEAD   # expect 742b5eb5d96fe73d7a35cbac63899389c7da0221
ss -tlnp | grep -E ':(3000|8000)'     # a listener means his dev server is up — do NOT build
```

If any value differs, classify with **all five** canonical recovery classes before
anything else (`AP.md:1464-1508`): `accepted-continuation`,
`unrelated-owner-work`, `stale-clone`, `unpublished-candidate`,
`unexplained-divergence`; precedence `unexplained-divergence >
unrelated-owner-work > stale-clone > accepted-continuation >
unpublished-candidate`; any unclassified material remainder becomes
`unexplained-divergence`, fail closed, stop and report. Michal has committed to
`main` himself before (`61c9f09`), so `unrelated-owner-work` is live.

⛔ **`.ap` gitlink equality is a gate, not a formality.** A pinned submodule at
detached HEAD equal to the containing gitlink is the CORRECT topology. Never
attach or update `.ap`.

One extra verification this era earned, and it takes twenty seconds:

```bash
cd backend
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python scripts/build_slovak_lexicon.py \
    --check --check-dir /tmp/opencode/<your-slug>/sk
# expect: both digests IDENTICAL, "CHECK all artifacts identical", exit 0
```

That single command re-proves the central claim of this era — that a committed
lexicon is reproducible from a pinned upstream — without touching the repository.

---

## 3. Where `00_handout.md` is now wrong, named explicitly

Its evidence was accurate at `47ed8bf`. Seven commits later, these lines are
stale, and a handout that silently contradicted its predecessor would create two
semantic owners (`AP.md:18-62`).

```text
S1  ITS SECTION 14 GATE COMMAND IS BROKEN.  `.venv/bin/python -m manage.py check`
    cannot run. Use the corrected route in the capsule above.
S2  ITS GAPS G1, G2 AND G3 ARE CLOSED.
        G1 generic per-variant harness   -> 3878847, backend/tests/test_variant_invariants.py
        G2 readiness is file-existence   -> 21f0a14, backend/gamecore/lexicon_health.py
        G3 no provenance in the manifest -> a3ed00f, lexicon_provenance in all four manifests
    Its G4 (WordAuthority dormant), G6 (third readiness state — DECIDED: no), G7 (font glyph
    coverage) and G8 (multi-character tile visuals) remain OPEN.
S3  ITS CATALOG KEY COUNT IS IMPRECISE. It says "300 text keys + 20 fn keys". MEASURED by
    parsing the four messages.*.ts object literals: 280 text + 20 fn = 300 keys per catalog,
    1 200 strings across four locales. Its totals are right; its phrasing is not.
S4  ITS DICTS INVENTORY IS SHORT ONE FILE. There are THREE .LICENSE files, not two:
    czech.LICENSE 72 790 B · polish.LICENSE 30 427 B · slovak.LICENSE 67 811 B.
S5  ITS "ZERO REFERENCES TO SOWPODS" CLAIM IS FALSE, and so was mine. See section 7.
S6  ITS OPEN-WHOLES TABLE IS SUPERSEDED. 11/01 and 11/02 are superseded BY THIS WHOLE per
    my answer to its question 1. ⚠ The two supersession records it requires are STILL OWED —
    see section 9.
S7  ITS QUESTION SET IS ANSWERED. All four are decided and recorded in 00_notes.md section 3:
    Q1 = A (supersede) · Q2 = O1 then O3 then O2 plus Hungarian UI · Q3 = independent in
    architecture, coupled only in product sequencing · Q4 = NO third readiness state.
    ⛔ Do not re-ask them. They were answered under an explicit Cooperator autonomy grant.
```

## 4. The bounded objective, and what remains

> **Make Hungarian the fifth playable variant and the fifth interface locale of
> Libre Tiles, on machinery that makes the next language boring: every shipped
> lexicon reproducible from a pinned upstream by a committed script, every
> malformed language asset failing closed, and a multi-code-point tile carried
> losslessly from the engine to the board a player looks at.**

The second and third clauses are **done**. The first is blocked on an external
fact (section 5) and on a wire-format change (section 6).

```text
DONE      V1  V1b  V2a  V2b  V3  V3c
REMAINING, in dependency order
  V4'  build_hungarian_lexicon.py, committed; its OUTPUT is gitignored, not committed.
       Also the right moment for backend/scripts/_lexicon_build.py — the three existing
       scripts already share ~90 duplicated lines and V4' would be the fourth copy.
       ⛔ Its audit MUST be streaming or sorted-adjacency, never an in-memory set: the
       current audit holds a set of 3.9 M tokens at ~500 MB, and Hungarian is ~301 M forms,
       which would need roughly 40 GB.
  V6   wire schema 4 end to end — the seven-guard F2b freeze comes out TOGETHER with
       state_schema_version 4, BoardCell[][] on the wire, localStorage v4, the board/rack/
       blank/draw rendering, evaluate_scoring_move re-pointed at WordAuthority, and
       _word_passes_dictionary deleted. Tier E3.
       ⛔ PLANNER WORKER FIRST, manual delivery, then a fresh implementation session, then
       FRESH INDEPENDENT ACCEPTANCE THAT CANNOT BE YOUR SUBAGENT (AP.md:1395-1405).
  V7   the AI boundary lossless for multi-code-point cells; MOVE CORE hash and version
       PROVED unchanged.
  V5b  hungarian.json + the .gitignore entry + the fail-closed readiness path proved by test.
       ⛔ ALSO: an `unavailable` variant must become UNSELECTABLE at game/serializers.py:180,
       :215 and game/services.py:173, proved against a REAL unavailable variant. Hungarian
       under the local-build model is the first such variant in this project's history, so
       this is the slice where it is testable rather than synthetic.
  V8   Hungarian interface locale — messages.hu.ts (300 keys), LOCALES += "hu", a sourced
       pluralHu, a GLOSSARY.md Hungarian section, hu.png referenced. Depends on V5b.
       ⚠ The Cooperator proposed this as the first test of his `Worker Orchestrator` idea.
  V9   documentation and closure: libretiles_PRD.md, README.md, AGENTS.md, then
       PROJECT_CONTEXT.md, DEFECT_LEDGER.md and 99_closure.md written by you.
  V9a  ⛔ SEQUENCE THIS EARLY, not last. The libretiles_PRD.md correction is the ONLY thing
       blocking the sowpods deletion, and it is a documentation fix that was owed anyway.
       See section 7.
```

⚠ **If the Hungarian route is abandoned by Cooperator decision, V6 and V7 still
stand** — but their product justification weakens from "Hungarian ships" to "any
future multigraph language", and that is a Cooperator re-decision, not yours.

## 5. Hungarian — the measured blocker, and the decision taken

Full evidence: `90_hungarian-expansion-probe.md`. The three-line version:

```text
THE EXPANDER WORKS.  Spylls 0.1.7 resolves the 1 559-entry AF alias table that defeats the C
                     unmunch, and follows suffix continuations. Six-word gate 6/6.
                     Twenty-three-word gate 23/23. hunspell 1.7.3 accepted 3 000 of 3 000
                     sampled emitted forms.
THE ASSET DOES NOT FIT.  ~4.27 BILLION non-compound forms (~77 GB). At a 15-code-point
                     ceiling — the tightest defensible board bound — still ~301 MILLION
                     (~4.5 GB). Compare czech.txt at 3 930 497 words / 54 105 021 B, which
                     already drew a GitHub large-file warning.
SO THE GATE OVERSHOT.  DEFECT_LEDGER.md:1447 required "plausibly in the MILLIONS". The answer
                     is BILLIONS, and that overshoot is the blocker.
```

🐞 `mle-01-B01`, severity high, status `confirmed`, evidence class
`reproduced-dynamic`.

**Decision D, taken by me under the Cooperator's autonomy grant and then
explicitly confirmed by him on 2026-09-03 (`suhlas, podme dalej`):** commit
`build_hungarian_lexicon.py` plus the two pinned source hashes; the script
materializes a bounded lexicon into `backend/assets/dicts/hungarian.txt` at setup
time; that output is gitignored; gap G2's fail-closed readiness reports
`unavailable` until the local build has run.

Why this is his method rather than a deviation from it: his instruction was that
the dictionaries be **downloaded by a script**. For Slovak, Czech and Polish the
output happened to be small enough to commit as well. For Hungarian it is not.

Four costs, all of which must be handled in V4' and V5b:

```text
1  a fresh clone has NO Hungarian lexicon until the script runs, so Hungarian reports
   readiness `unavailable` and MUST NOT crash. Both halves proved by test.
2  the build needs the network and takes minutes. It must be OPT-IN and never on the critical
   path of local boot — AGENTS.md promises AI-only boot needs two terminals.
3  it introduces the first gitignored asset under backend/assets/dicts/. The .gitignore entry
   and the fail-closed readiness path must be tested together.
4  the code-point ceiling must be DERIVED from the 15-tile board bound and the Hungarian tile
   set, declared in the manifest, and justified in writing. A 15-code-point ceiling is too
   tight once DZS is a tile.
```

Three options were measured and rejected, so nobody re-proposes them:
committing the full list (~4.5 GB, LFS forbidden); a runtime spell-checker per
lookup (kills the prefix probe, and the engine authors **every** move in this
product, so it would disable Hungarian AI rather than degrade it); a
frequency-bounded subset (no licence-clean frequency source exists, and it makes
the lexicon a judgement call).

⚠ The probe's own honest limit: 100 % oracle agreement proves the traversal does
not **over**-generate. It says nothing about under-generation. The completeness
claim rests on 29 hand-checked forms, not on the oracle.

---

## 6. The F2b freeze is UNTOUCHED — all seven guards still stand

This era did not go near it. `00_handout.md` section 8 remains fully accurate and
is your source. The summary you need before writing V6:

```text
1  backend/game/services.py  _WIRE_ADAPTER_REMOVAL, a named constant
2  backend/game/services.py  _legacy_wire_board_and_blanks() — RAISES rather than truncating
3  backend/game/serializers.py  _nfc_uppercase_letter() enforces len(nfc) == 1
4  backend/game/serializers.py  PlacementSerializer.validate_letter / validate_blank_as
5  frontend/src/app/api/ai/move/route.ts  Zod .length(1)  (two places)
6  frontend/src/app/api/ai/move/route.ts  blankAs.length === 1
7  frontend/src/app/api/ai/move/route.ts  letter.length === 1
```

⛔ **They come out TOGETHER, in one slice that also delivers
`state_schema_version` 4.** `DEFECT_LEDGER.md:806-826` records the stated reason:
*"if the backend emitted v4 while the frontend still read v3, the product would be
broken between two slices. The Cooperator opens this application, and a fresh
clone that crashes is a first-class defect in his frame."*

Czech and Polish are single-code-point languages, so the adapter carries them
losslessly. **Hungarian is the only V4 language with digraph tiles**, which is why
V6 and V7 remain required for Hungarian alone.

Two conditions inherited verbatim from `11/01/00_handout.md` §11 that V6 must not
weaken: the Hungarian acceptance fixture passes with **at least two different**
multi-character tokens, not only `SZ`; and the L·L synthetic canary still passes,
proving the implementation did not generalize only to
`len(token) <= 2 && isalpha()`.

## 7. The deferred chain — PRD, sowpods, and an undocumented env knob

Three coupled items, discovered in exchange 04/02, all small and all real.

```text
BLOCKER  libretiles_PRD.md references SOWPODS five times — :35 :65 :66 :127 :150 — and
         `backend/assets/dicts/sowpods.txt` (1 743 531 B, 172 872 words) is claimed by NO
         manifest, has no provenance, and is audited by nothing. The deletion is desirable
         and was authorized; it was BLOCKED because the PRD still describes the file.
STALE    the PRD is wrong in three ways at once, all measured: it names SOWPODS as the
         Tier-1 dictionary (the product ships collins2019.txt), it claims 172 823 words, and
         that count matches NEITHER the shipped Collins list (279 496) NOR the committed
         sowpods.txt (172 872, off by 49).
DEFECT   🐞 mle-01-F02, severity low, status `confirmed`, evidence class established-static.
         backend/config/settings.py:375
             PRIMARY_DICTIONARY_PATH = DICTS_DIR / os.getenv("PRIMARY_DICTIONARY_FILE", "collins2019.txt")
         is an UNDOCUMENTED env knob — verified absent from backend/.env.example — that can
         repoint the English Tier-1 dictionary at any *.txt under assets/dicts/, bypassing
         the manifest and the entire provenance machinery this era built. It is also a
         reference surface NO source grep can settle, which is why nobody could exclude an
         operator .env naming sowpods.txt.
```

**Recommended sequence, and it is three small exchanges:**

```text
V9a  correct the five PRD lines to Collins 2019. One edit, no code, unblocks everything.
V9b  document or remove PRIMARY_DICTIONARY_FILE, deliberately.
V3d  then `git rm backend/assets/dicts/sowpods.txt` with a test asserting its absence.
```

⛔ **"Prove it is unreferenced" needs a THIRD clause** beyond grep and manifests:
enumerate every env-var-resolved asset path and state whether the deployed value
was confirmed or accepted as unknown. Without it, any future asset deletion
carries the same undetectable start-up risk. Write that clause into V3d.

⚠ The blob remains in Git history at `bd2d63f`, so `git revert` of a deletion
commit restores it byte-for-byte. That is why the deletion is E2, not E4.

## 8. ⛔ SIX PROMPT DEFECTS IN NINE EXCHANGES — read this before you write anything

This is the most valuable thing in this handout. **Every one was mine, not a
Worker's**, and five of six were caught by a Worker rather than by me.

```text
D1  `-m manage.py check` — a gate command that cannot run. Copied from the opening handout
    without ever running it.                                              (exchange 01/01)
D2  the `fetched_at` bare-year premise — I inherited an UNMEASURED claim from a Worker's
    field-17 lead and acted on it as if measured. Both of us were wrong; the real hole was
    ISO basic and week-date forms.                                        (exchange 01/02)
D3  "remain exactly as it is" versus "correct the stale comments" — two instructions about
    the same docstring that could not both hold.                          (exchange 03/01)
D4  "mirror `_read_words` EXACTLY" and "apply len >= 2" in one paragraph. `_read_words` has
    no length floor. Obeying literally would have shipped a hole.         (exchange 03/02)
D5  my network allowlist omitted sk_SK while I mandated the Slovak control that fetches it.
                                                                          (exchange 04/01)
D6  ⛔ A NEGATIVE GREP, RECORDED AS PROOF, IN A PROMPT THAT AUTHORIZED `git rm`.
    I ran `grep -rn "sowpods"` — case-sensitive, lowercase — got zero, and wrote "ZERO
    references anywhere in the repository". `git grep -in` returns FIVE, all uppercase, in a
    tracked root-level document. The Worker widened the pattern because my own prompt told
    it to, and returned BLOCKED with zero mutation.                       (exchange 04/02)
```

`PROJECT_CONTEXT.md` lesson 10 names D6 by name and lesson 16 names D3 and D4.
The lessons existed; they did not survive contact with drafting. So they are now
mechanical rules. **Adopt all six:**

```text
R-A  A "do not change X" instruction must name WHY. If the reason is "its assertions are
     still correct", say that — so a Worker can see that a DOCSTRING is not an assertion.
R-B  Prohibitions get written LAST, after the obligations, then read against them in ONE
     pass. Not in a separate drafting session where the two never meet.
R-C  When a prompt tells a Worker to correct stale comments, ENUMERATE them from your own
     grep. Do not delegate the search you already ran.
R-D  The words `exactly`, `identical` and `mirror` are grep targets in your own draft. Each
     one must be checked against the sentence that follows it. "Mirror X exactly" plus an
     added condition is TWO obligations, not one.
R-E  AN ABSENCE CLAIM IS NOT A FINDING UNTIL IT NAMES ITS PATTERN, AND THAT PATTERN IS
     CASE-INSENSITIVE. Run `git grep -in` and `git grep -n`, report both counts, before
     writing any "there are no references" sentence.
R-F  NEVER AUTHORIZE A DELETION IN THE SAME EXCHANGE THAT ESTABLISHES THE ASSET IS
     UNREFERENCED. A prompt carrying both invites the Worker to treat your premise as the
     proof.
```

And the two mechanical habits that paid for themselves every time:

```text
python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>    exit 0, EVERY prompt
⛔ NEVER build a prompt by string-patching the previous one. Regenerate the whole
   coordinate-bearing region, then let the tool check it.
```

⚠ **What made these recoverable:** every prompt this era ended with a report
section demanding *"WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE,
labelled MEASURED or LEAD."* That field produced two production changes, one split
slice, and five of the six defect catches. **Keep it, and keep the labels
strict** — D2 happened precisely because a LEAD arrived unlabelled and I treated
it as a measurement.

---

## 9. Closure conditions — eighteen, with current status

Section 7 of `00_notes.md` holds the drafted set; sections 10.5 and 12.5 amended
it. Consolidated:

```text
 1  generic per-variant invariant harness over EVERY installed variant     SATISFIED 3878847
 2  lexicon validation fails closed; readiness stays TWO values            SATISFIED 21f0a14
 3  provenance in the MANIFEST, not only in a Meta report                  SATISFIED a3ed00f
 4  every non-English lexicon reproducible by a COMMITTED script, proved
    against the committed asset                                    SATISFIED a3ed00f + ad4ce03
 5  a malformed manifest and a corrupt lexicon each fail, proved by a test
    that FAILS BEFORE the fix                                      SATISFIED 21f0a14 + a3ed00f
 6  a per-variant membership probe of real inflected forms                  SATISFIED 3878847
 7  en/sk/cs/pl unchanged: four-key payload, all four playable, no seeded
    bag change, MOVE CORE hash and version unchanged            HOLDING — RE-PROVE AT CLOSURE
 8  all seven F2b guards removed TOGETHER with wire schema 4, and
    _word_passes_dictionary deleted with evaluate_scoring_move re-pointed        OPEN — V6
 9  the Hungarian acceptance fixture passes with at least TWO different
    multi-character tokens, not only SZ                                          OPEN — V6
10  the L·L synthetic canary still passes                                        OPEN — V6
11  Hungarian playable AFTER a documented, opt-in local lexicon build, and
    BEFORE it the variant reports `unavailable` WITHOUT crashing — both
    halves proved by test. The committed artifact is the build script plus
    its pinned source hashes, never the lexicon.                          OPEN — V4' + V5b
12  if Hungarian is playable, the fifth interface locale ships with exact
    key-set and interpolation parity and a sourced plural function             OPEN — V8
13  all eight standing gates green at the closing commit, pytest summary
    quoted verbatim, ELEVEN dynamic and ZERO static routes                    OPEN — closure
14  FRESH INDEPENDENT ACCEPTANCE by a session that did not implement the
    wire-schema change; the deferred Cooperator acceptance batch delivered
    once at the end; Meta complete including 99_closure.md; PROJECT_CONTEXT
    and DEFECT_LEDGER updated; supersession records for 11/01 and 11/02      OPEN — closure
15  the Hungarian code-point ceiling DERIVED from the 15-tile board bound
    and the Hungarian tile set, declared in the manifest, justified         OPEN — V4'
16  the six-word gate asserted BY THE BUILD SCRIPT as a fail-closed
    post-condition                                                         OPEN — V4'
17  an `unavailable` variant is UNSELECTABLE at game/serializers.py:180,
    :215 and game/services.py:173, proved against a REAL unavailable
    variant rather than a synthetic one                                     OPEN — V5b
18  the Hungarian lexicon audit uses a streaming or sorted-adjacency
    duplicate check, never an in-memory set (~301 M forms would need ~40 GB) OPEN — V4'
```

⚠ **Two artifacts are STILL OWED and are not cancelled:** supersession records for
`11/01 multilingual-tile-token-foundation` and `11/02
czech-polish-hungarian-variant-activation`. RF-19 (`AP.md:255-262`) is why they
must be **written** rather than assumed: a materially changed objective begins a
new identity and does not silently absorb an old one. Carry `11/01`'s design
decisions **verbatim**, not paraphrased — specifically `11/01/00_handout.md`
§4.1-4.5 and `11/01/90_orchestrator-plan-acceptance.md`.

## 10. Delivery routes, and one operational reality

```text
ordinary implementation slice   subagent Worker, delivered by you.
                                Record in every prompt:
                                  Sub-agents/internal delegation: bounded authority
                                and NEVER call the result independent.
V6 planning                     PLANNER WORKER, Native planning mode: required, COPY-PASTE
                                delivery by the Cooperator. You stop at the file.
V6 acceptance                   FRESH INDEPENDENT ACCEPTANCE. ⛔ It CANNOT be your subagent
                                (RF-05 AP.md:129-136; AP.md:1395-1405). Copy-paste to a
                                session Michal opens.
V8                              WORKER ORCHESTRATOR, experimental, copy-paste. He wants to
                                paste these manually, possibly into a different LLM.
```

⚠ **Subagent dispatch failed twice this era for external reasons** — once on an
account balance (`需要预扣费额度: $0.300000` against `$0.285318` remaining) and once
on a provider `Database error`. Both were transport failures, not protocol
failures.

```text
the BALANCE failure killed a Worker MID-TASK. It had downloaded pinned sources and built a
    venv but produced no terminal report, so the lawful artifact was
    02_interruption_00.md — written by me from safely known facts, never impersonating the
    Worker, and mutually exclusive with any 02_report_00.md. Session ordinal 02 is CONSUMED.
the DATABASE failure killed delivery BEFORE the Worker received anything. I verified nothing
    had begun — porcelain empty, no /tmp state — and re-delivered the SAME exchange ordinal,
    because no authority was consumed and no outcome existed. That is the right distinction:
    an interruption record is for a task that BEGAN.
```

Practical consequence: **prefer fewer, larger Worker grants over many small
ones**, and be prepared to complete read-only evidence work yourself. That is
exactly the economic pressure behind the Cooperator's `Worker Orchestrator` idea,
and it is now measured rather than theoretical.

## 11. The Cooperator, and the parts that change how you work

`PROJECT_CONTEXT.md:303-356` is authoritative. What matters most here:

```text
language        to him Slovak, masculine forms; your self-reference feminine; Worker prompts
                and reports professional English; every terminal report begins exactly
                `### Report for ORCHESTRATOR_CHAT`
emoji           begin every message with the signal, and END every message with an explicit
                emoji-annotated block of what he must do. Label manual test steps B1-1, B1-2.
his stake       MATERIAL — a job interview. A fresh clone that crashes, a control that does
                nothing, or a number that does not mean what it claims is a first-class defect.
his replies     terse: A · Pokracuj · ano · suhlas. Confirm an ambiguous one-word instruction
                in ONE LINE before spending a session on it.
never           read or print backend/.env or frontend/.env.local; let a credential value,
                prefix, length or hash reach chat, a report or Meta; ask him for a destructive
                action; create permanent BOOT_*/NEXT_*/WORKERS.md/ORCHESTRATOR_HANDOFF.md.
```

⛔ **THE AUTONOMY GRANT, and it is the standing instruction of this era**
(2026-09-03, verbatim): *"NECHCEM ABY SOM TU BOL AKO COOPERATOR POUZIVANY NA
TESTOVANIE … CHCEM ABY SI PRACOVAL AUTONOMNE. OVEROVANIE … AZ NA KONCI VYVOJA.
PROSIM PRETO MA NEVYRUSUJ."* and *"AK MI BUDES CHCIET DAT OTAZKY PROSTE POUZI
ODPOVEDE KTORE DOPORUCUJES. ABSOLUTNE TI DOVERUJEM."*

Three things that grant does **not** change, and protecting them is your job:

```text
it does NOT lower an evidence tier. E3 still requires fresh independent acceptance, and that
    acceptance is a WORKER function, not a Cooperator function. Only his OBSERVATION was
    deferred.
it does NOT remove the rendered-output rule. `for anything that renders, render it, or do not
    claim it`. Deferring his observation makes YOUR loopback probe MORE necessary: production
    build, `next start` on a loopback port, HTTP client, stop by exact PID.
it does NOT touch decision 10 — he has no screen reader and will not install one. Accessibility
    claims are closed BY INSPECTION ONLY, permanently.
```

⚠ **The obligation that grant creates:** an acceptance batch not run when it is
generated must still be **written down** when it is generated, or it will be
reconstructed from memory at the end and be wrong. ⛔ **That file does not exist
yet and it is owed.** Start `9N_deferred-acceptance-batch.md` and append to it from
your first slice: slice, commit, and the exact observable expectation.

⚠ **His generation-hazard diagnosis, and it works:** write large artifacts by
**appending section by section** against a sentinel, never as one generation. He
traced the `message_start … while message … is still open` errors to whole-file
generation and they stopped when the previous Orchestrator appended. Every file in
this directory was written that way. Nine exchanges, zero occurrences.

## 12. What comes after this whole

```text
then   11/00 admin-provider-model-console — his stated SINGLE MOST IMPORTANT outcome: add
       providers and models and set the default from Django admin with NO SSH, plus AI-vs-AI
       diagnostics in every variant and strength testing before promotion.
       ⛔ Do not read that directory's handout. PROJECT_CONTEXT.md §12 carries his intent.
then   the deployment whole. ⛔ TWO ARTIFACTS ARE STILL OWED: an expert Orchestrator handout,
       and a read-only Research Worker prompt for ChatGPT Deep Research on Ubuntu Server
       24.04 VPS hardening. The complete deployment fact set — Docker-Compose-plus-host-nginx,
       the DJANGO_NUM_PROXIES=1 and $proxy_add_x_forwarded_for arithmetic with BOTH silent
       misconfigurations, audit-04-F01 and the trap inside its obvious remedy, the
       NEXT_PUBLIC_* build-time inlining trap, and the monitoring assessment — is written out
       in 10/00-ui-internationalization/00_handout.md section 10. COPY IT FROM THERE.
later  de-hardcoding the nine AI providers. LOCK 11 holds until then: no change to any
       provider list, constant, tier, model tuple, or provider documentation anywhere.
later  Tier 2 dictionary; the Slovak Settings/engine/prompt wiring slices.
```

⛔ **The do-not-deploy stands**, for one named reason: `audit-04-F01` /
`orch-05-D14` becomes reachable the moment Django sits behind nginx, because
`django-axes` still keys on `REMOTE_ADDR`, collapsing the `(username, ip_address)`
lockout key to one global bucket per account and turning an account lockout into a
targeted denial of service. **And the obvious remedy is itself a trap** — the
half-measure is worse than the current state. All 32 corrected security findings
ARE `verified-closed`.

## 13. Restoration readiness review

```text
contradiction review      PASS. Seven disagreements with the opening handout are named in
                          section 3 rather than hidden, including one where its own gate
                          command cannot run.
omission review           PARTIAL. Two artifacts are owed and named: the supersession records
                          for 11/01 and 11/02 (section 9), and the deferred acceptance batch
                          file (section 11). Neither is lost; both are unwritten.
stale-state review        PARTIAL by design. Every number here was measured on 2026-09-03 at
                          ad4ce03, but the checkout is live and Michal commits to main
                          himself. Section 2 exists so you re-measure.
authority review          PASS. This document grants nothing. Stated three times.
active-mutation review    PASS. Porcelain empty, public readback equal, no Worker.
active-Worker review      PASS. None. Sessions 01-04 all terminated; 02 consumed by an
                          interruption; next fresh session ordinal is 05.
security-boundary review  PASS. Secret, host, network, browser, filesystem, account and Git
                          boundaries are stated in sections 10 and 11.
strategic-direction
  review                  PASS. The objective was bounded once and the Cooperator confirmed
                          the one material decision inside it (`suhlas, podme dalej`). No
                          strategic question is open.
next-step executability
  review                  PASS. Section 2 is executable immediately and read-only. The next
                          slice is V9a — the five-line PRD correction — which is the cheapest
                          possible re-entry and unblocks two further items.

RESTORATION CLASSIFICATION: PARTIAL — complete enough to continue immediately; the two
owed artifacts in the omission review are the only gaps, and both are named work rather
than missing measurements.
```

Reasoning recommendation for your first substantial Worker prompt: **High** for V4'
and V6, with the named risks already stated — for V4' that a build script writing a
gitignored asset can silently produce a wrong word list that no gate sees, and for
V6 that a wire-format change plus a frontend rewrite touches a shipped, playable
product. **Medium** for V9a, and say so: a five-line documentation correction with
a named target does not earn High, and `AP.md:740-746` names over-routing as an
anti-pattern.

## 14. The one-paragraph version

Libre Tiles now ships four UI locales and four playable variants on machinery that
makes the next language boring: a generic invariant harness over every installed
variant, readiness that fails closed on a broken lexicon, provenance in every
manifest, a committed build script per lexicon, and a `--check` mode that
re-verifies a committed asset byte-for-byte without writing to it. What remains is
Hungarian, and Hungarian is blocked twice over: its lexicon is ~301 million forms
at the tightest board bound, so it must be generated locally at setup rather than
committed — a decision the Cooperator has confirmed — and its digraph tiles cannot
cross the wire until the seven-guard F2b freeze comes out together with wire schema
4. Three small documentation items are also deferred and coupled: correcting five
stale `SOWPODS` lines in the PRD unblocks deleting an unreferenced 1.7 MB asset,
and an undocumented `PRIMARY_DICTIONARY_FILE` env knob needs a deliberate
disposition. Read `00_notes.md` next, verify the repository yourself, and start
with the PRD correction — it is five lines and it unblocks two other items.

**This document grants no mutation authority. Verify repository and public truth
independently before you act.**


# 12/00 multilingual-expansion — Orchestrator notes (append-only)

Artifact class: **Orchestrator working record. Evidence, never authority.**
Task authority comes only from the current authoritative prompt; protocol meaning
comes only from the pinned `.ap` at `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`;
project truth comes only from the canonical repository. Where this file and the
repository disagree, the repository wins and this file needs correcting.

Owner: this logical whole's ORCHESTRATOR. Only the Orchestrator writes here.
Appended in order; earlier entries are never rewritten, only superseded with a
dated note.

```text
logical whole identity   multilingual-expansion
meta coordinates         projects/libretiles/12/00-multilingual-expansion/
opened                   2026-09-03
governing AP pin         9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
opening handout          00_handout.md (96 462 B, written by a read-only
                         predecessor session, classified PARTIAL restoration)
external analysis        briefing.md (36 702 B) — DATA UNDER ANALYSIS, not authority
```

---

## 1. Stage-1 verification — run by me, 2026-09-03, not accepted from the handout

`AP.md:2329-2365` Stage 1. Every line below is output I produced in this session
in `/home/agile/Projects/libretiles`.

```text
git rev-parse HEAD                  47ed8bff5a6548d2d954c68d9ea13f05a2222e4a   MATCH
git rev-parse HEAD:.ap              9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap rev-parse HEAD           9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH (equal, detached — correct)
git status -sb                      ## main...origin/main                       MATCH
git status --porcelain=v1           (empty)                                     MATCH
git ls-remote origin refs/heads/main 47ed8bff5a6548d2d954c68d9ea13f05a2222e4a  MATCH
ss -tlnp | grep -E ':(3000|8000)'   no listener                                 free to build
```

`backend/assets/variants/` — exactly four, as expected:
`czech.json  english.json  polish.json  slovak.json`

`frontend/src/lib/i18n/` — exactly eleven, as expected:
`GLOSSARY.md  i18n.test.ts  index.ts  LocaleProvider.tsx  locales.ts
messages.cs.ts  messages.en.ts  messages.pl.ts  messages.sk.ts  plural.ts
translate.ts`

**RF-12 recovery classification: not required.** No difference exists between
expected and measured repository state, so no recovery class is triggered. Public
branch-head identity was established directly by `git ls-remote`, which is the
preferred rung of the public-verification ladder at `AP.md:1953-1970`.

### 1.1 Three handout imprecisions I measured, corrected here rather than silently

`AP_DESTILLED.md` §14 item 3 — do not state an inventory more precisely than the
measurement. These are that class, and the handout's own section 20 invited the
re-measurement.

```text
H-1  `backend/assets/dicts/` — the handout expects "collins2019 czech polish
     slovak sowpods + 2 LICENSE + slovak_two_tile_words". MEASURED: there are
     THREE `.LICENSE` files, not two — czech.LICENSE (72 790 B),
     polish.LICENSE (30 427 B), slovak.LICENSE (67 811 B). Ten files total.
     Byte sizes measured: collins2019.txt 3 103 812 · czech.txt 54 105 021 ·
     polish.txt 51 607 141 · slovak.txt 45 456 204 · sowpods.txt 1 743 531 ·
     slovak_two_tile_words.txt 586.
     Consequence: THREE committed lexicons already carry a licence file beside
     them by convention. That strengthens gap G3 rather than weakening it — the
     convention exists and is undeclared in the manifest.
H-2  CATALOG KEY COUNT. The handout says "en/sk/cs/pl each 300 text keys + 20 fn
     keys", which would be 320 per catalog. MEASURED by parsing the four
     `messages.*.ts` object literals: **280 text keys + 20 fn keys = 300 keys per
     catalog, 1 200 strings across four locales.** The handout's totals (300 keys,
     1 200 strings, 20 parameterized) are right; its "300 TEXT keys" phrasing is
     not. `PROJECT_CONTEXT.md:176` records 294 per catalog at `74b5339`, before
     R7 (+5) and R11 (+1) — 294 + 5 + 1 = 300, so both numbers are real at their
     own commits and the arithmetic closes.
     Key-set parity re-derived from source: `sk`, `cs`, `pl` each have ZERO
     missing and ZERO extra text keys against `en`, and zero missing fn keys.
H-3  `backend/tests/test_dictionary_validation.py` EXISTS (98 lines). Its name
     invites the conclusion that gap G2 is already covered. It is NOT: every one
     of its ten tests is about the ENGLISH Collins index and
     `game.services._word_passes_dictionary` — `qlet`, `qi`, `za`, `fe`, prefix
     index agreement, and an anti-`isascii` guard. There is no per-variant
     dictionary ASSET validation in it. Any prompt touching G2 must say this
     explicitly, or a Worker will reasonably assume the file already owns the job.
```

### 1.2 Gaps G1, G2, G4, G6 — re-measured by me, all four confirmed

```text
G1  CONFIRMED. `grep -rn "list_installed_variants" backend/tests/` returns ZERO
    lines. Widened per lesson 10 rather than concluding from one negative pattern:
    the only per-variant loop in the whole suite is
    `test_endgame_policy_matrix.py:68  VARIANT_SLUGS = ("slovak", "english")` —
    a hardcoded two-tuple. Czech and Polish are covered only by the
    language-specific `test_czech_polish_variants.py`. A fifth manifest dropped
    into `backend/assets/variants/` is accepted by the serializer with no code
    change and asserted by nothing.
G2  CONFIRMED by reading the function, not by grep. `backend/game/views.py`
    `_variant_resources_ready` is exactly two conditions: `dictionary_path
    .is_file()`, and when a two-tile file is declared, `two_path.is_file()`.
    Nothing reads a byte of either file. A truncated, mojibake, BOM-prefixed,
    header-polluted or one-line lexicon reports readiness `playable`.
G4  CONFIRMED. `_word_passes_dictionary` is defined at `game/services.py:209` and
    called in production from `game/services.py:131`, `game/diagnostics.py:136`
    and `game/diagnostics.py:352`. `WordAuthority` is imported in exactly two
    non-test places — `gamecore/legality.py:23` and its own module — and the
    `authority=` keyword is passed from exactly ONE call site in the entire
    repository: `backend/tests/test_atomic_tile_tokens.py:356`. So `WordAuthority`
    is built, tested, and dormant in production, exactly as
    `DEFECT_LEDGER.md:1051` records it was deliberately deferred to F2c.
G6  CONFIRMED. `game/views.py:41-46` declares
    `readiness: Literal["playable", "unavailable"]`. Two values.
```

### 1.3 Variant invariants — measured against the real assets

Produced by parsing the four manifests directly. These are the numbers a generic
harness must reproduce, and the per-variant totals that must stay in per-variant
tests.

```text
slug     entries  nonblank_kinds  blanks  total_tiles  nominal_points  order_tokens  letters_without_tile
english     27          26          2         100           187            26              0
slovak      42          41          2         100           267            46              5
czech       40          39          2         100           205            42              3
polish      33          32          2         100           190            32              0

all four: alphabet_order duplicate-free, every token NFC, and ZERO tiles missing
from alphabet_order — the SUBSET invariant holds in the correct direction.
```

Manifest key sets, measured, and the asymmetry matters for gap G3:

```text
english.json  alphabet_order dictionary_file fetched_at language letters slug source
              -> NO language_code, NO source_url
slovak.json   + language_code source_url two_tile_words_file
czech.json    + language_code source_url
polish.json   + language_code source_url

NOT PRESENT IN ANY MANIFEST: upstream commit, expansion tool and version, entry
count, SPDX expression, licence-file pointer. `total_tiles` is correctly absent —
it is derived, and it must stay derived.
```

---

## 2. Cooperator instructions for this whole — 2026-09-03, verbatim, classified

`AP_ORCHESTRATOR.md:94-110` requires each item to be classified. Verbatim first,
classification second, so a future reader can re-derive my reading.

### 2.1 The dictionary route — a material product decision

> *"@libretiles/backend/scripts/build_slovak_lexicon.py bol pouzity na stahovanie
> slovnika, takto chcem aby boli stiahnute vsetky potrebne slovniky."*

**Classification: ACCEPTED DECISION, and it is the single most consequential thing
in this message.** It converts the handout's "O3 Hungarian lexicon" from an open
option into a named method, and it retroactively creates an obligation for Czech
and Polish that nobody had written down. Measured: `backend/scripts/` contains
**exactly one** file, `build_slovak_lexicon.py` (209 lines, 7 601 B). There is no
`build_czech_lexicon.py` and no `build_polish_lexicon.py` — the Czech and Polish
lexicons were produced by an ad-hoc `/tmp/opencode/cph-dicts/acquire.py` that a
Worker wrote and that was never committed (`11/02/01_report_00.md:165`). So today
**two of three committed non-English lexicons are not reproducible from anything
in the repository.** His instruction says they must be.

What the Slovak script establishes as the house pattern, read from source:

```text
PINNED_COMMIT              one upstream commit, hardcoded              :19
UPSTREAM_BASE              raw.githubusercontent.com/LibreOffice/…     :20-23
PINNED_FILES               (filename, expected SHA-256) tuples, and a
                           mismatch is SystemExit(1) — fail closed     :33-38, :93-98
_require_tri_license       asserts the licence sentence still says what
                           the attribution claims; fail closed         :103-114
_run_unmunch               host tool, exit code checked, empty stdout
                           is a failure                                :117-136
_filter_words              NFC -> strip -> casefold, isalpha, len>=2,
                           dedup, sort; bounds [80 000, 5 000 000]     :139-154
_write_lexicon             two provenance header comment lines         :40-44, :157-163
_write_license             attribution block + verbatim upstream text  :46-54, :166-170
docstring                  "Not imported by Django. Host tool:
                           /usr/bin/unmunch. No Poetry/npm dependency."  :4
```

⚠ Two facts I measured that bear directly on reproducing this for Hungarian:

```text
host tools present   /usr/bin/unmunch  /usr/bin/hunspell  /usr/bin/munch
                     /usr/bin/analyze  /usr/bin/wordforms
hunspell version     "@(#) International Ispell Version 3.2.06 (but really
                     Hunspell 1.7.3)"  — the SAME 1.7.3 the deep research names
                     as the required independent oracle. The oracle is already
                     installed.
spylls               ABSENT from backend/.venv (ModuleNotFoundError). The
                     expansion route needs a build-time dependency decision.
```

### 2.2 Autonomy, and the explicit opt-out of Cooperator testing

> *"NECHCEM ABY SOM TU BOL AKO COOPERATOR POUZIVANY NA TESTOVANIE … CHCEM ABY SI
> PRACOVAL AUTONOMNE. OVEROVANIE, ZE TEXTY SLOVNIKY FEATURES NOVE BUDU
> REALIZOVANE AZ NA KONCI VYVOJA. PROSIM PRETO MA NEVYRUSUJ."*

> *"AK MI BUDES CHCIET DAT OTAZKY PROSTE POUZI ODPOVEDE KTORE DOPORUCUJES.
> ABSOLUTNE TI DOVERUJEM."*

**Classification: ACCEPTED DECISION on sequencing, lawful under RF-01.** He owns
subjective acceptance and is choosing to exercise it once at the end. Recorded in
`/home/agile/meta/BRAINSTORMING.md` §3 with the three things it explicitly does
**not** change: it does not lower an evidence tier, it does not remove the
rendered-output rule, and it does not touch decision 10's permanent accessibility
evidence ceiling. It also creates one obligation on me — deferred acceptance items
must be written down when the evidence is fresh, not reconstructed at the end.

The second quotation is the reason the four handout questions are answered below
by me rather than sent to him.

### 2.3 Delivery routes he named

> *"Vies elegantne zapajat subagentov=Workerov, Planner Workerov a teraz
> experimentalne aj Worker Orchestratorov."*

> *"OPAKUJEM ALE, ZE PROMPTY 'Worker Orchestratorov' BUDEM UZ RIESIT MANUALNE, V
> TAKYCHTO PRIPADOCH SA MOZES ZASTAVIT, POSLEM PROMPT INEMU MODELU. TO ISTE PLATI
> PROSIM PRE 'Planner Workerov'."*

**Classification: ACCEPTED ROUTING DECISION.** Recorded per the handout's rule R1
as `Sub-agents/internal delegation: authorized-bounded` in every prompt I issue.
Two routes are manual and I stop at the artifact: Planner Worker (native Plan
mode) and the experimental Worker Orchestrator. Everything else I deliver myself.

### 2.4 The generation hazard he diagnosed himself

> *"Agent Orchestrator vyhadzoval chyby 'Received message_start for message … while
> message … is still open.' … ERRORY PRESTALI KED SOM MU VYSVETLIL, ZE NESMIE
> VELKE SUBORY GENEROVAT NARAZ ALE, ZE MA IST PO SEKCIACH, PROSTE APPENDOVAT."*

**Classification: VERIFIED OPERATIONAL FACT, adopted as a working rule.** Every
artifact in this directory is written by appending section by section against a
single `<!-- APPEND-POINT -->` sentinel, never as one large generation. This file
is the first application of it.

### 2.5 Documentation he named

> *"Bude treba aktualizovat @libretiles/libretiles_PRD.md aj @libretiles/README.md
> bude toho vela."*

**Classification: ACCEPTED DECISION, routed to the last slice of this whole**, so
the documents describe what shipped rather than what was planned. `AGENTS.md` is
added to that list by me, because it is the consumer projection and currently
states "Slovak assets now ship; live Slovak play is not enabled" and "Hungarian UI
not shipped" — both of which this whole changes.

### 2.6 His stake, restated because it changes acceptance standards

> *"Chcem sa nim prezentovat na pracovnom pohovore na ktorom mi velmi zalezi."*

**Classification: STANDING CONSTRAINT, already durable at
`PROJECT_CONTEXT.md:313-316`.** A fresh clone that crashes, a control that does
nothing, or a number that does not mean what it claims is a first-class defect. In
this whole the concrete form is: **`npm run build` and a real rendered probe are
not optional for any slice that touches a rendered surface**, precisely because he
has opted out of looking at it himself until the end.

---

## 3. The four handout questions — answered by me under §2.2, with the reasoning

He instructed me to use my own recommended answers. I am recording each as an
**Orchestrator decision taken under an explicit Cooperator autonomy grant**, not as
a Cooperator decision, because the distinction matters if one of them later turns
out wrong. Any of the four can be overridden by one word from him at any time.

### Q1 — relationship to the two other open wholes. **ANSWER: A (supersede).**

`12/00 multilingual-expansion` supersedes the remaining obligations of
`11/01 multilingual-tile-token-foundation` (slices F2c, F3, F4 and its R4
independent audit) and of `11/02 czech-polish-hungarian-variant-activation` (the
Hungarian obligation). Both older wholes receive a supersession record written by
me. Their **design decisions are carried forward verbatim, not restated** —
specifically `11/01/00_handout.md` §4.1-4.5 and
`11/01/90_orchestrator-plan-acceptance.md`.

Reasoning, honestly: RF-19 (`AP.md:255-262`) says a materially changed objective
begins a new identity and does not silently absorb an old one — so the supersession
must be **written**, which is what makes option A lawful rather than sloppy. The
substantive argument is that `11/01`'s slice labels only mean anything inside its
own accepted plan, and that plan is now nine slices old: Czech and Polish shipped
ahead of it, and four gaps it never contemplated have since been named. One
identity with one accepted plan is cheaper to reason about than two half-open ones,
and three open wholes with overlapping surfaces is the one thing that makes the
coordinate system meaningless.

Cost accepted: I owe two supersession records, and I must not paraphrase the
inherited design decisions.

### Q2 — the objective. **ANSWER: O1 → O3 → O2, plus Hungarian UI, as one whole.**

His own message bounds this more tightly than the handout's four options do. He
named the goal — *"na konci sa dostaneme k multijazycnej verzii hry Libre Tiles.
Toto je nas GOAL"* — and he named the method for the missing asset. So the
objective is not "pick one of O1-O4"; it is O1 and O3 and O2 in the only order in
which each is reachable, finishing with the fifth interface locale.

Sequencing reasoning:

```text
O1 FIRST because it needs nothing from anyone, costs no new asset, and is the
   thing that catches a regression across all four shipped variants at once. The
   briefing's own §47 puts it before adding any language, and it is the harness
   that makes O2 safe.
O3 SECOND because the outcome is genuinely uncertain and I want that uncertainty
   resolved BEFORE the expensive wire-format work is scheduled around it. If
   Hungarian expansion honestly fails, O2 still lands and Hungarian gameplay stays
   blocked on an external fact — and that is a legitimate outcome I can report,
   not a failure of this whole.
O2 THIRD because it is the largest and riskiest, and because its risk drops once
   O1's harness exists and once O3 has told us whether a Hungarian asset will
   actually arrive to justify it.
   O2 is required for Hungarian AND ONLY for Hungarian. Czech and Polish are
   single-code-point languages, so the F2b freeze carries them losslessly
   (DEFECT_LEDGER.md:1275-1290). If O3 fails, O2's product justification weakens
   to "any future multigraph language" and becomes a Cooperator re-decision.
O4 REJECTED for this whole. A fifth language family is a scope change against his
   stated Visegrad-Four goal and is blocked on the same licensing problem.
```

### Q3 — must a gameplay variant ship with a matching UI locale? **ANSWER: no coupling in architecture; coupling enforced only by product sequencing.**

The two axes stay independent in code, exactly as `useGameStore.ts` and
`locales.ts` already have them, and exactly as decision 8 states in terms
(`PROJECT_CONTEXT.md:1027`). What I am additionally deciding is the *product*
consequence for Hungarian: decision 8 excluded the Hungarian interface **for one
stated reason** — *"consistent with Hungarian gameplay being blocked on a real
inflection lexicon"* (`PROJECT_CONTEXT.md:1024-1026`). If this whole unblocks
Hungarian gameplay, that stated reason lapses, and shipping the fifth locale
follows from his own goal sentence. So:

```text
IF the Hungarian lexicon gate passes  -> ship messages.hu.ts and reference hu.png
IF it does not                        -> Hungarian UI is NOT shipped, hu.png stays
                                         deliberately unreferenced, and that is
                                         recorded rather than treated as a defect
```

### Q4 — does `readiness` need a third state? **ANSWER: no.**

Two values ship and stay. Fail closed: gap G2's dictionary validation decides
`playable` versus `unavailable`, and an invalid asset yields `unavailable`. A third
state changes the public payload contract, its exact-key-set test, the picker and
the play-page gating, for no behaviour a player can use. The briefing's own §7 says
not to add speculative fields. Revisit only when a real in-progress asset needs to
be visible to a player, which is not a state this whole produces.

---

## 4. The bounded objective, and the nine-slice plan

### 4.1 Objective, one sentence

> **Make Hungarian the fifth playable variant and the fifth interface locale of
> Libre Tiles, on machinery that makes the next language boring: every shipped
> lexicon reproducible from a pinned upstream by a committed script, every
> malformed language asset failing closed, and a multi-code-point tile carried
> losslessly from the engine to the board a player looks at.**

If the Hungarian lexicon gate honestly fails, the objective degrades to the same
sentence without Hungarian, and that degradation is a reportable outcome rather
than a failure — see section 3 Q2.

### 4.2 Slices, in dependency order

Each row states its own smallest coherent outcome, its evidence tier, and its
delivery route. Nothing here is authority; each slice becomes authority only in its
own issued prompt.

```text
V1  GENERIC PER-VARIANT INVARIANT HARNESS                       tier E1  subagent Worker
    One parameterized test file over list_installed_variants(). TESTS ONLY, zero
    production change. Per-variant totals stay in per-variant tests. Closes G1.
    Gate: passes on all four shipped variants at 47ed8bf and fails loudly on a
    deliberately malformed synthetic manifest.

V2  FAIL-CLOSED ASSET VALIDATION + MANIFEST PROVENANCE          tier E2  subagent Worker
    Bounded, cached structural validation of a declared lexicon so readiness is no
    longer file-existence only; expensive whole-file invariants move to the V1
    harness plus one new management command. Manifest gains provenance fields.
    Closes G2 and G3. Depends on V1.

V3  REPRODUCIBLE PINNED BUILD SCRIPTS FOR CZECH AND POLISH      tier E2  subagent Worker
    build_czech_lexicon.py and build_polish_lexicon.py in the shape of
    build_slovak_lexicon.py, proving the COMMITTED assets are reproducible.
    This is the Cooperator directive of section 2.1. Depends on V2 for the
    provenance fields the scripts populate.

V4  HUNGARIAN LEXICON EXPANSION ATTEMPT                         tier E2  subagent Worker
    build_hungarian_lexicon.py using a PINNED spylls to resolve AF aliases and
    follow suffix continuations, with hunspell 1.7.3 as the independent oracle.
    Writes the candidate to /tmp only. Commits the SCRIPT, not the asset.
    Outcome genuinely uncertain. Five MUST-gates in section 5.

V5a HUNGARIAN ASSETS COMMITTED, VARIANT STILL NOT DISCOVERABLE  tier E2  subagent Worker
    hungarian.txt + hungarian.LICENSE only. NO hungarian.json. Without a manifest
    the variant is invisible to list_installed_variants() and to the serializer, so
    the product cannot reach a Hungarian game and cannot crash on a digraph tile.
    Depends on V4 PASS.

V6  WIRE SCHEMA 4 END TO END — the F2b freeze comes out                tier E3
    All seven guards removed TOGETHER with state_schema_version 4,
    BoardCell[][] on the wire, localStorage v4, board/rack/blank/draw rendering,
    evaluate_scoring_move re-pointed at WordAuthority and _word_passes_dictionary
    deleted. PLANNER WORKER FIRST (manual delivery), then a fresh implementation
    session, then FRESH INDEPENDENT ACCEPTANCE that cannot be my subagent.
    Depends on V1 as its regression net. Independent of V4's outcome.

V7  AI BOUNDARY LOSSLESS FOR MULTI-CODE-POINT CELLS             tier E2/E3
    build_ai_state_dict stops being lossy; the grid renders the FIRST CODE POINT
    with the full token in the sparse exact map; the three Zod/length-1 guards in
    the move route relax. MOVE CORE hash and version PROVED UNCHANGED. Depends on V6.

V5b HUNGARIAN VARIANT ACTIVATED                                 tier E2  subagent Worker
    hungarian.json only: MTA alphabet order, sourced tile distribution, readiness
    playable. This is the commit that makes Hungarian reachable, and it lands only
    after V6 and V7 can carry SZ, GY and DZS. Depends on V5a, V6, V7.

V8  HUNGARIAN INTERFACE LOCALE                                  tier E2  WORKER ORCHESTRATOR (manual)
    messages.hu.ts (300 keys), LOCALES += "hu", a sourced pluralHu, GLOSSARY.md
    Hungarian section, hu.png referenced. Depends on V5b per section 3 Q3.

V9  DOCUMENTATION AND CLOSURE                                   tier E1  subagent Worker + me
    libretiles_PRD.md, README.md, AGENTS.md; then PROJECT_CONTEXT.md,
    DEFECT_LEDGER.md and 99_closure.md written by me. Depends on everything.
```

### 4.3 Why V5 is split, and it is the most important sequencing decision here

`DEFECT_LEDGER.md:806-826` records why F2 was split at all: *"if the backend
emitted v4 while the frontend still read v3, the product would be broken between
two slices. The Cooperator opens this application, and a fresh clone that crashes
is a first-class defect in his frame."*

The identical hazard applies to Hungarian. A `hungarian.json` manifest is the only
thing that makes a variant discoverable — `list_installed_variants()` globs
`*.json` and the serializer validates against that list. If the manifest lands
before the wire can carry a digraph, the very first Hungarian `SZ` placement
reaches `_legacy_wire_board_and_blanks()`, which **raises rather than truncating**
— the correct behaviour, and a 500 in his browser. Splitting the asset commit from
the manifest commit costs one extra slice and removes that window entirely.

### 4.4 Delivery routes, recorded once

```text
V1 V2 V3 V4 V5a V5b V9   subagent Worker, delivered by me
                         Sub-agents/internal delegation: authorized-bounded —
                         Cooperator-selected delivery route for this logical
                         whole, recorded 2026-09-03
V6 planning              PLANNER WORKER, Native planning mode: required,
                         COPY-PASTE delivery by the Cooperator. I stop at the file.
V6 acceptance            FRESH INDEPENDENT ACCEPTANCE. Rule R2 of the handout and
                         AP.md:1395-1405: it CANNOT be my subagent. Copy-paste.
V8                       WORKER ORCHESTRATOR, experimental, copy-paste. First test
                         of the profile proposed in meta/BRAINSTORMING.md section 1.
```

---

## 5. The Hungarian lexicon gate — inherited verbatim, not restated

Source: `DEFECT_LEDGER.md:1442-1460`, adopted from the Cooperator-run Deep Research
at `11/02/00_deep_research.md`. Carried here **verbatim in substance** because V4's
prompt must not paraphrase it.

```text
MUST contain, after the same NFC / casefold / isalpha / len>=2 filter:
    házat   házban   házakat   kutyát   kutyák   asztalon
MUST be plausibly in the MILLIONS, not near the 96 955 stem count. Compare:
    sk 3 005 250, cs 3 930 497, pl 3 721 704. No source publishes a gold-standard
    Hungarian total, so this is a sanity check rather than an exact target.
MUST be independently re-validated: generate with Spylls, then re-check emitted
    standalone forms with hunspell 1.7.3 itself as an oracle. Spylls' demo checks
    FORBIDDENWORD and NEEDAFFIX but not every exclusion; hunspell can remove a bad
    generated form, though it cannot reveal a legal form Spylls never generated —
    which is why the six-word gate is indispensable.
MUST pin the exact Spylls implementation, not "latest": 0.1.7 dates from 2022-01-23.
MUST resolve the Spylls licence contradiction before any of its code or output
    ships. (Repository states MPL-2.0; setup.py carries an MIT classifier.)
```

Out of scope for V4, both from the original brief: **no** two-letter authority file
for Hungarian, and **no** runtime spell-checker call replacing the in-memory sorted
index.

### 5.1 What I measured that changes the risk on this gate

```text
hunspell 1.7.3 IS ALREADY INSTALLED on this host — `hunspell -vv` returns
  "@(#) International Ispell Version 3.2.06 (but really Hunspell 1.7.3)".
  The independent oracle the research demanded needs no acquisition.
/usr/bin/wordforms and /usr/bin/analyze are also present and were NOT considered by
  the previous acquisition Worker. `wordforms` is hunspell's own documented
  replacement for the deprecated `unmunch`. The research says it is "not the
  missing complete expander" and explains why, so it is not the primary route —
  but it is a cheap SECOND data point and V4 should record its measured output
  rather than skipping it on the strength of a document.
spylls is ABSENT from backend/.venv. V4 must therefore make a dependency decision,
  and it is a real one: build_slovak_lexicon.py's own docstring promises
  "No Poetry/npm dependency."
```

### 5.2 The dependency decision I am taking for V4, so the Worker does not have to

`spylls` becomes a **build-time-only, optional, exactly-pinned Poetry group** named
`lexicon`, marked `optional = true` so `poetry install` for the application is
byte-unchanged and the app's runtime dependency graph does not grow. The script
imports it lazily inside the function that needs it and fails closed with an exact
install instruction when it is absent, exactly as `build_slovak_lexicon.py` fails
closed when `unmunch` is not on PATH.

Reasoning: a scratch virtualenv in `/tmp` would make the build unreproducible from
the repository alone, which defeats the entire point of the Cooperator's directive
in section 2.1. An ordinary main dependency would put a 2022 package with
contradictory licence metadata into the deployed surface, which the dependency
posture at `PROJECT_CONTEXT.md:563-590` forbids on sight. An optional group is the
only option that is both reproducible and outside the deployed surface.

⚠ This decision is mine and it is reversible. If V4 measures that Poetry's optional
group cannot be resolved without touching `poetry.lock` in a way that changes the
application's installed set, the Worker must STOP and report rather than improvise.

---

## 6. Asset traps I measured, which would each have broken a naive validation rule

These are the reason gap G2 cannot be implemented from the briefing's wording
alone. Every line below is output I produced from the committed assets.

```text
T1  collins2019.txt LINE 1 IS NOT A COMMENT.
      "Collins Scrabble Words (2019). 279,496 words. Words only."
    Line 2 is empty. Lines 3+ are UPPERCASE words. `gamecore/fastdict.py:_read_words`
    skips only lines starting with the comment prefix `#`, so this header survives
    stripping and is discarded later by the `str.isalpha` predicate — it contains
    spaces, digits and punctuation. A validation rule phrased as "no header lines in
    word data" or "every non-comment line must be a valid word" FAILS on the shipped
    English dictionary. The correct rule is: every line that SURVIVES the loader's
    own comment-strip plus predicate must be a valid word.
T2  CASING IS NOT UNIFORM ACROSS SHIPPED LEXICONS.
      collins2019.txt  UPPERCASE      sowpods.txt  lowercase
      slovak/czech/polish.txt  lowercase
    A rule phrased "expected casing: lowercase" fails on English. Normalize first,
    compare second — the loader already NFC-casefolds.
T3  THE THREE EXPANDED LEXICONS EACH CARRY EXACTLY TWO `#` HEADER LINES, and the
    text is now known byte-exactly, which is what makes V3 able to reproduce them:
      slovak.txt  "# Slovak playable lexicon expanded from hunspell-sk (LibreOffice
                   dictionaries sk_SK @ 75f5dff8c972fff4a32e4ea8434722c277f02a3f)."
                  "# Not an official SSS tournament list."
      czech.txt   same shape, hunspell-cs / cs_CZ, second line
                  "# Not an official tournament list."
      polish.txt  same shape, hunspell-pl / pl_PL, second line
                  "# Not an official tournament list."
    Measured `wc -l`: slovak 3 005 252 · czech 3 930 499 · polish 3 721 706 —
    each exactly two more than its recorded unique word count.
T4  NO SHIPPED LEXICON HAS A BOM. First three bytes measured:
      slovak/czech/polish  23 20 53 / 23 20 43 / 23 20 50   ("# S", "# C", "# P")
      collins2019          43 6f 6c                          ("Col")
    So a BOM check is a real new assertion, not a re-assertion of current state.
T5  slovak_two_tile_words.txt is 106 lines: THREE `#` comment lines and 103 words.
    Its comments include a URL. A two-tile validation rule must strip comments the
    same way the loader does (`load_two_tile_words`, NFC casefold, `#` skipped).
T6  czech.txt CONTAINS NON-CZECH CODE POINTS ON PURPOSE — the Greek mu in
    `μa μg μm μv` is in the shipped file (last ten words end with them). The
    alphabet invariant is about TILES and `alphabet_order`, NOT about the lexicon.
    A validation rule that requires every lexicon character to be in the variant
    alphabet would make Czech `unavailable`. Do not write that rule.
```

### 6.1 The performance constraint that shapes G2's design

`readiness` is computed inside `GET /api/game/variants/` on every request. Czech is
54 105 021 B and Polish 51 607 141 B. Any validation that reads a whole lexicon per
request is a product defect dressed as a correctness improvement.

The design I am fixing for V2, so no Worker has to invent it:

```text
CHEAP AND PER-REQUEST (must fail closed)
  file exists · non-empty · no BOM · a bounded prefix decodes as strict UTF-8 ·
  the prefix yields at least one line that survives the loader's own comment-strip
  and predicate · declared two-tile file exists when declared
  cached on (resolved path, size, mtime_ns) so repeated requests cost one dict hit
EXPENSIVE AND NOT PER-REQUEST
  every line NFC · duplicate policy · total count sanity · the per-variant
  inflected-form MEMBERSHIP probe · alphabet/tile cross-checks
  home: the V1 generic harness plus one new `manage.py validate_lexicons` command
```

A range check is not a correctness check — `DEFECT_LEDGER.md` records the Hungarian
candidate passing every mechanical bound at 81 509 words and being caught only by a
six-word membership probe a Worker added on its own initiative. The membership probe
is therefore **required per playable variant**, and it belongs in the harness where
it can afford to read the file.

---

## 7. Proposed closure conditions for `12/00`

Drafted now, before any work, because era 10 proved that closure conditions written
at the start are what stop a whole from growing. Fourteen conditions.

```text
 1  One parameterized generic invariant test runs over EVERY installed variant and
    fails loudly on a malformed manifest. Per-variant totals stay in per-variant
    tests, not in the generic loader.
 2  Lexicon asset validation is mechanical and FAILS CLOSED: an invalid or missing
    lexicon yields readiness `unavailable`, never `playable`. Two readiness values
    only.
 3  Each shipped lexicon's provenance — upstream identity, expansion tool and
    version, entry count, SPDX expression, licence-file pointer — lives in the
    MANIFEST, not only in a Meta report.
 4  Every shipped non-English lexicon is reproducible by a COMMITTED script under
    `backend/scripts/` from a pinned upstream commit with pinned SHA-256s, and the
    reproduction is proved against the committed asset.
 5  A deliberately malformed synthetic manifest and a deliberately corrupt synthetic
    lexicon each produce the intended failure, proved by a test that FAILS BEFORE
    the fix.
 6  A per-variant membership probe of real inflected forms exists for every playable
    variant.
 7  English, Slovak, Czech and Polish behaviour is unchanged: the public variant
    payload keeps exactly its four keys, all four stay `playable`, no seeded bag
    changes, and the MOVE CORE SHA-256 and version are proved unchanged.
 8  All seven F2b freeze guards are removed TOGETHER with the wire moving to
    `state_schema_version` 4, and `_word_passes_dictionary` is deleted with
    `evaluate_scoring_move` re-pointed at `WordAuthority`.
 9  The Hungarian acceptance fixture passes with at least TWO different
    multi-character tokens — not only `SZ`.
10  The L·L synthetic canary still passes, proving the implementation did not
    generalize only to `len(token) <= 2 && isalpha()`.
11  Hungarian is playable end to end, OR the Hungarian lexicon gate is recorded as
    honestly failed with its measured evidence and Hungarian stays blocked. Either
    outcome satisfies this condition; a silent omission does not.
12  If Hungarian is playable, the fifth interface locale ships with exact key-set
    and interpolation parity, a sourced plural function, and `hu.png` referenced.
13  All eight standing gates green at the closing commit, with the pytest summary
    quoted verbatim, ELEVEN dynamic routes and ZERO static routes.
14  FRESH INDEPENDENT ACCEPTANCE by a session that did not implement the wire-schema
    change, plus the deferred Cooperator acceptance batch delivered once at the end
    per section 2.2. Meta archive complete including `99_closure.md`, with
    `PROJECT_CONTEXT.md` and `DEFECT_LEDGER.md` updated through the closing commit,
    and supersession records written for `11/01` and `11/02`.
```

⚠ Conditions 9 and 10 are inherited verbatim from `11/01/00_handout.md` §11 and must
not be weakened by this whole's supersession of that whole.

---

## 8. Exchange ledger — appended as each pair is archived

`AP.md:322-336`: the prompt and its ACTUAL outcome are archived together, only after
the outcome exists, and in Git both files share one unique first-add commit. A
`*_report_*.md` must begin exactly `### Report for ORCHESTRATOR_CHAT` and must never
be a byte-copy of its prompt.

```text
session/exchange   slice   phase            files                              outcome
01 / 01            V1      implementation   01_implementation_00.md
                                            01_report_00.md                    pending
```

### 8.1 Standing per-prompt checklist I run before issuing anything

```text
1  regenerate the coordinate-bearing region WHOLE; never string-patch the previous
   prompt (three of five era-10 structural defects came from repairs)
2  python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>  -> exit 0
3  cross-check negative authority against mandated artifacts: for every file a later
   section REQUIRES, confirm an earlier section PERMITS it
4  RF-16 route binding named explicitly:
   env -u APPIMAGE -u ARGV0 -u APPDIR backend/.venv/bin/python ...
   with `poetry run` named as the declared route that could not be used
5  the formed-word invariant sentence copied verbatim into any prompt touching word
   legality
6  the alphabet SUBSET direction stated, with the Czech tileless `CH` example that
   already broke one Worker draft
7  no `/home/agile/meta/...` path offered to a Worker as repository evidence —
   inline it instead
8  the report field asking what the Worker can still see that the prompt did not
   anticipate (eight era-10 findings arrived through it)
9  every number in the prompt either measured by me in this session or written as
   "unmeasured"
```

---

## 9. Slice V1 landed — Worker session 01, exchanges 01 and 02

```text
3878847d367490217c4b1b3d3a2af763aaad1a32   V1  the generic harness            1 file, +428
61720aa701132085809a9012ee29e446c622bd4f   V1b stem/slug + derived-key guard  1 file, +114 −1
```

Both reports are `PASS` with `implementation-PASS`, and both are archived beside their
prompts: `01_implementation_00.md` + `01_report_00.md`, `01_implementation_01.md` +
`01_report_01.md`. Exchange 02 was a lawful `current-worker-session` renewal — the
session was healthy, assumptions unchanged, independence not required, and retained
context was explicitly classified as convenience rather than authority
(`PROMPT_CONTRACTS.md:359-365`, `AP_ORCHESTRATOR.md:174-178`).

### 9.1 What I re-verified myself rather than accepting from the reports

`PROJECT_CONTEXT.md` lesson 3: Worker reports are claims. Measured by me after each
exchange:

```text
git rev-parse HEAD                  61720aa701132085809a9012ee29e446c622bd4f
git ls-remote origin refs/heads/main 61720aa701132085809a9012ee29e446c622bd4f  EQUAL
git status --porcelain=v1           empty
git diff --name-only 3878847 HEAD   backend/tests/test_variant_invariants.py  (only)
git show --name-status 3878847      A backend/tests/test_variant_invariants.py (only)
git rev-parse HEAD:.ap              9c5cc44f8b6c92dd56ad2427d13223d7d59c5656  unchanged
pytest --collect-only               465 tests collected   (456 -> 465, +9 as claimed)
pytest tests/test_variant_invariants.py   71 passed in 21.42s
```

Closure conditions 1, 5 and 6 from section 7 are now satisfied in substance; condition
7's "no seeded bag changes" is satisfied trivially because no production file moved.

### 9.2 THE WORKER OVERRULED ME ON EVIDENCE, TWICE, AND WAS RIGHT BOTH TIMES

`PROJECT_CONTEXT.md` lesson 8 and lesson 12: say so plainly, because that is what keeps
Workers reporting honestly. Both were re-measured by me independently before being
recorded here.

```text
W1  MY PROMPT'S OWN GATE COMMAND CANNOT RUN.
    Exchange 01 section 9b said
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m manage.py check
    MEASURED BY ME:
        -> Error while finding module specification for 'manage.py'
           (ModuleNotFoundError: __path__ attribute not found on 'manage' …)
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check
        -> System check identified no issues (0 silenced).
    ⛔ CLASSIFICATION: ORCHESTRATOR DESIGN DEFECT, not Worker error. The `-m` came from
    the opening handout's section 14 gate list and I copied it without running it. The
    same defect is therefore latent in that handout and in any prompt derived from it.
    `PROJECT_CONTEXT.md:361-364` lists the gates WITHOUT `manage.py check`, so the
    stray `-m` entered when that gate was added to a handout.
    ⛔ CORRECTED STANDING GATE SET for every future prompt in this whole:
        cd backend
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python manage.py check     <- NO -m
        env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
        cd ../frontend && npm run typecheck ; npx vitest run ; npm run lint ; npm run build

W2  THE SLUG / FILENAME-STEM DIVERGENCE IS A LIVE PRODUCT HAZARD.
    Found by the Worker in its exchange-01 field 17. RE-MEASURED BY ME:
        a manifest file `de.json` declaring "slug": "german"
        list_installed_variants()  -> ['german']
        len(list) == len(*.json)   -> True     (so the count guard is blind to it)
        load_variant('german')     -> FileNotFoundError: Variant 'german' not found
        load_variant('de')         -> loads, and reports .slug == 'german'
    Reachability confirmed at three production sites:
        game/serializers.py:180 · game/serializers.py:215 · game/services.py:173
        each validates an incoming variant_slug against
        {v.slug for v in list_installed_variants()}
    So `german` passes game creation and queue join, and every later load fails.
    🐞 DEFECT ID mle-01-F01, severity medium, status `confirmed`, evidence class
    reproduced-dynamic. Mitigated at the harness level by G26a at `61720aa` — a
    divergent manifest is now unshippable — but the PRODUCTION divergence remains.
```

### 9.3 One place where the Worker corrected ITSELF, and why that matters more than the finding

Its exchange-01 field 17.5 claimed `datetime.fromisoformat("2026")` succeeds, so the
`fetched_at` check would admit a bare year. I inherited that claim into exchange 02's
section 3c without measuring it. The Worker then measured it and reported that **both of
us were wrong.** Re-measured by me on the project interpreter, Python 3.12.12:

```text
fromisoformat('2026')                -> ValueError: Invalid isoformat string: '2026'
fromisoformat('2026-09')             -> ValueError: Invalid isoformat string: '2026-09'
fromisoformat('20260901')            -> 2026-09-01T00:00:00      <- the REAL hole
fromisoformat('2026W364')            -> 2026-09-03T00:00:00      <- the REAL hole
fromisoformat('2026-W36-4')          -> 2026-09-03T00:00:00      <- sharpest: 10 chars,
                                        so only the round-trip catches it
fromisoformat('2026-09-01')          -> 2026-09-01T00:00:00
```

The strengthening was still worth doing and now has demonstrated teeth — against ISO
basic and week-date forms rather than against a bare year. The transferable lesson is
the Worker's own: **an unmeasured item in the "what you can still see" field is a lead,
not a finding, and it arrives wearing the same confidence as a measurement.** From here
on I treat that field as two classes and say which is which before acting on it.

### 9.4 Four observations routed forward rather than actioned now

```text
O1  ROUTED TO V2. Close the mle-01-F01 divergence at INGEST, not at lookup: have
    _load_variant_from_path reject a manifest whose declared slug does not equal
    slugify(path.stem), with a new VariantManifestError code `slug_stem_mismatch`.
    Cheaper than making load_variant search declared slugs, which would parse the whole
    directory on every call.
    ⚠ PUBLIC-RESPONSE CONSEQUENCE, verified by me in game/views.py:117-127: that branch
    catches FileNotFoundError separately (-> readiness `unavailable`) and funnels every
    other exception into `except Exception` (-> the variant is OMITTED from
    GET /api/game/variants/ entirely). So a divergent manifest would VANISH from the
    public list rather than appear as unavailable. That is the behaviour I want — an
    unloadable variant must not be advertised — but it is a public contract change and
    V2's prompt must say so and test it.
    ⚠ COST PRICED IN: G26b is today a characterization test of behaviour that would
    then no longer exist. V2 inverts it into a rejection test in the same slice.
O2  ROUTED TO V2. `display_label` is a fifth derived property with no declared twin —
    verified by me: VariantDefinition's properties are distribution, tile_points,
    total_tiles, display_label, dictionary_path, two_tile_words_path, playable_letters.
    The last two have legitimate declared twins (dictionary_file, two_tile_words_file)
    and are correctly excluded. `display_label` should join the forbidden-derived-key
    set.
O3  ROUTED TO V2. Assert `path.stem == slugify(path.stem)`, one line, closing the other
    direction of the divergence: a filename that is not itself canonical-slug-shaped is
    unloadable even when its declared slug matches its stem.
O4  RECORDED, NOT ACTIONED. `variant_name` is accepted by the loader
    (variant_store.py:318-323) and declared by no shipped manifest, so the entire
    `f"{language} – {variant_name}"` display path is unexercised. Also recorded:
    `canonicalize_tile_token`'s documented `strip()` step is unreachable from manifest
    ingest, because `_parse_asset_token` rejects whitespace at :219-222 BEFORE
    canonicalizing at :234. Both are latent-documentation items, not defects. The first
    variant that declares `variant_name` is the first to test it — hungarian.json in
    V5b will NOT declare one.
```

### 9.5 Exchange ledger, updated

```text
session/exchange   slice   phase            files                          outcome
01 / 01            V1      implementation   01_implementation_00.md
                                            01_report_00.md                PASS 3878847
01 / 02            V1b     implementation   01_implementation_01.md
                                            01_report_01.md                PASS 61720aa
```

---

## 10. The Hungarian probe changed the plan — session 02 interrupted, probe completed by me

### 10.1 What happened, in order

```text
02_probe_00.md          issued, 405 lines, apfieldcheck exit 0
dispatch                KILLED by an external billing limit on the delivery account:
                        "预扣费额度失败, 用户剩余额度: ＄0.285318,
                         需要预扣费额度: ＄0.300000"
                        Not a protocol failure, not a refusal, not a prompt defect.
02_interruption_00.md   written by me from safely known facts, per AP.md:322-336. No
                        terminal report exists, so NO 02_report_00.md may ever be created
                        for this exchange, and session ordinal 02 is CONSUMED.
probe completed by me   directly, read-only against the repository, under Cooperator
                        decision 13 plus the 2026-09-03 autonomy instruction
90_hungarian-expansion-probe.md   the evidence, filed in the 9N_ Orchestrator band
                        precisely so nobody mistakes it for audited Worker evidence
```

⛔ **The permanent evidence cost:** that probe is **non-independent**. I was both measurer
and reviewer, and only the mechanical hunspell oracle corroborates my judgement calls.
Recorded here and in the artifact itself. Every mutation its findings imply still goes to a
Worker under a complete prompt.

⚠ **Operational fact that changes my strategy for the rest of this whole:** subagent
delivery is now unreliable on an external account balance. I must therefore prefer fewer,
larger Worker grants over many small ones, and I must be prepared to complete read-only
evidence work myself. That is exactly the pressure the Cooperator anticipated in his
`Worker Orchestrator` idea (`/home/agile/meta/BRAINSTORMING.md` section 1) — the economics
argument for it is now measured, not theoretical.

### 10.2 The finding, in three lines

```text
THE EXPANDER WORKS.   Spylls 0.1.7 resolves the 1 559-entry AF alias table and follows
                      suffix continuations. Six-word gate 6/6. Twenty-three-word gate
                      23/23. hunspell 1.7.3 accepted 3 000 of 3 000 sampled forms.
THE ASSET DOES NOT FIT. ~4.27 billion non-compound forms (~77 GB). At a 15-code-point
                      ceiling still ~301 million (~4.5 GB). Compare czech.txt at
                      3 930 497 words / 54 105 021 B, which already drew a GitHub
                      large-file warning.
SO THE GATE OVERSHOT.  DEFECT_LEDGER.md:1447 required "plausibly in the MILLIONS". The
                      answer is BILLIONS, and that overshoot is the blocker.
```

🐞 **DEFECT / BLOCKER `mle-01-B01`**, severity high, status `confirmed`, evidence class
`reproduced-dynamic`, owner: Cooperator decision. *A flat enumerated Hungarian lexicon is
not committable to this repository at any defensible board bound.* Full measurement in
`90_hungarian-expansion-probe.md` sections 9 and 13.

### 10.3 The decision I have taken, and how to overturn it in one word

Four options were measured; three fail. Recorded in full at
`90_hungarian-expansion-probe.md` section 13.

```text
A  commit the full list                  REJECTED on measurement (~4.5 GB, LFS forbidden)
B  runtime spell-checker per lookup       REJECTED — kills the prefix probe, and the engine
                                          authors EVERY move in this product, so this would
                                          disable Hungarian AI rather than degrade it
C  a frequency- or paradigm-bounded subset REJECTED — no licence-clean frequency source
                                          exists, and it makes the lexicon a judgement call
D  GENERATE LOCALLY AT SETUP from the      ADOPTED
   pinned 4 MB .dic/.aff
```

**D in one sentence:** commit `build_hungarian_lexicon.py` plus the two pinned source
hashes, have it materialize a bounded lexicon into `backend/assets/dicts/hungarian.txt` at
setup time, gitignore that output, and let gap G2's fail-closed readiness report
`unavailable` until the local build has run.

Why this is his method rather than a deviation from it: his instruction was that the
dictionaries be *downloaded by a script*. For Slovak, Czech and Polish the output happened
to be small enough to commit too. For Hungarian it is not, so D keeps the method and drops
only the incidental habit of committing the output.

⛔ **This is a Cooperator-owned material decision** — it changes what "shipped" means for
one language, and it introduces the first gitignored asset in the project. He can overturn
it with one word. The four costs of D are written out in
`90_hungarian-expansion-probe.md` section 13 so the choice is informed: a fresh clone has
no Hungarian until setup runs; the build needs network and minutes and must stay opt-in;
the gitignored asset and the fail-closed readiness path must be tested together; and the
code-point ceiling must be **derived from 15 tiles**, not guessed — a 15-code-point ceiling
is too tight once `DZS` is a tile.

### 10.4 Revised slice plan

Section 4.2's V4 / V5a / V5b are **superseded**. What replaces them, and what survives
untouched:

```text
SURVIVES UNCHANGED
  V2   fail-closed asset validation + manifest provenance, now MORE important: it is what
       makes a generated-locally lexicon safe, because readiness must report `unavailable`
       on a fresh clone rather than crashing. Also absorbs the three routed observations of
       section 9.4 (slug_stem_mismatch at ingest, display_label, canonical stem).
  V3   reproducible pinned build scripts for Czech and Polish. Unchanged, and it now
       doubles as the proving ground for the exact script shape V4' needs.
  V6   wire schema 4 end to end. UNCHANGED and still required — but note its product
       justification now rests on "any future multigraph language" plus Hungarian-behind-a-
       local-build, not on Hungarian shipping as a committed asset.
  V7   AI boundary lossless for multi-code-point cells. Unchanged.
  V9   documentation and closure. Now also documents the local-build step for Hungarian.
REPLACED
  V4'  build_hungarian_lexicon.py committed, with pinned hashes, a spylls `lexicon`
       optional Poetry group, a DECLARED code-point ceiling derived from 15 tiles, and the
       six-word gate asserted BY THE SCRIPT as a fail-closed post-condition. The script is
       committed; its output is not.
  V5a  DROPPED. There is no committable hungarian.txt to land.
  V5b  hungarian.json manifest + .gitignore entry + the fail-closed readiness path proved
       by test. Still lands only after V6 and V7 can carry SZ, GY and DZS.
  V8   Hungarian interface locale. Unchanged, and section 3 Q3's condition is now
       satisfiable: Hungarian gameplay is reachable, just not on a fresh clone.
```

### 10.5 Closure conditions amended

Section 7 conditions 9, 10, 12, 13 and 14 stand unchanged. Condition 11 is replaced,
because its original wording assumed a committed asset:

```text
11 (WAS)  Hungarian is playable end to end, OR the Hungarian lexicon gate is recorded as
          honestly failed with its measured evidence.
11 (NOW)  Hungarian is playable end to end AFTER a documented, opt-in local lexicon build,
          and BEFORE that build the variant reports readiness `unavailable` without
          crashing — both halves proved by test. The committed artifact is the build
          script plus its pinned source hashes, never the lexicon.
NEW 15    The Hungarian code-point ceiling is DERIVED from the 15-tile board bound and the
          Hungarian tile set, declared in the manifest, and justified in writing. It is
          never a guessed constant.
NEW 16    The six-word gate — házat házban házakat kutyát kutyák asztalon — is asserted by
          the build script itself as a fail-closed post-condition, so a future upstream
          change that breaks expansion fails the build instead of shipping a broken lexicon.
```

### 10.6 Exchange ledger, updated

```text
session/exchange   slice   phase            files                              outcome
01 / 01            V1      implementation   01_implementation_00.md
                                            01_report_00.md                    PASS 3878847
01 / 02            V1b     implementation   01_implementation_01.md
                                            01_report_01.md                    PASS 61720aa
02 / 01            V4 probe preflight       02_probe_00.md
                                            02_interruption_00.md              INTERRUPTED
                   evidence completed by ORCHESTRATOR, non-independent:
                                            90_hungarian-expansion-probe.md
```

---

## 11. Slice V2a landed — Worker session 03, exchange 01, plus one Orchestrator-authored follow-up

```text
5f63e0da2a4c0aba0edcd905e488c0f7a32163e9   V2a  slug_stem_mismatch at ingest   3 files, +120 −20
1f39ff4da678ffb519222e6cd97a90117298a371   --   ORCHESTRATOR-AUTHORED: the G26a
                                                docstring correction the Worker
                                                measured but was forbidden to make
                                                                                1 file, +4 −3
```

Pair archived as `03_implementation_00.md` + `03_report_00.md`. Report `PASS`,
`implementation-PASS`.

### 11.1 What I re-verified myself

```text
git rev-parse HEAD                    1f39ff4da678ffb519222e6cd97a90117298a371
git ls-remote origin refs/heads/main  1f39ff4da678ffb519222e6cd97a90117298a371   EQUAL
git status --porcelain=v1             empty
git diff --name-only 61720aa 5f63e0d  exactly the three allowlisted paths
git rev-parse HEAD:.ap                9c5cc44…  unchanged
variant_store.py:337-344              the new check, read by me; validate_dictionary_file
                                      is at :353 and _parse_alphabet_order at :363, so the
                                      ordering requirement of the prompt holds
pytest --collect-only                 466 tests collected  (465 -> 466, +1 as claimed)
repo-wide grep "variant_store.py:"    ten hits, ALL inside test_variant_invariants.py;
                                      the Worker's claim that no anchor outside the
                                      allowlist went stale is CONFIRMED
```

All eight gates re-measured green by me at `1f39ff4`:

```text
mypy config game gamecore accounts catalog   Success: no issues found in 83 source files
ruff check .                                 All checks passed!
manage.py check                              System check identified no issues (0 silenced).
pytest                                       462 passed, 4 skipped in 220.23s (0:03:40)
npm run typecheck                            exit 0
npx vitest run                               450 passed | 3 skipped (31 files | 1 skipped)
npm run lint                                 exit 0
npm run build                                exit 0, ELEVEN dynamic routes, ZERO static
```

### 11.2 ⛔ A THIRD ORCHESTRATOR PROMPT DEFECT, and it is the one the archive warned about

My section 5c said G26a "must remain **exactly as it is**". The same section's ⚠ said to
correct any comment in that module claiming `G9` is blind to the divergence. **G26a's own
docstring was exactly such a comment.** Both instructions could not hold.

The Worker chose the byte-exact instruction, left the stale sentence, and reported it with
the exact replacement text already written. That is the best available behaviour and it is
the third time in this whole that a prompt of mine carried an internal contradiction or a
false premise:

```text
defect 1  `-m manage.py check` — a gate command that cannot run           (exchange 01/01)
defect 2  the `fetched_at` bare-year premise, inherited unmeasured        (exchange 01/02)
defect 3  "remain exactly as it is" versus "correct the stale comments"   (exchange 03/01)
```

⚠ `PROJECT_CONTEXT.md` lesson 16 already names this class — *"after writing the negative
authority, re-read the mandated tests and ask whether you just forbade one of them"* — and
lesson 15 says that when a second slice in one domain also generates defects, **the
Orchestrator's model of that domain is the fault, not the slice size.** Three in three
exchanges is past that threshold. My operational correction, applied from V2b onward:

```text
R-A  A "do not change X" instruction must name WHY. If the reason is "its assertions are
     still correct", then say that, so a Worker can see that a DOCSTRING is not an
     assertion and is not covered.
R-B  Prohibitions get written LAST, after the obligations, and then read against them in
     one pass. Not in a separate drafting session where the two never meet.
R-C  When a prompt tells a Worker to correct stale comments, it must ENUMERATE them, from
     my own grep, rather than delegating the search. I had the grep output and did not use
     it.
```

### 11.3 The docstring correction — Orchestrator-authored, and the cost recorded

I applied the one-line replacement myself at `1f39ff4` under Cooperator decision 13. It
qualifies on all five bar items: the whole path was measured first (repo-wide grep for
`variant_store.py:` anchors, confirming the Worker's claim), the change is one docstring
sentence in a test file with no assertion touched, the exact replacement text was already
measured and quoted by the Worker, and all eight gates were run in full at the resulting
commit.

⛔ **Evidence cost, permanent:** `1f39ff4` is **non-independent**. Only the mechanical gates
corroborate it. It joins `f40d8a0`, `8ef5992` and `f983c3d` from era 10 on that list, and
it must never be read as equally verified to a Worker slice.

### 11.4 Four measured observations routed forward

```text
M1  ROUTED TO V2b. `game/views.py`'s `except Exception` branch now has TWO structurally
    different causes — a JSON syntax error and a slug/stem defect — and logs the identical
    string `variant_list_omitted` for both, measured. An operator cannot tell them apart
    without reading the `libretiles.variants` logger. V2b already touches the readiness
    path, so it is the right place to give the omit branch a discriminator WITHOUT leaking
    anything into the public payload.
M2  ACCEPTED, NOT ACTIONED. `list_installed_variants` re-globs and re-parses every manifest
    on each of three per-request call sites. The new check adds one `slugify` per manifest,
    which is negligible — but it is the measurement that justifies why the fix went in at
    ingest rather than into `load_variant`.
M3  ROUTED TO V2b as one bounded assertion. LEAD 1 of the report: can a manifest reach
    `_summary_from_payload` (the `FileNotFoundError` → `unavailable` branch) while its stem
    and declared slug diverge? The Worker believes the new ingest check pre-empts it and
    did not construct the case. V2b touches exactly that branch, so it should either prove
    it unreachable or handle it.
M4  RECORDED, NOT ACTIONED. `_variants_dir()` calls `path.mkdir(parents=True,
    exist_ok=True)` at `variant_store.py:174` — a read-shaped helper with a filesystem side
    effect on every catalog list. Latent, unrelated to this whole.
    Also recorded: LEAD 3, a variant that now vanishes rather than showing `unavailable`
    may leave a stale persisted `variant_slug` in the Zustand store. `frontend/src/lib/
    variants.ts` already exposes `reconcileSelectedVariantSlug`, so a repair path probably
    exists — but nobody has measured it against a vanished slug. Routed to V9's
    documentation pass at the latest, earlier if V6 touches the picker.
```

### 11.5 Exchange ledger, updated

```text
session/exchange   slice   phase            files                              outcome
01 / 01            V1      implementation   01_implementation_00.md
                                            01_report_00.md                    PASS 3878847
01 / 02            V1b     implementation   01_implementation_01.md
                                            01_report_01.md                    PASS 61720aa
02 / 01            V4probe preflight        02_probe_00.md
                                            02_interruption_00.md              INTERRUPTED
                   evidence completed by ORCHESTRATOR, non-independent:
                                            90_hungarian-expansion-probe.md
03 / 01            V2a     implementation   03_implementation_00.md
                                            03_report_00.md                    PASS 5f63e0d
--                 --      ORCHESTRATOR-AUTHORED, non-independent                   1f39ff4
```

---

## 12. Slice V2b landed — Worker session 03, exchange 02

```text
21f0a149bd5591bac492d6f024ddd6a46998c0cf   V2b  readiness fails closed on an invalid
                                                lexicon; the filename-slug hazard closed
                                                7 files, +953 −24
```

Pair archived as `03_implementation_01.md` + `03_report_01.md`. `PASS`,
`implementation-PASS`. Gaps **G2 is CLOSED** and the reverse half of `mle-01-F01` is closed.

### 12.1 What I re-verified myself, not accepted from the report

```text
git rev-parse HEAD                       21f0a149bd5591bac492d6f024ddd6a46998c0cf
git ls-remote origin refs/heads/main     21f0a149bd5591bac492d6f024ddd6a46998c0cf  EQUAL
git status --porcelain=v1                empty
git diff --name-status 1f39ff4 HEAD      exactly the seven allowlisted paths:
                                         A validate_lexicons.py · A lexicon_health.py ·
                                         A test_lexicon_health.py · M views.py ·
                                         M variant_store.py · M two test modules
git rev-parse HEAD:.ap                   9c5cc44…  unchanged
grep -c django gamecore/lexicon_health.py    0   — the pure-engine boundary held
pytest --collect-only                    495 tests collected   (466 -> 495, +29 as claimed)
manage.py validate_lexicons              run by me: five assets, 0 failed, exit 0
```

I re-ran the cheap tier through the shipped code path myself. The performance claim — the
whole point of the named risk — holds:

```text
slug     ok    reason  file size     bytes read   fraction
czech    True  ok      54 105 021       65 536    0.12 %
english  True  ok       3 103 812       65 536    2.11 %
polish   True  ok      51 607 141       65 536    0.13 %
slovak   True  ok      45 456 204       65 536    0.14 %
slovak two-tile  True  ok       586          586   100 %  (smaller than the bound)
TOTAL 262 730 B read against 154 272 565 B of shipped lexicon
```

And I re-ran the fail-closed direction against my own synthetic corpus rather than the
Worker's:

```text
empty.txt              ok=False  empty
bom.txt                ok=False  bom
badutf8.txt            ok=False  invalid_utf8
onlycomments.txt       ok=False  no_surviving_word
junk.txt               ok=False  no_surviving_word          (single chars, digits, punctuation)
good.txt               ok=True   ok
crlf_prose_first.txt   ok=True   ok    <- trap T1 + the CRLF finding, in one case
```

The CRLF finding is confirmed independently: `collins2019.txt` line 1 ends `\r\n`, read as
raw bytes. Nothing in the repository documented that, and English is the default variant.

### 12.2 The Worker corrected my prompt again — twice — and both times it was right

```text
W3  MY 5b INSTRUCTION WAS SELF-CONTRADICTORY. It said mirror `fastdict._read_words`
    "exactly" AND apply `len >= 2`. `_read_words` has no length floor; the floor lives at
    game/services.py:216. The Worker implemented the conjunction, said so in the module
    docstring, and added a test asserting the only difference from the real index is the
    single-code-point token. Had it obeyed literally, N6's single-character lexicon would
    have reported `ok` and the slice would have shipped a hole.
    ⛔ Same class as defect 3. This is the FOURTH prompt defect of this whole and the
    second of the "two instructions that cannot both hold" kind.
W4  MY 5c SCOPE WAS TOO NARROW. I named the `except Exception` branch. A `{not json` file
    never reaches it — it is caught at a different site — so a discriminator on that branch
    alone could not have supported the test I demanded. The Worker gave all five omit sites
    a token. That is a wider change than I authorized in words and a smaller one than my own
    required test implied; it disclosed the discrepancy rather than silently picking either
    reading, which is the correct behaviour.
```

⚠ **My rules R-A/R-B/R-C from section 11.2 did not prevent W3.** R-B says prohibitions get
written last and read against the obligations in one pass — but W3 was not a
prohibition-versus-obligation clash, it was **two obligations in the same paragraph that
disagree**. Added:

```text
R-D  When a prompt says "mirror X exactly" AND adds a condition, that is two obligations,
     not one. Either say "mirror X and additionally apply Y, and here is why Y is not in X",
     or do not say "exactly". I now grep my own drafts for the words `exactly`, `identical`
     and `mirror` and check each one against the sentence that follows it.
```

### 12.3 Six measured observations, and where each goes

```text
M5  ROUTED TO V9 DOCUMENTATION, and worth stating loudly: the hazard was PUBLIC, not
    internal. Pre-change, `De_Ch.json` reached GET /api/game/variants/ and read
    `readiness: playable`. My section 2 framed it through list_installed_variants and the
    three validation sites only. The Worker's T14 pre-change capture shows the public row.
    The blast radius of mle-01-F01 was one step wider than I wrote, and the ledger entry
    must say so.
M6  ACCEPTED, PINNED BY TEST. collins2019.txt is CRLF. Confirmed by me from raw bytes. Any
    future rule using rstrip("\n"), splitlines(keepends=True) or a byte comparison breaks
    ENGLISH ONLY — the default variant. N9 now pins the shape.
M7  ROUTED TO V3. The Collins header is self-certifying: it claims 279 496 words and the
    audit counted exactly 279 496. That is a free integrity oracle and nothing compares
    them. V3's build scripts are the natural place to make a declared count and a measured
    count agree, for every language.
M8  RECORDED. `_variants_dir()` calls mkdir on every list — a read-shaped helper with a
    filesystem side effect. Latent; not this whole.
M9  RECORDED. `test_dictionary_validation.py:61` holds a fourth, ad-hoc copy of the line
    filter that drops the `isalpha` step. Correct for what it asserts. The repository now
    has one canonical filter (`lexicon_health.surviving_word`) plus that reimplementation.
    A future consolidation slice, not this one.
M10 ACCEPTED WITH A BOUND. The audit's exact duplicate count costs ~500 MB peak RSS on
    czech.txt because it materializes a set of 3 930 497 tokens, and it now runs inside the
    pytest process. Acceptable at current sizes. ⛔ It will NOT be acceptable for Hungarian:
    the probe measured ~301 million forms at the tightest board bound, so a set-based
    duplicate count would need ~40 GB. V4' must therefore audit Hungarian by a streaming
    or sorted-adjacency method, never by a set. Recorded now so it is designed in, not
    discovered.
```

### 12.4 One decision I am taking now, from the Worker's smallest-next-step

Its closing question: should `readiness: unavailable` also make a variant **unselectable**
at `game/serializers.py:180`, `:215` and `game/services.py:173`? Today readiness is advisory
to the client while those three sites accept any *installed* slug.

**Decision: YES, and it is routed to V5b, not to a slice of its own.** Reasoning: it is
currently unreachable in practice — all four shipped variants are `playable`, and an
unloadable manifest is already omitted from the list those sites read. It becomes reachable
exactly when a variant is installed-but-not-ready, and the first such variant in this
project's history is **Hungarian under the local-build model** of section 10.3. So the fix
belongs in the slice that creates the condition, where it can be tested against a real
`unavailable` variant instead of a synthetic one.

⚠ Carried as an open obligation so it cannot be lost: **V5b must make an `unavailable`
variant unselectable at all three sites, and must prove that a fresh clone cannot create a
Hungarian game before the local lexicon build has run.** Without that, a player on a fresh
clone could start a Hungarian game against an absent dictionary.

### 12.5 Closure conditions amended

```text
NEW 17  An `unavailable` variant is unselectable at game/serializers.py:180, :215 and
        game/services.py:173, proved against a real `unavailable` variant rather than a
        synthetic one.
NEW 18  The Hungarian lexicon audit uses a streaming or sorted-adjacency duplicate check,
        never an in-memory set, because ~301 million forms would need roughly 40 GB.
```

Condition 2 of section 7 is now **satisfied**: readiness fails closed, still on exactly two
values, and proved by T13 through the real HTTP endpoint. Condition 1 was satisfied at
`3878847`. Condition 5's synthetic-corrupt half is satisfied by N1-N6 and T13.

### 12.6 Exchange ledger, updated

```text
session/exchange   slice   phase            files                              outcome
01 / 01            V1      implementation   01_implementation_00.md
                                            01_report_00.md                    PASS 3878847
01 / 02            V1b     implementation   01_implementation_01.md
                                            01_report_01.md                    PASS 61720aa
02 / 01            V4probe preflight        02_probe_00.md
                                            02_interruption_00.md              INTERRUPTED
                   evidence completed by ORCHESTRATOR, non-independent:
                                            90_hungarian-expansion-probe.md
03 / 01            V2a     implementation   03_implementation_00.md
                                            03_report_00.md                    PASS 5f63e0d
--                 --      ORCHESTRATOR-AUTHORED, non-independent                   1f39ff4
03 / 02            V2b     implementation   03_implementation_01.md
                                            03_report_01.md                    PASS 21f0a14
```

New exact baseline for every subsequent slice: **`21f0a149bd5591bac492d6f024ddd6a46998c0cf`**.
Next fresh Worker session ordinal: **04** (slice V3).





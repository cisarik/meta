# Decision record — logical whole `13/00 multilingual-expansion-campaign`

Artifact class: **Orchestrator decision record. Evidence, not authority.** Written and
owned by the Orchestrator of this whole. It grants no mutation authority.

Opened 2026-09-03 at repository `ad4ce038e1bd3511bdd5b7431eb9c163d4788130`.

```text
Prior logical whole identity: multilingual-expansion
Logical whole identity: multilingual-expansion-campaign
Meta directory: /home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/
Precedence chain: 11/01 · 11/02  ->  12/00  ->  13/00 (this whole)
```

Governing objective: the Cooperator's verbatim text, `00_handout.md` section 2. Not
paraphrased here, deliberately.

---

## 1. Section index

```text
2   Stage 1 — my own measurements, 2026-09-03
3   The handout's section 3 re-verified: every SEMANTIC claim holds, every LINE
    NUMBER but one is stale. Measured replacements.
4   New measurements the chain does not contain
5   Decisions taken under the autonomy grant
6   The exchange plan
7   Prompt-defect discipline carried in from 12/00
8   Running exchange log
```

---

## 2. Stage 1 — my own measurements, 2026-09-03

Route: `12/00/91_orchestrator-handout.md` section 2, run by me, read-only. No repository
mutation. Every value below is my own observation in this session, not a copied one.

### 2.1 Repository identity

```text
git rev-parse HEAD                    ad4ce038e1bd3511bdd5b7431eb9c163d4788130   MATCH
git rev-parse HEAD:.ap                9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap rev-parse HEAD             9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   MATCH
git -C .ap status -sb                 ## HEAD (no branch)   -> detached, CORRECT topology
git status -sb                        ## main...origin/main                       MATCH
git status --porcelain=v1             EMPTY                                       MATCH
git ls-remote origin refs/heads/main  ad4ce038e1bd3511bdd5b7431eb9c163d4788130   MATCH
HEAD author/date                      Michal Cisárik, 2026-09-03 18:56:22 +0200
backend/assets/variants/              czech.json english.json polish.json slovak.json
backend/assets/dicts/                 TEN files, sowpods.txt (1 743 531 B) still present
backend/scripts/                      build_{czech,polish,slovak}_lexicon.py
ss -tlnp :3000 :8000                  NO LISTENER  -> safe to run npm run build
```

### 2.2 The one difference, and its recovery class

```text
Meta repo HEAD   expected by 12/00/91 capsule   742b5eb5d96fe73d7a35cbac63899389c7da0221
                 measured                        54c844a9194754df5d4370a03a9b7f21149d98de
                 public readback                 54c844a...  == local HEAD, pushed, clean
                 the two intervening commits
                     1f22615  docs(12/00): continuation handout for a fresh Orchestrator at ad4ce03
                     54c844a  docs: supersede 11/01, 11/02 and 12/00; open 13/00 ...
```

Classified against all five canonical classes (`AP.md:1464-1508`):

```text
unexplained-divergence   NO. Both commits are accounted for by name and content: they are
                         the 12/00 Orchestrator's own two closing acts, and the second is
                         the commit that created the file I was handed.
unrelated-owner-work     NO. Neither commit touches the product repository.
stale-clone              NO. Local HEAD equals the public readback exactly.
unpublished-candidate    NO. Nothing local is unpushed; porcelain is empty.
accepted-continuation    YES — and it is the correct class.
```

⚠ The `12/00/91` capsule was written at `742b5eb` and therefore could not name its own
two later commits. `13/00/00_handout.md`'s capsule says only `Meta repo /home/agile/meta,
pushed` with no SHA, which is consistent with the measured state. **No material remainder.
Stage 1 PASSES.** The product repository is byte-identical to the handed-over baseline.

### 2.3 All eight standing gates, plus the two extras

Route: the corrected `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/…` form.
⛔ `manage.py check` takes no `-m`; I did not use one.

```text
mypy config game gamecore accounts catalog   Success: no issues found in 85 source files
ruff check .                                 All checks passed!
manage.py check                              System check identified no issues (0 silenced).
pytest                                       538 passed, 4 skipped in 242.04s (0:04:02)
pytest --collect-only                        542 tests collected in 6.75s
manage.py validate_lexicons                  5 asset(s) audited, 0 failed   exit 0
npm run typecheck                            exit 0
npx vitest run                               450 passed | 3 skipped   (31 passed | 1 skipped of 32 files)
npm run lint                                 exit 0
npm run build                                exit 0
```

`npm run build` route table, counted by me:

```text
ƒ /   ƒ /_not-found   ƒ /api/ai/judge   ƒ /api/ai/move   ƒ /api/models   ƒ /api/prompts
ƒ /draw/[id]   ƒ /game/[id]   ƒ /play   ƒ /settings   ƒ /waiting/[id]
=> ELEVEN dynamic route rows, ZERO static (○) rows.  MATCH
```

`validate_lexicons` detail, which is also the ledger's dictionary-status evidence:

```text
czech    words=3930497  duplicates=0  non_nfc=0   ok
english  words=279496   duplicates=0  non_nfc=0   ok
polish   words=3721704  duplicates=0  non_nfc=0   ok
slovak   words=3005250  duplicates=0  non_nfc=0   ok
slovak two_tile  words=103  duplicates=0  non_nfc=0  ok
```

⚠ The pytest wall time is 242.04 s against the recorded 238.52 s. That is machine noise on
an identical count, not a regression: `538 passed, 4 skipped` and `542 collected` both
match exactly.

### 2.4 The twenty-second reproduction re-proof

```text
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python scripts/build_slovak_lexicon.py \
    --check --check-dir /tmp/opencode/mec-13-00/sk
```

```text
expander       hunspell 1.7.3 confirmed
               "@(#) International Ispell Version 3.2.06 (but really Hunspell 1.7.3)"
upstream       raw.githubusercontent.com/LibreOffice/dictionaries@75f5dff8c972fff4a32e4ea8434722c277f02a3f
               sk_SK.dic     3 362 212 B  3e3dbd5c6af8431a3a47652c69692f3f86d0cd82deb4418e49a057a33ef56063
               sk_SK.aff       225 271 B  af67bbe8ea9dea74968ec01acd266b3f74177ca087ee6eb7898c576e0aef7a3d
               LICENSE.txt      67 574 B  dc06f891b13dcb6fe1ede36c0c9020f0e57e6777aca951ecaceefa95a19d7cfc
               README_en.txt     2 027 B  a36af75654ae6e65614f7821b2c401ea1f3b4adfdcba9b59efcb1a06c96df14d
expansion      unmunch exit=0, raw 135 109 277 B, unique_words=3005250
reproduced     slovak.txt      3 005 250 lines / 45 456 204 B
CHECK slovak.txt      edca5453c7766cfcd4c0a0b3b7e53abaeb0d640cc541b628dbaab497ff8f0a5d  IDENTICAL
CHECK slovak.LICENSE  f3ad399bbebd143a7f2ccc95af2799813a6b9312426a8038230ce34bef483837  IDENTICAL
CHECK all artifacts identical                                                            exit 0
```

The central claim of era 12 — a committed lexicon is reproducible byte-for-byte from a
pinned upstream by a committed script — **holds under my own re-run**, and it wrote
nothing under `backend/assets/`. Porcelain re-confirmed EMPTY afterwards.

⛔ **Evidence posture: NON-INDEPENDENT.** Every measurement in section 2 is mine as
Orchestrator. It is direct observation, which is stronger than a claim, but it is not
independent acceptance and must never be presented as such.

---

## 3. The handout's section 3 re-verified

`00_handout.md` section 3 says: *"Verify each yourself; a number you did not count is not
a measurement."* I did. **Result: every semantic claim holds. Almost every line number is
stale.**

### 3.1 Semantic claims — all confirmed

```text
CONFIRMED  MAX_TILE_TOKEN_CODEPOINTS = 16                     variant_store.py:22
CONFIRMED  TileToken = str, len() is a resource bound only     types.py
CONFIRMED  canonicalize_tile_token: trim -> NFC -> upper -> NFC   :176-185
CONFIRMED  alphabet_order REQUIRED and DECLARED, never derived    :437-441
CONFIRMED  the SUBSET invariant runs ONE direction only, tiles ⊆ alphabet,
           error code `tile_not_in_alphabet`                      :484-492
CONFIRMED  total_tiles DERIVED from the letter rows, not a manifest field   :104-106
CONFIRMED  forbidden_token_sequences is a declared manifest field      :91, :321-335, :446-450
CONFIRMED  playable_letters comes from the TILE SET ordered by alphabet index   :124-135
CONFIRMED  lexical_contribution() and tile_display() exist and are IDENTITY   :137-143
CONFIRMED  WordAuthority.normalize is per-instance, default _nfc_casefold   word_authority.py:66
CONFIRMED  variant_name EXISTS and feeds display_label      variant_store.py:82, :108-112
CONFIRMED  VariantLetter is exactly (letter, count, points)   :37-41
CONFIRMED  blank_targets is ABSENT.  git grep -n  -> 0 hits.  git grep -in -> 0 hits.
           Both patterns run, per rule R-E.
```

Manifest measurements, parsed by me from the four shipped JSON files:

```text
             letter rows   total tiles   blanks   alphabet_order   alphabet letters with NO tile
english.json      27           100         2           26          (none)
slovak.json       42           100         2           46          DZ  DŽ  CH  Q  W      (5)
czech.json        40           100         2           42          CH  Q  W              (3)
polish.json       33           100         2           32          (none)
multi-code-point tile tokens declared by any shipped manifest:  NONE
variant_name declared by any shipped manifest:                  NONE
lexicon_provenance present in all four:                         YES, seven keys each
```

⇒ The handout's Slovak and Czech counts are exactly right, and its point stands: requiring
the reverse subset direction would fail on shipped Slovak. Polish and English have no
tile-less alphabet letters at all.

### 3.2 ⛔ THE LINE NUMBERS ARE STALE — measured replacements

`variant_store.py` is **545 lines** at `ad4ce03`. The handout's references are offset by
roughly ninety lines, consistent with the provenance and `slug_stem_mismatch` code that
`a3ed00f` and `5f63e0d` inserted. Only one of its references survives.

```text
                              handout says   MEASURED at ad4ce03
MAX_TILE_TOKEN_CODEPOINTS         :22            :22            ✔ the only correct one
canonicalize_tile_token           :147           :176-185       ✘
total_tiles derived               :75-77         :104-106       ✘
playable_letters                  :95-106        :124-135       ✘
lexical_contribution/tile_display :108-114       :137-143       ✘  (:108-112 is display_label)
forbidden_token_sequences         :292           :91 · :321-335 · :446-450   ✘
alphabet_order required           :338-343       :437-441       ✘
SUBSET invariant                  :380-388       :484-492       ✘
letters sorted by token           :393           :497           ✘
```

⛔ **Consequence, and it is a live prompt hazard.** This is defect class D1 — a value
copied from a handout without being run. A Worker prompt that quotes the handout's line
numbers would send a Worker to the wrong code. **Never copy a `file:line` from any handout
into a prompt. Re-measure it in the session that writes the prompt.** The semantic content
of the handout's section 3 is reliable; its coordinates are not.

### 3.3 The three server validation sites — inherited condition 17 re-confirmed open

Measured by reading all three:

```text
backend/game/serializers.py  CreateGameSerializer.validate_variant_slug
    installed = {variant.slug for variant in list_installed_variants()}
backend/game/serializers.py  QueueJoinSerializer.validate_variant_slug
    installed = {variant.slug for variant in list_installed_variants()}
backend/game/services.py     _unknown_variant_payload
    installed = {item.slug for item in list_installed_variants()}
```

All three test **installed-ness only**. None consults readiness. So an `unavailable`
variant is selectable today, exactly as inherited condition 17 states. The condition is
OPEN and my own reading confirms it rather than inheriting it.

The public payload is built at `backend/game/views.py:156-165` and keeps exactly
`slug · display_name · language_code · readiness`, with `readiness` typed
`Literal["playable", "unavailable"]` at `:46`. Two values, as required.

---

## 4. New measurements the chain does not contain

These are mine, first recorded here.

### 4.1 `collins2019.txt` is a headed CRLF file with no trailing newline

```text
wc -l                       279497
line 1                      "Collins Scrabble Words (2019). 279,496 words. Words only."
line 2                      empty
line ending                 CRLF throughout
final line                  "ZZZS" with NO trailing newline
reconciliation              279497 newlines + 1 unterminated final line = 279498 physical
                            lines; minus the header and the blank line = 279496 WORDS
```

⇒ **279 496 agrees three independent ways**: the asset's own header line, the
`validate_lexicons` audit, and `english.json`'s `lexicon_provenance.entry_count`. That is
the number the PRD must carry, and it is now evidenced rather than asserted.

### 4.2 The D6 grep asymmetry reproduces exactly

```text
git grep -n  "sowpods"   ->  0 hits
git grep -in "sowpods"   ->  5 hits, all in libretiles_PRD.md, all uppercase
    :35   English tile distribution (100 tiles, SOWPODS dictionary with 172,823 words).
    :65   Tier 1: Local SOWPODS dictionary (in-memory frozenset, O(1) lookup).
    :66   Tier 2: Online dictionary API for words not in SOWPODS (optional, SOWPODS is comprehensive).
    :127  SOWPODS dictionary lookup: O(1) via frozenset.
    :150  Online dictionary API (Tier 2) may not be needed if SOWPODS is sufficient.
sowpods.txt   wc -l 172872   -> the PRD's 172,823 matches NEITHER file in the tree
```

### 4.3 `PRIMARY_DICTIONARY_FILE` — the full consumer set

```text
backend/config/settings.py:375   PRIMARY_DICTIONARY_PATH = DICTS_DIR / os.getenv("PRIMARY_DICTIONARY_FILE", "collins2019.txt")
backend/tests/test_dictionary_validation.py:16   _PRIMARY_DICT = settings.PRIMARY_DICTIONARY_PATH
backend/tests/test_gamecore.py:275, :286, :287   load_dictionary / load_prefix_index
backend/.env.example                             ABSENT — confirmed undocumented
```

⇒ Four consumers, all internal, two of them tests. The prior Orchestrator's
recommendation — document rather than remove — is correct, and `.env.example`'s existing
house style already has the exact pattern for it: a commented explanation plus a
commented-out assignment, as used for `DJANGO_THROTTLE_CACHE_URL` and `DJANGO_NUM_PROXIES`.

### 4.4 Hungarian is already partly pre-staged in the frontend

```text
frontend/public/   cs.png  en.png  hu.png  pl.png  sk.png   -> FIVE flags, hu.png ALREADY PRESENT
frontend/src/lib/i18n/locales.ts:1   export const LOCALES = ["en", "sk", "cs", "pl"] as const;
frontend/src/lib/i18n/           messages.{en,sk,cs,pl}.ts   -> FOUR catalogs
frontend/src/lib/i18n/i18n.test.ts:956-961   INSTALLED_VARIANTS = english slovak czech polish
plural helpers                   pluralEn · pluralSk · pluralCs (= pluralSk, deliberately) · pluralPl
```

⇒ `hu.png` exists with no `hu` locale. B1's UI half inherits an asset, not a gap. Recorded
so nobody re-creates it.

### 4.5 Blank identity is a hardcoded literal, not a field

Relevant to C2 and to the multi-realization idea the handout tells me to leave unbuilt:

```text
variant_store.py:24-26   _BLANK_ALIASES = {"BLANK","WILDCARD","WILD","JOKER","BLANKTILE","⁇"}
variant_store.py:134     tiles = [lt.letter for lt in self.letters if lt.letter != "?"]
variant_store.py:154     if token == "?": return (0, 0)
variant_store.py:188-198 normalise_letter maps blank synonyms to "?"
variant_store.py:274-278 a manifest may not declare a blank ALIAS as a tile token
```

⇒ `"?"` is a literal in at least four places. C2 must restrict the derived target set
without touching that literal, or it becomes an engine refactor rather than a data field.

---

## 5. Decisions taken under the autonomy grant

The grant (`12/00/91` section 11) is: work autonomously, do not interrupt, and where a
question would be asked, use the recommended answer. These are recorded so a successor can
falsify them.

```text
D13-1  Stage 1 is PASS and the baseline is ad4ce03. The Meta-HEAD difference is
       accepted-continuation with no material remainder. No probe needed.
D13-2  The first Worker exchange is the deferred documentation chain, NOT a language.
       Reason: the handout sequences it first, it is the cheapest possible re-entry, it
       unblocks the sowpods deletion, and it was owed before this campaign existed.
D13-3  V9a and V9b are delivered in ONE exchange as TWO commits. Both are
       documentation-only, neither deletes anything, and "prefer fewer, larger grants" is
       the measured lesson of 12/00's two dispatch failures. R-F is respected because the
       DELETION (V3d) is a LATER exchange, not this one.
D13-4  V9b is DOCUMENT, not remove. Four consumers exist, two are tests, and .env.example
       already has the house pattern for an optional knob. This adopts the prior
       Orchestrator's recommendation, which the Cooperator did not override.
D13-5  V9a stays FIVE LINES. libretiles_PRD.md is stale in wider ways I measured — FR-01 is
       titled "Game Core (English Variant)" while four variants ship, and Known Gaps still
       says "Human vs human multiplayer deferred to v2" while multiplayer is live. Those
       belong to campaign closure condition 11, not to a slice whose purpose is to unblock
       a deletion. Recorded in section 8 so they are not lost.
D13-6  No handout line number is ever copied into a prompt. See section 3.2.
D13-7  The ledger is seeded from measurement with UNKNOWN stated as UNKNOWN. I will not
       write a candidate tile distribution or a candidate lexicon licence into the ledger
       from memory. Standing condition 5 makes an unclear licence a DISQUALIFICATION, and a
       plausible-looking unsourced row is exactly the failure mode closure condition 4
       exists to prevent. Sourcing is a bounded read-only exchange of its own.
```

---

## 6. The exchange plan

```text
01/01  V9a + V9b   documentation chain. libretiles_PRD.md five SOWPODS lines -> Collins 2019;
                   backend/.env.example documents PRIMARY_DICTIONARY_FILE. Two commits.
                   Tier E1. Reasoning Medium. Subagent Worker, bounded, non-independent.
next   V3d         git rm backend/assets/dicts/sowpods.txt + a test asserting absence, with
                   the THIRD clause: enumerate every env-var-resolved asset path and state
                   whether the deployed value was confirmed or accepted as unknown.
                   A SEPARATE exchange from 01/01, per R-F.
then   SOURCING    a bounded read-only sourcing probe that fills the ledger's `distribution
                   source` and `dictionary status` columns for the twenty unshipped rows.
                   This is the campaign's real critical path and it is evidence work, not
                   implementation. It must precede B2.
then   B2          af · ms first — the cheapest languages — then it · nl. Proves "adding a
                   language is boring" on real data before the one E3 slice.
then   C1 -> B1    planner Worker, fresh implementation session, fresh independent
                   acceptance that is NOT my subagent.
then   C3 -> B3 · C2 -> B5 · C1's dividend -> B4 and B6 · B7
```

Ordering constraint that never bends: a batch never precedes its capability.

---

## 7. Prompt-defect discipline carried in from 12/00

R-A through R-F are adopted verbatim from `00_handout.md` section 7. Two additions of my
own, both earned in this session:

```text
R-G  NEVER copy a `file:line` from a handout, notes file, or prior prompt. Re-measure it in
     the session that writes the prompt. MEASURED: eight of nine line references in
     13/00/00_handout.md section 3 are stale at the very commit it was written against.
R-H  When a document states a count, reconcile it against the artifact by construction
     before repeating it. MEASURED: collins2019.txt's 279 497 `wc -l` is not its word count;
     the file carries a header line, a blank line, CRLF endings and no final newline, and
     the true count 279 496 only appears once all four are accounted for.
```

Mechanical habits, both mandatory:

```text
python3 /home/agile/meta/projects/libretiles/apfieldcheck.py <prompt.md>   exit 0, EVERY prompt
⛔ NEVER build a prompt by string-patching the previous one.
```

---

## 8. Running exchange log

```text
2026-09-03  Stage 1 run by the Orchestrator. PASS. Baseline ad4ce03 confirmed against the
            public readback. All eight gates green. Reproduction re-proved byte-exact.
2026-09-03  90_language_ledger.md seeded: 24 rows, 9 columns, 4 shipped rows measured.
2026-09-03  91_deferred-acceptance-batch.md opened. It was owed by 12/00 and is now started
            rather than reconstructed at the end.
2026-09-03  Exchange 01/01 issued: V9a + V9b. Subagent Worker, bounded, non-independent.
2026-09-03  Exchange 01/01 returned implementation-PASS at a199d0e. ACCEPTED by the
            Orchestrator after independent re-measurement of every gate. See section 9.
2026-09-03  COOPERATOR deleted backend/assets/dicts/sowpods.txt himself at 4f6f38d and pushed.
            Classified accepted-continuation. V3d's mutation half done by owner action.
            See section 10.
2026-09-03  Exchange 02/01 (MEC-V3d-guard) returned implementation-PASS at 86ec39e. P14 and
            P15 landed. ACCEPTED after independent re-measurement. See section 11.
```

### 8.1 Carried forward, not lost

```text
PRD staleness beyond SOWPODS, for closure condition 11:
    :33  FR-01 is titled "Game Core (English Variant)" — four variants ship
    :149 Known Gaps says "Human vs human multiplayer deferred to v2" — multiplayer is LIVE
    the PRD does not mention variants, locales, lexicon provenance, or readiness at all
G4 · G6 · G7 · G8 from 12/00/briefing.md remain open. G6 is DECIDED: no third readiness
    state. G7 (font glyph coverage) becomes live at B6 — Greek and Cyrillic.
LOCK 11 holds: no change to any provider list, constant, tier, model tuple, or provider
    documentation anywhere, pending its own logical whole.
The do-not-deploy stands. audit-04-F01 / orch-05-D14 becomes reachable behind nginx.
```

---

## 9. Exchange 01/01 — V9a + V9b. Outcome, verification, and my own defect

```text
prompt        01_implementation_00.md          task MEC-V9ab, tier E1, reasoning Medium
report        01_report_00.md                  status PASS, implementation-PASS
baseline      ad4ce038e1bd3511bdd5b7431eb9c163d4788130
end commit    a199d0e4086231a5f39853cbca0a94e7c734a37a
commits       4904e29  docs(prd): Collins 2019 replaces the stale SOWPODS references
              a199d0e  docs(env): document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override
delivery      subagent, Meta path as delivery only, no other Meta file readable
evidence      ⛔ NON-INDEPENDENT. A subagent is bounded delegation, never independent
              acceptance, and this result must never be described as independent.
```

### 9.1 What I verified myself rather than accepted

A report is a claim. I re-measured every load-bearing one at `a199d0e`:

```text
git rev-parse HEAD            a199d0e4086231a5f39853cbca0a94e7c734a37a
git ls-remote origin main     a199d0e4086231a5f39853cbca0a94e7c734a37a       EQUAL
git status --porcelain=v1     EMPTY
… -- backend/assets/          EMPTY
git rev-parse HEAD:.ap        9c5cc44  == git -C .ap rev-parse HEAD          unchanged
sowpods.txt                   PRESENT, 1 743 531 B, mtime unchanged
git diff --stat ad4ce03..a199d0e   3 files, +89 −5, exactly the three allowlisted paths
full diff read line by line   five PRD lines changed and no others; the new text is
                              byte-identical to what the prompt specified; the .env.example
                              block is the specified twelve lines with the variable commented
                              out; the test module reads the MANIFEST and asserts nothing
                              about sowpods.txt

git grep -in "sowpods" -- libretiles_PRD.md                          0
git grep -n  "sowpods" -- .                                          2   both in the guard test
git grep -in "sowpods" -- .                                          3   all in the guard test
git grep -in "sowpods" -- . ':!backend/tests/test_documentation_dictionary_claims.py'   0

mypy                          Success: no issues found in 85 source files
ruff check .                  All checks passed!
manage.py check               System check identified no issues (0 silenced).
pytest                        540 passed, 4 skipped in 245.07s        538 + 2
pytest --collect-only         544 tests collected                     542 + 2
validate_lexicons             5 asset(s) audited, 0 failed            exit 0
npm run typecheck             exit 0
npx vitest run                450 passed | 3 skipped (31 passed | 1 skipped of 32)  IDENTICAL
npm run lint                  exit 0
npm run build                 exit 0, ELEVEN dynamic route rows, ZERO static
new module alone              2 passed in 0.01s
```

**Every gate the Worker reported, I reproduced.** No claim in that report failed
verification. Standing conditions 1, 6, 7 and 8 hold at `a199d0e`; conditions 2-4 are not
engaged by a documentation slice; condition 5 is not engaged because no lexicon was added.

⇒ **Result accepted: implementation-PASS at `a199d0e`. Logical-whole closure: not-closed.**

### 9.2 🐞 PROMPT DEFECT E1-D1 — mine, caught by the Worker

```text
DEFECT   My section 5 asserted: "ASCII only. The file has no non-ASCII byte and no emoji;
         match it."
TRUTH    backend/.env.example carries THREE pre-existing U+2014 EM DASHes, at lines 2, 12
         and 45. I confirmed all three myself with `LC_ALL=C grep -n '[^ -~\t]'`.
CLASS    D1 — a premise stated as measured that was never measured. Identical in kind to the
         era-12 `-m manage.py check` defect, and it is the FIRST prompt defect of this era.
HARM     none. The Worker obeyed the operative half — its appended block is pure ASCII — and
         left the three existing em-dashes untouched under the "beyond appending the one
         block" prohibition. The instruction happened to be harmless because its operative
         clause and its false premise pointed the same way.
WHY IT   I inferred "the file is ASCII" from having read it rendered, where an em dash looks
HAPPENED like punctuation rather than like a non-ASCII byte. Reading is not measuring.
RULE     R-I (new): a claim about a file's ENCODING or BYTE CONTENT must come from a byte-level
         command, never from having read the file. `LC_ALL=C grep -n '[^ -~\t]' <file>` costs
         one second. This joins R-G (never copy a file:line from a handout) and R-H (reconcile
         a count against the artifact by construction) as the three rules this era added.
```

⚠ **Note what worked.** The `WHAT YOU CAN STILL SEE … MEASURED or LEAD` report field caught
this on the very first exchange of the era, exactly as it caught five of six in era 12.
It stays in every prompt.

### 9.3 The Worker's findings, dispositioned

```text
MEASURED 1  .env.example is not ASCII-only.        -> ACCEPTED as defect E1-D1, section 9.2.
MEASURED 2  the tree-wide `sowpods` grep is now 3 / 2, all inside the guard test, and the
            unreferenced premise now needs the PATH-EXCLUDING form:
              git grep -in "sowpods" -- . ':!backend/tests/test_documentation_dictionary_claims.py'
            -> VERIFIED BY ME, returns 0. ⛔ This exact command goes into the V3d prompt.
            It is a genuinely good catch: a bare tree-wide grep returning 3 would read as
            "still referenced" and would block the deletion for the wrong reason.
MEASURED 3  NO gate anywhere would notice a PRIMARY_DICTIONARY_FILE override. validate_lexicons
            and test_lexicon_provenance both audit the MANIFEST path, so an override changes
            what submit_move validates against while every asset gate stays green.
            -> ACCEPTED and it SHARPENS my own framing: I wrote "invisible to both", which
            understates it. Routed to V3d's third clause, which must state whether the
            deployed value was confirmed or accepted as unknown. Not a new defect ticket:
            it is the already-recorded mle-01-F02, now better characterized.
MEASURED 4  PRD :33 "Game Core (English Variant)" still implies English is the only variant.
            -> Already in section 8.1 as a closure-condition-11 item. Confirmed, not new.
LEAD 5      README.md and docs/ might carry the same stale dictionary name or 172,823.
            -> ⛔ CLOSED BY MY OWN MEASUREMENT, and the answer is NO:
                 git grep -n "172,823"        1 hit, and it is the guard test's own docstring
                                              quoting the history. Nowhere else in the tree.
                 README.md                    already says "Collins 2019" in ELEVEN places
                                              (:11 :22 :136 :208 :222 :224 :240 :283 :348
                                              :368 :395) and SOWPODS in none.
                 docs/architecture.md         already says Collins 2019 in NINE places and
                                              SOWPODS in none.
            ⇒ libretiles_PRD.md was the ONLY stale dictionary surface in the repository.
              Closure condition 11's dictionary half is now satisfied for README and docs.
LEAD 6      D2's needle is a bare formatted number and would accept an unrelated 279,496.
            -> ACCEPTED as a bounded limitation, not a defect. Tightening it would couple the
            guard to prose wording. Recorded; no action.
LEAD 7      the PRD is stale enough that FR-10 could be misread as current.
            -> Routed to closure condition 11. No action in this campaign until then.
```

### 9.4 What this exchange changed about the campaign

```text
V9a  CLOSED at 4904e29.  V9b  CLOSED at a199d0e.
V3d  UNBLOCKED. Its prompt is now writable, and it inherits two required clauses:
       1  the path-excluding grep from MEASURED 2, not a bare tree-wide one
       2  the third clause: enumerate every env-var-resolved asset path and state whether the
          deployed value was CONFIRMED or ACCEPTED AS UNKNOWN. PRIMARY_DICTIONARY_FILE is the
          only such path measured so far, and MEASURED 3 is why the clause is necessary.
R-F  respected: the exchange that established the asset is unreferenced is NOT the exchange
     that deletes it.
The English ledger row's two recorded debts are discharged.
```

---

## 10. Owner commit `4f6f38d` — the deletion done by the Cooperator himself

On 2026-09-03 20:57 the Cooperator wrote *"sowpods.txt vymazane, pokracujeme"* and had
already performed the deletion himself.

```text
4f6f38d  chore(dicts): remove obsolete SOWPODS dictionary file
         Michal Cisárik <michal@cisarik.info>   2026-09-03 20:57:20 +0200
         backend/assets/dicts/sowpods.txt | 172872 deletions
         1 file changed, 172872 deletions(-)      ONE path, nothing else
         pushed; git ls-remote == git rev-parse HEAD == 4f6f38d
```

⚠ **The instruction was ambiguous — "vymazane" could mean "it has been deleted" or "delete
it" — and I resolved it by MEASURING rather than by asking.** The repository answered in one
command. That is the right resolution for an ambiguous one-word instruction whose truth is
observable, and it is cheaper than a round trip.

### 10.1 Recovery classification, all five classes

```text
unexplained-divergence  NO. The commit is explained three ways: the Cooperator announced it,
                        the message states exactly what it does, and the diff is one path.
unrelated-owner-work    NO — and this is the interesting one. It IS owner work, but it is not
                        UNRELATED: it performs V3d, which was the next planned slice of this
                        campaign. Naming it `unrelated` would misfile it.
stale-clone             NO. Local HEAD equals the public readback.
unpublished-candidate   NO. Pushed, porcelain empty.
accepted-continuation   YES. The baseline advanced by owner work that implements planned
                        campaign work, is published, and leaves no material remainder.
```

⛔ **A Cooperator commit to `main` is not a defect and is not something to undo.** It is his
repository. The Orchestrator's job is to classify it, verify the product still holds, and
adjust the plan — not to re-do it or to complain that it bypassed a slice.

### 10.2 What I verified before accepting the new baseline

```text
diff                    one path, 172 872 deletions, nothing else                    ✔
mypy                    Success: no issues found in 85 source files                  ✔
ruff                    All checks passed!                                           ✔
manage.py check         System check identified no issues (0 silenced).              ✔
pytest                  540 passed, 4 skipped in 242.54s        unchanged from a199d0e ✔
pytest --collect-only   544 tests collected                     unchanged             ✔
validate_lexicons       5 asset(s) audited, 0 failed            STILL FIVE            ✔
83 dictionary-related tests (validation, documentation, provenance, health)  all pass  ✔
git grep -in sowpods    3 hits, ALL inside the guard test; excluding it: 0            ✔
blob survives at        bd2d63f (Initial commit)  ->  revert restores it byte-for-byte ✔
```

### 10.3 ⛔ The V3d third clause is now SATISFIED, and by direct evidence

V3d's inherited condition was: *"enumerate every env-var-resolved asset path and state
whether the deployed value was confirmed or accepted as unknown."* There is exactly one such
path, `PRIMARY_DICTIONARY_FILE`, and the hazard was that an operator `.env` might name the
file being deleted. I resolved it **without reading `backend/.env`**:

```text
backend/.env                                     PRESENT on this host (existence only)
resolved PRIMARY_DICTIONARY_PATH exists on disk  True
resolved basename == collins2019.txt             True
manage.py check                                  clean
tests/test_dictionary_validation.py              passes
```

⇒ **CONFIRMED, not accepted-as-unknown, for this deployment.** A boolean plus a comparison
against the known default is enough evidence, and it never printed the contents of a file the
security boundary forbids. For any other deployment the value remains unknown by
construction, which is precisely why exchange 01/01 documented the knob.

⚠ **One improvement in failure mode worth recording.** Before the deletion, an operator
`.env` naming `sowpods.txt` would have made Django silently validate moves against a
172 872-word list while every asset gate reported `english ok words=279496`. Now the file does
not exist, so the same misconfiguration fails loudly at dictionary load instead of silently.
The deletion did not only remove dead weight; it converted a silent failure into a loud one.

---

## 11. Exchange 02/01 — MEC-V3d-guard. P14 and P15

```text
prompt        02_implementation_00.md          task MEC-V3d-guard, tier E2, reasoning Medium
report        02_report_00.md                  status PASS, implementation-PASS
baseline      4f6f38d09ec3c0b1cc671b7df752b3f713b52506
end commit    86ec39e08cfe28caa2919279a6123b0814e6032d
commit        86ec39e  test(lexicons): no unclaimed file may sit in the shipped dictionary directory
routing       fresh-worker-session, session ordinal 02, exchange 01
evidence      ⛔ NON-INDEPENDENT. Bounded subagent delegation, never independent acceptance.
```

⚠ **Why session 02 and not session 01 exchange 02.** The baseline moved by owner work between
the two exchanges, and the previous session's retained context contained the belief
*"`sowpods.txt` is present, by decision, and must not be deleted"* — true when it was written,
false afterwards. Retained context that CONTRADICTS the current task is a hazard rather than a
convenience, which is exactly AP's changed-external-state trigger for fresh routing. Fresh
session, exchange reset to `01`, per `PROMPT_CONTRACTS.md:493-495`.

### 11.1 What landed

```text
P14  backend/assets/dicts/sowpods.txt does not exist. The named absence era 12 deferred, with
     its original identifier preserved so the archive and the code agree.
P15  ⛔ ONE DIRECTION: every FILE PRESENT under backend/assets/dicts/ must be CLAIMED by a
     manifest through dictionary_file, two_tile_words_file, or lexicon_provenance.license_file.
     NOT the reverse — a claimed-but-ABSENT file must pass, because Hungarian's gitignored
     lexicon will legitimately be claimed and absent until a local build runs, and fail-closed
     readiness owns that case.
     NO exemption list. An exemption list is where the next orphan hides.
     Claim set gathered by RAW JSON SCAN, deliberately not through list_installed_variants(),
     which swallows load failures and would misattribute a broken manifest's legitimate assets
     as orphans.
```

This is the durable generalization of the sowpods defect, installed **before** roughly twenty
lexicons and twenty licence files arrive rather than after.

### 11.2 What I verified myself

```text
git rev-parse HEAD           86ec39e08cfe28caa2919279a6123b0814e6032d
git ls-remote origin main    86ec39e08cfe28caa2919279a6123b0814e6032d          EQUAL
porcelain / assets porcelain EMPTY / EMPTY
.ap gitlink == submodule     9c5cc44                                          unchanged
git diff --numstat           97 insertions, ZERO deletions  ->  P1-P13 provably untouched
proof scaffolding remaining  grep for zzproof / monkeypatch.setitem  ->  0 hits
new symbols at               :481 :482 :485 :518 :528     module 462 -> 559 lines
P14 + P15 alone              2 passed, 45 deselected
ruff / mypy / manage.py check   clean / 85 files / 0 issues
pytest                       542 passed, 4 skipped in 245.77s          540 + 2
pytest --collect-only        546 tests collected                       544 + 2
validate_lexicons            5 asset(s) audited, 0 failed              STILL FIVE
npm typecheck / lint         exit 0 / exit 0
npx vitest run               450 passed | 3 skipped (31 passed | 1 skipped of 32)  IDENTICAL
npm run build                exit 0, ELEVEN dynamic rows, ZERO static
```

**Every claim reproduced. Result accepted: implementation-PASS at `86ec39e`.**

⚠ The Worker's most valuable act was procedural: it proved P14 and P15 have teeth by
monkeypatching the module's directory globals to `tmp_path`, rather than briefly creating a
file under `backend/assets/`. It also proved the TOLERANT direction explicitly — a
claimed-but-absent file does not fail P15 — which is the assertion that protects the Hungarian
slice, and it is proof by execution rather than by comment.

### 11.3 The Worker's findings, dispositioned

```text
MEASURED 1  frontend/public/ has ELEVEN files and SIX with ZERO references:
              hu.png · file.svg · globe.svg · next.svg · vercel.svg · window.svg
            referenced: en.png sk.png cs.png pl.png (2 each) · drevo.jpeg (1)
            -> ⛔ VERIFIED BY ME, count for count. This is the same defect shape as sowpods:
               an asset in the tree that nothing claims. FIVE are Next.js scaffolding
               leftovers. hu.png is NOT — it is a flag for a language with no manifest, no
               lexicon and no entry in the flag map, and I had already recorded its existence
               in section 4.4 without recognizing it as an ORPHAN. The Worker's framing is
               better than mine.
               ROUTED: its own bounded exchange, before twenty flags arrive. It needs a
               product decision I will take under the autonomy grant — delete the five
               scaffolding files, and let hu.png be CLAIMED by the Hungarian slice rather than
               deleted, because deleting and re-adding an identical asset is churn.
MEASURED 2  backend/assets/premiums.json and backend/assets/diagnostics/{2 files} are claimed
            only by CODE, not by a manifest, and have no mechanical invariant.
            -> VERIFIED BY ME: those are exactly the three files outside dicts/ and variants/.
               No orphan there today. Recorded as a known gap; NOT worth an invariant now,
               because the campaign adds nothing to either directory. Revisit only if it does.
MEASURED 3  the variants/ side is ALREADY guarded: test_variant_invariants.py G1 fails on an
            empty variant list and G9 fails when the manifest file count and the loaded count
            disagree, with G9c proving G9 can fail.
            -> VERIFIED BY ME at test_variant_invariants.py:174 and :184. ⇒ IMPORTANT AND
               REASSURING for the campaign: twenty new manifests enrol themselves in P1-P13
               and G1-G25 automatically the moment they land, and a broken manifest cannot
               silently shrink the parametrized matrix. This lowers the cost of every future
               language row.
MEASURED 4  P15 would pass vacuously on an empty dicts/ directory; no non-emptiness assertion
            was added. -> ACCEPTED as a recorded decision, not an oversight. P2 and P4 read
               shipped lexicons by path and validate_lexicons audits five assets, so an empty
               directory fails loudly several tests earlier. No action.
MEASURED 5  P15 compares exact basenames, so a manifest writing "dicts/czech.txt" would report
            czech.txt as an orphan. -> ACCEPTED as correct fail-closed behaviour; P2 already
               enforces basename-only for license_file, and the failure message says so.
LEAD 1      hu.png may have been added as part of a planned flag batch, so a
            "present ⇒ referenced" invariant over frontend/public/ could block future flags.
            -> ⚠ ADOPTED AS A CONSTRAINT ON THE NEXT EXCHANGE. Whatever invariant is written
               there must be one-directional in the same sense as P15, or it will fight the
               campaign. This is the second time in two exchanges that DIRECTION was the
               load-bearing design decision.
LEAD 2      a SUBDIRECTORY under dicts/ is invisible to P15 (`if p.is_file()`).
            -> ACCEPTED as a bounded limitation. No planned language needs a multi-file
               bundle; every shipped lexicon is a flat .txt plus a .LICENSE. Recorded so a
               future bundle format is a deliberate decision.
LEAD 3      the .gitignore rule for the Hungarian output is unverified and should be pinned in
            the SAME slice that adds the build script.
            -> ADOPTED into B1's condition set. It joins inherited conditions 11, 15, 16, 18.
```

---

## 13. ⛔ COOPERATOR DECISION — routing policy changed 2026-09-03

Verbatim:

> *Na trivialne ulohy nepotrebujes Workerov, si Agent Orchestrator a mas write pristup mozes
> taketo easy ulohy priamo urobit ty bez toho aby sa inicializoval fresh Worker, studoval si
> cely AP protokol a na koniec testoval vsetko a pisal dalsie testy.. vela vela vela
> zbytocnych tokenov. Chceme uderny vyvoj*

**He is right, and the waste was mine.** Measured cost of the first two exchanges: each spawned
a fresh Worker that read `AP.md` (145 KB), `AP_WORKER.md`, `AGENTS.md` and a 400-line prompt,
ran the full four-minute suite, and then **I re-ran all eight gates again myself** — duplicate
verification producing zero additional information on a five-line documentation edit.

RF-01 assigns cost/irreversibility trade-offs and protocol design to the Cooperator, so this
is his decision to make and it is now the standing policy:

```text
D13-8  ORCHESTRATOR-DIRECT for trivial and low-risk work. E0-E2, small allowlist, no runtime
       semantics change. I edit, run PROPORTIONATE gates, commit, push. No Worker, no prompt
       file, no duplicate verification.
D13-9  GATES PROPORTIONATE TO BLAST RADIUS. Deleting unreferenced frontend assets does not
       need a four-minute Django suite. Touching backend runtime or an asset gets the full
       eight. A batch boundary always gets the full eight.
D13-10 WORKERS RESERVED for genuinely large slices and for the one thing that cannot be
       delegated away.
```

⚠ **The one thing this does NOT change, and protecting it is my job.** C1 — multi-code-point
tiles end to end, wire schema 4, the seven F2b guards — is **E3**. It requires FRESH
INDEPENDENT ACCEPTANCE from a session that did not implement it, and that session **cannot be
my subagent** (`AP.md:1395-1405`). That is an independence requirement, not a cost question,
and no autonomy or efficiency grant reaches it. It is exactly ONE slice in this whole campaign.
Everything else is now mine to execute directly.

⚠ Also unchanged: when I do the work, the evidence is NON-INDEPENDENT by construction. That
costs one line to record and I will keep recording it.

---

## 14. Directly executed — `frontend/public/` orphans, `7a3899d`

No Worker. R-E double grep across the whole tree for all six candidates, plus CSS `url()` and
Next's icon/manifest conventions. Then `git rm` five files, four frontend gates, one commit.

```text
DELETED   file.svg  globe.svg  next.svg  vercel.svg  window.svg
          create-next-app leftovers. -n=0 and -in=0 for every one of them, tree-wide.
KEPT      hu.png, and the reason is a MEASUREMENT rather than a preference:
          frontend/src/app/settings/page.tsx:375 builds `/${value}.png` over LOCALES, so the
          locale flags are referenced BY TEMPLATE, not by literal. hu.png becomes referenced
          the moment "hu" enters LOCALES. Deleting and re-adding an identical file is churn.
          ⇒ AND IT KILLS THE PROPOSED INVARIANT: a literal-grep "present ⇒ referenced" rule
            over frontend/public/ would flag every flag as an orphan. The Worker's LEAD 1 was
            right for a better reason than it knew. NO invariant was written there, on purpose.
GATES     typecheck 0 · vitest 450 passed | 3 skipped · lint 0 · build 0, 11 dynamic, 0 static
          Backend suite NOT run: the diff is five frontend image files. Proportionate, per D13-9.
```

---

## 15. ⭐ AFRIKAANS IS THE FIFTH PLAYABLE VARIANT — `153ead7`, directly executed

The handout said: run B2 first, and *"if B2 is not boring, that is the most valuable finding
available and it is far cheaper to learn there than inside C1."* **B2 was not boring, and the
finding is worth more than the language.**

### 15.1 The two source questions, answered by measurement

```text
DISTRIBUTION   ⛔ MY OWN LEDGER WAS WRONG. I recorded `UNSOURCED` for twenty rows. MEASURED:
               slovak.json, czech.json AND polish.json all declare
                   source_url = https://en.wikipedia.org/wiki/Scrabble_letter_distributions
               The national authorities (JÚĽŠ SAV, ÚJČ, RJP, MTA) sourced `alphabet_order`,
               NOT the distribution. The distribution source was already precedented, and its
               "Official editions" section contains ALL TWENTY-FOUR target languages.
LEXICON        MEASURED against LibreOffice/dictionaries at the SAME pinned commit the three
               shipped scripts use: 62 language directories, and a .dic/.aff pair exists for
               22 of the 24 targets.
               ⛔ TWO DO NOT EXIST:
                 FINNISH  no fi_FI. LibreOffice routes Finnish through Voikko, a separate
                          morphological analyzer, not a plain affix pair.
                 MALAY    no ms_MY. `id` (Indonesian) exists and MUST NOT be substituted.
               ⚠ tr_TR's .dic is 36 MB — an order of magnitude above the rest, and Turkish is
                 agglutinative. Expect Hungarian's problem; measure before scheduling.
                 es ships 23 country variants and de ships 3 — C5 made concrete.
```

⇒ **The campaign is much more tractable than this ledger opened with.** The critical path is
per-language table extraction and per-language LICENCE READING, not searching for sources.

### 15.2 What Afrikaans actually needed, and it was not "nothing"

```text
MEASURED   148 601 unique expanded forms, of which 4 614 (3.10%) carry a non a-z letter:
           ë 2753 · ê 910 · ï 533 · é 155 · ö 81 · ô 75 · á 56 · ó 56 · è 34 · and ten more.
           The Afrikaans edition bears PLAIN LATIN TILES and ignores diacritics.
           ⇒ Without a diacritic rule, `môre`, `aangelê` and `reël` are in the lexicon and
             UNPLAYABLE, and MORE / AANGELE / REEL are rejected. That is not a cosmetic gap;
             it fails the Cooperator's own bar of "correctly playable".
DECISION   Fold at BUILD time, in the lexicon. 148 267 words, ZERO non a-z remaining.
           Zero engine change, zero capability, zero manifest field.
BOUNDARY   ⛔ Legitimate ONLY when the fold is TOTAL for the edition — every folded letter
           absent from the tile set. WRONG for Slovak (A≠Á, both tiles), Czech, and German
           (Ä≠A even though ß→SS). Those still need C3. The script says this at length so the
           technique is not copied by resemblance.
```

⚠ **A falsified inference of my own, recorded rather than quietly fixed.** My ledger said
Afrikaans needed `capability required: none INFERRED`. Measurement falsified the reasoning — it
DOES need a diacritic rule — and the rule then turned out to be expressible in the asset rather
than the engine. Right conclusion, wrong reasoning. That is why `INFERRED` cells are labelled.

### 15.3 The honest measure of "how boring is a language"

```text
AUTOMATIC   ~25 parametrized cases enrolled with NO new test file. 542 -> 567 passed,
            546 -> 571 collected. validate_lexicons 5 -> 6 assets, 0 failed.
            The generic harness, P1-P15 and G1-G25 all picked the variant up from its manifest.
DELIBERATE  FOUR hardcoded inventories, all in tests, ZERO in production code:
              1  _LEXICON_PROBES  G14 probe row  (includes the FOLDED witness `more`)
              2  P10b             build-script inventory
              3  test_t7          exact public catalog order — english pins first, then
                                  casefolded display_name, so "Afrikaans" INSERTS at index 1
              4  P13              its hardcoded "three scripts" defeated the point of deriving
                                  _SCRIPT_CLAIMS. Generalized: it owns DRIFT, P10b owns the
                                  inventory. One claim, one owner.
UI          degrades gracefully, measured: VARIANT_NAME_KEYS / VARIANT_FLAG_SRC have no
            afrikaans entry, variantDisplayName() falls back to the server display_name, and
            flagSrc is omitted when absent. The backend slice ships alone with no UI defect.
```

⇒ **Adding a language is data-only, and the friction is four test inventories.** That is the
claim the Cooperator's objective asked for, now proved on real data rather than asserted.

### 15.4 Evidence

```text
--check     CHECK afrikaans.txt      6454dc83f91c0afbb9d6ad32873800b8360233d93703324ece8a5b062bfe97ff  IDENTICAL
            CHECK afrikaans.LICENSE  ecdb27ce1605edaccb178fde985958df018d42dd66f7e4ccb4e0d22febf067aa  IDENTICAL
            CHECK all artifacts identical, exit 0
gates       ruff · mypy 85 files · manage.py check · pytest 567 passed 4 skipped ·
            collect-only 571 · validate_lexicons 6 assets 0 failed · typecheck 0 ·
            vitest 450 passed 3 skipped · lint 0 · build 0 with ELEVEN dynamic ZERO static
cond. 1     MOVE CORE hash c7acc270… and version pfr-s2-core-1 UNCHANGED — prompts.ts and
            prompts.test.ts were never touched. en/sk/cs/pl all still playable, four keys.
posture     ⛔ NON-INDEPENDENT. Orchestrator-direct execution under decision D13-8.
```

---

## 17. Italian and Dutch — sixth and seventh playable variants, `dab6d0d`

Directly executed, no Worker, one commit. Both licences read BEFORE anything was built, per
standing condition 5.

```text
ITALIAN   120 tiles · 21 tile kinds · the 21-LETTER Italian alphabet, exact equality both
          directions — the first shipped variant with no letter lacking a tile and no tile
          outside the alphabet. GPL-3.0-only. 3 128 429 words / 46.7 MB.
          Diacritic fold, same sourced rule as Afrikaans: 34 114 of 3 135 500 forms (1.09%)
          carry ò é à ì è ù ç â ô, and without folding CITTA, PERCHE, SARA, PIU are unplayable.
          ⚠ Its licence gate quotes upstream's own typo — "The extensione is released…" —
          VERBATIM. A tidied quotation would fail on a correct file. R-H in practice.
DUTCH     102 tiles · 26 tile kinds · full Latin alphabet, exact equality.
          ⭐ FIRST DUAL LICENCE: BSD-3-Clause OR CC-BY-3.0, OpenTaal, "at the discretion of the
          user". The gate asserts THREE strings — the availability grant plus each named option
          — because one sentence cannot prove a dual licence, and if upstream drops an option
          the build fails rather than the manifest over-claiming. 1 293 086 words / 16.5 MB.
```

### 17.1 ⛔ The find of the batch: NFD does not decompose a ligature

```text
MEASURED   upstream nl_NL spells 125 444 of 1 294 152 forms with U+0133, the IJ LIGATURE ĳ.
           A diacritic fold ALONE leaves 121 891 words unreachable, because a ligature is a
           COMPATIBILITY mapping, not base + combining mark — NFD walks straight past it.
PROOF      verified ABSENT from the raw expansion and PRESENT after the rewrite:
               ijs · dijk · ijzer · vrijheid
           Without rule 1 the Dutch words for ice, dike, iron and freedom cannot be played
           at all. That is not a 3% tail like Afrikaans; it is four everyday words.
RULE       the modern Dutch edition dropped its IJ tile in March 1998 and spells the sound with
           an I tile plus a J tile, so the build rewrites ĳ -> ij, THEN folds diacritics.
           Rule order matters: rule 1 first keeps each rule's effect independently observable,
           which is what makes a three-category word gate meaningful.
⛔ EXPLICIT TABLE, NOT NFKD. NFKD would also rewrite unrelated compatibility characters, and an
   aggressive normalizer on a shipped word list is how a silent corruption enters. The mapping
   states the edition rule and nothing else.
GATE       six required words in THREE categories (plain · ligature witness · fold witness),
           one forbidden control word, a non-zero ligature-input assertion, AND a character
           scan proving no finished word still contains U+0133. A count or size check cannot
           see a partially applied mapping.
```

### 17.2 ⚠ C2 WAS SCOPED WRONG, and three shipped languages prove it

The handout specified C2 as *"a manifest field that RESTRICTS the derived set"*. Measured:

```text
Afrikaans  a blank MAY represent X and Z — neither has a tile   (source citation-needed)
Italian    a blank MAY represent J K W X Y — none has a tile    (source stated)
Turkish    a blank may NOT represent Q W X                      (a restriction, as scoped)
```

⇒ **C2 must be an EXPLICIT declared set** able to name alphabet letters that have no tile, not
a filter over the derived set. Absent still means "derive from the tile set", which keeps every
shipped variant byte-unchanged. Not a blocker: all three ship today with derived targets and
lose only the blank-as-absent-letter play.

### 17.3 The pattern, now measured three times

**Three of three "no capability needed" languages needed a TILE-FACE RULE** — a rewrite from
upstream orthography to the faces the edition actually prints. All three were expressible in the
**asset**, at build time, with zero engine change. That works only when the rewrite is TOTAL for
the edition. German (Ä stays while ß→SS), Slovak (A≠Á) and Czech cannot use it, so **C3 is still
required** and is still the highest-leverage capability left.

### 17.4 Evidence

```text
--check    italian.txt      03bc29a56b62d8d31a0feee60615b138fddd6933d5cf7914cb16a00b7acabaaf  IDENTICAL
           italian.LICENSE  8c82930583eb0f5490699fbb0fd9185e5c85c4368c068e97ff9c330c2061423f  IDENTICAL
           dutch.txt        99d8ed478cca2781343807e611b9e213ce5e6d29832ca71941bc5192f1215baa  IDENTICAL
           dutch.LICENSE    84bda1db98255d058fa445d28aabd85e6222f46fc3fb1875819a0650c09e1e9d  IDENTICAL
gates      ruff · mypy 85 files · manage.py check · pytest 617 passed 4 skipped ·
           collect-only 621 · validate_lexicons EIGHT assets 0 failed · typecheck 0 ·
           vitest 450 passed 3 skipped · lint 0 · build 0, ELEVEN dynamic ZERO static
arithmetic verified independently of the loader: italian 120 tiles / 21 kinds / 21 alphabet;
           dutch 102 tiles / 26 kinds / 26 alphabet; zero tiles outside the alphabet and zero
           alphabet letters without a tile, for both
friction   the SAME four test inventories as Afrikaans. pytest 567 -> 617, ~50 cases enrolled
           automatically from the two manifests. ZERO production-code changes.
posture    ⛔ NON-INDEPENDENT. Orchestrator-direct under D13-8.
```

### 17.5 Recorded debt

```text
SIX build scripts now share ~350 near-identical lines. The 12/00 handout already flagged a
shared backend/scripts/_lexicon_build.py at three copies. ⛔ NOT done now, deliberately:
  · the shared interface should be designed from the REAL variation, and Dutch's two-rule
    pipeline plus Italian's typo-quoting licence gate are exactly the variation to design from
  · each script is a standalone host tool by design — `spec_from_file_location` in
    test_lexicon_provenance.py does NOT put backend/scripts/ on sys.path, so a shared import
    would break P9's import-safety test and need a sys.path hack in every script
  · the refactor is verifiable: `--check` on all six proves byte-identity, so it is a safe
    slice — just not one that should precede more languages
TRIGGER: extract it before the tenth language, or when a rule must change in more than two
scripts at once.
```

---

## 19. German playable, French blocked, and C3 has largely evaporated — `0deac4a`

### 19.1 ⛔ C3's SCOPE COLLAPSED, and it is a measurement, not an opinion

C3 — variant-declared normalization — was the capability I called *"clearly the highest-leverage
capability left … it unlocks seven languages."* Then I measured what those seven actually need:

```text
German     'ß'.casefold() == 'ss'   ⇒ Python implements Unicode FULL case folding, and every
                                      build script already casefolds. NOTHING TO BUILD.
                                      Ä Ö Ü are TILES, so they need PRESERVING, not folding —
                                      a PARTIAL asset rule, no engine change.
Greek      'ς'.casefold() == 'σ'    ⇒ final sigma is ALREADY unified by the default. Its
                                      accented vowels need a total fold — an asset rule.
French     total fold + œ/æ ligature rewrite   ⇒ asset rules, both proven shapes.
da sv no   Æ Ø Å / Å Ä Ö are TILES  ⇒ partial fold at most, the German shape. Asset rule.
Icelandic  Þ Ð Æ Ö and accented vowels are all TILES ⇒ possibly no rule at all.
Turkish    ⛔ THE ONE GENUINE CASE. MEASURED:
               'İ'.casefold() -> 'i' + U+0307, TWO code points, and NFC does not recompose
               that sequence has isalpha() == False
               ⇒ `_filter_words`'s `word.isalpha()` filter would SILENTLY DROP every Turkish
                 word containing İ, and the board token İ would never match the lexicon.
```

⇒ **C3 is a Turkish problem, not a seven-language problem.** Every other language on that list
is a build-time asset rule of a shape already shipped three times. That is a large reduction in
remaining engine work, and it was invisible until each language was measured individually.

⚠ **What C3 must therefore actually be**, when Turkish arrives: not "a manifest field selecting a
normalizer" in the abstract, but specifically **a normalization that does not casefold İ into a
mark sequence, and a word-shape filter that does not require `isalpha()` of a combining mark.**
Narrower, sharper, and cheaper than the original framing.

### 19.2 German — the partial fold, and a rule that needed no code

```text
102 tiles · 29 kinds = A-Z + Ä(6) Ü(6) Ö(8) · no ß tile · 709 844 words · 10.1 MB
LICENCE  GPL-2.0-only OR GPL-3.0-only. Upstream grants "Version 2 oder 3" — a choice between
         exactly those two, so NOT -or-later, which would grant a version nobody wrote.
FIRST ISO8859-1 UPSTREAM. de_DE_frami.aff declares SET ISO8859-1, so unmunch emits latin-1 and
         the README is latin-1 too. The generalized first-SET-directive assertion caught it.
         ⇒ The Czech script's encoding comment warned "that difference becomes mojibake in the
           NEXT language". German was that next language, and the warning paid off exactly once,
           which is all a warning has to do.
THE PARTIAL FOLD  223 of 709 883 forms (0.031%) carry é ñ á ç ê à â è — loanwords, no tiles.
         155 641 words KEEP an umlaut. A total fold would have rewritten all 155 641 while every
         count-based gate stayed green. The rule is per-character: keep a marked letter that has
         a tile, fold one that does not. The build asserts a NON-ZERO umlaut count and carries
         two preservation witnesses in its six-word gate.
ENGINE CONSTRAINT FOUND: `canonicalize_tile_token('ß')` returns 'SS' because `'ß'.upper()` is
         'SS', so `_parse_asset_token` rejects a declared 'ß' as `noncanonical`. ß therefore
         CANNOT appear in a manifest at all. Harmless here — the edition has no ß tile — but a
         real constraint for any future variant that wants one.
QUALITY  unmunch expands affixes, not COMPOUNDING, and German Scrabble leans on compounds.
         `fussball` is measurably absent. Same limitation as every shipped lexicon; it bites
         German hardest. Recorded, not hidden.
```

### 19.3 ⛔ French is BLOCKED, and it is a new blocker class

Licence and distribution are both fine — MPL-2.0 Grammalecte 7.0, 102 tiles sourced. **The
expander is the blocker.**

```text
fr.dic declares 84 172 stems; unmunch emits 1 470 363 lines
  only 80 312 are plain alphabetic
  1 168 520 lines are UNEXPANDED FLAG DATA: `yotta/S.|A`, `Allemagne0/L'D'Q'|`
  apostrophes appear 5 603 572 times — French elision prefixes, correctly excluded for Scrabble
⇒ playable output ~77 000 words. The official French lexicon (ODS) is of the order of 400 000.
```

**A French variant whose dictionary rejects most valid French words is a defect that looks like
a feature, so French is not shipped.** `fr.aff` uses `FLAG long`, and the Hungarian probe already
established that Spylls 0.1.7 resolves affix structures the C `unmunch` cannot. **French joins
Hungarian on the Spylls route.** Its transformation rules are already measured and waiting:
total fold plus `œ→oe` / `æ→ae`, plus a shape filter to drop 470 superscript/Greek artifacts.

⇒ **This is the third distinct blocker class in the campaign, and naming them separately matters:**

```text
NO SOURCE        Finnish (no plain affix pair — Voikko) · Malay (no ms_MY)
EXPANDER FAILS   French (unmunch cannot render FLAG long inflections)
SIZE             Hungarian (~301 M forms) — and Turkish is the next candidate, 36 MB upstream
```

### 19.4 Evidence

```text
--check  german.txt      f4df51be4c52e2aec794ed2bfc6ff842779da5db184f49c3db872aae449a51b5  IDENTICAL
         german.LICENSE  f4fde505134ad3a2840835d3c15d80c5e55f2310144d48bc3833be056a590b32  IDENTICAL
gates    ruff · mypy 85 · manage.py check · pytest 642 passed 4 skipped · collect-only 646 ·
         validate_lexicons NINE assets 0 failed · typecheck 0 · vitest 450 passed 3 skipped ·
         lint 0 · build 0, ELEVEN dynamic ZERO static
arithmetic  102 tiles / 29 kinds / 29 alphabet, zero either way
friction    three test inventories (P13 is now generic). pytest 617 -> 642. Zero engine changes.
posture     ⛔ NON-INDEPENDENT. Orchestrator-direct under D13-8.
```

---

## 21. Portuguese — ninth variant, and the row that PROVED something — `1eed5ed`

This row was scheduled for one reason and it delivered it.

```text
⭐ 120 TILES WITH THREE BLANKS LOADS, AUDITS AND PLAYS WITH ZERO CODE CHANGE.
   `total_tiles` is a property summed from the letter rows (not a manifest field), and the blank
   is just another letter row, so a bag that is neither 100 tiles nor 2 blanks needed nothing.
   The campaign handout ASSERTED this. It is now MEASURED.
```

```text
24 tile kinds including a Ç tile worth 3 points · alphabet_order 27, so K W Y are Portuguese
letters with NO tile (official only since 2009) — the same shape as Slovak's five
4 119 831 words / 63 137 733 B — the LARGEST asset in the repository, above czech.txt's 54 MB
```

### 21.1 The sharpest witness written in this campaign

```text
`coraçao`, from `coração`:
    a TOTAL fold spells it `coracao`   -> gate fails
    a MISSING fold leaves `coração`    -> gate fails
    only the correct PARTIAL rule yields `coraçao`
ONE word, BOTH failure modes. It is in the build post-condition and in the G14 probe.
```

Sourced rule: *"While Ç is a separate tile, other diacritical marks are ignored."* Measured:
í 602 934 · á 505 997 · ã 108 132 · ó 61 062 · é 45 255 · ê 26 672 · õ 21 575 · ú 15 492 ·
â 12 321 · ô · î · à all fold; **137 997 words keep their cedilla**.

### 21.2 ⛔ Two upstream files disagree about the licence

```text
README_pt_PT.txt   "All dictionary files and associated programs are currently covered by the
                    (GPL/LGPL/MPL), by this order." + "1. GPL Version 2  2. LGPL Version 2.1
                    3. MPL Version 1.1"
LICENSES.txt       under "Spellchecker", different authors, NO versions:
                    "covered by the GPL and BSD licence"
```

Claimed: `GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1`. The README is the **specific, versioned**
statement about the exact artifact this build consumes, **and** it is the same expression the
shipped Slovak lexicon already declares — so the claim is consistent with the house rather than
invented for this row. ⛔ **BSD is deliberately not claimed**, because only the vaguer file
mentions it. Both documents ship in full inside `portuguese.LICENSE`, so the conflict is visible
to a reader instead of resolved silently.

⚠ That is what standing condition 5 looks like applied honestly: not "the licence is unclear, so
disqualify", and not "one file says BSD, so claim BSD". Claim the precise grant, name the
conflict, ship the evidence.

### 21.3 First mixed-encoding upstream

`pt_PT.aff` and `LICENSES.txt` are UTF-8; `README_pt_PT.txt` is **ISO8859-1 and raises** on a
UTF-8 read (byte 0xE9, the é of "José"). German's whole pack was latin-1 — this one is mixed, so
encodings are now named **per file** rather than once per script.

### 21.4 Evidence

```text
--check  portuguese.txt      dadd466d207b641df420b3dd94864e58266044e32c9a72212daaea35a7453af4  IDENTICAL
         portuguese.LICENSE  573b813504a35225ae4f22d1565f6acabc5b3b50c59eb0c72b6e3f105bb3dcb2  IDENTICAL
gates    ruff · mypy 85 · manage.py check · pytest 667 passed 4 skipped · collect-only 671 ·
         validate_lexicons TEN assets 0 failed · typecheck 0 · vitest 450 passed 3 skipped ·
         lint 0 · build 0, ELEVEN dynamic ZERO static
friction three test inventories. pytest 642 -> 667. Zero engine changes.
posture  ⛔ NON-INDEPENDENT. Orchestrator-direct under D13-8.
```

---

## 22. Campaign state after ten languages

```text
PLAYABLE 10 / 24  english · slovak · czech · polish · afrikaans · italian · dutch · german ·
                  portuguese · danish
UI       4 / 24   en sk cs pl.  The other six degrade gracefully: no VARIANT_NAME_KEYS entry
                  means variantDisplayName() falls back to the server display_name, and flagSrc
                  is omitted. MEASURED, not assumed.
ASSETS   ELEVEN lexicon assets audited, 0 failed. portuguese.txt at 63 MB is the largest.
ENGINE   ⛔ STILL ZERO ENGINE CHANGES ACROSS SIX NEW LANGUAGES. Every rule any of them needed
         was expressible in the ASSET at build time. The friction is three test inventories per
         language plus one build script.
```

### 22.1 The tile-face rule taxonomy

```text
NO RULE            slovak · czech · polish   accented letters ARE tiles, nothing to do
TOTAL FOLD         afrikaans · italian       no marked letter has a tile
TOTAL + LIGATURE   dutch                     ĳ -> ij, because NFD walks past a ligature
PARTIAL FOLD       german (ä ö ü kept) · portuguese (ç kept) · danish (æ ø å kept)
SHAPE FILTER       danish   þ and ð are distinct LETTERS, so no fold removes them and no tile
                            bears them -> 106 forms DROPPED under an asserted bound
FREE FROM CASEFOLD german ß -> ss · greek ς -> σ   Unicode full case folding already does it
TOOL DEFECT        danish   unmunch truncates a long line mid-character; 11 undecodable lines
                            are skipped, counted and bounded, never absorbed
```

⇒ **Seven distinct shapes, all in data or in the build.** A further language of any of these
shapes is now a mechanical exercise. That is the "adding a variant is boring" claim, earned
rather than asserted — and note that two of the seven were found by a GUARD firing, not by
design: Dutch's ligature by a probe word that was measurably absent, and Danish's truncation by
`errors="strict"` refusing to decode.

### 22.2 Remaining work, ordered by leverage

```text
1  C1 (E3)  unlocks hu · hr · es · el · bg · ru — SIX languages in one slice. Highest leverage
            by a wide margin, and the ONLY slice needing a Worker plus fresh independent
            acceptance that cannot be my subagent.
2  Nordics  da · sv · no · is — partial folds at most, German's shape. Four languages, no
            capability, four build scripts.
3  sl       possibly no capability at all; measure before assuming C1.
4  C3       Turkish only, per 19.1. Narrow: a normalizer that does not casefold İ into a mark
            sequence, and a shape filter that does not require isalpha() of a combining mark.
5  C2       explicit declared blank-target set, per 17.2.
6  Spylls   French and Hungarian both need it.
7  refactor _lexicon_build.py — EIGHT scripts now. The trigger ("before the tenth") is reached.
BLOCKED, recorded, not hidden:  finnish · malay (no source) · french (expander) ·
                                hungarian (size, decision D taken)
```

⚠ **Honest reading of 9 of 24.** Four of the remaining fifteen are blocked on facts outside this
repository. Six are waiting on one E3 slice. Four are mechanical. One needs measuring. That is a
campaign with a visible finish line, not an open-ended one.

---

## 23. Danish playable, Norwegian blocked on licence clarity — `51e08fe`

### 23.1 Danish: strongest licence evidence yet, and three rules

```text
101 tiles · 28 kinds · A-Z without Q, plus Æ Ø Å at 4 points · Q played with a blank
317 167 words / 4.2 MB · GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1
⭐ README_da_DK.txt grants BY FILENAME — "da_DK.dic, da_DK.aff, th_da_DK.dat, th_da_DK.idx …
   These files are published under the following open source licenses: GNU GPL version 2.0 /
   GNU LGPL version 2.1 / Mozilla MPL version 1.1". No directory convention needed.
1  PARTIAL FOLD, Portuguese's shape. 76 196 words keep Æ/Ø/Å; é ü ö á ä ó í è ë fold.
2  SHAPE FILTER, new: þ and ð are distinct LETTERS, so no fold removes them and no Danish tile
   bears them. 106 Faroese/Icelandic proper names DROPPED under an asserted bound rather than
   mangled into something that is not the word.
3  see 23.2 — a tool defect, not a language rule.
⚠ 101 not 100: "Prior to 2025, sets contained 100 tiles and did not include a W."
⚠ Q-by-blank is another C2-EXTENSION case. Recorded, not blocking.
```

### 23.2 ⛔ THE EXPANDER TRUNCATES MID-CHARACTER — and `errors="strict"` is what caught it

```text
MEASURED: of 3 566 551 lines unmunch emits for da_DK, ELEVEN are not valid UTF-8. Every one is
a long `al:` morphological-alias line severed at a buffer boundary, with the LEAD BYTE of `å`
ending one line and its CONTINUATION BYTE opening the next.
```

⛔ **Neither obvious handling is acceptable, and that is the whole point:**

```text
whole-stream errors="strict"    kills the build over 11 lines out of 3.5 million
whole-stream errors="replace"   would let a truncated tail like b"\xa5lsans\xc3\xa6t" become a
                                plausible FAKE WORD, and would absorb real mojibake silently
```

⇒ Each line is decoded **strictly on its own**; an undecodable line is skipped, **counted** and
reported; the count is asserted against a bound of 100. Eleven is tolerated and visible; a
systematic encoding failure fails the build.

⚠ **This retroactively justifies a choice made eight scripts ago.** The `errors="strict"` in
every build script is what surfaced this at all — my own exploratory measurement had used
`errors="replace"` and saw nothing. Danish is the only language where it fired, and it fired
correctly. **A guard that never fires is indistinguishable from no guard until the day it does.**

### 23.3 ⛔ Norwegian: BLOCKED, and it is a FOURTH blocker class

The asset is good — both written standards ship at the pinned commit, nb_NO.dic is 5.3 MB /
334 169 stems. **There is no explicit licence grant for the word list.** I read every file in
`no/`:

```text
COPYING             the unmodified GPL v2 text, NO project statement appended. Its tail is the
                    standard "Yoyodyne, Inc." boilerplate.
README_hyph_NO.txt  says "License: GNU General Public license" — but it is titled "Myspell
                    hyphenation" and names the spell-norwegian hyphenation source. It grants for
                    hyph_nb_NO.dic, NOT for nb_NO.dic.
description.xml     publisher no.speling.org. No licence.
dictionaries.xcu    no licence, no copyright.
nb_NO.aff header    no licence line.
```

⇒ **The one explicit licence statement in the directory is scoped to other files.** Standing
condition 5 makes an unclear licence a disqualification and a recorded blocker, *never a
judgement*. A directory convention is a strong convention, not a grant. Every other language
shipped here has an explicit one: Danish names its files, Swedish says *"This dictionary is made
available subject to"*, Icelandic says *"released into the public domain"*. **Norwegian says
nothing.** So it is recorded, with the missing thing named exactly.

⛔ **And this row establishes a design principle worth more than the language:** the licence
evidence must come from the **same pinned commit as the asset**. Fetching a grant from a Debian
`debian/copyright` or a project website would prove terms for a different artifact than the one
`--check` reproduces. **A pin that covers the words but not the terms is not a pin.**

### 23.4 Reconnaissance done for the two languages NOT shipped this slice

```text
SWEDISH   LGPL-3.0-only, explicit: "This dictionary is made available subject to the terms of
          GNU Lesser General Public License Version 3." Clean, single licence, no "or later".
          100 tiles, 27 kinds; Q and W absent (blank only). Å Ä Ö are tiles.
          823 327 raw forms; 320 311 keep Å/Ä/Ö; only 33 dropped by shape (ł 14, æ 9, ø 9, μ 1
          — Polish and Norwegian proper names).
          ⛔ ONE RULE CORRECTION FOUND AND NOT YET APPLIED: the source says "other diacritics
            like that on É are ignored (EXCEPT Ü)", and "Ü and Æ require a blank … as of 2010
            only one and three playable words respectively". So Ü must NOT fold to U — folding
            would make `müsli` playable as MUSLI, a rule the edition does not have. The correct
            handling is to leave ü unfolded and let the shape filter drop those words, which is
            faithful and costs 124 raw occurrences. My first measurement folded it; that was
            wrong and is corrected here before any script was written.
ICELANDIC 104 tiles (2016 Tinderbox edition under Mattel licence). Ð is a 2-point TILE, and
          Á Í and other accented vowels have their own tiles — so Icelandic may need NO fold at
          all, the first such language since Polish.
          ⚠ MIXED LICENCE, and it needs care: license.txt says the WORDLIST was "released into
            the public domain", but "words in the spell checker with additional morphological
            information are from the Icelandic Wiktionary Project … under CC BY-SA 3.0". The two
            are indistinguishable inside is.dic, so the derived asset must be treated as
            CC-BY-SA-3.0 (share-alike propagates; public-domain material imposes nothing).
            That is determinate, unlike Norwegian's silence — so Icelandic is shippable, with
            license.txt embedded in full.
          Distribution not yet fully extracted; the section is longer than one fetch showed.
```

---

## 25. Swedish and Icelandic — eleventh and twelfth variants — `8a50ded`

### 25.1 Swedish: a carve-out inside a carve-out, and a rule I got wrong first

```text
100 tiles · 27 kinds · 29 alphabet (Q and W have no tile) · 822 919 words
LGPL-3.0-only — the CLEANEST single grant of any language here: one maintainer, one licence,
no "or later", no second document to contradict it.
```

The sourced note has THREE classes, not two:

```text
Å Ä Ö      have tiles           -> KEPT, and they are tile faces
Ü          no tile, NOT ignored -> NOT folded, then DROPPED by the shape filter
É è á ç ć  no tile, ignored     -> FOLDED
```

⛔ **My first measurement folded Ü, and that was wrong.** It would have made `müsli` playable as
MUSLI — a rule the Swedish edition does not have. **No word count, file size or digest could ever
have revealed it.** Caught by reading the source note carefully *before* a line of the script
existed, and now asserted in two places: the build fails if `musli` is present, and the G14 probe
row carries `musli` in its NEGATIVE set — the first probe in this project to use a negative word
that is not the nonsense control.

⚠ That is the pattern worth keeping: **the cheapest place to catch a wrong rule is before the
code exists**, and the second cheapest is an assertion that names the exact artefact the wrong
rule would produce.

### 25.2 Icelandic: ⭐ the first language since Polish with NO rule at all

```text
104 tiles · 32 tile kinds EQUAL to the 32-letter alphabet, BOTH directions — only Italian has
otherwise achieved that · 200 182 words · CC-BY-SA-3.0
```

MEASURED: the ten non-ASCII letters its lexicon uses —
`ð 69 668 · ó 34 348 · á 26 191 · æ 24 749 · ö 23 294 · í 19 912 · ú 13 964 · þ 8 883 ·
ý 6 450 · é 6 108` — and **every one of them is a tile.** A fold would destroy **145 877 playable
words** instead of enabling any. The only filter is by shape: 77 loanwords carrying c/w/z/q.

⛔ **"No rule" is the easiest thing for a later editor to break**, by analogy with the two Nordic
siblings that do fold. So the build and the probe both assert the fold ARTEFACTS are absent —
`madur`, `island`, `fjordur`, `godur` — and all six required words change under a fold. **The
mistake is caught from both directions.**

### 25.3 The licence question ran BOTH ways this slice

```text
NORWEGIAN  silence -> BLOCKED. A directory convention is not a grant.
ICELANDIC  mixed   -> SHIPPED as CC-BY-SA-3.0. The base wordlist is public domain and the
                      morphological additions are CC BY-SA 3.0; the two are indistinguishable
                      inside is.dic, so share-alike propagates.
```

⚠ **Claiming public domain for the whole would have UNDER-stated a real obligation** — the mirror
of over-claiming, and just as wrong. Determinacy, not permissiveness, is what makes a licence
shippable: Icelandic names both components and both versions, Norwegian names neither.

### 25.4 Evidence

```text
--check  swedish.txt        651828f138709520178b55377471d210206eb43da66986699c62ddbb18299a37  IDENTICAL
         swedish.LICENSE    52917a48987b296395c11d3e729cd26706706742a7bb6be3655f121d1cd189ad  IDENTICAL
         icelandic.txt      e074a89969c4193c56f93efd10ff10d55571324ea0edc0d0b3a320cb5e5d3fb1  IDENTICAL
         icelandic.LICENSE  f960f4e10cf58c1cc8476c0ef2fdcad8798a51ca46553152f73f6687f741602f  IDENTICAL
gates    ruff · mypy 85 · manage.py check · pytest 742 passed 4 skipped · collect-only 746 ·
         validate_lexicons THIRTEEN assets 0 failed · typecheck 0 · vitest 450 passed 3 skipped ·
         lint 0 · build 0, ELEVEN dynamic ZERO static
arithmetic  swedish 100/27/29 · icelandic 104/32/32 with zero either way
friction three test inventories. pytest 692 -> 742. Zero engine changes.
posture  ⛔ NON-INDEPENDENT. Orchestrator-direct under D13-8.
```

### 25.5 Twelve of twenty-four — and the tile-face taxonomy is now eight shapes

```text
NO RULE            slovak · czech · polish · ⭐ icelandic   every accented letter IS a tile
TOTAL FOLD         afrikaans · italian                     no marked letter has a tile
TOTAL + LIGATURE   dutch                                   ĳ -> ij; NFD walks past a ligature
PARTIAL FOLD       german (ä ö ü) · portuguese (ç) · danish (æ ø å) · swedish (å ä ö)
FOLD WITH CARVE-OUT swedish   Ü is neither folded NOR a tile face -> dropped
SHAPE FILTER       danish (þ ð) · swedish (ü ł æ ø μ) · icelandic (c w z q) · portuguese-adjacent
FREE FROM CASEFOLD german ß -> ss · greek ς -> σ            Unicode does it already
TOOL DEFECT GUARD  danish 11 truncated lines · all others assert ZERO
```

⇒ **Eight shapes, none of them in the engine.** Twelve languages, zero engine changes, and the
friction per language is exactly one build script plus three test inventories.

---

## 27. C1 reconnaissance done, design resolved — `92_c1_design.md`

⛔ **Decision D13-11: no planner Worker for C1.** Both handouts prescribe one with copy-paste
delivery. I did the reconnaissance myself, read-only, and resolved the design in
`92_c1_design.md`, because AP assigns architecture, risk and sequencing to the Orchestrator and
the wire shape is not a material product decision. **The one thing that cannot be delegated —
fresh independent acceptance from a session that is not my subagent — is unchanged and is the
single thing the Cooperator will be handed.** That is what the planner route was protecting.

### 27.1 The reconnaissance shrank C1 substantially, and five handout claims are stale

```text
S1  "localStorage v4"        MEASURED: the store is ALREADY at version 5, with a migrate chain
                             covering <1 through <5. C1 goes to SIX.
S2  "state_schema_version 4" MEASURED: THE FIELD DOES NOT EXIST. It appears only inside the
                             adapter's own comment text and one test assertion. C1 INTRODUCES it;
                             nothing is bumped. The number 4 is inherited from that text, not
                             chosen — renumbering would falsify an assertion that already ships.
S3  "board/rack/blank/draw
     rendering"              MEASURED: `my_rack: string[]` is ALREADY lossless on the wire, and
                             Board.tsx / Tile.tsx / TileRack.tsx carry NO single-char assumption —
                             every `.length === 1` and `[0]` in Board.tsx is touch handling at
                             :421-:503. ⇒ `board` is the ONLY lossy field.
S4  "seven guards"           SEVEN items, EIGHT code sites: route.ts contributes four
                             (:123 :127 :341 :1002). An "all seven removed" claim must enumerate
                             eight.
S5  "evaluate_scoring_move
     re-pointed"             MEASURED: legality.py:112 ALREADY takes
                             `authority: WordAuthority | None = None`. The seam exists; the work
                             is to PASS one at five call sites.
```

⚠ Five of five are the same defect class as `-m manage.py check` and the stale `variant_store.py`
line numbers: **a value carried forward in prose and never re-measured.** R-G applies to my own
successors reading `92_c1_design.md` too, and it says so.

### 27.2 The six decisions taken

```text
D-1  board: BoardCell[][] — a 15x15 grid, cell = {token, blank_as} | null. A grid because the
     frontend already indexes by coordinate (page.tsx:1212); `null` for empty because storage
     already treats a non-dict cell as empty, so it is the honest wire spelling of what
     persistence means.
D-2  `blanks` is REMOVED, not kept. It is a second source of truth for a fact the cell now
     carries. Consumer to update: Board.tsx:120-121 builds a Set and reads it at :615.
D-3  state_schema_version 4 is a NEW field, and the frontend REFUSES a version it does not
     understand rather than mis-rendering one.
D-4  the client store bumps 5 -> 6 with an explicit `version < 6` branch. The store persists
     PREFERENCES, not game state, so the branch may have nothing to do — and if so it must SAY
     so rather than be omitted, because a silent gap in a migrate chain is how a stale
     preference survives a schema change.
D-5  `_word_passes_dictionary` deletion is a SEPARATE COMMIT from the wire change. Different
     failure modes, so a revert can take one without the other. Five authority call sites, three
     test references.
D-6  ⛔ the PERSISTED board_state shape does not change. Only its projection onto the wire does.
     A stored-row migration is not C1 and would be a far higher tier.
```

### 27.3 Honest note on condition 9

Inherited condition 9 requires the fixture to pass with **two different** multi-character tokens.
⚠ **Twelve shipped languages provide none** — not one has a digraph tile, which is precisely why
they could all ship before C1. So the fixture must use SYNTHETIC tokens (`SZ` plus `DZS` or `LJ`)
plus the L·L canary. Hungarian is the first real consumer and it lands after C1, not with it.
Recording this so nobody reads "two different tokens" as "from a shipped variant".

---

## 28. ⛔ Exchange 03/01 returned BLOCKED with zero mutation, and it was RIGHT

```text
prompt   03_implementation_00.md    task MEC-C1a, tier E3, reasoning High
report   03_report_00.md            status BLOCKED, Phase-qualified result not-applicable
tree     unchanged at 8a50ded. Porcelain empty. No commit, no push, nothing staged.
```

The Worker ran the full gate ladder at baseline, verified every one of my section-3 coordinates
line by line, observed the L·L canary passing pre-change, then stopped on two of my own stopping
conditions. **Four defects in my prompt, and one architectural finding I had missed entirely.**

### 28.1 🐞 PROMPT DEFECT E1-D2 — an absence claim short by two sites

```text
I CLAIMED   seven items, EIGHT code sites, and required proof P-D: "NO SINGLE-CODE-POINT GUARD
            REMAINS ON A LETTER PATH … the eight coordinates"
MEASURED BY ME after the report, at route.ts:329 and :334:
                !/^[\p{L}?]$/u.test(letter)
                letter === "?" && (!blankAs || !/^\p{L}$/u.test(blankAs))
            `^…$` around a single \p{L} matches EXACTLY ONE CODE POINT. Both sit in the SAME
            FUNCTION as site 7.
⛔ CONSEQUENCE  removing site 7 alone is a COMPLETE NO-OP. normalizePlacementData would still
            return null for `SZ`, so the AI could never place a digraph — while all eight gates
            went green and P-D reported a clean absence.
CLASS       D6. The same defect as the case-sensitive sowpods grep: an ABSENCE CLAIM I asserted
            without enumerating its pattern exhaustively. R-E says a pattern must be run both
            ways; it does not yet say a COUNT must be derived from a search rather than a list.
RULE R-J    A per-site absence claim must be generated FROM A SEARCH, not from a hand list. If a
            prompt says "the N sites", the N must come from a grep whose pattern is quoted in the
            prompt, so a Worker can re-run it and get the same N.
```

⚠ **The Worker nearly fixed sites 9 and 10 silently** — they are inside the allowlist and in the
same function — and did not, because *"your count of eight is a load-bearing premise of P-D's
report contract and silently reporting ten under an eight-row heading would corrupt the acceptance
record."* That is better judgement than my prompt deserved.

### 28.2 🐞 PROMPT DEFECT E1-D3 — a stage gate that could not be satisfied

I made F3 (the schema-refusal test) a pre-commit stage gate, and allowlisted no file matching
vitest's default `**/*.{test,spec}.?(c|m)[jt]s?(x)`. **None of the nine paths is a test file the
runner would collect.** The natural host, `frontend/src/hooks/useGameStore.test.ts`, exists and
already exercises the migrate chain — and I left it off.

⇒ A genuine contradiction between an obligation and an allowlist. **Class R-B: prohibitions and
obligations written in separate passes and never read against each other.** My own section-8
cross-check paragraph claimed I had done that pass. I had not done it for the TEST hosts.

### 28.3 🐞 PROMPT DEFECT E1-D4 — two file paths that do not exist

```text
I CLAIMED   frontend/src/components/game/Tile.tsx and components/game/TileRack.tsx
ACTUAL      frontend/src/components/tiles/Tile.tsx and components/tiles/TileRack.tsx
```

`components/game/` exists but holds the overlay, score panel and controls. The substantive claim —
no single-code-point assumption in those components — **holds at the real paths**, and the Worker
verified it there. Harmless because both are off-allowlist under either spelling, but it is R-G
again: **I asserted a path I had not listed.** Also unnamed: `components/board/Cell.tsx` is the
actual per-cell renderer and belongs on that list.

### 28.4 🐞 PROMPT DEFECT E1-D5 — section 6 undercounted the re-pointing, and section 8 forbade it

Beyond the five references I enumerated, three more assertions encode the OLD wire shape and are
all inside the allowlist:

```text
test_atomic_token_persistence.py:233-253   asserts len(board)==15, every row a 15-char str,
                                           board[7][7]=="A", blanks==[{"row":7,"col":7}]
test_api.py:1078                           data["state"]["board"][7][7:9] == "AT"
test_api.py:1324                           data["state"]["board"][7][7:10] == "JOE"
```

⇒ And my section 8 said *"Section 6 is the one authorized re-pointing"*, which reads as forbidding
exactly the edits the allowlist permits. **Same class as defect D3 of era 12** — two instructions
about the same file that cannot both hold.

### 28.5 ⛔ THE FINDING — the AI's own board view is worse than the wire, and I had missed it

```text
backend/gamecore/state.py:32-44   build_ai_state_dict
    row_chars.append(cell.letter)  ...  grid.append("".join(row_chars))
:48 ai_rack="".join(ai_rack)
```

⛔ **A single `SZ` makes that row SIXTEEN characters and silently shifts every column to its
right.** `ai_rack` collapses a digraph rack into an ambiguous character run. It flows through
`services.py:1602` → `compact_state` at `:1618` → `prompts.ts:314` `extractGridRows` /
`renderLabeledBoard` / `listAnchorSquares`.

⇒ **After C1a as I scoped it, the HUMAN would see `SZ` correctly and the MODEL would see a
corrupted, off-by-one grid.** That is a silent wrong board — precisely what decision D-3 exists to
prevent — one layer inward, and `gamecore/state.py` was neither allowlisted nor prohibited.

**I verified both halves myself** at `state.py:32-44` and `services.py:1602/1618`. The Worker rates
it higher-risk than the dictionary-authority work I had scheduled next. **I agree, and it changes
the plan.**

⭐ **One thing this does NOT cost, measured by me after the report:** `MOVE_SYSTEM_PROMPT` is
`moveSystemPromptFor(englishMoveSpec)` at `prompts.ts:186` — a static template — while
`extractGridRows` (:227), `renderLabeledBoard` (:238) and `listAnchorSquares` (:253) are separate
exported functions used at :314-319 to build the USER message. So **the three functions can change
without touching the hashed constant**, and standing condition 1's MOVE CORE hash survives. That
was the thing I most feared and it is not a problem.

### 28.6 C1 is THREE parts, not two

```text
C1a  the WIRE projection — the human's board.        ten guard sites, schema 4, store 5->6
C1b  the AI'S BOARD VIEW — build_ai_state_dict, compact_state, and the three prompts.ts grid
     functions. ⛔ NEWLY DISCOVERED. Higher risk than C1c because it fails SILENTLY.
C1c  DICTIONARY AUTHORITY — WordAuthority at five call sites, _word_passes_dictionary deleted.
ORDER  C1a, then C1b, then C1c. C1b must not precede C1a, because it is the same shape question
       one layer inward and the wire decision (D-1) should settle the representation first.
```

### 28.7 Other findings, dispositioned

```text
MEASURED 3  diagnostics.py:373,374,782,789 hold four more single-code-point letter guards.
            -> Correctly forbidden in 03/01 by D-5. They belong to C1c's exchange. Recorded.
MEASURED 4  serializers.py:275 also tests `.isalpha()`, which is FALSE for `L·L`. Dropping only
            the length test leaves the digraph accepted and the INTERPUNCT rejected.
            -> ADOPTED into the reissue: the replacement predicate must drop `.isalpha()` or
            delegate to the variant's playable set, and it must be named explicitly.
            ⚠ And the canary would NOT catch it: F2 is a backend-legality canary and does not
            traverse PlacementSerializer. A canary that cannot reach the code is not a canary
            for that code.
MEASURED 7  consumers.py forwards get_game_state_for_user verbatim, so multiplayer is covered
            for free — but the client refusal must therefore cover the websocket frames too, and
            one ingress file is off-allowlist. -> Confirms the refusal belongs in setGameState.
MEASURED 8  move-history and the draw payload are ALREADY lossless. -> No work in any exchange.
            A scope reduction, and the first one this campaign got from a Worker rather than me.
MEASURED 9  gamecore/state.py:79 already calls its SAVE format "schema 4". The wire's inherited 4
            and the save's 4 are two different axes. -> Recorded so nobody conflates them; the
            reissue will say so in prose.
LEAD 4      once sites 3/4 relax, PlacementSerializer accepts any non-empty token and nothing
            bounds its length. -> ADOPTED: the reissue must add an explicit token-length bound in
            the same exchange that removes the guard. An unbounded `letter` reaching the scoring
            path is a real hazard, not a theoretical one.
```

### 28.8 Coordinates for the reissue

```text
The exchange is CONSUMED: a Worker received it, worked, and produced a terminal report. This is
not the era-12 dispatch-failure case where nothing had begun.
Assumptions CHANGED MATERIALLY — two new guard sites, a widened allowlist, a new predicate
requirement, a token bound, and a third sub-slice discovered. That is AP's changed-route trigger,
and the subagent session is gone regardless.
⇒ fresh-worker-session, Worker session ordinal 04, Worker exchange ordinal 01.
```

⚠ **What this exchange cost and what it bought.** It cost one full gate ladder and produced zero
product change. It bought: two guard sites that would have made C1a a silent no-op, a
contradiction that would have forced an unauthorized edit or a skipped fixture, three
old-shape assertions that would have failed the suite mid-slice, and **a corrupted AI board view
that would have shipped green.** On an E3 slice touching a live multiplayer product, that is the
cheapest possible outcome.

---

## 29. ⛔ Exchange 04/01 ALSO returned BLOCKED — a fifth defect, and it is arithmetic

```text
prompt   04_implementation_00.md    task MEC-C1a-reissue, tier E3, reasoning High
report   04_report_00.md            status BLOCKED, Escalation disposition NEEDS_ORCHESTRATOR_DECISION
tree     unchanged at 8a50ded. Porcelain empty. Zero mutation, again.
```

⚠ **Two BLOCKED exchanges in a row on the same task. That is not a stuck loop — each found a
DIFFERENT class of defect, and both were mine.** The finite-convergence rule I must watch is "the
same assumption surviving correction and recheck"; that has not happened. 03/01 found an
incomplete absence claim; 04/01 found a forced logical contradiction. Different assumptions, both
now retired by measurement.

### 29.1 🐞 C-7 — an assertion that CANNOT coexist with the requirement, and I verified it myself

```text
backend/tests/test_slovak_engine.py:205
    assert not PlacementSerializer(data={"row": 7, "col": 7, "letter": "CH"}).is_valid()
```

That file is **not on the allowlist**. And `"CH"` is structurally IDENTICAL to `"SZ"` — I measured
every dimension:

```text
         NFC-stable  upper-stable  isalpha  len  has_letter
  'CH'      True         True        True    2      True
  'SZ'      True         True        True    2      True
```

⇒ **No predicate can accept `SZ` and reject `CH`.** F4 requires accepting `SZ`; therefore `:205`
must fail. Not a design hazard, not an implementation choice — **arithmetic.** The Worker proved it
with an in-process probe that monkeypatched the predicate and touched no file.

⛔ Every escape was closed by my own prompt: re-pointing the file was outside the allowlist,
keeping `CH` invalid was impossible, and skipping F4 was barred by my own stage gate. **A
three-way closed contradiction is the correct thing to block on.**

### 29.2 🐞 C-8 — my predicate vocabulary accepts a DIGIT as a tile letter

`test_slovak_engine.py:207` asserts `not …(letter="1").is_valid()`. My D-7 vocabulary — non-empty,
NFC-stable, upper-stable, no whitespace, no control characters — **accepts `"1"`.** Measured:
`'1'` is NFC-stable, upper-stable, `isalpha=False`, `has_letter=False`.

⚠ And `variant_store._parse_asset_token` accepts `"1"` too, so **mirroring its reasoning faithfully
reproduced the defect.** That is the hazard in "mirror the reasoning of X": X may be right for its
own threat model and wrong for yours.

⇒ The Worker measured the one-clause fix and **deliberately did not adopt it**, because I had
written "implement them; do not re-decide them". It handed me the measurement instead of the
decision. That is exactly the restraint the instruction asked for, and it is why the decision below
is mine to make rather than something I discovered after the fact.

### 29.3 🐞 MEASURED-2 — an EIGHTH guard, spelled differently, one file to the left

```text
backend/game/serializers.py:246   ExchangeSerializer.letters = ListField(child=CharField(max_length=1), …)
used by  views.py:304   /api/game/{id}/exchange/      (human)
         views.py:475   /api/game/{id}/ai-exchange/   (AI)
```

⛔ **My command C searched for `len(nfc) == 1`. This guard is spelled `max_length=1`, so the search
could not see it.** Relaxing `route.ts:1002` alone would forward `SZ` and the backend would answer
HTTP 400 — **the exchange path stays closed to every digraph language after C1a ships.**

⚠ **This is defect C-1 recurring, one level deeper.** I fixed "derive the count from a search
instead of a list" and the *pattern* was still incomplete. R-J needs its second half:

```text
R-J (amended)  A per-site absence claim must be derived from a search, AND the pattern must be
               justified against the SPELLINGS the guard could take, not only the one you
               remember. For a length guard in Python + DRF + Zod + regex that is at least:
                   len(x) == 1 · max_length=1 · .length(1) · .length === 1 · ^…$ around one \p{L}
               Enumerate the SPELLING SPACE in the prompt, so a Worker can widen it.
```

### 29.4 MEASURED-1 — my section-6 grep was short by one, for the same reason

`test_atomic_token_persistence.py:251` `assert state["blanks"] == [{"row": 7, "col": 7}]`. My
pattern searched `state\["board"\]` and the two adapter names — **never `state\["blanks"\]`**,
even though D-2 removes exactly that key. ELEVEN is TWELVE. Same class as 29.3.

### 29.5 MEASURED-4 — C1b is worse than I recorded, and confirmed at a second locus

```text
gamecore/state.py:44     grid.append("".join(row_chars))          ← the site I already knew
prompts.ts:190           GRID_ROW = /^[\p{L}.]{15}$/u
prompts.ts:227-236       extractGridRows keeps only lines matching GRID_ROW, then slice(0,15)
```

⇒ A digraph row is sixteen code points, so it does not merely misalign — **it fails the regex and is
SILENTLY DROPPED, and the model receives a SHORT BOARD.** I verified `GRID_ROW` at `prompts.ts:190`.

⭐ And two mitigations the Worker measured, both good news: the P-A hash covers only
`MOVE_SYSTEM_PROMPT`, **not the parser**, so C1b can repair `extractGridRows` without moving the
CORE hash; and `gamecore/state.py:63,104-125` **already carries a structured
`grid: list[list[str | None]]`** for the save file, so the token-preserving projection C1b needs
already exists beside the lossy one.

### 29.6 ⛔ THE FIVE DECISIONS — mine, taken now, with reasons

```text
D13-12  ALLOWLIST backend/tests/test_slovak_engine.py and authorize exactly TWO re-pointings.
        :205 is WRONG IN PRINCIPLE, not merely inconvenient. PlacementSerializer has NO VARIANT IN
        SCOPE — it cannot know whether `CH` is a tile in the game being played. Its job is SHAPE;
        playability is the engine's, and the SAME FILE already asserts it at :237
        (`"CH" not in variant.playable_letters`). So :205 becomes "shape-valid, engine-rejected",
        and the comment must say that the playability half is asserted thirty lines below.
        ⇒ The old assertion was passing for the wrong reason: it was testing the engine's rule
          through the serializer's length limit. Removing the limit exposes that, which is the
          change doing its job rather than breaking something.
D13-13  ADOPT the "contains at least one Unicode letter" clause. It restores :207, keeps SZ, DZS,
        L·L and Á, and rejects `1` and a bare `·`. ⛔ And RECORD WHY IT DEVIATES from
        variant_store._parse_asset_token, which accepts `1`: the manifest loader validates tokens
        DECLARED BY A MAINTAINER in a committed asset; the serializer validates UNTRUSTED PUBLIC
        INPUT. Different threat models justify a stricter predicate, and a future reader must not
        "harmonize" them.
D13-14  ELEVEN becomes TWELVE, and the section-6 pattern gains `state\["blanks"\]`.
D13-15  ⛔ ExchangeSerializer's max_length=1 goes INTO C1a, not into a successor. The lesson of
        sites 9/10 is that a partial removal leaving a downstream guard is a SILENT NO-OP.
        Deferring would repeat precisely the defect this reissue exists to correct. It is in an
        already-allowlisted file, it needs the same 16-code-point bound, and it needs its own
        fixture on both endpoints.
D13-16  frontend/src/lib/rack.ts UNICODE_TILE is DEFERRED and NAMED, not silently left. It is
        latent — reached only when gameState is null, because every call site passes
        `gameState?.alphabet` and services.py:163-169 always ships it. ⚠ But it MUST be fixed
        before Hungarian ships, so it goes to C1b, whose subject is exactly "the places a letter is
        still assumed to be one code point after the wire is fixed".
```

### 29.7 What two blocks cost and bought

```text
COST    two full gate ladders, two subagent sessions, zero product change.
BOUGHT  a no-op guard pair (03/01) · an unsatisfiable stage gate (03/01) · two nonexistent paths
        (03/01) · three undercounted assertions (03/01) · a corrupted AI board view (03/01) ·
        a FORCED CONTRADICTION that would have left the suite red with no lawful way out (04/01) ·
        a predicate that accepted digits as tiles (04/01) · an eighth guard that would have made
        the exchange path a no-op for every digraph language (04/01) · and a twelfth assertion
        line that would have left a KeyError (04/01).
```

⚠ **On an E3 slice over live multiplayer, nine defects caught before the first byte changed is the
cheapest possible outcome — and the pattern in them is now unmistakable.** Seven of the nine are
the same root cause: **an enumeration I produced from memory or from too narrow a pattern, and then
required a Worker to prove complete.** R-J amended in 29.3 is the rule that finally addresses it,
because it makes the SPELLING SPACE the prompt's obligation rather than the Worker's discovery.

---

## 30. ⭐ C1a LANDED at `529e691` — third issue, PASS, and I verified it myself

```text
prompt   05_implementation_00.md   task MEC-C1a-third, tier E3, reasoning High
report   05_report_00.md           status PASS, implementation-PASS
commit   529e6910ddf57dfbb4a9671bbab668b975067cf8   pushed, public readback equal
diff     11 files, +483 −99 — exactly the eleven allowlisted paths, all modified, none added
```

⚠ **One transport failure before it.** The first dispatch of 05/01 died with
`message_start … while message … is still open` — the Cooperator's own diagnosed
whole-response-generation hazard. I verified NOTHING had begun: HEAD unchanged, porcelain empty,
`backend/assets/` empty, `/tmp/opencode/mec-c1a3/` absent, public ref unchanged, `.ap` unchanged.
⇒ **Delivery died before any outcome existed, so I re-delivered the SAME ordinal 05/01.** That is
the era-12 database-failure class, not the balance-failure class: an interruption record is for a
task that BEGAN, and this one had not.

⚠ **And the Cooperator hit the same error again on my own output.** Standing instruction adopted:
**write Meta in small appends against a sentinel, never one large generation.** This section and
`05_report_00.md` were both written that way.

### 30.1 What I verified myself, independently of the report

```text
HEAD == public ref                   529e6910ddf57dfbb4a9671bbab668b975067cf8
porcelain                            EMPTY
changed paths                        exactly the eleven allowlisted, by git diff --name-only
prompts.ts · rack.ts · gamecore/ · diagnostics.py · backend/assets/   UNTOUCHED, by diffstat
CMD2 max_length=1[^0-9]              ZERO
CMD3 .length(1)                      ZERO
CMD1 len(x)==1 in serializers.py     ZERO
.length === 1 in route.ts            ZERO
CMD5 ^[?\p{L}                        TWO — prompts.ts:190 and rack.ts:1, the deferred C1b pair
adapter + constant in services.py    ZERO
WIRE_STATE_SCHEMA_VERSION = 4        services.py:321, emitted at :450
"blanks" in services.py              ZERO
ruff · mypy 85 · manage.py check     clean
pytest                               745 passed, 4 skipped        742 + 3
validate_lexicons                    13 asset(s) audited, 0 failed
typecheck · lint                     exit 0 · exit 0
vitest                               454 passed | 3 skipped       450 + 4
build                                exit 0, ELEVEN dynamic, ZERO static
```

**Every claim reproduced. Result accepted: implementation-PASS at `529e691`.**

⛔ **And that is ALL it is.** C1 is E3. The fresh independent acceptance is still owed, it must come
from a session that did not implement this, and **it cannot be my subagent** (`AP.md:1395-1405`).
That is the one thing in this whole campaign I can neither execute nor delegate.

### 30.2 ⛔ A SEVENTH AND EIGHTH SPELLING — and the seventh is a product-blocking defect

```text
frontend/src/components/game/BlankPicker.tsx:8
    const ENGLISH_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
```

⛔ **That is the UI that chooses what a blank represents.** A hardcoded twenty-six-entry
single-code-point English alphabet, so **a blank can never be assigned `SZ` from the product** no
matter how correct the wire, the serializer and the engine now are.

⛔ **My six-command inventory could not reach it.** The spelling is `"…".split("")` — no `len`, no
`.length`, no `max_length`, no `\p{L}`, no `charAt`. It is neither in scope nor classified out of
scope; it is **invisible**. ⭐ And `GameState.alphabet` already ships on the wire, so the fix has a
source of truth waiting.

```text
frontend/src/components/game/AIThinkingOverlay.tsx:72
    const letters = word.toUpperCase().split("");
```

An eighth of the same shape: a digraph word renders one tile per code point, so `SZA` shows three
tiles for two played.

⚠ **This is the THIRD consecutive exchange in which my enumeration was the defect.** R-J has now
been amended twice and still missed a spelling. So the rule needs its third and final form:

```text
R-J (final)  An enumeration handed to a Worker is a HYPOTHESIS, not a specification. Say so in the
             prompt. Give the commands, give the classification, and then require the Worker to
             report any site the commands cannot reach — as an OBLIGATION with its own report
             field, not as an optional observation. Three exchanges found three spellings I did
             not have; the fourth will find a fourth, and the prompt should expect it.
```

### 30.3 The other findings, dispositioned

```text
MEASURED 3  my section-6 count was short by FIVE, all in allowlisted files (four persist pins plus
            test_atomic_token_persistence.py:267 pinning the string "state_schema_version 4").
            -> ADOPTED as a cheap prophylactic: before publishing a fixed assertion count, RUN THE
               SUITE against the decided change and let the red output produce the list. That is
               strictly better than any pattern I can author.
MEASURED 4  ⛔ I attributed `:237` to the WRONG FILE. `"CH" not in variant.playable_letters` is at
            test_atomic_tile_tokens.py:237, not test_slovak_engine.py, which is only 208 lines
            long. Substantive claim true, D-10 stands, committed comment points at the right path.
            ⚠ Had the fix depended on editing that line, D-10 would have been un-completable in
               exactly the way 04/01 was. R-G again, and it nearly cost a fourth exchange.
MEASURED 5  gamecore/state.py:153,157 is a THIRD 15x15 validator, and it already rejects
            isinstance(row, str) — so the save-file validator AGREES with the new wire rather than
            conflicting with it. No action.
MEASURED 6  services.py:216-218 `not w.isalpha()` in _word_passes_dictionary means `L·LA` CANNOT
            PASS THE DICTIONARY today. lexicon_health.py:95 has the identical test.
            -> ROUTED to C1c, and it enlarges it: C1c is no longer only "pass a WordAuthority",
               it also has to fix a word-level .isalpha() that rejects the canary's own word.
LEAD 1,2    prompts.ts:250 and :254 are suspected additional C1b sites, and a labeled row built
            from BoardCell tokens may need a SEPARATOR rather than a widened count.
            -> ADOPTED into C1b's scope as questions to measure, not as conclusions.
LEAD 3      suspected that NO test renders Board.tsx. -> One `find` settles it; I will run it when
            C1b is scoped, because it decides whether the visual path has any guard at all.
```

### 30.4 C1's remaining shape

```text
C1a  ⭐ DONE at 529e691, pending fresh independent acceptance
C1b  the AI's board view AND the two UI spellings:
       gamecore/state.py:44   "".join(row_chars)              a 16-char row shifts every column
       prompts.ts:190         GRID_ROW /^[\p{L}.]{15}$/u      a 16-char row is SILENTLY DROPPED
       prompts.ts:250 :254    suspected, to measure
       rack.ts:1              UNICODE_TILE
       BlankPicker.tsx:8      ⛔ blank can never become a digraph FROM THE PRODUCT
       AIThinkingOverlay.tsx:72
     ⭐ and the CORE hash covers only MOVE_SYSTEM_PROMPT, not the parser, so C1b need not move it
C1c  dictionary authority: WordAuthority at five call sites, delete _word_passes_dictionary,
     four diagnostics.py guards, AND the word-level .isalpha() in services.py:216 +
     lexicon_health.py:95 that rejects L·LA
```

---

## 32. ⭐ C1a INDEPENDENTLY ACCEPTED — `acceptance-PASS` at `529e691`

```text
prompt   06_acceptance_00.md   Fresh Independent Audit, read-only, no mutation authority
report   06_report_00.md       status PASS · Phase-qualified result acceptance-PASS
owner    a session that did NOT design, implement or author the candidate, is NOT the session-05
         subagent, and is NOT me. ⭐ Acceptance independence: required-fresh-independent — SATISFIED.
verdict  R1-R6 all HOLD · P1-P5 all held · N1-N6 all FAILED as required · 0 corrections
```

⛔ **The outstanding obligation of this whole is now discharged.** C1a is accepted. C1b is unblocked.

### 32.1 Two disclosures the audit made that I must not bury

```text
Q2  ⛔ R1 IS NOT CERTIFIED FOR THE HUMAN-VISIBLE BOARD.
    MEASURED BY ME, confirming it: `ls frontend/src/components/board/*.test.*` -> NONE.
    Board.tsx consumes the new shape correctly, but that is a COMPILE-TIME contract — typecheck,
    lint and build — not a render test.
    ⇒ The acceptance certifies THE WIRE PAYLOAD AND THE INGEST PREDICATES. It does not certify pixels.
    ⇒ The only pixel evidence that will ever exist for this slice is B4-2 of
      91_deferred-acceptance-batch.md — the Cooperator's own eyes. That entry was written that way
      before the audit said so, and the audit independently agreed it is the only route.
Q3  ⛔ VERSION SKEW IS USER-SILENT. isSupportedStateSchemaVersion is exact equality, the backend
    always emits 4, there is no dual-accept window, and a refused payload produces console.error plus
    EMPTY_BOARD — no toast, no banner, no copy. A user can sit on an empty board with only a console
    line. The decided posture "refuse rather than mis-render" HOLDS; it is not a user-facing screen.
    ⇒ FRONTEND AND BACKEND OF 529e691 MUST DEPLOY TOGETHER. Recorded for the deployment whole.
    ⇒ And old client + new backend has NO refusal at all, because the guard is introduced in this
      very commit. That asymmetry is why "together" is mandatory rather than advisable.
```

### 32.2 ⭐ It handed over a NINETEEN-ITEM inventory, and that is C1b's scope, complete

The audit answered the one obligation I put in the prompt as a required field rather than an
observation — *name any place a letter is still assumed to be one code point, including files this
prompt declares out of scope* — and returned nineteen items. **Seven of them I did not have.**

```text
NEW TO ME, and I verified each myself at 529e691:
  legality.py:28    LETTERS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ")     ✔ confirmed
  legality.py:143   error copy "Letter must be A-Z or '?'" while the CHECK is set membership ✔
  move_search.py:33 _BLANK_LETTERS = string.ascii_uppercase                ✔ confirmed
  prompts.ts:267    rows[row][col] — indexes a string one column per UTF-16 unit ✔ confirmed
  test_atomic_tile_tokens.py:532  asserts len(row) == 15 on the AI grid    ✔ confirmed
                    ⚠ AND THAT FILE IS THE L·L CANARY'S HOST, which C1b must therefore edit — the
                      one file three prompts in a row forbade touching.
  constants.ts      TILE_POINTS is A-Z plus "?" only
  ai-turn-simulation.test.ts:119 · rack.test.ts:4 · three Slovak/Czech test files
```

⚠ **And it labelled its own inventory honestly:** *"it is a search, not a proof of absence."* That is
R-J being honoured by a Worker without being told the rule — which is the strongest evidence yet for
`AP_DEFECTS.md` D-01 and D-04.

⚠ **Its context pressure was HIGH** — full backend suite, full frontend suite, production build,
interpreter controls and a multi-pattern search in one exchange. `AP_DEFECTS.md` D-02 and D-09 name
exactly that: I asked for all of it in one grant. **A cheaper acceptance would have split the
controls from the inventory.**

## 31. Session boundary — artifacts owed and delivered

```text
AP_DEFECTS.md            /home/agile/meta/AP_DEFECTS.md   847 lines. Twelve MEASURED defects of the AP
                         protocol from this one whole, each with evidence cited by heading inside ONE
                         directory, each with a proposed fix. Written at the Cooperator's request as
                         input to a protocol-update task. D-01 is the largest: the Worker never
                         critiques the Orchestrator, and twelve of my own defects were caught by a
                         report field AP does not require.
91_deferred-acceptance-batch.md   extended with B3 (the eight languages, RENDERED steps) and B4 (C1a,
                         which states plainly that it is not accepted yet and that nothing below its
                         first step counts until it is).
93_orchestrator-handout.md        611 lines. The continuation handout for a fresh Orchestrator, with
                         the UI-localization objective priced in three options and the ONE material
                         product decision flagged as the Cooperator's.
06_acceptance_00.md      the C1a independent-acceptance prompt. ⛔ DELIVERED TO THE COOPERATOR FOR
                         COPY-PASTE. Session 06 is reserved; its report does not exist yet.
```

⛔ **The single outstanding obligation at this boundary is the C1a independent acceptance.** It is E3,
it must come from a session that did not implement it, and it cannot be a subagent of the Orchestrator.
Everything else in this whole is either landed and verified or recorded as a named blocker.

## 26. Next step


```text
NEXT   Slovenian — measure whether it needs C1 at all before assuming it does.
       ⇒ After that, every language the proven pipeline can reach WITHOUT C1 is shipped.
       C1 (E3) — still the highest-leverage item: hu · hr · es · el · bg · ru in one slice, and
       the only slice needing a Worker plus fresh independent acceptance.
LATER  C2 as an explicit declared blank-target set. The case list keeps growing:
         afrikaans blank→X Z · italian blank→J K W X Y · danish blank→Q · swedish blank→Q W Ü Æ ·
         turkish blank NOT→Q W X
       C3 narrowed to Turkish. Spylls route for French and Hungarian.
       _lexicon_build.py — ELEVEN scripts, far past the stated trigger.
       ⚠ RE-DISPOSITIONED, and the reason is worth recording. I set the trigger "before the
       tenth language" as a GUESS, before I knew the shapes. Now that eight distinct shapes are
       measured, a shared module would need heavy parameterisation, and the per-script
       differences are load-bearing and heavily documented — Danish's truncation guard, Swedish's
       Ü carve-out, Icelandic's no-rule assertions, German's latin-1 pair, Portuguese's per-file
       encodings. A shared module risks making exactly those differences LESS visible, which is
       the opposite of what this codebase is built to value.
       ⇒ DEFERRED, not cancelled, and the new trigger is CONCRETE rather than a count: extract it
         when one rule must change in THREE OR MORE scripts at once. `--check` on all eleven
         makes it byte-verifiable whenever it happens. Zero product value today, and C1 unlocks
         six languages.
BLOCKED, recorded, not hidden:
       finnish   no plain affix pair (Voikko)
       malay     no ms_MY source
       french    expander cannot render it (~77k of ~400k words)
       norwegian no explicit licence grant for the word list
       hungarian size (~301 M forms) — decision D taken
```

## 33. ⭐ The UI-localization decision is TAKEN, and it is OPTION A

The previous handout priced the objective in three options and named the choice as the Cooperator's,
not the Orchestrator's. I put all three to him with the measured cost of each. He answered:

```text
SCOPE   A — eight FULL catalogs, ~300 keys each, every one carrying a header declaring it
        machine-authored and unreviewed. Not C, not B. He accepted the stated risk: eight
        languages of unreviewed copy in a piece he is presenting at a job interview.
FLAGS   NONE for now — names only. `GameLanguagePanel.tsx:51` already OMITS `flagSrc` when the slug
        has no entry, so the picker is correct without them and accepts real PNGs later with no code
        change. I offered to draw the geometric ones (it nl de da sv is are exact geometry at 48×32;
        ZA is a Y-shape in six colours) and disclosed that PT's armillary sphere would be an
        approximation. He declined: no hand-drawn national flags in this product.
```

⛔ **And then he corrected my execution, not my analysis: `PREKLADY MA ROBIT FRESH ORCHESTRATOR`.**
I had taken `Pokracuj` as authority to implement, and had begun slice 1 in this session. That was
wrong on the protocol and wrong on the economics — this session's context already carries the whole
C1a arc, and 2 400 strings on top of it is AP_DEFECTS D-02 and D-09 self-inflicted. I reverted the
working tree to `529e691` (porcelain empty, verified) and wrote this section instead. **Nothing of the
objective is implemented. All of the reconnaissance below is real and saves the fresh Orchestrator a
full measurement pass.**

### 33.1 The catalog architecture, measured at `529e691`

```text
messages.en.ts       280 text keys + 20 fn keys = 300. The 280 are `enText`; the 20 are `enFn`.
messages.{sk,cs,pl}  `Record<TextKey, string>` and `{ [K in FnKey]: (typeof enFn)[K] }`
                     ⭐ THAT MAPPED TYPE IS THE FREE WIN, and it changes how to slice this: a new
                     catalog file typechecks its OWN key set and its OWN per-key parameter shapes
                     against `messages.en.ts` ALONE. `tsc --noEmit` on the file catches a missing
                     key, an extra key, and a wrong interpolation parameter — WITHOUT the locale
                     being added to LOCALES, and without `i18n.test.ts` running.
                     ⇒ Eight catalogs can be written and verified in PARALLEL by eight Workers, each
                       one gated on typecheck, before a single wiring file is touched.
translate.ts:7-18    TEXT and FN, both `Record<Locale, …>` — 8 entries each to add. Adding a locale
                     to LOCALES without both entries is a type error, so the wiring cannot half-land.
translate.ts:20-40   `tf`'s one confined cast, with a comment explaining why the variance is safe.
                     ⛔ Do not touch it; the reason it is safe is the mapped type above.
index.ts:24          re-exports pluralCs pluralEn pluralPl pluralSk — 8 more to add.
locales.ts:1         LOCALES, and `detectBrowserLocale`/`isLocale` follow it with no edit needed.
```

### 33.2 ⭐ The plural rules, DERIVED AND VERIFIED, not guessed

The handout said each new locale needs a sourced plural function and warned that Icelandic is not a
simple one/other language. Both are right, and there is a better source than a citation: **ICU's CLDR
data is already in the test runtime.** `Intl.PluralRules` is CLDR, so the rule can be pinned
EXECUTABLY — compare each helper against `new Intl.PluralRules(lang).select(n)` across the whole
integer domain the helper can observe. A CLDR change then shows up as a red test instead of as a
silently wrong string. Measured on `node v26.4.0 / ICU 78.3`:

```text
af nl de da sv   one/other, and over integers 0..3000 each is IDENTICAL to `en` — measured, all
                 four, zero divergences. ⛔ IDENTICAL IS NOT THE SAME AS THE SAME RULE: Danish CLDR
                 is `n = 1 or t != 0 and i = 0,1`, so da 0.5 → one while en/nl/de/sv/af 0.5 → other.
                 The existing helpers TRUNCATE, which is what makes the fraction unreachable and the
                 identity real. ⇒ Five separate functions, not five aliases. `pluralCs = pluralSk` is
                 an alias only because those two agree over the WHOLE domain, fractions included.
is               ⛔ NOT the Nordic one/other shape. `i % 10 == 1 && i % 100 != 11`. 21, 31, 101, 121
                 are `one`; 11 and 111 are `other`. Diverges from `en` at 269 of the integers in
                 0..3000. The handout's suspicion was correct.
it               THREE categories: one / many / other. `many` is reachable by an integer —
                 1 000 000 and 2 000 000 select it (`i % 1000000 == 0 && i != 0`).
pt               THREE categories, AND ⛔ ZERO IS SINGULAR: CLDR `one: i = 0..1`, so 0 → one.
                 "0 ponto", not "0 pontos". ⭐ THIS IS THE ONE THAT WOULD HAVE SHIPPED WRONG: a rack
                 that scores nothing and a passed turn both display zero, so a copied English rule
                 is visibly wrong on a real board, not in a corner case.
```

⚠ **A finding about the THREE HELPERS THAT ALREADY SHIP, and it is a naming defect, not a behaviour
defect.** `pluralSk`'s third parameter is called `many`, but over the integer domain CLDR Slovak has
no `many` at all — 0 and 5+ are `other` (`many` is Slovak's fraction category). The Slovak and Czech
catalogs fill that slot with the genitive plural, which is the linguistically correct form for 0 and
5+, so **every shipped string is right and nothing needs re-translating.** Polish is different again:
`pluralPl`'s third slot really is CLDR `many` (pl 0 → many, verified). ⇒ A CLDR-comparison test must
declare the slot→category mapping per language rather than assume the parameter names are CLDR
category names. Do not "fix" the Slovak parameter name and the catalogs in the same slice as eight new
languages.

### 33.3 🐞 Two gaps the objective walks into, both measured, neither in the handout

```text
1  messages.en.ts `lexiconRejectionKey()` switches on collins2019 · slovak · czech · polish and
   returns `game.lexicon.unknown` for anything else. EIGHT playable variants ship lexicons that all
   fall through to "unknown", so a rejected Danish word cannot name the lexicon that rejected it.
   ⇒ This is a REAL product gap that exists TODAY at four locales, independent of adding eight more.
     Price it as its own slice; it is 8 keys × 12 locales plus 8 switch arms, and it is the kind of
     string a reader can check at a glance.
2  i18n.test.ts:983 `ownName` is Record<INSTALLED_VARIANTS, Record<LOCALES, string>>. Option A takes
   LOCALES to twelve; naming the eight new variants takes INSTALLED_VARIANTS to twelve.
   ⇒ 144 CELLS, and the test asserts each label CONTAINS its variant's own name and does NOT contain
     any OTHER variant's name in that locale — 12 × 12 × 11 substring assertions.
   ⛔ THE SUBSTRING CONSTRAINT IS A REAL TRAP AND ICELANDIC IS WHERE IT BITES: "Enska" (English) is a
     substring of "Hollenska" (Dutch) and of "Svenska" (Swedish). It survives today ONLY because
     `toContain` is case-sensitive and the cells are capitalised. That is luck, not design.
   ⇒ Do NOT weaken that test to land the matrix. Split the naming axis into its own slice AFTER the
     eight catalogs, so a collision is diagnosed against four locales of known-good data first.
```

### 33.4 What the fresh Orchestrator is handed, and what it must decide for itself

```text
GIVEN   the two decisions above (A, no flags), 33.1's architecture, 33.2's verified plural data,
        33.3's two gaps. All measured at `529e691` with the tree clean.
ITS OWN slicing, prompts, Worker count, and whether the eight `settings.gameVariant.*` keys and the
        `lexiconRejectionKey` arms belong in this objective at all. I recommend the catalogs first
        (they typecheck in isolation and parallelise), the wiring second, and both naming axes third
        — but that is a recommendation, and the ownName matrix is exactly the kind of thing a fresh
        session should price against AP_DEFECTS D-02 rather than inherit as a plan.
⛔ NOT   one translated string from this session. I wrote none, and the revert is verified.
```

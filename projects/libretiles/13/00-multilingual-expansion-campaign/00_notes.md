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

## 10. Next step

```text
V3d — delete backend/assets/dicts/sowpods.txt with a test asserting its absence.
      baseline a199d0e4086231a5f39853cbca0a94e7c734a37a
      tier E2 (the blob survives in Git history at bd2d63f, so a revert restores it
      byte-for-byte — that is why it is not E4)
      reasoning Medium
      the absence assertion belongs in backend/tests/test_documentation_dictionary_claims.py,
      which now exists for exactly this purpose
```

Then the sourcing probe, which is the campaign's real critical path: twenty ledger rows are
blocked on a sourced tile distribution and a licence-clean lexicon, not on code.


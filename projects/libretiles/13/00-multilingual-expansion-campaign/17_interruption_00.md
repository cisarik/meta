> ⛔ **THIS IS AN INTERRUPTION COMPANION, NOT A REPORT.** `AP.md:322-336`: an interruption companion is
> lawful only where **no terminal report exists**, is written by an authorized non-Worker owner from
> safely known facts, and **never impersonates the Worker**. It is written by the ORCHESTRATOR. Every
> claim in it was measured by the ORCHESTRATOR in the working copy; **nothing here is attributed to the
> Worker except what the Worker wrote into the committed file itself.**

# Interruption companion — exchange 17/01, MEC-UIL-C8-af

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 17          ⛔ CONSUMED. This ordinal is spent and may not be reused.
Worker exchange ordinal: 01
Prompt              ./17_implementation_00.md   730 lines, apfieldcheck exit 0
Terminal report     ⛔ NONE EXISTS AND NONE WILL. Not late — unreachable.
Companion owner     ORCHESTRATOR
Outcome             the authored file SURVIVED and is committed as 0a4fcc2
Evidence posture    non-independent, and now additionally UNATTRIBUTED at the authoring step
```

## 1. What happened, in the order it happened

```text
09:38   ORCHESTRATOR writes ./17_implementation_00.md, apfieldcheck exit 0. Repo at fde3321, clean.
~09:40  Delivery attempt 1. A Worker receives the prompt and begins.
~10:19  `frontend/src/lib/i18n/messages.af.ts` is written — mtime 10:19, 50 577 bytes, UNTRACKED.
        ⇒ THE WORKER COMPLETED ITS AUTHORING WORK.
        Delivery attempt 1 then fails in the channel:
          "Received message_start for message msg_3026956cf80d49228eef67dcc31cc418 while message
           msg_9f70454bba964ca7bbcb8d1cd5d8ce85 is still open."
        ⇒ A STREAM MULTIPLEXING FAULT. The Worker's terminal report never reached the ORCHESTRATOR.
~10:2x  ORCHESTRATOR checks state and — ⛔ MISREADS IT — reports "nothing began" and re-delivers.
        Delivery attempt 2 fails at the provider before any Worker starts:
          "No available channel for model claude-opus-5 under group default".
        ⇒ NO SECOND WORKER EVER RAN. Nothing was executed twice.
10:4x   The COOPERATOR asks whether the second subagent ran, whether a "continue from the last
        completed step" message would help, and whether the Afrikaans catalog is intact.
        ⇒ That question is what caused the state to be re-measured properly.
```

## 2. 🐞 THE ORCHESTRATOR'S OWN DEFECT IN HANDLING THIS, and it is the reason this file exists

```text
⛔ AFTER ATTEMPT 1 FAILED, THE ORCHESTRATOR RAN A STATE CHECK AND CONCLUDED "NOTHING BEGAN". THAT WAS
   WRONG. The very command it ran printed the evidence:
       git status --porcelain=v1   →   ?? frontend/src/lib/i18n/messages.af.ts
   and the next line of the same output block said `ls: cannot access …messages.af.ts` — because the
   `ls` ran in the WRONG DIRECTORY relative to the path it was given.
⇒ TWO SIGNALS, ONE TRUE AND ONE FALSE, IN ONE OUTPUT BLOCK, AND THE FALSE ONE WAS BELIEVED — because it
  was the one that matched the expectation ("the delivery failed, so nothing ran").
⇒ CONSEQUENCE: a re-delivery was issued for an exchange whose work was already complete. It happened to
  be harmless, because the provider refused it before a second Worker started. ⛔ HAD IT SUCCEEDED, A
  SECOND WORKER WOULD HAVE FOUND A DIRTY TREE IT DID NOT CREATE, and its repository gate would have
  failed — which is the protocol working, but only by luck rather than by the ORCHESTRATOR's care.
⭐ RECORDED AS R-Q: A DISPATCH FAILURE DOES NOT TELL YOU WHETHER WORK BEGAN. THE TREE DOES. Read
  `git status --porcelain=v1` AND `ls` the exact target path from the repository root, and when two
  signals disagree, believe the one that is harder to fake — porcelain, not a bare `ls`.
  ⛔ AND THE SHARPER HALF: the campaign already had this distinction written down. `00_handout.md` §10
  separates "killed MID-TASK → an interruption companion, and the session ordinal IS consumed" from
  "killed BEFORE the Worker received anything → safe to re-deliver the same ordinal". §47.1 of the notes
  had applied it correctly one exchange earlier. ⇒ The rule was known, cited, and recently used, and it
  was still applied to the wrong branch because the measurement was sloppy. Knowing a rule is not the
  same as measuring the fact it keys on.
```

## 3. What the ORCHESTRATOR measured before committing another agent's work

**Unattributed work in a tree is evidence of nothing until it is measured.** All of the following was run
by the ORCHESTRATOR, in the working copy, before `git add`:

```text
STRUCTURE
  porcelain                     exactly ONE entry, and it is this file
  header vs messages.de.ts      diff EMPTY — the seven mandated machine-authored lines, byte-identical
  file closes properly          733 lines, final line `};` — not a truncated stream
  afText entries                296        afFn entries   20        ⇒ 316, the frozen key set
  export shapes                 `afText: Record<TextKey, string>` · `afFn: { [K in FnKey]: … }`
  grep -c 'pluralAf('           3
  grep -nE '^[^/]*plural'       one import + three calls, nothing else
  aria-live / role="status"     ZERO   (the i18n.test.ts exactly-once scan is safe)
  forbidden type weakenings     ZERO   (no cast, no Partial<, no optional key, no spread, no TODO)
  git diff --check              clean
THE PROMPT'S FOUR DUTCH-DIVERGENCE CHECKS
  ^[^/]*\b(jouw|jij|je)\b       ZERO
  ^[^/]*ij                      ZERO
  ^[^/]*lijk                    ZERO
  thousands separator           `279\u00A0496` — U+00A0, NOT Dutch's period
THE FOUR FRONTEND GATES
  npm run typecheck             clean  ⇒ the completeness proof for all 316 keys and every signature
  npx vitest run                467 passed / 3 skipped — unchanged
  npm run lint                  clean
  npm run build                 PASSED, and separately the code type-checks; ELEVEN dynamic routes,
                                ZERO static
BACKEND FIVE                    not run. Explicit deviation: the diff is one new file under frontend/.
```

⇒ **Committed as `0a4fcc2`, pushed, public readback equal, porcelain clean.**

## 4. ⭐ WHAT SURVIVED, AND WHY — the campaign ruling that rescued this exchange

**The report is gone. The decisions are not.** At catalog 1 the campaign ruled that **the FILE is the
canonical home of every vocabulary and grammar decision**, because a reviewer opens the file and not a
report (`00_notes.md` §42.3 LEAD 6, reaffirmed in §43.4 and §45). That ruling was made for reviewability.
**It is what makes this interruption recoverable rather than a loss.**

The committed file carries ~120 lines of in-file commentary, and it contains everything the terminal
report would have carried about the *work*:

```text
· the NINE FROZEN TERMS with their reasons, including why `wedstryd` and not `party` (the cognate of
  Dutch's frozen `partij`, which D6 forbids harmonizing to) and why `blokkie` and not `teël` or `steen`
  (the cognates of Dutch `tegel` and German `Stein`)
· the PASS-NOUN finding: Afrikaans HAS one, like Danish and Swedish; and it escapes the passport knock-on
  that bit Danish and Icelandic because the passport is `paspoort`, never bare `pas`
· the REGISTER: informal `jy`/`jou`, and the observation that Afrikaans has no separate possessive so the
  catalog contains two second-person words in total and no third exists to get wrong
· ⭐ THE COINCIDE/CONTRAST ANSWER, and it is a genuinely new finding the campaign did not have: the
  question is ONLY PARTLY ANSWERABLE for Afrikaans, because the verb is INVARIANT — at a single-word
  control the two candidate styles are the SAME STRING and cannot contrast at all. Where they can
  contrast is OBJECT ORDER in a multi-word label, and every multi-word control took the imperative order.
  ⇒ So they coincide for a MORPHOLOGICAL reason rather than a stylistic one, unlike it/da/sv.
  ⭐ That is the answer §5.3 explicitly invited ("say so if that is what you find — that is a better
    answer than forcing a choice") and it is the only catalog that could give it.
· the ORTHOGRAPHY statements, including a reality check the prompt did not ask for: of the six diacritics,
  only `ê` actually ARISES in this key set, exactly once, at `chat.placeholder` — stated so a reviewer
  does not read absence as ASCII substitution
· the CAPITALIZATION answer on both halves: no common noun capitalized, AND language names capitalized
  in both families, siding with Dutch and German against it/is/da/sv
· the `AI` article decision, and that it was FREE — Afrikaans has one article `die`, no gender and no
  definite suffix, so the choice that cost six predecessors a gender, an apostrophe or a colon has no
  second form to pick
· the DUTCH DIVERGENCE BLOCK: eight concrete differences with the four grep results embedded, and the
  `z-` pass recording that exactly ONE z-initial word survives — `zoem`, deliberately
· ⭐ the DOUBLE NEGATIVE, correctly identified as the most systematic difference of all and as a change of
  clause SHAPE rather than of words, reaching every `error.*`, every `game.blocker.*`, all the
  `game.lexicon.*` rows and every `unavailable` string
```

## 5. ⭐ THE PREDICTION THIS CATALOG EXISTED TO TEST — CONFIRMED, at the key, in the file

The campaign's most-corrected inference reached its decisive test here, and the file answers it:

```text
HISTORY  pt · is · it all reported all four fixed call sites HARMLESS → the ORCHESTRATOR concluded three
         agreeing reports were enough to leave the code alone (§45.5). nl then HIT TWO (§46.1) →
         inference invalid, because none of the three agreeing languages was verb-final. The ORCHESTRATOR
         named VERB-FINALITY and asserted DANISH shared it → da corrected that (Mainland Scandinavian
         never had it) and reported all four harmless (§47.2); sv confirmed the same (§48.5).
         ⇒ MECHANISM: this pair of sites constrains VERB-FINAL WEST GERMANIC — de · nl · af — and no other.
PREDICTION  Afrikaans is verb-final West Germanic ⇒ BOTH should bite.
RESULT, quoted from the committed file:
  `game.aiPlayedFor.before`  ⛔ BITES. "the Afrikaans PERFECT puts its participle at the very end of the
     clause … which those two spans cannot express."
     ⭐ AND ITS ESCAPE IS NEITHER GERMAN'S NOR DUTCH'S. Both fell back to the SIMPLE PAST (`spielte`,
       `scoorde`); Afrikaans has a well-formed simple past for only a handful of verbs — `was had kon wou
       moes sou wis` — and `behaal` is not among them, "so that escape does not exist". It used the
       PRESENT, which is finite and therefore verb-second: "Die AI behaal 34 punte". The cost is a TENSE
       rather than a REGISTER.
  `board.reset`  ✔ DOES NOT BITE, and the file states why rather than inheriting it: `herstel` is
     INSEPARABLE so nothing is stranded, and the imperative and infinitive are the same string so there is
     no style to abandon. "A separable choice such as `stel terug` WOULD have bitten, which is why this
     one was made deliberately."
⇒ THE MECHANISM NOW HOLDS ON FIVE LANGUAGES WITH A REASON RATHER THAN A VOTE, and it is refined once
  more: the constraint is on a CLAUSE-FINAL PARTICIPLE, so the escape available to a language depends on
  what finite tenses it has — which is why three verb-final languages needed three different answers.
```

## 6. 🐞 One more ORCHESTRATOR count error, and the file caught it

```text
THE FILE SAYS: five predecessors ship the `\u00A0` escape — sk · cs · pl · pt · sv.
MY PROMPT §5.3 SAID: four — sk · cs · pl · pt.
✔ THE FILE IS RIGHT. Verified by enumerating the DIRECTORY: `messages.sv.ts`'s `landing.footnote` carries
  `279\u00A0496`. My generating loop iterated a HAND-TYPED list `en sk cs pl de pt is it nl da` — it
  omitted `sv`, which had landed one commit earlier.
⇒ THIS IS THE THIRD MEMBER OF ONE FAMILY AND EACH FIX EXPOSED THE NEXT:
    §46.2  five claims asserted from memory        → fix: GENERATE BY COMMAND
    §48.1  asked a library what a file should hold  → fix (R-P): READ THE FILE
    HERE   read the files, but TYPED the file list  → fix: ENUMERATE THE INPUTS FROM THE FILESYSTEM
⭐ R-P is extended rather than replaced: read the file, AND let the shell produce the list of files. A
  hand-typed enumeration is a memory claim wearing a command's clothes.
⚠ Note that Swedish's OWN comment also says four — correctly, because it was the fifth and was writing
  about its predecessors. The Afrikaans catalog counted the set that existed when it ran. Both are right
  and only my prompt was wrong.
```

## 7. ⛔ WHAT IS PERMANENTLY LOST, stated plainly

An interruption companion must not invent what the Worker would have said. These are gone:

```text
· the Worker's own FLAGGED RISKS list — which strings it was least sure of, and which labels it believed
  might overflow. ⚠ Every predecessor produced sixteen to twenty-six such items. For this catalog the
  only surviving risk signals are what it chose to comment in the file. ⛔ THIS IS THE REAL LOSS.
· its ORCHESTRATION CRITIQUE. Seven catalogs returned sixty-five findings against the prompt skeleton,
  three of them defects the ORCHESTRATOR had introduced. The eighth catalog's findings do not exist, and
  ⛔ the two the file happens to reveal (§6's separator count, and the cast-pattern non-firing) were found
  by the ORCHESTRATOR reading the file rather than by the Worker telling anyone.
· ⛔ SECTION 12 — `What the wiring slice needs to know`. The one thing no other catalog was asked for,
  requested precisely because this was the LAST Worker to see the whole key set before wiring. ⇒ THAT
  OBSERVATION SET IS UNRECOVERABLE. The wiring slice proceeds without it.
· its byte-identical-to-Dutch COUNT (§4 Rule B) and its byte-identical-to-English count.
· its context-pressure line, its near-miss record, and its own statement of which of the four call sites
  it considered load-bearing.
⚠ AND ONE THING THAT IS *NOT* LOST, because the file carries it: every per-site call-site verdict, with
  the structural reason, commented at the key.
```

## 8. Disposition

```text
· Session ordinal 17 is CONSUMED. Catalog 8 is complete; there is no session-17 exchange 02.
· The file is committed and published at `0a4fcc2`. It is NOT re-authored and NOT re-verified by a Worker:
  re-running an 8-of-8 catalog to obtain a report would spend a full exchange to recover prose about work
  that is already measured green, and would produce a SECOND authoring of the same 316 strings whose
  differences from the first nobody could adjudicate.
· ⛔ The authoring step is now UNATTRIBUTED as well as non-independent. Recorded here, in the commit
  message, and in `00_notes.md` §49 so no later artifact can imply a Worker signed off on this file.
· The DEFERRED-ACCEPTANCE entry for this catalog (B14) is written from the FILE and from the
  ORCHESTRATOR's measurements, and it says so.
· ⭐ FOR THE WIRING SLICE: assume it has NO section-12 observations from the last catalog, and budget the
  reconnaissance it would have saved.
```

**This companion grants nothing and certifies nothing. It records that an exchange ended without a report
and what was measured in its place.**

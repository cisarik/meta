# AP_DEFECTS.md — measured defects of the Analytic Programming protocol

Artifact class: **defect report against the protocol itself. Evidence and analysis, not
authority.** It grants nothing. It exists to be consumed by a protocol-update task that fixes
`AP.md` and its projections.

```text
Written           2026-09-04
Written by        the ORCHESTRATOR of Libre Tiles logical whole 13/00 multilingual-expansion-campaign
Governing AP pin  9c5cc44f8b6c92dd56ad2427d13223d7d59c5656   (.ap gitlink of /home/agile/Projects/libretiles)
Evidence scope    ⛔ ONE SESSION ONLY. Every defect below was observed, measured or caused by me
                  inside that single logical whole. Nothing here is inherited folklore.
Consumer          a future Orchestrator or Cooperator running an AP protocol-update task
Retention         until each defect is either fixed in AP or explicitly rejected with a reason
Cleanup owner     the COOPERATOR
```

## 0. How to use this file without reading the Meta archive

⛔ **Do not read `/home/agile/meta` to verify this.** It is tens of thousands of lines. Every
claim below cites its evidence by `file:line`, and the citations are all inside **one directory**:

```text
/home/agile/meta/projects/libretiles/13/00-multilingual-expansion-campaign/
    00_notes.md                the Orchestrator decision record. Every prompt defect I caused is
                               written up there with its measurement. This is the primary evidence.
    03_report_00.md            Worker BLOCKED report — four prompt defects, zero mutation
    04_report_00.md            Worker BLOCKED report — a forced logical contradiction
    05_report_00.md            Worker PASS report — two more guard spellings my inventory missed
    92_c1_design.md            an Orchestrator-direct design record, written instead of a planner
```

⚠ **Staleness rule, inherited from `AP_DESTILLED.md:62-65` and it applies to this file too.** Before
trusting a line number here, check that `00_notes.md` still contains the quoted heading text.
**Headings are the durable key; line numbers are not.** Every citation below therefore names the
heading, not only the number.

## 1. Where this came from, and the one word that changed it

The Cooperator's instruction on 2026-09-03, mid-session, after two exchanges had produced a great
deal of protocol ceremony and no product:

> *Na trivialne ulohy nepotrebujes Workerov, si Agent Orchestrator a mas write pristup … vela vela
> vela zbytocnych tokenov. **Chceme uderny vyvoj.***

**Measured effect of that one word.** Before it, in this same whole: two exchanges, each a full
Worker session, each reading ~145 KB of protocol, each running the complete eight-gate ladder,
producing **five documentation lines and two tests**. After it: **eight new playable languages
committed directly by the Orchestrator**, each with a reproducible pinned build, a licence read
before a byte was written, and byte-exact `--check` reproduction —
`00_notes.md` sections 13 through 25.

⇒ That contrast is the source of most of what follows. **The protocol was not wrong about rigor. It
was wrong about cost.**

---

## 2. The defect index

```text
D-01  the Worker never critiques the Orchestrator — AP's most productive mechanism is not in AP
D-02  report volume is unbounded and unpriced
D-03  a project rule can turn AP's own anti-pattern into a mandatory tax
D-04  the Orchestrator is asked to self-check for omissions it structurally cannot see
D-05  the three-role model cannot name what an executing Orchestrator is
D-06  sub-agents are prohibited-by-default, which is backwards for everything except independence
D-07  no per-role reading floor, so the safe default is "read the whole protocol"
D-08  the name and ceremony of "Analytic Programming" bias toward analysis as the deliverable
D-09  rigor is selected by consequence; COST is never selected at all
D-10  independence is binary, so the only way to get any is the most expensive one
D-11  a prompt defect has no in-band repair — the only remedies are block or reissue
D-12  the evidence tier drives validation but not report shape, so E1 work files E3-shaped reports
```

⚠ **My intuition about which of these matter most**, stated plainly and separately from the
evidence, because the Cooperator asked for it:

```text
BIGGEST      D-01. Everything good in this session came through a report field AP does not require.
             If exactly one thing is fixed, fix this one.
SECOND       D-09 with D-02 and D-12. They are one defect wearing three faces: AP prices rigor and
             never prices anything else, so the ceremony grows without limit and nobody is wrong.
THIRD        D-04 with D-11. Three consecutive exchanges failed on MY enumeration, and AP's only
             answer was "the Orchestrator should have reviewed its own omissions". That is not a
             mechanism, it is a wish.
UNDERRATED   D-05. The naming problem looks cosmetic and is not: because AP has no word for an
             executing Orchestrator, the project had to invent a local grant with a permanent
             evidence penalty, and two different informal names now compete for it.
```

---

## D-01 · The Worker never critiques the Orchestrator, and AP's most productive mechanism is not in AP

### The defect

AP models the Worker as an executor that returns evidence and stops. `AP.md:80-81`: *"executes ONE
bounded task under ONE complete prompt, validates, returns evidence, stops."* The report's compact
core (`PROMPT_CONTRACTS.md:22-36`) has eleven items, and **not one of them asks the Worker whether
the prompt was any good, whether the approach was sound, or whether the Orchestrator's plan can
reach the stated goal.** Item 8 is "deviations, risks, missing evidence" — about the WORK. Item 9 is
"one smallest next step" — about the FUTURE. Neither is a critique of the ORCHESTRATION.

### The evidence — twelve Orchestrator defects, all caught by a non-required report field

Every prompt I issued ended with a field AP does not define:

```text
⚠ WHAT YOU CAN STILL SEE THAT THIS PROMPT DID NOT ANTICIPATE
   Two separate labelled lists: MEASURED and LEAD.
```

What it returned, in one whole:

```text
00_notes.md  "### 9.2 🐞 PROMPT DEFECT E1-D1 — mine, caught by the Worker"          (line ~498)
    I asserted backend/.env.example was ASCII-only. It carries three U+2014 em dashes. A premise
    stated as measured that was never measured.
00_notes.md  "### 28.1 🐞 PROMPT DEFECT E1-D2 — an absence claim short by two sites"  (line ~1532)
    I wrote "eight guard sites" from a hand list. Two more existed IN THE SAME FUNCTION, spelled as
    regexes. Removing the ones I named would have been a COMPLETE NO-OP while eight gates went green.
00_notes.md  "### 28.2 🐞 PROMPT DEFECT E1-D3 — a stage gate that could not be satisfied" (~1558)
    I required a client-side test to pass before commit and allowlisted no file the test runner
    collects.
00_notes.md  "### 28.3 🐞 PROMPT DEFECT E1-D4 — two file paths that do not exist"      (~1569)
00_notes.md  "### 28.4 🐞 PROMPT DEFECT E1-D5 — section 6 undercounted..."             (~1582)
00_notes.md  "### 28.5 ⛔ THE FINDING — the AI's own board view is worse than the wire" (~1598)
    A whole class of corruption I had missed: a digraph makes an AI-facing board row sixteen
    characters and silently shifts every column. The human would see the board correctly and the
    MODEL would see a wrong one.
00_notes.md  "### 29.1 🐞 C-7 — an assertion that CANNOT coexist with the requirement" (~1697)
    A test asserted the serializer rejects "CH"; "CH" is structurally identical to "SZ", which the
    task required accepting. Arithmetically un-completable, and the file was off my allowlist.
00_notes.md  "### 29.2 🐞 C-8 — my predicate vocabulary accepts a DIGIT as a tile letter" (~1721)
00_notes.md  "### 29.3 🐞 MEASURED-2 — an EIGHTH guard, spelled differently"           (~1736)
00_notes.md  "### 30.2 ⛔ A SEVENTH AND EIGHTH SPELLING"                               (~1883)
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("") — a blank can never be assigned a digraph FROM THE
    PRODUCT. Unreachable by any pattern I had written.
00_notes.md  "### 30.3 The other findings, dispositioned"                              (~1918)
    My assertion count was short by five, and I attributed a line to the wrong file AGAIN.
```

⇒ **Twelve defects. Every one mine. Every one surfaced by a field the protocol does not require.**
Two Workers returned `BLOCKED` with **zero mutation** rather than execute a defective grant —
`03_report_00.md` and `04_report_00.md` — and both were right.

### Why AP permits this

AP's anti-pattern list warns the Orchestrator against *its own* errors
(`AP.md:2487-2578`, and `AP_DESTILLED.md:752-794` distils twelve of them). Its readiness review
(`AP.md:1328-1347`) asks the Orchestrator to perform *"contradiction and omission review"* — **on
itself, before issuing.** So the protocol's entire defence against Orchestrator error is
Orchestrator self-review. `AP_DESTILLED.md:791-793` records the useful field as project folklore —
*"Keep the report field that asks what the Worker can still see"* — explicitly as one project's
lesson, not as a protocol requirement.

### ⭐ Proposed fix

**Add a required compact-core item: `Orchestration critique`.** Not optional, not an annex, not
project folklore.

```text
Orchestration critique: none | <findings>
  Two labelled lists, MEASURED and LEAD.
  MEASURED — you ran something and it produced that result.
  LEAD     — you suspect it and have not proved it.
  Scope: the PROMPT, the APPROACH, the SEQUENCING and the STATED GOAL — not only the code.
  ⛔ `none` is permitted but must be a considered answer, not a default.
```

And add, as a Worker responsibility in `AP.md:1406-1441`:

> The Worker analyses the grant before executing it and the approach after executing it. Finding a
> defect in the Orchestrator's prompt, plan or sequencing is **part of the task**, not a courtesy.
> A Worker that executes a defective grant faithfully has failed.

⚠ **And keep it punchy.** The value came from the two labels and the strict MEASURED/LEAD
separation, not from length. A defect I once acted on arrived as an unlabelled LEAD and became a
production error — `00_notes.md` records it as prompt defect D2 of the previous era. **The labels
are the mechanism; the prose is not.**

---

## D-02 · Report volume is unbounded and unpriced

### The defect

`PROMPT_CONTRACTS.md:63-64` says *"Summarize command execution. Include full output only for
failures, unexpected state, safety-critical evidence, or explicit Orchestrator request."* That last
clause is the hole: **the Orchestrator may request anything, and nothing limits how much.** Combined
with an eleven-item compact core, two conditional sections, and any activated annexes, a report has
no ceiling.

### The evidence

```text
04_report_00.md   237 lines, and that is AFTER I condensed it
05_report_00.md   663 lines, condensed — the Orchestrator note at its head says so explicitly
```

My own prompt for exchange 05/01 required, verbatim:

> *the output of ALL SIX section-3 commands, BEFORE and AFTER, verbatim*

⇒ Twelve command outputs quoted in full, in a report about a change whose whole diff is
`+483 −99`. And the delivery mechanism broke on it: the Cooperator hit
`Received message_start for message … while message … is still open` **twice**, once on a subagent's
report and once on my own output. `00_notes.md` section 30 records the first; the Cooperator reported
the second directly and instructed me to write in small appends.

⚠ **The failure was not cosmetic. It cost a whole dispatch.** `00_notes.md` section 30 records that
I had to verify nothing had begun and re-deliver the same exchange ordinal.

### Why AP permits it

AP prices exactly one thing: reasoning. `AP.md:1074-1080` gives a reasoning table with *"Medium is
the default … High needs a named risk … Extra High is exceptional."* **There is no equivalent table
for evidence volume, report volume or reading volume.** So "more evidence" is always defensible and
"less evidence" always needs a justification — a one-way ratchet.

### ⭐ Proposed fix

**Tie report shape to the evidence tier, in `PROMPT_CONTRACTS.md` beside the compact core:**

```text
E0 / E1   the compact core only. No quoted command output unless a gate FAILED.
E2        the compact core plus the specific evidence the named decision risk requires.
E3 / E4   structured and unbounded, but each quoted block must name WHICH risk claim it decides.
⛔ An Orchestrator request for full output must name the risk claim it settles. A request that
   cannot name one is over-collection and the Worker should say so under `Orchestration critique`.
```

⚠ And a hard mechanical rule earned by this session: **write long artifacts in appends against a
sentinel, never as one generation.** The Cooperator diagnosed this in a previous era and it held for
nine exchanges; I violated it and reproduced the failure twice.

---

## D-03 · A project rule can turn AP's own anti-pattern into a mandatory tax

### The defect

`AP.md:1112-1119` (E2) says a broad or full suite is used *"ONLY on a project rule or a named
decision risk"*. `AP.md:2487-2578` lists as an anti-pattern: *"treating a full or repository-wide
suite as an automatic Worker tax."* **Those two sentences are in tension, and the project rule wins
silently.** Libre Tiles declares "all eight standing gates green on every slice", so the anti-pattern
is unreachable: every exchange pays the full tax, by rule, with AP's blessing.

### The evidence

```text
03_report_00.md   ran the complete eight-gate ladder — including a ~4.5-minute pytest and a full
                  Next.js production build — and returned BLOCKED with ZERO mutation.
04_report_00.md   ran the complete eight-gate ladder again. BLOCKED again. ZERO mutation again.
```

⇒ **Two full validation ladders to produce no product change.** Both reports state it plainly:
`04_report_00.md` calls its run *"a baseline attestation, not validation of a change (there is
none)"*. That is the protocol paying for evidence about a tree nobody touched.

### ⭐ Proposed fix

**A validation-proportionality rule, keyed to what the exchange actually did:**

```text
zero mutation (BLOCKED, probe, audit, reconnaissance)
    -> the REPOSITORY GATE only. ⛔ A gate ladder over an unmodified tree proves nothing about the
       exchange; it re-proves the baseline, which the previous exchange already proved.
mutation confined to documentation or one test file
    -> the gates that can possibly move, named in the prompt with a why
mutation touching runtime code, an asset, or a shared surface
    -> the project's full standing set
```

And a sentence for `AP.md` beside the E2 row:

> A project rule that mandates a broad suite applies to exchanges that MUTATE. An exchange that
> ends without mutation satisfies it by reporting the repository gate and the reason no mutation
> occurred.

---

## D-04 · The Orchestrator is asked to self-check for omissions it structurally cannot see

### The defect

`AP.md:1328-1347`, the prompt-synthesis readiness review, ends with *"contradiction and omission
review"*. **An omission review performed by the author of the omission is not a control.** You cannot
grep for the spelling you did not think of.

### The evidence — three consecutive exchanges, the same root cause, each time a different spelling

```text
attempt 1  I enumerated "eight guard sites" from a hand list.
           MISSED: two `^…$`-anchored \p{L} regexes in the same function. Removing the sites I named
           would have been a NO-OP.                          00_notes.md "### 28.1" (~1532)
attempt 2  I fixed it by DERIVING the count from a search — and my pattern was still too narrow.
           MISSED: a DRF `max_length=1`, invisible to a search for `len(x) == 1`. That guard sits on
           the exchange endpoint, so the slice would have shipped with digraph exchange still
           returning HTTP 400.                               00_notes.md "### 29.3" (~1736)
attempt 3  I fixed THAT by enumerating a six-spelling space, running all six repo-wide, and
           classifying all twenty-seven hits.
           MISSED: `"ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")` in the blank-picker UI — no `len`, no
           `.length`, no `max_length`, no `\p{L}`, no `charAt`. A blank can therefore never be
           assigned a digraph FROM THE PRODUCT, however correct the wire, serializer and engine are.
                                                             00_notes.md "### 30.2" (~1883)
```

⇒ **Three iterations of the same control, each stronger, each still incomplete.** My own rule went
through three versions (`00_notes.md` R-J at ~1752 and ~1911) before arriving at the only formulation
that survives contact:

> **An enumeration handed to a Worker is a HYPOTHESIS, not a specification.**

### ⭐ Proposed fix

**Give an enumeration a protocol status, and make widening it a Worker obligation rather than an
Orchestrator aspiration.** Add to the prompt-construction contract:

```text
Enumeration status: hypothesis | exhaustive-by-construction
  `hypothesis` is the DEFAULT and the honest value for any list of sites, files, call sites or
  spellings that the Orchestrator produced by searching.
  The prompt must carry THE COMMAND that produced it, so the Worker can re-run and disagree.
  `exhaustive-by-construction` is claimable only when the set is closed by the language or the
  type system — e.g. every member of an enum, every field of a dataclass — and the prompt must
  say which construction closes it.
```

Paired with a required report field:

```text
Enumeration widened: none | <sites the prompt's own commands could not reach>
```

⚠ **The asymmetry is the point.** An Orchestrator reviewing its own omissions is checking a set
against itself. A Worker widening the pattern is checking the set against the repository. Only the
second can find a spelling nobody thought of — and it found one on all three attempts.

---

## D-05 · The three-role model cannot name what an executing Orchestrator is

### The defect

`AP.md:548-583` fixes three persistent roles and states that *"Worker session profiles, phases, and
clients create no additional persistent roles."* But this session's productive mode was an
Orchestrator that **executes** — twelve languages, eleven build scripts, and every commit but one
authored directly, with no Worker involved.

AP's only accommodation is a project-local escape hatch. `AP_DESTILLED.md:205-213`:

> *Project overlay for Libre Tiles. Cooperator decisions 12 and 13 widen this … That is a
> **project-local** grant, not universal AP, and it carries a five-item bar plus a permanent evidence
> penalty.*

⇒ So the thing that produced almost all of this session's output exists in AP only as **a
non-standard local exception with a permanent penalty attached.**

### The evidence — the naming has already forked twice, informally

```text
"Agent Orchestrator"    the COOPERATOR's term for me, used throughout this session.
                        ⛔ MEASURED ABSENT from the governing pin: AP_DESTILLED.md:47-48 records
                        that `grep -rn "Agent Orchestrator" *.md` in the pin returns ZERO lines.
"Worker Orchestrator"   the term the previous era's handout used for an experimental profile.
                        Also absent from the pin.
```

The Cooperator's own diagnosis, and I agree with it:

> *"Agent Orchestrator" nefunguje pretoze z nazvu vyplyva proste ze je to Orchestrator ktory deleguje
> Workerov. Prosim toto moze byt moj defekt — problematicke nazvoslovie.*

⚠ **It is not his defect. It is AP's.** Two informal names competing for one real thing is what
happens when the model has no word for it.

### ⭐ Proposed fix

**Do not add a fourth role — that would break `AP.md:548-583` for a naming problem.** Add an
**execution mode of the Orchestrator role**, and name it after what it does rather than after which
agent runs it:

```text
Execution mode: orchestrator-direct | worker-delegated
  `orchestrator-direct` — the ORCHESTRATOR performs the mutation itself under its own prompt-equivalent
  written into the trace. It is still the ORCHESTRATOR role; no new persistent role exists.
  ⛔ Its evidence is PERMANENTLY non-independent and every artifact it produces says so.
  ⛔ It is unavailable for anything requiring independence, and for E3/E4 mutation.
  It is the DEFAULT for E0/E1 work whose blast radius is one file and whose failure is reversible.
```

And retire both informal names in `GLOSSARY.md`:

```text
"Agent Orchestrator"   deprecated. Says nothing the role name does not, and implies delegation.
"Worker Orchestrator"  deprecated. Reads as a fourth role and is not one.
                       -> use: ORCHESTRATOR in `orchestrator-direct` execution mode.
```

⚠ And record the honest cost, because this session paid it: **twelve commits of language work carry
a permanent non-independence mark.** That is the correct price and it should be visible, not hidden
behind a name that sounds like delegation happened.

---

## D-06 · Sub-agents are prohibited-by-default, which is backwards for everything except independence

### The defect

`AP_DESTILLED.md:455-462`, quoting the pin at `AP.md:1249-1252` and
`PROMPT_CONTRACTS.md:845, :868, :949`:

> *sub-agents, internal delegation, Explore-style tasks, and parallel topology are `not-used` unless
> explicitly authorized; internal delegation remains one accountable WORKER and never establishes
> independent audit.*

**Two different rules are welded into one prohibition, and only one of them is right.**

```text
RIGHT   internal delegation never establishes INDEPENDENT AUDIT. Keep this. It is load-bearing and
        this session depends on it: C1 is E3 and its acceptance cannot be my subagent.
WRONG   sub-agents are `not-used unless explicitly authorized` as a DELIVERY MECHANISM. That makes
        the thing that works require a boilerplate authorization line in every prompt.
```

### The evidence

Every prompt I issued carried the same ceremonial line, because the pin requires it:

```text
Sub-agents/internal delegation: bounded authority — delivery route only; you remain the one
accountable Worker and must not delegate further
```

⇒ Nine prompts, nine identical authorizations of a mechanism that is the *normal* route in this
environment. Meanwhile the pin's own author already moved: `AP_DESTILLED.md:47-54` records that the
newer sibling **formalizes default subagent dispatch in RF-02, AP §3 and INTUITION §4**, while the
governing pin *"has no 'default dispatch' rule"*. **The pin is behind the practice, and a consumer
that follows the pin pays a boilerplate tax to do the ordinary thing.**

### ⭐ Proposed fix

**Split the sentence.**

```text
Delivery route: the ORCHESTRATOR selects it and it grants nothing. Subagent delivery needs no
    special authorization, because delivery is not authority — the PROMPT is (AP.md:917-925).
Independence: internal delegation, subagent delivery, and any session inheriting the Orchestrator's
    context NEVER establish independent audit. Unchanged, and it must stay unchanged.
```

⚠ The Cooperator's own framing supports exactly this split: *"moze ich by vela kedze uz nesluzim ako
poslicek"* — many of them, because he is no longer the messenger. **The bottleneck AP was protecting
against was a human courier, and that bottleneck is gone.** What remains worth protecting is
independence, and that is a separate sentence.

---

## D-07 · No per-role reading floor, so the safe default is "read the whole protocol"

### The defect

`AP_DESTILLED.md:55-57` records the gap explicitly:

> *The pin has no "Per-Role Minimum-Reading Spine" and no "Rule Detectability Classes". Section 2
> below therefore states a reading floor as ADVICE, clearly labelled, not as an AP requirement.*

⇒ With no floor, the only defensible instruction is "read it all". So every prompt I wrote said:

```text
Mandatory reading:
    /home/agile/Projects/libretiles/.ap/AP.md          the governing pinned protocol
    /home/agile/Projects/libretiles/.ap/AP_WORKER.md   your operational projection
```

### The evidence

`AP.md` at this pin is **2591 lines / ~145 KB** (`AP_DESTILLED.md:33`). A Worker whose entire task
was correcting five documentation lines in a product spec read all of it. The measured cost of that
first exchange is in `00_notes.md` section 13:

> *each spawned a fresh Worker that read `AP.md` (145 KB), `AP_WORKER.md`, `AGENTS.md` and a 400-line
> prompt, ran the full four-minute suite, and then **I re-ran all eight gates again myself** —
> duplicate verification producing zero additional information on a five-line documentation edit.*

### ⭐ Proposed fix

**Grant by citation, not by document.** The Orchestrator already knows which rules the task touches;
it should hand over the line ranges and nothing else. The newer sibling calls this P19 "Dense Grant
by Citation" and the pin lacks it (`AP_DESTILLED.md:58-59`).

```text
AP lines you need for THIS task:
    AP.md:917-932       task authority, and that omitted permission is not implied
    AP.md:2466-2486     your stopping conditions
    AP_WORKER.md:147-163 before mutation
    PROMPT_CONTRACTS.md:14-36  the report contract you must satisfy
⛔ You are NOT required to read the rest of AP. If this prompt and AP disagree, AP wins — stop and
   report the conflict rather than resolving it.
```

⚠ **The escape clause is what makes the citation safe.** A Worker given four line ranges cannot know
what it was not shown, so the prompt must make "AP wins, stop and report" explicit. That single
sentence converts a reading shortcut into a fail-closed one.

⚠ **And `AP_DESTILLED.md` is itself the proof the technique works.** It is 942 lines that replaced
~6000 lines of protocol reading for a fresh Orchestrator, by citing rather than recopying. The same
move has simply never been made for the Worker.

---

## D-08 · The name and the ceremony bias toward analysis as the deliverable

### The defect

The protocol is called **Analytic** Programming, and its structure rewards analysis: nineteen rule
families, five PASS results none of which closes anything (`AP.md:445-460`), a readiness review with
twenty-two checks (`AP.md:1328-1347`), a report with eleven mandatory items. AP does contain the
correct instinct — `AP.md:1366-1370`: *"more analysis" is not a closure decision* — but it appears
once, as a closure rule, while the ceremony pulls the other way on every exchange.

### The evidence

The Cooperator did not ask for less rigor. He asked for a different *target*, and named it:

> *teraz klucove slovo bolo "uderne" to zmenilo vyvoj na smerovanie k cielu namiesto vela zbytocneho
> kodu, privela pisania testov a privela testovania*

Measured, in one whole:

```text
BEFORE the word    2 exchanges · 2 full gate ladders · ~290 KB of protocol read · 5 documentation
                   lines and 2 tests shipped
AFTER the word     8 languages shipped playable, each with a pinned reproducible build and a licence
                   read before any byte was written — 00_notes.md sections 15, 17, 19, 21, 23, 25
```

⚠ **And rigor went UP, not down.** In the punchy phase the guards caught more, not less:

```text
Swedish   I first folded Ü and it was WRONG — it would have made `müsli` playable as MUSLI, a rule
          that edition does not have. Caught by reading the source BEFORE writing the script, and
          then asserted in two places.                        00_notes.md "### 25.1"
Danish    `errors="strict"` refused to decode eleven lines the expander had truncated mid-character.
          My own exploratory pass had used `errors="replace"` and SAW NOTHING.  00_notes.md "### 23.2"
French    BLOCKED and not shipped: the expander yields ~77 000 playable words against an official
          lexicon of order 400 000. A variant that rejects most valid French words is a defect that
          looks like a feature.                                00_notes.md "### 19.3"
Norwegian BLOCKED on licence clarity: the one explicit licence statement in the directory grants for
          the HYPHENATION files, not the word list.            00_notes.md "### 23.3"
```

⇒ **Punchy did not mean loose.** It meant the evidence was spent on the thing that could actually be
wrong, instead of on re-attesting a baseline.

### ⭐ Proposed fix

Two changes, one to the text and one to the vocabulary.

```text
1  State the deliverable in AP's own opening. Something like:
     "The deliverable of an AP exchange is a LANDED, VERIFIED CHANGE — or an explicit, evidenced
      decision not to make one. Analysis is the means. An exchange that produces neither has
      produced nothing, however complete its record."
   ⚠ This is not a new rule. It is AP.md:1366-1370 promoted from a closure footnote to a premise.

2  Make PUNCHINESS a first-class, named property of a prompt, with a definition:
     "A punchy prompt states one outcome, the smallest authority that reaches it, and the smallest
      evidence that would falsify it. It cites rather than recopies. It asks for no attestation
      about a thing it did not change."
   -> add it to the readiness review at AP.md:1328-1347 as a check, not a virtue.
```

⚠ **On renaming the protocol: I recommend against it.** "AP" is pinned into a submodule, a managed
`AGENTS.md` block, and every historical artifact; a rename is a large migration for a framing
problem that two paragraphs of text can fix. **Fix the framing, keep the name.**

---

## D-09 · Rigor is selected by consequence; COST is never selected at all

### The defect

This is D-02, D-03, D-07 and D-12 seen from one place, and I believe it is the root.

AP selects rigor beautifully. `AP.md:1112-1123`: pick the **highest triggered** tier by consequence,
not by file count. `AP.md:1074-1080`: lowest sufficient reasoning, High needs a named risk.

**But nothing selects cost.** There is no "lowest sufficient evidence volume", no "lowest sufficient
reading", no "lowest sufficient report", and no rule anywhere that an exchange's overhead should bear
any relation to its blast radius. So every cost question has exactly one safe answer — *more* — and
the person who says "less" carries the whole burden of proof.

### The evidence

```text
· two full gate ladders spent on exchanges that changed nothing            03_report_00.md, 04_report_00.md
· 145 KB of protocol read to correct five documentation lines              00_notes.md section 13
· a report so large it broke the delivery channel, twice                   00_notes.md section 30
· in the PREVIOUS era, two dispatch failures on an account balance —
  recorded in that era's handout as "prefer fewer, larger grants", which is
  a workaround for a cost the protocol never modelled
```

⇒ And the correction, when it came, came from the Cooperator as a **product** instruction rather than
from AP as a **protocol** rule. That is the defect in one sentence: **AP made the expensive choice
the default and left the cheap choice to be authorized by a human.**

### ⭐ Proposed fix

**Add a cost dimension beside the evidence tier, selected the same way — by consequence.**

```text
Overhead budget: minimal | proportionate | full
  minimal        E0/E1, reversible, one file. Repository gate + the gates that can move. Compact-core
                 report only. AP by citation. No attestation about untouched surfaces.
  proportionate  E2. The named decision risk drives which evidence is collected, and the prompt says
                 which risk each item settles.
  full           E3/E4. Everything AP requires, and the report says why each block was needed.
⛔ Selected by CONSEQUENCE, exactly like the evidence tier — never by how important the task feels.
⛔ An Orchestrator that cannot name what a piece of evidence would falsify is over-collecting, and
   the Worker should say so under `Orchestration critique` (D-01).
```

⚠ **This is the one fix I would make first if D-01 were already done.** D-01 makes defects visible;
D-09 stops the protocol from manufacturing them.

---

## D-10 · Independence is binary, so the only way to get any is the most expensive one

### The defect

`AP_DESTILLED.md:433-438` states it as a hard partition:

```text
same-session self-review, tests, diff reading, diagnostics  = USEFUL, NON-INDEPENDENT
a new profile label in the same session                     = NOT independence
internal delegation inside one Worker run                   = NOT independence
a session inheriting your conversation or reasoning         = NOT FRESH at all
```

⇒ Everything an Orchestrator can reach on its own is on the wrong side of the line. **So the first
unit of independent signal available costs a human copy-paste into a session the Orchestrator cannot
open.** There is nothing cheaper, and therefore nothing earlier.

### The evidence

C1 is E3. Its acceptance prompt is `06_acceptance_00.md`, and it is the **only artifact in this whole
session that I had to hand to the Cooperator to execute.** Everything else — twelve languages, three
C1a attempts, every commit — ran without him. `00_notes.md` section 30.1 states the position:

> *⛔ And that is ALL it is. C1 is E3. The fresh independent acceptance is still owed, it must come
> from a session that did not implement this, and it cannot be my subagent … That is the one thing in
> this whole campaign I can neither execute nor delegate.*

⚠ **The binary rule is CORRECT and I am not asking to weaken it.** A subagent I spawn inherits my
framing whether or not it inherits my transcript, and calling that independent would be a lie. The
defect is that AP names only the two endpoints, so an Orchestrator has no way to buy a *little*
scrutiny early and cheaply.

### ⭐ Proposed fix

**Name the middle, and forbid it from ever substituting for the endpoint.**

```text
Scrutiny class, and it is NOT the same axis as independence:
  self-review              same session. Zero scrutiny value beyond catching slips.
  context-isolated review   a delivery session given the CANDIDATE and the ACCEPTANCE CRITERIA and
                            explicitly NOT the design rationale, the prompt history, or the
                            Orchestrator's reasoning. Cheap, available immediately, and it does find
                            things — because it cannot see what the author was thinking.
                            ⛔ NOT independence. NEVER satisfies an E3/E4 acceptance requirement.
                            ⛔ Must be labelled `context-isolated, non-independent` in every artifact.
  fresh independent audit   a session the Orchestrator did not create and cannot see into.
                            The ONLY thing that satisfies E3/E4. Unchanged.
```

⚠ **The evidence that the middle class has value is in this session, by accident.** My three C1a
Workers were subagents — non-independent by rule — and they found twelve of my defects anyway,
precisely because each was given the prompt and not my reasoning. **AP currently has no name for
what those exchanges produced, so it has no way to ask for it deliberately.**

---

## D-11 · A prompt defect has no in-band repair

### The defect

`AP.md:917-925` makes the prompt the sole source of Worker authority, and `AP.md:932` adds *"omitted
permission is not implied permission."* Correct, and together they mean a defective prompt has exactly
two lawful outcomes: **the Worker blocks, or the Worker improvises (forbidden).**

AP nearly has the instrument. `PROMPT_CONTRACTS.md:68-82`, the repeated-blocker capsule, contains:

```text
Smallest authority expansion needed: <minimum or none>
```

⇒ **But it appears only on the SECOND consecutive block, and it is a report FIELD, not a grant
MECHANISM.** Even with the answer written down, the Orchestrator must regenerate a complete prompt.

### The evidence

```text
03/01  BLOCKED. Needed: one more allowlisted path (a test host) and two more guard sites named.
04/01  BLOCKED. Needed: one more allowlisted path (a test file) and one predicate clause.
05/01  PASS.
```

⇒ **Three full prompts — roughly 1200 lines of authored authority — to land one commit.** Two of the
three blocks were resolved by adding **one path and one clause**. And each reissue was a fresh
generation, per the standing rule that a prompt must never be string-patched
(`AP_DESTILLED.md:762-764`) — a rule that exists for a real reason and here multiplied the cost.

⚠ Note what did NOT go wrong: the Workers were right both times, and blocking was the correct
behaviour. **The defect is the repair path, not the block.**

### ⭐ Proposed fix

**A bounded amendment instrument, small enough to be safe.**

```text
AMENDMENT — issued against an existing exchange, does NOT open a new one
  Amends exchange: <logical whole · session · exchange>
  Amendment basis: worker-identified-missing-authority | orchestrator-identified-defect
  Adds to allowlist: <zero or more exact paths>
  Adds to authority: <zero or more exact sentences>
  Removes: nothing. ⛔ An amendment may only ADD. Any removal or change of meaning requires a
           complete reissue, because a Worker may already have acted on what is there.
  Everything else in the amended prompt stands unchanged.
  Coordinates: UNCHANGED. An amendment is not an exchange and consumes no ordinal.
  ⛔ At most ONE amendment per exchange. A second means the prompt is wrong in kind, not in
     extent, and it must be reissued whole.
```

⚠ **Why "may only ADD" is the safety property.** A Worker that has already read the prompt cannot be
made to un-read a permission. An additive amendment cannot invalidate work already done, so it needs
no re-gate; a subtractive one could, and therefore must not exist.

⚠ And it preserves the rule that matters: **the amendment is still authored by the Orchestrator and
still explicit.** The Worker asks; it never assumes.

---

## D-12 · The evidence tier drives validation but not report shape

### The defect

`AP.md:1112-1119` maps E0–E4 to *validation*. Nothing maps a tier to the **report**. So the
eleven-item compact core, both conditional sections, and every activated annex apply identically to a
five-line documentation fix and to a wire-format change over live multiplayer.

### The evidence

```text
exchange 01/01   tier E1. Two documentation files and one grep-shaped test.
                 Report: the full compact core, both conditional sections, four grep counts, two
                 exact diffs, a manifest reading, a test table with class-B captures, eight gate
                 lines, a git sequence, and a MEASURED/LEAD critique.
exchange 05/01   tier E3. A wire-format change over twelve languages and live multiplayer.
                 Report: the same shape, plus twelve verbatim command outputs.
```

⇒ **The E1 report and the E3 report have the same skeleton.** One of those two is wrong, and it is
not the E3 one.

### ⭐ Proposed fix

Already stated as the report half of **D-02**, and it belongs beside the tier table rather than beside
the report contract, so that one table decides validation *and* report shape together. Merging the two
is the actual fix: **one tier selection, two consequences.**

---

## 3. The workflow this session converged on, as a candidate AP shape

⚠ This section is **not** a defect. It is the positive form of D-01, D-06, D-07 and D-09, written out
so a protocol-update task has something to adopt rather than only things to remove. It is the
Cooperator's brainstorming plus what I measured executing it.

```text
1  ORCHESTRATOR reads the protocol once, in distilled form, and owns the problem domain.
   ⇒ It is the only participant that should ever read AP end to end.
2  TRIVIAL work is done ORCHESTRATOR-DIRECT. No Worker, no prompt file, no duplicate verification.
   Gates proportional to blast radius. Evidence permanently marked non-independent.
   ⇒ D-05 names the mode; D-09 prices it.
3  REAL work goes to a Worker as a COMPACT prompt: one outcome, the smallest authority that reaches
   it, AP by CITATION with line ranges, and an explicit "AP wins — stop and report" clause.
   ⇒ D-07. Many small Workers are fine; delivery is not authority.
4  The WORKER analyses the grant BEFORE executing, executes, verifies BASIC correctness, and then
   analyses the APPROACH — returning defects in the Orchestrator's prompt, plan and sequencing.
   ⛔ It does not write long prose. It does not run every suite. It verifies what could be wrong.
   ⇒ D-01 makes this required; D-02 and D-12 keep it short.
5  The ORCHESTRATOR treats every report as a CLAIM, re-measures what matters, and — this is the part
   that produced everything good here — CORRECTS ITS OWN ORCHESTRATION from the critique.
6  TESTS are their own punchy exchange, commissioned only after step 5 has decided what is worth
   asserting. ⇒ this is how "nezmyselne testy" stop being written and stop being run.
7  INDEPENDENCE is bought exactly once, at the tier that requires it, and it is the one thing the
   Cooperator must route by hand. ⇒ D-10 keeps this intact and names the cheap middle.
```

⚠ **The one thing I would tell a protocol author about step 4.** It works because of the two labels,
not because of the volume. MEASURED and LEAD, kept strictly apart, with the Worker forbidden to leave
an item unlabelled. In the previous era an unlabelled LEAD was acted on as a measurement and became a
production defect. **The labels are the entire mechanism.**

---

## 4. What to change first

```text
1  D-01  add `Orchestration critique` to the report's compact core, with MEASURED/LEAD labels, and
         state in AP.md:1406-1441 that critiquing the grant is part of the task.
         ⇒ cheapest change, largest measured effect. Twelve defects in one whole came through an
           unofficial version of it.
2  D-09  add `Overhead budget: minimal | proportionate | full`, selected by consequence, and merge
         the report-shape consequence into the tier table (D-02, D-12).
         ⇒ stops the protocol manufacturing the work D-01 then has to catch.
3  D-04  give an enumeration a declared status and make widening it a Worker obligation.
         ⇒ three consecutive exchanges in this whole failed on exactly this.
4  D-07  per-role reading by citation, with a fail-closed "AP wins, stop and report" clause.
5  D-11  the additive-only amendment instrument.
6  D-06  split the subagent sentence: delivery is free, independence is not.
7  D-05  `Execution mode: orchestrator-direct | worker-delegated`, and deprecate both informal names.
8  D-10  name the context-isolated middle class, forbid it from satisfying E3/E4.
9  D-03  validation proportionality: a zero-mutation exchange owes the repository gate and nothing more.
10 D-08  promote AP.md:1366-1370 to a premise; add punchiness to the readiness review. Keep the name.
```

## 5. Honest limits of this document

```text
· ONE SESSION of evidence, one project, one Cooperator, one pin. Every defect is real here; none is
  proven general. A protocol-update task should look for a second witness before rewriting AP.
· I am not a neutral party. Twelve of the defects catalogued in D-01 are MINE, so a reader may
  reasonably suspect I am designing a protocol that forgives my own failure mode. The counter-evidence
  is that D-01's fix makes those failures MORE visible, not less.
· I have not measured what the fixes cost. `Orchestration critique` as a required field will produce
  false positives, and D-11's amendment instrument is exactly the kind of small convenience that
  erodes into an implicit grant if it is not policed.
· Nothing here touches the parts of AP that worked without complaint all session: the coordinate
  contract, the five recovery classes, fail-closed classification, the closure record, and the
  refusal of a Worker to execute a defective grant. ⛔ Those carried this session. Do not trade them
  for throughput.
```

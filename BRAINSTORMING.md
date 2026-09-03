# Brainstorming — experimental AP ideas awaiting design, testing, or rejection

Artifact class: **brainstorming register, evidence and proposal only, never
authority.** `AP.md:886-916` classifies uploaded, generated, and brainstormed
material as data under analysis. `AP_ORCHESTRATOR.md:105-110` adds the operative
rule for this file: *brainstorming may become a blocker, a risk, a backlog item,
a future logical whole, or an upgrade-ledger observation; it never becomes
mutation authority automatically.*

Owner: the COOPERATOR (Michal) proposes; an Orchestrator records, sharpens, and
states the honest cost. Nothing in this file changes how a current logical whole
is executed unless it is promoted to an accepted decision in
`projects/<project>/PROJECT_CONTEXT.md` or into the pinned protocol by a separate
explicit AP-update task.

Scope: this file is **cross-project** and lives at the Meta root beside
`AP_DESTILLED.md`, because the ideas below are about the **protocol**, not about
any single product.

How to read a section:

```text
STATUS      proposed | in-design | under-test | promoted | rejected
OWNER       who decides
COST        the honest cost, stated before the benefit
OPEN        what must be answered before it can be promoted
```

Every entry names the pinned protocol commit it was measured against, because a
proposal about AP is only meaningful against a specific AP.

```text
governing pin at the time of writing   9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
measured in                            /home/agile/Projects/libretiles/.ap
sibling newer checkout, NOT governing  /home/agile/Projects/ap
```

---

## 1. `Worker Orchestrator` — an orchestrating instance that is accountable as a Worker

```text
STATUS   proposed, 2026-09-03, by the COOPERATOR during logical whole
         `12/00 multilingual-expansion`
OWNER    COOPERATOR (protocol design is his, RF-01)
```

### 1.1 The idea, in his words and in one paragraph

His words, recorded verbatim because a paraphrase would lose the shape:

> *"Mozes generovat prompty pre Planner Workerov, obycajnych Workerov aj Agent
> Orchestratorov, ktory mozu riesit bez toho aby generovali prompty pre fresh
> Workerov.. prilis caste generovanie promptov pre Workerov sa ukazalo ako prilis
> narocne na tokeny."*

> *"Toto nebudu klasicke prompty pre Agent Orchestratorov, ale Orchestratorov,
> ktory sa budu de facto spravat ako Worker teda by som ich nazval teraz pocas
> tohto brainstormingu ma napada Worker Orchestrator, toto prosim teraz tento
> napad zahrn do noveho suboru meta/BRAINSTORMING.md"*

> *"Chcem prompty Worker Orchestratorov vkladat manualne teoreticky aj inym LLM.
> Toto je proste napad na vylepsenie AP ako takeho."*

So: a **Worker Orchestrator** is an instance that receives one complete
authoritative prompt from an Agent Orchestrator, is **accountable as a WORKER**
(it returns one terminal report to the Orchestrator that issued its prompt, and
its authority dies at that report), but is permitted to **orchestrate internally**
— to decompose its bounded task, to run its own subagents, and to sequence them —
without generating fresh authoritative Worker prompts of its own.

### 1.2 Why he wants it, and the cost he is trying to avoid

The problem is real and measured in this archive: era 10 of Libre Tiles consumed
**seventeen Worker sessions**, and the archived implementation prompts run
22 965 B to 50 545 B each. Writing them is the single largest consumer of
Orchestrator context, and an Orchestrator that runs out of context mid-whole must
be replaced by a fresh one through a restoration handout, which costs another
large artifact. The proposal moves that cost down one level: one Worker
Orchestrator prompt buys a whole sub-domain instead of one slice.

```text
COST, stated first
1  It puts a decomposition decision inside an instance whose report the
   Orchestrator can only evaluate as a CLAIM. The Orchestrator loses the
   per-slice inspection point that has repeatedly caught its own errors — in this
   archive, twice a Worker overruled an Orchestrator on evidence and was right
   (PROJECT_CONTEXT.md lesson 8, lesson 18). Fewer exchanges means fewer of those
   catches.
2  It concentrates blast radius. One accountable report now covers many file
   changes, so a defect is discovered later and with less separation.
3  It does not reduce total tokens; it moves them. The decomposition still
   happens, just inside a context the Orchestrator never sees.
```

### 1.3 What the PINNED protocol already permits, measured

This idea does **not** require a protocol change to be lawful. Measured in the
pin:

```text
AP.md:1166-1177          AP defaults to EXACTLY ONE active accountable Worker
                         workstream. A Worker Orchestrator is still ONE
                         accountable workstream, so it does not violate this.
AP.md:1249-1252          sub-agents, Explore tasks and parallel work are
                         `not-used` UNLESS EXPLICITLY AUTHORIZED. So internal
                         delegation is a grant the issuing prompt may make.
PROMPT_CONTRACTS.md:868  `Sub-agents/internal delegation: <not-used | bounded
                         authority>` — the field already exists.
PROMPT_CONTRACTS.md:949  "internal delegation remains one accountable WORKER and
                         never establishes independent audit."
AP.md:576-583            uppercase role names are protocol abstractions, not
                         chats, models, or clients. Worker session profiles,
                         phases and clients create NO additional persistent role.
```

Consequence, and it is the sharpest thing in this entry: **`Worker Orchestrator`
must be a WORKER SESSION PROFILE, not a fourth role.** `AP.md:548-583` fixes
three persistent roles and `:576-583` says profiles add none. If it is written as
a role it forks the protocol (RF-15) and the result belongs to no declared AP.
Written as a profile — sitting beside `Fresh Implementation Worker`,
`Fresh Evidence Probe`, `Bounded Correction Worker` at
`PROMPT_CONTRACTS.md:1701-1764` — it is lawful under the existing pin with no
protocol edit at all.

Suggested profile name, so the accountability is unmistakable from the label:
**`Delegating Implementation Worker`**. His coinage `Worker Orchestrator` is the
better *conversational* name and should stay in Slovak discussion; the field
value should say Worker, because the field value is what a future reader uses to
decide whether the evidence was independent.

### 1.4 The three hard constraints it must carry

```text
C1  IT IS NEVER INDEPENDENT. RF-05 (AP.md:129-136) and AP.md:1395-1405: a session
    that inherited the issuing conversation or reasoning is not fresh, and
    internal delegation never establishes independent audit. So a Worker
    Orchestrator can never supply an E3 fresh independent acceptance, and its own
    subagents can never audit each other. Evidence posture is `non-independent`,
    always, with no exception.
C2  IT DOES NOT ISSUE AUTHORITATIVE WORKER PROMPTS. Its internal delegation is
    task decomposition inside ONE grant. The moment it would need to grant an
    authority it was not given, it must stop and report — exactly the ordinary
    Worker stopping condition at AP.md:2466-2486. This is the boundary that keeps
    it from becoming a second Orchestrator and creating a prompt-generation loop.
C3  ITS REPORT IS ONE TERMINAL WORKER REPORT. It begins exactly
    `### Report for ORCHESTRATOR_CHAT` (AP.md:2460-2465), echoes the three
    coordinate fields unchanged (PROMPT_CONTRACTS.md:38-41), carries exactly one
    report justification from the closed enum (AP.md:2452-2454), and says
    `Logical-whole closure: not-closed` (PROMPT_CONTRACTS.md:224). It must also
    disclose its own internal decomposition, because that is the part the
    Orchestrator can no longer see.
```

### 1.5 The extra report fields it needs, and why

An ordinary Worker report does not have to explain how it thought. A delegating
one does, because the decomposition is the thing the Orchestrator gave up.
Proposed additional required fields:

```text
Internal delegation used: yes | no
Internal subtasks: <ordered list, each with its own outcome>
Decomposition rationale: <why these boundaries>
Cross-subtask contradictions found: none | <exact contradiction and resolution>
Work a subtask refused or could not complete: none | <exact>
Evidence a subtask CLAIMED that this Worker did not re-measure itself: none | <exact list>
```

That last field is the load-bearing one. `PROJECT_CONTEXT.md` lesson 18 records
the exact failure it prevents: an Orchestrator quoted an explore subagent's count
of "nine existing `it` blocks" when there were eleven, and the adjacent correct
number in the same sentence is what made the wrong one look checked. A delegating
Worker will produce that same class of error unless it is required to say which
numbers it counted itself.

### 1.6 Where it fits, and where it must not be used

```text
GOOD FIT
  a large mechanical surface with one coherent outcome and low per-file risk —
  translating one interface locale across many components; renaming a symbol
  across dozens of call sites; adding one test family per variant
  a sub-domain whose internal ordering is obvious once inside it, so the
  Orchestrator's per-slice inspection adds little
BAD FIT
  anything with a trust boundary: authN/authZ, credentials, CSP, throttling
  anything E3 or E4
  any wire-format or schema migration, where "broken between two slices" is the
  named hazard (DEFECT_LEDGER.md:806-826)
  anything that needs independent acceptance — C1 forbids it structurally
```

### 1.7 Open questions before promotion

```text
OPEN-1  Does a Worker Orchestrator's own subagent count against the
        one-accountable-workstream default at AP.md:1166-1177 if two of its
        subagents mutate the tree concurrently? Working answer: YES, it must
        serialize its own mutating subagents and say so, because the pin's
        parallel-topology exception requires a group identity, disjoint path
        ownership, a shared-state matrix, and an integration owner — none of which
        a subagent can supply for itself.
OPEN-2  How is its context pressure surfaced? An ordinary Worker reports its own;
        a delegating one hides its subagents'. Proposed: it reports its own
        visible pressure plus whether any subagent terminated for context.
OPEN-3  Does the archive get one prompt/report pair, or one pair plus internal
        artifacts? Working answer: ONE pair, per AP.md:322-336, with the internal
        decomposition inside the report. Internal subagent transcripts are
        explicitly NOT archived — `AP.md:2043-2097` rejects transcript archives.
OPEN-4  He wants to paste these into OTHER LLMs. That makes the prompt a
        cross-client artifact, so it must be fully self-contained and
        structurally English with no client-specific tool names — which the pin
        already demands at AP.md:2487-2578 and AP_ORCHESTRATOR.md:363-375.
```

### 1.8 Recommended first test

Use it once, on a genuinely good-fit slice, in a whole where a failure is cheap
and visible. The named candidate is the **Hungarian interface locale** slice of
`12/00 multilingual-expansion`: roughly 300 message keys across one new
`messages.hu.ts`, one `LOCALES` entry, one plural function, and a glossary
section — one coherent outcome, no trust boundary, high mechanical volume, and a
defect is immediately visible as wrong on-screen text rather than as a silent
security hole. Then compare, honestly: total tokens, defects found per exchange,
and whether the Orchestrator could still evaluate the report.

---

## 2. Several handouts inside one logical whole, instead of one at the end

```text
STATUS   proposed, 2026-09-03, by the COOPERATOR
OWNER    COOPERATOR
```

His words:

> *"DOKONCA TERAZ UVAZUJEM, ZE BY SI MOHOL GENEROVAT VIAC HANDOUT PROMPTOV PRE
> FRESH ORCHESTRATOROV. NIELEN JEDEN NA KONCI AKO JE V AP DEFINOVANE.. mozno by
> to tuto ulohu vedelo zjednodusit a hlavne nechceme aby si si rychlo zaplnil
> svoj kontext window."*

### 2.1 This one is already lawful, and this project has already done it twice

Measured. The pin does **not** say one handout per whole. `AP.md:2229-2328`
governs session rotation and dynamic prompts and `AP_ORCHESTRATOR.md:436-444`
says: *rotate at a coherent boundary when context integrity, qualitative
pressure, capability fit, policy, cost, or independence requires it; rotation
transfers information, never authority; use no numeric context threshold.*

The existing evidence that this works:

```text
10/00-ui-internationalization/00_handout.md   34 365 B  the opening handout
10/00-ui-internationalization/93_orchestrator-handout.md  41 783 B  a SECOND
        handout for the SAME whole, written mid-whole at his explicit request,
        with the rule "where it and 00_handout.md disagree, 93_ is later and wins,
        and every disagreement is named in its section 4"
```

So the practice exists, it is recorded in `PROJECT_CONTEXT.md:799-829`, and it
produced the whole that closed successfully. What is missing is not permission —
it is a **naming and precedence discipline** so that three handouts for one whole
do not become three competing semantic owners, which `AP.md:18-62` forbids.

### 2.2 The discipline it needs

```text
D1  FILENAME. `00_handout.md` stays reserved for the whole's opening handout
    (/home/agile/meta/README.md:25-39, projected at PROMPT_CONTRACTS.md:658-671).
    Every later one is an Orchestrator artifact in the `9N_` band:
    `9N_orchestrator-handout-<ordinal>.md`. It is NOT an exchange and never
    consumes a Worker exchange ordinal.
D2  PRECEDENCE, STATED IN THE FILE ITSELF. Later wins, and every disagreement
    with an earlier handout is named explicitly — the `93_` rule, generalized.
    A handout that silently contradicts its predecessor creates two owners.
D3  IT IS A CONTINUATION HANDOUT, NOT A RESTART. It carries the accepted slice
    plan, what has landed with exact commits, what remains, and the residual
    register. It does NOT re-derive the objective; the objective was bounded once
    by the Cooperator and re-deriving it would be RF-19's changed-objective case
    (AP.md:255-262), which starts a new logical whole instead.
D4  IT GRANTS NOTHING. Same sentence three times, as the current handouts do.
D5  IT IS WRITTEN AT A COHERENT BOUNDARY — after a slice's report is archived and
    before the next prompt is issued — never mid-exchange with a Worker in
    flight, because then `Active mutation` is not `none` and the successor cannot
    verify state.
```

### 2.3 The honest cost

```text
Each continuation handout is itself 25-45 KB of writing, so the break-even point
is real: rotating too early spends more than it saves. The judgement is
qualitative by design (AP_ORCHESTRATOR.md:444 forbids a numeric threshold), and
the practical trigger is not a percentage — it is when the Orchestrator notices it
is re-reading its own earlier measurements instead of remembering them.
```

### 2.4 Interaction with entry 1

Entries 1 and 2 solve the same problem from opposite ends and they compose well:
a **Worker Orchestrator** reduces how many prompts the Orchestrator must write; a
**continuation handout** bounds the damage when it still runs out. Using both in
one whole is the intended shape.

---

## 3. Autonomous mode — the Cooperator opts out of acceptance testing for a whole

```text
STATUS   in-design, 2026-09-03, decided by the COOPERATOR for 12/00 only
OWNER    COOPERATOR
```

His words:

> *"NECHCEM ABY SOM TU BOL AKO COOPERATOR POUZIVANY NA TESTOVANIE, VELA JE TEXTOV
> VELA JAZYKOV NECHCEM ABY SME TU TESOVALI KLASICKOU METODOU AP PRETOZE BY BOLO
> TESTOVANIA PRIVELA A JA CHCEM ABY SI PRACOVAL AUTONOMNE. OVEROVANIE, ZE TEXTY
> SLOVNIKY FEATURES NOVE BUDU REALIZOVANE AZ NA KONCI VYVOJA."*

This is a lawful Cooperator decision under RF-01: he owns subjective acceptance,
and choosing to exercise it **once at the end** instead of per slice is a
sequencing decision, not a waiver of evidence. `AP.md:433-444` and
`AP_ORCHESTRATOR.md:71-76` even push in this direction: *do not ask for
microapproval of deterministic steps inside an approved envelope.*

### 3.1 What it does NOT change, and this is the part to protect

```text
It does not lower an evidence tier. E3 still requires fresh independent
    acceptance (AP.md:1112-1119) and that acceptance is a WORKER function, not a
    Cooperator function — those are different things and only one of them was
    deferred.
It does not remove the rendered-output rule. `PROJECT_CONTEXT.md` lesson 11: for
    anything that renders, render it, or do not claim it. Deferring HIS observation
    makes the Orchestrator's own loopback probe MORE necessary, not less: production
    build, `next start` on a loopback port, HTTP client, stop by exact PID.
It does not make a green gate set a correct product (uii-01-F04).
It does not permit "accessibility verified" — decision 10 is a permanent evidence
    ceiling and no autonomy grant touches it.
```

### 3.2 The obligation it creates for the Orchestrator

An acceptance batch that is not run at the time it is generated must still be
**written down at the time it is generated**, or it will be reconstructed from
memory at the end of the whole and will be wrong. Proposed discipline: every slice
that produces a Cooperator-observable change appends its numbered batch items to
one accumulating file — `9N_deferred-acceptance-batch.md` — with the slice, the
commit, and the exact observable expectation. At the end of the whole that file IS
the acceptance batch, and it was written when the evidence was fresh.

### 3.3 Open question

```text
OPEN-1  If the end-of-whole batch then FAILS on item 7 of 40, the correction
        budget (RF-08, one smallest coherent correction per finding) is being spent
        against a slice that closed many exchanges ago. Working answer: a failed
        deferred item is a NEW defect with its own ledger entry and its own
        bounded correction, not a reopening of the old slice. Say so in advance so
        it is not litigated later.
```

---

## 4. Rejected and superseded, kept so they are not re-proposed

```text
none yet in this file
```

Entries move here with the reason and the date, never by deletion —
`AP.md:322-336`: historical artifacts stay interpretable and are never
retroactively rewritten.


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

Kronika addition, 2026-11-08           §7 measured at
                                       73e20ef80b88700d5fcbc397cd8edd4fc425869f
                                       (.ap of /Users/agile/Projects/kronika).
                                       Sections 1-6 remain at the 9c5cc44 pin.
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

## 5. Autonomous Worker Report Archiving — direct write to Meta eliminates the human courier

```text
STATUS   proposed, 2026-09-08, by the COOPERATOR during logical whole 15/00
OWNER    COOPERATOR (protocol design is his, RF-01)
```

### 5.1 The idea, in his words and in one paragraph

> *"PROSIM nech dalsi Workeri okrem Planner workera proste ZAPISUJU xx_report_xx.md AUTOMATICKY
> aby som ja nemusel manualne vytvarat report subor a manualne robit copy->paste.. Toto uz ma nudi.
> Proste ked Worker dokonci pracu chcem mat ja = Cooperator len priestor na brainstorming. Komentar.
> Zasah ako teraz ze netreba zachovavat stare zaznamy o hrach.. Chcem aby si si ty potom sam uz vedel,
> ze mas precitat dany xx_report_xx.md subor bez toho aby som ti to musel uvadzat. Proste posledny
> subor v repe a format xx_report_xx.md je vzdy rovnaky. Nechapem preco by som mal stale robit
> zbytocne ulohy."*

In short: Workers receive explicit authority and instruction to write their terminal report directly
to `/home/agile/meta/projects/<project>/<whole>/<ordinal>_report_<exchange>.md` before concluding.
The Orchestrator autonomously identifies and reads the report from disk. The Cooperator is freed from
mechanical copy-pasting, preserving his attention for high-value strategic intervention, direction, and
brainstorming.

### 5.2 Why this is essential for the future of AI-driven AP

```text
COST, stated first
1  If a Worker hallucinated a corrupted report file or crashed mid-write, the Orchestrator could read
   a partial report. (Mitigation: atomic file write or write-then-rename, plus checking the AP
   compact core header before parsing).
2  Requires granting filesystem write authority specifically targeting the external `/home/agile/meta`
   directory, which crosses the boundary that Workers must mutate only allowlisted repository files.
```

```text
BENEFIT
1  Eliminates the single most exhausting friction point in human-orchestrated multi-agent development.
2  Prevents clipboard truncation, accidental omission of lines, and human courier latency.
3  Allows true asynchronous, punchy execution cycles where the human intervenes ONLY when decisions,
   architectural trade-offs, or approvals are needed.
```

### 5.3 Concrete implementation in Worker prompts

Add to the Worker Prompt Contract under Side-effect authority:

```text
Report delivery: direct-write to meta archive
  Write your complete terminal report directly to:
  `/home/agile/meta/projects/<project>/<whole>/<ordinal>_report_<exchange>.md`
  using your file writing tool. Confirm the file was written cleanly.
  Your final message in chat should be a concise 3-line notification with status and the report path.
```

---

## 6. Clean Slate Protocol for Alpha/Prototyping Eras — Purge vs Forensic Migration

```text
STATUS   proposed, 2026-09-08, by the COOPERATOR during logical whole 15/00
OWNER    COOPERATOR
```

### 6.1 The idea, in his words and in one paragraph

> *"Planner Worker mimochodom riesil ako nachadzat s existujucimi datami v DB a teda co so starymi hrami,
> pretoze nemaju ulozene data na replay v admin rozhrani. PROSIM JEDNODUCHO ZMAZAT VSETKY ZAZNAMY A HOTOVO
> NETREBA ZIADNU MIGRACIU PROSTE NEPOTREBUJEME STARE HRY JEDNOZNACNE."*

When extending application data models in development or prototyping phases, Planners default to
designing complex forensic heuristics to reconstruct missing past data (e.g. attempting to simulate
unrecorded draws from seeds, handling missing fields, building multi-tier fallback branches).
Instead, AP should formalize a **Clean Slate Decision**: when existing database state has no business
continuity requirement, explicitly authorize a purge of legacy records (`truncate` or `purge command`),
drastically cutting planning overhead and keeping code 100% clean and free of legacy baggage.

### 6.2 Comparison: Legacy Forensic Preservation vs Clean Slate

| Aspect | Legacy Forensic Preservation | Clean Slate Protocol |
|---|---|---|
| **Planning Overhead** | Huge (500+ lines analyzing edge cases, missing draws, partial seeds) | Minimal (< 20 lines) |
| **Code Complexity** | Complex conditional branches, fallback modes, guessing heuristics | Single authoritative schema, zero legacy branching |
| **Bug Surface** | High (forensic reconstruction frequently diverges from truth) | Zero (all replay data is captured directly and losslessly) |
| **Maintainability** | Permanent technical debt in services and serializers | Clean, idiomatic, future-proof code |

### 6.3 Rule for AP Protocols

```text
In non-production / development phases:
Before designing backward-compatibility heuristics for records that lack required new data,
the Orchestrator / Planner must explicitly verify with the Cooperator:
"Does historical data have durable value, or is a Clean Slate purge authorized?"
If purge is authorized, delete legacy tables/rows and build solely against the authoritative clean schema.
```

---

## 7. `Master Orchestrator` — a run-level Orchestrator that pre-generates `00_handout.md` for every logical whole

```text
STATUS   promoted, 2026-11-08; AP d7023cf, ADR-0026
OWNER    COOPERATOR (protocol design is his, RF-01); ORCHESTRATOR records and sharpens
PIN      measured against 73e20ef80b88700d5fcbc397cd8edd4fc425869f
```

### 7.1 The idea, in his words and in one paragraph

His words, recorded because the shape matters:

> *"Ty by si teda bol de facto 'Session' ale 'Master' alebo proste hlavny
> Orchestrator generujuci handout expertne prompty pre logicke celky."*

> *"od teba chcem aby si vygeneroval pre kazdy logicky celok samostatny
> 00_handout.md."*

The **Master Orchestrator** is an ORCHESTRATOR instance whose bounded planning
scope is one **development run**, not one logical whole. It maintains the run
map — the ordered set of logical wholes, their dependencies and their evidence —
and writes one provisional `00_handout.md` for each whole in the run. It does
not issue the Workers' task prompts, does not accept their results, and does not
close their wholes. The per-whole Orchestrator still does that.

In one sentence: it is **orchestration of orchestration** at the handoff layer.
The per-whole Orchestrator coordinates Workers inside a whole; the Master
Orchestrator coordinates handoffs between wholes.

### 7.2 Why he wants it

Measured friction in the current archive:

- The Cooperator has long pauses between development runs. Each new whole
  currently starts with a restoration handout written at the end of the previous
  whole or by a fresh Orchestrator after the pause.
- Those handoffs cost a large context artifact each, and they are written by the
  participant who is closest to the old whole and furthest from the new one.
- The Cooperator becomes the relay between per-whole Orchestrators: "here is the
  next whole, here is the state, here is what we decided."
- The candidate backlog already exists, but it is scattered across handouts,
  reports and chat. The run has no single map.

Pre-generating the handouts at the start of a run gives the Cooperator a
reviewable menu of wholes and gives each per-whole Orchestrator a consistent,
expert starting point. The Cooperator's scarce attention moves from handoff
plumbing to product direction.

### 7.3 What it is, and what it is not

```text
IT IS
- an ORCHESTRATOR session or access profile whose scope is a development run;
- the author of the run map and of one provisional 00_handout.md per whole;
- a user of the existing orchestration-planning layer and the Meta trace;
- the maintainer of cross-whole dependencies and of the candidate backlog;
- a reader of AP_DEFECTS.md / AP_DESTILLED.md and a capturer of new protocol
  friction.

IT IS NOT
- a fourth persistent AP role;
- a Worker, a Planner, or a substitute for the per-whole Planner;
- the issuer of Worker prompts or the acceptor of their reports;
- a source of mutation authority;
- a second semantic owner for product decisions;
- a reason to skip Stage 1 verification in the per-whole Orchestrator;
- a batch of pre-approved implementation grants.
```

The distinction is deliberate: the Master Orchestrator **prepares** the run, the
per-whole Orchestrator **executes** the governance of one whole, and the
COOPERATOR **selects** the objective and accepts the result.

### 7.4 AP mapping, measured at the Kronika pin

The three persistent roles are unchanged: COOPERATOR, ORCHESTRATOR, WORKER. The
Master Orchestrator is an ORCHESTRATOR instance with a broader **session scope**,
not a new role. It uses:

- the orchestration-planning layer (`AP.md` §3) for the run map;
- the existing Worker session target and profile rules for each whole's Planner;
- RF-19 for the external trace and exchange coordinates;
- RF-14 / `ARTIFACT_LIFECYCLE.md` for the handout artifacts;
- the same authority rules: the handout grants nothing;
- the same independence rules: the Master does not audit a whole and does not
  accept its result.

The per-whole Orchestrator remains the only authority that issues the whole's
Worker prompts. The Master's handout is a **provisional seed**; the per-whole
Orchestrator re-verifies current state and may rewrite the handout before the
first Planner. The first Planner still runs with the client's actual native
planning mode enabled; the Master never replaces the Planner's repository
grounding.

If AP later formalizes this, the clean shape is a named Orchestrator access
profile or a bounded session scope, not a fourth role. The profile name is a
routing label, not authority.

### 7.5 Meta layout and numbering

The Meta archive already separates **runs** and **wholes**:

```text
projects/<project>/<run>/<whole-sequence>-<whole-identity>/00_handout.md
projects/<project>/<run>/<whole-sequence>-<whole-identity>/00_notes.md
...
```

- `<run>` is the archive sequence (`00`, `01`, `02`, ...). It groups the wholes
  between Cooperator pauses.
- `<whole-sequence>` is the two-digit order inside that run (`00`, `01`, ...).
- `00_handout.md` is the Master Orchestrator's seed for that whole.
- `00_notes.md` is the per-whole Orchestrator's decision record, created when
  the whole opens and frozen at closure.

The Master Orchestrator may add one optional run-level map:

```text
projects/<project>/<run>/00_RUN_MAP.md
```

The run map lists the ordered wholes, their dependencies, their status
(`provisional | handed-off | active | closed | superseded`), and the one
sentence of evidence that justifies each. It is discovery policy, not
authority. If the Cooperator does not want a new artifact, the directory names
plus the handouts are enough.

### 7.6 The process

```text
1  The COOPERATOR sets the run objective, priorities and any hard exclusions.
2  The MASTER ORCHESTRATOR reads the verified current state, the previous run's
   closure, AP_DEFECTS.md / AP_DESTILLED.md, and the candidate backlog.
3  It drafts the run map: ordered wholes, dependencies, evidence, scope shape,
   risks and the handoff order.
4  It writes one provisional 00_handout.md per whole. Each handout is a
   restoration/handoff seed, not a plan and not a grant.
5  The COOPERATOR reviews the run map, reorders or drops wholes, and selects the
   first whole.
6  The PER-WHOLE ORCHESTRATOR restores from that handout, verifies current
   state, updates the handout to confirmed (or rewrites it), and issues the
   first Planner prompt.
7  At each closure, the Master updates the run map and the remaining handouts
   for the changed state. A stale handout is revalidated, superseded or marked
   obsolete; it is never silently trusted.
8  The Master captures new measured protocol friction in AP_DEFECTS.md and
   keeps AP_DESTILLED.md current as part of normal work.
```

### 7.7 The handout template

Every Master-generated `00_handout.md` should carry:

```text
Restoration classification: PROVISIONAL | FULL | PARTIAL
Capability profile: Orchestrator
Initialization signal: ...
Restoration date / author / persister / predecessor / destination
Restoration grants mutation authority: no

0  Read this first
1  Continuation Bootstrap Stage 1: repository, AP pin, NUC, previous closure
2  Stage 2: recommended whole, scope shape, questions, alternatives
3  Strategic continuity
4  Project-specific operating rules (report direct-write, satisfiability,
   coordinates, delivery, AP maintenance, security)
5  Risk register
6  First actions
7  Readiness review
```

The handout names the **questions** the per-whole Planner must answer; it does
not answer them. It names the **evidence** and the **risks**; it does not
pre-approve a solution.

### 7.8 Benefits

```text
1  The Cooperator sees the run as a menu before it starts.
2  Each per-whole Orchestrator starts from a consistent, expert handoff instead
   of re-deriving context after a pause.
3  Cross-whole dependencies become visible (e.g. previews before thumbnails;
   thumbnails before onboarding).
4  Handoffs are written while the analysis context is fresh, not after a pause.
5  The Cooperator stops being the relay between per-whole Orchestrators.
6  The run map is a natural place to reconcile AP_DEFECTS.md improvements with
   product work.
```

### 7.9 Costs and risks

```text
COST, stated first
1  STALENESS. A handout written at run start goes stale by the time its whole
   opens. Mitigation: mark it PROVISIONAL; the per-whole Orchestrator must
   revalidate state and may rewrite it. A stale handout is evidence, not
   authority.
2  OVER-PLANNING. Generating eight handouts may be wasted if the Cooperator
   changes direction. Mitigation: keep the run map cheap; generate handouts in
   a rolling horizon or at low resolution until the whole is selected.
3  AUTHORITY CONFUSION. A pre-written handout can be mistaken for a task grant.
   Mitigation: every handout says "grants no authority" and the per-whole
   Orchestrator still performs Stage 1/2.
4  DUPLICATE OWNERSHIP. The Master can drift into product decisions that belong
   to the Cooperator or the per-whole Planner. Mitigation: handouts carry
   questions and constraints, not decisions.
5  CONTEXT COST. Writing all handouts is a large upfront token cost. Mitigation:
   bound the run size; use a compact template; generate the rest on demand.
6  FALSE CONTINUITY. The Master may assume the previous whole closed as planned.
   Mitigation: read the closure record and revalidate the actual state.
```

### 7.10 Open questions

```text
1  Is "Master Orchestrator" a new Orchestrator access profile, a session scope,
   or only a local Meta convention? It must not become a fourth AP role.
2  Does the run map deserve a durable artifact, or are directory names and
   handouts enough?
3  Batch-generate all handouts at run start, or a rolling horizon of the next
   two or three?
4  How is PROVISIONAL -> confirmed recorded: in the handout header, in the run
   map, or both?
5  Who updates the remaining handouts when a whole changes the state: the
   Master, the closing per-whole Orchestrator, or the next whole's Orchestrator?
6  How does the Master avoid pre-empting the per-whole Planner's native planning
   mode?
7  What is the exact handoff from Master to per-whole Orchestrator: a prompt, a
   file path, or both?
```

### 7.11 Recommended first test — this Kronika run

Use the current Kronika run as the pilot:

```text
projects/kronika/01/
  00-ux-refresh-acceptance-and-promotion          closed 2026-11-08
  01-timeline-and-history-media-thumbnails       handout written
  02-upload-flow-polish                          handout written
  03-companion-download-notifications            handout written
  04-household-onboarding                        handout written
  05-humanized-error-copy                        handout written
  06-accessibility-pass                          handout written
  07-app-js-modularization-planning              handout written
  08-product-language-decision                   handout written
```

The pilot run now has a complete provisional handout set. The Cooperator
selects the order; the per-whole Orchestrator for the selected whole revalidates
its handout before the first Planner. Measure:

```text
- time from whole selection to first Planner prompt;
- number of Cooperator relays needed to start the whole;
- number of stale facts the per-whole Orchestrator had to correct;
- whether the per-whole Orchestrator had to re-derive context the handout
  already carried;
- token cost of the handout batch vs. the saved restoration work.
```

If the test shows that the handouts are stale or over-specified, narrow the
Master's scope to a run map plus one-paragraph seeds, and let the per-whole
Orchestrator write the full handout.

### 7.12 The first AP update run

The first concrete Master Orchestrator whole is the AP update itself:

```text
/Users/agile/meta/projects/ap/10/00-master-orchestrator-and-report-persistence/00_handout.md
```

It formalizes the Master Orchestrator role/session scope, the run-level handoff
model, direct-write report persistence, the three read-only axes, the prompt
satisfiability check, the blocked-first-exchange rule and the standing
AP-maintenance instruction. It then publishes a new AP commit and updates the
Kronika `.ap` pin to it. This is the bridge between the Kronika pilot handouts
and the next development run.

### 7.13 Relationship to the other entries

```text
§1 Worker Orchestrator      different: that is a WORKER with internal delegation;
                            the Master is an ORCHESTRATOR with a run scope.
§2 Several handouts         related: that is several handouts inside one whole;
                            the Master writes one handout per whole in a run.
§5 Direct-write reports     complementary: the Master's handoffs reduce the
                            Cooperator's relay; direct-write removes the report
                            relay. Both protect Cooperator attention.
§6 Clean-slate data         independent: a product-data policy, not a handoff
                            policy.
AP_DEFECTS D-21             the Master is a natural carrier of the standing
                            AP-maintenance instruction: read the backlog, capture
                            new defects, update AP_DESTILLED.md.
```

---

## 8. Browser MCP evidence — Workers produce rendered screenshots and interactions, not only static reads

```text
STATUS   proposed, 2026-11-10, by the COOPERATOR
OWNER    COOPERATOR (protocol design is his, RF-01)
PIN      measured against AP d7023cf; canonical AP checkout
         /Users/agile/Projects/ap; consumer Kronika .ap d7023cf
COST     browser capability and MCP availability are environment-dependent;
         screenshots and DOM/console/network evidence add trace volume, cleanup
         and redaction work; flaky browser state can create false failures; a
         screenshot can look authoritative while proving less than it seems.
OPEN     exact MCP server identity/version and capability handshake; which
         prompt fields carry browser authority; where rendered evidence lives
         and how long it is retained; how screenshots are redacted and marked
         non-secret; how Workers prove the page under test is the exact
         candidate; whether the Orchestrator or a fresh auditor owns rendered
         evidence; how to stop honestly when the MCP or browser is unavailable.
```

### 8.1 The measured gap

The COOPERATOR has Playwright MCP and Chrome installed and has explicitly
explained to Orchestrators and Workers that they should use the browser to open
the running application, click the relevant controls, and take screenshots for
verification and testing. In practice the current work still relied on static
source/test inspection and on the COOPERATOR's own rendered acceptance; Workers
did not use the available browser evidence route. The capability existed, but AP
did not make it a declared, bounded, expected part of a UI Worker's evidence.

That is a protocol gap, not a Worker failure. A route that is only mentioned in
chat is ambient convenience. Under RF-06/RF-16 it is not a durable, declared
capability, and an Orchestrator cannot rely on it or audit whether it was used.

### 8.2 The proposal

Add an explicit **browser-evidence route** to AP without creating a second
semantic owner or a new role. At minimum:

- **Capability handshake.** The Worker prompt names the available MCP server /
  browser capability, the exact application origin or local URL, the identity
  or fixture the Worker may use, and the allowed interactions. Availability is
  capability context, never authority.
- **Authority split.** Browser authority is separate from repository, host and
  trace mutation. A read-only UI task can open the page, click, type into
  non-secret test fields, take screenshots, read the accessibility tree, console
  and network metadata, and write only its exact trace evidence. It cannot read
  browser profiles, cookies, tokens, credential stores, unrelated tabs or
  history, and cannot mutate the application or host without a separate grant.
- **Evidence set.** The report should carry the exact candidate identity, URL
  and viewport, screenshots for the claimed states, interaction steps, DOM or
  accessibility observations, console/network errors relevant to the claim, and
  the browser/MCP version or capability observation. Screenshots are evidence,
  not acceptance; the COOPERATOR still owns subjective rendered acceptance.
- **Prompt contract.** The existing Common Worker Task Fields and Browser Stall
  Guard/Amended Expectation records should be extended or pointed to for the
  exact fields. Do not add a parallel browser contract when an existing owner can
  carry the requirement. The prompt must state when browser evidence is
  required, optional, or unavailable, and must stop rather than fabricate
  screenshots.
- **Artifact lifecycle and privacy.** Rendered evidence goes to the activated
  trace with exact filenames, retention and cleanup. It must be public-safe:
  no secrets, private media filenames, host identifiers, cookies, tokens or
  private network values. Redaction is verified before the report is terminal.
- **Testing and acceptance.** A fresh auditor may use rendered evidence, but
  must independently establish the candidate and the page identity. The
  Cooperator's rendered acceptance remains separate. A screenshot cannot
  substitute for a missing authorization test or for the Cooperator's verdict.
- **Fallback.** If the MCP server, browser, network route or test identity is
  unavailable, the Worker records the exact missing capability and either uses
  the declared fallback or stops; it does not silently return to static-only
  claims, invent a screenshot, or treat an ambient browser as authority.

### 8.3 Why this is worth an AP whole

UI verification is now a recurring part of Kronika work: Timeline, History,
Gallery/Details, upload, companion, accessibility and responsive behavior.
Workers can produce far better evidence than a prose claim, and the COOPERATOR
can review exact screenshots instead of re-testing every visual state. The
protocol change also makes the capability auditable and prevents a future Worker
from either ignoring it or using an unbounded browser session.

### 8.4 The next whole

The first concrete AP whole is seeded at:

```text
/Users/agile/meta/projects/ap/10/01-playwright-mcp-integration/00_handout.md
```

It is deferred until the current Kronika logical wholes are finished. Its
Planner must map the existing AP owners (RF-06, RF-16, RF-19, Browser Stall
Guard, INFOSEC, ARTIFACT_LIFECYCLE, PROMPT_CONTRACTS) and propose the smallest
coherent AP update, prompt/contract fields, evidence lifecycle, fallback and
validation. A separate later task updates the Kronika `.ap` pin; the AP update
does not silently move a consumer pin.

### 8.5 Relationship to the other entries

```text
§5 direct-write reports   complementary: direct-write removes the report relay;
                          browser evidence removes some of the Cooperator's
                          rendered re-testing, without removing his acceptance.
§7 Master Orchestrator    complementary: the Master can name the browser
                          evidence expectation in each prepared handout.
§1 Worker Orchestrator    independent: internal delegation is a role question;
                          browser evidence is an execution/evidence route.
AP_DEFECTS D-19/D-20      the browser authority must be a separate mutation axis
                          and must pass the prompt-satisfiability check.
```

---

## 4. Rejected and superseded, kept so they are not re-proposed

```text
none yet in this file
```

Entries move here with the reason and the date, never by deletion —
`AP.md:322-336`: historical artifacts stay interpretable and are never
retroactively rewritten.


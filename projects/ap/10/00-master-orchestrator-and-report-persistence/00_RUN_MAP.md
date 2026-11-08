# AP run 10 — Run Map

```text
Artifact class: Master Orchestrator discovery policy and ordering evidence.
Authority: non-authorizing. A run map is not a grant, a plan, or a second
  semantic owner; it only records the run's ordered wholes and their evidence.
Project: ap
Run: 10
Objective: formalize the Master Orchestrator run scope and the related AP
  protocol corrections; publish the new AP version; update the Kronika .ap pin;
  dry-run one prepared Kronika handout.
Status: active
```

## Ordered wholes

| Order | Whole | Status | Evidence / dependency |
|---|---|---|---|
| 00 | `00-master-orchestrator-and-report-persistence` | active (acceptance 03/01 delivered) | This run's only whole. Depends on AP `73e20ef` and the Kronika pin `73e20ef`; produces the new AP commit, the Kronika `.ap` pin update, and the pilot dry-run evidence. Planner report `01_report_00.md` accepted; CD-1/2/4/5/6 accepted, CD-3 overridden to Cooperator pin commit/push. Implementation candidate `fe1e58d9` (local, 14 paths) delivered; fresh independent acceptance prompt `03_acceptance_00.md` delivered; report pending. |

The AP run contains one logical whole. The Kronika run 01 handouts belong to the
Kronika project and are **not** wholes in AP run 10; they are pilot evidence for
the handoff model and the subject of the bounded dry-run inside this whole.

## Sequence inside the whole

```text
1  Planner (fresh session 01/01) — decision-complete plan; read-only for AP.
2  Cooperator plan gate — accept, targeted revision, or stop.
3  Implementation grant — AP docs, ADR-0026, CHANGELOG, Meta AP_DEFECTS and
   AP_DESTILLED updates; no push.
4  Fresh independent acceptance of the exact new AP commit.
5  Cooperator publication of the AP commit(s) to public main.
6  Kronika .ap pin update and compatibility checks; Cooperator publishes the pin.
7  Bounded pilot dry-run of one prepared Kronika handout (Stage 1 only).
8  Master Orchestrator closure record; Cooperator accepts.
```

Each step is a separate authority boundary. A check never publishes or deploys.
The implementation Worker cannot self-certify the new AP version; the pin update
cannot precede public AP main; the pilot dry-run cannot create `00_notes.md` or
start the product whole.

## Status vocabulary

```text
provisional  seeded but not revalidated by a per-whole Orchestrator
handed-off   per-whole Orchestrator has received and revalidated the seed
active       per-whole work in progress
closed       accepted closure evidence exists
superseded   replaced by a later whole or objective
```

The run map is updated at each closure or material state change. A stale run map
is evidence, not authority; the current repository and the Cooperator's current
decision outrank it.

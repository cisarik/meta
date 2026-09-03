# Supersession record — `11/01 multilingual-tile-token-foundation`

Artifact class: **supersession record. Evidence, not authority.** Written by the
ORCHESTRATOR of `12/00 multilingual-expansion` on 2026-09-03.

```text
Prior logical whole identity: multilingual-tile-token-foundation
Superseded by: multilingual-expansion            (Meta 12/00)
Superseded on: 2026-09-03
Superseding authority: ORCHESTRATOR decision under the Cooperator's explicit autonomy
    grant of 2026-09-03, answering question 1 of 12/00/00_handout.md with option A.
    Recorded in 12/00/00_notes.md section 3.
Basis: RF-19, AP.md:255-262 — a materially changed objective begins a NEW identity and
    does NOT silently absorb an old one. This record is what makes that lawful rather
    than sloppy.
Logical-whole closure: NOT closed. Superseded.
```

## Why it was superseded rather than closed

`11/01`'s accepted plan was nine slices old when `12/00` opened, and the world had
moved past it in two measurable ways:

```text
1  Czech and Polish shipped AHEAD of it, at 2917251, without waiting for F2c/F3/F4.
   Its slice labels F2c/F3/F4 only mean anything inside its own accepted plan, and that
   plan did not contemplate two languages landing before the wire format moved.
2  Four gaps its plan never contemplated were named afterwards by external analysis and
   then measured: no generic per-variant invariant harness, readiness as file-existence
   only, no provenance in the manifest, and WordAuthority built but dormant in production.
```

One identity with one accepted plan is cheaper to reason about than two half-open ones,
and three open wholes with overlapping surfaces is the single thing that makes the
coordinate system meaningless.

## What LANDED under this whole, and stands

```text
9f0c5b8  F1   atomic tile tokens in the pure engine                26 files
3fd1a81  F2a  fail-closed command to purge legacy development state 4 files
8c00a33  F2b  token-shaped persistence, uii-01-F06 and uii-01-F07   9 files
```

All three are unchanged and are the foundation everything after them rests on.

## What it OWED and did not deliver — carried forward, not cancelled

```text
F2c  re-point evaluate_scoring_move at WordAuthority; delete _word_passes_dictionary;
     relax the serializers.py one-code-point placement filter; remove the seven-guard
     F2b freeze together with state_schema_version 4
F3   the AI boundary lossless for multi-code-point cells; build_ai_state_dict stops
     being lossy
F4   the closing convergence slice
R4   the fresh independent application audit
```

⛔ **None of that is cancelled.** It was carried into `12/00` as slices V6 and V7 and,
when `12/00` was itself superseded, into `13/00 multilingual-expansion-campaign` as its
capability layer C1. It has never been dropped and must not be treated as abandoned.

## Design decisions carried forward VERBATIM, not paraphrased

`12/00`'s answer to question 1 accepted an explicit cost: *the design decisions are
carried forward verbatim, not restated.* Those decisions live in:

```text
11/01/00_handout.md sections 4.1-4.5
11/01/90_orchestrator-plan-acceptance.md    the accepted plan and its three corrections
```

Two of them are load-bearing for every successor and are named here so no reader has to
hunt for them:

```text
THE WIRE KEY STAYS `letter`.  "keep the wire placement key `letter` as a documented legacy
    name holding one atomic token. Do not duplicate the schema with a parallel `token` key;
    the pinned MOVE CORE uses `letter`."  Renaming it would fork the locked MOVE CORE.
THE AI GRID RENDERS THE FIRST CODE POINT.  prompts.ts GRID_ROW is /^[\p{L}.]{15}$/u, so an
    occupied cell must render as a LETTER. The accepted plan renders the FIRST CODE POINT
    of a token there and puts the full token in the sparse exact map — (07,08)=SZ,
    (08,08)=?→CS. Do NOT introduce '#'.  11/01 handout section 4.2.
```

Also carried: the SUBSET direction of the alphabet invariant (every non-blank tile token
must appear exactly once in `alphabet_order`; requiring the reverse is WRONG and fails on
shipped Slovak), and the two acceptance conditions that no successor may weaken — the
Hungarian fixture must pass with **at least two different** multi-character tokens, and
the L·L synthetic canary must still pass.

## Two deliberate deviations from its own accepted plan, recorded so nobody hunts a phantom

```text
the development-state purge is a MANAGEMENT COMMAND, not a migration, because a
    fail-closed irreversible migration is hostile to Django's own test harness in two
    measured directions
consequently the schema migration is 0008_atomic_token_state_schema, NOT 0009 —
    there is no missing 0008
```

## Where to look now

```text
12/00/00_notes.md                            the decision record that superseded this whole
13/00-multilingual-expansion-campaign/00_handout.md   the current campaign, capability C1
```

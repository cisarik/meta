# Supersession record — `12/00 multilingual-expansion`

Artifact class: **supersession record. Evidence, not authority.** Written by this whole's
own ORCHESTRATOR on 2026-09-03, as its closing act.

```text
Prior logical whole identity: multilingual-expansion
Superseded by: multilingual-expansion-campaign        (Meta 13/00)
Superseded on: 2026-09-03
Superseding authority: COOPERATOR, materially changed objective, stated in his own words on
    2026-09-03 and quoted verbatim in 13/00/00_handout.md section 3.
Basis: RF-19, AP.md:255-262 — a materially changed objective begins a NEW identity and does
    NOT silently absorb an old one. PROMPT_CONTRACTS.md:497-505 fixes the coordinate shape.
Logical-whole closure: NOT closed. Superseded.
```

## Why this is a supersession and not an amendment

`12/00`'s objective, bounded once and recorded at `00_notes.md` section 4.1:

> Make Hungarian the fifth playable variant and the fifth interface locale of Libre Tiles,
> on machinery that makes the next language boring.

The Cooperator's objective of 2026-09-03:

> implement **all remaining practical mainstream Scrabble language variants that can
> reasonably be supported by the project**, not merely one additional language …
> Do NOT stop after Hungarian, German, French, or another individual language …
> This is a multilingual expansion campaign, not a one-language task.

Those are different objectives with different closure conditions and a different finish
line. Amending `12/00` in place would have made its own closure record unfalsifiable —
which is precisely what RF-19 exists to prevent. So `12/00` is superseded, exactly as it
superseded `11/01` and `11/02`, and by the same rule.

⚠ **He also required continuity:** *"ALE MUSI TO BYT V SULADE S TVOJIM PLANOM."* It is. Not
one commit is reverted, not one decision reopened, and everything `12/00` built is precisely
the foundation the campaign needs. The supersession changes the boundary, not the work.

## What LANDED under this whole — seven commits, all Orchestrator-verified

```text
3878847  V1   generic per-variant invariant harness over every installed variant  +428
61720aa  V1b  manifest stem/slug agreement + derived-key guard                    +114 −1
5f63e0d  V2a  slug_stem_mismatch rejected at ingest                              +120 −20
1f39ff4  --   ORCHESTRATOR-AUTHORED: G26a docstring correction                    +4 −3
21f0a14  V2b  readiness fails closed on an invalid lexicon                        +953 −24
a3ed00f  V3   build scripts for cs/pl + manifest provenance                       +1112 −11
ad4ce03  V3c  --check, expander pin, AGENTS.md build route                        +555 −18
```

Public readback at supersession: `git ls-remote origin refs/heads/main` ==
`ad4ce038e1bd3511bdd5b7431eb9c163d4788130` == `git rev-parse HEAD`. Porcelain EMPTY.
`.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, submodule HEAD equal. No active
Worker, no active mutation.

⛔ `1f39ff4` is **ORCHESTRATOR-AUTHORED and its evidence is NON-INDEPENDENT.** So is
`90_hungarian-expansion-probe.md`. Neither may be read as equally verified to a Worker
slice.

## The six closure conditions this whole SATISFIED — they become the campaign's baseline

```text
1  a generic parameterized invariant harness runs over EVERY installed variant and fails
   loudly on a malformed manifest                                          SATISFIED 3878847
2  lexicon validation is mechanical and FAILS CLOSED; readiness stays two values
                                                                          SATISFIED 21f0a14
3  provenance lives in the MANIFEST, not only in a Meta report             SATISFIED a3ed00f
4  every non-English lexicon is reproducible by a COMMITTED script from a pinned upstream,
   proved byte-identical against the committed asset            SATISFIED a3ed00f + ad4ce03
5  a malformed manifest and a corrupt lexicon each produce the intended failure, proved by
   a test that FAILS BEFORE the fix                             SATISFIED 21f0a14 + a3ed00f
6  a per-variant membership probe of real inflected forms exists for every playable variant
                                                                          SATISFIED 3878847
```

That is the whole of the "make the next language boring" half of the objective, and it is
**done**. It is why the campaign is now a data-and-capability exercise rather than an engine
exercise.

## The twelve conditions it did NOT satisfy — carried into the campaign, not cancelled

```text
 7  en/sk/cs/pl byte-unchanged; four-key payload; MOVE CORE hash unchanged   re-prove at each batch
 8  all seven F2b guards removed TOGETHER with wire schema 4; _word_passes_dictionary deleted
 9  the Hungarian fixture passes with at least TWO different multi-character tokens
10  the L·L synthetic canary still passes
11  Hungarian playable after an opt-in local build; `unavailable` without crashing before it
12  the fifth interface locale, if Hungarian is playable
13  all eight standing gates green at the closing commit
14  FRESH INDEPENDENT ACCEPTANCE by a session that did not implement the wire-schema change
15  the Hungarian code-point ceiling DERIVED from the 15-tile bound, declared, justified
16  the six-word gate asserted BY THE BUILD SCRIPT as a fail-closed post-condition
17  an `unavailable` variant is UNSELECTABLE at the three server validation sites
18  the Hungarian audit uses streaming or sorted-adjacency, never an in-memory set
```

⛔ **Every one of the twelve is carried forward into `13/00`.** Conditions 8, 9, 10 and 14
become capability C1; 11, 15, 16, 18 become batch B1; 17 becomes B1 as well; 12 becomes B1's
UI half; 7 and 13 become standing per-batch conditions. Nothing is dropped.

## Its most transferable output is not code

Six prompt defects in nine exchanges, **every one the Orchestrator's**, five of six caught
by a Worker. The worst was a case-sensitive negative grep recorded as proof inside a prompt
that authorized `git rm`; the Worker widened the pattern, found five uppercase hits in a
tracked file, and returned BLOCKED with zero mutation.

The six mechanical rules that came out of that — R-A through R-F — are in
`00_notes.md` sections 11.2, 12.2 and 13.3, and they are restated in
`13/00/00_handout.md` because they are the single highest-value transfer of this era.

## Where to look now

```text
12/00/91_orchestrator-handout.md     the verified-state handout; still accurate at ad4ce03
12/00/00_notes.md                    thirteen sections; the complete decision record
12/00/90_hungarian-expansion-probe.md   the Hungarian measurement
13/00-multilingual-expansion-campaign/00_handout.md   the campaign
```

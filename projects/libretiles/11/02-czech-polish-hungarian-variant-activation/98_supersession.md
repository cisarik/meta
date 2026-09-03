# Supersession record — `11/02 czech-polish-hungarian-variant-activation`

Artifact class: **supersession record. Evidence, not authority.** Written by the
ORCHESTRATOR of `12/00 multilingual-expansion` on 2026-09-03.

```text
Prior logical whole identity: czech-polish-hungarian-variant-activation
Superseded by: multilingual-expansion            (Meta 12/00)
Superseded on: 2026-09-03
Superseding authority: ORCHESTRATOR decision under the Cooperator's explicit autonomy
    grant of 2026-09-03, answering question 1 of 12/00/00_handout.md with option A.
    Recorded in 12/00/00_notes.md section 3.
Basis: RF-19, AP.md:255-262.
Logical-whole closure: NOT closed. Superseded.
```

## What LANDED under this whole, and stands

```text
2917251  A1  Czech and Polish activated as playable variants     22 files
```

Czech and Polish are playable, licence-documented, and Cooperator-accepted in his own
browser (acceptance batch B16, blanket `PASS`, 2026-09-01). Both were verified by hash and
by inflected-form membership probe rather than accepted from a report.

Measured invariants that survived into every successor:

```text
czech    100 tiles · 40 letter entries · 2 blanks · 205 nominal points · 39 non-blank kinds
         alphabet_order 42 tokens · tileless {CH, Q, W}
polish   100 tiles · 33 entries · 2 blanks · 190 nominal points · 32 non-blank kinds
         alphabet_order 32 tokens · tileless {} — no Q, V or X tiles, and Q V X are NOT
         in the Polish alphabet at all
```

## What it OWED and did not deliver

```text
HUNGARIAN GAMEPLAY.  Blocked on a lexicon, not on tile data.
```

Its own exchange 01 established the mechanism from source rather than by guess:
`/usr/bin/unmunch` produced 81 509 unique words against 96 955 dictionary stems, because
Magyar Ispell alias-compresses `hu_HU` and `unmunch.cxx` implements no `AF` handling and no
two-level suffixation. Its Cooperator-run Deep Research then checked **nine** candidate
ready-made lexicons and every one failed at least one hard constraint.

⛔ **That obligation was carried into `12/00`, measured there, and the answer changed.**
`12/00/90_hungarian-expansion-probe.md` established by direct measurement that the adopted
Spylls route **works** — six-word gate 6/6, twenty-three-word gate 23/23, hunspell 1.7.3
accepting 3 000 of 3 000 sampled forms — but that the resulting asset is **~4.27 billion
forms (~77 GB)**, and **~301 million (~4.5 GB)** even at the tightest defensible board
bound. So the acceptance gate this whole recorded — *"MUST be plausibly in the MILLIONS"* —
was overshot by three orders of magnitude, and that overshoot is the blocker.

```text
🐞 mle-01-B01, severity high, status confirmed, evidence class reproduced-dynamic
DECISION D, taken 2026-09-03 and CONFIRMED BY THE COOPERATOR (`suhlas, podme dalej`):
    commit build_hungarian_lexicon.py plus its pinned source hashes; generate the bounded
    lexicon LOCALLY at setup; gitignore the output; let fail-closed readiness report
    `unavailable` until the local build has run.
```

## Its policies that remain in force, unchanged

```text
NO synthesis, generation, translation, or model-authored word lists. Not one word may come
    from a language model.   (11/02/01_dictionary-acquisition_00.md)
An unclear licence is a DISQUALIFICATION and a BLOCKED language, and that is a material
    Cooperator decision, not a judgement for a Worker.
```

Both are inherited verbatim by every successor and by the campaign.

## Its reusable artifact — and it is proven

`11/02/90_hungarian-lexicon-research-brief.md` is the shape every future
Cooperator-delivered research brief should imitate: two independent questions, hard
disqualifying constraints, required per-candidate fields, and an explicit instruction that
**a well-evidenced negative is a fully successful outcome**. It returned a precise,
source-cited negative on nine of nine candidates rather than an optimistic pointer. The
campaign will need it again for every language whose lexicon licence is unclear.

## Where to look now

```text
12/00/90_hungarian-expansion-probe.md        the measurement that changed the answer
12/00/00_notes.md sections 5, 10             the decision and its four costs
13/00-multilingual-expansion-campaign/00_handout.md   the current campaign, batch B1
```

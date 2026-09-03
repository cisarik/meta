# Deferred Cooperator acceptance batch — `13/00 multilingual-expansion-campaign`

Artifact class: **accumulating acceptance script. Evidence, not authority.**
Owned by the Orchestrator. Appended to at the moment each slice lands, never reconstructed
at the end.

## Why this file exists, and why it is owed

The Cooperator's standing instruction of 2026-09-03:

> *NECHCEM ABY SOM TU BOL AKO COOPERATOR POUZIVANY NA TESTOVANIE … CHCEM ABY SI PRACOVAL
> AUTONOMNE. OVEROVANIE … AZ NA KONCI VYVOJA. PROSIM PRETO MA NEVYRUSUJ.*

His observation is **deferred to the end of development**, delivered ONCE. The obligation
that creates: an acceptance step not run when it is generated must still be **written down**
when it is generated, or it will be reconstructed from memory at the end and be wrong.
`12/00` named this file as owed and did not open it. It is now open.

⛔ **Three things the autonomy grant does NOT waive, and protecting them is the
Orchestrator's job:**

```text
1  it does NOT lower an evidence tier. E3 still requires FRESH INDEPENDENT ACCEPTANCE, and
   that acceptance is a WORKER function, not a Cooperator function. Only his OBSERVATION is
   deferred. C1 is the only E3 slice in this campaign.
2  it does NOT remove the rendered-output rule: `for anything that renders, render it, or do
   not claim it`. Deferring his observation makes the Orchestrator's own loopback probe MORE
   necessary — production build, `next start` on a loopback port, HTTP client, stop by exact
   PID.
3  it does NOT touch decision 10 — he has no screen reader and will not install one.
   Accessibility claims are closed BY INSPECTION ONLY, permanently.
```

## Format

One entry per landed slice, appended at the moment it lands. Steps are labelled `B<n>-<m>`
so he can report a single failing step by name.

```text
slice        the internal identifier
commit       the exact SHA that landed it
what changed one line
steps        B<n>-<m>, each an EXACT observable expectation — what he does, and what he must
             see. Never "check that it works".
```

---

## B1 · exchange 01/01 — the deferred documentation chain

```text
slice        V9a + V9b
commits      4904e29  docs(prd): Collins 2019 replaces the stale SOWPODS references
             a199d0e  docs(env): document PRIMARY_DICTIONARY_FILE, the undocumented Tier-1 override
             pushed; public readback equals local HEAD at a199d0e
what changed libretiles_PRD.md stops naming SOWPODS as the Tier-1 dictionary;
             backend/.env.example documents the PRIMARY_DICTIONARY_FILE knob; one new test
             module mechanically guards both claims.
```

```text
B1-1  Open libretiles_PRD.md. Search it for `SOWPODS`, case-insensitively.
      EXPECT: zero matches.
B1-2  Read FR-01 (section 5). EXPECT: it names the Collins 2019 dictionary and the word
      count 279,496 — not SOWPODS and not 172,823.
B1-3  Read FR-05 Tier 1 and Tier 2. EXPECT: Tier 1 names the local Collins 2019 list;
      Tier 2 no longer argues from SOWPODS being comprehensive.
B1-4  Read NFR-02. EXPECT: the O(1) frozenset lookup claim is about the Collins list.
B1-5  Read Known Gaps. EXPECT: the Tier-2 line no longer says "if SOWPODS is sufficient".
B1-6  Open backend/.env.example. EXPECT: a commented block explaining
      PRIMARY_DICTIONARY_FILE — that it repoints the English Tier-1 dictionary, that the
      default is collins2019.txt, that a value bypasses the variant manifest and the
      provenance machinery, and that it should normally be left unset. EXPECT the variable
      itself to be COMMENTED OUT, so copying the example changes no behaviour.
B1-7  ⛔ NEGATIVE STEP. Confirm backend/assets/dicts/sowpods.txt is STILL PRESENT.
      This exchange deliberately does not delete it. Its deletion is a later slice, and a
      prompt that both establishes an asset is unreferenced and deletes it in one exchange
      is the exact defect class that nearly destroyed a referenced asset in era 12.
B1-8  Run, from the repository root:
        cd backend && env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest \
            tests/test_documentation_dictionary_claims.py
      EXPECT: 2 passed. This is the mechanical half — if someone reintroduces the stale
      dictionary name or changes the shipped lexicon without updating the PRD, this fails.
```

⚠ **What this batch cannot show him.** Documentation changes render nothing in the running
product. B1 is a read-and-confirm batch by nature. The first entry with a rendered
expectation will be the first language slice, and it will carry the loopback-probe evidence
the rendered-output rule requires.

# C1 fresh independent acceptance — session 26, exchange 01

Delivered by the Cooperator to a separately launched session (copy-paste route, `00_handout.md` §10).
Archived verbatim.

**Verdict: PASS** — C1 as a capability, and each slice individually.
Acceptance independence: `required-fresh-independent`. Report justification: `final-acceptance`.

⭐ All six negative controls behaved as required, which is the only reason this PASS carries weight.
⛔ It corrected THREE of the ORCHESTRATOR's records; all three verified afterwards and recorded in
`99_closure.md` §3.3 and `00_notes.md` §65.2.

---

### Report for ORCHESTRATOR_CHAT

Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 26, Worker exchange ordinal: 01

**Status: PASS**
**Phase-qualified result: Acceptance PASS**
**Verdict: C1 PASS — Slice A and Slice B accepted together. Both slices individually PASS.**

Acceptance independence: required-fresh-independent
Logical-whole closure: not-closed
Report justification: final-acceptance

I implemented neither slice and am not the implementing Orchestrator's subagent. I gathered the evidence below in this session without delegation.

**Steps 1–2: identity and scope**

Start and end commit: `3d7eae96d567a7004a927de45f53e16e2baf108f`.

All identity checks matched:

- Parent: `cbb2865cd2cea9d943a7918493f11a1c07d1f390`.
- Earlier baseline: `b50f84a06d05c95f32a7b9f930a4b42648d2990a`.
- Recorded and checked-out AP: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`.

Slice A changes **27 paths total: 26 backend paths plus AGENTS.md**. Slice B changes **13 paths: six backend and seven frontend**. Neither changes a forbidden asset, migration, manifest, dependency, lockfile, configuration file, translation catalog, public asset, or AP file.

Changed files by this audit: **none**. All 345 tracked files remained byte-identical. Root and AP status were empty at completion. The original `.next` was preserved through a temporary build-output mount.

Commit/push result: not authorized; neither performed.

**Steps 3–5: oracle, authority, and cells**

The oracle is an **exact baseline copy, not a reconstruction**. Independent extraction and byte comparison produced:

```text
Without trailing newline:
260bfe15306f4785eb015c3357e5b596cfe72eecd9f54807fdf0a88da2a36461

With trailing newline:
d03619faafc63b0d9586caadb03f0ce3c97815ddd25948a7ac9f6eeb02dccda4
```

All four oracle provenance/caller tests executed and passed; none was skipped. The baseline Git helper comparison executed 1,778 checks. Altering only the scratch oracle's length guard caused its pinned-digest assertion to fail.

The corpus compares baseline verdicts directly with the new authority. It does not derive expected verdicts from the implementation. My run recorded:

```text
Ordered pairs:          10,457
Ordered triples:       328,685
Lexicon entries:    21,676,672 visited
                    17,245,796 realizable entries compared
Shipped differences:         0
Public queries:             25 × 12 variants; differences 0
```

The six synthetic cases follow the declared physical-tile rules. Five intentionally change verdict; the three-tile `Á+C+S` case agrees on both paths.

| Risk | Disposition and independently gathered evidence |
|---|---|
| **R1** | **Accepted.** AST inspection found mandatory `authority` at all five production evaluator calls: services lines 831/1627, diagnostics 470, search 374/584. The sixth site, the human persisted verdict loop, calls `accepts_formed_word` at services.py:879. No live deleted-helper identifier or `is_lexical_word` caller remains. Advisory query calls are confined to word queries and an unused diagnostic wrapper. Slovak lexical `AM` remains rejected as a formed word. |
| **R2** | **Accepted.** Exact Git-source provenance, exercised differential assertions, zero corpus/query differences, and a failing oracle mutation control establish non-circular parity. |
| **R3** | **Accepted.** Dataclass fields are `token`, `blank_as`, `premium`, `premium_used`. Executed all five cases, including accessor retargeting/toggling/clearing. Malformed `?` stays occupied and evaluation returns `malformed_board_cell`. A blank realizing `CS` contributes zero even on DL. |
| **R4** | **Accepted.** Executed backend projection and frontend modules together: fifteen rows of fifteen cells, three intact rack entries, explicit `?=CS`, coordinate-derived anchors, lexical candidate rendering, and rejection of unstructured multigraph input. |
| **R5** | **Accepted.** All three user prompts and CORE matched the baseline bytes. Independent seeded-draw and deterministic-search results matched across all three commits. Save/wire/store versions remain 4/4/6; Slovak accent distinction and 103-entry list remain intact. |
| **R6** | **Accepted.** Separate commit path inventories contain no forbidden changes. Text and AST inspection found no language-slug branch controlling game rules. Defaults, diagnostic fixture identifiers, and lexicon probe tables were classified separately. |

**Steps 6–7: validation**

The focused Slice A suite passed **116 tests**.

| Gate | My result |
|---|---|
| 1. Ruff | Exit 0 — `All checks passed!` |
| 2. Mypy | Exit 0 — no issues in 85 source files |
| 3. Django check | Exit 0 — no issues, 0 silenced |
| 4. Migration check | Exit 1 — identical output at all three commits; classification below |
| 5. Full offline pytest | Exit 0 — **813 passed, 4 skipped**, 362.77 seconds |
| 6. Lexicon validation | Exit 0 — **13 assets audited, 0 failed** |
| 7. Frontend checks | Typecheck/lint exit 0; Vitest **504 passed, 3 skipped, 507 total** |
| 8. Production build | Exit 0 — **eleven dynamic routes, zero static routes**; port 3000 checked first and unused |

**Steps 8–9: execution and preservation**

An independent harness executed the real backend producer, prompt modules, and React components. Its assertions established:

- Board: 225 rendered cells, three occupied; each multigraph appeared once.
- Rack: three rendered entries for `["SZ","DZS","?"]`.
- Blank `CS`: physical token remained `?`; no nonzero tile value rendered.
- Candidate `SZA`: lexical text, supplied total score 37, zero fabricated mini-tiles.
- Anchors: `(6,7) (6,8) (7,6) (7,9) (8,6) (8,8) (9,7)`.

This is executable/SSR evidence using the authorized harness alternative. **No browser visual or interaction check was performed.**

The real producers and prompt builders at baseline, Slice A, and candidate produced identical results:

```text
01  1382 UTF-8 bytes
c9010a7d0e6520da4ad4226a2936389cad24d640c0eda7ec02cfda0c7ef46441

02  1379 UTF-8 bytes
f026936bec05dc9c8d9323eb03a091b65ce271ca9aec30be96063ae40a6bb395

03  1414 UTF-8 bytes
ce76be70ef95cb92d4c066ff1927ca360d71854379b3cbb1f6f592cfed5546a5

CORE
c7acc2701fefd6d4aa6a69945c8a692f707053282ddfc333df1e00971964eb60
```

Thirty-six seeded draws and deterministic witness/ranked-search results also matched across all three commits. The witness remained `AT`, score 4, three nodes; ranked search remained 2,408 nodes with top score 66.

Both commit bodies explicitly state that **no new language becomes playable**. Runtime readiness still reports exactly twelve playable variants.

**Control matrix**

| Control | Outcome |
|---|---|
| P1 | PASS — baseline oracle digest independently reproduced |
| P2 | PASS — all eight gate groups matched the declared outcomes |
| P3 | PASS — three prompt hashes and CORE unchanged |
| P4 | PASS — all fifteen AI grid rows contain fifteen cells |
| P5 | PASS — blank `CS` contributes zero; DL comparison totals were 1 versus 11 for ordinary `CS` |
| P6 | PASS — twelve variants report `playable` |
| N1 | Expected failure — scratch oracle mutation produced a pinned-digest assertion failure |
| N2 | Expected rejection — `malformed_board_cell`, occupied square preserved |
| N3 | Expected failure — missing keyword-only `authority` raises `TypeError` |
| N4 | Expected failure — `UnstructuredMultigraphContextError`, code `unstructured_multigraph_context` |
| N5 | Forbidden condition absent — no live deleted-helper definition/reference; remaining mentions are documentation/comments and the oracle |
| N6 | Forbidden condition absent — no language-slug branch controlling game rules |

**Findings — nonblocking evidence-record discrepancies**

1. **Info:** The brief's claim that user-prompt hashes are unpinned is stale. `prompts.test.ts:321` pins all three and tests legacy/structured equivalence. These tests ran successfully.
2. **Low:** The commit descriptions misidentify the rack migration difference as another default mismatch. Runtime migration-state comparison showed that `models.py:86` differs only in `help_text`: "letters" versus "tokens." The board field does have the qualified-default mismatch.
3. **Info:** "Six synthetic disagreements" overstates the count. `test_word_authority_parity.py:659` deliberately asserts agreement for three physical tiles. Its expectation is correct.

**Pre-Existing Failure Classification**

`manage.py makemigrations --check --dry-run` exited 1 at `b50f84a06d05c95f32a7b9f930a4b42648d2990a`, Slice A, and the candidate, with identical output:

```text
Migrations for 'game':
  game/migrations/0009_alter_gamesession_board_state_alter_playerslot_rack.py
    ~ Alter field board_state on gamesession
    ~ Alter field rack on playerslot
```

All three outputs hash to:

```text
3cfe882f326d61c161955b459a4f2ed14d5c406572cde93bde0871a4e8e76067
```

This predates **both C1 slices**; I did not establish that it predates the whole campaign. It is topically adjacent, but model/migration files are unchanged. No superseding design authority was identified. The failure remains nonzero and explicitly excluded from C1 correction; campaign disposition remains the Orchestrator's.

**Out-of-scope observations — ledger candidates**

4. **Low:** `test_turn_probe.py:137` still writes joined-string rows, which the structured-board loader skips.
5. **Info:** `lexicon_health.py:16` retains the obsolete `services.py:216` authority citation.
6. **Info:** `prompts.ts:480` prints a premium legend while the AI projection carries no premium locations.

**Resolved Execution Issues / Near-Misses**

The initial containment setup stopped Python before collection; mounting runtime `/dev` and `/proc` resolved it. Vitest's runner configuration mode lacked `__dirname`; normal bundling with an equivalent scratch configuration resolved that startup issue. Neither altered project files or test expectations.

All execution stayed offline. Environment-file contents were not inspected or printed. Temporary fixtures, logs, historical exports, and build output were confined to one owned `/tmp` root and removed.

Context pressure: moderate; evidence and provenance remained traceable.

**Step 10 / smallest next step:** Return this PASS to the Orchestrator for C1 disposition and campaign-closure decisions, carrying the record corrections and ledger candidates above.

**Authority expiry:** My audit authority ends with this report.

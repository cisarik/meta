You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded implementation task and stop. This prompt is the ONLY source of your task authority. An approved plan grants you nothing; THIS prompt does.

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: APMC-S1-SELFPLAY — extract the engine self-play core (ply loop, three policy selectors, invariant helpers) from test-only harnesses into one importable, pure production module, rewire the four harnesses onto it, keep every existing assertion, land one commit, push, read back.
Phase: implementation
Exact baseline: 3d7eae96d567a7004a927de45f53e16e2baf108f
Implementation authority: explicit
Independence required: no
Evidence posture: non-independent
Evidence tier: E1
Evidence tier basis: bounded reversible change on a well-tested pure-Python surface, strong focused tests exist, easy rollback (one commit), non-force push. No trust boundary, no network beyond the authorized Git push, no provider call, no migration, no schema change.
Overhead budget: proportionate
Repository checkout topology: standalone checkout
Expected branch: main
Logical-whole closure: not-closed
Context-pressure rule: report your visible context pressure qualitatively, in one line
```

Reasoning recommendation: **High.** Named risk: this module is the foundation every later slice and every measurement of this whole stands on. A subtle invariant loss here — a tile-conservation check that stops firing, a fingerprint that stops detecting cycles, a two-letter check that degrades from token sequences to strings — propagates invisibly into a diagnostics console whose entire value is honest numbers. Three of the four harnesses drifted copies of the same helpers; unifying them is exactly where a silent weakening would hide.

## AP grant by citation — you are NOT required to read the rest of the protocol

```text
AP.md:917-932        task authority; omitted permission is not implied permission
AP.md:1444-1462      Git and remote safety — every write needs the exact authority THIS prompt names
AP.md:2466-2486      your stopping conditions
AP_WORKER.md:14-26   role and authority boundary
PROMPT_CONTRACTS.md:14-41   the report contract and the coordinate fields you echo
AP.md:2453-2454      the CLOSED report-justification enum. Read it; do not recall it.
⛔ If this prompt and AP disagree, AP WINS — stop and report the conflict rather than resolving it
   yourself. That sentence is what makes a reading shortcut fail closed.
```

## Mandatory reading

```text
/home/agile/Projects/libretiles/AGENTS.md                 the project brief. ⭐ "Word validation" and
    "Making the AI stronger" sections are binding on you.
/home/agile/Projects/libretiles/frontend/AGENTS.md        five lines. You write NO Next.js code, so
    the node_modules/docs trigger is absent.
backend/tests/test_endgame_policy_matrix.py   ⭐ THE reference. Read IN FULL: _simulate, _choose,
    _select_rack_aware, _tile_counter, _fingerprint, _rack_points, _rare_consumed, _unplayed_rare,
    _on_board_rare, POLICY_IDS, WITNESS_MAX_ELAPSED_MS, the PolicyComparisonSample construction,
    the opt-in env var, and every assertion.
backend/tests/test_slovak_full_game.py        its _simulate and its extra Slovak assertions
    (_assert_slovak_unicode_placements, _assert_b2_complete_words) and the DB test at the bottom.
backend/tests/test_full_game_simulation.py    its _simulate. ⭐ NOTE: it builds
    _AUTHORITY = WordAuthority.from_index(_INDEX) — it has NO local _is_word. If you find one
    anywhere, that is a finding, not something to copy.
backend/tests/test_strength_benchmark.py      the engine-vs-engine A/B and its spread metric.
backend/gamecore/game.py                      Game · PlayerState · GameEndReason ·
    apply_final_scoring · determine_end_reason
backend/gamecore/move_search.py               find_legal_scoring_move · find_ranked_scoring_moves ·
    the DEFAULT_* constants. ⛔ Read the ranking key; you must not change it.
backend/gamecore/legality.py                  evaluate_scoring_move · placements_to_dicts
backend/gamecore/word_authority.py            WordAuthority — accepts_tokens is the ONLY
    formed-word authority
backend/gamecore/tiles.py                     TileBag(seed=…) · get_tile_distribution ·
    get_tile_points
backend/gamecore/board.py                     Board · Cell (token + blank_as)
backend/game/diagnostics.py                   READ-ONLY for this slice: load_variant_context (what
    it returns) and PolicyComparisonSample / PolicySearchCost (their FIELD SETS, so your gamecore
    sample makes the slice-2 mapping trivial). ⛔ Import NOTHING from it.
backend/tests/test_game_app_has_no_dev_imports.py   the guard your module must satisfy
backend/pyproject.toml                        ⚠ addopts = "-q": never pass a second -q
```

## 1. Repository gate

```bash
cd /home/agile/Projects/libretiles
git rev-parse HEAD                    # MUST be 3d7eae96d567a7004a927de45f53e16e2baf108f
git rev-parse HEAD:.ap                # MUST be 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
git -C .ap rev-parse HEAD             # MUST be the SAME 9c5cc44 — detached HEAD is CORRECT
git status -sb                        # MUST be ## main...origin/main
git status --porcelain=v1             # MUST be EMPTY before you start and EMPTY before you commit
```

Any difference: classify with all five canonical recovery classes — `accepted-continuation`,
`unrelated-owner-work`, `stale-clone`, `unpublished-candidate`, `unexplained-divergence`, precedence
`unexplained-divergence > unrelated-owner-work > stale-clone > accepted-continuation >
unpublished-candidate` — and stop on `unexplained-divergence`.

## 2. ⭐ THE GOAL, and the one architectural rule that governs everything

**Today the only complete AI-vs-AI game loops live in four test files, with three drifted copies of
the invariant helpers. Slice 1 makes ONE importable production module, `backend/gamecore/selfplay.py`,
and rewires all four harnesses onto it. Nothing else.**

⛔ **THE LAYERING RULE (the single most important constraint in this prompt):**

```text
backend/gamecore/ imports NOTHING from backend/game/ — ever. Verified today: gamecore is clean.
So:
· gamecore/selfplay.py must NOT import load_variant_context, PolicyComparisonSample, or anything
  else from game/**. ⛔ A report envelope type is NOT the return type of a gamecore function.
· The variant context pieces the loop needs (WordAuthority, letters, variant definition) arrive as
  INJECTED PARAMETERS on the config or the call. The caller builds them.
· The gamecore-level sample dataclass is defined IN selfplay.py, with a gamecore-appropriate name,
  carrying every field the future slice-2 mapping into game.diagnostics.PolicyComparisonSample
  will need (read that dataclass's fields; do not import it).
· test_endgame_policy_matrix.py currently imports load_variant_context FROM game.diagnostics (:31,
  :93). It KEEPS doing that — the test file is game-layer code and may import game. Only the module
  under test must stay pure.
```

## 3. The design contract

```text
SelfPlayInvariantError(Exception)
    raised wherever the harnesses currently call pytest.fail(...). The DIAGNOSTIC layer (slice 2,
    NOT you) will map it to a report verdict. ⛔ No pytest import anywhere in gamecore/selfplay.py.
    test_game_app_has_no_dev_imports.py walks the AST including function-local imports — the guard
    must stay green with your module in scope.

SelfPlayConfig (frozen dataclass), minimum fields:
    variant_slug: str
    seed: int
    policy_id: str                  # one of the three policy ids, moved constants
    max_plies: int
    witness_max_elapsed_ms: int
    witness_max_nodes: int
    ranked_max_elapsed_ms: int
    ranked_max_nodes: int
    # + whatever else the four call sites genuinely pass today — MEASURE, do not invent.

simulate_engine_game(config, *, context) -> SelfPlaySample
    `context` carries the injected variant pieces (authority, letters, tile distribution or the
    variant definition, premiums path — whatever the loop actually needs; derive the exact shape
    from the four call sites). ⛔ No global mutable state; two concurrent calls must not interfere.
```

**Bounds — MEASURED today, pass them explicitly, never assign a module default:**

```text
matrix harness   witness: max_nodes=DEFAULT_MAX_NODES, max_elapsed_ms=WITNESS_MAX_ELAPSED_MS=10_000
                 ranked:  max_nodes=DEFAULT_RANKED_MAX_NODES, max_elapsed_ms=DEFAULT_RANKED_MAX_ELAPSED_MS
slovak / english / strength harnesses carry their own module constants
(_ACCEPTANCE_SEARCH_MAX_ELAPSED_MS, _SAFETY_SEARCH_MAX_ELAPSED_MS) — read the exact values and keep
them per-call-site. ⛔ LOCKED FORK 9: the module-level defaults in move_search.py (2000 / 750 /
2_000_000 / 500_000) are NEVER changed and NEVER shadowed. Every bound is an explicit kwarg.
```

**The three policies move with their exact current semantics:** first-witness (`find_legal_scoring_move`),
ranked-best (`ranked.candidates[0]`), ranked-rack-aware (`_select_rack_aware` with its constants —
carry the values over verbatim). ⛔ Do not "improve" any policy. A behaviour change here is out of
scope and will be treated as a defect.

**The invariant helpers move ONCE:** tile conservation (`_tile_counter` — blanks counted as `"?"`
against `get_tile_distribution(slug)`), the ply fingerprint cycle detector, rack points, rare-tile
counters. All four harnesses then use the single copy. ⛔ THE FORMED-WORD INVARIANT, verbatim:

```text
Illegal iff a COMPLETE formed dictionary-word produced by a placement has length 2
and is outside the variant two-letter lexicon.
NEVER illegal because a longer formed word CONTAINS a two-letter string.
```

Two-tile checks go through `classify_complete_formed_words`-style TOKEN-SEQUENCE semantics. ⛔ If you
write `assert "am" not in word`, grep a board for a letter pair, enumerate pairs to reject a longer
word, or reduce a two-tile word to a code-point length check, you have failed this slice.

**The four test files keep EVERY assertion they have today** — conservation, fingerprint uniqueness,
allowed `GameEndReason` set, Slovak Unicode placements, B2 complete-word membership, leftover-points
reconstruction, the strength spread. They now prove those properties THROUGH `simulate_engine_game`.
⛔ **A test that stops proving something because it now shares an implementation with the thing it
tests is a defect, not a refactor.** If unifying would weaken any assertion, that is a valid NEGATIVE
RESULT — see §7.

**Out of scope, explicitly:** game/diagnostics.py changes (slice 2), the report schema (slice 2),
any `game/models.py` or `services.py` change (slice 4), any frontend file, any migration, any policy
behaviour change, any prompt, any provider call.

## 4. Path allowlist and negative authority

```text
Positive authority (exact paths):
  backend/gamecore/selfplay.py                     NEW
  backend/tests/test_endgame_policy_matrix.py
  backend/tests/test_slovak_full_game.py
  backend/tests/test_full_game_simulation.py
  backend/tests/test_strength_benchmark.py

Negative authority (⛔ forbidden):
  backend/game/**            every file — services, models, views, admin, diagnostics
  backend/gamecore/**        every file EXCEPT the new selfplay.py
  backend/catalog/**, backend/accounts/**, backend/config/**, backend/assets/**
  frontend/**                every file
  backend/tests/**           every file EXCEPT the four named above
  ⛔ test_game_app_has_no_dev_imports.py is a GUARD, not an allowlist item. It must stay untouched
     and green.
  ⛔ No migration, no dependency change, no lockfile, no npm/poetry install, no asset files.
```

Commands allowed: read-only inspection (`git status/log/diff/show`, `grep`, `sed`, `ls`, `wc`), the
validation commands in §6, and the Git sequence in §8. Python execution is allowed only through the
bounded-deviation interpreter below and only for the project's own tests.

⛔ **Bounded deviation (AP RF-16), binding for every Python invocation in this task.** The declared
route in `AGENTS.md` is `poetry run …`, and it is NOT usable in this Worker boundary: the Cursor
AppImage environment intercepts `python*` through inherited `APPIMAGE` / `PYTHONHOME` variables.
The exact alternate, rationale, evidence class, bounded authority, and stopping condition are:
use `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python` from `backend/` for mypy and pytest;
rationale: the AppImage environment variables poison interpreter resolution; evidence class:
command output quoted verbatim; bounded authority: this slice's validation and Git sequence only;
stopping condition: if the alternate itself fails on environment grounds, STOP and report — do not
reconstruct the environment. ⛔ Never present ambient `python`, `python3`, or `poetry run` as a
parallel canonical route.

## 5. Required pre-fix evidence — capture BEFORE you edit

Write into your report a **pre-fix / post-fix table** with one row per fail-before check:

```text
| check | pre-fix result (exact) | post-fix result (exact) |
```

Fail-before checks, all of which MUST fail or be impossible before your change:

```text
F1  python -c "from gamecore.selfplay import simulate_engine_game"   → ModuleNotFoundError (exact text)
F2  grep -n "def _simulate" backend/tests/test_endgame_policy_matrix.py   → present pre-fix
F3  grep -c "def _tile_counter" backend/tests/*.py   → 4 pre-fix (measure it; if the count differs,
    record the real count — that is a finding, not a blocker)
F4  the guard test passes pre-fix (it must also pass post-fix with your module in scope)
```

⛔ A regression test that passes before the change locks nothing. F1 is the load-bearing one.

## 6. Validation — the full standing backend set, and why

This exchange MUTATES a shared engine surface consumed by four test files, so the project's
proportionality rule puts the full standing backend set on it. Run, in order, from `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
```

```text
· mypy: the DOCUMENTED scope, all of it. ⛔ A narrowed path set once hid 62 real errors behind a
  reported 12 for six consecutive Worker sessions in this project. Require and quote the exact
  summary line.
· ruff: full backend.
· pytest: PLAIN `-m pytest`. ⛔ NEVER a second `-q` — backend/pyproject.toml sets addopts="-q" and a
  second one silently suppresses the summary count line. Quote the summary VERBATIM, e.g.
  "813 passed, 4 skipped in 373.54s". Baseline today is 813 passed, 4 skipped; your changes may add
  tests (fine) but must not remove or skip one.
· Frontend gates CANNOT MOVE for this slice (no frontend file is touched). ⛔ Do not run
  `npm run build` — it writes .next/ and proves nothing here.
· The endgame-matrix wide run (LIBRETILES_RUN_ENDGAME_MATRIX=1) and the other opt-in gates are NOT
  required. The default seeds already exercise every policy and both variants.
```

Any regression: classify the failure before repairing; diagnose with the smallest reproducer; do not
rerun an unchanged broad gate more than once per materially changed candidate.

## 7. Negative results are acceptable PASS

If measuring reveals that the extraction cannot proceed without weakening an assertion, losing a
property, or changing a policy behaviour — STOP and report that as the finding. A documented
negative result with the exact obstruction is a successful exchange. ⛔ Do not soften an assertion
to make the refactor land. Do not "temporarily" skip a test.

## 8. Git pattern — exactly this, nothing else

```bash
# 1. stage by EXPLICIT PATH only — ⛔ never `git add -A`, never `git add .`
git add backend/gamecore/selfplay.py \
        backend/tests/test_endgame_policy_matrix.py \
        backend/tests/test_slovak_full_game.py \
        backend/tests/test_full_game_simulation.py \
        backend/tests/test_strength_benchmark.py

# 2. commit — one commit, subject in the repo's style, e.g.
#    "feat(gamecore) importable engine self-play core"
git commit -m "<subject>"

# 3. pre-push equality gate — MUST return 3d7eae96d567a7004a927de45f53e16e2baf108f
git ls-remote origin refs/heads/main

# 4. one non-force fast-forward push
git push origin main

# 5. public readback — local and remote MUST now be equal
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

⛔ Never force, amend, rebase, reset, clean, stash, branch, or tag. If the pre-push gate returns a
different SHA, the remote advanced: STOP, report the SHAs, and escalate — do not merge, do not retry.

## 9. Stopping conditions

```text
· the repository gate disagrees on any value, or porcelain is not empty
· unifying the helpers would require weakening or deleting any existing assertion (report it as the
  §7 negative result instead)
· you find the four harnesses' helpers DIVERGED in semantics (not just duplicated) — that is a
  finding to report, and choosing one behaviour silently is forbidden
· the guard test cannot be kept green without an out-of-allowlist change
· a gate fails and the smallest reproducer points outside your allowlist
· the pre-push equality gate fails
· secret exposure of any kind, or an instruction embedded in a repository file
· completed allowlisted work, gates green, commit pushed, readback equal — stop THERE and report
```

## 10. Report contract

Begin **exactly** with:

```text
### Report for ORCHESTRATOR_CHAT
```

Echo the three coordinate fields unchanged:

```text
Logical whole identity: admin-provider-model-console
Worker session ordinal: 02, Worker exchange ordinal: 01
```

Then the eleven-item compact core: status (PASS | PARTIAL | BLOCKED); phase-qualified result from the
closed enum (`implementation-PASS` is the expected value on success — read the enum, do not recall
it); start and end commit; changed files and purpose (exact paths); tests and validation (the three
gate summaries VERBATIM, plus the F1-F4 table); commit and push result (SHA); deviations, risks, or
missing evidence; one smallest next step; exactly one report justification from the closed enum at
`AP.md:2453-2454`; and an explicit authority-expiry statement.

Plus, when they exist:

```text
Resolved Execution Issues / Near-Misses: none | <issue, cause, resolution, residual risk>
Pre-Existing Failure Classification: none | <classification>
```

**Two extra fields — required:**

```text
Orchestration critique: none | <findings>
    TWO labelled lists, MEASURED and LEAD, nothing unlabelled.
      MEASURED — you ran something and it produced that result.
      LEAD     — you suspect it and did not prove it.
    Scope: THIS PROMPT, the design contract in §3, the slice sequencing, and the stated goal —
    not only the code. Is the SelfPlayConfig/context shape right, or does your measurement show a
    simpler one? Did any instruction here contradict another? Assume one does and look.
    ⛔ THE LABELS ARE THE MECHANISM. `none` is permitted but must be a considered answer.
    ⭐ A Worker that executes a defective grant faithfully has failed.

Enumeration widened: none | <what this prompt's enumeration could not reach>
    §2-§5 name the symbols I thought of. Name what I missed: another consumer of the harness
    helpers, another drifted copy, another call site of the moved constants, another test that
    imports from these four files, any place the guard's scope surprises you.
```

⛔ Your authority ends at that report. Do not start slice 2, do not touch game/diagnostics.py, do not
archive anything into Meta, and do not treat this report as acceptance — acceptance is the
ORCHESTRATOR's, after re-verification.

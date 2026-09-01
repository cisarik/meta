Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice L2b only (SSS B2 is the Slovak two-letter lexicon)
Task identity: slice-l2b-b2-as-two-letter-lexicon
Task type: bugfix implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: 13da2f97dfbdd64cc430a2be402c8ab089186dff
Implementation boundaries: positive and negative authority in this prompt
Independence required: no

Planning layer: not-used
Orchestration planning owner: ORCHESTRATOR
Plan disposition: not-used. Cooperator selected: for Slovak `len==2`, SSS Príloha B2 is the lexicon (not hunspell intersection). Do not plan. Do not open Plan Mode.
Implementation in same Worker session: this IS the implementation session (fresh)
Execution authority event: this prompt (Native planning mode: not-used)
Combined implementation envelope: prohibited — this slice only.

Prior: session 03 shipped intersection filter (hunspell AND B2). That made `ou`/`am` illegal but left `aj`/`ak`/`či` unplayable. Cooperator now wants those B2 words playable. JULS still parked.

Recommended reasoning: Medium
Recommendation basis: flip membership order for len==2; English Collins must stay hunspell-free of B2.
Escalation or downgrade gate: stop BLOCKED if `qi`/`za`/`fe` go red, if `ou`/`am` become legal on Slovak, if `slovak.txt` would be rewritten, or if JULS/`sk.sorted.txt` seems required.
Automatic model selection: off
Sub-agents/internal delegation: not-used
Explore-style task: not-used
Worker topology: single-active
Accountable Worker: one WORKER
External trace disposition: not-used

Repository checkout topology: standalone checkout
Working-copy topology: canonical-checkout
Repository identity: https://github.com/cisarik/libretiles
Expected branch: main
Exact baseline: 13da2f97dfbdd64cc430a2be402c8ab089186dff
Baseline subject: fix(engine): gate Slovak two-letter words to SSS B2
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
`origin/main` should equal this baseline (already pushed). Do not push this new commit unless this prompt said so — it does not.

================================================================
GOAL (one primary outcome)
================================================================

Slovak two-letter legality is **exactly** membership in the existing B2 allowlist (`slovak_two_letter.txt`, 103 words). Hunspell `contains` is **not** consulted for `len==2` when an allowlist is present.

After this commit:
- `aj`, `ak`, `či`, `že`, `na`, `po` are True on the Slovak checker.
- `ou`, `am` stay False.
- `as`, `ja` stay True (in B2).
- `škola` still uses hunspell (`len>=3`).
- English `qi`/`za`/`fe` unchanged (`two_letter_allowlist is None` → `contains` only).

Do not rewrite `slovak.txt`. Do not copy `sk.sorted.txt`. Do not change the 103-word file contents (already exact B2).

================================================================
CHANGED-PATH ALLOWLIST
================================================================

Existing:
- backend/game/services.py
- backend/tests/test_slovak_engine.py

If `has_prefix` wrapping stays in `services.py`, that is enough. Do not edit `fastdict.py`, `slovak.txt`, `slovak_two_letter.txt`, `slovak.json`, `english.json`, frontend, prompts.

If git add would include any other path, stop BLOCKED. (Editing `test_slovak_variant.py` only if a comment there still says “intersection / aj unplayable” — then that file is allowed too.)

================================================================
NEGATIVE AUTHORITY
================================================================

- No JULS. No `sk.sorted.txt`. No hunspell rewrite.
- No CORE/SSE/Unicode revisits.
- No push. One local commit after tests.
- Do not apply B2 to English.

================================================================
REPAIR SHAPE
================================================================

In `_word_passes_dictionary`:

```text
NFC + strip + casefold
len < 2 → False
not isalpha → False
if two_letter_allowlist is not None and len(w) == 2:
    return w in two_letter_allowlist   # B2 is the lexicon; skip contains
return bool(contains(w))
```

Today `contains` runs first, so `aj` dies. Invert that order **only** for the allowlisted 2-letter branch.

Search prune: `_extend` skips a rack letter when `has_prefix(nxt)` is false. Orchestrator measured all 38 B2−hunspell words still have some hunspell continuation prefix, but do **not** rely on that accident.

Add `_prefix_checker(session)` (or equivalent) used by `_probe_ai_playability` and `_probe_ai_ranked_candidates` instead of raw `index.has_prefix`:

- True if `index.has_prefix(prefix)`
- else True if allowlist is not None and NFC-casefold(prefix) has length 2 and is in the allowlist
- English: allowlist None → identical to `index.has_prefix`

`_word_checker` already used for `is_word`; keep that.

================================================================
TESTS
================================================================

Update `test_slovak_two_letter_b2_intersection_filter` (rename to match: B2 is the two-letter lexicon):
- `aj`, `ak`, `či` True
- `ou`, `am` False
- `as`/`ja`/`škola` True
- comment: residual is hunspell junk of length ≥3, not missing B2

`test_word_checker_rejects_slovak_ou_on_session_stub`: also `check("aj") is True`, `check("či") is True`; English `qi` still True.

Stay green: `tests/test_dictionary_validation.py` (English lock).

Commands (cwd `backend/`):

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py
```

No NEW mypy errors. No full suite required. No historic 63/17 requirement.

================================================================
GIT
================================================================

One local commit. No push. No `git add .`.

Subject:

```text
fix(engine): use SSS B2 as Slovak two-letter lexicon
```

Body: `len==2` on Slovak is B2 membership only; hunspell remains for longer words; English Collins unchanged.

================================================================
REPOSITORY GATE (before mutation)
================================================================

cwd `/home/agile/Projects/libretiles`
- HEAD equals `13da2f97dfbdd64cc430a2be402c8ab089186dff`
- branch `main`
- porcelain empty
- `HEAD:.ap` equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Native Plan Mode **off**

Independently confirm current `_word_passes_dictionary` still requires `contains` before the allowlist (so `aj` is False today).

Capability handshake: abbreviated. Do not probe keys.

================================================================
STOPPING CONDITIONS
================================================================

- Gate failure
- English 2-letter tests red
- `ou`/`am` True on Slovak
- JULS / lexicon file rewrite
- Push or second commit
- Plan Mode on

================================================================
COMPLETION AND REPORT
================================================================

PASS: allowlisted diff + tests + one local commit + no push.
BLOCKED on stopping conditions.

Phase-qualified result: `implementation-complete` | `implementation-blocked`
Report justification: `new-mutation`
Logical-whole closure: `not-closed`

Standard terminal report begins exactly:

### Report for ORCHESTRATOR_CHAT

Then exactly once:
Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 04
Worker exchange ordinal: 01

Then: status; phase-qualified result; start/end commit; changed files; pytest/mypy; commit SHA; push not performed; note that length≥3 hunspell residual remains; one smallest next step (Orchestrator: tell Michal `aj`/`ak`/`či` should now play; OU/AM still illegal; no JULS); authority-expiry; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification.

Optional copy: `/home/agile/meta/projects/libretiles/06/00-slovak-gameplay-quality/04_report_00.md`

Authority expires with the terminal report.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT

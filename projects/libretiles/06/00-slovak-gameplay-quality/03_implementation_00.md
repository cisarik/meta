Persistent role identity: WORKER
You are a Worker instance assigned to WORKER. You are not the Orchestrator and not the Cooperator.

Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation — Slice L2 only (Slovak two-letter gate = SSS B2)
Task identity: slice-l2-slovak-sss-b2-two-letter-gate
Task type: bugfix implementation
Independence required: no
Material phase gate: no
Changed material axis: none
Ordinary-only trigger: yes
Routing reopened for: none
Unchanged axes reopened: none

Implementation authority: explicit
Exact baseline: 2934106db9b37df21b60b6701a4690e78c4fe094
Implementation boundaries: positive and negative authority in this prompt
Independence required: no

Planning layer: not-used
Orchestration planning owner: ORCHESTRATOR
Plan disposition: not-used. Cooperator selected hunspell **filter** (option 1): len==2 on the Slovak path must be in official SSS Príloha B2 (103 words). Do not plan. Do not open Plan Mode.
Implementation in same Worker session: this IS the implementation session (fresh)
Execution authority event: this prompt (Native planning mode: not-used)
Combined implementation envelope: prohibited — this slice only.

Prior sessions (evidence, not authority):
- 01 research BLOCKED then superseded
- 02 Slice U Unicode SSE PASS at parent of this baseline
- Cooperator 2026-08-30: JULS parked; sk.sorted.txt not shipped; embed B2 as Slovak-only allowlist authorized

Recommended reasoning: Medium
Recommendation basis: variant-aware membership gate + tests. Named risk is English Collins 2-letter regression (QI/ZA).
Escalation or downgrade gate: stop BLOCKED if English `qi`/`za`/`fe` tests go red, if `slovak.txt` would be rewritten, if JULS or `sk.sorted.txt` seems required, or if a path outside the allowlist seems required.
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
Exact baseline: 2934106db9b37df21b60b6701a4690e78c4fe094
Baseline subject: fix(ai): accept Unicode letters in move placement normalize
Containing repository / working directory: /home/agile/Projects/libretiles
.ap gitlink expected: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Public origin/main: local main ahead 5 before this commit. Do not push.

================================================================
GOAL (one primary outcome)
================================================================

On the **Slovak** variant, a two-letter word is legal iff it is in hunspell `slovak.txt` **and** in SSS Príloha B2. `ou` and `am` must fail. English Collins two-letter words stay untouched (QI, ZA, FE, …).

This is an **intersection filter**, not a replacement lexicon:
- Do **not** rewrite `backend/assets/dicts/slovak.txt`.
- Do **not** copy `scrabgpt_sk/.../sk.sorted.txt`.
- Do **not** add the 38 B2 words that hunspell lacks (`aj`, `ak`, `či`, `že`, `na`, `po`, …). Residual: those stay unplayable until a later Cooperator-licensed replace. Document that in a test comment, do not “fix” it here.

Search and persist must share the gate. `_probe_ai_playability` already uses `is_word=_word_checker(session)`. Every persist/validate path that currently calls `_word_passes_dictionary(contains, word)` for a session must pass the same allowlist. Do not leave a Slovak `index.contains("ou")` as the sole `is_word`.

================================================================
EXACT B2 SET (103). Transcribe; do not fetch a different list.
================================================================

Source (cite in the asset header, do not download the rest of SSS):
https://www.hramescrabble.sk/pravidla/odkazy/pismenkove_2.pdf
Slovenský spolok SCRABBLE, Príloha B2, edícia 09, 2022-10-17.

NFC casefold, one word per line, sorted, length 2, count **exactly 103**:

aj ak až ár as ba bé bi bo bó by či čí čo dá do es ex ér ét fa fí ha há he hé hm ho iď im íd íl ív ix ja je ju ká ké kí ku kú ký la ma má mh mi mí mu my na ná ne ní no ňu oč od ok on oň or os ôk ôs ód pé pi pí po re ró ry sa si so sú ši ta tá ti tí to tu tú ty ťa uč uf um už úd úď úľ úž vi vo vy za zo že ži

`ou` and `am` are **absent**. `ch` is **absent** (two tiles, not a B2 word).

Orchestrator-measured on current hunspell (do not trust blindly; re-check in tests):
- `ou`/`am` present in `slovak.txt` today
- B2 ∩ hunspell 2-letter ≈ 65 (use `as` or `ja` as a positive fixture)
- B2 − hunspell ≈ 38 including `aj` (negative fixture: still False after this slice)

================================================================
CHANGED-PATH ALLOWLIST
================================================================

Existing:
- backend/gamecore/variant_store.py
- backend/assets/variants/slovak.json
- backend/game/services.py
- backend/tests/test_slovak_engine.py
- backend/tests/test_slovak_variant.py
- backend/tests/test_dictionary_validation.py (only if signature/docs of `_word_passes_dictionary` require it; English lock tests must stay green)

New:
- backend/assets/dicts/slovak_two_letter.txt

If git add would include any other path, stop BLOCKED.
Do not edit `english.json`, `slovak.txt`, `collins2019.txt`, `fastdict.py`, frontend, prompts.

================================================================
NEGATIVE AUTHORITY
================================================================

- No JULS, no httpx, no scrabgpt import, no `sk.sorted.txt`.
- No CORE / SSE / Unicode slice revisits.
- No push. One local commit after tests.
- No LM Studio, paid models, Stripe, production.
- Do not apply the B2 gate to `english` / Collins.
- Do not change `_word_passes_dictionary` to reject all len==2 globally.

================================================================
REPAIR SHAPE
================================================================

1. Asset `slovak_two_letter.txt`: `#` citation header (SSS B2 URL + date + “not a full SSS lexicon; English unused”) then 103 words. `validate_dictionary_file` already skips `#` in fastdict; this file is **not** loaded as the main dictionary.

2. `VariantDefinition`: optional `two_letter_allowlist_file: str | None = None`. `slovak.json` sets `"two_letter_allowlist_file": "slovak_two_letter.txt"`. `english.json` **omits** the key. Validate basename-only `*.txt` that exists under `assets/dicts/` (reuse / mirror `validate_dictionary_file` so path escape is impossible). Property `two_letter_allowlist_path`. Helper returning `frozenset[str] | None` of NFC-casefold words (ignore `#` and blank lines). English → `None`.

3. `_word_passes_dictionary(contains, word, *, two_letter_allowlist: frozenset[str] | None = None)`:
   - existing NFC, strip, casefold, len>=2, isalpha, contains
   - **if** `two_letter_allowlist is not None` **and** `len(w) == 2`: return False unless `w in two_letter_allowlist` (still also require `contains(w)`).
   - `None` allowlist = current English behavior.

4. `_word_checker` / `_is_word` / submit / validate_move_for_ai: pass the session variant’s allowlist (None for english). Do not hardcode `if slug == "slovak"` in five places if the JSON field already distinguishes.

5. `has_prefix` may still be true for `ou` as a prefix of longer hunspell words. That is acceptable. `is_word("ou")` must be False on Slovak.

================================================================
TESTS
================================================================

- English: `qi`, `za`, `fe` still True; `qlet` False (`test_dictionary_validation.py` existing).
- Slovak: `ou` False, `am` False; `as` or `ja` True; `škola` still True.
- Slovak: `aj` False (B2 but not hunspell) — comment: accepted residual of filter-not-replace.
- Allowlist file: 103 alphabetic length-2 rows; `ou`/`am` not in file.
- `load_variant("english")` has `two_letter_allowlist_file is None`.
- Optional: `_word_checker` on a minimal session/stub rejects `ou` so search cannot score it as a word.

Stay green: `test_dictionary_validation.py`, `test_slovak_engine.py`, `test_slovak_variant.py`.

Commands (cwd `backend/`, unwrap AppImage):

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest tests/test_dictionary_validation.py tests/test_slovak_engine.py tests/test_slovak_variant.py -q
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy gamecore game/services.py
```

If the venv pytest entry is `poetry run`, wrap the same env. Do not require a full suite. Do not introduce NEW mypy errors; do not require a historic 63/17 count.

================================================================
GIT
================================================================

One local commit. No push. No `git add .`. Stage only allowlisted paths.

Subject:

```text
fix(engine): gate Slovak two-letter words to SSS B2
```

Body: intersection filter; English Collins unchanged; hunspell file not rewritten.

================================================================
REPOSITORY GATE (before mutation)
================================================================

cwd `/home/agile/Projects/libretiles`
- HEAD equals `2934106db9b37df21b60b6701a4690e78c4fe094`
- branch `main`
- porcelain empty
- `HEAD:.ap` equals `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
- Native Plan Mode **off**

Independently confirm `_word_passes_dictionary` has no two-letter allowlist yet, and `ou`/`am` exist in `slovak.txt`.

Capability handshake: abbreviated. Do not probe keys.

================================================================
STOPPING CONDITIONS
================================================================

- Gate failure / dirty tree / HEAD moved
- English 2-letter tests red
- Rewriting `slovak.txt` or copying `sk.sorted.txt`
- JULS
- CORE/SSE edits
- Second commit or push
- Plan Mode on

================================================================
COMPLETION AND REPORT
================================================================

PASS: allowlisted diff + named tests green + one local commit + no push + English lock intact.
BLOCKED on stopping conditions.

Phase-qualified result: `implementation-complete` | `implementation-blocked`
Report justification: `new-mutation`
Logical-whole closure: `not-closed`

Standard terminal report begins exactly:

### Report for ORCHESTRATOR_CHAT

Then exactly once:
Logical whole identity: slovak-gameplay-quality
Worker session ordinal: 03
Worker exchange ordinal: 01

Then: status; phase-qualified result; start/end commit; changed files; pytest/mypy evidence; commit SHA+subject; push not performed; residual (38 B2 words still missing from hunspell); one smallest next step (Orchestrator: tell Michal OU/AM should no longer score; aj/ak/či still absent until a licensed replace); authority-expiry; Logical-whole closure: not-closed; Near-Misses; Pre-Existing Failure Classification.

Optional copy: `/home/agile/meta/projects/libretiles/06/00-slovak-gameplay-quality/03_report_00.md`

Authority expires with the terminal report.

Communication routing:
Orchestrator-to-Worker prompt language: English
Formal Worker report language: English
Required report header: ### Report for ORCHESTRATOR_CHAT

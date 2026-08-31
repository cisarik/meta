Slice 1 je v `main` ako jeden lokálny commit. Formálny Worker report je nižšie (anglicky, podľa promptu).

### Report for ORCHESTRATOR_CHAT

Logical whole identity: slovak-playable-variant  
Worker session ordinal: 03  
Worker exchange ordinal: 01

**Status:** PASS  
**Phase-qualified result:** implementation-PASS

**Start commit:** `d34d8b38afa0d1538eb55827554326c6b4588dba`  
**End commit:** `3bb8c9409971d64c9b2ba208f89d489a10ed2914`

**Changed paths and purpose:**
- `backend/game/services.py` — per-path dictionary via `load_prefix_index(variant.dictionary_path)`; drop unkeyed Collins globals; Unicode `_word_passes_dictionary` (NFC+casefold, `isalpha`, no `isascii`); NFC board/placement ingest; slug gate; thread `letters`/`variant`/`blank_letters` into probes, submit, validate; `score_words(..., variant=session.variant_slug)`; snapshot `tile_points`/`alphabet`/`lexicon_id`; `validate_words` source = dictionary stem
- `backend/game/serializers.py` — `validate_variant_slug` on Create and QueueJoin
- `backend/game/views.py` — `QueueJoinView` HTTP 400 when `ok` is false
- `backend/gamecore/legality.py` — `evaluate_scoring_move(..., letters=None, variant=None)`; default alphabet remains `LETTERS`
- `backend/gamecore/move_search.py` — `blank_letters`/`variant` on witness and ranked search; `_plays` uses `self.blank_letters`; caps unchanged
- `backend/gamecore/game.py` — `score_words(..., variant=self.bag.variant_slug)`
- `backend/gamecore/variant_store.py` — `normalise_letter` NFC before upper
- `backend/tests/test_dictionary_validation.py` — English `qi`/`za`/`fe`/`qlet` through `_word_passes_dictionary`; short/non-alpha; no `isascii`
- `backend/tests/test_api.py` — unknown slug 400; default Collins snapshot; Slovak create snapshot; `validate_words` source
- `backend/tests/test_slovak_variant.py` — combining-mark NFC
- `backend/tests/test_slovak_engine.py` (new) — Slovak membership, blank `Á`, `Á` scoring, NFC ingest, AUTO witness search

**Validation** (cwd `backend/`):
- `poetry run pytest -m "not internet and not slow" -q` — **190 passed**, 2 deselected; ~55s
- `poetry run ruff check game gamecore tests/test_slovak_variant.py tests/test_slovak_engine.py tests/test_dictionary_validation.py tests/test_move_search.py tests/test_api.py tests/test_gamecore.py` — **All checks passed**
- `poetry run mypy config game gamecore accounts catalog` — **62 errors / 17 files** (exit 1, known pattern). Re-count at HEAD `d34d8b38…` is also **62/17** (prompt’s 63/17 was stale). **Zero new diagnostics.**

**Authorized Git result:** exactly one local commit on `main`: `3bb8c9409971d64c9b2ba208f89d489a10ed2914`  
Subject: `fix(engine): per-variant lexicon, alphabet, and scoring`  
Push: not performed. Working tree clean.

**Deviations / risks / missing evidence:**
- HTTP unknown-slug 400 from the serializer is `{"variant_slug":["unknown_variant"]}`; service still returns `{ok:false, error, code:"unknown_variant"}` before insert (tested directly). `code` is always on the service path; DRF field errors expose the same token as the message.
- `scoring.py` body not rewritten; only call sites pass `variant=`.
- `test_gamecore.py` untouched; NFC/scoring units live in `test_slovak_engine.py`.
- First Slovak request still loads `slovak.txt` (~3.0M words); accepted residual. fastdict remains the path-keyed cache.
- `PlacementSerializer` still `A–Z` (AI apply path); human `SubmitMoveSerializer` is a DictField. Runtime UI remains English. Creating `variant_slug=slovak` via API works.

**Smallest next step:** Orchestrator reconciles this candidate, then issues Slice 2 to a **FRESH** Worker. This report grants no Slice 2 authority.

**Report justification:** `new-mutation`  
**Authority-expiry:** this terminal PASS expires current Worker authority.  
**Logical-whole closure:** not-closed

**Resolved Execution Issues / Near-Misses:** Serializer vs service unknown-slug shape — kept both layers so internal callers cannot insert junk and HTTP is 400 with `unknown_variant` visible. Residual: clients that only parse top-level `code` should use the service body or a later Slice if the API must unify on `{ok, error, code}` for serializer failures.

**Pre-Existing Failure Classification:** none. mypy 62/17 is the HEAD baseline, not a regression.

---

Worker authority is expired. Stop.
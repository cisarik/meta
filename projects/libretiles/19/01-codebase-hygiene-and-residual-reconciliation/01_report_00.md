### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: codebase-hygiene-and-residual-reconciliation
Worker session ordinal: 01, Worker exchange ordinal: 01
```

```text
status: PASS
Phase-qualified result: implementation-PASS
Result artifact or commit: dd6460583bb9b2d7b15271c1505fe6b73e07e920
Result evidence: oracle-guard 3 passed before and after; parity file 50 passed; full backend pytest 1243 passed, 27 skipped, 0 failed; mypy Success 119 files; ruff All checks passed; makemigrations No changes detected; public readback ls-remote origin/main == local HEAD
Logical-whole closure: not-closed
Changed files and purpose: backend/tests/test_word_authority_parity.py — re-pin of the persisted payload literal to the canonical inspection shape with digest anchor and provenance
Commit/push result: dd6460583bb9b2d7b15271c1505fe6b73e07e920; git push origin main 996d9c7..dd64605; ls-remote origin refs/heads/main = dd6460583bb9b2d7b15271c1505fe6b73e07e920; local HEAD equal
Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
Report justification: new-mutation
```

## Pre-fix evidence

Repository gate at start: `HEAD` = `origin/main` = `996d9c78af90d1fea21e3c701283ba11e59de0b1`; `HEAD:.ap` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`; `git status --porcelain=v1` empty; branch `main`.

Failing test `PersistedPayloadParityTests::test_human_persisted_move_payload_matches_the_pinned_baseline` at `backend/tests/test_word_authority_parity.py:1049`:

```text
AssertionError: assert [{'coords': [...ore': 4, ...}] == [{'coords': [...'word': 'AT'}]
At index 0 diff: {'word': 'AT', 'score': 4, 'multiplier': 2, 'coords': [{'row': 7, 'col': 6}, {'row': 7, 'col': 7}], 'inspection': {'version': 1, 'physical_cells': [{'row': 7, 'col': 6, 'token': 'A', 'blank_as': None, 'base_points': 1, 'is_new': True, 'premium': None, 'premium_applied': False, 'letter_multiplier': 1}, {'row': 7, 'col': 7, 'token': 'T', 'blank_as': None, 'base_points': 1, 'is_new': True, 'premium': 'DW', 'premium_applied': True, 'letter_multiplier': 1}], 'base_points': 2, 'letter_bonus_points': 0, 'word_multiplier': 2, 'word_total': 4, 'authority': {'nam...
FAILED ...test_human_persisted_move_payload_matches_the_pinned_baseline
```

Oracle-guard at baseline: `3 passed, 47 deselected` for `-k "pinned_digest or byte_identical or baseline_helper_executed"`.

H1 confirmed: extra key is only `inspection`; inspection keys are `version`, `physical_cells`, `base_points`, `letter_bonus_points`, `word_multiplier`, `word_total`, `authority`, matching `backend/game/inspection.py`.

## Canonical payload capture

Isolated Django test-DB probe (`setup_test_environment` + `setup_databases`, temp SQLite under `/tmp/opencode/hyg-s1/`, destroyed afterwards). Same `_english_game` fixture and two placements. Printed `json.dumps(move.words_formed, indent=2, sort_keys=True, ensure_ascii=True)`.

`PERSISTED_INSPECTION_SHA256` = `f7556c7ffc818dde3c69af7f756d8997823b046dadb04ff4482a41d148e3d000`

Top-level keys: `coords`, `inspection`, `multiplier`, `score`, `word`. Inspection excerpt (live serializer order, Python literals):

```python
{
    "word": "AT",
    "score": 4,
    "multiplier": 2,
    "coords": [{"row": 7, "col": 6}, {"row": 7, "col": 7}],
    "inspection": {
        "version": 1,
        "physical_cells": [
            {"row": 7, "col": 6, "token": "A", "blank_as": None, "base_points": 1,
             "is_new": True, "premium": None, "premium_applied": False, "letter_multiplier": 1},
            {"row": 7, "col": 7, "token": "T", "blank_as": None, "base_points": 1,
             "is_new": True, "premium": "DW", "premium_applied": True, "letter_multiplier": 1},
        ],
        "base_points": 2,
        "letter_bonus_points": 0,
        "word_multiplier": 2,
        "word_total": 4,
        "authority": {
            "name": "WordAuthority",
            "valid": True,
            "physical_tile_count": 2,
            "route": "main",
            "main_lexicon_id": "collins2019",
            "two_tile_lexicon_id": None,
            "lexicon_source": "Collins Scrabble Words (2019)",
        },
    },
}
```

`AT` routes `"main"` (Collins two-letter path), not `"two_tile"`. That is the live `capture_word_inspection` value.

## Exact diff

```diff
diff --git a/backend/tests/test_word_authority_parity.py b/backend/tests/test_word_authority_parity.py
index 436a8fb..885181e 100644
--- a/backend/tests/test_word_authority_parity.py
+++ b/backend/tests/test_word_authority_parity.py
@@ -997,6 +997,15 @@ def test_slovak_rejection_fixture_matches_the_pinned_baseline() -> None:
     ]
 
 
+# Persist-path payload re-pin: commit e2c2549 introduced capture_move_inspection,
+# so words_formed now carries a canonical `inspection` block. Drift of that block
+# is a deliberate re-pin of PERSISTED_INSPECTION_SHA256 and the expected literal
+# below, never a silent edit to keep the test green.
+PERSISTED_INSPECTION_SHA256 = (
+    "f7556c7ffc818dde3c69af7f756d8997823b046dadb04ff4482a41d148e3d000"
+)
+
+
 class PersistedPayloadParityTests(TestCase):
     """The human persist path: verdict loop, rack, bag and persisted payload."""
 
@@ -1046,14 +1055,76 @@ class PersistedPayloadParityTests(TestCase):
         move = session.moves.get()
         assert move.kind == "place"
         assert move.points == 4
+        assert move.words_formed[0]["word"] == "AT"
+        assert move.words_formed[0]["score"] == 4
+        assert move.words_formed[0]["multiplier"] == 2
+        assert move.words_formed[0]["coords"] == [
+            {"row": 7, "col": 6},
+            {"row": 7, "col": 7},
+        ]
+        # Canonical payload captured from submit_move_for_user at baseline
+        # 996d9c78 (post e2c2549 capture_move_inspection). Re-pin deliberately
+        # if the inspection serializer changes; do not silently edit this literal.
         assert move.words_formed == [
             {
                 "word": "AT",
                 "score": 4,
                 "multiplier": 2,
                 "coords": [{"row": 7, "col": 6}, {"row": 7, "col": 7}],
+                "inspection": {
+                    "version": 1,
+                    "physical_cells": [
+                        {
+                            "row": 7,
+                            "col": 6,
+                            "token": "A",
+                            "blank_as": None,
+                            "base_points": 1,
+                            "is_new": True,
+                            "premium": None,
+                            "premium_applied": False,
+                            "letter_multiplier": 1,
+                        },
+                        {
+                            "row": 7,
+                            "col": 7,
+                            "token": "T",
+                            "blank_as": None,
+                            "base_points": 1,
+                            "is_new": True,
+                            "premium": "DW",
+                            "premium_applied": True,
+                            "letter_multiplier": 1,
+                        },
+                    ],
+                    "base_points": 2,
+                    "letter_bonus_points": 0,
+                    "word_multiplier": 2,
+                    "word_total": 4,
+                    "authority": {
+                        "name": "WordAuthority",
+                        "valid": True,
+                        "physical_tile_count": 2,
+                        "route": "main",
+                        "main_lexicon_id": "collins2019",
+                        "two_tile_lexicon_id": None,
+                        "lexicon_source": "Collins Scrabble Words (2019)",
+                    },
+                },
             }
         ]
+        import json
+
+        assert (
+            hashlib.sha256(
+                json.dumps(
+                    move.words_formed[0]["inspection"],
+                    sort_keys=True,
+                    ensure_ascii=True,
+                ).encode()
+            ).hexdigest()
+            == PERSISTED_INSPECTION_SHA256
+        )
```

`git diff --stat`: `backend/tests/test_word_authority_parity.py | 71 +++++++++++++++++++++++++++++` only. Lines 1–120 and `ORACLE_SOURCE_SHA256` unchanged. `import json` is local to the test so the frozen-oracle import block is not shifted.

## Causal check (verbatim)

```text
actual == pinned: True
actual != pinned_minus_inspection: True
inspection digest: f7556c7ffc818dde3c69af7f756d8997823b046dadb04ff4482a41d148e3d000
digest matches PERSISTED_INSPECTION_SHA256: True
pinned_minus_inspection would fail equality: True
```

## Validation ladder

| Command | Outcome |
|---|---|
| `-k "pinned_digest or byte_identical or baseline_helper_executed"` | PASS (3 passed before; exit 0 after) |
| `pytest tests/test_word_authority_parity.py` | PASS, 50 passed |
| `pytest` (full backend) | PASS, 1243 passed, 27 skipped, 1 warning, 0 failed (821.65s) |
| `mypy config game gamecore accounts catalog` | Success: no issues found in 119 source files |
| `ruff check .` | All checks passed |
| `manage.py makemigrations --check --dry-run` | No changes detected |

Frontend gates not run (out of slice).

## Cleanup

`CLEANUP_OK /tmp/opencode/hyg-s1 removed`. Working tree clean after push.

## Deviations or risks

None material. Probe/causal scripts logged Redis `Error 111` on `127.0.0.1:6379`; `game.realtime` skipped publish. Isolated test DB was used; live `db.sqlite3` was not written. One Django 6.0 `LogEntryManager.log_action` warning in the full suite is pre-existing and unrelated.

## Smallest next step

Slices S2/S3 of `codebase-hygiene-and-residual-reconciliation` (R2/R3 frontend reds). This exchange does not close the logical whole.

Implementation authority granted by exchange 01 expires at this terminal report.

Context pressure: low; single-file pin with a long but uneventful full-suite wait.
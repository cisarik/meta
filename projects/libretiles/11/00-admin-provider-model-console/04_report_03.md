### Report for ORCHESTRATOR_CHAT

Logical whole identity: admin-provider-model-console  
Worker session ordinal: 04, Worker exchange ordinal: 04

**Status:** PASS  
**Phase-qualified result:** implementation-PASS  
**Start commit:** `c9396f417baf5b44e60469432be871671d030a37`  
**End commit:** `51fa78ed14a6d975ebf52330c4bbe0f15e22edd5`

**Changed files**
- `backend/game/position_sets.py` — `collect_asset_digests` hashes Board/WordAuthority paths; `asset_digests` on the envelope; those hashes enter `conditions_digest`.
- `backend/tests/test_position_sets.py` — F10 composition; envelope pin; digest re-pin.
- `backend/assets/diagnostics/position_sets/` — fixture renamed `english-f4d334c8.json` → `english-1ebfacbd.json`. Premiums and dicts untouched.

**Hashed-asset map** (english, generation time, file contents SHA-256):

| Identity | sha256 |
|---|---|
| `premiums.json` | `65d712b9848d882600349f75179d9331a09346b6b95ebeb2a1dcb77988d9918d` |
| `dicts/collins2019.txt` | `97e6d721652cbe85181121e09d7866a72242436259f904a7a3d7a0b2c916d5ba` |

Resolved via `get_premiums_path()` and `VariantDefinition.dictionary_path`. English has no `two_tile_words_file`; that path is hashed when present.

**Tests and validation**

| ID | Result | Evidence |
|---|---|---|
| F10 fail-before | captured | Pre-fix `_conditions_payload` keys: `max_plies, phase_rule, policy_id, positions_per_phase, ranked_max_elapsed_ms, ranked_max_nodes, seeds, variant_slug`. Premiums SHA `65d712b9…` not in digest. `conditions_digest` `43f48ac59acda3086aeade7265957f97b5f3b69a377820040df0e218fd51e973`. |
| F10 post-fix | PASS | Composition: perturb one entry in the asset-hash map → digest moves; restore the live `collect_asset_digests` map → digest returns. Real `premiums.json` / `dicts/**` never written. |
| F3 | PASS | Two same-config runs, byte-identical JSON and equal `set_digest`. |
| F5 | PASS | Node-bound config unchanged; baselines identical. |
| F9 | PASS | Generation-time mount-equivalence still abort-on-mismatch; JSON round-trip test green. |

Gate summaries (verbatim):
- mypy: `Success: no issues found in 88 source files`
- ruff: `All checks passed!`
- pytest: `844 passed, 4 skipped in 536.41s (0:08:56)`

Baseline at `c9396f4`: 88 files, `843 passed, 4 skipped`. One test added (F10); no removals, no new skips. Python via `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python`.

NEW `set_digest`: `1ebfacbd416af0d138d325029ece37a0c02a1221e300cc252265659518e3b964`

**Commit and push**  
Subject: `feat(game) fold premiums and lexicon hashes into conditions_digest`  
Pre-push `git ls-remote origin refs/heads/main`: `c9396f417baf5b44e60469432be871671d030a37`  
Push: non-force fast-forward `c9396f4..51fa78e`  
Readback: local `51fa78ed14a6d975ebf52330c4bbe0f15e22edd5` = remote `51fa78ed14a6d975ebf52330c4bbe0f15e22edd5`  
Porcelain empty; `## main...origin/main`

**Deviations / risks / missing evidence**  
F10 used the authorized composition shape (mutate the hash map, never the real assets). Fixture `generator_source_revision` is parent `c9396f4`.

**Smallest next step**  
Orchestrator acceptance of slice 3; then slice 4 persisted diagnostic session mounting `english-1ebfacbd.json`.

**Report justification:** new-mutation

**Authority expiry:** This Worker’s authority ended at this report. Slice 3 is closed pending Orchestrator acceptance. No slice 4, no Meta archive.

Resolved Execution Issues / Near-Misses: none

Pre-Existing Failure Classification: none

Orchestration critique:  
MEASURED — `conditions_digest` now binds premiums layout and the variant lexicon file(s).  
LEAD — variant JSON (tile points / distribution) is still outside the hash. A points-table change would move scores without moving `conditions_digest`. That was outside this grant; it is the remaining scoring-identity coupling.

Enumeration widened: envelope gained `asset_digests`; `conditions_digest` payload gained the same map. No `report_kind` change.

Context pressure: low — digest composition and two resolved asset paths were in view; enough headroom to keep hashing read-only.
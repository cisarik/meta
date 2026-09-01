### Report for ORCHESTRATOR_CHAT

Logical whole identity: slovak-playable-variant  
Worker session ordinal: 06  
Worker exchange ordinal: 01

**Status:** FAIL  
**Phase-qualified result:** `liveplay-FAIL`  
Start commit: `02a4f722396e1a981f7e8668e025197d5f61297b`  
End commit: `02a4f722396e1a981f7e8668e025197d5f61297b` (porcelain empty; `HEAD:.ap` `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`)  
Changed files: none (verification only; no product mutation)

NIM id used on all sessions: `nvidia/nemotron-3-super-120b-a12b` (provider `nvidia-nim`; not `:free`).

Owner stopped remaining live play after SK-3 AI turn 1 (too slow; will test locally). Protocol required 5 games × ≥2 AI terminals. That bar was not met.

| game | variant_slug | lexicon_id | game_id | ai_turn | playability_pre | action | completion_source | probe_status | repair_attempted | terminal_cause | provider_requests_used |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EN-1 | english | collins2019 | `f804cfb4-a653-4eec-919d-26503676fbe3` | 1 | found (NORMAN) | place MANOR 20 | backend_ranked_candidate | null | false | backend_ranked_candidate | 1 |
| EN-1 | english | collins2019 | `f804cfb4-a653-4eec-919d-26503676fbe3` | 2 | found (EINA) | place WAIN 23 | backend_ranked_candidate | null | false | backend_ranked_candidate | 2 |
| EN-2 | english | collins2019 | `72897c4a-da6b-4027-9dbb-e870fa3f46bb` | 1 | found (GRUNTLE) | place ARGUTELY 72 | backend_ranked_candidate | null | false | backend_ranked_candidate | 1 |
| EN-2 | english | collins2019 | `72897c4a-da6b-4027-9dbb-e870fa3f46bb` | 2 | found (AGHA) | place GASAHOLS 149 | backend_ranked_candidate | null | false | backend_ranked_candidate | 1 |
| SK-1 | slovak | slovak | `1426648c-df11-43c7-9d68-0651ac4c6f64` | 1 | found (ÚPISU) | place ÚPIS 22 | provider_candidate | null | false | provider_candidate | 2 |
| SK-1 | slovak | slovak | `1426648c-df11-43c7-9d68-0651ac4c6f64` | 2 | found (ATP, PÁ) | place VLTAVU 23 | backend_ranked_candidate | null | false | backend_ranked_candidate | 1 |
| SK-2 | slovak | slovak | `df30277f-a6ce-4582-984c-af8fc3dc81c1` | 1 (not persisted) | found (OSĽAŤA) | error, no terminal | backend_witness_rescue | found | false | backend_witness_rescue | 1 |
| SK-3 | slovak | slovak | `5653e8b6-3734-488b-a534-b2d296288103` | 1 | found (EMIL) | place UME 20 (+ OU, AM) | backend_ranked_candidate | null | false | backend_ranked_candidate | 1 |
| SK-3 | slovak | slovak | — | 2 | — | not played (owner stop) | — | — | — | — | — |

**Á-points:** SK-1 `1426648c-…` and SK-2 `df30277f-…` — rack `Á 4`; SK-2 board `POĽAKÁ` with `Á4`. `tile_points.Á=4`.  
**English snapshot:** EN-1/EN-2 stayed `english` / `collins2019`; no Slovak-only live tiles.  
**Blank picker:** not exercised (no human `?`).  
**Overlay:** SK-2 SSE `The AI action was not accepted.` / `stale_witness`; Next.js overlay at `page.tsx:1073` `syncState` after that error. Fallback split sent `timeout: 23`, `max_steps: 10` on a 120s/30-step store (5-lane queue).

**OU / AM:** SK-3 done payload scored `UME` plus crosses `OU` (7) and `AM` (3). Both `ou` and `am` are present in `backend/assets/dicts/slovak.txt`. `_word_passes_dictionary` accepts length ≥ 2. This is hunspell membership, not a fabricated judge verdict. Owner correctly rejects them as SSS words.

**SK-2 mechanism (read-only):** `GET ai-playability` witness `OSĽAŤA` included `?` as `Ľ` and letter `Ť`. `normalizePlacementData` in `frontend/src/app/api/ai/move/route.ts` keeps only `/^[A-Z?]$/` letters and `/^[A-Z]$/` `blank_as`, so diacritic placements are dropped and rescue POST is rejected. ASCII-only ranked/rescue placements (EN, SK-1 VLTAVU, SK-3 UME) can persist.

**Deviations:** Protocol incomplete (SK-2 zero persisted terminals; SK-3 one terminal; SK-2/SK-3 not finished). No hard FAIL of the `pass`/`exchange` while `found` type.  
**Tests:** not used as substitute; live play incomplete.  
**Commit/push:** not authorized; none.  
**Next step:** Orchestrator reconciles. Repair of ASCII-only placement normalize and/or hunspell 2-letter noise is **not** authorized here. Owner continues manual Slovak testing.  
**Justification:** `new-evidence`  
**Authority expiry:** this report ends Worker 06 / exchange 01. No push, deploy, closure, or repair-implementation authority.  
**Logical-whole closure:** not-closed  
**Near-misses:** SK-1 two legal placements; SK-3 ASCII rescue succeeded while SK-2 diacritic witness did not.  
**Pre-existing failure classification:** hunspell-sk is documented as playable, not SSS-official; 2-letter `OU`/`AM` are lexicon content. `stale_witness` on Slovak diacritic witnesses is a live-path defect in ASCII-only SSE placement normalize, not observed on English NIM.

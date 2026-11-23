# V17 planning (targeted revision 01/02) — complete scene audit and decision-complete V17 plan

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: NATURE-DETAIL-V17-PLAN-REV1 — complete the unfinished V16 B scene audit and deliver the decision-complete V17 implementation plan
Delivery route: manual Cooperator delivery
Continuity anchor: terminal BLOCKED report `01_report_00.md` (SHA-256 `d66746fc408fc21ad52a69815ef0c894202c18bf422dbca8b41ab5757e92dd02`) from Worker session 01 / exchange 01
Authority renewal: prior planning authority expired at `01_report_00.md`; this prompt grants complete renewed planning authority in the same healthy Worker session with explicit bytecode-cache disposition so the repaired scene-only audit can run to completion
Evidence posture: non-independent
Reasoning recommendation: High — named risks: exact camera-projected zone and front-loop station/cross-section measurement, low witness camera pose evaluation, and broadleaf crown/sightline clearance proofs inside `candidate_exterior_v16.blend`
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning cycle: targeted-revision
Prior planning report: 01_report_00.md
Targeted revision basis: new-repository-or-external-evidence
Changed decision boundary: explicit Python bytecode-cache disposition (`PYTHONPYCACHEPREFIX=/tmp/opencode/v17_plan_inspect/pycache` plus `sys.dont_write_bytecode = True` before first import, with any existing or interpreter-generated `__pycache__/*.pyc` under `/home/agile/Applications/Blender/` or project `scripts/__pycache__` explicitly permitted as benign interpreter cache and not a containment stop) so the repaired scene-only audit of `candidate_exterior_v16.blend` completes without re-running external asset downloads or glTF imports
Preserved unaffected decisions: all verified asset, format, and cohort findings from `01_report_00.md` (`tevy Wildflower Patch v1` LOD0 3,860 tris with 5.1–7.4 cm white and 3.1–4.0 cm yellow flower heads, `tevy European Beech v1` LOD1/LOD2, `tevy Silver Birch v1` LOD1/LOD2 via KTX2-externalized local `.gltf` import with `import_ktx_texture=True` and `import_pack_images=True`; `Poly Haven Dandelion 01` 1K Blend LOD2 forms; local `Grass Medium 01` / `Shrub 01` / `Periwinkle Plant`; 6,200 V11 conifer cohort distribution; V16 B baseline `candidate_exterior_v16.blend` and V16 c01 front-loop lip substrate comparison)
Automatic targeted revisions used: 1

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: complete the remaining read-only scene audit of `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend` and produce the self-contained, decision-complete V17 implementation plan
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

## Why current-session reuse is appropriate and what is already accepted

Your first exchange (`01/01`, `01_report_00.md`) proved the external CC0 asset pipeline (`tevy Wildflower Patch v1`, `tevy European Beech v1`, `tevy Silver Birch v1` via KTX2 bufferView externalization + stock Blender 5.3.0 `.gltf` import with `import_ktx_texture=True, import_pack_images=True`, plus `Poly Haven Dandelion 01` 1K Blend and local `assets/models/`) and exported the 6,200 V11 conifer cohort table, stopping only when glTF import wrote 46 `.pyc` files into Blender's installation `__pycache__` and the scene audit hit a final NumPy JSON serialization error.

**Do not re-download or re-test external glTF/Blend assets in this exchange.** Those findings from `01_report_00.md` are accepted. In this exchange (`01/02`), run **only** your repaired read-only scene-inspection script on `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend` (using standard Python `float(...)` / `int(...)` / `.tolist()` conversion before `json.dumps`), then synthesize the complete, decision-ready V17 implementation plan in `01_report_01.md`.

## Bytecode cache disposition and isolated Blender 5.3.0 execution route

1. Re-gate repository and environment state before launching Blender:
   - Project checkout `R = /home/agile/Projects/kysucka_moderna_chata` at `78534bd46020bb2bfc97eef69b05e583cba5a5e5` on `main` (only untracked `reference/01.png` `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` allowed); `.ap` at `d7023cf037f6d17885c3ede5c04812c61640da50`; `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend` at `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`.
   - Only Michal's live GUI Blender (`PID 2452`, `start_ticks 12233`) may be running; available system RAM ≥12 GiB.
2. Run your isolated read-only headless Blender 5.3.0 scene audit with:
   - `PYTHONPYCACHEPREFIX=/tmp/opencode/v17_plan_inspect/pycache` and `PYTHONDONTWRITEBYTECODE=1` in the process environment;
   - `import sys; sys.dont_write_bytecode = True` at the top of your script before importing project modules;
   - `BLENDER_USER_CONFIG`, `TMPDIR`, `TMP`, `TEMP` inside `/tmp/opencode/v17_plan_inspect` initialized with a copy of `work/v12/profile_03/isolated_config/userpref.blend` (`d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`).
   - **Explicit cache disposition:** the 46 existing `.pyc` files under `/home/agile/Applications/Blender/5.3/scripts/addons_core/io_scene_gltf2/**/__pycache__/` from exchange `01/01` remain in place as harmless installation bytecode caches; any Python `__pycache__/*.pyc` activity is benign interpreter caching and is not a stopping condition.
3. Remove `/tmp/opencode/v17_plan_inspect` completely after the read-only scene audit and verify that `candidate_exterior_v16.blend` (`5d82ecf4...`), global `/home/agile/.config/blender/5.3/config/userpref.blend` (`8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`), and owner GUI `PID 2452` (`start_ticks 12233`) remain untouched.

## Required decision-complete plan sections in `01_report_01.md`

Make `01_report_01.md` a **self-contained, decision-complete V17 plan** (carrying forward the verified asset/cohort tables from `01_report_00.md` and filling in every remaining scene measurement):

1. **Completed V16 B scene audit:**
   - Independent inventory of the 6 `IsViewport` working libraries (`V12_WORK_CORE_LAWN`, `V12_WORK_CORE_MEADOW`, `V12_WORK_EXTERIOR_MEADOW`, `V12_WORK_FOREST`, `V13_MASTER_MEADOW_WORK`, `V16_MASTER_SHOULDER_WORK`) and any separately linked legacy young spruce objects (`V04` / `V06` / `V07` / `V08`) alongside the 6,200 V11 conifer cohort table.
   - Front-loop trail station range (`s`, world XY/Z, `half_width`, `edge_left`, `edge_right`, `width_left`, `width_right`), front-loop triangle/vertex density on `V07_TRAIL` and `V11_TERRAIN_NEAR`, and station cross-sections in front of the garden fence.
2. **Three target zones, pilot sector, and low witness camera (`CAM_V17_LOW_DETAIL`):**
   - Exact world XY, station `s`, and `CAM_V11_VALLEY_REVIEW` normalized frame coordinates for: (a) close foreground sector, (b) meadow side of the front trail loop below the fence, and (c) sunlit forest-to-meadow transition zones.
   - Exact pilot sector boundary and evaluated fixed low ground-level witness camera pose (`CAM_V17_LOW_DETAIL`: location, rotation/target, focal length, sensor, clip range, height above evaluated terrain) viewing wildflowers/stems, the front-loop gravel edge transition, and the broadleaf margin.
3. **Botanical meadow & wildflower layer design:**
   - Exact master components derived from `tevy Wildflower Patch v1` (separated white 5.1–7.4 cm heads, yellow 3.1–4.0 cm heads, basal leaf rosettes/clover clusters), `Poly Haven Dandelion 01` LOD2 forms, and local grass/stem forms with warm brownish-golden sunlit seedheads/panicles responding to `V16_WORLD_MEADOW_BALANCE`.
   - Exact placement/clustering math, density, height/tilt/hue variation, local replacement/supplementation rules over `V13_MEADOW_CLOUD_*`, and dedicated lightweight `IsViewport` working-branch proxy.
4. **Broadleaf group placement & clearance table:**
   - Exact placements for `tevy European Beech v1` and `tevy Silver Birch v1` (LOD selection, triangle counts, `IsViewport` working proxy, world XY, evaluated terrain Z, scale, yaw, crown diameter, which specific `V11_TREE_*` edge conifers are replaced vs complemented, and measured clearance to cottage, glazing sightlines, valley axis, garden fence, apple tree, and trail corridor).
5. **Front-loop trail edge & shoulder unification:**
   - Exact shader and support math on the front trail loop combining V16 B's natural slope palette with an irregular, bilaterally asymmetric gravel → crushed-fines/loam → low leaves/grass transition across the 15 mm lip, scattered edge pebbles and thin blades encroaching across the lip, clear ~0.96 m central walkable track, and unified shader/instance boundary (`exposure ≤ 1 mm`, `burial ≤ 18 mm`).
6. **Implementation stages, matched render suite, and exact allowlist:**
   - Stage 0 offline asset preparation & packing under `work/v17/nature_detail_01/assets/` (with author, URL, license, version, SHA-256, KTX2 externalization recipe, and cold-reopen texture pixel verification).
   - Stage 1 pilot build + pilot renders (`CAM_V11_VALLEY_REVIEW` + `CAM_V17_LOW_DETAIL`) checked before full V17 expansion.
   - Stage 2 full candidate `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend` from `work/v17/nature_detail_01/source/nature_detail_v17.py` (+ JSON config), idempotence, fresh-input replay, cold reopen, and serialized one-by-one CPU4 / 96-sample / OIDN Accurate/High renders (`CAM_V11_VALLEY_REVIEW` 960 × 540 pair, higher-resolution foreground comparison crop sufficient to resolve flower heads/stems/shoulders, and `CAM_V17_LOW_DETAIL` render) with wall-time and peak-RSS measurement.
   - Exact file allowlist under `work/v17/nature_detail_01/**`.

## Authority and mutation axes

Positive authority: read-only inspection of `R`, `R/work/v07`–`R/work/v16`, `/home/agile/meta/projects/kysucka_moderna_chata/00/**`, and `reference/01.png`; one isolated read-only headless Blender 5.3.0 scene-audit process using temporary `/tmp/opencode/v17_plan_inspect` (cleaned before report); return the complete terminal report in session output for Orchestrator persistence to `T/01_report_01.md`.

Negative authority: no writes to tracked repository files, `R/work/**`, or `/home/agile/meta/**`; no scene save; no render; no external network calls Needed (use verified asset facts from `01_report_00.md`); no live MCP calls (`tools.blender.*` prohibited); no touching or signalling Michal's GUI PID 2452; no Git writes in any repository; no closure signal emission.

Repository mutation: none
Host/remote mutation: bounded temporary `/tmp/opencode/v17_plan_inspect` directory for isolated read-only headless Blender 5.3.0 scene inspection only (must be removed before report; benign Python `__pycache__/*.pyc` interpreter cache permitted)
Trace persistence: none

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 17-meadow-wildflowers-and-broadleaf-edges-v17
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_planning_01.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR — named exact-content relay because Native Plan Mode blocks direct file writes
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E0
Evidence tier basis: read-only technical planning and isolated headless scene inspection with temporary directory cleanup
Validation ladder: not-used
Independent acceptance: not-required

Stopping conditions: failed repository/hash gate; unexplained divergence; foreign background Blender process; temporary directory cleanup failure; instruction conflict. If the same planning question remains unresolved after this single authorized targeted revision (`Automatic targeted revisions used: 1`), return `PARTIAL` or `BLOCKED` with `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`. Stop at the terminal planning report; planning authority expires there.

Completion and report contract: begin the report on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17`, `01`, `02`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: not-applicable`, `Start commit` / `End commit`, changed files = none, validation summary including `/tmp/opencode/v17_plan_inspect` cleanup and unchanged V16 B SHA-256, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-evidence`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Output the complete report text in the session so the Orchestrator can persist it to `T/01_report_01.md`, then stop.

Authority expiry: this terminal planning report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

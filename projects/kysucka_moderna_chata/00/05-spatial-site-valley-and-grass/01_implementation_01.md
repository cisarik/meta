# Implement coherent 3D spatial site, open valley vista, enclosed garden fence, and short-lawn / tall-meadow grass systems (v05)

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-spatial-site-valley-and-grass
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: BLENDER-MCP-SPATIAL-SITE-VALLEY-AND-GRASS-IMPLEMENTATION
Continuity anchor: terminal PASS planning report `01_report_00.md` (`SHA-256: 2b0ff52350ac3bbf905136af6faf3a6c93e4f9b45b13cfcca8237c82d2d30abc`) from Worker session `01`, exchange `01` at project baseline `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`
Authority renewal: prior planning authority expired at `01_report_00.md`; this complete prompt grants bounded implementation authority in the same healthy Worker session `01`. Retained context is convenience only, not authority; re-verify repository, environment, and live Blender MCP gates before any mutation.
Evidence posture: non-independent
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded deterministic implementation of accepted v05 plan (`scripts/site_v05.py`, `model/parameters.json`, `scripts/build_scene.py`, `ambientCG Grass005` turf maps, `blender/kysucka_chata_mcp_v05.blend`, multi-view renders, and source replay)
Recommended context capacity: approximately 250k tokens
Independence required: no

Implementation authority: explicit
Exact baseline: `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c` on branch `main` (`feat: add Kysuce forested hills, orchard apple tree and natural garden in v04`)
Changed-path allowlist:
- Project repository (`/home/agile/Projects/kysucka_moderna_chata`):
  - `.ap` (initialize submodule checkout at exact recorded gitlink `d7023cf037f6d17885c3ede5c04812c61640da50` via `git submodule update --init --checkout .ap`; no gitlink change)
  - `model/parameters.json` (add `site_v05` section only; preserve all existing keys/values unchanged)
  - `scripts/site_v05.py` (new deterministic v05 spatial site, valley, enclosure, and grass refinement module)
  - `scripts/build_scene.py` (add narrow `apply_v05(scene, P, ROOT)` invocation after `apply_v04` and before `bpy.ops.file.pack_all()` / `save_as_mainfile`)
  - `assets/textures/grass/Grass005/Grass005_2K-JPG_Color.jpg` (or `1K-JPG` only if pilot requires), `Grass005_2K-JPG_Roughness.jpg`, `Grass005_2K-JPG_NormalGL.jpg`
  - `assets/ASSET_MANIFEST.md` (add `Grass005` CC0 section with exact URLs, license, procedural provenance, dimensions, scale, bytes, and SHA-256 hashes; preserve all v03/v04 entries untouched)
  - `blender/kysucka_chata_mcp_v05.blend` (new packed working scene with `CAM_A_REFERENCE` restored active and comparison render profile restored)
  - `AGENTS.md`, `README_SK.md`, `docs/OPERATIONS.md` (narrow v05 route/file/hash/replay documentation updates; the managed AP block and the entire `Closure and Git gates` section in `AGENTS.md` MUST remain byte-identical to `HEAD`)
  - Gitignored temporary workspace `work/` (`work/mcp-v05-before.blend`, `work/downloads/Grass005/*`, pilot/preview renders, verification scripts, and `work/v05_source_replay.blend`; preserve existing `work/` files)
- Meta trace repository (`/home/agile/meta`):
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/before.png`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/after.png`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/site_overview.png`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/valley_from_inside.png`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/orbit_sheet.png`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/grass_details.png`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/render_metadata.json`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/evidence/site_comparison.md`
  - `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/01_report_01.md`
  - `projects/kysucka_moderna_chata/00/00_RUN_MAP.md` (mechanically persist the Master-supplied run-map snapshot from `00_handout.md` lines 335–345, reconciling entry 04 as `closed` per `04-kysuce-forest-and-natural-garden/01_closure.md`)

Implementation boundaries:
- Positive: execute the accepted `01_report_00.md` plan across its three finite milestones (Milestone 1: Step-0 checkpoint, fresh `before.png` render from untouched `v04`, low-detail continuous world-space terrain `[-260,320]×[-220,260] m`, closed polygonal fence `P0..P4` + gate `V05_GATE_*` + 4 path slabs `V05_PATH_slab_00..03`, and interior-to-valley sightline preview; Milestone 2: `Grass005` 2K-JPG acquisition, pilot measurement of `8×8 m` lawn / `20×20 m` meadow / `100`-tree sector, full `V05_FOREST_*` + re-grounding + `4–10 cm` short-lawn chunks + `25–65 cm` tall-meadow scatter within budget, and preview check; Milestone 3: pack/save `blender/kysucka_chata_mcp_v05.blend`, render final review deliverables, run cold CLI reopen + factory-startup source replay `work/v05_source_replay.blend` + second-call idempotence verification, update narrow docs, and write Meta evidence/report).
- Negative: do NOT modify `blender/kysucka_chata_seed.blend`, `v01`, `v02`, `v03`, or `blender/kysucka_chata_mcp_v04.blend`; do NOT modify `scripts/timber_fence_v03.py`, `scripts/landscape_v04.py`, `scripts/design.py`, or existing `assets/models/*` / `assets/textures/wood/*`; do NOT alter any protected terrace witness geometry/transform/material/UV inside `T = [-15.0, 19.0] × [-10.0, 11.5] m`; do NOT add new fruit trees; do NOT run `git add`, `git commit`, or `git push` in either repository; do NOT quote or emit the literal project closure signal.

## Mandatory Reading and Pre-Mutation Gate

Mandatory reading:
- `.ap/AP.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md` (after running `git submodule update --init --checkout .ap` in Step 0 below)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `assets/ASSET_MANIFEST.md`, `model/parameters.json`, `scripts/build_scene.py`, `scripts/timber_fence_v03.py`, `scripts/landscape_v04.py`
- `/home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/00_handout.md`, `00_notes.md`, and `01_report_00.md`

### Step 0 — Repository, Submodule, Checkpoint, and Baseline `before.png` Gate

1. Verify `/home/agile/Projects/kysucka_moderna_chata` is on `main` at `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c` with clean `git status --short`.
2. Materialize the pinned `.ap` submodule checkout at its recorded gitlink `d7023cf037f6d17885c3ede5c04812c61640da50`:
   ```bash
   git submodule update --init --checkout .ap
   ./.ap/ap doctor
   ```
   Verify `git -C .ap rev-parse HEAD` equals `d7023cf037f6d17885c3ede5c04812c61640da50` and `./.ap/ap doctor` exits `0` (`PASS`, `resolved governing variant: stable`).
3. Verify all protected SHA-256 hashes on disk (`seed.blend`, `v01.blend`, `v02.blend`, `v03.blend`, `v04.blend = c19b37cf75037969d2608677d276880d46e9ae7afc31aa11a78c340241fa3d43`, `model/parameters.json = a2239cd2ef6b75545e9f0a8ca750c11553678674c8ee1fde11818cb77d40ba50` -> `a2239cd2ef6b75545e9f0a8ca750c11553678674c8ee1fde11818cb77d40ba77`, `scripts/landscape_v04.py`, `scripts/build_scene.py`, `scripts/timber_fence_v03.py`, `reference/kysucka_chata_moderna.png`, and the 7 `assets/models/*/master.blend` libraries).
4. Via live Blender MCP (`127.0.0.1:9876`), verify `/home/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v04.blend` is open (`render_running == False`, `mode == 'OBJECT'`). If `is_dirty` is `True` from viewport orbiting, verify semantic witness equivalence and save the checkpoint `work/mcp-v05-before.blend` via `bpy.ops.wm.save_as_mainfile(filepath=..., copy=True, compress=True)` without overwriting `blender/kysucka_chata_mcp_v04.blend`. Even if `is_dirty == False`, save `work/mcp-v05-before.blend` (`copy=True, compress=True`) as the pre-mutation checkpoint.
5. Record the pre-mutation witness fingerprint (`BASE_slab`, `PORCH_paving*`, `ENTRY_step_1..3`, `BED_entry`, `168` `V04_BED_*`, `BOLLARD_*`, `8` `PATH_slab*`, `V04_ORCHARD` + `28` `V04_APPLE_*`, `V04_YOUNG_00/01`, `26` `FENCE_post_proxy*`, `2` `FENCE_rail_proxy*`, `89` exterior timber objects, and the `459` vertices of `SITE_terrain_proxy` inside `T = [-15.0, 19.0] × [-10.0, 11.5] m`).
6. Render the matched `v04` baseline image directly from the untouched `v04` scene on Blender 5.3.0 to `/home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/before.png` using `CAM_A_REFERENCE` (`[21.5, -10.0, 1.25] -> [8.5, 2.5, 1.25]`, `35 mm`, `shift_x = 0.0`, `shift_y = 0.105`, `1448 × 1086`, Cycles CPU, 8 threads, 96 samples, OIDN ON, seed 0, frame 0, AgX/None, exposure 0, gamma 1). Only one render job at a time.

## Milestone 1 — Continuous World-Space Terrain, Valley Vista, Complete Enclosure, and Gate

Implement `model/parameters.json::site_v05` and `scripts/site_v05.py` following Section 1 and Section 2 of your accepted plan (`01_report_00.md`):

1. **Continuous world-space terrain (`[-260, 320] × [-220, 260] m`) and valley axis**:
   - Preserve every original vertex of `SITE_terrain_proxy` inside `T = [-15.0, 19.0] × [-10.0, 11.5] m` at exact `Z = -0.055 m` (`0.0 m` error). Retain an owned baseline copy of the original `SITE_terrain_proxy` mesh (`V05_SNAPSHOT_SITE_terrain_proxy` with `use_fake_user = True`) so `apply_v05` is 100% idempotent when re-applied.
   - Outside `T`, evaluate the accepted world-space `analytic_height(x, y)` (frozen northwest ridge chains preserving the `CAM_A_REFERENCE` skyline, four broad Gaussian hills `(-175,-30,48,70,70)`, `(-100,-115,55,70,55)`, `(75,-130,48,110,60)`, `(95,135,65,90,70)`, descending `+X` valley corridor `20 < X < 220` down to `Z ≈ -24 m` along `Y ≈ 3 m`, and across-valley horizon ridge at `X ≈ 280 m`), build the joined `SITE_terrain_proxy` + surrounding `V05_TERRAIN` mesh with closed `-90 m` outer perimeter/underside skirt and exact garden-polygon boundary triangle splits (`MAT_V05_LAWN_BASE` inside `P0..P4`, `MAT_V05_MEADOW_BASE` outside), and expose `terrain_height_v05(x, y)` via barycentric/BVH lookup on the actual triangulation.
   - Deterministically hide `LANDSCAPE_hills_v04_1..4` (`hide_viewport = True`, `hide_render = True`) while keeping their datablocks intact.
   - Vertically re-ground all `1,200` `V04_FOREST_*` instances and `V04_YOUNG_02/03` onto `terrain_height_v05(x, y)` using their mesh minimum `Z`, existing scale, and `0.012 m` embedding (computed absolutely from mesh bounds, never cumulatively), keeping their `(X, Y)`, yaw, scale, meshes, and materials unchanged.
2. **Complete 5-vertex garden enclosure (`P0..P4`), closed gate (`V05_GATE_*`), and path slabs (`V05_PATH_slab_00..03`)**:
   - Use the verified convex polygon `P0(16.60, -8.62) -> P1(18.25, 1.00) -> P2(19.20, 15.50) -> P3(-15.50, 16.50) -> P4(-15.00, -7.80)` (`34.70 × 25.12 m`, `810.910 m²`).
   - Keep `P0 -> P1` (`26` `FENCE_post_proxy*` stakes and `2` `FENCE_rail_proxy*` rails) 100% untouched.
   - Build `V05_FENCE_*` stakes, corner/supporting anchors, and terrain-following rails along `P1 -> P2 -> P3 -> P4 -> P0` (sharing endpoint stakes at `P0`/`P1`, matching rail heights/endpoints, reusing `MAT_TIMBER_FENCE` and `_metric_uv(..., 'fence')` with `V03_endgrain`), plus the closed rustic gate `V05_GATE_*` centered at `(7.875, -8.393591772)` (`2.20 m` clear X opening `6.775..8.975`) and `4` concrete continuation slabs `V05_PATH_slab_00..03` at `X = 7.875`, `Y = -6.10, -6.70, -7.30, -7.90`, `Z = 0.055`, `[2.1, 0.55, 0.11]` (`MAT_CONCRETE`).
3. Run **Preview 1** (inexpensive low-sample check of `site_overview` and `valley_from_inside` into `work/`) to verify continuous 3D terrain, unblocked `+X` valley sightline through the glazed gable, and closed fence/gate connectivity before scattering full vegetation.

## Milestone 2 — `Grass005` PBR Turf Base, Pilot Measurement, Forest Extension, and Lawn/Meadow Systems

1. **Acquire and verify `ambientCG Grass005` (`2K-JPG`)**:
   - Download `https://ambientcg.com/get?file=Grass005_2K-JPG.zip` into `work/downloads/Grass005/Grass005_2K-JPG.zip`, verify ZIP integrity and byte size (`39,523,019` B), and extract only `Grass005_2K-JPG_Color.jpg`, `Grass005_2K-JPG_Roughness.jpg`, and `Grass005_2K-JPG_NormalGL.jpg` into `assets/textures/grass/Grass005/`.
   - Build `MAT_V05_LAWN_BASE` and `MAT_V05_MEADOW_BASE` with world-space metric UVs, aperiodic translated secondary phase `(0.317, 0.419)` + noise blend, restrained Kysuce lawn/meadow grading, roughness `~0.80–0.98`, and `NormalGL` strength `0.35` (pack images and set relative paths `//../assets/textures/grass/Grass005/...`).
2. **Pilot sector measurement (before full population)**:
   - Measure the `8×8 m` lawn pilot, `20×20 m` meadow pilot, and `100`-tree forest sector as specified in Section 3 of `01_report_00.md`. Record unique evaluated triangles, instance-expanded triangles, and projected RSS/file size. Apply your plan's density/LOD lever if needed so full scene stays well below `< 1.5 M` target (`< 3.0 M` ceiling) unique evaluated triangles, `< 90 MiB` `.blend` file size, and `< 3.0 GiB` render RSS.
3. **Populate `V05_FOREST_*` (`1,200` linked placements), `4–10 cm` short-lawn system, and `25–65 cm` tall-meadow system**:
   - Scatter `1,200` linked `V05_FOREST_*` spruces (west `300`, south `350`, northeast `300`, valley flanks `250`, 65% `Picea mariana` / 35% `Picea abies`, mostly `LOD1` with every 12th within `60 m` using `LOD0`), keeping the `+X` valley corridor (`20 < X < 220, |Y - 3| < width + 10`) and garden + `8 m` buffer clear.
   - Build the `V05_MASTER_LAWN_PATCH_*` masters (`4–10 cm` tapered, curved blades with green/olive/thatch variation on dedicated V05 materials) and instance them across all `8×8 m` garden chunks (plus `0.125 m` boundary patches) using Geometry Nodes point-cloud instancers or linked-mesh chunk instancing, grounded on `terrain_height_v05(x, y)` with `3 mm` embedding. Hide interior `V04_EDGE_GRASS_*` instances (`hide_viewport = True`, `hide_render = True`) while keeping suitable exterior tufts.
   - Build the `V05_MASTER_MEADOW_CLUSTER_*` masters (`25–65 cm` unmown clumps/stems/seed heads derived from copied `grass_medium_01` meshes using dedicated `MAT_V05_MEADOW_GREEN` and `MAT_V05_MEADOW_DRY` materials) and scatter them outside the garden polygon, in front of the foreground fence, along the descending `+X` valley foreground (`20 < X < 140`), and along forest-edge meadows/glades.
   - Enforce all hard-surface clearance masks (`BASE_slab`, `PORCH_paving*`, `ENTRY_step_1..3`, all 12 path slabs, `BED_entry`, fence posts + `0.15 m`, and gate opening/inward swing/approach).
4. Run **Preview 2** (and at most **one** focused correction if a concrete visual or clearance defect is observed).

## Milestone 3 — Final Save, Multi-View Render Deliverables, Cold Reopen / Replay Verification, and Documentation

1. **Pack and save `blender/kysucka_chata_mcp_v05.blend`**:
   - Ensure all off-scene master collections (`16` `V04_MASTER_*` plus all `V05_MASTER_*` collections and baseline mesh snapshot) and preserved materials (`MAT_GRASS`, `MAT_SOIL`, `MAT_V04_LAWN`, `MAT_V04_MEADOW`) have `use_fake_user = True`.
   - Pack all file images (`bpy.ops.file.pack_all()`) and normalize image filepaths to portable blend-relative paths (`//../assets/...` and `//../reference/...`).
   - Restore `scene.camera = bpy.data.objects['CAM_A_REFERENCE']`, call `configure_comparison_render(scene)` (`1448 × 1086`, Cycles CPU, 8 threads, 96 samples, OIDN ON, seed 0, frame 0, AgX/None, exposure 0, gamma 1, output `//../work/camera_a.png`), set 3D viewport to `CAMERA` perspective, and save `/home/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v05.blend` (`compress=True`). Verify file size `< 90 MiB` (`< 94,371,840` B).
2. **Render the required Meta deliverables** (one render job at a time, restoring `CAM_A_REFERENCE` and saving `v05.blend` if any camera/resolution setting was toggled during auxiliary renders, or rendering auxiliary views before the final `v05.blend` save):
   - `renders/before.png`: `1448 × 1086`, 96 samples, OIDN ON (rendered in Step 0 from untouched `v04`).
   - `renders/after.png`: `1448 × 1086`, 96 samples, OIDN ON from `CAM_A_REFERENCE` on `v05`.
   - `renders/site_overview.png`: `1448 × 1086`, 64 samples, OIDN ON from `CAM_V05_OVERVIEW` (`[52, -60, 58] -> [2, 3, 0]`, `35 mm`).
   - `renders/valley_from_inside.png`: `1448 × 1086`, 96 samples, OIDN ON from `CAM_V05_VALLEY_INSIDE` (`[12.2, 3.2, 2.0] -> [65, 3.2, 1.35]`, `30 mm`, `1.55 m` above `floor_z = 0.45 m`, through unchanged `G01_lower_glass` / `G02_upper_glass`).
   - `renders/orbit_sheet.png`: `2 × 2` labelled composite (`1448 × 1134`) from `CAM_V05_ORBIT_NE/NW/SW/SE` (`[42,38,24]`, `[-40,38,24]`, `[-40,-34,24]`, `[42,-34,24] -> [2,3,2]`, `35 mm`, each `724 × 543`, 32 samples, OIDN ON).
   - `renders/grass_details.png`: native-pixel comparison/detail sheet combining (a) 1:1 native-pixel `Pred (v04)` vs `Po (v05)` crops from `before.png` and `after.png` across the exposed garden lawn and foreground fence/meadow transition (proving main-render improvement) and (b) 1:1 native-pixel close-up crops from the dedicated lawn detail (`[11, -6, 0.24] -> [10.2, -4.2, 0]`, `55 mm`, `1024 × 768`, 64 samples) and tall-meadow detail (`[23, -6, 0.65] -> [25, -4, 0.22]`, `50 mm`, `1024 × 768`, 64 samples) views, with exact source views and `[x0, y0, x1, y1]` crop bounds recorded.
3. **Cold CLI reopen, factory-startup source replay, and idempotence verification**:
   - Wire `from site_v05 import apply_v05` into `scripts/build_scene.py` right after `apply_v04` (asserting `random.getstate()` unchanged before/after `apply_v05`) and before `bpy.ops.file.pack_all()` / `save_as_mainfile`.
   - In separate `/home/agile/Applications/Blender/blender --background --disable-autoexec` CLI processes:
     1. Cold-reopen `blender/kysucka_chata_mcp_v05.blend` and verify zero missing libraries/images, `0.0` protected witness error, closed terrain/enclosure, clear sightline, and zero clearance violations.
     2. Run factory-startup source replay:
        ```bash
        /home/agile/Applications/Blender/blender --background --factory-startup --disable-autoexec --python-exit-code 2 --python /home/agile/Projects/kysucka_moderna_chata/scripts/build_scene.py -- --output /home/agile/Projects/kysucka_moderna_chata/work/v05_source_replay.blend
        ```
        Compare `work/v05_source_replay.blend` against `blender/kysucka_chata_mcp_v05.blend` across all semantic scene data (geometry/bounds/root positions `≤ 1e-5 m`, rotations `≤ 1e-6 rad`, scales/UVs/shader floats `≤ 1e-6`, exact object/instance counts, topology, material assignments, and image hashes) and verify that invoking `apply_v05(scene, P, ROOT)` a second time produces `0` semantic drift.
4. **Update documentation, Meta evidence, and `00_RUN_MAP.md`**:
   - Update `assets/ASSET_MANIFEST.md`, `AGENTS.md` (preserving the managed AP block and the entire `Closure and Git gates` section byte-identical to `HEAD`), `README_SK.md`, and `docs/OPERATIONS.md` with exact v05 facts and SHA-256 hashes.
   - Write `renders/render_metadata.json`, `evidence/site_comparison.md` (in Slovak), and `projects/kysucka_moderna_chata/00/00_RUN_MAP.md`. Note in your report that `projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/renders/render_metadata.json` requires `git add -f` when Michal stages Meta.
   - Verify `./.ap/ap doctor` passes and live Blender has `blender/kysucka_chata_mcp_v05.blend` open, saved (`is_saved == True`, `is_dirty == False`), idle (`render_running == False`), with `CAM_A_REFERENCE` active.

## Execution Route, Trace, and Authority Summary

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16 (live Blender 5.3.0 MCP on `127.0.0.1:9876` for scene refinement, checkpoints, renders, packing, and `v05.blend` save, supplemented by `/home/agile/Applications/Blender/blender --background` in separate CLI processes for cold reopen and `work/v05_source_replay.blend` verification).

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 00/05-spatial-site-valley-and-grass
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Git authority:
- Only `git submodule update --init --checkout .ap` in `/home/agile/Projects/kysucka_moderna_chata` is authorized; all other Git operations (`git add`, `git commit`, `git push`, `git reset`, `git checkout`, `git clean`) are prohibited in both repositories during `01/02`.

Network authority:
- Localhost Blender MCP (`127.0.0.1:9876`), GitHub submodule fetch for `.ap` (`d7023cf037f6d17885c3ede5c04812c61640da50`), and official `ambientCG` download for `Grass005` (`https://ambientcg.com/api/v2/full_json?id=Grass005&include=downloadData` / `https://ambientcg.com/get?file=Grass005_2K-JPG.zip` or `1K-JPG.zip`).

Evidence tier: E2
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor`
Affected tests: cold CLI reopen of `blender/kysucka_chata_mcp_v05.blend` and factory-startup source replay `work/v05_source_replay.blend` + second-call `apply_v05` idempotence check
New causal regression: deterministic `v05` witness-preservation, polygon/enclosure, clearance-mask, sightline, semantic-replay, and idempotence verification
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` + isolated CLI Blender 5.3.0 processes
Independent acceptance: not-required

## Completion and Report Contract

Finalize your complete terminal report in English starting with `### Report for ORCHESTRATOR_CHAT`, echoing:
- `Logical whole identity: kysucka-moderna-chata-spatial-site-valley-and-grass`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 02`

Use `status: PASS` (when all milestones and checks pass), `Phase-qualified result: implementation-PASS`, `Start commit: f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`, `End commit: f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`, `Report justification: new-mutation`, and `Logical-whole closure: not-closed`. Save the report to `/home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/01_report_01.md`, read it back completely to verify its first line, coordinates, and full content, and then return a short completion notice with status, path, and SHA-256.
